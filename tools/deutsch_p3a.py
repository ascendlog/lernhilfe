"""Deutsch Klasse 6, Paket 3a: Rechtschreibung 1 (Silben, Doppelkonsonanten, s-Laute, i/ie/ih, h und Doppelvokale).

Checkliste Diktat (DB S. 313–317, AH S. 64–81). Alle Sätze, Texte und Namen sind erfunden (nichts aus Buch oder Heft).
Lösungen laut Faktenblatt Abschnitt 8 und 12. s/ss/ß werden nur per Auswahl (mc/tf) oder über den Klang entschieden,
weil die App beim Tippen ß und ss gleich behandelt.
"""
from deutsch_lib import *

ID = "deutsch-3a-rechtschreibung-1"

B_A = "A – Silben schwingen: offen und geschlossen"
B_B = "B – Doppelkonsonanten, ck und tz"
B_C = "C – s, ss oder ß?"
B_D = "D – i, ie oder ih?"
B_E = "E – Das h und Wörter mit Doppelvokal"

L1 = "Silben schwingen: offen oder geschlossen"
L2 = "Doppelkonsonanten, ck und tz"
L3 = "s, ss oder ß?"
L4 = "Wechsel des s-Lauts und Merkwörter mit s"
L5 = "i, ie oder ih?"
L6 = "Das h und Wörter mit Doppelvokal"


def lernblatt():
    return [
        lb(L1,
           "Wörter bestehen aus **Silben**. Du erkennst sie, wenn du das Wort **langsam sprichst** und dabei **mitschwingst** (mit der Hand für jede Silbe einen Bogen zeichnen): Ba-na-ne (3 Silben), Son-ne (2 Silben), Rad (1 Silbe).\n"
           "Die erste Silbe kann **offen** oder **geschlossen** sein:\n"
           "- **Offene Silbe:** Sie endet auf einen **Vokal** (a, e, i, o, u), einen **Umlaut** (ä, ö, ü) oder einen **Zwielaut** (ei, au, eu, äu): Ho-se, Hö-fe, Hei-zung.\n"
           "- **Geschlossene Silbe:** Sie endet auf einen **Konsonanten**: Kan-ne, Hil-fe, Gar-ten.\n"
           "In einer offenen Silbe klingt der Vokal meistens **lang**, in einer geschlossenen Silbe **kurz**. Daran hängen fast alle Rechtschreibregeln auf diesem Lernblatt.",
           merke="Offene Silbe: endet auf Vokal, Umlaut oder Zwielaut (Ho-se). Geschlossene Silbe: endet auf einen Konsonanten (Kan-ne)."),
        lb(L2,
           "Nach einem **kurzen Vokal** steht oft ein **Doppelkonsonant**. Das gilt, wenn die erste Silbe **geschlossen** ist und du an der Silbengrenze **nur einen** Konsonanten hörst: kom-men, Kan-ne, Mit-te, Bäl-le.\n"
           "Hörst du an der Silbengrenze **zwei verschiedene** Konsonanten, wird **nicht verdoppelt**: Hil-fe, Kar-te, bun-te, Gar-ten.\n"
           "**Einsilber verlängern:** Dann hörst du es genau: Ball – Bälle, Bett – Betten, Tipp – tippen. Bei Heft – Hefte hörst du f und t, also kein Doppelkonsonant.\n"
           "Statt **kk** schreibt man **ck** (Ba-cken, Bä-cker, Zu-cker). Statt **zz** schreibt man **tz** (Kat-ze, Plät-ze, Sitz). Nach l, n und r steht nur ein z oder k: Salz, Tanz, Herz, Dank.",
           merke="Geschlossene erste Silbe und nur ein Konsonant zu hören: Doppelkonsonant. Zwei verschiedene Konsonanten: nicht verdoppeln. Statt kk schreibt man ck, statt zz schreibt man tz."),
        lb(L3,
           "Der s-Laut kann **summen** (wie eine Biene: Hase) oder **zischen** (wie eine Schlange: Straße). Dazu kommt, ob die erste Silbe **offen** oder **geschlossen** ist:\n"
           "- **s:** erste Silbe **offen**, der Laut **summt**: Ha-se, lei-se, Ro-se, Ra-sen.\n"
           "- **ß:** erste Silbe **offen**, der Laut **zischt**: Stra-ße, grü-ßen, bei-ßen, hei-ßen.\n"
           "- **ss:** erste Silbe **geschlossen** (kurzer Vokal), der Laut **zischt**: Tas-se, müs-sen, Wis-sen, Kes-sel.\n"
           "**Einsilber verlängern:** Gras – Grä-ser (s), Fuß – Fü-ße (ß), muss – müs-sen (ss), Fluss – Flüs-se (ss).",
           merke="s: offene Silbe, summt. ß: offene Silbe, zischt. ss: geschlossene Silbe, kurzer Vokal, zischt. Einsilber verlängern!"),
        lb(L4,
           "Bei Verben kann der s-Laut **wechseln**, weil sich der Vokal ändert: fließen – er fließt – er floss – der Fluss. Beim kurzen Vokal (floss, Fluss) steht ss, beim langen Vokal oder Zwielaut (fließen, heißen, beißen) steht ß.\n"
           "Weitere Beispiele: ich esse – ich **aß** (langer Vokal: ß), ich weiß – ich **wusste** (kurzer Vokal: ss), ich lasse – ich **ließ** (langer Vokal: ß).\n"
           "**Merkwörter mit s:** Diese Wörter kann man nicht verlängern. Man schreibt sie trotzdem mit einfachem s: als, aus, bis, es, etwas, niemals, alles, anders, morgens.",
           merke="Der s-Laut kann wechseln: fließen – floss – Fluss. Merkwörter mit s: als, aus, bis, es, etwas, niemals, alles, anders, morgens."),
        lb(L5,
           "Man schreibt **oft ie**, wenn die erste Silbe **offen** ist und der Vokal **lang** klingt: Zie-le, Brie-fe, Wie-se, Bie-ne, spie-len.\n"
           "Ist die erste Silbe **geschlossen** (kurzer Vokal), schreibt man **i**: Kin-der, Tin-te, Pil-ze, bil-den.\n"
           "**Einsilber verlängern:** Kind – Kin-der (i), Brief – Brie-fe (ie), Spiel – spie-len (ie).\n"
           "**Merkwörter mit i und ih:** mir, dir, wir, ihr, ihm, ihn, ihnen, ihre. Dazu kommen einige Fremdwörter, bei denen das i lang klingt und trotzdem nur ein i steht: Kino, Kilo, Tiger, Medizin. Verben auf **-ieren** schreibt man immer mit ie: probieren, trainieren, musizieren.",
           merke="Oft ie: erste Silbe offen, Vokal lang (Zie-le). i: erste Silbe geschlossen (Kin-der). Merkwörter: mir, dir, wir, ihr, ihm, ihn, ihnen, ihre."),
        lb(L6,
           "**Silbenöffnendes h:** Bei Einsilbern hört man das h nicht. Verlängere das Wort, dann steht das h **am Anfang der zweiten Silbe** und du kannst es **hören**: Kuh – Kü-he, geht – ge-hen, zieht – zie-hen, Zeh – Ze-hen, Mühe (Mü-he), ruhen (ru-hen).\n"
           "**h am Ende der ersten Silbe (Dehnungs-h):** Es steht oft vor **l, m, n, r**, man hört es nicht. Diese Wörter sind **Merkwörter**: Zahl, lahm, zahm, Mahnung, wohnen, Wohnung, fahren, Lehrer, Jahr, Nahrung.\n"
           "**Doppelvokale** (Merkwörter, nur wenige Wörter): **aa** (Aal, Haar, Paar, Saal, Staat), **ee** (Beere, Beet, Klee, Meer, Schnee, See, Allee, Idee, Kaffee, Tee), **oo** (Boot, Moor, Moos, Zoo).",
           merke="Silbenöffnendes h: beim Verlängern am Anfang der zweiten Silbe hörbar (zie-hen). h vor l, m, n, r: Merkwörter. Doppelvokale aa, ee, oo: Merkwörter."),
    ]


def aufgaben():
    a = []
    # ---------------------------------------------------------------- A: Silben, offen und geschlossen
    a.append(kurz("Wie viele Silben hat das Wort „Elefant“? Schwinge mit.", "3", B_A,
                  info="E-le-fant: Wenn du langsam sprichst und mitschwingst, zählst du drei Bögen, also drei Silben."))
    a.append(zuordnen("Wie viele Silben hat das Wort?",
                      [("Rad", "1"), ("Sonne", "2"), ("Kartoffel", "3"), ("Schokolade", "4"), ("Wassermelone", "5")],
                      B_A, info="Rad (1), Son-ne (2), Kar-tof-fel (3), Scho-ko-la-de (4), Was-ser-me-lo-ne (5). Sprich langsam und schwinge für jede Silbe einen Bogen."))
    a.append(reihenfolge("Bringe die Silben in die richtige Reihenfolge: Geburtstagsgeschenk.",
                         ["Ge", "burts", "tags", "ge", "schenk"], B_A,
                         info="Ge-burts-tags-ge-schenk: Das Wort hat fünf Silben. Schwinge beim Sprechen mit, dann hörst du die Reihenfolge."))
    a.append(mc("Wie trennt man „Kartoffel“ richtig in Silben?",
                "Kar-tof-fel", ["Kart-of-fel", "Kar-to-ffel", "Ka-rtof-fel"], B_A,
                info="Beim Schwingen hörst du: Kar – tof – fel. Der Doppelkonsonant ff wird bei der Silbentrennung geteilt: tof-fel."))
    a.append(zuordnen("Ist die erste Silbe offen oder geschlossen?",
                      [("Ho-se", "offen"), ("Kan-ne", "geschlossen"), ("Ke-gel", "offen"), ("Kis-te", "geschlossen"), ("Hei-zung", "offen"), ("Hil-fe", "geschlossen")],
                      B_A, info="Offen: Ho (Vokal o), Ke (Vokal e), Hei (Zwielaut ei). Geschlossen: Kan (endet auf n), Kis (endet auf s), Hil (endet auf l)."))
    a.append(mc("Eine offene Silbe endet auf …",
                "einen Vokal, einen Umlaut oder einen Zwielaut", ["einen Konsonanten", "zwei gleiche Konsonanten", "ein stummes e"], B_A,
                info="Offen heißt: Die Silbe endet auf einen Selbstlaut (Ho-se), einen Umlaut (Hö-fe) oder einen Zwielaut (Hei-zung). Endet sie auf einen Konsonanten, ist sie geschlossen (Kan-ne)."))
    a.append(mc("Wie klingt der Vokal meistens in einer geschlossenen ersten Silbe wie bei „Kan-ne“?",
                "kurz", ["lang", "gar nicht"], B_A,
                info="In einer geschlossenen Silbe klingt der Vokal kurz (Kan-ne). In einer offenen Silbe klingt er meistens lang (Ho-se)."))
    a.append(mc("Welche Wörter haben eine offene erste Silbe? (mehrere Antworten sind richtig)",
                ["Ho-se", "Ba-den", "Hei-zung"], ["Kis-te", "Hil-fe"], B_A,
                info="Offen: Ho, Ba und Hei enden auf Vokal beziehungsweise Zwielaut. Bei Kis-te und Hil-fe endet die erste Silbe auf einen Konsonanten (s, l), sie ist geschlossen."))
    a.append(tf("Die erste Silbe von „Hö-fe“ ist offen, weil sie auf einen Umlaut endet.", True, B_A,
                info="Das ö ist ein Umlaut, also ein Vokal. Die Silbe „Hö“ endet auf einen Vokal und ist deshalb offen."))
    a.append(tf("Die erste Silbe von „Wand-ta-fel“ ist offen.", False, B_A,
                info="„Wand“ endet auf die Konsonanten n und d. Die Silbe ist geschlossen."))
    a.append(tf("Bei „Hei-zung“ ist die erste Silbe offen, weil „ei“ ein Zwielaut ist.", True, B_A,
                info="„Hei“ endet auf einen Zwielaut (ei) und damit auf einen Vokalklang. Die Silbe ist offen."))
    a.append(luecke("Setze die passenden Wörter ein.",
                    "Eine Silbe ist {{offen}}, wenn sie auf einen Vokal, Umlaut oder Zwielaut endet. Sie ist {{geschlossen}}, wenn sie auf einen Konsonanten endet. Bei „Ho-se“ ist die erste Silbe {{offen}}.",
                    B_A, info="Offene Silbe: Vokal, Umlaut oder Zwielaut am Ende. Geschlossene Silbe: Konsonant am Ende. „Ho“ endet auf o, also ist die Silbe offen."))

    # ---------------------------------------------------------------- B: Doppelkonsonanten, ck, tz
    a.append(zuordnen("Hat das Wort einen Doppelkonsonanten?",
                      [("Kanne", "mit Doppelkonsonant"), ("Karte", "ohne Doppelkonsonant"), ("Sonne", "mit Doppelkonsonant"),
                       ("Hilfe", "ohne Doppelkonsonant"), ("Mitte", "mit Doppelkonsonant"), ("Wolke", "ohne Doppelkonsonant")],
                      B_B, info="Kan-ne, Son-ne und Mit-te: Man hört nur einen Konsonanten, also doppelt man. Kar-te, Hil-fe und Wol-ke: zwei verschiedene Konsonanten (r und t, l und f, l und k), also nicht doppelt."))
    a.append(mc("Warum schreibt man „Kanne“ mit nn?",
                "Die erste Silbe (Kan-) ist geschlossen und man hört nur einen Konsonanten.",
                ["Weil die erste Silbe offen ist.", "Weil „Kanne“ ein Nomen ist.", "Weil der Vokal lang klingt."], B_B,
                info="Kan-ne: Die erste Silbe endet auf n, der Vokal klingt kurz. Man hört an der Silbengrenze nur ein n, deshalb verdoppelt man es."))
    a.append(mc("Warum schreibt man „Hilfe“ nur mit einem f?",
                "An der Silbengrenze (Hil-fe) stehen zwei verschiedene Konsonanten, l und f.",
                ["Weil die erste Silbe offen ist.", "Weil „Hilfe“ ein Nomen ist.", "Weil man f nie verdoppelt."], B_B,
                info="Bei zwei verschiedenen Konsonanten (l und f) verdoppelt man nicht. Das f wird nur verdoppelt, wenn man an der Silbengrenze ein einzelnes f hört (Löf-fel)."))
    a.append(mc("Welches Wort ist richtig geschrieben? Am … schreibt die Klasse eine Deutscharbeit.",
                "Mittwoch", ["Mitwoch", "Mittwock"], B_B,
                info="Mitt-woch: Die erste Silbe (Mitt-) ist geschlossen, man hört nur ein t, also steht tt. Das Wort endet auf -woch."))
    a.append(mc("Welche Wörter haben einen Doppelkonsonanten? (mehrere Antworten sind richtig)",
                ["Kartoffel", "Sommer", "Mutter"], ["Garten", "Kerze"], B_B,
                info="Kar-tof-fel (ff), Som-mer (mm) und Mut-ter (tt) haben einen Doppelkonsonanten. Gar-ten (r und t) und Ker-ze (r und z) haben zwei verschiedene Konsonanten an der Silbengrenze."))
    a.append(tf("„Fallobst“ schreibt man mit ll, weil man verlängert: fallen.", True, B_B,
                info="Bei zusammengesetzten Wörtern klärt man den Teil mit dem unklaren Laut: Fall – fal-len. Man hört ein l an der Silbengrenze, die Silbe ist geschlossen, also schreibt man ll."))
    a.append(tf("Bei „Wolke“ steht kein Doppelkonsonant, weil an der Silbengrenze zwei verschiedene Konsonanten stehen (Wol-ke).", True, B_B,
                info="Zwischen l und k wird nicht verdoppelt. Man verdoppelt nur, wenn man an der Silbengrenze einen einzelnen Konsonanten hört."))
    a.append(mc("Was schreibt man statt „kk“ und statt „zz“?",
                "ck und tz", ["kk und zz", "ch und sch", "ks und zs"], B_B,
                info="Ba-cken statt „Bakken“ und Kat-ze statt „Kazze“: Statt kk schreibt man ck, statt zz schreibt man tz."))
    a.append(mc("Welche Wörter schreibt man mit tz? (mehrere Antworten sind richtig)",
                ["Katze", "Blitz", "Pfütze"], ["Tanz", "Herz"], B_B,
                info="Nach kurzem Vokal steht tz: Kat-ze, Blitz, Pfüt-ze. Nach n und r steht nur z: Tanz (tanzen), Herz."))
    a.append(zuordnen("Verlängere das Wort. Ordne die verlängerte Form zu.",
                      [("Ball", "Bälle"), ("Schiff", "Schiffe"), ("Bett", "Betten"), ("Tipp", "tippen"), ("Heft", "Hefte")],
                      B_B, info="Beim Verlängern hörst du den Konsonanten: Bäl-le, Schif-fe, Bet-ten, tip-pen. Bei Hef-te hörst du f und t, deshalb steht dort kein Doppelkonsonant."))
    a.append(kurz("Schreibe die Mehrzahl von „Ball“.", "Bälle", B_B, gross=True,
                  info="Ball – Bäl-le: Die erste Silbe ist geschlossen, nach dem kurzen ä steht ll. Aus a wird ä, weil es das Wort Ball dazu gibt."))
    a.append(kurz("Schreibe das Verb in der Grundform: er rennt – …", "rennen", B_B, gross=True,
                  info="Ren-nen: Die erste Silbe ist geschlossen, man hört ein n, deshalb steht nn. Auch bei „er rennt“ schreibt man nn."))
    a.append(luecke("Schreibe die Wörter richtig auf.",
                    "Im {{Sommer}} steht die {{Sonne}} hoch am {{Himmel}}.",
                    B_B, extra=["Somer", "Sone", "Himel"], gross=True,
                    info="Som-mer, Son-ne und Him-mel: Die erste Silbe ist jeweils geschlossen, nach dem kurzen Vokal hört man nur einen Konsonanten, deshalb steht mm beziehungsweise nn."))
    a.append(luecke("Schreibe die Wörter richtig auf.",
                    "Mia stellt einen {{Teller}} auf den Tisch und legt einen {{Löffel}} daneben. Dazu gibt es {{Pfannkuchen}} mit {{Butter}}.",
                    B_B, extra=["Teler", "Löfel", "Pfankuchen", "Buter"], gross=True,
                    info="Tel-ler (ll), Löf-fel (ff), Pfann-ku-chen (nn), But-ter (tt): Nach kurzem Vokal steht ein Doppelkonsonant.",
                tauschbar=[("Teller", "Löffel")]))
    a.append(luecke("Schreibe die Wörter richtig auf.",
                    "Die {{Katze}} springt auf die {{Decke}} und putzt ihren {{Rücken}}.",
                    B_B, extra=["Kaze", "Deke", "Rüken"], gross=True,
                    info="Kat-ze (tz statt zz), De-cke (ck statt kk), Rü-cken (ck statt kk)."))
    a.append(luecke("Schreibe die Wörter richtig auf.",
                    "Ole {{schwitzt}}, denn er rennt über den {{Platz}} und erzählt einen {{Witz}}.",
                    B_B, extra=["schwizt", "Plaz", "Wiz"], gross=True,
                    info="schwit-zen (tz), Platz (Plät-ze), Witz (Wit-ze): Nach kurzem Vokal schreibt man tz statt zz."))
    a.append(mc("Welches Wort ist richtig geschrieben? Die Kinder malen mit …",
                "Buntstiften", ["Bundstiften", "Bunstiften"], B_B,
                info="bunt – bun-te: Man hört ein t. An der Silbengrenze stehen zwei verschiedene Konsonanten (n und t), deshalb wird nicht verdoppelt: Bunt-stif-te."))

    # ---------------------------------------------------------------- C: s, ss, ß
    a.append(zuordnen("Summt oder zischt der s-Laut in dem Wort?",
                      [("Hase", "summt"), ("Straße", "zischt"), ("Dose", "summt"), ("beißen", "zischt"), ("leise", "summt"), ("Tasse", "zischt")],
                      B_C, info="Summt (wie eine Biene): Hase, Dose, leise. Zischt (wie eine Schlange): Straße, beißen, Tasse. Das ist der erste Schritt bei der Frage s, ss oder ß."))
    a.append(mc("Die erste Silbe ist offen und der s-Laut summt, wie bei „Hase“. Was schreibt man?",
                "s", ["ß", "ss", "z"], B_C,
                info="Offene Silbe und summender Laut: einfaches s. Beispiele: Ha-se, lei-se, Ro-se, Ra-sen."))
    a.append(mc("Die erste Silbe ist offen und der s-Laut zischt, wie bei „Straße“. Was schreibt man?",
                "ß", ["s", "ss", "sz"], B_C,
                info="Offene Silbe und zischender Laut: ß. Beispiele: Stra-ße, grü-ßen, bei-ßen, hei-ßen."))
    a.append(mc("Die erste Silbe ist geschlossen (kurzer Vokal) und der s-Laut zischt, wie bei „Tasse“. Was schreibt man?",
                "ss", ["ß", "s", "sz"], B_C,
                info="Geschlossene Silbe, kurzer Vokal, zischender Laut: ss. Beispiele: Tas-se, müs-sen, Kes-sel, wis-sen."))
    a.append(mc("Welches Wort ist richtig geschrieben? Wir wohnen in einer ruhigen …",
                "Straße", ["Strase", "Strasse"], B_C,
                info="Stra-ße: Die erste Silbe (Stra-) ist offen, der Vokal ist lang und der s-Laut zischt. Dann schreibt man ß."))
    a.append(mc("Welche Wörter schreibt man mit einfachem s? (mehrere Antworten sind richtig)",
                ["Hase", "Nase", "Rasen"], ["Gruß", "Tasse"], B_C,
                info="Ha-se, Na-se und Ra-sen: offene erste Silbe, summender Laut, also s. Bei Gruß (Grü-ße) zischt der Laut und die Silbe ist offen (ß), bei Tas-se ist die erste Silbe geschlossen (ss)."))
    a.append(mc("Verlängere: er muss – wir müssen. Wie schreibt man das Wort richtig?",
                "muss", ["mus", "muß"], B_C,
                info="müs-sen: Die erste Silbe ist geschlossen, der Vokal ist kurz, der Laut zischt. Also steht ss: er muss."))
    a.append(tf("Man schreibt „Gras“ mit einfachem s, weil man verlängern kann: Grä-ser.", True, B_C,
                info="Beim Verlängern (Grä-ser) ist die erste Silbe offen und der Laut summt. Also schreibt man s: Gras."))
    a.append(tf("Man schreibt „Fuß“ mit ß, weil beim Verlängern (Fü-ße) die erste Silbe offen ist und der s-Laut zischt.", True, B_C,
                info="Fü-ße: offene Silbe, langer Vokal, zischender Laut. Dann schreibt man ß, auch am Wortende: Fuß."))
    a.append(tf("Man schreibt „Tasse“ mit ss, weil die erste Silbe offen ist.", False, B_C,
                info="Bei Tas-se ist die erste Silbe geschlossen (sie endet auf s) und der Vokal ist kurz. Nur deshalb steht ss."))
    a.append(mc("Wechsel des s-Lauts: fließen – er floss – der Fluss. Warum schreibt man „floss“ mit ss?",
                "Der Vokal wird kurz gesprochen und der s-Laut zischt.",
                ["Der Vokal wird lang gesprochen und die Silbe ist offen.", "Weil „floss“ ein Nomen ist.", "Weil die Vergangenheit immer ss hat."], B_C,
                info="In „floss“ und „Fluss“ ist der Vokal kurz, deshalb steht ss. Bei „fließen“ ist der Vokal lang, deshalb steht ß. Der s-Laut wechselt mit dem Vokal."))
    a.append(mc("Wie schreibt man die Vergangenheit von „essen“? (ich esse – ich …) Der Vokal wird lang gesprochen.",
                "aß", ["ass", "as"], B_C,
                info="ich esse – ich aß: Der Vokal wird lang gesprochen, der Laut zischt, also steht ß."))
    a.append(mc("Welches Wort ist richtig geschrieben? Ich … nicht, wo mein Heft ist.",
                "weiß", ["weis", "weiss"], B_C,
                info="ich weiß: „ei“ ist ein Zwielaut, der s-Laut zischt, also steht ß. Die Vergangenheit „ich wusste“ hat einen kurzen Vokal und deshalb ss."))
    a.append(mc("Welche Wörter schreibt man mit s, obwohl man sie nicht verlängern kann? (Merkwörter)",
                ["als", "aus", "bis"], ["Gruß", "Floß"], B_C,
                info="Merkwörter mit s: als, aus, bis, es, etwas, niemals, alles, anders, morgens. Gruß (Grü-ße) und Floß (Flö-ße) kann man verlängern, dort zischt der Laut."))
    a.append(tf("Man schreibt „heiß“ mit ß, weil man verlängern kann: hei-ße Suppe, die erste Silbe ist offen und der Laut zischt.", True, B_C,
                info="Hei-ße: Die erste Silbe endet auf den Zwielaut ei, ist also offen. Der Laut zischt, deshalb ß."))

    # ---------------------------------------------------------------- D: i, ie, ih
    a.append(zuordnen("Verlängere das Wort. Ordne die verlängerte Form zu.",
                      [("Kind", "Kinder"), ("Brief", "Briefe"), ("Schild", "Schilder"), ("Spiel", "spielen"), ("Sieb", "Siebe")],
                      B_D, info="Kin-der (i, geschlossen), Brie-fe (ie, offen), Schil-der (i, geschlossen), spie-len (ie, offen), Sie-be (ie, offen). Beim Verlängern erkennst du, ob die erste Silbe offen ist."))
    a.append(mc("Wann schreibt man oft ie?",
                "Wenn die erste Silbe offen ist und der Vokal lang klingt (Zie-le).",
                ["Wenn die erste Silbe geschlossen ist und der Vokal kurz klingt.", "Immer, wenn ein i im Wort vorkommt.", "Nur bei Verben."], B_D,
                info="Oft ie: offene erste Silbe, langer Vokal, zum Beispiel Zie-le, Brie-fe, Wie-se. Bei geschlossener Silbe (Kin-der) steht i."))
    a.append(mc("Warum schreibt man „Kinder“ nur mit i?",
                "Die erste Silbe (Kin-) ist geschlossen und der Vokal klingt kurz.",
                ["Die erste Silbe ist offen und der Vokal klingt lang.", "Weil „Kinder“ ein Nomen ist.", "Weil das Wort aus drei Silben besteht."], B_D,
                info="Kin-der: Die erste Silbe endet auf n, der Vokal ist kurz. Dann schreibt man i."))
    a.append(luecke("Schreibe die Wörter richtig auf.",
                    "Auf der {{Wiese}} summt eine {{Biene}}, und eine {{Fliege}} sitzt auf einem {{Pilz}}.",
                    B_D, extra=["Wise", "Bine", "Flige", "Pielz"], gross=True,
                    info="Wie-se, Bie-ne und Flie-ge: offene erste Silbe, langer Vokal, also ie. Pilz hat einen kurzen Vokal (Pil-ze), deshalb nur i.",
                tauschbar=[("Biene", "Fliege")]))
    a.append(luecke("Schreibe die Wörter richtig auf.",
                    "Mia schreibt einen {{Brief}} mit blauer {{Tinte}} und hat dabei {{viel}} Spaß.",
                    B_D, extra=["Brif", "Tiente", "fil"], gross=True,
                    info="Brief (Brie-fe, ie), Tin-te (geschlossene Silbe, i), viel (vie-le, ie)."))
    a.append(mc("Wir geben das Buch meinem Bruder zurück. Wir geben es … zurück. Wie schreibt man das fehlende Wort?",
                "ihm", ["im", "iem"], B_D,
                info="„ihm“ ist ein Merkwort mit ih. „im“ (in dem) ist etwas ganz anderes."))
    a.append(luecke("Schreibe die Wörter richtig auf.",
                    "Mama erzählt {{ihr}} eine Geschichte, schenkt {{ihm}} ein Buch und singt {{ihnen}} ein Lied.",
                    B_D, extra=["ir", "inen"], gross=True,
                    info="Die Wörter ihr, ihm, ihn, ihnen und ihre sind Merkwörter. Man schreibt sie mit ih.",
                tauschbar=[("ihr", "ihm", "ihnen")]))
    a.append(tf("Die Wörter mir, dir und wir schreibt man nur mit i.", True, B_D,
                info="mir, dir und wir sind Merkwörter und werden nur mit einfachem i geschrieben (anders als ihr, ihm, ihn)."))
    a.append(mc("Bei welchen Wörtern klingt das i lang, obwohl nur ein i geschrieben wird? (mehrere Antworten sind richtig)",
                ["Kino", "Kilo", "Tiger"], ["Kinder", "Tinte"], B_D,
                info="Kino, Kilo und Tiger sind Fremdwörter mit langem i und einfachem i. Bei Kinder und Tinte ist das i kurz und die erste Silbe geschlossen."))
    a.append(mc("Welches Wort ist richtig geschrieben? Darf ich das Eis …?",
                "probieren", ["probiren", "probihren"], B_D,
                info="Verben auf -ieren schreibt man mit ie: probieren, trainieren, musizieren, verlieren."))
    a.append(tf("Man schreibt „Schild“ mit ie, weil beim Verlängern (Schilder) die erste Silbe offen ist.", False, B_D,
                info="Schil-der: Die erste Silbe endet auf l, sie ist geschlossen. Deshalb schreibt man i: Schild."))

    # ---------------------------------------------------------------- E: h und Doppelvokale
    a.append(zuordnen("Verlängere das Wort. Ordne die verlängerte Form zu. Dort hörst du das h.",
                      [("Kuh", "Kühe"), ("Reh", "Rehe"), ("geht", "gehen"), ("zieht", "ziehen"), ("Schuh", "Schuhe")],
                      B_E, info="Beim Verlängern hörst du das h am Anfang der zweiten Silbe: Kü-he, Re-he, ge-hen, zie-hen, Schu-he. Das ist das silbenöffnende h."))
    a.append(mc("Wie erkennst du ein silbenöffnendes h?",
                "Man verlängert das Wort und hört das h am Anfang der zweiten Silbe (Kuh – Kü-he).",
                ["Man hört das h immer deutlich im Einsilber.", "Das h steht immer am Wortanfang.", "Nach jedem langen Vokal steht ein h."], B_E,
                info="Bei Einsilbern hört man das h nicht. Nach dem Verlängern steht es am Anfang der zweiten Silbe und ist hörbar: Kü-he, zie-hen."))
    a.append(mc("Welche Wörter haben ein silbenöffnendes h (hörbar beim Verlängern)? (mehrere Antworten sind richtig)",
                ["ziehen", "ruhen", "Mühe"], ["Zahl", "wohnen"], B_E,
                info="zie-hen, ru-hen, Mü-he: Das h steht am Anfang der zweiten Silbe. Bei Zahl (Zah-len) und woh-nen steht das h am Ende der ersten Silbe, vor l und n. Diese Wörter sind Merkwörter."))
    a.append(zuordnen("Welcher Buchstabe steht direkt hinter dem h?",
                      [("Zahl", "l"), ("zahm", "m"), ("Wohnung", "n"), ("Lehrer", "r"), ("Fehler", "l")],
                      B_E, info="Das h steht oft vor l, m, n oder r: Zahl, zahm, Woh-nung, Leh-rer, Feh-ler. Man hört es nicht, deshalb sind das Merkwörter."))
    a.append(luecke("Schreibe die Wörter richtig auf.",
                    "Der {{Lehrer}} {{zählt}} die Kinder, und die Klasse {{wählt}} ihre Sprecherin.",
                    B_E, extra=["Lerer", "zält", "wält"], gross=True,
                    info="Leh-rer, zäh-len (Zahl), wäh-len (Wahl): Das h steht vor l oder r und ist ein Merkwort-h.",
                tauschbar=[("zählt", "wählt")]))
    a.append(luecke("Schreibe die Wörter richtig auf.",
                    "Mein Onkel {{wohnt}} schon ein {{Jahr}} in der {{Nähe}}.",
                    B_E, extra=["wont", "Jar", "Nehe"], gross=True,
                    info="wohnt (woh-nen), Jahr (Merkwort mit h) und Nähe (Nä-he, silbenöffnendes h) schreibt man mit h."))
    a.append(tf("Bei „Zahl“ hört man das h beim Verlängern (Zah-len).", False, B_E,
                info="Das h steht am Ende der ersten Silbe (Zahl, Zah-len) und ist nicht zu hören. Wörter mit h vor l, m, n und r sind Merkwörter."))
    a.append(mc("Welches Wort ist richtig geschrieben? Das Schiff fährt über das …",
                "Meer", ["Mehr", "Mer"], B_E,
                info="Meer ist ein Wort mit Doppelvokal ee. „mehr“ (mehr Wasser) ist ein anderes Wort."))
    a.append(luecke("Schreibe die Wörter richtig auf.",
                    "Am {{See}} liegt ein {{Boot}}, und im {{Beet}} wächst {{Klee}}.",
                    B_E, extra=["Sehe", "Bot", "Bet", "Kle"], gross=True,
                    info="See, Boot, Beet und Klee haben einen Doppelvokal. Das sind Merkwörter, die man auswendig lernen muss."))
    a.append(mc("Welches Wort ist richtig geschrieben? Im Park gibt es eine lange …",
                "Allee", ["Alee", "Aleh"], B_E,
                info="Fremdwörter mit ee am Ende: Allee, Idee, Kaffee, Püree, Tee."))
    a.append(zuordnen("Welcher Doppelvokal steckt im Wort?",
                      [("Haar", "aa"), ("Schnee", "ee"), ("Moos", "oo"), ("Saal", "aa"), ("Zoo", "oo"), ("Fee", "ee")],
                      B_E, info="aa: Haar, Saal. ee: Schnee, Fee. oo: Moos, Zoo. Diese Wörter muss man sich merken."))
    a.append(kurz("Wie heißt das warme Getränk aus Blättern oder Kräutern?", "Tee", B_E, gross=True,
                  info="Tee schreibt man mit Doppelvokal ee, genau wie Kaffee, Idee und Allee."))
    a.append(kurz("Wie heißt das kleine Schiff, mit dem man auf einem See rudern kann?", "Boot", B_E, gross=True,
                  info="Boot schreibt man mit Doppelvokal oo, genau wie Moor, Moos und Zoo."))
    return a


def build():
    p = pack(ID, "Deutsch Teil 3a: Rechtschreibung 1",
             "Silben schwingen (offen und geschlossen), Doppelkonsonanten, ck und tz, s/ss/ß, i/ie/ih, silbenöffnendes h und Doppelvokale. Mit Lernblatt und Übungsaufgaben.",
             lernblatt(), aufgaben(), min_aufgaben=60,
             hinweis="Alle Sätze, Texte und Namen sind selbst ausgedacht, nicht aus dem Deutschbuch oder Aufgabenheft. Die Regeln stehen so auch im Deutschbuch (S. 313–317) und im Aufgabenheft (S. 64–81). In der App zählen ß und ss beim Tippen als gleich. Deshalb entscheidest du bei s, ss und ß nur über die Auswahl. Bei den Lücken zählt jeder Buchstabe: Tippe das Wort genau so, wie es geschrieben werden muss.")
    return [nachlesen(p, {B_A: L1, B_B: L2, B_C: [L3, L4], B_D: L5, B_E: L6})]


if __name__ == "__main__":
    for p in build():
        print(p["id"], len(p["aufgaben"]), "Aufgaben")
