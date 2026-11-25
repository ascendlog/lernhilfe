"""Deutsch Klasse 6, Paket 1b: Nominalisierte Verben (Checkliste Nominalisierung 2 und 4; DB S. 302–303, Nominalisierungsheft S. 57–58, AH S. 83).

Alle Sätze, Texte und Namen sind erfunden. Lösungen laut Faktenblatt Abschnitt 2 und 13.
"""
from deutsch_lib import *

ID = "deutsch-1b-nominalisierte-verben"

B_A = "A – Verb oder Nomen?"
B_B = "B – Die Begleiter nominalisierter Verben"
B_C = "C – Verben nominalisieren"
B_D = "D – Mehrteilige Verben"
B_E = "E – Fallen: groß oder klein?"
B_F = "F – Kleine Texte"
B_G = "G – Sachlich formulieren"

L1 = "Verben als Nomen"
L2 = "Die Begleiter erkennen"
L3 = "Mehrteilige Verben"
L4 = "Fallen: Verb bleibt Verb"
L5 = "Sachlich formulieren mit Nominalisierungen"


def lernblatt():
    return [
        lb(L1,
           "Ein Verb in der **Grundform** (Infinitiv) kann wie ein **Nomen** gebraucht werden. Man nennt das **Nominalisierung**. Das nominalisierte Verb schreibt man **groß**.\n"
           "- Wir **spielen** draußen. (Verb, klein)\n"
           "- Das **Spielen** macht Spaß. (nominalisiert, groß)\n"
           "Weitere Beispiele: das Singen, beim Lesen, zum Plantschen, sein Lachen.\n"
           "Das nominalisierte Verb steht in der **Grundform**. Aus „er singt“ wird „das Singen“, nicht „das Singt“.",
           merke="Wird ein Verb wie ein Nomen gebraucht, schreibt man es groß: das Lesen, beim Singen."),
        lb(L2,
           "Nominalisierte Verben haben dieselben **Begleiter** wie Nomen:\n"
           "- **Artikel**: das Spielen, ein Lachen\n"
           "- **Adjektiv**: fröhliches Spielen, lautes Lachen\n"
           "- **Pronomen**: ihr Spielen, dein Zögern, unser Singen\n"
           "- **Präposition** (oft verschmolzen): beim (bei dem) Spielen, zum (zu dem) Singen, vom (von dem) Lesen, am (an dem) Basteln, im (in dem) Sitzen\n"
           "Mit der **Artikelprobe** prüfst du es: Kannst du einen Artikel davorsetzen? gehen → das Gehen, zögern → dein Zögern, singen → beim (bei dem) Singen.",
           merke="Begleiter vor dem Verb in der Grundform (das, beim, zum, dein, lautes …) zeigen: Das Verb ist nominalisiert, schreib groß."),
        lb(L3,
           "Manche Verben bestehen aus **mehreren Teilen**: aufgeben, aufstehen, hineinspringen, nachdenken.\n"
           "Wird so ein Verb nominalisiert, steht es in der Grundform und die Teile bleiben **zusammen**: Ich gebe auf → **das Aufgeben**. Wir stehen früh auf → **das Aufstehen**. Sie springen hinein → **das Hineinspringen**.\n"
           "Man schreibt nur den **Anfang groß**: das Hineinspringen, nicht „das HineinSpringen“ und nicht „das hinein Springen“.",
           merke="Bei mehrteiligen Verben bleibt die Grundform zusammen: aufgeben → das Aufgeben."),
        lb(L4,
           "Nicht jedes Verb in der Grundform ist nominalisiert. Diese Fälle bleiben **Verben** und werden **klein** geschrieben:\n"
           "- Verb nach einem **Modalverb** (können, wollen, müssen, dürfen, sollen): Wir wollen **spielen**. Sie kann gut **singen**.\n"
           "- Verb mit **zu** davor: Ich habe Lust **zu lesen**. Um die Prüfung **zu bestehen**, übe ich. Es gibt viel **zu entdecken**.\n"
           "Aber: **zum**, **beim**, **vom** bestehen aus Präposition und Artikel. Danach steht ein nominalisiertes Verb: **zum Aufgeben** zwingen, **beim Lesen**.\n"
           "Vergleiche: Sie kann herzlich **lachen** (Verb) – ihr **Lachen** steckt an (nominalisiert).",
           merke="Nach Modalverb und nach „zu“ bleibt das Verb klein. Nach Begleiter (das, beim, zum, dein …) schreibt man es groß."),
        lb(L5,
           "Mit Nominalisierungen kann man etwas **kurz und sachlich** sagen. Aus einem Nebensatz mit „dass“ wird ein Nomen:\n"
           "- Dass ich die Käfer im Garten beobachte, finde ich interessant. → **Das Beobachten** der Käfer im Garten ist interessant.\n"
           "Auch **Handlungsanweisungen** schreibt man so: Man soll messen. → **Das Messen** der Temperatur ist wichtig. Man soll die Blätter sammeln. → **Das Sammeln** der Blätter gehört dazu.\n"
           "Nach dem nominalisierten Verb steht oft ein **Genitiv** (der Käfer, der Blätter) oder eine **Präposition** (im Garten).",
           merke="Artikel + nominalisiertes Verb + Rest = sachlicher Ausdruck: Das Messen der Temperatur."),
    ]


def aufgaben():
    a = []
    # ---------------------------------------------------------------- A
    a.append(zuordnen("Verb oder nominalisiertes Verb? Ordne zu.",
                      [("Das Lesen macht mir Freude.", "nominalisiert"), ("Ich lese ein Buch.", "Verb"),
                       ("Beim Backen riecht es gut.", "nominalisiert"), ("Wir backen einen Kuchen.", "Verb"),
                       ("Zum Tanzen braucht man Musik.", "nominalisiert"), ("Sie tanzt gern.", "Verb")],
                      B_A, info="Mit Begleiter (Das, Beim, Zum) und in der Grundform ist das Verb nominalisiert. Als Personalform (lese, backen, tanzt) mit Subjekt bleibt es ein Verb."))
    a.append(mc("In welchem Satz wird „schwimmen“ wie ein Nomen gebraucht?",
                "Beim Schwimmen vergesse ich die Zeit.",
                ["Wir wollen im See schwimmen.", "Ole kann gut schwimmen.", "Sie schwimmt jeden Tag."], B_A,
                info="„Beim“ (= bei dem) ist ein Begleiter, deshalb ist „Schwimmen“ nominalisiert und groß. In den anderen Sätzen ist „schwimmen“ ein Verb."))
    a.append(tf("Ein nominalisiertes Verb steht in der Grundform: das Spielen.", True, B_A,
                info="Aus „er spielt“ wird beim Nominalisieren „das Spielen“. Die Grundform endet meist auf -en oder -n."))
    a.append(tf("Nominalisierte Verben schreibt man klein.", False, B_A,
                info="Ein Verb, das wie ein Nomen gebraucht wird, schreibt man groß: das Lesen."))
    a.append(mc("Woran erkennt man das nominalisierte Verb in „Sein Zögern war nicht zu übersehen.“?",
                "An dem Pronomen „Sein“ davor", ["An der Endung -ern", "Am Verb „war“", "Daran, dass es am Satzende steht"], B_A,
                info="Wie bei Nomen sind die Begleiter das Signal. „Sein“ steht vor „Zögern“. Mit der Artikelprobe geht es auch: das Zögern."))
    a.append(mc("Wir freuen uns auf das Wiedersehen mit euch. Welches Wort ist ein nominalisiertes Verb?",
                "Wiedersehen", ["freuen", "uns", "euch"], B_A,
                info="„das“ ist der Artikel von „Wiedersehen“ (von wiedersehen). „freuen“ ist ein Verb, „uns“ und „euch“ sind Pronomen."))
    a.append(zuordnen("Schreibe die Wortgruppe mit der verschmolzenen Form.",
                      [("bei dem Singen", "beim Singen"), ("zu dem Lesen", "zum Lesen"), ("von dem Spielen", "vom Spielen"),
                       ("an dem Basteln", "am Basteln"), ("in dem Rechnen", "im Rechnen")],
                      B_A, info="bei dem → beim, zu dem → zum, von dem → vom, an dem → am, in dem → im."))
    a.append(mc("Welche Schreibweise ist richtig?",
                "beim Singen", ["beim singen", "Beim singen", "beim SINGEN"], B_A,
                info="„beim“ ist ein Begleiter (bei dem). Das Verb danach ist nominalisiert: beim Singen."))
    a.append(tf("Aus „er singt“ wird beim Nominalisieren „das Singt“.", False, B_A,
                info="Nominalisiert wird die Grundform: singen → das Singen. Die Personalform „singt“ kann man nicht nominalisieren."))
    a.append(kurz("Setze das Verb „reiten“ als Nomen ein: Das … macht ihr Spaß.", "Reiten", B_A, gross=True,
                  info="Mit dem Artikel „Das“ davor wird das Verb nominalisiert: Das Reiten macht ihr Spaß."))

    # ---------------------------------------------------------------- B
    a.append(zuordnen("Welcher Begleiter steht vor dem nominalisierten Verb?",
                      [("das Spielen", "Artikel"), ("fröhliches Spielen", "Adjektiv"), ("ihr Spielen", "Pronomen"), ("beim Spielen", "Präposition (mit Artikel)")],
                      B_B, info="das = Artikel, fröhliches = Adjektiv, ihr = Pronomen, beim = Präposition und Artikel (bei dem)."))
    a.append(luecke("Setze die passende verschmolzene Form ein.",
                    "Ole hilft {{beim}} Aufräumen. Mia freut sich {{aufs}} Schwimmen. Wir gehen {{zum}} Wandern in die Berge.", B_B,
                    extra=["vom", "im", "am"], info="beim = bei dem, aufs = auf das, zum = zu dem. Danach folgt das nominalisierte Verb."))
    a.append(tf("In „zum Üben“ ist „zum“ ein Begleiter.", True, B_B,
                info="„zum“ ist zu dem. Es begleitet das nominalisierte Verb „Üben“."))
    a.append(mc("Welche Wortgruppe enthält ein nominalisiertes Verb mit zwei Begleitern?",
                "beim lauten Singen", ["das Singen", "laut singen", "zum Singen"], B_B,
                info="„beim“ (Präposition mit Artikel) und „lauten“ (Adjektiv) stehen vor „Singen“."))
    a.append(mc("Welcher Satz ist richtig geschrieben?",
                "Dein Zögern hat uns geärgert.", ["Dein zögern hat uns geärgert.", "dein Zögern hat uns geärgert.", "Dein zögern hat uns Geärgert."], B_B,
                info="„Dein“ steht am Satzanfang, danach ist „Zögern“ nominalisiert (Pronomen als Begleiter). „geärgert“ ist ein Verb und bleibt klein."))
    a.append(kurz("Wir freuen uns auf das Treffen mit Freunden. Welcher Artikel steht vor „Treffen“?", "das", B_B,
                  info="Der Artikel „das“ ist der Begleiter des nominalisierten Verbs: das Treffen."))
    a.append(mc("Welche Wörter können vor einem nominalisierten Verb stehen? (mehrere Antworten sind richtig)",
                ["das", "beim", "dein", "lautes"], ["sie", "wir"], B_B,
                info="Artikel (das), Präposition mit Artikel (beim), Pronomen (dein) und Adjektiv (lautes) sind Begleiter. „sie“ und „wir“ sind Personalpronomen für das Subjekt, keine Begleiter."))
    a.append(tf("Wörter wie „dein“, „unser“ und „ihr“ können vor einem nominalisierten Verb stehen.", True, B_B,
                info="Possessivpronomen sind Begleiter: dein Zögern, unser Singen, ihr Lachen."))
    a.append(gk("[Fröhliches|Satzanfang] [Singen|Adjektiv „Fröhliches“ steht davor] macht uns gute Laune.",
                B_B, tipp="Der Begleiter steht direkt vor dem Verb in der Grundform."))

    # ---------------------------------------------------------------- C
    a.append(kurz("Schreibe das Verb „lachen“ nominalisiert mit dem Artikel „das“.", ["das Lachen", "Das Lachen"], B_C, gross=True,
                  info="Artikel + Verb in der Grundform, das Verb wird großgeschrieben: das Lachen."))
    a.append(kurz("Schreibe „singen“ nominalisiert mit „beim“.", ["beim Singen", "Beim Singen"], B_C, gross=True,
                  info="beim = bei dem. Danach schreibt man das nominalisierte Verb groß: beim Singen."))
    a.append(kurz("Schreibe „schwimmen“ nominalisiert mit „zum“.", ["zum Schwimmen", "Zum Schwimmen"], B_C, gross=True,
                  info="zum = zu dem. Danach folgt das nominalisierte Verb: zum Schwimmen."))
    a.append(kurz("Schreibe „zeichnen“ nominalisiert mit „vom“.", ["vom Zeichnen", "Vom Zeichnen"], B_C, gross=True,
                  info="vom = von dem. Danach: vom Zeichnen."))
    a.append(kurz("Schreibe „zögern“ nominalisiert mit dem Pronomen „ihr“.", ["ihr Zögern", "Ihr Zögern"], B_C, gross=True,
                  info="Pronomen als Begleiter, das Verb wird großgeschrieben: ihr Zögern."))
    a.append(kurz("Schreibe „sitzen“ nominalisiert mit „im“.", ["im Sitzen", "Im Sitzen"], B_C, gross=True,
                  info="im = in dem. Danach: im Sitzen."))
    a.append(kurz("Schreibe „singen“ nominalisiert mit dem Adjektiv „fröhliches“.", ["fröhliches Singen", "Fröhliches Singen"], B_C, gross=True,
                  info="Adjektiv als Begleiter, das Verb wird großgeschrieben: fröhliches Singen."))
    a.append(mc("Wie schreibt man „das (kochen)“ richtig?", "das Kochen", ["das kochen", "Das kochen", "das KOCHEN"], B_C,
                info="Nach dem Artikel „das“ wird das Verb nominalisiert und großgeschrieben: das Kochen."))
    a.append(mc("Wie schreibt man „zum (üben)“ richtig?", "zum Üben", ["zum üben", "Zum üben", "zumÜben"], B_C,
                info="zum = zu dem. Danach folgt das nominalisierte Verb, es wird großgeschrieben: zum Üben."))

    # ---------------------------------------------------------------- D
    a.append(kurz("Ich gebe nicht auf. Nominalisiere „aufgeben“: Das … fällt mir schwer.", "Aufgeben", B_D, gross=True,
                  info="Die Teile des Verbs bleiben zusammen, nur der Anfang wird großgeschrieben: das Aufgeben."))
    a.append(kurz("Wir stehen früh auf. Nominalisiere „aufstehen“: Das … fällt ihm schwer.", "Aufstehen", B_D, gross=True,
                  info="Grundform von „stehen früh auf“ ist „aufstehen“. Nominalisiert: das Aufstehen."))
    a.append(kurz("Nominalisiere „hineinspringen“: Das … ins kalte Wasser macht Mut.", "Hineinspringen", B_D, gross=True,
                  info="Bei mehrteiligen Verben bleibt die Grundform zusammen: das Hineinspringen."))
    a.append(mc("Wie schreibt man das nominalisierte Verb „nachdenken“ richtig?",
                "das Nachdenken", ["das nachdenken", "das Nach denken", "das NachDenken"], B_D,
                info="Die Verbteile bleiben zusammen, nur der erste Buchstabe wird großgeschrieben: das Nachdenken."))
    a.append(zuordnen("Schreibe das nominalisierte Verb mit „das“.",
                      [("aufräumen", "das Aufräumen"), ("einkaufen", "das Einkaufen"), ("mitmachen", "das Mitmachen"),
                       ("vorlesen", "das Vorlesen"), ("zusehen", "das Zusehen")],
                      B_D, info="Verb in der Grundform zusammen lassen und großschreiben: das Aufräumen, das Einkaufen, das Mitmachen, das Vorlesen, das Zusehen."))
    a.append(gk("Beim [Aufräumen|Begleiter „beim“ (bei dem) steht davor] hilft jeder mit. Wir wollen heute das Zimmer [aufräumen|Verb nach dem Modalverb „wollen“].",
                B_D))
    a.append(tf("Bei „das Aufstehen“ bleiben die Verbteile zusammen, nur der Anfang wird großgeschrieben.", True, B_D,
                info="So schreibt man mehrteilige Verben nominalisiert: das Aufstehen, das Hineinspringen, das Nachdenken."))

    # ---------------------------------------------------------------- E
    a.append(gk("Zum [Schwimmen|Begleiter „zum“ (zu dem) steht davor] braucht man Badesachen, aber ich will heute nicht [schwimmen|Verb nach dem Modalverb „will“].", B_E))
    a.append(gk("Das [Lesen|Artikel „Das“ steht davor] macht Mia Spaß, deshalb [liest|Verb in der Personalform] sie jeden Abend.", B_E))
    a.append(gk("Ole hat Lust, zu [singen|Verb mit „zu“ davor (zu + Infinitiv)]. Beim [Singen|Begleiter „beim“ (bei dem) steht davor] vergisst er die Zeit.", B_E))
    a.append(gk("Um die Prüfung zu [bestehen|Verb mit „zu“ davor (zu + Infinitiv)], braucht man regelmäßiges [Üben|Adjektiv „regelmäßiges“ steht davor].", B_E))
    a.append(gk("Wir dürfen heute [spielen|Verb nach dem Modalverb „dürfen“], aber das [Spielen|Artikel „das“ steht davor] im Flur ist verboten.", B_E))
    a.append(gk("Sein [Lachen|Pronomen „Sein“ steht davor] steckt alle an, denn er kann herzlich [lachen|Verb nach dem Modalverb „kann“].", B_E))
    a.append(gk("Mia hat Freude am [Zuhören|Begleiter „am“ (an dem) steht davor], aber sie möchte nicht immer nur [zuhören|Verb nach dem Modalverb „möchte“].", B_E))
    a.append(gk("Nach dem [Essen|Artikel „dem“ steht davor] müssen wir den Tisch [abräumen|Verb nach dem Modalverb „müssen“].", B_E))
    a.append(gk("Wir mussten lange [warten|Verb nach dem Modalverb „mussten“]. Das [Warten|Artikel „Das“ steht davor] fiel uns schwer.", B_E))
    a.append(gk("Zum [Glück|Begleiter „zum“ (zu dem) steht davor] gibt es beim [Wandern|Begleiter „beim“ (bei dem) steht davor] immer etwas zu [entdecken|Verb mit „zu“ davor (zu + Infinitiv)].", B_E))

    # ---------------------------------------------------------------- F
    a.append(gk("Am [Freitag|Begleiter „Am“ (an dem) steht davor] ist Sporttag. Das [Laufen|Artikel „Das“ steht davor] fällt mir leicht, aber das [Werfen|Artikel „das“ steht davor] muss ich noch üben. Beim [Springen|Begleiter „Beim“ (bei dem) steht davor] zählt jeder Zentimeter. Zum [Abschluss|Begleiter „Zum“ (zu dem) steht davor] dürfen alle [mitmachen|Verb nach dem Modalverb „dürfen“].",
                B_F, frage="Groß oder klein? Ziehe in jede Lücke das Wort in der richtigen Schreibweise (Text: Der Sporttag).",
                tauschbar=[("Laufen", "Werfen", "Springen")]))
    a.append(gk("Im [Wald|Begleiter „Im“ (in dem) steht davor] gibt es viel zu [entdecken|Verb mit „zu“ davor (zu + Infinitiv)]. Das [Sammeln|Artikel „Das“ steht davor] von [Zapfen|Präposition „von“ steht davor] macht uns [Spaß|Nomen ohne Begleiter, Probe: der große Spaß]. Beim [Bauen|Begleiter „Beim“ (bei dem) steht davor] der Hütte hilft jeder mit.",
                B_F, frage="Groß oder klein? Ziehe in jede Lücke das Wort in der richtigen Schreibweise (Text: Ein Tag im Wald)."))
    a.append(gk("Vor dem [Backen|Artikel „dem“ steht davor] wiegt Mia die [Zutaten|Artikel „die“ steht davor] ab. Das [Rühren|Artikel „Das“ steht davor] des Teigs dauert lange, aber sie will nicht [aufgeben|Verb nach dem Modalverb „will“]. Nach dem [Aufgehen|Artikel „dem“ steht davor] kommt der Kuchen in den [Ofen|Artikel „den“ steht davor].",
                B_F, frage="Groß oder klein? Ziehe in jede Lücke das Wort in der richtigen Schreibweise (Text: Der Kuchen).",
                tauschbar=[("Backen", "Rühren")]))
    a.append(gk("Ole liebt das [Zeichnen|Artikel „das“ steht davor]. Beim [Malen|Begleiter „Beim“ (bei dem) steht davor] hört er gern [Musik|Nomen ohne Begleiter, Probe: die leise Musik]. Seine [Schwester|Pronomen „Seine“ steht davor] schaut ihm beim [Zusehen|Begleiter „beim“ (bei dem) steht davor] über die Schulter. Er kann gut [zeichnen|Verb nach dem Modalverb „kann“].",
                B_F, frage="Groß oder klein? Ziehe in jede Lücke das Wort in der richtigen Schreibweise (Text: Das Hobby).",
                tauschbar=[("Zeichnen", "Malen", "Zusehen")], auch={"zeichnen": ["malen"]}))
    a.append(gk("Das [Lernen|Artikel „Das“ steht davor] für die Arbeit fällt manchmal [schwer|Adjektiv, kein Nomen]. Zum [Üben|Begleiter „Zum“ (zu dem) steht davor] nehme ich mir [Zeit|Nomen ohne Begleiter, Probe: die nötige Zeit]. Nach dem [Lesen|Artikel „dem“ steht davor] schreibe ich Stichwörter auf. So kann ich mir viel [merken|Verb nach dem Modalverb „kann“].",
                B_F, frage="Groß oder klein? Ziehe in jede Lücke das Wort in der richtigen Schreibweise (Text: Vor der Arbeit).",
                tauschbar=[("Lernen", "Üben", "Lesen")]))
    a.append(gk("Vor dem [Einschlafen|Artikel „dem“ steht davor] liest Papa uns oft vor. Das [Vorlesen|Artikel „Das“ steht davor] gefällt uns, aber wir müssen leise [sein|Verb nach dem Modalverb „müssen“]. Beim [Zuhören|Begleiter „Beim“ (bei dem) steht davor] fallen uns die Augen zu. Am [Morgen|Begleiter „Am“ (an dem) steht davor] ist das [Aufstehen|Artikel „das“ steht davor] schwer.",
                B_F, frage="Groß oder klein? Ziehe in jede Lücke das Wort in der richtigen Schreibweise (Text: Am Abend).",
                tauschbar=[("Vorlesen", "Zuhören")]))

    # ---------------------------------------------------------------- G
    a.append(mc("Wie kann man „Dass ich die Vögel am Futterhaus beobachte, finde ich spannend.“ sachlicher sagen?",
                "Das Beobachten der Vögel am Futterhaus ist spannend.",
                ["Das beobachten der Vögel am Futterhaus ist spannend.", "Ich beobachte die Vögel am Futterhaus spannend.", "Beobachten ist Futterhaus spannend."], B_G,
                info="Aus dem Verb wird ein Nomen: Das Beobachten (Artikel + nominalisiertes Verb), danach folgt der Genitiv „der Vögel“ und „am Futterhaus“."))
    a.append(kurz("Formuliere als Anweisung: „Man soll die Pflanzen gießen.“ → Das … der Pflanzen ist wichtig.", "Gießen", B_G, gross=True,
                  info="Aus „gießen“ wird mit Artikel das nominalisierte Verb: Das Gießen der Pflanzen ist wichtig."))
    a.append(gk("Das [Messen|Artikel „Das“ steht davor] der Temperatur und das [Notieren|Artikel „das“ steht davor] der Werte gehören zum Versuch.", B_G,
                tauschbar=[("Messen", "Notieren")]))
    a.append(zuordnen("Welche sachliche Formulierung passt zu dem Satz?",
                      [("Dass wir die Zimmer aufräumen, ist nötig.", "Das Aufräumen der Zimmer ist nötig."),
                       ("Dass ich zeichne, entspannt mich.", "Das Zeichnen entspannt mich."),
                       ("Dass die Kinder singen, gefällt allen.", "Das Singen der Kinder gefällt allen.")],
                      B_G, extra=["Das Spielen der Kinder gefällt allen."],
                      info="Aus dem Nebensatz mit „dass“ wird ein Nomen: aufräumen → das Aufräumen, zeichnen → das Zeichnen, singen → das Singen."))
    a.append(gk("Das [Sammeln|Artikel „Das“ steht davor] der Blätter ist die erste Aufgabe. Danach folgt das [Trocknen|Artikel „das“ steht davor] auf Zeitungspapier. Vor dem [Aufkleben|Artikel „dem“ steht davor] muss man die Blätter pressen.", B_G))
    a.append(frei("Forme den Satz mit einem nominalisierten Verb um: „Dass wir miteinander reden, hilft bei Streit.“",
                  "Das Reden miteinander hilft bei Streit.",
                  ["Das Verb „reden“ ist nominalisiert und großgeschrieben (Das Reden).", "Der Satz hat keinen „dass“-Nebensatz mehr.", "Der Sinn bleibt gleich."],
                  2, B_G, info="Aus „dass wir miteinander reden“ wird „das Reden miteinander“. Auch „Das Miteinanderreden“ wäre möglich."))
    return a


def build():
    p = pack(ID, "Deutsch Teil 1b: Verben als Nomen (Nominalisierung)",
             "Nominalisierte Verben: Begleiter erkennen, Verben in der Grundform nominalisieren, mehrteilige Verben, Fallen (Modalverb, zu + Verb), sachlich formulieren. Mit Lernblatt und Übungsaufgaben.",
             lernblatt(), aufgaben(), min_aufgaben=50,
             hinweis="Alle Sätze, Texte und Namen sind selbst ausgedacht, nicht aus dem Deutschbuch, dem Nominalisierungsheft oder dem Aufgabenheft. Bei den Groß-/Kleinschreibungs-Aufgaben zählt jeder Buchstabe: Tippe das Wort genau so, wie es im Satz stehen muss.")
    return [nachlesen(p, {B_A: [L1, L2], B_B: L2, B_C: L2, B_D: L3, B_E: [L4, L2], B_F: [L2, L4], B_G: L5})]


if __name__ == "__main__":
    for p in build():
        print(p["id"], len(p["aufgaben"]), "Aufgaben")
