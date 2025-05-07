label fightingelective:

$ renpy.transition(dissolve)
show screen currentdate

scene map
show blank2:
    alpha 0.8

show classroom with dis

show fighttype:
    alpha 0.0 xalign 0.5 yalign 1.0
    ease 0.5 alpha 1.0

$ location = "fighting"
$ passedclass = False

############################################################################################################################################################################################################################
#### 13. FIGHTING    #######################################################################################################################################################################################################
############################################################################################################################################################################################################################
$ renpy.pause(1.0, hard=True)

call wallyevent from _call_wallyevent
call beaevent from _call_beaevent
call ethanevent from _call_ethanevent_5

label afterfightingsetup:

if (HasEvent("Sensei Marshal", 2.1)):
    menu:
        "{b}>General Studies{/b}":
            pass

        ">Ask for move tutoring":
            jump movetutorfighting

        ">Craft items" if (HasEvent("Sensei Marshal", 3.1)):
            jump itemcraftfighting

if (not HasEvent("Sensei Marshal", 1)): #first class
    $ AddEvent("Sensei Marshal", 1)
    $ renpy.pause(1.0, hard=True)

    ethan uniform happy "I was looking forward to this class! Calem and May are both here, right?"

    show may uniform happy at leftside with dis
    show calem uniform at rightside with dis

    red uniform "Looks like it. On opposite sides of the classroom, though. I don't want to play favorites. We'll sit between 'em?"
    ethan -happy @talkingmouth "Sounds like a plan."

    hide may at leftside with dis
    hide calem at rightside with dis

    pause 2.5

    hide may
    hide calem

    $ PlaySound("ExitBuilding.ogg")

    stop music
    play music "Audio/Music/Kimono_Start.ogg" noloop
    queue music "Audio/Music/Kimono_Loop.ogg"

    show marshal surprised:
        alpha 0.0 xpos 1200 yalign 1.0
        ease 0.25 xpos 720 alpha 1.0

    show fightclass behind marshal:
        parallel:
            xalign 0.0
            ease 0.02 xpos -20
            ease 0.02 xpos 20
            ease 0.02 xpos 0
            repeat 2
        parallel:
            yalign 0.0
            ease 0.02 ypos -20
            ease 0.02 ypos 20
            ease 0.02 ypos 0
            repeat 2

    marshal "{size=44}{i}KIOTSUKE!!{/i} {/size}"

    $ PlaySound("Marshal Punches.ogg")
    
    show marshal:
        subpixel True
        xpos 720 yalign 1.0 alpha 1.0
        ease 0.1 xpos 600
        ease 0.2 xpos 800 yalign 1.2
        ease 0.1 xpos 740 yalign 1.0
        ease 0.1 xpos 600
        ease 0.1 xpos 740
        ease 0.1 xpos 600 yalign 1.2
        ease 0.2 xpos 800
        ease 0.1 xpos 670 yalign 1.0

    $ renpy.pause(1.0, hard=True)
    
    show marshal:
        xpos 670 yalign 1.0

    ethan "Wha--"

    hide fightclass

    marshal surprised "{i}TSUKI!{w=0.25} EMPI!{/i} "

    marshal -surprisedbrow -frownmouth -surprised @talkingmouth "Welcome to my {color=#0048ff}Fighting dojo!{/color} I am your sensei--"

    show woodA:
        alpha 0.0 xpos 960 ypos 900
        ease 0.7 ypos 600 alpha 1.0

    $ renpy.pause(1.5, hard=True)

    show marshal angry:
        xpos 670 yalign 1.0
        ease 0.15 xpos 730 yalign 1.8

    $ PlaySound("Wood Break.ogg")

    hide woodA

    show woodB:
        xpos 960 ypos 600 alpha 1.0 rotate 0
        parallel:
            ease 0.25 xpos 2000 ypos 400
        parallel:
            ease 0.1 rotate 360
            ease 0.1 rotate 0
            repeat
        parallel:
            ease 0.4 alpha 0.0

    show woodC:
        xpos 960 ypos 600 alpha 1.0 rotate 0
        parallel:
            ease 0.25 xpos -900 ypos 400
        parallel:
            ease 0.1 rotate 360
            ease 0.1 rotate 0
            repeat
        parallel:
            ease 0.4 alpha 0.0

    $ BecomeNamed("Sensei Marshal")
    marshal "--{i}KIAI!{/i} MARSHAL!"

    show marshal happy:
        xpos 730 yalign 1.8
        ease 0.5 xpos 670 yalign 1.0

    ethan @closedbrow talking2mouth "I don't know anything about martial arts, but I guess that was impressive?"

    $ PlaySound("Scattered Applause.ogg")

    red @closedbrow talking2mouth "The uneasy applause coming from the class is making me cringe, but he seems to be taking it in stride."

    marshal "{i}Domo!{/i} "

    show bea uniform:
        ypos 2.0 xpos 0.75 
        ease 0.2 ypos 1.0

    bea "Incredible, Sensei!"

    redmind "She says 'incredible,' but her face is still as stony as ever..."

    bea "I'm massively impressed by your martial prowess. Please, continue to teach us with determined vigor!"

    if (calDate.month == 4 and calDate.day == 5):
        marshal angry "Of course! Nothing but the best for my students! Now, what's your name?"
        bea "Bea, Sensei! From Stow-On-Side, in Galar."

    marshal "Of course, Bea-chan! I'll impart my {i}saikyo{/i} unto each and every one of you!"

    show bea at dissolveaway:
        xpos 0.75 

    show marshal:
        xpos 670 alpha 1.0
        ease 0.5 xpos 700 alpha 0.0

    pause 0.5

    show marshalbg with dis

    pause 0.5
    marshal "For this class, I will not only be teaching you about Fighting-type Pokémon, but I will also train your mind!{w=0.5} Your {i}kata!{/i} Your {i}bunkai!{/i} "
    marshal "When you leave my dojo, your mind and reflexes will be as sharp as a katana!"
    marshal "Let us start with some {i}kokyu ho!{/i} "

    show may uniform surprised at rightside with dis

    may "Um.{w=0.25}.{w=0.25}.{w=0.25} Some what?"

    marshal "{i}Kokyu ho!{/i} Breathing exercises!"

    if (calDate.month == 4 and calDate.day == 5):
        marshal "What is your name?"
        may "I'm May."

        marshal "May-chan! {i}Kokyu ho{/i} is the most basic form of training for any martial artist!{w=0.5} It is simple and effective!"

        show may surprisedbrow frownmouth
        marshal "Now, when I say {i}'Yamato,'{/i} you say {i}'Nadeshiko!'{/i} "

        ethan "Oh, man, this guy really doesn't know what he's saying..."

        show calem uniform surprised at leftside with dis

        pause 1.0

        marshal "{i}Hai!{/i} What is your name?"

        calem "It's Calem, Sir."
        
        marshal "Calem-san! {i}Dozo!{/i} "

        calem closedbrow talking2mouth "Uh... I'm not too familiar with martial arts, but isn't this an academic class?"
        calem -thinking @talkingmouth "I thought we'd be here learning material about Pokémon from textbooks and whatnot."

        hide calem at leftside with dis

    else:
        may sad "He's always like this..."
        may "But we're going to at least open the textbook today, right...?"

    marshal "{i}Osu!{/i} Yes, this dojo will cover all the material from the required readings."

    hide may at rightside with dis

    marshal "But what good is simply learning from a textbook?"
    marshal "Any {i}boke{/i} can pick up a book and read from it, but a real master will embrace Fighting Pokémon by studying their {i}waza{/i}, their technique!"
    marshal "If you only study with books, you will only succeed in achieving {i}munshin!{/i} Nothing!"
    marshal "Only through {i}kumite{/i} will you truly understand Fighting Pokémon!"
    marshal "Do you understand now?"

    ethan "...I think I understand even less now."

    marshal "{i}Osu!{/i} Let's continue with {i}kokyu ho!{/i} "
    marshal "{i}Hajime! Yamato!{/i} "

    Character("Whole Class") "\"{size=26}{i}{cps=15}N-{w=0.25}Nadeshiko{/cps}.{w=0.25}.{w=0.25}.{/i}{/size}\""

    marshal "{size=44}Too quiet! {i}Mo ichi do!{/i} {/size}"
    marshal "{size=44}{i}YAMATO!{/i} {/size}"

    Character("Whole Class") "\"{i}Nadeshiko!{/i}\""

    narrator "Marshal subjects you to many grueling exercises that take up the entirety of class."

    marshal "{i}Nani?{/i} It looks like we're out of time."
    marshal "{i}Sayonara!{/i} We will continue with our exercises next class!"

    hide marshal
elif (not HasEvent("Sensei Marshal", 2.1) and classstats["Fighting"] >= 10):#Disabling Poke
    show marshal with dis
    if (not HasEvent("Sensei Marshal", 2)):
        $ renpy.pause(1.0, hard=True)

        narrator "The class is reaching the end of a set of katas Sensei Marshal had subjected you to, when..."

        marshal happy @neutral2 "{i}Yoi!{/i} Good!"

        red uniform @confusedeyebrows talking2mouth "Uh, Sensei? What happened?"

        marshal @neutral2 "Your balance is reaching its fulfillment point! Soon, you will unleash your {i}bunkai!{/i}"

        red @confusedeyebrows talking2mouth "I... don't know what that means."

        marshal @neutral2 "Ah, but do you know how to use it?"

        pause 2.0

        red @closedbrow talking2mouth "No."

        marshal angry @angry2 "Then you must learn! For when you know all your moves, you know all your opponent's moves, too!"

        red @surprised "I... don't see the connection."

        marshal @angry2 "Then open your {i}fito!{/i} Think!"

        marshal @neutral2 "If you remove your opponent's ability to use one move, what can your opponent do?"

        red @closedbrow talking2mouth "Um... use three other moves?"

        marshal @think2 "{i}Hai!{/i} Now, what if you have prepared defenses against their second move? And what if you are able to counter their third move?"

        red @talkingmouth "I guess they'd be forced to use their fourth move, then."

        marshal @angry2 "So now you see! You are able to make decisions in battle for your opponent! And if you are controlling both sides of the battlefield, you are guaranteed to win!"

        red @surprised "Huh... that, actually, seems like a good strategy."

        marshal @think2 "Defeat me in a one-on-one battle and I will teach you the high-level technique for fighting-types, {i}Disabling Poke!{/i}"

        red @happy "{i}Poke?{/i}"

        marshal @angry2 "No, that's a rice bowl with seaweed, and, often, Krabby. A poke! The subtlest and most powerful fighting technique!"

        red @happy "Funny. I didn't think subtlety was something you cared too much about, Sensei."

        marshal @think2 "Indeed, I do not. But a subtle, quick, move might get past your opponent's guard before they can react."

        marshal @angry2 "And so, you disrupt their {i}ki!{/i} Their {i}chakra!{/i} And their ability to fight!"

        red @talkingmouth "Alright. I'm ready to take this exam, then."

        $ AddEvent("Sensei Marshal", 2)
    else:
        red uniform @talking2mouth "Sensei Marshal, I have trained diligently since our last meeting--and now I am ready to reclaim my honor!"

    marshal @neutral2 "{i}Hajimeru!{/i} Choose one Pokémon to be your {i}samurai!{/i} {color=#0048ff}A Fighting-type is your best option for glory in this battle!{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    marshal @angry2 "Banzai!"
    $ hidebattleui=False
    $ mustswitch = False
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("marshal", TrainerType.Enemy, [
        Pokemon(304, level=11, moves=[GetMove("Tackle"), GetMove("Harden"), GetMove("Metal Claw"), GetMove("Rock Tomb")], ability="Rock Head")
    ])

    call Battle([trainer1, trainer2], customexpressions=["red uniform", "red uniform angrybrow happymouth", "marshal", "marshal angry2"], reanchor=[False, True]) from _call_Battle_29
    $ battlehistory["Sensei Marshal1"]  = _return

    show marshal with dis

    if (WonBattle("Sensei Marshal1")):
        $ AddEvent("Sensei Marshal", 2.1)

        marshal @think2 "{i}Arigato.{/i} That was a well-fought battle."
        marshal @neutral2 "You have advanced to the level of Red Belt!"

        $ passedclass = True
        jump aftertutorintrofighting
    
    else:
        marshal @sad2 "Such dishonor..."
        marshal @neutral2 "Sequester yourself and train. When you are worthy, come back to face me!"

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide marshal with dis
elif (not HasEvent("Sensei Marshal", 3.1) and classstats["Fighting"] >= 20):#Black Belt
    show marshal with dis
    if (not HasEvent("Sensei Marshal", 3)):
        $ renpy.pause(1.0, hard=True)

        marshal @neutral2 "{i}Gakusei{/i} [last_name]!"

        red uniform @talkingmouth "Sensei!"

        marshal @happy "You have advanced rapidly in this class, and I would like to give you the advancement exam."

        marshal @angry2 "HOWEVER!"

        marshal @neutral2 "I ask of you {i}ichi{/i} question."

        red @closedbrow talking2mouth "No, not really. I use a cream for that."

        pause 1.0

        marshal @surprised "{i}Nani?{/i}"

        red @surprised "What?"

        pause 0.5

        marshal @think2 "I ask of you one question. What is the true benefit of a Black Belt?"

        red @closedbrow talking2mouth "Hm... well, it shows everyone around you what rank of martial artist you are? So you don't have to tell them?"

        marshal @neutral2 "{i}Sore wa chigau yo.{/i} It reaffirms your own self-worth. Achievement without recognition--pah! Good for training, but what do you train for, {i}besides{/i} recognition?"
        marshal @happy "No! You wear the belt because it reminds you of what you've achieved. It reminds you of every battle you have fought, every strife you have pulled through."

        red @closedbrow talking2mouth "Huh."

        marshal @neutral2 "There is little reason for humans such as ourselves to keep fit, to remember how to {i}kenka{/i}, in this world of Pokémon."
        marshal @think2 "We do it for ourselves. To live longer, to feel good, to show off. Or, perhaps, to train our Pokémon more effectively."

        pause 0.5

        marshal @angry2 "And that is {i}subarashi!{/i} Belief in yourself is the most important thing a martial artist can have. Whether human, or Pokémon."

        pause 0.5

        red @closedbrow talking2mouth "...Hm. So... if I give a Pokémon a Black Belt, in recognition of some achievement, which doesn't necessarily have to be the full process of getting a Black Belt a human would go through... it would help them?"

        marshal @happy "{i}Hai.{/i}"

        marshal @neutral2 "Pass this advancement exam, and I will let you give Black Belts to your Pokémon. Your Pokémon's Fighting-type moves will be boosted by 10%%."

        red @happy "Cool! Do I get one?"

        marshal @angry2 "No! You must still pass seven {i}shiken{/i}, and win a {i}tonamento!{/i}"

        red @closedbrow talking2mouth "Worth a shot..."

        $ AddEvent("Sensei Marshal", 3)
    else:
        red uniform @talking2mouth "Sensei Marshal, I have trained diligently since our last meeting--and now I am ready to reclaim my honor!"

    marshal @neutral2 "If you wish to pass this exam, [bluecolor]pick a single Pokémon to fight against my Fighting-type.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    marshal @angry2 "Banzai!"
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("marshal", TrainerType.Enemy, [
        Pokemon("Timburr", level=21, moves=[GetMove("Rock Slide"), GetMove("Bulk Up"), GetMove("Focus Energy"), GetMove("Low Kick")], ability="Guts", item="Oran Berry")
    ])

    call Battle([trainer1, trainer2], customexpressions=["red uniform", "red uniform angrybrow happymouth", "marshal neutral", "marshal angry2"], reanchor=[False, True]) from _call_Battle_84
    $ battlehistory["Sensei Marshal2"]  = _return

    show marshal with dis

    if (WonBattle("Sensei Marshal2")):
        $ AddEvent("Sensei Marshal", 3.1)

        marshal @neutral2 "{i}Hajimete.{/i} Your Pokémon are now worthy of the Black Belt. But remember, you are not yet worthy of wearing one!"
        
        redmind uniform @confusedeyebrows frownmouth "This feels backwards."

        $ GetItem("Black Belt", 1, "You gained a Black Belt! You long to tighten it around your own waist, but...")

        $ renpy.pop_call()
        jump aftertutoring
    
    else:
        marshal @sad2 "Such dishonor..."
        marshal @neutral2 "Sequester yourself and train. When you are worthy, come back to face me!"

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide marshal with dis
elif (not HasEvent("Sensei Marshal", 4.1) and classstats["Fighting"] >= 30):#Force Palm
    show marshal with dis
    if (not HasEvent("Sensei Marshal", 4)):
        $ renpy.pause(1.0, hard=True)

        marshal @neutral2 "[first_name]!"

        red uniform @talkingmouth "{i}Kashikomarimashita!{/i}"

        marshal @neutral2 "A question. When engaging an opponent, how should you position your hand?"

        red @closedbrow talking2mouth "Hm... well, early on in your classes, I think I would have assumed you'd want us to make a fist. But then you taught me Disabling Poke."
        red @closedbrow talking2mouth "But you made clear Disabling Poke is a specialty move, meant to be used in specific situations. So..."

        pause 0.5

        red @happy "I don't know, Sensei!"

        marshal @happy "That is {i}daijobu.{/i} You're thinking through the question the right way."

        red @talkingmouth "So... what's the answer?"

        marshal @neutral2 "As you have correctly surmised, control is more important than impact. If you hit someone with a fist, then--"
        
        show marshal with vpunch
        
        marshal @angry2 "{i}Eikyo!{/i} They bounce off! There is no control, no {i}himo!{/i}" 
        marshal @neutral2 "If you use an open-palm strike, though, you can guide your opponent's fall into position for follow-up attacks!"

        pause 0.5

        marshal @happy "Besides. A flat-palm strike can stun and disorient your opponent. A fist brings nothing but pain, which is often an inducer of adrenaline."

        marshal @neutral2 "Remember. Your goal in any fight is not to hurt your opponent. It is to control them."

        red @talking2mouth "Of course, Sensei."

        pause 1.0

        red @confused "But what does this have to do with Pokémon?"

        marshal @sad2 "Everything I just said applies to Pokémon, as well."

        red @surprised "Oh."

        pause 1.0

        red @happy "So... will you teach my Pokémon how to use open-palm strikes? For, uh, controlling purposes?"

        marshal @neutral2 "{i}Hai.{/i} I will bestow upon your Pokémon the usage of the move Force Palm, which can paralyze a foe."

        red @talkingmouth "But?"

        marshal @happy "But first you must pass an advancement exam."

        red @happy "I thought so. Well, I'm ready now!"

        $ AddEvent("Sensei Marshal", 4)
    else:
        red uniform @talking2mouth "Sensei, I've studied since the last time we fought--and now I'm more than ready to beat you."

    marshal @neutral2 "If you are to pass this exam, pick a single Pokémon. {color=#0048ff}A Fighting-type is not suited for this combat.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    marshal @happy "Fight with honor."
    $ hidebattleui=False
    $ mustswitch = False
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("marshal", TrainerType.Enemy, [
        Pokemon("Mr. Mime", level=31, moves=[GetMove("Psybeam"), GetMove("Confusion"), GetMove("Protect"), GetMove("Dazzling Gleam")], ability="Filter", item="Sitrus Berry")
    ])

    call Battle([trainer1, trainer2], customexpressions=["red uniform", "red uniform angrybrow happymouth", "marshal neutral", "marshal happy"], reanchor=[False, True]) from _call_Battle_85
    $ battlehistory["Sensei Marshal3"]  = _return

    show marshal with dis

    if (WonBattle("Sensei Marshal3")):
        $ AddEvent("Sensei Marshal", 4.1)

        marshal @happy "You are one of my best pupils, [first_name]. I think I might recommend that you be moved up to Green Belt soon..."
        
        red uniform @happy "Thanks, Sensei!"

        redmind @thinking "...But I still haven't had a single fight with any other students, so I'm not sure how warranted that is."

        $ passedclass = True

        jump aftertutorintrofighting
    
    else:
        marshal @sad2 "Such dishonor..."
        marshal @neutral2 "Sequester yourself and train. When you are worthy, come back to face me!"

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide marshal with dis

elif (FindGenericClassScene(True)):#generic scene
    $ renpy.call(FindGenericClassScene())
    hide marshal with dis
else:# _really_ generic scene
    show marshal with dis
    marshal "{i}Ohaiyo, gakusei!{/i} Today, we will be studying {i}osakai{/i}!"
    hide marshal with dis
    show marshalbg with dis
    marshal "Prepare yourselves to study like never before, or you'll end up a {i}baka gaijin{/i}!"
    narrator "Class proceeds without incident."

return

label movetutorfighting:
show marshal with dis
marshal @neutral2 "Hmph. You want to access my ancient, secret techniques? Fine! Which {i}ken{/i} will you wield?"
marshal @neutral2 "I can teach Disabling Poke, a fast move which will disable the foe's last-used move for four turns, and do some damage!"
if (HasEvent("Sensei Marshal", 4.1)):
    marshal @happy "I can also teach the move Force Palm! This will paralyze the foe with a 30%% chance! Open-palm strikes will knock the wind out of any foe."

label aftertutorintrofighting:
$ taughtmove = None

menu:
    ">Learn Disabling Poke":
        $ taughtmove = "Disabling Poke"
    ">Learn Force Palm" if (HasEvent("Sensei Marshal", 4.1)):
        $ taughtmove = "Force Palm"
    "Nevermind":
        marshal @angry2 "{i}Baka!{/i} Clear your mind before speaking if you know not what you'll say!"

        if (passedclass):
            $ renpy.pop_call()
            jump aftertutoring
        else:
            jump afterfightingsetup
python:
    hidebattleui = True
    renpy.transition(dissolve)
    newindex = renpy.call_screen("switch", MakeRed())
    if (newindex != "back"):
        newmon = playerparty[newindex]
    hidebattleui=False
if (newindex == "back"):
    marshal @angry2 "{i}Baka!{/i} Clear your mind before speaking if you know not what you'll say!"
elif (MonCanLearn(newmon, taughtmove)):
    $ newmon.LearnNewMove([(1, taughtmove)])
    if (taughtmove in newmon.GetMoveNames()):
        jump endclass
else:
    marshal @sad2 "This Pokémon lacks the fighting spirit required to master [taughtmove]!"

jump aftertutorintrofighting

label itemcraftfighting:
show marshal with dis

marshal @happy "A martial artist must master more than hand-to-hand combat. They must also master the usage of {i}heiki{/i}, equipment!"
marshal @neutral2 "The Black Belt is an item of great honor for humans. But for Pokémon, it boosts the power of their Fighting-type moves by 10%%."

menu:    
    ">Craft Black Belt" if (HasEvent("Sensei Marshal", 3.1)):
        $ GetItem("Black Belt", 1, "You craft the Black Belt by shredding a spare curtain. Sensei Marshal seems, perplexingly, fine with that.")
        jump endclasscraft
    "Nevermind":
        marshal @happy "Perhaps you are unsure how to use these items of unlimited potential. Study and train, then return!"
        jump afterfightingsetup
