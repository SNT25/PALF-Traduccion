label waterelective:

$ renpy.transition(dissolve)
show screen currentdate

scene map
show blank2:
    alpha 0.8

show classroom with dis

show waterclass:
    alpha 0.0 xalign 0.5 yalign 1.0
    ease 0.5 alpha 1.0
show waterglow1:
    alpha 0.0 xalign 0.5 yalign 1.0
    block:
        ease 0.5 alpha 1.0
        ease 0.5 alpha 0.0
        pause 1.5
        repeat
show waterglow2:
    alpha 0.0 xalign 0.5 yalign 1.0
    block:
        pause 0.5
        ease 0.5 alpha 1.0
        ease 0.5 alpha 0.0
        pause 1.0
        repeat
show waterglow3:
    alpha 0.0 xalign 0.5 yalign 1.0
    block:
        pause 1.0
        ease 0.5 alpha 1.0
        ease 0.5 alpha 0.0
        pause 0.5
        repeat

############################################################################################################################################################################################################################
#### 13. WATER       #######################################################################################################################################################################################################
############################################################################################################################################################################################################################
$ renpy.pause(1.0, hard=True)

$ location = "water"
$ passedclass = False

call klaraevent from _call_klaraevent_1
call ethanevent from _call_ethanevent_17
call nessaevent from _call_nessaevent_1

label afterwatersetup:

if (HasEvent("Instructor Wallace", 2.1)):
    menu:
        "{b}>General Studies{/b}":
            pass

        ">Ask for move tutoring":
            jump movetutorwater

        ">Craft items" if (HasEvent("Instructor Wallace", 3.1)):
            jump itemcraftwater

if (HasEvent("Instructor Wallace", 1) and IsPresent("Klara", "Water") and not HasEvent("Melody", "WallaceInterruption")):#KLARANOTE:the first time you take class with that disgusting hussy, Melody
    $ AddEvent("Melody", "WallaceInterruption")
    narrator "It seems Instructor Wallace is a bit later than usual...?"

    show melody uniform on with dis:
        xpos 0.75 xzoom -1

    melody "{i}*Tap.*{/i}{w=2.2} {i}*Tap.*{/i}{w=2.2} {i}*Tap.*{/i}"

    redmind uniform @thinking "Geez, she even taps her fingers on the table annoyingly..."

    melody @bubblemouth "{i}*Psssscccchhhh...*{/i}"

    redmind @unamusedbrow unamusedmouth "If Instructor Wallace doesn't get here in three seconds, I'm going to someone else's class."

    pause 2.999

    $ PlaySound("ExitBuilding.ogg")

    show wallace behind melody with dis:
        xpos -0.1
        ease 0.5 xpos 0.5

    wallace surprised @happy "Hello, my wonderful stude-"

    show wallace:
        xpos 0.5
        ease 0.5 xpos 0.33

    show melody:
        xpos 0.75
        ease 0.5 xpos 0.66

    melody sadbrow @talkingmouth "What are you wearing?"

    wallace -surprisedbrow -frownmouth -surprised @happy "See something you like? Part of esteemed Poké Stylist Hermione's 2005 collection--early-access, naturally."

    melody @closedbrow talkingmouth "Uh-huh."

    pause 1.0

    melody @talkingmouth "And you thought you'd wear that in class."

    wallace @surprisedbrow talking2mouth "But of course! Beauty is war."
    wallace @happy "If you're not screaming out what you have, then why have it?" 
    wallace @angrybrow happymouth "If you're not dragging the competition into your undertow, then why even try? That's what I say!"

    pause 1.0

    show wallace surprisedbrow frownmouth with dis

    melody @talkingmouth "I can tell you're shaven."

    pause 0.5

    melody @sadbrow talkingmouth "{i}Completely{/i} shaven."

    wallace @talkingmouth "Well, I do like to be well-groomed. Besides, extra hair raises the {i}unsightliest{/i} lumps."

    melody @talkingmouth "That's not the point."

    wallace @closedbrow talking2mouth "My fashion choices are a form of self-expression."
    wallace @talkingmouth "Now, I {i}do{/i} love talking fashion, much like dear Valerie, but this is not the time to--"

    stop music

    show wallace angrybrow frownmouth with dis

    melody @talkingmouth "You're half-naked in front of a class of teenagers."

    pause 1.0

    redmind @surprised "Geez."

    pause 1.0

    melody -sadbrow @talkingmouth "I'm not wrong."

    if (IsDate(25, 5, 2004)):
        wallace @closedbrow talking2mouth "I don't believe I caught your name?"

        melody @talkingmouth "I don't believe I dropped it."

        klara uniform makeup hairpin @talkingmouth "It's Melody, sir!"

        wallace @talking2mouth "Melody..."

    else:
        wallace @talking2mouth "Melody, we've discussed this before..."

    wallace @closedbrow talking2mouth "My relationship with clothing is a complex one. As a member of the Waters clan, my modes of dress and expression were expected to fall within a certain mark, if not necessarily prescribed." 
    wallace @talkingmouth "Now, at my apex, I express the liberation I have earned through my clothing, which--"
    
    melody @talkingmouth "Justify it however you want."
    melody @sadbrow talkingmouth "Your 'moral imperative' or whatever. I see it. I know what you're doing."
    melody @talkingmouth "Maybe no-one else does. But I do."
    melody @talkingmouth "The Emperor has no clothes." 
    
    pause 0.5
    
    melody @bubblemouth "And he's a pervert."

    wallace @angrybrow talking2mouth "Out."

    pause 1.0

    melody @surprisedbrow talking2mouth "...Hm?"

    wallace @angrybrow talking2mouth "Get out of my classroom. Immediately."

    pause 1.0

    melody @talkingmouth "Maybe."

    pause 0.5

    show wallace surprisedbrow frownmouth with dis

    melody @talkingmouth "Why?"

    wallace @talking2mouth "Why...?"
    wallace -surprisedbrow @talking2mouth "Because I am your instructor for this class, and if you refuse to show me the respect due a Champion, I will refuse you a Champion's knowledge."

    pause 1.0

    melody @surprisedbrow talkingmouth "Oh, you were a champion?"
    melody @sadbrow talkingmouth "Sorry, I only check on the status of champions every eighty-one days. Must have missed you."
    melody @angrybrow talkingmouth "How long were you champion, again?"

    show wallace angrybrow frownmouth with dis

    melody "{w=0.5}.{w=0.5}.{w=0.5}."

    melody @closedbrow talkingmouth "Really thought you'd start screaming at that one."
    melody @talkingmouth "I'll keep looking."

    wallace @talkingmouth closedbrow "Oh, my dear Melody, it would seem that you hate me."

    melody @angry "Don't call me 'dear', you sicko."

    show wallace -angrybrow -frownmouth with dis
    
    wallace @happy "Well, hate, see, that's an emotion I'm quite familiar with. Hate is a reasonable reaction from the {i}jealous.{/i} The bitter. Those who know they cannot achieve what {i}I{/i} have."

    melody @bubblemouth "{w=0.5}.{w=0.5}.{w=0.5}."
    melody @talkingmouth "You think I'm jealous?"

    wallace @happy "But I'll have you know I did not claim my Championship off my inability to strategize. If your goal is truly just to 'get' to me..."
    wallace @angrybrow talkingmouth "Foolish girl. You'd have better luck with {i}any{/i} other instructor. Water off a duck's back, my dear."

    melody @talkingmouth "Hm."

    wallace @happy "I rescind what I said previously. You do not need to leave. In fact, I request that you stay here, such that I may--"

    show melody:
        xpos 0.75
        ease 0.5 xpos 1.2

    pause 0.3

    $ PlaySound("ExitBuilding.ogg")

    show wallace surprisedbrow frownmouth with dis

    pause 1.0

    wallace angrybrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    wallace @angrybrow talking2mouth "...No, I shan't allow this."
    wallace @closedbrow talkingmouth "Apologies, class. I need to talk to Dean Drayden immediately. Class is dismissed."

    hide wallace with dis

    pause 1.0

    if (IsPresent("Misty", "Water")):
        show misty uniform with dis:
            xpos 5/6

        misty @surprised "Uh... what do we do now?"

    if (IsPresent("Nessa", "Water")):
        show nessa uniform with dis:
            xpos 1/6 xzoom -1

        nessa @talkingmouth "I guess we should... probably study by ourselves?"

    if (IsPresent("Brendan", "Water")):
        show brendan uniform sad with dis:
            xpos 2/6

        brendan @talking2mouth "Even if Instructor Wallace goes to Dean Drayden, I'm pretty sure that the DC's done that a bunch already... May and I've seen her in there a bunch."

    if (IsPresent("Klara", "Water")):
        show klara sad uniform makeup hairpin with dis:
            xpos 4/6

        klara @talkingmouth "Wow. I mean, people have always been telling me how {i}awful{/i} she is, but I really didn't think she could be that bad..."

    if (IsPresent("Ethan")):
        show ethan uniform frownmouth with dis

        ethan @closedbrow talking2mouth "Jeez. Drama bomb much?"
        ethan @sad "No way we're going to be able to get any work done after {i}that.{/i}"

    narrator "With Instructor Wallace's abrupt departure, the class slowly disperses over the next hour."

    $ PlaySound("BellChime.ogg")

    if (IsPresent("Misty", "Water")):
        $ ValueChange("Misty", 2, 5/6, False)

    if (IsPresent("Nessa", "Water")):
        $ ValueChange("Nessa", 2, 1/6, False)

    if (IsPresent("Brendan", "Water")):
        $ ValueChange("Brendan", 2, 2/6, False)

    if (IsPresent("Klara", "Water")):
        $ ValueChange("Klara", 10, 4/6, False)

    if (IsPresent("Ethan")):
        $ ValueChange("Ethan", 2, 3/6)

    narrator "Sharing in such a harrowing experience increases your bonds with your classmates significantly..."
    narrator "But you do not gain any knowledge on the Water-type, due to Instructor Wallace's empty desk."

    $ renpy.pop_call()
    jump aftertutoring

elif (not HasEvent("Instructor Wallace", 1)): #first class
    $ AddEvent("Instructor Wallace", 1)
    $ renpy.pause(1.0, hard=True)

    show misty uniform angry:
        xpos 0.25 alpha 0.0
        ease 0.5 alpha 1.0

    $ renpy.pause(1.0, hard=True)

    redmind "Well, it's a familiar face, but she doesn't seem very excited to see me."
    redmind "Let's see... is there someone else?"

    hide misty at leftside with dis

    pause 1.0

    $ PlaySound("ExitBuilding.ogg")

    show wallace with dis:
        xpos 1200
        ease 0.5 xpos 660
        
    wallace @happy "Hello, my wonderful students!"

    redmind surprised "That almost gave me a heart attack!{w=0.5} This guy knows how to really make an entrance."
    redmind -surprisedbrow -frownmouth -surprised "Maybe Whitney took some lessons from him."
    redmind @thinking "And what the heck is this guy wearing? This has got to be against the school dress code!"

    show wallace:
        xpos 660 alpha 1.0
        ease 0.5 xpos 600 alpha 0.0

    show wallacebg with dis

    if (not IsDate(5, 4, 2004)):
        wallace @surprised "Ooooh? Looks like we've got a couple new students to join us! Let's see... your names are Ethan and [first_name], right? Splendid, just splendid!"
        wallace @happy "I'm Wallace, but you already know that. And I welcome both of you to your first {color=#0048ff}Water class{/color} at Kobukan Academy!"
    else:
        wallace @happy "I'm Wallace, but you already know that. And I welcome you all to your first {color=#0048ff}Water class{/color} at Kobukan Academy!"
    
    $ BecomeNamed("Instructor Wallace")
    wallace @talkingmouth "You didn't hear this from me, but Water really {i}is{/i} the best of types. It covers two thirds of the planet, after all!"
    wallace "Meowth got your tongues? Aren't you all just sparkling with excitement?{w=0.3} I know I am!"

    pause 1.0
    ethan uniform surprised "How are we supposed to react to all this?"

    if (not IsDate(5, 4, 2004)):
        wallace "I see my presence has dazzled you two into silence. I suppose it's not every day one meets a former Champion!"
    else:
        wallace "I see my presence has dazzled you all into silence. I suppose it's not every day one meets a former Champion!"

    wallace "If you won't talk, then I shall make you!"
    wallace "Hmm.{w=0.25}.{w=0.25}.{w=0.25} YOU!"

    narrator "Wallace flamboyantly points straight at Nessa."

    show nessa uniform:
        alpha 0.0 xpos 500
        ease 0.5 alpha 1.0

    nessa "[ellipses]"

    nessa @talkingmouth "Um, are you pointing at me?"
    
    if (not IsDate(5, 4, 2004)):
        wallace "Yes, Nessa! Stand up and introduce yourself to the new students."
        redmind "Didn't he kind of just do that for her...?"
    else:
        wallace "Yes, you! Stand up and introduce yourself."

    nessa @talkingmouth "Uh, okay..."
    nessa @closedbrow talkingmouth "But, like, we already know each other."
    
    nessa @talkingmouth "I'm Nessa. I'm from Hulbury, in Galar."
    nessa @talkingmouth "I specialize in Water-type Pokémon. I also work as a model." 
    nessa @sadbrow talkingmouth "Sometimes."
    wallace "Oh, really? What a coincidence--so do I. Ahahaha!{w=0.5} And {i}why{/i} are you in this class?"

    pause 1.5

    nessa @surprised "{cps=26}...because I want to learn more about Water Pokémon?{/cps}"
    wallace "Wonderful! Anything else?"
    nessa @talkingmouth closedbrow "...No, I think I'm good."
    
    show nessa uniform:
        alpha 1.0 xpos 500 ypos 1.0
        ease 0.5 ypos 2.0 alpha 0.0

    wallace "Very good, Nessa! A brilliant start."

    wallace "Now.{w=0.25}.{w=0.25}.{w=0.25} YOU!"

    narrator "Wallace proceeds to go down the entire roster and makes everyone introduce themselves."
    narrator "Nothing of value is accomplished, and you sit around awkwardly for an hour."

    pause 1.0

    wallace "...Well! I hope you've all learned the importance of class participation!"
    wallace "All right, that is all the time we have for today.{w=0.5} But best be prepared--next time we'll {i}really{/i} get swimming."
    wallace "Class dismissed!"
elif (not HasEvent("Instructor Wallace", 2.1) and classstats["Water"] >= 10):#Healing Spring
    show wallace with dis
    if (not HasEvent("Instructor Wallace", 2)):
        $ renpy.pause(1.0, hard=True)

        narrator "You're working hard on your studying when you notice Instructor Wallace is standing in the middle of the class, tapping his foot impatiently."

        redmind uniform @thinking "Looks like something's biting at the teacher. Maybe I should ask?"

        red @happy "Instructor Wallace? Is something wrong?"

        wallace @talkingmouth "It most certainly is! We've been taking these classes for far too long, and yet the number of people who've requested advancement is painfully low!"

        red @closedbrow talking2mouth "Maybe some students didn't know what advancement was?"

        wallace @sadbrow talkingmouth "Well, then they should've asked!"

        red @happy "Just playing devil's advocate here, but if someone asked, y'know, 'is there anything more to this class,' and you said no, that would be pretty embarrassing." 
        
        wallace @angry "Oh, embarrassment, shmembarrassement! I care less if you learn {i}anything{/i} about Water-types than I do that you learn embarrassement isn't real."

        red @surprised "Sir?"

        wallace @happy "Put yourself out there, darlings! Ask for those raises! Take up new hobbies! Wear what you want!"

        wallace @talkingmouth "{i}Anything{/i} but drowning under the suffocating weight of 'what if!'"

        red @talkingmouth "Well... can I advance in this class, yet?"

        wallace @happy "No."

        pause 2.0

        red @closedbrow talking2mouth "Huh, you're right, that's not so bad."

        wallace @happy "There we go, then! Why, yes, of course you can. But, first, you get to engage in a one-on-one battle with a former National Champion of the Hoenn Region!"

        wallace @talkingmouth "Aren't you lucky?"

        red @happy "Pretty lucky, yeah. But I look forward to facing you at your full strength one day."

        wallace @talkingmouth "Splendid! As for now, winning this battle will allow me to teach you 'Healing Spring'!" 
        wallace @sad "Personally, I'd like to teach you all my techniques immediately, but the school requires you show some competency before I start handing out the Champion-level moves."

        red @closedbrow talking2mouth "Healing Spring. I don't think I've heard of that one. Did you invent it?"

        wallace @happy "None other! It's a glorious shower of healing waters, which sets up rain and helps the user recover a little health every turn."

        red @happy "Cool. It's a better Rain Dance."

        wallace @happy "You get it? Fabulous! Now, let's dazzle the class with our battle!"

        $ AddEvent("Instructor Wallace", 2)
    else:
        red uniform @talking2mouth "Wallace, I've done a bit more training. And I'm ready to win, this time!"

    wallace @talkingmouth "Pick one Pokémon to use against me. Lucky for you, I'm not allowed to use my actual team, so {color=#0048ff}I recommend picking a Water-type.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    wallace @angrybrow happymouth "Dance, water, dance!"
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("wallace", TrainerType.Enemy, [
        Pokemon(111, level=11, moves=[GetMove("Tackle"), GetMove("Tail Whip"), GetMove("Smack Down"), GetMove("Bulldoze")], ability="Lightning Rod")
    ])

    call Battle([trainer1, trainer2], uniforms=[True, False]) from _call_Battle_41
    $ battlehistory["Instructor Wallace1"]  = _return

    show wallace with dis

    if (WonBattle("Instructor Wallace1")):
        $ AddEvent("Instructor Wallace", 2.1)

        wallace @happy "Dazzling! Take it from a former Champion! Keep that up and you may {i}someday{/i} grace my level!"

        $ passedclass = True
        jump aftertutorintrowater
    
    else:
        wallace @happy "You gave it your best and put yourself out there. I couldn't be prouder, darling!"
        wallace @talkingmouth "My door is open for your next attempt. Defeat is far from the end--just look at me!" 
        wallace @sadbrow talkingmouth "I'm a {i}former{/i} Champion--but do I look like a man defeated?"

        red uniform @happy "No, you don't. Thank you, Instructor Wallace."

        wallace @happy "Any time, darling!"

    hide wallace with dis
elif (not HasEvent("Instructor Wallace", 3.1) and classstats["Water"] >= 20):#Mystic Water
    show wallace with dis
    if (not HasEvent("Instructor Wallace", 3)):
        $ renpy.pause(1.0, hard=True)

        narrator "You are studying hard in class when you notice that Instructor Wallace has, in an uncharacteristically subtle move, managed to sneak up next to you."

        red uniform @surprised "Instructor? Is there something I can do for you?"

        wallace @happy "Well, certainly, darling. A little birdie told me that you want to be a Pokémon Champion!"

        red @talkingmouth "That's right, Sir. It's what I've wanted, more than anything else. Ever."

        wallace @talkingmouth "Well, then, why?"

        red @closedbrow talking2mouth "That's something a lot of people ask me. And I think I give a different answer to every single person."

        red @sadbrow happymouth "I've just got so many reasons that I can't narrow it down to just one."

        wallace @happy "Hm... well, that's fair."

        red @talkingmouth "What about you, Instructor Wallace? Why did you want to be a Champion?"

        wallace @talkingmouth "Well, I'd already been the World Contest Champion--long enough that I'd run out of challengers. And I happened to hear some so-called 'fans' of mine at an autograph signing, where they made light of my battle performance!"

        red @confused "Huh?"

        wallace @angry "Yes, can you believe it? They thought I only had the skills to dazzle and entertain! As though I was some limp-wristed fop unable to hit harder than my fashion sense!"

        red @surprised "Uh..."

        wallace @surprised "Well, when I heard that, I was, of course, incensed! And not the nice-smelling kind they burn on Mt. Pyre."
        wallace @closedbrow talkingmouth "The Hoenn Champion at the time, Steven Stone, is a good friend of mine. I happened to know that his party was rather poorly matched against mine, so I simply waltzed through the Elite Four and dethroned him!"
        wallace @happy "Really, it was quite simple. I don't know why more people don't become Champion for a while. It's a gorgeous story."

        red @surprised "So... wait... you became Champion out of spite?"

        wallace @happy "Well, there was a little bit about proving to myself I could do it, and kicking Stevey-boy out of his funk, but yes, it was mostly spite."

        red @talking2mouth "Huh."

        wallace @talkingmouth "Of course, as I'm sure you know, I didn't keep the position for very long. Steven has, with all fair credit to him, always been a stronger battler. With time to prepare, he easily took back the Championship."
        wallace @happy "But I believe I made my point sufficiently. To myself, to Steven, to my beloved Hoenn, and to those two buttheads who doubted me."

        red @sweat talkingmouth "Uh, yeah. Wow. I'll say."

        wallace @talkingmouth "But enough about me! (Though that is my favorite topic.) You've been doing splendidly in this class, [first_name], and I think it's about time I commend you for that."
        wallace @happy "What do you think about taking an advancement exam? If you pass, you'll be privy to one of my {i}personal{/i} Mystic Waters, which boost Water-type attacks by 10%%!"

        red @happy "I'm excited! Let's do this."

        $ AddEvent("Instructor Wallace", 3)
    else:
        red uniform @talking2mouth "Instructor Wallace, I've done a bit more training. And I'm ready to win, this time!"

    wallace @happy "Glorious! {color=#0048ff}Pick one Pokémon to use against my Water-type!{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    wallace @angrybrow happymouth "Behold!"
    $ hidebattleui=False
    $ mustswitch = False
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("wallace", TrainerType.Enemy, [
        Pokemon("Milotic", level=21, moves=["Aqua Ring", "Twister", "Disarming Voice", "Water Pulse"], ability="Cute Charm", item="Oran Berry")
    ])

    call Battle([trainer1, trainer2], uniforms=[True, False]) from _call_Battle_109
    $ battlehistory["Instructor Wallace2"]  = _return

    show wallace with dis

    if (WonBattle("Instructor Wallace2")):
        $ AddEvent("Instructor Wallace", 3.1)

        wallace @happy "Wonderful; wonderful! You'll make a title challenger yet!"

        $ GetItem("Mystic Water", 1, "Instructor Wallace flamboyantly tosses a Mystic Water your way. You're unsure where he was keeping it. His outfit clearly does not have pockets.")

        $ renpy.pop_call()
        jump aftertutoring
    
    else:
        wallace @happy "You gave it your best and put yourself out there. I couldn't be prouder, darling!"
        wallace @talkingmouth "My door is open for your next attempt. Defeat is far from the end--just look at me!" 
        wallace @sadbrow talkingmouth "I'm a {i}former{/i} Champion--but do I look like a man defeated?"

        red uniform @happy "No, you don't. Thank you, Instructor Wallace."

        wallace @happy "Any time, darling!"

    hide wallace with dis
elif (not HasEvent("Instructor Wallace", 4.1) and classstats["Water"] >= 30):#Aqua Jet
    show wallace with dis
    if (not HasEvent("Instructor Wallace", 4)):
        $ renpy.pause(1.0, hard=True)

        wallace @happy "[first_name]-boy! How are you doing in this class?"

        red uniform @closedbrow talking2mouth "Well enough, I think, Instructor. Um... I'm having a good time, at least. And I think I'm learning things, too."

        wallace @talkingmouth "Well, that's good to hear! I was concerned, given that I was a Contest Champion, {i}and{/i} a Battle Champion, that perhaps I wouldn't make a {i}fabulous{/i} teacher as well!"
        wallace @happy "It's {i}dazzling{/i} to see that my concerns were unfounded."

        red @confused "Uh... yeah."

        redmind @thinking "This guy has some impressive self-confidence."

        wallace @talkingmouth "Remind me--did I ever tell you why I decided to become a teacher?"

        red @closedbrow talking2mouth "No, Instructor, I don't think you did."

        wallace @happy "Well, pull up a chair, and sit yourself down! I've got a delicious little scandal to share."

        red @surprised "Oh! Really? I mean, I'm already sitting down, but I'd like to hear this!"

        wallace @talkingmouth "Well, as I already told you, I decided to become Champion when my good friend Steven was in a rut."
        wallace @happy "I'd retired from my illustrious career as a Contest Coordinator, and was the eighth Gym Leader of Hoenn at the time."
        wallace @talkingmouth "Well, after becoming Champion, my old mentor, and good friend, Juan, took my gym over for me. Meanwhile, my very own niece, who I'm incredibly proud of, by-the-by, had become the new Contest Champion."
        wallace @happy "That's, ah, {i}World{/i} Contest Champion, by the by."

        red @happy "Impressive!"

        wallace @talkingmouth "I was glad, of course, that my friends and family had managed to fill the gaping holes left by my presence. But that did mean that I was somewhat out of roles to fill when Stevey-boy ousted me from the Championship."

        pause 1.0

        red @confused "So... you became a teacher?"

        wallace @happy "Exactly! Look at me. I'm far too young and gorgeous to retire yet. I could, certainly. I have a tremendous number of beach houses that I can hear calling my name right now." 
        wallace @talkingmouth "I even rent a villa from the Champion of Sinnoh, I'll have you know."
        wallace @happy "But retirement would not suit me. I am the river. Ever moving on, taking new forms, new shapes, and dragging everything that fills into my presence along with me."

        red @talkingmouth "And... we, your students, are the stuff in the river?"

        wallace @happy "Quite so! And how lucky you are to be that."

        red @confused "Right..."

        wallace @talkingmouth "Oh, you may be doubtful, but there's no denying that I've been a fabulous teacher thus far. If I hadn't, you wouldn't be ready to advance in this class!"

        pause 1.0

        wallace @happy "And, of course, you are."

        red @talkingmouth "Uh, yeah. Sure. What do I get from advancing?"

        wallace @happy "Aqua Jet, [first_name]-boy! It doesn't deal Champion-level damage, but for the majority of slow, bulky, Water-types, the ability to hit something faster, first, is too good to turn down!"
        
        red @talkingmouth "I'll take it. I'm ready to battle now."

        $ AddEvent("Instructor Wallace", 4)
    else:
        red uniform @talking2mouth "Wallace, I've done a bit more training. And I'm ready to win, this time!"

    wallace @happy "Brilliant! Then Pick one Pokémon to use! {color=#0048ff}But don't use a Water-type this time. Things'll turn out poorly if you do!~{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    wallace @angrybrow happymouth "Let's see if you can give me a challenge..."

    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("wallace", TrainerType.Enemy, [
        Pokemon("Sunflora", level=31, moves=[GetMove("Giga Drain"), GetMove("Worry Seed"), GetMove("Leech Seed"), GetMove("Ingrain")], ability="Early Bird", item="Sitrus Berry")
    ])

    call Battle([trainer1, trainer2], uniforms=[True, False]) from _call_Battle_110
    $ battlehistory["Instructor Wallace3"]  = _return

    show wallace with dis

    if (WonBattle("Instructor Wallace3")):
        $ AddEvent("Instructor Wallace", 4.1)

        wallace @happy "What a marvelous show! My hat is off to you--metaphorically, of course."
        wallace @talkingmouth "Because you've beaten a Water-type, a Pokémon that easily defeats Water-types, and a Pokémon that Water-types have no trouble trouncing, future exams will be a bit harder."
        wallace @happymouth "Not to worry--I won't be using my {i}actual{/i} team, buuuuut I {i}will{/i} be using three Pokémon. So don't get swept awaaaaay!~"

        $ passedclass = True
        jump aftertutorintrowater
    
    else:
        wallace @happy "You gave it your best and put yourself out there. I couldn't be prouder, darling!"
        wallace @talkingmouth "My door is open for your next attempt. Defeat is far from the end--just look at me!" 
        wallace @sadbrow talkingmouth "I'm a {i}former{/i} Champion--but do I look like a man defeated?"

        red uniform @happy "No, you don't. Thank you, Instructor Wallace."

        wallace @happy "Any time, darling!"

    hide wallace with dis

elif (FindGenericClassScene(True)):#generic scene
    $ renpy.call(FindGenericClassScene())
    hide wallace with dis
else:# _really_ generic scene
    show wallace with dis
    wallace @happy "[timeOfDay], my fabulous students! Today, let's all conduct ourselves with elegance and decorum."
    hide wallace with dis
    show wallacebg with dis
    wallace "Please open your textbooks to page... oh, I'm falling asleep already. Nevermind, let's all go to the pool!"
    narrator "Class proceeds without incident."

return

label movetutorwater:
show wallace with dis
wallace @surprised "Oh-ho, you want your Pokémon to learn moves directly from a Champion? Well, at Kobukan, you can do that!"
wallace @happy "I can teach Healing Spring, which causes it to rain for five turns, and restores a little health to the user every turn."
if (HasEvent("Instructor Wallace", 4.1)):
    wallace @talkingmouth "But still tactics aren't for everyone, darling. If you want to surge out of the gate like a rush of water, try Aqua Jet! It {i}always{/i} hits first."

label aftertutorintrowater:
$ taughtmove = None

menu:
    ">Learn Healing Spring":
        $ taughtmove = "Healing Spring"
    ">Learn Aqua Jet" if (HasEvent("Instructor Wallace", 4.1)):
        $ taughtmove = "Aqua Jet"
    "Nevermind":
        wallace @sad "Don't back out now, darling!"

        if (passedclass):
            $ renpy.pop_call()
            jump aftertutoring
        else:
            jump afterwatersetup
python:
    hidebattleui = True
    renpy.transition(dissolve)
    newindex = renpy.call_screen("switch", MakeRed())
    if (newindex != "back"):
        newmon = playerparty[newindex]
    hidebattleui=False
if (newindex == "back"):
        wallace @sad "Don't back out now, darling!"
elif (MonCanLearn(newmon, taughtmove)):
    $ newmon.LearnNewMove([(1, taughtmove)])
    if (taughtmove in newmon.GetMoveNames()):
        jump endclass
else:
    wallace @sad "Oh, darling, there are some things not even a Champion can do. That Pokémon simply can't learn [taughtmove]."

jump aftertutorintrowater

label itemcraftwater:
show wallace with dis

wallace @talkingmouth "Inner beauty is one thing, but true stars know how to accentuate their outsides with glimglams galore!"
wallace @happy "A Mystic Water--which comes in stylish pendant form--boosts the power of Water-type moves by 10%%! My Champion team held a few back in the day."

menu:    
    ">Craft Mystic Water" if (HasEvent("Instructor Wallace", 3.1)):
        $ GetItem("Mystic Water", 1, "You polish, shine, buff, and round an aquamarine gem to perfection. Wallace compliments your craftsmanship.")
        jump endclasscraft
    "Nevermind":
        wallace @happy "Come back anytime, darling!"
        jump afterwatersetup
