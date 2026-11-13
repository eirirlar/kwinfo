"""Build every generated file in the repo from its sources, in dependency order, and run the checks.

Usage (from the project root):
    uv run python src/build_all.py                  # everything that is out of date, then the employee CVs
    uv run python src/build_all.py --only cv,document
    uv run python src/build_all.py --list           # all targets and whether they are up to date
    uv run python src/build_all.py --dry-run        # what would be built, and why
    uv run python src/build_all.py --force          # rebuild everything
    uv run python src/build_all.py --no-check       # skip the checks after each build

Generated files (PDF, PNG) are not kept in git; they lie next to their sources and are ignored by
.gitignore. A target is rebuilt only when an output is missing or one of its inputs (source, images,
styles and templates, the build script, the font zip) is newer than its outputs.

Groups, in build order (later groups use the output of earlier ones):
    assets         logo and graphics SVG -> PDF and PNG            src/export_profile_assets.py
    profile        the profile manual                              src/build_profile_manual.py
    cv             CV template and example                         src/build_cv_pdf.py
    presentation   presentation template and example               src/build_presentation.py
    document       letter and document templates and examples      src/build_document.py
    business-card  business card template and example              src/build_business_card.py
    overview       the overview sheet of all deliverables          src/build_visualprofile_overview.py
    employee-cvs   every CV in cvs/ and its business card          src/build_employee_cvs.py (own change check)
"""
from __future__ import annotations

import argparse

from build_targets import ROOT, Target, build, print_table, reconfigure_output, run, uv

VP = "deliverable/visualprofile"
GROUPS = ["assets", "profile", "cv", "presentation", "document", "business-card", "overview", "employee-cvs"]

# The logo and graphics sources (SVG); the exported PDF/PNG next to them are outputs, not inputs.
ASSET_SVGS = [f"{VP}/profile/assets/*.svg", f"{VP}/profile/assets/presentation/*.svg"]
# Inputs every build of a profile-coloured deliverable reads (they copy the exported logo PDFs).
PROFILE_DATA = [f"{VP}/profile/colors.json", *ASSET_SVGS, f"{VP}/profile/assets/pdf/*.pdf"]


def asset_targets() -> list[Target]:
    svgs = sorted((ROOT / VP / "profile/assets").rglob("*.svg"))
    outs = []
    for s in svgs:
        outs += [f"{VP}/profile/assets/pdf/{s.stem}.pdf", f"{VP}/profile/assets/png/{s.stem}.png"]
    return [Target("assets", "assets: logos and graphics", uv("export_profile_assets.py"),
                   [*ASSET_SVGS, "src/export_profile_assets.py"], outs)]


def targets() -> list[Target]:
    t: list[Target] = asset_targets()
    t.append(Target("profile", "profile/profile-manual.pdf", uv("build_profile_manual.py"),
                    [f"{VP}/profile/profile-manual.md", f"{VP}/profile/images", *ASSET_SVGS,
                     "src/profile_manual", "src/build_profile_manual.py"],
                    [f"{VP}/profile/profile-manual.pdf"]))
    for stem in ("cv-template", "cv-example"):
        src, pdf = f"{VP}/cv/{stem}.md", f"{VP}/cv/{stem}.pdf"
        check = ["uv", "run", "python", "src/check_cv_md.py", src] if stem == "cv-example" else None
        t.append(Target("cv", f"cv/{stem}.pdf", uv("build_cv_pdf.py", src, pdf),
                        [src, f"{VP}/cv/images", *ASSET_SVGS, "src/cv_pdf", "src/build_cv_pdf.py",
                         "src/cv_markdown.py"], [pdf], check=check))
    for stem in ("presentation-template", "example"):
        src, pdf = f"{VP}/presentation/{stem}.md", f"{VP}/presentation/{stem}.pdf"
        t.append(Target("presentation", f"presentation/{stem}.pdf", uv("build_presentation.py", src),
                        [src, f"{VP}/presentation/images", *PROFILE_DATA, "src/presentation",
                         "src/build_presentation.py"], [pdf], check=uv("check_presentation_pdf.py", pdf)))
    for stem in ("letter-template", "document-template", "example-letter", "example-job-posting"):
        src, pdf = f"{VP}/document/{stem}.md", f"{VP}/document/{stem}.pdf"
        t.append(Target("document", f"document/{stem}.pdf", uv("build_document.py", src),
                        [src, *PROFILE_DATA, "src/document", "src/build_document.py", "src/build_presentation.py"],
                        [pdf], check=uv("check_document_pdf.py", pdf)))
    for stem in ("business-card-template", "business-card-example"):
        src = f"{VP}/business-card/{stem}.md"
        t.append(Target("business-card", f"business-card/{stem}.pdf", uv("build_business_card.py", src),
                        [src, *PROFILE_DATA, "src/business_card", "src/build_business_card.py",
                         "src/build_presentation.py"],
                        [f"{VP}/business-card/{stem}.pdf", f"{VP}/business-card/{stem}.png"],
                        note="the print checks run inside the build"))
    deliverable_pdfs = [o for x in t for o in x.outputs if o.endswith(".pdf") and "/assets/" not in o]
    t.append(Target("overview", "overview.pdf", uv("build_visualprofile_overview.py"),
                    deliverable_pdfs + ["src/build_visualprofile_overview.py"], [f"{VP}/overview.pdf"]))
    return t


def sources() -> list[str]:
    """Every Markdown source that becomes a PDF (used by the test that the list is complete)."""
    return sorted({i for x in targets() for i in x.inputs if i.endswith(".md")})


def main() -> int:
    reconfigure_output()
    ap = argparse.ArgumentParser(description="Build every generated file from its sources")
    ap.add_argument("--only", help=f"comma-separated groups: {', '.join(GROUPS)}")
    ap.add_argument("--force", action="store_true", help="rebuild even when up to date")
    ap.add_argument("--list", action="store_true", help="list the targets and whether they are up to date")
    ap.add_argument("--dry-run", action="store_true", help="show what would be built, without building")
    ap.add_argument("--no-check", action="store_true", help="skip the checks after each build")
    args = ap.parse_args()

    groups = GROUPS if not args.only else [g.strip() for g in args.only.split(",") if g.strip()]
    unknown = [g for g in groups if g not in GROUPS]
    if unknown:
        raise SystemExit(f"unknown group(s): {', '.join(unknown)} (valid: {', '.join(GROUPS)})")
    selected = [x for x in targets() if x.group in groups]

    if args.list:
        for x in selected:
            stale, why = x.is_stale()
            print(f"{x.group:<14} {x.name:<42} {'OUT OF DATE: ' + why if stale else 'up to date'}")
        if "employee-cvs" in groups:
            print(f"{'employee-cvs':<14} {'cvs/*/ (see src/build_employee_cvs.py --list)':<42}")
        return 0

    rows = build(selected, force=args.force, dry_run=args.dry_run, checks=not args.no_check)
    code = print_table(rows) if rows else 0
    if "employee-cvs" in groups:
        cmd = ["uv", "run", "python", "src/build_employee_cvs.py"]
        cmd += ["--force"] if args.force else []
        cmd += ["--dry-run"] if args.dry_run else []
        cmd += ["--no-check"] if args.no_check else []
        print("\n== employee CVs (src/build_employee_cvs.py)")
        ecode, out = run(cmd, timeout=3600)
        print(out)
        code = code or ecode
    return code


if __name__ == "__main__":
    raise SystemExit(main())
