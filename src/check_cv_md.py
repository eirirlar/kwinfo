"""Check that KodeWorks CV files in Markdown follow the shared conventions.

Usage (from the project root):
    uv run python src/check_cv_md.py <cv.md> [<cv.md> ...]

Prints one line per deviation ("<file>: <message>") and exits with 1 if any file deviates.
The format itself is defined by src/cv_markdown.py; this script checks the conventions on top of it,
so that all CVs look alike and can be maintained the same way:

- section order: Om <first name>, Teknisk kompetanse, Erfaring, Arbeidserfaring, Utdanning,
  Sertifiseringer, then extra lists with fixed titles (Verv og engasjement, Foredrag og publikasjoner,
  Kurs, Utmerkelser);
- contact list with known labels in a fixed order; phone, experience and languages in a fixed form;
- projects newest first, metadata in the order Kunde, Prosjekt, Periode, Logo, Prosjekt not equal to Kunde;
- periods as MM.ÅÅÅÅ – MM.ÅÅÅÅ, MM.ÅÅÅÅ – nå or ÅÅÅÅ – ÅÅÅÅ (optional addition in parentheses);
- skill group names not in capitals, no duplicate items in a group;
- bullets as Markdown lists, not as "\\-" or "•" text;
- images/foto.<ext> and images/logo-<customer>.<ext> exist where referenced;
- for the employees' CVs in cvs/<name>/: logos come from the shared library ../logos/<customer>.<ext>,
  the photo is a JPG without metadata whose largest crop in the frame ratio is at most
  PHOTO_MAX_CROP_W pixels wide, and raster logos are at most LOGO_MAX_PX (see src/normalize_cv_images.py);
- parse -> render -> parse round-trips.
"""
from __future__ import annotations

import re
import struct
import sys
from pathlib import Path

import cv_markdown as cm

SECTION_ORDER_NB = ["om", "teknisk kompetanse", "erfaring", "arbeidserfaring", "utdanning", "sertifiseringer"]
SECTION_ORDER_EN = ["about", "skills", "experience", "work experience", "education", "certifications"]
LIST_TITLES_NB = ["Verv og engasjement", "Foredrag og publikasjoner", "Kurs", "Utmerkelser"]
LIST_TITLES_EN = ["Positions of trust", "Talks and publications", "Courses", "Awards"]
CONTACT_ORDER_NB = ["Telefon", "E-post", "Erfaring", "Språk", "Foto", "Fotofokus"]
CONTACT_ORDER_EN = ["Phone", "Email", "Experience", "Languages", "Photo", "Photo focus"]
PROJECT_META_NB = ["Kunde", "Prosjekt", "Periode", "Logo"]
PROJECT_META_EN = ["Customer", "Project", "Period", "Logo"]

DATE = r"(?:\d{2}\.\d{4}|\d{4})"
PERIOD = re.compile(rf"^{DATE}(?: – (?:{DATE}|nå|now))?(?: \([^()]+\))?$")
PHONE_NO = re.compile(r"^\+47 \d{3} \d{2} \d{3}$")
YEARS = re.compile(r"^\d+\+?$")
BAD_BULLET = re.compile(r"^\s*(\\-|•|·|–\s)", re.M)
IMAGE_FOTO = re.compile(r"^images/foto\.(jpe?g|png)$")
IMAGE_LOGO = re.compile(r"^images/logo-[a-z0-9]+(?:-[a-z0-9]+)*\.(png|svg|jpe?g)$")
LIBRARY_LOGO = re.compile(r"^\.\./logos/[a-z0-9]+(?:-[a-z0-9]+)*\.(png|svg|jpe?g)$")
# Image format for the employees' CVs (cvs/<name>/), kept in step with src/normalize_cv_images.py.
PHOTO_RATIO = 60.0 / 74.0          # width / height of the photo frame in the CV (PHOTO_W, PHOTO_H in build_cv_pdf.py)
PHOTO_MAX_CROP_W = 1200            # pixels across the largest crop in the frame ratio
LOGO_MAX_PX = (700, 260)           # largest raster logo, width x height


def image_info(path: Path) -> tuple[str, int, int, bool] | None:
    """(format, width, height, has metadata) for a PNG or JPEG, read from the file header; None otherwise.

    Metadata means EXIF or an embedded ICC profile (JPEG APP1 Exif / APP2 ICC_PROFILE, PNG eXIf / iCCP)."""
    data = path.read_bytes()
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        w, h = struct.unpack(">II", data[16:24])
        return "png", w, h, b"eXIf" in data or b"iCCP" in data
    if data[:2] != b"\xff\xd8":
        return None
    i, size, meta = 2, None, False
    while i + 4 <= len(data) and data[i] == 0xFF:
        marker = data[i + 1]
        if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
            i += 2
            continue
        length = struct.unpack(">H", data[i + 2:i + 4])[0]
        seg = data[i + 4:i + 2 + length]
        if marker == 0xE1 and seg.startswith(b"Exif"):
            meta = True
        if marker == 0xE2 and seg.startswith(b"ICC_PROFILE"):
            meta = True
        if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC) and size is None:
            h, w = struct.unpack(">HH", seg[1:5])
            size = (w, h)
        if marker == 0xDA:   # start of scan: no more headers
            break
        i += 2 + length
    return ("jpeg", size[0], size[1], meta) if size else None


def _start_key(period: str) -> tuple[int, int] | None:
    m = re.match(r"^(?:(\d{2})\.)?(\d{4})", period or "")
    return (int(m.group(2)), int(m.group(1) or 0)) if m else None


def _headings(text: str, level: int) -> list[str]:
    out = []
    for line in cm._strip_comments(text).splitlines():
        m = cm.HEADING.match(line)
        if m and len(m.group(1)) == level:
            out.append(cm._clean(m.group(2)))
    return out


def _list_labels(lines: list[str]) -> list[str]:
    """Labels of the first bullet list in the given lines ('- Label: value')."""
    labels = []
    for b in cm._blocks(lines):
        if b["type"] == "list":
            for it in b["items"]:
                m = cm.LABEL.match(it["text"])
                labels.append(m.group(1).strip("* ") if m else "")
            break
    return labels


def check_text(text: str, base: Path | None = None) -> list[str]:
    """Deviations for one CV given as text; base is the folder image paths are relative to."""
    issues: list[str] = []
    try:
        cv = cm.parse_text(text)
    except Exception as e:  # noqa: BLE001 - report any parse failure as a deviation
        return [f"cannot be read: {e}"]
    en = cv.get("language") == "en"
    order = SECTION_ORDER_EN if en else SECTION_ORDER_NB
    list_titles = LIST_TITLES_EN if en else LIST_TITLES_NB

    if not cv.get("name"):
        issues.append("missing name (# Name)")
    first = (cv.get("name") or "").split()[0] if cv.get("name") else ""

    # sections and their order
    name, head, sections = cm._sections(text)
    pos = -1
    for title, _ in sections:
        low = title.lower()
        key = "om" if (low.startswith("om ") or low == "om") else ("about" if low.startswith("about") else low)
        if key in order:
            i = order.index(key)
            if i < pos:
                issues.append(f"section «{title}» is out of order")
            pos = max(pos, i)
            if key in ("om", "about") and first and title not in (f"Om {first}", f"About {first}"):
                issues.append(f"«{title}» should be «{'About' if en else 'Om'} {first}»")
        elif title in list_titles:
            pos = len(order)
        else:
            issues.append(f"unknown section «{title}» (extra lists: {', '.join(list_titles)})")

    # contact list
    contact_order = CONTACT_ORDER_EN if en else CONTACT_ORDER_NB
    labels = _list_labels(head)
    idx = [contact_order.index(l) if l in contact_order else -1 for l in labels]
    for l, i in zip(labels, idx):
        if i < 0:
            issues.append(f"unknown label in the contact list: «{l}»")
    known = [i for i in idx if i >= 0]
    if known != sorted(known):
        issues.append(f"the contact list should have the order {', '.join(contact_order)}")
    phone = cv.get("phone")
    if phone and phone.startswith("+47") and not PHONE_NO.match(phone):
        issues.append(f"phone should be written «+47 000 00 000»: «{phone}»")
    if phone and not phone.startswith("+"):
        issues.append(f"phone has no country code: «{phone}»")
    if cv.get("experience_years") and not YEARS.match(str(cv["experience_years"])):
        issues.append(f"Erfaring should be «N år»: «{cv['experience_years']}»")
    for lang in cv.get("languages") or []:
        if lang != lang.lower():
            issues.append(f"languages are written in lower case: «{lang}»")

    # images; the employees' CVs (cvs/<name>/) also follow the image format and the shared logo library
    employee = base is not None and base.parent.name == "cvs"

    def image(path: str | None, pattern: re.Pattern, what: str) -> None:
        if not path:
            return
        if pattern is IMAGE_LOGO and employee:
            if not LIBRARY_LOGO.match(path):
                issues.append(f"{what} should come from the shared library: ../logos/<customer>.png (or .svg/.jpg): «{path}»")
        elif not pattern.match(path):
            want = "images/foto.jpg (or .png)" if pattern is IMAGE_FOTO else "images/logo-<customer>.png (or .svg/.jpg)"
            issues.append(f"{what} should be {want}: «{path}»")
        if base is not None and not (base / path).exists():
            issues.append(f"{what} does not exist: «{path}»")
            return
        if not employee or base is None:
            return
        info = image_info(base / path)
        if info is None:
            if not path.endswith(".svg"):
                issues.append(f"{what} is not a readable PNG or JPEG: «{path}»")
            return
        fmt, w, h, meta = info
        if pattern is IMAGE_FOTO:
            crop_w = min(w, h * PHOTO_RATIO)
            if fmt != "jpeg":
                issues.append(f"photo should be a JPG (images/foto.jpg), not {fmt.upper()}: run src/normalize_cv_images.py")
            if crop_w > PHOTO_MAX_CROP_W + 1:
                issues.append(f"photo is larger than needed ({w} × {h} px; the crop may be at most "
                              f"{PHOTO_MAX_CROP_W} px wide): run src/normalize_cv_images.py")
            if meta:
                issues.append("photo contains metadata (EXIF or ICC profile): run src/normalize_cv_images.py")
        elif w > LOGO_MAX_PX[0] or h > LOGO_MAX_PX[1]:
            issues.append(f"{what} is larger than needed ({w} × {h} px, at most {LOGO_MAX_PX[0]} × {LOGO_MAX_PX[1]}): "
                          "run src/normalize_cv_images.py")
    image(cv.get("photo"), IMAGE_FOTO, "photo")

    # skills
    for g in cv.get("skills") or []:
        group = g.get("group", "")
        if group and group == group.upper() and any(c.isalpha() for c in group):
            issues.append(f"skill group «{group}» should be in sentence case")
        items = [i.lower() for i in g.get("items") or []]
        dups = sorted({i for i in items if items.count(i) > 1})
        if dups:
            issues.append(f"duplicates in «{group or 'skills'}»: {', '.join(dups)}")

    # projects
    meta_order = PROJECT_META_EN if en else PROJECT_META_NB
    proj_sections = [l for t, l in sections if t.lower() in ("erfaring", "experience", "prosjekter", "projects")]
    raw_projects = cm._subsections(proj_sections[0])[1] if proj_sections else []
    starts = []
    for (heading, lines), p in zip(raw_projects, cv.get("projects") or []):
        label = heading or "(no heading)"
        mlabels = _list_labels(lines)
        midx = [meta_order.index(l) for l in mlabels if l in meta_order]
        if midx != sorted(midx):
            issues.append(f"project «{label}»: the fields should be in the order {', '.join(meta_order)}")
        if not p.get("role"):
            issues.append(f"project «{label}»: the heading should be the role")
        if p.get("project") and p.get("customer") and p["project"].lower() == p["customer"].lower():
            issues.append(f"project «{label}»: Prosjekt equals Kunde and should be left out")
        if not p.get("period"):
            issues.append(f"project «{label}»: missing period")
        elif not PERIOD.match(p["period"]):
            issues.append(f"project «{label}»: period in the wrong form «{p['period']}»")
        image(p.get("logo"), IMAGE_LOGO, f"logo in «{label}»")
        starts.append((label, _start_key(p.get("period", ""))))
    keyed = [(l, k) for l, k in starts if k]
    for (l1, k1), (l2, k2) in zip(keyed, keyed[1:]):
        if k2 > k1:
            issues.append(f"the projects are not newest first («{l2}» after «{l1}»)")
            break

    # general lists
    rows = [("Arbeidserfaring", r) for r in cv.get("experience") or []] + \
           [("Utdanning", r) for r in cv.get("education") or []] + \
           [("Sertifiseringer", r) for r in cv.get("certifications") or []] + \
           [(lst.get("title", ""), r) for lst in cv.get("lists") or [] for r in lst.get("items") or []]
    for title, r in rows:
        if r.get("period") and not PERIOD.match(r["period"]):
            issues.append(f"{title}: period in the wrong form «{r['period']}»")
        if not (r.get("employer") or r.get("degree") or r.get("name")):
            issues.append(f"{title}: row without a name ({r})")

    # raw text
    for m in BAD_BULLET.finditer(cm._strip_comments(text)):
        line = text[m.start():text.find("\n", m.start())].strip()
        issues.append(f"bullet written as text, not as a Markdown list: «{line[:50]}»")
        break
    if "\t" in text:
        issues.append("contains a tab character")

    # round trip
    if cm.parse_text(cm.render(cv)) != cv:
        issues.append("round trip parse → render → parse does not give the same data")
    return issues


def check_file(path: Path) -> list[str]:
    return check_text(path.read_text(encoding="utf-8"), base=path.parent)


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    bad = 0
    for a in argv:
        p = Path(a)
        issues = check_file(p)
        for i in issues:
            print(f"{p}: {i}")
        bad += bool(issues)
    print(f"{len(argv)} files, {bad} with deviations")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
