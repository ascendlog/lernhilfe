"""Englisch Klasse 6, Paket 2h: Schreiben (über meine Schule und meinen Schultag schreiben, Schulen vergleichen, Pläne, E-Mail).

Alle Sätze, Namen, Schulen und Zahlen sind selbst ausgedacht. Die Fakten über die Schule aus dem Buch (Plymstock) stehen nur im Buch:
hier wird mit einer erfundenen Schule (Greenfield School) und einer erfundenen deutschen Schule (Lindenschule) geübt.
"""
from eng_lib import *
from geo_lib import svg_tabelle

ID = "englisch-2h-schreiben"

B_A = "A – Meine Schule vorstellen"
B_B = "B – Mein Schultag"
B_C = "C – Zwei Schulen vergleichen"
B_D = "D – Pläne mit going to"
B_E = "E – Sätze verbinden und E-Mails"
B_F = "F – Eigene Texte schreiben"

L1 = "So planst du einen Text"
L2 = "Über meine Schule schreiben"
L3 = "Mein Schultag"
L4 = "Meine Schule mit einer englischen Schule vergleichen"
L5 = "Sätze verbinden: and, but, because, so"
L6 = "Pläne und E-Mails"


def lernblatt():
    return [
        lb(L1,
           "Ein guter Text hat **drei Teile**:\n\n"
           "- **Einleitung:** Worüber schreibst du? (My school is called …)\n"
           "- **Hauptteil:** Die wichtigsten Informationen, jede Information in einem eigenen Satz.\n"
           "- **Schluss:** Ein kurzer Satz zum Abschluss (My school is great!).\n\n"
           "So gehst du vor:\n\n"
           "- **Stichwörter sammeln:** Was willst du erzählen? Schreibe 4 bis 6 Stichpunkte.\n"
           "- **Sätze bauen:** Jeder Satz hat ein Subjekt und ein Verb (I go, we have, she likes).\n"
           "- **Verbinden:** Benutze and, but, because und so.\n"
           "- **Kontrollieren:** Großschreibung am Satzanfang, Punkt am Ende, Rechtschreibung, -s bei he/she/it, Zahlen und Uhrzeiten.\n\n"
           "**Tipp:** Schreibe lieber einfache Sätze, die richtig sind, als lange Sätze mit vielen Fehlern.",
           merke="Einleitung, Hauptteil, Schluss. Erst Stichwörter, dann Sätze, dann kontrollieren."),
        lb(L2,
           "Mit diesen Satzanfängen kannst du deine Schule vorstellen:\n\n"
           "- **My school is called** Linden School. / **It is in** a small town.\n"
           "- **There are** 450 students and 30 teachers **at my school.**\n"
           "- **We have** six lessons every day. / **We don't have** a uniform.\n"
           "- **My favourite subject is** art **because** it is fun.\n"
           "- **I go to school by** bus. / **I walk to school.**\n"
           "- **The school has** a big playground and a library.\n\n"
           "**Achtung:** **There are** (mit mehreren Dingen), **there is** (mit einem Ding). Bei Zahlen: six hundred (ohne -s bei hundred).\n\n"
           "Ein **Uniform** (school uniform) ist die einheitliche Schulkleidung. Man sagt: **We wear a uniform** (wir tragen) und **We don't wear a uniform.**",
           merke="My school is called … / There are … / We have … / My favourite subject is … / I go to school by …"),
        lb(L3,
           "Einen **Schultag** beschreibst du in der richtigen **Reihenfolge**. Diese Wörter helfen:\n\n"
           "- **first** (zuerst), **then** (dann), **after that** (danach), **later** (später), **finally** (zum Schluss)\n"
           "- **in the morning / in the afternoon / in the evening**\n"
           "- **at** + Uhrzeit: at half past eight. **on** + Tag: on Monday.\n\n"
           "Wichtige Wendungen: **get up**, **have breakfast**, **go to school**, **have lunch**, **do my homework**, **go to bed**.\n\n"
           "**Wortstellung:** Steht die Zeitangabe am Satzanfang, bleibt die Reihenfolge normal: **In the afternoon I play football.** (Nicht: In the afternoon play I football wie im Deutschen.)\n\n"
           "**Achtung bei he, she, it:** Das Verb bekommt ein **-s**: She **gets** up. He **goes** to school. She **has** lunch.",
           merke="first, then, after that, finally. Zeitangabe + Subjekt + Verb. he/she/it: Verb mit -s (gets, goes, has)."),
        lb(L4,
           "In der Arbeit sollst du deine Schule mit der englischen Schule aus dem Buch (Plymstock) vergleichen. Die Fakten über die englische Schule findest du im Buch. Hier übst du mit zwei erfundenen Schulen. Benutze die Vergleiche aus der Grammatik:\n\n"
           "- **bigger than / smaller than:** My school is **smaller than** Greenfield School.\n"
           "- **not as … as:** My school is **not as big as** Greenfield School.\n"
           "- **earlier than / later than:** Our school starts **earlier than** their school.\n"
           "- **the biggest of / in:** It is **the biggest** school **in** the town.\n"
           "- **but:** In England students wear a uniform, **but** in Germany we don't.\n\n"
           "Kurze Adjektive bekommen **-er** (bigger, older, earlier), lange bekommen **more** (more interesting). Nach dem Komparativ steht **than**.\n\n"
           "**Tipp:** Vergleiche immer **gleiche Dinge**: Zahl der Schüler mit Zahl der Schüler, Schulbeginn mit Schulbeginn.",
           merke="smaller than, not as big as, earlier than. Nach dem Komparativ steht than."),
        lb(L5,
           "Mit **Bindewörtern** verbindest du zwei Sätze:\n\n"
           "- **and** = und: I like music **and** art.\n"
           "- **but** = aber: I like PE, **but** I don't like maths.\n"
           "- **because** = weil: I like art **because** it is fun.\n"
           "- **so** = deshalb: It is raining, **so** we play inside.\n"
           "- **or** = oder: Do you walk **or** do you take the bus?\n\n"
           "**Achtung:** **because** steht vor dem Grund. **so** steht vor der Folge. Vor **but** und **so** steht meistens ein Komma.\n\n"
           "Die Wortstellung nach because bleibt wie im normalen Satz (Subjekt, Verb): I like English because **the teacher is** nice. (Nicht wie im Deutschen: weil der Lehrer nett **ist**.)",
           merke="and = und, but = aber, because = weil, so = deshalb. Nach because bleibt die Wortstellung normal."),
        lb(L6,
           "**Pläne** schreibst du mit **going to** + Grundform:\n\n"
           "- Tomorrow I **am going to** visit my grandma.\n"
           "- This weekend we **are going to** have a picnic.\n"
           "- She **is going to** play football after school.\n\n"
           "**E-Mail an einen Freund** (Aufbau):\n\n"
           "- **Anfang:** Hi Sam, / Dear Sam,\n"
           "- **Einstieg:** Thank you for your email. / How are you?\n"
           "- **Hauptteil:** Das, was du erzählen willst (zum Beispiel über deine Schule).\n"
           "- **Frage:** What about your school? / What is your school like?\n"
           "- **Schluss:** Please write back soon. / Write soon!\n"
           "- **Gruß:** Bye, / Best wishes, und dein Name.",
           merke="going to + Grundform. E-Mail: Anfang, Einstieg, Hauptteil, Frage, Schluss, Gruß."),
    ]


# ------------------------------------------------------------------ erfundene Daten für den Schulvergleich

GREEN = {"students": 900, "lessons": 5, "start": (8, 45), "uniform": True}
LINDEN = {"students": 450, "lessons": 6, "start": (7, 55), "uniform": False}
assert GREEN["students"] > LINDEN["students"]          # Greenfield ist größer
assert GREEN["start"] > LINDEN["start"]                 # Lindenschule beginnt früher
assert GREEN["lessons"] < LINDEN["lessons"]             # Lindenschule hat mehr Stunden
assert GREEN["uniform"] and not LINDEN["uniform"]


def tab_schulen():
    return svg_tabelle(["Facts", "Greenfield School", "Lindenschule"],
                       [["Students", "900", "450"], ["Lessons a day", "5", "6"], ["School starts", "8:45", "7:55"], ["Uniform", "yes", "no"]],
                       spalten_breit=[150, 180, 150])


ALT_SCHULEN = ("Tabelle: Greenfield School hat 900 Schüler, 5 Stunden am Tag, Schulbeginn 8:45 und Uniform. "
               "Lindenschule hat 450 Schüler, 6 Stunden am Tag, Schulbeginn 7:55 und keine Uniform.")


def mit_bild(t, bild, alt):
    t["bild"] = bild
    t["bildAlt"] = alt
    return t


def varianten(anfaenge, kerne):
    """Alle Kombinationen aus Satzanfang und Rest, mit und ohne Komma nach der Zeitangabe (nicht doppelt)."""
    out = []
    for a in anfaenge:
        for k in kerne:
            out.append(f"{a} {k}".strip())
            if a:
                out.append(f"{a}, {k}")
    seen = []
    for o in out:
        if o.lower() not in [s.lower() for s in seen]:
            seen.append(o)
    return seen


def aufgaben():
    a = []
    # ---------------------------------------------------------------- A: Meine Schule vorstellen
    a.append(mc("Welcher Satz ist richtig?", "My school is in a small town.",
                ["My school are in a small town.", "My school is on a small town.", "My school in a small town is."], B_A,
                info="Das Subjekt my school ist Einzahl, also is. Die Wortstellung ist Subjekt – Verb – Rest: My school is in a small town."))
    a.append(luecke("Ergänze die Wörter.",
                    "I go to school {{by}} bus. We have six lessons {{every|each}} day. My favourite subject {{is}} art.",
                    B_A, extra=["in", "at", "are"],
                    info="by bus = mit dem Bus, every day = jeden Tag, My favourite subject is art. (Einzahl, deshalb is)."))
    a.append(zuordnen("Ordne die deutschen Sätze den englischen zu.",
                      [("Wir tragen eine Uniform.", "We wear a uniform."), ("Wir haben keine Uniform.", "We don't wear a uniform."),
                       ("Die Schule beginnt um acht Uhr.", "School starts at eight o'clock."), ("Mein Lieblingsfach ist Kunst.", "My favourite subject is art.")],
                      B_A, info="wear = tragen, don't wear = tragen nicht, starts at eight o'clock = beginnt um acht Uhr, favourite subject = Lieblingsfach."))
    a.append(luecke("Ergänze die Wörter.",
                    "There {{are}} twenty-five students in my class. My teacher {{is}} Mrs Berg. We {{have}} a big playground.",
                    B_A, extra=["has", "am"],
                    info="There are + Mehrzahl (twenty-five students). My teacher is (Einzahl). We have = wir haben."))
    a.append(kurz("Schreibe die Zahl 600 als englisches Wort.", ["six hundred"], B_A,
                  info="600 = six hundred. Nach einer Zahl bekommt hundred kein -s."))
    a.append(kurz("Ergänze das Wort: We have a ___ at half past ten and play outside.", ["break"], B_A,
                  info="break = Pause. Half past ten ist 10:30."))
    a.append(tf("„We don't wear a uniform“ bedeutet: Wir tragen keine Uniform.", True, B_A,
                info="wear = tragen, uniform = Uniform. don't + wear = tragen nicht."))
    a.append(mc("Welche Frage passt zu der Antwort „My favourite subject is art.“?", "What is your favourite subject?",
                ["Where is your school?", "How old are you?", "When does school start?"], B_A,
                info="Die Antwort nennt das Lieblingsfach. Die Frage dazu: What is your favourite subject?"))
    a.append(mc("Welcher Satz ist richtig?", "There are 450 students at my school.",
                ["There is 450 students at my school.", "There are 450 student at my school.", "It have 450 students at my school."], B_A,
                info="There are + Mehrzahl. Nach 450 steht die Mehrzahl: students."))
    a.append(frei("Schreibe 3 Sätze über deine Schule: Wie heißt sie, wie viele Schüler gibt es, was ist dein Lieblingsfach?",
                  "My school is called Linden School. There are 450 students at my school. My favourite subject is art.",
                  ["Es gibt einen Satz zum Namen oder Ort der Schule (My school is called …).", "Es gibt einen Satz mit There are + Zahl.",
                   "Es gibt einen Satz zum Lieblingsfach (My favourite subject is …)."],
                  3, B_A))

    # ---------------------------------------------------------------- B: Mein Schultag
    a.append(reihenfolge("Bringe die Sätze in die richtige Reihenfolge.",
                         ["I get up at seven o'clock.", "Then I have breakfast.", "After that I go to school by bus.", "At eight o'clock the first lesson starts."], B_B,
                         info="Die Wörter then und after that zeigen die Reihenfolge: aufstehen, frühstücken, zur Schule fahren, Unterricht."))
    a.append(luecke("Ergänze die Wörter.",
                    "{{First}}, I get up at seven o'clock. {{Then}} I have breakfast. {{After that}} I go to school by bus. {{Finally}}, I am at school at eight.",
                    B_B, extra=["because", "but"], tauschbar=[("Then", "After that")],
                    info="first = zuerst, then = dann, after that = danach, finally = zum Schluss."))
    a.append(mc("Welcher Satz ist richtig?", "I have lunch at half past twelve.",
                ["I have lunch on half past twelve.", "I have lunch in half past twelve.", "I have lunch to half past twelve."], B_B,
                info="Vor der Uhrzeit steht at: at half past twelve."))
    a.append(luecke("Ergänze on, at oder in.",
                    "We have PE {{on}} Tuesday. I go to bed {{at}} half past nine. I play football {{in}} the afternoon.",
                    B_B, extra=["to", "by"],
                    info="on + Wochentag, at + Uhrzeit, in the afternoon = am Nachmittag."))
    a.append(kurz("Ergänze das Wort: I get ___ at seven o'clock. (aufstehen)", ["up"], B_B,
                  info="get up = aufstehen."))
    a.append(zuordnen("Ordne die Wendungen den deutschen Wörtern zu.",
                      [("get up", "aufstehen"), ("have breakfast", "frühstücken"), ("do my homework", "meine Hausaufgaben machen"),
                       ("go to bed", "ins Bett gehen"), ("have lunch", "zu Mittag essen")], B_B,
                      info="get up = aufstehen, have breakfast = frühstücken, do my homework = Hausaufgaben machen, go to bed = ins Bett gehen, have lunch = zu Mittag essen."))
    a.append(mc("Welcher Satz hat die richtige Wortstellung?", "In the afternoon I play football.",
                ["In the afternoon play I football.", "In the afternoon I football play.", "I in the afternoon football play."], B_B,
                info="Im Englischen bleibt die Reihenfolge Subjekt – Verb – Rest, auch nach einer Zeitangabe: In the afternoon I play football."))
    a.append(luecke("Ergänze die Verben (he/she braucht -s).",
                    "My sister {{gets}} up at six. She {{goes}} to school by bike. She {{has}} lunch in the canteen.",
                    B_B, extra=["get", "go", "have"],
                    info="she + Verb mit -s: gets, goes, has (have wird zu has)."))
    a.append(kurz("Schreibe auf Englisch: Nach der Schule mache ich meine Hausaufgaben. (after school, do, my homework)",
                  varianten(["After school", ""], ["I do my homework"]) + ["I do my homework after school"], B_B,
                  info="After school I do my homework. Die Zeitangabe kann vorn oder hinten stehen: I do my homework after school."))

    # ---------------------------------------------------------------- C: Zwei Schulen vergleichen
    t = lambda x: mit_bild(x, tab_schulen(), ALT_SCHULEN)
    a.append(t(mc("Schau dir die Tabelle an. Welcher Satz stimmt?", "Greenfield School has more students than Lindenschule.",
                  ["Lindenschule has more students than Greenfield School.", "Lindenschule is bigger than Greenfield School.", "Both schools have 900 students."], B_C,
                  info="Greenfield School hat 900 Schüler, Lindenschule 450. Greenfield School hat also mehr Schüler und ist größer.")))
    a.append(t(luecke("Ergänze die Steigerung.",
                      "Greenfield School is {{bigger}} than Lindenschule. Lindenschule is {{smaller}} than Greenfield School.",
                      B_C, extra=["more big", "biger"],
                      info="big → bigger (g wird verdoppelt), small → smaller. Nach dem Komparativ steht than.")))
    a.append(t(tf("Lindenschule starts earlier than Greenfield School.", True, B_C,
                  info="Lindenschule beginnt um 7:55, Greenfield School um 8:45. 7:55 ist früher, also stimmt die Aussage.")))
    a.append(t(tf("Students at Lindenschule have five lessons a day.", False, B_C,
                  info="Lindenschule hat sechs Stunden am Tag. Fünf Stunden hat Greenfield School.")))
    a.append(kurz("Ergänze ein Wort: Lindenschule starts earlier ___ Greenfield School.", ["than"], B_C,
                  info="Nach dem Komparativ steht than (nicht as, nicht then)."))
    a.append(t(luecke("Ergänze die Wörter.",
                      "Lindenschule is not as {{big}} as Greenfield School. Greenfield School starts {{later}} than Lindenschule.",
                      B_C, wortbank=False,
                      info="not as + Grundform + as: not as big as. later = später (Komparativ von late).")))
    a.append(mc("Welches Wort fehlt? At Greenfield School students wear a uniform, ___ at Lindenschule they don't.", "but",
                ["because", "so", "or"], B_C,
                info="Hier stehen zwei Gegensätze (Uniform – keine Uniform). Dafür nimmt man but (= aber)."))
    a.append(t(mc_fest("Welche Schule hat eine Uniform?", ["Greenfield School", "Lindenschule", "both schools", "neither school"], "Greenfield School", B_C,
                       info="In der Tabelle steht bei Greenfield School „yes“ und bei Lindenschule „no“.")))
    a.append(kurz("Schreibe auf Englisch: Meine Schule ist kleiner als Greenfield School.",
                  ["My school is smaller than Greenfield School"], B_C,
                  info="small + er = smaller. Nach dem Komparativ steht than."))
    a.append(mc("Welcher Satz ist richtig?", "My school is bigger than Greenfield School.",
                ["My school is more big than Greenfield School.", "My school is biger than Greenfield School.", "My school is bigger as Greenfield School."], B_C,
                info="big → bigger (g verdoppelt, -er), danach than."))
    a.append(reihenfolge("Bringe die Wörter in die richtige Reihenfolge (Vergleich der Schulen).",
                         ["Greenfield School", "is", "bigger", "than", "Lindenschule"], B_C,
                         info="Subjekt – is – Komparativ – than – zweites Ding: Greenfield School is bigger than Lindenschule."))

    # ---------------------------------------------------------------- D: Pläne mit going to
    a.append(kurz("Schreibe auf Englisch mit going to: Morgen besuche ich meine Oma. (visit, grandma) Beginne mit „Tomorrow“.",
                  varianten(["Tomorrow"], ["I'm going to visit my grandma", "I am going to visit my grandma"]), B_D,
                  info="Tomorrow I'm going to visit my grandma. I'm ist die Kurzform von I am; beides ist richtig."))
    a.append(mc("Welcher Satz ist richtig?", "After school I'm going to play football.",
                ["After school I going to play football.", "After school I'm going to playing football.", "After school I'm go to play football."], B_D,
                info="Plan = am/is/are + going to + Grundform. Das Verb nach to bleibt in der Grundform (play)."))
    a.append(luecke("Ergänze am, is oder are.",
                    "This weekend my friends and I {{are}} going to have a picnic. My mum {{is}} going to bake a cake. I {{am}} going to bring some drinks.",
                    B_D, extra=["be", "was"],
                    info="we/they: are, he/she/it: is, I: am. Danach going to + Grundform."))
    a.append(tf("„I'm going to read a book“ sagt, was ich in der Zukunft vorhabe.", True, B_D,
                info="going to benutzt man für Pläne und Vorhaben (Zukunft)."))
    a.append(mc("Welcher Satz bedeutet „Wir werden am Samstag Fußball spielen“?", "We are going to play football on Saturday.",
                ["We are going to played football on Saturday.", "We going to play football on Saturday.", "We are go to play football on Saturday."], B_D,
                info="we are going to + Grundform (play). Nach to steht kein -ed und kein -s."))
    a.append(frei("Schreibe 3 Sätze mit going to: Was machst du morgen nach der Schule?",
                  "After school I'm going to do my homework. Then I'm going to play with my friends. In the evening we are going to watch a film.",
                  ["Alle drei Sätze benutzen am/is/are + going to + Grundform.", "Die Sätze beschreiben drei verschiedene Pläne.", "Satzanfang groß, Punkt am Ende, Rechtschreibung stimmt."],
                  3, B_D))

    # ---------------------------------------------------------------- E: Sätze verbinden und E-Mails
    a.append(mc("Welches Wort fehlt? I like art, ___ I don't like maths.", "but", ["because", "so", "or"], B_E,
                info="Die beiden Teile sind ein Gegensatz (mag Kunst – mag Mathe nicht). Dafür nimmt man but."))
    a.append(luecke("Ergänze die Bindewörter.",
                    "I like music {{and}} art. I like PE, {{but}} I don't like maths. I get up early {{because}} school starts at eight. It is raining, {{so}} we play inside.",
                    B_E, extra=["or"],
                    info="and = und, but = aber, because = weil (vor dem Grund), so = deshalb (vor der Folge)."))
    a.append(zuordnen("Ordne die Bindewörter zu.",
                      [("and", "und"), ("but", "aber"), ("because", "weil"), ("so", "deshalb"), ("or", "oder")], B_E,
                      info="and = und, but = aber, because = weil, so = deshalb, or = oder."))
    a.append(reihenfolge("Bringe die Teile der E-Mail in die richtige Reihenfolge.",
                         ["Hi Sam,", "Thank you for your email.", "I'm going to tell you about my school.", "Please write back soon.", "Bye, Mila"], B_E,
                         info="Eine E-Mail hat: Anrede, Einstieg, Hauptteil, Schluss, Gruß mit Namen."))
    a.append(kurz("Ergänze das Wort: I like English ___ my teacher is nice.", ["because"], B_E,
                  info="because = weil. Danach steht der Grund in normaler Wortstellung: my teacher is nice."))
    a.append(tf("Ein guter Text hat eine Einleitung, einen Hauptteil und einen Schluss.", True, B_E,
                info="Einleitung (Worum geht es?), Hauptteil (die Informationen), Schluss (kurzer Abschluss)."))
    a.append(mc("Welcher Satz ist ein guter Schluss für eine E-Mail an einen Freund?", "Please write back soon. Bye!",
                ["Hi Sam, how are you?", "Thank you for your email.", "My name is Mila."], B_E,
                info="Please write back soon. und Bye! stehen am Ende einer E-Mail. Hi Sam steht am Anfang."))

    # ---------------------------------------------------------------- F: Eigene Texte schreiben
    a.append(mc("Mila schreibt über ihre Schule. Welcher Satz hat einen Fehler?", "We has six lessons every day.",
                ["My school is bigger than my old school.", "I like art because it is fun.", "After school I'm going to play football."], B_F,
                info="Nach we steht have (We have six lessons). has gehört zu he, she, it."))
    a.append(frei("Schreibe einen kurzen Text über deine Schule (5 Sätze): Name, Ort, Zahl der Schüler, Lieblingsfach, Uniform.",
                  "My school is called Linden School. It is in a small town. There are 450 students at my school. My favourite subject is art because it is fun. We don't wear a uniform.",
                  ["Der Text hat mindestens 5 vollständige Sätze.", "Der Text nennt Name oder Ort der Schule.", "Der Text benutzt There are oder We have richtig.",
                   "Der Text benutzt because oder and oder but richtig."],
                  4, B_F))
    a.append(frei("Beschreibe deinen Schultag (5 Sätze). Benutze first, then, after that und Uhrzeiten.",
                  "First, I get up at half past six. Then I have breakfast. After that I go to school by bus. School starts at eight o'clock. After school I do my homework.",
                  ["Der Text hat mindestens 5 vollständige Sätze.", "Die Reihenfolge ist klar (first, then, after that oder in the morning).", "Die Uhrzeiten sind richtig auf Englisch geschrieben.",
                   "Bei he/she/it steht -s, bei I/we nicht."],
                  4, B_F))
    a.append(mit_bild(frei("Vergleiche deine Schule mit Greenfield School (Tabelle). Schreibe 5 Sätze: Schüler, Stunden, Schulbeginn, Uniform.",
                           "My school is smaller than Greenfield School. We have six lessons, but they have five. School starts earlier at my school than at Greenfield School. They wear a uniform, but we don't. Greenfield School is not as small as my school.",
                           ["Der Text hat mindestens 5 Sätze.", "Es kommt ein richtiger Komparativ mit than vor.", "Es kommt not as … as oder but für einen Gegensatz vor.",
                            "Die Angaben stimmen zur Tabelle (oder zu deiner Schule).", "Rechtschreibung und Satzanfänge stimmen."],
                           5, B_F,
                           info=None), tab_schulen(), ALT_SCHULEN))
    a.append(frei("Schreibe eine E-Mail an einen englischen Freund (Sam). Erzähle von deiner Schule und stelle eine Frage über seine Schule.",
                  "Hi Sam, thank you for your email. I'm going to tell you about my school. My school is called Linden School and there are 450 students. We have six lessons every day, but we don't wear a uniform. What is your school like? Please write back soon. Bye, Mila",
                  ["Die E-Mail hat eine Anrede (Hi Sam,) und einen Gruß mit Namen.", "Die E-Mail erzählt mindestens zwei Dinge über die Schule (zum Beispiel Schüler, Stunden, Uniform).",
                   "Es gibt eine Frage an Sam (What is your school like?).", "Die E-Mail hat einen Schluss (Please write back soon.).", "Rechtschreibung und Verbformen stimmen."],
                  5, B_F))
    a.append(frei("Schreibe 4 Sätze: Was machst du am nächsten Wochenende? Benutze going to und and, but oder because.",
                  "On Saturday I'm going to visit my cousin. We are going to play games because it is going to rain. On Sunday I'm going to do my homework, but I'm also going to watch a film.",
                  ["Alle Sätze mit Plänen benutzen am/is/are + going to + Grundform.", "Es kommt ein Bindewort (and, but, because oder so) richtig vor.",
                   "Es gibt mindestens 4 vollständige Sätze.", "Rechtschreibung und Satzzeichen stimmen."],
                  4, B_F))
    return a


def build():
    p = pack(ID, "Englisch Teil 2h: Schreiben (Schule, Schultag, Vergleich)",
             "Schreiben für die Englischarbeit: über deine Schule und deinen Schultag schreiben, deine Schule mit einer englischen Schule vergleichen, Pläne mit going to und eine E-Mail. Mit Lernblatt, Satzbausteinen und Übungsaufgaben.",
             lernblatt(), aufgaben(), min_aufgaben=36,
             hinweis="Alle Sätze, Namen und Zahlen sind selbst ausgedacht, nicht aus dem Schulbuch oder dem Workbook. Die Fakten über die Schule aus dem Buch (Plymstock) stehen nur im Buch: "
                     "Schau sie dir dort an und übe den Vergleich mit deiner eigenen Schule. Freie Texte (Aufgaben mit Muster) bewertest du selbst oder zusammen mit den Eltern anhand der Kriterien.")
    return [nachlesen(p, {B_A: L2, B_B: L3, B_C: L4, B_D: L6, B_E: [L5, L6], B_F: [L1, L2, L3, L4]})]


if __name__ == "__main__":
    for p in build():
        print(p["id"], len(p["aufgaben"]), "Aufgaben")
