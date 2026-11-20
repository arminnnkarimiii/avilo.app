// G2: the game screen has a renderer block for every engine used in content/play.json,
// and loads the play file.
import { readJSON, screen, split, problem, finish } from './lib.mjs';

const play = readJSON('content/play.json');
const used = [...new Set(play.activities.map((a) => a.engine))];
const g = screen('-game');
const { markup, script } = split(g.text);
for (const e of used) {
  if (!markup.includes(`data-engine="${e}"`)) problem(`no renderer block data-engine="${e}" in ${g.name}`);
  if (!new RegExp(`\\b${e}\\s*:\\s*\\(`).test(script) && !script.includes(`'${e}'`)) problem(`no logic for engine ${e} in ${g.name}`);
}
if (!script.includes('content/play.json')) problem(`${g.name} does not load content/play.json`);
if (!script.includes('avilo.attempts')) problem(`${g.name} does not record attempts for tracking`);
if (used.length < 12) problem(`only ${used.length} engines used`);
finish(`ENGINES OK ${used.length}`);
