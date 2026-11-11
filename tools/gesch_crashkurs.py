"""Geschichte Klasse 6: Crashkurs (Das Wichtigste kurz gefasst) für Joel und Dario.

Der letzte Blick am Tag vor der Arbeit (16.11.2026): kurzes Lernblatt (kein neuer Stoff, nur Auswahl und Verdichtung der
Lernblätter der Übungspakete in eigenen Worten), Tipps, Checkliste und ein Blitz-Check mit neuen Kurzaufgaben.
Anweisung: siehe crashkurs-baustein.md im Projekt. Alle Zahlen und Fakten werden gegen die Lernblätter der anderen Pakete geprüft.
Datenschutz: nur erfundene Personen (Familie Berger aus gesch_lib.PERSONEN).
"""
import difflib
import re

from gesch_lib import (EPOCHEN, PERSONEN, WAFFEN, epoche, jahr, kurz, lb, luecke, mc, nachlesen, pack, reihenfolge,
                       spanne, svg_drei, svg_epochen, tf, zuordnen)

S = "Blitz-Check"
ID = "geschichte-crashkurs"

# Titel der Abschnitte (die Aufgaben benutzen sie als „lesen“)
T_NUTZEN = "So nutzt du den Crashkurs"
T_QUELLE = "Quellen und Darstellungen"
T_STAMM = "Lebenslauf und Stammbaum"
T_ZEIT = "Zeit messen und Zeitrechnung"
T_EPOCHEN = "Epochen und Zeitstrahl"
T_LUCY = "Lucy und der aufrechte Gang"
T_STEIN = "Steinzeit und Altsteinzeit"
T_JUNG = "Jungsteinzeit und die Unterschiede"
T_OETZI = "Ötzi, der Mann aus dem Eis"
T_TIPPS = "Tipps für die Arbeit"
T_CHECK = "Checkliste für morgen"
THEMEN = [T_QUELLE, T_STAMM, T_ZEIT, T_EPOCHEN, T_LUCY, T_STEIN, T_JUNG, T_OETZI]

ALT_EPOCHEN = ("Zeitstrahl mit fünf farbigen Balken nebeneinander, von links nach rechts: Ur- und Frühgeschichte bis 3000 v. Chr., "
               "Altertum 3000 bis 1000 v. Chr., Antike 1000 v. Chr. bis 500 n. Chr., Mittelalter 500 bis 1500 n. Chr. und Neuzeit ab 1500 n. Chr. "
               "Christi Geburt liegt in der Antike.")
ALT_LUCY = ("Drei einfache Strichfiguren von der Seite (nicht maßstabsgetreu), von links nach rechts mit Namen. Schimpanse: stark nach vorn gebeugt, "
            "lange Arme, kurze Beine. Lucy: fast aufrecht, nur leicht nach vorn geneigt. Moderner Mensch: ganz aufrecht, lange Beine, kürzere Arme.")


def lernblatt():
    return [
        lb(T_NUTZEN,
           "Das ist dein **letzter Blick** am Tag vor der Arbeit: einmal in Ruhe lesen (etwa 10 Minuten), danach den **Blitz-Check** machen (etwa 5 Minuten). "
           "Hier steht nichts Neues. Wenn du unsicher bist, geh in das passende Übungspaket zurück. "
           "Wo Heft und Buch etwas verschieden nennen, steht das **Heft zuerst**."),
        lb(T_QUELLE,
           "Eine **Quelle** ist etwas aus der früheren Zeit selbst, aus dem man etwas über diese Zeit erfährt.\n\n"
           "- **Heft**: **Sachquellen** (Werkzeug, Knochen, Bauwerke), **Texte** (Urkunden, Inschriften), **Bilder** (Malereien, Fotos), "
           "**Tonaufnahmen und Filme**, **Zeitzeugen** (erzählen selbst Erlebtes).\n"
           "- **Buch**: **schriftliche**, **bildliche** und **gegenständliche Quellen** (das sind die Sachquellen, auch Münzen), dazu die **mündliche Überlieferung**.\n"
           "- Eine **Darstellung** machen Menschen später über eine Zeit, die sie nicht erlebt haben, zum Beispiel ein Schulbuchtext.\n"
           "- **Historiker**: Frage stellen, Quellen suchen (meist im **Archiv**), Quellen auswerten.",
           merke="Eine Rekonstruktionszeichnung ist eine Darstellung. Die Funde dahinter sind Quellen."),
        lb(T_STAMM,
           "- Ein **Lebenslauf** ist deine eigene Lebensgeschichte, oft als Tabelle. Quellen dafür: Geburtsurkunde, Zeugnisse, Fotos.\n"
           "- Ein **Stammbaum** zeigt Familiengeschichte als Bild. Geschwister stehen nebeneinander, Kinder meist über den Eltern. Dazu stehen Beruf und oft der Geburtsort.\n"
           "- Zeichen: **∞** (oder zwei Ringe ⚭) = verheiratet mit, **∗** = geboren, **†** = gestorben. Nicht verwechseln!\n"
           "- **Von der kleinen zur großen Geschichte**: Familie, **Ortsgeschichte**, **Regionalgeschichte**, **Nationalgeschichte**, **Weltgeschichte**.",
           merke="∗ = geboren, † = gestorben, zwei Ringe = verheiratet."),
        lb(T_ZEIT,
           "- **Warum?** Das Zeitgefühl täuscht. Mit einer **Zeiteinteilung** kannst du dich zeitlich **orientieren**.\n"
           "- **Messen**: Tag und Nacht, **Sonnenuhr**, **Sanduhr**, **mechanische Uhr** (um 1400).\n"
           "- **Kalender**: Monat = 29,5 Tage. **Mondjahr** 354 Tage, **Sonnenjahr** etwa 365 Tage, **Schaltjahr** 366 Tage. "
           "Römer zählen ab 753 v. Chr., Juden ab 3761 v. Chr., Muslime ab 622 n. Chr.\n"
           "- **Unsere Zeitrechnung**: Nullpunkt ist Christi Geburt. Davor **v. Chr.** (größere Zahl = früher), danach **n. Chr.**\n"
           "- **Abstand** (ohne Jahr 0): 100 v. Chr. bis 50 n. Chr. sind 100 + 50 = 150 Jahre.\n"
           "- **Jahrhundert**: letzte zwei Stellen weg, plus 1. 1969 → 19 + 1 = 20. Jahrhundert.",
           merke="Gleiche Seite: abziehen. Über Christi Geburt: zusammenzählen."),
        lb(T_EPOCHEN,
           "Die Geschichte ist lang, darum teilt man sie in **Epochen** ein, vom ältesten zum jüngsten:\n\n"
           "- **Ur- und Frühgeschichte**: bis 3000 v. Chr. (die ganze Steinzeit)\n"
           "- **Altertum**: 3000 bis 1000 v. Chr.\n"
           "- **Antike**: 1000 v. Chr. bis 500 n. Chr.\n"
           "- **Mittelalter** (MA): ca. 500 bis 1500 n. Chr.\n"
           "- **Neuzeit** (NZ): ca. ab 1500 n. Chr.\n\n"
           "Ein **Zeitstrahl** zeigt Ereignisse nacheinander: links ist früher, rechts ist später. Maßstab zum Beispiel 10 Jahre = 1 cm.",
           merke="Altertum und Antike nicht verwechseln: Das Altertum kommt zuerst.",
           bild=svg_epochen(nummern=False, jahre=True, namen_unten=True), bildAlt=ALT_EPOCHEN),
        lb(T_LUCY,
           "- **Lucy** ist das Skelett eines **Australopithecus afarensis** (ein **Vormensch**), gefunden in **Ostafrika**, **über 3 Millionen Jahre** alt "
           "(Buch: 3,18 Millionen Jahre). Afrika heißt **Wiege der Menschheit**.\n"
           "- Lucy sah **wahrscheinlich** eher wie ein **Schimpanse** aus, ging aber **vorwiegend aufrecht** (Knochenbau, Fußspuren). "
           "Der aufrechte Gang begann vor etwa 4 Millionen Jahren.\n"
           "- Auf der Zeichnung: **Schimpanse** gebeugt, lange Arme, kurze Beine. **Lucy** schon überwiegend aufrecht. **Mensch** ganz aufrecht, kürzere Arme.\n"
           "- **Vorteile** des aufrechten Gangs: bessere Sicht, weniger Energie, Hände frei.\n"
           "- **Verfassertext**: 1 Überblick, 2 Untersuchung (Signalwörter), 3 Zusammenfassung.",
           merke="Lucy: wahrscheinlich wie ein Schimpanse, vorwiegend aufrecht wie ein Mensch.",
           bild=svg_drei(("S", "L", "M"), "namen"), bildAlt=ALT_LUCY),
        lb(T_STEIN,
           "- **Steinzeit**: Werkzeuge aus Stein und Holz.\n"
           "- **Heft**: zwei Teile, **Altsteinzeit** (bis ca. 9000 v. Chr.) und **Jungsteinzeit** (ca. 9000 bis 3000 v. Chr.). Das **Buch** nennt zusätzlich die **Mittelsteinzeit**.\n"
           "- **Würm-Eiszeit** (in der Altsteinzeit): letzte Kaltzeit, etwa 100 000 Jahre. Gletscher, Steppe.\n"
           "- **Jagen und Sammeln**: Männer jagten meist, Frauen sammelten.\n"
           "- **Reichweite**: Lanze 0 bis 3 m, Speer 0 bis 15 m, Speerschleuder 8 bis 30 m, Pfeil und Bogen 5 bis 50 m.\n"
           "- **Feuer**: nutzen seit etwa 1,5 Millionen Jahren, selbst erzeugen erst seit etwa 150 000 bis 100 000 Jahren.\n"
           "- **Nicht sesshaft**: **Nomaden** in Gruppen von etwa 25 bis 30 Personen, Zelte.",
           merke="Heft: zwei Teile. Buch: drei Teile."),
        lb(T_JUNG,
           "- Um **9000 v. Chr.** wurden Menschen **sesshaft**: **Ackerbau**, **Viehzucht**, **Vorratshaltung**. "
           "Das ist die **neolithische Revolution**: ein grundlegender Wandel, kein Aufstand. Start im Irak, an Euphrat und Tigris.\n"
           "- **Erfindungen**: Pflug (Mitteleuropa seit 4500 v. Chr.), Keramik, Webstuhl, Mahlstein, geschliffene Beile, Rad (um 3000 v. Chr.).\n"
           "- **Folgen**: Dörfer, Berufe, Vorräte (unabhängiger von der Umwelt). Aber auch Hungersnöte bei Ernteausfall und Neid und Streit um Besitz.\n"
           "- **Alt gegen Jung**: Nomaden gegen sesshafte Bauern, Zelt gegen Haus im Dorf, Jagen und Sammeln gegen Ackerbau und Viehzucht.",
           merke="Aus Jägern und Sammlern werden sesshafte Bauern."),
        lb(T_OETZI,
           "- **Fund**: Herbst **1991**, **Ötztaler Alpen**, über 3000 m hoch (Buch: 3210 m). Die **Mumie** im Gletscher ist über 5000 Jahre alt (Buch: rund 5250).\n"
           "- **Person**: Mitte 40 (Buch: 46 Jahre), 1,60 m, blaue Augen, über 50 Tätowierungen. Er lebte zwischen **3359 und 3105 v. Chr.**, am Ende der Jungsteinzeit (**Kupfersteinzeit**).\n"
           "- **Ausrüstung**: Fellkleidung, Bogen, Steindolch, aber auch ein **Kupferbeil**: „**Wanderer zwischen den Zeiten**“.\n"
           "- **Tod**: Pfeilspitze in der linken Schulter, verblutet. Schnittwunde an der rechten Hand (Nahkampf). Wer es war, weiß man nicht.\n"
           "- **Woher man das weiß**: Pollen, Mikroskop, Computertomografie. Der Text des Arztes ist eine **Darstellung**.",
           merke="Ötzi: Mumie aus der Kupfersteinzeit, getötet durch einen Pfeil."),
        lb(T_TIPPS,
           "- Lies jede Aufgabe **zweimal** und teile deine Zeit ein.\n"
           "- Bei 2 oder 3 Punkten wollen die Lehrer meist 2 oder 3 Gedanken sehen.\n"
           "- „Nenne“ = kurz aufzählen. „Erkläre“ und „begründe“ = mit **weil**. „Vergleiche“ = beide Seiten nennen.\n"
           "- Bei Jahren immer **v. Chr.** oder **n. Chr.** dazuschreiben.\n"
           "- Zur Steinzeit zuerst die Heft-Antwort schreiben (zwei Teile)."),
        lb(T_CHECK,
           "**Ich kann:**\n\n"
           "- Quellen nennen und Quelle und Darstellung unterscheiden.\n"
           "- einen Stammbaum lesen und die Zeichen ∞, ∗ und † erklären.\n"
           "- erklären, wozu man die Zeit einteilt, und Jahre und Jahrhunderte berechnen.\n"
           "- die fünf Epochen nennen und auf einem Zeitstrahl einzeichnen.\n"
           "- Lucy mit Schimpanse und Mensch vergleichen.\n"
           "- die Steinzeit unterteilen und die Altsteinzeit beschreiben.\n"
           "- die Jungsteinzeit erklären und mit der Altsteinzeit vergleichen.\n"
           "- sagen, wer Ötzi war und was man über ihn weiß."),
    ]


# ------------------------------------------------------------------ Hilfen für die Antworten

def zahl_antw(n, einheit="Jahre"):
    """Zahl mit und ohne Einheit (bei großen Zahlen auch mit Tausenderpunkt)."""
    out = [str(n), f"{n} {einheit}"]
    if n >= 1000:
        p = f"{n:,}".replace(",", ".")
        out += [p, f"{p} {einheit}"]
    return out


def jh(y):
    """Jahrhundert eines Jahres n. Chr. (Schulregel: Zahl ohne die letzten zwei Stellen plus 1; volle Hunderter vermeiden)."""
    assert y > 0 and y % 100 != 0, y
    return y // 100 + 1


def jh_antw(n):
    return [str(n), f"{n}.", f"{n}. Jahrhundert", f"das {n}. Jahrhundert", f"im {n}. Jahrhundert", f"{n}. Jahrhundert n. Chr.", f"{n}. Jh.", f"{n}. Jh"]


def zeitraum(i):
    """Epoche i als Text, aus EPOCHEN berechnet: '1000 v. Chr. bis 500 n. Chr.'"""
    n, a, b = EPOCHEN[i]
    if a is None:
        return f"bis {jahr(b)}"
    if b is None:
        return f"ab {jahr(a)}"
    if (a < 0) == (b < 0):   # beide Jahre auf derselben Seite: Zusatz nur einmal
        return f"{abs(a)} bis {jahr(b)}"
    return f"{jahr(a)} bis {jahr(b)}"


def aufgaben():
    """Die Blitz-Check-Aufgaben. Rückgabe: (Aufgaben, Belege). Belege: je Aufgabe Zeichenfolgen, die im Crashkurs-Abschnitt stehen müssen."""
    A, B = [], []

    def neu(t, lesen, belege):
        t["lesen"] = lesen
        A.append(t)
        B.append((t["frage"][:50], lesen if isinstance(lesen, list) else [lesen], belege))

    # 1 Quellengruppen (Heft)
    neu(zuordnen("Ordne jedes Fundstück der richtigen Quellengruppe aus dem Heft zu.",
                 [("Inschrift auf einem Grabstein", "Texte"),
                  ("Mauerreste einer Burg", "Sachquellen"),
                  ("Gemälde eines Fürsten", "Bilder"),
                  ("Filmaufnahme aus dem Jahr 1950", "Tonaufnahmen und Filme"),
                  ("Mann, der erzählt, wie er als Kind eine Flut erlebt hat", "Zeitzeugen")], S,
                 extra=["Darstellungen"],
                 info="Das Heft kennt fünf Gruppen. Zu den Sachquellen zählen auch Bauwerke, zu den Texten auch Inschriften, zu den Bildern auch Malereien."),
        T_QUELLE, ["Sachquellen (Werkzeug, Knochen, Bauwerke)", "Texte (Urkunden, Inschriften)", "Bilder (Malereien, Fotos)", "Tonaufnahmen und Filme", "Zeitzeugen (erzählen selbst Erlebtes)"])

    # 2 Quelle oder Darstellung (Museum)
    neu(mc("Ein Museum zeigt ein Steinbeil aus der Jungsteinzeit und daneben ein neues Wandbild, das ein Maler heute nach Funden gemalt hat. Was stimmt?",
           "Das Beil ist eine Quelle, das Wandbild eine Darstellung.",
           ["Das Beil ist eine Darstellung, das Wandbild eine Quelle.", "Beide sind Quellen, weil sie im Museum stehen.", "Beide sind Darstellungen, weil man sie ansehen kann."], S,
           info="Das Beil stammt aus der Zeit selbst. Das Wandbild haben Menschen viel später gemalt, die die Zeit nicht erlebt haben, und zwar mithilfe von Funden."),
        T_QUELLE, ["Quelle ist etwas aus der früheren Zeit selbst", "Darstellung machen Menschen später", "die sie nicht erlebt haben"])

    # 3 Stammbaum: Zeichen lesen
    k = PERSONEN["Karl"]
    assert (k["geb"], k["tod"]) == (1952, 2019), k
    neu(tf(f"Im Stammbaum der Familie Berger steht bei Karl „∗ {k['geb']} † {k['tod']}“. Das † zeigt, dass Karl {k['tod']} geheiratet hat.", False, S,
           info=f"Das † heißt gestorben, das ∗ geboren: Karl wurde {k['geb']} geboren und starb {k['tod']}. Verheiratet zeigen zwei Ringe (oder ∞)."),
        T_STAMM, ["∞ (oder zwei Ringe ⚭) = verheiratet mit", "∗ = geboren", "† = gestorben"])

    # 4 Abstand über Christi Geburt hinweg
    a, b = -80, 120
    d = spanne(a, b)
    assert d == 200 == abs(a) + b
    neu(kurz(f"Eine römische Münze stammt aus dem Jahr {jahr(a)}, eine andere aus dem Jahr {jahr(b)}. Wie viele Jahre liegen zwischen den beiden Münzen? "
             "Rechne wie in der Schule (ohne Jahr 0).", zahl_antw(d), S, einheit="Jahre",
             info=f"Ein Jahr liegt vor und eins nach Christi Geburt, also zählst du zusammen: {abs(a)} + {b} = {d} Jahre."),
        T_ZEIT, ["über Christi Geburt: zusammenzählen", "100 + 50 = 150 Jahre"])

    # 5 Jahrhundert
    y = 1348
    j = jh(y)
    assert j == 14 and str(y)[:2] == "13"
    neu(kurz(f"Ein Brief wurde im Jahr {y} n. Chr. geschrieben. In welchem Jahrhundert war das? Schreibe die Zahl.", jh_antw(j), S,
             info=f"Letzte zwei Stellen weg, plus 1: {y} → {str(y)[:2]} + 1 = {j}. Jahrhundert."),
        T_ZEIT, ["letzte zwei Stellen weg, plus 1", "1969 → 19 + 1 = 20. Jahrhundert"])

    # 6 Epochen rückwärts
    namen = [e[0] for e in EPOCHEN]
    assert namen == ["Ur- und Frühgeschichte", "Altertum", "Antike", "Mittelalter", "Neuzeit"], namen
    rueck = list(reversed(namen))
    neu(reihenfolge("Ordne die Epochen von heute aus rückwärts. Die jüngste Epoche steht zuerst.", rueck, S,
                    info="Von heute aus rückwärts: " + ", ".join(f"{n} ({zeitraum(len(namen) - 1 - i)})" for i, n in enumerate(rueck)) + "."),
        T_EPOCHEN, ["Ur- und Frühgeschichte: bis 3000 v. Chr.", "Altertum: 3000 bis 1000 v. Chr.", "Antike: 1000 v. Chr. bis 500 n. Chr.",
                    "Mittelalter (MA): ca. 500 bis 1500 n. Chr.", "Neuzeit (NZ): ca. ab 1500 n. Chr."])

    # 7 Lucy und der aufrechte Gang: was war zuerst?
    lucy, gang = 3.18, 4.0   # Millionen Jahre (Buch: 3,18; Heft: aufrechter Gang vor ca. 4 Mio.)
    assert lucy < gang
    neu(tf("Der aufrechte Gang begann erst mit Lucy.", False, S,
           info="Der aufrechte Gang begann schon vor etwa 4 Millionen Jahren. Lucy lebte später: Sie ist über 3 Millionen Jahre alt (3,18 Millionen laut Buch)."),
        T_LUCY, ["über 3 Millionen Jahre alt (Buch: 3,18 Millionen Jahre)", "Der aufrechte Gang begann vor etwa 4 Millionen Jahren"])

    # 8 Waffen und Reichweiten: Tier in 40 m Entfernung
    ziel = 40
    treffer = [n for n, von, bis in WAFFEN if von <= ziel <= bis]
    assert treffer == ["Pfeil und Bogen"], treffer
    reich = {n: f"{von} bis {bis} m" for n, von, bis in WAFFEN}
    assert reich == {"Lanze": "0 bis 3 m", "Speer": "0 bis 15 m", "Speerschleuder": "8 bis 30 m", "Pfeil und Bogen": "5 bis 50 m"}, reich
    neu(mc(f"Ein Tier steht {ziel} m entfernt. Welche Jagdwaffe der Altsteinzeit reicht noch bis dorthin?",
           "Pfeil und Bogen", ["Speerschleuder", "Speer", "Lanze"], S,
           info=f"Pfeil und Bogen reichen {reich['Pfeil und Bogen']}. Die Speerschleuder ({reich['Speerschleuder']}), der Speer ({reich['Speer']}) und die Lanze ({reich['Lanze']}) sind zu kurz."),
        T_STEIN, ["Lanze 0 bis 3 m, Speer 0 bis 15 m, Speerschleuder 8 bis 30 m, Pfeil und Bogen 5 bis 50 m"])

    # 9 Steinzeit unterteilen und neolithische Revolution (Lückentext)
    neu(luecke("Ergänze den Text über die Steinzeit.",
               "Nach dem Heft hat die Steinzeit {{zwei}} Teile: Altsteinzeit und Jungsteinzeit. Das Buch nennt zusätzlich die {{Mittelsteinzeit}}. "
               "Um {{9000}} v. Chr. begannen Menschen, {{sesshaft}} zu werden. Diesen Wandel nennt man neolithische {{Revolution}}.",
               S, extra=["drei", "3000", "Eiszeit"],
               info="Das Heft zählt zwei Teile, das Buch drei. Um 9000 v. Chr. begann die Jungsteinzeit: Die Menschen wurden sesshaft, ein grundlegender Wandel."),
        [T_STEIN, T_JUNG], ["Heft: zwei Teile", "Das Buch nennt zusätzlich die Mittelsteinzeit", "Um 9000 v. Chr. wurden Menschen sesshaft", "neolithische Revolution"])

    # 10 Altsteinzeit oder Jungsteinzeit
    neu(zuordnen("Ordne jedes Stichwort dem richtigen Abschnitt der Steinzeit zu.",
                 [("Leben in der Würm-Eiszeit", "Altsteinzeit"),
                  ("Gruppen von etwa 25 bis 30 Personen", "Altsteinzeit"),
                  ("Webstuhl", "Jungsteinzeit"),
                  ("Hungersnöte bei Ernteausfall", "Jungsteinzeit"),
                  ("Neid und Streit um Besitz", "Jungsteinzeit")], S,
                 info="Würm-Eiszeit und kleine Gruppen von Nomaden gehören zur Altsteinzeit. Webstuhl, Hungersnöte und Streit um Besitz gehören zu den sesshaften Bauern der Jungsteinzeit."),
        [T_STEIN, T_JUNG], ["Würm-Eiszeit (in der Altsteinzeit)", "Nomaden in Gruppen von etwa 25 bis 30 Personen", "Webstuhl", "Hungersnöte bei Ernteausfall", "Neid und Streit um Besitz"])

    # 11 Ötzi: wann innerhalb der Steinzeit?
    oe_von, oe_bis = -3359, -3105
    jung_von, jung_bis = -9000, -3000
    assert jung_von < oe_von < oe_bis < jung_bis, "Ötzi liegt in der Jungsteinzeit"
    assert spanne(oe_bis, jung_bis) == 105 < spanne(oe_von, jung_von), "und zwar ganz am Ende"
    assert epoche(oe_von) == epoche(oe_bis) == "Ur- und Frühgeschichte"
    neu(mc(f"Ötzi lebte zwischen {abs(oe_von)} und {jahr(oe_bis)}. Wann war das nach den Jahreszahlen im Heft?",
           "Am Ende der Jungsteinzeit.",
           ["Am Anfang der Jungsteinzeit.", "Am Ende der Altsteinzeit.", "Im Altertum, schon nach der Steinzeit."], S,
           info=f"Die Jungsteinzeit dauerte nach dem Heft von {abs(jung_von)} bis {jahr(jung_bis)}. Ötzis Zeit liegt kurz davor, das Altertum begann erst danach."),
        [T_OETZI, T_STEIN], ["zwischen 3359 und 3105 v. Chr.", "am Ende der Jungsteinzeit", "Jungsteinzeit (ca. 9000 bis 3000 v. Chr.)"])
    return A, B


# ------------------------------------------------------------------ Abgleich mit den Lernblättern der Übungspakete

# Fakten des Crashkurs-Lernblatts. Jede Zeichenfolge muss im Crashkurs stehen UND im Lernblatt mindestens eines Übungspakets (Groß-/Kleinschreibung egal, ** ignoriert).
FAKTEN = [
    # Quellen
    "Sachquellen", "Tonaufnahmen und Filme", "Zeitzeugen", "Bauwerke", "Urkunden", "Inschriften", "Malereien", "Fotos", "schriftliche", "bildliche", "gegenständliche Quellen",
    "Münzen", "mündliche Überlieferung", "Rekonstruktionszeichnung ist eine Darstellung", "Schulbuchtext", "Historiker", "Archiv", "Frage stellen", "Quellen suchen", "Quellen auswerten",
    # Lebenslauf, Stammbaum
    "Lebenslauf", "Tabelle", "Geburtsurkunde", "Zeugnisse", "Geschwister stehen nebeneinander", "Geburtsort", "zwei Ringe ⚭", "verheiratet mit", "∗", "†", "geboren", "gestorben",
    "Ortsgeschichte", "Regionalgeschichte", "Nationalgeschichte", "Weltgeschichte",
    # Zeit
    "Zeiteinteilung", "orientieren", "Sonnenuhr", "Sanduhr", "mechanische Uhr", "um 1400", "29,5 Tage", "Mondjahr", "354 Tage", "Sonnenjahr", "etwa 365 Tage", "Schaltjahr", "366 Tage",
    "753 v. Chr.", "3761 v. Chr.", "622 n. Chr.", "Nullpunkt", "Christi Geburt", "größere Zahl = früher", "Jahr 0", "100 + 50 = 150 Jahre", "plus 1", "1969 → 19 + 1 = 20. Jahrhundert",
    "Gleiche Seite: abziehen", "zusammenzählen",
    # Epochen, Zeitstrahl
    "Ur- und Frühgeschichte", "bis 3000 v. Chr.", "Altertum", "3000 bis 1000 v. Chr.", "Antike", "1000 v. Chr. bis 500 n. Chr.", "Mittelalter", "500 bis 1500 n. Chr.", "Neuzeit", "ab 1500 n. Chr.",
    "MA", "NZ", "ganze Steinzeit", "Zeitstrahl", "links ist früher, rechts ist später", "10 Jahre = 1 cm",
    # Lucy
    "Australopithecus afarensis", "Vormensch", "Ostafrika", "über 3 Millionen Jahre", "3,18 Millionen Jahre", "Wiege der Menschheit", "wahrscheinlich", "vorwiegend aufrecht", "Knochenbau", "Fußspuren",
    "4 Millionen Jahren", "lange Arme", "kurze Beine", "bessere Sicht", "weniger Energie", "Hände frei", "Verfassertext", "Überblick", "Untersuchung", "Zusammenfassung", "Signalwörter",
    # Steinzeit, Altsteinzeit
    "Werkzeuge", "Holz", "zwei Teile", "Altsteinzeit", "9000 v. Chr.", "Jungsteinzeit", "9000 bis 3000 v. Chr.", "Mittelsteinzeit", "Würm-Eiszeit", "100 000 Jahre", "Gletscher", "Steppe",
    "Jagen und Sammeln", "Männer", "Frauen", "0 bis 3 m", "0 bis 15 m", "8 bis 30 m", "5 bis 50 m", "1,5 Millionen Jahren", "150 000 bis 100 000 Jahren", "Nomaden", "25 bis 30 Personen", "Zelte",
    # Jungsteinzeit
    "sesshaft", "Ackerbau", "Viehzucht", "Vorratshaltung", "neolithische Revolution", "grundlegender Wandel", "Aufstand", "Irak", "Euphrat", "Tigris", "Pflug", "4500 v. Chr.", "Keramik", "Webstuhl",
    "Mahlstein", "geschliffene Beile", "Rad", "um 3000 v. Chr.", "Dörfer", "Berufe", "Vorräte", "unabhängiger von der Umwelt", "Hungersnöte", "Ernteausfall", "Neid und Streit", "Besitz",
    "sesshafte Bauern", "haus im dorf",
    # Ötzi
    "1991", "Ötztaler Alpen", "über 3000 m", "3210 m", "Mumie", "über 5000 Jahre", "5250", "Mitte 40", "46 Jahre", "1,60 m", "blaue Augen", "über 50 Tätowierungen",
    "3359 und 3105 v. Chr.", "Kupfersteinzeit", "am Ende der Jungsteinzeit", "Fellkleidung", "Steindolch", "Kupferbeil", "Wanderer zwischen den Zeiten", "Pfeilspitze", "linken Schulter",
    "verblutet", "rechten Hand", "Nahkampf", "Pollen", "Mikroskop", "Computertomografie",
    # Tipps
    "beide Seiten", "Vergleiche",
]
# Fachwörter (fett gedruckt), die der Crashkurs selbst einführt und die nicht im Lernblatt der Übungspakete stehen müssen
EIGENE_FETT = {"Ich kann", "letzter Blick", "Blitz-Check", "Heft zuerst", "Heft", "Buch", "zweimal", "weil", "v. Chr.", "n. Chr.", "Warum?", "Messen", "Kalender", "Abstand",
               "Fund", "Person", "Ausrüstung", "Tod", "Woher man das weiß", "Reichweite", "Feuer", "Erfindungen", "Folgen", "Alt gegen Jung", "Vorteile",
               "Unsere Zeitrechnung", "Jahrhundert", "Steinzeit"}


def woerter(text):
    """Wörter wie im Vorbild (ohne **, Zeichen wie = und + zählen nicht mit)."""
    return len(re.findall(r"[\wÄÖÜäöüß%−–„“-]+", re.sub(r"\*\*", "", text)))


def woerter_split(text):
    """Strenge Zählung: alles, was durch Leerzeichen getrennt ist (so zählt auch der Selbsttest)."""
    return len(re.sub(r"\*\*", "", text).split())


def norm(s):
    return re.sub(r"\s+", " ", s.replace("**", "")).lower()


ZAHL = re.compile(r"\d+(?:[  ]\d{3})*(?:,\d+)?")


def zahlen(text):
    """Alle Zahlen eines Textes (mit Tausenderleerzeichen und Komma), einstellige ohne Komma bleiben außen vor."""
    out = set()
    for m in ZAHL.finditer(text):
        z = m.group().replace(" ", " ")
        if len(z) >= 2:
            out.add(z)
    return out


def pruefe_lernblatt(LB):
    titel = [s["titel"] for s in LB]
    assert len(set(titel)) == len(titel), titel
    assert titel[0] == T_NUTZEN and titel[-2:] == [T_TIPPS, T_CHECK] and titel[1:-2] == THEMEN, titel
    for s in LB:
        assert "#" not in s["text"] and "|---" not in s["text"], s["titel"]
        assert not re.search(r"(?<![*\w])\*(?![*])", s["text"].replace("∗", "")), f"Kursivschrift? {s['titel']}"
    # Länge: Themenabschnitte 60 bis 120 Wörter (Text allein mindestens 60, Text mit merke höchstens 120, nach beiden Zählweisen)
    je = []
    for s in LB:
        if s["titel"] in THEMEN:
            m = s.get("merke") or ""
            assert m, f"merke fehlt: {s['titel']}"
            lo = min(woerter(s["text"]), woerter_split(s["text"]))
            hi = max(woerter(s["text"] + " " + m), woerter_split(s["text"] + " " + m))
            assert 60 <= lo and hi <= 120, (s["titel"], lo, hi)
            je.append((s["titel"], woerter_split(s["text"]), woerter_split(s["text"] + " " + m)))
    text_summe = sum(woerter_split(s["text"]) for s in LB)
    gesamt = sum(woerter(s["titel"] + " " + s["text"] + " " + (s.get("merke") or "")) for s in LB)
    assert 800 <= text_summe <= 1000, text_summe
    assert gesamt <= 1000, gesamt
    return je, text_summe, gesamt


def pruefe_fakten(LB, pakete):
    crash = norm("\n".join(s["text"] + "\n" + (s.get("merke") or "") for s in LB))
    quelle = norm("\n".join(s["titel"] + "\n" + s["text"] + "\n" + (s.get("merke") or "") for p in pakete for s in p.get("lernblatt", []) if p["id"] != ID))
    nur_crash = [f for f in FAKTEN if norm(f) not in crash]
    assert not nur_crash, f"Fakten stehen nicht im Crashkurs: {nur_crash}"
    fehlen = [f for f in FAKTEN if norm(f) not in quelle]
    assert not fehlen, f"Fakten nicht im Lernblatt der Übungspakete: {fehlen}"
    # jede Zahl des Crashkurs-Lernblatts (außer im Einleitungstext) steht auch in den Übungspaketen
    zq = zahlen(quelle)
    for s in LB[1:]:
        neu_ = sorted(z for z in zahlen(s["text"] + " " + (s.get("merke") or "")) if z not in zq)
        assert not neu_, f"Zahlen nicht in den Übungspaketen ({s['titel']}): {neu_}"
    # jedes fette Fachwort steht auch in den Übungspaketen (außer den eigenen Ankerwörtern)
    for s in LB:
        for fett in re.findall(r"\*\*(.+?)\*\*", s["text"]):
            f = fett.strip().rstrip(":")
            if f in EIGENE_FETT:
                continue
            assert norm(f) in quelle, f"Fachwort nicht in den Übungspaketen: {f} ({s['titel']})"


def pruefe_aufgaben(LB, A, B, pakete):
    assert 8 <= len(A) <= 12, len(A)
    assert not any(t["typ"] == "frei" for t in A)
    assert all(t["abschnitt"] == S for t in A)
    titel = {s["titel"]: norm(s["text"] + "\n" + (s.get("merke") or "")) for s in LB}
    arten = {}
    for t in A:
        arten[t["typ"]] = arten.get(t["typ"], 0) + 1
        for x in (t["lesen"] if isinstance(t["lesen"], list) else [t["lesen"]]):
            assert x in titel and x in THEMEN, f"lesen: Abschnitt „{x}“ gibt es nicht im Crashkurs"
        ohne = re.sub(r"(\d)\.", r"\1", re.sub(r"\b[vn]\. Chr\.", "Chr", t["info"]))
        assert 1 <= len(re.findall(r"[.!?](?:\s|$)", ohne)) <= 2, ("info soll 1 bis 2 Sätze haben", t["info"])
        if t["typ"] == "kurz":
            r = t["richtig"] if isinstance(t["richtig"], list) else [t["richtig"]]
            assert all(x.strip() for x in r)
        if t["typ"] == "mc":
            r = t["richtig"] if isinstance(t["richtig"], list) else [t["richtig"]]
            falsch = [a for i, a in enumerate(t["antworten"]) if i not in r]
            assert max(len(t["antworten"][i]) for i in r) <= 1.4 * max(len(a) for a in falsch), ("richtige Antwort auffällig lang", t["antworten"])
            assert len(set(t["antworten"])) == len(t["antworten"])
            assert not any(("alle" in a.lower() or "keine" in a.lower()) and "antwort" in a.lower() for a in t["antworten"])
    # die Antwort steht wirklich im Abschnitt, auf den die Aufgabe verweist
    for frage, lesen, belege in B:
        text = " ".join(titel[x] for x in lesen)
        for b in belege:
            assert norm(b) in text, f"Beleg „{b}“ fehlt in {lesen} (Aufgabe: {frage})"
    # Luecken: Wortbank mit 1 bis 3 Extra-Wörtern, Lücken nicht vertauschbar
    for t in A:
        if t["typ"] == "luecke":
            erste = [g.split("|")[0].strip() for g in re.findall(r"\{\{([\s\S]*?)\}\}", t["text"])]
            extra = [w for w in t["wortbank"] if w not in erste]
            assert 1 <= len(extra) <= 3, extra
            assert len(set(erste)) == len(erste), erste
    # neu: nicht aus den Übungspaketen übernommen (identisch oder fast gleich)
    if pakete is not None:
        alt = [(p["id"], t["frage"], t.get("text", "")) for p in pakete if p["id"] != ID for t in p["aufgaben"]]
        keys = {f"{f}|{x}" for _, f, x in alt}
        for t in A:
            assert f"{t['frage']}|{t.get('text', '')}" not in keys, f"Aufgabe schon vorhanden: {t['frage']}"
            for pid, f, x in alt:
                r = difflib.SequenceMatcher(None, t["frage"] + " " + t.get("text", ""), f + " " + x).ratio()
                assert r < 0.8, f"zu ähnlich ({r:.2f}) zu {pid}: {f}\n   neu: {t['frage']}"
    return arten


def build(pakete=None):
    LB = lernblatt()
    A, B = aufgaben()
    je, text_summe, gesamt = pruefe_lernblatt(LB)
    if pakete is not None:
        pruefe_fakten(LB, pakete)
    arten = pruefe_aufgaben(LB, A, B, pakete)
    anzahl = {10: "zehn", 11: "elf", 12: "zwölf", 9: "neun", 8: "acht"}.get(len(A), str(len(A)))
    p = pack(ID, "Geschichte Klasse 6: Crashkurs (das Wichtigste kurz gefasst)",
             f"Das Wichtigste kurz gefasst, für den letzten Blick vor der Arbeit: Lernblatt, Checkliste und ein Blitz-Check mit {anzahl} Kurzaufgaben.",
             LB, A,
             hinweis="Kein neuer Stoff: Alles steht auch in den Lernblättern der Übungspakete. Wo Heft und Buch verschieden sind (Quellengruppen, zwei oder drei Teile der Steinzeit, "
                     "Zahlen zu Ötzi), steht das Heft zuerst.")
    nachlesen(p, {S: [x for x in THEMEN if any(x in (b[1]) for b in B)]})
    p["probe"] = False
    print(f"Crashkurs: {len(LB)} Abschnitte, {text_summe} Wörter Text ({gesamt} mit Titeln und merke), {len(A)} Blitz-Check-Aufgaben {arten}")
    for titel, w, wm in je:
        print(f"   {w:4d} ({wm:4d} mit merke)  {titel}")
    return p


if __name__ == "__main__":
    build()
