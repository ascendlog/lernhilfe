#!/usr/bin/env python3
"""Verschiebt ein Thema oder eine ganze Arbeit in den Unterordner „abgeschlossen/<name>/“ (oder zurück).

In der App stehen diese Pakete unter „Pakete aus dem Repo“ in der Gruppe „Abgeschlossen“ → „<Name>“ und
stören die Übersicht der aktuellen Themen nicht mehr. Bereits importierte Pakete der Kinder bleiben unverändert.

Aufruf (im Repo-Ordner):
  python3 tools/thema_abschliessen.py <ordner> <thema> <dateiprefix>          # lose Pakete mit Präfix verschieben
  python3 tools/thema_abschliessen.py <ordner> <thema> <dateiprefix> --zurueck # wieder zurück in die normale Liste
  python3 tools/thema_abschliessen.py <ordner> <arbeit>                        # ganzen Arbeits-Ordner verschieben
  python3 tools/thema_abschliessen.py <ordner> <arbeit> --zurueck              # Arbeits-Ordner wieder zurückholen

Beispiele:
  python3 tools/thema_abschliessen.py joel-dario geografie geografie-
    verschiebt pakete/joel-dario/geografie-*.json nach pakete/joel-dario/abgeschlossen/geografie/
    und ändert die Einträge in pakete/joel-dario/index.json zu „abgeschlossen/geografie/<datei>“.
  python3 tools/thema_abschliessen.py joel-dario deutscharbeit-02.12.2026
    verschiebt pakete/joel-dario/deutscharbeit-02.12.2026/ (alle Pakete dieser Arbeit) nach .../abgeschlossen/.
Mit `git mv`, wenn das Repo ein Git-Repository ist (sonst normales Verschieben).
Arbeits-Ordner legt tools/arbeit_ordner.py an.
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
    if len(args) not in (2, 3):
        sys.exit(__doc__)
    ordner, thema = args[0], args[1]
    prefix = args[2] if len(args) == 3 else None   # ohne Präfix: ganzer Arbeits-Ordner
    if not re.fullmatch(r'[a-z0-9][a-z0-9.-]*', thema) or thema == 'abgeschlossen':
        sys.exit('Name: nur Kleinbuchstaben, Zahlen, Bindestriche und Punkte (z. B. geografie oder deutscharbeit-02.12.2026).')
    basis = os.path.join(REPO, 'pakete', ordner)
    ix_path = os.path.join(basis, 'index.json')
    ix = json.load(open(ix_path, encoding='utf-8'))
    unter = f'abgeschlossen/{thema}/'
    neu, bewegt = [], []
    if prefix is None:
        # ganzer Arbeits-Ordner: <thema>/<datei> <-> abgeschlossen/<thema>/<datei>
        von, nach = (unter, thema + '/') if zurueck else (thema + '/', unter)
        for eintrag in ix:
            if eintrag.startswith(von) and '/' not in eintrag[len(von):]:
                ziel = nach + eintrag[len(von):]
                verschieben(os.path.join(basis, eintrag), os.path.join(basis, ziel))
                neu.append(ziel); bewegt.append(eintrag[len(von):])
            else:
                neu.append(eintrag)
        if not bewegt:
            sys.exit(f'Keine Pakete in „{von}“ gefunden (Name der Arbeit prüfen, siehe index.json).')
    else:
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
    elif prefix is None:
        try:
            os.rmdir(os.path.join(basis, thema))   # leeren Arbeits-Ordner entfernen
        except OSError:
            pass
    if prefix is None:
        print((f'Zurück nach pakete/{ordner}/{thema}/: ' if zurueck else f'Verschoben nach pakete/{ordner}/abgeschlossen/{thema}/: ') + f'{len(bewegt)} Pakete')
    else:
        print(('Zurück in die normale Liste: ' if zurueck else f'Verschoben nach pakete/{ordner}/abgeschlossen/{thema}/: ') + f'{len(bewegt)} Pakete')
    for n in bewegt:
        print('  ', n)


if __name__ == '__main__':
    main(sys.argv[1:])
