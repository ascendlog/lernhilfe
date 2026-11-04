"""Geografie Klasse 6: eigene Probearbeit (der Lehrer hat keine Probearbeit vorgegeben).

Alle Aufgaben sind neu, nicht aus den Übungspaketen. 48 Punkte, etwa 45 Minuten.
"""
from geo_lib import *
from geo_lib import _gaps
from geo_svg2 import svg_siel_paar

NAMEN = ["Seeseite", "Landseite", "Deichkrone", "Grasdecke", "Klei", "Sandkern", "Deichfuß", "Sturmflutwasserstand", "Hochwasser"]
PERM_C = (6, 9, 2, 4, 1, 7, 5, 3, 8)
assert sorted(PERM_C) == list(range(1, 10))

# Gezeitenkurve und Tidenkalender (neu, nicht in den Übungspaketen)
T_HW, HW, NW = 210, 3.2, 0.7
T0_KAL = 365


def punkte(t):
    """Punkte wie in der App: Lücken, Paare, frei (punkte), sonst 1 oder punkte."""
    if t["typ"] == "luecke":
        return len(_gaps(t["text"]))
    if t["typ"] == "zuordnen":
        return len(t["paare"])
    if t["typ"] == "frei":
        return t["punkte"]
    return t.get("punkte", 1)


def uhr(minuten):
    m = int(round(minuten)) % 1440
    return f"{m // 60}:{m % 60:02d} Uhr"


def teil_a():
    s = "Teil A – Nord- und Ostsee (9 Punkte)"
    return [
        luecke("Aufgabe 1: Ergänze die Bundesländer.",
               "Die Bundesländer an der Nordsee sind Schleswig-Holstein und {{Niedersachsen}}. An der Ostsee liegen Schleswig-Holstein und {{Mecklenburg-Vorpommern}}. Das Bundesland {{Schleswig-Holstein}} liegt an beiden Meeren.",
               s, extra=["Bayern", "Sachsen"]),
        zuordnen("Aufgabe 2: Welche Eigenschaft passt zu welchem Meer? Ordne zu.",
                 [("im Durchschnitt etwa 52 m tief", "Ostsee"), ("etwa 3,5 % Salz", "Nordsee"), ("kaum Gezeiten", "Ostsee"), ("Watt und Dünen", "Nordsee")], s),
        luecke("Aufgabe 3: Ergänze die Inselgruppen.",
               "Sylt gehört zu den {{nordfriesischen}} Inseln und Borkum zu den {{ostfriesischen}} Inseln.",
               s, extra=["westfriesischen", "ostseeischen"]),
    ]


def teil_b():
    s = "Teil B – Gezeiten (15 Punkte)"
    out = []
    out.append(luecke("Aufgabe 4: Beschrifte die Zeichnung der Gezeiten. Welches Wort gehört zu welcher Nummer?",
                      "(1) {{Mond}}\n(2) {{Anziehungskraft|Anziehungskraft des Mondes}}\n(3) {{Erde}}\n(4) {{Flut}}\n(5) {{Ebbe}}\n(6) {{Fliehkraft|Fliehkraft der Erde}}",
                      s, extra=["Sonne", "Gezeit"], bild=svg_gezeiten(True, mond_rechts=False),
                      bildAlt="Die Erde mit zwei Wasserbergen und dem Mond links daneben, mit den Nummern 1 bis 6"))
    out.append(frei("Aufgabe 5: Erkläre, warum es an der Küste zweimal am Tag Flut gibt.",
                    "Der Mond zieht mit seiner Anziehungskraft das Wasser auf der zugewandten Seite der Erde an, dort entsteht ein Wasserberg. Auf der abgewandten Seite drückt die Fliehkraft das Wasser nach außen, dort entsteht ein zweiter Wasserberg. Die Erde dreht sich unter den beiden Wasserbergen hindurch, deshalb gibt es zweimal am Tag Flut und dazwischen Ebbe.",
                    ["Anziehungskraft des Mondes oder Wasserberg auf der zugewandten Seite", "Fliehkraft oder zweiter Wasserberg auf der abgewandten Seite", "Erde dreht sich unter den Wasserbergen hindurch (zweimal Flut, zweimal Ebbe)"],
                    2, s))
    # Gezeitenkurve
    bild = svg_kurve(T_HW, HW, NW)
    alt = "Gezeitenkurve eines Tages (0 bis 24 Uhr), waagerecht die Uhrzeit, senkrecht der Wasserstand in Metern."
    nw_nach = T_HW + 745 / 2
    a = int(round(T_HW / 30.0)) * 30
    assert uhr(a) == "3:30 Uhr"
    out.append(mc("Aufgabe 6a: Lies die Gezeitenkurve ab. Um wie viel Uhr ist das erste Hochwasser des Tages? (Auf eine halbe Stunde genau.)",
                  uhr(a), [uhr(a + 360), uhr(a + 180), uhr(a + 540)], s, bild=bild, bildAlt=alt))
    th = round(HW - NW, 1)
    assert th == 2.5
    t = kurz("Aufgabe 6b: Berechne den Tidenhub an diesem Tag. Lies erst Hochwasser und Niedrigwasser ab. (2 Punkte)",
             [de(th), str(th)], s, einheit="m", bild=bild, bildAlt=alt,
             info=f"Tidenhub = Hochwasser − Niedrigwasser = {de(HW)} m − {de(NW)} m = {de(th)} m.")
    t["punkte"] = 2
    out.append(t)
    sieben = 7 * 60
    assert kurve_h(sieben + 1, T_HW, HW, NW) < kurve_h(sieben - 1, T_HW, HW, NW)
    out.append(mc("Aufgabe 6c: Was ist um 7 Uhr: Ebbe oder Flut?", "Ebbe", ["Flut", "Hochwasser", "Niedrigwasser"], s, bild=bild, bildAlt=alt))
    # Tidenkalender
    tab, svg, alt_k = kalender_svg(T0_KAL)
    alt_k = "Tidenkalender (Uhrzeiten). " + alt_k
    hw1 = [d[0] for d in tab]
    out.append(kurz("Aufgabe 7a: Lies den Tidenkalender ab. Wann ist am 2. Tag das erste Hochwasser? (Schreibe die Uhrzeit so: 04:05)",
                    [hhmm(hw1[1]), hhmm(hw1[1]).lstrip('0')], s, bild=svg, bildAlt=alt_k))
    assert hw1[1] - hw1[0] == 50
    out.append(frei("Aufgabe 7b: Im Tidenkalender wird das Hochwasser jeden Tag später. Erkläre, warum das so ist.",
                    "Der Mond umrundet die Erde in etwa 28 Tagen. Wenn sich die Erde nach 24 Stunden einmal gedreht hat, ist der Mond ein Stück weitergewandert. Die Erde braucht noch etwa 50 Minuten, bis sie ihn eingeholt hat. Deshalb verschieben sich die Gezeiten jeden Tag um etwa 50 Minuten.",
                    ["Mond wandert auf seiner Bahn weiter", "Erde braucht etwa 50 Minuten länger, bis sie den Mond eingeholt hat"], 2, s, bild=svg, bildAlt=alt_k))
    return out


def teil_c():
    s = "Teil C – Wattenmeer (12 Punkte)"
    return [
        frei("Aufgabe 8: Erkläre, warum das Wattenmeer ein wichtiger Lebensraum ist. Nenne drei Aufgaben des Watts für Tiere.",
             "Das Watt ist reich an Nährstoffen und deshalb ein Futterplatz für viele Tiere. Es ist eine Kinderstube für Fische, Garnelen und Seehunde. Außerdem ist es ein Brut- und Rastplatz für Zugvögel.",
             ["Futterplatz (viele Nährstoffe)", "Kinderstube für Fische oder andere Jungtiere", "Brut- oder Rastplatz für Vögel"], 3, s),
        zuordnen("Aufgabe 9: Welche Zone des Watts ist gemeint? Ordne zu.",
                 [("wird zweimal am Tag überflutet", "Watt"), ("wird selten überflutet, Queller wächst hier", "Salzwiese"), ("ist ständig überflutet", "Meer"), ("schützt das Land und wird nicht überflutet", "Deich")], s,
                 info="Im Buch steht an der Stelle des Deichs „Düne“. Das gilt hier auch."),
        frei("Aufgabe 10: Das Wattenmeer wird geschützt. Nenne einen Grund und zwei Schutzmaßnahmen.",
             "Grund: Das Watt ist einzigartig auf der Erde und die Tiere sind angepasst, jede Störung gefährdet sie. Schutzmaßnahmen: Es ist Nationalpark (seit 1986) und Weltnaturerbe (seit 2009), außerdem gibt es Schutzzonen und Hinweisschilder.",
             ["Ein Grund genannt (einzigartig, empfindlich, Tiere nicht stören)", "Erste Schutzmaßnahme genannt", "Zweite Schutzmaßnahme genannt (zum Beispiel Nationalpark, Weltnaturerbe, Schutzzonen, Schilder)"], 3, s),
        luecke("Aufgabe 11: Ergänze die Schutzzonen.",
               "Die Zone mit den strengsten Regeln heißt {{Ruhezone}}. Zur {{Erholungszone}} gehören die Badestrände.",
               s, extra=["Brutzone", "Zwischenzone"]),
    ]


def teil_d():
    s = "Teil D – Küstenschutz (12 Punkte)"
    out = []
    img = svg_deich(True, False, PERM_C)
    gefragt = ["Landseite", "Deichkrone", "Grasdecke", "Sandkern", "Deichfuß"]
    paare = sorted(((f"Nummer {PERM_C[NAMEN.index(n)]}", n) for n in gefragt), key=lambda p: int(p[0].split()[1]))
    out.append(zuordnen("Aufgabe 12: Beschrifte den Deich. Hier liegt das Meer rechts. Schreibe zu jeder genannten Nummer das passende Wort.",
                        paare, s, extra=["Düne", "Priel"], bild=img,
                        bildAlt="Querschnitt durch einen Deich, das Meer liegt rechts, das Land links, mit den Nummern 1 bis 9. Gefragt sind fünf der neun Nummern."))
    out.append(frei("Aufgabe 13: Erkläre, welche Aufgabe die Steine am Deichfuß und die Grasdecke haben.",
                    "Am Deichfuß treffen die Wellen zuerst auf den Deich. Die Steine verhindern, dass das Wasser den Fuß aushöhlt und wegspült. Die Wurzeln der Grasdecke halten den Boden fest, sodass der Deich nicht von Wellen, Wind und Regen abgetragen wird.",
                    ["Steine schützen den Deichfuß vor dem Aushöhlen", "Gras hält mit den Wurzeln den Boden fest"], 2, s))
    out.append(luecke("Aufgabe 14: Ergänze, wie eine Düne wächst.",
                      "Der Wind weht Sand vom Strand landeinwärts. Der {{Strandhafer}} hält den Sand mit seinen {{Wurzeln}} fest. Wird er mit Sand zugeschüttet, wächst er oben wieder {{heraus}}.",
                      s, extra=["Muscheln", "hinein"]))
    out.append(frei("Aufgabe 15: Schau dir die Zeichnungen an. Welche Zeichnung zeigt Flut? Beschreibe, was am Sieltor passiert, und erkläre warum.",
                    "Zeichnung 2 zeigt Flut. Das Meerwasser steht hoch und drückt das Tor zu. So kommt kein Salzwasser ins Land. (Zeichnung 1 zeigt Ebbe: Das Tor ist offen und das Wasser aus dem Land fließt ins Meer ab.)",
                    ["Flut richtig zugeordnet (Zeichnung 2) und Tor geschlossen", "Erklärt, dass das Meerwasser das Tor zudrückt und kein Salzwasser ins Land kommt"], 2, s,
                    bild=svg_siel_paar(True, ("Zeichnung 1", "Zeichnung 2")),
                    bildAlt="Zwei vereinfachte Zeichnungen eines Sieltors im Deich, Zeichnung 1 links und Zeichnung 2 rechts"))
    return out


def lernblatt():
    return [
        lb("So läuft die Probearbeit",
           "Das ist eine **eigene Probearbeit**. Dein Lehrer hat keine vorgegeben, deshalb wurde sie nach den 13 Punkten des Wissenschecks selbst zusammengestellt. Die echte Arbeit kann anders aufgebaut sein.\n"
           "- **Zeit**: etwa 45 Minuten.\n"
           "- **Punkte**: 48 Punkte in vier Teilen: A Nord- und Ostsee (9), B Gezeiten (15), C Wattenmeer (12), D Küstenschutz (12). Die Punkte stehen über jedem Teil.\n"
           "- **Hilfsmittel**: keine. Schlage nichts nach, lies das Lernblatt erst danach.\n"
           "- Die Aufgaben sind neu. Sie stehen nicht in den Übungspaketen.\n"
           "- Faustregel zur Selbsteinschätzung: Ab etwa 38 Punkten (80 %) sitzt der Stoff gut. Welche Note es für welche Punktzahl gibt, bestimmt dein Lehrer.",
           merke="Erst alles ohne Hilfe lösen, dann vergleichen. Wo Punkte fehlen, geh in das passende Übungspaket zurück."),
        lb("Was die Arbeitsaufträge verlangen",
           "- **Nenne**: kurz aufzählen, ganze Sätze sind nicht nötig.\n"
           "- **Beschrifte** oder **ordne zu**: Wörter oder Nummern richtig eintragen.\n"
           "- **Lies ab**: Werte aus der Kurve oder dem Tidenkalender nehmen. Bei der Kurve genügt die Uhrzeit auf eine halbe Stunde genau.\n"
           "- **Berechne**: rechnen und die Einheit schreiben, zum Beispiel Tidenhub = Hochwasser − Niedrigwasser.\n"
           "- **Erkläre** und **begründe**: einen Zusammenhang mit „weil“ oder „deshalb“ darlegen.",
           merke="Bei Aufgaben mit 2 oder 3 Punkten wollen die Lehrer meist 2 oder 3 Gedanken sehen."),
    ]


def build():
    A = teil_a() + teil_b() + teil_c() + teil_d()
    summen = {}
    for t in A:
        k = t["abschnitt"][:6]
        summen[k] = summen.get(k, 0) + punkte(t)
    assert summen == {"Teil A": 9, "Teil B": 15, "Teil C": 12, "Teil D": 12}, summen
    assert sum(summen.values()) == 48
    # Die Überschriften nennen die Punkte; sie müssen zur Summe passen
    for t in A:
        k = t["abschnitt"][:6]
        assert f"({summen[k]} Punkte)" in t["abschnitt"], t["abschnitt"]
    p = pack("geografie-probearbeit", "Geografie Klasse 6: Probearbeit (Nord- und Ostsee, Gezeiten, Wattenmeer, Küstenschutz)",
                "Eigene Probearbeit mit 48 Punkten in vier Teilen, etwa 45 Minuten. Alle Aufgaben sind neu. Gut für die Probearbeit-Funktion.",
                lernblatt(), A,
                hinweis="Das ist eine eigene Probearbeit, nicht die des Lehrers (es gibt keine). Aufbau, Punkte und Zeit sind selbst festgelegt. Tidenkalender und Wasserstände sind erfunden. Die vierte Zone des Watts heißt im Buch „Düne“, im Arbeitsblatt „Deich“.")
    p["ueben"] = False   # Probearbeit: nur proben wie in der Schule, kein Übungsmodus
    return p
