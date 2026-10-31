"""Kleiner Notensatz-Zeichner für die Lernhilfe: erzeugt SVG-Bilder für Aufgaben.

Nur Violinschlüssel, einfache Noten (ganze, halbe, Viertel, Achtel), Pausen,
Kreuz/Be, Taktarten und Taktstriche. Die Glyphen (Schlüssel, Pausen, Vorzeichen,
Ziffern) stehen als Pfade in glyphs.json (aus GNU FreeFont und DejaVu Sans Bold
herausgezogen), so braucht das SVG später keine Schrift.

Maße: Eine Notenlinie hat den Abstand S = 10 Einheiten. Stufe p = 0 ist die
untere Linie (e'), jede Stufe ist eine halbe Linienabstand höher.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
GLYPHS = json.load(open(os.path.join(HERE, 'glyphs.json')))

S = 10.0
INK = '#1a1a1a'
GREY = '#6b6b6b'
ORANGE = '#c2410c'
SANS = 'Helvetica, Arial, sans-serif'

LETTER = {'c': 0, 'd': 1, 'e': 2, 'f': 3, 'g': 4, 'a': 5, 'h': 6}


def pitch(name):
    """Notenname wie "fis'" oder "c''" -> (Stufe, Vorzeichen). e' = 0."""
    m = re.fullmatch(r"([cdefgah])(is|es)?('*)", name)
    if not m:
        raise ValueError('Notenname?', name)
    letter, acc, apo = m.groups()
    octave = len(apo)
    step = (octave - 1) * 7 + LETTER[letter] - 2
    return step, {'is': '#', 'es': 'b', None: None}[acc]


class Sym:
    """Ein Zeichen in einem Takt: Note, Pause oder Lücke."""

    def __init__(self, kind, dur=None, p=None, acc=None, beam=None, label=None,
                 num=None, w=None, hint=None, color=None, nostem=False, pos=None, accafter=False, space=None):
        self.kind, self.dur, self.p, self.acc = kind, dur, p, acc
        self.beam, self.label, self.num = beam, label, num
        self.w, self.hint, self.color, self.nostem = w, hint, color, nostem
        self.pos, self.accafter, self.space = pos, accafter, space
        self.x = 0.0      # Mitte des Notenkopfs bzw. der Pause
        self.left = 0.0   # linker Rand (für Vorzeichen)


def N(name, dur, **kw):
    p, acc = pitch(name)
    return Sym('note', dur=dur, p=p, acc=acc, **kw)


def R(dur, **kw):
    return Sym('rest', dur=dur, **kw)


def GAP(hint='Lücke', w=26):
    return Sym('gap', w=w, hint=hint)


BASE_W = {0.5: 27, 1: 36, 2: 56, 4: 84}


def f1(x):
    return ('%.1f' % x).rstrip('0').rstrip('.')


def glyph(name, x, y, height=None, width=None, anchor='center', valign='center', fill=INK):
    """Setzt einen Glyphen so, dass seine Hülle (Höhe) die gewünschte Größe hat."""
    g = GLYPHS[name]
    x0, y0, x1, y1 = g['bbox']
    sc = (height / (y1 - y0)) if height else (width / (x1 - x0))
    w = (x1 - x0) * sc
    h = (y1 - y0) * sc
    left = x - w / 2 if anchor == 'center' else x
    top = y - h / 2 if valign == 'center' else y
    # Pfad: Schrift-y zeigt nach oben -> spiegeln
    tx = left - x0 * sc
    ty = top + y1 * sc
    return '<path transform="translate(%s %s) scale(%s %s)" d="%s" fill="%s"/>' % (
        f1(tx), f1(ty), '%.5f' % sc, '%.5f' % -sc, g['d'], fill), w


class Row:
    """Eine Notenzeile mit mehreren Takten."""

    def __init__(self, bars, ts=None, tsbox=None, numbers=None, end='final',
                 width=None, clef=True, label=None, cont=False, ts_size=1.0):
        self.bars, self.ts, self.tsbox = bars, ts, tsbox
        self.numbers, self.end, self.width = numbers, end, width
        self.clef, self.label, self.cont = clef, label, cont

    # ---- Layout ----
    def layout(self):
        x = 6.0
        self.x_clef = x
        if self.clef:
            x += 30
        if self.ts:
            self.x_ts = x + 2
            x += 26
        if self.tsbox:
            self.x_tsbox = x + 4
            x += 38
        self.x_bars_start = x
        # natürliche Breiten
        nat = []
        for bar in self.bars:
            w = 14
            for s in bar:
                if s.kind == 'gap':
                    w += s.w + 6
                else:
                    w += (s.space or BASE_W[s.dur]) + (13 if s.acc else 0)
            w += 6
            nat.append(w)
        total = sum(nat)
        avail = (self.width - x - 8) if self.width else total
        fac = avail / total if self.width else 1.0
        fac = max(fac, 0.8)
        cur = x
        self.bar_x = []
        for bar, nw in zip(self.bars, nat):
            bw = nw * fac
            self.bar_x.append((cur, cur + bw))
            sx = cur + 14 * fac
            for s in bar:
                if s.kind == 'gap':
                    s.left = sx
                    s.x = sx + s.w / 2
                    sx += (s.w + 6) * fac
                else:
                    wd = ((s.space or BASE_W[s.dur]) + (13 if s.acc else 0)) * fac
                    s.left = sx
                    lead = 13 if (s.acc and not s.accafter) else 0
                    s.x = sx + lead + (wd - (13 if s.acc else 0)) / 2 - 2
                    sx += wd
            cur += bw
        self.w = cur + 6

    def bottom(self):
        """Platz unter der untersten Linie (für Beschriftungen und Hilfslinien)."""
        syms = [s for bar in self.bars for s in bar]
        if any(s.num and s.label for s in syms):
            return 64
        if any(s.label for s in syms):
            return 48
        return 26

    # ---- Zeichnen ----
    def draw(self, y_top):
        self.layout()
        yb = y_top + 4 * S
        out = []
        x_end = self.bar_x[-1][1]
        # Linien
        for i in range(5):
            y = y_top + i * S
            out.append('<line x1="2" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.1"/>' % (f1(y), f1(x_end), f1(y), INK))
        # Schlüssel
        if self.clef:
            gx, _ = glyph('clef', self.x_clef, y_top + 2.9 * S, height=5.6 * S, anchor='start', valign='center')
            out.append(gx)
        if self.ts:
            a, b = self.ts.split('/')
            ga, _ = glyph('d' + a, self.x_ts + 9, y_top + 1.0 * S, height=1.9 * S)
            gb, _ = glyph('d' + b, self.x_ts + 9, y_top + 3.0 * S, height=1.9 * S)
            out.append(ga)
            out.append(gb)
        if self.tsbox:
            bx = self.x_tsbox
            out.append('<rect x="%s" y="%s" width="26" height="%s" fill="none" stroke="%s" stroke-width="1.1" stroke-dasharray="4 3"/>' % (f1(bx), f1(y_top - 4), f1(4 * S + 8), GREY))
            out.append('<text x="%s" y="%s" font-family="%s" font-size="10.5" fill="%s" text-anchor="middle">%s</text>' % (f1(bx + 13), f1(y_top - 10), SANS, GREY, self.tsbox))
        # Takte
        for bi, (bar, (bx0, bx1)) in enumerate(zip(self.bars, self.bar_x)):
            if self.numbers is not None:
                out.append('<text x="%s" y="%s" font-family="%s" font-size="10.5" fill="%s">%s</text>' % (f1(bx0 + 4), f1(y_top - 10), SANS, GREY, self.numbers + bi))
            last = bi == len(self.bars) - 1
            if not last or self.end == 'bar':
                out.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.2"/>' % (f1(bx1), f1(y_top), f1(bx1), f1(yb), INK))
            elif self.end == 'final':
                out.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.2"/>' % (f1(bx1 - 5), f1(y_top), f1(bx1 - 5), f1(yb), INK))
                out.append('<rect x="%s" y="%s" width="3.4" height="%s" fill="%s"/>' % (f1(bx1 - 2.4), f1(y_top), f1(4 * S), INK))
            # Zeichen
            self._draw_bar(bar, y_top, yb, out)
        return out, yb

    def _draw_bar(self, bar, y_top, yb, out):
        ystep = lambda p: yb - p * S / 2.0
        i = 0
        while i < len(bar):
            s = bar[i]
            if s.kind == 'gap':
                out.append('<rect x="%s" y="%s" width="%s" height="%s" fill="none" stroke="%s" stroke-width="1.1" stroke-dasharray="4 3"/>' % (f1(s.left), f1(y_top - 4), f1(s.w), f1(4 * S + 8), GREY))
                if s.hint:
                    out.append('<text x="%s" y="%s" font-family="%s" font-size="10.5" fill="%s" text-anchor="middle">%s</text>' % (f1(s.x), f1(y_top - 10), SANS, GREY, s.hint))
            elif s.kind == 'rest':
                self._rest(s, y_top, yb, out)
            else:
                # Balken: nächstes Achtel mit beam='start'
                if s.beam == 'start' and i + 1 < len(bar):
                    self._beamed(s, bar[i + 1], yb, out)
                    i += 2
                    continue
                self._note(s, yb, out)
            self._labels(s, y_top, yb, out)
            i += 1

    def _labels(self, s, y_top, yb, out):
        ly = yb + 38
        if s.label:
            out.append('<text x="%s" y="%s" font-family="%s" font-size="13" font-weight="700" fill="%s" text-anchor="middle">%s</text>' % (f1(s.x), f1(max(ly, yb + 36)), SANS, s.color or INK, s.label))
        if s.num:
            out.append('<text x="%s" y="%s" font-family="%s" font-size="10.5" font-weight="700" fill="%s" text-anchor="middle">%s</text>' % (f1(s.x), f1(max(ly, yb + 36) + (14 if s.label else 0)), SANS, ORANGE, s.num))

    def _rest(self, s, y_top, yb, out):
        ymid = yb - 4.0 * S / 2.0  # mittlere Linie
        x = s.x
        if s.dur == 4:
            # hängt unter der 4. Linie (von unten gezählt); pos = Stufe der Linie, an der sie hängt
            y = yb - (s.pos if s.pos is not None else 6) * S / 2.0
            out.append('<rect x="%s" y="%s" width="14" height="5.2" fill="%s"/>' % (f1(x - 7), f1(y), INK))
        elif s.dur == 2:
            # sitzt auf der mittleren Linie; pos = Stufe der Linie, auf der sie sitzt
            y = yb - (s.pos if s.pos is not None else 4) * S / 2.0
            out.append('<rect x="%s" y="%s" width="14" height="5.2" fill="%s"/>' % (f1(x - 7), f1(y - 5.2), INK))
        elif s.dur == 1:
            g, _ = glyph('rest4', x, ymid - 0.15 * S, height=3.2 * S)
            out.append(g)
        elif s.dur == 0.5:
            g, _ = glyph('rest8', x, ymid - 0.35 * S, height=2.0 * S)
            out.append(g)

    def _head(self, s, y, out):
        x = s.x
        if s.dur == 4:
            out.append('<ellipse cx="%s" cy="%s" rx="7.4" ry="4.9" fill="%s"/>' % (f1(x), f1(y), INK))
            out.append('<ellipse cx="%s" cy="%s" rx="3.5" ry="4.2" fill="#fff" transform="rotate(38 %s %s)"/>' % (f1(x), f1(y), f1(x), f1(y)))
        elif s.dur == 2:
            out.append('<ellipse cx="%s" cy="%s" rx="6.4" ry="4.5" fill="%s" transform="rotate(-22 %s %s)"/>' % (f1(x), f1(y), INK, f1(x), f1(y)))
            out.append('<ellipse cx="%s" cy="%s" rx="4.7" ry="2.3" fill="#fff" transform="rotate(-30 %s %s)"/>' % (f1(x), f1(y), f1(x), f1(y)))
        else:
            out.append('<ellipse cx="%s" cy="%s" rx="6.4" ry="4.5" fill="%s" transform="rotate(-22 %s %s)"/>' % (f1(x), f1(y), INK, f1(x), f1(y)))

    def _extras(self, s, yb, out):
        y = yb - s.p * S / 2.0
        x = s.x
        # Hilfslinien
        if s.p <= -2:
            for q in range(-2, s.p - 1, -2):
                yy = yb - q * S / 2.0
                out.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.1"/>' % (f1(x - 10.5), f1(yy), f1(x + 10.5), f1(yy), INK))
        if s.p >= 10:
            for q in range(10, s.p + 1, 2):
                yy = yb - q * S / 2.0
                out.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.1"/>' % (f1(x - 10.5), f1(yy), f1(x + 10.5), f1(yy), INK))
        # Vorzeichen
        ax = x + 17 if s.accafter else x - 15
        if s.acc == '#':
            g, _ = glyph('sharp', ax, y, height=2.7 * S)
            out.append(g)
        elif s.acc == 'b':
            g, _ = glyph('flat', ax + 1, y - 0.55 * S, height=2.7 * S)
            out.append(g)

    def _note(self, s, yb, out):
        y = yb - s.p * S / 2.0
        self._extras(s, yb, out)
        self._head(s, y, out)
        if s.dur == 4 or s.nostem:
            return
        up = s.p < 4
        if up:
            sx = s.x + 6.0
            y2 = y - 3.5 * S
            out.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.4"/>' % (f1(sx), f1(y - 0.5), f1(sx), f1(y2), INK))
            if s.dur == 0.5:
                out.append(flag(sx, y2, True))
        else:
            sx = s.x - 6.0
            y2 = y + 3.5 * S
            out.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.4"/>' % (f1(sx), f1(y + 0.5), f1(sx), f1(y2), INK))
            if s.dur == 0.5:
                out.append(flag(sx, y2, False))

    def _beamed(self, a, b, yb, out):
        for s in (a, b):
            self._extras(s, yb, out)
            self._head(s, yb - s.p * S / 2.0, out)
        up = (a.p + b.p) / 2.0 < 4
        ya, yb2 = yb - a.p * S / 2.0, yb - b.p * S / 2.0
        L = 3.5 * S
        if up:
            xa, xb = a.x + 6.0, b.x + 6.0
            ta, tb = ya - L, yb2 - L
            d = max(-6.0, min(6.0, tb - ta))
            ta0 = min(ta, tb - d)
            tb0 = ta0 + d
            th = 4.6
            out.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.4"/>' % (f1(xa), f1(ya - 0.5), f1(xa), f1(ta0), INK))
            out.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.4"/>' % (f1(xb), f1(yb2 - 0.5), f1(xb), f1(tb0), INK))
            out.append('<polygon points="%s,%s %s,%s %s,%s %s,%s" fill="%s"/>' % (f1(xa - 0.7), f1(ta0), f1(xb + 0.7), f1(tb0), f1(xb + 0.7), f1(tb0 + th), f1(xa - 0.7), f1(ta0 + th), INK))
        else:
            xa, xb = a.x - 6.0, b.x - 6.0
            ta, tb = ya + L, yb2 + L
            d = max(-6.0, min(6.0, tb - ta))
            ta0 = max(ta, tb - d)
            tb0 = ta0 + d
            th = 4.6
            out.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.4"/>' % (f1(xa), f1(ya + 0.5), f1(xa), f1(ta0), INK))
            out.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.4"/>' % (f1(xb), f1(yb2 + 0.5), f1(xb), f1(tb0), INK))
            out.append('<polygon points="%s,%s %s,%s %s,%s %s,%s" fill="%s"/>' % (f1(xa - 0.7), f1(ta0), f1(xb + 0.7), f1(tb0), f1(xb + 0.7), f1(tb0 - th), f1(xa - 0.7), f1(ta0 - th), INK))
        self._labels(a, 0, yb, out)
        self._labels(b, 0, yb, out)


def ystep_y(yb, p):
    return yb - p * S / 2.0


def flag(x, y, up):
    """Achtelfähnchen am Stielende (x, y)."""
    if up:
        d = 'M%s %s C%s %s %s %s %s %s C%s %s %s %s %s %s Z' % (
            f1(x - 0.7), f1(y), f1(x + 2), f1(y + 7), f1(x + 11), f1(y + 9), f1(x + 9), f1(y + 22),
            f1(x + 9), f1(y + 14), f1(x + 3), f1(y + 13), f1(x - 0.7), f1(y + 11))
    else:
        d = 'M%s %s C%s %s %s %s %s %s C%s %s %s %s %s %s Z' % (
            f1(x - 0.7), f1(y), f1(x + 2), f1(y - 7), f1(x + 11), f1(y - 9), f1(x + 9), f1(y - 22),
            f1(x + 9), f1(y - 14), f1(x + 3), f1(y - 13), f1(x - 0.7), f1(y - 11))
    return '<path d="%s" fill="%s"/>' % (d, INK)


def doc(rows, title=None, scale=1.15, width=None, gap=62, tag=None, tags=None, pad=10):
    """Mehrere Zeilen untereinander -> ein SVG. rows: Row oder (Beschriftung, Row)."""
    parts = []
    y = pad + (22 if title else 0)
    if title:
        pass
    maxw = 0
    for item in rows:
        lab = None
        row = item
        if isinstance(item, tuple):
            lab, row = item
        row.width = row.width or width
        top = y + 16
        frag, yb = row.draw(top)
        if lab:
            parts.append('<text x="%s" y="%s" font-family="%s" font-size="14" font-weight="700" fill="%s">%s</text>' % (f1(4), f1(top - 8), SANS, INK, lab))
        parts.extend(frag)
        maxw = max(maxw, row.w)
        y = yb + gap
        last_extra = row.bottom()
    h = y - gap + last_extra
    if title:
        parts.insert(0, '<text x="%s" y="20" font-family="%s" font-size="15" font-weight="700" fill="%s" text-anchor="middle">%s</text>' % (f1((width or maxw) / 2), SANS, INK, title))
    w = (width or maxw) + 4
    svg = '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %s %s" role="img"><rect width="100%%" height="100%%" fill="#fff"/>%s</svg>' % (
        round(w * scale), round(h * scale), f1(w), f1(h), ''.join(parts))
    return svg
