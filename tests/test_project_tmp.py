"""Work folders for the scripts are created in <project root>/tmp/, and no script uses the system temp folder."""
import re
from pathlib import Path

import pytest

import project_tmp

ROOT = Path(__file__).resolve().parent.parent


def test_mkdtemp_is_inside_project_tmp():
    p = project_tmp.mkdtemp("kwtest_")
    try:
        assert p.is_dir()
        assert p.parent == ROOT / "tmp"
        assert p.name.startswith("kwtest_")
    finally:
        p.rmdir()


def test_work_dir_is_deleted_after_the_block():
    with project_tmp.work_dir("kwtest_") as p:
        (p / "x.txt").write_text("x", encoding="utf-8")
        assert p.parent == ROOT / "tmp"
    assert not p.exists()


def test_work_dir_is_deleted_after_an_error():
    with pytest.raises(RuntimeError):
        with project_tmp.work_dir("kwtest_") as p:
            (p / "x.txt").write_text("x", encoding="utf-8")
            raise RuntimeError("build failed")
    assert not p.exists()


def test_work_dir_keep_leaves_the_folder():
    with project_tmp.work_dir("kwtest_", keep=True) as p:
        pass
    try:
        assert p.is_dir()
    finally:
        p.rmdir()


SCRIPTS = sorted(p for p in (ROOT / "src").rglob("*.py") if p.name != "project_tmp.py")


@pytest.mark.parametrize("script", SCRIPTS, ids=lambda p: p.relative_to(ROOT).as_posix())
def test_scripts_do_not_use_the_system_temp_folder(script: Path):
    text = script.read_text(encoding="utf-8")
    found = re.findall(r"^\s*(?:import tempfile|from tempfile import)|\bgettempdir\(|['\"]/tmp/", text, flags=re.M)
    assert not found, f"{script.name} uses the system temp folder; use src/project_tmp.py instead"
