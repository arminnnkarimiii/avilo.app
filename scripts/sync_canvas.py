"""Copy the canvas working folder into the repo so it can be reviewed and verified.

    python scripts/sync_canvas.py <canvas-project-folder>

Writes design/canvas.json and design/screens/NN-<slug>.html in canvas order,
and removes screen files that are no longer on the canvas.
"""
import json
import pathlib
import re
import shutil
import sys

src = pathlib.Path(sys.argv[1])
repo = pathlib.Path(__file__).resolve().parent.parent
out = repo / "design" / "screens"
out.mkdir(parents=True, exist_ok=True)
canvas = json.loads((src / "canvas.json").read_text(encoding="utf-8"))
shutil.copyfile(src / "canvas.json", repo / "design" / "canvas.json")

def slug(title):
    t = re.sub(r"^\d+\s*·\s*", "", title).lower()
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t[:40].strip("-")

wanted = set()
for i, f in enumerate(canvas["order"], 1):
    name = f"{i:02d}-{slug(canvas['boards'][f].get('title', f))}.html"
    wanted.add(name)
    shutil.copyfile(src / f, out / name)
for old in out.glob("*.html"):
    if old.name not in wanted:
        old.unlink()
print(f"synced {len(wanted)} screens")
