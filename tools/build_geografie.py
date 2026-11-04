#!/usr/bin/env python3
"""Erzeugt alle Geografie-Lernpakete (Klasse 6) für Joel und Dario in pakete/joel-dario/.

Aufruf: python3 tools/build_geografie.py

Pakete: 1 Nord- und Ostsee, 2a/2b Gezeiten, 3a/3b Wattenmeer, 4a bis 4d Küstenschutz, eine eigene Probearbeit und der Crashkurs.
Die Zahlen und Lösungen werden in den geo_*.py-Dateien berechnet und mit assert geprüft.
"""
import json
import os
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
OUT = os.path.join(HIER, '..', 'pakete', 'joel-dario')
os.makedirs(OUT, exist_ok=True)

import geo_p1, geo_p2, geo_p3, geo_p4, geo_pt, geo_crashkurs, geo_lesen

ALT = ['geografie-nordsee-wattenmeer.json']   # alter Entwurf mit 13 Aufgaben, ersetzt durch die neuen Pakete


def datei(p):
    return p['id'] + '.json'


THEMA = 'geografie'


def ziel(p):
    """(Ordner, Eintrag für index.json): Ist das Thema abgeschlossen (Datei liegt unter abgeschlossen/geografie/), wird dort weitergeschrieben."""
    abg = os.path.join(OUT, 'abgeschlossen', THEMA)
    if os.path.exists(os.path.join(abg, datei(p))):
        return abg, f'abgeschlossen/{THEMA}/{datei(p)}'
    return OUT, datei(p)


def main():
    pakete = [geo_p1.build()] + geo_p2.build() + geo_p3.build() + geo_p4.build() + [geo_pt.build()]
    pakete.append(geo_crashkurs.build(pakete))   # Crashkurs zuletzt: wählt aus den Lernblättern der anderen Pakete aus
    geo_lesen.anwenden(pakete)   # Verweise „Nachlesen“ (Aufgabe -> Lernblatt-Abschnitt), prüft alle Ziele
    ids = [p['id'] for p in pakete]
    assert len(set(ids)) == len(ids), ids
    for p in pakete:
        with open(os.path.join(ziel(p)[0], datei(p)), 'w', encoding='utf-8') as f:
            json.dump(p, f, ensure_ascii=False, indent=1)
            f.write('\n')
        print(f"{p['id']:45s} {len(p['aufgaben']):3d} Aufgaben, {len(p.get('lernblatt', []))} Lernblatt-Abschnitte")
    for a in ALT:
        pfad = os.path.join(OUT, a)
        if os.path.exists(pfad):
            os.remove(pfad)
    # index.json: Reihenfolge wie im Wissenscheck, Probearbeit und Crashkurs zuletzt
    ix_path = os.path.join(OUT, 'index.json')
    try:
        alt = json.load(open(ix_path, encoding='utf-8'))
    except Exception:
        alt = []
    eigene = [datei(p) for p in pakete]
    fremde = [n for n in alt if n not in ALT and n.split('/')[-1] not in eigene]
    ix = [ziel(p)[1] for p in pakete] + fremde
    with open(ix_path, 'w', encoding='utf-8') as f:
        json.dump(ix, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print('Aufgaben gesamt:', sum(len(p['aufgaben']) for p in pakete))
    print('index.json:', ix)


if __name__ == '__main__':
    main()
