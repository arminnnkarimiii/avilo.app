"""Creativity Studio: 20 activities per band."""
from common import *

N = 5


def drawing(r, words, wrong_pool):
    out = []
    for w in r.sample(words, N if len(words) >= N else len(words)):
        out.append(draw(w, r.sample([x for x in wrong_pool if x != w], 2)))
    return out


EASY = ["sun", "cat", "house", "tree", "fish", "flower", "car", "star", "apple", "ball", "moon", "heart"]
MID = ["rocket", "rainbow", "snowman", "butterfly", "castle", "dinosaur", "bicycle", "robot", "umbrella", "volcano"]
HARD = ["lighthouse", "dragon", "skateboard", "telescope", "submarine", "waterfall", "helicopter", "octopus", "pyramid", "guitar"]
GUESS = EASY + MID + HARD + ["cloud", "boat", "egg", "snake", "potato", "hat"]


def colouring(r, icon):
    out = []
    for _ in range(N):
        c = r.choice(COLORS)
        out.append(pick(r, f"Colour time! Which {icon} is {c}?", tok(icon, c), [tok(icon, x) for x in r.sample([x for x in COLORS if x != c], 2)]))
    return out


# ---------------- Little Cubs ----------------
def c01(r): return ("Draw it, Avi guesses!", "Draw big and simple. Avi will guess.", drawing(r, EASY, GUESS))
def c02(r): return ("Color the dino", "Pick the color Avi asks for.", colouring(r, "dino"))
def c03(r): return ("Drum jam", "Copy the drum beat.", [rhythm(r, 2, 2 + i % 3) for i in range(N)])
def c04(r):
    faces = [["Eyes", "Nose", "Mouth"], ["Hair", "Eyes", "Smile"], ["Ears", "Eyes", "Nose", "Mouth"], ["Hat", "Eyes", "Big grin"], ["Eyebrows", "Eyes", "Tongue out"]]
    return ("Build a funny face", "Top to bottom: what goes first?", [build(r, "Build the face from top to bottom.", f) for f in faces])
def c05(r): return ("Finger-paint stars", "Follow the dots to paint a star.", [trace("star", shape_path("star")) for _ in range(2)] + [trace("star", [(x * 0.8 + 10, y * 0.8 + 10) for x, y in shape_path("star")]) for _ in range(2)])
def c06(r):
    an = [("Cat", ["circle", "triangle"]), ("Fish", ["diamond", "triangle"]), ("House", ["triangle", "square"]), ("Rocket", ["triangle", "rect"]), ("Snowman", ["circle", "circle"])]
    rounds = []
    for name, parts in an:
        right = " + ".join(p for p in parts)
        rounds.append(pick(r, f"Which shapes make a {name.lower()}?", right, [" + ".join(r.sample(["square", "star", "heart", "rect", "diamond"], 2)), "heart + star"]))
    return ("Shape animals", "Look for big shapes inside the picture.", rounds)
def c07(r): return ("Sing the ABC", "Tap along with each letter beat.", [rhythm(r, 3, 3 + i % 2) for i in range(N)])
def c08(r):
    outfits = [["Hat", "Shirt", "Trousers", "Boots"], ["Straw hat", "Scarf", "Coat"], ["Hat", "Patches", "Boots"], ["Sun hat", "Shirt", "Shoes"], ["Crown", "Cape", "Boots"]]
    return ("Dress the scarecrow", "Dress from head to toe.", [build(r, "Dress the scarecrow from head to toe.", o) for o in outfits])
def c09(r):
    sc = [["Sky", "Sun", "Tree", "Dog"], ["Sea", "Boat", "Fish"], ["Night", "Moon", "Stars"], ["Grass", "Flowers", "Butterfly"], ["Snow", "Snowman", "Hat"]]
    return ("Sticker story scene", "Background first, then the stars of the show.", [build(r, "Build the scene: background first.", s) for s in sc])
def c10(r): return ("Draw a sun", "Round circle, then rays.", [trace("sun", shape_path("circle")) for _ in range(2)] + [trace("sun", [(x * 0.7 + 15, y * 0.7 + 15) for x, y in shape_path("circle")]) for _ in range(2)])
def c11(r):
    mix = [("Red + yellow", "Orange"), ("Blue + yellow", "Green"), ("Red + blue", "Purple"), ("Red + white", "Pink"), ("Black + white", "Grey")]
    return ("Mix two colors", "Two colors make a new one!", [choice(f"{a} makes…", [(b, True, "That's the new color!"), (r.choice([x for _, x in mix if x != b]), False, "Try mixing them in your mind.")]) for a, b in mix])
def c12(r):
    rb = ["red", "orange", "yellow", "green", "blue", "purple"]
    return ("Make a rainbow", "Red is always on the outside.", [build(r, "Build the rainbow.", [tok("rect", c) for c in rb[i:i + 3 + i % 2]]) for i in range(N)])
def c13(r): return ("Animal band", "Each animal plays a beat. Copy them.", [rhythm(r, 3, 3 + i % 2) for i in range(N)])
def c14(r):
    cakes = [["Sponge", "Cream", "Strawberries"], ["Cake", "Icing", "Candles"], ["Base", "Jam", "Sprinkles"], ["Cake", "Chocolate", "Cherry"], ["Cupcake", "Frosting", "Star"]]
    return ("Decorate a cake", "Bottom first, then decorate!", [build(r, "Decorate from bottom to top.", c) for c in cakes])
def c15(r): return ("Draw your family", "Draw everyone you love. Avi will guess.", drawing(r, ["mum", "dad", "baby", "grandma", "dog", "cat"], GUESS + ["mum", "dad", "baby", "grandma"]))
def c16(r):
    return ("Puppet show", "You choose what happens next!", [
        choice("The puppet bear is hungry. What should he eat?", [("Honey", True, "Bears love honey!"), ("A shoe", True, "A silly choice, the audience laughs!")]),
        choice("A dragon puppet appears. What does it do?", [("Says hello", True, "A friendly dragon!"), ("Sneezes glitter", True, "Sparkly!")]),
        choice("The puppets go to the beach. They…", [("Build a sandcastle", True, "Great building!"), ("Swim with fish", True, "Splash!")]),
        choice("It starts to rain on the show.", [("Puppets open umbrellas", True, "Clever!"), ("Puppets dance in puddles", True, "So fun!")]),
        choice("How should the show end?", [("Everyone bows", True, "Take a bow!"), ("A big dance party", True, "Hooray!")]),
    ])
def c17(r):
    return ("Fill the fish bowl", "Count the fish you add.", [count(r, "fish", n, "How many fish are in the bowl?", color=c) for n, c in zip(r.sample(range(2, 8), N), r.sample(COLORS, N))])
def c18(r): return ("Dot to dot", "Join the numbers in order.", [trace(n, shape_path(n)) for n in ["house", "heart", "fish", "boat", "rocket"]])
def c19(r): return ("Shake the maracas", "Tap to the beat.", [rhythm(r, 2, 3 + i % 2) for i in range(N)])
def c20(r):
    sc = [["Bucket of sand", "Tip it out", "Add a flag"], ["Dig a moat", "Build towers", "Add shells"], ["Wet sand", "Pat it down", "Carve windows"], ["Big base", "Middle tower", "Top tower"], ["Walls", "Gate", "Flag"]]
    return ("Build a sandcastle", "Strong base first.", [build(r, "Build the sandcastle in order.", s) for s in sc])

# ---------------- Explorers ----------------
def e01(r): return ("Draw it, Avi guesses: harder words", "Add details so Avi can tell.", drawing(r, MID, GUESS))
def e02(r):
    cs = [["Hero wakes up", "Finds a map", "Sets off", "Finds treasure"], ["Cat sees a mouse", "Chases it", "Trips over", "Mouse escapes"], ["Rain starts", "Kids find a puddle", "Big splash", "Everyone laughs"],
          ["Robot is lonely", "Builds a friend", "They play", "Best friends"], ["Seed is planted", "Storm comes", "Sun returns", "Flower blooms"]]
    return ("Comic strip maker", "Panels go left to right.", [build(r, "Order the comic panels.", c) for c in cs])
def e03(r): return ("Compose a melody", "Copy the notes, then make your own.", [rhythm(r, 4, 3 + i) for i in range(N)])
def e04(r):
    m = [["Body shape", "Eyes", "Horns", "Colour"], ["Head", "Body", "Tail", "Spots"], ["Fluffy body", "Big eyes", "Tiny wings"], ["Round body", "Six legs", "Antennae"], ["Long neck", "Stripes", "Smile"]]
    return ("Design a pet monster", "Start with the big shape, then add details.", [build(r, "Design your monster in order.", x) for x in m])
def e05(r):
    rounds = []
    for _ in range(N):
        c1, c2 = r.sample(COLORS, 2)
        seq = [tok("square", c1), tok("square", c2), tok("square", c1), tok("square", c2)]
        rounds.append(pattern(r, seq, tok("square", c1), [tok("square", c2), tok("square", r.choice([c for c in COLORS if c not in (c1, c2)]))], "Continue the pixel row."))
    return ("Pixel art grid", "Pixel art repeats little squares.", rounds)
def e06(r):
    v = [("A car that flies", ["Wings", "Wheels", "Engine"]), ("A boat that drives on roads", ["Wheels", "Hull", "Motor"]), ("A bike for two", ["Two seats", "Two pedals", "Long frame"]),
         ("A space scooter", ["Rocket", "Handlebars", "Seat"]), ("A digger that swims", ["Scoop", "Fins", "Engine"])]
    return ("Invent a vehicle", "Combine parts in a new way!", [build(r, f"Build: {n}. Tap the parts you'd add first.", p) | {"free": True} for n, p in v])
def e07(r):
    mix = [("Red + yellow", "Orange"), ("Yellow + blue", "Green"), ("Blue + red", "Purple"), ("Orange + blue", "Brown"), ("Purple + white", "Lavender")]
    return ("Color mixing lab", "Primary colours make secondary colours.", [choice(f"Mix {a}. You get…", [(b, True, "Correct mix!"), (r.choice([x for _, x in mix if x != b]), False, "Think about which colours combine.")]) for a, b in mix])
def e08(r):
    return ("Story starters", "There's no wrong idea, only your idea!", [
        choice("“I opened the door and saw…”", [("a talking dragon", True, "Exciting!"), ("a room full of jelly", True, "Wobbly and fun!")]),
        choice("“The robot's only wish was…”", [("to taste ice cream", True, "Sweet idea."), ("to learn to dance", True, "Groovy!")]),
        choice("“Deep in the ocean, there was…”", [("a glowing city", True, "Magical."), ("a shy whale", True, "Aww.")]),
        choice("“My shoes started to…”", [("float", True, "Up, up and away!"), ("sing", True, "Musical feet!")]),
        choice("“The map led us to…”", [("a cloud castle", True, "Dreamy."), ("a volcano of popcorn", True, "Pop pop!")]),
    ])
def e09(r): return ("Beat maker", "Layer beats like a DJ.", [rhythm(r, 4, 4 + i % 2) for i in range(N)])
def e10(r): return ("Draw with shapes", "Use circles, squares and triangles.", drawing(r, ["robot", "castle", "rocket", "snowman", "house", "car"], GUESS))
def e11(r):
    p = [("A playground for dinosaurs", ["Giant slide", "Swing", "Sandpit"]), ("A playground in space", ["Moon bounce", "Rocket climb", "Star swing"]), ("A water playground", ["Splash pad", "Water slide", "Fountain"]),
         ("A treehouse park", ["Rope bridge", "Ladder", "Lookout"]), ("A quiet playground", ["Reading nook", "Garden", "Hammock"])]
    return ("Design a playground", "Think about who will play there.", [build(r, f"{n}: choose your order.", x) | {"free": True} for n, x in p])
def e12(r):
    mk = [["Cut the shape", "Cut eye holes", "Decorate", "Add string"], ["Paper plate", "Paint it", "Add feathers", "Tie elastic"], ["Draw a face", "Cut it out", "Colour it", "Add a stick"],
          ["Cardboard", "Cut out", "Glitter", "Ribbon"], ["Fold paper", "Cut eyes", "Draw stripes", "Wear it"]]
    return ("Make a mask", "Plan, cut, decorate.", [build(r, "Order the mask steps.", m) for m in mk])
def e13(r): return ("Paint your mood", "Draw how you feel. Avi guesses the mood.", [draw(m, r.sample([x for x in ["happy", "sad", "excited", "calm", "silly", "sleepy"] if x != m], 2)) for m in r.sample(["happy", "sad", "excited", "calm", "silly"], N)])
def e14(r):
    s = [("Twinkle twinkle little ___", "star", ["car", "jar"]), ("Old MacDonald had a ___", "farm", ["car", "bear"]), ("Row, row, row your ___", "boat", ["goat", "coat"]),
         ("The wheels on the bus go round and ___", "round", ["square", "down"]), ("If you're happy and you know it, clap your ___", "hands", ["feet", "head"])]
    return ("Finish the song", "Sing it in your head.", [sound(r, l.replace("___", a), a, w, l) for l, a, w in s])
def e15(r):
    f = [["Ball on the ground", "Ball goes up", "Ball at the top", "Ball comes down"], ["Seed", "Sprout", "Stem", "Flower"], ["Closed eyes", "Half open", "Wide awake"],
         ["Frame 1", "Frame 2", "Frame 3", "Frame 4"], ["Walk", "Run", "Jump", "Land"]]
    return ("Stop-motion frames", "Tiny changes make movement.", [build(r, "Put the animation frames in order.", x) for x in f])
def e16(r): return ("Draw the ending", "What happens last? Draw it!", drawing(r, ["treasure", "party", "rainbow", "castle", "rocket"], GUESS + ["treasure", "party"]))
def e17(r):
    ins = [("Drum", "Hit"), ("Guitar", "Strum"), ("Flute", "Blow"), ("Piano", "Press keys"), ("Violin", "Bow"), ("Trumpet", "Buzz lips")]
    return ("Instrument match", "How do you play it?", [match(r.sample(ins, 3)) for _ in range(N)])
def e18(r):
    t = [["Wide base", "Strong middle", "Pointy top"], ["Foundation", "Walls", "Roof"], ["Big blocks", "Medium blocks", "Small blocks"], ["Square base", "Pillars", "Dome"], ["Ground floor", "First floor", "Rooftop garden"]]
    return ("Architect tower", "Wide at the bottom stays standing.", [build(r, "Build the tower from the ground up.", x) for x in t])
def e19(r):
    rounds = []
    for _ in range(N):
        a, b, c = r.sample(["heart", "star", "diamond", "circle", "square"], 3)
        cl = r.sample(COLORS, 2)
        seq = [tok(a, cl[0]), tok(b, cl[1]), tok(c, cl[0]), tok(a, cl[0]), tok(b, cl[1])]
        rounds.append(pattern(r, seq, tok(c, cl[0]), [tok(a, cl[0]), tok(c, cl[1])], "Continue the quilt pattern."))
    return ("Pattern quilt", "Find the repeating part.", rounds)
def e20(r):
    fl = [("Flag of Kindness", ["Heart", "Blue background", "Yellow stars"]), ("Flag of Adventure", ["Mountain", "Green stripe", "Sun"]), ("Flag of Science", ["Atom", "Purple", "Stars"]),
          ("Flag of the Ocean", ["Waves", "Blue", "Fish"]), ("Flag of Music", ["Note", "Red stripe", "Gold border"])]
    return ("Create a flag", "Pick symbols that mean something.", [build(r, f"{n}: add the parts in your order.", p) | {"free": True} for n, p in fl])

# ---------------- Trailblazers ----------------
def t01(r): return ("Draw it, Avi guesses: expert", "Draw the key features first.", drawing(r, HARD, GUESS))
def t02(r):
    s = [["Introduce the hero", "Problem appears", "Hero struggles", "Turning point", "Resolution"], ["Ordinary day", "Strange letter", "Journey begins", "Big challenge", "Returns changed"],
         ["Setting", "Character", "Conflict", "Climax", "Ending"], ["Hook", "Build tension", "Twist", "Ending"], ["Opening line", "Rising action", "Climax", "Falling action"]]
    return ("Write a short story", "Plan the shape before writing.", [build(r, "Order your story plan.", x) for x in s])
def t03(r): return ("Music producer", "Layer the beat track by track.", [rhythm(r, 4, 5 + i % 3) for i in range(N)])
def t04(r):
    return ("Design a logo", "Simple logos are memorable.", [
        choice("A logo for a pet shop should be…", [("Simple and friendly", True, "Easy to recognise."), ("Covered in tiny text", False, "Too hard to read.")]),
        choice("How many colours usually work best?", [("2–3", True, "Clean and clear."), ("15", False, "Too busy.")]),
        choice("Your logo should look good…", [("Small and big", True, "It appears everywhere."), ("Only huge", False, "Logos shrink on phones.")]),
        choice("A bakery logo could use…", [("A simple loaf or whisk shape", True, "Relevant symbol."), ("A random car", False, "Doesn't match.")]),
        build(r, "Order the logo process.", ["Brainstorm", "Sketch", "Pick the best", "Refine"]),
    ])
def t05(r):
    f = [["Ball high", "Falling", "Squash on ground", "Stretch up"], ["Start pose", "Anticipation", "Action", "Follow-through"], ["Key frame 1", "In-between", "Key frame 2"],
         ["Sketch", "Line art", "Colour", "Play"], ["Storyboard", "Animate", "Add sound"]]
    return ("Animate a bouncing ball", "Squash on impact, stretch in the air.", [build(r, "Order the animation steps.", x) for x in f])
def t06(r):
    g = [("Shoes that tie themselves", ["Sensor", "Tiny motor", "Laces"]), ("A homework helper robot", ["Camera", "Speaker", "Screen"]), ("An umbrella drone", ["Propellers", "Umbrella", "Battery"]),
         ("A self-watering plant pot", ["Water tank", "Soil sensor", "Pump"]), ("A glowing book", ["Light strip", "Battery", "Switch"])]
    return ("Invent a gadget", "Solve a real problem.", [build(r, f"{n}: order the parts you'd build first.", p) | {"free": True} for n, p in g])
def t07(r): return ("Perspective drawing", "Things far away look smaller.", drawing(r, ["road", "railway", "skyscraper", "hallway", "bridge"], GUESS + ["road", "railway", "skyscraper", "hallway", "bridge"]))
def t08(r):
    p = [["Pick a topic", "Brainstorm words", "Find rhymes", "Write lines", "Read aloud"], ["Choose a feeling", "Pick images", "Write a first line", "Edit"],
         ["Haiku: 5 syllables", "7 syllables", "5 syllables"], ["Title", "Verse 1", "Chorus", "Verse 2"], ["Notice something", "Describe it", "Add a twist"]]
    return ("Poem workshop", "Poems are built line by line.", [build(r, "Order the poem steps.", x) for x in p])
def t09(r):
    sb = [["Wide shot", "Medium shot", "Close-up"], ["Establishing shot", "Action", "Reaction"], ["Sunrise", "Chase", "Showdown", "Sunset"], ["Hero enters", "Villain appears", "Battle", "Victory"], ["Quiet room", "Door creaks", "Shadow", "Reveal"]]
    return ("Movie storyboard", "Shots tell the story visually.", [build(r, "Order the storyboard.", x) for x in sb])
def t10(r):
    qs = [("Warm colours are…", "Red, orange, yellow", ["Blue, green, purple", "Black, white"]), ("Cool colours feel…", "Calm", ["Hot", "Loud"]),
          ("Complementary colours are…", "Opposite on the colour wheel", ["Next to each other", "Always grey"]), ("Blue's complementary colour is…", "Orange", ["Green", "Purple"]),
          ("Adding white to a colour makes a…", "Tint", ["Shade", "Tone"])]
    return ("Color palettes", "The colour wheel is your map.", [pick(r, q, a, w) for q, a, w in qs])
def t11(r):
    c = [("Hero", ["Goal", "Weakness", "Special skill"]), ("Villain", ["Motive", "Plan", "Secret"]), ("Sidekick", ["Joke style", "Loyalty", "Talent"]), ("Mentor", ["Wisdom", "Past", "Gift"]), ("Creature", ["Habitat", "Diet", "Power"])]
    return ("Character creator", "Great characters want something.", [build(r, f"Create your {n}: order the details.", d) | {"free": True} for n, d in c])
def t12(r):
    a = [("Mona Lisa", "Leonardo da Vinci"), ("The Starry Night", "Vincent van Gogh"), ("Water Lilies", "Claude Monet"), ("The Scream", "Edvard Munch"), ("Guernica", "Pablo Picasso"), ("The Great Wave", "Hokusai")]
    return ("Famous art match", "Each artist has a style.", [match(r.sample(a, 3)) for _ in range(N)])
def t13(r):
    rounds = []
    for _ in range(N):
        cs = r.sample(COLORS, 3)
        seq = [tok("square", cs[i % 3]) for i in range(5)]
        rounds.append(pattern(r, seq, tok("square", cs[5 % 3]), [tok("square", cs[0]), tok("square", cs[1])] if cs[2] != cs[5 % 3] else [tok("square", cs[0]), tok("square", cs[1])], "Next pixel in the animation loop?"))
    return ("Pixel art animation", "Loops repeat smoothly.", rounds)
def t14(r):
    return ("Remix a fairy tale", "Change one thing and see what happens!", [
        choice("Cinderella, but in space. The glass slipper becomes…", [("A moon boot", True, "Space style!"), ("A rocket sock", True, "Fun twist!")]),
        choice("The Three Little Pigs build houses of…", [("Lego", True, "Strong and colourful!"), ("Pancakes", True, "Delicious but floppy!")]),
        choice("Little Red Riding Hood rides a…", [("Skateboard", True, "Speedy!"), ("Dragon", True, "Epic!")]),
        choice("Jack's beanstalk leads to…", [("An underwater city", True, "Surprising!"), ("A video game world", True, "Level up!")]),
        choice("Goldilocks tries three…", [("Pizzas", True, "Too hot, too cold, just right!"), ("Spaceships", True, "Too fast, too slow, just right!")]),
    ])
def t15(r): return ("Rhythm battle", "Match Avi's beats, then beat them.", [rhythm(r, 4, 6 + i % 3) for i in range(N)])
def t16(r):
    c = [["Roads", "Houses", "Shops", "Park"], ["Power plant", "Water tower", "Homes", "School"], ["Map the river", "Build bridges", "Add markets"], ["Plan zones", "Build transport", "Add homes", "Add green spaces"], ["Town square", "Streets", "Library", "Museum"]]
    return ("Build a city", "Cities need roads before buildings.", [build(r, "Order your city plan.", x) for x in c])
def t17(r):
    o = [("Rainy day outfit", ["Raincoat", "Wellies", "Umbrella"]), ("Party look", ["Sparkly top", "Jeans", "Trainers"]), ("Space explorer", ["Helmet", "Silver suit", "Moon boots"]),
         ("Beach day", ["Sun hat", "T-shirt", "Sandals"]), ("Winter adventure", ["Beanie", "Puffer coat", "Snow boots"])]
    return ("Fashion designer", "Head to toe, with a theme.", [build(r, f"{n}: dress head to toe.", x) for n, x in o])
def t18(r): return ("Draw a photo story", "Draw the most important moment.", drawing(r, ["birthday", "beach", "camping", "concert", "snowball fight"], GUESS + ["birthday", "beach", "camping", "concert", "snowball fight"]))
def t19(r):
    s = [("Thunder", "Shake a metal sheet"), ("Horse hooves", "Clap coconut shells"), ("Rain", "Pour rice on paper"), ("Fire crackling", "Crumple cellophane"), ("Footsteps in snow", "Squeeze cornflour"), ("Wind", "Blow across a bottle")]
    return ("Sound effects studio", "Everyday objects make movie sounds.", [match(r.sample(s, 3)) for _ in range(N)])
def t20(r): return ("Sketch your dream app", "Sketch the main screen. Avi guesses what it does.", [draw(w, r.sample([x for x in ["game", "map", "music player", "camera", "calendar"] if x != w], 2)) for w in r.sample(["game", "map", "music player", "camera", "calendar"], N)])

GEN = {
    "cubs": [c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20],
    "explorers": [e01, e02, e03, e04, e05, e06, e07, e08, e09, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20],
    "trailblazers": [t01, t02, t03, t04, t05, t06, t07, t08, t09, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20],
}
