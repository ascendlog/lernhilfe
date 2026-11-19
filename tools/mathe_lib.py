"""Hilfen für Mathe-Lernpakete (Klasse 6, Brüche): Paketbau, Prüfungen und Zeichnungen (SVG).

Baut auf geo_lib.py auf (mc, tf, kurz, luecke, zuordnen, reihenfolge, frei, lb, check_pack).
Alle Rechnungen laufen über fractions.Fraction und werden mit assert geprüft.
Anders als bei den Geschichte-Paketen wird `nachsicht` NICHT gesetzt: Die Nachsicht der App entfernt „/“ und Leerzeichen,
dann würde bei einer Texteingabe „34“ für „3/4“ gelten. Brüche werden deshalb in zwei Feldern (Zähler, Nenner) eingegeben.
"""
import math
import re
from fractions import Fraction

from geo_lib import *                      # noqa: F401,F403  (mc, tf, kurz, luecke, zuordnen, reihenfolge, frei, lb, check_pack ...)
from geo_lib import _svg, _label, _gaps    # noqa: F401
from gesch_lib import _normalisiere, punkte_von   # noqa: F401  (Listen-Absätze, Punkte wie in der App)

FACH = "Mathe"

import geo_lib as _g


def _mit_lesen(f):
    """Baustein von geo_lib um das Aufgabenfeld "lesen" ergänzen (Titel oder Liste von Titeln eines Lernblatt-Abschnitts)."""
    def w(*a, lesen=None, **k):
        t = f(*a, **k)
        if lesen is not None:
            t["lesen"] = lesen
        return t
    w.__name__ = f.__name__
    return w


mc, tf, kurz, luecke, zuordnen, reihenfolge, frei = (_mit_lesen(getattr(_g, n)) for n in ("mc", "tf", "kurz", "luecke", "zuordnen", "reihenfolge", "frei"))


def bruch(z, n):
    """Text eines Bruchs: 3/4"""
    return f"{z}/{n}"


def ggt(a, b):
    return math.gcd(a, b)


def pack(id, titel, beschreibung, lernblatt, aufgaben, hinweis=None):
    """Ein Mathe-Paket für Joel und Dario. Jede Aufgabe außer frei braucht ein info (Regel vom 04.11.2026)."""
    for i, t in enumerate(aufgaben, 1):
        if t["typ"] != "frei":
            assert t.get("info", "").strip(), f"{id} Aufgabe {i}: info fehlt ({t['frage'][:50]})"
    p = {"typ": "lernpaket", "version": 1, "person": ["joel", "dario"], "id": id, "titel": titel,
         "fach": FACH, "klasse": "6", "beschreibung": beschreibung}
    if hinweis:
        p["hinweis"] = hinweis
    p["lernblatt"] = lernblatt
    p["aufgaben"] = aufgaben
    p = _normalisiere(p)
    check_pack(p)
    return p


def nachlesen(p, bloecke):
    """Setzt p["nachlesen"] (Aufgabenblock -> Titel eines Lernblatt-Abschnitts oder Liste) und prüft alles."""
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


# ------------------------------------------------------------------ Zeichnungen

BLAU, BLAU_HELL = "#3b6ea5", "#bcd6ee"
ORANGE = "#e2701a"


def _bruch_svg(x, y, z, n, size=20, fill="#222", bold=True):
    """Gestapelter Bruch, Mitte bei x, Bruchstrich bei y. Gibt SVG-Text zurück."""
    w = max(len(str(z)), len(str(n))) * size * 0.62 + 10
    wt = "bold" if bold else "normal"
    return (f'<text x="{x}" y="{y - 5}" font-size="{size}" font-weight="{wt}" fill="{fill}" text-anchor="middle">{z}</text>'
            f'<line x1="{x - w / 2:.1f}" y1="{y}" x2="{x + w / 2:.1f}" y2="{y}" stroke="{fill}" stroke-width="2.2"/>'
            f'<text x="{x}" y="{y + size + 1}" font-size="{size}" font-weight="{wt}" fill="{fill}" text-anchor="middle">{n}</text>')


def _bogen(x1, y1, x2, y2, hoch, farbe=ORANGE):
    """Gebogener Pfeil von (x1,y1) nach (x2,y2); hoch>0: Bogen nach oben, <0: nach unten. Spitze am Ende."""
    cx, cy = (x1 + x2) / 2, min(y1, y2) - hoch if hoch > 0 else max(y1, y2) - hoch
    # Richtung am Ende für die Pfeilspitze
    dx, dy = x2 - cx, y2 - cy
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    px, py = -uy, ux
    s = 11
    a = (x2 - s * ux + 0.55 * s * px, y2 - s * uy + 0.55 * s * py)
    b = (x2 - s * ux - 0.55 * s * px, y2 - s * uy - 0.55 * s * py)
    return (f'<path d="M{x1},{y1} Q{cx},{cy} {x2},{y2}" fill="none" stroke="{farbe}" stroke-width="3"/>'
            f'<polygon points="{x2},{y2} {a[0]:.1f},{a[1]:.1f} {b[0]:.1f},{b[1]:.1f}" fill="{farbe}"/>')


def svg_streifen(zeilen, breite=520, titel_links=True):
    """Bruchstreifen untereinander, alle gleich lang. zeilen: [(Zähler, Nenner)] oder [(Zähler, Nenner, 'Beschriftung')].

    Zeilen mit Beschriftung None zeigen links keinen Bruch (für Aufgaben, in denen man den Bruch ablesen soll);
    eine Beschriftung aus Buchstaben (A, B) steht dann links als Buchstabe.
    """
    x0, h, abst = 100, 40, 70
    H = 24 + len(zeilen) * abst
    g = []
    for i, z in enumerate(zeilen):
        zz, nn = z[0], z[1]
        lab = z[2] if len(z) > 2 else "bruch"
        y = 20 + i * abst
        w = breite / nn
        for k in range(nn):
            fill = BLAU if k < zz else "#ffffff"
            g.append(f'<rect x="{x0 + k * w:.1f}" y="{y}" width="{w:.1f}" height="{h}" fill="{fill}" stroke="#222" stroke-width="2"/>')
        if lab == "bruch":
            g.append(_bruch_svg(48, y + h / 2 - 2, zz, nn, size=22))
        elif lab:
            g.append(_label(48, y + h / 2 + 8, lab, size=26, weight="bold"))
    return _svg(x0 + breite + 20, H, ''.join(g))


def svg_rechenweg(z, n, op, k):
    """z/n --(·k)--> Ergebnis. op '·' (Erweitern) oder ':' (Kürzen). Oben und unten ein Pfeil mit „· k“ bzw. „: k“."""
    if op == "·":
        z2, n2 = z * k, n * k
    else:
        assert z % k == 0 and n % k == 0, (z, n, k)
        z2, n2 = z // k, n // k
    assert Fraction(z, n) == Fraction(z2, n2)
    xa, xb, y = 170, 430, 108
    g = [_bruch_svg(xa, y, z, n, size=34), _label((xa + xb) / 2, y + 12, "=", size=40, weight="bold"),
         _bruch_svg(xb, y, z2, n2, size=34)]
    g.append(_bogen(xa + 56, y - 46, xb - 56, y - 46, 36))
    g.append(_bogen(xa + 56, y + 52, xb - 56, y + 52, -36))
    g.append(_label((xa + xb) / 2, y - 76, f"{op} {k}", size=28, weight="bold", fill=ORANGE))
    g.append(_label((xa + xb) / 2, y + 104, f"{op} {k}", size=28, weight="bold", fill=ORANGE))
    return _svg(600, 232, ''.join(g))


def svg_zahlenstrahl12(markiert):
    """Zahlenstrahl von 0 bis 1 in Zwölfteln. markiert: Liste von Brüchen (Fraction), die oben gekürzt beschriftet werden."""
    x0, x1, ay = 40, 720, 130
    X = lambda f: x0 + float(f) * (x1 - x0)
    g = [f'<line x1="{x0 - 16}" y1="{ay}" x2="{x1 + 22}" y2="{ay}" stroke="#222" stroke-width="3"/>']
    for k in range(13):
        x = X(Fraction(k, 12))
        g.append(f'<line x1="{x:.1f}" y1="{ay - 11}" x2="{x:.1f}" y2="{ay + 11}" stroke="#222" stroke-width="2"/>')
        g.append(_label(round(x, 1), ay + 34, f"{k}/12" if k not in (0, 12) else ("0" if k == 0 else "1"), size=15, weight="bold" if k in (0, 12) else "normal"))
    for f in markiert:
        assert (f * 12).denominator == 1
        x = X(f)
        g.append(f'<line x1="{x:.1f}" y1="{ay}" x2="{x:.1f}" y2="{ay - 40}" stroke="{ORANGE}" stroke-width="2.5"/>')
        g.append(f'<circle cx="{x:.1f}" cy="{ay}" r="6" fill="{ORANGE}"/>')
        g.append(_bruch_svg(round(x, 1), ay - 62, f.numerator, f.denominator, size=20, fill=ORANGE))
    return _svg(760, 180, ''.join(g))
