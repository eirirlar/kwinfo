# /// script
# requires-python = ">=3.10"
# dependencies = ["pymupdf"]
# ///
"""Check a finished KodeWorks A4 document (letter or document) PDF. Prints OK / WARN / FAIL per check.

Usage:
    uv run check_document_pdf.py file.pdf [--company "KodeWorks AS"] [--margin-mm 8]
        [--footer-mm 32] [--header-mm 25]
    uv run check_document_pdf.py --self-test

Exit code 1 if any check FAILs. Checks:
  size      every page is A4 (210 x 297 mm)
  fonts     every font is NON Natural Grotesk and embedded
  images    no raster images at all (graphics must be vector)
  bounds    no text outside the page (FAIL) or within --margin-mm of the edge (WARN)
  footer    footer of every page has company name, org.nr. and both office addresses
  markdown  no literal Markdown left in the text
  typo      no straight apostrophe or double hyphen in the text
  pagenum   page numbers on pages 2+ when the document has more than one page
  fill      WARN when the last page is under ~12 % filled or a page is nearly empty
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import pymupdf
from project_tmp import work_dir  # work folders in <project root>/tmp/ (CLAUDE.md)

MM = 72 / 25.4
A4_W, A4_H = 210 * MM, 297 * MM
WIDE = pymupdf.Rect(-5000, -5000, 5000, 5000)  # so text outside the page is still seen

COMPANIES = {
    "KodeWorks AS": "820 478 452",
    "KodeWorks Trondheim AS": "920 478 492",
    "KodeWorks Eiendom AS": "920 478 506",
    "KodeWorks Oslo AS": "922 070 709",
}
ADDRESSES = ("Fjordgata 30", "Grønnegata 10")

results: list[tuple[str, str, str]] = []  # (status, check, message)


def add(status: str, check: str, msg: str) -> None:
    results.append((status, check, msg))


def norm(s: str) -> str:
    """Collapse all whitespace, including NBSP and thin spaces, to single spaces."""
    return re.sub(r"[\s    ]+", " ", s).strip()


def pages_str(pages) -> str:
    p = sorted(set(pages))
    return ", ".join(map(str, p[:12])) + (" ..." if len(p) > 12 else "")


def spans_of(page):
    for b in page.get_text("dict", clip=WIDE)["blocks"]:
        for line in b.get("lines", []):
            for sp in line["spans"]:
                if sp["text"].strip():
                    yield sp


def check_size(doc) -> None:
    bad = []
    for i, page in enumerate(doc, 1):
        r = page.rect
        if abs(r.width - A4_W) > 1.5 or abs(r.height - A4_H) > 1.5:
            bad.append(f"page {i}: {r.width / MM:.1f} x {r.height / MM:.1f} mm")
    if bad:
        add("FAIL", "size", "wrong page size (expected A4, 210 x 297 mm): " + "; ".join(bad[:5]))
    else:
        add("OK", "size", f"all {doc.page_count} pages are A4")


def check_fonts(doc) -> None:
    fonts: dict = {}
    for i, page in enumerate(doc, 1):
        for xref, ext, ftype, basefont, name, enc in page.get_fonts():
            fonts.setdefault((basefont, ext, ftype), []).append(i)
    if not fonts:
        add("WARN", "fonts", "no fonts found (no text?)")
        return
    for (basefont, ext, ftype), pgs in sorted(fonts.items()):
        clean = basefont.split("+")[-1]
        embedded = ext not in ("n/a", "")
        n = re.sub(r"[\s_-]", "", clean).lower()
        problems = []
        if "nonnaturalgrotesk" not in n:
            problems.append("not NON Natural Grotesk")
        if not embedded:
            problems.append("not embedded")
        add("FAIL" if problems else "OK", "fonts",
            f"{basefont} ({ftype}, {'embedded' if embedded else 'NOT embedded'}) page {pages_str(pgs)}"
            + (" - " + ", ".join(problems) if problems else ""))


def check_images(doc) -> None:
    bad = []
    for i, page in enumerate(doc, 1):
        for info in page.get_image_info():
            bad.append(f"page {i}: {info['width']}x{info['height']} px")
    if bad:
        add("FAIL", "images", f"{len(bad)} raster image(s); all graphics must be vector: " + "; ".join(bad[:6]))
    else:
        add("OK", "images", "no raster images (all vector)")


def check_bounds(doc, margin_mm: float) -> None:
    margin = margin_mm * MM
    out_bad, margin_bad = [], []
    for i, page in enumerate(doc, 1):
        pw, ph = page.rect.width, page.rect.height
        for sp in spans_of(page):
            txt = sp["text"].strip()
            x0, y0, x1, y1 = sp["bbox"]
            if x0 < -0.5 or y0 < -0.5 or x1 > pw + 0.5 or y1 > ph + 0.5:
                out_bad.append(f"page {i}: «{txt[:40]}» outside the page")
            elif x0 < margin or x1 > pw - margin or y0 < margin or y1 > ph - margin:
                margin_bad.append(f"page {i}: «{txt[:40]}» ({x0 / MM:.1f},{y0 / MM:.1f})-({x1 / MM:.1f},{y1 / MM:.1f}) mm")
    if out_bad:
        add("FAIL", "bounds", f"{len(out_bad)} text piece(s) outside the page: " + " | ".join(out_bad[:6]))
    else:
        add("OK", "bounds", "no text outside the page")
    if margin_bad:
        add("WARN", "bounds", f"{len(margin_bad)} text piece(s) within {margin_mm:g} mm of the page edge: " + " | ".join(margin_bad[:6]))
    else:
        add("OK", "bounds", f"no text within {margin_mm:g} mm of the page edge")


def check_footer(doc, company: str, footer_mm: float) -> None:
    orgnr = COMPANIES[company]
    bad = []
    for i, page in enumerate(doc, 1):
        top = page.rect.height - footer_mm * MM
        text = norm(" ".join(sp["text"] for sp in spans_of(page) if sp["bbox"][1] >= top))
        missing = []
        if company not in text:
            missing.append(f"company name «{company}»")
        if orgnr not in text:
            missing.append(f"org.nr. {orgnr}")
        for a in ADDRESSES:
            if a not in text:
                missing.append(f"address «{a}»")
        if missing:
            bad.append(f"page {i}: missing " + ", ".join(missing))
    if bad:
        add("FAIL", "footer", f"the footer is incomplete for {company}: " + " | ".join(bad[:6]))
    else:
        add("OK", "footer", f"the footer on every page has {company}, org. no. {orgnr} and both office addresses")


MD_PATTERNS = [
    (r"\*\*", "**"),
    (r":::", ":::"),
    (r"\\\\|\\$|\\ ", "backslash (\\)"),
    (r"\{\.", "{."),
    (r"\[[^\]]*\]\(", "[..](..)"),
]


def check_markdown_and_typo(doc) -> None:
    md_bad, typo_bad = [], []
    for i, page in enumerate(doc, 1):
        text = page.get_text()
        for pat, label in MD_PATTERNS:
            if re.search(pat, text, flags=re.M):
                md_bad.append(f"page {i}: {label}")
        if "'" in text:
            ctx = text[max(0, text.index("'") - 15): text.index("'") + 15].replace("\n", " ")
            typo_bad.append(f"page {i}: straight apostrophe in «{ctx}»")
        if "--" in text:
            ctx = text[max(0, text.index("--") - 15): text.index("--") + 15].replace("\n", " ")
            typo_bad.append(f"page {i}: double hyphen in «{ctx}»")
    if md_bad:
        add("FAIL", "markdown", "Markdown remnants in the text: " + "; ".join(md_bad[:8]))
    else:
        add("OK", "markdown", "no Markdown remnants in the text")
    if typo_bad:
        add("FAIL", "typo", " | ".join(typo_bad[:6]))
    else:
        add("OK", "typo", "no straight apostrophe or double hyphen")


def check_pagenum(doc) -> None:
    if doc.page_count < 2:
        add("OK", "pagenum", "one page, page number not required")
        return
    pat = re.compile(r"^(?:side\s*)?\d{1,3}(?:\s*(?:/|av)\s*\d{1,3})?$", re.I)
    missing = []
    for i, page in enumerate(doc, 1):
        if i == 1:
            continue
        if not any(pat.match(norm(sp["text"])) for sp in spans_of(page)):
            missing.append(i)
    if missing:
        add("FAIL", "pagenum", f"page number missing on page {pages_str(missing)}")
    else:
        add("OK", "pagenum", "page numbers from page 2 on")


def body_fill(page, header_mm: float, footer_mm: float) -> tuple[float, int]:
    """Return (fill fraction, character count) for the body zone between header and footer."""
    top = header_mm * MM
    bottom = page.rect.height - footer_mm * MM
    ys, chars = [], 0
    for sp in spans_of(page):
        y0, y1 = sp["bbox"][1], sp["bbox"][3]
        if y0 >= top - 1 and y1 <= bottom + 1:
            ys.append(y1)
            chars += len(sp["text"].strip())
    if not ys:
        return 0.0, 0
    return max(0.0, (max(ys) - top) / (bottom - top)), chars


def check_fill(doc, header_mm: float, footer_mm: float) -> None:
    warns = []
    for i, page in enumerate(doc, 1):
        fill, chars = body_fill(page, header_mm, footer_mm)
        last = i == doc.page_count
        if chars < 30 and not (last and doc.page_count == 1 and chars > 0):
            warns.append(f"page {i}: almost empty ({chars} characters in the body area)")
        elif last and doc.page_count > 1 and fill < 0.12:
            warns.append(f"the last page is only {fill * 100:.0f} % full (a lone remainder on its own page)")
    if warns:
        add("WARN", "fill", "; ".join(warns))
    else:
        add("OK", "fill", "no empty pages and the last page is reasonably full")


def run_checks(pdf: Path, company: str, margin_mm: float, header_mm: float, footer_mm: float) -> int:
    results.clear()
    doc = pymupdf.open(pdf)
    check_size(doc)
    check_fonts(doc)
    check_images(doc)
    check_bounds(doc, margin_mm)
    check_footer(doc, company, footer_mm)
    check_markdown_and_typo(doc)
    check_pagenum(doc)
    check_fill(doc, header_mm, footer_mm)
    print(f"Checking {pdf.name}: {doc.page_count} pages, company {company}\n")
    for check in ("size", "fonts", "images", "bounds", "footer", "markdown", "typo", "pagenum", "fill"):
        for status, c, msg in results:
            if c == check:
                print(f"{status:<4}  {c:<8} {msg}")
    n = {s: sum(1 for r in results if r[0] == s) for s in ("OK", "WARN", "FAIL")}
    print(f"\nSummary: {n['OK']} OK, {n['WARN']} WARN, {n['FAIL']} FAIL")
    return 1 if n["FAIL"] else 0


def self_test() -> int:
    """Build a deliberately bad PDF and confirm that every check fires."""
    with work_dir("kwcheck_") as d:
        pdf = Path(d) / "bad.pdf"
        doc = pymupdf.open()
        p1 = doc.new_page(width=612, height=792)  # US Letter, not A4
        p1.insert_text((20, 40), "Helvetica **fet** og it's og -- og [lenke](x) {.cls} :::", fontname="helv", fontsize=11)
        p1.insert_text((600, 100), "utenfor", fontname="helv", fontsize=11)
        pix = pymupdf.Pixmap(pymupdf.csRGB, pymupdf.IRect(0, 0, 40, 40), False)
        pix.clear_with(200)
        p1.insert_image(pymupdf.Rect(100, 200, 200, 300), pixmap=pix)
        p2 = doc.new_page(width=612, height=792)
        p2.insert_text((100, 300), "x", fontname="helv", fontsize=11)
        doc.save(pdf)
        doc.close()
        print("Self-test: a deliberately bad PDF\n")
        run_checks(pdf, "KodeWorks AS", 8, 25, 32)
        fired = {(s, c) for s, c, _ in results if s in ("FAIL", "WARN")}
    expected = {("FAIL", "size"), ("FAIL", "fonts"), ("FAIL", "images"), ("FAIL", "bounds"), ("WARN", "bounds"),
                ("FAIL", "footer"), ("FAIL", "markdown"), ("FAIL", "typo"), ("FAIL", "pagenum"), ("WARN", "fill")}
    missing = expected - fired
    print()
    if missing:
        print(f"SELF-TEST FAILED: checks that did not fire: {sorted(missing)}")
        return 1
    print(f"SELF-TEST OK: all {len(expected)} expected warnings fired")
    return 0


def main() -> None:
    for s in (sys.stdout, sys.stderr):
        s.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="Check a KodeWorks A4 document (PDF)")
    ap.add_argument("pdf", nargs="?")
    ap.add_argument("--company", default="KodeWorks AS", choices=sorted(COMPANIES))
    ap.add_argument("--margin-mm", type=float, default=8.0)
    ap.add_argument("--header-mm", type=float, default=25.0, help="height of the top area that is not counted as body text")
    ap.add_argument("--footer-mm", type=float, default=32.0, help="height of the footer at the bottom")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        sys.exit(self_test())
    if not args.pdf:
        ap.error("give a PDF or --self-test")
    pdf = Path(args.pdf)
    if not pdf.is_file():
        sys.exit(f"ERROR: {pdf} not found")
    sys.exit(run_checks(pdf, args.company, args.margin_mm, args.header_mm, args.footer_mm))


if __name__ == "__main__":
    main()
