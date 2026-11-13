# /// script
# requires-python = ">=3.10"
# dependencies = ["pymupdf"]
# ///
"""Build deliverable/visualprofile/overview.pdf: one page per deliverable of the visual profile.

Usage (from the project root):
    uv run src/build_visualprofile_overview.py [-o out.pdf]

Every page is A4 landscape with a small title in the profile font and a grid of pages from one deliverable
(profile manual, CV, business card, presentation, A4 document/letter), placed as vector pages with
PyMuPDF's show_pdf_page, so nothing is rasterised. The profile font is read from the licensed zip in the
repo and embedded (embedding in PDF is allowed by the licence); no installed font is used.
Build the deliverables first: the sheet shows their current PDFs.
"""
from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
VP = ROOT / "deliverable" / "visualprofile"
FONT_ZIP = (ROOT / "background" / "visualprofile" / "Fonts" / "Non Natural Grotesk" / "Desktop variant"
            / "NonNaturalGroteskFontFamily-hqlqfp.zip")
MM = 72 / 25.4
PAGE_W, PAGE_H = 297 * MM, 210 * MM
MARGIN = 14 * MM
GREY = (0xE8 / 255, 0xE7 / 255, 0xE6 / 255)
MUTED = (0x66 / 255, 0x66 / 255, 0x66 / 255)

# (title, note, [(pdf relative to visualprofile/, page index, use trim box)], columns)
SHEETS = [
    ("Profilmanual", "40 sider, 16:9. Omslag, innhold, farger og bruk av seismografen.",
     [("profile/profile-manual.pdf", 0, False), ("profile/profile-manual.pdf", 1, False),
      ("profile/profile-manual.pdf", 12, False), ("profile/profile-manual.pdf", 23, False)], 2),
    ("CV", "Markdown → PDF. Eksempelet: forside, første side med prosjekter og siste side med «Generelt».",
     [("cv/cv-example.pdf", 0, False), ("cv/cv-example.pdf", 1, False), ("cv/cv-example.pdf", 3, False)], 3),
    ("Visittkort", "85 × 55 mm, trykk-PDF i CMYK med utfallende kant. Forside og bakside.",
     [("business-card/business-card-example.pdf", 0, True), ("business-card/business-card-example.pdf", 1, True)], 2),
    ("Presentasjon", "16:9. Åpning, innhold, seksjonsskille og avslutning.",
     [("presentation/example.pdf", 0, False), ("presentation/example.pdf", 2, False),
      ("presentation/example.pdf", 5, False), ("presentation/example.pdf", 13, False)], 2),
    ("Dokument og brev", "A4. Brev og utlysning av konsulentoppdrag, med samme rutenett som CV-en.",
     [("document/example-letter.pdf", 0, False), ("document/example-job-posting.pdf", 0, False),
      ("document/example-job-posting.pdf", 1, False)], 3),
]


def profile_font(name: str) -> bytes:
    with zipfile.ZipFile(FONT_ZIP) as z:
        for n in z.namelist():
            if n.endswith(f"/{name}.otf") or n == f"{name}.otf":
                return z.read(n)
    raise SystemExit(f"{name}.otf not found in {FONT_ZIP}")


def place_grid(page: pymupdf.Page, items: list, cols: int, top: float) -> None:
    sources = [(pymupdf.open(VP / rel), idx, trim) for rel, idx, trim in items]
    rows = (len(sources) + cols - 1) // cols
    gap = 6 * MM
    cell_w = (PAGE_W - 2 * MARGIN - (cols - 1) * gap) / cols
    cell_h = (PAGE_H - top - MARGIN - (rows - 1) * gap) / rows
    for k, (doc, idx, trim) in enumerate(sources):
        r, c = divmod(k, cols)
        src = doc[idx]
        clip = src.trimbox if trim else src.rect
        scale = min(cell_w / clip.width, cell_h / clip.height)
        w, h = clip.width * scale, clip.height * scale
        x0 = MARGIN + c * (cell_w + gap) + (cell_w - w) / 2
        y0 = top + r * (cell_h + gap) + (cell_h - h) / 2
        target = pymupdf.Rect(x0, y0, x0 + w, y0 + h)
        page.draw_rect(target + (-0.6, -0.6, 0.6, 0.6), color=GREY, width=0.6)
        page.show_pdf_page(target, doc, idx, clip=clip)


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="Build the overview sheet of the visual profile deliverables")
    ap.add_argument("-o", "--output", default=str(VP / "overview.pdf"), help="output PDF (default: %(default)s)")
    args = ap.parse_args()
    light, regular = profile_font("NON Natural Grotesk-Light"), profile_font("NON Natural Grotesk-Regular")
    missing = [rel for _, _, items, _ in SHEETS for rel, _, _ in items if not (VP / rel).is_file()]
    if missing:
        raise SystemExit("Build these deliverables first: " + ", ".join(sorted(set(missing))))
    out = pymupdf.open()
    for n, (title, note, items, cols) in enumerate(SHEETS, 1):
        page = out.new_page(width=PAGE_W, height=PAGE_H)
        page.insert_font(fontname="kwlight", fontbuffer=light)
        page.insert_font(fontname="kwregular", fontbuffer=regular)
        page.insert_text((MARGIN, MARGIN + 9 * MM), title, fontname="kwlight", fontsize=24)
        page.insert_text((MARGIN, MARGIN + 15 * MM), note, fontname="kwregular", fontsize=9, color=MUTED)
        page.insert_text((PAGE_W - MARGIN - 40 * MM, PAGE_H - 6 * MM), f"KodeWorks visuell profil  {n}/{len(SHEETS)}",
                         fontname="kwregular", fontsize=7, color=MUTED)
        place_grid(page, items, cols, top=MARGIN + 22 * MM)
    out.set_metadata({"title": "KodeWorks visuell profil – oversikt", "author": "KodeWorks"})
    out.save(args.output, garbage=3, deflate=True)
    print(f"Built {args.output} ({len(SHEETS)} pages)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
