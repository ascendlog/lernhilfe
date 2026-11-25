"""Deutsch Klasse 6, Paket 2a: Die Satzreihe (Checkliste Kommasetzung 2; DB S. 273, DB S. 308 Nr. 1 mit Merkkasten S. 309, Heftblatt S. 56, AH S. 57).

Alle Sätze, Texte und Namen sind erfunden (nichts aus Buch oder Heft). Lösungen laut Faktenblatt Abschnitt 5.
Kommas werden mit Auswahllisten „Komma“ / „kein Komma“ abgefragt (in der App getestet).
"""
from deutsch_lib import *

ID = "deutsch-2a-satzreihe"

B_A = "A – Hauptsätze erkennen und zählen"
B_B = "B – Nebenordnende Konjunktionen"
B_C = "C – Das Komma in der Satzreihe"
B_D = "D – Satzreihen bilden"
B_E = "E – Texte mit Kommas"

L1 = "Hauptsatz und Satzreihe"
L2 = "Nebenordnende Konjunktionen"
L3 = "Das Komma in der Satzreihe"
L4 = "Satzreihen bilden"


def lernblatt():
    return [
        lb(L1,
           "Ein **Hauptsatz** kann allein stehen. In ihm steht die **Personalform** des Verbs (das gebeugte Verb) an **zweiter Stelle**: Die Kinder **spielen** im Garten. – Heute **backt** Mama einen Kuchen.\n"
           "Eine **Satzreihe** besteht aus **zwei oder mehr Hauptsätzen**. Die Hauptsätze werden durch ein **Komma** getrennt oder durch eine Konjunktion verbunden.\n"
           "Beispiel mit zwei Hauptsätzen: Ich lese gern, denn die Geschichte ist spannend.\n"
           "Beispiel mit drei Hauptsätzen: Mia singt, Ole spielt Gitarre und Pia trommelt.",
           merke="Satzreihe = zwei oder mehr Hauptsätze. Die Personalform steht in jedem Hauptsatz an zweiter Stelle."),
        lb(L2,
           "Hauptsätze werden oft durch **nebenordnende Konjunktionen** verbunden: **und, oder, aber, sondern, denn, doch** (das Buch nennt zusätzlich **jedoch**).\n"
           "Sie haben verschiedene Bedeutungen:\n"
           "- **und**: Reihung (Ole malt, und Mia baut.)\n"
           "- **oder**: Alternative (Spielen wir Karten, oder schauen wir einen Film?)\n"
           "- **aber, doch, jedoch**: Gegensatz (Es regnet, aber wir gehen raus.)\n"
           "- **sondern**: Berichtigung nach „nicht“ (Er ruft nicht an, sondern er schreibt.)\n"
           "- **denn**: Begründung (Ich bleibe zu Hause, denn ich bin müde.)\n"
           "Nach diesen Konjunktionen bleibt die Wortstellung des **Hauptsatzes**: Das Verb steht an zweiter Stelle. …, denn die Geschichte **ist** lustig.",
           merke="und, oder, aber, sondern, denn, doch verbinden Hauptsätze. Danach steht das Verb an zweiter Stelle."),
        lb(L3,
           "So setzt du das **Komma** in der Satzreihe:\n"
           "- Vor **aber, sondern, denn, doch** (und jedoch) steht **immer** ein Komma.\n"
           "- Vor **und** und **oder** darf das Komma **wegfallen**. Man kann es aber setzen.\n"
           "- Steht **keine Konjunktion** zwischen zwei Hauptsätzen, steht **immer** ein Komma: Es klingelt, Mia öffnet die Tür.\n"
           "Wichtig: Verbindet „und“ nur zwei **Wörter oder Satzteile** (niedlich und zahm, Äpfel und Birnen), steht **kein** Komma davor.",
           merke="Komma immer vor aber, sondern, denn, doch. Vor und und oder darf es wegfallen. Ohne Konjunktion steht es immer."),
        lb(L4,
           "So machst du aus zwei Hauptsätzen eine Satzreihe:\n"
           "1. Lies beide Sätze und überlege, wie sie zusammenhängen (Grund, Gegensatz, Reihung, Auswahl).\n"
           "2. Wähle die passende Konjunktion.\n"
           "3. Schreibe beide Hauptsätze hintereinander. Setze das Komma, wenn es nötig ist.\n"
           "Beispiel: Wir bleiben zu Hause. Es regnet. → Wir bleiben zu Hause, **denn** es regnet.\n"
           "Mehrere Konjunktionen können passen: Ich möchte kommen, **aber** ich habe keine Zeit. Oder: …, **doch** ich habe keine Zeit.",
           merke="Erst den Zusammenhang klären, dann die Konjunktion wählen, dann das Komma setzen."),
    ]


def aufgaben():
    a = []
    # ---------------------------------------------------------------- A
    a.append(mc("Wo steht die Personalform im Hauptsatz?", "An zweiter Stelle", ["An erster Stelle", "Am Ende", "An dritter Stelle"], B_A,
                info="Im Hauptsatz steht die Personalform (das gebeugte Verb) an zweiter Satzgliedstelle: Die Kinder spielen im Garten."))
    a.append(mc("Welcher Satz ist ein Hauptsatz?",
                "Die Kinder spielen im Garten.", ["weil die Kinder im Garten spielen", "ob die Kinder im Garten spielen", "damit sie im Garten spielen"], B_A,
                info="Nur im ersten Satz steht die Personalform „spielen“ an zweiter Stelle, und er kann allein stehen. Die anderen drei sind Nebensätze mit dem Verb am Ende."))
    a.append(tf("Eine Satzreihe besteht aus zwei oder mehr Hauptsätzen.", True, B_A,
                info="So steht es im Merkkasten. Die Hauptsätze werden durch ein Komma getrennt oder durch eine Konjunktion verbunden."))
    a.append(tf("Die Hauptsätze einer Satzreihe werden durch ein Komma getrennt.", True, B_A,
                info="Das Komma steht zwischen den Hauptsätzen. Nur vor „und“ und „oder“ darf es wegfallen."))
    a.append(mc("Wie viele Hauptsätze hat diese Satzreihe? Ich lese gern, denn die Geschichte ist spannend, und mein Bruder liest mit.",
                "3", ["1", "2", "4"], B_A,
                info="Ich lese gern. – Die Geschichte ist spannend. – Mein Bruder liest mit. In jedem Teil steht die Personalform an zweiter Stelle."))
    a.append(mc("Wie viele Hauptsätze hat diese Satzreihe? Mia singt, Ole spielt Gitarre, Pia trommelt und Tom tanzt.",
                "4", ["2", "3", "5"], B_A,
                info="Mia singt. – Ole spielt Gitarre. – Pia trommelt. – Tom tanzt. Vier Hauptsätze, zwei Kommas ohne Konjunktion und ein „und“."))
    a.append(kurz("Schreibe die Personalform auf: Heute backt Mama einen Kuchen.", "backt", B_A,
                  info="„backt“ ist das gebeugte Verb und steht an zweiter Stelle (Heute – backt – …)."))
    a.append(mc("Welcher Satz ist eine Satzreihe?",
                "Es regnet, aber wir gehen trotzdem raus.",
                ["Wir gehen raus, obwohl es regnet.", "Weil es regnet, bleiben wir drinnen.", "Wir gehen raus."], B_A,
                info="Es regnet (Hauptsatz) und wir gehen trotzdem raus (Hauptsatz) sind durch „aber“ verbunden. In den anderen Sätzen steht ein Nebensatz oder nur ein Hauptsatz."))

    # ---------------------------------------------------------------- B
    a.append(zuordnen("Welche Bedeutung hat die Konjunktion?",
                      [("und", "Reihung"), ("oder", "Alternative"), ("aber", "Gegensatz"), ("denn", "Begründung"), ("sondern", "Berichtigung nach „nicht“")],
                      B_B, info="und reiht auf, oder stellt zur Wahl, aber drückt einen Gegensatz aus, denn nennt einen Grund, sondern berichtigt etwas nach „nicht“."))
    a.append(mc("Welche Wörter sind nebenordnende Konjunktionen? (mehrere Antworten sind richtig)",
                ["und", "oder", "aber", "denn"], ["weil", "obwohl"], B_B,
                info="und, oder, aber, denn (außerdem sondern und doch) verbinden Hauptsätze. „weil“ und „obwohl“ leiten Nebensätze ein."))
    a.append(mc("Welche Konjunktion passt? Ich möchte ein Eis, … es ist zu kalt.", "aber", ["denn", "oder", "sondern"], B_B,
                info="Es ist ein Gegensatz: Ich möchte Eis, aber es ist zu kalt. „doch“ würde auch passen."))
    a.append(luecke("Ergänze die passende Konjunktion.",
                    "Mia kommt nicht zu Fuß, {{sondern}} sie fährt mit dem Rad. Ich bleibe zu Hause, {{denn}} ich bin müde. Wir können Karten spielen, {{oder}} wir schauen einen Film.", B_B,
                    extra=["aber", "und"], info="sondern berichtigt nach „nicht“, denn nennt den Grund, oder stellt zur Wahl."))
    a.append(mc("Nach „nicht“ steht in einer Satzreihe oft die Konjunktion …", "sondern", ["denn", "oder", "und"], B_B,
                info="Beispiel: Er ruft nicht an, sondern er schreibt einen Brief. Mit „sondern“ wird etwas berichtigt."))
    a.append(tf("„denn“ leitet eine Begründung ein und verbindet zwei Hauptsätze.", True, B_B,
                info="Nach „denn“ bleibt die Wortstellung des Hauptsatzes: Ich bleibe zu Hause, denn ich bin müde."))
    a.append(mc("Welche Form ist richtig? Ich bleibe zu Hause, …",
                "denn ich bin müde.", ["denn ich müde bin.", "denn bin ich müde.", "denn müde ich bin."], B_B,
                info="Nach „denn“ steht ein Hauptsatz: Die Personalform „bin“ steht an zweiter Stelle."))
    a.append(mc("Welche Satzreihe ist richtig gebildet?",
                "Ich lese gern, aber mein Bruder spielt lieber.",
                ["Ich lese gern, aber mein Bruder lieber spielt.", "Ich lese gern, aber spielt mein Bruder lieber lieber.", "Ich lese gern aber, mein Bruder spielt lieber."], B_B,
                info="Nach „aber“ steht wieder ein Hauptsatz: Die Personalform „spielt“ ist an zweiter Stelle. Das Komma steht vor „aber“."))
    a.append(kurz("Welche nebenordnende Konjunktion leitet eine Begründung ein? (Sie hat vier Buchstaben.)", "denn", B_B,
                  info="Mit „denn“ nennt man einen Grund: Wir gehen früh schlafen, denn morgen ist ein langer Tag."))

    # ---------------------------------------------------------------- C
    a.append(kommas("Ich lese gern {,} denn die Geschichte ist spannend.", B_C,
                    "Vor „denn“ steht immer ein Komma, weil zwei Hauptsätze verbunden werden."))
    a.append(kommas("Mia singt laut {,} aber Ole hört nicht zu.", B_C,
                    "Vor „aber“ steht immer ein Komma."))
    a.append(kommas("Wir bleiben zu Hause {,} denn es regnet in Strömen.", B_C,
                    "Vor „denn“ steht immer ein Komma."))
    a.append(kommas("Er ruft nicht an {,} sondern er schreibt einen Brief.", B_C,
                    "Vor „sondern“ steht immer ein Komma."))
    a.append(kommas("Ole spielt Fußball {?} und Mia fährt Rad.", B_C,
                    "Vor „und“ darf das Komma wegfallen. Beide Antworten sind richtig."))
    a.append(kommas("Möchtest du ein Eis {?} oder möchtest du lieber einen Kuchen?", B_C,
                    "Vor „oder“ darf das Komma wegfallen. Beide Antworten sind richtig."))
    a.append(kommas("Es klingelt {,} Mia öffnet die Tür.", B_C,
                    "Zwischen zwei Hauptsätzen ohne Konjunktion steht immer ein Komma."))
    a.append(kommas("Die Sonne scheint {,} die Vögel singen {,} der Frühling beginnt.", B_C,
                    "Drei Hauptsätze ohne Konjunktion: Nach dem ersten und nach dem zweiten Hauptsatz steht ein Komma."))
    a.append(mc("Vor welchen Konjunktionen darf das Komma in einer Satzreihe wegfallen?",
                "und, oder", ["aber, sondern", "denn, doch", "aber, denn"], B_C,
                info="Nur vor „und“ und „oder“ darf das Komma entfallen. Vor aber, sondern, denn und doch steht es immer."))
    a.append(tf("Vor „aber“ darf man das Komma weglassen.", False, B_C,
                info="Vor aber, sondern, denn und doch muss das Komma stehen. Nur vor und/oder darf es wegfallen."))
    a.append(mc("Welcher Satz ist richtig geschrieben?",
                "Ole kommt heute nicht, denn er ist krank.",
                ["Ole kommt heute nicht denn er ist krank.", "Ole kommt heute nicht denn, er ist krank.", "Ole kommt, heute nicht denn er ist krank."], B_C,
                info="Das Komma gehört vor „denn“, direkt hinter den ersten Hauptsatz."))
    a.append(kurz("Schreibe den Satz mit dem richtigen Komma ab: Ich mag Tee aber meine Schwester trinkt lieber Saft.",
                  "Ich mag Tee, aber meine Schwester trinkt lieber Saft.", B_C, gross=True,
                  info="Vor „aber“ steht immer ein Komma: Ich mag Tee, aber meine Schwester trinkt lieber Saft."))
    a.append(kurz("Schreibe den Satz mit dem richtigen Komma ab: Wir gehen früh schlafen denn morgen ist ein langer Tag.",
                  "Wir gehen früh schlafen, denn morgen ist ein langer Tag.", B_C, gross=True,
                  info="Vor „denn“ steht immer ein Komma."))
    a.append(tf("Zwischen zwei Hauptsätzen ohne Konjunktion steht immer ein Komma.", True, B_C,
                info="Ohne Konjunktion trennt das Komma die Hauptsätze: Es klingelt, Mia öffnet die Tür."))

    # ---------------------------------------------------------------- D
    a.append(mc("Verbinde die Sätze: Mara ist müde. Sie geht nicht schlafen. Welche Satzreihe ist richtig?",
                "Mara ist müde, aber sie geht nicht schlafen.",
                ["Mara ist müde aber sie geht nicht schlafen.", "Mara ist müde, denn sie geht nicht schlafen.", "Mara ist müde, sondern sie geht nicht schlafen."], B_D,
                info="Es ist ein Gegensatz, deshalb passt „aber“ (oder „doch“). Das Komma steht vor „aber“."))
    a.append(kurz("Verbinde mit „denn“: Wir bleiben zu Hause. Es regnet.", "Wir bleiben zu Hause, denn es regnet.", B_D, gross=True,
                  info="Beide Sätze bleiben Hauptsätze. Vor „denn“ steht ein Komma: Wir bleiben zu Hause, denn es regnet."))
    a.append(kurz("Verbinde mit „und“ (das Komma darf wegfallen): Ole malt ein Bild. Mia baut einen Turm.",
                  ["Ole malt ein Bild, und Mia baut einen Turm.", "Ole malt ein Bild und Mia baut einen Turm."], B_D, gross=True,
                  info="Vor „und“ darf das Komma wegfallen. Beide Schreibweisen sind richtig."))
    a.append(kurz("Verbinde mit „sondern“: Mara geht nicht zu Fuß. Sie fährt mit dem Rad.",
                  "Mara geht nicht zu Fuß, sondern sie fährt mit dem Rad.", B_D, gross=True,
                  info="Nach „nicht“ berichtigt „sondern“ die Aussage. Vor „sondern“ steht immer ein Komma."))
    a.append(kurz("Verbinde mit „oder“ (das Komma darf wegfallen): Wir spielen Karten. Wir schauen einen Film.",
                  ["Wir spielen Karten, oder wir schauen einen Film.", "Wir spielen Karten oder wir schauen einen Film."], B_D, gross=True,
                  info="Vor „oder“ darf das Komma wegfallen. Beide Schreibweisen sind richtig."))
    a.append(mc("Welche Konjunktionen passen? Es ist kalt, … ich friere nicht. (mehrere Antworten sind richtig)",
                ["aber", "doch"], ["denn", "sondern", "oder"], B_D,
                info="Der zweite Satz sagt das Gegenteil von dem, was man erwartet (ein Gegensatz). Dafür passen aber und doch."))
    a.append(frei("Bilde eine Satzreihe mit „aber“ aus den Sätzen: Ich möchte spielen. Ich muss lernen.",
                  "Ich möchte spielen, aber ich muss lernen.",
                  ["Beide Teile sind Hauptsätze (Personalform an zweiter Stelle).", "Die Konjunktion „aber“ verbindet sie.", "Vor „aber“ steht ein Komma."],
                  2, B_D, info="Vor „aber“ steht immer ein Komma. Auch „doch“ wäre möglich."))
    a.append(frei("Schreibe eine eigene Satzreihe mit drei Hauptsätzen.",
                  "Die Sonne scheint, die Vögel singen und wir gehen spazieren.",
                  ["Der Satz hat drei Hauptsätze.", "In jedem Hauptsatz steht die Personalform an zweiter Stelle.", "Die Kommas sind richtig gesetzt."],
                  3, B_D, info="Zwischen den ersten beiden Hauptsätzen steht ein Komma, vor „und“ darf es wegfallen."))

    # ---------------------------------------------------------------- E
    a.append(kommas("Ich möchte heute Fußball spielen {,} aber es regnet {?} und der Platz ist nass. Wir bleiben zu Hause {,} denn bei dem Wetter macht Spielen keinen Spaß. Mia malt ein Bild {?} und Ole liest ein Buch.", B_E,
                    "Vor „aber“ und „denn“ steht immer ein Komma. Vor „und“ darf es wegfallen (beide Antworten sind richtig).",
                    frage="Wo gehört ein Komma hin? Wähle bei jeder Lücke „Komma“ oder „kein Komma“ (Text: Ein Regentag)."))
    a.append(kommas("Der Hund bellt laut {,} denn er hört ein Geräusch. Die Katze schläft {-} und träumt von Mäusen. Papa lacht {,} Mama kocht Tee.", B_E,
                    "Vor „denn“ steht ein Komma. „und“ verbindet in „schläft und träumt“ nur zwei Verben, kein Hauptsatz folgt, also kein Komma. Ohne Konjunktion (Papa lacht, Mama kocht) steht ein Komma.",
                    frage="Wo gehört ein Komma hin? Wähle bei jeder Lücke „Komma“ oder „kein Komma“ (Text: Zu Hause)."))
    a.append(kommas("Wir wollten wandern {,} doch das Wetter war schlecht. Also fuhren wir ins Schwimmbad {?} und wir hatten viel Spaß. Ich war nicht müde {,} sondern ich wollte weiter schwimmen.", B_E,
                    "Vor „doch“ und „sondern“ steht immer ein Komma. Vor „und“ vor einem neuen Hauptsatz darf es wegfallen.",
                    frage="Wo gehört ein Komma hin? Wähle bei jeder Lücke „Komma“ oder „kein Komma“ (Text: Ein Ausflug)."))
    a.append(kommas("Pia mag Äpfel {-} und Birnen. Sie isst keinen Käse {,} aber sie liebt Schinken. Ole mag Nudeln {,} Mia mag Reis {?} und Tom isst gern Pizza.", B_E,
                    "„Äpfel und Birnen“: „und“ verbindet nur zwei Wörter, kein Komma. Vor „aber“ steht ein Komma. Bei der Reihung von Hauptsätzen steht ein Komma, vor „und“ darf es wegfallen.",
                    frage="Wo gehört ein Komma hin? Wähle bei jeder Lücke „Komma“ oder „kein Komma“ (Text: Beim Essen)."))
    a.append(kommas("Die Schule ist aus {?} und alle rennen nach Hause. Mia wartet auf Ole {,} denn sie gehen zusammen. Er kommt nicht {,} sondern er ist schon vorgegangen.", B_E,
                    "Vor „denn“ und „sondern“ steht immer ein Komma. Vor „und“ darf es wegfallen.",
                    frage="Wo gehört ein Komma hin? Wähle bei jeder Lücke „Komma“ oder „kein Komma“ (Text: Nach der Schule)."))
    a.append(kommas("Soll ich dir helfen {?} oder machst du es allein? Du kannst es versuchen {,} aber du musst es nicht tun. Es ist spät {,} doch ich bin nicht müde.", B_E,
                    "Vor „oder“ darf das Komma wegfallen. Vor „aber“ und „doch“ steht immer ein Komma.",
                    frage="Wo gehört ein Komma hin? Wähle bei jeder Lücke „Komma“ oder „kein Komma“ (Text: Am Abend)."))
    return a


def build():
    p = pack(ID, "Deutsch Teil 2a: Die Satzreihe",
             "Hauptsätze erkennen und zählen, nebenordnende Konjunktionen (und, oder, aber, sondern, denn, doch), Kommaregeln in der Satzreihe, Satzreihen bilden und mit Kommas schreiben. Mit Lernblatt und Übungsaufgaben.",
             lernblatt(), aufgaben(), min_aufgaben=40,
             hinweis="Alle Sätze, Texte und Namen sind selbst ausgedacht, nicht aus dem Deutschbuch oder Aufgabenheft. Kommas wählst du in einer Liste aus („Komma“ oder „kein Komma“). Wo das Komma wegfallen darf (vor „und“ und „oder“), gelten beide Antworten. Beim Abschreiben zählt jeder Buchstabe und jedes Komma.")
    return [nachlesen(p, {B_A: L1, B_B: L2, B_C: L3, B_D: L4, B_E: [L2, L3]})]


if __name__ == "__main__":
    for p in build():
        print(p["id"], len(p["aufgaben"]), "Aufgaben")
