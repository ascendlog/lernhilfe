#!/usr/bin/env python3
"""Erzeugt aus index.html eine eigenständige Kopie der Lernhilfe für eine andere Familie.

Aufruf:   python3 tools/kopie_erstellen.py KONFIG.json [AUSGABEORDNER]

Die Namen stehen NICHT in diesem Skript, sondern in der Konfigurationsdatei (liegt außerhalb des Repos):
{
  "ausgabe": "/pfad/zum/ausgabeordner",
  "personen": [
    {"id": "anna", "name": "Anna", "klasse": "6", "farbe": "#5ec2ff", "h": 205, "auf_akzent": "#06202e", "akzent_hell": "#0b5a80"},
    {"id": "ben",  "name": "Ben",  "klasse": "5", "farbe": "#ff9e7d", "h": 14,  "auf_akzent": "#3a1306", "akzent_hell": "#a63d1a"}
  ],
  "verboten": ["…Namen, die in der Kopie nirgends vorkommen dürfen…"]
}
Die Kopie enthält: index.html (Personenliste ersetzt, keine Namen der Ursprungsfamilie, keine Repo-Pakete),
manifest und Icons, anleitung.html, vorlage.txt (für das Claude der Eltern), beispielpaket.json, README.md.
Am Ende wird die Kopie nach den verbotenen Namen durchsucht; findet das Skript einen, bricht es ab.
"""
import json, os, re, shutil, subprocess, sys

HIER = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HIER)
KOPIE = os.path.join(HIER, 'kopie')


def fehler(msg):
    print('FEHLER:', msg, file=sys.stderr)
    sys.exit(1)


def ersetze(s, muster, neu, anzahl=1, flags=re.S, name=''):
    """Regex-Ersetzung mit Pflicht-Trefferzahl: ändert sich index.html, bricht das Skript ab statt still falsch zu kopieren."""
    s2, n = re.subn(muster, neu, s, flags=flags)
    if n != anzahl:
        fehler(f'Ersetzung „{name or muster[:50]}“: {n} Treffer statt {anzahl}. index.html hat sich geändert, Skript anpassen.')
    return s2


# ---- Kontrast (WCAG), damit gewählte Farben lesbar bleiben ----
def _lin(c):
    c /= 255
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

def _lum(rgb):
    r, g, b = (_lin(x) for x in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def _hex(h):
    h = h.lstrip('#'); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

def _hsl(h, s, l):  # h in Grad, s und l in Prozent
    s /= 100; l /= 100
    k = lambda n: (n + h / 30) % 12
    a = s * min(l, 1 - l)
    f = lambda n: l - a * max(-1, min(k(n) - 3, 9 - k(n), 1))
    return tuple(round(255 * f(n)) for n in (0, 8, 4))

def kontrast(a, b):
    la, lb = _lum(a), _lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def pruefe_farben(p):
    dunkel_bg = _hsl(p['h'], 34, 8)
    dunkel_flaeche = _hsl(p['h'], 27, 13)
    hell_bg = _hsl(p['h'], 38, 96)
    tests = [
        ('Akzent auf dunklem Hintergrund', _hex(p['farbe']), dunkel_bg, 4.5),
        ('Akzent auf dunkler Fläche', _hex(p['farbe']), dunkel_flaeche, 4.5),
        ('Schrift auf Akzentknopf', _hex(p['auf_akzent']), _hex(p['farbe']), 4.5),
        ('Akzentschrift im hellen Design (weiß)', _hex(p['akzent_hell']), (255, 255, 255), 4.5),
        ('Akzentschrift im hellen Design (Hintergrund)', _hex(p['akzent_hell']), hell_bg, 4.5),
    ]
    for t, a, b, soll in tests:
        c = kontrast(a, b)
        if c < soll:
            fehler(f'{p["name"]}: {t}: Kontrast {c:.2f} (mindestens {soll}). Farbe anpassen.')


def lade_konfig(pfad):
    with open(pfad, encoding='utf-8') as f:
        k = json.load(f)
    ps = k.get('personen')
    if not isinstance(ps, list) or len(ps) != 2:
        fehler('„personen“ braucht genau zwei Einträge (die Vorlage für Claude nennt zwei Kinder).')
    for p in ps:
        for f in ('id', 'name', 'klasse', 'farbe', 'h', 'auf_akzent', 'akzent_hell'):
            if f not in p:
                fehler(f'Person ohne Feld „{f}“: {p}')
        if not re.fullmatch(r'[a-z][a-z0-9]*', p['id']):
            fehler(f'id „{p["id"]}“ muss aus Kleinbuchstaben und Zahlen bestehen.')
        for f in ('farbe', 'auf_akzent', 'akzent_hell'):
            if not re.fullmatch(r'#[0-9a-fA-F]{6}', p[f]):
                fehler(f'{f} von {p["name"]} ist keine Farbe wie #5ec2ff.')
        if not isinstance(p['h'], int) or not 0 <= p['h'] <= 360:
            fehler(f'h von {p["name"]} muss eine ganze Zahl von 0 bis 360 sein.')
        pruefe_farben(p)
    if ps[0]['id'] == ps[1]['id']:
        fehler('Die beiden ids müssen verschieden sein.')
    k.setdefault('verboten', [])
    return k


def platzhalter(text, ps):
    for n, p in enumerate(ps, 1):
        text = (text.replace(f'@@KIND{n}_ID@@', p['id']).replace(f'@@KIND{n}_NAME@@', p['name'])
                    .replace(f'@@KIND{n}_KLASSE@@', str(p['klasse'])))
    return text


def kopie_index(s, ps):
    a, b = ps
    # 1. Eigener Speicher: Die Kopie darf sich auf derselben Domain keine Schlüssel mit der Ursprungs-App teilen.
    s, n = re.subn(r"'lernhilfe\.", "'lhfam.", s)
    if n < 10:
        fehler(f'Speicherschlüssel: nur {n} Treffer, erwartet mindestens 10.')

    # 2. Personenliste
    personen = ',\n'.join(
        f"  {{ id: '{p['id']}', name: '{p['name']}', art: 'kind', farbe: '{p['farbe']}', h: {p['h']} }}" for p in ps)
    neu = ("/* Wer die App nutzt. Weitere Person: einfach eine Zeile ergänzen (id klein und ohne Leerzeichen).\n"
           "   Für eine eigene Farbe zusätzlich im CSS oben eine Zeile html[data-p=<id>] ergänzen.\n"
           "   probeMinuten = Zeit der Probearbeit/-klausur in Minuten, wenn das Paket kein eigenes \"dauer\" hat (ohne Angabe: kein Timer). */\n"
           "const PERSONEN = [ /* farbe = Akzent, h = Farbton des „Raums“ (0–360) */\n" + personen + "\n];\n")
    s = ersetze(s, r"/\* Wer die App nutzt\..*?\*/\nconst PERSONEN = \[.*?\n\];\n", lambda m: neu, name='PERSONEN')
    s = ersetze(s, r"const ALT_BESITZER = '[a-z]*'; /\*.*?\*/",
                lambda m: "const ALT_BESITZER = ''; /* kein Speicherstand aus der Zeit vor den Profilen */", name='ALT_BESITZER')

    # 3. Farben je Person
    dunkel = ''.join(
        f"html[data-p={p['id']}]{{--h:{p['h']};--accent:{p['farbe']};--accent-text:{p['farbe']};--on-accent:{p['auf_akzent']}}}\n" for p in ps)
    hell = ''.join(f"html[data-theme=light][data-p={p['id']}]{{--accent-text:{p['akzent_hell']}}}\n" for p in ps)
    for muster, neu_css, nm in ((r"^html\[data-p=\w+\]\{[^\n]*\}\n", dunkel, 'CSS dunkel'),
                                (r"^html\[data-theme=light\]\[data-p=\w+\]\{[^\n]*\}\n", hell, 'CSS hell')):
        treffer = list(re.finditer(muster, s, re.M))
        if not treffer:
            fehler(f'{nm}: keine Zeilen gefunden.')
        for m in reversed(treffer[1:]):
            s = s[:m.start()] + s[m.end():]
        m = treffer[0]
        s = s[:m.start()] + neu_css + s[m.end():]

    # 4. Beispiele in Fehlermeldungen
    s = ersetze(s, r'z\. B\. "[a-z]+"\)', lambda m: f'z. B. "{a["id"]}")', name='Meldung person (Text)')
    s = ersetze(s, r'z\. B\. \["[a-z]+", "[a-z]+"\]\)', lambda m: f'z. B. ["{a["id"]}", "{b["id"]}"])', name='Meldung person (Liste)')

    # 5. Kommentare und Sondertexte der Ursprungsfamilie
    s = ersetze(s, r'\s*\(Meldung von [^)]*\)', lambda m: '', name='Kommentar Meldung')
    s = ersetze(s, r"const rosa = cur && cur\.id === '[a-z]+'; /\*.*?\*/", lambda m: 'const rosa = false;', name='rosa')
    s = ersetze(s, r'damit sich .{0,40}? sehen können', lambda m: 'damit sich zwei Kinder sehen können', name='Kommentar Freunde-Code')
    s = ersetze(s, r' Das Freunde-Album \(.*?\) hat einen eigenen Freunde-Code.*?jederzeit verbergen\.', lambda m: '', name='Hilfetext Freunde-Album')
    s = ersetze(s, r"function elFreundCard\(o\) \{\n.*?\n\}\n", lambda m: '', name='elFreundCard')
    s = ersetze(s, r"  h \+= rw\(\(\) => elFreundCard\(o\), ''\);\n", lambda m: '', name='Aufruf elFreundCard')

    s = ersetze(s, r'Freunde-Album: .{0,40}? sehen sich live', lambda m: 'Freunde-Album: zwei Kinder sehen sich live', name='Kommentar Freunde-Album')
    s = ersetze(s, r'\(nur Kinder, nicht [A-ZÄÖÜ][\wäöüß]*\)', lambda m: '(nur Kinder)', name='Überschrift Eltern')

    # 6. Keine Repo-Pakete: Die Eltern importieren ihre Pakete selbst
    s = ersetze(s, r'<button class="btn sec" data-act="library">Pakete aus dem Repo</button>', lambda m: '', name='Knopf Repo')

    # 7. Verweise auf die Anleitung
    s = ersetze(s, r'(\(Stand der Kinder ansehen\)</p>)',
                lambda m: m.group(1) + '<p class="legend"><a class="link" href="anleitung.html">Anleitung: so kommen Aufgaben in die App</a></p>', name='Link Startseite')
    s = ersetze(s, r'(Du kannst sie auch einfach in dieses Fenster ziehen\.</p>)(</div>)',
                lambda m: m.group(1) + '<p class="muted">Eltern: Die <a class="link" href="anleitung.html">Anleitung</a> enthält eine Vorlage, mit der Claude passende Pakete baut.</p>' + m.group(2), name='Link leere Startseite')
    return s


def node_pruefung(html, pfad):
    if not shutil.which('node'):
        print('Hinweis: node nicht gefunden, Syntaxprüfung übersprungen.'); return
    for i, m in enumerate(re.finditer(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>', html, re.S)):
        tmp = f'{pfad}.script{i}.js'
        with open(tmp, 'w', encoding='utf-8') as f:
            f.write(m.group(1))
        r = subprocess.run(['node', '--check', tmp], capture_output=True, text=True)
        os.remove(tmp)
        if r.returncode:
            fehler('Syntaxfehler in der erzeugten index.html:\n' + r.stderr)


def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    k = lade_konfig(sys.argv[1])
    ziel = sys.argv[2] if len(sys.argv) > 2 else k.get('ausgabe')
    if not ziel:
        fehler('Kein Ausgabeordner (Argument 2 oder „ausgabe“ in der Konfiguration).')
    ps = k['personen']
    os.makedirs(ziel, exist_ok=True)

    with open(os.path.join(REPO, 'index.html'), encoding='utf-8') as f:
        html = kopie_index(f.read(), ps)
    node_pruefung(html, os.path.join(ziel, '.pruefung'))

    def schreibe(name, text):
        with open(os.path.join(ziel, name), 'w', encoding='utf-8', newline='\n') as f:
            f.write(text)

    schreibe('index.html', html)
    shutil.copy(os.path.join(REPO, 'manifest.webmanifest'), os.path.join(ziel, 'manifest.webmanifest'))
    shutil.copytree(os.path.join(REPO, 'icons'), os.path.join(ziel, 'icons'), dirs_exist_ok=True)

    with open(os.path.join(KOPIE, 'vorlage.txt'), encoding='utf-8') as f:
        vorlage = platzhalter(f.read(), ps)
    schreibe('vorlage.txt', vorlage)
    with open(os.path.join(KOPIE, 'anleitung.html'), encoding='utf-8') as f:
        anl = f.read()
    esc = vorlage.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    schreibe('anleitung.html', platzhalter(anl.replace('@@VORLAGE@@', esc), ps))
    shutil.copy(os.path.join(KOPIE, 'beispielpaket.json'), os.path.join(ziel, 'beispielpaket.json'))
    with open(os.path.join(KOPIE, 'README.md'), encoding='utf-8') as f:
        schreibe('README.md', platzhalter(f.read(), ps))

    # Endkontrolle: nichts von der Ursprungsfamilie darf in der Kopie stehen
    verboten = [v for v in k['verboten'] if v.strip()]
    if verboten:
        rx = re.compile(r'\b(?:' + '|'.join(re.escape(v) for v in verboten) + r')\b', re.I)  # ganze Wörter, sonst träfe „lio“ auch „Bibliothek“
        funde = []
        for wurzel, _, dateien in os.walk(ziel):
            if os.sep + '.git' in wurzel + os.sep:
                continue
            for d in dateien:
                if d.lower().endswith(('.png', '.ico', '.jpg')):
                    continue
                p = os.path.join(wurzel, d)
                with open(p, encoding='utf-8', errors='replace') as f:
                    for nr, zeile in enumerate(f, 1):
                        m = rx.search(zeile)
                        if m:
                            funde.append(f'  „{m.group(0)}“ in {os.path.relpath(p, ziel)}, Zeile {nr}: {zeile.strip()[:140]}')
        if funde:
            fehler('Namen der Ursprungsfamilie in der Kopie:\n' + '\n'.join(funde))
    else:
        print('Hinweis: „verboten“ ist leer, keine Endkontrolle auf Namen.')
    print('Kopie erzeugt in', ziel)
    for d in sorted(os.listdir(ziel)):
        print('  ', d)


if __name__ == '__main__':
    main()
