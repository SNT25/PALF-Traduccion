label secondhomeroom010510:

scene blank2

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom behind blank2

show oakbg behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade

oak @talkingmouth "Welcome back to class, ladies and gentlemen." 
oak @talkingmouth "Today's quiz is going to introduce a new concept to you--{i}trained{/i} Pokémon."

redmind uniform @thinking "Hm? {b}Trained{/b} Pokémon?"

oak @talkingmouth "You are probably familiar by now with certain moves that were invented by faculty at Kobukan."
oak @talkingmouth "These moves are powerful, and can be used as a surprise tool to take opponents off-guard, as they're not commonly known outside of Kobukan."
oak @talkingmouth "Of course, this {i}does{/i} imply that your fellow students are likely to have access to these moves, as well."

pause 0.5

oak @talkingmouth "It is not always apparent what moves your classmates may have access to." 
oak @talkingmouth "However, Pokémon with these special moves often show some particular behavior, some visually-identifiable characteristics, that make it clear that they're a specially-trained Pokémon."
oak @talkingmouth "Once you get used to looking for those behavioral patterns, they're as clear to a keen-eyed trainer as the Pokémon's level!"

pause 0.5

oak @talkingmouth "Well... this is something you should keep an eye out for, for future information."
oak @talkingmouth "Incidentally, Professor Cherry is quite excellent at identifying specially-trained Pokémon. For more details, one might want to talk to her."

pause 0.5

oak @talkingmouth "Now, for the upcoming test, you may be relieved to hear that [bluecolor]none of your opponents are able to damage you.{/color} However, it should be noted that [bluecolor]a specially-trained Fighting-type has the move 'Stone Cold Stunner'.{/color}" 
oak @talkingmouth "[bluecolor]If you let the particular Pokémon use this move, you will automatically lose the fight, regardless of what other Pokémon you have on hand! Do what you can to prevent that!{/color} " 
oak @talkingmouth "Take out your pencils... and remember, [bluecolor]this is graded!{/color}"

python:
    trainer1 = Trainer("red", TrainerType.Player, [
        Pokemon("Bidoof", level=10, moves=[GetMove("Headbutt"), GetMove("Simple World"), GetMove("Rollout"), GetMove("Yawn")], ivs=[0, 0, 0, 0, 0, 0], ability="Simple", nature=Natures.Serious),
        Pokemon("Blaziken", level=100, moves=[GetMove("Stone Cold Stunner")], ivs=[0, 0, 0, 0, 0, 0], ability="Speed Boost", nature=Natures.Serious),
        Pokemon("Bagon", level=10, moves=[GetMove("Bite"), GetMove("Legacy"), GetMove("Rage"), GetMove("Ember")], ivs=[0, 0, 0, 0, 0, 0], ability="Sheer Force", nature=Natures.Serious),
        Pokemon("Dewgong", level=25, moves=[GetMove("Fake Out"), GetMove("Aurora Beam"), GetMove("Slow Freeze"), GetMove("Hail")], ivs=[0, 0, 0, 0, 0, 0], ability="Thick Fat", nature=Natures.Serious)
    ], number=3)
    trainer2 = Trainer("oak", TrainerType.Enemy, [
        Pokemon("Nacli", level=20, moves=[GetMove("Splinter Shield")], ability="Purifying Salt", ivs=[0, 0, 0, 0, 0, 0], trained=["Splinter Shield"], nature=Natures.Serious),
        Pokemon("Pawmot", level=20, moves=[GetMove("Stone Cold Stunner")], ability="Volt Absorb", ivs=[0, 0, 0, 0, 0, 0], trained=["Stone Cold Stunner"], nature=Natures.Serious),
        Pokemon("Machop", level=20, moves=[GetMove("Leer")], ability="Steadfast", ivs=[0, 0, 0, 0, 0, 0], nature=Natures.Serious)
    ], number=3)

call Battle([trainer1, trainer2], clearstats=False, gainexp=False, healParty=False, uniforms=[True, False], lockbag=True) from _call_Battle_119
$ battlehistory["Oak8"] = _return

$ renpy.transition(dissolve)
show screen currentdate

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

if (WonBattle("Oak8")):
    redmind uniform @surprised "Dang! I had to swap in a Pokémon {b}and{/b} keep that Pawmot flinch-locked for, like, three turns, {i}and{/i} I had to get used to the new trained Pokémon thing? What happened to just using Tackle on a Cherubi once or twice?"
else:
    redmind uniform @sad "Uh-oh. I think we might be hitting the point where these tests aren't quite as easy as they seemed at the beginning of the year."

    redmind @thinking "Damn, when Advisor Lance said things were about to get harder, he {b}wasn't{/b} kidding."

oak @talkingmouth ".{w=0.5}.{w=0.5}.{w=0.5}"

pause 0.5

oak @talkingmouth "At a glance..."

show homeroom 
show blue uniform angrybrow frownmouth
with vpunch

blue @talkingmouth "Hey! Why don't you take more than a glance this time, Gramps? Why don't you look at {i}everyone's{/i} test, instead of, I dunno, {i}just{/i} [first_name]'s?"

hide oakbg
show oak surprisedbrow frownmouth
show blue:
    ease 0.5 xpos 0.25
with dis

oak @talking2mouth "I'm sorry?"

blue @talkingmouth "I want to know how {i}everyone else did{/i}, too! So I can make sure I'm still on top!"

oak @confusedeyebrows talking2mouth "Er... well, looking through the stack of quizzes more thoroughly... I see some poor logic, and insufficient understanding of elemental immunities."
oak @closedbrow talking2mouth "And it appears to be that many students weren't aware that they were intended to make use of their entire party..."

pause 1.0

oak @confusedeyebrows talking2mouth "Does that satisfy you, Blue?"

blue @talkingmouth "...So, I passed it. 'Cause {i}I{/i} didn't screw up like any of those losers you're talking about."

oak @talkingmouth "Of course you passed it. You always pass them."

if (not WonBattle("IgnoredOak")):
    oak @closedbrow talking2mouth "Well... except for last Monday. But there were extenuating circumstances then. I know how upset you were about--"

    blue @angry "Gramps!"

blue @closedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

blue angrybrow happymouth "You hear that, everyone?! I {i}passed{/i}!" 
blue @happy "That means I'm one step closer to the national championship--and then the {i}world{/i} championship! If you don't pull your shit together, then there's no way you'll make it there, or even graduate! Get serious!"

hide blue
hide oak 
show oakbg
with dis

red @upeyes frownmouth "{size=30}I'm this close. {i}This{/i} close. Do you think we... hm?{/size}"

narrator "You had, out-of-habit, leaned over to whisper to Leaf... before suddenly realizing that she's not here, as she hadn't been, all day."

redmind @thinking "{w=0.5}.{w=0.5}.{w=0.5}.Should I be concerned?"

pause 0.5

$ PlaySound("BellChime.ogg")

pause 2.0

oak @talkingmouth "Oh, it looks like class is over. Hm... well, we'll discuss the quizzes in further detail tomorrow. Be safe, now."

hide oakbg with dis

if ("TalkToBlue" in persondex["Professor Oak"]["Events"]):
    show oak at rightside

    show blue uniform at leftside

    oak @talking2mouth "Blue."

    blue @closedbrow talkingmouth "Yeah, yeah, 'be humble,' 'stop acting out,' I {i}know.{/i}"
    
    oak @talkingmouth closedbrow "Not {i}this{/i} time. Do you have a moment for a couple words?"

    blue @surprised "Huh? Uh... sure...?"

    oak @closedbrow talkingmouth "[first_name], please excuse us."

    red @happy "No probs."

    hide oak
    hide blue
    with dis

    pause 1.0

    narrator "You wait for Blue to finish talking with his grandfather. You give them some privacy, but turn around when you hear some footsteps."

pause 0.5

if (not HasEvent("Blue", "NoBattle")):
    show blue uniform with dis

    blue @talkingmouth "It's time for our battle. Let's go. You need to get the rat from our dorm, right?"

    $ PlaySound("Pokemon/Ball sound.ogg")
    $ PlaySound("Pokemon/pikachu_happy2.ogg")

    pause 1.5

    show blue surprisedbrow frownmouth with dis

    libpikachu @happy "Pika!"

    red @happy "Nope. [pika_name] learned to ride in his Poké Ball."
    red @winkeyes talkingmouth "Hey, maybe he even likes it...?"

    show blue -surprisedbrow -frownmouth with dis

    $ PlaySound("Pokemon/pikachu_angry1.ogg")

    libpikachu @angrybrow talkingmouth "Pika."

    red @sweat talking2mouth closedbrow "Guess we're not there yet. Maybe in a bit."

    blue @talkingmouth "Great. If you don't need to go to the dorm, let's go to the Battle Hall right now."

    red @confusedeyebrows talkingmouth "You don't want to change into something more flexible?"

    blue @closedbrow talkingmouth "Heh. I don't need to bend over backwards to beat you."

    red @closedbrow talkingmouth "Alright. Let's go, then."

    call clearscreens from _call_clearscreens_133
    scene blank2 with splitfade

    pause 0.5

    scene stadium_empty
    show screen currentdate
    show blue uniform
    show yellow uniformhat at rightside
    show ethan uniform at leftside
    with splitfade

    yellow @talkingmouth "Good luck, you guys!"

    ethan @happy "Cheering them both on? Devious, Yellow! You're playing both sides, huh?"

    yellow @sadbrow talkingmouth "N-no, I just want everyone to have fun..."

    red uniform @happy "Thanks for watching, you guys."

    ethan @talkingmouth "It's nothing."
    ethan @talkingmouth "I'm going to head up to the bleachers, though. Don't want to get in your way."

    blue @talkingmouth "Hmph. Keep your eyes on me, you two. {i}I'm{/i} going to win."

    hide ethan
    hide yellow 
    with dis

    pause 1.0

    blue @closedbrow talkingmouth "Well... let's go."

    if (HasEvent("Blue", "SingleBattle")):
        blue @talkingmouth "You're {i}just{/i} using your Pikachu, right?"

        red uniform @sweat talkingmouth "I said I would, man. And I want you to hold up your end of the bargain and not be an ass if you beat me."

        blue @closedbrow talkingmouth "...I said I would."

        redmind @upeyes frownmouth "Oh, well, that seals it, then. Nothing to worry about."

    else:
        blue @talkingmouth "Like I said before. Use your Pikachu in this battle."

        pause 0.5

        blue @sweat closedbrow talkingmouth "Uh... {size=30}Please.{/size}"

        red @confusedeyebrows talking2mouth "{w=0.5}.{w=0.5}.{w=0.5}.Like {i}I{/i} said before, if I get around to it. I'm not going to go out of my way."

        blue @angrybrow frownmouth "Yeah, I {i}know{/i}!"

        pause 1.0

    blue @angrybrow talkingmouth "Let's do this."

    python:
        if (HasEvent("Blue", "SingleBattle")):
            trainer1 = Trainer("red", TrainerType.Player, [pikachuobj])
        else:
            trainer1 = MakeRed()
        
        trainer2 = Trainer("blue", TrainerType.Enemy, GetTrainerTeam("Blue"))

    call Battle([trainer1, trainer2], uniforms=[True, True]) from _call_Battle_120
    $ battlehistory["Blue5"] = _return

    $ HealParty()

    show screen songsplash("Pallet Town", "Zame")
    queue music "audio/music/palletpiano.ogg"

    show blue uniform angrybrow frownmouth 
    show screen currentdate
    with dis

    pause 1.0

    red @playfuleyes unamusedeyebrows talking2mouth "What?"

    if (not WonBattle("Blue5")):
        red @talkingmouth "You {i}won.{/i} You can't possibly be upset about that."

        if (HasEvent("Blue", "SingleBattle")):
            blue @talkingmouth "This doesn't count. You were only using one Pokémon."

            red @closedbrow talking2mouth "You {i}asked{/i} me to use only one Pokémon."

            blue @angry "I know!"

            pause 0.5

            blue @closedbrow talking2mouth "I know."

    else:
        if (HasEvent("Blue", "SingleBattle")):
            red @talkingmouth "You asked me to use [pika_name], and I did. And I beat your whole team with him. You literally {i}asked{/i} for this."
            red @talking2mouth "You can't possibly be upset by this."

        else:
            red @talkingmouth "I won, in a fair, even, battle. My whole team against yours. I didn't have any friends backing me up. I'm only using my own Pokémon, you're only {i}kinda{/i} overleveled."
            red @closedbrow talking2mouth "This is exactly what you wanted. You can't possibly be upset by this."

    blue -angrybrow @talkingmouth "...I'm not. I'm just thinking."

    pause 0.5

    if (WonBattle("Blue5")):
        if (HasEvent("Blue", "SingleBattle")):
            $ ValueChange("Blue", 5, 0.5)
        else:
            $ ValueChange("Blue", 3, 0.5)

    blue @angrybrow frownmouth "I need one. I need a [pika_name]."

    red @talkingmouth "I thought you said you didn't need a new special Pokémon? Because your team's already the best?"

    blue @closedbrow talkingmouth "I've still got an open slot on my team. Anyway, who says my special Pokémon has to be {i}new{/i}? [pika_name] was a completely normal Pikachu for years before {i}this{/i} nonsense."

    red @closedbrow talking2mouth "Fair enough. Maybe if we find any more meteor shards around, you can chuck one into your Pidgeotto's gizzard."

    blue @closedbrow happymouth "Heh. That's not exactly what I'm thinking, but you're on the right track."

    pause 0.5

    if ("TalkToBlue" in persondex["Professor Oak"]["Events"]):
        blue @closedbrow talkingmouth "Oh. Right. Gramps said some stuff to me after class. I'm pretty sure you put him up to it."

        red @talkingmouth "Earlier today, I {i}suggested{/i} that he talk to you."

        blue @talkingmouth "{w=0.5}.{w=0.5}.{w=0.5}.You know I don't want you to fix this. If he's going to sort himself out, he needs to sort {i}himself{/i} out."

        pause 1.0

        $ ValueChange("Blue", 3, 0.5)

        blue @closedbrow talkingmouth "But... thanks."

        red @surprisedbrow talking2mouth "Oh. Uh... you're welcome."
else:
    show ethan uniform  at leftside with dis

    red @talkingmouth "Hey, man."

    ethan @talkingmouth "Hey, bro. Got any plans?"

    red @talkingmouth "Nothing in particular. I think I was going to study... or maybe hang out with someone..."

    ethan @talkingmouth "Got a couple moments to help me look for Leaf, then?"

    red @surprised "Oh, you noticed she was gone, too?"

    ethan @talkingmouth "Yeah, I didn't even hear her Giga Drill Break-level snores this morning."
    ethan @sad2eyes sadeyebrows talking2mouth "I'm low-key a bit concerned, after all the stuff that's happened over the past few days. I'm thinking the water might have finally gotten her."

    red @closedeyes talkingmouth "Bad joke, man. But where've you checked?"

    ethan @talkingmouth "Oh, nowhere. Figured you'd know where to look better than me."

    if (GetRelationshipRank("Leaf") > 0):
        ethan @talkingmouth "After all, you're her 'bestie,' aren't you?"

        if (HasEvent("Leaf", "AcceptedConfession")):
            red @confusedeyebrows talking2mouth "Either that or her 'date.' It's honestly a bit confusing."
        else:
            red @confusedeyebrows talking2mouth "Either that or her 'pursuit.' It's honestly a bit confusing."

        red @talkingmouth "Anyway, the first place to check would probably be the Battle Hall."

    else:
        red @talkingmouth "I getcha. Anyway, the first place to check would probably be the Battle Hall."

    ethan @talking2mouth "Right. She {i}is{/i} a battle maniac."

    red @talkingmouth "Shall we ask Blue if... huh?"

    pause 0.5

    ethan @talkingmouth "Looks like he already left."
    ethan @lightblush sad2eyes talking2mouth "Shame. I would've like to watch him go."

    red @angrybrow talkingmouth "Dude!"

    ethan @closedbrow talkingmouth "Hey, I don't razz you for {i}your{/i} taste."

    red @confusedeyebrows talking2mouth "You could be forgiven for not knowing his personality that first day. {i}Now{/i} you know what you're signing yourself up for."

    ethan @talking2mouth winkeyes "What can I say? I like a challenge."

    pause 1.0

    ethan @sad2eyes talking2mouth "Wait, no I don't. Why'd I say that? I hate challenges."

    red @upeyes talking2mouth "Whatever, man. Come on, let's go to the Battle Hall."

    call clearscreens from _call_clearscreens_134
    scene blank2 with splitfade

    pause 0.5

    scene stadium_empty
    show screen currentdate
    show yellow uniformhat at rightside
    show ethan uniform at leftside
    with splitfade

    ethan @talkingmouth "Hey, Yell'."

    yellow @closedbrow talking2mouth "{size=30}Yell'?{/size}"

    ethan @talkingmouth "What're you doing here? I thought you didn't like battles?"

    yellow @talkingmouth "Not so much, no. But... well..."

    narrator "You suddenly hear the sounds of a battle going on in the pit."

    red uniform @talkingmouth "Huh. I guess since I turned him down for a battle, he found someone else."

    yellow @sadeyes talking2mouth "Actually... a lot of people have been asking Blue to battle ever since Wednesday... they're pretty mad at him for holding up the Quarter Qlashes."

    pause 0.5

    red @unamusedeyebrows playfuleyes talkingmouth "Yeah, okay, but you can't pretend he doesn't {i}love{/i} that."

    yellow @sadbrow happymouth "He {i}does.{/i}"

    hide ethan
    hide yellow
    with dis

    narrator "You watch Blue's battle for a while. While watching him battle, you get the oddest feeling of...{w=0.5} jealousy?"

    redmind @thinking "Come to think of it, I'm not sure I can think of any other time I've turned down a battle... well, that's that, I guess."

    pause 1.0

    show blue with dis

show yellow uniformhat at rightside 
show ethan uniform at leftside
with dis

pause 1.0

show yellow surprisedbrow
show ethan surprisedbrow
with dis

blue @talkingmouth "You two."

show yellow -surprisedbrow
show ethan -surprisedbrow
with dis

ethan @talkingmouth "That's my name."

blue @talkingmouth "Did you notice anything I could improve on in that past fight?"

if (WonBattle("Blue5")):
    ethan @confusedeyebrows talkingmouth "Well, you didn't win. I'd recommend fixing that part."

    blue @angrybrow talkingmouth "Yeah, obviously! I'm asking for {i}specifics!{/i}"

    ethan @closedbrow talking2mouth "Blue, get off the roof. You asked for my counsel; I gave you my thoughts." 
    ethan @talking2mouth "If you want anyone who can actually help you, there's Advisor Lance. Or, I dunno, Loaf."
    
    ethan @closedbrow talking2mouth "Actually..."

else:
    ethan @talkingmouth "I mean, you won. That means you were doing everything right, right?"

    blue @closedbrow talkingmouth "Obviously not. There are bad ways to win."

    yellow @happy "And good ways to lose, right?"

    blue @closedbrow talkingmouth "Hah! No. Only losers would say that."

    pause 1.0

    yellow @angrybrow talkingmouth "You mean like when Dawn--"

    blue @angry "Could you {i}stop{/i} bringing that up?!"

ethan @confusedeyebrows talkingmouth "Since we're all here, has {i}anyone{/i} seen Loaf today?"

pause 1.5

ethan @confusedeyebrows talking2mouth "Nothing, huh? Maybe we {i}should{/i} be concerned, then."

menu:
    "Should we go looking for her?":
        blue @closedbrow talkingmouth "You can, if you want. I'm done running after people for {i}at least{/i} a month."
        blue @closedbrow talkingmouth "Besides, me and Yellow have got plans tonight."

        ethan @talkingmouth "'Yellow and I.'"

        red @surprised "What, you've got plans, too?"

    "She's probably looking for Tia.":
        yellow @surprised "Oh! Yes, that makes sense. I haven't seen Tia in any of my medical classes, either."

        red @closedbrow talking2mouth "Wait, Tia's in the medical program, too?"

        yellow @talkingmouth "Yep."

        ethan @closedbrow talking2mouth "Well, if Whimsicott's in the nurse program, and Tea just copied her, I guess that makes sense."

        yellow @closedbrow talking2mouth "Whimsicott?"

        show ethan unamusedeyebrows sad2eyes frownmouth with dis

        blue @talkingmouth "He means 'Whitney.' He does this annoying thing where he pretends to forget people's names. Just ignore him."

    "Good riddance.":
        show yellow surprisedbrow frownmouth
        show blue surprisedbrow frownmouth
        show ethan surprisedbrow frownmouth
        with dis

        pause 1.0

        show blue closedbrow
        show ethan unamusedeyebrows
        show yellow sadbrow
        with dis

        ethan @closedbrow talking2mouth "Not the time for jokes, dude."

        redmind @thinking "Who's joking?"

        show blue -closedbrow -frownmouth
        show ethan -unamusedeyebrows -frownmouth
        show yellow -sadbrow -frownmouth
        with dis

pause 1.0

red @talkingmouth "Alright. I'd love to stick around, but Sam told me to drop by his office before the day is up, so I gotta go."

blue @closedbrow talkingmouth "Great. What's he going to tell you {i}this{/i} time? You can actually walk on water? You put your pants on two legs at a time?"

red @talkingmouth "I'm not sure. I'll let you guys know when I get back to the dorm, though."

pause 0.5

yellow @happymouth "Blue? Now's a good time, if..."

pause 0.5

blue @closedbrow talkingmouth "Don't stay out too late. I mean... come back to the dorm after you're done, alright?"

red @talkingmouth "...I wasn't planning on staying out late."

hide blue with dis

yellow @happy "See you later!"

hide yellow with dis

ethan @closedbrow talking2mouth "Wonder what that was about?"

hide ethan with dis

call clearscreens from _call_clearscreens_135
scene blank2 with splitfade

show screen songsplash("Sonia's Theme", "Syntthetix")
stop music fadeout 1.5
queue music "audio/music/sonia_start.ogg" noloop 
queue music "audio/music/sonia_loop.ogg"

scene research 
show screen currentdate
show nate happy:
    xpos 0.25 ypos 1.0
    parallel:
        ease 3.0 xpos 0.25
        ease 3.0 xpos 0.22
        ease 3.0 xpos 0.25
        ease 3.0 xpos 0.28
        repeat
    parallel:
        ease 2.0 ypos 1.05
        ease 2.0 ypos 1.0
        ease 2.0 ypos 0.95
        ease 2.0 ypos 1.0
        repeat
show sonia happy:
    xpos 0.5 ypos 1.0 xzoom 1.0
    parallel:
        ease 1.0 xpos 0.25
        ease 1.0 xpos 0.5
        ease 1.0 xpos 0.75
        ease 1.0 xpos 0.5
        repeat
    parallel:
        ease 0.5 ypos 1.05
        ease 0.5 ypos 1.0
        ease 0.5 ypos 0.95
        ease 0.5 ypos 1.0
        repeat
    parallel:
        pause 1.7
        ease 0.3 xzoom -1
        pause 1.7
        ease 0.3 xzoom 1
        repeat
with splitfade

pause 1.0

narrator "As you walk into... wait, what's happening here?"

show nate surprisedbrow frownmouth:
    ease 0.5 xpos 0.25 ypos 1.0 xzoom 1
show sonia surprisedbrow frownmouth with vpunch:
    ease 0.5 xpos 0.5 ypos 1.0 xzoom 1

sonia @talking2mouth "[first_name]?"

show sonia happy with dis:
    ease 0.5 xpos 0.5 ypos 1.2 zoom 1.3

sonia @talking2mouth "[first_name]!"

show nate:
    ease 0.5 xpos -0.5

show research behind nate:
    subpixel True
    xanchor 0.0 xpos 0.0
    block:
        linear 1.5 xpos -1.0
        xpos 1.0
        linear 1.5 xpos 0.0
        repeat

show research as research2 behind nate:
    subpixel True
    xanchor 0.0 xpos 1.0 xzoom -1
    block:
        linear 3.0 xpos -1.0
        xpos 1.0
        repeat

show sonia:
    xzoom 1 ypos 1.2 zoom 1.3
    block:
        linear 1.5 xzoom -1
        linear 1.5 xzoom 1
        repeat

narrator "Sonia spins you around in a tight hug. Any thoughts or preconceptions you'd had about linking her physical strength to her lack of ego are instantly dispelled as you become {i}very{/i} unable to breathe."

pause 0.5

narrator "{size=30}(It's not the worst thing in the world, though.){/size}"

menu: 
    ">Accept your death":
        $ AddEvent("Sonia", "SoniaDeath")
        show blank2:
            alpha 0.0
            ease 6.0 alpha 1.0

        narrator "As your last breath leaves your body, you get a sinking feeling in your stomach that this was not how your story was supposed to end."

        pause 2.0

        narrator "Yet end it does."

        scene blank2
        call clearscreens from _call_clearscreens_136

        show gameover at truecenter

        pause 10

        narrator "Honestly, I'd do the same. You can have this one, I'll bring you back."

    ">Rage against the dying of the light":
        narrator "Through frantic gasps and application of elbows, you manage to extricate yourself. Sonia seems unperturbed."

scene research: 
    ease 0.5 xpos 0
hide research2
show screen currentdate
show nate:
    ease 0.5 xpos 0.25
show sonia:
    xpos 0.5 ypos 1.2 zoom 1.3
    ease 0.5 xpos 0.75 ypos 1.0 zoom 1.0 xzoom 1
with dis

red uniform @surprised "Wh-wh-what is {i}happening{/i} here?!"

$ firstinitial = first_name[0]
nate @happy "Seems like the sun's come out for once, [firstinitial]!"

sonia @happy "[first_name], this is fantastic! It's absolutely brilliant!"

red @happy "Great! What is it?"

sonia @talking2mouth "I've been looking at these Foreverals {i}all{/i} evening, and all morning, too, and I've finally figured them out!"

red @talkingmouth "Oh, you mean how they work?"

if ("ForeveralsFiguredOut" in persondex["Professor Oak"]["Events"]):
    red @happy "Yeah, I figured them out, too. It's really easy to figure out what they do when you're using them in battle, actually."

    sonia @surprised "Oh!"

    pause 0.5

    sonia @happy "Well, that's mildly disheartening, but, no, that's not what I mean!"

else:
    sonia @happy "Well, yes, that, but also-- {i}also{/i}-- something even better!"

pause 0.5

red @confusedeyebrows talking2mouth "Go ahead?"

sonia @angrybrow happymouth "These foreverals aren't minerals at all! They're biological material! Do you know what this means?!"

menu:
    "Well, you're an Astrobiologist, so... you can study them?":
        $ ValueChange("Sonia", 1, 0.75)
        sonia @happy "You remembered!"

    "Absolutely nothing?":
        sonia @sad "{i}Must{/i} you rain on my parade?"

        red @sadbrow talking2mouth "Sorry. Guess I'm forgetting something."

        sonia @talking2mouth "I'm an astrobiologist, remember? Or, well that's my field of study... anyway, this is a massive opportunity!"

    "[bluecolor][[Sonia Rank 1]{/color} Your karma's come around." if (GetRelationshipRank("Sonia") > 0):
        sonia @blush surprised "You remembered that conversation?"

        red @happy "Of course."
        
        show sonia blush closedbrow with dis

        $ ValueChange("Sonia", 3, 0.75)

        sonia @talking2mouth "Then... well, yes."

        show sonia -blush -closedbrow with dis

sonia @happy "A new field of astrobiology has quite literally fallen at my feet, right as I was tearing my hair out about how I could possibly pay for school! This is brilliant!"

red @talkingmouth "Well, that's great. I'm glad for you. What does it mean for [pika_name], though?"

sonia @talking2mouth "I couldn't rightly say. Not just yet. I'm detecting three distinct genomes from the Foreverals. It's difficult for me to isolate what is coming from your Liberation Form Pikachu, and what's coming from the meteor."

red @talkingmouth "Well, you let me know if I can help, at all."

sonia @talking2mouth "You can, actually. Or, rather, your Pikachu can."

$ renpy.music.play("Audio/Pokemon/pikachu_question.ogg", channel="altcry", loop=None)
libpikachu @surprisedeyes frownmouth "Pika?"

sonia @happy "If you could have your Pikachu lick this tongue depressor..."

red @talkingmouth "I don't see why not. Go ahead, [pika_name].{w=0.5} Lick the stick.{w=0.5} Do it quick."

$ renpy.music.play("Audio/Pokemon/pikachu_sad.ogg", channel="altcry", loop=None)
libpikachu @sadeyes talkingmouth "Pikaaaa..."

narrator "[pika_name] licks the stick, but doesn't seem to enjoy the taste."

sonia @talking2mouth "Oh, yes, it's coated in a sort of bitter-tasting adhesive that maintains and traps the moisture. I probably should've mentioned. Sorry about that."

$ renpy.music.play("Audio/Pokemon/pikachu_angry1.ogg", channel="altcry", loop=None)
libpikachu @dizzyeyes surprisedmouth "Pika."

sonia @talking2mouth "There is {i}one{/i} thing I should mention, though."

red @closedbrow talking2mouth "Hm?"

sonia @talking2mouth "Overuse of the Foreverals' power could prove to be very dangerous for... [pika_name], was it?"

red @talkingmouth "That's right."

pause 0.5

red @surprised "Wait, what do you mean, {i}dangerous?!{/i}"

sonia @talking2mouth "Ah, well, are you at all familiar with biology?"

pause 0.5

show sonia surprisedbrow frownmouth with dis

red @unamusedeyebrows playfuleyes talkingmouth "...No. No, I'm not."

sonia @talking2mouth "Oh."

sonia -surprisedbrow -frownmouth -surprised @talking2mouth "Well, the basis of all biology, astro- or otherwise, is that all life attempts to perpetuate itself, and remove intruders."

red @talkingmouth "Intruders?"

sonia @talking2mouth "'Invaders' might be another word for it. Liberation Form Pikachu wasn't built to handle the generation of Foreverals, nor their power." 
sonia @sadbrow talking2mouth "Using the power of too many Foreverals at once could set off a false positive in [pika_name]'s immune system."
sonia @talking2mouth "He could develop a fever, or strain his muscles too far, or even enter a maddened, frenzied, state."

red @closedbrow sweat talking2mouth "Man, I knew it couldn't be this easy."

red @closedbrow talking2mouth "Alright, so what are the rules? I'm guessing I can't just slap on any move I want anymore."

sonia @sadbrow happymouth "I'm afraid not. You'll want to be careful about utilizing the form-changing Foreverals, as well."

red @sad2eyes talking2mouth "Well... at least I got three days out of it."

sonia @talking2mouth "We're on the forefront of science, here, so there aren't any official terms to describe what I'm trying to convey... but let's say that your Pikachu only has a certain level of power it can safely store in its body."
sonia @closedbrow talkingmouth "We'll call this the 'Liberation Limit.'"

red @talkingmouth "With you so far."
    
sonia @talking2mouth "Now, every move it knows has a certain level of power, depending on its complexity, that contributes to that limit. Also, every Foreveral you equip him with, or every form he changes into, also contributes to that limit."
sonia @happy "So what you need to do is make sure his 'Liberation Level' is under the 'Liberation Limit.'"

red @talkingmouth "Okay. Do you know how I could keep track of those numbers?"

sonia @talking2mouth "Yes, I've written it all up in this notepad. I'm still figuring some things out, and these are approximate values, but it {i}should{/i} work."

python:
    usingliberationlimit = True
    RemoveForeverals(pikachuobj)
    pikachuobj.Moves = [GetMove("Quick Attack"), GetMove("Growl"), GetMove("Nuzzle"), GetMove("Electro Ball")]
    pikachuobj.ChangeForme(25.2, revert=True)
    HealParty()

narrator "[bluecolor]You gained access to the Liberation Limit ledger!{/color} More options have opened up to you in the Foreveral Menu. Check [pika_name]'s stats, or the Foreveral Menu, any time, for a current summary of your liberation limit!"

pause 0.5 

narrator "([pika_name]'s movepool has also been reset. [bluecolor]You may want to adjust that.{/color})"

pause 1.0

red @closedbrow talking2mouth "...Is there a way to increase this limit?"

sonia @talking2mouth "Ought to be. Just like a body builds up an immunity when exposed to a vaccine, [pika_name] ought to be able to build up an immunity to the power of the Foreverals with practice and time."

narrator "[bluecolor]Your Liberation Limit will steadily increase every day.{/color} Battling with trainers can also increase your Liberation Limit--losing battles will increase your Liberation Limit faster."

red @sweat closedbrow talking2mouth "Well, it's disappointing, but I guess it's better I know now than just keep pumping these gems into him, and cause him to explode a few weeks down the line."

$ renpy.music.play("Audio/Pokemon/pikachu_fun1.ogg", channel="altcry", loop=None)
libpikachu @lightblush happy "Pika!"

pause 1.0

nate @talkingmouth "...Mind if I step in here?"

red frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

redmind "He knew about Frienergy before anyone else... did he have something to do with Cheren's actions? They roomed together, after all..."

menu:
    "Go ahead.":
        $ AddEvent("Nate", "AllowedApologize")
        $ ValueChange("Nate", 1, 0.25)
        nate @happy "Ah, thanks."

    "Is there something you want to say to me?":
        $ AddEvent("Nate", "NeutralApologize")
        nate @talking2mouth "Yeah." 

    "I've nothing to say to you.":
        $ AddEvent("Nate", "DenyApologize")
        show nate sad
        show sonia sad
        with dis

        $ ValueChange("Nate", -1, 0.25)

        pause 1.0

        nate @closedbrow talking2mouth "I can't blame you for that."

        pause 0.5

        nate sadbrow frownmouth @talking2mouth "But my mission right now is to apologize. And {i}nothing{/i} moves me from my mission."

nate sadbrow frownmouth @talking2mouth "S, mind giving us a bit of room to breathe, here?"

show sonia -sad:
    xpos 0.75 xzoom 1
    ease 0.3 xzoom -1
    ease 1.0 xpos 0.9
    pause 0.4
    ease 0.3 xzoom 1
    pause 0.5
    ease 0.3 xzoom -1
    ease 1.0 xpos 1.2

sonia @talking2mouth "Right. I'll just be... over here, then..."

pause 4.0

show nate:
    ease 0.5 xpos 0.5

nate @talkingmouth "I gave those two purple kids on Saturday their information. I'm sorry about that, [firstinitial]. I don't have any excuse or defense. I just want you to know I'm sorry."

label prepology:

menu:
    "Apology accepted.":
        $ AddEvent("Nate", "AcceptedApology")
        $ ValueChange("Nate", 1, 0.5)

        nate @sadbrow talkingmouth "Thanks. I know I don't deserve that, but thanks anyway."
        
    "Why'd you do it?" if not HasEvent("Nate", "WhydYouDoIt"):
        $ AddEvent("Nate", "WhydYouDoIt")
        nate @closedbrow talking2mouth "Ugh. I'm investigating the forest. The guy said he and his 'sister' would help. It was a devil's deal, but now I just wish I'd told them to go to hell."

        jump prepology

    "I'm going to need some time to think about this.":
        $ AddEvent("Nate", "RejectedApology")
        nate @talking2mouth "Take all the time you need. You don't even need to forgive me. Just wanted to let you know."

pause 0.5

show nate:
    ease 0.5 xpos 0.25

nate -sadbrow -frownmouth @closedbrow talking2mouth "S, I know you're listening."

pause 1.0

redmind @confusedeyebrows frownmouth "Nothing?"

show sonia blush sadbrow:
    xpos 1.2 xzoom 1
    ease 0.5 xpos 0.75

sonia @talking2mouth "Right. Sorry about that."
sonia -blush -sadbrow @talking2mouth "I was just thinking... if you want to {i}really{/i} apologize, maybe you could do something for him."

nate @surprisedbrow talking2mouth "Eh? Don't think I like the sound of that. Can I at least keep my socks on?"

sonia @surprised "What? No, get your mind out of the gutter."

nate @happy "Easier said than done. My mind has a long-term housing contract with the gutter. Cancelling the mortgage now would come with massive fees, and not even {i}my{/i} mouth can handle a check that big."

sonia @talking2mouth "Oh, you're ridiculous. [first_name], maybe there's something you can think of?"

$ nate_name = first_name[0]

label nateoffer:

menu:
    "I'd like to change my nickname.":
        nate @closedbrow talking2mouth "{size=30}I'm never going to hear the end of this. Thanks a lot, LG.{/size}"

        nate @talking2mouth "Fine. You know the rules. Three characters or less."

        label natename:

        $ nate_name = renpy.input("Please type the name you'd like Nate to refer to you by, then press ENTER to confirm.", length=3, exclude="{}[[]%<>")

        if (nate_name.lower() == "sex"):
            show nate:
                ease 0.5 ypos 1.28 zoom 1.3 xpos 0.5

            pause 0.5

            show nate nude with dis

            show sonia sadbrow fullblush with dis

            nate @talkingmouth "Yeah, okay."

            red @fullblush surprised "N-N-Nate?! Put some clothes on!"

            nate @angrybrow talking2mouth "Yeah, that's what I thought. You want to go to {i}war,{/i} buddy? I'm a thousand times more shameless than you."

            red @closedbrow fullblush talkingmouth "P-put your clothes back on!"

            nate @closedbrow talking2mouth "I don't need this body-shaming. I'm proud of how I look."

            show nate -nude with dis

            pause 1.0

            show nate:
                ease 0.5 ypos 1.0 zoom 1.0 xpos 0.25
            show sonia -sadbrow -fullblush 
            with dis

            nate @talkingmouth "Now, do you want to try again, or do you want to be smart with me?"

            menu:
                "I'm going to be smart.":
                    nate @closedbrow talking2mouth "{i}Sigh.{/i}"

                    jump nateoffer

                "Let's try that again...":
                    jump natename

        else:
            nate @talkingmouth "Got it. [nate_name] it is."

            jump nateoffer

    "I want to help you with whatever you needed help with." if HasEvent("Nate", "WhydYouDoIt"):
        $ AddEvent("Nate", "OfferedHelp")
        nate @surprised "Huh?"

        red @talkingmouth "I don't know what you asked for help from those purple students for. But they're gone, and I'm here. I need help, and you do, too. We could work together."

        pause 0.5

        nate @closedbrow talking2mouth "Hm... yeah, actually, maybe that {i}would{/i} work. Hilbert is already... hm."

        $ ValueChange("Nate", 3, 0.25)

        nate @talkingmouth "I might take you up on that."

    "Can you find something out for me?" if not HasEvent("Nate", "CanYouFindOut"):
        $ AddEvent("Nate", "CanYouFindOut")
        nate @closedbrow talking2mouth "Depends on what you're looking for. Want to know who's got a crush? I can crush that. Looking for the launch codes? That'll take a bit longer."

        menu:
            "Where is Sabrina?":
                $ AddEvent("Nate", "FindOUtSabrina")
                show nate angrybrow frownmouth with dis

                pause 0.5

                nate @talking2mouth "She's in the forest. I can't tell you how I know this, though. And I should probably tell you that you definitely shouldn't go looking for her. Leave that to the professionals."
                
                red @closedbrow talking2mouth "I'll keep that in mind."

            "Where is Leaf?":
                $ AddEvent("Nate", "FindOutLeaf")
                show nate surprisedbrow frownmouth with dis

                pause 0.5

                nate -surprisedbrow -frownmouth -surprised @happy "Oh, that's an easy one. She's back at your dorm!"

                red @closedbrow talking2mouth "Oh."

            "Where is Tia?": 
                $ AddEvent("Nate", "FindOutTia")
                show nate angrybrow frownmouth with dis

                pause 0.5

                nate @talking2mouth "She's in the forest. I can't tell you how I know this, though. And I should probably tell you that you definitely shouldn't go looking for her. Leave that to the professionals."
                
                red @closedbrow talking2mouth "I'll keep that in mind."
                
            "Where is Instructor Will?":
                $ AddEvent("Nate", "FindOutWill")
                show nate angrybrow frownmouth with dis

                pause 0.5

                nate @talking2mouth "He's in the forest. I can't tell you how I know this, though. And I should probably tell you that you definitely shouldn't go looking for him. Leave that to the professionals."
                
                red @closedbrow talking2mouth "I'll keep that in mind."

        show nate -angrybrow -frownmouth with dis

        jump nateoffer

    "Nothing, thanks.":
        pass

nate @talkingmouth "Alright. Mind if I do one more thing? S, maybe you could help out, too."

red @confusedeyebrows frownmouth "Hm?"

nate @talkingmouth "I'm trying to figure out how these 'Foreverals' work. A teacher's got a bit of an interest in it."
nate @talking2mouth "Mind if I ask a couple questions? Shouldn't take more than five minutes. Seems like you two have the most understanding of anyone at this school. Think of it kinda like... a quiz."

sonia @happy "Oh, joy, I {i}love{/i} quizzes!"

if (not WonBattle("Oak8")):
    redmind @thinking "Man, I already failed one quiz today..."
else:
    redmind @thinking "Man, I already took one quiz today..."

menu:
    "I don't have any interest in this.":
        $ AddEvent("Nate", "RejectQuiz")
        $ ValueChange("Nate", -1, 0.25, False)
        $ ValueChange("Sonia", -1, 0.75)
        nate @closedbrow talking2mouth "Well, that's not very interesting. Fine, I'll just ask S."

    "Sure.":
        $ AddEvent("Nate", "DoQuiz")
        $ ValueChange("Nate", 1, 0.25, False)
        $ ValueChange("Sonia", 1, 0.75)
        nate @talkingmouth "Cool."

nate @talkingmouth "Question Numero Uno. How many types of Foreverals are there?"

if (HasEvent("Nate", "DoQuiz")):
    menu:
        "One.":
            sonia @talking2mouth "That's not {i}quite{/i} right. Every Foreveral is associated with a specific type of Pokémon, but they can be generally broken down into five categories."

        "Three.":
            sonia @talking2mouth "That's not {i}quite{/i} right. Every Foreveral is associated with a specific type of Pokémon, but they can be generally broken down into five categories."

        "Five.":
            sonia @talking2mouth "Yes, that's right."

            $ ValueChange("Nate", 1, 0.75, changemood=False)

        "As many as there are Pokémon.":
            nate @talkingmouth "Huh, so each Pokémon has a unique Foreveral?"

            sonia @talking2mouth "That's not {i}quite{/i} right. It's true that every Foreveral is associated with a specific type of Pokémon, but they can be broken down into five categories."
            sonia @closedbrow talkingmouth "Come to think of it, it seems quite likely there could be {i}more{/i} Foreverals than species of Pokémon, in the event a single species has multiple associated Foreverals."

else:
    sonia @talking2mouth "Five."

nate @talkingmouth "Gotcha. Here's part two--What are the five categories?"

if (HasEvent("Nate", "DoQuiz")):
    menu:
        "Foreverals, Everals, Gigaverals, Megaverals, and Diverals.":
            sonia @talking2mouth "Right you are."

            $ ValueChange("Sonia", 1, 0.25, changemood=False)

        "Eternals, Longals, Largeals, Ultimals, and Changeals.":
            sonia @talking2mouth "If I could make a small correction... The categories are actually Foreverals, Everals, Gigaverals, Megaverals, and Diverals."

        "Emeras, Eviolites, Wishing Stars, Mega Stones, and Homeland Soil.":
            sonia @talking2mouth "The corresponding Foreverals {i}do{/i} vaguely resemble the effects of these items, but the categories are actually Foreverals, Everals, Gigaverals, Megaverals, and Diverals."

        "You can't honestly expect me to remember.":
            sonia @closedbrow talkingmouth "Didn't advisor Lance say you memorized every single Pokémon at some point?"

            red @playfuleyes unamusedeyebrows talking2mouth "I can memorize Pokémon, not {i}rocks{/i}."

            sonia @sadbrow talking2mouth "{size=30}Technically it's organic material, but...{/size} Anyway, the categories are Foreverals, Everals, Gigaverals, Megaverals, and Diverals."

else:
    sonia @talking2mouth "The categories are Foreverals, Everals, Gigaverals, Megaverals, and Diverals."

nate @talkingmouth "Understood. Can you handle {i}parte tres{/i}, though? What do Megaverals do?"

if (HasEvent("Nate", "DoQuiz")):
    menu:
        "They allow a Pokémon to Gigantamax.":
            sonia @talking2mouth "Not quite, I'm afraid. They actually generate... well, 'Mega Stones' at the start of each turn."

        "They generate Mega Stones at the start of the turn.":
            sonia @talking2mouth "That's right."

            $ ValueChange("Nate", 1, 0.75, changemood=False)

        "They teach a Pokémon moves.":
            sonia @happy "This is technically correct, but all Foreverals do that, actually. That's not unique to Megaverals. They actually generate... well, 'Mega Stones' at the start of each turn."
            
        "They allow a Pokémon to stay Mega Evolved after battle.":
            sonia @happy "Oh, wouldn't that be a marvel? That's not {i}quite{/i} right, though. They actually generate... well, 'Mega Stones' at the start of each turn."
else:
    sonia @talking2mouth "They actually generate... well, 'Mega Stones' at the start of each turn."

sonia @closedbrow talkingmouth "Although... they're wispy, and non-solid. Not very stonelike at all. It might be more accurate to say they generate 'emanations' that have the properties of Mega Stones."

nate @talkingmouth "Gotcha. What happens if a Pokémon's holding an item when the stone is generated?"

sonia @talking2mouth "Oh, they'll simply toss it away."

nate @talkingmouth "Right... I've got a follow-up question, then. How do Gigaverals work?"

if (HasEvent("Nate", "DoQuiz")):
    menu:
        "They allow a Pokémon to Gigantamax.":
            sonia @happy "Ooh, this is actually a fascinating subject. They {i}don't{/i} allow a Pokemon to Gigantamax, but it's a {i}very{/i} similar phenomenon that seems to have an entirely different power source than Eternatus."

            sonia @talking2mouth "They work basically the same as Megaverals. Except instead of generating 'Mega Stones,' they generate miniature 'Wishing Stars.'"

        "They double a Pokémon's weight.":
            sonia @surprised "Er... they actually triple a Pokémon's weight, but they also do a good bit more than that."

            sonia @talking2mouth "They work basically the same as Megaverals. Except instead of generating 'Mega Stones,' they generate miniature 'Wishing Stars.'"

        "They don't.":
            sonia @sad "...Now, that's not very nice. If you don't want to be part of this fun quiz, you could've just said no."

            sonia @talking2mouth "Nate, they work basically the same as Megaverals. Except instead of generating 'Mega Stones,' they generate miniature 'Wishing Stars.'"
            
        "Almost identically to Megaverals.":
            sonia @happy "True! And is it alright if I nerd out about the 'Wishing Stars' they generate?"

            red @happy "Go ahead."

            $ ValueChange("Sonia", 1, 0.75, changemood=False)
else:
    sonia @talking2mouth "They work basically the same as Megaverals. Except instead of generating 'Mega Stones,' they generate miniature 'Wishing Stars.'"

sonia @closedbrow talkingmouth "These 'Wishing Stars,' in addition their ethereal, unsolid nature, don't seem to truly invoke the G-Max phenomenon as I was familiar with in Galar."
sonia @angrybrow happymouth "Rather, it seems to be trying to {i}imitate{/i} G-Max, but without the power or size typically associated with the phenomemon." 
sonia @angrybrow happymouth "For this reason, the Pokémon only get roughly three times bigger, as opposed to the approximate 25 meters commonly achieved in Galar."
sonia @happy "This new phenomenon could be called 'Minigigamax!'"
sonia @talking2mouth "It's the oddest thing, though. I'm not too familiar with Mega Evolution, but the energy being emitted from the Gigaverals don't seem to have any relation to anything that could invoke a Dynamax-like effect."
sonia @closedbrow talking2mouth "It truly seems like the Pokémon's genetics are just being altered on the basis of nothing more solid than what it wishes."

red @talkingmouth "I think Professor Oak said something similar to that."

nate @talkingmouth "Okay, I think I'm getting this now. Diverals. They...?"

if (HasEvent("Nate", "DoQuiz")):
    menu:
        "They swap a Pokémon's Form.":
            sonia @happy "Yes, that's right. Pokémon with extreme sexual dichotomy, regional variations... Diverals seem to be able to trigger a shift between those."

            $ ValueChange("Nate", 1, 0.25, changemood=False)

        "They swap a Pokémon's type.":
            sonia @talking2mouth "Occasionally, but not specifically. Rather, it seems that Diverals swap between forms of the same species. This {i}may{/i} result in a type change."
            
        "They swap a Pokémon's sex.":
            sonia @talking2mouth "Not that I've seen. Even if swapping between forms of Nidoran, the sex of the creature appears to remain the same... besides the obvious, of course. Rather, it seems that Diverals swap between forms of the same species."
            
        "They swap a Pokémon's species.":
            sonia @talking2mouth "Bit off. They only seem to be able to swap between forms of the same species."
else:
    sonia @talking2mouth "Pokémon with extreme sexual dimorphism, regional variations... Diverals seem to be able to trigger a shift between those."

sonia @talking2mouth "Diverals are able to swap a Pokémon's form in-battle, or even out of battle, it should be noted. Though if its form is switched out-of-battle, it seems it isn't able to hold a Foreveral."
sonia @closedbrow talking2mouth "Too much interference from the energy waves, I suppose."
sonia @sad "Actually, truth be told, I don't have any idea why that doesn't work. I'm really just firing science at the wall here, and seeing what sticks."

nate @happy "Hey, you're doing fine from my point of view! Last question. What is this, number six?"

if (HasEvent("Nate", "DoQuiz")):
    menu:
        "Yes. That was an easy question.":
            $ ValueChange("Nate", 1, 0.25, changemood=False)
            nate @happy "Funny guy."

        "No, it's seven.":
            sonia @talking2mouth "No, no, this is number six. Well... {i}this{/i} one is. The next one will be seven, I suppose."

        ">Stay silent":
            pass

nate @talkingmouth "Finally, what do Foreverals and Everals do?"
 
if (HasEvent("Nate", "DoQuiz")):
    menu: 
        "FVLs do anything, EVLs make it easier to evolve Pokémon.":
            sonia @talking2mouth "Right you are."
            $ ValueChange("Nate", 1, 0.75, changemood=False)
        
        "FVLs make Pokémon live forever, EVLs make Pokémon eat apples.":
            sonia @surprisedbrow talking2mouth "Not quite."

        "FVLs let Pokémon level up, EVLs let Pokémon evolve.":
            sonia @surprisedbrow talking2mouth "Not quite."

        "FVLs prevent Pokémon from evolving, EVLs make Pokémon evolve.":
            sonia @surprisedbrow talking2mouth "Not quite."
else:
    sonia @talking2mouth "Foreverals do pretty much anything, while Everals make it easier to evolve Pokémon."

sonia @talking2mouth "Foreverals seem to provide a random boost to stats, or moves, or provide new abilities... they're custom boosts for the Pokémon they're equipped to, essentially."
sonia @closedbrow talkingmouth "Everals, on the other hand, don't often provide powerful boosts, but they make a Pokémon easier to train or evolve."
sonia @talking2mouth "Finally, something most Foreverals have in common is that they can change the type of [pika_name], and teach moves."

redmind @thinking "Right, but those moves are capped by the 'liberation limit'..."

red @surprised "Oh, wait! Will other Pokémon be affected by the liberation limit? Like, do I need to worry about the Foreverals I give to a different Pokémon?"

sonia @talking2mouth "Doesn't appear so. Besides the obvious addendum that a Pokémon can't draw power from a Foreveral it's incompatible with, of course."

show nate:
    ease 0.5 xpos 0.33

show sonia:
    ease 0.5 xpos 0.66

if (HasEvent("Nate", "DoQuiz")):
    nate @happy "Well, hey, I appreciate the info, S & [nate_name]! This'll really help me flesh out my report."

else:
    nate @happy "Well, hey, I appreciate the info, S! This'll really help me flesh out my report."

sonia @talking2mouth "It's a pleasure. I really feel like I'm doing something grand, now. This is {i}immeasurably{/i} exciting."

nate @talkingmouth "Great! Keep that sunny smile. Now, I gotta bounce."

show nate:
    parallel:
        easeout_bounce 3.0 ypos 0.0

    parallel:
        ease 3.0 xpos -0.15

pause 4.0

show sonia with dis

sonia @closedbrow talking2mouth "Ah, I see what he did there. Clever."

pause 1.0

sonia @talking2mouth "Oh, right, is there something I could help you with?"

red @talkingmouth "Yeah, I actually came here to talk to Professor Oak. Is he around?"

sonia @talking2mouth "Sure, let me just call him."

show sonia:
    ease 0.5 xpos 1.2

pause 1.0

sonia @talking2mouth "Professor! Your food is here!"

redmind @confusedeyebrows frownmouth "What?"

show sonia:
    ease 0.5 xpos 0.5

sonia @talking2mouth "He doesn't usually come out of his office unless I tell him that."

red @happy "Oh, I'm sure he'd come out for me. He called me here."

sonia surprisedbrow happymouth "Are you, now?"

hide sonia with dis

pause 0.5

stop music fadeout 1.5
queue music "audio/music/power plant_start.ogg" noloop fadein 1.0
queue music "audio/music/power plant_loop.ogg"

show oak happy with dis

oak @talkingmouth "Hello! That'll be two thousand, right?"

show oak surprisedbrow frownmouth with dis

red @talkingmouth "That, plus tip."

oak @talking2mouth "[first_name]? I didn't know you were working for Pokéats."

show oak -surprisedbrow -frownmouth with dis

red @sweat closedbrow talkingmouth "Well, I had to do something to pay for Kobukan."

oak @happy "Oh! That's what I wanted to tell you about, lad! I think I may have discovered how we could pay for that."

red @confusedeyebrows frownmouth "Hm?"

oak @talkingmouth "You see, ever since you reminded me that you didn't have a way to pay for Kobukan, I've been looking for a way to avert that problem."

redmind @confusedeyebrows frownmouth "Really? I'd kinda assumed that you'd forgotten."

oak @happy "And I do believe we may have a solution!"

red @talkingmouth "Is it just... paying for me, too?"

oak @sadbrow talking2mouth "...I wish I could, lad, but I don't have the funds for that. I could afford Blueberry if I really scraped together everything I had, but Kobukan's far more expensive, and the way it is now..."

red @sad2eyes angryeyebrows talking2mouth "...It's fine. I get it. So what were you thinking?"

oak @happy "A research grant, my boy! If I could secure a research grant to study Foreverals, your Pikachu, and perhaps even the long-term effects of Frienergy--"

show oak surprisedbrow frownmouth

red @surprised "Woah, woah, wait! I thought you binned your Frienergy research?"

oak -surprisedbrow -frownmouth @closedbrow talking2mouth sweat "Well, the work I had been working towards is not something I particularly care to pursue anymore. The effects are, clearly, too damaging to you for me to attempt pursuit any longer."

redmind @confusedeyebrows frownmouth "I appreciate the thought, Sam, but hasn't the damage basically already been done?"

oak @talkingmouth "At the very least, your power should still be catalogued. That could be worth a few years' of research. Though it will understandably take a secondary position to the power of the Foreverals."

red @talkingmouth "Okay. So... what do I do? To help you get this research grant?"

oak @happy "Well, exactly what you're doing already!"

red @talkingmouth sweat closedeyes "Sam, you have to stop inviting me over here to tell me to keep on doing what I was already doing."

oak @talkingmouth "Continue producing these Foreverals. Whatever mechanism [pika_name] produces them by, you must do {i}more{/i} of that!"

red @talkingmouth "Okay. And if you get this grant, you could use it to pay for my attendance here?"

oak @surprisedbrow talking2mouth "Hm?"

oak @happy "Oh, I see what you mean! No, not at all. That'd be unethical, to use research funding on a personal project!"

redmind @thinking "Personal project? He's been talking to Whitney."

red @talkingmouth "Okay. So what {i}were{/i} you thinking?"

oak @talkingmouth "Well, these gems represent an absolutely unsurpassed power boost for any Pokémon they're given to."
oak @talkingmouth "I took a quick course on business over the weekend, and it seems we can exchange these Foreverals for monetary gain!"

pause 1.0

red @confusedeyebrows talking2mouth "You're suggesting we sell them?"

oak @talkingmouth "Precisely. And not to just anyone, but to Champions! According to the laws of supply and demand{w=0.5} (which I just learned about){w=0.5}, you, as sole provider of these gems, should be able to set essentially any price."

pause 2.0

show oak sadbrow frownmouth with dis

red @sad "I... don't know. I feel like that would kinda cheapen the whole '[pika_name] has a special power' thing, if every champion had one."

oak @talking2mouth "Er... well... I'm not quite sure if I know how to resolve that concern."

red @sad2eyes talking2mouth "I guess I should be practical about this."
red @talkingmouth "Okay. Well, do you have a Champion in mind who would be willing to buy?"

oak @talking2mouth "Not particularly. We've got a good few months before your first payment is due." 
oak -sadbrow -frownmouth @talkingmouth "Between Instructor Wallace, Instructor Alder, Advisor Lance, and the many alumni of Kobukan, we should be able to contact pretty much any one of them."
oak @closedbrow talkingmouth "This is possible only due to the reputation and connections that Kobukan affords you. I'm just as thankful they hired me as you are that they let you in."

red @closedbrow talking2mouth "Hm."

pause 1.0

oak @talkingmouth "Well, we don't need to make any decisions now. As I said, it'll be a good few months."

pause 1.0

oak @closedbrow talking2mouth "But... there are two things you should keep in mind."

red @talkingmouth "Yeah?"

oak @talkingmouth "When it comes time to pick a 'customer,' you may want... well... to be rather coldhearted about how you approach them. It's tempting to just ask for enough money to get you through Kobukan, I warrant, but..."
oak @sad2eyes talking2mouth "...Do think about what some additional funds could acquire you. Your mother could retire. You could evolve your Pikachu. If you ask for enough, you could even send your own progeny to Kobukan."

pause 1.0

red @sadbrow talking2mouth "I don't like the idea of asking for more than these gems are worth."

oak @talking2mouth "I know you don't, lad. And early in my career, I thought similarly, continuously sacrificing financial success for 'pure science.' I worked harder than I should, and my family suffered for it."
oak @closedbrow talking2mouth "I'd hate to see you repeat my mistakes, as numerous as they are. Ask yourself what prosperity and security, for you and your family, is worth. If a couple stiff words, once, can secure all that, might it be the 'moral' choice?"

pause 0.5

oak @closedbrow talkingmouth "Well, I couldn't say. I'm no philosopher, I work on {i}real{/i} sciences. But do keep it in mind."

pause 1.0

red @talking2mouth "Right. What was the second thing I should remember?"

oak @surprisedbrow talking2mouth "Hm?"

red @talkingmouth "You said I should remember two things."

oak @closedbrow talking2mouth "I don't... I don't {i}remember{/i} that..."

red @confusedeyebrows talking2mouth "Oh. Maybe I... maybe I mis-remembered?"

oak sad2eyes talking2mouth "Er... yes, maybe."

pause 0.5

oak -sad2eyes @talkingmouth "Well, I should be getting back to work."

red @talkingmouth "Alright. Seeya, Sam."

oak happy "Goodbye. Remember, you're always welcome to drop in any time."
oak surprisedbrow frownmouth @surprised "Oh, but, before that--my Pokéats?"

red @happy sweat "Sam, that was a joke!"

hide oak with Dissolve(1.0)

red @closedbrow talking2mouth "Alright. Time to myself, at last. Let's see who's around."

pause 0.5 

red @sweat closedbrow talking2mouth "Though... I should probably get changed first, huh?"

call freeroam from _call_freeroam_17

$ HealParty()

scene suitenight 
show leaf:
    xpos 0.66
show ethan:
    xpos 0.33
with splitfade

show screen songsplash("Viridian Forest", "Zame")
stop music fadeout 1.5
queue music "audio/music/viridianforestgentle_start.ogg" noloop
queue music "audio/music/viridianforestgentle_loop.ogg"

pause 1.0

if (HasEvent("Nate", "FindOutLeaf")):
    red @talkingmouth "Hey, Leaf."

    leaf @talkingmouth "Hey yourself. Where've you been?"

    red @talkingmouth "That's my line! I was worried, we didn't see you all day. I even asked Nate where you were."

    leaf @happy "Aw, you were that worried about me?"

    $ ValueChange("Leaf", 1, 0.66)

    leaf @flirtbrow talkingmouth "I'm so flattered."

    red @talkingmouth "Yeah, you seem to interpret everything I say as some form of flattery. Where have {i}you{/i} been?"

else:
    red @surprised "Leaf? You're here?"

    leaf @surprisedbrow talking2mouth "Hm? Yeah, I'm here."

    red @talkingmouth "We were worried about you. None of us saw you all day."

    leaf @closedbrow talkingmouth "I'm {i}very{/i} sorry for depriving you of my presence."

    show leaf: 
        xpos 0.66 ypos 1.0
        ease 0.3 ypos 1.2
        pause 0.5
        ease 0.3 ypos 1.0

    ethan @talkingmouth "No, but for real, where have you been?"

leaf @talking2mouth "Looking for Tia, obviously."

leaf @closedbrow talking2mouth "Honestly, kinda peeved you guys left me to do it by myself."

ethan surprisedbrow frownmouth @surprised "Wait... you just ditched classes all day to look for Tiamat?! The {i}dragon?{/i}"

leaf @talking2mouth "Careful, these walls are thin. And, like, {i}yeah{/i}. She flew me across an ocean? Twice? I think that's fair."

show ethan -surprisedbrow -frownmouth -surprised with dis

red @closedbrow talking2mouth sweat "Leaf, you would rip up your diploma to help a guy who handed you a coffee once."

if (HasEvent("Nate", "FindOutTia")):
    leaf @closedbrow talkingmouth "We'll see. Anyway, Tia is--"

    show leaf surprisedbrow frownmouth with dis

    red @closedbrow talking2mouth "In the forest, I know. Nate told me."

    pause 1.0

    leaf @talking2mouth "Oh."

    pause 1.0

    leaf @talking2mouth "So... me ditching classes all day was..."

    ethan @closedbrow talking2mouth "Entirely unnecessary, yes."

    pause 1.0

    leaf closedbrow talkingmouth "Hm."

    pause 1.0

    leaf @talkingmouth "Excuse me for one second."

    show leaf:
        xpos 0.66
        ease 0.5 xpos 1.1

    pause 1.0

    show suitenight with vpunch

    leaf "{cps=2}AAAAAAAAAGH.{/cps}"

    show leaf -closedbrow -frownmouth:
        xpos 1.1
        ease 0.5 xpos 0.66

    leaf @happy "Okay, I'm cool. That's cool. Glad we're on the same page. Ten out of ten."

    leaf @flirtbrow talking2mouth "Anyway, Tia's in the forest. I'm sneaking out tomorrow night to find her."

else:
    leaf @closedbrow talkingmouth "We'll see. Anyway, Tia is in the forest. I'm sneaking out tomorrow night to find her."

ethan @unamusedeyebrows playfuleyes talking2mouth "Are you, now?"

leaf @happy "Yup, you're welcome to join. You can totally say no. I'll just assume you have no balls."

ethan @talking2mouth "That's toxic."

leaf @flirtbrow talking2mouth "Eat a Pecha about it."

ethan @talkingmouth "No, seriously, think about this. If the forest is a dangerous enough place to keep Tea there for multiple days, then what can we even do?"

if (HasEvent("Nate", "FindOutSabrina")):
    red @talkingmouth "Nate told me that Sabrina's in the forest... It sounded like Instructor Will was missing, too. They're all Espers, right?"
elif (HasEvent("Nate", "FindOutWill")):
    red @talkingmouth "Nate told me that Instructor Will's in the forest... It sounded like Sabrina was missing, too. They're all Espers, right?"
else:
    red @sad2eyes sadeyebrows talking2mouth "Actually... I heard that Sabrina and Will are missing, too. I wonder if it's related. They're all Espers, right?"

ethan @talkingmouth "I don't know. Would you call a Psychic-type Pokémon an Esper?"

leaf @closedbrow talking2mouth "Maybe an Esper is just a Psychic-type human..."

show leaf surprisedbrow frownmouth with dis

ethan @talkingmouth "These are the thoughts Leffela comes up with while screaming in the shower."

leaf -surprisedbrow -frownmouth angry "It's not {i}screaming{/i}! It's {i}singing{/i}!"

ethan @talkingmouth "Whatever it is, it could wake up a Snorlax."

leaf @angry "That's it, you! Let's battle! I'll defend my dulcet tones at the tip of a blade!"

ethan @closedbrow talkingmouth "I don't think--"

stop music fadeout 1.5

queue music "audio/music/potown_start.ogg" noloop
queue music "audio/music/potown_loop.ogg"

$ hideside = True

show ethan surprisedbrow frownmouth
show leaf surprisedbrow frownmouth
with dis

narrator "Suddenly, you hear a couple of voices coming from the closed door to Yellow's bedroom."

yellow @talkingmouth "{size=30}P-p-p-please! No! Leave me alone!{/size}"

blue @talkingmouth "{size=30}'Please, no!' You make me sick! Stop pretending! You're going to give me it {i}all!{/i}{/size}"

ethan @confusedeyebrows playfuleyes talking2mouth "'Give me it all?' Talk about a double object construction error. Dude needs to learn to use indirect objects."

leaf @surprised "That's what you're concerned about?! Blue's attacking Yellow, or... or worse!"

ethan @closedeyes unamusedeyebrows "Nah. This is just a hilarious misunderstanding. Trust me, I know this stuff."

blue @talkingmouth "{size=30}I hope you're not misunderstanding me! If you don't give me what I want, I will literally stab you!{/size}"

ethan @confusedeyebrows playfuleyes talking2mouth "...That does, admittedly, remove some ambiguity."

yellow @talkingmouth "{size=30}S-someone... please, help!{/size}"

blue @talkingmouth "{size=30}Cry some more! Only the perfectly-timed arrival of some heroes could possibly stop a terrible thing from happening to you...{/size} {size=20}mumble.{/size}"

pause 1.0

yellow @talkingmouth "{size=30}What was that?{/size}"

blue @talkingmouth "{size=30}I said... {w=0.5}{/size}{size=20}tender maiden.{/size}"

pause 1.0

show ethan closedbrow
show leaf closedbrow
with dis

show screen songsplash("Viridian Forest", "Zame")
stop music fadeout 1.5
queue music "audio/music/viridianforestgentle_start.ogg" noloop
queue music "audio/music/viridianforestgentle_loop.ogg"

yellow @talkingmouth "{size=30}You don't sound into it.{/size}"

blue @talkingmouth "{size=40}I'm not!{/size} Why don't we just ask them normally?!"

yellow @talkingmouth "This was {i}your{/i} idea!"

blue @talkingmouth "Yeah, but it's {i}your{/i} job to tell me when my ideas are stupid!"

pause 1.0

show ethan -closedbrow -frownmouth
show leaf -closedbrow -frownmouth
with dis

ethan @talkingmouth "Pick up the phone. I called it."

leaf @talking2mouth "I still think busting in there would have been safer."

ethan @talkingmouth "You might have a bit of a hero complex."

$ hideside = False

leaf @flirtbrow talking2mouth "Oh no. I want to be heroic. I want to help those in need. What a character flaw."

show ethan surprisedbrow frownmouth
show leaf surprisedbrow frownmouth
with dis

red @talking2mouth "Guys, focus up. I'm going to knock on their door."

show blank2 with splitfade

$ PlaySound("knock.ogg")

pause 1.0

blue @talkingmouth "Come in!"

scene yellowroomnight 
show blue:
    xpos 0.8 ypos 1.15 xzoom -1
show leaf:
    xpos 0.2 xzoom -1
show ethan:
    xpos 0.4
show yellow:
    xpos 0.6 ypos 1.15
with splitfade

red @surprised "Woah. That's pink."

$ hideside = False

blue @happy "Welcome to the{w=0.5}.{w=0.5}.{w=0.5}."

pause 0.5

blue closedbrow talking2mouth "No. No, I can't do this. No."

yellow @sadbrow talkingmouth "C'mon, Blue. At least give it a chance."

show blue angrybrow frownmouth with dis

red @confused "What... what's happening here?"

narrator "Spread out on a short, square table in front of you are pieces of paper, a mat depicting some sort of ruined temple, and a few action figures scattered about."
narrator "There's a thick book on the center of the table that says, in bold, emblazoned font, 'Inferno & Logos'."

leaf @surprised "Wait. Hold the front door. I know this! This is that one board game they play in that show, right? The one with all the knights and dungeons and stuff?"

blue -angrybrow -frownmouth @closedbrow talkingmouth "It's not a board game, and it existed before the show."

yellow @talkingmouth "...But yes."

leaf @angrybrow happymouth "Oh my god, Blue, you {i}play{/i} this? I didn't realize you were a {i}nerd!{/i}"

blue @closedbrow talkingmouth "I do more than just play it. I'm the GM."

ethan @talkingmouth "GM?"

blue @talkingmouth "Game Master. It means I decide what the enemies do, I control the narrative, I roleplay the NPCs, and... basically, I'm the boss."

leaf @closedbrow talkingmouth "That must be therapeutic."

blue @angrybrow talkingmouth "I don't know what you're implying, but you better quit it."

yellow @talkingmouth "We--"

blue @angrybrow frownmouth "!"

yellow @closedbrow talkingmouth "--{i}we{/i}, yes, {i}we{/i}, were hoping you might want to play with us."

show ethan:
    ease 0.5 ypos 1.15 xpos 0.4

ethan @talkingmouth "I'm game. I've seen a few people play on podcasts. Well, not 'seen,' but you know."

show leaf:
    ease 0.5 ypos 1.15 xpos 0.2

leaf @talking2mouth "Yeah, sure, but, like, the {i}only{/i} thing I know about this I got from sitcoms making fun of the people who play it. So, like, you're going to need to run me through the rules."

yellow @talkingmouth "That's completely fine. We set up a simple beginner's one-shot for you three, to see if you liked it. If you do, then you could be part of the campaign Blue and I play."

pause 0.5

yellow @happy "No pressure, though! I just want you to have fun, first and foremost. This game is a great way to explore your feelings, and be someone you've always wanted to be."

blue @talkingmouth "There's that. It's also a wargame. It teaches tactics better than any of our classes. Type matchups, positioning, move ranges... all that stuff {i}really{/i} matters in this game."

yellow @talkingmouth "Everyone finds something different to like about it."

narrator "You suddenly realize you're the only one left standing."

yellow @happy "Well, [first_name]? Would you like to play? I'd really like you to give it a chance. If you don't like it, you don't have to play again."

show blue closedbrow frownmouth with dis

narrator "You look at Blue. He seems to be avoiding your line of sight."

menu:
    "No.":
        show leaf surprisedbrow frownmouth
        show yellow sad
        show ethan sad2eyes frownmouth
        show blue surprisedbrow frownmouth
        with dis

        blue @talkingmouth "{i}No{/i}?"

        red @unamusedeyebrows playfuleyes talking2mouth "Blue, every moment we spend together, you're criticizing me, telling me what to do, or--at best--ignoring me. I don't want to play a game where {i}you're{/i} in charge, and can kill me at any moment, or criticize every move I make."

        pause 0.5

        blue -surprisedbrow @closedbrow talkingmouth "It would, uh, it'd mean a lot to Yellow..."

        red @talking2mouth "My problem isn't with her."

        pause 0.5

        blue @talkingmouth "I promise I won't... do any of that shit you said. Okay? I just want to keep GMing my original campaign with Yellow, and it doesn't really work with only one player."

        pause 1.0

        menu:
            "I said no.":
                $ AddEvent("Blue", "RejectGame")
                $ ValueChange("Leaf", -3, 0.2, False)
                $ ValueChange("Ethan", -3, 0.4, False)
                $ ValueChange("Blue", -3, 0.8)

                show blue angrybrow frownmouth with dis

                pause 2.0

                blue @talkingmouth "Fine."

                call clearscreens from _call_clearscreens_137
                scene blank2 with splitfade

                $ charactertype = "Berserker"
                $ dungeonskills = ["Risk-Taking", "Adaptability", "Pokémon Handling"]

                pause 1.0

                call texting from _call_texting_15

                jump postil

            "Okay. I'll hold you to that.":
                show leaf -surprisedbrow -frownmouth
                show yellow -sad
                show ethan -sad2eyes -frownmouth
                show blue -surprisedbrow -frownmouth
                with dis

                pass

    "Sure.":
        pass

show blue -closedbrow -frownmouth with dis

yellow @happy "That's great! The first step is to make a character."

leaf @talking2mouth "Oh, awesome. I'd like to play this, like, sexy femme fatale who wears a skimpy black dress and uses her feminine charms to get what she wants."

yellow @talkingmouth "Okay, we can definitely do that. Making a character from scratch usually takes quite a while, so we made some pre-made characters for you to choose from."

blue @talkingmouth "Every single one of the characters is completely optimized. I made them myself. {i}No-one{/i} could make a better character at that level, with that race/class combination."

yellow @talkingmouth "Based on what you said you wanted, I think... {i}this{/i} one would be best."

narrator "Yellow hands Leaf a piece of paper."

leaf @sadbrow talking2mouth "Okay, she's some kinda devil woman witch. That's pretty cool. But... don't you have a picture of her?"

yellow @happy "I'm afraid not. If a group is lucky enough to have an artist in it, then sometimes they'll make character portraits, but most of the time you just have to imagine what they look like."

leaf @closedbrow talkingmouth "Ah, I'm terrible at that. I just can't picture things in my head."

yellow @talkingmouth "That might be aphantasia."

leaf @surprised "Huh?"

yellow @talkingmouth "It's alright. If you {i}do{/i} have aphantasia, that's just another aspect of you, like being female, or being right-handed." 
yellow @talkingmouth "People with aphantasia can't picture things in their mind. It's uncommon, but not debilitating, or anything to worry about."

leaf @talking2mouth "Huh. How'd you know that, sweetie?"

yellow @closedbrow talkingmouth "Medical course."

ethan @talkingmouth "Oh, duh."

yellow @talkingmouth "Also... you can call me 'sweetie' if you want... but I'm older than you."

show ethan surprisedbrow frownmouth
show leaf surprisedbrow frownmouth
with dis

leaf @talking2mouth "What?!"

yellow @happy "Yes, I'm nineteen. You're only eighteen, right?"

leaf @talking2mouth "I... yeah, I am, but... {i}what?{/i} {i}You're{/i} nineteen?"

show ethan -surprisedbrow -frownmouth -surprised with dis

yellow @happy "I am, yes. So please respect your elders."

leaf -surprisedbrow -frownmouth -surprised @sadbrow talking2mouth "They... they grow up so fast..."

blue @talkingmouth "Ethan. What kind of character do you want to play?"

narrator "Ethan looks hopelessly at you."

ethan @talkingmouth "I mean, I don't want to double up, but [first_name] and I are going to give the same answer, right?"

blue @talkingmouth "There's only one of each character. You {i}can't{/i} double up."

ethan @talkingmouth "Alright. I guess... I dunno, I'd kinda like to be able to do a bit of everything?"

narrator "Blue nods thoughtfully and hands Ethan a piece of paper."

blue surprised @talkingmouth "Alright. Here's your character. He's a dwarven Twinblade Rogue. He can--"

ethan @talkingmouth "Can I play a chick?"

pause 1.0

blue -surprisedbrow -frownmouth -surprised frownmouth @talkingmouth "Yeah, fine. Just cross out the 'M' up on the top-right and write an 'F.'"

ethan @talkingmouth "Score."

yellow @talkingmouth "[first_name], do you--"

ethan @happy "Oh, wait, can I play a half-elf?"

blue @angrybrow happymouth "Y-yes."

pause 1.0

ethan @closedbrow talking2mouth "Oh, can I--"

blue angry "Yes, Ethan! You can make whatever changes you want! I made the character {i}perfect{/i} for his race, class, and sex, but if you want to change something and be {i}suboptimal{/i}, that's fine!"

leaf @flirtbrow talking2mouth "Woah, you made the character {i}perfect{/i}? And you made him male? What're you trying to say?"

blue @angry "That males get a +1 to Strength, which will help patch up the Twinblade Rogue's mediocre growth rates!"

leaf @surprisedbrow talking2mouth "Oh."

pause 1.0

show blue -angry with dis

leaf @talking2mouth "Wait, so what do I get, then?"

yellow @talkingmouth "You get an additional +1 to your Dexterity. That's optimal, for your character."

leaf @happy "Cool."

pause 0.5

yellow @talkingmouth "What about you, [first_name]? What kind of character do you want to play?"

$ charactertype = ""

label characterchoice:

menu:
    "[witoption] I cast the spells that makes the peoples fall down!":
        yellow @happy "So, a Warlock? They're very good at doing damage from a distance, but they're not very versatile and take a lot of naps."
        yellow @talkingmouth "Their special skills are [knowledgecolor]Lore Smarts{/color}, [witcolor]Cunning{/color}, and [patiencecolor]Learning.{/color}"
        yellow @talkingmouth "They're best for players with a lot of [knowledgecolor]Knowledge{/color}, [witcolor]Wit{/color}, and [patiencecolor]Patience.{/color}"

        $ charactertype = "Warlock"

    "[patienceoption] That thing was too big to be called a sword.":
        yellow @happy "So, a Fighter? They're pretty simple, but they're good at doing damage at close range, and they have enough defense to be on the frontlines, too."
        yellow @talkingmouth "Their special skills are [couragecolor]Physicality{/color}, [knowledgecolor]World Smarts{/color}, and [witcolor]Strategy.{/color}"
        yellow @talkingmouth "They're best for players with a lot of [couragecolor]Courage{/color}, [knowledgecolor]Knowledge{/color}, and [witcolor]Wit.{/color}"

        $ charactertype = "Fighter"

    "[charmoption] A hardened mercenary captain leading the vanguard!":
        yellow @happy "So, a Paladin? They're charismatic leaders that can do a little bit of everything! Like a Twinblade Rogue, but better!"
        yellow @talkingmouth "Their special skills are [couragecolor]Resilience{/color}, [patiencecolor]Leadership{/color}, and [charmcolor]Persuasion.{/color}"
        yellow @talkingmouth "They're best for players with a lot of [couragecolor]Courage{/color}, [patiencecolor]Patience{/color}, and [charmcolor]Charm.{/color}"

        $ charactertype = "Paladin"

    "[knowledgeoption] A mysterious dungeoneer who explores time and space!":
        yellow @happy "So, a Ranger? They're very in-tune with nature and their Pokémon. They know a lot about the wild, and are good at tracking!"
        yellow @talkingmouth "Their special skills are [charmcolor]Pokémon Handling{/color}, [patiencecolor]Healing{/color}, and [knowledgecolor]Pokémon Smarts.{/color}"
        yellow @talkingmouth "They're best for players with a lot of [charmcolor]Charm{/color}, [patiencecolor]Patience{/color}, and [knowledgecolor]Knowledge.{/color}"

        $ charactertype = "Ranger"

    "[courageoption] I would like to rage.":
        yellow @happy "So, a Berserker? They're strong and have lots and lots of health. The only downside is they can't do much outside of battle."
        yellow @talkingmouth "Their special skills are [couragecolor]Risk-Taking{/color}, [witcolor]Adaptability{/color}, and [charmcolor]Pokémon Handling.{/color}"
        yellow @talkingmouth "They're best for players with a lot of [couragecolor]Courage{/color}, [witcolor]Wit{/color}, and [charmcolor]Charm.{/color}"

        $ charactertype = "Berserker"

    "I'm going to make your job a living nightmare, Blue.":
        yellow @happy "So, a Bard? They're charismatic, persuasive, and good at avoiding combat! They don't do much {i}in{/i} combat, though..."
        yellow @talkingmouth "They're really only good at [charmcolor]Deception.{/color}"
        yellow @sadbrow talkingmouth "But... I'm not sure that's a good fit for you. Unless you {i}really{/i} want it?"
        
        $ charactertype = "Bard"

        narrator "[bluecolor]You sense that this may be a very poor decision...{/color}"

menu:
    "Yes, I want to be a [charactertype].":
        python:
            dungeonclass = charactertype
            if (charactertype == "Warlock"):
                TraitChange("Wit")
                dungeonskills = ["Lore Smarts", "Cunning", "Learning"]
            elif (charactertype == "Fighter"):
                TraitChange("Patience")
                dungeonskills = ["Physicality", "World Smarts", "Strategy"]
            elif (charactertype == "Paladin"):
                TraitChange("Charm")
                dungeonskills = ["Resilience", "Leadership", "Persuasion"]
            elif (charactertype == "Ranger"):
                TraitChange("Knowledge")
                dungeonskills = ["Pokémon Handling", "Healing", "Pokémon Smarts"]
            elif (charactertype == "Berserker"):
                TraitChange("Courage")
                dungeonskills = ["Risk-Taking", "Adaptability", "Pokémon Handling"]
            else:
                dungeonskills = ["Deception", "Deception", "Deception"]

    "Actually, let me rethink...":
        jump characterchoice

ethan @talkingmouth "Man, I {i}knew{/i} you would pick a [charactertype]. Guess it's a good thing I didn't choose one, then."

leaf @talking2mouth "Wait, so, then, what's your character, Blue?"

blue @talkingmouth "The GM doesn't get a character. The GM is the entire world."

yellow @closedbrow talkingmouth "Sometimes GMs {i}will{/i} create their own character, but... um..."

blue @angrybrow talkingmouth "Don't do that shit. It's the GM's job to make the players feel like heroes, not to try and take any of that glory for yourself."

ethan @talking2mouth confusedeyebrows "How selfless. You {i}are{/i} still Blue, right?"

blue @angry "It's not about selflessness! It's just how the game's played! It's literally in the rules!"

pause 1.0

blue @closedbrow talking2mouth "Anyway, the fourth character is Yellow's."

yellow @happy "My character's name is Amarillo Del Bosque Verde! She's a Halfling, and she's a cleric, and she has a pet Rattata that she always keeps with her."

blue @talkingmouth "She's a lot higher level than you guys, but..."

yellow @talkingmouth "I don't mind being reset to level 1, to play alongside everyone else. I prefer the RP parts of the game, anyway."

blue @closedbrow talkingmouth "Thanks."

leaf @closedbrow talkingmouth "RP?"

ethan @talkingmouth "It means 'roleplay'. It's when instead of trying to slay the dragon, you try to lay the dragon."

leaf @sad "Oh, it's {i}that{/i} kind of game?"

yellow @closedbrow talkingmouth "Ethan, please stop confusing Leaf."

ethan @happy "{i}Mea culpa.{/i}"

leaf @talking2mouth "So, like, what are the {i}actual{/i} rules? Can I just say I become queen, and it happens?"

blue @talkingmouth "The rules are laid out in the rulebook."

narrator "Blue points to the book titled {i}Inferno & Logos{/i} on the table."

blue @closedbrow sweat talkingmouth "...But there's a lot of them to remember. So we'll walk you through this slowly."
blue @talkingmouth "The most important thing to remember is that, in this game, [bluecolor]you're only bringing one Pokémon with you.{/color}"

leaf @surprised "What?! That's not realistic! Why?"

yellow @talkingmouth "Most Inferno & Logos settings are based around a fictionalized version of the Heian period. Or 'middle ages' in Galar."
yellow @happy "Back then, before Poké Balls existed, if anyone was to partner with a Pokémon, they'd only be able to partner with one at most." 
yellow @talking2mouth "You had to {i}really think{/i} about who you wanted to partner with, since that might be the only Pokémon you'd ever meet who didn't want to eat you."

blue @closedbrow talkingmouth "That's right. So you're wrong, Leaf, it's actually {i}extremely{/i} historically accurate {i}and{/i} realistic."

yellow @sad2eyes happymouth "{size=30}As long as you ignore the magic...{/size}"

blue @talkingmouth "Anyway, this Pokémon is called your 'partner Pokémon.'"
blue @closedbrow talkingmouth "Creating a partner Pokémon is also a pretty in-depth process... so let's just use the Pokémon you have on hand for this one-shot."

label partnertutorial:

blue @talkingmouth "[bluecolor]Generally, the highest-level Pokémon in your party will be your partner.{/color}" 

$ PlaySound("Pokemon/pikachu_confused.ogg")

libpikachu @surprised "Piiiika?"

red @talkingmouth "Hm... is it alright if [pika_name] is my partner?"

blue @closedbrow talkingmouth "Yeah, sure. Tell you what, just--y'know, [bluecolor]whichever Pokémon is at the start of your party, that will be your partner.{/color} So just remember that before we go in."
blue @happy "No switching after you're inside! Whatever you go in with, you're stuck with!"

$ PlaySound("Pokemon/pikachu_happy1.ogg")

libpikachu @happyeyes talking2mouth "Pika."

yellow @talkingmouth "The higher your partner's level is, the better. But levels matter less in this game than type advantage does. So you should pick a partner that's good against the Pokémon in the environment."
yellow @happy "This dungeon will be full of Bug and Grass-types, by the way."

narrator "[bluecolor]Before entering a dungeon, you should use your Foreverals to make [pika_name] strong against Pokémon you expect to see in that dungeon.{/color}"
narrator "[bluecolor]For example, in this dungeon, which is full of Bug and Grass-types, you might want to equip a Flying or Fire Foreveral, and teach [pika_name] Flying or Fire moves.{/color}"
narrator "[bluecolor]Alternatively, you could switch a Flying or Fire-type Pokémon to the front of the party."

pause 1.0

blue @talkingmouth "Got that?"

menu:
    "One more time, please.":
        blue @closedbrow talkingmouth "...Nnrgh. Fine."

        jump partnertutorial

    "Got it.":
        pass

blue @thinking "[ellipses]"

blue @talkingmouth "Alright. Are you ready?"

$ dungeonrunonce = False

label beforetutorialdungeon:

stop music fadeout 1.5
queue music "audio/music/sealedruin.ogg"

if (not dungeonrunonce):
    blue @closedbrow happymouth "Welcome to the world of {i}Inferno & Logos{/i}."
else:
    blue @closedbrow happymouth "Welcome back to the world of {i}Inferno & Logos{/i}."

pause 1.0

call infestedbasementsetup from _call_infestedbasementsetup

$ HealParty()

jump StartDungeon

label aftertutorialdungeon:

show screen songsplash("Viridian Forest", "Zame")
stop music fadeout 1.5
queue music "audio/music/viridianforestgentle_start.ogg" noloop
queue music "audio/music/viridianforestgentle_loop.ogg"

$ AddEvent("Blue", "WonGame")
$ _rollback = True
$ isgame = False
scene yellowroomnight
show blue:
    xpos 0.8 ypos 1.15 xzoom -1
show leaf:
    xpos 0.2 xzoom -1 ypos 1.15
show ethan:
    xpos 0.4 ypos 1.15
show yellow:
    xpos 0.6 ypos 1.15
with Dissolve(2.0) 

$ ValueChange("Blue", 3, 0.8, False)
$ ValueChange("Leaf", 3, 0.2, False)
$ ValueChange("Ethan", 3, 0.4)

ethan @happy "Oh man, that was {i}great!{/i} How long have we been playing for...?"

yellow @talkingmouth "Well, it's... 2:00, so..."

show ethan:
    xpos 0.4
    ease 0.5 ypos 1.0

ethan @surprised "Woah, what?! That's crazy! I gotta go to sleep."

blue @closedbrow talking2mouth "Heh. I'm just that good. When I GM, {i}anyone{/i} could lose track of time."

show leaf:
    xpos 0.2
    ease 0.5 ypos 1.0

leaf @flirtbrow talking2mouth "Yeah, don't ruin it, sweetheart. I actually had a good time. I don't need you shoving your foot in that with your big ego."

blue @closedbrow frownmouth "Tch."

pause 1.0

show blue:
    xpos 0.8
    ease 0.5 ypos 1.0

blue @talkingmouth "What did you think, [first_name]?"

menu:
    "I had no idea you liked stuff like this.":
        $ AddEvent("Blue", "SurprisedBlueLikedGame")
        
        blue @closedbrow frownmouth "Hmph."

    "It was fun.":
        $ ValueChange("Blue", 3, 0.8)
        $ AddEvent("Blue", "LikedGame")

        blue @closedbrow "Hmph."

    "Might not be for me.":
        $ AddEvent("Blue", "DidntLikeGame")

        blue @closedbrow frownmouth  "Hmph."

pause 1.0

yellow @talkingmouth "We should probably all get to sleep. If anyone sleeps in, I'll wake you up, okay?"

leaf @happy "Thanks, sweetie. Goodnight, all!"

red @talkingmouth "Goodnight, you guys."

hide ethan
hide leaf
with dis

pause 1.0

show yellow:
    xpos 0.6
    ease 0.5 xzoom -1 ypos 1.0

yellow @happy "I think that went well."

blue @closedbrow talkingmouth "Maybe. I dunno. It wasn't as painful as I thought it would be."

pause 0.5

yellow @talkingmouth "You're doing the right things, Blue. You're making progress. It might just be inches by inches, but you're moving forward."

blue @closedbrow talkingmouth "Ugh, you sound like Daisy."

pause 1.0

yellow @happy "I like Daisy."

blue @talkingmouth "...Yeah, I do, too."

yellow @talkingmouth "Have you given any more thought to our picnic?"

blue @talkingmouth "Yeah, of course. I said we'd go on one, didn't I? Don't worry about it."

hide blue with dis

pause 0.5

yellow "[ellipses]"

label postil:

call clearscreens from _call_clearscreens_138
scene blank2 with splitfade

jump day010511