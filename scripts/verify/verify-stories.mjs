// G3: story library completeness and drawability.
import { readJSON, screen, split, problem, finish, fail } from './lib.mjs';

const lib = readJSON('content/stories.json');
const LEN = { cubs: 10, explorers: 16, trailblazers: 24 };
const reader = screen('-story-book');
const { markup } = split(reader.text);
const drawable = new Set([...markup.matchAll(/data-kind="([a-z-]+)"/g)].map((m) => m[1]));
const skies = new Set([...markup.matchAll(/data-sky="([a-z-]+)"/g)].map((m) => m[1]));
const grounds = new Set([...markup.matchAll(/data-ground="([a-z-]+)"/g)].map((m) => m[1]));
if (drawable.size < 15) problem(`reader draws only ${drawable.size} prop kinds`);
const books = lib.books || [];
for (const band of Object.keys(LEN)) {
  const n = books.filter((b) => b.band === band).length;
  if (n < 3) problem(`${band}: ${n} books, need 3`);
}
const ids = new Set();
for (const b of books) {
  if (ids.has(b.id)) problem(`duplicate book id ${b.id}`);
  ids.add(b.id);
  if (!b.title || !b.title.includes('{name}')) problem(`${b.id}: title must star the child ({name})`);
  if (!Array.isArray(b.tags) || !b.tags.length) problem(`${b.id}: no interest tags`);
  if (!LEN[b.band]) { problem(`${b.id}: bad band`); continue; }
  if (b.pages.length !== LEN[b.band]) problem(`${b.id}: ${b.pages.length} pages, need ${LEN[b.band]}`);
  b.pages.forEach((p, i) => {
    const words = (p.t || '').trim().split(/\s+/).length;
    if (words < 8) problem(`${b.id} p${i + 1}: text too short (${words} words)`);
    const needArt = i % 2 === 0;
    if (needArt && !p.scene) problem(`${b.id} p${i + 1}: missing illustration`);
    if (p.scene) {
      if (!skies.has(p.scene.sky)) problem(`${b.id} p${i + 1}: sky ${p.scene.sky} not drawable`);
      if (!grounds.has(p.scene.ground)) problem(`${b.id} p${i + 1}: ground ${p.scene.ground} not drawable`);
      if (!Array.isArray(p.scene.props) || p.scene.props.length < 2) problem(`${b.id} p${i + 1}: scene needs ≥2 props`);
      for (const pr of p.scene.props || []) if (!drawable.has(pr.k)) problem(`${b.id} p${i + 1}: prop ${pr.k} not drawable`);
    }
  });
}
if (books.length < 9) fail(`only ${books.length} books`);
finish(`STORIES OK ${books.length} books`);
