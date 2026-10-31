# Lernhilfe

Aufgaben für Klassenarbeiten am Bildschirm statt auf Papier. Läuft als Web-App im Browser (Laptop/PC), ohne Server und ohne Anmeldung, genau wie der Quiz-Abend.

## Dateien

- `index.html` – die komplette App
- `pakete/` – Beispiel-Lernpakete (Englisch, Geografie) und `index.json` mit der Liste der Dateien
- `tools/build_beispielpakete.py` – erzeugt die Beispielpakete neu (nur nötig, wenn du sie ändern willst)

## Einrichten auf GitHub

1. Neues Repository anlegen, z. B. `lernhilfe`.
2. `index.html`, `README.md` und den Ordner `pakete/` hochladen (im Browser: „Add file“ → „Upload files“, Ordner per Drag & Drop).
3. Settings → Pages → „Deploy from a branch“ → Branch `main`, Ordner `/ (root)`.
4. Nach ein bis zwei Minuten ist die App unter `https://<name>.github.io/lernhilfe/` erreichbar. Diesen Link auf dem Laptop der Kinder als Lesezeichen speichern.

Zum Ausprobieren reicht es auch, `index.html` per Doppelklick zu öffnen. Nur „Pakete aus dem Repo“ geht dann nicht, das Importieren per Datei funktioniert immer.

## So kommen Aufgaben in die App

1. Im Claude-Projekt „Schulaufgaben“ ein **Lernpaket** erstellen lassen, zum Beispiel: „Erstelle ein Lernpaket im Lernhilfe-Format für Joel, Mathe Klasse 6, Thema Brüche. Hier ist die Themenliste vom Lehrer: …“
2. Die JSON-Datei herunterladen.
3. In der App auf **Lernpaket importieren** klicken oder die Datei in das Fenster ziehen. Alternativ **Text einfügen**.
4. Gibt es ein Paket mit derselben `id` schon, fragt die App, ob die neue Fassung die alte ersetzen soll. Ergebnisse bleiben dabei erhalten. So lassen sich Korrekturen leicht einspielen.

Fehlerhafte Pakete werden nicht importiert. Die App nennt dann die Stelle (z. B. „Aufgabe 4 (mc): …“). Diese Meldung einfach an Claude schicken.

**Alternative über GitHub:** Die Paketdatei in den Ordner `pakete/` legen und ihren Namen in `pakete/index.json` ergänzen. Dann erscheint sie in der App unter „Pakete aus dem Repo“. Achtung: Ist das Repository öffentlich, sind diese Dateien öffentlich. Alles, was nicht jeder lesen soll (oder aus urheberrechtlich geschützten Schulbüchern stammt), besser nur per Datei importieren. Dann bleibt es lokal im Browser.

## Üben und Probearbeit

- **Üben:** Nach jeder Aufgabe gibt es sofort die Auswertung, die richtige Lösung und eine kurze Erklärung. Tipps sind möglich. „Weiß ich nicht“ zeigt die Lösung. Am Ende können die Fehler gezielt wiederholt werden.
- **Probearbeit:** Wie in der Schule. Man kann zwischen den Aufgaben springen, es gibt keine Tipps und keine Auswertung, bis man abgibt.
- Freie Antworten (Sätze, Erklärungen) bewertet das Kind selbst anhand der Musterlösung und einer Checkliste (Passt / Teilweise / Noch nicht).
- Eine laufende Sitzung bleibt beim Neuladen oder Schließen des Browsers erhalten („Fortsetzen“ auf der Startseite).
- Auf der Startseite steht je Paket der Verlauf der letzten Ergebnisse in Prozent.
- Groß- und Kleinschreibung zählt beim Prüfen nicht (für strenge Aufgaben `"gross": true` setzen), ebenso nicht der Punkt oder das Fragezeichen am Ende. ß und ss gelten als gleich.

## Speicher und Sicherung

Pakete, Ergebnisse und die laufende Aufgabe liegen nur im Browser des jeweiligen Geräts (und Browser-Profils). Jedes Kind, das mit einem eigenen Profil oder Gerät lernt, hat also eigene Ergebnisse. Mit **Sicherung** (oben rechts) lässt sich alles als Datei speichern oder als Text kopieren und über denselben Import wiederherstellen.

## Format eines Lernpakets

```json
{
  "typ": "lernpaket",
  "version": 1,
  "id": "mathe-bruchrechnen-6",
  "titel": "Mathe: Brüche",
  "fach": "Mathe",
  "klasse": "6",
  "kind": "Joel",
  "beschreibung": "Optionaler Text für die Karte",
  "hinweis": "Optional, z. B. was noch geprüft werden muss",
  "lernblatt": [
    { "titel": "Brüche kürzen", "text": "- Zähler und Nenner durch dieselbe Zahl teilen", "merke": "Optional" }
  ],
  "aufgaben": [ ... ]
}
```

Pflicht sind `typ`, `id` (Buchstaben, Zahlen, `-`, `_`), `titel` und `aufgaben`. In Texten gelten `**fett**`, Zeilenumbruch `\n` und Listen mit `- `.

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
| `mc` | `antworten` (Liste), `richtig` (Nummer ab 0, oder Liste von Nummern bei mehreren richtigen), optional `mischen: false` | alles oder nichts |
| `tf` | `richtig`: `true` oder `false` | 1 |
| `kurz` | `richtig`: Text oder Liste erlaubter Texte; optional `einheit`, `toleranz` bei Zahlen | 1 |
| `luecke` | `text` mit Lücken `{{richtig}}` oder `{{richtig\|auch richtig}}`; optional `auswahl` (Lücken werden Auswahllisten), `wortbank` (Wörter zur Hilfe) | 1 je Lücke |
| `zuordnen` | `paare`: `[["links","rechts"], ...]`, optional `extra` (falsche Antworten zur Ablenkung) | 1 je Paar |
| `reihenfolge` | `schritte` in der richtigen Reihenfolge (die App mischt sie) | anteilig |
| `frei` | `muster` (Musterlösung), optional `kriterien` (Checkliste) | Selbstbewertung |

## Hinweise zu den Beispielpaketen

- **Englisch** ist frei formuliert und passt zu den Themen von Unit 1 (was/were, simple past, did, Hören, Telefonieren, Schreiben).
- **Geografie** ist ein Entwurf. Die Schutzzonen im Nationalpark und die Jahreszahlen sollten mit Joels Unterlagen abgeglichen werden. Auch die vierte Zone des Wattenmeeres (Düne oder Deich) ist darin bewusst nicht enthalten, weil Buch und Arbeitsblatt sich dort unterscheiden.
- „Anhören“ nutzt die Stimme des Browsers (am besten in Chrome oder Edge). Die Qualität hängt vom Gerät ab. Der Text zum Vorlesen für die Eltern ist immer aufklappbar.
