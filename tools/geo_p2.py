"""Geografie Klasse 6, Teil 2: Gezeiten (Punkte 5 bis 7 des Wissenschecks)."""
from geo_lib import *

TIDE = 745  # 12 Stunden und 25 Minuten in Minuten


def runde_halbe_stunde(minuten):
    """Auf eine halbe Stunde runden (wie beim Ablesen der Kurve)."""
    return int(round(minuten / 30.0)) * 30


def uhr(minuten):
    """Uhrzeit für Antwortmöglichkeiten: 5:00 Uhr (ohne führende Null)."""
    m = int(round(minuten)) % 1440
    return f"{m // 60}:{m % 60:02d} Uhr"


KURVEN = [
    # (Hochwasser am Morgen in Minuten, Hochwasser in m, Niedrigwasser in m, Name)
    dict(t=300, hw=3.5, nw=1.0, name="Kurve A"),
    dict(t=450, hw=3.0, nw=0.5, name="Kurve B"),
    dict(t=90, hw=2.5, nw=0.5, name="Kurve C"),
]


def kurven_aufgaben(abschnitt):
    out = []
    for k in KURVEN:
        t_hw, hw, nw = k["t"], k["hw"], k["nw"]
        bild = svg_kurve(t_hw, hw, nw)
        alt = f"Gezeitenkurve eines Tages (0 bis 24 Uhr), waagerecht die Uhrzeit, senkrecht der Wasserstand in Metern ({k['name']})."
        nw_nach = t_hw + TIDE / 2          # Niedrigwasser nach dem ersten Hochwasser
        hw_zwei = t_hw + TIDE
        assert hw_zwei < 1440 and nw_nach < 1440
        # Wert an den Stellen kontrollieren
        assert abs(kurve_h(t_hw, t_hw, hw, nw) - hw) < 1e-9
        assert abs(kurve_h(nw_nach, t_hw, hw, nw) - nw) < 1e-9
        # a) erstes Hochwasser (auf halbe Stunde genau)
        a = runde_halbe_stunde(t_hw)
        opts_falsch = [uhr(a + 360), uhr(a + 180), uhr(a - 180 if a >= 180 else a + 540)]
        assert len({uhr(a), *opts_falsch}) == 4
        out.append(mc(f"Lies die Gezeitenkurve ab ({k['name']}): Um wie viel Uhr ist das erste Hochwasser des Tages? (Auf eine halbe Stunde genau.)",
                      uhr(a), opts_falsch, abschnitt, bild=bild, bildAlt=alt,
                      info="Das Hochwasser ist der Gipfel der Kurve, der höchste Wasserstand."))
        # b) Niedrigwasser danach
        b = runde_halbe_stunde(nw_nach)
        opts_falsch_b = [uhr(b + 180), uhr(b - 180), uhr(a)]
        assert len({uhr(b), *opts_falsch_b}) == 4
        out.append(mc(f"({k['name']}) Um wie viel Uhr ist das Niedrigwasser nach dem ersten Hochwasser? (Auf eine halbe Stunde genau.)",
                      uhr(b), opts_falsch_b, abschnitt, bild=bild, bildAlt=alt,
                      info="Das Niedrigwasser ist das Tal der Kurve, der tiefste Wasserstand."))
        # c) Wasserstand bei Hochwasser
        out.append(kurz(f"({k['name']}) Wie hoch steht das Wasser bei Hochwasser?", [de(hw), str(hw)], abschnitt, einheit="m", bild=bild, bildAlt=alt,
                        tipp="Lies am Gipfel der Kurve die Höhe an der linken Achse ab."))
        # d) Wasserstand bei Niedrigwasser
        out.append(kurz(f"({k['name']}) Wie hoch steht das Wasser bei Niedrigwasser?", [de(nw), str(nw)], abschnitt, einheit="m", bild=bild, bildAlt=alt))
        # e) Tidenhub
        th = round(hw - nw, 1)
        out.append(kurz(f"({k['name']}) Berechne den Tidenhub.", [de(th), str(th)], abschnitt, einheit="m", bild=bild, bildAlt=alt,
                        info=f"Tidenhub = Hochwasser − Niedrigwasser = {de(hw)} m − {de(nw)} m = {de(th)} m."))
        # f) Flut oder Ebbe zu einer Uhrzeit
        fallend = int(round((t_hw + nw_nach) / 2 / 60.0)) * 60      # Stunde mitten zwischen HW und NW (Ebbe)
        steigend = int(round((nw_nach + hw_zwei) / 2 / 60.0)) * 60  # mitten zwischen NW und HW (Flut)
        assert kurve_h(fallend + 1, t_hw, hw, nw) < kurve_h(fallend - 1, t_hw, hw, nw)
        assert kurve_h(steigend + 1, t_hw, hw, nw) > kurve_h(steigend - 1, t_hw, hw, nw)
        out.append(mc(f"({k['name']}) Was ist um {fallend // 60} Uhr: Ebbe oder Flut?", "Ebbe", ["Flut", "Hochwasser", "Niedrigwasser"], abschnitt, bild=bild, bildAlt=alt,
                      info="Wo die Kurve fällt, läuft das Wasser ab: Das ist Ebbe."))
        out.append(mc(f"({k['name']}) Was ist um {steigend // 60} Uhr: Ebbe oder Flut?", "Flut", ["Ebbe", "Hochwasser", "Niedrigwasser"], abschnitt, bild=bild, bildAlt=alt,
                      info="Wo die Kurve steigt, kommt das Wasser zurück: Das ist Flut."))
    return out


def kalender_aufgaben(t0, abschnitt, ort="Beispielhafen"):
    tab, svg, alt = kalender_svg(t0)
    alt = f"Tidenkalender für {ort}. " + alt
    out = []
    hw1 = [d[0] for d in tab]
    # a) erstes Hochwasser am 2. Tag
    out.append(kurz(f"Lies den Tidenkalender von {ort} ab: Wann ist am 2. Tag das erste Hochwasser? (Schreibe die Uhrzeit so: 04:05)",
                    [hhmm(hw1[1]), hhmm(hw1[1]).lstrip('0')], abschnitt, bild=svg, bildAlt=alt))
    # b) zweites Niedrigwasser am 1. Tag
    out.append(kurz(f"Wann ist am 1. Tag das zweite Niedrigwasser? (Schreibe die Uhrzeit so: 04:05)", [hhmm(tab[0][3]), hhmm(tab[0][3]).lstrip('0')], abschnitt, bild=svg, bildAlt=alt))
    # c) Strich
    dash = [(d, spalte) for d, row in enumerate(tab) for spalte, v in enumerate(row) if v is None]
    assert len(dash) == 1, dash
    d, sp = dash[0]
    spalte = {1: "zweiten Hochwasser", 2: "ersten Niedrigwasser", 3: "zweiten Niedrigwasser"}[sp]
    out.append(mc(f"Am {d + 1}. Tag steht beim {spalte} ein Strich (–). Erkläre, warum.",
                  "An diesem Tag gibt es nur einmal Hochwasser oder Niedrigwasser, weil sich die Zeiten täglich nach hinten verschieben und das nächste erst nach Mitternacht kommt.",
                  ["Die Uhrzeit war nicht zu erkennen.", "Das Wasser hat an diesem Tag Pause gemacht.", "Der Mond war an diesem Tag nicht da."], abschnitt, bild=svg, bildAlt=alt,
                  info="Die Gezeiten verschieben sich jeden Tag um etwa 50 Minuten nach hinten. Darum fällt manchmal ein Hoch- oder Niedrigwasser erst auf den nächsten Tag."))
    # d) Zeit zwischen erstem HW und erstem NW danach (am 1. Tag)
    a, nw_after = tab[0][0], [x for x in (tab[0][2], tab[0][3]) if x is not None and x > tab[0][0]][0]
    diff = nw_after - a
    out.append(kurz(f"Berechne am 1. Tag die Zeit vom ersten Hochwasser bis zum Niedrigwasser danach, in Minuten.", [str(diff)], abschnitt, einheit="Minuten", bild=svg, bildAlt=alt,
                    info=f"{hhmm(nw_after)} Uhr − {hhmm(a)} Uhr = {stunden_min(diff)} = {diff} Minuten."))
    h, m = divmod(diff, 60)
    out.append(mc(f"Berechne am 1. Tag die Zeit vom ersten Hochwasser ({hhmm(a)} Uhr) bis zum Niedrigwasser danach ({hhmm(nw_after)} Uhr).",
                  stunden_min(diff), [stunden_min(diff + 60), stunden_min(diff - 60), stunden_min(diff + 90)], abschnitt, bild=svg, bildAlt=alt,
                  info=f"{hhmm(nw_after)} Uhr − {hhmm(a)} Uhr = {stunden_min(diff)}."))
    # e) Verschiebung
    out.append(kurz("Um wie viele Minuten verschiebt sich das erste Hochwasser vom 1. auf den 2. Tag?", [str(hw1[1] - hw1[0])], abschnitt, einheit="Minuten", bild=svg, bildAlt=alt,
                    info=f"{hhmm(hw1[1])} Uhr − {hhmm(hw1[0])} Uhr = {hw1[1] - hw1[0]} Minuten."))
    assert hw1[1] - hw1[0] == 50
    # f) Voraussage
    out.append(kurz(f"Rechne ohne den Kalender: Am 1. Tag ist das erste Hochwasser um {hhmm(hw1[0])} Uhr. Wann ist es etwa am 3. Tag, wenn es sich täglich um 50 Minuten verschiebt? (Schreibe die Uhrzeit so: 04:05)",
                    [hhmm(hw1[2]), hhmm(hw1[2]).lstrip('0')], abschnitt, bild=svg, bildAlt=alt,
                    info=f"{hhmm(hw1[0])} Uhr + 2 × 50 Minuten = {hhmm(hw1[2])} Uhr."))
    assert hw1[2] == hw1[0] + 100
    # g) Hafen bei Hochwasser
    out.append(mc(f"Der Hafen von {ort} fällt bei Ebbe trocken. Krabbenfischer Jensen kann am 1. Tag nur um die Zeit des Hochwassers auslaufen. Um welche Uhrzeit kann er auslaufen?",
                  f"um {hhmm(tab[0][0])} Uhr oder um {hhmm(tab[0][1])} Uhr", [f"um {hhmm(tab[0][2])} Uhr oder um {hhmm(tab[0][3])} Uhr", f"nur um {hhmm(tab[0][0])} Uhr", "zu jeder Uhrzeit"], abschnitt, bild=svg, bildAlt=alt,
                  info="Bei Niedrigwasser ist im Hafen zu wenig Wasser. Der Hafen ist dann zweimal am Tag nicht zu erreichen."))
    # h) Anzahl Hochwasser
    out.append(kurz("Wie oft ist am 1. Tag Hochwasser?", ["2", "zweimal"], abschnitt, bild=svg, bildAlt=alt))
    for t in out:
        if ort not in t["frage"]:
            t["frage"] = f"({ort}) {t['frage']}"
    return out


def lernblatt_alle():
    return [
        lb("So entstehen die Gezeiten",
           "- Der **Mond** zieht mit seiner **Anziehungskraft** das Wasser der Erde an. Auf der Seite, die dem Mond zugewandt ist, entsteht ein „Wasserberg“. Dort ist **Flut**.\n"
           "- Erde und Mond drehen sich um einen gemeinsamen **Schwerpunkt**. Er liegt nicht genau in der Mitte, sondern näher an der Erde, weil die Erde viel schwerer ist als der Mond. Wie bei einer Wippe: Die schwere Person muss näher an der Mitte sitzen, damit die Wippe im Gleichgewicht ist.\n"
           "- Durch die Drehung entsteht die **Fliehkraft**. Dreht sich eine Wippe, fliegen lange Haare nach außen. So wird auch auf der Seite der Erde, die vom Mond abgewandt ist, das Wasser nach außen gedrückt. Auch dort entsteht ein Wasserberg und somit Flut.\n"
           "- Die Erde dreht sich einmal am Tag um ihre Achse unter den beiden Wasserbergen hindurch. Darum gibt es an der Küste **zweimal Flut und zweimal Ebbe** am Tag. Von einer Flut bis zur nächsten vergehen etwa **12 Stunden und 25 Minuten**.\n"
           "- Zusatzwissen: Auch die Sonne zieht am Wasser, aber der Mond hat den größeren Einfluss.",
           merke="Die Anziehungskraft des Mondes (zugewandte Seite) und die Fliehkraft (abgewandte Seite) lassen zwei Wasserberge entstehen, also zwei Fluten gleichzeitig. An den Seiten dazwischen ist Ebbe.",
           bild=svg_gezeiten(False), bildAlt="Skizze: Die Erde mit zwei Wasserbergen (Flut), dazwischen Ebbe. Rechts der Mond mit der Anziehungskraft, links die Fliehkraft der Erde."),
        lb("Wichtige Begriffe",
           "- **Gezeiten (Tide)**: das Wechselspiel von Ebbe und Flut.\n"
           "- **Ebbe**: Das Wasser läuft ab, der Wasserstand sinkt (etwa 6 Stunden).\n"
           "- **Flut**: Das Wasser läuft auf, der Wasserstand steigt (etwa 6 Stunden).\n"
           "- **Niedrigwasser (NW)**: der niedrigste Wasserstand, am Ende der Ebbe.\n"
           "- **Hochwasser (HW)**: der höchste Wasserstand, am Ende der Flut.\n"
           "- **Tidenhub**: der Höhenunterschied zwischen Hochwasser und Niedrigwasser. An der deutschen Nordseeküste beträgt er etwa 3 bis 4 m.",
           merke="In 12 Stunden und 25 Minuten hebt und senkt sich der Meeresspiegel einmal: erst Ebbe bis zum Niedrigwasser, dann Flut bis zum Hochwasser. Der Tidenhub ist der Unterschied dazwischen."),
        lb("Der Tidenhub ist nicht überall gleich",
           "- **Bristol (England)**: 12 m. Das ist für Schiffe ein Problem. Man baute einen neuen Hafen direkt an der Küste.\n"
           "- **Saint-Malo (Frankreich)**: 11 m. Das ist groß genug für ein Gezeitenkraftwerk.\n"
           "- **Bremerhaven**: 4 m. Das behindert die Schifffahrt. Man baute einen Hafen mit Schleusen.\n"
           "- **Hallig Langeneß**: 3 m. Die Häuser stehen auf **Warften** (aufgeschütteten Hügeln), damit sie nicht überschwemmt werden.\n"
           "- **Rostock (Ostsee)**: Gezeiten spürt man kaum.\n"
           "- **Warum sind die Gezeiten in der Ostsee so schwach?** Die Flutwelle läuft von Norden in die Nordsee, an der englischen, niederländischen und deutschen Küste entlang und läuft bei Dänemark aus. Nur ein kleiner Teil strömt um Dänemark herum in die Ostsee. Die dänischen Inseln stehen im Weg und verringern die Flutwelle weiter."),
        lb("Gezeitenkurve lesen",
           "- Die **Gezeitenkurve** zeigt den Wasserstand an einem Tag. Waagerecht steht die **Uhrzeit**, senkrecht der **Wasserstand** in Metern.\n"
           "- Wo die Kurve **steigt**, ist **Flut**. Wo die Kurve **fällt**, ist **Ebbe**.\n"
           "- Der **Gipfel** der Kurve ist das **Hochwasser**. Das **Tal** ist das **Niedrigwasser**.\n"
           "- Den **Tidenhub** liest du ab, indem du den Wasserstand bei Niedrigwasser vom Wasserstand bei Hochwasser abziehst.\n"
           "- Beispiel in der Zeichnung: Hochwasser um 5 Uhr mit 3,5 m, Niedrigwasser gegen 11 Uhr mit 1 m. Der Tidenhub ist 3,5 m − 1 m = 2,5 m. Vom Hochwasser bis zum Niedrigwasser vergehen etwa 6 Stunden.",
           bild=svg_kurve(300, 3.5, 1.0), bildAlt="Gezeitenkurve eines Tages: Hochwasser um 5 Uhr bei 3,5 m, Niedrigwasser gegen 11 Uhr bei 1 m, Hochwasser gegen 17:30 Uhr."),
        lb("Tidenkalender lesen",
           "- Der **Tidenkalender** ist eine Tabelle mit den Uhrzeiten von Hochwasser und Niedrigwasser für jeden Tag. Suche die Zeile des Tages und lies in der richtigen Spalte die Uhrzeit ab.\n"
           "- Ein **Strich (–)** bedeutet: An diesem Tag gibt es in der Spalte keine Uhrzeit, weil das nächste Hoch- oder Niedrigwasser erst nach Mitternacht kommt.\n"
           "- **Zeit zwischen Hoch- und Niedrigwasser berechnen**: späterer Zeitpunkt minus früherer Zeitpunkt. Beispiel: 10:18 Uhr − 04:05 Uhr = 6 Stunden und 13 Minuten.\n"
           "- **Warum verschieben sich die Zeiten jeden Tag?** Der Mond umrundet die Erde in etwa 28 Tagen. Wenn sich die Erde nach 24 Stunden einmal gedreht hat, ist der Mond auf seiner Bahn ein Stück weitergewandert. Die Erde braucht dann noch etwa **50 Minuten**, bis sie ihn „eingeholt“ hat. Deshalb verschieben sich die Gezeiten jeden Tag um etwa 50 Minuten.\n"
           "- Ein **tideabhängiger Hafen** fällt bei Niedrigwasser trocken. Schiffe können dort nur um die Zeit des Hochwassers ein- und auslaufen.",
           merke="Tag für Tag etwa 50 Minuten später: Das erste Hochwasser von heute 04:05 Uhr ist morgen etwa um 04:55 Uhr.",
           bild=kalender_svg(245)[1], bildAlt="Tidenkalender (Beispiel): " + kalender_svg(245)[2]),
    ]


def aufgaben_alle():
    A = []
    # ------------------------------------------------------------------ A Entstehung
    s = "A – So entstehen die Gezeiten"
    A += [
        mc("Wodurch entstehen die Gezeiten vor allem?", "durch die Anziehungskraft des Mondes", ["durch den Wind", "durch Regen und Flüsse", "durch die Wellen der Schiffe"], s),
        mc("Welche zwei Kräfte lassen die zwei Wasserberge entstehen?", ["Anziehungskraft des Mondes", "Fliehkraft"], ["Windkraft", "Reibungskraft"], s,
           info="Die Anziehungskraft des Mondes wirkt auf der zugewandten Seite, die Fliehkraft auf der abgewandten Seite."),
        tf("Auf der Seite der Erde, die dem Mond zugewandt ist, entsteht ein Wasserberg.", True, s),
        tf("Auf der Seite der Erde, die vom Mond abgewandt ist, entsteht auch ein Wasserberg.", True, s, info="Dort drückt die Fliehkraft das Wasser nach außen."),
        tf("Der gemeinsame Schwerpunkt von Erde und Mond liegt genau in der Mitte zwischen beiden.", False, s,
           info="Er liegt näher an der Erde, weil die Erde viel schwerer ist als der Mond."),
        mc("Warum liegt der gemeinsame Schwerpunkt näher an der Erde?", "Weil die Erde viel schwerer ist als der Mond.", ["Weil die Erde schneller ist.", "Weil der Mond kleiner aussieht.", "Weil das Meer die Erde festhält."], s),
        mc("Womit vergleicht man den gemeinsamen Schwerpunkt von Erde und Mond im Unterricht?", "mit einer Wippe", ["mit einem Fahrstuhl", "mit einem Staubsauger", "mit einem Trampolin"], s,
           info="Auf einer Wippe sitzt die schwere Person näher an der Mitte, damit die Wippe im Gleichgewicht ist."),
        mc("Wo entsteht durch die Fliehkraft ein Wasserberg?", "auf der Seite der Erde, die vom Mond abgewandt ist", ["auf der Seite der Erde, die dem Mond zugewandt ist", "nur am Nordpol", "nur im Ostseeraum"], s),
        kurz("Wie oft am Tag gibt es an der Küste Flut?", ["2", "zweimal", "2 mal", "2x"], s, einheit="mal", info="Die Erde dreht sich einmal am Tag unter den beiden Wasserbergen hindurch."),
        kurz("Wie oft am Tag gibt es an der Küste Ebbe?", ["2", "zweimal", "2 mal", "2x"], s, einheit="mal"),
        mc("Wie lange dauert es von einer Flut bis zur nächsten Flut etwa?", "12 Stunden und 25 Minuten", ["6 Stunden und 12 Minuten", "24 Stunden", "28 Tage"], s),
        tf("Auch die Sonne beeinflusst die Gezeiten, aber der Mond hat den größeren Einfluss.", True, s),
        luecke("Ergänze den Text zur Entstehung der Gezeiten.",
               "Der {{Mond}} zieht mit seiner {{Anziehungskraft}} das Wasser an. Auf der abgewandten Seite drückt die {{Fliehkraft}} das Wasser nach außen. Es entstehen {{zwei}} Wasserberge, an der Küste also zweimal {{Flut}} und zweimal {{Ebbe}} am Tag.",
               s, extra=["Wind", "drei"]),
        reihenfolge("Bringe die Entstehung der Gezeiten in die richtige Reihenfolge.",
                    ["Der Mond zieht mit seiner Anziehungskraft das Wasser an, ein Wasserberg entsteht",
                     "Erde und Mond drehen sich um einen gemeinsamen Schwerpunkt",
                     "Die Fliehkraft drückt das Wasser auf der abgewandten Seite nach außen, ein zweiter Wasserberg entsteht",
                     "Die Erde dreht sich einmal am Tag unter den Wasserbergen hindurch: zweimal Flut, zweimal Ebbe"], s),
        luecke("Beschrifte die Skizze. Welcher Begriff gehört zu welcher Nummer? (Die Nummern 4 und 5 kommen jeweils zweimal vor.)",
               "(1) {{Mond}}\n(2) {{Anziehungskraft des Mondes|Anziehungskraft}}\n(3) {{Erde}}\n(4) {{Flut|Flut (Wasserberg)|Wasserberg}}\n(5) {{Ebbe}}\n(6) {{Fliehkraft der Erde|Fliehkraft}}",
               s, extra=["Sonne", "Hochwasser"], bild=svg_gezeiten(True), bildAlt="Skizze der Gezeiten mit den Nummern 1 bis 6: Mond, Anziehungskraft, Erde, zwei Fluten, zwei Ebben, Fliehkraft",
               tipp="Bei den Wasserbergen ist Flut, an den Seiten dazwischen Ebbe."),
        luecke("Noch eine Skizze (der Mond ist hier links). Beschrifte sie.",
               "(1) {{Mond}}\n(2) {{Anziehungskraft des Mondes|Anziehungskraft}}\n(3) {{Erde}}\n(4) {{Flut|Flut (Wasserberg)|Wasserberg}}\n(5) {{Ebbe}}\n(6) {{Fliehkraft der Erde|Fliehkraft}}",
               s, extra=["Sonne", "Niedrigwasser"], bild=svg_gezeiten(True, False), bildAlt="Skizze der Gezeiten, der Mond links, mit den Nummern 1 bis 6"),
        mc("Wo ist an der Erde gleichzeitig Flut?", "auf der dem Mond zugewandten und auf der abgewandten Seite", ["nur auf der dem Mond zugewandten Seite", "nur an den Seiten zwischen den Wasserbergen", "nirgendwo"], s,
           bild=svg_gezeiten(False), bildAlt="Erde mit zwei Wasserbergen"),
        frei("Erkläre in drei bis vier Sätzen, wie die Gezeiten entstehen.",
             "Der Mond zieht mit seiner Anziehungskraft das Wasser der Erde an, auf der dem Mond zugewandten Seite entsteht ein Wasserberg und dort ist Flut. Erde und Mond drehen sich um einen gemeinsamen Schwerpunkt, der näher an der Erde liegt, weil die Erde schwerer ist. Durch die Drehung entsteht die Fliehkraft, sie drückt das Wasser auf der abgewandten Seite nach außen und es entsteht ein zweiter Wasserberg. Die Erde dreht sich einmal am Tag unter den beiden Wasserbergen hindurch, deshalb gibt es zweimal am Tag Flut und zweimal Ebbe.",
             ["Der Mond zieht das Wasser an (Anziehungskraft)", "Wasserberg auf der zugewandten Seite = Flut", "Fliehkraft auf der abgewandten Seite, zweiter Wasserberg", "Die Erde dreht sich unter den Wasserbergen hindurch: zweimal Flut und zweimal Ebbe am Tag"], 4, s),
        frei("Erkläre mit dem Bild einer Wippe, warum der gemeinsame Schwerpunkt von Erde und Mond näher an der Erde liegt.",
             "Bei einer Wippe muss die schwere Person näher an der Mitte sitzen, damit die Wippe im Gleichgewicht ist. Die Erde ist viel schwerer als der Mond. Darum liegt der gemeinsame Schwerpunkt näher an der Erde.",
             ["Die schwere Person sitzt näher an der Mitte", "Die Erde ist viel schwerer als der Mond", "Der Schwerpunkt liegt deshalb näher an der Erde"], 2, s),
    ]
    # ------------------------------------------------------------------ B Begriffe
    s = "B – Wichtige Begriffe"
    A += [
        zuordnen("Ordne dem Begriff die richtige Bedeutung zu.",
                 [("Ebbe", "Das Wasser läuft ab, der Wasserstand sinkt."), ("Flut", "Das Wasser läuft auf, der Wasserstand steigt."), ("Hochwasser", "höchster Wasserstand, am Ende der Flut"),
                  ("Niedrigwasser", "niedrigster Wasserstand, am Ende der Ebbe"), ("Tidenhub", "Höhenunterschied zwischen Hochwasser und Niedrigwasser")], s),
        kurz("Wie nennt man den niedrigsten Wasserstand?", ["Niedrigwasser", "NW"], s),
        kurz("Wie nennt man den höchsten Wasserstand?", ["Hochwasser", "HW"], s),
        kurz("Wie nennt man den Höhenunterschied zwischen Hochwasser und Niedrigwasser?", ["Tidenhub", "der Tidenhub"], s),
        mc("Was bedeutet Ebbe?", "Das Wasser läuft ab und der Wasserstand sinkt.", ["Das Wasser steigt.", "Das Meer ist ganz zugefroren.", "Es gibt einen Sturm."], s),
        mc("Was bedeutet Flut?", "Das Wasser läuft auf und der Wasserstand steigt.", ["Das Wasser sinkt.", "Das Watt fällt trocken.", "Es regnet viel."], s),
        mc("Was ist am Ende der Ebbe?", "Niedrigwasser", ["Hochwasser", "Flut", "Sturmflut"], s),
        mc("Was ist am Ende der Flut?", "Hochwasser", ["Niedrigwasser", "Ebbe", "Tidenhub"], s),
        mc("Wie lange dauert Ebbe oder Flut etwa?", "etwa 6 Stunden", ["etwa 1 Stunde", "etwa 12 Stunden", "etwa 24 Stunden"], s),
        mc("Wie groß ist der Tidenhub an der deutschen Nordseeküste etwa?", "etwa 3 bis 4 m", ["etwa 30 cm", "etwa 12 m", "etwa 100 m"], s),
        mc("Was bedeutet das Wort „Gezeiten“ (Tide)?", "das Wechselspiel von Ebbe und Flut", ["ein starker Sturm", "ein Hafen", "die Uhrzeit des Sonnenaufgangs"], s),
        tf("Am Ende der Flut ist Niedrigwasser.", False, s, info="Am Ende der Flut ist Hochwasser."),
        tf("Bei Ebbe sinkt der Wasserstand.", True, s),
        tf("Der Tidenhub ist der Unterschied zwischen Hochwasser und Niedrigwasser.", True, s),
        luecke("Ergänze die Begriffe.",
               "Bei {{Ebbe}} läuft das Wasser ab, bei {{Flut}} kommt es zurück. Den höchsten Wasserstand nennt man {{Hochwasser}}, den niedrigsten {{Niedrigwasser}}. Der Unterschied zwischen beiden heißt {{Tidenhub}}.",
               s, extra=["Sturmflut", "Brandung"]),
        reihenfolge("Bringe den Ablauf der Gezeiten in die richtige Reihenfolge (Start: Hochwasser).",
                    ["Hochwasser: Das Wasser steht am höchsten", "Ebbe: Das Wasser läuft ab", "Niedrigwasser: Das Wasser steht am tiefsten", "Flut: Das Wasser kommt zurück"], s),
        frei("Erkläre in je einem Satz die Begriffe Ebbe, Flut und Tidenhub.",
             "Ebbe: Das Wasser läuft ab und der Wasserstand sinkt. Flut: Das Wasser läuft auf und der Wasserstand steigt. Tidenhub: Das ist der Höhenunterschied zwischen Hochwasser und Niedrigwasser.",
             ["Ebbe richtig erklärt", "Flut richtig erklärt", "Tidenhub richtig erklärt"], 3, s),
    ]
    # ------------------------------------------------------------------ C Tidenhub an verschiedenen Orten
    s = "C – Der Tidenhub an verschiedenen Orten"
    orte = [("Bristol (England)", 12), ("Saint-Malo (Frankreich)", 11), ("Bremerhaven", 4), ("Hallig Langeneß", 3)]
    A += [
        zuordnen("Ordne dem Ort den Tidenhub zu.", [("Bristol (England)", "12 m"), ("Saint-Malo (Frankreich)", "11 m"), ("Bremerhaven", "4 m"), ("Hallig Langeneß", "3 m"), ("Rostock (Ostsee)", "kaum spürbar")], s),
        mc("An welchem Ort ist der Tidenhub am größten?", "Bristol", ["Bremerhaven", "Hallig Langeneß", "Rostock"], s),
        mc("An welchem Ort spürt man die Gezeiten kaum?", "Rostock", ["Bristol", "Saint-Malo", "Bremerhaven"], s),
        kurz("Wie groß ist der Tidenhub in Bremerhaven?", ["4", "4 m"], s, einheit="m"),
        kurz("Wie viel größer ist der Tidenhub in Bristol (12 m) als in Bremerhaven (4 m)?", [str(12 - 4), f"{12 - 4} m"], s, einheit="m", info="12 m − 4 m = 8 m"),
        kurz("Wie viel größer ist der Tidenhub in Bremerhaven (4 m) als auf der Hallig Langeneß (3 m)?", [str(4 - 3), f"{4 - 3} m"], s, einheit="m", info="4 m − 3 m = 1 m"),
        kurz("Wie viel größer ist der Tidenhub in Bristol (12 m) als in Saint-Malo (11 m)?", [str(12 - 11), f"{12 - 11} m"], s, einheit="m", info="12 m − 11 m = 1 m"),
        zuordnen("Welche Folge hat der große Tidenhub an dem Ort?",
                 [("Bristol", "Man baute einen neuen Hafen direkt an der Küste."), ("Saint-Malo", "Der Tidenhub ist groß genug für ein Gezeitenkraftwerk."),
                  ("Bremerhaven", "Man baute einen Hafen mit Schleusen."), ("Hallig Langeneß", "Die Häuser stehen auf Warften.")], s),
        mc("Warum stehen auf der Hallig Langeneß die Häuser auf Warften?", "Damit sie nicht überschwemmt werden.", ["Damit man weit aufs Meer sehen kann.", "Damit die Schafe Platz haben.", "Weil der Boden dort aus Eis besteht."], s),
        tf("Ein Gezeitenkraftwerk braucht einen großen Tidenhub.", True, s, info="Saint-Malo mit 11 m Tidenhub ist ein Beispiel."),
        tf("Der Tidenhub ist überall auf der Erde gleich groß.", False, s),
        mc("Welche Aussage über Bremerhaven stimmt?", "Der Tidenhub von etwa 4 m behindert die Schifffahrt, deshalb gibt es einen Hafen mit Schleusen.", ["Dort gibt es keine Gezeiten.", "Dort liegt der Tidenhub bei 12 m.", "Dort baute man ein Gezeitenkraftwerk."], s),
        luecke("Ergänze: Warum sind die Gezeiten in der Ostsee so schwach?",
               "Die Flutwelle läuft von {{Norden}} in die {{Nordsee}} und läuft bei {{Dänemark}} aus. Nur ein {{kleiner}} Teil strömt um Dänemark herum in die Ostsee. Die dänischen {{Inseln}} stehen im Weg.",
               s, extra=["Süden", "großer"]),
        mc("Warum sind die Gezeiten in der Ostsee so schwach?", "Die Flutwelle kommt nur durch eine enge Passage und die dänischen Inseln verringern sie weiter.", ["Es gibt in der Ostsee keinen Mond.", "Das Wasser ist zu kalt für Gezeiten.", "Die Ostsee ist zu tief."], s),
        frei("Erkläre, warum es in der Ostsee kaum Gezeiten gibt.",
             "Die Flutwelle läuft von Norden in die Nordsee, an der englischen, niederländischen und deutschen Küste entlang und bei Dänemark wieder hinaus. Nur ein kleiner Teil strömt um Dänemark herum in die Ostsee, und die dänischen Inseln stehen im Weg und verringern die Flutwelle weiter.",
             ["Nur ein kleiner Teil der Flutwelle gelangt in die Ostsee", "Die dänischen Inseln stehen im Weg", "Deshalb sind die Gezeiten sehr schwach"], 2, s),
    ]
    # ------------------------------------------------------------------ D Gezeitenkurve
    s = "D – Die Gezeitenkurve lesen"
    A += kurven_aufgaben(s)
    A += [
        mc("Woran erkennst du in der Gezeitenkurve die Flut?", "Die Kurve steigt.", ["Die Kurve fällt.", "Die Kurve ist ganz oben.", "Die Kurve ist ganz unten."], s, bild=svg_kurve(300, 3.5, 1.0), bildAlt="Gezeitenkurve"),
        mc("Woran erkennst du in der Gezeitenkurve das Hochwasser?", "Am Gipfel der Kurve.", ["Am Tal der Kurve.", "Am Anfang der Kurve.", "Dort, wo die Kurve steigt."], s, bild=svg_kurve(300, 3.5, 1.0), bildAlt="Gezeitenkurve"),
        kurz("Wie viele Stunden vergehen vom Hochwasser bis zum nächsten Niedrigwasser etwa?", ["6", "6 Stunden"], s, einheit="Stunden", bild=svg_kurve(300, 3.5, 1.0), bildAlt="Gezeitenkurve mit Hochwasser um 5 Uhr und Niedrigwasser gegen 11 Uhr",
             info="Genau sind es 6 Stunden und etwa 12 Minuten."),
    ]
    A += [
        zuordnen("Ordne zu, was an dieser Stelle der Gezeitenkurve gilt.", [("Gipfel der Kurve", "Hochwasser"), ("Tal der Kurve", "Niedrigwasser"), ("Die Kurve steigt", "Flut"), ("Die Kurve fällt", "Ebbe")], s),
        luecke("Ergänze den Text zur Gezeitenkurve.", "Auf der Gezeitenkurve steht waagerecht die {{Uhrzeit}} und senkrecht der {{Wasserstand}}. Der Gipfel ist das {{Hochwasser}}, das Tal das {{Niedrigwasser}}.",
               s, extra=["Tidenhub", "Windstärke"]),
        reihenfolge("So liest du den Tidenhub aus der Kurve ab. Bringe die Schritte in die richtige Reihenfolge.",
                    ["Den Gipfel der Kurve suchen und den Wasserstand ablesen (Hochwasser)", "Das Tal der Kurve suchen und den Wasserstand ablesen (Niedrigwasser)",
                     "Den Wasserstand bei Niedrigwasser vom Wasserstand bei Hochwasser abziehen", "Das Ergebnis ist der Tidenhub"], s),
        tf("Wo die Gezeitenkurve fällt, ist Ebbe.", True, s),
        tf("Im Tal der Gezeitenkurve ist Hochwasser.", False, s, info="Im Tal der Kurve ist Niedrigwasser."),
        mc("Wie viele Gipfel (Hochwasser) hat die Gezeitenkurve an diesem Tag?", "zwei", ["einen", "drei", "keinen"], s, bild=svg_kurve(300, 3.5, 1.0), bildAlt="Gezeitenkurve mit zwei Gipfeln um 5 Uhr und gegen 17:30 Uhr"),
    ]
    # ------------------------------------------------------------------ E Tidenkalender
    s = "E – Der Tidenkalender"
    A += [
        tf("Ein Strich (–) im Tidenkalender bedeutet: An diesem Tag gibt es in dieser Spalte keine Uhrzeit.", True, s),
        luecke("Ergänze den Satz zum Tidenkalender.", "Im Tidenkalender stehen die {{Uhrzeiten}} von Hochwasser und {{Niedrigwasser}}. Jeden Tag verschieben sie sich um etwa {{50}} Minuten nach {{hinten}}.",
               s, extra=["Wassertemperaturen", "vorn"]),
        zuordnen("Was bedeutet das?", [("Strich (–) im Tidenkalender", "an diesem Tag keine Uhrzeit in der Spalte"), ("tideabhängiger Hafen", "fällt bei Niedrigwasser trocken"),
                                        ("Tidenhub", "Höhenunterschied zwischen Hochwasser und Niedrigwasser")], s),
    ]
    A += kalender_aufgaben(245, s)
    A += kalender_aufgaben(140, s, ort="Beispielstadt")
    # ------------------------------------------------------------------ F Rechnen mit den Gezeiten
    s = "F – Warum sich die Gezeiten verschieben"
    A += [
        mc("Um wie viele Minuten verschieben sich die Gezeiten jeden Tag etwa?", "um etwa 50 Minuten nach hinten", ["um etwa 5 Minuten nach vorn", "um etwa 3 Stunden nach hinten", "gar nicht"], s),
        mc("Warum verschieben sich die Gezeiten jeden Tag?",
           "Der Mond wandert in 24 Stunden ein Stück weiter, die Erde braucht noch etwa 50 Minuten, bis sie ihn eingeholt hat.",
           ["Die Erde dreht sich jeden Tag langsamer.", "Der Wind schiebt das Wasser weiter.", "Die Sonne geht jeden Tag später auf."], s),
        kurz("Wie lange braucht der Mond für einen Umlauf um die Erde ungefähr? (in Tagen)", ["28", "28 Tage"], s, einheit="Tage"),
        kurz("Heute ist um 06:10 Uhr Hochwasser. Wann ist das nächste Hochwasser ungefähr? (12 Stunden und 25 Minuten später, Schreibweise: 04:05)", [hhmm(6 * 60 + 10 + TIDE)], s,
             info="06:10 Uhr + 12 Stunden und 25 Minuten = 18:35 Uhr."),
        kurz("Heute ist um 08:30 Uhr Hochwasser. Wann ist das nächste Hochwasser ungefähr? (12 Stunden und 25 Minuten später, Schreibweise: 04:05)", [hhmm(8 * 60 + 30 + TIDE)], s,
             info="08:30 Uhr + 12 Stunden und 25 Minuten = 20:55 Uhr."),
        kurz("Heute ist um 11:05 Uhr Hochwasser. Wann ist das nächste Hochwasser ungefähr? (12 Stunden und 25 Minuten später, Schreibweise: 04:05)", [hhmm(11 * 60 + 5 + TIDE)], s,
             info="11:05 Uhr + 12 Stunden und 25 Minuten = 23:30 Uhr."),
        kurz("Heute ist um 07:00 Uhr Hochwasser. Etwa 6 Stunden und 12 Minuten später ist Niedrigwasser. Wann? (Schreibweise: 04:05)", [hhmm(7 * 60 + 372)], s,
             info="07:00 Uhr + 6 Stunden und 12 Minuten = 13:12 Uhr."),
        frei("Erkläre, warum sich die Gezeiten jeden Tag verschieben.",
             "Der Mond umrundet die Erde in etwa 28 Tagen. Wenn sich die Erde nach 24 Stunden einmal gedreht hat, ist der Mond auf seiner Bahn ein Stück weitergewandert. Die Erde braucht dann noch etwa 50 Minuten, bis sie ihn eingeholt hat. Deshalb verschieben sich die Gezeiten jeden Tag um etwa 50 Minuten.",
             ["Der Mond umrundet die Erde in etwa 28 Tagen", "Der Mond wandert in 24 Stunden ein Stück weiter", "Die Erde braucht noch etwa 50 Minuten, bis sie ihn eingeholt hat"], 3, s),
        frei("Juist hat einen tideabhängigen Hafen. Krabbenfischer Jensen kann nur zu bestimmten Zeiten mit seinem Kutter auslaufen. Erkläre, warum.",
             "Bei Niedrigwasser ist im Hafen zu wenig Wasser, der Hafen ist dann zweimal am Tag nicht zu erreichen. Jensen kann nur um die Zeit des Hochwassers auslaufen.",
             ["Bei Niedrigwasser ist zu wenig Wasser im Hafen", "Er kann nur um die Zeit des Hochwassers auslaufen"], 2, s),
    ]
    return A


def split_aufgaben():
    """Teilt die Aufgaben nach Abschnitten: Grundlagen (A bis C) und Kurve/Kalender (D bis F)."""
    alle = aufgaben_alle()
    a = [t for t in alle if t["abschnitt"][0] in "ABC"]
    b = [t for t in alle if t["abschnitt"][0] in "DEF"]
    assert len(a) + len(b) == len(alle)
    return a, b


def build():
    lb_alle = lernblatt_alle()
    a, b = split_aufgaben()
    p1 = pack("geografie-2a-gezeiten-grundlagen", "Geografie Teil 2a: Gezeiten – Grundlagen",
              "Wie die Gezeiten entstehen, wichtige Begriffe und der Tidenhub an verschiedenen Orten. Mit Lernblatt und vielen Übungsaufgaben.",
              lb_alle[:3], a, min_aufgaben=45)
    p2 = pack("geografie-2b-gezeiten-kurve-kalender", "Geografie Teil 2b: Gezeiten – Kurve und Tidenkalender",
              "Die Gezeitenkurve und den Tidenkalender lesen, rechnen und erklären, warum sich die Gezeiten täglich verschieben. Mit Lernblatt und sehr vielen Übungsaufgaben.",
              lb_alle[3:], b, min_aufgaben=50,
              hinweis="Die Tidenkalender in den Aufgaben sind selbst erfundene Beispiele (kein echter Ort). Die Uhrzeiten beim Ablesen der Kurve gelten auf eine halbe Stunde genau.")
    return [p1, p2]
