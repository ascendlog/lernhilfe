"""Englisch Klasse 6, Paket 2d: going to-future 1 (Bildung, Kurzformen, Verneinung, Zeitangaben).

Alle Sätze, Texte und Namen sind erfunden (nichts aus Buch, Heft oder Arbeitsblatt). Regeln laut Faktenblatt Abschnitt „going to-future“.
"""
from eng_lib import *

ID = "englisch-2d-going-to-1"

B_A = "A – Formen von be: am, is, are"
B_B = "B – Aussagesätze mit going to"
B_C = "C – Kurzformen"
B_D = "D – Verneinung"
B_E = "E – Zeitangaben und Vorhersagen"
B_F = "F – Kleine Texte"

L1 = "Wann benutzt man going to?"
L2 = "So bildest du going to"
L3 = "Die Verneinung"
L4 = "Zeitangaben"
L5 = "Typische Fehler"


def lernblatt():
    return [
        lb(L1,
           "Mit **going to** sprichst du über die **Zukunft**. Du benutzt es vor allem für **Pläne und Vorhaben**: Du hast dich schon entschieden, etwas zu tun.\n\n"
           "- I'm going to sing a song at the audition. (Ich habe vor, ein Lied zu singen.)\n"
           "- We are going to visit my aunt on Saturday.\n\n"
           "Auch wenn man schon **sieht**, dass gleich etwas passiert, passt going to: Look at the black clouds! It's going to rain.\n\n"
           "Frage dich also: Ist es ein Plan oder ist schon etwas zu sehen? Dann nimm going to.",
           merke="going to = Plan, Vorhaben oder etwas, das man schon kommen sieht. Es steht immer zusammen mit am, is oder are."),
        lb(L2,
           "Das Muster: **Subjekt + am / is / are + going to + Grundform des Verbs**.\n\n"
           "- I **am** going to **play** football.\n"
           "- You, we, they **are** going to **play** football.\n"
           "- He, she, it **is** going to **play** football.\n\n"
           "Nach **to** steht immer die **Grundform** des Verbs: nicht plays, nicht playing. Bei Namen und Gruppen richtest du dich nach der Person: Mia **is** going to swim. Mia and Ben **are** going to swim.\n\n"
           "**Kurzformen:** I'm, you're, he's, she's, it's, we're, they're. Beispiel: She's going to swim.",
           merke="Subjekt + am / is / are + going to + Grundform. Das Wort be passt sich dem Subjekt an, das Verb danach bleibt unverändert."),
        lb(L3,
           "Die Verneinung steht in der Mitte: **am / is / are + not + going to**.\n\n"
           "- I **am not** going to dance. Kurzform: I'm not going to dance.\n"
           "- He **is not** going to dance. Kurzform: He **isn't** going to dance.\n"
           "- They **are not** going to dance. Kurzform: They **aren't** going to dance.\n\n"
           "Bei „I“ gibt es keine Kurzform „amn't“. Man sagt **I'm not**. Das Hilfsverb „do“ brauchst du hier nicht: nicht „I don't going to“.",
           merke="Verneinung: am / is / are + not + going to. Kurzformen: isn't, aren't, I'm not."),
        lb(L4,
           "going to passt gut zu Zeitangaben, die in die Zukunft zeigen: **tomorrow, tonight, this evening, next week, next year, at the weekend, after school, in the break, on Monday, in two days, this year**.\n\n"
           "Meist stehen sie am Satzende: We are going to watch a film tonight. Sie können aber auch am Anfang stehen: Tonight we are going to watch a film.\n\n"
           "Ohne Zeitangabe zeigt going to trotzdem in die Zukunft: Ich habe etwas vor.",
           merke="Zeitangaben wie tomorrow, tonight, next week zeigen in die Zukunft und gehören meist ans Satzende."),
        lb(L5,
           "Diese Fehler passieren oft. Prüfe deine Sätze danach:\n\n"
           "- **am / is / are vergessen:** He going to play. → He **is** going to play.\n"
           "- **going to vergessen:** They are play football. → They are **going to** play football.\n"
           "- **Falsche Verbform:** She is going to plays. → She is going to **play**.\n"
           "- **do statt be:** I don't going to sing. → I'm **not** going to sing.\n"
           "- **Zwei Zukunftswörter:** He is going to will win. → He is going to win.\n\n"
           "Lies jeden Satz am Ende noch einmal und suche: Ist ein **am / is / are** da? Steht **going to** dahinter? Folgt die **Grundform**?",
           merke="Dreifach-Check: be da? going to da? Grundform danach?"),
    ]


# Sätze: (Subjekt, Verb mit Rest, Zeitangabe)
S = [
    ("Mia", "play tennis", "after school"),
    ("Ben", "do his homework", "this evening"),
    ("I", "read a new book", "tonight"),
    ("we", "visit our grandparents", "at the weekend"),
    ("the twins", "bake a cake", "tomorrow"),
    ("my sister", "join the drama club", "next week"),
    ("you", "help me", "in the break"),
    ("they", "watch a film", "on Friday"),
    ("Nora", "sing a song", "at the audition"),
    ("Oskar", "build a robot", "this year"),
    ("our teacher", "read us a story", "after lunch"),
    ("the children", "paint a poster", "in two days"),
    ("I", "learn the recorder", "next year"),
    ("Emma and Paul", "ride their bikes", "on Saturday"),
    ("Finn", "cook dinner", "tonight"),
    ("we", "walk to school", "tomorrow morning"),
    ("my dad", "clean the car", "on Sunday"),
    ("Ruby", "write an email", "after dinner"),
    ("Kai and Zoe", "play chess", "in the break"),
    ("she", "meet her friends", "at the weekend"),
]


def satz(i, neg=False):
    s, r, z = S[i]
    return [v + " " + z for v in gt_varianten(s, r, neg)]


def satz_text(i, neg=False):
    x = satz(i, neg)[0]
    return x[0].upper() + x[1:] + "."


def kurz_satz(i, neg=False, abschnitt=B_B, extra_info=""):
    s, r, z = S[i]
    form = "verneint" if neg else "bejaht"
    sol = satz_text(i, neg)
    b = be_of(s)
    info = f"Richtig: {sol} Zuerst kommt das Subjekt „{s}“, dann „{b}{' not' if neg else ''}“, dann going to und die Grundform „{r}“." + extra_info
    return kurz(f"Schreibe den Satz mit going to ({form}). Die Zeitangabe steht am Ende: {s} – {r} – {z}", satz(i, neg), abschnitt,
                info=info, tipp="Subjekt + am / is / are" + (" + not" if neg else "") + " + going to + Grundform + Zeitangabe.")


def be_mc(subj, rest, abschnitt=B_A):
    b = be_of(subj)
    art = {"am": "Zu „I“ gehört am.", "is": "Zu he, she, it und zu einer einzelnen Person oder Sache gehört is.", "are": "Zu you, we, they und zu mehreren Personen gehört are."}[b]
    return mc_fest(f"Welches Wort fehlt? {subj[0].upper() + subj[1:]} … going to {rest}.", ["am", "is", "are"], b, abschnitt,
                   info=f"Richtig: {subj[0].upper() + subj[1:]} {b} going to {rest}. {art}")


def aufgaben():
    a = []
    # ---------------------------------------------------------------- A: Formen von be
    a.append(luecke("Setze am, is oder are ein.",
                    "I {{am}} going to visit my cousin.\nMia {{is}} going to bake a cake.\nWe {{are}} going to play football.\nThe twins {{are}} going to swim.\nMy dad {{is}} going to cook.",
                    B_A, auswahl=["am", "is", "are"],
                    info="I → am. He, she, it und einzelne Personen (Mia, my dad) → is. We, you, they und mehrere Personen (the twins) → are."))
    a.append(be_mc("my friends", "watch a film"))
    a.append(be_mc("he", "learn the guitar"))
    a.append(be_mc("I", "join the chess club"))
    a.append(be_mc("the teacher", "read a story"))
    a.append(kurz("Welche Form von be fehlt? You … going to sing at the party. Schreibe nur das fehlende Wort.", ["are"], B_A,
                  info="Zu „you“ gehört immer are, auch bei einer einzelnen Person: You are going to sing."))
    a.append(tf("„We is going to visit Grandma.“ Dieser Satz ist richtig.", False, B_A,
                info="Zu „we“ gehört are: We are going to visit Grandma."))
    a.append(tf("„Ella and Tim are going to paint a picture.“ Dieser Satz ist richtig.", True, B_A,
                info="Ella and Tim sind zwei Personen, also they. Dazu passt are."))
    a.append(luecke("Setze die richtige Form von be ein (ohne Kurzform).",
                    "{{Are}} you going to join the choir?\nMy cat {{is}} going to sleep all day.\nI {{am}} going to help you.",
                    B_A, extra=["be", "being"],
                    info="Zu „you“ gehört are, zu „my cat“ (it) gehört is, zu „I“ gehört am. Am Satzanfang schreibt man Are groß, das spielt beim Prüfen keine Rolle."))

    # ---------------------------------------------------------------- B: Aussagesätze
    for i in (0, 1, 3, 4, 8):
        a.append(kurz_satz(i))
    a.append(reihenfolge("Bringe die Satzteile in die richtige Reihenfolge (Satz 1).", ["Mia", "is going to", "play tennis", "after school"], B_B,
                         info="Subjekt, dann is going to, dann das Verb mit Rest, am Ende die Zeitangabe: Mia is going to play tennis after school."))
    a.append(reihenfolge("Bringe die Satzteile in die richtige Reihenfolge (Satz 2).", ["The twins", "are going to", "bake a cake", "tomorrow"], B_B,
                         info="Zu „the twins“ passt are: The twins are going to bake a cake tomorrow."))
    a.append(reihenfolge("Bringe die Satzteile in die richtige Reihenfolge (Satz 3).", ["We", "are going to", "visit our grandparents", "at the weekend"], B_B,
                         info="Das Muster bleibt gleich: Subjekt, be + going to, Grundform + Rest, Zeitangabe."))
    a.append(luecke("Setze die Verben in der richtigen Form ein. Nach going to steht die Grundform.",
                    "Nora is going to {{sing}} a song.\nWe are going to {{walk}} to school.\nHe is going to {{read}} a new book.\nThey are going to {{paint}} a poster.",
                    B_B, extra=["sings", "walking", "walks"],
                    info="Nach „to“ steht immer die Grundform: sing, walk, read, paint. Nie mit -s und nie mit -ing."))
    a.append(mc("Welcher Satz ist richtig?", "My sister is going to join the drama club.",
                ["My sister going to join the drama club.", "My sister is going to joins the drama club.", "My sister are going to join the drama club."], B_B,
                info="Es braucht is (Subjekt: my sister) und die Grundform join. Die anderen Sätze haben kein is, ein falsches -s oder ein falsches are."))
    a.append(mc("Welcher Satz ist richtig?", "I am going to learn the recorder.",
                ["I going to learn the recorder.", "I am go to learn the recorder.", "I am going learn the recorder."], B_B,
                info="Das Muster heißt am / is / are + going to + Grundform. Bei „am go to“ fehlt das -ing, bei „going learn“ fehlt das to."))

    # ---------------------------------------------------------------- C: Kurzformen
    a.append(zuordnen("Ordne die Kurzform der langen Form zu.",
                      [("I am", "I'm"), ("she is", "she's"), ("we are", "we're"), ("they are", "they're"), ("you are", "you're")], B_C,
                      info="Der Apostroph ersetzt den ersten Buchstaben von am, is oder are: I am → I'm, she is → she's, we are → we're."))
    a.append(luecke("Schreibe die Kurzform (mit Apostroph) in die Lücke.",
                    "{{I'm}} going to sing. (I am)\n{{She's}} going to dance. (she is)\n{{We're}} going to play. (we are)\n{{They're}} going to run. (they are)",
                    B_C, wortbank=False,
                    info="Die Kurzform steht für Subjekt + be: I am → I'm, she is → she's, we are → we're, they are → they're."))
    a.append(kurz("Schreibe den Satz mit Kurzform: He is going to buy a ticket.", ["He's going to buy a ticket"], B_C,
                  info="He is → He's. Der Rest des Satzes bleibt gleich: He's going to buy a ticket."))
    a.append(kurz("Schreibe den Satz mit Kurzform: You are going to love this song.", ["You're going to love this song"], B_C,
                  info="You are → You're. Achtung: you're (= you are) und your (= dein) sind verschiedene Wörter."))
    a.append(mc("Welche Kurzform stimmt? … going to help you. (Mia is)", "Mia's", ["Mia're", "Mia'm"], B_C,
                info="Bei is wird nur das i weggelassen: Mia is → Mia's. Dazu passt is, nicht are oder am."))
    a.append(tf("„I'm going to watch TV.“ und „I am going to watch TV.“ bedeuten dasselbe.", True, B_C,
                info="I'm ist die Kurzform von I am. Beide Sätze sagen dasselbe, die Kurzform klingt beim Sprechen natürlicher."))

    # ---------------------------------------------------------------- D: Verneinung
    for i in (2, 5, 7, 9, 12):
        a.append(kurz_satz(i, neg=True, abschnitt=B_D))
    a.append(luecke("Verneine den Satz. Schreibe die Verneinung mit Kurzform (isn't, aren't) oder ausgeschrieben (is not, are not).",
                    "She is going to swim. → She {{isn't|is not}} going to swim.\nThey are going to sing. → They {{aren't|are not}} going to sing.\nWe are going to play. → We {{aren't|are not}} going to play.",
                    B_D, wortbank=False,
                    info="Das not steht hinter is oder are. Kurzformen: isn't (is not) und aren't (are not)."))
    a.append(luecke("Setze die Verneinung ein. Schreibe sie ausgeschrieben (is not, are not, am not).",
                    "Oskar {{is not}} going to cook dinner.\nWe {{are not}} going to be late.\nI {{am not}} going to play football today.",
                    B_D, wortbank=False,
                    info="Verneinung = am / is / are + not. Bei Oskar: is not. Bei we: are not. Bei I: am not (Kurzform I'm not)."))
    a.append(mc("Welcher Satz ist richtig verneint?", "Ruby isn't going to write an email.",
                ["Ruby doesn't going to write an email.", "Ruby isn't going to writes an email.", "Ruby not going to write an email."], B_D,
                info="Verneint wird mit is + not, nicht mit „do“. Danach folgt die Grundform write."))
    a.append(mc("Welche Antwort verneint den Satz „They are going to play chess.“ richtig?", "They aren't going to play chess.",
                ["They don't going to play chess.", "They aren't going to playing chess.", "They isn't going to play chess."], B_D,
                info="Zu they gehört are, die Verneinung ist aren't. Danach folgt die Grundform play."))
    a.append(tf("„I amn't going to sing.“ ist richtig.", False, B_D,
                info="„amn't“ gibt es nicht. Man sagt I'm not going to sing oder I am not going to sing."))
    a.append(tf("„He's not going to come.“ und „He isn't going to come.“ bedeuten dasselbe.", True, B_D,
                info="Es gibt zwei Kurzformen: he's not (he is not) und he isn't. Beide sind richtig."))

    # ---------------------------------------------------------------- E: Zeitangaben und Vorhersagen
    a.append(zuordnen("Ordne die deutsche Zeitangabe der englischen zu.",
                      [("morgen", "tomorrow"), ("heute Abend", "tonight"), ("nächste Woche", "next week"), ("am Wochenende", "at the weekend"), ("nach der Schule", "after school")], B_E,
                      info="tomorrow = morgen, tonight = heute Abend, next week = nächste Woche, at the weekend = am Wochenende, after school = nach der Schule."))
    a.append(mc("Welche Zeitangabe passt zu going to? We are going to visit Grandma …", "next week", ["last week", "yesterday", "two days ago"], B_E,
                info="going to zeigt in die Zukunft, also passt next week. Last week, yesterday und two days ago zeigen in die Vergangenheit."))
    a.append(mc("Look at the black clouds! It … rain.", "is going to", ["are going to", "am going to", "going to"], B_E,
                info="Man sieht schon Zeichen (dunkle Wolken), also passt going to. Zu „it“ gehört is: It is going to rain."))
    a.append(luecke("Ergänze die Zeitangaben.",
                    "Today is Monday. On Friday I am going to visit my friend. That is in {{four}} days.\nThe next school year starts in September. I am going to learn Spanish {{next}} year.",
                    B_E, extra=["last", "five"],
                    info="in four days = in vier Tagen (von Montag bis Freitag sind es vier Tage). next year = nächstes Jahr."))
    a.append(tf("In dem Satz „Last week we are going to play football.“ passt die Zeitangabe.", False, B_E,
                info="Last week ist vergangen. Für going to brauchst du eine Zeit in der Zukunft: Next week we are going to play football."))
    a.append(mc("Welcher Satz sagt einen Plan?", "I'm going to learn the guitar this year.",
                ["I learned the guitar last year.", "I was on stage yesterday.", "I played the recorder two years ago."], B_E,
                info="Nur der erste Satz sagt, was ich vorhabe (going to). Die anderen sprechen über die Vergangenheit."))

    # ---------------------------------------------------------------- F: Texte
    a.append(luecke("Ergänze den Text mit am, is, are und going to.",
                    "Next week is the school show. Mia {{is}} going to sing a song. Her brother Ben {{is}} going to play the guitar. "
                    "I {{am}} going to help with the lights. Our teachers {{are}} going to sit in the first row.",
                    B_F, auswahl=["am", "is", "are"],
                    info="Mia und Ben (je eine Person) → is. I → am. Our teachers (mehrere Personen) → are."))
    a.append(luecke("Ergänze den Text. Schreibe die Verbformen ohne Kurzform.",
                    "At the weekend we {{are}} going to visit my aunt. My mum {{is}} going to bake an apple pie. "
                    "My dad and I are going to {{play}} football in the garden.",
                    B_F, extra=["am", "plays"],
                    info="we → are, my mum → is. Nach going to steht die Grundform play (nicht plays)."))
    a.append(kurz("Wie heißt der verneinte Satz? Finn is going to cook tonight. → Finn … tonight. Schreibe den ganzen Satz verneint (Kurzform).",
                  ["Finn isn't going to cook tonight", "Finn is not going to cook tonight", "Finn's not going to cook tonight"], B_F,
                  info="Verneinung mit is + not (Kurzform isn't). Alles andere bleibt gleich."))
    a.append(tf("In „Tim and Anna aren't going to walk to school.“ ist die Verneinung richtig.", True, B_F,
                info="Tim and Anna sind zwei Personen (they), also are + not = aren't. Danach die Grundform walk."))
    return a


def build():
    p = pack(ID, "Englisch Teil 2d: going to-future (1)",
             "Plänen und Vorhaben: going to bilden (am / is / are + going to + Grundform), Kurzformen, Verneinung, Zeitangaben und typische Fehler. Mit Lernblatt und Übungsaufgaben.",
             lernblatt(), aufgaben(), min_aufgaben=34,
             hinweis="Alle Sätze, Texte und Namen sind selbst ausgedacht, nicht aus dem Schulbuch, dem Workbook oder den Arbeitsblättern. "
                     "In den Lücken zählt jeder Buchstabe. Wo ein Apostroph verlangt ist (I'm, isn't), steht es in der Aufgabe.")
    return [nachlesen(p, {B_A: L2, B_B: [L1, L2], B_C: L2, B_D: L3, B_E: L4, B_F: [L2, L5]})]


if __name__ == "__main__":
    for p in build():
        print(p["id"], len(p["aufgaben"]), "Aufgaben")
