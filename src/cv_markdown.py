"""KodeWorks CV in Markdown <-> the CV data model used by src/build_cv_pdf.py.

The CV source is a plain Markdown file that reads well as text, in VS Code preview and on GitHub:

    # Pål Nødseth

    Senior fullstack-utvikler

    - Telefon: +47 930 85 452
    - E-post: paal@kodeworks.no
    - Erfaring: 9 år
    - Språk: norsk, engelsk
    - Foto: images/paal.jpg

    ## Om Pål
    Paragraphs (and bullet lists).

    ## Teknisk kompetanse
    ### Språk og rammeverk
    - TypeScript
    - React

    ## Erfaring
    ### Senior frontend-utvikler            <- role (one ### per project, newest first)
    - Kunde: Equinor
    - Prosjekt: Echo 3D
    - Periode: 03.2022 – nå
    - Logo: logoer/equinor.svg

    Description paragraphs, bullet lists, **bold**, and a paragraph that is only **bold** (a subheading).

    Nøkkelord: React, TypeScript, Three.js

    ## Arbeidserfaring
    - 03.2022 – nå | KodeWorks | Senior utvikler
      - optional bullets under a row become its description

    ## Utdanning
    - 2015 – 2016 | Business Economics, M.Sc. | Handelshøyskolen BI

    ## Sertifiseringer
    - 2021 | Azure Fundamentals (AZ-900) | Microsoft

    ## Verv og engasjement                   <- any other heading after the projects: an extra list
    - 2019 – 2021 | Styremedlem | TIHLDE

English labels and headings work too (Phone, Email, Experience, Languages, Photo; About, Skills,
Experience/Projects, Customer, Project, Period, Keywords, Work experience, Education, Certifications).
A CV with an English «Experience»/«Projects» section is set in English unless «Dokumentspråk» says
otherwise. HTML comments (<!-- -->) are ignored, so templates can carry guidance.

parse(path) -> dict and render(dict) -> str; render(parse(x)) round-trips the data model.
"""
from __future__ import annotations

import re
from pathlib import Path

# ------------------------------------------------------------------ vocabulary
HEADER_LABELS = {
    "telefon": "phone", "phone": "phone", "tlf": "phone", "mobil": "phone",
    "e-post": "email", "epost": "email", "email": "email", "e-mail": "email",
    "erfaring": "experience_years", "experience": "experience_years",
    "språk": "languages", "languages": "languages",
    "foto": "photo", "bilde": "photo", "photo": "photo",
    "fotofokus": "photo_focus", "photo focus": "photo_focus",
    "dokumentspråk": "language", "document language": "language",
}
PROJECT_LABELS = {
    "kunde": "customer", "customer": "customer", "client": "customer",
    "prosjekt": "project", "project": "project",
    "periode": "period", "period": "period",
    "logo": "logo",
}
KEYWORD_LABELS = ("nøkkelord", "keywords")
SECTION_KINDS = {
    "teknisk kompetanse": "skills", "kompetanse": "skills", "skills": "skills",
    "technical skills": "skills",
    "erfaring": "projects", "prosjekter": "projects", "prosjekterfaring": "projects",
    "experience": "projects", "projects": "projects", "project experience": "projects",
    "arbeidserfaring": "experience", "work experience": "experience", "employment": "experience",
    "utdanning": "education", "education": "education",
    "sertifiseringer": "certifications", "certifications": "certifications",
}
ENGLISH_PROJECT_HEADINGS = {"experience", "projects", "project experience"}
ROW_KEYS = {"experience": ("period", "employer", "role"),
            "education": ("period", "degree", "school"),
            "certifications": ("period", "name", "issuer"),
            "lists": ("period", "name", "issuer")}

LABELS_OUT = {
    "nb": {"phone": "Telefon", "email": "E-post", "experience_years": "Erfaring", "languages": "Språk",
           "photo": "Foto", "photo_focus": "Fotofokus", "language": "Dokumentspråk",
           "customer": "Kunde", "project": "Prosjekt", "period": "Periode", "logo": "Logo",
           "keywords": "Nøkkelord", "about": "Om", "skills": "Teknisk kompetanse", "projects": "Erfaring",
           "experience": "Arbeidserfaring", "education": "Utdanning", "certifications": "Sertifiseringer",
           "years": "år"},
    "en": {"phone": "Phone", "email": "Email", "experience_years": "Experience", "languages": "Languages",
           "photo": "Photo", "photo_focus": "Photo focus", "language": "Document language",
           "customer": "Customer", "project": "Project", "period": "Period", "logo": "Logo",
           "keywords": "Keywords", "about": "About", "skills": "Skills", "projects": "Experience",
           "experience": "Work experience", "education": "Education", "certifications": "Certifications",
           "years": "years"},
}

BULLET = re.compile(r"^(\s*)[-*+]\s+(.*)$")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
LABEL = re.compile(r"^([^:]{1,30}?)\s*:\s*(.*)$")


# ------------------------------------------------------------------ text helpers
def _strip_comments(text: str) -> str:
    return re.sub(r"<!--.*?-->", "", text, flags=re.S)


def _clean(s: str) -> str:
    """One logical line: hard-break markers removed, Markdown escapes we write undone."""
    s = re.sub(r"\\$", "", s.rstrip())
    s = s.replace(r"\|", "|")
    s = re.sub(r"^\\([#\-*+>])", r"\1", s)
    return s.strip()


def _unbold(s: str) -> str:
    m = re.fullmatch(r"\*\*(.+?)\*\*:?", s.strip())
    return m.group(1) if m else s


def _split_items(s: str) -> list[str]:
    """Split 'a, b (x, y), c' at commas or middle dots that are not inside brackets."""
    items, buf, depth = [], "", 0
    for ch in s:
        depth += ch in "([{"
        depth -= ch in ")]}" and depth > 0
        if ch in ",·" and depth == 0:
            items.append(buf)
            buf = ""
        else:
            buf += ch
    items.append(buf)
    return [x.strip() for x in items if x.strip()]


def _blocks(lines: list[str]) -> list[dict]:
    """Group the lines of one section into paragraphs and bullet lists (with nesting)."""
    blocks: list[dict] = []
    para: list[str] = []

    def flush_para() -> None:
        if para:
            blocks.append({"type": "para", "text": " ".join(_clean(x) for x in para if _clean(x))})
            para.clear()

    for raw in lines:
        if not raw.strip():
            flush_para()
            if blocks and blocks[-1]["type"] == "list":
                blocks[-1]["closed"] = True
            continue
        m = BULLET.match(raw)
        if m:
            flush_para()
            indent = len(m.group(1).expandtabs(4))
            item = {"text": _clean(m.group(2)), "children": []}
            last = blocks[-1] if blocks else None
            if last and last["type"] == "list" and (not last.get("closed") or indent >= 2):
                last.pop("closed", None)
                if indent >= 2 and last["items"]:
                    last["items"][-1]["children"].append("- " + item["text"])
                else:
                    last["items"].append(item)
            else:
                blocks.append({"type": "list", "items": [item]})
            continue
        last = blocks[-1] if blocks else None
        if last and last["type"] == "list" and raw[:1].isspace():
            target = last["items"][-1]
            if last.get("closed"):          # indented paragraph after a blank line: belongs to the item
                last.pop("closed")
                target["children"].append(_clean(raw))
            elif target["children"]:
                target["children"][-1] += " " + _clean(raw)
            else:
                target["text"] += " " + _clean(raw)
            continue
        para.append(raw)
    flush_para()
    for b in blocks:
        b.pop("closed", None)
    return [b for b in blocks if b["type"] == "list" or b["text"]]


def _sections(text: str) -> tuple[str | None, list[str], list[tuple[str, list[str]]]]:
    """-> (name from #, lines before the first ##, [(## title, lines)])."""
    name, head, sections = None, [], []
    current: list[str] = head
    for line in _strip_comments(text).splitlines():
        m = HEADING.match(line)
        if m and len(m.group(1)) == 1 and name is None:
            name = _clean(m.group(2))
            continue
        if m and len(m.group(1)) == 2:
            sections.append((_clean(m.group(2)), []))
            current = sections[-1][1]
            continue
        current.append(line)
    return name, head, sections


def _subsections(lines: list[str]) -> tuple[list[str], list[tuple[str, list[str]]]]:
    pre, subs = [], []
    current = pre
    for line in lines:
        m = HEADING.match(line)
        if m and len(m.group(1)) == 3:
            subs.append((_clean(m.group(2)), []))
            current = subs[-1][1]
            continue
        current.append(line)
    return pre, subs


def _paragraphs(blocks: list[dict]) -> list[str]:
    """Blocks -> the model's list of paragraphs, where '- …' items are bullets."""
    out = []
    for b in blocks:
        if b["type"] == "para":
            out.append(b["text"])
        else:
            for it in b["items"]:
                out.append("- " + it["text"])
                out.extend(c if c.startswith("- ") else "- " + c for c in it["children"])
    return out


def _labelled(item_text: str, labels: dict) -> tuple[str, str] | None:
    """'Label: value' (label optionally **bold**, as in '**Telefon:** …') -> (model key, value)."""
    m = LABEL.match(item_text.replace("**", "", 2) if item_text.startswith("**") else item_text)
    if not m:
        return None
    key = labels.get(m.group(1).strip("* ").lower())
    return (key, m.group(2).strip().lstrip("* ").strip()) if key else None


def _row(text: str, keys: tuple[str, str, str]) -> dict:
    parts = [p.strip() for p in re.split(r"(?<!\\)\|", text)]
    parts = [p.replace(r"\|", "|") for p in parts]
    if len(parts) == 1:
        parts = ["", parts[0], ""]
    elif len(parts) == 2:
        parts = [parts[0], parts[1], ""]
    elif len(parts) > 3:
        parts = [parts[0], parts[1], " | ".join(parts[2:])]
    return {k: v for k, v in zip(keys, parts) if v}


# ------------------------------------------------------------------ parse
def parse_text(text: str) -> dict:
    name, head, sections = _sections(text)
    cv: dict = {}
    if name:
        cv["name"] = name
    for b in _blocks(head):
        if b["type"] == "para" and "title" not in cv and not _labelled(b["text"], HEADER_LABELS):
            cv["title"] = b["text"]
            continue
        items = b["items"] if b["type"] == "list" else [{"text": b["text"], "children": []}]
        for it in items:
            kv = _labelled(it["text"], HEADER_LABELS)
            if not kv:
                continue
            key, val = kv
            if key == "experience_years":
                val = re.sub(r"\s*(år|years?)\.?$", "", val, flags=re.I)
            if key == "languages":
                val = _split_items(val)
            if key == "photo_focus":
                val = [float(x) for x in re.split(r"[,\s]+", val) if x]
            if val in ("", [], "null"):
                continue
            cv[key] = val

    english_projects = False
    seen_projects = False
    for title, lines in sections:
        low = title.lower().rstrip(":")
        kind = SECTION_KINDS.get(low)
        if kind is None and (low.startswith("om ") or low == "om" or low.startswith("about")):
            kind = "about"
        if kind is None and not seen_projects and low in ("annet", "other"):
            kind = "lists"
        if kind is None:
            kind = "lists"
        if kind == "about":
            cv["about"] = _paragraphs(_blocks(lines))
        elif kind == "skills":
            pre, subs = _subsections(lines)
            groups = []
            for gtitle, glines in (subs or [("", pre)]):
                items: list[str] = []
                for b in _blocks(glines):
                    if b["type"] == "list":
                        items += [it["text"] for it in b["items"]]
                    else:
                        items += _split_items(b["text"])
                group = {"group": gtitle, "items": items} if gtitle else {"items": items}
                groups.append(group)
            cv["skills"] = groups
        elif kind == "projects":
            seen_projects = True
            english_projects = english_projects or low in ENGLISH_PROJECT_HEADINGS
            cv["projects"] = [_parse_project(t, l) for t, l in _subsections(lines)[1]]
        elif kind in ("experience", "education", "certifications"):
            cv[kind] = _parse_rows(lines, ROW_KEYS[kind])
        else:
            cv.setdefault("lists", []).append({"title": title, "items": _parse_rows(lines, ROW_KEYS["lists"])})
    if "language" not in cv and english_projects:
        cv["language"] = "en"
    if cv.get("language") in ("nb", "no", "norsk", "bokmål"):
        cv["language"] = "nb"
    elif cv.get("language") in ("en", "engelsk", "english"):
        cv["language"] = "en"
    return cv


def _parse_project(heading: str, lines: list[str]) -> dict:
    p: dict = {}
    blocks = _blocks(lines)
    if blocks and blocks[0]["type"] == "list" and all(_labelled(it["text"], PROJECT_LABELS)
                                                      for it in blocks[0]["items"]):
        for it in blocks.pop(0)["items"]:
            key, val = _labelled(it["text"], PROJECT_LABELS)
            if val and val != "null":
                p[key] = val
    if heading and heading != p.get("project") or "project" not in p:
        p = {"role": heading, **p} if heading else p
    keywords = None
    if blocks and blocks[-1]["type"] == "para":
        m = LABEL.match(blocks[-1]["text"])
        if m and m.group(1).strip("* ").lower() in KEYWORD_LABELS:
            keywords = _split_items(m.group(2))
            blocks.pop()
    desc = _paragraphs(blocks)
    if desc:
        p["description"] = desc
    if keywords:
        p["keywords"] = keywords
    order = ["role", "customer", "project", "period", "description", "keywords", "logo"]
    return {k: p[k] for k in order if k in p}


def _parse_rows(lines: list[str], keys: tuple[str, str, str]) -> list[dict]:
    rows = []
    for b in _blocks(lines):
        items = b["items"] if b["type"] == "list" else [{"text": b["text"], "children": []}]
        for it in items:
            row = _row(it["text"], keys)
            if it["children"]:
                row["description"] = list(it["children"])
            if row:
                rows.append(row)
    return rows


def parse(path: str | Path) -> dict:
    return parse_text(Path(path).read_text(encoding="utf-8"))


# ------------------------------------------------------------------ render
def _esc_line(s: str) -> str:
    s = str(s)
    return "\\" + s if re.match(r"^([#>+*]|-\s)", s) and not s.startswith("**") else s


def _esc_cell(s) -> str:
    return str(s).replace("|", r"\|")


def _render_paragraphs(paras: list) -> list[str]:
    out: list[str] = []
    prev_bullet = False
    for x in paras:
        x = str(x)
        bullet = x.startswith("- ")
        if out and not (bullet and prev_bullet):
            out.append("")
        out.append("- " + x[2:].strip() if bullet else _esc_line(x))
        prev_bullet = bullet
    return out


def render(cv: dict) -> str:
    lang = "en" if cv.get("language") == "en" else "nb"
    L = LABELS_OUT[lang]
    out = [f"# {cv.get('name', '')}".rstrip(), ""]
    if cv.get("title"):
        out += [_esc_line(cv["title"]), ""]
    head = []
    for key in ("phone", "email", "experience_years", "languages", "photo", "photo_focus", "language"):
        val = cv.get(key)
        if val in (None, "", []):
            continue
        if key == "experience_years":
            val = f"{val} {L['years']}"
        elif key in ("languages", "photo_focus"):
            val = ", ".join(str(v) for v in val) if isinstance(val, list) else val
        elif key == "language" and val == "en":
            continue  # implied by the English section headings
        head.append(f"- {L[key]}: {val}")
    if head:
        out += head + [""]
    if cv.get("about"):
        first = str(cv.get("name", "")).split()[0] if cv.get("name") else ""
        out += [f"## {L['about']} {first}".rstrip(), ""] + _render_paragraphs(cv["about"]) + [""]
    if cv.get("skills"):
        out += [f"## {L['skills']}", ""]
        for g in cv["skills"]:
            if g.get("group"):
                out += [f"### {g['group']}", ""]
            items = [str(i) for i in g.get("items") or []]
            if any(len(_split_items(i)) != 1 or len(i) > 40 for i in items):
                out += [f"- {_esc_cell(i)}" for i in items] + [""]   # sentences: one bullet each
            else:
                out += [_esc_line(", ".join(items)), ""]             # short items: one line
    if cv.get("projects"):
        out += [f"## {L['projects']}", ""]
        for p in cv["projects"]:
            heading = p.get("role") or p.get("project") or p.get("customer") or ""
            out += [f"### {heading}", ""]
            meta = [f"- {L[k]}: {p[k]}" for k in ("customer", "project", "period", "logo")
                    if p.get(k) not in (None, "")]
            if meta:
                out += meta + [""]
            if p.get("description"):
                out += _render_paragraphs(p["description"]) + [""]
            if p.get("keywords"):
                kws = p["keywords"]
                kws = kws if isinstance(kws, str) else ", ".join(str(k) for k in kws)
                out += [f"{L['keywords']}: {kws}", ""]
    for key in ("experience", "education", "certifications"):
        if cv.get(key):
            out += [f"## {L[key]}", ""] + _render_rows(cv[key], ROW_KEYS[key]) + [""]
    for lst in cv.get("lists") or []:
        out += [f"## {lst.get('title', '')}", ""] + _render_rows(lst.get("items") or [], ROW_KEYS["lists"]) + [""]
    while out and out[-1] == "":
        out.pop()
    return "\n".join(out) + "\n"


def _render_rows(rows: list[dict], keys: tuple[str, str, str]) -> list[str]:
    out = []
    for r in rows:
        cells = [_esc_cell(r.get(k, "") or "") for k in keys]
        while len(cells) > 2 and not cells[-1]:
            cells.pop()                       # keep two cells, so «2010 |» stays a period
        out.append(("- " + " | ".join(cells)).rstrip())
        for d in r.get("description") or []:
            d = str(d)
            if d.startswith("- "):
                out.append("  - " + d[2:].strip())
            else:
                out += ["", "  " + _esc_line(d)]   # paragraph inside the list item
    return out


if __name__ == "__main__":
    import json
    import sys
    print(json.dumps(parse(sys.argv[1]), ensure_ascii=False, indent=1))
