# /// script
# requires-python = ">=3.10"
# dependencies = ["pymupdf"]
# ///
"""Export every SVG in the profile asset folder to PDF (vector) and PNG (transparent).

Usage (from the project root):
    uv run src/export_profile_assets.py [--assets DIR] [--png-size 2000]

For each <assets>/**/name.svg this writes <assets>/pdf/name.pdf and <assets>/png/name.png
(longest side --png-size px, transparent background). The SVGs stay the source of truth;
re-run after changing an SVG. Files in pdf/ and png/ are overwritten.
"""
import argparse
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_ASSETS = ROOT / "deliverable" / "visualprofile" / "profile" / "assets"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--assets", type=Path, default=DEFAULT_ASSETS)
    ap.add_argument("--png-size", type=int, default=2000, help="longest side of the PNG in pixels")
    args = ap.parse_args()

    pdf_dir, png_dir = args.assets / "pdf", args.assets / "png"
    pdf_dir.mkdir(exist_ok=True)
    png_dir.mkdir(exist_ok=True)
    svgs = sorted(p for p in args.assets.rglob("*.svg") if pdf_dir not in p.parents and png_dir not in p.parents)
    for svg in svgs:
        doc = pymupdf.open(svg)
        (pdf_dir / f"{svg.stem}.pdf").write_bytes(doc.convert_to_pdf())
        page = doc[0]
        zoom = args.png_size / max(page.rect.width, page.rect.height)
        page.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom), alpha=True).save(png_dir / f"{svg.stem}.png")
        print(f"{svg.name}: pdf + png")
    print(f"{len(svgs)} assets exported to {pdf_dir} and {png_dir}")


if __name__ == "__main__":
    main()
