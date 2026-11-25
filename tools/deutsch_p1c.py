"""Deutsch Klasse 6, Paket 1c: Nominalisierte Adjektive, Indefinitpronomen und Superlativ (Checkliste Nominalisierung 2–4; DB S. 302–304, Nominalisierungsheft S. 59, AH S. 83–85).

Alle Sätze, Texte und Namen sind erfunden. Lösungen laut Faktenblatt Abschnitt 3, 4 und 13.
"""
from deutsch_lib import *

ID = "deutsch-1c-nominalisierte-adjektive-superlativ"

B_A = "A – Adjektiv oder nominalisiert?"
B_B = "B – Begleiter nominalisierter Adjektive"
B_C = "C – Indefinitpronomen"
B_D = "D – Superlativ: am … oder das …ste?"
B_E = "E – Fallen: Adjektiv vor dem Nomen"
B_F = "F – Gemischte Texte"

L1 = "Adjektive als Nomen"
L2 = "Begleiter nominalisierter Adjektive"
L3 = "Indefinitpronomen"
L4 = "Superlativ mit „am“ oder nominalisiert?"
L5 = "Fallen: Adjektiv, Nomen oder Verb?"


def lernblatt():
    return [
        lb(L1,
           "**Adjektive** (Eigenschaftswörter) schreibt man **klein**. Man erkennt sie an Endungen wie **-ig, -isch, -lich, -sam, -bar** (eifrig, diebisch, wirklich, wirksam, lesbar) und daran, dass man die meisten **steigern** kann: schön – schöner – am schönsten.\n"
           "Wird ein Adjektiv **wie ein Nomen** gebraucht, ist es **nominalisiert** und wird **großgeschrieben**:\n"
           "- Das Wetter ist **schön**. (Adjektiv, klein)\n"
           "- Das **Schöne** an dem Tag war die Ruhe. (nominalisiert, groß)\n"
           "Weitere Beispiele: das Neue, im Dunkeln, aufs Neue, im Allgemeinen, für Junge und Alte.",
           merke="Wird ein Adjektiv als Nomen gebraucht, schreibt man es groß: das Neue, im Dunkeln."),
        lb(L2,
           "Nominalisierte Adjektive erkennst du an ihren **Begleitern**. Das sind:\n"
           "- **Artikel**: das Neue, der Verdächtige, das Schöne\n"
           "- **Präposition** (oft mit Artikel verschmolzen): im Dunkeln, im Allgemeinen, im Besonderen, aufs Neue, im Geringsten, für Junge und Alte\n"
           "- **Indefinitpronomen**: etwas Schönes, nichts Neues, alles Gute\n"
           "Mit der **Artikelprobe** prüfst du es: Kannst du einen Artikel davorsetzen (oder steht schon einer da)? Dann ist es nominalisiert. Ein häufiger Begleiter ist die Präposition **im**: im Dunkeln, im Besonderen.",
           merke="Artikel, Präposition (im, aufs, für …) und Indefinitpronomen (etwas, nichts, alles …) sind die Begleiter nominalisierter Adjektive."),
        lb(L3,
           "**Indefinitpronomen** (unbestimmte Fürwörter) geben eine **ungefähre Menge oder Anzahl** an:\n"
           "**etwas, manches, alles, nichts, einige(s), kein, viel, (ein) paar, wenig, allerlei, mancherlei, genug**\n"
           "Sie begleiten oft ein **nominalisiertes Adjektiv**: etwas Schönes, alles Gute, viel Schönes, nichts Neues, manches Kleine, einiges Traurige, allerlei Leckeres, etwas Erfreuliches.\n"
           "Die Wortart von „nichts“, „etwas“ und „alles“ heißt **Indefinitpronomen**. Das Indefinitpronomen selbst schreibt man **klein**.\n"
           "Das Adjektiv danach endet oft auf **-es** (etwas Schönes), nach „alles“ oft auf **-e** (alles Gute).",
           merke="Indefinitpronomen (etwas, nichts, alles, viel …) + Adjektiv = nominalisiertes Adjektiv, groß: etwas Schönes, nichts Neues."),
        lb(L4,
           "Superlative mit „am“ und nominalisierte Adjektive sehen ähnlich aus, werden aber verschieden geschrieben:\n"
           "- **am schönsten, am spannendsten, am mutigsten** (Superlativ mit „am“) → **klein**. „am“ gehört zum Superlativ und ist hier kein Begleiter.\n"
           "- **das Schönste, das Spannendste, das Mutigste** (nominalisiert) → **groß**. Davor steht ein Artikel.\n"
           "**Proben:** Wie war es? → am spannendsten (klein). Was war es? → das Spannendste (groß). Auch mit Zusatz davor schreibt man groß: mit Abstand das Gruseligste.",
           merke="Frage „Wie?“ → am …sten, klein. Frage „Was?“ → das …ste, groß."),
        lb(L5,
           "Diese Fälle sind knifflig:\n"
           "- Ein **Adjektiv vor einem Nomen** bleibt **klein**: ein furchtloser Held, die blinden Fußballer, einige schräge Töne, ein paar weiße Socken. Nach einem Indefinitpronomen schreibt man klein, wenn danach noch ein Nomen folgt.\n"
           "- Ein Adjektiv, das etwas über das **Verb** oder das **Subjekt** sagt, bleibt **klein**: Er singt **laut**. Das Zimmer ist **dunkel**.\n"
           "- **Endungen** nicht vergessen: ein berühmtes Lied, die coolen Songtexte, berühmte Sänger.\n"
           "- Manche Wörter sehen aus wie Verben oder Adjektive, sind aber **Nomen**: mit Hilfe, im Flug, in Not.",
           merke="Folgt ein Nomen, bleibt das Adjektiv klein. Nominalisiert (groß) ist es nur, wenn es selbst wie ein Nomen gebraucht wird."),
    ]


def aufgaben():
    a = []
    # ---------------------------------------------------------------- A
    a.append(zuordnen("Adjektiv oder nominalisiertes Adjektiv? Ordne zu.",
                      [("Das Neue gefällt mir.", "nominalisiert (groß)"), ("Das neue Fahrrad gefällt mir.", "Adjektiv (klein)"),
                       ("Im Dunkeln fürchte ich mich.", "nominalisiert (groß)"), ("Das Zimmer ist dunkel.", "Adjektiv (klein)"),
                       ("Er wünscht sich etwas Besonderes.", "nominalisiert (groß)"), ("Das Geschenk ist besonders schön.", "Adjektiv (klein)")],
                      B_A, info="Nominalisiert ist ein Adjektiv, wenn ein Begleiter davorsteht und kein Nomen folgt: das Neue, im Dunkeln, etwas Besonderes. Sonst bleibt es klein."))
    a.append(mc("In welchem Satz wird „schön“ wie ein Nomen gebraucht?",
                "Das Schöne an dem Tag war die Ruhe.",
                ["Der Tag war schön.", "Wir hatten schönes Wetter.", "Es war ein schöner Tag."], B_A,
                info="Nur im ersten Satz steht der Artikel „Das“ vor „Schöne“ und es folgt kein Nomen direkt dahinter. In den anderen Sätzen ist „schön“ ein Adjektiv."))
    a.append(tf("Wird ein Adjektiv wie ein Nomen gebraucht, schreibt man es groß.", True, B_A,
                info="Das nennt man Nominalisierung: das Neue, im Dunkeln, etwas Schönes."))
    a.append(tf("„Das Beste“ ist ein nominalisiertes Adjektiv.", True, B_A,
                info="Vor „Beste“ steht der Artikel „Das“. Es ist von „gut“ abgeleitet (gut – besser – am besten) und wird großgeschrieben."))
    a.append(kurz("Setze „besonders“ passend ein: Sie wünscht sich etwas … zum Geburtstag.", "Besonderes", B_A, gross=True,
                  info="Nach dem Indefinitpronomen „etwas“ wird das Adjektiv nominalisiert und großgeschrieben: etwas Besonderes."))
    a.append(mc("Welche Schreibweise ist richtig?",
                "im Allgemeinen", ["im allgemeinen", "Im allgemeinen", "im ALLGEMEINEN"], B_A,
                info="„im“ (= in dem) ist ein Begleiter, deshalb wird „Allgemeinen“ nominalisiert und großgeschrieben."))
    a.append(zuordnen("Schreibe das nominalisierte Adjektiv mit „das“.",
                      [("gut", "das Gute"), ("schön", "das Schöne"), ("neu", "das Neue"), ("lustig", "das Lustige"), ("wichtig", "das Wichtige")],
                      B_A, info="Artikel „das“ + Adjektiv mit Endung -e, großgeschrieben: das Gute, das Schöne, das Neue, das Lustige, das Wichtige."))
    a.append(mc("Ich wünsche dir alles Gute zum Geburtstag! Welches Wort ist das nominalisierte Adjektiv?",
                "Gute", ["wünsche", "alles", "Geburtstag"], B_A,
                info="„alles“ ist das Indefinitpronomen und der Begleiter, „Gute“ ist das nominalisierte Adjektiv (gut). „Geburtstag“ ist ein Nomen, „wünsche“ ein Verb."))
    a.append(gk("Das [Geheimnisvolle|Artikel „Das“ steht davor] und das [Spannende|Artikel „das“ steht davor] mag ich [gern|Adverb, kein Nomen].", B_A,
                tauschbar=[("Geheimnisvolle", "Spannende")]))

    # ---------------------------------------------------------------- B
    a.append(zuordnen("Welcher Begleiter steht vor dem nominalisierten Adjektiv?",
                      [("das Schöne", "Artikel"), ("im Dunkeln", "Präposition (mit Artikel)"), ("nichts Neues", "Indefinitpronomen"), ("für Junge und Alte", "Präposition")],
                      B_B, info="das = Artikel, im = in dem (Präposition mit Artikel), nichts = Indefinitpronomen, für = Präposition."))
    a.append(luecke("Setze die verschmolzene Form ein.",
                    "Ich bin {{im}} Großen und Ganzen zufrieden. Sie probiert es {{aufs}} Neue. Er wartet {{im}} Stillen.", B_B,
                    extra=["zum", "am", "ins"], info="im = in dem, aufs = auf das. Danach stehen nominalisierte Adjektive: im Großen, aufs Neue, im Stillen."))
    a.append(mc("Welcher Satz ist richtig geschrieben?",
                "Im Dunkeln leuchtet die Lampe.", ["Im dunkeln leuchtet die Lampe.", "im Dunkeln leuchtet die Lampe.", "Im Dunkeln Leuchtet die Lampe."], B_B,
                info="„Im“ steht am Satzanfang. „Dunkeln“ ist nominalisiert (Begleiter „Im“). „leuchtet“ ist ein Verb und bleibt klein."))
    a.append(tf("Nach „im“ kann ein nominalisiertes Adjektiv stehen: im Besonderen.", True, B_B,
                info="Ein häufiger Begleiter nominalisierter Adjektive ist die Präposition „im“: im Allgemeinen, im Besonderen, im Dunkeln."))
    a.append(mc("Welche Wörter sind Begleiter nominalisierter Adjektive? (mehrere Antworten sind richtig)",
                ["das", "etwas", "im", "nichts"], ["schnell", "sie"], B_B,
                info="Artikel (das), Indefinitpronomen (etwas, nichts) und Präposition mit Artikel (im) begleiten nominalisierte Adjektive. „schnell“ ist ein Adjektiv, „sie“ ein Personalpronomen."))
    a.append(kurz("Schreibe „schön“ nominalisiert mit „etwas“.", ["etwas Schönes", "Etwas Schönes"], B_B, gross=True,
                  info="Nach „etwas“ wird das Adjektiv großgeschrieben, die Endung ist -es: etwas Schönes."))
    a.append(kurz("Schreibe „neu“ nominalisiert mit „nichts“.", ["nichts Neues", "Nichts Neues"], B_B, gross=True,
                  info="Nach „nichts“ wird das Adjektiv großgeschrieben: nichts Neues."))
    a.append(kurz("Schreibe „gut“ nominalisiert mit „alles“.", ["alles Gute", "Alles Gute"], B_B, gross=True,
                  info="Nach „alles“ endet das Adjektiv meist auf -e: alles Gute."))

    # ---------------------------------------------------------------- C
    a.append(mc("Welches Wort ist ein Indefinitpronomen?", "nichts", ["dein", "der", "schnell"], B_C,
                info="Indefinitpronomen geben eine ungefähre Menge an: etwas, nichts, alles, viel, manches … „dein“ ist ein Possessivpronomen, „der“ ein Artikel, „schnell“ ein Adjektiv."))
    a.append(mc("Welche Wörter sind Indefinitpronomen? (mehrere Antworten sind richtig)",
                ["etwas", "alles", "nichts", "viel"], ["mein", "das"], B_C,
                info="etwas, alles, nichts und viel sind Indefinitpronomen. „mein“ ist ein Possessivpronomen und „das“ ein Artikel."))
    a.append(tf("„nichts“, „etwas“ und „alles“ gehören zur Wortart Indefinitpronomen.", True, B_C,
                info="Sie geben eine ungefähre Menge an und begleiten häufig nominalisierte Adjektive."))
    a.append(tf("Ein Indefinitpronomen nennt immer eine genaue Zahl.", False, B_C,
                info="Indefinitpronomen geben eine ungefähre Menge oder Anzahl an, zum Beispiel etwas, einige, manches, viel."))
    a.append(luecke("Setze das Adjektiv in Klammern nominalisiert ein. Achte auf die Großschreibung.",
                    "Zum Fest gibt es etwas {{Leckeres}}. Ich wünsche dir alles {{Gute}}. Wir haben nichts {{Neues}} gehört.", B_C,
                    extra=["leckeres", "gute", "neues"], gross=True,
                    info="Nach etwas, alles und nichts wird das Adjektiv nominalisiert und großgeschrieben: etwas Leckeres, alles Gute, nichts Neues."))
    a.append(gk("Im Laden gab es [allerlei|Indefinitpronomen, kein Nomen] [Leckeres|Indefinitpronomen „allerlei“ steht davor].", B_C))
    a.append(gk("Zum Geburtstag wünsche ich dir [viel|Indefinitpronomen, kein Nomen] [Schönes|Indefinitpronomen „viel“ steht davor].", B_C))
    a.append(gk("Er erzählte [manches|Indefinitpronomen, kein Nomen] [Lustige|Indefinitpronomen „manches“ steht davor], aber [nichts|Indefinitpronomen, kein Nomen] [Wichtiges|Indefinitpronomen „nichts“ steht davor].", B_C))
    a.append(gk("Sie hat [einiges|Indefinitpronomen, kein Nomen] [Neue|Indefinitpronomen „einiges“ steht davor] gelernt und [wenig|Indefinitpronomen, kein Nomen] [Schwieriges|Indefinitpronomen „wenig“ steht davor] gefunden.", B_C))
    a.append(gk("Beim Spielen gab es [etwas|Indefinitpronomen, kein Nomen] [Besonderes|Indefinitpronomen „etwas“ steht davor] und [nichts|Indefinitpronomen, kein Nomen] [Langweiliges|Indefinitpronomen „nichts“ steht davor].", B_C,
                tauschbar=[("etwas", "nichts"), ("Besonderes", "Langweiliges")]))

    # ---------------------------------------------------------------- D
    a.append(tf("Adjektive im Superlativ mit „am“ schreibt man klein: am schönsten.", True, B_D,
                info="„am“ gehört hier zum Superlativ und ist kein Begleiter. Die Frage lautet „Wie?“."))
    a.append(tf("Nominalisierte Adjektive wie „das Schönste“ schreibt man klein.", False, B_D,
                info="Vor „Schönste“ steht der Artikel „das“. Das Adjektiv wird wie ein Nomen gebraucht und großgeschrieben."))
    a.append(mc("Welche Frage passt zu „am spannendsten“?", "Wie?", ["Was?", "Wer?", "Wann?"], B_D,
                info="Wie war es? – Am spannendsten. Bei der Frage „Was?“ würde man „das Spannendste“ schreiben."))
    a.append(zuordnen("Welche Probefrage passt zu der Wortgruppe?",
                      [("am spannendsten", "Wie?"), ("das Spannendste", "Was?"), ("am lautesten", "Wie?"), ("das Lauteste", "Was?")],
                      B_D, info="am …sten antwortet auf „Wie?“ (klein). das …ste antwortet auf „Was?“ (groß)."))
    a.append(mc("Welcher Satz ist richtig geschrieben?",
                "Am schönsten war der Strand.",
                ["Am Schönsten war der Strand.", "Das schönste war der Strand.", "am schönsten war der Strand."], B_D,
                info="Wie war es? – Am schönsten. „am“ steht am Satzanfang groß, „schönsten“ bleibt klein. Bei „Das Schönste war der Strand“ wäre es nominalisiert."))
    a.append(gk("[Am|Satzanfang] [lautesten|Superlativ mit „am“ (Frage: Wie?)] war der Löwe. Das [Lauteste|Artikel „Das“ steht davor (Frage: Was?)] im ganzen Zoo war sein Gebrüll.", B_D))
    a.append(gk("Mia findet die Rutsche am [aufregendsten|Superlativ mit „am“ (Frage: Wie?)]. Für Ole ist das [Aufregendste|Artikel „das“ steht davor (Frage: Was?)] der Sprung ins Wasser.", B_D))
    a.append(gk("Im Winter ist es am [kältesten|Superlativ mit „am“ (Frage: Wie?)]. Das [Kälteste|Artikel „Das“ steht davor (Frage: Was?)] ist der Wind am Morgen.", B_D))
    a.append(gk("Was war bei dem Spiel am [schwierigsten|Superlativ mit „am“ (Frage: Wie?)]? Das [Schwierigste|Artikel „Das“ steht davor (Frage: Was?)] war, leise zu bleiben.", B_D))
    a.append(gk("[Am|Satzanfang] [liebsten|Superlativ mit „am“ (Frage: Wie?)] esse ich Pizza. Das [Beste|Artikel „Das“ steht davor (Frage: Was?)] daran ist der Käse.", B_D))

    # ---------------------------------------------------------------- E
    a.append(tf("Ein Adjektiv vor einem Nomen schreibt man klein: ein furchtloser Held.", True, B_E,
                info="Hier ist „furchtloser“ ein Adjektiv, das „Held“ beschreibt. Es wird nicht wie ein Nomen gebraucht."))
    a.append(mc("Welcher Satz ist richtig geschrieben?",
                "Die mutigen Kinder bauen eine große Hütte.",
                ["Die Mutigen Kinder bauen eine große Hütte.", "Die mutigen Kinder bauen eine Große Hütte.", "Die mutigen Kinder bauen eine große hütte."], B_E,
                info="„mutigen“ und „große“ stehen vor einem Nomen und bleiben klein. „Kinder“ und „Hütte“ sind Nomen."))
    a.append(gk("Eine [kluge|Adjektiv vor dem Nomen „Füchsin“, bleibt klein] [Füchsin|Artikel „Eine“ und Adjektiv „kluge“ stehen davor] suchte etwas [Essbares|Indefinitpronomen „etwas“ steht davor].", B_E))
    a.append(gk("[Einige|Satzanfang] [schräge|Adjektiv vor dem Nomen „Töne“, bleibt klein] [Töne|Indefinitpronomen „Einige“ und Adjektiv „schräge“ stehen davor] störten niemanden, denn wir hörten [nichts|Indefinitpronomen, kein Nomen] [Peinliches|Indefinitpronomen „nichts“ steht davor].", B_E))
    a.append(gk("[Ein|Satzanfang] [paar|Indefinitpronomen, kein Nomen] [weiße|Adjektiv vor dem Nomen „Socken“, bleibt klein] [Socken|Indefinitpronomen „paar“ und Adjektiv „weiße“ stehen davor] lagen im Schrank.", B_E))
    a.append(mc("Warum schreibt man „bunten“ in „Sie trägt einen bunten Schal.“ klein?",
                "Weil danach das Nomen „Schal“ folgt.",
                ["Weil „bunten“ am Ende steht.", "Weil Farben immer klein geschrieben werden.", "Weil „einen“ ein Verb ist."], B_E,
                info="Ein Adjektiv vor einem Nomen bleibt klein. Nur wenn kein Nomen folgt, wäre es nominalisiert, zum Beispiel: Sie mag das Bunte."))
    a.append(kurz("Setze „berühmt“ mit der richtigen Endung ein: Sie singt ein … Lied.", "berühmtes", B_E, gross=True,
                  info="Das Nomen „Lied“ ist sächlich, deshalb endet das Adjektiv auf -es: ein berühmtes Lied. Es bleibt klein, weil ein Nomen folgt."))
    a.append(kurz("Setze „cool“ mit der richtigen Endung ein: Er trägt eine … Jacke.", "coole", B_E, gross=True,
                  info="Das Nomen „Jacke“ ist weiblich, deshalb endet das Adjektiv auf -e: eine coole Jacke. Es bleibt klein, weil ein Nomen folgt."))

    # ---------------------------------------------------------------- F
    a.append(gk("Am [Samstag|Begleiter „Am“ (an dem) steht davor] feiert unsere Klasse ein [Fest|Artikel „ein“ steht davor]. Das [Beste|Artikel „Das“ steht davor] daran ist das [Tanzen|Artikel „das“ steht davor]. Wir wollen [laut|Adjektiv oder Adverb, kein Nomen] [singen|Verb nach dem Modalverb „wollen“] und nichts [Trauriges|Indefinitpronomen „nichts“ steht davor] hören. Am [meisten|Superlativ mit „am“ (Frage: Wie?)] freut sich Ole auf den [Kuchen|Artikel „den“ steht davor].",
                B_F, frage="Groß oder klein? Ziehe in jede Lücke das Wort in der richtigen Schreibweise (Text: Das Klassenfest)."))
    a.append(gk("Beim [Radfahren|Begleiter „Beim“ (bei dem) steht davor] im [Wald|Begleiter „im“ (in dem) steht davor] entdeckten wir [viel|Indefinitpronomen, kein Nomen] [Neues|Indefinitpronomen „viel“ steht davor]. Im [Flug|Begleiter „Im“ (in dem) steht davor] raste ein [Specht|Artikel „ein“ steht davor] an uns vorbei. Mit [Hilfe|Präposition „Mit“ steht davor] einer [Karte|Artikel „einer“ steht davor] fanden wir den Weg.",
                B_F, frage="Groß oder klein? Ziehe in jede Lücke das Wort in der richtigen Schreibweise (Text: Die Radtour)."))
    a.append(gk("Im [Tierheim|Begleiter „Im“ (in dem) steht davor] gibt es [allerlei|Indefinitpronomen, kein Nomen] [Interessantes|Indefinitpronomen „allerlei“ steht davor]. Das [Füttern|Artikel „Das“ steht davor] der kleinen [Katzen|Artikel „der“ und Adjektiv „kleinen“ stehen davor] macht Pia [Freude|Nomen ohne Begleiter, Probe: die große Freude]. Sie möchte am [liebsten|Superlativ mit „am“ (Frage: Wie?)] alle Tiere [mitnehmen|Verb nach dem Modalverb „möchte“].",
                B_F, frage="Groß oder klein? Ziehe in jede Lücke das Wort in der richtigen Schreibweise (Text: Im Tierheim)."))
    a.append(gk("Der [Spieleabend|Artikel „Der“ steht davor] war das [Schönste|Artikel „das“ steht davor] am Wochenende. Wir spielten [lange|Adverb, kein Nomen] und hatten nichts [Besseres|Indefinitpronomen „nichts“ steht davor] vor. Beim [Würfeln|Begleiter „Beim“ (bei dem) steht davor] war Mia am [glücklichsten|Superlativ mit „am“ (Frage: Wie?)]. Zum [Schluss|Begleiter „Zum“ (zu dem) steht davor] gab es [Popcorn|Nomen ohne Begleiter, Probe: das süße Popcorn].",
                B_F, frage="Groß oder klein? Ziehe in jede Lücke das Wort in der richtigen Schreibweise (Text: Der Spieleabend)."))
    a.append(gk("Wandern ist für [Junge|Präposition „für“ steht davor] und [Alte|nominalisiert wie „Junge“, die Präposition „für“ gehört auch dazu] ein [Vergnügen|Artikel „ein“ steht davor]. Im [Gebirge|Begleiter „Im“ (in dem) steht davor] gibt es viel [Schönes|Indefinitpronomen „viel“ steht davor] zu [sehen|Verb mit „zu“ davor (zu + Infinitiv)]. Das [Beste|Artikel „Das“ steht davor] ist die frische [Luft|Artikel „die“ und Adjektiv „frische“ stehen davor].",
                B_F, frage="Groß oder klein? Ziehe in jede Lücke das Wort in der richtigen Schreibweise (Text: Wandern).",
                tauschbar=[("Junge", "Alte")]))
    a.append(gk("Mara bastelt gern. Zum [Basteln|Begleiter „Zum“ (zu dem) steht davor] braucht sie [Papier|Nomen ohne Begleiter, Probe: das bunte Papier] und etwas [Kleber|Indefinitpronomen „etwas“ steht davor, Nomen]. Das [Schneiden|Artikel „Das“ steht davor] fällt ihr [leicht|Adjektiv, kein Nomen]. Beim [Kleben|Begleiter „Beim“ (bei dem) steht davor] ist sie am [genauesten|Superlativ mit „am“ (Frage: Wie?)].",
                B_F, frage="Groß oder klein? Ziehe in jede Lücke das Wort in der richtigen Schreibweise (Text: Das Basteln).",
                tauschbar=[("Basteln", "Schneiden", "Kleben"), ("Papier", "Kleber")]))
    a.append(gk("Der [Zirkus|Artikel „Der“ steht davor] kommt jedes Jahr in unsere [Stadt|Pronomen „unsere“ steht davor]. Das [Aufregendste|Artikel „Das“ steht davor] ist der [Auftritt|Artikel „der“ steht davor] der Artisten. Sie zeigen viel [Mutiges|Indefinitpronomen „viel“ steht davor] und manches [Lustige|Indefinitpronomen „manches“ steht davor]. Am [besten|Superlativ mit „am“ (Frage: Wie?)] gefällt uns das [Jonglieren|Artikel „das“ steht davor].",
                B_F, frage="Groß oder klein? Ziehe in jede Lücke das Wort in der richtigen Schreibweise (Text: Der Zirkus)."))
    a.append(gk("Im [Herbst|Begleiter „Im“ (in dem) steht davor] ist das [Wetter|Artikel „das“ steht davor] oft [kalt|Adjektiv, kein Nomen] und [nass|Adjektiv, kein Nomen]. Ich bleibe dann im [Warmen|Begleiter „im“ (in dem), nominalisiert: das Warme] und lese ein [Buch|Artikel „ein“ steht davor]. Das [Lesen|Artikel „Das“ steht davor] macht mir [Spaß|Nomen ohne Begleiter, Probe: der große Spaß]. Etwas [Spannendes|Indefinitpronomen „Etwas“ steht davor] ist mir am [liebsten|Superlativ mit „am“ (Frage: Wie?)].",
                B_F, frage="Groß oder klein? Ziehe in jede Lücke das Wort in der richtigen Schreibweise (Text: Ein Regentag).",
                tauschbar=[("kalt", "nass")]))
    return a


def build():
    p = pack(ID, "Deutsch Teil 1c: Adjektive als Nomen, Indefinitpronomen und Superlativ",
             "Nominalisierte Adjektive (das Neue, im Dunkeln, etwas Schönes), Indefinitpronomen als Begleiter, Superlativ mit „am“ oder nominalisiert, Fallen und gemischte Texte. Mit Lernblatt und Übungsaufgaben.",
             lernblatt(), aufgaben(), min_aufgaben=50,
             hinweis="Alle Sätze, Texte und Namen sind selbst ausgedacht, nicht aus dem Deutschbuch, dem Nominalisierungsheft oder dem Aufgabenheft. Die Regeln stehen so auch im Deutschbuch (S. 302–304). Bei den Groß-/Kleinschreibungs-Aufgaben zählt jeder Buchstabe: Tippe das Wort genau so, wie es im Satz stehen muss.")
    return [nachlesen(p, {B_A: [L1, L2], B_B: L2, B_C: L3, B_D: L4, B_E: L5, B_F: [L1, L3, L4, L5]})]


if __name__ == "__main__":
    for p in build():
        print(p["id"], len(p["aufgaben"]), "Aufgaben")
