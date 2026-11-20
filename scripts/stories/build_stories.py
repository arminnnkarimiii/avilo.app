"""Build content/stories.json from the book modules.

    python scripts/stories/build_stories.py

Text placeholders ({name}, {he}, {him}, {his}, {He}, {His}) are filled by the
story reader from the child's profile. Every page with an illustration has a
scene the reader draws as layered vector art (sky, ground, props).
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import books_cubs, books_explorers, books_trailblazers  # noqa: E402

books = []
for mod in (books_cubs, books_explorers, books_trailblazers):
    for b in mod.BOOKS:
        pages = []
        for text, scene in b["pages"]:
            p = {"t": text}
            if scene:
                sky, ground, props = scene
                p["scene"] = {"sky": sky, "ground": ground, "props": [{"k": k, "x": x, "y": y, "s": s} for k, x, y, s in props]}
            pages.append(p)
        books.append({**{k: v for k, v in b.items() if k != "pages"}, "pages": pages})

out = HERE.parent.parent / "content" / "stories.json"
out.write_text(json.dumps({"version": 1, "books": books}, ensure_ascii=False, indent=1), encoding="utf-8")
print(out, len(books), "books,", sum(len(b["pages"]) for b in books), "pages,", sum(1 for b in books for p in b["pages"] if "scene" in p), "illustrations")
