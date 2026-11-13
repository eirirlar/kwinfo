# /// script
# requires-python = ">=3.10"
# dependencies = ["pymupdf", "pyyaml"]
# ///
"""Build KodeWorks business cards from the CVs in Markdown.

Usage (from the project root):
    uv run src/build_cv_business_cards.py                         # every CV in cvs/*/<name>.md
    uv run src/build_cv_business_cards.py cvs/paal-noedseth/paal-noedseth.md [...]
    uv run src/build_cv_business_cards.py --out <folder> [--dry-run] [cv.md ...]

For each CV the contact fields are read with src/cv_markdown.py (name, title, phone, email; the web
address is always kodeworks.no), written as a card file in the format of src/build_business_card.py, and
built with that script, so the card layout and its print checks live in one place only.

Output, next to the CV unless --out is given: visittkort-<folder name>.pdf (print, CMYK, bleed and crop
marks) and visittkort-<folder name>.png (screen). The intermediate card file is not kept. A CV without a
name is skipped; a card that fails the print checks (e.g. a title too long for the safe zone) is reported
and the run ends with exit code 1.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

import cv_markdown  # noqa: E402
from project_tmp import work_dir  # work folders in <project root>/tmp/ (CLAUDE.md)

WEB = "kodeworks.no"
DEFAULT_GLOB = "cvs/*/*.md"


def card_fields(cv: dict) -> dict[str, str]:
    """The business card fields for one CV (empty fields left out)."""
    fields = {"name": cv.get("name"), "title": cv.get("title"), "phone": cv.get("phone"),
              "email": cv.get("email"), "web": WEB}
    return {k: str(v).strip() for k, v in fields.items() if v and str(v).strip()}


def card_markdown(fields: dict[str, str]) -> str:
    """The card file: a YAML header only, values quoted so ':' and '#' in a title are safe."""
    def quoted(v: str) -> str:
        if '"' not in v:
            return '"' + v.replace("\\", "\\\\") + '"'
        return "'" + v.replace("'", "''") + "'"   # YAML single quotes: only ' needs escaping (as '')
    lines = ["---"] + [f"{k}: {quoted(v)}" for k, v in fields.items()]
    return "\n".join(lines + ["---", ""])


def cv_files(args: list[str]) -> list[Path]:
    if args:
        return [Path(a).resolve() for a in args]
    # the CV is the Markdown file named like its folder (cvs/<name>/<name>.md)
    return sorted(p for p in ROOT.glob(DEFAULT_GLOB) if p.stem == p.parent.name)


def main() -> int:
    for s in (sys.stdout, sys.stderr):
        s.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="Build business cards from the CVs in Markdown")
    ap.add_argument("cvs", nargs="*", help=f"CV files in Markdown (default: {DEFAULT_GLOB})")
    ap.add_argument("--out", help="folder for the cards (default: next to each CV)")
    ap.add_argument("--dry-run", action="store_true", help="only show which cards would be built, with their fields")
    args = ap.parse_args()

    files = cv_files(args.cvs)
    if not files:
        print(f"No CV files found ({DEFAULT_GLOB}).")
        return 1
    failed, built = [], 0
    for cv_path in files:
        if not cv_path.is_file():
            print(f"SKIP {cv_path}: file not found")
            failed.append(cv_path.name)
            continue
        fields = card_fields(cv_markdown.parse(cv_path))
        if "name" not in fields:
            print(f"SKIP {cv_path}: the CV has no name (# Name)")
            failed.append(cv_path.name)
            continue
        out_dir = Path(args.out).resolve() if args.out else cv_path.parent
        stem = f"visittkort-{cv_path.parent.name if cv_path.stem == cv_path.parent.name else cv_path.stem}"
        pdf, png = out_dir / f"{stem}.pdf", out_dir / f"{stem}.png"
        missing = [k for k in ("title", "phone", "email") if k not in fields]
        note = f"  (no {', '.join(missing)} in the CV)" if missing else ""
        if args.dry_run:
            print(f"would build {pdf}: " + " | ".join(fields.values()) + note)
            continue
        out_dir.mkdir(parents=True, exist_ok=True)
        with work_dir("kwcards_") as tmp:
            card = Path(tmp) / f"{stem}.md"
            card.write_text(card_markdown(fields), encoding="utf-8", newline="\n")
            res = subprocess.run([sys.executable, str(HERE / "build_business_card.py"), str(card),
                                  "-o", str(pdf), "--png", str(png)],
                                 capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=110)
        if res.returncode != 0:
            print(f"FAIL {cv_path.parent.name}:{note}")
            for line in (res.stdout + res.stderr).splitlines():
                if line.strip() and not line.startswith(("Built", "      ")):
                    print("     " + line.strip())
            failed.append(cv_path.name)
        else:
            print(f"OK   {pdf}{note}")
            built += 1
    if not args.dry_run:
        print(f"\n{built} card(s) built, {len(failed)} failed or skipped.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
