# /// script
# requires-python = ">=3.10"
# dependencies = ["pymupdf"]
# ///
"""Build the KodeWorks identity manual (profilmanual): Markdown -> pandoc -> lualatex -> PDF.

Usage (from the project root):
    uv run src/build_profile_manual.py [manual.md] [--assets DIR] [--photos DIR] [--fonts-zip ZIP]

Defaults build deliverable/visualprofile/profile/profilmanual.md into profilmanual.pdf next to it.

The layout system (LaTeX template, page types, components, palette) lives in src/profile_manual/.
Everything is assembled in a temporary build folder, so nothing but the PDF is written:
  1. copy the support files; extract the Non Natural Grotesk OTFs from the licensed font zip
     (loaded with fontspec Path=, no installation; the licence permits embedding in PDF);
  2. convert every SVG in the assets folder to PDF with PyMuPDF (rsvg-convert is not needed),
     plus a few recoloured helper variants (EXTRA) with colours from colors.tex;
  3. copy the photos to photos/; resolve '<!-- include: file.md -->' lines;
  4. pandoc (filter.lua + template.tex) -> .tex; lualatex twice (TikZ remember picture, page refs).
     lualatex (not xelatex) because it loads the Norwegian bokmål hyphenation patterns at run
     time; the installed xelatex format has none and silently falls back to English patterns.
"""
import argparse
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

import pymupdf

import font_guard  # src/font_guard.py: fail if a font comes from the OS instead of the repo/TeX Live
from project_tmp import work_dir  # work folders in <project root>/tmp/ (CLAUDE.md)

ROOT = Path(__file__).resolve().parent.parent
SUPPORT = ROOT / "src" / "profile_manual"
SUPPORT_FILES = ["template.tex", "colors.tex", "fonts.tex", "layout.tex", "filter.lua"]
PROFILE = ROOT / "deliverable" / "visualprofile" / "profile"
DEFAULT_FONTS_ZIP = (ROOT / "background" / "visualprofile" / "Fonts" / "Non Natural Grotesk"
                     / "Desktop variant" / "NonNaturalGroteskFontFamily-hqlqfp.zip")
# Stand-in for Arial on the fallback examples (same advance widths); ships with every TeX Live.
TEXLIVE_FONTS = ["texgyreheros-regular.otf"]

# helper variants: output stem -> (source stem, colour name from colors.tex)
# The *mork-gronn* pattern is used on dividers; the x-* files exist only for misuse examples.
EXTRA = {
    "femte-element-mork-gronn": ("femte-element-svart", "kwdarkgreen"),
    "femte-element-hvit": ("femte-element-svart", "kwwhite"),
    "x-navnetrekk-skygge": ("kw-navnetrekk-svart", "kwshadow"),
    "x-navnetrekk-mork-gronn": ("kw-navnetrekk-svart", "kwdarkgreen"),
    "x-symbol-skygge": ("kw-symbol-svart", "kwshadow"),
}


def read_colors(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    return {m[0]: m[1] for m in re.findall(r"\\definecolor\{(\w+)\}\{HTML\}\{([0-9A-Fa-f]{6})\}", text)}


def recolour(svg: str, hexcol: str) -> str:
    """Force a single fill on every path (drops class/fill/style so no renderer can ignore it)."""
    def fix(m: re.Match) -> str:
        tag = re.sub(r'\s(class|fill|style)="[^"]*"', "", m.group(0))
        return tag.replace("<path", f'<path fill="#{hexcol}"', 1)
    return re.sub(r"<path\b[^>]*>", fix, svg)


def svg_to_pdf(svg: str) -> bytes:
    return pymupdf.open(stream=svg.encode("utf-8"), filetype="svg").convert_to_pdf()


def convert_svgs(assets: Path, out: Path, colors: dict[str, str]) -> None:
    out.mkdir(parents=True, exist_ok=True)
    for svg_path in sorted(assets.rglob("*.svg")):
        (out / f"{svg_path.stem}.pdf").write_bytes(svg_to_pdf(svg_path.read_text(encoding="utf-8")))
    for name, (stem, colour) in EXTRA.items():
        svg = recolour((assets / f"{stem}.svg").read_text(encoding="utf-8"), colors[colour])
        (out / f"{name}.pdf").write_bytes(svg_to_pdf(svg))


def extract_fonts(zip_path: Path, out: Path) -> None:
    """Profile font from the licensed zip, plus TEXLIVE_FONTS copied from the TeX distribution."""
    out.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path) as z:
        for name in z.namelist():
            if name.lower().endswith(".otf") and "__MACOSX" not in name:
                (out / Path(name).name).write_bytes(z.read(name))
    for name in TEXLIVE_FONTS:
        found = subprocess.run(["kpsewhich", name], capture_output=True, text=True).stdout.strip()
        if not found:
            raise SystemExit(f"{name} not found in TeX Live (kpsewhich)")
        shutil.copyfile(found, out / name)


def write_kernfix(out: Path) -> None:
    """kernfix.json (extra kern pairs per face, font units) -> kernfix.lua for luaotfload.

    Adds kern features kwfr/kwfl/kwfm (Regular/Light/Medium; OpenType tags must be 4 characters,
    longer names are ignored silently). Closes gaps the font leaves around j (sj, kj …) and r-f.
    Shared with src/build_cv_pdf.py; fonts.tex switches the features on.
    """
    import json
    fixes = json.loads((SUPPORT / "kernfix.json").read_text(encoding="utf-8"))
    lua = []
    for face, pairs in fixes.items():
        data: dict[int, dict[int, int]] = {}
        for pair, val in pairs.items():
            data.setdefault(ord(pair[0]), {})[ord(pair[1])] = val
        body = ",".join(f"[{a}]={{" + ",".join(f"[{c}]={v}" for c, v in d.items()) + "}" for a, d in data.items())
        lua.append(f'fonts.handlers.otf.addfeature{{name="kwf{face[0].lower()}",type="kern",data={{{body}}}}}')
    out.write_text("\n".join(lua) + "\n", encoding="utf-8")


def assemble(src: Path, dest: Path) -> None:
    """Resolve '<!-- include: file.md -->' lines (recursively) into one Markdown file."""
    def expand(path: Path) -> str:
        lines = []
        for line in path.read_text(encoding="utf-8").splitlines():
            m = re.match(r"\s*<!--\s*include:\s*(.+?)\s*-->\s*$", line)
            lines.append("\n" + expand(path.parent / m.group(1)) + "\n" if m else line)
        return "\n".join(lines)
    dest.write_text(expand(src), encoding="utf-8", newline="\n")


def run(cmd: list[str], cwd: Path) -> None:
    res = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if res.returncode != 0:
        sys.stderr.write(res.stdout[-3000:] + res.stderr[-2000:])
        raise SystemExit(f"command failed: {' '.join(cmd[:3])}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", nargs="?", default=str(PROFILE / "profilmanual.md"))
    ap.add_argument("--assets", default=str(PROFILE / "assets"), help="folder with the clean SVG assets")
    ap.add_argument("--photos", default=str(PROFILE / "images"), help="folder with photos used in the manual")
    ap.add_argument("--fonts-zip", default=str(DEFAULT_FONTS_ZIP), help="Non Natural Grotesk font zip")
    args = ap.parse_args()

    src = Path(args.source).resolve()
    with work_dir("kwmanual_") as tmp:
        work = Path(tmp)
        build = work / "build"
        build.mkdir()
        for name in SUPPORT_FILES:
            shutil.copyfile(SUPPORT / name, work / name)
        extract_fonts(Path(args.fonts_zip), work / "fonts")
        write_kernfix(work / "kernfix.lua")
        font_guard.write_hook(work)
        convert_svgs(Path(args.assets), build / "img", read_colors(SUPPORT / "colors.tex"))
        shutil.copytree(args.photos, work / "photos")
        (build / "paths.tex").write_text(
            f"\\def\\kwfontdir{{{(work / 'fonts').as_posix()}/}}\n\\def\\kwimgdir{{build/img}}\n",
            encoding="utf-8")

        assembled = build / f"{src.stem}.assembled.md"
        assemble(src, assembled)
        tex = build / f"{src.stem}.tex"
        run(["pandoc", str(assembled), "-f", "markdown+fenced_divs+raw_tex", "-t", "latex",
             "--template", "template.tex", "--lua-filter", "filter.lua", "-o", str(tex)], work)
        for _ in range(2):
            run(["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-output-directory=build",
                 f"build/{src.stem}.tex"], work)
        font_guard.check(work)
        pdf = src.with_suffix(".pdf")
        shutil.copyfile(build / f"{src.stem}.pdf", pdf)
    print(f"built {pdf}")


if __name__ == "__main__":
    main()
