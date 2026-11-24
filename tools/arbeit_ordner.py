#!/usr/bin/env python3
"""Legt für eine Klassenarbeit einen Unterordner an und verschiebt die (Teil-)Pakete hinein (oder wieder heraus).

In der App erscheinen die Pakete dieses Ordners unter „Pakete aus dem Repo“ als eigene, aufklappbare Gruppe
(z. B. „Deutscharbeit 02.12.2026“) mit dem Knopf „Alle hinzufügen“. Bereits importierte Pakete bleiben unverändert.

Aufruf (im Repo-Ordner):
  python3 tools/arbeit_ordner.py <ordner> <arbeit> <dateiprefix>           # lose Pakete mit Präfix in den Arbeits-Ordner
  python3 tools/arbeit_ordner.py <ordner> <arbeit> <dateiprefix> --zurueck  # wieder lose in die normale Liste

Beispiel: python3 tools/arbeit_ordner.py joel-dario deutscharbeit-02.12.2026 deutsch-
  verschiebt pakete/joel-dario/deutsch-*.json nach pakete/joel-dario/deutscharbeit-02.12.2026/
  und ändert die Einträge in pakete/joel-dario/index.json zu „deutscharbeit-02.12.2026/<datei>“.

Name der Arbeit: Kleinbuchstaben, Zahlen, Bindestriche und Punkte; die App zeigt „deutscharbeit-02.12.2026“ als
„Deutscharbeit 02.12.2026“ an. Wenn die Arbeit vorbei ist: tools/thema_abschliessen.py <ordner> <arbeit>.
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
    ordner, arbeit, prefix = args
    if not re.fullmatch(r'[a-z0-9][a-z0-9.-]*', arbeit) or arbeit == 'abgeschlossen':
        sys.exit('Name der Arbeit: nur Kleinbuchstaben, Zahlen, Bindestriche und Punkte (z. B. deutscharbeit-02.12.2026).')
    basis = os.path.join(REPO, 'pakete', ordner)
    ix_path = os.path.join(basis, 'index.json')
    ix = json.load(open(ix_path, encoding='utf-8'))
    unter = arbeit + '/'
    neu, bewegt = [], []
    for eintrag in ix:
        name = eintrag.split('/')[-1]
        if not zurueck and '/' not in eintrag and name.startswith(prefix):
            ziel = unter + name
            verschieben(os.path.join(basis, name), os.path.join(basis, ziel))
            neu.append(ziel); bewegt.append(name)
        elif zurueck and eintrag.startswith(unter) and '/' not in eintrag[len(unter):] and name.startswith(prefix):
            verschieben(os.path.join(basis, eintrag), os.path.join(basis, name))
            neu.append(name); bewegt.append(name)
        else:
            neu.append(eintrag)
    if not bewegt:
        sys.exit(f'Keine passenden Pakete mit dem Präfix „{prefix}“ gefunden.')
    with open(ix_path, 'w', encoding='utf-8') as f:
        json.dump(neu, f, ensure_ascii=False, indent=1)
        f.write('\n')
    if zurueck:
        try:
            os.rmdir(os.path.join(basis, arbeit))   # leeren Arbeits-Ordner entfernen
        except OSError:
            pass
    print((f'Zurück in die normale Liste von pakete/{ordner}/: ' if zurueck else f'Verschoben nach pakete/{ordner}/{arbeit}/: ') + f'{len(bewegt)} Pakete')
    for n in bewegt:
        print('  ', n)


if __name__ == '__main__':
    main(sys.argv[1:])
