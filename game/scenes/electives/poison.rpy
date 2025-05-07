label poisonelective:

$ renpy.transition(dissolve)
show screen currentdate

scene map
show blank2:
    alpha 0.8

show classroom with dis

show poisontype:
    alpha 0.0 xalign 0.5 yalign 1.0
    ease 0.5 alpha 1.0

$ location = "poison"
$ passedclass = False

############################################################################################################################################################################################################################
#### 13. POISON    #######################################################################################################################################################################################################
############################################################################################################################################################################################################################
$ renpy.pause(1.0, hard=True)

call nateevent from _call_nateevent_1
call silverevent from _call_silverevent_1
call erikaevent("Poison") from _call_erikaevent
call ethanevent from _call_ethanevent_13

label afterpoisonsetup:

if (HasEvent("Instructor Koga", 2.1)):
    menu:
        "{b}>General Studies{/b}":
            pass

        ">Ask for move tutoring":
            jump movetutorpoison

        ">Craft items" if (HasEvent("Instructor Koga", 3.1)):
            jump itemcraftpoison

if (not HasEvent("Instructor Koga", 1)): #first class
    $ AddEvent("Instructor Koga", 1)
    $ renpy.pause(3.0, hard=True)

    red uniform closedbrow talking2mouth "I wonder where the teacher is?"
    ethan uniform happy "Did you know that if the teacher isn't here in fifteen minutes, you're legally allowed to leave?"
    red -thinking @talkingmouth "Well, yeah. There's no law saying we can't leave before fifteen minutes, either."
    red @confusedeyebrows talking2mouth "Although... I guess maybe Kobukan might have something weird like that? Probably not, though."

    stop music fadeout 0.5
    $ PlaySound("Whoosh.ogg")

    show koga with dis:
        alpha 0.3 matrixcolor TintMatrix("#424243")
        ease 1.0 alpha 1.0 matrixcolor TintMatrix("#fff")
    show smoke:
        alpha 0.0 xpos 0.5 yalign 3.0
        parallel:
            ease 3.0 yalign 0.5
        parallel:
            ease 0.5 alpha 1.0
            pause 0.5
            ease 3.0 alpha 0.0

    $ renpy.pause(1.0, hard=True)

    show koga thinking with dis

    play music "Audio/Music/Kimono_Start.ogg" noloop
    queue music "Audio/Music/Kimono_Loop.ogg"

    red @surprised "Whoa!"

    ethan @surprised "Was this guy here the whole time?!"
        
    koga @talkingmouth "Welcome to the {color=#0048ff}Poison class,{/color} children."
    $ BecomeNamed("Instructor Koga")
    koga @talkingmouth "I am your instructor, Koga."

    $ PlaySound("Whoosh.ogg")
    
    show koga:
        alpha 1.0 matrixcolor TintMatrix("#fff")
        ease 1.0 alpha 0.0 matrixcolor TintMatrix("#424243")
    show smoke:
        alpha 0.0 xpos 700 yalign 3.0
        parallel:
            ease 3.0 yalign 0.5
        parallel:
            ease 0.5 alpha 1.0
            pause 0.5
            ease 3.0 alpha 0.0

    $ renpy.pause(1.0, hard=True)

    show kogabg:
        alpha 0.0 yalign 1.0 xalign 0.5
        pause 0.5
        ease 0.5 alpha 1.0

    $ renpy.pause(2.0, hard=True)

    ethan surprised "What is this guy, some kind of ninja?"

    hide koga
    hide smoke

    koga @talking2mouth "I am both an expert in Poison-type Pokémon and the thirty-fifth grandmaster of Koga-ryu ninjutsu."

    ethan closedbrow talking2mouth "Of course..."

    koga @talking2mouth "You have come here to study Poison Pokémon.{w=0.5} In that, I will meet your expectations."
    koga @angrybrow talking2mouth "But that is not all I will teach you!"
    koga "I shall show you every weakness of the human and Pokémon mind--and how, in battle, they can be exploited."
    koga @closedbrow "Let me start this class with a simple question to you."
    koga @talking2mouth "What makes a Pokémon strong?"

    ethan "This sounds like a trick question, but it's gotta be--"

    Character("Rude Student") "\"The Pokémon's level, duh!\""
    Character("Rude Student") "\"Is that even a real question?\""

    koga @talking2mouth "Oh? And how can you be so sure?"

    Character("Rude Student") "\"What? Its combat potential will be higher, obviously!\""
    Character("Rude Student") "\"How can you be a teacher and not know that?\""
    Character("Rude Student") "\"Speaking of which, what kind of teacher is late to class?{w=0.5} I thought this was an elite university!\""

    show kunai:
        alpha 1.0 zoom 0.0 xpos 900 ypos 460
        ease 0.3 zoom 0.6 xpos 2000 ypos 640
    pause 0.15
    $ PlaySound("LightTap.ogg")

    $ renpy.pause(0.5, hard=True)
    ethan @surprised "Holy shuriken!"
    red @closedbrow talking2mouth "I think that was a Kunai, actually."

    Character("Rude Student") "\"...!\""

    hide kunai

    show poisclass:
        parallel:
            xalign 0.0
            ease 0.03 xpos -15
            ease 0.03 xpos 15
            ease 0.03 xpos 0
            repeat 2
        parallel:
            yalign 0.0
            ease 0.03 ypos -25
            ease 0.03 ypos 25
            ease 0.03 ypos 0
            repeat 2

    koga @angrybrow talking2mouth "Fool. If you understood Pokémon, you would understand why I remained hidden."
    koga @talking2mouth "Surely one of you can imagine?"
    koga @talkingmouth "I will even give you a hint:{w=0.5} it is more important than strength, technique, or skill itself."

    hide poisclass
    pause 1.5

    koga @closedbrow "Nobody knows? Well, then..."

    if (IsPresent("Hilda", "Poison")):
        show hildaintro:
            subpixel True
            alpha 0.0 xalign 0.5 zoom 1.0
            parallel:
                ease 1.5 alpha 1.0
            parallel:
                ease 5.0 zoom 0.75


        hilda uniform "Is it knowing your opponent before the encounter?"

        koga @talking2mouth "Go on."

        hilda @talkingmouth "Like, you analyze their weak points and capabilities beforehand so you don't have to make things up on the fly."

        pause 1.0

        koga @talking2mouth "...You."

        hilda @surprised "Wh-what?"

        if (IsDate(5, 4, 2004)):
            koga "What is your name?"

            hilda "Hilda, Sir."

        koga @talkingmouth "Explain your thinking, Hilda."

        hilda "It's really self-explanatory.{w=0.5} If you engage a Pokémon or a Trainer without knowing anything about them, you're immediately putting yourself at a disadvantage."
        hilda "It's Pokémon battling 101."

        koga @talkingmouth "Hilda is correct!"

        hide hildaintro with dis

    elif (IsPresent("Rosa", "Poison")):
        rosa uniform "Is it knowing your opponent before you get started?"

        koga @talking2mouth "Go on."

        rosa @closedbrow talking2mouth "Like, before you start the cameras rolling, everyone needs to know what part they're going to play, how they're going to play off each other."
        rosa @talkingmouth "It's the same way with battles, right?"

        pause 1.0

        koga @talking2mouth "...You."

        rosa @surprised "Y-yes?"

        koga @talking2mouth "You seem familiar. What is your name?"

        rosa @talkingmouth "Rosa, Sir. Maybe you saw me in {i}Samurai vs. Ninja: The Ultimate Kapowdown!!!{/i}?"

        koga @closedbrow talking2mouth "No, I don't watch documentaries."
        koga @talkingmouth "Regardless. Explain your thinking!"

        rosa @talkingmouth "I think it's self-explanatory.{w=0.5} You need to know what your opponent can do before you can stop them, right?"
        
        koga @talkingmouth "Rosa is correct!"

    koga @talking2mouth "Pokémon are not mere tools of brute strength.{w=0.5} You must understand your opponent's strengths; their weaknesses; their mentality."
    koga @talkingmouth "If you know these things, even the weakest Pokémon can defeat the strongest!"
    koga @talking2mouth "In the field, you must exploit every possible advantage."
    koga @talkingmouth "And if none are in sight, you must make them yourselves."
    koga @closedbrow talkingmouth "Confusion... poison... sleep...{w=0.5} all means of gaining the upper hand, and all signature tools of Poison-type Pokémon."
    koga @talkingmouth "You shall learn soon enough!"

    ethan happy "This guy is making it sound like we're going to assassinate someone rather than just study Pokémon."
    red @talkingmouth "Yeah... but why do you look so happy about that?"

    pause 2.0

    narrator "Koga lectures on the many ways the weak may uproot the strong."

    pause 2.0

    koga @closedbrow talkingmouth "And so our time here dwindles."
    koga "Very well. You are dismissed."

    hide koga
elif (not HasEvent("Instructor Koga", 2.1) and classstats["Poison"] >= 10):#Bad Breath
    show koga with dis
    if (not HasEvent("Instructor Koga", 2)):
        $ renpy.pause(1.0, hard=True)

        narrator "You're busy studying the anatomy of a wide array of Pokémon, when Instructor Koga suddenly materializes next to you."

        koga smilemouth @happy "You are progressing well within your studies. Do not think your efforts have gone unnoticed."

        red @happy "Thanks, Instructor."

        koga @talking2mouth "I pose to you a question: why do I have you studying Pokémon anatomy?"

        red @closedbrow talking2mouth "Hm... well, you have us studying Poison-types because that's what you're paid to do. But you have us studying the other types as well, because..."
        red @talkingmouth "Understanding other types gives us a better idea of how to shut down their capabilities, I think. Is that right?"

        koga @happy "Fwahaha! You are very astute, my pupil. Yes, that's right."
        koga @talkingmouth "When you understand your opponent's strengths, you understand how to make them weak." 
        koga @closedbrow talking2mouth "Never assume yourself prepared for a fight out of confidence in your {i}own abilities.{/i}"
        koga @talking2mouth "You must also be confident in your knowledge of your opponent's abilities. It is knowledge and preparation that win battles, not brute strength."

        red @angrybrow talkingmouth "I agree completely."

        koga @talkingmouth "Then perhaps you are ready to advance in this class."

        red @surprised "Oh, really? So, you can teach me some new stuff?"

        koga @closedbrow talking2mouth "Yes. The ultimate debilitating effect, created by my forebears in the Shogunate's youth. It is called {i}Bad Breath.{/i}"

        red @closedbrow talking2mouth "What does that do?"

        koga @closedbrow talking2mouth "If the opponent can be badly poisoned, it will be. If the opponent cannot, it will be paralyzed. And if it cannot be paralyzed, it will be confused."

        red @surprised "Woah?! A move with multiple effects?! How does that work?"

        koga @closedbrow talking2mouth "It is a secret shinobi technique. Do not worry about it."

        red @closedbrow talking2mouth "That sounds familiar."

        koga @angry "I will now administer the advancement exam--a one-on-one battle against me, a ninja master! Are you prepared?"

        red @happy "Absolutely, Sir!"

        $ AddEvent("Instructor Koga", 2)
    else:
        red uniform @talking2mouth "Koga, I've been doing my research into you and your Pokémon since the last time we battled, and I'm ready to try again."

    koga @talkingmouth "The battle's outcome is decided as soon as you choose your Pokémon. Now, which will it be? {color=#0048ff}A Poison-type will excel in this conflict.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    koga @angry "Attack with all you have!"
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("koga", TrainerType.Enemy, [
        Pokemon(546, level=11, moves=[GetMove("Absorb"), GetMove("Fairy Wind"), GetMove("Stun Spore")], ability="Prankster")
    ])

    call Battle([trainer1, trainer2], uniforms=[True, False]) from _call_Battle_37
    $ battlehistory["Instructor Koga1"]  = _return

    show koga with dis

    if (WonBattle("Instructor Koga1")):
        $ AddEvent("Instructor Koga", 2.1)

        koga @happy "You have clearly learned well. Fwahahaha! Fine, then: I will teach you my technique!"

        $ passedclass = True
        jump aftertutorintropoison
    
    else:
        koga @talking2mouth "Ah."
        koga @talkingmouth "A disappointing outcome. But I am certain you will return to remedy this. Do not let up on your training!"

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide koga with dis
elif (not HasEvent("Instructor Koga", 3.1) and classstats["Poison"] >= 20):#Poison Barb
    show koga with dis
    if (not HasEvent("Instructor Koga", 3)):
        $ renpy.pause(1.0, hard=True)

        koga @happy "Fwahahaha! You, [first_name]: tell me, what are the seven tools of the bandit?"

        red uniform @surprised "I am absolutely certain that you have never told us that."

        koga @closedbrow talking2mouth "Why would I ask a question to which I had already given the answer?"

        red @surprised "Um."

        pause 1.0

        red @closedbrow talking2mouth "Just... going on a limb here... a knife, a lockpick, a screwdriver, a chisel, a corkscrew, and a cyanide capsule?"

        koga @angry "That is only six tools."

        red @closedbrow talking2mouth "Well, yeah, the seventh one is a secret."

        pause 1.0

        koga @happy "Hm. You are swift on your feet, [last_name]-san. My daughter was not incorrect to place you within her Battle Team."

        red @surprised "Oh, right! I completely forgot you were Janine's Dad. Um, can I ask you questions about her?"

        koga @closedbrow talking2mouth "Hm... I will permit this. I am her father, after all, and it is my ninja duty to share embarrassing baby stories about her."

        red @surprised "Do you have pictures?"

        koga @happy "Many pictures, yes. Photography is one of the ninja arts."

        red @happy "So... we're in class, now, but can I, like, come to your office hours and we can gossip?"

        koga @closedbrow talking2mouth "This is acceptable."

        show koga with vpunch

        koga @angry "However! Before I am to share this confidential information, I would ask you to prove yourself worthy!"

        red @closedbrow talking2mouth "Would passing another class advancement exam qualify?"

        koga @closedbrow talking2mouth "Yes. And, in doing so, I will teach you how to make a {i}true{/i} bandit's tool: the Poison Barb! It will increase the power of your Poison-type moves by 10%%."

        red @happy "Cool."

        red @talkingmouth "I'm ready now, Sensei."

        pause 1.0

        show koga closedbrow talking2mouth with dis

        "{color=#5f3869}Sensei Koga{/color}" "\"You need not call me Sensei. I am not that weeaboo, Marshal. Just 'Instructor' works fine, thank you.\""

        show koga -closedbrow -talking2mouth with dis

        red @sweat happy "Oops! Noted."

        $ AddEvent("Instructor Koga", 3)
    else:
        red uniform @talking2mouth "Koga, I've been doing my research into you and your Pokémon since the last time we battled, and I'm ready to try again."

    koga @talkingmouth "Pick, then, the Pokémon you will use in this trial of ninjutsu. [bluecolor]I will be relying on the insidious powers of the Poison-type.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    koga @angry "Let us see if your preparations bear fruit."
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("koga", TrainerType.Enemy, [
        Pokemon("Venonat", level=21, moves=[GetMove("Psybeam"), GetMove("Poison Powder"), GetMove("Supersonic"), GetMove("Venoshock")], ability="Compound Eyes", item="Oran Berry")
    ])

    call Battle([trainer1, trainer2], uniforms=[True, False]) from _call_Battle_100
    $ battlehistory["Instructor Koga2"]  = _return

    show koga with dis

    if (WonBattle("Instructor Koga2")):
        $ AddEvent("Instructor Koga", 3.1)

        koga @talkingmouth "Sufficient. A performance worthy of your prize."

        $ GetItem("Poison Barb", 1, "Koga snaps his fingers and, in a puff of smoke, a Poison Barb appears in your hands.")
        
        $ renpy.pop_call()
        jump aftertutoring
    
    else:
        koga @talking2mouth "Hm."
        koga @talking2mouth "I had expected more. Ensure that I see it during your {i}next{/i} challenge."

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide koga with dis
elif (not HasEvent("Instructor Koga", 4.1) and classstats["Poison"] >= 30):#Venoshock
    show koga with dis
    if (not HasEvent("Instructor Koga", 4)):
        $ renpy.pause(1.0, hard=True)

        koga @talkingmouth "[first_name], I would ask you a question."

        red @confused "Is it another thing I don't know the answer to, like your tools of the bandit question?"

        koga @closedbrow talking2mouth "No. That question tested the flexibility of your thinking. This one, I believe, you have the power to understand by yourself."

        koga @talkingmouth "I have told you what strength is, yes?"

        red @talkingmouth "Yes. You've said it's versatility."

        koga @happy "Correct. Versatility, and the ability to capitalize on an opponent's weakness."

        koga @angry "What, then, is 'weakness', beyond something to be capitalized on?"

        red @closedbrow talking2mouth "That's a tough one. If strength is versatility, then it'd be easy for me to say that weakness is just its opposite. Single-mindedness, or something like that."
        red @confused "But that feels a bit too easy for this class. All your questions are trick questions, with, like, three layers of trickery to them."

        koga @talkingmouth "Awareness is power: it is good that you have noticed. You learn well."

        red @closedbrow talking2mouth "Right..."
        red @confused "So, I guess my final answer is... uh... also versatility."

        koga @surprised "Oh?"

        red @closedbrow talking2mouth "Well, not versatility {i}itself.{/i} But the answer is versatile. Like, weakness isn't one specific thing that you can seek out and utilize in every single foe."
        red @talking2mouth "Every foe has a different weakness. Right?"

        pause 1.0

        koga closedbrow frownmouth @closedbrow talking2mouth "Hm."

        pause 1.0

        red @sweat happy "Uh... Instructor Koga? You're not giving me much to go on here."

        koga happy @happy "Your answer is correct enough."
        koga @talkingmouth "You are right, that every foe has a different weakness. So you cannot exploit every weakness the same way." 
        koga @closedbrow talking2mouth "I would contend that there are some things that almost all weaknesses share, as common traits, but perhaps that is an advanced lesson."

        red @closedbrow talking2mouth "Advanced lesson... oh, so can I take the advancement exam?"

        koga @talkingmouth "Yes. Passing it will grant you the ability to teach your Pokémon the move Venoshock. I am sure I need not tell you that its power doubles when used on a poisoned foe."

        red @talking2mouth "No, Sir, you don't. I'm ready to take the exam now."

        $ AddEvent("Instructor Koga", 4)
    else:
        red uniform @talking2mouth "Koga, I've been doing my research into you and your Pokémon since the last time we battled, and I'm ready to try again."

    koga @talkingmouth "Good. Now, pick your Pokémon. [bluecolor]I recommend not picking a Poison-type for this fight.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    koga @talking2mouth "Now your lesson truly begins."
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("koga", TrainerType.Enemy, [
        Pokemon("Bronzor", level=31, moves=[GetMove("Extrasensory"), GetMove("Safeguard"), GetMove("Hypnosis"), GetMove("Gyro Ball")], ability="Levitate", item="Sitrus Berry")
    ])

    call Battle([trainer1, trainer2], uniforms=[True, False]) from _call_Battle_101
    $ battlehistory["Instructor Koga3"]  = _return

    show koga with dis

    if (WonBattle("Instructor Koga3")):
        $ AddEvent("Instructor Koga", 4.1)

        koga @talkingmouth "Another victory... you ought be proud."

        koga @talkingmouth "You have now beaten a Pokémon that is strong against the Poison-type, one that struggles against the Poison-type, and, of course, a Poison-type itself!"
        koga @closedbrow talking2mouth "As you have mastered the basics, future battles in this class will utilize three Pokémon, instead of merely one."

        $ passedclass = True
        jump aftertutorintropoison
    
    else:
        koga @closedbrow talking2mouth "Leaves in autumn..."
        koga @talking2mouth "A ninja chooses his battles when certain of victory."

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide koga with dis

elif (FindGenericClassScene(True)):#generic scene
    $ renpy.call(FindGenericClassScene())
    hide koga with dis
else:# _really_ generic scene
    show koga with dis
    koga @talkingmouth "Are you prepared to deepen your mastery of the tricks of Poison-type Pokémon?"
    hide koga with dis
    show kogabg with dis
    koga "The key to a Pokémon's power is versatility. From four moves, you must develop a dozen techniques! Now..."
    narrator "Class proceeds without incident."

return

label movetutorpoison:
show koga with dis
koga @talkingmouth "A Poison-type Pokémon's arsenal is not complete without powerful techniques. Which would you like to learn?"
koga @talkingmouth "I can teach Bad Breath, which will attempt to badly poison, paralyze, and confuse a foe, if the prior status cannot be applied."
if (HasEvent("Instructor Koga", 4.1)):
    koga @happy "Follow it up with a lethal Venoshock! This move doubles in power on a poisoned foe."

label aftertutorintropoison:
$ taughtmove = None

menu:
    ">Learn Bad Breath":
        $ taughtmove = "Bad Breath"
    ">Learn Venoshock" if (HasEvent("Instructor Koga", 4.1)):
        $ taughtmove = "Venoshock"
    "Nevermind":
        koga @surprised "Indecisiveness must be cut out of the winning trainer."

        if (passedclass):
            $ renpy.pop_call()
            jump aftertutoring
        else:
            jump afterpoisonsetup
python:
    hidebattleui = True
    renpy.transition(dissolve)
    newindex = renpy.call_screen("switch", MakeRed())
    if (newindex != "back"):
        newmon = playerparty[newindex]
    hidebattleui=False
if (newindex == "back"):
        koga @surprised "Indecisiveness must be cut out of the winning trainer."
elif (MonCanLearn(newmon, taughtmove)):
    $ newmon.LearnNewMove([(1, taughtmove)])
    if (taughtmove in newmon.GetMoveNames()):
        jump endclass
else:
    koga @closedbrow talking2mouth "Teaching that Pokémon [taughtmove] is beyond even my abilities."

jump aftertutorintropoison

label itemcraftpoison:
show koga with dis

koga @talkingmouth "The ninjas of the Ransei Period developed many items to bolster their techniques. I impart this knowledge unto you now, in hopes you will never need use them on another man."
koga @closedbrow talking2mouth "The Poison Barb inflicts lethal poison that renders a victim comatose within seconds. However, for a Pokémon, it boosts their Poison-type moves' power by 10%%."

menu:    
    ">Craft Poison Barb" if (HasEvent("Instructor Koga", 3.1)):
        $ GetItem("Poison Barb", 1, "You tease a Mareanie for an hour straight until it gets mad enough at you to spit out a poisonous barb, which you quickly grab with protective gloves.")
        jump endclasscraft
    "Nevermind":
        koga @talkingmouth "Acceptable. Choose carefully whom you entrust with this knowledge..."
        jump afterpoisonsetup
