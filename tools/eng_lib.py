"""Hilfen für die Englisch-Lernpakete (Klasse 6, Written Exam Unit 2 „A school day“, Arbeit am 08.12.2026).

Baut auf geo_lib.py und gesch_lib.py auf. Alle Sätze, Texte und Namen sind selbst geschrieben, nichts aus Buch, Heft oder Arbeitsblatt
(das Repository ist öffentlich). Grundlage der Inhalte ist das Faktenblatt im Projekt (englisch-klasse-6-unit-2-fakten.md).

Wichtig für die App (index.html, normText): Es wird kleingeschrieben verglichen, am Ende stehen Satzzeichen nicht im Weg, typografische
Apostrophe zählen wie ein gerader Apostroph. Bei Englisch setzen wir KEIN „nachsicht“: Die Schreibweise muss stimmen. Deshalb:
- Verkürzte und volle Formen (isn't / is not, I'm / I am) als Alternativen anbieten.
- Lücken so bauen, dass nur ein Wort oder alle gleichwertigen Wörter (a|b) richtig sind.
- Lücken mit Verbformen: „schreibe ohne Kurzform“ in die Frage, wenn der Apostroph stören würde.
"""
import re

import geo_lib
from geo_lib import mc, tf, zuordnen, reihenfolge, frei, lb, check_pack, _gaps   # noqa: F401
from gesch_lib import _normalisiere, punkte_von, nachlesen                       # noqa: F401

FACH = "Englisch"
GRUPPE = "Englischarbeit 08.12.2026"
TERMIN = "2026-12-08"
SPRACHE = "en-GB"


# ------------------------------------------------------------------ Aufgaben-Bausteine (mit vorlesen, auswahl, ohne nachsicht)

def kurz(frage, richtig, abschnitt, info=None, tipp=None, vorlesen=None, einheit=None):
    t = geo_lib.kurz(frage, richtig, abschnitt, einheit=einheit, info=info, tipp=tipp)
    if vorlesen:
        t["vorlesen"] = {"text": vorlesen, "sprache": SPRACHE}
    return t


def luecke(frage, text, abschnitt, extra=(), info=None, tipp=None, wortbank=True, auswahl=None, vorlesen=None):
    if wortbank and not auswahl:   # jedes Wort der Wortbank wird nur einmal gebraucht
        ersten = [g.split("|")[0].strip().lower() for g in _gaps(text)]
        assert len(set(ersten)) == len(ersten), f"gleiche Antwort in zwei Lücken mit Wortbank: {ersten}"
    t = geo_lib.luecke(frage, text, abschnitt, extra=extra, info=info, tipp=tipp, wortbank=bool(wortbank and not auswahl))
    if auswahl:
        t["auswahl"] = list(auswahl)
    if vorlesen:
        t["vorlesen"] = {"text": vorlesen, "sprache": SPRACHE}
    return t


def mc_fest(frage, optionen, richtig, abschnitt, info=None, tipp=None):
    """Auswahl mit fester Reihenfolge der Antworten (z. B. am / is / are), die richtige steht dort, wo sie hingehört."""
    t = geo_lib.mc(frage, richtig, [o for o in optionen if o != richtig], abschnitt, info=info, tipp=tipp)
    t["antworten"] = list(optionen)
    t["richtig"] = list(optionen).index(richtig)
    t["mischen"] = False
    return t


def mit_ton(t, text):
    """Hörtext (wird in der App vorgelesen) an eine beliebige Aufgabe hängen."""
    t["vorlesen"] = {"text": text, "sprache": SPRACHE}
    return t


# ------------------------------------------------------------------ Steigerung: Formen werden berechnet und gegen eine feste Liste geprüft

VOKALE = "aeiou"
UNREGELMAESSIG = {"good": ("better", "best"), "bad": ("worse", "worst")}
# Wörter, die in der Steigerung den Endkonsonanten verdoppeln (kurzer Vokal + ein Konsonant)
VERDOPPELN = {"big", "thin", "hot", "fat", "sad", "wet"}
# Adjektive auf -y (y → i)
Y_WOERTER = {"happy", "funny", "pretty", "easy", "heavy", "busy", "lucky", "noisy", "tidy", "silly", "friendly", "sunny", "rainy", "windy", "healthy", "lazy", "angry", "early", "dirty", "tasty"}
# Lange Adjektive: more / most
LANG = {"beautiful", "expensive", "interesting", "intelligent", "famous", "boring", "difficult", "careful", "popular", "dangerous", "exciting", "modern",
        "comfortable", "important", "delicious", "terrible", "fantastic", "serious", "nervous", "talented", "scary", "brilliant", "awful"}


def steigerung(adj):
    """(Komparativ, Superlativ) als Text, z. B. ('taller', 'tallest') oder ('more beautiful', 'most beautiful')."""
    a = adj.lower()
    if a in UNREGELMAESSIG:
        return UNREGELMAESSIG[a]
    if a in LANG:
        return ("more " + a, "most " + a)
    if a in VERDOPPELN:
        return (a + a[-1] + "er", a + a[-1] + "est")
    if a in Y_WOERTER:
        return (a[:-1] + "ier", a[:-1] + "iest")
    if a.endswith("e"):
        return (a + "r", a + "st")
    return (a + "er", a + "est")


# feste Kontrolliste (von Hand geschrieben), gegen die steigerung() geprüft wird
KONTROLLE = {
    "tall": ("taller", "tallest"), "small": ("smaller", "smallest"), "short": ("shorter", "shortest"), "long": ("longer", "longest"),
    "old": ("older", "oldest"), "young": ("younger", "youngest"), "fast": ("faster", "fastest"), "slow": ("slower", "slowest"),
    "cheap": ("cheaper", "cheapest"), "strong": ("stronger", "strongest"), "high": ("higher", "highest"), "low": ("lower", "lowest"),
    "cold": ("colder", "coldest"), "warm": ("warmer", "warmest"), "dark": ("darker", "darkest"), "light": ("lighter", "lightest"),
    "clean": ("cleaner", "cleanest"), "new": ("newer", "newest"), "loud": ("louder", "loudest"), "quiet": ("quieter", "quietest"),
    "great": ("greater", "greatest"), "tidy": ("tidier", "tidiest"), "fresh": ("fresher", "freshest"), "hard": ("harder", "hardest"),
    "nice": ("nicer", "nicest"), "large": ("larger", "largest"), "late": ("later", "latest"), "close": ("closer", "closest"),
    "wide": ("wider", "widest"), "safe": ("safer", "safest"), "brave": ("braver", "bravest"), "rude": ("ruder", "rudest"),
    "big": ("bigger", "biggest"), "thin": ("thinner", "thinnest"), "hot": ("hotter", "hottest"), "fat": ("fatter", "fattest"),
    "sad": ("sadder", "saddest"), "wet": ("wetter", "wettest"),
    "happy": ("happier", "happiest"), "funny": ("funnier", "funniest"), "pretty": ("prettier", "prettiest"), "easy": ("easier", "easiest"),
    "heavy": ("heavier", "heaviest"), "busy": ("busier", "busiest"), "lucky": ("luckier", "luckiest"), "noisy": ("noisier", "noisiest"),
    "silly": ("sillier", "silliest"), "friendly": ("friendlier", "friendliest"), "sunny": ("sunnier", "sunniest"), "rainy": ("rainier", "rainiest"),
    "windy": ("windier", "windiest"), "lazy": ("lazier", "laziest"), "angry": ("angrier", "angriest"), "dirty": ("dirtier", "dirtiest"), "tasty": ("tastier", "tastiest"),
    "beautiful": ("more beautiful", "most beautiful"), "expensive": ("more expensive", "most expensive"), "interesting": ("more interesting", "most interesting"),
    "intelligent": ("more intelligent", "most intelligent"), "famous": ("more famous", "most famous"), "boring": ("more boring", "most boring"),
    "difficult": ("more difficult", "most difficult"), "careful": ("more careful", "most careful"), "popular": ("more popular", "most popular"),
    "dangerous": ("more dangerous", "most dangerous"), "exciting": ("more exciting", "most exciting"), "modern": ("more modern", "most modern"),
    "comfortable": ("more comfortable", "most comfortable"), "important": ("more important", "most important"), "delicious": ("more delicious", "most delicious"),
    "scary": ("scarier", "scariest"),
    "good": ("better", "best"), "bad": ("worse", "worst"),
}
LANG.discard("scary")   # scary: -y-Adjektiv
Y_WOERTER.add("scary")
for _a, _f in KONTROLLE.items():
    assert steigerung(_a) == _f, (_a, steigerung(_a), _f)


def komp(adj):
    return steigerung(adj)[0]


def sup(adj):
    return steigerung(adj)[1]


def sup_mit_the(adj):
    return "the " + steigerung(adj)[1]


# ------------------------------------------------------------------ going to: Formen von be

BE = {"I": "am", "you": "are", "he": "is", "she": "is", "it": "is", "we": "are", "they": "are"}
BE_KURZ = {"I": "I'm", "you": "you're", "he": "he's", "she": "she's", "it": "it's", "we": "we're", "they": "they're"}
NICHT_KURZ = {"I": "I'm not", "you": "you aren't", "he": "he isn't", "she": "she isn't", "it": "it isn't", "we": "we aren't", "they": "they aren't"}


def be_of(subj):
    """Form von be zu einem Subjekt (Pronomen, Name oder Gruppe mit and / Plural)."""
    s = subj.strip()
    if s in BE:
        return BE[s]
    low = s.lower()
    if " and " in low or low.startswith(("the children", "my parents", "the girls", "the boys", "the students", "our friends", "my friends", "the teachers", "the pupils", "the twins", "my cousins", "my brothers", "my sisters", "the kids", "our parents", "the dogs", "the cats", "my classmates", "my grandparents", "our neighbours")):
        return "are"
    return "is"


def gt_voll(subj, rest, neg=False):
    """'Mia is going to play tennis.' / 'Mia is not going to play tennis.' (ohne Satzzeichen am Ende)."""
    b = be_of(subj)
    return f"{subj} {b}{' not' if neg else ''} going to {rest}"


def gt_varianten(subj, rest, neg=False, satz_anfang=True):
    """Alle gleichwertigen Schreibweisen als Liste für kurz: volle Form, Kurzform mit not, Kurzform mit 's / 're."""
    b = be_of(subj)
    out = []
    out.append(f"{subj} {b}{' not' if neg else ''} going to {rest}")
    if not neg:
        if subj in BE_KURZ:
            out.append(f"{BE_KURZ[subj]} going to {rest}")
        elif b == "is":
            out.append(f"{subj}'s going to {rest}")
        else:
            pass
    else:
        if subj in NICHT_KURZ:
            out.append(f"{NICHT_KURZ[subj]} going to {rest}")
            if subj != "I":
                out.append(f"{BE_KURZ[subj]} not going to {rest}")
        else:
            out.append(f"{subj} {'isn' if b == 'is' else 'aren'}'t going to {rest}")
    seen, res = set(), []
    for x in out:
        if x not in seen:
            seen.add(x)
            res.append(x)
    return res


def frage_gt(subj, rest, wh=None):
    """Frage mit be going to: 'Is Mia going to play tennis?' / 'What is Mia going to play?' (rest ohne Fragewort)."""
    b = be_of(subj)
    if wh:
        return f"{wh} {b} {subj} going to {rest}?"
    return f"{b.capitalize()} {subj} going to {rest}?"


# ------------------------------------------------------------------ Paket

def pack(id, titel, beschreibung, lernblatt, aufgaben, hinweis=None, min_aufgaben=None, info_pflicht=True):
    """Wie gesch_lib.pack, aber Fach Englisch. Jede Aufgabe außer frei braucht ein info. KEIN nachsicht (Rechtschreibung zählt)."""
    if min_aufgaben:
        assert len(aufgaben) >= min_aufgaben, f"{id}: nur {len(aufgaben)} Aufgaben (Ziel {min_aufgaben})"
    if info_pflicht:
        for i, t in enumerate(aufgaben, 1):
            if t["typ"] != "frei":
                assert t.get("info", "").strip(), f"{id} Aufgabe {i}: info fehlt ({t['frage'][:50]})"
    p = {"typ": "lernpaket", "version": 1, "person": ["joel", "dario", "lio", "luca"], "id": id, "titel": titel,
         "fach": FACH, "klasse": "6", "beschreibung": beschreibung}
    if hinweis:
        p["hinweis"] = hinweis
    if lernblatt:
        p["lernblatt"] = lernblatt
    p["aufgaben"] = aufgaben
    p = _normalisiere(p)
    pruefe(p)
    check_pack(p)
    return p


def pruefe(p):
    """Zusätzliche Prüfungen für Englisch."""
    for i, t in enumerate(p["aufgaben"], 1):
        w = f"{p['id']} Aufgabe {i} ({t['typ']}): "
        assert "nachsicht" not in t, w + "nachsicht ist bei Englisch nicht erlaubt"
        if t["typ"] == "luecke":
            for g in _gaps(t["text"]):
                for a in g.split("|"):
                    assert re.search(r"[A-Za-z0-9]", a), w + f"Lückenantwort ohne Buchstaben: {g!r}"
                    assert a == a.strip(), w + f"Leerzeichen in Lückenantwort: {g!r}"
            if "wortbank" in t:
                bank = t["wortbank"]
                assert len(set(bank)) == len(bank), w + "doppelte Wörter in der Wortbank"
        if t["typ"] == "kurz":
            r = t["richtig"] if isinstance(t["richtig"], list) else [t["richtig"]]
            assert all(re.search(r"[A-Za-z0-9]", x) for x in r), w
            assert len({x.lower() for x in r}) == len(r), w + f"doppelte Schreibweisen: {r}"
        if t["typ"] == "frei":
            assert t["punkte"] == len(t["kriterien"]), w + f"punkte {t['punkte']} ≠ Kriterien {len(t['kriterien'])}"
        for feld in ("frage", "text", "info", "tipp"):
            s = t.get(feld, "")
            if isinstance(s, str):
                assert "  " not in s.replace("\n", " "), w + f"zwei Leerzeichen in {feld}: {s[:60]!r}"
                ohne = s.replace("{{", "").replace("}}", "").replace("...", "…")
                assert not re.search(r"[A-Za-z0-9]\s[.,;:!?]", ohne) or "→" in s or "„" in s or "·" in s, w + f"Leerzeichen vor Satzzeichen in {feld}: {s[:80]!r}"
    for s in p.get("lernblatt", []):
        assert "  " not in s["text"], f"{p['id']} Lernblatt {s['titel']}: zwei Leerzeichen"


def woerter(text):
    """Anzahl Wörter (für Crashkurs-Prüfung)."""
    return len(re.findall(r"[A-Za-zÄÖÜäöüß0-9']+", re.sub(r"\*\*", "", text)))


def ref(paket, titel):
    return {"paket": paket, "titel": titel}
