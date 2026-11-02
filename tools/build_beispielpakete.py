#!/usr/bin/env python3
"""Erzeugt das Beispielpaket Englisch in pakete/joel/ (gültiges JSON, ohne Tippfehler-Risiko). Geografie siehe build_geografie.py.
Aufruf: python3 tools/build_beispielpakete.py
"""
import json, os

OUT = os.path.join(os.path.dirname(__file__), '..', 'pakete', 'joel')
os.makedirs(OUT, exist_ok=True)

def write(name, obj, out=None):
    with open(os.path.join(out or OUT, name), 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
        f.write('\n')

# ------------------------------------------------------------------ Englisch
english = {
 "typ": "lernpaket", "version": 1, "person": "joel",
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

# Listen der Pakete im Repo: vorhandene Einträge behalten (z. B. die Musikpakete) und ergänzen
def update_index(folder, names):
    ix_path = os.path.join(folder, 'index.json')
    try:
        ix = json.load(open(ix_path, encoding='utf-8'))
    except Exception:
        ix = []
    for name in reversed(names):
        if name not in ix:
            ix.insert(0, name)
    with open(ix_path, 'w', encoding='utf-8') as f:
        json.dump(ix, f, ensure_ascii=False, indent=1)
        f.write('\n')

update_index(OUT, ['englisch-unit1-simple-past.json'])
print('geschrieben:', sorted(os.listdir(OUT)))
