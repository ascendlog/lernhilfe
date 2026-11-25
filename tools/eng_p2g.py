"""Englisch Klasse 6, Paket 2g: Steigerung der Adjektive 2 (than, the … of/in, as … as, not as … as, Umformen, Texte).

Zahlen in den Tabellen sind erfunden, die Aussagen werden gegen die Daten per assert geprüft. Namen sind erfunden.
"""
from eng_lib import *
from geo_lib import svg_tabelle

ID = "englisch-2g-steigerung-2"

B_A = "A – Vergleiche mit than"
B_B = "B – Der Superlativ: the … of / in"
B_C = "C – as … as und not as … as"
B_D = "D – Komparativ, Superlativ oder Grundform?"
B_E = "E – Vergleiche umschreiben"
B_F = "F – Tabellen und Texte"

L1 = "Vergleichen mit than"
L2 = "Der Superlativ im Satz: of und in"
L3 = "as … as und not as … as"
L4 = "Vergleiche umschreiben"
L5 = "Welche Form? Typische Fehler"


def lernblatt():
    return [
        lb(L1,
           "Mit dem **Komparativ** vergleichst du **zwei** Dinge. Das deutsche „als“ heißt im Englischen **than** (nicht „as“, nicht „then“).\n\n"
           "- Tom is **taller than** Ben.\n"
           "- This book is **more interesting than** that film.\n"
           "- My sister is **older than** me.\n\n"
           "Nach than stehen oft die Objektformen: older than **me**, faster than **him**, smaller than **us**.\n\n"
           "**Achtung:** than (als) und then (dann) klingen ähnlich, bedeuten aber etwas anderes. Beim Vergleich schreibst du immer **than**.",
           merke="Komparativ + than = „… er als …“. Beispiel: faster than, more expensive than."),
        lb(L2,
           "Der **Superlativ** nennt das **Höchste, Kleinste oder Beste unter mehreren**. Er hat immer **the** vor sich: Tom is **the tallest**.\n\n"
           "Danach sagst du, womit verglichen wird:\n\n"
           "- **of** + mehrere Personen oder Dinge: the tallest **of the three**, the best **of all**\n"
           "- **in** + Gruppe oder Ort: the best singer **in the school**, the most beautiful village **in Britain**, the oldest **in our family**\n\n"
           "Das kleine **the** gehört fest zum Superlativ. Bei most gehört es ebenfalls dazu: **the most** interesting.",
           merke="Superlativ: the + -est / most … Danach of (mehrere) oder in (Ort, Gruppe)."),
        lb(L3,
           "Mit **as … as** (so … wie) sagst du, dass zwei Dinge **gleich** sind: Tom is **as tall as** Ben.\n\n"
           "Mit **not as … as** (nicht so … wie) sagst du, dass das erste **weniger** hat: Ben is **not as tall as** Tom. Das bedeutet: Tom ist größer als Ben.\n\n"
           "Zwischen as und as steht immer die **Grundform** des Adjektivs: as tall as, not as old as, as expensive as. Nie as taller as und nie as more expensive as.",
           merke="as + Grundform + as = gleich. not as + Grundform + as = weniger."),
        lb(L4,
           "Du kannst fast jeden Vergleich auf zwei Arten sagen. Dazu drehst du den Satz um:\n\n"
           "- Mia is **older than** Tom. = Tom is **not as old as** Mia.\n"
           "- This bag is **more expensive than** that bag. = That bag is **not as expensive as** this bag.\n"
           "- Mia is **taller than** Tom. = Tom is **shorter than** Mia.\n\n"
           "Dafür brauchst du die Gegensätze: tall – short, old – young, big – small, fast – slow, cheap – expensive, heavy – light.",
           merke="A is taller than B = B is not as tall as A = B is shorter than A."),
        lb(L5,
           "So entscheidest du, welche Form du brauchst:\n\n"
           "- Siehst du **than** oder sind es **zwei** Dinge? → **Komparativ** (taller than).\n"
           "- Siehst du **the**, **of the three**, **of all** oder **in the class**? → **Superlativ** (the tallest).\n"
           "- Siehst du **as … as**? → **Grundform** (as tall as).\n\n"
           "**Typische Fehler:**\n\n"
           "- Komparativ statt Superlativ: Mia is the older of the three. → Mia is **the oldest** of the three.\n"
           "- most vergessen: the beautiful girl in the class → the **most** beautiful girl in the class.\n"
           "- as statt than: bigger as → bigger **than**.\n"
           "- doppelt gesteigert: more taller, most tallest → taller, the tallest.\n"
           "- the vergessen: She is tallest. → She is **the** tallest.",
           merke="than → Komparativ. the … of / in → Superlativ. as … as → Grundform."),
    ]


# Erfundene Daten
KIDS = {"Mara": (11, 150), "Nils": (12, 146), "Pia": (10, 156)}                # Alter, Größe in cm
TIERE = {"cheetah": 110, "horse": 70, "dog": 55}                                 # km/h (vereinfacht)
BIKES = {"red": 120, "blue": 180, "green": 150}                                  # Preis in Pfund
JUNGS = {"Jonas": (11, 148), "Elias": (12, 143), "Oskar": (11, 152)}

assert KIDS["Pia"][1] > KIDS["Mara"][1] > KIDS["Nils"][1]
assert KIDS["Nils"][0] > KIDS["Mara"][0] > KIDS["Pia"][0]
assert TIERE["cheetah"] > TIERE["horse"] > TIERE["dog"]
assert BIKES["blue"] > BIKES["green"] > BIKES["red"]
assert JUNGS["Oskar"][1] > JUNGS["Jonas"][1] > JUNGS["Elias"][1]
assert JUNGS["Elias"][0] > JUNGS["Jonas"][0] == JUNGS["Oskar"][0]


def tab_kids():
    return svg_tabelle(["Name", "Age", "Height"], [[n, f"{a} years", f"{h} cm"] for n, (a, h) in KIDS.items()], spalten_breit=[110, 130, 130])


ALT_KIDS = "Tabelle: Mara ist 11 Jahre alt und 150 cm groß, Nils ist 12 Jahre alt und 146 cm groß, Pia ist 10 Jahre alt und 156 cm groß."


def tab_tiere():
    return svg_tabelle(["Animal", "Speed"], [[n, f"{s} km/h"] for n, s in TIERE.items()], spalten_breit=[130, 150])


ALT_TIERE = "Tabelle: Gepard 110 km/h, Pferd 70 km/h, Hund 55 km/h."


def tab_bikes():
    return svg_tabelle(["Bike", "Price"], [[f"the {n} bike", f"£{p}"] for n, p in BIKES.items()], spalten_breit=[150, 120])


ALT_BIKES = "Tabelle: das rote Fahrrad kostet 120 Pfund, das blaue 180 Pfund, das grüne 150 Pfund."


def tab_jungs():
    return svg_tabelle(["Name", "Age", "Height"], [[n, f"{a} years", f"{h} cm"] for n, (a, h) in JUNGS.items()], spalten_breit=[110, 130, 130])


ALT_JUNGS = "Tabelle: Jonas ist 11 Jahre alt und 148 cm groß, Elias ist 12 Jahre alt und 143 cm groß, Oskar ist 11 Jahre alt und 152 cm groß."


def mit_bild(t, bild, alt):
    t["bild"] = bild
    t["bildAlt"] = alt
    return t


def aufgaben():
    a = []
    # ---------------------------------------------------------------- A: than
    a.append(mit_bild(luecke("Schau auf die Tabelle und ergänze die Komparative.",
                             "Pia is {{taller}} than Mara.\nNils is {{older}} than Mara.\nPia is {{younger}} than Nils.",
                             B_A, extra=["more tall", "oldest", "youngest"],
                             info="Pia (156 cm) ist größer als Mara (150 cm): taller than. Nils (12) ist älter als Mara (11): older than. Pia (10) ist jünger als Nils (12): younger than."),
                      tab_kids(), ALT_KIDS))
    a.append(mit_bild(kurz("Nils (146 cm) und Mara (150 cm): Nils is … than Mara. Schreibe die richtige Form von „short“.", ["shorter"], B_A,
                           info="short ist kurz: shorter. Nils ist kleiner als Mara, also: Nils is shorter than Mara."),
                      tab_kids(), ALT_KIDS))
    a.append(mc("Welches Wort fehlt? A horse is faster … a dog.", "than", ["then", "as", "that"], B_A,
                info="Nach dem Komparativ steht than (= als). Then bedeutet „dann“, as steht bei as … as."))
    a.append(mit_bild(mc("Welcher Satz stimmt mit der Tabelle überein?", "The blue bike is more expensive than the red bike.",
                         ["The blue bike is cheaper than the red bike.", "The red bike is more expensive than the green bike.", "The green bike is cheaper than the red bike."], B_A,
                         info="Das blaue Fahrrad kostet £180, das rote £120. Also ist das blaue teurer: more expensive than."),
                      tab_bikes(), ALT_BIKES))
    a.append(mit_bild(kurz("Schreibe einen Vergleich mit than: the blue bike (£180) – the green bike (£150) – expensive. Beginne mit „The blue bike“.",
                           ["The blue bike is more expensive than the green bike"], B_A,
                           info="expensive ist ein langes Adjektiv: more expensive than. Das blaue Fahrrad kostet mehr als das grüne."),
                      tab_bikes(), ALT_BIKES))
    a.append(mit_bild(tf("„A cheetah is faster than a horse.“ Das stimmt nach der Tabelle.", True, B_A,
                         info="Der Gepard läuft 110 km/h, das Pferd 70 km/h. Also: A cheetah is faster than a horse."),
                      tab_tiere(), ALT_TIERE))
    a.append(mit_bild(tf("„Nils is younger than Pia.“ Das stimmt nach der Tabelle.", False, B_A,
                         info="Nils ist 12, Pia ist 10. Also ist Nils älter: Nils is older than Pia."),
                      tab_kids(), ALT_KIDS))
    a.append(reihenfolge("Bringe die Wörter in die richtige Reihenfolge.", ["Pia", "is", "taller", "than", "Mara"], B_A,
                         info="Subjekt, is, Komparativ, than, zweites Subjekt: Pia is taller than Mara."))
    a.append(mc("Welcher Satz ist richtig?", "Mia is older than her brother.",
                ["Mia is older then her brother.", "Mia is older as her brother.", "Mia is more old than her brother."], B_A,
                info="than = als. Das Wort then bedeutet „dann“. old ist kurz: older (nicht more old)."))
    a.append(luecke("Setze den Komparativ von „heavy“, „boring“ und „small“ ein.",
                    "My bag is {{heavier}} than your bag.\nThis film is {{more boring}} than that book.\nA mouse is {{smaller}} than a cat.",
                    B_A, extra=["heavyer", "more small", "boringer"],
                    info="heavy → heavier (y wird i). boring ist lang: more boring. small ist kurz: smaller."))

    # ---------------------------------------------------------------- B: Superlativ
    a.append(mit_bild(luecke("Schau auf die Tabelle und ergänze die Superlative (ohne the).",
                             "Pia is the {{tallest}} of the three.\nNils is the {{oldest}} of the three.\nPia is the {{youngest}} of the three.",
                             B_B, extra=["taller", "most tall", "older"],
                             info="Pia ist mit 156 cm die Größte (the tallest), Nils mit 12 Jahren der Älteste (the oldest), Pia mit 10 Jahren die Jüngste (the youngest)."),
                      tab_kids(), ALT_KIDS))
    a.append(mit_bild(mc("Der Gepard in der Tabelle: The cheetah is … animal in the table.", "the fastest", ["faster", "the faster", "the most fast"], B_B,
                         info="Der Gepard ist von allen Tieren das schnellste: the fastest. fast ist kurz (-est), und beim Superlativ steht the."),
                      tab_tiere(), ALT_TIERE))
    a.append(luecke("Setze in oder of ein.",
                    "Tom is the best player {{in}} the team.\nMara is the oldest {{of}} the three girls.\nThis is the most beautiful beach {{in}} the world.\nHe is the fastest runner {{of}} all.",
                    B_B, auswahl=["in", "of"],
                    info="of steht bei mehreren Personen oder Dingen (of the three, of all). in steht bei einem Ort oder einer Gruppe (in the team, in the world)."))
    a.append(kurz("Bilde den Superlativ: Mia is the tall girl in our class. → Mia is the … girl in our class. Schreibe nur das fehlende Wort.", ["tallest"], B_B,
                  info="Der Superlativ von tall ist the tallest. Das the steht schon im Satz."))
    a.append(mit_bild(luecke("Ergänze den Superlativ.",
                             "The blue bike is the {{most expensive}} of the three bikes.\nThe red bike is the {{cheapest}} of the three bikes.",
                             B_B, extra=["expensivest", "most cheap"],
                             info="Das blaue Fahrrad kostet £180 und ist das teuerste: the most expensive (langes Adjektiv). Das rote kostet £120 und ist das billigste: the cheapest."),
                      tab_bikes(), ALT_BIKES))
    a.append(mit_bild(tf("„Mara is the oldest of the three.“ Das stimmt nach der Tabelle.", False, B_B,
                         info="Mara ist 11, Nils ist 12. Nils ist der Älteste: Nils is the oldest of the three."),
                      tab_kids(), ALT_KIDS))
    a.append(mc("Welcher Satz ist richtig?", "Lena is the best singer in our school.",
                ["Lena is best singer in our school.", "Lena is the goodest singer in our school.", "Lena is the best singer of our school."], B_B,
                info="Der Superlativ von good ist the best (unregelmäßig). Nach dem Superlativ steht in, wenn man von einem Ort oder einer Gruppe spricht (in our school)."))
    a.append(reihenfolge("Bringe die Satzteile in die richtige Reihenfolge.", ["This is", "the most beautiful", "village", "in Britain"], B_B,
                         info="Superlativ: the most beautiful, danach das Nomen und die Gruppe mit in."))
    a.append(kurz("Setze den Superlativ von „big“ ein: Our school is the … school in the town. Schreibe nur das fehlende Wort.", ["biggest"], B_B,
                  info="big verdoppelt das g: bigger, the biggest."))
    a.append(mc("Welche Form passt? Ruby is … of the three sisters.", "the youngest", ["younger", "the younger", "the most young"], B_B,
                info="Der Superlativ von young ist the youngest. of the three zeigt: unter mehreren (drei), also Superlativ mit the."))

    # ---------------------------------------------------------------- C: as … as
    a.append(luecke("Ergänze die Grundform. Ella und Finn sind beide 152 cm groß. Finn ist 11, Ella ist 12.",
                    "Ella is as {{tall}} as Finn.\nFinn is not as {{old}} as Ella.",
                    B_C, extra=["taller", "older"],
                    info="Zwischen as und as steht die Grundform: as tall as, not as old as."))
    a.append(mit_bild(kurz("Mara (150 cm) und Pia (156 cm): Mara is not … Pia. Schreibe die fehlenden Wörter (as … as).", ["as tall as"], B_C,
                           info="Mara ist kleiner als Pia, also: Mara is not as tall as Pia. Dazwischen steht die Grundform tall."),
                      tab_kids(), ALT_KIDS))
    a.append(mc("Welcher Satz ist richtig?", "Tom is as fast as Ben.",
                ["Tom is as faster as Ben.", "Tom is as fast than Ben.", "Tom is so fast as Ben."], B_C,
                info="Bei as … as steht die Grundform (fast). Danach kommt wieder as, nicht than."))
    a.append(tf("„Pia is not as old as Nils.“ Das stimmt nach der Tabelle (Pia 10, Nils 12).", True, B_C,
                info="not as old as = nicht so alt wie. Pia ist 10 und Nils ist 12, also ist Pia weniger alt."))
    a.append(mit_bild(luecke("Ergänze mit as … as.",
                             "The red bike is not as {{expensive}} as the blue bike.\nThe green bike is not as {{cheap}} as the red bike.",
                             B_C, extra=["more expensive", "cheaper"],
                             info="Das rote Fahrrad (£120) ist weniger teuer als das blaue (£180). Das grüne (£150) ist nicht so billig wie das rote. Zwischen as und as steht die Grundform."),
                      tab_bikes(), ALT_BIKES))
    a.append(kurz("Schreibe den Satz mit not as … as: Mia is taller than Ben. → Ben is not as … as Mia. Schreibe nur das Wort in der Mitte.", ["tall"], B_C,
                  info="Aus dem Vergleich mit taller than wird not as tall as: Ben is not as tall as Mia."))
    a.append(zuordnen("Ordne die Struktur der Bedeutung zu.",
                      [("as … as", "gleich (so … wie)"), ("not as … as", "weniger (nicht so … wie)"), ("… -er than", "mehr als (… er als)"), ("the … -est", "am meisten (Superlativ)")], B_C,
                      info="as … as: gleich. not as … as: weniger. -er than: mehr als (Komparativ). the -est: das Höchste unter mehreren (Superlativ)."))
    a.append(mc("Welche Form steht zwischen as … as?", "die Grundform (tall)", ["der Komparativ (taller)", "der Superlativ (tallest)", "more + Grundform"], B_C,
                info="Zwischen as und as steht immer die Grundform des Adjektivs: as tall as."))
    a.append(tf("„Tom is as taller as Ben.“ ist richtig.", False, B_C,
                info="Zwischen as und as steht die Grundform: Tom is as tall as Ben."))

    # ---------------------------------------------------------------- D: welche Form
    a.append(mc("Tom is … boy in our class. (tall)", "the tallest", ["taller", "the taller", "as tall"], B_D,
                info="in our class zeigt: unter vielen, also Superlativ mit the: the tallest."))
    a.append(mc("Tom is … than Ben. (tall)", "taller", ["the tallest", "tallest", "as tall"], B_D,
                info="than zeigt: Komparativ, ohne the: taller than."))
    a.append(luecke("Welche Stufe ist es? Wähle Grundform, Komparativ oder Superlativ.",
                    "Pia is taller than Mara. → {{Komparativ}}\nPia is the tallest of the three. → {{Superlativ}}\nPia is as tall as her cousin. → {{Grundform}}",
                    B_D, auswahl=["Grundform", "Komparativ", "Superlativ"],
                    info="than → Komparativ. the … of the three → Superlativ. as … as → Grundform."))
    a.append(zuordnen("Welche Stufe gehört zu welchem Signal?",
                      [("than", "Komparativ"), ("of the three", "Superlativ"), ("as … as", "Grundform")], B_D,
                      info="than verlangt den Komparativ. of the three verlangt den Superlativ. as … as verlangt die Grundform."))
    a.append(luecke("Setze den Komparativ oder den Superlativ ein.",
                    "My dog is {{bigger}} than your dog. But the {{biggest}} dog in our street is Rex.",
                    B_D, extra=["more big", "big"],
                    info="than → bigger (Komparativ, g wird doppelt). in our street → the biggest (Superlativ)."))
    a.append(kurz("Setze die richtige Form von „high“ ein: Mount Everest is the … mountain in the world. Schreibe nur das fehlende Wort.", ["highest"], B_D,
                  info="Der Berg ist der höchste von allen: Superlativ the highest."))
    a.append(mc("Welcher Satz ist richtig?", "Anna is the most intelligent girl in our group.",
                ["Anna is the intelligentest girl in our group.", "Anna is the more intelligent girl in our group.", "Anna is the intelligent girl in our group."], B_D,
                info="intelligent ist lang: the most intelligent. Mit in our group steht der Superlativ."))
    a.append(tf("„The more beautiful“ ist ein Superlativ.", False, B_D,
                info="„more beautiful“ ist ein Komparativ. Der Superlativ heißt the most beautiful."))

    # ---------------------------------------------------------------- E: umschreiben
    a.append(kurz("Schreibe denselben Vergleich mit not as … as: Mia is older than Tom. → Tom …", ["Tom is not as old as Mia", "Tom isn't as old as Mia"], B_E,
                  info="Du drehst den Satz um: Tom is not as old as Mia. Die Grundform old steht zwischen den beiden as."))
    a.append(kurz("Schreibe denselben Vergleich mit than: Ben isn't as fast as Max. → Max …", ["Max is faster than Ben"], B_E,
                  info="Ben ist weniger schnell, also ist Max schneller: Max is faster than Ben."))
    a.append(kurz("Schreibe denselben Vergleich mit dem Gegenwort „shorter“: Mia is taller than Tom. → Tom …", ["Tom is shorter than Mia"], B_E,
                  info="tall und short sind Gegensätze: Tom is shorter than Mia."))
    a.append(reihenfolge("Bringe die Wörter in die richtige Reihenfolge (Vergleich mit more).", ["The blue bike", "is more expensive", "than", "the red bike"], B_E,
                         info="more expensive than: langes Adjektiv mit more, danach than und das zweite Nomen."))
    a.append(kurz("Bilde einen Satz mit dem Komparativ: dog / small / horse. Beginne mit „A dog“.", ["A dog is smaller than a horse"], B_E,
                  info="small ist kurz: smaller than. Ein Hund ist kleiner als ein Pferd."))
    a.append(mc("Welcher Satz sagt dasselbe wie „The red bag is cheaper than the blue bag.“?", "The blue bag is more expensive than the red bag.",
                ["The blue bag is cheaper than the red bag.", "The blue bag is not as expensive as the red bag.", "The red bag is as cheap as the blue bag."], B_E,
                info="Wenn die rote Tasche billiger ist, ist die blaue teurer. Die anderen Sätze sagen das Gegenteil oder etwas anderes."))

    # ---------------------------------------------------------------- F: Tabellen und Texte
    a.append(luecke("Ergänze den Text.",
                    "There are five people in my family. My grandpa is the {{oldest}} (old). My dad is {{taller}} (tall) than my mum, but my brother is the {{tallest}} (tall) in the family. "
                    "My sister is {{younger}} (young) than me. My mum is the {{best}} (good) cook in the world. Her cake is {{more delicious}} (delicious) than any cake in the shop.",
                    B_F, extra=["goodest", "more tall", "youngest"],
                    info="old → the oldest, tall → taller (than) und the tallest (in the family), young → younger (than me), good → the best, delicious → more delicious."))
    a.append(mit_bild(luecke("Schau auf die Tabelle und ergänze.",
                             "Oskar is the {{tallest}}.\nElias is {{shorter}} than Jonas.\nJonas is not as {{tall}} as Oskar.\nElias is the {{oldest}} of the three boys.",
                             B_F, extra=["taller", "more tall", "older"],
                             info="Oskar hat 152 cm und ist der Größte. Elias (143) ist kleiner als Jonas (148). Jonas ist nicht so groß wie Oskar. Elias ist 12 und der Älteste."),
                      tab_jungs(), ALT_JUNGS))
    a.append(frei("Vergleiche zwei Tiere (zum Beispiel Hund und Katze, Pferd und Maus). Schreibe 3 Sätze mit than, as … as und the … -est.",
                  "A horse is bigger than a dog. A dog is not as big as a horse. The elephant is the biggest animal of all.",
                  ["Ein Satz hat einen richtigen Komparativ mit than.", "Ein Satz hat as … as oder not as … as mit der Grundform.", "Ein Satz hat einen richtigen Superlativ mit the (und of oder in)."],
                  3, B_F))
    a.append(frei("Vergleiche drei Personen aus deiner Familie oder deinem Freundeskreis (ohne Namen, zum Beispiel my cousin, my sister, my friend). Schreibe 4 Sätze.",
                  "My brother is older than me. My cousin is as tall as my sister. My friend is not as fast as my brother. My brother is the oldest of the four.",
                  ["Es kommt ein Komparativ mit than vor.", "Es kommt as … as oder not as … as mit der Grundform vor.", "Es kommt ein Superlativ mit the vor.", "Die Sätze sind richtig geschrieben (Verb is, Rechtschreibung der Steigerung)."],
                  4, B_F))
    return a


def build():
    p = pack(ID, "Englisch Teil 2g: Steigerung der Adjektive (2) – Vergleiche",
             "Comparison of adjectives, Teil 2: Vergleiche mit than, Superlativ mit the … of / in, as … as und not as … as, Vergleiche umschreiben, Tabellen und Texte. Mit Lernblatt und Übungsaufgaben.",
             lernblatt(), aufgaben(), min_aufgaben=34,
             hinweis="Alle Sätze, Namen und Zahlen sind selbst ausgedacht, nicht aus dem Schulbuch, dem Workbook oder den Arbeitsblättern. Die Tabellen sind erfunden.")
    return [nachlesen(p, {B_A: L1, B_B: L2, B_C: L3, B_D: L5, B_E: L4, B_F: [L1, L2, L3, L5]})]


if __name__ == "__main__":
    for p in build():
        print(p["id"], len(p["aufgaben"]), "Aufgaben")
