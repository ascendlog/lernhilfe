"""Gemeinsame Hilfe für die Build-Skripte: Liegt ein Paket schon in einem Unterordner (Arbeits-Ordner wie
pakete/<ordner>/deutscharbeit-02.12.2026/ oder pakete/<ordner>/abgeschlossen/<thema>/), wird dort weitergeschrieben
statt eine zweite Kopie im normalen Ordner anzulegen (siehe arbeit_ordner.py und thema_abschliessen.py)."""
import json
import os


def finde(basis, thema, dateiname):
    """(Ordner, Eintrag für index.json) für ein Paket: dort, wo es schon liegt, sonst im Basisordner."""
    try:
        ix = json.load(open(os.path.join(basis, 'index.json'), encoding='utf-8'))
    except Exception:
        ix = []
    for e in ix:   # 1. so, wie es in der index.json steht (Arbeits-Ordner, abgeschlossen/…)
        if e.split('/')[-1] == dateiname and os.path.exists(os.path.join(basis, e)):
            return os.path.join(basis, os.path.dirname(e)), e
    abg = os.path.join(basis, 'abgeschlossen', thema)   # 2. Thema abgeschlossen, Datei schon dort
    if os.path.exists(os.path.join(abg, dateiname)):
        return abg, f'abgeschlossen/{thema}/{dateiname}'
    return basis, dateiname   # 3. neu: normaler Ordner


def ziel(basis, thema, dateiname):
    return finde(basis, thema, dateiname)[0]


def hat_eintrag(ix, dateiname):
    """True, wenn die index.json den Dateinamen schon kennt (auch mit Unterpfad, z. B. deutscharbeit-02.12.2026/…)."""
    return any(e.split('/')[-1] == dateiname for e in ix)
