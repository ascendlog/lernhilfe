"""Hilfen für die Deutsch-Lernpakete (Klasse 6, Arbeit am 02.12.2026): Bausteine, Prüfungen, Hilfsfunktionen.

Baut auf geo_lib.py und gesch_lib.py auf. Grundlage aller Inhalte ist das Faktenblatt im Projekt (deutsch-klasse-6-fakten.md).
Datenschutz/Urheberrecht: Das Repository ist öffentlich. Alle Sätze, Texte und Namen sind selbst geschrieben, nichts aus Buch oder Heft.

Wichtig für die App (index.html, normText): ß und ss gelten beim Prüfen als gleich, Groß-/Kleinschreibung zählt nur mit "gross": true,
ein Komma als Lückenantwort geht nicht (am Ende abgeschnitten). Deshalb:
- Groß/klein: luecke/kurz mit gross=True (und ohne Nachsicht).
- s / ss / ß: nur als mc oder tf entscheiden lassen (nie als Lücke oder Zuordnung, dort sind ß und ss gleich).
- Kommas: Lücken mit Auswahl „Komma“ / „kein Komma“ (Funktion kommas) oder ganzen Satz abtippen lassen.
- Vertauschbare Lücken: Stehen zwei Lücken mit „und“, „oder“ oder Komma nebeneinander und dürfen ihre Wörter tauschen
  („Ich habe Hunger und Durst“ = „Ich habe Durst und Hunger“), wertet die App ohne Hilfe nur die Reihenfolge des Textes als richtig.
  Deshalb tauschbar=[("Hunger", "Durst")] angeben (die Wörter werden gegenseitig zu Alternativen {{Hunger|Durst}} … {{Durst|Hunger}}).
  Hängt die Reihenfolge am Text („Teig und schiebt“, „Hs , Ns“), steht dort fest=True. Ohne eine der beiden Angaben bricht der Build ab.
"""
import re

import geo_lib
from geo_lib import mc, tf, zuordnen, reihenfolge, frei, lb, check_pack, _gaps   # noqa: F401
from geo_lib import tausche as _tausche, pruefe_tausch as _pruefe_tausch
from gesch_lib import _normalisiere, punkte_von, nachlesen                       # noqa: F401

FACH = "Deutsch"
GRUPPE = "Deutscharbeit 02.12.2026"
TERMIN = "2026-12-02"
SPRACHE = "de-DE"


# ------------------------------------------------------------------ Aufgaben-Bausteine (mit gross, vorlesen, auswahl)

def kurz(frage, richtig, abschnitt, info=None, tipp=None, gross=False, vorlesen=None, einheit=None):
    t = geo_lib.kurz(frage, richtig, abschnitt, einheit=einheit, info=info, tipp=tipp)
    if gross:
        t["gross"] = True
    if vorlesen:
        t["vorlesen"] = {"text": vorlesen, "sprache": SPRACHE}
    return t


def luecke(frage, text, abschnitt, extra=(), info=None, tipp=None, wortbank=True, gross=False, auswahl=None, vorlesen=None,
           tauschbar=(), fest=False):
    """Lückentext. tauschbar=[("Hunger", "Durst")]: diese Wörter dürfen die Plätze tauschen. fest=True: Reihenfolge ist Pflicht."""
    text = _tausche(text, tauschbar)
    if not auswahl:
        _pruefe_tausch(text, fest)
    t = geo_lib.luecke(frage, text, abschnitt, extra=extra, info=info, tipp=tipp, wortbank=bool(wortbank and not auswahl))
    if auswahl:
        t["auswahl"] = list(auswahl)
    if gross:
        t["gross"] = True
    if vorlesen:
        t["vorlesen"] = {"text": vorlesen, "sprache": SPRACHE}
    return t


def _fix_gaps(t):
    """Mehrere richtige Wörter in einer Lücke ergänzen sich nur bei Alternativen {{a|b}}, die Wortbank braucht nur das erste."""
    return t


# ------------------------------------------------------------------ Groß oder klein? (gk)

GK_FRAGE = "Groß oder klein? Ziehe in jede Lücke das Wort in der richtigen Schreibweise."


def flip(w):
    return (w[0].lower() if w[0].isupper() else w[0].upper()) + w[1:]


def gk(satz, abschnitt, frage=GK_FRAGE, extra=(), tipp=None, info_zusatz=None, tauschbar=(), fest=False):
    """Lückentext Groß/klein. Im Satz steht jedes zu entscheidende Wort als [Wort|Grund] in seiner RICHTIGEN Schreibweise.

    Die Wortbank enthält die richtigen Wörter plus die jeweils andere Schreibweise (und extra). info entsteht aus den Gründen.
    tauschbar=[("Hunger", "Durst")]: Wörter, die ihre Plätze tauschen dürfen (siehe luecke); fest=True: Reihenfolge ist Pflicht.
    """
    gaps = []

    def rep(m):
        gaps.append((m.group(1).strip(), m.group(2).strip()))
        return "{{" + m.group(1).strip() + "}}"

    text = re.sub(r"\[([^\]|]+)\|([^\]]+)\]", rep, satz)
    assert gaps, satz
    firsts = [w for w, _ in gaps]
    ex = []
    for w in firsts:
        f = flip(w)
        if f not in firsts and f not in ex:
            ex.append(f)
    for w in extra:
        if w not in firsts and w not in ex:
            ex.append(w)
    teile = []
    for w, why in gaps:
        teile.append(f"„{w}“ schreibt man {'groß' if w[0].isupper() else 'klein'}: {why}.")
    info = " ".join(teile) + ((" " + info_zusatz) if info_zusatz else "")
    return luecke(frage, text, abschnitt, extra=ex, info=info, tipp=tipp, gross=True, tauschbar=tauschbar, fest=fest)


# ------------------------------------------------------------------ Kommas setzen (kommas)

KOMMA = "Komma"
KEIN = "kein Komma"
KOMMA_FRAGE = "Wo gehört ein Komma hin? Wähle bei jeder Lücke „Komma“ oder „kein Komma“."


def kommas(satz, abschnitt, info, frage=KOMMA_FRAGE, tipp=None):
    """Satz mit Kommastellen: {,} = Komma Pflicht, {-} = kein Komma, {?} = Komma darf wegfallen (beides richtig).

    Beispiel: "Ich lese gern {,} denn die Geschichte ist lustig." Die Stellen werden zu Lücken mit Auswahlliste.
    """
    ersetze = {"{,}": "{{" + KOMMA + "}}", "{-}": "{{" + KEIN + "}}", "{?}": "{{" + KOMMA + "|" + KEIN + "}}"}
    text = satz
    for k, v in ersetze.items():
        text = text.replace(k, v)
    assert "{{" in text and "{," not in text and "{-" not in text and "{?" not in text, satz
    return luecke(frage, text, abschnitt, info=info, tipp=tipp, wortbank=False, auswahl=[KOMMA, KEIN])


def satz_mit_kommas(satz):
    """Der korrekte Satz aus einer kommas-Vorlage (Pflichtkommas gesetzt, optionale weggelassen)."""
    s = satz.replace(" {,}", ",").replace("{,}", ",").replace(" {-}", "").replace("{-}", "").replace(" {?}", "").replace("{?}", "")
    return re.sub(r"\s+", " ", s).strip()


def satz_mit_optionalen(satz):
    """Wie satz_mit_kommas, aber optionale Kommas gesetzt."""
    s = satz.replace(" {,}", ",").replace(" {?}", ",").replace(" {-}", "")
    return re.sub(r"\s+", " ", s).strip()


# ------------------------------------------------------------------ Paket

def pack(id, titel, beschreibung, lernblatt, aufgaben, hinweis=None, min_aufgaben=None, info_pflicht=True):
    """Wie gesch_lib.pack, aber Fach Deutsch. Jede Aufgabe außer frei braucht ein info.

    nachsicht (Tippfehler, Artikel, Bindestriche egal) gilt nur für Aufgaben ohne gross; bei Rechtschreibung zählt jede Schreibweise."""
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
    for t in aufgaben:
        if t["typ"] in ("kurz", "luecke") and not t.get("gross"):
            t["nachsicht"] = True
    p = _normalisiere(p)
    pruefe(p)
    check_pack(p)
    return p


def pruefe(p):
    """Zusätzliche Prüfungen für Deutsch."""
    for i, t in enumerate(p["aufgaben"], 1):
        w = f"{p['id']} Aufgabe {i} ({t['typ']}): "
        if t["typ"] == "luecke":
            for g in _gaps(t["text"]):
                for a in g.split("|"):
                    assert re.search(r"[A-Za-zÄÖÜäöüß]", a), w + f"Lückenantwort ohne Buchstaben: {g!r}"
            if t.get("gross") and "wortbank" in t:
                bank = t["wortbank"]
                assert len(set(bank)) == len(bank), w + "doppelte Wörter in der Wortbank"
        if t["typ"] == "kurz":
            r = t["richtig"] if isinstance(t["richtig"], list) else [t["richtig"]]
            assert all(re.search(r"[A-Za-zÄÖÜäöüß0-9]", x) for x in r), w
        for feld in ("frage", "text", "info", "tipp"):
            s = t.get(feld, "")
            if isinstance(s, str):
                assert "  " not in s, w + f"zwei Leerzeichen in {feld}: {s[:60]!r}"
                assert not re.search(r"\s[.,;:!?]", s.replace("{{", "").replace("}}", "")) or "„" in s or "→" in s or "Hs" in s, w + f"Leerzeichen vor Satzzeichen in {feld}: {s[:80]!r}"


def woerter(text):
    """Anzahl Wörter (für Crashkurs-Prüfung)."""
    return len(re.findall(r"[A-Za-zÄÖÜäöüß0-9]+", re.sub(r"\*\*", "", text)))


def ref(paket, titel):
    return {"paket": paket, "titel": titel}
