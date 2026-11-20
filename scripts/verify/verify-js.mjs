// G5: every screen's logic script compiles.
import vm from 'node:vm';
import { screens, split, problem, finish } from './lib.mjs';

let n = 0;
for (const s of screens()) {
  const { script } = split(s.text);
  if (!script.trim()) { problem(`${s.name}: no logic script`); continue; }
  try { new vm.Script(`class DCLogic {}\n${script}\n;Component;`, { filename: s.name }); n++; }
  catch (e) { problem(`${s.name}: ${e.message}`); }
}
finish(`JS OK ${n} screens`);
