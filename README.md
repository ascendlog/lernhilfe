# Lernhilfe

Aufgaben für Klassenarbeiten am Bildschirm statt auf Papier. Läuft als Web-App im Browser (Laptop/PC), ohne Server und ohne Anmeldung, genau wie der Quiz-Abend. Beim Öffnen fragt die App zuerst, **wer lernt** (Joel, Dario oder Saskia). Jede Person hat ihre eigenen Lernpakete und Ergebnisse.

## Dateien

- `index.html` – die komplette App
- `pakete/<person>/` – Lernpakete im Repo, je Person ein Ordner (`pakete/joel/`, `pakete/dario/`, `pakete/saskia/`) mit einer `index.json`, die die Dateien dieser Person auflistet. Dazu der **gemeinsame Ordner `pakete/joel-dario/`** für Pakete, die beide lernen sollen (Joel und Dario sind Klassenkameraden): Er wird bei beiden unter „Pakete aus dem Repo“ angezeigt. Bei Joel: Englisch und Musik (nur Joel), Geografie (gemeinsam mit Dario)
- `tools/build_beispielpakete.py` – erzeugt das Englischpaket (liegt jetzt unter `pakete/joel/abgeschlossen/englisch/`) neu (nur nötig, wenn du es ändern willst)
- `tools/thema_abschliessen.py` – verschiebt alle Pakete eines Themas in `abgeschlossen/<thema>/` (oder zurück), siehe „Abgeschlossene Themen“
- `tools/build_geografie.py` – erzeugt die elf Geografiepakete (inklusive Probearbeit und Crashkurs) in `pakete/joel-dario/` (Aufgaben, Zeichnungen und Lösungen werden in `tools/geo_*.py` berechnet und mit `assert` geprüft; `geo_lib.py` enthält die Bausteine und die Zeichnungen von Gezeiten, Watt und Deich, `geo_svg2.py` Düne, Sieltor und Deichprofile, `geo_lesen.py` die Nachlesen-Verweise)
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
3. In der App zuerst die Person wählen, dann oben auf **Verwalten** tippen und auf **Lernpaket importieren** klicken oder die Datei in das Fenster ziehen. Alternativ **Text einfügen**. (Ohne Pakete sind die Importknöpfe gleich sichtbar.)
4. Gibt es ein Paket mit derselben `id` schon, fragt die App, ob die neue Fassung die alte ersetzen soll. Ergebnisse bleiben dabei erhalten. So lassen sich Korrekturen leicht einspielen.

Fehlerhafte Pakete werden nicht importiert. Die App nennt dann die Stelle (z. B. „Aufgabe 4 (mc): …“). Diese Meldung einfach an Claude schicken.

**Alternative über GitHub:** Die Paketdatei in den Ordner der Person legen (`pakete/joel/`, `pakete/dario/`, `pakete/saskia/` oder für Joel und Dario gemeinsam `pakete/joel-dario/`) und ihren Namen in der `index.json` dieses Ordners ergänzen. Dann erscheint sie bei dieser Person unter „Pakete aus dem Repo“. Achtung: Ist das Repository öffentlich, sind diese Dateien öffentlich. Alles, was nicht jeder lesen soll (oder aus urheberrechtlich geschützten Schulbüchern, Skripten und Unterlagen der Hochschule stammt), besser nur per Datei importieren. Dann bleibt es lokal im Browser.

**Abgeschlossene Themen:** Damit „Pakete aus dem Repo“ übersichtlich bleibt, lassen sich alle Pakete eines Themas in einen Unterordner verschieben. Sie liegen dann in `pakete/<ordner>/abgeschlossen/<thema>/` und stehen in der `index.json` als `abgeschlossen/<thema>/<datei>.json`. In der App erscheinen sie unten in der aufklappbaren Gruppe „Abgeschlossen“, darin ein Eintrag je Thema (zum Beispiel „Englisch“ und „Musik“, die bei Joel schon dort liegen). Verschoben wird nur auf Anweisung, mit `python3 tools/thema_abschliessen.py <ordner> <thema> <dateiprefix>` (zum Beispiel `joel-dario geografie geografie-`), mit `--zurueck` wieder zurück. Schon in der App importierte Pakete bleiben dabei unverändert.

## Üben und Probearbeit

- **Üben:** Nach jeder Aufgabe gibt es sofort die Auswertung, die richtige Lösung und eine kurze Erklärung. Tipps sind möglich. „Weiß ich nicht“ zeigt die Lösung. Am Ende können die Fehler gezielt wiederholt werden.
- **Probearbeit:** Wie in der Schule. Man kann zwischen den Aufgaben springen, es gibt keine Tipps und keine Auswertung, bis man abgibt.
- Standardmäßig bietet jedes Paket beide Wege an. Mit `"probe": false` im Paket entfällt der Knopf „Probearbeit“ (gedacht für Teilpakete, wenn es für die ganze Arbeit eine gemeinsame Probearbeit gibt). Mit `"ueben": false` entfällt umgekehrt der Knopf „Üben“ (gedacht für das Probearbeit-Paket selbst, das nur zum Proben da ist). Beides zusammen ist nicht erlaubt. Das Probearbeit-Paket hat außerdem kein Lernblatt: `lernblatt` ist optional, ohne Lernblatt erscheint kein Knopf „Lernblatt“, und was dort zum Ablauf stünde (Zeit, Punkte, Hilfsmittel), steht in `beschreibung` und `hinweis`.
- **Termin und Reihenfolge:** Mit dem Paketfeld `"termin": "2026-11-16"` (Datum der Arbeit oder Klausur, Format JJJJ-MM-TT) erscheint oben auf der Startseite eine Karte „Fach: Arbeit am Montag, 16.11.“ mit den Tagen bis dahin („Heute“ und „Morgen“ am Tag davor), einem Fortschrittsbalken („3 von 11 Paketen durch“) und dem nächsten Paket mit Knöpfen zum Starten. Pakete mit gleichem Fach und gleichem Termin gehören zusammen; für Erwachsene heißt es „Klausur“, sonst „Arbeit“. Ein Paket zählt als „durch“, sobald es einmal ganz bearbeitet wurde (Fehler-Wiederholungen zählen nicht). Nach dem Termintag verschwindet die Karte. Mit `"reihenfolge": 1` (Zahl größer 0, 1 = zuerst) werden die Pakete auf der Startseite entsprechend sortiert und mit „Schritt n“ beschriftet; das nächste offene Paket trägt „Als Nächstes“. Empfohlen: erst die Übungspakete, dann die Probearbeit, zuletzt der Crashkurs. Beide Felder sind freiwillig, ohne sie bleibt alles wie bisher.
- **Timer für Probearbeit und Probeklausur:** Mit dem Paketfeld `"dauer": 45` (Minuten, 1 bis 600) läuft bei „Probearbeit“/„Probeklausur“ ein Countdown in der Kopfzeile („noch 40 Min.“, in den letzten 10 Minuten als Minuten:Sekunden). **Ist die Zeit um, wird die Arbeit automatisch abgegeben** und das Ergebnis erscheint; Aufgaben ohne Antwort zählen als nicht gelöst, schon eingetippte Antworten werden mit gewertet. Die Uhr zählt nur, solange die Aufgabenansicht offen ist, und bleibt nach dem Neuladen erhalten. Ohne `dauer` gilt der Standard der Person (`probeMinuten` in `PERSONEN`, bei Saskia 90 Minuten), sonst gibt es keinen Timer. Beim Üben und bei „Fehler wiederholen“ gibt es nie einen Timer.
- **Tastatur am Laptop:** Bei Auswahlaufgaben wählen die Tasten A bis D (oder 1 bis 4) die Antwort, bei mehreren richtigen Antworten schaltet dieselbe Taste um. Bei Richtig/Falsch gelten R und F (oder 1 und 2). Enter drückt den Hauptknopf (Prüfen, Weiter, Abgeben), in der Probearbeit geht Umschalt+Enter einen Schritt zurück. Beim Tippen in Textfeldern und bei geöffnetem Fenster passiert nichts, bei Aufgaben, die schon geprüft sind, ändern die Buchstaben nichts. Unter der Aufgabe steht ein Hinweis, auf Touch-Geräten ist er ausgeblendet.
- **Verwalten (für Eltern):** Auf der Startseite sind Import, „Pakete aus dem Repo“ und Löschen ausgeblendet; nur ein kleiner Knopf „Verwalten“ ist sichtbar. Er zeigt „Lernpaket importieren“, „Text einfügen“, „Pakete aus dem Repo“, **„Alle Pakete löschen“** (mit Rückfrage; Ergebnisse und Sicherung bleiben erhalten, eine laufende Sitzung wird beendet) und an jeder Karte „Löschen“. „Fertig“ blendet alles wieder aus. Ohne Pakete steht die Importleiste immer da. Der Zustand gilt nur für die Sitzung und wird beim Personenwechsel zurückgesetzt.
- **Lernstand auf der Startseite:** Oben stehen „Pakete geübt“ (z. B. 3/11, gezählt wird ein Paket mit mindestens einem vollständigen Durchgang), „zuletzt geübt“ (heute, gestern, vor n Tagen) und „Ø aktuell“ (Durchschnitt aus dem letzten Ergebnis jedes Pakets, ohne Probearbeit). Unter „Hallo“ steht, sobald mindestens zwei Pakete geübt wurden, das schwächste Thema als Knopf („Zum Wiederholen: … (60 %)“, startet das Üben), solange es unter 75 % liegt; sonst der Hinweis, dass alle bei 75 % oder mehr liegen. Probearbeiten und „Fehler wiederholen“-Durchgänge zählen dafür nicht; Ergebnisse gelöschter Pakete werden ignoriert.
- **Hinweise auf den Karten:** Das Paketfeld `hinweis` steht auf der Startseite eingeklappt in einer Zeile („⚠ Hinweis: Die Zeichnung von Schimp…“) und klappt per Tippen oder Enter auf. Aufgeklappte Hinweise bleiben beim Neuaufbau der Startseite offen, bis die Seite neu geladen wird. Im Lernblatt steht der Hinweis weiterhin vollständig.
- **Als App installieren (eigenes Fenster und Symbol):** Die Seite bringt `manifest.webmanifest` und Icons (`icons/`) mit. In Chrome oder Edge am Laptop: Menü (drei Punkte) → „Speichern und teilen“ → „Seite als App installieren“ (Edge: „Apps“ → „Diese Website als App installieren“); danach liegt ein Symbol auf dem Desktop oder in der Taskleiste. Auf dem Android-Tablet in Chrome: Menü → „App installieren“ bzw. „Zum Startbildschirm hinzufügen“. Die installierte App startet direkt bei der zuletzt benutzten Person (gemerkt als `lernhilfe.zuletzt`); „wechseln“ führt weiter zur Auswahl. Im normalen Browser-Tab bleibt es bei „Wer lernt heute?“. Daten und Ergebnisse sind dieselben wie im Browser (derselbe Speicher). Offline öffnen (Service Worker) gibt es bewusst noch nicht.
- **Belohnungen (Joel, Dario und Saskia):** Auf der Startseite steht eine Karte mit Stufe, Punkten und Fortschritt zur nächsten Stufe, dazu die Knöpfe „Mein Album“ und „Abzeichen“. Punkte: jede beantwortete Aufgabe 1 Punkt, halb richtig 2, ganz richtig 3 (freie Aufgaben höchstens 2, „Weiß ich nicht“ nichts). Jede Aufgabe zählt je Paket nur einmal, durch spätere Verbesserung kommen die fehlenden Punkte dazu – das ist die Obergrenze je Paket. Ein vollständiger Durchgang (mindestens 80 % beantwortet) bringt +20 Punkte, die Karte des Pakets gibt es ab 50 % (Bronze, +10), 75 % (Silber, insgesamt +20) und 90 % (Gold, insgesamt +30). Zehn Stufen von „Rucksack-Packer“ bis „Legende“ (alle Geschichte-Pakete zusammen bringen etwa 2000 Punkte). Abzeichen haben vier Stufen (Bronze, Silber, Gold, Diamant) und zählen über alle Pakete und Fächer: Aufgabenheld, Fehlerjäger, Mut zum Fehler, Dranbleiber, Paketprofi, Volltreffer, Alle Teile stark, Prüfungsprofi, Zeitmeister, Früh dran, Aufsteiger, Goldschmied, Sammler, Crashkurs-Champion. Neue Stufen, Karten und Abzeichen werden eingeblendet, begleitet von kurzem Konfetti (entfällt bei „Bewegung reduzieren“). Das Sammelalbum (Adresse `#/joel/album`) zeigt alle Karten, noch nicht erspielte grau. Der Spielstand liegt wie die Ergebnisse im Browser (`punkte`) und ist in der Sicherung enthalten. **Bei Saskia gilt dieselbe Punkte-Logik im Erwachsenen-Ton:** Stufen von „Erstsemester“ bis „Nobelpreisträgerin“, statt Sammelalbum eine „Kartei“ mit Karteikarten (Rang Bronze, Silber, Gold wie bei den Kindern), andere Abzeichen-Namen (z. B. Aufgabenprofi, Klausurprofi, Zeitmanagement, Bestnoten), „Probeklausur“ statt „Probearbeit“. Das Konfetti gibt es auch bei Saskia, dort als rosa Glitzer mit funkelnden Sternchen. Echte Belohnungen sind bewusst nicht Teil der App.
- **Gruppen auf der Startseite:** Mit dem Paketfeld `"gruppe": "Überschrift"` (kurzer Text, höchstens 80 Zeichen) erscheinen Pakete getrennt von den übrigen unter einer eigenen Überschrift mit Anzahl, unterhalb der Pakete ohne `gruppe`. Alle Pakete mit derselben Überschrift stehen zusammen, die Reihenfolge ist die des Imports. Ein Klick auf die Überschrift klappt die Gruppe zu oder auf (auch per Tastatur); der Browser merkt sich die Wahl je Person. Gedacht für Dauerhaftes, das zu keiner Arbeit gehört, z. B. Saskias R-Studio-Pakete zum Üben und Nachschlagen („R Studio: Üben und Nachschlagen“). Ohne das Feld bleibt alles wie bisher.
- **Fehlerliste je Paket:** Die Lernhilfe merkt sich, welche Aufgaben im letzten vollständigen Durchgang (Üben oder Probearbeit) nicht ganz richtig waren. Auf der Paketkarte erscheint „Fehler üben (n)“, auch nach dem Verlassen der Ergebnisseite und nach dem Neuladen. In einer Fehlerrunde fallen richtig beantwortete Aufgaben aus der Liste, ein neuer vollständiger Durchgang ersetzt sie. Freie Aufgaben (Selbstbewertung) gehören nicht dazu; der Lernstand bleibt unverändert, weil Fehlerrunden dort nicht zählen. Aufgaben werden über Position und eine Kurzkennung ihres Inhalts erkannt, ein aktualisiertes Paket bringt die Liste also nicht durcheinander (geänderte Aufgaben fallen heraus). Die Liste liegt im Speicher der Person (`fehler`) und ist Teil der Sicherung.
- **Nachlesen:** Unter jeder falsch beantworteten Aufgabe (beim Üben, bei „Fehler wiederholen“ und in der Auswertung der Probearbeit) steht ein aufklappbarer Kasten „Nachlesen“ mit dem passenden Abschnitt des Lernblatts, bei Saskia dazu „Mehr dazu: Lehrbrief …“. So braucht auch die Probearbeit, die kein Lernblatt hat, keinen eigenen Text: Ihre Aufgaben verweisen auf die Lernblätter der Übungspakete. Die Felder dafür stehen unter „Format eines Lernpakets“.
- Freie Antworten (Sätze, Erklärungen) bewertet das Kind selbst anhand der Musterlösung und einer Checkliste (Passt / Teilweise / Noch nicht).
- Eine laufende Sitzung bleibt beim Neuladen oder Schließen des Browsers erhalten („Fortsetzen“ auf der Startseite).
- Auf der Startseite steht je Paket der Verlauf der letzten Ergebnisse in Prozent.
- Groß- und Kleinschreibung zählt beim Prüfen nicht (für strenge Aufgaben `"gross": true` setzen), ebenso nicht der Punkt oder das Fragezeichen am Ende. ß und ss gelten als gleich.
- **Eltern (nur Joel und Dario, nicht Saskia):** Zwei Wege, wie die Eltern sehen, wie die Kinder üben, ohne Server und ohne Konto.
  - **Text zum Teilen:** Auf der Ergebnisseite „An die Eltern schicken“ und unten auf der Startseite „Stand als Text schicken“. Es öffnet sich eine Vorschau (Paket, Ergebnis in Prozent, Teile mit dem schwächsten, Anzahl Fehler, Termin, Stufe) mit „Senden …“ (Teilen-Menü des Geräts, z. B. WhatsApp) oder „Text kopieren“.
  - **Eltern-Ansicht (live):** Auf dem Gerät der Eltern: Startseite „Wer lernt heute?“ → unten „Eltern-Ansicht“ → „Eltern-Ansicht einrichten“ erzeugt einen Familiencode (12 Zeichen, Adresse `#/eltern`). Auf dem Gerät der Kinder: Startseite unten „Mit Eltern-Ansicht verbinden“, Code eintragen. Danach schickt das Kind nach jedem Durchgang automatisch seinen Stand (Name, Punkte, Stufe, Lernstand je Paket, letzte Ergebnisse, schwächster Teil; keine einzelnen Antworten), solange die Eltern-Ansicht offen ist; sonst wird er nachgeholt, sobald sie offen ist und das Kind die Lernhilfe geöffnet hat („Jetzt senden“ geht jederzeit). Die Eltern-Ansicht merkt sich den letzten Stand je Kind. Die Verbindung läuft direkt von Gerät zu Gerät (WebRTC über PeerJS, wie in der Quiz-App, die Bibliothek wird nur bei Bedarf von unpkg geladen); der öffentliche Vermittlungsserver sieht nur, dass sich zwei Geräte verbinden. Alles Empfangene wird geprüft, gekürzt und als Text angezeigt. Ein neuer Code kann jederzeit erzeugt werden, dann müssen die Kinder ihn neu eintragen. Auf Kinder-Geräten steht der Code unter `lernhilfe.elterncode`, auf dem Eltern-Gerät der Stand unter `lernhilfe.eltern.v1`.
- **Freunde-Album (nur Joel und Dario):** Die beiden können sich ihr Sammelalbum live gegenseitig ansehen: auf der Startseite unten „Album von … ansehen“ (oder auf der eigenen Album-Seite). Voraussetzung ist derselbe **Freunde-Code** bei beiden: Die Eltern erzeugen ihn in der Eltern-Ansicht („Freunde-Code für das Album“), geben ihn an die Eltern des anderen Kindes weiter, und die Kinder tragen ihn auf der Startseite unter „Freunde-Code“ ein. So können beide Familien je einen eigenen Familiencode für die Eltern-Ansicht haben und sehen trotzdem nur das eigene Kind. Ohne eigenen Freunde-Code gilt der Familiencode. Ohne Code gibt es nichts zu sehen, die Eltern behalten also die Kontrolle. Der andere muss die Lernhilfe geöffnet haben; Joel ist erreichbar, solange er in seiner Person ist, und Dario entsprechend. Zu sehen sind nur Stufe, Karten mit Rang und Abzeichen, keine Prozente, keine Punkte, keine Ergebnisse. Jeder kann sein Album mit „verbergen“ (Startseite unten) ausblenden. Technik wie bei der Eltern-Ansicht (PeerJS, direkt von Gerät zu Gerät, Kennung `lh-freund-<Code>-<Person>`); alles Empfangene wird geprüft, gekürzt und nur als Text angezeigt. Saskia hat das nicht.

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
  "karte": { "titel": "Lucy", "motiv": "🦴", "text": "Kurzer Text für die Sammelkarte" },
  "lernblatt": [
    { "titel": "Brüche kürzen", "text": "- Zähler und Nenner durch dieselbe Zahl teilen", "merke": "Optional", "bild": "Optional: SVG-Code oder Bilddatei" }
  ],
  "aufgaben": [ ... ]
}
```

Pflicht sind `typ`, `id` (Buchstaben, Zahlen, `-`, `_`), `titel` und `aufgaben`. `person` ist optional (`joel`, `dario`, `saskia` oder eine Liste wie `["joel", "dario"]`): Es sagt, für wen das Paket gedacht ist, und löst beim Import in einen fremden Bereich eine Rückfrage aus. `klasse` ist frei: Eine Zahl wird als „Klasse 6“ angezeigt, anderer Text (z. B. „2. Semester“) unverändert. In Texten gelten `**fett**`, Zeilenumbruch `\n` und Listen mit `- `. Für Programmcode gibt es zwei Schreibweisen: Eine Zeichenfolge zwischen einzelnen Backticks wird als **Code im Satz** gesetzt (überall erlaubt, auch in Antworten, `info` und `tipp`; `*` und `_` bleiben darin unverändert). Ein **Codeblock** beginnt und endet mit einer Zeile aus drei Backticks, hinter den ersten drei steht die Art: `r` (R-Code, mit Knopf „Kopieren“), `out` („Ausgabe in der Konsole“, ohne Knopf) oder `text`. Codeblöcke gelten nur in den Textfeldern mit Absätzen (`frage`, `text`, Lernblatt-`text`, `muster`, Lesetext), nicht in `info`, `tipp`, `merke` und Antworten. Innerhalb eines Codeblocks darf kein weiterer Block stehen, und ein einzelnes Backtick im Code im Satz lässt sich nicht schreiben. `karte` (freiwillig) ist die Sammelkarte des Pakets im Album (bei Saskia: Karteikarte in der Kartei): `titel` (höchstens 40 Zeichen), `motiv` (ein Emoji) und `text` (höchstens 200 Zeichen). Fehlt sie, nimmt die App den Paketnamen und das Symbol des Fachs; neue Pakete sollten immer eine eigene `karte` mitbringen.

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
| `lesen` | Nachlesen bei falscher Antwort: Titel eines Lernblatt-Abschnitts im selben Paket oder `{"paket": "<id>", "titel": "<Abschnitt>"}` für ein anderes Paket, mehrere als Liste. Überschreibt `nachlesen` des Pakets |
| `punkte` | Punkte der Aufgabe (Standard 1, bei `frei` 2) |

### Nachlesen (Verweise auf das Lernblatt)

Ein Paket kann seinen Aufgaben Lernblatt-Abschnitte zuordnen, damit die App bei einer falschen Antwort den passenden Abschnitt zeigt:

- `nachlesen` (Paketfeld): ordnet jedem `abschnitt` der Aufgaben einen oder mehrere Lernblatt-Abschnitte zu, z. B. `"nachlesen": { "A – Meere und Länder": "Länder und Bundesländer an den Meeren" }`. Der Titel muss genau so im `lernblatt` des Pakets stehen (die App meldet es sonst beim Import).
- `lesen` (Aufgabenfeld): genauerer Verweis für eine einzelne Aufgabe, auch auf ein anderes Paket (`{"paket": "geografie-2b-…", "titel": "Gezeitenkurve lesen"}`). So verweist ein Paket ohne Lernblatt (Probearbeit, Probeklausur) auf die Lernblätter der Übungspakete. Ist das andere Paket nicht auf dem Gerät, bleibt der Kasten weg.
- `quelle` (Paketfeld): Text, der im Kasten als „Mehr dazu: …“ erscheint, z. B. `"Lehrbrief Testverfahren I, Kapitel 3"`. Gilt für Verweise auf das Lernblatt dieses Pakets.

Die Verweise der Geografie-Pakete setzt `tools/geo_lesen.py` beim Bauen und prüft, dass jedes Ziel existiert und jede Aufgabe einen Verweis hat.

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
