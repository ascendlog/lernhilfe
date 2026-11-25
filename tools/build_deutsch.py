#!/usr/bin/env python3
"""Erzeugt alle Deutsch-Lernpakete (Klasse 6, Deutscharbeit am 02.12.2026) für Joel, Dario, Lio und Luca.

Aufruf: python3 tools/build_deutsch.py

Pakete: 1a bis 1c Nominalisierung, 2a bis 2c Satzreihe/Satzgefüge/Komma, 3a bis 3c Rechtschreibung und Diktat, eine Probearbeit und der Crashkurs.
Die Pakete liegen im Arbeits-Ordner pakete/joel-dario/deutscharbeit-02.12.2026/ (in der App eine eigene Gruppe mit „Alle hinzufügen“).
Alle Lösungen werden in den deutsch_*.py-Dateien mit assert geprüft; getestet wird mit tools/deutsch_test.py.
"""
import json
import os
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
OUT = os.path.join(HIER, '..', 'pakete', 'joel-dario')
ARBEIT = 'deutscharbeit-02.12.2026'
os.makedirs(os.path.join(OUT, ARBEIT), exist_ok=True)

import deutsch_p1a, deutsch_p1b, deutsch_p1c, deutsch_p2a, deutsch_p2b, deutsch_p2c, deutsch_p3a, deutsch_p3b, deutsch_p3c   # noqa: E402
from repo_ziel import finde   # noqa: E402

THEMA = 'deutsch'
TERMIN = '2026-12-02'   # Deutscharbeit (Mittwoch)
GRUPPE = 'Deutscharbeit 02.12.2026'
DAUER = {'deutsch-probearbeit': 45}   # eigene Probearbeit, etwa 45 Minuten (siehe beschreibung)
# Sammelkarte je Paket (Album in der App): Titel höchstens 40 Zeichen, ein Emoji als Motiv, kurzer Text (höchstens 200 Zeichen).
KARTEN = {
    'deutsch-1a-nomen-begleiter': {'titel': 'Begleiter-Detektiv', 'motiv': '🔎', 'text': 'Artikel, Adjektiv, Pronomen: Wer einen Begleiter hat, ist ein Nomen und wird großgeschrieben.'},
    'deutsch-1b-nominalisierte-verben': {'titel': 'Verben-Verwandler', 'motiv': '🔄', 'text': 'Aus Verben werden Nomen: beim Lesen, zum Essen, das Schwimmen.'},
    'deutsch-1c-nominalisierte-adjektive-superlativ': {'titel': 'Adjektiv-Profi', 'motiv': '🌟', 'text': 'Etwas Neues, im Dunkeln, das Schönste – und „am schnellsten“ bleibt klein.'},
    'deutsch-2a-satzreihe': {'titel': 'Satzreihen-Baumeister', 'motiv': '🧱', 'text': 'Zwei Hauptsätze, eine Konjunktion und das Komma an der richtigen Stelle.'},
    'deutsch-2b-satzgefuege': {'titel': 'Satzgefüge-Knacker', 'motiv': '🧩', 'text': 'Hauptsatz plus Nebensatz: Das Verb steht am Ende und davor steht das Komma.'},
    'deutsch-2c-satzreihe-oder-satzgefuege': {'titel': 'Komma-Meister', 'motiv': '✍️', 'text': 'Satzreihe oder Satzgefüge? Die Verbprobe verrät es.'},
    'deutsch-3a-rechtschreibung-1': {'titel': 'Silbenschwinger', 'motiv': '🎵', 'text': 'Offene und geschlossene Silben, Doppelkonsonanten, s-Laute, ie und h.'},
    'deutsch-3b-rechtschreibung-2': {'titel': 'Wörter-Detektiv', 'motiv': '🕵️', 'text': 'Verlängern, zerlegen, ableiten: Mit der richtigen Strategie sicher schreiben.'},
    'deutsch-3c-diktat-ueben': {'titel': 'Diktat-Profi', 'motiv': '🎧', 'text': 'Genau zuhören, Satz für Satz schreiben und am Ende prüfen.'},
    'deutsch-probearbeit': {'titel': 'Probearbeit-Urkunde', 'motiv': '🏆', 'text': 'Die Probearbeit gemeistert: Nominalisierung, Kommas, Diktat und Rechtschreibung.'},
    'deutsch-crashkurs': {'titel': 'Spickzettel', 'motiv': '⚡', 'text': 'Das Wichtigste kurz gefasst – schnell wiederholt.'},
}


def datei(p):
    return p['id'] + '.json'


def ziel(p):
    """(Ordner, Eintrag für index.json): Liegt das Paket schon irgendwo (Arbeits-Ordner, abgeschlossen/…), wird dort weitergeschrieben, sonst im Arbeits-Ordner."""
    ordner, eintrag = finde(OUT, THEMA, datei(p))
    if eintrag == datei(p):   # nirgends gefunden: in den Arbeits-Ordner
        return os.path.join(OUT, ARBEIT), f'{ARBEIT}/{datei(p)}'
    return ordner, eintrag


def main():
    pakete = []
    for m in (deutsch_p1a, deutsch_p1b, deutsch_p1c, deutsch_p2a, deutsch_p2b, deutsch_p2c, deutsch_p3a, deutsch_p3b, deutsch_p3c):
        pakete += m.build()
    import deutsch_pt
    pakete.append(deutsch_pt.build(pakete))
    import deutsch_crashkurs
    pakete.append(deutsch_crashkurs.build(pakete))   # Crashkurs zuletzt: wählt aus den Lernblättern der anderen Pakete aus
    ids = [p['id'] for p in pakete]
    assert len(set(ids)) == len(ids), ids
    # Termin der Arbeit, Gruppe auf der Startseite und empfohlene Reihenfolge: erst üben (1–9), dann Probearbeit, zuletzt der Crashkurs
    for n, p in enumerate(pakete, 1):
        p['termin'] = TERMIN
        p['reihenfolge'] = n
        p['gruppe'] = GRUPPE
        p['dauerhaft'] = False   # sonst bleiben Pakete mit „gruppe“ bei „Alle Pakete löschen“ stehen
        if p['id'] in DAUER:
            p['dauer'] = DAUER[p['id']]   # Timer der Probearbeit in Minuten
        assert p['id'] in KARTEN, f"Karte fehlt für {p['id']}"
        k = KARTEN[p['id']]
        assert len(k['titel']) <= 40 and len(k['text']) <= 200, k
        p['karte'] = k   # Sammelkarte fürs Album
    for p in pakete:
        d = ziel(p)[0]
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, datei(p)), 'w', encoding='utf-8') as f:
            json.dump(p, f, ensure_ascii=False, indent=1)
            f.write('\n')
        print(f"{p['id']:50s} {len(p['aufgaben']):3d} Aufgaben, {len(p.get('lernblatt', []))} Lernblatt-Abschnitte")
    # index.json: Deutsch zuerst (Reihenfolge wie im Lernzettel), übrige Einträge bleiben
    ix_path = os.path.join(OUT, 'index.json')
    try:
        alt = json.load(open(ix_path, encoding='utf-8'))
    except Exception:
        alt = []
    eigene = [datei(p) for p in pakete]
    fremde = [n for n in alt if n.split('/')[-1] not in eigene]
    ix = [ziel(p)[1] for p in pakete] + fremde
    with open(ix_path, 'w', encoding='utf-8') as f:
        json.dump(ix, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print('Aufgaben gesamt:', sum(len(p['aufgaben']) for p in pakete))


if __name__ == '__main__':
    main()
