# Gates: Avilo canvas v3

OWNS: content/**, scripts/**, design/**, docs/**, README.md, GATES.md

Scope: every one of the 480 catalog activities is playable with its own content in a working game engine, a full illustrated story library exists, the onboarding quiz adapts to gender and age, no text-hole spacing bugs remain, and Avi's room and star points are gone.

- [x] G1: all 480 activities have their own valid, non-duplicated playable content
  CHECK: node scripts/verify/verify-play.mjs
  EXPECT: PLAY OK 480
  EVIDENCE: automatic-evidence=v1; definition-sha256=2bfb6a0dab8e44229dfe8a14d338efeb55b6821cafc322c97bbd438221ed339e; exit=0; EXPECT=matched; output-sha256=a670d9c44c27b5faa0070deb4bf3f3ac2daa2088a615775373850395ef56db79; output-bytes=12; shell=C:\WINDOWS\system32\cmd.exe; cwd=C:\Users\famil\avilo; path=e3320bf75e9a/32 entries

- [x] G2: the game screen renders every engine used by the content
  CHECK: node scripts/verify/verify-engines.mjs
  EXPECT: ENGINES OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=27e4ca436558aa51902782b2f54b21f99d5c72b96bb2ee1c0e5cbb2ea64d56e1; exit=0; EXPECT=matched; output-sha256=589b5a87c0a0d6f8e6104722f6c1555cd4cd32506c2e564e9bd14d71edc42158; output-bytes=14; shell=C:\WINDOWS\system32\cmd.exe; cwd=C:\Users\famil\avilo; path=e3320bf75e9a/32 entries

- [x] G3: story library has 3 complete books per age band with correct lengths and an illustration every 2nd page, all drawable
  CHECK: node scripts/verify/verify-stories.mjs
  EXPECT: STORIES OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=e6f430eea68d4f501c60383dbb5f90e763683d05ee5612435b1f4ea4c1250af3; exit=0; EXPECT=matched; output-sha256=d9fc8ad62c2d1cefe8a325446afe17c9a5dc8b61277c2cceb9e2557a02b3a695; output-bytes=19; shell=C:\WINDOWS\system32\cmd.exe; cwd=C:\Users\famil\avilo; path=e3320bf75e9a/32 entries

- [x] G4: no screen mixes literal text and a {{hole}} in one text node, and no sample name remains
  CHECK: node scripts/verify/lint-holes.mjs
  EXPECT: HOLES OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=7b58c324084ae7be3e7e4aa74cc22247c3ac80b02332f2a6dcac631260676d3f; exit=0; EXPECT=matched; output-sha256=7c5ca0f47bf5730d7a28391602cb5207f32dc113f91e6be3717c17f2982e376e; output-bytes=39; shell=C:\WINDOWS\system32\cmd.exe; cwd=C:\Users\famil\avilo; path=e3320bf75e9a/32 entries

- [x] G5: every screen script compiles
  CHECK: node scripts/verify/verify-js.mjs
  EXPECT: JS OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=f57c362062fb33d7eb837cdeca1c006b9c96f28787aee8e113595b68114861cd; exit=0; EXPECT=matched; output-sha256=ef20a970778a46137877ceed3d8c710c260202dbecb01a1cb9043c2194ee75c2; output-bytes=17; shell=C:\WINDOWS\system32\cmd.exe; cwd=C:\Users\famil\avilo; path=e3320bf75e9a/32 entries

- [x] G6: Avi's room and star points are removed and Avi is plain everywhere
  CHECK: node scripts/verify/verify-removals.mjs
  EXPECT: REMOVALS OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=b7a6c58654a07a795a5e9ed99d05ed0507f8477f1f5dbd3b2ba9b6f9aed633d8; exit=0; EXPECT=matched; output-sha256=21d5ba24589e092d35f6fa711c3ce1b47c4f0e1bc3e421704264dd9990453028; output-bytes=12; shell=C:\WINDOWS\system32\cmd.exe; cwd=C:\Users\famil\avilo; path=e3320bf75e9a/32 entries

- [x] G7: quiz asks boy or girl first, branches by age band and answers, and recommends 15–20 minutes
  CHECK: node scripts/verify/verify-quiz.mjs
  EXPECT: QUIZ OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=b68fcd435d8a1ab922a698737827b930e10eb5cfc313150b75af5a28dca49c71; exit=0; EXPECT=matched; output-sha256=cf24e100077e7c5c09f70c46a8c8a7f30364c0135d14178fa55d39784d57845d; output-bytes=8; shell=C:\WINDOWS\system32\cmd.exe; cwd=C:\Users\famil\avilo; path=e3320bf75e9a/32 entries

- [x] G9: every screen runs, every one of the 2397 rounds can be played to a win, and every story page renders
  CHECK: node scripts/verify/smoke.mjs
  EXPECT: /SMOKE OK screens=17 rounds=\d+ wins=\d+ pages=150/
  EVIDENCE: automatic-evidence=v1; definition-sha256=8951003747e6aa835c2fdc4b11c76e179cf6c7a443ec2d71cae320e6e8e39eb3; exit=0; EXPECT=matched; output-sha256=2ddb0f7b1c967c2220d53e178dd071ea771d97906b2011eddab0296d648b6c36; output-bytes=52; shell=C:\WINDOWS\system32\cmd.exe; cwd=C:\Users\famil\avilo; path=e3320bf75e9a/32 entries

- [ ] G8: the published canvas matches design/screens and plays in the browser (manual review)
  EVIDENCE: pending
