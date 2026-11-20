"""Science Sky: 20 activities per band."""
from common import *

N = 5


def S(r, bins, a, b, k=3):
    return sort(bins, shuffled(r, [(x, 0) for x in r.sample(a, k)] + [(x, 1) for x in r.sample(b, k)]))


def Q(r, qs, n=N):
    return [pick(r, q, a, w) for q, a, w in r.sample(qs, n)]


# ---------------- Little Cubs ----------------
def c01(r):
    sea = ["Fish", "Whale", "Octopus", "Crab", "Shark", "Starfish", "Seahorse"]
    land = ["Lion", "Cow", "Rabbit", "Horse", "Dog", "Elephant", "Bear"]
    return ("Who lives in the ocean?", "Does it need water to swim in?", [S(r, ["Ocean", "Land"], sea, land) for _ in range(N)])
def c02(r):
    day = ["Sun", "Breakfast", "Rainbow", "Butterflies", "School", "Sunflowers"]
    night = ["Moon", "Stars", "Owls", "Pyjamas", "Bedtime", "Fireflies"]
    return ("Day or night?", "When do you see it, when it's light or dark?", [S(r, ["Day", "Night"], day, night) for _ in range(N)])
def c03(r):
    pairs = [("Cat", "Kitten"), ("Dog", "Puppy"), ("Cow", "Calf"), ("Sheep", "Lamb"), ("Frog", "Tadpole"), ("Hen", "Chick"), ("Horse", "Foal"), ("Duck", "Duckling"), ("Bear", "Cub")]
    return ("Baby animals match", "Babies often have their own special names.", [match(r.sample(pairs, 3)) for _ in range(N)])
def c04(r):
    sets = [("A rubber duck", True), ("A rock", False), ("A leaf", True), ("A coin", False), ("A beach ball", True), ("A key", False), ("A cork", True), ("A spoon", False)]
    rounds = []
    for thing, floats in r.sample(sets, N):
        rounds.append(choice(f"{thing} goes into the water. What happens?", [("It floats", floats, "Light, air-filled things float." if floats else "Heavy, solid things sink."), ("It sinks", not floats, "Heavy, solid things sink." if not floats else "Light, air-filled things float.")]))
    return ("Sink or float?", "Light things with air inside often float.", rounds)
def c05(r):
    qs = [("It's raining! What do you wear?", "A raincoat", ["Sunglasses", "A swimsuit"]), ("It's snowing! What do you wear?", "A warm coat", ["Shorts", "Sandals"]),
          ("It's sunny and hot! What do you wear?", "A sun hat", ["A scarf", "Snow boots"]), ("It's windy! What can you fly?", "A kite", ["A boat", "A sled"]),
          ("It's cold and icy! What goes on your hands?", "Gloves", ["Socks", "A cap"]), ("Puddles everywhere! What goes on your feet?", "Rain boots", ["Slippers", "Flip-flops"])]
    return ("Weather dress-up", "Think about how the weather feels.", Q(r, qs))
def c06(r):
    qs = [("Which part of the plant is under the ground?", "Roots", ["Petals", "Leaves"]), ("Which part is often colourful and smells nice?", "The flower", ["The roots", "The stem"]),
          ("Which part holds the plant up?", "The stem", ["The petals", "The seed"]), ("Which part makes food from sunlight?", "The leaves", ["The roots", "The flower"]),
          ("What grows into a new plant?", "A seed", ["A leaf", "A stone"])]
    return ("Parts of a plant", "Roots drink, leaves eat sunlight, flowers make seeds.", Q(r, qs))
def c07(r):
    hot = ["Fire", "Sun", "Hot soup", "Oven", "Toast", "Bath water", "Desert"]
    cold = ["Ice cream", "Snow", "Fridge", "Ice cube", "Penguin's home", "Snowman", "Frozen peas"]
    return ("Hot or cold?", "Would it warm you up or cool you down?", [S(r, ["Hot", "Cold"], hot, cold) for _ in range(N)])
def c08(r):
    snd = [("Moo", "Cow"), ("Woof", "Dog"), ("Meow", "Cat"), ("Quack", "Duck"), ("Baa", "Sheep"), ("Oink", "Pig"), ("Roar", "Lion"), ("Hoot", "Owl"), ("Neigh", "Horse")]
    rounds = []
    for s_, a in r.sample(snd, N):
        rounds.append(sound(r, f"{s_}! {s_}!", a, r.sample([x for _, x in snd if x != a], 2), "Who makes this sound?"))
    return ("Animal sounds", "Listen, then copy the sound yourself.", rounds)
def c09(r):
    senses = [("Eyes", "See"), ("Ears", "Hear"), ("Nose", "Smell"), ("Tongue", "Taste"), ("Hands", "Touch")]
    return ("Five senses", "Each body part helps you notice the world.", [match(r.sample(senses, 3)) for _ in range(N)])
def c10(r):
    qs = [("Which planet do we live on?", "Earth", ["Mars", "The Moon"]), ("Which is the big hot star in our sky?", "The Sun", ["The Moon", "A cloud"]),
          ("Which planet has big rings?", "Saturn", ["Earth", "Mars"]), ("Which planet is red?", "Mars", ["Saturn", "Earth"]),
          ("What goes around the Earth at night?", "The Moon", ["The Sun", "A rocket"]), ("What do astronauts fly in?", "A rocket", ["A bus", "A boat"])]
    return ("Planet peek", "Our Sun is a star. Planets go around it.", Q(r, qs))
def c11(r):
    steps = ["Plant the seed", "Water it", "Sunshine", "A sprout", "A flower"]
    return ("Grow a seed", "Seeds need water and sunlight.", [build(r, "Help the seed grow. Tap in order.", steps[:3 + (i % 3)]) for i in range(N)])
def c12(r):
    food = [("Rabbit", "Carrot"), ("Monkey", "Banana"), ("Cat", "Fish"), ("Dog", "Bone"), ("Bee", "Nectar"), ("Cow", "Grass"), ("Panda", "Bamboo"), ("Bird", "Worm"), ("Mouse", "Cheese")]
    return ("What do animals eat?", "Think about where each animal lives.", [match(r.sample(food, 3)) for _ in range(N)])
def c13(r):
    sets = [("Opening a door toward you", "Pull"), ("Kicking a ball", "Push"), ("Opening a drawer", "Pull"), ("Riding a swing forward", "Push"),
            ("Pulling a wagon", "Pull"), ("Pressing a button", "Push"), ("Tug of war", "Pull"), ("Pushing a pram", "Push")]
    rounds = []
    for s_, a in r.sample(sets, N):
        rounds.append(choice(f"{s_}: is it a push or a pull?", [("Push", a == "Push", "A push moves things away from you." if a == "Push" else "A pull brings things toward you."), ("Pull", a == "Pull", "A pull brings things toward you." if a == "Pull" else "A push moves things away from you.")]))
    return ("Push or pull?", "Push = away from you. Pull = toward you.", rounds)
def c14(r):
    rb = ["red", "orange", "yellow", "green", "blue", "purple"]
    rounds = []
    for k in range(N):
        s = k % 3
        seq = [tok("circle", c) for c in rb[s:s + 3]]
        rounds.append(pattern(r, seq, tok("circle", rb[s + 3]), [tok("circle", rb[s]), tok("circle", "pink")], "Rainbow order! Which color comes next?"))
    return ("Rainbow colors", "Red, orange, yellow, green, blue, purple.", rounds)
def c15(r):
    yes = ["Apple", "Carrot", "Water", "Broccoli", "Banana", "Fish", "Yogurt"]
    no = ["Candy", "Soda", "Chips", "Cake every day", "Lollipop", "Cookies for dinner"]
    return ("Healthy food plate", "Growing foods give you energy and strong muscles.", [S(r, ["Every day", "Sometimes"], yes, no) for _ in range(N)])
def c16(r):
    qs = [("How many legs does an insect have?", "6", ["8", "4"]), ("Which bug makes honey?", "A bee", ["A fly", "An ant"]), ("Which bug glows at night?", "A firefly", ["A beetle", "A worm"]),
          ("What does a caterpillar turn into?", "A butterfly", ["A bee", "A spider"]), ("Which bug is red with black spots?", "A ladybug", ["A wasp", "A moth"]), ("How many legs does a spider have?", "8", ["6", "10"])]
    return ("Bugs up close", "Insects have 6 legs. Spiders have 8!", Q(r, qs))
def c17(r):
    seasons = ["Spring", "Summer", "Autumn", "Winter"]
    rounds = []
    for k in range(N):
        s = k % 4
        seq = [seasons[(s + i) % 4] for i in range(3)]
        rounds.append(pattern(r, seq, seasons[(s + 3) % 4], [seasons[(s + 1) % 4], seasons[(s + 2) % 4]], "Which season comes next?"))
    return ("Seasons tree", "Spring, summer, autumn, winter, then spring again.", rounds)
def c18(r):
    rounds = []
    things = [("Plane", "Sky"), ("Boat", "Sea"), ("Car", "Land"), ("Helicopter", "Sky"), ("Submarine", "Sea"), ("Train", "Land"), ("Hot air balloon", "Sky"), ("Ship", "Sea"), ("Bike", "Land")]
    for _ in range(N):
        bins = r.sample(["Land", "Sky", "Sea"], 2)
        items = [(t, bins.index(p)) for t, p in r.sample(things, 9) if p in bins][:6]
        while len(items) < 4:
            t, p = r.choice([x for x in things if x[1] in bins]); items.append((t, bins.index(p)))
        rounds.append(sort(bins, items))
    return ("Land, sky or sea?", "Wheels for land, wings for sky, hulls for sea.", rounds)
def c19(r):
    sets = [("An ice cube in the sun", "It melts into water"), ("Water in the freezer", "It turns to ice"), ("Chocolate in a hot hand", "It melts"),
            ("A snowman on a warm day", "It melts"), ("A puddle on a frosty night", "It freezes"), ("Butter in a hot pan", "It melts")]
    rounds = []
    for s_, a in r.sample(sets, N):
        other = "It freezes" if "melt" in a else "It melts"
        rounds.append(choice(f"{s_}. What happens?", [(a, True, "Heat melts things, cold freezes them."), (other, False, "Think: is it getting warmer or colder?"), ("Nothing at all", False, "Temperature changes things.")]))
    return ("Melt the ice", "Warm makes ice melt. Cold makes water freeze.", rounds)
def c20(r):
    plant = ["Triceratops", "Stegosaurus", "Brachiosaurus", "Diplodocus", "Ankylosaurus", "Iguanodon"]
    meat = ["T. rex", "Velociraptor", "Spinosaurus", "Allosaurus", "Giganotosaurus", "Carnotaurus"]
    return ("What did dinos eat?", "Sharp teeth for meat, flat teeth for plants.", [S(r, ["Plants", "Meat"], plant, meat) for _ in range(N)])

# ---------------- Explorers ----------------
def e01(r):
    life = ["Egg", "Tadpole", "Froglet", "Frog"]
    others = [["Egg", "Caterpillar", "Chrysalis", "Butterfly"], ["Seed", "Sprout", "Plant", "Flower"], ["Egg", "Chick", "Hen"]]
    return ("Life cycles", "Living things change as they grow.", [build(r, "Put the frog's life cycle in order.", life)] + [build(r, "Put the life cycle in order.", o) for o in others] + [build(r, "Frog life cycle again, faster!", life)])
def e02(r):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    rounds = []
    for s in r.sample(range(0, 5), N):
        rounds.append(build(r, "Order these planets from the Sun outward.", planets[s:s + 4]))
    return ("Solar system order", "My Very Easy Method Just Speeds Up Naming.", rounds)
def e03(r):
    solids = ["Ice", "Rock", "Wood", "Coin", "Pencil", "Apple"]
    liquids = ["Water", "Milk", "Juice", "Honey", "Oil", "Rain"]
    gases = ["Steam", "Air", "Bubbles' air", "Breath", "Helium", "Fog"]
    rounds = []
    for _ in range(N):
        a, b = r.sample([("Solid", solids), ("Liquid", liquids), ("Gas", gases)], 2)
        rounds.append(S(r, [a[0], b[0]], a[1], b[1]))
    return ("Solid, liquid, gas", "Solids keep shape, liquids pour, gases spread out.", rounds)
def e04(r):
    mag = ["Paperclip", "Iron nail", "Steel spoon", "Fridge door", "Safety pin", "Steel can"]
    non = ["Wooden block", "Plastic cup", "Rubber band", "Paper", "Glass marble", "Cotton sock"]
    return ("Magnet test", "Magnets pull iron and steel.", [S(r, ["Sticks to a magnet", "Does not stick"], mag, non) for _ in range(N)])
def e05(r):
    chains = [["Sun", "Grass", "Rabbit", "Fox"], ["Sun", "Plant", "Caterpillar", "Bird"], ["Sun", "Algae", "Fish", "Seal"], ["Sun", "Seeds", "Mouse", "Owl"], ["Sun", "Leaves", "Snail", "Frog"]]
    return ("Food chain builder", "Energy starts at the Sun and moves up the chain.", [build(r, "Build the food chain.", c) for c in chains])
def e06(r):
    q = [("The hot liquid rock inside a volcano is…", "Magma", ["Ice", "Sand"]), ("When magma comes out it's called…", "Lava", ["Steam", "Mud"]),
         ("The top opening of a volcano is the…", "Crater", ["Root", "Tail"]), ("Lava cools and becomes…", "Rock", ["Water", "Glass of juice"]),
         ("The layer we live on is the Earth's…", "Crust", ["Core", "Mantle"]), ("The very centre of the Earth is the…", "Core", ["Crust", "Crater"])]
    return ("Volcano layers", "Crust on top, mantle in the middle, core at the centre.", Q(r, q))
def e07(r):
    bones = [("Skull", "Protects the brain"), ("Ribs", "Protect the heart and lungs"), ("Spine", "Holds you up"), ("Femur", "Thigh bone, the longest"), ("Pelvis", "Hip bones")]
    return ("Skeleton puzzle", "You have 206 bones!", [match(r.sample(bones, 3)) for _ in range(N)])
def e08(r):
    sets = [("The sun is behind you. Where is your shadow?", [("In front of you", True, "Light is blocked by you, so the shadow falls ahead."), ("Behind you", False, "Shadows fall away from the light.")]),
            ("At noon the sun is high. Your shadow is…", [("Short", True, "High light makes short shadows."), ("Very long", False, "Long shadows happen when the sun is low.")]),
            ("Can a clear window make a dark shadow?", [("No, light passes through", True, "Transparent things let light through."), ("Yes, a very dark one", False, "Only opaque things block light.")]),
            ("You move a torch closer to your toy. The shadow gets…", [("Bigger", True, "Closer light makes bigger shadows."), ("Smaller", False, "Try it: closer makes bigger.")]),
            ("At sunset your shadow is…", [("Long", True, "Low light stretches shadows."), ("Gone", False, "There's still light, so there's still a shadow.")])]
    return ("Light and shadow", "A shadow forms where light is blocked.", [choice(q, o) for q, o in sets])
def e09(r):
    cyc = ["Evaporation", "Condensation", "Precipitation", "Collection"]
    rounds = [build(r, "Order the water cycle.", cyc)]
    rounds += [pick(r, q, a, w) for q, a, w in [("Water heating up and rising as vapour is…", "Evaporation", ["Precipitation", "Collection"]),
               ("Vapour cooling into clouds is…", "Condensation", ["Evaporation", "Erosion"]), ("Rain, snow and hail are…", "Precipitation", ["Condensation", "Collection"]),
               ("Water gathering in rivers and seas is…", "Collection", ["Evaporation", "Condensation"])]]
    return ("The water cycle", "Up as vapour, down as rain, round and round.", rounds)
def e10(r):
    q = [("A scientist who studies fossils is a…", "Palaeontologist", ["Astronaut", "Chef"]), ("Fossils are usually found in…", "Rock", ["Clouds", "Rivers of lava"]),
         ("Which dinosaur had three horns?", "Triceratops", ["T. rex", "Stegosaurus"]), ("Which dinosaur had plates on its back?", "Stegosaurus", ["Velociraptor", "Triceratops"]),
         ("Dinosaurs lived about how long ago?", "Over 66 million years ago", ["100 years ago", "Last week"]), ("To dig carefully, a fossil hunter uses a…", "Brush", ["Hammer only", "Spoon"])]
    return ("Dinosaur fossil dig", "Dig slowly. Fossils are fragile!", Q(r, q))
def e11(r):
    living = ["Tree", "Mushroom", "Cat", "Moss", "Butterfly", "Fish", "Grass"]
    non = ["Rock", "Cloud", "Car", "Toy robot", "Water", "Sand", "Bicycle"]
    return ("Living or not?", "Living things grow, eat and have babies.", [S(r, ["Living", "Not living"], living, non) for _ in range(N)])
def e12(r):
    m = [("Ramp", "Inclined plane"), ("Seesaw", "Lever"), ("Flagpole rope", "Pulley"), ("Door knob", "Wheel and axle"), ("Axe", "Wedge"), ("Jar lid", "Screw")]
    return ("Simple machines", "Simple machines make work easier.", [match(r.sample(m, 3)) for _ in range(N)])
def e13(r):
    ph = ["New moon", "Crescent", "Half moon", "Gibbous", "Full moon"]
    rounds = [build(r, "Order the Moon growing from new to full.", ph[i:i + 3 + (i % 2)]) for i in range(3)]
    rounds += [pick(r, "When the whole Moon is lit, it's a…", "Full moon", ["New moon", "Crescent"]), pick(r, "About how long from full moon to full moon?", "About a month", ["A day", "A year"])]
    return ("Moon phases", "The Moon doesn't change. We see different lit parts.", rounds)
def e14(r):
    q = [("Rock made from cooled lava is…", "Igneous", ["Sedimentary", "Metamorphic"]), ("Rock made of squashed layers of sand is…", "Sedimentary", ["Igneous", "Metamorphic"]),
         ("Rock changed by heat and pressure is…", "Metamorphic", ["Igneous", "Sedimentary"]), ("Which is the hardest mineral?", "Diamond", ["Chalk", "Salt"]),
         ("Chalk is soft enough to…", "Draw with", ["Cut glass", "Build skyscrapers alone"]), ("Fossils are most often found in…", "Sedimentary rock", ["Igneous rock", "Metal"])]
    return ("Rocks and minerals", "Rocks are made of minerals.", Q(r, q))
def e15(r):
    h = [("Camel", "Desert"), ("Polar bear", "Arctic"), ("Monkey", "Rainforest"), ("Shark", "Ocean"), ("Owl", "Woodland"), ("Penguin", "Antarctic"), ("Frog", "Pond"), ("Lion", "Savanna")]
    return ("Habitat match", "Animals live where their bodies fit best.", [match(r.sample(h, 3)) for _ in range(N)])
def e16(r):
    sets = [("You pluck a tight rubber band. It makes a…", [("Higher sound", True, "Tighter means faster vibrations, higher pitch."), ("No sound", False, "Vibrations make sound.")]),
            ("Sound travels best through…", [("Solids", True, "Particles are closest in solids."), ("Empty space", False, "Sound can't travel in space.")]),
            ("Why do you hear a drum?", [("It vibrates the air", True, "Vibrations travel to your ear."), ("It glows", False, "Light isn't sound.")]),
            ("A big drum compared with a small drum sounds…", [("Lower", True, "Bigger things vibrate slower."), ("Higher", False, "Small things vibrate faster.")]),
            ("Which is louder?", [("A big vibration", True, "Bigger vibrations are louder."), ("A tiny vibration", False, "Tiny vibrations are quiet.")])]
    return ("Sound vibrations", "All sounds are vibrations.", [choice(q, o) for q, o in sets])
def e17(r):
    sets = [("A plant is kept in a dark cupboard for a week. What happens?", [("It turns pale and weak", True, "Plants need light to make food."), ("It grows faster", False, "Without light, it can't make food.")]),
            ("One plant gets water, one doesn't. Which grows?", [("The watered one", True, "Water carries food around the plant."), ("The dry one", False, "Plants wilt without water.")]),
            ("Plants take in which gas from the air?", [("Carbon dioxide", True, "They turn it into food and oxygen."), ("Helium", False, "Plants don't use helium.")]),
            ("What do roots do?", [("Take up water", True, "Roots drink and hold the plant."), ("Make flowers", False, "Flowers grow on stems.")]),
            ("To test what plants need, you change…", [("Only one thing", True, "A fair test changes one thing at a time."), ("Everything at once", False, "Then you can't tell what worked.")])]
    return ("What do plants need?", "Light, water, air and nutrients.", [choice(q, o) for q, o in sets])
def e18(r):
    rec = ["Paper", "Glass bottle", "Tin can", "Cardboard", "Plastic bottle", "Newspaper"]
    comp = ["Banana peel", "Apple core", "Leaves", "Eggshells", "Tea leaves", "Grass cuttings"]
    return ("Recycle sort", "Food scraps go to compost. Paper and bottles get recycled.", [S(r, ["Recycle", "Compost"], rec, comp) for _ in range(N)])
def e19(r):
    q = [("Dark grey clouds usually mean…", "Rain is coming", ["It will be sunny", "Snow in summer"]), ("A weather tool that measures temperature is a…", "Thermometer", ["Telescope", "Ruler"]),
         ("Wind direction is shown by a…", "Weather vane", ["Microscope", "Scale"]), ("Rain is measured with a…", "Rain gauge", ["Compass", "Clock"]),
         ("A sky with no clouds is…", "Clear", ["Overcast", "Foggy"]), ("Lightning comes before thunder because…", "Light travels faster than sound", ["Thunder is shy", "Clouds are slow"])]
    return ("Weather forecaster", "Look at the clouds and the tools.", Q(r, q))
def e20(r):
    sets = [("You sneeze. What should you do?", [("Sneeze into your elbow", True, "That stops germs spreading."), ("Sneeze on your friend", False, "That spreads germs.")]),
            ("How long should you wash your hands?", [("About 20 seconds", True, "Sing Happy Birthday twice!"), ("1 second", False, "Too quick to wash germs off.")]),
            ("When should you wash your hands?", [("Before eating", True, "Clean hands keep food safe."), ("Never", False, "Germs build up on hands.")]),
            ("What helps kill germs?", [("Soap and water", True, "Soap breaks germs apart."), ("Just shaking hands dry", False, "That leaves germs on.")]),
            ("Your friend is sick. What helps?", [("Give them space and rest", True, "Rest helps the body fight germs."), ("Share their drink", False, "That spreads germs.")])]
    return ("Germs and hand washing", "Germs are tiny. Soap stops them.", [choice(q, o) for q, o in sets])

# ---------------- Trailblazers ----------------
def t01(r):
    p = [("Nucleus", "Control centre"), ("Cell membrane", "Lets things in and out"), ("Chloroplast", "Makes food in plants"), ("Mitochondria", "Makes energy"), ("Cell wall", "Gives plant cells shape")]
    return ("Cells under the microscope", "All living things are made of cells.", [match(r.sample(p, 3)) for _ in range(N)])
def t02(r):
    sets = [("A bulb, battery and wires make a loop. What happens?", [("The bulb lights", True, "A complete circuit lets current flow."), ("Nothing", False, "A complete loop works.")]),
            ("The circuit has a gap. What happens?", [("The bulb stays off", True, "A broken circuit stops the current."), ("The bulb gets brighter", False, "No current can flow.")]),
            ("Which material lets electricity through?", [("Copper", True, "Metals are conductors."), ("Rubber", False, "Rubber is an insulator.")]),
            ("Adding a second battery makes the bulb…", [("Brighter", True, "More voltage, more current."), ("Dimmer", False, "Try it: more power, brighter.")]),
            ("A switch is used to…", [("Open and close the circuit", True, "That turns it on and off."), ("Store electricity", False, "That's a battery.")])]
    return ("Circuit builder", "Electricity needs a complete loop.", [choice(q, o) for q, o in sets])
def t03(r):
    el = [("O", "Oxygen"), ("H", "Hydrogen"), ("C", "Carbon"), ("Fe", "Iron"), ("Na", "Sodium"), ("Au", "Gold"), ("He", "Helium"), ("Ag", "Silver")]
    return ("Periodic table pals", "Symbols are short codes for elements.", [match(r.sample(el, 3)) for _ in range(N)])
def t04(r):
    sets = [("You kick a ball on grass and on ice. Where does it go further?", [("On ice", True, "Less friction."), ("On grass", False, "Grass has more friction.")]),
            ("A heavier truck needs ___ force to start moving.", [("More", True, "More mass needs more force."), ("Less", False, "Heavy things resist moving.")]),
            ("When you jump, what pulls you back down?", [("Gravity", True, "Gravity pulls toward Earth."), ("Wind", False, "It's gravity.")]),
            ("A parachute slows you because of…", [("Air resistance", True, "Big surfaces push on lots of air."), ("Magnetism", False, "It's air pushing back.")]),
            ("Every action has an equal and opposite…", [("Reaction", True, "Newton's third law."), ("Colour", False, "It's a reaction.")])]
    return ("Forces and motion lab", "Forces push, pull and twist.", [choice(q, o) for q, o in sets])
def t05(r):
    sets = [("Wolves are removed from a park. Deer numbers…", [("Rise, and they eat too many plants", True, "Predators keep balance."), ("Stay exactly the same", False, "Changes ripple through.")]),
            ("Bees disappear. What happens to flowers?", [("Fewer get pollinated", True, "Bees carry pollen."), ("Nothing changes", False, "Bees are pollinators.")]),
            ("A river is polluted. Fish…", [("Become sick or fewer", True, "Clean water keeps them healthy."), ("Grow bigger", False, "Pollution harms them.")]),
            ("Trees are planted on bare hills. The soil…", [("Is held in place", True, "Roots stop erosion."), ("Washes away faster", False, "Roots protect soil.")]),
            ("Which keeps an ecosystem healthy?", [("Many different species", True, "Biodiversity adds balance."), ("Just one species", False, "Variety matters.")])]
    return ("Ecosystem balance", "Every living thing is connected.", [choice(q, o) for q, o in sets])
def t06(r):
    s = [("Heart", "Pumps blood"), ("Lungs", "Breathe in oxygen"), ("Brain", "Controls the body"), ("Stomach", "Digests food"), ("Kidneys", "Clean the blood"), ("Skin", "Protects the body")]
    return ("Human body systems", "Organs work together in systems.", [match(r.sample(s, 3)) for _ in range(N)])
def t07(r):
    w = ["It's raining today", "Tomorrow will be windy", "This afternoon is foggy", "It snowed last night", "There's a thunderstorm now"]
    c = ["The Sahara is dry most years", "The Arctic is cold all year", "Rainforests are wet year-round", "Summers here are usually warm", "Monsoons come every year"]
    return ("Climate or weather?", "Weather is today. Climate is the pattern over many years.", [S(r, ["Weather", "Climate"], w, c) for _ in range(N)])
def t08(r):
    rounds = []
    facts = [("Jupiter", "the largest planet"), ("Mercury", "closest to the Sun"), ("Mars", "the red planet"), ("Venus", "the hottest planet"), ("Saturn", "famous rings"), ("Neptune", "farthest from the Sun")]
    for name, fact in r.sample(facts, N):
        rounds.append(pop(r, name, r.sample([n for n, _ in facts if n != name] + ["Pluto", "Earth"], 5), 3, 9) | {"q": f"Pop the planet that is {fact}!"})
    return ("Planet facts race", "Remember one fact per planet.", rounds)
def t09(r):
    ch = ["Burning wood", "Baking a cake", "Rusting iron", "Frying an egg", "Milk going sour", "Fireworks exploding"]
    ph = ["Melting ice", "Cutting paper", "Boiling water", "Dissolving sugar", "Crushing a can", "Freezing juice"]
    return ("Chemical or physical change?", "Chemical changes make a new substance.", [S(r, ["Chemical", "Physical"], ch, ph) for _ in range(N)])
def t10(r):
    q = [("Traits passed from parents to children are…", "Inherited", ["Learned", "Invented"]), ("Information for traits is stored in…", "DNA", ["Bones", "Hair gel"]),
         ("Eye colour is an example of an…", "Inherited trait", ["Learned skill", "Habit"]), ("Riding a bike is an example of a…", "Learned skill", ["Inherited trait", "Gene"]),
         ("A section of DNA for one trait is a…", "Gene", ["Cell wall", "Planet"]), ("Identical twins share the same…", "DNA", ["Fingerprints", "Handwriting"])]
    return ("Traits and genes", "Some things you inherit. Some you learn.", Q(r, q))
def t11(r):
    q = [("Earth's crust is broken into huge…", "Plates", ["Bricks", "Bubbles"]), ("When plates push together they can form…", "Mountains", ["Oceans of ice", "Clouds"]),
         ("Sudden plate movement causes…", "Earthquakes", ["Rainbows", "Tides"]), ("Where plates pull apart, new crust is made from…", "Magma", ["Sand", "Glass"]),
         ("The Himalayas formed when India collided with…", "Asia", ["Australia", "Antarctica"])]
    return ("Plate tectonics", "Plates move only a few centimetres a year.", Q(r, q))
def t12(r):
    sets = [("A ball rolls down a hill. Stored energy becomes…", [("Movement energy", True, "Potential becomes kinetic."), ("Sound only", False, "Most becomes movement.")]),
            ("A solar panel turns sunlight into…", [("Electricity", True, "Light energy to electrical."), ("Water", False, "It makes electricity.")]),
            ("Rubbing your hands makes them warm. That's…", [("Movement to heat", True, "Friction makes heat."), ("Heat to light", False, "It's friction heat.")]),
            ("Food gives your body…", [("Chemical energy", True, "Stored in food."), ("Magnetic energy", False, "It's chemical energy.")]),
            ("Energy can't be created or destroyed, only…", [("Changed", True, "Conservation of energy."), ("Deleted", False, "It's transformed.")])]
    return ("Energy transfer", "Energy changes form but never disappears.", [choice(q, o) for q, o in sets])
def t13(r):
    steps = ["Ask a question", "Make a prediction", "Plan a fair test", "Do the experiment", "Record results", "Draw a conclusion"]
    return ("Design an experiment", "Change one thing, keep the rest the same.", [build(r, "Order the science steps.", steps[i:i + 4]) for i in range(3)] + [build(r, "Order all the steps.", steps), build(r, "Order these steps.", steps[::2])])
def t14(r):
    q = [("The number of waves per second is…", "Frequency", ["Volume", "Colour"]), ("Higher frequency sounds are…", "Higher pitched", ["Louder always", "Slower"]),
         ("The height of a wave relates to…", "Loudness", ["Pitch", "Speed"]), ("Humans can't hear very high sounds called…", "Ultrasound", ["Infrared", "Echoes"]),
         ("A bouncing sound is an…", "Echo", ["Orbit", "Eclipse"])]
    return ("Sound waves", "Pitch is frequency. Loudness is amplitude.", Q(r, q))
def t15(r):
    sets = [("You weigh 30 kg on Earth. On the Moon you'd feel…", [("Much lighter", True, "Moon gravity is about 1/6 of Earth's."), ("Heavier", False, "The Moon has weaker gravity.")]),
            ("On Jupiter you'd feel…", [("Heavier", True, "Jupiter's gravity is stronger."), ("Lighter", False, "Bigger planet, stronger pull.")]),
            ("Drop a feather and hammer on the Moon. They…", [("Land together", True, "No air resistance."), ("The feather floats away", False, "No air to slow it.")]),
            ("Why do astronauts float in the space station?", [("They're falling around Earth", True, "They're in free fall."), ("There's no gravity at all", False, "Gravity is still there.")]),
            ("Your mass on Mars is…", [("The same", True, "Mass doesn't change, weight does."), ("Zero", False, "You still have mass.")])]
    return ("Gravity on other planets", "Weight changes with gravity. Mass doesn't.", [choice(q, o) for q, o in sets])
def t16(r):
    a = [("Camel's hump", "Stores fat for energy"), ("Polar bear's thick fur", "Keeps warm"), ("Giraffe's long neck", "Reaches high leaves"), ("Duck's webbed feet", "Swims well"),
         ("Chameleon's colour change", "Hides from predators"), ("Owl's big eyes", "Sees at night")]
    return ("Animal adaptations", "Adaptations help animals survive.", [match(r.sample(a, 3)) for _ in range(N)])
def t17(r):
    ren = ["Solar", "Wind", "Hydro", "Geothermal", "Tidal", "Biomass"]
    non = ["Coal", "Oil", "Natural gas", "Diesel", "Petrol", "Peat"]
    return ("Renewable energy", "Renewables won't run out.", [S(r, ["Renewable", "Non-renewable"], ren, non) for _ in range(N)])
def t18(r):
    good = ["Yogurt bacteria", "Yeast for bread", "Gut bacteria", "Compost microbes", "Cheese mould", "Soil bacteria"]
    bad = ["Flu virus", "Cold virus", "Food poisoning bacteria", "Strep throat", "Athlete's foot fungus", "Mould on old bread"]
    return ("Microbes: good or bad?", "Most microbes are harmless or helpful.", [S(r, ["Helpful", "Harmful"], good, bad) for _ in range(N)])
def t19(r):
    sp = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
    return ("The light spectrum", "ROY G BIV.", [build(r, "Order the colours of the rainbow.", sp[i:i + 4]) for i in range(4)] + [build(r, "All seven, in order!", sp)])
def t20(r):
    z = ["Sunlight zone", "Twilight zone", "Midnight zone", "Abyss", "Trenches"]
    return ("Ocean zones", "The deeper you go, the darker and colder.", [build(r, "Order the ocean from surface to deepest.", z[i:i + 3]) for i in range(3)] + [build(r, "All the ocean zones, in order.", z), pick(r, "Which zone gets the most sunlight?", "Sunlight zone", ["Midnight zone", "Abyss"])][:N])

GEN = {
    "cubs": [c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20],
    "explorers": [e01, e02, e03, e04, e05, e06, e07, e08, e09, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20],
    "trailblazers": [t01, t02, t03, t04, t05, t06, t07, t08, t09, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20],
}
