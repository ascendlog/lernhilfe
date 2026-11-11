"""Geschichte Klasse 6, Teil 2: Zeitrechnung und Kalender (2a), Epochen und Zeitstrahl (2b).

Alle Jahreszahlen, Abstände und Maßstäbe werden im Code berechnet und mit assert geprüft.
Alle Beispiele sind sachlich gesichert oder erfunden, keine echten Personendaten.
"""
from gesch_lib import *                       # noqa: F401,F403
from gesch_lib import _svg, _label, _num, _arrow   # noqa: F401
from gesch_lib import jahr, spanne, epoche, EPOCHEN, nachlesen, svg_epochen, svg_zeitstrahl_punkte, pack

GRENZEN = (-3000, -1000, 500, 1500)


# ------------------------------------------------------------------ Helfer: Schreibweisen und Rechnungen

def jahr_antw(y):
    """Akzeptierte Schreibweisen für ein Jahr (mit und ohne v. Chr. / n. Chr.)."""
    a = abs(y)
    if y < 0:
        return [f"{a} v. Chr.", f"{a} v.Chr.", f"{a} v. Chr", f"{a} vor Christus", f"{a} vor Christi Geburt",
                f"{a} v. u. Z.", f"{a} v.u.Z.", f"-{a}", f"−{a}", f"{a}"]
    return [f"{a} n. Chr.", f"{a} n.Chr.", f"{a} n. Chr", f"{a} nach Christus", f"{a} n. u. Z.", f"{a}"]


def zahl_antw(n, einheit="Jahre", ca=False):
    """Zahl mit und ohne Einheit, bei großen Zahlen auch mit Tausenderpunkt. ca=True: zusätzlich mit „ca.“, „etwa“, „ungefähr“."""
    if isinstance(n, float) and n != int(n):
        s = f"{n:.1f}".replace(".", ",")
        out = [s, s.replace(",", "."), f"{s} {einheit}", f"{s.replace(',', '.')} {einheit}"]
        basis = [s, s.replace(",", ".")]
    else:
        n = int(n)
        out = [str(n), f"{n} {einheit}"]
        basis = [str(n)]
        if n >= 1000:
            p = f"{n:,}".replace(",", ".")
            out += [p, f"{p} {einheit}"]
            basis.append(p)
    if ca:
        for w in ("ca.", "etwa", "ungefähr"):
            for b in basis:
                out += [f"{w} {b}", f"{w} {b} {einheit}"]
    return out


def jh(y):
    """Jahrhundert eines Jahres (Schulregel: Zahl ohne die letzten zwei Stellen plus 1). Volle Hunderter vermeiden."""
    assert y > 0 and y % 100 != 0, y
    return y // 100 + 1


def jh_antw(n):
    return [str(n), f"{n}.", f"{n}. Jahrhundert", f"das {n}. Jahrhundert", f"im {n}. Jahrhundert", f"{n}. Jahrhundert n. Chr.",
            f"{n}. Jh.", f"{n}. Jh"]


def jh_range(n):
    """Jahre des n-ten Jahrhunderts n. Chr. (1. Jh.: 1 bis 99, wie im Buch)."""
    return (1 if n == 1 else (n - 1) * 100, n * 100 - 1)


ARTIKEL = {"Ur- und Frühgeschichte": "die", "Altertum": "das", "Antike": "die", "Mittelalter": "das", "Neuzeit": "die"}
ZW = "(Zusatzwissen, nicht aus Heft oder Buch)"


def ep_antw(name, kuerzel=True):
    """Akzeptierte Antworten für eine Epoche: Name mit und ohne richtigen Artikel. kuerzel=False bei Fragen nach der Abkürzung selbst."""
    kurz_ = {"Mittelalter": ["MA"], "Neuzeit": ["NZ"]}.get(name, []) if kuerzel else []
    return [name, f"{ARTIKEL[name]} {name}"] + kurz_


def zeitraum(i):
    """Epoche i (0 bis 4) als Text: '1000 v. Chr. bis 500 n. Chr.'"""
    n, a, b = EPOCHEN[i]
    if a is None:
        return f"bis {abs(b)} v. Chr."
    if b is None:
        return f"ab {a} n. Chr."
    sa = f"{abs(a)} v. Chr." if a < 0 else f"{a} n. Chr."
    sb = f"{abs(b)} v. Chr." if b < 0 else f"{b} n. Chr."
    if (a < 0) == (b < 0):
        sa = str(abs(a))
        return f"{sa} bis {sb}"
    return f"{sa} bis {sb}"


def ep_jahr(y):
    """Epoche eines Jahres, nur Jahre mit genug Abstand zu einer Epochengrenze."""
    assert all(abs(y - g) >= 50 for g in GRENZEN), f"Jahr {y} liegt zu nah an einer Grenze"
    return epoche(y)


def _t(x, y, text, size=16, weight="bold", anchor="middle", fill="#222"):
    """Beschriftung mit weißem Rand."""
    return (f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" '
            f'stroke="#fff" stroke-width="4" paint-order="stroke" stroke-linejoin="round">{text}</text>')


# ------------------------------------------------------------------ Zeichnungen

def svg_jahre():
    """Balken: Mondjahr (12 Monate), Sonnenjahr, Schaltjahr. Tage im Code berechnet."""
    MONAT = 29.5
    mond = 12 * MONAT
    assert mond == 354 and 365 - 354 == 11 and 366 - 365 == 1
    x0, s = 175, 1.3
    X = lambda d: x0 + d * s
    g = []
    # Mondjahr: 12 Monate
    y = 30
    for m in range(12):
        g.append(f'<rect x="{X(m * MONAT):.1f}" y="{y}" width="{MONAT * s:.1f}" height="40" fill="#8fb8d8" stroke="#33597a" stroke-width="1.5"/>')
        g.append(_t(round(X(m * MONAT + MONAT / 2), 1), y + 26, str(m + 1), size=15, weight="bold"))
    g.append(_t(x0 - 10, y + 26, "Mondjahr", size=17, anchor="end"))
    g.append(_t(round(X(354) + 10, 1), y + 26, "354 Tage", size=17, anchor="start"))
    # Sonnenjahr: 354 + 11
    y = 100
    g.append(f'<rect x="{x0}" y="{y}" width="{354 * s:.1f}" height="40" fill="#e8c27a" stroke="#7a5a1a" stroke-width="1.5"/>')
    g.append(f'<rect x="{X(354):.1f}" y="{y}" width="{11 * s:.1f}" height="40" fill="#e2701a" stroke="#7a3a00" stroke-width="1.5"/>')
    g.append(_t(x0 - 10, y + 26, "Sonnenjahr", size=17, anchor="end"))
    g.append(_t(round(X(365) + 10, 1), y + 26, "365 Tage", size=17, anchor="start"))
    # Schaltjahr: 365 + 1
    y = 170
    g.append(f'<rect x="{x0}" y="{y}" width="{365 * s:.1f}" height="40" fill="#9fc5a0" stroke="#2f6a3a" stroke-width="1.5"/>')
    g.append(f'<rect x="{X(365):.1f}" y="{y}" width="{1 * s + 3:.1f}" height="40" fill="#1f7a3a" stroke="#0f4a1f" stroke-width="1.5"/>')
    g.append(_t(x0 - 10, y + 26, "Schaltjahr", size=17, anchor="end"))
    g.append(_t(round(X(366) + 12, 1), y + 26, "366 Tage", size=17, anchor="start"))
    # Legende
    g.append(f'<rect x="{x0}" y="236" width="18" height="18" fill="#e2701a" stroke="#7a3a00"/>')
    g.append(_t(x0 + 28, 251, "11 Tage mehr als das Mondjahr", size=16, weight="normal", anchor="start"))
    g.append(f'<rect x="{x0}" y="264" width="18" height="18" fill="#1f7a3a" stroke="#0f4a1f"/>')
    g.append(_t(x0 + 28, 279, "1 Tag mehr als im normalen Sonnenjahr", size=16, weight="normal", anchor="start"))
    g.append(_t(x0 - 10, 20, "Die Zahlen 1 bis 12 sind die Monate (je 29,5 Tage).", size=15, weight="normal", anchor="start"))
    return _svg(760, 296, ''.join(g))


def svg_jahrhunderte():
    """Drei Jahrhunderte nebeneinander, das 13. hervorgehoben."""
    g = []
    for i, n in enumerate((12, 13, 14)):
        a, b = jh_range(n)
        assert (a, b) == ((n - 1) * 100, n * 100 - 1)
        x = 20 + i * 250
        hell = n == 13
        g.append(f'<rect x="{x}" y="30" width="220" height="86" rx="8" fill="{"#ffe3b0" if hell else "#f1f1f1"}" stroke="{"#e2701a" if hell else "#888"}" stroke-width="{3 if hell else 1.5}"/>')
        g.append(_t(x + 110, 64, f"{n}. Jahrhundert", size=18))
        g.append(_t(x + 110, 98, f"{a} bis {b}", size=18, weight="normal"))
        if i < 2:
            g.append(_arrow(x + 224, 73, x + 246, 73))
    g.append(_t(380, 152, "1200 bis 1299: Die Zahl beginnt mit „12“.", size=17, weight="normal"))
    g.append(_t(380, 180, "12 + 1 = 13, also das 13. Jahrhundert", size=17))
    return _svg(760, 200, ''.join(g))


def svg_lineal(von=-100, bis=50, marke=None, pro_cm=10):
    """Lineal mit cm-Strichen und den Jahren (10 Jahre = 1 cm). marke: ein Jahr, das markiert wird."""
    cm_gesamt = spanne(von, bis) / pro_cm
    assert cm_gesamt == int(cm_gesamt)
    n = int(cm_gesamt)
    x0, pcm = 60, 42
    X = lambda cm: x0 + cm * pcm
    ay = 110
    g = [f'<line x1="{x0 - 20}" y1="{ay}" x2="{X(n) + 20}" y2="{ay}" stroke="#222" stroke-width="3"/>']
    for c in range(n + 1):
        gross = c % 5 == 0
        g.append(f'<line x1="{X(c)}" y1="{ay - (12 if gross else 8)}" x2="{X(c)}" y2="{ay + (12 if gross else 8)}" stroke="#222" stroke-width="{2.4 if gross else 1.4}"/>')
        g.append(_t(X(c), ay + 30, str(c), size=15, weight="normal"))
    for c in range(0, n + 1, 5):
        jj = von + c * pro_cm
        txt = "Christi Geburt" if jj == 0 else (f"{abs(jj)} v. Chr." if jj < 0 else f"{jj} n. Chr.")
        g.append(_t(X(c), ay + 58, txt, size=15))
    g.append(_t(x0 - 10, ay + 30, "cm", size=15, weight="normal", anchor="end"))
    if marke is not None:
        c = (marke - von) / pro_cm
        g.append(f'<line x1="{X(c):.1f}" y1="{ay}" x2="{X(c):.1f}" y2="{ay - 48}" stroke="#e2701a" stroke-width="2.5"/>')
        g.append(f'<circle cx="{X(c):.1f}" cy="{ay}" r="6" fill="#e2701a"/>')
        txt = f"{abs(marke)} v. Chr. = {str(round(c, 1)).replace('.', ',')} cm" if marke < 0 else f"{marke} n. Chr. = {str(round(c, 1)).replace('.', ',')} cm"
        g.append(_t(round(X(c), 1), ay - 56, txt, size=16))
    return _svg(760, 190, ''.join(g))


# ================================================================== Paket 2a: Zeit messen, Kalender und Zeitrechnung

L1 = "Warum teilt man die Zeit ein?"
L2 = "Zeit messen: vom Sonnenstand zur Uhr"
L3 = "Mondphasen, Monate und Jahre"
L4 = "Unsere Zeitrechnung: vor und nach Christi Geburt"
L5 = "Jahre vergleichen und Abstände berechnen"
L6 = "Jahrhunderte bestimmen"
L7 = "Andere Kalender und ihr Beginn"


def lernblatt_a():
    return [
        lb(L1,
           "Wie lange etwas dauert, schätzt du nach Gefühl. Aber das Gefühl täuscht: Manchmal vergeht die Zeit „wie im Flug“, manchmal scheint sie stehen zu bleiben. "
           "Darum haben Menschen schon früh begonnen, die Zeit zu **messen** und einzuteilen.\n"
           "Eine **Zeiteinteilung** hilft dir, dich zeitlich zu **orientieren**. Du kannst dann sagen, was früher war und was später, und wie lange etwas her ist. "
           "Ohne Uhr und Kalender wäre es schwer, sich mit jemandem zu verabreden.\n"
           "Für die Geschichte ist das besonders wichtig: Nur mit einer Zeiteinteilung kannst du Ereignisse in eine Reihenfolge bringen.",
           merke="Das Zeitgefühl ist unsicher. Deshalb misst man die Zeit und teilt sie ein, um sich zeitlich zu orientieren."),
        lb(L2,
           "Am Anfang hielten sich die Menschen an den Wechsel von **Tag und Nacht**. Das ist aber nur eine grobe Orientierung, denn der Tag ist im Lauf des Jahres mal länger und mal kürzer.\n"
           "Danach teilte man den Tag selbst ein. Immer feinere Geräte entstanden:\n"
           "- **Sonnenuhr**: Sie zeigt die Tageszeit mit dem Schatten der Sonne an. Eine griechische Sonnenuhr stammt aus dem 3. Jahrhundert v. Chr.\n"
           "- **Sanduhr**: Sand rieselt durch eine enge Stelle. Sie misst eine feste Zeitspanne.\n"
           "- **mechanische Uhr**: In Deutschland gab es sie um 1400.\n"
           "- **Uhr mit Zifferblatt**: Die Uhr, wie du sie kennst, laut Buch im 20. Jahrhundert.\n"
           "Heute messen wir Zeitunterschiede, die ein Mensch gar nicht mehr wahrnehmen kann.",
           merke="Von Tag und Nacht über Sonnenuhr, Sanduhr und mechanische Uhr bis zur Uhr mit Zifferblatt: Die Messung der Zeit wurde immer genauer."),
        lb(L3,
           "Lange Zeit war der **Mond** das wichtigste Hilfsmittel, denn man sieht seine **Mondphasen** (sein wechselndes Aussehen) mit bloßem Auge. "
           "Von einem Vollmond bis zum nächsten vergehen etwa **29,5 Tage**. Daraus entstand der **Monat**.\n"
           "Zwölf Monate ergeben ein **Mondjahr**: 12 × 29,5 = **354 Tage**. Die Jahreszeiten richten sich aber nach dem Lauf der Erde um die Sonne. "
           "Ein **Sonnenjahr** dauert etwa **365 Tage**, also 11 Tage länger als das Mondjahr. Darum passt ein reines Mondjahr nicht zu den Jahreszeiten.\n"
           "Auch 365 Tage sind nicht ganz genau. Deshalb gibt es alle vier Jahre ein **Schaltjahr** mit **366 Tagen**. (Zusatzwissen: Der zusätzliche Tag ist der 29. Februar.)",
           merke="Monat = etwa 29,5 Tage. Mondjahr = 354 Tage. Sonnenjahr = etwa 365 Tage. Schaltjahr = 366 Tage.",
           bild=svg_jahre(),
           bildAlt="Drei Balken: Das Mondjahr besteht aus zwölf Monaten und hat 354 Tage. Das Sonnenjahr ist 11 Tage länger (365 Tage). Das Schaltjahr hat einen weiteren Tag (366 Tage)."),
        lb(L4,
           "Wir zählen die Jahre ab der **Geburt Christi**. Das ist der **Nullpunkt** unserer Zeitrechnung.\n"
           "- Davor wird **rückwärts** gezählt. Dahinter schreibt man **v. Chr.** (vor Christus).\n"
           "- Danach wird **vorwärts** gezählt. Dahinter schreibt man **n. Chr.** (nach Christus).\n"
           "Es gibt auch andere Kürzel mit derselben Bedeutung: **v. u. Z.** (vor unserer Zeitrechnung) und **n. u. Z.** (nach unserer Zeitrechnung).\n"
           "Auf einem **Zeitstrahl** liegt das Frühere links und das Spätere rechts. Bei „v. Chr.“ gilt: Je größer die Zahl, desto weiter liegt das Jahr zurück. Beispiel: 753 v. Chr. liegt früher als 44 v. Chr.\n"
           "Streng genommen gibt es kein Jahr 0, auf 1 v. Chr. folgt gleich 1 n. Chr. Bei Abständen über Christi Geburt hinweg rechnest du in der Schule trotzdem einfach zusammen.",
           merke="Nullpunkt = Geburt Christi. Davor v. Chr. (rückwärts gezählt), danach n. Chr. Bei v. Chr. gilt: größere Zahl = früher.",
           bild=svg_zeitstrahl_punkte([], von=-100, bis=50),
           bildAlt="Zeitstrahl von 100 v. Chr. bis 50 n. Chr. Links liegen die Jahre vor Christi Geburt, in der Mitte steht Christi Geburt, rechts die Jahre danach."),
        lb(L5,
           "**Welches Jahr ist früher?**\n"
           "- Beide Jahre v. Chr.: Das Jahr mit der größeren Zahl ist früher (300 v. Chr. liegt vor 200 v. Chr.).\n"
           "- Beide Jahre n. Chr.: Das Jahr mit der kleineren Zahl ist früher (800 n. Chr. liegt vor 1450 n. Chr.).\n"
           "- Ein Jahr v. Chr. liegt immer vor einem Jahr n. Chr.\n"
           "**Wie viele Jahre liegen dazwischen?**\n"
           "- Beide Jahre auf **derselben** Seite von Christi Geburt: Du **ziehst** die Zahlen **ab**. Beispiel: 753 − 44 = 709 Jahre zwischen 753 v. Chr. und 44 v. Chr.\n"
           "- Ein Jahr davor, eins danach: Du **zählst zusammen**. Beispiel: 100 v. Chr. bis 50 n. Chr. sind 100 + 50 = 150 Jahre.\n"
           "Streng genommen gibt es kein Jahr 0. In der Schule rechnest du trotzdem so (ohne Jahr 0). In Aufgaben steht dann „Rechne wie in der Schule“.",
           merke="Gleiche Seite: abziehen. Über Christi Geburt hinweg: zusammenzählen."),
        lb(L6,
           "Ein **Jahrhundert** hat 100 Jahre. Das **1. Jahrhundert** umfasst die Jahre unter 100, also 1 bis 99. Das 2. Jahrhundert beginnt mit 100. "
           "Das **13. Jahrhundert** umfasst 1200 bis 1299, also alle Jahre, die mit „12“ beginnen.\n"
           "So findest du das Jahrhundert eines Jahres: Streiche die letzten **zwei** Stellen und zähle **1 dazu**. Beispiel: 1969 → 19 + 1 = **20.** Jahrhundert. Beispiel: 44 → 0 + 1 = **1.** Jahrhundert.\n"
           "Auch vor Christi Geburt gibt es Jahrhunderte, sie werden genauso nummeriert. 44 v. Chr. liegt im 1. Jahrhundert v. Chr., 753 v. Chr. im 8. Jahrhundert v. Chr. (Zusatzwissen: Man zählt von Christi Geburt aus rückwärts. Das 1. Jahrhundert v. Chr. sind die Jahre 100 bis 1 v. Chr. Bei vollen Hundertern wie 100 v. Chr. gibt die Rechenregel das falsche Jahrhundert. Solche Jahre kommen in den Aufgaben nicht vor.)",
           merke="13. Jahrhundert = 1200 bis 1299. Jahrhundert = Jahreszahl ohne die letzten zwei Stellen, plus 1.",
           bild=svg_jahrhunderte(),
           bildAlt="Drei Kästchen: 12. Jahrhundert (1100 bis 1199), 13. Jahrhundert (1200 bis 1299, hervorgehoben) und 14. Jahrhundert (1300 bis 1399). Darunter die Rechnung 12 plus 1 gleich 13."),
        lb(L7,
           "Nicht alle Völker zählen die Jahre ab der Geburt Christi. Jeder Kalender beginnt bei einem Ereignis, das für das Volk wichtig war. "
           "Kalendersysteme entstanden aus der Beobachtung der Mondphasen, der Wiederkehr der Jahreszeiten und der Sonnenbahn.\n"
           "- **christlicher Kalender**: ein **Sonnenkalender**. Die Zählung beginnt mit der Geburt Christi.\n"
           "- **römischer Kalender**: Die Römer zählten ab der sagenhaften Gründung ihrer Stadt, **753 v. Chr.** („ab urbe condita“ heißt „seit Gründung der Stadt“).\n"
           "- **jüdischer Kalender**: ein **kombinierter** Sonnen- und Mondkalender. Die Zählung beginnt mit der Erschaffung der Welt, **3761 v. Chr.**\n"
           "- **muslimischer Kalender**: ein **Mondkalender**. Die Zählung beginnt mit dem Auszug Mohammeds aus Mekka, **622 n. Chr.**\n"
           "Ein Beispiel: Am 1. Januar 2000 zählte der muslimische Kalender das Jahr 1420. Seit 622 n. Chr. waren nur 1378 Sonnenjahre vergangen (2000 − 622). "
           "Der Unterschied kommt daher, dass ein Mondjahr kürzer ist als ein Sonnenjahr.",
           merke="Römer: 753 v. Chr. (Stadtgründung). Juden: 3761 v. Chr. (Erschaffung der Welt). Muslime: 622 n. Chr. (Auszug aus Mekka). Mondkalender, Sonnenkalender oder beides."),
    ]


def a_block_a():
    s = "A – Zeit einteilen und messen"
    # Reihenfolge nach dem Alter (Jahreszahlen nur zur Prüfung)
    geraete = [("Wechsel von Tag und Nacht", -10**6), ("Sonnenuhr im alten Griechenland (3. Jh. v. Chr.)", -250),
               ("mechanische Uhr in Deutschland (um 1400)", 1400), ("Uhr mit Zifferblatt (20. Jh.)", 1950)]
    assert [y for _, y in geraete] == sorted(y for _, y in geraete)
    return [
        mc("Wozu teilt man die Zeit ein und misst sie?", "Damit man sich zeitlich orientieren kann.",
           ["Damit man sich im Gelände nicht verläuft.", "Damit man Entfernungen genau messen kann.", "Damit man das Wetter vorhersagen kann."], s,
           info="Eine Zeiteinteilung hilft dir, dich zeitlich zu orientieren: Was war früher, was später, wie lange ist etwas her? Im Gelände orientierst du dich dagegen mit Karte und Kompass."),
        tf("Wie lange etwas gedauert hat, kann man nach dem Gefühl zuverlässig sagen.", False, s,
           info="Das Zeitgefühl täuscht: Manchmal vergeht die Zeit „wie im Flug“, manchmal scheint sie stehen zu bleiben. Darum misst man sie."),
        mc("Wähle alle Geräte, mit denen man die Zeit misst.", ["Sonnenuhr", "Sanduhr", "mechanische Uhr"], ["Kompass", "Thermometer"], s,
           info="Sonnenuhr, Sanduhr und mechanische Uhr zeigen die Zeit an. Der Kompass zeigt die Richtung, das Thermometer die Temperatur."),
        mc("Woran hielten sich die Menschen zuerst, um sich zeitlich zu orientieren?", "am Wechsel von Tag und Nacht",
           ["an der mechanischen Uhr", "an der Uhr mit Zifferblatt", "an einem Kalender mit 366 Tagen"], s,
           info="Der Wechsel von Tag und Nacht war die erste Orientierung. Erst danach teilte man den Tag selbst ein, zum Beispiel mit der Sonnenuhr."),
        mc("Warum ist der Wechsel von Tag und Nacht nur eine grobe Orientierung?", "Der Tag ist im Lauf des Jahres mal länger, mal kürzer.",
           ["Man kann damit nur ganze Jahre zählen, aber keine Tage.", "Tag und Nacht wechseln ganz unregelmäßig, mal nach drei, mal nach zehn Stunden.", "Man sieht den Wechsel nur im Winter, im Sommer ist es immer hell."], s,
           info="Weil sich die Länge des Tages im Jahresverlauf ändert, taugt der Wechsel nur für eine grobe Einteilung."),
        zuordnen("Ordne jedem Hilfsmittel die passende Angabe zu.",
                 [("Wechsel von Tag und Nacht", "grobe Orientierung ohne Gerät"), ("Sonnenuhr", "griechisches Beispiel aus dem 3. Jh. v. Chr."),
                  ("Sanduhr", "Sand rieselt durch eine enge Stelle"), ("mechanische Uhr", "in Deutschland um 1400"),
                  ("Uhr mit Zifferblatt", "20. Jahrhundert")],
                 s, extra=["Zeiger zeigen immer nach Norden"],
                 info="Die Geräte wurden immer feiner: erst die Sonnenuhr, dann Sanduhr und mechanische Uhr, im 20. Jahrhundert die Uhr mit Zifferblatt."),
        reihenfolge("Ordne die Hilfsmittel der Zeitmessung nach ihrem Alter. Das älteste steht oben.", [n for n, _ in geraete], s,
                    info="Zuerst gab es nur Tag und Nacht, dann die Sonnenuhr (3. Jh. v. Chr.), um 1400 die mechanische Uhr und im 20. Jahrhundert die Uhr mit Zifferblatt.",
                    tipp="Denke an die Jahreszahlen: 3. Jahrhundert v. Chr., um 1400, 20. Jahrhundert."),
        luecke("Ergänze den Text über die Zeitmessung.",
               "Zuerst hielt man sich an den Wechsel von {{Tag und Nacht}}. Dann teilte man den Tag selbst ein. Die {{Sonnenuhr}} gab es schon bei den Griechen. "
               "Später kamen die {{Sanduhr}} (Sand rieselt durch eine enge Stelle) und die {{mechanische Uhr}} (in Deutschland um 1400). So konnte man die Zeit immer {{genauer}} messen.",
               s, extra=["Kalender", "ungenauer"],
               info="Die Zeitmessung wurde in einem sehr langen Prozess immer feiner: von Tag und Nacht bis zu Uhren, die winzige Zeitunterschiede messen."),
    ]


def a_block_b():
    s = "B – Mondphasen, Monate und Jahre"
    MONAT = 29.5
    assert 12 * MONAT == 354 and 6 * MONAT == 177 and 365 - 354 == 11
    return [
        kurz("Wie viele Tage dauert es etwa von einem Vollmond bis zum nächsten?", zahl_antw(29.5, "Tage", ca=True), s, einheit="Tage",
             info="Von Vollmond zu Vollmond vergehen etwa 29,5 Tage. Daraus entstand der Monat."),
        mc("Wie viele Tage hat ein Mondjahr?", "354 Tage", ["365 Tage", "366 Tage", "295 Tage"], s,
           info="Ein Mondjahr hat 12 Monate. 12 × 29,5 Tage = 354 Tage."),
        kurz("Rechne: Wie viele Tage dauern 6 Monate zu je 29,5 Tagen?", zahl_antw(177, "Tage"), s, einheit="Tage",
             info="6 × 29,5 = 177. Zwölf Monate wären doppelt so viel, nämlich 354 Tage.",
             tipp="Rechne 6 × 29 und dazu 6 × 0,5."),
        mc("Um wie viele Tage ist das Mondjahr kürzer als das Sonnenjahr (365 Tage)?", "11 Tage", ["1 Tag", "19 Tage", "29,5 Tage"], s,
           info="365 − 354 = 11. Deshalb verschieben sich die Jahreszeiten, wenn man nur nach dem Mond zählt."),
        mc("Warum passt ein reines Mondjahr nicht zu den Jahreszeiten?", "Die Jahreszeiten richten sich nach dem Lauf der Erde um die Sonne.",
           ["Der Mond bewegt sich im Winter deutlich schneller um die Erde.", "Im Mondjahr gibt es nur drei Jahreszeiten statt vier.", "Das Mondjahr hat mehr Tage als das Sonnenjahr."], s,
           info="Die Jahreszeiten entstehen durch den Umlauf der Erde um die Sonne. Das Mondjahr ist mit 354 Tagen außerdem kürzer als das Sonnenjahr mit etwa 365 Tagen."),
        tf("Ein Mondjahr ist länger als ein Sonnenjahr.", False, s, info="Das Mondjahr hat 354 Tage, das Sonnenjahr etwa 365 Tage. Das Mondjahr ist also 11 Tage kürzer."),
        zuordnen("Ordne die Zeitspannen den Tageszahlen zu.",
                 [("Monat (Vollmond bis Vollmond)", "etwa 29,5 Tage"), ("Mondjahr", "354 Tage"), ("Sonnenjahr", "etwa 365 Tage"), ("Schaltjahr", "366 Tage")],
                 s, extra=["360 Tage"],
                 info="Ein Monat dauert etwa 29,5 Tage, das Mondjahr 12 Monate (354 Tage), das Sonnenjahr etwa 365 Tage und das Schaltjahr 366 Tage."),
        luecke("Ergänze die Tageszahlen.",
               "Das Mondjahr hat 12 Monate und {{354}} Tage. Ein Sonnenjahr dauert etwa {{365}} Tage. Weil das nicht ganz genau stimmt, gibt es alle {{vier}} Jahre ein Schaltjahr mit {{366}} Tagen.",
               s, extra=["355", "zwei"],
               info="354 Tage Mondjahr, etwa 365 Tage Sonnenjahr, alle vier Jahre ein Schaltjahr mit 366 Tagen."),
    ]


def a_block_c():
    s = "C – Vor und nach Christi Geburt"
    jahre = [-900, -300, -44, 30, 800]
    assert jahre == sorted(jahre)
    weit = [-3761, -753, -44, 622]
    assert min(weit) == -3761
    return [
        mc("Von welchem Ereignis aus zählt unsere Zeitrechnung die Jahre?", "von der Geburt Christi",
           ["von der Gründung der Stadt Rom", "von der Erschaffung der Welt", "vom Auszug Mohammeds aus Mekka"], s,
           info="Die Geburt Christi ist der Nullpunkt. Die anderen Ereignisse sind die Anfänge des römischen, jüdischen und muslimischen Kalenders."),
        kurz("Wofür steht das Kürzel „v. Chr.“?", ["vor Christus", "vor Christi Geburt", "vor Christi", "vor Christus Geburt"], s,
             info="v. Chr. heißt „vor Christus“. Diese Jahre zählt man rückwärts vom Nullpunkt aus."),
        luecke("Ergänze den Text über unsere Zeitrechnung.",
               "Unsere Zeitrechnung beginnt mit der {{Geburt Christi}}. Die Jahre davor zählt man {{rückwärts}} und schreibt „{{v. Chr.}}“ dahinter. Die Jahre danach schreibt man mit „{{n. Chr.}}“.",
               s, extra=["Gründung Roms", "vorwärts"],
               info="Nullpunkt ist die Geburt Christi. Davor v. Chr. (rückwärts gezählt), danach n. Chr."),
        zuordnen("Was bedeutet das Kürzel?",
                 [("v. Chr.", "vor Christus"), ("n. Chr.", "nach Christus"), ("v. u. Z.", "vor unserer Zeitrechnung"), ("n. u. Z.", "nach unserer Zeitrechnung")],
                 s, extra=["vor unserem Zeitalter"],
                 info="„Chr.“ steht für Christus, „u. Z.“ für „unsere Zeitrechnung“. Beide Schreibweisen meinen dasselbe."),
        mc("Wähle alle Jahre, die vor Christi Geburt liegen.", ["753 v. Chr.", "44 v. Chr."], ["30 n. Chr.", "622 n. Chr.", "1969 n. Chr."], s,
           info="Alle Jahre mit „v. Chr.“ liegen vor dem Nullpunkt, alle mit „n. Chr.“ danach."),
        mc("Welches dieser Jahre liegt am weitesten zurück?", jahr(min(weit)), [jahr(y) for y in weit if y != min(weit)], s,
           info="Bei „v. Chr.“ liegt das Jahr mit der größten Zahl am weitesten zurück. 3761 v. Chr. ist deshalb das früheste Jahr.",
           tipp="Bei v. Chr. wird rückwärts gezählt."),
        reihenfolge("Ordne die Jahre vom frühesten zum spätesten.", [jahr(y) for y in jahre], s,
                    info="Erst die Jahre v. Chr. (die größte Zahl zuerst: 900, 300, 44), dann die Jahre n. Chr. (die kleinste Zahl zuerst: 30, 800).",
                    tipp="Bei v. Chr. ist die größere Zahl früher."),
        tf("Bei Jahren v. Chr. liegt das Jahr mit der kleineren Zahl früher.", False, s,
           info="Es ist umgekehrt: Bei v. Chr. wird rückwärts gezählt, deshalb liegt 300 v. Chr. früher als 200 v. Chr."),
    ]


def les(t, titel):
    """Verfeinert den Nachlesen-Verweis einer Aufgabe."""
    t["lesen"] = titel
    return t


def a_block_d():
    s = "D – Jahre vergleichen und Abstände berechnen"
    d1 = spanne(-753, -44)
    d2 = spanne(-100, 50)
    d3 = spanne(-44, 800)
    d5 = spanne(-3761, -753)
    d8 = spanne(800, 1450)
    assert (d1, d2, d3, d5, d8) == (709, 150, 844, 3008, 650) and d2 == 100 + 50 and d3 == 44 + 800
    paare = [(-500, 100), (-200, -50), (400, 900), (-60, 30)]
    abst = [spanne(a, b) for a, b in paare]
    assert abst == [600, 150, 500, 90] and max(abst) == 600
    txt = lambda a, b: f"{jahr(a)} und {jahr(b)}"
    return [
        kurz("Wie viele Jahre liegen zwischen 753 v. Chr. und 44 v. Chr.?", zahl_antw(d1), s, einheit="Jahre",
             info="Beide Jahre liegen vor Christi Geburt, also ziehst du ab: 753 − 44 = 709 Jahre."),
        kurz("Wie viele Jahre liegen zwischen 100 v. Chr. und 50 n. Chr.? Rechne wie in der Schule (ohne Jahr 0).", zahl_antw(d2), s, einheit="Jahre",
             info="Ein Jahr liegt vor, eins nach Christi Geburt. Du zählst zusammen: 100 + 50 = 150 Jahre.",
             tipp="Die beiden Jahre liegen auf verschiedenen Seiten von Christi Geburt."),
        mc("Wie viele Jahre liegen zwischen 44 v. Chr. und 800 n. Chr.? Rechne wie in der Schule (ohne Jahr 0).", f"{d3} Jahre", ["756 Jahre", "988 Jahre", "1244 Jahre"], s,
           info="Über Christi Geburt hinweg zählst du zusammen: 44 + 800 = 844. Wer 800 − 44 rechnet, vergisst, dass die Jahre auf verschiedenen Seiten liegen."),
        mc("Wie rechnest du, wie viele Jahre zwischen 300 v. Chr. und 200 n. Chr. liegen?", "300 + 200 = 500 Jahre",
           ["300 − 200 = 100 Jahre", "200 − 300 = −100 Jahre"], s,
           info="Das eine Jahr liegt vor, das andere nach Christi Geburt. Dann zählst du die beiden Zahlen zusammen."),
        kurz("Der jüdische Kalender beginnt 3761 v. Chr., der römische 753 v. Chr. Wie viele Jahre liegen dazwischen?", zahl_antw(d5), s, einheit="Jahre",
             info="Beide Jahre liegen vor Christi Geburt. Du ziehst ab: 3761 − 753 = 3008 Jahre.",
             tipp="Beide Jahre haben „v. Chr.“."),
        mc("Bei welchem Paar liegen die Jahre am weitesten auseinander?", txt(*paare[0]), [txt(*p) for p in paare[1:]], s,
           info="500 v. Chr. bis 100 n. Chr.: 500 + 100 = 600 Jahre. Bei den anderen Paaren sind es 150, 500 und 90 Jahre.",
           tipp="Rechne bei jedem Paar den Abstand aus (wie in der Schule, ohne Jahr 0). Achte darauf, ob die Jahre auf derselben Seite von Christi Geburt liegen."),
        tf("Rechne wie in der Schule (ohne Jahr 0): Zwischen 50 v. Chr. und 50 n. Chr. liegen 100 Jahre.", True, s, info="50 + 50 = 100. Die Jahre liegen auf verschiedenen Seiten, also zählst du zusammen."),
        tf("Zwischen 800 n. Chr. und 1450 n. Chr. liegen 2250 Jahre.", False, s,
           info=f"Beide Jahre liegen nach Christi Geburt. Du ziehst ab: 1450 − 800 = {d8} Jahre. Zusammenzählen darfst du nur über Christi Geburt hinweg."),
        luecke("Ergänze die Rechenregeln für Abstände.",
               "Liegen beide Jahre auf derselben Seite von Christi Geburt, {{ziehst}} du die Zahlen ab. Liegt ein Jahr vor und eins nach Christi Geburt, {{zählst}} du die Zahlen zusammen.",
               s, extra=["teilst", "multiplizierst"],
               info="Gleiche Seite: abziehen. Über Christi Geburt hinweg: zusammenzählen."),
    ]


def a_block_e():
    s = "E – Jahrhunderte bestimmen"
    assert jh(1969) == 20 and jh(1450) == 15 and jh(44) == 1 and jh(876) == 9 and jh(2005) == 21 and jh(753) == 8
    assert jh(1517) == 16 and jh(1848) == 19 and jh(87) == 1
    assert jh_range(13) == (1200, 1299) and jh_range(1) == (1, 99)
    zu = [(1517, 16), (1848, 19), (876, 9), (2005, 21), (87, 1)]
    return [
        mc("Welche Jahre gehören zum 13. Jahrhundert?", "1200 bis 1299", ["1300 bis 1399", "1100 bis 1199", "1250 bis 1350"], s,
           info="Alle Jahreszahlen, die mit „12“ beginnen, gehören zum 13. Jahrhundert: 12 + 1 = 13."),
        kurz("In welchem Jahrhundert liegt das Jahr 1969?", jh_antw(jh(1969)), s,
             info="Die letzten zwei Stellen weglassen: 19. Dann 1 dazuzählen: 19 + 1 = 20. Es ist das 20. Jahrhundert.", tipp="Streiche „69“ und zähle 1 dazu."),
        kurz("In welchem Jahrhundert liegt das Jahr 1450?", jh_antw(jh(1450)), s,
             info="14 + 1 = 15. Das Jahr 1450 liegt im 15. Jahrhundert."),
        kurz("In welchem Jahrhundert liegt das Jahr 44 n. Chr.?", jh_antw(jh(44)), s,
             info="Alle Jahre unter 100 gehören zum 1. Jahrhundert. Rechnerisch: 0 + 1 = 1.", tipp="Es ist ein Jahr unter 100."),
        luecke("Ergänze den Text über Jahrhunderte.",
               "Das 13. Jahrhundert reicht von {{1200}} bis {{1299}}. Das {{1.}} Jahrhundert umfasst alle Jahre unter {{100}}.",
               s, extra=["1300", "1100"],
               info="13. Jahrhundert = 1200 bis 1299. 1. Jahrhundert = die Jahre unter 100."),
        zuordnen("Ordne jedem Jahr sein Jahrhundert zu.",
                 [(f"{y} n. Chr.", f"{n}. Jahrhundert") for y, n in zu], s, extra=["14. Jahrhundert", "18. Jahrhundert"],
                 info="Rechne: Jahr ohne die letzten zwei Stellen, plus 1. Zum Beispiel 876 → 8 + 1 = 9."),
        mc("Wie findest du das Jahrhundert eines Jahres?", "Die letzten zwei Stellen streichen und 1 dazuzählen.",
           ["Die letzte Stelle streichen und 1 dazuzählen.", "Die letzten zwei Stellen streichen, nichts dazuzählen.", "Die Jahreszahl durch 10 teilen."], s,
           info="Beispiel 1969: 19 + 1 = 20. Das Jahrhundert ist immer um 1 größer als die Zahl vor den letzten zwei Stellen."),
        mc("In welchem Jahrhundert liegt das Jahr 753 v. Chr.?", "im 8. Jahrhundert v. Chr.",
           ["im 7. Jahrhundert v. Chr.", "im 1. Jahrhundert v. Chr.", "im 75. Jahrhundert v. Chr."], s,
           info="Auch bei v. Chr. streichst du die letzten zwei Stellen und zählst 1 dazu: 7 + 1 = 8. " + ZW,
           tipp="Gleiche Rechnung wie bei n. Chr."),
    ]


def a_block_f():
    s = "F – Andere Kalender"
    wf = 2000 - 622
    assert wf == 1378 and 1419 <= wf * 365 / 354 <= 1422
    return [
        zuordnen("Ordne jedem Kalender den Beginn seiner Zählung zu.",
                 [("christlicher Kalender", "Geburt Christi"), ("römischer Kalender", "Gründung der Stadt Rom (753 v. Chr.)"),
                  ("jüdischer Kalender", "Erschaffung der Welt (3761 v. Chr.)"), ("muslimischer Kalender", "Auszug Mohammeds aus Mekka (622 n. Chr.)")],
                 s, extra=["Tod Julius Caesars (44 v. Chr.)"],
                 info="Jeder Kalender beginnt bei einem Ereignis, das für das Volk wichtig war."),
        zuordnen("Ordne jedem Kalender seine Art zu.",
                 [("christlicher Kalender", "Sonnenkalender"), ("muslimischer Kalender", "Mondkalender"), ("jüdischer Kalender", "kombinierter Sonnen- und Mondkalender")],
                 s, extra=["reiner Sternenkalender"],
                 info="Der christliche Kalender folgt der Sonne, der muslimische dem Mond und der jüdische verbindet beides."),
        kurz("In welchem Jahr n. Chr. begann der Auszug Mohammeds aus Mekka, mit dem der muslimische Kalender anfängt?", jahr_antw(622), s,
             info="Der muslimische Kalender zählt ab dem Auszug Mohammeds aus Mekka im Jahr 622 n. Chr."),
        kurz("Die Römer zählten ihre Jahre ab der Gründung ihrer Stadt. In welchem Jahr v. Chr. war das nach der Sage?", jahr_antw(-753), s,
             info="Nach der Sage wurde Rom 753 v. Chr. gegründet. „ab urbe condita“ heißt „seit Gründung der Stadt“."),
        mc("Welcher dieser Kalender ist ein reiner Mondkalender?", "der muslimische Kalender", ["der christliche Kalender", "der jüdische Kalender"], s,
           info="Der muslimische Kalender folgt allein den Mondphasen. Der christliche ist ein Sonnenkalender, der jüdische verbindet Sonne und Mond."),
        tf("Die Römer zählten ihre Jahre ab der Geburt Christi.", False, s,
           info="Die Römer zählten ab der Gründung ihrer Stadt (753 v. Chr.). Die Geburt Christi ist der Nullpunkt der christlichen Zeitrechnung."),
        tf("Im Jahr 2000 zählte der muslimische Kalender das Jahr 1420, obwohl seit 622 nur 1378 Jahre vergangen waren. Das liegt am kürzeren Mondjahr.", True, s,
           info="Das Mondjahr hat nur 354 Tage. In derselben Zeit vergehen also mehr Mondjahre als Sonnenjahre. 1378 Sonnenjahre sind rund 1420 Mondjahre."),
        mc("Was bedeutet „ab urbe condita“, wie die Römer ihre Jahre zählten?", "seit Gründung der Stadt",
           ["seit dem Ende des Krieges", "seit der Geburt des Kaisers", "vor Christi Geburt"], s,
           info="Die Römer zählten ab der sagenhaften Gründung ihrer Stadt Rom (753 v. Chr.)."),
    ]


def a_block_g():
    s = "G – Klausurnah: Zeit und Zeitrechnung"
    g5 = [("Beginn des jüdischen Kalenders (3761 v. Chr.)", -3761), ("Beginn des römischen Kalenders (753 v. Chr.)", -753),
          ("Geburt Christi (Nullpunkt unserer Zeitrechnung)", 0), ("Beginn des muslimischen Kalenders (622 n. Chr.)", 622)]
    assert [y for _, y in g5] == sorted(y for _, y in g5)
    g3 = spanne(-753, 622)
    assert g3 == 753 + 622 == 1375
    return [
        les(frei("Was ist eine Zeiteinteilung und wofür braucht man sie? Antworte in zwei bis drei Sätzen.",
                 "Die Dauer der Zeit nach Gefühl zu schätzen ist unsicher: Manchmal vergeht die Zeit wie im Flug, manchmal gar nicht. Darum haben die Menschen die Zeit gemessen und eingeteilt, mit Uhren und Kalendern. "
                 "So kann man sich zeitlich orientieren, also sagen, was früher und was später war.",
                 ["Das Zeitgefühl ist unsicher", "Zeit wird mit Uhren und Kalendern gemessen und eingeteilt", "Zweck: sich zeitlich orientieren (früher, später, wie lange her)"], 3, s), L1),
        les(frei("Erkläre den Unterschied zwischen Mondjahr, Sonnenjahr und Schaltjahr.",
                 "Von Vollmond zu Vollmond vergehen etwa 29,5 Tage, das ist ein Monat. Zwölf Monate ergeben das Mondjahr mit 354 Tagen. Die Jahreszeiten richten sich aber nach der Sonne. "
                 "Das Sonnenjahr dauert etwa 365 Tage und ist damit 11 Tage länger. Weil auch das nicht ganz genau ist, gibt es alle vier Jahre ein Schaltjahr mit 366 Tagen.",
                 ["Mondjahr: 12 Monate, 354 Tage (Monat etwa 29,5 Tage)", "Sonnenjahr: etwa 365 Tage, passt zu den Jahreszeiten", "Schaltjahr: alle vier Jahre, 366 Tage"], 3, s), L3),
        les(kurz("Wie viele Jahre liegen zwischen der Gründung Roms (753 v. Chr.) und dem Auszug Mohammeds aus Mekka (622 n. Chr.)? Rechne wie in der Schule (ohne Jahr 0).", zahl_antw(g3), s, einheit="Jahre",
                 info="Das eine Jahr liegt vor, das andere nach Christi Geburt. Du zählst zusammen: 753 + 622 = 1375 Jahre.",
                 tipp="Über Christi Geburt hinweg zählt man zusammen."), L5),
        les(mc("Wähle alle richtigen Aussagen.", ["Das Mondjahr hat 354 Tage.", "Ein Schaltjahr hat 366 Tage.", "Das 13. Jahrhundert reicht von 1200 bis 1299."],
               ["Der muslimische Kalender ist ein Sonnenkalender.", "Die Römer zählten ihre Jahre ab der Geburt Christi."], s,
               info="Der muslimische Kalender ist ein Mondkalender, und die Römer zählten ab der Gründung ihrer Stadt (753 v. Chr.). Die drei anderen Aussagen stimmen."), [L3, L6, L7]),
        les(reihenfolge("Ordne die Anfänge der Kalender vom frühesten zum spätesten.", [n for n, _ in g5], s,
                        info="Bei v. Chr. liegt die größere Zahl früher: erst 3761 v. Chr., dann 753 v. Chr., dann der Nullpunkt, zuletzt 622 n. Chr.",
                        tipp="Bei v. Chr. ist die größere Zahl früher."), L7),
        les(frei("Erkläre unsere Zeitrechnung: Wo beginnt sie, was bedeuten v. Chr. und n. Chr., und wie viele Jahre liegen zwischen 100 v. Chr. und 50 n. Chr. (rechne wie in der Schule, ohne Jahr 0)?",
                 "Unsere Zeitrechnung beginnt mit der Geburt Christi, das ist der Nullpunkt. Die Jahre davor zählt man rückwärts und schreibt v. Chr. (vor Christus). Die Jahre danach schreibt man n. Chr. (nach Christus). "
                 "Zwischen 100 v. Chr. und 50 n. Chr. liegen 100 + 50 = 150 Jahre, weil man über Christi Geburt hinweg zusammenzählt.",
                 ["Nullpunkt ist die Geburt Christi", "v. Chr. = vor Christus (rückwärts gezählt), n. Chr. = nach Christus", "Abstand 150 Jahre, richtig durch Zusammenzählen"], 3, s), [L4, L5]),
    ]


def aufgaben_a():
    return a_block_a() + a_block_b() + a_block_c() + a_block_d() + a_block_e() + a_block_f() + a_block_g()


def paket_a():
    p = pack("geschichte-2a-zeitrechnung-kalender", "Geschichte Teil 2a: Zeit messen, Kalender und Zeitrechnung",
             "Warum man die Zeit einteilt, Zeitmessung von der Sonnenuhr bis zur Uhr, Mondjahr und Sonnenjahr, vor und nach Christi Geburt, Jahrhunderte und andere Kalender. Mit Lernblatt und vielen Übungsaufgaben.",
             lernblatt_a(), aufgaben_a(), min_aufgaben=45,
             hinweis="Bei Abständen über Christi Geburt hinweg wird wie in der Schule einfach zusammengezählt (streng genommen gibt es kein Jahr 0). Aufgaben mit „Zusatzwissen“ gehen über das Heft hinaus.")
    nachlesen(p, {
        "A – Zeit einteilen und messen": [L1, L2],
        "B – Mondphasen, Monate und Jahre": L3,
        "C – Vor und nach Christi Geburt": L4,
        "D – Jahre vergleichen und Abstände berechnen": L5,
        "E – Jahrhunderte bestimmen": L6,
        "F – Andere Kalender": L7,
        "G – Klausurnah: Zeit und Zeitrechnung": [L1, L3, L4, L5, L6, L7],
    })
    p["probe"] = False
    return p


# ================================================================== Paket 2b: Epochen und Zeitstrahl

M1 = "Die fünf Epochen"
M2 = "Reihenfolge und Abkürzungen der Epochen"
M3 = "Die Epoche eines Jahres bestimmen"
M4 = "Ereignisse den Epochen zuordnen"
M5 = "Wofür ein Zeitstrahl gut ist"
M6 = "Einen Zeitstrahl zeichnen und lesen"
M7 = "Abstände zwischen Ereignissen berechnen"

NAMEN = [n for n, _, _ in EPOCHEN]

# Ereignisse: (Text mit Jahr, Jahr zur Prüfung). Bevorzugt Ereignisse aus fakten.md; Pyramide und Mondlandung sind Zusatzwissen.
EV = {
    "oetzi": ("Ötzis Leben (3359 bis 3105 v. Chr.)", -3232),
    "acker": ("Beginn des Ackerbaus in Mitteleuropa (ab etwa 5700 v. Chr.)", -5700),
    "pyramide": ("Bau der großen Pyramide von Gizeh (um 2500 v. Chr.)", -2500),
    "rom": ("Gründung Roms nach der Sage (753 v. Chr.)", -753),
    "sonnenuhr": ("griechische Sonnenuhr (3. Jahrhundert v. Chr.)", -250),
    "caesar": ("Tod Julius Caesars (44 v. Chr.)", -44),
    "mohammed": ("Auszug Mohammeds aus Mekka (622 n. Chr.)", 622),
    "uhr": ("mechanische Uhr in Deutschland (um 1400)", 1400),
    "mond": ("erste Mondlandung (1969)", 1969),
}
EV_EP = {k: ep_jahr(y) for k, (_, y) in EV.items()}
assert EV_EP == {"oetzi": "Ur- und Frühgeschichte", "acker": "Ur- und Frühgeschichte", "pyramide": "Altertum", "rom": "Antike",
                 "sonnenuhr": "Antike", "caesar": "Antike", "mohammed": "Mittelalter", "uhr": "Mittelalter", "mond": "Neuzeit"}


def lernblatt_b():
    dauer = [None, spanne(-3000, -1000), spanne(-1000, 500), spanne(500, 1500)]
    assert dauer[1:] == [2000, 1500, 1000]
    return [
        lb(M1,
           "Die Geschichte der Menschen ist sehr lang. Damit man den Überblick behält, teilt man sie in große Abschnitte ein. Diese Abschnitte heißen **Epochen**. Du lernst fünf:\n"
           "- **Ur- und Frühgeschichte**: bis 3000 v. Chr. Dazu gehört die ganze Steinzeit.\n"
           "- **Altertum**: 3000 v. Chr. bis 1000 v. Chr.\n"
           "- **Antike**: 1000 v. Chr. bis 500 n. Chr.\n"
           "- **Mittelalter**: etwa 500 n. Chr. bis 1500 n. Chr.\n"
           "- **Neuzeit**: etwa ab 1500 n. Chr. bis heute.\n"
           "Die Grenzen gelten nur ungefähr. Darum steht bei manchen Angaben „ca.“ davor.",
           merke="Fünf Epochen: Ur- und Frühgeschichte (bis 3000 v. Chr.), Altertum (3000 bis 1000 v. Chr.), Antike (1000 v. Chr. bis 500 n. Chr.), Mittelalter (500 bis 1500 n. Chr.), Neuzeit (ab 1500 n. Chr.).",
           bild=svg_epochen(nummern=False, jahre=False),
           bildAlt="Zeitstrahl mit fünf farbigen Balken nebeneinander: Ur- und Frühgeschichte, Altertum, Antike, Mittelalter und Neuzeit, jeweils mit ihren Jahreszahlen darunter."),
        lb(M2,
           "Lerne die Epochen in dieser Reihenfolge, vom ältesten zum jüngsten: Ur- und Frühgeschichte, Altertum, Antike, Mittelalter, Neuzeit.\n"
           "- Abkürzungen: **MA** steht für Mittelalter, **NZ** für Neuzeit.\n"
           "- Altertum und Antike sind zwei verschiedene Epochen. Das Altertum kommt zuerst.\n"
           "- Wie lange dauern die Epochen? Das Altertum 2000 Jahre (3000 − 1000), die Antike 1500 Jahre (1000 + 500) und das Mittelalter 1000 Jahre (1500 − 500).",
           merke="Reihenfolge: Ur- und Frühgeschichte, Altertum, Antike, Mittelalter (MA), Neuzeit (NZ)."),
        lb(M3,
           "So bestimmst du die Epoche eines Jahres:\n"
           "- Schau, ob das Jahr v. Chr. oder n. Chr. ist.\n"
           "- Vergleiche es mit den Grenzen: 3000 v. Chr., 1000 v. Chr., 500 n. Chr. und 1500 n. Chr.\n"
           "- Denke daran: Bei v. Chr. ist die größere Zahl früher.\n"
           "Beispiele: 4000 v. Chr. ist früher als 3000 v. Chr., also Ur- und Frühgeschichte. 2000 v. Chr. liegt zwischen 3000 und 1000 v. Chr., also Altertum. "
           "300 v. Chr. liegt nach 1000 v. Chr., aber vor Christi Geburt, also Antike. 1200 n. Chr. liegt zwischen 500 und 1500, also Mittelalter. 1969 n. Chr. liegt nach 1500, also Neuzeit.\n"
           "In Aufgaben liegt ein Jahr nicht genau auf einer Grenze.",
           merke="Erst v. Chr. oder n. Chr. klären, dann mit den Grenzen vergleichen. Bei v. Chr. gilt: größere Zahl = früher."),
        lb(M4,
           "Um ein Ereignis einer Epoche zuzuordnen, brauchst du seine Jahreszahl. Diese Beispiele solltest du kennen:\n"
           "- **Steinzeit** (Lucy, Altsteinzeit, Jungsteinzeit): Ur- und Frühgeschichte. Ötzi lebte zwischen 3359 und 3105 v. Chr., also auch dort.\n"
           "- Beginn des Ackerbaus in Mitteleuropa, ab etwa 5700 v. Chr.: Ur- und Frühgeschichte.\n"
           "- Bau der großen Pyramide von Gizeh, um 2500 v. Chr.: Altertum. (Zusatzwissen, nicht aus Heft oder Buch)\n"
           "- griechische Sonnenuhr, 3. Jahrhundert v. Chr.: Antike.\n"
           "- Gründung Roms nach der Sage, 753 v. Chr.: Antike.\n"
           "- Tod Julius Caesars, 44 v. Chr.: Antike.\n"
           "- Auszug Mohammeds aus Mekka, 622: Mittelalter.\n"
           "- mechanische Uhr in Deutschland, um 1400: Mittelalter.\n"
           "- erste Mondlandung, 1969: Neuzeit. (Zusatzwissen, nicht aus Heft oder Buch)",
           merke="Jahreszahl des Ereignisses suchen und mit den Epochengrenzen vergleichen. Die Steinzeit gehört zur Ur- und Frühgeschichte."),
        lb(M5,
           "Ein **Zeitstrahl** ist eine gezeichnete Linie, auf der man Ereignisse in ihrer zeitlichen Abfolge darstellt. Links liegt das Frühere, rechts das Spätere. "
           "So siehst du auf einen Blick, was zuerst geschah und wie weit zwei Ereignisse auseinanderliegen.\n"
           "Christi Geburt ist der Nullpunkt: links davon liegen die Jahre v. Chr., rechts die Jahre n. Chr. Im Bild steht der Punkt A für den Tod Julius Caesars (44 v. Chr.). "
           "Auch die Epochen kann man als Abschnitte auf einen Zeitstrahl zeichnen.",
           merke="Ein Zeitstrahl stellt Ereignisse in ihrer zeitlichen Abfolge dar. Links ist früher, rechts ist später.",
           bild=svg_zeitstrahl_punkte([("A", -44)]),
           bildAlt="Zeitstrahl von 100 v. Chr. bis 50 n. Chr. mit einem Punkt A zwischen 50 v. Chr. und 40 v. Chr."),
        lb(M6,
           "Beim Zeichnen wählst du einen **Maßstab**. Er sagt, wie viele Jahre ein Zentimeter bedeutet. Beispiel: **10 Jahre = 1 cm**. "
           "Die Länge rechnest du so aus: Jahre geteilt durch 10 ergibt die Zentimeter. 80 Jahre sind 8 cm.\n"
           "So zeichnest du einen Zeitstrahl von 100 v. Chr. bis 50 n. Chr.:\n"
           "- Länge berechnen: 150 Jahre : 10 = 15 cm.\n"
           "- Eine Linie von 15 cm zeichnen.\n"
           "- Alle 10 Jahre, also alle 1 cm, einen Strich setzen.\n"
           "- Wichtige Jahre beschriften: 100 v. Chr. (0 cm), 50 v. Chr. (5 cm), Christi Geburt (10 cm) und 50 n. Chr. (15 cm).\n"
           "- Ereignisse eintragen. Beispiel 44 v. Chr.: Es liegt 56 Jahre nach 100 v. Chr., also bei 5,6 cm.\n"
           "Zwei Wörter helfen bei Aufgaben: Ein **Jahrzehnt** sind 10 Jahre. Das 4. Jahrzehnt des 1. Jahrhunderts n. Chr. sind die Jahre 30 bis 39 n. Chr. "
           "Das 1. Jahrhundert v. Chr. sind die Jahre 100 bis 1 v. Chr., seine zweite Hälfte reicht also von 50 v. Chr. bis Christi Geburt.",
           merke="Zentimeter = Jahre : 10 (bei 10 Jahre = 1 cm). Position = Jahre seit dem Anfang des Zeitstrahls : 10.",
           bild=svg_lineal(marke=-44),
           bildAlt="Lineal von 0 bis 15 cm. Darunter die Jahre 100 v. Chr. (0 cm), 50 v. Chr. (5 cm), Christi Geburt (10 cm) und 50 n. Chr. (15 cm). Eine Markierung bei 5,6 cm zeigt das Jahr 44 v. Chr."),
        lb(M7,
           "Wie viele Jahre liegen zwischen zwei Ereignissen?\n"
           "- Beide Jahre auf derselben Seite von Christi Geburt: **abziehen**. Von der Gründung Roms (753 v. Chr.) bis zum Tod Caesars (44 v. Chr.) sind es 753 − 44 = 709 Jahre.\n"
           "- Ein Jahr vor und eins nach Christi Geburt: **zusammenzählen**. Vom Tod Caesars (44 v. Chr.) bis zum Auszug Mohammeds aus Mekka (622 n. Chr.) sind es 44 + 622 = 666 Jahre.\n"
           "Streng genommen gibt es kein Jahr 0. In der Schule rechnest du trotzdem so (ohne Jahr 0). In Aufgaben steht dann „Rechne wie in der Schule“.\n"
           "Steht bei einem Ereignis „um“ oder „ca.“, ist auch das Ergebnis nur ungefähr.",
           merke="Gleiche Seite: abziehen. Über Christi Geburt hinweg: zusammenzählen."),
    ]


def b_block_a():
    s = "A – Die fünf Epochen kennen"
    assert NAMEN == ["Ur- und Frühgeschichte", "Altertum", "Antike", "Mittelalter", "Neuzeit"]
    mittelalter = spanne(500, 1500)
    assert mittelalter == 1000
    return [
        mc("Welche Epoche kommt direkt nach dem Altertum?", "Antike", ["Mittelalter", "Neuzeit", "Ur- und Frühgeschichte"], s,
           info="Die Reihenfolge lautet: Ur- und Frühgeschichte, Altertum, Antike, Mittelalter, Neuzeit.",
           tipp="Altertum und Antike sind zwei verschiedene Epochen."),
        reihenfolge("Ordne die fünf Epochen vom ältesten zum jüngsten.", NAMEN, s,
                    info="Von ganz früh bis heute: Ur- und Frühgeschichte, Altertum, Antike, Mittelalter, Neuzeit."),
        zuordnen("Ordne jeder Epoche ihren Zeitraum zu.", [(NAMEN[i], zeitraum(i)) for i in range(5)], s, extra=["2000 bis 1000 v. Chr."],
                 info="Die Grenzen sind 3000 v. Chr., 1000 v. Chr., 500 n. Chr. und 1500 n. Chr.",
                 tipp="Die Antike ist die einzige Epoche, die über Christi Geburt hinweggeht."),
        kurz("Wofür steht die Abkürzung MA?", ep_antw("Mittelalter", kuerzel=False), s, info="MA heißt Mittelalter. Es dauerte etwa von 500 bis 1500 n. Chr."),
        kurz("Wofür steht die Abkürzung NZ?", ep_antw("Neuzeit", kuerzel=False), s, info="NZ heißt Neuzeit. Sie beginnt etwa 1500 n. Chr. und dauert bis heute."),
        luecke("Ergänze den Text über die Epochen.",
               "Die Geschichte teilt man in {{Epochen}} ein. Die erste heißt {{Ur- und Frühgeschichte}} und reicht bis 3000 v. Chr. Auf das {{Altertum}} folgt die {{Antike}}. Danach kommen das {{Mittelalter}} und die {{Neuzeit}}.",
               s, extra=["Eiszeit"],
               info="Epochen sind große Abschnitte der Geschichte. Es sind fünf, vom ältesten zum jüngsten."),
        mc("In wie viele Epochen teilt man die Geschichte hier ein?", "5 Epochen", ["3 Epochen", "4 Epochen", "7 Epochen"], s,
           info="Es sind fünf: Ur- und Frühgeschichte, Altertum, Antike, Mittelalter und Neuzeit."),
        tf("Das Mittelalter dauerte etwa 1000 Jahre.", True, s, info=f"Es reicht von etwa 500 bis etwa 1500 n. Chr. Das sind 1500 − 500 = {mittelalter} Jahre."),
    ]


def b_block_b():
    s = "B – Die Epoche eines Jahres bestimmen"
    zu = [(-4000, "Ur- und Frühgeschichte"), (-2000, "Altertum"), (-200, "Antike"), (300, "Antike"), (900, "Mittelalter"), (1800, "Neuzeit")]
    for y, n in zu:
        assert ep_jahr(y) == n
    antike = [-600, 100, 400]
    nicht = [-2000, 900]
    assert all(ep_jahr(y) == "Antike" for y in antike) and all(ep_jahr(y) != "Antike" for y in nicht)
    assert ep_jahr(-3500) == NAMEN[0] and all(ep_jahr(y) != NAMEN[0] for y in (-1500, -300, 800))
    assert (ep_jahr(1200), ep_jahr(-2000), ep_jahr(-300), ep_jahr(-4000)) == ("Mittelalter", "Altertum", "Antike", NAMEN[0])
    assert (ep_jahr(1300), ep_jahr(-1500), ep_jahr(-400), ep_jahr(-5000)) == ("Mittelalter", "Altertum", "Antike", NAMEN[0])
    return [
        mc("In welcher Epoche liegt das Jahr 1200 n. Chr.?", ep_jahr(1200), [n for n in NAMEN if n != ep_jahr(1200)][:3], s,
           info="1200 liegt zwischen 500 und 1500 n. Chr. Das ist das Mittelalter."),
        mc("Welches dieser Jahre gehört zur Ur- und Frühgeschichte?", jahr(-3500), [jahr(-1500), jahr(-300), jahr(800)], s,
           info="3500 v. Chr. ist früher als 3000 v. Chr. (bei v. Chr. ist die größere Zahl früher). Alle späteren Jahre gehören zu anderen Epochen.",
           tipp="Die Ur- und Frühgeschichte endet 3000 v. Chr. Bei v. Chr. ist die größere Zahl früher."),
        mc("In welcher Epoche liegt das Jahr 2000 v. Chr.?", ep_jahr(-2000), ["Ur- und Frühgeschichte", "Antike", "Neuzeit"], s,
           info="2000 v. Chr. liegt zwischen 3000 v. Chr. und 1000 v. Chr. Das ist das Altertum."),
        zuordnen("In welcher Epoche liegt das Jahr?", [(jahr(y), n) for y, n in zu], s,
                 info="Vergleiche jedes Jahr mit den Grenzen 3000 v. Chr., 1000 v. Chr., 500 n. Chr. und 1500 n. Chr.",
                 tipp="Die Antike geht von 1000 v. Chr. bis 500 n. Chr."),
        kurz("Nenne die Epoche, zu der das Jahr 700 n. Chr. gehört.", ep_antw(ep_jahr(700)), s,
             info="700 liegt zwischen 500 und 1500 n. Chr. Das ist das Mittelalter (MA)."),
        luecke("Ergänze die Epochen der Jahre.",
               "Das Jahr 1300 n. Chr. liegt im {{Mittelalter}}. Das Jahr 1500 v. Chr. gehört zum {{Altertum}}. Das Jahr 400 v. Chr. gehört zur {{Antike}}. Das Jahr 5000 v. Chr. liegt in der {{Ur- und Frühgeschichte}}.",
               s, extra=["Neuzeit", "Eiszeit"],
               info="Jedes Jahr mit den Grenzen vergleichen: 3000 v. Chr., 1000 v. Chr., 500 n. Chr., 1500 n. Chr."),
        tf("Das Jahr 800 v. Chr. gehört zum Altertum.", False, s,
           info="800 v. Chr. liegt nach 1000 v. Chr. (die Zahl ist kleiner, das Jahr also später). Es gehört deshalb zur Antike.",
           tipp="Vergleiche 800 v. Chr. mit der Grenze 1000 v. Chr.: Welches der beiden Jahre ist später?"),
        tf("Das Jahr 1700 n. Chr. gehört zur Neuzeit.", True, s, info="Die Neuzeit beginnt etwa 1500 n. Chr. 1700 liegt danach."),
        mc("Wähle alle Jahre, die zur Antike gehören.", [jahr(y) for y in antike], [jahr(y) for y in nicht], s,
           info="Die Antike reicht von 1000 v. Chr. bis 500 n. Chr. 2000 v. Chr. liegt davor (Altertum), 900 n. Chr. danach (Mittelalter).",
           tipp="Achte auf v. Chr. und n. Chr."),
    ]


def b_block_c():
    s = "C – Ereignisse den Epochen zuordnen"
    t = lambda k: EV[k][0]
    reihe = ["oetzi", "rom", "caesar", "mohammed", "uhr", "mond"]
    assert [EV[k][1] for k in reihe] == sorted(EV[k][1] for k in reihe)
    return [
        zuordnen("Ordne jedem Ereignis seine Epoche zu.",
                 [(t(k), EV_EP[k]) for k in ("oetzi", "pyramide", "rom", "mohammed", "uhr", "mond")], s,
                 info="Vergleiche die Jahreszahl mit den Epochengrenzen: Ötzi vor 3000 v. Chr., Rom 1000 v. Chr. bis 500 n. Chr., Mohammed und die mechanische Uhr 500 bis 1500, "
                      "Pyramide (3000 bis 1000 v. Chr.) und Mondlandung (nach 1500) sind Zusatzwissen, nicht aus Heft oder Buch."),
        mc("In welcher Epoche begann der Auszug Mohammeds aus Mekka (622 n. Chr.)?", EV_EP["mohammed"], ["Antike", "Neuzeit", "Altertum"], s,
           info="622 liegt zwischen 500 und 1500 n. Chr. Das ist das Mittelalter."),
        mc("Welches dieser Ereignisse gehört zur Neuzeit?", t("mond"), [t("rom"), t("caesar"), t("mohammed")], s,
           info="Die Neuzeit beginnt etwa 1500 n. Chr. Nur die erste Mondlandung (1969) liegt danach. " + ZW),
        mc("Welches dieser Ereignisse gehört in die Ur- und Frühgeschichte?", t("oetzi"), [t("caesar"), t("uhr"), t("sonnenuhr")], s,
           info="Ötzi lebte vor 3000 v. Chr. Das ist Ur- und Frühgeschichte (Steinzeit). Die anderen drei Ereignisse liegen nach 1000 v. Chr."),
        tf("Ötzi lebte in der Antike.", False, s,
           info="Ötzi lebte zwischen 3359 und 3105 v. Chr. und damit vor 3000 v. Chr. Das ist die Ur- und Frühgeschichte.",
           tipp="Wann beginnt die Antike?"),
        tf("Die ganze Steinzeit gehört zur Ur- und Frühgeschichte.", True, s,
           info="Die Jungsteinzeit endet um 3000 v. Chr., und genau dort endet auch die Ur- und Frühgeschichte."),
        kurz("In welcher Epoche wurde Rom nach der Sage gegründet (753 v. Chr.)?", ep_antw(EV_EP["rom"]), s,
             info="753 v. Chr. liegt nach 1000 v. Chr. und vor Christi Geburt. Das ist die Antike."),
        reihenfolge("Ordne die Ereignisse nach der Zeit. Das früheste steht oben.", [t(k) for k in reihe], s,
                    info="Ötzi (3359 bis 3105 v. Chr.), Gründung Roms (753 v. Chr.), Caesar (44 v. Chr.), Auszug Mohammeds (622), mechanische Uhr (um 1400), Mondlandung (1969; Zusatzwissen, nicht aus Heft oder Buch).",
                    tipp="Zuerst die Jahre v. Chr. (größere Zahl zuerst), dann die Jahre n. Chr."),
        luecke("Ergänze die Epochen.",
               "Ötzi lebte in der {{Ur- und Frühgeschichte}}. Der Tod Caesars (44 v. Chr.) liegt in der {{Antike}}. Der Auszug Mohammeds aus Mekka (622 n. Chr.) liegt im {{Mittelalter}}. Die erste Mondlandung (1969) gehört zur {{Neuzeit}}.",
               s, extra=["Altertum", "Eiszeit"],
               info="Jahr mit den Grenzen vergleichen: vor 3000 v. Chr., 1000 v. Chr. bis 500 n. Chr., 500 bis 1500, nach 1500. Die Mondlandung ist Zusatzwissen, nicht aus Heft oder Buch."),
    ]


def b_block_d():
    s = "D – Zeitstrahl lesen"
    img_ep = svg_epochen(nummern=True, jahre=False)
    alt_ep = "Fünf farbige Balken nebeneinander, von links nach rechts mit den Nummern 1 bis 5 versehen. Sie zeigen die fünf Epochen in zeitlicher Reihenfolge."
    pk = [("A", -80), ("B", -40), ("C", 10), ("D", 40)]
    img_p = svg_zeitstrahl_punkte(pk)
    alt_p = "Zeitstrahl von 100 v. Chr. bis 50 n. Chr. mit den vier Punkten A, B, C und D. Zwischen den beschrifteten Strichen liegt alle 10 Jahre ein kleiner Strich."
    img_b = svg_zeitstrahl_punkte([], bereiche=[("E", -50, 0), ("F", 30, 40)])
    alt_b = "Zeitstrahl von 100 v. Chr. bis 50 n. Chr. mit zwei farbigen Bereichen E und F über der Linie."
    assert ep_jahr(0) == NAMEN[2] and NAMEN.index("Neuzeit") + 1 == 5
    d = dict(pk)
    assert spanne(d["A"], d["C"]) == 90 and d["B"] < 0 < d["C"] < d["D"]
    return [
        mc("Welche Nummer trägt im Bild die Epoche, die um 1500 n. Chr. beginnt?", "5", ["2", "3", "4"], s, bild=img_ep, bildAlt=alt_ep,
           info="Um 1500 n. Chr. beginnt die Neuzeit. Sie ist die fünfte und jüngste Epoche, ganz rechts.",
           tipp="Die Nummern gehen vom ältesten zum jüngsten."),
        zuordnen("Welche Epoche trägt welche Nummer im Bild?", [(f"Nummer {i + 1}", NAMEN[i]) for i in range(5)], s, bild=img_ep, bildAlt=alt_ep,
                 info="Links liegt das Älteste, rechts das Jüngste: 1 Ur- und Frühgeschichte, 2 Altertum, 3 Antike, 4 Mittelalter, 5 Neuzeit."),
        mc("Welche Nummer trägt im Bild die Epoche, in der Christi Geburt liegt?", "3", ["2", "4", "5"], s, bild=img_ep, bildAlt=alt_ep,
           info="Christi Geburt liegt zwischen 1000 v. Chr. und 500 n. Chr. Das ist die Antike, Nummer 3.",
           tipp="Liegt Christi Geburt vor oder nach 1000 v. Chr., und vor oder nach 500 n. Chr.?"),
        kurz("Welches Jahr zeigt der Punkt B auf dem Zeitstrahl?", jahr_antw(d["B"]), s, bild=img_p, bildAlt=alt_p,
             info="Der Punkt B liegt links von Christi Geburt, vier Striche (40 Jahre) davor: 40 v. Chr.",
             tipp="Zähle die Striche von Christi Geburt aus. Zwischen zwei Strichen liegen 10 Jahre."),
        kurz("Wie viele Jahre liegen zwischen Punkt A und Punkt C? Rechne wie in der Schule (ohne Jahr 0).", zahl_antw(90), s, bild=img_p, bildAlt=alt_p, einheit="Jahre",
             info="A liegt bei 80 v. Chr., C bei 10 n. Chr. Über Christi Geburt hinweg zählst du zusammen: 80 + 10 = 90 Jahre."),
        mc("Wähle alle Punkte, die vor Christi Geburt liegen.", ["Punkt A", "Punkt B"], ["Punkt C", "Punkt D"], s, bild=img_p, bildAlt=alt_p,
           info="Links von Christi Geburt liegen die Jahre v. Chr. Das sind A und B."),
        tf("Das Ereignis D liegt auf dem Zeitstrahl rechts von C. Es geschah also später.", True, s, bild=img_p, bildAlt=alt_p,
           info="Auf einem Zeitstrahl liegt das Spätere weiter rechts."),
        luecke("Ergänze den Text über den Zeitstrahl.",
               "Ein Zeitstrahl stellt Ereignisse in ihrer zeitlichen {{Abfolge}} dar. Links liegt das {{Frühere}}, rechts das {{Spätere}}. Der Nullpunkt ist {{Christi Geburt}}.",
               s, extra=["Lautstärke", "Mondphase"],
               info="Auf einem Zeitstrahl liest du von links nach rechts: früher, dann später. Bei Christi Geburt wechseln v. Chr. und n. Chr."),
        mc("Welchen Zeitraum zeigt der Bereich E?", "50 v. Chr. bis Christi Geburt", ["Christi Geburt bis 50 n. Chr.", "100 v. Chr. bis 50 v. Chr.", "50 v. Chr. bis 50 n. Chr."], s,
           bild=img_b, bildAlt=alt_b,
           info="E beginnt beim Strich 50 v. Chr. und endet bei Christi Geburt. Das ist die zweite Hälfte des 1. Jahrhunderts v. Chr."),
        mc("Welche Jahre zeigt der Bereich F?", "30 bis 40 n. Chr.", ["20 bis 30 n. Chr.", "30 bis 40 v. Chr.", "3 bis 4 n. Chr."], s,
           bild=img_b, bildAlt=alt_b,
           info="F liegt rechts von Christi Geburt, also n. Chr. Er beginnt beim Strich 30 und endet beim Strich 40.",
           tipp="Rechts von Christi Geburt sind die Jahre n. Chr."),
    ]


def b_block_e():
    s = "E – Zeitstrahl zeichnen und Maßstab"
    cm = lambda j, pro=10: j / pro
    assert cm(80) == 8 and cm(spanne(-100, 50)) == 15 and cm(65, 0.1) == 650 and round(cm(spanne(-100, -27)), 1) == 7.3
    assert cm(spanne(-100, 20)) == 12 and cm(spanne(500, 1500), 100) == 10
    ruler = svg_lineal()
    alt_r = "Lineal von 0 bis 15 cm mit den Jahren 100 v. Chr. (0 cm), 50 v. Chr. (5 cm), Christi Geburt (10 cm) und 50 n. Chr. (15 cm)."
    return [
        kurz("Du zeichnest einen Zeitstrahl mit dem Maßstab 10 Jahre = 1 cm. Wie viele cm sind 80 Jahre?", zahl_antw(8, "cm"), s, einheit="cm",
             info="80 Jahre : 10 = 8 cm. Je 10 Jahre ist 1 cm."),
        mc("Wie lang ist ein Zeitstrahl von 100 v. Chr. bis 50 n. Chr. bei 10 Jahre = 1 cm?", "15 cm", ["10 cm", "5 cm", "150 cm"], s,
           info="Von 100 v. Chr. bis 50 n. Chr. sind es 100 + 50 = 150 Jahre. 150 : 10 = 15 cm."),
        kurz("Zwei Ereignisse liegen auf dem Zeitstrahl 6,5 cm auseinander (10 Jahre = 1 cm). Wie viele Jahre liegen dazwischen?", zahl_antw(65), s, einheit="Jahre",
             info="6,5 cm × 10 Jahre = 65 Jahre.", tipp="Jeder Zentimeter sind 10 Jahre."),
        kurz("Der Zeitstrahl beginnt bei 100 v. Chr. (0 cm). Bei wie viel cm liegt das Jahr 27 v. Chr.?", zahl_antw(7.3, "cm"), s, einheit="cm", bild=ruler, bildAlt=alt_r,
             info="Von 100 v. Chr. bis 27 v. Chr. sind es 100 − 27 = 73 Jahre. 73 : 10 = 7,3 cm.",
             tipp="Rechne zuerst, wie viele Jahre nach dem Anfang das Jahr liegt."),
        mc("Auf demselben Zeitstrahl (Anfang 100 v. Chr. bei 0 cm): Bei wie viel cm liegt das Jahr 20 n. Chr.?", "12 cm", ["8 cm", "2 cm", "10 cm"], s, bild=ruler, bildAlt=alt_r,
           info="Von 100 v. Chr. bis 20 n. Chr. sind es 100 + 20 = 120 Jahre. 120 : 10 = 12 cm.",
           tipp="Über Christi Geburt hinweg zählst du zusammen."),
        mc("Der Maßstab ist 1 cm = 100 Jahre. Wie lang ist der Zeitstrahl von 500 bis 1500 n. Chr. (das Mittelalter)?", "10 cm", ["1 cm", "100 cm", "15 cm"], s,
           info="Das Mittelalter dauert 1500 − 500 = 1000 Jahre. 1000 : 100 = 10 cm."),
        reihenfolge("Ordne die Schritte beim Zeichnen eines Zeitstrahls.",
                    ["Anfang und Ende festlegen und die Länge berechnen", "Eine Linie in dieser Länge zeichnen", "Alle 10 Jahre einen Strich setzen",
                     "Wichtige Jahreszahlen an die Striche schreiben", "Ereignisse an der richtigen Stelle eintragen"], s,
                    info="Erst die Länge, dann die Linie mit Strichen, dann die Beschriftung, zuletzt die Ereignisse."),
        luecke("Ergänze die Rechnungen beim Maßstab 10 Jahre = 1 cm.",
               "100 Jahre sind {{10}} cm lang. 150 Jahre sind {{15}} cm lang. 30 Jahre sind {{3}} cm lang.",
               s, extra=["1", "100"],
               info="Zentimeter = Jahre : 10. 100 : 10 = 10, 150 : 10 = 15, 30 : 10 = 3."),
    ]


def b_block_f():
    s = "F – Abstände und Reihenfolgen"
    lang = {"Altertum": spanne(-3000, -1000), "Antike": spanne(-1000, 500), "Mittelalter": spanne(500, 1500)}
    assert min(lang, key=lang.get) == "Mittelalter" and lang == {"Altertum": 2000, "Antike": 1500, "Mittelalter": 1000}
    a1, a2, a3, a5 = spanne(-1000, -44), spanne(-44, 622), spanne(622, 1400), spanne(-9000, -3000)
    assert (a1, a2, a3, a5) == (956, 666, 778, 6000) and a2 == 44 + 622
    neu = [("Feuer nutzen (vor ca. 1,5 Mio. Jahren)", -1_500_000), ("Feuer selbst erzeugen (vor ca. 150 000 Jahren)", -150_000),
           ("Sesshaft werden, Ackerbau beginnt (um 9000 v. Chr.)", -9000), ("Keramik (seit ca. 7000 v. Chr.)", -7000),
           ("Pflug in Mitteleuropa (ca. 4500 v. Chr.)", -4500)]
    assert [y for _, y in neu] == sorted(y for _, y in neu)
    return [
        kurz("Die Antike beginnt etwa 1000 v. Chr. Etwa wie viele Jahre später starb Julius Caesar (44 v. Chr.)?", zahl_antw(a1, ca=True) + ["950", "ca. 950", "etwa 950", "ungefähr 950"], s, einheit="Jahre",
             info="Beide Jahre liegen vor Christi Geburt. Du ziehst ab: 1000 − 44 = 956 Jahre. Weil die Epochengrenze nur ungefähr gilt, ist das Ergebnis ungefähr.",
             tipp="Beide Jahre haben „v. Chr.“."),
        kurz("Wie viele Jahre liegen zwischen dem Tod Julius Caesars (44 v. Chr.) und dem Auszug Mohammeds aus Mekka (622 n. Chr.)? Rechne wie in der Schule (ohne Jahr 0).",
             zahl_antw(a2), s, einheit="Jahre",
             info="Das eine Ereignis liegt vor, das andere nach Christi Geburt. Du zählst zusammen: 44 + 622 = 666 Jahre."),
        kurz("Etwa wie viele Jahre liegen zwischen dem Auszug Mohammeds aus Mekka (622 n. Chr.) und den ersten mechanischen Uhren in Deutschland (um 1400)?",
             zahl_antw(a3, ca=True), s, einheit="Jahre",
             info="Beide Jahre liegen nach Christi Geburt: 1400 − 622 = 778 Jahre. Weil die mechanische Uhr nur „um“ 1400 datiert ist, ist das Ergebnis ungefähr.",
             tipp="Beide Jahre haben „n. Chr.“."),
        mc("Welche dieser drei Epochen dauerte am kürzesten?", "Mittelalter", ["Altertum", "Antike"], s,
           info="Mittelalter: 1000 Jahre (500 bis 1500). Antike: 1500 Jahre (1000 v. Chr. bis 500 n. Chr.). Altertum: 2000 Jahre (3000 bis 1000 v. Chr.).",
           tipp="Rechne die Dauer jeder Epoche aus."),
        kurz("Die Jungsteinzeit dauerte etwa von 9000 bis 3000 v. Chr. Wie viele Jahre waren das ungefähr?",
             zahl_antw(a5, ca=True), s, einheit="Jahre",
             info="Beide Jahre liegen vor Christi Geburt. Du ziehst ab: 9000 − 3000 = 6000 Jahre. Die Jungsteinzeit war also sehr lang."),
        mc("Wofür ist ein Zeitstrahl gut?", "Er zeigt Ereignisse in ihrer zeitlichen Abfolge.",
           ["Er zeigt, wie weit Orte voneinander entfernt sind.", "Er zeigt, wo ein Ereignis stattgefunden hat.", "Er zeigt, wie viele Menschen zu einer Zeit lebten."], s,
           info="Auf dem Zeitstrahl liegt das Frühere links und das Spätere rechts. So sieht man, was zuerst geschah und wie weit zwei Ereignisse auseinanderliegen.",
           ),
        reihenfolge("Ordne diese Neuerungen der Steinzeit nach der Zeit. Das Älteste steht oben. (Den Stoff kennst du aus den Aufgaben zur Alt- und Jungsteinzeit.)", [n for n, _ in neu], s,
                    info="Feuer nutzen (vor ca. 1,5 Mio. Jahren), selbst erzeugen (vor ca. 150 000 Jahren), sesshaft werden (um 9000 v. Chr.), Keramik (ca. 7000 v. Chr.), Pflug (ca. 4500 v. Chr.).",
                    tipp="Zuerst die Zeiten „vor Jahren“, dann die Jahre v. Chr. mit der größeren Zahl zuerst."),
    ]


def b_block_g():
    s = "G – Klausurnah: Epochen und Zeitstrahl"
    g1 = "; ".join(f"{i + 1}. {NAMEN[i]}{' (MA)' if NAMEN[i] == 'Mittelalter' else ' (NZ)' if NAMEN[i] == 'Neuzeit' else ''}: {zeitraum(i)}" for i in range(5))
    # Zeitstrahl 1000 v. Chr. bis 2000 n. Chr., 1 cm = 100 Jahre
    pos = lambda y: (y - (-1000)) / 100
    assert (pos(-1000), pos(0), pos(500), pos(1500), pos(2000)) == (0, 10, 15, 25, 30) and spanne(-1000, 2000) / 100 == 30
    # Buchaufgabe: 100 v. Chr. bis 50 n. Chr., 10 Jahre = 1 cm
    p10 = lambda y: (y + 100) / 10
    assert (spanne(-100, 50) / 10, p10(-50), p10(0), round(p10(-44), 1), p10(30), round(p10(39), 1)) == (15, 5, 10, 5.6, 13, 13.9)
    ev = [("Gründung Roms", "rom"), ("Ötzi", "oetzi"), ("Tod Julius Caesars", "caesar"), ("Auszug Mohammeds aus Mekka", "mohammed"),
          ("erste Mondlandung", "mond"), ("Bau der großen Pyramide von Gizeh", "pyramide")]
    return [
        les(frei("Nenne die fünf Epochen in der richtigen Reihenfolge mit ihren Jahreszahlen und den Abkürzungen für Mittelalter und Neuzeit.",
                 g1 + ".",
                 ["alle fünf Epochen genannt", "in der richtigen Reihenfolge (vom ältesten zum jüngsten)", "Grenzen richtig: 3000 v. Chr., 1000 v. Chr., 500 n. Chr., 1500 n. Chr.", "Abkürzungen MA und NZ richtig"],
                 4, s), [M1, M2]),
        les(frei("Zeichne auf Papier einen Zeitstrahl von 1000 v. Chr. bis 2000 n. Chr. (1 cm = 100 Jahre) und trage Antike, Mittelalter und Neuzeit ein. Schreibe hier auf, wie lang dein Zeitstrahl ist und bei wie viel cm die Epochengrenzen liegen.",
                 "Der Zeitstrahl ist 3000 Jahre : 100 = 30 cm lang. 1000 v. Chr. liegt bei 0 cm (Beginn der Antike), Christi Geburt bei 10 cm, 500 n. Chr. bei 15 cm (Ende der Antike, Beginn des Mittelalters), "
                 "1500 n. Chr. bei 25 cm (Beginn der Neuzeit) und 2000 n. Chr. bei 30 cm. Die Antike reicht also von 0 bis 15 cm, das Mittelalter von 15 bis 25 cm und die Neuzeit von 25 bis 30 cm.",
                 ["Länge 30 cm richtig berechnet", "Epochengrenzen bei 0, 15, 25 cm richtig", "Antike, Mittelalter und Neuzeit in der richtigen Reihenfolge eingetragen", "Zeitstrahl beschriftet"], 4, s,
                 tipp="Zentimeter = Jahre : 100. Zähle ab 1000 v. Chr. (0 cm)."), [M6, M2]),
        les(frei("Zeichne auf Papier einen Zeitstrahl von 100 v. Chr. bis 50 n. Chr. (10 Jahre = 1 cm). Trage ein: die zweite Hälfte des 1. Jahrhunderts v. Chr., das Todesjahr Julius Caesars (44 v. Chr.) und das 4. Jahrzehnt des 1. Jahrhunderts n. Chr. (30 bis 39 n. Chr.). Schreibe auf, wie lang der Zeitstrahl ist und bei wie viel cm vom linken Ende die Einträge liegen.",
                 "Der Zeitstrahl ist 150 Jahre : 10 = 15 cm lang. Die zweite Hälfte des 1. Jahrhunderts v. Chr. (50 v. Chr. bis Christi Geburt) reicht von 5 cm bis 10 cm. "
                 "Das Todesjahr Caesars (44 v. Chr.) liegt 56 Jahre nach dem Anfang, also bei 5,6 cm. Das 4. Jahrzehnt (30 bis 39 n. Chr.) reicht von 13 cm bis 13,9 cm.",
                 ["Länge 15 cm richtig", "zweite Hälfte des 1. Jh. v. Chr.: 5 bis 10 cm", "Caesar bei 5,6 cm", "30 bis 39 n. Chr.: 13 bis etwa 14 cm", "Zeitstrahl mit Strichen und Jahreszahlen beschriftet"], 5, s,
                 tipp="Rechne bei jedem Eintrag: Jahre seit 100 v. Chr., geteilt durch 10. Ein Jahrzehnt sind 10 Jahre."), [M6, M5]),
        les(mc("Wähle alle richtigen Aussagen.",
               ["Die Antike reicht von 1000 v. Chr. bis 500 n. Chr.", "Ötzi lebte in der Ur- und Frühgeschichte.", "MA ist die Abkürzung für Mittelalter."],
               ["Die Neuzeit endete um 1500 n. Chr.", "Das Altertum kommt zeitlich nach der Antike."], s,
               info="Die Neuzeit beginnt um 1500 n. Chr. und dauert bis heute. Das Altertum (3000 bis 1000 v. Chr.) liegt vor der Antike."), [M1, M3, M4]),
        les(zuordnen("Ordne die Ereignisse den Epochen zu. Diesmal stehen keine Jahreszahlen dabei.", [(n, EV_EP[k]) for n, k in ev], s,
                     info="Ötzi lebte vor 3000 v. Chr., Rom (753 v. Chr.) und Caesar (44 v. Chr.) gehören zur Antike, Mohammeds Auszug (622) ins Mittelalter. Die Pyramide (um 2500 v. Chr., Altertum) und die Mondlandung (1969, Neuzeit) sind Zusatzwissen, nicht aus Heft oder Buch."), M4),
        les(kurz("Wie heißt die Epoche, die etwa 1500 n. Chr. beginnt und bis heute dauert?", ep_antw("Neuzeit"), s,
                 info="Die Neuzeit beginnt etwa 1500 n. Chr. Die Abkürzung ist NZ."), M1),
    ]


def les_by(aufgaben, anfang, titel):
    """Setzt das Feld lesen bei genau der Aufgabe, deren Frage mit anfang beginnt."""
    t = [x for x in aufgaben if x["frage"].startswith(anfang)]
    assert len(t) == 1, (anfang, len(t))
    t[0]["lesen"] = titel


def aufgaben_b():
    A = b_block_a() + b_block_b() + b_block_c() + b_block_d() + b_block_e() + b_block_f() + b_block_g()
    les_by(A, "Welche dieser drei Epochen dauerte am kürzesten", M2)
    les_by(A, "Wofür ist ein Zeitstrahl gut", M5)
    les_by(A, "Ordne diese Neuerungen der Steinzeit", M3)
    les_by(A, "Wähle alle Jahre, die zur Antike gehören", M3)
    return A


def paket_b():
    p = pack("geschichte-2b-epochen-zeitstrahl", "Geschichte Teil 2b: Epochen und Zeitstrahl",
             "Die fünf Epochen mit Namen und Daten, Jahre und Ereignisse den Epochen zuordnen, Zeitstrahl lesen und zeichnen, Abstände berechnen. Mit Lernblatt und vielen Übungsaufgaben.",
             lernblatt_b(), aufgaben_b(), min_aufgaben=45,
             hinweis="Die Epochengrenzen gelten nur ungefähr („ca.“). Ereignisse mit „Zusatzwissen“ im Lernblatt gehen über das Heft hinaus.")
    nachlesen(p, {
        "A – Die fünf Epochen kennen": [M1, M2],
        "B – Die Epoche eines Jahres bestimmen": M3,
        "C – Ereignisse den Epochen zuordnen": M4,
        "D – Zeitstrahl lesen": [M5, M6],
        "E – Zeitstrahl zeichnen und Maßstab": M6,
        "F – Abstände und Reihenfolgen": [M7, M5],
        "G – Klausurnah: Epochen und Zeitstrahl": [M1, M2, M3, M4, M5, M6, M7],
    })
    p["probe"] = False
    return p


def build():
    return [paket_a(), paket_b()]
