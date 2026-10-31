#!/usr/bin/env python3
"""Erzeugt die Beispiel-Lernpakete im Ordner pakete/ (gültiges JSON, ohne Tippfehler-Risiko).
Aufruf: python3 tools/build_beispielpakete.py
"""
import json, os

OUT = os.path.join(os.path.dirname(__file__), '..', 'pakete')
os.makedirs(OUT, exist_ok=True)

def write(name, obj):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
        f.write('\n')

# ------------------------------------------------------------------ Englisch
english = {
 "typ": "lernpaket", "version": 1,
 "id": "englisch-g-access-2-unit-1",
 "titel": "English G Access 2 – Unit 1: In the holidays",
 "fach": "Englisch", "klasse": "6",
 "beschreibung": "Simple past (was/were, regelmäßige und unregelmäßige Verben, Verneinung, Fragen mit did), Hörverstehen, Telefonieren, Schreiben.",
 "hinweis": "Beispielpaket zum Ausprobieren. Aufgaben und Lernblatt sind frei formuliert und nicht aus dem Schulbuch abgeschrieben.",
 "lernblatt": [
  {"titel": "was / were", "text":
   "- I / he / she / it → **was**\n- you / we / they → **were**\n- Verneinung: **wasn't**, **weren't**\n- Frage: **Was** he at home? / **Were** you at school?\n- Kurzantwort: Yes, I **was**. / No, they **weren't**.",
   "merke": "Auch bei „Sam and his family“ heißt es **were**, denn das ist „they“."},
  {"titel": "Regelmäßige und unregelmäßige Verben", "text":
   "- Regelmäßig: Grundform + **-ed**: visit → visit**ed**, play → play**ed**\n- Besonderheiten: stop → stop**ped**, study → stud**ied**\n- Unregelmäßig: die Form muss man lernen: go → **went**, see → **saw**, have → **had**, eat → **ate**, swim → **swam**, buy → **bought**, take → **took**, make → **made**",
   "merke": "Unregelmäßige Verben bekommen kein -ed."},
  {"titel": "Verneinung und Fragen mit did", "text":
   "- Verneinung: **didn't** + Grundform: I didn't **go**. (nicht: I didn't went)\n- Frage: **Did** + Person + Grundform: **Did** you **go** to the beach?\n- Kurzantwort: Yes, I **did**. / No, I **didn't**.\n- Mit Fragewort: **Where did** you **go**?",
   "merke": "Nach did / didn't steht immer die **Grundform**. Die Vergangenheit steckt schon in did."},
  {"titel": "Fragen nach dem Subjekt und nach dem Objekt", "text":
   "Fragst du nach dem **Subjekt** (wer hat es getan?), brauchst du **kein did**:\n\n- Sam met Lucy. → **Who met** Lucy?\n\nFragst du nach dem **Objekt** (wen oder was?), brauchst du **did**:\n\n- Sam met Lucy. → **Who did** Sam **meet**?"},
  {"titel": "Telefonieren", "text":
   "- Hello, this is Tom.\n- Can I speak to Sam, please?\n- Hold on, please. / Just a moment.\n- I'm sorry, he isn't here. Can I take a message?\n- Can he call me back?\n- Thank you. Goodbye!"}
 ],
 "aufgaben": [
  {"typ": "luecke", "abschnitt": "Block A – was / were",
   "frage": "Setze **was** oder **were** ein.",
   "text": "Last summer Sam and his family {{were}} in Cornwall. The weather {{was}} sunny, but the sea {{was}} cold. Sam's parents {{were}} happy. His sister {{was}} not at the beach – she {{was}} in a café. \"Where {{were}} you?\" Sam asked her.",
   "auswahl": ["was", "were"],
   "tipp": "I, he, she, it → was. You, we, they → were. „Sam and his family“ ist „they“.",
   "info": "Bei mehreren Personen (Sam and his family, Sam's parents) steht **were**."},
  {"typ": "luecke", "abschnitt": "Block A – was / were",
   "frage": "Mach die Sätze verneint. Schreibe die Kurzform (wasn't / weren't).",
   "text": "1. It was cold. → It {{wasn't|was not}} cold.\n2. They were hungry. → They {{weren't|were not}} hungry.\n3. I was late. → I {{wasn't|was not}} late.\n4. We were in London. → We {{weren't|were not}} in London."},
  {"typ": "luecke", "abschnitt": "Block A – was / were",
   "frage": "Ergänze die Fragen und Kurzantworten.",
   "text": "{{Was}} it a good holiday? – Yes, it {{was}}.\n{{Were}} you at the beach? – No, we {{weren't|were not}}.\n{{Were}} Sam and Lucy in the café? – Yes, they {{were}}."},
  {"typ": "mc", "abschnitt": "Block B – Verben und did",
   "frage": "Welcher Satz ist richtig?",
   "antworten": ["Did you went to the museum?", "Did you go to the museum?", "Do you went to the museum?", "Did you gone to the museum?"],
   "richtig": 1,
   "tipp": "Nach did steht die Grundform des Verbs.",
   "info": "Did + Grundform: **Did you go** …? Die Vergangenheit steckt schon in did."},
  {"typ": "tf", "abschnitt": "Block B – Verben und did",
   "frage": "Der Satz „Sam didn't saw the castle.“ ist richtig.",
   "richtig": False,
   "info": "Richtig ist: Sam didn't **see** the castle. Nach didn't kommt die Grundform."},
  {"typ": "zuordnen", "abschnitt": "Block B – Verben und did",
   "frage": "Ordne jedem Verb die Form der Vergangenheit (simple past) zu.",
   "paare": [["go", "went"], ["see", "saw"], ["have", "had"], ["eat", "ate"], ["swim", "swam"], ["buy", "bought"], ["take", "took"], ["make", "made"]]},
  {"typ": "luecke", "abschnitt": "Block B – Verben und did",
   "frage": "Schreibe die Verben in der Vergangenheit (simple past).",
   "text": "Yesterday we {{visited}} (visit) a museum. I {{played}} (play) football on the beach. My brother {{went}} (go) swimming. We {{had}} (have) ice cream. Dad {{took}} (take) lots of photos. Mum {{bought}} (buy) a postcard. Then we {{stopped}} (stop) at a café.",
   "tipp": "Regelmäßige Verben bekommen -ed (bei stop wird das p verdoppelt). Die anderen sind unregelmäßig."},
  {"typ": "luecke", "abschnitt": "Block B – Verben und did",
   "frage": "Mach die Sätze verneint mit didn't + Grundform.",
   "text": "Sam saw a shark. → Sam {{didn't|did not}} {{see}} a shark.\nWe went to the museum. → We {{didn't|did not}} {{go}} to the museum.\nI ate fish. → I {{didn't|did not}} {{eat}} fish."},
  {"typ": "luecke", "abschnitt": "Block B – Verben und did",
   "frage": "Ergänze die Fragen und Antworten.",
   "text": "{{Did}} you {{go}} to the beach? – Yes, I {{did}}.\n{{Did}} Sam {{visit}} the castle? – No, he {{didn't|did not}}.\nWhere {{did}} they {{stay}}? – In a small hotel.",
   "tipp": "Frage: Did + Person + Grundform. Kurzantwort: Yes, I did. / No, he didn't."},
  {"typ": "reihenfolge", "abschnitt": "Block B – Verben und did",
   "frage": "Bring die Wörter in die richtige Reihenfolge, sodass eine Frage entsteht.",
   "schritte": ["Where", "did", "you", "go", "last summer?"]},
  {"typ": "kurz", "abschnitt": "Block B – Verben und did",
   "frage": "Korrigiere den Fehler. Schreibe den ganzen Satz richtig auf:\n\n**Did you went to the beach?**",
   "richtig": ["Did you go to the beach"],
   "info": "Nach did steht die Grundform: Did you **go** to the beach?"},
  {"typ": "kurz", "abschnitt": "Block B – Verben und did",
   "frage": "Korrigiere den Fehler. Schreibe den ganzen Satz richtig auf:\n\n**Sam and his family was in Italy.**",
   "richtig": ["Sam and his family were in Italy"],
   "info": "„Sam and his family“ ist „they“, also **were**."},
  {"typ": "zuordnen", "abschnitt": "Block C – Subjekt- und Objektfragen",
   "frage": "Sam met Lucy at the beach. Welche Frage passt zu welcher Antwort?",
   "paare": [["Die Antwort soll **Sam** sein (Subjekt).", "Who met Lucy at the beach?"], ["Die Antwort soll **Lucy** sein (Objekt).", "Who did Sam meet at the beach?"]],
   "extra": ["Who did meet Lucy at the beach?", "Who Sam met at the beach?"],
   "info": "Subjektfrage: kein did. Objektfrage: did + Grundform."},
  {"typ": "luecke", "abschnitt": "Block D – Hören",
   "frage": "Drücke auf „Anhören“ (so oft du willst) und ergänze die Stichpunkte.",
   "vorlesen": {"sprache": "en-GB", "text": "Last summer I was in Wales with my family. On Monday the weather was rainy, so we visited a castle. On Tuesday it was sunny. We went to the beach and I swam in the sea. I didn't see any sharks, but I saw a lot of crabs. On Wednesday my brother was ill, so we stayed at the campsite."},
   "text": "Monday: The weather was {{rainy}}. The family visited a {{castle}}.\nTuesday: It was {{sunny}}. The narrator went to the {{beach}} and {{swam}} in the sea.\nWednesday: The narrator's {{brother}} was {{ill|sick}}."},
  {"typ": "reihenfolge", "abschnitt": "Block E – Telefonieren",
   "frage": "Bring das Telefongespräch in die richtige Reihenfolge.",
   "schritte": ["Hello, this is the Miller family.", "Hello, this is Tom. Can I speak to Sam, please?", "I'm sorry, he isn't here. Can I take a message?", "Yes, please. Can he call me back?", "Of course. Goodbye!"]},
  {"typ": "frei", "abschnitt": "Block F – Schreiben", "punkte": 4,
   "frage": "Schreibe 5 Sätze über deine letzten Ferien (oder erfinde sie). Benutze was/were, ein regelmäßiges und ein unregelmäßiges Verb, einen verneinten Satz und eine Frage mit did.",
   "muster": "Last summer we were in Italy. The weather was hot and sunny. We visited a big castle and I swam in the sea every day. I didn't like the food in the hotel. Did you go on holiday, too?",
   "kriterien": ["was oder were richtig benutzt", "mindestens ein regelmäßiges Verb mit -ed", "mindestens ein unregelmäßiges Verb (went, saw, had …)", "ein verneinter Satz mit didn't + Grundform", "eine Frage mit Did + Grundform"]}
 ]
}
write('englisch-unit1-simple-past.json', english)

# ------------------------------------------------------------------ Geografie
dike_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 330" width="560" height="330" font-family="Arial,Helvetica,sans-serif">
<rect width="560" height="330" fill="#ffffff"/>
<rect x="0" y="235" width="300" height="60" fill="#bfe0f3"/>
<path d="M0 235 q15 -9 30 0 t30 0 t30 0 t30 0 t30 0 t30 0 t30 0 t30 0" fill="none" stroke="#5aa6d1" stroke-width="2.5"/>
<rect x="0" y="290" width="560" height="40" fill="#c9ad7a"/>
<polygon points="150,290 320,150 360,150 470,290" fill="#9a6b43"/>
<polygon points="192,290 324,186 356,186 438,290" fill="#f0d9a0"/>
<polyline points="150,290 320,150 360,150 470,290" fill="none" stroke="#3f9b4f" stroke-width="9" stroke-linejoin="round"/>
<text x="22" y="212" font-size="15" fill="#2d6f96">Meer</text>
<text x="500" y="276" font-size="15" fill="#6b5535">Land</text>
<g stroke="#333" stroke-width="1.4" fill="none">
<line x1="150" y1="133" x2="236" y2="218"/>
<line x1="480" y1="143" x2="416" y2="222"/>
<line x1="340" y1="83" x2="340" y2="146"/>
<line x1="255" y1="123" x2="302" y2="192"/>
<line x1="340" y1="296" x2="340" y2="246"/>
<line x1="96" y1="212" x2="150" y2="288"/>
</g>
<g fill="#e2701a">
<circle cx="150" cy="120" r="13"/><circle cx="480" cy="130" r="13"/><circle cx="340" cy="70" r="13"/>
<circle cx="255" cy="110" r="13"/><circle cx="340" cy="309" r="13"/><circle cx="96" cy="199" r="13"/>
</g>
<g fill="#fff" font-size="15" font-weight="bold" text-anchor="middle">
<text x="150" y="125.5">1</text><text x="480" y="135.5">2</text><text x="340" y="75.5">3</text>
<text x="255" y="115.5">4</text><text x="340" y="314.5">5</text><text x="96" y="204.5">6</text>
</g>
</svg>'''

geo = {
 "typ": "lernpaket", "version": 1,
 "id": "geografie-nordsee-wattenmeer",
 "titel": "Geografie: Nordsee, Wattenmeer und Küstenschutz",
 "fach": "Geografie", "klasse": "6",
 "beschreibung": "Gezeiten, Nordsee und Ostsee im Vergleich, Wattenmeer und Nationalpark, Deich, Düne und Siel.",
 "hinweis": "Entwurf zum Ausprobieren. Vor der Nutzung mit den Unterlagen aus der Schule abgleichen, besonders die Schutzzonen, die Jahreszahlen und die Zonen des Wattenmeeres.",
 "lernblatt": [
  {"titel": "Gezeiten", "text":
   "- **Ebbe**: Das Wasser läuft ab, der Wasserstand sinkt.\n- **Flut**: Das Wasser kommt zurück, der Wasserstand steigt.\n- **Hochwasser** und **Niedrigwasser** sind der höchste und der tiefste Wasserstand.\n- Der **Tidenhub** ist der Höhenunterschied zwischen Hochwasser und Niedrigwasser.\n- Ebbe und Flut wechseln etwa alle 6 Stunden. Zwischen zwei Hochwassern liegen ungefähr 12 Stunden und 25 Minuten.",
   "merke": "Gezeiten entstehen durch die Anziehungskraft des Mondes und die Fliehkraft im System Erde–Mond."},
  {"titel": "Nordsee und Ostsee im Vergleich", "text":
   "- Die Nordsee ist weit zum Atlantik geöffnet: Es gibt deutliche Gezeiten.\n- Die Ostsee ist nur durch schmale Meerengen zwischen den dänischen Inseln mit der Nordsee verbunden. Es kann kaum Wasser ein- und ausströmen, deshalb sind die Gezeiten sehr schwach (nur wenige Zentimeter).\n- Tidenhub im Vergleich: Bristol ca. 12 m, Bremerhaven ca. 4 m, Hallig Langeneß ca. 3 m."},
  {"titel": "Das Wattenmeer", "text":
   "- Das Watt liegt bei Flut unter Wasser und fällt bei Ebbe trocken.\n- Es ist Lebensraum für besondere Tiere und Pflanzen und ein wichtiger Rastplatz für Zugvögel.\n- Das Wattenmeer ist Nationalpark (laut Buch seit 1986) und seit 2009 UNESCO-Weltnaturerbe.\n- Schutzzonen: **Ruhezone**, **Zwischenzone**, **Erholungszone**."},
  {"titel": "Küstenschutz", "text":
   "- **Deiche** schützen das Land vor Sturmfluten.\n- Aufbau: ein **Sandkern**, darüber eine Schicht aus **Klei** (fester, lehmiger Boden), oben eine **Grasdecke**.\n- Die **Seeseite** ist flach, die Wellen verlieren Kraft. Die **Landseite** ist steiler. Unten liegt der **Deichfuß**.\n- **Dünen** sind natürliche Sandwälle. Strandhafer hält den Sand mit seinen Wurzeln fest.\n- Ein **Siel** (Schleuse im Deich) lässt Wasser vom Land ins Meer abfließen und wird bei Flut geschlossen."}
 ],
 "aufgaben": [
  {"typ": "mc", "abschnitt": "Gezeiten",
   "frage": "Was ist der Tidenhub?",
   "antworten": ["Der Höhenunterschied zwischen Hochwasser und Niedrigwasser", "Die Zeit zwischen zwei Hochwassern", "Die Geschwindigkeit der Wellen", "Die Menge Wasser im Watt"],
   "richtig": 0},
  {"typ": "luecke", "abschnitt": "Gezeiten",
   "frage": "Ergänze die Begriffe.",
   "text": "Bei {{Ebbe}} läuft das Wasser ab und der Wasserstand sinkt. Bei {{Flut}} kommt das Wasser zurück. Den höchsten Wasserstand nennt man {{Hochwasser}}, den tiefsten {{Niedrigwasser}}.",
   "wortbank": ["Niedrigwasser", "Flut", "Ebbe", "Hochwasser"]},
  {"typ": "mc", "abschnitt": "Gezeiten",
   "frage": "Wodurch entstehen die Gezeiten?",
   "antworten": ["Anziehungskraft des Mondes", "Fliehkraft im System Erde–Mond", "Starker Wind über dem Meer", "Schmelzwasser aus den Alpen"],
   "richtig": [0, 1],
   "info": "Die Anziehungskraft des Mondes und die Fliehkraft im System Erde–Mond zusammen erzeugen die Gezeiten."},
  {"typ": "reihenfolge", "abschnitt": "Gezeiten",
   "frage": "Bringe den Ablauf der Gezeiten in die richtige Reihenfolge (Start: Hochwasser).",
   "schritte": ["Hochwasser: Das Wasser steht am höchsten", "Ebbe: Das Wasser läuft ab", "Niedrigwasser: Das Wasser steht am tiefsten", "Flut: Das Wasser kommt zurück"]},
  {"typ": "zuordnen", "abschnitt": "Nordsee und Ostsee",
   "frage": "Ordne dem Ort den passenden Tidenhub zu.",
   "paare": [["Bristol (Großbritannien)", "ca. 12 m"], ["Bremerhaven", "ca. 4 m"], ["Hallig Langeneß", "ca. 3 m"], ["Ostsee", "nur wenige Zentimeter"]]},
  {"typ": "frei", "abschnitt": "Nordsee und Ostsee", "punkte": 2,
   "frage": "Erkläre, warum es in der Ostsee kaum Gezeiten gibt.",
   "muster": "Die Ostsee ist nur durch schmale Meerengen zwischen den dänischen Inseln mit der Nordsee verbunden. Deshalb kann kaum Wasser ein- und ausströmen, und die Gezeiten sind nur sehr schwach.",
   "kriterien": ["Die Ostsee ist nur durch schmale Meerengen (dänische Inseln) mit der Nordsee verbunden", "Es kann kaum Wasser ein- und ausströmen"]},
  {"typ": "tf", "abschnitt": "Wattenmeer",
   "frage": "Das Watt liegt bei Flut unter Wasser und fällt bei Ebbe trocken.",
   "richtig": True},
  {"typ": "mc", "abschnitt": "Wattenmeer",
   "frage": "Seit welchem Jahr ist das Wattenmeer UNESCO-Weltnaturerbe?",
   "antworten": ["1986", "1999", "2009", "2015"],
   "richtig": 2,
   "info": "Laut Buch wurde das Gebiet 1986 Nationalpark. 2009 kam der UNESCO-Titel dazu."},
  {"typ": "zuordnen", "abschnitt": "Wattenmeer",
   "frage": "Ordne den Schutzzonen im Nationalpark ihre Bedeutung zu.",
   "paare": [["Ruhezone", "Die Natur hat Vorrang, Betreten meist verboten"], ["Zwischenzone", "Betreten nur auf ausgewiesenen Wegen oder zu bestimmten Zeiten"], ["Erholungszone", "Erholung und Baden sind erlaubt"]]},
  {"typ": "luecke", "abschnitt": "Küstenschutz",
   "frage": "Beschrifte den Deich. Welcher Begriff gehört zu welcher Nummer?",
   "bild": dike_svg, "bildAlt": "Querschnitt durch einen Deich mit den Nummern 1 bis 6",
   "text": "(1) {{Seeseite}}\n(2) {{Landseite}}\n(3) {{Grasdecke}}\n(4) {{Klei}}\n(5) {{Sandkern}}\n(6) {{Deichfuß|Deichfuss}}",
   "wortbank": ["Sandkern", "Seeseite", "Deichfuß", "Klei", "Landseite", "Grasdecke"],
   "tipp": "Das Meer liegt links. Außen liegt die Grasdecke, darunter Klei, innen der Sandkern."},
  {"typ": "mc", "abschnitt": "Küstenschutz",
   "frage": "Wozu dient ein Siel im Deich?",
   "antworten": ["Es lässt Wasser vom Land ins Meer abfließen und wird bei Flut geschlossen", "Es ist ein Hafen für Fischerboote", "Es hält Touristen vom Strand fern", "Es erzeugt Strom aus den Gezeiten"],
   "richtig": 0},
  {"typ": "mc", "abschnitt": "Küstenschutz",
   "frage": "Warum pflanzt man auf Dünen Strandhafer?",
   "antworten": ["Seine Wurzeln halten den Sand fest", "Er dient als Futter für Schafe", "Er macht das Meerwasser salziger", "Er zeigt an, wann Hochwasser kommt"],
   "richtig": 0},
  {"typ": "frei", "abschnitt": "Küstenschutz", "punkte": 3,
   "frage": "Erkläre, wie ein Deich das Land vor Sturmfluten schützt. Beschreibe dabei seinen Aufbau.",
   "muster": "Ein Deich ist ein Wall an der Küste. Er hat einen Sandkern, darüber eine feste Schicht aus Klei und oben eine Grasdecke. Die Seeseite ist flach, so verlieren die Wellen Kraft. Die Landseite ist steiler. Bei einer Sturmflut hält der Deich das Wasser zurück, damit das Land dahinter nicht überflutet wird.",
   "kriterien": ["Der Deich hält das Wasser bei Sturmflut zurück", "Aufbau: Sandkern, Klei, Grasdecke", "Seeseite flach, Landseite steiler"]}
 ]
}
write('geografie-nordsee-wattenmeer.json', geo)

with open(os.path.join(OUT, 'index.json'), 'w', encoding='utf-8') as f:
    json.dump(['englisch-unit1-simple-past.json', 'geografie-nordsee-wattenmeer.json'], f, ensure_ascii=False, indent=1)
    f.write('\n')
print('geschrieben:', sorted(os.listdir(OUT)))
