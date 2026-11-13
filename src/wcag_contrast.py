# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""WCAG 2.x contrast matrix.

Usage (from the project root):
    uv run src/wcag_contrast.py deliverable/visualprofile/profile/colors.json

Input JSON: a list of "#RRGGBB" strings, a list of {"name", "hex"} objects,
or {"colors": [...], "technical": [...]} with either of those ("technical" is optional). Output: Markdown with a ratio
matrix and a table of all colour pairs with pass/fail for AA normal text
(4.5:1), AA large text (3:1) and AAA (7:1).
"""
import argparse
import json
import sys

AA_NORMAL, AA_LARGE, AAA = 4.5, 3.0, 7.0


def parse_hex(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        raise ValueError(f"bad hex colour: {h!r}")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def channel(c8):
    c = c8 / 255.0
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def luminance(rgb):
    r, g, b = (channel(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(c1, c2):
    l1, l2 = luminance(c1), luminance(c2)
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def load(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, dict):
        data = data["colors"] + data.get("technical", [])
    res = []
    for item in data:
        if isinstance(item, str):
            h = item if item.startswith("#") else "#" + item
            res.append((h.upper(), h.upper()))
        else:
            h = item["hex"] if item["hex"].startswith("#") else "#" + item["hex"]
            res.append((item.get("name", h.upper()), h.upper()))
    return res


def classify(r):
    if r >= AA_NORMAL:
        return "Brødtekst"
    if r >= AA_LARGE:
        return "Kun stor tekst / ikke-tekst"
    return "Forbudt"


def mark(ok):
    return "ja" if ok else "nei"


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("colors", help="JSON file with colours")
    ap.add_argument("--no-pairs", action="store_true", help="only print the ratio matrix")
    args = ap.parse_args()
    cols = [(n, h, parse_hex(h)) for n, h in load(args.colors)]

    print("## Kontrastmatrise (forholdstall)\n")
    print("Kontrast er symmetrisk: rad og kolonne kan byttes om.\n")
    print("| | " + " | ".join(f"{n} {h}" for n, h, _ in cols) + " |")
    print("|---|" + "---:|" * len(cols))
    for n1, h1, c1 in cols:
        cells = ["-" if h1 == h2 else f"{ratio(c1, c2):.2f}" for _, h2, c2 in cols]
        print(f"| **{n1}** {h1} | " + " | ".join(cells) + " |")

    if args.no_pairs:
        return
    print("\n## Alle par, sortert etter forholdstall\n")
    print("| Farge A | Farge B | Forhold | AA normal 4.5 | AA stor 3.0 | AAA 7.0 | Klasse |")
    print("|---|---|---:|:---:|:---:|:---:|---|")
    rows = []
    for i, (n1, h1, c1) in enumerate(cols):
        for n2, h2, c2 in cols[i + 1:]:
            rows.append((ratio(c1, c2), f"{n1} {h1}", f"{n2} {h2}"))
    for r, a, b in sorted(rows, key=lambda x: -x[0]):
        print(f"| {a} | {b} | {r:.2f}:1 | {mark(r >= AA_NORMAL)} | {mark(r >= AA_LARGE)} | {mark(r >= AAA)} | {classify(r)} |")


if __name__ == "__main__":
    sys.exit(main())
