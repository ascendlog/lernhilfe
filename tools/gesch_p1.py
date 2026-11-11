"""Geschichte Klasse 6, Teil 1: Quellen, Lebenslauf und Stammbaum (Lernzettel Punkt 2, Buch S. 7 und 9).

Alles Beispielmaterial (Familie Berger, Lea, Mia) ist erfunden. Jahre und Zahlen werden im Code berechnet.
"""
from gesch_lib import *
from gesch_lib import _svg, _label, _num, _arrow, PERSONEN, kinder, svg_stammbaum

P = PERSONEN


# ------------------------------------------------------------------ Prüfwerte aus dem Stammbaum (Familie Berger)
assert sorted(kinder("Jan")) == ["Mia", "Tom"] and sorted(kinder("Hans")) == ["Anna"] and kinder("Karl") == ["Jan"]
ENKEL_HANS = sum(len(kinder(k)) for k in kinder("Hans"))
assert ENKEL_HANS == 2
KARL_JAHRE = P["Karl"]["tod"] - P["Karl"]["geb"]
assert KARL_JAHRE == 67
assert P["Eva"]["beruf"] == "Schneiderin" and P["Hans"]["beruf"] == "Bäcker" and P["Hans"]["eltern"] is None
GEB_SORT = sorted(["Hans", "Karl", "Jan", "Anna", "Tom"], key=lambda n: P[n]["geb"])
assert GEB_SORT == ["Hans", "Karl", "Jan", "Anna", "Tom"]
# Reihenfolge nach Alter bei Gegenständen (Steinzeit, Mittelalter, 1950, gestern)
assert epoche(-20000) == "Ur- und Frühgeschichte" and epoche(1200) == "Mittelalter" and epoche(1950) == "Neuzeit"


def alt_stamm(marker=None, versteckt=()):
    """Bildbeschreibung des Stammbaums (passend zu svg_stammbaum)."""
    def n(name):
        return "ein Kästchen mit Fragezeichen" if name in versteckt else name

    def zeile(name):
        p = P[name]
        s = f"{n(name)} (geboren {p['geb']}" + (f", gestorben {p['tod']}" if p["tod"] else "") + f", {p['beruf']}"
        if name in (marker or {}):
            s += f", Nummer {marker[name]}"
        return s + ")"
    return ("Stammbaum der erfundenen Familie Berger in drei Reihen. Oben die Kinder " + zeile("Tom") + " und " + zeile("Mia") +
            ". In der Mitte ihre Eltern " + zeile("Jan") + " und " + zeile("Anna") + ", verheiratet (zwei Ringe). Unten die Großeltern: " +
            zeile("Karl") + " und " + zeile("Ruth") + " (Eltern von Jan) sowie " + zeile("Hans") + " und " + zeile("Eva") + " (Eltern von Anna).")


# ------------------------------------------------------------------ Zeichnung: von der kleinen zur großen Geschichte

STUFEN = ["Ich und meine Familie", "Ortsgeschichte: mein Wohnort", "Regionalgeschichte: meine Umgebung",
          "Nationalgeschichte: mein Land", "Weltgeschichte: alle Länder"]


def svg_stufen():
    farben = ["#fbe3c8", "#f6d58f", "#cfe3b5", "#b9d6ea", "#d9c4e6"]
    g = []
    for i, t in enumerate(STUFEN):
        w = 300 + i * 90
        y = 14 + i * 56
        g.append(f'<rect x="20" y="{y}" width="{w}" height="46" rx="8" fill="{farben[i]}" stroke="#555" stroke-width="2"/>')
        g.append(_label(20 + w / 2, y + 29, t, size=17, weight="bold"))
    return _svg(720, 300, ''.join(g))


# ------------------------------------------------------------------ Lernblatt

def lernblatt():
    return [
        lb("Was ist eine Quelle?",
           "Menschen und ihre Zeit hinterlassen Spuren. Wer etwas über früher herausfinden will, sucht nach diesen Spuren. Man nennt sie **Quellen**.\n"
           "Eine **Quelle** ist etwas, das aus einer früheren Zeit übrig geblieben ist. Aus ihr kann man etwas über diese Zeit erfahren.\n"
           "Ein Beispiel: Dein Zeugnis aus der Grundschule ist eine Quelle. Es verrät, welche Fächer du hattest und welche Noten du bekommen hast. Auch ein altes Foto oder ein Brief von früher sind Quellen.\n"
           "Aus der Steinzeit sind vor allem Knochen, Werkzeuge und Zeichnungen in Höhlen erhalten. Aus ihnen lesen die Forscher ab, wie die Menschen damals lebten.",
           merke="Quelle = etwas aus der früheren Zeit selbst, aus dem man etwas über diese Zeit erfährt."),
        lb("Quellengattungen: Buch und Heft",
           "Es gibt viele Arten von Quellen. Im Buch werden sie so eingeteilt:\n"
           "- **schriftliche Quellen**: alles Geschriebene, zum Beispiel Briefe, Urkunden und Inschriften\n"
           "- **bildliche Quellen**: zum Beispiel Höhlenzeichnungen, Gemälde, Plakate und Fotos\n"
           "- **gegenständliche Quellen**: alles, was man anfassen kann, zum Beispiel Münzen, Waffen und Werkzeuge\n"
           "- **mündliche Überlieferung**: Erinnerungen, die von Generation zu Generation weitererzählt werden\n"
           "In deinem Heft stehen fünf Gruppen. Lerne beide Einteilungen:\n"
           "- **Sachquellen** (das sind die gegenständlichen Quellen): Knochen, Waffen, Schmuck, Versteinerungen, Bauwerke, Statuen, Kleidung, Werkzeug, Scherben, Münzen\n"
           "- **Texte** (die schriftlichen Quellen): Bücher, Schriftrollen, Pergament, Inschriften, Urkunden, Verträge, Gesetze\n"
           "- **Bilder** (die bildlichen Quellen): Malereien und Fotos\n"
           "- **Tonaufnahmen und Filme**\n"
           "- **Zeitzeugen**: Menschen, die etwas selbst erlebt haben und davon erzählen\n"
           "Der Unterschied bei den Menschen: Ein Zeitzeuge war selbst dabei. Bei der mündlichen Überlieferung wird eine Geschichte über viele Generationen weitererzählt.",
           merke="Sachquelle = gegenständliche Quelle, Texte = schriftliche Quellen, Bilder = bildliche Quellen. Münzen zählst du zu den Sachquellen."),
        lb("Quellen erkennen und einordnen",
           "Wenn du eine Quelle einordnen sollst, stelle dir diese Fragen: Kann man es anfassen? Ist es geschrieben? Ist es ein Bild? Hört man es oder sieht man es als Film? Erzählt ein Mensch, der dabei war?\n"
           "Beispiele aus drei Zeiten:\n"
           "- **Heute**: ein Foto vom Klassenausflug (Bild), dein Zeugnis (Text), eine Sprachnachricht (Tonaufnahme), dein altes Spielzeug (Sachquelle), dein Opa erzählt, was er als Kind erlebt hat (Zeitzeuge)\n"
           "- **Steinzeit**: ein Faustkeil und ein Knochen (Sachquellen), eine Höhlenzeichnung (Bild)\n"
           "- **Mittelalter**: eine Urkunde auf Pergament (Text), eine Burg (Bauwerk, also Sachquelle), ein Schwert und eine Münze (Sachquellen)\n"
           "Das Mittelalter dauerte ungefähr von 500 bis 1500 nach Christus.",
           merke="Erst fragen, was es ist (Gegenstand, Text, Bild, Ton, Mensch), dann die Gruppe nennen."),
        lb("Wie Historiker vorgehen",
           "Ein **Historiker** erforscht die Geschichte. Er geht in drei Schritten vor:\n"
           "- **1. Eine Frage stellen.** Am Anfang steht immer eine Frage, zum Beispiel: „Warum brach der Erste Weltkrieg aus?“\n"
           "- **2. Quellen suchen.** Er sucht Quellen aus der Zeit, über die er etwas wissen will. Meist findet er sie in Archiven.\n"
           "- **3. Quellen auswerten.** Er untersucht die Quellen und beantwortet seine Frage damit.\n"
           "Ein Beispiel aus dem Buch: Klio besucht die Saalburg, ein römisches Kastell (Kastell = Militärlager der Römer) mit Museum. Sie will darüber einen Aufsatz schreiben und fragt sich zuerst, wann sie dort waren. Zu Hause sammelt sie, was ihr vom Besuch geblieben ist: Eintrittskarte, Ansichtskarten, ein Buch, eine Spielfigur eines römischen Legionärs, ihr Heft mit dem Aufsatz, die Aussagen von Eltern und Bruder und die Internetseite der Saalburg. Das sind ihre Quellen.\n"
           "Klio legt alles in eine Kiste. Diese Kiste ist ihr **Privatarchiv**.",
           merke="Frage, Quellen suchen, Quellen auswerten: So arbeitet ein Historiker."),
        lb("Überlieferung und Archive",
           "Der Weg einer Quelle von ihrer Entstehung bis heute heißt **Überlieferung**. Unterwegs kann viel passieren: Quellen wechseln den Besitzer, verschwinden und tauchen wieder auf. Sie können beschädigt oder verändert werden.\n"
           "Darum kennen wir aus der Vergangenheit immer nur einen Teil der Quellen.\n"
           "Ein **Archiv** ist ein Ort, an dem Schriftstücke, Gegenstände, Karten und Fotos aufbewahrt werden. Historiker suchen dort nach Quellen. Auch eine Familie kann ein Archiv haben, zum Beispiel eine Kiste mit Fotos und Briefen (Privatarchiv).",
           merke="Überlieferung = der Weg einer Quelle bis heute. Archiv = Ort, an dem Quellen aufbewahrt werden."),
        lb("Quelle oder Darstellung?",
           "Eine **Darstellung** machen Menschen später über eine Zeit, die sie nicht selbst erlebt haben. Sie benutzen dafür Quellen.\n"
           "Beispiele für Darstellungen: ein Schulbuchtext über die Steinzeit und eine Rekonstruktionszeichnung der Altsteinzeit. Der Zeichner hat die Zeit nicht gesehen, er hat nach Funden gezeichnet.\n"
           "Die Funde selbst, zum Beispiel Knochen und Werkzeuge, sind dagegen Quellen. Sie stammen aus der Zeit selbst.\n"
           "Ein Test: Stammt es aus der damaligen Zeit oder hat es jemand viel später gemacht? Das Erste ist eine Quelle, das Zweite eine Darstellung.",
           merke="Eine Rekonstruktionszeichnung ist eine Darstellung, keine Quelle. Die Funde, auf denen sie beruht, sind Quellen."),
        lb("Lebenslauf: meine eigene Geschichte",
           "Ein **Lebenslauf** erzählt deine eigene Lebensgeschichte. Man schreibt ihn meist als Tabelle, zum Beispiel bei einer Bewerbung.\n"
           "Das Buch nennt diese Teile: Name, Geburtstag, Kindergarten, Grundschule, weiterführende Schule, wichtige Ereignisse, Sport und Hobbys.\n"
           "Ein erfundenes Beispiel: Mia Berger, geboren 2014, Kindergarten, Grundschule, danach Gymnasium. Sport: Schwimmen. Hobby: Lesen.\n"
           "Auch dein Leben hinterlässt Quellen: Geburtsurkunde, Spielzeug, selbst gemalte Bilder, Zeugnisse und Fotos. Wer seinen Lebensweg aufschreibt, wird selbst zum Historiker.",
           merke="Lebenslauf = die eigene Lebensgeschichte, oft als Tabelle. Quellen: Geburtsurkunde, Zeugnisse, Fotos, Spielzeug."),
        lb("Der Stammbaum",
           "Mit einem **Stammbaum** stellt man die Geschichte einer Familie als Bild dar. Man sieht alle Familienmitglieder und wie sie miteinander verwandt sind.\n"
           "So ist er aufgebaut: Geschwister stehen nebeneinander. Die Kinder stehen meist über ihren Eltern, denn ein Baum wächst von unten nach oben. Manchmal hängt man sie auch unter das Elternpaar. Bei jeder Person stehen Beruf und oft auch Geburtsort.\n"
           "Diese Zeichen musst du kennen:\n"
           "- **∞** oder **zwei Ringe ⚭**: verheiratet mit\n"
           "- **∗**: geboren\n"
           "- **†**: gestorben\n"
           "Mit einem Stammbaum kannst du fragen: Wie lange haben die Familienmitglieder gelebt? Wie viele Kinder hatten sie? Welchen Beruf? Sind sie umgezogen? Wie weit kann man die Familie zurückverfolgen?\n"
           "Herrscherfamilien führten ihren Stammbaum oft auf große Könige, Heilige oder Götter zurück. So wollten sie zeigen, dass sie zu Recht herrschen.",
           merke="∗ = geboren, † = gestorben, zwei Ringe = verheiratet. Geschwister nebeneinander, Kinder über den Eltern.",
           bild=svg_stammbaum(), bildAlt=alt_stamm()),
        lb("Von der kleinen zur großen Geschichte",
           "Geschichte beginnt bei dir: bei deinem Leben und deiner Familie. Von dort geht es in Stufen immer weiter.\n"
           "- **Ortsgeschichte**: die Geschichte deines Wohnorts\n"
           "- **Regionalgeschichte**: die Geschichte der näheren Umgebung\n"
           "- **Nationalgeschichte**: die Geschichte deines Landes\n"
           "- **Weltgeschichte**: die Geschichte aller Länder und Menschen\n"
           "Auch zeitlich geht es immer weiter zurück, bis zu den ersten Menschen.",
           merke="Von klein nach groß: Familie, Ort, Region, Nation, Welt.",
           bild=svg_stufen(), bildAlt="Fünf Balken, die von oben nach unten immer breiter werden: Ich und meine Familie, Ortsgeschichte (mein Wohnort), Regionalgeschichte (meine Umgebung), Nationalgeschichte (mein Land), Weltgeschichte (alle Länder)."),
    ]


# ------------------------------------------------------------------ Aufgaben

def block_a():
    s = "A – Was ist eine Quelle?"
    return [
        mc("Was ist eine Quelle in der Geschichte?",
           "Etwas aus früherer Zeit, aus dem man etwas über damals erfährt",
           ["Ein Text, den ein Historiker heute über eine frühere Zeit schreibt",
            "Ein Ort, an dem Gegenstände aus der Vergangenheit aufbewahrt werden",
            "Eine Jahreszahl, mit der man Ereignisse auf dem Zeitstrahl einordnet"], s,
           info="Eine Quelle stammt aus der früheren Zeit selbst und verrät uns etwas über sie."),
        luecke("Ergänze den Satz über Quellen.",
               "Menschen hinterlassen aus ihrer Zeit {{Spuren}}. Solche Spuren heißen {{Quellen}}. Mit ihnen erfährt man etwas über die {{frühere|damalige}} Zeit.",
               s, extra=["Darstellungen", "Zukunft"],
               info="Spuren aus früherer Zeit heißen Quellen."),
        tf("Dein Zeugnis aus der Grundschule ist eine Quelle.", True, s,
           info="Es stammt aus deiner früheren Schulzeit und verrät etwas darüber, zum Beispiel Fächer und Noten."),
        tf("Ein Schulbuchtext von heute über die Steinzeit ist eine Quelle aus der Steinzeit.", False, s,
           info="Der Text wurde viele tausend Jahre später geschrieben. Er ist eine Darstellung, die auf Quellen beruht.",
           tipp="Frage dich: Stammt der Text aus der Steinzeit selbst?"),
        mc("Wähle alle richtigen Antworten: Was ist eine Quelle?",
           ["Ein Foto von einer Familienfeier vor 40 Jahren", "Ein Faustkeil aus der Steinzeit"],
           ["Ein Schulbuchtext über das Mittelalter", "Eine Zeichnung von heute, die ein Steinzeitlager nach Funden nachbildet"], s,
           info="Foto und Faustkeil stammen aus der früheren Zeit selbst. Buchtext und Nachzeichnung sind erst später entstanden und gehören zu den Darstellungen.",
           tipp="Eine Quelle stammt aus der Zeit, über die sie etwas verrät."),
        kurz("Dein Zeugnis, ein altes Foto und ein Brief von früher haben etwas gemeinsam: Sie sind ... (Fachwort in der Mehrzahl)",
             ["Quellen", "Quelle", "die Quellen", "historische Quellen", "geschichtliche Quellen"], s,
             info="Alle drei stammen aus einer früheren Zeit und erzählen etwas darüber. Das macht sie zu Quellen."),
    ]


def block_b():
    s = "B – Quellengattungen in Buch und Heft"
    return [
        zuordnen("Ordne jeder Quellengattung aus dem Buch ein Beispiel zu.",
                 [("schriftliche Quelle", "Brief"), ("bildliche Quelle", "Höhlenzeichnung"), ("gegenständliche Quelle", "Münze"),
                  ("mündliche Überlieferung", "Geschichte, die seit Generationen weitererzählt wird")],
                 s, extra=["Schulbuchtext"],
                 info="Schriftlich ist alles Geschriebene, bildlich sind Bilder, gegenständlich ist alles Greifbare. Mündlich wird weitererzählt."),
        mc("Wie heißen im Buch alle greifbaren Quellen wie Münzen, Waffen und Werkzeuge?",
           "gegenständliche Quellen", ["schriftliche Quellen", "bildliche Quellen", "mündliche Überlieferung"], s,
           info="Gegenständlich kommt von Gegenstand: Man kann diese Quellen anfassen. Im Heft heißen sie Sachquellen."),
        zuordnen("Ordne jeder Quellengruppe aus dem Heft ein Beispiel zu.",
                 [("Sachquellen", "Scherbe eines Tonkrugs"), ("Texte", "Vertrag auf Pergament"), ("Bilder", "Foto vom ersten Schultag"),
                  ("Tonaufnahmen und Filme", "Aufnahme einer Rede im Radio"), ("Zeitzeugen", "Mann, der etwas Selbsterlebtes erzählt")],
                 s, extra=["Rekonstruktionszeichnung"],
                 info="Das Heft kennt fünf Gruppen. Eine Rekonstruktionszeichnung gehört nicht dazu, denn sie ist eine Darstellung."),
        luecke("Ergänze die Gattungen aus dem Buch.",
               "Im Buch gibt es {{schriftliche}} Quellen (Briefe, Urkunden), {{bildliche}} Quellen (Gemälde, Fotos) und {{gegenständliche}} Quellen (Münzen, Waffen). Dazu kommt die {{mündliche}} Überlieferung.",
               s, extra=["akustische", "digitale"],
               info="Diese vier Begriffe sollst du aus dem Buch kennen."),
        tf("Sachquelle und gegenständliche Quelle sind zwei Namen für dieselbe Gruppe von Quellen.", True, s,
           info="Das Heft sagt Sachquellen, das Buch sagt gegenständliche Quellen. Gemeint sind greifbare Dinge."),
        mc("Was unterscheidet einen Zeitzeugen von der mündlichen Überlieferung?",
           "Der Zeitzeuge erzählt, was er selbst erlebt hat. Bei der Überlieferung wird über Generationen weitererzählt.",
           ["Der Zeitzeuge erzählt, was er von seinen Urgroßeltern gehört hat. Die Überlieferung ist selbst erlebt.",
            "Zeitzeugen sind Gegenstände, die mündliche Überlieferung besteht aus Texten.",
            "Beides sind Bilder, nur aus unterschiedlichen Zeiten."], s,
           info="Beim Zeitzeugen ist die Erzählung selbst erlebt. Die mündliche Überlieferung wird von Generation zu Generation weitergegeben.",
           tipp="Wer war selbst dabei?"),
        kurz("Wie heißt im Heft die Quellengruppe, zu der Bücher, Schriftrollen, Urkunden und Verträge gehören?",
             ["Texte", "Text", "die Texte"], s,
             info="Im Buch heißen diese Quellen schriftliche Quellen."),
        mc("Welche Gruppe gehört nicht zu den fünf Quellengruppen im Heft?",
           "Darstellungen", ["Sachquellen", "Zeitzeugen", "Tonaufnahmen und Filme"], s,
           info="Darstellungen sind keine Quellen. Sie entstehen erst später, mit Hilfe von Quellen.",
           tipp="Sind Darstellungen Hinterlassenschaften aus der Zeit selbst?"),
    ]


def block_c():
    s = "C – Quellen erkennen und einordnen"
    return [
        zuordnen("Zu welcher Quellengruppe aus dem Heft gehört das Beispiel?",
                 [("Faustkeil", "Sachquellen"), ("Urkunde aus dem Mittelalter", "Texte"), ("Foto vom Schulfest", "Bilder"),
                  ("Sprachnachricht", "Tonaufnahmen und Filme"), ("Opa erzählt von seiner Kindheit", "Zeitzeugen")],
                 s, extra=["Archive"],
                 info="Frage dich bei jedem Beispiel: Ist es ein Ding, ein Text, ein Bild, ein Ton oder ein Mensch, der berichtet?"),
        mc("Eine Burg aus dem Mittelalter steht noch heute. Zu welcher Quellengruppe im Heft gehört sie?",
           "Sachquellen", ["Texte", "Bilder", "Zeitzeugen"], s,
           info="Bauwerke stehen im Heft bei den Sachquellen."),
        mc("Eine Höhlenzeichnung zeigt Tiere der Eiszeit. Welche Gattung ist das im Buch?",
           "bildliche Quelle", ["schriftliche Quelle", "gegenständliche Quelle", "mündliche Überlieferung"], s,
           info="Höhlenzeichnungen nennt das Buch bei den bildlichen Quellen."),
        mc("Lea findet auf dem Dachboden den Brief ihrer Urgroßmutter, ein altes Foto und eine Spieluhr. Wähle alle richtigen Antworten.",
           ["Der Brief ist eine schriftliche Quelle.", "Das Foto ist eine bildliche Quelle.", "Die Spieluhr ist eine gegenständliche Quelle."],
           ["Der Brief ist eine mündliche Überlieferung.", "Das Foto ist ein Zeitzeuge."], s,
           info="Brief = Text, Foto = Bild, Spieluhr = Gegenstand. Mündliche Überlieferung und Zeitzeugen sind Erzählungen von Menschen."),
        tf("Ein Kinofilm von heute, in dem Schauspieler das Mittelalter nachspielen, ist eine Quelle aus dem Mittelalter.", False, s,
           info="Der Film ist erst heute entstanden und beruht auf Quellen. Er ist eine Darstellung.",
           tipp="Wann ist der Film entstanden?"),
        mc("Wähle alle richtigen Antworten: Welche dieser Dinge sind Sachquellen?",
           ["Eine Statue", "Eine Scherbe", "Eine Münze"], ["Ein Vertrag", "Ein Foto", "Eine Tonaufnahme"], s,
           info="Statuen, Scherben und Münzen sind Gegenstände. Vertrag = Text, Foto = Bild."),
        kurz("Eine Geschichte wird seit vielen Generationen von den Eltern an die Kinder weitererzählt. Wie heißt diese Art der Quelle?",
             ["mündliche Überlieferung", "die mündliche Überlieferung", "mündliche Überlieferungen", "mündlich überliefert"], s,
             info="Was von Generation zu Generation weitererzählt wird, nennt das Buch mündliche Überlieferung."),
        reihenfolge("Ordne diese Quellen nach ihrem Alter. Die älteste steht zuerst.",
                    ["Faustkeil aus der Steinzeit", "Urkunde aus dem Mittelalter", "Foto aus dem Jahr 1950", "Sprachnachricht von gestern"], s,
                    info="Steinzeit kommt vor dem Mittelalter (500 bis 1500). Danach folgt 1950, zuletzt die Nachricht von gestern.",
                    tipp="Die Steinzeit ist viel älter als das Mittelalter."),
    ]


def mit(t, lesen):
    """Setzt das Feld lesen (Titel eines Lernblatt-Abschnitts) an einer Aufgabe."""
    t["lesen"] = lesen
    return t


L_HIST, L_UEBER, L_DAR = "Wie Historiker vorgehen", "Überlieferung und Archive", "Quelle oder Darstellung?"
L_LEBEN, L_KLEIN, L_STAMM = "Lebenslauf: meine eigene Geschichte", "Von der kleinen zur großen Geschichte", "Der Stammbaum"


def block_d():
    s = "D – Historiker, Überlieferung und Darstellung"
    return [
        mit(reihenfolge("Ordne die Schritte, mit denen ein Historiker vorgeht.",
                        ["Eine Frage stellen", "Quellen aus der Zeit suchen, meist in Archiven", "Die Quellen auswerten"], s,
                        info="Am Anfang steht die Frage. Danach sucht man Quellen und wertet sie aus, um die Frage zu beantworten."), L_HIST),
        mit(mc("Womit beginnt die Arbeit eines Historikers immer?",
               "Mit einer Frage an die Vergangenheit",
               ["Mit dem Aufräumen eines Archivs", "Mit dem Zeichnen eines Zeitstrahls", "Mit dem Anfertigen eines Stammbaums"], s,
               info="Ohne Frage weiß man nicht, welche Quellen man suchen soll. Klio fragte zum Beispiel: Wann waren wir auf der Saalburg?"), L_HIST),
        mit(kurz("Wie nennt man einen Ort, an dem Schriftstücke, Gegenstände, Karten und Fotos aufbewahrt werden?",
                 ["Archiv", "das Archiv", "ein Archiv", "Archive"], s,
                 info="Historiker suchen ihre Quellen meist in Archiven."), L_UEBER),
        mit(kurz("Klio legt alle Erinnerungsstücke an den Besuch der Saalburg in eine Kiste. Wie nennt das Buch diese Sammlung?",
                 ["Privatarchiv", "das Privatarchiv", "ihr Privatarchiv", "ein Privatarchiv", "Privat-Archiv", "privates Archiv"], s,
                 info="Eine Sammlung, die jemand privat aufbewahrt, ist ein Privatarchiv.",
                 tipp="Ein Archiv, das einer einzelnen Person gehört, nicht einem Amt."), L_UEBER),
        mit(luecke("Ergänze den Text über den Weg einer Quelle.",
                   "Der Weg einer Quelle von der Entstehung bis heute heißt {{Überlieferung}}. Unterwegs kann eine Quelle den {{Besitzer}} wechseln, {{verschwinden}} und wieder auftauchen. Sie kann auch {{beschädigt}} oder verändert werden.",
                   s, extra=["Archiv", "Epoche"],
                   info="Wegen der Überlieferung wissen wir von der Vergangenheit immer nur einen Teil."), L_UEBER),
        mit(tf("Alle Quellen aus der Vergangenheit sind bis heute erhalten geblieben.", False, s,
               info="Quellen verschwinden, werden beschädigt oder verändert. Darum bleibt unser Wissen oft lückenhaft."), L_UEBER),
        mit(mc("Welche dieser Aussagen beschreibt eine Darstellung?",
               "Eine Zeichnerin malt heute ein Steinzeitlager nach Funden.",
               ["Ein Steinzeitmensch malt ein Tier an eine Höhlenwand.", "Ein Mensch aus dem Mittelalter schreibt eine Urkunde.",
                "Ein Faustkeil liegt im Boden und wird von Forschern gefunden."], s,
               info="Die Zeichnerin hat die Steinzeit nicht erlebt. Sie benutzt Funde, die Quellen sind, und macht daraus eine Darstellung.",
               tipp="Wer hat die Zeit selbst erlebt, wer nicht?"), L_DAR),
        mit(zuordnen("Ist es eine Quelle oder eine Darstellung?",
                     [("Faustkeil aus der Steinzeit", "Quelle"), ("Rekonstruktionszeichnung der Altsteinzeit", "Darstellung"),
                      ("Schulbuchtext über die Steinzeit", "Darstellung"), ("Höhlenzeichnung", "Quelle"),
                      ("Knochenfund", "Quelle"), ("Urkunde aus dem Mittelalter", "Quelle")], s,
                     info="Funde und Dinge aus der Zeit selbst sind Quellen. Was später mit Hilfe von Quellen gezeichnet oder geschrieben wurde, ist eine Darstellung."), L_DAR),
        mit(tf("Eine Rekonstruktionszeichnung ist eine Quelle.", False, s,
               info="Sie ist eine Darstellung. Die Funde, nach denen gezeichnet wurde, sind die Quellen."), L_DAR),
    ]


def block_e():
    s = "E – Lebenslauf und kleine bis große Geschichte"
    return [
        mit(mc("Wie nennt man die eigene Lebensgeschichte, die man oft als Tabelle aufschreibt?",
               "Lebenslauf", ["Stammbaum", "Zeitstrahl", "Archiv"], s,
               info="Einen Lebenslauf verlangt man zum Beispiel bei einer Bewerbung."), L_LEBEN),
        mit(mc("Wähle alle richtigen Antworten: Was gehört in einen Lebenslauf nach der Vorlage im Buch?",
               ["Geburtstag", "Grundschule", "Hobbys"], ["Beruf der Großeltern", "Todesjahr der Eltern", "Namen der Urgroßeltern"], s,
               info="Ein Lebenslauf handelt von dir. Die Daten der Großeltern gehören in den Stammbaum."), L_LEBEN),
        mit(zuordnen("Zu welcher Quellengruppe aus dem Heft gehört die Quelle aus deinem Leben?",
                     [("Geburtsurkunde", "Texte"), ("Kuscheltier aus der Kindheit", "Sachquellen"), ("Selbst gemaltes Bild", "Bilder"),
                      ("Video vom Sportfest", "Tonaufnahmen und Filme")], s, extra=["Zeitzeugen"],
                     info="Urkunde = Text, Kuscheltier = Gegenstand, gemaltes Bild = Bild, Video = Film."), L_LEBEN),
        mit(kurz("Wer seinen Lebensweg aufschreibt und dafür Zeugnisse und Fotos benutzt, wird zum ... (Berufsbezeichnung)",
                 ["Historiker", "Historikerin", "zum Historiker", "ein Historiker", "Geschichtsforscher", "Geschichtsforscherin"], s,
                 info="Wer die Spuren seines Lebens ordnet und auswertet, arbeitet wie ein Historiker.",
                 tipp="Wer erforscht die Geschichte?"), L_LEBEN),
        mit(luecke("Ergänze die Stufen der Geschichte.",
                   "Die Geschichte deines Wohnorts heißt {{Ortsgeschichte}}, die Geschichte deiner Umgebung {{Regionalgeschichte}}. Die Geschichte deines Landes heißt {{Nationalgeschichte}} und die Geschichte aller Länder {{Weltgeschichte}}.",
                   s, extra=["Familiengeschichte", "Erdgeschichte"],
                   info="Die Stufen werden immer größer: Ort, Region, Nation, Welt."), L_KLEIN),
        mit(reihenfolge("Ordne von der kleinen zur großen Geschichte.",
                        ["Ich und meine Familie", "Ortsgeschichte", "Regionalgeschichte", "Nationalgeschichte", "Weltgeschichte"], s,
                        info="Man beginnt bei sich selbst und geht Schritt für Schritt weiter nach außen."), L_KLEIN),
        mit(mc("Ein Buch erzählt die Geschichte Deutschlands. Welche Stufe der Geschichte ist das?",
               "Nationalgeschichte", ["Ortsgeschichte", "Regionalgeschichte", "Weltgeschichte"], s,
               info="Deutschland ist ein Land, also eine Nation. Die Geschichte eines Landes heißt Nationalgeschichte."), L_KLEIN),
        mit(tf("Zur Weltgeschichte gehört nur das, was in deinem eigenen Land passiert ist.", False, s,
               info="Die Weltgeschichte umfasst alle Länder und Menschen. Das eigene Land ist die Nationalgeschichte."), L_KLEIN),
    ]


def block_f():
    s = "F – Der Stammbaum und die Familie Berger"
    bild, alt = svg_stammbaum(), alt_stamm()
    mk = {"Tom": 1, "Anna": 2, "Karl": 3}
    return [
        mc("Was zeigt ein Stammbaum?",
           "Die Mitglieder einer Familie und wie sie verwandt sind",
           ["Die Reihenfolge der Epochen auf einem Zeitstrahl", "Alle Quellen, die in einem Archiv liegen", "Die Noten eines Schülers aus allen Schuljahren"], s,
           info="Mit einem Stammbaum stellt man Familiengeschichte als Bild dar."),
        zuordnen("Was bedeutet das Zeichen im Stammbaum?",
                 [("∗", "geboren"), ("†", "gestorben"), ("zwei Ringe ⚭", "verheiratet mit")], s,
                 extra=["ist umgezogen", "hat Kinder"],
                 info="Der Stern steht für die Geburt, das Kreuz für den Tod. Zwei Ringe zeigen, dass zwei Personen verheiratet sind."),
        luecke("Ergänze den Satz über Stammbäume.",
               "Mit einem {{Stammbaum}} kann man {{Familiengeschichte}} bildlich darstellen. Das Zeichen ∗ steht für {{geboren}}, das Zeichen † für {{gestorben|tot}}. Zwei Ringe bedeuten {{verheiratet}}.",
               s, extra=["Lebenslauf", "Zeitstrahl"],
               info="Alle drei Zeichen findest du auch in unserem Stammbaum der Familie Berger."),
        tf("Tom und Mia sind Geschwister. Im Stammbaum der Familie Berger stehen sie nebeneinander.", True, s,
           info=f"Geschwister stehen nebeneinander. Beide haben dieselben Eltern, Jan und Anna.", bild=bild, bildAlt=alt),
        kurz("Wie viele Jahre liegen zwischen Karls Geburtsjahr und seinem Todesjahr?",
             [str(KARL_JAHRE), f"{KARL_JAHRE} Jahre", f"{KARL_JAHRE} Jahre alt"], s, einheit="Jahre",
             info=f"Karl wurde {P['Karl']['geb']} geboren (∗) und starb {P['Karl']['tod']} (†). {P['Karl']['tod']} minus {P['Karl']['geb']} sind {KARL_JAHRE} Jahre.",
             tipp="Rechne Todesjahr minus Geburtsjahr.", bild=bild, bildAlt=alt),
        kurz("Wie viele Enkelkinder haben Hans und Eva?",
             [str(ENKEL_HANS), "zwei", f"{ENKEL_HANS} Enkelkinder", "zwei Enkelkinder"], s,
             info="Hans und Eva haben eine Tochter, Anna. Annas Kinder Tom und Mia sind ihre Enkelkinder.",
             tipp="Enkelkinder sind die Kinder der eigenen Kinder.", bild=bild, bildAlt=alt),
        mc("Wie ist Person 3 mit Person 1 verwandt?",
           "Person 3 ist der Großvater von Person 1.",
           ["Person 3 ist der Vater von Person 1.", "Person 3 ist der Onkel von Person 1.", "Person 3 ist der Bruder von Person 1."], s,
           info="Karl (3) ist der Vater von Jan. Jan ist der Vater von Tom (1). Also ist Karl Toms Großvater.",
           tipp="Gehe von Person 1 Schritt für Schritt nach unten.", bild=svg_stammbaum(marker=mk), bildAlt=alt_stamm(marker=mk)),
        mc("Im Stammbaum ist ein Name durch ein Fragezeichen ersetzt. Wer ist diese Person für Mia?",
           "Mias Großmutter, die Mutter von Anna",
           ["Mias Großmutter, die Mutter von Jan", "Mias Tante, die Schwester von Anna", "Mias Schwester"], s,
           info="Die Person ist mit Hans verheiratet. Beide sind die Eltern von Anna, und Anna ist Mias Mutter.",
           tipp="Folge der Linie vom Ehepaar nach oben.", bild=svg_stammbaum(versteckt=("Eva",)), bildAlt=alt_stamm(versteckt=("Eva",))),
        kurz("Welchen Beruf hat im Stammbaum der Mann, der mit Eva verheiratet ist?",
             ["Bäcker", "der Bäcker", "Hans ist Bäcker"], s,
             info=f"Eva ist mit Hans verheiratet. Hans ist {P['Hans']['beruf']}.", bild=bild, bildAlt=alt),
        reihenfolge("Ordne diese Personen der Familie Berger nach ihrem Geburtsjahr. Die älteste Person steht zuerst.",
                    GEB_SORT, s,
                    info="Geburtsjahre: " + ", ".join(f"{n} {P[n]['geb']}" for n in GEB_SORT) + ".",
                    tipp="Schau auf die Zahl hinter dem Stern.", bild=bild, bildAlt=alt),
        tf("Herrscherfamilien führten ihren Stammbaum oft auf große Könige, Heilige oder Götter zurück, um ihre Herrschaft zu rechtfertigen.", True, s,
           info="Sie wollten damit ihre Würde und ihren Anspruch auf die Herrschaft betonen."),
        mc("Welche Frage kann man mit einem Stammbaum nicht beantworten?",
           "Welche Waffen benutzten die Vorfahren?",
           ["Wie lange lebten die Familienmitglieder?", "Wie viele Kinder hatte jedes Paar?", "Welche Berufe übten die Vorfahren aus?"], s,
           info="Ein Stammbaum zeigt Verwandtschaft, Lebensdaten, Kinder und Berufe, aber nichts über Waffen."),
    ]


def block_g():
    s = "G – Klausurnahe Aufgaben"
    bild, alt = svg_stammbaum(), alt_stamm()
    kinder_jan = " und ".join(f"{n} (geboren {P[n]['geb']})" for n in sorted(kinder("Jan"), key=lambda n: -P[n]["geb"]))
    return [
        mit(zuordnen("Ordne jedem Begriff die richtige Erklärung zu.",
                     [("Quelle", "Etwas aus früherer Zeit, aus dem man etwas über damals erfährt"),
                      ("Darstellung", "Etwas, das später mit Hilfe von Quellen gemacht wurde"),
                      ("Archiv", "Ort, an dem Schriftstücke, Gegenstände, Karten und Fotos aufbewahrt werden"),
                      ("Überlieferung", "Weg einer Quelle von der Entstehung bis heute"),
                      ("Zeitzeuge", "Mensch, der etwas selbst erlebt hat")], s,
                     extra=["Abschnitt der Geschichte, zum Beispiel das Mittelalter"],
                     info="Das sind die wichtigsten Begriffe dieses Themas. Der Abschnitt der Geschichte heißt Epoche und gehört zu einem anderen Thema."),
            [L_DAR, L_UEBER, L_HIST]),
        mit(mc("Welche Aussage über Quelle und Darstellung stimmt?",
               "Eine Quelle stammt aus der Zeit selbst, eine Darstellung entsteht später mit Hilfe von Quellen.",
               ["Eine Darstellung stammt aus der Zeit selbst, eine Quelle entsteht später mit Hilfe von Darstellungen.",
                "Quelle und Darstellung sind dasselbe, nur mit zwei Namen.",
                "Eine Quelle ist immer ein Text, eine Darstellung immer ein Bild."], s,
               info="Genau das ist der Unterschied: Quellen sind Hinterlassenschaften der Zeit, Darstellungen sind spätere Werke.",
               tipp="Denke an den Faustkeil und an die Rekonstruktionszeichnung."), L_DAR),
        mit(luecke("Ergänze den Text über die Arbeit von Historikern.",
                   "Historiker beginnen mit einer {{Frage}}. Dann suchen sie {{Quellen}}, meist in {{Archiven|Archiv}}. Diese Quellen müssen sie {{auswerten}}. Was Menschen später mit Hilfe von Quellen schreiben oder zeichnen, ist eine {{Darstellung}}.",
                   s, extra=["Epoche", "Zeitstrahl"],
                   info="Frage, Quellen suchen, auswerten: So gehen Historiker vor."), [L_HIST, L_DAR]),
        mit(frei("Erkläre den Unterschied zwischen einer Quelle und einer Darstellung. Nenne zu beiden ein Beispiel.",
                 "Eine Quelle stammt aus der früheren Zeit selbst und verrät etwas über sie, zum Beispiel ein Faustkeil oder ein Brief. Eine Darstellung machen Menschen später über eine Zeit, die sie nicht selbst erlebt haben, und sie benutzen dafür Quellen. Beispiele sind ein Schulbuchtext oder eine Rekonstruktionszeichnung der Altsteinzeit.",
                 ["Quelle stammt aus der Zeit selbst", "Darstellung entsteht später mit Hilfe von Quellen", "passendes Beispiel für eine Quelle", "passendes Beispiel für eine Darstellung"], 4, s), L_DAR),
        mit(frei("Nenne die fünf Quellengruppen aus dem Heft und gib zu jeder Gruppe ein Beispiel.",
                 "Sachquellen: zum Beispiel ein Faustkeil oder eine Münze. Texte: zum Beispiel eine Urkunde. Bilder: zum Beispiel ein Foto oder eine Malerei. Tonaufnahmen und Filme: zum Beispiel die Aufnahme einer Rede. Zeitzeugen: zum Beispiel ein Mensch, der berichtet, was er selbst erlebt hat.",
                 ["Sachquellen mit Beispiel", "Texte mit Beispiel", "Bilder mit Beispiel", "Tonaufnahmen und Filme mit Beispiel", "Zeitzeugen mit Beispiel"], 5, s), "Quellengattungen: Buch und Heft"),
        mit(frei("Du siehst den Stammbaum der Familie Berger. Nenne vier verschiedene Arten von Angaben, die man aus ihm ablesen kann.",
                 f"Jan und Anna sind verheiratet und haben zwei Kinder: {kinder_jan}. Tom und Mia sind Geschwister. Karl wurde {P['Karl']['geb']} geboren und starb {P['Karl']['tod']}. Hans ist von Beruf {P['Hans']['beruf']}, Anna ist {P['Anna']['beruf']}. Der Stammbaum zeigt drei Generationen.",
                 ["Verwandtschaft (zum Beispiel Eltern und Kinder oder Geschwister)", "Zahl der Kinder", "Lebensdaten (geboren oder gestorben)", "Beruf einer Person"], 4, s,
                 bild=bild, bildAlt=alt), L_STAMM),
        mit(frei("Lea will herausfinden, wie ihr Wohnort vor 50 Jahren aussah. Beschreibe, wie sie wie eine Historikerin vorgehen kann, und nenne zwei passende Quellen.",
                 "Lea beginnt mit einer Frage: Wie sah unser Ort vor 50 Jahren aus? Dann sucht sie Quellen, zum Beispiel alte Fotos aus dem Familienarchiv oder dem Ortsarchiv und Briefe. Sie kann auch ältere Menschen fragen, die damals im Ort gelebt haben, das sind Zeitzeugen. Zuletzt wertet sie die Quellen aus und beantwortet ihre Frage.",
                 ["Frage formuliert", "Quellen werden gesucht (Archiv, Familie oder Zeitzeugen)", "zwei passende Quellen genannt", "Quellen werden ausgewertet"], 4, s), [L_HIST, L_UEBER]),
    ]


def aufgaben():
    return block_a() + block_b() + block_c() + block_d() + block_e() + block_f() + block_g()


def build():
    p = pack("geschichte-1-quellen-stammbaum", "Geschichte Teil 1: Quellen, Lebenslauf und Stammbaum",
             "Was ist eine Quelle, welche Arten gibt es (Buch und Heft), wie arbeiten Historiker, Quelle und Darstellung, Lebenslauf, Stammbaum der Familie Berger und von der kleinen zur großen Geschichte. Mit Lernblatt und Übungsaufgaben.",
             lernblatt(), aufgaben(), min_aufgaben=48,
             hinweis="Die Familie Berger, Lea und Mia sind erfunden. Bei den Quellengruppen kennt das Heft andere Namen als das Buch, beide stehen im Lernblatt.")
    nachlesen(p, {
        "A – Was ist eine Quelle?": "Was ist eine Quelle?",
        "B – Quellengattungen in Buch und Heft": "Quellengattungen: Buch und Heft",
        "C – Quellen erkennen und einordnen": "Quellen erkennen und einordnen",
        "D – Historiker, Überlieferung und Darstellung": [L_HIST, L_UEBER, L_DAR],
        "E – Lebenslauf und kleine bis große Geschichte": [L_LEBEN, L_KLEIN],
        "F – Der Stammbaum und die Familie Berger": L_STAMM,
        "G – Klausurnahe Aufgaben": [L_HIST, L_UEBER, L_DAR, L_STAMM, "Quellengattungen: Buch und Heft"],
    })
    p["probe"] = False
    assert 48 <= len(p["aufgaben"]) <= 60, len(p["aufgaben"])
    assert 5 <= len(p["lernblatt"]) <= 9
    return [p]
