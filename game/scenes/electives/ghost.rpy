label ghostelective:

$ renpy.transition(dissolve)
show screen currentdate

scene map
show blank2:
    alpha 0.8

show classroom with dis
show ghostclass:
    alpha 0.0 xalign 0.5 yalign 1.0
    ease 0.5 alpha 1.0
show dragglow:
    alpha 0.75 xalign 0.5 yalign 1.0
    block:
        ease 2.25 alpha 0.2
        ease 1.8 alpha 0.7
        repeat

$ location = "ghost"
$ passedclass = False

############################################################################################################################################################################################################################
#### 13. GHOST       #######################################################################################################################################################################################################
############################################################################################################################################################################################################################
$ renpy.pause(1.0, hard=True)

call sabrinaevent from _call_sabrinaevent
call ethanevent from _call_ethanevent_8
call gardeniaevent from _call_gardeniaevent

label afterghostsetup:

if (HasEvent("Instructrice Fantina", 2.1)):
    menu:
        "{b}>General Studies{/b}":
            pass

        ">Ask for move tutoring":
            jump movetutorghost

        ">Craft items" if (HasEvent("Instructrice Fantina", 3.1)):
            jump itemcraftghost

if (not HasEvent("Instructrice Fantina", 1)): #first class
    $ AddEvent("Instructrice Fantina", 1)
    $ renpy.pause(1.0, hard=True)

    show hilbert uniform at rightside with dis

    ethan sad uniform "Oh, man... I forgot that Herschel was in this class."
    red uniform "It'll be fine. Let's sit over here. Faaaaar away." 

    hide hilbert at rightside with dis

    pause 1.0

    show fantina happy2:
        xpos 900 yalign 1.0 alpha 0.0
        parallel:
            ease 1.0 xpos 700
            pause 0.25
            ease 1.0 xpos 840
            pause 0.25
            ease 1.0 xpos 720
        parallel:
            ease 0.5 alpha 1.0

    fantina "{i}Bonjour{/i}, my students!{w=0.5} How is everybody?"

    show fantina norm:
        ease 0.5 xpos 720 alpha 1.0

    ethan happy "Hey, she sounds like Calem!"

    fantina "Calem? Oh, the lovely boy from home country I met in the hall. {i}Oui,{/i} you are much astute!"
    $ BecomeNamed("Instructrice Fantina")
    fantina norm2 "I am Fantina, and I am your teacher for {color=#0048ff}Ghost class!{/color}"

    show fantina:
        xpos 720
        ease 0.5 xpos 780

    fantina happy2 "I am also new to country, so I hope to improve knowledge of local language in this class as you improve knowledge of ghosts!"

    show fantina norm2:
        xpos 780

    fantina "I came to country because I have heard about its Pokémon and unique contests."

    show fantina:
        xpos 780
        ease 0.5 xpos 700

    fantina happy2 "And much to my delight, {i}c'était magnifique!{/i}{w=0.5} They are unlike anything I have seen!"

    show fantina:
        xpos 700

    fantina norm2 "It is quite amazing how many things we have not experienced and might never experience in the world, {i}non?{/i} "
    fantina happy2 "{i}C'est la vie{/i}, but you are all still so young.{w=0.5} You must not yet realize how big the world truly is."

    show fantina:
        alpha 1.0
        ease 0.5 alpha 0.0

    show fantinabg:
        alpha 0.0 yalign 1.0 xalign 0.5
        pause 0.5
        ease 0.5 alpha 1.0

    ethan "Tell me about it.{w=0.5} I wouldn't want to know how I'd turn out if I spent my entire life cooped up in New Bark Town."

    fantina "Oh, pardon. I did not mean to make mood sad."
    fantina "But the fragility of humanity is quite interesting, {i}n'est-ce pas?{/i} "

    show hilbert uniform at rightside with dis

    pause 1.0

    fantina "{i}Oui, jeune homme!{/i}{w=0.5}?"

    hilbert "I've read that humans can become Ghost types on death. That death isn't the..."
    hilbert sad "...Isn't the end. Is that true, or just another fairytale?"

    show gardenia surprisedbrow frownmouth uniform:
        xpos 0.25 ypos 2.0
        ease 0.2 ypos 1.0

    gardenia "Wh-what?! Ghost types can be {i}humans?!{/i} Aggggh, that makes them even creepier!"

    fantina "{i}Très bien!{/i}"

    show hilbert surprisedbrow frownmouth with dis
    fantina "{i}Oui{/i}, it is accepted among many Ghost experts and scientists that human spirits are linked to the birth of some Pokémon, like Yamask and Drifloon."

    gardenia sad "Oh no..."

    show gardenia:
        ypos 1.0 xpos 0.25 rotate 0
        ease 2.0 ypos 2.0 rotate -45

    hilbert "It is?"

    hide sabrina
    hide gardenia

    fantina "Of course! Why, there are many cases of Yamask reacting to objects and images that relate to their former human selves."
    fantina "This supports theory that they retain memories of themselves when they were still human."
    fantina "{i}En fait{/i}, I have seen cases where Yamask even possess the body of a human to live their lives as humans again!"

    if ("Sabrina" in GetStudents()):
        show sabrina uniform at leftside with dis

        pause 1.0

        sabrina "There's an opposing view, though."

    elif ("Gardenia" in GetStudents()):
        show gardenia sadbrow uniform at leftside with dis

        pause 1.0

        gardenia @talkingmouth "Is that, like, totally true, though? I heard there were some other theories."

    fantina "{i}Oui, oui.{/i} Some scientists are of the belief that ghosts are not re-incarnated humans but, ah... how do you say..."
    fantina "'Effects.' The death of a being causes another being to come to life. A new being with traits of the old... but {i}not{/i} the old, if you will."

    hilbert sad "...Yeah. That makes sense. Once someone's gone, they're gone."

    hide hilbert
    hide sabrina
    hide gardenia
    with dis

    pause 1.0

    fantina "Now, I am much appreciating the class participation! Let us move on to main body of lecture, {i}non?{/i}"
    fantina "...Now, continuing with our lecture, I require a volunteer to become human spirit for the class."
    fantina "Ohohohoho! {i}Je plaisante!{/i} A joke!"

    narrator "Fantina continues to lecture. Despite her airy nature, she seems very knowledgeable."

    fantina "Oh, heavens, what is this?{w=0.5} Look at the time!"
    fantina "{i}Au revoir{/i}, students!{w=0.5} Be certain to check the syllabus for required readings!"

    hide fantina
elif (not HasEvent("Instructrice Fantina", 2.1) and classstats["Ghost"] >= 10):#Deathless
    show fantina with dis
    if (not HasEvent("Instructrice Fantina", 2)):
        $ renpy.pause(1.0, hard=True)

        fantina happy @happy2 "{size=40}Ohohohoho!~{/size}"

        red uniform @surprised "Geez! A little warning, please?"

        fantina norm @norm2 "Ah, but, {i}mon chéri!{/i} I was just so revelled by your progress in the class, it thrilled me!"

        fantina @happy "When the spirit of the show grabs you, must you not entertain it?"

        pause 2.0

        red @confusedeyebrows talking2mouth "I have no idea."

        fantina @happy2 "Then that is why you are here, no?"

        red @talkingmouth "...{i}Non?{/i}"

        fantina @sad2 "Oh, please, please. If I am to improve language, I must ask that you speak Japanese only."
        fantina @happy2 "Besides, besides, you have clearly said the wrong word! You meant '{i}oui!{/i}'"

        red @happy "Okay. So... I'm here to learn how to entertain the spirit of the show? And that will make me better at battling with Ghost-types?"

        fantina @surprised2 "You are much acute! Yes, that it is exact."

        red @closedbrow talking2mouth "Okay... so, that being the case, then... what do shows and ghosts have in common?"

        fantina @happy2 "Have you ever heard the phrase, in Japanese, I believe it is... {i}the show must go on?{/i}"

        red @happy "Oh, yeah! Like, no matter how bad things get, the actors need to figure out a way to keep things moving."

        fantina @norm2 "{i}Oui, oui.{/i} And that is the specialty of the Ghost-type, too. If we are to believe common scientific theory, they are echoes of human and Pokémon soul!"
        fantina @happy2 "Is there performer better at making 'the show must go on'? I think not!"

        red @closedbrow talking2mouth "So... what does that mean for battle?"

        fantina @surprised2 "All ghosts have a... how do you say... {i}deathless{/i} nature."
        fantina @happy2 "With proper trainage, of which I am provider, you can let them use the technique Deathless in battle!"

        red @closedbrow talking2mouth "Hm. Sounds edgy. I'm not sure what that does...?"

        fantina @surprised2 "Ah, perhaps it is a Kalos thing?"
        fantina @happy2 "In home country, it is common technique that prevent Ghost-type Pokémon from fainting for a turn!" 
        fantina @norm2 "Further, if they are to take mortal blow, they will instead recover half their health."

        red @surprised "That seems overpowered!"

        fantina @happy2 "Ah-ha!~ Perhaps so. But it will fail if you use it too often, ah, in a row."

        red @closedbrow talking2mouth "Seems like it'd still be really good. But I guess you wouldn't teach a bad move, huh?"

        fantina "{i}Non.{/i}"

        fantina @happy2 "Now, are you ready to begin the show? It will be one-one battle."

        red @happy "I'm more than ready, Ma'am!"

        $ AddEvent("Instructrice Fantina", 2)
    else:
        red uniform @talking2mouth "Fantina, I've brushed up on the script since last time, and I'm ready for an encore."

    fantina @happy2 "Then pick the Pokémon you wish to put in the starring role! {color=#0048ff}Top billing is given to the Ghost-type, {i}bien sur{/i}.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    fantina @happy2 "Let the curtain rise!"
    $ hidebattleui=False
    $ mustswitch = False
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("fantina", TrainerType.Enemy, [
        Pokemon(102, level=11, moves=[GetMove("Absorb"), GetMove("Hypnosis"), GetMove("Reflect"), GetMove("Leech Seed")], ability="Chlorophyll")
    ])

    call Battle([trainer1, trainer2], customexpressions=["red uniform", "red uniform angrybrow happymouth", "fantina norm", "fantina happy2"], reanchor=[False, True]) from _call_Battle_32
    $ battlehistory["Instructrice Fantina1"]  = _return

    show fantina with dis

    if (WonBattle("Instructrice Fantina1")):
        $ AddEvent("Instructrice Fantina", 2.1)

        fantina @happy2 "A resplendent performance! I see a future for you in contests, {i}oui!{/i}"

        red uniform @happy "Well, my Mom always did say I was a drama queen!"

        $ passedclass = True

        jump aftertutorintroghost
    
    else:
        fantina @sad2 "Ah... a letdown."
        fantina @happy "But no matter. We will not let this dampen our spirits, no? Come back for an encore, after you have rehearsed!"

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide fantina with dis
elif (not HasEvent("Instructrice Fantina", 3.1) and classstats["Ghost"] >= 20):#Spell Tag
    show fantina with dis
    if (not HasEvent("Instructrice Fantina", 3)):
        $ renpy.pause(1.0, hard=True)

        fantina happy @happy2 "{size=40}Ohohohoho!~{/size}"

        red uniform @surprised "Uh, hi! What is it, Instructor? The spirit of the show again?"

        fantina norm @happy2 "{i}Non{/i}, not this time. I simply wish to tell you that you are doing well in class! {i}C'est un compliment!{/i}"

        red @confused "So, the... 'Ohohohoho' is...?"

        fantina @happy2 "Excitement to see that my {i}précieux{/i} student is doing so well."

        red @happy "Well... thanks, then. Guess I can't be too startled by excitement."

        fantina @norm4 "Tell me, {i}Monsieur{/i} [last_name]. Are you familiar with the item, the... how do you say... 'Spell Tag'?"

        red @closedbrow talking2mouth "Yeah."

        red @talkingmouth "They raise the power of Ghost-type moves by 20%%, right?"

        fantina @happy2 "{i}Oui,{/i} in some region. But in Kobukan, it is seeming to be closer to 10%%."

        red @surprisedeyebrows talking2mouth "Oh. Well, that's fine, too."

        fantina @norm2 "If you take the exam of advancement, and are passing, of course, then I will show you how to make them. They will give your ghosts a, ah, spooky boost!"

        red @happy "Great! I'm ready now."

        $ AddEvent("Instructrice Fantina", 3)
    else:
        red uniform @talking2mouth "Fantina, I've brushed up on the script since last time, and I'm ready for an encore."

    fantina @happy2 "Then pick the Pokémon you wish to put in the starring role! {color=#0048ff}My lead actor will be of the Ghost-type, {i}bien sur{/i}.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    fantina @happy2 "{i}Allons-y{/i}!"
    $ hidebattleui=False
    $ mustswitch = False
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("fantina", TrainerType.Enemy, [
        Pokemon("Misdreavus", level=21, moves=[GetMove("Confuse Ray"), GetMove("Astonish"), GetMove("Confusion"), GetMove("Hex")], ability="Levitate", item="Oran Berry")
    ])

    call Battle([trainer1, trainer2], customexpressions=["red uniform", "red uniform angrybrow happymouth", "fantina norm", "fantina happy2"], reanchor=[False, True]) from _call_Battle_90
    $ battlehistory["Instructrice Fantina2"]  = _return

    show fantina with dis

    if (WonBattle("Instructrice Fantina2")):
        $ AddEvent("Instructrice Fantina", 3.1)

        fantina @happy2 "A resplendent performance! I hope I will see you in the Coordinator's club, no?"

        red uniform @happy "Well... I'm pretty busy, but, y'know, I might drop by..."

        $ GetItem("Spell Tag", 1, "Fantina gives you a Spell Tag. When you hold it up to your ear, you hear quiet whispers...")

        $ renpy.pop_call()
        jump aftertutoring
    
    else:
        fantina @sad2 "Hmmm... most unfortunate."
        fantina @happy "But keep your spirits upward! There is no need to grieve while your candle still burns!"

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide fantina with dis
elif (not HasEvent("Instructrice Fantina", 4.1) and classstats["Ghost"] >= 30):#Shadow Punch
    show fantina with dis
    if (not HasEvent("Instructrice Fantina", 4)):
        $ renpy.pause(1.0, hard=True)

        fantina "[first_name], I am providing the warning about my laughter that you ask for."

        red @confused "Huh?"

        show fantina with vpunch

        fantina happy @happy2 "{size=40}Ohohohoho!~{/size}"

        red @surprised "Oh, right, that's what you meant!"

        fantina @norm2 "I am much obliged to see your progress, [first_name]! You are having a deep understanding of the Ghost-type Pokémon!"

        red @happy "Yeah, thanks! I think I'm picking up a few things."

        fantina @norm2 "{i}S'il vous plaît dites-moi.{/i} What do you think is weakness of Ghost-type?"

        red @closedbrow talking2mouth "Hm... well, they're not very physically bulky. Most of them, I mean. A few have high defenses, but they often have low health."

        red @confused "Maybe because they're already kinda so strong in the 'death force', they don't have a lot of 'life force'?"

        fantina @sad2 "{i}Oui,{/i} perhaps so."

        red @talkingmouth "I've noticed a lot of them don't have very strong physical moves, either. There aren't a ton of Ghost-type physical moves that I know of."

        fantina @norm2 "Oui, many, many, many are species-unique. Few are commonly known by many Ghost Pokémon, or many Pokémon in general."

        red @talkingmouth "Hm... there's Lick, Shadow Claw... Shadow Punch..."

        fantina @happy2 "Speaking of, I wish to give you advancement exam."

        red @happy "Really? Already? Sweet!"

        pause 0.5

        red @confused "You said 'speaking of.' Does that mean...?"

        fantina @norm2 "{i}Oui.{/i} For passage of this exam, I will teach your Pokémon the move 'Shadow Punch.' If they can learn it, of course."

        red @happy "Alright! That'll be useful to learn. I'm ready to take the exam now!"

        $ AddEvent("Instructrice Fantina", 4)
    else:
        red uniform @talking2mouth "Fantina, I've brushed up on the script since last time, and I'm ready for an encore."

    fantina @happy2 "Then pick the Pokémon you wish to put in the starring role! {color=#0048ff}You may find the spotlight burns away a Ghost-type, this time.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    fantina @happy2 "Take the stage, and show me your learning!"
    $ hidebattleui=False
    $ mustswitch = False
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("fantina", TrainerType.Enemy, [
        Pokemon("Umbreon", level=31, moves=[GetMove("Moonlight"), GetMove("Confuse Ray"), GetMove("Assurance"), GetMove("Sand Attack")], ability="Synchronize", item="Sitrus Berry")
    ])

    call Battle([trainer1, trainer2], customexpressions=["red uniform", "red uniform angrybrow happymouth", "fantina norm", "fantina happy2"], reanchor=[False, True]) from _call_Battle_91
    $ battlehistory["Instructrice Fantina3"]  = _return

    show fantina with dis

    if (WonBattle("Instructrice Fantina3")):
        $ AddEvent("Instructrice Fantina", 4.1)

        fantina @happy2 "{i}Fantastique!{/i} By my recall, that means you have beaten {i}un{/i} Ghost-type, one Pokémon strong against the Ghost-type, and one Pokémon weak to Ghosts, no?"

        red uniform @happy "{i}Oui.{/i}"

        fantina @norm2 "Splendid. Future exams, I will be using {i}trois{/i} Pokémon. But for now, you have done very well."

        $ passedclass = True

        jump aftertutorintroghost
    
    else:
        fantina @sad2 "Hmmm... Your performance is fallen quite flat."
        fantina @happy "Come again once the spirit moves you--and let us finish your story on a high note!"

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide fantina with dis

elif (FindGenericClassScene(True)):#generic scene
    $ renpy.call(FindGenericClassScene())
    hide fantina with dis
else:# _really_ generic scene
    show fantina with dis
    fantina "Ohohohoho! Did you have eyes upon the contest that aired on TV yesterday?"
    hide fantina with dis
    show fantinabg with dis
    fantina "C'était magnifique! The winner used Ghost types to extraordinary effect, non? Let's discuss that..."
    narrator "Class proceeds without incident."

return

label movetutorghost:
show fantina with dis
fantina @norm2 "Ohohohoho! You would like to study the ghostly script, for the benefit of battle? Very well!"
fantina @norm2 "I can teach Deathless, a move that prevents your Ghost-type from taking a mortal blow for a turn, and heals them if they would!"
if (HasEvent("Instructrice Fantina", 4.1)):
    fantina @happy2 "Or, for example, I could teach you the move, ah, Shadow Punch. It is a physical move that is also a Ghost move that does not miss!"

label aftertutorintroghost:
$ taughtmove = None

menu:
    ">Learn Deathless":
        $ taughtmove = "Deathless"
    ">Learn Shadow Punch" if (HasEvent("Instructrice Fantina", 4.1)):
        $ taughtmove = "Shadow Punch"
    "Nevermind":
        fantina @surprised2 "Oh? A plot twist?"

        if (passedclass):
            $ renpy.pop_call()
            jump aftertutoring
        else:
            jump afterghostsetup
python:
    hidebattleui = True
    renpy.transition(dissolve)
    newindex = renpy.call_screen("switch", MakeRed())
    if (newindex != "back"):
        newmon = playerparty[newindex]
    hidebattleui=False
if (newindex == "back"):
        fantina @surprised2 "Oh? A plot twist?"
elif (MonCanLearn(newmon, taughtmove)):
    $ newmon.LearnNewMove([(1, taughtmove)])
    if (taughtmove in newmon.GetMoveNames()):
        jump endclass
else:
    fantina @happy2 "Ohohoho! Not every actor can play every part, I am afraid..."

jump aftertutorintroghost

label itemcraftghost:
show fantina with dis

fantina @happy2 "An actor is nothing without their wardrobe, is it not true? Let us see what you might have interest in making in this class!"
fantina @norm2 "Oho!~ A Spell Tag is quite effective, no? Simple paper, but it boosts the power of Ghost-type moves by 10%%!"

menu:    
    ">Craft Spell Tag" if (HasEvent("Instructrice Fantina", 3.1)):
        $ GetItem("Spell Tag", 1, "You chant ominous latin words over a piece of paper, creating a Spell Tag. You feel a bit silly.")
        jump endclasscraft
    "Nevermind":
        fantina @norm4 "Oh, are you not wanting to take up a prop? Fine, fine."
        jump afterghostsetup
