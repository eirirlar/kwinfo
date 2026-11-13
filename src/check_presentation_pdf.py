# /// script
# requires-python = ">=3.10"
# dependencies = ["pymupdf"]
# ///
"""Check a finished KodeWorks presentation PDF. Prints PASS / WARN / FAIL per check.

Usage:
    uv run check_presentation_pdf.py deck.pdf [--colors colors.json] [--margin-mm 8]
        [--footer-mm 17] [--allow-empty 3,5] [--png-dir DIR]

Exit code 1 if any check FAILs. Checks:
  size      page size 338.67 x 190.5 mm (960 x 540 pt) on every page
  fonts     only NON Natural Grotesk, all embedded, no Thin/Bold (the pdffonts equivalent)
  images    raster images: logo-like (small, transparent, few colours, non-photo) = FAIL;
            photos under 150 dpi effective = WARN; every image is listed with size and dpi
  bounds    no text outside the page (FAIL) or inside the margin (WARN)
  footer    on white content slides no text but the page number in the footer band
  colors    fills, strokes and text colours belong to the palette in colors.json (WARN)
  empty     pages that are (nearly) empty (WARN), unless listed in --allow-empty
  textsize  text below 12 pt (WARN)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import pymupdf

HERE = Path(__file__).resolve().parent
MM = 72 / 25.4
PAGE_W, PAGE_H = 338.67 * MM, 190.5 * MM
PROFILE_REL = Path("deliverable/visualprofile/profile/colors.json")

WIDE = pymupdf.Rect(-5000, -5000, 5000, 5000)  # so text outside the page is still seen
results: list[tuple[str, str, str]] = []  # (status, check, message)


def add(status: str, check: str, msg: str) -> None:
    results.append((status, check, msg))


def find_colors(explicit: str | None) -> Path | None:
    if explicit:
        return Path(explicit)
    for start in (HERE, Path.cwd()):
        for p in (start, *start.parents):
            if (p / PROFILE_REL).exists():
                return p / PROFILE_REL
    return None


def load_palette(path: Path) -> dict[tuple[int, int, int], str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    pal = {}
    for c in data["colors"] + data.get("technical", []):
        h = c["hex"].lstrip("#")
        pal[tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))] = c["name"]
    return pal


def near_palette(rgb: tuple[int, int, int], pal: dict, tol: int = 2) -> bool:
    return any(all(abs(a - b) <= tol for a, b in zip(rgb, p)) for p in pal)


def to_rgb255(c) -> tuple[int, int, int] | None:
    if c is None:
        return None
    if isinstance(c, int):
        return (c >> 16) & 255, (c >> 8) & 255, c & 255
    if len(c) == 1:
        v = round(c[0] * 255)
        return v, v, v
    if len(c) == 3:
        return tuple(round(x * 255) for x in c)
    if len(c) == 4:  # cmyk
        k = c[3]
        return tuple(round(255 * (1 - min(1, x + k))) for x in c[:3])
    return None


def hexof(rgb) -> str:
    return "#%02X%02X%02X" % rgb


def pages_str(pages) -> str:
    p = sorted(set(pages))
    return ", ".join(map(str, p[:12])) + (" ..." if len(p) > 12 else "")


def check_size(doc) -> None:
    bad = []
    for i, page in enumerate(doc, 1):
        r = page.rect
        if abs(r.width - PAGE_W) > 1 or abs(r.height - PAGE_H) > 1:
            bad.append(f"page {i}: {r.width / MM:.2f} x {r.height / MM:.2f} mm")
    if bad:
        add("FAIL", "size", "wrong page size (expected 338.67 x 190.5 mm): " + "; ".join(bad[:5]))
    else:
        add("PASS", "size", f"all {doc.page_count} pages are 338.67 x 190.5 mm")


def check_fonts(doc) -> None:
    fonts = {}
    for i, page in enumerate(doc, 1):
        for xref, ext, ftype, basefont, name, enc in page.get_fonts():
            fonts.setdefault((basefont, ext, ftype), []).append(i)
    bad = False
    for (basefont, ext, ftype), pgs in sorted(fonts.items()):
        clean = basefont.split("+")[-1]
        embedded = ext not in ("n/a", "")
        norm = re.sub(r"[\s_-]", "", clean).lower()
        problems = []
        if "nonnaturalgrotesk" not in norm:
            problems.append("not NON Natural Grotesk")
        if not embedded:
            problems.append("not embedded")
        if re.search(r"thin|bold", norm):
            problems.append("Thin/Bold must not be used")
        status = "FAIL" if problems else "PASS"
        bad |= bool(problems)
        add(status, "fonts", f"{basefont} ({ftype}, {'embedded' if embedded else 'NOT embedded'}) page {pages_str(pgs)}"
            + (" - " + ", ".join(problems) if problems else ""))
    if not fonts:
        add("WARN", "fonts", "no fonts found (no text?)")


def check_images(doc) -> None:
    listed = 0
    flagged = False
    for i, page in enumerate(doc, 1):
        infos = page.get_image_info(xrefs=True)
        for info in infos:
            xref = info.get("xref", 0)
            w, h = info["width"], info["height"]
            bbox = pymupdf.Rect(info["bbox"])
            if bbox.width <= 0 or bbox.height <= 0:
                continue
            dpi = min(w / (bbox.width / 72), h / (bbox.height / 72))
            ext, has_alpha, ncolors = "?", False, None
            if xref:
                try:
                    ex = doc.extract_image(xref)
                    ext = ex.get("ext", "?")
                    has_alpha = bool(ex.get("smask"))
                except Exception:
                    pass
                try:
                    pix = pymupdf.Pixmap(doc, xref)
                    if pix.alpha:
                        has_alpha = True
                    if pix.width * pix.height <= 4_000_000:
                        ncolors = pix.color_count()
                except Exception:
                    pass
            reasons = []
            if min(w, h) < 400:
                reasons.append("small raster file")
            if has_alpha:
                reasons.append("transparent (logo-like)")
            if ncolors is not None and ncolors < 256:
                reasons.append(f"only {ncolors} colours (logo/fill)")
            if ext not in ("jpeg", "jpg", "jpx") and not (min(w, h) >= 1000 and (ncolors or 9999) >= 256):
                reasons.append(f"format {ext}, not a photo")
            desc = f"page {i}: {w}x{h} px, shown {bbox.width / MM:.0f}x{bbox.height / MM:.0f} mm, {dpi:.0f} dpi, {ext}"
            listed += 1
            if reasons:
                add("FAIL", "images", desc + " - raster that is not a photo: " + "; ".join(reasons))
                flagged = True
            elif dpi < 150:
                add("WARN", "images", desc + " - foto under 150 dpi effektivt")
                flagged = True
            else:
                add("PASS", "images", desc + " - foto")
    if listed == 0:
        add("PASS", "images", "no raster images (all vector)")


def is_white_slide(page) -> bool:
    pix = page.get_pixmap(dpi=12)
    # sample a few points along the left/middle where body text would sit
    pts = [(int(pix.width * 0.06), int(pix.height * 0.5)), (int(pix.width * 0.06), int(pix.height * 0.3))]
    return all(all(c >= 250 for c in pix.pixel(x, y)[:3]) for x, y in pts)


def check_text(doc, margin_mm: float, footer_mm: float) -> None:
    margin = margin_mm * MM
    out_bad, margin_bad, footer_bad, small = [], [], [], []
    for i, page in enumerate(doc, 1):
        content = is_white_slide(page)
        PAGE_W, PAGE_H = page.rect.width, page.rect.height
        footer_top = PAGE_H - footer_mm * MM
        for b in page.get_text("dict", clip=WIDE)["blocks"]:
            for line in b.get("lines", []):
                for sp in line["spans"]:
                    txt = sp["text"].strip()
                    if not txt:
                        continue
                    x0, y0, x1, y1 = sp["bbox"]
                    # use font-size box for vertical extent (bbox includes leading)
                    if x0 < -0.5 or y0 < -0.5 or x1 > PAGE_W + 0.5 or y1 > PAGE_H + 0.5:
                        out_bad.append(f"page {i}: «{txt[:40]}» outside the page")
                    elif x0 < margin or x1 > PAGE_W - margin or y0 < margin or y1 > PAGE_H - margin:
                        margin_bad.append(f"page {i}: «{txt[:40]}» ({x0 / MM:.1f},{y0 / MM:.1f})-({x1 / MM:.1f},{y1 / MM:.1f}) mm")
                    if content and y1 > footer_top and not re.fullmatch(r"\d{1,3}", txt):
                        footer_bad.append(f"page {i}: «{txt[:40]}» in the footer area (y={y1 / MM:.1f} mm)")
                    if sp["size"] < 11.95:
                        small.append(f"page {i}: «{txt[:30]}» {sp['size']:.1f} pt")
    if out_bad:
        add("FAIL", "bounds", f"{len(out_bad)} text piece(s) outside the page: " + " | ".join(out_bad[:6]))
    else:
        add("PASS", "bounds", "no text outside the page")
    if margin_bad:
        add("WARN", "bounds", f"{len(margin_bad)} text piece(s) within the {margin_mm:g} mm margin (page number/footer may be intended): "
            + " | ".join(margin_bad[:6]))
    else:
        add("PASS", "bounds", f"no text within the {margin_mm:g} mm margin")
    if footer_bad:
        add("FAIL", "footer", f"{len(footer_bad)} text piece(s) overlap the footer area ({footer_mm:g} mm): " + " | ".join(footer_bad[:6]))
    else:
        add("PASS", "footer", f"no body text in the footer area ({footer_mm:g} mm) on white content slides")
    if small:
        add("WARN", "textsize", f"{len(small)} text piece(s) under 12 pt: " + " | ".join(small[:6]))
    else:
        add("PASS", "textsize", "no text under 12 pt")


def check_colors(doc, pal) -> None:
    dev = defaultdict(set)   # hex -> pages
    count = defaultdict(int)
    for i, page in enumerate(doc, 1):
        for b in page.get_text("dict", clip=WIDE)["blocks"]:
            for line in b.get("lines", []):
                for sp in line["spans"]:
                    if not sp["text"].strip():
                        continue
                    rgb = to_rgb255(sp["color"])
                    if rgb and not near_palette(rgb, pal):
                        dev[("text", hexof(rgb))].add(i)
                        count[("text", hexof(rgb))] += 1
        for d in page.get_drawings():
            for key, label in (("fill", "fill"), ("color", "strek")):
                rgb = to_rgb255(d.get(key))
                if rgb and not near_palette(rgb, pal):
                    dev[(label, hexof(rgb))].add(i)
                    count[(label, hexof(rgb))] += 1
    if dev:
        parts = [f"{k[0]} {k[1]} (page {pages_str(v)}; {count[k]} object(s))" for k, v in sorted(dev.items())]
        add("WARN", "colors", f"{len(dev)} colour(s) outside the palette: " + "; ".join(parts[:12]))
    else:
        add("PASS", "colors", "all text and vector graphics use palette colours")


def check_empty(doc, allow: set[int]) -> None:
    bad = []
    for i, page in enumerate(doc, 1):
        if i in allow:
            continue
        nchars = len(page.get_text().strip())
        nimg = len(page.get_image_info())
        ndraw = len(page.get_drawings())
        if nchars == 0 and nimg == 0 and ndraw == 0:
            bad.append(f"page {i}: completely empty")
        elif nchars < 5 and nimg == 0 and ndraw < 4:
            bad.append(f"page {i}: almost empty ({nchars} characters, {ndraw} shapes)")
    if bad:
        add("WARN", "empty", "; ".join(bad))
    else:
        add("PASS", "empty", "no empty or almost empty pages")


def main() -> None:
    for s in (sys.stdout, sys.stderr):
        s.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="Check a KodeWorks presentation (PDF)")
    ap.add_argument("pdf")
    ap.add_argument("--colors", help="colors.json (default: found via the project root)")
    ap.add_argument("--margin-mm", type=float, default=8.0)
    ap.add_argument("--footer-mm", type=float, default=17.0, help="height of the footer area at the bottom")
    ap.add_argument("--allow-empty", default="", help="comma-separated page numbers that are (almost) empty on purpose")
    ap.add_argument("--png-dir", help="also write the pages as PNG (70 dpi) here")
    args = ap.parse_args()

    pdf = Path(args.pdf)
    if not pdf.is_file():
        sys.exit(f"ERROR: {pdf} not found")
    cpath = find_colors(args.colors)
    if cpath is None or not cpath.exists():
        sys.exit("ERROR: colors.json not found (use --colors)")
    pal = load_palette(cpath)
    allow = {int(x) for x in args.allow_empty.split(",") if x.strip()}
    doc = pymupdf.open(pdf)

    check_size(doc)
    check_fonts(doc)
    check_images(doc)
    check_text(doc, args.margin_mm, args.footer_mm)
    check_colors(doc, pal)
    check_empty(doc, allow)

    if args.png_dir:
        out = Path(args.png_dir)
        out.mkdir(parents=True, exist_ok=True)
        for i, page in enumerate(doc, 1):
            page.get_pixmap(dpi=70).save(out / f"{pdf.stem}-{i:02d}.png")

    print(f"Checking {pdf.name}: {doc.page_count} pages\n")
    for check in ("size", "fonts", "images", "bounds", "footer", "textsize", "colors", "empty"):
        for status, c, msg in results:
            if c == check:
                print(f"{status:<4}  {c:<8} {msg}")
    n = {s: sum(1 for r in results if r[0] == s) for s in ("PASS", "WARN", "FAIL")}
    print(f"\nSummary: {n['PASS']} PASS, {n['WARN']} WARN, {n['FAIL']} FAIL")
    sys.exit(1 if n["FAIL"] else 0)


if __name__ == "__main__":
    main()
