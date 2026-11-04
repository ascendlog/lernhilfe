"""Geografie Klasse 6: Verweise „Nachlesen“ (welche Aufgabe gehört zu welchem Lernblatt-Abschnitt).

Die App zeigt unter einer falsch beantworteten Aufgabe einen aufklappbaren Kasten mit dem passenden Abschnitt des Lernblatts.
- Übungspakete: Paketfeld "nachlesen" ordnet jedem Aufgabenblock (abschnitt) einen oder mehrere Lernblatt-Abschnitte zu.
  Wo ein Block mehrere Abschnitte umfasst, verfeinern Stichwort-Regeln je Aufgabe (Feld "lesen" an der Aufgabe).
- Probearbeit (hat kein Lernblatt): Feld "lesen" je Aufgabe, verweist auf die Lernblätter der Übungspakete.
- Crashkurs: Feld "lesen" je Aufgabe auf den eigenen Abschnitt.

Alle Verweise werden hier geprüft: Der Abschnitt muss im Ziel-Lernblatt vorkommen, und jede Aufgabe muss mindestens einen Verweis haben.
"""
import re

P1 = "geografie-1-nord-ostsee"
P2A = "geografie-2a-gezeiten-grundlagen"
P2B = "geografie-2b-gezeiten-kurve-kalender"
P3A = "geografie-3a-wattenmeer-lebensraum"
P3B = "geografie-3b-wattenmeer-schutz"
P4A = "geografie-4a-deich-aufbau"
P4B = "geografie-4b-deich-beschriften-hoehen"
P4C = "geografie-4c-duene"
P4D = "geografie-4d-sieltor"
PT = "geografie-probearbeit"
CK = "geografie-crashkurs"


def ref(paket, titel):
    return {"paket": paket, "titel": titel}


# Abschnitte (Titel) der Lernblätter, auf die verwiesen wird
L_BL = "Länder und Bundesländer an den Meeren"
L_VERGL = "Nordsee und Ostsee im Vergleich"
L_STAEDTE = "Städte, Flüsse und Inseln"
L_INSELN = "Nordfriesische und Ostfriesische Inseln"
L_ENTSTEHEN = "So entstehen die Gezeiten"
L_BEGRIFFE = "Wichtige Begriffe"
L_HUB = "Der Tidenhub ist nicht überall gleich"
L_KURVE = "Gezeitenkurve lesen"
L_KALENDER = "Tidenkalender lesen"
L_WATT = "Das Wattenmeer: ein besonderer Lebensraum"
L_WERLEBT = "Wer lebt wo? Meer, Watt und Salzwiese"
L_ZONEN = "Die vier Zonen des Watts"
L_SCHUTZ = "Warum und wie wird das Wattenmeer geschützt?"
L_SCHUTZZONEN = "Die drei Schutzzonen"
L_DEICH = "Der Deich: Aufgabe und Teile"
L_DEICHBAU = "Woraus besteht ein Deich?"
L_PROFIL = "Deiche werden höher: die Deichprofile"
L_DUENE = "Dünen: Sandwälle am Strand"
L_DUENE_BETRETEN = "Warum darf man Dünen nicht betreten?"
L_SIEL = "Das Sieltor"

# Block (abschnitt) -> Lernblatt-Abschnitt(e) im selben Paket oder Verweis auf ein anderes Paket
NACHLESEN = {
    P1: {
        "A – Meere und Länder": L_BL,
        "B – Unterschiede zwischen Nordsee und Ostsee": L_VERGL,
        "C – Städte an den Küsten": L_STAEDTE,
        "D – Flüsse": L_STAEDTE,
        "E – Inseln": [L_STAEDTE, L_INSELN],
    },
    P2A: {
        "A – So entstehen die Gezeiten": L_ENTSTEHEN,
        "B – Wichtige Begriffe": L_BEGRIFFE,
        "C – Der Tidenhub an verschiedenen Orten": L_HUB,
    },
    P2B: {
        "D – Die Gezeitenkurve lesen": L_KURVE,
        "E – Der Tidenkalender": L_KALENDER,
        "F – Warum sich die Gezeiten verschieben": L_KALENDER,
    },
    P3A: {
        "A – Der Lebensraum Watt": L_WATT,
        "B – Wer lebt wo? Meer, Watt und Salzwiese": L_WERLEBT,
        "D – Die vier Zonen des Watts": L_ZONEN,
    },
    P3B: {
        "C – Warum und wie wird das Wattenmeer geschützt?": [L_SCHUTZ, L_SCHUTZZONEN],
    },
    P4A: {
        "A – Wozu gibt es Deiche?": L_DEICH,
        "B – Aufbau und Teile des Deichs": [L_DEICH, L_DEICHBAU],
    },
    P4B: {
        "C – Den Deich beschriften": L_DEICH,
        "D – Deichprofile und Deichhöhen": L_PROFIL,
        "E – Anwenden und erklären": [L_DEICH, L_PROFIL],
    },
    P4C: {
        "A – Dünen: wie sie wachsen": L_DUENE,
        "B – Dünen schützen": L_DUENE_BETRETEN,
        "C – Die Düne beschriften": L_DUENE,
    },
    P4D: {
        "D – Das Sieltor: Ebbe und Flut": L_SIEL,
        "E – Sieltor zeichnen und lesen": L_SIEL,
        "F – Deich, Düne und Siel im Vergleich": [L_SIEL, ref(P4A, L_DEICH), ref(P4C, L_DUENE)],
    },
}

# Verfeinerung: Stichwörter in Frage und Text einer Aufgabe wählen aus dem Block-Verweis genauer aus (nur wenn genau eine Regel passt).
REGELN = {
    (P1, "E – Inseln"): [
        (r"friesisch|Borkum|Juist|Norderney|Baltrum|Langeoog|Spiekeroog|Wangerooge|Sylt|Föhr|Amrum|Helgoland", L_INSELN),
        (r"Meer|größte|Ostsee|Nordsee", L_STAEDTE),
    ],
    (P3B, "C – Warum und wie wird das Wattenmeer geschützt?"): [
        (r"zone", L_SCHUTZZONEN),
        (r"Nationalpark|Weltnaturerbe|Schild|Vorland|Schutzbestimmung|schützt|Gruppen|Tourist|Dänemark", L_SCHUTZ),
    ],
    (P4A, "B – Aufbau und Teile des Deichs"): [
        (r"Sandkern|Klei|Grasdecke|Schaf|Aufbau|von innen|Deichfuß|Steine|Inneren", L_DEICHBAU),
        (r"Seeseite|Landseite|flach|steil|Deichkrone|höchste", L_DEICH),
    ],
    (P4B, "E – Anwenden und erklären"): [
        (r"Sturmflut|höher|breiter|Profil|Höhe", L_PROFIL),
        (r"Deichfuß|Steine|zeichne|beschrift|Teile", L_DEICH),
    ],
}

# Probearbeit (kein Lernblatt): Aufgabe (ab 1) -> Verweise auf die Lernblätter der Übungspakete
PROBEARBEIT = {
    1: ref(P1, L_BL),
    2: ref(P1, L_VERGL),
    3: ref(P1, L_INSELN),
    4: ref(P2A, L_ENTSTEHEN),
    5: ref(P2A, L_ENTSTEHEN),
    6: ref(P2B, L_KURVE),
    7: [ref(P2A, L_BEGRIFFE), ref(P2B, L_KURVE)],
    8: ref(P2B, L_KURVE),
    9: ref(P2B, L_KALENDER),
    10: ref(P2B, L_KALENDER),
    11: ref(P3A, L_WATT),
    12: ref(P3A, L_ZONEN),
    13: ref(P3B, L_SCHUTZ),
    14: ref(P3B, L_SCHUTZZONEN),
    15: ref(P4A, L_DEICH),
    16: [ref(P4A, L_DEICH), ref(P4A, L_DEICHBAU)],
    17: ref(P4C, L_DUENE),
    18: ref(P4D, L_SIEL),
}

# Crashkurs: Blitz-Check-Aufgabe (ab 1) -> eigener Abschnitt
CRASHKURS = {
    1: "Nord- und Ostsee: Bundesländer, Städte, Flüsse",
    2: "Nordsee gegen Ostsee",
    3: "Inseln",
    4: "Gezeiten: So entstehen Ebbe und Flut",
    5: "Gezeiten: So entstehen Ebbe und Flut",
    6: "Gezeiten: Begriffe, Kurve und Tidenkalender",
    7: "Wattenmeer: Lebensraum und Zonen",
    8: "Wattenmeer: Schutz und Schutzzonen",
    9: "Küstenschutz: Düne und Sieltor",
    10: "Küstenschutz: Düne und Sieltor",
    11: "Küstenschutz: Der Deich",
    12: "Küstenschutz: Der Deich",
}

# Inhaltliche Anker: Das Stichwort muss im verwiesenen Abschnitt wirklich vorkommen (Schutz vor falschen Zuordnungen)
BELEG = [
    (P2A, L_BEGRIFFE, "Tidenhub"), (P2B, L_KURVE, "Tidenhub"), (P2B, L_KALENDER, "verschieb"),
    (P3A, L_ZONEN, "Zone"), (P3B, L_SCHUTZZONEN, "Ruhezone"), (P3B, L_SCHUTZ, "Vorland"),
    (P4A, L_DEICH, "Seeseite"), (P4A, L_DEICHBAU, "Klei"), (P4A, L_DEICHBAU, "Schaf"), (P4A, L_DEICHBAU, "Grasdecke"),
    (P4A, L_DEICH, "Deichfuß"), (P4B, L_PROFIL, "Sturmflut"), (P4C, L_DUENE, "Strandhafer"),
    (P1, L_INSELN, "Sylt"),
]


def _aufgabentext(t):
    """Frage und Text der Aufgabe (ohne Antworten), zum Suchen der Stichwörter."""
    return (t.get("frage", "") + " " + t.get("text", "")).replace("{{", "").replace("}}", "")


def _liste(x):
    return x if isinstance(x, list) else [x]


def anwenden(pakete):
    """Setzt "nachlesen" und "lesen" in die gebauten Pakete (in place) und prüft alle Verweise."""
    byid = {p["id"]: p for p in pakete}

    def titel_da(paket_id, titel):
        return any(s["titel"] == titel for s in byid[paket_id].get("lernblatt", []))

    def pruefe(r, eigen):
        if isinstance(r, dict):
            assert titel_da(r["paket"], r["titel"]), f"Verweis ins Leere: {r}"
        else:
            assert titel_da(eigen, r), f"{eigen}: Abschnitt „{r}“ fehlt im Lernblatt"

    for paket_id, bloecke in NACHLESEN.items():
        p = byid[paket_id]
        vorhanden = []
        for t in p["aufgaben"]:
            if t["abschnitt"] not in vorhanden:
                vorhanden.append(t["abschnitt"])
        assert set(vorhanden) == set(bloecke), (paket_id, set(vorhanden) ^ set(bloecke))
        for r in bloecke.values():
            for x in _liste(r):
                pruefe(x, paket_id)
        # Verfeinerung je Aufgabe
        for t in p["aufgaben"]:
            regeln = REGELN.get((paket_id, t["abschnitt"]))
            if not regeln:
                continue
            treffer = []
            for muster, ziel in regeln:
                if re.search(muster, _aufgabentext(t), re.I) and ziel not in treffer:
                    pruefe(ziel, paket_id)
                    treffer.append(ziel)
            # Nur eindeutige Treffer verfeinern; passen mehrere Regeln, bleibt der Verweis des ganzen Blocks (alle Abschnitte)
            if len(treffer) == 1 and _liste(treffer[0]) != _liste(bloecke[t["abschnitt"]]):
                t["lesen"] = treffer[0]
        a = p.pop("aufgaben")
        p["nachlesen"] = bloecke
        p["aufgaben"] = a

    p = byid[PT]
    assert sorted(PROBEARBEIT) == list(range(1, len(p["aufgaben"]) + 1)), "Probearbeit: Verweis je Aufgabe nötig"
    for i, t in enumerate(p["aufgaben"], 1):
        for x in _liste(PROBEARBEIT[i]):
            pruefe(x, PT)
        t["lesen"] = PROBEARBEIT[i]

    p = byid[CK]
    assert sorted(CRASHKURS) == list(range(1, len(p["aufgaben"]) + 1)), "Crashkurs: Verweis je Aufgabe nötig"
    for i, t in enumerate(p["aufgaben"], 1):
        pruefe(CRASHKURS[i], CK)
        t["lesen"] = CRASHKURS[i]

    for paket_id, titel, wort in BELEG:
        text = next(s["text"] + " " + (s.get("merke") or "") for s in byid[paket_id]["lernblatt"] if s["titel"] == titel)
        assert wort.lower() in text.lower(), f"{paket_id} „{titel}“ enthält „{wort}“ nicht"

    # Jede Aufgabe aller Pakete (außer Englisch/Musik) hat mindestens einen Verweis
    for p in pakete:
        for i, t in enumerate(p["aufgaben"], 1):
            r = t.get("lesen")
            if r is None:
                r = p.get("nachlesen", {}).get(t.get("abschnitt"))
            assert r, f"{p['id']} Aufgabe {i}: kein Verweis"
    return pakete
