"""Compare a generated PDF against its original document: text coverage and image counts.

Original text is extracted independently of pandoc:
  PDF  -> pdftotext
  DOCX -> all <w:t> in document, headers, footers, footnotes (runs joined per paragraph)
  PPTX -> all <a:t> in slides (runs joined per paragraph)
Generated text -> pdftotext.

Text coverage = share of the original's word occurrences (case-insensitive multiset) that
also occur in the generated PDF. Words missing from the generated PDF are listed.

Usage (from project root):
    uv run python src/compare_md_pdf.py <original> <generated.pdf>
"""

import re
import subprocess
import sys
import zipfile
from collections import Counter
from pathlib import Path

RASTER_EXT = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tif", ".tiff", ".emf", ".wmf"}


def pdf_text(path: Path) -> str:
    return subprocess.run(["pdftotext", "-enc", "UTF-8", str(path), "-"], check=True,
                          capture_output=True).stdout.decode("utf-8", "replace")


def ooxml_text(path: Path) -> str:
    with zipfile.ZipFile(path) as z:
        if path.suffix.lower() == ".docx":
            parts = [n for n in z.namelist()
                     if re.fullmatch(r"word/(document|header\d*|footer\d*|footnotes)\.xml", n)]
            para, run = r"<w:p[ >].*?</w:p>", r"<w:t(?: [^>]*)?>([^<]*)</w:t>"
        else:
            parts = sorted(n for n in z.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", n))
            para, run = r"<a:p>.*?</a:p>", r"<a:t>([^<]*)</a:t>"
        out = []
        for name in parts:
            xml = z.read(name).decode("utf-8", "replace")
            for p in re.findall(para, xml, re.S):
                out.append("".join(re.findall(run, p)))
    text = "\n".join(out)
    for ent, ch in (("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"'), ("&apos;", "'")):
        text = text.replace(ent, ch)
    return text


def words(text: str) -> Counter:
    # Drop hyphens (and any following line break) on both sides, so that LaTeX line-end
    # hyphenation ("what-so-ever" -> "whatso-\never") compares equal to the original.
    text = re.sub(r"-\s*", "", text)
    return Counter(w.lower() for w in re.findall(r"\w+", text))


def pdf_image_count(path: Path) -> int:
    out = subprocess.run(["pdfimages", "-list", str(path)], check=True,
                         capture_output=True).stdout.decode("utf-8", "replace")
    objs = {l.split()[10] for l in out.splitlines()[2:] if len(l.split()) > 10 and l.split()[2] == "image"}
    return len(objs)


def main() -> None:
    orig, gen = Path(sys.argv[1]), Path(sys.argv[2])
    if orig.suffix.lower() == ".pdf":
        o_text, o_img = pdf_text(orig), pdf_image_count(orig)
    else:
        o_text = ooxml_text(orig)
        with zipfile.ZipFile(orig) as z:
            o_img = sum(1 for n in z.namelist() if "/media/" in n and Path(n).suffix.lower() in RASTER_EXT)
    o, g = words(o_text), words(pdf_text(gen))
    total = sum(o.values())
    found = sum(min(c, g[w]) for w, c in o.items())
    missing = Counter({w: c - g[w] for w, c in o.items() if c > g[w]})
    cov = 100 * found / total if total else 100.0
    print(f"{gen.name}: text {found}/{total} words ({cov:.1f} %), "
          f"raster images original={o_img} generated={pdf_image_count(gen)}")
    if missing:
        print("  missing: " + ", ".join(f"{w}×{c}" if c > 1 else w for w, c in missing.most_common(40)))


if __name__ == "__main__":
    main()
