"""Geografie Klasse 6, Teil 1: Nord- und Ostsee (Punkte 1 bis 4 des Wissenschecks)."""
from geo_lib import *

NORD_STAEDTE = ["Cuxhaven", "Bremerhaven", "Wilhelmshaven", "Emden", "Husum"]
OST_STAEDTE = ["Flensburg", "Kiel", "Lübeck", "Wismar", "Rostock", "Stralsund", "Greifswald"]
NORD_FLUESSE = ["Ems", "Weser", "Elbe", "Eider"]
OST_FLUESSE = ["Trave", "Warnow", "Peene", "Oder"]
NORD_INSELN = ["Sylt", "Föhr", "Amrum", "Pellworm", "Helgoland", "Borkum", "Norderney"]
OST_INSELN = ["Fehmarn", "Rügen", "Usedom", "Hiddensee"]
OSTFRIESISCH = ["Borkum", "Juist", "Norderney", "Baltrum", "Langeoog", "Spiekeroog", "Wangerooge"]
NORDFRIESISCH = ["Sylt", "Föhr", "Amrum", "Pellworm"]

# Längengrade (nur zur Prüfung der Reihenfolgen West nach Ost)
LON = {"Flensburg": 9.43, "Kiel": 10.13, "Lübeck": 10.69, "Wismar": 11.47, "Rostock": 12.14, "Stralsund": 13.08, "Greifswald": 13.38,
       "Emden": 7.21, "Wilhelmshaven": 8.12, "Bremerhaven": 8.58, "Cuxhaven": 8.70, "Husum": 9.05,
       "Borkum": 6.67, "Juist": 7.0, "Norderney": 7.22, "Baltrum": 7.4, "Langeoog": 7.5, "Spiekeroog": 7.7, "Wangerooge": 7.9}


def west_nach_ost(namen):
    assert [LON[n] for n in namen] == sorted(LON[n] for n in namen), namen
    return list(namen)


def lernblatt():
    return [
        lb("Länder und Bundesländer an den Meeren",
           "- **Nordsee**: Die deutschen Bundesländer an der Nordsee sind **Schleswig-Holstein** und **Niedersachsen**. Dazu kommen die Stadtstaaten **Hamburg** (an der Elbe) und **Bremen** (an der Weser).\n"
           "- **Ostsee**: Die deutschen Bundesländer an der Ostsee sind **Schleswig-Holstein** und **Mecklenburg-Vorpommern**.\n"
           "- Länder rund um die **Nordsee**: Deutschland, Dänemark, Niederlande, Belgien, Frankreich, Vereinigtes Königreich und Norwegen.\n"
           "- Länder rund um die **Ostsee**: Deutschland, Dänemark, Schweden, Finnland, Russland, Estland, Lettland, Litauen und Polen.\n"
           "- Der **Nord-Ostsee-Kanal** verbindet beide Meere. Er verläuft von Brunsbüttel (Nordsee) nach Kiel (Ostsee).",
           merke="Schleswig-Holstein ist das einzige Bundesland, das an beiden Meeren liegt."),
        lb("Nordsee und Ostsee im Vergleich",
           "- **Gezeiten**: Die Nordsee hat Ebbe und Flut (Tidenhub etwa 3 bis 4 m). In der Ostsee gibt es kaum Gezeiten, denn die Flutwelle kommt nur durch eine enge Passage zwischen den dänischen Inseln hinein.\n"
           "- **Salzgehalt**: Die Nordsee hat etwa 3,5 % Salz. Die Ostsee hat nur etwa 1 % und ist **Brackwasser** (ein Gemisch aus Salz- und Süßwasser). Sie ist das größte Brackwassermeer der Welt.\n"
           "- **Verbindung zum Ozean**: Die Nordsee ist weit zum Atlantik geöffnet. Die Ostsee ist fast abgeschlossen und hat nur schmale Zugänge (ein **Binnenmeer**).\n"
           "- **Tiefe**: Die Nordsee ist im Durchschnitt etwa 94 m tief. Die Ostsee ist flacher, im Durchschnitt etwa 52 m. Ihre tiefste Stelle liegt bei etwa 459 m.\n"
           "- **Küste**: An der Nordsee gibt es Watt, Deiche und Dünen. An der Ostsee gibt es **Förden** (lange Meeresbuchten), **Bodden** (flache Buchten), Steilküsten und Sandstrände.\n"
           "- **Wellen**: Die Nordsee ist oft rau mit hohen Wellen. Die Ostsee ist meist ruhiger. In kalten Wintern kann sie teilweise zufrieren.",
           merke="Vier Unterschiede reichen: Gezeiten, Salzgehalt, Tiefe und Küstenform. Die Nordsee hat Ebbe und Flut, ist salziger und tiefer. Die Ostsee hat kaum Gezeiten, ist Brackwasser und flacher."),
        lb("Städte, Flüsse und Inseln",
           "- **Städte an der Nordsee**: Cuxhaven, Bremerhaven, Wilhelmshaven, Emden, Husum. (Hamburg und Bremen liegen weiter landeinwärts an Elbe und Weser.)\n"
           "- **Städte an der Ostsee**: Flensburg, Kiel, Lübeck, Wismar, Rostock, Stralsund, Greifswald.\n"
           "- **Flüsse zur Nordsee**: Ems, Weser, Elbe, Eider.\n"
           "- **Flüsse zur Ostsee**: Trave, Warnow, Peene, Oder.\n"
           "- **Inseln in der Nordsee**: Sylt, Föhr, Amrum, Pellworm, Helgoland, Borkum, Norderney.\n"
           "- **Inseln in der Ostsee**: Fehmarn, Rügen, Usedom, Hiddensee.",
           merke="Rügen ist die größte deutsche Insel. Die Elbe fließt bei Hamburg vorbei und mündet bei Cuxhaven in die Nordsee. Bei Namen hilft der Blick in den Atlas."),
        lb("Nordfriesische und Ostfriesische Inseln",
           "- Die **Nordfriesischen Inseln** liegen vor Schleswig-Holstein: Sylt, Föhr, Amrum, Pellworm.\n"
           "- Die **Ostfriesischen Inseln** liegen vor Niedersachsen. Von West nach Ost: Borkum, Juist, Norderney, Baltrum, Langeoog, Spiekeroog, Wangerooge.\n"
           "- **Helgoland** liegt weit draußen in der Nordsee und gehört zu keiner der beiden Gruppen.\n"
           "- Eselsbrücke (ein Vorschlag, du kannst dir auch eine eigene ausdenken): **B**ei **J**edem **N**ordwind **B**rauchen **L**ange **S**ieben **W**indjacken.",
           merke="Für den Wissenscheck brauchst du eine nordfriesische und mindestens zwei ostfriesische Inseln, zum Beispiel Sylt, Borkum und Norderney."),
    ]


def aufgaben():
    A = []
    # ------------------------------------------------------------------ A Meere und Länder
    s = "A – Meere und Länder"
    A += [
        mc("Welches Bundesland liegt an der Nordsee und an der Ostsee?", "Schleswig-Holstein", ["Niedersachsen", "Mecklenburg-Vorpommern", "Bremen"], s),
        mc("Welches Bundesland liegt nur an der Ostsee?", "Mecklenburg-Vorpommern", ["Niedersachsen", "Schleswig-Holstein", "Hamburg"], s,
           info="Schleswig-Holstein liegt an beiden Meeren, Niedersachsen nur an der Nordsee."),
        mc("An welchem Meer liegt Niedersachsen?", "Nordsee", ["Ostsee", "Nordsee und Ostsee", "Mittelmeer"], s),
        zuordnen("Ordne jedem Bundesland sein Meer zu.", [("Schleswig-Holstein", "Nordsee und Ostsee"), ("Niedersachsen", "nur Nordsee"), ("Mecklenburg-Vorpommern", "nur Ostsee")], s),
        luecke("Ergänze den Text über die deutschen Meere.",
               "Schleswig-Holstein liegt an der {{Nordsee}} und an der {{Ostsee}}. Der {{Nord-Ostsee-Kanal}} verbindet beide Meere miteinander. Er verläuft von {{Brunsbüttel}} nach Kiel.",
               s, extra=["Mittelmeer", "Rhein"]),
        tf("Hamburg und Bremen sind Stadtstaaten. Sie liegen an der Elbe und an der Weser.", True, s),
        mc("Welches Land liegt an der Nordsee, aber nicht an der Ostsee?", "Niederlande", ["Polen", "Estland", "Litauen"], s),
        mc("Welches Land liegt an der Ostsee, aber nicht an der Nordsee?", "Polen", ["Niederlande", "Belgien", "Vereinigtes Königreich"], s),
        zuordnen("Zu welchem Meer gehört das Land?", [("Niederlande", "Nordsee"), ("Polen", "Ostsee"), ("Belgien", "Nordsee"), ("Estland", "Ostsee"), ("Lettland", "Ostsee"), ("Norwegen", "Nordsee")], s),
        tf("Dänemark hat eine Küste an der Nordsee und an der Ostsee.", True, s),
        kurz("Wie heißt der Kanal, der die Nordsee mit der Ostsee verbindet?", ["Nord-Ostsee-Kanal", "Nord-Ostsee Kanal", "Kiel-Kanal", "NOK"], s,
             info="Der Kanal verläuft von Brunsbüttel an der Elbmündung bis nach Kiel."),
        mc("In welcher Stadt endet der Nord-Ostsee-Kanal an der Ostsee?", "Kiel", ["Rostock", "Cuxhaven", "Husum"], s),
    ]
    # ------------------------------------------------------------------ B Unterschiede
    s = "B – Unterschiede zwischen Nordsee und Ostsee"
    A += [
        mc("Welches Meer hat deutliche Gezeiten (Ebbe und Flut)?", "Nordsee", ["Ostsee", "Beide gleich stark", "Keines von beiden"], s),
        mc("Wie viel Salz enthält das Wasser der Nordsee etwa?", "etwa 3,5 %", ["etwa 1 %", "etwa 10 %", "etwa 0,1 %"], s),
        kurz("Wie viel Prozent Salz hat die Ostsee etwa?", ["1", "1 %", "1%"], s, einheit="%", info="Wegen des geringen Salzgehalts nennt man die Ostsee ein Brackwassermeer."),
        mc("Wie nennt man Wasser, das aus einer Mischung von Salz- und Süßwasser besteht?", "Brackwasser", ["Meerwasser", "Quellwasser", "Sole"], s),
        tf("Die Ostsee ist tiefer als die Nordsee.", False, s, info="Die Nordsee ist im Durchschnitt etwa 94 m tief, die Ostsee nur etwa 52 m."),
        kurz("Wie tief ist die Nordsee im Durchschnitt?", ["94", "94 m"], s, einheit="m"),
        kurz("Wie tief ist die Ostsee im Durchschnitt?", ["52", "52 m"], s, einheit="m"),
        mc("Welche Küstenformen gibt es an der Ostsee?", "Förden, Bodden und Steilküsten", ["Watt, Deiche und Dünen", "Wüsten und Oasen", "Fjorde und Gletscher"], s),
        mc("Welche Küstenformen gibt es an der Nordsee?", "Watt, Deiche und Dünen", ["Förden, Bodden und Steilküsten", "Korallenriffe", "Vulkane"], s),
        zuordnen("Gehört das zur Nordsee oder zur Ostsee?", [("Ebbe und Flut", "Nordsee"), ("Brackwasser", "Ostsee"), ("Watt", "Nordsee"), ("Förden", "Ostsee"), ("Bodden", "Ostsee"), ("Deiche", "Nordsee")], s),
        luecke("Ergänze den Vergleich.",
               "Die {{Nordsee}} ist weit zum Atlantik geöffnet, deshalb gibt es dort Ebbe und Flut. Die {{Ostsee}} ist fast abgeschlossen. Sie ist ein {{Binnenmeer}} und enthält nur etwa 1 % Salz, also {{Brackwasser}}.",
               s, extra=["Ozean", "Süßwasser"]),
        mc("Warum gibt es in der Ostsee kaum Gezeiten?", "Die Flutwelle kommt nur durch eine enge Passage zwischen den dänischen Inseln hinein.",
           ["Die Ostsee ist zu kalt.", "Der Mond zieht dort nicht am Wasser.", "Es gibt in der Ostsee keine Küsten."], s),
        tf("Die Ostsee ist mit dem Atlantik nur durch schmale Zugänge verbunden.", True, s, info="Darum sagt man auch Binnenmeer."),
        tf("In sehr kalten Wintern kann die Ostsee teilweise zufrieren.", True, s),
        tf("Die Ostsee ist das größte Brackwassermeer der Welt.", True, s),
        mc("Wie tief ist die Ostsee an ihrer tiefsten Stelle etwa?", "etwa 459 m", ["etwa 59 m", "etwa 159 m", "etwa 1459 m"], s),
        mc("Welche Aussage über die Nordsee stimmt?", "Sie ist oft rau mit hohen Wellen.", ["Sie ist ein Binnenmeer.", "Sie hat nur 1 % Salz.", "Sie ist flacher als die Ostsee."], s),
        frei("Nenne vier Unterschiede zwischen Nordsee und Ostsee.",
             "Gezeiten: Die Nordsee hat Ebbe und Flut, die Ostsee kaum. Salzgehalt: Die Nordsee hat etwa 3,5 %, die Ostsee etwa 1 % (Brackwasser). Tiefe: Die Nordsee ist im Durchschnitt etwa 94 m tief, die Ostsee nur etwa 52 m. Küste: An der Nordsee gibt es Watt, Deiche und Dünen, an der Ostsee Förden, Bodden und Steilküsten.",
             ["Gezeiten richtig genannt", "Salzgehalt richtig genannt", "Tiefe richtig genannt", "Küstenform richtig genannt"], 4, s),
        frei("Erkläre, warum man an der Ostsee kaum Gezeiten spürt.",
             "Die Flutwelle läuft von Norden in die Nordsee, an der englischen, niederländischen und deutschen Küste entlang und bei Dänemark wieder hinaus. Nur ein kleiner Teil strömt um Dänemark herum in die Ostsee, und die dänischen Inseln stehen im Weg. Deshalb spürt man in der Ostsee kaum Gezeiten.",
             ["Die Flutwelle kommt nur durch eine enge Passage in die Ostsee", "Die dänischen Inseln stehen im Weg", "Deshalb kaum Gezeiten"], 2, s),
    ]
    # ------------------------------------------------------------------ C Städte
    s = "C – Städte an den Küsten"
    A += [
        zuordnen("Zu welchem Meer gehört die Stadt?", [("Kiel", "Ostsee"), ("Cuxhaven", "Nordsee"), ("Rostock", "Ostsee"), ("Emden", "Nordsee"), ("Lübeck", "Ostsee"), ("Husum", "Nordsee")], s),
        zuordnen("Zu welchem Meer gehört die Stadt?", [("Flensburg", "Ostsee"), ("Wilhelmshaven", "Nordsee"), ("Stralsund", "Ostsee"), ("Bremerhaven", "Nordsee"), ("Wismar", "Ostsee"), ("Greifswald", "Ostsee")], s),
        mc("Welche Stadt liegt an der Ostsee?", "Rostock", ["Emden", "Husum", "Wilhelmshaven"], s),
        mc("Welche Stadt liegt an der Nordsee?", "Cuxhaven", ["Kiel", "Lübeck", "Stralsund"], s),
        mc("Welche Stadt liegt nicht an der Ostsee?", "Bremerhaven", ["Flensburg", "Wismar", "Greifswald"], s),
        mc("Welche Stadt liegt nicht an der Nordsee?", "Lübeck", ["Emden", "Cuxhaven", "Husum"], s),
        luecke("Ergänze die Städte.", "An der Nordsee liegen zum Beispiel {{Cuxhaven}}, {{Emden}} und {{Husum}}. An der Ostsee liegen zum Beispiel {{Kiel}}, {{Lübeck}} und {{Rostock}}.", s,
               extra=["Hamburg", "Dresden"]),
        mc("Hamburg liegt nicht direkt am Meer. Wo liegt Hamburg?", "an der Elbe, weiter landeinwärts", ["an der Ostsee", "an der Weser", "auf einer Insel"], s),
        reihenfolge("Ordne diese Städte an der Ostsee von West nach Ost.", west_nach_ost(["Kiel", "Lübeck", "Rostock", "Stralsund", "Greifswald"]), s,
                    tipp="Kiel liegt in Schleswig-Holstein, Greifswald in Mecklenburg-Vorpommern ganz im Osten."),
        reihenfolge("Ordne diese Städte an der Nordsee von West nach Ost.", west_nach_ost(["Emden", "Wilhelmshaven", "Bremerhaven", "Cuxhaven", "Husum"]), s),
        kurz("Welche Hafenstadt liegt an der Mündung der Elbe in die Nordsee?", ["Cuxhaven"], s),
        tf("Schleswig-Holstein hat Städte an der Nordsee und an der Ostsee.", True, s, info="Zum Beispiel Husum an der Nordsee und Kiel an der Ostsee."),
    ]
    # ------------------------------------------------------------------ D Flüsse
    s = "D – Flüsse"
    A += [
        zuordnen("In welches Meer mündet der Fluss?", [("Elbe", "Nordsee"), ("Warnow", "Ostsee"), ("Weser", "Nordsee"), ("Trave", "Ostsee"), ("Ems", "Nordsee"), ("Peene", "Ostsee")], s),
        mc("Welcher Fluss mündet in die Ostsee?", "Warnow", ["Weser", "Elbe", "Eider"], s),
        mc("Welcher Fluss mündet in die Nordsee?", "Weser", ["Trave", "Peene", "Oder"], s),
        mc("Welcher Fluss fließt bei Hamburg vorbei und mündet bei Cuxhaven in die Nordsee?", "Elbe", ["Ems", "Trave", "Oder"], s),
        kurz("An welchem Fluss liegt Hamburg?", ["Elbe"], s),
        kurz("An welchem Fluss liegt Bremen?", ["Weser"], s),
        kurz("An welchem Fluss liegt Rostock?", ["Warnow"], s, info="Die Warnow mündet bei Warnemünde in die Ostsee."),
        kurz("An welchem Fluss liegt Lübeck?", ["Trave"], s, info="Die Trave mündet bei Travemünde in die Ostsee."),
        luecke("Ergänze die Flüsse.", "Die {{Elbe}}, die {{Weser}} und die {{Ems}} fließen in die Nordsee. Die {{Warnow}}, die {{Trave}} und die {{Oder}} fließen in die Ostsee.", s,
               extra=["Donau", "Rhein"]),
        tf("Die Ems mündet in die Ostsee.", False, s, info="Die Ems mündet in die Nordsee."),
    ]
    # ------------------------------------------------------------------ E Inseln
    s = "E – Inseln"
    A += [
        zuordnen("In welchem Meer liegt die Insel?", [("Sylt", "Nordsee"), ("Rügen", "Ostsee"), ("Borkum", "Nordsee"), ("Fehmarn", "Ostsee"), ("Norderney", "Nordsee"), ("Usedom", "Ostsee")], s),
        mc("Welches ist die größte deutsche Insel?", "Rügen", ["Sylt", "Borkum", "Fehmarn"], s),
        mc("Welche Insel liegt in der Ostsee?", "Hiddensee", ["Föhr", "Amrum", "Helgoland"], s),
        mc("Welche Insel liegt in der Nordsee?", "Pellworm", ["Usedom", "Rügen", "Fehmarn"], s),
        zuordnen("Gehört die Insel zu den Nordfriesischen oder zu den Ostfriesischen Inseln?",
                 [("Sylt", "Nordfriesisch"), ("Borkum", "Ostfriesisch"), ("Föhr", "Nordfriesisch"), ("Norderney", "Ostfriesisch"), ("Amrum", "Nordfriesisch"), ("Spiekeroog", "Ostfriesisch")], s),
        mc("Vor welchem Bundesland liegen die Nordfriesischen Inseln?", "Schleswig-Holstein", ["Niedersachsen", "Mecklenburg-Vorpommern", "Bremen"], s),
        mc("Vor welchem Bundesland liegen die Ostfriesischen Inseln?", "Niedersachsen", ["Schleswig-Holstein", "Mecklenburg-Vorpommern", "Hamburg"], s),
        mc("Welche Insel gehört nicht zu den Ostfriesischen Inseln?", "Sylt", ["Juist", "Baltrum", "Langeoog"], s),
        tf("Helgoland gehört zu den Ostfriesischen Inseln.", False, s, info="Helgoland liegt weit draußen in der Nordsee und gehört zu keiner der beiden Inselgruppen."),
        reihenfolge("Ordne die sieben Ostfriesischen Inseln von West nach Ost.", west_nach_ost(OSTFRIESISCH), s,
                    tipp="Eselsbrücke: Bei Jedem Nordwind Brauchen Lange Sieben Windjacken."),
        kurz("Welche Ostfriesische Insel liegt ganz im Westen?", ["Borkum"], s),
        kurz("Welche Ostfriesische Insel liegt ganz im Osten?", ["Wangerooge"], s),
        luecke("Ergänze die Ostfriesischen Inseln von West nach Ost.", "{{Borkum}}, {{Juist}}, {{Norderney}}, {{Baltrum}}, {{Langeoog}}, {{Spiekeroog}}, {{Wangerooge}}", s,
               extra=["Sylt", "Rügen"]),
        luecke("Ergänze die Nordfriesischen Inseln.", "Zu den Nordfriesischen Inseln gehören {{Sylt}}, {{Föhr}}, {{Amrum}} und {{Pellworm}}.", s, extra=["Borkum", "Usedom"]),
        frei("Nenne eine nordfriesische und zwei ostfriesische Inseln und sage, wo sie liegen.",
             "Sylt ist eine nordfriesische Insel und liegt vor Schleswig-Holstein. Borkum und Norderney sind ostfriesische Inseln und liegen vor Niedersachsen.",
             ["eine nordfriesische Insel (zum Beispiel Sylt, Föhr, Amrum, Pellworm)", "zwei ostfriesische Inseln (zum Beispiel Borkum, Juist, Norderney)", "Lage vor Schleswig-Holstein beziehungsweise Niedersachsen"], 3, s),
    ]
    return A


def build():
    return pack("geografie-1-nord-ostsee", "Geografie Teil 1: Nord- und Ostsee",
                "Bundesländer und Länder, Unterschiede zwischen Nord- und Ostsee, Städte, Flüsse, Inseln. Mit Lernblatt und vielen Übungsaufgaben.",
                lernblatt(), aufgaben(), min_aufgaben=50,
                hinweis="Die Karte zu diesem Teil lag nicht vor. Städte, Flüsse und Inseln bitte mit dem Atlas oder der Karte aus dem Unterricht abgleichen.")
