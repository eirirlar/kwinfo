"""Work folders for the scripts in src/, inside the project: <project root>/tmp/ (ignored by git).

CLAUDE.md: scripts that choose where their intermediate files go keep them in the project, not in the
system's temporary folder. Installed programs (uv, LuaLaTeX, pytest, pandoc) keep their own caches.

    from project_tmp import mkdtemp, work_dir

    with work_dir("kwcv_") as work:          # deleted when the block ends, also after an error
        ...
    with work_dir("kwdeck_", keep=True) as work:   # kept; the caller prints the path
        ...
    work = mkdtemp("kwdoc_")                 # caller deletes it (e.g. in a finally block)
"""
from __future__ import annotations

import shutil
import tempfile
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

ROOT = Path(__file__).resolve().parent.parent
TMP = ROOT / "tmp"


def mkdtemp(prefix: str = "kw_") -> Path:
    """A new, unique folder under <project root>/tmp/. The caller is responsible for deleting it."""
    TMP.mkdir(exist_ok=True)
    return Path(tempfile.mkdtemp(prefix=prefix, dir=TMP))


@contextmanager
def work_dir(prefix: str = "kw_", keep: bool = False) -> Iterator[Path]:
    """A unique folder under <project root>/tmp/ for the duration of the block; deleted afterwards unless keep."""
    path = mkdtemp(prefix)
    try:
        yield path
    finally:
        if not keep:
            shutil.rmtree(path, ignore_errors=True)
