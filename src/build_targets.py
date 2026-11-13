"""Shared helpers for src/build_all.py and src/build_employee_cvs.py: build targets with a change check.

A Target is one build step: the command that builds it, the files it reads (sources and dependencies:
images, styles, templates, the build script itself) and the files it writes. It is out of date when an
output is missing or any input is newer than the oldest output. Paths are relative to the project root.
Generated files live next to their sources and are kept out of git by .gitignore.
"""
from __future__ import annotations

import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Inputs shared by every LaTeX build: the licensed font zip, the font guard and the kerning fixes.
FONT_ZIP = "background/visualprofile/Fonts/Non Natural Grotesk/Desktop variant/NonNaturalGroteskFontFamily-hqlqfp.zip"
COMMON = [FONT_ZIP, "src/font_guard.py", "src/profile_manual/kernfix.json"]


@dataclass
class Target:
    group: str
    name: str
    command: list[str]
    inputs: list[str]                        # files, folders (all files inside) or globs
    outputs: list[str]
    check: list[str] | None = None           # optional check command run after the build
    note: str = ""

    def input_files(self) -> list[Path]:
        files: list[Path] = []
        for spec in self.inputs + COMMON:
            if any(c in spec for c in "*?["):
                files += [p for p in ROOT.glob(spec) if p.is_file()]
                continue
            p = ROOT / spec
            if p.is_dir():
                files += [q for q in p.rglob("*") if q.is_file() and "__pycache__" not in q.parts]
            elif p.is_file():
                files.append(p)
        return files

    def output_files(self) -> list[Path]:
        return [ROOT / o for o in self.outputs]

    def missing_inputs(self) -> list[str]:
        return [s for s in self.inputs if not any(c in s for c in "*?[") and not (ROOT / s).exists()]

    def is_stale(self) -> tuple[bool, str]:
        outs = self.output_files()
        missing = [o for o in outs if not o.exists()]
        if missing:
            return True, f"missing {missing[0].relative_to(ROOT).as_posix()}"
        oldest = min(o.stat().st_mtime for o in outs)
        newer = [p for p in self.input_files() if p.stat().st_mtime > oldest + 1e-6]
        if newer:
            newest = max(newer, key=lambda p: p.stat().st_mtime)
            return True, f"{newest.relative_to(ROOT).as_posix()} is newer"
        return False, "up to date"


def run(cmd: list[str], timeout: int = 600) -> tuple[int, str]:
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace",
                         timeout=timeout)
    return res.returncode, (res.stdout + res.stderr).strip()


def build(targets: list[Target], force: bool, dry_run: bool, checks: bool) -> list[tuple[str, str, str, float]]:
    """Build the out-of-date targets in order. Returns (target, status, detail, seconds) per target."""
    rows = []
    rebuilt: set[Path] = set()   # outputs built (or, in a dry run, to be built) in this run
    for t in targets:
        stale, why = (True, "forced") if force else t.is_stale()
        upstream = [p for p in t.input_files() if p in rebuilt]
        if not stale and upstream:
            stale, why = True, f"{upstream[0].relative_to(ROOT).as_posix()} is rebuilt in this run"
        if stale:
            rebuilt.update(t.output_files())
        if not stale:
            rows.append((t.name, "up to date", "", 0.0))
            continue
        lost = t.missing_inputs()
        if lost:
            rows.append((t.name, "FAILED", f"input missing: {lost[0]}", 0.0))
            continue
        if dry_run:
            rows.append((t.name, "would build", why, 0.0))
            continue
        print(f"build  {t.name}  ({why})", flush=True)
        start = time.time()
        code, out = run(t.command)
        status, detail = ("built", "") if code == 0 else ("FAILED", last_lines(out))
        if code == 0 and checks and t.check:
            ccode, cout = run(t.check)
            if ccode != 0:
                status, detail = "CHECK FAILED", last_lines(cout)
        rows.append((t.name, status, detail, time.time() - start))
    return rows


def last_lines(text: str, n: int = 3) -> str:
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    return " | ".join(lines[-n:])


def print_table(rows: list[tuple[str, str, str, float]]) -> int:
    width = max([len(r[0]) for r in rows] + [6])
    print()
    print(f"{'target':<{width}}  {'status':<13}  {'time':>6}  detail")
    for name, status, detail, secs in rows:
        print(f"{name:<{width}}  {status:<13}  {secs:5.1f}s  {detail}")
    failed = [r for r in rows if "FAILED" in r[1]]
    built = [r for r in rows if r[1] == "built"]
    print(f"\n{len(built)} built, {len(rows) - len(built) - len(failed)} unchanged or skipped, {len(failed)} failed")
    return 1 if failed else 0


def uv(script: str, *args: str) -> list[str]:
    """Command for a script in src/: scripts with a PEP 723 block run with 'uv run <script>'."""
    return ["uv", "run", f"src/{script}", *args]


def reconfigure_output() -> None:
    for s in (sys.stdout, sys.stderr):
        s.reconfigure(encoding="utf-8", errors="replace")
