"""Deutsch Klasse 6, Paket 3b: Rechtschreibung 2 (Verlängern, Zerlegen, Ableiten, Strategien, Mischtexte).

Checkliste Diktat (DB S. 313–317, AH S. 64–68). Alle Sätze, Texte und Namen sind erfunden (nichts aus Buch oder Heft).
Lösungen laut Faktenblatt Abschnitt 8 und 12.
"""
from deutsch_lib import *

ID = "deutsch-3b-rechtschreibung-2"

B_A = "A – Verlängern: b/p, d/t, g/k"
B_B = "B – Zerlegen und verlängern"
B_C = "C – Ableiten: e/ä und eu/äu"
B_D = "D – Strategien und Mischtexte"

L1 = "Verlängern: b/p, d/t, g/k"
L2 = "Zerlegen und verlängern"
L3 = "Ableiten: e oder ä, eu oder äu"
L4 = "Welche Strategie hilft?"


def lernblatt():
    return [
        lb(L1,
           "Am **Wortende** (und bei Einsilbern) hört man **b/p**, **d/t** und **g/k** schlecht. Dann hilft das **Verlängern**. Verlängere das Wort und sprich langsam: Jetzt hörst du den Buchstaben am Anfang der zweiten Silbe.\n"
           "- **Nomen** in die **Mehrzahl**: Korb – Kör-be (b), Feld – Fel-der (d), Zug – Zü-ge (g).\n"
           "- **Adjektive** steigern oder mit -e verlängern: bunt – bun-te (t), stark – star-ke (k), grob – grö-ber (b).\n"
           "- **Verben** in die **Grundform**: er liebt – lie-ben (b), er pumpt – pum-pen (p), er steigt – stei-gen (g).",
           merke="Unklarer Laut am Wortende? Verlängern! Nomen: Mehrzahl. Adjektive: steigern. Verben: Grundform."),
        lb(L2,
           "Bei **zusammengesetzten Wörtern** gehst du in zwei Schritten vor:\n"
           "1. **Zerlegen:** Teile das Wort in seine Bestandteile: Land | karte.\n"
           "2. **Verlängern:** Verlängere den Teil mit dem unklaren Laut: Land – Län-der, also d.\n"
           "Weitere Beispiele: Hand|tuch (Hän-de), Flug|zeug (Flü-ge), Leucht|turm (Tür-me), Sand|burg (Sand, Bur-gen).\n"
           "So klärst du auch das h: Faul|tier (faul, ohne h), Dreh|wurm (dre-hen, mit h), Tor|bogen (To-re, ohne h). Bei Wörtern wie **achtlos** (Acht) oder **Rolltreppe** (rollen) leitest du den Teil von einem verwandten Wort ab.",
           merke="Erst zerlegen, dann den unklaren Teil verlängern: Land|karte – Länder."),
        lb(L3,
           "Man hört den Unterschied zwischen **e** und **ä** (und zwischen **eu** und **äu**) nicht. Deshalb hilft das **Ableiten**:\n"
           "- Gibt es ein **verwandtes Wort mit a oder au**, schreibt man **ä** oder **äu**: Läufer (laufen), Bäume (Baum), Häuser (Haus), Wäsche (waschen), Käufer (kaufen).\n"
           "- Gibt es **kein** verwandtes Wort mit a oder au, schreibt man **e** oder **eu**: Keller, treffen, Leuchte, seufzen.\n"
           "Einige Wörter mit ä sind **Merkwörter**, bei denen man kein verwandtes Wort mit a findet: Käfig, Mädchen, Säge, Träne, während, ärgern.",
           merke="Verwandtes Wort mit a oder au? Dann ä oder äu. Kein verwandtes Wort? Dann e oder eu. Einige Merkwörter mit ä muss man sich merken."),
        lb(L4,
           "Bei jedem unsicheren Wort fragst du dich: **Welche Strategie hilft?**\n"
           "- **Schwingen:** Das Wort in Silben sprechen (offene und geschlossene Silbe).\n"
           "- **Verlängern:** b/p, d/t, g/k am Wortende, Doppelkonsonant bei Einsilbern, h, s-Laut.\n"
           "- **Zerlegen:** Bei zusammengesetzten Wörtern die Teile trennen und den unklaren Teil verlängern.\n"
           "- **Ableiten:** ä oder äu über ein verwandtes Wort mit a oder au klären.\n"
           "- **Nomensignale:** Steht ein Begleiter davor, schreibt man groß.\n"
           "- **Merkwörter:** Wörter, bei denen keine Regel hilft, lernt man auswendig.\n"
           "Im **Diktat** kreist du unsichere Wörter beim Schreiben ein und prüfst sie am Ende mit einer Strategie.",
           merke="Schwingen, Verlängern, Zerlegen, Ableiten, Nomensignale, Merkwörter: Such dir bei jedem unsicheren Wort die passende Strategie."),
    ]


def aufgaben():
    a = []
    # ---------------------------------------------------------------- A: Verlängern
    a.append(mc("Was machst du, wenn du am Wortende nicht hörst, ob b oder p, d oder t, g oder k steht?",
                "Ich verlängere das Wort, dann höre ich den Buchstaben.",
                ["Ich schreibe immer b, d oder g.", "Ich schreibe immer p, t oder k.", "Ich lasse den Buchstaben weg."], B_A,
                info="Durch das Verlängern (Korb – Körbe) rutscht der unklare Laut an den Anfang der zweiten Silbe, und du hörst ihn deutlich."))
    a.append(zuordnen("Verlängere das Nomen (Mehrzahl). Ordne zu.",
                      [("Korb", "Körbe"), ("Feld", "Felder"), ("Hut", "Hüte"), ("Zug", "Züge"), ("Dieb", "Diebe")],
                      B_A, info="Kör-be (b), Fel-der (d), Hü-te (t), Zü-ge (g), Die-be (b). Nach dem Verlängern hörst du den richtigen Buchstaben."))
    a.append(zuordnen("Verlängere das Adjektiv mit -e. Ordne zu.",
                      [("bunt", "bunte"), ("gesund", "gesunde"), ("stark", "starke"), ("plump", "plumpe"), ("klug", "kluge")],
                      B_A, info="bun-te (t), ge-sun-de (d), star-ke (k), plum-pe (p), klu-ge (g)."))
    a.append(zuordnen("Schreibe die Grundform des Verbs. Ordne zu.",
                      [("liebt", "lieben"), ("lebt", "leben"), ("steigt", "steigen"), ("pumpt", "pumpen"), ("fliegt", "fliegen")],
                      B_A, info="Bei Verben verlängerst du mit der Grundform: lie-ben (b), le-ben (b), stei-gen (g), pum-pen (p), flie-gen (g)."))
    a.append(mc("Welches Wort ist richtig geschrieben? Der Apfel liegt im …",
                "Korb", ["Korp", "Kork"], B_A,
                info="Korb – Kör-be: Beim Verlängern hörst du ein b."))
    a.append(mc("Welches Wort ist richtig geschrieben? Opa trägt einen …",
                "Hut", ["Hud", "Hutt"], B_A,
                info="Hut – Hü-te: Beim Verlängern hörst du ein t. Der Vokal ist lang, deshalb steht nur ein t."))
    a.append(mc("Welches Wort ist richtig geschrieben? Der Hund ist …",
                "gesund", ["gesunt", "gesundt"], B_A,
                info="gesund – ge-sun-de: Beim Verlängern hörst du ein d."))
    a.append(mc("Welches Wort ist richtig geschrieben? Ich höre einen lauten …",
                "Schlag", ["Schlak", "Schlach"], B_A,
                info="Schlag – Schlä-ge: Beim Verlängern hörst du ein g."))
    a.append(mc("Welches Wort ist richtig geschrieben? Unsere Lehrerin ist sehr …",
                "beliebt", ["beliept", "beliebd"], B_A,
                info="beliebt – be-lieb-te: Beim Verlängern hörst du ein b."))
    a.append(tf("Man schreibt „Dieb“ mit b, weil man verlängern kann: Die-be.", True, B_A,
                info="Beim Verlängern (Die-be) hörst du ein b. Deshalb schreibt man auch am Wortende b."))
    a.append(tf("Das Wort „Berg“ schreibt man am Ende mit k, weil man ein k hört.", False, B_A,
                info="Man verlängert: Ber-ge. Dort hörst du ein g. Also schreibt man Berg mit g."))
    a.append(luecke("Schreibe die Wörter richtig auf.",
                    "Der {{Dieb}} läuft mit dem {{Korb}} zum {{Feld}}.",
                    B_A, extra=["Diep", "Korp", "Felt"], gross=True,
                    info="Die-be (b), Kör-be (b), Fel-der (d): Verlängern zeigt dir den richtigen Buchstaben."))
    a.append(luecke("Schreibe die Wörter richtig auf.",
                    "Auf dem {{Weg}} liegt ein {{Stab}} und ein {{Hut}}.",
                    B_A, extra=["Wek", "Stap", "Hud"], gross=True,
                    info="Wege (g), Stä-be (b), Hü-te (t): Beim Verlängern hörst du die Buchstaben.",
                tauschbar=[("Stab", "Hut")]))
    a.append(luecke("Schreibe die Wörter richtig auf.",
                    "Mein Hund ist {{gesund}}, {{stark}} und {{beliebt}}.",
                    B_A, extra=["gesunt", "starg", "beliept"], gross=True, tauschbar=[("gesund", "stark", "beliebt")],
                    info="gesun-de (d), star-ke (k), be-lieb-te (b): Bei Adjektiven verlängerst du mit der Form auf -e."))
    a.append(luecke("Schreibe die Wörter richtig auf.",
                    "Der Hamster {{nagt}} am Holz, das Auto {{blinkt}}, und die Oma {{lebt}} auf dem Land.",
                    B_A, extra=["nakt", "blinckt", "lept"], gross=True,
                    info="na-gen (g), blin-ken (k), le-ben (b): Bei Verben verlängerst du mit der Grundform."))

    # ---------------------------------------------------------------- B: Zerlegen und verlängern
    a.append(mc("Wie klärst du den unklaren Laut in „Landkarte“?",
                "Ich zerlege das Wort in Land und Karte und verlängere Land (Länder).",
                ["Ich verlängere das ganze Wort „Landkarte“.", "Ich schwinge nur die Silben.", "Ich schreibe es mit t, weil man es hört."], B_B,
                info="Bei zusammengesetzten Wörtern zerlegst du zuerst: Land | karte. Dann verlängerst du den Teil mit dem unklaren Laut: Länder, also d."))
    a.append(zuordnen("Wie zerlegt man das Wort?",
                      [("Handtuch", "Hand + Tuch"), ("Leuchtturm", "Leucht + Turm"), ("Rolltreppe", "Roll + Treppe"), ("Sandburg", "Sand + Burg"), ("Torbogen", "Tor + Bogen")],
                      B_B, info="Die Bestandteile sind: Hand + Tuch, Leucht + Turm, Roll + Treppe, Sand + Burg, Tor + Bogen."))
    a.append(zuordnen("Welches verlängerte Wort hilft bei der Schreibweise?",
                      [("Handtuch", "Hände"), ("Flugzeug", "Flüge"), ("Leuchtturm", "Türme"), ("Landkarte", "Länder"), ("Farbton", "Farben")],
                      B_B, info="Hand – Hän-de (d), Flug – Flü-ge (g), Turm – Tür-me, Land – Län-der (d), Farb(e) – Far-ben (b)."))
    a.append(mc("Welches Wort ist richtig geschrieben? Nach dem Duschen nimmt Ole ein …",
                "Handtuch", ["Hanttuch", "Hantuch"], B_B,
                info="Hand | tuch: Hand – Hände, also d. Danach folgt das Wort tuch."))
    a.append(mc("Welches Wort ist richtig geschrieben? Am Himmel fliegt ein …",
                "Flugzeug", ["Fluckzeug", "Flukzeug"], B_B,
                info="Flug | zeug: Flug – Flüge, also g."))
    a.append(mc("Welches Wort ist richtig geschrieben? Im Zoo hängt ein … im Baum.",
                "Faultier", ["Fahultier", "Faulthier"], B_B,
                info="Faul | tier: faul hat kein h, auch beim Verlängern nicht. Tier schreibt man mit ie."))
    a.append(mc("Welches Wort ist richtig geschrieben? Wir gehen durch einen …",
                "Torbogen", ["Thorbogen", "Tohrbogen"], B_B,
                info="Tor | bogen: Tor – To-re, ohne h."))
    a.append(tf("Bei „Rolltreppe“ zerlegt man in Roll und Treppe und leitet „Roll“ von „rollen“ ab (ll).", True, B_B,
                info="rollen: Die erste Silbe ist geschlossen, man hört ein l, also schreibt man ll."))
    a.append(luecke("Schreibe die Wörter richtig auf.",
                    "Am Strand steht ein {{Strandkorb}}, und die Kinder bauen eine {{Sandburg}}, während ein {{Windsurfer}} über die Wellen gleitet.",
                    B_B, extra=["Strantkorb", "Sandburk", "Wintsurfer"], gross=True,
                    info="Strand | korb (Strände, Körbe), Sand | burg (Burgen), Wind | surfer (Winde): Zerlege die Wörter und verlängere den Teil mit dem unklaren Laut."))
    a.append(luecke("Schreibe die Wörter richtig auf.",
                    "Im Urlaub sehen wir einen {{Leuchtturm}}, kaufen eine {{Landkarte}} und fahren mit der {{Rolltreppe}} ins Hotel.",
                    B_B, extra=["Leuchtthurm", "Lantkarte", "Roltreppe"], gross=True,
                    info="Leucht | turm (Türme), Land | karte (Länder), Roll | treppe (rollen): Zuerst zerlegen, dann verlängern."))

    # ---------------------------------------------------------------- C: Ableiten
    a.append(mc("Wann schreibt man ä oder äu?",
                "Wenn es ein verwandtes Wort mit a oder au gibt.",
                ["Wenn man den Unterschied deutlich hören kann.", "Immer am Wortanfang.", "Wenn das Wort ein Nomen ist."], B_C,
                info="Man hört den Unterschied zwischen e und ä nicht. Deshalb hilft das verwandte Wort: Läufer – laufen, Bäume – Baum."))
    a.append(mc("Welche Aussagen zum Ableiten sind richtig? (mehrere Antworten sind richtig)",
                ["Verwandte Wörter helfen bei der Entscheidung.", "Gibt es ein verwandtes Wort mit a oder au, schreibt man ä oder äu.", "Gibt es kein verwandtes Wort mit a oder au, schreibt man e oder eu."],
                ["Man hört den Unterschied zwischen e und ä immer deutlich."], B_C,
                info="Richtig sind die drei Regeln zum Ableiten. Falsch ist die letzte Aussage: e und ä klingen gleich, deshalb muss man ableiten."))
    a.append(zuordnen("Welches verwandte Wort mit a oder au hilft?",
                      [("Bäume", "Baum"), ("Mäuse", "Maus"), ("Gläser", "Glas"), ("Kälte", "kalt"), ("Wärme", "warm"), ("Häuser", "Haus")],
                      B_C, info="Bäume – Baum, Mäuse – Maus, Gläser – Glas, Kälte – kalt, Wärme – warm, Häuser – Haus. Es gibt ein verwandtes Wort mit a oder au, also schreibt man ä oder äu."))
    a.append(zuordnen("Welche Buchstaben fehlen? Ordne zu.",
                      [("W_sche (waschen)", "ä"), ("K_ller (kein Wort mit a)", "e"), ("K_ufer (kaufen)", "äu"),
                       ("L_chte (kein Wort mit au)", "eu"), ("D_mpfe (Dampf)", "ä"), ("verb_lt (Beule)", "eu")],
                      B_C, info="Wäsche (waschen), Keller (kein a-Wort), Käufer (kaufen), Leuchte (kein au-Wort), Dämpfe (Dampf), verbeult (Beule hat eu)."))
    a.append(mc("Welches Wort ist richtig geschrieben? Der … zahlt an der Kasse.",
                "Käufer", ["Keufer", "Kaufer"], B_C,
                info="Käufer – kaufen: Es gibt ein verwandtes Wort mit au, also schreibt man äu."))
    a.append(mc("Welches Wort ist richtig geschrieben? Die schmutzige … kommt in die Maschine.",
                "Wäsche", ["Wesche", "Wasche"], B_C,
                info="Wäsche – waschen: Es gibt ein verwandtes Wort mit a, also schreibt man ä."))
    a.append(mc("Welches Wort ist richtig geschrieben? Im … ist es kühl.",
                "Keller", ["Käller", "Keler"], B_C,
                info="Zu „Keller“ gibt es kein verwandtes Wort mit a. Also schreibt man e. Nach kurzem Vokal steht ll."))
    a.append(mc("Welches Wort ist richtig geschrieben? Nach der Arbeit … Papa laut.",
                "seufzt", ["säufzt", "seuzt"], B_C,
                info="Zu „seufzen“ gibt es kein verwandtes Wort mit au. Also schreibt man eu."))
    a.append(mc("Bei welchen Wörtern gibt es kein verwandtes Wort mit a? Man muss sie sich merken und schreibt sie mit ä. (mehrere Antworten sind richtig)",
                ["Käfig", "Mädchen", "Träne"], ["Keller", "treffen"], B_C,
                info="Käfig, Mädchen, Träne, Säge, während und ärgern sind Merkwörter mit ä. Keller und treffen schreibt man mit e."))
    a.append(tf("„Käfig“ ist ein Merkwort mit ä.", True, B_C,
                info="Zu „Käfig“ gibt es kein verwandtes Wort mit a. Man muss sich merken, dass man es mit ä schreibt."))
    a.append(tf("„treffen“ schreibt man mit e, weil es kein verwandtes Wort mit a gibt.", True, B_C,
                info="Zu „treffen“ findest du kein Wort mit a. Also schreibt man e. Nach dem kurzen Vokal steht ff."))
    a.append(luecke("Schreibe die Wörter richtig auf.",
                    "Im Herbst fallen die Blätter von den {{Bäumen}}, und die {{Mäuse}} suchen Futter in den {{Wäldern}}.",
                    B_C, extra=["Beumen", "Mäse", "Welder"], gross=True,
                    info="Bäume – Baum, Mäuse – Maus, Wälder – Wald: Es gibt jeweils ein verwandtes Wort mit a oder au.",
                tauschbar=[("Bäumen", "Wäldern")]))
    a.append(luecke("Schreibe die Wörter richtig auf.",
                    "Der {{Läufer}} wird {{kräftiger}}, denn er trainiert {{täglich}}.",
                    B_C, extra=["Leufer", "kreftiger", "teglich"], gross=True,
                    info="Läufer – laufen, kräftiger – Kraft, täglich – Tag: Ableiten mit a."))
    a.append(luecke("Schreibe die Wörter richtig auf.",
                    "Die {{Leuchte}} im {{Keller}} flackert, und Ole {{seufzt}}.",
                    B_C, extra=["Läuchte", "Käller", "säufzt"], gross=True,
                    info="Leuchte, Keller und seufzen haben kein verwandtes Wort mit au oder a. Deshalb schreibt man eu und e."))
    a.append(kurz("Schreibe das verwandte Wort mit au auf: Mäuse – …", "Maus", B_C, gross=True,
                  info="Mäuse – Maus: Aus dem Wort Maus wird in der Mehrzahl Mäuse. Deshalb schreibt man äu."))
    a.append(kurz("Schreibe das verwandte Wort mit a auf: kräftig – …", "Kraft", B_C, gross=True,
                  info="kräftig – Kraft: Das verwandte Nomen hat ein a. Deshalb schreibt man ä."))

    # ---------------------------------------------------------------- D: Strategien und Mischtexte
    a.append(zuordnen("Welche Strategie hilft bei dem Wort?",
                      [("Stab", "verlängern"), ("Windsurfer", "zerlegen und verlängern"), ("Läufer", "ableiten"),
                       ("Rolltreppe", "zerlegen und verlängern"), ("Mäuse", "ableiten"), ("Berg", "verlängern")],
                      B_D, info="Stab (Stäbe) und Berg (Berge): verlängern. Windsurfer (Wind | surfer) und Rolltreppe (Roll | treppe): zerlegen und verlängern. Läufer (laufen) und Mäuse (Maus): ableiten."))
    a.append(tf("Bei zusammengesetzten Nomen verlängert man immer das ganze Wort.", False, B_D,
                info="Man zerlegt zuerst in die Bestandteile und verlängert dann nur den Teil mit dem unklaren Laut (Land | karte – Länder)."))
    a.append(tf("Bei Verben verlängert man mit der Grundform: er liebt – lieben.", True, B_D,
                info="Die Grundform (lie-ben) zeigt dir das b."))
    a.append(luecke("Schreibe die Wörter richtig auf (Text: Der Wintertag).",
                    "Im Winter fällt viel {{Schnee}}. Die {{Kinder}} bauen einen {{Schneemann}} und werfen {{Bälle}} aus Schnee. Danach trinken sie warmen {{Tee}}.",
                    B_D, extra=["Schne", "Kiender", "Schneman", "Bele", "Te"], gross=True,
                    info="Schnee und Tee haben Doppelvokal ee. Kin-der hat eine geschlossene erste Silbe (i). Schnee|mann hat nn (Mann). Bälle – Ball (ä, ll)."))
    a.append(luecke("Schreibe die Wörter richtig auf (Text: Der Onkel am Meer).",
                    "Mein {{Onkel}} {{wohnt}} in einer {{Stadt}} am {{Meer}}. Er {{fährt}} jeden Tag mit dem {{Fahrrad}} zur Arbeit.",
                    B_D, extra=["Onkl", "wont", "Stat", "Mer", "fert", "Farrad"], gross=True,
                    info="wohnt und Fahrrad haben ein h vor n und r (Merkwörter). Stadt – Städte (d). fährt – fahren (ä). Meer hat Doppelvokal ee."))
    a.append(luecke("Schreibe die Wörter richtig auf (Text: In der Backstube).",
                    "Der {{Bäcker}} {{knetet}} den {{Teig}} und {{schiebt}} die {{Brötchen}} in den Ofen.",
                    B_D, extra=["Beker", "knätet", "Teik", "schibt", "Brotchen"], gross=True, fest=True,
                    info="Bäcker – backen (ä), kneten (e, kein Wort mit a), Teig – Teige (g), schiebt – schieben (ie, b), Brötchen – Brote (ö)."))
    a.append(luecke("Schreibe die Wörter richtig auf (Text: Im Keller).",
                    "Im {{Keller}} liegt ein alter {{Koffer}} mit {{Wäsche}}, und im {{Schrank}} stehen bunte {{Gläser}}.",
                    B_D, extra=["Käller", "Kofer", "Wesche", "Schrang", "Gleser"], gross=True,
                    info="Keller (e), Koffer (ff nach kurzem Vokal), Wäsche – waschen (ä), Schrank – Schränke (k), Gläser – Glas (ä).",
                tauschbar=[("Keller", "Schrank")]))
    a.append(luecke("Schreibe die Wörter richtig auf (Text: Im Garten).",
                    "Die {{Mädchen}} spielen mit einem {{Ball}} im {{Garten}}. Plötzlich {{liegt}} er im {{Beet}}.",
                    B_D, extra=["Medchen", "Bal", "Garden", "ligt", "Bet"], gross=True,
                    info="Mädchen ist ein Merkwort mit ä. Ball – Bälle (ll). Garten (r und t, kein Doppelkonsonant). liegt – liegen (ie, g). Beet hat Doppelvokal ee.",
                tauschbar=[("Garten", "Beet")]))
    a.append(mc("Welcher Satz ist richtig geschrieben?",
                "Der Hund bellt laut, weil ein Dieb über den Zaun klettert.",
                ["Der Hunt bellt laut, weil ein Dieb über den Zaun klettert.", "Der Hund bellt laut, weil ein Diep über den Zaun klettert."], B_D,
                info="Hund – Hunde (d) und Dieb – Diebe (b): Das Verlängern zeigt dir die Buchstaben."))
    a.append(mc("Welcher Satz ist richtig geschrieben?",
                "Die Kinder rennen über den Platz und spielen mit dem Ball.",
                ["Die Kinder renen über den Platz und spielen mit dem Ball.", "Die Kinder rennen über den Plaz und spielen mit dem Ball."], B_D,
                info="ren-nen (nn nach kurzem Vokal) und Platz – Plät-ze (tz). Bei einem Wort mit tz hörst du das t im Silbenschnitt."))
    a.append(mc("Welcher Satz ist richtig geschrieben?",
                "Die Mäuse laufen über die Wiese, und die Katze schleicht heran.",
                ["Die Meuse laufen über die Wiese, und die Katze schleicht heran.", "Die Mäuse laufen über die Wise, und die Katze schleicht heran."], B_D,
                info="Mäuse – Maus (äu). Wie-se hat eine offene erste Silbe mit langem i, also ie."))
    return a


def build():
    p = pack(ID, "Deutsch Teil 3b: Rechtschreibung 2",
             "Verlängern (b/p, d/t, g/k), Zerlegen zusammengesetzter Wörter, Ableiten (e/ä, eu/äu) und die passende Strategie wählen. Mit Lernblatt und Übungsaufgaben.",
             lernblatt(), aufgaben(), min_aufgaben=45,
             hinweis="Alle Sätze, Texte und Namen sind selbst ausgedacht, nicht aus dem Deutschbuch oder Aufgabenheft. Die Strategien stehen so auch im Deutschbuch (S. 313–317) und im Aufgabenheft (S. 64–68). Bei den Lücken zählt jeder Buchstabe: Tippe das Wort genau so, wie es geschrieben werden muss.")
    return [nachlesen(p, {B_A: L1, B_B: L2, B_C: L3, B_D: [L4, L1, L2, L3]})]


if __name__ == "__main__":
    for p in build():
        print(p["id"], len(p["aufgaben"]), "Aufgaben")
