# /// script
# requires-python = ">=3.10"
# dependencies = ["pymupdf", "pillow"]
# ///
"""KodeWorks seismograph strip generator (the identity's "fifth element").

Produces transparent PNG (300 dpi at the requested physical size) and optional SVG
strips built only from straight line segments: a few THICK segments (high activity)
and many THIN ones (low activity), thick:thin = 13:3, joined in a zigzag.

Usage:
  uv run seismograph.py --width-mm 170 --height-mm 6 --variant band \
      --colour B6FF9E --out band.png [--svg band.svg] [--seed 3] [--dpi 300]

Variants (the geometry is deterministic for a given --seed):
  band        full-width thick rule along the TOP edge, thin trace falling from it
              (section start / top of frame)
  band-up     the same mirrored: thick rule along the BOTTOM edge (header line)
  closing     thin diagonal falling to a thick horizontal and a short vertical stub
              (end of document; closes the zigzag)
  corner      thick L (bottom + right edge) with a thin trace leaving the corner
  vleft       vertical strip, thick rule along the LEFT edge (margin strip)
  vright      vertical strip, thick rule along the RIGHT edge

Options:
  --thick-mm  thick stroke width (default 1.06 mm = 3 pt, same as the CV's left
              border); thin = thick * 3/13 unless --thin-mm is given.
  --margin-mm clear padding kept inside the image so strokes are never clipped.
  --thin-colour  separate colour for the thin strokes (e.g. 000000 with green thick strokes).

Rules: strokes use butt caps (flat ends like the identity files); the colour is a
parameter, so the same strips can be reused for other templates (card, letter) or in
black. Import as a module: `render(variant, w_mm, h_mm, colour, seed, ...)` returns
(svg_text, segments).
"""
import argparse
import re
import random
from pathlib import Path

VARIANTS = ("band", "band-up", "closing", "corner", "vleft", "vright")


class Seg:
    """A straight segment (x1,y1)-(x2,y2) in mm with a stroke width in mm."""
    def __init__(self, x1, y1, x2, y2, w):
        self.x1, self.y1, self.x2, self.y2, self.w = x1, y1, x2, y2, w


def _trace(L, D, thick, thin, rng):
    """Core pattern in a local frame: l along the strip (0..L), d depth (0..D, 0 = rule).

    The rule is a thick line at d = thick/2. A long thin diagonal runs from the right
    end of the rule down to the lower left; from there the trace zigzags back with
    shrinking amplitude, with one short thick step - the character of the funnel in
    the fifth-element motifs. Returns segments as (l1, d1, l2, d2, width).
    """
    segs = [(0, thick / 2, L, thick / 2, thick)]
    lo = D - thin / 2  # lowest d the trace may use
    hi = thick + thin  # just under the rule
    a = (L * rng.uniform(0.80, 0.93), thick / 2)
    b = (L * rng.uniform(0.02, 0.07), lo - (lo - hi) * rng.uniform(0.0, 0.15))
    pts = [a, b]
    # funnel: alternate right/left, shrinking, depth stepping up
    x_l, x_r = b[0], a[0] - L * rng.uniform(0.15, 0.30)
    d = lo
    n = 1 if D < 10 else rng.randint(3, 4)  # shallow strips: calm, one return only
    for i in range(n):
        d = hi + (lo - hi) * (1 - (i + 1) / (n + 1)) * rng.uniform(0.7, 1.0)
        if i % 2 == 0:
            pts.append((x_r, d))
            x_r -= (x_r - x_l) * rng.uniform(0.25, 0.4)
        else:
            pts.append((x_l, d))
            x_l += (x_r - x_l) * rng.uniform(0.25, 0.4)
    for (p, q) in zip(pts, pts[1:]):
        segs.append((p[0], p[1], q[0], q[1], thin))
    # one short thick step (high activity) near the lower right, horizontal
    sl = L * rng.uniform(0.05, 0.08)
    sx = L * rng.uniform(0.55, 0.70)
    sd = D - thick / 2
    segs.append((sx, sd, sx + sl, sd, thick))
    segs.append((sx + sl, sd, sx + sl, sd - (sd - hi) * rng.uniform(0.35, 0.6), thin))
    return segs


def _map(segs, variant, W, H):
    out = []
    for l1, d1, l2, d2, w in segs:
        if variant == "band":
            out.append(Seg(l1, d1, l2, d2, w))
        elif variant == "band-up":
            out.append(Seg(l1, H - d1, l2, H - d2, w))
        elif variant == "vleft":
            out.append(Seg(d1, l1, d2, l2, w))
        elif variant == "vright":
            out.append(Seg(W - d1, l1, W - d2, l2, w))
    return out


def build(variant, W, H, seed, thick, thin, margin):
    if variant not in VARIANTS:
        raise SystemExit(f"unknown variant {variant}; choose from {VARIANTS}")
    rng = random.Random(seed)
    if variant in ("band", "band-up"):
        return _map(_trace(W, H, thick, thin, rng), variant, W, H)
    if variant in ("vleft", "vright"):
        return _map(_trace(H, W, thick, thin, rng), variant, W, H)
    if variant == "closing":
        ty = H * rng.uniform(0.74, 0.80)          # y of the thick horizontal
        tx2 = W * rng.uniform(0.62, 0.72)         # its right end
        s = [Seg(0, ty, tx2, ty, thick)]          # thick horizontal
        s.append(Seg(thick / 2, ty - thick / 2, thick / 2, H - thin / 2, thin))  # stub down
        top = (W * rng.uniform(0.03, 0.08), thin / 2 + H * 0.02)
        s.append(Seg(top[0], top[1], tx2, ty, thin))  # long diagonal falling to the rule
        s.append(Seg(tx2, ty, W - thin, ty - H * rng.uniform(0.10, 0.16), thin))  # tail up
        # short thick step on the diagonal's way in (high activity)
        t = rng.uniform(0.55, 0.7)
        px, py = top[0] + (tx2 - top[0]) * t, top[1] + (ty - top[1]) * t
        qx, qy = top[0] + (tx2 - top[0]) * (t + 0.07), top[1] + (ty - top[1]) * (t + 0.07)
        s.append(Seg(px, py, qx, qy, thick))
        return s
    # corner: thick L along bottom and right, thin trace leaving the inside corner
    s = [Seg(0, H - thick / 2, W, H - thick / 2, thick),
         Seg(W - thick / 2, 0, W - thick / 2, H, thick)]
    cx, cy = W - thick, H - thick
    p1 = (W * rng.uniform(0.15, 0.3), H * rng.uniform(0.05, 0.2))
    p2 = (W * rng.uniform(0.45, 0.6), cy - H * rng.uniform(0.0, 0.1))
    p3 = (W * rng.uniform(0.7, 0.8), H * rng.uniform(0.1, 0.3))
    pts = [(cx, cy), p2, p1, p3, (cx, p3[1] + H * 0.1)]
    for a, b in zip(pts, pts[1:]):
        s.append(Seg(a[0], a[1], b[0], b[1], thin))
    return s


def to_svg(segs, W, H, colour, thin_colour=None, thin_mm=None):
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H}mm" '
           f'viewBox="0 0 {W} {H}">']
    for g in segs:
        out.append(f'<line x1="{g.x1:.3f}" y1="{g.y1:.3f}" x2="{g.x2:.3f}" y2="{g.y2:.3f}" '
                   f'stroke="#{thin_colour if (thin_colour and g.w <= thin_mm * 1.5) else colour}" stroke-width="{g.w:.3f}" stroke-linecap="butt"/>')
    out.append("</svg>")
    return "\n".join(out)


def render(variant, w_mm, h_mm, colour="B6FF9E", seed=1, thick_mm=1.06, thin_mm=None,
           margin_mm=0.0, thin_colour=None):
    thin = thin_mm if thin_mm else thick_mm * 3 / 13
    segs = build(variant, w_mm, h_mm, seed, thick_mm, thin, margin_mm)
    return to_svg(segs, w_mm, h_mm, colour, thin_colour, thin), segs


def svg_to_png(svg_text, w_mm, h_mm, dpi, out):
    """Rasterise the SVG to a transparent RGBA PNG at `dpi`.

    Every distinct stroke colour is rendered as its own alpha mask and painted in its exact
    colour, so antialiased edges never pick up a grey fringe and thick/thin may differ in colour.
    """
    import pymupdf
    from PIL import Image
    head = svg_text.split(">", 1)[0] + ">"
    lines = re.findall(r"<line [^>]*/>", svg_text)
    colours = sorted({re.search(r'stroke="#([0-9A-Fa-f]{6})"', l).group(1) for l in lines})
    result = None
    for col in colours:
        body = "\n".join(l for l in lines if f'stroke="#{col}"' in l)
        doc = pymupdf.open(stream=(head + body + "</svg>").encode("utf8"), filetype="svg")
        page = doc[0]
        zoom = dpi / 72 * (w_mm / 25.4 * 72) / page.rect.width
        pix = page.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom), alpha=True)
        mask = Image.frombytes("RGBA", (pix.width, pix.height), pix.samples).getchannel("A")
        layer = Image.new("RGBA", mask.size, tuple(int(col[k:k + 2], 16) for k in (0, 2, 4)) + (255,))
        layer.putalpha(mask)
        if result is None:
            result = Image.new("RGBA", mask.size, (0, 0, 0, 0))
        result.alpha_composite(layer)
    result.save(out, dpi=(dpi, dpi))
    return result.width, result.height


def main():
    ap = argparse.ArgumentParser(description="KodeWorks seismograph strip generator")
    ap.add_argument("--width-mm", type=float, required=True)
    ap.add_argument("--height-mm", type=float, required=True)
    ap.add_argument("--variant", choices=VARIANTS, default="band")
    ap.add_argument("--colour", default="B6FF9E", help="hex RGB without #")
    ap.add_argument("--out", required=True, help="PNG output (transparent, --dpi)")
    ap.add_argument("--thin-colour", default=None,
                    help="hex RGB for the thin strokes (default: same as --colour); the identity "
                         "uses green thick + black thin where green alone is too faint")
    ap.add_argument("--svg", default=None, help="optional SVG output")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--dpi", type=int, default=300)
    ap.add_argument("--thick-mm", type=float, default=1.06)
    ap.add_argument("--thin-mm", type=float, default=None)
    ap.add_argument("--margin-mm", type=float, default=0.0)
    a = ap.parse_args()
    svg, _ = render(a.variant, a.width_mm, a.height_mm, a.colour.lstrip("#"), a.seed,
                    a.thick_mm, a.thin_mm, a.margin_mm,
                    a.thin_colour.lstrip('#') if a.thin_colour else None)
    if a.svg:
        Path(a.svg).write_text(svg, encoding="utf8")
    w, h = svg_to_png(svg, a.width_mm, a.height_mm, a.dpi, a.out)
    print(f"{a.out}: {w}x{h}px, {a.variant}, seed {a.seed}")


if __name__ == "__main__":
    main()
