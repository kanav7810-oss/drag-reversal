"""Parametric riblet-wall geometry -> STL for OpenFOAM snappyHexMesh.

Extrudes a V-groove or blade cross-section (same definitions as
fabrication/riblet_plate.scad) along the spanwise direction, producing a
periodic lower wall patch sized for a minimal-span channel.

Usage:
    python make_snake_stl.py --shape v --s 0.5 --h 0.25 \
        --length 90 --span 12 --out v_s500.stl
(length/span/s/h in mm; scale to wall units in the case setup)
"""
import argparse
import struct


def cross_section(shape, s, h):
    if shape == "v":
        return [(-s / 2, 0.0), (s / 2, 0.0), (0.0, h)]
    tip = min(0.05 * s, 0.05 * h)
    base = tip + 2 * h * 0.0699  # tan(4 deg)
    return [(-base / 2, 0.0), (base / 2, 0.0),
            (tip / 2, h), (-tip / 2, h)]


def write_stl(path, triangles):
    with open(path, "wb") as f:
        f.write(b"\x00" * 80)
        f.write(struct.pack("<I", len(triangles)))
        for tri in triangles:
            normal = (0.0, 0.0, 0.0)
            f.write(struct.pack("<3f", *normal))
            for p in tri:
                f.write(struct.pack("<3f", *p))
            f.write(struct.pack("<H", 0))


def build(shape, s, h, length, span, pitch):
    pts = cross_section(shape, s, h)
    tris = []
    n = len(pts)
    z0, z1 = 0.0, span
    x_end = length
    # base slab from y=-(slab) up to y=0 of each tooth, then teeth, tiled
    slab_top = [(x, 0.0) for x, _ in pts]
    xs = [x for x, _ in pts]
    xmin, xmax = min(xs) - s, max(xs) + s
    positions = []
    x = -s
    while x < x_end + s:
        positions.append(x)
        x += pitch
    for cx in positions:
        poly = [(cx + px, py) for px, py in pts]
        for i in range(1, n - 1):
            tris.append([(poly[0][0], poly[0][1], z0),
                         (poly[i][0], poly[i][1], z0),
                         (poly[i + 1][0], poly[i + 1][1], z0)])
            tris.append([(poly[0][0], poly[0][1], z1),
                         (poly[i + 1][0], poly[i + 1][1], z1),
                         (poly[i][0], poly[i][1], z1)])
        loop = poly + [poly[0]]
        for i in range(n):
            a, b = loop[i], loop[i + 1]
            tris.append([(a[0], a[1], z0), (b[0], b[1], z0), (b[0], b[1], z1)])
            tris.append([(a[0], a[1], z0), (b[0], b[1], z1), (a[0], a[1], z1)])
    return tris


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shape", choices=["v", "blade"], default="v")
    ap.add_argument("--s", type=float, default=0.5)
    ap.add_argument("--h", type=float, default=0.25)
    ap.add_argument("--length", type=float, default=90.0)
    ap.add_argument("--span", type=float, default=12.0)
    ap.add_argument("--pitch", type=float, default=None,
                    help="groove pitch override (default: 2*s for V)")
    ap.add_argument("--out", default="riblet_wall.stl")
    args = ap.parse_args()
    pitch = args.pitch or (args.s if args.shape == "v" else args.s)
    tris = build(args.shape, args.s, args.h, args.length, args.span, pitch)
    write_stl(args.out, tris)
    print(f"wrote {args.out}: {len(tris)} triangles "
          f"(shape={args.shape}, s={args.s} mm, h={args.h} mm)")


if __name__ == "__main__":
    main()
