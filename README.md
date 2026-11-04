# Lernhilfe

Aufgaben für Klassenarbeiten am Bildschirm statt auf Papier. Läuft als Web-App im Browser (Laptop/PC), ohne Server und ohne Anmeldung, genau wie der Quiz-Abend. Beim Öffnen fragt die App zuerst, **wer lernt** (Joel, Dario oder Saskia). Jede Person hat ihre eigenen Lernpakete und Ergebnisse.

## Dateien

- `index.html` – die komplette App
- `pakete/<person>/` – Lernpakete im Repo, je Person ein Ordner (`pakete/joel/`, `pakete/dario/`, `pakete/saskia/`) mit einer `index.json`, die die Dateien dieser Person auflistet. Dazu der **gemeinsame Ordner `pakete/joel-dario/`** für Pakete, die beide lernen sollen (Joel und Dario sind Klassenkameraden): Er wird bei beiden unter „Pakete aus dem Repo“ angezeigt. Bei Joel: Englisch und Musik (nur Joel), Geografie (gemeinsam mit Dario)
- `tools/build_beispielpakete.py` – erzeugt das Englischpaket (liegt jetzt unter `pakete/joel/abgeschlossen/englisch/`) neu (nur nötig, wenn du es ändern willst)
- `tools/thema_abschliessen.py` – verschiebt alle Pakete eines Themas in `abgeschlossen/<thema>/` (oder zurück), siehe „Abgeschlossene Themen“
- `tools/build_geografie.py` – erzeugt die elf Geografiepakete (inklusive Probearbeit und Crashkurs) in `pakete/joel-dario/` (Aufgaben, Zeichnungen und Lösungen werden in `tools/geo_*.py` berechnet und mit `assert` geprüft; `geo_lib.py` enthält die Bausteine und die Zeichnungen von Gezeiten, Watt und Deich, `geo_svg2.py` Düne, Sieltor und Deichprofile)
- `tools/build_musikpakete.py` – erzeugt die drei Musikpakete (liegen jetzt unter `pakete/joel/abgeschlossen/musik/`); `tools/notation.py` zeichnet dafür die Notenbilder (SVG), `tools/glyphs.json` enthält die Zeichen dazu (Schlüssel, Pausen, Kreuz aus GNU FreeFont, Ziffern aus DejaVu Sans Bold)

## Einrichten auf GitHub

1. Neues Repository anlegen, z. B. `lernhilfe`.
2. `index.html`, `README.md` und den Ordner `pakete/` (mit den Unterordnern) hochladen (im Browser: „Add file“ → „Upload files“, Ordner per Drag & Drop).
3. Settings → Pages → „Deploy from a branch“ → Branch `main`, Ordner `/ (root)`.
4. Nach ein bis zwei Minuten ist die App unter `https://<name>.github.io/lernhilfe/` erreichbar. Diesen Link auf dem Laptop als Lesezeichen speichern. Wer direkt bei sich landen will, speichert `…/lernhilfe/#/joel`, `…/lernhilfe/#/dario` oder `…/lernhilfe/#/saskia`.

Zum Ausprobieren reicht es auch, `index.html` per Doppelklick zu öffnen. Nur „Pakete aus dem Repo“ geht dann nicht, das Importieren per Datei funktioniert immer.

## Wer lernt? (Personen)

- Die Startseite zeigt alle Personen mit der Zahl ihrer Pakete. Ein Klick öffnet den eigenen Bereich, oben rechts wechselt man mit dem Namen wieder zurück.
- **Pakete, Ergebnisse, laufende Sitzung und Sicherung sind je Person getrennt.** Dasselbe Paket kann bei mehreren liegen, die Ergebnisse vermischen sich nicht.
- Importiert man ein Paket (oder eine Sicherung), das laut `person` für jemand anderen gedacht ist, fragt die App vorher nach.
- Das ist eine Ordnungshilfe und **keine Zugangssperre**: Jeder, der den Link und den Browser hat, kann jeden Bereich öffnen.
- Saskia sieht „Probeklausur“ statt „Probearbeit“ und den Hinweis „fürs Studium“. Das steuert das Feld `art` in der Personenliste.
- **Optik:** Standardmäßig dunkel, mit dem Sonne/Mond-Knopf oben rechts lässt sich auf hell umschalten (wird pro Gerät gemerkt). Jede Person hat ihre eigene Akzentfarbe, Joel gold, Dario violett, Saskia türkis. Fächer bekommen automatisch ein Symbol und eine Farbe. Die Schriften kommen vom Gerät (Überschriften auf Windows in Bahnschrift), es werden keine Schriften aus dem Internet geladen.
- **Weitere Person (z. B. Aurelio oder Lili) ergänzen:** In `index.html` steht oben im Skript die Liste `PERSONEN`. Eine Zeile mehr genügt, z. B. `{ id: 'aurelio', name: 'Aurelio', art: 'kind', farbe: '#7a4fd0', h: 280 }`. Danach den Ordner `pakete/aurelio/` mit einer `index.json` (`[]`) anlegen, wenn Pakete im Repo liegen sollen. Eine eigene Akzentfarbe gibt es mit einer Zeile `html[data-p=aurelio]{…}` im CSS (Vorlage: die Zeilen für `dario`).
- **Gemeinsame Ordner:** Jede Person lädt in der Repo-Bibliothek die Ordner aus ihrem Feld `ordner` (Standard: nur `pakete/<id>/`). Bei Joel und Dario steht dort zusätzlich `joel-dario`. Ein Paket für beide bekommt `"person": ["joel", "dario"]` und liegt in `pakete/joel-dario/` (mit Eintrag in der `index.json` dort). Pakete nur für Joel (z. B. Musik) bleiben in `pakete/joel/`.
- **Altdaten:** Wer die App schon vor den Profilen benutzt hat, findet alles bei **Joel** wieder. Beim ersten Öffnen von Joels Bereich wird der alte Speicherstand (`lernhilfe.v1`) dorthin kopiert. Die alte Kopie bleibt im Browser unangetastet liegen.

## So kommen Aufgaben in die App

1. In Claude ein **Lernpaket** erstellen lassen (für Joels Schulaufgaben im Projekt „Schulaufgaben“), zum Beispiel: „Erstelle ein Lernpaket im Lernhilfe-Format für Joel, Mathe Klasse 6, Thema Brüche. Hier ist die Themenliste vom Lehrer: …“
2. Die JSON-Datei herunterladen.
3. In der App zuerst die Person wählen, dann auf **Lernpaket importieren** klicken oder die Datei in das Fenster ziehen. Alternativ **Text einfügen**.
4. Gibt es ein Paket mit derselben `id` schon, fragt die App, ob die neue Fassung die alte ersetzen soll. Ergebnisse bleiben dabei erhalten. So lassen sich Korrekturen leicht einspielen.

Fehlerhafte Pakete werden nicht importiert. Die App nennt dann die Stelle (z. B. „Aufgabe 4 (mc): …“). Diese Meldung einfach an Claude schicken.

**Alternative über GitHub:** Die Paketdatei in den Ordner der Person legen (`pakete/joel/`, `pakete/dario/`, `pakete/saskia/` oder für Joel und Dario gemeinsam `pakete/joel-dario/`) und ihren Namen in der `index.json` dieses Ordners ergänzen. Dann erscheint sie bei dieser Person unter „Pakete aus dem Repo“. Achtung: Ist das Repository öffentlich, sind diese Dateien öffentlich. Alles, was nicht jeder lesen soll (oder aus urheberrechtlich geschützten Schulbüchern, Skripten und Unterlagen der Hochschule stammt), besser nur per Datei importieren. Dann bleibt es lokal im Browser.

**Abgeschlossene Themen:** Damit „Pakete aus dem Repo“ übersichtlich bleibt, lassen sich alle Pakete eines Themas in einen Unterordner verschieben. Sie liegen dann in `pakete/<ordner>/abgeschlossen/<thema>/` und stehen in der `index.json` als `abgeschlossen/<thema>/<datei>.json`. In der App erscheinen sie unten in der aufklappbaren Gruppe „Abgeschlossen“, darin ein Eintrag je Thema (zum Beispiel „Englisch“ und „Musik“, die bei Joel schon dort liegen). Verschoben wird nur auf Anweisung, mit `python3 tools/thema_abschliessen.py <ordner> <thema> <dateiprefix>` (zum Beispiel `joel-dario geografie geografie-`), mit `--zurueck` wieder zurück. Schon in der App importierte Pakete bleiben dabei unverändert.

## Üben und Probearbeit

- **Üben:** Nach jeder Aufgabe gibt es sofort die Auswertung, die richtige Lösung und eine kurze Erklärung. Tipps sind möglich. „Weiß ich nicht“ zeigt die Lösung. Am Ende können die Fehler gezielt wiederholt werden.
- **Probearbeit:** Wie in der Schule. Man kann zwischen den Aufgaben springen, es gibt keine Tipps und keine Auswertung, bis man abgibt.
- Standardmäßig bietet jedes Paket beide Wege an. Mit `"probe": false` im Paket entfällt der Knopf „Probearbeit“ (gedacht für Teilpakete, wenn es für die ganze Arbeit eine gemeinsame Probearbeit gibt). Mit `"ueben": false` entfällt umgekehrt der Knopf „Üben“ (gedacht für das Probearbeit-Paket selbst, das nur zum Proben da ist). Beides zusammen ist nicht erlaubt.
- Freie Antworten (Sätze, Erklärungen) bewertet das Kind selbst anhand der Musterlösung und einer Checkliste (Passt / Teilweise / Noch nicht).
- Eine laufende Sitzung bleibt beim Neuladen oder Schließen des Browsers erhalten („Fortsetzen“ auf der Startseite).
- Auf der Startseite steht je Paket der Verlauf der letzten Ergebnisse in Prozent.
- Groß- und Kleinschreibung zählt beim Prüfen nicht (für strenge Aufgaben `"gross": true` setzen), ebenso nicht der Punkt oder das Fragezeichen am Ende. ß und ss gelten als gleich.

## Speicher und Sicherung

Pakete, Ergebnisse und die laufende Aufgabe liegen nur im Browser des jeweiligen Geräts (und Browser-Profils), getrennt je Person (`lernhilfe.v2.joel`, `lernhilfe.v2.dario`, `lernhilfe.v2.saskia`). Mit **Sicherung** (oben rechts, gilt für die gerade gewählte Person) lässt sich alles als Datei speichern oder als Text kopieren und über denselben Import wiederherstellen. Wer an mehreren Geräten lernt, sichert und stellt je Person wieder her.

## Format eines Lernpakets

```json
{
  "typ": "lernpaket",
  "version": 1,
  "id": "mathe-bruchrechnen-6",
  "titel": "Mathe: Brüche",
  "fach": "Mathe",
  "klasse": "6",
  "person": "joel",
  "beschreibung": "Optionaler Text für die Karte",
  "hinweis": "Optional, z. B. was noch geprüft werden muss",
  "lernblatt": [
    { "titel": "Brüche kürzen", "text": "- Zähler und Nenner durch dieselbe Zahl teilen", "merke": "Optional", "bild": "Optional: SVG-Code oder Bilddatei" }
  ],
  "aufgaben": [ ... ]
}
```

Pflicht sind `typ`, `id` (Buchstaben, Zahlen, `-`, `_`), `titel` und `aufgaben`. `person` ist optional (`joel`, `dario`, `saskia` oder eine Liste wie `["joel", "dario"]`): Es sagt, für wen das Paket gedacht ist, und löst beim Import in einen fremden Bereich eine Rückfrage aus. `klasse` ist frei: Eine Zahl wird als „Klasse 6“ angezeigt, anderer Text (z. B. „2. Semester“) unverändert. In Texten gelten `**fett**`, Zeilenumbruch `\n` und Listen mit `- `.

### Felder, die jede Aufgabe haben kann

| Feld | Bedeutung |
|---|---|
| `typ` | Aufgabenart (siehe unten) |
| `frage` | Aufgabenstellung (Pflicht) |
| `abschnitt` | Kleine Überschrift über der Aufgabe, z. B. „Block A“ |
| `text` | Lesetext über der Aufgabe (bei `luecke`: der Lückentext) |
| `bild` | SVG-Code (beginnt mit `<svg`) oder eine Bilddatei im Repo; `bildAlt` ist die Beschreibung |
| `vorlesen` | `{ "text": "...", "sprache": "en-GB" }` – Knopf „Anhören“; der Text steht für Eltern aufklappbar darunter |
| `tipp` | Nur beim Üben, per Knopf |
| `info` | Erklärung, die nach dem Prüfen erscheint |
| `punkte` | Punkte der Aufgabe (Standard 1, bei `frei` 2) |

### Aufgabenarten

| `typ` | Felder | Punkte |
|---|---|---|
| `mc` | `antworten` (Liste), `richtig` (Nummer ab 0, oder Liste von Nummern bei mehreren richtigen), optional `mischen: false` | eine richtige Antwort: alles oder nichts. Bei einer Liste: richtige Kreuze minus falsche Kreuze, anteilig |
| `tf` | `richtig`: `true` oder `false` | 1 |
| `kurz` | `richtig`: Text oder Liste erlaubter Texte; optional `einheit`, `toleranz` bei Zahlen | 1 |
| `luecke` | `text` mit Lücken `{{richtig}}` oder `{{richtig\|auch richtig}}`; optional `auswahl` (Lücken werden Auswahllisten), `wortbank` (Wörter zum **Ziehen**: die Lücken werden zu Feldern, in die man die Wörter per Drag & Drop (Maus oder Finger) oder Antippen setzt, ideal für Tablets und für Symbole wie α, β, H₀; die richtigen Antworten kommen automatisch dazu, falsche Wörter dürfen als Ablenkung drin stehen, ein Wort darf mehrfach verwendet werden; per Knopf kann man auf Tippen umschalten). Zahlenlücken bleiben Eingabefelder | 1 je Lücke |
| `zuordnen` | `paare`: `[["links","rechts"], ...]`, optional `extra` (falsche Antworten zur Ablenkung) | 1 je Paar |
| `reihenfolge` | `schritte` in der richtigen Reihenfolge (die App mischt sie) | anteilig |
| `frei` | `muster` (Musterlösung), optional `kriterien` (Checkliste) | Selbstbewertung |

## Hinweise zu den Beispielpaketen

- **Englisch** ist frei formuliert und passt zu den Themen von Unit 1 (was/were, simple past, did, Hören, Telefonieren, Schreiben).
- **Geografie** (Klasse 6, für Joel und Dario, 11 Pakete mit zusammen rund 450 Aufgaben): Teil 1 Nord- und Ostsee, Teil 2a/2b Gezeiten (Grundlagen, Kurve und Tidenkalender), Teil 3a/3b Wattenmeer (Lebensraum und Zonen, Schutz), Teil 4a bis 4d Küstenschutz (Deich, Deich beschriften und Deichhöhen, Dünen, Sieltor) eine eigene Probearbeit mit 48 Punkten (etwa 45 Minuten, alle Aufgaben neu) und ein **Crashkurs** („Das Wichtigste kurz gefasst“ für den letzten Blick am Tag vor der Arbeit: kurzes Lernblatt mit Checkliste und Tipps plus Blitz-Check mit zwölf Aufgaben, ohne Knopf „Probearbeit“). Jedes Übungspaket hat ein Lernblatt und 34 bis 68 Aufgaben in Blöcken. Die Zeichnungen sind selbst gezeichnet, die Tidenkalender und Kurven erfunden. Die vierte Zone des Watts heißt im Buch „Düne“, im Arbeitsblatt „Deich“: Die Aufgaben werten beides als richtig. Die Probearbeit ist selbst entworfen, weil der Lehrer keine vorgegeben hat.
- „Anhören“ nutzt die Stimme des Browsers (am besten in Chrome oder Edge). Die Qualität hängt vom Gerät ab. Der Text zum Vorlesen für die Eltern ist immer aufklappbar.
- **Musik** (drei Pakete für Klasse 6): Notennamen/Notenwerte/Vorzeichen, Pausen/Taktarten und eine Probearbeit mit 38 Punkten (Lied, Chanson, Bilder einer Ausstellung, Hören). Die Notenbilder sind SVG und entstehen aus den Aufgabendaten, die Lösungen passen also zu den Bildern. Zeichenaufgaben vom Papier sind als Auswahlaufgaben umgebaut. Das Zeichnen selbst bleibt Papierarbeit (das Lernblatt erklärt, wie). Teil D (Hören) braucht Musikausschnitte auf einem zweiten Gerät. Die Stückbeschreibungen wurden nicht angehört und sollten beim Zuhören geprüft werden. Merkmale und Schreibweisen aus dem Unterricht haben Vorrang.
