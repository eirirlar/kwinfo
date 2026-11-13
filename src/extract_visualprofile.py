# /// script
# dependencies = ["Pillow", "pymupdf"]
# ///
"""Convert a PDF/DOCX/PPTX into Markdown with text extracted and images saved separately.

Output is written next to the input file:
    <dir>/<YYYY-MM-DD>_<slug>.md
    <dir>/<YYYY-MM-DD>_<slug>_media/

PDF:  text via `pdftotext` per page, images via `pdfimages` per page. Each image is
      saved once (deduplicated by PDF object ID) and referenced on every page where it
      appears. Soft masks (alpha) are skipped.
      Vector graphics via PyMuPDF `get_drawings()`: paths that overlap or touch are grouped
      into one figure and written as a standalone SVG (vector only, no text or raster).
      Full-page shapes (backgrounds) become their own figure. Identical SVGs are saved
      once. Gradients (shadings) and clip paths are not part of `get_drawings()` and are
      therefore missing.
DOCX/PPTX: `pandoc --extract-media`, then images are downscaled in place.

All raster images are downscaled by --scale (default 0.25 of width/height). Images whose
longest side would drop below --min-side are kept at original size.

The document date is read from file metadata (PDF CreationDate, OOXML dcterms:created).

Usage (from project root):
    uv run src/extract_visualprofile.py "background/new/Rapport.pdf"   # -> <dato>_rapport.md and _media/ next to it
"""

import argparse
import hashlib
import html
import re
import shutil
import subprocess
import sys
import unicodedata
import zipfile
from datetime import date
from pathlib import Path

import pymupdf
from PIL import Image
from project_tmp import work_dir  # work folders in <project root>/tmp/ (CLAUDE.md)

Image.MAX_IMAGE_PIXELS = None

# Shapes covering more than this share of the page are treated as backgrounds and kept
# out of grouping, otherwise everything on the page would merge into one figure.
BACKGROUND_SHARE = 0.8
# Plain single rectangles covering more than this share are panels behind other content
# and are kept out of grouping for the same reason.
PANEL_SHARE = 0.15
# Two shapes belong to the same figure if the gap between them is at most
# GROUP_TOLERANCE pt or GROUP_RELATIVE x the height of the shorter one, whichever is larger,
# capped at GROUP_MAX_GAP pt. The relative part keeps outlined words (e.g. the wordmark)
# together as one figure; the cap keeps large, separate figures (symbols, swatches) apart.
GROUP_TOLERANCE = 2.0
GROUP_RELATIVE = 0.4
GROUP_MAX_GAP = 50.0
LINE_CAPS = {0: "butt", 1: "round", 2: "square"}
LINE_JOINS = {0: "miter", 1: "round", 2: "bevel"}


def run(cmd: list[str]) -> str:
    # Tools emit CRLF on Windows; normalise to LF so files are not written with "\r\r\n".
    out = subprocess.run(cmd, check=True, capture_output=True).stdout.decode("utf-8", "replace")
    return out.replace("\r\n", "\n")


def write_lf(path: Path, text: str) -> None:
    """Write UTF-8 text with LF line endings on every platform (the repo is shared with Linux)."""
    path.write_text(text, encoding="utf-8", newline="\n")


def slugify(name: str) -> str:
    s = name.lower().replace("æ", "ae").replace("ø", "oe").replace("å", "aa")
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-z0-9]+", "_", s).strip("_")
    return s


def pdf_date(path: Path) -> str | None:
    out = run(["pdfinfo", "-isodates", str(path)])
    m = re.search(r"^CreationDate:\s+(\d{4}-\d{2}-\d{2})", out, re.M)
    return m.group(1) if m else None


def ooxml_date(path: Path) -> str | None:
    try:
        with zipfile.ZipFile(path) as z:
            xml = z.read("docProps/core.xml").decode("utf-8", "replace")
    except (KeyError, zipfile.BadZipFile):
        return None
    m = re.search(r"<dcterms:created[^>]*>(\d{4}-\d{2}-\d{2})", xml)
    return m.group(1) if m else None


def downscale(img: Image.Image, scale: float, min_side: int) -> Image.Image:
    w, h = img.size
    nw, nh = round(w * scale), round(h * scale)
    if max(nw, nh) < min_side:
        return img
    return img.resize((max(nw, 1), max(nh, 1)), Image.LANCZOS)


def save_jpeg(src: Path, dst: Path, scale: float, min_side: int) -> None:
    with Image.open(src) as img:
        img = img.convert("RGB")
        downscale(img, scale, min_side).save(dst, "JPEG", quality=85, optimize=True)


def parse_image_list(path: Path) -> list[dict]:
    rows = []
    for line in run(["pdfimages", "-list", str(path)]).splitlines()[2:]:
        f = line.split()
        if len(f) < 11:
            continue
        rows.append({"page": int(f[0]), "num": int(f[1]), "type": f[2],
                     "width": int(f[3]), "height": int(f[4]), "obj": f[10]})
    return rows


def hex_color(c) -> str:
    return "#" + "".join(f"{round(max(0.0, min(1.0, v)) * 255):02x}" for v in c[:3])


def path_data(d: dict, ox: float, oy: float) -> str:
    """SVG path data for one PyMuPDF drawing, translated by (-ox, -oy)."""
    def pt(p) -> str:
        return f"{p.x - ox:.2f} {p.y - oy:.2f}"

    parts: list[str] = []
    cur = None
    for item in d["items"]:
        kind = item[0]
        if kind == "l":
            if cur is None or cur != item[1]:
                parts.append("M" + pt(item[1]))
            parts.append("L" + pt(item[2]))
            cur = item[2]
        elif kind == "c":
            if cur is None or cur != item[1]:
                parts.append("M" + pt(item[1]))
            parts.append("C" + " ".join(pt(p) for p in item[2:5]))
            cur = item[4]
        elif kind == "re":
            # Orientation matters for nonzero fill: an inner rect drawn the other way is a hole.
            r = item[1]
            corners = [r.tl, r.tr, r.br, r.bl] if (len(item) < 3 or item[2] >= 0) else [r.tl, r.bl, r.br, r.tr]
            parts.append("M" + pt(corners[0]) + "".join("L" + pt(c) for c in corners[1:]) + "Z")
            cur = None
        elif kind == "qu":
            q = item[1]
            parts.append("M" + pt(q.ul) + "L" + pt(q.ur) + "L" + pt(q.lr) + "L" + pt(q.ll) + "Z")
            cur = None
    if d.get("closePath") and parts and not parts[-1].endswith("Z"):
        parts.append("Z")
    return "".join(parts)


def path_element(d: dict, ox: float, oy: float) -> str:
    attrs = [f'd="{path_data(d, ox, oy)}"']
    fill = d.get("fill")
    attrs.append(f'fill="{hex_color(fill)}"' if fill else 'fill="none"')
    if fill and d.get("fill_opacity") not in (None, 1, 1.0):
        attrs.append(f'fill-opacity="{d["fill_opacity"]:.3f}"')
    if fill and d.get("even_odd"):
        attrs.append('fill-rule="evenodd"')
    stroke = d.get("color")
    if stroke and d.get("type") in ("s", "fs"):
        attrs.append(f'stroke="{hex_color(stroke)}"')
        attrs.append(f'stroke-width="{(d.get("width") or 1):.2f}"')
        if d.get("stroke_opacity") not in (None, 1, 1.0):
            attrs.append(f'stroke-opacity="{d["stroke_opacity"]:.3f}"')
        caps = d.get("lineCap")
        if caps:
            attrs.append(f'stroke-linecap="{LINE_CAPS.get(int(max(caps)), "butt")}"')
        if d.get("lineJoin") is not None:
            attrs.append(f'stroke-linejoin="{LINE_JOINS.get(int(d["lineJoin"]), "miter")}"')
        dash = re.match(r"\[\s*([^\]]*)\]", d.get("dashes") or "")
        if dash and dash.group(1).strip():
            attrs.append(f'stroke-dasharray="{dash.group(1).strip()}"')
    return "<path " + " ".join(attrs) + "/>"


def group_drawings(drawings: list[dict], page_rect) -> list[list[dict]]:
    """Group drawings into figures: backgrounds alone, the rest by overlapping bounding boxes."""
    page_area = page_rect.width * page_rect.height
    backgrounds, rest = [], []
    for d in drawings:
        r = d["rect"]
        share = r.width * r.height / page_area
        plain_rect = len(d["items"]) == 1 and d["items"][0][0] in ("re", "qu")
        if share > BACKGROUND_SHARE or (plain_rect and share > PANEL_SHARE):
            backgrounds.append(d)
        else:
            rest.append(d)

    parent = list(range(len(rest)))

    def find(i: int) -> int:
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    # Sweep over shapes sorted by left edge; only compare with shapes that can still overlap in x.
    order = sorted(range(len(rest)), key=lambda i: rest[i]["rect"].x0)
    for a, i in enumerate(order):
        ri = rest[i]["rect"]
        # Upper bound for any partner's tolerance, so the sweep can stop early.
        t_max = max(GROUP_TOLERANCE, min(GROUP_RELATIVE * ri.height, GROUP_MAX_GAP))
        for j in order[a + 1:]:
            rj = rest[j]["rect"]
            if rj.x0 > ri.x1 + t_max:
                break
            t = max(GROUP_TOLERANCE, min(GROUP_RELATIVE * min(ri.height, rj.height), GROUP_MAX_GAP))
            if rj.x0 <= ri.x1 + t and rj.y0 <= ri.y1 + t and ri.y0 <= rj.y1 + t:
                parent[find(i)] = find(j)

    groups: dict[int, list[dict]] = {}
    for i, d in enumerate(rest):
        groups.setdefault(find(i), []).append(d)
    # Keep original paint order inside each group (and order groups by first appearance).
    result = [[d] for d in backgrounds]
    result += sorted(groups.values(), key=lambda g: g[0]["seqno"])
    return result


def figure_svg(group: list[dict]) -> str:
    pad = max((d.get("width") or 0) for d in group) / 2 + 0.5
    x0 = min(d["rect"].x0 for d in group) - pad
    y0 = min(d["rect"].y0 for d in group) - pad
    x1 = max(d["rect"].x1 for d in group) + pad
    y1 = max(d["rect"].y1 for d in group) + pad
    w, h = x1 - x0, y1 - y0
    body = "\n".join(path_element(d, x0, y0) for d in sorted(group, key=lambda d: d["seqno"]))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w:.2f}" height="{h:.2f}" '
            f'viewBox="0 0 {w:.2f} {h:.2f}">\n{body}\n</svg>\n')


def page_vectors(page, media: Path, saved: dict[str, str]) -> list[str]:
    """Write each vector figure on the page as SVG (deduplicated); return file names in order."""
    names: list[str] = []
    for group in group_drawings(page.get_drawings(), page.rect):
        svg = figure_svg(group)
        digest = hashlib.sha1(svg.encode()).hexdigest()[:12]
        if digest not in saved:
            name = f"vec_{digest}.svg"
            write_lf(media / name, svg)
            saved[digest] = name
        if saved[digest] not in names:
            names.append(saved[digest])
    return names


def convert_pdf(path: Path, md_path: Path, media: Path, title: str, doc_date: str,
                scale: float, min_side: int) -> tuple[int, int]:
    pages = int(re.search(r"^Pages:\s+(\d+)", run(["pdfinfo", str(path)]), re.M).group(1))
    rows = parse_image_list(path)
    doc = pymupdf.open(path)
    vectors: dict[str, str] = {}
    saved: dict[str, str] = {}
    lines = [f"# {title}", "", f"Dokumentdato: {doc_date}", ""]
    with work_dir("kwextract_") as tmp:
        for p in range(1, pages + 1):
            text = run(["pdftotext", "-enc", "UTF-8", "-f", str(p), "-l", str(p), str(path), "-"])
            text = text.replace("\f", "").strip()
            page_rows = [r for r in rows if r["page"] == p]
            # pdfimages numbers files per call in the same order as -list rows for the page.
            need = [i for i, r in enumerate(page_rows) if r["type"] == "image" and r["obj"] not in saved]
            if need:
                prefix = Path(tmp) / f"p{p}"
                # Uncompressed PPM/PGM output: PNG encoding of multi-megapixel images is very slow.
                run(["pdfimages", "-f", str(p), "-l", str(p), str(path), str(prefix)])
                files = sorted(Path(tmp).glob(f"p{p}-*"))
                for i in need:
                    r = page_rows[i]
                    if r["obj"] in saved:
                        continue
                    name = f"img_{r['obj']}.jpg"
                    save_jpeg(files[i], media / name, scale, min_side)
                    saved[r["obj"]] = name
                for f in files:
                    f.unlink()
            lines += [f"## Side {p}", ""]
            if text:
                lines += [text, ""]
            seen_on_page = set()
            for r in page_rows:
                if r["type"] != "image" or r["obj"] in seen_on_page:
                    continue
                seen_on_page.add(r["obj"])
                lines += [f"![]({media.name}/{saved[r['obj']]})", ""]
            for name in page_vectors(doc[p - 1], media, vectors):
                lines += [f"![]({media.name}/{name})", ""]
    write_lf(md_path, "\n".join(lines))
    print(f"  vector figures: {len(vectors)} unique SVGs")
    return pages, len(saved)


def docx_headers_footers(path: Path, media: Path) -> list[str]:
    """Markdown lines for DOCX header/footer text and images, which pandoc does not output.

    Images are copied to <media>/media/ (where pandoc puts body images). Empty and
    duplicate headers/footers are skipped.
    """
    lines: list[str] = []
    seen: set = set()
    with zipfile.ZipFile(path) as z:
        names = sorted((n for n in z.namelist() if re.fullmatch(r"word/(header|footer)\d+\.xml", n)),
                       key=lambda n: (n.split("/")[1][:6], int(re.search(r"(\d+)\.xml", n).group(1))))
        for name in names:
            xml = z.read(name).decode("utf-8", "replace")
            paras = ["".join(re.findall(r"<w:t(?: [^>]*)?>([^<]*)</w:t>", p))
                     for p in re.findall(r"<w:p[ >].*?</w:p>", xml, re.S)]
            paras = [html.unescape(p).strip() for p in paras if p.strip()]
            rels_name = f"word/_rels/{Path(name).name}.rels"
            rel_targets: dict[str, str] = {}
            if rels_name in z.namelist():
                for rel in re.findall(r"<Relationship [^>]*>", z.read(rels_name).decode("utf-8", "replace")):
                    rid, target = re.search(r'Id="([^"]+)"', rel), re.search(r'Target="([^"]+)"', rel)
                    if rid and target:
                        rel_targets[rid.group(1)] = target.group(1)
            images = [rel_targets[r] for r in re.findall(r'r:embed="([^"]+)"', xml) if r in rel_targets]
            key = (tuple(paras), tuple(images))
            if key == ((), ()) or key in seen:
                continue
            seen.add(key)
            kind = "Topptekst" if "header" in name else "Bunntekst"
            number = re.search(r"(\d+)\.xml", name).group(1)
            lines += [f"### {kind} {number}", ""]
            lines += [p + "\n" for p in paras]
            for target in images:
                src = "word/" + target
                dst = media / "media" / Path(target).name
                dst.parent.mkdir(parents=True, exist_ok=True)
                if not dst.exists():
                    dst.write_bytes(z.read(src))
                lines += [f"![]({media.name}/media/{dst.name})", ""]
    return (["## Topp- og bunntekst", ""] + lines) if lines else []


def convert_ooxml(path: Path, md_path: Path, media: Path, title: str, doc_date: str,
                  scale: float, min_side: int) -> tuple[int, int]:
    body = run(["pandoc", str(path), "-t", "gfm", "--wrap=none",
                f"--extract-media={media.as_posix()}"])
    # Make image references relative to the .md file.
    body = body.replace(media.as_posix() + "/", media.name + "/")
    body = body.replace(str(media) + "\\", media.name + "/")
    if path.suffix.lower() == ".docx":
        extra = docx_headers_footers(path, media)
        if extra:
            body = body.rstrip("\n") + "\n\n" + "\n".join(extra)
    count = 0
    for f in media.rglob("*"):
        if f.suffix.lower() not in {".png", ".jpg", ".jpeg"}:
            continue
        with Image.open(f) as img:
            img.load()
            small = downscale(img, scale, min_side)
        if small is not img:
            small.save(f, quality=85, optimize=True) if f.suffix.lower() != ".png" else small.save(f, optimize=True)
        count += 1
    header = f"# {title}\n\nDokumentdato: {doc_date}\n\n"
    write_lf(md_path, header + body)
    return 0, count


def merge_image_text(md_path: Path) -> int:
    """Insert hand-made transcriptions of text in images into the .md.

    The transcriptions live in a sibling file <stem>_image_text.md, which this script never
    overwrites, so they survive re-runs. Each section is headed `## <image file name>`; its
    body is inserted as a quote block after the first reference to that image.
    Returns the number of images that received text.
    """
    sidecar = md_path.with_name(md_path.stem + "_image_text.md")
    if not sidecar.exists():
        return 0
    texts: dict[str, str] = {}
    current = None
    for line in sidecar.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^## +`?([^`\s]+)`?\s*$", line)
        if m:
            current = m.group(1)
            texts[current] = ""
        elif current:
            texts[current] += line + "\n"
    lines = md_path.read_text(encoding="utf-8").split("\n")
    out: list[str] = []
    done: set[str] = set()
    for line in lines:
        out.append(line)
        for name, body in texts.items():
            if name not in done and re.search(r"/" + re.escape(name) + r"[)\"\s]", line):
                quoted = ["> " + l if l else ">" for l in body.strip("\n").split("\n")]
                out += ["", "> **Tekst i bildet:**", ">", *quoted]
                done.add(name)
    missing = set(texts) - done
    if missing:
        print(f"  WARNING: no image reference found for: {', '.join(sorted(missing))}")
    write_lf(md_path, "\n".join(out))
    return len(done)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", type=Path)
    ap.add_argument("--scale", type=float, default=0.25)
    ap.add_argument("--min-side", type=int, default=200)
    args = ap.parse_args()

    path: Path = args.input
    ext = path.suffix.lower()
    if ext == ".pdf":
        doc_date = pdf_date(path)
    elif ext in {".docx", ".pptx"}:
        doc_date = ooxml_date(path)
    else:
        sys.exit(f"Unsupported file type: {ext}")
    date_note = doc_date or f"{date.today().isoformat()} (ukjent, dagens dato brukt)"
    # Drop legacy six-digit date prefixes (e.g. "030521_") since the ISO date replaces them.
    base = re.sub(r"^\d{6}_", "", path.stem)
    stem = f"{doc_date or date.today().isoformat()}_{slugify(base)}"
    md_path = path.with_name(stem + ".md")
    media = path.with_name(stem + "_media")
    if media.exists():
        shutil.rmtree(media)
    media.mkdir()

    conv = convert_pdf if ext == ".pdf" else convert_ooxml
    pages, images = conv(path, md_path, media, path.stem, date_note, args.scale, args.min_side)
    if not any(media.iterdir()):
        media.rmdir()
    transcribed = merge_image_text(md_path)
    print(f"{md_path}: pages={pages} images={images}" + (f" image_text={transcribed}" if transcribed else ""))


if __name__ == "__main__":
    main()
