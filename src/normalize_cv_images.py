# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow", "numpy"]
# ///
"""Bring the images of the employees' CVs to one format: small files, enough resolution, no metadata.

Usage (from the project root):
    uv run src/normalize_cv_images.py              # dry run: what would change, per file
    uv run src/normalize_cv_images.py --apply      # change the files
    uv run src/normalize_cv_images.py cvs/paal-noedseth/images/photo.jpg cvs/logos/equinor.png [--apply]
    uv run src/normalize_cv_images.py --self-test   # check the rules on synthetic images (used by the tests)

Default: every photo cvs/*/images/photo.* and every logo in the shared library cvs/logos/.

Photo: JPG, quality 85 (lower, down to 70, if the file would otherwise grow), sRGB, no metadata (EXIF, ICC); transparency is flattened onto white. Scaled down so the
largest crop in the CV's photo frame ratio (60:74) is PHOTO_MAX_CROP_W pixels wide (at most 1200 x 1480 for a
portrait photo), never up. The file is not cropped: src/build_cv_pdf.py crops it around photo_focus. A photo that
changes from .png to .jpg gets its reference in the CV (`- Foto: images/photo.png`) updated, and the .png is removed.

Logo (PNG/JPG; SVG is left alone): transparent or near-white margins are trimmed, then the logo is scaled down to
fit LOGO_MAX_PX, never up. A scaled PNG is saved as a 256-colour palette with transparency, optimised; JPG is saved at quality 90.

The script is idempotent: a file that already follows the format is not rewritten. Files that shrink to less than
30 % of their size are flagged in the dry run, to be looked at before --apply. The limits are shared with the
checks in src/check_cv_md.py.
"""
from __future__ import annotations

import argparse
import io
import re
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
from check_cv_md import LOGO_MAX_PX, PHOTO_MAX_CROP_W, PHOTO_RATIO  # noqa: E402

JPEG_PHOTO_QUALITY = 85
JPEG_PHOTO_MIN_QUALITY = 70   # lowest quality tried to keep a photo from growing
JPEG_LOGO_QUALITY = 90
INK_ALPHA, INK_WHITE = 16, 245   # a pixel is ink if alpha > INK_ALPHA and its darkest channel < INK_WHITE
FLAG_SHARE = 0.30


def photo_target(w: int, h: int) -> tuple[int, int]:
    """Size after scaling so the largest frame-ratio crop is at most PHOTO_MAX_CROP_W wide (never up)."""
    crop_w = min(w, h * PHOTO_RATIO)
    scale = min(1.0, PHOTO_MAX_CROP_W / crop_w)
    return (w, h) if scale >= 1.0 else (max(1, round(w * scale)), max(1, round(h * scale)))


def flatten(im: Image.Image) -> Image.Image:
    """RGB image; transparency composited onto white."""
    if im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info):
        rgba = im.convert("RGBA")
        bg = Image.new("RGBA", rgba.size, (255, 255, 255, 255))
        bg.alpha_composite(rgba)
        return bg.convert("RGB")
    return im.convert("RGB")


def normalize_photo(path: Path) -> tuple[bytes | None, Path, str]:
    """(new JPG bytes or None if unchanged, target path, description)."""
    im = Image.open(path)
    im = ImageOps.exif_transpose(im)   # keep the orientation the EXIF data asked for, then drop the EXIF
    target = path.with_suffix(".jpg")
    w, h = im.size
    tw, th = photo_target(w, h)
    has_meta = bool(Image.open(path).getexif()) or "icc_profile" in Image.open(path).info
    is_jpeg = Image.open(path).format == "JPEG" and path.suffix.lower() == ".jpg"
    if is_jpeg and (tw, th) == (w, h) and not has_meta and im.mode == "RGB":
        return None, path, "ok"
    out = flatten(im)
    if (tw, th) != (w, h):
        out = out.resize((tw, th), Image.LANCZOS)
    size = path.stat().st_size
    for q in range(JPEG_PHOTO_QUALITY, JPEG_PHOTO_MIN_QUALITY - 1, -5):
        buf = io.BytesIO()
        out.save(buf, "JPEG", quality=q, optimize=True, progressive=True)
        if buf.tell() <= size:   # an already well compressed original: do not let the file grow
            break
    reasons = [r for r, on in (("to JPG", not is_jpeg), (f"{w}x{h} -> {tw}x{th}", (tw, th) != (w, h)),
                               ("metadata removed", has_meta)) if on]
    return buf.getvalue(), target, ", ".join(reasons)


def ink_box(im: Image.Image) -> tuple[int, int, int, int] | None:
    a = np.asarray(im.convert("RGBA"))
    ink = (a[..., 3] > INK_ALPHA) & (a[..., :3].min(axis=2) < INK_WHITE)
    ys, xs = np.where(ink)
    if not len(xs):
        return None
    return int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1


def normalize_logo(path: Path) -> tuple[bytes | None, Path, str]:
    if path.suffix.lower() == ".svg":
        return None, path, "ok (SVG)"
    im = Image.open(path)
    fmt = im.format
    w, h = im.size
    box = ink_box(im)
    trimmed = box is not None and box != (0, 0, w, h)
    if trimmed:
        im = im.crop(box)
    cw, ch = im.size
    scale = min(1.0, LOGO_MAX_PX[0] / cw, LOGO_MAX_PX[1] / ch)
    if not trimmed and scale >= 1.0:
        return None, path, "ok"
    reasons = []
    if trimmed:
        reasons.append(f"margins trimmed {w}x{h} -> {cw}x{ch}")
    if scale < 1.0:
        nw, nh = max(1, round(cw * scale)), max(1, round(ch * scale))
        im = im.convert("RGBA" if fmt == "PNG" else "RGB").resize((nw, nh), Image.LANCZOS)
        if fmt == "PNG":   # back to a palette (alpha kept): a logo has few colours, and RGBA PNGs are large
            im = im.quantize(colors=256, method=Image.Quantize.FASTOCTREE)
        # resampling softens the outermost pixels, so trim again; otherwise a second run would trim more
        box = ink_box(im)
        if box is not None and box != (0, 0, *im.size):
            im = im.crop(box)
        reasons.append(f"scaled to {im.width}x{im.height}")
    buf = io.BytesIO()
    if fmt == "PNG":
        im.save(buf, "PNG", optimize=True)
    else:
        flatten(im).save(buf, "JPEG", quality=JPEG_LOGO_QUALITY, optimize=True)
    return buf.getvalue(), path, ", ".join(reasons)


def default_files() -> list[Path]:
    return sorted(ROOT.glob("cvs/*/images/photo.*")) + sorted(p for p in (ROOT / "cvs/logos").glob("*") if p.is_file())


def update_reference(old: Path, new: Path) -> bool:
    """Point the CV in the photo's person folder at the new file name."""
    cv = old.parent.parent / f"{old.parent.parent.name}.md"
    if not cv.is_file():
        return False
    text = cv.read_text(encoding="utf-8")
    pat = re.compile(rf"^(- (?:Foto|Photo): )images/{re.escape(old.name)}\s*$", re.M)
    new_text, n = pat.subn(rf"\g<1>images/{new.name}", text)
    if n:
        cv.write_text(new_text, encoding="utf-8", newline="\n")
    return bool(n)


def self_test() -> int:
    """Synthetic images in a work folder under tmp/: every rule of the format, and idempotence."""
    from check_cv_md import image_info
    from project_tmp import work_dir

    def check(cond: bool, what: str) -> None:
        if not cond:
            raise SystemExit(f"SELF-TEST FAILED: {what}")

    with work_dir("kwnormtest_") as work:
        person = work / "cvs" / "ola" / "images"
        person.mkdir(parents=True)
        cv = work / "cvs" / "ola" / "ola.md"
        cv.write_text("# Ola\n\n- Foto: images/photo.png\n", encoding="utf-8")
        # photo: large RGBA PNG, half transparent -> JPG, flattened on white, crop width 1200
        im = Image.new("RGBA", (1600, 2400), (200, 30, 30, 255))
        im.paste((0, 0, 0, 0), (0, 0, 800, 2400))
        im.save(person / "photo.png")
        data, target, _ = normalize_photo(person / "photo.png")
        check(target.name == "photo.jpg", "a PNG photo becomes photo.jpg")
        target.write_bytes(data)
        check(update_reference(person / "photo.png", target), "the CV reference is updated")
        check("images/photo.jpg" in cv.read_text(encoding="utf-8"), "the CV points at photo.jpg")
        fmt, w, h, meta = image_info(target)
        check(fmt == "jpeg" and not meta, "the photo is a JPG without metadata")
        check(round(min(w, h * PHOTO_RATIO)) == PHOTO_MAX_CROP_W, f"the crop is {PHOTO_MAX_CROP_W} px wide ({w}x{h})")
        px = Image.open(target).convert("RGB").getpixel((10, 10))
        check(min(px) > 240, f"transparency is flattened onto white ({px})")
        check(normalize_photo(target)[0] is None, "a normalized photo is left alone (idempotent)")
        # photo with EXIF and small size: metadata removed, never scaled up
        small = person.parent.parent / "kari" / "images"
        small.mkdir(parents=True)
        exif = Image.Exif()
        exif[0x010F] = "Camera maker"
        Image.new("RGB", (400, 500), (90, 120, 150)).save(small / "photo.jpg", exif=exif, quality=95)
        check(image_info(small / "photo.jpg")[3], "the test photo has metadata")
        data, target, _ = normalize_photo(small / "photo.jpg")
        target.write_bytes(data)
        fmt, w, h, meta = image_info(target)
        check((w, h) == (400, 500) and not meta, f"a small photo is not scaled up and loses its metadata ({w}x{h})")
        # logo: white margins trimmed, scaled down to LOGO_MAX_PX, transparency kept, idempotent
        logo = work / "logo.png"
        im = Image.new("RGBA", (2000, 1000), (255, 255, 255, 0))
        im.paste((0, 60, 120, 255), (200, 300, 1800, 700))
        im.save(logo)
        data, _, _ = normalize_logo(logo)
        logo.write_bytes(data)
        out = Image.open(logo)
        check(out.width <= LOGO_MAX_PX[0] and out.height <= LOGO_MAX_PX[1], f"the logo fits {LOGO_MAX_PX} ({out.size})")
        check(abs(out.width / out.height - 4.0) < 0.05, f"margins are trimmed and the aspect kept ({out.size})")
        check(out.convert("RGBA").getpixel((out.width // 2, out.height // 2))[3] == 255, "the logo keeps its ink")
        check(normalize_logo(logo)[0] is None, "a normalized logo is left alone (idempotent)")
        # a small logo inside the limits is not touched
        tiny = work / "tiny.png"
        Image.new("RGBA", (300, 80), (10, 10, 10, 255)).save(tiny)
        check(normalize_logo(tiny)[0] is None, "a logo within the limits is left alone")
    print("SELF-TEST OK: photo (format, crop width, flattening, metadata, no upscaling, reference) and logo rules hold")
    return 0


def main(argv: list[str] | None = None) -> int:
    for s in (sys.stdout, sys.stderr):
        s.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="Normalize the photos and logos of the employees' CVs")
    ap.add_argument("files", nargs="*", help="images (default: cvs/*/images/photo.* and cvs/logos/*)")
    ap.add_argument("--apply", action="store_true", help="change the files (default: dry run)")
    ap.add_argument("--self-test", action="store_true", help="check the rules on synthetic images and exit")
    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()

    files = [Path(f).resolve() for f in args.files] or default_files()
    before = after = changed = flagged = 0
    for p in files:
        is_photo = p.parent.name == "images" and p.stem == "photo"
        data, target, why = (normalize_photo if is_photo else normalize_logo)(p)
        size = p.stat().st_size
        before += size
        rel = p.relative_to(ROOT).as_posix() if p.is_relative_to(ROOT) else str(p)
        if data is None:
            after += size
            print(f"  ok      {rel}")
            continue
        changed += 1
        after += len(data)
        share = len(data) / size
        flag = share < FLAG_SHARE
        flagged += flag
        print(f"{'  FLAG' if flag else '      '}  {rel}: {size // 1024} KB -> {len(data) // 1024} KB "
              f"({share:.0%}); {why}" + (f"; -> {target.name}" if target != p else ""))
        if args.apply:
            target.write_bytes(data)
            if target != p:
                if not update_reference(p, target):
                    print(f"        WARNING: no reference to images/{p.name} found in the CV; update it by hand")
                p.unlink()
    verb = "changed" if args.apply else "would change"
    print(f"\n{len(files)} files, {changed} {verb}, {flagged} flagged (< {FLAG_SHARE:.0%} of the size); "
          f"{before / 1048576:.1f} MB -> {after / 1048576:.1f} MB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
