#!/usr/bin/env python3
"""Erzeugt alle Englisch-Lernpakete (Klasse 6, Englischarbeit am 08.12.2026, Unit 2) für Joel, Dario, Lio und Luca.

Aufruf: python3 tools/build_englisch.py

Pakete: 2a Hören, 2b und 2c Wortschatz, 2d und 2e going to, 2f und 2g Steigerung der Adjektive, 2h Schreiben, eine Probearbeit und der Crashkurs.
Die Pakete liegen im Arbeits-Ordner pakete/joel-dario/englischarbeit-08.12.2026/ (in der App eine eigene Gruppe mit „Alle hinzufügen“).
Alle Lösungen werden in den eng_*.py-Dateien mit assert geprüft; getestet wird mit tools/deutsch_test.py.
"""
import json
import os
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
OUT = os.path.join(HIER, '..', 'pakete', 'joel-dario')
ARBEIT = 'englischarbeit-08.12.2026'
os.makedirs(os.path.join(OUT, ARBEIT), exist_ok=True)

import eng_p2a, eng_p2b, eng_p2c, eng_p2d, eng_p2e, eng_p2f, eng_p2g, eng_p2h   # noqa: E402
from repo_ziel import finde   # noqa: E402

THEMA = 'englisch'
TERMIN = '2026-12-08'   # Englischarbeit (Dienstag)
GRUPPE = 'Englischarbeit 08.12.2026'
DAUER = {'englisch-probearbeit': 45}   # eigene Probearbeit, etwa 45 Minuten (siehe beschreibung)
# Sammelkarte je Paket (Album in der App): Titel höchstens 40 Zeichen, ein Emoji als Motiv, kurzer Text (höchstens 200 Zeichen).
KARTEN = {
    'englisch-2a-hoeren': {'titel': 'Hör-Profi', 'motiv': '🎧', 'text': 'Zahlen, Uhrzeiten und Daten verstehen: thirteen oder thirty? Wer genau hinhört, hat die Antwort schon.'},
    'englisch-2b-wortschatz-1': {'titel': 'Vokabel-Held', 'motiv': '🎭', 'text': 'Schule, Bühne und Gefühle: audition, stage, nervous – und aus Verben werden Personen: singer, dancer.'},
    'englisch-2c-wortschatz-2': {'titel': 'Wörter-Zauberer', 'motiv': '🪄', 'text': 'get hat viele Bedeutungen, mine und yours stehen allein, und jedes Wort will genau geschrieben sein.'},
    'englisch-2d-going-to-1': {'titel': 'Going-to-Planer', 'motiv': '🗓️', 'text': 'I\'m going to … Pläne mit am, is, are plus Grundform und die Verneinung mit not.'},
    'englisch-2e-going-to-2': {'titel': 'Fragen-Meister', 'motiv': '❓', 'text': 'Are you going to come? Fragen, Fragewörter und Kurzantworten mit going to.'},
    'englisch-2f-steigerung-1': {'titel': 'Steigerungs-Sprinter', 'motiv': '🏃', 'text': 'tall, taller, the tallest: kurze Adjektive mit -er und -est, lange mit more und most.'},
    'englisch-2g-steigerung-2': {'titel': 'Vergleichs-König', 'motiv': '👑', 'text': 'than, as … as und the … of / in: Menschen, Tiere und Schulen sicher vergleichen.'},
    'englisch-2h-schreiben': {'titel': 'Schreib-Talent', 'motiv': '✍️', 'text': 'Meine Schule, mein Schultag und ein Vergleich mit einer englischen Schule: ein Text mit Anfang, Mitte und Schluss.'},
    'englisch-probearbeit': {'titel': 'Probearbeit-Urkunde', 'motiv': '🏆', 'text': 'Die Probearbeit gemeistert: Listening, Vocabulary, Grammar und Writing.'},
    'englisch-crashkurs': {'titel': 'Spickzettel', 'motiv': '⚡', 'text': 'Das Wichtigste für die Englischarbeit kurz gefasst – schnell wiederholt.'},
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
    for m in (eng_p2a, eng_p2b, eng_p2c, eng_p2d, eng_p2e, eng_p2f, eng_p2g, eng_p2h):
        pakete += m.build()
    import eng_pt
    pakete.append(eng_pt.build(pakete))
    import eng_crashkurs
    pakete.append(eng_crashkurs.build(pakete))   # Crashkurs zuletzt: wählt aus den Lernblättern der anderen Pakete aus
    ids = [p['id'] for p in pakete]
    assert len(set(ids)) == len(ids), ids
    # Termin der Arbeit, Gruppe auf der Startseite und empfohlene Reihenfolge: erst üben (2a–2h), dann Probearbeit, zuletzt der Crashkurs
    for n, p in enumerate(pakete, 1):
        p['termin'] = TERMIN
        p['reihenfolge'] = n
        p['gruppe'] = GRUPPE
        p['dauerhaft'] = False   # sonst bleiben Pakete mit „gruppe“ bei „Alle Pakete löschen“ stehen
        if p['id'] != 'englisch-probearbeit':
            p['probe'] = False   # Übungspakete und Crashkurs ohne Probearbeit: die gibt es nur im eigenen Paket „englisch-probearbeit“
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
    # index.json: bestehende Einträge bleiben. Die aktuellen Arbeits-Ordner (z. B. Deutsch) stehen zuerst, dann Englisch, dann abgeschlossene Themen.
    ix_path = os.path.join(OUT, 'index.json')
    try:
        alt = json.load(open(ix_path, encoding='utf-8'))
    except Exception:
        alt = []
    eigene = [datei(p) for p in pakete]
    fremde = [n for n in alt if n.split('/')[-1] not in eigene]
    aktiv = [n for n in fremde if not n.startswith('abgeschlossen/')]
    erledigt = [n for n in fremde if n.startswith('abgeschlossen/')]
    ix = aktiv + [ziel(p)[1] for p in pakete] + erledigt
    with open(ix_path, 'w', encoding='utf-8') as f:
        json.dump(ix, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print('Aufgaben gesamt:', sum(len(p['aufgaben']) for p in pakete))


if __name__ == '__main__':
    main()
