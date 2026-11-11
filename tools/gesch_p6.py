"""Geschichte Klasse 6, Teil 6: Ötzi, der Mann aus dem Eis (Lernzettel Punkt 8, Buch S. 32 bis 33).

Buch S. 32/33 ist maßgeblich. Die Kopie (anderes Buch) hat leicht andere Zahlen (Alter, Höhe, Gewicht):
Solche Zahlen werden nur gerundet gefragt oder beide Werte werden akzeptiert.
"""
from gesch_lib import *
from gesch_lib import _svg, _label, _num, _arrow

# ------------------------------------------------------------------ Zahlen (alles berechnet und geprüft)

OETZI_VON, OETZI_BIS, OETZI_MITTE = -3359, -3105, -3300
HEUTE = 2026
ROEMER = -753                      # sagenhafte Gründung Roms (Heft)
FUND = 1991

assert OETZI_VON < OETZI_MITTE < OETZI_BIS < -3000
assert epoche(OETZI_VON) == epoche(OETZI_MITTE) == epoche(OETZI_BIS) == "Ur- und Frühgeschichte"
assert -9000 < OETZI_VON and OETZI_BIS < -3000        # Ende der Jungsteinzeit (Heft: ca. 9000 bis 3000 v. Chr.)
assert epoche(-2500) == "Altertum"                          # nächste Epoche nach Ötzis Zeit
DAUER = spanne(OETZI_VON, OETZI_BIS)
assert DAUER == 254
ABSTAND = spanne(OETZI_MITTE, HEUTE)                        # Jahre bis heute (v. Chr. und n. Chr. zusammenrechnen)
assert ABSTAND == 3300 + 2026 == 5326 and round(ABSTAND, -2) == 5300
ABSTAND_RUND = int(round(ABSTAND, -2))
ABSTAND_2000 = spanne(OETZI_MITTE, 2000)
assert ABSTAND_2000 == 5300
FALSCH_SUBTRAKTION = abs(abs(OETZI_MITTE) - HEUTE)          # typischer Fehler: 3300 - 2026
assert round(FALSCH_SUBTRAKTION, -2) == 1300
assert spanne(OETZI_BIS, ROEMER) == 2352 and spanne(OETZI_BIS, ROEMER) > 2000   # Ötzi lebte lange vor der Gründung Roms
assert spanne(OETZI_MITTE, FUND) > 5000                     # über 5000 Jahre alt (Buch 5250, Kopie 5400)
assert 5000 < ABSTAND - (HEUTE - FUND) < 5400

BOZEN = "Bozen"


def _varianten(zahlen, praefixe=("", "ca. ", "etwa "), suffixe=("", " Jahre")):
    """Natürliche Schreibweisen einer Zahl (kurz-Aufgaben vergleichen exakt): Präfix + Zahl + Suffix, ohne Doppelte."""
    out = []
    for z in zahlen:
        for p in praefixe:
            for x in suffixe:
                v = f"{p}{z}{x}"
                if v not in out:
                    out.append(v)
    return out


def _zahlformen(n):
    """5300 -> ['5300', '5.300', '5 300']"""
    a = str(n)
    return [a, f"{n:,}".replace(",", "."), f"{n:,}".replace(",", " ")]


# ------------------------------------------------------------------ Zeichnungen

def _txt(x, y, text, anchor="middle", size=16, weight="bold", fill="#1b1b1b"):
    """Beschriftung mit weißem Rand."""
    return (f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" '
            f'stroke="#fff" stroke-width="4" paint-order="stroke" stroke-linejoin="round">{text}</text>')


def svg_oetzi_zeit(abstand=None):
    """Zeitstrahl von 3500 v. Chr. bis 2100 n. Chr. (maßstäblich): Ötzis Lebenszeit, Christi Geburt und heute.

    abstand: Text für den Doppelpfeil zwischen Ötzi und heute (zum Beispiel 'etwa 5300 Jahre'), None = ohne Pfeil.
    """
    von, bis = -3500, 2100
    x0, x1 = 40, 720
    X = lambda y: x0 + (y - von) * (x1 - x0) / (bis - von)
    ay = 150
    g = [f'<line x1="{x0 - 20}" y1="{ay}" x2="{x1 + 25}" y2="{ay}" stroke="#222" stroke-width="3"/>']
    for y in range(-3000, 2001, 1000):
        x = round(X(y), 1)
        g.append(f'<line x1="{x}" y1="{ay - 10}" x2="{x}" y2="{ay + 10}" stroke="#222" stroke-width="2.4"/>')
        g.append(_txt(x, ay + 34, "Christi Geburt" if y == 0 else jahr(y), size=15))
    # Ur- und Frühgeschichte (bis 3000 v. Chr.)
    xe = round(X(-3000), 1)
    g.append(f'<line x1="22" y1="{ay + 52}" x2="{xe}" y2="{ay + 52}" stroke="#a9895c" stroke-width="6" stroke-linecap="round"/>')
    g.append(_txt(22, ay + 78, "Ur- und Frühgeschichte (bis 3000 v. Chr.)", anchor="start", size=15, weight="normal"))
    # Ötzi
    xa, xb = round(X(OETZI_VON), 1), round(X(OETZI_BIS), 1)
    g.append(f'<rect x="{xa}" y="{ay - 26}" width="{xb - xa:.1f}" height="26" fill="#e2701a" stroke="#a14a00" stroke-width="2"/>')
    g.append(_txt(40, ay - 36, f"Ötzi: {abs(OETZI_VON)}–{jahr(OETZI_BIS)}", anchor="start", size=16))
    # heute
    xh = round(X(HEUTE), 1)
    g.append(f'<line x1="{xh}" y1="{ay}" x2="{xh}" y2="{ay - 62}" stroke="#3b6ea5" stroke-width="2.5" stroke-dasharray="6 4"/>')
    g.append(f'<circle cx="{xh}" cy="{ay}" r="6" fill="#3b6ea5"/>')
    g.append(_txt(xh - 8, ay - 36, f"heute ({HEUTE})", anchor="end", size=16, fill="#2a5585"))
    if abstand:
        xm = round(X(OETZI_MITTE), 1)
        mid = round((xm + xh) / 2, 1)
        g.append(_arrow(mid, ay - 62, xm, ay - 62, "#333", 2.5))
        g.append(_arrow(mid, ay - 62, xh, ay - 62, "#333", 2.5))
        g.append(_txt(mid, ay - 72, abstand, size=17))
    return _svg(760, 240, ''.join(g))


AUSRUESTUNG = ["Bogen", "Köcher mit Pfeilen", "Kupferbeil", "Steindolch", "Gefäß für Glut", "Fellmütze"]


def _ic_bogen():
    return ('<path d="M 88,34 Q 172,84 88,134" fill="none" stroke="#7a4f24" stroke-width="8" stroke-linecap="round"/>'
            '<line x1="88" y1="34" x2="88" y2="134" stroke="#555" stroke-width="2.5"/>'
            '<line x1="66" y1="84" x2="176" y2="84" stroke="#6b4a2a" stroke-width="3.5" stroke-linecap="round"/>'
            '<polygon points="190,84 174,77 174,91" fill="#777"/>'
            '<line x1="66" y1="84" x2="58" y2="77" stroke="#6b4a2a" stroke-width="3"/><line x1="66" y1="84" x2="58" y2="91" stroke="#6b4a2a" stroke-width="3"/>')


def _ic_koecher():
    return ('<g transform="rotate(8 120 95)">'
            '<line x1="108" y1="64" x2="102" y2="34" stroke="#6b4a2a" stroke-width="3.5"/>'
            '<line x1="120" y1="64" x2="120" y2="30" stroke="#6b4a2a" stroke-width="3.5"/>'
            '<line x1="132" y1="64" x2="138" y2="34" stroke="#6b4a2a" stroke-width="3.5"/>'
            '<polygon points="102,24 96,38 108,38" fill="#777"/><polygon points="120,20 114,34 126,34" fill="#777"/><polygon points="138,24 132,38 144,38" fill="#777"/>'
            '<rect x="97" y="62" width="46" height="76" rx="9" fill="#b98a55" stroke="#6b4a2a" stroke-width="3"/>'
            '<line x1="97" y1="84" x2="143" y2="84" stroke="#6b4a2a" stroke-width="2.5"/><line x1="97" y1="116" x2="143" y2="116" stroke="#6b4a2a" stroke-width="2.5"/>'
            '</g>')


def _ic_beil():
    return ('<line x1="102" y1="140" x2="102" y2="36" stroke="#8a5a2b" stroke-width="11" stroke-linecap="round"/>'
            '<polygon points="108,42 168,24 168,92 108,74" fill="#d2773a" stroke="#8a3f10" stroke-width="3" stroke-linejoin="round"/>'
            '<line x1="118" y1="52" x2="118" y2="68" stroke="#8a3f10" stroke-width="2"/>')


def _ic_dolch():
    return ('<rect x="46" y="76" width="62" height="20" rx="7" fill="#a87b4a" stroke="#6b4a2a" stroke-width="3"/>'
            '<polygon points="108,70 196,86 108,102" fill="#d9d4c7" stroke="#666" stroke-width="3" stroke-linejoin="round"/>')


def _ic_glut():
    return ('<path d="M 62,78 Q 62,140 120,140 Q 178,140 178,78 Z" fill="#b98a55" stroke="#6b4a2a" stroke-width="3"/>'
            '<ellipse cx="120" cy="78" rx="58" ry="12" fill="#5a3f22" stroke="#6b4a2a" stroke-width="3"/>'
            '<circle cx="98" cy="78" r="7" fill="#e2701a"/><circle cx="120" cy="75" r="8" fill="#f4a233"/><circle cx="142" cy="79" r="7" fill="#e2701a"/>')


def _ic_muetze():
    return ('<path d="M 64,106 Q 64,40 120,40 Q 176,40 176,106 Z" fill="#7a5a3a" stroke="#4d3822" stroke-width="3"/>'
            '<rect x="56" y="98" width="128" height="30" rx="15" fill="#a07b52" stroke="#4d3822" stroke-width="3"/>'
            '<path d="M 76,113 l 8,-8 m 12,8 l 8,-8 m 12,8 l 8,-8 m 12,8 l 8,-8 m 12,8 l 8,-8" fill="none" stroke="#4d3822" stroke-width="2.5"/>')


def svg_ausruestung(namen=True):
    """Skizze mit sechs Teilen von Ötzis Ausrüstung (vereinfacht, nicht maßstäblich), nummeriert 1 bis 6."""
    icons = [_ic_bogen, _ic_koecher, _ic_beil, _ic_dolch, _ic_glut, _ic_muetze]
    g = []
    for i, ic in enumerate(icons):
        ox, oy = 10 + (i % 3) * 250, 10 + (i // 3) * 190
        g.append(f'<g transform="translate({ox},{oy})">'
                 f'<rect x="0" y="0" width="240" height="180" rx="10" fill="#faf6ec" stroke="#cdbf9f" stroke-width="2"/>'
                 f'{ic()}{_num(22, 22, i + 1)}')
        if namen:
            g.append(_txt(120, 168, AUSRUESTUNG[i], size=17))
        g.append('</g>')
    return _svg(760, 390, ''.join(g))


ALT_ZEIT = (f"Zeitstrahl von 3500 v. Chr. bis 2100 n. Chr. mit Ötzis Lebenszeit ({abs(OETZI_VON)} bis {jahr(OETZI_BIS)}) ganz links, "
            f"Christi Geburt in der Mitte und heute ({HEUTE}) ganz rechts")
ALT_AUSR = ("Skizze mit sechs nummerierten Teilen von Ötzis Ausrüstung: 1 Bogen, 2 Köcher mit Pfeilen, 3 Kupferbeil, "
            "4 Steindolch, 5 Gefäß für Glut, 6 Fellmütze")


# ------------------------------------------------------------------ Lernblatt

T_FUND = "Der Fund im Eis"
T_WER = "Wer war Ötzi?"
T_WANN = "Wann lebte Ötzi?"
T_AUSR = "Kleidung und Ausrüstung"
T_WANDERER = "Wanderer zwischen den Zeiten"
T_TOT = "Ötzi wurde getötet"
T_KRIMI = "Kriminalfall Ötzi: Woher weiß man das?"
T_BELEGT = "Belegt oder vermutet? Quelle oder Darstellung?"
T_MUSEUM = "Ötzi im Museum"


def lernblatt():
    return [
        lb(T_FUND,
           "Im Herbst **1991** war ein deutsches Ehepaar in den **Ötztaler Alpen** auf Bergtour. Beim Abstieg nahmen die beiden eine Abkürzung. "
           "Dabei entdeckten sie in über 3000 m Höhe einen Toten im **Gletscher** (ein riesiger, langsam fließender Strom aus Eis). "
           "Der Körper war im Eis erhalten geblieben. So einen Körper nennt man **Mumie**.\n"
           "Zuerst dachte man, es sei ein **verunglückter Bergsteiger**. Das stimmte nicht: Die Untersuchungen zeigten, dass der Mann über **5000 Jahre** alt war. "
           "Nach dem Fundort bekam er den Namen **„Ötzi“** (Ötztaler Alpen).\n"
           "Buch und Kopie nennen leicht verschiedene Zahlen: Das Buch schreibt 3210 m Höhe und etwa 5250 Jahre, die Kopie 3200 m und etwa 5400 Jahre. "
           "Du musst dir nur merken: **über 3000 m** (zwischen 3000 und 3500 m) und **über 5000 Jahre** (zwischen 5000 und 5500 Jahren).",
           merke="Ötzi wurde im Herbst 1991 von einem Ehepaar in den Ötztaler Alpen im Gletscher gefunden. Er war über 5000 Jahre alt. "
                 "Zuerst hielt man ihn für einen verunglückten Bergsteiger."),
        lb(T_WER,
           "Forscher haben Ötzi mit modernsten Methoden untersucht. Darum weiß man heute viel über ihn:\n"
           "- **Alter**: etwa 46 Jahre (die Kopie sagt 45, also Mitte 40). Für die damalige Zeit war das ein hohes Alter.\n"
           "- **Aussehen**: etwa 1,60 m groß, etwa 50 kg schwer (die Kopie nennt 40 kg), laut Buch blaue Augen, dunkelbraunes oder schwarzes Haar.\n"
           "- **Gesundheit**: abgenutzte Gelenke, verkalkte Blutgefäße, schon verheilte Rippenbrüche und ein verheilter Nasenbeinbruch, "
           "Erfrierungen am linken Fuß und Parasiten im Darm (sie machten Durchfall).\n"
           "- **Zähne**: ohne Karies, aber stark abgenutzt. Vielleicht benutzte er seine Zähne als Werkzeug.\n"
           "- **Tätowierungen**: über 50 Striche und Kreuze auf der Haut, an Stellen der **Akupunktur** (einer Behandlung, bei der man bestimmte Körperstellen reizt). "
           "Vielleicht war das eine frühe Behandlung gegen Schmerzen.",
           merke="Ötzi war etwa 46 Jahre alt, etwa 1,60 m groß und hatte laut Buch blaue Augen. Er hatte abgenutzte Gelenke, verheilte Brüche, "
                 "Erfrierungen am linken Fuß und über 50 Tätowierungen."),
        lb(T_WANN,
           f"Ötzi lebte zwischen **{abs(OETZI_VON)} und {jahr(OETZI_BIS)}** in der sogenannten **Kupfersteinzeit**: "
           "Die Menschen lebten noch wie in der Jungsteinzeit, aber sie begannen schon, mit **Kupfer** (einem Metall) zu arbeiten. "
           "Damit bereiteten sie die Zeiten vor, in denen Metall wichtig wurde.\n"
           "Nach den Epochen aus dem Heft gehört Ötzi zur **Ur- und Frühgeschichte** (bis 3000 v. Chr.). "
           "Die nächste Epoche, das **Altertum**, beginnt erst nach seiner Zeit. Innerhalb der Steinzeit liegt er nach den Jahreszahlen am Ende der **Jungsteinzeit** (ca. 9000 bis 3000 v. Chr.). "
           f"Zum Vergleich: Rom wurde der Sage nach erst {jahr(ROEMER)} gegründet, also mehr als 2000 Jahre nach Ötzi.\n"
           "So rechnest du den Abstand zu heute: Ötzi lebte vor Christi Geburt, wir leben danach. Darum rechnest du die Jahre **zusammen**. "
           f"Beispiel: von {jahr(OETZI_MITTE)} bis {HEUTE} n. Chr. sind es {abs(OETZI_MITTE)} + {HEUTE} = {ABSTAND}, also **etwa {ABSTAND_RUND} Jahre**. "
           "Ein Jahr 0 gibt es nicht, in der Schule rechnet man einfach zusammen.",
           merke=f"Ötzi lebte {abs(OETZI_VON)} bis {jahr(OETZI_BIS)}, also vor etwa {ABSTAND_RUND} Jahren, in der Kupfersteinzeit. "
                 "Seine Epoche ist die Ur- und Frühgeschichte.",
           bild=svg_oetzi_zeit(f"etwa {ABSTAND_RUND} Jahre"),
           bildAlt=ALT_ZEIT + ". Ein Doppelpfeil zeigt den Abstand von etwa 5300 Jahren."),
        lb(T_AUSR,
           "Bei Ötzi lagen viele Gegenstände. Sie sind **Sachquellen**, denn man kann aus ihnen etwas über seine Zeit lernen:\n"
           "- **Fellkleidung**: wintertauglich. Laut Kopie gehörten auch Lederschuhe, eine Mütze aus Bärenfell und ein Umhang aus Gras dazu.\n"
           "- **Bogen und Köcher** mit Pfeilen. Der Köcher war laut Kopie aus Gamsleder, einer der Pfeile hatte eine Steinspitze.\n"
           "- **Steindolch**: Klinge aus Feuerstein, Griff aus Eschenholz (laut Kopie).\n"
           "- **Kupferbeil**: etwa 60 cm lang, Klinge aus gegossenem Kupfer, Schaft (der Stiel, an dem die Klinge befestigt ist) aus **Eibenholz**. "
           "Es ist das einzige vollständig erhaltene Beil aus der Vorgeschichte auf der ganzen Welt.\n"
           "- **Gefäß für Glut**: Ötzi hatte Glut dabei, um unterwegs Feuer zu haben.\n"
           "- Dazu laut Kopie: ein Bohrer aus Feuerstein und eine Schnur aus Baumbast (der inneren Schicht der Baumrinde).",
           merke="Fast alle Teile von Ötzis Ausrüstung sind steinzeitlich. Nur das Kupferbeil mit der Metallklinge zeigt schon die neue Zeit.",
           bild=svg_ausruestung(True), bildAlt=ALT_AUSR),
        lb(T_WANDERER,
           "Das Buch nennt Ötzi einen **„Wanderer zwischen den Zeiten“**. Gemeint ist nicht, dass er viel gewandert ist, "
           "sondern dass er in einer **Übergangszeit** lebte: zwischen der Steinzeit und der Zeit, in der Metall wichtig wurde.\n"
           "Das siehst du an seiner Ausrüstung. Fellkleidung, Steindolch, Bogen und Pfeile mit Steinspitze sind steinzeitlich. "
           "Das Kupferbeil ist neu und zeigt den Weg zu den Metallzeiten.\n"
           "Was verrät die Ausrüstung noch über sein Leben? Das sind **Schlüsse**, keine sicheren Tatsachen:\n"
           "- Er konnte Werkzeug und Waffen selbst herstellen und ausbessern (Bohrer, halbfertiger Bogen, Rohlinge für Pfeilschäfte).\n"
           "- Er war auf Kälte vorbereitet (wintertaugliche Fellkleidung).\n"
           "- Er nahm Feuer in Form von Glut mit.\n"
           "- Er kannte Kupfer und besaß ein Beil daraus.",
           merke="„Wanderer zwischen den Zeiten“ heißt: Ötzi lebte zwischen Steinzeit und Metallzeit. Fast alles an ihm ist steinzeitlich, das Kupferbeil ist neu."),
        lb(T_TOT,
           "Lange wusste man nicht, woran Ötzi gestorben war. Heute weiß man: Er war das **Opfer einer Gewalttat**.\n"
           "- In seiner **linken Schulter** steckte eine **Pfeilspitze**.\n"
           "- Er **verblutete** innerhalb weniger Minuten (die Kopie spricht von inneren Blutungen).\n"
           "- An der **rechten Hand** hatte er eine tiefe **Schnittwunde**. Sie deutet auf einen Nahkampf kurz vor seinem Tod.\n"
           "Wer ihn getötet hat und warum, ist bis heute ein Rätsel. Sein Körper blieb Jahrtausende im Gletschereis verborgen.",
           merke="Ötzi wurde von einem Pfeil in die linke Schulter getroffen und verblutete. Wer es war und warum, weiß man nicht."),
        lb(T_KRIMI,
           "Im Buch (S. 33) erzählt der Arzt **Eduard Egarter-Vigl** (2011) Ötzis letzte Minuten wie einen Kriminalfall. "
           "Er stützt sich auf Untersuchungen:\n"
           "- **Pollen** (Blütenstaub) in Lunge und Darm: Sie blühen nur im Frühling und Frühsommer. Ötzi war also in dieser Jahreszeit unterwegs.\n"
           "- **Mikroskop**: Die Wundränder an der Hand zeigen, dass die Verletzung ein bis drei Tage alt war.\n"
           "- **Computertomografie** (CT, ein Röntgenverfahren, das Bilder vom Inneren des Körpers macht): Der Magen war gut gefüllt, "
           "der Inhalt kaum verdaut. Die letzte Mahlzeit lag höchstens eine Stunde zurück.\n"
           "- **Halbfertiger Bogen und Rohlinge für Pfeilschäfte** (grob vorgearbeitete Holzstücke): Ötzi musste seine Waffen erneuern.\n"
           "So erzählt der Arzt den Ablauf: Die Hand wird verletzt. Ötzi steigt müde über die Baumgrenze (die Höhe, ab der keine Bäume mehr wachsen) und trinkt aus Bächen. "
           "Zwischen Felsen sucht er einen Rastplatz, lehnt die Ausrüstung an den Fels und setzt sich zum Essen. Dann trifft ihn der Pfeil. "
           "Er verliert das Gleichgewicht und fällt nieder.",
           merke="Pollen zeigen die Jahreszeit, das Mikroskop das Alter der Wunde, die Computertomografie die letzte Mahlzeit."),
        lb(T_BELEGT,
           "**Belegt** heißt: Ein Fund oder eine Untersuchung stützt die Aussage. **Vermutet** heißt: Es ist möglich oder wahrscheinlich, aber nicht bewiesen. "
           "Auf Vermutungen weisen **Wörter der Unsicherheit** hin: wohl, vermutlich, wahrscheinlich, vielleicht, eventuell.\n"
           "- **Belegt**: die Pfeilspitze in der linken Schulter, die tiefe Schnittwunde an der Hand, der gefüllte Magen, die verkalkten Blutgefäße.\n"
           "- **Nur vermutet**: dass die Tätowierungen gegen Schmerzen waren, dass er die Zähne als Werkzeug benutzte, "
           "ob der Schütze sich anschlich oder wartete, wer Ötzi tötete und warum.\n"
           "**Quelle** oder **Darstellung**? Eine Quelle stammt aus der Zeit selbst: die Mumie, die Kleidung, das Beil, die Pfeilspitze. "
           "Eine Darstellung machen Menschen später, die die Zeit nicht erlebt haben, mithilfe von Quellen: der Text des Arztes, "
           "die Rekonstruktion von 2011, der Schulbuchtext.\n"
           "Im Heft sollst du Aussagen prüfen. Prüfe Teil für Teil. „Ötzi wurde von einem Pfeil getroffen und hat sehr viel Blut verloren“ ist belegt "
           "(Pfeilspitze, verblutet). Bei „weit gelaufen“ ist es eine Einschätzung: Die Funde zeigen nur, dass er über die Alpen unterwegs und vom Aufstieg müde war. "
           "Vergleiche das mit dem, was in deinem Heft dazu steht. "
           "„Ötzi ist in Italien gestorben“: Man fand ihn in den Ötztaler Alpen an der Grenze zu Italien, und die Mumie liegt heute in Bozen in Italien. "
           "Zusatzwissen: Das Land Italien gab es zu Ötzis Zeit noch nicht.",
           merke="Belegt = durch Funde oder Untersuchungen gestützt. Vermutet = Wörter wie wohl, vielleicht, vermutlich. "
                 "Quelle = Hinterlassenschaft der Zeit (Mumie, Fundstücke). Darstellung = spätere Deutung (Arzttext, Zeichnung, Schulbuch)."),
        lb(T_MUSEUM,
           "Die Mumie liegt im **Südtiroler Archäologiemuseum in Bozen** (Italien) in einem eigens gebauten **Kühlraum**. Sie ist dort ein Ausstellungsstück.\n"
           "Manche Menschen finden das **würdelos**. Andere finden es in Ordnung. Das Buch fragt nach Gründen dafür und dagegen. Beispiele:\n"
           "- **Spricht für „würdelos“**: Ein Mensch wird wie ein Ausstellungsstück angeschaut. Man hat ihn nicht gefragt. Tote sollen in Ruhe liegen.\n"
           "- **Spricht dagegen**: Ötzi ist schon lange tot und spürt nichts mehr. Die Forschung lernt durch ihn viel über die Steinzeit. "
           "Er wird sorgfältig in einem Kühlraum aufbewahrt.\n"
           "Bei dieser Aufgabe gibt es keine einzig richtige Meinung. Du musst aber **begründen**, was du denkst.",
           merke="Mumie in Bozen im Kühlraum. Würdelos oder nicht? Nenne einen Grund dafür, einen dagegen und begründe dann deine eigene Meinung."),
    ]


# ------------------------------------------------------------------ Aufgaben

S_A = "A – Der Fund im Eis"
S_B = "B – Wer war Ötzi?"
S_C = "C – Wann lebte Ötzi?"
S_D = "D – Kleidung und Ausrüstung"
S_E = "E – Tod und Kriminalfall"
S_F = "F – Quelle, Darstellung, belegt oder vermutet"
S_G = "G – Museum und klausurnahe Aufgaben"


def aufgaben_a():
    s = S_A
    return [
        kurz("In welchem Jahr wurde Ötzi gefunden?",
             [str(FUND), f"{FUND} n. Chr.", f"im Jahr {FUND}", f"im Herbst {FUND}", f"Herbst {FUND}"], s,
             info="Im Herbst 1991 entdeckte ein Ehepaar den Toten im Gletscher. Buch und Kopie nennen dasselbe Jahr."),
        mc("Wer entdeckte den Toten im Gletscher?", "Ein Ehepaar auf einer Bergtour",
           ["Ein Forscherteam bei einer Ausgrabung", "Zwei Schäfer auf der Alm", "Arbeiter beim Bau einer Seilbahn"], s,
           info="Ein deutsches Ehepaar nahm beim Abstieg eine Abkürzung und stieß dabei auf den Toten."),
        kurz("Nach welchem Gebirge hat Ötzi seinen Namen?", ["Ötztaler Alpen", "die Ötztaler Alpen", "den Ötztaler Alpen", "nach den Ötztaler Alpen", "Ötztaler", "Ötztal"], s,
             info="Er wurde in den Ötztaler Alpen gefunden und nach dem Fundort „Ötzi“ genannt.",
             tipp="Der Name steckt schon im Namen „Ötzi“."),
        luecke("Ergänze den Text über den Fund.",
               "Im Herbst {{1991}} entdeckte ein {{Ehepaar}} in den {{Ötztaler Alpen}} einen Toten im {{Gletscher}}. "
               "Zuerst hielt man ihn für einen verunglückten {{Bergsteiger}}. In Wirklichkeit war er über {{5000|5.000}} Jahre alt.",
               s, extra=["Hirten", "500"],
               info="Der Fund war 1991. Erst die Untersuchungen zeigten, dass der Tote über 5000 Jahre alt war."),
        mc("In welcher Höhe lag die Fundstelle ungefähr?", "zwischen 3000 und 3500 m",
           ["zwischen 2000 und 2500 m", "zwischen 1000 und 1500 m", "zwischen 300 und 500 m"], s,
           info="Das Buch nennt 3210 m, die Kopie 3200 m. In beiden Fällen sind es über 3000 m, hoch oben im Gletscher.",
           tipp="Es war ein Gletscher im Hochgebirge."),
        mc("Wie alt ist die Mumie ungefähr?", "zwischen 5000 und 5500 Jahren",
           ["zwischen 3000 und 3500 Jahren", "zwischen 1000 und 1500 Jahren", "zwischen 100 und 500 Jahren"], s,
           info="Das Buch nennt etwa 5250 Jahre, die Kopie etwa 5400 Jahre. Beide Zahlen liegen zwischen 5000 und 5500 Jahren, die Mumie ist also über 5000 Jahre alt.",
           tipp="Ötzi lebte um 3300 v. Chr. Rechne die Jahre bis heute zusammen."),
        tf("Zuerst hielt man den Toten für einen verunglückten Bergsteiger.", True, s,
           info="Erst die Untersuchung zeigte, dass der Mann über 5000 Jahre alt war."),
        reihenfolge("Bringe den Weg von Ötzis Tod bis zum Museum in die richtige Reihenfolge.",
                    ["Ötzi wird von einem Pfeil getroffen und stirbt.",
                     "Sein Körper bleibt Jahrtausende im Gletschereis verborgen.",
                     "Im Herbst 1991 entdeckt ein Ehepaar den Leichnam.",
                     "Zuerst glaubt man, es sei ein verunglückter Bergsteiger.",
                     "Die Mumie kommt in einen Kühlraum im Museum in Bozen."], s,
                    info="Ötzi starb vor über 5000 Jahren und lag lange im Eis. Entdeckt wurde er erst 1991, später kam die Mumie ins Museum.",
                    tipp="Fange bei Ötzis Tod an und höre beim Museum auf."),
    ]


def aufgaben_b():
    s = S_B
    return [
        mc("Wie groß war Ötzi ungefähr?", "etwa 1,60 m", ["etwa 1,30 m", "etwa 1,90 m", "etwa 2,05 m"], s,
           info="Buch und Kopie nennen beide etwa 1,60 m. Beim Gewicht weichen sie ab (50 kg und 40 kg)."),
        kurz("Wie alt war Ötzi ungefähr, als er starb? Schreibe die Zahl.",
             _varianten(["46", "45"], ("", "ca. ", "etwa ", "ungefähr "), ("", " Jahre", " Jahre alt")), s,
             info="Das Buch nennt etwa 46 Jahre, die Kopie 45. Beide Werte sind richtig: Ötzi war Mitte 40, für damals ein hohes Alter."),
        mc("Etwa wie viele Tätowierungen (Striche und Kreuze) hatte Ötzi auf der Haut?", "mehr als 50",
           ["weniger als 10", "10 bis 30", "31 bis 50"], s,
           info="Es waren über 50 Striche und Kreuze auf der Haut, an Stellen der Akupunktur.",
           tipp="Es waren sehr viele Striche und Kreuze."),
        mc("Welche Befunde hat man an Ötzis Körper festgestellt? Wähle alle richtigen Antworten.",
           ["Erfrierungen am linken Fuß", "Verheilte Rippenbrüche", "Verkalkte Blutgefäße"],
           ["Ein frisch gebrochenes Bein", "Ein Gebiss voller Karies"], s,
           info="Alle drei richtigen Befunde stehen im Buch. Die Zähne waren ohne Karies, und Brüche waren schon verheilt.",
           tipp="Vergleiche mit der Liste im Lernblatt."),
        tf("Ötzis Zähne waren stark abgenutzt, hatten aber keine Karies.", True, s,
           info="Vielleicht hat er die Zähne als Werkzeug benutzt. Das ist eine Vermutung, kein Beweis."),
        mc("Wofür waren die Tätowierungen nach einer Vermutung der Forscher vielleicht gedacht?",
           "Als frühe Behandlung gegen Schmerzen", ["Als Zeichen für seine Familie und sein Dorf", "Als Schmuck für große Feste im Sommer", "Als Schutz gegen die Kälte im Gebirge"], s,
           info="Die Striche und Kreuze sitzen an Akupunkturpunkten. Darum denken Forscher an eine frühe Schmerzbehandlung.",
           tipp="Wo auf dem Körper sitzen die Striche? Es sind Punkte, die man bei einer Behandlung reizt."),
        zuordnen("Ordne dem Körperteil den Befund zu.",
                 [("Blutgefäße", "verkalkt"), ("Gelenke", "abgenutzt"), ("Rippen", "verheilte Brüche"),
                  ("linker Fuß", "Erfrierungen"), ("Haut", "über 50 Tätowierungen"), ("Augen", "blau")], s,
                 extra=["tiefe Narbe im Gesicht"],
                 info="Alle diese Befunde nennt das Buch bei der Untersuchung der Mumie. Die Zähne waren stark abgenutzt, aber ohne Karies."),
    ]


def aufgaben_c():
    s = S_C
    von, bis = abs(OETZI_VON), jahr(OETZI_BIS)
    ereignisse = [("Lucy lebt (vor über 3 Millionen Jahren)", -3_000_000),
                  ("Die ersten Menschen werden sesshaft (um 9000 v. Chr.)", -9000),
                  (f"Ötzi lebt (um {jahr(OETZI_MITTE)})", OETZI_MITTE),
                  (f"Rom wird der Sage nach gegründet ({jahr(ROEMER)})", ROEMER),
                  (f"Ötzi wird gefunden ({FUND} n. Chr.)", FUND)]
    assert [y for _, y in ereignisse] == sorted(y for _, y in ereignisse)
    return [
        mc("Wann lebte Ötzi?", f"zwischen {von} und {bis}",
           [f"zwischen {von} und {abs(OETZI_BIS)} n. Chr.", f"zwischen {von - 3000} und {abs(OETZI_BIS) - 3000} v. Chr.",
            f"zwischen {abs(OETZI_BIS) - 2000} und {von - 2000} n. Chr."], s,
           info=f"Die richtige Zeitangabe lautet: zwischen {von} und {bis}, also vor Christi Geburt. „v. Chr.“ steht für „vor Christi Geburt“.",
           tipp="Achte auf v. Chr. und n. Chr."),
        kurz("In welcher Epoche (nach dem Heft) lebte Ötzi?",
             ["Ur- und Frühgeschichte", "die Ur- und Frühgeschichte", "Ur-und Frühgeschichte", "Ur und Frühgeschichte",
              "Ur- und Frühgeschichte (bis 3000 v. Chr.)", "Ur- und Frühgeschichte bis 3000 v. Chr."], s,
             info=f"Ötzi lebte vor 3000 v. Chr. Diese Zeit nennt das Heft Ur- und Frühgeschichte.",
             tipp="Die erste der fünf Epochen reicht bis 3000 v. Chr."),
        mc("Welche Epoche beginnt direkt nach der Zeit, in der Ötzi lebte?", "Altertum", ["Antike", "Mittelalter", "Neuzeit"], s,
           info="Die Ur- und Frühgeschichte reicht bis 3000 v. Chr. Danach folgt das Altertum (3000 bis 1000 v. Chr.).",
           tipp="Ötzis Epoche endet im Jahr 3000 v. Chr."),
        kurz(f"Ötzi lebte um {jahr(OETZI_MITTE)}. Wie viele Jahre sind es von da bis zum Jahr 2000 n. Chr.? Schreibe nur die Zahl.",
             _varianten(_zahlformen(ABSTAND_2000)), s,
             info=f"{abs(OETZI_MITTE)} + 2000 = {ABSTAND_2000}. Du rechnest zusammen, weil Christi Geburt dazwischen liegt.",
             tipp="Vor und nach Christi Geburt: Die Jahre werden zusammengerechnet."),
        mc("Etwa wie viele Jahre liegt Ötzis Leben bis heute zurück?", f"etwa {ABSTAND_RUND} Jahre",
           [f"etwa {abs(OETZI_MITTE)} Jahre", f"etwa {int(round(FALSCH_SUBTRAKTION, -2))} Jahre", "etwa 2000 Jahre"], s,
           info=f"{abs(OETZI_MITTE)} + {HEUTE} = {ABSTAND}, also etwa {ABSTAND_RUND} Jahre. Wer {abs(OETZI_MITTE)} − {HEUTE} rechnet, bekommt etwa {FALSCH_SUBTRAKTION} und liegt falsch.",
           tipp="Christi Geburt liegt zwischen Ötzi und heute.",
           bild=svg_oetzi_zeit(), bildAlt=ALT_ZEIT),
        tf(f"Ötzi lebte erst nach der Gründung der Stadt Rom (der Sage nach {jahr(ROEMER)}).", False, s,
           info=f"Ötzi lebte schon vor {abs(OETZI_BIS)} v. Chr., also mehr als {spanne(OETZI_BIS, ROEMER) // 1000 * 1000} Jahre vor der Gründung Roms, die der Sage nach {jahr(ROEMER)} war.",
           tipp="Bei v. Chr. gilt: Je größer die Zahl, desto früher."),
        luecke("Ergänze den Text über Ötzis Zeit.",
               "Ötzi lebte in der {{Kupfersteinzeit}}. Die Menschen lebten noch ähnlich wie in der {{Jungsteinzeit}}, "
               "aber sie begannen schon, mit {{Kupfer}} zu arbeiten. Nach den Epochen im Heft gehört Ötzi zur {{Ur- und Frühgeschichte|Ur und Frühgeschichte}}.",
               s, extra=["Altsteinzeit", "Eisen"],
               info="Kupfer war ein neues Metall. Es bereitete die Metallzeiten vor, die auf die Steinzeit folgten."),
        reihenfolge("Bringe diese Ereignisse in die richtige zeitliche Reihenfolge. Das früheste steht zuerst.",
                    [e for e, _ in ereignisse], s,
                    info="Je größer die Zahl bei v. Chr., desto früher. Lucy ist am ältesten, Ötzis Fund (1991) das jüngste Ereignis.",
                    tipp="Bei v. Chr. gilt: Je größer die Zahl, desto früher."),
    ]


def aufgaben_d():
    s = S_D
    return [
        mc("Welches Teil aus der Skizze ist NICHT steinzeitlich?",
           "Kupferbeil", ["Bogen", "Steindolch", "Fellmütze", "Gefäß für Glut"], s,
           info="Das Kupferbeil hat eine Klinge aus Metall und zeigt den Übergang zur Metallzeit. Bogen, Steindolch, Fellmütze und Gefäß für Glut sind steinzeitlich.",
           tipp="Welches Material gab es in der Steinzeit noch nicht?",
           bild=svg_ausruestung(True), bildAlt=ALT_AUSR),
        zuordnen("Aus welchem Material war das Teil?",
                 [("Dolch (Klinge)", "Feuerstein"), ("Dolch (Griff)", "Eschenholz"), ("Köcher", "Gamsleder"),
                  ("Mütze", "Bärenfell"), ("Bohrer", "Feuerstein"), ("Schnur", "Baumbast")], s,
                 extra=["Schafwolle"],
                 info="Feuerstein, Eschenholz, Gamsleder, Bärenfell und Baumbast stehen auf der Kopie. Zum Kupferbeil kommen gleich noch zwei Fragen."),
        kurz("Aus welchem Metall war die Klinge von Ötzis Beil?", ["Kupfer", "aus Kupfer"], s,
             info="Die Klinge war aus Kupfer gegossen. Deshalb heißt Ötzis Zeit Kupfersteinzeit."),
        kurz("Aus welchem Holz war der Schaft von Ötzis Beil?", ["Eibenholz", "Eibe", "aus Eibenholz"], s,
             info="Der Schaft des etwa 60 cm langen Beils war aus Eibenholz.",
             tipp="Es ist ein Nadelbaum, dessen Name mit E anfängt."),
        tf("Von allen Beilen aus der Vorgeschichte ist nur Ötzis Kupferbeil vollständig erhalten.", True, s,
           info="Es ist das einzige vollständig erhaltene vorgeschichtliche Beil der Welt. Darum ist es so wertvoll für die Forschung."),
        luecke("Ergänze den Text über Ötzis Ausrüstung.",
               "Zu Ötzis Ausrüstung gehörten wintertaugliche {{Fellkleidung|Kleidung}}, ein {{Bogen|Köcher|Steindolch}}, ein {{Köcher|Bogen|Steindolch}} "
               "für die Pfeile und ein {{Steindolch|Bogen|Köcher}}. Dazu kam ein Gefäß, in dem er {{Glut|Feuer}} mitnahm. "
               "Das {{Kupferbeil|Beil}} zeigt den Übergang zur Metallzeit.",
               s, extra=["Eisenschwert", "Schild"],
               info="Fast alles war steinzeitlich. Nur das Kupferbeil zeigt schon das neue Metall."),
        mc("Welche Aussage über Ötzis Leben lässt sich aus seiner Ausrüstung am besten begründen?",
           "Er stellte Waffen und Werkzeug selbst her.",
           ["Er besorgte alle Waffen bei einem Händler.", "Er kannte Metall noch gar nicht.", "Er trug nur leichte Kleidung für den Sommer."], s,
           info="Der halbfertige Bogen, die Rohlinge für Pfeilschäfte und der Bohrer sprechen dafür. Das ist ein Schluss aus den Funden.",
           tipp="Denke an den halbfertigen Bogen."),
    ]


def aufgaben_e():
    s = S_E
    return [
        mc("Warum nennt das Buch Ötzi einen „Wanderer zwischen den Zeiten“?",
           "Er lebte in der Übergangszeit von Stein zu Metall.",
           ["Er wanderte ständig zwischen Italien und Deutschland.", "Er war ein Nomade ohne festen Wohnort.",
            "Er lebte zugleich in Alt- und Jungsteinzeit."], s,
           info="Gemeint ist die Übergangszeit: Seine Ausrüstung ist fast ganz steinzeitlich, das Kupferbeil zeigt schon die Metallzeit.",
           tipp="Die Überschrift sagt etwas über seine Zeit, nicht über seine Wege."),
        mc("Woran starb Ötzi?", "Er verblutete, nachdem ihn ein Pfeil getroffen hatte.",
           ["Er erfror nachts bei einem Schneesturm in den Bergen.", "Er wurde unterwegs von einer Lawine verschüttet.",
            "Er starb an einer Krankheit durch Parasiten im Darm."], s,
           info="In seiner linken Schulter steckte eine Pfeilspitze. Er verblutete innerhalb weniger Minuten."),
        kurz("In welcher Schulter steckte die Pfeilspitze?",
             ["linke", "linken", "links", "linke Schulter", "die linke", "die linke Schulter", "der linken Schulter", "in der linken Schulter"], s,
             info="Die Pfeilspitze steckte in der linken Schulter. Die Schnittwunde war dagegen an der rechten Hand."),
        mc("Worauf deutet die tiefe Schnittwunde an Ötzis rechter Hand hin?", "auf einen Nahkampf kurz vor seinem Tod",
           ["auf eine Verletzung, die schon Jahre alt war", "auf Erfrierungen durch die Kälte im Gletscher", "auf einen Sturz in eine Gletscherspalte"], s,
           info="Unter dem Mikroskop war die Wunde ein bis drei Tage alt. Der Arzt hält sie für eine Kampf- oder Verteidigungsverletzung.",
           tipp="Wie alt war die Wunde nach dem Mikroskop?"),
        tf("Ötzis Körper wurde schon wenige Wochen nach seinem Tod entdeckt.", False, s,
           info="Der Körper blieb Jahrtausende im Gletschereis verborgen. Erst 1991 wurde er gefunden."),
        reihenfolge("Ordne Ötzis letzte Tage sinnvoll in die richtige Reihenfolge.",
                    ["Ötzi wird an der Hand verletzt (ein bis drei Tage vor seinem Tod).",
                     "Er steigt müde über die Baumgrenze und trinkt Wasser aus Bächen.",
                     "Er sucht zwischen Felsen einen Platz zum Ausruhen und lehnt die Ausrüstung an den Fels.",
                     "Er setzt sich und isst eine Mahlzeit.",
                     "Ein Pfeil trifft ihn in die linke Schulter.",
                     "Er verliert das Gleichgewicht und fällt nieder."], s,
                    info="Die Handwunde war schon ein bis drei Tage alt, sie liegt also am weitesten zurück. Die letzte Mahlzeit lag höchstens eine Stunde vor dem Tod: Erst kommen Rast und Essen, dann trifft ihn der Pfeil.",
                    tipp="Die Verletzung an der Hand lag ein bis drei Tage zurück. Der Pfeil kam erst nach der Mahlzeit."),
        zuordnen("Woher weiß man das? Ordne die Untersuchung der Erkenntnis zu.",
                 [("Pollen in Lunge und Darm", "Ötzi war im Frühling oder Frühsommer unterwegs"),
                  ("Wundränder unter dem Mikroskop", "Die Handwunde war ein bis drei Tage alt"),
                  ("Computertomografie des Magens", "Die letzte Mahlzeit lag höchstens eine Stunde zurück"),
                  ("halbfertiger Bogen und Rohlinge für Pfeilschäfte", "Ötzi musste seine Waffen erneuern"),
                  ("Pfeilspitze in der linken Schulter", "Er wurde von einem Pfeil getroffen und verblutete")], s,
                 extra=["Er war schon als Kind verletzt worden"],
                 info="Jede Erkenntnis stützt sich auf einen Fund oder eine Untersuchung. So kann man den „Kriminalfall“ Schritt für Schritt aufklären.",
                 tipp="Pollen blühen nur zu einer bestimmten Jahreszeit."),
        kurz("Wie heißt das Verfahren, mit dem man Ötzis Magen und dessen Inhalt untersucht hat? (Abkürzung CT)",
             ["Computertomografie", "Computertomographie", "CT", "Computertomograf", "Computertomograph"], s,
             info="Die Computertomografie zeigte einen gut gefüllten Magen mit kaum verdauten Speisen.",
             tipp="Das Wort beginnt mit „Computer“."),
        luecke("Ergänze den Text über Ötzis Tod.",
               "Ötzi starb durch einen {{Pfeil}}, dessen Spitze in der {{linken}} Schulter steckte. Er {{verblutete}} innerhalb weniger {{Minuten}}. "
               "Die tiefe Schnittwunde an der rechten {{Hand}} deutet auf einen {{Nahkampf}}.",
               s, extra=["rechten", "erfror", "Beil"],
               info="Pfeilspitze links in der Schulter, Wunde rechts an der Hand: Merke dir die beiden Körperseiten."),
    ]


def aufgaben_f():
    s = S_F
    return [
        zuordnen("Ist es eine Quelle oder eine Darstellung?",
                 [("Ötzis Mumie", "Quelle"), ("Das Kupferbeil", "Quelle"), ("Die Pfeilspitze in Ötzis Schulter", "Quelle"),
                  ("Text des Arztes über Ötzis letzte Minuten", "Darstellung"), ("Rekonstruktionszeichnung von 2011", "Darstellung"),
                  ("Schulbuchtext über Ötzi", "Darstellung")], s,
                 info="Quellen stammen aus Ötzis Zeit. Darstellungen machen Menschen später mithilfe der Quellen.",
                 tipp="Wer hat es gemacht, und wann? Gehörte es schon zu Ötzis Zeit?"),
        kurz("Zu welcher Art von Quellen gehören Ötzis Mumie, seine Kleidung und seine Waffen?",
             ["Sachquellen", "Sachquelle", "gegenständliche Quellen", "gegenständliche Quelle"], s,
             info="Man kann sie anfassen und untersuchen. Das Heft nennt sie Sachquellen, das Buch gegenständliche Quellen.",
             tipp="Man kann sie anfassen."),
        mc("Warum ist der Text des Arztes Egarter-Vigl eine Darstellung und keine Quelle?",
           "Er schreibt später über etwas, das er nicht selbst erlebt hat.",
           ["Er enthält Wörter der Unsicherheit wie „wohl“ und „vielleicht“.", "Er wurde in einem Buch gedruckt und nicht im Museum gezeigt.",
            "Er enthält keine Zeichnungen oder Fotos als Beleg."], s,
           info="Der Arzt hat Ötzis Tod nicht erlebt. Er erzählt ihn Jahrtausende später und stützt sich dabei auf Funde.",
           tipp="Denke an den Zeitabstand zwischen Ötzis Tod und dem Text."),
        tf("Eine Rekonstruktionszeichnung von Ötzi ist eine Quelle.", False, s,
           info="Sie ist eine Darstellung, denn sie entstand erst später. Quellen sind die Funde, auf denen sie beruht (Mumie, Kleidung, Ausrüstung)."),
        luecke("Ergänze den Text über Wörter der Unsicherheit.",
               "Wenn ein Forscher etwas nicht sicher weiß, benutzt er Wörter der {{Unsicherheit}}, zum Beispiel „{{vermutlich|wahrscheinlich|vielleicht|wohl}}“, "
               "„{{wahrscheinlich|vermutlich|vielleicht|wohl}}“ oder „{{vielleicht|vermutlich|wahrscheinlich|wohl}}“. "
               "Das zeigt: Man {{vermutet}} etwas, aber man hat es nicht {{bewiesen}}.",
               s, extra=["sicher", "bestimmt"],
               info="Solche Wörter stehen oft bei Aussagen, die nur vermutet sind, zum Beispiel bei Ötzis Tätowierungen."),
        zuordnen("Ist die Aussage belegt oder nur vermutet?",
                 [("Eine Pfeilspitze steckte in Ötzis linker Schulter", "belegt"), ("Ötzis Blutgefäße waren verkalkt", "belegt"),
                  ("Kurz vor seinem Tod hatte Ötzi gegessen", "belegt"), ("Die Tätowierungen sollten Schmerzen lindern", "nur vermutet"),
                  ("Der Schütze schlich sich heimlich an", "nur vermutet"), ("Ein Feind aus einem anderen Dorf hat Ötzi getötet", "nur vermutet")], s,
                 info="Belegt sind Dinge, die man an der Mumie und den Funden sieht. Wer Ötzi tötete und warum, bleibt ein Rätsel.",
                 tipp="Gibt es einen Fund oder eine Untersuchung dazu?"),
        tf("Die Belege reichen aus, um genau zu sagen, wer Ötzi getötet hat.", False, s,
           info="Man weiß, dass ein Pfeil ihn traf. Wer geschossen hat und warum, bleibt ein Rätsel."),
        mc("Worauf stützt sich die Aussage „Ötzi ist in Italien gestorben“?", "Auf den Fundort der Mumie in den Ötztaler Alpen",
           ["Auf einen Brief, den Ötzi selbst geschrieben hat", "Auf Zeugen, die seinen Tod beobachtet haben", "Auf eine Urkunde aus Bozen aus Ötzis Zeit"], s,
           info="Die Mumie lag in den Ötztaler Alpen an der Grenze zu Italien und liegt heute in Bozen. Briefe, Urkunden oder Augenzeugen aus Ötzis Zeit gibt es dazu nicht.",
           tipp="Was hat man wirklich gefunden?"),
    ]


def aufgaben_g():
    s = S_G
    muster_aussagen = (
        "Mögliche Lösung (eine Einschätzung, bitte mit deinem Heft abgleichen): "
        "„Ötzi ist weit gelaufen, wurde von einem Pfeil getroffen und hat sehr viel Blut verloren“: Der Pfeil ist belegt (Pfeilspitze in der linken Schulter), "
        "der Blutverlust auch (er verblutete). Bei „weit gelaufen“ ist es eine Einschätzung: Die Funde zeigen nur, dass er müde vom Aufstieg und über die Alpen unterwegs war. "
        "„Ötzi ist in Italien gestorben“: Dafür spricht der Fundort in den Ötztaler Alpen an der Grenze zu Italien. Die Mumie liegt heute in Bozen in Italien. "
        "Das Land Italien gab es damals aber noch nicht.")
    A = [
        mc("Wo wird Ötzis Mumie heute aufbewahrt?", "Im Südtiroler Archäologiemuseum in Bozen",
           ["Im Deutschen Museum in München", "Im Landesmuseum in Innsbruck", "Im Römisch-Germanischen Museum in Köln"], s,
           info="Laut Kopie kam die Mumie nach dem Fund zuerst nach Innsbruck. Heute liegt sie im Museum in Bozen in Italien."),
        tf("Die Mumie wird in einem eigens gebauten Kühlraum aufbewahrt.", True, s,
           info="Der Kühlraum wurde extra für Ötzi gebaut, damit die Mumie erhalten bleibt."),
        luecke("Ergänze den Text über das Museum.",
               "Ötzis Mumie liegt im Südtiroler {{Archäologiemuseum}} in der Stadt {{Bozen}}. Die Stadt liegt in {{Italien}}. "
               "Die Mumie wird dort in einem {{Kühlraum}} aufbewahrt.",
               s, extra=["Innsbruck", "Österreich"],
               info="Die Mumie ist heute in Bozen. Nach dem Fund kam sie laut Kopie zuerst nach Innsbruck."),
        zuordnen("Ist die Ausstellung würdelos? Ordne jedes Argument zu.",
                 [("Ein Mensch wird wie ein Ausstellungsstück angeschaut", "spricht dafür (würdelos)"),
                  ("Man hat Ötzi nicht um Erlaubnis gefragt", "spricht dafür (würdelos)"),
                  ("Ötzi ist schon lange tot und spürt nichts mehr", "spricht dagegen (nicht würdelos)"),
                  ("Die Forschung lernt durch Ötzi viel über die Steinzeit", "spricht dagegen (nicht würdelos)"),
                  ("Die Mumie wird sorgfältig im Kühlraum aufbewahrt", "spricht dagegen (nicht würdelos)")], s,
                 info="Das sind Argumente, keine Fakten. Du kannst sie für deine eigene Meinung nutzen.",
                 tipp="Würdelos heißt: ohne Achtung vor dem Menschen."),
        frei("Ötzi liegt in Bozen in einem Kühlraum und wird ausgestellt. Manche finden das würdelos. Nenne ein Argument dafür, ein Argument dagegen und schreibe deine eigene Meinung mit Begründung.",
             "Dafür (würdelos): Ötzi war ein Mensch. Es ist nicht schön, wenn ein Toter wie ein Ausstellungsstück angeschaut wird. "
             "Dagegen: Ötzi ist schon lange tot und spürt nichts mehr. Außerdem lernen die Forscher und Besucher durch ihn viel über die Steinzeit. "
             "Meine Meinung: Ich finde es nicht würdelos, solange die Mumie sorgfältig und mit Respekt aufbewahrt wird, weil man durch sie viel über das Leben vor über 5000 Jahren erfährt.",
             ["Ein Argument, das dafür spricht, dass es würdelos ist", "Ein Argument, das dagegen spricht", "Eine eigene Meinung", "Die Meinung ist begründet"], 4, s,
             tipp="Es gibt keine einzig richtige Meinung. Wichtig ist, dass du sie begründest."),
        frei("Erkläre die Überschrift „Wanderer zwischen den Zeiten“. Nenne dazu zwei Teile von Ötzis Ausrüstung.",
             "Ötzi lebte in der Kupfersteinzeit, in einer Übergangszeit zwischen Steinzeit und Metallzeit. "
             "Viele Teile seiner Ausrüstung sind steinzeitlich, zum Beispiel der Steindolch und die Fellkleidung. "
             "Das Kupferbeil mit der Metallklinge zeigt schon die neue Zeit.",
             ["Übergangszeit zwischen Steinzeit und Metallzeit genannt", "Ein steinzeitliches Teil genannt (zum Beispiel Steindolch, Fellkleidung, Bogen)",
              "Das Kupferbeil als neues Teil genannt"], 3, s,
             tipp="Welches Teil der Ausrüstung passt nicht zur reinen Steinzeit?"),
        frei("Prüfe die beiden Aussagen aus dem Heft. Was ist durch Quellen belegt, was nicht? „Ötzi ist weit gelaufen, wurde von einem Pfeil getroffen und hat sehr viel Blut verloren.“ "
             "und „Ötzi ist in Italien gestorben.“",
             muster_aussagen,
             ["Pfeil und Blutverlust als belegt genannt (Pfeilspitze, verblutet)", "Zu „weit gelaufen“ begründet Stellung genommen (zum Beispiel: Die Funde zeigen nur, dass er über die Alpen unterwegs war)",
              "Die Aussage zu Italien mit dem Fundort begründet", "Die Aussagen Teil für Teil geprüft"], 4, s,
             info="Das Muster ist eine Einschätzung aus den Funden. Vergleiche deine Antwort mit der Lösung in deinem Heft.",
             tipp="Prüfe jede Aussage Teil für Teil: Gibt es einen Fund oder eine Untersuchung dazu?"),
        frei("Wer war Ötzi und was weiß man über ihn? Schreibe fünf bis sechs Sätze.",
             "Ötzi ist eine Mumie, die 1991 von einem Ehepaar in den Ötztaler Alpen im Gletscher gefunden wurde. "
             "Er lebte zwischen 3359 und 3105 v. Chr. in der Kupfersteinzeit, also vor über 5000 Jahren. "
             "Er war etwa 46 Jahre alt, etwa 1,60 m groß und hatte blaue Augen und über 50 Tätowierungen. "
             "Zu seiner Ausrüstung gehörten Fellkleidung, Bogen, Steindolch und ein Kupferbeil. "
             "Er wurde von einem Pfeil in die linke Schulter getroffen und verblutete. Heute liegt die Mumie im Museum in Bozen.",
             ["Gefunden 1991 von einem Ehepaar in den Ötztaler Alpen (im Gletscher)", "Lebte um 3300 v. Chr., Kupfersteinzeit, über 5000 Jahre her",
              "Aussehen oder Alter (etwa 46 Jahre, etwa 1,60 m, blaue Augen, Tätowierungen)", "Ausrüstung (zum Beispiel Bogen, Steindolch, Kupferbeil)",
              "Tod durch einen Pfeil, verblutet", "Mumie im Museum in Bozen"], 6, s,
             tipp="Gehe der Reihe nach vor: Fund, Zeit, Aussehen, Ausrüstung, Tod, Museum."),
    ]
    # Verweise auf Lernblatt-Abschnitte für einzelne Aufgaben
    A[4]["lesen"] = T_MUSEUM
    A[5]["lesen"] = [T_AUSR, T_WANDERER]
    A[6]["lesen"] = T_BELEGT
    A[7]["lesen"] = [T_FUND, T_WER, T_WANN, T_TOT]
    return A


# ------------------------------------------------------------------ Paket

def build():
    a, e, f = aufgaben_a(), aufgaben_e(), aufgaben_f()
    a[7]["lesen"] = [T_FUND, T_TOT, T_MUSEUM]        # T8: Tod bis Museum
    e[0]["lesen"] = T_WANDERER                        # T31: „Wanderer zwischen den Zeiten“
    f[1]["lesen"] = [T_AUSR, T_BELEGT]                # T41: Sachquellen stehen in „Kleidung und Ausrüstung“
    aufgaben = (a + aufgaben_b() + aufgaben_c() + aufgaben_d() + e + f + aufgaben_g())
    p = pack("geschichte-6-oetzi", "Geschichte Teil 6: Ötzi, der Mann aus dem Eis",
             "Fund, Person, Zeit, Ausrüstung, Tod und „Kriminalfall Ötzi“: Woher weiß man das? Quelle oder Darstellung, belegt oder vermutet, Ötzi im Museum. "
             "Mit Lernblatt und vielen Übungsaufgaben.",
             lernblatt(), aufgaben, min_aufgaben=45,
             hinweis="Buch (S. 32 bis 33) und Kopie nennen bei Ötzi leicht verschiedene Zahlen (Alter, Höhe, Gewicht). "
                     "Hier gilt das Buch, bei Abweichungen sind beide Werte richtig oder die Zahlen sind gerundet.")
    nachlesen(p, {
        S_A: T_FUND,
        S_B: T_WER,
        S_C: T_WANN,
        S_D: [T_AUSR, T_WANDERER],
        S_E: [T_TOT, T_KRIMI],
        S_F: T_BELEGT,
        S_G: T_MUSEUM,
    })
    p["probe"] = False
    return [p]
