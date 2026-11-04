#!/usr/bin/env python3
"""Verschiebt alle Pakete eines Themas in den Unterordner „abgeschlossen/<thema>/“ (oder zurück).

In der App stehen diese Pakete unter „Pakete aus dem Repo“ in der Gruppe „Abgeschlossen“ → „<Thema>“ und
stören die Übersicht der aktuellen Themen nicht mehr. Bereits importierte Pakete der Kinder bleiben unverändert.

Aufruf (im Repo-Ordner):
  python3 tools/thema_abschliessen.py <ordner> <thema> <dateiprefix>          # verschieben
  python3 tools/thema_abschliessen.py <ordner> <thema> <dateiprefix> --zurueck # wieder zurück in die normale Liste

Beispiel: python3 tools/thema_abschliessen.py joel-dario geografie geografie-
  verschiebt pakete/joel-dario/geografie-*.json nach pakete/joel-dario/abgeschlossen/geografie/
  und ändert die Einträge in pakete/joel-dario/index.json zu „abgeschlossen/geografie/<datei>“.
Mit `git mv`, wenn das Repo ein Git-Repository ist (sonst normales Verschieben).
"""
import json
import os
import re
import subprocess
import sys

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')


def verschieben(a, b):
    os.makedirs(os.path.dirname(b), exist_ok=True)
    if os.path.exists(b):
        os.remove(b)   # alte Fassung im Ziel ersetzen
    r = subprocess.run(['git', 'mv', '-f', a, b], cwd=REPO, capture_output=True)
    if r.returncode != 0:
        os.replace(a, b)


def main(argv):
    zurueck = '--zurueck' in argv
    args = [x for x in argv if not x.startswith('--')]
    if len(args) != 3:
        sys.exit(__doc__)
    ordner, thema, prefix = args
    if not re.fullmatch(r'[a-z0-9][a-z0-9-]*', thema):
        sys.exit('Thema: nur Kleinbuchstaben, Zahlen und Bindestriche (z. B. geografie).')
    basis = os.path.join(REPO, 'pakete', ordner)
    ix_path = os.path.join(basis, 'index.json')
    ix = json.load(open(ix_path, encoding='utf-8'))
    unter = f'abgeschlossen/{thema}/'
    neu, bewegt = [], []
    for eintrag in ix:
        name = eintrag.split('/')[-1]
        if not zurueck and '/' not in eintrag and name.startswith(prefix):
            ziel = unter + name
            verschieben(os.path.join(basis, name), os.path.join(basis, ziel))
            neu.append(ziel); bewegt.append(name)
        elif zurueck and eintrag.startswith(unter) and name.startswith(prefix):
            verschieben(os.path.join(basis, eintrag), os.path.join(basis, name))
            neu.append(name); bewegt.append(name)
        else:
            neu.append(eintrag)
    if not bewegt:
        sys.exit(f'Keine Pakete mit dem Präfix „{prefix}“ gefunden.')
    with open(ix_path, 'w', encoding='utf-8') as f:
        json.dump(neu, f, ensure_ascii=False, indent=1)
        f.write('\n')
    if zurueck:
        try:
            os.rmdir(os.path.join(basis, 'abgeschlossen', thema)); os.rmdir(os.path.join(basis, 'abgeschlossen'))
        except OSError:
            pass
    print(('Zurück in die normale Liste: ' if zurueck else f'Verschoben nach pakete/{ordner}/abgeschlossen/{thema}/: ') + f'{len(bewegt)} Pakete')
    for n in bewegt:
        print('  ', n)


if __name__ == '__main__':
    main(sys.argv[1:])
