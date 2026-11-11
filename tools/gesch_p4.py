"""Geschichte Klasse 6, Teil 4: Steinzeit (Lernzettel Punkt 6, Altsteinzeit).

Zwei Pakete:
  4a  Steinzeit, Eiszeit und Werkzeuge (Name, Gliederung, Zeitspannen, Eiszeit, Tiere, Werkzeuge, Quellen)
  4b  Jagen, Sammeln und Leben in der Altsteinzeit (Waffen, Rentier, Feuer, nicht sesshaft, Handel)

Fakten stehen in /home/claude/gesch-work/fakten.md (Abschnitt 5). Zahlen und Rechnungen werden im Code berechnet und geprüft.
Heft vor Buch: Die Steinzeit hat laut Heft zwei Teile, die Mittelsteinzeit aus dem Buch zählt als Ergänzung, nicht als Fehler.
"""
from gesch_lib import *
from gesch_lib import _svg, _label, _num, _arrow

# ------------------------------------------------------------------ Zahlen und Fakten (aus fakten.md)

HEUTE = 2026                                   # Jahr der Klassenarbeit
ALT_ENDE = -9000                               # Heft: Altsteinzeit bis ca. 9000 v. Chr.
JUNG_VON, JUNG_BIS = -9000, -3000              # Heft: Jungsteinzeit ca. 9000 bis ca. 3000 v. Chr.
JUNG_DAUER = spanne(JUNG_VON, JUNG_BIS)
assert JUNG_DAUER == 6000
SEIT_ENDE = HEUTE - JUNG_BIS                   # Jahre vom Ende der Steinzeit bis 2026 (Jahre davor und danach zusammenzählen)
assert SEIT_ENDE == 5026 and 5000 < SEIT_ENDE < 5100
WUERM_DAUER = 100_000                          # Würm-Eiszeit ca. 100 000 Jahre

# Zeitangaben "vor ... Jahren" (Buch S. 19/20 und S. 21)
VOR_STEINWERKZEUG = 2_000_000
VOR_MUSIK = 40_000
VOR_NAEHNADEL = 24_000
VOR_FEUER_NUTZEN = 1_500_000
VOR_FEUER_SELBST = (150_000, 100_000)
assert VOR_MUSIK - VOR_NAEHNADEL == 16_000
assert VOR_FEUER_NUTZEN - max(VOR_FEUER_SELBST) > 1_000_000 and VOR_FEUER_NUTZEN - min(VOR_FEUER_SELBST) > 1_000_000
assert VOR_STEINWERKZEUG > VOR_FEUER_NUTZEN > max(VOR_FEUER_SELBST) > VOR_MUSIK > VOR_NAEHNADEL


def tausend(n, trenner="."):
    return f"{n:,}".replace(",", trenner)


def zahlen(n, einheit=None):
    """Akzeptierte Schreibweisen einer ganzen Zahl: 6000, 6.000, 6 000, jeweils auch mit Einheit."""
    basis = list(dict.fromkeys([str(n), tausend(n, "."), tausend(n, " ")]))
    res = list(basis)
    if einheit:
        res += [f"{b} {einheit}" for b in basis]
    return res


def L(t, *titel):
    """Verfeinert den Verweis „Nachlesen“ einer einzelnen Aufgabe (Titel des Lernblatt-Abschnitts)."""
    t["lesen"] = titel[0] if len(titel) == 1 else list(titel)
    return t


def vor(n):
    """Jahre als Text: 2000000 -> '2 Mio.', 1500000 -> '1,5 Mio.', 24000 -> '24 000'."""
    if n >= 1_000_000:
        return f"{n / 1_000_000:g}".replace(".", ",") + " Mio."
    return tausend(n, " ")


assert vor(2_000_000) == "2 Mio." and vor(1_500_000) == "1,5 Mio." and vor(24_000) == "24 000"


def zeitraum(a, b):
    """Epochen-Zeitraum als Text, Jahre negativ = v. Chr."""
    if a is None:
        return f"bis {abs(b)} v. Chr."
    return f"{abs(a)} bis {abs(b)} v. Chr."


# ------------------------------------------------------------------ Zeichnung: Werkzeuge der Altsteinzeit (selbst gezeichnet, vereinfacht)

WERKZEUGE = ["Faustkeil", "Klinge", "Schaber", "Harpune", "Nähnadel"]


def _wz(k, cx, y0):
    """Ein Werkzeug (vereinfachte Umrisszeichnung, nicht maßstabsgetreu) mit Mittellinie bei cx, Oberkante y0."""
    stein, knochen, rand = "#c9bb9d", "#eadfc4", "#4f4126"
    if k == "Faustkeil":
        d = (f'M {cx} {y0} C {cx + 48} {y0 + 36} {cx + 54} {y0 + 104} {cx + 24} {y0 + 142} C {cx + 12} {y0 + 156} {cx - 12} {y0 + 156} {cx - 24} {y0 + 142} '
             f'C {cx - 54} {y0 + 104} {cx - 48} {y0 + 36} {cx} {y0} Z')
        g = f'<path d="{d}" fill="{stein}" stroke="{rand}" stroke-width="3" stroke-linejoin="round"/>'
        for (x1, y1, x2, y2) in ((-26, 60, 0, 70), (0, 70, 24, 56), (-22, 100, 6, 108), (6, 108, 28, 96), (-8, 36, 8, 44)):
            g += f'<polyline points="{cx + x1},{y0 + y1} {cx + x2},{y0 + y2}" fill="none" stroke="#8d7d5c" stroke-width="2.2" stroke-linecap="round"/>'
        return g
    if k == "Klinge":
        pts = f'{cx - 14},{y0 + 156} {cx - 16},{y0 + 34} {cx},{y0 + 2} {cx + 16},{y0 + 34} {cx + 14},{y0 + 156}'
        return (f'<polygon points="{pts}" fill="{stein}" stroke="{rand}" stroke-width="3" stroke-linejoin="round"/>'
                f'<line x1="{cx}" y1="{y0 + 14}" x2="{cx}" y2="{y0 + 150}" stroke="#8d7d5c" stroke-width="2.2"/>')
    if k == "Schaber":
        d = (f'M {cx - 54} {y0 + 128} C {cx - 62} {y0 + 70} {cx - 24} {y0 + 24} {cx + 26} {y0 + 34} C {cx + 58} {y0 + 44} {cx + 62} {y0 + 96} {cx + 50} {y0 + 128} Z')
        return (f'<path d="{d}" fill="{stein}" stroke="{rand}" stroke-width="3" stroke-linejoin="round"/>'
                f'<path d="M {cx - 46} {y0 + 80} C {cx - 40} {y0 + 44} {cx - 12} {y0 + 34} {cx + 24} {y0 + 42} C {cx + 46} {y0 + 50} {cx + 50} {y0 + 80} {cx + 44} {y0 + 100}" '
                f'fill="none" stroke="#8d7d5c" stroke-width="2.4" stroke-dasharray="5 4"/>')
    if k == "Harpune":
        g = (f'<polygon points="{cx - 6},{y0 + 22} {cx},{y0 - 4} {cx + 6},{y0 + 22}" fill="{knochen}" stroke="{rand}" stroke-width="3" stroke-linejoin="round"/>'
             f'<rect x="{cx - 6}" y="{y0 + 20}" width="12" height="140" rx="3" fill="{knochen}" stroke="{rand}" stroke-width="3"/>')
        for dy in (34, 62, 90, 118):
            g += (f'<polygon points="{cx + 6},{y0 + dy} {cx + 28},{y0 + dy + 24} {cx + 6},{y0 + dy + 20}" fill="{knochen}" stroke="{rand}" stroke-width="2.6" stroke-linejoin="round"/>')
        return g
    if k == "Nähnadel":
        return (f'<polygon points="{cx - 3.5},{y0 + 34} {cx + 3.5},{y0 + 34} {cx + 1},{y0 + 166} {cx - 1},{y0 + 166}" fill="{knochen}" stroke="{rand}" stroke-width="3" stroke-linejoin="round"/>'
                f'<ellipse cx="{cx}" cy="{y0 + 30}" rx="8" ry="18" fill="{knochen}" stroke="{rand}" stroke-width="3"/>'
                f'<ellipse cx="{cx}" cy="{y0 + 28}" rx="2.8" ry="9" fill="#ffffff" stroke="{rand}" stroke-width="2"/>')
    raise AssertionError(k)


def svg_werkzeuge(namen=True, reihenfolge=(0, 1, 2, 3, 4)):
    """Fünf Werkzeuge der Altsteinzeit nebeneinander: Faustkeil, Klinge, Schaber, Harpune, Nähnadel (vereinfacht gezeichnet).

    namen=True: Namen darunter. namen=False: Buchstaben A bis E von links, reihenfolge sagt, welches Werkzeug an welcher Stelle steht.
    """
    assert sorted(reihenfolge) == [0, 1, 2, 3, 4]
    g = []
    for i, k in enumerate(reihenfolge):
        cx = 76 + 152 * i
        g.append(_wz(WERKZEUGE[k], cx, 24))
        txt = WERKZEUGE[k] if namen else "ABCDE"[i]
        g.append(f'<text x="{cx}" y="{240 if namen else 242}" font-size="{16 if namen else 22}" font-weight="bold" fill="#1b1b1b" text-anchor="middle" '
                 f'stroke="#fff" stroke-width="4" paint-order="stroke" stroke-linejoin="round">{txt}</text>')
    return _svg(760, 262, ''.join(g))


def werkzeug_buchstabe(reihenfolge, name):
    return "ABCDE"[list(reihenfolge).index(WERKZEUGE.index(name))]


# ================================================================== PAKET 4a: Steinzeit, Eiszeit und Werkzeuge

T_NAME = "Woher der Name Steinzeit kommt"
T_TEILE = "Die Steinzeit in Teile gliedern"
T_ZEIT = "Die Steinzeit auf dem Zeitstrahl"
T_EISZEIT = "Die Eiszeit: Klima und Landschaft"
T_TIERE = "Tiere der Eiszeit"
T_WERKZEUGE = "Werkzeuge und Geräte der Altsteinzeit"
T_HERSTELLEN = "Werkzeuge herstellen und benutzen"
T_QUELLEN = "Quellen der Steinzeit"


def lernblatt_a():
    return [
        lb(T_NAME,
           "Die frühen Menschen stellten ihre Werkzeuge zuerst aus **Stein** her. Stein hält sehr lange, deshalb war er das erste **dauerhafte Material** für Werkzeuge.\n"
           "Neben Stein war auch **Holz** wichtig. Das blieb so, bis die Menschen gelernt hatten, **Metalle** zu verarbeiten.\n"
           "Nach dem Material der Werkzeuge nennt man diese lange Zeit die **Steinzeit**.",
           merke="Die Steinzeit heißt so, weil die Menschen ihre Werkzeuge aus Stein machten. Holz und Stein waren die wichtigsten Materialien, bis man Metalle verarbeiten konnte."),
        lb(T_TEILE,
           "Die Steinzeit war sehr lang. In dieser Zeit lernten die Menschen immer besser, Stein zu bearbeiten. Deshalb teilt man sie in Abschnitte ein.\n"
           "Dein Lehrer teilt die Steinzeit in **zwei Teile** ein. Das ist die Antwort für die Arbeit:\n"
           f"- **Altsteinzeit**: bis etwa {abs(ALT_ENDE)} v. Chr.\n"
           f"- **Jungsteinzeit**: etwa {abs(JUNG_VON)} bis {abs(JUNG_BIS)} v. Chr.\n"
           "Dein Schulbuch nennt zusätzlich einen dritten Teil, die **Mittelsteinzeit**. Sie gehört zur Zeit nach der Eiszeit: In Mitteleuropa lebten die Menschen damals noch rund 3000 Jahre als Jäger und Sammler im Wald. Der Ackerbau kam dort erst ab etwa 5700 v. Chr. an.\n"
           f"Die Jahreszahlen sind nur Näherungswerte, und sie hängen vom Ort ab: Um {abs(JUNG_VON)} v. Chr. begannen im Nahen Osten die ersten Menschen, sesshaft zu werden. In Mitteleuropa lebte man noch lange als Jäger und Sammler. Deshalb ist die Mittelsteinzeit eine Ergänzung und kein Widerspruch.\n"
           "Für die Teile gibt es Fachwörter: **Paläolithikum** heißt Altsteinzeit, **Mesolithikum** heißt Mittelsteinzeit und **Neolithikum** heißt Jungsteinzeit.",
           merke="Laut Heft hat die Steinzeit zwei Teile: Altsteinzeit (bis ca. 9000 v. Chr.) und Jungsteinzeit (ca. 9000 bis 3000 v. Chr.). Das Buch nennt zusätzlich die Mittelsteinzeit. Die Jahreszahlen sind Näherungswerte und hängen vom Ort ab."),
        lb(T_ZEIT,
           "Die Geschichte teilt man in fünf große Zeitabschnitte ein, die **Epochen**. Die erste heißt **Ur- und Frühgeschichte** und reicht bis 3000 v. Chr. Die ganze Steinzeit liegt in dieser Epoche. Danach folgen Altertum, Antike, Mittelalter und Neuzeit.\n"
           "Zeitspannen rechnest du so aus:\n"
           f"- Die Jungsteinzeit dauerte nach dem Heft von {abs(JUNG_VON)} bis {abs(JUNG_BIS)} v. Chr. Bei Jahren vor Christi Geburt rechnest du rückwärts, also {abs(JUNG_VON)} − {abs(JUNG_BIS)} = {JUNG_DAUER} Jahre.\n"
           f"- Vom Ende der Steinzeit (3000 v. Chr.) bis zum Jahr {HEUTE} zählst du die Jahre vor und nach Christi Geburt zusammen: {abs(JUNG_BIS)} + {HEUTE} = {SEIT_ENDE} Jahre.",
           merke="Die Steinzeit gehört zur Epoche Ur- und Frühgeschichte (bis 3000 v. Chr.). Über Christi Geburt hinweg zählst du die Jahre zusammen.",
           bild=svg_epochen(nummern=False),
           bildAlt="Zeitstrahl mit den fünf Epochen: Ur- und Frühgeschichte bis 3000 v. Chr., Altertum 3000 bis 1000 v. Chr., Antike 1000 v. Chr. bis 500 n. Chr., Mittelalter 500 bis 1500 n. Chr., Neuzeit ab 1500 n. Chr."),
        lb(T_EISZEIT,
           f"In der Altsteinzeit wechselten kalte und warme Zeiten mehrmals. Die letzte Kaltzeit heißt **Würm-Eiszeit** und dauerte etwa {tausend(WUERM_DAUER, ' ')} Jahre. Sie war nicht immer gleich kalt: Kurze, etwas wärmere Phasen wechselten mit sehr kalten.\n"
           "In Europa lebten in dieser Zeit **Neandertaler** (eine andere Menschenart) und **moderne Menschen** zur selben Zeit.\n"
           "Das passierte in der Eiszeit:\n"
           "- Die Temperaturen sanken weltweit stark.\n"
           "- **Gletscher** (riesige Eismassen) dehnten sich weit aus. Zur größten Ausdehnung war sogar die Gegend um Berlin von Eis bedeckt.\n"
           "- Viel Wasser war im Eis gebunden. Deshalb sank der **Meeresspiegel**.\n"
           "- Es gab nur wenig Niederschlag. Kälte und Trockenheit ließen in Mitteleuropa keine Wälder wachsen. Stattdessen gab es eine weite, offene **Steppe** mit Gräsern, Kräutern und niedrigen Büschen.",
           merke="Würm-Eiszeit: letzte Kaltzeit, etwa 100 000 Jahre. Gletscher wuchsen, der Meeresspiegel sank, in Mitteleuropa gab es Steppe statt Wald. Neandertaler und moderne Menschen lebten zugleich in Europa."),
        lb(T_TIERE,
           "Die Steppe bot Futter für riesige Herden. Dazu kamen Raubtiere, die Herden und Menschen gefährlich werden konnten.\n"
           "- **Große Pflanzenfresser**: Mammut, Wollnashorn, Steppenbison und Höhlenbär. Dazu riesige Herden von Rentieren und Wildpferden.\n"
           "- **Raubtiere**: Höhlenlöwe, Wolf und Höhlenhyäne.\n"
           "Das Buch nennt die großen Tiere dieser Zeit die „Giganten der Eiszeit“.",
           merke="Pflanzenfresser: Mammut, Wollnashorn, Steppenbison, Höhlenbär, Rentier, Wildpferd. Raubtiere: Höhlenlöwe, Wolf, Höhlenhyäne."),
        lb(T_WERKZEUGE,
           f"Schon vor etwa **{vor(VOR_STEINWERKZEUG)} Jahren** stellten Menschen einfache Werkzeuge aus Stein her. Ein Beispiel ist der **Faustkeil** aus einem Geröllstein. Damit kam man an Fleisch und Knochenmark.\n"
           "Die Neandertaler machten aus Stein Faustkeile, **Schaber**, **Klingen**, Spitzen und Messer. Ein wichtiges Material war der **Feuerstein**.\n"
           "Später kamen **Knochen, Geweih und Elfenbein** dazu. Daraus machte man Werkzeuge, Messer, **Harpunen** (Spitzen zum Fischfang), Speere und Speerschleudern.\n"
           "Wichtige Zeitangaben:\n"
           f"- vor etwa {vor(VOR_STEINWERKZEUG)} Jahren: einfache Steinwerkzeuge\n"
           f"- vor etwa {tausend(VOR_MUSIK, ' ')} Jahren: Musikinstrumente\n"
           f"- vor etwa {tausend(VOR_NAEHNADEL, ' ')} Jahren: Nähnadeln aus Knochen\n"
           "Zusatz: Mit einem Schaber bearbeitete man zum Beispiel Felle. Eine Klinge ist ein langes, schmales Steinstück mit scharfer Kante.",
           merke="Werkzeuge aus Feuerstein, Knochen, Geweih und Elfenbein. Steinwerkzeuge gibt es seit etwa 2 Mio. Jahren, Musikinstrumente seit etwa 40 000 und Nähnadeln seit etwa 24 000 Jahren.",
           bild=svg_werkzeuge(namen=True),
           bildAlt="Fünf vereinfacht gezeichnete Werkzeuge der Altsteinzeit: Faustkeil, Klinge, Schaber, Harpune mit Widerhaken und Nähnadel mit Öhr."),
        lb(T_HERSTELLEN,
           "Stein kann man nicht schnitzen wie Holz. Man bearbeitete ihn mit einem **Schlagstein** oder mit einem Geweih. Wenn man Stücke abschlägt, entsteht ein Werkzeug mit scharfer Kante.\n"
           "Benutzt wurden solche Werkzeuge zum Beispiel, um Fleisch zu zerschneiden.\n"
           "So kann man sich die Herstellung vorstellen:\n"
           "- Man sucht einen passenden Stein, zum Beispiel Feuerstein.\n"
           "- Man schlägt mit dem Schlagstein Stücke ab.\n"
           "- Man arbeitet die Kanten nach, bis sie scharf sind.\n"
           "- Dann benutzt man das Werkzeug.\n"
           "Zusatz: Die einzelnen Schritte sind Allgemeinwissen. Im Buch steht nur, dass man Stein mit Schlagstein oder Geweih bearbeitet und die Werkzeuge zum Beispiel zum Zerschneiden von Fleisch benutzt.",
           merke="Stein wird mit Schlagstein oder Geweih bearbeitet. So entstehen Werkzeuge mit scharfen Kanten, zum Beispiel zum Zerschneiden von Fleisch."),
        lb(T_QUELLEN,
           "Aus der Altsteinzeit gibt es keine Texte. Die Menschen konnten damals noch nicht schreiben (Zusatz). Trotzdem wissen wir viel, denn sie haben **Spuren** hinterlassen. Solche Hinterlassenschaften nennt man **Quellen**.\n"
           "Wichtige Quellen der Steinzeit:\n"
           "- **Sachquellen** (das Buch sagt: gegenständliche Quellen): Knochen, Faustkeile, Harpunen, Nähnadeln, Schmuck.\n"
           "- **Bilder**: zum Beispiel Höhlenzeichnungen.\n"
           "**Zeitzeugen** sind Menschen, die eine Zeit selbst erlebt haben und davon erzählen können. Sie sind eine weitere Art von Quellen. Aus der Altsteinzeit lebt aber niemand mehr, deshalb gibt es von dort keine Zeitzeugen.\n"
           "Eine **Rekonstruktionszeichnung** zeigt, wie sich ein Zeichner das Leben von damals vorstellt. Er hat sie viel später gemacht, mithilfe der Funde. Sie ist deshalb eine **Darstellung** und keine Quelle. Die Funde, auf denen sie beruht, sind die Quellen.",
           merke="Funde sind Quellen. Eine Rekonstruktionszeichnung ist eine Darstellung, denn sie wurde später von Menschen gemacht, die die Zeit nicht erlebt haben."),
    ]


def aufgaben_a():
    A = []
    # ------------------------------------------------------------------ A Name und Gliederung
    s = "A – Name und Gliederung der Steinzeit"
    A += [
        L(mc("Warum heißt die Steinzeit „Steinzeit“?",
             "Die Menschen machten ihre Werkzeuge aus Stein.",
             ["Die Menschen bauten ihre Häuser aus Stein.", "Die Menschen wohnten fast nur in Höhlen aus Stein.", "Die Menschen schützten sich mit Mauern aus Stein."], s,
             info="Stein war das erste dauerhafte Material für Werkzeuge. Nach diesem Material hat die Zeit ihren Namen."), T_NAME),
        L(luecke("Ergänze den Text über den Namen.",
                 "Die {{Steinzeit}} heißt so, weil die Menschen ihre Werkzeuge aus {{Stein}} herstellten. Neben Stein war lange auch {{Holz}} wichtig, bis die Menschen lernten, {{Metalle}} zu verarbeiten.",
                 s, extra=["Glas", "Wolle"],
                 info="Holz und Stein waren die wichtigsten Materialien, bis man Metalle verarbeiten konnte."), T_NAME),
        L(tf("Das Wort „Steinzeit“ bedeutet, dass die Menschen damals nur Stein und kein Holz benutzten.", False, s,
             info="Holz und Stein waren die wichtigsten Materialien. Stein war das erste dauerhafte Material für Werkzeuge."), T_NAME),
        L(tf("Nach deinem Heft hat die Steinzeit zwei Teile: die Altsteinzeit und die Jungsteinzeit.", True, s,
             info="Im Heft stehen zwei Teile. Das Buch nennt zusätzlich die Mittelsteinzeit, das ist eine Ergänzung und kein Widerspruch."), T_TEILE),
        L(mc("Man kann die Steinzeit in Teile gliedern. Wähle alle richtigen Einteilungen.",
             ["Zwei Teile: Altsteinzeit und Jungsteinzeit", "Drei Teile: Altsteinzeit, Mittelsteinzeit und Jungsteinzeit"],
             ["Zwei Teile: Frühsteinzeit und Spätsteinzeit", "Drei Teile: Altsteinzeit, Eisenzeit und Jungsteinzeit"], s,
             info="Im Heft stehen zwei Teile, im Buch drei Teile mit der Mittelsteinzeit. Beides ist richtig."), T_TEILE),
        L(zuordnen("Ordne jedem Fachwort seine Bedeutung zu.",
                   [("Paläolithikum", "Altsteinzeit"), ("Mesolithikum", "Mittelsteinzeit"), ("Neolithikum", "Jungsteinzeit"), ("Epoche", "großer Zeitabschnitt der Geschichte")], s,
                   extra=["Bronzezeit", "Eisenzeit"],
                   info="Die drei langen Wörter sind die Fachwörter für die Teile der Steinzeit. Eine Epoche ist ein großer Zeitabschnitt, zum Beispiel die Ur- und Frühgeschichte. Zusatz: Die Fachwörter kommen aus dem Griechischen, „lithos“ heißt Stein."),
          T_TEILE, T_ZEIT),
        L(kurz("Wie heißt der älteste Teil der Steinzeit, der bis etwa 9000 v. Chr. dauerte?", ["Altsteinzeit", "die Altsteinzeit", "Paläolithikum"], s,
               info="Die Altsteinzeit reicht bis etwa 9000 v. Chr. Danach beginnt nach dem Heft die Jungsteinzeit."), T_TEILE),
        L(kurz("Wie heißt nach deinem Heft der Teil der Steinzeit von etwa 9000 bis etwa 3000 v. Chr.?", ["Jungsteinzeit", "die Jungsteinzeit", "Neolithikum"], s,
               info="Die Jungsteinzeit dauerte nach dem Heft von etwa 9000 bis etwa 3000 v. Chr."), T_TEILE),
        L(mc("Warum teilt man die Steinzeit in mehrere Abschnitte ein?",
             "Die Menschen entwickelten die Bearbeitung von Stein immer weiter.",
             ["In jedem Abschnitt wurde ein anderes Metall benutzt.", "In jedem Abschnitt bauten die Menschen größere Städte.", "Die Menschen zogen in jedem Abschnitt in ein anderes Land."], s,
             info="Das Buch sagt: Die Kunst der Steinbearbeitung wurde stetig weiterentwickelt und verbessert. Deshalb gliedert man die Steinzeit."), T_TEILE),
        L(tf("Wer in der Arbeit zusätzlich die Mittelsteinzeit nennt, hat etwas Falsches geschrieben.", False, s,
             info="Das Buch teilt in drei Teile ein, deshalb ist die Mittelsteinzeit nicht falsch. Sicher wissen musst du die zwei Teile aus dem Heft.",
             tipp="Denke an den Unterschied zwischen Heft und Buch."), T_TEILE),
    ]
    # ------------------------------------------------------------------ B Epochen und Zeitspannen
    s = "B – Die Steinzeit in der Zeit"
    assert epoche(-7000) == "Ur- und Frühgeschichte" and epoche(-5000) == "Ur- und Frühgeschichte" and epoche(-2000) == "Altertum"
    B_EP = EPOCHEN[0][0]
    A += [
        L(mc("Auf dem Zeitstrahl sind die fünf Epochen nummeriert. Welche Nummer trägt die Epoche, zu der die Steinzeit gehört?",
             "Nummer 1", ["Nummer 2", "Nummer 3", "Nummer 4"], s,
             info="Die Steinzeit gehört zur Ur- und Frühgeschichte, der ersten Epoche. Sie reicht bis 3000 v. Chr.",
             tipp="Zähle die Epochen von links nach rechts. Die Steinzeit ist sehr alt.",
             bild=svg_epochen(nummern=True),
             bildAlt="Zeitstrahl mit fünf nummerierten Epochen von der ersten bis zur Neuzeit, Jahreszahlen 3000 v. Chr., 1000 v. Chr., Christi Geburt, 500 und 1500."), T_ZEIT),
        L(kurz("Zu welcher Epoche der Geschichte gehört die Steinzeit?",
               ["Ur- und Frühgeschichte", "Ur und Frühgeschichte", "Ur-und Frühgeschichte", "Ur- u. Frühgeschichte", "die Ur- und Frühgeschichte"], s,
               info="Die erste Epoche heißt Ur- und Frühgeschichte und reicht bis 3000 v. Chr."), T_ZEIT),
        L(kurz(f"Die Jungsteinzeit dauerte nach dem Heft von {abs(JUNG_VON)} bis {abs(JUNG_BIS)} v. Chr. Wie viele Jahre waren das?",
               zahlen(JUNG_DAUER, "Jahre"), s, einheit="Jahre",
               info=f"Bei Jahren vor Christi Geburt rechnest du rückwärts: {abs(JUNG_VON)} − {abs(JUNG_BIS)} = {JUNG_DAUER}.",
               tipp="Beide Jahre liegen vor Christi Geburt. Ziehe die kleinere Zahl von der größeren ab."), T_ZEIT),
        L(mc(f"Die Steinzeit endete etwa {abs(JUNG_BIS)} v. Chr. Wie lange ist das bis {HEUTE} ungefähr her?",
             "gut 5000 Jahre", ["etwa 1000 Jahre", "etwa 3000 Jahre", "etwa 9000 Jahre"], s,
             info=f"Du zählst die Jahre vor und nach Christi Geburt zusammen: {abs(JUNG_BIS)} + {HEUTE} = {SEIT_ENDE} Jahre, also gut 5000.",
             tipp="Der Weg geht über Christi Geburt hinweg."), T_ZEIT),
        L(zuordnen("Ordne jedem Abschnitt seinen Zeitraum zu. Die Jahre stehen so im Heft und sind gerundet.",
                   [("Altsteinzeit", zeitraum(None, ALT_ENDE)), ("Jungsteinzeit", zeitraum(JUNG_VON, JUNG_BIS)),
                    ("Ur- und Frühgeschichte (Epoche)", zeitraum(EPOCHEN[0][1], EPOCHEN[0][2])), ("Altertum (Epoche)", zeitraum(EPOCHEN[1][1], EPOCHEN[1][2]))], s,
                   extra=[zeitraum(EPOCHEN[3][1], EPOCHEN[3][2]).replace("v. Chr.", "n. Chr.")],
                   info="Nach dem Heft endet die Altsteinzeit um 9000 v. Chr. und die Jungsteinzeit um 3000 v. Chr. Dort endet auch die Ur- und Frühgeschichte, dann beginnt das Altertum."), T_ZEIT),
        L(kurz("Welche Epoche folgt direkt auf die Ur- und Frühgeschichte?", [EPOCHEN[1][0], "das " + EPOCHEN[1][0]], s,
               info="Die Reihenfolge der Epochen: Ur- und Frühgeschichte, Altertum, Antike, Mittelalter, Neuzeit."), T_ZEIT),
        L(reihenfolge("Ordne vom ältesten zum jüngsten Abschnitt.", ["Altsteinzeit", "Jungsteinzeit", "Altertum", "Mittelalter"], s,
                      info="Alt- und Jungsteinzeit gehören zur Ur- und Frühgeschichte (bis 3000 v. Chr.). Danach folgen das Altertum und später das Mittelalter (ab 500 n. Chr.)."), T_ZEIT),
        L(luecke("Ergänze den Text über die Zeit.",
                 f"Die Steinzeit liegt in der Epoche {{{{Ur- und Frühgeschichte}}}}. Sie endet etwa {{{{{abs(JUNG_BIS)}}}}} v. Chr. Dann beginnt das {{{{Altertum}}}}. Nach dem Heft dauerte die Jungsteinzeit {{{{{JUNG_DAUER}}}}} Jahre.",
                 s, extra=["Antike", "1000"],
                 info="Die Ur- und Frühgeschichte reicht bis 3000 v. Chr., danach beginnt das Altertum."), T_ZEIT),
        L(tf("Das Jahr 7000 v. Chr. liegt in der Epoche Altertum.", epoche(-7000) == "Altertum", s,
             info="Das Altertum beginnt erst 3000 v. Chr. 7000 v. Chr. ist älter und gehört zur Ur- und Frühgeschichte.",
             tipp="Je größer die Zahl bei v. Chr., desto länger ist es her."), T_ZEIT),
    ]
    # ------------------------------------------------------------------ C Eiszeit und Tiere
    s = "C – Eiszeit, Klima und Tiere"
    A += [
        L(kurz("Wie heißt die letzte Kaltphase der Eiszeit?", ["Würm-Eiszeit", "Würm Eiszeit", "Würmeiszeit", "die Würm-Eiszeit", "Würm"], s,
               info="Die Würm-Eiszeit war die letzte Kaltphase und dauerte etwa 100 000 Jahre."), T_EISZEIT),
        L(kurz("Wie viele Jahre dauerte die Würm-Eiszeit ungefähr?", zahlen(WUERM_DAUER, "Jahre"), s, einheit="Jahre",
               info=f"Die Würm-Eiszeit dauerte etwa 100 000 Jahre. Zum Vergleich: Die Jungsteinzeit dauerte nach dem Heft nur {JUNG_DAUER} Jahre."), T_EISZEIT),
        L(mc("Was passierte in der Würm-Eiszeit? Wähle alle richtigen Antworten.",
             ["Gletscher dehnten sich weit aus.", "Der Meeresspiegel sank.", "Es fiel nur wenig Niederschlag."],
             ["In Mitteleuropa wuchsen dichte Mischwälder.", "Der Meeresspiegel stieg stark an."], s,
             info="Viel Wasser war im Eis gebunden, deshalb sank der Meeresspiegel. Wälder gab es wegen Kälte und Trockenheit nicht, Mischwälder kamen erst nach der Eiszeit."), T_EISZEIT),
        L(mc("Warum sank der Meeresspiegel in der Eiszeit?",
             "Viel Wasser war als Eis in den Gletschern gebunden.",
             ["Das Wasser der Meere verdunstete in der Kälte.", "Das Wasser versickerte im Boden von Mitteleuropa.", "Die Sonne trocknete die Meere aus."], s,
             info="Die Gletscher dehnten sich aus und hielten riesige Wassermengen als Eis fest. Darum fehlte Wasser in den Meeren.",
             tipp="Wohin ging das Wasser, wenn es kalt war?"), T_EISZEIT),
        L(mc("Welche Landschaft gab es in der Eiszeit in Mitteleuropa?",
             "eine weite, offene Steppe", ["dichten Mischwald", "eine heiße Wüste", "einen tropischen Regenwald"], s,
             info="Kälte und Trockenheit verhinderten Wälder. Es wuchsen Gräser, Kräuter und niedrige Büsche."), T_EISZEIT),
        L(zuordnen("Pflanzenfresser oder Raubtier? Ordne die Tiere der Eiszeit zu.",
                   [("Mammut", "Pflanzenfresser"), ("Höhlenlöwe", "Raubtier"), ("Wollnashorn", "Pflanzenfresser"), ("Wolf", "Raubtier"),
                    ("Steppenbison", "Pflanzenfresser"), ("Höhlenhyäne", "Raubtier")], s,
                   info="Mammut, Wollnashorn und Steppenbison fraßen Pflanzen. Höhlenlöwe, Wolf und Höhlenhyäne waren Raubtiere und gefährlich für Herden und Menschen."), T_TIERE),
        L(mc("Welche Tiere zogen in riesigen Herden durch die Steppe? Wähle alle richtigen Antworten.",
             ["Rentiere", "Wildpferde"], ["Höhlenlöwen", "Höhlenhyänen"], s,
             info="Riesige Herden von Rentieren und Wildpferden lebten in der Eiszeit-Steppe. Höhlenlöwen und Höhlenhyänen waren Raubtiere."), T_TIERE),
        L(tf("Während der gesamten Altsteinzeit blieb es ununterbrochen gleich kalt.", False, s,
             info="Warme und kalte Perioden wechselten sich mehrmals ab. Auch in der Würm-Eiszeit gab es kurze, etwas wärmere Phasen."), T_EISZEIT),
        L(mc("Welche Aussage über die Menschen in der Würm-Eiszeit stimmt?",
             "Neandertaler und moderne Menschen lebten zugleich in Europa.",
             ["Nur Neandertaler lebten damals in Europa.", "Nur moderne Menschen lebten damals in Europa.", "Damals lebte in Europa niemand, weil es zu kalt war."], s,
             info="Neandertaler und moderne Menschen lebten in Europa zugleich. Das steht im Buch bei der Würm-Eiszeit."), T_EISZEIT),
        L(luecke("Ergänze den Text über die Eiszeit.",
                 f"In der Eiszeit dehnten sich die {{{{Gletscher}}}} weit aus. Viel Wasser war im Eis gebunden, deshalb sank der {{{{Meeresspiegel}}}}. Weil es kalt und trocken war, gab es keine Wälder, sondern weite {{{{Steppe|Steppen|Steppenlandschaft}}}}. Die Würm-Eiszeit dauerte etwa {{{{{tausend(WUERM_DAUER, ' ')}|{WUERM_DAUER}|{tausend(WUERM_DAUER)}}}}} Jahre.",
                 s, extra=["Wälder", "Wüsten"],
                 info="Gletscher, sinkender Meeresspiegel und Steppe gehören zum Klima der Würm-Eiszeit."), T_EISZEIT),
    ]
    # ------------------------------------------------------------------ D Werkzeuge und Geräte
    s = "D – Werkzeuge und Geräte"
    perm_d = (3, 0, 4, 1, 2)   # A Harpune, B Faustkeil, C Nähnadel, D Klinge, E Schaber
    bild_d = svg_werkzeuge(namen=False, reihenfolge=perm_d)
    assert werkzeug_buchstabe(perm_d, "Schaber") == "E" and werkzeug_buchstabe(perm_d, "Nähnadel") == "C"
    alt_d = "Fünf Werkzeuge der Altsteinzeit mit den Buchstaben A bis E: A Harpune mit Widerhaken, B Faustkeil, C Nähnadel mit Öhr, D Klinge, E Schaber."
    z_nadel = [("Einfache Steinwerkzeuge", f"vor ca. {vor(VOR_STEINWERKZEUG)} Jahren"), ("Musikinstrumente", f"vor ca. {tausend(VOR_MUSIK, ' ')} Jahren"),
               ("Nähnadeln", f"vor ca. {tausend(VOR_NAEHNADEL, ' ')} Jahren")]
    A += [
        L(zuordnen("Aus welchem Material waren die Geräte der Altsteinzeit gemacht?",
                   [("Faustkeil", "Stein"), ("Schaber", "Stein"), ("Klinge", "Stein"), ("Harpune", "Knochen oder Geweih"), ("Nähnadel", "Knochen oder Geweih")], s, extra=["Kupfer"],
                   info="Faustkeile, Schaber und Klingen schlug man aus Stein. Harpunen machte man aus Knochen oder Geweih. Nähnadeln zeigt das Buch aus Knochen, und das passt ebenfalls zu „Knochen oder Geweih“."), T_WERKZEUGE),
        L(mc("Aus welchen Materialien stellten die Menschen der Altsteinzeit Werkzeuge her? Wähle alle richtigen Antworten.",
             ["Feuerstein", "Knochen", "Geweih", "Elfenbein"], ["Bronze", "Eisen"], s,
             info="Neben Feuerstein nutzte man Knochen, Geweih und Elfenbein. Metalle konnten die Menschen damals noch nicht verarbeiten."), T_WERKZEUGE),
        L(kurz("Welcher Stein war ein wichtiges Material für Werkzeuge? Sein Name enthält das Wort „Feuer“.", ["Feuerstein", "der Feuerstein", "Flint"], s,
               info="Aus Feuerstein schlug man Faustkeile, Klingen und Spitzen. Zusatz: Feuerstein heißt auch Flint."), T_WERKZEUGE),
        L(mc("Wozu benutzte man einen einfachen Faustkeil aus Geröll vor etwa 2 Millionen Jahren?",
             "Um an Fleisch und Knochenmark zu kommen.",
             ["Um Felle zusammenzunähen.", "Um Getreide zu mahlen.", "Um Tiere aus der Ferne zu erlegen."], s,
             info="Mit dem Faustkeil kam man an Fleisch und Knochenmark. Nähnadeln zum Nähen von Fellen gab es erst vor etwa 24 000 Jahren."), T_WERKZEUGE),
        L(tf("Schon die Neandertaler stellten Faustkeile, Schaber und Klingen aus Stein her.", True, s,
             info="Das steht im Buch: Neandertaler machten Faustkeile, Schaber, Klingen, Spitzen und Messer aus Stein."), T_WERKZEUGE),
        L(mc("Welches Werkzeug zeigt der Buchstabe E?", "Schaber", ["Faustkeil", "Klinge", "Harpune"], s, bild=bild_d, bildAlt=alt_d,
             info="Der Faustkeil ist mandelförmig, die Klinge lang und schmal, der Schaber flach mit einer runden Arbeitskante. Die Harpune hat Widerhaken.",
             tipp="Vergleiche die Zeichnungen mit dem Bild im Lernblatt."), T_WERKZEUGE),
        L(reihenfolge("Ordne vom ältesten zum jüngsten Fund.", ["Einfache Steinwerkzeuge", "Musikinstrumente", "Nähnadeln"], s,
                      info=f"Steinwerkzeuge gibt es seit etwa {vor(VOR_STEINWERKZEUG)} Jahren, Musikinstrumente seit etwa {tausend(VOR_MUSIK, ' ')} und Nähnadeln seit etwa {tausend(VOR_NAEHNADEL, ' ')} Jahren.",
                      tipp="Je länger es her ist, desto älter ist der Fund."), T_WERKZEUGE),
        L(zuordnen("Ordne jeder Erfindung oder Zeitspanne die Angabe zu.",
                   z_nadel + [("Würm-Eiszeit (Dauer)", f"ca. {tausend(WUERM_DAUER, ' ')} Jahre")], s, extra=["vor ca. 4000 Jahren"],
                   info="Alle Angaben sind gerundet. Die Eiszeit dauerte etwa 100 000 Jahre, die anderen drei Zeitangaben sagen, wie lange die Erfindung her ist."), T_WERKZEUGE, T_EISZEIT),
        L(luecke("Ergänze den Text über die Werkzeuge.",
                 f"Aus Feuerstein machte man {{{{Faustkeile}}}}, Schaber und Klingen. Vor etwa {tausend(VOR_MUSIK, ' ')} Jahren gab es schon {{{{Musikinstrumente}}}}, und vor etwa {tausend(VOR_NAEHNADEL, ' ')} Jahren gab es {{{{Nähnadeln}}}} aus Knochen. Fische fing man mit {{{{Harpunen}}}}.",
                 s, extra=["Pflüge", "Webstühle"],
                 info="Die Zeitangaben stehen im Buch. Harpunen wurden aus Knochen oder Geweih gemacht."), T_WERKZEUGE),
    ]
    # ------------------------------------------------------------------ E Herstellen und Quellen
    s = "E – Herstellen, benutzen und Quellen"
    A += [
        L(mc("Welche Aussage über eine Rekonstruktionszeichnung der Altsteinzeit stimmt?",
             "Sie ist eine Darstellung, die später nach Funden gemacht wurde.",
             ["Sie ist eine Quelle, denn sie zeigt Menschen der Steinzeit.", "Sie wurde von Menschen der Altsteinzeit selbst gezeichnet.", "Sie ist eine schriftliche Quelle, die aus der Steinzeit stammt."], s,
             info="Ein Zeichner von heute hat sie gemacht und die Zeit nicht selbst erlebt, also ist sie eine Darstellung. Die Funde dahinter sind die Quellen."), T_QUELLEN),
        L(zuordnen("Quelle oder Darstellung? Ordne zu.",
                   [("Faustkeil aus der Altsteinzeit", "Quelle"), ("Zeichnung, die ein Zeichner heute von einem Eiszeit-Lager macht", "Darstellung"),
                    ("Knochen eines Mammuts", "Quelle"), ("Schulbuchtext über die Altsteinzeit", "Darstellung"),
                    ("Höhlenmalerei von Menschen der Eiszeit", "Quelle"), ("Harpune aus Geweih", "Quelle")], s,
                   info="Quellen stammen aus der Zeit selbst. Darstellungen machen Menschen später, ohne die Zeit erlebt zu haben, und sie benutzen dafür Quellen."), T_QUELLEN),
        L(kurz("Zu welcher Quellenart zählen im Heft Knochen, Faustkeile und Harpunen?", ["Sachquellen", "Sachquelle", "gegenständliche Quellen", "gegenständliche Quelle"], s,
               info="Im Heft heißen sie Sachquellen, im Buch gegenständliche Quellen. Gemeint sind greifbare Dinge."), T_QUELLEN),
        L(tf("Zeitzeugen können uns von der Altsteinzeit erzählen.", False, s,
             info="Zeitzeugen haben die Zeit selbst erlebt. Aus der Altsteinzeit lebt niemand mehr, deshalb sind wir auf Funde angewiesen."), T_QUELLEN),
        L(mc("Warum gibt es aus der Altsteinzeit keine Texte als Quellen?",
             "Die Menschen konnten damals noch nicht schreiben.",
             ["Die Menschen schrieben nur auf Holz, und das ist verrottet.", "Die Steinzeit ist zu lange her, deshalb sind alle Texte verloren.", "Texte zählen nicht zu den Quellen."], s,
             info="Zusatz: Schrift gab es in der Altsteinzeit noch nicht. Texte sind aber Quellen, und zwar für spätere Zeiten."), T_QUELLEN),
        L(luecke("Ergänze den Text über die Quellen der Steinzeit.",
                 "Wir wissen etwas über die Altsteinzeit aus {{Funden}} wie Knochen, Werkzeugen und Höhlenbildern. Solche Hinterlassenschaften nennt man {{Quellen}}. Eine Rekonstruktionszeichnung ist dagegen eine {{Darstellung}}. Knochen, Waffen und Werkzeuge sind greifbare Dinge und zählen zu den {{Sachquellen|Quellen}}.",
                 s, extra=["Zeitzeugen", "Urkunden"],
                 info="Funde sind Quellen. Die Zeichnung, die ein Zeichner später daraus macht, ist eine Darstellung. Greifbare Dinge heißen Sachquellen, sie sind natürlich auch Quellen. Zeitzeugen haben die Zeit selbst erlebt, die gibt es aus der Altsteinzeit nicht mehr."), T_QUELLEN),
        L(reihenfolge("Ordne die Herstellung eines Steinwerkzeugs in die richtige Reihenfolge.",
                      ["Man sucht einen passenden Stein, zum Beispiel Feuerstein.", "Man schlägt mit einem Schlagstein Stücke ab.",
                       "Man arbeitet die Kanten nach, bis sie scharf sind.", "Man benutzt das Werkzeug, zum Beispiel zum Zerschneiden von Fleisch."], s,
                      info="Zusatz: Die Schritte sind Allgemeinwissen. Im Buch steht, dass man Stein mit Schlagstein oder Geweih bearbeitet und mit den Werkzeugen zum Beispiel Fleisch zerschneidet.",
                      tipp="Zuerst braucht man etwas zum Bearbeiten, zuletzt benutzt man das fertige Werkzeug."), T_HERSTELLEN),
        L(mc("Womit bearbeitete man Stein in der Altsteinzeit? Wähle alle richtigen Antworten.",
             ["mit einem Schlagstein", "mit einem Geweih"], ["mit einem Metallhammer", "mit einer Eisensäge"], s,
             info="Im Buch steht, dass man Stein mit einem Schlagstein oder mit Geweih bearbeitete. Metalle kannte man noch nicht."), T_HERSTELLEN),
    ]
    # ------------------------------------------------------------------ F Klausurnah
    s = "F – Klausurnah: Steinzeit, Eiszeit, Werkzeuge"
    perm_f = (2, 3, 4, 0, 1)   # A Schaber, B Harpune, C Nähnadel, D Faustkeil, E Klinge
    pairs_f = [("ABCDE"[i], WERKZEUGE[k]) for i, k in enumerate(perm_f)]
    A += [
        zuordnen("Beschrifte die Abbildung: Ordne jedem Buchstaben das richtige Werkzeug zu.", pairs_f, s, extra=["Steinbeil"],
                 info="Der Faustkeil ist mandelförmig, die Klinge lang und schmal, der Schaber hat eine runde Arbeitskante, die Harpune Widerhaken und die Nähnadel ein Öhr.",
                 bild=svg_werkzeuge(namen=False, reihenfolge=perm_f),
                 bildAlt="Fünf Werkzeuge mit den Buchstaben A bis E: A Schaber, B Harpune mit Widerhaken, C Nähnadel mit Öhr, D Faustkeil, E Klinge."),
        L(mc("Eine Mitschülerin schreibt über die Steinzeit. Welcher Satz enthält einen Fehler?",
           "Die Steinzeit gehört zur Epoche Altertum.",
           ["Die letzte Kaltzeit hieß Würm-Eiszeit und dauerte etwa 100 000 Jahre.", "Faustkeile und Schaber stellten schon die Neandertaler her.",
            "Eine Rekonstruktionszeichnung ist eine Darstellung und keine Quelle."], s,
           info="Die Steinzeit gehört zur Ur- und Frühgeschichte. Das Altertum beginnt erst 3000 v. Chr., wenn die Steinzeit endet.",
           tipp="Drei Sätze stimmen. Prüfe jeden einzeln."), T_ZEIT, T_EISZEIT, T_WERKZEUGE, T_QUELLEN),
        L(luecke("Fasse die Steinzeit zusammen. Ergänze den Text.",
               "Nach dem Heft hat die Steinzeit zwei Teile: die {{Altsteinzeit}} bis etwa 9000 v. Chr. und die {{Jungsteinzeit}} bis etwa 3000 v. Chr. Das Buch nennt zusätzlich die {{Mittelsteinzeit}}. Die ganze Steinzeit gehört zur Epoche {{Ur- und Frühgeschichte}}.",
               s, extra=["Antike", "Bronzezeit"],
               info="Zwei Teile laut Heft, die Mittelsteinzeit als Ergänzung aus dem Buch. Die Jahreszahlen sind Näherungswerte. Die Epoche ist die erste: Ur- und Frühgeschichte."), T_TEILE, T_ZEIT),
        L(frei("Nenne die Teile der Steinzeit mit ihren Zeitangaben und erkläre, woher der Name Steinzeit kommt.",
             "Nach dem Heft hat die Steinzeit zwei Teile: die Altsteinzeit bis etwa 9000 v. Chr. und die Jungsteinzeit von etwa 9000 bis etwa 3000 v. Chr. Das Buch nennt dazu noch die Mittelsteinzeit. "
             "Die Steinzeit heißt so, weil die Menschen ihre Werkzeuge aus Stein herstellten. Stein war das erste dauerhafte Material dafür, und Holz und Stein blieben wichtig, bis man Metalle verarbeiten konnte.",
             ["Altsteinzeit und Jungsteinzeit genannt", "Zeitangaben richtig (bis ca. 9000 v. Chr. und ca. 9000 bis 3000 v. Chr.)", "Name erklärt: Werkzeuge aus Stein", "Holz und Stein als wichtige Materialien oder Stein als erstes dauerhaftes Material"],
             4, s, info="Die Mittelsteinzeit darf zusätzlich genannt werden, sie ist kein Fehler."), T_NAME, T_TEILE),
        L(frei("Beschreibe die Würm-Eiszeit: Wie lange dauerte sie, wie war das Klima und welche Landschaft gab es? Nenne außerdem zwei Pflanzenfresser und zwei Raubtiere.",
             "Die Würm-Eiszeit war die letzte Kaltphase und dauerte etwa 100 000 Jahre. Es war sehr kalt und trocken, dazwischen gab es kurze wärmere Phasen. Gletscher dehnten sich weit aus. "
             "Viel Wasser war im Eis gebunden, deshalb sank der Meeresspiegel. Wälder wuchsen in Mitteleuropa nicht, stattdessen gab es eine weite Steppe. "
             "Pflanzenfresser waren zum Beispiel Mammut und Wollnashorn, Raubtiere zum Beispiel Höhlenlöwe und Wolf. In Europa lebten damals Neandertaler und moderne Menschen zur selben Zeit.",
             ["etwa 100 000 Jahre", "kalt und trocken, Gletscher breiten sich aus", "Meeresspiegel sinkt, weil Wasser im Eis gebunden ist", "Steppe statt Wald", "zwei Pflanzenfresser genannt", "zwei Raubtiere genannt"],
             6, s), T_EISZEIT, T_TIERE),
        L(frei("Woher wissen wir etwas über die Werkzeuge der Altsteinzeit? Nenne zwei Werkzeuge mit ihrem Material und erkläre, warum eine Rekonstruktionszeichnung keine Quelle ist.",
             "Wir wissen es aus Funden, zum Beispiel aus Faustkeilen aus Stein und aus Harpunen oder Nähnadeln aus Knochen oder Geweih. Solche Funde sind Sachquellen. "
             "Eine Rekonstruktionszeichnung ist keine Quelle, sondern eine Darstellung. Ein Zeichner hat sie viel später gemacht, mithilfe der Funde, und er hat die Zeit nicht selbst erlebt.",
             ["Funde als Grundlage genannt", "erstes Werkzeug mit passendem Material", "zweites Werkzeug mit passendem Material", "Rekonstruktionszeichnung ist eine Darstellung", "Begründung: später und mithilfe der Funde gemacht"],
             5, s), T_WERKZEUGE, T_QUELLEN),
    ]
    return A


def paket_a():
    p = pack("geschichte-4a-steinzeit-eiszeit-werkzeuge", "Geschichte Teil 4a: Steinzeit, Eiszeit und Werkzeuge",
             "Woher die Steinzeit ihren Namen hat, wie man sie einteilt und einordnet, wie die Eiszeit war, welche Werkzeuge es gab und was wir aus Funden wissen. Mit Lernblatt und vielen Übungsaufgaben.",
             lernblatt_a(), aufgaben_a(), min_aufgaben=42,
             hinweis="Im Heft hat die Steinzeit zwei Teile, im Buch drei (mit der Mittelsteinzeit). In den Aufgaben zählen beide Einteilungen als richtig. Die Jahreszahlen sind Näherungswerte und hängen vom Ort ab.")
    assert 42 <= len(p["aufgaben"]) <= 55, len(p["aufgaben"])
    assert 5 <= len(p["lernblatt"]) <= 9
    nachlesen(p, {
        "A – Name und Gliederung der Steinzeit": [T_NAME, T_TEILE],
        "B – Die Steinzeit in der Zeit": T_ZEIT,
        "C – Eiszeit, Klima und Tiere": [T_EISZEIT, T_TIERE],
        "D – Werkzeuge und Geräte": T_WERKZEUGE,
        "E – Herstellen, benutzen und Quellen": [T_HERSTELLEN, T_QUELLEN],
        "F – Klausurnah: Steinzeit, Eiszeit, Werkzeuge": [T_TEILE, T_EISZEIT, T_WERKZEUGE, T_QUELLEN],
    })
    p["probe"] = False
    return p


# ================================================================== PAKET 4b: Jagen, Sammeln und Leben in der Altsteinzeit

T_JAGEN = "Jagen und Sammeln: wovon die Menschen lebten"
T_TECHNIK = "Wie man in der Altsteinzeit jagte"
T_WAFFEN = "Waffen und ihre Reichweiten"
T_RENTIER = "Das Rentier: fast alles wurde genutzt"
T_SAMMELN = "Sammeln und Fischen"
T_FEUER = "Feuer nutzen und selbst machen"
T_NOMADEN = "Unterwegs leben: nicht sesshaft"
T_NATUR = "Abhängig von der Natur und Vorräte"
T_HANDEL = "Handel und Schmuck"

W_NAMEN = [w[0] for w in WAFFEN]
W_MAX = {w[0]: w[2] for w in WAFFEN}
W_MIN = {w[0]: w[1] for w in WAFFEN}
# Fortschritt: jede Waffe reicht weiter als die vorige (Reihenfolge der Entwicklung = Reihenfolge nach größter Reichweite)
assert W_NAMEN == sorted(W_NAMEN, key=lambda n: W_MAX[n]) and W_NAMEN == ["Lanze", "Speer", "Speerschleuder", "Pfeil und Bogen"]
assert W_MAX["Speerschleuder"] == 2 * W_MAX["Speer"]
assert W_MAX["Pfeil und Bogen"] - W_MAX["Speer"] == 35 and W_MAX["Pfeil und Bogen"] - W_MAX["Lanze"] == 47


def m(a, b):
    return f"{a} bis {b} m"


def trifft(entfernung):
    """Waffen, die eine Beute in dieser Entfernung (Meter) erreichen."""
    return [n for n in W_NAMEN if W_MIN[n] <= entfernung <= W_MAX[n]]


assert trifft(20) == ["Speerschleuder", "Pfeil und Bogen"] and trifft(45) == ["Pfeil und Bogen"] and trifft(10) == ["Speer", "Speerschleuder", "Pfeil und Bogen"]
assert "Lanze" not in trifft(10)

NT = list(NUTZTIER)          # Geweih, Fell/Haut, Sehnen, Fleisch, Magen, Knochen


def nt_teil(perm, nr):
    """Welches Teil trägt in der Zeichnung mit dieser Nummerierung die Nummer nr?"""
    return NT[list(perm).index(nr)]


def nt_nr(perm, teil):
    return perm[NT.index(teil)]


def gruppe_formen():
    """Schreibweisen für die Gruppengröße 25 bis 30 (Bindestrich, Gedankenstrich, „bis“, mit und ohne Wort danach)."""
    res = []
    for vorne in ("", "etwa ", "ca. "):
        for a in ("25 bis 30", "25-30", "25 - 30", "25 – 30", "25–30"):
            for hinten in ("", " Personen", " Menschen"):
                res.append(f"{vorne}{a}{hinten}")
    for hinten in ("", " Personen", " Menschen"):
        res += [f"zwischen 25 und 30{hinten}", f"25 und 30{hinten}"]
    return list(dict.fromkeys(res))


assert "25-30 Personen" in gruppe_formen() and "zwischen 25 und 30" in gruppe_formen() and "25 bis 30" in gruppe_formen()


def lernblatt_b():
    wl ="\n".join(f"- **{n}**: {m(W_MIN[n], W_MAX[n])}" for n in W_NAMEN)
    return [
        lb(T_JAGEN,
           "In der Altsteinzeit kannte man noch keinen **Ackerbau** und keine **Viehzucht**. Die Menschen lebten von dem, was die Natur ihnen bot. Ihre Lebensgrundlage waren die **Jagd** auf Großwild und das **Sammeln** von Pflanzen.\n"
           "Gejagt wurden vor allem Rentier, Pferd, Bison und Wollnashorn. Ein Mammut erlegte man nur selten.\n"
           "Meist jagten die **Männer**, und die **Frauen** sammelten. Deshalb spricht man vom **Zeitalter der Sammlerinnen und Jäger**.\n"
           "Die Jagd auf Großwild war gefährlich. Verletzungen kamen oft vor.",
           merke="Lebensgrundlage: Jagen und Sammeln. Meist jagten die Männer und die Frauen sammelten. Man sagt: Zeitalter der Sammlerinnen und Jäger."),
        lb(T_TECHNIK,
           "Es gab zwei Arten zu jagen:\n"
           "- **Nah am Tier**: Eine Gruppe trieb ein Tier in eine **Engstelle** oder in sumpfiges Gelände. Dort erlegte sie es mit **Lanzen**.\n"
           "- **Aus der Distanz**: Man jagte mit **Speeren**, **Schleudern** (dazu gehört die Speerschleuder) oder mit **Pfeil und Bogen**. Auch **Bumerangs** gab es schon. Sie sind keine Erfindung aus Australien.\n"
           "Der Unterschied zwischen Lanze und Speer liegt in der **Reichweite** (mehr dazu im nächsten Abschnitt): Die Lanze reicht nur 0 bis 3 m, der Jäger muss also ganz nah ans Tier. Der Speer reicht bis 15 m.\n"
           "Zusatz: In der Engstelle oder im Sumpf konnte das Tier wohl nicht mehr gut ausweichen.",
           merke="Nah: Tier in Engstelle oder Sumpf treiben und mit Lanzen erlegen. Aus der Distanz: Speere, Schleudern, Pfeil und Bogen."),
        lb(T_WAFFEN,
           "Die Jagdwaffen wurden im Lauf der Zeit besser. Die **Reichweite** sagt, wie weit entfernt ein Tier stehen darf, damit man es noch treffen kann. Das Bild zeigt die Reichweiten in Metern. Die Reihenfolge der Entwicklung ist:\n"
           f"{wl}\n"
           "Die **Speerschleuder** ist ein Hilfsmittel, mit dem man einen Speer weiter werfen kann (Zusatz).\n"
           "Die neueren Waffen waren ein **Fortschritt**. Man konnte ein Tier aus der Ferne töten. Das war weniger gefährlich, und man konnte besser zielen.",
           merke="Reihenfolge: Lanze, Speer, Speerschleuder, Pfeil und Bogen. Jede neue Waffe reichte weiter. Ein Fortschritt, denn man konnte das Tier aus der Ferne töten.",
           bild=svg_waffen(namen=True),
           bildAlt="Balkendiagramm der Reichweiten in Metern: Lanze 0 bis 3, Speer 0 bis 15, Speerschleuder 8 bis 30, Pfeil und Bogen 5 bis 50."),
        lb(T_RENTIER,
           "Vom erlegten Tier wurde nahezu alles verwertet. Das Schema im Buch zeigt es am **Rentier**:\n"
           "- **Fleisch**: Nahrung\n"
           "- **Fell und Haut**: Kleidung und Zelte\n"
           "- **Geweih und Knochen**: Werkzeuge. Harpunen machte man aus Knochen oder Geweih, Nähnadeln aus Knochen.\n"
           "- **Sehnen**: Fäden zum Nähen und Binden (Zusatz)\n"
           "- **Magen**: Behälter, zum Beispiel für Wasser oder Vorräte (Zusatz)",
           merke="Vom Rentier nutzte man Fleisch, Fell und Haut, Geweih, Knochen, Sehnen und Magen. Fast nichts wurde weggeworfen.",
           bild=svg_nutztier(nummern=False),
           bildAlt="Schema eines Rentiers mit den sechs Teilen Geweih, Fell/Haut, Sehnen, Fleisch, Magen und Knochen."),
        lb(T_SAMMELN,
           "Neben der Jagd war das Sammeln wichtig. Gesammelt wurden zum Beispiel Beeren, Nüsse, Pilze, Wurzeln, Kräuter, Wildobst, Körner wilder Getreidearten, Honig, Eier und Insekten. Getreide wurde noch nicht angebaut, es wuchs wild.\n"
           "Man kannte auch **Heilpflanzen**. Das sind Pflanzen, die gegen Krankheiten helfen, zum Beispiel Thymian, Malve, Kornblume und Rosmarin.\n"
           "Fische fing man mit **Harpunen**. Später kamen **Reusen** (Fangkörbe) und Angelhaken dazu.",
           merke="Sammeln: Beeren, Körner, Pilze, Honig, Eier, Kräuter, Wurzeln, Nüsse und Heilpflanzen. Fische: erst Harpunen, später Reusen und Angelhaken."),
        lb(T_FEUER,
           f"Vor etwa **1,5 Millionen Jahren** begannen Menschen, Feuer zu hüten und zu nutzen, zum Beispiel nach einem Blitzeinschlag. Feuer gab **Wärme** und **Schutz** vor wilden Tieren. Gegartes Fleisch war **leichter verdaulich** und gesünder.\n"
           f"Selbst erzeugen konnten die Menschen Feuer erst vor etwa **{tausend(max(VOR_FEUER_SELBST), ' ')} bis {tausend(min(VOR_FEUER_SELBST), ' ')} Jahren**. Dazwischen lagen mehr als eine Million Jahre. Es ging auf zwei Wegen:\n"
           "- durch Reibung zweier Hölzer\n"
           "- durch Funkenschlag von Feuersteinen\n"
           "Nach dem Buch benutzte man zum Entfachen **Zunderschwamm**, Feuerstein und **Pyrit**. Pyrit ist ein glänzendes Gestein, das man auch **Katzengold** nennt. Zusatz: Der Zunderschwamm nimmt die Funken auf und glimmt.",
           merke="Feuer nutzen: seit etwa 1,5 Mio. Jahren. Selbst erzeugen: erst vor etwa 150 000 bis 100 000 Jahren, mit Reibung von Hölzern oder Funken von Feuersteinen. Vorteile: Wärme, Schutz, Fleisch leichter verdaulich."),
        lb(T_NOMADEN,
           "Die Menschen der Altsteinzeit hatten keinen festen, dauerhaften Wohnsitz. Man sagt: Sie waren **nicht sesshaft**. Menschen, die immer weiterziehen, nennt man **Nomaden**.\n"
           "Sie lebten in kleinen Gruppen von etwa **25 bis 30 Personen**.\n"
           "Sie folgten den **Wanderbewegungen der Beutetiere**, zum Beispiel von Wildpferd, Rentier und Mammut. Je nach Jahreszeit und Nahrungsangebot wechselten sie ihre **Lagerplätze**. Ein Lagerplatz ist ein Ort, an dem eine Gruppe eine Zeit lang wohnt. Sie wohnten in **Zelten** aus Fell und Stangen. Ein nachgebautes Haus-Zelt steht im Archäopark Vogelherd in Baden-Württemberg.",
           merke="Nicht sesshaft: kein fester Wohnsitz, kleine Gruppen von etwa 25 bis 30 Personen, Zelte, wechselnde Lagerplätze. Die Gruppen folgten den Beutetieren."),
        lb(T_NATUR,
           "Die Menschen waren der Natur viel stärker ausgeliefert als wir heute. Lebensbedrohlich konnten werden:\n"
           "- Klimaschwankungen\n"
           "- Erdbeben\n"
           "- das Ausbleiben von Jagdwild\n"
           "- zu geringe Erträge beim Sammeln\n"
           "Gegen den Mangel half es, Fleisch zu **konservieren**, also haltbar zu machen, und in **Depots** aufzubewahren. Depots sind Vorratslager. Das konnten schon die eiszeitlichen Jäger. Zusatz: In der Kälte der Eiszeit blieb Fleisch lange frisch.",
           merke="Die Menschen waren von der Natur abhängig. Fleisch konservieren und in Depots lagern half gegen Mangel."),
        lb(T_HANDEL,
           "Schon in der Altsteinzeit tauschte man Dinge über große Entfernungen. Das zeigen Funde:\n"
           "- **Pyrit** aus Norditalien wurde in Polen, Deutschland und der Schweiz gefunden.\n"
           "- Gehäuse von Schnecken und Muscheln aus dem Mittelmeergebiet fand man als **Schmuck** in Andernach (Rheinland-Pfalz).\n"
           "Die Funde sind Quellen. Sie zeigen, dass Menschen Kontakt hatten und Dinge weitergaben.",
           merke="Pyrit aus Norditalien und Muschelschmuck aus dem Mittelmeergebiet zeigen: Man handelte schon in der Altsteinzeit über große Entfernungen."),
    ]


def aufgaben_b():
    A = []
    # ------------------------------------------------------------------ A Jagen und Sammeln
    s = "A – Jagen und Sammeln"
    A += [
        mc("Wovon lebten die Menschen in der Altsteinzeit hauptsächlich?",
           "Von der Jagd auf Großwild und vom Sammeln.",
           ["Von Ackerbau und Viehzucht auf eigenen Feldern.", "Vom Handel mit selbst hergestellten Töpfen.", "Vom Fischen in selbst angelegten Teichen."], s,
           info="Ackerbau und Viehzucht begannen erst mit der Jungsteinzeit, ab etwa 9000 v. Chr. Davor war Jagen und Sammeln die Lebensgrundlage."),
        kurz("Wie nennt das Heft die Zeit, in der meist die Männer jagten und die Frauen sammelten?",
             ["Zeitalter der Sammlerinnen und Jäger", "Sammlerinnen und Jäger", "Zeitalter der Jäger und Sammler", "Jäger und Sammler"], s,
             info="Weil meist die Männer jagten und die Frauen sammelten, spricht man vom Zeitalter der Sammlerinnen und Jäger."),
        kurz("Wer sammelte in der Altsteinzeit meistens Pflanzen? Schreibe „Männer“ oder „Frauen“.", ["Frauen", "die Frauen"], s,
             info="Meist jagten die Männer und die Frauen sammelten."),
        tf("In der Altsteinzeit hielten die Menschen schon Schafe und Rinder als Haustiere.", False, s,
           info="Viehzucht gehört zur Jungsteinzeit. In der Altsteinzeit lebten die Menschen vom Jagen und Sammeln.",
           tipp="Wann begannen Ackerbau und Viehzucht?"),
        luecke("Ergänze den Text über die Lebensgrundlage.",
               "Die {{Jagd}} auf Großwild und das {{Sammeln}} von Pflanzen waren die Lebensgrundlage. Meist jagten die {{Männer}}, und die {{Frauen}} sammelten. Die Menschen kannten noch keinen {{Ackerbau}} und keine Viehzucht.",
               s, extra=["Bergbau", "Töpferei"],
               info="Ackerbau und Viehzucht kamen erst in der Jungsteinzeit."),
        tf("Die Jagd auf Großwild war damals ungefährlich.", False, s,
           info="Die Jagd war gefährlich. Verletzungen kamen häufig vor."),
        mc("Welche Tiere jagten die Menschen der Altsteinzeit? Wähle alle richtigen Antworten.",
           ["Rentier", "Wildpferd", "Wollnashorn"], ["Hausschwein", "Hausschaf"], s,
           info="Gejagt wurden Rentier, Pferd, Bison, Wollnashorn und selten das Mammut. Haustiere wie Schwein und Schaf gab es noch nicht."),
    ]
    # ------------------------------------------------------------------ B Jagdtechniken
    s = "B – Jagdtechniken"
    A += [
        mc("Wie jagte eine Gruppe ein großes Tier mit Lanzen?",
           "Sie trieb es in eine Engstelle oder in sumpfiges Gelände.",
           ["Sie jagte es zu Pferd über weite Strecken.", "Sie ließ es von allein auf ein Feld laufen.", "Sie fing es lebend in einer Grube mit Eisenspitzen."], s,
           info="Dort erlegte man das Tier mit Lanzen. Zusatz: In der Engstelle oder im Sumpf konnte das Tier wohl nicht mehr gut ausweichen."),
        luecke("Ergänze den Text über die Jagd.",
               "Eine Gruppe trieb ein Tier in eine {{Engstelle}} oder in {{sumpfiges}} Gelände und erlegte es dort mit {{Lanzen}}. Aus der Distanz jagte man mit Speeren, {{Schleudern|Speerschleudern|Pfeil und Bogen}} und {{Pfeil und Bogen|Schleudern|Speerschleudern}}.",
               s, extra=["Faustkeilen", "Sicheln"],
               info="Nah am Tier benutzte man Lanzen, aus der Entfernung Speere, Schleudern, Pfeil und Bogen. Die beiden letzten Wörter sind austauschbar, beide Reihenfolgen zählen."),
        L(reihenfolge("Ordne den Ablauf einer Jagd mit Lanzen.",
                    ["Die Jäger treiben das Tier in eine Engstelle oder ins sumpfige Gelände.",
                     "Sie erlegen das Tier dort mit Lanzen.", "Vom erlegten Tier wird nahezu alles verwertet, zum Beispiel Fleisch, Fell und Geweih."], s,
                    info="Erst wird das Tier in die Enge getrieben, dann erlegt, dann verwertet. Beim Rentier zeigt das Schema im Buch, wie viel man nutzte.",
                    tipp="Man kann nicht verwerten, was noch nicht erlegt ist."), T_TECHNIK, T_RENTIER),
        tf("Das Mammut war das häufigste Beutetier der Jäger.", False, s,
           info="Gejagt wurden vor allem Rentier, Pferd, Bison und Wollnashorn. Ein Mammut erlegte man selten."),
        mc("Mit welchen Waffen jagte man aus der Distanz? Wähle alle richtigen Antworten.",
           ["Speere", "Schleudern", "Pfeil und Bogen"], ["Lanzen", "Faustkeile"], s,
           info="Lanzen nutzte man in der Engstelle nah am Tier. Faustkeile sind Werkzeuge und keine Wurfwaffen."),
        kurz("Welche Wurfwaffe verbindet man oft mit Australien? Nach dem Buch gab es sie schon in der Altsteinzeit.", ["Bumerang", "der Bumerang", "Boomerang", "Bumerangs"], s,
             info="Der Bumerang ist keine australische Erfindung. Auch Jäger der Altsteinzeit kannten ihn."),
    ]
    # ------------------------------------------------------------------ C Waffen und Reichweiten
    s = "C – Waffen und Reichweiten"
    perm1 = (1, 3, 0, 2)    # A Speer, B Pfeil und Bogen, C Lanze, D Speerschleuder
    perm2 = (3, 1, 2, 0)    # A Pfeil und Bogen, B Speer, C Speerschleuder, D Lanze
    assert W_NAMEN[perm1[3]] == "Speerschleuder" and W_NAMEN[perm2[1]] == "Speer"
    l2 = "ABCD"[perm2.index(W_NAMEN.index("Speer"))]
    assert l2 == "B"
    A += [
        reihenfolge("Ordne die Jagdwaffen in der Reihenfolge ihrer Entwicklung.", list(W_NAMEN), s,
                    info="Jede neue Waffe reichte weiter: Lanze, Speer, Speerschleuder, Pfeil und Bogen.",
                    tipp="Schau im Lernblatt auf das Bild mit den Reichweiten."),
        zuordnen("Ordne jeder Waffe ihre Reichweite zu.", [(n, m(W_MIN[n], W_MAX[n])) for n in W_NAMEN], s, extra=["10 bis 100 m"],
                 info="Die Reichweiten stammen aus dem Schaubild im Buch. Mit Pfeil und Bogen traf man am weitesten, bis zu 50 m."),
        mc("Welche Waffe zeigt der Balken D?", W_NAMEN[perm1[3]], [n for n in W_NAMEN if n != W_NAMEN[perm1[3]]], s,
           info="Der Balken D beginnt bei 8 m und endet bei 30 m. Das ist die Speerschleuder.",
           tipp="Lies am unteren Rand ab, wo der Balken beginnt und wo er endet.",
           bild=svg_waffen(namen=False, reihenfolge=perm1),
           bildAlt="Balkendiagramm der Reichweiten mit Buchstaben statt Namen: A reicht von 0 bis 15 m, B von 5 bis 50 m, C von 0 bis 3 m, D von 8 bis 30 m."),
        kurz("Welcher Buchstabe gehört zur Waffe Speer?", [l2, l2.lower()], s,
             info="Der Speer reicht von 0 bis 15 m. Der Balken B hat genau diese Länge.",
             bild=svg_waffen(namen=False, reihenfolge=perm2),
             bildAlt="Balkendiagramm der Reichweiten mit Buchstaben statt Namen: A reicht von 5 bis 50 m, B von 0 bis 15 m, C von 8 bis 30 m, D von 0 bis 3 m."),
        luecke("Ergänze die Reichweiten der Waffen.",
               f"Die {{{{Lanze}}}} reicht {m(W_MIN['Lanze'], W_MAX['Lanze'])}. Der {{{{Speer}}}} reicht {m(W_MIN['Speer'], W_MAX['Speer'])}. Die {{{{Speerschleuder}}}} reicht {m(W_MIN['Speerschleuder'], W_MAX['Speerschleuder'])}. {{{{Pfeil und Bogen}}}} reichen {m(W_MIN['Pfeil und Bogen'], W_MAX['Pfeil und Bogen'])}.",
               s, extra=["Faustkeil", "Harpune"],
               info="Die Waffen reichen immer weiter, von höchstens 3 m bis zu 50 m."),
        kurz("Vergleiche die größten Reichweiten. Um wie viele Meter reicht Pfeil und Bogen weiter als der Speer?",
             zahlen(W_MAX["Pfeil und Bogen"] - W_MAX["Speer"], "m") + [f"{W_MAX['Pfeil und Bogen'] - W_MAX['Speer']} Meter", f"{W_MAX['Pfeil und Bogen'] - W_MAX['Speer']}m"], s, einheit="m",
             info=f"Pfeil und Bogen reichen bis {W_MAX['Pfeil und Bogen']} m, der Speer bis {W_MAX['Speer']} m. Es sind {W_MAX['Pfeil und Bogen']} − {W_MAX['Speer']} = {W_MAX['Pfeil und Bogen'] - W_MAX['Speer']} m.",
             tipp="Lies die beiden größten Werte im Lernblatt ab und bilde den Unterschied."),
        tf("Die größte Reichweite der Speerschleuder ist doppelt so groß wie die des Speers.", W_MAX["Speerschleuder"] == 2 * W_MAX["Speer"], s,
           info=f"Die Speerschleuder reicht bis {W_MAX['Speerschleuder']} m, der Speer bis {W_MAX['Speer']} m. {W_MAX['Speer']} · 2 = {2 * W_MAX['Speer']}."),
        mc("Ein Jäger sieht ein Tier in 20 m Entfernung. Welche Waffen erreichen es? Wähle alle richtigen Antworten.",
           trifft(20), [n for n in W_NAMEN if n not in trifft(20)], s,
           info="20 m liegen im Bereich der Speerschleuder (8 bis 30 m) und von Pfeil und Bogen (5 bis 50 m). Lanze und Speer reichen zu kurz.",
           tipp="Prüfe bei jeder Waffe, ob 20 m zwischen Anfang und Ende der Reichweite liegen."),
        tf("Mit der Lanze kann man ein Tier treffen, das 10 m entfernt steht.", "Lanze" in trifft(10), s,
           info="Die Lanze reicht nur 0 bis 3 m. Man musste dicht am Tier sein, deshalb war es gefährlich."),
        mc("Warum war es ein Fortschritt, von der Lanze zu Pfeil und Bogen zu kommen?",
           "Man konnte Tiere aus der Ferne töten und war weniger in Gefahr.",
           ["Man musste näher an das Tier herangehen und traf besser.", "Die Reichweite wurde kleiner, deshalb traf man genauer.", "Man konnte nur noch kleine Tiere jagen, das war ungefährlicher."], s,
           info="Pfeil und Bogen reichen bis 50 m, die Lanze nur bis 3 m. Man war weniger in Gefahr und konnte besser zielen.",
           tipp="Vergleiche die Reichweiten der beiden Waffen im Lernblatt."),
    ]
    # ------------------------------------------------------------------ D Das Rentier
    s = "D – Das Rentier"
    p0 = (1, 2, 3, 4, 5, 6)
    p1 = (3, 5, 1, 6, 2, 4)
    p2 = (6, 4, 2, 1, 3, 5)
    for pp in (p0, p1, p2):
        assert sorted(pp) == [1, 2, 3, 4, 5, 6]
    # Die Texte der Abbildungen (bildAlt) werden aus der Nummerierung berechnet, p0 ist die Reihenfolge der Liste NUTZTIER
    assert [nt_teil(p0, n) for n in (1, 2, 3, 4, 5, 6)] == NT
    alt0 = ("Rentier mit sechs nummerierten Teilen: " + ", ".join(f"{nt_nr(p0, t)} {t}" for t in sorted(NT, key=lambda t: nt_nr(p0, t))) + ".")
    alt1 = ("Rentier mit sechs nummerierten Teilen: " + ", ".join(f"{nt_nr(p1, t)} {t}" for t in sorted(NT, key=lambda t: nt_nr(p1, t))) + ".")
    alt2 = ("Rentier mit sechs nummerierten Teilen: " + ", ".join(f"{nt_nr(p2, t)} {t}" for t in sorted(NT, key=lambda t: nt_nr(p2, t))) + ".")
    nr_magen = nt_nr(p1, "Magen")
    nr_geweih = nt_nr(p0, "Geweih")
    # Die Nummern 24 bis 26 (4b) hängen von svg_nutztier ab: Jede Nummer sitzt am Ende einer Linie, die zu einem Punkt auf dem Tier führt.
    A += [
        kurz(f"Welches Teil des Rentiers trägt in der Abbildung die Nummer {nr_geweih}?", [nt_teil(p0, nr_geweih), "das " + nt_teil(p0, nr_geweih)], s,
             info="Das Geweih sitzt am Kopf des Rentiers. Man machte daraus zum Beispiel Harpunen.",
             tipp="Folge der Linie von der Nummer bis zum Punkt auf dem Tier.",
             bild=svg_nutztier(nummern=True, perm=p0), bildAlt=alt0),
        mc("Welche Nummer steht in dieser Abbildung am Magen?", str(nr_magen), [str(n) for n in (1, 2, 3, 4, 5, 6) if n != nr_magen][:3], s,
           info="Die Nummern sind in jeder Abbildung anders vergeben. Du musst also in jeder Abbildung neu nachsehen, wo der Magen liegt, und die Nummer am Ende der Linie ablesen.",
           tipp="Folge der Linie von der Nummer bis zum Punkt auf dem Tier. Der Magen liegt im Bauch.",
           bild=svg_nutztier(nummern=True, perm=p1), bildAlt=alt1),
        zuordnen("Welches Teil des Rentiers trägt welche Nummer? Ordne zu.", [(f"Nummer {n}", nt_teil(p2, n)) for n in (1, 2, 3, 4, 5, 6)], s,
                 info="Die sechs Teile sind Geweih, Fell und Haut, Sehnen, Fleisch, Magen und Knochen.",
                 tipp="Folge jeweils der Linie von der Nummer bis zum Punkt auf dem Tier. Das Lernblatt zeigt dir dasselbe Tier mit den Namen.",
                 bild=svg_nutztier(nummern=True, perm=p2), bildAlt=alt2),
        zuordnen("Wozu nutzte man diese Teile des Rentiers?",
                 [("Fleisch", "Nahrung"), ("Fell und Haut", "Kleidung und Zelte"), ("Geweih und Knochen", "Werkzeuge wie Harpunen und Nähnadeln"),
                  ("Sehnen", "Fäden zum Nähen und Binden"), ("Magen", "Behälter")], s, extra=["Töpfe zum Kochen"],
                 info="Zusatz: Sehnen als Fäden und der Magen als Behälter sind Allgemeinwissen. Aus Geweih und Knochen machte man Werkzeuge: Harpunen aus Knochen oder Geweih, Nähnadeln aus Knochen."),
        mc("Welches Teil des Rentiers lieferte das Material für Kleidung und Zeltdecken?", "Fell und Haut", ["Geweih", "Magen", "Sehnen"], s,
           info="Aus Fellen und Leder machte man Kleidung. Auch die Haus-Zelte bestanden aus Fell und Stangen."),
        tf("Von einem erlegten Tier nutzte man nur das Fleisch.", False, s,
           info="Man verwertete nahezu alles: Fleisch, Fell und Haut, Geweih, Sehnen, Magen und Knochen."),
        kurz("Aus welchem Teil des Rentiers machte man Nähnadeln?", ["Knochen", "aus Knochen", "den Knochen"], s,
             info="Nähnadeln gab es schon vor etwa 24 000 Jahren. Man machte sie aus Knochen."),
        luecke("Ergänze den Text über das Rentier.",
               "Das {{Fleisch}} diente als Nahrung. Aus Fell und Haut machte man {{Kleidung}} und Zeltdecken. Nähnadeln stellte man aus {{Knochen}} her. Aus Sehnen wurden {{Fäden}}, und der Magen diente als {{Behälter}}.",
               s, extra=["Töpfe", "Pflüge"],
               info="Zusatz: Sehnen als Fäden und der Magen als Behälter sind Allgemeinwissen. Fast alle Teile des Rentiers wurden genutzt."),
    ]
    # ------------------------------------------------------------------ E Sammeln, Fischen, Feuer
    s = "E – Sammeln, Fischen und Feuer"
    zeiten_f = [("Feuer wird genutzt", VOR_FEUER_NUTZEN), ("Feuer wird selbst erzeugt", max(VOR_FEUER_SELBST)), ("Nähnadeln werden erfunden", VOR_NAEHNADEL)]
    ord_f = [n for n, _ in sorted(zeiten_f, key=lambda x: -x[1])]
    assert ord_f == ["Feuer wird genutzt", "Feuer wird selbst erzeugt", "Nähnadeln werden erfunden"]
    A += [
        mc("Was sammelten die Menschen der Altsteinzeit? Wähle alle richtigen Antworten.",
           ["Beeren", "Pilze", "Nüsse", "Wurzeln"], ["Weizen von eigenen Feldern", "Gemüse aus dem eigenen Garten"], s,
           info="Man sammelte, was die Natur bot: Beeren, Pilze, Nüsse, Wurzeln, Kräuter und mehr. Felder und Gärten gab es noch nicht."),
        tf("Die Menschen der Altsteinzeit bauten Getreide auf Feldern an.", False, s,
           info="Der Ackerbau begann erst in der Jungsteinzeit, ab etwa 9000 v. Chr. Vorher sammelte man wild wachsende Körner."),
        tf("Auch Heilpflanzen wie Thymian oder Malve gehörten zu den gesammelten Pflanzen.", True, s,
           info="Das Buch nennt Thymian, Malve, Kornblume und Rosmarin als Heilpflanzen."),
        luecke("Ergänze den Text über das Sammeln und den Fischfang.",
               "Man sammelte Beeren, Nüsse und Pilze, aber auch {{Heilpflanzen}} wie Thymian. Fische fing man mit {{Harpunen}}, später auch mit {{Reusen}} und Angelhaken.",
               s, extra=["Pflügen", "Sicheln"],
               info="Reusen sind Fangkörbe. Sie kamen später zu den Harpunen dazu."),
        kurz("Vor etwa wie vielen Jahren begannen Menschen, Feuer zu nutzen?", ["1,5 Millionen", "1,5 Mio", "1,5 Mio.", "1,5 Millionen Jahre", "1,5 Millionen Jahren", "1,5 Mio Jahre", "1,5 Mio. Jahre", "1,5 Mio. Jahren", "1.5 Millionen", "1500000", "1.500.000", "1 500 000"], s,
             info="Vor etwa 1,5 Millionen Jahren hütete und nutzte man Feuer, zum Beispiel nach einem Blitzeinschlag."),
        mc("Wie konnten die Menschen Feuer selbst erzeugen? Wähle alle richtigen Antworten.",
           ["durch Reibung zweier Hölzer", "durch Funkenschlag von Feuersteinen"], ["durch Warten auf einen Blitzeinschlag", "durch Aneinanderschlagen von Knochen"], s,
           info="Selbst erzeugen konnte man Feuer erst vor etwa 150 000 bis 100 000 Jahren. Auf einen Blitz zu warten war die ältere Art, an Feuer zu kommen."),
        mc("Welche Vorteile brachte das Feuer? Wähle alle richtigen Antworten.",
           ["Es gab Wärme.", "Es schützte vor wilden Tieren.", "Fleisch wurde leichter verdaulich."],
           ["Es lockte Rentiere zu den Lagerplätzen.", "Es machte Werkzeuge aus Feuerstein überflüssig."], s,
           info="Feuer bot Wärme und Schutz, und gegartes Fleisch war leichter verdaulich und gesünder."),
        reihenfolge("Ordne vom ältesten zum jüngsten Ereignis.", ord_f, s,
                    info=f"Feuer nutzte man seit etwa {vor(VOR_FEUER_NUTZEN)} Jahren, selbst erzeugte man es seit etwa {tausend(max(VOR_FEUER_SELBST), ' ')} bis {tausend(min(VOR_FEUER_SELBST), ' ')} Jahren, und Nähnadeln gibt es seit etwa {tausend(VOR_NAEHNADEL, ' ')} Jahren.",
                    tipp="Je mehr Jahre her, desto älter."),
        luecke("Ergänze den Text über das Feuer.",
               "Vor etwa {{1,5 Millionen|1,5 Mio.|1,5 Mio}} Jahren begannen Menschen, Feuer zu nutzen, zum Beispiel nach einem {{Blitzeinschlag}}. Selbst erzeugen konnten sie es erst viel später, durch {{Reibung}} zweier Hölzer oder {{Funkenschlag}} von Feuersteinen.",
               s, extra=["Regen", "Wind"],
               info=f"Zwischen dem ersten Nutzen und dem Selbermachen lagen mehr als eine Million Jahre ({tausend(VOR_FEUER_NUTZEN, ' ')} − {tausend(max(VOR_FEUER_SELBST), ' ')} = {tausend(VOR_FEUER_NUTZEN - max(VOR_FEUER_SELBST), ' ')})."),
        kurz("Beim Feuermachen benutzte man nach dem Buch Zunderschwamm, Feuerstein und einen glänzenden Stein, der „Katzengold“ genannt wird. Wie heißt dieser Stein?",
             ["Pyrit", "der Pyrit"], s,
             info="Pyrit glänzt wie Gold, deshalb nennt man ihn auch Katzengold. Er wird im Buch zusammen mit Zunderschwamm und Feuerstein beim Entfachen von Feuer genannt."),
    ]
    # ------------------------------------------------------------------ F Nicht sesshaft, Natur, Handel
    s = "F – Unterwegs leben, Natur und Handel"
    A += [
        zuordnen("Ordne jedem Begriff die passende Erklärung zu.",
                 [("sesshaft", "hat einen festen, dauerhaften Wohnsitz"), ("Lagerplatz", "Ort, an dem eine Gruppe eine Zeit lang wohnt"), ("Nomaden", "Menschen, die immer weiterziehen"),
                  ("Beutetier", "Tier, das gejagt wird"), ("konservieren", "Lebensmittel haltbar machen"), ("Depot", "Vorratslager")], s,
                 extra=["Gerät zum Fischfang"],
                 info="Die Menschen der Altsteinzeit waren nicht sesshaft. Sie zogen den Beutetieren nach, wechselten die Lagerplätze und legten Fleischvorräte in Depots an."),
        kurz("Wie viele Personen lebten in der Altsteinzeit etwa in einer Gruppe? Schreibe den Bereich.", gruppe_formen(), s,
             info="Die Gruppen waren klein, etwa 25 bis 30 Personen. Sie zogen gemeinsam weiter."),
        luecke("Ergänze den Text über das Leben unterwegs.",
               "Die Menschen der Altsteinzeit waren nicht {{sesshaft}}. Sie lebten in kleinen Gruppen und wohnten in {{Zelten}}. Sie wechselten ihre {{Lagerplätze}} und folgten den {{Beutetieren}}.",
               s, extra=["Dörfern", "Feldern"],
               info="Wegen der Wanderbewegungen der Beutetiere und des wechselnden Nahrungsangebots zog man weiter."),
        mc("Woraus bestanden die Haus-Zelte der Altsteinzeit?", "aus Fell und Stangen", ["aus Lehm und Stroh", "aus Steinplatten", "aus Holzbalken und Strohdach"], s,
           info="Haus-Zelte aus Fell und Stangen wurden zum Beispiel im Archäopark Vogelherd nachgebaut. Lange Häuser mit Strohdach gehören zur Jungsteinzeit."),
        tf("Eiszeitliche Jäger konnten Fleisch konservieren und in Depots aufbewahren.", True, s,
           info="Vorräte halfen, wenn die Jagd einmal nicht erfolgreich war. Zusatz: In der Eiszeitkälte blieb Fleisch lange frisch."),
        mc("Was konnte für die Menschen der Altsteinzeit lebensbedrohlich werden? Wähle alle richtigen Antworten.",
           ["Klimaschwankungen", "das Ausbleiben von Jagdwild", "zu geringe Erträge beim Sammeln"], ["Ernteausfälle auf den eigenen Feldern", "Streit um Besitz und Land"], s,
           info="Die Menschen waren der Natur stark ausgeliefert. Felder und Besitz um Land gab es erst in der Jungsteinzeit.",
           tipp="Denke an das, wovon die Menschen damals lebten."),
        mc("Was zeigt der Fund von Pyrit aus Norditalien in Polen, Deutschland und der Schweiz?",
           "Schon in der Altsteinzeit tauschte man Dinge über große Entfernungen.",
           ["Pyrit kommt in allen Ländern gleich häufig vor.", "Alle Menschen zogen ständig zwischen Italien und Polen hin und her.", "Der Pyrit wurde dort aus dem Boden gegraben."], s,
           info="Der Stein stammt aus Norditalien, wurde aber weit entfernt gefunden. Also muss er über große Strecken weitergegeben worden sein."),
        tf("Schmuck aus Schnecken- und Muschelgehäusen vom Mittelmeer, der in Andernach gefunden wurde, zeigt weiträumigen Handel.", True, s,
           info="Die Gehäuse stammen aus dem Mittelmeergebiet. Gefunden wurden sie in Andernach in Rheinland-Pfalz, also weit entfernt."),
    ]
    # ------------------------------------------------------------------ G Klausurnah
    s = "G – Klausurnah: Leben in der Altsteinzeit"
    paare_g = [("Nicht sesshaft", "Altsteinzeit"), ("Feste Dörfer", "Jungsteinzeit"), ("Faustkeil", "Altsteinzeit"),
               ("Pflug", "Jungsteinzeit"), ("Zelt aus Fell und Stangen", "Altsteinzeit"), ("Keramik aus Ton", "Jungsteinzeit")]
    A += [
        L(mc("Ein Schüler schreibt über die Altsteinzeit. Welcher Satz enthält einen Fehler?",
           "Die Menschen hatten feste Häuser und bauten Getreide an.",
           ["Die Menschen lebten in kleinen Gruppen und zogen mit Zelten umher.", "Aus der Ferne jagte man zum Beispiel mit Speeren und mit Pfeil und Bogen.",
            "Vom Rentier nutzte man Fell, Geweih, Knochen und Fleisch."], s,
           info="Feste Häuser und Ackerbau gehören zur Jungsteinzeit. In der Altsteinzeit waren die Menschen nicht sesshaft.",
           tipp="Drei Sätze stimmen. Prüfe jeden einzeln."), T_JAGEN, T_NOMADEN, T_WAFFEN, T_RENTIER),
        L(zuordnen("Altsteinzeit oder Jungsteinzeit? Ordne zu.", paare_g, s,
                 info="Nicht sesshaft, Faustkeil und Zelte passen zur Altsteinzeit. Feste Dörfer, Pflug und Keramik gehören zur Jungsteinzeit, als die Menschen sesshaft wurden."), T_JAGEN, T_NOMADEN),
        L(frei("Beschreibe das Leben der Menschen in der Altsteinzeit. Gehe auf Nahrung, Jagd, Feuer, Wohnen und Gefahren ein.",
             "Die Menschen in der Altsteinzeit lebten vom Jagen und Sammeln. Meist jagten die Männer Großwild wie Rentier, Pferd und Bison, und die Frauen sammelten Beeren, Nüsse, Pilze und Wurzeln. "
             "Gejagt wurde mit Lanzen, Speeren, Speerschleudern und später mit Pfeil und Bogen. Vom erlegten Tier verwertete man fast alles, zum Beispiel Fleisch, Fell, Geweih und Knochen. "
             "Das Feuer gab Wärme und Schutz vor wilden Tieren, und das Fleisch war leichter verdaulich. "
             "Die Menschen waren nicht sesshaft. Sie lebten in kleinen Gruppen von etwa 25 bis 30 Personen, wohnten in Zelten und wechselten ihre Lagerplätze, weil sie den Beutetieren folgten. "
             "Das Leben war gefährlich. Die Jagd war riskant, und man war von der Natur abhängig. Klimaschwankungen oder ausbleibendes Wild konnten lebensbedrohlich werden.",
             ["Nahrung: Jagen und Sammeln (Männer jagten, Frauen sammelten)", "Jagdwaffen genannt", "Nutzung der erlegten Tiere (zum Beispiel Rentier)", "Feuer mit Nutzen (Wärme, Schutz, Fleisch leichter verdaulich)",
              "nicht sesshaft: Zelte, wechselnde Lagerplätze, kleine Gruppen", "Gefahren und Abhängigkeit von der Natur"],
             6, s, info="Schreibe zu jedem Bereich mindestens einen Satz."),
          T_JAGEN, T_TECHNIK, T_FEUER, T_NOMADEN, T_NATUR),
        L(frei("War es ein Fortschritt, dass man statt der Lanze Pfeil und Bogen benutzte? Entscheide dich und begründe mit den Reichweiten.",
             f"Ja, das war ein Fortschritt. Die Lanze reicht nur {m(W_MIN['Lanze'], W_MAX['Lanze'])}, Pfeil und Bogen reichen {m(W_MIN['Pfeil und Bogen'], W_MAX['Pfeil und Bogen'])}. "
             "Man konnte das Tier aus der Ferne töten, war dadurch weniger in Gefahr und konnte besser zielen.",
             ["Entscheidung: Ja, Fortschritt", "Reichweiten verglichen (Lanze bis 3 m, Pfeil und Bogen bis 50 m)", "Begründung: aus der Ferne töten, weniger gefährlich oder besser zielen"],
             3, s), T_WAFFEN),
        L(frei("Erkläre, warum die Menschen der Altsteinzeit nicht sesshaft sein konnten.",
             "Die Nahrung war nicht an einem Ort zu finden. Die Beutetiere wie Rentier und Wildpferd wanderten, und je nach Jahreszeit gab es woanders etwas zum Sammeln. "
             "Deshalb folgten die Gruppen den Tieren und wechselten ihre Lagerplätze. Mit Zelten aus Fell und Stangen konnten sie leicht weiterziehen.",
             ["Beutetiere wandern, Nahrungsangebot wechselt", "Gruppen folgen den Tieren und wechseln die Lagerplätze", "Zelte als Wohnung zum Weiterziehen"],
             3, s), T_NOMADEN),
        L(frei("Nenne vier Teile des Rentiers und sage, wofür man sie nutzte.",
             "Das Fleisch diente als Nahrung. Aus Fell und Haut machte man Kleidung und Zelte. Aus Knochen stellte man Nähnadeln her, aus Geweih zum Beispiel Harpunen. "
             "Aus Sehnen machte man Fäden, und der Magen diente als Behälter.",
             ["erstes Teil mit passender Nutzung", "zweites Teil mit passender Nutzung", "drittes Teil mit passender Nutzung", "viertes Teil mit passender Nutzung"],
             4, s, info="Es zählen alle sechs Teile: Geweih, Fell und Haut, Sehnen, Fleisch, Magen und Knochen."), T_RENTIER),
    ]
    return A


def paket_b():
    p = pack("geschichte-4b-altsteinzeit-jagen-leben", "Geschichte Teil 4b: Jagen, Sammeln und Leben in der Altsteinzeit",
             "Wovon die Menschen der Altsteinzeit lebten: Jagen und Sammeln, Waffen und ihre Reichweiten, das Rentier, Feuer, Leben unterwegs, Handel und Schmuck. Mit Lernblatt und vielen Übungsaufgaben.",
             lernblatt_b(), aufgaben_b(), min_aufgaben=45,
             hinweis="Die Reichweiten der Waffen stammen aus dem Schaubild im Buch (S. 21). Wo „Zusatz“ steht (zum Beispiel bei Sehnen und Magen des Rentiers), ist es Allgemeinwissen und nicht aus dem Heft.")
    assert 45 <= len(p["aufgaben"]) <= 58, len(p["aufgaben"])
    assert 5 <= len(p["lernblatt"]) <= 9
    nachlesen(p, {
        "A – Jagen und Sammeln": T_JAGEN,
        "B – Jagdtechniken": T_TECHNIK,
        "C – Waffen und Reichweiten": T_WAFFEN,
        "D – Das Rentier": T_RENTIER,
        "E – Sammeln, Fischen und Feuer": [T_SAMMELN, T_FEUER],
        "F – Unterwegs leben, Natur und Handel": [T_NOMADEN, T_NATUR, T_HANDEL],
        "G – Klausurnah: Leben in der Altsteinzeit": [T_JAGEN, T_TECHNIK, T_WAFFEN, T_RENTIER, T_FEUER, T_NOMADEN, T_NATUR],
    })
    p["probe"] = False
    return p


def build():
    return [paket_a(), paket_b()]
