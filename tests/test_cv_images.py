"""Image rules for the employees' CVs: header reading and checks in src/check_cv_md.py, and the normalizer."""
import struct
import subprocess
import zlib
from pathlib import Path

import pytest

from check_cv_md import LOGO_MAX_PX, PHOTO_MAX_CROP_W, check_text, image_info
from test_check_cv_md import GOOD

ROOT = Path(__file__).resolve().parent.parent


def png(w: int, h: int, icc: bool = False) -> bytes:
    def chunk(kind: bytes, data: bytes) -> bytes:
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data))
    raw = b"".join(b"\x00" + b"\x00" * w for _ in range(h))   # grey, filter byte per row
    body = chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 0, 0, 0, 0))
    if icc:
        body += chunk(b"iCCP", b"sRGB\x00\x00" + zlib.compress(b"x"))
    return b"\x89PNG\r\n\x1a\n" + body + chunk(b"IDAT", zlib.compress(raw)) + chunk(b"IEND", b"")


def jpeg_header(w: int, h: int, exif: bool = False) -> bytes:
    """Only the headers image_info reads: SOI, optional APP1 Exif, SOF0 and SOS."""
    out = b"\xff\xd8"
    if exif:
        seg = b"Exif\x00\x00" + b"\x00" * 8
        out += b"\xff\xe1" + struct.pack(">H", len(seg) + 2) + seg
    sof = struct.pack(">BHHB", 8, h, w, 3) + b"\x01\x11\x00\x02\x11\x00\x03\x11\x00"
    out += b"\xff\xc0" + struct.pack(">H", len(sof) + 2) + sof
    out += b"\xff\xda" + struct.pack(">H", 2)
    return out


def test_image_info_png(tmp_path: Path):
    (tmp_path / "a.png").write_bytes(png(30, 20))
    (tmp_path / "b.png").write_bytes(png(30, 20, icc=True))
    assert image_info(tmp_path / "a.png") == ("png", 30, 20, False)
    assert image_info(tmp_path / "b.png") == ("png", 30, 20, True)


def test_image_info_jpeg(tmp_path: Path):
    (tmp_path / "a.jpg").write_bytes(jpeg_header(1200, 1480))
    (tmp_path / "b.jpg").write_bytes(jpeg_header(640, 480, exif=True))
    assert image_info(tmp_path / "a.jpg") == ("jpeg", 1200, 1480, False)
    assert image_info(tmp_path / "b.jpg") == ("jpeg", 640, 480, True)


def test_image_info_other(tmp_path: Path):
    (tmp_path / "a.svg").write_text("<svg/>", encoding="utf-8")
    assert image_info(tmp_path / "a.svg") is None


def employee_cv(tmp_path: Path, photo: str, photo_bytes: bytes, logo: str | None, logo_bytes: bytes | None) -> list[str]:
    """Check GOOD as an employee CV in tmp/cvs/ola/, with the given photo and logo for the first project."""
    folder = tmp_path / "cvs" / "ola"
    (folder / "images").mkdir(parents=True)
    (folder / photo).write_bytes(photo_bytes)
    text = GOOD.replace("- Språk: norsk, engelsk", f"- Språk: norsk, engelsk\n- Foto: {photo}")
    if logo:
        (folder / logo).parent.mkdir(parents=True, exist_ok=True)
        (folder / logo).write_bytes(logo_bytes)
        text = text.replace("- Periode: 03.2022 – nå", f"- Periode: 03.2022 – nå\n- Logo: {logo}")
    return check_text(text, base=folder)


def test_employee_cv_with_normalized_images_passes(tmp_path: Path):
    issues = employee_cv(tmp_path, "images/photo.jpg", jpeg_header(PHOTO_MAX_CROP_W, 1480),
                         "../logos/equinor.png", png(357, 141))
    assert issues == []


@pytest.mark.parametrize("photo, data, expected", [
    ("images/photo.png", png(400, 500), "should be a JPG"),
    ("images/photo.jpg", jpeg_header(2000, 2000), "larger than needed"),
    ("images/photo.jpg", jpeg_header(800, 1000, exif=True), "metadata"),
])
def test_employee_photo_rules(tmp_path: Path, photo: str, data: bytes, expected: str):
    issues = employee_cv(tmp_path, photo, data, None, None)
    assert any(expected in i for i in issues), issues


def test_employee_landscape_photo_crop_width(tmp_path: Path):
    # 2048 x 1277: the largest 60:74 crop is about 1035 px wide, within the limit
    assert employee_cv(tmp_path, "images/photo.jpg", jpeg_header(2048, 1277), None, None) == []


def test_employee_logo_must_come_from_library(tmp_path: Path):
    issues = employee_cv(tmp_path, "images/photo.jpg", jpeg_header(800, 1000), "images/logo-equinor.png", png(300, 100))
    assert any("shared library" in i for i in issues), issues


def test_employee_logo_size(tmp_path: Path):
    w, h = LOGO_MAX_PX
    issues = employee_cv(tmp_path, "images/photo.jpg", jpeg_header(800, 1000), "../logos/big.png", png(w + 1, h))
    assert any("larger than needed" in i for i in issues), issues


def test_template_cv_keeps_its_own_images(tmp_path: Path):
    """Outside cvs/ (the CV template and example) logos stay in images/ and the image format is not checked."""
    (tmp_path / "images").mkdir()
    (tmp_path / "images/photo.png").write_bytes(png(2000, 2000))
    (tmp_path / "images/logo-equinor.png").write_bytes(png(2000, 1000))
    text = GOOD.replace("- Språk: norsk, engelsk", "- Språk: norsk, engelsk\n- Foto: images/photo.png")
    text = text.replace("- Periode: 03.2022 – nå", "- Periode: 03.2022 – nå\n- Logo: images/logo-equinor.png")
    assert check_text(text, base=tmp_path) == []


def test_repo_has_one_file_per_logo_and_no_logos_in_person_folders():
    assert not list(ROOT.glob("cvs/*/images/logo-*"))
    stems = [p.stem for p in (ROOT / "cvs/logos").iterdir() if p.is_file()]
    assert stems and len(stems) == len(set(stems))


@pytest.mark.timeout(90)
def test_normalizer_self_test():
    """src/normalize_cv_images.py needs Pillow (PEP 723), so its rules are checked in a separate uv process."""
    res = subprocess.run(["uv", "run", "src/normalize_cv_images.py", "--self-test"], cwd=ROOT,
                         capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=80)
    assert res.returncode == 0, res.stdout + res.stderr
    assert "SELF-TEST OK" in res.stdout
