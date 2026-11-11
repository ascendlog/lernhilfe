"""Geschichte Klasse 6, Teil 5: Die Neolithische Revolution (5a) und das Leben in der Jungsteinzeit im Vergleich mit der Altsteinzeit (5b).

Alle Jahreszahlen und Rechnungen werden im Code berechnet und mit assert geprüft (gesch_lib.jahr, spanne, epoche).
Quelle der Fakten: gesch-work/fakten.md, Abschnitt 6 (und Abschnitt 5 für den Vergleich). Texte in eigenen Worten.
Datenschutz: Das Repository ist öffentlich. Alle Zeichnungen und Beispiele sind erfunden, keine echten Personen.
"""
from gesch_lib import *                                   # noqa: F401,F403  (mc, tf, kurz, luecke, zuordnen, reihenfolge, frei, lb, pack, nachlesen, jahr, spanne, epoche)
from gesch_lib import _svg, _label, _num, _arrow          # noqa: F401
import math

HEUTE = 2026   # Jahr der Klassenarbeit, für „Wie lange ist das her?“


# ------------------------------------------------------------------ Hilfen für Zahlen

def vchr(y):
    """Jahr als Zahl v. Chr. (positiv) -> Jahreszahl im Code (negativ)."""
    return -y


def tausend(n):
    """11026 -> '11 026' (Leerzeichen als Tausendertrenner)."""
    s = f"{n:,}".replace(",", " ")
    return s


def _ohne_doppelte(liste):
    seen = []
    for x in liste:
        if x not in seen:
            seen.append(x)
    return seen


def schreibweisen_jahr(y):
    """Erlaubte Schreibweisen für ein Jahr v. Chr. (y positiv), zum Beispiel 9000: mit/ohne „um, ca., etwa“, „v. Chr.“, „vor Christus“, „vor Christi Geburt“.

    Die App vergleicht exakt (nur Groß/Klein und Schlusspunkt sind egal), darum werden die Varianten hier erzeugt.
    """
    a, b, c = f"{y}", f"{y:,}".replace(",", "."), f"{y:,}".replace(",", " ")
    out = [f"{a} v. Chr."]
    for pre in ("", "um ", "ca. ", "etwa "):
        for suf in ("", " v. Chr.", " v.Chr.", " vor Chr.", " vor Christus", " vor Christi Geburt"):
            out.append(f"{pre}{a}{suf}")
    for pre in ("ungefähr ", "rund "):
        for suf in ("", " v. Chr."):
            out.append(f"{pre}{a}{suf}")
    for z in (b, c):
        for pre in ("", "ca. "):
            for suf in ("", " v. Chr."):
                out.append(f"{pre}{z}{suf}")
    return _ohne_doppelte(out)


def schreibweisen_zahl(n, praefixe=("", "ca. ", "etwa ", "ungefähr ", "rund ", "circa "), formen="abc"):
    """Erlaubte Schreibweisen einer ganzen Zahl: 11026, 11.026, 11 026, mit „Jahre“ und „ca./etwa/ungefähr/rund/circa“.

    formen: a = 11026, b = 11.026, c = 11 026. Die Varianten werden hier erzeugt, weil die App exakt vergleicht.
    """
    z = {"a": f"{n}", "b": f"{n:,}".replace(",", "."), "c": f"{n:,}".replace(",", " ")}
    out = []
    for f in formen:
        for pre in praefixe:
            for suf in ("", " Jahre"):
                if f != "a" and pre not in ("", "ca. ", "etwa "):
                    continue          # gepunktete und getrennte Zahlen nur mit den kurzen Zusätzen
                out.append(f"{pre}{z[f]}{suf}")
    return _ohne_doppelte(out)


# ------------------------------------------------------------------ Zeichnungen (SVG)

def _lab(x, y, text, anchor="middle", size=15, weight="bold", fill="#1b1b1b"):
    """Beschriftung mit weißem Rand (gut lesbar auf Farbflächen)."""
    return (f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" '
            f'stroke="#fff" stroke-width="4" paint-order="stroke" stroke-linejoin="round">{text}</text>')


def _pfeil(x1, y1, x2, y2, farbe="#a14a00", w=6, kopf=20):
    """Pfeil mit deutlicher Spitze."""
    ang = math.atan2(y2 - y1, x2 - x1)
    bx, by = x2 - kopf * math.cos(ang), y2 - kopf * math.sin(ang)
    px, py = -math.sin(ang) * kopf * 0.55, math.cos(ang) * kopf * 0.55
    return (f'<line x1="{x1}" y1="{y1}" x2="{bx:.1f}" y2="{by:.1f}" stroke="{farbe}" stroke-width="{w}" stroke-linecap="round"/>'
            f'<polygon points="{x2},{y2} {bx + px:.1f},{by + py:.1f} {bx - px:.1f},{by - py:.1f}" fill="{farbe}"/>')


def _kreis_buchstabe(x, y, b):
    return (f'<circle cx="{x}" cy="{y}" r="14" fill="#e2701a"/>'
            f'<text x="{x}" y="{y + 5.5}" font-size="16" font-weight="bold" fill="#fff" text-anchor="middle">{b}</text>')


# Ereignisse auf dem Zeitstrahl: (Jahr v. Chr., Buchstabe, Zeile 1, Zeile 2, Reihe, Ausrichtung)
STRAHL = [
    (9000, "A", "Menschen werden", "sesshaft", "unten", "middle"),
    (7000, "B", "Keramik", "", "oben", "middle"),
    (5700, "C", "Ackerbau in", "Mitteleuropa", "unten", "middle"),
    (5000, "D", "Esel und Pferd als", "Reit- und Packtiere", "oben", "middle"),
    (4500, "E", "Pflug in", "Mitteleuropa", "unten", "start"),
    (3000, "F", "Rad", "", "oben", "middle"),
]


def svg_strahl(namen=True):
    """Zeitstrahl der Jungsteinzeit von 10 500 bis 3000 v. Chr. mit sechs Ereignissen (Heft und Buch).

    namen=True: Namen der Ereignisse. namen=False: nur Buchstaben A bis F (die Jahre stehen unter der Leiste).
    """
    von, bis = 10500, 3000
    x0, x1 = 30, 710
    X = lambda y: x0 + (von - y) * (x1 - x0) / (von - bis)
    by0, by1 = 124, 162
    g = []
    # Leisten
    xa = X(9000)
    g.append(f'<rect x="{x0}" y="{by0}" width="{xa - x0:.1f}" height="{by1 - by0}" fill="#c9b8a0" stroke="#555" stroke-width="1.5"/>')
    g.append(f'<rect x="{xa:.1f}" y="{by0}" width="{x1 - xa:.1f}" height="{by1 - by0}" fill="#e8c27a" stroke="#555" stroke-width="1.5"/>')
    g.append(f'<polygon points="{x0},{(by0 + by1) / 2} {x0 - 14},{(by0 + by1) / 2 - 9} {x0 - 14},{(by0 + by1) / 2 + 9}" fill="#555"/>')
    g.append(_label(round((x0 + xa) / 2, 1), by0 + 25, "Altsteinzeit", size=15, weight="bold"))
    g.append(_label(round((xa + x1) / 2, 1), by0 + 25, "Jungsteinzeit", size=16, weight="bold"))
    # Jahreszahlen unter der Leiste
    for y, b, z1, z2, reihe, anker in STRAHL:
        x = X(y)
        g.append(f'<line x1="{x:.1f}" y1="{by1}" x2="{x:.1f}" y2="{by1 + 10}" stroke="#222" stroke-width="2.4"/>')
        g.append(_label(round(x, 1), by1 + 30, str(y), size=15, weight="bold"))
    g.append(_label(round((x0 + x1) / 2, 1), by1 + 56, "Jahre v. Chr.", size=15, fill="#444"))
    # Ereignisse über der Leiste
    for y, b, z1, z2, reihe, anker in STRAHL:
        x = X(y)
        if namen:
            top = 44 if reihe == "oben" else 92      # Grundlinie der letzten Textzeile = top + 2
            g.append(f'<line x1="{x:.1f}" y1="{top + 8}" x2="{x:.1f}" y2="{by0}" stroke="#e2701a" stroke-width="2"/>')
            g.append(f'<circle cx="{x:.1f}" cy="{by0}" r="5" fill="#e2701a"/>')
            tx = x - 8 if anker == "start" else x
            if z2:
                g.append(_lab(round(tx, 1), top - 16, z1, anchor=anker))
                g.append(_lab(round(tx, 1), top + 2, z2, anchor=anker))
            else:
                g.append(_lab(round(tx, 1), top + 2, z1, anchor=anker))
        else:
            cy = 50 if reihe == "oben" else 96
            g.append(f'<line x1="{x:.1f}" y1="{cy + 14}" x2="{x:.1f}" y2="{by0}" stroke="#e2701a" stroke-width="2"/>')
            g.append(f'<circle cx="{x:.1f}" cy="{by0}" r="5" fill="#e2701a"/>')
            g.append(_kreis_buchstabe(round(x, 1), cy, b))
    return _svg(760, 236, ''.join(g))


def svg_halbmond(nummern=False):
    """Vereinfachte Skizze (nicht maßstäblich): Mittelmeer, Persischer Golf, Euphrat und Tigris, fruchtbarer Halbmond.

    nummern=True: Zahlen 1 bis 4 statt der Namen (1 Mittelmeer, 2 Persischer Golf, 3 Euphrat und Tigris, 4 fruchtbarer Halbmond).
    """
    g = []
    g.append('<rect width="760" height="440" fill="#f3ead0"/>')
    # Meere
    g.append('<polygon points="0,170 120,172 250,196 240,262 220,340 200,440 0,440" fill="#bfe0f3" stroke="#5aa6d1" stroke-width="2"/>')
    g.append('<polygon points="600,350 650,342 706,362 760,392 760,440 640,440 624,396" fill="#bfe0f3" stroke="#5aa6d1" stroke-width="2"/>')
    # fruchtbarer Halbmond (grüner Bogen)
    g.append('<path d="M 258 336 C 246 244, 304 154, 414 152 C 524 150, 592 240, 606 340" fill="none" stroke="#7fb36b" stroke-width="56" stroke-linecap="round" opacity="0.6"/>')
    # Flüsse
    g.append('<path d="M 372 118 C 392 176, 478 240, 604 352" fill="none" stroke="#2b7bb9" stroke-width="5" stroke-linecap="round"/>')
    g.append('<path d="M 470 104 C 500 172, 566 246, 616 352" fill="none" stroke="#2b7bb9" stroke-width="5" stroke-linecap="round"/>')
    # Pfeil: Ausbreitung nach Europa
    g.append(_pfeil(318, 150, 96, 58))
    # Marke Irak
    g.append('<circle cx="540" cy="300" r="9" fill="#e2701a" stroke="#fff" stroke-width="3"/>')
    if nummern:
        g.append(_num(96, 316, 1))
        g.append(_num(706, 410, 2))
        g.append(_num(566, 262, 3))
        g.append(_num(250, 258, 4))
    else:
        g.append(_lab(96, 316, "Mittelmeer", fill="#1b5e8c", size=16))
        g.append(_lab(702, 402, "Persischer", fill="#1b5e8c"))
        g.append(_lab(702, 421, "Golf", fill="#1b5e8c"))
        g.append(_lab(396, 112, "Euphrat", fill="#1f5f96", anchor="end"))
        g.append(_lab(488, 98, "Tigris", fill="#1f5f96", anchor="start"))
        g.append(_lab(246, 258, "fruchtbarer", fill="#2f6b24"))
        g.append(_lab(246, 277, "Halbmond", fill="#2f6b24"))
    g.append(_lab(290, 80, "Türkei", fill="#555", weight="normal"))
    g.append(_lab(364, 232, "Syrien", fill="#555", weight="normal"))
    g.append(_lab(540, 332, "Irak", fill="#7a3a00"))
    g.append(_lab(690, 210, "Iran", fill="#555", weight="normal"))
    g.append(_lab(20, 30, "Weg nach Europa", anchor="start", fill="#a14a00", size=16))
    g.append(_lab(742, 28, "vereinfachte Skizze, nicht maßstäblich", anchor="end", fill="#555", weight="normal"))
    return _svg(760, 440, ''.join(g))


# Vergleichstabelle (Zeilen aus dem Buch, Antworten aus Heft und Buch): (Zeile, Altsteinzeit (2 Zeilen), Jungsteinzeit (2 Zeilen))
VERGLEICH = [
    ("Nahrungserwerb", ("Jagen und Sammeln", ""), ("Ackerbau und Viehzucht", "(Jagd nur daneben)")),
    ("Nahrung", ("Fleisch, Fisch, Beeren,", "Wurzeln, Pilze, Nüsse"), ("Getreide (Brot, Brei), Milch,", "Käse, Fleisch der Haustiere")),
    ("Erfindungen", ("Faustkeil, Speer, Speerschleuder,", "Pfeil und Bogen, Nähnadel, Feuer"), ("Pflug, Keramik, Webstuhl, Mahlstein,", "geschliffene Beile, Rad")),
    ("Aufenthaltsorte", ("wechselnde Lagerplätze,", "Zelte, Höhlen"), ("feste Dörfer", "mit Häusern")),
    ("Gefahren", ("Raubtiere, Kälte, Jagdunfälle,", "Nahrungsmangel"), ("Missernten, Hunger,", "Streit um Besitz")),
    ("Bekleidung", ("Felle und Leder", ""), ("gewebte Stoffe (Wolle, Lein)", "neben Fellen")),
    ("Lebensweise", ("Nomaden in kleinen Gruppen", ""), ("sesshaft, Arbeitsteilung", "und Berufe")),
]


def svg_vergleich(jung=True, alt=True):
    """Vergleichstabelle Altsteinzeit / Jungsteinzeit als Bild. jung=False: Spalte der Jungsteinzeit leer (zum Ergänzen)."""
    W = 760
    cw = [146, 300, 300]
    x = [10, 10 + cw[0], 10 + cw[0] + cw[1]]
    rh, kh = 52, 40
    g = []
    heads = ["", "Altsteinzeit", "Jungsteinzeit"]
    fills = ["#ffffff", "#e4d7c3", "#f3dca0"]
    for i in (1, 2):
        g.append(f'<rect x="{x[i]}" y="10" width="{cw[i]}" height="{kh}" fill="{fills[i]}" stroke="#7a6a50" stroke-width="1.5"/>')
        g.append(_label(x[i] + cw[i] / 2, 10 + kh / 2 + 6, heads[i], size=17, weight="bold"))
    for r, (zeile, a, j) in enumerate(VERGLEICH):
        y = 10 + kh + r * rh
        g.append(f'<rect x="{x[0]}" y="{y}" width="{cw[0]}" height="{rh}" fill="#eef3f7" stroke="#7a8fa3" stroke-width="1.5"/>')
        g.append(_label(x[0] + cw[0] / 2, y + rh / 2 + 5, zeile, size=15, weight="bold"))
        for i, (txt, sichtbar) in enumerate(((a, alt), (j, jung)), start=1):
            g.append(f'<rect x="{x[i]}" y="{y}" width="{cw[i]}" height="{rh}" fill="{"#ffffff" if r % 2 == 0 else "#f8f8f8"}" stroke="#7a8fa3" stroke-width="1.5"/>')
            if not sichtbar:
                g.append(_label(x[i] + cw[i] / 2, y + rh / 2 + 6, "?", size=20, weight="bold", fill="#999"))
                continue
            l1, l2 = txt
            if l2:
                g.append(_label(x[i] + cw[i] / 2, y + 22, l1, size=15))
                g.append(_label(x[i] + cw[i] / 2, y + 42, l2, size=15))
            else:
                g.append(_label(x[i] + cw[i] / 2, y + rh / 2 + 5, l1, size=15))
    H = 10 + kh + rh * len(VERGLEICH) + 10
    return _svg(W, H, ''.join(g))


def svg_dorf(nummern=False):
    """Erfundene, vereinfachte Skizze eines Dorfs der Jungsteinzeit von oben (nicht maßstäblich).

    nummern=True: Zahlen 1 bis 5 statt der Namen (1 Langhaus, 2 Acker, 3 Weide mit Schafen, 4 Töpferei, 5 Wald).
    """
    g = []
    g.append('<rect width="760" height="420" fill="#d5e7b8"/>')
    # Wald (oben links)
    for (cx, cy, r) in [(40, 40, 28), (92, 30, 26), (144, 46, 28), (200, 32, 24), (66, 92, 26), (122, 100, 28), (178, 92, 26), (236, 76, 24), (30, 140, 24), (96, 150, 22)]:
        g.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#4f8a3c" stroke="#3b6b2c" stroke-width="2"/>')
    # Acker (oben rechts) mit Furchen
    g.append('<rect x="440" y="30" width="290" height="150" fill="#e0c07c" stroke="#8a6a2a" stroke-width="3"/>')
    for k in range(1, 8):
        yy = 30 + k * 18.75
        g.append(f'<line x1="440" y1="{yy}" x2="730" y2="{yy}" stroke="#b98f3f" stroke-width="3"/>')
    for k in range(0, 8):
        yy = 30 + k * 18.75 + 9
        for xx in range(458, 730, 34):
            g.append(f'<line x1="{xx}" y1="{yy + 4}" x2="{xx}" y2="{yy - 5}" stroke="#6f9b3a" stroke-width="3" stroke-linecap="round"/>')
    # Weide (unten rechts) mit Zaun und Schafen
    g.append('<rect x="440" y="230" width="290" height="160" fill="#bfe08f" stroke="#7a5a3a" stroke-width="3" stroke-dasharray="10 6"/>')
    for (sx, sy) in [(490, 290), (570, 326), (640, 280), (690, 352), (520, 358)]:
        g.append(f'<ellipse cx="{sx}" cy="{sy}" rx="20" ry="13" fill="#ffffff" stroke="#777" stroke-width="2"/>')
        g.append(f'<circle cx="{sx + 20}" cy="{sy - 3}" r="7" fill="#555"/>')
    # Dorfweg
    g.append('<path d="M 20 240 C 140 232, 260 250, 420 214 L 420 244 C 260 282, 140 266, 20 276 Z" fill="#e6d3a3" opacity="0.8"/>')
    # Langhäuser (links): lange Rechtecke mit Strohdach (Linien)
    def haus(x, y, w, h=46):
        s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="#d9b45e" stroke="#7a5a2a" stroke-width="3"/>'
        for k in range(1, 5):
            s += f'<line x1="{x}" y1="{y + k * h / 5:.1f}" x2="{x + w}" y2="{y + k * h / 5:.1f}" stroke="#b58c3a" stroke-width="2"/>'
        return s
    g.append(haus(40, 170, 230))
    g.append(haus(60, 296, 210))
    g.append(haus(300, 296, 110, 40))
    # Töpferei (klein) mit Töpfen
    g.append('<rect x="300" y="150" width="96" height="60" rx="6" fill="#c97f4a" stroke="#7a3c15" stroke-width="3"/>')
    for (px, py) in [(322, 232), (352, 234), (380, 230)]:
        g.append(f'<ellipse cx="{px}" cy="{py}" rx="13" ry="10" fill="#b5532a" stroke="#6b2a10" stroke-width="2"/>')
        g.append(f'<rect x="{px - 7}" y="{py - 15}" width="14" height="7" fill="#b5532a" stroke="#6b2a10" stroke-width="2"/>')
    if nummern:
        g.append(_num(155, 193, 1))
        g.append(_num(585, 105, 2))
        g.append(_num(440 + 145, 258, 3))
        g.append(_num(348, 180, 4))
        g.append(_num(130, 62, 5))
    else:
        g.append(_lab(155, 198, "Langhaus"))
        g.append(_lab(585, 110, "Acker"))
        g.append(_lab(585, 262, "Weide mit Schafen"))
        g.append(_lab(348, 186, "Töpferei"))
        g.append(_lab(130, 66, "Wald"))
        g.append(_lab(355, 322, "Haus", size=15))
        g.append(_lab(165, 322, "Langhaus"))
    g.append(_lab(742, 410, "erfundene Skizze, nicht maßstäblich", anchor="end", weight="normal", fill="#444"))
    return _svg(760, 420, ''.join(g))


# ------------------------------------------------------------------ Jahreszahlen und Rechnungen (Heft und Buch), im Code geprüft

ALT_ENDE = 9000                    # Altsteinzeit bis ca. 9000 v. Chr. (Heft)
JUNG_BEGINN, JUNG_ENDE = 9000, 3000
KERAMIK_J = 7000                   # Keramik seit ca. 7000 v. Chr.
ACKERBAU_MITTELEUROPA_J = 5700     # Mitteleuropa ab ca. 5700 v. Chr.
ESEL_PFERD_J = 5000                # Esel und Pferd als Reit-, Pack- und Zugtiere ab ca. 5000 v. Chr.
PFLUG_J = 4500                     # Pflug in Mitteleuropa seit ca. 4500 v. Chr.
RAD_J = 3000                       # Rad um 3000 v. Chr.
HUND_VOR_JAHREN = 14000            # Hund schon in der Altsteinzeit vor ca. 14 000 Jahren
MITTELSTEINZEIT_DAUER = 3000       # in Mitteleuropa rund 3000 Jahre

EREIGNISSE = [(JUNG_BEGINN, "Menschen werden sesshaft"), (KERAMIK_J, "Keramik"), (ACKERBAU_MITTELEUROPA_J, "Ackerbau in Mitteleuropa"),
              (ESEL_PFERD_J, "Esel und Pferd als Reit- und Packtiere"), (PFLUG_J, "Pflug in Mitteleuropa"), (RAD_J, "Rad")]
assert [e[0] for e in EREIGNISSE] == [x[0] for x in STRAHL]                       # Zeichnung und Daten stimmen überein
assert [e[0] for e in EREIGNISSE] == sorted((e[0] for e in EREIGNISSE), reverse=True)   # früh nach spät (v. Chr. fallend)

DAUER_JUNGSTEINZEIT = spanne(vchr(JUNG_BEGINN), vchr(JUNG_ENDE))                  # 6000
ABSTAND_9000_HEUTE = spanne(vchr(JUNG_BEGINN), HEUTE)                             # 11026
AUSBREITUNG_BIS_MITTELEUROPA = spanne(vchr(JUNG_BEGINN), vchr(ACKERBAU_MITTELEUROPA_J))   # 3300
PFLUG_BIS_RAD = spanne(vchr(PFLUG_J), vchr(RAD_J))                                # 1500
assert DAUER_JUNGSTEINZEIT == 6000
assert ABSTAND_9000_HEUTE == 11026
assert AUSBREITUNG_BIS_MITTELEUROPA == 3300
assert PFLUG_BIS_RAD == 1500
assert epoche(vchr(6000)) == "Ur- und Frühgeschichte" and epoche(vchr(JUNG_BEGINN + 1500)) == "Ur- und Frühgeschichte"
assert epoche(vchr(2000)) == "Altertum"
ABSTAND_RUND = round(ABSTAND_9000_HEUTE, -3)                                      # 11000 (die Jahreszahlen sind Näherungswerte)
assert ABSTAND_RUND == 11000
# erlaubt: 11 026 (Schulregel, ohne Jahr 0), 11 025 (streng gerechnet) und 11 000 (gerundet), jeweils auch mit „etwa“ usw.
ABSTAND_NAEHERUNG = _ohne_doppelte(schreibweisen_zahl(ABSTAND_9000_HEUTE, ("", "ca. ", "etwa "))
                                   + schreibweisen_zahl(ABSTAND_9000_HEUTE - 1, ("", "ca. ", "etwa "), formen="ac")
                                   + schreibweisen_zahl(ABSTAND_RUND, ("", "ca. ", "etwa ", "ungefähr ", "rund "), formen="ac"))
HUND_JAHR = HEUTE - HUND_VOR_JAHREN                                               # -11974, also 11974 v. Chr.
assert jahr(HUND_JAHR) == "11974 v. Chr." and HUND_JAHR < vchr(ALT_ENDE)          # liegt vor 9000 v. Chr. = Altsteinzeit
assert jahr(vchr(JUNG_BEGINN)) == "9000 v. Chr." and jahr(vchr(RAD_J)) == "3000 v. Chr."


# ====================================================================== Paket 5a

def lernblatt_5a():
    return [
        lb("Das Ende der Eiszeit",
           "Die **Eiszeit** war eine lange Kaltzeit. Ihre letzte Kaltphase heißt **Würm-Eiszeit**. In Mitteleuropa gab es damals kaum Wälder. Stattdessen breitete sich eine weite **Steppe** aus, eine Landschaft mit Gräsern, Kräutern und niedrigen Büschen. Dort lebten Mammuts, Wollnashörner, Steppenbisons und riesige Herden von Rentieren und Wildpferden.\n"
           "Vor rund 10 000 bis 11 000 Jahren wurde es wärmer. Damit begann die **Warmzeit**, in der wir noch heute leben. Das änderte sich:\n"
           "- Die **Gletscher** schmolzen, und es kam zu Überschwemmungen.\n"
           "- Es regnete mehr.\n"
           "- Das Schmelzwasser floss in die Meere, der **Meeresspiegel** (die Höhe des Wassers im Meer) stieg wieder.\n"
           "- **Mischwälder** (Wälder aus Laub- und Nadelbäumen) breiteten sich aus.\n"
           "- Tiere, die Kälte lieben, zogen nach Norden oder starben aus. Im Wald lebten nun zum Beispiel Ur, Braunbär, Wisent, Hirsch, Reh, Wildschwein, Wolf und Luchs.",
           merke="Am Ende der Eiszeit wird es wärmer und regnerischer: Die Gletscher schmelzen, der Meeresspiegel steigt, Mischwälder ersetzen die Steppe, und die Tierwelt ändert sich."),
        lb("Die Mittelsteinzeit: Jäger im Wald",
           "Nach der Eiszeit begann in Mitteleuropa laut Buch zusätzlich die **Mittelsteinzeit**. Sie dauerte nach dem Buch rund 3000 Jahre. Die Menschen blieben noch **Jäger und Sammler**: Sie lebten von der Jagd und von dem, was sie sammelten. Ackerbau und Viehzucht kannten sie noch nicht.\n"
           "Im dichten Wald war die Jagd schwerer als in der offenen Steppe. Dabei half **Pfeil und Bogen**, denn damit kann man aus der Ferne gezielt schießen.\n"
           "Für die Prüfung zählt, wie dein Lehrer die Steinzeit einteilt. Im Heft sind es **zwei Teile**: Altsteinzeit (bis ca. 9000 v. Chr.) und Jungsteinzeit (ca. 9000 bis 3000 v. Chr.). Im Buch kommt die Mittelsteinzeit zusätzlich dazu, dort sind es drei Teile. Beides ist nicht falsch. Alle Jahreszahlen sind Näherungswerte (ungefähre Angaben), darum passen Heft und Buch nicht überall genau zusammen. Die drei Abschnitte haben auch griechische Namen: **Paläolithikum** (Altsteinzeit), **Mesolithikum** (Mittelsteinzeit) und **Neolithikum** (Jungsteinzeit).",
           merke="Heft: zwei Teile (Alt- und Jungsteinzeit). Buch: drei Teile, dazu die Mittelsteinzeit. In der Mittelsteinzeit sind die Menschen noch Jäger und Sammler."),
        lb("Sesshaft werden: die neolithische Revolution",
           "Um **9000 v. Chr.** begannen die ersten Menschen, **sesshaft** zu werden. Das heißt: Sie wohnten dauerhaft an einem festen Ort. Vorher waren sie ihrer Nahrung hinterhergezogen. Nun sorgten sie selbst für ihr Essen:\n"
           "- **Ackerbau**: Sie bauten Getreide an.\n"
           "- **Viehzucht**: Sie hielten und züchteten Tiere.\n"
           "- **Vorratshaltung**: Sie legten Vorräte an.\n"
           "Das warme, regenreiche Klima der Warmzeit machte den Getreideanbau möglich. Der Wandel war so gewaltig, dass man von der **neolithischen Revolution** spricht. Neolithisch heißt jungsteinzeitlich, deshalb sagt man auch **steinzeitliche Revolution**. Mit „Revolution“ ist hier kein Aufstand gemeint, sondern ein **grundlegender Wandel**. Er geschah nicht von heute auf morgen, sondern Schritt für Schritt. Gejagt wurde weiterhin.",
           merke="Neolithische Revolution: Aus Jägern und Sammlern werden sesshafte Bauern (um 9000 v. Chr.) mit Ackerbau, Viehzucht und Vorratshaltung. „Revolution“ heißt hier grundlegender Wandel, nicht Aufstand."),
        lb("Der fruchtbare Halbmond und der Weg nach Europa",
           "Die neue Lebensweise begann im heutigen **Irak**, in der fruchtbaren Gegend um die Flüsse **Euphrat** und **Tigris**. Allgemein sagt man: im **fruchtbaren Halbmond**. So nennt man das halbmondförmige Gebiet zwischen dem Mittelmeer und dem Persischen Golf. Heute liegen dort Israel, Libanon, die Türkei, Syrien, der Irak und der Iran.\n"
           "Von dort verbreitete sich die neue Lebensweise langsam nach Westen und Norden. Das dauerte Jahrhunderte und Jahrtausende. In Mitteleuropa gibt es die ersten Ackerbauern ab etwa **5700 v. Chr.** Nach ihren verzierten Gefäßen nennt man sie die **Linienbandkeramische Kultur**.",
           merke="Ausgangspunkt: Irak, Euphrat und Tigris (fruchtbarer Halbmond). In Mitteleuropa ab ca. 5700 v. Chr.: Linienbandkeramische Kultur.",
           bild=svg_halbmond(False),
           bildAlt="Vereinfachte Skizze: links das Mittelmeer, unten rechts der Persische Golf, dazwischen ein grüner Bogen, der fruchtbare Halbmond. Die Flüsse Euphrat und Tigris fließen von oben zum Persischen Golf. Der Irak ist markiert. Ein Pfeil zeigt von dort nach Nordwesten: der Weg nach Europa."),
        lb("Haustiere: Domestikation und Züchtung",
           "Die ersten Bauern **domestizierten** Tiere und Pflanzen. Bei der **Domestikation** werden wilde Tiere und Pflanzen gefangen, gezähmt und für den Menschen nutzbar gemacht. Bei der **Züchtung** wählt man gezielt Tiere und Pflanzen mit gewünschten Eigenschaften aus und fördert sie.\n"
           "- Der **Hund** wurde schon in der Altsteinzeit zum Haustier, vor etwa 14 000 Jahren.\n"
           "- Danach folgten **Schaf, Ziege, Rind, Schwein** und Pferd.\n"
           "- **Schafe** liefern Fleisch, Wolle und Milch. Aus der Milch machte man Käse, der länger haltbar ist.\n"
           "- Ab etwa **5000 v. Chr.** nutzte man **Esel** und Pferd als Reit-, Pack- und Zugtiere.\n"
           "Tiere zu halten und zu züchten war weniger gefährlich als die Jagd. Gejagt wurde trotzdem weiter.",
           merke="Domestikation: zähmen und nutzbar machen. Züchtung: gezielt die besten Tiere und Pflanzen auswählen. Hund schon in der Altsteinzeit, dann Schaf, Ziege, Rind, Schwein."),
        lb("Nutzpflanzen der ersten Bauern",
           "Die wichtigsten Pflanzen der ersten Bauern waren:\n"
           "- **Emmer, Einkorn und Gerste**: Getreide für Brot und Brei.\n"
           "- **Lein**: Aus ihm gewann man Öl und Fasern zum Spinnen.\n"
           "- **Mohn**: Er diente als Gewürz und als Heilmittel.\n"
           "- Dazu kamen Hülsenfrüchte (Pflanzen mit Schoten, zum Beispiel Erbsen und Linsen). Pilze, Nüsse, Obst, Beeren und Wurzeln rundeten den Speiseplan ab.\n"
           "Am Anfang war das Essen einseitig. Fiel die Ernte aus, drohten **Hungersnöte** (viele Menschen haben zu wenig zu essen). Trotzdem wuchs die Bevölkerung stetig, und es mussten neue Siedlungen und Ackerflächen angelegt werden.",
           merke="Getreide (Emmer, Einkorn, Gerste) wurde das Grundnahrungsmittel. Lein liefert Öl und Fasern, Mohn ist Gewürz und Heilmittel."),
        lb("Pflug und Rad",
           "Der **Pflug** lockert den Boden, bevor man das Getreide aussät. Die ersten Pflüge waren aus Holz. In Mitteleuropa gibt es den Pflug seit etwa **4500 v. Chr.** Getreide wurde zum **Grundnahrungsmittel**, also zum wichtigsten Essen.\n"
           "Das **Rad** wurde erst um **3000 v. Chr.** erfunden, also lange nach dem Beginn des Ackerbaus. Esel und Pferd nutzte man schon seit etwa 5000 v. Chr. als Reit-, Pack- und Zugtiere.",
           merke="Pflug in Mitteleuropa seit ca. 4500 v. Chr., Rad um 3000 v. Chr. Das Rad kam viel später als der Ackerbau."),
        lb("Zeitstrahl und Rechnen mit Jahren",
           "Auf dem Zeitstrahl siehst du die wichtigsten Jahre dieses Teils. Bei Jahren **vor Christi Geburt (v. Chr.)** zählen die Zahlen rückwärts: Je größer die Zahl, desto früher war es. Darum rechnest du so:\n"
           f"- Von einem Jahr v. Chr. zu einem späteren Jahr v. Chr.: **abziehen**. Beispiel: {JUNG_BEGINN} v. Chr. bis {JUNG_ENDE} v. Chr. = {JUNG_BEGINN} − {JUNG_ENDE} = {DAUER_JUNGSTEINZEIT} Jahre. So lange dauerte die Jungsteinzeit nach dem Heft.\n"
           f"- Von einem Jahr v. Chr. bis heute: **addieren**. Beispiel: {JUNG_BEGINN} v. Chr. bis {HEUTE} = {JUNG_BEGINN} + {HEUTE} = {tausend(ABSTAND_9000_HEUTE)} Jahre, also etwa {tausend(round(ABSTAND_9000_HEUTE, -3))} Jahre.\n"
           "Rechne wie in der Schule, ohne Jahr 0: Ein Jahr 0 gibt es nicht, du rechnest bei Abständen über Christi Geburt einfach zusammen. Weil die Jahre ungefähre Werte sind (um, ca.), sind auch die Ergebnisse ungefähre Werte.\n"
           "Die Jungsteinzeit gehört zur Epoche **Ur- und Frühgeschichte** (bis 3000 v. Chr.). Die Mittelsteinzeit ist auf diesem Zeitstrahl nicht extra eingezeichnet, denn er folgt dem Heft.",
           merke="Von v. Chr. zu v. Chr.: abziehen. Von v. Chr. bis heute: addieren.",
           bild=svg_strahl(True),
           bildAlt="Zeitstrahl von 10 500 bis 3000 v. Chr. Die Altsteinzeit reicht bis 9000 v. Chr., danach folgt die Jungsteinzeit bis 3000 v. Chr. Eingezeichnet sind: 9000 Menschen werden sesshaft, 7000 Keramik, 5700 Ackerbau in Mitteleuropa, 5000 Esel und Pferd als Reit- und Packtiere, 4500 Pflug in Mitteleuropa, 3000 Rad."),
    ]


def aufgaben_5a():
    A = []
    L_EIS = "Das Ende der Eiszeit"
    L_MITTEL = "Die Mittelsteinzeit: Jäger im Wald"
    L_REV = "Sesshaft werden: die neolithische Revolution"
    L_HALB = "Der fruchtbare Halbmond und der Weg nach Europa"
    L_TIER = "Haustiere: Domestikation und Züchtung"
    L_PFL = "Nutzpflanzen der ersten Bauern"
    L_PFLUG = "Pflug und Rad"
    L_ZEIT = "Zeitstrahl und Rechnen mit Jahren"

    # ------------------------------------------------------------------ A Ende der Eiszeit
    s = "A – Das Ende der Eiszeit"
    A += [
        mc("Wie nennt man die Zeit, die vor rund 10 000 bis 11 000 Jahren begann und in der wir bis heute leben?", "Warmzeit",
           ["Eiszeit", "Altsteinzeit", "Würm-Eiszeit"], s,
           info="Nach der letzten Kaltphase, der Würm-Eiszeit, begann die Warmzeit. Wir leben noch heute in ihr."),
        mc("Wähle alle richtigen Antworten: Was veränderte sich am Ende der Eiszeit?",
           ["Die Gletscher schmolzen.", "Der Meeresspiegel stieg wieder.", "Mischwälder breiteten sich aus."],
           ["Die Steppe wurde größer.", "Es fiel weniger Regen."], s,
           info="Es wurde wärmer und es regnete mehr. Das Eis schmolz, das Wasser floss in die Meere, und Wälder ersetzten die Steppe."),
        tf("Als die Eiszeit zu Ende ging, sank der Meeresspiegel.", False, s,
           info="Das Eis schmolz und das Wasser floss zurück in die Meere, darum stieg der Meeresspiegel. In der Eiszeit war er niedrig, weil viel Wasser im Eis gebunden war."),
        zuordnen("Gehört das zur Eiszeit oder zur Warmzeit?",
                 [("Gletscher dehnen sich weit aus", "Eiszeit"), ("Meeresspiegel steigt", "Warmzeit"), ("Steppe ohne Wälder", "Eiszeit"),
                  ("Mischwälder breiten sich aus", "Warmzeit"), ("wenig Niederschlag", "Eiszeit"), ("Überschwemmungen durch Schmelzwasser", "Warmzeit")], s,
                 info="Die Eiszeit ist kalt und trocken, die Warmzeit warm und regenreicher."),
        mc("Welche Tiere lebten nach dem Ende der Eiszeit in den Wäldern Mitteleuropas?", "Hirsch, Reh und Wildschwein",
           ["Mammut, Wollnashorn und Höhlenbär", "Höhlenlöwe, Höhlenhyäne und Mammut", "Steppenbison, Wollnashorn und Höhlenlöwe"], s,
           info="Im Wald lebten Ur, Braunbär, Wisent, Hirsch, Reh, Wildschwein, Wolf und Luchs. Mammut, Wollnashorn und Höhlenlöwe gehören in die kalte Steppe.",
           tipp="Denke an Tiere, die im Wald leben, nicht an Tiere der offenen, kalten Steppe."),
        kurz("Wie nennt man die weite Landschaft aus Gräsern, Kräutern und niedrigen Büschen, die in der Eiszeit in Mitteleuropa fast ohne Bäume war?",
             ["Steppe", "die Steppe", "Steppenlandschaft"], s,
             info="In der kalten, trockenen Eiszeit wuchsen keine Wälder, sondern eine Steppe."),
        luecke("Ergänze den Text über das Ende der Eiszeit.",
               "Am Ende der Eiszeit wurde es {{wärmer}} und es regnete mehr. Die {{Gletscher}} schmolzen und der {{Meeresspiegel}} stieg wieder. Anstelle der Steppe breiteten sich {{Mischwälder}} aus. Tiere, die Kälte lieben, zogen nach {{Norden}} oder verschwanden.",
               s, extra=["kälter", "Süden"],
               info="Wärme und mehr Regen verändern die Landschaft: Eis schmilzt, Wald wächst, Kältetiere ziehen nach Norden."),
    ]
    # ------------------------------------------------------------------ B Mittelsteinzeit
    s = "B – Die Mittelsteinzeit"
    A += [
        reihenfolge("Ordne die Abschnitte der Steinzeit von früh nach spät.", ["Altsteinzeit", "Mittelsteinzeit", "Jungsteinzeit"], s,
                    info="Altsteinzeit (Paläolithikum), Mittelsteinzeit (Mesolithikum), Jungsteinzeit (Neolithikum). Im Heft stehen nur zwei Teile, im Buch drei."),
        tf("In der Mittelsteinzeit lebten die Menschen schon als Bauern in festen Dörfern.", False, s,
           info="In der Mittelsteinzeit waren die Menschen noch Jäger und Sammler. Ackerbau und Viehzucht kamen erst mit der Jungsteinzeit."),
        mc("Welche Jagdwaffe erleichterte die Jagd im dichten Wald?", "Pfeil und Bogen", ["Lanze und Speer", "Speerschleuder und Speer", "Harpune und Angel"], s,
           info="Mit Pfeil und Bogen kann man aus der Ferne gezielt schießen. Das half bei der Jagd im dichten Wald."),
        zuordnen("Lebte das Tier in der Steppe der Eiszeit oder im Wald der Warmzeit?",
                 [("Mammut", "Steppe der Eiszeit"), ("Ur", "Wald der Warmzeit"), ("Wollnashorn", "Steppe der Eiszeit"),
                  ("Luchs", "Wald der Warmzeit"), ("Steppenbison", "Steppe der Eiszeit"), ("Wisent", "Wald der Warmzeit")], s,
                 info="Mammut, Wollnashorn und Steppenbison gehören zur kalten Steppe, Ur, Luchs und Wisent zum Wald der Warmzeit."),
        tf(f"Nach dem Buch dauerte die Mittelsteinzeit in Mitteleuropa rund {MITTELSTEINZEIT_DAUER} Jahre.", True, s,
           info="Das steht nur im Buch, nicht im Heft. Das Buch teilt die Steinzeit in drei Teile, das Heft in zwei. Alle Jahreszahlen sind Näherungswerte."),
        luecke("Ergänze den Text über die Mittelsteinzeit.",
               "In der {{Mittelsteinzeit}} blieben die Menschen noch {{Jäger|Sammler}} und {{Sammler|Jäger}}. Im dichten Wald erleichterten {{Pfeil und Bogen}} die Jagd. Ackerbau und Viehzucht gab es noch nicht.",
               s, extra=["Bauern", "Lanzen"],
               info="Die Mittelsteinzeit liegt zwischen Alt- und Jungsteinzeit. Die Menschen lebten noch von Jagd und Sammeln."),
    ]
    # ------------------------------------------------------------------ C Neolithische Revolution
    s = "C – Sesshaft werden: die neolithische Revolution"
    A += [
        kurz("Um welches Jahr v. Chr. begannen die ersten Menschen, sesshaft zu werden?", schreibweisen_jahr(JUNG_BEGINN), s,
             info="Nach dem Heft begannen die ersten Menschen um 9000 v. Chr. sesshaft zu werden."),
        mc("Was bedeutet das Wort „sesshaft“?", "Man wohnt dauerhaft an einem festen Ort.",
           ["Man zieht mit den Tierherden umher.", "Man wechselt je nach Jahreszeit den Lagerplatz.", "Man wohnt nur im Winter in einer Höhle."], s,
           info="Sesshaft sind Menschen, die an einem Ort bleiben. Die Jäger und Sammler der Altsteinzeit waren nicht sesshaft."),
        mc("Wähle alle richtigen Antworten: Was gehörte zur neuen Lebensweise der ersten Bauern?",
           ["Ackerbau", "Viehzucht", "Vorratshaltung"],
           ["Ständig wechselnde Lagerplätze", "Wanderungen hinter den Tierherden her"], s,
           info="Die neue Lebensweise bestand aus Ackerbau, Viehzucht und Vorratshaltung. Wechselnde Lager und Wanderungen gehören zu den Jägern und Sammlern."),
        luecke("Ergänze den Text über den Beginn der neuen Lebensweise.",
               "Um {{9000}} v. Chr. begannen die ersten Menschen, {{sesshaft}} zu werden. Statt ihrer Nahrung hinterherzuziehen, betrieben sie {{Ackerbau|Viehzucht}} und {{Viehzucht|Ackerbau}} und legten {{Vorräte}} an.",
               s, extra=["Nomaden", "Wanderschaft"],
               info="Sesshaft werden heißt, an einem Ort zu bleiben. Dort bauten die Menschen Getreide an, hielten Tiere und legten Vorräte an."),
        mc("Warum spricht man von einer neolithischen (steinzeitlichen) „Revolution“?", "Weil sich das Leben der Menschen grundlegend änderte.",
           ["Weil die Menschen gegen ihre Anführer kämpften und sie stürzten.", "Weil innerhalb eines einzigen Jahres plötzlich alles anders wurde.", "Weil zwischen Jägern und Bauern ein großer Krieg ausbrach."], s,
           info="Revolution heißt hier nicht Aufstand, sondern grundlegender Wandel: vom Jagen und Sammeln zu Ackerbau, Viehzucht und Vorratshaltung.",
           tipp="Es geht nicht um einen Kampf."),
        tf("Das Leben der ersten Bauern veränderte sich nicht von heute auf morgen, sondern Schritt für Schritt.", True, s,
           info="Die neue Lebensweise brauchte Jahrhunderte und Jahrtausende, um sich zu verbreiten."),
        zuordnen("Ordne die Fachwörter zu.",
                 [("Paläolithikum", "Altsteinzeit"), ("Mesolithikum", "Mittelsteinzeit"), ("Neolithikum", "Jungsteinzeit"),
                  ("neolithische Revolution", "grundlegender Wandel zu Ackerbau und Viehzucht"), ("sesshaft", "dauerhaft an einem Ort wohnend")], s,
                 extra=["Wandel zu Jagen und Sammeln"],
                 info="„Neolithisch“ heißt jungsteinzeitlich. Paläo = alt, meso = mittel, neo = neu (jung).",
                 tipp="Alt, mittel, jung: Paläo, Meso, Neo."),
    ]
    # ------------------------------------------------------------------ D Fruchtbarer Halbmond
    s = "D – Der fruchtbare Halbmond und der Weg nach Europa"
    A += [
        kurz("Der Tigris ist einer der beiden großen Flüsse im Gebiet des fruchtbaren Halbmonds. Wie heißt der andere?", ["Euphrat", "der Euphrat"], s,
             info="Euphrat und Tigris fließen durch den Irak zum Persischen Golf."),
        mc("Wo begann die neolithische Revolution?", "Im heutigen Irak, an den Flüssen Euphrat und Tigris",
           ["In Mitteleuropa, in den Flusstälern von Rhein und Donau", "In Nordeuropa, an den Küsten von Nordsee und Ostsee", "Im Süden Afrikas, am Rand der großen Wüste"], s,
           info="Der Ausgangspunkt war der heutige Irak mit der fruchtbaren Gegend um Euphrat und Tigris."),
        luecke("Ergänze die Beschreibung.",
               "Das halbmondförmige Gebiet zwischen dem {{Mittelmeer|Persischen Golf}} und dem {{Persischen Golf|Mittelmeer}} nennt man den {{fruchtbaren Halbmond}}.",
               s, extra=["Schwarzen Meer", "Roten Meer"],
               info="Der fruchtbare Halbmond reicht vom Mittelmeer bis zum Persischen Golf."),
        mc("Wähle alle richtigen Antworten: Welche heutigen Länder gehören zum fruchtbaren Halbmond?", ["Irak", "Syrien", "Libanon"],
           ["Griechenland", "Spanien", "Polen"], s,
           info="Zum fruchtbaren Halbmond gehören heute Israel, Libanon, die Türkei, Syrien, der Irak und der Iran."),
        zuordnen("Was zeigt die Nummer auf der Skizze?",
                 [("Nummer 1", "Mittelmeer"), ("Nummer 2", "Persischer Golf"), ("Nummer 3", "Euphrat und Tigris"), ("Nummer 4", "fruchtbarer Halbmond")], s,
                 extra=["Schwarzes Meer"],
                 bild=svg_halbmond(True),
                 bildAlt="Vereinfachte Skizze: Nummer 1 im Mittelmeer links, Nummer 2 im Persischen Golf unten rechts, Nummer 3 bei den beiden Flüssen und Nummer 4 auf dem grünen Bogen des fruchtbaren Halbmonds.",
                 info="Das Mittelmeer liegt links (im Westen), der Persische Golf unten rechts. Der grüne Bogen dazwischen ist der fruchtbare Halbmond, die Flüsse fließen auf den Golf zu."),
        kurz("Ab wann etwa gab es in Mitteleuropa die ersten Ackerbauern? Nenne das Jahr v. Chr.", schreibweisen_jahr(ACKERBAU_MITTELEUROPA_J), s,
             info="In Mitteleuropa gibt es die ersten Ackerbauern ab ca. 5700 v. Chr. Man nennt sie Linienbandkeramische Kultur."),
        mc("Wie nennt man die erste Kultur der Ackerbauern in Mitteleuropa, benannt nach ihren verzierten Gefäßen?", "Linienbandkeramische Kultur",
           ["Faustkeilkultur der Altsteinzeit", "Rentierjäger-Kultur der Eiszeit", "Würm-Kultur der Kaltzeit"], s,
           info="Die Linienbandkeramische Kultur ist nach den verzierten Gefäßen ihrer Bauern benannt (Keramik = Gefäße aus Ton)."),
        tf("Schon um 9000 v. Chr. gab es in Mitteleuropa Ackerbauern.", False, s,
           info=f"Um 9000 v. Chr. begann es im Irak. In Mitteleuropa gibt es die ersten Bauern erst ab ca. 5700 v. Chr., also etwa {AUSBREITUNG_BIS_MITTELEUROPA} Jahre später.",
           tipp="Die neue Lebensweise breitete sich langsam aus."),
    ]
    # ------------------------------------------------------------------ E Haustiere und Pflanzen
    s = "E – Haustiere und Nutzpflanzen"
    A += [
        mc("Was bedeutet „Domestikation“?", "Wilde Tiere und Pflanzen werden gezähmt und genutzt.",
           ["Wilde Tiere und Pflanzen werden nur gejagt und gesammelt.", "Man legt große Vorräte für den Winter im Dorf an.", "Man brennt Wald ab, um Platz für Felder zu schaffen."], s,
           info="Bei der Domestikation fängt und zähmt man wilde Tiere und Pflanzen und macht sie für den Menschen nutzbar."),
        mc("Welches Beispiel zeigt eine Züchtung?", "Ein Bauer sät nur die Körner der besten Pflanzen aus.",
           ["Ein Jäger fängt ein wildes Schaf und sperrt es in ein Gehege.", "Eine Bäuerin mahlt Getreide auf dem Mahlstein zu Mehl.", "Ein Hirte treibt die Schafe am Morgen auf die Weide."], s,
           info="Züchtung heißt: gezielt Tiere und Pflanzen mit gewünschten Eigenschaften auswählen und fördern.",
           tipp="Bei der Züchtung wählt man gezielt aus."),
        reihenfolge("Ordne den Weg vom Wildtier zum Haustier.",
                    ["Menschen fangen wilde Tiere.", "Sie zähmen die Tiere und halten sie bei sich.", "Sie wählen Tiere mit nützlichen Eigenschaften aus.",
                     "Die Nachkommen werden weitergezüchtet, bis ein Haustier entsteht."], s,
                    info="Erst kommen Fangen und Zähmen (Domestikation), danach die gezielte Auswahl (Züchtung)."),
        zuordnen("Wozu nutzten die Menschen die Pflanze oder das Tier?",
                 [("Lein", "Öl und Fasern zum Spinnen"), ("Mohn", "Gewürz und Heilmittel"), ("Gerste", "Brot und Brei"),
                  ("Schaf", "Fleisch, Wolle und Milch"), ("Esel", "Reit-, Pack- und Zugtier")], s,
                 extra=["Waffe für die Jagd", "Schmuck aus Muscheln"],
                 info="Lein lieferte Öl und Fasern, Mohn Gewürz und Heilmittel, Gerste Brot und Brei. Schafe gaben Fleisch, Wolle und Milch, Esel trugen und zogen."),
        mc("Wähle alle richtigen Antworten: Welche Pflanzen bauten die Menschen in der Jungsteinzeit an?", ["Emmer", "Einkorn", "Lein"],
           ["Kartoffeln", "Mais"], s,
           info="Emmer und Einkorn sind Getreide, Lein liefert Öl und Fasern. Zusatz: Kartoffeln und Mais kamen erst nach der Entdeckung Amerikas (1492) nach Europa."),
        luecke("Ergänze den Text über das Schaf.",
               "Von Schafen gewann man Fleisch und {{Wolle}} für die Kleidung. Aus der {{Milch}} machte man {{Käse}}, der länger {{haltbar}} blieb.",
               s, extra=["Federn", "Eier"],
               info="Schafe lieferten Fleisch, Wolle und Milch. Aus Milch wurde Käse, und Käse hält sich länger."),
        tf("Die Menschen der Jungsteinzeit hörten ganz auf zu jagen, weil sie Haustiere hatten.", False, s,
           info="Tiere zu halten war weniger gefährlich als die Jagd. Gejagt wurde aber weiterhin."),
        kurz("Aus welcher Pflanze gewannen die Menschen Öl und Fasern zum Spinnen?", ["Lein", "der Lein", "Flachs"], s,
             info="Aus Lein gewann man Öl und Fasern. Zusatz: Lein heißt auch Flachs."),
        luecke("Ergänze den Text über die Haustiere.",
               "Der {{Hund}} wurde schon in der {{Altsteinzeit}} zum Haustier. Später kamen {{Schaf|Ziege|Rind|Schwein|Pferd}} und weitere Tiere dazu. Ab etwa 5000 v. Chr. nutzte man {{Esel|Pferd}} und {{Pferd|Esel}} als Reit-, Pack- und Zugtiere.",
               s, extra=["Mammut", "Luchs"],
               info="Der Hund ist das älteste Haustier der Liste (vor ca. 14 000 Jahren). Esel und Pferd als Reit-, Pack- und Zugtiere gibt es ab ca. 5000 v. Chr."),
    ]
    # ------------------------------------------------------------------ F Pflug, Rad, Rechnen
    s = "F – Pflug, Rad und Rechnen mit Jahren"
    A += [
        mc("Welcher Zeitraum gehört nach dem Heft zur Jungsteinzeit?", f"ca. {JUNG_BEGINN} bis ca. {JUNG_ENDE} v. Chr.",
           [f"ca. {JUNG_ENDE} bis 1000 v. Chr.", f"bis ca. {ALT_ENDE} v. Chr.", "ca. 1000 v. Chr. bis 500 n. Chr."], s,
           info="Die Altsteinzeit reicht bis ca. 9000 v. Chr., danach folgt die Jungsteinzeit bis ca. 3000 v. Chr.",
           tipp="Die Altsteinzeit endet dort, wo die Jungsteinzeit beginnt."),
        mc("Wozu benutzt man einen Pflug?", "Er lockert den Boden für die Saat.",
           ["Er mahlt die Getreidekörner zu Mehl.", "Er zerschneidet das Fleisch der Beute.", "Er trägt die Ernte vom Feld nach Hause."], s,
           info="Der Pflug lockert den Boden, bevor man aussät (Zusatz zum Heft). In Mitteleuropa gibt es ihn seit etwa 4500 v. Chr."),
        tf("Die Jungsteinzeit gehört zur Epoche „Ur- und Frühgeschichte“.", True, s,
           info="Die Ur- und Frühgeschichte reicht bis 3000 v. Chr. Die Jungsteinzeit endet um 3000 v. Chr. und gehört deshalb dazu."),
        zuordnen("Welches Ereignis gehört zu welchem Buchstaben? Lies die Jahre unter dem Zeitstrahl ab.",
                 [("Buchstabe A", "Menschen werden sesshaft"), ("Buchstabe B", "Keramik"), ("Buchstabe C", "Ackerbau in Mitteleuropa"),
                  ("Buchstabe D", "Esel und Pferd als Reit- und Packtiere"), ("Buchstabe E", "Pflug in Mitteleuropa"), ("Buchstabe F", "Rad")], s,
                 extra=["Feuer wird genutzt"],
                 bild=svg_strahl(False),
                 bildAlt="Zeitstrahl mit den Buchstaben A bis F bei den Jahren 9000, 7000, 5700, 5000, 4500 und 3000 v. Chr. Die Altsteinzeit reicht bis 9000 v. Chr., die Jungsteinzeit bis 3000 v. Chr.",
                 info="9000 sesshaft, 7000 Keramik, 5700 Ackerbau in Mitteleuropa, 5000 Esel und Pferd, 4500 Pflug, 3000 Rad."),
        reihenfolge("Ordne die Ereignisse von früh nach spät.", [t for y, t in EREIGNISSE if y in (JUNG_BEGINN, KERAMIK_J, ACKERBAU_MITTELEUROPA_J, PFLUG_J, RAD_J)], s,
                    info="Bei Jahren v. Chr. ist die größere Zahl die frühere: 9000, 7000, 5700, 4500, 3000.",
                    tipp="Das Rad kam zuletzt."),
        kurz(f"Wie viele Jahre dauerte die Jungsteinzeit von {JUNG_BEGINN} bis {JUNG_ENDE} v. Chr.?", schreibweisen_zahl(DAUER_JUNGSTEINZEIT), s, einheit="Jahre",
             info=f"Bei Jahren v. Chr. ziehst du ab: {JUNG_BEGINN} − {JUNG_ENDE} = {DAUER_JUNGSTEINZEIT} Jahre.",
             tipp="Bei zwei Jahren vor Christus ziehst du die kleinere von der größeren Zahl ab."),
        mc(f"Um {JUNG_BEGINN} v. Chr. begann die neue Lebensweise im Irak. Ab {ACKERBAU_MITTELEUROPA_J} v. Chr. gab es Ackerbau in Mitteleuropa. Wie viele Jahre liegen dazwischen?",
           f"{AUSBREITUNG_BIS_MITTELEUROPA} Jahre", [f"{tausend(JUNG_BEGINN + ACKERBAU_MITTELEUROPA_J)} Jahre", f"{JUNG_BEGINN - ACKERBAU_MITTELEUROPA_J + 400} Jahre", f"{AUSBREITUNG_BIS_MITTELEUROPA // 10} Jahre"], s,
           info=f"Beide Jahre liegen vor Christi Geburt, also ziehst du ab: {JUNG_BEGINN} − {ACKERBAU_MITTELEUROPA_J} = {AUSBREITUNG_BIS_MITTELEUROPA}. Die Ausbreitung dauerte mehr als 3000 Jahre.",
           tipp="Beide Jahre liegen vor Christi Geburt: abziehen, nicht addieren."),
        kurz(f"Etwa wie viele Jahre ist es her, dass die ersten Menschen sesshaft wurden ({JUNG_BEGINN} v. Chr.)? Rechne mit dem Jahr {HEUTE} und wie in der Schule ohne Jahr 0.",
             ABSTAND_NAEHERUNG, s, einheit="Jahre",
             info=f"Von {JUNG_BEGINN} v. Chr. bis Christi Geburt vergehen {JUNG_BEGINN} Jahre, danach noch {HEUTE}: {JUNG_BEGINN} + {HEUTE} = {tausend(ABSTAND_9000_HEUTE)} Jahre, also etwa {tausend(ABSTAND_RUND)} Jahre. Das passt zum Buch: vor rund 10 000 bis 11 000 Jahren.",
             tipp="Von v. Chr. bis heute addierst du."),
    ]
    # ------------------------------------------------------------------ G Klausurnah
    s = "G – Klausurnah: Erklären und Begründen"
    A += [
        luecke("Fasse zusammen: vom Ende der Eiszeit zur neolithischen Revolution.",
               "Als die {{Eiszeit}} endete, wurde es wärmer und {{Mischwälder}} breiteten sich aus. Um {{9000}} v. Chr. begannen im Gebiet des {{fruchtbaren Halbmonds}} die ersten Menschen, {{sesshaft}} zu werden. "
               "Sie lebten von {{Ackerbau|Viehzucht}} und {{Viehzucht|Ackerbau}}. Diesen grundlegenden Wandel nennt man neolithische {{Revolution}}.",
               s, extra=["Aufstand", "Nomaden"],
               info="Die Zusammenfassung verbindet Klima, Ort, Zeit und Lebensweise: Warmzeit, fruchtbarer Halbmond, um 9000 v. Chr., Ackerbau und Viehzucht."),
        mc("Eine Mitschülerin sagt: „Um 9000 v. Chr. gab es in Mitteleuropa schon Bauern.“ Wie korrigierst du sie?",
           "Es begann um 9000 v. Chr. im Irak. In Mitteleuropa gab es Bauern erst ab ca. 5700 v. Chr.",
           ["Es begann um 9000 v. Chr. in Mitteleuropa. Im Irak gab es Bauern erst ab ca. 5700 v. Chr.", "Bauern gab es erst, nachdem das Rad erfunden worden war. Das geschah um 3000 v. Chr.", "Um 9000 v. Chr. gab es überall auf der Welt schon Bauern, auch in Mitteleuropa und im Irak."], s,
           info=f"Die neue Lebensweise begann im Irak und brauchte etwa {AUSBREITUNG_BIS_MITTELEUROPA} Jahre bis Mitteleuropa."),
        frei("Erkläre, was man unter der neolithischen (steinzeitlichen) Revolution versteht. Gehe darauf ein, warum man von einer „Revolution“ spricht.",
             "Um 9000 v. Chr. begannen die ersten Menschen, sesshaft zu werden. Sie zogen nicht mehr ihrer Nahrung hinterher, sondern betrieben Ackerbau und Viehzucht und legten Vorräte an. "
             "Man spricht von einer Revolution, weil sich das Leben grundlegend änderte. Gemeint ist kein Aufstand, sondern ein tiefer Wandel, der Schritt für Schritt geschah.",
             ["sesshaft werden um 9000 v. Chr. genannt", "Ackerbau, Viehzucht und Vorratshaltung genannt", "Revolution = grundlegender Wandel, kein Aufstand", "Wandel geschah Schritt für Schritt oder veränderte das Leben dauerhaft"], 4, s,
             tipp="Denke an die Lebensweise vorher und nachher."),
        frei("Beschreibe, wo die neolithische Revolution begann und wie sie sich nach Europa ausbreitete.",
             "Sie begann im heutigen Irak, im Gebiet der Flüsse Euphrat und Tigris, im fruchtbaren Halbmond zwischen dem Mittelmeer und dem Persischen Golf. "
             "Von dort breitete sie sich über Jahrhunderte und Jahrtausende nach Westen und Norden aus. In Mitteleuropa gab es die ersten Ackerbauern ab etwa 5700 v. Chr. (Linienbandkeramische Kultur).",
             ["Irak, Euphrat und Tigris genannt", "fruchtbarer Halbmond zwischen Mittelmeer und Persischem Golf", "langsame Ausbreitung nach Westen und Norden", "Mitteleuropa ab ca. 5700 v. Chr."], 4, s),
        frei("Erkläre, was sich am Ende der Eiszeit veränderte und was das für die Menschen bedeutete (Klima, Pflanzen, Tiere, Jagd).",
             "Am Ende der Eiszeit wurde es wärmer und es regnete mehr. Die Gletscher schmolzen, der Meeresspiegel stieg, und Mischwälder ersetzten die Steppe. "
             "Kälteliebende Tiere zogen nach Norden oder verschwanden, im Wald lebten nun zum Beispiel Hirsch, Reh und Wildschwein. Die Jagd im Wald war schwerer, dabei halfen Pfeil und Bogen. "
             "Das warme, regenreiche Klima machte außerdem den Anbau von Getreide möglich.",
             ["wärmer, Gletscher schmelzen, Meeresspiegel steigt", "Mischwälder statt Steppe", "Tiere ändern sich (Kältetiere ziehen weg, Waldtiere)", "Jagd im Wald, Pfeil und Bogen, oder Getreideanbau möglich"], 4, s,
             tipp="Gehe der Reihe nach vor: Klima, Pflanzen, Tiere, Menschen."),
        frei("Nenne vier Pflanzen oder Tiere, die die Menschen in der Jungsteinzeit anbauten oder hielten, und erkläre bei zwei davon, wozu man sie nutzte.",
             "Zum Beispiel Gerste, Lein, Schaf und Ziege. Gerste gab Getreide für Brot und Brei. Das Schaf lieferte Fleisch, Wolle und Milch, aus der man Käse machte, der länger haltbar war.",
             ["vier richtige Pflanzen oder Tiere genannt", "Nutzung bei der ersten richtig erklärt", "Nutzung bei der zweiten richtig erklärt"], 3, s),
    ]
    # Verweise auf das Lernblatt je Aufgabe (Feinschliff)
    lesen = {
        "B": {3: L_EIS},
        "C": {6: [L_MITTEL, L_REV]},
        "E": {0: L_TIER, 1: L_TIER, 2: L_TIER, 3: [L_TIER, L_PFL], 4: L_PFL, 5: L_TIER, 6: L_TIER, 7: L_PFL, 8: L_TIER},
        "F": {0: L_ZEIT, 1: L_PFLUG, 2: L_ZEIT, 3: L_ZEIT, 4: L_ZEIT, 5: L_ZEIT, 6: L_ZEIT, 7: L_ZEIT},
        "G": {0: [L_EIS, L_REV, L_HALB], 1: L_HALB, 2: L_REV, 3: L_HALB, 4: L_EIS, 5: [L_TIER, L_PFL]},
    }
    _lesen_setzen(A, lesen)
    return A


def _lesen_setzen(A, lesen):
    """Setzt das Feld „lesen“ je Aufgabe. lesen: {Blockbuchstabe: {Nummer im Block ab 0: Titel oder Liste}}."""
    blocks = {}
    for t in A:
        blocks.setdefault(t["abschnitt"][0], []).append(t)
    for b, m in lesen.items():
        for i, titel in m.items():
            blocks[b][i]["lesen"] = titel


def paket_5a():
    p = pack("geschichte-5a-neolithische-revolution", "Geschichte Teil 5a: Die Neolithische Revolution",
             "Ende der Eiszeit, Mittelsteinzeit, sesshaft werden um 9000 v. Chr., fruchtbarer Halbmond, Haustiere und Nutzpflanzen, Pflug und Rad, Rechnen mit Jahren. Mit Lernblatt, Zeichnungen und Übungsaufgaben.",
             lernblatt_5a(), aufgaben_5a(), min_aufgaben=42,
             hinweis="Die Jahreszahlen folgen dem Heft (Jungsteinzeit ca. 9000 bis 3000 v. Chr.). Das Buch nennt den Beginn der Warmzeit „vor rund 10 000 bis 11 000 Jahren“ und teilt die Steinzeit in drei Teile (mit Mittelsteinzeit). Beides gilt.")
    assert 42 <= len(p["aufgaben"]) <= 55, len(p["aufgaben"])
    L = {s["titel"] for s in p["lernblatt"]}
    nachlesen(p, {
        "A – Das Ende der Eiszeit": "Das Ende der Eiszeit",
        "B – Die Mittelsteinzeit": "Die Mittelsteinzeit: Jäger im Wald",
        "C – Sesshaft werden: die neolithische Revolution": "Sesshaft werden: die neolithische Revolution",
        "D – Der fruchtbare Halbmond und der Weg nach Europa": "Der fruchtbare Halbmond und der Weg nach Europa",
        "E – Haustiere und Nutzpflanzen": ["Haustiere: Domestikation und Züchtung", "Nutzpflanzen der ersten Bauern"],
        "F – Pflug, Rad und Rechnen mit Jahren": ["Pflug und Rad", "Zeitstrahl und Rechnen mit Jahren"],
        "G – Klausurnah: Erklären und Begründen": ["Das Ende der Eiszeit", "Sesshaft werden: die neolithische Revolution", "Der fruchtbare Halbmond und der Weg nach Europa",
                                                  "Haustiere: Domestikation und Züchtung", "Nutzpflanzen der ersten Bauern"],
    })
    p["probe"] = False
    return p


# ====================================================================== Paket 5b

# Gruppengröße der Jäger und Sammler (Heft: etwa 25 bis 30 Personen), natürliche Schreibweisen im Code erzeugt
GRUPPENGROESSE = _ohne_doppelte(
    [f"{k}{suf}" for k in ("25 bis 30", "25-30", "25–30", "25 - 30", "25 – 30") for suf in ("", " Personen")]
    + [f"{pre}{k}{suf}" for k in ("25 bis 30", "25-30") for pre in ("etwa ", "ca. ", "ungefähr ") for suf in ("", " Personen")]
    + ["25", "30", "ca. 30", "etwa 30", "30 Personen"])

# Alter von Erfindungen in Jahren vor heute (für „Ordne nach dem Alter“): Steinwerkzeuge 2 Mio., Feuer nutzen 1,5 Mio., Nähnadel 24 000, dann die Jahre v. Chr. plus HEUTE
ALTER_ERFINDUNGEN = [
    ("Einfache Steinwerkzeuge (vor ca. 2 Millionen Jahren)", 2_000_000),
    ("Feuer hüten und nutzen (vor ca. 1,5 Millionen Jahren)", 1_500_000),
    ("Nähnadel aus Knochen (vor ca. 24 000 Jahren)", 24_000),
    ("Keramik (ca. 7000 v. Chr.)", KERAMIK_J + HEUTE),
    ("Pflug in Mitteleuropa (ca. 4500 v. Chr.)", PFLUG_J + HEUTE),
    ("Rad (um 3000 v. Chr.)", RAD_J + HEUTE),
]
assert [a for _, a in ALTER_ERFINDUNGEN] == sorted((a for _, a in ALTER_ERFINDUNGEN), reverse=True)


def lernblatt_5b():
    return [
        lb("Leben im Dorf der Jungsteinzeit",
           "Die ersten Bauern wohnten nicht mehr in Zelten, die man immer wieder abbaut, sondern in **Dörfern**. Ihre Häuser waren größer und fester. Oft waren es **Langhäuser** mit einem Dach aus Stroh. Im Dorf lagerten die **Vorräte**, und die Tiere gehörten dazu.\n"
           "Im Dorf hatte jeder eine Aufgabe. Diese **Arbeitsteilung** führte zu **Berufen**:\n"
           "- **Bauern** bauten Getreide an und brachten die Ernte ein.\n"
           "- **Schäfer** hüteten Schafe und andere Tiere.\n"
           "- **Töpfer** formten Gefäße aus Ton.\n"
           "- **Handwerker** stellten Werkzeuge her, zum Beispiel geschliffene Steinbeile.\n"
           "Woher wissen wir das? Funde wie Mahlsteine oder Scherben von Tontöpfen sind **Sachquellen**, denn sie stammen aus der Zeit selbst. Eine Zeichnung, die Menschen viel später nach solchen Funden gemacht haben, ist dagegen eine **Darstellung**.",
           merke="Dorf mit Langhäusern, Vorräten und Tieren. Jeder hat eine Aufgabe (Arbeitsteilung): Bauer, Schäfer, Töpfer, Handwerker. Funde sind Quellen, spätere Zeichnungen sind Darstellungen.",
           bild=svg_dorf(False),
           bildAlt="Erfundene Skizze eines Dorfs der Jungsteinzeit von oben: mehrere Langhäuser mit Strohdach, eine Töpferei mit Töpfen, rechts oben ein Acker mit Furchen, rechts unten eine Weide mit Schafen und links oben ein Wald."),
        lb("Spinnen, Weben, Töpfern und Mahlen",
           "Die Menschen der Jungsteinzeit erfanden viele Dinge für den Alltag im Dorf:\n"
           "- **Spinnen und Weben**: Aus Wolle und Lein spann man Fäden und webte daraus auf dem **Webstuhl** (einem Gerät zum Weben, mit Gewichten) Stoffe. So entstanden Kleidung und Decken.\n"
           f"- **Keramik**: Aus Ton formte man Töpfe, Becher und Näpfe. Man konnte darin kochen und Essen aufbewahren. Keramik gibt es seit etwa {KERAMIK_J} v. Chr.\n"
           "- **Mahlstein und Reibstein**: Damit mahlte man Getreidekörner. Aus dem Mehl wurden Brot und Brei.",
           merke="Spinnen und Weben: Stoffe. Keramik: Kochen und Aufbewahren. Mahlstein und Reibstein: Getreide mahlen."),
        lb("Beil, Pflug und Rad",
           "Auch bei Werkzeugen und Geräten tat sich viel:\n"
           "- **Geschliffene Beile**: Früher hatte man Steine nur grob zurechtgeschlagen. Jetzt schliff man Steinäxte und Steinbeile glatt. Mit **Bohrungen** im Stein konnte man ihn am **Schaft** (dem Stiel) befestigen.\n"
           f"- **Pflug**: Er lockert den Boden für die Saat. Die ersten Pflüge waren aus Holz. In Mitteleuropa gibt es den Pflug seit etwa {PFLUG_J} v. Chr.\n"
           f"- **Rad**: Es wurde um {RAD_J} v. Chr. erfunden, also viel später als der Ackerbau und die Keramik.",
           merke="Geschliffene Beile mit Bohrung zum Befestigen am Schaft. Pflug seit ca. 4500 v. Chr. in Mitteleuropa, Rad um 3000 v. Chr."),
        lb("Folgen der neuen Lebensweise",
           "Das Leben als Bauer hatte viele Folgen:\n"
           "- Mit **Vorräten** waren die Menschen **unabhängiger von der Umwelt**. Sie hatten auch dann zu essen, wenn gerade keine Beute da war.\n"
           "- **Besitz** führte zu **Neid und Streit**.\n"
           "- Der Mensch **veränderte die Umwelt**: Durch **Brandrodung** (Wald wird abgebrannt, um Platz zu schaffen) entstanden **Felder** und **Weideflächen**.\n"
           "- Die Menschen hingen von der Ernte ab. Bei **Ernteausfällen** drohten **Hungersnöte**. Am Anfang war das Essen auch einseitig.\n"
           "- Trotzdem nahm die Bevölkerung stetig zu. Deshalb mussten neue Siedlungen und Ackerflächen angelegt werden.",
           merke="Folgen: Vorräte (unabhängiger), Besitz (Neid und Streit), Umweltveränderung (Brandrodung, Felder, Weiden), Hungersnöte bei Ernteausfall, mehr Menschen."),
        lb("Vorteile und Nachteile abwägen",
           "**Abwägen** heißt: Du sammelst Vorteile und Nachteile und kommst dann zu einem begründeten Urteil. Für die neue Lebensweise:\n"
           "- **Vorteile**: Vorräte machen unabhängiger von der Umwelt. Die Häuser sind größer und fester. Tiere halten ist weniger gefährlich als jagen. Durch Arbeitsteilung entstehen Berufe.\n"
           "- **Nachteile**: Bei Ernteausfällen drohen Hungersnöte. Das Essen ist am Anfang einseitig. Besitz führt zu Neid und Streit. Der Mensch verändert die Landschaft.\n"
           "Ein gutes Urteil nennt beide Seiten und sagt dann, was überwiegt. Zum Beispiel: „Die neue Lebensweise hatte viele Vorteile, aber sie brachte auch neue Gefahren.“",
           merke="Erst Vorteile und Nachteile nennen, dann ein Urteil mit Begründung."),
        lb("Die Altsteinzeit in Kürze",
           "Für den Vergleich musst du die Altsteinzeit gut kennen. Das war die Zeit der **Jäger und Sammler**:\n"
           "- **Nahrung**: Sie jagten Großwild wie Ren, Pferd, Bison und Wollnashorn, fischten und sammelten Beeren, Körner, Pilze, Wurzeln und Nüsse.\n"
           "- **Wohnen**: Sie waren nicht sesshaft. Als **Nomaden** (Menschen ohne festen Wohnsitz) zogen sie in kleinen Gruppen von etwa 25 bis 30 Personen umher und folgten den Beutetieren. Sie lebten in Zelten aus Fell und Stangen, manchmal in Höhlen.\n"
           "- **Erfindungen**: Faustkeil, Speer, Speerschleuder, Pfeil und Bogen, Nähnadel, Feuer. Die ersten einfachen Steinwerkzeuge gab es schon vor etwa 2 Millionen Jahren, Feuer nutzte man seit etwa 1,5 Millionen Jahren, Nähnadeln gibt es seit etwa 24 000 Jahren.\n"
           "- **Kleidung**: aus Fellen und Leder.\n"
           "- **Gefahren**: Raubtiere, Kälte, Jagdunfälle und Nahrungsmangel. Fleisch konnten sie schon haltbar machen und in Depots (Vorratslagern) aufbewahren.",
           merke="Altsteinzeit: Jagen und Sammeln, Nomaden in kleinen Gruppen, Zelte, Felle, Gefahr durch Raubtiere und Kälte."),
        lb("Altsteinzeit und Jungsteinzeit im Vergleich",
           "Das Bild zeigt den Vergleich in sieben Zeilen. Merke dir die Stichwörter: Nahrungserwerb, Nahrung, Erfindungen, Aufenthaltsorte, Gefahren, Bekleidung, Lebensweise.\n"
           "Der Kern: Aus Jägern und Sammlern, die ihrer Nahrung hinterherzogen, wurden sesshafte Bauern, die ihre Nahrung selbst erzeugten. Davon hängt vieles in der Tabelle ab: Dorf statt Zelt, Berufe statt Wanderung.\n"
           "Beachte: In der Jungsteinzeit wurde auch weiter gejagt, und schon die Eiszeitjäger legten Fleischdepots an. Es sind also Schwerpunkte, keine strengen Gegensätze.",
           merke="Kern des Vergleichs: nomadische Jäger und Sammler (Altsteinzeit) gegen sesshafte Bauern (Jungsteinzeit).",
           bild=svg_vergleich(True),
           bildAlt="Tabelle mit sieben Zeilen. Nahrungserwerb: Jagen und Sammeln gegen Ackerbau und Viehzucht. Nahrung: Fleisch, Fisch, Beeren, Wurzeln, Pilze, Nüsse gegen Getreide, Milch, Käse, Fleisch der Haustiere. Erfindungen: Faustkeil, Speer, Speerschleuder, Pfeil und Bogen, Nähnadel, Feuer gegen Pflug, Keramik, Webstuhl, Mahlstein, geschliffene Beile, Rad. Aufenthaltsorte: wechselnde Lagerplätze, Zelte, Höhlen gegen feste Dörfer mit Häusern. Gefahren: Raubtiere, Kälte, Jagdunfälle, Nahrungsmangel gegen Missernten, Hunger, Streit um Besitz. Bekleidung: Felle und Leder gegen gewebte Stoffe neben Fellen. Lebensweise: Nomaden in kleinen Gruppen gegen sesshaft mit Arbeitsteilung und Berufen."),
        lb("Gegensätze und Vergleiche aufschreiben",
           "Gegensatzpaare helfen beim Lernen. Links steht die Altsteinzeit, rechts die Jungsteinzeit:\n"
           "- Nomaden – sesshaft\n"
           "- Zelt – festes Haus im Dorf\n"
           "- Jagen und Sammeln – Ackerbau und Viehzucht\n"
           "- nur Felle und Leder – auch gewebte Stoffe\n"
           "- Gefahr durch Raubtiere und Kälte – Gefahr durch Missernten und Streit um Besitz\n"
           "Wenn du **vergleichen** sollst, nennst du immer beide Seiten und verbindest sie mit Wörtern wie „dagegen“, „während“ oder „im Unterschied dazu“. Beispiel: „In der Altsteinzeit lebten die Menschen als Nomaden in Zelten. In der Jungsteinzeit dagegen waren sie sesshaft und wohnten in Dörfern.“\n"
           "Wenn du dich in eine Person hineinversetzen sollst (Rollenspiel), schreibst du aus ihrer Sicht. Du benutzt aber nur Dinge, die es zu ihrer Zeit wirklich gab.",
           merke="Beim Vergleich immer beide Zeiten nennen und mit „dagegen“ oder „während“ verbinden."),
    ]


def aufgaben_5b():
    A = []
    L_DORF = "Leben im Dorf der Jungsteinzeit"
    L_HAUSH = "Spinnen, Weben, Töpfern und Mahlen"
    L_WERK = "Beil, Pflug und Rad"
    L_FOLGEN = "Folgen der neuen Lebensweise"
    L_ABW = "Vorteile und Nachteile abwägen"
    L_ALT = "Die Altsteinzeit in Kürze"
    L_VGL = "Altsteinzeit und Jungsteinzeit im Vergleich"
    L_GEG = "Gegensätze und Vergleiche aufschreiben"

    # ------------------------------------------------------------------ A Leben im Dorf
    s = "A – Leben im Dorf"
    A += [
        mc("Wie wohnten die Menschen in der Jungsteinzeit?", "In festen Dörfern, oft in Langhäusern mit Strohdach.",
           ["In Zelten, die sie je nach Jahreszeit abbauten.", "In Höhlen, die sie mit Fellen auskleideten.", "In wechselnden Lagern, immer dort, wo gerade Beute war."], s,
           info="Die ersten Bauern waren sesshaft und bauten Dörfer mit größeren, festeren Häusern. Zelte und wechselnde Lager gehören zur Altsteinzeit."),
        zuordnen("Welche Aufgabe gehört zu welchem Beruf im Dorf?",
                 [("Bauer", "baut Getreide an und erntet es"), ("Schäfer", "hütet Schafe"), ("Töpfer", "formt Gefäße aus Ton"),
                  ("Handwerker", "schleift Steinbeile und stellt Werkzeuge her")], s,
                 extra=["jagt Rentiere in der Steppe"],
                 info="Im Dorf hatte jeder einen Job: Ernte, Schäfer, Töpfer und andere Handwerker. Der Töpfer arbeitet mit Ton, der Handwerker mit Stein und Holz."),
        tf("Mit der neuen Lebensweise im Dorf entstanden Berufe, zum Beispiel Töpfer und Handwerker.", True, s,
           info="Jeder im Dorf übernahm eine Aufgabe. Diese Arbeitsteilung führte zu Berufen."),
        kurz("Wie nennt man es, wenn die Menschen eines Dorfes verschiedene Aufgaben übernehmen?", ["Arbeitsteilung", "die Arbeitsteilung"], s,
             info="Bei der Arbeitsteilung macht nicht jeder alles, sondern jeder hat eine eigene Aufgabe. So entstehen Berufe."),
        mc("Wähle alle richtigen Antworten: Was gehörte zu einem Dorf der Jungsteinzeit?",
           ["Lange Häuser mit Strohdach", "Felder für den Ackerbau", "Weiden für die Tiere"],
           ["Zelte aus Fell, die man abbaute", "Höhlen mit Wandmalereien"], s,
           info="Zum Dorf gehörten feste Häuser, Felder und Weideflächen. Zelte und Höhlen sind Wohnorte der Altsteinzeit."),
        luecke("Ergänze den Text über das Dorf.",
               "In der Jungsteinzeit bauten die Menschen {{größere|festere}} und {{festere|größere}} Häuser. Sie siedelten in {{Dörfern}} und legten {{Vorräte}} an.",
               s, extra=["Höhlen", "kleinere"],
               info="Die sesshaften Bauern bauten größere und festere Häuser als die Zelte der Jäger und legten Vorräte an."),
        zuordnen("Was zeigt die Nummer auf der Skizze eines Dorfs?",
                 [("Nummer 1", "Langhaus"), ("Nummer 2", "Acker"), ("Nummer 3", "Weide mit Schafen"), ("Nummer 4", "Töpferei"), ("Nummer 5", "Wald")], s,
                 extra=["Höhle"],
                 bild=svg_dorf(True),
                 bildAlt="Erfundene Skizze eines Dorfs von oben. Nummer 1 ist ein langes Haus mit Strohdach links, Nummer 2 ein Acker mit Furchen rechts oben, Nummer 3 eine Weide mit Schafen rechts unten, Nummer 4 ein kleines Haus mit Töpfen in der Mitte oben, Nummer 5 ein Wald links oben.",
                 info="Der lange Bau mit Strohdach ist das Langhaus, der gefurchte Streifen der Acker, die eingezäunte Fläche mit Schafen die Weide und das Haus mit Töpfen die Töpferei."),
        kurz("Woraus bestand das Dach der Langhäuser?", ["Stroh", "Strohdach", "aus Stroh", "ein Strohdach"], s,
             info="Die Langhäuser der Jungsteinzeit hatten ein Strohdach."),
    ]
    # ------------------------------------------------------------------ B Erfindungen
    s = "B – Erfindungen und ihre Bedeutung"
    A += [
        zuordnen("Welche Erfindung passt zu welchem Nutzen?",
                 [("Spinnen und Weben", "Stoffe für Kleidung und Decken"), ("Keramik", "Gefäße zum Kochen und Aufbewahren"), ("Mahlstein", "Getreide mahlen"),
                  ("Bohrung im Stein", "Stein am Schaft befestigen"), ("Pflug", "Boden für die Saat lockern")], s,
                 extra=["Feuer entzünden", "Höhlen bemalen"],
                 info="Webstuhl, Keramik, Mahlstein, Bohrung und Pflug machten das Leben im Dorf leichter. (Der Nutzen des Pflugs ist ein Zusatz zum Heft.)"),
        mc("Welche Erfindung der Jungsteinzeit machte es möglich, Stoffe für Kleidung und Decken herzustellen?", "Spinnen und Weben mit dem Webstuhl",
           ["Töpfern von Gefäßen aus Ton", "Mahlen von Getreide auf dem Mahlstein", "Pflügen der Felder mit dem Holzpflug"], s,
           info="Aus Wolle und Lein spann man Fäden und webte sie auf dem Webstuhl zu Stoff."),
        kurz("Aus welchem Material formte man Töpfe, Becher und Näpfe?", ["Ton", "aus Ton", "der Ton"], s,
             info="Keramik sind Gefäße aus Ton. Man konnte darin kochen und Essen aufbewahren."),
        mc("Wozu dienten die Bohrungen in den geschliffenen Steinbeilen?", "Man konnte den Stein am Schaft befestigen.",
           ["Sie machten die Klinge schärfer und glatter.", "Sie machten das Beil leichter und handlicher.", "Man konnte das Beil als Schmuck um den Hals tragen."], s,
           info="Durch das gebohrte Loch ließ sich der Stein am Schaft befestigen. Geschliffen wurden die Beile, damit sie glatt waren."),
        tf("Steinbeile wurden in der Jungsteinzeit geschliffen. Vorher hatte man sie nur zurechtgeschlagen.", True, s,
           info="Geschliffene Steinäxte und Steinbeile sind eine Neuerung der Jungsteinzeit."),
        reihenfolge("Ordne diese Erfindungen nach ihrem Alter. Die älteste steht oben.", [t for t, _ in ALTER_ERFINDUNGEN], s,
                    info=f"Steinwerkzeuge sind am ältesten, dann Feuer und Nähnadel. Die Jahre v. Chr. rechnest du auf „Jahre vor heute“ um (zum Beispiel {RAD_J} + {HEUTE} = {RAD_J + HEUTE} Jahre beim Rad).",
                    tipp=f"Rechne die Jahre v. Chr. in „Jahre vor heute“ um: Du addierst {HEUTE}."),
        kurz("Seit welchem Jahr v. Chr. gibt es ungefähr Keramik?", schreibweisen_jahr(KERAMIK_J), s,
             info="Keramik gibt es seit etwa 7000 v. Chr."),
        luecke("Ergänze den Text über die Erfindungen.",
               "Mit dem {{Webstuhl}} stellte man {{Stoffe}} aus Wolle und {{Lein}} her. In Töpfen aus {{Ton}} konnte man Essen kochen und {{aufbewahren}}.",
               s, extra=["Fell", "Faustkeil"],
               info="Webstuhl und Töpferei gehören zu den Neuerungen der Jungsteinzeit."),
        kurz("Womit mahlten die Menschen das Getreide?", ["Mahlstein", "Reibstein", "der Mahlstein", "der Reibstein", "Mahlstein und Reibstein"], s,
             info="Getreidekörner wurden auf Mahlsteinen und Reibsteinen gemahlen. Aus dem Mehl wurden Brot und Brei."),
        reihenfolge("Vom Korn zum Brei: Ordne die Arbeitsschritte.",
                    ["Getreide aussäen", "Das reife Getreide ernten", "Die Körner auf dem Mahlstein mahlen", "Aus dem Mehl im Tontopf Brei kochen"], s,
                    info="Erst wächst das Getreide, dann wird gemahlen, und zum Schluss kocht man im Tontopf den Brei.",
                    tipp="Ohne Ernte gibt es nichts zu mahlen."),
    ]
    # ------------------------------------------------------------------ C Folgen
    s = "C – Folgen der neuen Lebensweise"
    A += [
        mc("Warum machten Vorräte die Menschen unabhängiger von der Umwelt?",
           "Sie hatten auch dann zu essen, wenn nichts wuchs oder keine Beute da war.",
           ["Sie schützten die Menschen vor Raubtieren und vor der Kälte im Winter.", "Sie ersetzten die Arbeit auf den Feldern, sodass man nichts mehr anbauen musste.", "Sie sorgten dafür, dass die Ernte nie ausfiel und alle Tiere gesund blieben."], s,
           info="Mit Vorräten überbrückte man schlechte Zeiten. Man war nicht mehr jeden Tag auf das Glück bei Jagd und Sammeln angewiesen."),
        kurz("Wie nennt man es, wenn man Wald abbrennt, um Platz für Felder und Weiden zu schaffen?", ["Brandrodung", "die Brandrodung"], s,
             info="Die Brandrodung ist ein Beispiel dafür, wie die Bauern die Umwelt veränderten. Dadurch entstanden Felder und Weideflächen. (Dass dabei Wald abgebrannt wird, ist ein Zusatz zum Heft.)"),
        mc("Wähle alle richtigen Antworten: Wie veränderten die Menschen der Jungsteinzeit ihre Umwelt?",
           ["Sie rodeten Wald durch Brandrodung.", "Sie legten Felder an.", "Sie schufen Weideflächen für ihre Tiere."],
           ["Sie ließen die Landschaft so, wie sie war."], s,
           info="Der Mensch veränderte die Umwelt durch Brandrodung, Felder und Weideflächen."),
        luecke("Ergänze den Text über die Folgen für die Umwelt.",
               "Der Mensch veränderte die Umwelt: Durch {{Brandrodung}} entstanden {{Felder|Weideflächen}} und {{Weideflächen|Felder}}. Weil die {{Bevölkerung}} stetig wuchs, mussten neue {{Siedlungen}} und Ackerflächen angelegt werden.",
               s, extra=["Gletscher", "Nomaden"],
               info="Mehr Menschen brauchten mehr Platz und mehr Nahrung. Darum entstanden neue Dörfer und Felder."),
        tf("Dank der Vorräte gab es in der Jungsteinzeit keine Hungersnöte mehr.", False, s,
           info="Fiel die Ernte aus, drohten weiterhin Hungersnöte. Am Anfang war das Essen außerdem einseitig."),
        reihenfolge("Ordne die Folgen so, dass jeder Schritt zum nächsten führt.",
                    ["Die Menschen bauen Getreide an und halten Tiere.", "Sie siedeln in Dörfern und legen Vorräte an.", "Die Bevölkerung nimmt stetig zu.",
                     "Neue Siedlungen und Ackerflächen müssen angelegt werden."], s,
                    info="Ackerbau und Viehzucht machen sesshaft. Mit mehr Menschen braucht man mehr Siedlungen und Ackerflächen.",
                    tipp="Fange mit der neuen Lebensweise an."),
    ]
    # ------------------------------------------------------------------ D Abwägen
    s = "D – Vorteile und Nachteile abwägen"
    A += [
        zuordnen("War das ein Vorteil oder ein Nachteil der neuen Lebensweise?",
                 [("Vorräte im Haus", "Vorteil"), ("feste Häuser statt Zelte", "Vorteil"), ("Hungersnot bei Ernteausfall", "Nachteil"),
                  ("Neid und Streit um Besitz", "Nachteil"), ("einseitige Ernährung am Anfang", "Nachteil"), ("Tiere halten statt gefährlicher Jagd", "Vorteil")], s,
                 info="Vorräte, feste Häuser und die weniger gefährliche Tierhaltung waren Vorteile. Hunger, Streit und einseitiges Essen waren Nachteile."),
        mc("Welchen Vorteil hatte die Viehzucht gegenüber der Jagd?", "Sie war weniger gefährlich als die Jagd.",
           ["Man musste die Tiere nicht mehr hüten.", "Man brauchte keine Vorräte mehr.", "Man brauchte keinen Platz für Weiden."], s,
           info="Bei der Jagd gab es oft Verletzungen. Tiere zu halten und zu züchten war weniger gefährlich."),
        tf("Am Anfang war die Ernährung der ersten Bauern einseitig.", True, s,
           info="Am Anfang war die Ernährung einseitig. Bei Ernteausfällen drohten sogar Hungersnöte."),
        mc("Wähle alle richtigen Antworten: Welche Aussagen nennen Vorteile der neuen Lebensweise?",
           ["Man hatte Vorräte für schlechte Zeiten.", "Man wohnte in größeren und festeren Häusern.", "Tiere zu halten war weniger gefährlich als die Jagd."],
           ["Es gab keinen Streit um Besitz mehr.", "Bei Ernteausfall war immer genug zu essen da."], s,
           info="Streit um Besitz und Hunger bei Ernteausfall gehören zu den Nachteilen.",
           tipp="Zwei der Aussagen stimmen nicht."),
        mc("Welche Folge der neuen Lebensweise war ein Nachteil?", "Bei Ernteausfall drohte eine Hungersnot.",
           ["Es gab neue Berufe wie Töpfer und Handwerker.", "Man konnte Vorräte anlegen.", "Man wohnte in festen Häusern."], s,
           info="Wer vom Getreide lebt, ist auf die Ernte angewiesen. Fällt sie aus, droht Hunger."),
        luecke("Ergänze die Abwägung.",
               "Durch Vorräte wurden die Menschen {{unabhängiger}} von der Umwelt. Bei einem {{Ernteausfall}} drohte aber {{Hunger}}. Außerdem führte Besitz zu {{Neid}} und Streit.",
               s, extra=["abhängiger", "Nomaden"],
               info="Die neue Lebensweise hatte Vorteile und Nachteile. Vorräte halfen, aber Ernteausfälle und Besitz brachten neue Probleme."),
    ]
    # ------------------------------------------------------------------ E Alt oder Jung?
    s = "E – Altsteinzeit oder Jungsteinzeit?"
    A += [
        zuordnen("Gehört das zur Altsteinzeit oder zur Jungsteinzeit?",
                 [("Zelte, die man abbaut", "Altsteinzeit"), ("Langhäuser in festen Dörfern", "Jungsteinzeit"), ("Nähnadel aus Knochen", "Altsteinzeit"),
                  ("Pflug", "Jungsteinzeit"), ("Mahlstein", "Jungsteinzeit"), ("Speerschleuder", "Altsteinzeit")], s,
                 info="Zelte, Nähnadel und Speerschleuder kennen die Jäger und Sammler der Altsteinzeit. Dorf, Pflug und Mahlstein gehören zu den Bauern der Jungsteinzeit."),
        kurz("Wie viele Personen lebten in der Altsteinzeit ungefähr in einer Gruppe?", GRUPPENGROESSE, s, einheit="Personen",
             info="Die Jäger und Sammler lebten in kleinen Gruppen von etwa 25 bis 30 Personen.",
             tipp="Es waren nur wenige Dutzend."),
        mc("Welche Aussage passt zur Altsteinzeit?", "Die Menschen zogen in kleinen Gruppen von Lager zu Lager.",
           ["Die Menschen bauten Getreide an und ernteten es auf Feldern.", "Die Menschen webten Stoffe für ihre Kleidung am Webstuhl.", "Die Menschen formten Töpfe und Becher aus Ton im Dorf."], s,
           info="Die Jäger und Sammler der Altsteinzeit waren Nomaden. Ackerbau, Weben und Töpfern gehören zur Jungsteinzeit."),
        mc("Welche Aussage passt zur Jungsteinzeit?", "Die Menschen blieben dauerhaft in ihrem Dorf wohnen.",
           ["Die Menschen folgten den Wanderbewegungen der Beutetiere.", "Die Menschen schliefen meist in Zelten aus Fell.", "Die Menschen lebten allein vom Jagen und Sammeln."], s,
           info="In der Jungsteinzeit wurden die Menschen sesshaft. Die anderen Aussagen beschreiben die Altsteinzeit."),
        mc("Wähle alle richtigen Antworten: Was gab es schon in der Altsteinzeit?", ["Faustkeil", "Nähnadel aus Knochen", "Feuer"],
           ["Pflug", "Keramik", "Webstuhl"], s,
           info="Faustkeil, Nähnadel und Feuer kannten schon die Jäger und Sammler. Pflug, Keramik und Webstuhl sind Neuerungen der Jungsteinzeit."),
        tf("Die Menschen der Jungsteinzeit hörten ganz auf zu jagen.", False, s,
           info="Auch in der Jungsteinzeit wurde weiter gejagt. Hauptsächlich lebten die Menschen aber von Ackerbau und Viehzucht."),
        tf("Nur in der Jungsteinzeit legten Menschen Vorräte an.", False, s,
           info="Auch Eiszeitjäger konnten Fleisch konservieren und in Depots aufbewahren. Neu in der Jungsteinzeit war die Vorratshaltung im Dorf mit Getreide aus eigenem Anbau.",
           tipp="Denke an die Jäger der Eiszeit."),
    ]
    # ------------------------------------------------------------------ F Vergleich Zeile für Zeile
    s = "F – Der Vergleich Zeile für Zeile"
    A += [
        zuordnen("In der Tabelle fehlt die Spalte der Jungsteinzeit. Ordne jeder Zeile den passenden Eintrag zu.",
                 [("Nahrungserwerb", "Ackerbau und Viehzucht"), ("Nahrung", "Getreide, Milch, Käse"), ("Erfindungen", "Pflug, Keramik, Webstuhl, Rad"),
                  ("Aufenthaltsorte", "feste Dörfer mit Häusern"), ("Gefahren", "Missernten, Hunger, Streit um Besitz"), ("Bekleidung", "gewebte Stoffe neben Fellen"),
                  ("Lebensweise", "sesshaft, Arbeitsteilung und Berufe")], s,
                 extra=["Faustkeil, Speerschleuder, Nähnadel"],
                 bild=svg_vergleich(False),
                 bildAlt="Vergleichstabelle mit den Zeilen Nahrungserwerb, Nahrung, Erfindungen, Aufenthaltsorte, Gefahren, Bekleidung und Lebensweise. Die Spalte der Altsteinzeit ist ausgefüllt, die Spalte der Jungsteinzeit zeigt nur Fragezeichen.",
                 info="Vergleiche mit der Altsteinzeit in der linken Spalte: Dort stehen Jagen und Sammeln, wechselnde Lagerplätze und Raubtiere. In der Jungsteinzeit sind es Ackerbau, Dörfer und Missernten, bei der Kleidung kommen gewebte Stoffe dazu.",
                 tipp="Die Spalte der Altsteinzeit hilft dir: Die Jungsteinzeit ist meist das Gegenteil."),
        mc("Wie unterscheiden sich Altsteinzeit und Jungsteinzeit beim Nahrungserwerb?",
           "Altsteinzeit: Jagen und Sammeln. Jungsteinzeit: Ackerbau und Viehzucht.",
           ["Altsteinzeit: Ackerbau und Viehzucht. Jungsteinzeit: Jagen und Sammeln.", "In beiden Zeiten lebten die Menschen nur vom Jagen und Sammeln.", "In beiden Zeiten lebten die Menschen nur von Ackerbau und Viehzucht."], s,
           info="Der Nahrungserwerb ist der wichtigste Unterschied. In der Jungsteinzeit wurde nebenbei weiter gejagt."),
        zuordnen("Ordne jedem Merkmal der Altsteinzeit das passende Gegenstück der Jungsteinzeit zu.",
                 [("Nomaden", "sesshafte Dorfbewohner"), ("Zelt", "festes Haus"), ("Jagen und Sammeln", "Ackerbau und Viehzucht"),
                  ("Kleidung nur aus Fell", "gewebte Stoffe neben Fellen"), ("Gefahr durch Raubtiere", "Gefahr durch Missernten")], s,
                 extra=["Töpfer"],
                 info="Das sind Gegensatzpaare aus der Vergleichstabelle."),
        kurz("Wie nennt man Menschen, die keinen festen Wohnsitz haben und ihrer Nahrung hinterherziehen?", ["Nomaden", "Nomade", "die Nomaden"], s,
             info="Die Jäger und Sammler der Altsteinzeit waren Nomaden. Die Bauern der Jungsteinzeit waren sesshaft."),
        luecke("Ergänze den Vergleich.",
               "In der Altsteinzeit lebten die Menschen als {{Nomaden}} in {{Zelten}} oder Höhlen. In der Jungsteinzeit wurden sie {{sesshaft}} und wohnten in {{Dörfern}}. Sie ernährten sich nun von {{Getreide}}, Milch und Käse.",
               s, extra=["Städten", "Mammutfleisch"],
               info="Nomaden und Zelte gehören zur Altsteinzeit, sesshaft sein und Dörfer zur Jungsteinzeit."),
        mc("Welche Gefahr betraf vor allem die Menschen der Altsteinzeit?", "Angriffe von Raubtieren wie Wölfen",
           ["Streit zwischen den Nachbarn um Besitz", "Missernten auf den großen Feldern", "Hunger nach einem Ernteausfall"], s,
           info="In der Tabelle stehen für die Altsteinzeit Raubtiere, Kälte, Jagdunfälle und Nahrungsmangel. Missernten und Streit um Besitz gehören zur Jungsteinzeit."),
        frei("Nenne drei Unterschiede zwischen Altsteinzeit und Jungsteinzeit.",
             "Nahrung: In der Altsteinzeit lebten die Menschen vom Jagen und Sammeln, in der Jungsteinzeit von Ackerbau und Viehzucht. "
             "Wohnen: In der Altsteinzeit wohnten sie in Zelten oder Höhlen und zogen umher (Nomaden), in der Jungsteinzeit lebten sie sesshaft in Dörfern mit festen Häusern. "
             "Erfindungen: In der Altsteinzeit gab es zum Beispiel Faustkeil, Speer und Nähnadel, in der Jungsteinzeit Pflug, Keramik, Webstuhl und Rad.",
             ["Unterschied 1 richtig, beide Zeiten genannt", "Unterschied 2 richtig, beide Zeiten genannt", "Unterschied 3 richtig, beide Zeiten genannt"], 3, s,
             tipp="Nimm drei Zeilen der Tabelle, zum Beispiel Nahrungserwerb, Aufenthaltsorte und Erfindungen."),
        tf("In der Jungsteinzeit trugen die Menschen gewebte Stoffe neben Fellen.", True, s,
           info="In der Tabelle steht für die Jungsteinzeit: gewebte Stoffe (Wolle, Lein) neben Fellen."),
    ]
    # ------------------------------------------------------------------ G Klausurnah
    s = "G – Klausurnah: Vergleichen und Begründen"
    A += [
        frei("Vergleiche das Leben in der Altsteinzeit und in der Jungsteinzeit in drei Bereichen deiner Wahl (zum Beispiel Nahrung, Wohnen, Kleidung, Gefahren). Schreibe in ganzen Sätzen.",
             "Nahrung: In der Altsteinzeit jagten und sammelten die Menschen, in der Jungsteinzeit dagegen bauten sie Getreide an und hielten Tiere. "
             "Wohnen: In der Altsteinzeit zogen sie als Nomaden in kleinen Gruppen von Lagerplatz zu Lagerplatz und lebten in Zelten oder Höhlen. In der Jungsteinzeit wohnten sie sesshaft in Dörfern mit festen Häusern. "
             "Gefahren: In der Altsteinzeit drohten vor allem Raubtiere, Kälte und Jagdunfälle, während es in der Jungsteinzeit eher Missernten, Hunger und Streit um Besitz gab.",
             ["Bereich 1: Altsteinzeit richtig", "Bereich 1: Jungsteinzeit richtig", "Bereich 2: Altsteinzeit richtig", "Bereich 2: Jungsteinzeit richtig",
              "Bereich 3: Altsteinzeit richtig", "Bereich 3: Jungsteinzeit richtig", "Beide Seiten werden verglichen (zum Beispiel mit „dagegen“ oder „während“)"], 7, s,
             tipp="Nenne in jedem Bereich zuerst die Altsteinzeit und dann die Jungsteinzeit."),
        frei("War der Wechsel zum Leben als Bauer nur ein Vorteil? Nenne zwei Vorteile und zwei Nachteile und schreibe am Ende dein begründetes Urteil.",
             "Vorteile waren die Vorräte, die die Menschen unabhängiger von der Umwelt machten, und die festen Häuser im Dorf. Auch die Tierhaltung war weniger gefährlich als die Jagd. "
             "Nachteile waren, dass bei Ernteausfällen Hungersnöte drohten und dass Besitz zu Neid und Streit führte. "
             "Mein Urteil: Die neue Lebensweise war ein großer Schritt nach vorn, weil man sicherer leben konnte, aber sie brachte auch neue Probleme mit sich.",
             ["Vorteil 1 richtig genannt", "Vorteil 2 richtig genannt", "Nachteil 1 richtig genannt", "Nachteil 2 richtig genannt", "Urteil mit Begründung"], 5, s,
             tipp="Es gibt kein einziges richtiges Urteil. Wichtig ist, dass du es mit den Vor- und Nachteilen begründest."),
        frei("Stell dir vor, Jäger und Sammler aus der Altsteinzeit besuchen ein Dorf der Jungsteinzeit. Schreibe aus der Sicht einer Jägerin oder eines Jägers auf, was ihr auffällt. Nenne mindestens drei Beobachtungen und vergleiche mit deinem eigenen Leben.",
             "Wir haben ein Dorf besucht, und alles war anders als bei uns. Die Menschen wohnen dort in langen, festen Häusern mit Strohdach und ziehen nie weiter. Wir dagegen bauen unsere Zelte ab, sobald die Herde weiterzieht. "
             "Sie haben Felder mit Getreide und Weiden mit Schafen, deshalb müssen sie nicht jeden Tag auf die Jagd gehen. In ihren Häusern lagern große Vorräte. Sie tragen Kleidung aus gewebten Stoffen und kochen in Töpfen aus Ton. "
             "Es gibt viele Aufgaben, jeder macht etwas anderes, einer hütet Schafe, eine andere formt Töpfe. Das gefällt mir, aber ich habe auch gehört, dass es Streit um Besitz gibt und dass die Menschen Hunger leiden, wenn die Ernte ausfällt.",
             ["Beobachtung 1 richtig (zum Beispiel Häuser, Felder, Vorräte, Töpfe, Berufe)", "Beobachtung 2 richtig", "Beobachtung 3 richtig",
              "Vergleich mit dem eigenen Leben als Jäger oder Sammler", "Bewertung oder Gefühl mit Begründung"], 5, s,
             tipp="Überlege, was für Nomaden neu und ungewohnt wäre: Häuser, Felder, Vorräte, Berufe. Benutze nur Dinge, die es damals gab."),
        mc("Archäologen finden an einer Fundstelle Mahlsteine, Scherben von Tontöpfen und Spuren von langen Häusern. Aus welchem Abschnitt der Steinzeit stammt der Fund?", "aus der Jungsteinzeit",
           ["aus der Altsteinzeit", "aus der Mittelsteinzeit"], s,
           info="Mahlsteine weisen auf Getreide hin, Tontöpfe auf Keramik und lange Häuser auf ein Dorf. Das sind Sachquellen aus der Jungsteinzeit.",
           tipp="Mahlsteine, Töpfe und Dörfer gehören zu den Bauern."),
        tf("Eine Rekonstruktionszeichnung eines Dorfs der Jungsteinzeit ist eine Quelle.", False, s,
           info="Eine Quelle stammt aus der Zeit selbst, zum Beispiel ein Mahlstein. Eine Zeichnung, die Menschen später mithilfe von Quellen gemacht haben, ist eine Darstellung."),
        mc("Ein Mitschüler behauptet: „In der Jungsteinzeit lebten die Menschen mit Mahlstein und Pflug in Zelten, die sie immer wieder abbauten.“ Was ist falsch?",
           "Sie lebten in festen Dörfern und nicht in Zelten, die sie abbauten.",
           ["Mahlsteine gab es erst in der Altsteinzeit, lange vor den Bauern.", "Der Pflug wurde erst erfunden, nachdem es schon das Rad gab.", "Mahlstein und Pflug sind keine Geräte, die Bauern benutzten."], s,
           info=f"Pflug und Mahlstein gehören zu den sesshaften Bauern. Der Pflug (seit ca. {PFLUG_J} v. Chr.) ist außerdem älter als das Rad (um {RAD_J} v. Chr.).",
           tipp="Wer einen Pflug benutzt, bleibt an einem Ort."),
        luecke("Fasse den Vergleich zusammen.",
               "In der Altsteinzeit sicherten sich die Menschen ihre Nahrung durch {{Jagen|Sammeln}} und {{Sammeln|Jagen}} und lebten als {{Nomaden}} in kleinen Gruppen. "
               "In der Jungsteinzeit wurden sie {{sesshaft}}. Sie betrieben {{Ackerbau|Viehzucht}} und {{Viehzucht|Ackerbau}} und wohnten in {{Dörfern}}. "
               "Weil jeder eine eigene Aufgabe hatte, spricht man von {{Arbeitsteilung}}. So entstanden Berufe wie {{Töpfer|Schäfer|Handwerker|Bauern}}.",
               s, extra=["Höhlen", "Eiszeit"],
               info="Das fasst den Kern des Vergleichs zusammen: nomadische Jäger und Sammler gegen sesshafte Bauern mit Arbeitsteilung."),
    ]
    lesen = {
        "A": {0: L_DORF, 1: L_DORF, 2: L_DORF, 3: L_DORF, 4: L_DORF, 5: L_DORF, 6: L_DORF, 7: L_DORF},
        "B": {0: [L_HAUSH, L_WERK], 1: L_HAUSH, 2: L_HAUSH, 3: L_WERK, 4: L_WERK, 5: [L_HAUSH, L_WERK, L_ALT], 6: L_HAUSH, 7: L_HAUSH, 8: L_HAUSH, 9: [L_HAUSH, L_WERK]},
        "C": {0: L_FOLGEN, 1: L_FOLGEN, 2: L_FOLGEN, 3: L_FOLGEN, 4: L_FOLGEN, 5: L_FOLGEN},
        "D": {0: L_ABW, 1: L_ABW, 2: L_ABW, 3: L_ABW, 4: L_ABW, 5: L_ABW},
        "E": {0: [L_ALT, L_VGL], 1: L_ALT, 2: L_ALT, 3: L_DORF, 4: L_ALT, 5: L_VGL, 6: L_ALT},
        "F": {0: L_VGL, 1: L_VGL, 2: L_GEG, 3: L_ALT, 4: L_GEG, 5: L_ALT, 6: L_GEG, 7: L_VGL},
        "G": {0: [L_VGL, L_GEG], 1: L_ABW, 2: [L_DORF, L_ALT, L_GEG], 3: [L_HAUSH, L_DORF], 4: L_DORF, 5: [L_DORF, L_VGL]},
    }
    _lesen_setzen(A, lesen)
    return A


def paket_5b():
    p = pack("geschichte-5b-jungsteinzeit-leben-vergleich", "Geschichte Teil 5b: Leben in der Jungsteinzeit und Vergleich mit der Altsteinzeit",
             "Leben im Dorf, Erfindungen und ihre Bedeutung, Folgen der neuen Lebensweise, Vor- und Nachteile abwägen und der große Vergleich zwischen Altsteinzeit und Jungsteinzeit. Mit Lernblatt, Zeichnungen und Übungsaufgaben.",
             lernblatt_5b(), aufgaben_5b(), min_aufgaben=45,
             hinweis="Der Vergleich folgt den Zeilen der Tabelle im Buch. Die Antworten sind aus Heft und Buch abgeleitet. Bitte mit deinem Heft und deinem Tafelanschrieb abgleichen.")
    assert 45 <= len(p["aufgaben"]) <= 58, len(p["aufgaben"])
    nachlesen(p, {
        "A – Leben im Dorf": "Leben im Dorf der Jungsteinzeit",
        "B – Erfindungen und ihre Bedeutung": ["Spinnen, Weben, Töpfern und Mahlen", "Beil, Pflug und Rad"],
        "C – Folgen der neuen Lebensweise": "Folgen der neuen Lebensweise",
        "D – Vorteile und Nachteile abwägen": "Vorteile und Nachteile abwägen",
        "E – Altsteinzeit oder Jungsteinzeit?": ["Die Altsteinzeit in Kürze", "Altsteinzeit und Jungsteinzeit im Vergleich"],
        "F – Der Vergleich Zeile für Zeile": ["Altsteinzeit und Jungsteinzeit im Vergleich", "Gegensätze und Vergleiche aufschreiben"],
        "G – Klausurnah: Vergleichen und Begründen": ["Altsteinzeit und Jungsteinzeit im Vergleich", "Gegensätze und Vergleiche aufschreiben", "Vorteile und Nachteile abwägen"],
    })
    p["probe"] = False
    return p


def build():
    """Liste der Pakete: 5a, 5b."""
    return [paket_5a(), paket_5b()]
