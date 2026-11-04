"""Gemeinsame Hilfe für die Build-Skripte: Liegt ein Thema schon unter pakete/<ordner>/abgeschlossen/<thema>/,
wird dort weitergeschrieben statt eine zweite Kopie im normalen Ordner anzulegen (siehe thema_abschliessen.py)."""
import os


def ziel(basis, thema, dateiname):
    abg = os.path.join(basis, 'abgeschlossen', thema)
    return abg if os.path.exists(os.path.join(abg, dateiname)) else basis


def hat_eintrag(ix, dateiname):
    """True, wenn die index.json den Dateinamen schon kennt (auch mit Unterpfad abgeschlossen/<thema>/...)."""
    return any(e.split('/')[-1] == dateiname for e in ix)
