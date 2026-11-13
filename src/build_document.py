# /// script
# requires-python = ">=3.10"
# dependencies = ["pymupdf"]
# ///
"""Build a KodeWorks A4 document (letter or document variant): Markdown -> pandoc -> lualatex -> PDF.

Usage (from the project root):
    uv run src/build_document.py doc.md [-o out.pdf] [--style-dir DIR] [--keep-build]

Style folder (default: document/ next to this script) holds template.tex, kwdocument.sty and filter.lua.
Everything is assembled in a temporary build folder: the style files are copied in, the Non Natural Grotesk
OTFs are unpacked from the licensed zip (never installed, never copied into the repo), kernfix.json becomes
kernfix.lua, the vector assets are written as PDF, font_guard enforces that no OS fonts are used. pandoc
(with filter.lua) writes doc.tex, lualatex runs twice. The build folder is always deleted afterwards.
Warnings are printed in Norwegian with the offending text.
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
from pathlib import Path
from project_tmp import mkdtemp  # work folders in <project root>/tmp/ (CLAUDE.md)

HERE = Path(__file__).resolve().parent


def _find_src() -> Path:
    """Folder that holds build_presentation.py (this folder, or <root>/src found from here or the cwd)."""
    for start in (HERE, Path.cwd()):
        for p in (start, *start.parents):
            for cand in (p, p / "src"):
                if (cand / "build_presentation.py").exists() and (cand / "font_guard.py").exists():
                    return cand
    raise SystemExit("ERROR: src/build_presentation.py not found. Run from the project root.")


SRC = _find_src()
sys.path.insert(0, str(SRC))
import font_guard  # noqa: E402
import pymupdf  # noqa: E402
from build_presentation import (FONT_ZIP_REL, PROFILE_REL, build_assets, die, extract_fonts,  # noqa: E402
                                find_root, run, show_latex_error, write_kernfix)

TEXMF_NOISE = ("Overfull \\hbox (0.", "Overfull \\hbox (1.0")


def read_log(log: Path) -> str:
    return log.read_text(encoding="utf-8", errors="replace") if log.exists() else ""


def tex_to_text(s: str) -> str:
    s = re.sub(r"\\(?:kw)?[A-Za-z]+\s?", " ", s)
    s = s.replace("[]", " ").replace("\\", " ")
    return re.sub(r"\s+", " ", s).strip()


def analyse_log(text: str) -> list[str]:
    """Warnings from the lualatex log: overfull boxes (with the text), missing glyphs, own warnings."""
    out: list[str] = []
    seen: set[str] = set()
    page = 1
    lines = text.splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"Overfull \\([hv])box \(([\d.]+)pt too (?:wide|high)\)(.*)", line)
        if m:
            kind, amt, rest = m.group(1), float(m.group(2)), m.group(3)
            if amt < 1.5 and kind == "h":
                continue
            snippet = ""
            for nxt in lines[i + 1:i + 4]:
                if nxt.strip():
                    snippet = tex_to_text(nxt)
                    break
            snippet = (snippet[:90] + "…") if len(snippet) > 90 else snippet
            if kind == "h":
                msg = (f"A line is {amt:.0f} pt too wide and runs into the margin: «{snippet}». "
                       "Break up a long word or link, or shorten the text.") if snippet else \
                    f"A line is {amt:.0f} pt too wide (table or column?)."
            else:
                msg = f"The content is {amt:.0f} pt too tall for the page: «{snippet}»."
            if msg not in seen:
                seen.add(msg)
                out.append(msg)
    for m in re.finditer(r"Missing character: There is no (.+?) \(U\+([0-9A-Fa-f]{4,6})\) in font ([^!\n]*)", text):
        msg = (f"The character «{m.group(1)}» (U+{m.group(2).upper()}) is not in the font and is left out. "
               "Replace it with a character the font has.")
        if msg not in seen:
            seen.add(msg)
            out.append(msg)
    return out


def check_pdf(pdf: Path) -> list[str]:
    """Checks on the finished PDF: no raster images, nothing outside the margins, no lone short word on a last line."""
    out: list[str] = []
    mm = 72 / 25.4
    with pymupdf.open(pdf) as doc:
        for pno, page in enumerate(doc, 1):
            if page.get_images(full=True):
                out.append(f"Page {pno} contains raster images; the template should have vector graphics only.")
            data = page.get_text("dict")
            for blk in data["blocks"]:
                if blk.get("type") != 0:
                    continue
                for ln in blk["lines"]:
                    x0, y0, x1, y1 = ln["bbox"]
                    txt = "".join(s["text"] for s in ln["spans"]).strip()
                    if x1 > page.rect.width - 18 * mm or x0 < 18 * mm:
                        out.append(f"Page {pno}: the text «{txt[:60]}» lies outside the margin.")
                blines = blk["lines"]
                if len(blines) >= 3 and 36 * mm < blk["bbox"][1] < page.rect.height - 40 * mm and blk["bbox"][0] < 21 * mm and blk["bbox"][2] - blk["bbox"][0] > 90 * mm:
                    first = blines[0]["spans"][0]["size"]
                    last = "".join(s["text"] for s in blines[-1]["spans"]).strip()
                    if first < 11.5 and " " not in last and 0 < len(last) <= 9 and not last.isupper() and not re.match(r"^[\d\W]", last):
                        out.append(f"Page {pno}: the paragraph ends with a single word on its last line («{last}»): "
                                   f"«{''.join(s['text'] for s in blines[0]['spans']).strip()[:40]}…». "
                                   "Rephrase the paragraph slightly.")
    return out


def main() -> None:
    for s in (sys.stdout, sys.stderr):
        s.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="Build a KodeWorks document or letter (Markdown -> PDF)")
    ap.add_argument("md", help="the Markdown file")
    ap.add_argument("-o", "--output", help="PDF file (default: next to the Markdown file)")
    ap.add_argument("--style-dir", default=str(HERE / "document"), help="style folder (default: document/ next to the script)")
    ap.add_argument("--keep-build", action="store_true", help="keep the build folder (contains licensed font files)")
    ap.add_argument("--fonts-zip", help="font zip (default: via the project root)")
    ap.add_argument("--profile-dir", help="folder with colors.json and assets/ (default: via the project root)")
    args = ap.parse_args()

    md = Path(args.md).resolve()
    if not md.is_file():
        die(f"Markdown file not found: {md}")
    style = Path(args.style_dir).resolve()
    for need in ("template.tex", "kwdocument.sty", "filter.lua"):
        if not (style / need).is_file():
            die(f"The style folder {style} has no {need}.")
    root = find_root()
    profile = Path(args.profile_dir).resolve() if args.profile_dir else (root / PROFILE_REL if root else None)
    zip_path = Path(args.fonts_zip).resolve() if args.fonts_zip else (root / FONT_ZIP_REL if root else None)
    if profile is None or not (profile / "colors.json").exists():
        die("Profile folder not found (colors.json, assets/). Use --profile-dir.")
    if zip_path is None or not zip_path.is_file():
        die("The licensed font zip was not found. Use --fonts-zip.")
    for tool in ("pandoc", "lualatex"):
        if not shutil.which(tool):
            die(f"«{tool}» is not on PATH.")
    kern_candidates = [style / "kernfix.json", SRC / "presentation" / "kernfix.json"]
    if root:
        kern_candidates += [root / "src/presentation/kernfix.json", root / "src/profile_manual/kernfix.json"]
    kernfix = next((p for p in kern_candidates if p.exists()), None)
    if kernfix is None:
        die("kernfix.json not found.")
    out_pdf = Path(args.output).resolve() if args.output else md.with_suffix(".pdf")

    work = mkdtemp("kwdoc_")
    warnings: list[str] = []
    try:
        for p in style.iterdir():
            if p.is_file():
                shutil.copyfile(p, work / p.name)
        extract_fonts(zip_path, work / "fonts")
        write_kernfix(kernfix, work / "kernfix.lua")
        build_assets(profile, work / "assets")
        font_guard.write_hook(work)
        (work / "paths.tex").write_text(
            f"\\def\\kwfontdir{{{(work / 'fonts').as_posix()}/}}\n"
            f"\\def\\kwassetdir{{{(work / 'assets').as_posix()}/}}\n"
            f"\\graphicspath{{{{{md.parent.as_posix()}/}}{{{(work / 'assets').as_posix()}/}}}}\n", encoding="utf-8")

        cmd = ["pandoc", str(md), "-f", "markdown", "-t", "latex", "--template", "template.tex",
               "--lua-filter", "filter.lua", "--resource-path", str(md.parent), "-o", "doc.tex"]
        res = run(cmd, work, "pandoc")
        if res.returncode != 0:
            sys.stderr.write(res.stderr)
            die("pandoc failed (see the message above; check the YAML header and the Markdown syntax).")
        for line in res.stderr.splitlines():
            if line.startswith("KWWARN: "):
                warnings.append(line[len("KWWARN: "):])
            elif line.startswith("KWINFO: "):
                print("INFO: " + line[len("KWINFO: "):])
            elif line.strip():
                print("pandoc:", line)

        for n in (1, 2):
            res = run(["lualatex", "-interaction=nonstopmode", "-halt-on-error", "doc.tex"], work,
                      f"lualatex (run {n})")
            if res.returncode != 0:
                show_latex_error(work / "doc.log")
                die(f"lualatex failed in run {n}. See the lines above.")
        font_guard.check(work)
        warnings += analyse_log(read_log(work / "doc.log"))
        out_pdf.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(work / "doc.pdf", out_pdf)
        warnings += check_pdf(out_pdf)
        with pymupdf.open(out_pdf) as d:
            npages = d.page_count
        print(f"Built {out_pdf} ({npages} {'page' if npages == 1 else 'pages'})")
        if warnings:
            print(f"\n{len(warnings)} warning(s):")
            for w in warnings:
                print("  WARNING: " + w)
        else:
            print("No warnings.")
    finally:
        if args.keep_build:
            print(f"WARNING: the build folder is kept and contains unpacked licensed font files; delete it when done: {work}")
        else:
            shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    main()
