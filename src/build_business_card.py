# /// script
# requires-python = ">=3.10"
# dependencies = ["pymupdf"]
# ///
"""Build a KodeWorks business card: Markdown (YAML header) -> pandoc template -> lualatex -> print PDF + PNG.

Usage (from the project root):
    uv run src/build_business_card.py card.md [-o out.pdf] [--png out.png] [--keep-build]

The card's Markdown file holds everything that differs between cards in its YAML header:
name (required), title, phone, email, web. The template is src/business_card/card.tex.

Output:
  - print PDF, two pages (front, back): sheet 105 x 75 mm, trim 85 x 55 mm with TrimBox/BleedBox set,
    3 mm bleed, crop marks, all colours in DeviceCMYK from colors.json, the profile font embedded;
  - screen PNG (front and back side by side, cropped to the trim box), rendered from a second build
    with the profile's RGB colours, since the neon green cannot be shown through CMYK.

The fonts are unpacked from the licensed Non Natural Grotesk zip into a temporary build folder (never
installed, never copied into the repo) and font_guard stops the build if any font outside the build folder
and TeX Live is loaded. The black wordmark and symbol are rewritten from RGB to 100 % K. The build folder
is deleted afterwards. Checks on the finished PDF are printed after the build.

Cards for every CV in Markdown are built with src/build_cv_business_cards.py, which uses this script.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import font_guard  # noqa: E402
import pymupdf  # noqa: E402
from build_presentation import (FONT_ZIP_REL, PROFILE_REL, die, extract_fonts, find_root, run,  # noqa: E402
                                show_latex_error, write_kernfix)
from project_tmp import mkdtemp  # noqa: E402  work folders in <project root>/tmp/ (CLAUDE.md)

MM = 72 / 25.4
SHEET = (105.0, 75.0)          # mm
TRIM = (10.0, 10.0, 95.0, 65.0)  # mm, from the lower left corner of the sheet
BLEED = 3.0                    # mm
SAFE = 3.0                     # mm: text must stay this far inside the trim edge
# wordmark (card.tex): 40 mm wide, top edge 16 mm below the sheet top; aspect from kw-wordmark-black.svg
WORDMARK_BOTTOM_MM = 16.0 + 40.0 * 132.83 / 900.81
LOGO_CLEAR = 5.0               # mm: minimum gap between the wordmark and the contact block
REQUIRED_FIELDS = ("name",)
KNOWN_FIELDS = ("name", "title", "phone", "email", "web")


def color_defs(profile: Path, model: str) -> str:
    """colors.tex: the profile colours from colors.json, as cmyk (print) or HTML/RGB (screen) definitions."""
    data = json.loads((profile / "colors.json").read_text(encoding="utf-8"))
    by_id = {c["id"]: c for c in data["colors"] + data.get("technical", [])}

    def define(name: str, cid: str) -> str:
        c = by_id[cid]
        if model == "cmyk":
            v = ",".join(f"{x / 100:g}" for x in c["cmyk"])
            return f"\\definecolor{{{name}}}{{cmyk}}{{{v}}}  % {c['name']} {c['hex']}\n"
        return f"\\definecolor{{{name}}}{{HTML}}{{{c['hex'].lstrip('#')}}}  % {c['name']}\n"

    reg = ("\\definecolor{kwregistration}{cmyk}{1,1,1,1}" if model == "cmyk"
           else "\\definecolor{kwregistration}{HTML}{000000}")
    return (define("kwgreen", "green") + define("kwgrey", "grey") + define("kwblack", "black")
            + reg + "  % crop marks\n")


def cmyk_logo(src: Path, dst: Path) -> None:
    """Copy a black single-colour vector PDF and turn its RGB black fill/stroke into 100 % K."""
    with pymupdf.open(src) as doc:
        for page in doc:
            for xref in page.get_contents():
                stream = doc.xref_stream(xref).decode("latin-1")
                stream = re.sub(r"\b0 0 0 rg\b", "0 0 0 1 k", stream)
                stream = re.sub(r"\b0 0 0 RG\b", "0 0 0 1 K", stream)
                if re.search(r"\brg\b|\bRG\b", stream):
                    die(f"{src.name} contains RGB colours other than black; it cannot be converted to CMYK.")
                doc.update_stream(xref, stream.encode("latin-1"))
        doc.save(dst)


def read_fields(md: Path) -> dict[str, str]:
    """The YAML header as plain strings (flat key: value only), for the pre-flight check."""
    text = md.read_text(encoding="utf-8")
    m = re.match(r"﻿?---\s*\n(.*?)\n(---|\.\.\.)\s*\n", text, re.S)
    if not m:
        die("The Markdown file has no YAML header (--- ... ---) with name, title, phone, email and web.")
    fields = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^([A-Za-z_]+):\s*(.*?)\s*$", line)
        if kv:
            fields[kv.group(1)] = kv.group(2).strip("'\"")
    return fields


def check_pdf(pdf: Path) -> list[str]:
    """Print checks: sheet size, trim and bleed boxes, text inside the safe zone, fonts embedded, no raster."""
    out: list[str] = []
    with pymupdf.open(pdf) as doc:
        if doc.page_count != 2:
            out.append(f"The PDF has {doc.page_count} pages; expected 2 (front and back).")
        for pno, page in enumerate(doc, 1):
            side = "front" if pno == 1 else "back"
            w, h = page.mediabox.width / MM, page.mediabox.height / MM
            if abs(w - SHEET[0]) > 0.05 or abs(h - SHEET[1]) > 0.05:
                out.append(f"{side}: the sheet is {w:.2f} × {h:.2f} mm, expected {SHEET[0]:g} × {SHEET[1]:g} mm.")
            t = page.trimbox
            tw, th = t.width / MM, t.height / MM
            if abs(tw - 85) > 0.05 or abs(th - 55) > 0.05:
                out.append(f"{side}: the trim box is {tw:.2f} × {th:.2f} mm, expected 85 × 55 mm.")
            b = page.bleedbox
            for got, want in ((t.x0 - b.x0, BLEED), (b.x1 - t.x1, BLEED), (t.y0 - b.y0, BLEED), (b.y1 - t.y1, BLEED)):
                if abs(got / MM - want) > 0.05:
                    out.append(f"{side}: the bleed is {got / MM:.2f} mm, expected {want:g} mm.")
                    break
            safe = pymupdf.Rect(t.x0 + SAFE * MM, t.y0 + SAFE * MM, t.x1 - SAFE * MM, t.y1 - SAFE * MM)
            logo_bottom = WORDMARK_BOTTOM_MM * MM if pno == 1 else None
            for blk in page.get_text("dict")["blocks"]:
                for ln in blk.get("lines", []):
                    text = "".join(sp["text"] for sp in ln["spans"]).strip()
                    if not text:
                        continue
                    r = pymupdf.Rect(ln["bbox"])
                    if not safe.contains(r):
                        out.append(f"{side}: the line «{text}» goes outside the safe zone "
                                   f"({SAFE:g} mm from the trim edge). Shorten the text.")
                    elif logo_bottom is not None and r.y0 < logo_bottom + LOGO_CLEAR * MM:
                        out.append(f"{side}: the line «{text}» comes closer than {LOGO_CLEAR:g} mm "
                                   "below the wordmark. Shorten the title or remove a line.")
            for img in page.get_images(full=True):
                out.append(f"{side}: contains a raster image (xref {img[0]}); the card should have vector graphics only.")
            for f in page.get_fonts(full=True):
                ext, name = f[1], f[3]
                if ext in ("n/a", "") or "NaturalGrotesk" not in name.replace(" ", ""):
                    out.append(f"{side}: the font {name} ({ext}) is not the profile font or is not embedded.")
            streams = [page.read_contents()] + [doc.xref_stream(x[0]) for x in page.get_xobjects()]
            if any(non_cmyk_paint(s) for s in streams):
                out.append(f"{side}: something is drawn or written in RGB or greyscale; everything must be CMYK.")
    return out


PAINT_OPS = {"f", "F", "f*", "S", "s", "B", "B*", "b", "b*", "Tj", "TJ", "'", '"', "sh"}
FILL_OPS = {"f", "F", "f*", "Tj", "TJ", "'", '"', "sh"}
STROKE_OPS = {"S", "s"}


def non_cmyk_paint(stream: bytes) -> bool:
    """True if something is painted while the active fill or stroke colour is DeviceGray or DeviceRGB.
    (LuaTeX resets its colour stack to '0 g 0 G' between objects; that alone paints nothing.)"""
    tokens = re.findall(r"\((?:\\.|[^\\)])*\)|<[^>]*>|\[|\]|/[^\s/\[\]()<>]+|[^\s\[\]()<>/]+", stream.decode("latin-1"))
    fill, stroke, stack = "cmyk", "cmyk", []
    for tok in tokens:
        if tok in ("g", "rg"):
            fill = "other"
        elif tok in ("G", "RG"):
            stroke = "other"
        elif tok in ("k", "sc", "scn"):
            fill = "cmyk"
        elif tok in ("K", "SC", "SCN"):
            stroke = "cmyk"
        elif tok == "q":
            stack.append((fill, stroke))
        elif tok == "Q" and stack:
            fill, stroke = stack.pop()
        elif tok in PAINT_OPS:
            if (tok in FILL_OPS or tok not in STROKE_OPS) and fill == "other":
                return True
            if tok not in FILL_OPS and stroke == "other":
                return True
    return False


def write_png(pdf: Path, png: Path, dpi: int = 300) -> None:
    """Front and back side by side, each cropped to the trim box, with a white gap of 4 mm."""
    with pymupdf.open(pdf) as doc:
        pix = [p.get_pixmap(dpi=dpi, clip=p.trimbox) for p in doc]
    gap = round(4 / 25.4 * dpi)
    out = pymupdf.Pixmap(pymupdf.csRGB, pymupdf.IRect(0, 0, pix[0].width * 2 + gap, pix[0].height), False)
    out.clear_with(255)
    for i, p in enumerate(pix):
        p.set_origin(i * (pix[0].width + gap), 0)
        out.copy(p, p.irect)
    out.set_dpi(dpi, dpi)
    out.save(png)


def main() -> None:
    for s in (sys.stdout, sys.stderr):
        s.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="Build a KodeWorks business card (Markdown -> print PDF and PNG)")
    ap.add_argument("md", help="the card's Markdown file (YAML header with name, title, phone, email, web)")
    ap.add_argument("-o", "--output", help="print PDF (default: next to the Markdown file)")
    ap.add_argument("--png", help="screen version (default: same name as the PDF, .png)")
    ap.add_argument("--keep-build", action="store_true", help="keep the build folder (contains licensed font files)")
    args = ap.parse_args()

    md = Path(args.md).resolve()
    if not md.is_file():
        die(f"Markdown file not found: {md}")
    fields = read_fields(md)
    for f in REQUIRED_FIELDS:
        if not fields.get(f):
            die(f"The field «{f}» is missing in the YAML header.")
    unknown = sorted(set(fields) - set(KNOWN_FIELDS))
    if unknown:
        print("WARNING: unknown fields in the YAML header are not used: " + ", ".join(unknown))

    root = find_root()
    if root is None:
        die("Project root not found (deliverable/visualprofile/profile/colors.json). Run from the project root.")
    profile, zip_path = root / PROFILE_REL, root / FONT_ZIP_REL
    if not zip_path.is_file():
        die(f"The licensed font zip was not found: {zip_path}")
    for tool in ("pandoc", "lualatex"):
        if not shutil.which(tool):
            die(f"«{tool}» is not on PATH.")
    style = HERE / "business_card"
    kernfix = root / "src/presentation/kernfix.json"
    out_pdf = Path(args.output).resolve() if args.output else md.with_suffix(".pdf")
    out_png = Path(args.png).resolve() if args.png else out_pdf.with_suffix(".png")

    work = mkdtemp("kwcard_")
    try:
        shutil.copyfile(style / "card.tex", work / "card-template.tex")
        extract_fonts(zip_path, work / "fonts")
        write_kernfix(kernfix, work / "kernfix.lua")
        font_guard.write_hook(work)
        log = ""
        for model in ("rgb", "cmyk"):  # rgb: screen version only; cmyk: the print PDF
            for asset in ("kw-wordmark", "kw-symbol"):
                src = profile / f"assets/pdf/{asset}-black.pdf"
                if model == "cmyk":
                    cmyk_logo(src, work / f"{asset}.pdf")
                else:
                    shutil.copyfile(src, work / f"{asset}.pdf")
            (work / "colors.tex").write_text(color_defs(profile, model), encoding="utf-8")
            (work / "paths.tex").write_text(f"\\def\\kwfontdir{{{(work / 'fonts').as_posix()}/}}\n"
                                            f"\\def\\kwcolormodel{{{model}}}\n", encoding="utf-8")
            res = run(["pandoc", str(md), "-f", "markdown", "-t", "latex", "--template", "card-template.tex",
                       "-o", "card.tex"], work, "pandoc")
            if res.returncode != 0:
                sys.stderr.write(res.stderr)
                die("pandoc failed (check the YAML header).")
            res = run(["lualatex", "-interaction=nonstopmode", "-halt-on-error", "card.tex"], work, f"lualatex ({model})")
            if res.returncode != 0:
                show_latex_error(work / "card.log")
                die(f"lualatex failed ({model}). See the lines above.")
            font_guard.check(work)
            log += (work / "card.log").read_text(encoding="utf-8", errors="replace")
            shutil.copyfile(work / "card.pdf", work / f"card-{model}.pdf")
        warnings = sorted({f"The character «{m.group(1)}» is not in the font and is left out."
                           for m in re.finditer(r"Missing character: There is no (.+?) \(U\+", log)})
        out_pdf.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(work / "card-cmyk.pdf", out_pdf)
        warnings += check_pdf(out_pdf)
        write_png(work / "card-rgb.pdf", out_png)
        print(f"Built {out_pdf}\n      {out_png}")
        if warnings:
            print(f"\n{len(warnings)} warning(s):")
            for w in warnings:
                print("  WARNING: " + w)
            sys.exit(1)
        print("Check: trim size 85 × 55 mm, 3 mm bleed, text in the safe zone, profile font only "
              "(embedded), CMYK only, no raster images.")
    finally:
        if args.keep_build:
            print(f"WARNING: the build folder is kept and contains licensed font files; delete it afterwards: {work}")
        else:
            shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    main()
