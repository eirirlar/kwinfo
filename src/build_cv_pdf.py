# /// script
# requires-python = ">=3.10"
# dependencies = ["pymupdf", "pyyaml", "fonttools", "pillow", "numpy"]
# ///
"""Build a KodeWorks CV (v3) from Markdown straight to PDF with lualatex.

Usage (from the project root): uv run src/build_cv_pdf.py <cv.md> <out.pdf> [--keep DIR]

The source format is Markdown (src/cv_markdown.py); .yaml with the same data model is also read (tests).
Style: src/cv_pdf/cv-style.tex; extra kern pairs: src/profile_manual/kernfix.json (shared with the manual).
Fonts only from the licensed zip and TeX Live (src/font_guard.py). Photo and logo paths are relative to the
source file (absolute paths also work). lualatex, not xelatex: it loads the Norwegian bokmal hyphenation
patterns at run time. The extra kern pairs close gaps the font leaves
around j and r-f.

Robustness: all text is escaped for LaTeX (specials, Norwegian quotes/dashes, glyphs missing in the font are
dropped with a warning); every field is optional; long tokens get break hints (URLs break at slashes, never
with a hyphen); name/title/contact values are fitted by measuring the font; the front page measures the
intro and falls back to a smaller or stacked layout; page breaks inside projects and lists are controlled
(no lone keyword row, at least three lines on each side, no list split to one row); if the last page ends up
under 40 % full, the build is retried with tighter spacing.

Images: logos are trimmed (transparent, white or almost white margin; the drawn extent for SVG/PDF) and
scaled to a roughly constant optical area; photos are cropped to the frame (cover) around a focus point.
"""
import argparse
import json
import math
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

import numpy as np
import pymupdf
import yaml
from fontTools.ttLib import TTFont
from PIL import Image, ImageOps

import font_guard  # fail if a font comes from the OS instead of the repo/TeX Live
from project_tmp import work_dir  # work folders in <project root>/tmp/ (CLAUDE.md)

ROOT = Path(__file__).resolve().parent.parent
HERE = ROOT / "src" / "cv_pdf"
KERNFIX = ROOT / "src" / "profile_manual" / "kernfix.json"  # extra kern pairs, shared with the manual
STYLE = HERE / "cv-style.tex"
ASSETS = ROOT / "deliverable" / "visualprofile" / "profile" / "assets"
FONT_ZIP = (ROOT / "background" / "visualprofile" / "Fonts" / "Non Natural Grotesk"
            / "Desktop variant" / "NonNaturalGroteskFontFamily-hqlqfp.zip")
BRK, HARD = "\ue000", "\ue001"      # sentinels: optional break / hyphenated break
WARNINGS: list[str] = []
SPECIAL = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_",
           "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}

LABELS = {
    "nb": dict(customer="Kunde", project="Prosjekt", period="Periode", description="Beskrivelse",
               keywords="Nøkkelord", experience="Erfaring", general="Generelt", work="Arbeidserfaring",
               education="Utdanning", certs="Sertifiseringer", about="Om {first}", about_nameless="Om",
               skills="Teknisk kompetanse", phone="Telefon", email="E-post", years="Erfaring",
               years_fmt="{n} år", langs="Språk", default_project="Prosjekt"),
    "en": dict(customer="Customer", project="Project", period="Period", description="Description",
               keywords="Keywords", experience="Experience", general="General", work="Work experience",
               education="Education", certs="Certifications", about="About {first}", about_nameless="About",
               skills="Technical skills", phone="Phone", email="E-mail", years="Experience",
               years_fmt="{n} years", langs="Languages", default_project="Project"),
}


# ------------------------------------------------------------------ font metrics / glyphs
class Fonts:
    def __init__(self, folder: Path):
        self.faces = {}
        for key in ("Regular", "Light", "Medium"):
            f = TTFont(str(folder / f"NON Natural Grotesk-{key}.otf"))
            self.faces[key] = (f.getBestCmap(), f["hmtx"], f["head"].unitsPerEm)
        self.codes = set().union(*(set(c.keys()) for c, _, _ in self.faces.values()))

    def has(self, ch: str) -> bool:
        return ord(ch) in self.codes

    def width_mm(self, text: str, size_pt: float, face: str = "Regular") -> float:
        cmap, hmtx, upm = self.faces[face]
        w = sum(hmtx[cmap.get(ord(c), ".notdef")][0] if ord(c) in cmap else upm * 0.5 for c in text)
        return w / upm * size_pt * 0.3528 * 1.02

    def wrap(self, text: str, size_pt: float, face: str, max_mm: float) -> list[str]:
        lines, cur = [], ""
        for word in text.split():
            trial = (cur + " " + word).strip()
            if cur and self.width_mm(trial, size_pt, face) > max_mm:
                lines.append(cur)
                cur = word
            else:
                cur = trial
        return lines + ([cur] if cur else [])


FONTS: Fonts | None = None


def est_lines(raw: str, width_mm: float, size: float = 9.5) -> int:
    """Estimated number of lines a paragraph takes (used to decide where page breaks are allowed)."""
    plain = re.sub(r"\*\*", "", str(raw))
    return max(1, len(FONTS.wrap(plain, size, "Regular", width_mm)))


# ------------------------------------------------------------------ text escaping
def typography(s: str) -> str:
    s = s.replace("---", "\u2014").replace("--", "\u2013")
    s = re.sub(r"(?<=\s)-(?=\s)", "\u2013", s)
    s = s.replace("...", "\u2026")
    s = re.sub(r"(\d)[ \t]+%", "\\1\u00a0%", s)   # hard space between a number and the percent sign
    out, prev = [], " "
    for ch in s:
        if ch == '"':
            out.append("\u00ab" if prev in " \t\n([{\u2013\u2014" else "\u00bb")
        elif ch in "\u201c\u201e":
            out.append("\u00ab")
        elif ch == "\u201d":
            out.append("\u00bb")
        elif ch == "'":
            out.append("\u2018" if prev in " \t\n([{" else "\u2019")
        else:
            out.append(ch)
        prev = ch
    return "".join(out)


def is_urlish(w: str) -> bool:
    return bool(re.search(r"https?://|www\.|@|^/|[A-Za-z0-9]/[A-Za-z0-9_.-]{3,}/", w))


def add_break_hints(s: str) -> str:
    """Break points in long unbreakable tokens. URLs and e-mail addresses break at / . @ ? = & and are never hyphenated."""
    def fix(m: re.Match) -> str:
        w = m.group(0)
        if len(w) < 14:
            return w
        url = is_urlish(w)
        w = re.sub(r"([/_.@=&?:,;+#-])(?=\w)", lambda k: k.group(1) + BRK, w) if url else \
            re.sub(r"([/_.@=&?:,;+])(?=\w)", lambda k: k.group(1) + BRK, w)
        parts = re.split(f"[{BRK}\\-\u2013]", w)
        if max(len(p) for p in parts) > 22:
            hard = BRK if url else HARD
            w = re.sub(r"(\w{14})(?=\w)", lambda k: k.group(1) + hard, w)
        return w
    return re.sub(r"\S+", fix, s)


def esc(value, hints: bool = True) -> str:
    """Escape arbitrary text for LaTeX. **bold** gives Medium weight."""
    if value is None:
        return ""
    s = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", str(value))
    s = typography(re.sub(r"\s*\n\s*", " ", s).strip())
    if hints:
        s = add_break_hints(s)
    out = []
    for i, part in enumerate(re.split(r"\*\*(.+?)\*\*", s)):
        t = []
        for ch in part:
            if ch == BRK:
                t.append(r"\allowbreak{}")
            elif ch == HARD:
                t.append(r"\discretionary{-}{}{}")
            elif ch in SPECIAL:
                t.append(SPECIAL[ch])
            elif ch == "\u00a0":
                t.append("~")
            elif ch == "\u00ad":
                t.append(r"\-")
            elif ch == "\u200b":
                t.append(r"\allowbreak{}")
            elif ch == "\ufeff":
                pass
            elif ch.isspace() or ord(ch) < 128 or (FONTS and FONTS.has(ch)):
                t.append(ch)
            else:
                WARNINGS.append(f"glyph U+{ord(ch):04X} {ch!r} not in font; dropped")
                continue
        text = "".join(t)
        out.append(r"{\kwmedium " + text + "}" if i % 2 == 1 else text)
    return re.sub(r"(\\allowbreak\{\})+", r"\\allowbreak{}", "".join(out))


def esc_nb(value) -> str:
    """Skill / keyword text: no hyphenation, break only at spaces and slashes (a hyphen never breaks)."""
    raw = re.sub(r"\S{27,}", lambda m: re.sub(r"(\S{20})(?=\S)", lambda k: k.group(1) + BRK, m.group(0)), str(value))
    s = esc(raw, hints=False)   # absurdly long tokens get plain break points (no hyphen)
    return s.replace("-", r"\mbox{-}").replace("/", r"/\allowbreak{}")


def bind_tail(text) -> str:
    """Bind the last two words with a no-break space so a paragraph never ends on a single short word."""
    t = str(text).strip()
    words = t.split(" ")
    if len(words) >= 4 and len(words[-1]) <= 14 and not words[-2].endswith(("-", "\u2013")):
        return " ".join(words[:-1]) + "\u00a0" + words[-1]
    return t


def period_tex(value) -> str:
    s = esc(value)
    s = re.sub(r"\s+(?:\\allowbreak\{\})?([\u2013\u2014])\s+", r"\\nobreakspace{}\1\\nobreakspace{}", s)
    if "(" not in str(value) and len(str(value)) <= 26:
        return r"\mbox{" + s + "}"
    # period with an addition: break only before the parenthesis, never inside it ("2011 - 2018" / "(40 % stilling)")
    return re.sub(r"\([^()]*\)", lambda m: r"\mbox{" + re.sub(r"\s+", "~", m.group(0)) + "}", s)


# ------------------------------------------------------------------ data coercion
def as_text(v) -> str:
    return "" if v is None else str(v).strip()


def as_list(v) -> list:
    if v is None:
        return []
    if isinstance(v, (list, tuple)):
        return [x for x in v if x is not None and str(x).strip()]
    return [x for x in re.split(r"\n+", str(v)) if x.strip()]


def as_dicts(v) -> list[dict]:
    return [x for x in (v if isinstance(v, list) else []) if isinstance(x, dict)]


def load_cv(path: Path) -> dict:
    """Source file to the CV dict: YAML via yaml.safe_load, Markdown via cv_markdown.parse."""
    if path.suffix.lower() in (".md", ".markdown"):
        import cv_markdown  # src/cv_markdown.py
        cv = cv_markdown.parse(path)
    else:
        cv = yaml.safe_load(path.read_text(encoding="utf-8"))
    cv = cv or {}
    if not isinstance(cv, dict):
        raise SystemExit("CV source must be a mapping")
    return cv


# ------------------------------------------------------------------ assets
def write_kernfix(work: Path) -> None:
    """kernfix.json (extra kern pairs per face, font units) -> kernfix.lua for luaotfload (features kwfr/kwfl/kwfm)."""
    fixes = json.loads(KERNFIX.read_text(encoding="utf-8"))
    lua = []
    for face, pairs in fixes.items():
        data = {}
        for pair, val in pairs.items():
            data.setdefault(ord(pair[0]), {})[ord(pair[1])] = val
        body = ",".join(f"[{a}]={{" + ",".join(f"[{c}]={v}" for c, v in d.items()) + "}" for a, d in data.items())
        lua.append(f'fonts.handlers.otf.addfeature{{name="kwf{face[0].lower()}",type="kern",data={{{body}}}}}')
    (work / "kernfix.lua").write_text(chr(10).join(lua) + chr(10), encoding="utf-8")


def svg_to_pdf_bytes(svg: Path) -> bytes:
    return pymupdf.open(stream=svg.read_bytes(), filetype="svg").convert_to_pdf()


def resolve(path, base: Path) -> Path | None:
    if not as_text(path):
        return None
    src = Path(str(path))
    if not src.is_absolute():
        src = base / src
    if not src.exists():
        WARNINGS.append(f"image not found: {path}")
        return None
    return src


# --- logos -----------------------------------------------------------------------------------------
LOGO_AREA = 230.0   # target optical area in mm2
LOGO_MAX_H, LOGO_MAX_W = 13.0, 34.0
LOGO_MIN_DPI = 200


def trim_vector(data: bytes, dest: Path) -> tuple[float, float, float]:
    """Crop a one-page vector PDF to its drawn extent; returns (width, height in pt, ink density guess)."""
    doc = pymupdf.open(stream=data, filetype="pdf")
    page = doc[0]
    rects = [pymupdf.Rect(d["rect"]) for d in page.get_drawings() if d["rect"].width > 0 or d["rect"].height > 0]
    for img in page.get_images(full=True):
        rects += list(page.get_image_rects(img[0]))
    rects += [pymupdf.Rect(b[:4]) for b in page.get_text("blocks")]
    rects = [r & page.rect for r in rects if not r.is_empty]
    if rects:
        box = rects[0]
        for r in rects[1:]:
            box |= r
        box = box + (-0.3, -0.3, 0.3, 0.3)
        box &= page.rect
        if not box.is_empty:
            page.set_cropbox(box)
    r = page.cropbox
    doc.save(str(dest))
    return r.width, r.height, 0.5


def trim_raster(src: Path, dest: Path) -> tuple[int, int, float]:
    """Trim transparent / white / almost white margins; almost white becomes pure white. Returns px size and ink density."""
    im = Image.open(src)
    im.load()
    if im.mode in ("P", "PA", "LA", "L", "1", "CMYK", "I;16", "I"):
        im = im.convert("RGBA")
    elif im.mode != "RGBA":
        im = im.convert("RGBA")
    a = np.array(im)
    alpha = a[..., 3]
    has_alpha = bool((alpha < 250).any())
    rgb = a[..., :3]
    near_white = rgb.min(axis=2) >= 238
    if has_alpha:
        ink = alpha > 24
        ink &= ~(near_white & (alpha > 200) & False)
    else:
        ink = ~near_white
    if not ink.any():
        im.save(dest)
        return im.width, im.height, 0.5
    ys, xs = np.nonzero(ink)
    x0, x1, y0, y1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1
    a = a[y0:y1, x0:x1].copy()
    ink = ink[y0:y1, x0:x1]
    if not has_alpha:
        nw = a[..., :3].min(axis=2) >= 238
        a[nw, :3] = 255
    Image.fromarray(a, "RGBA").save(dest)
    return a.shape[1], a.shape[0], float(ink.mean())


def prepare_logo(path, base: Path, work: Path, tag: str):
    """Returns (relative file, width mm, height mm) or None. Size from a constant optical area."""
    src = resolve(path, base)
    if src is None:
        return None
    try:
        if src.suffix.lower() in (".svg", ".pdf"):
            data = svg_to_pdf_bytes(src) if src.suffix.lower() == ".svg" else src.read_bytes()
            dest = work / "img" / f"{tag}.pdf"
            wpt, hpt, dens = trim_vector(data, dest)
            aspect, px_w = wpt / hpt, None
        else:
            dest = work / "img" / f"{tag}.png"
            pw, ph, dens = trim_raster(src, dest)
            aspect, px_w = pw / ph, pw
    except Exception as exc:  # noqa: BLE001
        WARNINGS.append(f"logo unusable ({src.name}: {exc})")
        return None
    area = LOGO_AREA * min(1.2, max(0.85, (0.45 / max(dens, 0.05)) ** 0.25))
    h = math.sqrt(area / aspect)
    w = aspect * h
    if h > LOGO_MAX_H:
        h, w = LOGO_MAX_H, aspect * LOGO_MAX_H
    if w > LOGO_MAX_W:
        w, h = LOGO_MAX_W, LOGO_MAX_W / aspect
    if px_w and px_w / (w / 25.4) < LOGO_MIN_DPI:
        WARNINGS.append(f"low resolution logo {src.name}: {px_w / (w / 25.4):.0f} dpi at {w:.0f} mm")
    return f"img/{dest.name}", w, h


# --- photo -----------------------------------------------------------------------------------------
PHOTO_W, PHOTO_H = 60.0, 74.0
PX0, PY0 = 24.0, 22.0
PX1, PY1 = PX0 + PHOTO_W, PY0 + PHOTO_H
CONTACT_X = PX1 + 12.0


def subject_x(im: Image.Image, crop_w: float) -> float:
    """Horizontal focus (0..1) for a landscape photo: the window of the crop width with the most edge detail
    (a face and clothes against a plain wall), mildly biased towards the centre."""
    g = np.asarray(im.convert("L").resize((max(2, im.width // 4), max(2, im.height // 4))), dtype=float)
    energy = np.abs(np.diff(g, axis=1)).sum(axis=0)
    energy = np.convolve(energy, np.ones(3) / 3, mode="same")
    w = max(1, round(crop_w / 4))
    if w >= len(energy):
        return 0.5
    csum = np.concatenate([[0.0], np.cumsum(energy)])
    scores = csum[w:] - csum[:-w]
    centre = (np.arange(len(scores)) + w / 2) / len(energy)
    best = int(np.argmax(scores * (1 - 0.35 * np.abs(centre - 0.5))))
    return float((best + w / 2) / len(energy))


def prepare_photo(path, focus, base: Path, work: Path):
    """Crop the photo to the frame ratio (cover) around the focus point; returns the relative file or None."""
    src = resolve(path, base)
    if src is None:
        return None
    try:
        if src.suffix.lower() in (".svg", ".pdf"):
            WARNINGS.append("photo must be a raster image; placeholder used")
            return None
        im = ImageOps.exif_transpose(Image.open(src))
        if im.mode in ("RGBA", "LA", "P"):
            im = im.convert("RGBA")
            bg = Image.new("RGB", im.size, (255, 255, 255))
            bg.paste(im, mask=im.split()[3])
            im = bg
        else:
            im = im.convert("RGB")
        iw, ih = im.size
        fx, fy = 0.5, 0.35
        given = isinstance(focus, (list, tuple)) and len(focus) == 2
        if given:
            try:
                fx, fy = float(focus[0]), float(focus[1])
            except (TypeError, ValueError):
                WARNINGS.append("photo_focus must be [x, y] as fractions; default used")
        ratio = PHOTO_W / PHOTO_H
        if iw / ih > ratio:
            cw, ch = ih * ratio, float(ih)
        else:
            cw, ch = float(iw), iw / ratio
        if not given and iw - cw > 2:
            fx = subject_x(im, cw)   # no photo_focus: put the window where the picture has most detail
        left = min(max(fx * iw - cw / 2, 0), iw - cw)
        top = min(max(fy * ih - ch / 2, 0), ih - ch)
        im = im.crop((round(left), round(top), round(left + cw), round(top + ch)))
        if im.width / (PHOTO_W / 25.4) < 150:
            WARNINGS.append(f"low resolution photo: {im.width / (PHOTO_W / 25.4):.0f} dpi")
        if im.width > 1800:
            im = im.resize((1800, round(1800 / ratio)), Image.LANCZOS)
        dest = work / "img" / "photo.jpg"
        im.save(dest, quality=92)
        return "img/photo.jpg"
    except Exception as exc:  # noqa: BLE001
        WARNINGS.append(f"photo unusable ({exc}); placeholder used")
        return None


def photo_tex(rel: str | None) -> str:
    if rel:
        return (rf"\node[anchor=north west,inner sep=0pt] at ({PX0},{PY0}) "
                rf"{{\includegraphics[width={PHOTO_W}mm,height={PHOTO_H}mm]{{{rel}}}}};")
    cx = PX0 + PHOTO_W / 2
    return (rf"\fill[kwgrey] ({PX0},{PY0}) rectangle ({PX1},{PY1});"
            rf"\begin{{scope}}\clip ({PX0},{PY0}) rectangle ({PX1},{PY1});"
            rf"\fill[kwgrey!78!black] ({cx},{PY0 + 27}) ellipse (10.6 and 12.4);"
            rf"\fill[kwgrey!78!black] ({cx - 7},{PY0 + 36}) rectangle ({cx + 7},{PY0 + 52});"
            rf"\fill[kwgrey!78!black] ({cx - 25},{PY1 + 20}) .. controls ({cx - 25},{PY0 + 52}) and ({cx - 13},{PY0 + 44}) .. "
            rf"({cx},{PY0 + 44}) .. controls ({cx + 13},{PY0 + 44}) and ({cx + 25},{PY0 + 52}) .. ({cx + 25},{PY1 + 20}) -- cycle;"
            r"\end{scope}")


# ------------------------------------------------------------------ header
def header_tex(cv: dict, base: Path, work: Path, lab: dict) -> str:
    name = as_text(cv.get("name")) or "Navn"
    title = as_text(cv.get("title"))
    photo = prepare_photo(cv.get("photo"), cv.get("photo_focus"), base, work)
    L = [r"\noindent\begin{tikzpicture}[remember picture,overlay,x=1mm,y=-1mm,shift={(current page.north west)}]",
         photo_tex(photo),
         rf"\fill[kwgreen] ({PX1 + 3},{PY0}) rectangle ({PX1 + 4.3},{PY1 + 4.3});"
         rf"\fill[kwgreen] (20,{PY1 + 3}) rectangle ({PX1 + 4.3},{PY1 + 4.3});"]
    langs = cv.get("languages")
    langs = [x.strip() for x in langs.split(",")] if isinstance(langs, str) else [as_text(x) for x in as_list(langs)]
    entries = []
    if as_text(cv.get("phone")):
        entries.append((lab["phone"], as_text(cv["phone"])))
    if as_text(cv.get("email")):
        entries.append((lab["email"], as_text(cv["email"])))
    if as_text(cv.get("experience_years")):
        entries.append((lab["years"], lab["years_fmt"].format(n=as_text(cv["experience_years"]))))
    if [x for x in langs if x]:
        entries.append((lab["langs"], ", ".join(x for x in langs if x)))
    # title (last line on the photo's bottom edge) and name above it; right-aligned at x = 190
    avail = 190 - CONTACT_X - 2
    tsize = next((s for s in (14, 12.5, 11) if FONTS.width_mm(title, s, "Light") <= avail), 11)
    tlines = FONTS.wrap(title, tsize, "Light", avail) if title else []
    tlead = tsize * 1.3 * 0.3528
    nodes = []
    for k, ln in enumerate(tlines):
        y = PY1 - (len(tlines) - 1 - k) * tlead
        nodes.append(rf"\node[anchor=base east,inner sep=0pt] at (190,{y:.2f}) "
                     rf"{{\kwsize{{{tsize}}}{{{tsize * 1.3:.1f}}}\kwlight\color{{kwdarkgreen}} {esc(ln, hints=False)}}};")
    first_title_y = PY1 - max(len(tlines) - 1, 0) * tlead
    nsize = next((s for s in (30, 27, 24, 21, 18) if FONTS.width_mm(name, s, "Light") <= avail), None)
    if nsize is None:
        nsize = 17
        nlines = FONTS.wrap(name, nsize, "Light", avail)
    else:
        nlines = [name]
    nlead = nsize * 1.08 * 0.3528
    name_y = first_title_y - (tsize * 0.72 * 0.3528 + 5.5 + (1.5 if len(tlines) == 2 else 0) if title else 0)
    for k, ln in enumerate(nlines):
        y = name_y - (len(nlines) - 1 - k) * nlead
        nodes.append(rf"\node[anchor=base east,inner sep=0pt] at (190,{y:.2f}) "
                     rf"{{\kwsize{{{nsize}}}{{{nsize * 1.1:.1f}}}\kwlight {esc(ln, hints=False)}}};")
    name_top = name_y - (len(nlines) - 1) * nlead - nsize * 0.72 * 0.3528
    # contact values: 10 pt, down to 9 pt if that avoids a break; otherwise wrapped (never smaller text)
    cw = 175 - CONTACT_X
    prepared = []
    for i, (lb, val) in enumerate(entries):
        # below the symbol (y > ~54 mm) the value may run further right
        cwi = cw if PY0 + 2.4 + i * 15 < 54 else cw + 11
        size = 10.0
        if FONTS.width_mm(val, 10) > cwi and FONTS.width_mm(val, 9) <= cwi:
            size = 9.0
        nl = 1 if FONTS.width_mm(val, size) <= cwi else max(2, len(FONTS.wrap(val, size, "Regular", cwi)))
        prepared.append((lb, val, size, nl, cwi))
    extra_total = 4.3 * sum(nl - 1 for _, _, _, nl, _ in prepared)
    pitch = 15.0
    if len(prepared) > 1 and (len(nlines) > 1 or len(tlines) > 1):
        pitch = max(8.3, min(15.0, (name_top - 3 - PY0 - 2.4 - 5.4 - 1.5 - extra_total) / (len(prepared) - 1)))
    shift = 0.0
    for i, (lb, val, size, nl, cwi) in enumerate(prepared):
        y = PY0 + 2.4 + i * pitch + shift
        if nl > 1:
            shift += 4.3 * (nl - 1)
            L.append(rf"\kwcontactitem{{{CONTACT_X}}}{{{y:.1f}}}{{{lb}}}{{{size:.1f}}}"
                     rf"{{\parbox[t]{{{cwi:.0f}mm}}{{\RaggedRight {esc(val, hints=True)}}}}}")
        else:
            L.append(rf"\kwcontactitem{{{CONTACT_X}}}{{{y:.1f}}}{{{lb}}}{{{size:.1f}}}{{{esc(val, hints=False)}}}")
    L.append(r"\node[anchor=north east,inner sep=0pt] at (190,22) "
             r"{\includegraphics[width=17mm]{img/kw-symbol-svart-med-gronn-strek.pdf}};")
    L += nodes
    L.append(rf"\end{{tikzpicture}}\par\vspace*{{{PY1 + 4.3 - 22 + 16:.1f}mm}}")
    return "\n".join(L)


# ------------------------------------------------------------------ intro (about + skills)
def skill_columns(items: list[str], widths_mm: list[float]) -> str:
    """Items in len(widths) columns (column-major), each column a box of the given width."""
    n = len(widths_mm)
    per = math.ceil(len(items) / n)
    cols = []
    for k in range(n):
        chunk = items[k * per:(k + 1) * per]
        if chunk:
            cols.append(rf"\kwitems{{{widths_mm[k]:g}mm}}{{" + "".join(rf"\kwitem{{{skill_item(i, widths_mm[k])}}}" for i in chunk) + "}")
    return r"\hfill ".join(cols) + r"\par"


def skill_item(i: str, col_mm: float) -> str:
    t = esc_nb(i)
    return r"\mbox{" + t + "}" if FONTS.width_mm(i, 9.5) <= col_mm - 4.4 else t


def choose_columns(items: list[str], total_mm: float, options: list[int]) -> list[float]:
    """Column widths for a skill group: as many columns as the longest item allows (1 to 3)."""
    longest = max(FONTS.width_mm(i, 9.5) for i in items) + 4.4 + 0.8
    gap = 2.0
    for n in sorted(options, reverse=True):
        w = (total_mm - gap * (n - 1)) / n
        if longest <= w or n == min(options):
            return [w] * n


def about_block(paras: list, name: str, lede: str, lab: dict) -> str:
    first = name.split()[0] if name else ""
    head = lab["about"].format(first=first) if first else lab["about_nameless"]
    out = [rf"\kwhd{{{esc(head, hints=False)}}}"]
    prev_bullet = False
    for p in paras:
        p = str(p).strip()
        m = re.match(r"^[-*\u2022]\s+(\S.*)$", p)
        if m:
            out.append(rf"\kwabullet{{{lede}}}{{{esc(bind_tail(m.group(1)))}}}")
            prev_bullet = True
        else:
            if prev_bullet:
                out.append(r"\vspace{\kwq}")
            out.append(rf"{{\RaggedRight{lede} {esc(bind_tail(p))}\par}}\vspace{{\kwh}}")
            prev_bullet = False
    return "".join(out) + (r"\vspace{\kwh}" if prev_bullet else "")


def intro_tex(cv: dict, lab: dict) -> str:
    name = as_text(cv.get("name"))
    paras = as_list(cv.get("about"))
    groups = [(as_text(g.get("group")), [as_text(i) for i in as_list(g.get("items"))])
              for g in as_dicts(cv.get("skills"))]
    groups = [(t, it) for t, it in groups if it]
    if not paras and not groups:
        return ""
    about10 = about_block(paras, name, r"\kwlede", lab) if paras else ""
    about95 = about_block(paras, name, r"\kwlededense", lab) if paras else ""
    s2 = s3 = s5 = ""
    if groups:
        s2 = rf"\kwhd{{{esc(lab['skills'], hints=False)}}}"
        s3, s5 = "", s2
        cont = esc(lab["skills"] + (" (cont.)" if lab is LABELS["en"] else " (forts.)"), hints=False)
        for gi, (t, items) in enumerate(groups, 1):
            hd = rf"\kwgrouphd{{{esc(t.upper(), hints=False)}}}" if t else ""
            s2 += hd + skill_columns(items, choose_columns(items, 64, [1, 2])) + r"\vspace{\kwf}"
            s5 += hd + skill_columns(items, choose_columns(items, 70, [1, 2])) + r"\vspace{\kwf}"
            top = rf"\kwhd{{{esc(lab['skills'], hints=False)}}}" if gi == 1 else ""
            s3 += (rf"\kwsg{{{gi}}}{{{cont}}}{{{top}{hd}}}{{"
                   + skill_columns(items, choose_columns(items, 170, [1, 2, 3, 4])) + r"}")
    return rf"\kwintro{{{about10}}}{{{about95}}}{{{s2}}}{{{s3}}}{{{s5}}}"


# ------------------------------------------------------------------ projects and lists
def is_subhead(line: str) -> str | None:
    m = re.fullmatch(r"\*\*(.+?)\*\*:?", line.strip())
    return m.group(1).strip() if m else None


def same_name(a, b) -> bool:
    return as_text(a).casefold() == as_text(b).casefold() and as_text(a) != ""


def project_tex(p: dict, base: Path, work: Path, idx: int, lab: dict) -> tuple[str, float]:
    role = (as_text(p.get("role")) or as_text(p.get("project")) or as_text(p.get("customer"))
            or lab["default_project"])
    customer, project = as_text(p.get("customer")), as_text(p.get("project"))
    logo = None
    if not re.search(r"kodeworks", customer, re.I):   # the name stroke closes the document already
        logo = prepare_logo(p.get("logo"), base, work, f"logo{idx}")
    TEXT_W, BUL_W = 128.0, 123.0
    rows = []   # dicts: tex, lines, kind
    if customer:
        rows.append(dict(kind="head", label=lab["customer"], tex=esc(customer), lines=1))
    if project and not same_name(project, customer):
        rows.append(dict(kind="head", label=lab["project"], tex=r"{\kwmedium " + esc(project) + "}", lines=1))
    if as_text(p.get("period")):
        rows.append(dict(kind="head", label=lab["period"], tex=period_tex(p["period"]), lines=1))
    label = lab["description"]
    for ln in as_list(p.get("description")):
        ln = str(ln).strip()
        sub = is_subhead(ln)
        m = re.match(r"^(?:[-*\u2022\u2013])\s+(\S.*)$", ln)
        if sub:
            rows.append(dict(kind="sub", label=label if label else "", tex=esc(sub), lines=1))
            label = ""
        elif m:
            rows.append(dict(kind="bullet", label=label, tex=esc(bind_tail(m.group(1))),
                             lines=est_lines(m.group(1), BUL_W)))
            label = ""
        else:
            rows.append(dict(kind="text", label=label, tex=esc(bind_tail(ln)), lines=est_lines(ln, TEXT_W)))
            label = ""
    kws = p.get("keywords")
    kws = re.split(r",\s*", kws) if isinstance(kws, str) else as_list(kws)
    kws = [as_text(k) for k in kws if as_text(k)]
    if kws:
        parts = [r"\mbox{" + esc_nb(k) + "}" if len(k) <= 22 else esc_nb(k) for k in kws]
        rows.append(dict(kind="kw", label=lab["keywords"], tex=r"\kwnh " + r"\kwsep ".join(parts),
                         lines=est_lines(", ".join(kws), TEXT_W)))
    if not rows:
        rows.append(dict(kind="head", label="", tex=r"\mbox{}", lines=1))
    # where a page break may fall: the top stays together with the first three description lines,
    # at least three lines remain on each side, and the keyword row never stands alone
    total_after = [sum(r["lines"] for r in rows[i + 1:]) for i in range(len(rows))]
    desc_cum, c = [], 0
    for r in rows:
        if r["kind"] in ("text", "bullet", "sub"):
            c += r["lines"]
        desc_cum.append(c)
    n_head = sum(r["kind"] == "head" for r in rows)
    # space the unbreakable top of the block needs: head rows plus description rows until three lines are reached
    first_lines, acc = 0, 0
    for r in rows:
        if r["kind"] in ("text", "bullet", "sub"):
            take = r["lines"] if (r["lines"] < 4 or r["kind"] != "text") else 2
            first_lines += take
            acc += r["lines"]
            if acc >= 2:
                break
    need = 3.6 + 1.3 * n_head + 1.15 * max(first_lines, 2) + 0.8
    if logo:
        need = max(need, 3.5 + logo[2] / 4.94 + 1.0)
    out = [rf"\kwheading[{need:.1f}]{{" + esc(role) + "}", r"\begin{kwblock}"]
    if logo:
        out.append(rf"\kwlogo{{{logo[0]}}}{{{logo[1]:.2f}}}{{{logo[2]:.2f}}}\setlength{{\kwlw}}{{{logo[1] + 6:.1f}mm}}")
    count = 0
    for i, r in enumerate(rows):
        count += 1
        hold = (r["kind"] in ("head", "sub") or desc_cum[i] < 2 or total_after[i] < 2) and i < len(rows) - 1
        if hold:
            out.append(r"\kwholdtrue")
        if r["kind"] == "sub":
            out.append(r"\vspace{\kwq}")
        if r["kind"] == "bullet":
            out.append(rf"\kwbulletl{{{r['label']}}}{{{r['tex']}}}" if r["label"] else rf"\kwbullet{{{r['tex']}}}")
        else:
            macro = r"\kwrowr" if logo and count <= 3 else r"\kwrow"
            tex = r"\kwsubhd{" + r["tex"] + "}" if r["kind"] == "sub" else r["tex"]
            out.append(f"{macro}{{{r['label']}}}{{{tex}}}")
    out.append(r"\end{kwblock}")
    return "\n".join(out), need


def period_width(rows: list[dict]) -> float:
    """Period column width (mm), sized for the typical periods (70th percentile); longer ones wrap inside it."""
    ws = sorted(FONTS.width_mm(r["period"], 9.5) for r in rows if r["period"])
    if not ws:
        return 0.0
    ref = ws[min(len(ws) - 1, int(len(ws) * 0.7))]
    # Periods of up to 26 characters are set unbreakable (\mbox), so the column must hold the widest of
    # them; the metric estimate runs ~5 % short of the set width, hence the margin.
    # Longer periods break only before an addition in parentheses, which is itself unbreakable.
    pieces = []
    for r in rows:
        p = str(r["period"] or "")
        pieces += [p] if ("(" not in p and len(p) <= 26) else [x for x in re.split(r" (?=\()", p) if x]
    floor = max((FONTS.width_mm(x, 9.5) for x in pieces), default=0.0) * 1.06 + 4.5
    # typical periods fit on one line; a long outlier gets at most two lines in the column
    return min(40.0, max(ref + 4.5, ws[-1] / 2 + 6.0, floor))


def column_widths(rows: list[dict], pw: float, total: float = 160.5) -> tuple[float, float, float]:
    """Widths (middle, right, gap) in mm from the measured natural text widths.
    Everything fits: nothing wraps and the surplus goes to the middle column. Otherwise the column with the
    longest text shrinks first; the right column keeps at least ~30 % of the width (or its natural width)."""
    has_side = any(r["side"] for r in rows)
    gap = 5.0 if has_side else 0.0
    avail = total - pw - gap
    nat_m = max([FONTS.width_mm(r["main"], 9.5) for r in rows] + [20.0]) + 1.0
    nat_s = (max([FONTS.width_mm(r["side"], 9.5) for r in rows] + [0.0]) + 1.0) if has_side else 0.0
    if nat_m + nat_s <= avail:
        return avail - nat_s, nat_s, gap
    lo_s = min(nat_s, 0.30 * total) if has_side else 0.0
    lo_m = min(nat_m, 45.0)
    m, s_ = nat_m, nat_s
    while m + s_ > avail + 0.01:
        can_m, can_s = m - lo_m > 0.5, s_ - lo_s > 0.5
        if not (can_m or can_s):
            break
        if can_m and (m >= s_ or not can_s):
            m -= min(1.0, m - lo_m)
        else:
            s_ -= min(1.0, s_ - lo_s)
    return avail - s_, s_, gap


def list_block(title: str, rows: list[dict], grid: tuple | None = None) -> str:
    """A 'Generelt' list. rows: dicts with period, main, side (raw text) and desc (list of raw lines)."""
    rows = [r for r in rows if r["period"] or r["main"] or r["side"] or r["desc"]]
    if not rows:
        return ""
    if grid is None:
        pw = period_width(rows)
        grid = (pw,) + column_widths(rows, pw)
    pw, mw, sw, gap = grid
    n = len(rows)
    need = 6.0
    if n <= 8:
        # a short list is never split over a page break: it moves as a whole together with its title
        lines = sum(max(est_lines(r["main"], mw), est_lines(r["side"], max(sw, 20.0)) if r["side"] else 1,
                        est_lines(r["period"], max(pw - 4, 15.0)) if r["period"] else 1)
                    + sum(est_lines(d, 125.0) for d in r["desc"] if str(d).strip()) for r in rows)
        need = 3.0 + lines * 1.0 + 0.55 * n
    out = [rf"\kwheading[{need:.1f}]{{" + esc(title, hints=False) + "}", r"\begin{kwblock}"]
    for i, r in enumerate(rows):
        if n <= 8:
            boundary_hold = i < n - 1
        else:   # longer list: at least three rows on each side of a break
            boundary_hold = i < n - 1 and (i < 2 or i >= n - 3)
        items = [("row", None)] + [("d", x) for x in (str(y).strip() for y in r["desc"]) if x]
        for k, (kind, dl) in enumerate(items):
            if k < len(items) - 1 or boundary_hold:
                out.append(r"\kwholdtrue")
            if kind == "row":
                per = period_tex(r["period"]) if r["period"] else ""
                out.append(rf"\kwgrow{{{pw:.1f}}}{{{mw:.1f}}}{{{sw:.1f}}}{{{gap:.1f}}}{{{per}}}{{{esc(r['main'])}}}{{{esc(r['side'])}}}")
            else:
                sub = is_subhead(dl)
                m = re.match(r"^(?:[-*\u2022\u2013])\s+(\S.*)$", dl)
                if sub:
                    out.append(rf"\kwgdesc{{{pw:.1f}}}{{\kwmedium {esc(sub)}}}")
                elif m:
                    out.append(rf"\kwgbul{{{pw:.1f}}}{{{esc(bind_tail(m.group(1)))}}}")
                else:
                    out.append(rf"\kwgdesc{{{pw:.1f}}}{{{esc(bind_tail(dl))}}}")
    out.append(r"\end{kwblock}")
    return "\n".join(o for o in out if o), need


def build_tex(cv: dict, base: Path, work: Path, lab: dict) -> str:
    L = [r"\documentclass[10pt,a4paper]{article}", r"\usepackage{polyglossia}",
         r"\input{cv-style.tex}", r"\begin{document}", r"\kwhyph", header_tex(cv, base, work, lab), intro_tex(cv, lab)]
    projects = as_dicts(cv.get("projects"))
    if projects:
        built = [project_tex(p, base, work, i, lab) for i, p in enumerate(projects)]
        # the section title keeps company with the whole unbreakable top of the first project
        L.append(rf"\kwsection{{{esc(lab['experience'], hints=False)}}}{{{5.2 + built[0][1]:.1f}\baselineskip}}")
        L.append(r"\label{kwfirst}")
        L += [t for t, _ in built]
    def rows_of(items, main_key, side_key):
        return [dict(period=as_text(e.get("period")), main=as_text(e.get(main_key)), side=as_text(e.get(side_key)),
                     desc=as_list(e.get("description"))) for e in as_dicts(items)]

    sections = [(lab["work"], rows_of(cv.get("experience"), "employer", "role")),
                (lab["education"], rows_of(cv.get("education"), "degree", "school")),
                (lab["certs"], rows_of(cv.get("certifications"), "name", "issuer"))]
    for lst in as_dicts(cv.get("lists")):
        sections.append((as_text(lst.get("title")) or "", rows_of(lst.get("items"), "name", "issuer")))
    # one grid (period, middle, right) for every list in Generelt, from the natural widths of all rows together
    every = [r for _, rows in sections for r in rows if r["period"] or r["main"] or r["side"] or r["desc"]]
    pw = period_width(every)
    grid = (pw,) + column_widths(every, pw)
    general = [list_block(title, rows, grid) for title, rows in sections]
    general = [g for g in general if g]   # (tex, need) per list; empty lists return ""
    if general:
        # the section title keeps company with the whole first list when that list is short
        # (the title with its bar is ~6 lines tall; with less margin the list's own needspace fails right
        # after the title and the title is left alone at the foot of the page)
        first_need = 8.0 + general[0][1] if general[0][1] > 6.0 else 13.8
        L.append(rf"\ifnum\kwgenbreak=1 \clearpage\fi\kwsection{{{esc(lab['general'], hints=False)}}}{{{first_need:.1f}\baselineskip}}")
        if not projects:
            L.append(r"\label{kwfirst}")
        L += [t for t, _ in general]
    L.append(r"\par\end{document}")
    return "\n".join(L)


# ------------------------------------------------------------------ build with auto-fit
def run_tex(work: Path) -> tuple[bool, str]:
    log = ""
    for run in range(3):
        r = subprocess.run(["lualatex", "-interaction=nonstopmode", "-halt-on-error", "cv.tex"], cwd=work,
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        lf = work / "cv.log"
        log = lf.read_text(encoding="utf-8", errors="replace") if lf.exists() else r.stdout
        if r.returncode != 0:
            return False, log
        if run >= 1 and "Rerun to get" not in log:
            break
    font_guard.check(work)
    return True, log


def page_fills(pdf: Path) -> list[float]:
    """Fill (0..1) of each page's body area (22..267 mm)."""
    doc = pymupdf.open(str(pdf))
    top, bottom = 22 * 72 / 25.4, 267 * 72 / 25.4
    fills = []
    for page in doc:
        ys = [b[3] for b in page.get_text("blocks") if b[3] < bottom and b[1] > top - 2]
        ys += [d["rect"].y1 for d in page.get_drawings() if d["rect"].y1 < bottom and d["rect"].y0 > top - 2]
        fills.append(max(0.0, (max(ys) - top) / (bottom - top)) if ys else 0.0)
    return fills


def front_quality(pdf: Path, cv: dict, lab: dict) -> int:
    """Front page quality: 2 = skills on page 1 in the two-column layout (or no skills), 1 = stacked on page 1,
    0 = skills not (completely) on page 1. Autofit never trades a worse front page for fewer pages."""
    groups = [g for g in as_dicts(cv.get("skills")) if as_list(g.get("items"))]
    if not groups:
        return 2
    doc = pymupdf.open(str(pdf))
    mm = 72 / 25.4
    hits = doc[0].search_for(lab["skills"])
    if not hits:
        return 0
    two_col = hits[0].x0 > 100 * mm
    first_item = as_text(as_list(groups[0]["items"])[0])
    last_item = as_text(as_list(groups[-1]["items"])[-1])
    if two_col:
        return 2 if (not last_item or doc[0].search_for(last_item[:40])) else 0
    # stacked: groups may continue on page 2 (never inside a group), as long as the first group is on page 1
    return 1 if (not first_item or doc[0].search_for(first_item[:40])) else 0


def main() -> None:
    global FONTS
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source")
    ap.add_argument("pdf")
    ap.add_argument("--keep", default=None, help="folder to copy cv.tex and cv.log into")
    a = ap.parse_args()
    src, out = Path(a.source).resolve(), Path(a.pdf).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    cv = load_cv(src)
    lang = "en" if as_text(cv.get("language")).lower() in ("en", "eng", "english", "engelsk") else "nb"
    lab = LABELS[lang]
    with work_dir("kwcv_") as tmp:
        work = Path(tmp)
        (work / "img").mkdir()
        (work / "fonts").mkdir()
        with zipfile.ZipFile(FONT_ZIP) as z:
            for n in z.namelist():
                if n.lower().endswith(".otf") and "__MACOSX" not in n:
                    (work / "fonts" / Path(n).name).write_bytes(z.read(n))
        FONTS = Fonts(work / "fonts")
        for stem in ["kw-symbol-svart-med-gronn-strek", "kw-navnetrekk-svart"]:
            (work / "img" / f"{stem}.pdf").write_bytes(svg_to_pdf_bytes(ASSETS / f"{stem}.svg"))
        shutil.copyfile(STYLE, work / "cv-style.tex")
        write_kernfix(work)
        font_guard.write_hook(work)
        (work / "cv.tex").write_text(build_tex(cv, src.parent, work, lab), encoding="utf-8", newline="\n")
        name_tex = esc(cv.get("name") or "Navn", hints=False)
        best, best_good = None, False
        # variants: (density, forced break before Generelt, minimum space left on page 1 for Erfaring to start there)
        variants = ((1, 0, 70), (2, 0, 70), (1, 0, 45), (2, 0, 45), (1, 1, 70), (2, 1, 70))
        for density, gb, erfmin in variants:
            meta = [f"\\def\\kwfontdir{{{(work / 'fonts').as_posix()}/}}",
                    f"\\def\\kwimgdir{{img}}", f"\\def\\kwcvname{{{name_tex}}}",
                    f"\\def\\kwdensity{{{density}}}", f"\\def\\kwgenbreak{{{gb}}}",
                    f"\\def\\kwerfmin{{{erfmin}mm}}", f"\\def\\kwisen{{{1 if lang == 'en' else 0}}}"]
            (work / "meta.tex").write_text(chr(10).join(meta) + chr(10), encoding="utf-8")
            (work / "cv.aux").unlink(missing_ok=True)
            ok, log = run_tex(work)
            if not ok:
                shutil.copyfile(work / "cv.tex", out.with_suffix(".failed.tex"))
                sys.stderr.write(chr(10).join(l for l in log.splitlines() if l.startswith(("!", "l.")))[-2500:])
                raise SystemExit("lualatex failed")
            fills = page_fills(work / "cv.pdf")
            pages, fill = len(fills), fills[-1]
            # pages after the first (the front page) should be at least 40 % full; the last page may go down to 30 %
            mid = min(fills[1:-1]) if pages > 2 else 1.0
            minfill = min(mid, fill) if pages > 1 else 1.0
            good = pages == 1 or (mid >= 0.40 and fill >= 0.30)
            front = front_quality(work / "cv.pdf", cv, lab)
            print(f"density {density}, generelt-break {gb}, erfaring-min {erfmin}: {pages} pages, last page {fill:.0%}, "
                  f"emptiest middle page {mid:.0%}, front page {front}" + (" -> ok" if good else ""))
            cand = (pages, density, log, (work / "cv.pdf").read_bytes(), fill, minfill, front)
            if best is None or (front, good, -pages, minfill) > (best[6], best_good, -best[0], best[5]):
                best, best_good = cand, good
            if front == 2 and good and (fill >= 0.70 or density == 2):   # also try the denser variant before settling
                break
        pages, density, log, data, fill, minfill, front = best
        out.write_bytes(data)
        for m in re.findall(r"Missing character:[^\n]*", log):
            WARNINGS.append(m)
        big = [float(x) for x in re.findall(r"Overfull \\[hv]box \(([\d.]+)pt too (?:wide|high)\)", log) if float(x) > 3]
        if big:
            WARNINGS.append(f"{len(big)} overfull boxes > 3pt (max {max(big)}pt)")
        if a.keep:
            Path(a.keep).mkdir(parents=True, exist_ok=True)
            shutil.copytree(work, Path(a.keep), dirs_exist_ok=True)   # whole build folder, for debugging
    print(f"built {out} ({pages} pages, density {density}, last page {fill:.0%})")
    for w in sorted(set(WARNINGS)):
        print("WARNING:", w)


if __name__ == "__main__":
    main()
