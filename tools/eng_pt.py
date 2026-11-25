"""Englisch Klasse 6: eigene Probearbeit für die Englischarbeit am 08.12.2026 (Dauer, Aufbau und Punkte der echten Arbeit sind unbekannt).

Alle Aufgaben sind neu, nicht aus den Übungspaketen, aber auf Grundlage derselben Themen (Unit 2) und auf derselben Schwierigkeit.
Vier Teile: A Listening, B Vocabulary, C Grammar (going to, Steigerung), D Writing. Etwa 45 Minuten, ohne Hilfsmittel.
Das Paket hat kein Lernblatt; jede Aufgabe verweist mit „lesen“ auf den passenden Abschnitt eines Übungspakets.
Alle Hörtexte (werden vorgelesen), Sätze, Namen, Schulen und Zahlen sind erfunden (nichts aus Buch, Workbook oder Heft).
"""
from eng_lib import *
from geo_lib import svg_tabelle
from eng_p2e import ant

ID = "englisch-probearbeit"

P2A = "englisch-2a-hoeren"
P2B = "englisch-2b-wortschatz-1"
P2C = "englisch-2c-wortschatz-2"
P2D = "englisch-2d-going-to-1"
P2E = "englisch-2e-going-to-2"
P2F = "englisch-2f-steigerung-1"
P2G = "englisch-2g-steigerung-2"
P2H = "englisch-2h-schreiben"

TEILE = {
    "A": ("Listening", 10),
    "B": ("Vocabulary", 12),
    "C": ("Grammar", 18),
    "D": ("Writing", 8),
}
GESAMT = 48


def abschnitt(k):
    name, pt = TEILE[k]
    return f"Teil {k} – {name} ({pt} Punkte)"


T_TRIP = ("Hi Max, it's Nina. The class trip is on the twentieth of June, not on the thirteenth. "
          "We meet at quarter to eight at the school gate. The bus leaves at eight o'clock and the ticket costs fifteen pounds. "
          "Please bring a sandwich and a drink. See you!")
T_ELLA = ("My name is Ella and I'm in the choir. We practise on Monday and on Thursday. "
          "On Monday the choir starts at half past three and on Thursday at four o'clock. I like the choir because the teacher is kind. "
          "On Friday I'm going to play chess with my friend.")

OAK = {"students": 600, "lessons": 6, "start": (8, 30), "uniform": True}


def tab_oak():
    return svg_tabelle(["Facts", "Oakfield School"],
                       [["Students", "600"], ["Lessons a day", "6"], ["School starts", "8:30"], ["Uniform", "yes"], ["Lunch", "in the canteen"]],
                       spalten_breit=[160, 200])


ALT_OAK = "Tabelle: Oakfield School hat 600 Schüler, 6 Stunden am Tag, Schulbeginn 8:30, Uniform und Mittagessen in der Kantine."


def mit_bild(t, bild, alt):
    t["bild"] = bild
    t["bildAlt"] = alt
    return t


# ------------------------------------------------------------------ Aufgaben
# Jede Aufgabe: (Teil, lesen, Aufgabe). Nummer und Punkte in der Frage setzt build().

def teil_a():
    s = abschnitt("A")
    return [
        ("A", [ref(P2A, "Hörstrategien"), ref(P2A, "Zahlen verstehen"), ref(P2A, "Datum und Ordnungszahlen"), ref(P2A, "Uhrzeiten")],
         luecke("Höre den Text (Anhören) und ergänze die Angaben zum Ausflug (Ziffern).",
                "Date of the trip: {{20|twentieth}} June\nMeeting time: {{7:45|7.45}}\nThe bus leaves at: {{8:00|8.00|8}}\nTicket: £{{15|fifteen}}",
                s, wortbank=False, vorlesen=T_TRIP,
                info="twentieth of June = 20. Juni (nicht thirteenth). quarter to eight = 7:45. eight o'clock = 8:00. fifteen pounds = £15.")),
        ("A", ref(P2A, "Richtig oder falsch? Antworten finden"),
         mit_ton(tf("Höre den Text noch einmal. Die Klasse trifft sich am Bahnhof.", False, s,
                    info="Im Text: „at the school gate“. Die Klasse trifft sich am Schultor."), T_TRIP)),
        ("A", ref(P2A, "Richtig oder falsch? Antworten finden"),
         mit_ton(mc("Was sollen die Kinder mitbringen?", "ein Sandwich und etwas zu trinken",
                    ["Geld für ein Eis", "eine Mütze und Handschuhe", "ein Buch und einen Stift"], s,
                    info="Im Text: „Please bring a sandwich and a drink.“"), T_TRIP)),
        ("A", [ref(P2A, "Hörstrategien"), ref(P2A, "Uhrzeiten")],
         mit_ton(zuordnen("Höre den Text (Anhören). Was macht Ella an welchem Tag?",
                          [("Monday", "Choir at 3:30"), ("Thursday", "Choir at 4:00"), ("Friday", "Chess with a friend")], s,
                          info="Im Text: Monday half past three (3:30), Thursday four o'clock (4:00), on Friday chess with a friend."), T_ELLA)),
        ("A", ref(P2A, "Richtig oder falsch? Antworten finden"),
         mit_ton(mc("Warum mag Ella den Chor?", "Die Lehrerin ist nett.",
                    ["Der Chor ist sehr laut.", "Ihre Freundin singt auch im Chor.", "Sie darf auf der Bühne tanzen."], s,
                    info="Im Text: „because the teacher is kind“ (weil die Lehrerin nett ist)."), T_ELLA)),
    ]


def teil_b():
    s = abschnitt("B")
    return [
        ("B", [ref(P2B, "Bühne, Musical und Gefühle"), ref(P2C, "Dinge und Orte"), ref(P2B, "Schule und Schultag")],
         zuordnen("Ordne die englischen Wörter den deutschen zu.",
                  [("recorder", "Blockflöte"), ("stairs", "Treppe"), ("worksheet", "Arbeitsblatt"), ("awful", "schrecklich")], s,
                  info="recorder = Blockflöte, stairs = Treppe, worksheet = Arbeitsblatt, awful = schrecklich.")),
        ("B", [ref(P2B, "Schule und Schultag"), ref(P2C, "Verben und Wendungen")],
         luecke("Ergänze die Wörter.",
                "Our teacher gives everyone a {{worksheet}}. Please read the text {{aloud}} and {{label}} the picture. Try not to make a {{mistake}}.",
                s, extra=["article", "stage"],
                info="worksheet = Arbeitsblatt, read aloud = laut lesen, label = beschriften, mistake = Fehler.")),
        ("B", ref(P2B, "Bühne, Musical und Gefühle"),
         kurz("Ergänze das Wort: Sam sings really well. He is a very ___ singer. (begabt)", ["talented"], s,
              info="talented = begabt, talentiert.")),
        ("B", ref(P2C, "Possessivpronomen: my und mine"),
         luecke("Ergänze das richtige Wort.",
                "I have a blue bag and Mila has a red bag. The blue bag is {{mine}} and the red bag is {{hers}}.",
                s, extra=["her", "my"],
                info="mine = meins (statt my bag), hers = ihrs (statt her bag). Nach mine und hers steht kein Nomen.")),
        ("B", ref(P2C, "get – ein Wort, viele Bedeutungen"),
         mc_fest("Was bedeutet get in diesem Satz? „It is getting dark.“", ["bekommen", "werden", "holen", "gehen"], "werden", s,
                 info="get + Adjektiv heißt „werden“: It is getting dark = Es wird dunkel.")),
    ]


def teil_c():
    s = abschnitt("C")
    return [
        ("C", [ref(P2D, "So bildest du going to"), ref(P2D, "Wann benutzt man going to?")],
         luecke("Ergänze am, is oder are.",
                "Tonight my brother {{is}} going to cook. My parents {{are}} going to clean the kitchen, and I {{am}} going to set the table.",
                s, extra=["be", "was"],
                info="I am, he/she/it is, we/you/they are. Danach going to + Grundform.")),
        ("C", ref(P2D, "Die Verneinung"),
         mc("Welcher Satz ist richtig?", "She isn't going to watch TV tonight.",
            ["She not going to watch TV tonight.", "She doesn't going to watch TV tonight.", "She isn't going to watches TV tonight."], s,
            info="Verneinung: is not / isn't + going to + Grundform. Kein doesn't, und das Verb bleibt in der Grundform (watch).")),
        ("C", ref(P2E, "Fragen mit going to"),
         kurz("Bilde eine Frage mit going to: Nina / play tennis / tomorrow", ["Is Nina going to play tennis tomorrow"], s,
              info="Frage: Is + Subjekt + going to + Grundform. Is Nina going to play tennis tomorrow?")),
        ("C", ref(P2E, "Kurzantworten"),
         kurz("Antworte mit einer Kurzantwort (nein): Are your friends going to come?", ant(False, "they"), s,
              info="No, they aren't. (oder: No, they are not.) Bei der Kurzantwort wird das Hilfsverb are wiederholt, nicht going to.")),
        ("C", ref(P2E, "Fragewörter"),
         mc("Welche Frage ist richtig?", "What are you going to do on Saturday?",
            ["What do you going to do on Saturday?", "What are you going to doing on Saturday?", "What you are going to do on Saturday?"], s,
            info="Fragewort + are + Subjekt + going to + Grundform: What are you going to do?")),
        ("C", [ref(P2F, "Kurze Adjektive: -er und -est"), ref(P2F, "Lange Adjektive: more und most"), ref(P2F, "Rechtschreibung der Formen")],
         luecke("Ergänze die richtige Form des Adjektivs.",
                "My bag is {{heavier}} than your bag. This book is {{more interesting}} than that book. February is the {{shortest}} month of the year.",
                s, extra=["heavyer", "interestinger"],
                info="heavy → heavier (y wird zu i). interesting ist lang: more interesting. short → shortest (Superlativ mit the).")),
        ("C", ref(P2G, "as … as und not as … as"),
         mc("Mia ist 150 cm groß. Tom ist auch 150 cm groß. Welcher Satz ist richtig?", "Mia is as tall as Tom.",
            ["Mia is taller than Tom.", "Mia is as taller as Tom.", "Mia is tall as Tom."], s,
            info="Gleich groß: as + Grundform + as. Nach as … as steht die Grundform (tall), nicht taller.")),
        ("C", ref(P2F, "Unregelmäßige Formen"),
         kurz("Ergänze die Steigerung: This pizza is good, but that pizza is ___ than this one.", ["better"], s,
              info="good – better – the best. Das sind unregelmäßige Formen (nicht gooder).")),
        ("C", ref(P2G, "Der Superlativ im Satz: of und in"),
         kurz("Ergänze den Superlativ: Mount Everest is the ___ mountain in the world. (high)", ["highest"], s,
              info="high – higher – the highest. Der Superlativ steht mit the und mit in oder of.")),
        ("C", ref(P2G, "Welche Form? Typische Fehler"),
         mc("Welcher Satz hat einen Fehler?", "My dog is more fast than your dog.",
            ["This film is more exciting than that film.", "Ben is the oldest of the three boys.", "Our school is not as big as that school."], s,
            info="fast ist ein kurzes Adjektiv: faster, nicht more fast. Bei langen Adjektiven (exciting) nimmt man more.")),
        ("C", ref(P2D, "So bildest du going to"),
         reihenfolge("Bringe die Wörter in die richtige Reihenfolge.", ["Lena", "is", "going", "to", "buy", "a", "present"], s,
                     info="Subjekt – is – going to – Grundform – Rest: Lena is going to buy a present.")),
        ("C", ref(P2G, "Welche Form? Typische Fehler"),
         tf("Der Satz „My bike is more old than yours.“ ist richtig.", False, s,
            info="old ist kurz: older. Richtig: My bike is older than yours.")),
        ("C", ref(P2D, "Die Verneinung"),
         luecke("Ergänze die verneinte Form.",
                "My sister {{isn't|is not}} going to come. We {{aren't|are not}} going to wait for her.",
                s, extra=["don't", "am not"],
                info="Verneinung mit going to: is not (isn't) bei he/she/it, are not (aren't) bei we/you/they.")),
    ]


def teil_d():
    s = abschnitt("D")
    return [
        ("D", ref(P2H, "Sätze verbinden: and, but, because, so"),
         kurz("Verbinde die beiden Sätze mit because: „I like Fridays.“ „We have art.“",
              ["I like Fridays because we have art", "I like Fridays, because we have art"], s,
              info="because = weil. Es steht vor dem Grund: I like Fridays because we have art.")),
        ("D", ref(P2H, "Mein Schultag"),
         reihenfolge("Bringe die Sätze in die richtige Reihenfolge.",
                     ["First, I have breakfast.", "Then I pack my bag.", "After that I walk to school.", "Finally, I meet my friends at the gate."], s,
                     info="first, then, after that, finally zeigen die Reihenfolge.")),
        ("D", [ref(P2H, "Mein Schultag"), ref(P2H, "Meine Schule mit einer englischen Schule vergleichen"), ref(P2H, "Pläne und E-Mails")],
         mit_bild(frei("Schreibe einen Text mit 6 bis 8 Sätzen: Beschreibe kurz deinen Schultag (mit Uhrzeiten) und vergleiche deine Schule mit Oakfield School (Tabelle). Schreibe auch, was du nach der Schule vorhast (going to).",
                       "I get up at half past six. After that I go to school by bus. School starts at five to eight at my school, so it starts earlier than at Oakfield School. "
                       "My school is smaller than Oakfield School, but we have six lessons too. Oakfield School has a uniform, but we don't wear a uniform. "
                       "After school I'm going to play football with my friends.",
                       ["Der Text hat 6 bis 8 vollständige Sätze mit Satzanfang groß und Punkt.",
                        "Der Schultag wird mit richtigen Uhrzeiten oder mit first, then, after that beschrieben.",
                        "Es kommt ein richtiger Komparativ mit than vor (zum Beispiel smaller than, earlier than).",
                        "Es kommt not as … as oder but für einen Gegensatz vor.",
                        "Ein Satz sagt mit am/is/are + going to + Grundform, was du nach der Schule vorhast.",
                        "Rechtschreibung stimmt, bei he/she/it steht -s."],
                       6, s, info=None), tab_oak(), ALT_OAK)),
    ]


def aufgaben_mit_meta():
    out = []
    for f in (teil_a, teil_b, teil_c, teil_d):
        for k, lesen, t in f():
            out.append((k, lesen, t))
    return out


def build(pakete):
    byid = {p["id"]: p for p in pakete}

    def titel_da(paket_id, titel):
        return paket_id in byid and any(s["titel"] == titel for s in byid[paket_id].get("lernblatt", []))

    A = []
    summen = {}
    for n, (k, lesen, t) in enumerate(aufgaben_mit_meta(), 1):
        assert t["abschnitt"].startswith(f"Teil {k} "), (k, t["abschnitt"])
        pt = punkte_von(t)
        summen[k] = summen.get(k, 0) + pt
        t["frage"] = f"Aufgabe {n}: {t['frage']}" + (f" ({pt} Punkte)" if pt > 1 else "")
        for r in (lesen if isinstance(lesen, list) else [lesen]):
            assert titel_da(r["paket"], r["titel"]), f"Verweis ins Leere: {r}"
        t["lesen"] = lesen
        A.append(t)
    assert summen == {k: v[1] for k, v in TEILE.items()}, summen
    assert sum(summen.values()) == GESAMT == sum(punkte_von(t) for t in A)
    for t in A:
        k = t["abschnitt"][5]
        assert f"({summen[k]} Punkte)" in t["abschnitt"], t["abschnitt"]
    teile_txt = ", ".join(f"{k} {TEILE[k][0]} {TEILE[k][1]}" for k in "ABCD")
    p = pack(ID, "Englisch Klasse 6: Probearbeit (Listening, Vocabulary, Grammar, Writing)",
             f"Eigene Probearbeit mit {GESAMT} Punkten in vier Teilen ({teile_txt}), 45 Minuten mit Timer, Buch und Heft zu. Alle Aufgaben sind neu. Wo Punkte fehlen, geh in das passende Übungspaket zurück.",
             None, A,
             hinweis="Das ist nicht die Klassenarbeit deines Lehrers, sondern eine eigene Probearbeit unter Prüfungsbedingungen. Dauer, Aufbau und Punkte der echten Arbeit sind nicht bekannt, deshalb sind Aufbau, Punkte und Zeit selbst festgelegt. "
                     "Die Hörtexte sind selbst geschrieben (Knopf „Anhören“, du darfst jeden Text zweimal hören). Lege Buch, Heft und Vokabelheft weg und vergleiche erst am Ende mit den Lösungen. "
                     "Den Text in Teil D bewertest du mit einem Elternteil nach den Kriterien. Welche Note es für welche Punktzahl gibt, bestimmt dein Lehrer.")
    p["ueben"] = False   # kein Übungsmodus, nur proben wie in der Schule
    return p


if __name__ == "__main__":
    import eng_p2a, eng_p2b, eng_p2c, eng_p2d, eng_p2e, eng_p2f, eng_p2g, eng_p2h
    pakete = []
    for m in (eng_p2a, eng_p2b, eng_p2c, eng_p2d, eng_p2e, eng_p2f, eng_p2g, eng_p2h):
        pakete += m.build()
    p = build(pakete)
    print(p["id"], len(p["aufgaben"]), "Aufgaben", sum(punkte_von(t) for t in p["aufgaben"]), "Punkte")
