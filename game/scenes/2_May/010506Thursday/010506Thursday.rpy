label day010506:
$ timeOfDay = "Morning"

call calendar(1) from _call_calendar_31
$ calDate = calDate.replace(day=6, month=5, year=2004)

show morning at vspaz

pause 3.5

$ renpy.music.queue("Audio/Morning_ambience.ogg", channel='music', loop=True, fadein=1.5, tight=None)

scene suite
show screen currentdate
with transeye2

pause 1.0

narrator "You wake up in an unfamiliar room."
narrator "The ceiling above you has a crack in it that somewhat resembles [starter_preposition] [starter_species_name]."

pause 1.0

redmind "...Alright. Time to face the world."

$ PlaySound("Snore_F2.ogg")

narrator "Looking around, you see that there doesn't appear to be anyone else in the dorm, except Leaf, who you can hear snoring on the opposite couch."
narrator "A long train of drools {i}glops{/i} unattractively out of her mouth."

redmind @thinking "Makes sense. She's probably beyond exhausted after flying for so long."

menu: 
    "Let her sleep.":
        narrator "You ignore her, and move to the window."

    "Wake her up.":
        narrator "You gently prod Leaf's shoulder."

        $ PlaySound("Snore_F2.ogg")

        leaf @closedbrow talking2mouth "{size=30}...No, [first_name]... That's too much salad...{/size}"

        $ ValueChange("Leaf", 1, 0.5)

        red @confused "Huh?"

        narrator "She seems very deeply asleep. You decide to let her rest for a while longer..."

    "Splash some water on her.":
        $ AddEvent("Leaf", "Splashed")
        
        narrator "You pour some water into a cup, and..."

        $ PlaySound("splash.ogg")

        show suite at vpunch

        show leaf sadbrow surprisedmouth:
            xpos 0.3 alpha 0.0 ypos 2.0
            ease 0.5 alpha 1.0 ypos 1.0

        leaf @surprised "AH!"

        red @surprised "Oh, shit, sorry, I wasn't thinking!"

        leaf angry "You-- you {i}dick!{/i}"

        $ ValueChange("Leaf", -5, 0.3)

        show leaf:
            ease 0.3 xpos -0.2

        pause 2.0

        redmind @thinking "Yup. Not my brightest moment."

        red @sadbrow surprisedmouth "Sorry!"

        pause 2.0

narrator "Your thoughts return to last night..."

show suitenight at sepia 
show flashback
hide leaf
with dis

$ renpy.pause(1.0, hard=True)

show blue angry at sepia behind flashback with dis

pause 0.5

blue @talkingmouth "No way in hell am I letting you dorm here! This is {i}my{/i} suite, and I {i}just{/i} got rid of those other losers!"

show leaf angrybrow talking2mouth at rightside, sepia behind flashback with dis

pause 2.0

blue @talkingmouth "Fine, but there's no way I'm letting you sleep in one of the bedrooms! Gramps paid extra for this suite, and I'm using the whole damn thing! You can take the couch!"

show yellow angrybrow talkingmouth at leftside, sepia behind flashback with dis

pause 2.0

blue @talkingmouth "Fine, but if you think I'm going to {i}schlep{/i} my way over to your smelly old dorm in the morning and pick up {i}your{/i} crap, then--"

pause 1.0

show blank with splitfade

hide blue
hide suitenight
hide flashback
hide blank
hide leaf
hide yellow
with Dissolve(2.0)

narrator "...You don't remember what, exactly, was said, but your understanding of the situation is that Blue, Ethan, and Yellow have headed to dorm 151 to pick up your stuff."

show kitchen with splitfade

narrator "You wander into the suite's kitchen. The cafeteria is probably open, even with lessons being paused, but you don't overly feel like going out right now."

$ PlaySound("idea.ogg")

narrator "You spot a note on the fridge."

"{color=#3110dd}Blue's Handwriting{/color}" "{b}BLUE'S  RULES{/b}\n{w=0.5}
1. EVERYTHING has its place! Put the dishes away after you use them!{w=0.5}\n
1b. WASH THEM FIRST, YOU IDIOT!\n{w=0.5}"

"{color=#3110dd}Blue's Handwriting{/color}" "1b2. THAT MEANS USING SOAP! YOU {i}NEVER{/i} USED SOAP! WATER DOESN'T KILL GERMS!\n{w=0.5}
1b2i. YOU KNOW WHAT? FORGET IT! I'LL DO IT! YOU'RE GODDAMN US\n{w=0.5}
(It appears that Blue's pencil broke here.)"

narrator "The note continues like this for a while, laying out a rigorous schedule and procedure for everything from cooking, laundry, and dusting to taking out trash and... game nights?"

redmind @confusedeyebrows frownmouth "Blue has game nights?"

$ PlaySound("wood break.ogg")

show kitchen with vpunch

if (not HasEvent("Leaf", "Splashed")):
    blue @angry "HEY! WAKE UP!"

    leaf @surprised "Ah! Burglar!"

else:
    blue @angry "HEY! WHY ARE YOU SOAKING?!"

    leaf towel @angry bigblush "I'm getting changed! Don't come barging in here!"

blue @surprised "What? This is {i}my{/i} dorm."

red @sadbrow talkingmouth "Hey--"

show blue angry:
    xpos 1.2
    ease 0.5 xpos -0.2

pause 0.3

blue @talkingmouth "Move!"

pause 1.5

$ PlaySound("Door_Slam.ogg")

narrator "Blue barges past you into another room, slamming the door closed behind him. You thought you saw him carrying a pile of clothes... and a big, white, box?"

pause 1.5

scene suite
show leaf at leftside
show ethan
show yellow at rightside
with dis

if (not HasEvent("Leaf", "Splashed")):
    leaf @closedbrow talking2mouth "{i}Yawwwwwwn...{/i}"
    leaf @talking2mouth "Mmmorning. Mmrmph. I need coffee..."
else:
    leaf @angrybrow frownmouth "[ellipses]"

ethan @talkingmouth "Hey, [first_name]."

red @talkingmouth "Morning. You're up early."

ethan @happy "Hey, I hiked up a frigid mountain yesterday morning. This is nothing."

red @surprised "Hm?"

ethan @sad2eyes talkingmouth "You'll find out."

yellow @talkingmouth "I didn't really have time to talk last night before you passed out, so I just wanted to say welcome to Dorm 25, you three!"

leaf @surprised "Wait, aren't you new to this dorm, too?"

yellow @blush talkingmouth "Yes... but I spent a bunch of time here."
yellow @blush happy "It's really great that everyone can dorm together, now! That was a silly rule."

leaf @sarcastic "Tell me about it."

ethan @talkingmouth "Hey, how come you decided to shift dorms?"

if (HasEvent("Leaf", "AcceptedConfession")):

    show leaf frownmouth flirtbrow with dis

    narrator "Leaf looks at you, then back at Ethan with a deadpan expression."

    show leaf -frownmouth -flirtbrow with dis

    ethan @closedbrow talking2mouth "Yeah, dumb question."

else:
    leaf @talking2mouth "I've got my reasons."

    ethan @playfulbrow talking2mouth "You mean [first_name]?"

    leaf @sarcastic "I said reasons. {i}Plural.{/i}"

pause 1.0

$ PlaySound("drill.ogg")

pause 1.0

ethan @confusedeyebrows talking2mouth "What's Blue doing in that room?"

yellow @sadbrow happymouth "Oh, he's... assembling [first_name]'s bed."

ethan @closedbrow talking2mouth "Uh... why?"

yellow @closedbrow blush talkingmouth "Blue is... {i}a bit{/i} of a perfectionist. It would irritate him if the bed wasn't put together properly."

show suite 
show leaf surprisedbrow frownmouth
show yellow surprisedbrow frownmouth
show ethan surprisedbrow frownmouth
with vpunch

blue @angry "Yeah, and I've got to do this shit instead of training! You're such a waste of space--can't even put your own damn bed together!"

pause 1.0

show leaf -surprisedbrow -frownmouth
show yellow -surprisedbrow -frownmouth
show ethan -surprisedbrow -frownmouth
with dis

red @playfuleyes confusedeyebrows frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

ethan @talkingmouth "Hey, do you need any help?"

blue @angry "No! Don't come in yet! I'm not done!"

yellow @sadbrow happymouth "{size=30}And... that's Blue, in a nutshell.{/size}"

ethan @talkingmouth "Well, we've got a while before our Quarter Qlash matches, right? What do you guys wanna do? Some sort of roommate-bonding thing?"

leaf @embarrassedbrow talkingmouth "Sorry, Ethan, but I'm kinda behind on my schoolwork... missing an evening's worth of classes is seriously tough at Kobukan."

pause 1.0

yellow @surprised "Oh... yes, you must need to catch up as well, right, [first_name]?"

narrator "You nod."

ethan @talkingmouth "Yeah, that makes sense. Well, [first_name], what do you want to do before the second Quarter Qlash round?"
ethan @closedbrow talking2mouth "We'll probably have time to do one thing before that match, and one thing after, before we have to go to that Battle Team meeting."

leaf @surprised "Huh. I just realized four out of the five of us in this dorm are Battle Team members."

yellow @sadbrow happymouth "Yeah, I... noticed that."

leaf @surprised "Huh? Is something wrong?"

yellow @talkingmouth "No... I'm just not a massive fan of battles, so... um..."
yellow @surprised "Oh, but, you don't need to, like, not talk about battles or anything! I just don't think I'd be able to contribute to those conversations..."

leaf @surprisedbrow frownmouth "Hm."

leaf @surprised "Wait, you can talk to Pokémon."

yellow @sad "{size=30}Not exactly.{/size}"

leaf @sad "Do the Pokémon not like battling?"

yellow @happy "Oh! No, no they love it."

leaf @closedbrow talking2mouth "Phew. That was {i}not{/i} a moral dilemma I wanted to sign up for at this time in the morning."

show suite 
show leaf surprisedbrow frownmouth
show yellow surprisedbrow frownmouth
show ethan surprisedbrow frownmouth
with vpunch

blue @angry "It's eight goddamn fifty-four!"

pause 1.5

show leaf -surprisedbrow -frownmouth
show yellow -surprisedbrow -frownmouth
show ethan -surprisedbrow -frownmouth
with dis

ethan @confusedeyebrows playfuleyes talking2mouth "Is that meant to be late?"

call clearscreens from _call_clearscreens_121
scene blank2 
with Dissolve(1.0)

narrator "Eventually, the sound of construction coming from the room Blue was in ends, and he grumpily joins the rest of the dormmates as you prepare for the next Quarter Qlash match."
narrator "What would you like to do?"

$ attemptedtoleave = False

label preqq2:

scene blank2

$ pretype = None

menu:
    ">Study a type":
        call screen studyfocus
        $ selectedtype = _return 

        if (selectedtype == "Back"):
            jump preqq2

        redmind @thinking "With everyone studying together, I should probably be able to increase my proficiency by one."

        menu:
            "That's fine.":
                $ pretype = selectedtype

                $ IncreaseProficiency(selectedtype, 1)

                narrator "You and your new roommates crack open the books and pore over the readings you missed during your leave of absence."

                $ ValueChange("Leaf", 1, 0.2, False)
                $ ValueChange("Blue", 1, 0.4, False)
                $ ValueChange("Ethan", 1, 0.6)

                narrator "Bonds increased!"

            "Nevermind.":
                jump preqq2

    ">Train your Pokémon":
        $ aimlevel = AimLevel()
        $ expamount = math.floor(pow(aimlevel, 3) / 25)
        
        redmind @thinking "With everyone training together, I should probably be able to increase my Pokémon's experience by [expamount], if they're at level [aimlevel]."

        menu:
            "Let's do it.":
                narrator "You and your new roommates head out to the gym and throw your Pokémon at each other until everyone's good and warmed up for the upcoming battles."

                $ BattleTeamTraining()

                $ ValueChange("Leaf", 1, 0.2, False)
                $ ValueChange("Blue", 1, 0.4, False)
                $ ValueChange("Ethan", 1, 0.6)

                narrator "Bonds increased!"

            "Nevermind.":
                jump preqq2

    ">Leave the dorm alone" if not attemptedtoleave:
        narrator "You're...{w=0.5} not sure...{w=0.5} you want to.{w=0.5} Not just yet.{w=0.5} Not unless you {i}have{/i} to."

        $ attemptedtoleave = True

        jump preqq2

call clearscreens from _call_clearscreens_122
narrator "Preparations complete, you and your dormmates head to the Battle Hall."

show noon at vspaz
$ timeOfDay = "Noon"

pause 3.5

stop music fadeout 1.5
show blank as firstblank behind blank2
show stadium_full behind blank2
show blank as secondblank behind blank2
$ renpy.music.play("Audio/Stadium_crowd.ogg", channel='crowd', loop=True, fadein=1.5)
$ renpy.music.play("Audio/Stadium_chant.ogg", channel='crowd2', loop=True, fadein=1.5)

$ renpy.pause(0.75, hard=True)

$ renpy.music.queue("Audio/Music/Indigo_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/Indigo_Loop.ogg", channel='music', loop=True, tight=None)

$ renpy.pause(1.0, hard=True)

hide blank2 with transball
$ renpy.pause(0.25, hard=True)
hide secondblank with dis

show stadium_full:
    subpixel True
    zoom 3.0 alpha 0.65 xalign 0.15 ypos 2600
    ease 1.25 alpha 1.0 xalign 0.0 ypos 3000
    xalign 0.85 alpha 0.65 ypos 2600
    ease 1.25 alpha 1.0 xalign 1.0 ypos 3000
    xalign 0.5 alpha 0.4 ypos 2400
    ease 1.0 alpha 1.0 zoom 1.0 ypos 1080

show lightbeam1 as beam1:
    pause 2.75
    zoom 0.6 alpha 0.0 yalign 0.9 xpos 0 rotate 40
    block:
        ease 0.25 alpha 0.5
    pause 0.3
    block:
        ease 1.0 rotate -40
        pause 0.5
        ease 1.0 rotate 40
        pause 0.5
        repeat
    
show lightbeam1 as beam2:
    pause 2.75
    zoom 0.6 alpha 0.0 yalign 0.9 xpos -300 rotate -40
    block:
        ease 0.25 alpha 0.5
    pause 0.1
    block:
        ease 1.0 rotate 40
        pause 0.5
        ease 1.0 rotate -40
        pause 0.5
        repeat

show lightbeam1 as beam3:
    pause 2.75
    alpha 0.0 yalign 0.8 xpos -400 rotate -40
    block:
        ease 0.25 alpha 0.6
    pause 0.2
    block:
        ease 1.0 rotate 40
        pause 0.5
        ease 1.0 rotate -40
        pause 0.5
        repeat
        
show lightbeam1 as beam4:
    pause 2.75
    alpha 0.0 yalign 0.8 xpos -1400 rotate 40
    block:
        ease 0.25 alpha 0.6
    block:
        ease 1.0 rotate -40
        pause 0.5
        ease 1.0 rotate 40
        pause 0.5
        repeat
        
pause 3.5

show screen currentdate
show lisia behind beam1 
with dis

lisia @happy "Laaaaaadies and {i}gentlemen!{/i} It's day two of the first round of the two hundred and twenty-eighth annual Quarter Qlashes!"
lisia @xdbrow happymouth "And we get to start on time today! Isn't that {i}great?{/i}"

$ PlaySound("crowd_cheer.ogg")

pause 1.0

lisia @happy "That's what I like to hear! Once again, the one and only Lisia, World Contest Champion, is here to announce for you!"
lisia @angrybrow happymouth "Yesterday, we saw hundreds of incredible battles! Everyone did their best--trainer {i}and{/i} Pokémon! Now, who thinks we'll see even better battles today?"

$ PlaySound("crowd_cheer.ogg")

pause 1.0

lisia @happy "I know we will!"
lisia @talkingmouth "I saw a bunch of really impressive battlers yesterday! Especially those in groups one, seven, nineteen, and forty-two!"
lisia @happy "Why don't we take a quick little look at one of the battlers that really impressed me yesterday?"

$ PlaySound("crowd_cheer.ogg")

pause 1.0

lisia @talkingmouth "Hi there! What's your name?"

show lisia:
    ease 0.5 xpos 0.25

show wally behind beam1 with dis:
    xpos 0.75 xzoom -1

wally @talkingmouth "...Wait, is this broadcasting?"

lisia @surprised "Huh?"

wally judgingeyebrows judgingeyes surprisedmouth  @talkingmouth "I mean, am I on camera right now?"

lisia @happy "You sure are! Say hi to--"

show wally:
    xpos 0.75 xzoom -1
    ease 0.3 rotate 45 ypos 1.9
show lisia surprisedbrow frownmouth with dis
show stadium_full with vpunch

pause 1.0

lisia @talkingmouth "Excuse me?"

wally @talkingmouth "Sorry, I'm not good with cameras. It's, uh, it's against my religion. To be onscreen."

narrator "As you watch the green-haired man's bizarre behavior, you vaguely seem to recall glimpses of green hair vanishing around the corners at Kobukan."

lisia -surprisedbrow -frownmouth -surprised @sadbrow happymouth "Hah hah... okay, well, absolutely no offense intended! Perhaps we can find someone else around here, then?"

show brock surprisedbrow frownmouth at rightside behind beam1 with dis:
    xzoom -1

lisia @talkingmouth "Hi! Is there anything you'd like to tell the folks back at--"

show brock:
    xpos 0.75
    ease 0.3 rotate 45 ypos 1.9
show lisia surprisedbrow frownmouth with dis
show stadium_full with vpunch

brock @talkingmouth "Yup, sorry, sis. Same deal, with me. Actually, I'm not even allowed to show my face."

lisia -surprisedbrow -frownmouth -surprised @angry ".{w=0.5}.{w=0.5}.{w=0.5}Okay."

redmind @confusedeyebrows frownmouth "Wasn't that the pervert from the pool?"

hide brock
hide wally

lisia @happy "Seems we're having some difficulty finding an interviewee, folks! Maybe you could just put your hands up?"

narrator "About a dozen people put their hands up. Lisia scans the battlers, then her eyes lock onto someone nearby."

lisia @happy "Oh, great! You--yes, {i}you!{/i} {size=30}You look like you won't get me cancelled!{/size}"

show bianca behind beam1 with dis:
    ypos 1.0 xpos 0.75
    block:
        ease 0.5 ypos 1.1
        ease 0.5 ypos 1.0
        repeat 5

bianca @happy "Hiiiii!~"

lisia @talkingmouth "Hi, sweetie! What's your name?"

bianca @happy "Hi, Lisia! My name's Bianca. I'm a {i}really{/i} big fan of yours."

lisia @happy "That's awesome! I'm always happy to meet a fan. Where do you come from, Bianca?"

bianca @talkingmouth "Oh, Nuvema Town! Originally! Though I moved to Aspertia a few years back, and--"

lisia @sadbrow talking2mouth "Sorry, sweetheart. Runtimes."

bianca @happy "Oh, okaaaay!~"

lisia @talkingmouth "Well, can you think of anyone back home in Nuvema who might be watching this battle?"

bianca @happy "Yup! My Daddy!"

lisia @happy "Aw! And you're planning to win this battle, so he can see, right?"

bianca @surprised "Gosh, I sure hope so!"

pause 1.0

narrator "The crowd laughs.{w=0.5} ...Something about that rubs you the wrong way."

lisia @happy "Well, one last question, then, before we begin the second round. Is there anything you'd like to say to your Daddy?"

bianca @happy "Sure thing!"

narrator "Bianca looks directly into the camera, her smile absolutely unflinching."

show lisia surprisedbrow frownmouth with dis

bianca @talkingmouth "Daddy? Thank you so much for kicking me out of the house."

$ renpy.music.set_volume(0.5, 2.0, channel="crowd")
$ renpy.music.set_volume(0.5, 2.0, channel="crowd2")

lisia @talkingmouth "Um... sorry, what was that?"

bianca @happy "Oh, I'm just saying thanks so much to my Daddy."
bianca @shadow talkingmouth "If you hadn't been such an insecure pig--if the thought of your darling baby girl becoming something more than someone's wife hadn't been so repulsive--then I never would have made it here."

lisia @sadbrow talkingmouth "Um... Bianca..."

$ renpy.music.set_volume(0.0, 2.0, channel="crowd")
$ renpy.music.set_volume(0.0, 2.0, channel="crowd2")

bianca @happy "You gave me the opportunity to spread my wings and realize how far I could fly when I wasn't tied down by your expectations."
bianca @soullesseyes angryeyebrows happymouth "I really hope you're watching, Daddy! Remember, I'm doing all this to prove you wrong!"

lisia @sad "Bianca, please--"

bianca @soulless2eyes angrymouth angryeyebrows "But just in case you {i}aren't{/i} watching, I'm talking to Melvin Whittaker, who lives at 413 Oldline Ro--"

lisia @angry "Cut the feed!"

pause 1.0

lisia @closedbrow talking2mouth "Was that necessary?"

bianca @happy "Hehe! Ooopsy-daisy!~"

hide bianca with dis

pause 2.0

narrator "Lisia knuckles her forehead in silence for a few moments. And then..."

show blank

pause 0.1

hide blank 

pause 0.1

show lisia:
    ease 0.5 xpos 0.5

lisia -surprisedbrow -frownmouth @happy "Wow! What passion, ladies and gentlemen!"

$ renpy.music.set_volume(1.0, 0.5, channel="crowd")
$ renpy.music.set_volume(1.0, 0.5, channel="crowd2")

lisia @talkingmouth "That's the power of Pokémon battles for you! Everyone's fighting for something different! Some of us battle to protect our friends! Some to achieve our dreams!"
lisia @happy "All that matters is that you put your whole heart into your goal! Isn't that great, everyone?"

$ PlaySound("crowd_cheer.ogg")

pause 1.0

redmind @surprisedbrow frownmouth "Damn. This woman's a professional."

lisia sadbrow frownmouth "{size=30}I need an aspirin...{/size}"

pause 1.0

lisia -sadbrow -frownmouth @happy "Oh! Battler number fifteen. Would you take your place, please?"

red @happy "Sure."

hide lisia with dis

pause 1.0

show lace behind beam1 with dis

red @happy "Hello, Ma'am!"

lace @talkingmouth "Hello, young man. How pleasant it is to see that not all Kobukanian students are utterly lacking in manners."

red @surprised "Huh? Did something happen?"

lace @angry "Something most certainly did. Yesterday? Not twenty-four hours ago? I was stopped from entering this very Battle Hall."

red @angrybrow talking2mouth "What?! Who did that?"

lace @angry "I didn't catch his name. Some sandy, spiky-haired ruffian. Quite rude. He said he'd 'smell me later'! As though I had {i}any{/i} sort of odor."

pause 1.0

red @sweat closedbrow talkingmouth "...Ah."

pause 1.0

red @sweat happy "Well, let's battle!"

lace "Yes. Good luck, young man!"

python:
    trainer1 = MakeRed(2)
    trainer2 = Trainer("lace", TrainerType.Enemy, [Pokemon("Frillish", level=13), Pokemon("Ducklett", level=14), Pokemon("Wishiwashi", level=14), Pokemon(393, level=14)], number=2)

call Battle([trainer1, trainer2], specialmusic=("audio/music/swordshieldgym-intro.ogg", "audio/music/swordshieldgym-loop.ogg"), customexpressions=["red", "red angrybrow happymouth", "lace", "lace angry"]) from _call_Battle_115 
$ battlehistory["Lace1"] = _return

if (not WonBattle("Lace1")):
    jump gameover

$ renpy.music.queue("Audio/Music/Indigo_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/Indigo_Loop.ogg", channel='music', loop=True, tight=None)

show lace behind beam1 with dis

red @happy "Seems you're a fan of Water-types, then?"

lace @talkingmouth "Yes, quite so. Seems I got swept away in this battle, though... Ah, well."

red @talkingmouth "It was fun, anyway. Sorry about that delay yesterday."

lace @angry "Oh, I'm sure you had nothing to do with it. I've quite a mind to lodge a complaint, though. I'd heard rumors that Kobukan Academy was declining in quality, but..."

hide lace with dis

pause 1.0

redmind @angrybrow frownmouth "What did she mean by that?"

pause 1.0

lisia @happy "Great battles, everybody! I'm looking forward to seeing you return tomorrow for the grand finale of the first round!"

call clearscreens from _call_clearscreens_123
scene blank2 with splitfade

show afternoon at vspaz
$ timeOfDay = "Afternoon"

pause 3.5

stop music fadeout 1.5
stop music fadeout 1.5 channel "crowd"
stop music fadeout 1.5 channel "crowd2"

show screen currentdate with dis

queue music "audio/music/NewFriends_start.ogg" noloop
queue music "audio/music/NewFriends_loop.ogg"

narrator "You return to your dorm. What would you like to do before you go to the Battle Team meeting?"

$ attemptedtoleave2 = False

label postqq2:

scene blank2

menu:
    ">Study a type":
        call screen studyfocus
        $ selectedtype = _return 

        if (selectedtype == "Back"):
            jump postqq2
        elif (selectedtype == pretype):
            redmind @thinking "We've already studied that type today..."

            jump postqq2

        redmind @thinking "With everyone studying together, I should probably be able to increase my proficiency by one."

        menu:
            "That's fine.":
                $ IncreaseProficiency(selectedtype, 1)

                narrator "You and your new roommates crack open the books and pore over the readings you missed during your leave of absence."

                $ ValueChange("Leaf", 1, 0.2, False)
                $ ValueChange("Blue", 1, 0.4, False)
                $ ValueChange("Ethan", 1, 0.6)

                narrator "Bonds increased!"

            "Nevermind.":
                jump postqq2

    ">Train your Pokémon":
        $ aimlevel = AimLevel()
        $ expamount = math.floor(pow(aimlevel, 3) / 25)
        
        redmind @thinking "With everyone training together, I should probably be able to increase my Pokémon's experience by [expamount], if they're at level [aimlevel]."

        menu:
            "Let's do it.":
                narrator "You and your new roommates head out to the gym and throw your Pokémon at each other until everyone's good and warmed up for the upcoming battles."

                $ BattleTeamTraining()

                $ ValueChange("Leaf", 1, 0.2, False)
                $ ValueChange("Blue", 1, 0.4, False)
                $ ValueChange("Ethan", 1, 0.6)

                narrator "Bonds increased!"

            "Nevermind.":
                jump postqq2

    ">Leave the dorm alone" if not attemptedtoleave2:
        narrator "You don't think you have the willpower to leave alone...{w=0.5} not just yet.{w=0.5} Not {i}quite{/i} yet."

        $ attemptedtoleave2 = True

        jump postqq2

call clearscreens from _call_clearscreens_124
scene blank2 with splitfade

show evening at vspaz
$ timeOfDay = "Evening"

pause 3.5

show screen currentdate with dis

scene suitenight 
show blue frownmouth:
    xpos 0.2
show leaf:
    xpos 0.8
show yellow:
    xpos 0.6
show ethan:
    xpos 0.4    
with Dissolve(3.0)

pause 1.0

yellow @talkingmouth "How did you all do with your battles?"

blue @closedbrow talking2mouth "Some rando with trash Pokémon. I don't even remember what they were."

ethan @closedbrow talking2mouth "Yeah, I was fine, too."

leaf @talking2mouth "No problems here."

pause 2.0

blue @surprisedbrow talkingmouth "Well?"

yellow @blush happy "I... I lost."

ethan @surprised "What?!"

yellow @sadbrow happymouth "I only have a Pichu, and my Chuchu has barely ever battled..."
yellow @happy "My opponent was a nice lady from the city, actually. She runs a small cafe. I'm going there with a friend this weekend."

leaf @happy "Sounds like, even if you didn't win, you got something from the battle, then!"

yellow @happy "Yes, that's a nice way to think about it."

blue -frownmouth @closedbrow talking2mouth "Psh. The only win that matters is the one where you completely beat your opponent."

pause 1.0

yellow @angrybrow talkingmouth "You mean like when Dawn--"

blue @angry "Hey! It's getting late. Shouldn't we go to that Battle Team meeting?"

leaf @sarcastic "It's like a ten-minute walk, and we're half an hour out...?"

blue angry "Well, you losers can stick around and {i}be late{/i} if you want. I'm heading out!"

show blue:
    ease 0.3 xpos -0.2

pause 0.3

$ PlaySound("door_slam.ogg")

pause 0.7

redmind @closedbrow frownmouth "...Hilbert and Blue should bond over their mutual love of slamming doors."

pause 1.0

leaf @talking2mouth "Hey, [first_name], you..."

pause 1.0

leaf @closedbrow talkingmouth "Uh, maybe I'll leave this one to Ethan. I'm going to the Battle Hall."

show leaf:
    ease 0.5 xpos 1.2

pause 1.0

show yellow surprisedbrow frownmouth:
    xpos 0.6
    pause 1.0
    ease 0.5 xpos 1.2
show leaf:
    ease 0.5 xpos 0.68
    pause 0.5
    ease 0.5 xpos 1.2

pause 2.0

redmind @confusedeyebrows frownmouth "Hm? What was that about?"

ethan @talking2mouth "Right. So... you good, man?"

red @talkingmouth "Yeah."

pause 1.0

ethan @sad2eyes talkingmouth "'Kay. You just haven't been talking very much."

red @sweat sadbrow talkingmouth "Oh... yeah, I guess I haven't."

pause 1.0

ethan @sadbrow happymouth "And, y'know, you're going to have to tell everyone in the Battle Team about what happened in, like, half an hour..."
ethan @sad2eyes talking2mouth "Assuming Erina even lets you get a word out, of course."

red @sadbrow talking2mouth "Erina? You mean Erika? I guess she's not happy."

ethan @sad2eyes talking2mouth "You'll... see."

red @closedbrow talking2mouth "Great."

pause 1.0

ethan @talkingmouth "You wanna head out, then?"

red @talkingmouth "Sure. We'll be a bit early, but sure."

scene blank2 with Dissolve(2.0)

pause 1.0

redmind @thinking "Okay... moment of truth..."

scene blank with splitfade

call clearscreens from _call_clearscreens_125
scene blank2 with splitfade

show night at vspaz
$ timeOfDay = "Night"

pause 3.5

show screen currentdate with dis

pause 1.0

stop music fadeout 1.5

scene stadium_empty with Dissolve(2.0)

$ renpy.music.play("Audio/bigcrowdloop.ogg", channel='crowd', loop=True, fadein=1.5)

narrator @talkingmouth "As you walk into the Battle Hall, you notice that Kobukan Academy staff are swarming over the bleachers, cleaning up spilt drinks, hot dogs, and popcorn. The sound fills the air."

$ renpy.music.stop(channel='crowd', fadeout=10.0)

show blue frownmouth:
    xpos 1.0/10.0
show leaf:
    xpos 6.0/10.0
show sonia sadbrow:
    xpos 9.0/10.0
show ethan:
    xpos 4.0/10.0
show silver angrybrow:
    xpos 2.0/10.0
show bea behind ethan:
    xpos 3.0/10.0
show dawn sadbrow frownmouth behind ethan:
    xpos 5.0/10.0
show hilbert angrybrow behind sonia:
    xpos 8.0/10.0
show erika angrybrow frownmouth:
    xpos 7.0/10.0
with dis

pause 1.0

redmind @thinking "Not a lot of friendly faces..."

pause 1.0

redmind @confusedeyebrows frownmouth "It looks like they're all looking at Erika...? Wait, are they waiting for her to say something?"

erika "{w=0.5}.{w=0.5}.{w=0.5}."

show erika:
    ease 0.5 ypos 1.2 zoom 1.3 xpos 0.5

erika "{w=0.5}.{w=0.5}.{w=0.5}."

redmind @sadbrow frownmouth "She's just... staring. Is she trying to intimidate me? This would be scarier if she wasn't even shorter than Whitney."

erika @surprisedmouth "{size=30}[first_name] [last_name]. Why have you chosen to come back?{/size}"

redmind @frownmouth "Wow. Okay. Her slaps might be Wynaut-strength, but her scorn is like a Houndoom's flames..."

erika @surprisedmouth "{size=30}Do you have any concept of the embarrassment you've caused this school? Do you have any idea how much shame you've brought unto Kobukan's lauded battle team?{/size}"
erika @angrymouth "{size=30}Every victory of ours from this point on will be stained by the knowledge that one of our members achieved their victory through dishonorable means.{/size}"

show smoke behind erika:
    animation
    alpha 0.0 yalign 3.0 xpos 0.15
    parallel:
        ease 3.0 yalign 0.5
    parallel:
        ease 0.5 alpha 1.0
        pause 0.5
        ease 3.0 alpha 0.0 

show leaf surprisedbrow frownmouth
show sonia surprisedbrow frownmouth
show ethan surprisedbrow frownmouth
show dawn surprisedbrow frownmouth
show blue surprisedbrow frownmouth
show ethan surprisedbrow frownmouth
show hilbert surprisedbrow frownmouth
show bea surprisedbrow frownmouth
with dis

redmind @frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

erika @angry "{size=30}Have you no response?{/size}"

pause 1.0

erika @closedbrow angrymouth "Disgraceful."

stop music fadeout 1.5

queue music "Audio/Music/fuchsia_start.ogg" noloop
queue music "audio/music/fuchsia_loop.ogg"


show screen songsplash("Fuchsia City", "Zame")

pause 1.0

show blank
show janine behind blank:
    xpos 0.25

pause 0.1

hide smoke
hide blank

pause 1.0

janine @closedbrow talking2mouth "Line up."

show blue:
    ease 0.8 xpos 1.5
show leaf:
    ease 0.5 xpos -0.5
show ethan:
    ease 0.4 xpos 1.5
    pause 0.2
    ease 0.4 xpos -0.5
show silver:
    ease 0.5 xpos -0.5
show bea:
    ease 0.5 xpos 1.5
show dawn:
    ease 0.2 xpos -0.5
show sonia:
    ease 0.5 xpos 1.5
show hilbert:
    ease 0.5 xpos -0.5

pause 1.0

erika @angrymouth "Madam Janine."

janine @talking2mouth "I'm not a madam. I'm only a couple years older than you."
janine @talking2mouth "And I believe I told you what I expect of you right now."

pause 1.0

erika @closedbrow talkingmouth "Of course."

show erika:
    ease 0.5 xpos 1.2 ypos 1.0 zoom 1.0 alpha 0.0

hide blue
hide ethan
hide leaf
hide silver
hide bea
hide dawn
hide sonia
hide hilbert

janine @talking2mouth "...I'm going to check in with all of you, now. {i}Then{/i}, I'll open the floor to other discussion."

janine @closedbrow talking2mouth "I saw most of your matches. You're all still in, right?"

$ PlaySound("short_crowd_talking.ogg")

pause 1.0

narrator "There are a few muttered words of assent."

janine @talking2mouth "Good. I'm not going to be the first Battle Team Captain who had a Battle Team member lose in round one."

hilbert @sadbrow talkingmouth "{size=30}...It's not going to be up to you...{/size}"

janine @talking2mouth "Alright. Now, anyone who wants to say something, you can."

pause 1.0

narrator "Janine looks pointedly at you."

pause 1.0

show janine surprisedbrow with dis

narrator "But..."

pause 1.0

show janine sadbrow with dis:
    ease 0.5 xpos 0.25

show erika frownmouth:
    xpos 0.75 ypos 1.2 zoom 1.3 alpha 0.0
    ease 0.5 ypos 1.0 zoom 1.0 alpha 1.0

erika @surprisedmouth "[first_name] has betrayed our trust, dishonored the battle team, and association with him will bruise our reputation forever on."
erika @closedbrow surprisedmouth "If we ever want to participate in battle competitions with other academies--Naranjuva or Blueberry, for example--his presence is a direct impediment."

pause 1.0

erika @surprisedmouth "We cannot allow ourselves to become a team that wins at any cost."

pause 1.0

erika @angry "Therefore, I move that [first_name] be dishonorably dismissed from the Battle Team."

redmind @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

show leaf angry:
    xpos 0.6 ypos 1.2 zoom 1.3 alpha 0.0
    ease 0.5 ypos 1.0 zoom 1.0 alpha 1.0

show ethan angry:
    xpos 0.4 ypos 1.2 zoom 1.3 alpha 0.0
    ease 0.5 ypos 1.0 zoom 1.0 alpha 1.0

leaf @talking2mouth "Well, I {i}move{/i} that you take that awful idea and flush it down the toilet!"

ethan @talkingmouth "Yeah! [first_name] did literally nothing wrong! He {i}can't{/i} control minds!"

erika @surprisedmouth "I have just as much evidence to believe he does as you do to believe he doesn't."
erika @angry "How am I supposed to interpret his silence aside from guilt?"

leaf @talking2mouth "Oh, I don't know, maybe {i}trauma?!{/i}"

erika @closedbrow surprisedmouth "That seems unlikely."

hide leaf
hide ethan
with dis

show bea with dis:
    xpos 0.5

bea @talkingmouth "Perhaps we should simply put it to a vote."

pause 1.0

janine @talking2mouth "Everyone, get out a piece of paper. Write on it 'eject' or 'keep.'"

hide bea with dis

leaf @surprised "What?!"

janine @talking2mouth "Do it now. You have two minutes to pass them in."

pause 2.0

$ PlaySound("short_crowd_talking.ogg")

narrator "Everyone quickly begins digging scrap paper out of their pockets, and pens are shared around. Sonia passes you a piece of paper, guiltily."

sonia @sadbrow happymouth "Right. Good luck, then."

narrator "What will you write?"

$ playervote = False

menu:
    "\"Eject\"":
        $ playervote = True

    "\"Keep\"":
        pass

narrator "You do so."

narrator "After a minute of frantic scribbling, the votes are passed into Janine. She looks over the paper dispassionately, her face betraying no emotion."

janine "{w=0.5}.{w=0.5}.{w=0.5}."

python:
    bluevote = False#can't beat red if he's off the team
    silvervote = False#everyone can be redeemed. 
    leafvote = False#c'mon
    ethanvote = False#c'mon^2
    beavote = False#knows about Frienergy through Nate
    soniavote = (False if GetRelationshipRank("Sonia") + GetRelationshipRank("Nessa") > 0 else True)#trusts if she knows
    persondex["Sonia"]["Events"].append("VotedYes" if soniavote else "VotedNo")
    dawnvote = (False if GetRelationshipRank("Dawn") else True)#trusts if she knows
    persondex["Dawn"]["Events"].append("VotedYes" if dawnvote else "VotedNo")
    erikavote = True#she's the person who started this whole thing
    hilbertvote = True#knows that Red's going to lose to Dawn anyway

    truevotes = playervote + bluevote + silvervote + leafvote + ethanvote + beavote + soniavote + dawnvote + erikavote + hilbertvote

if (truevotes == 5):
    janine @talking2mouth "It's split evenly."
elif (truevotes == 4):
    janine @talking2mouth "Four ejects to six keeps."
elif (truevotes == 3):
    janine @talking2mouth "Three ejects to seven keeps."
elif (truevotes == 2):
    janine @talking2mouth "Two ejects to eight keeps."

pause 1.0

$ PlaySound("paperrip.ogg")

janine -sadbrow @talking2mouth "And it doesn't matter. This is not a democracy. I have made a decision, and my decision is that [first_name] is staying on the team."

erika @surprised "But... you said... that the togetherness of the team was your priority?"

janine @angrybrow talking2mouth "I do. And by trying to eject another team member, you're the one who is causing problems. Not him."

erika @sadmouth "But... his powers..."

hide erika with dis

janine @talking2mouth "Let's put these rumors to rest. [first_name], give an explanation of your powers. Now."

pause 1.0

red "{w=0.5}.{w=0.5}.{w=0.5}."

pause 1.0

narrator "You open your mouth to speak... but you find that you can't."

janine @surprisedbrow talking2mouth "[first_name]? What's wrong? You told me before..."

red @sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."

janine @closedbrow talkingmouth "Okay. I didn't expect this. Change of plans, then."

pause 1.0

janine @talking2mouth "The point is that he's staying, and his powers aren't mind control. They're, like... mind influence. We don't feel our own feelings, we feel--"
janine @closedbrow talking2mouth "No, wait, that just makes it sound worse. Okay, his power makes Pokémon do whatever he says, which is--"
janine @sad "...No, that's not it, either."

pause 1.0

hilbert @talkingmouth "...Why are we even bothering with this?"

janine @angrybrow talking2mouth "What?"

hilbert @closedbrow talking2mouth "He's going to be out of the Quarter Qlashes tomorrow anyway."

janine @surprised "What do you mean?"

show hilbert with dis

hilbert @closedbrow talkingmouth "Why am I always the one that has to notice these things...?"

pause 1.0

hilbert @talkingmouth "Look, [first_name]'s battler number for the Quarter Qlashes is fifteen, right?"
hilbert @sadbrow talkingmouth "He's in the second bracket of eight. That means he's in competition with everyone with numbers nine through sixteen."
hilbert @closedbrow talkingmouth "He's already beaten his side of the bracket--numbers thirteen through sixteen."
hilbert @talkingmouth "That means he's going to need to battle the winning trainer from the group of nine through twelve."

hide hilbert with dis

narrator "There's silence for a moment, and then you hear a little gasp."

stop music fadeout 1.5

queue music "audio/music/legendary.ogg" fadein 5.0

pause 2.0

narrator "You feel goosebumps crawl up your back as you, and the entire rest of the Battle Team, turn to look."

show dawn sadbrow surprisedmouth with Dissolve(3.0)

dawn sadbrow frownmouth @sadmouth "I... I'm... number eleven."

pause 1.0

play music "<from 10>audio/crowdargue.ogg" channel "crowd"
play music "audio/crowdargue2.ogg" channel "crowd2"

janine @surprised "What? How did I miss--"

hilbert @closedbrow talkingmouth "You were watching every group you weren't part of like a hawk. But you battled in the same group as Dawn and [first_name]."
hilbert @sadbrow talkingmouth "This whole vote was pointless. We already know the outcome."
hilbert @closedbrow talking2mouth "There are two hundred and forty groups of eight battling at this location. With nine of us, the odds of any two of us ending up in the same group was 14.08%%."

stop music fadeout 1.5

janine surprisedbrow frownmouth @surprised "...I should've split us up into different areas."
janine @angry "Goddamn it! What a pathetic rookie mistake! What the hell was I thinking? What's my problem?!"

narrator @talkingmouth "Your senses dull as the sinking, drowning feeling that everything--flying back to Kobukan, winning the previous two rounds--was pointless settles on you."

pause 1.0

show janine -surprisedbrow -frownmouth -surprised
show blank

pause 0.1

hide blank

pause 1.0

stop music
stop music channel "crowd"
stop music channel "crowd2"

queue music "Audio/Music/fuchsia_start.ogg" noloop
queue music "audio/music/fuchsia_loop.ogg"


show screen songsplash("Fuchsia City", "Zame")

janine -surprisedbrow -frownmouth -surprised @closedbrow talking2mouth "Quiet."

pause 1.0

janine @talking2mouth "I need to think about what to do."

dawn @sadmouth "I... I can just... drop ou--"

janine @talking2mouth "No, you can't."

pause 1.0

dawn @sadmouth "I {i}could{/i}, though." 

janine @closedbrow talking2mouth "I will not permit you to." 

dawn @talkingmouth "I'm... I'm {i}really{/i} sorry, but I don't think you can actually stop me."

janine "{w=0.5}.{w=0.5}.{w=0.5}."

dawn @sadmouth "Um... what are you doing?"

janine "{w=0.5}.{w=0.5}.{w=0.5}."

dawn @sadmouth "J-Janine? I... I didn't mean to talk back, I'm sorry..."

janine "{w=0.5}.{w=0.5}.{w=0.5}."

dawn @sadmouth "{size=30}Okay, I won't quit, I'm sorry, please just stop staring at me...{/size}"

janine @closedbrow talking2mouth "That's better."

pause 1.0

janine @talking2mouth "[first_name]."

pause 1.0

janine @talking2mouth "Can I trust that you won't quit, either?"

narrator "You hang your head."

show janine sad with dis

narrator "Would it really be worth it to go out there tomorrow and be defeated so publicly and humiliatingly?"

narrator "You look dejectedly down at the ground. You open your mouth and say--"

$ renpy.music.play("Audio/Pokemon/pikachu_angry1.ogg", channel="altcry", loop=None)

show janine surprisedbrow frownmouth with dis

red @surprised "Ow!"

pikachu angry "Piii."

$ renpy.music.play("Audio/Pokemon/pikachu_angry2.ogg", channel="altcry", loop=None)

pikachu angry_2b "Pika! Pi, pi, pika. Pika, pika, pika!"

red @confused "You bit my ear."

pikachu angry_3 "Pika, pika!"

red @closedbrow talking2mouth "I think you drew blood..."

$ renpy.music.play("Audio/Pokemon/pikachu_angry3.ogg", channel="altcry", loop=None)

pikachu angry_3 "Pika! Pika, pikachu!"

red @surprised "Alright, alright! I won't quit. But... geez. Where'd {i}this{/i} motivation come from, huh?"

pikachu @cocky "Pika."

narrator "[pika_name] puffs out his chest and looks defiantly at Dawn. You can feel his small, 13-pound body quiver with fury."

red @closedbrow talking2mouth "Cool it, buster. The battle isn't until tomorrow."

janine @talking2mouth "You're talking again."

red @surprised "Oh."

pause 1.0

red @talkingmouth "Yeah. I guess I am."

janine @closedbrow talking2mouth "...I don't want to be the first Captain to have a Battle Team member lose in the first round."
janine @talking2mouth "But it looks like that's already happened. God damn it. This was {i}so{/i} avoidable, if I just hadn't been lazy... I separated our signups the past two years, but with a smaller team this year, I thought... {i}ugh.{/i}"

dawn @talkingmouth "If... if I drop out of the Battle Team, then, if [first_name] beats me, then... technically... no Battle Team member will have lost."

janine @talking2mouth "But [first_name] would still need to beat you. If we were trying to avoid damaging the Battle Team's reputation, then... [first_name] leaving the Battle Team, and being beaten by you, would solve most of our issues..."

red @talking2mouth "...I'm not planning on quitting the Battle Team. Even if I lose. You said at the beginning of this year that even if we lose in the Quarter Qlashes, the Battle Team will still be responsible for representing the school in tournaments."

$ renpy.music.play("Audio/Pokemon/pikachu_angry3.ogg", channel="altcry", loop=None)

pikachu angry_3 "Pika! Pika, pika... pikachu!"

janine @sad "It's... not really a matter of 'if'..."

redmind @surprisedbrow frownmouth "What? But she always had so much faith in me. Is... Is Dawn {i}really{/i} that strong...?"

janine @talking2mouth "Okay. I need some more time to think about what we should do."

erika @angrybrow sadmouth "Perhaps my suggestion seems more attractive, in light of this new information?"

janine @talking2mouth "...Enough. Pick a training partner. I need to have a talk with Lance."

hide lance with dis
hide dawn with dis

redmind @confusedeyebrows frownmouth "Wait, Lance is...?"

narrator "Looking up, you notice that Lance is standing on the stage lights' crossbar, staring down."

redmind @thinking "It's a wonder that he didn't pipe up when Erika was trying to get me kicked out..."

narrator "Who do you want to train with?"

$ seendawn = False
$ seenerika = False
$ seensilver = False
$ seenhilbert = False

label BattleTeamTraining2:

menu:
    ">Train with Blue":
        show blue closedbrow frownmouth with dis

        $ ValueChange("Blue", 3, 0.5)

        blue @talkingmouth "Fine. Just don't do anything weird."
        
    ">Train with Leaf":
        show leaf with dis

        $ ValueChange("Leaf", 3, 0.5)

        leaf @talkingmouth "Of course."
        leaf @sadbrow talking2mouth "And... sorry about Erika. I take grass classes with her, but I've never seen her {i}like that{/i} before..."

    ">Train with Ethan":
        show ethan with dis

        $ ValueChange("Ethan", 3, 0.5)

        ethan @talkingmouth "Sure thing, man. Since we've got such similar teams, we should be pretty good at helping each other train."
    
    ">Train with Dawn" if (not seendawn):
        $ seendawn = True
        show dawn sadbrow with dis

        $ ValueChange("Dawn", 1, 0.5)

        dawn @sadbrow talkingmouth "I... I'm sorry, but... I don't think we should train together... you know, because of tomorrow. I don't... {size=30}I don't want...{/size}"
        dawn @sadbrow happymouth "Thanks anyway, though..."

        hide dawn with dis

        jump BattleTeamTraining2

    ">Train with Bea":
        show bea with dis

        $ ValueChange("Bea", 3, 0.5)

        bea @closedbrow talking2mouth "Very well. Let us commence."

        show stadium_empty:
            xalign 0.5 yalign 0.5
            ease 2.0 zoom 1.2

        show bea:
            ease 2.0 ypos 1.2 zoom 1.3

        bea @closedbrow talking2mouth "Now..."

        bea angry "Begin!"

        show bea:
            ease 0.3 ypos 2.0 zoom 3.0 alpha 0.0

    ">Train with Erika" if (not seenerika):
        $ seenerika = True
        show erika frownmouth angrybrow with dis

        $ ValueChange("Erika", -1, 0.5)

        pause 2.0

        erika @angrymouth "Surely you can't be serious."

        hide erika with dis

        pause 1.0

        redmind @thinking "I am serious. And don't call me Shirley."

        jump BattleTeamTraining2

    ">Train with Sonia":
        show sonia with dis

        $ ValueChange("Sonia", 3, 0.5)

        sonia @talking2mouth "Right-o. I remember a few techniques Janine taught us at the end of last year. If you wouldn't overly mind skipping ahead a bit...?"

    ">Train with Silver" if (not seensilver):
        $ seensilver = True
        show silver with dis

        $ ValueChange("Silver", 1, 0.5)

        silver @sad "I... Thanks, but I need some time to process."

        hide silver with dis

        jump BattleTeamTraining2

    ">Train with Hilbert" if (not seenhilbert):
        show hilbert with dis

        $ seenhilbert = True

        $ ValueChange("Hilbert", -1, 0.5)

        hilbert @talkingmouth "No."

        hide hilbert with dis

        jump BattleTeamTraining2

scene black with dis

narrator "You train with your partner. Lance taps his foot impatiently while waiting for you to finish."

$ BattleTeamTraining()

scene stadium_empty
show lance 
with dis

pause 1.0

lance @talking2mouth "Do you have a plan to prevail over Dawn tomorrow?" 

red @closedbrow talking2mouth "No."

lance @sad2eyes talking2mouth "So it falls to me. Unsurprising."

red @surprised "Well... I'm surprised. Why-- I mean--"
red @confused "Do you {i}want{/i} me to win?"

lance @shadow talking2mouth "Dawn does not even {i}want{/i} to be a member of the Battle Team." 
lance @sad2eyes talking2mouth "Between someone who insists on self-sabotage and someone who does not even want to compete, I find you, regrettably, being my favored victor."

red @happy "Aw. We're warming up to each other."

lance @shadow talking2mouth "As long as that damnable Pikachu is in your party, my feelings for you will never be warmer than a Baxcalibur's scales."

red @closedbrow talking2mouth "...Great."

lance @talking2mouth "I will talk with you tomorrow morning about possible solutions to this inconvenience."
lance @talking2mouth "For now, I am willing to remind one of your Pokémon of a move."

label movetutor506:

call screen SelectMon

if (_return == 'back'):
    lance @angry "Are you certain that is a good idea?"

    menu:
        "I don't want to teach any of my Pokémon one of their old moves.":
            lance @closedbrow talking2mouth "Fine."

        "On second thought...":
            jump movetutor506

else:
    $ tutormon = _return
    $ tutormonname = pokedexlookup(tutormon.GetId(), DexMacros.Name)

    lance @talking2mouth "You wish me to teach your [tutormonname]... not what I would do, but fine."
    
    $ rememberablemoves = GetRememberableMoves(tutormon)

    if (len(rememberablemoves) == 0):
        lance @talking2mouth "This Pokémon has no moves it can remember."

        jump movetutor506

    else:        
        lance @talking2mouth "What do you want me to re-teach this Pokémon?"

        $ learnmove = renpy.call_screen("rememberablemoves", tutormon)

        if (learnmove == "Back"):
            lance @talking2mouth "You will have to battle Dawn, one of the strongest battlers this Battle Team has ever seen, in approximately fourteen hours."
            lance @sad2eyes talking2mouth "I wouldn't waste these precious moments with indecision."

            jump movetutor506

        else:
            $ tutormon.LearnNewMove([(0, learnmove)])

            if (learnmove not in tutormon.GetMoveNames()):
                jump movetutor506

lance @sadbrow talking2mouth "I have done all I can for now."
lance @talking2mouth "I will be expecting you here, tomorrow, at eight o'clock. If you are to have the slightest chance of victory, then you will attend."

pause 1.0

lance closedbrow talking2mouth "For now, I..."

pause 1.0

lance @shadow sad2eyes talking2mouth "Am going."

hide lance with dis

pause 1.0

redmind @happy "Heh. He didn't say 'take my leave.' We're totally in his head, now."

pause 1.0

show janine with dis

janine @talking2mouth "Everyone, head back to your dorms. Tomorrow is going to be a big day. Everyone focus on winning your own matches. Lance and I will figure out what to do about Dawn and [first_name]'s match."

pause 0.5

janine @closedbrow talking2mouth "[first_name], stay here a moment."

pause 1.0

janine @talking2mouth "...The Team comes first."

red @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

janine @angrybrow talking2mouth "You get what I mean, right? More than my reputation. More than anyone's pride. The reputation of the Team needs to come first."

red @sadbrow talking2mouth "I'm not dropping out."

janine @smirkmouth "...Good. But there's more."
janine @talking2mouth "I need you to explain your powers to everyone."

red @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

janine @talking2mouth "Only someone with your powers can explain it in a way that {i}doesn't{/i} make it sound insane. Or evil."

red @sadbrow talking2mouth "I... I tried."

show janine with dis:
    ease 0.5 ypos 1.2 zoom 1.3

narrator "Janine steps up to you and puts her hand on your shoulder. She speaks, slowly, clearly, and carefully."

janine @talking2mouth "I don't need you to try. I need you to {i}succeed.{/i}"

stop music fadeout 1.5

scene blank2 with Dissolve(2.0)

narrator "You leave the Battle Hall and head back to your new dorm."

$ renpy.music.queue("audio/music/Eterna_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
$ renpy.music.queue("audio/music/Eterna_Loop.ogg", channel='music', loop=True)

scene suitenight 
show blue frownmouth
with splitfade

red @surprised "Blue? {w=0.5}Hi."
red @confused "Uh, what's up?"

blue @talkingmouth "I'm only going to say this once."

pause 1.0

blue @talkingmouth "You can't beat Dawn."

red @playfuleyes angryeyebrows talking2mouth "Oh, geez, thanks."

blue @angrybrow talkingmouth "I'm serious, idiot. You're going to need to convince her to quit. Or... steal her Poké Balls or something. Lock her in the changing room before the match."

red @closedbrow talkingmouth "Yeah, I won't be doing anything like that. [pika_name] and I will figure something out."

show suitenight with vpunch

show blue angry:
    ease 0.5 ypos 1.2 zoom 1.3

blue @talkingmouth "You {i}can't{/i} 'figure something out' with her! She's a dragon! She's a dragon, and one of my classmates is a literal dragon, so I know what I'm talking about!"
blue -angry closedbrow frownmouth @angrymouth "You need a better plan than just throwing your ass into the fire again."

red @closedbrow talking2mouth "She doesn't take Fire-type classes, so I'm pretty sure I'll be fine."

blue @angrybrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
blue @angrybrow talkingmouth "She beat me. She beat me harder than anyone ever has. {i}I{/i} never had a chance. And if I didn't have a chance, you'll lose before you even get into the arena."

pause 1.0

blue @angrybrow talkingmouth "Smell ya later."

hide blue with dis

redmind @thinking "Oh boy. This will be every day from now on, won't it?"

show yellow at rightside with dis

pause 1.0

yellow @sadbrow happymouth "H-hi."

red @happy "Oh, hi! Did you see my battle today?"

yellow @talkingmouth "I did. Your [pika_name] is very cute."

red @happy "Heh. Thanks."

$ renpy.music.play("Audio/Pokemon/pikachu_happy1.ogg", channel="altcry", loop=None)

pikachu happy_2 "Pika!"

yellow @talkingmouth "I hope that my Chuchu finds something to do she likes as much as your [pika_name] likes battling."

red @confusedeyebrows talking2mouth "You like battling? Could've fooled me, tubby."

$ renpy.music.play("Audio/Pokemon/pikachu_sad.ogg", channel="altcry", loop=None)

pikachu bashful_2 "Pi..."

yellow @talkingmouth "Um... while you were all gone at the Battle Team meeting, Professor Oak came here. He went to your old dorm first, actually, but... um..."
yellow @sadbrow talkingmouth "He wants to talk. He seemed pretty serious."

red @sadbrow talking2mouth "Right... I figured he'd want to talk, but I was hoping... ugh."

yellow @talkingmouth "He said to meet him at 11:30 tomorrow morning."

red @surprised "Really? That's just half an hour before I need to go battle Dawn, though. He's cutting it a bit close."

yellow @surprised "Wait... you're battling Dawn?"

red @closedbrow talkingmouth "Apparently."

show yellow sadbrow frownmouth with dis

pause 2.0

hide yellow with dis

red @confused "Well... that's not a good sign."

scene bedroomnight with splitfade

pause 2.0

redmind @surprised "Wow. Blue actually set up all my stuff."

pause 1.0

redmind @playfuleyebrows playfuleyes frownmouth "Wait a minute. That's not all {i}my{/i} stuff."

pause 1.0

narrator "It seems that quite a fair amount of Brendan, Calem, Hilbert, and Ethan's stuff made its way into your room as well..."

redmind @closedbrow frownmouth "Well... I guess they hadn't finished moving out yet. I'll tell Ethan about his stuff in the morning, and if the other guys ever talk with me again, then..."

pause 1.0

redmind @closedbrow frownmouth "No, I shouldn't be bitter. It's my fault for not explaining things clearly, and hiding stuff from them.{w=0.5} ...But I will."

pause 1.0

narrator "You fall into bed, completely exhausted."

pause 1.0

red @sadbrow happymouth "Hey, bud. Mind turning the light switch off for me?"

$ renpy.sound.play("Audio/Pokemon/pikachu_excite2.ogg", channel="altcry", loop=None)

pikachu happy_2 "Pika!"

scene bedroommidnight

red night @talkingmouth "Thanks, buddy."

pause 2.0

narrator "You look at your phone with trepidation. ...But if you want to resume life as it was before, you'll need to proceed as though things are normal."

pause 2.0

narrator "Even though they very much are not."

call texting from _call_texting_12

pause 1.0

$ PlaySound("knock.ogg")

pause 2.0

red night @swimsuithatless happyeyes happyeyebrows happymouth "Don't come in. I'm indecent."

$ hideside = True

pause 1.0

leaf @talking2mouth "So am I, but you don't hear me bragging about it."

pause 1.0

leaf @talking2mouth "On a serious note, though, I... I wanted to tell you something."
leaf @talking2mouth "When you froze during the Battle Team meeting today..."
leaf @talking2mouth "Are you scared of telling people about... Frienergy? Telling people the truth?"

pause 1.0

$ hideside = False 

red @sadeyes sadeyebrows talking2mouth swimsuithatless "...Yes. More than anything else."
red @sadmouth sadeyes sadeyebrows swimsuithatless "I don't want people thinking that they were only ever my friends because of a power."
red @sad2eyes neutraleyebrows talking2mouth swimsuithatless "Of course, I don't want people thinking that I'm mind-controlling them, either..."

$ hideside = True

pause 1.0

leaf @talking2mouth "Instructor Surge said something to me that... um... I think you should hear."

pause 1.0

leaf @talking2mouth "He said that sometimes, there are things that only you can do. No matter who you look to for help, they won't be able to help you."
leaf @talking2mouth "If I could wave a magic wand and make your problems go away, I would. I believe in you. But my belief isn't enough, here."

pause 1.0

leaf @talking2mouth "You can speak, [first_name]. I trust you. But it has to be {i}you{/i} who speaks."

pause 1.0

leaf @talking2mouth "'Aight. That was all. {size=30}G'night.{/size}"

narrator "You drift off to sleep, Leaf's words echoing in your mind... {w=0.5}{i}it has to be you.{/i}"

$ hideside = False

jump day010507