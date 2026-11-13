# /// script
# requires-python = ">=3.10"
# dependencies = ["pymupdf"]
# ///
"""Build a KodeWorks presentation: pandoc Markdown -> beamer -> lualatex -> PDF.

Usage:
    uv run build_presentation.py deck.md [-o deck.pdf] [--theme-dir DIR] [--notes] [--keep-build]

Works from any directory (project root included). Paths to images in the Markdown are
relative to the Markdown file. Everything is assembled in a temporary build folder:
  1. the theme folder (filter.lua, beamerthemekodeworks.sty, optional template.tex) is copied in;
  2. the Non Natural Grotesk OTFs are unpacked from the licensed font zip into the build
     folder (never installed, never copied into the repo; the folder is deleted afterwards);
  3. kernfix.json -> kernfix.lua (kerning repairs), SVG assets -> vector PDF with PyMuPDF
     (plus recoloured variants of every *-svart asset), paths.tex is written;
  4. pandoc -> deck.tex, lualatex twice, PDF copied out.
Theme contract: the .sty must \\input{paths.tex} (defines \\kwfontdir, \\kwassetdir and a
\\graphicspath to the Markdown folder) and may \\directlua{dofile("kernfix.lua")}; features
kwfr/kwfl/kwfm are defined there. Fonts are in <build>/fonts/, vector assets in <build>/assets/.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

import pymupdf
from project_tmp import mkdtemp  # work folders in <project root>/tmp/ (CLAUDE.md)

HERE = Path(__file__).resolve().parent
FONT_ZIP_REL = Path("background/visualprofile/Fonts/Non Natural Grotesk/Desktop variant/NonNaturalGroteskFontFamily-hqlqfp.zip")
PROFILE_REL = Path("deliverable/visualprofile/profile")
TIMEOUT = 115  # seconds per external command


def find_root() -> Path | None:
    """Locate the project root (has deliverable/visualprofile/profile) from script dir or cwd."""
    for start in (HERE, Path.cwd()):
        for p in (start, *start.parents):
            if (p / PROFILE_REL / "colors.json").exists():
                return p
    return None


def die(msg: str) -> None:
    sys.stderr.write(f"\nERROR: {msg}\n")
    raise SystemExit(1)


def run(cmd: list[str], cwd: Path, what: str) -> subprocess.CompletedProcess:
    # max_print_line: keep TeX from wrapping log lines at 79 characters, so warnings with
    # long slide titles can be read back from the log in one piece.
    env = {**os.environ, "max_print_line": "10000"}
    try:
        return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8",
                              errors="replace", timeout=TIMEOUT, env=env)
    except FileNotFoundError:
        die(f"Program not found: «{cmd[0]}». Install it and make sure it is on PATH.")
    except subprocess.TimeoutExpired:
        die(f"{what} took more than {TIMEOUT} seconds and was stopped (the first lualatex run "
            "builds the font cache and can be slow; run again).")


# ---------------------------------------------------------------- assets and fonts

def extract_fonts(zip_path: Path, out: Path) -> None:
    out.mkdir(parents=True, exist_ok=True)
    try:
        with zipfile.ZipFile(zip_path) as z:
            for name in z.namelist():
                if name.lower().endswith(".otf") and "__MACOSX" not in name:
                    (out / Path(name).name).write_bytes(z.read(name))
    except zipfile.BadZipFile:
        die(f"The font file is not a valid zip: {zip_path}")
    if not any(out.glob("*.otf")):
        die(f"No .otf files found in {zip_path}")


def write_kernfix(src_json: Path, out: Path) -> None:
    fixes = json.loads(src_json.read_text(encoding="utf-8"))
    lua = []
    for face, pairs in fixes.items():
        data: dict[int, dict[int, int]] = {}
        for pair, val in pairs.items():
            data.setdefault(ord(pair[0]), {})[ord(pair[1])] = val
        body = ",".join(f"[{a}]={{" + ",".join(f"[{c}]={v}" for c, v in d.items()) + "}" for a, d in data.items())
        lua.append(f'fonts.handlers.otf.addfeature{{name="kwf{face[0].lower()}",type="kern",data={{{body}}}}}')
    out.write_text("\n".join(lua) + "\n", encoding="utf-8")


def recolour(svg: str, hexcol: str) -> str:
    def fix(m: re.Match) -> str:
        tag = re.sub(r'\s(class|fill|style)="[^"]*"', "", m.group(0))
        return tag.replace("<path", f'<path fill="#{hexcol}"', 1)
    return re.sub(r"<path\b[^>]*>", fix, svg)


def svg_to_pdf(svg: str) -> bytes:
    return pymupdf.open(stream=svg.encode("utf-8"), filetype="svg").convert_to_pdf()


def build_assets(profile: Path, out: Path) -> None:
    """Copy ready vector PDFs; convert SVGs lacking a PDF; add recoloured variants of *-svart assets
    (name: <stem without -svart>-<colour id>.pdf, e.g. kw-navnetrekk-deepgreen.pdf; plus the alias
    -mork-gronn for the dark green #35664C used on dividers in the manual)."""
    out.mkdir(parents=True, exist_ok=True)
    pdf_dir = profile / "assets" / "pdf"
    if pdf_dir.is_dir():
        for p in pdf_dir.glob("*.pdf"):
            shutil.copyfile(p, out / p.name)
    colors = {c["id"]: c["hex"].lstrip("#") for c in
              json.loads((profile / "colors.json").read_text(encoding="utf-8"))["colors"]}
    for svg_path in sorted((profile / "assets").glob("*.svg")):
        text = svg_path.read_text(encoding="utf-8")
        if not (out / f"{svg_path.stem}.pdf").exists():
            (out / f"{svg_path.stem}.pdf").write_bytes(svg_to_pdf(text))
        if svg_path.stem.endswith("-svart"):
            base = svg_path.stem[:-len("-svart")]
            for cid in ("white", "green", "darkgreen", "deepgreen", "grey"):
                target = out / f"{base}-{cid}.pdf"
                if not target.exists():
                    target.write_bytes(svg_to_pdf(recolour(text, colors[cid])))
            (out / f"{base}-mork-gronn.pdf").write_bytes(svg_to_pdf(recolour(text, colors["darkgreen"])))


# ---------------------------------------------------------------- pre-flight on the Markdown

IMG_RE = re.compile(r"!\[[^\]]*\]\(\s*<?([^)\s>]+)")


def check_markdown(md: Path) -> None:
    text = md.read_text(encoding="utf-8")
    # Blank out fenced code blocks and inline code (same length, so line numbers stay right):
    # image syntax shown as an example in a code span is not an image.
    blank = lambda m: re.sub(r"[^\n]", " ", m.group(0))
    text = re.sub(r"(?ms)^(```|~~~).*?^\1", blank, text)
    text = re.sub(r"`[^`\n]+`", blank, text)
    if not text.lstrip().startswith("---"):
        print("WARNING: the file has no YAML header (title, subtitle, author, date); the title slide will be empty.")
    missing = []
    for m in IMG_RE.finditer(text):
        ref = m.group(1)
        if re.match(r"^[a-z]+://", ref):
            continue
        if ref.lower().endswith(".svg"):
            print(f"WARNING: {ref} is SVG; lualatex needs PDF/PNG/JPG. Convert the SVG to PDF first.")
        if not (md.parent / ref).exists():
            line = text[:m.start()].count("\n") + 1
            missing.append(f"  line {line}: {ref}")
    if missing:
        die("Images not found (paths are relative to the Markdown file):\n" + "\n".join(missing))


# ---------------------------------------------------------------- log analysis

def frame_index(tex: Path) -> list[tuple[int, str]]:
    """(line number, frame title) for every frame in deck.tex."""
    out = []
    lines = tex.read_text(encoding="utf-8", errors="replace").splitlines()
    for i, line in enumerate(lines, 1):
        if r"\begin{frame}" in line:
            window = " ".join(lines[i - 1:i + 6])
            m = re.search(r"\\frametitle\{(.*?)\}", window) or re.search(r"\\begin\{frame\}(?:\[[^\]]*\])?\{(.+?)\}", window)
            title = ""
            if m:
                title = re.sub(r"\\(?:text)?color\{[^}]*\}", "", m.group(1))
                title = re.sub(r"\\[a-zA-Z]+\*?|[{}]", " ", title)
                title = re.sub(r"\s+", " ", title).strip()
            out.append((i, title))
    return out


BOX_RE = re.compile(
    r"(?P<ship>\[(?P<pg>\d+)(?:\{[^}]*\})?[^\[\]]*\])|"
    r"(?P<kind>Overfull|Underfull) \\(?P<box>[hv])box \((?P<amt>[^)]*)\)(?P<rest>[^\n]*)")


def analyse_log(log: Path, tex: Path) -> list[str]:
    """Human-readable warnings for Overfull/Underfull boxes, with page and slide title."""
    text = log.read_text(encoding="utf-8", errors="replace")
    frames = frame_index(tex)
    warnings: list[str] = []
    page = 1
    seen = set()
    for m in BOX_RE.finditer(text):
        if m.group("ship"):
            page = int(m.group("pg")) + 1
            continue
        kind, box, amt, rest = m.group("kind"), m.group("box"), m.group("amt"), m.group("rest")
        if kind == "Underfull":
            b = re.search(r"badness (\d+)", amt + rest)
            if box == "h" or not b or int(b.group(1)) < 10000:
                continue  # underfull hboxes are routine in ragged text
        ln = re.search(r"lines? (\d+)", rest)
        title, where = "", ""
        if ln:
            n = int(ln.group(1))
            prev = [f for f in frames if f[0] <= n]
            title = prev[-1][1] if prev else ""
            where = f", deck.tex line {n}"
        key = (kind, box, amt, page, where)
        if key in seen:
            continue
        seen.add(key)
        what = {("Overfull", "h"): "line too wide (horizontal overflow)",
                ("Overfull", "v"): "content too tall (vertical overflow)",
                ("Underfull", "v"): "too little content vertically"}.get((kind, box), "layout warning")
        t = f" «{title}»" if title else ""
        warnings.append(f"WARNING: {what} ({kind} \\{box}box, {amt.strip()}) near page {page}{t}{where}")
    # Warnings issued by the theme itself (\PackageWarning{kodeworks}{...}); TeX wraps long
    # log lines, so join the continuation lines that start with "(kodeworks)".
    joined = re.sub(r"\n\(kodeworks\)\s*", " ", text)
    for m in re.finditer(r"Package kodeworks Warning: (.+?)(?: on input line \d+)?\.?\n", joined):
        msg = re.sub(r"\s+", " ", m.group(1)).strip()
        if msg not in seen:
            seen.add(msg)
            warnings.append(f"WARNING: {msg}")
    return warnings


def show_latex_error(log: Path) -> None:
    lines = log.read_text(encoding="utf-8", errors="replace").splitlines() if log.exists() else []
    shown = 0
    for i, line in enumerate(lines):
        if line.startswith("Here is how much"):
            break
        if line.startswith("!") or ("Error" in line and line.startswith(("Package", "Class"))):
            sys.stderr.write("\n".join(lines[i:i + 7]) + "\n---\n")
            shown += 1
            if shown >= 3:
                break
    if shown == 0:
        sys.stderr.write("\n".join(lines[-25:]) + "\n")
    blob = "\n".join(lines)
    if "fontspec" in blob and "cannot be found" in blob:
        sys.stderr.write("Hint: a font was not found; check that the theme loads fonts via \\kwfontdir.\n")
    if "File `paths.tex' not found" in blob:
        sys.stderr.write("Hint: the theme must \\input{paths.tex}.\n")


# ---------------------------------------------------------------- main

def main() -> None:
    for s in (sys.stdout, sys.stderr):
        s.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="Build a KodeWorks presentation (Markdown -> PDF)")
    ap.add_argument("deck", help="the Markdown file")
    ap.add_argument("-o", "--output", help="PDF file (default: next to the Markdown file)")
    ap.add_argument("--theme-dir", default=str(HERE / "presentation"), help="theme folder (default: presentation/ next to the script)")
    ap.add_argument("--notes", action="store_true", help="include speaker notes as separate pages")
    ap.add_argument("--keep-build", action="store_true", help="keep the build folder (contains unpacked fonts) and print its path")
    ap.add_argument("--fonts-zip", help="font zip (default: found via the project root)")
    ap.add_argument("--profile-dir", help="folder with colors.json and assets/ (default: via the project root)")
    args = ap.parse_args()

    md = Path(args.deck).resolve()
    if not md.is_file():
        die(f"Markdown file not found: {md}")
    theme = Path(args.theme_dir).resolve()
    if not (theme / "filter.lua").is_file():
        die(f"The theme folder {theme} has no filter.lua.")
    sty = sorted(theme.glob("beamertheme*.sty"))
    if not sty:
        die(f"The theme folder {theme} has no beamertheme*.sty.")
    theme_name = sty[0].stem[len("beamertheme"):]

    root = find_root()
    profile = Path(args.profile_dir).resolve() if args.profile_dir else (root / PROFILE_REL if root else None)
    zip_path = Path(args.fonts_zip).resolve() if args.fonts_zip else (root / FONT_ZIP_REL if root else None)
    if profile is None or not (profile / "colors.json").exists():
        die("Profile folder not found (colors.json, assets/). Use --profile-dir.")
    if zip_path is None or not zip_path.is_file():
        die("The licensed font zip was not found. Use --fonts-zip (the font is unpacked temporarily, never installed).")
    for tool in ("pandoc", "lualatex"):
        if not shutil.which(tool):
            die(f"«{tool}» is not on PATH.")

    check_markdown(md)
    # The notes version gets its own name, so it never overwrites the PDF that is sent out.
    default_pdf = md.with_name(md.stem + ("-notater.pdf" if args.notes else ".pdf"))
    out_pdf = Path(args.output).resolve() if args.output else default_pdf
    candidates = [theme / "kernfix.json", HERE / "kernfix.json"]
    if root:
        candidates.append(root / "src/profile_manual/kernfix.json")
    kernfix_src = next((p for p in candidates if p.exists()), None)
    if kernfix_src is None:
        die("kernfix.json not found.")

    work = mkdtemp("kwdeck_")
    try:
        for p in theme.iterdir():
            if p.is_file():
                shutil.copyfile(p, work / p.name)
            elif p.is_dir():
                shutil.copytree(p, work / p.name)
        extract_fonts(zip_path, work / "fonts")
        write_kernfix(kernfix_src, work / "kernfix.lua")
        build_assets(profile, work / "assets")
        (work / "paths.tex").write_text(
            f"\\def\\kwfontdir{{{(work / 'fonts').as_posix()}/}}\n"
            f"\\def\\kwassetdir{{{(work / 'assets').as_posix()}/}}\n"
            f"\\graphicspath{{{{{md.parent.as_posix()}/}}{{{(work / 'assets').as_posix()}/}}}}\n", encoding="utf-8")
        (work / "build-options.tex").write_text(
            "\\setbeameroption{show notes}\n" if args.notes else "% no notes\n", encoding="utf-8")

        cmd = ["pandoc", str(md), "-f", "markdown", "-t", "beamer", "--slide-level=2",
               "--lua-filter", "filter.lua", "-V", f"theme={theme_name}",
               "-V", "lang=nb-NO", "--include-in-header", "build-options.tex",
               "--resource-path", str(md.parent), "-o", "deck.tex"]
        if (work / "template.tex").is_file():
            cmd += ["--template", "template.tex"]
        res = run(cmd, work, "pandoc")
        if res.returncode != 0:
            sys.stderr.write(res.stderr)
            die("pandoc failed (see the message above; check the YAML header and the Markdown syntax).")
        if res.stderr.strip():
            print("pandoc:", res.stderr.strip())

        for n in (1, 2):
            res = run(["lualatex", "-interaction=nonstopmode", "-halt-on-error", "deck.tex"], work,
                      f"lualatex (run {n})")
            if res.returncode != 0:
                show_latex_error(work / "deck.log")
                die(f"lualatex failed in run {n}. See the lines above.")
        warnings = analyse_log(work / "deck.log", work / "deck.tex")
        out_pdf.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(work / "deck.pdf", out_pdf)
        with pymupdf.open(out_pdf) as doc:
            npages = doc.page_count
        print(f"Built {out_pdf} ({npages} pages)")
        if warnings:
            print(f"\n{len(warnings)} layout warning(s) from lualatex:")
            for w in warnings:
                print("  " + w)
        else:
            print("No Overfull/Underfull warnings.")
    finally:
        if args.keep_build:
            print(f"Build folder kept (contains unpacked fonts; delete it when done): {work}")
        else:
            shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    main()
