// G7: adaptive onboarding quiz.
import { screen, split, problem, finish } from './lib.mjs';

const name = screen('-quiz-name');
const nm = split(name.text);
if (!/>Boy</.test(nm.markup + nm.script) && !/'Boy'/.test(nm.script)) problem('no Boy option');
if (!/>Girl</.test(nm.markup + nm.script) && !/'Girl'/.test(nm.script)) problem('no Girl option');
const gi = nm.markup.search(/gender/i), ni = nm.markup.search(/id="kidname"/);
if (gi < 0 || ni < 0 || gi > ni) problem('gender is not asked before the name');
if (!nm.script.includes("'avilo.gender'")) problem('gender is not saved');
if (!nm.script.includes("'avilo.age'")) problem('age is not saved');

const moreFull = screen('-quiz-more').text;
const more = split(moreFull).script;
for (const band of ['cubs', 'explorers', 'trailblazers']) if (!new RegExp(`band === '${band}'|${band}:`).test(more)) problem(`no ${band}-specific questions`);
if (!/when\s*:|followUp|branch/i.test(more)) problem('no answer-based follow-up questions');
if (!/Recommended/.test(moreFull) || !/15/.test(more) || !/20/.test(more)) problem('no recommended 15–20 minutes');
if (!/\b(he|she)\b|P\.he|pron/.test(more)) problem('questions are not personalised with he/she');
const interests = split(screen('-quiz-interests').text).script;
for (const band of ['cubs', 'explorers', 'trailblazers']) if (!interests.includes(band)) problem(`interests do not vary for ${band}`);
for (const f of ['-quiz-name', '-quiz-interests', '-quiz-more']) {
  const t = screen(f).text;
  if (!/confetti|burst/i.test(t)) problem(`${f}: no confetti on answer`);
}
finish('QUIZ OK');
