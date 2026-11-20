"""Shared builders for playable activity content (content/play.json).

Every builder returns one *round* in the exact shape the game screen renders.
Tokens: plain text, or "@icon", "@icon:color", "@icon*3" (three of the icon),
"@icon:color*3". Icons must be in ICONS (the game screen draws each one).
"""
import math
import random

ICONS = ["apple", "star", "egg", "fish", "car", "ball", "flower", "heart", "rocket", "dino", "cat", "dog",
         "sun", "moon", "tree", "leaf", "duck", "cookie", "balloon", "shell", "block", "bug", "cloud", "drop",
         "house", "circle", "square", "triangle", "rect", "diamond", "bell", "drum", "book", "cup", "key", "planet"]
COLORS = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown"]


def rng(seed):
    return random.Random(seed)


def shuffled(r, items):
    items = list(items)
    r.shuffle(items)
    return items


def tok(icon, color=None, k=None):
    assert icon in ICONS, icon
    s = "@" + icon
    if color:
        s += ":" + color
    if k:
        s += "*" + str(k)
    return s


def pick(r, q, right, wrongs, icon=None, n_choices=None):
    wrongs = [w for w in dict.fromkeys(wrongs) if w != right]
    if n_choices:
        wrongs = wrongs[: n_choices - 1]
    opts = shuffled(r, [right] + wrongs)
    out = {"q": q, "choices": opts, "answer": opts.index(right)}
    if icon:
        out["icon"] = icon
    return out


def sound(r, say, right, wrongs, q=None):
    d = pick(r, q or "Listen and choose.", right, wrongs)
    d["say"] = say
    return d


def count(r, icon, n, q=None, color=None):
    opts = sorted({n, max(1, n - 1), n + 1} if n > 1 else {1, 2, 3})
    if len(opts) < 3:
        opts = [1, 2, 3]
    opts = shuffled(r, [str(o) for o in opts])
    d = {"q": q or f"How many {icon}s?", "icon": icon, "n": n, "choices": opts, "answer": opts.index(str(n))}
    if color:
        d["color"] = color
    return d


def sort(bins, items):
    return {"bins": list(bins), "items": [list(i) for i in items]}


def match(pairs):
    return {"pairs": [list(p) for p in pairs]}


def pattern(r, seq, right, wrongs, q="What comes next?"):
    d = pick(r, q, right, wrongs)
    d["seq"] = list(seq)
    return d


def build(r, q, answer):
    pieces = list(answer)
    for _ in range(10):
        r.shuffle(pieces)
        if pieces != list(answer):
            break
    return {"q": q, "pieces": pieces, "answer": list(answer)}


def choice(scene, options):
    return {"scene": scene, "options": [{"t": t, "ok": ok, "why": why} for t, ok, why in options]}


def changed(r, pool, size, q="What changed?"):
    grid = r.sample(pool, size)
    idx = r.randrange(size)
    swap = r.choice([p for p in pool if p not in grid] or [p for p in ICONS if p not in grid])
    return {"q": q, "grid": grid, "idx": idx, "swap": swap}


def pop(r, target, others, goal, total):
    bubbles = [target] * goal + [r.choice(others) for _ in range(total - goal)]
    return {"target": target, "goal": goal, "bubbles": shuffled(r, bubbles)}


def trace(label, dots):
    return {"label": label, "dots": [[round(x, 1), round(y, 1)] for x, y in dots]}


def draw(word, wrong_guesses):
    return {"word": word, "guesses": list(wrong_guesses) + [word]}


def rhythm(r, pads, length):
    return {"pads": pads, "seq": [r.randrange(pads) for _ in range(length)]}


def motion(q, speed, zone):
    return {"q": q, "speed": speed, "zone": zone}


# ---- stroke paths for tracing (0–100 grid, one continuous path each) ----
GLYPHS = {
    "A": [(20, 90), (50, 10), (80, 90), (65, 55), (35, 55)],
    "B": [(25, 90), (25, 10), (60, 10), (72, 25), (60, 48), (25, 48), (65, 50), (78, 70), (65, 90), (25, 90)],
    "C": [(78, 22), (60, 10), (35, 14), (22, 35), (22, 65), (35, 86), (60, 90), (78, 78)],
    "D": [(25, 90), (25, 10), (55, 12), (75, 30), (78, 55), (70, 78), (50, 90), (25, 90)],
    "E": [(75, 10), (25, 10), (25, 50), (65, 50), (25, 50), (25, 90), (75, 90)],
    "F": [(75, 10), (25, 10), (25, 50), (62, 50), (25, 50), (25, 90)],
    "G": [(78, 22), (58, 10), (32, 15), (22, 40), (24, 68), (40, 88), (64, 88), (78, 72), (78, 55), (55, 55)],
    "H": [(25, 10), (25, 90), (25, 50), (75, 50), (75, 10), (75, 90)],
    "I": [(35, 10), (65, 10), (50, 10), (50, 90), (35, 90), (65, 90)],
    "J": [(70, 10), (70, 70), (60, 88), (40, 90), (25, 75)],
    "K": [(25, 10), (25, 90), (25, 55), (72, 10), (40, 42), (75, 90)],
    "L": [(28, 10), (28, 90), (75, 90)],
    "M": [(18, 90), (22, 10), (50, 60), (78, 10), (82, 90)],
    "N": [(25, 90), (25, 10), (75, 90), (75, 10)],
    "O": [(50, 10), (25, 22), (18, 50), (25, 78), (50, 90), (75, 78), (82, 50), (75, 22), (50, 10)],
    "P": [(25, 90), (25, 10), (62, 10), (75, 25), (62, 48), (25, 48)],
    "Q": [(50, 10), (25, 22), (18, 50), (25, 78), (50, 90), (75, 78), (82, 50), (75, 22), (50, 10), (60, 70), (82, 92)],
    "R": [(25, 90), (25, 10), (62, 10), (75, 25), (62, 48), (25, 48), (75, 90)],
    "S": [(75, 20), (55, 10), (32, 14), (25, 30), (40, 46), (62, 54), (75, 70), (65, 88), (40, 90), (22, 80)],
    "T": [(20, 10), (80, 10), (50, 10), (50, 90)],
    "U": [(25, 10), (25, 70), (35, 88), (50, 92), (65, 88), (75, 70), (75, 10)],
    "V": [(20, 10), (50, 90), (80, 10)],
    "W": [(15, 10), (32, 90), (50, 40), (68, 90), (85, 10)],
    "X": [(22, 10), (78, 90), (50, 50), (78, 10), (22, 90)],
    "Y": [(22, 10), (50, 48), (78, 10), (50, 48), (50, 90)],
    "Z": [(22, 10), (78, 10), (22, 90), (78, 90)],
    "a": [(70, 50), (55, 40), (35, 45), (28, 65), (40, 85), (60, 82), (70, 65), (70, 45), (72, 90)],
    "0": [(50, 10), (28, 25), (22, 50), (28, 75), (50, 90), (72, 75), (78, 50), (72, 25), (50, 10)],
    "1": [(35, 25), (52, 10), (52, 90), (35, 90), (68, 90)],
    "2": [(25, 28), (40, 12), (62, 12), (74, 30), (65, 50), (25, 90), (78, 90)],
    "3": [(25, 18), (50, 10), (72, 22), (68, 42), (45, 50), (70, 60), (74, 78), (52, 90), (25, 82)],
    "4": [(62, 90), (62, 10), (20, 65), (82, 65)],
    "5": [(72, 10), (32, 10), (28, 45), (52, 40), (72, 52), (74, 75), (55, 90), (28, 84)],
    "6": [(70, 15), (48, 10), (28, 30), (24, 62), (36, 86), (58, 90), (74, 72), (66, 52), (44, 48), (26, 62)],
    "7": [(22, 10), (78, 10), (40, 90)],
    "8": [(50, 48), (30, 35), (35, 15), (50, 10), (65, 15), (70, 35), (50, 48), (26, 65), (32, 86), (50, 90), (68, 86), (74, 65), (50, 48)],
    "9": [(72, 38), (60, 50), (38, 48), (26, 30), (40, 12), (62, 12), (74, 30), (70, 65), (55, 90), (30, 86)],
}


def glyph(ch):
    return GLYPHS[ch]


def wave(n=9, amp=25, cycles=1.5):
    return [(8 + 84 * i / (n - 1), 50 + amp * math.sin(i / (n - 1) * cycles * 2 * math.pi)) for i in range(n)]


def zigzag(n=8, amp=30):
    return [(8 + 84 * i / (n - 1), 50 + (amp if i % 2 else -amp)) for i in range(n)]


def spiral(n=12, turns=1.6):
    pts = []
    for i in range(n):
        a = i / (n - 1) * turns * 2 * math.pi
        rad = 8 + 38 * i / (n - 1)
        pts.append((50 + rad * math.cos(a), 50 + rad * math.sin(a)))
    return pts


def shape_path(name):
    return {
        "star": [(50, 8), (61, 38), (93, 38), (67, 57), (77, 88), (50, 69), (23, 88), (33, 57), (7, 38), (39, 38), (50, 8)],
        "heart": [(50, 88), (14, 52), (12, 28), (28, 14), (50, 26), (72, 14), (88, 28), (86, 52), (50, 88)],
        "house": [(15, 90), (15, 45), (50, 12), (85, 45), (85, 90), (15, 90)],
        "fish": [(10, 50), (35, 28), (65, 30), (80, 50), (65, 70), (35, 72), (10, 50), (90, 30), (90, 70), (80, 50)],
        "boat": [(10, 60), (90, 60), (75, 85), (25, 85), (10, 60), (50, 60), (50, 12), (80, 50), (50, 50)],
        "triangle": [(50, 12), (88, 85), (12, 85), (50, 12)],
        "square": [(18, 18), (82, 18), (82, 82), (18, 82), (18, 18)],
        "circle": [(50 + 38 * math.cos(a * math.pi / 6), 50 + 38 * math.sin(a * math.pi / 6)) for a in range(13)],
        "rocket": [(50, 8), (66, 30), (66, 70), (80, 88), (50, 78), (20, 88), (34, 70), (34, 30), (50, 8)],
        "moon": [(62, 10), (35, 20), (24, 50), (35, 80), (62, 90), (45, 70), (42, 50), (45, 30), (62, 10)],
        "flower": [(50, 50), (50, 15), (62, 38), (85, 50), (62, 62), (50, 85), (38, 62), (15, 50), (38, 38), (50, 15)],
        "lightning": [(60, 8), (30, 52), (52, 52), (40, 92), (72, 42), (50, 42), (60, 8)],
    }[name]


def round_robin(r, pool, k):
    """k distinct items from pool, in random order."""
    return r.sample(pool, min(k, len(pool)))


def uniq_pairs(r, pool, k):
    """k pairs from pool where no word appears in two pairs."""
    for _ in range(200):
        ch = r.sample(pool, k)
        sides = [x for p in ch for x in p]
        if len(set(sides)) == len(sides):
            return ch
    raise ValueError("cannot pick unique pairs")
