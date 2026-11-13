"""The build list in src/build_all.py is complete, and .gitignore keeps built files out of git but not sources."""
from __future__ import annotations

import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

import build_all  # noqa: E402
import build_employee_cvs  # noqa: E402

VP = ROOT / "deliverable" / "visualprofile"
# Markdown in the template folders that is reference text, not a build source.
NOT_BUILT = {"deliverable/visualprofile/profile/colors.md"}


def ignore_patterns() -> list[re.Pattern]:
    """The .gitignore lines as regexes over root-relative POSIX paths (enough for the patterns used here)."""
    pats = []
    for line in (ROOT / ".gitignore").read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        assert not line.startswith("!"), "negated patterns are not handled by this test"
        directory = line.endswith("/")
        body = line.strip("/")
        rx = "".join("[^/]*" if c == "*" else re.escape(c) for c in body)
        prefix = "" if "/" in body else "(?:.*/)?"      # a bare name matches at any depth
        pats.append(re.compile(f"^{prefix}{rx}" + ("/.*$" if directory else "(?:/.*)?$")))
    return pats


PATTERNS = ignore_patterns()


def ignored(rel: str) -> bool:
    return any(p.match(rel) for p in PATTERNS)


def rel(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()


SOURCES = sorted(rel(p) for p in VP.rglob("*.md") if p.name != "README.md" and rel(p) not in NOT_BUILT)


@pytest.mark.parametrize("source", SOURCES)
def test_every_template_source_is_built(source: str) -> None:
    assert source in build_all.sources(), f"{source} is not in the build list in src/build_all.py"


OUTPUTS = sorted({o for t in build_all.targets() for o in t.outputs}
                 | {o for t in build_employee_cvs.targets(build_employee_cvs.people()) for o in t.outputs})


@pytest.mark.parametrize("output", OUTPUTS)
def test_built_files_are_ignored(output: str) -> None:
    assert ignored(output), f"{output} is built but not covered by .gitignore"


TRACKED = sorted(set(build_all.sources())
                 | {rel(p) for p in (ROOT / "cvs").glob("*/*.md")}
                 | {rel(p) for p in (ROOT / "cvs").glob("*/images/*")}
                 | {rel(p) for p in VP.glob("*/images/*")}
                 | {rel(p) for p in (VP / "profile" / "assets").rglob("*.svg")}
                 | {"cvs/DEVIATIONS.md", "deliverable/visualprofile/profile/colors.json"})


@pytest.mark.parametrize("source", TRACKED)
def test_sources_are_not_ignored(source: str) -> None:
    assert not ignored(source), f"{source} is a source but .gitignore excludes it"


def test_matcher_sanity() -> None:
    assert ignored("data/anything/x.xlsx")
    assert ignored("src/__pycache__/x.pyc")
    assert not ignored("src/build_all.py")


@pytest.mark.parametrize("name", build_employee_cvs.people())
def test_employee_cv_inputs_exist_in_a_clean_checkout(name: str) -> None:
    # Only tracked files may be required: a folder that is empty on one machine does not exist in a clone.
    for target in build_employee_cvs.targets([name]):
        assert target.missing_inputs() == [], f"{target.name}: required inputs are missing"
