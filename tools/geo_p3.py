"""Geografie Klasse 6, Teil 3: Wattenmeer (Punkte 8 bis 10 des Wissenschecks)."""
from geo_lib import *


def lernblatt():
    return [
        lb("Das Wattenmeer: ein besonderer Lebensraum",
           "Das Wattenmeer zieht sich an der Nordsee entlang, vom niederländischen Den Helder bis nach Dänemark. Bei **Ebbe** läuft das Wasser ab und der Meeresboden liegt frei, bei **Flut** kommt das Wasser zurück. Von weitem sieht das Watt grau und leer aus. In Wahrheit ist es voller Leben und gehört zu den letzten Landschaften, die der Mensch kaum verändert hat.\n"
           "- **Viel Nahrung**: Im Wattboden leben Millionen winziger Algen, Würmer, Muscheln und Schnecken. Der Wattwurm frisst Schlick und hinterlässt kleine Kothäufchen, die man bei Ebbe sieht.\n"
           "- **Kinderstube**: Junge Fische, Garnelen und andere Jungtiere wachsen im flachen Wasser auf. Dort sind sie vor großen Raubfischen sicher.\n"
           "- **Seehunde** ziehen auf den Sandbänken ihre Jungen groß.\n"
           "- **Zugvögel**: Im Frühjahr und im Herbst machen Millionen Zugvögel hier Rast, weil sie viel Futter finden. Manche brüten auch hier. Das Watt gehört zu den vogelreichsten Gebieten der Erde.\n"
           "- **Salzpflanzen**: Der **Queller** (fleischig, mit kleinen schuppigen Blättern) und der **Strandflieder** vertragen Salzwasser. Der Queller hält außerdem den Schlick fest.\n"
           "- **Angepasst**: Viele Tiere sind genau auf diesen Lebensraum eingestellt. Wird er gestört, kommen sie schlecht zurecht.",
           merke="Das Watt bietet viel Nahrung. Darum ist es Futterplatz, Kinderstube für Fische und Brut- und Rastplatz für Vögel. Weil die Tiere so angepasst sind, schadet jede Störung."),
        lb("Wer lebt wo? Meer, Watt und Salzwiese",
           "- **Meer** (immer unter Wasser): Hier suchen Schwimm- und Tauchvögel Futter, hier leben die Fische, und Seehunde ruhen auf Sandbänken.\n"
           "- **Watt** (zweimal am Tag unter Wasser): Zuhause von Garnelen, Jungfischen, Muscheln, Krebstieren und Wattwürmern. Auch der Austernfischer sucht hier sein Futter.\n"
           "- **Salzwiese** (nur selten unter Wasser): Hier brüten Vögel, und die Salzpflanzen wachsen (Queller, Strandflieder).\n"
           "- **Priele** sind Rinnen im Watt, in denen das Wasser abläuft und wieder zuläuft. Für Badende und Wattwanderer sind sie gefährlich. Eine Wattwanderung ohne Wattführer ist riskant, denn die Flut kommt schnell und die Priele laufen zuerst voll.",
           merke="Je weiter weg vom Meer, desto seltener steht eine Zone unter Wasser: Meer, Watt, Salzwiese."),
        lb("Warum und wie wird das Wattenmeer geschützt?",
           "- **Warum?** Ein Watt wie das der Nordsee gibt es nur einmal auf der Erde. Es soll sich möglichst ohne den Einfluss des Menschen weiterentwickeln, denn jede Störung gefährdet die angepassten Tiere. Gleichzeitig leben die Menschen an der Küste von Fischerei, Landwirtschaft, Industrie und Tourismus. Deshalb gibt es für die Nutzung strenge Regeln.\n"
           "- Ein **Nationalpark** ist ein Schutzgebiet, in dem die Natur Vorrang hat und möglichst in Ruhe gelassen wird. Es gelten besondere Regeln.\n"
           "- **1986** wurden in Deutschland drei Nationalparks im Wattenmeer gegründet: das Schleswig-Holsteinische, das Hamburgische und das Niedersächsische Wattenmeer. Auch Dänemark und die Niederlande schützen ihre Teile.\n"
           "- Seit **2009** gehören große Gebiete zum **Weltnaturerbe** der Menschheit. Die Küstenlinie ist etwa 450 km lang.\n"
           "- **Schutzzonen**: In Schleswig-Holstein und Hamburg gibt es zwei, in Niedersachsen drei.\n"
           "- **Hinweisschilder** zeigen, was man tun soll und was verboten ist. Beispiele: Das Vorland darf vom 1. April bis 31. Juli nicht betreten werden (Brut- und Aufzuchtzeit der Vögel), Hunde anleinen, Pflanzen nicht pflücken, Abstand zu Seehunden halten, Müll mitnehmen.\n"
           "- Gegen strenge Regeln sind oft Fischer, Landwirte, Industrie, Tourismus-Betriebe und Hafenbetreiber, weil die Regeln ihre Arbeit einschränken.",
           merke="Das Wattenmeer ist einzigartig und soll möglichst ungestört bleiben. Darum gibt es Nationalparks (1986), das Weltnaturerbe (seit 2009), Schutzzonen und Hinweisschilder."),
        lb("Die drei Schutzzonen",
           "- **Zone I, Ruhezone**: Hier gelten die strengsten Regeln. Dazu gehören Wattflächen, Seehundbänke, Salzwiesen und Dünen. Besucher dürfen sie nicht oder nur auf markierten Wegen betreten, damit die Tiere ungestört bleiben. Fisch- und Krabbenfang sind nur eingeschränkt erlaubt. Das Buch nennt hier Salzwiesen, Seehundbänke und Brutgebiete der Vögel.\n"
           "- **Zone II, Zwischenzone**: Betreten, Wattwandern und Bootfahren sind erlaubt. Nur die Brutgebiete der Vögel darf man nicht oder nur auf markierten Wegen betreten. Baden, Fischerei und Jagd sind erlaubt.\n"
           "- **Zone III, Erholungszone**: Badestrände und Kureinrichtungen, also Ferien- und Kurbetrieb. Strandbuggies und Motorfahrzeuge sind verboten. Laut Buch dürfen hier außerdem Häfen gebaut und Erdöl gefördert werden.",
           merke="Ruhezone = strengste Regeln. Zwischenzone = Betreten und Wattwandern erlaubt. Erholungszone = Badestrände und Kureinrichtungen."),
        lb("Die vier Zonen des Watts",
           "Von der See zum Land (Arbeitsblatt „Lebensraum Watt“, Buch S. 130):\n"
           "- **Meer**: ständig unter Wasser.\n"
           "- **Watt**: zweimal am Tag unter Wasser, bei Ebbe trocken. Es liegt zwischen dem mittleren Niedrigwasser und dem mittleren Hochwasser.\n"
           "- **Salzwiese**: nur selten unter Wasser. Hier wachsen Salzpflanzen wie der Queller, und Vögel brüten.\n"
           "- **Deich**: schützt das Land und steht nicht unter Wasser. Im Buch (S. 130) steht an dieser Stelle „Düne“. Beide Antworten zählen in den Aufgaben als richtig.\n"
           "Die Grenze zwischen Meer und Watt ist das **mittlere Niedrigwasser**, die Grenze zwischen Watt und Salzwiese das **mittlere Hochwasser**.",
           merke="Meer, Watt, Salzwiese, Deich: Je weiter weg vom Meer, desto seltener steht die Zone unter Wasser.",
           bild=svg_watt_zonen(False), bildAlt="Querschnitt von der See zum Land mit den vier Zonen Meer, Watt, Salzwiese und Deich und den Marken für mittleres Niedrigwasser und mittleres Hochwasser"),
    ]


def aufgaben():
    A = []
    # ------------------------------------------------------------------ A Lebensraum Watt
    s = "A – Der Lebensraum Watt"
    A += [
        tf("Das Watt fällt zweimal am Tag trocken.", True, s),
        tf("Im Wattenmeer leben nur sehr wenige Tiere.", False, s, info="Im Wattenmeer leben sehr viele Tiere, es ist reich an Nährstoffen."),
        tf("Das Wattenmeer ist eine Kinderstube für junge Fische.", True, s),
        tf("Der Queller wächst in der Salzwiese und verträgt Salzwasser.", True, s),
        tf("Ohne Wattführer ist eine Wattwanderung ungefährlich.", False, s, info="Die Flut kommt schnell und die Priele füllen sich zuerst."),
        tf("Zugvögel nutzen das Wattenmeer als Rastplatz.", True, s),
        tf("Das Wattenmeer ist arm an Nährstoffen.", False, s),
        tf("Seehunde ziehen auf den Sandbänken ihre Jungtiere auf.", True, s),
        mc("Wie oft am Tag wird das Watt überflutet?", "zweimal", ["einmal", "gar nicht", "dreimal"], s),
        mc("Was passiert im Watt bei Ebbe?", "Das Meer fließt ab und der Meeresboden fällt trocken.", ["Das Watt wird besonders tief überflutet.", "Das Wasser friert zu.", "Das Watt verschwindet für immer."], s),
        mc("Warum ist das Wattenmeer ein wichtiger Futterplatz?", "Im und auf dem Boden leben Millionen Algen, Würmer, Muscheln und Schnecken.", ["Dort wachsen große Obstbäume.", "Dort gibt es viele Restaurants.", "Dort liegt das ganze Jahr Schnee."], s),
        mc("Warum nennt man das Wattenmeer eine Kinderstube?", "Fische, Garnelen und andere Tiere ziehen dort geschützt ihren Nachwuchs auf.", ["Dort gibt es viele Kindergärten.", "Dort spielen Kinder am Strand.", "Dort werden Boote gebaut."], s),
        mc("Wo sammeln sich im Frühjahr und Herbst Millionen Zugvögel?", "im Watt", ["in der Wüste", "im Hochgebirge", "in der Stadt"], s),
        mc("Was zeigt der Wattwurm durch seine Kothäufchen?", "Er frisst sich durch den Schlick.", ["Er baut Burgen aus Sand.", "Er sucht Wasser.", "Er will Vögel anlocken."], s),
        mc("Warum ist jede Störung im Watt gefährlich?", "Die Tiere sind angepasst und spezialisiert, deshalb gefährdet jede Störung ihre Lebensbedingungen.", ["Weil Störungen das Wasser süßer machen.", "Weil der Mond dann stärker zieht.", "Weil sonst die Gezeiten ausfallen."], s),
        luecke("Ergänze den Text über den Lebensraum Watt.",
               "Bei {{Ebbe}} fällt das Watt trocken, bei {{Flut}} wird es überflutet. Das geschieht {{zweimal}} am Tag. Das Wattenmeer ist reich an {{Nährstoffen}}. Viele Fische ziehen hier ihren {{Nachwuchs}} auf.",
               s, extra=["Sturm", "Eis"]),
        luecke("Ergänze: Warum ist das Wattenmeer wichtig?",
               "Das Watt ist {{Futterplatz}}, {{Kinderstube}} für Fische und Brut- und {{Rastplatz}} für Vögel. Millionen {{Zugvögel}} machen hier im Frühjahr und Herbst Halt.",
               s, extra=["Parkplatz", "Spielplatz"]),
        kurz("Welche fleischige Salzpflanze wächst in der Salzwiese und hält den Schlick fest?", ["Queller"], s, info="Auch der Strandflieder verträgt Salzwasser."),
        frei("Beschreibe den Lebensraum Watt in drei Sätzen.",
             "Das Watt wird zweimal am Tag überflutet und fällt bei Ebbe trocken. Hier leben Garnelen, Jungfische, Muscheln und Würmer, die sich an den Wechsel angepasst haben. Vögel finden viel Nahrung, und Seehunde ruhen auf den Sandbänken.",
             ["Wechsel von Überflutung und Trockenfallen genannt", "Tiere und Pflanzen genannt (zum Beispiel Wattwurm, Muscheln, Garnelen, Queller)", "Bedeutung als Futterplatz, Kinderstube oder Rastplatz erklärt"], 3, s),
    ]
    # ------------------------------------------------------------------ B Wer lebt wo?
    s = "B – Wer lebt wo? Meer, Watt und Salzwiese"
    A += [
        zuordnen("Wo kommt das im Lebensraum Watt vor? (Meer, Watt oder Salzwiese)",
                 [("Brutplätze der Vögel", "Salzwiese"), ("Rastplatz der Seehunde", "Meer"), ("Lebensraum der Garnelen und Jungfische", "Watt"), ("Nahrungsgebiet der Schwimm- und Tauchvögel", "Meer"),
                  ("Lebensraum der Salzpflanzen (Queller)", "Salzwiese"), ("Wattwurm und Muscheln", "Watt")], s),
        zuordnen("Wo kommt das im Lebensraum Watt vor? (Meer, Watt oder Salzwiese)",
                 [("Austernfischer sucht Futter", "Watt"), ("Strandflieder", "Salzwiese"), ("Lebensraum der Fische", "Meer"), ("Krebstiere", "Watt"), ("Seehunde auf Sandbänken", "Meer"), ("Vögel brüten", "Salzwiese")], s),
        zuordnen("Wie oft wird die Zone überflutet?", [("Meer", "immer überflutet"), ("Watt", "zweimal täglich überflutet"), ("Salzwiese", "selten überflutet")], s),
        mc("Wo leben der Wattwurm und die Muscheln?", "im Watt", ["in der Salzwiese", "im Meer ganz weit draußen", "auf dem Deich"], s),
        mc("Wo brüten viele Vögel?", "in der Salzwiese", ["im Meer", "im Watt bei Flut", "unter Wasser"], s),
        mc("Welche Zone nennt das Arbeitsblatt als Rastplatz der Seehunde (auf Sandbänken)?", "das Meer", ["die Salzwiese", "der Deich", "die Dünen"], s),
        mc("Welche Pflanzen wachsen in der Salzwiese?", "Salzpflanzen wie Queller und Strandflieder", ["Eichen und Buchen", "Weizen und Mais", "Kakteen"], s),
        mc("Welches Tier sucht im Watt bei Ebbe sein Futter?", "der Austernfischer", ["der Uhu", "das Reh", "der Feldhase"], s),
        mc("Was sind Priele?", "Rinnen im Watt, in denen das Wasser auf- und abläuft", ["Muscheln im Watt", "Sandburgen", "Schilder im Nationalpark"], s),
        tf("Priele sind für Badende und Wattwanderer gefährlich.", True, s),
        mc("Warum ist eine Wattwanderung ohne Wattführer gefährlich?", "Die Flut kommt schnell und die Priele füllen sich zuerst.", ["Das Wasser ist dort immer eiskalt.", "Man versinkt im Watt sofort bis zum Hals.", "Bei Ebbe fließt das Wasser aus dem Meer ins Watt."], s),
        kurz("Wie heißen die Rinnen im Watt, in denen das Wasser auf- und abläuft?", ["Priele", "Prielen", "Priel"], s),
    ]
    # ------------------------------------------------------------------ C Schutz
    s = "C – Warum und wie wird das Wattenmeer geschützt?"
    A += [
        mc("Was ist ein Nationalpark?", "Ein Schutzgebiet, in dem sich die Natur weitgehend ungestört und möglichst ursprünglich entfalten kann.", ["Ein Freizeitpark mit Fahrgeschäften", "Ein Parkplatz für Touristen", "Ein Garten mit Blumenbeeten"], s),
        kurz("In welchem Jahr wurden in Deutschland drei Nationalparks zum Schutz des Wattenmeeres eingerichtet?", ["1986"], s),
        kurz("Seit welchem Jahr gelten große Gebiete des Wattenmeeres als Weltnaturerbe?", ["2009"], s),
        luecke("Ergänze den Text.", "1986 wurden in Deutschland drei {{Nationalparks}} zum Schutz des Wattenmeeres eingerichtet. Seit {{2009}} gelten große Gebiete als {{Weltnaturerbe}} der Menschheit.",
               s, extra=["1999", "Naturpark"]),
        mc("Wie viele Nationalparks schützen das deutsche Wattenmeer?", "drei", ["einer", "fünf", "zehn"], s,
           info="Das Schleswig-Holsteinische, das Hamburgische und das Niedersächsische Wattenmeer."),
        zuordnen("Ordne dem Bundesland den Nationalpark zu.", [("Schleswig-Holstein", "Schleswig-Holsteinisches Wattenmeer"), ("Hamburg", "Hamburgisches Wattenmeer"), ("Niedersachsen", "Niedersächsisches Wattenmeer")], s),
        tf("Auch Dänemark und die Niederlande schützen ihre Anteile am Wattenmeer.", True, s),
        mc("Warum wird das Wattenmeer geschützt?", "Es ist einzigartig auf der Erde und soll sich weitgehend ohne Einfluss des Menschen entwickeln.", ["Weil dort sehr viel Öl gefunden wird.", "Weil dort keine Tiere leben.", "Weil es im Sommer sehr heiß ist."], s),
        zuordnen("Welche Schutzzone ist gemeint?",
                 [("Hier gelten die strengsten Regeln. Touristen dürfen die Zone nicht oder nur auf markierten Wegen betreten.", "Ruhezone"),
                  ("Hierzu gehören die Badestrände sowie Erholungs- und Kureinrichtungen. Strandbuggies und Motorfahrzeuge sind verboten.", "Erholungszone"),
                  ("Betreten, Wattwandern und Boot fahren sind erlaubt. Brutgebiete der Vögel dürfen nicht oder nur auf markierten Wegen betreten werden.", "Zwischenzone")], s),
        mc("In welcher Zone gelten die strengsten Regeln?", "Ruhezone", ["Zwischenzone", "Erholungszone", "Badezone"], s),
        mc("In welcher Zone liegen Badestrände sowie Erholungs- und Kureinrichtungen?", "Erholungszone", ["Ruhezone", "Zwischenzone", "Brutzone"], s),
        mc("In welcher Zone sind Betreten, Wattwandern und Bootfahren erlaubt?", "Zwischenzone", ["Ruhezone", "Erholungszone", "in keiner Zone"], s),
        tf("In der Erholungszone sind Strandbuggies und Motorfahrzeuge verboten.", True, s),
        tf("In der Ruhezone dürfen Touristen überall frei herumlaufen.", False, s),
        tf("In der Ruhezone ist der Fisch- und Krabbenfang nur eingeschränkt erlaubt.", True, s),
        tf("In der Zwischenzone sind Baden, Fischerei und Jagd erlaubt.", True, s),
        tf("Im Buch steht: In der Erholungszone dürfen Häfen gebaut und Erdöl gefördert werden.", True, s),
        mc("Welche Aussage über die Zwischenzone stimmt?", "Betreten, Wattwandern und Bootfahren sind erlaubt, Brutgebiete der Vögel aber nur auf markierten Wegen.", ["Hier gelten die strengsten Regeln.", "Hier sind Strandbuggies erlaubt.", "Hier darf niemand hinein."], s),
        tf("In Schleswig-Holstein und Hamburg gibt es zwei Schutzzonen, in Niedersachsen drei.", True, s),
        mc("Welche Aussage über die Schutzzonen stimmt?", "Zone I ist die Ruhezone, Zone II die Zwischenzone und Zone III die Erholungszone.", ["Zone I ist die Erholungszone.", "Zone II ist die Ruhezone.", "Es gibt nur eine Zone."], s),
        mc("Was steht auf Hinweisschildern im Nationalpark Wattenmeer?", "Gebote und Verbote, zum Beispiel Hunde anleinen und Müll mitnehmen.", ["Die aktuellen Fußballergebnisse", "Preise für Eis", "Wettervorhersagen für Mallorca"], s),
        mc("Welche Regel kann auf einem Hinweisschild im Nationalpark stehen?", "Abstand zu Seehunden halten", ["Seehunde füttern", "Pflanzen pflücken", "Müll im Watt lassen"], s),
        mc("Was darf man im Nationalpark nicht tun?", "Pflanzen pflücken", ["Müll mitnehmen", "Hunde anleinen", "Abstand zu Seehunden halten"], s),
        tf("Das Vorland darf vom 1. April bis 31. Juli nicht betreten werden, weil in dieser Zeit die Vögel brüten und ihre Jungen aufziehen.", True, s),
        mc("Warum darf das Vorland vom 1. April bis 31. Juli nicht betreten werden?", "Es ist die Brut- und Aufzuchtzeit der Vögel. Sie sollen nicht gestört werden.", ["Dort wird gerade gebaut.", "Dort ist es im Sommer zu heiß.", "Dort liegt dann Schnee."], s),
        mc("Welche Gruppen sind oft gegen strenge Schutzbestimmungen?", ["Fischer", "Hafenbetreiber", "Landwirte"], ["Nationalpark-Ranger", "Vogelkundler"], s,
           info="Auch Industrie und Tourismus-Betriebe gehören dazu, weil die Regeln ihre Arbeit einschränken."),
        mc("Warum sind manche Menschen gegen die Schutzbestimmungen?", "Die Regeln schränken ihre Arbeit ein.", ["Sie mögen keine Tiere.", "Die Schilder sind zu bunt.", "Sie wollen das Wetter ändern."], s),
        frei("Begründe, warum man im Nationalpark Ruhezonen einrichtet.",
             "Damit die Tiere, zum Beispiel die Vögel in ihren Brutgebieten und die Seehunde, nicht gestört werden und sich die Natur möglichst ungestört entwickeln kann.",
             ["Die Tiere sollen nicht gestört werden", "Die Natur soll sich möglichst ungestört entwickeln"], 2, s),
        frei("Schreibe drei Verhaltensregeln für Touristen auf, die auf Hinweisschildern im Nationalpark stehen könnten.",
             "Hunde anleinen. Pflanzen nicht pflücken. Abstand zu Seehunden halten. (Weitere Möglichkeiten: Müll mitnehmen, auf den markierten Wegen bleiben.)",
             ["Drei sinnvolle Verhaltensregeln genannt", "Die Regeln schützen Tiere und Pflanzen"], 3, s),
        frei("Auf einem Schild steht: „Das Betreten des Vorlandes ist vom 1. April bis 31. Juli nicht gestattet.“ Erkläre, warum.",
             "Vom 1. April bis 31. Juli ist die Brut- und Aufzuchtzeit der Vögel. Sie sollen in dieser Zeit nicht gestört werden.",
             ["Brut- und Aufzuchtzeit der Vögel", "Die Vögel sollen nicht gestört werden"], 2, s),
        frei("Nenne zwei Gruppen von Menschen, die gegen die strengen Schutzbestimmungen sind, und begründe es.",
             "Zum Beispiel Fischer und Hafenbetreiber, weil die Regeln ihre Arbeit einschränken. Auch Landwirte, Industrie und Tourismus-Betriebe können dagegen sein.",
             ["Zwei Gruppen genannt (zum Beispiel Fischer, Landwirte, Industrie, Tourismus-Betriebe, Hafenbetreiber)", "Begründung: Die Regeln schränken ihre Arbeit ein"], 2, s),
    ]
    # ------------------------------------------------------------------ D Die vier Zonen
    s = "D – Die vier Zonen des Watts"
    A += [
        luecke("Beschrifte die Zeichnung. Welche Zone gehört zu welcher Nummer?",
               "(1) {{Meer}}\n(2) {{Watt}}\n(3) {{Salzwiese}}\n(4) {{Deich|Düne}}",
               s, extra=["Strand", "Insel"], bild=svg_watt_zonen(True), bildAlt="Querschnitt von der See zum Land mit den Zonen 1 bis 4",
               tipp="Je weiter weg vom Meer, desto seltener wird die Zone überflutet.",
               info="Im Buch (S. 130) heißt die vierte Zone „Düne“, im Arbeitsblatt „Deich“."),
        reihenfolge("Ordne die Zonen von der See zum Land.", ["Meer", "Watt", "Salzwiese", "Deich"], s),
        zuordnen("Wie oft wird die Zone überflutet?", [("Meer", "ständig"), ("Watt", "zweimal täglich"), ("Salzwiese", "selten"), ("Deich", "nicht")], s),
        mc("Welche Zone wird zweimal am Tag überflutet?", "Watt", ["Meer", "Salzwiese", "Deich"], s),
        mc("Welche Zone wird selten überflutet?", "Salzwiese", ["Meer", "Watt", "Deich"], s),
        mc("Welche Zone ist ständig überflutet?", "Meer", ["Watt", "Salzwiese", "Deich"], s),
        mc("Wo liegt das Watt?", "zwischen mittlerem Niedrigwasser und mittlerem Hochwasser", ["oberhalb des Deichs", "ganz tief im Meer", "zwischen Deich und Land"], s),
        mc("Was ist die Grenze zwischen Meer und Watt?", "das mittlere Niedrigwasser", ["das mittlere Hochwasser", "der Deich", "die Salzwiese"], s),
        mc("Was ist die Grenze zwischen Watt und Salzwiese?", "das mittlere Hochwasser", ["das mittlere Niedrigwasser", "der Deichfuß", "die Düne"], s),
        mc("Welche Zone schützt das Land und wird nicht überflutet?", "der Deich", ["das Meer", "das Watt", "die Salzwiese"], s, info="Im Buch steht an dieser Stelle „Düne“."),
        tf("Je weiter man vom Meer entfernt ist, desto seltener wird die Zone überflutet.", True, s),
        tf("Die Salzwiese wird häufiger überflutet als das Watt.", False, s),
        luecke("Ergänze die Zonen von der See zum Land.", "{{Meer}}, {{Watt}}, {{Salzwiese}}, {{Deich|Düne}}", s, extra=["Strand", "Marsch"]),
        luecke("Ergänze den Text zu den Zonen.", "Die Grenze zwischen Meer und Watt ist das mittlere {{Niedrigwasser}}. Die Grenze zwischen Watt und Salzwiese ist das mittlere {{Hochwasser}}. Das Watt wird {{zweimal}} täglich überflutet.",
               s, extra=["Sturmflut", "dreimal"]),
        zuordnen("Was passiert in der Zone?", [("Meer", "Nahrungsgebiet der Schwimm- und Tauchvögel"), ("Watt", "Lebensraum der Garnelen, Muscheln und Wattwürmer"), ("Salzwiese", "Brutplätze der Vögel und Salzpflanzen"), ("Deich", "schützt das Land vor Überflutung")], s),
        frei("Beschreibe eine der vier Zonen in einem Satz.",
             "Zum Beispiel: Die Salzwiese wird selten überflutet. Hier wachsen Queller und Strandflieder, und Vögel brüten. (Oder: Das Watt wird zweimal täglich überflutet und liegt zwischen mittlerem Niedrigwasser und mittlerem Hochwasser.)",
             ["Eine Zone richtig benannt", "Eine passende Eigenschaft genannt (Überflutung, Pflanzen oder Tiere)"], 2, s),
        frei("Erkläre, wie sich die vier Zonen von der See zum Land unterscheiden.",
             "Das Meer ist ständig überflutet. Das Watt wird zweimal täglich überflutet und fällt bei Ebbe trocken. Die Salzwiese wird nur selten überflutet. Der Deich schützt das Land und wird nicht überflutet. Je weiter von der See entfernt, desto seltener wird die Zone überflutet.",
             ["Meer ständig überflutet", "Watt zweimal täglich", "Salzwiese selten", "Deich nicht überflutet (schützt das Land)"], 4, s),
    ]
    return A


def _extra_schutz(s):
    """Zusätzliche Aufgaben zum Schutz (Block C): Gebote und Verbote, Zahlen, Begründungen."""
    return [
        zuordnen("Erlaubt oder verboten im Nationalpark Wattenmeer?",
                 [("Hunde anleinen", "Gebot"), ("Pflanzen pflücken", "Verbot"), ("Müll mitnehmen", "Gebot"), ("Seehunde füttern oder anfassen", "Verbot"),
                  ("Abstand zu Seehunden halten", "Gebot"), ("Müll im Watt liegen lassen", "Verbot")], s,
                 info="Gebote sagen, was man tun soll, Verbote sagen, was man nicht tun darf."),
        kurz("Wie viele Nationalparks schützen das Wattenmeer in Deutschland?", ["3", "drei"], s),
        kurz("Wie viele Schutzzonen gibt es in Niedersachsen?", ["3", "drei"], s),
        kurz("Wie viele Schutzzonen gibt es in Schleswig-Holstein und Hamburg?", ["2", "zwei"], s),
        mc("Welches Schild ist im Nationalpark sinnvoll?", "Bitte Hunde anleinen und Müll mitnehmen!", ["Hier Müll abladen erlaubt!", "Pflanzen pflücken ausdrücklich erwünscht!", "Seehunde bitte füttern!"], s),
        luecke("Ergänze die Schutzzonen.", "In der {{Ruhezone}} gelten die strengsten Regeln. In der {{Zwischenzone}} sind Wattwandern und Bootfahren erlaubt. In der {{Erholungszone}} liegen die Badestrände.",
               s, extra=["Brutzone", "Sperrzone"]),
        frei("Erkläre in zwei Sätzen, warum das Wattenmeer ein Nationalpark ist.",
             "Das Wattenmeer ist einzigartig auf der Erde und soll sich weitgehend ohne Einfluss des Menschen entwickeln. Als Nationalpark gelten besondere Schutzbestimmungen, damit Tiere und Pflanzen nicht gestört werden.",
             ["Einzigartig und möglichst ungestört genannt", "Besondere Schutzbestimmungen oder Schutz der Tiere und Pflanzen genannt"], 2, s),
    ]


def aufgaben_alle():
    A = aufgaben()
    # die zusätzlichen Schutz-Aufgaben stehen hinter Block C
    extra = _extra_schutz("C – Warum und wie wird das Wattenmeer geschützt?")
    idx = max(i for i, t in enumerate(A) if t["abschnitt"].startswith("C")) + 1
    return A[:idx] + extra + A[idx:]


def build():
    lbs = lernblatt()
    alle = aufgaben_alle()
    lebensraum = [t for t in alle if t["abschnitt"][0] in "ABD"]
    schutz = [t for t in alle if t["abschnitt"][0] == "C"]
    assert len(lebensraum) + len(schutz) == len(alle)
    # Lernblatt: 0 Lebensraum, 1 Wer lebt wo, 2 Schutz, 3 Schutzzonen, 4 vier Zonen
    p1 = pack("geografie-3a-wattenmeer-lebensraum", "Geografie Teil 3a: Wattenmeer – Lebensraum und Zonen",
              "Der Lebensraum Watt, wer wo lebt und die vier Zonen des Watts. Mit Lernblatt und vielen Übungsaufgaben.",
              [lbs[0], lbs[1], lbs[4]], lebensraum, min_aufgaben=40,
              hinweis="Die vierte Zone heißt im Buch (S. 130) „Düne“, im Arbeitsblatt „Deich“. In den Aufgaben werden beide Antworten als richtig gewertet. Bei Abweichungen zählt, was im Unterricht gelernt wurde.")
    p2 = pack("geografie-3b-wattenmeer-schutz", "Geografie Teil 3b: Wattenmeer – Schutz und Nationalpark",
              "Warum und wie das Wattenmeer geschützt wird: Nationalpark, Weltnaturerbe, die drei Schutzzonen und Regeln für Besucher. Mit Lernblatt und vielen Übungsaufgaben.",
              [lbs[2], lbs[3]], schutz, min_aufgaben=35)
    return [p1, p2]
