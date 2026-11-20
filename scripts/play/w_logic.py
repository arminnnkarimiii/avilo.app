"""Logic Lane: 20 activities per band."""
from common import *

N = 5
SHAPES = ["circle", "square", "triangle", "star", "heart", "diamond"]


def abpat(r, kinds):
    a, b = kinds
    return [a, b, a, b], a


# ---------------- Little Cubs ----------------
def c01(r):
    rounds = []
    for k in range(N):
        a, b, c = r.sample(SHAPES, 3)
        seq = [tok(a, "red"), tok(b, "blue"), tok(a, "red"), tok(b, "blue")] if k % 2 == 0 else [tok(a), tok(b), tok(c), tok(a), tok(b)]
        right = tok(a, "red") if k % 2 == 0 else tok(c)
        wrong = [tok(b, "blue") if k % 2 == 0 else tok(a), tok(r.choice([s for s in SHAPES if s not in (a, b, c)]))]
        rounds.append(pattern(r, seq, right, wrong))
    return ("What comes next?", "Say the pattern out loud.", rounds)
def c02(r):
    groups = [(["apple", "cookie", "egg"], "car"), (["fish", "duck", "shell"], "rocket"), (["cat", "dog", "duck"], "block"), (["sun", "moon", "star"], "cup"),
              (["tree", "flower", "leaf"], "ball"), (["drum", "bell", "book"], "fish")]
    rounds = []
    for same, odd in r.sample(groups, N):
        rounds.append(pick(r, "Which one doesn't belong?", tok(odd), [tok(s) for s in same]))
    return ("Odd one out", "Three are alike. Which one is different?", rounds)
def c03(r): return ("Simple maze", "Follow the path with your finger.", [trace("maze", p) for p in [zigzag(6, 25), wave(7, 22, 1), zigzag(7, 30), wave(8, 28, 1.5), zigzag(8, 20)]])
def c04(r):
    pairs = [("@cat", "@cat:brown"), ("@star", "@star:brown"), ("@fish", "@fish:brown"), ("@apple", "@apple:brown"), ("@duck", "@duck:brown"), ("@tree", "@tree:brown"), ("@house", "@house:brown")]
    return ("Shadow match", "A shadow has the same shape, but it's dark.", [match(r.sample(pairs, 3)) for _ in range(N)])
def c05(r):
    rounds = []
    for k in range(N):
        n = 3 + (k % 2)
        ic = r.choice(["ball", "block", "circle", "star"])
        rounds.append(build(r, "Line them up from biggest to smallest.", [tok(ic, "blue", i) for i in range(n, 0, -1)]))
    return ("Big to small", "Find the biggest first.", rounds)
def c06(r):
    pics = [["Head", "Body", "Legs"], ["Roof", "Walls", "Door"], ["Top", "Middle", "Bottom"], ["Sky", "Tree", "Grass"], ["Hat", "Face", "Bow"]]
    return ("4-piece puzzle", "Start with the top piece.", [build(r, "Build the picture top to bottom.", p) for p in pics])
def c07(r):
    pairs = [("@cup", "@drop:blue"), ("@key", "@house"), ("@book", "@star"), ("@dog", "@ball"), ("@cat", "@fish"), ("@sun", "@flower"), ("@cloud", "@drop"), ("@bug", "@leaf")]
    pairs = [("Cup", "Juice"), ("Key", "Door"), ("Sock", "Shoe"), ("Dog", "Bone"), ("Toothbrush", "Toothpaste"), ("Pencil", "Paper"), ("Bat", "Ball"), ("Bucket", "Spade")]
    return ("Which go together?", "Things that are used together are a pair.", [match(r.sample(pairs, 3)) for _ in range(N)])
def c08(r):
    rounds = []
    for _ in range(N):
        c1, c2 = r.sample(["red", "blue", "green", "yellow"], 2)
        ics = r.sample(["car", "ball", "block", "star", "heart", "flower"], 5)
        rounds.append(sort([f"{c1.capitalize()} train", f"{c2.capitalize()} train"], shuffled(r, [(tok(i, c1), 0) for i in ics[:3]] + [(tok(i, c2), 1) for i in ics[2:5]])))
    return ("Color sorting train", "Each train only takes one color.", rounds)
def c09(r):
    dirs = ["Up", "Down", "Left", "Right"]
    rounds = []
    for _ in range(N):
        a, b = r.sample(dirs, 2)
        rounds.append(pattern(r, [a, b, a, b], a, [b, r.choice([d for d in dirs if d not in (a, b)])], "Follow the arrows. Which way next?"))
    return ("Follow the arrows", "Arrows repeat in a pattern.", rounds)
def c10(r):
    fixes = [("A cat with no tail. What's missing?", "Tail", ["Hat", "Wheel"]), ("A car with no wheels. What's missing?", "Wheels", ["Wings", "Leaves"]),
             ("A face with no nose. What's missing?", "Nose", ["Roof", "Tail"]), ("A tree with no leaves in summer. What's missing?", "Leaves", ["Wheels", "Nose"]),
             ("A bird with no wings. What's missing?", "Wings", ["Wheels", "Door"]), ("A house with no door. What's missing?", "Door", ["Tail", "Wings"])]
    return ("Fix the picture", "Picture the whole thing in your head.", [pick(r, q, a, w) for q, a, w in r.sample(fixes, N)])
def c11(r):
    rounds = []
    for k in range(N):
        n = 3 + (k % 3)
        rounds.append(build(r, "Stack the cups: biggest on the bottom first.", [tok("cup", "orange", i) for i in range(n, 0, -1)]))
    return ("Stack the cups", "Big cups go on the bottom.", rounds)
def c12(r): return ("Find the pair", "Remember where each picture is.", [match([(tok(i), tok(i)) for i in r.sample(ICONS[:24], 3)]) for _ in range(N)])
def c13(r):
    qs = [("The bird is above the tree. Where is the bird?", "Up high", ["Under the ground", "Inside the tree"]), ("The cat hides under the bed. Where is the cat?", "Below the bed", ["On the roof", "In the sky"]),
          ("The ball is on top of the box. Where is the ball?", "Above the box", ["Under the box", "Inside the box"]), ("The fish swims below the boat. Where is the fish?", "Under the boat", ["Above the boat", "In the boat"]),
          ("The kite flies over the house. Where is the kite?", "Above the house", ["Under the house", "In the house"])]
    return ("Above or below?", "Above is up. Below is down.", [pick(r, q, a, w) for q, a, w in qs])
def c14(r):
    rounds = []
    for _ in range(N):
        a, b = r.sample(SHAPES, 2)
        rounds.append(pick(r, f"Row 1: {a}, {b}. Row 2: {b}, ?", tok(a), [tok(b), tok(r.choice([s for s in SHAPES if s not in (a, b)]))]))
    return ("Shape sudoku 2×2", "Each row needs one of each shape.", rounds)
def c15(r): return ("Count the path", "Count each stepping stone.", [count(r, "circle", n, "How many stepping stones?", color="brown") for n in r.sample(range(3, 10), N)])
def c16(r):
    qs = [("The cat is missing its…", "Tail", ["Wheel", "Roof"], "cat"), ("The rocket is missing its…", "Fire", ["Leaves", "Ears"], "rocket"), ("The tree is missing its…", "Trunk", ["Wings", "Nose"], "tree"),
          ("The house is missing its…", "Roof", ["Tail", "Fins"], "house"), ("The fish is missing its…", "Fins", ["Legs", "Door"], "fish")]
    return ("Missing piece", "Which part would make it whole?", [pick(r, q, a, w, icon=i) for q, a, w, i in qs])
def c17(r):
    ins = ["Fish in a bowl", "Bird in a nest", "Toy in a box", "Milk in a cup", "Car in a garage", "Bee in a hive"]
    out = ["Kite in the sky", "Dog in the yard", "Sun over the hill", "Boat on the lake", "Bike on the path", "Cloud above the tree"]
    return ("In or out?", "Inside means it's in something.", [sort(["Inside", "Outside"], shuffled(r, [(x, 0) for x in r.sample(ins, 3)] + [(x, 1) for x in r.sample(out, 3)])) for _ in range(N)])
def c18(r):
    rounds = []
    for k in range(N):
        moves = r.choices(["Forward", "Turn", "Jump"], k=3)
        rounds.append(build(r, "Program the robot: " + ", then ".join(moves) + ".", moves))
    return ("Robot moves", "Robots follow steps in order.", rounds)
def c19(r):
    h = [("Bird", "Nest"), ("Bee", "Hive"), ("Fish", "Pond"), ("Dog", "Kennel"), ("Rabbit", "Burrow"), ("Spider", "Web"), ("Bear", "Cave"), ("Cow", "Barn")]
    return ("Animal homes", "Every animal has a home that fits it.", [match(r.sample(h, 3)) for _ in range(N)])
def c20(r):
    rounds = []
    for s in r.sample(SHAPES, N):
        c, c2 = r.sample(COLORS, 2)
        rounds.append(pick(r, "Mirror me! Which one is the same on the other side?", tok(s, c), [tok(s, c2), tok(r.choice([x for x in SHAPES if x != s]), c)], icon=s))
    return ("Mirror me", "A mirror shows the same shape and color.", rounds)

# ---------------- Explorers ----------------
def e01(r):
    rounds = []
    for _ in range(N):
        nums = r.sample(range(1, 5), 4)
        missing = r.randrange(4)
        row = [str(n) if i != missing else "?" for i, n in enumerate(nums)]
        rounds.append(pick(r, f"Each row has 1–4 once. Row: {' '.join(row)}. What is ?", str(nums[missing]), [str(n) for n in range(1, 5) if n != nums[missing]][:2]))
    return ("Sudoku 4×4", "Each number appears once in every row.", rounds)
def e02(r):
    rounds = []
    for _ in range(N):
        moves = r.choices(["Up", "Right", "Down", "Left"], k=4)
        rounds.append(build(r, "Code the robot to the star: " + " → ".join(moves), moves))
    return ("Code the robot", "Read the code from left to right.", rounds)
def e03(r):
    t = [("A square made of 2 triangles needs how many?", "2", ["3", "4"]), ("How many tangram pieces are there?", "7", ["5", "9"]),
         ("Two right triangles can make a…", "Square", ["Circle", "Star"]), ("A tangram's biggest pieces are…", "Triangles", ["Circles", "Hearts"]),
         ("Four small triangles can make a…", "Bigger triangle", ["Circle", "Oval"])]
    return ("Tangram shapes", "Turn and flip pieces in your head.", [pick(r, q, a, w) for q, a, w in t])
def e04(r):
    puzzles = [("Ana, Ben and Cal own a cat, a dog and a fish. Ana's pet barks. Ben's pet swims. Cal owns…", "The cat", ["The dog", "The fish"]),
               ("Three kids like red, blue and green. Mia hates red. Leo likes blue. Mia likes…", "Green", ["Red", "Blue"]),
               ("Sam is taller than Tia. Tia is taller than Ola. Who is shortest?", "Ola", ["Sam", "Tia"]),
               ("The bike is between the car and the bus. The car is first. What is last?", "The bus", ["The car", "The bike"]),
               ("Ivy is older than Max but younger than Zoe. Who is oldest?", "Zoe", ["Ivy", "Max"])]
    return ("Logic grid: pets", "Cross out what can't be true.", [pick(r, q, a, w) for q, a, w in puzzles])
def e05(r):
    rounds = []
    for _ in range(N):
        a, d = r.randint(1, 10), r.choice([2, 3, 5, 10])
        rounds.append(pattern(r, [str(a + d * i) for i in range(3)], str(a + 3 * d), [str(a + 3 * d + 1), str(a + 2 * d + 1)]))
    return ("Number patterns", "Find how much it grows each time.", rounds)
def e06(r):
    plans = [["Get the key", "Open the door", "Walk through"], ["Find the map", "Follow the path", "Dig for treasure"], ["Pick up the torch", "Enter the cave", "Find the exit"],
             ["Climb the ladder", "Grab the key", "Unlock the gate"], ["Cross the bridge", "Collect the gem", "Reach the castle"]]
    return ("Maze with keys", "You need the key before the door.", [build(r, "Order the moves to escape.", p) for p in plans])
def e07(r):
    return ("River crossing", "Think about what happens when you leave things together.", [
        choice("A farmer must cross with a fox, a chicken and grain. The boat fits one. What goes first?", [("The chicken", True, "Fox won't eat grain, so the chicken goes first."), ("The fox", False, "The chicken would eat the grain."), ("The grain", False, "The fox would eat the chicken.")]),
        choice("Chicken is across. What next?", [("Take the fox, bring the chicken back", True, "Swap so they're never alone together."), ("Take the grain and stay", False, "Then the chicken eats the grain later.")]),
        choice("Two kids weigh 40 kg each, the boat holds 80 kg. Can they cross together?", [("Yes", True, "40 + 40 = 80, just fits."), ("No", False, "It holds exactly 80 kg.")]),
        choice("Three friends, one boat for two. One must row back. How many trips at least?", [("3 trips", True, "Two across, one back, two across."), ("1 trip", False, "The boat only holds two.")]),
        choice("A goat and cabbage can't be left alone. You have a wolf too. Who never needs to be left alone with the cabbage?", [("The wolf", True, "Wolves don't eat cabbage."), ("The goat", False, "Goats eat cabbage!")]),
    ])
def e08(r):
    fly = ["Bird", "Bee", "Bat", "Butterfly", "Plane"]
    swim = ["Fish", "Dolphin", "Shark", "Seal", "Boat"]
    return ("Venn diagram sort", "Each thing goes in the circle it fits.", [sort(["Flies", "Swims"], shuffled(r, [(x, 0) for x in r.sample(fly, 3)] + [(x, 1) for x in r.sample(swim, 3)])) for _ in range(N)])
def e09(r):
    qs = [("An arrow points up. Turn it a quarter turn right. It points…", "Right", ["Down", "Left"]), ("An arrow points right. Turn it half a turn. It points…", "Left", ["Up", "Right"]),
          ("An arrow points down. Quarter turn left. It points…", "Right", ["Left", "Up"]), ("A triangle points up. Flip it upside down. It points…", "Down", ["Up", "Left"]),
          ("An arrow points left. Full turn. It points…", "Left", ["Right", "Up"])]
    return ("Rotate the shape", "Picture turning it like a clock hand.", [pick(r, q, a, w) for q, a, w in qs])
def e10(r):
    return ("If-then rules", "If the first part is true, the second happens.", [
        choice("Rule: If it rains, we take umbrellas. It's raining. So…", [("We take umbrellas", True, "The rule says so."), ("We wear sunglasses", False, "Follow the rule.")]),
        choice("Rule: If the light is red, stop. The light is red. So…", [("Stop", True, "Red means stop."), ("Go fast", False, "Never on red.")]),
        choice("Rule: If you finish homework, you can play. You finished. So…", [("You can play", True, "Rule met!"), ("You must sleep", False, "The rule says play.")]),
        choice("Rule: If it's Saturday, there's no school. It's Saturday. So…", [("No school", True, "Correct."), ("School is on", False, "Not on Saturday.")]),
        choice("Rule: If the dog barks, someone is at the door. The dog barks. So…", [("Someone is at the door", True, "That's the rule."), ("The dog is hungry", False, "The rule talks about the door.")]),
    ])
def e11(r):
    rid = [("What has hands but can't clap?", "A clock", ["A tree", "A dog"]), ("What gets wetter the more it dries?", "A towel", ["A sponge cake", "Sand"]),
           ("What has a neck but no head?", "A bottle", ["A shirt", "A giraffe"]), ("What has keys but can't open locks?", "A piano", ["A door", "A car"]),
           ("What goes up but never comes down?", "Your age", ["A ball", "A kite"]), ("What has one eye but can't see?", "A needle", ["A pirate", "A cat"])]
    return ("Riddle me this", "Think about other meanings of the words.", [pick(r, q, a, w) for q, a, w in r.sample(rid, N)])
def e12(r):
    rounds = []
    for _ in range(N):
        segs = r.choices(["Straight", "Bend", "Corner", "T-piece"], k=3)
        rounds.append(build(r, "Connect the pipe in this order: " + ", ".join(segs), segs))
    return ("Pipe connect", "Plan the path before you place.", rounds)
def e13(r):
    rounds = []
    for _ in range(N):
        a, b = r.randint(2, 9), r.randint(2, 9)
        rounds.append(pick(r, f"Left pan: {a} + {b}. Right pan: ? Balance it!", str(a + b), [str(a + b + 1), str(a * b if a * b != a + b else a + b + 2)]))
    return ("Balance the scale", "Both sides must be equal.", rounds)
def e14(r): return ("Spot the difference", "Look carefully, one thing changes.", [changed(r, ICONS[:24], 6) for _ in range(N)])
def e15(r):
    sts = [["Caterpillar hatches", "Eats leaves", "Makes a cocoon", "Becomes a butterfly"], ["Wake up", "Get dressed", "Eat breakfast", "Go to school"],
           ["Mix batter", "Pour in pan", "Bake", "Eat pancakes"], ["Buy seeds", "Plant", "Water", "Pick flowers"], ["Write letter", "Put in envelope", "Add stamp", "Post it"]]
    return ("Sequence the story", "What has to happen first?", [build(r, "Put the events in order.", s) for s in sts])
def e16(r):
    return ("Bridge builder", "Triangles make bridges strong.", [
        choice("Which shape makes the strongest bridge frame?", [("Triangles", True, "Triangles don't bend out of shape."), ("Circles of string", False, "String sags.")]),
        choice("Your paper bridge sags. What helps?", [("Fold it into pleats", True, "Folds make it stiffer."), ("Make it wetter", False, "Wet paper is weaker.")]),
        choice("Where should the supports go?", [("At both ends", True, "Ends carry the load to the ground."), ("Nowhere", False, "Bridges need support.")]),
        choice("A longer bridge needs…", [("More support", True, "Longer spans bend more."), ("Less support", False, "Longer is harder.")]),
        choice("To test it, you…", [("Add weights slowly", True, "Careful testing shows the limit."), ("Jump on it", False, "Test safely!")]),
    ])
def e17(r):
    words = ["CAT", "DOG", "SUN", "MAP", "OWL", "BEE", "FOX", "HAT"]
    rounds = []
    for word in r.sample(words, N):
        shift = r.randint(1, 3)
        code = "".join(chr((ord(c) - 65 + shift) % 26 + 65) for c in word)
        rounds.append(pick(r, f"Secret code: {code}. Each letter moved forward {shift}. What's the word?", word, r.sample([w for w in words if w != word], 2)))
    return ("Secret code", "Move each letter back the same number of places.", rounds)
def e18(r):
    return ("Tower of Hanoi: 3 rings", "Move the small ring first, and never put big on small.", [build(r, "Order the first moves.", ["Small to C", "Medium to B", "Small to B"]), build(r, "Next moves.", ["Large to C", "Small to A", "Medium to C"]),
            build(r, "Last moves.", ["Small to C", "Tower complete"]), build(r, "Order rings bottom to top.", ["Large", "Medium", "Small"]), build(r, "Order the rule.", ["Move one ring", "Never big on small", "Rebuild on the end peg"])])
def e19(r):
    an = [("Bird is to nest as bee is to…", "Hive", ["Tree", "Flower"]), ("Glove is to hand as sock is to…", "Foot", ["Hat", "Arm"]), ("Big is to small as hot is to…", "Cold", ["Warm", "Fire"]),
          ("Puppy is to dog as kitten is to…", "Cat", ["Mouse", "Fish"]), ("Pen is to write as brush is to…", "Paint", ["Read", "Sleep"]), ("Triangle is to 3 as square is to…", "4", ["5", "3"])]
    return ("Shape analogies", "Find how the first pair is linked.", [pick(r, q, a, w) for q, a, w in r.sample(an, N)])
def e20(r):
    bugs = [("Robot code: Forward, Forward, Right. It should turn left. Fix which step?", "Right → Left", ["First Forward", "Second Forward"]),
            ("Code: Jump, Walk, Jump. It should walk first. Fix by…", "Swapping the first two", ["Adding a jump", "Deleting a walk"]),
            ("The robot stops one square early. Add…", "One more Forward", ["A Turn", "A Jump"]),
            ("It walks into a wall. Before the wall add…", "A Turn", ["Another Forward", "Nothing"]),
            ("It repeats forever. Add a…", "Stop", ["Forward", "Turn"])]
    return ("Debug the robot", "Find the step that goes wrong.", [pick(r, q, a, w) for q, a, w in bugs])

# ---------------- Trailblazers ----------------
def t01(r):
    rounds = []
    for _ in range(N):
        nums = r.sample(range(1, 7), 6); m = r.randrange(6)
        row = [str(n) if i != m else "?" for i, n in enumerate(nums)]
        rounds.append(pick(r, f"Row uses 1–6 once: {' '.join(row)}. What is ?", str(nums[m]), [str(n) for n in nums if n != nums[m]][:3]))
    return ("Sudoku 6×6", "Each row has every number once.", rounds)
def t02(r):
    qs = [("repeat 3 [move 2] moves the robot…", "6 steps", ["3 steps", "5 steps"]), ("A function is…", "A named set of steps you can reuse", ["A random number", "A bug"]),
          ("repeat 4 [turn right 90°] makes the robot face…", "The same way", ["Backwards", "Left"]), ("Loop 5 times: score + 2. Score starts at 0. Ends at…", "10", ["7", "5"]),
          ("Which is a loop?", "repeat 10 times", ["if raining", "x = 5"])]
    return ("Loops and functions", "Loops repeat. Functions name a group of steps.", [pick(r, q, a, w) for q, a, w in qs])
def t03(r):
    ps = [("The jewel was stolen at noon. The cook was baking, the gardener was at the market, the butler has no alibi. Who is the suspect?", "The butler", ["The cook", "The gardener"]),
          ("Muddy boots size 9 at the scene. Ana wears 6, Ben 9, Cy 11. Suspect?", "Ben", ["Ana", "Cy"]), ("The thief is left-handed and wears glasses. Only Dee is both. Suspect?", "Dee", ["Eli", "Fay"]),
          ("Clue: the window was locked from inside. So the thief…", "Used the door", ["Flew in", "Used the window"]), ("Two say 'it wasn't me'. One lies. Only Kim was in the room. Who?", "Kim", ["Lou", "Max"])]
    return ("Logic grid: mystery", "Rule out suspects with each clue.", [pick(r, q, a, w) for q, a, w in ps])
def t04(r):
    rounds = []
    for _ in range(N):
        word = r.choice(["PLANET", "ROBOT", "CASTLE", "GALAXY", "DRAGON", "PUZZLE", "FOREST"])
        k = r.randint(1, 4)
        code = "".join(chr((ord(c) - 65 + k) % 26 + 65) for c in word)
        rounds.append(pick(r, f"Shift each letter back {k}: {code}", word, [w for w in ["PLANET", "ROBOT", "CASTLE", "GALAXY", "DRAGON", "PUZZLE", "FOREST"] if w != word][:2]))
    return ("Cryptogram", "Undo the shift one letter at a time.", rounds)
def t05(r):
    qs = [("A row clue '3' on a 5-wide grid means…", "3 filled squares in a row together", ["3 empty squares", "3 rows"]), ("Clue '5' on a 5-wide row means…", "The whole row is filled", ["Nothing is filled", "Half is filled"]),
          ("Clue '1 1' means…", "Two single squares with a gap", ["One block of two", "Nothing"]), ("Clue '0' means…", "The row is empty", ["Full row", "One square"]),
          ("Nonograms reveal a…", "Hidden picture", ["Secret word", "Number"])]
    return ("Nonogram", "Numbers tell you how many squares to fill in a row.", [pick(r, q, a, w) for q, a, w in qs])
def t06(r):
    qs = [("Which piece moves in an L shape?", "Knight", ["Bishop", "Rook"]), ("Which piece moves diagonally only?", "Bishop", ["Rook", "King"]), ("Checkmate means the king…", "Can't escape capture", ["Is safe", "Won"]),
          ("Which is the most powerful piece?", "Queen", ["Pawn", "Knight"]), ("A pawn reaching the end can become…", "A queen", ["A king", "Nothing"])]
    return ("Chess puzzles", "Think one move ahead.", [pick(r, q, a, w) for q, a, w in qs])
def t07(r):
    return ("Tower of Hanoi: 5 rings", "Minimum moves = 2ⁿ − 1.", [pick(r, "Fewest moves for 3 rings?", "7", ["5", "9"]), pick(r, "Fewest moves for 4 rings?", "15", ["12", "16"]), pick(r, "Fewest moves for 5 rings?", "31", ["25", "32"]),
            build(r, "Order the strategy.", ["Move top 4 to spare peg", "Move the big ring", "Move the 4 back on top"]), pick(r, "Can a big ring ever go on a small one?", "Never", ["Sometimes", "Always"])])
def t08(r):
    rounds = []
    for _ in range(N):
        nums = r.sample(range(1, 50), 5)
        rounds.append(build(r, "Sort smallest to largest, like a sorting algorithm.", [str(n) for n in sorted(nums)]))
    return ("Sorting algorithms", "Compare two at a time and swap.", rounds)
def t09(r):
    qs = [("A spinner has 4 equal parts, 1 red. Chance of red?", "1 in 4", ["1 in 2", "3 in 4"]), ("A coin flip: chance of heads?", "1 in 2", ["1 in 4", "Certain"]),
          ("A dice: chance of rolling a 6?", "1 in 6", ["1 in 3", "1 in 2"]), ("A bag: 3 blue, 1 red. Most likely?", "Blue", ["Red", "Equal"]),
          ("Chance of rolling 7 on a normal dice?", "Impossible", ["Likely", "Certain"])]
    return ("Probability spinner", "Chance = wanted outcomes ÷ all outcomes.", [pick(r, q, a, w) for q, a, w in qs])
def t10(r):
    rid = [("A man pushes his car to a hotel and loses his money. Why?", "He's playing Monopoly", ["He was robbed", "The car broke"]), ("What can you catch but not throw?", "A cold", ["A ball", "A fish"]),
           ("The more you take, the more you leave behind. What are they?", "Footsteps", ["Cookies", "Photos"]), ("What has cities but no houses, rivers but no water?", "A map", ["A desert", "A dream"]),
           ("What breaks when you say its name?", "Silence", ["Glass", "A promise"])]
    return ("Lateral thinking riddles", "Question your first assumption.", [pick(r, q, a, w) for q, a, w in rid])
def t11(r):
    b = [("0001", "1"), ("0010", "2"), ("0011", "3"), ("0100", "4"), ("0101", "5"), ("1000", "8"), ("1010", "10"), ("1111", "15")]
    return ("Binary numbers", "Each place doubles: 8, 4, 2, 1.", [match(r.sample(b, 3)) for _ in range(N)])
def t12(r):
    return ("Escape room", "Use every clue in the room.", [
        choice("The lock needs 3 digits. A clock shows 4:15 and a calendar shows the 7th.", [("Try 4-1-5 first", True, "The clock is the clearest clue."), ("Try 9-9-9", False, "Use the clues.")]),
        choice("A note says 'look up'. You…", [("Check the ceiling", True, "Follow the clue literally."), ("Look under the rug", False, "It said up.")]),
        choice("Four coloured buttons: red, blue, red, green on a poster.", [("Press them in that order", True, "Patterns in the room are clues."), ("Press all at once", False, "Order matters.")]),
        choice("The key is behind glass that says 'break in emergency'.", [("Find another way first", True, "Safety and logic first."), ("Smash it immediately", False, "Look for clues first.")]),
        choice("Your team is stuck for 5 minutes.", [("Share what each person found", True, "Teamwork combines clues."), ("Everyone searches the same spot", False, "Split up!")]),
    ])
def t13(r):
    qs = [("A cube has how many faces?", "6", ["4", "8"]), ("A net of 6 squares in a cross folds into a…", "Cube", ["Pyramid", "Cylinder"]), ("A square pyramid has how many faces?", "5", ["4", "6"]),
          ("A cylinder net has 2 circles and a…", "Rectangle", ["Triangle", "Star"]), ("A triangular prism has how many faces?", "5", ["6", "3"])]
    return ("Fold the 3D net", "Imagine folding the paper up.", [pick(r, q, a, w) for q, a, w in qs])
def t14(r):
    return ("Truth-teller puzzles", "Knights always tell the truth, knaves always lie.", [
        choice("A says 'I am a knave.' Could A be a knight?", [("No, and A can't be a knave either", True, "A knight wouldn't say it; a knave couldn't truthfully. It's impossible."), ("Yes", False, "A knight would be lying.")]),
        choice("A says 'B is a knight.' A is a knight. B is…", [("A knight", True, "Knights tell the truth."), ("A knave", False, "A is truthful.")]),
        choice("A knave says 'It is raining.' Is it raining?", [("No", True, "Knaves lie."), ("Yes", False, "A knave's words are false.")]),
        choice("A says 'We are both knaves.' What is A?", [("A knave", True, "A knight couldn't say it, so A lies; B is a knight."), ("A knight", False, "That would be a lie.")]),
        choice("Two doors, one guard who always lies. You ask 'Which door is safe?' He points left. You choose…", [("Right", True, "He lies, so the other door."), ("Left", False, "He always lies.")]),
    ])
def t15(r):
    routes = [["Home", "Park", "Library", "School"], ["Start", "Bridge", "Forest", "Castle"], ["Station", "Market", "Museum", "Hotel"], ["Base", "Lake", "Hill", "Summit"], ["Dock", "Island", "Reef", "Lighthouse"]]
    return ("Find the fastest route", "The shortest path avoids backtracking.", [build(r, "Order the stops on the shortest route.", ro) for ro in routes])
def t16(r):
    rounds = []
    for _ in range(N):
        a, m = r.randint(1, 4), r.choice([2, 3])
        rounds.append(pattern(r, [str(a * m ** i) for i in range(3)], str(a * m ** 3), [str(a * m ** 3 + m), str(a * m ** 2 + m)], "Multiplying pattern: what's next?"))
    return ("Pattern rule finder", "Is it adding or multiplying?", rounds)
def t17(r):
    qs = [("AND gate: both inputs ON. Output?", "ON", ["OFF"]), ("AND gate: one input OFF. Output?", "OFF", ["ON"]), ("OR gate: one input ON. Output?", "ON", ["OFF"]),
          ("NOT gate: input ON. Output?", "OFF", ["ON"]), ("OR gate: both OFF. Output?", "OFF", ["ON"])]
    return ("Logic gates", "AND needs both, OR needs one, NOT flips it.", [pick(r, q, a, w) for q, a, w in qs])
def t18(r):
    return ("Strategy: Nim", "Take 1–3 sticks a turn; whoever takes the last stick wins. Leave your opponent a multiple of 4.", [
        choice("21 sticks. You go first. How many do you take?", [("1, leaving 20", True, "20 is a multiple of 4, so you're in control."), ("3, leaving 18", False, "Aim to leave a multiple of 4.")]),
        choice("Your opponent takes 2 and leaves 18. You take…", [("2, leaving 16", True, "Back to a multiple of 4."), ("1, leaving 17", False, "17 isn't a multiple of 4.")]),
        choice("It's their turn with 12 sticks left. Who is winning?", [("You", True, "Whatever they take, you can make it 8."), ("Them", False, "A multiple of 4 on their turn is bad for them.")]),
        choice("5 sticks left on your turn. You take…", [("1, leaving 4", True, "Now they can't stop you taking the last one."), ("3, leaving 2", False, "Then they take both and win.")]),
        choice("The big idea of Nim strategy is…", [("Control the number your opponent faces", True, "Think backwards from the end."), ("Always take the most sticks", False, "Greedy moves often lose.")]),
    ])
def t19(r):
    rounds = []
    for _ in range(N):
        secret = r.sample("1234567", 3); guess = r.sample("1234567", 3)
        right = sum(a == b for a, b in zip(secret, guess))
        rounds.append(pick(r, f"Secret code {''.join(secret)}. Guess {''.join(guess)}. How many digits are in the right place?", str(right), [str(x) for x in range(4) if x != right][:2]))
    return ("Codebreaker", "Compare each position carefully.", rounds)
def t20(r):
    return ("Design a game level", "Good levels teach, then test.", [
        choice("The first level should…", [("Teach one simple move", True, "Easy start builds confidence."), ("Be the hardest", False, "Players quit.")]),
        choice("A player keeps falling at the same gap. You…", [("Add a hint or make the gap smaller", True, "Fair difficulty."), ("Make it bigger", False, "That frustrates players.")]),
        choice("Where should the checkpoint go?", [("Before a hard section", True, "Less repeating."), ("At the very start only", False, "Players lose too much progress.")]),
        build(r, "Order the level design steps.", ["Sketch the map", "Build a prototype", "Playtest", "Improve"]),
        choice("Rewards work best when…", [("They come after effort", True, "Earned rewards feel good."), ("They're random always", False, "Players feel lost.")]),
    ])

GEN = {
    "cubs": [c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20],
    "explorers": [e01, e02, e03, e04, e05, e06, e07, e08, e09, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20],
    "trailblazers": [t01, t02, t03, t04, t05, t06, t07, t08, t09, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20],
}
