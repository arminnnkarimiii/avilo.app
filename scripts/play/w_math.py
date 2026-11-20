"""Math Meadow: 20 activities per band. Each function returns (prompt, tip, rounds)."""
from common import *

N = 5  # rounds per activity


def _nums(r, lo, hi, k):
    return r.sample(range(lo, hi + 1), k)


# ---------------- Little Cubs 3–5 ----------------
def c01(r):
    return ("Count the dino eggs in the nest.", "Touch each egg as you count it.",
            [count(r, "egg", n, "How many eggs in the nest?") for n in _nums(r, 1, 5, N)])

def c02(r):
    big = ["Elephant", "Whale", "Bus", "House", "Giraffe", "Mountain", "Ship", "Truck"]
    small = ["Ant", "Mouse", "Button", "Pea", "Bee", "Coin", "Ladybug", "Pebble"]
    return ("Is it big or small?", "Think: could it fit in your hand?",
            [sort(["Big", "Small"], shuffled(r, [(b, 0) for b in r.sample(big, 3)] + [(s, 1) for s in r.sample(small, 3)])) for _ in range(N)])

def c03(r):
    others = ["square", "triangle", "rect", "diamond", "star", "heart"]
    return ("Find the circle!", "A circle is round all the way, like a ball.",
            [pick(r, "Which one is a circle?", tok("circle", c), [tok(o, c) for o in r.sample(others, 2)]) for c in r.sample(COLORS, N)])

def c04(r):
    return ("Count the rockets up to 10.", "Count slowly, one rocket at a time.",
            [count(r, "rocket", n, "How many rockets?") for n in _nums(r, 6, 10, N)])

def c05(r):
    rounds = []
    for _ in range(N):
        ns = r.sample(range(1, 7), 3)
        rounds.append(match([(str(n), "●" * n) for n in ns]))
    return ("Match each number to its dots.", "Count the dots, then find the number.", rounds)

def c06(r):
    rounds = []
    for _ in range(N):
        a, b = r.sample(range(1, 7), 2)
        right = tok("apple", "red", max(a, b))
        rounds.append(pick(r, "Which basket has more apples?", right, [tok("apple", "red", min(a, b))]))
    return ("More or fewer apples?", "More means the bigger pile.", rounds)

def c07(r):
    rounds = []
    for _ in range(N):
        c1, c2 = r.sample(["red", "blue", "green", "yellow"], 2)
        icons = r.sample(["ball", "balloon", "heart", "flower", "car", "star"], 4)
        items = [(tok(i, c1), 0) for i in icons[:3]] + [(tok(i, c2), 1) for i in icons[1:4]]
        rounds.append(sort([c1.capitalize(), c2.capitalize()], shuffled(r, items)))
    return ("Sort the toys by color.", "Look only at the color, not the shape.", rounds)

def c08(r):
    return ("Trace the numbers 1, 2 and 3.", "Start at the dot with the number 1.",
            [trace(d, glyph(d)) for d in ["1", "2", "3", "2", "3"]])

def c09(r):
    rounds = []
    for _ in range(N):
        a, b = r.sample(["red", "blue", "yellow", "green", "purple"], 2)
        ic = r.choice(["ball", "circle", "flower"])
        rounds.append(pattern(r, [tok(ic, a), tok(ic, b), tok(ic, a), tok(ic, b), tok(ic, a)], tok(ic, b), [tok(ic, a)]))
    return ("Finish the bead pattern.", "Say the colors out loud: red, blue, red, blue…", rounds)

def c10(r):
    longs = ["Train", "Snake", "Scarf", "Rope", "River", "Ladder", "Hose"]
    shorts = ["Crayon", "Spoon", "Key", "Worm", "Toothbrush", "Sock", "Peanut"]
    return ("Long or short?", "Long things stretch far. Short things are tiny.",
            [sort(["Long", "Short"], shuffled(r, [(x, 0) for x in r.sample(longs, 3)] + [(x, 1) for x in r.sample(shorts, 3)])) for _ in range(N)])

def c11(r):
    houses = [["triangle", "square"], ["triangle", "square", "rect"], ["square", "triangle", "circle"]]
    rounds = []
    for i in range(N):
        parts = [tok(p) for p in r.choice(houses)]
        rounds.append(build(r, "Build the house: roof first, then walls!", ["@triangle"] + [p for p in parts if p != "@triangle"][: 1 + i % 2]))
    return ("Build a house from shapes.", "The roof is a triangle. It goes on top.", rounds)

def c12(r):
    return ("Pop every number 4!", "4 looks like a chair upside down.",
            [pop(r, "4", ["1", "2", "3", "5", "7"], g, 9) for g in [3, 4, 3, 5, 4]])

def c13(r):
    return ("Feed the bear 3 berries.", "Give one berry at a time and count.",
            [count(r, "apple", n, "How many berries does the bear have?", color="purple") for n in [3, 2, 4, 3, 5]])

def c14(r):
    rounds = []
    for s in r.sample(range(1, 7), N):
        rounds.append(pattern(r, [str(s), str(s + 1), str(s + 2)], str(s + 3), [str(s + 1), str(s + 5)], "Which number comes next?"))
    return ("What comes next?", "Count up: 1, 2, 3…", rounds)

def c15(r):
    rounds = []
    for _ in range(N):
        a, b = r.sample(range(2, 7), 2)
        rounds.append(pick(r, "Which tower is taller?", tok("block", "blue", max(a, b)), [tok("block", "blue", min(a, b))]))
    return ("Tall towers", "Taller means more blocks stacked up.", rounds)

def c16(r):
    return ("Count the stars in the sky.", "Point and count. Don't skip any!",
            [count(r, "star", n, "How many stars?") for n in _nums(r, 4, 10, N)])

def c17(r):
    others = ["circle", "square", "rect", "heart", "diamond"]
    return ("Find the triangles in space.", "A triangle has 3 sides and 3 corners.",
            [pick(r, "Which one is a triangle?", tok("triangle", c), [tok(o, c) for o in r.sample(others, 2)]) for c in r.sample(COLORS, N)])

def c18(r):
    return ("Trace the numbers 4, 5 and 6.", "Follow the dots in order.",
            [trace(d, glyph(d)) for d in ["4", "5", "6", "5", "6"]])

def c19(r):
    rounds = []
    for _ in range(N):
        ic = r.sample(["apple", "star", "fish", "duck", "car", "heart"], 3)
        rounds.append(match([(tok(i), tok(i)) for i in ic]))
    return ("Same or different? Find the matching pairs.", "Two cards that look exactly the same are a pair.", rounds)

def c20(r):
    rounds = []
    names = ["duck", "cat", "dog", "car", "fish", "bug"]
    for pos in ["first", "last", "middle", "first", "last"]:
        row = r.sample(names, 3)
        right = {"first": row[0], "last": row[2], "middle": row[1]}[pos]
        q = f"In the line {', '.join(row)}, who is {pos}?"
        rounds.append(pick(r, q, right.capitalize(), [x.capitalize() for x in row if x != right]))
    return ("First, middle or last?", "First is at the front of the line.", rounds)


# ---------------- Explorers 6–8 ----------------
def _arith(r, op, lo, hi):
    a, b = r.randint(lo, hi), r.randint(lo, hi)
    if op == "-":
        a, b = max(a, b), min(a, b)
    v = {"+": a + b, "-": a - b, "×": a * b}[op]
    return a, b, v

def e01(r):
    rounds = []
    for _ in range(N):
        a, b, v = _arith(r, "+", 2, 10)
        rounds.append(pick(r, f"A dino walks {a} steps, then {b} more. How many steps?", str(v), [str(v - 1), str(v + 1), str(v + 2)]))
    return ("Add with dino tracks.", "Start at the bigger number and count on.", rounds)

def e02(r):
    rounds = []
    for _ in range(N):
        a, b, v = _arith(r, "-", 3, 15)
        rounds.append(pick(r, f"There are {a} cookies. You eat {b}. How many are left?", str(v), [str(v + 1), str(v + 2), str(max(0, v - 1))]))
    return ("Take away cookies.", "Count back from the first number.", rounds)

def e03(r):
    rounds = []
    for _ in range(N):
        s, h = r.randint(0, 12), r.randint(2, 7)
        rounds.append(pick(r, f"Start at {s} and hop {h} forward. Where do you land?", str(s + h), [str(s + h - 1), str(s + h + 1), str(s + h + 2)]))
    return ("Hop along the number line.", "Each hop moves one number.", rounds)

def e04(r):
    rounds = []
    for _ in range(N):
        t, o = r.randint(1, 9), r.randint(0, 9)
        rounds.append(pick(r, f"{t} tens and {o} ones make…", str(10 * t + o), [str(10 * o + t) if o else str(t + 1), str(10 * t + o + 10), str(t + o)]))
    return ("Tens and ones blocks", "A ten is a long stick of 10 cubes.", rounds)

def e05(r):
    rounds = []
    for s in r.sample(range(0, 20, 2), N):
        rounds.append(pattern(r, [str(s), str(s + 2), str(s + 4)], str(s + 6), [str(s + 5), str(s + 8)], "Count by 2s. What's next?"))
    return ("Skip count by 2s.", "Jump over one number each time.", rounds)

def e06(r):
    rounds = []
    for _ in range(N):
        a = r.choice([5, 10, 25]); b = r.choice([1, 5, 10])
        v = a + b * 2
        rounds.append(pick(r, f"A sticker costs {a}¢ and two pencils cost {b}¢ each. Total?", f"{v}¢", [f"{a + b}¢", f"{v + 5}¢", f"{v - 1}¢"]))
    return ("Coin shop", "Add the prices one at a time.", rounds)

def e07(r):
    rounds = []
    for h in r.sample(range(1, 13), N):
        half = r.random() < 0.5
        right = f"{h}:30" if half else f"{h}:00"
        q = f"The big hand points to {'6' if half else '12'} and the little hand is near {h}. What time is it?"
        rounds.append(pick(r, q, right, [f"{h}:00" if half else f"{h}:30", f"{(h % 12) + 1}:00", f"6:{h:02d}"]))
    return ("Tell the time.", "The little hand shows the hour.", rounds)

def e08(r):
    rounds = []
    for _ in range(N):
        a, b = r.sample(range(2, 9), 2)
        rounds.append(match([(f"{a} + {b}", str(a + b)), (f"{a + b} − {a}", str(b)), (f"{b} + {a + 1}", str(a + b + 1))]))
    return ("Fact family match", "Adding and taking away are opposites.", rounds)

def e09(r):
    rounds = []
    for _ in range(N):
        ns = r.sample(range(1, 40), 6)
        rounds.append(sort(["Even", "Odd"], [(str(n), n % 2) for n in ns]))
    return ("Even or odd?", "Even numbers end in 0, 2, 4, 6 or 8.", rounds)

def e10(r):
    things = [("pencil", 6), ("crayon", 3), ("book", 9), ("spoon", 5), ("shoe", 8), ("key", 2), ("toy car", 4)]
    rounds = []
    for name, n in r.sample(things, N):
        rounds.append(pick(r, f"How many paperclips long is the {name}? (It lines up with {n} clips.)", str(n), [str(n + 1), str(n + 3), str(max(1, n - 2))]))
    return ("Measure with paperclips.", "Line the clips up with no gaps.", rounds)

def e11(r):
    qs = [("A pizza cut into 2 equal parts. One part is…", "one half", ["one quarter", "one third"]),
          ("A pizza cut into 4 equal parts. One part is…", "one quarter", ["one half", "one third"]),
          ("How many quarters make a whole pizza?", "4", ["2", "3"]),
          ("How many halves make a whole?", "2", ["4", "3"]),
          ("Which is bigger: one half or one quarter?", "one half", ["one quarter"]),
          ("2 quarters are the same as…", "one half", ["one whole", "one third"])]
    return ("Half and quarter pizza", "Equal parts must be the same size.", [pick(r, q, a, w) for q, a, w in r.sample(qs, N)])

def e12(r):
    shapes = [("triangle", 3), ("square", 4), ("rect", 4), ("diamond", 4), ("star", 10)]
    rounds = []
    for name, n in shapes:
        rounds.append(count(r, name, n, f"How many sides does this shape have?") if False else pick(r, f"How many sides does a {name if name != 'rect' else 'rectangle'} have?", str(n), [str(n + 1), str(max(1, n - 1)), str(n + 2)], icon=name))
    return ("Count the shape sides.", "Trace each side with your finger.", rounds)

def e13(r):
    rounds = []
    for _ in range(N):
        a, b = r.randint(2, 12), r.randint(2, 9)
        rounds.append(pick(r, f"{a} + ? = {a + b}", str(b), [str(b + 1), str(max(0, b - 1)), str(a + b)]))
    return ("Find the missing number.", "Count up from the first number to the total.", rounds)

def e14(r):
    pets = ["cats", "dogs", "fish", "birds", "rabbits"]
    rounds = []
    for _ in range(N):
        ps = r.sample(pets, 3); vals = r.sample(range(2, 10), 3)
        desc = ", ".join(f"{p}: {v}" for p, v in zip(ps, vals))
        best = ps[vals.index(max(vals))]
        rounds.append(pick(r, f"The class graph shows {desc}. Which pet is most popular?", best, [p for p in ps if p != best]))
    return ("Read the bar graph of pets.", "The tallest bar is the biggest number.", rounds)

def e15(r):
    rounds = []
    for n in r.sample(range(2, 11), N):
        others = [str(x) for x in range(2, 23) if x != 2 * n]
        rounds.append(pop(r, str(2 * n), r.sample(others, 5), 3, 9) | {"q": f"Pop the double of {n}!"})
    return ("Double it!", "Double means add the number to itself.", rounds)

def e16(r):
    rounds = []
    for _ in range(N):
        a, b = r.sample(range(10, 100), 2)
        rounds.append(pick(r, f"Which is bigger: {a} or {b}?", str(max(a, b)), [str(min(a, b))]))
    return ("Bigger number wins.", "Compare the tens first.", rounds)

def e17(r):
    qs = []
    for _ in range(N):
        a, b = r.randint(3, 12), r.randint(2, 9)
        kind = r.choice(["more", "left"])
        if kind == "more":
            qs.append(pick(r, f"Avi has {a} acorns and finds {b} more. How many now?", str(a + b), [str(a + b - 1), str(a + b + 2), str(a)]))
        else:
            a = a + b
            qs.append(pick(r, f"Avi baked {a} muffins and gave away {b}. How many are left?", str(a - b), [str(a - b + 1), str(a + b), str(b)]))
    return ("Word problems with Avi", "Find the numbers, then decide: add or take away?", qs)

def e18(r):
    rounds = []
    for shape in r.sample(["circle", "heart", "triangle", "diamond", "star", "square"], N):
        c, c2 = r.sample(COLORS, 2)
        other = r.choice([x for x in ["circle", "heart", "triangle", "diamond", "star", "square"] if x != shape])
        rounds.append(pick(r, "The left wing is this. Which right wing makes the butterfly match?", tok(shape, c), [tok(shape, c2), tok(other, c)], icon=shape))
    return ("Symmetry butterflies", "Both wings must match like a mirror: same shape, same color.", rounds)


def e19(r):
    return ("Skip count by 5s to the beat.", "5, 10, 15… tap on each beat.", [rhythm(r, 3, 3 + i) for i in range(N)])

def e20(r):
    rounds = []
    for _ in range(N):
        a, b = r.randint(2, 10), r.randint(2, 10)
        others = [str(x) for x in range(2, 21) if x != a + b]
        rounds.append(pop(r, str(a + b), r.sample(others, 5), 3, 9) | {"q": f"Pop {a} + {b}!"})
    return ("Speed sums", "Know your facts? Go fast!", rounds)


# ---------------- Trailblazers 9–12 ----------------
def t01(r):
    rounds = []
    for _ in range(N):
        a, b = r.randint(3, 12), r.randint(3, 12)
        others = [str(x) for x in r.sample(range(9, 145), 12) if x != a * b]
        rounds.append(pop(r, str(a * b), others[:5], 3, 9) | {"q": f"Pop {a} × {b}!"})
    return ("Times tables race", "Use a fact you know: 7 × 8 = 7 × 4 × 2.", rounds)

def t02(r):
    rounds = []
    for _ in range(N):
        b, v = r.randint(3, 9), r.randint(3, 12)
        rounds.append(pick(r, f"{b * v} stickers shared equally by {b} friends. Each gets?", str(v), [str(v + 1), str(v - 1), str(b)]))
    return ("Division sharing", "Division is sharing into equal groups.", rounds)

def t03(r):
    qs = [("3/8 + 2/8 =", "5/8", ["5/16", "1/8", "6/8"]), ("Which is larger: 2/3 or 3/5?", "2/3", ["3/5", "They are equal"]),
          ("1/2 of 18 slices is…", "9", ["6", "12", "8"]), ("3/4 − 1/4 =", "1/2", ["2/0", "1/4", "3/8"]),
          ("Simplify 6/8", "3/4", ["2/3", "6/4", "1/2"]), ("2/5 of 20 is…", "8", ["4", "10", "5"])]
    return ("Fraction pizza party", "Same bottom number? Just add the tops.", [pick(r, q, a, w) for q, a, w in r.sample(qs, N)])

def t04(r):
    rounds = []
    for _ in range(N):
        a = round(r.uniform(0.1, 9.9), 1); b = round(a + r.choice([0.1, 0.2, 0.5]), 1)
        rounds.append(pick(r, f"Which is greater: {a} or {b}?", str(b), [str(a)]))
    return ("Decimal number line", "Compare the tenths after the point.", rounds)

def t05(r):
    rounds = []
    for _ in range(N):
        w, h = r.randint(3, 12), r.randint(3, 9)
        rounds.append(pick(r, f"A room is {w} m by {h} m. What is its area?", f"{w * h} m²", [f"{2 * (w + h)} m²", f"{w + h} m²", f"{w * h + w} m²"]))
    return ("Area of rooms", "Area = length × width.", rounds)

def t06(r):
    rounds = []
    for _ in range(N):
        w, h = r.randint(4, 20), r.randint(3, 15)
        rounds.append(pick(r, f"How much fence goes around a {w} m by {h} m garden?", f"{2 * (w + h)} m", [f"{w * h} m", f"{w + h} m", f"{2 * w + h} m"]))
    return ("Perimeter fences", "Perimeter = add all the sides.", rounds)

def t07(r):
    qs = [("An angle smaller than 90° is…", "acute", ["obtuse", "right", "straight"]), ("An angle of exactly 90° is…", "a right angle", ["acute", "obtuse"]),
          ("An angle between 90° and 180° is…", "obtuse", ["acute", "right"]), ("A straight line makes an angle of…", "180°", ["90°", "360°"]),
          ("The angles in a triangle add up to…", "180°", ["90°", "360°", "270°"]), ("A full turn is…", "360°", ["180°", "90°"])]
    return ("Angle detective", "Compare to the corner of a page: that's 90°.", [pick(r, q, a, w) for q, a, w in r.sample(qs, N)])

def t08(r):
    rounds = []
    for _ in range(N):
        a, b, c = r.randint(2, 9), r.randint(2, 6), r.randint(2, 6)
        v = a + b * c
        rounds.append(pick(r, f"{a} + {b} × {c} =", str(v), [str((a + b) * c), str(v + 1), str(a * b + c)]))
    return ("Order of operations", "Multiply before you add.", rounds)

def t09(r):
    rounds = []
    for _ in range(N):
        p = r.choice([10, 20, 25, 50]); price = r.choice([20, 40, 60, 80, 100])
        off = price * p // 100
        rounds.append(pick(r, f"A ${price} game is {p}% off. New price?", f"${price - off}", [f"${off}", f"${price - p}", f"${price - off + 5}"]))
    return ("Percent sale", "10% is one tenth of the price.", rounds)

def t10(r):
    rounds = []
    for _ in range(N):
        a, b, k = r.randint(1, 4), r.randint(2, 6), r.randint(2, 5)
        rounds.append(pick(r, f"Pancakes use {a} cup of milk for every {b} cups of flour. With {b * k} cups of flour, how much milk?", f"{a * k} cups", [f"{a + k} cups", f"{b * k} cups", f"{a * k + 1} cups"]))
    return ("Ratio recipes", "Scale both parts by the same number.", rounds)

def t11(r):
    rounds = []
    for _ in range(N):
        x, y = r.randint(0, 9), r.randint(0, 9)
        rounds.append(pick(r, f"The treasure is {x} steps right and {y} steps up from (0,0). Its coordinates?", f"({x},{y})", [f"({y},{x})" if x != y else f"({x + 1},{y})", f"({x},{y + 1})", f"({x - 1},{y})"]))
    return ("Coordinate treasure map", "Go along the corridor, then up the stairs: (x, y).", rounds)

def t12(r):
    rounds = []
    for kind in ["mean", "median", "mode", "mean", "median"]:
        if kind == "mean":
            v, o = r.randint(5, 15), r.randint(1, 4)
            nums = shuffled(r, [v - o, v + o, v - 1, v + 1])
        elif kind == "median":
            nums = sorted(r.sample(range(1, 30), 5)); v = nums[2]; nums = shuffled(r, nums)
        else:
            base = r.sample(range(1, 20), 3); v = base[0]; nums = shuffled(r, base + [v])
        rounds.append(pick(r, f"Find the {kind} of {', '.join(map(str, nums))}.", str(v), [str(v + 1), str(max(nums)), str(min(nums))]))
    return ("Mean, median, mode", "Median is the middle once they are in order. Mode is the most common.", rounds)


def t13(r):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    rounds = []
    for _ in range(N):
        p = r.choice(primes)
        rounds.append(pop(r, str(p), [str(x) for x in r.sample([4, 6, 8, 9, 10, 12, 14, 15, 16, 21, 25, 27], 5)], 3, 9) | {"q": f"Pop the prime number {p}!"})
    return ("Prime number hunt", "A prime has exactly two factors: 1 and itself.", rounds)

def t14(r):
    rounds = []
    for _ in range(N):
        d, q = r.randint(3, 9), r.randint(12, 99)
        rounds.append(pick(r, f"{d * q} ÷ {d} =", str(q), [str(q + 1), str(q - 1), str(q + 10)]))
    return ("Long division steps", "Divide, multiply, subtract, bring down.", rounds)

def t15(r):
    rounds = []
    for _ in range(N):
        a, b, c = r.randint(2, 8), r.randint(2, 6), r.randint(2, 5)
        rounds.append(pick(r, f"Volume of a box {a} × {b} × {c} cm?", f"{a * b * c} cm³", [f"{a + b + c} cm³", f"{a * b} cm³", f"{a * b * c + a} cm³"]))
    return ("Volume of boxes", "Volume = length × width × height.", rounds)

def t16(r):
    rounds = []
    for _ in range(N):
        t, d = r.randint(-8, 6), r.randint(3, 10)
        rounds.append(pick(r, f"It is {t}°C and the temperature drops {d}°. Now?", f"{t - d}°C", [f"{t + d}°C", f"{d - t}°C", f"{t - d + 1}°C"]))
    return ("Negative numbers thermometer", "Going down past zero makes negative numbers.", rounds)

def t17(r):
    rounds = []
    for _ in range(N):
        bases = r.sample([(1, 2), (1, 3), (2, 3), (1, 4), (3, 4), (2, 5)], 3)
        rounds.append(match([(f"{a}/{b}", f"{a * k}/{b * k}") for (a, b), k in zip(bases, r.sample([2, 3, 4], 3))]))
    return ("Equivalent fractions", "Multiply top and bottom by the same number.", rounds)

def t18(r):
    items = [("rocket fuel", 40), ("space suit", 25), ("snacks", 10), ("telescope", 30), ("map", 5), ("tent", 20)]
    rounds = []
    for _ in range(N):
        chosen = r.sample(items, 3); total = sum(v for _, v in chosen)
        rounds.append(pick(r, "Budget: " + ", ".join(f"{n} ${v}" for n, v in chosen) + ". Total cost?", f"${total}", [f"${total - 5}", f"${total + 10}", f"${total + 5}"]))
    return ("Budget a space trip", "Add the biggest numbers first.", rounds)

def t19(r):
    rounds = []
    for _ in range(N):
        a, d = r.randint(1, 9), r.randint(2, 7)
        seq = [str(a + d * i) for i in range(4)]
        rounds.append(pattern(r, seq, str(a + 4 * d), [str(a + 4 * d + 1), str(a + 3 * d + 1)], f"What's the rule's next number?"))
    return ("Find the pattern rule", "How much does it grow each step?", rounds)

def t20(r):
    rounds = []
    for _ in range(N):
        a, b = r.randint(11, 49), r.randint(11, 49)
        rounds.append(pick(r, f"Quick! {a} + {b} =", str(a + b), [str(a + b + 10), str(a + b - 1), str(a + b + 1)]))
    return ("Mental math sprint", "Add the tens, then the ones.", rounds)


GEN = {
    "cubs": [c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20],
    "explorers": [e01, e02, e03, e04, e05, e06, e07, e08, e09, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20],
    "trailblazers": [t01, t02, t03, t04, t05, t06, t07, t08, t09, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20],
}
