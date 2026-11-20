// G1: every catalog activity has its own valid playable content in content/play.json.
import { readJSON, problem, finish, fail } from './lib.mjs';

const cat = readJSON('content/activities.json');
const play = readJSON('content/play.json');
if (!Array.isArray(cat.activities) || cat.activities.length !== 480) fail(`catalog has ${cat.activities?.length} activities, expected 480`);
const byId = new Map((play.activities || []).map((a) => [a.id, a]));
const ICONS = new Set(play.icons || []);
const isInt = (n) => Number.isInteger(n);
const str = (s) => typeof s === 'string' && s.trim().length > 0;
const token = (t) => {
  if (!str(t)) return false;
  if (!t.startsWith('@')) return true;
  const name = t.slice(1).split(/[:*]/)[0];
  return ICONS.has(name);
};
const choices = (r, id, min = 2) => {
  if (!Array.isArray(r.choices) || r.choices.length < min) return problem(`${id}: needs ≥${min} choices`);
  if (!r.choices.every(token)) problem(`${id}: bad choice token ${JSON.stringify(r.choices)}`);
  if (new Set(r.choices).size !== r.choices.length) problem(`${id}: duplicate choices`);
  if (!isInt(r.answer) || r.answer < 0 || r.answer >= r.choices.length) problem(`${id}: answer out of range`);
};
const minRounds = { draw: 3, rhythm: 3, motion: 3 };
const check = {
  count: (r, id) => { if (!ICONS.has(r.icon)) problem(`${id}: unknown icon ${r.icon}`); if (!isInt(r.n) || r.n < 1 || r.n > 20) problem(`${id}: bad n`); choices(r, id, 3); if (r.choices[r.answer] !== String(r.n)) problem(`${id}: answer is not n`); },
  pick: (r, id) => { if (!str(r.q)) problem(`${id}: missing q`); choices(r, id); },
  sound: (r, id) => { if (!str(r.say)) problem(`${id}: missing say`); choices(r, id); },
  pattern: (r, id) => { if (!Array.isArray(r.seq) || r.seq.length < 3 || !r.seq.every(token)) problem(`${id}: bad seq`); choices(r, id); },
  match: (r, id) => { if (!Array.isArray(r.pairs) || r.pairs.length < 3 || !r.pairs.every((p) => p.length === 2 && p.every(token))) problem(`${id}: bad pairs`); const flat = (r.pairs || []).flatMap((p) => (p[0] === p[1] ? [p[0]] : p)); if (new Set(flat).size !== flat.length) problem(`${id}: a card appears in two different pairs`); },
  sort: (r, id) => { if (!Array.isArray(r.bins) || r.bins.length < 2 || !r.bins.every(str)) problem(`${id}: bad bins`); if (!Array.isArray(r.items) || r.items.length < 4 || !r.items.every((it) => token(it[0]) && isInt(it[1]) && it[1] >= 0 && it[1] < r.bins.length)) problem(`${id}: bad items`); },
  build: (r, id) => { if (!str(r.q)) problem(`${id}: missing q`); if (!Array.isArray(r.answer) || r.answer.length < 2 || !r.answer.every(token)) problem(`${id}: bad answer order`); if (!Array.isArray(r.pieces) || [...r.pieces].sort().join('|') !== [...r.answer].sort().join('|')) problem(`${id}: pieces must be the answer shuffled`); },
  choice: (r, id) => { if (!str(r.scene)) problem(`${id}: missing scene`); if (!Array.isArray(r.options) || r.options.length < 2 || !r.options.every((o) => str(o.t) && str(o.why) && typeof o.ok === 'boolean')) problem(`${id}: bad options`); else if (!r.options.some((o) => o.ok)) problem(`${id}: no good option`); },
  changed: (r, id) => { if (!Array.isArray(r.grid) || r.grid.length < 4 || !r.grid.every((g) => ICONS.has(g))) problem(`${id}: bad grid`); if (!isInt(r.idx) || r.idx < 0 || r.idx >= (r.grid || []).length) problem(`${id}: bad idx`); if (!ICONS.has(r.swap) || r.swap === (r.grid || [])[r.idx]) problem(`${id}: bad swap`); },
  pop: (r, id) => { if (!token(r.target)) problem(`${id}: bad target`); if (!Array.isArray(r.bubbles) || r.bubbles.length < 6 || !r.bubbles.every(token)) problem(`${id}: bad bubbles`); const hits = (r.bubbles || []).filter((b) => b === r.target).length; if (hits !== r.goal || hits < 2) problem(`${id}: goal ${r.goal} != target count ${hits}`); },
  trace: (r, id) => { if (!str(r.label)) problem(`${id}: missing label`); if (!Array.isArray(r.dots) || r.dots.length < 3 || !r.dots.every((d) => d.length === 2 && d.every((v) => typeof v === 'number' && v >= 0 && v <= 100))) problem(`${id}: bad dots`); },
  draw: (r, id) => { if (!str(r.word)) problem(`${id}: missing word`); if (!Array.isArray(r.guesses) || r.guesses.length < 2 || r.guesses[r.guesses.length - 1] !== r.word) problem(`${id}: guesses must end with the word`); },
  rhythm: (r, id) => { if (!isInt(r.pads) || r.pads < 2 || r.pads > 4) problem(`${id}: bad pads`); if (!Array.isArray(r.seq) || r.seq.length < 2 || !r.seq.every((s) => isInt(s) && s >= 0 && s < r.pads)) problem(`${id}: bad seq`); },
  motion: (r, id) => { if (!(r.speed > 0) || !(r.zone > 0 && r.zone < 60)) problem(`${id}: bad speed/zone`); if (!str(r.q)) problem(`${id}: missing q`); },
};
const seen = new Map();
for (const a of cat.activities) {
  const p = byId.get(a.id);
  if (!p) { problem(`${a.id}: no play content`); continue; }
  if (p.engine !== a.engine) problem(`${a.id}: engine ${p.engine} != catalog ${a.engine}`);
  if (!str(p.prompt) || !str(p.tip)) problem(`${a.id}: missing prompt or tip`);
  const rounds = p.rounds || [];
  if (rounds.length < (minRounds[p.engine] || 4)) problem(`${a.id}: only ${rounds.length} rounds`);
  rounds.forEach((r, i) => {
    const fn = check[r.engine];
    if (!fn) return problem(`${a.id}#${i + 1}: unknown round engine ${r.engine}`);
    fn(r, `${a.id}#${i + 1}`);
  });
  const main = rounds.filter((r) => r.engine === p.engine).length;
  if (main * 2 < rounds.length) problem(`${a.id}: engine ${p.engine} is not the main round type`);
  const key = JSON.stringify(rounds);
  if (seen.has(key)) problem(`${a.id}: same rounds as ${seen.get(key)}`);
  seen.set(key, a.id);
}
if (byId.size !== 480) problem(`play.json has ${byId.size} activities`);
finish(`PLAY OK ${cat.activities.length}`);
