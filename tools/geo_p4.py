"""Geografie Klasse 6, Teil 4: Küstenschutz (Punkte 11 bis 13 des Wissenschecks): Deich, Dünen, Sieltor."""
from geo_lib import *
from geo_svg2 import svg_duene, svg_siel, svg_siel_paar, svg_deichprofile

NAMEN = ["Seeseite", "Landseite", "Deichkrone", "Grasdecke", "Klei", "Sandkern", "Deichfuß", "Sturmflutwasserstand", "Hochwasser"]
PERM_A = (3, 1, 5, 2, 7, 4, 6, 9, 8)
PERM_B = (2, 6, 1, 8, 4, 9, 3, 5, 7)
for _p in (PERM_A, PERM_B):
    assert sorted(_p) == list(range(1, 10))

H1599, H1766, HHEUTE = 3.0, 5.1, 8.8
assert round(H1766 - H1599, 1) == 2.1 and round(HHEUTE - H1766, 1) == 3.7 and round(HHEUTE - H1599, 1) == 5.8

ALT_DEICH = "Querschnitt durch einen Deich mit dem Meer auf einer und dem Land auf der anderen Seite"
ALT_PROFILE = "Drei Deichprofile nebeneinander mit den Jahren 1599, 1766 und heute und den Höhen etwa 3 m, 5,1 m und 8,8 m"
ALT_DUENE = "Querschnitt durch Strand und Düne mit Strandhafer, dessen Wurzeln tief in die Düne reichen, und Wind vom Meer"
ALT_SIEL = "Querschnitt durch einen Deich mit Sieltor: Meer auf der einen, Land (Marsch) auf der anderen Seite des Deichs"


def nr(name, perm):
    return perm[NAMEN.index(name)]


# =====================================================================  Lernblatt Deich


def lernblatt_deich():
    return [
        lb("Der Deich: Aufgabe und Teile",
           "Ein **Deich** ist ein langer Wall aus Erde an der Küste. An der deutschen Nordseeküste, an den Flussmündungen und auf den Inseln gibt es zusammen etwa **1500 Kilometer** davon. Der Deich schützt das Land dahinter, die **Marsch** (das flache Land hinter dem Deich), vor Überflutung. Am wichtigsten ist das bei einer **Sturmflut**, wenn das Wasser viel höher steigt als bei normalem Hochwasser. Den höchsten Stand dabei nennt man **Sturmflutwasserstand**.\n"
           "- **Seeseite**: die Seite zum Meer. Sie ist **flach**, damit die Wellen daran hochlaufen und dabei ihre Kraft verlieren.\n"
           "- **Landseite**: die Seite zur Marsch. Hier müssen keine Wellen abgehalten werden, deshalb ist sie **steiler**.\n"
           "- **Deichkrone**: der höchste Punkt oben auf dem Deich.\n"
           "- **Deichfuß**: der Rand ganz unten. Hier treffen die Wellen zuerst auf. Steine schützen ihn, damit das Wasser ihn nicht aushöhlt und wegspült.",
           merke="Seeseite flach, Landseite steil, oben die Deichkrone, unten der Deichfuß aus Steinen.",
           bild=svg_deich(False), bildAlt="Querschnitt durch einen Deich mit allen beschrifteten Teilen: Seeseite, Landseite, Deichkrone, Grasdecke, Klei, Sandkern, Deichfuß, Sturmflutwasserstand und Hochwasser"),
        lb("Woraus besteht ein Deich?",
           "Von innen nach außen:\n"
           "- **Sandkern**: der Kern des Deichs.\n"
           "- **Klei**: eine Schicht aus festem Lehm darüber. Sie schützt den Kern.\n"
           "- **Grasdecke**: die oberste Schicht. Die Graswurzeln halten die Erde zusammen, sodass Wellen, Wind und Regen den Deich nicht abtragen.\n"
           "- **Schafe** gehören zum Deich: Sie halten das Gras kurz und dicht, und mit ihren Hufen drücken sie den Boden fest.\n"
           "Im Wissenscheck zeichnest du zuerst die Form (Seeseite flach, Landseite steil) und beschriftest dann alle Teile.",
           merke="Innen Sandkern, darüber Klei, außen Grasdecke, am Deichfuß Steine."),
        lb("Deiche werden höher: die Deichprofile",
           "Über die Jahrhunderte haben die Menschen die Deiche immer wieder erhöht und verbreitert, damit sie höhere Sturmfluten aushalten. Das Buch (S. 128, M2) zeigt drei Querschnitte:\n"
           "- **1599**: etwa 3 m hoch\n"
           "- **1766**: etwa 5,1 m hoch\n"
           "- **heute**: etwa 8,8 m hoch\n"
           "Der heutige Deich ist also etwa 5,8 m höher als der von 1599 (8,8 m − 3 m) und viel breiter. Die Breiten sind in der Zeichnung nur ungefähr gezeichnet.",
           merke="1599 etwa 3 m, 1766 etwa 5,1 m, heute etwa 8,8 m: Deiche wurden immer höher und breiter.",
           bild=svg_deichprofile(True), bildAlt=ALT_PROFILE),
    ]


# =====================================================================  Aufgaben Deich


def beschriftung_aufgaben(s):
    out = []
    # a) Standardnummerierung, Lückentext mit allen neun Teilen
    img = svg_deich(True, True, tuple(range(1, 10)))
    teile = ", ".join(f"({i + 1}) {{{{{n}}}}}" for i, n in enumerate(NAMEN))
    out.append(luecke("Beschrifte den Deich. Welches Wort gehört zu welcher Nummer?", teile.replace(", (", "\n("), s,
                      extra=["Düne", "Siel"], bild=img, bildAlt=ALT_DEICH + " mit den Nummern 1 bis 9",
                      tipp="Die Seeseite ist die flache Seite. Die Deichkrone ist die höchste Stelle.",
                      info="1 Seeseite, 2 Landseite, 3 Deichkrone, 4 Grasdecke, 5 Klei, 6 Sandkern, 7 Deichfuß, 8 Sturmflutwasserstand, 9 Hochwasser."))
    # b) andere Nummerierung, Zuordnen
    img_b = svg_deich(True, True, PERM_A)
    paare = sorted(((f"Nummer {nr(n, PERM_A)}", n) for n in NAMEN), key=lambda p: int(p[0].split()[1]))
    out.append(zuordnen("Ordne die Nummern den Teilen des Deichs zu.", paare, s, bild=img_b, bildAlt=ALT_DEICH + " mit neu verteilten Nummern 1 bis 9"))
    # c) gespiegelt, andere Nummern
    img_c = svg_deich(True, False, PERM_B)
    paare_c = sorted(((f"Nummer {nr(n, PERM_B)}", n) for n in NAMEN), key=lambda p: int(p[0].split()[1]))
    out.append(zuordnen("Hier liegt das Meer rechts. Ordne die Nummern den Teilen des Deichs zu.", paare_c, s, bild=img_c,
                        bildAlt=ALT_DEICH + ", das Meer liegt rechts, mit den Nummern 1 bis 9",
                        tipp="Die flache Seite zeigt immer zum Meer, die steile Seite zum Land."))
    # d) Multiple-Choice zu einzelnen Teilen mit Bild
    fragen = [
        ("Deichkrone", PERM_A, True, "Welche Nummer zeigt die Deichkrone?"),
        ("Sandkern", PERM_A, True, "Welche Nummer zeigt den Sandkern?"),
        ("Seeseite", PERM_B, True, "Welche Nummer zeigt die Seeseite?"),
        ("Klei", PERM_B, True, "Welche Nummer zeigt den Klei?"),
        ("Deichfuß", PERM_A, False, "Das Meer liegt hier rechts. Welche Nummer zeigt den Deichfuß?"),
        ("Landseite", PERM_B, False, "Das Meer liegt hier rechts. Welche Nummer zeigt die Landseite?"),
        ("Sturmflutwasserstand", PERM_B, True, "Welche Nummer zeigt den Sturmflutwasserstand?"),
        ("Grasdecke", PERM_A, False, "Das Meer liegt hier rechts. Welche Nummer zeigt die Grasdecke?"),
    ]
    for name, perm, links, frage in fragen:
        bild = svg_deich(True, links, perm)
        richtig = str(nr(name, perm))
        andere = [str(x) for x in range(1, 10) if str(x) != richtig]
        falsch = [andere[(i * 3 + perm[0]) % len(andere)] for i in range(3)]
        falsch = list(dict.fromkeys(falsch))
        while len(falsch) < 3:
            falsch.append(next(x for x in andere if x not in falsch))
        assert richtig not in falsch and len(set(falsch)) == 3
        out.append(mc(frage, richtig, falsch, s, bild=bild, bildAlt=ALT_DEICH + (", das Meer liegt links" if links else ", das Meer liegt rechts") + ", mit Nummern",
                      mischen=True))
    # e) Beschriftung mit Wortbank, gespiegelt
    img_d = svg_deich(True, False, PERM_A)
    teile = "\n".join(f"({nr(n, PERM_A)}) {{{{{n}}}}}" for n in sorted(NAMEN, key=lambda n: nr(n, PERM_A)))
    out.append(luecke("Das Meer liegt hier rechts. Beschrifte den Deich noch einmal.", teile, s, extra=["Düne", "Priel"], bild=img_d,
                      bildAlt=ALT_DEICH + ", das Meer liegt rechts, mit den Nummern 1 bis 9"))
    return out


def rechen_aufgaben(s):
    out = []
    bild = svg_deichprofile(True)
    out.append(kurz("Wie hoch war der Deich im Jahr 1599?", [de(H1599), str(H1599), "3"], s, einheit="m", bild=bild, bildAlt=ALT_PROFILE))
    out.append(kurz("Wie hoch ist der Deich heute?", [de(HHEUTE), str(HHEUTE)], s, einheit="m", bild=bild, bildAlt=ALT_PROFILE))
    out.append(kurz("Um wie viele Meter war der Deich von 1766 höher als der Deich von 1599?", [de(H1766 - H1599), str(round(H1766 - H1599, 1))], s, einheit="m",
                    info=f"{de(H1766)} m − {de(H1599)} m = {de(H1766 - H1599)} m", bild=bild, bildAlt=ALT_PROFILE))
    out.append(kurz("Um wie viele Meter ist der heutige Deich höher als der Deich von 1766?", [de(HHEUTE - H1766), str(round(HHEUTE - H1766, 1))], s, einheit="m",
                    info=f"{de(HHEUTE)} m − {de(H1766)} m = {de(HHEUTE - H1766)} m", bild=bild, bildAlt=ALT_PROFILE))
    out.append(kurz("Um wie viele Meter ist der heutige Deich höher als der Deich von 1599?", [de(HHEUTE - H1599), str(round(HHEUTE - H1599, 1))], s, einheit="m",
                    info=f"{de(HHEUTE)} m − {de(H1599)} m = {de(HHEUTE - H1599)} m", bild=bild, bildAlt=ALT_PROFILE))
    out.append(kurz(f"Ein Deich ist {de(H1599)} m hoch und wird um {de(H1766 - H1599)} m erhöht. Wie hoch ist er dann?", [de(H1766), str(H1766)], s, einheit="m",
                    info=f"{de(H1599)} m + {de(H1766 - H1599)} m = {de(H1766)} m"))
    out.append(kurz(f"Ein Deich ist {de(H1766)} m hoch. Um wie viele Meter muss er erhöht werden, damit er so hoch ist wie der heutige Deich ({de(HHEUTE)} m)?",
                    [de(HHEUTE - H1766), str(round(HHEUTE - H1766, 1))], s, einheit="m", info=f"{de(HHEUTE)} m − {de(H1766)} m = {de(HHEUTE - H1766)} m"))
    # Sturmflut-Beispiele (erfundene Wasserstände)
    for hoehe in (6.4, 7.5, 5.9):
        diff = round(HHEUTE - hoehe, 1)
        assert diff > 0
        out.append(kurz(f"Beispiel: Bei einer Sturmflut steigt das Wasser auf {de(hoehe)} m. Wie viele Meter fehlen bis zur Deichkrone des heutigen Deichs ({de(HHEUTE)} m)?",
                        [de(diff), str(diff)], s, einheit="m", info=f"{de(HHEUTE)} m − {de(hoehe)} m = {de(diff)} m"))
    for hoehe in (6.4, 7.5):
        diff = round(hoehe - H1766, 1)
        assert diff > 0
        out.append(kurz(f"Beispiel: Das Wasser einer Sturmflut steht {de(hoehe)} m hoch. Um wie viele Meter wäre es höher als die Krone des Deichs von 1766 ({de(H1766)} m)?",
                        [de(diff), str(diff)], s, einheit="m", info=f"{de(hoehe)} m − {de(H1766)} m = {de(diff)} m. Der alte Deich würde überflutet."))
    out.append(tf(f"Eine Sturmflut mit {de(6.4)} m Wasserstand würde über den Deich von 1766 laufen.", 6.4 > H1766, s, info="Der Deich von 1766 war nur etwa 5,1 m hoch."))
    out.append(tf(f"Eine Sturmflut mit {de(6.4)} m Wasserstand würde über den heutigen Deich laufen.", 6.4 > HHEUTE, s, info="Der heutige Deich ist etwa 8,8 m hoch."))
    out.append(reihenfolge("Ordne die Deiche nach ihrer Höhe, vom niedrigsten zum höchsten.", ["Deich von 1599", "Deich von 1766", "heutiger Deich"], s))
    out.append(mc("Welche Aussage über die Deichprofile stimmt?", "Die Deiche wurden im Lauf der Jahrhunderte höher und breiter.",
                  ["Die Deiche wurden niedriger und schmaler.", "Alle drei Deiche sind gleich hoch.", "Der älteste Deich ist der höchste."], s, bild=bild, bildAlt=ALT_PROFILE))
    return out


def aufgaben_deich():
    A = []
    s = "A – Wozu gibt es Deiche?"
    A += [
        tf("Ein Deich schützt das Land hinter ihm vor Überflutung.", True, s),
        tf("Entlang der deutschen Nordseeküste gibt es etwa 1500 Kilometer Deiche.", True, s),
        tf("Deiche gibt es nur an der Ostsee.", False, s, info="Deiche gibt es an der Nordseeküste, an den Trichtermündungen der Flüsse und auf den Inseln."),
        mc("Was schützt ein Deich?", "das Land dahinter, die Marsch", ["das Watt", "das offene Meer", "die Schiffe im Hafen"], s),
        mc("Was ist eine Sturmflut?", "ein Hochwasser, bei dem das Wasser viel höher steigt als normal", ["eine besonders niedrige Ebbe", "ein starker Regen", "Wellen ohne Wind"], s),
        mc("Wie nennt man das flache Land hinter dem Deich?", "Marsch", ["Watt", "Düne", "Salzwiese"], s),
        kurz("Wie viele Kilometer Deiche gibt es etwa an der deutschen Nordseeküste?", ["1500", "1500 km"], s, einheit="km"),
        mc("Wo gibt es Deiche?", ["entlang der deutschen Nordseeküste", "auf den Inseln", "an den Trichtermündungen der Flüsse"], ["mitten im Hochgebirge", "in der Sahara"], s),
        luecke("Ergänze den Text.", "Ein {{Deich}} schützt das Land hinter ihm, die {{Marsch}}, vor Überflutung. Besonders wichtig ist er bei einer {{Sturmflut}}, weil das Wasser dann viel höher steigt als beim normalen {{Hochwasser}}.",
               s, extra=["Ebbe", "Düne"]),
        mc("Welches Wort passt: Der höchste Wasserstand bei einer Sturmflut heißt …", "Sturmflutwasserstand", ["Tidenhub", "Niedrigwasser", "Deichfuß"], s),
        frei("Erkläre in zwei Sätzen, wozu ein Deich gebaut wird.",
             "Ein Deich ist ein langer Erdwall an der Küste. Er schützt das Land dahinter vor Überflutung, vor allem bei einer Sturmflut.",
             ["Deich schützt das Land (Marsch)", "Vor Überflutung oder Sturmflut genannt"], 2, s),
    ]
    s = "B – Aufbau und Teile des Deichs"
    A += [
        mc("Welche Seite des Deichs ist flach?", "die Seeseite", ["die Landseite", "beide gleich", "die Deichkrone"], s),
        mc("Welche Seite des Deichs ist steiler?", "die Landseite", ["die Seeseite", "beide gleich", "der Deichfuß"], s),
        mc("Warum ist die Seeseite flach?", "Die Wellen laufen auf und verlieren ihre Kraft.", ["Damit Schafe besser grasen können.", "Damit man dort baden kann.", "Damit das Wasser schneller abfließt."], s),
        mc("Warum kann die Landseite steiler sein?", "Sie muss keine Wellen abhalten.", ["Weil dort mehr Platz ist.", "Weil dort die Sonne scheint.", "Weil dort Steine liegen."], s),
        mc("Wie heißt die höchste Stelle des Deichs?", "Deichkrone", ["Deichfuß", "Seeseite", "Klei"], s),
        mc("Woraus besteht der Deichfuß?", "aus Steinen", ["aus Gras", "aus Sand", "aus Holz"], s),
        mc("Warum liegen am Deichfuß Steine?", "Hier treffen die Wellen zuerst auf den Deich. Die Steine verhindern, dass der Fuß ausgehöhlt und weggespült wird.", ["Damit die Schafe nicht herunterfallen.", "Damit der Deich schöner aussieht.", "Damit das Meer salziger wird."], s),
        mc("Was liegt im Inneren des Deichs?", "der Sandkern", ["der Klei", "die Grasdecke", "die Krone"], s),
        mc("Was liegt über dem Sandkern?", "eine Schicht aus Klei", ["die Deichkrone", "eine Schicht aus Steinen", "das Watt"], s),
        mc("Was ist Klei?", "fester Lehm", ["loser Sand", "Muschelschalen", "Salzwasser"], s),
        mc("Was liegt ganz außen auf dem Deich?", "die Grasdecke", ["der Sandkern", "der Klei", "das Meer"], s),
        reihenfolge("Ordne den Aufbau des Deichs von innen nach außen.", ["Sandkern", "Klei", "Grasdecke"], s),
        mc("Wozu dient die Grasdecke?", "Die Wurzeln halten den Boden fest, so wird der Deich nicht von Wellen, Wind und Regen abgetragen.", ["Sie hält das Meerwasser süß.", "Sie lockt Seehunde an.", "Sie wärmt den Deich im Winter."], s),
        mc("Wie pflegen Schafe den Deich?", "Sie fressen das Gras kurz und festigen den Boden mit ihren Hufen.", ["Sie graben Löcher in den Deich.", "Sie bringen Sand zum Deich.", "Sie halten die Wellen ab."], s),
        tf("Die Schafe auf dem Deich schaden ihm, weil sie das Gras fressen.", False, s, info="Die Schafe halten das Gras kurz und dicht und festigen den Boden mit ihren Hufen."),
        tf("Die Seeseite zeigt zum Meer.", True, s),
        tf("Der Sandkern liegt außen und die Grasdecke innen.", False, s),
        zuordnen("Ordne dem Teil des Deichs seine Aufgabe zu.",
                 [("Seeseite", "flach, damit die Wellen ihre Kraft verlieren"), ("Landseite", "steiler, muss keine Wellen abhalten"), ("Deichkrone", "höchste Stelle des Deichs"),
                  ("Grasdecke", "Wurzeln halten den Boden fest"), ("Deichfuß", "Steine gegen das Aushöhlen"), ("Klei", "Schicht aus festem Lehm")], s),
        luecke("Ergänze den Aufbau.", "Im Inneren des Deichs liegt der {{Sandkern}}. Darüber liegt eine Schicht aus {{Klei}}. Ganz außen wächst die {{Grasdecke}}. Am {{Deichfuß}} liegen Steine.",
               s, extra=["Düne", "Marsch"]),
        luecke("Ergänze die Eigenschaften.", "Die {{Seeseite}} ist flach, damit die Wellen ihre Kraft verlieren. Die {{Landseite}} ist steiler. Die höchste Stelle heißt {{Deichkrone}}.",
               s, extra=["Marsch", "Sturmflut"]),
        frei("Beschreibe den Aufbau eines Deichs von innen nach außen.",
             "Innen liegt der Sandkern, darüber eine Schicht aus Klei (festem Lehm) und ganz außen die Grasdecke. Am Deichfuß liegen Steine.",
             ["Sandkern innen genannt", "Klei darüber genannt", "Grasdecke außen genannt", "Steine am Deichfuß genannt"], 4, s),
        frei("Erkläre, warum Schafe auf dem Deich weiden.",
             "Die Schafe fressen das Gras kurz, sodass es dicht wächst. Mit ihren Hufen festigen sie den Boden. So wird der Deich nicht abgetragen.",
             ["Gras wird kurz gehalten und wächst dicht", "Hufe festigen den Boden"], 2, s),
        frei("Erkläre, warum die Seeseite eines Deichs flach und die Landseite steiler ist.",
             "Auf der flachen Seeseite laufen die Wellen auf und verlieren ihre Kraft. Die Landseite muss keine Wellen abhalten und kann deshalb steiler sein.",
             ["Seeseite flach: Wellen verlieren Kraft", "Landseite muss keine Wellen abhalten"], 2, s),
    ]
    s = "C – Den Deich beschriften"
    A += beschriftung_aufgaben(s)
    s = "D – Deichprofile und Deichhöhen"
    A += rechen_aufgaben(s)
    s = "E – Anwenden und erklären"
    A += [
        frei("Beschreibe, wie du den Deich im Wissenscheck zeichnest und welche Teile du beschriftest.",
             "Erst zeichne ich die Form: flach zur Seeseite, steil zur Landseite, oben die Deichkrone. Dann beschrifte ich: Seeseite, Landseite, Deichkrone, Grasdecke, Klei, Sandkern, Deichfuß (Steine), Sturmflutwasserstand und Hochwasser.",
             ["Form richtig beschrieben (Seeseite flach, Landseite steil)", "Mindestens fünf Teile genannt", "Sturmflutwasserstand oder Hochwasser genannt"], 3, s),
        frei("Was würde passieren, wenn der Deichfuß keine Steine hätte? Erkläre.",
             "Die Wellen treffen zuerst auf den Deichfuß. Ohne Steine würde das Wasser den Fuß aushöhlen und wegspülen. Dann könnte der ganze Deich einstürzen.",
             ["Wellen treffen zuerst den Deichfuß", "Wasser würde den Fuß aushöhlen und wegspülen"], 2, s),
        frei("Warum werden Deiche immer höher und breiter gebaut?",
             "Damit sie höhere Sturmfluten aushalten und das Land dahinter besser schützen.",
             ["Höhere Sturmfluten aushalten", "Land besser schützen"], 2, s),
        tf("Der Sturmflutwasserstand liegt höher als das normale Hochwasser.", True, s),
        mc("Warum muss der Deich höher sein als der Sturmflutwasserstand?", "Sonst würde das Wasser über die Deichkrone laufen.", ["Sonst würden die Schafe nass.", "Sonst gäbe es keine Ebbe mehr.", "Sonst würde der Sandkern verschwinden."], s),
        zuordnen("Welches Teil des Deichs ist gemeint?",
                 [("Hier treffen die Wellen zuerst auf den Deich.", "Deichfuß"), ("Die höchste Stelle des Deichs.", "Deichkrone"), ("Die Wurzeln halten hier den Boden fest.", "Grasdecke"),
                  ("Fester Lehm über dem Kern.", "Klei"), ("Das Innere des Deichs.", "Sandkern")], s),
        kurz("Wie heißt die Seite des Deichs, die zum Meer zeigt?", ["Seeseite", "See-Seite"], s),
        kurz("Wie heißt die Seite des Deichs, die zum Land zeigt?", ["Landseite", "Land-Seite"], s),
        kurz("Wie nennt man den Wasserstand bei einer Sturmflut?", ["Sturmflutwasserstand"], s),
    ]
    return A


# =====================================================================  Lernblatt Düne und Siel


def lernblatt_duene_siel():
    return [
        lb("Dünen: Sandwälle am Strand",
           "**Dünen** sind Sandhügel hinter dem Strand, die der Wind aufbaut. Besonders auf den Inseln schützen sie die Küste. Darum stehen dort Schilder mit der Aufschrift „Dünenschutz ist Inselschutz. Bitte nicht betreten!“\n"
           "**So wächst eine Düne:**\n"
           "- Der **Wind** trägt Sand vom Strand ins Land.\n"
           "- Der **Strandhafer** hilft dabei am meisten. Seine Wurzeln bilden ein dichtes, fein verzweigtes Netz und reichen bis zu **5 m** tief. Das Netz hält den Sand fest.\n"
           "- Wird der Strandhafer vom Sand zugeweht, wächst er oben wieder heraus. So wird die Düne immer höher, am Ende mehrere Meter.",
           merke="Dünen wachsen durch Wind und Strandhafer. Seine Wurzeln halten den Sand fest.",
           bild=svg_duene(False), bildAlt="Querschnitt durch Strand und Düne mit Wind, Strandhafer und Wurzeln, daneben das Meer"),
        lb("Warum darf man Dünen nicht betreten?",
           "Es gibt zwei Gründe:\n"
           "- Wer auf die Düne tritt, **zertritt den Strandhafer**. Dann weht der Wind den Sand fort, die Düne verschwindet und die Insel ist schlechter geschützt.\n"
           "- Vögel **brüten und ruhen** in den Dünen und sollen nicht gestört werden.\n"
           "Bleib deshalb auf den markierten Wegen und Holzstegen.",
           merke="Wer eine Düne betritt, zerstört die Pflanzen: Der Sand weht weg, der Schutz der Insel geht verloren, und die Vögel werden gestört."),
        lb("Das Sieltor",
           "Ein **Siel** ist ein Durchlass im Deich. Durch ihn läuft das Wasser aus dem Hinterland, der **Marsch**, in die Nordsee. Das Tor geht von selbst auf, wenn Ebbe ist, und von selbst zu, wenn Flut ist.\n"
           "- **Ebbe**: Draußen ist das Wasser niedrig. Das Wasser von der Landseite drückt das Tor auf und fließt ins Meer ab.\n"
           "- **Flut**: Draußen ist das Wasser hoch. Es drückt das Tor zu, und so kann kein Salzwasser ins Land kommen.\n"
           "Wenn das nicht genügt, pumpen **Schöpfwerke** das Wasser über den Deich. Die Zeichnung ist vereinfacht.",
           merke="Das Sieltor lässt bei Ebbe Wasser aus dem Land ins Meer ab und hält bei Flut das Meer draußen.",
           bild=svg_siel_paar(True, ("Ebbe", "Flut")), bildAlt="Zwei vereinfachte Zeichnungen eines Sieltors im Deich: links bei Ebbe mit geöffnetem Tor und abfließendem Wasser, rechts bei Flut mit geschlossenem Tor"),
    ]


# =====================================================================  Aufgaben Düne und Siel


def aufgaben_duene():
    A = []
    s = "A – Dünen: wie sie wachsen"
    A += [
        tf("Dünen sind besonders auf den Inseln wichtig für den Schutz der Küste.", True, s),
        tf("Der Wind weht Sand vom Strand landeinwärts.", True, s),
        tf("Dünen werden vom Meer aufgeschüttet.", False, s, info="Der Wind weht den Sand vom Strand landeinwärts."),
        tf("Der Strandhafer hat Wurzeln, die bis zu 5 m tief reichen.", True, s),
        tf("Strandhafer wächst nur an Orten, wo es keinen Sand gibt.", False, s),
        mc("Was bedeutet der Spruch „Dünenschutz ist Inselschutz“?", "Wer die Dünen schützt, schützt die ganze Insel.", ["Dünen werden nur im Sommer geschützt.", "Inseln haben keine Dünen.", "Man darf Dünen nur mit dem Boot erreichen."], s),
        mc("Was bringt den Sand zur Düne?", "der Wind", ["die Flut", "die Schafe", "die Wellen allein"], s),
        mc("Welche Pflanze trägt entscheidend zum Wachstum der Dünen bei?", "der Strandhafer", ["der Queller", "der Strandflieder", "die Eiche"], s),
        mc("Wie tief reichen die Wurzeln des Strandhafers bis zu?", "bis zu 5 m", ["bis zu 5 cm", "bis zu 50 cm", "bis zu 50 m"], s),
        mc("Wie sehen die Wurzeln des Strandhafers aus?", "wie ein fein verzweigtes, dichtes Netz", ["wie eine einzige dicke Rübe", "wie Steine", "gar nicht, er hat keine Wurzeln"], s),
        mc("Was machen die Wurzeln des Strandhafers mit dem Sand?", "Sie halten ihn fest.", ["Sie lösen ihn auf.", "Sie spülen ihn ins Meer.", "Sie färben ihn grün."], s),
        mc("Was geschieht, wenn der Wind den Strandhafer mit Sand zuschüttet?", "Die Pflanze wächst oben wieder heraus.", ["Die Pflanze stirbt sofort.", "Die Düne verschwindet.", "Der Sand wird zu Stein."], s),
        mc("Warum können Dünen mehrere Meter hoch werden?", "Der Strandhafer wächst immer wieder aus dem Sand heraus und hält ihn fest.", ["Weil das Meer sie hochdrückt.", "Weil dort Steine liegen.", "Weil Schafe Sand hinbringen."], s),
        reihenfolge("Bringe das Wachstum einer Düne in die richtige Reihenfolge.",
                    ["Der Wind weht Sand vom Strand landeinwärts.", "Die Wurzeln des Strandhafers halten den Sand fest.", "Der Sand schüttet die Pflanze zu.", "Der Strandhafer wächst oben wieder heraus.", "Die Düne wird mehrere Meter hoch."], s),
        luecke("Ergänze den Text.", "Der {{Wind}} weht Sand vom Strand landeinwärts. Der {{Strandhafer}} hält den Sand mit seinen {{Wurzeln}} fest. Wird die Pflanze zugeschüttet, wächst sie oben wieder heraus. So können Dünen mehrere {{Meter}} hoch werden.",
               s, extra=["Wellen", "Muscheln"]),
        luecke("Ergänze die Zahlen und Wörter.", "Die Wurzeln des Strandhafers bilden ein {{Netz}} und reichen bis zu {{5}} m tief. Sie halten den {{Sand}} fest.",
               s, extra=["50", "Wasser"]),
        kurz("Wie tief reichen die Wurzeln des Strandhafers höchstens? (in Metern)", ["5", "5 m"], s, einheit="m"),
        frei("Erkläre in drei Sätzen, wie eine Düne wächst.",
             "Der Wind weht Sand vom Strand landeinwärts. Die dichten Wurzeln des Strandhafers halten den Sand fest. Wird die Pflanze mit Sand zugeschüttet, wächst sie oben wieder heraus, und die Düne wird immer höher.",
             ["Wind weht Sand landeinwärts", "Strandhafer und seine Wurzeln halten den Sand fest", "Pflanze wächst wieder heraus, Düne wird höher"], 3, s),
    ]
    s = "B – Dünen schützen"
    A += [
        tf("Man darf Dünen betreten, wenn man vorsichtig geht.", False, s),
        tf("Auf Schildern steht: „Dünenschutz ist Inselschutz. Bitte nicht betreten!“", True, s),
        mc("Warum darf man Dünen nicht betreten? Nenne den ersten Grund.", "Tritte zerstören den Strandhafer.", ["Der Sand ist zu heiß.", "Dort wohnen Seehunde.", "Es ist zu gefährlich wegen der Flut."], s),
        mc("Warum darf man Dünen nicht betreten? Nenne den zweiten Grund.", "Dünen sind ein wichtiger Brut- und Ruheplatz für Vögel.", ["Dort wächst der Queller.", "Dort liegt der Deichfuß.", "Dort versinkt man im Schlick."], s),
        mc("Was passiert, wenn der Strandhafer zertreten wird?", "Der Wind trägt den Sand weg und die Düne wird zerstört.", ["Die Düne wächst schneller.", "Die Düne wird zum Deich.", "Nichts, er wächst sofort nach."], s),
        mc("Was geht verloren, wenn die Dünen zerstört werden?", "der Schutz für die Insel", ["das Gezeitenwasser", "die Salzwiese", "die Marsch"], s),
        mc("Wo darf man in den Dünen gehen?", "nur auf markierten Wegen und Holzstegen", ["überall am Rand", "nur nachts", "überall, wenn man leise ist"], s),
        zuordnen("Ursache und Folge: Was passiert dann?",
                 [("Menschen betreten die Düne.", "Der Strandhafer wird zertreten."), ("Der Strandhafer ist zertreten.", "Der Wind trägt den Sand weg."),
                  ("Der Sand ist weggeweht.", "Die Düne wird zerstört."), ("Die Düne ist zerstört.", "Der Schutz für die Insel geht verloren.")], s),
        reihenfolge("Bringe die Folgen des Betretens in die richtige Reihenfolge.",
                    ["Tritte zerstören den Strandhafer.", "Der Wind trägt den Sand weg.", "Die Düne wird zerstört.", "Der Schutz für die Insel geht verloren."], s),
        luecke("Ergänze die Gründe.", "Man darf Dünen nicht betreten, weil Tritte den {{Strandhafer}} zerstören und die Dünen ein wichtiger {{Brut}}- und Ruheplatz für Vögel sind. Geh nur auf {{Holzstegen}} und markierten Wegen.",
               s, extra=["Deichfuß", "Seehund"]),
        frei("Nenne zwei Gründe, warum man Dünen nicht betreten darf.",
             "Erstens zerstören Tritte den Strandhafer, dann trägt der Wind den Sand weg und der Schutz für die Insel geht verloren. Zweitens sind Dünen ein Brut- und Ruheplatz für Vögel, die nicht gestört werden sollen.",
             ["Tritte zerstören den Strandhafer (Sand weht weg, Schutz geht verloren)", "Brut- und Ruheplatz der Vögel"], 2, s),
        frei("Du siehst, wie ein Kind auf eine Düne klettert. Was sagst du ihm und warum?",
             "Ich sage: Bitte geh nicht auf die Düne! Du zertrittst den Strandhafer. Dann weht der Wind den Sand weg und die Düne und der Schutz für die Insel gehen verloren. Außerdem brüten und ruhen dort Vögel. Wir gehen lieber auf dem Holzsteg.",
             ["Aufforderung, die Düne nicht zu betreten", "Mindestens einen Grund genannt", "Alternative genannt (Wege, Holzstege)"], 3, s),
    ]
    s = "C – Die Düne beschriften"
    bild1 = svg_duene(True)
    alt1 = ALT_DUENE + ", mit den Nummern 1 bis 6"
    A += [
        luecke("Beschrifte die Düne. Welches Wort gehört zu welcher Nummer?", "(1) {{Wind}}\n(2) {{Strand}}\n(3) {{Strandhafer}}\n(4) {{Düne}}\n(5) {{Wurzeln}}\n(6) {{Meer}}",
               s, extra=["Deich", "Priel"], bild=bild1, bildAlt=alt1, info="1 Wind, 2 Strand, 3 Strandhafer, 4 Düne, 5 Wurzeln, 6 Meer."),
        zuordnen("Ordne die Nummern zu.", [("Nummer 1", "Wind"), ("Nummer 2", "Strand"), ("Nummer 3", "Strandhafer"), ("Nummer 4", "Düne"), ("Nummer 5", "Wurzeln"), ("Nummer 6", "Meer")], s, bild=bild1, bildAlt=alt1),
        mc("Welche Nummer zeigt den Strandhafer?", "3", ["1", "4", "6"], s, bild=bild1, bildAlt=alt1),
        mc("Welche Nummer zeigt die Wurzeln?", "5", ["2", "3", "4"], s, bild=bild1, bildAlt=alt1),
        mc("Welche Nummer zeigt die Düne?", "4", ["1", "2", "6"], s, bild=bild1, bildAlt=alt1),
        mc("Welche Nummer zeigt den Wind, der den Sand landeinwärts weht?", "1", ["2", "5", "6"], s, bild=bild1, bildAlt=alt1),
    ]
    return A


def aufgaben_siel():
    A = []
    s = "D – Das Sieltor: Ebbe und Flut"
    A += [
        tf("Ein Siel ist ein Durchlass im Deich.", True, s),
        tf("Durch das Siel fließt das Wasser aus der Marsch zur Nordsee ab.", True, s),
        tf("Das Sieltor öffnet sich bei Flut.", False, s, info="Bei Flut wird das Tor vom Meerwasser zugedrückt. Es öffnet sich bei Ebbe."),
        tf("Das Sieltor öffnet sich bei Ebbe.", True, s),
        tf("Bei Flut kommt durch das Sieltor Salzwasser ins Land.", False, s),
        tf("Das Sieltor wird von Hand geöffnet und geschlossen.", False, s, info="Das Tor öffnet und schließt sich automatisch, durch den Druck des Wassers."),
        mc("Was ist ein Siel?", "ein Durchlass im Deich, durch den das Wasser aus dem Land abfließt", ["ein Gebäude auf der Düne", "ein Boot für das Watt", "eine Pflanze im Watt"], s),
        mc("Wohin fließt das Wasser durch das Siel?", "aus dem Hinterland (Marsch) in die Nordsee", ["aus der Nordsee ins Land", "aus dem Watt in die Düne", "von der Salzwiese in den Deich"], s),
        mc("Wann öffnet sich das Sieltor?", "bei Ebbe", ["bei Flut", "bei Vollmond", "nur bei Sturmflut"], s),
        mc("Wann schließt sich das Sieltor?", "bei Flut", ["bei Ebbe", "bei Niedrigwasser", "nie"], s),
        mc("Warum öffnet sich das Sieltor bei Ebbe?", "Das Wasser steht draußen niedrig. Das Tor wird vom Wasser aus dem Land aufgedrückt.", ["Das Meerwasser zieht das Tor auf.", "Ein Wärter öffnet es.", "Der Mond schiebt es auf."], s),
        mc("Warum schließt sich das Sieltor bei Flut?", "Das hohe Meerwasser drückt das Tor zu.", ["Es friert zu.", "Das Land drückt das Tor zu.", "Der Wind bläst es zu."], s),
        mc("Warum soll bei Flut kein Wasser durch das Siel ins Land?", "Es wäre Salzwasser und würde das Land überfluten.", ["Es wäre zu kalt.", "Es wäre zu süß.", "Es wäre zu schmutzig für die Schafe."], s),
        mc("Was machen Schöpfwerke?", "Sie pumpen das Wasser über den Deich, wenn das Siel nicht reicht.", ["Sie bauen Dünen auf.", "Sie fangen Fische.", "Sie bringen das Meerwasser ins Land."], s),
        zuordnen("Was passiert wann?", [("Ebbe", "Das Tor öffnet sich und Wasser aus dem Land fließt ins Meer ab."), ("Flut", "Das Meerwasser drückt das Tor zu, kein Salzwasser kommt ins Land.")], s),
        zuordnen("Beschreibe das Wasser draußen und das Tor.",
                 [("Ebbe: Wasser draußen", "niedrig"), ("Flut: Wasser draußen", "hoch"), ("Ebbe: Sieltor", "geöffnet"), ("Flut: Sieltor", "geschlossen")], s),
        luecke("Ergänze die Tabelle als Text.", "Bei {{Ebbe}} steht das Wasser draußen niedrig. Das Sieltor {{öffnet}} sich und das Wasser aus dem Land fließt ins Meer ab. Bei {{Flut}} drückt das Meerwasser das Tor zu, sodass kein {{Salzwasser}} ins Land kommt.",
               s, extra=["Süßwasser", "Sturm"]),
        luecke("Ergänze den Text über das Siel.", "Ein {{Siel}} ist ein Durchlass im {{Deich}}. Durch ihn fließt das Wasser aus der {{Marsch}} zur Nordsee ab. Reicht das nicht, pumpen {{Schöpfwerke}} das Wasser über den Deich.",
               s, extra=["Düne", "Watt"]),
        reihenfolge("Bringe den Ablauf in die richtige Reihenfolge (Start: Ebbe).",
                    ["Das Meerwasser draußen sinkt (Ebbe).", "Das Tor öffnet sich durch den Druck des Wassers von der Landseite.", "Wasser aus dem Land fließt ins Meer ab.", "Die Flut kommt und das Wasser draußen steigt.", "Das Meerwasser drückt das Tor zu."], s),
        frei("Erkläre, wie ein Sieltor funktioniert.",
             "Das Sieltor ist ein Durchlass im Deich. Bei Ebbe steht das Wasser draußen niedrig, das Tor wird vom Wasser aus dem Land aufgedrückt und das Wasser fließt ins Meer ab. Bei Flut drückt das hohe Meerwasser das Tor zu, sodass kein Salzwasser ins Land kommt.",
             ["Siel als Durchlass im Deich genannt", "Ebbe: Tor öffnet sich, Wasser fließt ab", "Flut: Tor schließt sich, Meer bleibt draußen"], 3, s),
        frei("Wozu braucht man zusätzlich Schöpfwerke?",
             "Wenn das Wasser aus dem Land nicht schnell genug durch das Siel abfließen kann (zum Beispiel weil das Tor wegen der Flut geschlossen ist), pumpen Schöpfwerke das Wasser über den Deich.",
             ["Schöpfwerke pumpen Wasser über den Deich", "Wenn das Siel nicht reicht"], 2, s),
        kurz("Wie nennt man den Durchlass im Deich, durch den das Wasser aus dem Land abfließt?", ["Siel", "Sieltor"], s),
        kurz("Wie nennt man die Anlagen, die das Wasser über den Deich pumpen?", ["Schöpfwerk", "Schöpfwerke"], s),
    ]
    s = "E – Sieltor zeichnen und lesen"
    ebbe_links = svg_siel_paar(True, ("Zeichnung A", "Zeichnung B"))
    flut_links = svg_siel_paar(False, ("Zeichnung A", "Zeichnung B"))
    alt_paar = "Zwei vereinfachte Zeichnungen eines Sieltors im Deich nebeneinander, Zeichnung A und Zeichnung B"
    A += [
        mc("Welche Zeichnung zeigt Ebbe?", "Zeichnung A", ["Zeichnung B"], s, bild=ebbe_links, bildAlt=alt_paar, tipp="Bei Ebbe steht das Meerwasser niedrig und das Tor ist offen."),
        mc("Welche Zeichnung zeigt Flut?", "Zeichnung B", ["Zeichnung A"], s, bild=ebbe_links, bildAlt=alt_paar),
        mc("Welche Zeichnung zeigt Ebbe?", "Zeichnung B", ["Zeichnung A"], s, bild=flut_links, bildAlt=alt_paar, tipp="Achte auf den Wasserstand im Meer und auf das Tor."),
        mc("Welche Zeichnung zeigt Flut?", "Zeichnung A", ["Zeichnung B"], s, bild=flut_links, bildAlt=alt_paar),
        mc("In welcher Zeichnung ist das Sieltor geschlossen?", "Zeichnung A", ["Zeichnung B", "in beiden Zeichnungen", "in keiner Zeichnung"], s, bild=flut_links, bildAlt=alt_paar),
        mc("In welcher Zeichnung fließt das Wasser aus dem Land ins Meer ab?", "Zeichnung B", ["Zeichnung A", "in beiden Zeichnungen", "in keiner Zeichnung"], s, bild=flut_links, bildAlt=alt_paar),
        luecke("Beschrifte das Sieltor bei Ebbe.", "(1) {{Meer}}\n(2) {{Deich}}\n(3) {{Tor|Sieltor}}\n(4) {{Land|Marsch|Land (Marsch)}}",
               s, extra=["Düne", "Watt"], bild=svg_siel("ebbe", True), bildAlt=ALT_SIEL + " bei Ebbe, mit Nummern 1 bis 4",
               tipp="Der Deich steht in der Mitte, das Meer liegt auf der Seite mit dem Wasser draußen."),
        luecke("Beschrifte das Sieltor bei Flut.", "(1) {{Meer}}\n(2) {{Deich}}\n(3) {{Tor|Sieltor}}\n(4) {{Land|Marsch|Land (Marsch)}}",
               s, extra=["Düne", "Watt"], bild=svg_siel("flut", True), bildAlt=ALT_SIEL + " bei Flut, mit Nummern 1 bis 4"),
        mc("Was zeigt diese Zeichnung?", "Ebbe: Das Tor ist geöffnet, Wasser aus dem Land fließt ins Meer ab.",
           ["Flut: Das Tor ist geöffnet, Wasser aus dem Land fließt ins Meer ab.", "Flut: Das Meerwasser fließt durch das Siel ins Land.", "Ebbe: Das Tor ist geschlossen, das Meer bleibt draußen."], s,
           bild=svg_siel("ebbe", False), bildAlt=ALT_SIEL + " bei Ebbe"),
        mc("Was zeigt diese Zeichnung?", "Flut: Das Tor ist geschlossen, das Meerwasser bleibt draußen.",
           ["Ebbe: Das Tor ist geschlossen, das Meerwasser bleibt draußen.", "Ebbe: Das Tor ist geöffnet, Wasser aus dem Land fließt ab.", "Flut: Das Meerwasser fließt durch das Siel ins Land."], s,
           bild=svg_siel("flut", False), bildAlt=ALT_SIEL + " bei Flut"),
        tf("In dieser Zeichnung ist Flut, denn das Meerwasser drückt das Tor zu.", True, s, bild=svg_siel("flut", False), bildAlt=ALT_SIEL + " bei Flut"),
        tf("In dieser Zeichnung ist Flut, denn das Tor ist geöffnet.", False, s, bild=svg_siel("ebbe", False), bildAlt=ALT_SIEL + " bei Ebbe",
           info="Das Tor ist geöffnet, weil Ebbe ist. Das Wasser aus dem Land fließt ins Meer ab."),
        frei("Schau dir die Zeichnung an. Beschreibe, was am Sieltor passiert.",
             "Bei Ebbe steht das Wasser im Meer niedrig. Das Tor ist geöffnet und das Wasser aus dem Land fließt durch den Deich ins Meer ab.",
             ["Ebbe erkannt (niedriger Wasserstand im Meer)", "Tor ist geöffnet", "Wasser aus dem Land fließt ab"], 3, s, bild=svg_siel("ebbe", False), bildAlt=ALT_SIEL + " bei Ebbe"),
        frei("Schau dir die Zeichnung an. Beschreibe, was am Sieltor passiert.",
             "Bei Flut steht das Wasser im Meer hoch. Das Meerwasser drückt das Tor zu. Es kommt kein Salzwasser ins Land.",
             ["Flut erkannt (hoher Wasserstand im Meer)", "Tor ist geschlossen", "Kein Salzwasser kommt ins Land"], 3, s, bild=svg_siel("flut", False), bildAlt=ALT_SIEL + " bei Flut"),
    ]
    s = "F – Deich, Düne und Siel im Vergleich"
    A += [
        zuordnen("Welcher Küstenschutz ist gemeint?",
                 [("langer Erdwall mit Sandkern, Klei und Grasdecke", "Deich"), ("Sandberg, der vom Wind aufgeweht und vom Strandhafer gehalten wird", "Düne"),
                  ("Durchlass im Deich, der sich bei Ebbe öffnet", "Sieltor"), ("pumpt Wasser über den Deich", "Schöpfwerk")], s),
        mc("Was schützt vor allem die Inseln?", "die Dünen", ["das Sieltor", "der Sandkern", "die Marsch"], s),
        mc("Was schützt vor allem das Festland an der Küste?", "der Deich", ["der Strandhafer", "der Queller", "das Watt"], s),
        mc("Was lässt Wasser aus dem Land abfließen und hält das Meer draußen?", "das Sieltor", ["die Deichkrone", "die Düne", "der Deichfuß"], s),
        mc("Was gehört zum Deich, nicht zur Düne?", "Klei", ["Strandhafer", "Wind", "Wurzeln"], s),
        mc("Was gehört zur Düne, nicht zum Deich?", "Strandhafer", ["Klei", "Deichkrone", "Sandkern"], s),
        tf("Eine Düne entsteht durch Wind und Strandhafer, ein Deich wird von Menschen gebaut.", True, s),
        tf("Das Sieltor ist ein Teil des Deichs.", True, s, info="Es ist ein Durchlass im Deich."),
        frei("Vergleiche Deich und Düne: Was ist gleich, was ist verschieden?",
             "Beide schützen das Land vor dem Meer. Der Deich ist vom Menschen gebaut (Sandkern, Klei, Grasdecke), die Düne ist ein natürlicher Sandberg, der durch Wind und Strandhafer wächst. Die Düne schützt vor allem die Inseln.",
             ["Beide schützen vor dem Meer", "Deich gebaut mit Aufbau genannt", "Düne natürlich durch Wind und Strandhafer"], 3, s),
        frei("Erkläre, wie Deich, Düne und Sieltor zusammen die Küste schützen.",
             "Der Deich schützt das Land vor Überflutung, vor allem bei Sturmflut. Auf den Inseln schützen die Dünen, die vom Strandhafer festgehalten werden. Das Sieltor lässt bei Ebbe Wasser aus dem Land abfließen und hält bei Flut das Meer draußen.",
             ["Deich schützt vor Überflutung", "Dünen schützen vor allem die Inseln", "Sieltor lässt Wasser ab und hält das Meer draußen"], 3, s),
    ]
    return A


def build():
    deich = aufgaben_deich()
    duene = aufgaben_duene()
    siel = aufgaben_siel()
    ld = lernblatt_deich()
    ldn = lernblatt_duene_siel()
    deich_a = [t for t in deich if t["abschnitt"][0] in "AB"]
    deich_b = [t for t in deich if t["abschnitt"][0] in "CDE"]
    assert len(deich_a) + len(deich_b) == len(deich)
    p1 = pack("geografie-4a-deich-aufbau", "Geografie Teil 4a: Küstenschutz – Deich, Aufbau und Teile",
              "Wozu es Deiche gibt, aus welchen Schichten ein Deich besteht und wie seine Teile heißen. Mit Lernblatt und vielen Übungsaufgaben.",
              ld[:2], deich_a, min_aufgaben=30)
    p2 = pack("geografie-4b-deich-beschriften-hoehen", "Geografie Teil 4b: Küstenschutz – Deich beschriften und Deichhöhen",
              "Den Deich beschriften (auch gespiegelt), Deichprofile lesen und Deichhöhen berechnen. Mit Lernblatt und vielen Übungsaufgaben.",
              [ld[0], ld[2]], deich_b, min_aufgaben=30,
              hinweis="Die Deichhöhen (1599 etwa 3 m, 1766 etwa 5,1 m, heute etwa 8,8 m) stammen aus dem Buch S. 128. Die Wasserstände in den Rechenbeispielen sind erfunden.")
    p3 = pack("geografie-4c-duene", "Geografie Teil 4c: Küstenschutz – Dünen",
              "Wie Dünen wachsen, welche Rolle der Strandhafer spielt und warum man Dünen nicht betreten darf. Mit Lernblatt und vielen Übungsaufgaben.",
              ldn[:2], duene, min_aufgaben=30,
              hinweis="Die Zeichnung der Düne ist vereinfacht und selbst gezeichnet.")
    p4 = pack("geografie-4d-sieltor", "Geografie Teil 4d: Küstenschutz – Sieltor",
              "Wie das Sieltor bei Ebbe und Flut arbeitet, Zeichnungen lesen und Deich, Düne und Sieltor vergleichen. Mit Lernblatt und vielen Übungsaufgaben.",
              [ldn[2]], siel, min_aufgaben=40,
              hinweis="Die Zeichnungen des Sieltors sind vereinfacht und selbst gezeichnet.")
    return [p1, p2, p3, p4]
