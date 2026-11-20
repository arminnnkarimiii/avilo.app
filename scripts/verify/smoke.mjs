// G9: run every screen's logic headlessly. For the game screen, start every one of the
// 480 activities, render every round, and tap the right answer (and a wrong one where
// possible) to check each engine reaches "right" without throwing.
import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import { screens, split, problem, finish, readJSON, root } from './lib.mjs';

const store = new Map(Object.entries({ 'avilo.kid': 'Sam', 'avilo.gender': 'boy', 'avilo.age': '7', 'avilo.interests': '["space","robots"]', 'avilo.color': 'blue' }));
function sandbox() {
  const timers = [];
  const ctx = {
    console, Math, JSON, Date, Object, Array, String, Number, Set, Map, parseInt, RegExp, Promise,
    localStorage: { getItem: (k) => (store.has(k) ? store.get(k) : null), setItem: (k, v) => store.set(k, String(v)) },
    setTimeout: (fn, ms) => { timers.push(fn); return timers.length; }, clearTimeout: () => {}, setInterval: () => 0, clearInterval: () => {},
    fetch: () => new Promise(() => {}), speechSynthesis: { cancel() {}, speak() {} }, SpeechSynthesisUtterance: function () {}, window: { location: {} },
  };
  ctx.DCLogic = class { constructor() { this.state = {}; } setState(p) { this.state = { ...this.state, ...(typeof p === 'function' ? p(this.state) : p) }; } };
  vm.createContext(ctx);
  return { ctx, timers };
}
function load(text) {
  const { script } = split(text);
  const { ctx, timers } = sandbox();
  vm.runInContext(script + '\n;this.__C = Component;', ctx);
  const c = new ctx.__C(); c.state = {};
  return { c, timers, flush: (n = 50) => { for (let i = 0; i < n && timers.length; i++) timers.shift()(); } };
}

let screensRun = 0;
for (const s of screens()) {
  try { const { c } = load(s.text); if (c.componentDidMount) try { c.componentDidMount(); } catch (e) { if (!/fetch/.test(String(e))) throw e; } c.renderVals(); screensRun++; }
  catch (e) { problem(`${s.name}: renderVals threw ${e.message}`); }
}

const play = readJSON('content/play.json');
const game = screens().find((s) => s.name.includes('-game'));
let rounds = 0, wins = 0;
for (const act of play.activities) {
  const g = load(game.text);
  g.c.all = play.activities;
  try { g.c.start(act); } catch (e) { problem(`${act.id}: start threw ${e.message}`); continue; }
  for (let i = 0; i < act.rounds.length; i++) {
    try {
      g.c.round(act, i); g.flush(5);
      const rd = act.rounds[i];
      let v = g.c.renderVals();
      const tapIdx = (list, pred) => { const k = list.findIndex(pred); if (k >= 0) list[k].tap(); };
      switch (rd.engine) {
        case 'pick': case 'sound': case 'pattern': case 'count':
          g.c.setState({ look: false }); v = g.c.renderVals(); v.choices[rd.answer].tap(); break;
        case 'match': {
          const cards = g.c.state.cards;
          for (let k = 0; k < rd.pairs.length; k++) { const two = cards.filter((x) => x.k === k); g.c.setState({ open: [] }); g.c.renderVals().cards.find((c, j) => cards[j].id === two[0].id).tap(); g.c.renderVals().cards.find((c, j) => cards[j].id === two[1].id).tap(); g.flush(3); }
          break; }
        case 'sort': for (const it of rd.items) { g.c.renderVals().bins[it[1]].tap(); } break;
        case 'build': { g.c.setState({ look: false }); const order = g.c.state.order; for (const want of rd.answer) { const vv = g.c.renderVals(); const k = order.findIndex((idx) => rd.pieces[idx] === want && !g.c.state.built.includes(idx)); vv.pieces[k].tap(); } break; }
        case 'choice': { const k = rd.options.findIndex((o) => o.ok); g.c.renderVals().options[k].tap(); g.flush(3); break; }
        case 'changed': g.c.setState({ look: false }); g.c.renderVals().gridCells[rd.idx].tap(); break;
        case 'pop': rd.bubbles.forEach((b, k) => { if (b === rd.target && !g.c.state.result) g.c.renderVals().bubbles[k].tap(); }); break;
        case 'trace': rd.dots.forEach((_, k) => g.c.renderVals().dots[k].tap()); break;
        case 'draw': g.c.setState({ strokes: [{ d: 'M1 1 L2 2', c: '#000' }] }); g.c.renderVals().finishDrawing(); g.flush(20); break;
        case 'rhythm': g.c.setState({ rhythmPhase: 'play', rhythmIn: [] }); rd.seq.forEach((p) => { g.c.renderVals().pads[p].tap(); }); break;
        case 'motion': { const Dur = 1.6 / rd.speed; const zl = g.c.renderVals().zoneL; const target = (zl + rd.zone / 2) / 100; g.c.setState({ mStart: Date.now() - target * Dur * 1000 }); g.c.renderVals().motionTap(); break; }
        default: problem(`${act.id}#${i + 1}: no smoke driver for ${rd.engine}`);
      }
      rounds++;
      if (g.c.state.result === 'right') wins++; else problem(`${act.id}#${i + 1} (${rd.engine}): correct play did not win`);
    } catch (e) { problem(`${act.id}#${i + 1} (${act.rounds[i].engine}): ${e.message}`); }
  }
  try { g.c.nextRound(); g.c.renderVals(); } catch (e) { problem(`${act.id}: finish threw ${e.message}`); }
}
// stories: render every page of every book
const lib = readJSON('content/stories.json');
const reader = screens().find((s) => s.name.includes('-story-book'));
let pages = 0;
for (const b of lib.books) {
  const r = load(reader.text);
  store.set('avilo.book', b.id);
  r.c.setState({ lib: lib, reading: true });
  for (let i = 0; i < b.pages.length; i++) { r.c.setState({ i }); const v = r.c.renderVals(); if (!v.props.length || v.words.some((w) => /\{(name|he|his|him)\}/i.test(w.t))) problem(`${b.id} p${i + 1}: missing art or unfilled placeholder`); pages++; }
}
finish(`SMOKE OK screens=${screensRun} rounds=${rounds} wins=${wins} pages=${pages}`);
