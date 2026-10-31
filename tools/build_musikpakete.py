#!/usr/bin/env python3
"""Erzeugt die drei Musik-Lernpakete (Klasse 6) im Ordner pakete/.

Die Notenbilder zeichnet tools/notation.py als SVG, die Lösungen ergeben sich
aus denselben Daten wie die Bilder. Aufruf: python3 tools/build_musikpakete.py
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from notation import Row, N, R, GAP, doc, ORANGE, INK  # noqa: E402

OUT = os.path.join(HERE, '..', 'pakete')
os.makedirs(OUT, exist_ok=True)


def write(name, obj):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
        f.write('\n')


# =====================================================================
# Notenbilder
# =====================================================================
def bar_img(bars, width=560, ts=None, tsbox=None, numbers=None, end='final'):
    return doc([Row(bars, ts=ts, tsbox=tsbox, numbers=numbers, end=end, width=width)], width=width)


def rows_img(rows, width=520, scale=1.0, gap=40):
    return doc(rows, width=width, scale=scale, gap=gap)


def img_notennamen():
    names = ["c'", "d'", "e'", "f'", "g'", "a'", "h'", "c''", "d''", "e''"]
    syms = []
    for i, n in enumerate(names):
        on_line = i % 2 == 0   # c' (Hilfslinie), e', g', h', d'' liegen auf Linien
        syms.append(N(n, 1, nostem=True, label=n, color=INK if on_line else ORANGE, space=46))
    return doc([Row([syms], end='final', width=600)], width=600, gap=56)


def img_notenwerte(mit_pausen=False):
    noten = [N("g'", 4, label='Ganze Note', num='4 Schläge', space=112),
             N("g'", 2, label='Halbe Note', num='2 Schläge', space=112),
             N("g'", 1, label='Viertelnote', num='1 Schlag', space=112),
             N("g'", .5, label='Achtelnote', num='½ Schlag', space=112)]
    rows = [Row([noten], end='final', width=560)]
    if mit_pausen:
        pausen = [R(4, label='Ganze Pause', num='4 Schläge', space=112),
                  R(2, label='Halbe Pause', num='2 Schläge', space=112),
                  R(1, label='Viertelpause', num='1 Schlag', space=112),
                  R(.5, label='Achtelpause', num='½ Schlag', space=112)]
        rows.append(Row([pausen], end='final', width=560))
    return doc(rows, width=560, gap=62)


def img_kreuz_merk():
    return doc([Row([[N("f'", 1, label="f'", space=90), N("fis'", 1, label="fis'", space=90),
                      N("c''", 1, label="c''", space=90), N("cis''", 1, label="cis''", space=90)]],
                    end='final', width=470)], width=470, gap=56)


def img_loesung_papier():
    a = Row([[N("g'", 1, label="g'"), N("c''", 1, label="c''"), N("e'", 1, label="e'"), N("a'", 1, label="a'")]],
            ts='4/4', end='final', width=420)
    b = Row([[N("g'", 1, label="g'"), N("ais'", 1, label="ais'"), N("h'", 1, label="h'"), N("c''", 1, label="c''")]],
            ts='4/4', end='final', width=420)
    return doc([('Noten setzen: g\', c\'\', e\', a\'', a), ('Melodie schreiben', b)], width=420, gap=62)


# ---- Paket 1 -------------------------------------------------------
def img_lesen():
    notes = [("f'", 'a)'), ("h'", 'b)'), ("c'", 'c)'), ("d''", 'd)'), ("a'", 'e)')]
    return bar_img([[N(n, 1, label=l, space=62) for n, l in notes]], width=500)


def img_setzen():
    # Zu jedem Ton die passende Note suchen (A bis E)
    notes = [("c''", 'A'), ("e'", 'B'), ("a'", 'C'), ("g'", 'D'), ("d''", 'E')]
    return bar_img([[N(n, 1, label=l, space=62) for n, l in notes]], width=500)


def img_melodie():
    bars = [[N("e'", 1, num=1), N("g'", 1, num=2), N("h'", 2, num=3)],
            [N("c''", 1, num=4), N("a'", .5, beam='start', num=5), N("g'", .5, num=6), N("f'", 1, num=7), N("d'", 1, num=8)],
            [N("d''", 2, num=9), N("h'", 1, num=10), N("g'", 1, num=11)]]
    return doc([Row(bars, ts='4/4', numbers=1, end='final', width=600)], width=600, title='Kleine Melodie', gap=62)


def img_werte():
    notes = [(N("c''", 1), 'a)'), (N("f'", 2), 'b)'), (N("g'", .5), 'c)'), (N("e''", 4), 'd)'), (N("h'", 2), 'e)')]
    for s, l in notes:
        s.label = l
        s.space = 70 if s.dur != .5 else 62
    return bar_img([[s for s, _ in notes]], width=560)


def img_kreuz():
    return bar_img([[N("fis'", 1, label='a)', space=150), N("cis''", 1, label='b)', space=150)]], width=420)


def img_ben():
    return bar_img([[N("h'", 2, space=120)]], width=300)


def img_melodie_zeilen():
    def zeile(namen, accafter_idx=None):
        syms = []
        for i, n in enumerate(namen):
            syms.append(N(n, 1, accafter=(i == accafter_idx), space=60))
        return Row([syms], ts='4/4', end='final', width=420)
    rows = [('A)', zeile(["g'", "a'", "h'", "c''"])),
            ('B)', zeile(["g'", "ais'", "h'", "c''"], accafter_idx=1)),
            ('C)', zeile(["g'", "ais'", "h'", "c''"])),
            ('D)', zeile(["gis'", "a'", "h'", "c''"]))]
    return doc(rows, width=420, gap=46)


# ---- Paket 2 -------------------------------------------------------
def img_pausen_lesen():
    return bar_img([[R(2, label='a)', space=100), R(.5, label='b)', space=100), R(4, label='c)', space=100), R(1, label='d)', space=100)]], width=500)


def img_pausen_lage():
    rows = [('A)', Row([[R(4)]], end='final', width=300)),
            ('B)', Row([[R(2)]], end='final', width=300)),
            ('C)', Row([[R(2, pos=2)]], end='final', width=300)),
            ('D)', Row([[R(4, pos=4)]], end='final', width=300))]
    return doc(rows, width=300, gap=40)


def img_takt_luecke():
    a = Row([[N("g'", 1), N("f'", 1), N("e'", 1), GAP('Lücke')]], ts='4/4', end='final', width=500)
    b = Row([[N("a'", 1), N("g'", 1), GAP('Lücke')]], ts='4/4', end='final', width=500)
    c = Row([[N("g'", .5), GAP('Lücke'), N("a'", 1), N("h'", 2)]], ts='4/4', end='final', width=500)
    return doc([('a)', a), ('b)', b), ('c)', c)], width=500, gap=44)


def img_taktart():
    a = Row([[N("g'", .5, beam='start'), N("a'", .5), N("h'", 1), R(1)]], tsbox='Taktart?', end='final', width=500)
    b = Row([[R(1), N("g'", 1)]], tsbox='Taktart?', end='final', width=500)
    c = Row([[N("f'", 1), R(1), N("g'", 2)]], tsbox='Taktart?', end='final', width=500)
    return doc([('a)', a), ('b)', b), ('c)', c)], width=500, gap=44)


def img_lisa():
    return bar_img([[N("g'", 1, space=110), N("h'", 2, space=130), N("g'", 1, space=110)]], width=440, ts='3/4')


def img_takte_wahl():
    def zeile(syms):
        return Row([syms], ts='4/4', end='final', width=420)
    rows = [('A)', zeile([N("h'", 2, space=100), R(1), N("g'", 1)])),
            ('B)', zeile([N("g'", 2, space=100), R(1), N("a'", .5)])),
            ('C)', zeile([N("e'", 1), N("g'", 2, space=100), R(1)])),
            ('D)', zeile([N("g'", 1), R(1), N("a'", 1)]))]
    return doc(rows, width=420, gap=46)


# ---- Paket 3: Das Wanderlied ---------------------------------------
def img_wanderlied(luecken=True):
    r1 = Row([[N("c'", 1), N("d'", 1), N("e'", 1), N("f'", 1)],
              [N("g'", 2), N("e'", 1), N("c'", 1)],
              [N("d'", 1), N("f'", 1), N("a'", 1), N("f'", 1)],
              [N("e'", 1), N("g'", 1), R(2)]],
             tsbox='Taktart?' if luecken else None, ts=None if luecken else '4/4',
             numbers=1, end='bar', width=720)
    r2 = Row([[N("e'", .5, beam='start'), N("f'", .5), N("gis'", 1), N("a'", 1), N("a'", 1)],
              [N("h'", 2), N("g'", 1), GAP('Lücke') if luecken else R(1)],
              [R(.5), N("g'", .5), N("f'", 1), N("e'", 1), N("d'", 1)],
              [N("e'", 1), N("d'", 1), N("c'", 2)]],
             numbers=5, end='final', width=720)
    return doc([r1, r2], title='Das Wanderlied', width=720, gap=64)


# =====================================================================
# Bausteine
# =====================================================================
def fraction_alts(*first):
    return '|'.join(first)


HALB = "½|1/2|0,5|0.5|halber|ein halber"
HALBE_NOTE = "halbe Note|halbe|halbe-Note|halbenote"
VIERTELNOTE = "Viertelnote|Viertel|Viertel-Note|Viertel Note|viertelnote"
ACHTELNOTE = "Achtelnote|Achtel|Achtel-Note|Achtel Note"
GANZE_NOTE = "ganze Note|ganze|ganze-Note|ganzenote"
GANZE_PAUSE = "ganze Pause|ganze|ganze-Pause|ganzepause"
HALBE_PAUSE = "halbe Pause|halbe|halbe-Pause|halbepause"
VIERTELPAUSE = "Viertelpause|Viertel|Viertel-Pause|Viertel Pause|viertelpause"
ACHTELPAUSE = "Achtelpause|Achtel|Achtel-Pause|Achtel Pause|achtelpause"

MERKBILD_ALT = 'Notenwerte mit ihren Schlägen: ganze Note 4, halbe Note 2, Viertelnote 1, Achtelnote ½'

# =====================================================================
# Paket 1: Notennamen, Notenwerte, Vorzeichen
# =====================================================================
p1 = {
 "typ": "lernpaket", "version": 1,
 "id": "musik-6-notennamen-notenwerte-vorzeichen",
 "titel": "Musik Klasse 6: Notennamen, Notenwerte, Vorzeichen",
 "fach": "Musik", "klasse": "6",
 "beschreibung": "Noten im Violinschlüssel lesen, Notenwerte und Schläge bestimmen, das Kreuz. Die Zeichenaufgaben vom Papier sind hier als Auswahlaufgaben gebaut.",
 "hinweis": "Hier zählt jede Lücke einzeln, deshalb gibt es mehr Punkte als auf dem Papier. Im Heft gilt die Schreibweise aus dem Unterricht (z. B. beim Hochkomma). Zeichnen bleibt Papierarbeit: Im Lernblatt steht, wie man es mit einem leeren Blatt übt.",
 "lernblatt": [
  {"titel": "Notennamen im Violinschlüssel",
   "bild": img_notennamen(), "bildAlt": "Die Noten von c' bis e'' im Violinschlüssel mit ihren Namen",
   "text": "- **Auf den Linien** (von unten nach oben, schwarz im Bild): e' – g' – h' – d'' – f''\n- **In den Zwischenräumen** (von unten nach oben, orange im Bild): f' – a' – c'' – e'' (zusammen ergibt das das Wort „face“)\n- **Das Hochkomma gehört zum Namen.** c' (eingestrichen) und c'' (zweigestrichen) sind zwei verschiedene Töne. Ein h ohne Hochkomma wäre ein anderer, tieferer Ton als h'. Schreibe das Hochkomma deshalb immer mit.\n- Das Hochkomma tippst du auf der deutschen Tastatur mit ⇧ + #.",
   "merke": "Linien und Zwischenräume zählt man immer von unten. Die unterste Linie ist e'."},
  {"titel": "Notenwerte und Schläge",
   "bild": img_notenwerte(), "bildAlt": MERKBILD_ALT,
   "text": "- **Zuerst auf den Kopf schauen:** hohl heißt halbe oder ganze Note, ausgefüllt heißt Viertel oder Achtel. Danach zählen Hals und Fähnchen.\n- Ganze Note: hohler Kopf, kein Hals. Halbe Note: hohler Kopf mit Hals. Viertelnote: ausgefüllter Kopf mit Hals. Achtelnote: ausgefüllter Kopf mit Hals und Fähnchen.\n- Ob der Hals nach oben oder nach unten zeigt, ändert weder den Namen noch den Wert der Note.\n- **Schläge:** ganze Note 4, halbe Note 2, Viertelnote 1, Achtelnote ½. Jede Stufe ist halb so lang wie die vorige.",
   "merke": "Erst der Kopf, dann Hals und Fähnchen."},
  {"titel": "Das Kreuz",
   "bild": img_kreuz_merk(), "bildAlt": "Die Noten f' und fis' sowie c'' und cis'' (mit Kreuz) im Vergleich",
   "text": "- Das Kreuz (♯) steht **vor** der Note und erhöht den Ton um einen **Halbton**.\n- Der Name bekommt die Endung „-is“: f' wird zu fis', c'' wird zu cis'', a' wird zu ais'. Das Hochkomma bleibt dran.\n- Zusatz (nur, wenn ihr das im Unterricht schon hattet): Neben dem Kreuz gibt es das b (♭). Es senkt den Ton um einen Halbton. Aus h' wird b', aus g' wird ges'.",
   "merke": "Kreuz = höher = Endung „-is“."},
  {"titel": "Zum Aufschreiben auf Papier (ohne Drucker)",
   "bild": img_loesung_papier(), "bildAlt": "Lösung der Zeichenaufgaben: vier Viertelnoten g', c'', e', a' und die Melodie g', ais', h', c''",
   "text": "Zeichnen übt man am besten mit dem Stift. Ein leeres Blatt reicht: fünf Linien selbst ziehen, Violinschlüssel davor.\n\n- **Noten setzen:** Zeichne vier Viertelnoten auf g', c'', e' und a' (ausgefüllter Kopf mit Hals, der Hals darf nach oben oder unten zeigen).\n- **Melodie schreiben:** Schreibe in einen 4/4-Takt vier Viertelnoten nacheinander: g' – ais' – h' – c''. Das Kreuz steht **vor** dem a' und auf derselben Höhe.\n\nDas Bild zeigt, wie es richtig aussieht. Am besten vergleicht ihr gemeinsam."}
 ],
 "aufgaben": [
  # ---------------- Teil 1: Notennamen ----------------
  {"typ": "luecke", "abschnitt": "Teil 1 – Notennamen",
   "frage": "Noten lesen: Schreibe unter jede Note ihren Namen. Achte auf das Hochkomma.",
   "bild": img_lesen(), "bildAlt": "Fünf Noten im Violinschlüssel, a) bis e)",
   "text": "a) {{f'}}   b) {{h'}}   c) {{c'}}   d) {{d''}}   e) {{a'}}",
   "tipp": "Zähle die Linien und Zwischenräume von unten. Die unterste Linie ist e'.",
   "info": "a) f': 1. Zwischenraum. b) h': mittlere Linie. c) c': Hilfslinie unter dem System. d) d'': 4. Linie. e) a': 2. Zwischenraum. Ohne Hochkomma ist der Name unvollständig."},
  {"typ": "zuordnen", "abschnitt": "Teil 1 – Notennamen",
   "frage": "Noten finden: Welche Note im Bild ist welcher Ton? Ordne zu.",
   "bild": img_setzen(), "bildAlt": "Fünf Noten A bis E im Violinschlüssel",
   "paare": [["g'", "Note D"], ["c''", "Note A"], ["e'", "Note B"], ["a'", "Note C"]], "extra": ["Note E"],
   "tipp": "e' ist die unterste Linie, g' die zweite. Von dort aus kannst du hochzählen.",
   "info": "Von unten: e' 1. Linie, g' 2. Linie, a' 2. Zwischenraum, c'' 3. Zwischenraum. Note E ist ein d'' (4. Linie) und gehört zu keinem dieser Töne."},
  {"typ": "luecke", "abschnitt": "Teil 1 – Notennamen",
   "frage": "Kleine Melodie: Wie heißt die **höchste** Note, und welchen Notenwert hat sie?",
   "bild": img_melodie(), "bildAlt": "Kleine Melodie im 4/4-Takt mit drei Takten, die Noten sind von 1 bis 11 nummeriert",
   "text": "Name: {{d''}}   Notenwert: {{" + HALBE_NOTE + "}}",
   "tipp": "Benenne zuerst alle Noten und suche dann die höchste. Den Notenwert siehst du am Kopf.",
   "info": "Die höchste Note ist das d'' in Takt 3 (Note 9, 4. Linie). Sie hat einen hohlen Kopf mit Hals: halbe Note."},
  {"typ": "luecke", "abschnitt": "Teil 1 – Notennamen",
   "frage": "Kleine Melodie: Wie heißt die **tiefste** Note, und welchen Notenwert hat sie?",
   "bild": img_melodie(), "bildAlt": "Kleine Melodie im 4/4-Takt mit drei Takten, die Noten sind von 1 bis 11 nummeriert",
   "text": "Name: {{d'}}   Notenwert: {{" + VIERTELNOTE + "}}",
   "tipp": "Die tiefste Note hängt unter der untersten Linie.",
   "info": "Die tiefste Note ist das d' am Ende von Takt 2 (Note 8): Sie steht direkt unter der untersten Linie und hat einen ausgefüllten Kopf mit Hals: Viertelnote."},
  {"typ": "mc", "abschnitt": "Teil 1 – Notennamen", "mischen": False,
   "frage": "Kleine Melodie: Welche Noten sind **halbe Noten**? Kreuze alle an (die Nummern stehen unter den Noten).",
   "bild": img_melodie(), "bildAlt": "Kleine Melodie im 4/4-Takt mit drei Takten, die Noten sind von 1 bis 11 nummeriert",
   "antworten": ["Note 2", "Note 3", "Note 5", "Note 8", "Note 9", "Note 11"], "richtig": [1, 4],
   "info": "Halbe Noten haben einen hohlen Kopf: Note 3 (h' in Takt 1) und Note 9 (d'' in Takt 3). Zur Kontrolle: Jeder Takt hat 4 Schläge. Takt 1: 1 + 1 + 2. Takt 2: 1 + ½ + ½ + 1 + 1. Takt 3: 2 + 1 + 1."},
  # ---------------- Teil 2: Notenwerte und Vorzeichen ----------------
  {"typ": "reihenfolge", "abschnitt": "Teil 2 – Notenwerte und Vorzeichen",
   "frage": "Bringe die Notenwerte in die Reihenfolge von der **längsten** zur **kürzesten** Note.",
   "schritte": ["Ganze Note (4 Schläge)", "Halbe Note (2 Schläge)", "Viertelnote (1 Schlag)", "Achtelnote (½ Schlag)"],
   "info": "Jede Stufe ist halb so lang wie die vorige: 4 – 2 – 1 – ½."},
  {"typ": "luecke", "abschnitt": "Teil 2 – Notenwerte und Vorzeichen",
   "frage": "Notenwert bestimmen: Schreibe zu jeder Note den Namen, den Notenwert (zum Beispiel „Viertelnote“) und die Anzahl der Schläge.",
   "bild": img_werte(), "bildAlt": "Fünf Noten mit unterschiedlichen Notenwerten, a) bis e)",
   "text": ("a) Name {{c''}}  Notenwert {{" + VIERTELNOTE + "}}  Schläge {{1}}\n"
            "b) Name {{f'}}  Notenwert {{" + HALBE_NOTE + "}}  Schläge {{2}}\n"
            "c) Name {{g'}}  Notenwert {{" + ACHTELNOTE + "}}  Schläge {{" + HALB + "}}\n"
            "d) Name {{e''}}  Notenwert {{" + GANZE_NOTE + "}}  Schläge {{4}}\n"
            "e) Name {{h'}}  Notenwert {{" + HALBE_NOTE + "}}  Schläge {{2}}"),
   "tipp": "Erst der Kopf (hohl oder ausgefüllt), dann Hals und Fähnchen. Die Schläge: 4 – 2 – 1 – ½.",
   "info": "a) c'': ausgefüllter Kopf, Hals, kein Fähnchen. b) f': hohler Kopf mit Hals. c) g': ausgefüllter Kopf, Hals und Fähnchen. d) e'': hohler Kopf ohne Hals. e) h': hohler Kopf mit Hals, der Hals zeigt hier nach unten."},
  {"typ": "tf", "abschnitt": "Teil 2 – Notenwerte und Vorzeichen",
   "frage": "Stimmt das? „Eine Note mit Hals ist immer eine Viertelnote.“",
   "richtig": False,
   "info": "Einen Hals haben halbe Noten, Viertelnoten und Achtelnoten. Der Hals allein sagt also nichts. Man erkennt den Notenwert zuerst am Kopf."},
  {"typ": "mc", "abschnitt": "Teil 2 – Notenwerte und Vorzeichen", "mischen": False,
   "frage": "Das Kreuz: Steht es vor oder hinter der Note?",
   "bild": img_kreuz(), "bildAlt": "Zwei Noten mit Kreuz im Violinschlüssel, a) und b)",
   "antworten": ["vor der Note", "hinter der Note"], "richtig": 0},
  {"typ": "mc", "abschnitt": "Teil 2 – Notenwerte und Vorzeichen",
   "frage": "Was bewirkt das Kreuz bei einer Note?",
   "antworten": ["Es erhöht den Ton um einen Halbton.", "Es senkt den Ton um einen Halbton.", "Es macht die Note doppelt so lang.", "Es macht den Ton lauter."],
   "richtig": 0},
  {"typ": "luecke", "abschnitt": "Teil 2 – Notenwerte und Vorzeichen",
   "frage": "Wie heißen die Töne mit Kreuz? Schreibe die Namen mit Hochkomma.",
   "bild": img_kreuz(), "bildAlt": "Zwei Noten mit Kreuz im Violinschlüssel, a) und b)",
   "text": "Note a): {{fis'}}   Note b): {{cis''}}",
   "tipp": "Erst den Namen ohne Kreuz bestimmen, dann „-is“ anhängen.",
   "info": "Note a) ist ein f' mit Kreuz, also fis'. Note b) ist ein c'' mit Kreuz, also cis''. Der Name bleibt gleich und bekommt die Endung „-is“. Das Hochkomma bleibt dran."},
  {"typ": "kurz", "abschnitt": "Teil 2 – Notenwerte und Vorzeichen",
   "frage": "Fehler finden: Ben sagt zu dieser Note: „Das ist ein h und eine Viertelnote, weil sie einen Hals hat.“ Wie heißt die Note richtig (mit Hochkomma)?",
   "bild": img_ben(), "bildAlt": "Eine Note auf der mittleren Linie, hohler Kopf mit Hals",
   "richtig": ["h'"],
   "info": "Die Note steht auf der mittleren Linie, im Violinschlüssel ist das h'. Das Hochkomma fehlt in Bens Antwort."},
  {"typ": "kurz", "abschnitt": "Teil 2 – Notenwerte und Vorzeichen",
   "frage": "Ben hat auch den Notenwert falsch genannt. Welcher Notenwert ist richtig?",
   "bild": img_ben(), "bildAlt": "Eine Note auf der mittleren Linie, hohler Kopf mit Hals",
   "richtig": ["halbe Note", "halbe", "halbe-Note", "halbenote"],
   "info": "Der Kopf ist hohl und die Note hat einen Hals: halbe Note (2 Schläge)."},
  {"typ": "mc", "abschnitt": "Teil 2 – Notenwerte und Vorzeichen",
   "frage": "Woran erkennt man den Notenwert **zuerst**?",
   "antworten": ["Am Kopf: Ist er hohl oder ausgefüllt?", "Am Hals: Hat die Note einen Hals?", "An der Farbe der Note", "An der Zeile, in der sie steht"],
   "richtig": 0,
   "info": "Der Kopf entscheidet: Hohl heißt halbe oder ganze Note, ausgefüllt heißt Viertel oder Achtel. Hals und Fähnchen kommen danach."},
  {"typ": "mc", "abschnitt": "Teil 2 – Notenwerte und Vorzeichen", "mischen": False, "punkte": 2,
   "frage": "Melodie schreiben: Welche Zeile zeigt vier Viertelnoten nacheinander g' – ais' – h' – c'' mit dem Kreuz **vor** dem ais'?",
   "bild": img_melodie_zeilen(), "bildAlt": "Vier Zeilen A bis D mit je vier Viertelnoten im 4/4-Takt",
   "antworten": ["Zeile A", "Zeile B", "Zeile C", "Zeile D"], "richtig": 2,
   "tipp": "ais' ist ein a' mit Kreuz. Das Kreuz muss links vor dem Notenkopf stehen, auf derselben Höhe.",
   "info": "Zeile A hat gar kein Kreuz. In Zeile B steht das Kreuz hinter der Note. In Zeile D steht das Kreuz bei g' statt bei a'. Nur Zeile C stimmt: g' – ais' – h' – c''. Kontrolle: 4 Viertelnoten ergeben 4 Schläge, der Takt ist voll."}
 ]
}

# =====================================================================
# Paket 2: Pausen und Taktarten
# =====================================================================
p2 = {
 "typ": "lernpaket", "version": 1,
 "id": "musik-6-pausen-taktarten",
 "titel": "Musik Klasse 6: Pausen und Taktarten",
 "fach": "Musik", "klasse": "6",
 "beschreibung": "Pausen erkennen, fehlende Pausen im Takt berechnen, Taktarten bestimmen. Die Zeichenaufgaben vom Papier sind hier als Auswahlaufgaben gebaut.",
 "hinweis": "Hier zählt jede Lücke einzeln, deshalb gibt es mehr Punkte als auf dem Papier. Was im Unterricht notiert wurde, hat Vorrang, besonders bei Schreibweise und Namen der Pausen. Zeichnen bleibt Papierarbeit (siehe Lernblatt).",
 "lernblatt": [
  {"titel": "Notenwerte und Pausen",
   "bild": img_notenwerte(mit_pausen=True), "bildAlt": "Noten und Pausen mit ihren Schlägen: ganze 4, halbe 2, Viertel 1, Achtel ½",
   "text": "- Jede Stufe ist halb so lang wie die vorige: 4 – 2 – 1 – ½ Schläge.\n- Eine Pause zählt genauso viele Schläge wie die Note mit demselben Namen.\n- Die Linien einer Notenzeile werden von unten gezählt. Die **halbe Pause** sitzt wie ein Hut **auf** der mittleren (3.) Linie, die **ganze Pause** hängt **unter** der 4. Linie.\n- Vor jeder Aufgabe das Schlüsselwort unterstreichen, zum Beispiel „Takt 4“, „zweite Notenzeile“ oder „Viertelschläge“.",
   "merke": "Halbe Pause = Hut auf der Linie. Ganze Pause = hängt darunter."},
  {"titel": "Taktarten",
   "text": "- Die **obere Zahl** sagt, wie viele Schläge in einen Takt passen. Die **untere Zahl** ist hier 4, weil ein Schlag eine Viertelnote ist. Eine Taktart ist kein Bruch.\n- So bestimmst du die Taktart: Jede Note und jede Pause in Schläge umrechnen (Achtel = ½), alles addieren. Die Summe ist die obere Zahl. **Pausen zählen mit.**\n- Beispiel: Viertelnote + halbe Note + Viertelnote = 1 + 2 + 1 = 4 Schläge. Das ist ein 4/4-Takt, obwohl nur drei Zeichen dastehen.\n- Eine fehlende Pause findest du so: Schläge der Noten addieren, von der Taktsumme abziehen, zum Rest die Pause mit gleicher Schlagzahl suchen.",
   "merke": "Nicht die Zeichen zählen, sondern die Schläge."},
  {"titel": "Pausen zeichnen (auf Papier)",
   "text": "Das Zeichnen übt man am besten mit dem Stift auf einem leeren Blatt mit fünf selbst gezogenen Linien.\n\n- **Ganze und halbe Pause** sind kleine Rechtecke: Die ganze hängt unter der 4. Linie, die halbe sitzt auf der 3. Linie.\n- **Viertelpause** in drei Zügen: oben ein schräger Strich, dann zwei kleine Zacken, unten ein Haken wie ein kleines „c“.\n- **Achtelpause:** ein Punkt oben mit einem schrägen Strich nach unten.\n- Übungstipp: Jede Pause fünfmal auf die Linien zeichnen und dabei den Namen und die Schläge laut sagen."}
 ],
 "aufgaben": [
  # ---------------- Teil 1: Pausen ----------------
  {"typ": "reihenfolge", "abschnitt": "Teil 1 – Pausen",
   "frage": "Bringe die Pausen in die Reihenfolge von der **längsten** zur **kürzesten** Pause.",
   "schritte": ["Ganze Pause (4 Schläge)", "Halbe Pause (2 Schläge)", "Viertelpause (1 Schlag)", "Achtelpause (½ Schlag)"],
   "info": "Eine Pause zählt so viele Schläge wie die Note mit demselben Namen: 4 – 2 – 1 – ½."},
  {"typ": "luecke", "abschnitt": "Teil 1 – Pausen",
   "frage": "Wie heißen diese Pausen, und wie viele Schläge dauern sie?",
   "bild": img_pausen_lesen(), "bildAlt": "Vier Pausen in gemischter Reihenfolge, a) bis d)",
   "text": ("a) Name {{" + HALBE_PAUSE + "}}  Schläge {{2}}\n"
            "b) Name {{" + ACHTELPAUSE + "}}  Schläge {{" + HALB + "}}\n"
            "c) Name {{" + GANZE_PAUSE + "}}  Schläge {{4}}\n"
            "d) Name {{" + VIERTELPAUSE + "}}  Schläge {{1}}"),
   "tipp": "Erst die Form: Zickzack = Viertelpause, Punkt mit Strich = Achtelpause, flacher Balken = ganze oder halbe Pause. Beim Balken entscheidet die Lage.",
   "info": "a) halbe Pause (sitzt auf der Linie), b) Achtelpause, c) ganze Pause (hängt unter der Linie), d) Viertelpause. Ganze und halbe Pause sehen fast gleich aus und unterscheiden sich nur in der Lage."},
  {"typ": "mc", "abschnitt": "Teil 1 – Pausen", "mischen": False,
   "frage": "Pausen erkennen: Welche Zeile zeigt eine **halbe Pause** an der richtigen Stelle?",
   "bild": img_pausen_lage(), "bildAlt": "Vier Zeilen A bis D mit je einer ganzen oder halben Pause an unterschiedlicher Stelle",
   "antworten": ["Zeile A", "Zeile B", "Zeile C", "Zeile D"], "richtig": 1,
   "tipp": "Die halbe Pause sitzt wie ein Hut auf der mittleren Linie.",
   "info": "Zeile B: Das Rechteck sitzt auf der mittleren (3.) Linie, das ist die halbe Pause. Zeile A zeigt die ganze Pause (hängt unter der 4. Linie). In Zeile C und D sitzt das Zeichen an der falschen Stelle."},
  {"typ": "mc", "abschnitt": "Teil 1 – Pausen", "mischen": False,
   "frage": "Pausen erkennen: Welche Zeile zeigt eine **ganze Pause** an der richtigen Stelle?",
   "bild": img_pausen_lage(), "bildAlt": "Vier Zeilen A bis D mit je einer ganzen oder halben Pause an unterschiedlicher Stelle",
   "antworten": ["Zeile A", "Zeile B", "Zeile C", "Zeile D"], "richtig": 0,
   "tipp": "Die ganze Pause hängt unter der 4. Linie (von unten gezählt).",
   "info": "Zeile A: Das Rechteck hängt unter der 4. Linie, das ist die ganze Pause. In Zeile D hängt es unter der mittleren Linie, das ist nicht die richtige Stelle."},
  {"typ": "luecke", "abschnitt": "Teil 1 – Pausen",
   "frage": "In jedem Takt fehlt eine Pause. Jeder Takt ist ein 4/4-Takt. Rechne, wie viele Schläge fehlen, und schreibe den Namen der Pause auf.",
   "bild": img_takt_luecke(), "bildAlt": "Drei 4/4-Takte, in denen jeweils eine Pause fehlt, a) bis c)",
   "text": ("a) Es fehlen {{1}} Schläge → {{" + VIERTELPAUSE + "}}\n"
            "b) Es fehlen {{2}} Schläge → {{" + HALBE_PAUSE + "}}\n"
            "c) Es fehlen {{" + HALB + "}} Schläge → {{" + ACHTELPAUSE + "}}"),
   "tipp": "Zähle die Schläge der Noten zusammen und ziehe sie von 4 ab. Eine Achtel zählt nur ½.",
   "info": "a) 1 + 1 + 1 = 3, es fehlt 1 Schlag: Viertelpause. b) 1 + 1 = 2, es fehlen 2 Schläge: halbe Pause. c) ½ + 1 + 2 = 3½, es fehlt ½ Schlag: Achtelpause. Typische Falle in c): die Achtel als vollen Schlag zählen. Dann kommt 4 heraus und es scheint nichts zu fehlen."},
  # ---------------- Teil 2: Taktarten ----------------
  {"typ": "luecke", "abschnitt": "Teil 2 – Taktarten",
   "frage": "Welche Taktart passt? Zähle die Schläge (Pausen zählen mit, eine Achtel zählt ½) und trage die Summe und die Taktart ein.",
   "bild": img_taktart(), "bildAlt": "Drei Takte mit leerem Kästchen für die Taktart, a) bis c)",
   "text": ("a) {{3}} Schläge → Taktart {{3/4|3 / 4}}\n"
            "b) {{2}} Schläge → Taktart {{2/4|2 / 4}}\n"
            "c) {{4}} Schläge → Taktart {{4/4|4 / 4}}"),
   "tipp": "Schreibe unter jedes Zeichen die Schläge und addiere. Die Summe ist die obere Zahl, darunter steht die 4.",
   "info": "a) ½ + ½ + 1 + 1 = 3 Schläge → 3/4. b) 1 + 1 = 2 Schläge → 2/4. c) 1 + 1 + 2 = 4 Schläge → 4/4. Typische Falle: Zeichen zählen statt Schläge. In a) stehen vier Zeichen, aber nur 3 Schläge. In c) drei Zeichen, aber 4 Schläge. Und die Pause zählt mit."},
  {"typ": "frei", "abschnitt": "Teil 2 – Taktarten", "punkte": 2,
   "frage": "Lisa sagt zu diesem Takt: „Ich sehe drei Zeichen, also ist es ein 3/4-Takt.“ Hat Lisa recht? Begründe mit einer Rechnung.",
   "bild": img_lisa(), "bildAlt": "Ein Takt mit Viertelnote, halber Note und Viertelnote, als 3/4 bezeichnet",
   "muster": "Nein, Lisa hat nicht recht, weil man nicht die Zeichen zählt, sondern die Schläge. Die Viertelnote zählt 1, die halbe Note 2, die zweite Viertelnote wieder 1. Das sind 4 Schläge, also ein 4/4-Takt.",
   "kriterien": ["Urteil: Lisa hat nicht recht, es ist ein 4/4-Takt", "Begründung mit „weil“: Schläge zählen, nicht Zeichen", "Rechnung: 1 + 2 + 1 = 4"],
   "info": "Nur „Nein, es ist ein 4/4-Takt“ zu schreiben ist eine Behauptung ohne Beleg und gibt nur den ersten Punkt."},
  {"typ": "mc", "abschnitt": "Teil 2 – Taktarten", "mischen": False,
   "frage": "Eigener Takt: Welche Takte sind richtige 4/4-Takte mit **einer halben Note, einer Viertelpause und einer Viertelnote**? Die Reihenfolge ist egal. Kreuze alle an.",
   "bild": img_takte_wahl(), "bildAlt": "Vier 4/4-Takte A bis D mit unterschiedlichen Noten und Pausen",
   "antworten": ["Takt A", "Takt B", "Takt C", "Takt D"], "richtig": [0, 2],
   "tipp": "Rechne in jedem Takt die Schläge zusammen. Es müssen genau 4 sein und alle drei Zeichen vorkommen.",
   "info": "Takt A: 2 + 1 + 1 = 4 und Takt C: 1 + 2 + 1 = 4 stimmen. In Takt B steht eine Achtelnote statt der Viertelnote (2 + 1 + ½ = 3½). In Takt D fehlt die halbe Note (1 + 1 + 1 = 3)."},
  {"typ": "luecke", "abschnitt": "Teil 2 – Taktarten",
   "frage": "Rechne zur Kontrolle: Ein 4/4-Takt mit halber Note, Viertelpause und Viertelnote.",
   "text": "halbe Note {{2}} + Viertelpause {{1}} + Viertelnote {{1}} = {{4}} Schläge",
   "info": "Zum Üben auf Papier: Schreibe selbst einen 4/4-Takt mit diesen drei Zeichen. Die halbe Note hat einen hohlen Kopf mit Hals, die Viertelpause ist ein Zickzack in der Mitte der Notenzeile."}
 ]
}

# =====================================================================
# Paket 3: Probearbeit im Format der Musikarbeit (38 Punkte)
# =====================================================================
WANDER = img_wanderlied()
WANDER_ALT = "Das Wanderlied in zwei Notenzeilen mit acht Takten. Am Anfang fehlt die Taktart, in Takt 6 fehlt eine Pause."
TEIL_A = "Teil A – Ein Lied unter der Lupe (21 Punkte)"
TEIL_B = "Teil B – Das Chanson (6 Punkte)"
TEIL_C = "Teil C – Bilder einer Ausstellung (4 Punkte)"
TEIL_D = "Teil D – Höraufgabe (7 Punkte)"

p3 = {
 "typ": "lernpaket", "version": 1,
 "id": "musik-6-probearbeit-wanderlied-hoeren",
 "titel": "Musik Klasse 6: Probearbeit (Lied, Chanson, Ausstellung, Hören)",
 "fach": "Musik", "klasse": "6",
 "beschreibung": "Übungsarbeit mit 38 Punkten in vier Teilen: A Lied, B Chanson, C Bilder einer Ausstellung, D Höraufgabe. Gut für die Probearbeit-Funktion (35–40 Minuten).",
 "hinweis": "Teil D braucht zwei Musikausschnitte, die auf einem anderen Gerät laufen (z. B. YouTube oder Spotify). Die Beschreibungen der Stücke beruhen auf allgemein bekannten Merkmalen und wurden nicht angehört, bitte beim Zuhören prüfen. Was im Unterricht notiert wurde (Merkmale des Chansons, Titel der Stücke, Notenbereiche), hat Vorrang.",
 "lernblatt": [
  {"titel": "Was die Arbeitsaufträge verlangen",
   "text": "- **Nenne:** kurz aufzählen, ganze Sätze sind nicht nötig. Beispiel: „Viertelnote, halbe Note“.\n- **Kreuze an:** nur markieren. Bei „alle richtigen“ können mehrere stimmen.\n- **Beschreibe:** sagen, wie etwas klingt oder aussieht, mit Fachwörtern. Beispiel: „Die Musik ist langsam, tief und feierlich.“\n- **Erkläre:** einen Zusammenhang mit „weil“ oder „deshalb“ darlegen. Beispiel: „…, weil alle Notenwerte zusammen vier Viertel ergeben.“\n- **Begründe:** Aussage plus Beleg aus der Musik oder dem Notentext. Beispiel: „Die Musik wirkt ruhig, weil sie langsam ist.“\n\nBei 2 Punkten erwartet die Lehrkraft meistens zwei Gedanken oder zwei Teilantworten, bei 1 Punkt einen."},
  {"titel": "Notenwerte, Pausen und Taktart",
   "bild": img_notenwerte(mit_pausen=True), "bildAlt": "Noten und Pausen mit ihren Schlägen: ganze 4, halbe 2, Viertel 1, Achtel ½",
   "text": "- Jede Stufe ist halb so lang wie die vorige: 4 – 2 – 1 – ½ Schläge. Eine Pause zählt so viel wie die Note mit demselben Namen.\n- Die halbe Pause sitzt wie ein Hut **auf** der mittleren Linie, die ganze Pause hängt **unter** der 4. Linie.\n- Bei 4/4 hat jeder Takt vier Viertelschläge. Man zählt Schläge, nicht Zeichen, und Pausen zählen mit.\n- Ein Vorzeichen ändert den Ton, ist aber selbst keine Note. Das Kreuz steht links vor der Note und erhöht sie um einen Halbton: aus g wird gis."},
  {"titel": "Notennamen",
   "bild": img_notennamen(), "bildAlt": "Die Noten von c' bis e'' im Violinschlüssel mit ihren Namen",
   "text": "- Linien von unten: e' – g' – h' – d'' – f''. Dafür hilft ein Merksatz, zum Beispiel „Eine Gute Hexe Denkt Fröhlich“. Denk dir am besten einen eigenen aus oder nimm den aus dem Unterricht.\n- Zwischenräume von unten: f' – a' – c'' – e'' (wie das Wort „face“).\n- Das Hochkomma gehört zum Namen.",
   "merke": "Immer von unten zählen. Der Schlüssel windet sich um die zweite Linie, das ist das g'."},
  {"titel": "Das Chanson",
   "text": "- Das Chanson kommt ursprünglich aus Frankreich und wird meist auf Französisch gesungen.\n- Der Text ist besonders wichtig und soll verstanden werden. Es geht oft um Liebe, Alltag oder Gesellschaft.\n- Meist singt eine einzelne Person, begleitet von wenigen Instrumenten (zum Beispiel Klavier, Akkordeon oder Gitarre).\n- Text und Musik gehören eng zusammen.\n\nFreiwillige Hörtipps zum Vergleichen: Edith Piaf – „La vie en rose“, Charles Aznavour – „La Bohème“, Joe Dassin – „Les Champs-Élysées“. Achte darauf, wie die Stimme im Vordergrund steht und der Text die Hauptrolle spielt.",
   "merke": "Wörter wie „immer“ und „nur“ machen eine Aussage oft falsch. Prüfe sie trotzdem einzeln."},
  {"titel": "Bilder einer Ausstellung",
   "text": "- Komponist: **Modest Mussorgsky**, ein russischer Komponist.\n- Anlass: Er sah eine Ausstellung mit Bildern seines Freundes, des Malers Viktor Hartmann, der kurz zuvor gestorben war.\n- Fast jedes Stück gehört zu einem Bild und zeigt mit Musik, was auf dem Bild zu sehen ist (Tonmalerei).\n- Zwischen den Stücken kommt immer wieder die „Promenade“. Sie zeigt, wie der Besucher von einem Bild zum nächsten geht.\n\n**Vier Stücke und wie sie klingen:**\n- Gnomus (ein kleiner Wicht): ruckartig, mit Sprüngen und Pausen, ein bisschen unheimlich.\n- Ballett der Küchlein in ihren Eierschalen: hohe, schnelle, leichte Töne, die an Piepsen und Hüpfen erinnern.\n- Bydło (ein schwerer Ochsenkarren): schwer, tief und stampfend, wie ein langsamer Karren.\n- Das große Tor von Kiew: feierlich und groß, mit vollem Klang und Glockenschlägen.\n\nDiese Beschreibungen beruhen auf allgemein bekannten Merkmalen und wurden nicht angehört. Die Titel können im Unterricht leicht anders lauten, zum Beispiel „Der Ochsenkarren“ statt „Bydło“."},
  {"titel": "Die Hörkarte",
   "text": "So hört man systematisch hin. Bei jeder Höraufgabe gehst du diese Zeilen durch und kommst am Ende bei der Wirkung an.\n\n- **Tempo:** schnell oder langsam, gleichmäßig oder wechselnd? (schnell, langsam, wird schneller)\n- **Tonlage:** hoch oder tief, hell oder dunkel?\n- **Lautstärke:** leise oder laut, wird es lauter oder leiser?\n- **Instrumente:** Streicher, Holz, Blech, Klavier, Stimme? (Flöte, Trompete, Tuba)\n- **Rhythmus:** gleichmäßig, stampfend, hüpfend, ruckartig?\n- **Wirkung:** Was macht die Musik mit mir? (ruhig, bewegt, feierlich, leicht, schwer, fröhlich, unheimlich)\n\n**Zweimal hören:** Beim ersten Hören konzentrierst du dich auf den Gesamteindruck. Beim zweiten Hören bearbeitest du die Aufgaben.\n\n**Zum Vergleichen (ohne Punkte):** Höre nach dem Ballett der Küchlein auch „Bydło“ und fülle die Hörkarte aus. Erwartet wird ungefähr: langsam, tief, ruhig und schwer, gleichmäßig, stampfend. Zwischendurch wird es laut, bleibt aber gleichmäßig und schwer.",
   "merke": "Jede Zeile einzeln hören. Schnelle Musik ist nicht automatisch hoch, langsame nicht automatisch ruhig."},
  {"titel": "Begründen mit „weil“",
   "text": "Ein Dreischritt für „Erkläre“ und „Begründe“:\n\n- 1. Die Aussage nennen.\n- 2. „weil“ sagen.\n- 3. Einen Beleg anfügen: bei Musik etwas, das man hört (Tempo, Tonlage, Instrument, Lautstärke, Rhythmus), bei Noten etwas, das man rechnen kann.\n\nBeispiel: „Die Musik wirkt feierlich, weil sie langsam und tief ist.“ Ein schönes Bild im Kopf (zum Beispiel „ein König auf einem Thron“) darf als Ergänzung dabeistehen, ersetzt aber den Beleg nicht."}
 ],
 "aufgaben": [
  # ---------------- Teil A ----------------
  {"typ": "luecke", "abschnitt": TEIL_A,
   "frage": "**A1 (2 P)** Trage die passende Taktart in die gestrichelte Lücke am Anfang ein.",
   "bild": WANDER, "bildAlt": WANDER_ALT,
   "text": "Die Taktart ist {{4}} / {{4}}",
   "tipp": "Nimm einen Takt mit nur Viertelnoten (Takt 1 oder 3) und zähle die Schläge.",
   "info": "4/4 (Viervierteltakt). Die obere 4 heißt: vier Schläge pro Takt. Die untere 4 heißt: Ein Schlag ist eine Viertelnote. Gegenprobe an Takt 2: halbe Note (2) + zwei Viertel (1 + 1) = 4. Typische Falle: Pausen vergessen. Takt 4 hat nur 1 + 1 Schlag, bis zur 4 fehlen die 2 Schläge der halben Pause."},
  {"typ": "kurz", "abschnitt": TEIL_A,
   "frage": "**A2 (1 P)** Wie heißt das Zeichen ganz am Anfang jeder Notenzeile?",
   "bild": WANDER, "bildAlt": WANDER_ALT,
   "richtig": ["Violinschlüssel", "Notenschlüssel", "G-Schlüssel", "Violin-Schlüssel", "Violinschluessel", "G Schlüssel"],
   "info": "Violinschlüssel (auch Notenschlüssel oder G-Schlüssel). Er legt fest, welche Linie welchen Ton bedeutet. Er windet sich um die zweite Linie von unten, das ist das g'. Daher kommt der Name G-Schlüssel."},
  {"typ": "kurz", "abschnitt": TEIL_A,
   "frage": "**A3 (1 P)** Wie viele Achtelnoten findest du im Lied? (Achtelpausen zählen nicht.)",
   "bild": WANDER, "bildAlt": WANDER_ALT,
   "richtig": ["3"],
   "tipp": "Geh Takt für Takt durch. Ein Balken verbindet zwei Achtelnoten, die einzeln zählen.",
   "info": "3 Achtelnoten: zwei in Takt 5 (durch einen Balken verbunden) und eine in Takt 7. Die Achtelpause am Anfang von Takt 7 ist keine Note."},
  {"typ": "mc", "abschnitt": TEIL_A,
   "frage": "**A4 (1 P)** Welche Note in der zweiten Notenzeile ist genauso lang wie vier Achtelnoten zusammen?",
   "bild": WANDER, "bildAlt": WANDER_ALT,
   "antworten": ["Die halbe Note in Takt 8", "Eine Viertelnote in Takt 6", "Eine Viertelnote in Takt 7", "Die beiden verbundenen Achtel in Takt 5"], "richtig": 0,
   "tipp": "Vier Achtel sind 4 × ½ Schlag. Wie viele Schläge sind das?",
   "info": "4 × ½ = 2 Schläge, das ist eine halbe Note. In der zweiten Zeile gibt es sie in Takt 6 und in Takt 8, eine genügt. Die halbe Note in Takt 2 gehört zur ersten Zeile."},
  {"typ": "luecke", "abschnitt": TEIL_A,
   "frage": "**A5 (2 P)** Wie heißen Name und Wert der **höchsten** Note im Lied?",
   "bild": WANDER, "bildAlt": WANDER_ALT,
   "text": "Notenname {{h'}}   Notenwert {{" + HALBE_NOTE + "}}",
   "tipp": "Achte nur auf die Köpfe, nicht auf die Hälse. Zähle von unten: e' erste Linie, f' erster Zwischenraum, g' zweite Linie, a' zweiter Zwischenraum, h' dritte Linie.",
   "info": "h' (halbe Note in Takt 6). Der Kopf liegt auf der mittleren Linie und ist hohl. Typische Falle: Im Deutschen heißt die Note auf der mittleren Linie h', nicht b'. Dass der Hals nach unten zeigt, sagt nichts über die Tonhöhe."},
  {"typ": "luecke", "abschnitt": TEIL_A,
   "frage": "**A6 (2 P)** Die Pause in Takt 4: Wie heißt sie, und wie viele Viertelschläge dauert sie?",
   "bild": WANDER, "bildAlt": WANDER_ALT,
   "text": "Name {{" + HALBE_PAUSE + "}}   Dauer {{2}} Viertelschläge",
   "tipp": "Der flache Balken sitzt auf der mittleren Linie. Rechenprobe: Takt 4 hat 1 + 1 Schlag, bis 4 fehlen ...",
   "info": "Halbe Pause, sie dauert 2 Viertelschläge. Die halbe Pause liegt wie ein Hut auf der mittleren Linie, die ganze Pause hängt unter der 4. Linie."},
  {"typ": "luecke", "abschnitt": TEIL_A,
   "frage": "**A7 (2 P)** In Takt 6 fehlt ein Pausenwert. Rechne nach: Wie viele Schläge fehlen, und welche Pause gehört in die Lücke?",
   "bild": WANDER, "bildAlt": WANDER_ALT,
   "text": "Es fehlt {{1}} Schlag. In die Lücke gehört eine {{" + VIERTELPAUSE + "}}.",
   "tipp": "Zähle die Schläge der Noten in Takt 6 zusammen und ziehe sie von 4 ab.",
   "info": "Takt 6 hat eine halbe Note (2) und eine Viertelnote (1) = 3 Schläge. Zu 4 fehlt 1 Schlag: Viertelpause. Auf Papier würde man ein Zickzack in die Mitte der Notenzeile zeichnen. Typische Falle: Viertelpause und Achtelpause verwechseln. Nur die Achtelpause hat oben einen Punkt (wie am Anfang von Takt 7)."},
  {"typ": "luecke", "abschnitt": TEIL_A,
   "frage": "**A8 (2 P)** In Takt 5 wird eine Note durch ein Vorzeichen erhöht. Wie heißt das Zeichen, und was wird aus dem g?",
   "bild": WANDER, "bildAlt": WANDER_ALT,
   "text": "Das Zeichen heißt {{Kreuz|♯}}. Aus g wird {{gis}}.",
   "tipp": "Das Zeichen steht links vor dem Notenkopf. Erhöht heißt: Name + „is“.",
   "info": "Das Kreuz steht links vor der Note und erhöht sie um einen Halbton. Aus g wird gis. Erniedrigt (mit b) wäre es ges."},
  {"typ": "mc", "abschnitt": TEIL_A, "mischen": False,
   "frage": "**A9 (1 P)** In welchem Takt steht die Notenfolge d' – f' – a'?",
   "bild": WANDER, "bildAlt": WANDER_ALT,
   "antworten": ["Takt 1", "Takt 3", "Takt 5", "Takt 7"], "richtig": 1,
   "tipp": "d' hängt direkt unter der untersten Linie, f' steht im ersten Zwischenraum, a' im zweiten.",
   "info": "Takt 3: Die Folge steht gleich am Anfang (d' f' a' f'). Die Zwischenräume von unten heißen f' – a' – c'' – e'' (wie „face“)."},
  {"typ": "luecke", "abschnitt": TEIL_A,
   "frage": "**A10 (2 P)** Rechne: Eine Viertelnote + eine Achtelnote + eine Achtelpause sind zusammen so lang wie eine …",
   "text": "1 + ½ + ½ = {{2}} Schläge. Das ist so lang wie eine {{" + HALBE_NOTE + "}}.",
   "tipp": "Rechne alle Werte in Schläge um. Stille hat auch eine Länge.",
   "info": "1 + ½ + ½ = 2 Schläge, also eine halbe Note. Ein aufgeschriebener Rechenweg bringt oft Teilpunkte. Typische Falle: die Pause weglassen. Dann käme 1½ heraus, und diese Länge gibt es als einfache Note nicht."},
  {"typ": "mc", "abschnitt": TEIL_A, "mischen": False, "punkte": 3,
   "frage": "**A11 (3 P)** In welchen Takten steht eine **halbe Note**? Kreuze alle an. (Eine halbe Pause ist keine Note.)",
   "bild": WANDER, "bildAlt": WANDER_ALT,
   "antworten": ["Takt 1", "Takt 2", "Takt 3", "Takt 4", "Takt 5", "Takt 6", "Takt 7", "Takt 8"], "richtig": [1, 5, 7],
   "tipp": "Eine halbe Note hat einen hohlen Kopf mit Hals. Geh beide Zeilen Takt für Takt durch.",
   "info": "Halbe Noten stehen in Takt 2 (g'), Takt 6 (h') und Takt 8 (c'). Typische Falle: die halbe Pause in Takt 4 mitzählen. Sie sieht ähnlich aus, ist aber keine Note."},
  {"typ": "frei", "abschnitt": TEIL_A, "punkte": 2,
   "frage": "**A12 (2 P)** Erkläre kurz: Warum passt in jeden Takt dieses Liedes genau dieselbe Anzahl an Viertelschlägen?",
   "bild": WANDER, "bildAlt": WANDER_ALT,
   "muster": "Weil das Lied im 4/4-Takt steht, hat jeder Takt vier Viertelschläge. Die Noten und Pausen eines Taktes ergeben zusammen immer vier Viertel, zum Beispiel in Takt 5: zwei Achtel (1) plus drei Viertel (3) sind 4.",
   "kriterien": ["Taktart nennen (4/4)", "Sagen, was sie bedeutet (vier Viertelschläge pro Takt)", "Ein Beispiel rechnen (zum Beispiel Takt 5: ½ + ½ + 1 + 1 + 1 = 4)"],
   "tipp": "Aufbau: 1. Taktart nennen, 2. sagen, was sie bedeutet, 3. ein Beispiel rechnen.",
   "info": "Nur „weil die Takte gleich lang sind“ zu schreiben sagt dasselbe noch einmal mit anderen Worten. Das Beispiel ist der Beweis, dass du den Zusammenhang verstanden hast."},
  # ---------------- Teil B ----------------
  {"typ": "mc", "abschnitt": TEIL_B, "mischen": False, "punkte": 4,
   "frage": "**B1 (4 P)** Kreuze alle richtigen Aussagen an.",
   "antworten": ["Das Chanson stammt ursprünglich aus Frankreich.",
                 "Im Chanson erzählt der Text oft von Liebe, Alltag oder Gesellschaft.",
                 "Ein Chanson wird immer von einem großen Chor gesungen.",
                 "Beim Chanson kommt es nur auf die Melodie an, der Text ist egal."],
   "richtig": [0, 1],
   "info": "Richtig sind die ersten beiden Aussagen. Aussage 3 passt nicht, weil meist eine einzelne Person singt. Aussage 4 passt nicht, weil Text und Musik zusammenwirken und der Text verstanden werden soll. Wörter wie „immer“ und „nur“ sind ein Warnsignal."},
  {"typ": "frei", "abschnitt": TEIL_B, "punkte": 2,
   "frage": "**B2 (2 P)** Nenne zwei Merkmale des Chansons in eigenen Worten.",
   "muster": "Der Text ist besonders wichtig und soll verstanden werden.\nMeist singt eine Person, begleitet von wenigen Instrumenten (zum Beispiel Klavier, Akkordeon, Gitarre).",
   "kriterien": ["Zwei verschiedene Merkmale („Text wichtig“ und „Text verstehen“ zählen meist nur einmal)", "Je Merkmal ein kurzer Satzteil mit Verb, nicht nur ein Stichwort", "Mögliche Merkmale: Text ist wichtig · kommt aus Frankreich, meist auf Französisch · meist eine Person mit wenigen Instrumenten · Text und Musik gehören eng zusammen, oft um Liebe, Alltag oder Gesellschaft"],
   "info": "Wichtig: Die Merkmale aus dem Unterricht haben Vorrang. Bitte mit Heft oder Arbeitsblatt abgleichen."},
  # ---------------- Teil C ----------------
  {"typ": "mc", "abschnitt": TEIL_C, "mischen": False,
   "frage": "**C1 (1 P)** Wer komponierte „Bilder einer Ausstellung“?",
   "antworten": ["Antonio Vivaldi", "Modest Mussorgsky", "Johannes Brahms"], "richtig": 1,
   "info": "Modest Mussorgsky, ein russischer Komponist."},
  {"typ": "frei", "abschnitt": TEIL_C, "punkte": 1,
   "frage": "**C2 (1 P)** Was inspirierte den Komponisten zu diesem Werk? Schreibe einen Satz.",
   "muster": "Mussorgsky sah eine Ausstellung mit Bildern seines Freundes, des Malers Viktor Hartmann, der kurz zuvor gestorben war.",
   "kriterien": ["Bilder (Ausstellung)", "Freund des Komponisten (der Name Hartmann ist ein Zusatz)"]},
  {"typ": "frei", "abschnitt": TEIL_C, "punkte": 2,
   "frage": "**C3 (2 P)** Erkläre kurz, wie Bilder und Musik bei „Bilder einer Ausstellung“ zusammenhängen. Schreibe zwei Gedanken auf.",
   "muster": "Fast jedes Stück gehört zu einem Bild und zeigt mit Musik, was auf dem Bild zu sehen ist (Tonmalerei).\nZwischen den Stücken kommt immer wieder die „Promenade“. Sie zeigt, wie der Besucher von einem Bild zum nächsten geht.",
   "kriterien": ["1. Gedanke: Die Musik zeigt, was auf dem Bild zu sehen ist (Tonmalerei), am besten mit einem kurzen Beispiel", "2. Gedanke: Die Promenade ist der Gang von Bild zu Bild"],
   "tipp": "Satzanfänge: „Der Komponist wollte … darstellen, deshalb …“ und „Zwischen den Bildern hört man …“.",
   "info": "Ein kurzes Beispiel macht aus einer Behauptung einen Beleg."},
  # ---------------- Teil D ----------------
  {"typ": "zuordnen", "abschnitt": TEIL_D,
   "frage": "**D1 (3 P)** Was hörst du bei Ausschnitt 1? Wähle bei jedem Merkmal die passende Möglichkeit.",
   "text": "**Vorbereitung:** Such dir auf YouTube oder Spotify einen Ausschnitt von etwa einer Minute: **Ausschnitt 1** ist „Ballett der Küchlein in ihren Eierschalen“ aus „Bilder einer Ausstellung“ (Mussorgsky, Orchesterfassung von Ravel). Höre ihn **zweimal**: beim ersten Mal nur zuhören, beim zweiten Mal die Aufgaben D1 bis D3 bearbeiten.",
   "paare": [["Tempo", "eher schnell"], ["Tonlage", "eher hoch"], ["Wirkung", "eher bewegt"]],
   "extra": ["eher langsam", "eher tief", "eher ruhig"],
   "tipp": "Jede Zeile einzeln hören. Tempo: Kann ich bequem mitklopfen? Tonlage: Klingt es hell und dünn wie Piepsen oder dunkel und breit wie eine Tuba? Wirkung: Möchte ich dazu hüpfen oder ruhig sitzen bleiben?",
   "info": "Erwartet wird: schnell, hoch, bewegt. Wenn du beim Hören etwas anderes wahrnimmst und es passend begründest, ist das in Ordnung. Schnelle Musik ist nicht automatisch hoch, und langsame Musik nicht automatisch ruhig."},
  {"typ": "frei", "abschnitt": TEIL_D, "punkte": 2,
   "frage": "**D2 (2 P)** Beschreibe die Wirkung der Musik (Ausschnitt 1) mit zwei passenden Wörtern. Die Musik wirkt … und …",
   "muster": "Die Musik wirkt leicht und verspielt.",
   "kriterien": ["Zwei Wirkungswörter, zum Beispiel leicht, verspielt, lebhaft, fröhlich, lustig, hüpfend", "Eine Wirkung beschreiben, nicht Zeit oder Ort („mittelalterlich“ ist eher eine Epoche als eine Wirkung)"],
   "tipp": "Frage dich, wozu die Musik passen würde: tanzen, schlafen, sich fürchten, feiern? Dann wähle zwei Wörter aus der letzten Zeile der Hörkarte.",
   "info": "D1 fragt nach Merkmalen der Musik (schnell, hoch), D2 nach dem Eindruck, den sie macht."},
  {"typ": "frei", "abschnitt": TEIL_D, "punkte": 2,
   "frage": "**D3 (2 P)** Begründe eine deiner Aussagen mit etwas, das du in der Musik hörst.",
   "muster": "Die Musik wirkt leicht und verspielt, weil sie sehr schnell ist und die Töne hoch und kurz sind.",
   "kriterien": ["Aussage: Eine Wirkung wird genannt", "Beleg aus der Musik: Tempo, Tonlage, Instrument, Lautstärke oder Rhythmus (nicht nur ein Bild im Kopf)"],
   "tipp": "Dreischritt: Wirkung nennen, „weil“ sagen, ein hörbares Merkmal anfügen. Die Belege hast du in D1 schon angekreuzt.",
   "info": "Ein schönes Bild darf als Ergänzung dabeistehen, gibt aber vermutlich keinen Punkt, wenn es nichts über die Musik selbst sagt."}
 ]
}

write('musik-6-notennamen-notenwerte-vorzeichen.json', p1)
write('musik-6-pausen-taktarten.json', p2)
write('musik-6-probearbeit-wanderlied-hoeren.json', p3)

# Liste der Pakete im Repo ergänzen
ix_path = os.path.join(OUT, 'index.json')
try:
    ix = json.load(open(ix_path, encoding='utf-8'))
except Exception:
    ix = []
for name in ['musik-6-notennamen-notenwerte-vorzeichen.json', 'musik-6-pausen-taktarten.json', 'musik-6-probearbeit-wanderlied-hoeren.json']:
    if name not in ix:
        ix.append(name)
with open(ix_path, 'w', encoding='utf-8') as f:
    json.dump(ix, f, ensure_ascii=False, indent=1)
    f.write('\n')

for p in (p1, p2, p3):
    print(p['id'], len(p['aufgaben']), 'Aufgaben')
