"""Geschichte Klasse 6: eigene Probearbeit (der Lehrer hat keine Probearbeit und keine Form vorgegeben).

Alle Aufgaben sind neu, nicht aus den Übungspaketen, aber auf Grundlage derselben Fakten und auf derselben Schwierigkeit.
46 Punkte in sechs Teilen, etwa 45 Minuten, ohne Hilfsmittel. Das Paket hat kein Lernblatt; jede Aufgabe verweist
mit „lesen“ auf den passenden Abschnitt eines Übungspakets. Jahreszahlen und Rechnungen werden im Code berechnet und mit assert geprüft.
Datenschutz: Das Repository ist öffentlich. Die Familie Berger ist erfunden, es kommen keine echten Daten vor.
"""
import gesch_lib
from gesch_lib import *                                   # noqa: F401,F403  (mc, tf, kurz, luecke, zuordnen, reihenfolge, frei, pack ...)
from gesch_lib import (jahr, spanne, epoche, EPOCHEN, PERSONEN, EHEN, WAFFEN, punkte_von,
                       svg_epochen, svg_zeitstrahl_punkte, svg_stammbaum, svg_drei)

ID = "geschichte-probearbeit"

# Pakete der Übungsreihe, auf die verwiesen wird
P1 = "geschichte-1-quellen-stammbaum"
P2A = "geschichte-2a-zeitrechnung-kalender"
P2B = "geschichte-2b-epochen-zeitstrahl"
P3 = "geschichte-3-lucy"
P4A = "geschichte-4a-steinzeit-eiszeit-werkzeuge"
P4B = "geschichte-4b-altsteinzeit-jagen-leben"
P5A = "geschichte-5a-neolithische-revolution"
P5B = "geschichte-5b-jungsteinzeit-leben-vergleich"
P6 = "geschichte-6-oetzi"


def ref(paket, titel):
    return {"paket": paket, "titel": titel}


# Überschriften der Teile mit ihren Punkten (werden in build() gegen die Aufgaben geprüft)
TEILE = {
    "A": ("Quellen, Lebenslauf und Stammbaum", 10),
    "B": ("Zeit, Zeitrechnung und Epochen", 10),
    "C": ("Lucy", 6),
    "D": ("Altsteinzeit", 7),
    "E": ("Jungsteinzeit und der Vergleich", 7),
    "F": ("Ötzi", 6),
}
GESAMT = 46


def abschnitt(k):
    name, pt = TEILE[k]
    return f"Teil {k} – {name} ({pt} Punkte)"


def jahrhundert(y):
    """Jahrhundert eines Jahres n. Chr. (Buch: 1200 bis 1299 = 13. Jahrhundert; Jahreszahl ohne die letzten zwei Stellen plus 1)."""
    return y // 100 + 1


# ------------------------------------------------------------------ Bildbeschreibungen

def alt_stammbaum():
    """Passend zu svg_stammbaum() ohne Markierungen. Nennt nur die Zeichen, nicht ihre Bedeutung."""
    def z(n):
        p = PERSONEN[n]
        return f"{n} (∗ {p['geb']}" + (f", † {p['tod']}" if p["tod"] else "") + f", {p['beruf']})"
    return ("Stammbaum der erfundenen Familie Berger in drei Reihen. Oben die Kinder " + z("Tom") + " und " + z("Mia") +
            ". In der Mitte ihre Eltern " + z("Jan") + " und " + z("Anna") + ", zwischen ihnen zwei Ringe. Unten die Großeltern: " +
            z("Karl") + " und " + z("Ruth") + " (Jans Eltern, zwischen ihnen zwei Ringe) sowie " + z("Hans") + " und " + z("Eva") +
            " (Annas Eltern, zwischen ihnen zwei Ringe).")


NAMEN = {"S": "Schimpanse", "L": "Lucy", "M": "moderner Mensch"}
HALTUNG = {
    "S": "stark nach vorn gebeugt, mit langen Armen und kurzen Beinen",
    "L": "fast aufrecht, nur leicht nach vorn geneigt",
    "M": "ganz aufrecht, mit langen Beinen und kürzeren Armen",
}


def alt_drei_namen(reihe):
    teile = [f"{NAMEN[k]}: {HALTUNG[k]}" for k in reihe]
    return ("Drei einfache Strichfiguren von der Seite (nicht maßstabsgetreu), von links nach rechts mit Namen. " + "; ".join(teile) + ".")


def alt_zeitstrahl(punkte):
    """Beschreibt die Lage der Punkte in Teilstrichen (10 Jahre je Strich) von der nächsten Marke aus, ohne Jahreszahlen zu nennen."""
    marken = {-100: "100 v. Chr.", -50: "50 v. Chr.", 0: "Christi Geburt", 50: "50 n. Chr."}
    teile = []
    for b, y in punkte:
        m = min(marken, key=lambda k: abs(y - k))
        n = abs(y - m) // 10
        teile.append(f"Punkt {b} liegt genau auf der Marke {marken[m]}" if n == 0 else
                     f"Punkt {b} liegt {n} Teilstriche (je 10 Jahre) {'rechts' if y > m else 'links'} von der Marke {marken[m]}")
    return ("Ein Zeitstrahl von 100 v. Chr. bis 50 n. Chr. mit einem Teilstrich alle 10 Jahre. Beschriftet sind 100 v. Chr., 50 v. Chr., "
            "Christi Geburt und 50 n. Chr. Drei Punkte sind markiert: " + "; ".join(teile) + ".")


def alt_epochen():
    return ("Ein Zeitstrahl aus fünf farbigen Abschnitten mit den Nummern 1 bis 5 von links nach rechts. Die Grenzen sind beschriftet: "
            "3000 v. Chr. (zwischen 1 und 2), 1000 v. Chr. (zwischen 2 und 3), 500 n. Chr. (zwischen 3 und 4) und 1500 (zwischen 4 und 5). "
            "Im Abschnitt 3 ist außerdem Christi Geburt markiert.")


# ------------------------------------------------------------------ Aufgaben
# Jede Aufgabe: (Schwierigkeit L/M/S, lesen, Aufgabe). Nummer und Punkte in der Frage setzt build().
# Winkel: Die Übungspakete fragen die Fakten schon direkt ab. Hier werden sie anders gebraucht (Quelle auswählen, Szenarien,
# Fehler suchen, Streit entscheiden, Zahlen kombinieren), mit anderen Beispielen und Zahlen.

def teil_a():
    s = abschnitt("A")
    # Mias Lebenslauf: Grundschule 2020 bis 2024 (Mia ist laut Stammbaum 2014 geboren, bei der Einschulung also 6 Jahre alt)
    mia = PERSONEN["Mia"]["geb"]
    gs0, gs1 = 2020, 2024
    gs = spanne(gs0, gs1)
    assert mia == 2014 and gs == 4 and gs0 - mia == 6
    # Stammbaum: Mia ist die jüngste Person, nur Karl ist gestorben, mit Jan ist Anna verheiratet
    jung = max(PERSONEN, key=lambda n: PERSONEN[n]["geb"])
    tot = [n for n, p in PERSONEN.items() if p["tod"]]
    frau = [b for a, b in EHEN if a == "Jan"]
    assert jung == "Mia" and tot == ["Karl"] and frau == ["Anna"]
    return [
        ("L", [ref(P1, "Quelle oder Darstellung?"), ref(P1, "Was ist eine Quelle?")],
         mc("Du möchtest herausfinden, womit die Menschen der Altsteinzeit Tiere jagten. Welche Quelle hilft dir am besten?",
            "Eine ausgegrabene Speerspitze aus Feuerstein",
            ["Ein Kinderbuch mit Zeichnungen von Steinzeitjägern",
             "Ein Spielfilm von 2018 über Jäger der Eiszeit",
             "Das Foto eines Jägers aus dem Jahr 1950"],
            s, info="Die Speerspitze stammt aus der Altsteinzeit selbst. Sie ist eine Sachquelle. Kinderbuch und Spielfilm sind viel später gemacht worden (Darstellungen), das Foto stammt aus einer ganz anderen Zeit.")),
        ("L", ref(P1, "Quellengattungen: Buch und Heft"),
         zuordnen("Im Archiv deiner Stadt liegen Quellen. Welche Art von Quelle ist jede davon nach deinem Heft? Ordne zu.",
                  [("eine Bauurkunde aus dem Jahr 1850", "Texte"),
                   ("eine Malerei, die den Marktplatz vor 300 Jahren zeigt", "Bilder"),
                   ("eine Schere, die ein Handwerker früher benutzt hat", "Sachquellen"),
                   ("eine Filmaufnahme vom Stadtfest 1960", "Tonaufnahmen und Filme")],
                  s, extra=["Zeitzeugen"],
                  info="Urkunden sind Texte, Malereien sind Bilder, Werkzeuge sind Sachquellen und Filmaufnahmen gehören zu den Tonaufnahmen und Filmen. Ein Zeitzeuge wäre ein Mensch, der selbst Erlebtes erzählt.")),
        ("M", ref(P1, "Quelle oder Darstellung?"),
         mc("Wähle alle richtigen Antworten. Was davon sind Darstellungen und keine Quellen?",
            ["Das Modell eines Dorfs der Jungsteinzeit, das ein Museum heute gebaut hat",
             "Ein Lexikonartikel über Ötzi"],
            ["Ein Mahlstein aus einem ausgegrabenen Dorf der Jungsteinzeit",
             "Eine Höhlenmalerei, die Menschen der Altsteinzeit gemalt haben"],
            s, info="Modell und Lexikonartikel haben Menschen viel später mithilfe von Quellen gemacht. Mahlstein und Höhlenmalerei stammen aus der Zeit selbst und sind Quellen.")),
        ("L", ref(P1, "Lebenslauf: meine eigene Geschichte"),
         kurz(f"Hier siehst du einen Teil von Mias Lebenslauf:\n- geboren: {mia}\n- Grundschule: {gs0} bis {gs1}\n- weiterführende Schule: ab {gs1}\nWie viele Jahre ging Mia zur Grundschule? Schreibe die Zahl.",
              [str(gs), f"{gs} Jahre", "vier", "vier Jahre"], s, einheit="Jahre",
              info=f"Von {gs0} bis {gs1} sind es {gs1} − {gs0} = {gs} Jahre. Ein Lebenslauf ordnet Schule, Ereignisse und Hobbys nach der Zeit.")),
        ("L", ref(P1, "Der Stammbaum"),
         luecke("Sieh dir den Stammbaum der Familie Berger an. Ergänze die Namen.",
                "Bei {{Mia}} steht ∗ 2014, sie ist die jüngste Person. Das Zeichen † steht nur bei {{Karl}}, denn nur er ist schon gestorben. Mit Jan ist {{Anna}} verheiratet, das zeigen die zwei Ringe.",
                s, extra=["Tom", "Ruth"],
                info="∗ gibt das Geburtsjahr an, 2014 ist das späteste. † zeigt, wer gestorben ist (Karl, 2019). Zwei Ringe (∞) zeigen, wer miteinander verheiratet ist.",
                bild=svg_stammbaum(), bildAlt=alt_stammbaum())),
    ]


def teil_b():
    s = abschnitt("B")
    # Zeitstrahl mit drei Punkten: 10 Jahre = 1 Teilstrich. Rechnen über Christi Geburt hinweg ohne Jahr 0.
    pa, pb, pc = -70, -20, 30
    punkte = [("A", pa), ("B", pb), ("C", pc)]
    ac = spanne(pa, pc)
    assert ac == 100 and pa < 0 < pc and pa % 50 and pc % 50
    # Jahrhundert: Jahreszahl ohne die letzten zwei Stellen plus 1
    jh_jahr = 1347
    jh = jahrhundert(jh_jahr)
    falsch = [1247, 1430, 1114]
    assert jh == 14 and all(jahrhundert(y) != 14 for y in falsch)
    # Epochen auf dem Bild: Das Jahr 1215 liegt in der Epoche mit der Nummer 4 (Mittelalter), Nummer 3 ist die Antike
    ep_jahr = 1215
    nr = [e[0] for e in EPOCHEN].index(epoche(ep_jahr)) + 1
    assert epoche(ep_jahr) == "Mittelalter" and nr == 4 and EPOCHEN[2][0] == "Antike" and EPOCHEN[4][0] == "Neuzeit"
    # 3. Jahrhundert v. Chr. (Jahre 200 bis 299 v. Chr.) liegt ganz in der Antike
    assert epoche(-200) == epoche(-299) == "Antike"
    # Ereignisse in zeitlicher Reihenfolge (Jahre als Zahlen; 14 000 Jahre vor 2026 = rund 12 000 v. Chr.)
    hund = -(14000 - 2026)
    assert -12500 < hund < -11500
    jahre = [-12000, -5000, -3000, -250, 1400]
    assert jahre == sorted(jahre) and -299 <= jahre[3] <= -200
    return [
        ("L", ref(P2A, "Zeit messen: vom Sonnenstand zur Uhr"),
         tf("Heute messen wir nur Zeitunterschiede, die ein Mensch auch ohne Gerät wahrnehmen kann.", False, s,
            info="Die Messung der Zeit wurde immer genauer. Heute messen wir Zeitunterschiede, die ein Mensch gar nicht mehr wahrnehmen kann.")),
        ("M", [ref(P2A, "Jahre vergleichen und Abstände berechnen"), ref(P2B, "Einen Zeitstrahl zeichnen und lesen")],
         kurz("Auf dem Zeitstrahl zeigt Punkt A das Jahr, in dem eine Brücke gebaut wurde, und Punkt C das Jahr, in dem sie einstürzte. Wie viele Jahre stand die Brücke? Rechne wie in der Schule (ohne Jahr 0).",
              [str(ac), f"{ac} Jahre"], s, einheit="Jahre",
              info=f"Punkt A zeigt {jahr(pa)}, Punkt C zeigt {jahr(pc)}. Über Christi Geburt hinweg rechnet man zusammen: {abs(pa)} + {pc} = {ac} Jahre.",
              bild=svg_zeitstrahl_punkte(punkte, von=-100, bis=50), bildAlt=alt_zeitstrahl(punkte))),
        ("L", ref(P2A, "Jahrhunderte bestimmen"),
         mc("Welche dieser Jahreszahlen liegt im 14. Jahrhundert?",
            f"{jh_jahr} n. Chr.", [f"{y} n. Chr." for y in falsch], s,
            info=f"Das {jh}. Jahrhundert umfasst die Jahre {(jh - 1) * 100} bis {(jh - 1) * 100 + 99}, also die Zahlen, die mit {jh - 1} beginnen.")),
        ("L", [ref(P2B, "Die fünf Epochen"), ref(P2B, "Die Epoche eines Jahres bestimmen")],
         luecke("Sieh dir den Zeitstrahl mit den fünf Epochen an. Ergänze.",
                f"Das Jahr {ep_jahr} n. Chr. liegt in der Epoche mit der Nummer {{{{{nr}}}}}. Sie heißt {{{{Mittelalter}}}}. Die Epoche mit der Nummer 3 heißt {{{{Antike}}}}.",
                s, extra=["Neuzeit", "5"],
                info="Die Reihenfolge ist: 1 Ur- und Frühgeschichte, 2 Altertum, 3 Antike, 4 Mittelalter, 5 Neuzeit. Das Mittelalter reicht von 500 bis 1500 n. Chr.",
                bild=svg_epochen(nummern=True, jahre=True, namen_unten=False), bildAlt=alt_epochen())),
        ("M", [ref(P2B, "Die Epoche eines Jahres bestimmen"), ref(P2A, "Jahrhunderte bestimmen")],
         kurz("Eine griechische Sonnenuhr stammt aus dem 3. Jahrhundert v. Chr. In welcher Epoche war das? Nimm die Epochen aus dem Heft.",
              ["Antike", "die Antike"], s,
              info="Das 3. Jahrhundert v. Chr. sind die Jahre 200 bis 299 v. Chr. Das liegt zwischen 1000 v. Chr. und 500 n. Chr., also in der Antike.")),
        ("M", [ref(P2A, "Jahre vergleichen und Abstände berechnen"), ref(P5A, "Haustiere: Domestikation und Züchtung")],
         reihenfolge("Sortiere diese fünf Erfindungen und Ereignisse vom ältesten zum jüngsten.",
                     ["Der Hund wird zum Haustier (vor ca. 14 000 Jahren)",
                      "Esel und Pferd werden als Reit- und Packtiere genutzt (ab ca. 5000 v. Chr.)",
                      "Das Rad wird erfunden (um 3000 v. Chr.)",
                      "Eine griechische Sonnenuhr entsteht (3. Jahrhundert v. Chr.)",
                      "In Deutschland gibt es mechanische Uhren (um 1400)"],
                     s, info="Vor ca. 14 000 Jahren ist etwa 12 000 v. Chr. Danach folgen 5000 v. Chr., 3000 v. Chr., das 3. Jahrhundert v. Chr. und um 1400 n. Chr. Bei Jahren vor Christi Geburt ist die größere Zahl das ältere Jahr.")),
        ("S", [ref(P2A, "Warum teilt man die Zeit ein?"), ref(P2B, "Wofür ein Zeitstrahl gut ist")],
         frei("Ein Freund sagt: „Ich schätze einfach nach Gefühl, wie lange etwas her ist. Dafür brauche ich keine Uhr und keinen Kalender.“ Widersprich ihm mit zwei Gründen, warum man die Zeit misst und einteilt.",
              "Das Gefühl für Zeit täuscht: Manchmal vergeht sie wie im Flug, manchmal gar nicht. Mit Uhren, Kalendern und Zeitstrahlen kann man sich zeitlich orientieren und Ereignisse in die richtige Reihenfolge bringen.",
              ["Das Gefühl für die Dauer der Zeit ist unsicher (mal vergeht sie schnell, mal langsam).",
               "Man misst und teilt die Zeit ein, um sich zeitlich zu orientieren (zum Beispiel mit Uhr, Kalender, Zeitstrahl oder Epochen)."],
              2, s)),
    ]


def teil_c():
    s = abschnitt("C")
    reihe = ("S", "L", "M")        # von links nach rechts: Schimpanse, Lucy, moderner Mensch (mit Namen beschriftet)
    return [
        ("L", ref(P3, "Schimpanse, Lucy und Mensch im Vergleich"),
         mc("Wähle alle richtigen Antworten. Sieh dir die Zeichnung an. Welche Aussagen passen dazu?",
            ["Lucy steht aufrechter als der Schimpanse.", "Der moderne Mensch steht ganz aufrecht."],
            ["Lucy steht genauso aufrecht wie der moderne Mensch.", "Der Schimpanse steht aufrechter als Lucy."],
            s, info="Der Schimpanse ist stark nach vorn gebeugt, Lucy ist nur noch leicht nach vorn geneigt und der moderne Mensch steht ganz aufrecht.",
            bild=svg_drei(reihe, "namen"), bildAlt=alt_drei_namen(reihe))),
        ("L", ref(P3, "Lucy: der Fund"),
         luecke("Ergänze die Sätze über Lucys Fundort.",
                "Lucy wurde 1974 bei Hadar in {{Äthiopien}} gefunden. Gefunden hat sie eine amerikanisch-{{französische}} Forschergruppe.",
                s, extra=["Tansania", "deutsche"],
                info="Das Buch nennt als Fundort Hadar in Äthiopien (Ostafrika). Die Forschergruppe war amerikanisch-französisch. Laetoli in Tansania ist der Fundort der Fußspuren.")),
        ("M", ref(P3, "Der aufrechte Gang und seine Folgen"),
         mc("Eine Gruppe von Vormenschen zieht durch die Savanne. Eines der Tiere trägt Früchte in beiden Händen nach Hause. Welchen Vorteil des aufrechten Gangs nutzt es?",
            "Die Hände sind frei zum Tragen.",
            ["Man hat eine bessere Sicht.", "Man braucht weniger Energie.", "Man ist besser vor Kälte geschützt."],
            s, info="Wer aufrecht geht, hat die Hände frei und kann Nahrung oder Gegenstände tragen. Bessere Sicht und weniger Energie sind die beiden anderen Vorteile.")),
        ("S", [ref(P3, "Wie sah Lucy aus?"), ref(P3, "Schimpanse, Lucy und Mensch im Vergleich")],
         frei("Du arbeitest in einem Museum und schreibst ein Schild für Lucys Skelett. Es soll erklären, warum Lucy zwischen Schimpanse und Mensch steht. Schreibe zwei bis drei Sätze.",
              "Lucy sah wahrscheinlich eher wie ein Schimpanse aus. Sie ging aber vorwiegend aufrecht wie ein Mensch, das erkennt man am Knochenbau und an Fußspuren. Deshalb gehört sie zu den Vormenschen auf dem Weg zum Menschen.",
              ["Aussehen: Lucy sah wahrscheinlich eher wie ein Schimpanse aus.",
               "Gang: Lucy ging vorwiegend aufrecht wie ein Mensch (Knochenbau, Fußspuren)."],
              2, s)),
    ]


def teil_d():
    s = abschnitt("D")
    # Der Speer reicht höchstens 5-mal so weit wie die Lanze (15 m gegen 3 m)
    w = {n: (a, b) for n, a, b in WAFFEN}
    mal = w["Speer"][1] // w["Lanze"][1]
    assert w["Speer"][1] % w["Lanze"][1] == 0 and mal == 5 and w["Lanze"] == (0, 3) and w["Speer"] == (0, 15)
    return [
        ("L", ref(P4A, "Die Steinzeit in Teile gliedern"),
         mc("Ein Mitschüler schreibt: „Die Steinzeit endete nach dem Heft um 9000 v. Chr.“ Was ist daran falsch?",
            "Um 9000 v. Chr. endete nur die Altsteinzeit, die ganze Steinzeit erst um 3000 v. Chr.",
            ["Die Steinzeit endete erst um 1000 v. Chr., zu Beginn der Antike, also viel später.",
             "Nichts, denn Altsteinzeit und Jungsteinzeit endeten nach dem Heft beide um 9000 v. Chr.",
             "Das Heft nennt für das Ende der Steinzeit gar keine Jahreszahl, nur für den Beginn."],
            s, info="Nach dem Heft dauerte die Altsteinzeit bis etwa 9000 v. Chr. Dann folgte die Jungsteinzeit bis etwa 3000 v. Chr. Erst damit endete die Steinzeit.")),
        ("L", ref(P4A, "Die Eiszeit: Klima und Landschaft"),
         tf("Zur größten Ausdehnung der Gletscher in der Eiszeit war sogar die Gegend um Berlin von Eis bedeckt.", True, s,
            info="In der Eiszeit dehnten sich die Gletscher weit aus. Zur größten Ausdehnung reichte das Eis bis über die Gegend um Berlin.")),
        ("L", ref(P4B, "Waffen und ihre Reichweiten"),
         kurz("Wie viel Mal so weit wie die Lanze reicht der Speer höchstens? Schreibe die Zahl.",
              [str(mal), "fünf", f"{mal}-mal", f"{mal} mal", "fünfmal", "das fünffache", f"{mal}-fach", f"{mal}fach"], s,
              info="Die Lanze reicht 0 bis 3 m, der Speer 0 bis 15 m. Die größte Reichweite des Speers ist 15 : 3 = 5-mal so groß.")),
        ("L", ref(P4B, "Feuer nutzen und selbst machen"),
         mc("Wähle alle richtigen Antworten. Was gilt für das Feuer in der Altsteinzeit?",
            ["Am Anfang konnten die Menschen Feuer nur hüten und nutzen, etwa nach einem Blitzschlag.",
             "Später erzeugten sie Feuer selbst, etwa durch Reibung zweier Hölzer."],
            ["Die ersten Menschen konnten das Feuer von Anfang an ganz allein selbst erzeugen.",
             "Das Feuer gab es erst seit der Jungsteinzeit, davor kannte man es nicht."],
            s, info="Feuer nutzen konnte man seit etwa 1,5 Millionen Jahren. Selbst erzeugen konnte man es erst viel später, durch Reibung zweier Hölzer oder Funkenschlag von Feuersteinen.")),
        ("M", [ref(P4B, "Unterwegs leben: nicht sesshaft"), ref(P4B, "Jagen und Sammeln: wovon die Menschen lebten")],
         frei("Eine Gruppe von Jägern und Sammlern der Altsteinzeit will das ganze Jahr an einem Platz bleiben und feste Häuser bauen. Erkläre, warum das für sie nicht gut gehen würde. Schreibe zwei bis drei Sätze.",
              "Die Menschen lebten vom Jagen und Sammeln und hatten keinen Ackerbau und keine Viehzucht. Die Beutetiere zogen weiter, und das Nahrungsangebot wechselte mit der Jahreszeit. Deshalb mussten sie ihre Lagerplätze wechseln und in Zelten wohnen.",
              ["Sie lebten vom Jagen und Sammeln, nicht von Ackerbau und Viehzucht.",
               "Die Beutetiere zogen weiter und das Nahrungsangebot wechselte mit der Jahreszeit.",
               "Deshalb wechselten sie die Lagerplätze und wohnten in Zelten (nicht sesshaft)."],
              3, s)),
    ]


def teil_e():
    s = abschnitt("E")
    # Keramik seit ca. 7000 v. Chr., Rad um 3000 v. Chr.: beide vor Christi Geburt, man zieht ab
    k, r = -7000, -3000
    abstand = spanne(k, r)
    assert abstand == 4000
    return [
        ("L", [ref(P5B, "Spinnen, Weben, Töpfern und Mahlen"), ref(P5B, "Beil, Pflug und Rad")],
         kurz("Wie lange nach dem Beginn der Keramik wurde das Rad erfunden? Schreibe die Zahl der Jahre.",
              [str(abstand), f"{abstand} Jahre", "4.000", "4.000 Jahre", "4 000", "4 000 Jahre"], s, einheit="Jahre",
              info=f"Keramik gibt es seit etwa {jahr(k)}, das Rad wurde um {jahr(r)} erfunden. Beide Jahre liegen vor Christi Geburt, man zieht ab: {abs(k)} − {abs(r)} = {abstand} Jahre.")),
        ("L", [ref(P5B, "Spinnen, Weben, Töpfern und Mahlen"), ref(P5B, "Beil, Pflug und Rad")],
         mc("Wähle alle richtigen Antworten. Was kam erst in der Jungsteinzeit auf?",
            ["Der Mahlstein zum Mahlen von Getreide", "Der Webstuhl mit Gewichten"],
            ["Die Harpune aus Knochen oder Geweih", "Die Speerschleuder zum Werfen von Speeren"],
            s, info="Mahlstein und Webstuhl sind Erfindungen der Jungsteinzeit. Harpune und Speerschleuder kannten schon die Jäger und Sammler der Altsteinzeit.")),
        ("M", ref(P5B, "Altsteinzeit und Jungsteinzeit im Vergleich"),
         zuordnen("Ordne jede Lebensweise der richtigen Zeit zu.",
                  [("Die Gruppe folgte den Rentierherden und zog weiter.", "Altsteinzeit"),
                   ("Wer Töpfe brauchte, ging zum Töpfer im Dorf.", "Jungsteinzeit"),
                   ("Auf dem Feld wuchs Getreide, auf der Weide grasten Schafe.", "Jungsteinzeit")],
                  s, info="Wer den Herden folgt, ist nicht sesshaft (Altsteinzeit). Berufe wie der Töpfer, Felder und Weiden gehören zu den sesshaften Bauern der Jungsteinzeit.")),
        ("S", [ref(P5B, "Vorteile und Nachteile abwägen"), ref(P5B, "Folgen der neuen Lebensweise")],
         frei("Mit der neolithischen Revolution wurden die Menschen sesshaft und lebten als Bauern. Ein Bauer der Jungsteinzeit sagt: „Mein Leben ist viel sicherer als das der Jäger.“ Gib ihm in einem Punkt recht und widersprich ihm in einem anderen Punkt.",
              "Recht hat er, weil er Vorräte hat, in einem festen Haus wohnt und Tiere zu halten weniger gefährlich ist als jagen. Widersprechen kann man, weil bei einem Ernteausfall Hunger droht und der Besitz zu Neid und Streit führt.",
              ["Er hat in einem Punkt recht (zum Beispiel Vorräte, festes Haus, Tiere halten ist weniger gefährlich als jagen).",
               "Man kann ihm widersprechen (zum Beispiel Hunger bei Ernteausfall, Neid und Streit um Besitz, einseitige Ernährung)."],
              2, s)),
    ]


def teil_f():
    s = abschnitt("F")
    return [
        ("L", ref(P6, "Kleidung und Ausrüstung"),
         kurz("Zu Ötzis Ausrüstung gehörte ein Kupferbeil. Wie viele Zentimeter lang war es etwa? Schreibe die Zahl.",
              ["60", "60 cm", "60 Zentimeter"], s, einheit="cm",
              info="Das Beil war etwa 60 cm lang, die Klinge aus gegossenem Kupfer und der Schaft aus Eibenholz. Es ist das einzige vollständig erhaltene Beil aus der Vorgeschichte auf der ganzen Welt.")),
        ("M", ref(P6, "Der Fund im Eis"),
         mc("Ein Ehepaar fand Ötzi 1991 in den Ötztaler Alpen. Das Buch nennt für Ötzis Alter etwa 5250 Jahre, eine Kopie etwa 5400 Jahre. Was kannst du daraus sicher sagen?",
            "Ötzi ist mehr als 5000 Jahre alt, das passt zu beiden.",
            ["Eines der beiden Bücher ist falsch, das andere stimmt genau.",
             "Ötzi ist genau 5325 Jahre alt, das ist der Mittelwert.",
             "Über Ötzis Alter kann man deshalb gar nichts sagen."],
            s, info="Das Alter lässt sich nur ungefähr bestimmen, deshalb weichen die Zahlen leicht ab. Sicher ist: mehr als 5000 Jahre.")),
        ("L", ref(P6, "Ötzi wurde getötet"),
         tf("Ötzi starb an der tiefen Schnittwunde in seiner rechten Hand.", False, s,
            info="Ötzi verblutete, nachdem ihn eine Pfeilspitze in der linken Schulter getroffen hatte. Die Schnittwunde an der rechten Hand deutet auf einen Nahkampf kurz vorher.")),
        ("M", [ref(P6, "Wer war Ötzi?"), ref(P6, "Belegt oder vermutet? Quelle oder Darstellung?")],
         mc("Welche Aussage über Ötzi ist durch die Untersuchung seines Körpers belegt und nicht nur vermutet?",
            "Ötzi hatte sich früher einmal das Nasenbein gebrochen.",
            ["Ötzi war vor seinen Verfolgern geflohen.",
             "Der Täter kannte Ötzi von früheren Begegnungen her.",
             "Ötzi wollte zu Verwandten auf der anderen Seite des Passes."],
            s, info="Ein verheilter Nasenbeinbruch ist ein Befund am Körper und damit belegt. Warum Ötzi unterwegs war und wer ihn tötete, weiß man nicht.")),
        ("S", ref(P6, "Belegt oder vermutet? Quelle oder Darstellung?"),
         frei("Der Arzt Egarter-Vigl hat 2011 die letzten Minuten von Ötzi beschrieben. Ist sein Text eine Quelle oder eine Darstellung? Begründe deine Antwort.",
              "Der Text ist eine Darstellung. Der Arzt hat ihn viel später geschrieben und war nicht dabei. Er stützt sich auf Untersuchungen und Funde, und das sind die Quellen.",
              ["Der Text ist eine Darstellung und keine Quelle.",
               "Begründung: Er wurde viel später von jemandem geschrieben, der nicht dabei war, und stützt sich auf Funde und Untersuchungen (die Quellen)."],
              2, s)),
    ]


def aufgaben_mit_meta():
    """[(Teil, Schwierigkeit, lesen, Aufgabe)] in der Reihenfolge der Probearbeit (noch ohne Nummer in der Frage)."""
    out = []
    for k, f in zip("ABCDEF", (teil_a, teil_b, teil_c, teil_d, teil_e, teil_f)):
        for schw, lesen, t in f():
            out.append((k, schw, lesen, t))
    return out


def build(pakete):
    byid = {p["id"]: p for p in pakete}

    def titel_da(paket_id, titel):
        return paket_id in byid and any(s["titel"] == titel for s in byid[paket_id].get("lernblatt", []))

    meta = aufgaben_mit_meta()
    A = []
    summen = {}
    for n, (k, schw, lesen, t) in enumerate(meta, 1):
        assert schw in ("L", "M", "S")
        assert t["abschnitt"].startswith(f"Teil {k} "), (k, t["abschnitt"])
        pt = punkte_von(t)
        summen[k] = summen.get(k, 0) + pt
        t["frage"] = f"Aufgabe {n}: {t['frage']}" + (f" ({pt} Punkte)" if pt > 1 else "")
        # Nachlesen: jede Aufgabe verweist auf Abschnitte der Übungspakete (Paket und Titel müssen es geben)
        for r in (lesen if isinstance(lesen, list) else [lesen]):
            assert titel_da(r["paket"], r["titel"]), f"Verweis ins Leere: {r}"
        t["lesen"] = lesen
        A.append(t)
    # Die Überschriften nennen die Punkte; sie müssen zur Summe passen
    assert summen == {k: v[1] for k, v in TEILE.items()}, summen
    assert sum(summen.values()) == GESAMT == sum(punkte_von(t) for t in A)
    for t in A:
        k = t["abschnitt"][5]
        assert f"({summen[k]} Punkte)" in t["abschnitt"], t["abschnitt"]
    teile_txt = ", ".join(f"{k} {TEILE[k][0]} {TEILE[k][1]}" for k in "ABCDEF")
    p = pack(ID, "Geschichte Klasse 6: Probearbeit (Quellen, Zeit, Lucy, Steinzeit, Ötzi)",
             f"Eigene Probearbeit mit {GESAMT} Punkten in sechs Teilen ({teile_txt}), 45 Minuten mit Timer, Buch und Heft zu. Alle Aufgaben sind neu. Wo Punkte fehlen, geh in das passende Übungspaket zurück.",
             None, A,
             hinweis="Das ist nicht die Klassenarbeit deines Lehrers, sondern eine eigene Probearbeit unter Prüfungsbedingungen. Der Lehrer hat keine Form vorgegeben, deshalb sind Aufbau, Punkte und Zeit selbst festgelegt. "
                     "Lege Buch und Heft weg und vergleiche erst am Ende mit den Lösungen. Die Familie Berger ist erfunden. Welche Note es für welche Punktzahl gibt, bestimmt dein Lehrer.")
    p["ueben"] = False   # kein Übungsmodus, nur proben wie in der Schule
    return p
