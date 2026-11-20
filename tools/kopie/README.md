# Lernhilfe

Aufgaben für Klassenarbeiten am Bildschirm statt auf Papier. Läuft als Web-App im Browser, ohne Server und ohne Anmeldung. Beim Öffnen fragt die App zuerst, **wer lernt** (@@KIND1_NAME@@ oder @@KIND2_NAME@@). Jedes Kind hat seine eigenen Lernpakete und Ergebnisse.

## Dateien

- `index.html` – die komplette App
- `anleitung.html` – Anleitung für Eltern, mit Vorlage für Claude
- `vorlage.txt` – dieselbe Vorlage als Textdatei
- `beispielpaket.json` – Beispielpaket zum Ausprobieren
- `manifest.webmanifest`, `icons/` – damit sich die App auf den Startbildschirm legen lässt

Diese Dateien werden aus der Ursprungs-App erzeugt. Änderungen nicht von Hand machen, sondern neu erzeugen lassen.

## Veröffentlichen

Settings → Pages → „Deploy from a branch“ → Branch `main`, Ordner `/ (root)`. Nach ein bis zwei Minuten ist die App unter `https://<konto>.github.io/<repository>/` erreichbar. Direkt zu einem Kind: `…/#/@@KIND1_ID@@` oder `…/#/@@KIND2_ID@@`.

## Lernpakete

Lernpakete (JSON) erstellt man mit Claude nach der Vorlage in `anleitung.html` und importiert sie in der App: Kind wählen, „Lernpaket importieren“. Pakete und Ergebnisse liegen nur im Browser des jeweiligen Geräts.
