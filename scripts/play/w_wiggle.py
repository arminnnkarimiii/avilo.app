"""Wiggle Park: motor and tap skills. 20 activities per band.

Pop rounds are timed (bubbles float), trace rounds score precision, motion rounds
score timing. The game screen records tap accuracy and reaction time for each.
"""
from common import *

N = 5
POOL = ["@balloon:red", "@balloon:blue", "@balloon:yellow", "@balloon:green", "@star", "@heart", "@fish", "@bug", "@leaf", "@apple"]


def pops(r, target, others, total, goals):
    return [pop(r, target, others, g, total) for g in goals]


def paths(gen_list):
    return [trace(label, pts) for label, pts in gen_list]


# ---------------- Little Cubs ----------------
def c01(r): return ("Pop the bubbles!", "Tap gently with one finger.", pops(r, "@circle:blue", ["@circle:green", "@circle:pink"], 7, [3, 3, 4, 4, 5]))
def c02(r):
    return ("Drag the ball to the goal", "Tap the ball, then tap the right goal.",
            [sort(["Red goal", "Blue goal"], shuffled(r, [(tok("ball", "red"), 0)] * 2 + [(tok("ball", "blue"), 1)] * 2)) for _ in range(N)])
def c03(r): return ("Trace the wavy line", "Slow and steady.", paths([("wave", wave(7, 18, 1)), ("wave", wave(8, 22, 1.2)), ("wave", wave(9, 25, 1.5)), ("wave", wave(9, 28, 1.8)), ("wave", wave(10, 30, 2))]))
def c04(r): return ("Tap the twinkling star", "Tap the star as fast as you can.", pops(r, "@star:yellow", ["@moon", "@cloud"], 6, [2, 2, 3, 3, 3]))
def c05(r):
    return ("Feed the fish", "Tap the food, then the fish who wants it.",
            [sort(["Big fish", "Little fish"], shuffled(r, [("Big pellet", 0), ("Worm", 0), ("Tiny flake", 1), ("Crumb", 1)])) for _ in range(N)])
def c06(r): return ("Hold to grow the flower", "Press and hold until it's in the green.", [motion("Press when the flower reaches the green zone!", s, z) for s, z in [(0.6, 44), (0.7, 42), (0.8, 40), (0.9, 38), (1.0, 36)]])
def c07(r): return ("Follow the ladybug", "Keep your finger on the path.", paths([("ladybug", spiral(10, 1.2)), ("ladybug", wave(8, 20, 1)), ("ladybug", zigzag(6, 22)), ("ladybug", spiral(12, 1.5)), ("ladybug", wave(9, 26, 1.4))]))
def c08(r): return ("Zoom with two fingers", "Tap the right size.", [pick(r, "Which picture is zoomed in?", tok("bug", "red", 1), [tok("bug", "red", 3), tok("bug", "red", 2)]) | {"q": f"Zoom! Which shows ONE big {x}?"} for x in ["bug", "fish", "star", "leaf", "duck"]])
def c09(r): return ("Swipe the leaves", "Tap each leaf to sweep it away.", pops(r, "@leaf:orange", ["@leaf:green"], 8, [3, 4, 4, 5, 5]))
def c10(r): return ("Connect the dots", "Go in number order.", paths([("dots", zigzag(5, 25)), ("dots", shape_path("triangle")), ("dots", shape_path("square")), ("dots", shape_path("house")), ("dots", shape_path("heart"))]))
def c11(r): return ("Catch the falling apples", "Tap each apple before it lands.", pops(r, "@apple:red", ["@leaf", "@cloud"], 8, [3, 4, 4, 5, 5]))
def c12(r): return ("Pinch the crab", "Tap the crab, not the shells.", pops(r, "@bug:red", ["@shell", "@fish"], 8, [2, 3, 3, 4, 4]))
def c13(r): return ("Spin the wheel", "Tap the turns in order.", [build(r, "Spin the wheel all the way round.", ["Top", "Right", "Bottom", "Left"][:3 + i % 2]) for i in range(N)])
def c14(r): return ("Tap to the beat", "Listen, then tap along.", [rhythm(r, 2, 3 + i % 2) for i in range(N)])
def c15(r): return ("Stack the blocks", "Biggest on the bottom.", [build(r, "Stack biggest first.", [tok("block", c, k) for k in range(3 + i % 2, 0, -1)]) for i, c in enumerate(r.sample(COLORS, N))])
def c16(r): return ("Color inside the lines", "Follow the outline carefully.", paths([("circle", shape_path("circle")), ("square", shape_path("square")), ("heart", shape_path("heart")), ("star", shape_path("star")), ("triangle", shape_path("triangle"))]))
def c17(r): return ("Squish the jelly", "Tap every jelly!", pops(r, "@drop:pink", ["@drop:blue"], 8, [3, 4, 4, 5, 5]))
def c18(r): return ("Zigzag road", "Turn at each corner.", paths([("zigzag", zigzag(5, 20)), ("zigzag", zigzag(6, 24)), ("zigzag", zigzag(7, 28)), ("zigzag", zigzag(8, 30)), ("zigzag", zigzag(9, 32))]))
def c19(r): return ("Shake to wake Avi", "Tap when the bar hits green to wake Avi.", [motion("Tap when the marker is in the green to wake Avi!", s, z) for s, z in [(0.7, 42), (0.8, 40), (0.9, 38), (1.0, 36), (1.1, 34)]])
def c20(r): return ("Double-tap the drum", "Two quick taps!", [rhythm(r, 2, 2 + i % 3) for i in range(N)])

# ---------------- Explorers ----------------
def e01(r): return ("Speed tap challenge", "Only the targets. Fast!", pops(r, "@star:red", ["@star:blue", "@star:yellow"], 10, [4, 4, 5, 5, 6]))
def e02(r): return ("Trace letters neatly", "Stay on the dots.", [trace(L, glyph(L)) for L in r.sample(list("BDEFGKPRSZ"), N)])
def e03(r): return ("Catch the moving target", "Tap the target bubbles as they float.", pops(r, "@heart:red", ["@heart:pink", "@circle:red"], 10, [3, 4, 4, 5, 5]))
def e04(r): return ("Slingshot aim", "Release in the green!", [motion("Release when the marker is in the green.", s, z) for s, z in [(1.0, 30), (1.2, 28), (1.4, 26), (1.6, 24), (1.8, 22)]])
def e05(r): return ("Balance the ball", "Tap to keep the ball in the green.", [motion("Keep it balanced: tap in the green!", s, z) for s, z in [(1.1, 30), (1.3, 28), (1.5, 26), (1.7, 24), (1.9, 22)]])
def e06(r): return ("Finger maze run", "Don't touch the walls.", paths([("maze", zigzag(7, 30)), ("maze", spiral(12, 1.5)), ("maze", wave(9, 30, 2)), ("maze", zigzag(9, 34)), ("maze", spiral(14, 2))]))
def e07(r): return ("Rhythm runner", "Jump on the beat.", [rhythm(r, 3, 4 + i % 2) for i in range(N)])
def e08(r): return ("Fast swipes", "Clear the targets quickly.", pops(r, "@leaf:orange", ["@leaf:green", "@flower"], 10, [4, 5, 5, 6, 6]))
def e09(r): return ("Thread the needle", "Tiny, careful moves.", paths([("thread", wave(10, 12, 2)), ("thread", wave(11, 14, 2.5)), ("thread", zigzag(10, 15)), ("thread", wave(12, 16, 3)), ("thread", zigzag(12, 18))]))
def e10(r): return ("Draw shapes freehand", "Draw the shape. Avi guesses it.", [draw(s, r.sample([x for x in ["circle", "square", "triangle", "star", "heart"] if x != s], 2)) for s in r.sample(["circle", "square", "triangle", "star", "heart"], N)])
def e11(r): return ("Whack-a-mole", "Tap the moles, not the flowers!", pops(r, "@dog:brown", ["@flower", "@leaf"], 9, [3, 4, 4, 5, 5]))
def e12(r):
    return ("Drag-and-sort race", "Sort fast but carefully.",
            [sort(["Fruit", "Toy"], shuffled(r, [(tok(i), 0) for i in r.sample(["apple", "cookie", "egg"], 2)] + [(tok(i), 1) for i in r.sample(["ball", "car", "block", "drum"], 3)])) for _ in range(N)])
def e13(r): return ("Two-hand tap", "Left hand left drum, right hand right drum.", [rhythm(r, 2, 4 + i % 3) for i in range(N)])
def e14(r): return ("Tightrope walker", "Stay on the rope.", paths([("rope", wave(9, 8, 1)), ("rope", wave(10, 10, 1.5)), ("rope", wave(11, 12, 2)), ("rope", wave(12, 10, 2.5)), ("rope", wave(12, 14, 3))]))
def e15(r): return ("Bounce timing", "Tap at the top of the bounce.", [motion("Tap when the ball is in the green.", s, z) for s, z in [(1.2, 26), (1.4, 24), (1.6, 22), (1.8, 20), (2.0, 18)]])
def e16(r): return ("Air hockey", "Hit the puck when it's in the green.", [motion("Strike in the green zone!", s, z) for s, z in [(1.3, 26), (1.5, 24), (1.7, 22), (1.9, 20), (2.1, 18)]])
def e17(r): return ("Star connect speed", "Connect the star points quickly.", paths([("star", shape_path("star")), ("lightning", shape_path("lightning")), ("star", [(x * 0.9 + 5, y * 0.9 + 5) for x, y in shape_path("star")]), ("moon", shape_path("moon")), ("flower", shape_path("flower"))]))
def e18(r): return ("Pinch and place", "Place them in size order.", [build(r, "Place from biggest to smallest.", [tok(ic, "blue", k) for k in range(4, 0, -1)]) for ic in r.sample(["ball", "block", "star", "circle", "heart"], N)])
def e19(r): return ("Pattern taps", "Plan your taps, then go.", [rhythm(r, 4, 4 + i % 2) for i in range(N)])
def e20(r): return ("Catch the butterflies", "Track them as they float.", pops(r, "@bug:purple", ["@bug:green", "@leaf"], 10, [3, 4, 4, 5, 5]))

# ---------------- Trailblazers ----------------
def t01(r): return ("Reflex lab", "React the moment it's in the zone.", [motion("Tap in the green as fast as you can react.", s, z) for s, z in [(2.0, 16), (2.3, 14), (2.6, 13), (2.9, 12), (3.2, 10)]])
def t02(r): return ("Precision drawing", "Smooth and accurate.", paths([("spiral", spiral(16, 2.2)), ("wave", wave(14, 30, 3)), ("star", shape_path("star")), ("lightning", shape_path("lightning")), ("flower", shape_path("flower"))]))
def t03(r): return ("Rhythm master", "Long sequences, perfect timing.", [rhythm(r, 4, 6 + i % 3) for i in range(N)])
def t04(r):
    rounds = []
    for w in r.sample(["Q", "W", "E", "R", "T", "Y", "A", "S", "D", "F"], N):
        rounds.append(pop(r, w, [x for x in "QWERTYASDF" if x != w], 4, 10) | {"q": f"Tap every {w} key!"})
    return ("Speed typing letters", "Find the key, tap it fast.", rounds)
def t05(r): return ("Laser maze", "Thread between the lasers.", paths([("laser", zigzag(10, 36)), ("laser", zigzag(12, 38)), ("laser", wave(14, 36, 3.5)), ("laser", zigzag(14, 40)), ("laser", spiral(16, 2.5))]))
def t06(r): return ("Juggling taps", "Keep every ball up!", pops(r, "@ball:orange", ["@ball:purple", "@ball:green"], 12, [4, 5, 5, 6, 6]))
def t07(r): return ("Archery aim", "Release in the bullseye.", [motion("Release in the green bullseye.", s, z) for s, z in [(1.8, 16), (2.0, 14), (2.2, 13), (2.4, 12), (2.6, 10)]])
def t08(r): return ("Moving maze", "Follow the path as it twists.", paths([("maze", spiral(14, 2)), ("maze", wave(13, 32, 3)), ("maze", zigzag(12, 36)), ("maze", spiral(16, 2.6)), ("maze", wave(15, 34, 3.6))]))
def t09(r): return ("Two-thumb race", "Left and right, alternate fast.", [rhythm(r, 2, 6 + i) for i in range(N)])
def t10(r): return ("Draw a perfect circle", "One smooth loop.", paths([("circle", shape_path("circle")), ("circle", [(x * 0.8 + 10, y * 0.8 + 10) for x, y in shape_path("circle")]), ("circle", [(x * 0.6 + 20, y * 0.6 + 20) for x, y in shape_path("circle")]), ("circle", [(x * 0.9 + 5, y * 0.9 + 5) for x, y in shape_path("circle")]), ("circle", [(x * 0.7 + 15, y * 0.7 + 15) for x, y in shape_path("circle")])]))
def t11(r): return ("Beat drop", "Hit the drop exactly.", [motion("Tap right on the drop: the green zone!", s, z) for s, z in [(2.0, 14), (2.2, 13), (2.4, 12), (2.6, 11), (2.8, 10)]])
def t12(r): return ("Ninja slice", "Slice the fruit, avoid the bombs!", pops(r, "@apple:green", ["@circle:brown", "@diamond:brown"], 12, [4, 5, 5, 6, 6]))
def t13(r): return ("Tower stacker pro", "Perfect order, no wobble.", [build(r, "Stack biggest to smallest.", [tok(ic, c, k) for k in range(5, 0, -1)]) for ic, c in zip(r.sample(["block", "ball", "circle", "square", "star"], N), r.sample(COLORS, N))])
def t14(r): return ("Dodge ball", "Tap only the safe balls.", pops(r, "@ball:green", ["@ball:red", "@ball:yellow"], 12, [3, 4, 5, 5, 6]))
def t15(r): return ("Pendulum timing", "Tap at the bottom of the swing.", [motion("Tap as it swings through the green.", s, z) for s, z in [(1.6, 18), (1.8, 16), (2.0, 15), (2.2, 14), (2.4, 12)]])
def t16(r): return ("Calligraphy strokes", "Smooth curves, steady speed.", paths([("loop", spiral(14, 2)), ("S", glyph("S")), ("G", glyph("G")), ("wave", wave(14, 26, 2.5)), ("Q", glyph("Q"))]))
def t17(r): return ("Speed memory taps", "Remember, then tap fast.", [rhythm(r, 4, 5 + i) for i in range(N)])
def t18(r): return ("Goalkeeper", "Dive when the ball is in the zone.", [motion("Save it! Tap in the green.", s, z) for s, z in [(1.9, 16), (2.1, 15), (2.3, 14), (2.5, 12), (2.7, 11)]])
def t19(r): return ("Tilt maze pro", "Guide the ball along the path.", paths([("tilt", zigzag(11, 34)), ("tilt", spiral(15, 2.3)), ("tilt", wave(14, 30, 3.2)), ("tilt", zigzag(13, 38)), ("tilt", spiral(17, 2.8))]))
def t20(r): return ("Stretch break", "Move along with the beat: reach, twist, bend.", [rhythm(r, 3, 4) for _ in range(N)])

GEN = {
    "cubs": [c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20],
    "explorers": [e01, e02, e03, e04, e05, e06, e07, e08, e09, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20],
    "trailblazers": [t01, t02, t03, t04, t05, t06, t07, t08, t09, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20],
}
