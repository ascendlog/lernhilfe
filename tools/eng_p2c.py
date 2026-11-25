"""Englisch Klasse 6, Paket 2c: Wortschatz 2 (get, Possessivpronomen, Beschreiben, Dinge und Orte, Verben, Satzzeichen).

Wörter und Bedeutungen laut Vokabelliste Unit 2 (Buch S. 184–187). Alle Beispielsätze und Texte sind selbst geschrieben.
"""
from eng_vok import *

ID = "englisch-2c-wortschatz-2"

B_A = "A – get: ein Wort, viele Bedeutungen"
B_B = "B – Possessivpronomen: mine, yours, hers …"
B_C = "C – Beschreiben: Adjektive und kleine Wörter"
B_D = "D – Dinge und Orte"
B_E = "E – Verben und ihre Vergangenheit"
B_F = "F – Satzzeichen"

L1 = "get – ein Wort, viele Bedeutungen"
L2 = "Possessivpronomen: my und mine"
L3 = "Beschreiben: Adjektive und kleine Wörter"
L4 = "Dinge und Orte"
L5 = "Verben und Wendungen"
L6 = "Satzzeichen"


def lernblatt():
    return [
        lb(L1,
           "**(to) get** (Simple Past: **got**) hat je nach Satz ganz verschiedene Bedeutungen:\n\n"
           "- **bekommen:** I get a letter from my aunt every month.\n"
           "- **besorgen, holen:** Can you get some bread from the shop?\n"
           "- **gelangen, (hin)kommen:** How do we get to the station?\n"
           "- **werden:** It gets dark early in winter.\n\n"
           "Dazu kommen feste Wendungen:\n\n"
           "- **(to) get on** = vorankommen, zurechtkommen\n"
           "- **(to) get on / off (the bus)** = ein- / aussteigen\n"
           "- **(to) get ready (for)** = sich fertig machen (für)\n"
           "- **(to) get up** = aufstehen",
           merke="get = bekommen, holen, gelangen, werden. get up = aufstehen, get ready = sich fertig machen, get on / off = ein- / aussteigen."),
        lb(L2,
           "Zu jedem Personalpronomen gibt es zwei Possessivformen:\n\n"
           "- **my** steht vor einem Nomen: This is my bag.\n"
           "- **mine** steht allein: This bag is mine. (meiner, meine, meins)\n\n"
           "Die Reihe:\n\n"
           "- I → my → **mine**\n"
           "- you → your → **yours**\n"
           "- he → his → **his**\n"
           "- she → her → **hers**\n"
           "- we → our → **ours**\n"
           "- they → their → **theirs**\n\n"
           "**Whose …?** heißt „wessen …?“: Whose bike is that? – It's mine. Nach mine, yours, hers, ours, theirs steht **kein Nomen** und **kein Apostroph**: The bag is theirs (nicht their's).",
           merke="my + Nomen, mine allein. his bleibt his. Kein Apostroph bei yours, hers, ours, theirs."),
        lb(L3,
           "Wörter zum **Beschreiben**:\n\n"
           "- **big / large** = groß (austauschbar bei Dingen: a big / large lake). **large** nimmt man in der Regel nicht für Menschen.\n"
           "- **tall** = groß bei Menschen und Tieren, hoch bei Gebäuden und Bäumen: a tall man, a tall tree.\n"
           "- **awful** = schrecklich; **lovely** = schön, hübsch, herrlich; **brilliant** = großartig, genial\n"
           "- **scared** = verängstigt (ich fühle mich so); **scary** = unheimlich, gruselig (der Film ist so)\n"
           "- **shy** = schüchtern; **clear** = klar, deutlich; **correct** = richtig, korrekt\n"
           "- **even** = sogar; **so far** = bis jetzt; **a bit** = ein bisschen; **about** = ungefähr\n\n"
           "Merke den Unterschied: Der Film war **scary**. Ich war **scared**.",
           merke="tall für Menschen und Höhe, big und large für Größe. scared = verängstigt, scary = gruselig."),
        lb(L4,
           "**Dinge und Orte** der Unit:\n\n"
           "- **(the) earth** = die Erde; **plane** = Flugzeug; **town hall** = Rathaus; **snow** = Schnee\n"
           "- **paw** = Pfote, Tatze; **stairs** (nur Plural) = Treppe; **upstairs** = oben (die Treppe hinauf), **downstairs** = unten\n"
           "- **square kilometre (sq km)** = Quadratkilometer; **round the world** = um die Welt\n"
           "- **fork** = Gabel; **knife** (Plural **knives**) = Messer; **spoon** = Löffel\n"
           "- **size** = Größe: What size are your shoes?\n\n"
           "**Achtung bei den Präpositionen:** Im Flugzeug heißt auf Englisch **on the plane**, auf der Erde **on earth**.",
           merke="knife – knives. Im Flugzeug: on the plane. stairs ist ein Pluralwort."),
        lb(L5,
           "**Verben und Wendungen** mit ihrer Vergangenheit (Simple Past):\n\n"
           "- (to) **ring** – **rang** (klingeln, läuten)\n"
           "- (to) **mean** – **meant** (bedeuten; meinen, sagen wollen): What does this word mean? / What do you mean?\n"
           "- (to) **get** – **got**\n"
           "- (to) **lie** – **lay** (liegen), -ing-Form: **lying**\n"
           "- (to) **wake sb. up** – **woke up** (jemanden aufwecken)\n"
           "- (to) **stick sth. into sth.** – **stuck** (etwas in etwas stecken)\n"
           "- (to) **change** = (ver)ändern; (to) **pause** = innehalten, pausieren\n"
           "- (to) **make sure that …** = darauf achten, dass …; (to) **read aloud** = laut vorlesen\n"
           "- **could** = konnte(n) oder könnte(n): We could go to the cinema.\n"
           "- **like this** = so: Do it like this.",
           merke="ring – rang, mean – meant, get – got, lie – lay (lying), wake up – woke up, stick – stuck."),
        lb(L6,
           "Die **Satzzeichen** (punctuation) auf Englisch:\n\n"
           "- **.** = full stop (Punkt)\n"
           "- **,** = comma (Komma)\n"
           "- **:** = colon (Doppelpunkt)\n"
           "- **?** = question mark (Fragezeichen)\n"
           "- **!** = exclamation mark (Ausrufezeichen)\n"
           "- **-** = hyphen (Bindestrich)\n\n"
           "Am Satzende steht ein full stop, nach einer Frage ein question mark und nach einem Ausruf ein exclamation mark.",
           merke="full stop, comma, colon, question mark, exclamation mark, hyphen."),
    ]


def get_mc(satz, richtig, abschnitt=B_A):
    optionen = ["bekommen", "besorgen, holen", "gelangen, (hin)kommen", "werden"]
    assert richtig in optionen
    return mc_fest(f"Was bedeutet „get“ in diesem Satz? {satz}", optionen, richtig, abschnitt,
                   info=f"In diesem Satz bedeutet get „{richtig}“. get hat je nach Satz vier Bedeutungen: bekommen, besorgen, gelangen, werden.")


def aufgaben():
    a = []
    # ---------------------------------------------------------------- A: get
    a.append(get_mc("I get a letter from my aunt every month.", "bekommen"))
    a.append(get_mc("Can you get some bread from the shop?", "besorgen, holen"))
    a.append(get_mc("How do we get to the station?", "gelangen, (hin)kommen"))
    a.append(get_mc("It gets dark early in winter.", "werden"))
    a.append(zuordnen("Ordne die Wendung der Bedeutung zu.",
                      [("get up", "aufstehen"), ("get ready", "sich fertig machen"), ("get on", "vorankommen, zurechtkommen"), ("get on the bus", "in den Bus einsteigen"), ("get off the bus", "aus dem Bus aussteigen")], B_A,
                      info="get up = aufstehen, get ready = sich fertig machen, get on = vorankommen, get on the bus = einsteigen, get off the bus = aussteigen."))
    a.append(luecke("Ergänze die Wendungen mit get.",
                    "I always {{get up}} at seven. Then I {{get ready}} for school. I {{get on}} the bus at twenty to eight and {{get off}} at the school gate.",
                    B_A, extra=["get in", "get over"],
                    info="get up = aufstehen, get ready = sich fertig machen, get on the bus = einsteigen, get off = aussteigen."))
    a.append(kurz("Schreibe die Vergangenheit (Simple Past) von „get“.", ["got"], B_A,
                  info="get ist unregelmäßig: get – got. Beispiel: Yesterday I got a new bike."))
    a.append(kurz("Wie sagt man „aufstehen“ auf Englisch?", ["get up", "to get up"], B_A,
                  info="get up = aufstehen. Beispiel: I get up at seven."))
    a.append(tf("„get off the bus“ bedeutet „in den Bus einsteigen“.", False, B_A,
                info="get on = einsteigen, get off = aussteigen. Die Wörter on und off verraten es."))

    # ---------------------------------------------------------------- B: Possessivpronomen
    a.append(zuordnen("Ordne dem Personalpronomen das Possessivpronomen (allein stehend) zu.",
                      [("I", "mine"), ("you", "yours"), ("she", "hers"), ("we", "ours"), ("they", "theirs")], B_B,
                      info="I → mine, you → yours, she → hers, we → ours, they → theirs. he hat his (wie vor einem Nomen)."))
    a.append(luecke("Ergänze das Possessivpronomen.",
                    "That is my bag. It's {{mine}}.\nThis is your pen. It's {{yours}}.\nThat is Mia's coat. It's {{hers}}.\nThis is our car. It's {{ours}}.\nThose are their books. They are {{theirs}}.",
                    B_B, extra=["his", "its"],
                    info="my → mine, your → yours, Mia's (= her) → hers, our → ours, their → theirs. Danach steht kein Nomen."))
    a.append(luecke("Wähle my / mine und your / yours.",
                    "This is {{my}} bike. The red bike is {{mine}}.\nIs that {{your}} jacket? No, it is not {{yours}}.",
                    B_B, auswahl=["my", "mine", "your", "yours"],
                    info="my und your stehen vor einem Nomen (my bike, your jacket). mine und yours stehen allein."))
    a.append(mc("Whose bike is that? – It's Tom's. It's …", "his", ["hers", "mine", "theirs"], B_B,
                info="Tom ist he. Possessivpronomen für he ist his."))
    a.append(mc("Are these your pencils? – No, they aren't. They're Ella's. They're …", "hers", ["his", "ours", "yours"], B_B,
                info="Ella ist she. Das allein stehende Possessivpronomen für she ist hers."))
    a.append(kurz("Wie heißt „unserer, unsere, unseres“ (allein stehend) auf Englisch?", ["ours"], B_B,
                  info="we → our (vor Nomen) und ours (allein): Whose house is that? – It's ours."))
    a.append(kurz("Wie heißt „wessen?“ auf Englisch?", ["whose"], B_B,
                  info="whose = wessen? Beispiel: Whose scarf is this?"))
    a.append(tf("„The red scarf is her.“ ist richtig.", False, B_B,
                info="Allein stehend heißt es hers: The red scarf is hers."))
    a.append(mc("Welcher Satz ist richtig geschrieben?", "The pencil case is theirs.",
                ["The pencil case is their's.", "The pencil case is theirs'.", "The pencil case is their."], B_B,
                info="theirs wird ohne Apostroph geschrieben. Allein stehend steht theirs, nicht their."))
    a.append(tf("„his“ passt vor einem Nomen (his dog) und allein (It's his).", True, B_B,
                info="Bei he ist beides his: his dog, The dog is his."))

    # ---------------------------------------------------------------- C: Beschreiben
    a.append(mc("Welches Wort passt? A very … building. (Höhe)", "tall", ["small", "awful", "shy"], B_C,
                info="tall benutzt man bei der Höhe von Gebäuden, Bäumen und bei der Größe von Menschen."))
    a.append(tf("„large“ benutzt man in der Regel nicht, um Menschen zu beschreiben.", True, B_C,
                info="Für Menschen sagt man tall (groß) oder big (kräftig). large nimmt man eher bei Dingen: a large house."))
    a.append(zuordnen("Ordne das englische Adjektiv der deutschen Bedeutung zu.",
                      [("awful", "schrecklich"), ("lovely", "schön, herrlich"), ("brilliant", "großartig, genial"), ("shy", "schüchtern"), ("scared", "verängstigt")], B_C,
                      info="awful = schrecklich, lovely = schön, brilliant = großartig, shy = schüchtern, scared = verängstigt."))
    a.append(luecke("Ergänze scary oder scared.",
                    "The ghost story was {{scary}}, and the children were {{scared}}.",
                    B_C, extra=["shy", "awful"],
                    info="scary beschreibt, wie etwas ist (gruselig). scared beschreibt, wie man sich fühlt (verängstigt)."))
    a.append(luecke("Ergänze die Wörter.",
                    "The weather was {{lovely}} on Saturday, but on Sunday it was {{awful}}. {{Even}} the dog did not want to go out.",
                    B_C, extra=["shy", "large"],
                    info="lovely = herrlich, awful = schrecklich, even = sogar."))
    a.append(en_kurz("brilliant", B_C))
    a.append(en_kurz("so far", B_C))
    a.append(en_kurz("clear", B_C))
    a.append(tf("„correct“ bedeutet „falsch“.", False, B_C,
                info="correct = richtig, korrekt. Das Gegenteil ist wrong."))
    a.append(kurz("Welches Wort passt? What … are your shoes? Schreibe das Wort für „Größe“.", ["size"], B_C,
                  info="size = Größe. Beispiel: What size are your shoes?"))

    # ---------------------------------------------------------------- D: Dinge und Orte
    a.append(paare_zu(["earth", "plane", "town hall", "snow", "paw"], B_D))
    a.append(paare_zu(["stairs", "fork", "knife", "spoon", "round the world"], B_D))
    a.append(mc("Wie heißt der Plural von „knife“?", "knives", ["knifes", "knifs", "knive"], B_D,
                info="knife → knives: Bei einigen Wörtern auf -fe wird f zu v: knife – knives."))
    a.append(tf("„stairs“ gibt es nur im Plural: The stairs are old.", True, B_D,
                info="stairs ist ein Pluralwort (Treppe, Treppenstufen)."))
    a.append(luecke("Ergänze die Wörter.",
                    "My bedroom is {{upstairs}}, the kitchen is {{downstairs}}.",
                    B_D, extra=["stairs", "plane"],
                    info="upstairs = oben (im oberen Stockwerk), downstairs = unten."))
    a.append(luecke("Ergänze das Besteck.",
                    "For dinner we use a {{knife}}, a {{fork}} and a {{spoon}}.",
                    B_D, extra=["paw", "stairs"],
                    info="knife = Messer, fork = Gabel, spoon = Löffel."))
    a.append(kurz("Wie schreibt man „Quadratkilometer“ auf Englisch? Schreibe das ganze Wort (zwei Wörter).", ["square kilometre", "square kilometer", "sq km"], B_D,
                  info="square kilometre (Abkürzung sq km) = Quadratkilometer."))
    a.append(mc("Wie sagt man „im Flugzeug“ auf Englisch?", "on the plane", ["in the plane", "at the plane", "by the plane"], B_D,
                info="Im Englischen sagt man on the plane (auch on the bus, on the train)."))
    a.append(mc("Wie sagt man „auf der Erde“ auf Englisch?", "on earth", ["in earth", "at earth", "by earth"], B_D,
                info="on earth = auf der Erde."))
    a.append(en_kurz("town hall", B_D))

    # ---------------------------------------------------------------- E: Verben
    a.append(zuordnen("Ordne dem Verb die Vergangenheit (Simple Past) zu.",
                      [("ring", "rang"), ("mean", "meant"), ("get", "got"), ("lie", "lay"), ("stick", "stuck")], B_E,
                      info="Alle fünf Verben sind unregelmäßig: ring – rang, mean – meant, get – got, lie – lay, stick – stuck."))
    a.append(luecke("Setze die Vergangenheit (Simple Past) ein.",
                    "Yesterday I {{got}} a letter. The bell {{rang}} at nine. I {{woke up}} at six. The cat {{lay}} in the sun. He {{stuck}} his hand into the bag. I did not understand what she {{meant}}.",
                    B_E, extra=["getted", "ringed", "waked up"],
                    info="get – got, ring – rang, wake up – woke up, lie – lay, stick – stuck, mean – meant."))
    a.append(mc("Was bedeutet „mean“ in: What does „umbrella“ mean?", "bedeuten", ["meinen, sagen wollen", "bekommen", "ändern"], B_E,
                info="Wenn man nach einer Bedeutung fragt, heißt mean „bedeuten“."))
    a.append(mc("Was bedeutet „mean“ in: I don't understand. What do you mean?", "meinen, sagen wollen", ["bedeuten", "ändern", "liegen"], B_E,
                info="In dieser Frage fragt man, was jemand sagen will: What do you mean? = Was meinst du?"))
    a.append(en_kurz("lie", B_E))
    a.append(kurz("Wie heißt die -ing-Form von „lie“?", ["lying"], B_E,
                  info="lie wird zu lying: Why are you lying there?"))
    a.append(kurz("Wie sagt man „jemanden aufwecken“ auf Englisch? Schreibe die Grundform.", ["wake sb. up", "wake somebody up", "wake someone up", "wake up", "to wake sb. up", "to wake up"], B_E,
                  info="(to) wake sb. up = jemanden aufwecken. Simple Past: woke up."))
    a.append(de_mc("change", B_E))
    a.append(tf("„could“ bedeutet nur „kann“.", False, B_E,
                info="could = konnte(n) oder könnte(n). Beispiel: We could go to the cinema."))
    a.append(kurz("Übersetze: Wir könnten ins Kino gehen.", ["We could go to the cinema"], B_E,
                  info="could = könnten: We could go to the cinema."))
    a.append(tf("„Make sure that you close the door.“ bedeutet: Achte darauf, dass du die Tür schließt.", True, B_E,
                info="(to) make sure that … = darauf achten, dass …"))
    a.append(en_kurz("like this", B_E))

    # ---------------------------------------------------------------- F: Satzzeichen
    a.append(zuordnen("Ordne dem Satzzeichen den englischen Namen zu.",
                      [(".", "full stop"), (",", "comma"), (":", "colon"), ("?", "question mark"), ("!", "exclamation mark"), ("-", "hyphen")], B_F,
                      info=". = full stop, , = comma, : = colon, ? = question mark, ! = exclamation mark, - = hyphen."))
    a.append(mc("Wie heißt das Zeichen „:“ auf Englisch?", "colon", ["comma", "hyphen", "full stop"], B_F,
                info="Der Doppelpunkt heißt colon. Das comma ist das Komma."))
    a.append(kurz("Wie heißt das Zeichen „!“ auf Englisch?", ["exclamation mark"], B_F,
                  info="! = exclamation mark (Ausrufezeichen)."))
    a.append(luecke("Setze die Satzzeichen ein.",
                    "A {{full stop}} comes at the end of a sentence.\nA {{question mark}} comes after a question.\nA {{hyphen}} joins two words like in „well-known“.",
                    B_F, extra=["colon", "comma"],
                    info="full stop = Punkt, question mark = Fragezeichen, hyphen = Bindestrich."))
    return a


def build():
    p = pack(ID, "Englisch Teil 2c: Wortschatz (2) – get, Possessivpronomen, Wendungen",
             "Wortschatz zu Unit 2 „A school day“: get, Possessivpronomen (mine, yours, hers …), Adjektive zum Beschreiben, Dinge und Orte, Verben mit Vergangenheit, Satzzeichen. Mit Lernblatt und Übungsaufgaben.",
             lernblatt(), aufgaben(), min_aufgaben=34,
             hinweis="Wörter und Bedeutungen folgen der Vokabelliste Unit 2 (S. 184–187). Alle Sätze und Texte sind selbst ausgedacht. In den Antworten zählt jeder Buchstabe.")
    return [nachlesen(p, {B_A: L1, B_B: L2, B_C: L3, B_D: L4, B_E: L5, B_F: L6})]


if __name__ == "__main__":
    for p in build():
        print(p["id"], len(p["aufgaben"]), "Aufgaben")
