"""Geografie Klasse 6: Crashkurs (Das Wichtigste kurz gefasst) für Joel und Dario.

Der letzte Blick am Tag vor der Arbeit: kurzes Lernblatt (kein neuer Stoff, nur Auswahl aus den Lernblättern der
Übungspakete), Checkliste, Tipps und ein Blitz-Check mit neuen Kurzaufgaben.
Anweisung: siehe crashkurs-baustein.md im Projekt. Alle Fakten werden gegen die Lernblätter der anderen Pakete geprüft.
"""
import re

from geo_lib import *
from geo_lib import _gaps

S = "Blitz-Check"
ID = "geografie-crashkurs"

ALT_KURVE = "Gezeitenkurve eines Tages: Hochwasser um 5 Uhr bei 3,5 m, Niedrigwasser gegen 11 Uhr bei 1 m, Hochwasser gegen 17:30 Uhr."
ALT_WATT = "Querschnitt von der See zum Land mit den vier Zonen Meer, Watt, Salzwiese und Deich und den Marken für mittleres Niedrigwasser und mittleres Hochwasser"
ALT_DEICH = "Querschnitt durch einen Deich mit allen beschrifteten Teilen: Seeseite, Landseite, Deichkrone, Grasdecke, Klei, Sandkern, Deichfuß, Sturmflutwasserstand und Hochwasser"


def lernblatt():
    return [
        lb("So nutzt du den Crashkurs",
           "Das ist dein **letzter Blick** am Tag vor der Arbeit: einmal in Ruhe lesen (etwa 10 Minuten), danach den **Blitz-Check** machen (etwa 5 Minuten). "
           "Hier steht nichts Neues. Wenn du bei etwas unsicher bist, geh in das passende Übungspaket zurück."),
        lb("Nord- und Ostsee: Bundesländer, Städte, Flüsse",
           "- **Nordsee**: Schleswig-Holstein und Niedersachsen, dazu die Stadtstaaten Hamburg (an der Elbe) und Bremen (an der Weser).\n"
           "- **Ostsee**: Schleswig-Holstein und Mecklenburg-Vorpommern.\n"
           "- Städte an der **Nordsee**: Cuxhaven, Bremerhaven, Wilhelmshaven, Emden, Husum. An der **Ostsee**: Flensburg, Kiel, Lübeck, Wismar, Rostock, Stralsund, Greifswald.\n"
           "- Flüsse zur Nordsee: Ems, Weser, Elbe, Eider. Zur Ostsee: Trave, Warnow, Peene, Oder.\n"
           "- Der **Nord-Ostsee-Kanal** verbindet beide Meere (Brunsbüttel bis Kiel).\n\n"
           "Typischer Fehler: Hamburg und Bremen liegen nicht direkt am Meer, sondern an Elbe und Weser.",
           merke="Schleswig-Holstein ist das einzige Bundesland an beiden Meeren."),
        lb("Inseln",
           "- **Nordfriesische Inseln**: Sylt, Föhr, Amrum, Pellworm.\n"
           "- **Ostfriesische Inseln** (von West nach Ost): Borkum, Juist, Norderney, Baltrum, Langeoog, Spiekeroog, Wangerooge.\n"
           "- **Helgoland** gehört zu keiner der beiden Gruppen.\n"
           "- **Ostsee**: Fehmarn, Rügen, Usedom, Hiddensee. Rügen ist die größte deutsche Insel.",
           merke="Gefragt sind meist eine nordfriesische und zwei ostfriesische Inseln, zum Beispiel Sylt, Borkum und Norderney."),
        lb("Nordsee gegen Ostsee",
           "- **Gezeiten**: Die Nordsee hat Ebbe und Flut (Tidenhub etwa 3 bis 4 m). In der Ostsee gibt es kaum Gezeiten, weil die Flutwelle nur durch eine enge Passage zwischen den dänischen Inseln hineinkommt.\n"
           "- **Salz**: Nordsee etwa 3,5 %, Ostsee nur etwa 1 % (**Brackwasser**).\n"
           "- **Tiefe**: Nordsee im Durchschnitt etwa 94 m, Ostsee etwa 52 m.\n"
           "- **Küste**: Nordsee mit Watt, Deichen und Dünen. Ostsee mit Förden, Bodden und Steilküsten.",
           merke="Nordsee: Ebbe und Flut, salziger, tiefer. Ostsee: kaum Gezeiten, Brackwasser, flacher."),
        lb("Gezeiten: So entstehen Ebbe und Flut",
           "- Der **Mond** zieht mit seiner **Anziehungskraft** das Wasser an: Wasserberg auf der zugewandten Seite, dort ist **Flut**.\n"
           "- Erde und Mond drehen sich um einen gemeinsamen **Schwerpunkt**. Die **Fliehkraft** drückt das Wasser auf der abgewandten Seite nach außen: zweiter Wasserberg, **zweite Flut**.\n"
           "- Die Erde dreht sich unter den Wasserbergen hindurch: **zweimal Flut und zweimal Ebbe** am Tag, von Flut zu Flut etwa **12 Stunden und 25 Minuten**.\n"
           "- Jeden Tag etwa **50 Minuten** später, weil der Mond weiterwandert.",
           merke="Zwei Wasserberge gleichzeitig: Anziehungskraft (zugewandt) und Fliehkraft (abgewandt)."),
        lb("Gezeiten: Begriffe, Kurve und Tidenkalender",
           "- **Ebbe**: Wasser läuft ab. **Flut**: Wasser läuft auf. Jeweils etwa 6 Stunden.\n"
           "- **Hochwasser (HW)** ist der höchste, **Niedrigwasser (NW)** der niedrigste Wasserstand.\n"
           "- **Tidenhub** = HW − NW, zum Beispiel 3,5 m − 1 m = 2,5 m.\n"
           "- **Kurve**: steigt = Flut, fällt = Ebbe, Gipfel = Hochwasser, Tal = Niedrigwasser.\n"
           "- **Tidenkalender**: Zeile des Tages suchen. Ein Strich (–) heißt: keine Uhrzeit an diesem Tag. Zeitabstand = später minus früher: 10:18 Uhr − 04:05 Uhr = 6 Stunden und 13 Minuten.\n"
           "- Tidenhub: **Bristol (England)**: 12 m, **Saint-Malo (Frankreich)**: 11 m, **Bremerhaven**: 4 m, **Hallig Langeneß**: 3 m (Häuser auf Warften).",
           merke="Tidenhub = Hochwasser − Niedrigwasser. Immer die Einheit dazuschreiben.",
           bild=svg_kurve(300, 3.5, 1.0), bildAlt=ALT_KURVE),
        lb("Wattenmeer: Lebensraum und Zonen",
           "- Das Watt ist voller Nahrung. Darum ist es **Kinderstube** für Jungfische, Platz für **Seehunde** und Rastplatz für Millionen **Zugvögel**.\n"
           "- Salzpflanzen: **Queller** und **Strandflieder**.\n"
           "- **Priele** sind Rinnen im Watt und laufen zuerst voll. Wattwanderung nur mit Wattführer.\n"
           "- Zonen von der See zum Land: **Meer** (immer unter Wasser), **Watt** (zweimal am Tag), **Salzwiese** (selten), **Deich** (im Buch „Düne“, beides zählt).\n"
           "- Grenzen: **mittleres Niedrigwasser** (Meer und Watt), **mittleres Hochwasser** (Watt und Salzwiese).",
           merke="Je weiter weg vom Meer, desto seltener steht die Zone unter Wasser.",
           bild=svg_watt_zonen(False), bildAlt=ALT_WATT),
        lb("Wattenmeer: Schutz und Schutzzonen",
           "- Das Wattenmeer gibt es nur einmal und soll ungestört bleiben. Ein **Nationalpark** ist ein Schutzgebiet, in dem die Natur Vorrang hat. **1986** wurden drei Nationalparks gegründet, seit **2009** ist es **Weltnaturerbe**.\n"
           "- **Zone I, Ruhezone**: strengste Regeln, nicht oder nur auf markierten Wegen betreten.\n"
           "- **Zone II, Zwischenzone**: Betreten, Wattwandern und Bootfahren erlaubt, nur Brutgebiete nicht.\n"
           "- **Zone III, Erholungszone**: Badestrände und Kureinrichtungen.\n"
           "- Regeln auf Schildern: Hunde anleinen, Abstand zu Seehunden, Müll mitnehmen.",
           merke="Ruhezone = strengste Regeln. Zwischenzone = Wattwandern erlaubt. Erholungszone = Badestrände."),
        lb("Küstenschutz: Der Deich",
           "- Ein **Deich** ist ein Erdwall (etwa **1500 Kilometer**). Er schützt die **Marsch** vor **Sturmflut**.\n"
           "- **Seeseite** flach (Wellen laufen hoch und verlieren Kraft), **Landseite** steiler. Oben die **Deichkrone**, unten der **Deichfuß** mit Steinen.\n"
           "- Von innen nach außen: **Sandkern**, **Klei** (fester Lehm), **Grasdecke**. Schafe halten das Gras kurz.\n"
           "- Höhe: 1599 etwa 3 m, 1766 etwa 5,1 m, heute etwa 8,8 m.",
           merke="Seeseite flach, Landseite steil. Innen Sandkern, darüber Klei, außen Grasdecke.",
           bild=svg_deich(False), bildAlt=ALT_DEICH),
        lb("Küstenschutz: Düne und Sieltor",
           "- **Dünen** baut der Wind aus Sand. Der **Strandhafer** hält ihn mit Wurzeln fest (bis zu **5 m** tief). Wer die Düne betritt, zertritt den Strandhafer: Der Sand weht weg und der Schutz geht verloren. Außerdem brüten dort Vögel.\n"
           "- Ein **Siel** ist ein Durchlass im Deich. **Ebbe**: Das Wasser aus der Marsch drückt das Tor auf und fließt ins Meer. **Flut**: Das Meer drückt das Tor zu, kein Salzwasser kommt ins Land.\n"
           "- **Schöpfwerke** pumpen das Wasser über den Deich, wenn das nicht reicht.",
           merke="Düne: Wind und Strandhafer bauen sie, Betreten zerstört sie. Sieltor: Ebbe auf, Flut zu."),
        lb("Tipps für die Arbeit",
           "- Lies jede Aufgabe **zweimal** und teile deine Zeit ein.\n"
           "- Bei 2 oder 3 Punkten wollen die Lehrer meist 2 oder 3 Gedanken sehen.\n"
           "- „Nenne“ = kurz aufzählen. „Erkläre“ und „begründe“ = mit **weil**.\n"
           "- Beim Rechnen die **Einheit** dazuschreiben, beim Beschriften jede Nummer belegen."),
        lb("Checkliste für morgen",
           "**Ich kann:**\n\n"
           "- Bundesländer und Städte an Nordsee und Ostsee nennen.\n"
           "- eine nordfriesische und zwei ostfriesische Inseln nennen.\n"
           "- Nordsee und Ostsee vergleichen.\n"
           "- erklären, wie Ebbe und Flut entstehen.\n"
           "- den Tidenhub aus Kurve und Tidenkalender berechnen.\n"
           "- die Zonen des Watts nennen und erklären, warum das Wattenmeer geschützt wird.\n"
           "- die drei Schutzzonen unterscheiden.\n"
           "- einen Deich zeichnen und beschriften.\n"
           "- erklären, wie Düne und Sieltor schützen."),
    ]


def aufgaben():
    return [
        tf("Schleswig-Holstein hat als einziges Bundesland sowohl Nordsee- als auch Ostseeküste.", True, S,
           info="Niedersachsen liegt nur an der Nordsee, Mecklenburg-Vorpommern nur an der Ostsee. Nachlesen: Crashkurs, Abschnitt „Nord- und Ostsee“."),
        mc("Welche Aussage über die Ostsee stimmt?",
           "Sie ist Brackwasser mit nur etwa 1 % Salz.",
           ["Sie hat einen Tidenhub von 3 bis 4 m.", "Sie ist im Durchschnitt tiefer als die Nordsee.", "Sie hat Watt und Deiche."], S,
           info="Die Ostsee hat kaum Gezeiten, ist flacher (etwa 52 m) und hat Förden und Bodden. Nachlesen: „Nordsee gegen Ostsee“."),
        zuordnen("Welche Insel gehört wohin?",
                 [("Sylt", "Nordfriesische Insel"), ("Borkum", "Ostfriesische Insel"), ("Rügen", "Insel in der Ostsee"), ("Helgoland", "keine der beiden Gruppen")], S,
                 extra=["Insel im Rhein"],
                 info="Nachlesen: „Inseln“."),
        luecke("Ergänze den Text über die Gezeiten.",
               "Die {{Anziehungskraft}} des Mondes zieht das Wasser an. Auf der abgewandten Seite der Erde entsteht Flut durch die {{Fliehkraft}}. "
               "Darum gibt es am Tag {{zweimal}} Flut. Von einer Flut bis zur nächsten vergehen etwa {{12 Stunden und 25 Minuten}}.",
               S, extra=["Reibung", "einmal", "24 Stunden"],
               info="Nachlesen: „Gezeiten: So entstehen Ebbe und Flut“."),
        kurz("Das erste Hochwasser ist heute um 06:30 Uhr. Wann ist es morgen etwa? (Schreibe die Uhrzeit so: 07:20)", ["07:20", "7:20"], S,
             info="Jeden Tag etwa 50 Minuten später: 06:30 Uhr + 50 Minuten = 07:20 Uhr. Nachlesen: „Gezeiten: So entstehen Ebbe und Flut“."),
        kurz("Hochwasser: 4,2 m, Niedrigwasser: 0,9 m. Wie groß ist der Tidenhub?", ["3,3", "3.3", "3,3 m"], S, einheit="m",
             info="Tidenhub = Hochwasser − Niedrigwasser = 4,2 m − 0,9 m = 3,3 m. Nachlesen: „Gezeiten: Begriffe, Kurve und Tidenkalender“."),
        reihenfolge("Ordne die Zonen des Watts von der See zum Land.", ["Meer", "Watt", "Salzwiese", "Deich"], S,
                    info="Je weiter weg vom Meer, desto seltener steht die Zone unter Wasser. Im Buch heißt die vierte Zone „Düne“. Nachlesen: „Wattenmeer: Lebensraum und Zonen“."),
        mc("In welcher Schutzzone des Wattenmeeres gelten die strengsten Regeln?",
           "Zone I, Ruhezone",
           ["Zone II, Zwischenzone", "Zone III, Erholungszone", "In allen Zonen gelten die gleichen Regeln."], S,
           info="Nachlesen: „Wattenmeer: Schutz und Schutzzonen“."),
        tf("Das Sieltor öffnet sich bei Flut, damit das Meerwasser ins Land fließen kann.", False, S,
           info="Bei Flut drückt das Meer das Tor zu. Bei Ebbe öffnet es sich und das Wasser aus der Marsch fließt ab. Nachlesen: „Düne und Sieltor“."),
        mc("Warum darf man Dünen nicht betreten?",
           "Man zertritt den Strandhafer, dann weht der Sand weg und der Schutz geht verloren.",
           ["Weil Dünen aus Beton sind.", "Weil dort die Seehunde leben.", "Weil man sich im Sand verlaufen kann."], S,
           info="Außerdem brüten und ruhen in den Dünen Vögel. Nachlesen: „Düne und Sieltor“."),
        zuordnen("Wie hoch waren die Deiche?",
                 [("1599", "etwa 3 m"), ("1766", "etwa 5,1 m"), ("heute", "etwa 8,8 m")], S,
                 extra=["etwa 12 m"],
                 info="Die Deiche wurden immer höher und breiter. Nachlesen: „Küstenschutz: Der Deich“."),
        luecke("Ergänze die Sätze über den Deich.",
               "Die Seeseite des Deichs ist {{flach}}, die Landseite ist {{steiler|steil}}. Oben liegt die {{Deichkrone}}, unten schützen {{Steine}} den Deichfuß. "
               "Von innen nach außen besteht der Deich aus {{Sandkern}}, {{Klei}} und {{Grasdecke}}.",
               S, extra=["Beton", "Sand", "Schilf"],
               info="Nachlesen: „Küstenschutz: Der Deich“."),
    ]


# Fakten, die im Crashkurs vorkommen und wörtlich im Lernblatt eines Übungspakets stehen müssen
FAKTEN = [
    "Schleswig-Holstein ist das einzige Bundesland, das an beiden Meeren liegt",
    "Cuxhaven, Bremerhaven, Wilhelmshaven, Emden, Husum", "Flensburg, Kiel, Lübeck, Wismar, Rostock, Stralsund, Greifswald",
    "Ems, Weser, Elbe, Eider", "Trave, Warnow, Peene, Oder", "Sylt, Föhr, Amrum, Pellworm", "Borkum, Juist, Norderney, Baltrum, Langeoog, Spiekeroog, Wangerooge",
    "Fehmarn, Rügen, Usedom, Hiddensee", "Rügen ist die größte deutsche Insel",
    "Tidenhub etwa 3 bis 4 m", "etwa 3,5 % Salz", "nur etwa 1 %", "etwa 94 m", "etwa 52 m", "Förden", "Bodden", "Steilküsten",
    "12 Stunden und 25 Minuten", "50 Minuten", "zweimal Flut und zweimal Ebbe",
    "Bristol (England)**: 12 m", "Saint-Malo (Frankreich)**: 11 m", "Bremerhaven**: 4 m", "Hallig Langeneß**: 3 m", "Warften",
    "10:18 Uhr − 04:05 Uhr = 6 Stunden und 13 Minuten", "3,5 m − 1 m = 2,5 m",
    "Queller", "Strandflieder", "Priele", "mittleren Niedrigwasser", "mittleren Hochwasser",
    "1986", "2009", "Weltnaturerbe", "Zone I, Ruhezone", "Zone II, Zwischenzone", "Zone III, Erholungszone",
    "Hunde anleinen", "Abstand zu Seehunden", "Müll mitnehmen", "Brunsbüttel",
    "1500 Kilometer", "Marsch", "Sandkern", "Klei", "Grasdecke", "Deichkrone", "Deichfuß",
    "1599", "etwa 3 m", "etwa 5,1 m", "etwa 8,8 m", "Strandhafer", "bis zu **5 m** tief", "Schöpfwerke",
]


def woerter(text):
    return len(re.findall(r"[\wÄÖÜäöüß%−–„“-]+", re.sub(r"\*\*", "", text)))


def build(pakete=None):
    LB = lernblatt()
    A = aufgaben()
    gesamt = sum(woerter(s["titel"] + " " + s["text"] + " " + (s.get("merke") or "")) for s in LB)
    je = [(s["titel"], woerter(s["text"] + " " + (s.get("merke") or ""))) for s in LB]
    assert gesamt <= 1000, (gesamt, je)
    for titel, w in je:
        assert w <= 130, (titel, w)
    # Fakten gegen die Lernblätter der Übungspakete prüfen
    if pakete is not None:
        quelle = "\n".join(s["text"] + "\n" + (s.get("merke") or "") for p in pakete for s in p["lernblatt"])
        fehlen = [f for f in FAKTEN if f not in quelle]
        assert not fehlen, f"Fakten nicht im Lernblatt: {fehlen}"
        # Aufgaben dürfen nicht wörtlich aus den anderen Paketen stammen
        alte = {t["frage"] + "|" + t.get("text", "") for p in pakete for t in p["aufgaben"]}
        for t in A:
            assert t["frage"] + "|" + t.get("text", "") not in alte, f"Aufgabe schon vorhanden: {t['frage']}"
    assert 8 <= len(A) <= 12, len(A)
    assert not any(t["typ"] == "frei" for t in A)
    p = pack(ID, "Geografie Klasse 6: Crashkurs (Nord- und Ostsee, Gezeiten, Wattenmeer, Küstenschutz)",
             "Das Wichtigste kurz gefasst: der letzte Blick am Tag vor der Arbeit, dazu ein Blitz-Check mit zwölf Kurzaufgaben.",
             LB, A,
             hinweis="Kein neuer Stoff: Alles steht auch in den Lernblättern der Übungspakete. Die vierte Zone des Watts heißt im Buch „Düne“, im Arbeitsblatt „Deich“ (beides zählt).")
    p["probe"] = False
    print(f"Crashkurs: {len(LB)} Abschnitte, {gesamt} Wörter, {len(A)} Blitz-Check-Aufgaben")
    for titel, w in je:
        print(f"   {w:4d}  {titel}")
    return p


if __name__ == "__main__":
    build()
