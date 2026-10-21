#!/usr/bin/env python3
"""Draw the lesson figures (img/svg/fig-*.svg): antenna shapes, mouthparts,
leg parts, leg types, wing types and abdomen tips.

    python3 tools/make-figures.py

Schematic drawings made for this app. They carry numbers only, no words, so
one file serves all three languages: the figure caption explains each number,
in the same order as the list on the page. A light card behind each drawing
keeps it readable in dark themes."""
from math import cos, sin, pi
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "img" / "svg"
INK, FILL, SOFT, ACC, CARD = "#3d4654", "#c9a46a", "#e9dcc2", "#b5523b", "#faf6ee"
CELL = 170


def svg(cols, rows, body, cell=CELL):
    w, h = cols * cell, rows * cell
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'font-family="sans-serif" stroke-linecap="round" stroke-linejoin="round">'
            f'<rect width="{w}" height="{h}" rx="14" fill="{CARD}"/>{body}</svg>')


def num(n, x, y):
    return (f'<circle cx="{x}" cy="{y}" r="12" fill="{ACC}"/>'
            f'<text x="{x}" y="{y + 5}" font-size="15" font-weight="700" fill="#fff" text-anchor="middle">{n}</text>')


def cell(i, cols, draw):
    x, y = (i % cols) * CELL, (i // cols) * CELL
    return f'<g transform="translate({x},{y})">{draw}{num(i + 1, 18, 18)}</g>'


def line(x1, y1, x2, y2, w=3, c=INK):
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{c}" stroke-width="{w}"/>'


def ell(cx, cy, rx, ry, fill=FILL, w=2.5, rot=0):
    return (f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="{fill}" stroke="{INK}" '
            f'stroke-width="{w}" transform="rotate({rot} {cx:.1f} {cy:.1f})"/>')


def path(d, fill="none", w=3):
    return f'<path d="{d}" fill="{fill}" stroke="{INK}" stroke-width="{w}"/>'


HEAD = ell(85, 150, 26, 14, SOFT)


# ---------------------------------------------------------------- antennae
def antennae():
    out = []
    # 1 filiform: equal small segments
    out.append(HEAD + "".join(ell(85, 132 - k * 9.5, 3.2, 4.6) for k in range(12)))
    # 2 moniliform: beads
    out.append(HEAD + "".join(f'<circle cx="85" cy="{132 - k * 11}" r="5.5" fill="{FILL}" stroke="{INK}" stroke-width="2.5"/>' for k in range(10)))
    # 3 geniculate: long scape, then an elbow
    g = HEAD + path("M85 138 L85 78", w=6)
    g += "".join(ell(85 + k * 7.5, 74 - k * 4.3, 3.2, 4.2, rot=60) for k in range(9))
    out.append(g)
    # 4 clavate: thickening towards the tip
    out.append(HEAD + "".join(ell(85, 134 - k * 10, 2.5 + k * 0.75, 4.6) for k in range(11)))
    # 5 serrate: teeth on one side
    s = HEAD
    for k in range(10):
        y = 134 - k * 10
        s += path(f"M82 {y + 5} L82 {y - 5} L94 {y - 2} Z", FILL, 2.2)
    out.append(s)
    # 6 pectinate / plumose: long side branches
    p = HEAD + line(85, 140, 85, 32, 3)
    for k in range(11):
        y = 132 - k * 9.5
        L = 22 - abs(k - 4) * 2
        p += line(85, y, 85 - L, y - 10, 1.8) + line(85, y, 85 + L, y - 10, 1.8)
    out.append(p)
    # 7 lamellate: short stalk ending in fanned plates
    l = HEAD + "".join(ell(85, 134 - k * 9, 3, 4.2) for k in range(6))
    for a in (-35, 0, 35):
        l += ell(85 + 22 * sin(a * pi / 180), 72 - 22 * cos(a * pi / 180), 6, 20, FILL, rot=a)
    out.append(l)
    return svg(4, 2, "".join(cell(i, 4, d) for i, d in enumerate(out)))


# ---------------------------------------------------------------- mouthparts
def mouthparts():
    out = []
    head = ell(85, 70, 34, 30, SOFT) + f'<circle cx="64" cy="62" r="7" fill="{INK}"/><circle cx="106" cy="62" r="7" fill="{INK}"/>'
    # 1 chewing: toothed mandibles
    m = head + path("M70 96 Q60 120 84 128 L80 118 L74 116 L78 108 Z", FILL, 2.5)
    m += path("M100 96 Q110 120 86 128 L90 118 L96 116 L92 108 Z", FILL, 2.5)
    out.append(m)
    # 2 chewing-lapping: mandibles plus a long tongue
    m = head + path("M70 96 Q62 112 78 118", FILL, 2.5) + path("M100 96 Q108 112 92 118", FILL, 2.5)
    m += path("M85 98 L85 150", w=7) + ell(85, 152, 5, 6, FILL)
    out.append(m)
    # 3 sponging: proboscis ending in a pad
    m = head + path("M85 98 L85 132", w=8) + ell(85, 140, 22, 10, FILL)
    out.append(m)
    # 4 siphoning: coiled tube
    coil = "M85 98 " + " ".join(
        f"L{85 + (16 - t * 1.6) * sin(t):.1f} {124 - (16 - t * 1.6) * cos(t):.1f}" for t in [k * 0.25 for k in range(0, 40)])
    out.append(head + path(coil, w=3.5))
    # 5 piercing-sucking: beak folded under the head (side view)
    side = ell(70, 70, 34, 26, SOFT) + f'<circle cx="52" cy="62" r="7" fill="{INK}"/>'
    side += path("M48 90 L60 150", w=6) + line(60, 150, 63, 158, 2)
    out.append(side)
    return svg(3, 2, "".join(cell(i, 3, d) for i, d in enumerate(out)))


# ---------------------------------------------------------------- one leg, six parts
def leg():
    body = ell(70, 70, 60, 34, SOFT)
    parts = [
        ell(120, 92, 16, 11, FILL, rot=30),                                   # coxa
        ell(140, 106, 9, 7, FILL, rot=30),                                    # trochanter
        ell(205, 112, 62, 14, FILL, rot=-8),                                  # femur
        path("M262 106 L330 182", w=7) + "".join(line(270 + k * 12, 118 + k * 13, 278 + k * 12, 114 + k * 13, 2) for k in range(5)),  # tibia
        "".join(ell(338 + k * 13, 188 + k * 2, 6, 4.5, FILL) for k in range(5)),  # tarsus
        path("M400 198 Q412 196 412 208", w=2.5) + path("M400 198 Q410 206 404 214", w=2.5),  # pretarsus claws
    ]
    labels = [(120, 50), (150, 140), (205, 72), (318, 130), (366, 160), (420, 224)]
    marks = "".join(num(i + 1, x, y) for i, (x, y) in enumerate(labels))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 250" width="460" height="250" font-family="sans-serif" '
            f'stroke-linecap="round" stroke-linejoin="round"><rect width="460" height="250" rx="14" fill="{CARD}"/>'
            f'{body}{"".join(parts)}{marks}</svg>')


# ---------------------------------------------------------------- leg types
def legtypes():
    out = []
    # 1 walking / running: slender, similar parts
    out.append(ell(70, 70, 22, 6, FILL, rot=40) + path("M86 84 L120 140", w=4) + path("M120 140 L150 146", w=3))
    # 2 jumping: huge femur
    out.append(ell(78, 74, 44, 15, FILL, rot=-30) + path("M116 50 L82 140", w=4) + path("M82 140 L112 148", w=3))
    # 3 grasping: spiny femur and tibia that fold shut
    g = ell(80, 72, 40, 11, FILL, rot=30) + path("M114 92 L62 118", w=5)
    g += "".join(line(56 + k * 14, 58 + k * 8, 52 + k * 14, 70 + k * 8, 2.2) for k in range(4))
    g += "".join(line(70 + k * 12, 113 - k * 6, 74 + k * 12, 103 - k * 6, 2.2) for k in range(4))
    out.append(g)
    # 4 digging: broad flat tibia with teeth
    d = ell(70, 62, 30, 13, FILL, rot=20) + path("M92 76 L140 96 L132 122 L84 100 Z", FILL, 2.5)
    d += "".join(path(f"M{136 - k * 12} {104 + k * 4} L{150 - k * 12} {130 + k * 3} L{128 - k * 12} {116 + k * 4} Z", FILL, 2) for k in range(3))
    out.append(d)
    # 5 swimming: flattened leg fringed with hairs
    s = ell(70, 70, 26, 8, FILL, rot=30) + path("M90 84 Q120 110 150 120", w=8)
    s += "".join(line(94 + k * 8, 92 + k * 4.2, 90 + k * 8, 108 + k * 4.2, 1.5) for k in range(8))
    out.append(s)
    return svg(3, 2, "".join(cell(i, 3, d) for i, d in enumerate(out)))


# ---------------------------------------------------------------- wing types
def wings():
    out = []
    # 1 elytra: beetle from above, hard covers meeting in a straight line
    e = ell(85, 40, 14, 10, SOFT) + path("M58 52 Q52 110 85 150 Q118 110 112 52 Z", FILL, 3) + line(85, 52, 85, 150, 3)
    out.append(e)
    # 2 hemelytra: hard base, clear membranous tip
    h = path("M40 60 L120 50 L130 80 L60 92 Z", FILL, 3) + path("M120 50 Q160 70 130 80", SOFT, 3)
    h += line(126, 62, 148, 68, 1.5) + line(128, 72, 146 , 74, 1.5)
    out.append(h)
    # 3 tegmina: long, narrow, leathery
    t = path("M30 90 Q90 70 150 78 Q100 98 30 100 Z", "#b9a47a", 3) + "".join(line(40 + k * 20, 92, 60 + k * 20, 84, 1.5) for k in range(5))
    out.append(t)
    # 4 scaly: overlapping coloured scales
    wing = "M30 60 Q90 30 150 60 Q120 130 40 120 Z"
    sc = f'<clipPath id="scaly"><path d="{wing}"/></clipPath>' + path(wing, SOFT, 3) + '<g clip-path="url(#scaly)">'
    for r in range(8):
        for c in range(10):
            sc += f'<path d="M{24 + c * 14 + (r % 2) * 7} {44 + r * 11} q7 9 14 0" fill="{ACC if (r + c) % 3 == 0 else FILL}" stroke="{INK}" stroke-width="1.2"/>'
    sc += '</g>' + path(wing, "none", 3)
    out.append(sc)
    # 5 membranous: clear wing with a net of veins
    m = path("M30 80 Q90 46 150 70 Q110 112 30 92 Z", "#eef3f6", 3)
    m += "".join(line(40 + k * 18, 78 - k * 2, 52 + k * 18, 96 - k * 2, 1.3) for k in range(6)) + line(32, 84, 146, 72, 1.3)
    out.append(m)
    # 6 halteres: a fly from above, one pair of wings and two knobs
    f = ell(85, 92, 12, 34, SOFT) + ell(85, 52, 12, 10, SOFT)
    f += path("M75 70 Q30 64 26 100 Q50 102 76 82", "#eef3f6", 2.5) + path("M95 70 Q140 64 144 100 Q120 102 94 82", "#eef3f6", 2.5)
    f += line(76, 86, 64, 96, 2) + f'<circle cx="62" cy="98" r="5" fill="{ACC}" stroke="{INK}" stroke-width="2"/>'
    f += line(94, 86, 106, 96, 2) + f'<circle cx="108" cy="98" r="5" fill="{ACC}" stroke="{INK}" stroke-width="2"/>'
    out.append(f)
    return svg(3, 2, "".join(cell(i, 3, d) for i, d in enumerate(out)))


# ---------------------------------------------------------------- abdomen tips
def tips():
    out = []
    abd = ell(70, 85, 52, 16, SOFT)
    # 1 ovipositor: long blade
    out.append(abd + path("M120 84 Q150 70 162 44", w=5))
    # 2 cerci: a pair of slender feelers
    out.append(abd + path("M120 80 Q145 70 160 60", w=2.5) + path("M120 90 Q145 100 160 110", w=2.5))
    # 3 forceps: pincers
    out.append(abd + path("M118 78 Q150 66 152 90", w=5) + path("M118 92 Q150 104 152 80", w=5))
    # 4 sting
    out.append(abd + path("M120 80 L150 85 L120 90 Z", ACC, 2.5))
    # 5 claspers: dragonfly male
    out.append(abd + path("M120 80 Q140 74 148 84 Q140 82 128 84", FILL, 2.5) + path("M120 90 Q138 96 140 104", w=3))
    return svg(3, 2, "".join(cell(i, 3, d) for i, d in enumerate(out)))


FIGS = {"fig-antennae.svg": antennae, "fig-mouthparts.svg": mouthparts, "fig-leg.svg": leg,
        "fig-legtypes.svg": legtypes, "fig-wings.svg": wings, "fig-abdomen-tips.svg": tips}

if __name__ == "__main__":
    for name, fn in FIGS.items():
        (OUT / name).write_text(fn())
        print("wrote", name)
