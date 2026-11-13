"""Guard against machine-specific fonts in LaTeX builds (lualatex).

Every document we build must look the same on Windows, WSL2 and Linux, whatever fonts happen to be
installed. Fonts may therefore only come from the build folder (unpacked from files in the repo, e.g.
the licensed Non Natural Grotesk zip) or from the TeX distribution itself (TeX Gyre, DejaVu, Latin
Modern ...). A font found through the operating system (the Windows font folders, the system and
user font folders on Linux and macOS) makes the build fail.

How: the build writes HOOK_TEX into the build folder and the document inputs it in the preamble
(`\\InputIfFileExists{fontguard.tex}{}{}`). At the end of the run it writes the file name of every font
LuaTeX loaded to fontfiles.txt; check() compares those paths with the allowed roots. (The -recorder
.fls file is not enough: fonts that fontspec loads with Path= are not listed there.)

Usage in a build script:
    font_guard.write_hook(work)          # before lualatex
    ...run lualatex in work...
    font_guard.check(work)               # after lualatex; raises SystemExit on a violation
"""
import os
import subprocess
from functools import lru_cache
from pathlib import Path

HOOK_NAME = "fontguard.tex"
LIST_NAME = "fontfiles.txt"

HOOK_TEX = r"""% Written by src/font_guard.py: list every font file LuaTeX loaded (checked after the run).
\AtEndDocument{\directlua{
  local out = io.open("@LIST@", "w")
  for id, f in font.each() do
    if f.filename then out:write(f.filename, string.char(10)) end
  end
  out:close()
}}
""".replace("@LIST@", LIST_NAME)

def _norm(p: str | Path) -> str:
    s = os.path.normcase(os.path.abspath(str(p))).replace("\\", "/")
    return s.rstrip("/") + "/"


@lru_cache(maxsize=1)
def texmf_roots() -> tuple[str, ...]:
    """TeX's own trees: every folder in TeX's search path $TEXMF, as kpathsea expands it.

    Fonts inside them come with the TeX distribution, not with the OS. Asking kpathsea for the
    whole search path covers every distribution's layout (TeX Live from tug.org, and Debian/Ubuntu,
    which install e.g. Latin Modern in a separate tree) without naming any of them here.
    """
    r = subprocess.run(["kpsewhich", "--expand-path=$TEXMF"], capture_output=True, text=True, check=True)
    roots = [_norm(part) for part in r.stdout.strip().split(os.pathsep) if part.strip()]
    return tuple(sorted(set(roots)))


def write_hook(work: Path) -> None:
    (work / HOOK_NAME).write_text(HOOK_TEX, encoding="utf-8", newline="\n")


def offending(work: Path) -> list[str]:
    """Font files outside the build folder and the TeX trees ([] if all are fine)."""
    listing = work / LIST_NAME
    if not listing.exists():
        return [f"{LIST_NAME} was not written (is {HOOK_NAME} input in the preamble?)"]
    allowed = (_norm(work),) + texmf_roots()
    bad = []
    for line in sorted(set(listing.read_text(encoding="utf-8").splitlines())):
        path = line.strip()
        if not path:
            continue
        full = path if Path(path).is_absolute() else str(work / path)
        if not _norm(full).startswith(allowed):
            bad.append(path)
    return bad


def check(work: Path) -> None:
    bad = offending(work)
    if bad:
        raise SystemExit("font_guard: fonts from outside the repo and TeX Live were used; the build would "
                         "look different on other machines:\n  " + "\n  ".join(bad))
