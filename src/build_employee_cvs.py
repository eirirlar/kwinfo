"""Build the employees' CV PDFs and business cards from the CVs in Markdown in cvs/<name>/<name>.md.

Usage (from the project root):
    uv run python src/build_employee_cvs.py                     # every CV that is out of date
    uv run python src/build_employee_cvs.py paal-noedseth [...]  # only these people (folder names)
    uv run python src/build_employee_cvs.py --list | --dry-run | --force | --no-check

For each person two targets are built next to the CV, both kept out of git by .gitignore:
    cvs/<name>/<name>.pdf                       the CV (src/build_cv_pdf.py)
    cvs/<name>/visittkort-<name>.pdf and .png   the business card (src/build_cv_business_cards.py)
A target is rebuilt only when it is missing or the CV, its photo, the shared logos in cvs/logos/ or the build
scripts and styles are newer.
After the builds, every CV is checked against the shared conventions (src/check_cv_md.py).
src/build_all.py runs this script as its last step.
"""
from __future__ import annotations

import argparse

from build_targets import ROOT, Target, build, print_table, reconfigure_output, run, uv

VP = "deliverable/visualprofile"
ASSET_SVGS = [f"{VP}/profile/assets/*.svg", f"{VP}/profile/assets/presentation/*.svg"]


def people() -> list[str]:
    return sorted(p.name for p in (ROOT / "cvs").iterdir() if p.is_dir() and (p / f"{p.name}.md").is_file())


def targets(names: list[str]) -> list[Target]:
    t = []
    for n in names:
        src = f"cvs/{n}/{n}.md"
        t.append(Target("cv", f"{n}: CV", uv("build_cv_pdf.py", src, f"cvs/{n}/{n}.pdf"),
                        [src, f"cvs/{n}/images", "cvs/logos", *ASSET_SVGS, "src/cv_pdf", "src/build_cv_pdf.py",
                         "src/cv_markdown.py"], [f"cvs/{n}/{n}.pdf"]))
        t.append(Target("card", f"{n}: business card", uv("build_cv_business_cards.py", src),
                        [src, f"{VP}/profile/colors.json", *ASSET_SVGS, f"{VP}/profile/assets/pdf/*.pdf", "src/business_card",
                         "src/build_business_card.py", "src/build_cv_business_cards.py", "src/build_presentation.py",
                         "src/cv_markdown.py"],
                        [f"cvs/{n}/visittkort-{n}.pdf", f"cvs/{n}/visittkort-{n}.png"]))
    return t


def main() -> int:
    reconfigure_output()
    ap = argparse.ArgumentParser(description="Build the employees' CVs and business cards from cvs/")
    ap.add_argument("names", nargs="*", help="folder names in cvs/ (default: everyone)")
    ap.add_argument("--force", action="store_true", help="rebuild even when up to date")
    ap.add_argument("--list", action="store_true", help="list the targets and whether they are up to date")
    ap.add_argument("--dry-run", action="store_true", help="show what would be built, without building")
    ap.add_argument("--no-check", action="store_true", help="skip the CV check after the builds")
    args = ap.parse_args()

    everyone = people()
    unknown = [n for n in args.names if n not in everyone]
    if unknown:
        raise SystemExit(f"not found in cvs/: {', '.join(unknown)}")
    selected = targets(args.names or everyone)
    if args.list:
        for x in selected:
            stale, why = x.is_stale()
            print(f"{x.name:<44} {'OUT OF DATE: ' + why if stale else 'up to date'}")
        return 0
    code = print_table(build(selected, force=args.force, dry_run=args.dry_run, checks=False))
    if not args.no_check and not args.dry_run:
        files = [f"cvs/{n}/{n}.md" for n in (args.names or everyone)]
        ccode, out = run(["uv", "run", "python", "src/check_cv_md.py", *files])
        print("\nCV check: " + (out.splitlines()[-1] if out else ""))
        if ccode != 0:
            print(out)
            code = 1
    return code


if __name__ == "__main__":
    raise SystemExit(main())
