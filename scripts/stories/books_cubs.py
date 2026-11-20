"""Little Cubs books (10 pages). Placeholders: {name} {he} {him} {his} {He} {His}.
Scenes: (sky, ground, [(kind, x, y, scale), ...]) on a 360 × 240 canvas."""

BOOKS = [
 {"id": "cubs-star-dino", "band": "cubs", "tags": ["dino", "space", "animals"], "skill": "Counting to 5",
  "title": "{name} and the Star-Counting Dinosaur", "pages": [
  ("{name} lived in a cozy house with a cat named Pepper. Every night, {he} looked out of the window at the twinkly stars.", ("dusk", "hills", [("house", 70, 170, 1), ("kid", 200, 185, 1), ("cat", 245, 200, .8), ("star", 300, 40, .6), ("star", 250, 60, .5)])),
  ("One night, a little green dinosaur peeked over the garden fence. \"Hello,\" he whispered. \"My name is Tops.\"", None),
  ("\"I fell down from Star Valley,\" said Tops, wiping a tear. \"Can you help me get home?\" {name} nodded. \"Of course I can!\"", ("night", "grass", [("dino", 120, 185, 1.1), ("kid", 230, 190, 1), ("moon", 300, 50, 1), ("star", 60, 40, .5)])),
  ("{name} found {his} crayons and drew a big red rocket on the garden wall. Pepper meowed, \"Me too, please!\"", None),
  ("Swoosh! The rocket zoomed up, up, up. It flew past one, two, three fluffy clouds. \"Wheee!\" said Tops.", ("night", "none", [("rocket", 180, 150, 1.3), ("cloud", 60, 180, 1), ("cloud", 290, 150, .9), ("cloud", 110, 70, .8)])),
  ("Up in space, the stars sparkled like glitter. \"My home has five stars in a row,\" said Tops. \"Can you find them?\"", None),
  ("{name} counted carefully: one, two, three, four. \"There are only four!\" {he} said. \"Where is the fifth star?\"", ("space", "none", [("star", 60, 80, .7), ("star", 130, 80, .7), ("star", 200, 80, .7), ("star", 270, 80, .7), ("rocket", 180, 180, .9), ("planet", 320, 190, .7)])),
  ("Pepper pointed a fluffy paw. A tiny star was hiding behind the moon. \"Five!\" shouted {name}. The stars began to glow.", None),
  ("Tops gave {name} a big dinosaur hug. \"Thank you! You are the best star-counter in the whole sky.\"", ("space", "moon", [("dino", 150, 190, 1), ("kid", 220, 195, 1), ("star", 60, 60, .6), ("star", 300, 50, .6), ("planet", 320, 120, .6)])),
  ("Back in bed, {name} smiled a sleepy smile. Up above, five stars twinkled in a row, just for {him}. The end.", None),
 ]},
 {"id": "cubs-ocean-splash", "band": "cubs", "tags": ["ocean", "animals", "music"], "skill": "Colours and counting",
  "title": "{name}'s Big Ocean Splash", "pages": [
  ("{name} went to the beach with a bucket and a spade. The waves went splish, splash, splosh.", ("day", "sand", [("kid", 140, 190, 1), ("sun", 300, 50, 1), ("ball", 220, 205, .7), ("boat", 300, 150, .6)])),
  ("A shiny shell sat on the sand. When {name} held it to {his} ear, it sang a little song: \"Come and play under the sea!\"", None),
  ("{name} put on goggles and dived into the bubbly blue water. Down, down, down {he} went.", ("sea", "sand", [("kid", 170, 120, 1), ("fish", 80, 80, .8), ("fish", 280, 160, .8), ("flower", 60, 205, .7)])),
  ("A yellow fish swam by. Then a red fish. Then a blue fish. \"One, two, three fish!\" counted {name}.", None),
  ("A big whale smiled at {name}. \"Would you like a ride?\" she rumbled. \"Yes, please!\" said {name}.", ("sea", "sand", [("whale", 170, 130, 1.3), ("kid", 190, 85, .8), ("fish", 60, 190, .6), ("fish", 310, 80, .6)])),
  ("They swam past green seaweed and pink coral. A crab waved one claw, then two claws. Hello, crab!", None),
  ("The fish wanted to play a colour game. \"Find something orange!\" {name} pointed to a bright orange starfish.", ("sea", "sand", [("star", 120, 200, .8), ("fish", 220, 110, .9), ("kid", 280, 170, .9), ("flower", 60, 200, .8)])),
  ("Then the whale sang a song, and all the fish danced in a twirly circle. {name} danced too!", None),
  ("Soon it was time to go home. The whale gave {name} a gentle push back up to the sunny beach.", ("day", "sand", [("whale", 270, 150, .9), ("kid", 120, 190, 1), ("sun", 60, 50, .9), ("boat", 200, 150, .5)])),
  ("{name} held the shell to {his} ear one more time. It whispered, \"Come back soon!\" And {he} promised {he} would. The end.", None),
 ]},
 {"id": "cubs-lost-puppy", "band": "cubs", "tags": ["animals", "pets", "dog", "feelings"], "skill": "Kindness and helping",
  "title": "{name} and the Lost Puppy", "pages": [
  ("It was a sunny morning in the park. {name} was swinging high when {he} heard a tiny sound. Whimper, whimper.", ("day", "grass", [("tree", 70, 160, 1.2), ("kid", 190, 185, 1), ("sun", 300, 50, .9), ("flower", 280, 205, .7)])),
  ("Under a bench sat a little brown puppy with floppy ears. The puppy looked very sad and a little bit scared.", None),
  ("\"Hello, little puppy,\" said {name} in a soft, gentle voice. \"Are you lost?\" The puppy wagged its tail, just a tiny bit.", ("day", "grass", [("dog", 150, 195, 1), ("kid", 230, 190, 1), ("tree", 50, 160, 1), ("cloud", 280, 60, .8)])),
  ("The puppy had a red collar with a name on it. \"Biscuit,\" read Grandma. \"And here is a phone number!\"", None),
  ("While Grandma made the call, {name} sat with Biscuit so he wouldn't feel lonely. They shared a cuddle.", ("day", "grass", [("dog", 170, 195, .9), ("kid", 200, 190, 1), ("tree", 300, 160, 1), ("flower", 60, 205, .8)])),
  ("{name} felt a little worried. \"What if nobody comes?\" Grandma smiled. \"Someone is already on the way.\"", None),
  ("Then a girl came running across the grass. \"Biscuit! I looked everywhere for you!\" Biscuit jumped and barked with joy.", ("day", "grass", [("kid", 110, 190, 1), ("dog", 180, 195, .9), ("kid", 260, 190, 1), ("sun", 320, 40, .7)])),
  ("\"Thank you for looking after him,\" said the girl. \"You were very kind.\" {name} felt warm and happy inside.", None),
  ("The girl's name was Ruby, and she asked if {name} wanted to play ball with her and Biscuit. Of course {he} did!", ("day", "grass", [("kid", 100, 190, 1), ("ball", 180, 150, .7), ("dog", 230, 195, .9), ("kid", 290, 190, 1)])),
  ("That night, {name} told {his} family all about Biscuit. Helping a friend felt like the best feeling in the world. The end.", None),
 ]},
]
