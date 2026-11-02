"""Weitere Zeichnungen (SVG) für Küstenschutz: Düne, Sieltor, Deichprofile."""
import random
from geo_lib import _svg, _num, _label, _arrow


# ------------------------------------------------------------------ Düne


def _tuft(x, y, h=26, n=5, color="#4f9d3a"):
    """Büschel Strandhafer (leicht geschwungene Halme)."""
    out = []
    offs = [-10, -5, 0, 5, 10][:n]
    for i, o in enumerate(offs):
        hh = h - abs(o) * 0.7
        out.append(f'<path d="M{x + o * 0.3:.1f} {y} Q{x + o * 0.8:.1f} {y - hh * 0.6:.1f} {x + o * 1.7:.1f} {y - hh:.1f}" '
                   f'fill="none" stroke="{color}" stroke-width="2.4" stroke-linecap="round"/>')
    return ''.join(out)


def svg_duene(nummern=True):
    """Querschnitt Strand und Düne mit Strandhafer.

    1 Wind, 2 Strand, 3 Strandhafer, 4 Düne, 5 Wurzeln, 6 Meer.
    """
    W, H = 640, 340
    prof = [(0, 300), (100, 292), (210, 262), (300, 240), (350, 205), (405, 160), (445, 142), (490, 155), (545, 200), (590, 232), (640, 240)]

    def y_at(x):
        for (x1, y1), (x2, y2) in zip(prof, prof[1:]):
            if x1 <= x <= x2:
                return y1 + (y2 - y1) * (x - x1) / (x2 - x1)
        raise ValueError(x)

    g = []
    pts = ' '.join(f'{x},{y}' for x, y in prof)
    # Wasser: bis zur Höhe y=262 (Meer)
    g.append('<polygon points="0,262 210,262 100,292 0,300" fill="#bfe0f3"/>')
    g.append('<path d="M0 262 q15 -8 30 0 t30 0 t30 0 t30 0 t30 0 t30 0 t30 0" fill="none" stroke="#5aa6d1" stroke-width="2.5"/>')
    # Sand
    g.append(f'<polygon points="{pts} 640,{H} 0,{H}" fill="#ecd9a2"/>')
    g.append(f'<polyline points="{pts}" fill="none" stroke="#b99a55" stroke-width="3" stroke-linejoin="round"/>')
    # Wurzeln: verzweigtes Netz unter dem Bewuchs
    wurzeln = [(390, 165), (430, 147), (470, 148), (505, 168)]
    for (x, y) in wurzeln:
        g.append(f'<path d="M{x} {y + 6} q-6 40 -4 85 M{x} {y + 18} q-24 22 -34 50 M{x} {y + 22} q22 24 30 54 M{x - 3} {y + 50} q-14 10 -20 30" '
                 f'fill="none" stroke="#8a5a2b" stroke-width="1.8" stroke-linecap="round"/>')
    # Strandhafer
    for (x, y) in wurzeln:
        g.append(_tuft(x, y + 3))
    for x in (340, 560):
        g.append(_tuft(x, y_at(x) + 3, h=20, n=3))
    # Windpfeile
    ys = (205, 232)
    for y in ys:
        g.append(_arrow(205, y, 312, y - 8, "#555", 2.4))
    # Beschriftung
    if nummern:
        pos = {
            1: ((255, 190), None),
            2: ((250, 285), (250, 258)),
            3: ((385, 112), (392, 152)),
            4: ((445, 100), None),
            5: ((350, 300), (385, 232)),
            6: ((60, 232), None),
        }
        for n, (p, z) in pos.items():
            if z:
                g.append(f'<line x1="{p[0]}" y1="{p[1]}" x2="{z[0]}" y2="{z[1]}" stroke="#333" stroke-width="1.4"/>')
            g.append(_num(p[0], p[1], n))
    else:
        g.append(_label(255, 172, "Wind", weight="bold", size=20))
        g.append(_label(250, 294, "Strand", weight="bold", size=20))
        g.append(_label(60, 232, "Meer", weight="bold", size=20, fill="#1f5f8f"))
        g.append(f'<line x1="352" y1="112" x2="388" y2="150" stroke="#333" stroke-width="1.4"/>')
        g.append(_label(330, 104, "Strandhafer", weight="bold", size=20))
        g.append(_label(540, 120, "Düne", weight="bold", size=22))
        g.append(f'<line x1="372" y1="300" x2="385" y2="232" stroke="#333" stroke-width="1.4"/>')
        g.append(_label(372, 322, "Wurzeln", weight="bold", size=20))
    return _svg(W, H, ''.join(g))


# ------------------------------------------------------------------ Sieltor


def _siel_panel(zustand, x0, nummern, titel=None):
    """Ein Bild: Meer links, Deich (Schema) mit Siel in der Mitte, Land (Marsch) rechts. Breite 380, Höhe 330."""
    assert zustand in ("ebbe", "flut")
    g = []
    wall_l, wall_r = x0 + 160, x0 + 220
    boden = 300
    meer = 270 if zustand == "ebbe" else 140
    land = 238
    # Meer
    g.append(f'<rect x="{x0}" y="{meer}" width="{wall_l - x0}" height="{boden - meer}" fill="#bfe0f3"/>')
    g.append(f'<line x1="{x0}" y1="{meer}" x2="{wall_l}" y2="{meer}" stroke="#5aa6d1" stroke-width="2.5"/>')
    # Land (Wasser im Hinterland)
    g.append(f'<rect x="{wall_r}" y="{land}" width="{x0 + 380 - wall_r}" height="{boden - land}" fill="#d6edf9"/>')
    g.append(f'<line x1="{wall_r}" y1="{land}" x2="{x0 + 380}" y2="{land}" stroke="#7bb9dc" stroke-width="2" stroke-dasharray="6 4"/>')
    # Boden
    g.append(f'<rect x="{x0}" y="{boden}" width="380" height="30" fill="#c9ad7a"/>')
    # Deich (Schema) mit Durchlass
    g.append(f'<rect x="{wall_l}" y="60" width="{wall_r - wall_l}" height="{boden - 60}" fill="#9a6b43"/>')
    g.append(f'<rect x="{wall_l}" y="56" width="{wall_r - wall_l}" height="10" fill="#4f9d3a"/>')
    durch_o, durch_u = 225, boden
    g.append(f'<rect x="{wall_l}" y="{durch_o}" width="{wall_r - wall_l}" height="{durch_u - durch_o}" fill="#d6edf9"/>')
    # Wasser im Durchlass nur bei Ebbe (es fließt ab)
    if zustand == "ebbe":
        g.append(f'<rect x="{wall_l}" y="{land + 4}" width="{wall_r - wall_l}" height="{durch_u - land - 4}" fill="#aed6ee"/>')
    # Tor: oben befestigt, an der Meerseite
    if zustand == "flut":
        g.append(f'<line x1="{wall_l}" y1="{durch_o}" x2="{wall_l}" y2="{durch_u}" stroke="#222" stroke-width="7" stroke-linecap="round"/>')
    else:
        g.append(f'<line x1="{wall_l}" y1="{durch_o}" x2="{wall_l - 38}" y2="{durch_u - 14}" stroke="#222" stroke-width="7" stroke-linecap="round"/>')
    g.append(f'<circle cx="{wall_l}" cy="{durch_o}" r="5" fill="#fff" stroke="#222" stroke-width="2"/>')
    # Pfeile
    if zustand == "ebbe":
        g.append(_arrow(wall_r + 60, 262, wall_l - 55, 262, "#1f78b4", 3.5))
    else:
        g.append(_arrow(x0 + 30, 200, wall_l - 8, 200, "#1f78b4", 3.5))
        g.append(_arrow(x0 + 30, 160, wall_l - 8, 160, "#1f78b4", 3.5))
    # Beschriftung
    if nummern:
        g.append(_num(x0 + 70, 300 - 22 if zustand == 'flut' else 296 - 14, 1))
        g.append(_num((wall_l + wall_r) / 2, 105, 2))
        g.append(_num(wall_l - 24 if zustand == "ebbe" else wall_l - 24, 262 if zustand == "flut" else 206, 3))
        g.append(_num(x0 + 320, 290 - 10, 4))
    else:
        g.append(_label(x0 + 70, 128 if zustand == "flut" else 236, "Meer", weight="bold", size=21, fill="#1f5f8f"))
        g.append(_label((wall_l + wall_r) / 2, 108, "Deich", weight="bold", size=19, fill="#fff"))
        g.append(_label(x0 + 300, 292, "Land (Marsch)", weight="bold", size=17, fill="#6b5535"))
        if zustand == "ebbe":
            g.append(_label(wall_l - 46, durch_o - 12, "Tor", weight="bold", size=21))
        else:
            g.append(_label(wall_l - 24, 268, "Tor", weight="bold", size=21))
    if titel:
        g.append(_label(x0 + 190, 36, titel, weight="bold", size=26))
    return ''.join(g)


def svg_siel(zustand, nummern=False, titel=None):
    return _svg(380, 330, _siel_panel(zustand, 0, nummern, titel))


def svg_siel_paar(ebbe_links=True, kopf=("Zeichnung A", "Zeichnung B")):
    """Zwei Zeichnungen nebeneinander (Ebbe und Flut). kopf: Überschriften links und rechts."""
    z1, z2 = ("ebbe", "flut") if ebbe_links else ("flut", "ebbe")
    inner = _siel_panel(z1, 0, False, kopf[0]) + _siel_panel(z2, 400, False, kopf[1])
    inner += '<line x1="390" y1="20" x2="390" y2="320" stroke="#bbb" stroke-width="1.5"/>'
    return _svg(780, 330, inner)


# ------------------------------------------------------------------ Deichprofile (Buch S. 128, M2)


def svg_deichprofile(werte=True):
    """Drei Deichprofile nebeneinander: 1599 (etwa 3 m), 1766 (etwa 5,1 m), heute (etwa 8,8 m). Breiten nicht maßstäblich."""
    W, H = 800, 360
    base_y = 310
    m = 28  # Pixel pro Meter
    g = []
    # Achse
    g.append(f'<line x1="56" y1="{base_y}" x2="56" y2="{base_y - 10 * m}" stroke="#444" stroke-width="2"/>')
    for k in range(0, 11, 2):
        y = base_y - k * m
        g.append(f'<line x1="50" y1="{y}" x2="62" y2="{y}" stroke="#444" stroke-width="2"/>')
        g.append(_label(44, y + 5, str(k), anchor="end", size=14))
        g.append(f'<line x1="62" y1="{y}" x2="790" y2="{y}" stroke="#e5e5e5" stroke-width="1"/>')
    g.append(_label(70, 16, "Höhe in m", anchor="start", size=13))
    g.append(f'<line x1="56" y1="{base_y}" x2="790" y2="{base_y}" stroke="#444" stroke-width="2"/>')
    profile = [("1599", 3.0, 190, 120, 18, "etwa 3 m"), ("1766", 5.1, 395, 190, 24, "etwa 5,1 m"), ("heute", 8.8, 630, 270, 30, "etwa 8,8 m")]
    for name, h, cx, base, kron, txt in profile:
        top = base_y - h * m
        pts = f'{cx - base / 2},{base_y} {cx - kron / 2},{top} {cx + kron / 2},{top} {cx + base / 2},{base_y}'
        g.append(f'<polygon points="{pts}" fill="#d8b97c" stroke="#8a6a34" stroke-width="2"/>')
        g.append(f'<polyline points="{cx - base / 2},{base_y} {cx - kron / 2},{top} {cx + kron / 2},{top} {cx + base / 2},{base_y}" fill="none" stroke="#4f9d3a" stroke-width="7" stroke-linejoin="round"/>')
        g.append(_label(cx, base_y + 28, name, weight="bold", size=17))
        if werte:
            g.append(f'<line x1="{cx - base / 2 - 14}" y1="{top}" x2="{cx - kron / 2}" y2="{top}" stroke="#c0392b" stroke-width="1.6" stroke-dasharray="5 4"/>')
            g.append(_label(cx - base / 2 - 14, top - 7, txt, anchor="start" if False else "middle", size=13, weight="bold", fill="#c0392b"))
    return _svg(W, H, ''.join(g))
