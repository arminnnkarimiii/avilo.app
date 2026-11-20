"""Memory Pond: 20 activities per band. Patterns marked hide=True are shown, then hidden."""
from common import *

N = 5
POOL = [i for i in ICONS if i not in ("circle", "square", "triangle", "rect", "diamond")]


def pairs_round(r, k, pool=POOL):
    return match([(tok(i), tok(i)) for i in r.sample(pool, k)])


def hidden_seq(r, length, pool, q="Remember the order! What came next?"):
    length = max(3, length)
    seq = [r.choice(pool) for _ in range(length + 1)] if len(pool) < length + 1 else r.sample(pool, length + 1)
    d = pattern(r, seq[:length], seq[length], r.sample([p for p in pool if p != seq[length]], 2), q)
    d["hide"] = True
    return d


def recall(r, pool, k, q):
    shown = r.sample(pool, k)
    right = r.choice(shown)
    d = pick(r, q, right, r.sample([p for p in pool if p not in shown], 2))
    d["show"] = shown
    d["hide"] = True
    return d


# ---------------- Little Cubs ----------------
def c01(r): return ("Animal pairs", "Remember where each animal hides.", [pairs_round(r, 3, ["cat", "dog", "duck", "fish", "bug", "dino"]) for _ in range(N)])
def c02(r): return ("What's missing?", "Look at all the toys, then check again.", [changed(r, POOL, 4) for _ in range(N)])
def c03(r):
    cols = ["red", "blue", "green", "yellow", "purple"]
    return ("Remember the colors", "Say the colors out loud to remember.", [hidden_seq(r, 2 + i % 2, [tok("circle", c) for c in cols]) for i in range(N)])
def c04(r): return ("Hide-and-seek bear", "Watch closely before it changes.", [changed(r, POOL, 4, "Which spot changed?") for _ in range(N)])
def c05(r): return ("Sound copycat", "Listen, then copy the drums.", [rhythm(r, 2, 2 + i % 2) for i in range(N)])
def c06(r): return ("Which cup?", "Keep your eyes on the cups.", [changed(r, ["cup", "ball", "star", "heart", "apple", "bell"], 4, "Which cup changed?") for _ in range(N)])
def c07(r): return ("Picture flash", "Look fast, then remember!", [recall(r, POOL, 3, "Which one did you see?") for _ in range(N)])
def c08(r): return ("Fruit pairs", "Turn two cards. Same? Keep them!", [pairs_round(r, 3, ["apple", "cookie", "egg", "leaf", "flower", "drop"]) for _ in range(N)])
def c09(r): return ("Repeat the song", "Copy the beat Avi plays.", [rhythm(r, 3, 2 + i % 2) for i in range(N)])
def c10(r): return ("Where did it go?", "Remember each spot.", [changed(r, POOL, 6) for _ in range(N)])
def c11(r): return ("Toy box memory", "Remember what went into the box.", [recall(r, ["ball", "block", "drum", "bell", "book", "car", "balloon"], 3, "Which toy went in the box?") for _ in range(N)])
def c12(r): return ("Shape pairs", "Shapes can look alike. Look closely!", [pairs_round(r, 3, ["circle", "square", "triangle", "star", "heart", "diamond"]) for _ in range(N)])
def c13(r): return ("Copy Avi's dance", "Watch the moves, then repeat them.", [hidden_seq(r, 2 + i % 2, ["Clap", "Jump", "Spin", "Wave", "Stomp"], "Avi's dance! Which move comes next?") for i in range(N)])
def c14(r): return ("Spot the change", "One thing will be different.", [changed(r, POOL, 6) for _ in range(N)])
def c15(r): return ("Remember the order", "First, then, last.", [hidden_seq(r, 3, POOL) for _ in range(N)])
def c16(r): return ("Pop every dog!", "Only the dogs. Ignore the others.", [pop(r, "@dog", ["@cat", "@duck", "@fish", "@bug"], g, 9) for g in [3, 4, 3, 4, 5]])
def c17(r): return ("Letter pairs", "Find the two cards with the same letter.", [match([(l, l + " ") if False else (l, l.lower()) for l in r.sample("ABDEFGHMNRST", 3)]) for _ in range(N)])
def c18(r):
    rounds = []
    for _ in range(N):
        ic = r.choice(POOL); n = r.randint(2, 5)
        d = count(r, ic, n, f"How many did you see?"); d["hide"] = True
        rounds.append(d)
    return ("Count and remember", "Count quickly before they hide.", rounds)
def c19(r): return ("Peekaboo cards", "Peek, remember, match.", [pairs_round(r, 3) for _ in range(N)])
def c20(r): return ("Freeze when the music stops", "Tap when the bar hits the green.", [motion("Tap when the marker is in the green!", s, z) for s, z in [(0.8, 40), (1.0, 36), (1.1, 34), (1.2, 32), (1.3, 30)]])

# ---------------- Explorers ----------------
def e01(r): return ("Memory grid 4×4", "Make a picture in your head of where things are.", [pairs_round(r, 4) for _ in range(N)])
def e02(r): return ("Simon says", "Repeat the lights in order.", [rhythm(r, 4, 3 + i) for i in range(N)])
def e03(r):
    st = [("Pip the penguin went sledding, then had hot cocoa, then took a nap.", "What did Pip do second?", "Had hot cocoa", ["Went sledding", "Took a nap"]),
          ("Rosa bought eggs, milk and a red balloon.", "What colour was the balloon?", "Red", ["Blue", "Green"]),
          ("The fox hid three acorns under the oak tree.", "How many acorns?", "3", ["2", "5"]),
          ("Leo packed a torch, a map and a sandwich for his hike.", "What did Leo NOT pack?", "A tent", ["A map", "A torch"]),
          ("Zoe's cat is called Pepper and sleeps on the blue rug.", "Where does Pepper sleep?", "On the blue rug", ["In a box", "On the sofa"])]
    rounds = []
    for s, q, a, w in st:
        d = pick(r, q, a, w); d["read"] = s; d["hide"] = True; rounds.append(d)
    return ("Story recall", "Picture the story like a movie.", rounds)
def e04(r): return ("What changed? 8 things", "Scan row by row.", [changed(r, POOL, 8) for _ in range(N)])
def e05(r): return ("Number span", "Say the numbers in your head.", [hidden_seq(r, 3 + i % 2, [str(n) for n in range(1, 10)], "Remember the numbers! What came next?") for i in range(N)])
def e06(r): return ("Shopping list", "Make a silly picture of each item.", [recall(r, ["apple", "cookie", "egg", "fish", "cup", "leaf", "drop", "shell"], 4, "Which was on the list?") for _ in range(N)])
def e07(r):
    rounds = []
    for _ in range(N):
        s = r.sample(["Moo", "Woof", "Meow", "Quack", "Baa", "Oink"], 4)
        odd = r.choice(["Ding", "Beep", "Honk"])
        d = sound(r, ", ".join(s[:3] + [odd]), odd, s[:2], "Which sound is not an animal?"); rounds.append(d)
    return ("Spot the odd sound", "Listen for the sound that doesn't fit.", rounds)
def e08(r): return ("Find all the stars", "Only stars! Stay focused.", [pop(r, "@star", ["@heart", "@moon", "@sun", "@flower", "@diamond"], g, 10) for g in [3, 4, 4, 5, 5]])
def e09(r):
    names = [("Ava", "@cat:orange"), ("Ben", "@dog:brown"), ("Cleo", "@fish:blue"), ("Dan", "@duck:yellow"), ("Eva", "@bug:red"), ("Finn", "@dino:green")]
    return ("Faces and names", "Link each name to a picture.", [match(r.sample(names, 3)) for _ in range(N)])
def e10(r):
    rounds = []
    for _ in range(N):
        ns = [str(n) for n in r.sample(range(1, 10), 3)]
        d = build(r, f"Remember {' '.join(ns)}. Now tap them backwards!", ns[::-1]); d["hide"] = True; d["show"] = ns
        rounds.append(d)
    return ("Say it backwards", "Hold it in your head, then reverse.", rounds)
def e11(r): return ("Speedy card flip", "Fast and focused.", [pairs_round(r, 4) for _ in range(N)])
def e12(r):
    cw = [("red", "blue"), ("green", "yellow"), ("blue", "red"), ("yellow", "purple"), ("purple", "green")]
    rounds = []
    for word, ink in cw:
        d = pick(r, f"The word “{word.upper()}” is written in {ink} ink. Tap the INK colour.", ink.capitalize(), [word.capitalize(), r.choice([c for c in ["Red", "Blue", "Green", "Yellow", "Purple"] if c.lower() not in (word, ink)])])
        rounds.append(d)
    return ("Color word trick", "Ignore the word. Look at the colour.", rounds)
def e13(r): return ("Map memory", "Remember the landmarks.", [recall(r, ["house", "tree", "rocket", "planet", "bell", "key", "book", "cup"], 4, "Which landmark was on the map?") for _ in range(N)])
def e14(r): return ("Copy the rhythm", "Listen, then tap it back.", [rhythm(r, 3, 4 + i % 2) for i in range(N)])
def e15(r):
    qs = [("An arrow points up. You turn it right twice. It points…", "Down", ["Up", "Left"]), ("Remember: star top-left, moon bottom-right. Where was the moon?", "Bottom-right", ["Top-left", "Top-right"]),
          ("Flip a 'b' left to right. You get…", "d", ["p", "q"]), ("Flip a 'p' upside down. You get…", "b", ["q", "d"]), ("Turn an 'M' upside down. You get…", "W", ["N", "Z"])]
    return ("Turn it in your mind", "Picture it moving slowly.", [pick(r, q, a, w) for q, a, w in qs])
def e16(r): return ("Word list recall", "Link the words into a silly story.", [recall(r, ["Dragon", "Pancake", "Rocket", "Banana", "Castle", "Robot", "Ocean", "Guitar"], 4, "Which word was on the list?") for _ in range(N)])
def e17(r): return ("Focus timer", "Wait for the zone, then tap.", [motion("Tap when the marker is in the green zone.", s, z) for s, z in [(1.2, 28), (1.4, 26), (1.6, 24), (1.8, 22), (2.0, 20)]])
def e18(r): return ("Pattern flash", "Remember the pattern before it hides.", [hidden_seq(r, 4, [tok(s, c) for s in ["circle", "square", "star"] for c in ["red", "blue"]]) for _ in range(N)])
def e19(r): return ("Hidden objects", "Search the whole picture.", [changed(r, POOL, 8, "Find the one that changed!") for _ in range(N)])
def e20(r):
    rounds = []
    for _ in range(N):
        moves = r.choices(["Left", "Right", "Up", "Down"], k=4)
        d = build(r, "Remember the route, then tap it: " + " → ".join(moves), moves); d["hide"] = True; d["show"] = moves
        rounds.append(d)
    return ("Remember the route", "Say each turn as you go.", rounds)

# ---------------- Trailblazers ----------------
def t01(r):
    rooms = [("Front door", "Rocket"), ("Hallway", "Banana"), ("Kitchen", "Volcano"), ("Bedroom", "Piano"), ("Bathroom", "Dragon"), ("Garden", "Snowman")]
    return ("Memory palace", "Place each item in a room you know.", [match(r.sample(rooms, 3)) for _ in range(N)])
def t02(r):
    rounds = []
    for _ in range(N):
        seq = r.choices(["A", "B", "C", "D"], k=5)
        same = seq[-1] == seq[-3]
        rounds.append(pick(r, f"2-back: letters {' '.join(seq)}. Is the last letter the same as 2 before it?", "Yes" if same else "No", ["No" if same else "Yes"]))
    return ("N-back challenge", "Keep the last two in mind.", rounds)
def t03(r): return ("Speed card match", "Speed and accuracy both count.", [pairs_round(r, 5) for _ in range(N)])
def t04(r):
    rounds = []
    for k in range(N):
        ns = [str(n) for n in r.sample(range(1, 10), 4 + k % 2)]
        d = build(r, f"Memorise {' '.join(ns)}, then tap backwards.", ns[::-1]); d["hide"] = True; d["show"] = ns
        rounds.append(d)
    return ("Digits backwards", "Chunk them in pairs.", rounds)
def t05(r): return ("Focus marathon", "Steady focus, steady tap.", [motion("Tap in the green zone.", s, z) for s, z in [(1.8, 20), (2.1, 18), (2.4, 16), (2.7, 14), (3.0, 12)]])
def t06(r):
    cw = [("blue", "green"), ("red", "yellow"), ("green", "purple"), ("purple", "red"), ("yellow", "blue")]
    return ("Color word trick: extreme", "Read the ink, not the word.", [pick(r, f"“{w.upper()}” in {i} ink. Ink colour?", i.capitalize(), [w.capitalize(), "Orange"]) for w, i in cw])
def t07(r):
    rounds = []
    for _ in range(N):
        moves = r.choices(["North", "East", "South", "West"], k=5)
        d = build(r, "Recall the route: " + " → ".join(moves), moves); d["hide"] = True; d["show"] = moves
        rounds.append(d)
    return ("Map route recall", "Visualise walking it.", rounds)
def t08(r):
    v = [("Ancient", "Very old"), ("Brave", "Not afraid"), ("Curious", "Wants to know"), ("Enormous", "Huge"), ("Fragile", "Breaks easily"), ("Generous", "Likes to give"), ("Humble", "Not boastful")]
    return ("Vocabulary flashcards", "Say the word, then the meaning.", [match(r.sample(v, 4)) for _ in range(N)])
def t09(r): return ("Spot 10 differences", "Be systematic: left to right.", [changed(r, POOL, 10) for _ in range(N)])
def t10(r):
    rounds = []
    for _ in range(N):
        n = "".join(str(r.randint(0, 9)) for _ in range(6))
        d = pick(r, f"Chunk it: {n[:3]} {n[3:]}. What were the last three digits?", n[3:], [n[:3], n[3:][::-1] if n[3:][::-1] != n[3:] else str((int(n[3:]) + 1) % 1000).zfill(3)]); d["hide"] = True; d["read"] = f"{n[:3]} {n[3:]}"
        rounds.append(d)
    return ("Chunk the numbers", "Groups of three are easier.", rounds)
def t11(r):
    clips = [("Train announcement: platform 4, 9:15 to Leeds.", "Which platform?", "4", ["9", "15"]), ("Weather: sunny morning, rain after 3pm.", "When does rain start?", "After 3pm", ["Morning", "Noon"]),
             ("Coach: bring boots, water and a jacket.", "What do you NOT need?", "A swimsuit", ["Boots", "Water"]), ("Shop: apples £1, pears £2, plums 50p.", "How much are pears?", "£2", ["£1", "50p"]),
             ("Teacher: test on Friday, chapters 3 and 4.", "Which chapters?", "3 and 4", ["1 and 2", "4 and 5"])]
    rounds = []
    for s, q, a, w in clips:
        d = sound(r, s, a, w, q); rounds.append(d)
    return ("Listening detective", "Listen for numbers and names.", rounds)
def t12(r):
    ev = [["Alarm rings", "Shower", "Breakfast", "Bus", "School"], ["Seed planted", "Sprouts", "Grows leaves", "Buds", "Blooms"], ["Rocket fuelled", "Countdown", "Lift-off", "Orbit", "Landing"],
          ["Map found", "Journey", "Cave", "Treasure", "Home"], ["Ingredients", "Mix", "Bake", "Cool", "Decorate"]]
    rounds = []
    for e in ev:
        d = build(r, "Recall the order of events.", e); d["hide"] = True; d["show"] = e; rounds.append(d)
    return ("Sequence of events", "Tell it to yourself like a story.", rounds)
def t13(r):
    rounds = []
    for _ in range(N):
        a, b = r.randint(2, 9), r.randint(2, 9)
        rule = r.choice(["bigger", "even"])
        if rule == "bigger":
            rounds.append(pick(r, f"Task switch! Rule: pick the BIGGER number. {a} or {b}?", str(max(a, b)) if a != b else str(a), [str(min(a, b)) if a != b else str(a + 1)]))
        else:
            ev = a if a % 2 == 0 else a + 1
            rounds.append(pick(r, f"Task switch! Rule: pick the EVEN number. {ev} or {ev + 1}?", str(ev), [str(ev + 1)]))
    return ("Multitask juggle", "Check which rule is active each time.", rounds)
def t14(r): return ("Memory grid 6×6", "Work in sections.", [pairs_round(r, 6) for _ in range(N)])
def t15(r):
    f = [("Japan", "Red circle on white"), ("Canada", "Red maple leaf"), ("Brazil", "Green with yellow diamond"), ("Italy", "Green, white, red stripes"),
         ("USA", "Stars and stripes"), ("UK", "Union Jack"), ("Kenya", "Black, red, green with a shield")]
    return ("Name that flag", "Notice colours and symbols.", [match(r.sample(f, 3)) for _ in range(N)])
def t16(r):
    m = [("Planets in order", "My Very Easy Method Just Speeds Up Naming"), ("Rainbow colours", "ROY G BIV"), ("Compass points", "Never Eat Soggy Waffles"),
         ("Great Lakes", "HOMES"), ("Music lines E G B D F", "Every Good Boy Deserves Fudge")]
    return ("Mnemonic maker", "A silly sentence holds a list.", [match(r.sample(m, 3)) for _ in range(N)])
def t17(r): return ("Detail detective", "Tiny details matter.", [changed(r, POOL, 9, "What tiny thing changed?") for _ in range(N)])
def t18(r): return ("Rhythm memory pro", "Longer and faster.", [rhythm(r, 4, 5 + i) for i in range(N)])
def t19(r):
    art = [("Octopuses have three hearts and blue blood.", "How many hearts does an octopus have?", "3", ["1", "2"]), ("Honey never spoils. Jars 3,000 years old were still good.", "What never spoils?", "Honey", ["Milk", "Bread"]),
           ("A day on Venus is longer than its year.", "Which is longer on Venus?", "Its day", ["Its year", "They're equal"]), ("Bananas are berries but strawberries are not.", "Which is a berry?", "Banana", ["Strawberry", "Neither"]),
           ("Sharks existed before trees.", "What came first?", "Sharks", ["Trees", "Dinosaurs"])]
    rounds = []
    for s, q, a, w in art:
        d = pick(r, q, a, w); d["read"] = s; d["hide"] = True; rounds.append(d)
    return ("Recall the article", "Read, then answer from memory.", rounds)
def t20(r):
    rounds = []
    for _ in range(N):
        moves = r.choices(["Up", "Right", "Down", "Left"], k=6)
        d = build(r, "Plan the maze route: " + " ".join(moves), moves); d["hide"] = True; d["show"] = moves
        rounds.append(d)
    return ("Mind maze", "Memorise in chunks of three.", rounds)

GEN = {
    "cubs": [c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20],
    "explorers": [e01, e02, e03, e04, e05, e06, e07, e08, e09, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20],
    "trailblazers": [t01, t02, t03, t04, t05, t06, t07, t08, t09, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20],
}
