"""Deutsch Klasse 6: Crashkurs (das Wichtigste kurz gefasst) für die Deutscharbeit am 02.12.2026.

Der letzte Blick am Tag vor der Arbeit: kurzes Lernblatt (kein neuer Stoff, nur Auswahl und Verdichtung der Lernblätter
der Übungspakete in eigenen Worten), Tipps, Checkliste und ein Blitz-Check mit neuen Kurzaufgaben.
Anweisung: siehe crashkurs-baustein.md im Projekt. Alle Beispiele sind erfunden (nichts aus Buch oder Heft).
"""
import difflib
import re

from deutsch_lib import *   # noqa: F401,F403
from deutsch_lib import _gaps  # noqa: F401

S = "Blitz-Check"
ID = "deutsch-crashkurs"

T_NUTZEN = "So nutzt du den Crashkurs"
T_NOM = "Nomen und Begleiter"
T_VERB = "Nominalisierte Verben"
T_ADJ = "Nominalisierte Adjektive"
T_SUP = "Superlativ: am oder das?"
T_KOMMA1 = "Satzreihe und Komma"
T_KOMMA2 = "Satzgefüge, Relativsatz und Komma"
T_RS1 = "Silben, Doppelkonsonanten und s-Laute"
T_RS2 = "i, ie, h und Doppelvokale"
T_RS3 = "Verlängern, Zerlegen, Ableiten"
T_TIPPS = "Tipps für die Arbeit"
T_CHECK = "Checkliste für morgen"
THEMEN = [T_NOM, T_VERB, T_ADJ, T_SUP, T_KOMMA1, T_KOMMA2, T_RS1, T_RS2, T_RS3]


def lernblatt():
    return [
        lb(T_NUTZEN,
           "Das ist dein **letzter Blick** am Tag vor der Arbeit: einmal in Ruhe lesen (etwa 10 Minuten), danach den **Blitz-Check** machen (etwa 5 Minuten). "
           "Hier steht nichts Neues. Wenn du unsicher bist, geh in das passende Übungspaket zurück. "
           "Das Diktat und die Aufgaben der echten Arbeit kennen wir nicht, die Regeln aber schon."),
        lb(T_NOM,
           "- **Nomen** schreibt man groß, Namen auch.\n"
           "- Vor einem Nomen steht oft ein **Begleiter**: **Artikel** (der, ein), **Adjektiv** (kleine), **Pronomen** (mein), **Präposition** (mit, auf) oder **Zahlwort** (zwei).\n"
           "- Verschmolzene Wörter sind auch Begleiter: im, beim, zum, zur, vom, am, ins (in dem, bei dem, zu dem …).\n"
           "- Steht kein Begleiter da, hilft die **Artikel-Adjektiv-Probe**: Geht „der große …“, ist es ein Nomen (der große Hunger).\n"
           "- Bei gern, schnell, heute geht die Probe nicht, diese Wörter schreibt man klein.",
           merke="Erst den Begleiter suchen, dann die Probe machen."),
        lb(T_VERB,
           "- Ein **Verb** in der **Grundform** wird zum Nomen, wenn ein **Begleiter** davorsteht: beim Lesen, zum Essen, das Schwimmen, ihr Lachen. Man nennt das **Nominalisierung**.\n"
           "- Bei mehrteiligen Verben bleibt die Grundform zusammen: aufgeben, das Aufgeben.\n"
           "- **Falle:** Nach einem **Modalverb** (wollen, können, müssen) und nach **zu** bleibt das Verb klein: Wir wollen spielen. Es gibt viel zu entdecken.\n"
           "- Vergleiche: Sie kann lachen (Verb). Ihr Lachen steckt an (nominalisiert).",
           merke="Nach Begleiter groß, nach Modalverb und nach „zu“ klein."),
        lb(T_ADJ,
           "- Ein **Adjektiv**, das wie ein Nomen gebraucht wird, ist **nominalisiert** und wird großgeschrieben: das Neue, im Dunkeln, aufs Neue.\n"
           "- Begleiter sind **Artikel**, **Präposition** (im, aufs, für …) und **Indefinitpronomen** (etwas, nichts, alles, viel): etwas Schönes, nichts Neues, alles Gute, viel Schönes.\n"
           "- Das Indefinitpronomen selbst schreibt man klein.\n"
           "- **Falle:** Folgt noch ein Nomen, bleibt das Adjektiv klein: ein furchtloser Held. Auch bei „Er singt laut.“ bleibt es klein.",
           merke="Indefinitpronomen plus Adjektiv: groß. Folgt ein Nomen: klein."),
        lb(T_SUP,
           "- **am schönsten, am spannendsten** (Superlativ mit „am“) schreibt man **klein**. Die Frage lautet **Wie?** Mia läuft am schnellsten.\n"
           "- **das Schönste, das Spannendste** (nominalisiert) schreibt man **groß**. Davor steht ein Artikel. Die Frage lautet **Was?** Das Spannendste war der Schluss.\n"
           "- Auch mit Zusatz davor schreibt man groß: mit Abstand das Gruseligste.\n"
           "- Typische Fälle: am liebsten und am besten schreibt man klein.",
           merke="Wie? am …sten, klein. Was? das …ste, groß."),
        lb(T_KOMMA1,
           "- Ein **Hauptsatz** kann allein stehen. Die **Personalform** steht an zweiter Stelle.\n"
           "- Eine **Satzreihe** besteht aus zwei oder mehr Hauptsätzen. Es gibt **nebenordnende Konjunktionen**: und, oder, aber, sondern, denn, doch.\n"
           "- Vor **aber, sondern, denn, doch** steht **immer** ein Komma: Ich lese, denn das Buch ist spannend.\n"
           "- Vor **und** und **oder** darf das Komma **wegfallen**.\n"
           "- Ohne Konjunktion steht immer ein Komma. Verbindet „und“ nur Wörter (Äpfel und Birnen), steht keins.",
           merke="Komma immer vor aber, sondern, denn, doch. Vor und und oder darf es fehlen."),
        lb(T_KOMMA2,
           "- Ein **Satzgefüge** besteht aus **Hauptsatz** und **Nebensatz**. Im Nebensatz steht die Personalform am **Ende**: Ole bleibt zu Hause, weil er krank ist.\n"
           "- Es gibt **unterordnende Konjunktionen**: weil, da, obwohl, damit, wenn, dass, sodass, nachdem, während, bevor, indem.\n"
           "- Zwischen Hauptsatz und Nebensatz steht **immer ein Komma**. Steht der Nebensatz vorn, folgt das Komma hinter ihm.\n"
           "- Steht er in der Mitte, setzt man **zwei Kommas**. Das gilt auch für den **Relativsatz** (der, die, das): Der Hund, der gern bellt, gehört Mia.",
           merke="Satzgefüge: immer ein Komma. Mitten im Satz: zwei Kommas."),
        lb(T_RS1,
           "- Beim **Schwingen** sprichst du in Silben. Eine Silbe ist **offen** (endet auf einen Vokal: Ho-se) oder **geschlossen** (endet auf einen Konsonanten: Kan-ne).\n"
           "- **Doppelkonsonant:** erste Silbe geschlossen und nur ein Konsonant zu hören (Kan-ne). Zwei verschiedene Konsonanten: nicht verdoppeln (Hil-fe). Statt kk schreibt man **ck**, statt zz **tz**.\n"
           "- **s-Laut:** offene Silbe und summend: s (Ha-se). Offene Silbe und zischend: ß (Stra-ße). Geschlossene Silbe: ss (Tas-se).",
           merke="s summt, ß zischt in offener Silbe, ss in geschlossener Silbe."),
        lb(T_RS2,
           "- **ie:** oft bei offener erster Silbe und langem i (Zie-le, Wie-se). Bei geschlossener Silbe steht **i** (Kin-der).\n"
           "- Merkwörter: mir, dir, wir, ihr, ihm, ihn, ihnen. Verben auf -ieren schreibt man mit ie (probieren).\n"
           "- **h:** Das silbenöffnende h hörst du beim Verlängern am Anfang der zweiten Silbe (zie-hen, Mü-he).\n"
           "- Vor l, m, n, r steht ein h, das man nicht hört. Das sind Merkwörter: Zahl, Wohnung, Lehrer.\n"
           "- Doppelvokale sind Merkwörter: See, Meer, Boot, Haar.",
           merke="ie bei offener Silbe, i bei geschlossener Silbe. Das h beim Verlängern hören."),
        lb(T_RS3,
           "- **Verlängern:** Bei b/p, d/t und g/k am Wortende verlängerst du: Korb – Körbe, Hund – Hunde, Zug – Züge. Nomen in die Mehrzahl, Verben in die Grundform.\n"
           "- **Zerlegen:** Bei zusammengesetzten Wörtern trennst du die Teile und verlängerst den unklaren Teil: Land|karte – Länder.\n"
           "- **Ableiten:** Gibt es ein verwandtes Wort mit a oder au, schreibt man **ä** oder **äu**: Bäume (Baum), Häuser (Haus). Gibt es keins, schreibt man e oder eu: Keller, Leuchte.",
           merke="Unsicher? Verlängern, zerlegen oder ableiten."),
        lb(T_TIPPS,
           "- Lies jede Aufgabe **zweimal**.\n"
           "- **Diktat:** zuhören, Satz für Satz schreiben, unsichere Wörter **einkreisen**, am Ende mit einer Strategie prüfen.\n"
           "- Bei groß oder klein erst den **Begleiter** suchen, dann die Probe machen.\n"
           "- **am** plus Superlativ bleibt klein.\n"
           "- Bei Kommas hilft die **Verbprobe**: Steht die Personalform am Ende, ist es ein Nebensatz und davor steht ein Komma.\n"
           "- Lies am Ende alles noch einmal Wort für Wort."),
        lb(T_CHECK,
           "**Ich kann:**\n\n"
           "- Begleiter von Nomen erkennen und die Artikel-Adjektiv-Probe machen.\n"
           "- nominalisierte Verben und Adjektive großschreiben.\n"
           "- am plus Superlativ und das plus Superlativ unterscheiden.\n"
           "- Satzreihe und Satzgefüge erkennen und die Kommas setzen.\n"
           "- einen Relativsatz mit Kommas abtrennen.\n"
           "- Wörter mit Verlängern, Zerlegen und Ableiten klären.\n"
           "- ein Diktat schreiben und unsichere Wörter prüfen."),
    ]


# ------------------------------------------------------------------ Blitz-Check

def aufgaben():
    """Die Blitz-Check-Aufgaben. Rückgabe: (Aufgaben, Belege). Belege: je Aufgabe Zeichenfolgen, die im Crashkurs-Abschnitt stehen müssen."""
    A, B = [], []

    def neu(t, lesen, belege):
        t["lesen"] = lesen
        A.append(t)
        B.append((t["frage"][:50], lesen if isinstance(lesen, list) else [lesen], belege))

    neu(gk("Zum [Backen|Begleiter „zum“ (zu dem)] braucht Papa [Mehl|Nomen ohne Begleiter, Probe: das feine Mehl].", S,
           frage="Blitz-Check, groß oder klein: Ziehe in jede Lücke das Wort in der richtigen Schreibweise."),
        [T_VERB, T_NOM], ["beim Lesen, zum Essen", "Artikel-Adjektiv-Probe"])
    neu(mc("Blitz-Check, Adjektiv: Welche Schreibweise stimmt im Satz über den Sommer?",
           "Im Sommer gibt es viel Schönes zu erleben.",
           ["Im Sommer gibt es viel schönes zu erleben.", "Im Sommer gibt es viel Schönes zu Erleben."], S,
           info="Nach „viel“ ist das Adjektiv nominalisiert und wird großgeschrieben. Nach „zu“ bleibt das Verb klein."),
        T_ADJ, ["indefinitpronomen (etwas, nichts, alles, viel)", "etwas schönes, nichts neues"])
    neu(tf("Blitz-Check, Superlativ: In dem Satz „Der Hase läuft am schnellsten.“ schreibt man „schnellsten“ klein.", True, S,
           info="Die Frage „Wie läuft der Hase?“ führt zu „am schnellsten“. Superlative mit „am“ schreibt man klein."),
        T_SUP, ["am schönsten, am spannendsten", "die frage lautet wie?"])
    neu(mc("Blitz-Check, Satzreihe: Welches Wort passt? Mia ist müde, … sie geht noch nicht ins Bett.",
           "aber", ["weil", "dass", "damit"], S,
           info="„aber“ ist eine nebenordnende Konjunktion und verbindet zwei Hauptsätze. „weil“, „dass“ und „damit“ leiten Nebensätze ein."),
        T_KOMMA1, ["nebenordnende konjunktionen: und, oder, aber, sondern, denn, doch"])
    neu(kommas("Ich lerne heute {,} denn morgen schreiben wir eine Arbeit. Mia lernt mit {?} und Ole liest.", S,
               info="Vor „denn“ steht immer ein Komma. Vor „und“ zwischen zwei Hauptsätzen darf es wegfallen.",
               frage="Blitz-Check, Komma: Wähle bei jeder Lücke „Komma“ oder „kein Komma“."),
        T_KOMMA1, ["vor aber, sondern, denn, doch", "vor und und oder darf das komma wegfallen"])
    neu(kurz("Blitz-Check, Satzgefüge: Verbinde mit „obwohl“: Mia schwimmt im See. Das Wasser ist kalt.",
             ["Mia schwimmt im See, obwohl das Wasser kalt ist.", "Obwohl das Wasser kalt ist, schwimmt Mia im See."], S, gross=True,
             info="Im Nebensatz mit „obwohl“ steht die Personalform am Ende. Zwischen Hauptsatz und Nebensatz steht immer ein Komma."),
        T_KOMMA2, ["im nebensatz steht die personalform am ende", "zwischen hauptsatz und nebensatz steht immer ein komma", "obwohl"])
    neu(kommas("Das Buch {,} das auf dem Tisch liegt {,} gehört Ole.", S,
               info="Der Relativsatz steht mitten im Hauptsatz. Deshalb steht davor und dahinter ein Komma.",
               frage="Blitz-Check, Relativsatz: Wähle bei jeder Lücke „Komma“ oder „kein Komma“."),
        T_KOMMA2, ["relativsatz (der, die, das)", "mitte, setzt man zwei kommas"])
    neu(mc("Blitz-Check, s-Laut: Welches Wort ist richtig geschrieben? Zum Nachtisch gibt es …",
           "Süßigkeiten", ["Süsigkeiten", "Süssigkeiten"], S,
           info="süß – sü-ße: Die erste Silbe ist offen und der s-Laut zischt. Dann schreibt man ß."),
        T_RS1, ["offene silbe und zischend: ß (stra-ße)"])
    neu(mc("Blitz-Check, ie oder i: Welches Wort ist richtig geschrieben? Wir singen gern …",
           "Lieder", ["Lider", "Lihder"], S,
           info="Lie-der: Die erste Silbe ist offen und das i klingt lang. Dann schreibt man oft ie."),
        T_RS2, ["ie: oft bei offener erster silbe und langem i"])
    neu(mc("Blitz-Check, Verlängern: Welches Wort ist richtig geschrieben? Der … fährt in den Bahnhof.",
           "Zug", ["Zuk", "Zuck"], S,
           info="Zug – Züge: Beim Verlängern hörst du ein g. Deshalb schreibt man auch am Wortende g."),
        T_RS3, ["zug – züge", "verlängern"])
    neu(mc("Blitz-Check, Ableiten: Welches Wort ist richtig geschrieben? Im Dorf stehen viele alte …",
           "Häuser", ["Heuser", "Hauser"], S,
           info="Häuser – Haus: Es gibt ein verwandtes Wort mit au, also schreibt man äu."),
        T_RS3, ["häuser (haus)", "ableiten"])
    neu(tf("Blitz-Check, Verb: Der Satz „Wir wollen draußen Spielen.“ ist richtig geschrieben.", False, S,
           info="Nach einem Modalverb (wollen) bleibt das Verb klein. Richtig ist: Wir wollen draußen spielen."),
        T_VERB, ["modalverb (wollen, können, müssen)", "bleibt das verb klein"])
    return A, B


# ------------------------------------------------------------------ Prüfungen

EIGENE_FETT = {"Ich kann", "Ich kann:", "letzter Blick", "Blitz-Check", "zweimal", "einkreisen", "Wie?", "Was?", "klein", "groß", "ie", "i", "h", "ä", "äu", "ck", "tz", "ß",
               "Verbprobe", "Falle:", "Doppelkonsonant:", "s-Laut:", "Schwingen", "am", "Diktat:", "Begleiter", "Verlängern:", "Zerlegen:", "Ableiten:", "ie:", "h:",
               "Hauptsatz", "Nebensatz", "Satzgefüge", "Satzreihe", "Relativsatz", "Personalform", "offen", "geschlossen", "Nomen", "Adjektiv", "Pronomen",
               "Präposition", "Zahlwort", "Artikel", "Grundform", "Verb", "Modalverb", "zu", "aber, sondern, denn, doch", "und", "immer", "immer ein Komma", "Ende",
               "zwei Kommas", "wegfallen", "nominalisiert", "Nominalisierung"}


def woerter_split(text):
    return len(re.sub(r"\*\*", "", text).split())


def woerter_re(text):
    return len(re.findall(r"[\wÄÖÜäöüß%−–„“-]+", re.sub(r"\*\*", "", text)))


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
    # „Ich kann:“ als eigener Absatz vor der Liste, Tipps und Checkliste vorhanden
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
    p = pack(ID, "Deutsch Klasse 6: Crashkurs (das Wichtigste kurz gefasst)",
             f"Das Wichtigste kurz gefasst, für den letzten Blick vor der Arbeit: Lernblatt, Checkliste und ein Blitz-Check mit {len(A)} Kurzaufgaben.",
             LB, A,
             hinweis="Kein neuer Stoff: Alles steht auch in den Lernblättern der Übungspakete. Die Beispiele sind selbst ausgedacht, nicht aus dem Deutschbuch oder Aufgabenheft.")
    nachlesen(p, {S: [x for x in THEMEN if any(x in b[1] for b in B)]})
    p["probe"] = False
    print(f"Crashkurs: {len(LB)} Abschnitte, {text_summe} Wörter Text ({gesamt} mit Titeln und merke), {len(A)} Blitz-Check-Aufgaben {arten}")
    for titel, w, wm in je:
        print(f"   {w:4d} ({wm:4d} mit merke)  {titel}")
    return p


if __name__ == "__main__":
    build()
