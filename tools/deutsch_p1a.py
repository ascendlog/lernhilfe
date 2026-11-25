"""Deutsch Klasse 6, Paket 1a: Nomen und ihre Begleiter (Checkliste Nominalisierung 1; DB S. 301, AH S. 82).

Alle Sätze, Texte und Namen sind erfunden (nichts aus Buch oder Heft). Lösungen laut Faktenblatt Abschnitt 1 und 13.
"""
from deutsch_lib import *

ID = "deutsch-1a-nomen-begleiter"

B_A = "A – Begleiter erkennen"
B_B = "B – Präposition und Artikel in einem Wort"
B_C = "C – Nomen ohne Begleiter: die Probe"
B_D = "D – Groß oder klein: einzelne Sätze"
B_E = "E – Kleine Texte"

L1 = "Nomen und ihre Begleiter"
L2 = "Präposition und Artikel verschmolzen"
L3 = "Nomen ohne Begleiter: die Probe"
L4 = "Groß oder klein bei Nomen?"


def lernblatt():
    return [
        lb(L1,
           "**Nomen** schreibt man **groß**. Nomen sind Namen für Menschen, Tiere, Pflanzen, Dinge und Gedachtes: der Junge, die Katze, der Baum, das Handy, die Freude.\n"
           "Vor einem Nomen steht oft ein Wort, das zu ihm gehört. Man nennt es **Begleiter** (Begleitwort). Daran erkennst du ein Nomen:\n"
           "- **Artikel**: der Hund, ein Hund, die Katze, das Spiel\n"
           "- **Adjektiv**: der kleine Hund, schöne Ferien\n"
           "- **Pronomen**: mein Hund, dieses Spiel, unsere Klasse, deine Idee\n"
           "- **Präposition**: mit Spaß, auf dem Dach, in einer Mannschaft\n"
           "- **Zahlwort**: elf Spieler, zwanzig Karten\n"
           "Es können auch **zwei Begleiter** vor einem Nomen stehen: das schnelle Auto, bei strahlendem Sonnenschein, in einer kleinen Stadt.",
           merke="Begleiter eines Nomens: Artikel, Adjektiv, Pronomen, Präposition, Zahlwort. Wo ein Begleiter steht, folgt ein groß geschriebenes Nomen."),
        lb(L2,
           "Oft sind Präposition und Artikel zu **einem Wort** verschmolzen:\n"
           "- in dem → **im**, bei dem → **beim**, zu dem → **zum**, zu der → **zur**, von dem → **vom**, an dem → **am**\n"
           "- an das → **ans**, auf das → **aufs**, in das → **ins**, für das → **fürs**\n"
           "Auch diese Wörter sind **Begleiter**. Danach steht ein Nomen: im Garten, beim Bäcker, zum Training, zur Schule, vom Dach, am Fenster, ins Bett.\n"
           "**Probe:** Kannst du das Wort in zwei Wörter zerlegen (in dem, zu der)? Dann ist es Präposition und Artikel in einem Wort.",
           merke="im = in dem, beim = bei dem, zum = zu dem, zur = zu der, vom = von dem, am = an dem. Danach folgt ein Nomen."),
        lb(L3,
           "Manchmal steht **kein Begleiter** vor dem Nomen: Wir haben Hunger. Sie braucht Zeit. Dann hilft die **Artikel-Adjektiv-Probe**: Setze einen **Artikel** und ein **Adjektiv** davor.\n"
           "- Hunger → der große Hunger\n"
           "- Zeit → die nötige Zeit\n"
           "- Hunde (Plural) → die großen Hunde\n"
           "Geht die Probe, ist das Wort ein **Nomen** und wird großgeschrieben. Bei Wörtern wie **gern**, **schnell**, **heute** oder **und** geht sie nicht: „das große gern“ ergibt keinen Sinn.\n"
           "Auch **Namen** (Mara, Hamburg, Rhein) schreibt man groß.",
           merke="Artikel-Adjektiv-Probe: Passt „der große …“ oder „die nötige …“ davor, ist es ein Nomen. Es wird großgeschrieben."),
        lb(L4,
           "Neben den Nomen schreibt man **groß**: den **Satzanfang** und **Namen**.\n"
           "**Klein** schreibt man Verben (spielen, schläft), Adjektive (schnell, klein) und die meisten kleinen Wörter (gern, heute, und, mit).\n"
           "So entscheidest du bei einem Wort:\n"
           "1. Steht ein **Begleiter** davor (Artikel, Adjektiv, Pronomen, Präposition, Zahlwort)? Dann **groß**.\n"
           "2. Steht keiner da? Dann mach die **Artikel-Adjektiv-Probe**. Geht sie, schreib **groß**.\n"
           "3. Geht sie nicht, schreib **klein**.",
           merke="Erst nach dem Begleiter suchen, dann die Probe machen. Erst dann entscheiden: groß oder klein."),
    ]


def aufgaben():
    a = []
    # ---------------------------------------------------------------- A
    a.append(zuordnen("Welche Art von Begleiter steht vor dem Nomen? Ordne zu.",
                      [("die Pizza", "Artikel"), ("leckere Pizza", "Adjektiv"), ("seine Pizza", "Pronomen"), ("mit Pizza", "Präposition")],
                      B_A, info="Artikel: der, die, das, ein, eine. Adjektiv: beschreibt das Nomen (lecker). Pronomen: mein, sein, dieser. Präposition: mit, auf, in, bei."))
    a.append(mc("Tim putzt im Garten sein Fahrrad. Welches Wort ist der Begleiter des Nomens „Fahrrad“?",
                "sein", ["putzt", "Tim", "im"], B_A,
                info="„sein“ steht direkt vor „Fahrrad“ und gehört dazu (Pronomen). „im“ begleitet „Garten“, „putzt“ ist ein Verb."))
    a.append(mc("Welche Art von Begleiter ist „dieses“ in „dieses Spiel“?",
                "Pronomen", ["Artikel", "Adjektiv", "Präposition"], B_A,
                info="Wörter wie dieses, mein, unser, ihre gehören zu den Pronomen. Sie stehen vor dem Nomen und begleiten es."))
    a.append(mc("Die kleine Mara trägt ihre rote Mütze zum Bäcker. Welche Wörter sind Begleiter von Nomen? (mehrere Antworten sind richtig)",
                ["Die", "kleine", "ihre", "rote", "zum"], ["trägt"], B_A,
                info="Begleiter sind: Die (Artikel), kleine (Adjektiv), ihre (Pronomen), rote (Adjektiv), zum (= zu dem, Präposition und Artikel). „trägt“ ist ein Verb und kein Begleiter."))
    a.append(tf("Ein Begleiter steht meistens vor dem Nomen.", True, B_A,
                info="Begleiter stehen direkt vor dem Nomen oder vor einem weiteren Begleiter: der alte Baum."))
    a.append(tf("In dem Satz „Wir spielen Fußball.“ hat „Fußball“ keinen Begleiter und ist trotzdem ein Nomen.", True, B_A,
                info="Es steht kein Begleiter davor. Mit der Probe merkst du es aber: der spannende Fußball. Also schreibt man „Fußball“ groß."))
    a.append(zuordnen("Welche Art von Begleiter ist das Wort?",
                      [("der", "Artikel"), ("schöne", "Adjektiv"), ("mein", "Pronomen"), ("auf", "Präposition"), ("zwei", "Zahlwort")],
                      B_A, info="der = Artikel, schöne = Adjektiv, mein = Pronomen, auf = Präposition, zwei = Zahlwort."))
    a.append(mc("Welche Wortgruppe enthält zwei Begleiter?",
                "das schnelle Auto", ["schnelle Autos", "das Auto", "Auto fahren"], B_A,
                info="„das“ (Artikel) und „schnelle“ (Adjektiv) stehen vor „Auto“. Bei „schnelle Autos“ und „das Auto“ ist es nur ein Begleiter."))
    a.append(kurz("Im Garten blüht die Rose. Schreibe den Artikel auf, der zu „Rose“ gehört.", "die", B_A,
                  info="Der Artikel steht direkt vor dem Nomen: die Rose. „Im“ gehört zu „Garten“."))
    a.append(mc("In „zwölf Schüler“ ist „zwölf“ ein …", "Zahlwort", ["Artikel", "Pronomen", "Verb"], B_A,
                info="Zahlwörter wie zwölf, zwanzig oder drei können Nomen begleiten. Danach steht ein groß geschriebenes Nomen."))

    # ---------------------------------------------------------------- B
    a.append(zuordnen("Aus welchen zwei Wörtern besteht das verschmolzene Wort?",
                      [("im", "in dem"), ("beim", "bei dem"), ("zum", "zu dem"), ("zur", "zu der"), ("vom", "von dem")],
                      B_B, info="im = in dem, beim = bei dem, zum = zu dem, zur = zu der, vom = von dem. Präposition und Artikel sind zusammengezogen."))
    a.append(zuordnen("Schreibe die lange Form dazu.",
                      [("ans", "an das"), ("aufs", "auf das"), ("ins", "in das"), ("fürs", "für das"), ("am", "an dem")],
                      B_B, info="ans = an das, aufs = auf das, ins = in das, fürs = für das, am = an dem."))
    a.append(mc("Wir gehen zum Schwimmbad. Welches Wort ist Präposition und Artikel in einem Wort?",
                "zum", ["gehen", "Wir", "Schwimmbad"], B_B,
                info="„zum“ ist zu dem. Danach steht das Nomen „Schwimmbad“."))
    a.append(luecke("Setze die verschmolzene Form ein.",
                    "Die Katze sitzt {{am}} Fenster. Ole spielt {{im}} Garten. Mia geht {{ins}} Bett.", B_B,
                    extra=["beim", "zum", "vom"], info="am = an dem Fenster, im = in dem Garten, ins = in das Bett.",
                tauschbar=[("am", "im")]))
    a.append(luecke("Setze die verschmolzene Form ein.",
                    "Tom geht {{zum}} Training. Seine Mutter holt ihn {{vom}} Sportplatz ab. Sie fahren dann {{zur}} Oma.", B_B,
                    extra=["beim", "im", "ins"], info="zum Training = zu dem Training, vom Sportplatz = von dem Sportplatz, zur Oma = zu der Oma."))
    a.append(luecke("Setze die verschmolzene Form ein.",
                    "Pia hilft {{beim}} Kochen. Dann schreibt sie {{fürs}} Wochenende eine Liste. Danach geht sie {{ans}} Telefon.", B_B,
                    extra=["zum", "am", "vom"], info="beim = bei dem, fürs = für das, ans = an das Telefon."))
    a.append(tf("„im“ ist ein Begleiter, weil es für „in dem“ steht.", True, B_B,
                info="Präposition (in) und Artikel (dem) sind zu „im“ verschmolzen. Das Wort begleitet ein Nomen: im Haus."))
    a.append(mc("Welcher Satz ist richtig geschrieben?",
                "Mara wohnt im dritten Stock.", ["Mara wohnt im dritten stock.", "Mara wohnt Im dritten Stock.", "mara wohnt im dritten Stock."], B_B,
                info="„im“ und „dritten“ sind Begleiter, deshalb schreibt man „Stock“ groß. „im“ bleibt mitten im Satz klein. „Mara“ ist ein Name und steht am Satzanfang."))
    a.append(gk("Beim [Frühstück|Begleiter „beim“ (bei dem) steht davor] liest Papa die [Zeitung|Artikel „die“ steht davor] und trinkt [Kaffee|Nomen ohne Begleiter, Probe: der starke Kaffee].",
                B_B, tipp="Suche zuerst die Begleiter. Beim Wort ohne Begleiter hilft die Artikel-Adjektiv-Probe."))

    # ---------------------------------------------------------------- C
    a.append(tf("„Mut“ ist ein Nomen, denn man kann sagen: der große Mut.", True, B_C,
                info="Die Artikel-Adjektiv-Probe geht (der große Mut). Also ist „Mut“ ein Nomen und wird großgeschrieben."))
    a.append(tf("„gern“ ist ein Nomen, denn man kann sagen: das große gern.", False, B_C,
                info="Die Probe geht nicht: „das große gern“ ergibt keinen Sinn. „gern“ ist ein Wort, das man kleinschreibt."))
    a.append(zuordnen("Nomen oder kein Nomen? Mach die Artikel-Adjektiv-Probe.",
                      [("Freude", "Nomen"), ("schnell", "kein Nomen"), ("Zeit", "Nomen"), ("heute", "kein Nomen"), ("Ruhe", "Nomen"), ("und", "kein Nomen")],
                      B_C, info="Freude (die große Freude), Zeit (die nötige Zeit) und Ruhe (die tiefe Ruhe) bestehen die Probe. Bei schnell, heute und und geht sie nicht."))
    a.append(mc("Der Hund hat Durst. Welches Wort ist ein Nomen ohne Begleiter?",
                "Durst", ["Der", "Hund", "hat"], B_C,
                info="„Hund“ hat den Begleiter „Der“. Bei „Durst“ steht kein Begleiter, aber die Probe geht: der große Durst."))
    a.append(mc("In welchem Satz steht ein Nomen ohne Begleiter?",
                "Hunde bellen.", ["Der Hund bellt.", "Mein Hund bellt.", "Ein Hund bellt."], B_C,
                info="„Hunde“ hat keinen Begleiter, es ist aber ein Nomen (die lauten Hunde). In den anderen Sätzen stehen der, mein oder ein davor."))
    a.append(zuordnen("Welcher Artikel passt bei der Probe? (der, die oder das)",
                      [("Hilfe", "die"), ("Spaß", "der"), ("Wetter", "das"), ("Ruhe", "die"), ("Mut", "der")],
                      B_C, info="Die Artikel-Probe zeigt, dass es Nomen sind: die Hilfe, der Spaß, das Wetter, die Ruhe, der Mut."))
    a.append(gk("Ich habe [Hunger|Nomen ohne Begleiter, Probe: der große Hunger] und [Durst|Nomen ohne Begleiter, Probe: der große Durst], deshalb esse ich [schnell|Adjektiv oder Adverb, die Probe geht nicht].",
                B_C, tauschbar=[("Hunger", "Durst")]))
    a.append(gk("Wir brauchen [Zeit|Nomen ohne Begleiter, Probe: die nötige Zeit] und [Geduld|Nomen ohne Begleiter, Probe: die nötige Geduld], dann klappt es [bestimmt|Adverb, die Probe geht nicht].",
                B_C, tauschbar=[("Zeit", "Geduld")]))
    a.append(mc("Wie lautet die Artikel-Adjektiv-Probe bei „Angst“?",
                "die große Angst", ["groß die Angst", "die große angst", "das große angst"], B_C,
                info="Man setzt einen Artikel und ein Adjektiv vor das Wort: die große Angst. Das Nomen bleibt groß geschrieben."))

    # ---------------------------------------------------------------- D
    a.append(gk("Im [Keller|Begleiter „im“ (in dem)] steht ein [Regal|Artikel „ein“] mit alten [Gläsern|Adjektiv „alten“ steht davor].", B_D))
    a.append(gk("Meine [Schwester|Pronomen „meine“] spielt am [Nachmittag|Begleiter „am“ (an dem)] mit dem [Hund|Artikel „dem“] im [Park|Begleiter „im“].", B_D))
    a.append(gk("Der [Lehrer|Artikel „der“] erklärt den [Kindern|Artikel „den“] die [Aufgabe|Artikel „die“] sehr [genau|Adverb, kein Nomen: die Probe geht nicht].", B_D))
    a.append(gk("Zum [Geburtstag|Begleiter „zum“ (zu dem)] bekommt Ole ein neues [Fahrrad|Artikel „ein“ und Adjektiv „neues“ stehen davor] und zwei [Karten|Zahlwort „zwei“ steht davor].", B_D))
    a.append(gk("Die [Katze|Artikel „die“] schläft [gern|Adverb, kein Nomen] auf dem warmen [Sofa|Artikel „dem“ und Adjektiv „warmen“ stehen davor].", B_D))
    a.append(gk("Bei starkem [Regen|Adjektiv „starkem“ steht davor] bleiben wir [lieber|Adverb, kein Nomen] im [Haus|Begleiter „im“] und spielen ein [Spiel|Artikel „ein“].", B_D))
    a.append(gk("In der [Pause|Artikel „der“] essen wir [Brötchen|Nomen ohne Begleiter, Probe: die leckeren Brötchen] und trinken [Saft|Nomen ohne Begleiter, Probe: der kalte Saft].", B_D))
    a.append(gk("Unser [Nachbar|Pronomen „unser“] hat einen [Garten|Artikel „einen“] mit bunten [Blumen|Adjektiv „bunten“ steht davor].", B_D))
    a.append(gk("Mit [Freude|Präposition „mit“ steht davor] helfen die [Schüler|Artikel „die“] ihrer [Lehrerin|Pronomen „ihrer“] im [Klassenzimmer|Begleiter „im“].", B_D))
    a.append(gk("Ich lese [gern|Adverb, kein Nomen] ein [Buch|Artikel „ein“] über [Piraten|Präposition „über“ steht davor] und große [Schiffe|Adjektiv „große“ steht davor].", B_D,
                tauschbar=[("Piraten", "Schiffe")]))

    # ---------------------------------------------------------------- E (kleine Texte)
    a.append(gk("Am [Morgen|Begleiter „am“ (an dem)] packt [Mia|Name einer Person] ihren [Rucksack|Pronomen „ihren“]. Sie legt eine [Flasche|Artikel „eine“] mit [Wasser|Präposition „mit“] und zwei [Äpfel|Zahlwort „zwei“] hinein. Dann geht sie zum [Bahnhof|Begleiter „zum“ (zu dem)].",
                B_E, frage="Groß oder klein? Ziehe in jede Lücke das Wort in der richtigen Schreibweise (Text: Der Ausflug)."))
    a.append(gk("Im [Zoo|Begleiter „im“ (in dem)] sehen die [Kinder|Artikel „die“] einen [Löwen|Artikel „einen“]. Er liegt [faul|Adjektiv, kein Nomen] auf einem großen [Felsen|Artikel „einem“ und Adjektiv „großen“ stehen davor]. Ein [Wärter|Artikel „ein“] bringt [Fleisch|Nomen ohne Begleiter, Probe: das frische Fleisch].",
                B_E, frage="Groß oder klein? Ziehe in jede Lücke das Wort in der richtigen Schreibweise (Text: Im Zoo)."))
    a.append(gk("Bei schönem [Wetter|Adjektiv „schönem“ steht davor] fahren wir mit dem [Rad|Artikel „dem“ steht davor] zum [See|Begleiter „zum“ (zu dem)]. Unterwegs machen wir eine [Pause|Artikel „eine“] und essen [Brot|Nomen ohne Begleiter, Probe: das frische Brot] mit [Käse|Präposition „mit“ steht davor].",
                B_E, frage="Groß oder klein? Ziehe in jede Lücke das Wort in der richtigen Schreibweise (Text: Die Radtour).",
                tauschbar=[("Brot", "Käse")]))
    a.append(gk("Ole [kauft|Verb, kein Nomen] auf dem [Flohmarkt|Artikel „dem“ steht davor] ein altes [Buch|Artikel „ein“ und Adjektiv „altes“ stehen davor] und eine [Mütze|Artikel „eine“]. Die [Verkäuferin|Artikel „die“] gibt ihm einen [Beutel|Artikel „einen“] dazu. Seine [Schwester|Pronomen „seine“] freut sich über die [Überraschung|Artikel „die“ steht davor].",
                B_E, frage="Groß oder klein? Ziehe in jede Lücke das Wort in der richtigen Schreibweise (Text: Auf dem Flohmarkt)."))
    a.append(gk("Am [Abend|Begleiter „am“ (an dem)] schauen wir einen [Film|Artikel „einen“ steht davor] im [Wohnzimmer|Begleiter „im“ (in dem)]. Mama bringt [Popcorn|Nomen ohne Begleiter, Probe: das süße Popcorn] und [Saft|Nomen ohne Begleiter, Probe: der kalte Saft]. Wir [lachen|Verb, kein Nomen] [laut|Adjektiv oder Adverb, kein Nomen] über die [Szenen|Artikel „die“ steht davor].",
                B_E, frage="Groß oder klein? Ziehe in jede Lücke das Wort in der richtigen Schreibweise (Text: Der Filmabend).",
                tauschbar=[("Popcorn", "Saft")]))
    a.append(gk("Der [Bäcker|Artikel „der“] steht schon früh am [Morgen|Begleiter „am“ (an dem)] in seiner [Backstube|Pronomen „seiner“ steht davor]. Er [knetet|Verb, kein Nomen] den [Teig|Artikel „den“ steht davor] und schiebt die [Brote|Artikel „die“ steht davor] in den [Ofen|Artikel „den“ steht davor]. Der [Duft|Artikel „der“ steht davor] zieht durch die [Straße|Artikel „die“ steht davor].",
                B_E, frage="Groß oder klein? Ziehe in jede Lücke das Wort in der richtigen Schreibweise (Text: In der Backstube)."))
    a.append(gk("Im [Herbst|Begleiter „im“ (in dem)] fallen die [Blätter|Artikel „die“ steht davor] von den [Bäumen|Artikel „den“ steht davor]. Die [Kinder|Artikel „die“ steht davor] sammeln [Kastanien|Nomen ohne Begleiter, Probe: die braunen Kastanien] und basteln [Figuren|Nomen ohne Begleiter, Probe: die lustigen Figuren] daraus. Das [macht|Verb, kein Nomen] großen [Spaß|Adjektiv „großen“ steht davor].",
                B_E, frage="Groß oder klein? Ziehe in jede Lücke das Wort in der richtigen Schreibweise (Text: Im Herbst)."))
    a.append(gk("Mit meiner [Klasse|Pronomen „meiner“ steht davor] fahre ich im [Sommer|Begleiter „im“ (in dem)] ins [Landschulheim|Begleiter „ins“ (in das)]. Wir wandern durch den [Wald|Artikel „den“ steht davor], bauen eine [Hütte|Artikel „eine“ steht davor] und kochen am [Feuer|Begleiter „am“ (an dem)] unser [Essen|Pronomen „unser“ steht davor].",
                B_E, frage="Groß oder klein? Ziehe in jede Lücke das Wort in der richtigen Schreibweise (Text: Das Landschulheim)."))
    return a


def build():
    p = pack(ID, "Deutsch Teil 1a: Nomen und ihre Begleiter",
             "Begleitwörter von Nomen (Artikel, Adjektiv, Pronomen, Präposition mit Artikel, Zahlwort), verschmolzene Präpositionen (im, beim, zum …), Nomen ohne Begleiter mit der Artikel-Adjektiv-Probe, Groß- und Kleinschreibung. Mit Lernblatt und Übungsaufgaben.",
             lernblatt(), aufgaben(), min_aufgaben=40,
             hinweis="Alle Sätze, Texte und Namen sind selbst ausgedacht, nicht aus dem Deutschbuch oder Aufgabenheft. Die Regeln stehen so auch im Deutschbuch (S. 301) und im Aufgabenheft (S. 82). Bei den Groß-/Kleinschreibungs-Lücken zählt jeder Buchstabe: Tippe das Wort so, wie es im Satz stehen muss.")
    return [nachlesen(p, {B_A: L1, B_B: L2, B_C: L3, B_D: [L1, L4], B_E: [L1, L3, L4]})]


if __name__ == "__main__":
    for p in build():
        print(p["id"], len(p["aufgaben"]), "Aufgaben")
