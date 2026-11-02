#!/usr/bin/env python3
"""Erzeugt alle Geografie-Lernpakete (Klasse 6) für Joel und Dario in pakete/joel-dario/.

Aufruf: python3 tools/build_geografie.py

Pakete: 1 Nord- und Ostsee, 2a/2b Gezeiten, 3a/3b Wattenmeer, 4a bis 4d Küstenschutz und eine eigene Probearbeit.
Die Zahlen und Lösungen werden in den geo_*.py-Dateien berechnet und mit assert geprüft.
"""
import json
import os
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
OUT = os.path.join(HIER, '..', 'pakete', 'joel-dario')
os.makedirs(OUT, exist_ok=True)

import geo_p1, geo_p2, geo_p3, geo_p4, geo_pt

ALT = ['geografie-nordsee-wattenmeer.json']   # alter Entwurf mit 13 Aufgaben, ersetzt durch die neuen Pakete


def datei(p):
    return p['id'] + '.json'


def main():
    pakete = [geo_p1.build()] + geo_p2.build() + geo_p3.build() + geo_p4.build() + [geo_pt.build()]
    ids = [p['id'] for p in pakete]
    assert len(set(ids)) == len(ids), ids
    for p in pakete:
        with open(os.path.join(OUT, datei(p)), 'w', encoding='utf-8') as f:
            json.dump(p, f, ensure_ascii=False, indent=1)
            f.write('\n')
        print(f"{p['id']:45s} {len(p['aufgaben']):3d} Aufgaben, {len(p['lernblatt'])} Lernblatt-Abschnitte")
    for a in ALT:
        pfad = os.path.join(OUT, a)
        if os.path.exists(pfad):
            os.remove(pfad)
    # index.json: Reihenfolge wie im Wissenscheck, Probearbeit zuletzt
    ix_path = os.path.join(OUT, 'index.json')
    try:
        alt = json.load(open(ix_path, encoding='utf-8'))
    except Exception:
        alt = []
    fremde = [n for n in alt if n not in ALT and n not in [datei(p) for p in pakete]]
    ix = [datei(p) for p in pakete] + fremde
    with open(ix_path, 'w', encoding='utf-8') as f:
        json.dump(ix, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print('Aufgaben gesamt:', sum(len(p['aufgaben']) for p in pakete))
    print('index.json:', ix)


if __name__ == '__main__':
    main()
