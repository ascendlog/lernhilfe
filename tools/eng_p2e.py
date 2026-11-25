"""Englisch Klasse 6, Paket 2e: going to-future 2 (Fragen, Kurzantworten, Fragewörter, Mischformen, Fehler, Gespräche).

Alle Sätze, Texte und Namen sind erfunden (nichts aus Buch, Heft oder Arbeitsblatt).
"""
from eng_lib import *

ID = "englisch-2e-going-to-2"

B_A = "A – Fragen bilden"
B_B = "B – Kurzantworten"
B_C = "C – Fragewörter"
B_D = "D – Aussage, Verneinung oder Frage?"
B_E = "E – Fehler finden"
B_F = "F – Gespräche und Texte"

L1 = "Fragen mit going to"
L2 = "Kurzantworten"
L3 = "Fragewörter"
L4 = "Alle Formen im Überblick"
L5 = "Typische Fehler bei Fragen"


def lernblatt():
    return [
        lb(L1,
           "Bei einer **Ja-Nein-Frage** tauschen **am / is / are** und das Subjekt die Plätze. Das Wort „going to“ bleibt dahinter stehen.\n\n"
           "- Aussage: Mia **is** going to play tennis.\n"
           "- Frage: **Is** Mia going to play tennis?\n"
           "- Aussage: You **are** going to join the club.\n"
           "- Frage: **Are** you going to join the club?\n\n"
           "Du brauchst **kein do oder does**: nicht „Does Mia going to play?“. Nach dem Subjekt kommt wie immer going to und dann die **Grundform** des Verbs.",
           merke="Frage: am / is / are + Subjekt + going to + Grundform ...? Kein do, kein does."),
        lb(L2,
           "Die **Kurzantwort** besteht nur aus Yes oder No, dem Pronomen und dem Wort **be**. Das „going to“ lässt man weg.\n\n"
           "- Are you going to sing? – **Yes, I am.** / **No, I'm not.**\n"
           "- Is she going to sing? – **Yes, she is.** / **No, she isn't.**\n"
           "- Are they going to sing? – **Yes, they are.** / **No, they aren't.**\n\n"
           "Bei **Yes** schreibt man die Form ohne Kurzform: Yes, I **am** (nicht „Yes, I'm“). Bei **No** gibt es Kurzformen: No, I'm not. No, he isn't. No, we aren't.\n\n"
           "Für Namen nimmst du das passende Pronomen: Is Ben going to come? – Yes, **he** is. Are Mia and Ella going to sing? – No, **they** aren't.",
           merke="Kurzantwort: Yes, Pronomen + am / is / are. No, Pronomen + am not / isn't / aren't. Kein going to."),
        lb(L3,
           "Mit einem **Fragewort** fragst du nach etwas Bestimmtem. Es steht ganz vorn, danach geht es weiter wie bei der Ja-Nein-Frage.\n\n"
           "- **What** are you going to do? (Was?)\n"
           "- **Where** is Ben going to eat? (Wo? Wohin?)\n"
           "- **When** are they going to start? (Wann?)\n"
           "- **Who** are you going to invite? (Wen? Wer?)\n"
           "- **Why** is she going to stay at home? (Warum?)\n"
           "- **How** are we going to get there? (Wie?)\n\n"
           "Fragst du nach dem **Subjekt** (wer?), steht kein Tausch: **Who** is going to sing? (Wer wird singen?) Dann antwortest du: Mia is. / I am.",
           merke="Fragewort + am / is / are + Subjekt + going to + Grundform? Bei „Who is going to ...?“ (Subjektfrage) bleibt die Wortstellung wie in der Aussage."),
        lb(L4,
           "So sehen alle drei Formen im Überblick aus:\n\n"
           "- **Aussage:** He is going to dance.\n"
           "- **Verneinung:** He isn't going to dance.\n"
           "- **Frage:** Is he going to dance?\n"
           "- **Kurzantwort:** Yes, he is. / No, he isn't.\n\n"
           "Das Muster ist immer gleich: **be** (am, is, are) kommt zuerst oder in die Mitte, dann **going to**, dann die **Grundform**. Wenn du nicht sicher bist, schreibe zuerst die Aussage und forme sie dann um.",
           merke="Erst die Aussage schreiben, dann umformen: Verneinung = not hinter be, Frage = be nach vorn."),
        lb(L5,
           "Achte bei Fragen auf diese Fehler:\n\n"
           "- **do statt be:** Do you going to swim? → **Are** you going to swim?\n"
           "- **Kein Tausch:** You are going to swim? (nur als Satz mit Fragezeichen, aber keine richtige Frage) → Are you going to swim?\n"
           "- **going to in der Kurzantwort:** Yes, I am going to. → Yes, I **am**.\n"
           "- **Kurzform bei Yes:** Yes, I'm. → Yes, I **am**.\n"
           "- **Falsche Grundform:** Is he going to goes? → Is he going to **go**?",
           merke="Frage mit be beginnen, Kurzantwort ohne going to, bei Yes keine Kurzform."),
    ]


def ant(ja, pron):
    """Alle gleichwertigen Kurzantworten als Liste (mit und ohne Komma, mit Kurzform bei No)."""
    p = pron
    b = BE[p] if p in BE else be_of(p)
    if ja:
        koerper = [f"{p} {b}"]
    else:
        koerper = [f"{p} {b} not"]
        if p == "I":
            koerper.append("I'm not")
        else:
            koerper.append(f"{p} {'isn' if b == 'is' else 'aren'}'t")
            koerper.append(f"{BE_KURZ[p]} not")
    out = []
    for k in koerper:
        for pre in (("Yes, ", "Yes ") if ja else ("No, ", "No ")):
            out.append(pre + k)
    return out


def aufgaben():
    a = []
    # ---------------------------------------------------------------- A: Fragen bilden
    a.append(kurz("Mache aus dem Satz eine Frage: Mia is going to play tennis.", ["Is Mia going to play tennis"], B_A,
                  info="is geht nach vorn: Is Mia going to play tennis? Das Wort going to bleibt hinter dem Subjekt."))
    a.append(kurz("Mache aus dem Satz eine Frage: You are going to join the drama club.", ["Are you going to join the drama club"], B_A,
                  info="are geht nach vorn: Are you going to join the drama club? Aus „You“ wird in der Mitte „you“."))
    a.append(kurz("Mache aus dem Satz eine Frage: The children are going to paint a poster.", ["Are the children going to paint a poster"], B_A,
                  info="are geht nach vorn: Are the children going to paint a poster?"))
    a.append(kurz("Mache aus dem Satz eine Frage: Your brother is going to buy a ticket.", ["Is your brother going to buy a ticket"], B_A,
                  info="is geht nach vorn: Is your brother going to buy a ticket? Der Rest bleibt gleich."))
    a.append(reihenfolge("Bringe die Satzteile in die richtige Reihenfolge, sodass eine Frage entsteht (Frage 1).", ["Are", "you", "going to", "sing", "a song"], B_A,
                         info="Frage: be + Subjekt + going to + Grundform + Rest: Are you going to sing a song?"))
    a.append(reihenfolge("Bringe die Satzteile in die richtige Reihenfolge, sodass eine Frage entsteht (Frage 2).", ["Is", "Oskar", "going to", "cook", "dinner"], B_A,
                         info="Is Oskar going to cook dinner? is steht zuerst, dann das Subjekt Oskar."))
    a.append(reihenfolge("Bringe die Satzteile in die richtige Reihenfolge, sodass eine Frage entsteht (Frage 3).", ["Are", "they", "going to", "watch", "a film", "tonight"], B_A,
                         info="Frage: Are they going to watch a film tonight? Die Zeitangabe steht am Ende."))
    a.append(mc("Welche Frage ist richtig?", "Is she going to learn the guitar?",
                ["Does she going to learn the guitar?", "She is going to learn the guitar?", "Is she going to learns the guitar?"], B_A,
                info="Fragen mit going to beginnen mit am, is oder are (kein do, kein does). Danach folgt die Grundform learn."))
    a.append(mc("Welche Frage ist richtig?", "Are we going to be late?",
                ["Is we going to be late?", "Do we going to be late?", "We are going to be late?"], B_A,
                info="Zu we gehört are. Es steht am Anfang der Frage: Are we going to be late?"))

    # ---------------------------------------------------------------- B: Kurzantworten
    a.append(luecke("Ergänze die Kurzantworten.",
                    "Is Ben going to swim? – Yes, he {{is}}.\nAre you going to sing? – Yes, I {{am}}.\nAre they going to dance? – Yes, they {{are}}.\nIs Nora going to cook? – Yes, she {{is}}.",
                    B_B, auswahl=["am", "is", "are"],
                    info="Die Kurzantwort besteht aus dem Pronomen und dem Wort be: he is, I am, they are, she is. Das „going to“ fällt weg."))
    a.append(kurz("Antworte kurz mit Yes: Are you going to help me?", ant(True, "I"), B_B,
                  info="Yes, I am. Bei Yes schreibt man am voll aus (nicht „Yes, I'm“)."))
    a.append(kurz("Antworte kurz mit No: Are you going to help me?", ant(False, "I"), B_B,
                  info="No, I'm not. oder No, I am not. Bei I gibt es keine Kurzform „amn't“."))
    a.append(kurz("Antworte kurz mit No: Is she going to come? Schreibe die Antwort mit Kurzform (isn't).", ant(False, "she"), B_B,
                  info="No, she isn't. (oder: No, she is not / No, she's not). Die Kurzform von is not ist isn't."))
    a.append(kurz("Antworte kurz mit Yes: Are Mia and Ella going to sing?", ant(True, "they"), B_B,
                  info="Mia and Ella sind they, also: Yes, they are."))
    a.append(mc("Welche Kurzantwort passt? Is Finn going to play chess? – No, …", "he isn't.", ["he doesn't.", "he isn't going to.", "he don't."], B_B,
                info="Für Finn nimmst du he. Die Verneinung von is ist isn't. do/does und going to gehören nicht in die Kurzantwort."))
    a.append(tf("„Yes, I'm.“ ist eine richtige Kurzantwort auf „Are you going to come?“.", False, B_B,
                info="Bei Yes darf das be nicht verkürzt werden: Yes, I am. Bei No sind Kurzformen erlaubt: No, I'm not."))
    a.append(tf("„No, they aren't.“ ist eine richtige Kurzantwort auf „Are they going to wait?“.", True, B_B,
                info="Die Kurzantwort besteht aus No, dem Pronomen und aren't (= are not). Going to fehlt hier richtig."))

    # ---------------------------------------------------------------- C: Fragewörter
    a.append(zuordnen("Ordne das Fragewort der Bedeutung zu.",
                      [("What", "was"), ("Where", "wo, wohin"), ("When", "wann"), ("Who", "wer, wen"), ("Why", "warum"), ("How", "wie")], B_C,
                      info="What = was, where = wo oder wohin, when = wann, who = wer oder wen, why = warum, how = wie."))
    a.append(luecke("Ergänze das passende Fragewort.",
                    "{{What}} are you going to do after school? – I'm going to play football.\n{{Where}} is Ben going to eat? – In the canteen.\n{{When}} are they going to start? – At nine o'clock.\n{{Why}} is she going to stay at home? – Because she is ill.",
                    B_C, extra=["Who", "How"],
                    info="What fragt nach einer Tätigkeit, where nach dem Ort, when nach der Zeit, why nach dem Grund (Antwort mit because)."))
    a.append(mc("… are you going to travel to London? – By train.", "How", ["Where", "Why", "When"], B_C,
                info="Die Antwort „By train“ sagt, wie man reist. Also fragt man mit how."))
    a.append(mc("… is going to sing at the show? – Nora is.", "Who", ["What", "Where", "When"], B_C,
                info="Gefragt ist eine Person (Nora). Das Fragewort ist who. Bei „Who is going to ...?“ steht kein Subjekt hinter is."))
    a.append(kurz("Schreibe die Frage mit Fragewort: Where / you / go on holiday? (going to, vollständiger Satz mit Fragezeichen)",
                  ["Where are you going to go on holiday"], B_C,
                  info="Where + are + you + going to + go on holiday? Auch das zweite „go“ ist richtig: going to go."))
    a.append(kurz("Schreibe die Frage mit Fragewort: What / Mia / wear to the party? (going to)",
                  ["What is Mia going to wear to the party"], B_C,
                  info="What + is + Mia + going to + wear to the party? Zu Mia gehört is."))
    a.append(kurz("Schreibe die Frage mit Fragewort: When / the twins / start the game? (going to)",
                  ["When are the twins going to start the game"], B_C,
                  info="When + are + the twins + going to + start the game? Zu the twins (they) gehört are."))
    a.append(mc("Welche Frage ist richtig?", "What are they going to do tomorrow?",
                ["What they are going to do tomorrow?", "What do they going to do tomorrow?", "What are going they to do tomorrow?"], B_C,
                info="Nach dem Fragewort kommt wie bei der Ja-Nein-Frage zuerst be (are), dann das Subjekt (they), dann going to."))

    # ---------------------------------------------------------------- D: Aussage, Verneinung oder Frage
    a.append(kurz("Verneine den Satz (Kurzform): Tom is going to wait.", ["Tom isn't going to wait", "Tom is not going to wait", "Tom's not going to wait"], B_D,
                  info="Verneinung: not hinter is. Tom isn't going to wait."))
    a.append(kurz("Mache aus der Aussage eine Verneinung: We are going to leave early.", ["We aren't going to leave early", "We are not going to leave early", "We're not going to leave early"], B_D,
                  info="Verneinung: not hinter are. We aren't going to leave early."))
    a.append(kurz("Mache aus der Verneinung eine Frage: He isn't going to come. → … ?", ["Is he going to come"], B_D,
                  info="Frage: be nach vorn, not fällt weg: Is he going to come?"))
    a.append(kurz("Mache aus der Frage eine Aussage: Are they going to win?", ["They are going to win", "They're going to win"], B_D,
                  info="Subjekt zuerst, dann be: They are going to win."))
    a.append(mc("Welche Aussage passt zur Antwort „No, she isn't.“?", "Is Kim going to come?",
                ["Kim is going to come.", "Kim isn't going to come.", "Does Kim come?"], B_D,
                info="Die Kurzantwort „No, she isn't.“ beantwortet eine Ja-Nein-Frage, also Is Kim going to come?"))
    a.append(zuordnen("Ordne jedem Satz die Satzart zu.",
                      [("Are you going to sing?", "Frage"), ("You aren't going to sing.", "Verneinung"), ("You are going to sing.", "Aussage"), ("No, I'm not.", "Kurzantwort")], B_D,
                      info="Die Frage beginnt mit be. Die Verneinung hat not (aren't) in der Mitte. Die Aussage hat das Subjekt vorn. Die Kurzantwort beginnt mit Yes oder No."))
    a.append(luecke("Wähle für jede Lücke: Aussage (affirmative), Verneinung (negative) oder Frage (question).",
                    "She is going to dance. → {{affirmative}}\nShe isn't going to dance. → {{negative}}\nIs she going to dance? → {{question}}",
                    B_D, auswahl=["affirmative", "negative", "question"],
                    info="Aussage = affirmative, Verneinung = negative, Frage = question."))
    a.append(mc("Wie lautet die richtige Verneinung? Nora is going to wear her new shoes.", "Nora isn't going to wear her new shoes.",
                ["Nora doesn't going to wear her new shoes.", "Nora isn't going to wears her new shoes.", "Nora not going to wear her new shoes."], B_D,
                info="Verneinung = is + not (isn't) und danach die Grundform wear."))
    a.append(kurz("Schreibe die Frage: they – going to – win – the game", ["Are they going to win the game"], B_D,
                  info="Frage: Are they going to win the game? Das Wort be (are) steht vorn."))

    # ---------------------------------------------------------------- E: Fehler finden
    a.append(kurz("Schreibe den Satz richtig auf: He going to buy a new bike.", ["He is going to buy a new bike", "He's going to buy a new bike"], B_E,
                  info="Es fehlt is: He is going to buy a new bike."))
    a.append(kurz("Schreibe den Satz richtig auf: They are play football tomorrow. (going to)", ["They are going to play football tomorrow", "They're going to play football tomorrow"], B_E,
                  info="Es fehlt going to: They are going to play football tomorrow."))
    a.append(kurz("Schreibe den Satz richtig auf: Ruby is going to plays the piano.", ["Ruby is going to play the piano", "Ruby's going to play the piano"], B_E,
                  info="Nach to steht die Grundform: play, nicht plays."))
    a.append(kurz("Schreibe die Frage richtig auf: Do you going to come?", ["Are you going to come"], B_E,
                  info="Fragen mit going to beginnen mit be: Are you going to come?"))
    a.append(mc("In welchem Satz steckt ein Fehler?", "Mia is going to goes home.",
                ["Mia is going to go home.", "Is Mia going to go home?", "Mia isn't going to go home."], B_E,
                info="Falsch ist „going to goes“: Nach to steht die Grundform go."))
    a.append(tf("„Are you going to coming to the party?“ ist richtig.", False, B_E,
                info="Nach going to steht die Grundform: Are you going to come to the party?"))

    # ---------------------------------------------------------------- F: Gespräche und Texte
    a.append(luecke("Ergänze das Gespräch (ohne Kurzformen).",
                    "Ella: What {{are}} you going to do after school, Tim?\nTim: I {{am}} going to play basketball. Are you going to come with me?\n"
                    "Ella: No, I {{am not}}. I am going to {{practise|practice}} for the school show.",
                    B_F, extra=["is", "practising"],
                    info="you → are, I → am. Die Kurzantwort verneint mit am not. Nach going to steht die Grundform practise (britisch, auch practice ist hier erlaubt)."))
    a.append(luecke("Ergänze die E-Mail. Schreibe die Verbformen ohne Kurzform.",
                    "Hi Oskar,\nOn Saturday we {{are}} going to have a picnic in the park. Mum {{is}} going to make sandwiches. "
                    "Are you going to {{bring}} your football? We are going to {{play}} a match!\nSee you, Finn",
                    B_F, extra=["am", "brings"],
                    info="we → are, Mum → is. Nach going to steht die Grundform bring und play (nicht brings oder playing)."))
    a.append(reihenfolge("Bringe das Gespräch in die richtige Reihenfolge.",
                         ["Are you going to sing at the audition?", "Yes, I am.", "What are you going to sing?", "I'm going to sing a pop song."], B_F,
                         info="Erst die Ja-Nein-Frage, dann die Kurzantwort, dann die Frage mit What und die passende Antwort."))
    a.append(mc("Welche Antwort passt? What are you going to do at the weekend?", "I'm going to visit my cousin.",
                ["Yes, I am.", "No, I'm not.", "I visit not."], B_F,
                info="Auf eine Frage mit What antwortet man mit einem ganzen Satz, nicht mit Yes oder No."))
    a.append(frei("Schreibe 3 Sätze mit going to über deine Pläne für das Wochenende (zum Beispiel: I'm going to ...).",
                  "I'm going to play football with my friends on Saturday. My mum is going to bake a cake. On Sunday we are going to visit my grandparents.",
                  ["Alle drei Sätze haben am / is / are + going to + Grundform.", "Die Sätze sind verständlich und sinnvoll.", "Rechtschreibung und Satzanfänge (Großbuchstaben) stimmen."],
                  3, B_F))
    return a


def build():
    p = pack(ID, "Englisch Teil 2e: going to-future (2)",
             "Fragen und Kurzantworten mit going to, Fragewörter, Aussage, Verneinung und Frage im Wechsel, typische Fehler, Gespräche und E-Mails. Mit Lernblatt und Übungsaufgaben.",
             lernblatt(), aufgaben(), min_aufgaben=34,
             hinweis="Alle Sätze, Texte und Namen sind selbst ausgedacht, nicht aus dem Schulbuch, dem Workbook oder den Arbeitsblättern. "
                     "Wenn mehrere Schreibweisen richtig sind (isn't / is not), werden alle gewertet.")
    return [nachlesen(p, {B_A: L1, B_B: L2, B_C: L3, B_D: [L4, L1, L2], B_E: [L5, L1, L2], B_F: [L1, L2, L3]})]


if __name__ == "__main__":
    for p in build():
        print(p["id"], len(p["aufgaben"]), "Aufgaben")
