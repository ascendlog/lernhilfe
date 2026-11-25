"""Deutsch Klasse 6, Paket 2b: Das Satzgefüge (Checkliste Kommasetzung 3; DB S. 274–275, S. 308 Nr. 3–4 mit Merkkasten S. 309, Heftblätter S. 57–58, AH S. 58, Relativsätze nur wie AH S. 61).

Alle Sätze, Texte und Namen sind erfunden (nichts aus Buch oder Heft). Lösungen laut Faktenblatt Abschnitt 6.
"""
from deutsch_lib import *

ID = "deutsch-2b-satzgefuege"

B_A = "A – Haupt- und Nebensatz"
B_B = "B – Unterordnende Konjunktionen"
B_C = "C – Das Komma im Satzgefüge"
B_D = "D – Nebensatz vorn, in der Mitte, hinten"
B_E = "E – Satzbaupläne"
B_F = "F – Relativsätze (nur das Wichtigste)"

L1 = "Hauptsatz, Nebensatz und Satzgefüge"
L2 = "Unterordnende Konjunktionen"
L3 = "Das Komma im Satzgefüge"
L4 = "Satzbaupläne"
L5 = "Relativsätze"


def lernblatt():
    return [
        lb(L1,
           "Ein **Satzgefüge** besteht aus einem **Hauptsatz** und mindestens einem **Nebensatz**.\n"
           "- Der **Hauptsatz** kann allein stehen. Die **Personalform** steht an **zweiter Stelle**: Ole **bleibt** zu Hause.\n"
           "- Der **Nebensatz** kann **nicht allein** stehen. Er ist dem Hauptsatz **untergeordnet**. Die **Personalform** steht am **Ende**: …, weil er krank **ist**.\n"
           "Beispiel: Ole bleibt zu Hause, weil er krank ist.\n"
           "Im Buch heißt es „aus mindestens einem Hauptsatz und mindestens einem Nebensatz“, im Heft „aus einem Hauptsatz und mindestens einem weiteren Nebensatz“. Beides ist richtig.",
           merke="Satzgefüge = Hauptsatz + Nebensatz. Hauptsatz: Verb an zweiter Stelle. Nebensatz: Verb am Ende."),
        lb(L2,
           "Ein Nebensatz beginnt oft mit einer **unterordnenden Konjunktion**:\n"
           "**weil, da, obwohl, damit, wenn, dass, sodass, nachdem, während, bevor, indem** (im Buch auch **als** und **bis**).\n"
           "Sie haben verschiedene Bedeutungen:\n"
           "- **Begründung**: weil, da (Ole bleibt zu Hause, weil er krank ist.)\n"
           "- **Zeit**: nachdem, bevor, während, als, bis (Putze die Zähne, bevor du schlafen gehst.)\n"
           "- **Einschränkung**: obwohl (Wir gehen raus, obwohl es regnet.)\n"
           "- **Bedingung**: wenn (Wenn die Sonne scheint, gehen wir schwimmen.)\n"
           "- **Zweck**: damit (Ich lerne, damit ich eine gute Note bekomme.)\n"
           "- **Folge**: sodass (Es regnete so stark, sodass wir nass wurden.)\n"
           "- **Inhalt**: dass (Mia sagt, dass sie kommt.)\n"
           "- **Art und Weise**: indem (Du öffnest die Tür, indem du den Griff drückst.)",
           merke="weil, da, obwohl, damit, wenn, dass, sodass, nachdem, während, bevor, indem leiten Nebensätze ein. Das Verb steht am Ende."),
        lb(L3,
           "Zwischen Hauptsatz und Nebensatz steht **immer ein Komma**. Hier darf es nicht wegfallen.\n"
           "Der Nebensatz kann an drei Stellen stehen:\n"
           "- **hinten**: Wir gehen raus, obwohl es regnet. (Das Komma steht **vor** der Konjunktion.)\n"
           "- **vorn**: Obwohl es regnet, gehen wir raus. (Der Hauptsatz beginnt danach mit der **Personalform**.)\n"
           "- **in der Mitte** (eingeschoben): Wir gehen, obwohl es regnet, raus. (**Zwei** Kommas: eins davor und eins dahinter.)",
           merke="Komma zwischen Haupt- und Nebensatz, immer. Eingeschobener Nebensatz: zwei Kommas. Steht der Nebensatz vorn, folgt die Personalform."),
        lb(L4,
           "Ein **Satzbauplan** zeigt, wie ein Satz aufgebaut ist. **Hs** = Hauptsatz, **Ns** = Nebensatz.\n"
           "- **Hs , Ns**: Ole freut sich, dass Mia kommt. (Nebensatz hinten)\n"
           "- **Ns , Hs**: Wenn die Sonne scheint, gehen wir raus. (Nebensatz vorn)\n"
           "- **Hs , Ns , Hs**: Das Kind hat, weil es Hunger hatte, einen Apfel gegessen. (Nebensatz in der Mitte; der Hauptsatz wird fortgesetzt)\n"
           "- **Hs , Hs**: Ole lacht, denn der Witz ist gut. (Satzreihe, kein Nebensatz)",
           merke="Satzbaupläne: Hs , Ns – Ns , Hs – Hs , Ns , Hs. Bei einer Satzreihe: Hs , Hs."),
        lb(L5,
           "Ein **Relativsatz** ist ein **Nebensatz**, der mit **der, die, das** beginnt. Er bezieht sich auf ein **Nomen** davor und sagt etwas darüber:\n"
           "- Der Dieb, **der** eine Mütze trägt, flüchtet.\n"
           "- Die Tasche, **die** auf dem Tisch lag, war leer.\n"
           "- Das Kind, **das** lacht, heißt Ole.\n"
           "Das **Relativpronomen** richtet sich nach dem Nomen davor (Dieb → der, Tasche → die, Kind → das, Kinder → die). Die **Personalform** steht am **Ende**.\n"
           "Der Relativsatz wird mit **Komma** abgetrennt. Steht er mitten im Satz, setzt man **zwei Kommas**: Der Hund, der gern bellt, gehört Mia. Das ist der Plan **Hs , Ns , Hs**.",
           merke="Relativsatz = Nebensatz mit der, die, das. Zwei Kommas, wenn er mitten im Satz steht."),
    ]


def aufgaben():
    a = []
    # ---------------------------------------------------------------- A
    a.append(mc("Wo steht die Personalform im Nebensatz?", "Am Ende", ["An zweiter Stelle", "An erster Stelle", "Direkt nach der Konjunktion"], B_A,
                info="Im Nebensatz steht die Personalform an letzter Stelle (am Satzende): …, weil er krank ist."))
    a.append(mc("Mia freut sich, weil die Sonne scheint. Welcher Teil ist der Nebensatz?",
                "weil die Sonne scheint", ["Mia freut sich", "die Sonne", "Mia"], B_A,
                info="Der Nebensatz beginnt mit der Konjunktion „weil“ und hat das Verb „scheint“ am Ende. „Mia freut sich“ ist der Hauptsatz."))
    a.append(tf("Ein Nebensatz kann allein stehen.", False, B_A,
                info="Ein Nebensatz ist dem Hauptsatz untergeordnet und kann nicht allein stehen. „weil die Sonne scheint“ ist kein vollständiger Satz."))
    a.append(tf("Ein Satzgefüge besteht aus mindestens einem Hauptsatz und mindestens einem Nebensatz.", True, B_A,
                info="So steht es im Merkkasten des Buchs. Im Heft heißt es „aus einem Hauptsatz und mindestens einem weiteren Nebensatz“. Beides ist richtig."))
    a.append(kurz("Ole bleibt zu Hause, weil er krank ist. Schreibe die Personalform am Ende des Nebensatzes auf.", "ist", B_A,
                  info="Im Nebensatz steht die Personalform am Satzende: weil er krank ist."))
    a.append(kurz("Wir gehen schwimmen, obwohl es kalt ist. Schreibe die unterordnende Konjunktion auf.", "obwohl", B_A,
                  info="„obwohl“ leitet den Nebensatz ein. Er drückt eine Einschränkung aus."))
    a.append(mc("Welcher Satz ist ein Nebensatz?", "weil es regnet", ["Es regnet.", "Wir bleiben zu Hause.", "Der Regen fällt."], B_A,
                info="„weil es regnet“ beginnt mit einer Konjunktion, das Verb steht am Ende und der Satz kann nicht allein stehen."))
    a.append(mc("Woran erkennt man einen Nebensatz?", "Die Personalform steht am Ende.",
                ["Er beginnt immer mit einem Nomen.", "Er steht immer am Satzanfang.", "Er hat kein Verb."], B_A,
                info="Das sicherste Zeichen ist die Stellung der Personalform: Im Nebensatz steht sie am Satzende, im Hauptsatz an zweiter Stelle."))

    # ---------------------------------------------------------------- B
    a.append(zuordnen("Welche Bedeutung hat die Konjunktion?",
                      [("weil", "Begründung"), ("da", "Begründung"), ("obwohl", "Einschränkung"), ("nachdem", "Zeit"), ("damit", "Zweck"), ("sodass", "Folge")],
                      B_B, info="weil und da begründen, obwohl schränkt ein, nachdem nennt die Zeit, damit nennt den Zweck, sodass nennt die Folge."))
    a.append(mc("Welche Wörter sind unterordnende Konjunktionen? (mehrere Antworten sind richtig)",
                ["weil", "obwohl", "damit", "nachdem"], ["denn", "aber"], B_B,
                info="weil, obwohl, damit und nachdem leiten Nebensätze ein. „denn“ und „aber“ verbinden Hauptsätze."))
    a.append(mc("Welche Konjunktion passt? Wir gehen spazieren, … es regnet.", "obwohl", ["weil", "damit", "nachdem"], B_B,
                info="Es regnet, trotzdem gehen wir spazieren. Das ist eine Einschränkung: obwohl."))
    a.append(mc("Welche Konjunktion passt? Ole übt jeden Tag, … er besser wird.", "damit", ["obwohl", "nachdem", "bevor"], B_B,
                info="Das Üben hat einen Zweck, nämlich besser zu werden: damit."))
    a.append(luecke("Ergänze die passende Konjunktion.",
                    "Ich lerne, {{damit}} ich eine gute Note bekomme. Er lacht, {{weil}} der Witz lustig ist. Wir spielen draußen, {{obwohl}} es kalt ist.", B_B,
                    extra=["nachdem", "bevor"], info="damit nennt den Zweck, weil die Begründung, obwohl die Einschränkung."))
    a.append(luecke("Ergänze die passende Konjunktion.",
                    "Mia putzt die Zähne, {{bevor}} sie ins Bett geht. Wir essen Eis, {{nachdem}} wir geschwommen sind. Er singt, {{während}} er kocht.", B_B,
                    extra=["weil", "damit"], info="bevor = vor einer Handlung, nachdem = nach einer Handlung, während = gleichzeitig."))
    a.append(tf("„denn“ und „weil“ nennen beide eine Begründung, verlangen aber eine andere Wortstellung.", True, B_B,
                info="Nach „denn“ steht ein Hauptsatz (… denn ich bin müde), nach „weil“ ein Nebensatz (… weil ich müde bin)."))
    a.append(mc("Welcher Satz ist richtig?", "Ich bleibe zu Hause, weil ich müde bin.",
                ["Ich bleibe zu Hause, weil ich bin müde.", "Ich bleibe zu Hause, weil bin ich müde.", "Ich bleibe zu Hause weil ich müde bin."], B_B,
                info="Im Nebensatz steht die Personalform „bin“ am Ende. Vor „weil“ steht ein Komma."))
    a.append(mc("Was drückt „obwohl“ aus?", "eine Einschränkung", ["eine Begründung", "einen Zweck", "einen Zeitpunkt"], B_B,
                info="Mit „obwohl“ nennt man etwas, das gegen die Erwartung gilt: Wir gehen raus, obwohl es regnet."))
    a.append(tf("Mit „weil“ und „denn“ kann man dieselbe Begründung ausdrücken: …, denn ich bin müde. / …, weil ich müde bin.", True, B_B,
                info="Beide Sätze haben denselben Sinn. Der Satz mit „denn“ ist eine Satzreihe, der Satz mit „weil“ ein Satzgefüge."))

    # ---------------------------------------------------------------- C
    a.append(kommas("Ole bleibt zu Hause {,} weil er krank ist.", B_C, "Vor „weil“ steht immer ein Komma: Haupt- und Nebensatz werden getrennt."))
    a.append(kommas("Mia lacht {,} obwohl der Witz nicht lustig ist.", B_C, "Vor „obwohl“ steht ein Komma."))
    a.append(kommas("Wir gehen schwimmen {,} wenn die Sonne scheint.", B_C, "Vor „wenn“ steht ein Komma, wenn der Nebensatz hinten steht."))
    a.append(kommas("Nachdem wir gegessen haben {,} spielen wir Fußball.", B_C, "Steht der Nebensatz vorn, folgt das Komma hinter dem Nebensatz (vor der Personalform des Hauptsatzes)."))
    a.append(kommas("Weil es regnet {,} bleiben wir drinnen.", B_C, "Nach dem Nebensatz „Weil es regnet“ steht ein Komma."))
    a.append(kommas("Ich putze die Zähne {,} bevor ich ins Bett gehe.", B_C, "Vor „bevor“ steht ein Komma."))
    a.append(kommas("Der Hund bellt {,} damit niemand näher kommt.", B_C, "Vor „damit“ steht ein Komma."))
    a.append(kommas("Meine Schwester sagt {,} dass sie Hunger hat.", B_C, "Auch vor „dass“ steht ein Komma."))
    a.append(mc("Wann steht im Satzgefüge ein Komma?", "Immer zwischen Hauptsatz und Nebensatz.",
                ["Nur vor „und“.", "Nie.", "Nur nach dem Nebensatz am Ende des Satzes."], B_C,
                info="Zwischen Haupt- und Nebensatz muss immer ein Komma stehen, egal ob der Nebensatz vorn, in der Mitte oder hinten steht."))
    a.append(tf("Zwischen Haupt- und Nebensatz darf das Komma wegfallen.", False, B_C,
                info="Das gilt nur für „und“ und „oder“ in der Satzreihe. Zwischen Hauptsatz und Nebensatz muss das Komma stehen."))
    a.append(kurz("Schreibe den Satz mit dem richtigen Komma ab: Ich gehe nach Hause weil ich müde bin.",
                  "Ich gehe nach Hause, weil ich müde bin.", B_C, gross=True,
                  info="Das Komma steht vor „weil“, direkt zwischen Hauptsatz und Nebensatz."))
    a.append(kurz("Schreibe den Satz mit dem richtigen Komma ab: Wenn die Sonne scheint gehen wir in den Park.",
                  "Wenn die Sonne scheint, gehen wir in den Park.", B_C, gross=True,
                  info="Der Nebensatz steht vorn. Das Komma steht hinter dem Nebensatz, vor „gehen“."))
    a.append(mc("Welcher Satz ist richtig geschrieben?", "Obwohl es kalt ist, gehen wir raus.",
                ["Obwohl es kalt ist gehen wir raus.", "Obwohl, es kalt ist gehen wir raus.", "Obwohl es kalt ist gehen, wir raus."], B_C,
                info="Der Nebensatz steht vorn, danach steht das Komma. Der Hauptsatz beginnt mit der Personalform „gehen“."))

    # ---------------------------------------------------------------- D
    a.append(zuordnen("Wo steht der Nebensatz?",
                      [("Weil es regnet, bleiben wir zu Hause.", "Nebensatz vorn"), ("Wir bleiben zu Hause, weil es regnet.", "Nebensatz hinten"),
                       ("Wir bleiben, weil es regnet, zu Hause.", "Nebensatz in der Mitte"), ("Obwohl er müde war, ging er laufen.", "Nebensatz vorn"),
                       ("Er ging laufen, obwohl er müde war.", "Nebensatz hinten")],
                      B_D, info="Vorn: Der Satz beginnt mit der Konjunktion. Hinten: Der Satz endet mit dem Nebensatz. In der Mitte: Der Nebensatz ist in den Hauptsatz eingeschoben (zwei Kommas)."))
    a.append(kommas("Mia hat {,} weil sie Durst hatte {,} ein Glas Wasser getrunken.", B_D,
                    "Der Nebensatz ist eingeschoben. Deshalb stehen zwei Kommas: eins davor und eins dahinter."))
    a.append(kommas("Wir sind {,} obwohl es regnete {,} spazieren gegangen.", B_D,
                    "Der Nebensatz „obwohl es regnete“ steht in der Mitte. Er wird von zwei Kommas eingeschlossen."))
    a.append(kommas("Mama hat {,} damit wir pünktlich kommen {,} den Wecker gestellt.", B_D,
                    "Auch hier ist der Nebensatz eingeschoben: zwei Kommas."))
    a.append(mc("Wie beginnt der Hauptsatz, wenn der Nebensatz vorn steht?", "Mit der Personalform",
                ["Mit einem Nomen", "Mit einer Konjunktion", "Mit einem Komma"], B_D,
                info="Beispiel: Weil es regnet, bleiben wir zu Hause. Nach dem Komma steht zuerst die Personalform „bleiben“."))
    a.append(mc("Beginne mit dem Nebensatz: Ich ziehe eine Jacke an, weil es kalt ist. Welcher Satz ist richtig?",
                "Weil es kalt ist, ziehe ich eine Jacke an.",
                ["Weil es kalt ist, ich ziehe eine Jacke an.", "Weil es kalt ist ziehe ich eine Jacke an.", "Weil ich eine Jacke anziehe, ist es kalt."], B_D,
                info="Der Nebensatz steht vorn, dahinter folgt ein Komma und der Hauptsatz beginnt mit der Personalform „ziehe“. Der Sinn bleibt gleich."))
    a.append(kurz("Beginne mit dem Nebensatz: Wir spielen draußen, obwohl es kalt ist.", "Obwohl es kalt ist, spielen wir draußen.", B_D, gross=True,
                  info="Der Nebensatz kommt nach vorn, dann das Komma, dann der Hauptsatz mit der Personalform an erster Stelle: Obwohl es kalt ist, spielen wir draußen."))
    a.append(kurz("Beginne mit dem Nebensatz: Ole putzt die Zähne, bevor er ins Bett geht.", "Bevor er ins Bett geht, putzt Ole die Zähne.", B_D, gross=True,
                  info="Nebensatz vorn, Komma, Hauptsatz mit der Personalform: Bevor er ins Bett geht, putzt Ole die Zähne."))

    # ---------------------------------------------------------------- E
    a.append(zuordnen("Welcher Satzbauplan passt?",
                      [("Ich bleibe zu Hause, weil ich müde bin.", "Hs , Ns"), ("Weil ich müde bin, bleibe ich zu Hause.", "Ns , Hs"),
                       ("Ich bleibe, weil ich müde bin, zu Hause.", "Hs , Ns , Hs"), ("Wir spielen, obwohl es regnet.", "Hs , Ns"),
                       ("Nachdem wir gegessen hatten, gingen wir raus.", "Ns , Hs"), ("Mia hat, damit sie pünktlich ist, den Wecker gestellt.", "Hs , Ns , Hs")],
                      B_E, info="Hs = Hauptsatz, Ns = Nebensatz. Steht der Nebensatz hinten, ist es „Hs , Ns“, vorn „Ns , Hs“, in der Mitte „Hs , Ns , Hs“."))
    a.append(mc("Welcher Satzbauplan passt zu: Wenn die Sonne scheint, gehen wir raus.?", "Ns , Hs", ["Hs , Ns", "Hs , Ns , Hs", "Hs , Hs"], B_E,
                info="Der Nebensatz „Wenn die Sonne scheint“ steht vorn, danach folgt der Hauptsatz."))
    a.append(mc("Welcher Satzbauplan passt zu: Ole freut sich, dass Mia kommt.?", "Hs , Ns", ["Ns , Hs", "Hs , Ns , Hs", "Hs , Hs"], B_E,
                info="Der Hauptsatz „Ole freut sich“ steht vorn, der Nebensatz „dass Mia kommt“ steht hinten."))
    a.append(mc("Welcher Satzbauplan passt zu: Das Kind hat, weil es Hunger hatte, einen Apfel gegessen.?", "Hs , Ns , Hs", ["Hs , Ns", "Ns , Hs", "Hs , Hs"], B_E,
                info="Der Nebensatz ist in den Hauptsatz eingeschoben, der Hauptsatz wird danach fortgesetzt."))
    a.append(mc("Welcher Satz passt zum Plan „Ns , Hs“?", "Als der Regen aufhörte, gingen wir raus.",
                ["Wir gingen raus, als der Regen aufhörte.", "Wir gingen, als der Regen aufhörte, raus.", "Wir gingen raus, und der Regen hörte auf."], B_E,
                info="Bei „Ns , Hs“ steht der Nebensatz vorn. Der Hauptsatz folgt mit der Personalform an erster Stelle."))
    a.append(tf("Beim Plan „Hs , Ns , Hs“ steht der Nebensatz in der Mitte des Hauptsatzes.", True, B_E,
                info="Der Hauptsatz wird durch den Nebensatz unterbrochen und danach fortgesetzt. Davor und dahinter steht ein Komma."))
    a.append(zuordnen("Benenne die Teile des Satzes: Weil es regnet, bleiben wir zu Hause.",
                      [("Weil es regnet", "Nebensatz"), ("bleiben wir zu Hause", "Hauptsatz"), ("weil", "Konjunktion"),
                       ("bleiben", "Personalform im Hauptsatz"), ("regnet", "Personalform im Nebensatz")],
                      B_E, info="Der Nebensatz beginnt mit der Konjunktion „weil“ und hat die Personalform „regnet“ am Ende. Im Hauptsatz steht „bleiben“ an erster Stelle des Satzteils."))
    a.append(luecke("Ergänze den Satzbauplan mit Hs (Hauptsatz) und Ns (Nebensatz).",
                    "Ich lache, weil es lustig ist: {{Hs}} , {{Ns}}\nWeil es lustig ist, lache ich: {{Ns}} , {{Hs}}", B_E, fest=True,
                    info="Im ersten Satz steht der Hauptsatz vorn, im zweiten der Nebensatz."))

    # ---------------------------------------------------------------- F
    a.append(mc("Welches Relativpronomen passt? Der Hund, … bellt, gehört Mia.", "der", ["die", "das", "dem"], B_F,
                info="„Hund“ ist männlich (der Hund), deshalb beginnt der Relativsatz mit „der“."))
    a.append(mc("Welches Relativpronomen passt? Die Tasche, … auf dem Tisch lag, war leer.", "die", ["der", "das", "dem"], B_F,
                info="„Tasche“ ist weiblich (die Tasche), deshalb „die“."))
    a.append(mc("Welches Relativpronomen passt? Das Kind, … lacht, heißt Ole.", "das", ["der", "die", "dem"], B_F,
                info="„Kind“ ist sächlich (das Kind), deshalb „das“."))
    a.append(mc("Welches Relativpronomen passt? Die Kinder, … am Teich spielen, sind laut.", "die", ["der", "das", "dem"], B_F,
                info="„Kinder“ steht in der Mehrzahl, dafür gilt „die“."))
    a.append(kommas("Der Hund {,} der gern bellt {,} gehört Mia.", B_F,
                    "Der Relativsatz „der gern bellt“ steht mitten im Satz. Er wird von zwei Kommas eingeschlossen."))
    a.append(kommas("Das Mädchen {,} das gerade lacht {,} heißt Pia.", B_F,
                    "Der Relativsatz steht in der Mitte, deshalb zwei Kommas."))
    a.append(kurz("Verbinde mit einem Relativsatz: Der Dieb flüchtet. Der Dieb trägt eine Mütze.", "Der Dieb, der eine Mütze trägt, flüchtet.", B_F, gross=True,
                  info="Der zweite Satz wird zum Relativsatz „der eine Mütze trägt“ und mitten in den ersten Satz eingeschoben (zwei Kommas, Personalform am Ende)."))
    a.append(mc("Welchen Satzbauplan hat: Der Dieb, der eine Mütze trägt, flüchtet.?", "Hs , Ns , Hs", ["Hs , Ns", "Ns , Hs", "Hs , Hs"], B_F,
                info="Der Relativsatz ist ein Nebensatz und steht mitten im Hauptsatz: „Der Dieb … flüchtet“ ist der Hauptsatz."))
    return a


def build():
    p = pack(ID, "Deutsch Teil 2b: Das Satzgefüge",
             "Haupt- und Nebensatz, unterordnende Konjunktionen und ihre Bedeutung, Kommas im Satzgefüge (Nebensatz vorn, in der Mitte, hinten), Satzbaupläne und ein kleiner Relativsatz-Block (so weit wie auf der Seite „Teste dich“ im Aufgabenheft). Mit Lernblatt und Übungsaufgaben.",
             lernblatt(), aufgaben(), min_aufgaben=50,
             hinweis="Alle Sätze, Texte und Namen sind selbst ausgedacht, nicht aus dem Deutschbuch oder Aufgabenheft. Kommas wählst du in einer Liste aus („Komma“ oder „kein Komma“). Beim Abschreiben zählt jeder Buchstabe und jedes Komma. Relativsätze üben wir nur so weit, wie sie im Aufgabenheft („Teste dich“, S. 61) vorkommen.")
    return [nachlesen(p, {B_A: L1, B_B: L2, B_C: L3, B_D: L3, B_E: L4, B_F: L5})]


if __name__ == "__main__":
    for p in build():
        print(p["id"], len(p["aufgaben"]), "Aufgaben")
