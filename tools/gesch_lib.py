"""Hilfen für die Geschichte-Lernpakete (Klasse 6, Steinzeit): Pakete, Prüfungen und Zeichnungen (SVG).

Baut auf geo_lib.py auf (Aufgaben-Bausteine mc, tf, kurz, luecke, zuordnen, reihenfolge, frei, lb).
Alle Jahreszahlen, Rechnungen und Positionen werden im Code berechnet und mit assert geprüft.
Datenschutz: Das Repository ist öffentlich. Der Stammbaum und alle Beispiele sind erfunden, keine echten Familiendaten.
"""
import math
import re

from geo_lib import *                      # noqa: F401,F403  (mc, tf, kurz, luecke, zuordnen, reihenfolge, frei, lb, de, svg_tabelle ...)
from geo_lib import _svg, _num, _label, _arrow, _gaps   # noqa: F401

FACH = "Geschichte"


def pack(id, titel, beschreibung, lernblatt, aufgaben, hinweis=None, min_aufgaben=None, info_pflicht=True):
    """Wie geo_lib.pack, aber Fach Geschichte. Jede Aufgabe außer frei braucht ein info (Regel vom 04.11.2026)."""
    if min_aufgaben:
        assert len(aufgaben) >= min_aufgaben, f"{id}: nur {len(aufgaben)} Aufgaben (Ziel {min_aufgaben})"
    if info_pflicht:
        for i, t in enumerate(aufgaben, 1):
            if t["typ"] != "frei":
                assert t.get("info", "").strip(), f"{id} Aufgabe {i}: info fehlt ({t['frage'][:50]})"
    p = {"typ": "lernpaket", "version": 1, "person": ["joel", "dario"], "id": id, "titel": titel,
         "fach": FACH, "klasse": "6", "beschreibung": beschreibung}
    if hinweis:
        p["hinweis"] = hinweis
    if lernblatt:
        p["lernblatt"] = lernblatt
    p["aufgaben"] = aufgaben
    p = _normalisiere(p)
    check_pack(p)
    return p


_LISTE = re.compile(r"^\s*[-•]\s+")


def _text_normal(s):
    """Listenzeilen brauchen in der App einen eigenen Absatz (Leerzeile davor und danach); zwei Punkte hintereinander werden zu einem."""
    if "\n" in s:
        out, vorher = [], None   # vorher: war die letzte nichtleere Zeile eine Listenzeile?
        for z in s.split("\n"):
            if z.strip() == "":
                vorher = None
                out.append(z)
                continue
            ist = bool(_LISTE.match(z))
            if vorher is not None and ist != vorher and out and out[-1].strip() != "":
                out.append("")
            out.append(z)
            vorher = ist
        s = "\n".join(out)
    return re.sub(r"(?<!\.)\.\.(?!\.)", ".", s)


def _normalisiere(x):
    if isinstance(x, str):
        return _text_normal(x)
    if isinstance(x, list):
        return [_normalisiere(i) for i in x]
    if isinstance(x, dict):
        return {k: (v if k in ("bild",) else _normalisiere(v)) for k, v in x.items()}
    return x


def punkte_von(t):
    """Punkte wie in der App: Lücken, Paare, frei (punkte), sonst 1 oder punkte."""
    if t["typ"] == "luecke":
        return len(_gaps(t["text"]))
    if t["typ"] == "zuordnen":
        return len(t["paare"])
    if t["typ"] == "frei":
        return t["punkte"]
    return t.get("punkte", 1)


# ------------------------------------------------------------------ Jahreszahlen

def jahr(y):
    """-3000 -> '3000 v. Chr.', 500 -> '500 n. Chr.'"""
    return f"{abs(y)} v. Chr." if y < 0 else f"{y} n. Chr."


def spanne(a, b):
    """Jahre zwischen zwei Jahreszahlen (ohne Jahr 0, wie im Schulbuch: 100 v. Chr. bis 50 n. Chr. = 150 Jahre)."""
    return abs(b - a)


# Epochen nach dem Heft: (Name, Beginn, Ende), None = offen
EPOCHEN = [
    ("Ur- und Frühgeschichte", None, -3000),
    ("Altertum", -3000, -1000),
    ("Antike", -1000, 500),
    ("Mittelalter", 500, 1500),
    ("Neuzeit", 1500, None),
]


def epoche(y):
    """Epoche eines Jahres (Grenzjahre vermeiden!)."""
    for name, a, b in EPOCHEN:
        if (a is None or y > a) and (b is None or y < b):
            return name
    raise AssertionError(y)


# ------------------------------------------------------------------ Zeichnung: Epochen auf dem Zeitstrahl

def svg_epochen(nummern=True, jahre=True, namen_unten=True):
    """Zeitstrahl von 3000 v. Chr. bis 2000 n. Chr. mit den fünf Epochen (Heft). Nicht maßstäblich bei der ersten Epoche.

    nummern: Kreise 1 bis 5 in den Balken. jahre: Jahreszahlen an den Grenzen. namen_unten: Namen und Daten unter den Balken.
    """
    X = lambda y: 110 + (y + 3000) * 0.124
    farben = ["#c9b8a0", "#e8c27a", "#9fc5a0", "#8fb8d8", "#d4a0c0"]
    g = []
    y0, h = 96, 46
    grenzen = [(20, 110), (X(-3000), X(-1000)), (X(-1000), X(500)), (X(500), X(1500)), (X(1500), 730)]
    for i, (a, b) in enumerate(grenzen):
        g.append(f'<rect x="{a:.1f}" y="{y0}" width="{b - a:.1f}" height="{h}" fill="{farben[i]}" stroke="#555" stroke-width="1.5"/>')
        if nummern:
            g.append(_num(round((a + b) / 2, 1), y0 + h / 2, i + 1))
    g.append(f'<polygon points="20,{y0 + h / 2} 6,{y0 + h / 2 - 9} 6,{y0 + h / 2 + 9}" fill="#555"/>')
    if jahre:
        for yy, txt in ((-3000, "3000 v. Chr."), (-1000, "1000 v. Chr."), (0, "Christi Geburt"), (500, "500"), (1500, "1500")):
            x = X(yy)
            hoch = 22 if yy == 500 else 0   # "500" steht eine Zeile höher, sonst stößt es an "Christi Geburt"
            g.append(f'<line x1="{x:.1f}" y1="{y0 - 12 - hoch}" x2="{x:.1f}" y2="{y0 + h}" stroke="#222" stroke-width="2"/>')
            g.append(_label(round(x, 1), y0 - 18 - hoch, "500 n. Chr." if yy == 500 else txt, size=14, weight="bold"))
    if namen_unten:
        mitten = [65, (X(-3000) + X(-1000)) / 2, (X(-1000) + X(500)) / 2, (X(500) + X(1500)) / 2, (X(1500) + 730) / 2]
        daten = ["bis 3000 v. Chr.", "3000–1000 v. Chr.", "1000 v. Chr.–500 n. Chr.", "500–1500 n. Chr.", "ab 1500 n. Chr."]
        for i, (n, _, _) in enumerate(EPOCHEN):
            if not nummern:
                if i == 0:
                    g.append(_label(8, y0 + h + 26, n, anchor="start", size=15, weight="bold"))
                else:
                    g.append(_label(round(mitten[i], 1), y0 + h + 26, n, size=15, weight="bold"))
                dy = 46 if i < 4 else 62
                g.append(_label(8 if i == 0 else round(mitten[i], 1), y0 + h + dy, daten[i], anchor="start" if i == 0 else "middle", size=13, fill="#444"))
    return _svg(760, 214, ''.join(g))


# ------------------------------------------------------------------ Zeichnung: Zeitstrahl mit Punkten und Zeiträumen

def svg_zeitstrahl_punkte(punkte, bereiche=(), von=-100, bis=50):
    """Einfacher Zeitstrahl (10 Jahre = 1 cm). punkte: [(Buchstabe, Jahr)], bereiche: [(Buchstabe, Beginn, Ende)]."""
    x0, x1 = 60, 700
    X = lambda y: x0 + (y - von) * (x1 - x0) / (bis - von)
    ay = 118
    g = []
    for b, a, e in bereiche:
        g.append(f'<rect x="{X(a):.1f}" y="{ay - 30}" width="{X(e) - X(a):.1f}" height="30" fill="#ffe3b0" stroke="#e2701a" stroke-width="2"/>')
        g.append(_label(round((X(a) + X(e)) / 2, 1), ay - 9, b, size=17, weight="bold", fill="#a14a00"))
    g.append(f'<line x1="{x0 - 20}" y1="{ay}" x2="{x1 + 20}" y2="{ay}" stroke="#222" stroke-width="3"/>')
    for y in range(von, bis + 1, 10):
        x = X(y)
        gross = y % 50 == 0
        g.append(f'<line x1="{x:.1f}" y1="{ay - (12 if gross else 7)}" x2="{x:.1f}" y2="{ay + (12 if gross else 7)}" stroke="#222" stroke-width="{2.4 if gross else 1.4}"/>')
        if gross:
            txt = "Christi Geburt" if y == 0 else (f"{abs(y)} v. Chr." if y < 0 else f"{y} n. Chr.")
            g.append(_label(round(x, 1), ay + 34, txt, size=15, weight="bold"))
    for b, y in punkte:
        x = X(y)
        g.append(f'<line x1="{x:.1f}" y1="{ay}" x2="{x:.1f}" y2="{ay - 52}" stroke="#e2701a" stroke-width="2"/>')
        g.append(f'<circle cx="{x:.1f}" cy="{ay}" r="5" fill="#e2701a"/>')
        g.append(f'<circle cx="{x:.1f}" cy="{ay - 66}" r="14" fill="#e2701a"/>')
        g.append(f'<text x="{x:.1f}" y="{ay - 60.5}" font-size="16" font-weight="bold" fill="#fff" text-anchor="middle">{b}</text>')
    return _svg(760, 170, ''.join(g))


# ------------------------------------------------------------------ Zeichnung: Stammbaum einer erfundenen Familie

# Erfundene Familie Berger. Jahr der Geburt, Tod (oder None), Beruf, Eltern
PERSONEN = {
    "Mia": dict(geb=2014, tod=None, beruf="Schülerin", eltern=("Jan", "Anna")),
    "Tom": dict(geb=2011, tod=None, beruf="Schüler", eltern=("Jan", "Anna")),
    "Jan": dict(geb=1980, tod=None, beruf="Lehrer", eltern=("Karl", "Ruth")),
    "Anna": dict(geb=1982, tod=None, beruf="Ärztin", eltern=("Hans", "Eva")),
    "Karl": dict(geb=1952, tod=2019, beruf="Schlosser", eltern=None),
    "Ruth": dict(geb=1954, tod=None, beruf="Verkäuferin", eltern=None),
    "Hans": dict(geb=1950, tod=None, beruf="Bäcker", eltern=None),
    "Eva": dict(geb=1953, tod=None, beruf="Schneiderin", eltern=None),
}
EHEN = [("Jan", "Anna"), ("Karl", "Ruth"), ("Hans", "Eva")]


def kinder(name):
    return [n for n, p in PERSONEN.items() if p["eltern"] and name in p["eltern"]]


def _ringe(x, y):
    return (f'<circle cx="{x - 5}" cy="{y}" r="7" fill="none" stroke="#222" stroke-width="2"/>'
            f'<circle cx="{x + 5}" cy="{y}" r="7" fill="none" stroke="#222" stroke-width="2"/>')


def svg_stammbaum(marker=None, versteckt=()):
    """Stammbaum der erfundenen Familie Berger (drei Generationen, Kinder oben, der Baum wächst nach oben wie im Buch).

    marker: {Name: Zahl} setzt orange Nummern an die Kästchen. versteckt: Namen, die als „?“ erscheinen.
    """
    W, H = 800, 380
    bw, bh = 150, 66
    pos = {"Tom": (245, 20), "Mia": (405, 20), "Jan": (115, 150), "Anna": (535, 150),
           "Karl": (30, 290), "Ruth": (200, 290), "Hans": (450, 290), "Eva": (620, 290)}
    g = []
    # Verbindungslinien zuerst
    def mitte(n):
        x, y = pos[n]
        return x + bw / 2, y
    # Ehen: Strich zwischen den Kästchen + Ringe
    for a, b in EHEN:
        xa, ya = pos[a]
        xb, yb = pos[b]
        yy = ya + bh / 2
        g.append(f'<line x1="{xa + bw}" y1="{yy}" x2="{xb}" y2="{yy}" stroke="#222" stroke-width="2.5"/>')
    # Kinder -> Ehepaar (vom Mittelpunkt zwischen den Eltern nach oben zu den Kindern)
    for (a, b) in EHEN:
        ks = kinder(a)
        if not ks:
            continue
        xa, ya = pos[a]
        xb, yb = pos[b]
        mx = (xa + bw + xb) / 2
        my = ya + bh / 2
        bar = ya - 34
        g.append(f'<line x1="{mx}" y1="{my}" x2="{mx}" y2="{bar}" stroke="#222" stroke-width="2.5"/>')
        xs = [pos[k][0] + bw / 2 for k in ks]
        g.append(f'<line x1="{min(xs + [mx])}" y1="{bar}" x2="{max(xs + [mx])}" y2="{bar}" stroke="#222" stroke-width="2.5"/>')
        for k, x in zip(ks, xs):
            g.append(f'<line x1="{x}" y1="{bar}" x2="{x}" y2="{pos[k][1] + bh}" stroke="#222" stroke-width="2.5"/>')
    for a, b in EHEN:
        xa, ya = pos[a]
        xb, yb = pos[b]
        g.append(_ringe((xa + bw + xb) / 2, ya + bh / 2))
    for n, (x, y) in pos.items():
        p = PERSONEN[n]
        gen = {2014: 0, 2011: 0}.get(p["geb"], None)
        g.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="6" fill="#fffbe9" stroke="#444" stroke-width="2"/>')
        name = "?" if n in versteckt else n
        g.append(_label(x + bw / 2, y + 21, name, size=17, weight="bold"))
        zeile = f"∗ {p['geb']}" + (f"   † {p['tod']}" if p["tod"] else "")
        g.append(_label(x + bw / 2, y + 41, zeile, size=15))
        g.append(_label(x + bw / 2, y + 59, p["beruf"], size=14, fill="#444"))
    for n, k in (marker or {}).items():
        x, y = pos[n]
        g.append(_num(x + 8, y + 8, k))
    return _svg(W, H, ''.join(g))


# ------------------------------------------------------------------ Zeichnung: Schimpanse, Lucy, Mensch (vereinfachte Strichfiguren)

def _figur(cx, boden, bein, rumpf, neigung, arm, kopf_r, farbe, knie=0):
    """Eine Strichfigur von der Seite (schaut nach rechts). neigung = Neigung des Rumpfes nach vorn in Grad."""
    th = math.radians(neigung)
    hx, hy = cx, boden - bein
    nx, ny = hx + rumpf * math.sin(th), hy - rumpf * math.cos(th)
    kx, ky = hx + knie, hy + bein * 0.5
    fx, fy = hx - 2, boden
    # Kopf sitzt vorn am Hals
    kopfx, kopfy = nx + (kopf_r + 3) * math.sin(th) + kopf_r * 0.3, ny - (kopf_r + 3) * math.cos(th)
    # Arm hängt vom Schulterpunkt nach unten und etwas nach vorn
    ax_, ay_ = nx + 6, ny + arm
    g = []
    sw = 7
    g.append(f'<line x1="{hx:.1f}" y1="{hy:.1f}" x2="{kx:.1f}" y2="{ky:.1f}" stroke="{farbe}" stroke-width="{sw}" stroke-linecap="round"/>')
    g.append(f'<line x1="{kx:.1f}" y1="{ky:.1f}" x2="{fx:.1f}" y2="{fy:.1f}" stroke="{farbe}" stroke-width="{sw}" stroke-linecap="round"/>')
    g.append(f'<line x1="{fx:.1f}" y1="{fy:.1f}" x2="{fx + 20:.1f}" y2="{fy:.1f}" stroke="{farbe}" stroke-width="{sw}" stroke-linecap="round"/>')
    g.append(f'<line x1="{hx:.1f}" y1="{hy:.1f}" x2="{nx:.1f}" y2="{ny:.1f}" stroke="{farbe}" stroke-width="{sw + 5}" stroke-linecap="round"/>')
    g.append(f'<line x1="{nx:.1f}" y1="{ny:.1f}" x2="{ax_:.1f}" y2="{ay_:.1f}" stroke="{farbe}" stroke-width="{sw - 1}" stroke-linecap="round"/>')
    g.append(f'<circle cx="{kopfx:.1f}" cy="{kopfy:.1f}" r="{kopf_r}" fill="{farbe}"/>')
    return ''.join(g)


def svg_drei(reihenfolge=("S", "L", "M"), beschriftung="buchstaben"):
    """Drei vereinfachte Strichfiguren (nicht maßstabsgetreu): S = Schimpanse, L = Lucy, M = moderner Mensch.

    beschriftung: 'buchstaben' (A, B, C von links), 'namen' oder 'keine'.
    """
    boden = 270
    kind = {
        "S": dict(bein=64, rumpf=96, neigung=52, arm=104, kopf_r=19, farbe="#7a5a3a", knie=14, name="Schimpanse"),
        "L": dict(bein=88, rumpf=92, neigung=24, arm=96, kopf_r=17, farbe="#b0793b", knie=10, name="Lucy"),
        "M": dict(bein=122, rumpf=96, neigung=0, arm=82, kopf_r=19, farbe="#3b6ea5", knie=0, name="moderner Mensch"),
    }
    g = [f'<line x1="10" y1="{boden}" x2="630" y2="{boden}" stroke="#777" stroke-width="3"/>']
    xs = [110, 300, 490]
    for x, k in zip(xs, reihenfolge):
        d = {a: b for a, b in kind[k].items() if a != "name"}
        g.append(_figur(x, boden, **d))
    for i, (x, k) in enumerate(zip(xs, reihenfolge)):
        if beschriftung == "buchstaben":
            g.append(_label(x + 10, 304, "ABC"[i], size=20, weight="bold"))
        elif beschriftung == "namen":
            g.append(_label(x + 10, 304, kind[k]["name"], size=16, weight="bold"))
    return _svg(640, 318, ''.join(g))


# ------------------------------------------------------------------ Zeichnung: Reichweiten der Jagdwaffen (Buch S. 21, M6)

WAFFEN = [("Lanze", 0, 3), ("Speer", 0, 15), ("Speerschleuder", 8, 30), ("Pfeil und Bogen", 5, 50)]


def svg_waffen(namen=True, reihenfolge=(0, 1, 2, 3)):
    """Balken: Reichweite der Jagdwaffen in Metern. namen=False: Buchstaben A bis D statt der Namen."""
    x0, x1 = 230, 730
    X = lambda m: x0 + m * (x1 - x0) / 50
    farben = ["#b5651d", "#c9923a", "#6a9f5a", "#3b6ea5"]
    g = []
    for m in range(0, 51, 10):
        g.append(f'<line x1="{X(m):.1f}" y1="30" x2="{X(m):.1f}" y2="250" stroke="#ddd" stroke-width="1.5"/>')
        g.append(_label(round(X(m), 1), 276, str(m), size=15))
    g.append(_label(round((x0 + x1) / 2, 1), 302, "Entfernung in Metern", size=15, weight="bold"))
    for i, k in enumerate(reihenfolge):
        name, a, b = WAFFEN[k]
        y = 48 + i * 52
        g.append(f'<rect x="{X(a):.1f}" y="{y}" width="{X(b) - X(a):.1f}" height="30" fill="{farben[k]}" stroke="#333" stroke-width="1.5"/>')
        g.append(_label(222, y + 21, name if namen else "ABCD"[i], anchor="end", size=16, weight="bold"))
    g.append(f'<line x1="{x0}" y1="26" x2="{x0}" y2="252" stroke="#222" stroke-width="2.5"/>')
    g.append(f'<line x1="{x0}" y1="252" x2="{x1 + 10}" y2="252" stroke="#222" stroke-width="2.5"/>')
    return _svg(760, 316, ''.join(g))


# ------------------------------------------------------------------ Zeichnung: Nutztier (Rentier), Buch S. 20, M5

NUTZTIER = ["Geweih", "Fell/Haut", "Sehnen", "Fleisch", "Magen", "Knochen"]


def svg_nutztier(nummern=True, perm=(1, 2, 3, 4, 5, 6)):
    """Schema eines Rentiers mit sechs Teilen. perm gibt die Nummer jedes Teils in der Reihenfolge von NUTZTIER."""
    g = []
    # Körper
    g.append('<ellipse cx="300" cy="190" rx="130" ry="58" fill="#e7d8c0" stroke="#7a5a3a" stroke-width="3"/>')
    # Beine
    for lx in (205, 240, 355, 390):
        g.append(f'<line x1="{lx}" y1="230" x2="{lx - 4}" y2="320" stroke="#7a5a3a" stroke-width="12" stroke-linecap="round"/>')
    # Hals und Kopf
    g.append('<polygon points="410,160 462,98 492,118 448,196" fill="#e7d8c0" stroke="#7a5a3a" stroke-width="3" stroke-linejoin="round"/>')
    g.append('<ellipse cx="505" cy="112" rx="30" ry="18" transform="rotate(25 505 112)" fill="#e7d8c0" stroke="#7a5a3a" stroke-width="3"/>')
    g.append('<circle cx="512" cy="106" r="3.5" fill="#222"/>')
    # Geweih
    g.append('<polyline points="480,92 468,50 452,18" fill="none" stroke="#6b4a2a" stroke-width="6" stroke-linecap="round"/>')
    g.append('<polyline points="468,50 440,42 424,24" fill="none" stroke="#6b4a2a" stroke-width="5" stroke-linecap="round"/>')
    g.append('<polyline points="474,66 504,54 520,34" fill="none" stroke="#6b4a2a" stroke-width="5" stroke-linecap="round"/>')
    g.append('<polyline points="462,34 490,24" fill="none" stroke="#6b4a2a" stroke-width="5" stroke-linecap="round"/>')
    # Zeiger: Teil -> (Ziel, Beschriftungsposition)
    ziele = {
        "Geweih": ((452, 30), (386, 40)),
        "Fell/Haut": ((300, 134), (270, 76)),
        "Fleisch": ((222, 200), (96, 190)),
        "Sehnen": ((202, 285), (96, 292)),
        "Magen": ((300, 210), (296, 300)),
        "Knochen": ((353, 285), (462, 300)),
    }
    for name, (z, p) in ziele.items():
        g.append(f'<line x1="{z[0]}" y1="{z[1]}" x2="{p[0]}" y2="{p[1]}" stroke="#222" stroke-width="1.8"/>')
        g.append(f'<circle cx="{z[0]}" cy="{z[1]}" r="4" fill="#222"/>')
        if nummern:
            g.append(_num(p[0], p[1], perm[NUTZTIER.index(name)]))
        else:
            g.append(f'<text x="{p[0]}" y="{p[1] + 5}" font-size="16" font-weight="bold" fill="#1b1b1b" text-anchor="middle" '
                     f'stroke="#fff" stroke-width="4" paint-order="stroke" stroke-linejoin="round">{name}</text>')
    return _svg(600, 340, ''.join(g))


# ------------------------------------------------------------------ Nachlesen-Verweise (Aufgabe -> Lernblatt-Abschnitt)

def nachlesen(p, bloecke):
    """Setzt p["nachlesen"] (Aufgabenblock -> Titel eines Lernblatt-Abschnitts oder Liste von Titeln) und prüft alles.

    Jeder Block (abschnitt) der Aufgaben braucht einen Eintrag, jeder Titel muss im Lernblatt dieses Pakets vorkommen.
    Einzelne Aufgaben dürfen zusätzlich ein Feld "lesen" (Titel oder Liste) haben, das den Verweis des Blocks verfeinert.
    """
    titel = {s["titel"] for s in p["lernblatt"]}
    vorhanden = {t["abschnitt"] for t in p["aufgaben"]}
    assert vorhanden == set(bloecke), (p["id"], "Blöcke ohne Verweis / Verweis ohne Block:", vorhanden ^ set(bloecke))
    for b, r in bloecke.items():
        for x in (r if isinstance(r, list) else [r]):
            assert x in titel, f"{p['id']} Block „{b}“: Abschnitt „{x}“ fehlt im Lernblatt ({sorted(titel)})"
    for i, t in enumerate(p["aufgaben"], 1):
        if "lesen" in t:
            for x in (t["lesen"] if isinstance(t["lesen"], list) else [t["lesen"]]):
                assert x in titel, f"{p['id']} Aufgabe {i}: lesen „{x}“ fehlt im Lernblatt"
    p["nachlesen"] = bloecke
    return p
