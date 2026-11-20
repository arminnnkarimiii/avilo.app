// G4: in canvas markup, a text node must be either plain text or exactly one {{hole}}.
// Mixing them ("Make {{kidPos}} plan") loses the spaces when rendered.
// Also rejects the old sample name.
import { screens, split, problem, finish } from './lib.mjs';

let checked = 0;
for (const s of screens()) {
  const { markup } = split(s.text);
  const body = markup.replace(/<helmet>[\s\S]*?<\/helmet>/, '');
  for (const m of body.matchAll(/>([^<>]*)</g)) {
    const t = m[1];
    if (!t.includes('{{')) continue;
    checked++;
    const rest = t.replace(/\{\{[^}]+\}\}/g, '').trim();
    const holes = (t.match(/\{\{[^}]+\}\}/g) || []).length;
    if (rest.length || holes > 1) problem(`${s.name}: mixed text node "${t.trim().slice(0, 70)}"`);
  }
  if (/\bMila\b|\bMILA\b/.test(s.text)) problem(`${s.name}: sample name Mila still present`);
}
// positive control: the linter must catch the known-bad pattern
const control = '<div>Make {{kidPos}} plan</div>'.match(/>([^<>]*)</)[1];
if (!control.replace(/\{\{[^}]+\}\}/g, '').trim()) problem('linter self-test failed');
finish(`HOLES OK (${checked} hole text nodes checked)`);
