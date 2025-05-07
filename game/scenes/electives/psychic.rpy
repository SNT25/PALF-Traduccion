label psychicelective:

$ renpy.transition(dissolve)
show screen currentdate

scene map
show blank2:
    alpha 0.8

show classroom with dis

show psychtype with dis:
    xalign 0.5 yalign 1.0

############################################################################################################################################################################################################################
#### 13. POISON    #######################################################################################################################################################################################################
############################################################################################################################################################################################################################
$ renpy.pause(1.0, hard=True)

$ location  = "psychic"
$ passedclass = False

call sabrinaevent from _call_sabrinaevent_1
call rosaevent from _call_rosaevent_2
call ethanevent from _call_ethanevent_14
call tiaevent from _call_tiaevent_1

if (IsAfter(3, 5, 2004) and IsBefore(3, 9, 2004) and rescuedwill and "BackInClass" not in persondex["Instructor Will"]["Events"]):
    $ AddEvent("Instructor Will", "BackInClass")
    show will with dis

    will @happy "Welcome back to class, everyone!"

    $ PlaySound("crowd_cheer.ogg")

    pause 2.0

    will @happy "Yes, I'm quite happy to be back, too! It's all thanks to the effort of our disciplinary committee, and [first_name] helping them."
    will @closedbrow talkingmouth "I was in quite a pickle, too! My wondrous psychic powers had been overwhelmed by a brute of evil bearing and wicked design!"
    will @happy "So, please, instead of quivering in your boots before a force that could overpower even The Great Will, take this as a sign that even teachers like myself can always improve!"

    if (not rescuedsabrina or not rescuedtia):
        will @sad "Now... it {i}is{/i} true that there are still students of this class who have not yet been returned to safety."
        will @talkingmouth "Be reassured that I'm working closely with the Disciplinary Committee to get them back. Of course... assistance cannot be solicited, but is appreciated."

        pause 1.0

        will @happy "But, please, don't worry about that! Everything will be handled shortly."

    will @talkingmouth "Right now, though, I'd just like to commend everyone for continuing your studies so diligently in my absence. I'm truly proud of all of you."
    will @talkingmouth "However! Diligence alone will not raise you all into the fine psychic prodigies I know you are capable of being!" 
    will @happy "Indeed, only my own illustrious instruction can do that! So, without further ado, let's begin the lesson!"

    hide will with dis

label afterpsychicsetup:

if (HasEvent("Instructor Will", 2.1)):
    menu:
        "{b}>General Studies{/b}":
            pass

        ">Ask for move tutoring":
            jump movetutorpsychic

        ">Craft items" if (HasEvent("Instructor Will", 3.1)):
            jump itemcraftpsychic

if (not HasEvent("Instructor Will", 1)): #first class
    $ AddEvent("Instructor Will", 1)
    $ renpy.pause(1.0, hard=True)

    show will:
        xpos 800 alpha 0.0
        ease 0.7 xpos 750 alpha 1.0

    will @happy "Salutations, my students! Welcome to your {color=#0048ff}Psychic class.{/color}"

    if (not (calDate.month == 4 and calDate.day == 5 and calDate.year == 2004)):
        will @surprised "New students? Wait, don't tell me... Ethan and [first_name]!"

    if (not IsBefore(26, 4, 2004) or (calDate.day == 26 and calDate.month == 4 and calDate.year == 2004 and timeOfDay == "Evening")):
        red @talkingmouth "Um... yeah, Instructor Will. We've met."

        will @surprised "So we have! Then let me introduce myself to Ethan here."

    $ BecomeNamed("Instructor Will")
    will @happy "Allow me to introduce myself.{w=0.5} I am the Great Will, your teacher!"

    hide will with dis

    pause 1.0

    show willbg with dis

    will "For this class, we will not only be learning about Psychic Pokémon. We will also be training your innate psychic powers!"

    ethan uniform "Our.{w=0.25}.{w=0.25}.{w=0.25} psychic powers?"
    ethan closedbrow talking2mouth "I think my Dad got me meds for those..."

    will @surprised "Unbeknownst to most, every living being has psychic potential."
    will @talkingmouth "The power is just hidden away.{w=0.5} It will be my job to bring it out of you, and to increase your natural focus."
    will @talking2mouth "If your focus is too weak, your telepathic bonds with your Pokémon will be easily severed."
    will @happy "But if you strengthen those bonds, your Pokémon will become undefeatable! You will act as limbs of a single mind!"
    will @talking2mouth "Hm... I believe I sense suspicion."
    will @talkingmouth "But you may rest assured of the Great Will's qualifications! As you can see, I am quite the capable Esper."

    show book1 as book_A:
        subpixel True
        alpha 0.0 zoom 0.05 xpos 900 ypos 460
        parallel:
            ease 0.5 alpha 1.0
        parallel:
            ease 0.4 ypos 450
            ease 0.4 ypos 460
            repeat
    show book1 as book_B:
        subpixel True
        alpha 0.0 zoom 0.04 xpos 980 ypos 450 rotate 12
        parallel:
            pause 0.25
            ease 0.5 alpha 1.0
        parallel:
            ease 0.3 ypos 440
            ease 0.3 ypos 450
            repeat
    show book2:
        subpixel True
        alpha 0.0 zoom 0.04 xpos 920 ypos 470 rotate 12
        parallel:
            ease 0.75 alpha 1.0
        parallel:
            ease 0.5 ypos 480
            ease 0.5 ypos 470
            repeat
    show calc:
        subpixel True
        alpha 0.0 zoom 0.05 xpos 990 ypos 470 rotate 12
        parallel:
            pause 0.2
            ease 0.4 alpha 1.0
        parallel:
            ease 0.4 ypos 460
            ease 0.4 ypos 470
            repeat

    $ renpy.pause(1.5, hard=True)

    ethan happy "Wow, that's really cool.{w=0.5} And a bit terrifying."

    $ PlaySound("Scattered Applause.ogg")

    show bianca happy uniform at rightside with dis

    bianca "Incredible, Instructor Will! Not even my little Moony can do that!"

    will "Thank you, thank you!"

    hide bianca at rightside with dis

    show book1 as book_A:
        ypos 460 alpha 1.0
        ease 0.3 ypos 490 alpha 0.0
    show book1 as book_B:
        ypos 450 alpha 1.0
        pause 0.15
        ease 0.3 ypos 490 alpha 0.0
    show book2:
        ypos 470 alpha 1.0
        pause 0.1
        ease 0.3 ypos 490 alpha 0.0
    show calc:
        ypos 470 alpha 1.0
        pause 0.2
        ease 0.3 ypos 490 alpha 0.0

    will "Telekinesis is just one among dozens of psychic powers. Aren't you curious to see how your own develop?"
    will @happy "One step at a time, children! And the very first is to practice meditation.{w=0.5} To meditate efficiently, you must have solid concentration."
    will @talkingmouth "In order to have solid concentration, you must rid your mind of distractions."
    will @talking2mouth "Distractions come in many shapes and forms, but the most pernicious are..."
    
    hide book1 as book_A
    hide book1 as book_B
    hide book2
    hide calc

    ethan "This all sounds like a load of baloney to me."
    red @angrybrow talking2mouth "Dude, he just lifted a bunch of books into the air in front of us."
    ethan "Eh, he's probably got an Espeon hidden under that desk."

    will "...Now, for our first exercise, I want you all to close your eyes and concentrate all your thoughts on one thing.{w=0.5} It doesn't matter what, as long as it's the only thing you're thinking about."
    will "This way, you can attune yourselves to your natural focus and bring forth your latent powers!"

    show blank2 as blank_A with transeye

    window hide
    pause 1.5

    $ PlaySound("Whoosh.ogg")
    pause 1.0

    redmind "Eh? What was that...?"

    window hide

    pause 1.0

    hide blank2 as blank_A with transeye2

    will "...Right, that's enough of that for now. Open your eyes, students!"
    will @happy "Are you all feeling enlightened? I'm sure."
    will "Let's move on to some basic psionic theory, shall we?"

    narrator "In between the various mental exercises, you manage to learn more about Psychic-types."

    will @surprised "Oh, time's up already?"
    will "Very well--we'll pick up from here next time! I assure you, we're only getting started!"

    red @talkingmouth "This has to be one of the weirdest classes I've ever been in."
    ethan happy "Sure, but at least it's not boring!"

    hide will
elif (not HasEvent("Instructor Will", 2.1) and classstats["Psychic"] >= 10):#Clear Mind
    show will with dis
    if (not HasEvent("Instructor Will", 2)):
        $ renpy.pause(1.0, hard=True)

        narrator "Psychic class is in full swing, with Instructor Will enthusiastically extolling the virtues of Psychic-types, when, suddenly..."

        will @talkingmouth "[first_name]! I require a volunteer for a demonstration."

        red uniform @surprised "Huh? A demonstration?"

        will @happy "Yes, indeed! By reading your mundane euthymic brainwaves, I am certain that you think you are ready for the advancement exam!"

        redmind @confusedeyebrows frownmouth "Huh? I wasn't thinking that at all. And now I feel kinda insulted."

        will @surprised "And now you feel insulted!"

        pause 1.0

        red @talking2mouth "Your powers are incomparable, Instructor."

        will @happy "So say all to the Great Will!"

        will @angrybrow happymouth "But I do not ask for your assistance in this demonstration for naught! I will bestow upon you the ultimate Psychic technique--{i}Clear Mind!{/i}"

        red @talkingmouth "I mean, you're the instructor, so you can just {i}make{/i} me help, but sure, I'm down. What does Clear Mind do?"

        will @closedbrow talking2mouth "You may target any Pokémon on the field with it--thus removing their status conditions, and resetting their stat changes!"

        will @happy "A perfectly balanced tool for offensive or defensive use!"

        red @closedbrow talking2mouth "Okay, that's pretty good, yeah."
        red @talkingmouth "So this demonstration is..."

        will @happy "I knew you would ask! It is a one-on-one battle."

        red @happy "Alright. Let's do this, then!"

        $ AddEvent("Instructor Will", 2)
    else:
        red uniform @talking2mouth "Will, I've done some more training. I'm ready to battle you properly, now. And I'll win this time."

    will @happy "Hahaha! I foresaw this battle! Send out your Pokémon, and roll the dice of fate! {color=#0048ff}A Psychic-type will give you the best odds here!{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    will @happy "May the odds be ever in your favor!"
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("will", TrainerType.Enemy, [
        Pokemon(453, level=11, moves=[GetMove("Poison Sting"), GetMove("Mud-Slap"), GetMove("Astonish"), GetMove("Taunt")], ability="Anticipation")
    ])

    call Battle([trainer1, trainer2], uniforms=[True, False]) from _call_Battle_102
    $ battlehistory["Instructor Will1"] = _return

    show will with dis

    if (WonBattle("Instructor Will1")):
        $ AddEvent("Instructor Will", 2.1)

        will @happy "Hahaha! Exactly as I predicted!"

        $ passedclass = True
        jump aftertutorintropsychic
    
    else:
        will @happy "Hahaha! Exactly as I predicted!"
        will @talkingmouth "Still, I foresee that you will come back again... and truly show your strength then!"

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide will with dis
elif (not HasEvent("Instructor Will", 3.1) and classstats["Psychic"] >= 20):#Twisted Spoon
    show will with dis
    if (not HasEvent("Instructor Will", 3)):
        $ renpy.pause(1.0, hard=True)

        will @happy "[first_name]! How are your psychic powers developing?"

        red uniform @surprised "I am thankful every day, Instructor Will, that I don't need to have psychic powers to pass this class' exams."

        pause 1.0

        will poutmouth @talking2mouth "Well... yes, that's true."

        pause 2.0

        will -poutmouth @closedbrow talking2mouth "But it doesn't {i}hurt.{/i}"

        red @talkingmouth "Hm... well, I think I'm getting something, actually..."

        will @surprised "Oh? Are you?"
        will @happy "Are you really? Fantastic! We might make an Esper out of you yet!"

        pause 1.0

        red @closedbrow talking2mouth "You're thinking that you want to give me this class' advancement exam, right?"

        pause 1.0

        will @poutmouth closedbrow "Eh, fine."

        will @happy "Pass this one, and I will demonstrate the true scope of my psychic powers by creating the ultimate tool of the Esper--the Twisted Spoon! This item boosts the power of your Psychic-type moves by a tremendous 10%%!"

        red @talkingmouth "Can't wait to earn it. In fact, I don't need to. Let's battle!"

        $ AddEvent("Instructor Will", 3)
    else:
        red uniform @talking2mouth "Will, I've done some more training. I'm ready to battle you properly, now. And I'll win this time."

    will @happy "Hahaha! Let us see, then, whether your prediction bears fruit! {color=#0048ff}I will be using an illustrious Psychic-type for this bout!{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    will @happy "Go on, then--try to surprise me!"
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("will", TrainerType.Enemy, [
        Pokemon("Natu", level=21, moves=[GetMove("Night Shade"), GetMove("Confuse Ray"), GetMove("Peck"), GetMove("Psyshock")], ability="Magic Bounce", item="Oran Berry")
    ])

    call Battle([trainer1, trainer2], uniforms=[True, False]) from _call_Battle_103
    $ battlehistory["Instructor Will2"]  = _return

    show will with dis

    if (WonBattle("Instructor Will2")):
        $ AddEvent("Instructor Will", 3.1)

        will @happy "Hahaha! Exactly as I predicted!"

        $ GetItem("Twisted Spoon", 1, "Instructor Will produces a regular spoon and bends it before proudly presenting it to you. You're pretty sure he just bent it with his thumb.")

        $ renpy.pop_call()
        jump aftertutoring
    
    else:
        will @happy "Hahaha! An inevitable outcome, I'm afraid."
        will @talkingmouth "Still, I foresee hope in your future! You'll try again, won't you?"

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide will with dis
elif (not HasEvent("Instructor Will", 4.1) and classstats["Psychic"] >= 30):#Psybeam
    show will with dis
    if (not HasEvent("Instructor Will", 4)):
        $ renpy.pause(1.0, hard=True)

        will @talkingmouth "[first_name]! I hear your thoughts! And what you want is... a Psychic move that can deal damage?"

        pause 1.0

        red uniform @closedbrow talking2mouth "I... guess so? Like, in the abstract? Clear Mind is useful, but it can't damage."

        will @happy "Fantastic news for you, my Student! The Great Will has looked into the future, and sees a reality where that {i}is{/i} the case!"

        pause 1.0

        red @closedbrow talking2mouth "Do I just have to pass an advancement exam?"

        will @surprised "Oh? You may have something prescient about you, too! Yes, pass an advancement exam, and unlock the forbidden power of 'Psybeam!'"

        redmind @thinking "Forbidden power? It's not {i}that{/i} good a move."

        will @happy "Not only can it do damage, it can also confuse! Not even Psychic can do that!"

        red @happy "Fair enough. I'm ready to battle you for it, then."

        $ AddEvent("Instructor Will", 4)
    else:
        red uniform @talking2mouth "Will, I've done some more training. I'm ready to battle you properly, now. And I'll win this time."

    will @happy "I'm of a mind to test that prediction. {color=#0048ff}But if you use a Psychic-type, you're rolling against loaded dice!{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    will @happy "Let's see whom Lady Luck favors!"
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("will", TrainerType.Enemy, [
        Pokemon("Murkrow", level=31, moves=[GetMove("Taunt"), GetMove("Assurance"), GetMove("Night Shade"), GetMove("Wing Attack")], ability="Prankster", item="Sitrus Berry")
    ])

    call Battle([trainer1, trainer2], uniforms=[True, False]) from _call_Battle_104
    $ battlehistory["Instructor Will3"]  = _return

    show will with dis

    if (WonBattle("Instructor Will3")):
        $ AddEvent("Instructor Will", 4.1)

        will @happy "Hahaha! Exactly as I predicted!"
        will @talkingmouth "With this, you have beaten one Psychic-type, a Pokémon that's strong against Psychic types, and one that's weak to Psychic-types!"
        will @happy "In future lessons, then, I shall unveil even more of my awesome abilities, and use {i}three{/i} Pokémon at once! I do hope you're prepared in kind..."

        $ passedclass = True
        jump aftertutorintropsychic
    
    else:
        will @happy "Victory just wasn't in the cards!"
        will @talkingmouth "And yet I sense your determination. Surely you'll be back once more."

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide will with dis

elif (FindGenericClassScene(True)):#generic scene
    $ renpy.call(FindGenericClassScene())
    hide will with dis
else:# _really_ generic scene
    show will with dis
    will @happy "Salutations, students! Today, we will hone our psychic powers while learning about Psychic Pokémon!"
    will @talkingmouth "You're permitted to close your eyes for meditative purposes{w=0.5}{nw}"
    extend @angry "--but no falling asleep during the lectures!"
    hide will
    show willbg 
    with dis
    narrator "Class proceeds without incident."
return

label movetutorpsychic:
show will with dis
will @talkingmouth "You want the Great Will to teach your Pokémon a new Psychic-type move? Very well! I deign to do so!"
will @happy "Do you want to learn Clear Mind? This move will remove the status effects and stat changes of any Pokémon on the field!"
if (HasEvent("Instructor Will", 4.1)):
    will @angrybrow happymouth "Psybeam allows you to use your psychic powers offensively! Bring to bear the might of the telekinetic force!!"

label aftertutorintropsychic:
$ taughtmove = None

menu:
    ">Learn Clear Mind":
        $ taughtmove = "Clear Mind"
    ">Learn Psybeam" if (HasEvent("Instructor Will", 4.1)):
        $ taughtmove = "Psybeam"
    "Nevermind":
        will @surprised "Not yet ready to change your fate?"

        if (passedclass):
            $ renpy.pop_call()
            jump aftertutoring
        else:
            jump afterpsychicsetup
python:
    hidebattleui = True
    renpy.transition(dissolve)
    newindex = renpy.call_screen("switch", MakeRed())
    if (newindex != "back"):
        newmon = playerparty[newindex]
    hidebattleui=False
if (newindex == "back"):
        will @surprised "Not yet ready to change your fate?"
elif (MonCanLearn(newmon, taughtmove)):
    $ newmon.LearnNewMove([(1, taughtmove)])
    if (taughtmove in newmon.GetMoveNames()):
        jump endclass
else:
    will @happy "Hahaha! Not even the Great Will can teach that Pokémon [taughtmove]!"

jump aftertutorintropsychic

label itemcraftpsychic:
show will with dis

will @happy "A great Psychic often relies on physical props to demonstrate his Psychic powers to his captive audience! Why don't you see what I have in store?"
will @angrybrow happymouth "This Twisted Spoon is a splendid example. After bending it with naught but my mind, it will boost the power of all Psychic-type moves by 10%%!"

menu:    
    ">Craft Twisted Spoon" if (HasEvent("Instructor Will", 3.1)):
        $ GetItem("Twisted Spoon", 1, "You 'ooh' and 'aah' at Instructor Will's performance, until, after about an hour's worth of concentration, he produces a single Twisted Spoon for you. (You're pretty sure he bent it with his thumb.)")
        jump endclasscraft
    "Nevermind":
        will @surprised "I did not foresee this!"
        jump afterpsychicsetup
