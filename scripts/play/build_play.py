"""Build content/play.json: playable rounds for every activity in content/activities.json.

    python scripts/play/build_play.py

Each world module (w_<world>.py) has GEN[band] = 20 functions returning
(prompt, tip, rounds). The engine of each round is inferred from its shape, and the
activity's engine is the one most of its rounds use. If that differs from the
catalog, content/engine_overrides.json is updated and the catalog rebuilt so both agree.
"""
import collections
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))

import common  # noqa: E402
import w_creativity, w_feelings, w_logic, w_math, w_memory, w_reading, w_science, w_wiggle  # noqa: E402

WORLDS = {"math": w_math, "reading": w_reading, "science": w_science, "feelings": w_feelings,
          "logic": w_logic, "memory": w_memory, "creativity": w_creativity, "wiggle": w_wiggle}
FREE_HINTS = ("your order", "favourite order", "for you", "choose your order", "you'd add first", "you'd build first", "rank them")


def engine_of(rd):
    if "speed" in rd: return "motion"
    if "pads" in rd: return "rhythm"
    if "word" in rd and "guesses" in rd: return "draw"
    if "dots" in rd: return "trace"
    if "bubbles" in rd: return "pop"
    if "grid" in rd: return "changed"
    if "scene" in rd: return "choice"
    if "pieces" in rd: return "build"
    if "bins" in rd: return "sort"
    if "pairs" in rd: return "match"
    if "seq" in rd and "choices" in rd: return "pattern"
    if "say" in rd: return "sound"
    if "icon" in rd and "n" in rd: return "count"
    if "choices" in rd: return "pick"
    raise ValueError(f"unknown round shape: {sorted(rd)}")


def main():
    cat = json.loads((ROOT / "content" / "activities.json").read_text(encoding="utf-8"))
    ov_path = ROOT / "content" / "engine_overrides.json"
    old = json.loads(ov_path.read_text(encoding="utf-8")) if ov_path.exists() else {}
    out, overrides = [], dict(old)
    for a in cat["activities"]:
        fn = WORLDS[a["world"]].GEN[a["band"]][a["order"] - 1]
        prompt, tip, rounds = fn(common.rng(a["id"]))
        for rd in rounds:
            rd["engine"] = engine_of(rd)
            if rd["engine"] == "build" and any(h in rd["q"].lower() for h in FREE_HINTS):
                rd["free"] = True
            if rd["engine"] == "pick" and rd.get("q", "").startswith(("Mirror me", "The left wing")):
                rd["show"] = [rd["choices"][rd["answer"]]]
                rd.pop("icon", None)
        engine = collections.Counter(rd["engine"] for rd in rounds).most_common(1)[0][0]
        if engine != a["engine"]:
            overrides[a["id"]] = engine
        out.append({"id": a["id"], "world": a["world"], "band": a["band"], "order": a["order"], "title": a["title"],
                    "skill": a["skill"], "engine": engine, "prompt": prompt, "tip": tip, "rounds": rounds})
    if overrides != old:
        ov_path.write_text(json.dumps(overrides, indent=1, sort_keys=True), encoding="utf-8")
        subprocess.run([sys.executable, str(ROOT / "scripts" / "build_catalog.py")], check=True)
    play = {"version": 1, "icons": common.ICONS, "activities": out}
    (ROOT / "content" / "play.json").write_text(json.dumps(play, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    n_rounds = sum(len(a["rounds"]) for a in out)
    print(f"play.json: {len(out)} activities, {n_rounds} rounds, {len(overrides)} engine overrides (catalog engines match play)")


if __name__ == "__main__":
    main()
