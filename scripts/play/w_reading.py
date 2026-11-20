"""Reading Forest: 20 activities per band."""
from common import *

N = 5
WORDS = {  # first-sound words for little ones
    "a": ["apple", "ant", "alligator"], "b": ["ball", "bear", "bus"], "c": ["cat", "car", "cake"], "d": ["dog", "duck", "drum"],
    "e": ["egg", "elephant", "elf"], "f": ["fish", "fox", "frog"], "g": ["goat", "gift", "guitar"], "h": ["hat", "house", "horse"],
    "i": ["igloo", "insect", "itch"], "j": ["jam", "jelly", "jet"], "k": ["kite", "king", "key"], "l": ["lion", "leaf", "lemon"],
    "m": ["moon", "mouse", "milk"], "n": ["nest", "nose", "nut"], "o": ["octopus", "otter", "orange"], "p": ["pig", "pen", "pizza"],
    "r": ["rabbit", "rocket", "rain"], "s": ["sun", "sock", "snake"], "t": ["tiger", "tree", "toy"], "w": ["whale", "web", "wagon"],
}
RHYMES = [("cat", "hat"), ("dog", "frog"), ("bee", "tree"), ("star", "car"), ("moon", "spoon"), ("cake", "lake"), ("bear", "chair"),
          ("fish", "dish"), ("sock", "rock"), ("mouse", "house"), ("king", "ring"), ("bug", "rug"), ("sun", "bun"), ("goat", "boat")]
SIGHT = ["the", "and", "is", "you", "to", "said", "was", "they", "have", "my", "are", "we", "said", "come", "here", "look", "play", "what"]


def _sounds(r, letters, rounds=N):
    out = []
    for L in r.sample(letters, rounds):
        right = L.upper()
        wrong = [x.upper() for x in r.sample([x for x in WORDS if x != L], 2)]
        w = r.choice(WORDS[L])
        out.append(sound(r, f"{w}. {w} starts with…", right, wrong, f"Which letter does “{w}” start with?"))
    return out

# ---------------- Little Cubs ----------------
def c01(r): return ("Letter sounds A to E", "Say the word slowly and listen to the very first sound.", _sounds(r, list("abcde")))
def c02(r): return ("Find the letter M!", "M has two mountains.", [pop(r, "M", list("NWHAVK"), g, 9) for g in [3, 4, 3, 5, 3]])
def c03(r): return ("Trace a big A.", "Up, down, then across the middle.", [trace("A", glyph("A")) for _ in range(3)] + [trace("A", [(x * 0.9 + 5, y) for x, y in glyph("A")]), trace("A", [(x, y * 0.9 + 5) for x, y in glyph("A")])])
def c04(r):
    rounds = []
    for _ in range(N):
        rounds.append(match(r.sample(RHYMES, 3)))
    return ("Rhyme time: cat and hat", "Rhyming words sound the same at the end.", rounds)
def c05(r):
    rounds = []
    for L in r.sample(list(WORDS), N):
        w = WORDS[L][0]
        rounds.append(sound(r, f"{w}", L.upper(), [x.upper() for x in r.sample([x for x in WORDS if x != L], 2)], f"What is the first sound in “{w}”?"))
    return ("First sound: ball", "Make the mouth shape for the first sound.", rounds)
def c06(r):
    rounds = []
    for _ in range(N):
        ls = r.sample("abdefghmnrst", 3)
        rounds.append(match([(l.upper(), l) for l in ls]))
    return ("Match big and little letters", "Big B and little b are the same letter.", rounds)
def c07(r):
    words = ["CAT", "DOG", "SUN", "BUS", "HAT", "PIG", "BED", "MOP", "CUP", "FOX"]
    return ("Build the word, sound by sound.", "Say each sound, then blend them together.", [build(r, f"Build the word {w}.", list(w)) for w in r.sample(words, N)])
def c08(r):
    stories = [("Plant a seed", ["Dig a hole", "Plant the seed", "Water it", "It grows"]), ("Make a sandwich", ["Get bread", "Add jam", "Close it", "Eat it"]),
               ("Bedtime", ["Bath time", "Pyjamas on", "Read a story", "Sleep"]), ("Build a snowman", ["Roll a big ball", "Add a middle", "Add a head", "Put on a hat"]),
               ("A rainy day", ["Clouds come", "It rains", "Puddles", "A rainbow"]), ("Morning", ["Wake up", "Breakfast", "Brush teeth", "Go to school"])]
    return ("Put the story in order.", "What happens first? What happens last?", [build(r, f"{t}: tap the steps in order.", s[:3 + (i % 2)]) for i, (t, s) in enumerate(r.sample(stories, N))])
def c09(r):
    qs = [("Which animal says “moo”?", "Cow", ["Cat", "Duck"]), ("Which animal has a long trunk?", "Elephant", ["Tiger", "Rabbit"]),
          ("Which animal can fly?", "Bird", ["Fish", "Dog"]), ("Which animal hops?", "Kangaroo", ["Snake", "Fish"]),
          ("Which animal has black and white stripes?", "Zebra", ["Lion", "Pig"]), ("Which animal lives in water?", "Fish", ["Horse", "Cat"]),
          ("Which animal says “quack”?", "Duck", ["Cow", "Sheep"])]
    return ("Name the animal", "Picture the animal in your head.", [pick(r, q, a, w) for q, a, w in r.sample(qs, N)])
def c10(r):
    ws = [("cat", 1), ("apple", 2), ("banana", 3), ("dinosaur", 4), ("elephant", 3), ("rocket", 2), ("sun", 1), ("butterfly", 3), ("caterpillar", 5)]
    return ("Clap the syllables", "Clap once for each beat in the word.", [pick(r, f"How many claps in “{w}”?", str(n), [str(x) for x in range(1, 6) if x != n][:2]) for w, n in r.sample(ws, N)])
def c11(r): return ("Trace a little a.", "Round like a ball, then a little line down.", [trace("a", glyph("a")) for _ in range(2)] + [trace("a", [(x * 0.85 + 8, y) for x, y in glyph("a")]) for _ in range(2)])
def c12(r): return ("Letter sounds F to J", "Listen to the first sound.", _sounds(r, list("fghij")))
def c13(r):
    rounds = []
    for a, b in r.sample(RHYMES, N):
        wrong = r.sample([x for x, _ in RHYMES if x not in (a, b)], 2)
        rounds.append(pick(r, f"Which word rhymes with “{a}”?", b, wrong))
    return ("Find the rhyme", "Rhymes end with the same sound.", rounds)
def c14(r):
    pairs = [("@apple:red", "apple"), ("@fish:blue", "fish"), ("@sun:yellow", "sun"), ("@car:red", "car"), ("@cat:orange", "cat"), ("@tree:green", "tree"),
             ("@duck:yellow", "duck"), ("@star:yellow", "star"), ("@house:brown", "house"), ("@moon:yellow", "moon")]
    return ("Picture words", "Say the picture's name, then find the word.", [match(r.sample(pairs, 3)) for _ in range(N)])
def c15(r): return ("Sight word: the", "“the” has a t, an h and an e.", [pop(r, "the", ["he", "then", "tea", "she", "to"], g, 9) for g in [3, 4, 3, 4, 5]])
def c16(r):
    rounds = []
    for _ in range(N):
        a, b = r.sample(list(WORDS), 2)
        items = [(w, 0) for w in r.sample(WORDS[a], 2)] + [(w, 1) for w in r.sample(WORDS[b], 2)]
        rounds.append(sort([a.upper(), b.upper()], shuffled(r, items)))
    return ("Sort by beginning sound", "Listen to the first sound of each word.", rounds)
def c17(r):
    qs = [("“I am yellow and shine in the sky.” What am I?", "The sun", ["A fish", "A shoe"]), ("“You wear me on your feet.” What am I?", "Shoes", ["A hat", "A cup"]),
          ("“I say woof!” Who am I?", "A dog", ["A cat", "A cow"]), ("“You sleep in me at night.” What am I?", "A bed", ["A car", "A tree"]),
          ("“I am cold and you build me in winter.” What am I?", "A snowman", ["A cake", "A kite"]), ("“I have pages and words.” What am I?", "A book", ["A ball", "A sock"])]
    return ("Listen and pick", "Listen to all the clues before you choose.", [pick(r, q, a, w) for q, a, w in r.sample(qs, N)])
def c18(r):
    ops = [("hot", "cold"), ("big", "small"), ("up", "down"), ("day", "night"), ("happy", "sad"), ("fast", "slow"), ("open", "closed"), ("wet", "dry"), ("loud", "quiet")]
    return ("Opposites match", "Opposites are as different as can be.", [match(r.sample(ops, 3)) for _ in range(N)])
def c19(r): return ("Letter sounds K to O", "Listen to the first sound.", _sounds(r, list("klmno")))
def c20(r):
    return ("Trace the letters of a name.", "Start at dot 1 each time.",
            [trace(L, glyph(L)) for L in r.sample(list("ABCDEHJKLMNOPRSTW"), N)])

# ---------------- Explorers ----------------
def e01(r):
    words = ["CAT", "MAP", "PEN", "SIT", "HOP", "RUG", "JAM", "TOP", "WIG", "NET", "BUG", "FAN"]
    return ("Blend 3-letter words", "Slide the sounds together: c-a-t, cat!", [build(r, f"Build “{w.lower()}”.", list(w)) for w in r.sample(words, N)])
def e02(r):
    rounds = []
    for w in r.sample(SIGHT, N):
        decoys = r.sample([s for s in SIGHT if s != w], 5)
        rounds.append(pop(r, w, decoys, 3, 9) | {"q": f"Pop the word “{w}”!"})
    return ("Sight word pop", "These words show up everywhere. Learn them by heart.", rounds)
def e03(r):
    vowels = {"a": ["cat", "map", "bag", "hat", "jam"], "e": ["pen", "bed", "net", "leg", "hen"], "i": ["pig", "sit", "fin", "lid", "wig"],
              "o": ["dog", "hop", "pot", "fox", "log"], "u": ["sun", "bug", "cup", "rug", "nut"]}
    rounds = []
    for _ in range(N):
        a, b = r.sample(list(vowels), 2)
        rounds.append(sort([f"short {a}", f"short {b}"], shuffled(r, [(w, 0) for w in r.sample(vowels[a], 3)] + [(w, 1) for w in r.sample(vowels[b], 3)])))
    return ("Short vowel sort", "Listen to the middle sound.", rounds)
def e04(r):
    qs = [("“The fish swims in the bowl.” Which picture fits?", "@fish:orange", ["@dog:brown", "@car:red"]), ("“The red car is fast.” Which picture fits?", "@car:red", ["@car:blue", "@bus" if False else "@ball:red"]),
          ("“A yellow duck sits on the pond.” Which picture fits?", "@duck:yellow", ["@duck:brown", "@fish:yellow"]), ("“The moon is out at night.” Which picture fits?", "@moon:yellow", ["@sun:yellow", "@cloud:blue"]),
          ("“A green tree grows tall.” Which picture fits?", "@tree:green", ["@flower:pink", "@leaf:orange"]), ("“The cat naps on a blue mat.” Which picture fits?", "@cat:orange", ["@dog:brown", "@fish:blue"])]
    return ("Read and choose the picture", "Read every word, then look for the match.", [pick(r, q, a, w) for q, a, w in r.sample(qs, N)])
def e05(r):
    ss = [["The", "dog", "runs", "fast."], ["I", "like", "red", "apples."], ["We", "play", "in", "the", "park."], ["The", "sun", "is", "hot."],
          ["My", "cat", "can", "jump."], ["She", "reads", "a", "book."], ["He", "rides", "his", "bike."]]
    return ("Sentence builder", "A sentence starts with a capital and ends with a full stop.", [build(r, "Put the words in order.", s) for s in r.sample(ss, N)])
def e06(r):
    d = {"sh": ["ship", "shell", "fish", "shoe"], "ch": ["chip", "chair", "lunch", "cheese"], "th": ["thumb", "bath", "three", "moth"]}
    rounds = []
    for _ in range(N):
        k = r.choice(list(d)); w = r.choice(d[k])
        rounds.append(sound(r, w, k, [x for x in d if x != k], f"Which sound is in “{w}”?"))
    return ("Digraphs sh, ch, th", "Two letters can make one sound.", rounds)
def e07(r):
    pairs = [("cap", "cape"), ("kit", "kite"), ("hop", "hope"), ("tub", "tube"), ("pin", "pine"), ("can", "cane"), ("not", "note"), ("cub", "cube")]
    rounds = []
    for a, b in r.sample(pairs, N):
        rounds.append(sound(r, b, b, [a, b[:-1] + "a"], f"Add a magic e! Which word do you hear?"))
    return ("Magic e words", "Magic e makes the vowel say its name.", rounds)
def e08(r):
    passages = [("Ben lost his red hat. He looked under the bed and found it.", "Where was the hat?", "Under the bed", ["In the car", "On the roof"]),
                ("Sara planted a seed. She watered it every day. Soon a sunflower grew.", "What grew?", "A sunflower", ["A tree", "A carrot"]),
                ("The puppy was muddy, so Dad gave him a bath.", "Why did the puppy get a bath?", "He was muddy", ["He was hungry", "It was his birthday"]),
                ("Lily packed a sandwich, an apple and juice for the picnic.", "What fruit did Lily pack?", "An apple", ["A banana", "Grapes"]),
                ("It was snowing, so Max wore his warm coat and boots.", "Why did Max wear a coat?", "It was snowing", ["It was sunny", "He was going swimming"]),
                ("The owl sleeps all day and hunts at night.", "When does the owl hunt?", "At night", ["In the morning", "At lunch"])]
    return ("Story questions", "Look back at the story to check.", [pick(r, f"{p} {q}", a, w) for p, q, a, w in r.sample(passages, N)])
def e09(r):
    ps = [("one cat", "two cats", ["two cat", "two cates"]), ("one box", "two boxes", ["two boxs", "two box"]), ("one baby", "two babies", ["two babys", "two baby"]),
          ("one bus", "two buses", ["two buss", "two bus"]), ("one fox", "two foxes", ["two foxs", "two fox"]), ("one mouse", "two mice", ["two mouses", "two mouse"])]
    return ("Plural detective", "Most words add s. Words ending in x or s add es.", [pick(r, f"{a} → ?", b, w) for a, b, w in r.sample(ps, N)])
def e10(r):
    cs = [("sun", "flower"), ("rain", "bow"), ("foot", "ball"), ("cup", "cake"), ("star", "fish"), ("butter", "fly"), ("snow", "man"), ("tooth", "brush"), ("pan", "cake")]
    return ("Compound words", "Two small words join to make a new word.", [match(uniq_pairs(r, cs, 3)) for _ in range(N)])
def e11(r):
    ws = ["FROG", "DUCK", "CAKE", "MILK", "SHIP", "TREE", "BEAR", "STAR", "FISH", "BOAT"]
    return ("Spelling bee", "Say the word slowly and write each sound.", [build(r, f"Spell “{w.lower()}”.", list(w)) for w in r.sample(ws, N)])
def e12(r):
    qs = [("Which ends a question?", "?", [".", "!"]), ("“What a big dog” needs which mark?", "!", [".", "?"]), ("“I like pizza” needs which mark?", ".", ["?", "!"]),
          ("“Where is my shoe” needs which mark?", "?", [".", ","]), ("A sentence starts with a…", "capital letter", ["small letter", "number"]), ("“Help” shouted Sam. Which mark goes after Help?", "!", ["?", "."])]
    return ("Punctuation stop", "Questions ask. Exclamations shout. Statements tell.", [pick(r, q, a, w) for q, a, w in r.sample(qs, N)])
def e13(r):
    verbs = ["run", "jump", "eat", "swim", "read", "sing", "climb", "draw"]
    nouns = ["dog", "ball", "tree", "book", "car", "apple", "house", "moon"]
    return ("Verb or noun?", "A verb is an action. A noun is a thing.", [sort(["Verb", "Noun"], shuffled(r, [(v, 0) for v in r.sample(verbs, 3)] + [(n, 1) for n in r.sample(nouns, 3)])) for _ in range(N)])
def e14(r):
    ch = [("Tom found a tiny dragon egg in the garden. It was warm.", "What did Tom find?", "A dragon egg", ["A rock", "A ball"]),
          ("The egg cracked. Out came a dragon no bigger than a cat.", "How big was the dragon?", "As big as a cat", ["As big as a house", "As big as an ant"]),
          ("Tom named the dragon Ember because it sneezed sparks.", "Why was it called Ember?", "It sneezed sparks", ["It was blue", "It liked water"]),
          ("Ember loved toast, so Tom made a stack every morning.", "What did Ember eat?", "Toast", ["Fish", "Ice cream"]),
          ("One day Ember flew Tom over the hills to the sea.", "Where did they fly?", "To the sea", ["To school", "To the moon"]),
          ("At sunset they flew home, and Ember curled up by the fire.", "Where did Ember sleep?", "By the fire", ["In a tree", "In the sea"])]
    return ("Read-along chapter: Tom and Ember", "Read each part, then answer.", [pick(r, f"{p} {q}", a, w) for p, q, a, w in ch[:N]])
def e15(r):
    syn = [("big", "large"), ("happy", "glad"), ("small", "tiny"), ("fast", "quick"), ("start", "begin"), ("shout", "yell"), ("pretty", "lovely"), ("scared", "afraid"), ("cold", "chilly")]
    return ("Synonym match", "Synonyms mean the same thing.", [match(r.sample(syn, 3)) for _ in range(N)])
def e16(r):
    qs = [("Which is correct?", "She has two cats.", ["She have two cats.", "She has two cat."]), ("Which is correct?", "We are going home.", ["We is going home.", "We am going home."]),
          ("Which is correct?", "I ate an apple.", ["I ate a apple.", "I eated an apple."]), ("Which is correct?", "They were happy.", ["They was happy.", "They is happy."]),
          ("Which is correct?", "He ran to the park.", ["He runned to the park.", "He run to the park yesterday."]), ("Which is correct?", "The dogs bark.", ["The dogs barks.", "The dog bark."])]
    return ("Fix the sentence", "Read it out loud. Does it sound right?", [pick(r, q, a, w) for q, a, w in r.sample(qs, N)])
def e17(r):
    ps = [("Bees fly from flower to flower. They collect nectar. They make honey in the hive.", "How bees make honey", ["How flowers grow", "Why the sky is blue"]),
          ("Penguins live in cold places. They can't fly but they swim very fast.", "Penguins and how they live", ["Birds that fly", "Hot deserts"]),
          ("First, mix flour and eggs. Then bake for 20 minutes. Let it cool and add icing.", "How to bake a cake", ["How to plant a tree", "How to wash a dog"]),
          ("Trains carry people and goods. Some are very fast. Some run under cities.", "Trains", ["Boats", "Planes"]),
          ("Kittens sleep a lot. They also love to play with string and chase toys.", "What kittens do", ["What puppies eat", "How fish breathe"])]
    return ("What's the main idea?", "What is the whole text mostly about?", [pick(r, p + " What is this mostly about?", a, w) for p, a, w in r.sample(ps, N)])
def e18(r):
    rows = [("I see a goat in a ___.", "boat", ["car", "tree"]), ("The cat sat on a ___.", "mat", ["bed", "chair"]), ("The bee is in the ___.", "tree", ["box", "car"]),
            ("A mouse lives in my ___.", "house", ["shoe", "bag"]), ("I saw a frog sit on a ___.", "log", ["rock", "leaf"]), ("A star shines on my ___.", "car", ["bed", "cup"])]
    return ("Rhyming poem", "The missing word rhymes with the end of the line.", [sound(r, s.replace("___", a), a, w, s) for s, a, w in r.sample(rows, N)])
def e19(r):
    sets = [["apple", "banana", "cherry"], ["dog", "fish", "goat"], ["moon", "nest", "owl"], ["rain", "sun", "tree"], ["cat", "dog", "egg"], ["kite", "lamp", "milk"], ["bear", "lion", "zebra"]]
    return ("Alphabet order", "Look at the first letter: which comes first in the ABC?", [build(r, "Put these words in ABC order.", s) for s in r.sample(sets, N)])
def e20(r):
    fams = {"at": ["c", "h", "b", "m"], "an": ["c", "f", "p", "v"], "ig": ["p", "w", "d", "b"], "op": ["h", "m", "t", "p"]}
    rounds = []
    for _ in range(N):
        f = r.choice(list(fams)); first = r.choice(fams[f])
        rounds.append(build(r, f"Build “{first}{f}”.", [first.upper()] + list(f.upper())))
    return ("Word families -at, -an", "Change the first letter to make a new word.", rounds)

# ---------------- Trailblazers ----------------
def t01(r):
    ps = [("un + happy", "unhappy"), ("re + play", "replay"), ("help + ful", "helpful"), ("care + less", "careless"), ("pre + view", "preview"),
          ("kind + ness", "kindness"), ("dis + agree", "disagree"), ("quick + ly", "quickly")]
    return ("Prefix and suffix lab", "A prefix goes in front, a suffix goes at the end.", [match(r.sample(ps, 3)) for _ in range(N)])
def t02(r):
    qs = [("The desert was arid; nothing grew for miles. Arid means…", "very dry", ["very cold", "very loud"]), ("She was elated when she won, jumping for joy. Elated means…", "very happy", ["very tired", "angry"]),
          ("The cave was so murky we couldn't see our hands. Murky means…", "dark and unclear", ["bright", "tiny"]), ("He was famished after skipping lunch. Famished means…", "very hungry", ["sleepy", "bored"]),
          ("The fragile vase broke when it was touched. Fragile means…", "easily broken", ["heavy", "shiny"]), ("They were reluctant to swim in the icy lake. Reluctant means…", "not wanting to", ["excited", "fast"])]
    return ("Context clues", "Use the rest of the sentence to work out the word.", [pick(r, q, a, w) for q, a, w in r.sample(qs, N)])
def t03(r):
    facts = ["Water freezes at 0°C.", "The Moon orbits the Earth.", "Spiders have eight legs.", "Paris is in France.", "A week has seven days.", "Plants need sunlight."]
    ops = ["Pizza is the best food.", "Winter is boring.", "Cats are cuter than dogs.", "Maths is the most fun subject.", "Blue is the nicest colour.", "Football is better than tennis."]
    return ("Fact or opinion?", "A fact can be checked. An opinion is what someone thinks.", [sort(["Fact", "Opinion"], shuffled(r, [(f, 0) for f in r.sample(facts, 3)] + [(o, 1) for o in r.sample(ops, 3)])) for _ in range(N)])
def t04(r):
    qs = [("Maya's hands shook as she walked on stage.", "How does Maya feel?", "Nervous", ["Bored", "Sleepy"]), ("Leo slammed the door and stomped upstairs.", "How does Leo feel?", "Angry", ["Calm", "Proud"]),
          ("Ava hugged the letter and couldn't stop smiling.", "How does Ava feel?", "Joyful", ["Scared", "Lonely"]), ("Sam stared out the window as his friends played without him.", "How does Sam feel?", "Left out", ["Excited", "Hungry"]),
          ("Zara held up her trophy for everyone to see.", "How does Zara feel?", "Proud", ["Embarrassed", "Worried"]), ("Noah kept checking the clock before the test.", "How does Noah feel?", "Anxious", ["Relaxed", "Thrilled"])]
    return ("Character feelings", "Actions and body language are clues to feelings.", [choice(f"{s} {q}", [(a, True, "Yes. The clues point to that feeling."), (w[0], False, "Look at the action again."), (w[1], False, "Look at the action again.")]) for s, q, a, w in r.sample(qs, N)])
def t05(r):
    ss = [["The", "enormous", "whale", "leaped", "from", "the", "waves."], ["Suddenly,", "the", "lights", "flickered", "and", "went", "out."],
          ["Carefully,", "she", "opened", "the", "ancient", "map."], ["The", "brave", "knight", "rode", "into", "the", "dark", "forest."],
          ["After", "the", "storm,", "a", "rainbow", "filled", "the", "sky."]]
    return ("Write a better sentence", "Strong verbs and adjectives make writing exciting.", [build(r, "Order the words into a vivid sentence.", s) for s in ss])
def t06(r):
    fl = [("as brave as a lion", "simile"), ("the wind whispered", "personification"), ("time is money", "metaphor"), ("buzz", "onomatopoeia"),
          ("I've told you a million times", "hyperbole"), ("as busy as a bee", "simile"), ("the classroom was a zoo", "metaphor"), ("the stars danced", "personification")]
    rounds = []
    for _ in range(N):
        three = []
        used = set()
        for p, k in r.sample(fl, len(fl)):
            if k not in used:
                three.append((p, k)); used.add(k)
            if len(three) == 3:
                break
        rounds.append(match(three))
    return ("Figurative language", "A simile uses like or as. A metaphor says something IS something else.", rounds)
def t07(r):
    ps = [("Kai wanted a new bike, so he walked dogs every weekend for months. Finally he had enough money and bought a blue bike.", "Kai saved up by walking dogs and bought a bike.", ["Kai likes the colour blue.", "Kai has a dog."]),
          ("A storm knocked out the town's power. Neighbours shared candles and food until the lights came back two days later.", "Neighbours helped each other during a power cut.", ["Storms are loud.", "Candles are bright."]),
          ("Rosa practised the piano every day. At first she made mistakes, but by spring she played perfectly at the concert.", "Rosa's practice helped her play well at the concert.", ["Rosa likes spring.", "Pianos have keys."]),
          ("The team was losing at half time. They changed their plan, worked together, and won in the last minute.", "The team changed plans and came back to win.", ["The game was long.", "Half time is a break."]),
          ("Explorers crossed the ice for weeks, short on food, until they reached the coast and a waiting ship.", "Explorers survived a hard trip to reach safety.", ["Ships are big.", "Ice is cold."])]
    return ("Summarize the chapter", "A summary tells the most important events briefly.", [pick(r, p + " Best summary?", a, w) for p, a, w in ps])
def t08(r):
    qs = [("The dog wagged ___ tail.", "its", ["it's"]), ("___ going to the park.", "They're", ["Their", "There"]), ("Put the box over ___.", "there", ["their", "they're"]),
          ("I want ___ apples.", "two", ["to", "too"]), ("She ___ the race.", "won", ["one"]), ("The wind ___ hard.", "blew", ["blue"])]
    return ("Homophone hunt", "Homophones sound the same but mean different things.", [pick(r, q, a, w) for q, a, w in r.sample(qs, N)])
def t09(r):
    maps = [["Setting", "Problem", "Rising action", "Climax", "Resolution"], ["Meet the hero", "A challenge appears", "The hero tries and fails", "The big moment", "Home again"],
            ["Beginning", "Middle", "End"], ["Introduce characters", "Conflict starts", "Things get worse", "Turning point", "Ending"]]
    return ("Story map", "Every story has a beginning, middle and end.", [build(r, "Put the parts of a story in order.", m) for m in maps] + [build(r, "Order the plot points.", ["Wolf meets Red", "Wolf runs to Grandma's", "Red finds the wolf", "The woodcutter saves them"])])
def t10(r):
    ce = [("It rained all night", "The streets were wet"), ("She forgot her coat", "She was cold"), ("He studied hard", "He passed the test"),
          ("The ice melted", "The river rose"), ("The alarm didn't ring", "They were late"), ("The plant got no water", "It wilted")]
    return ("Cause and effect", "The cause makes the effect happen.", [match(r.sample(ce, 3)) for _ in range(N)])
def t11(r): return ("Poetry rhythm", "Tap the stressed beats: da-DUM da-DUM.", [rhythm(r, 3, 4 + i) for i in range(N)])
def t12(r):
    roots = [("bio", "life"), ("geo", "earth"), ("tele", "far"), ("aqua", "water"), ("photo", "light"), ("micro", "small"), ("port", "carry"), ("graph", "write")]
    return ("Root words", "Knowing roots unlocks hard words.", [match(r.sample(roots, 3)) for _ in range(N)])
def t13(r):
    qs = [("“I walked to school and saw my friend.”", "First person", ["Third person", "Second person"]), ("“She grabbed her bag and ran.”", "Third person", ["First person", "Second person"]),
          ("“You open the door and step inside.”", "Second person", ["First person", "Third person"]), ("“We cheered when our team scored.”", "First person", ["Third person"]),
          ("“They whispered so no one could hear.”", "Third person", ["First person"])]
    return ("Point of view", "I/we = first, you = second, he/she/they = third.", [pick(r, f"{q} Which point of view?", a, w) for q, a, w in qs])
def t14(r):
    qs = [("Which is correct?", "After dinner, we played games.", ["After dinner we, played games.", "After, dinner we played games."]),
          ("Which is correct?", "I bought apples, pears and plums.", ["I bought apples pears, and plums.", "I, bought apples pears and plums."]),
          ("Which is correct?", "My brother, who is ten, loves chess.", ["My brother who, is ten loves chess.", "My, brother who is ten loves chess."]),
          ("Which is correct?", "Yes, I would love to come.", ["Yes I, would love to come.", "Yes I would, love to come."]),
          ("Which is correct?", "If it snows, we will build a snowman.", ["If it snows we, will build a snowman.", "If, it snows we will build a snowman."])]
    return ("Commas and clauses", "Commas separate lists and extra information.", [pick(r, q, a, w) for q, a, w in qs])
def t15(r):
    topics = [("Should kids have homework every night?", [("Some, so practice stays regular without stress.", True, "A balanced reason that considers both sides."), ("Yes, because I said so.", False, "That is not a reason."), ("No, homework is the worst.", False, "That is an opinion without a reason.")]),
              ("Should schools have longer lunch breaks?", [("Yes, because rest and play help kids focus afterwards.", True, "Gives a clear reason."), ("Lunch is food.", False, "That doesn't answer the question."), ("Yes, longer is longer.", False, "That repeats without a reason.")]),
              ("Should pets be allowed in classrooms?", [("Maybe a class fish, since it's calm and teaches responsibility.", True, "Thinks about pros and cons."), ("Dogs are cute.", False, "Cute isn't an argument."), ("No, never, ever.", False, "No reason given.")]),
              ("Should video games count as sport?", [("Some can, since they need skill, practice and teamwork.", True, "Gives evidence."), ("Games are games.", False, "That isn't a reason."), ("Yes because they're fun.", False, "Fun alone doesn't make a sport.")]),
              ("Should everyone learn to cook?", [("Yes, it keeps you healthy and independent.", True, "Gives two reasons."), ("Cooking is hot.", False, "Not an argument."), ("No, because pizza exists.", False, "That avoids the question.")])]
    return ("Debate: pick a side", "A strong argument gives a reason and evidence.", [choice(q, o) for q, o in topics])
def t16(r):
    lads = [["tiny", "small", "big", "huge"], ["freezing", "cold", "warm", "hot"], ["whisper", "talk", "shout", "scream"], ["walk", "jog", "run", "sprint"], ["glad", "happy", "delighted", "ecstatic"]]
    return ("Vocabulary ladder", "Order words from weakest to strongest.", [build(r, "Order from least to most.", l) for l in lads])
def t17(r):
    ws = ["NIGHT", "LIGHT", "KNIFE", "WRITE", "PHONE", "LAUGH", "CHOIR", "THUMB"]
    return ("Spelling patterns", "Watch for silent letters like k, w and b.", [build(r, f"Spell “{w.lower()}”.", list(w)) for w in r.sample(ws, N)])
def t18(r):
    qs = [("Cinderella and Rapunzel both…", "are rescued from a hard life", ["live under the sea", "are dragons"]), ("Unlike the tortoise, the hare…", "was overconfident", ["was slow", "won the race"]),
          ("The Three Little Pigs and Goldilocks both have…", "the number three", ["a dragon", "a spaceship"]), ("Both Jack (and the Beanstalk) and Aladdin…", "find great treasure", ["are kings", "can fly"]),
          ("In both The Lion King and Hamlet, a son…", "loses his father", ["goes to space", "becomes a fish"])]
    return ("Compare two stories", "Look for what's the same and what's different.", [pick(r, q, a, w) for q, a, w in qs])
def t19(r):
    hs = [["Who", "What", "Where", "When", "Why"], ["Headline", "Opening line", "Details", "Quote", "Ending"], ["Hook the reader", "Give the facts", "Add a quote", "Wrap up"],
          ["Title", "Byline", "Lead paragraph", "Body"], ["Interview a witness", "Check the facts", "Write the story", "Publish"]]
    return ("News reporter", "Good reports answer who, what, where, when and why.", [build(r, "Put the reporting steps in order.", h) for h in hs])
def t20(r):
    rounds = []
    for w in r.sample(["through", "though", "thought", "tough", "thorough", "throne", "thrown", "throw"], N):
        others = [x for x in ["through", "though", "thought", "tough", "thorough", "throne", "thrown", "throw"] if x != w]
        rounds.append(pop(r, w, r.sample(others, 5), 3, 9) | {"q": f"Speed read! Pop “{w}”."})
    return ("Speed reading sprint", "Look at the whole word shape, fast.", rounds)

GEN = {
    "cubs": [c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20],
    "explorers": [e01, e02, e03, e04, e05, e06, e07, e08, e09, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20],
    "trailblazers": [t01, t02, t03, t04, t05, t06, t07, t08, t09, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20],
}
