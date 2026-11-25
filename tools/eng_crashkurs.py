"""Englisch Klasse 6: Crashkurs (das Wichtigste kurz gefasst) für die Englischarbeit am 08.12.2026.

Der letzte Blick am Tag vor der Arbeit: kurzes Lernblatt (kein neuer Stoff, nur Auswahl und Verdichtung der Lernblätter
der Übungspakete in eigenen Worten), Tipps, Checkliste und ein Blitz-Check mit neuen Kurzaufgaben.
Anweisung: siehe crashkurs-baustein.md im Projekt. Alle Beispiele sind erfunden (nichts aus Buch oder Heft).
"""
import difflib
import re

from eng_lib import *   # noqa: F401,F403
from geo_lib import _gaps  # noqa: F401

S = "Blitz-Check"
ID = "englisch-crashkurs"

T_NUTZEN = "So nutzt du den Crashkurs"
T_HOER = "Hören: Zahlen, Zeiten, Daten"
T_WORT = "Wortschatz: Schule und Bühne"
T_GET = "get und Possessivpronomen"
T_GT1 = "going to: Plan, Aussage, Verneinung"
T_GT2 = "going to: Fragen und Kurzantworten"
T_ST1 = "Steigerung: -er, -est, more, most"
T_ST2 = "Vergleiche: than, as … as, of und in"
T_SCHR = "Schreiben: Schule, Schultag, E-Mail"
T_TIPPS = "Tipps für die Arbeit"
T_CHECK = "Checkliste für morgen"
THEMEN = [T_HOER, T_WORT, T_GET, T_GT1, T_GT2, T_ST1, T_ST2, T_SCHR]


def lernblatt():
    return [
        lb(T_NUTZEN,
           "Das ist dein **letzter Blick** am Tag vor der Arbeit: einmal in Ruhe lesen (etwa 10 Minuten), danach den **Blitz-Check** machen (etwa 5 Minuten). "
           "Hier steht nichts Neues. Wenn du unsicher bist, geh in das passende Übungspaket zurück."),
        lb(T_HOER,
           "- Lies die Aufgabe **vorher** und überlege, welche Wörter kommen.\n"
           "- **thirTEEN** (13) ist hinten betont, **THIRty** (30) vorn. Genauso fifteen und fifty.\n"
           "- Schreibe **forty** ohne u und **eighty** mit einem t.\n"
           "- **half past seven** ist 7:30, **quarter past** ist Viertel nach, **quarter to** ist Viertel vor.\n"
           "- Datum: first, second, third, **fifth**, **twelfth**, **twentieth**.\n"
           "- Achte auf **but** und **not**: Sie ändern oft die Aussage.\n"
           "- Beim zweiten Hören prüfst du deine Antworten.",
           merke="-teen hinten betont, -ty vorn. half past seven = 7:30."),
        lb(T_WORT,
           "- Schule: **uniform**, **canteen**, **lessons**, **break**, **registration**, **worksheet**, **mistake**.\n"
           "- Bühne: **audition**, **stage**, **concert**, **theatre**, **recorder**, **nervous**, **talented**.\n"
           "- Aus Verben werden Personen mit **-er**: sing – **singer**, dance – **dancer**, run – **runner**.\n"
           "- Kleine Wörter: **a bit** (ein bisschen), **a few** (ein paar), **You should …** (Du solltest …).\n"
           "- Beim Schreiben zählt jeder Buchstabe: **theatre** (nicht theater), **dialogue** (nicht dialog).\n"
           "- Lerne mit eigenen Sätzen statt mit einzelnen Wörtern.",
           merke="Verb + -er = Person. a few = ein paar, a bit = ein bisschen."),
        lb(T_GET,
           "- **get** heißt je nach Satz **bekommen**, **holen**, **gelangen** oder **werden**: It gets dark early in winter.\n"
           "- **get up** = aufstehen, **get ready** = sich fertig machen, **get on / off** = ein- / aussteigen.\n"
           "- **my** steht vor einem Nomen: This is my bag. **mine** steht allein: This bag is mine.\n"
           "- Die Reihe: mine, **yours**, his, **hers**, **ours**, **theirs**.\n"
           "- Nach yours, hers, ours, theirs steht **kein Apostroph**: The bag is theirs.",
           merke="get = bekommen, holen, gelangen, werden. my + Nomen, mine allein."),
        lb(T_GT1,
           "- Mit **going to** sagst du, was du vorhast oder was man schon kommen sieht: Look at the clouds! It's going to rain.\n"
           "- Das Muster: **Subjekt + am / is / are + going to + Grundform**: She is going to play.\n"
           "- Nach to bleibt das Verb unverändert (nicht plays, nicht playing).\n"
           "- Verneinung: **am / is / are + not**. He **isn't** going to play. They **aren't** going to play. I'm not going to play.\n"
           "- Kein do: nicht I don't going to sing.\n"
           "- Zeitangaben wie **tomorrow**, **tonight**, **next week** stehen meist am Satzende.",
           merke="Subjekt + am / is / are + going to + Grundform. Verneinung: not hinter be."),
        lb(T_GT2,
           "- Bei einer **Ja-Nein-Frage** steht **am / is / are** vor dem Subjekt: Is Mia going to play tennis? Kein do, kein does.\n"
           "- **Fragewörter** stehen ganz vorn: **What**, **Where**, **When**, **Who**, **Why**, **How**. What are you going to do?\n"
           "- Fragst du nach dem Subjekt, bleibt die Wortstellung: **Who** is going to sing?\n"
           "- Die **Kurzantwort** hat kein going to: Yes, I **am**. No, he **isn't**. No, they **aren't**.\n"
           "- Bei Yes gibt es keine Kurzform: Yes, I am (nicht Yes, I'm).\n"
           "- Bist du unsicher, schreibe erst die Aussage und forme sie dann um.",
           merke="Frage: be + Subjekt + going to + Grundform. Kurzantwort ohne going to."),
        lb(T_ST1,
           "- Die drei Stufen: **Grundform** tall, **Komparativ** taller, **Superlativ** the tallest.\n"
           "- **Kurze Adjektive** (meist eine Silbe) bekommen **-er** und **-est**: old – older – the oldest.\n"
           "- Endet das Adjektiv auf **-e**, hängst du nur -r und -st an: nice – nicer – the nicest.\n"
           "- Kurzer Vokal und ein Konsonant: **doppelt** schreiben: big – bigger – the biggest. Das y wird zu i: happy – happier.\n"
           "- **Lange Adjektive** bekommen **more** und **the most**: beautiful – more beautiful – the most beautiful.\n"
           "- Unregelmäßig: **good** – **better** – **the best**, **bad** – **worse** – **the worst**.",
           merke="-er / -est bei kurzen, more / most bei langen Adjektiven. Nie more taller."),
        lb(T_ST2,
           "- Zwei Dinge vergleichst du mit dem Komparativ und **than**: Tom is taller than Ben.\n"
           "- Das **the** gehört zum Superlativ: Tom is **the tallest**. Danach steht **of** (mehrere) oder **in** (Gruppe, Ort): the best of all, the best singer in the school.\n"
           "- **as … as** (so … wie) braucht die **Grundform**: Tom is as tall as Ben.\n"
           "- **not as … as** heißt weniger: Ben is not as tall as Tom.\n"
           "- Dasselbe sagst du so: Mia is older than Tom. = Tom is not as old as Mia.",
           merke="than → Komparativ. the … of / in → Superlativ. as … as → Grundform."),
        lb(T_SCHR,
           "- Ein Text hat **Einleitung**, **Hauptteil** und **Schluss**.\n"
           "- Schule: **My school is called** … / **There are** 450 students. / **We have** six lessons.\n"
           "- Schultag: **first**, **then**, **after that**, **finally** und **at** plus Uhrzeit.\n"
           "- Nach einer Zeitangabe bleibt die Reihenfolge normal: In the afternoon I play football.\n"
           "- Bei he, she, it bekommt das Verb ein **-s**: She gets up.\n"
           "- Verbinde mit **and** (und), **but** (aber), **because** (weil), **so** (deshalb).\n"
           "- Beim Vergleich der Schulen: **smaller than**, **not as big as**.",
           merke="first, then, after that. he/she/it: Verb mit -s. Bindewörter: and, but, because, so."),
        lb(T_TIPPS,
           "- Lies jede Aufgabe **zweimal**.\n"
           "- **Listening:** erst die Aufgabe lesen, dann zuhören.\n"
           "- **Vocabulary:** Jeder Buchstabe zählt.\n"
           "- **Grammar:** Bei going to gilt der **Dreifach-Check**: be da? going to da? Grundform danach?\n"
           "- Bei der Steigerung zuerst nach **than**, **the** und **as … as** suchen.\n"
           "- **Writing:** einfache, richtige Sätze schreiben und am Ende alles noch einmal lesen."),
        lb(T_CHECK,
           "**Ich kann:**\n\n"
           "- Zahlen, Uhrzeiten und Daten verstehen.\n"
           "- Wörter zu Schule und Bühne richtig schreiben.\n"
           "- get und die Possessivpronomen benutzen.\n"
           "- Pläne mit going to sagen, verneinen und erfragen.\n"
           "- Kurzantworten ohne going to geben.\n"
           "- Adjektive steigern.\n"
           "- Schulen vergleichen (than, as … as, of / in).\n"
           "- einen Text über Schule und Schultag schreiben."),
    ]


# ------------------------------------------------------------------ Blitz-Check

def aufgaben():
    """Die Blitz-Check-Aufgaben. Rückgabe: (Aufgaben, Belege). Belege: je Aufgabe Zeichenfolgen, die im Crashkurs-Abschnitt stehen müssen."""
    A, B = [], []

    def neu(t, lesen, belege):
        t["lesen"] = lesen
        A.append(t)
        B.append((t["frage"][:50], lesen if isinstance(lesen, list) else [lesen], belege))

    neu(mit_ton(mc("Blitz-Check, Hören: Höre zu (Anhören). Wie viele Minuten dauert es bis zum Bus?", "40", ["14", "4", "44"], S,
                   info="Im Text: „forty minutes“. forty (vorn betont) ist 40, fourteen (hinten betont) wäre 14."),
                "The next bus comes in forty minutes."),
        T_HOER, ["thirteen (13) ist hinten betont, thirty (30) vorn", "schreibe forty ohne u"])
    neu(mc("Blitz-Check, Uhrzeit: Welche Uhrzeit ist „half past nine“?", "9:30", ["8:30", "9:15", "9:45"], S,
           info="half past nine heißt 30 Minuten nach neun. Das ist 9:30 Uhr."),
        T_HOER, ["half past seven ist 7:30"])
    neu(mc("Blitz-Check, Wortschatz: Welches Wort ist richtig geschrieben? On Saturday we are going to the …", "theatre", ["theater", "theatr", "teatre"], S,
           info="theatre schreibt man im britischen Englisch mit -re am Ende. Das Wort ist ein Merkwort."),
        T_WORT, ["theatre (nicht theater)"])
    neu(luecke("Blitz-Check, Possessivpronomen: Ergänze mine, hers oder ours.",
               "These books are not {{mine}}. They are {{hers}}.", S, extra=["her", "my"],
               info="Nach mine und hers steht kein Nomen. my und her stehen dagegen vor einem Nomen."),
        T_GET, ["mine steht allein", "kein apostroph"])
    neu(mc("Blitz-Check, get: Was bedeutet get in „It gets cold in winter“?", "werden", ["bekommen", "holen", "gehen"], S,
           info="get + Adjektiv bedeutet werden: Es wird kalt im Winter."),
        T_GET, ["bekommen, holen, gelangen oder werden"])
    neu(mc("Blitz-Check, going to: Welcher Satz ist richtig?", "My cousin isn't going to come.",
           ["My cousin doesn't going to come.", "My cousin isn't going to comes.", "My cousin not going to come."], S,
           info="Verneinung: is not (isn't) vor going to. Kein do, und das Verb bleibt in der Grundform."),
        T_GT1, ["kein do", "nach to bleibt das verb unverändert"])
    neu(kurz("Blitz-Check, Frage: Bilde die Frage mit going to: they / watch a film / tonight",
             ["Are they going to watch a film tonight"], S,
             info="Frage: Are + Subjekt + going to + Grundform. Kein do."),
        T_GT2, ["steht am / is / are vor dem subjekt", "kein do, kein does"])
    neu(tf("Blitz-Check, Kurzantwort: Auf „Is Ben going to swim?“ ist „Yes, he is going to.“ die richtige Kurzantwort.", False, S,
           info="Die Kurzantwort hat kein going to. Richtig ist: Yes, he is."),
        T_GT2, ["die kurzantwort hat kein going to"])
    neu(kurz("Blitz-Check, Steigerung: Ergänze den Komparativ: Anna is ___ than Lea. (happy)", ["happier"], S,
             info="Bei Adjektiven auf -y wird das y zu i: happy – happier."),
        T_ST1, ["das y wird zu i"])
    neu(mc("Blitz-Check, as … as: Lea und Anna sind beide 12 Jahre alt. Welcher Satz ist richtig?", "Lea is as old as Anna.",
           ["Lea is older than Anna.", "Lea is as older as Anna.", "Lea is not as old than Anna."], S,
           info="Gleich alt: as + Grundform + as. Nach as … as steht nie der Komparativ."),
        T_ST2, ["as … as (so … wie) braucht die grundform"])
    neu(luecke("Blitz-Check, Steigerung: Ergänze die Formen.",
               "The blue bag is {{cheaper}} than the red bag. It is also {{the most}} beautiful bag in the shop.", S, extra=["more cheap"],
               info="cheap ist kurz und bekommt -er. beautiful ist lang und bekommt the most."),
        [T_ST1, T_ST2], ["kurze adjektive (meist eine silbe) bekommen -er und -est", "lange adjektive bekommen more und the most"])
    neu(mc("Blitz-Check, Text: Welches Wort passt? We have a test tomorrow, ___ I am going to learn tonight.", "so", ["but", "or", "because"], S,
           info="so bedeutet deshalb und steht vor der Folge. but wäre ein Gegensatz und because steht vor dem Grund."),
        T_SCHR, ["and (und), but (aber), because (weil), so (deshalb)"])
    return A, B


# ------------------------------------------------------------------ Prüfungen

EIGENE_FETT = {"Ich kann", "Ich kann:", "letzter Blick", "Blitz-Check", "zweimal", "Listening:", "Vocabulary:", "Grammar:", "Writing:", "Dreifach-Check",
               "vorher", "Grundform", "Komparativ", "Superlativ", "of", "in", "y", "i", "-e", "doppelt", "Subjekt", "Ja-Nein-Frage"}


def woerter_split(text):
    return len(re.sub(r"\*\*", "", text).split())


def woerter_re(text):
    return len(re.findall(r"[\wÄÖÜäöüß%−–„“'-]+", re.sub(r"\*\*", "", text)))


def norm(s):
    return re.sub(r"\s+", " ", s.replace("**", "")).lower()


def pruefe_lernblatt(LB):
    titel = [s["titel"] for s in LB]
    assert len(set(titel)) == len(titel), titel
    assert titel[0] == T_NUTZEN and titel[-2:] == [T_TIPPS, T_CHECK] and titel[1:-2] == THEMEN, titel
    for s in LB:
        assert "#" not in s["text"] and "|---" not in s["text"], s["titel"]
        assert not re.search(r"(?<![*\w])\*(?![*])", s["text"]), f"Kursivschrift? {s['titel']}"
    je = []
    for s in LB:
        if s["titel"] in THEMEN:
            m = s.get("merke") or ""
            assert m, f"merke fehlt: {s['titel']}"
            lo = min(woerter_re(s["text"]), woerter_split(s["text"]))
            hi = max(woerter_re(s["text"] + " " + m), woerter_split(s["text"] + " " + m))
            assert 60 <= lo and hi <= 120, (s["titel"], lo, hi)
            je.append((s["titel"], woerter_split(s["text"]), woerter_split(s["text"] + " " + m)))
    text_summe = sum(woerter_split(s["text"]) for s in LB)
    gesamt = sum(woerter_re(s["titel"] + " " + s["text"] + " " + (s.get("merke") or "")) for s in LB)
    assert 800 <= text_summe <= 1000, text_summe
    assert gesamt <= 1000, gesamt
    chk = [s for s in LB if s["titel"] == T_CHECK][0]["text"]
    assert chk.startswith("**Ich kann:**\n\n"), chk[:30]
    return je, text_summe, gesamt


def pruefe_fakten(LB, pakete):
    """Jedes fett gedruckte Fachwort steht auch in den Lernblättern der Übungspakete (außer den eigenen Ankerwörtern)."""
    quelle = norm("\n".join(s["titel"] + "\n" + s["text"] + "\n" + (s.get("merke") or "") for p in pakete for s in p.get("lernblatt", []) if p["id"] != ID))
    fehlt = []
    for s in LB:
        for fett in re.findall(r"\*\*(.+?)\*\*", s["text"]):
            f = fett.strip()
            if f in EIGENE_FETT:
                continue
            if norm(f) not in quelle:
                fehlt.append((f, s["titel"]))
    assert not fehlt, f"Fachwörter nicht in den Übungspaketen: {fehlt}"


def pruefe_aufgaben(LB, A, B, pakete):
    assert 8 <= len(A) <= 12, len(A)
    assert not any(t["typ"] == "frei" for t in A)
    assert all(t["abschnitt"] == S for t in A)
    titel = {s["titel"]: norm(s["text"] + "\n" + (s.get("merke") or "")) for s in LB}
    arten = {}
    for t in A:
        arten[t["typ"]] = arten.get(t["typ"], 0) + 1
        for x in (t["lesen"] if isinstance(t["lesen"], list) else [t["lesen"]]):
            assert x in titel and x in THEMEN, f"lesen: Abschnitt „{x}“ gibt es nicht im Crashkurs"
        ohne = re.sub(r"(\d)\.", r"\1", t["info"])
        assert 1 <= len(re.findall(r"[.!?](?:\s|$)", ohne)) <= 2, ("info soll 1 bis 2 Sätze haben", t["info"])
        if t["typ"] == "mc":
            r = t["richtig"] if isinstance(t["richtig"], list) else [t["richtig"]]
            falsch = [a for i, a in enumerate(t["antworten"]) if i not in r]
            assert max(len(t["antworten"][i]) for i in r) <= 1.4 * max(len(a) for a in falsch), ("richtige Antwort auffällig lang", t["antworten"])
            assert len(set(t["antworten"])) == len(t["antworten"])
    for frage, lesen, belege in B:
        text = " ".join(titel[x] for x in lesen)
        for b in belege:
            assert norm(b) in text, f"Beleg „{b}“ fehlt in {lesen} (Aufgabe: {frage})"
    for t in A:
        if t["typ"] == "luecke" and "wortbank" in t:
            erste = [g.split("|")[0].strip() for g in _gaps(t["text"])]
            extra = [w for w in t["wortbank"] if w not in erste]
            assert 1 <= len(extra) <= 3, extra
    if pakete is not None:
        alt = [(p["id"], t["frage"], t.get("text", "")) for p in pakete if p["id"] != ID for t in p["aufgaben"]]
        keys = {f"{f}|{x}" for _, f, x in alt}
        for t in A:
            assert f"{t['frage']}|{t.get('text', '')}" not in keys, f"Aufgabe schon vorhanden: {t['frage']}"
            for pid, f, x in alt:
                r = difflib.SequenceMatcher(None, t["frage"] + " " + t.get("text", ""), f + " " + x).ratio()
                assert r < 0.8, f"zu ähnlich ({r:.2f}) zu {pid}: {f}\n   neu: {t['frage']}"
    return arten


def build(pakete=None):
    LB = lernblatt()
    A, B = aufgaben()
    je, text_summe, gesamt = pruefe_lernblatt(LB)
    if pakete is not None:
        pruefe_fakten(LB, pakete)
    arten = pruefe_aufgaben(LB, A, B, pakete)
    p = pack(ID, "Englisch Klasse 6: Crashkurs (das Wichtigste kurz gefasst)",
             f"Das Wichtigste kurz gefasst, für den letzten Blick vor der Arbeit: Lernblatt, Checkliste und ein Blitz-Check mit {len(A)} Kurzaufgaben.",
             LB, A,
             hinweis="Kein neuer Stoff: Alles steht auch in den Lernblättern der Übungspakete. Die Beispiele und der Hörtext sind selbst ausgedacht, nicht aus dem Schulbuch oder Workbook.")
    nachlesen(p, {S: [x for x in THEMEN if any(x in b[1] for b in B)]})
    p["probe"] = False
    print(f"Crashkurs: {len(LB)} Abschnitte, {text_summe} Wörter Text ({gesamt} mit Titeln und merke), {len(A)} Blitz-Check-Aufgaben {arten}")
    for titel, w, wm in je:
        print(f"   {w:4d} ({wm:4d} mit merke)  {titel}")
    return p


if __name__ == "__main__":
    import eng_p2a, eng_p2b, eng_p2c, eng_p2d, eng_p2e, eng_p2f, eng_p2g, eng_p2h, eng_pt
    pakete = []
    for m in (eng_p2a, eng_p2b, eng_p2c, eng_p2d, eng_p2e, eng_p2f, eng_p2g, eng_p2h):
        pakete += m.build()
    pakete.append(eng_pt.build(pakete))
    build(pakete)
