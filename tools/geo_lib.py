"""Hilfen für die Geografie-Lernpakete (Klasse 6): Aufgaben-Bausteine, Zeichnungen (SVG) und Prüfungen.

Alle Zahlen, Uhrzeiten und Lösungen werden hier im Code berechnet und mit assert geprüft,
damit in den Paketen keine falschen Lösungen stehen.
"""
import math
import re

# ---------------------------------------------------------------- kleine Helfer


def hhmm(minuten):
    """Minuten seit Mitternacht -> 'hh:mm' (über 24 Stunden hinaus wird abgeschnitten)."""
    minuten = int(round(minuten)) % 1440
    return f"{minuten // 60:02d}:{minuten % 60:02d}"


def de(x, nd=1):
    """Zahl mit Komma statt Punkt."""
    return f"{x:.{nd}f}".replace('.', ',')


def _gaps(text):
    return re.findall(r"\{\{([\s\S]*?)\}\}", text)


# ---------------------------------------------------------------- Aufgaben


def _base(typ, frage, abschnitt, info=None, tipp=None, bild=None, bildAlt=None, text=None):
    t = {"typ": typ}
    if abschnitt:
        t["abschnitt"] = abschnitt
    t["frage"] = frage
    if text is not None:
        t["text"] = text
    if bild:
        assert bildAlt, "bildAlt fehlt"
        t["bild"] = bild
        t["bildAlt"] = bildAlt
    if tipp:
        t["tipp"] = tipp
    if info:
        t["info"] = info
    return t


def mc(frage, richtig, falsch, abschnitt, info=None, tipp=None, bild=None, bildAlt=None, punkte=None, mischen=True):
    """Auswahl. richtig: Text (eine richtige Antwort) oder Liste (mehrere richtige). falsch: Liste falscher Antworten."""
    rl = [richtig] if isinstance(richtig, str) else list(richtig)
    antworten = rl + list(falsch)
    assert len(set(antworten)) == len(antworten), f"doppelte Antworten: {antworten}"
    assert 2 <= len(antworten) <= 6, antworten
    t = _base("mc", frage, abschnitt, info, tipp, bild, bildAlt)
    t["antworten"] = antworten
    t["richtig"] = 0 if isinstance(richtig, str) else list(range(len(rl)))
    if not mischen:
        t["mischen"] = False
    if punkte:
        t["punkte"] = punkte
    return t


def tf(frage, wahr, abschnitt, info=None, tipp=None, bild=None, bildAlt=None):
    t = _base("tf", frage, abschnitt, info, tipp, bild, bildAlt)
    t["richtig"] = bool(wahr)
    return t


def kurz(frage, richtig, abschnitt, einheit=None, toleranz=None, info=None, tipp=None, bild=None, bildAlt=None):
    r = [richtig] if isinstance(richtig, (str, int, float)) else list(richtig)
    t = _base("kurz", frage, abschnitt, info, tipp, bild, bildAlt)
    t["richtig"] = [str(x) for x in r] if len(r) > 1 else str(r[0])
    if einheit:
        t["einheit"] = einheit
    if toleranz is not None:
        t["toleranz"] = toleranz
    return t


def luecke(frage, text, abschnitt, extra=(), info=None, tipp=None, bild=None, bildAlt=None, wortbank=True):
    """Lückentext mit {{richtig|auch richtig}}. Die Wortbank enthält die ersten Antworten plus extra (falsche Wörter)."""
    gaps = _gaps(text)
    assert gaps, "keine Lücken"
    first = [g.split('|')[0].strip() for g in gaps]
    t = _base("luecke", frage, abschnitt, info, tipp, bild, bildAlt, text=text)
    if wortbank:
        bank = []
        for w in first + list(extra):
            if w not in bank:
                bank.append(w)
        for w in extra:
            assert w not in first, f"extra-Wort ist eine richtige Antwort: {w}"
        t["wortbank"] = bank
    return t


def zuordnen(frage, paare, abschnitt, extra=(), info=None, tipp=None, bild=None, bildAlt=None):
    assert len(paare) >= 2
    t = _base("zuordnen", frage, abschnitt, info, tipp, bild, bildAlt)
    t["paare"] = [[a, b] for a, b in paare]
    if extra:
        t["extra"] = list(extra)
    return t


def reihenfolge(frage, schritte, abschnitt, info=None, tipp=None, bild=None, bildAlt=None):
    assert len(schritte) >= 3 and len(set(schritte)) == len(schritte)
    t = _base("reihenfolge", frage, abschnitt, info, tipp, bild, bildAlt)
    t["schritte"] = list(schritte)
    return t


def frei(frage, muster, kriterien, punkte, abschnitt, info=None, tipp=None, bild=None, bildAlt=None):
    assert kriterien, "Kriterien fehlen"
    t = _base("frei", frage, abschnitt, info, tipp, bild, bildAlt)
    t["punkte"] = punkte
    t["muster"] = muster
    t["kriterien"] = list(kriterien)
    return t


def lb(titel, text, merke=None, bild=None, bildAlt=None):
    """Ein Abschnitt des Lernblatts."""
    s = {"titel": titel, "text": text}
    if merke:
        s["merke"] = merke
    if bild:
        assert bildAlt
        s["bild"] = bild
        s["bildAlt"] = bildAlt
    return s


def pack(id, titel, beschreibung, lernblatt, aufgaben, hinweis=None, min_aufgaben=None):
    if min_aufgaben:
        assert len(aufgaben) >= min_aufgaben, f"{id}: nur {len(aufgaben)} Aufgaben (Ziel {min_aufgaben})"
    p = {"typ": "lernpaket", "version": 1, "person": ["joel", "dario"], "id": id, "titel": titel,
         "fach": "Geografie", "klasse": "6", "beschreibung": beschreibung}
    if hinweis:
        p["hinweis"] = hinweis
    if lernblatt:   # optional: Probearbeit-Pakete haben kein Lernblatt
        p["lernblatt"] = lernblatt
    p["aufgaben"] = aufgaben
    check_pack(p)
    return p


def check_pack(p):
    """Strenge Prüfung vor dem Schreiben (ergänzt validatePack der App)."""
    assert re.fullmatch(r"[A-Za-z0-9_-]+", p["id"]), p["id"]
    seen = set()
    for i, t in enumerate(p["aufgaben"], 1):
        w = f"{p['id']} Aufgabe {i}"
        assert t["typ"] in ("mc", "tf", "kurz", "luecke", "zuordnen", "reihenfolge", "frei"), w
        assert t.get("frage", "").strip(), w
        key = (t["typ"], t["frage"], t.get("text", ""), str(t.get("antworten", "")), str(t.get("paare", "")), str(t.get("richtig", "")), hash(t.get("bild", "")))
        assert key not in seen, f"{w}: doppelte Aufgabe: {t['frage'][:60]}"
        seen.add(key)
        if t["typ"] == "mc":
            r = t["richtig"] if isinstance(t["richtig"], list) else [t["richtig"]]
            assert all(0 <= x < len(t["antworten"]) for x in r), w
        if t["typ"] == "luecke":
            gaps = _gaps(t["text"])
            assert gaps, w
            if "wortbank" in t:
                for g in gaps:
                    assert g.split('|')[0].strip() in t["wortbank"], f"{w}: {g} fehlt in der Wortbank"
        if t["typ"] == "zuordnen":
            lefts = [a for a, _ in t["paare"]]
            assert len(set(lefts)) == len(lefts), w
        if t["typ"] == "kurz":
            assert t["richtig"] not in ("", []), w
        if t["typ"] == "frei":
            assert t["muster"].strip() and t["kriterien"], w
        for feld in ("frage", "text", "info", "tipp", "muster"):
            s = t.get(feld, "")
            if isinstance(s, str):
                assert "**" not in s.replace("**", "", 0) or s.count("**") % 2 == 0, f"{w}: ** ungerade in {feld}"
    for s in p.get("lernblatt", []):
        assert s["titel"].strip() and s["text"].strip(), p["id"]
        assert s["text"].count("**") % 2 == 0, f"Lernblatt {s['titel']}: ** ungerade"
        if s.get("merke"):
            assert s["merke"].count("**") % 2 == 0
    # Hinweis zur App: Tabellen und Kursivschrift gibt es nicht
    for s in p.get("lernblatt", []):
        assert "|---" not in s["text"], "Tabellen im Lernblatt nicht erlaubt"


# ---------------------------------------------------------------- Zeichnungen (SVG)

FONT = 'font-family="Arial,Helvetica,sans-serif"'


def _svg(w, h, inner):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" {FONT}>'
            f'<rect width="{w}" height="{h}" fill="#ffffff"/>{inner}</svg>')


def _num(x, y, n):
    """Orange Kreis mit weißer Nummer (wie bei den Beschriftungsaufgaben)."""
    return (f'<circle cx="{x}" cy="{y}" r="13" fill="#e2701a"/>'
            f'<text x="{x}" y="{y + 5.5}" font-size="15" font-weight="bold" fill="#fff" text-anchor="middle">{n}</text>')


def _label(x, y, text, anchor="middle", size=15, weight="normal", fill="#222"):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{text}</text>'


def _arrow(x1, y1, x2, y2, color="#333", w=2.5):
    ang = math.atan2(y2 - y1, x2 - x1)
    ax, ay = x2 - 11 * math.cos(ang - 0.4), y2 - 11 * math.sin(ang - 0.4)
    bx, by = x2 - 11 * math.cos(ang + 0.4), y2 - 11 * math.sin(ang + 0.4)
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}"/>'
            f'<polygon points="{x2},{y2} {ax:.1f},{ay:.1f} {bx:.1f},{by:.1f}" fill="{color}"/>')


def svg_gezeiten(nummern=True, mond_rechts=True):
    """Erde mit zwei Wasserbergen und Mond. nummern=True: Zahlen 1-6, sonst Wörter.

    1 Mond, 2 Anziehungskraft des Mondes, 3 Erde, 4 Flut (zweimal), 5 Ebbe (zweimal), 6 Fliehkraft der Erde.
    """
    s = 1 if mond_rechts else -1
    ex, ey = (200 if mond_rechts else 400), 170
    mx = ex + s * 330
    parts = []
    parts.append(f'<ellipse cx="{ex}" cy="{ey}" rx="104" ry="72" fill="#bfe0f3" stroke="#5aa6d1" stroke-width="2"/>')
    parts.append(f'<circle cx="{ex}" cy="{ey}" r="60" fill="#d9cfa8" stroke="#8a7a45" stroke-width="2"/>')
    parts.append(f'<circle cx="{mx}" cy="{ey}" r="26" fill="#cfcfcf" stroke="#777" stroke-width="2"/>')
    parts.append(_arrow(ex + s * 112, ey, mx - s * 36, ey, "#333"))
    parts.append(_arrow(ex - s * 112, ey, ex - s * 176, ey, "#333"))
    near, far = ex + s * 82, ex - s * 82
    top, bot = ey - 82, ey + 82
    if nummern:
        parts.append(_num(mx, ey - 48, 1))
        parts.append(_num(ex + s * 230, ey - 20, 2))
        parts.append(_num(ex, ey, 3))
        parts.append(_num(near, ey, 4))
        parts.append(_num(far, ey, 4))
        parts.append(_num(ex, top - 12, 5) + f'<line x1="{ex}" y1="{top + 1}" x2="{ex}" y2="{ey - 66}" stroke="#e2701a" stroke-width="2"/>')
        parts.append(_num(ex, bot + 12, 5) + f'<line x1="{ex}" y1="{bot - 1}" x2="{ex}" y2="{ey + 66}" stroke="#e2701a" stroke-width="2"/>')
        parts.append(_num(ex - s * 144, ey - 22, 6))
    else:
        parts.append(_label(mx, ey - 40, "Mond", weight="bold"))
        parts.append(_label(ex + s * 230, ey - 26, "Anziehungskraft", size=14))
        parts.append(_label(ex + s * 230, ey - 9, "des Mondes", size=14))
        parts.append(_label(ex, ey + 5, "Erde", weight="bold"))
        parts.append(_label(near, ey + 5, "Flut", size=14, weight="bold", fill="#1b5e8c"))
        parts.append(_label(far, ey + 5, "Flut", size=14, weight="bold", fill="#1b5e8c"))
        parts.append(_label(ex, top - 12, "Ebbe", size=14, weight="bold", fill="#1b5e8c"))
        parts.append(_label(ex, bot + 20, "Ebbe", size=14, weight="bold", fill="#1b5e8c"))
        parts.append(_label(ex - s * 144, ey - 26, "Fliehkraft", size=14))
        parts.append(_label(ex - s * 144, ey - 9, "der Erde", size=14))
    return _svg(600, 340, ''.join(parts))


def kurve_h(t, t_hw, hw, nw):
    """Wasserstand zur Zeit t (Minuten) bei Hochwasser um t_hw. Eine Tide dauert 12 h 25 min = 745 min."""
    return (hw + nw) / 2 + (hw - nw) / 2 * math.cos(2 * math.pi * (t - t_hw) / 745)


def svg_kurve(t_hw, hw, nw, hoehe_max=4.0):
    """Gezeitenkurve eines Tages (0 bis 24 Uhr). Waagerecht die Uhrzeit, senkrecht der Wasserstand in m."""
    W, H = 760, 395
    x0, x1, y0, y1 = 70, 730, 330, 30  # Rand des Diagramms (y0 unten, y1 oben)
    X = lambda t: x0 + (x1 - x0) * t / 1440
    Y = lambda h: y0 - (y0 - y1) * h / hoehe_max
    g = []
    for hh in range(25):
        x = X(hh * 60)
        major = hh % 3 == 0
        g.append(f'<line x1="{x:.1f}" y1="{y1}" x2="{x:.1f}" y2="{y0}" stroke="{"#c9c9c9" if major else "#e6e6e6"}" stroke-width="{1.2 if major else 1}"/>')
        if major:
            g.append(_label(round(x, 1), y0 + 22, f"{hh}", size=14))
    h = 0.0
    while h <= hoehe_max + 1e-9:
        y = Y(h)
        g.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" stroke="{"#c9c9c9" if abs(h - round(h)) < 1e-9 else "#e6e6e6"}" stroke-width="1"/>')
        g.append(_label(x0 - 8, round(y + 5, 1), de(h) if abs(h - round(h)) > 1e-9 else str(int(round(h))), anchor="end", size=14))
        h += 0.5
    pts = []
    for t in range(0, 1441, 15):
        pts.append(f"{X(t):.1f},{Y(kurve_h(t, t_hw, hw, nw)):.1f}")
    g.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="#1f78b4" stroke-width="3.5" stroke-linejoin="round"/>')
    g.append(f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}" stroke="#333" stroke-width="2"/><line x1="{x0}" y1="{y1}" x2="{x0}" y2="{y0}" stroke="#333" stroke-width="2"/>')
    g.append(_label((x0 + x1) // 2, y0 + 48, "Uhrzeit (Stunden)", size=15, weight="bold"))
    g.append(f'<text x="22" y="{(y0 + y1) // 2}" font-size="15" font-weight="bold" fill="#222" text-anchor="middle" transform="rotate(-90 22 {(y0 + y1) // 2})">Wasserstand in m</text>')
    return _svg(W, H, ''.join(g))


def svg_tabelle(kopf, zeilen, spalten_breit=None, schriftgroesse=17):
    """Einfache Tabelle als Bild (für den Tidenkalender)."""
    n = len(kopf)
    breit = spalten_breit or [110] + [130] * (n - 1)
    W = sum(breit) + 20
    rh = 38
    H = rh * (len(zeilen) + 1) + 20
    g = []
    y = 10
    x = 10
    for i, k in enumerate(kopf):
        g.append(f'<rect x="{x}" y="{y}" width="{breit[i]}" height="{rh}" fill="#dbe9f4" stroke="#7a8fa3"/>')
        g.append(_label(x + breit[i] / 2, y + rh / 2 + 6, k, size=schriftgroesse - 2, weight="bold"))
        x += breit[i]
    for r, row in enumerate(zeilen):
        x = 10
        y = 10 + rh * (r + 1)
        for i, c in enumerate(row):
            g.append(f'<rect x="{x}" y="{y}" width="{breit[i]}" height="{rh}" fill="{"#f7f7f7" if r % 2 else "#ffffff"}" stroke="#7a8fa3"/>')
            g.append(_label(x + breit[i] / 2, y + rh / 2 + 6, c, size=schriftgroesse, weight="bold" if i == 0 else "normal"))
            x += breit[i]
    return _svg(W, H, ''.join(g))


def tidenkalender(t0, tage=5):
    """Uhrzeiten für Hochwasser und Niedrigwasser, jeden Tag etwa 50 Minuten später.

    t0: erstes Hochwasser des ersten Tages (Minuten seit Mitternacht). Rückgabe: Liste je Tag mit
    (hw1, hw2, nw1, nw2) in Minuten seit Mitternacht oder None (Strich), dazu alle Ereignisse.
    """
    hws = [t0 + k * 745 for k in range(0, 2 * tage + 3)]
    nws = [round(t0 + 372.5 + k * 745 + 0.001) for k in range(-1, 2 * tage + 3)]
    tab = []
    for d in range(tage):
        lo, hi = 1440 * d, 1440 * (d + 1)
        h = [t for t in hws if lo <= t < hi]
        n = [t for t in nws if lo <= t < hi]
        assert 1 <= len(h) <= 2 and 1 <= len(n) <= 2, (d, h, n)
        tab.append((h[0] - lo, (h[1] - lo) if len(h) > 1 else None, n[0] - lo, (n[1] - lo) if len(n) > 1 else None))
    return tab


def kalender_svg(t0, tage=5):
    tab = tidenkalender(t0, tage)
    zeilen = []
    for d, (a, b, c, e) in enumerate(tab, 1):
        zeilen.append([f"{d}. Tag", hhmm(a), hhmm(b) if b is not None else "–", hhmm(c), hhmm(e) if e is not None else "–"])
    svg = svg_tabelle(["Tag", "Hochwasser", "Hochwasser", "Niedrigwasser", "Niedrigwasser"], zeilen, [90, 140, 140, 160, 160])
    alt = "Tidenkalender (Uhrzeiten): " + "; ".join(f"{z[0]}: HW {z[1]} und {z[2]}, NW {z[3]} und {z[4]}" for z in zeilen)
    return tab, svg, alt


def svg_watt():
    """Querschnitt vom Meer bis zum Deich: Boden, Wasser bei Hochwasser und die Marken für mittleres Niedrig- und Hochwasser."""
    g = []
    mnw, mhw = 215, 160
    # Wasser bei Hochwasser (bis zur Höhe des mittleren Hochwassers)
    g.append(f'<polygon points="0,{mhw} 460,{mhw} 260,{mnw} 0,262" fill="#cfe7f6"/>')
    # Boden
    g.append('<polygon points="0,262 260,215 460,160 520,150 640,146 740,70 760,70 760,330 0,330" fill="#cdb98a" stroke="#8a7a45" stroke-width="2"/>')
    g.append('<polyline points="460,160 520,150 640,146" fill="none" stroke="#6aa84f" stroke-width="7"/>')
    g.append('<polyline points="640,146 740,70" fill="none" stroke="#3f9b4f" stroke-width="9"/>')
    g.append(f'<line x1="0" y1="{mhw}" x2="460" y2="{mhw}" stroke="#1f78b4" stroke-width="2" stroke-dasharray="7 5"/>')
    g.append(f'<line x1="0" y1="{mnw}" x2="260" y2="{mnw}" stroke="#1f78b4" stroke-width="2" stroke-dasharray="7 5"/>')
    for x in (260, 460, 640):
        g.append(f'<line x1="{x}" y1="40" x2="{x}" y2="300" stroke="#555" stroke-width="1.8" stroke-dasharray="3 5"/>')
    return g, mnw, mhw


def svg_watt_zonen(nummern=True):
    g, mnw, mhw = svg_watt()
    mitten = [(130, 1, "Meer"), (360, 2, "Watt"), (550, 3, "Salzwiese"), (700, 4, "Deich")]
    for x, n, name in mitten:
        if nummern:
            g.append(_num(x, 62, n))
        else:
            g.append(_label(x, 66, name, weight="bold"))
    g.append(_label(8, mhw - 8, "mittleres Hochwasser", anchor="start", size=13, fill="#1f5f8f"))
    g.append(_label(8, mnw - 8, "mittleres Niedrigwasser", anchor="start", size=13, fill="#1f5f8f"))
    return _svg(760, 330, ''.join(g))


def svg_deich(nummern=True, meer_links=True, reihenfolge=(1, 2, 3, 4, 5, 6, 7, 8, 9)):
    """Deich-Querschnitt. Nummern: Seeseite, Landseite, Deichkrone, Grasdecke, Klei, Sandkern, Deichfuß, Sturmflutwasserstand, Hochwasser.

    reihenfolge ordnet jedem Teil (in dieser Reihenfolge) eine Nummer zu.
    """
    W, H = 640, 360
    names = ["Seeseite", "Landseite", "Deichkrone", "Grasdecke", "Klei", "Sandkern", "Deichfuß", "Sturmflutwasserstand", "Hochwasser"]
    nr = dict(zip(names, reihenfolge))
    g = []
    # Boden
    g.append('<rect x="0" y="300" width="640" height="60" fill="#c9ad7a"/>')
    # Wasser (Hochwasser und Sturmflut)
    g.append('<polygon points="0,175 232,175 80,300 0,300" fill="#d9ecf8"/>')
    g.append('<polygon points="0,255 134,255 80,300 0,300" fill="#a9d1ec"/>')
    # Deichkörper: außen, Klei, Sand
    g.append('<polygon points="80,300 320,100 380,100 500,300" fill="#9a6b43"/>')
    g.append('<polygon points="96,300 324,112 376,112 484,300" fill="#b88a5a"/>')
    g.append('<polygon points="150,300 336,140 364,140 440,300" fill="#f0d9a0"/>')
    g.append('<polyline points="80,300 320,100 380,100 500,300" fill="none" stroke="#3f9b4f" stroke-width="10" stroke-linejoin="round"/>')
    # Steine am Deichfuß (seeseitig)
    for sx, sy in ((88, 292), (104, 296), (121, 290), (137, 295), (112, 281), (96, 285)):
        g.append(f'<circle cx="{sx}" cy="{sy}" r="7" fill="#8d8d8d" stroke="#555"/>')
    g.append('<line x1="0" y1="175" x2="232" y2="175" stroke="#1f78b4" stroke-width="2.2" stroke-dasharray="7 5"/>')
    g.append('<line x1="0" y1="255" x2="134" y2="255" stroke="#1f78b4" stroke-width="2.2"/>')
    g.append(_label(40, 285, "Meer", size=15, weight="bold", fill="#1f5f8f"))
    g.append(_label(560, 285, "Land", size=15, weight="bold", fill="#6b5535"))
    # Zeiger: (Name, Zielpunkt, Position der Beschriftung)
    ziele = {
        "Seeseite": ((190, 210), (150, 140)),
        "Landseite": ((438, 215), (520, 150)),
        "Deichkrone": ((350, 100), (350, 52)),
        "Grasdecke": ((290, 128), (230, 70)),
        "Klei": ((224, 215), (262, 258)),
        "Sandkern": ((380, 215), (385, 262)),
        "Deichfuß": ((100, 288), (62, 332)),
        "Sturmflutwasserstand": ((40, 175), (110, 140)),
        "Hochwasser": ((20, 255), (50, 222)),
    }
    # Beschriftung mit Wörtern: (Textposition x, y, Anker, Ende der Linie oder None)
    tpos = {
        "Seeseite": (165, 126, "middle", (176, 134)),
        "Landseite": (520, 150, "middle", (506, 157)),
        "Deichkrone": (350, 64, "middle", (350, 71)),
        "Grasdecke": (222, 78, "middle", (243, 86)),
        "Klei": (262, 262, "middle", (252, 248)),
        "Sandkern": (385, 264, "middle", (384, 250)),
        "Deichfuß": (62, 334, "middle", (76, 322)),
        "Sturmflutwasserstand": (8, 167, "start", None),
        "Hochwasser": (8, 247, "start", None),
    }
    for name, (z, p) in ziele.items():
        if nummern:
            g.append(f'<line x1="{z[0]}" y1="{z[1]}" x2="{p[0]}" y2="{p[1]}" stroke="#333" stroke-width="1.4"/>')
            g.append(_num(p[0], p[1], nr[name]))
        else:
            tx, ty, anker, ende = tpos[name]
            if ende:
                g.append(f'<line x1="{z[0]}" y1="{z[1]}" x2="{ende[0]}" y2="{ende[1]}" stroke="#333" stroke-width="1.4"/>')
            g.append(f'<text x="{tx}" y="{ty}" font-size="15" font-weight="bold" fill="#1b1b1b" text-anchor="{anker}" '
                     f'stroke="#fff" stroke-width="4" paint-order="stroke" stroke-linejoin="round">{name}</text>')
    inner = ''.join(g) if meer_links else _spiegeln_ok(g, W)
    return _svg(W, H, inner)


def _spiegeln_ok(g, W):
    """Spiegelt die Zeichnung, aber nicht die Beschriftungen (Kreise und Text bleiben lesbar)."""
    res = []
    for el in g:
        if el.startswith('<circle') and 'r="13"' in el or el.startswith('<text') or ('<text' in el and 'r="13"' in el):
            res.append(_mirror_text_group(el, W))
        else:
            res.append(f'<g transform="translate({W} 0) scale(-1 1)">{el}</g>')
    return ''.join(res)


def _mirror_text_group(el, W):
    def fix_x(m):
        return f'{m.group(1)}="{W - float(m.group(2)):g}"'
    el = re.sub(r'\b(cx|x)="([0-9.]+)"', fix_x, el)
    # Beschriftungen, die links oder rechts ansetzen, wechseln beim Spiegeln die Seite
    if 'text-anchor="start"' in el:
        el = el.replace('text-anchor="start"', 'text-anchor="end"')
    elif 'text-anchor="end"' in el:
        el = el.replace('text-anchor="end"', 'text-anchor="start"')
    return el


# Ein bequemer Weg für Texte in Aufgaben mit Zeitangaben
def stunden_min(minuten):
    h, m = divmod(int(minuten), 60)
    return f"{h} Stunden und {m} Minuten" if h else f"{m} Minuten"
