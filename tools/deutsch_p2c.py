"""Deutsch Klasse 6, Paket 2c: Satzreihe oder Satzgefüge? (Checkliste Kommasetzung 1; AH S. 61 „Teste dich“, DB S. 273–275, 308–309, Heftblätter S. 56–58).

Alle Sätze, Texte und Namen sind erfunden (nichts aus Buch oder Heft). Lösungen laut Faktenblatt Abschnitt 5, 6 und 7.
"""
from deutsch_lib import *

ID = "deutsch-2c-satzreihe-oder-satzgefuege"

B_A = "A – Satzreihe oder Satzgefüge?"
B_B = "B – Konjunktionen sortieren und wählen"
B_C = "C – Kommas: alles gemischt"
B_D = "D – Umformen und Satzbaupläne"

L1 = "Satzreihe oder Satzgefüge? Die Verbprobe"
L2 = "Nebenordnend oder unterordnend?"
L3 = "Die Kommaregeln im Überblick"
L4 = "Umformen und Satzbaupläne"


def lernblatt():
    return [
        lb(L1,
           "**Satzreihe** und **Satzgefüge** unterscheidest du mit der **Verbprobe**: Wo steht das gebeugte Verb (die Personalform)?\n"
           "- Steht es in **jedem** Satzteil an **zweiter Stelle**, sind es zwei Hauptsätze: **Satzreihe** (Hs + Hs). Ich bleibe zu Hause, denn ich **bin** müde.\n"
           "- Steht es im zweiten Teil am **Ende**, ist dieser Teil ein Nebensatz: **Satzgefüge** (Hs + Ns). Ich bleibe zu Hause, weil ich müde **bin**.\n"
           "Beide Sätze sagen dasselbe, aber die Wortstellung ist anders.",
           merke="Verb überall an zweiter Stelle: Satzreihe. Verb im zweiten Teil am Ende: Satzgefüge."),
        lb(L2,
           "Die Konjunktion verrät dir, welcher Satztyp es ist:\n"
           "- **nebenordnend** (verbinden Hauptsätze, Satzreihe): **und, oder, aber, sondern, denn, doch** (jedoch)\n"
           "- **unterordnend** (leiten Nebensätze ein, Satzgefüge): **weil, da, obwohl, damit, wenn, dass, sodass, nachdem, während, bevor, indem** (im Buch auch als, bis)\n"
           "Merkpaare mit gleicher Bedeutung, aber anderer Wortstellung:\n"
           "- **denn** (Hauptsatz) und **weil / da** (Nebensatz): Begründung\n"
           "- **aber / doch** (Hauptsatz) und **obwohl** (Nebensatz): Gegensatz oder Einschränkung",
           merke="denn = weil, aber = obwohl (fast): Mit denn und aber steht das Verb vorn, mit weil und obwohl hinten."),
        lb(L3,
           "**Satzreihe** (Hauptsätze):\n"
           "- Komma **immer** vor aber, sondern, denn, doch (jedoch).\n"
           "- Vor **und** und **oder** darf das Komma **wegfallen**.\n"
           "- Ohne Konjunktion steht **immer** ein Komma.\n"
           "**Satzgefüge** (Haupt- und Nebensatz):\n"
           "- **Immer** ein Komma zwischen Haupt- und Nebensatz. Das Komma steht **vor** der Konjunktion, wenn der Nebensatz hinten steht.\n"
           "- Steht der Nebensatz **vorn**, folgt das Komma hinter ihm.\n"
           "- Steht er **in der Mitte**, setzt man **zwei** Kommas.\n"
           "Kein Komma steht, wenn „und“ nur Wörter oder Satzteile verbindet (Äpfel und Birnen).",
           merke="Satzreihe: Komma vor aber, sondern, denn, doch; vor und/oder darf es fehlen. Satzgefüge: immer Komma."),
        lb(L4,
           "**Umformen:** Aus einer Satzreihe wird ein Satzgefüge, wenn du die Konjunktion tauschst und das Verb ans Ende stellst:\n"
           "- Ich lache, **denn** der Witz **ist** lustig. → Ich lache, **weil** der Witz lustig **ist**.\n"
           "- Es regnet, **aber** wir gehen raus. → Wir gehen raus, **obwohl** es regnet.\n"
           "**Satzbaupläne** (Hs = Hauptsatz, Ns = Nebensatz):\n"
           "- Hs , Hs (Satzreihe): Ole lacht, denn der Witz ist gut.\n"
           "- Hs , Ns: Ole lacht, weil der Witz gut ist.\n"
           "- Ns , Hs: Weil der Witz gut ist, lacht Ole.\n"
           "- Hs , Ns , Hs: Ole hat, weil der Witz gut war, laut gelacht.",
           merke="Satzreihe: Hs , Hs. Satzgefüge: Hs , Ns oder Ns , Hs oder Hs , Ns , Hs."),
    ]


def aufgaben():
    a = []
    # ---------------------------------------------------------------- A
    a.append(zuordnen("Satzreihe oder Satzgefüge? Ordne zu.",
                      [("Ich lese, denn das Buch ist spannend.", "Satzreihe"), ("Ich lese, weil das Buch spannend ist.", "Satzgefüge"),
                       ("Es regnet, aber wir gehen raus.", "Satzreihe"), ("Wir gehen raus, obwohl es regnet.", "Satzgefüge"),
                       ("Mia singt, und Ole spielt Gitarre.", "Satzreihe"), ("Wenn Ole Gitarre spielt, singt Mia.", "Satzgefüge")],
                      B_A, info="Verbprobe: In der Satzreihe steht die Personalform in jedem Teil an zweiter Stelle. Im Satzgefüge steht sie im Nebensatz am Ende."))
    a.append(mc("Welcher Satz ist ein Satzgefüge?", "Ole bleibt zu Hause, weil er krank ist.",
                ["Ole bleibt zu Hause, denn er ist krank.", "Ole bleibt zu Hause, und er ruht sich aus.", "Ole ist krank, aber er bleibt nicht liegen."], B_A,
                info="Nur im ersten Satz steht die Personalform „ist“ im zweiten Teil am Ende. Die anderen Sätze sind Satzreihen."))
    a.append(mc("Welcher Satz ist eine Satzreihe?", "Mia lacht, aber Ole bleibt ernst.",
                ["Mia lacht, weil Ole lustig ist.", "Mia lacht, obwohl Ole ernst bleibt.", "Mia lacht, wenn Ole erzählt."], B_A,
                info="Nach „aber“ steht ein Hauptsatz mit der Personalform „bleibt“ an zweiter Stelle."))
    a.append(mc("Woran erkennt man das Satzgefüge?", "Das gebeugte Verb steht im zweiten Teil am Ende.",
                ["Das gebeugte Verb steht überall an zweiter Stelle.", "Es steht immer ein „und“ im Satz.", "Es hat kein Komma."], B_A,
                info="Das ist die Verbprobe: Steht das gebeugte Verb im zweiten Teil am Ende, ist dieser Teil ein Nebensatz."))
    a.append(tf("In einer Satzreihe steht das gebeugte Verb in jedem Satzteil an zweiter Stelle.", True, B_A,
                info="Eine Satzreihe besteht nur aus Hauptsätzen, und im Hauptsatz steht die Personalform an zweiter Stelle."))
    a.append(tf("In einem Satzgefüge steht das gebeugte Verb im Nebensatz am Ende.", True, B_A,
                info="Das ist das Merkmal des Nebensatzes. Im Hauptsatz steht die Personalform dagegen an zweiter Stelle."))
    a.append(kurz("Satzreihe oder Satzgefüge? Ich bleibe zu Hause, denn ich bin krank.", "Satzreihe", B_A,
                  info="Nach „denn“ steht die Personalform „bin“ an zweiter Stelle. Beide Teile sind Hauptsätze."))
    a.append(kurz("Satzreihe oder Satzgefüge? Ich bleibe zu Hause, weil ich krank bin.", "Satzgefüge", B_A,
                  info="Nach „weil“ steht die Personalform „bin“ am Ende. Der zweite Teil ist ein Nebensatz."))
    a.append(mc("Wie viele Hauptsätze hat diese Satzreihe? Ich lese, Mia malt und Ole baut.", "3", ["1", "2", "4"], B_A,
                info="Ich lese. – Mia malt. – Ole baut. In jedem Teil steht die Personalform an zweiter Stelle."))
    a.append(mc("Ein Satz besteht aus einem Hauptsatz und einem Nebensatz. Wie heißt er?", "Satzgefüge", ["Satzreihe", "Aufzählung", "Wortgruppe"], B_A,
                info="Hauptsatz + Nebensatz = Satzgefüge. Zwei oder mehr Hauptsätze = Satzreihe."))

    # ---------------------------------------------------------------- B
    a.append(zuordnen("Nebenordnend oder unterordnend? Ordne die Konjunktion zu.",
                      [("und", "nebenordnend"), ("weil", "unterordnend"), ("aber", "nebenordnend"), ("obwohl", "unterordnend"),
                       ("denn", "nebenordnend"), ("damit", "unterordnend"), ("sondern", "nebenordnend"), ("nachdem", "unterordnend")],
                      B_B, info="Nebenordnend (Hauptsätze): und, oder, aber, sondern, denn, doch. Unterordnend (Nebensätze): weil, da, obwohl, damit, wenn, dass, sodass, nachdem, während, bevor, indem."))
    a.append(mc("Welche Wörter sind unterordnende Konjunktionen? (mehrere Antworten sind richtig)",
                ["weil", "obwohl", "nachdem", "bevor"], ["denn", "doch"], B_B,
                info="weil, obwohl, nachdem und bevor leiten Nebensätze ein. „denn“ und „doch“ verbinden Hauptsätze."))
    a.append(tf("„denn“ und „weil“ nennen beide eine Begründung.", True, B_B,
                info="Bei „denn“ steht danach ein Hauptsatz, bei „weil“ ein Nebensatz mit dem Verb am Ende."))
    a.append(mc("Welche Konjunktion macht aus „Ich bleibe, denn ich bin müde.“ ein Satzgefüge?", "weil", ["denn", "aber", "und"], B_B,
                info="Mit „weil“ wird der zweite Teil ein Nebensatz: Ich bleibe, weil ich müde bin."))
    a.append(luecke("Ergänze „denn“ oder „weil“.",
                    "Ich lache, {{denn}} der Film ist lustig. Ich lache, {{weil}} der Film lustig ist.", B_B,
                    extra=["obwohl"], info="Nach „denn“ steht ein Hauptsatz (Verb an zweiter Stelle), nach „weil“ ein Nebensatz (Verb am Ende)."))
    a.append(luecke("Ergänze „aber“ oder „obwohl“.",
                    "Es regnet, {{aber}} wir gehen raus. Wir gehen raus, {{obwohl}} es regnet.", B_B,
                    extra=["denn"], info="Nach „aber“ steht ein Hauptsatz, nach „obwohl“ ein Nebensatz mit dem Verb am Ende."))
    a.append(mc("Welche Konjunktion passt in eine Satzreihe? Ich möchte kommen, … ich habe keine Zeit.", "doch", ["weil", "obwohl", "damit"], B_B,
                info="Es ist ein Gegensatz zwischen zwei Hauptsätzen: Ich möchte kommen, doch ich habe keine Zeit. Mit „aber“ ginge es auch."))
    a.append(mc("Welche Konjunktion passt? Ole möchte kommen, … er keine Zeit hat.", "obwohl", ["doch", "aber", "denn"], B_B,
                info="Das Verb „hat“ steht am Ende, also ist es ein Nebensatz. Nur „obwohl“ ist von den Wörtern eine unterordnende Konjunktion."))
    a.append(tf("Nach „denn“ bleibt die Wortstellung des Hauptsatzes (Verb an zweiter Stelle).", True, B_B,
                info="Beispiel: …, denn die Geschichte ist lustig. „ist“ steht an zweiter Stelle."))

    # ---------------------------------------------------------------- C
    a.append(kommas("Ich esse einen Apfel {,} denn ich habe Hunger.", B_C, "Satzreihe: Vor „denn“ steht immer ein Komma."))
    a.append(kommas("Ich esse einen Apfel {,} weil ich Hunger habe.", B_C, "Satzgefüge: Zwischen Haupt- und Nebensatz steht immer ein Komma."))
    a.append(kommas("Mia spielt Klavier {?} und Ole zeichnet Bilder.", B_C, "Satzreihe: Vor „und“ darf das Komma wegfallen. Beide Antworten sind richtig."))
    a.append(kommas("Wenn es dunkel wird {,} gehen wir nach Hause.", B_C, "Satzgefüge mit vorangestelltem Nebensatz: Nach dem Nebensatz steht das Komma."))
    a.append(kommas("Ole ist klein {,} aber er ist sehr schnell.", B_C, "Satzreihe: Vor „aber“ steht immer ein Komma."))
    a.append(kommas("Pia weiß {,} dass sie gewinnen kann.", B_C, "Satzgefüge: Vor „dass“ steht ein Komma."))
    a.append(kommas("Sie lacht {,} sie tanzt {,} sie ist glücklich.", B_C, "Drei Hauptsätze ohne Konjunktion: Dazwischen steht jeweils ein Komma."))
    a.append(kommas("Wir wollten gehen {,} doch es hat geregnet.", B_C, "Satzreihe: Vor „doch“ steht immer ein Komma."))
    a.append(kommas("Ole bleibt zu Hause {,} obwohl er gesund ist.", B_C, "Satzgefüge: Vor „obwohl“ steht ein Komma."))
    a.append(kommas("Mia kauft Brot {-} und Milch.", B_C, "„und“ verbindet nur zwei Wörter (Brot und Milch). Es folgt kein neuer Hauptsatz, also steht kein Komma."))
    a.append(kommas("Soll ich anrufen {?} oder schreibst du?", B_C, "Satzreihe: Vor „oder“ darf das Komma wegfallen. Beide Antworten sind richtig."))

    # ---------------------------------------------------------------- D
    a.append(mc("Forme in ein Satzgefüge um: Ich bleibe zu Hause, denn ich bin krank.",
                "Ich bleibe zu Hause, weil ich krank bin.",
                ["Ich bleibe zu Hause, weil ich bin krank.", "Ich bleibe zu Hause, aber ich bin krank.", "Ich bleibe zu Hause weil ich krank bin."], B_D,
                info="„denn“ wird zu „weil“, die Personalform „bin“ rückt ans Ende. Das Komma bleibt."))
    a.append(kurz("Forme in eine Satzreihe um (mit „denn“): Ich lache, weil der Witz lustig ist.", "Ich lache, denn der Witz ist lustig.", B_D, gross=True,
                  info="Aus „weil“ wird „denn“. Das Verb „ist“ rückt an die zweite Stelle: Ich lache, denn der Witz ist lustig."))
    a.append(kurz("Forme in eine Satzreihe um (mit „aber“): Wir gehen raus, obwohl es regnet.",
                  ["Es regnet, aber wir gehen raus.", "Es regnet, doch wir gehen raus."], B_D, gross=True,
                  info="Aus „obwohl“ wird „aber“ (oder „doch“). Der Regen steht dann im ersten Hauptsatz: Es regnet, aber wir gehen raus."))
    a.append(mc("Welcher Satzbauplan passt zu: Es regnet, aber wir gehen raus.?", "Hs , Hs", ["Hs , Ns", "Ns , Hs", "Hs , Ns , Hs"], B_D,
                info="Beide Teile sind Hauptsätze, es ist eine Satzreihe."))
    a.append(mc("Welcher Satzbauplan passt zu: Wir gehen raus, obwohl es regnet.?", "Hs , Ns", ["Hs , Hs", "Ns , Hs", "Hs , Ns , Hs"], B_D,
                info="Der Hauptsatz steht vorn, der Nebensatz „obwohl es regnet“ steht hinten."))
    a.append(zuordnen("Ordne jedem Satz den passenden Satzbauplan zu.",
                      [("Ole lacht, denn der Witz ist gut.", "Hs , Hs"), ("Weil der Witz gut ist, lacht Ole.", "Ns , Hs"),
                       ("Ole lacht, weil der Witz gut ist.", "Hs , Ns"), ("Ole hat, weil der Witz gut war, laut gelacht.", "Hs , Ns , Hs")],
                      B_D, info="Hs , Hs ist eine Satzreihe. Bei Hs , Ns steht der Nebensatz hinten, bei Ns , Hs vorn und bei Hs , Ns , Hs in der Mitte."))
    a.append(zuordnen("Ordne jedem Satz den passenden Satzbauplan zu.",
                      [("Mia singt, und Ole spielt Gitarre.", "Hs , Hs"), ("Nachdem Mia gesungen hat, klatschen alle.", "Ns , Hs"),
                       ("Alle klatschen, nachdem Mia gesungen hat.", "Hs , Ns"), ("Mia hat, obwohl sie Angst hatte, gesungen.", "Hs , Ns , Hs")],
                      B_D, info="Bei jedem Satz zuerst die Personalformen suchen: Wo das Verb am Ende steht, ist ein Nebensatz."))
    a.append(kommas("Wir gehen {,} nachdem wir gegessen haben {,} spazieren.", B_D,
                    "Der Nebensatz steht in der Mitte des Hauptsatzes und wird von zwei Kommas eingeschlossen."))
    a.append(kurz("Nenne den Satzbauplan von: Weil es kalt ist, ziehe ich eine Jacke an. (Schreibe zum Beispiel: Hs , Ns)", "Ns , Hs", B_D,
                  info="Der Nebensatz „Weil es kalt ist“ steht vorn, danach folgt der Hauptsatz: „Ns , Hs“."))
    a.append(frei("Schreibe einen Satz mit dem Satzbauplan Hs , Ns , Hs.",
                  "Mia hat, weil sie müde war, früh geschlafen.",
                  ["Der Satz hat einen Hauptsatz, der durch einen Nebensatz unterbrochen wird.", "Der Nebensatz hat eine unterordnende Konjunktion und das Verb am Ende.", "Vor und hinter dem Nebensatz steht ein Komma."],
                  2, B_D, info="Der Nebensatz steht in der Mitte des Hauptsatzes. Er wird durch zwei Kommas abgetrennt."))
    return a


def build():
    p = pack(ID, "Deutsch Teil 2c: Satzreihe oder Satzgefüge?",
             "Satzreihe und Satzgefüge unterscheiden (Verbprobe), Konjunktionen sortieren, Kommaregeln gemischt anwenden, Sätze umformen und Satzbaupläne zuordnen. Mit Lernblatt und Übungsaufgaben.",
             lernblatt(), aufgaben(), min_aufgaben=36,
             hinweis="Alle Sätze, Texte und Namen sind selbst ausgedacht, nicht aus dem Deutschbuch oder Aufgabenheft. Kommas wählst du in einer Liste aus („Komma“ oder „kein Komma“). Beim Abschreiben und Umformen zählt jeder Buchstabe und jedes Komma.")
    return [nachlesen(p, {B_A: L1, B_B: L2, B_C: L3, B_D: L4})]


if __name__ == "__main__":
    for p in build():
        print(p["id"], len(p["aufgaben"]), "Aufgaben")
