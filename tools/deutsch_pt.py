"""Deutsch Klasse 6: eigene Probearbeit für die Deutscharbeit am 02.12.2026 (Dauer, Aufbau und Diktattext der echten Arbeit sind unbekannt).

Alle Aufgaben sind neu, nicht aus den Übungspaketen, aber auf Grundlage derselben Regeln und auf derselben Schwierigkeit.
Drei Teile: A Nominalisierung, B Satzreihe, Satzgefüge und Komma, C Diktat und Rechtschreibung. Etwa 45 Minuten, ohne Hilfsmittel.
Das Paket hat kein Lernblatt; jede Aufgabe verweist mit „lesen“ auf den passenden Abschnitt eines Übungspakets.
Alle Sätze, Texte und Namen sind erfunden (nichts aus Buch oder Heft).
"""
from deutsch_lib import *
from deutsch_lib import _gaps  # noqa: F401

ID = "deutsch-probearbeit"

P1A = "deutsch-1a-nomen-begleiter"
P1B = "deutsch-1b-nominalisierte-verben"
P1C = "deutsch-1c-nominalisierte-adjektive-superlativ"
P2A = "deutsch-2a-satzreihe"
P2B = "deutsch-2b-satzgefuege"
P2C = "deutsch-2c-satzreihe-oder-satzgefuege"
P3A = "deutsch-3a-rechtschreibung-1"
P3B = "deutsch-3b-rechtschreibung-2"
P3C = "deutsch-3c-diktat-ueben"

# Überschriften der Teile mit ihren Punkten (werden in build() gegen die Aufgaben geprüft)
TEILE = {
    "A": ("Nominalisierung: groß oder klein", 23),
    "B": ("Satzreihe, Satzgefüge und Komma", 14),
    "C": ("Diktat und Rechtschreibung", 14),
}
GESAMT = 51


def abschnitt(k):
    name, pt = TEILE[k]
    return f"Teil {k} – {name} ({pt} Punkte)"


def mit_punkten(t, n):
    t["punkte"] = n
    return t


DIKTAT = ("Am Sonntag backt Mama mit uns einen Kuchen. "
          "Beim Rühren darf jeder etwas Eigenes beitragen, denn das Schönste ist das gemeinsame Backen. "
          "Ole holt die Eier, die im Keller liegen. "
          "Danach riecht es im Haus nach etwas Süßem.")


# ------------------------------------------------------------------ Aufgaben
# Jede Aufgabe: (Schwierigkeit L/M/S, lesen, Aufgabe). Nummer und Punkte in der Frage setzt build().

def teil_a():
    s = abschnitt("A")
    return [
        ("L", [ref(P1A, "Nomen und ihre Begleiter"), ref(P1A, "Groß oder klein bei Nomen?")],
         gk("Nach dem [Frühstück|Begleiter „dem“ (nach dem) steht davor] packt [Ole|Name einer Person] seine [Tasche|Pronomen „seine“ steht davor] und geht zum [Bus|Begleiter „zum“ (zu dem)].",
            s)),
        ("L", ref(P1B, "Verben als Nomen"),
         mc("Welcher Satz ist richtig geschrieben?",
            "Beim Schwimmen hat Tim viel Spaß.",
            ["Beim schwimmen hat Tim viel Spaß.", "Beim Schwimmen hat Tim viel spaß."], s,
            info="„Beim“ steht vor „Schwimmen“, das Verb ist nominalisiert und wird großgeschrieben. „viel Spaß“: Spaß ist ein Nomen.")),
        ("M", [ref(P1B, "Die Begleiter erkennen"), ref(P1A, "Nomen ohne Begleiter: die Probe")],
         gk("Zum [Lernen|Begleiter „zum“ (zu dem)] braucht Mia [Ruhe|Nomen ohne Begleiter, Probe: die große Ruhe]. Beim [Rechnen|Begleiter „beim“ (bei dem)] hilft ihr der [Taschenrechner|Artikel „der“ steht davor].",
            s,
                tauschbar=[("Lernen", "Rechnen")])),
        ("M", [ref(P1C, "Adjektive als Nomen"), ref(P1C, "Indefinitpronomen")],
         gk("Ole hat etwas [Besonderes|Signalwort „etwas“ steht davor] erlebt und erzählt [alles|Indefinitpronomen, bleibt klein] [Interessante|Signalwort „alles“ steht davor].",
            s)),
        ("S", ref(P1C, "Superlativ mit „am“ oder nominalisiert?"),
         gk("Im Zoo läuft der Gepard am [schnellsten|Superlativ mit „am“ bleibt klein]. Das [Schönste|Artikel „das“ steht davor] aber sind die [Pinguine|Artikel „die“ steht davor].",
            s)),
        ("M", [ref(P1B, "Die Begleiter erkennen"), ref(P1C, "Indefinitpronomen")],
         mit_punkten(mc("Welche Wörter schreibt man in diesem Satz groß? wir hoffen auf ein baldiges wiedersehen und wünschen euch alles gute. (mehrere Antworten sind richtig)",
                        ["wiedersehen", "gute"], ["baldiges", "hoffen"], s,
                        info="Groß: Wiedersehen (Begleiter „ein baldiges“) und Gute (Signalwort „alles“). „baldiges“ ist ein Adjektiv vor einem Nomen und bleibt klein, „hoffen“ ist ein Verb."), 2)),
        ("S", [ref(P1B, "Verben als Nomen"), ref(P1C, "Adjektive als Nomen")],
         mit_punkten(kurz("Schreibe den Satz richtig auf: „beim tauchen sah ole etwas buntes.“", "Beim Tauchen sah Ole etwas Buntes.", s, gross=True,
                          info="„Beim Tauchen“ ist ein nominalisiertes Verb. „etwas Buntes“ ist ein nominalisiertes Adjektiv. „Ole“ ist ein Name."), 2)),
        ("M", ref(P1B, "Fallen: Verb bleibt Verb"),
         mc("Welcher Satz ist richtig geschrieben?",
            "Das Laufen im Wald macht Mia Spaß.",
            ["Das laufen im Wald macht Mia Spaß.", "Mia will im Wald Laufen gehen."], s,
            info="„Das Laufen“ ist ein nominalisiertes Verb mit Artikel. In „laufen gehen“ bleibt „laufen“ ein Verb und wird kleingeschrieben.")),
        ("M", ref(P1B, "Fallen: Verb bleibt Verb"),
         luecke("Verb oder Nomen? Ziehe in jede Lücke das Wort in der richtigen Schreibweise.",
                "Ole kann gut {{schwimmen}}. Das {{Schwimmen}} macht ihm Freude. Er will morgen wieder {{schwimmen}} gehen.", s,
                extra=[], gross=True,
                info="Im ersten und dritten Satz ist „schwimmen“ ein Verb (kann gut schwimmen, schwimmen gehen) und wird kleingeschrieben. Im zweiten Satz steht der Artikel „Das“ davor, das Verb ist nominalisiert.")),
    ]


def teil_b():
    s = abschnitt("B")
    return [
        ("L", ref(P2A, "Hauptsatz und Satzreihe"),
         mc("Welche Aussage passt zu dem Satz „Es regnet, aber wir gehen trotzdem hinaus.“?",
            "Eine Satzreihe: zwei Hauptsätze, durch „aber“ verbunden.",
            ["Ein Satzgefüge: ein Hauptsatz und ein Nebensatz.", "Ein einfacher Satz mit nur einem Verb.", "Ein Satzgefüge mit einem Relativsatz."], s,
            info="Beide Teile könnten allein stehen und haben die Personalform an zweiter Stelle (regnet, gehen). „aber“ ist eine nebenordnende Konjunktion. Also ist es eine Satzreihe.")),
        ("M", [ref(P2A, "Das Komma in der Satzreihe"), ref(P2B, "Das Komma im Satzgefüge")],
         kommas("Wir bleiben zu Hause {,} weil es regnet. Ole liest ein Buch {,} denn er mag Geschichten. Mia malt ein Bild {?} und ihr Bruder baut mit Klötzen.", s,
                info="Vor „weil“ (Nebensatz) und vor „denn“ (Satzreihe) steht immer ein Komma. Vor „und“ zwischen zwei Hauptsätzen darf das Komma wegfallen.")),
        ("M", ref(P2B, "Relativsätze"),
         kommas("Der Hund {,} der im Garten spielt {,} gehört unserem Nachbarn.", s,
                info="Der Relativsatz „der im Garten spielt“ steht mitten im Hauptsatz und wird vorn und hinten mit einem Komma abgetrennt.")),
        ("L", ref(P2B, "Unterordnende Konjunktionen"),
         mc("Ich bleibe zu Hause. Ich bin krank. Welche Konjunktion macht daraus ein Satzgefüge?",
            "weil", ["und", "aber", "denn"], s,
            info="„weil“ ist unterordnend und leitet einen Nebensatz ein: Ich bleibe zu Hause, weil ich krank bin. „und“, „aber“ und „denn“ verbinden Hauptsätze zu einer Satzreihe.")),
        ("S", ref(P2C, "Satzreihe oder Satzgefüge? Die Verbprobe"),
         zuordnen("Satzreihe oder Satzgefüge? Ordne zu.",
                  [("Ich lese, denn das Buch ist spannend.", "Satzreihe"), ("Ich lese, weil das Buch spannend ist.", "Satzgefüge"),
                   ("Mia singt, und Ole spielt Gitarre.", "Satzreihe"), ("Ole freut sich, dass Mia singt.", "Satzgefüge")],
                  s, info="Verbprobe: Steht die Personalform im zweiten Teil an zweiter Stelle (denn das Buch ist …, und Ole spielt …), ist es eine Satzreihe. Steht sie am Ende (weil das Buch spannend ist, dass Mia singt), ist es ein Nebensatz.")),
        ("M", ref(P2C, "Umformen und Satzbaupläne"),
         mit_punkten(kurz("Verbinde die Sätze mit „weil“: Ole bleibt zu Hause. Er ist krank.",
                          ["Ole bleibt zu Hause, weil er krank ist.", "Weil er krank ist, bleibt Ole zu Hause."], s, gross=True,
                          info="Der Nebensatz mit „weil“ hat die Personalform am Ende (er krank ist). Zwischen Hauptsatz und Nebensatz steht ein Komma. Der Nebensatz darf auch vorn stehen."), 2)),
        ("M", ref(P2B, "Satzbaupläne"),
         mc("Welcher Satzbauplan passt zu „Ich freue mich, dass du kommst.“?",
            "Hs , Ns", ["Ns , Hs", "Hs , Hs", "Hs , Ns , Hs"], s,
            info="„Ich freue mich“ ist der Hauptsatz (Hs), „dass du kommst“ der Nebensatz (Ns). Der Hauptsatz steht vorn, dann folgt ein Komma und der Nebensatz.")),
    ]


def teil_c():
    s = abschnitt("C")
    t = frei("Diktat: Ein Elternteil liest den Text vor (oder tippe auf „Anhören“). Schreibe ihn auf und vergleiche erst danach mit der Musterlösung.",
             DIKTAT,
             ["Die Nominalisierungen sind großgeschrieben (Beim Rühren, etwas Eigenes, Das Schönste, das gemeinsame Backen, etwas Süßem).",
              "Die Kommas vor „denn“ und vor und nach dem Relativsatz stehen richtig.",
              "Wörter wie Keller, Eier und Kuchen sind richtig geschrieben.",
              "Satzanfänge und Nomen sind großgeschrieben, Verben und Adjektive kleingeschrieben."],
             6, s, info="Zähle deine Fehler. Ordne jeden Fehler einer Fehlerart zu und übe sie im passenden Übungspaket.")
    t["vorlesen"] = {"text": DIKTAT, "sprache": SPRACHE}
    return [
        ("M", [ref(P3C, "So gehst du beim Diktat vor"), ref(P1B, "Verben als Nomen")], t),
        ("M", [ref(P3A, "Doppelkonsonanten, ck und tz"), ref(P3B, "Ableiten: e oder ä, eu oder äu"), ref(P3B, "Verlängern: b/p, d/t, g/k")],
         luecke("Schreibe die Wörter richtig auf.",
                "Die {{Katze}} sitzt im {{Keller}}, und die {{Mäuse}} suchen den {{Weg}}.", s,
                extra=["Kaze", "Käller", "Meuse", "Wek"], gross=True,
                info="Kat-ze (tz statt zz), Keller (kein verwandtes Wort mit a, ll nach kurzem Vokal), Mäuse – Maus (äu), Weg – Wege (g).")),
        ("L", ref(P3A, "s, ss oder ß?"),
         mc("Welches Wort ist richtig geschrieben? Ole … heute sein Zimmer aufräumen.",
            "muss", ["mus", "muß"], s,
            info="müs-sen: Die erste Silbe ist geschlossen, der Vokal ist kurz, der Laut zischt. Also steht ss: er muss.")),
        ("M", ref(P3B, "Welche Strategie hilft?"),
         zuordnen("Welche Strategie hilft dir bei dem Wort?",
                  [("Handtuch", "zerlegen und verlängern"), ("Bäume", "ableiten"), ("Korb", "verlängern")],
                  s, info="Handtuch: erst zerlegen (Hand + Tuch), dann Hand verlängern (Hände). Bäume: ableiten (Baum). Korb: verlängern (Körbe).")),
    ]


def aufgaben_mit_meta():
    out = []
    for k, f in zip("ABC", (teil_a, teil_b, teil_c)):
        for schw, lesen, t in f():
            out.append((k, schw, lesen, t))
    return out


def build(pakete):
    byid = {p["id"]: p for p in pakete}

    def titel_da(paket_id, titel):
        return paket_id in byid and any(s["titel"] == titel for s in byid[paket_id].get("lernblatt", []))

    meta = aufgaben_mit_meta()
    A = []
    summen = {}
    for n, (k, schw, lesen, t) in enumerate(meta, 1):
        assert schw in ("L", "M", "S")
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
    teile_txt = ", ".join(f"{k} {TEILE[k][0]} {TEILE[k][1]}" for k in "ABC")
    p = pack(ID, "Deutsch Klasse 6: Probearbeit (Nominalisierung, Satzreihe und Satzgefüge, Diktat)",
             f"Eigene Probearbeit mit {GESAMT} Punkten in drei Teilen ({teile_txt}), 45 Minuten mit Timer, Buch und Heft zu. Alle Aufgaben sind neu. Wo Punkte fehlen, geh in das passende Übungspaket zurück.",
             None, A,
             hinweis="Das ist nicht die Klassenarbeit deines Lehrers, sondern eine eigene Probearbeit unter Prüfungsbedingungen. Dauer, Aufbau und Diktattext der echten Arbeit sind nicht bekannt, deshalb sind Aufbau, Punkte und Zeit selbst festgelegt. "
                     "Lege Buch, Heft und Regelheft weg und vergleiche erst am Ende mit den Lösungen. Für das Diktat liest ein Elternteil vor (oder tippe auf „Anhören“). Welche Note es für welche Punktzahl gibt, bestimmt dein Lehrer.")
    p["ueben"] = False   # kein Übungsmodus, nur proben wie in der Schule
    return p
