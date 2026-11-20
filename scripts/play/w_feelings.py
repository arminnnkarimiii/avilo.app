"""Feelings Cottage: 20 activities per band. Mostly gentle scenario choices."""
from common import *

N = 5


def C(sets):
    return [choice(q, o) for q, o in sets]


def G(good, why_good, bad, why_bad, bad2=None, why2=None):
    opts = [(good, True, why_good), (bad, False, why_bad)]
    if bad2:
        opts.append((bad2, False, why2))
    return opts


# ---------------- Little Cubs ----------------
def c01(r):
    qs = [("Avi got a present and is smiling big. How does Avi feel?", "Happy", ["Sad", "Angry"]), ("Avi dropped his ice cream. How does Avi feel?", "Sad", ["Happy", "Excited"]),
          ("Avi heard a loud bang in the dark. How does Avi feel?", "Scared", ["Proud", "Silly"]), ("Avi's tower got knocked over on purpose. How does Avi feel?", "Angry", ["Calm", "Happy"]),
          ("It's Avi's birthday party tomorrow! How does Avi feel?", "Excited", ["Bored", "Sad"]), ("Avi built a tall tower all by himself. How does Avi feel?", "Proud", ["Scared", "Sad"])]
    return ("How does Avi feel?", "Look at what happened to Avi.", [pick(r, q, a, w) for q, a, w in r.sample(qs, N)])
def c02(r):
    happy = ["Playing at the park", "A big hug", "Ice cream", "A birthday party", "Puppy kisses", "Finding a shell"]
    sad = ["A broken toy", "Saying goodbye", "Losing a game", "A scraped knee", "A rainy picnic", "Missing a friend"]
    return ("Happy or sad?", "How would it make you feel?", [sort(["Happy", "Sad"], shuffled(r, [(x, 0) for x in r.sample(happy, 3)] + [(x, 1) for x in r.sample(sad, 3)])) for _ in range(N)])
def c03(r): return ("Calm-down breathing", "Breathe in when it lights up, out when it goes dark.", [rhythm(r, 2, 4) | {"seq": [0, 1, 0, 1][: 2 + i % 3] + [0, 1]} for i in range(N)])
def c04(r):
    return ("Sharing toys", "Sharing makes playing more fun.", C([
        ("Your friend wants to play with your blocks.", G("Let's build together!", "Sharing makes playing more fun.", "No! Mine!", "That might make your friend sad.")),
        ("There is one swing and two kids.", G("Take turns", "Turns mean everyone gets to swing.", "Push the other kid off", "That could hurt someone.")),
        ("You have 4 crackers and your friend has none.", G("Give your friend 2", "Now you both have 2. That's fair!", "Hide them", "Your friend would feel left out.")),
        ("Your little brother wants your crayon.", G("Give him a different color", "Finding a way to share is kind.", "Snap it in half and throw it", "That breaks the crayon.")),
        ("A new kid has no toy to play with.", G("Offer one of yours", "That helps them feel welcome.", "Ignore them", "They might feel lonely.")),
    ]))
def c05(r):
    return ("Saying sorry", "A real sorry fixes things.", C([
        ("You bumped into a friend and they fell.", G("Say sorry and help them up", "That shows you care.", "Run away", "They might think you did it on purpose.")),
        ("You broke your sister's drawing by accident.", G("Say sorry and help fix it", "Fixing things helps a lot.", "Say it wasn't you", "Telling the truth is better.")),
        ("You shouted at your friend.", G("Say sorry and use a calm voice", "Calm words help friends feel safe.", "Shout louder", "That makes it worse.")),
        ("You took a toy without asking.", G("Give it back and say sorry", "Asking first is kind.", "Keep it", "It isn't yours.")),
        ("You spilled juice on the table.", G("Say oops and help clean up", "Accidents happen. Helping is great.", "Leave it", "Someone could slip.")),
    ]))
def c06(r):
    steps = ["Bath", "Pyjamas", "Brush teeth", "Story", "Sleep"]
    return ("Bedtime routine", "A routine helps your body get ready for sleep.", [build(r, "Put bedtime in order.", steps[i % 2:i % 2 + 3 + (i % 3)]) for i in range(N)])
def c07(r):
    fc = [("Yellow", "Happy"), ("Blue", "Sad"), ("Red", "Angry"), ("Green", "Calm"), ("Purple", "Scared"), ("Orange", "Excited")]
    return ("Feeling colors", "Some people imagine feelings as colors.", [match(r.sample(fc, 3)) for _ in range(N)])
def c08(r):
    return ("Help a friend", "Kind helpers notice when someone needs help.", C([
        ("Your friend is crying because they fell.", G("Ask if they're okay", "Checking in shows you care.", "Laugh", "Laughing could hurt their feelings.")),
        ("Your friend dropped all their crayons.", G("Help pick them up", "Many hands make it quick.", "Walk away", "They'd have to do it alone.")),
        ("A friend can't reach the shelf.", G("Get a grown-up to help", "Grown-ups can reach high places safely.", "Climb the shelf", "Climbing shelves isn't safe.")),
        ("A friend is sad their balloon flew away.", G("Give them a hug", "Hugs can help sad feelings.", "Say it's silly to be sad", "All feelings are okay.")),
        ("Your friend is scared of the dark.", G("Hold their hand", "Being together feels safer.", "Turn off more lights", "That makes it scarier.")),
    ]))
def c09(r):
    steps = ["Wet the brush", "Add toothpaste", "Brush top teeth", "Brush bottom teeth", "Spit and rinse"]
    return ("Brush your teeth", "Brush for two minutes, twice a day.", [build(r, "Put the steps in order.", steps[i % 2:i % 2 + 3 + (i % 2)]) for i in range(N)])
def c10(r):
    return ("Brave little bear", "Being brave means trying even when you're a little scared.", C([
        ("It's your first day at a new class.", G("Say hello to one kid", "One hello is a brave start.", "Hide all day", "You might miss the fun.")),
        ("You want to try the big slide.", G("Try it with a grown-up nearby", "Brave and safe together.", "Never try anything new", "New things can be fun.")),
        ("The doctor needs to check your ears.", G("Take a deep breath and sit still", "Breathing helps you feel calm.", "Run out the door", "The doctor is there to help.")),
        ("You want to sing in the show.", G("Practice and give it a go", "Practice makes it easier.", "Say you can't", "You can try your best.")),
        ("You're scared of a big dog.", G("Stand still and ask the owner first", "That keeps you safe.", "Scream and run at it", "That could scare the dog.")),
    ]))
def c11(r):
    kind = ["Thank you", "You're my friend", "Great job", "Please", "I'm sorry", "Let's play"]
    unkind = ["Go away", "You're silly", "I don't like you", "That's mine"]
    return ("Pop the kind words!", "Kind words make people feel good.", [pop(r, k, unkind, 3, 8) | {"q": f"Pop the kind words “{k}”!"} for k in r.sample(kind, N)])
def c12(r):
    fam = [("Mum", "@heart:red"), ("Dad", "@heart:blue"), ("Grandma", "@flower:pink"), ("Grandpa", "@tree:green"), ("Baby", "@star:yellow"), ("Pet", "@cat:orange"), ("Sister", "@flower:purple"), ("Brother", "@ball:blue")]
    return ("My family", "Every family is different and special.", [match(r.sample(fam, 3)) for _ in range(N)])
def c13(r):
    return ("Taking turns", "Waiting for your turn is fair.", C([
        ("Everyone wants the red crayon.", G("Take turns with it", "Fair for everyone.", "Grab it first", "Others would feel upset.")),
        ("It's your friend's turn on the game.", G("Wait and cheer them on", "Cheering makes waiting fun.", "Take the controller", "It's their turn.")),
        ("Lots of kids want to talk at circle time.", G("Raise your hand", "Then everyone gets heard.", "Shout over everyone", "Nobody can hear then.")),
        ("Two kids want the same book.", G("Read it together", "Sharing a book is cosy.", "Pull it away", "Books can tear.")),
        ("A line for the slide.", G("Wait at the back", "Lines keep it fair.", "Push to the front", "That isn't fair.")),
    ]))
def c14(r):
    return ("Scared of the dark", "It's okay to feel scared. There are ways to feel safer.", C([
        ("Your room is dark and you feel scared.", G("Turn on a night light", "Soft light helps you see it's safe.", "Hide and cry all night", "Ask for help instead.")),
        ("You heard a noise at night.", G("Call a grown-up", "Grown-ups can check for you.", "Pretend you're not scared", "It's okay to ask for help.")),
        ("Shadows look like monsters.", G("Look closely: it's your coat!", "Shadows are just shapes.", "Run out of bed", "You might trip in the dark.")),
        ("You can't sleep.", G("Hug your teddy and breathe slowly", "Slow breaths help your body relax.", "Jump on the bed", "That makes you more awake.")),
        ("A storm is loud outside.", G("Count between flash and boom", "Counting helps you feel calm.", "Open the window", "Keep it shut and stay cosy.")),
    ]))
def c15(r):
    ff = [("Smile", "Happy"), ("Frown", "Sad"), ("Wide eyes", "Surprised"), ("Clenched teeth", "Angry"), ("Yawn", "Tired"), ("Shaking", "Scared")]
    return ("Feelings faces match", "Faces show how we feel inside.", [match(r.sample(ff, 3)) for _ in range(N)])
def c16(r):
    return ("The thank-you game", "Saying thank you makes people feel appreciated.", C([
        ("Grandma gives you a cookie.", G("Say thank you!", "That makes Grandma smile.", "Grab it and run", "Remember your thank you.")),
        ("A friend lends you a pencil.", G("Thank you!", "It shows you noticed.", "Say nothing", "They might not know you're grateful.")),
        ("Dad made your favourite dinner.", G("Thank you, Dad!", "Cooking takes work.", "Yuck", "That could hurt his feelings.")),
        ("Your teacher helped you tie your shoe.", G("Thanks for helping!", "Helpers love to hear thanks.", "Run off", "Saying thanks is kind.")),
        ("Someone holds the door for you.", G("Thank you!", "Small thanks matter.", "Push past", "Be gentle and grateful.")),
    ]))
def c17(r): return ("Calm the angry volcano", "Breathe in for the rumble, out to cool the lava.", [rhythm(r, 2, 3 + i) for i in range(N)])
def c18(r):
    qs = [("You want a cookie. What do you say?", "May I have a cookie, please?", ["Give me a cookie!", "Cookie now!"]), ("Someone gives you a gift. You say…", "Thank you!", ["Whatever", "Is that all?"]),
          ("You need to get past someone. You say…", "Excuse me, please.", ["Move!", "Out of my way!"]), ("You bumped someone. You say…", "Sorry!", ["Watch out!", "Ha!"]),
          ("You want to join a game. You ask…", "Can I play too, please?", ["I'm playing now!", "My turn!"])]
    return ("Please and thank you", "Magic words make people want to help.", [pick(r, q, a, w) for q, a, w in qs])
def c19(r):
    acts = ["Draw them a picture", "Tell a joke", "Share a snack", "Give a hug", "Play their game", "Say something kind"]
    return ("Make a friend smile", "Little kind acts make big smiles.", [build(r, "Plan 3 kind things in your favourite order.", r.sample(acts, 3)) for _ in range(N)])
def c20(r):
    return ("Gentle hands", "Gentle hands keep everyone safe.", C([
        ("You feel angry at your friend.", G("Use words, not hands", "Words solve problems safely.", "Hit them", "Hitting hurts.")),
        ("You want to pet the cat.", G("Stroke it softly", "Gentle touch makes cats happy.", "Pull its tail", "That hurts the cat.")),
        ("The baby grabbed your toy.", G("Ask a grown-up for help", "Grown-ups help sort it out.", "Grab it back hard", "The baby could get hurt.")),
        ("You're excited and want to hug.", G("Ask first: hug?", "Asking first is respectful.", "Squeeze really hard", "Too hard can hurt.")),
        ("Your tower fell down.", G("Take a breath and build again", "Calm hands build better.", "Throw the blocks", "Blocks can hurt someone.")),
    ]))

# ---------------- Explorers ----------------
def e01(r):
    qs = [("Your heart races before a test.", "Nervous", ["Bored", "Sleepy"]), ("You finally learn to ride a bike.", "Proud", ["Jealous", "Ashamed"]),
          ("Your friend got the toy you wanted.", "Jealous", ["Calm", "Grateful"]), ("You told a joke and nobody laughed.", "Embarrassed", ["Proud", "Brave"]),
          ("You got a surprise party.", "Surprised", ["Lonely", "Grumpy"]), ("Someone helped you when you were stuck.", "Grateful", ["Furious", "Bored"])]
    return ("Name the feeling", "Naming a feeling helps you handle it.", [pick(r, q + " This feeling is…", a, w) for q, a, w in r.sample(qs, N)])
def e02(r):
    tools = [("Feeling angry", "Count to ten"), ("Feeling worried", "Talk to someone you trust"), ("Feeling sad", "Draw or write about it"),
             ("Feeling overexcited", "Take five slow breaths"), ("Feeling frustrated", "Take a break and try again"), ("Feeling lonely", "Invite a friend to play")]
    return ("Big feelings toolbox", "Every feeling has a tool that helps.", [match(r.sample(tools, 3)) for _ in range(N)])
def e03(r):
    return ("Friendship problem solving", "Talk, listen, then find a fix together.", C([
        ("Two friends both want to be team captain.", G("Take turns being captain", "Everyone gets a go.", "Quit the game", "Then nobody plays.", "Argue until recess ends", "That wastes the fun.")),
        ("Your friend said something that hurt you.", G("Tell them calmly how you felt", "Honest, calm words help.", "Say something mean back", "That hurts both of you.")),
        ("You and a friend disagree on what to play.", G("Play one game each", "A fair compromise.", "Play alone", "You could have played together.")),
        ("A friend keeps copying your drawing.", G("Say you'd like to make different ones", "Clear and kind.", "Rip up their paper", "That's unkind.")),
        ("Your friend forgot your birthday.", G("Tell them it mattered to you", "Friends want to know.", "Stop being friends", "Everyone forgets sometimes.")),
    ]))
def e04(r):
    return ("Mistakes help us grow", "Every mistake is a step to learning.", C([
        ("You got a sum wrong.", G("Check where it went wrong", "That's how you learn.", "Say you're bad at maths", "You're still learning!")),
        ("You missed the goal.", G("Practise and try again", "Practice builds skill.", "Never play again", "Then you can't improve.")),
        ("Your cake came out flat.", G("Try a different recipe next time", "Experimenting is learning.", "Throw the oven away", "The oven isn't the problem.")),
        ("You spelled a word wrong in your story.", G("Fix it and keep writing", "Mistakes are easy to fix.", "Tear up the story", "The ideas were great!")),
        ("You lost a chess game.", G("Ask what you could do next time", "Learning from losses makes you better.", "Blame the board", "Owning it helps you grow.")),
    ]))
def e05(r):
    bc = [("Butterflies in tummy", "Nervous"), ("Hot face", "Embarrassed or angry"), ("Tight fists", "Angry"), ("Tears", "Sad"), ("Heavy eyes", "Tired"), ("Bouncy legs", "Excited")]
    return ("Body clues for feelings", "Your body tells you what you feel.", [match(r.sample(bc, 3)) for _ in range(N)])
def e06(r):
    fair = ["Everyone gets one slice", "Taking turns on the swing", "Same rules for all players", "Sharing the last cookie in half", "Choosing teams by drawing names"]
    unfair = ["One kid gets all the slices", "Cutting in line", "Changing the rules to win", "Only friends can play", "Peeking during hide and seek"]
    return ("Fair or unfair?", "Fair means everyone has a chance.", [sort(["Fair", "Unfair"], shuffled(r, [(x, 0) for x in r.sample(fair, 3)] + [(x, 1) for x in r.sample(unfair, 3)])) for _ in range(N)])
def e07(r):
    return ("Kindness challenge", "Small kind things add up.", C([
        ("A classmate is sitting alone at lunch.", G("Ask them to join you", "Inclusion feels great.", "Pretend not to see", "They might feel lonely.")),
        ("Your neighbour carries heavy bags.", G("Offer to help carry one", "Helping hands are kind.", "Watch and laugh", "That's unkind.")),
        ("Someone drops their books.", G("Help pick them up", "Quick and kind.", "Step over them", "Help is better.")),
        ("Your sibling had a bad day.", G("Make them a card", "Thoughtful and caring.", "Tease them", "That makes it worse.")),
        ("A new student looks lost.", G("Show them around", "You'd want that too.", "Ignore them", "Being new is hard.")),
    ]))
def e08(r):
    w = [("Worried about a test", "Study a little each day"), ("Worried about a sick pet", "Talk to a grown-up"), ("Worried about a new school", "Visit first and ask questions"),
         ("Worried about the dark", "Use a night light"), ("Worried about a friend being mad", "Talk it out kindly"), ("Worried about a storm", "Stay inside with family")]
    return ("Worry jar", "Put the worry in the jar, then pick a helper.", [match(r.sample(w, 3)) for _ in range(N)])
def e09(r):
    return ("Listening ears", "Good listeners look, wait and ask.", C([
        ("Your friend is telling a story.", G("Look at them and wait", "That shows you care.", "Interrupt with your story", "Wait your turn to talk.")),
        ("The teacher is giving directions.", G("Listen, then ask if confused", "Smart listening.", "Chat with your friend", "You'll miss the directions.")),
        ("Mum is explaining something important.", G("Put your toy down and listen", "Full attention.", "Keep playing your game", "You might miss something.")),
        ("A friend is upset and talking.", G("Nod and say 'that sounds hard'", "Empathy helps.", "Change the subject", "They want to be heard.")),
        ("Someone has a different idea.", G("Hear them out first", "Respect builds teams.", "Say 'that's dumb'", "That shuts people down.")),
    ]))
def e10(r):
    steps = ["Share ideas", "Pick a plan", "Split the jobs", "Build together", "Celebrate"]
    return ("Teamwork tower", "Teams work best when everyone has a job.", [build(r, "Order the teamwork steps.", steps[i % 2:i % 2 + 3 + (i % 2)]) for i in range(N)])
def e11(r):
    levels = ["Calm", "A little annoyed", "Frustrated", "Angry", "Furious"]
    return ("Feelings thermometer", "Catch feelings early, when they're small.", [build(r, "Order from coolest to hottest feeling.", levels[i:i + 3]) for i in range(3)] + [build(r, "Order all five.", levels), build(r, "Order these.", levels[::2])])
def e12(r):
    return ("Saying no politely", "You can say no and still be kind.", C([
        ("A friend wants you to skip homework and play.", G("No thanks, I'll play after", "Kind and clear.", "Okay, forget homework", "Homework matters too.")),
        ("Someone offers you candy you're not allowed.", G("No thank you", "Polite and safe.", "Take it secretly", "Follow your family's rules.")),
        ("A friend wants to borrow your new toy and you're not ready.", G("Not today, maybe later", "Honest and kind.", "Yell NO!", "Calm voices work better.")),
        ("Someone dares you to do something unsafe.", G("No, that's not safe", "Safety first.", "Do it to look cool", "Safety matters more.")),
        ("Someone wants a hug and you don't feel like it.", G("Can we high five instead?", "Your body, your choice.", "Hug anyway", "You can say no.")),
    ]))
def e13(r):
    g = ["I'm thankful for my family", "I'm thankful for sunny days", "I'm thankful for my friends", "I'm thankful for good food", "I'm thankful for my pet", "I'm thankful for books"]
    return ("Gratitude garden", "Each thank-you grows a flower.", [build(r, "Plant 3 thank-yous in your order.", r.sample(g, 3)) for _ in range(N)])
def e14(r):
    return ("Lost and found feelings", "Imagine how someone else feels.", C([
        ("Your friend lost their dog.", G("They feel worried. Help make posters.", "Empathy plus action.", "Say dogs are everywhere", "That dismisses their feelings.")),
        ("A classmate's family moved away.", G("They might feel lonely. Invite them to play.", "Thoughtful.", "Ignore them", "They need friends now.")),
        ("Your brother didn't make the team.", G("He feels disappointed. Say you're proud he tried.", "Kind and true.", "Tell him he wasn't good enough", "Ouch.")),
        ("Your friend's grandma is sick.", G("They feel sad. Ask how they're doing.", "Caring.", "Talk only about your weekend", "Notice their feelings.")),
        ("A kid got laughed at.", G("They feel embarrassed. Stand with them.", "Brave and kind.", "Laugh too", "That hurts more.")),
    ]))
def e15(r): return ("Calm corner breathing", "In through the nose, out through the mouth.", [rhythm(r, 3, 3 + i) for i in range(N)])
def e16(r):
    return ("Telling the truth", "Honesty builds trust.", C([
        ("You broke a vase by accident.", G("Tell a grown-up what happened", "Honesty builds trust.", "Blame the cat", "The truth usually comes out.")),
        ("You didn't finish your homework.", G("Tell your teacher honestly", "They can help you.", "Say the dog ate it", "Make-believe excuses lose trust.")),
        ("You found money that isn't yours.", G("Hand it in", "Someone is looking for it.", "Keep it", "It belongs to someone.")),
        ("You ate the last cookie.", G("Say it was me, sorry", "Owning it is brave.", "Say it vanished", "Truth is better.")),
        ("Your friend asks if you liked their song and you didn't love it.", G("Say a part you liked", "Honest and kind.", "Laugh at it", "That's hurtful.")),
    ]))
def e17(r):
    return ("New school day", "New places get easier every day.", C([
        ("You don't know anyone yet.", G("Say hi and ask their name", "One friend is a great start.", "Stay quiet all year", "Friends come from saying hi.")),
        ("You can't find your classroom.", G("Ask a teacher", "Teachers love to help.", "Wander alone and cry", "Asking is faster.")),
        ("Lunch feels noisy and scary.", G("Sit with someone from class", "Familiar faces help.", "Skip lunch", "You need food to learn.")),
        ("Your new teacher is different.", G("Give it time", "Change takes time.", "Refuse to listen", "You'll miss out.")),
        ("You feel homesick.", G("Think of your family hug later", "Something to look forward to.", "Pretend you're sick", "Feelings are okay to share.")),
    ]))
def e18(r):
    c = ["You're a great friend", "Your drawing is amazing", "Thanks for helping", "You're really brave", "I love your ideas", "You make me laugh"]
    return ("Compliment cards", "A real compliment notices something true.", [pick(r, "Which is a kind compliment?", x, ["You're weird", "Whatever", "That's ugly"]) for x in r.sample(c, N)])
def e19(r): return ("Patience waiting game", "Wait for the signal, then tap!", [motion("Wait until the bar is in the green zone, then tap.", s, z) for s, z in [(1.2, 30), (1.5, 26), (1.8, 22), (2.1, 20), (2.4, 18)]])
def e20(r):
    return ("Different is great", "Our differences make the world interesting.", C([
        ("A new kid speaks a different language.", G("Learn a word in their language", "Curiosity builds friendship.", "Laugh at their accent", "That's hurtful.")),
        ("A classmate uses a wheelchair.", G("Include them in the game", "Everyone can play.", "Leave them out", "Everyone wants to belong.")),
        ("Your friend eats different food at lunch.", G("Ask about it", "Food tells stories!", "Say it's gross", "That's unkind.")),
        ("Someone likes things you don't.", G("Ask them to show you", "You might find something new.", "Tell them they're wrong", "People like different things.")),
        ("A family looks different from yours.", G("Every family is special", "Families come in many kinds.", "Say it's not a real family", "All families are real.")),
    ]))

# ---------------- Trailblazers ----------------
def t01(r):
    s = [("Big test tomorrow", "Make a study plan"), ("Too many activities", "Drop one for now"), ("Argument with a friend", "Cool off, then talk"),
         ("Can't sleep from worry", "Write worries down"), ("Feeling overwhelmed", "Break it into small steps"), ("Stressed after school", "Move your body: walk or dance")]
    return ("Stress busters", "Name the stress, then pick a strategy.", [match(r.sample(s, 3)) for _ in range(N)])
def t02(r):
    return ("Peer pressure choices", "Strong people decide for themselves.", C([
        ("Friends are mocking a kid and want you to join.", G("Refuse and check on the kid", "That takes courage.", "Join in to fit in", "Fitting in isn't worth hurting someone.")),
        ("Friends dare you to skip class.", G("Say no and suggest meeting after", "Smart and social.", "Skip it", "You'd miss learning and break rules.")),
        ("A group shares answers in a test.", G("Do your own work", "Integrity matters.", "Copy them", "That's cheating.")),
        ("Friends want to post an embarrassing photo of someone.", G("Say it's not okay", "Protects someone's dignity.", "Laugh and share it", "Posts can hurt for a long time.")),
        ("Everyone's buying something you can't afford.", G("It's fine to say it's not for me", "Confidence.", "Lie that you have it", "Honesty is stronger.")),
    ]))
def t03(r):
    return ("Online kindness", "Behind every screen is a real person.", C([
        ("Someone posts a mean comment on a friend's video.", G("Report it and support your friend", "Upstander!", "Add another mean comment", "That's cyberbullying.")),
        ("A stranger asks for your address in a game chat.", G("Don't share and tell a grown-up", "Personal info stays private.", "Tell them", "Never share where you live.")),
        ("You're angry at a friend.", G("Talk in person, not in a post", "Calmer and private.", "Post about it", "Posts spread fast.")),
        ("A friend sends a funny photo of someone else.", G("Don't forward it", "Respect others' privacy.", "Send it to everyone", "That could embarrass them.")),
        ("You see fake news shared.", G("Check a trusted source first", "Think before you share.", "Share it quickly", "False info spreads.")),
    ]))
def t04(r):
    gr = ["I can't do it yet", "Mistakes help me learn", "I'll try another way", "Effort makes me better", "Challenges help me grow"]
    fx = ["I'm just not smart", "I'll never get it", "I give up", "Some people are naturally good", "If it's hard, I quit"]
    return ("Growth or fixed mindset?", "A growth mindset believes you can improve.", [sort(["Growth", "Fixed"], shuffled(r, [(x, 0) for x in r.sample(gr, 3)] + [(x, 1) for x in r.sample(fx, 3)])) for _ in range(N)])
def t05(r):
    steps = ["Pick a goal", "Break it into steps", "Set a deadline", "Track progress", "Celebrate"]
    return ("Goal-setting map", "Big goals are made of small steps.", [build(r, "Order the goal steps.", steps[i:i + 3 + (i % 2)]) for i in range(3)] + [build(r, "All the steps.", steps), build(r, "These steps.", steps[::2])])
def t06(r):
    return ("Empathy interviews", "Ask, listen, imagine their side.", C([
        ("A friend seems quiet today.", G("Ask: is everything okay?", "Open questions help.", "Ignore it", "They might need you.")),
        ("Your friend failed a test and is upset.", G("Say: that must feel rough", "Validating feelings helps.", "Say you got an A", "That hurts more.")),
        ("A teammate missed the winning shot.", G("Say: we win and lose as a team", "Supportive.", "Blame them", "They already feel bad.")),
        ("Your sibling's pet died.", G("Sit with them and listen", "Presence matters.", "Say get a new one", "That dismisses grief.")),
        ("A classmate is anxious about a speech.", G("Offer to listen to them practise", "Helpful.", "Say speeches are easy", "It's not easy for everyone.")),
    ]))
def t07(r):
    return ("Handling disappointment", "Feel it, then find the next step.", C([
        ("You didn't get the part in the play.", G("Ask what to work on for next time", "Turns disappointment into growth.", "Quit drama forever", "There will be other chances.")),
        ("Your trip got cancelled.", G("Plan something fun at home", "Flexible thinking.", "Sulk all week", "Feelings are okay, but don't get stuck.")),
        ("Your team lost the final.", G("Congratulate the winners", "Good sportsmanship.", "Refuse to shake hands", "Respect matters.")),
        ("Your science project didn't work.", G("Figure out why", "That's real science!", "Throw it away", "Failed experiments teach a lot.")),
        ("Your best friend chose another partner.", G("Find a new partner and enjoy it", "Resilient.", "Stop talking to them", "Friends can have other partners.")),
    ]))
def t08(r):
    return ("Leadership moments", "Leaders listen, include and help.", C([
        ("Your group can't agree.", G("Ask everyone for ideas and vote", "Fair leadership.", "Decide alone", "People feel left out.")),
        ("A teammate is struggling.", G("Offer help without taking over", "Supportive.", "Do it all yourself", "They won't learn.")),
        ("Your team made a mistake.", G("Own it and fix it together", "Accountability.", "Blame someone", "Leaders take responsibility.")),
        ("Someone has a quiet voice.", G("Ask what they think", "Includes everyone.", "Talk over them", "Every voice matters.")),
        ("The project is due tomorrow.", G("Make a plan and split tasks", "Organised.", "Panic", "Calm planning wins.")),
    ]))
def t09(r):
    bl = [("Crossed arms", "Closed off or upset"), ("Eye contact and nodding", "Listening"), ("Tapping foot", "Impatient"), ("Slumped shoulders", "Sad or tired"),
          ("Big smile", "Happy"), ("Looking away", "Uncomfortable")]
    return ("Body language clues", "Bodies talk too.", [match(r.sample(bl, 3)) for _ in range(N)])
def t10(r):
    h = ["Listens to you", "Respects your no", "Celebrates your wins", "Keeps secrets that are safe", "Apologises when wrong"]
    u = ["Makes fun of you", "Pressures you", "Only around when they need something", "Shares your secrets", "Gets angry if you have other friends"]
    return ("Healthy friendships", "Good friends make you feel safe and valued.", [sort(["Healthy", "Unhealthy"], shuffled(r, [(x, 0) for x in r.sample(h, 3)] + [(x, 1) for x in r.sample(u, 3)])) for _ in range(N)])
def t11(r): return ("Mindful minute", "Follow the rhythm with slow breaths.", [rhythm(r, 3, 4 + i) for i in range(N)])
def t12(r):
    plans = [["Homework", "Dinner", "Practice piano", "Free time", "Bed"], ["Pack bag", "Breakfast", "Leave for school"], ["Read the task", "Plan", "Do it", "Check it"],
             ["Write the list", "Do the hardest first", "Take a break", "Finish the rest"], ["Set alarm", "Wake up", "Stretch", "Get ready"]]
    return ("Managing my time", "Plan your time so the important things fit.", [build(r, "Order this plan sensibly.", p) for p in plans])
def t13(r):
    return ("Standing up to bullying", "Upstanders change things.", C([
        ("Someone is being pushed around at recess.", G("Get a teacher and stay with the kid", "Safe and supportive.", "Film it", "That doesn't help them.")),
        ("A group chat is mocking a classmate.", G("Say stop and tell an adult", "Brave.", "React with a laughing emoji", "That joins in.")),
        ("You're the one being bullied.", G("Tell a trusted adult", "You deserve help.", "Keep it secret forever", "You don't have to handle it alone.")),
        ("A kid is called names for their clothes.", G("Say 'not cool' and walk with them", "Upstander.", "Stay silent and laugh", "Silence can feel like agreement.")),
        ("Your friend is the one bullying.", G("Tell them it's hurting someone", "Real friends tell the truth.", "Join them", "Don't follow the crowd.")),
    ]))
def t14(r):
    steps = ["Say what you did", "Say sorry", "Explain how you'll fix it", "Ask how they feel"]
    return ("An apology that works", "A real apology names it and fixes it.", [build(r, "Order a real apology.", steps[i % 2:i % 2 + 3]) for i in range(4)] + [build(r, "The full apology.", steps)])
def t15(r):
    st = [("I'm so stupid", "I'm still learning"), ("I can't", "I can't yet"), ("This is too hard", "This will take effort"), ("I always mess up", "I can fix mistakes"),
          ("Nobody likes me", "Some people really like me"), ("I'll fail", "I'll do my best")]
    return ("Self-talk switch", "Swap the mean voice for a coach's voice.", [match(r.sample(st, 3)) for _ in range(N)])
def t16(r):
    return ("Screen time balance", "Balance screens with sleep, play and people.", C([
        ("It's bedtime and you're mid-game.", G("Save and stop", "Sleep helps your brain.", "Play till 2am", "You'll be exhausted.")),
        ("You've been on screens for 3 hours.", G("Go outside or read", "Balance feels better.", "Another 3 hours", "Your eyes and body need a break.")),
        ("Family dinner time.", G("Phone away", "Present with family.", "Text under the table", "It's family time.")),
        ("Homework vs a new video.", G("Homework first, video after", "Smart order.", "Video first, homework never", "Homework still needs doing.")),
        ("You feel grumpy after scrolling.", G("Take a break and move", "Notice how screens make you feel.", "Scroll more", "That may make it worse.")),
    ]))
def t17(r):
    q = [("How many hours of sleep do 9–12 year olds need?", "9–12 hours", ["4–5 hours", "15–18 hours"]), ("Too little sleep often makes people feel…", "Grumpy and unfocused", ["Super energetic", "Taller"]),
         ("Which helps you fall asleep?", "A calm routine", ["Scary movies", "Energy drinks"]), ("Screens before bed can…", "Keep your brain awake", ["Make you sleepier", "Do nothing"]),
         ("Good sleep helps your…", "Memory and mood", ["Hair colour", "Shoe size"])]
    return ("Sleep and mood", "Sleep is a superpower for feelings.", [pick(r, q, a, w) for q, a, w in q])
def t18(r):
    g = ["Something that made me laugh", "Someone who helped me", "Something I learned", "A place I love", "Something I'm proud of", "A meal I enjoyed"]
    return ("Gratitude journal", "Three good things, every day.", [build(r, "Choose 3 good things and order them.", r.sample(g, 3)) for _ in range(N)])
def t19(r):
    return ("Solving disagreements", "Win-win beats win-lose.", C([
        ("You and your sibling both want the TV.", G("Make a schedule", "Fair for both.", "Hide the remote", "That starts a fight.")),
        ("Your group can't pick a project topic.", G("Combine ideas", "Creative compromise.", "Insist on yours", "Others lose out.")),
        ("A friend says you cheated, but you didn't.", G("Calmly explain and replay the round", "Clears it up.", "Storm off", "Nothing gets solved.")),
        ("You want pizza, your friend wants burgers.", G("Pizza today, burgers next time", "Compromise.", "Refuse to eat", "That helps no one.")),
        ("You disagree with a teacher's mark.", G("Ask politely to go over it", "Respectful.", "Argue loudly in class", "Not the time or way.")),
    ]))
def t20(r):
    s = ["Kind", "Creative", "Funny", "Hard-working", "Brave", "Curious", "Good listener", "Organised"]
    return ("My strengths", "Knowing your strengths helps you use them.", [build(r, "Pick 3 strengths and rank them for you.", r.sample(s, 3)) for _ in range(N)])

GEN = {
    "cubs": [c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20],
    "explorers": [e01, e02, e03, e04, e05, e06, e07, e08, e09, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20],
    "trailblazers": [t01, t02, t03, t04, t05, t06, t07, t08, t09, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20],
}
