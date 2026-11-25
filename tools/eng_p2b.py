"""Englisch Klasse 6, Paket 2b: Wortschatz 1 (Wortfamilien auf -er, Schule und Schultag, Bühne und Musical, kleine Wörter und Wendungen).

Wörter und Bedeutungen laut Vokabelliste Unit 2 (Buch S. 184–187) und Lernzettel. Alle Beispielsätze und Texte sind selbst geschrieben.
"""
from eng_vok import *

ID = "englisch-2b-wortschatz-1"

B_A = "A – Wortfamilien: Verb und Person (-er)"
B_B = "B – Schule und Schultag"
B_C = "C – Bühne, Musical und Gefühle"
B_D = "D – Kleine Wörter, Pläne und Ratschläge"
B_E = "E – Gemischt"

L1 = "Wortfamilien: Wer macht das?"
L2 = "Schule und Schultag"
L3 = "Bühne, Musical und Gefühle"
L4 = "Kleine Wörter, Pläne und Ratschläge"
L5 = "So lernst du Vokabeln"


def lernblatt():
    return [
        lb(L1,
           "Aus vielen Verben machst du mit **-er** eine **Person**, die das tut:\n\n"
           "- (to) call = anrufen → **caller** = Anrufer/in\n"
           "- (to) dance = tanzen → **dancer** = Tänzer/in\n"
           "- (to) fight = kämpfen → **fighter** = Kämpfer/in\n"
           "- (to) help = helfen → **helper** = Helfer/in\n"
           "- (to) listen = zuhören → **listener** = Zuhörer/in\n"
           "- (to) read = lesen → **reader** = Leser/in\n"
           "- (to) run = laufen → **runner** = Läufer/in\n"
           "- (to) shop = einkaufen → **shopper** = (Ein-)Käufer/in\n"
           "- (to) sing = singen → **singer** = Sänger/in\n"
           "- (to) speak = sprechen → **speaker** = Sprecher/in, Redner/in\n"
           "- (to) work = arbeiten → **worker** = Arbeiter/in\n\n"
           "**Achtung bei der Schreibweise:** run und shop haben einen kurzen Vokal: Der Konsonant wird verdoppelt (runner, shopper), genau wie bei bigger. Endet das Verb auf -e, fällt das -e weg: dance → dancer.",
           merke="Verb + -er = Person. Bei run und shop wird der Endkonsonant verdoppelt: runner, shopper."),
        lb(L2,
           "Diese Wörter brauchst du für den **Schultag**:\n\n"
           "- **uniform** = Schuluniform\n"
           "- **break** = Pause\n"
           "- **canteen** = Kantine (an der Schule in Plymstock heißt sie „the Galley“)\n"
           "- **lessons** = Unterrichtsstunden\n"
           "- **clubs** = AGs, Clubs\n"
           "- **registration** = Anwesenheitskontrolle am Morgen (der Lehrer ruft die Namen auf)\n"
           "- **(to) queue** = Schlange stehen, sich anstellen\n"
           "- **(to) ring** = klingeln, läuten (Simple Past: rang)\n"
           "- **(to) call out the names** = die Namen aufrufen\n"
           "- **article** = Artikel (in einer Zeitung); **worksheet** = Arbeitsblatt\n"
           "- **(to) label** = beschriften; **mistake** = Fehler; **correct** = richtig\n"
           "- **(to) read aloud** = laut vorlesen; **(to) make sure that …** = darauf achten, dass …\n"
           "- **(to) get ready (for)** = sich fertig machen (für); **dialogue** = Dialog\n\n"
           "Ein Beispiel mit mehreren Wörtern: At registration the teacher calls out the names, and then the first lesson starts.",
           merke="Schultag: uniform, break, canteen, lessons, clubs, registration, queue. Das Wort ring hat die Vergangenheit rang."),
        lb(L3,
           "Diese Wörter gehören zu **Bühne, Musical und Gefühlen**:\n\n"
           "- **audition** = Vorsprechen, Vorsingen, Vorspielen\n"
           "- **this year's musical** = das diesjährige Musical (last year's, next year's musical)\n"
           "- **stage** = Bühne; **concert** = Konzert; **theatre** = Theater\n"
           "- **recorder** = Blockflöte; **earphones** = Kopfhörer, Ohrhörer\n"
           "- **talented** = begabt, talentiert; **brilliant** = großartig, genial\n"
           "- **(to) cheer** = jubeln; **(to) clap** = (Beifall) klatschen\n"
           "- **nervous** = nervös, aufgeregt; **shy** = schüchtern, scheu\n"
           "- **fashion** = Mode; **syllable** = Silbe\n\n"
           "**Betonung:** Bei audition und recorder ist die **zweite** Silbe betont (audition, recorder). Bei concert, theatre, nervous, talented, article und dialogue ist die **erste** Silbe betont.",
           merke="Bühne: audition, stage, concert, theatre, recorder. Gefühle: nervous, shy. Betonung bei audition und recorder auf der zweiten Silbe."),
        lb(L4,
           "Kleine Wörter, die du oft brauchst:\n\n"
           "- **I'm going to sing a song.** = Ich habe vor, ein Lied zu singen. (Plan mit going to)\n"
           "- **You should …** = Du solltest … / Ihr solltet … (Ratschlag): You should read more.\n"
           "- **a bit** = ein bisschen, etwas (a bit dark) und **a few** = ein paar, einige (a few pounds)\n"
           "- **by …** = von … (Urheber): a song by a band\n"
           "- **side** = Seite (the other side); **about** = ungefähr; **even** = sogar; **so far** = bis jetzt; **everything** = alles\n"
           "- **present** = Gegenwart (the past – the present – the future)\n"
           "- **on my / your / his / … own** = allein (not „an own room“: Do you have your own room?)\n\n"
           "**Achtung:** a bit hat mit **Menge** zu tun (a bit of cake), a few mit **Anzahl** (a few cakes).",
           merke="a few = ein paar (zählbar). a bit = ein bisschen. should = solltest. own steht immer mit my, your, his … (my own room)."),
        lb(L5,
           "So bleiben Vokabeln im Kopf:\n\n"
           "- **Laut sprechen** und gleichzeitig aufschreiben. Wörter mit Betonung (nervous, theatre) merkst du dir besser, wenn du sie laut sagst.\n"
           "- **Gruppen bilden:** Schule, Bühne, Gefühle, kleine Wörter. Dann sind es kleinere Päckchen.\n"
           "- **Wortfamilien nutzen:** sing → singer, dance → dancer.\n"
           "- **Mit Beispielsätzen lernen** statt Einzelwörter: Schreibe zu jedem Wort einen eigenen Satz.\n"
           "- **Deutsch abdecken und Englisch aufschreiben**, danach umgekehrt.\n\n"
           "Wichtig: Beim Aufschreiben zählt jeder Buchstabe, zum Beispiel **theatre** (nicht theater), **dialogue** (nicht dialog) und **canteen**.",
           merke="Karteikarten, laut sprechen, Gruppen bilden, mit eigenen Sätzen üben. Auf die Schreibweise achten: theatre, dialogue."),
    ]


def aufgaben():
    a = []
    # ---------------------------------------------------------------- A: Wortfamilien
    a.append(zuordnen("Ordne dem Verb die passende Person zu.",
                      [(v, p) for v, p, _ in FAMILIEN[:5]], B_A,
                      info="Verb + -er ergibt die Person: call → caller, dance → dancer (das -e fällt weg), fight → fighter, help → helper, listen → listener."))
    a.append(zuordnen("Ordne dem Verb die passende Person zu.",
                      [(v, p) for v, p, _ in FAMILIEN[5:]], B_A,
                      info="read → reader, run → runner und shop → shopper (Endkonsonant doppelt), sing → singer, speak → speaker, work → worker."))
    a.append(kurz("Eine Person, die läuft, ist ein … Schreibe das englische Wort.", ["runner"], B_A,
                  info="run → runner: Der Endkonsonant wird verdoppelt, weil der Vokal kurz ist."))
    a.append(kurz("Eine Person, die einkauft, ist ein … Schreibe das englische Wort.", ["shopper"], B_A,
                  info="shop → shopper (Konsonant doppelt, wie bei runner)."))
    a.append(mc("Was bedeutet „speaker“?", "Sprecher/in, Redner/in", ["Zuhörer/in", "Sänger/in", "Leser/in"], B_A,
                info="speak = sprechen, also ist ein speaker jemand, der spricht oder eine Rede hält."))
    a.append(luecke("Setze die Personen ein.",
                    "A {{singer}} sings, a {{dancer}} dances, a {{reader}} reads and a {{helper}} helps.",
                    B_A, extra=["worker", "caller"],
                    info="Die Person hat dasselbe Wort wie das Verb plus -er: sing → singer, dance → dancer, read → reader, help → helper."))
    a.append(luecke("Setze die passende Person ein.",
                    "My uncle is a {{worker}} in a factory.\nThe {{caller}} on the phone asks for my mum.\nThe {{runner}} wins the race.\nThe {{speaker}} talks to the whole school.",
                    B_A, extra=["listener", "shopper"],
                    info="work → worker (arbeitet), call → caller (ruft an), run → runner (läuft), speak → speaker (spricht)."))
    a.append(tf("Eine Person, die tanzt, heißt auf Englisch „danceer“.", False, B_A,
                info="dance endet auf -e. Beim Anhängen von -er fällt das -e weg: dancer."))
    a.append(kurz("Wie heißt „Helfer/in“ auf Englisch?", ["helper"], B_A, info="help → helper (Verb + -er)."))
    a.append(mc("Welche Person gehört zu „listen“?", "listener", ["listenner", "lister", "listener to"], B_A,
                info="listen → listener. Das Wort hat nur ein n in der Mitte."))

    # ---------------------------------------------------------------- B: Schule und Schultag
    a.append(paare_zu(["uniform", "canteen", "break", "lessons", "clubs"], B_B))
    a.append(luecke("Ergänze den Text über eine Schule. (Der Text ist selbst ausgedacht.)",
                    "At my cousin's school the day starts with {{registration}}: the teacher checks who is there. "
                    "Then there are four {{lessons}} before the {{break}}. Everybody wears a school {{uniform}}. "
                    "Lunch is in the {{canteen}}, and after school you can join one of the {{clubs}}.",
                    B_B, extra=["queue", "article"],
                    info="registration = Anwesenheitskontrolle, lessons = Stunden, break = Pause, uniform = Schuluniform, canteen = Kantine, clubs = AGs."))
    a.append(en_kurz("worksheet", B_B))
    a.append(en_kurz("mistake", B_B))
    a.append(de_mc("queue", B_B))
    a.append(de_mc("ring", B_B))
    a.append(en_mc("label", B_B))
    a.append(luecke("Setze das passende Wort oder die passende Wendung ein.",
                    "We {{queue}} in front of the canteen.\nAt registration the teacher {{calls out the names}}.\nPlease {{read aloud}} the first paragraph.\nThe teacher gives us a {{worksheet}} about verbs.",
                    B_B, extra=["label", "mistake"],
                    info="queue = Schlange stehen, call out the names = die Namen aufrufen (ohne s, wenn es in der Wortbank steht), read aloud = laut vorlesen, worksheet = Arbeitsblatt."))
    a.append(tf("Ein „worksheet“ ist ein Blatt mit Aufgaben.", True, B_B,
                info="worksheet = Arbeitsblatt."))
    a.append(tf("„Registration“ bedeutet auf Deutsch „Pause“.", False, B_B,
                info="registration ist die Anwesenheitskontrolle am Morgen, wenn der Lehrer die Namen aufruft. Pause heißt break."))
    a.append(en_kurz("correct", B_B))
    a.append(de_mc("make sure", B_B))
    a.append(en_kurz("read aloud", B_B))
    a.append(kurz("Wie heißt die Vergangenheit (Simple Past) von „ring“?", ["rang"], B_B,
                  info="ring ist unregelmäßig: ring – rang. Die Schulglocke rang pünktlich."))
    a.append(mc("Wie nennt man an einer englischen Schule den Raum, in dem man isst?", "canteen", ["uniform", "registration", "worksheet"], B_B,
                info="Die Kantine heißt canteen. An der Schule in Plymstock hat sie den Namen „the Galley“."))

    # ---------------------------------------------------------------- C: Bühne
    a.append(paare_zu(["audition", "stage", "concert", "theatre", "recorder"], B_C))
    a.append(paare_zu(["talented", "cheer", "clap", "nervous", "earphones"], B_C))
    a.append(luecke("Ergänze die Geschichte. (Der Text ist selbst ausgedacht.)",
                    "Before the {{audition}} Nora felt {{nervous}}. She went on {{stage}} and sang her song. "
                    "Everybody began to {{clap}}. The teachers said that she was very {{talented}}.",
                    B_C, extra=["recorder", "theatre"],
                    info="audition = Vorsingen, nervous = nervös, stage = Bühne, clap = klatschen, talented = begabt."))
    a.append(en_kurz("concert", B_C))
    a.append(en_kurz("recorder", B_C))
    a.append(de_mc("talented", B_C))
    a.append(en_mc("theatre", B_C))
    a.append(en_kurz("fashion", B_C))
    a.append(de_mc("earphones", B_C))
    a.append(kurz("Die Fans … (jubeln), wenn die Band spielt. Schreibe das englische Verb ohne to.", ["cheer"], B_C,
                  info="(to) cheer = jubeln. Beispiel: The fans cheer when the band plays."))
    a.append(mc("Welches Wort hat die Betonung auf der zweiten Silbe?", "recorder", ["concert", "nervous", "dialogue"], B_C,
                info="recorder und audition betont man auf der zweiten Silbe. Bei concert, nervous und dialogue ist die erste Silbe betont."))
    a.append(tf("Eine „recorder“ ist ein Gerät, das Lieder aufnimmt.", False, B_C,
                info="Im Musikunterricht ist a recorder eine Blockflöte."))
    a.append(mc("Welches englische Wort steht für „schüchtern“?", "shy", ["nervous", "brilliant", "talented"], B_C,
                info="shy = schüchtern, scheu. nervous = nervös, brilliant = großartig, talented = begabt."))
    a.append(en_kurz("audition", B_C))

    # ---------------------------------------------------------------- D: kleine Wörter, Pläne
    a.append(luecke("Setze das passende kleine Wort ein.",
                    "You {{should}} drink more water.\nThe soup is a {{bit}} too hot.\nI have a {{few}} books about horses.\nThis song is {{by}} a famous band.",
                    B_D, extra=["many", "some"],
                    info="should = solltest, a bit = ein bisschen, a few = ein paar, by = von (Urheber)."))
    a.append(de_mc("a few", B_D))
    a.append(mc("Welche Wendung passt? I only have … coins in my pocket.", "a few", ["a bit", "even", "so far"], B_D,
                info="Coins kann man zählen: a few coins (ein paar Münzen). a bit passt zu Mengen wie a bit of cake."))
    a.append(tf("„You should read more.“ bedeutet „Du musst mehr lesen.“", False, B_D,
                info="should ist ein Ratschlag: Du solltest mehr lesen. Bei „musst“ sagt man must oder have to."))
    a.append(en_kurz("present", B_D))
    a.append(reihenfolge("Bringe die Zeiten in die richtige Reihenfolge (von früher nach später).", ["the past", "the present", "the future"], B_D,
                         info="Vergangenheit (the past), Gegenwart (the present), Zukunft (the future)."))
    a.append(en_kurz("about", B_D))
    a.append(en_kurz("even", B_D))
    a.append(en_kurz("everything", B_D))
    a.append(tf("„Do you have an own room?“ ist richtig.", False, B_D,
                info="own steht immer mit my, your, his, her … : Do you have your own room?"))
    a.append(kurz("Übersetze: Ich habe vor, ein Lied zu singen.", ["I'm going to sing a song", "I am going to sing a song"], B_D,
                  info="Pläne sagt man mit going to: I'm going to sing a song."))
    a.append(kurz("Übersetze: Du solltest mehr lesen.", ["You should read more"], B_D,
                  info="Ratschlag mit should: You should read more."))

    # ---------------------------------------------------------------- E: gemischt
    a.append(luecke("Setze die Wörter ein. (Gemischte Wörter, selbst ausgedachte Sätze.)",
                    "The {{stage}} is very big. I am {{nervous}}.\nPlease {{label}} the picture.\nI made a {{mistake}} in the test.\nThe bell {{rang}} at nine.",
                    B_E, extra=["queue", "audition", "rings"],
                    info="stage = Bühne, nervous = nervös, label = beschriften, mistake = Fehler, rang = Simple Past von ring."))
    a.append(mc("Welches Wort passt nicht in die Gruppe?", "concert", ["uniform", "break", "canteen"], B_E,
                info="uniform, break und canteen gehören zum Schultag. concert (Konzert) gehört zur Bühne."))
    a.append(mc("Welches Wort passt nicht in die Gruppe?", "queue", ["stage", "audition", "clap"], B_E,
                info="stage, audition und clap gehören zum Thema Bühne und Musical. Schlange stehen (queue) ist ein Schulwort."))
    a.append(paare_zu(["uniform", "nervous", "worksheet", "stage", "a bit"], B_E, frage="Ordne die gemischten Wörter der deutschen Bedeutung zu."))
    a.append(frei("Schreibe 3 Sätze über einen Schultag. Benutze mindestens 5 Wörter aus der Wortliste (zum Beispiel uniform, break, canteen, lessons, queue, clubs).",
                  "At my school we wear a uniform. We have six lessons every day. In the break we queue in the canteen. After school I go to a club.",
                  ["Mindestens 5 Wörter aus der Wortliste kommen vor.", "Die Sätze sind richtig gebaut (Subjekt und Verb).", "Die Wörter sind richtig geschrieben.", "Die Sätze sind verständlich."],
                  4, B_E))
    return a


def build():
    p = pack(ID, "Englisch Teil 2b: Wortschatz (1) – Schule, Bühne, Wortfamilien",
             "Wortschatz zu Unit 2 „A school day“: Wortfamilien auf -er, Schule und Schultag in Großbritannien, Bühne, Musical und Gefühle, kleine Wörter und Wendungen. Mit Lernblatt und Übungsaufgaben.",
             lernblatt(), aufgaben(), min_aufgaben=34,
             hinweis="Wörter und Bedeutungen folgen der Vokabelliste Unit 2 (S. 184–187). Alle Sätze und Texte sind selbst ausgedacht. In den Antworten zählt jeder Buchstabe, denn auch in der Arbeit zählt die Schreibweise.")
    return [nachlesen(p, {B_A: L1, B_B: L2, B_C: L3, B_D: L4, B_E: [L2, L3, L4, L5]})]


if __name__ == "__main__":
    for p in build():
        print(p["id"], len(p["aufgaben"]), "Aufgaben")
