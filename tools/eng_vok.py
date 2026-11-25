"""Vokabeln Englisch Klasse 6, Unit 2 „A school day“ (Vokabelliste S. 184–187 im Buch, Schulalltag in Großbritannien aus dem Lernzettel).

Nur Wort und deutsche Bedeutung sind aus der Liste übernommen (Fakten). Alle Beispielsätze sind selbst geschrieben.
Aus dieser Tabelle werden die Wortschatzaufgaben der Pakete 2b und 2c erzeugt (mit Prüfungen).
"""
from eng_lib import *

# key: (englisch, deutsche Kurzbedeutung, akzeptierte englische Schreibweisen, eigener Beispielsatz, Gruppe)
VOK = {
    # Schule und Schultag
    "uniform": ("uniform", "Schuluniform", ["uniform", "school uniform"], "At my cousin's school all students wear a blue uniform.", "schule"),
    "break": ("break", "Pause", ["break"], "In the break we eat our sandwiches in the yard.", "schule"),
    "canteen": ("canteen", "Kantine", ["canteen"], "The canteen is open from twelve to one.", "schule"),
    "lessons": ("lessons", "Unterrichtsstunden", ["lessons", "lesson"], "We have five lessons on Monday.", "schule"),
    "clubs": ("clubs", "AGs, Clubs", ["clubs", "club"], "My sister is in two clubs after school.", "schule"),
    "registration": ("registration", "Anwesenheitskontrolle am Morgen", ["registration"], "At registration the teacher checks who is at school.", "schule"),
    "queue": ("(to) queue", "Schlange stehen, sich anstellen", ["queue", "to queue"], "We queue at the bus stop every morning.", "schule"),
    "ring": ("(to) ring", "klingeln, läuten", ["ring", "to ring"], "The school bell rings at nine o'clock.", "schule"),
    "call out the names": ("(to) call out the names", "die Namen aufrufen", ["call out the names", "to call out the names"], "At the start of the lesson the teacher calls out the names.", "schule"),
    "article": ("article", "Artikel (in einer Zeitung)", ["article"], "My dad reads an article about trains in the paper.", "schule"),
    "worksheet": ("worksheet", "Arbeitsblatt", ["worksheet"], "Our teacher gives us a worksheet about verbs.", "schule"),
    "label": ("(to) label", "beschriften, etikettieren", ["label", "to label"], "Please label the picture with the words in the box.", "schule"),
    "mistake": ("mistake", "Fehler", ["mistake"], "I found a mistake in my homework.", "schule"),
    "correct": ("correct", "richtig, korrekt", ["correct"], "Is this the correct answer?", "schule"),
    "read aloud": ("(to) read aloud", "laut (vor)lesen", ["read aloud", "to read aloud"], "Can you read the text aloud, please?", "schule"),
    "make sure": ("(to) make sure that …", "sich vergewissern, dass …; darauf achten, dass …", ["make sure that", "to make sure that", "make sure", "to make sure"], "Make sure that you have your pencil case with you.", "schule"),
    "get ready": ("(to) get ready (for)", "sich fertig machen (für), sich vorbereiten (auf)", ["get ready", "to get ready", "get ready for", "to get ready for"], "We get ready for the lesson and open our books.", "schule"),
    "dialogue": ("dialogue", "Dialog", ["dialogue"], "In class we act out a dialogue about shopping.", "schule"),
    "syllable": ("syllable", "Silbe", ["syllable"], "The word „banana“ has three syllables.", "schule"),
    "size": ("size", "Größe", ["size"], "These shoes are the wrong size for me.", "schule"),
    "clear": ("clear", "klar, deutlich", ["clear"], "The teacher has a clear voice.", "schule"),
    "like this": ("like this", "so", ["like this"], "Hold the pencil like this.", "schule"),
    # Musical und Bühne
    "audition": ("audition", "Vorsprechen, Vorsingen, Vorspielen", ["audition"], "Nora has an audition for the school show on Thursday.", "buehne"),
    "musical": ("this year's musical", "das diesjährige Musical", ["this year's musical", "this years musical"], "This year's musical is about a pirate ship.", "buehne"),
    "stage": ("stage", "Bühne", ["stage"], "The singers walk onto the stage.", "buehne"),
    "concert": ("concert", "Konzert", ["concert"], "We are going to a concert in the town hall.", "buehne"),
    "theatre": ("theatre", "Theater", ["theatre"], "The theatre is next to the library.", "buehne"),
    "recorder": ("recorder", "Blockflöte", ["recorder"], "In music we learn to play the recorder.", "buehne"),
    "talented": ("talented", "begabt, talentiert", ["talented"], "She is a talented dancer.", "buehne"),
    "cheer": ("(to) cheer", "jubeln", ["cheer", "to cheer"], "The fans cheer when the team scores a goal.", "buehne"),
    "clap": ("(to) clap", "(Beifall) klatschen", ["clap", "to clap"], "At the end of the song everybody claps.", "buehne"),
    "nervous": ("nervous", "nervös, aufgeregt", ["nervous"], "Before the test I felt a bit nervous.", "buehne"),
    "earphones": ("earphones", "Ohrhörer, Kopfhörer", ["earphones"], "I listen to music with my earphones on the bus.", "buehne"),
    "fashion": ("fashion", "Mode", ["fashion"], "My aunt works in a fashion shop.", "buehne"),
    "shy": ("shy", "schüchtern, scheu", ["shy"], "Mia is shy and does not like talking to new people.", "buehne"),
    "brilliant": ("brilliant", "großartig, genial", ["brilliant"], "That was a brilliant idea!", "buehne"),
    # Pläne, Ratschläge, kleine Wörter
    "a bit": ("a bit", "ein bisschen, etwas", ["a bit"], "The soup is a bit too hot.", "klein"),
    "a few": ("a few", "ein paar, einige", ["a few"], "I have a few books about horses.", "klein"),
    "side": ("side", "Seite", ["side"], "The bus stop is on the other side of the road.", "klein"),
    "present": ("present", "Gegenwart", ["present"], "The present is the time right now.", "klein"),
    "by": ("by …", "von … (Urheber)", ["by"], "This picture is by a famous painter.", "klein"),
    "should": ("You should …", "Du solltest … / Ihr solltet …", ["you should", "should"], "You should drink more water.", "klein"),
    "about": ("about", "ungefähr", ["about"], "There were about twenty children in the hall.", "klein"),
    "even": ("even", "sogar", ["even"], "Everybody laughed, even the teacher.", "klein"),
    "so far": ("so far", "bis jetzt, bis hierher", ["so far"], "So far the weather has been great.", "klein"),
    "everything": ("everything", "alles", ["everything"], "Thank you for everything!", "klein"),
    "on my own": ("on my / your / … own", "allein", ["on my own", "on your own", "on his own", "on her own", "on our own", "on their own"], "I did my homework on my own.", "klein"),
    # get, Verben
    "get on": ("(to) get on", "vorankommen, zurechtkommen", ["get on", "to get on"], "How are you getting on with your new class?", "verben"),
    "mean": ("(to) mean", "bedeuten; meinen, sagen wollen", ["mean", "to mean"], "What does this word mean?", "verben"),
    "pause": ("(to) pause", "innehalten, pausieren", ["pause", "to pause"], "The singer paused for a second.", "verben"),
    "change": ("(to) change", "(ver)ändern, sich (ver)ändern", ["change", "to change"], "The leaves change their colour in autumn.", "verben"),
    "lie": ("(to) lie", "liegen", ["lie", "to lie"], "The cat likes to lie in the sun.", "verben"),
    "wake up": ("(to) wake sb. up", "jemanden (auf)wecken", ["wake up", "to wake up", "wake sb. up", "to wake sb. up"], "My alarm clock wakes me up at six.", "verben"),
    "stick": ("(to) stick sth. into sth.", "etwas in etwas stecken", ["stick", "to stick", "stick into", "to stick into"], "He sticks his hand into the bag.", "verben"),
    "could": ("could", "konnte(n), könnte(n)", ["could"], "We could play cards if it rains.", "verben"),
    # Dinge, Orte
    "earth": ("(the) earth", "(die) Erde", ["earth", "the earth"], "The earth goes around the sun.", "dinge"),
    "plane": ("plane", "Flugzeug", ["plane"], "The plane lands at four o'clock.", "dinge"),
    "town hall": ("town hall", "Rathaus", ["town hall"], "The market is in front of the town hall.", "dinge"),
    "snow": ("snow", "Schnee", ["snow"], "There was a lot of snow on the hill.", "dinge"),
    "paw": ("paw", "Pfote, Tatze", ["paw"], "The dog gives me his paw.", "dinge"),
    "stairs": ("stairs (pl)", "Treppe, Treppenstufen", ["stairs"], "Our classroom is up the stairs.", "dinge"),
    "square kilometre": ("square kilometre (sq km)", "Quadratkilometer", ["square kilometre", "sq km"], "The island is five square kilometres big.", "dinge"),
    "round the world": ("round the world", "um die Welt", ["round the world"], "She wants to travel round the world.", "dinge"),
    "fork": ("fork", "Gabel", ["fork"], "Please take a knife and a fork.", "dinge"),
    "knife": ("knife", "Messer", ["knife"], "Be careful with the knife.", "dinge"),
    "spoon": ("spoon", "Löffel", ["spoon"], "I eat my soup with a spoon.", "dinge"),
    # Adjektive
    "large": ("large", "groß", ["large"], "They live in a large house.", "adj"),
    "tall": ("tall", "groß (Person); hoch (Gebäude, Baum)", ["tall"], "The tree in our garden is very tall.", "adj"),
    "awful": ("awful", "schrecklich, fürchterlich", ["awful"], "The weather was awful yesterday.", "adj"),
    "scared": ("scared", "verängstigt", ["scared"], "The little boy was scared of the dark.", "adj"),
    "lovely": ("lovely", "schön, hübsch, herrlich", ["lovely"], "What a lovely day!", "adj"),
}

# Anzeige-Reihenfolge der Gruppen und kurze Überschriften
GRUPPEN = {"schule": "Schule und Schultag", "buehne": "Bühne, Musical und Gefühle", "klein": "Kleine Wörter und Wendungen",
           "verben": "Verben", "dinge": "Dinge und Orte", "adj": "Beschreiben"}

# Wortfamilien auf -er (Verb – Person)
FAMILIEN = [("call", "caller", "Anrufer/in"), ("dance", "dancer", "Tänzer/in"), ("fight", "fighter", "Kämpfer/in"), ("help", "helper", "Helfer/in"),
            ("listen", "listener", "Zuhörer/in"), ("read", "reader", "Leser/in"), ("run", "runner", "Läufer/in"), ("shop", "shopper", "(Ein-)Käufer/in"),
            ("sing", "singer", "Sänger/in"), ("speak", "speaker", "Sprecher/in, Redner/in"), ("work", "worker", "Arbeiter/in")]
VERB_DE = {"call": "anrufen", "dance": "tanzen", "fight": "kämpfen", "help": "helfen", "listen": "zuhören", "read": "lesen", "run": "laufen", "shop": "einkaufen",
           "sing": "singen", "speak": "sprechen, reden", "work": "arbeiten"}

# unregelmäßige Verben (Grundform – Simple Past), wie in der Vokabelliste angegeben
PAST = [("ring", "rang"), ("mean", "meant"), ("get", "got"), ("lie", "lay"), ("wake up", "woke up"), ("stick", "stuck")]


def _kurzgloss(de):
    return de


def zeige(key):
    return VOK[key][0]


def de_von(key):
    return VOK[key][1]


def info_eintrag(key):
    en, de, _, bsp, _g = VOK[key]
    s = f"„{en}“ bedeutet „{de}“."
    if bsp:
        s += f" Beispiel: {bsp}"
    return s


def en_kurz(key, abschnitt, extra_tipp=None):
    """Deutsch → Englisch als Texteingabe."""
    en, de, alts, bsp, _ = VOK[key]
    assert alts, key
    return kurz(f"Wie heißt das auf Englisch? „{de}“", alts, abschnitt, info=info_eintrag(key), tipp=extra_tipp)


def de_mc(key, abschnitt, gruppe=None):
    """Englisch → Deutsch als Auswahl (Fehlantworten aus derselben Gruppe)."""
    en, de, _, bsp, g = VOK[key]
    pool = [k for k, v in VOK.items() if v[4] == (gruppe or g) and k != key and v[1] != de and v[1] not in de and de not in v[1]]
    assert len(pool) >= 3, (key, pool)
    i = sorted(VOK).index(key)
    wahl = []
    for j in range(len(pool)):
        k = pool[(i + j) % len(pool)]
        if VOK[k][1] not in wahl:
            wahl.append(VOK[k][1])
        if len(wahl) == 3:
            break
    return mc(f"Was bedeutet „{en}“?", de, wahl, abschnitt, info=info_eintrag(key))


def en_mc(key, abschnitt, gruppe=None):
    """Deutsch → Englisch als Auswahl (Fehlantworten sind englische Wörter derselben Gruppe)."""
    en, de, alts, bsp, g = VOK[key]
    pool = [k for k, v in VOK.items() if v[4] == (gruppe or g) and k != key and v[0] != en]
    i = sorted(VOK).index(key)
    wahl = []
    for j in range(len(pool)):
        k = pool[(i * 2 + j) % len(pool)]
        if VOK[k][0] not in wahl and VOK[k][0] != en:
            wahl.append(VOK[k][0])
        if len(wahl) == 3:
            break
    return mc(f"Welches englische Wort passt? „{de}“", en, wahl, abschnitt, info=info_eintrag(key))


def paare_zu(keys, abschnitt, frage="Ordne das englische Wort der deutschen Bedeutung zu."):
    """Zuordnen: englisch → deutsch, mit Kurzbedeutungen (rechte Seite eindeutig)."""
    paare = [(VOK[k][0], VOK[k][1]) for k in keys]
    assert len({d for _, d in paare}) == len(paare), keys
    info = " ".join(f"{VOK[k][0]} = {VOK[k][1]}." for k in keys[:5])
    return zuordnen(frage, paare, abschnitt, info=info)


def satz_luecke(frage, zeilen, abschnitt, extra=(), info=None, alle=True):
    """Lückentext aus (Satz mit {{Wort}}) Zeilen; info wird sonst aus den Wörtern gebaut."""
    text = "\n".join(zeilen)
    return luecke(frage, text, abschnitt, extra=list(extra), info=info or "Die Wörter passen nach ihrer Bedeutung in den Satz.")
