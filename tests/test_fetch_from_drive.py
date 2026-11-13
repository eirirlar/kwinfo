import os
from datetime import datetime, timezone
from pathlib import Path

import pytest

from fetch_from_drive import (
    DEFAULT_OUT,
    DOC_MIME,
    FOLDER_MIME,
    SHEET_MIME,
    SLIDES_MIME,
    Item,
    drive_timestamp,
    expand,
    export_choice,
    extract_id,
    is_folder_link,
    is_up_to_date,
    parse_args,
    read_link_list,
    safe_filename,
    target_filename,
)

ID = "18jkCKtiE1Q0gbZsZtwPFtZzsYluGlYQWjLAZRKkY0Pk"


@pytest.mark.parametrize(
    "ref, expected",
    [
        ("https://docs.google.com/document/d/abc123", "abc123"),
        ("https://docs.google.com/document/d/abc123/edit?tab=t.0", "abc123"),
        ("https://docs.google.com/document/u/0/d/abc123/edit", "abc123"),
        ("https://docs.google.com/spreadsheets/d/sheet1/edit#gid=0", "sheet1"),
        ("https://docs.google.com/presentation/d/deck1/edit", "deck1"),
        ("https://drive.google.com/file/d/xyz789/view", "xyz789"),
        ("https://drive.google.com/open?id=qwe456", "qwe456"),
        ("https://drive.google.com/drive/folders/fold123", "fold123"),
        ("https://drive.google.com/drive/u/1/folders/fold123?usp=sharing", "fold123"),
        (ID, ID),
        (f"  {ID}  ", ID),
        ("https://example.com/nothing", None),
        ("not an id", None),
        ("short", None),
    ],
)
def test_extract_id(ref, expected):
    assert extract_id(ref) == expected


@pytest.mark.parametrize(
    "ref, expected",
    [
        ("https://drive.google.com/drive/folders/fold123", True),
        ("https://drive.google.com/drive/u/0/folders/fold123", True),
        ("https://docs.google.com/document/d/abc123", False),
        (ID, False),
    ],
)
def test_is_folder_link(ref, expected):
    assert is_folder_link(ref) is expected


def test_safe_filename_removes_forbidden_characters():
    assert safe_filename('Master CV: Pål / "Nødseth"?') == "Master CV_ Pål _ _Nødseth__"


@pytest.mark.parametrize(
    "name, mime, fmt, expected",
    [
        ("Master CV - Pål Nødseth", DOC_MIME, "docx", "Master CV - Pål Nødseth.docx"),
        ("Notat", DOC_MIME, "md", "Notat.md"),
        ("Notat.pdf", DOC_MIME, "pdf", "Notat.pdf"),
        ("Budsjett", SHEET_MIME, "docx", "Budsjett.xlsx"),
        ("Budsjett", SHEET_MIME, "pdf", "Budsjett.pdf"),
        ("Deck", SLIDES_MIME, "md", "Deck.pptx"),
        ("cv.pdf", "application/pdf", "docx", "cv.pdf"),
        ("photo.jpg", "image/jpeg", "md", "photo.jpg"),
    ],
)
def test_target_filename(name, mime, fmt, expected):
    assert target_filename(name, mime, fmt) == expected


def test_export_choice_rejects_forms():
    with pytest.raises(ValueError):
        export_choice("application/vnd.google-apps.form", "docx")


def test_read_link_list_semicolon_and_comma(tmp_path: Path):
    a = tmp_path / "a.csv"
    a.write_text("Name;Link;Intern;\nOla;https://docs.google.com/document/d/id1;TRUE;\n;;\nKari;x2;FALSE;\n",
                 encoding="utf-8")
    assert read_link_list(a) == ["https://docs.google.com/document/d/id1", "x2"]
    b = tmp_path / "b.csv"
    b.write_text("Link,Note\nhttps://drive.google.com/drive/folders/f1,mappe\n", encoding="utf-8")
    assert read_link_list(b) == ["https://drive.google.com/drive/folders/f1"]


def test_read_link_list_needs_link_column(tmp_path: Path):
    f = tmp_path / "x.csv"
    f.write_text("Name;Url\nOla;x\n", encoding="utf-8")
    with pytest.raises(SystemExit):
        read_link_list(f)


def test_parse_args_defaults_and_list(tmp_path: Path):
    a = parse_args([ID])
    assert a.refs == [ID] and a.out == DEFAULT_OUT and a.format == "docx" and not a.recursive
    f = tmp_path / "l.csv"
    f.write_text("Link\nabcdefghijklm\n", encoding="utf-8")
    b = parse_args(["--list", str(f), "--format", "md", "--recursive", "--out", "x"])
    assert b.refs == ["abcdefghijklm"] and b.format == "md" and b.recursive and b.out == Path("x")


def test_parse_args_requires_something():
    with pytest.raises(SystemExit):
        parse_args([])


def test_default_out_is_ignored_by_git():
    root = Path(__file__).resolve().parent.parent
    lines = (root / ".gitignore").read_text(encoding="utf-8").splitlines()
    assert DEFAULT_OUT.parts[0] + "/" in lines


class FakeDrive:
    """files().list(...).execute() over a fixed tree, enough for expand()."""

    def __init__(self, tree: dict[str, list[dict]]):
        self.tree = tree

    def files(self):
        return self

    def list(self, q, **_):
        folder = q.split("'")[1]
        return type("R", (), {"execute": lambda _s: {"files": self.tree.get(folder, [])}})()


def _f(i, name, mime="application/pdf"):
    return {"id": i, "name": name, "mimeType": mime, "modifiedTime": "2026-10-01T08:00:00Z"}


TREE = {"root": [_f("s", "Sub", FOLDER_MIME), _f("a", "a.pdf")], "s": [_f("b", "b.pdf")]}


def test_expand_folder_without_recursive_skips_subfolders():
    notes: list[str] = []
    items = expand(FakeDrive(TREE), _f("root", "Mappe", FOLDER_MIME), recursive=False, notes=notes)
    assert [(i.subdir, i.name) for i in items] == [("Mappe", "a.pdf")]
    assert notes and "Sub" in notes[0]


def test_expand_folder_recursive_mirrors_subfolders():
    items = expand(FakeDrive(TREE), _f("root", "Mappe", FOLDER_MIME), recursive=True)
    assert [(i.subdir, i.name) for i in items] == [("Mappe", "a.pdf"), ("Mappe/Sub", "b.pdf")]


def test_expand_single_file():
    assert expand(FakeDrive({}), _f("a", "a.pdf"), recursive=False) == [
        Item("a", "a.pdf", "application/pdf", "2026-10-01T08:00:00Z", "")]


def test_drive_timestamp_parses_utc_with_fraction():
    expected = datetime(2026, 10, 1, 8, 15, 30, 123000, tzinfo=timezone.utc).timestamp()
    assert drive_timestamp("2026-10-01T08:15:30.123Z") == expected


def test_is_up_to_date_compares_mtime_with_drive(tmp_path: Path):
    f = tmp_path / "cv.docx"
    ts = drive_timestamp("2026-10-01T08:15:30.123Z")
    assert not is_up_to_date(f, ts)  # missing file
    f.write_bytes(b"x")
    os.utime(f, (ts, ts))
    assert is_up_to_date(f, ts)
    assert not is_up_to_date(f, ts + 3600)  # changed on Drive since download
