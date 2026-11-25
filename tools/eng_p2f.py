"""Englisch Klasse 6, Paket 2f: Steigerung der Adjektive 1 (Formen: -er / -est, Rechtschreibung, more / most, unregelmäßige Formen).

Alle Formen werden in eng_lib.steigerung() berechnet und gegen eine feste Liste geprüft. Sätze und Namen sind erfunden.
"""
from eng_lib import *

ID = "englisch-2f-steigerung-1"

B_A = "A – Kurze Adjektive: -er und -est"
B_B = "B – Rechtschreibung: e, doppelter Buchstabe, y"
B_C = "C – Lange Adjektive: more und most"
B_D = "D – Unregelmäßige Formen: good und bad"
B_E = "E – Welche Regel gilt?"
B_F = "F – Tabellen und Texte"

L1 = "Was ist die Steigerung?"
L2 = "Kurze Adjektive: -er und -est"
L3 = "Rechtschreibung der Formen"
L4 = "Lange Adjektive: more und most"
L5 = "Unregelmäßige Formen"


def lernblatt():
    return [
        lb(L1,
           "Mit der **Steigerung** (comparison of adjectives) vergleichst du Dinge, Tiere oder Personen. Jedes Adjektiv hat drei Stufen:\n\n"
           "- **Grundform:** tall (groß) – Tom is tall.\n"
           "- **Komparativ:** taller (größer) – Tom is taller than Ben.\n"
           "- **Superlativ:** the tallest (am größten) – Tom is the tallest in the class.\n\n"
           "Den Komparativ benutzt du, wenn du **zwei** Dinge vergleichst (mit **than** = als). Den Superlativ benutzt du für **das Größte, Kleinste, Beste** unter mehreren (mit **the** davor).",
           merke="Grundform: tall. Komparativ: taller (than). Superlativ: the tallest."),
        lb(L2,
           "Bei **kurzen Adjektiven** (meist eine Silbe) hängst du **-er** und **-est** an:\n\n"
           "- tall → taller → the tallest\n"
           "- old → older → the oldest\n"
           "- small → smaller → the smallest\n"
           "- fast → faster → the fastest\n"
           "- cheap → cheaper → the cheapest\n\n"
           "Das Adjektiv bleibt dabei unverändert. Vor dem Superlativ steht **the**. Vor dem Komparativ steht kein the: Anna is **taller** than Mia.",
           merke="Kurze Adjektive: -er (than) und the -est. Beispiel: old, older, the oldest."),
        lb(L3,
           "Bei einigen Adjektiven verändert sich beim Anhängen die **Schreibweise**:\n\n"
           "- **Endet das Adjektiv auf -e**, hängst du nur **-r** und **-st** an: nice → nicer → the nicest, large → larger → the largest.\n"
           "- **Kurzer Vokal + ein Konsonant:** Der Konsonant wird **doppelt** geschrieben: big → bigger → the biggest, hot → hotter → the hottest, thin → thinner → the thinnest.\n"
           "- **Konsonant + y:** Das y wird zu **i**: happy → happier → the happiest, funny → funnier → the funniest, easy → easier → the easiest.\n\n"
           "Merke dir zum Prüfen: Sprich das Wort mit Endung leise nach und zähle die Buchstaben.",
           merke="-e: nur -r / -st. Kurzer Vokal: Konsonant doppelt. y: wird zu i."),
        lb(L4,
           "Bei **langen Adjektiven** (zwei oder mehr Silben, aber nicht auf -y) steigerst du mit **more** und **most**. Das Adjektiv bleibt dabei unverändert:\n\n"
           "- beautiful → **more** beautiful → **the most** beautiful\n"
           "- expensive → **more** expensive → **the most** expensive\n"
           "- interesting → **more** interesting → **the most** interesting\n"
           "- intelligent, famous, difficult, dangerous, popular, boring …\n\n"
           "**Achtung:** Man sagt nie „more taller“ und nie „most tallest“. Entweder -er / -est **oder** more / most, nie beides zusammen.",
           merke="Lange Adjektive: more … (than) und the most …. Niemals -er und more zusammen."),
        lb(L5,
           "Zwei wichtige Adjektive haben **eigene Formen**. Du musst sie auswendig lernen:\n\n"
           "- **good** → **better** → **the best** (gut, besser, am besten)\n"
           "- **bad** → **worse** → **the worst** (schlecht, schlechter, am schlechtesten)\n\n"
           "Es heißt nie „gooder“, „more good“, „badder“ oder „the most bad“. Beispiel: My bike is **better** than your bike. This is **the best** song of all.",
           merke="good – better – the best. bad – worse – the worst."),
    ]


# Sammlung nach Kategorie
KURZ = ["tall", "small", "short", "long", "old", "young", "fast", "cheap", "strong", "high"]
E_ADJ = ["nice", "large", "late", "wide", "safe", "brave"]
VERD = ["big", "thin", "hot", "fat", "sad", "wet"]
Y_ADJ = ["happy", "funny", "pretty", "easy", "heavy", "busy", "lucky", "noisy"]
LANG_ADJ = ["beautiful", "expensive", "interesting", "intelligent", "famous", "boring", "difficult", "careful", "popular", "dangerous"]
IRR = ["good", "bad"]


def kategorie(adj):
    if adj in UNREGELMAESSIG:
        return "irr"
    if adj in LANG:
        return "lang"
    if adj in VERDOPPELN:
        return "verd"
    if adj in Y_WOERTER:
        return "y"
    if adj.endswith("e"):
        return "e"
    return "kurz"


def regel(adj):
    k, s = steigerung(adj)
    kat = kategorie(adj)
    return {
        "kurz": f"„{adj}“ ist kurz: einfach -er und -est anhängen: {adj} → {k} → the {s}.",
        "e": f"„{adj}“ endet schon auf -e: nur -r und -st anhängen: {adj} → {k} → the {s}.",
        "verd": f"„{adj}“ hat einen kurzen Vokal und einen Konsonanten am Ende: Der Konsonant wird verdoppelt: {adj} → {k} → the {s}.",
        "y": f"„{adj}“ endet auf Konsonant + y: Das y wird zu i: {adj} → {k} → the {s}.",
        "lang": f"„{adj}“ ist ein langes Adjektiv: more und most davor, das Adjektiv bleibt: {adj} → {k} → the {s}.",
        "irr": f"„{adj}“ hat eigene Formen: {adj} → {k} → the {s}.",
    }[kat]


def falsche_komp(adj):
    """Typische falsche Komparative (immer verschieden von der richtigen Form)."""
    k = komp(adj)
    kat = kategorie(adj)
    if kat == "kurz":
        f = ["more " + adj, adj + "est"]
    elif kat == "e":
        f = [adj + "er", "more " + adj]
    elif kat == "verd":
        f = [adj + "er", "more " + adj]
    elif kat == "y":
        f = [adj + "er", "more " + adj]
    elif kat == "lang":
        f = [adj + "er", "more " + adj + "er"]
    else:
        f = [{"good": "gooder", "bad": "badder"}[adj], "more " + adj]
    assert k not in f, (adj, k, f)
    return f


def falsche_sup(adj):
    s = sup(adj)
    kat = kategorie(adj)
    if kat == "kurz":
        f = ["the most " + adj, "the " + komp(adj)]
    elif kat in ("e", "verd", "y"):
        f = ["the " + adj + "est", "the most " + adj]
    elif kat == "lang":
        f = ["the " + adj + "est", "the more " + adj]
    else:
        f = [{"good": "the goodest", "bad": "the baddest"}[adj], "the most " + adj]
    assert "the " + s not in f, (adj, s, f)
    return f


def komp_kurz(adj):
    k = komp(adj)
    return kurz(f"Schreibe den Komparativ von „{adj}“.", [k], _abs(adj), info=regel(adj),
                tipp="Ist das Adjektiv kurz oder lang? Endet es auf e, y oder auf einen Konsonanten mit kurzem Vokal?")


def sup_kurz(adj):
    s = sup(adj)
    return kurz(f"Schreibe den Superlativ von „{adj}“ (mit the).", ["the " + s], _abs(adj), info=regel(adj),
                tipp="Vor dem Superlativ steht the.")


def komp_mc(adj):
    return mc(f"Was ist der richtige Komparativ von „{adj}“?", komp(adj), falsche_komp(adj), _abs(adj), info=regel(adj))


def sup_mc(adj):
    return mc(f"Was ist der richtige Superlativ von „{adj}“?", "the " + sup(adj), falsche_sup(adj), _abs(adj), info=regel(adj))


def _abs(adj):
    return {"kurz": B_A, "e": B_B, "verd": B_B, "y": B_B, "lang": B_C, "irr": B_D}[kategorie(adj)]


def tabelle(adjs, abschnitt, frage, extra=(), info=None):
    """Lückentext: Grundform – Komparativ – the Superlativ."""
    zeilen = []
    for ad in adjs:
        k, s = steigerung(ad)
        zeilen.append(f"{ad} – {{{{{k}}}}} – the {{{{{s}}}}}")
    inf = info or " ".join(regel(ad) for ad in adjs[:3])
    return luecke(frage, "\n".join(zeilen), abschnitt, extra=list(extra), info=inf)


def paare(adjs, abschnitt, frage, art="komp", info=None):
    f = komp if art == "komp" else sup_mit_the
    return zuordnen(frage, [(ad, f(ad)) for ad in adjs], abschnitt,
                    info=info or " ".join(regel(ad) for ad in adjs[:3]))


def aufgaben():
    a = []
    # ---------------------------------------------------------------- A: kurze Adjektive
    a.append(tabelle(["tall", "old", "small"], B_A, "Ergänze Komparativ und Superlativ.", extra=["more tall", "most small", "olderest"]))
    a.append(paare(["tall", "old", "small", "fast", "cheap"], B_A, "Ordne jedem Adjektiv seinen Komparativ zu."))
    a.append(paare(["young", "long", "short", "strong", "high"], B_A, "Ordne jedem Adjektiv seinen Superlativ zu.", art="sup"))
    a.append(komp_kurz("fast"))
    a.append(sup_kurz("cheap"))
    a.append(komp_mc("strong"))
    a.append(sup_mc("young"))
    a.append(tf("„Tom is more tall than Ben.“ ist richtig.", False, B_A,
                info="Tall ist ein kurzes Adjektiv. Es heißt taller (nicht more tall): Tom is taller than Ben."))
    a.append(mc("Wann steht vor der Steigerungsform the?", "Beim Superlativ (the tallest).", ["Beim Komparativ (the taller).", "Bei beiden Formen.", "Nie."], B_A,
                info="Nur der Superlativ hat the: the tallest, the oldest. Der Komparativ wird mit than verbunden: taller than."))

    # ---------------------------------------------------------------- B: Rechtschreibung
    a.append(tabelle(["nice", "large", "late"], B_B, "Ergänze Komparativ und Superlativ (Adjektive auf -e).", extra=["niceer", "the nicer"]))
    a.append(tabelle(["big", "thin", "hot"], B_B, "Ergänze Komparativ und Superlativ (der Konsonant wird verdoppelt).", extra=["biger", "the bigest"]))
    a.append(tabelle(["happy", "funny", "easy"], B_B, "Ergänze Komparativ und Superlativ (y wird zu i).", extra=["happyer", "the funnyest"]))
    a.append(paare(["nice", "wide", "safe", "brave"], B_B, "Ordne jedem Adjektiv auf -e seinen Komparativ zu."))
    a.append(paare(["big", "hot", "fat", "sad", "wet"], B_B, "Ordne jedem Adjektiv seinen Superlativ zu (doppelter Konsonant).", art="sup"))
    a.append(paare(["pretty", "heavy", "busy", "lucky", "noisy"], B_B, "Ordne jedem Adjektiv auf -y seinen Superlativ zu.", art="sup"))
    for ad in ("large", "thin", "happy"):
        a.append(komp_kurz(ad))
    a.append(sup_kurz("funny"))
    a.append(komp_mc("big"))
    a.append(sup_mc("nice"))
    a.append(tf("„The hotest day“ ist richtig geschrieben.", False, B_B,
                info="hot hat einen kurzen Vokal und einen Konsonanten am Ende: Das t wird verdoppelt: hotter, the hottest."))
    a.append(tf("„Mia is happier than Ben.“ ist richtig geschrieben.", True, B_B,
                info="happy endet auf Konsonant + y: Das y wird zu i: happier, the happiest."))

    # ---------------------------------------------------------------- C: lange Adjektive
    a.append(tabelle(["beautiful", "expensive", "interesting"], B_C, "Ergänze Komparativ und Superlativ (lange Adjektive).", extra=["beautifuler", "more good"]))
    a.append(paare(["beautiful", "difficult", "famous", "popular", "boring"], B_C, "Ordne jedem langen Adjektiv seinen Komparativ zu."))
    a.append(komp_kurz("intelligent"))
    a.append(sup_kurz("dangerous"))
    a.append(komp_mc("careful"))
    a.append(sup_mc("famous"))
    a.append(tf("„The most expensivest watch“ ist richtig.", False, B_C,
                info="Bei langen Adjektiven steigert man nur mit most: the most expensive. Nie most und -est zusammen."))
    a.append(mc("Welcher Satz ist richtig?", "This film is more interesting than that book.",
                ["This film is interestinger than that book.", "This film is more interestinger than that book.", "This film is most interesting than that book."], B_C,
                info="interesting ist ein langes Adjektiv: more interesting than. -er und more darf man nicht kombinieren, most steht nur beim Superlativ."))

    # ---------------------------------------------------------------- D: unregelmäßig
    a.append(tabelle(["good", "bad"], B_D, "Ergänze die unregelmäßigen Formen.", extra=["gooder", "badder", "the goodest"],
                     info="good → better → the best und bad → worse → the worst sind eigene Formen, die man lernen muss."))
    a.append(komp_kurz("good"))
    a.append(sup_kurz("bad"))
    a.append(mc("Welcher Satz ist richtig?", "My new bike is better than my old bike.",
                ["My new bike is gooder than my old bike.", "My new bike is more good than my old bike.", "My new bike is the better than my old bike."], B_D,
                info="Der Komparativ von good ist better. Vor dem Komparativ steht kein the."))
    a.append(tf("„This is the worst day of my life.“ ist richtig gesteigert.", True, B_D,
                info="Der Superlativ von bad ist the worst (nicht the baddest)."))
    a.append(zuordnen("Ordne die deutsche Bedeutung der englischen Form zu.",
                      [("besser", "better"), ("am besten", "the best"), ("schlechter", "worse"), ("am schlechtesten", "the worst")], B_D,
                      info="good – better – the best (gut, besser, am besten); bad – worse – the worst (schlecht, schlechter, am schlechtesten)."))

    # ---------------------------------------------------------------- E: welche Regel
    a.append(zuordnen("Ordne jedes Adjektiv der Regel zu.",
                      [("tall", "-er / -est"), ("nice", "nur -r / -st"), ("big", "Konsonant doppelt"), ("happy", "y wird i"), ("beautiful", "more / most")], B_E,
                      info="tall: einfach -er / -est. nice endet auf -e. big: kurzer Vokal, der Konsonant wird verdoppelt. happy: y wird zu i. beautiful: langes Adjektiv, more / most."))
    a.append(mc("Welches Adjektiv wird mit more / most gesteigert?", "difficult", ["cheap", "happy", "nice"], B_E,
                info="difficult hat drei Silben: more difficult, the most difficult. Die anderen steigert man mit -er / -est (cheaper, happier, nicer)."))
    a.append(mc("Welche Steigerung ist FALSCH?", "dangerous – dangerouser – the dangerousest",
                ["old – older – the oldest", "easy – easier – the easiest", "good – better – the best"], B_E,
                info="dangerous ist lang: more dangerous, the most dangerous. Die anderen drei Reihen sind richtig."))
    a.append(kurz("Welches Wort ist der Komparativ von „heavy“? Schreibe die Form.", ["heavier"], B_E, info=regel("heavy")))
    a.append(kurz("Schreibe den Superlativ von „thin“ (mit the).", ["the thinnest"], B_E, info=regel("thin")))
    a.append(kurz("Schreibe den Komparativ von „popular“.", ["more popular"], B_E, info=regel("popular")))
    a.append(luecke("Setze die richtige Form ein.",
                    "This is the {{best}} (good) cake of all.\nMy sister is {{taller}} (tall) than me.\nThat was the {{funniest}} (funny) film.\nA car is {{more expensive}} (expensive) than a bike.",
                    B_E, extra=["goodest", "more tall", "funnyest", "expensiver"],
                    info="good → the best, tall → taller, funny → the funniest (y wird i), expensive → more expensive."))
    a.append(tf("Bei jedem Adjektiv mit zwei Silben nimmt man more und most.", False, B_E,
                info="Zweisilbige Adjektive auf -y (happy, easy, funny) steigert man mit -ier / -iest. more und most nimmt man bei langen Adjektiven wie beautiful, interesting, expensive."))

    # ---------------------------------------------------------------- F: Tabellen und Texte
    a.append(luecke("Ergänze die Tabelle (Grundform, Komparativ, Superlativ).",
                    "wide – {{wider}} – the {{widest}}\nhot – {{hotter}} – the {{hottest}}\nfunny – {{funnier}} – the {{funniest}}\ngood – {{better}} – the {{best}}",
                    B_F, extra=["more wide", "hoter", "funnyer", "gooder"],
                    info="wide endet auf -e (nur -r / -st), hot verdoppelt das t, funny macht aus y ein i, good ist unregelmäßig."))
    a.append(luecke("Setze die Adjektive aus der Klammer in der richtigen Form ein (Komparativ oder Superlativ).",
                    "Ruby is {{older}} (old) than Max, but Tom is the {{oldest}} (old) of the three.\nThe red bag is {{cheaper}} (cheap) than the blue bag, but the green bag is the {{cheapest}} (cheap) of all.",
                    B_F, extra=["more old", "most cheap", "olderer"],
                    info="Der Komparativ (older, cheaper) vergleicht zwei Dinge. Der Superlativ (the oldest, the cheapest) steht für das Höchste unter mehreren."))
    a.append(reihenfolge("Bringe die Formen von „expensive“ in die richtige Reihenfolge (von der Grundform zum Superlativ).",
                         ["expensive", "more expensive", "the most expensive"], B_F,
                         info="Grundform → Komparativ (more expensive) → Superlativ (the most expensive)."))
    a.append(reihenfolge("Bringe die Formen von „busy“ in die richtige Reihenfolge (von der Grundform zum Superlativ).",
                         ["busy", "busier", "the busiest"], B_F,
                         info="busy endet auf Konsonant + y: Das y wird zu i: busier, the busiest."))
    return a


def build():
    p = pack(ID, "Englisch Teil 2f: Steigerung der Adjektive (1) – Formen",
             "Comparison of adjectives, Teil 1: Grundform, Komparativ und Superlativ bilden (-er / -est, Rechtschreibung bei e, doppeltem Konsonanten und y, more / most, good und bad). Mit Lernblatt und Übungsaufgaben.",
             lernblatt(), aufgaben(), min_aufgaben=34,
             hinweis="Alle Sätze und Namen sind selbst ausgedacht, nicht aus dem Schulbuch, dem Workbook oder den Arbeitsblättern. "
                     "Bei den Adjektiven mit zwei Silben (zum Beispiel clever) steigern Schulbücher manchmal unterschiedlich. Hier kommen nur eindeutige Beispiele vor.")
    return [nachlesen(p, {B_A: [L1, L2], B_B: L3, B_C: L4, B_D: L5, B_E: [L2, L3, L4, L5], B_F: [L2, L3, L4, L5]})]


if __name__ == "__main__":
    for p in build():
        print(p["id"], len(p["aufgaben"]), "Aufgaben")
