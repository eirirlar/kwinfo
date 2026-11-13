# /// script
# dependencies = ["pymupdf"]
# ///
"""Build a PDF from a Markdown file produced by extract_visualprofile.py.

The .md and its media folder are left untouched. In a temporary build folder:
  1. every referenced SVG is converted to PDF with PyMuPDF (xelatex cannot embed SVG
     without rsvg-convert), and a temporary copy of the .md points to those PDFs;
  2. the copy is converted Markdown -> HTML -> LaTeX (pandoc) and set with lualatex. Going via
     HTML makes pandoc parse the raw HTML tables (rowspan/colspan from DOCX sources) instead of
     silently dropping them in the LaTeX writer.

Fonts are files from TeX Live (TeX Gyre Heros, which has Arial's advance widths, and DejaVu Sans
Mono), never fonts installed in the operating system; src/font_guard.py fails the build otherwise.
lualatex (not xelatex) because it loads the Norwegian bokmål hyphenation patterns.

Output: <same dir>/<same stem>.pdf

Usage (from project root):
    uv run src/build_md_pdf.py "background/new/2026-11-13_rapport.md"   # -> .pdf next to the .md
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import pymupdf

import font_guard  # src/font_guard.py
from project_tmp import work_dir  # work folders in <project root>/tmp/ (CLAUDE.md)

TEX_OPTS = [
    "-s",
    "-V", "documentclass=scrartcl",
    "-V", "geometry:margin=2cm",
    "-V", "lang=nb",
    "-V", "mainfont=texgyreheros-regular.otf",
    "-V", "mainfontoptions=BoldFont=texgyreheros-bold.otf, ItalicFont=texgyreheros-italic.otf, "
          "BoldItalicFont=texgyreheros-bolditalic.otf",
    "-V", "sansfont=texgyreheros-regular.otf",
    "-V", "sansfontoptions=BoldFont=texgyreheros-bold.otf, ItalicFont=texgyreheros-italic.otf, "
          "BoldItalicFont=texgyreheros-bolditalic.otf",
    "-V", "monofont=DejaVuSansMono.ttf",
]


def main() -> None:
    # Warnings may contain characters the Windows console code page cannot encode.
    sys.stdout.reconfigure(errors="replace")
    sys.stderr.reconfigure(errors="replace")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("markdown", type=Path)
    args = ap.parse_args()

    md: Path = args.markdown.resolve()
    out = md.with_suffix(".pdf")
    text = md.read_text(encoding="utf-8")

    with work_dir("kwmdpdf_") as tmp:
        tmp_dir = Path(tmp)

        def svg_to_pdf(m: re.Match) -> str:
            svg = md.parent / m.group(2)
            pdf = tmp_dir / (svg.stem + ".pdf")
            if not pdf.exists():
                with pymupdf.open(svg) as doc:
                    pdf.write_bytes(doc.convert_to_pdf())
            return m.group(1) + pdf.as_posix() + m.group(3)

        text = re.sub(r"(\]\()([^)\s]+\.svg)(\))", svg_to_pdf, text)
        build_md = tmp_dir / "build.md"
        build_md.write_text(text, encoding="utf-8", newline="\n")
        html = tmp_dir / "build.html"
        # Bare URLs become links, so LaTeX sets them with \url and does not hyphenate them away.
        subprocess.run(["pandoc", str(build_md), "-f", "markdown+autolink_bare_uris", "-t", "html",
                        "-o", str(html)], check=True)
        # Headings inside table cells become LaTeX run-in \paragraph, which is not printed at
        # all when nothing follows it in the cell. Turn them into bold paragraphs instead.
        page = html.read_text(encoding="utf-8")
        page = re.sub(r"<table.*?</table>",
                      lambda t: re.sub(r"<h[1-6][^>]*>(.*?)</h[1-6]>", r"<p><strong>\1</strong></p>",
                                       t.group(0), flags=re.S),
                      page, flags=re.S)
        html.write_text(page, encoding="utf-8", newline="\n")
        font_guard.write_hook(tmp_dir)
        tex = tmp_dir / "build.tex"
        res = subprocess.run(
            ["pandoc", str(html), "-f", "html", "-t", "latex", "-o", str(tex),
             "-H", str(tmp_dir / font_guard.HOOK_NAME), *TEX_OPTS],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
        )
        warnings = [l for l in res.stderr.splitlines() if l.strip()]
        # Images are referenced relative to the .md; let kpathsea find them there.
        env = dict(os.environ, TEXINPUTS=f"{md.parent}{os.pathsep}")
        for _ in range(2):
            if res.returncode != 0:
                break
            res = subprocess.run(["lualatex", "-interaction=nonstopmode", "-halt-on-error", "build.tex"],
                                 cwd=tmp_dir, env=env, capture_output=True, text=True,
                                 encoding="utf-8", errors="replace")
        if res.returncode != 0:
            print("\n".join(warnings) + res.stdout[-3000:], file=sys.stderr)
            sys.exit(f"FAILED: {md}")
        font_guard.check(tmp_dir)
        warnings += [l for l in res.stdout.splitlines() if "Warning" in l]
        shutil.copyfile(tmp_dir / "build.pdf", out)
    print(f"{out}  ({out.stat().st_size // 1024} KB, {len(warnings)} warnings)")
    for w in warnings[:5]:
        print("  " + w)


if __name__ == "__main__":
    main()
