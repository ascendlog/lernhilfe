#!/usr/bin/env python3
"""Erzeugt alle Geschichte-Lernpakete (Klasse 6, Steinzeit) für Joel und Dario in pakete/joel-dario/.

Aufruf: python3 tools/build_geschichte.py

Pakete: 1 Quellen/Stammbaum, 2a/2b Zeit, 3 Lucy, 4a/4b Altsteinzeit, 5a/5b Jungsteinzeit, 6 Ötzi, eine Probearbeit und der Crashkurs.
Alle Zahlen und Lösungen werden in den gesch_*.py-Dateien berechnet und mit assert geprüft.
"""
import json
import os
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
OUT = os.path.join(HIER, '..', 'pakete', 'joel-dario')
os.makedirs(OUT, exist_ok=True)

import gesch_p1, gesch_p2, gesch_p3, gesch_p4, gesch_p5, gesch_p6

THEMA = 'geschichte'
TERMIN = '2026-11-16'   # Geschichte-Arbeit (Montag)
DAUER = {'geschichte-probearbeit': 45}   # eigene Probearbeit, etwa 45 Minuten (siehe beschreibung)
# Sammelkarte je Paket (Album in der App): Titel höchstens 40 Zeichen, ein Emoji als Motiv, kurzer Text (höchstens 200 Zeichen).
# Neue Pakete bekommen immer eine eigene "karte".
KARTEN = {
    'geschichte-1-quellen-stammbaum': {'titel': 'Quellenforscher', 'motiv': '📜', 'text': 'Eine Quelle stammt aus der Zeit selbst. Eine Darstellung berichtet erst später darüber.'},
    'geschichte-2a-zeitrechnung-kalender': {'titel': 'Kalendermeister', 'motiv': '🗓️', 'text': 'Jahre vor und nach Christi Geburt vergleichen und Jahrhunderte bestimmen.'},
    'geschichte-2b-epochen-zeitstrahl': {'titel': 'Zeitstrahl-Profi', 'motiv': '📏', 'text': 'Die fünf Epochen in der richtigen Reihenfolge – und Ereignisse auf dem Zeitstrahl.'},
    'geschichte-3-lucy': {'titel': 'Lucy', 'motiv': '🦴', 'text': 'Über 3 Millionen Jahre alt, aus Ostafrika – und sie ging schon aufrecht.'},
    'geschichte-4a-steinzeit-eiszeit-werkzeuge': {'titel': 'Eiszeitforscher', 'motiv': '🦣', 'text': 'Steinzeit, Eiszeit, Mammut und die ersten Werkzeuge.'},
    'geschichte-4b-altsteinzeit-jagen-leben': {'titel': 'Rentierjäger', 'motiv': '🏹', 'text': 'Jagen und Sammeln: Vom Rentier wurde fast alles genutzt.'},
    'geschichte-5a-neolithische-revolution': {'titel': 'Erste Bauern', 'motiv': '🌾', 'text': 'Sesshaft werden, Tiere zähmen und Getreide anbauen.'},
    'geschichte-5b-jungsteinzeit-leben-vergleich': {'titel': 'Dorfbewohner', 'motiv': '🏡', 'text': 'Leben im Dorf der Jungsteinzeit – und der Vergleich mit der Altsteinzeit.'},
    'geschichte-6-oetzi': {'titel': 'Ötzi', 'motiv': '🏔️', 'text': 'Der Mann aus dem Eis – über 5000 Jahre alt.'},
    'geschichte-probearbeit': {'titel': 'Probearbeit-Urkunde', 'motiv': '🏆', 'text': 'Die Probearbeit gemeistert: Quellen, Zeit, Lucy, Steinzeit und Ötzi.'},
    'geschichte-crashkurs': {'titel': 'Spickzettel', 'motiv': '⚡', 'text': 'Das Wichtigste kurz gefasst – schnell wiederholt.'},
}


def datei(p):
    return p['id'] + '.json'


def ziel(p):
    """(Ordner, Eintrag für index.json): Ist das Thema abgeschlossen (liegt unter abgeschlossen/geschichte/), wird dort weitergeschrieben."""
    abg = os.path.join(OUT, 'abgeschlossen', THEMA)
    if os.path.exists(os.path.join(abg, datei(p))):
        return abg, f'abgeschlossen/{THEMA}/{datei(p)}'
    return OUT, datei(p)


def main():
    pakete = (gesch_p1.build() + gesch_p2.build() + gesch_p3.build() + gesch_p4.build() + gesch_p5.build() + gesch_p6.build())
    try:
        import gesch_pt
        pakete.append(gesch_pt.build(pakete))
    except ImportError:
        print('(noch keine Probearbeit)')
    try:
        import gesch_crashkurs
        pakete.append(gesch_crashkurs.build(pakete))   # Crashkurs zuletzt: wählt aus den Lernblättern der anderen Pakete aus
    except ImportError:
        print('(noch kein Crashkurs)')
    ids = [p['id'] for p in pakete]
    assert len(set(ids)) == len(ids), ids
    # Termin der Arbeit (von Alessandro genannt) und empfohlene Reihenfolge: erst üben (1–9), dann Probearbeit, zuletzt der Crashkurs als letzter Blick
    for n, p in enumerate(pakete, 1):
        p['termin'] = TERMIN
        p['reihenfolge'] = n
        if p['id'] in DAUER:
            p['dauer'] = DAUER[p['id']]   # Timer der Probearbeit in Minuten
        assert p['id'] in KARTEN, f"Karte fehlt für {p['id']}"
        k = KARTEN[p['id']]
        assert len(k['titel']) <= 40 and len(k['text']) <= 200, k
        p['karte'] = k   # Sammelkarte fürs Album
    for p in pakete:
        with open(os.path.join(ziel(p)[0], datei(p)), 'w', encoding='utf-8') as f:
            json.dump(p, f, ensure_ascii=False, indent=1)
            f.write('\n')
        print(f"{p['id']:45s} {len(p['aufgaben']):3d} Aufgaben, {len(p.get('lernblatt', []))} Lernblatt-Abschnitte")
    # index.json: Geschichte zuerst (Reihenfolge wie im Lernzettel), Probearbeit und Crashkurs zuletzt, übrige Einträge bleiben
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
