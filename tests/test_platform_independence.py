"""Builds must not depend on the operating system or on fonts installed on the machine.

Fonts come from files in the repo (the licensed Non Natural Grotesk zip) or from TeX Live.
"""
import re
from pathlib import Path

import pytest

import font_guard

ROOT = Path(__file__).resolve().parent.parent

# Sources that feed the document builds.
BUILD_SOURCES = sorted(
    [p for p in (ROOT / "src").rglob("*") if p.suffix in {".py", ".tex", ".lua"}]
    + [ROOT / "deliverable" / "visualprofile" / "profile" / "profilmanual.md"]
)

# References to OS font folders or to fonts that only exist when installed in the OS.
FORBIDDEN = [
    r"[A-Za-z]:[/\\]+Windows[/\\]+Fonts",
    r"AppData[/\\]+Local[/\\]+Microsoft[/\\]+Windows[/\\]+Fonts",
    r"/usr/share/fonts",
    r"/Library/Fonts",
    r"~/\.fonts",
    r"truetype\(\s*[\"'](arial|calibri|times|consolas)",
    r"mainfont\s*=\s*(Arial|Consolas|Calibri|\"?Times New Roman)",
    r"monofont\s*=\s*(Consolas|Courier New)",
    r"\{(arial|consolas|calibri|times)\.ttf\}",
]


@pytest.mark.parametrize("path", BUILD_SOURCES, ids=lambda p: str(p.relative_to(ROOT)))
def test_no_os_font_references(path: Path) -> None:
    text = path.read_text(encoding="utf-8", errors="replace")
    hits = [m.group(0) for pat in FORBIDDEN for m in re.finditer(pat, text, re.IGNORECASE)]
    assert hits == [], f"{path.relative_to(ROOT)} refers to OS fonts: {hits}"


def test_guard_accepts_build_folder_and_rejects_os_fonts(tmp_path: Path, monkeypatch) -> None:
    texmf = tmp_path / "texlive" / "texmf-dist"
    monkeypatch.setattr(font_guard, "texmf_roots", lambda: (font_guard._norm(texmf),))
    work = tmp_path / "work"
    work.mkdir()
    (work / font_guard.LIST_NAME).write_text("\n".join([
        str(work / "fonts" / "NON Natural Grotesk-Regular.otf"),
        str(texmf / "fonts" / "opentype" / "public" / "tex-gyre" / "texgyreheros-regular.otf"),
        "C:/Windows/Fonts/arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]), encoding="utf-8")
    assert font_guard.offending(work) == ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
                                          "C:/Windows/Fonts/arial.ttf"]
    with pytest.raises(SystemExit):
        font_guard.check(work)


def test_guard_fails_when_listing_is_missing(tmp_path: Path) -> None:
    assert font_guard.offending(tmp_path) != []
