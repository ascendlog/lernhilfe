"""Englisch Klasse 6, Paket 2a: Hören (Hörstrategien, Zahlen, Datum, Uhrzeiten, Telefonnummern, Dialoge, längere Hörtexte).

Alle Hörtexte sind selbst geschrieben (die Hörtexte und Audios des Buchs und des Workbooks liegen nicht vor) und werden in der App
vorgelesen (Sprache en-GB, Knopf „Anhören“). Namen sind erfunden. Zahlen und Zeiten sind im Hörtext ausgeschrieben.
"""
from eng_lib import *

ID = "englisch-2a-hoeren"

B_A = "A – Zahlen verstehen (13 oder 30?)"
B_B = "B – Datum und Ordnungszahlen"
B_C = "C – Uhrzeiten"
B_D = "D – Telefonnummern, Buchstaben und Preise"
B_E = "E – Kurze Gespräche"
B_F = "F – Ein längerer Hörtext"

L1 = "Hörstrategien"
L2 = "Zahlen verstehen"
L3 = "Datum und Ordnungszahlen"
L4 = "Uhrzeiten"
L5 = "Telefonnummern, Buchstaben und Preise"
L6 = "Richtig oder falsch? Antworten finden"


def lernblatt():
    return [
        lb(L1,
           "Beim **Hören** musst du nicht jedes Wort verstehen. Diese Strategien helfen dir:\n\n"
           "- **Vorher:** Lies zuerst die Aufgabe. Überlege: Worum geht es? Welche Wörter könnten vorkommen (Zahlen, Orte, Namen)?\n"
           "- **Beim ersten Hören:** Achte auf das Wichtigste. Notiere kurze Stichwörter, keine ganzen Sätze.\n"
           "- **Geräusche** (Klingel, Verkehr, Stimmen) verraten oft den **Ort**.\n"
           "- **Beim zweiten Hören:** Prüfe deine Antworten und fülle Lücken.\n"
           "- **Nicht aufgeben:** Wenn du ein Wort nicht verstehst, hör auf das Wort davor und danach. Rate mit dem Zusammenhang.\n"
           "- **Antworten kurz halten.** Bei Lückentexten zählt die **Rechtschreibung**: Schreibe Zahlen und Wörter genau.\n\n"
           "Achte auch auf Wörter wie **but** (aber), **not** und **no**: Sie ändern oft die Aussage.",
           merke="Aufgabe vorher lesen, Schlüsselwörter hören, nicht jedes Wort verstehen müssen, beim zweiten Hören prüfen."),
        lb(L2,
           "Zahlen mit **-teen** und **-ty** klingen ähnlich. Der Unterschied liegt in der **Betonung**:\n\n"
           "- **thirTEEN** (13): hinten betont, das -teen ist lang.\n"
           "- **THIRty** (30): vorn betont, das -ty ist kurz.\n\n"
           "So bildest du die Zahlen:\n\n"
           "- 13 thirteen, 14 fourteen, 15 **fifteen**, 16 sixteen, 17 seventeen, 18 **eighteen**, 19 nineteen\n"
           "- 30 thirty, 40 **forty**, 50 **fifty**, 60 sixty, 70 seventy, 80 **eighty**, 90 ninety\n\n"
           "**Achtung bei der Schreibweise:** four**teen** aber **forty** (ohne u), five → **fif**teen und **fif**ty, eight → eighteen aber **eighty** (nur ein t).",
           merke="-teen: Betonung hinten (thirTEEN). -ty: Betonung vorn (THIRty). Schreibe forty ohne u, fifty ohne v, eighty mit einem t."),
        lb(L3,
           "Für das **Datum** brauchst du **Ordnungszahlen**:\n\n"
           "- 1st **first**, 2nd **second**, 3rd **third**, 4th fourth, 5th **fifth**\n"
           "- 9th **ninth**, 12th **twelfth**, 13th thirteenth, 20th **twentieth**, 21st twenty-first, 30th **thirtieth**\n\n"
           "Man sagt: **the thirteenth of May** oder **May the thirteenth**. Geschrieben: 13th May oder May 13th.\n\n"
           "**Achtung:** Bei den Ordnungszahlen gibt es Sonderformen: fifth (nicht fiveth), twelfth (nicht twelveth), ninth (nicht nineth). Bei Zahlen auf -y wird das y zu ie: twenty → twentieth, thirty → thirtieth.\n\n"
           "Die Monate: January, February, March, April, May, June, July, August, September, October, November, December.",
           merke="Sonderformen: first, second, third, fifth, ninth, twelfth. twenty → twentieth, thirty → thirtieth."),
        lb(L4,
           "So sagt man die **Uhrzeit**:\n\n"
           "- **o'clock** = volle Stunde: 9:00 = nine o'clock\n"
           "- **quarter past** = Viertel nach: 8:15 = quarter past eight\n"
           "- **half past** = halb danach (30 Minuten nach der vollen Stunde): 7:30 = half past seven\n"
           "- **quarter to** = Viertel vor: 8:45 = quarter to nine\n"
           "- **… past** (nach) bis 30 Minuten: 10:20 = twenty past ten\n"
           "- **… to** (vor) nach der halben Stunde: 11:55 = five to twelve\n\n"
           "**Achtung:** **half past seven** ist 7:30 (nicht 6:30). Im Deutschen heißt 7:30 „halb acht“. Rechne also nicht deutsch, sondern: Stunde + half past.",
           merke="past = nach, to = vor. half past seven = 7:30 (nicht halb acht = 7:30 deutsch gedacht)."),
        lb(L5,
           "**Telefonnummern** sagt man Ziffer für Ziffer. Die Null heißt **oh** oder **zero**. Zwei gleiche Ziffern: **double** (double five = 55).\n\n"
           "**Buchstabieren:** Bei Namen kommen Buchstaben einzeln vor. Verwechsle nicht: **E** (sprich i) und **I** (sprich ai), **G** (dschi) und **J** (dschei).\n\n"
           "**Preise:** £4.50 = four pounds fifty. 50p = fifty pence. Achte auf thirteen und thirty, fifteen und fifty.",
           merke="0 = oh / zero. 55 = double five. £4.50 = four pounds fifty."),
        lb(L6,
           "Bei **Richtig / Falsch** (right / wrong) geht es darum, ob die Aussage zum Hörtext passt.\n\n"
           "- Lies die Aussage zuerst und suche das **Schlüsselwort** (Zahl, Name, Ort, Tag).\n"
           "- Achte auf **Gegenteile**: Wenn der Sprecher sagt „not on Tuesday, but on Thursday“, dann ist Tuesday falsch.\n"
           "- Wenn eine Aussage nur teilweise stimmt, ist sie **falsch**.\n"
           "- Bei **Auswahl** (a, b, c) hilft es, falsche Antworten zu streichen.\n"
           "- **Kurzantworten:** Schreibe nur das Wichtige (eine Zahl, ein Wort).",
           merke="Schlüsselwort suchen, auf but und not achten. Stimmt nur ein Teil der Aussage, ist sie falsch."),
    ]


# ---------------------------------------------------------------- Hörtexte (eigene Texte)

T_PLAN = ("Hi Ruby, this is Tom. Are you going to join the drama club this year? "
          "Yes, I am. I'm going to try for the school musical. Are you going to try too? "
          "No, I'm not. I'm going to stay in the chess club. The auditions are on Tuesday at four o'clock, not on Wednesday. "
          "OK. Then I'm going to practise a song at the weekend. Good luck!")
T_BUS = ("Excuse me, is this seat free? Yes, please sit down. Thanks. Have you got your ticket? The driver is coming. "
         "Oh yes, here it is. Where do you get off? At the town hall. Me too. The next stop is the town hall.")
T_WOCHENENDE = ("What are you going to do on Saturday, Mia? I'm going to visit my grandma. And on Sunday? "
                "We are going to have a picnic in the park, but only if it doesn't rain. Are your cousins going to come too? "
                "No, they aren't. They are going to stay at home and watch a film.")
T_SCHULE = ("Welcome to Greenfield School. My name is Mrs Parker and I am the head teacher. The doors open at quarter past eight. "
            "Registration is at twenty to nine, and the teachers call out your names. You have five lessons every day. "
            "The break is at half past ten, and lunch is at half past twelve in the canteen. All students wear a green uniform. "
            "After school there are clubs: the choir on Monday, the chess club on Wednesday and the football club on Friday. "
            "Please remember: earphones are not allowed in class, and don't be late!")


def aufgaben():
    a = []
    # ---------------------------------------------------------------- A: Zahlen
    a.append(kurz("Höre zu. Wie viele Pfund kostet das Ticket? Schreibe die Zahl mit Ziffern.", ["13", "thirteen"], B_A, vorlesen="The ticket costs thirteen pounds.",
                  info="Im Text: „thirteen pounds“. thirTEEN (hinten betont) = 13, THIRty (vorn betont) = 30."))
    a.append(kurz("Höre zu. Wie viele Schüler sind in der Klasse? Schreibe die Zahl mit Ziffern.", ["30", "thirty"], B_A, vorlesen="There are thirty students in my class.",
                  info="Im Text: „thirty students“. THIRty (vorn betont) = 30, thirTEEN (hinten betont) = 13."))
    a.append(mit_ton(mc("Höre zu. Wie alt ist die Sprecherin?", "15", ["50", "5", "16"], B_A,
                        info="Im Text: „fifteen years old“. fifTEEN (hinten betont) = 15, FIFty (vorn betont) = 50."),
                     "I am fifteen years old."))
    a.append(mit_ton(mc("Höre zu. Wie alt ist der Großvater?", "70", ["17", "7", "60"], B_A,
                        info="Im Text: „My grandpa is seventy.“ SEVenty (vorn betont) = 70, sevenTEEN (hinten betont) = 17."),
                     "My grandpa is seventy."))
    a.append(kurz("Höre zu. Welche Nummer hat der Bus? Schreibe die Zahl mit Ziffern.", ["16", "sixteen"], B_A, vorlesen="The bus number is sixteen.",
                  info="Im Text: „sixteen“. sixTEEN = 16, SIXty = 60."))
    a.append(kurz("Höre zu. Wie viele Kinder sind in der Halle? Schreibe die Zahl mit Ziffern.", ["80", "eighty"], B_A, vorlesen="Eighty children are in the hall.",
                  info="Im Text: „eighty children“. EIGHty = 80, eighTEEN = 18."))
    a.append(luecke("Höre zu und ergänze die Raumnummern (Ziffern).",
                    "Choir: room {{14|fourteen}}\nBand: room {{40|forty}}\nDrama club: room {{19|nineteen}}",
                    B_A, wortbank=False, vorlesen="Room fourteen is for the choir. Room forty is for the band. Room nineteen is for the drama club.",
                    info="fourTEEN = 14 (hinten betont), FORty = 40 (vorn betont), ninETEEN = 19. forty schreibt man ohne u."))
    a.append(luecke("Höre zu und ergänze die Zahlen (Ziffern).",
                    "The bus leaves in {{13|thirteen}} minutes.\nThe film is {{90|ninety}} minutes long.\nThe tickets cost £{{18|eighteen}}.",
                    B_A, wortbank=False, vorlesen="The bus leaves in thirteen minutes. The film is ninety minutes long. The tickets cost eighteen pounds.",
                    info="thirTEEN = 13, NINEty = 90, eighTEEN = 18. Auf die Betonung achten: -teen hinten, -ty vorn."))
    a.append(mit_ton(tf("Höre zu. Die Sprecherin sagt eine Zahl: „thirty“. Dann ist die Zahl 13.", False, B_A,
                        info="thirty = 30. Die Zahl 13 heißt thirteen. Beim Hören unterscheidest du an der Betonung."),
                     "I am thirty."))
    a.append(kurz("Schreibe die Zahl 15 als Wort.", ["fifteen"], B_A,
                  info="15 = fifteen (nicht fiveteen). five wird in fifteen und fifty zu fif."))
    a.append(kurz("Schreibe die Zahl 40 als Wort.", ["forty"], B_A,
                  info="40 = forty. Anders als four ist forty ohne u."))

    # ---------------------------------------------------------------- B: Datum
    a.append(mit_ton(mc("Höre zu. Wann hat die Sprecherin Geburtstag?", "13th May", ["30th May", "13th March", "30th March"], B_B,
                        info="Im Text: „thirteenth of May“. thirTEENth = 13th, THIRtieth = 30th, May = Mai."),
                     "My birthday is on the thirteenth of May."))
    a.append(mit_ton(mc("Höre zu. Wann ist die Schulaufführung?", "30th June", ["13th June", "30th July", "3rd June"], B_B,
                        info="Im Text: „thirtieth of June“. THIRtieth = 30th, June = Juni."),
                     "The school show is on the thirtieth of June."))
    a.append(luecke("Höre zu und ergänze die Daten. Schreibe nur die Zahl.",
                    "Class trip: {{12|twelfth}} June\nParents' evening: {{30|thirtieth}} June",
                    B_B, wortbank=False, vorlesen="Hello, this is the school office. The class trip is on the twelfth of June. The parents' evening is on the thirtieth of June. Please remember the dates.",
                    info="Im Text: „twelfth of June“ (12.) und „thirtieth of June“ (30.). Die Ordnungszahl twelfth hört sich anders an als twenty."))
    a.append(mit_ton(zuordnen("Höre zu. Welche Veranstaltung ist an welchem Tag?",
                              [("school show", "15 July"), ("sports day", "12 July"), ("summer disco", "13 July"), ("last day of school", "30 July")], B_B,
                              info="Im Text: school show fifteenth, sports day twelfth, summer disco thirteenth, last day of school thirtieth (alle im July)."),
                     "The school show is on the fifteenth of July. Sports day is on the twelfth of July. The summer disco is on the thirteenth of July. The last day of school is on the thirtieth of July."))
    a.append(kurz("Schreibe „13th“ als Wort (nur die Ordnungszahl).", ["thirteenth"], B_B,
                  info="13th = thirteenth. Zahl + th, aber Achtung: thir- (nicht three-)."))
    a.append(kurz("Schreibe „12th“ als Wort (nur die Ordnungszahl).", ["twelfth"], B_B,
                  info="12th = twelfth: Das v von twelve fällt weg: twelfth."))
    a.append(kurz("Schreibe „20th“ als Wort (nur die Ordnungszahl).", ["twentieth"], B_B,
                  info="20th = twentieth: Bei Zahlen auf -y wird das y zu ie, dann kommt -th."))
    a.append(mc("Wie schreibt man „5th“ als Wort?", "fifth", ["fiveth", "fivth", "fith"], B_B,
                info="Sonderform: 5th = fifth."))
    a.append(tf("1st, 2nd und 3rd heißen first, second und third.", True, B_B,
                info="Die ersten drei Ordnungszahlen sind Sonderformen: first, second, third."))
    a.append(mit_ton(kurz("Höre zu. In welchem Monat hat Tim Geburtstag? Schreibe den Monat.", ["February"], B_B,
                          info="Im Text: „in February“. February (Februar) schreibt man mit r vor dem u: Feb-ru-ary."),
                      "My name is Tim. My birthday is in February."))

    # ---------------------------------------------------------------- C: Uhrzeiten
    a.append(mit_ton(mc("Höre zu. Wann beginnt der Film?", "7:30", ["6:30", "7:15", "7:45"], B_C,
                        info="Im Text: „half past seven“ = 7:30 (30 Minuten nach sieben). Nicht deutsch denken: halb acht heißt auf Englisch half past seven."),
                     "The film starts at half past seven."))
    a.append(mit_ton(mc("Höre zu. Wann beginnt der Unterricht?", "8:15", ["8:45", "7:15", "9:15"], B_C,
                        info="Im Text: „quarter past eight“ = Viertel nach acht = 8:15."),
                     "The first lesson starts at quarter past eight."))
    a.append(mit_ton(mc("Höre zu. Wann fährt der Bus?", "8:45", ["9:15", "8:15", "9:45"], B_C,
                        info="Im Text: „quarter to nine“ = Viertel vor neun = 8:45."),
                     "The bus leaves at quarter to nine."))
    a.append(mit_ton(mc("Höre zu. Wann ist die Pause?", "10:20", ["10:40", "9:20", "10:02"], B_C,
                        info="Im Text: „twenty past ten“ = zwanzig nach zehn = 10:20."),
                     "The break is at twenty past ten."))
    a.append(mit_ton(mc("Höre zu. Wann kommt der Zug an?", "11:55", ["12:05", "11:05", "12:55"], B_C,
                        info="Im Text: „five to twelve“ = fünf vor zwölf = 11:55."),
                     "The train arrives at five to twelve."))
    a.append(luecke("Höre zu und ergänze die Uhrzeiten (Ziffern).",
                    "Registration: {{8:45|8.45}}\nFirst lesson: {{9:00|9.00|9}}\nBreak: {{10:30|10.30}}",
                    B_C, wortbank=False, vorlesen="Registration is at quarter to nine. The first lesson starts at nine o'clock. The break is at half past ten.",
                    info="quarter to nine = 8:45, nine o'clock = 9:00, half past ten = 10:30."))
    a.append(mit_ton(reihenfolge("Höre zu. In welcher Reihenfolge läuft der Schultag ab?", ["registration", "first lesson", "break", "lunch"], B_C,
                                 info="Im Text: First registration, then the first lesson, after that the break and then lunch."),
                     "First, we have registration. Then the first lesson. After that it's the break and then lunch."))
    a.append(kurz("Wie sagt man 6:15 auf Englisch? Schreibe es mit Wörtern.", ["quarter past six", "a quarter past six", "six fifteen"], B_C,
                  info="6:15 = quarter past six (Viertel nach sechs)."))
    a.append(tf("„Half past two“ ist 2:30. Und „quarter to three“ ist 3:15.", False, B_C,
                info="half past two = 2:30 stimmt, aber quarter to three = 2:45 (Viertel vor drei). Die Aussage ist insgesamt falsch."))

    # ---------------------------------------------------------------- D: Telefon, Buchstaben, Preise
    a.append(mit_ton(mc("Höre zu. Wie lautet die Telefonnummer?", "017 55 39", ["017 5 539", "017 53 9", "017 55 93"], B_D,
                        info="Im Text: oh one seven, double five, three, nine = 017 55 39. double five = 55."),
                     "My phone number is oh one seven, double five, three, nine."))
    a.append(mit_ton(kurz("Höre zu. Der Name wird buchstabiert. Schreibe den Namen.", ["Jonas"], B_D,
                          info="Die Buchstaben J-O-N-A-S ergeben den Namen Jonas."),
                     "My name is Jonas. That is J. O. N. A. S."))
    a.append(mit_ton(mc("Höre zu. Wie viel kostet das Heft?", "£4.50", ["£4.15", "£14.50", "£40.50"], B_D,
                        info="Im Text: four pounds fifty = £4.50. fifty (vorn betont) ist 50."),
                     "The notebook costs four pounds fifty."))
    a.append(mit_ton(kurz("Höre zu. Wie viele Pfund kostet die Karte? Schreibe die Zahl.", ["12", "£12", "twelve"], B_D,
                          info="Im Text: twelve pounds = £12. Auf twelve und twenty achten."),
                     "The ticket costs twelve pounds."))
    a.append(tf("„Double nine“ bedeutet 99.", True, B_D,
                info="double + Zahl heißt: die Ziffer zweimal. double nine = 99, double five = 55."))

    # ---------------------------------------------------------------- E: Gespräche
    a.append(mit_ton(mc("Höre zu. Wo sind die beiden Personen?", "in a bus", ["in a cinema", "in a canteen", "in a classroom"], B_E,
                        info="Hinweise im Gespräch: ticket, driver, get off, stop. Das alles passt zu einem Bus."),
                     T_BUS))
    a.append(mit_ton(tf("Höre zu. Die beiden steigen an der Stadthalle (town hall) aus.", True, B_E,
                        info="Im Gespräch: „At the town hall. Me too.“ Beide steigen also an der town hall aus."),
                     T_BUS))
    a.append(mit_ton(mc("Höre zu. Was hat Ruby vor?", "Sie will bei dem Schulmusical vorsprechen.", ["Sie will im Schachclub bleiben.", "Sie will nicht mitmachen.", "Sie will ein Lied für Tom schreiben."], B_E,
                        info="Ruby sagt: „I'm going to try for the school musical.“ Im Schachclub bleibt Tom."),
                     T_PLAN))
    a.append(mit_ton(tf("Höre zu. Das Vorsprechen ist am Mittwoch.", False, B_E,
                        info="Im Text: „on Tuesday at four o'clock, not on Wednesday“. Es ist also am Dienstag."),
                     T_PLAN))
    a.append(mit_ton(kurz("Höre zu. Um wie viel Uhr ist das Vorsprechen? Schreibe die Uhrzeit.", ["4", "four", "4 o'clock", "four o'clock", "4:00", "4pm", "4 pm"], B_E,
                          info="Im Text: „at four o'clock“. Das ist 4:00."),
                      T_PLAN))
    a.append(mit_ton(mc("Höre zu. Was macht Tom?", "Er bleibt im Schachclub.", ["Er macht bei dem Musical mit.", "Er hört mit dem Schach auf.", "Er ruft Ruby am Mittwoch an."], B_E,
                        info="Tom sagt: „I'm going to stay in the chess club.“"),
                     T_PLAN))
    a.append(mit_ton(mc("Höre zu. Was macht Mia am Samstag?", "Sie besucht ihre Oma.", ["Sie macht ein Picknick.", "Sie sieht einen Film.", "Sie bleibt zu Hause."], B_E,
                        info="Mia sagt: „On Saturday I'm going to visit my grandma.“"),
                     T_WOCHENENDE))
    a.append(mit_ton(tf("Höre zu. Das Picknick am Sonntag findet auf jeden Fall statt.", False, B_E,
                        info="Das Picknick ist nur, wenn es nicht regnet („but only if it doesn't rain“)."),
                     T_WOCHENENDE))
    a.append(mit_ton(tf("Höre zu. Mias Cousins kommen zum Picknick.", False, B_E,
                        info="Mia sagt „No, they aren't.“ Die Cousins bleiben zu Hause und sehen einen Film."),
                     T_WOCHENENDE))

    # ---------------------------------------------------------------- F: längerer Hörtext
    a.append(luecke("Höre zu und ergänze die Uhrzeiten (Ziffern).",
                    "Doors open: {{8:15|8.15}}\nRegistration: {{8:40|8.40}}\nBreak: {{10:30|10.30}}\nLunch: {{12:30|12.30}}",
                    B_F, wortbank=False, vorlesen=T_SCHULE,
                    info="quarter past eight = 8:15, twenty to nine = 8:40, half past ten = 10:30, half past twelve = 12:30."))
    a.append(luecke("Höre zu und ergänze die Wörter.",
                    "Lessons every day: {{5|five}}\nUniform colour: {{green}}\nLunch is in the {{canteen}}.\nNot allowed in class: {{earphones}}",
                    B_F, wortbank=False, vorlesen=T_SCHULE,
                    info="Im Text: five lessons, a green uniform, lunch in the canteen, earphones are not allowed in class."))
    a.append(mit_ton(zuordnen("Höre zu. Welcher Club ist an welchem Tag?",
                              [("choir", "Monday"), ("chess club", "Wednesday"), ("football club", "Friday")], B_F,
                              info="Im Text: the choir on Monday, the chess club on Wednesday and the football club on Friday."),
                     T_SCHULE))
    a.append(mit_ton(tf("Höre zu. Die Schule beginnt mit der Anwesenheitskontrolle (registration) um 8:40.", True, B_F,
                        info="Im Text: „Registration is at twenty to nine“ = 8:40."),
                     T_SCHULE))
    a.append(mit_ton(tf("Höre zu. Man darf im Unterricht Kopfhörer tragen.", False, B_F,
                        info="Im Text: „earphones are not allowed in class“."),
                     T_SCHULE))
    a.append(mit_ton(mc("Höre zu. Wer spricht?", "die Schulleiterin", ["eine Schülerin", "eine Lehrerin der Klasse 6", "ein Busfahrer"], B_F,
                        info="Die Sprecherin sagt: „My name is Mrs Parker and I am the head teacher.“ Head teacher = Schulleiterin."),
                     T_SCHULE))
    a.append(mit_ton(reihenfolge("Höre zu. In welcher Reihenfolge nennt die Sprecherin diese Dinge?", ["Türen öffnen", "Registration", "Pause", "Mittagessen"], B_F,
                                 info="Im Text: doors open, registration, break at half past ten, lunch at half past twelve."),
                     T_SCHULE))
    a.append(frei("Schreibe 2 bis 3 Sätze (auf Englisch) über deinen Schultag: Wann beginnt die Schule, wann ist Pause?",
                  "School starts at eight o'clock. We have six lessons. The break is at ten o'clock.",
                  ["Es gibt mindestens zwei vollständige Sätze.", "Die Uhrzeiten sind richtig auf Englisch genannt (o'clock, half past, quarter past, quarter to).", "Die Rechtschreibung stimmt."],
                  3, B_F))
    return a


def build():
    p = pack(ID, "Englisch Teil 2a: Hören (Listening)",
             "Hörverstehen für die Englischarbeit: Hörstrategien, Zahlen (13 oder 30?), Datum mit Ordnungszahlen, Uhrzeiten, Telefonnummern, Buchstaben und Preise, kurze Gespräche und ein längerer Hörtext. Mit Lernblatt und Übungsaufgaben.",
             lernblatt(), aufgaben(), min_aufgaben=34,
             hinweis="Die Hörtexte (Knopf „Anhören“) sind selbst geschrieben, nicht aus dem Buch oder Workbook, und werden vom Browser mit einer britischen Stimme vorgelesen. Unter jeder Höraufgabe steht aufklappbar „Text zum Vorlesen (für Eltern)“: Damit können die Eltern den Text selbst vorlesen, wenn die Stimme des Browsers nicht geht. Erst nach dem Lösen aufklappen, sonst fehlt die Übung im Hören. "
                     "Die Stimme kann bei Zahlen und Buchstaben ungewohnt klingen. Beim Hören gilt wie in der Arbeit: erst die Aufgabe lesen, dann zuhören.")
    return [nachlesen(p, {B_A: L2, B_B: L3, B_C: L4, B_D: L5, B_E: [L1, L6], B_F: [L1, L6]})]


if __name__ == "__main__":
    for p in build():
        print(p["id"], len(p["aufgaben"]), "Aufgaben")
