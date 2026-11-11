"""Geschichte Klasse 6, Teil 3: Vom Affen zum Menschen (Lucy), Lernzettel Punkt 5 (Heft, Buch S. 28, Infoblatt S. 29).

Der Beispieltext über Lucy ist selbst formuliert (nach den Fakten aus dem Unterricht), nicht aus dem Buch abgeschrieben.
Merkmale von Schimpanse, Lucy und Mensch, die nicht im Faktenblatt stehen, werden nur als Zusatzwissen und vorsichtig benutzt.
"""
from gesch_lib import *
from gesch_lib import _svg, _label, _num, _arrow, svg_drei

NAMEN = {"S": "Schimpanse", "L": "Lucy", "M": "moderner Mensch"}
HALTUNG = {
    "S": "stark nach vorn gebeugt, mit langen Armen und kurzen Beinen",
    "L": "fast aufrecht, nur leicht nach vorn geneigt",
    "M": "ganz aufrecht, mit langen Beinen und kürzeren Armen",
}

# Prüfwerte (Fakten aus dem Faktenblatt, Abschnitt 4)
LUCY_ALTER_HEFT = 3_000_000      # „über 3 Millionen Jahre“
LUCY_ALTER_BUCH = 3_180_000      # 3,18 Millionen
GANG_BEGINN = 4_000_000          # vor ca. 4 Mio. Jahren
assert LUCY_ALTER_BUCH > LUCY_ALTER_HEFT and GANG_BEGINN > LUCY_ALTER_BUCH
FUND_LUCY, FUND_SPUREN = 1974, 1978
assert FUND_LUCY < FUND_SPUREN


def buchst(reihe, k):
    """Buchstabe (A, B, C) der Figur k in der angegebenen Reihenfolge von svg_drei."""
    return "ABC"[reihe.index(k)]


def alt_drei(reihe, beschr="buchstaben"):
    """Bildbeschreibung zu svg_drei: nennt nur die Haltung, bei „namen“ auch die Namen."""
    teile = []
    for i, k in enumerate(reihe):
        if beschr == "namen":
            teile.append(f"{NAMEN[k]}: {HALTUNG[k]}")
        else:
            teile.append(f"Figur {'ABC'[i]}: {HALTUNG[k]}")
    kopf = "Drei einfache Strichfiguren von der Seite (nicht maßstabsgetreu), von links nach rechts"
    return kopf + (" mit Namen. " if beschr == "namen" else " mit den Buchstaben A, B und C. ") + "; ".join(teile) + "."


# ------------------------------------------------------------------ Beispieltext (selbst formuliert)

BEISPIEL = ("Lucy lebte vor mehr als drei Millionen Jahren in Ostafrika. 1974 fanden Forscher ihr Skelett. "
            "Weil etwa 40 Prozent der Knochen erhalten waren, weiß man heute viel über sie. "
            "Sie sah wahrscheinlich eher wie ein Schimpanse aus. Trotzdem ging sie vorwiegend aufrecht. "
            "Das erkennt man an ihrem Knochenbau. "
            "Später fand man in Tansania auch Fußspuren eines Vormenschen, die zu einem aufrechten Gang passen. "
            "Da der aufrechte Gang die Hände frei machte, konnten die Vormenschen Nahrung tragen. "
            "Deshalb war er ein wichtiger Schritt auf dem Weg zum Menschen.")

# Zweiter, kurzer Sachtext nur für die Klausuraufgaben 42 bis 44 (nicht im Lernblatt ausgewertet). Nur Fakten aus dem Faktenblatt, Abschnitt 4.
BEISPIEL2 = ("Vor etwa vier Millionen Jahren begannen menschenähnliche Lebewesen in Afrika, aufrecht zu gehen. "
             "Wer aufrecht geht, sieht Nahrung und Gefahren früher und braucht weniger Energie auf langen Wegen. "
             "Weil seine Hände frei sind, kann er außerdem Gegenstände tragen. "
             "Danach lebte Lucy in Ostafrika. Sie sah wahrscheinlich eher wie ein Schimpanse aus. "
             "Obwohl sie so aussah, ging sie vorwiegend aufrecht. "
             "1978 fand man in Laetoli in Tansania Fußabdrücke eines Vormenschen, die dazu passen. "
             "Deshalb gilt der aufrechte Gang als wichtiger Schritt zum Menschen.")
assert BEISPIEL2 != BEISPIEL and BEISPIEL2[:40] != BEISPIEL[:40]


def ost_formen():
    """Schreibweisen für den Fundort: Ostafrika (Heft) oder Äthiopien/Hadar (Buch), mit und ohne „in“."""
    ost = ["Ostafrika", "Ost-Afrika", "Ost Afrika", "östliches Afrika", "Ostteil Afrikas"]
    res = list(ost) + [f"in {o}" for o in ost] + ["im Osten Afrikas", "im Osten von Afrika", "im östlichen Afrika", "Osten Afrikas", "Osten von Afrika"]
    res += ["Äthiopien", "in Äthiopien", "Hadar", "in Hadar", "Hadar in Äthiopien", "Hadar (Äthiopien)", "Ostafrika (Äthiopien)", "Ostafrika, Äthiopien"]
    return list(dict.fromkeys(res))


def mio_formen(zahl, wort):
    """Schreibweisen für „vor n Millionen Jahren“: 4, vier, 4 Mio., 4 Millionen Jahre, vor etwa 4 Millionen Jahren ... (wird klein verglichen)."""
    kern = []
    for z in (zahl, wort):
        kern += [f"{z} Millionen", f"{z} Mio", f"{z} Mio."]
    res = [zahl, wort]
    for k in kern:
        res += [k, f"{k} Jahre", f"{k} Jahren"]
        for vorn in ("vor", "etwa", "ca.", "vor etwa", "vor ca."):
            res += [f"{vorn} {k}", f"{vorn} {k} Jahren"]
    return list(dict.fromkeys(res))


# Titel der Lernblatt-Abschnitte (für die Verweise)
L_AFRIKA, L_FUND, L_AUSSEHEN, L_GANG = "Afrika: Wiege der Menschheit", "Lucy: der Fund", "Wie sah Lucy aus?", "Der aufrechte Gang und seine Folgen"
L_VERGLEICH, L_METHODE, L_SPRACHE, L_TEXT = ("Schimpanse, Lucy und Mensch im Vergleich", "Verfassertext auswerten: drei Schritte",
                                             "Sprache im Text: Signalwörter", "Beispieltext: Lucy")


# ------------------------------------------------------------------ Lernblatt

def lernblatt():
    return [
        lb(L_AFRIKA,
           "Die ersten menschenähnlichen Lebewesen lebten in Afrika. Die ältesten Skelettfunde von ihnen stammen von dort. Darum nennt man Afrika auch die **Wiege der Menschheit**.\n"
           "Vor etwa **4 Millionen Jahren** fingen diese Lebewesen an, **aufrecht zu gehen**. Das war ein wichtiger Schritt auf dem Weg zum Menschen.",
           merke="Der Mensch stammt aus Afrika. Der aufrechte Gang begann vor etwa 4 Millionen Jahren."),
        lb(L_FUND,
           "**Lucy** ist der Name eines Skeletts. Es gehört zu einem **Australopithecus afarensis**. Das ist ein **Vormensch**, der Name bedeutet etwa „Südaffe“. Das weißt du über den Fund:\n"
           "- Fundort: **Ostafrika**. Das Buch nennt Hadar in Äthiopien und das Jahr 1974.\n"
           "- Gefunden hat es eine amerikanisch-französische Forschergruppe.\n"
           "- Erhalten sind etwa **40 Prozent** der Knochen. Lucy ist eines der ältesten und am besten erhaltenen menschenartigen Wesen.\n"
           "- Alter: **über 3 Millionen Jahre**. Das Buch nennt genauer 3,18 Millionen Jahre.\n"
           "- Der Name: Beim Fund lief im Radio gerade ein Lied der Gruppe Beatles. Nach diesem Lied wurde das Skelett Lucy genannt.",
           merke="Lucy = Australopithecus afarensis, ein Vormensch. Gefunden in Ostafrika, über 3 Millionen Jahre alt."),
        lb(L_AUSSEHEN,
           "Lucy sah **wahrscheinlich** eher wie ein Schimpanse aus. Sie ging aber **vorwiegend aufrecht**. Die Wörter „wahrscheinlich“ und „vorwiegend“ zeigen: Man weiß es nicht ganz genau.\n"
           "Woran erkennt man den aufrechten Gang?\n"
           "- am **Knochenbau**\n"
           "- an **Fußspuren**: In Laetoli in Tansania fand man 1978 Fußabdrücke eines Vormenschen der Art Australopithecus afarensis.",
           merke="Lucy sah wahrscheinlich eher wie ein Schimpanse aus, ging aber vorwiegend aufrecht. Beweise: Knochenbau und Fußspuren."),
        lb(L_GANG,
           "Der **aufrechte Gang** war ein wichtiger Entwicklungsschritt hin zum Menschen. Er hatte drei Vorteile:\n"
           "- **Bessere Sicht**: Man erkennt Nahrung und Gefahren früher.\n"
           "- **Weniger Energie**: Lange Wege sind weniger anstrengend.\n"
           "- **Hände frei**: Man kann Nahrung sammeln oder Gegenstände tragen.",
           merke="Aufrechter Gang: bessere Sicht, weniger Energie für lange Wege, Hände frei."),
        lb(L_VERGLEICH,
           "Die Zeichnung zeigt drei einfache Figuren von der Seite. Sie sind nicht maßstabsgetreu. Von links nach rechts: Schimpanse, Lucy, moderner Mensch. Das erkennst du an der Haltung:\n"
           "- Der **Schimpanse** ist stark nach vorn gebeugt.\n"
           "- **Lucy** steht schon überwiegend aufrecht.\n"
           "- Der **moderne Mensch** geht ganz aufrecht.\n"
           "Zusatzwissen (steht nicht im Heft, ist aber allgemein bekannt): Der Schimpanse hat lange Arme und kurze Beine. Beim modernen Menschen sind die Arme kürzer und die Beine lang. Lucys Gehirn war noch klein, ähnlich wie beim Schimpansen. Solche Angaben darfst du nur vorsichtig benutzen.",
           merke="Lucy steht zwischen Schimpanse und Mensch: Sie ging überwiegend aufrecht. Ihr Gehirn war noch klein (Zusatzwissen).",
           bild=svg_drei(("S", "L", "M"), "namen"), bildAlt=alt_drei(("S", "L", "M"), "namen")),
        lb(L_METHODE,
           "Ein **Verfassertext** ist ein Text, den ein Verfasser (Autor) geschrieben hat, um etwas zu erklären, zum Beispiel ein Sachtext im Schulbuch. Du wertest ihn in drei Schritten aus:\n"
           "- **1. Überblick**: Lies den Text zügig. Finde Thema und Fragestellung. Schreibe Überschrift und Stichwörter auf.\n"
           "- **2. Untersuchung**: Gliedere den Text in Abschnitte. Notiere die Gedanken jedes Abschnitts. Achte darauf, wie der Verfasser schreibt (siehe nächster Abschnitt).\n"
           "- **3. Zusammenfassung**: Schreibe die wichtigsten Informationen in eigener Form auf, zum Beispiel in wenigen Sätzen, als Stichwortliste, als Tabelle oder als **Strukturskizze**.\n"
           "Eine Strukturskizze ist eine kleine Zeichnung aus Kästchen und Pfeilen, die zeigt, wie die wichtigsten Gedanken zusammenhängen (Zusatz).",
           merke="Überblick, Untersuchung, Zusammenfassung: Das sind die drei Schritte beim Auswerten eines Verfassertextes."),
        lb(L_SPRACHE,
           "Verfasser benutzen bestimmte Wörter, die dir etwas verraten. Die Wörter helfen dir bei der Untersuchung des Textes:\n"
           "- **zeitliche Bezüge**: vorher, nachher, plötzlich, danach, später\n"
           "- **Begründungen**: weil, da, deshalb, deswegen\n"
           "- **Gegensätze**: einerseits – andererseits, obwohl, trotzdem\n"
           "- **Unsicherheit**: manche meinen, vielleicht, vermutlich, wahrscheinlich, vorwiegend\n"
           "Das Wort „vorwiegend“ heißt „meistens, aber nicht immer“. Es sagt also auch: Man weiß es nicht ganz genau.\n"
           "Beispiel: „Sie sah wahrscheinlich wie ein Schimpanse aus. Trotzdem ging sie vorwiegend aufrecht.“ Hier zeigt „wahrscheinlich“ Unsicherheit, „trotzdem“ einen Gegensatz.",
           merke="Wörter der Unsicherheit (wahrscheinlich, vielleicht, vorwiegend) zeigen: Man weiß etwas nicht ganz genau."),
        lb(L_TEXT,
           "Hier ist ein Beispieltext über Lucy. Er ist eigens für dich geschrieben:\n"
           f"„{BEISPIEL}“\n"
           "So wertest du ihn aus:\n"
           "- **Überblick**: Thema ist Lucy. Die Frage lautet: Wie sah Lucy aus, und warum ist der aufrechte Gang wichtig? Stichwörter: Lucy, Ostafrika, aufrechter Gang, Fußspuren.\n"
           "- **Untersuchung**: Unsicherheit zeigen „wahrscheinlich“ und „vorwiegend“. Der Gegensatz steht bei „trotzdem“. Begründungen beginnen mit „weil“, „da“ und „deshalb“. Zeitlich sind „1974“ und „später“.\n"
           "- **Zusammenfassung**: Lucy, über 3 Millionen Jahre alt, Ostafrika. Sah wahrscheinlich wie ein Schimpanse aus, ging vorwiegend aufrecht (Knochenbau, Fußspuren). Aufrechter Gang: Hände frei, wichtiger Schritt zum Menschen.",
           merke="Erst Überblick, dann die Signalwörter finden, dann in eigenen Worten zusammenfassen."),
    ]


def mit(t, lesen):
    t["lesen"] = lesen
    return t


# ------------------------------------------------------------------ Aufgaben

def block_a():
    s = "A – Afrika und der Fund von Lucy"
    return [
        mc("Auf welchem Kontinent fand man die ältesten Skelette menschenähnlicher Lebewesen?",
           "Afrika", ["Asien", "Europa", "Südamerika"], s,
           info="Die ältesten Skelettfunde stammen aus Afrika. Darum sagt man: Der Mensch stammt aus Afrika."),
        kurz("Afrika heißt auch die „Wiege der ...“. Ergänze das fehlende Wort.",
             ["Menschheit", "Wiege der Menschheit", "die Wiege der Menschheit"], s,
             info="Dort lebten die ersten menschenähnlichen Lebewesen. Deshalb heißt Afrika Wiege der Menschheit."),
        mc("Was ist Lucy?",
           "Das Skelett eines Vormenschen, des Australopithecus afarensis",
           ["Das Skelett eines Neandertalers aus der Eiszeit", "Die Mumie eines Jägers aus den Alpen", "Eine Zeichnung eines Vormenschen aus Afrika"], s,
           info="Lucy ist der Name eines Skeletts. Es gehört zu einem Australopithecus afarensis, einem Vormenschen."),
        kurz("In welchem Teil Afrikas wurde Lucy gefunden?", ost_formen(), s,
             info="Das Heft sagt Ostafrika. Das Buch nennt Hadar in Äthiopien, das liegt in Ostafrika. Beide Angaben zählen."),
        mc("Wie alt ist Lucy ungefähr?",
           "etwa 3 Millionen Jahre", ["etwa 30 000 Jahre", "etwa 300 000 Jahre", "etwa 30 Millionen Jahre"], s,
           info="Nach dem Heft ist Lucy über 3 Millionen Jahre alt, ungefähr 3 Millionen. Das Buch nennt genauer 3,18 Millionen Jahre.",
           tipp="Es sind Millionen, nicht Tausende von Jahren."),
        tf("Von Lucys Skelett sind etwa 40 Prozent der Knochen erhalten.", True, s,
           info="Deshalb gilt Lucy als eines der am besten erhaltenen menschenartigen Wesen."),
        mc("Wonach wurde Lucy benannt?",
           "Nach einem Lied der Beatles, das beim Fund im Radio lief",
           ["Nach der Forscherin, die das Skelett entdeckt hat", "Nach dem Fundort Hadar in Äthiopien", "Nach der Tochter eines Forschers der Gruppe"], s,
           info="Die Forschergruppe hörte beim Fund ein Lied der Beatles im Radio. Danach nannte sie das Skelett Lucy."),
        luecke("Ergänze den Text über Lucy.",
               "Das Skelett {{Lucy}} gehört zu einem {{Vormenschen|Vormensch}}. Es wurde auf dem Kontinent {{Afrika}} gefunden, und zwar in der Region {{Ostafrika|Ost-Afrika}}.",
               s, extra=["Europa", "Neandertaler"],
               info="Lucy ist der Name des Skeletts eines Vormenschen. Der Kontinent ist Afrika, die Region Ostafrika."),
        zuordnen("Ordne jede Angabe der richtigen Zahl oder dem richtigen Ort zu.",
                 [("Alter von Lucy", "über 3 Millionen Jahre"), ("Beginn des aufrechten Gangs", "vor etwa 4 Millionen Jahren"),
                  ("Erhaltene Knochen", "etwa 40 Prozent"), ("Jahr des Fundes (Buch)", "1974"), ("Fundregion", "Ostafrika")],
                 s, extra=["Südafrika", "1994"],
                 info="Der aufrechte Gang begann früher (4 Millionen Jahre) als Lucy lebte (über 3 Millionen Jahre)."),
    ]


def block_b():
    s = "B – Aussehen, aufrechter Gang und seine Folgen"
    ereignisse = [(f"Beginn des aufrechten Gangs (vor etwa 4 Millionen Jahren)", 0), ("Lucy lebt (vor über 3 Millionen Jahren)", 1),
                  (f"Forscher finden Lucys Skelett in Ostafrika ({FUND_LUCY})", 2), (f"Forscher finden die Fußspuren in Laetoli, Tansania ({FUND_SPUREN})", 3)]
    return [
        mc("Wie sah Lucy wahrscheinlich aus?",
           "Eher wie ein Schimpanse, ging aber vorwiegend aufrecht.",
           ["Ganz wie ein heutiger Mensch, nur etwas kleiner.", "Wie ein Neandertaler mit Fellkleidung und Speer.", "Wie ein Wesen, das niemals aufrecht gehen konnte."], s,
           info="Das Heft sagt: Lucy sah wahrscheinlich eher wie ein Schimpanse aus, ging aber vorwiegend aufrecht."),
        kurz("Vor etwa wie vielen Millionen Jahren begannen die ersten menschenähnlichen Lebewesen, aufrecht zu gehen?",
             mio_formen("4", "vier"), s, einheit="Millionen Jahre",
             info="Der aufrechte Gang begann vor etwa 4 Millionen Jahren, also noch vor Lucy.",
             tipp="Der aufrechte Gang begann, bevor Lucy lebte. Schau im Abschnitt über Afrika nach."),
        mc("Woran erkennt man, dass Lucy vorwiegend aufrecht ging?",
           "Am Knochenbau und an Fußspuren von Vormenschen",
           ["An ihrem hohen Alter von über 3 Millionen Jahren", "An ihrem Fundort in Ostafrika", "An dem Lied, das beim Fund im Radio lief"], s,
           info="Der Knochenbau und die Fußspuren (Buch: Laetoli in Tansania) zeigen den aufrechten Gang."),
        tf("Die Fußspuren aus Laetoli in Tansania stammen von einem Vormenschen und passen zu einem aufrechten Gang.", True, s,
           info="Das Buch zeigt Fußabdrücke eines Vormenschen der Art Australopithecus afarensis. Fußspuren sind eine Quelle für den aufrechten Gang."),
        mc("Wähle alle richtigen Antworten: Welche Folgen hatte der aufrechte Gang?",
           ["Man sah Nahrung und Gefahren früher.", "Man brauchte weniger Energie für lange Wege.", "Die Hände waren frei zum Tragen."],
           ["Das Gehirn wurde sofort viel größer.", "Man konnte plötzlich Feuer erzeugen."], s,
           info="Bessere Sicht, weniger Energie und freie Hände sind die drei Vorteile. Feuer erzeugen konnte der Mensch erst viel später."),
        mit(zuordnen("Ordne zu: Welche Folge hatte der aufrechte Gang, und woran erkennt man ihn?",
                     [("Bessere Sicht", "Man erkennt Nahrung oder Gefahren früher"), ("Weniger Energie", "Lange Wege sind weniger anstrengend"),
                      ("Hände frei", "Man kann Nahrung oder Gegenstände tragen"), ("Woran man den aufrechten Gang erkennt", "Knochenbau und Fußspuren")],
                     s, extra=["Man kann Feuer selbst erzeugen"],
                     info="Die drei Vorteile stehen im Heft. Den aufrechten Gang erkennt man am Knochenbau und an Fußspuren."), [L_GANG, L_AUSSEHEN]),
        luecke("Ergänze den Satz über den aufrechten Gang.",
               "Beim aufrechten Gang sind die {{Hände}} frei. Man hat eine bessere {{Sicht}} und braucht weniger {{Energie}} für lange Wege. Der aufrechte Gang war ein wichtiger {{Entwicklungsschritt}} hin zum Menschen.",
               s, extra=["Zähne", "Feuer"],
               info="Das sind die Folgen des aufrechten Gangs."),
        tf("Nach dem Heft ging Lucy ausschließlich aufrecht.", False, s,
           info="Das Heft sagt vorwiegend aufrecht. Das heißt: meistens, aber nicht immer.",
           tipp="Achte auf das Wort „vorwiegend“."),
        reihenfolge("Ordne die Ereignisse. Das früheste steht zuerst.", [e for e, _ in sorted(ereignisse, key=lambda x: x[1])], s,
                    info="Erst begann der aufrechte Gang, dann lebte Lucy. Viel später fanden Forscher 1974 ihr Skelett und 1978 die Fußspuren in Laetoli.",
                    tipp="Zwei Ereignisse geschahen vor Millionen Jahren, zwei sind Funde der Forscher. Achte auf die Jahreszahlen."),
    ]


def block_c():
    s = "C – Schimpanse, Lucy und Mensch vergleichen"
    r1, r2, r3, r4 = ("M", "S", "L"), ("L", "M", "S"), ("S", "M", "L"), ("L", "S", "M")
    std = ("S", "L", "M")
    return [
        mc("Auf dem Bild stehen ein Schimpanse, Lucy und ein moderner Mensch in gemischter Reihenfolge. Welche Figur ist Lucy?",
           f"Figur {buchst(r1, 'L')}", [f"Figur {buchst(r1, 'M')}", f"Figur {buchst(r1, 'S')}"], s,
           info="Lucy steht schon überwiegend aufrecht, ist aber noch leicht nach vorn geneigt. Der Mensch steht ganz gerade, der Schimpanse ist stark gebeugt.",
           tipp="Lucy steht zwischen dem Schimpansen und dem Menschen.", bild=svg_drei(r1, "buchstaben"), bildAlt=alt_drei(r1)),
        mc("Zusatzwissen: Welche Figur hat im Vergleich die längsten Arme und die kürzesten Beine?",
           f"Figur {buchst(r2, 'S')}", [f"Figur {buchst(r2, 'L')}", f"Figur {buchst(r2, 'M')}"], s,
           info="Der Schimpanse hat lange Arme und kurze Beine. Das gehört zu seiner gebeugten Haltung (Zusatzwissen).",
           tipp="Vergleiche die drei Figuren mit der Zeichnung im Lernblatt.", bild=svg_drei(r2, "buchstaben"), bildAlt=alt_drei(r2)),
        zuordnen("Auf dem Bild stehen ein Schimpanse, Lucy und ein moderner Mensch. Ordne jedem Buchstaben die richtige Figur zu.",
                 [(f"Figur {buchst(r3, 'S')}", "Schimpanse"), (f"Figur {buchst(r3, 'M')}", "moderner Mensch"), (f"Figur {buchst(r3, 'L')}", "Lucy")],
                 s, extra=["Mammut"],
                 info="Der Schimpanse ist am stärksten gebeugt, der Mensch geht ganz aufrecht, Lucy liegt dazwischen.",
                 bild=svg_drei(r3, "buchstaben"), bildAlt=alt_drei(r3)),
        mc("Was zeigt die Zeichnung über die beiden äußeren Figuren, den Schimpansen und den modernen Menschen?",
           "Der Schimpanse ist stark nach vorn gebeugt, der moderne Mensch geht ganz aufrecht.",
           ["Der Schimpanse geht ganz aufrecht, der moderne Mensch ist stark nach vorn gebeugt.", "Beide gehen ganz aufrecht.", "Beide sind gleich stark nach vorn gebeugt."], s,
           info="Der Schimpanse und der moderne Mensch bilden die beiden Gegensätze. Dazwischen steht Lucy.",
           bild=svg_drei(std, "namen"), bildAlt=alt_drei(std, "namen")),
        mc("In welchem Punkt ist Lucy dem Menschen ähnlicher als dem Schimpansen?",
           "Sie ging vorwiegend aufrecht.",
           ["Sie hatte ein ebenso großes Gehirn wie ein moderner Mensch.", "Sie lebte erst vor wenigen tausend Jahren.", "Sie wurde nicht in Afrika gefunden."], s,
           info="Der aufrechte Gang ist die Ähnlichkeit mit dem Menschen. Ihr Gehirn war dagegen noch klein, ähnlich wie beim Schimpansen (Zusatzwissen).",
           tipp="Denke an den Körperbau."),
        tf("Die Zeichnung zeigt genau, wie groß Schimpanse, Lucy und moderner Mensch waren.", False, s,
           info="Die Zeichnung ist stark vereinfacht und nicht maßstabsgetreu. Sie zeigt nur die Körperhaltung der drei.",
           tipp="Lies im Lernblatt nach, was zur Zeichnung gesagt wird.",
           bild=svg_drei(std, "namen"), bildAlt=alt_drei(std, "namen")),
        luecke("Ergänze den Vergleich.",
               "Der {{Schimpanse}} ist stark nach vorn gebeugt. {{Lucy}} ging vorwiegend aufrecht, ihr Gehirn war aber noch klein. Der {{moderne Mensch|Mensch}} geht ganz aufrecht.",
               s, extra=["Wollnashorn", "Mammut"],
               info="So unterscheiden sich die drei in Haltung und Gehirn (Gehirn: Zusatzwissen)."),
        reihenfolge("Ordne die Figuren nach ihrer Haltung, von der am stärksten gebeugten bis zur ganz aufrechten.",
                    [f"Figur {buchst(r4, 'S')}", f"Figur {buchst(r4, 'L')}", f"Figur {buchst(r4, 'M')}"], s,
                    info="Schimpanse (stark gebeugt), dann Lucy (fast aufrecht), zuletzt der Mensch (ganz aufrecht).",
                    tipp="Beschreibe zuerst, wie jede Figur steht: stark gebeugt, fast aufrecht oder ganz aufrecht.", bild=svg_drei(r4, "buchstaben"), bildAlt=alt_drei(r4)),
        zuordnen("Zu welchem Wesen passt das Merkmal?",
                 [("stark nach vorn gebeugt", "Schimpanse"), ("lange Arme, kurze Beine", "Schimpanse"),
                  ("vorwiegend aufrecht, Gehirn noch klein", "Lucy"), ("ganz aufrecht", "moderner Mensch"),
                  ("lange Beine, kürzere Arme", "moderner Mensch")], s,
                 info="Die Merkmale stehen im Lernblatt. Das Gehirn und die Armlängen sind Zusatzwissen."),
    ]


def block_d():
    s = "D – Verfassertext auswerten: die drei Schritte"
    return [
        reihenfolge("Ordne die drei Schritte beim Auswerten eines Verfassertextes.",
                    ["Einen Überblick gewinnen", "Den Text untersuchen", "Die wichtigsten Informationen zusammenfassen"], s,
                    info="Zuerst liest man zügig und sucht das Thema. Dann untersucht man den Text genauer. Zuletzt fasst man zusammen."),
        mc("Was tust du im ersten Schritt, dem Überblick?",
           "Zügig lesen, Thema finden, Stichwörter notieren",
           ["Wort für Wort abschreiben und auswendig lernen", "Zuerst die Zusammenfassung schreiben, dann lesen", "Nur den letzten Absatz lesen, den Rest weglassen"], s,
           info="Beim Überblick geht es um das Thema und die Frage des Textes. Die Einzelheiten kommen erst im zweiten Schritt."),
        zuordnen("Was gehört zu welchem Schritt?",
                 [("Schritt 1: Überblick", "Thema und Fragestellung finden"), ("Schritt 2: Untersuchung", "Gedanken jedes Abschnitts notieren und auf die Sprache achten"),
                  ("Schritt 3: Zusammenfassung", "Das Wichtigste kurz in eigener Form festhalten")],
                 s, extra=["den Text auswendig lernen", "den Text Wort für Wort abschreiben"],
                 info="Jeder Schritt hat eine eigene Aufgabe. Eine Zusammenfassung schreibst du mit eigenen Worten, zum Beispiel als wenige Sätze oder als Stichwortliste."),
        luecke("Ergänze den Satz über die Methode.",
               "Zuerst verschafft man sich einen {{Überblick}}, dann {{untersucht}} man den Text und zuletzt fasst man die wichtigsten Informationen in eigener Form {{zusammen}}.",
               s, extra=["abschreiben", "auswendig"],
               info="Das sind die drei Schritte: Überblick, Untersuchung, Zusammenfassung."),
        tf("Im ersten Schritt schreibt man die Überschrift und Stichwörter des Textes auf.", True, s,
           info="Überschrift und Stichwörter gehören zum Überblick."),
        tf("Eine Zusammenfassung darf auch eine Stichwortliste, eine Tabelle oder eine Strukturskizze sein.", True, s,
           info="Du darfst die Form selbst wählen. Wichtig ist, dass du das Wichtigste in eigenen Worten festhältst."),
        mc("Was ist ein Verfassertext?",
           "Ein Sachtext, den ein Autor geschrieben hat, um etwas zu erklären",
           ["Eine Urkunde aus dem Mittelalter, die damals entstand", "Ein Brief, den ein Zeitzeuge an seine Familie schrieb", "Eine Zeichnung, die ein Forscher nach Funden anfertigte"], s,
           info="Der Verfasser ist der Autor. Der Text auf dem Infoblatt über Lucy ist ein solcher Sachtext.",
           tipp="Überlege, wer den Text geschrieben hat und wozu."),
    ]


def block_e():
    s = "E – Sprache im Text: Signalwörter erkennen"
    t1 = "Lucy lebte vor über drei Millionen Jahren in Ostafrika. Sie sah wahrscheinlich eher wie ein Schimpanse aus. Trotzdem ging sie vorwiegend aufrecht."
    t2 = "Weil Lucy aufrecht ging, hatte sie die Hände frei. Deshalb konnte sie Nahrung tragen."
    t3 = "Vor etwa vier Millionen Jahren begannen menschenähnliche Lebewesen, aufrecht zu gehen. Danach lebte Lucy in Ostafrika. Später fand man ihr Skelett."
    return [
        mc(f"Lies den Text:\n„{t1}“\nWähle alle richtigen Antworten: Welche Wörter zeigen, dass der Verfasser etwas nicht ganz sicher weiß?",
           ["wahrscheinlich", "vorwiegend"], ["Trotzdem", "Ostafrika"], s,
           info="Wörter der Unsicherheit sind zum Beispiel wahrscheinlich, vielleicht und vorwiegend. Trotzdem zeigt einen Gegensatz.",
           tipp="Welche Wörter schränken eine Aussage ein?"),
        kurz(f"Lies den Text:\n„{t1}“\nWelches Wort zeigt einen Gegensatz?",
             ["Trotzdem", "trotzdem"], s,
             info="Trotzdem verbindet zwei Aussagen, die nicht zusammenpassen: Sie sah wie ein Schimpanse aus, ging aber aufrecht."),
        kurz(f"Lies den Text:\n„{t2}“\nMit welchem Wort beginnt der zweite Satz? Es zeigt eine Begründung.",
             ["Deshalb", "deshalb"], s,
             info="Deshalb gehört zu den Begründungswörtern (weil, da, deshalb, deswegen). Es verbindet einen Grund mit dem, was daraus folgt: Weil Lucy aufrecht ging, hatte sie die Hände frei, deshalb konnte sie Nahrung tragen."),
        zuordnen("Welche Art von Signalwort ist das?",
                 [("danach", "zeitlicher Bezug"), ("deshalb", "Begründung"), ("trotzdem", "Gegensatz"), ("vielleicht", "Unsicherheit"),
                  ("da", "Begründung"), ("obwohl", "Gegensatz")], s,
                 info="Zeit: vorher, nachher, danach. Grund: weil, da, deshalb. Gegensatz: obwohl, trotzdem. Unsicherheit: vielleicht, vermutlich."),
        kurz(f"Lies den Text:\n„{t3}“\nNenne ein Wort im Text, das die zeitliche Reihenfolge anzeigt.",
             ["Danach", "Später", "danach", "später"], s,
             info="Danach und später zeigen, was zuerst und was später geschah."),
        tf("Wörter wie „wahrscheinlich“ oder „vermutlich“ zeigen, dass der Verfasser etwas nicht ganz sicher weiß.", True, s,
           info="Solche Wörter der Unsicherheit sagen dir: Das weiß man nicht genau."),
        mc("Warum schreibt ein Verfasser über Lucys Aussehen „wahrscheinlich“?",
           "Weil man ihr Aussehen nur aus Funden erschließen kann",
           ["Weil man von Lucy nur Fußspuren, aber keine Knochen gefunden hat", "Weil Forscher Lucys Alter schätzen, ihr Aussehen aber genau kennen", "Weil niemand weiß, wo man Lucy gefunden hat"], s,
           info="Von Lucy gibt es nur Knochen, dazu Fußspuren eines Vormenschen derselben Art, aber keine Fotos. Deshalb bleibt manches unsicher."),
    ]


def block_f():
    s = "F – Klausurnahe Aufgaben"
    std = ("S", "L", "M")
    return [
        mit(mc(f"Lies den Text:\n„{BEISPIEL2}“\nWelche Überschrift passt am besten?",
               "Der aufrechte Gang als Schritt zum Menschen",
               ["Die Erfindung des Feuers durch den Menschen", "Ötzi, der Mann aus dem Gletschereis", "Das Leben der Jäger und Sammler in der Eiszeit"], s,
               info="Der Text handelt vom aufrechten Gang und von Lucy. Die anderen Themen kommen im Text nicht vor.",
               tipp="Suche das Thema: Wer oder was steht im Mittelpunkt?"), [L_METHODE, L_TEXT]),
        mit(frei(f"Lies den Text:\n„{BEISPIEL2}“\nSuche je ein Beispiel für ein Wort der Unsicherheit, ein Begründungswort, einen Gegensatz und einen zeitlichen Bezug.",
                 "Unsicherheit: „wahrscheinlich“ oder „vorwiegend“. Begründung: „weil“ oder „deshalb“. Gegensatz: „obwohl“. Zeitlicher Bezug: „danach“, „vor etwa vier Millionen Jahren“ oder „1978“.",
                 ["Wort der Unsicherheit richtig (wahrscheinlich oder vorwiegend)", "Begründungswort richtig (weil oder deshalb)", "Gegensatz richtig (obwohl)", "zeitlicher Bezug richtig (danach, 1978 oder vor etwa vier Millionen Jahren)"], 4, s), [L_SPRACHE, L_TEXT]),
        mit(frei(f"Lies den Text:\n„{BEISPIEL2}“\nFasse den Text in drei bis vier Sätzen oder als Stichwortliste zusammen.",
                 "Vor etwa 4 Millionen Jahren begannen menschenähnliche Lebewesen in Afrika, aufrecht zu gehen. Das brachte bessere Sicht, weniger Energieverbrauch auf langen Wegen und freie Hände zum Tragen. Lucy sah wahrscheinlich eher wie ein Schimpanse aus, ging aber vorwiegend aufrecht. Dazu passen Fußabdrücke eines Vormenschen, die man 1978 in Laetoli in Tansania fand.",
                 ["Beginn des aufrechten Gangs genannt (vor etwa 4 Millionen Jahren, Afrika)", "Vorteile genannt (bessere Sicht, weniger Energie, Hände frei)", "Lucy: wahrscheinlich wie ein Schimpanse, aber vorwiegend aufrecht", "Fußabdrücke aus Laetoli (1978) als Beleg genannt", "in eigenen Worten und kurz"], 5, s), [L_METHODE, L_TEXT]),
        mit(frei("Erkläre, warum der aufrechte Gang ein wichtiger Entwicklungsschritt hin zum Menschen war. Nenne drei Folgen.",
                 "Wer aufrecht geht, sieht Nahrung und Gefahren früher (bessere Sicht). Er braucht weniger Energie für lange Wege. Außerdem hat er die Hände frei, um Nahrung zu sammeln oder Gegenstände zu tragen.",
                 ["bessere Sicht", "weniger Energie für lange Wege", "Hände frei zum Sammeln oder Tragen"], 3, s), L_GANG),
        mit(frei("Das Bild zeigt einen Schimpansen, Lucy und einen modernen Menschen. Vergleiche die drei. Wo ähnelt Lucy dem Menschen, wo dem Schimpansen?",
                 "Der Schimpanse ist stark nach vorn gebeugt und hat lange Arme und kurze Beine. Der Mensch geht ganz aufrecht und hat lange Beine. Lucy steht dazwischen: Sie ging vorwiegend aufrecht, das ähnelt dem Menschen. Sie sah aber wahrscheinlich eher wie ein Schimpanse aus, und ihr Gehirn war noch klein (Zusatzwissen).",
                 ["Schimpanse: gebeugt", "Mensch: ganz aufrecht", "Lucy ähnelt dem Menschen im aufrechten Gang", "Lucy ähnelt dem Schimpansen (Aussehen oder kleines Gehirn)"], 4, s,
                 tipp="Beschreibe zuerst die Haltung jeder Figur.", bild=svg_drei(std, "namen"), bildAlt=alt_drei(std, "namen")), L_VERGLEICH),
        mit(luecke("Ergänze die Zusammenfassung über Lucy.",
                   "Lucy gehört zu den {{Vormenschen}}. Sie lebte vor über {{3}} Millionen Jahren in {{Ostafrika}}. Sie ging {{vorwiegend|überwiegend}} aufrecht und sah wahrscheinlich eher wie ein {{Schimpanse}} aus.",
                   s, extra=["30", "Neandertaler"],
                   info="Das ist die Kurzfassung des Themas Lucy."), [L_FUND, L_AUSSEHEN]),
    ]


def _lesen(bl, liste):
    """Setzt bei den Aufgaben eines Blocks das Feld lesen: liste = {Index: Titel oder Liste}."""
    for i, v in liste.items():
        bl[i]["lesen"] = v
    return bl


def aufgaben():
    a = _lesen(block_a(), {0: L_AFRIKA, 1: L_AFRIKA, 2: L_FUND, 3: L_FUND, 4: L_FUND, 5: L_FUND, 6: L_FUND, 7: [L_AFRIKA, L_FUND], 8: [L_AFRIKA, L_FUND]})
    b = _lesen(block_b(), {0: L_AUSSEHEN, 1: L_AFRIKA, 2: L_AUSSEHEN, 3: L_AUSSEHEN, 4: L_GANG, 5: [L_GANG, L_AUSSEHEN], 6: L_GANG, 7: L_AUSSEHEN, 8: [L_AFRIKA, L_FUND, L_AUSSEHEN]})
    return a + b + block_c() + block_d() + block_e() + block_f()


def build():
    p = pack("geschichte-3-lucy", "Geschichte Teil 3: Vom Affen zum Menschen (Lucy)",
             "Afrika als Wiege der Menschheit, Lucy (Fund, Alter, Aussehen), der aufrechte Gang, Vergleich von Schimpanse, Lucy und Mensch und das Auswerten eines Verfassertextes. Mit Lernblatt und Übungsaufgaben.",
             lernblatt(), aufgaben(), min_aufgaben=38,
             hinweis="Die Zeichnung von Schimpanse, Lucy und Mensch ist stark vereinfacht und nicht maßstabsgetreu. Angaben zu Gehirn, Armen und Beinen sind Zusatzwissen, das nicht im Heft steht. Die Texte zum Auswerten sind selbst geschrieben.")
    nachlesen(p, {
        "A – Afrika und der Fund von Lucy": [L_AFRIKA, L_FUND],
        "B – Aussehen, aufrechter Gang und seine Folgen": [L_AFRIKA, L_FUND, L_AUSSEHEN, L_GANG],
        "C – Schimpanse, Lucy und Mensch vergleichen": L_VERGLEICH,
        "D – Verfassertext auswerten: die drei Schritte": L_METHODE,
        "E – Sprache im Text: Signalwörter erkennen": [L_SPRACHE, L_TEXT],
        "F – Klausurnahe Aufgaben": [L_FUND, L_AUSSEHEN, L_GANG, L_VERGLEICH, L_METHODE, L_SPRACHE, L_TEXT],
    })
    p["probe"] = False
    assert 38 <= len(p["aufgaben"]) <= 50, len(p["aufgaben"])
    assert 5 <= len(p["lernblatt"]) <= 9
    return [p]
