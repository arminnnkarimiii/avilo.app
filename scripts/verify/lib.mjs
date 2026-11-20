// Shared helpers for the canvas verifiers. Run from the repository root.
import fs from 'node:fs';
import path from 'node:path';

export const root = process.cwd();
export const screensDir = path.join(root, 'design', 'screens');

export function readJSON(rel) {
  return JSON.parse(fs.readFileSync(path.join(root, rel), 'utf8'));
}

export function screens() {
  return fs.readdirSync(screensDir).filter((f) => f.endsWith('.html')).sort()
    .map((f) => ({ name: f, text: fs.readFileSync(path.join(screensDir, f), 'utf8') }));
}

export function split(text) {
  const i = text.indexOf('<script type="text/x-dc"');
  if (i < 0) return { markup: text, script: '' };
  const m = /<script type="text\/x-dc"[^>]*>([\s\S]*?)<\/script>/.exec(text.slice(i));
  return { markup: text.slice(0, i), script: m ? m[1] : '' };
}

export function screen(fragment) {
  const s = screens().find((x) => x.name.includes(fragment));
  if (!s) fail(`screen matching "${fragment}" not found`);
  return s;
}

const problems = [];
export function problem(msg) { problems.push(msg); }
export function finish(okToken) {
  if (problems.length) {
    for (const p of problems.slice(0, 40)) console.error('FAIL', p);
    if (problems.length > 40) console.error(`… and ${problems.length - 40} more`);
    process.exit(1);
  }
  console.log(okToken);
}
export function fail(msg) { console.error('FAIL', msg); process.exit(1); }
