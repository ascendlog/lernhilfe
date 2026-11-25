"""Deutsch Klasse 6, Paket 3c: Diktat üben (Schwerpunkt Nominalisierung).

Der Text des Diktats in der Arbeit ist unbekannt. Alle Sätze und Diktattexte sind selbst geschrieben (nicht der Buchtext
von S. 312, keine wörtliche Rede). Fehlerarten und Strategien laut Faktenblatt Abschnitt 8 und 9.
Die Vorlese-Funktion (vorlesen, sprache de-DE) nutzt die Sprachausgabe des Browsers. Sie lässt sich im Testbrowser nicht
anhören; der Vorlesetext steht deshalb zusätzlich als „Text für Eltern“ in jeder Aufgabe.
"""
from deutsch_lib import *

ID = "deutsch-3c-diktat-ueben"

B_A = "A – Einzelne Sätze diktieren"
B_B = "B – Diktattexte Satz für Satz"
B_C = "C – Fehler finden und verbessern"
B_D = "D – Ganzes Diktat auf Papier"
B_E = "E – Fehlerarten und Selbstkontrolle"

L1 = "So gehst du beim Diktat vor"
L2 = "Fehlerarten im Diktat: Wo liegt der Fehler?"


def lernblatt():
    return [
        lb(L1,
           "Im Diktat schreibst du einen Text, den dir jemand vorliest. So gehst du vor:\n"
           "1. **Zuhören:** Der Text wird zuerst ganz vorgelesen. Höre genau hin.\n"
           "2. **Schreiben:** Schreibe Satz für Satz. Sprich leise mit und **schwinge** die Silben. Bei unsicheren Wörtern: **einkreisen** und weiterschreiben.\n"
           "3. **Prüfen:** Lies am Ende alles noch einmal Wort für Wort. Prüfe die eingekreisten Wörter mit einer Strategie: Verlängern, Zerlegen, Ableiten, Merkwörter.\n"
           "**Schwerpunkt Nominalisierung:** Achte auf Wörter, vor denen ein **Begleiter** oder Signalwort steht: beim Wandern, zum Essen, im Dunkeln, das Schönste, etwas Neues, nichts Besonderes, viel Interessantes, alles Gute. Diese Wörter schreibst du **groß**. Bei **am** plus Superlativ (am schnellsten) schreibst du **klein**.\n"
           "**Kommas:** Ein Komma steht vor aber, doch, sondern und denn, vor Nebensätzen (weil, dass, wenn, obwohl, damit) und vor und nach einem Relativsatz (der, die, das). Vor „und“ und „oder“ zwischen Hauptsätzen darf das Komma wegfallen.",
           merke="Diktat: Zuhören, Satz für Satz schreiben, unsichere Wörter einkreisen, am Ende prüfen. Nominalisierungen groß, am + Superlativ klein, Kommas nicht vergessen."),
        lb(L2,
           "Im Fehlerbogen ordnest du jeden Fehler einer **Fehlerart** zu. Daran erkennst du auch die passende Strategie:\n"
           "- **Doppelkonsonanten, ck und tz** (Kanne, Decke, Katze): schwingen und verlängern.\n"
           "- **s, ss oder ß** (Hase, Tasse, Straße): Silbe offen oder geschlossen? Summt oder zischt der Laut?\n"
           "- **i oder ie** (Kinder, Wiese): Ist die erste Silbe offen oder geschlossen?\n"
           "- **Silbenöffnendes h** (ziehen, Mühe): verlängern, das h steht am Anfang der zweiten Silbe.\n"
           "- **b/p, d/t, g/k** (Korb, Hund, Berg): verlängern.\n"
           "- **Zusammengesetzte Wörter** (Handtuch, Landkarte): zerlegen und verlängern.\n"
           "- **e/ä und eu/äu** (Bäume, Keller): ableiten.\n"
           "- **Groß- und Kleinschreibung** (beim Wandern, das Schönste): Begleiter suchen, Probe machen.",
           merke="Acht Fehlerarten: Doppelkonsonant/ck/tz, s-Laute, i/ie, h, b/p d/t g/k, zusammengesetzte Wörter, e/ä eu/äu, Groß- und Kleinschreibung."),
    ]


def satz(frage, text, abschnitt, info, tipp=None):
    """Diktat-Aufgabe: Satz anhören und abtippen (Groß-/Kleinschreibung und Kommas zählen)."""
    return kurz(frage, text, abschnitt, info=info, tipp=tipp, gross=True, vorlesen=text)


def aufgaben():
    a = []
    F = "Hör genau hin (Tippe auf „Anhören“) und schreibe den Satz auf."
    # ---------------------------------------------------------------- A: einzelne Sätze
    a.append(satz(F, "Beim Lesen vergesse ich die Zeit.", B_A,
                  "„Beim“ (bei dem) steht vor „Lesen“. Das Verb ist nominalisiert und wird großgeschrieben. „Zeit“ ist ein Nomen.",
                  tipp="Suche den Begleiter vor dem Verb."))
    a.append(satz(F, "Im Garten gibt es viel Schönes zu sehen.", B_A,
                  "„viel“ steht vor „Schönes“. Das Adjektiv ist nominalisiert und wird großgeschrieben. „sehen“ ist ein Verb und bleibt klein."))
    a.append(satz(F, "Er hat nichts Besseres zu tun.", B_A,
                  "Nach „nichts“ wird das Adjektiv nominalisiert: nichts Besseres. „tun“ bleibt klein."))
    a.append(satz(F, "Am schnellsten läuft Mia von allen.", B_A,
                  "Frage: Wie läuft Mia? Am schnellsten. Superlative mit „am“ schreibt man klein. „allen“ ist ein Indefinitpronomen und bleibt klein.",
                  tipp="Mache die Frage „Wie?“"))
    a.append(satz(F, "Das Wichtigste ist die Gesundheit.", B_A,
                  "„Das Wichtigste“: Der Artikel „das“ steht davor, der Superlativ ist nominalisiert und wird großgeschrieben. „Gesundheit“ ist ein Nomen."))
    a.append(satz(F, "Wir wünschen dir alles Gute zum Geburtstag.", B_A,
                  "„alles Gute“ ist nominalisiert (Signalwort „alles“). „zum“ ist zu dem, deshalb schreibt man „Geburtstag“ groß."))
    a.append(satz(F, "Beim Kochen hilft mir mein Bruder.", B_A,
                  "„Beim“ steht vor „Kochen“: nominalisiertes Verb, groß. „Bruder“ hat den Begleiter „mein“."))
    a.append(satz(F, "Der Lehrer erklärt den Kindern etwas Neues.", B_A,
                  "„etwas Neues“ ist nominalisiert. Kin-der hat eine geschlossene erste Silbe, deshalb schreibt man i."))
    a.append(satz(F, "Auf das Wiedersehen freuen wir uns sehr.", B_A,
                  "„auf das“ steht vor „Wiedersehen“: nominalisiertes Verb, groß. „sehr“ bleibt klein."))
    a.append(satz(F, "Das Schwimmen im Meer macht Mia Freude.", B_A,
                  "„Das Schwimmen“ ist nominalisiert. „Meer“ hat einen Doppelvokal (ee), „Freude“ ist ein Nomen."))
    a.append(satz(F, "Im Dunkeln hat Ole keine Angst.", B_A,
                  "„Im Dunkeln“ (in dem Dunkeln) ist ein nominalisiertes Adjektiv und wird großgeschrieben. „Angst“ hat den Begleiter „keine“."))
    a.append(satz(F, "Zum Frühstück gibt es Brötchen mit Marmelade.", B_A,
                  "„Zum“ (zu dem) steht vor „Frühstück“. Brötchen kommt von Brot (ö). „Marmelade“ ist ein Nomen."))

    # ---------------------------------------------------------------- B: Diktattexte
    t1 = "Diktat 1 „Der Schulausflug“, Satz {}: Hör genau hin und schreibe den Satz auf."
    a.append(satz(t1.format(1), "Beim Wandern im Wald haben wir viel Neues gesehen.", B_B,
                  "„Beim“ steht vor „Wandern“ (nominalisiert). „viel Neues“ ist ein nominalisiertes Adjektiv. „Wald“ hat den Begleiter „im“ (in dem)."))
    a.append(satz(t1.format(2), "Das Schönste war das Picknick am See.", B_B,
                  "„Das Schönste“ ist ein nominalisierter Superlativ. „Picknick“ und „See“ sind Nomen (See hat Doppelvokal ee)."))
    a.append(satz(t1.format(3), "Zum Essen gab es Brote mit Käse, denn die Kinder hatten großen Hunger.", B_B,
                  "„Zum Essen“ ist nominalisiert. Käse ist ein Merkwort mit ä. Vor „denn“ steht ein Komma (Satzreihe). Brote kommt von Brot, großen und Hunger schreibt man wie gehört."))
    a.append(satz(t1.format(4), "Nach dem Spielen suchten wir Pilze, die am Rand des Weges wuchsen.", B_B,
                  "„Nach dem Spielen“ ist nominalisiert. „die am Rand des Weges wuchsen“ ist ein Relativsatz, davor steht ein Komma. Pil-ze hat eine geschlossene erste Silbe (i)."))
    a.append(satz(t1.format(5), "Auf dem Heimweg waren alle müde, aber das Beste war der gemeinsame Ausflug.", B_B,
                  "„alle“ bleibt klein. Vor „aber“ steht ein Komma. „Das Beste“ ist ein nominalisierter Superlativ."))
    t2 = "Diktat 2 „Im Hallenbad“, Satz {}: Hör genau hin und schreibe den Satz auf."
    a.append(satz(t2.format(1), "Am Mittwoch gehen wir zum Schwimmen ins Hallenbad.", B_B,
                  "Mitt-woch hat tt. „zum Schwimmen“ ist nominalisiert. „ins“ ist in das, danach steht das Nomen „Hallenbad“."))
    a.append(satz(t2.format(2), "Die Kinder freuen sich auf das Springen, weil das Wasser angenehm warm ist.", B_B,
                  "„auf das Springen“ ist nominalisiert. Vor „weil“ steht ein Komma (Satzgefüge). „warm“ ist ein Adjektiv und bleibt klein."))
    a.append(satz(t2.format(3), "Beim Tauchen dürfen sie nichts Gefährliches tun.", B_B,
                  "„Beim Tauchen“ ist nominalisiert. „nichts Gefährliches“ ist ein nominalisiertes Adjektiv. „dürfen“ und „tun“ sind Verben."))
    a.append(satz(t2.format(4), "Nach dem Schwimmen gibt es etwas Warmes zu trinken.", B_B,
                  "„Nach dem Schwimmen“ ist nominalisiert. „etwas Warmes“ ist ein nominalisiertes Adjektiv. „trinken“ bleibt klein."))
    a.append(satz(t2.format(5), "Am Ende sind alle müde, doch das Schönste war das gemeinsame Lachen.", B_B,
                  "Vor „doch“ steht ein Komma (Gegensatz). „Das Schönste“ ist ein nominalisierter Superlativ, „das gemeinsame Lachen“ ein nominalisiertes Verb mit Adjektiv."))
    t3 = "Diktat 3 „Im Herbst“, Satz {}: Hör genau hin und schreibe den Satz auf."
    a.append(satz(t3.format(1), "Im Herbst fallen die Blätter von den Bäumen, weil der Wind kräftig weht.", B_B,
                  "Blätter (Blatt) und Bäumen (Baum) schreibt man mit ä. Vor „weil“ steht ein Komma. kräftig kommt von Kraft."))
    a.append(satz(t3.format(2), "Beim Sammeln der Kastanien finden die Kinder viel Interessantes.", B_B,
                  "„Beim Sammeln“ ist nominalisiert. „viel Interessantes“ ist ein nominalisiertes Adjektiv. Kastanien hat keine Verdopplung (s und t)."))
    a.append(satz(t3.format(3), "Das Laub, das auf dem Boden liegt, raschelt beim Gehen.", B_B,
                  "„das auf dem Boden liegt“ ist ein Relativsatz, er steht zwischen zwei Kommas. „beim Gehen“ ist nominalisiert."))
    a.append(satz(t3.format(4), "Am liebsten spielen sie im Laub, denn das Lustigste ist das Verstecken.", B_B,
                  "„Am liebsten“ ist ein Superlativ mit „am“ und bleibt klein. Vor „denn“ steht ein Komma. „Das Lustigste“ und „das Verstecken“ sind nominalisiert."))
    a.append(satz(t3.format(5), "Mit etwas Glück scheint am Nachmittag noch die Sonne.", B_B,
                  "„Mit etwas Glück“: „Glück“ ist ein Nomen. „am Nachmittag“ (an dem Nachmittag) ist ein Nomen mit Begleiter. Son-ne hat nn."))

    # ---------------------------------------------------------------- C: Fehler finden
    FC = "In diesem Satz stecken Fehler: {}. Schreibe den Satz richtig auf."
    a.append(kurz(FC.format("„Beim tanzen entdeckte Mia etwas lustiges.“"), "Beim Tanzen entdeckte Mia etwas Lustiges.", B_C, gross=True,
                  info="„Beim Tanzen“ ist ein nominalisiertes Verb (Begleiter „beim“). „etwas Lustiges“ ist ein nominalisiertes Adjektiv (Signalwort „etwas“)."))
    a.append(kurz(FC.format("„Am Besten malt Ole von allen.“"), "Am besten malt Ole von allen.", B_C, gross=True,
                  info="Frage: Wie malt Ole? Am besten. Superlative mit „am“ schreibt man klein."))
    a.append(kurz(FC.format("„Das Wasser ist kalt aber die Kinder baden trotzdem.“"), "Das Wasser ist kalt, aber die Kinder baden trotzdem.", B_C, gross=True,
                  info="Vor „aber“ steht in einer Satzreihe immer ein Komma."))
    a.append(kurz(FC.format("„Der Hunt trägt einen Stap im Maul.“"), "Der Hund trägt einen Stab im Maul.", B_C, gross=True,
                  info="Verlängern: Hunde (d), Stäbe (b)."))
    a.append(kurz(FC.format("„Die Meuse laufen über die Wise.“"), "Die Mäuse laufen über die Wiese.", B_C, gross=True,
                  info="Mäuse – Maus (äu). Wie-se: offene erste Silbe, langes i, also ie."))
    a.append(kurz(FC.format("„Ole hat nichts gefährliches getan, weil er vorsichtig war.“"), "Ole hat nichts Gefährliches getan, weil er vorsichtig war.", B_C, gross=True,
                  info="Nach „nichts“ wird das Adjektiv nominalisiert: nichts Gefährliches. Das Komma vor „weil“ steht schon richtig."))

    # ---------------------------------------------------------------- D: Diktat auf Papier
    d1 = ("Am Samstag blieben wir zu Hause, weil es den ganzen Tag regnete. "
          "Beim Spielen im Wohnzimmer entdeckten die Kinder viel Altes auf dem Dachboden. "
          "Das Interessanteste war eine Kiste, die mit Briefen gefüllt war. "
          "Mia las die Briefe leise, aber Ole suchte nach etwas Besonderem. "
          "Zum Abendessen gab es Suppe, denn bei Kälte schmeckt Warmes am besten. "
          "Das Beste am Tag war das Vorlesen vor dem Einschlafen.")
    FD = ("Diktat auf Papier: Ein Elternteil liest den Text vor (Tippe auf „Anhören“ oder lass dir den Text aufklappen). "
          "Erst ganz, dann in kleinen Stücken, am Ende noch einmal ganz. Schreibe in dein Heft oder hier und vergleiche danach mit der Musterlösung. ")
    t = frei(FD + "Text: Der Regentag.", d1,
             ["Alle Nominalisierungen sind großgeschrieben (Beim Spielen, viel Altes, Das Interessanteste, etwas Besonderem, Warmes, Das Beste, das Vorlesen, dem Einschlafen).",
              "Am besten steht klein (Superlativ mit „am“).",
              "Die Kommas vor weil, aber und denn und vor dem Relativsatz (die mit Briefen gefüllt war) stehen richtig.",
              "Unsichere Wörter hast du mit einer Strategie geprüft (Verlängern, Ableiten, Zerlegen, Merkwörter)."],
             6, B_D, info="Zähle deine Fehler und ordne sie einer Fehlerart zu. Übe diese Fehlerart noch einmal im passenden Übungspaket.")
    t["vorlesen"] = {"text": d1, "sprache": SPRACHE}
    a.append(t)
    d2 = ("Nach der Schule gehen die Kinder auf den Spielplatz. "
          "Beim Klettern auf dem hohen Gerüst haben sie keine Angst. "
          "Ole schaukelt am höchsten, doch Mia rutscht am schnellsten. "
          "Alle freuen sich auf das Wippen, das sie jeden Tag machen. "
          "Am Ende wissen sie nichts Neues zu erzählen, aber das Schönste ist das Zusammensein.")
    t = frei(FD + "Text: Auf dem Spielplatz.", d2,
             ["Alle Nominalisierungen sind großgeschrieben (Beim Klettern, das Wippen, nichts Neues, das Schönste, das Zusammensein).",
              "Die Superlative mit „am“ (am höchsten, am schnellsten) stehen klein.",
              "Die Kommas vor doch und aber und vor dem Relativsatz (das sie jeden Tag machen) stehen richtig.",
              "Unsichere Wörter hast du mit einer Strategie geprüft (Verlängern, Ableiten, Zerlegen, Merkwörter)."],
             6, B_D, info="Zähle deine Fehler und ordne sie einer Fehlerart zu. Übe diese Fehlerart noch einmal im passenden Übungspaket.")
    t["vorlesen"] = {"text": d2, "sprache": SPRACHE}
    a.append(t)

    # ---------------------------------------------------------------- E: Fehlerarten und Selbstkontrolle
    a.append(zuordnen("Welcher Fehlerart gehört der Fehler an?",
                      [("Kaze statt Katze", "Doppelkonsonant, ck oder tz"), ("Strase statt Straße", "s, ss oder ß"), ("Spilen statt spielen", "i oder ie"),
                       ("Müe statt Mühe", "silbenöffnendes h"), ("Hunt statt Hund", "b/p, d/t oder g/k"), ("Meuse statt Mäuse", "e/ä oder eu/äu"),
                       ("beim schwimmen statt beim Schwimmen", "Groß- und Kleinschreibung")],
                      B_E, info="Kaze: tz fehlt. Strase: ß fehlt (Stra-ße). Spilen: ie fehlt (spie-len). Müe: das silbenöffnende h fehlt (Mü-he). Hunt: Verlängern zeigt d (Hunde). Meuse: Ableiten zeigt äu (Maus). beim schwimmen: Nominalisierung groß."))
    a.append(mc("Du bist bei einem Wort im Diktat unsicher. Was machst du?",
                "Ich kreise es ein, schreibe weiter und prüfe am Ende mit einer Regel oder Strategie.",
                ["Ich höre auf zu schreiben und warte.", "Ich lasse das Wort weg.", "Ich schreibe es dreimal und nehme das schönste."], B_E,
                info="Unsichere Wörter einkreisen und weiterschreiben, damit du den Faden nicht verlierst. Am Ende prüfst du sie mit Verlängern, Zerlegen, Ableiten oder bei Merkwörtern aus dem Gedächtnis."))
    a.append(mc("Welche Wörter schreibst du in diesem Satz groß? beim wandern im wald hatten wir viel spaß und sahen etwas schönes. (mehrere Antworten sind richtig)",
                ["wandern", "wald", "spaß", "schönes"], ["hatten", "sahen"], B_E,
                info="Groß: Wandern (Begleiter „beim“), Wald (Begleiter „im“), Spaß (Signalwort „viel“), Schönes (Signalwort „etwas“). Klein: hatten und sahen sind Verben."))
    a.append(tf("Vor einer Nominalisierung steht ein Begleiter oder Signalwort wie beim, zum, das, etwas, viel oder nichts.", True, B_E,
                info="Diese Wörter zeigen dir, dass ein Verb oder Adjektiv zum Nomen geworden ist: beim Lesen, etwas Neues, nichts Besonderes."))
    a.append(tf("Bei „am schnellsten“ schreibt man „schnellsten“ groß, weil „am“ davor steht.", False, B_E,
                info="Superlative mit „am“ beantworten die Frage „Wie?“ und bleiben klein: Mia läuft am schnellsten."))
    return a


def build():
    p = pack(ID, "Deutsch Teil 3c: Diktat üben",
             "Diktat üben mit Schwerpunkt Nominalisierung: Sätze anhören und schreiben, drei Diktattexte Satz für Satz, Fehler finden, zwei Diktate auf Papier und die Fehlerarten zuordnen. Mit Lernblatt.",
             lernblatt(), aufgaben(), min_aufgaben=35,
             hinweis="Das Diktat in der Arbeit ist unbekannt. Diese Texte sind selbst geschrieben und nicht der Text des Lehrers. Auf „Anhören“ liest dein Gerät den Satz vor (geht in Edge und Chrome am besten). Klappt das nicht, liest ein Elternteil den Text vor („Text zum Vorlesen“). Beim Abtippen zählt jeder Buchstabe, Groß- und Kleinschreibung und jedes Komma mitten im Satz.")
    return [nachlesen(p, {B_A: L1, B_B: L1, B_C: [L2, L1], B_D: L1, B_E: L2})]


if __name__ == "__main__":
    for p in build():
        print(p["id"], len(p["aufgaben"]), "Aufgaben")
