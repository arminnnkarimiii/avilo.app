// G6: Avi's room, star points and Avi outfits are gone from every screen;
// chests give badges and unlock stories.
import fs from 'node:fs';
import path from 'node:path';
import { screens, split, screen, problem, finish, root } from './lib.mjs';

const banned = [
  [/AviRoom\.dc\.html/, 'link to Avi\'s room'],
  [/Avi's room/i, 'Avi\'s room text'],
  [/Star shop/i, 'star shop'],
  [/openStars|starsOpen/, 'star sheet'],
  [/\+\s?\d+ stars|\d+ stars<|>stars</i, 'star points'],
  [/★/, 'star rating glyph'],
  [/wardrobe|fedora|7fb17821dfd6dd71cde50a5bc0035546/i, 'Avi outfit'],
];
for (const s of screens()) {
  const { markup, script } = split(s.text);
  for (const [re, what] of banned) if (re.test(markup) || re.test(script)) problem(`${s.name}: still has ${what}`);
}
if (screens().some((s) => /avi-room/.test(s.name))) problem('avi-room screen file still exists');
const canvas = JSON.parse(fs.readFileSync(path.join(root, 'design', 'canvas.json'), 'utf8'));
if (canvas.boards['AviRoom.dc.html'] || canvas.order.includes('AviRoom.dc.html')) problem('canvas index still lists AviRoom');
const road = screen('-trophy-road').text;
if (!/badge/i.test(road) || !/story unlocked|New story/i.test(road)) problem('chest does not give a badge and unlock a story');
if (!/Stories\.dc\.html/.test(road)) problem('chest reveal does not link to the story library');
// positive control: the star-points pattern must match a known bad sample
if (!/\+\s?\d+ stars/.test('<span>+3 stars</span>')) problem('self-test failed');
finish('REMOVALS OK');
