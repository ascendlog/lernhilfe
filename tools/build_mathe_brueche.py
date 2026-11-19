#!/usr/bin/env python3
"""Erzeugt das Kurzpaket „Mathe Klasse 6: Minitest Brüche“ (Erweitern, Kürzen, Vergleichen) für Joel und Dario.

Aufruf: python3 tools/build_mathe_brueche.py

Abgespeckte Form für einen Minitest (kein Vollpaket): ein Paket mit kurzem Lernblatt und rund 35 Übungsaufgaben,
keine eigene Probearbeit, kein eigener Crashkurs (Lernblatt-Abschnitt „Checkliste und Tipps“ übernimmt das).
Alle Rechnungen laufen über fractions.Fraction und werden mit assert geprüft.
Datenschutz: Das Repository ist öffentlich. Alle Namen in Aufgaben (Mia, Ben, Lena, Tim, Anna) sind erfunden.
"""
import json
import os
import sys
from fractions import Fraction

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
OUT = os.path.join(HIER, '..', 'pakete', 'joel-dario')

from mathe_lib import *   # noqa: E402,F401,F403
from repo_ziel import ziel, hat_eintrag   # noqa: E402,F401

ID = 'mathe-minitest-brueche'
TERMIN = '2026-11-24'   # Minitest (Dienstag), von Alessandro genannt
KARTE = {'titel': 'Bruchmeister', 'motiv': '🍕',
         'text': 'Brüche erweitern, kürzen und vergleichen: Der Wert bleibt gleich, nur die Stücke werden feiner oder gröber.'}

T1 = 'Gleichwertige Brüche: Erweitern und Kürzen'
T2 = 'Brüche erweitern'
T3 = 'Brüche kürzen'
T4 = 'Brüche vergleichen'
T5 = 'Checkliste und Tipps für den Minitest'

A = 'A – Brüche erweitern'
B = 'B – Brüche kürzen'
C = 'C – Brüche vergleichen'
D = 'D – Minitest-Mix'


def fr(z, n):
    return f'{z}/{n}'


def erw(z, n, k):
    """Erweitern: (z·k, n·k), der Wert muss gleich bleiben."""
    assert k > 1
    assert Fraction(z * k, n * k) == Fraction(z, n)
    return z * k, n * k


def kue(z, n, k):
    """Kürzen durch k: (z:k, n:k), k muss beide teilen."""
    assert k > 1 and z % k == 0 and n % k == 0, (z, n, k)
    assert Fraction(z // k, n // k) == Fraction(z, n)
    return z // k, n // k


def voll(z, n):
    """Vollständig gekürzt: (Zähler, Nenner, ggT)."""
    g = ggt(z, n)
    return z // g, n // g, g


def vgl(a, b):
    """Vergleichszeichen für Fraction a gegen b."""
    return '<' if a < b else ('>' if a > b else '=')


def F(s):
    z, n = s.split('/')
    return Fraction(int(z), int(n))


# ---------------------------------------------------------------- Lernblatt

def lernblatt():
    return [
        lb(T1,
           'Ein Bruch besteht aus **Zähler** (oben), **Bruchstrich** und **Nenner** (unten). Der Nenner sagt, in wie viele gleich große Teile das Ganze geteilt ist. '
           'Der Zähler sagt, wie viele dieser Teile gemeint sind. Bei 3/4 ist das Ganze in 4 Teile geteilt und 3 davon sind gefärbt.\n\n'
           'Den **gleichen Anteil** kannst du mit ganz verschiedenen Brüchen aufschreiben. Die Hälfte ist 1/2, aber auch 2/4, 3/6 oder 4/8. '
           'Schau dir die Streifen an: Die gefärbte Länge ist immer gleich lang, nur die Stücke sind verschieden groß. '
           'Solche Brüche heißen **gleichwertig**: 1/2 = 2/4 = 3/6 = 4/8.\n\n'
           'Zwei Wege führen zu gleichwertigen Brüchen: **Erweitern** (feinere Stücke, mehr davon) und **Kürzen** (gröbere Stücke, weniger davon).',
           merke='Gleichwertige Brüche haben denselben Wert. Erweitern und Kürzen ändern nur die Stückelung, nicht den Anteil.',
           bild=svg_streifen([(1, 2), (2, 4), (3, 6), (4, 8)]),
           bildAlt='Vier gleich lange Streifen: 1/2, 2/4, 3/6 und 4/8. Bei allen ist die Hälfte gefärbt.'),
        lb(T2,
           '**Erweitern** heißt: Du multiplizierst (nimmst mal) **Zähler und Nenner mit derselben Zahl**. Die Zahl darf nicht 0 sein.\n\n'
           f'Beispiel: 3/4 mit 5 erweitern. 3 · 5 = {erw(3, 4, 5)[0]} und 4 · 5 = {erw(3, 4, 5)[1]}, also 3/4 = {fr(*erw(3, 4, 5))}.\n\n'
           '**Welche Zahl fehlt?** Beispiel: 2/3 = ?/12. Schau zuerst auf die Nenner: Von 3 zu 12 geht es mal 4 (3 · 4 = 12). '
           f'Dann muss auch der Zähler mal 4 genommen werden: 2 · 4 = {2 * 4}. Ergebnis: 2/3 = {fr(*erw(2, 3, 4))}.\n\n'
           '**Typische Fehler:** Du erweiterst nur den Nenner (3/4 → 3/20) oder du rechnest + statt · (3/4 → 8/9). Dann ändert sich der Wert.',
           merke='Erweitern: Zähler UND Nenner mal dieselbe Zahl. Der Bruch sieht anders aus, hat aber denselben Wert.',
           bild=svg_rechenweg(3, 4, '·', 5),
           bildAlt='3/4 wird mit 5 erweitert: Zähler und Nenner mal 5, Ergebnis 15/20.'),
        lb(T3,
           '**Kürzen** ist das Gegenteil von Erweitern: Du teilst **Zähler und Nenner durch dieselbe Zahl**. '
           'Diese Zahl muss in beide Zahlen genau hineinpassen (ein **gemeinsamer Teiler**).\n\n'
           f'Beispiel: 12/18 durch 6 kürzen. 12 : 6 = {kue(12, 18, 6)[0]} und 18 : 6 = {kue(12, 18, 6)[1]}, also 12/18 = {fr(*kue(12, 18, 6))}.\n\n'
           '**Vollständig gekürzt** ist ein Bruch, wenn man nicht mehr weiter kürzen kann, weil Zähler und Nenner außer 1 keinen gemeinsamen Teiler mehr haben. '
           'Beispiele: 2/3 und 7/12.\n\n'
           'Du siehst den größten gemeinsamen Teiler nicht gleich? Dann kürze in Schritten: '
           f'48/72 → durch 2 → {fr(*kue(48, 72, 2))} → durch 2 → {fr(*kue(24, 36, 2))} → durch 6 → {fr(*kue(12, 18, 6))}. '
           'Am Ende immer prüfen: Geht noch was?\n\n'
           '**Teilbarkeit hilft beim Suchen:**\n'
           '- durch 2 teilbar: letzte Ziffer 0, 2, 4, 6 oder 8\n'
           '- durch 3 teilbar: Quersumme durch 3 teilbar (57: 5 + 7 = 12, also ja)\n'
           '- durch 5 teilbar: letzte Ziffer 0 oder 5\n'
           '- durch 9 teilbar: Quersumme durch 9 teilbar\n'
           '- durch 10 teilbar: letzte Ziffer 0 (bei 30/50 streichst du in beiden Zahlen die Null weg: 3/5)\n\n'
           '**Typischer Fehler:** Du teilst nur den Zähler (18/24 → 9/24). Dann stimmt der Wert nicht mehr.',
           merke='Kürzen: Zähler UND Nenner durch dieselbe Zahl teilen. Danach prüfen, ob man noch weiter kürzen kann.',
           bild=svg_rechenweg(12, 18, ':', 6),
           bildAlt='12/18 wird durch 6 gekürzt: Zähler und Nenner geteilt durch 6, Ergebnis 2/3.'),
        lb(T4,
           'Beim Vergleichen schreibst du < (kleiner als), > (größer als) oder = (gleich). Es gibt drei Fälle:\n\n'
           '**1. Gleicher Nenner:** Die Stücke sind gleich groß. Dann ist der Bruch mit dem **größeren Zähler** größer. Beispiel: 5/8 > 3/8.\n\n'
           '**2. Gleicher Zähler:** Du hast gleich viele Stücke, aber die Stücke sind verschieden groß. Je **größer der Nenner**, desto kleiner die Stücke. '
           'Beispiel: 1/3 > 1/5 (Drittel sind größer als Fünftel).\n\n'
           '**3. Verschiedene Nenner:** Mache die Brüche erst **gleichnamig**. Das heißt, du erweiterst sie auf denselben Nenner. '
           'Am besten nimmst du den kleinsten Nenner, in den beide Nenner hineinpassen (den **Hauptnenner**). Dann vergleichst du die Zähler wie im Fall 1.\n\n'
           f'Beispiel: 3/4 und 5/6. Der Hauptnenner ist 12. 3/4 = {fr(*erw(3, 4, 3))} und 5/6 = {fr(*erw(5, 6, 2))}. '
           f'Weil {3 * 3}/12 < {5 * 2}/12 ist, gilt 3/4 < 5/6.\n\n'
           '**Hauptnenner finden:** Zähle die Vielfachen des größeren Nenners auf (6, 12, 18 …), bis eine Zahl dabei ist, die auch der andere Nenner teilt (4 passt in 12). '
           'Findest du nichts Schnelles, multipliziere die beiden Nenner (4 · 6 = 24). Das klappt immer, nur sind die Zahlen größer.\n\n'
           '**Der Größe nach ordnen:** Bringe alle Brüche auf denselben Nenner und ordne dann die Zähler.',
           merke='Gleicher Nenner: größerer Zähler gewinnt. Gleicher Zähler: kleinerer Nenner gewinnt. Verschiedene Nenner: erst gleichnamig machen.',
           bild=svg_zahlenstrahl12([F('1/4'), F('1/3'), F('1/2'), F('2/3'), F('3/4'), F('5/6')]),
           bildAlt='Zahlenstrahl von 0 bis 1 in Zwölfteln. 1/4 liegt bei 3/12, 1/3 bei 4/12, 1/2 bei 6/12, 2/3 bei 8/12, 3/4 bei 9/12 und 5/6 bei 10/12. Je weiter rechts, desto größer.'),
        lb(T5,
           '**Ich kann:**\n\n'
           '- erklären, was Zähler und Nenner sind\n'
           '- einen Bruch erweitern (Zähler und Nenner mal dieselbe Zahl)\n'
           '- die fehlende Zahl bei 2/3 = ?/12 finden\n'
           '- einen Bruch kürzen und vollständig kürzen\n'
           '- mit den Teilbarkeitsregeln sehen, ob ich noch kürzen kann\n'
           '- Brüche mit gleichem Nenner, mit gleichem Zähler und mit verschiedenen Nennern vergleichen\n'
           '- Brüche gleichnamig machen und der Größe nach ordnen\n'
           '- die Zeichen <, > und = richtig setzen\n\n'
           '**Tipps für die Arbeit:**\n\n'
           '- Lies jede Aufgabe zweimal. Steht da erweitern (mal) oder kürzen (geteilt)?\n'
           '- Schreibe die Zwischenschritte auf, auch wenn du sie im Kopf rechnest.\n'
           '- Mache die Probe: Einen erweiterten Bruch kannst du wieder kürzen, einen gekürzten wieder erweitern. Kommst du beim Anfang an, stimmt es.\n'
           '- Beim Kürzen am Ende fragen: Geht noch was?\n'
           '- Haben die Brüche verschiedene Nenner? Dann zuerst gleichnamig machen.',
           merke='Erweitern = mal, Kürzen = geteilt, beides mit Zähler und Nenner. Vergleichen geht am sichersten mit gleichem Nenner.'),
    ]


# ---------------------------------------------------------------- Aufgaben

def bl_a():
    t = []
    # A1: erweitern mit 5
    z, n, k = 3, 4, 5
    z2, n2 = erw(z, n, k)
    falsch = [fr(z + k, n + k), fr(z, n2), fr(z2, n)]
    for f in falsch:
        assert F(f) != Fraction(z, n)
    t.append(mc(f'Du erweiterst {fr(z, n)} mit {k}. Welcher Bruch entsteht?', fr(z2, n2), falsch, A,
                info=f'Zähler und Nenner werden mit {k} multipliziert: {z} · {k} = {z2} und {n} · {k} = {n2}. '
                     f'Addieren ({fr(z + k, n + k)}) oder nur eine Zahl ändern ({fr(z, n2)}, {fr(z2, n)}) verändert den Wert.'))
    # A2: einfach
    z, n, k = 2, 5, 3
    z2, n2 = erw(z, n, k)
    t.append(luecke(f'Erweitere {fr(z, n)} mit {k}. Schreibe Zähler und Nenner in die Felder.', f'{fr(z, n)} = {{{{{z2}}}}}/{{{{{n2}}}}}', A, wortbank=False,
                    info=f'{z} · {k} = {z2} und {n} · {k} = {n2}.'))
    # A3: drei Brüche
    items = [(1, 3, 4), (5, 6, 2), (3, 7, 5)]
    zeilen = []
    for i, (z, n, k) in enumerate(items):
        z2, n2 = erw(z, n, k)
        zeilen.append(f'{"abc"[i]}) {fr(z, n)} mit {k} erweitern: {fr(z, n)} = {{{{{z2}}}}}/{{{{{n2}}}}}')
    t.append(luecke('Erweitere mit der angegebenen Zahl.', '\n'.join(zeilen), A, wortbank=False,
                    info='Immer Zähler und Nenner mit derselben Zahl multiplizieren. ' +
                         ' '.join(f'{fr(z, n)} mit {k}: {z} · {k} = {z * k}, {n} · {k} = {n * k}.' for z, n, k in items)))
    # A4: mit welcher Zahl?
    z, n, k = 3, 8, 7
    z2, n2 = erw(z, n, k)
    assert n2 // n == k
    t.append(kurz(f'Mit welcher Zahl wurde erweitert? {fr(z, n)} = {fr(z2, n2)}', str(k), A,
                  tipp='Teile den neuen Nenner durch den alten Nenner.',
                  info=f'{n2} : {n} = {k}. Zur Probe: {z} · {k} = {z2}. Es wurde mit {k} erweitert.'))
    # A5: fehlende Zahlen
    teile = []
    infos = []
    for (z, n, k), fehlt in [((2, 3, 4), 'z'), ((5, 6, 4), 'n'), ((4, 9, 3), 'z')]:
        z2, n2 = erw(z, n, k)
        if fehlt == 'z':
            teile.append(f'{fr(z, n)} = {{{{{z2}}}}}/{n2}')
        else:
            teile.append(f'{fr(z, n)} = {z2}/{{{{{n2}}}}}')
        infos.append(f'{fr(z, n)} = {fr(z2, n2)} (erweitert mit {k})')
    t.append(luecke('Welche Zahl fehlt? Ergänze so, dass die Brüche gleichwertig sind.',
                    '\n'.join(f'{"abc"[i]}) {x}' for i, x in enumerate(teile)), A, wortbank=False,
                    tipp='Finde zuerst heraus, mit welcher Zahl erweitert wurde.',
                    info='Schau, mit welcher Zahl erweitert wurde, und rechne dann die fehlende Zahl aus: ' + '; '.join(infos) + '.'))
    # A6: nicht gleichwertig
    basis = Fraction(2, 3)
    richtig = '8/10'
    falsch = ['4/6', '6/9', '10/15']
    assert F(richtig) != basis and all(F(f) == basis for f in falsch)
    t.append(mc('Welcher Bruch ist NICHT gleichwertig zu 2/3?', richtig, falsch, A,
                info='2/3 = 4/6 (mit 2 erweitert), 2/3 = 6/9 (mit 3) und 2/3 = 10/15 (mit 5). '
                     'Bei 8/10 passt es nicht: 8/10 kürzt man zu 4/5, und 4/5 ist nicht 2/3 (2/3 wäre 8/12).'))
    # A7: zuordnen mit Nenner 12
    paare = [('1/2', '6/12'), ('1/3', '4/12'), ('3/4', '9/12'), ('5/6', '10/12'), ('1/4', '3/12')]
    for a, b in paare:
        assert F(a) == F(b) and F(b).denominator <= 12 and b.endswith('/12')
    assert len({b for _, b in paare}) == len(paare)
    t.append(zuordnen('Ordne jedem Bruch den gleichwertigen Bruch mit dem Nenner 12 zu.', paare, A, extra=['7/12'],
                      tipp='Mit welcher Zahl musst du den Nenner erweitern, damit 12 herauskommt?',
                      info='Du erweiterst jeden Bruch auf den Nenner 12: 1/2 mit 6 (6/12), 1/3 mit 4 (4/12), 3/4 mit 3 (9/12), 5/6 mit 2 (10/12) und 1/4 mit 3 (3/12). '
                           'Der Zähler wird immer mit derselben Zahl multipliziert wie der Nenner. 7/12 passt zu keinem der Brüche.'))
    # A8: Bild, erweitern
    assert erw(3, 4, 3) == (9, 12)
    t.append(luecke('Beide Streifen sind gleich lang. Der obere zeigt 3/4. Der untere Streifen ist in 12 Teile geteilt. '
                    'Schreibe auf, welchen Bruch der untere Streifen zeigt und mit welcher Zahl 3/4 erweitert wurde.',
                    '3/4 = {{9}}/{{12}} (erweitert mit {{3}})', A, wortbank=False,
                    bild=svg_streifen([(3, 4), (9, 12, None)]),
                    bildAlt='Zwei gleich lange Streifen. Oben: 4 Teile, 3 gefärbt (3/4). Unten: 12 Teile, 9 gefärbt.',
                    info='Der untere Streifen hat 12 Teile, 9 davon sind gefärbt: 9/12. Von 4 Teilen zu 12 Teilen: 4 · 3 = 12, also wurde mit 3 erweitert (3 · 3 = 9).'))
    return t


def bl_b():
    t = []
    # B1: kürzen mit 6
    z, n, k = 12, 18, 6
    z2, n2 = kue(z, n, k)
    falsch = [fr(z2, n), fr(z, n2), '6/12']
    for f in falsch:
        assert F(f) != Fraction(z, n)
    t.append(mc(f'Du kürzt {fr(z, n)} mit {k}. Welcher Bruch entsteht?', fr(z2, n2), falsch, B,
                info=f'Zähler und Nenner werden durch {k} geteilt: {z} : {k} = {z2} und {n} : {k} = {n2}. '
                     'Wer nur eine der beiden Zahlen teilt, ändert den Wert.'))
    # B2: einfach
    z, n, k = 15, 20, 5
    z2, n2 = kue(z, n, k)
    t.append(luecke(f'Kürze {fr(z, n)} durch {k}. Schreibe Zähler und Nenner in die Felder.', f'{fr(z, n)} = {{{{{z2}}}}}/{{{{{n2}}}}}', B, wortbank=False,
                    info=f'{z} : {k} = {z2} und {n} : {k} = {n2}.'))
    # B3: vollständig kürzen
    items = [(8, 12), (18, 30), (20, 32)]
    zeilen, infos = [], []
    for i, (z, n) in enumerate(items):
        z2, n2, g = voll(z, n)
        assert ggt(z2, n2) == 1
        zeilen.append(f'{"abc"[i]}) {fr(z, n)} = {{{{{z2}}}}}/{{{{{n2}}}}}')
        infos.append(f'{fr(z, n)} durch {g} = {fr(z2, n2)}')
    t.append(luecke('Kürze vollständig.', '\n'.join(zeilen), B, wortbank=False,
                    tipp='Wenn du nicht gleich die größte Zahl siehst: Kürze in kleinen Schritten, zum Beispiel erst durch 2.',
                    info='Vollständig gekürzt heißt: Zähler und Nenner haben keinen gemeinsamen Teiler mehr (außer 1). ' + '; '.join(infos) + '.'))
    # B4: durch welche Zahl gekürzt?
    z, n, k = 35, 45, 5
    z2, n2 = kue(z, n, k)
    t.append(kurz(f'Durch welche Zahl wurde gekürzt? {fr(z, n)} = {fr(z2, n2)}', str(k), B,
                  tipp='Teile den alten Nenner durch den neuen Nenner.',
                  info=f'{n} : {n2} = {k}. Zur Probe: {z} : {k} = {z2}. Es wurde durch {k} gekürzt.'))
    # B5: vollständig gekürzt?
    richtig, falsch = '7/12', ['9/12', '10/15', '14/21']
    assert ggt(7, 12) == 1 and all(ggt(*map(int, f.split('/'))) > 1 for f in falsch)
    t.append(mc('Welcher Bruch ist schon vollständig gekürzt?', richtig, falsch, B,
                info='9/12 lässt sich durch 3 kürzen (3/4), 10/15 durch 5 (2/3) und 14/21 durch 7 (2/3). '
                     '7/12 hat keinen gemeinsamen Teiler außer 1: Die 7 teilt die 12 nicht, die 12 hat nur die Teiler 1, 2, 3, 4, 6 und 12.'))
    # B6: tf wahr
    z2, n2 = kue(21, 28, 7)
    t.append(tf('Der Bruch 21/28 lässt sich durch 7 kürzen.', True, B,
                info=f'21 : 7 = {z2} und 28 : 7 = {n2}. Es ergibt {fr(z2, n2)}, und das ist vollständig gekürzt.'))
    # B7: zuordnen Teilbarkeit
    t.append(zuordnen('Woran erkennst du, dass eine Zahl durch … teilbar ist? Ordne zu.',
                      [('durch 2', 'letzte Ziffer ist 0, 2, 4, 6 oder 8'), ('durch 3', 'Quersumme ist durch 3 teilbar'),
                       ('durch 5', 'letzte Ziffer ist 0 oder 5'), ('durch 9', 'Quersumme ist durch 9 teilbar'),
                       ('durch 10', 'letzte Ziffer ist 0')], B, extra=['letzte Ziffer ist 1'],
                      tipp='Bei einer Regel zählt als letzte Ziffer nur die 0.',
                      info='Diese Regeln helfen dir, schnell einen gemeinsamen Teiler von Zähler und Nenner zu finden. '
                           'Bei 3 und 9 zählst du die Ziffern zusammen (Quersumme) und prüfst, ob die Summe in der 3er- bzw. 9er-Reihe steht. '
                           'Endet eine Zahl auf 0, ist sie durch 2, 5 und 10 teilbar. Hier gehört „letzte Ziffer ist 0“ zur 10, weil nur bei der 10 allein die 0 zählt.',
                      lesen=T3))
    # B8: Fehler finden
    t.append(mc('Tim kürzt 18/24 und schreibt: 18/24 = 9/24. Was hat er falsch gemacht?',
                'Er hat nur den Zähler durch 2 geteilt. Der Nenner muss auch durch 2 geteilt werden.',
                ['Er darf 18/24 gar nicht kürzen.', 'Er hätte mit 2 erweitern müssen.', 'Er hat nichts falsch gemacht.'], B,
                info=f'Beim Kürzen werden Zähler und Nenner durch dieselbe Zahl geteilt: 18 : 2 = 9 und 24 : 2 = 12, also {fr(*kue(18, 24, 2))}. '
                     '9/24 hat einen anderen Wert als 18/24. Vollständig gekürzt wäre sogar 3/4 (durch 6).'))
    # B9: Bild, kürzen
    assert kue(8, 12, 4) == (2, 3)
    t.append(luecke('Beide Streifen sind gleich lang. Der obere zeigt 8/12. Kürze den Bruch so, dass er zum unteren Streifen passt, und nenne die Zahl, durch die du gekürzt hast.',
                    '8/12 = {{2}}/{{3}} (gekürzt durch {{4}})', B, wortbank=False,
                    bild=svg_streifen([(8, 12), (2, 3, None)]),
                    bildAlt='Zwei gleich lange Streifen. Oben: 12 Teile, 8 gefärbt (8/12). Unten: 3 Teile, 2 gefärbt.',
                    info='Der untere Streifen hat 3 Teile, 2 davon sind gefärbt: 2/3. Von 12 Teilen zu 3 Teilen: 12 : 3 = 4, also wurde durch 4 gekürzt (8 : 4 = 2).'))
    return t


def symbole(paare_text):
    """Lückentext mit Vergleichszeichen: [(a, b)] mit a, b als 'z/n' -> 'a) a {{<}} b' (Zeichen im Code berechnet)."""
    zeilen = []
    for i, (a, b) in enumerate(paare_text):
        zeilen.append(f'{"abc"[i]}) {a} {{{{{vgl(F(a), F(b))}}}}} {b}')
    return '\n'.join(zeilen)


def bl_c():
    t = []
    # C1: gleicher Nenner
    paare = [('3/8', '5/8'), ('7/9', '4/9'), ('2/5', '3/5')]
    assert all(F(a).denominator == F(b).denominator for a, b in paare)
    t.append(luecke('Setze <, > oder = ein. Die Brüche haben denselben Nenner.', symbole(paare), C, extra=['='],
                    info='Gleicher Nenner heißt: gleich große Stücke. Der Bruch mit dem größeren Zähler hat mehr Stücke und ist größer. '
                         '3 < 5, 7 > 4 und 2 < 3.'))
    # C2: gleicher Zähler
    paare = [('1/4', '1/7'), ('3/5', '3/4'), ('5/6', '5/8')]
    assert all(F(a).numerator == F(b).numerator for a, b in paare)
    t.append(luecke('Setze <, > oder = ein. Die Brüche haben denselben Zähler.', symbole(paare), C, extra=['='],
                    tipp='Je größer der Nenner, desto kleiner sind die Stücke.',
                    info='Gleicher Zähler heißt: gleich viele Stücke, aber verschieden große. Der kleinere Nenner gibt die größeren Stücke, also den größeren Bruch. '
                         'Viertel sind größer als Siebtel, Fünftel kleiner als Viertel, Sechstel größer als Achtel.'))
    # C3: mc gleicher Zähler
    assert F('4/9') < F('4/7')
    t.append(mc('Welcher Bruch ist kleiner: 4/7 oder 4/9?', '4/9', ['4/7', 'Beide sind gleich groß.'], C,
                info='Gleicher Zähler: je größer der Nenner, desto kleiner die Stücke. Neuntel sind kleiner als Siebtel, also ist 4/9 < 4/7.'))
    # C4: gleichnamig machen mit Hauptnenner 12
    (z1, n1, k1), (z2, n2, k2) = (2, 3, 4), (3, 4, 3)
    a, b = erw(z1, n1, k1), erw(z2, n2, k2)
    assert a[1] == b[1] == 12
    t.append(luecke('Mache gleichnamig. Der Hauptnenner von 2/3 und 3/4 ist 12. Erweitere beide Brüche auf den Nenner 12.',
                    f'a) 2/3 = {{{{{a[0]}}}}}/12\nb) 3/4 = {{{{{b[0]}}}}}/12', C, wortbank=False,
                    info=f'2/3: von 3 nach 12 ist es mal {k1}, also 2 · {k1} = {a[0]}. 3/4: von 4 nach 12 ist es mal {k2}, also 3 · {k2} = {b[0]}. '
                         f'Weil {a[0]}/12 < {b[0]}/12 ist, gilt 2/3 < 3/4.'))
    # C5: ein Nenner ist ein Vielfaches des anderen
    paare = [('1/2', '5/8'), ('2/3', '5/9'), ('3/4', '9/12')]
    assert [vgl(F(a), F(b)) for a, b in paare] == ['<', '>', '=']
    t.append(luecke('Setze <, > oder = ein. Erweitere im Kopf oder auf dem Blatt.', symbole(paare), C,
                    tipp='Erweitere den Bruch mit dem kleineren Nenner auf den größeren Nenner.',
                    info='a) 1/2 = 4/8 und 4/8 < 5/8. b) 2/3 = 6/9 und 6/9 > 5/9. c) 3/4 = 9/12, beide Brüche sind gleichwertig.'))
    # C6: Hauptnenner nötig
    paare = [('3/4', '5/6'), ('2/5', '3/8'), ('5/6', '7/9')]
    assert [vgl(F(a), F(b)) for a, b in paare] == ['<', '>', '>']
    t.append(luecke('Setze <, > oder = ein. Mache zuerst gleichnamig.', symbole(paare), C,
                    tipp='Hauptnenner suchen: a) 12, b) 40, c) 18.',
                    info='a) 3/4 = 9/12 und 5/6 = 10/12, also 3/4 < 5/6. b) 2/5 = 16/40 und 3/8 = 15/40, also 2/5 > 3/8. '
                         'c) 5/6 = 15/18 und 7/9 = 14/18, also 5/6 > 7/9.'))
    # C7: größter Bruch
    opts = ['3/5', '7/10', '2/3', '3/4']
    werte = [F(x) for x in opts]
    assert max(werte) == F('3/4') and sorted(werte).count(max(werte)) == 1
    t.append(mc('Welcher dieser Brüche ist der größte?', '3/4', ['3/5', '7/10', '2/3'], C,
                tipp='Gemeinsamer Nenner kann 60 sein.',
                info='Auf den Nenner 60 erweitert: 3/5 = 36/60, 7/10 = 42/60, 2/3 = 40/60, 3/4 = 45/60. Der größte Zähler gehört zu 3/4.'))
    # C8: ordnen mit Nenner 6
    folge = ['1/3', '1/2', '2/3', '5/6']
    assert sorted(folge, key=F) == folge and len({F(x) for x in folge}) == 4
    t.append(reihenfolge('Ordne die Brüche der Größe nach. Der kleinste Bruch kommt zuerst.', folge, C,
                         tipp='Bringe alle auf den Nenner 6.',
                         info='Hauptnenner 6: 1/3 = 2/6, 1/2 = 3/6, 2/3 = 4/6, 5/6. Also 2/6 < 3/6 < 4/6 < 5/6.'))
    # C9: ordnen mit Nenner 20
    folge = ['13/20', '7/10', '3/4', '4/5']
    assert sorted(folge, key=F) == folge and len({F(x) for x in folge}) == 4
    t.append(reihenfolge('Ordne die Brüche mit verschiedenen Nennern der Größe nach. Beginne mit dem kleinsten.', folge, C,
                         tipp='Der Hauptnenner ist 20.',
                         info='Hauptnenner 20: 7/10 = 14/20, 3/4 = 15/20, 4/5 = 16/20, dazu 13/20. Also 13/20 < 14/20 < 15/20 < 16/20.'))
    # C10: Bild, zwei Streifen
    assert F('5/8') < F('2/3')
    t.append(mc('Die beiden Streifen sind gleich lang. Lies die Brüche am Bild ab und vergleiche sie. Welche Aussage stimmt?',
                '5/8 < 2/3', ['5/8 > 2/3', '5/8 = 2/3'], C,
                bild=svg_streifen([(5, 8, 'A'), (2, 3, 'B')]),
                bildAlt='Zwei gleich lange Streifen. A: 8 Teile, 5 gefärbt. B: 3 Teile, 2 gefärbt. B ist ein kleines Stück weiter gefärbt als A.',
                info='A zeigt 5/8, B zeigt 2/3. Mit Nenner 24: 5/8 = 15/24 und 2/3 = 16/24. Also 5/8 < 2/3. Der Unterschied ist klein, nur ein Vierundzwanzigstel.',
                lesen=[T1, T4]))
    return t


def bl_d():
    t = []
    # D1: erweitern
    z2, n2 = erw(5, 8, 6)
    t.append(luecke('Erweitere 5/8 mit 6.', f'5/8 = {{{{{z2}}}}}/{{{{{n2}}}}}', D, wortbank=False, lesen=T2,
                    info=f'5 · 6 = {z2} und 8 · 6 = {n2}.'))
    # D2: vollständig kürzen
    z2, n2, g = voll(36, 48)
    t.append(luecke('Kürze 36/48 vollständig.', f'36/48 = {{{{{z2}}}}}/{{{{{n2}}}}}', D, wortbank=False, lesen=T3,
                    tipp='Probiere erst die 2, dann siehst du weiter.',
                    info=f'Der größte gemeinsame Teiler ist {g}: 36 : {g} = {z2} und 48 : {g} = {n2}. Schrittweise geht es auch: 36/48 → 18/24 → 9/12 → 3/4.'))
    # D3: Vergleichszeichen gemischt
    paare = [('4/9', '3/7'), ('5/12', '1/2'), ('7/10', '14/20')]
    assert [vgl(F(a), F(b)) for a, b in paare] == ['>', '<', '=']
    t.append(luecke('Setze <, > oder = ein.', symbole(paare), D, lesen=T4,
                    info='a) Nenner 63: 4/9 = 28/63 und 3/7 = 27/63, also 4/9 > 3/7. b) 1/2 = 6/12 und 5/12 < 6/12. c) 14/20 gekürzt durch 2 ist 7/10, die Brüche sind gleichwertig.'))
    # D4: ordnen mit Nenner 16
    folge = ['1/4', '5/16', '3/8', '1/2']
    assert sorted(folge, key=F) == folge and len({F(x) for x in folge}) == 4
    t.append(reihenfolge('Ordne die Brüche vom kleinsten zum größten.', folge, D, lesen=T4,
                         tipp='Der Hauptnenner ist 16.',
                         info='Auf Sechzehntel erweitert: 1/4 = 4/16, 3/8 = 6/16, 1/2 = 8/16, dazu 5/16. Also 4/16 < 5/16 < 6/16 < 8/16.'))
    # D5: rückwärts
    z, n = 35 // 7, 56 // 7
    assert erw(z, n, 7) == (35, 56) and ggt(z, n) == 1
    t.append(luecke('Ein Bruch wurde mit 7 erweitert. Es entstand 35/56. Wie hieß der Bruch vorher?', f'35/56 = {{{{{z}}}}}/{{{{{n}}}}}', D, wortbank=False, lesen=[T2, T3],
                    tipp='Erweitern rückgängig machen heißt kürzen.',
                    info=f'Du musst durch 7 kürzen: 35 : 7 = {z} und 56 : 7 = {n}. Zur Probe: {z} · 7 = 35 und {n} · 7 = 56.'))
    # D6: Textaufgabe
    mia, ben = Fraction(3, 4), Fraction(5, 8)
    assert mia > ben
    t.append(mc('Mia und Ben bekommen gleich große Schokoladentafeln. Mia isst 3/4 ihrer Tafel, Ben isst 5/8 seiner Tafel. Wer hat mehr gegessen?',
                'Mia', ['Ben', 'Beide gleich viel'], D, lesen=T4,
                info='Mache gleichnamig: 3/4 = 6/8. Mia hat 6/8 gegessen, Ben 5/8. Weil 6/8 > 5/8 ist, hat Mia mehr gegessen.'))
    # D7: begründen
    t.append(frei('Lena sagt: „1/3 ist größer als 1/2, weil 3 größer ist als 2.“ Hat Lena recht? Begründe.',
                  'Nein. Lena hat nicht recht. Beim Nenner ist es umgekehrt: Je größer der Nenner, desto kleiner sind die Stücke. '
                  'Drittel sind kleiner als Halbe. Man sieht es auch, wenn man gleichnamig macht: 1/2 = 3/6 und 1/3 = 2/6, und 2/6 ist kleiner als 3/6. '
                  'Also ist 1/3 < 1/2.',
                  ['Antwort: Nein, Lena hat nicht recht (1/3 ist kleiner als 1/2).',
                   'Begründung: Je größer der Nenner, desto kleiner die Stücke, oder Vergleich mit gleichem Nenner (1/2 = 3/6, 1/3 = 2/6).'],
                  2, D, lesen=T4))
    assert Fraction(1, 3) < Fraction(1, 2) and Fraction(1, 2) == Fraction(3, 6) and Fraction(1, 3) == Fraction(2, 6)
    # D8: tf, nicht vollständig gekürzt
    z2, n2 = kue(18, 27, 3)
    assert ggt(z2, n2) == 3 and voll(18, 27)[:2] == (2, 3)
    t.append(tf('Anna kürzt 18/27 durch 3 und erhält 6/9. Damit ist der Bruch vollständig gekürzt.', False, D, lesen=T3,
                info=f'18/27 durch 3 ergibt {fr(z2, n2)}. Aber 6 und 9 kann man noch einmal durch 3 teilen: 2/3. '
                     'Der größte gemeinsame Teiler war 9, deshalb kommt man mit einem Schritt durch 9 auch gleich auf 2/3.'))
    return t


def build():
    aufgaben = bl_a() + bl_b() + bl_c() + bl_d()
    p = pack(ID, 'Mathe Klasse 6: Minitest Brüche (Erweitern, Kürzen, Vergleichen)',
             'Kurzpaket für den Minitest: Brüche erweitern und kürzen und Brüche vergleichen. Mit kurzem Lernblatt und 35 Übungsaufgaben mit Lösungen.',
             lernblatt(), aufgaben,
             hinweis='Kurzfassung für den Minitest am 24.11. (kein Vollpaket). Brüche gibst du in zwei Feldern ein: erst den Zähler, dann den Nenner. '
                     'Steht in deinem Heft beim Vergleichen ein anderer Rechenweg als das Gleichnamig-Machen, gilt der Weg aus dem Heft.')
    nachlesen(p, {A: T2, B: T3, C: T4, D: [T2, T3, T4]})
    p['probe'] = False   # eine Kurzarbeit: nur Üben, keine eigene Probearbeit
    p['termin'] = TERMIN
    p['reihenfolge'] = 1
    assert len(KARTE['titel']) <= 40 and len(KARTE['text']) <= 200, KARTE
    p['karte'] = KARTE
    return p


def main():
    p = build()
    datei = p['id'] + '.json'
    d = ziel(OUT, 'mathe', datei)   # liegt das Thema später unter abgeschlossen/mathe/, wird dort weitergeschrieben
    eintrag = datei if d == OUT else f'abgeschlossen/mathe/{datei}'
    with open(os.path.join(d, datei), 'w', encoding='utf-8') as f:
        json.dump(p, f, ensure_ascii=False, indent=1)
        f.write('\n')
    ix_path = os.path.join(OUT, 'index.json')
    ix = json.load(open(ix_path, encoding='utf-8'))
    if not hat_eintrag(ix, p['id'] + '.json'):
        ix.insert(0, eintrag)   # neues Thema steht vorn
        with open(ix_path, 'w', encoding='utf-8') as f:
            json.dump(ix, f, ensure_ascii=False, indent=1)
            f.write('\n')
    pts = sum(punkte_von(t) for t in p['aufgaben'])
    print(f"{p['id']}: {len(p['aufgaben'])} Aufgaben, {pts} Punkte, {len(p['lernblatt'])} Lernblatt-Abschnitte")


if __name__ == '__main__':
    main()
