label groundelective:

$ renpy.transition(dissolve)
show screen currentdate

scene map
show blank2:
    alpha 0.8

show classroom with dis

show groundtype:
    xalign 0.5 yalign 1.0

$ location = "ground"
$ passedclass = False

############################################################################################################################################################################################################################
#### 13. GROUND    #######################################################################################################################################################################################################
############################################################################################################################################################################################################################
$ renpy.pause(1.0, hard=True)

call jasmineevent from _call_jasmineevent
call ethanevent from _call_ethanevent_10

label aftergroundsetup:

if (HasEvent("Instructor Bertha", 2.1)):
    menu:
        "{b}>General Studies{/b}":
            pass

        ">Ask for move tutoring":
            jump movetutorground

        ">Craft items" if (HasEvent("Instructor Bertha", 3.1)):
            jump itemcraftground

if (not HasEvent("Instructor Bertha", 1)): #first class
    $ AddEvent("Instructor Bertha", 1)
    $ renpy.pause(1.0, hard=True)

    show bertha happy2:
        xpos 900 yalign 1.0 alpha 0.0
        parallel:
            ease 1.5 xpos 860
        parallel:
            ease 0.5 alpha 1.0

    $ lowerstring = timeOfDay.lower()
    bertha "Good [lowerstring], children."

    window hide
    
    show bertha norm2:
        xpos 860 yalign 1.0 alpha 1.0

    if (not (calDate.month == 4 and calDate.day == 5)):
        bertha surprised2 "Oh? We have some new students? Fantastic!"

    $ BecomeNamed("Instructor Bertha")
    bertha "Welcome to your first {color=#0048ff}Ground-type class{/color} at Kobukan Academy. I'm your teacher, Bertha."

    show bertha norm:
        xpos 860 alpha 1.0
        ease 0.5 xpos 840 alpha 0.0

    pause 0.5

    show berthabg:
        alpha 0.0 yalign 1.0 xalign 0.5
        pause 0.5
        ease 0.5 alpha 1.0

    bertha "For this class, we'll be learning the biology and anatomy of Ground Pokémon and the effects they have on the world's tectonics."
    bertha "If we have time, we can take a field trip through Mt. Coronet and see them in action!"

    ethan uniform surprised "Nobody told me we'd be traveling to other regions!" 
    ethan closedbrow talking2mouth "Then again, nobody told me anything about this school in general..."

    bertha "I know this is all very exciting for you youngsters, so let's get the dull stuff out of the way.{w=0.5} I personally don't see the point in a syllabus, but the school sadly requires it."
    bertha "Let's all be patient and get through this quickly together."
    bertha "Take a syllabus and pass it along, please."

    pause 1.0

    bertha "Oh, dear. I don't think I've made enough copies.{w=0.5} Let me run to the office and get more."

    show berthabg:
        subpixel True
        alpha 1.0 xpos 960
        parallel:
            ease 1.5 xpos 980
        parallel:
            pause 1.0
            ease 0.5 alpha 0.0

    $ renpy.pause(2.0, hard=True)

    $ PlaySound("LightTap.ogg")

    show pencil:
        alpha 1.0 xpos 1050 ypos 500 zoom 4.0 rotate 0
        parallel:
            ease 0.15 rotate 360
            ease 0.15 rotate 0
            repeat
        parallel:
            ease 0.5 xpos 1000 ypos 400 zoom 0.75
            ease 0.75 xpos 900 ypos 800 zoom 0.25
        parallel:
            pause 0.75
            ease 0.5 alpha 0.0

    show groundclass behind pencil:
        xpos 0 zoom 1.0
        ease 0.1 zoom 1.15 xpos -50 ypos -100

    redmind surprised "Ow! What the...{w=0.5} is someone flinging pencils?!"

    show groundclass:
        zoom 1.15 ypos -100 xpos -50
        ease 0.5 zoom 1.0 xpos 0 ypos 0

    show brendan uniform surprised:
        alpha 0.0 zoom 1.2 xpos 1000 ypos 1.1
        ease 0.5 xpos 900 alpha 1.0

    brendan "Oh, man, really sorry about that!"

    brendan talking2mouth "Are you okay?{w=0.5} You're not bleedin' or anything are you?"
    
    red happy "I'm fine. It's only a pencil. Still, watch where you fling those things!"

    brendan closedbrow talkingmouth "Shoot, my bad, man.{w=0.5} It's kind of a bad habit of mine. Nervous fingers, y'know?"
    brendan -thinking @talkingmouth "When I get bored, I start spinnin' pencils. You know, like those guys do in the movies."
    brendan happybrow surprisedmouth sweat "And this one sort of got away from me. I'm usually a lot better at it!"
    show brendan happy -sweat with dis
    
    red -happy @talkingmouth "Well, keep practicing, then. We'll need your deadly skills when Hilbert acts up."

    brendan surprised "Oh, shoot, the teacher's comin' back. Talk to you later!"

    show brendan:
        xpos 900 alpha 1.0 ypos 1.1 zoom 1.2
        ease 0.3 xpos 1100 alpha 0.0

    hide groundclass

    pause 0.5

    show berthabg:
        subpixel True
        alpha 0.0 xpos 980
        parallel:
            ease 1.5 xpos 960
        parallel:
            pause 1.0
            ease 0.5 alpha 1.0

    bertha "Sorry for the wait, dears."
    bertha "Oh, I almost forgot!"
    
    show berthabg:
        xpos 960 alpha 1.0

    bertha "I made some sweets for you all."
    bertha "I have Lumiose Galettes, Shalour Sables, and Lava Cookies. Who wants some?"

    $ PlaySound("Snore_F3.ogg")
    $ renpy.pause(0.6, hard=True)

    $ PlaySound("Body Roll.ogg")

    show flannery uniform surprised:
        alpha 1.0 xpos -500 ypos 1.1 zoom 1.2
        ease 0.3 xpos 300 ypos 1.0

    flannery "Did someone say Lava Cookies?!"

    show brendan:
        xpos 1100 ypos 1.1 alpha 0.0 zoom 1.2
        ease 0.5 xpos 950 alpha 1.0

    show serena uniform surprised at rightside with dis

    serena "Lumiose Galette? I haven't had those since I was back in Kalos..."        
    brendan "Wow, they look great!"
    show flannery happy with dis
    show serena happy with dis

    show brendan happy:
        xpos 950 ypos 1.1 alpha 1.0 zoom 1.2
        
    brendan "I'm not big on sweets, but still, damn, this class is kick{w=0.2}ASS!"
    ethan happy "I'm so happy that I decided to take this class."
    red happy "I feel bad for everyone that decided not to take the Ground elective.{w=0.5} They missed out on something magical."

    show flannery:
        alpha 1.0 xpos 300 ypos 1.0 zoom 1.2
        ease 0.5 alpha 0.0

    hide serena at rightside with dis

    show brendan:
        xpos 950 ypos 1.1 alpha 1.0 zoom 1.2
        ease 0.5 alpha 0.0

    narrator "An hour passes quickly as you munch away and take notes."

    hide bertha
elif (not HasEvent("Instructor Bertha", 2.1) and classstats["Ground"] >= 10):#Burial Ground
    show bertha with dis
    if (not HasEvent("Instructor Bertha", 2)):
        $ renpy.pause(1.0, hard=True)

        narrator "The class is watching a dramatized movie about a battle fought a few years ago, in which the Legendary Pokémon Groudon was reported to appear."
        narrator "You are skeptical of the veracity of the movie, especially as the actors who claim to be everyman teens are clearly, at minimum, thirty-five."
        narrator "Instructor Bertha walks next to your chair and sits down, speaking quietly so as not to disturb the other students."

        bertha @norm4 "You look concerned, young man."

        red uniform @closedbrow talking2mouth "Maybe less concerned, and more confused."

        bertha @happy2 "Oh? Are you confused as to why Brycen's character is always shirtless?"

        red @happy "No, his pecs explain that one for me. He's pretty in-shape for an older guy. I'm just confused as to if this is true or not." 
        red @talking2mouth "I mean, it's obviously a dramatization, and it's pretty fun, but did this battle really happen?"

        bertha @surprised2 "Oh yes, absolutely. There's endless recorded footage of the event. The movie even intersperses actual footage with dramatizations."

        red @closedbrow talking2mouth "I did wonder why the camera went shaky so often."

        bertha @norm2 "Oh, that might just be the director's style. He's well-known for that sort of thing. Explosions, too."

        red @happy "Pardon me for saying this, Instructor Bertha, but I'm surprised you know so much about movies!"

        bertha @happy2 "Well, when you get to be an old duffer like me, you need to keep your mind active to stay grounded."
        bertha @norm2 "Let too much time pass without thinking about it, and you won't have any time left, dearie. Remember that."

        red @closedbrow talking2mouth "Hmm... so this movie {i}did{/i} actually happen..." 
        red @closedbrow talking2mouth "Those two Pokémon are legends. People didn't even think they were real, right? I mean, I know {i}a lot{/i} about Pokémon, and I'd only heard of them as myths." 
        red @happy "I feel like the world should have changed because of that, but it all seemed the same to me."
        red @surprised "I mean, I didn't even know about this! Two legends came to life, and fought each other?"

        bertha @happy2 "Hm... I think I recognize your accent. You're from Pallet Town, aren't you?"

        red @surprised "Huh? Well... yeah, I am. How do you know?"

        bertha sad @sad2 "I... used to visit frequently. My sister grew up there."

        red @sad "You look sad."

        bertha @sad2 "She's passed away."

        pause 1.0 

        bertha angry @angry2 "And hasn't had the common decency to pass {i}on{/i}, yet! What a bother she is."

        red @surprised "Huh?"

        bertha norm @happy2 "Oh, never mind that. I ask if you came from Pallet Town because it isn't the worldliest place. I'm not wholly surprised you're a little behind the times."

        red @sad "Oh... so I've got a lot of catching up to do, huh?"

        bertha @norm2 "Perhaps. I'm not sure that's necessary, though."

        red @closedbrow talking2mouth "What do you mean, Instructor?"

        bertha @happy2 "The world's a big one. There are so many legends and powers, myths and heroes, villains and curses, all buried right beneath us. And maybe they'll come back up someday."
        bertha @norm2 "It's impossible to know the world, you know. Even for an old duffer like me, with my many, many, years under my belt." 
        bertha @happy2 "But take it from this duffer--as long as you know the ground you plant your feet on, you're as prepared as you need to be."

        pause 2.0

        red @happy "Wow, Instructor Bertha. You're really wise."

        bertha @happy2 "It comes with age."

        red @talkingmouth "Do you mind if I ask another question?"

        bertha @norm2 "Oh? Go ahead."

        red @closedbrow talking2mouth "What lesson are we supposed to be getting from this movie? Is it that Ground-types are responsible for the world's formation?"
        red @surprised "Or, wait... Groudon is completely out of its element here... is it something about how if you're in someone else's arena, you should turn it into your own?"

        bertha @norm2 "No. I just like watching a younger man run around shirtless for an hour and a half."

        red @surprised "Uhhhhhh..."

        bertha @happy2 "But keep that one to yourself, alright? Besides, you've all been working so hard, you deserve a break. Popcorn?"

        red @closedbrow talking2mouth "Oh, no thanks. I just... Hm."
        red @talkingmouth "Um... I feel like I've gotten to know this class pretty well so far... do you think you'd be able to move me to the next level?"

        bertha @happy2 "Certainly. And I'm glad you asked."

        red @surprised "Huh. That easy, huh?"

        bertha @norm2 "Well, I was thinking the same thing. Didn't want to throw you in before you were ready, though."
        bertha @happy2 "Very well. I'll administer a little exam--a one-on-one battle--after the movie is over, and if you pass, I'll show you a move I bet you haven't seen before."

        red @surprised "A new move?"

        bertha @norm2 "Yes, one my sister and I developed together. It's called 'Burial Ground.' Apologies for the macabre name, she named it."

        red @closedbrow talking2mouth "What does it do...?"

        bertha @norm2 "Well, it sets up a terrain that affects the entire battlefield for five turns." 
        bertha @happy2 "Any grounded, not Ground or Ground-type Pokémon that stands on it will lose some speed and health at the end of the turn!"

        red @closedbrow talking2mouth "Huh... okay, I can see the implications there."

        bertha @norm2 "Splendid. Now, let's wait for this movie to come to an end, and then..."

        pause 2.0

        narrator "You wait until the movie finishes."

        red @happy "Alright, Instructor! I'm ready to take my exam!"

        $ AddEvent("Instructor Bertha", 2)
    else:
        red uniform @talking2mouth "Bertha, I've studied since the last time we fought--and now I'm more than ready to beat you."

    bertha @happy2 "Ah, it does me good to see young people like you so excited to learn. So which Pokémon will you be using? Here's a hint--{color=#0048ff}pick a Ground-type.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    bertha @norm2 "Ready, young man? I won't be holding back!"
    $ hidebattleui=False
    $ mustswitch = False
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("bertha", TrainerType.Enemy, [
        Pokemon(304, level=11, moves=[GetMove("Tackle"), GetMove("Harden"), GetMove("Metal Claw"), GetMove("Rock Tomb")], ability="Rock Head")
    ])
    call Battle([trainer1, trainer2], customexpressions=["red uniform", "red uniform angrybrow happymouth", "bertha norm", "bertha happy2"], reanchor=[False, True]) from _call_Battle_34
    $ battlehistory["Instructor Bertha1"]  = _return

    show bertha with dis

    if (WonBattle("Instructor Bertha1")):
        $ AddEvent("Instructor Bertha", 2.1)

        bertha @happy2 "Good show! You've done wonderfully. Victory treacle?"

        red uniform @sadeyes sadeyebrows happymouth "I probably shouldn't. They always get stuck between my teeth."

        $ passedclass = True

        jump aftertutorintroground
    
    else:
        bertha @sad2 "Oh, dear... Perhaps I went too hard, then?"
        bertha @happy2 "Don't let it get to you! I'm sure you can launch a splendid comeback."

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide bertha with dis
elif (not HasEvent("Instructor Bertha", 3.1) and classstats["Ground"] >= 20):#Soft Sand
    show bertha with dis
    if (not HasEvent("Instructor Bertha", 3)):
        $ renpy.pause(1.0, hard=True)
        
        $ lowertime = timeOfDay.lower()

        bertha @norm2 "Good [lowertime], [first_name]."

        red uniform @happy "Good [lowertime], Instructor!"

        bertha @sad2 "You look pale. Have you been eating well? Getting enough exercise?"

        red @talkingmouth "Absolutely. Don't worry about me."

        bertha @happy2 "Oh, don't spoil my fun. Pestering the young is half the fun of being old!"
        
        red @happy "Half? I {i}know{/i} that's not true, Instructor. You wouldn't be such a brilliant teacher if you didn't enjoy it!"

        bertha @norm2 "Well, you're very kind for saying that. But, really, what is teaching except worrying about the youth?"

        red @closedbrow talking2mouth "Hm. Not sure I know that one."

        bertha @norm4 "Maybe you'll be a teacher someday, and figure it out."

        red @happy "Maybe! I'm planning on being a Pokémon Champion, though."

        bertha @surprised2 "Well, don't forget you can be both. Just look at that strapping young man, Lance."

        redmind @confusedeyebrows frownmouth "Young? I mean, I guess he's not old, but he doesn't look good for his age... whatever his age is."

        bertha @norm2 "Anyway, I think it's about time you take another advancement exam for this class. You've been doing well enough, I think you're ready to move up a level."

        red @happy "Oh, really? Sweet! Thanks!"

        bertha @norm2 "Speaking of sweet, if you need a snack to keep your energy up for the exam, help yourself to these Poffins."

        red @confused "Aren't those Pokémon food?"

        bertha @happy2 "I won't tell if you don't."

        red @happy "Thanks, Instructor, but I'll pass. I'm ready to take the exam now."

        $ AddEvent("Instructor Bertha", 3)
    else:
        red uniform @talking2mouth "Instructor Bertha, I've trained and studied since our last battle, and I think I can do it this time."

    bertha @happy2 "So persistent! That's good to see. Now, you know what to do. {color=#0048ff}Pick just one Pokémon to fight my Ground-type.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    bertha @norm2 "Ready, [first_name]? I won't be holding back!"
    $ hidebattleui=False
    $ mustswitch = False
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("bertha", TrainerType.Enemy, [
        Pokemon("Hippopotas", level=21, moves=[GetMove("Crunch"), GetMove("Dig"), GetMove("Sand Tomb"), GetMove("Yawn")], gender=Genders.Male, ability="Sand Stream", item="Oran Berry")
    ])
    call Battle([trainer1, trainer2], customexpressions=["red uniform", "red uniform angrybrow happymouth", "bertha norm", "bertha happy2"], reanchor=[False, True]) from _call_Battle_94
    $ battlehistory["Instructor Bertha2"]  = _return

    show bertha with dis

    if (WonBattle("Instructor Bertha2")):
        $ AddEvent("Instructor Bertha", 3.1)

        bertha @happy2 "Well done once again! Here's a packet of Soft Sand. I made this ahead of time, since I figured you were going to be taking the exam any day now."

        $ GetItem("Soft Sand", 1, "You gained a Soft Sand! The pouch appears to be hand-embroidered, bearing your name.")

        $ renpy.pop_call()
        jump aftertutoring
    
    else:
        bertha @sad2 "Oh, dear... It seems I got a bit carried away."
        bertha @happy2 "Just remember--you're down but not out! There's plenty of time to try again."

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide bertha with dis
elif (not HasEvent("Instructor Bertha", 4.1) and classstats["Ground"] >= 30):#Bulldoze
    show bertha with dis
    if (not HasEvent("Instructor Bertha", 4)):
        $ renpy.pause(1.0, hard=True)

        bertha @norm2 "Good [lowertime], [first_name]."

        red uniform @happy "Good [lowertime], Instructor!"

        bertha @norm2 "I think it's about time you took this class' advancement exam. Do you agree?"

        red @surprised "Oh! Yes, definitely! Thank you."

        bertha @happy2 "Thank you for being such a good student. Does my old heart well to see my students understanding the material as well as you do."

        red @talkingmouth "You're a good teacher, Instructor Bertha. I wouldn't be getting it without you."

        bertha @norm2 "You flatter me, dearie. Now, are you ready to take the exam? This'll be a harder one, but you're a tough cookie, so I'm sure you can handle it."

        red @happy "I'm pretty sure I can do this, yeah!"

        $ AddEvent("Instructor Bertha", 4)
    else:
        red uniform @talking2mouth "Instructor Bertha, I've trained and studied since our last battle, and I think I can do it this time."

    bertha @happy2 "Let's begin this battle, then. {color=#0048ff}Pick just one Pokémon, but don't pick a Ground-type unless you want to have a bad time.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    bertha @norm2 "Fasten your seatbelt, kiddo--here I come!"
    $ hidebattleui=False
    $ mustswitch = False
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("bertha", TrainerType.Enemy, [
        Pokemon("Ducklett", level=31, moves=[GetMove("Roost"), GetMove("Air Slash"), GetMove("Bubble Beam"), GetMove("Aqua Ring")], ability="Keen Eye", item="Sitrus Berry")
    ])
    call Battle([trainer1, trainer2], customexpressions=["red uniform", "red uniform angrybrow happymouth", "bertha norm", "bertha happy2"], reanchor=[False, True]) from _call_Battle_95
    $ battlehistory["Instructor Bertha3"]  = _return

    show bertha with dis

    if (WonBattle("Instructor Bertha3")):
        $ AddEvent("Instructor Bertha", 4.1)

        bertha @happy2 "Very well done, youngster! With that, you've beaten a Pokémon that's good against Ground-types, one that's weak to Ground-types, and, of course, a Ground-type!"
        bertha @norm2 "Seems you're well-grounded in the basics. So, in future exams, I'll be using three Pokémon. I look forward to seeing how you excel there!"

        $ passedclass = True

        jump aftertutorintroground
    
    else:
        bertha @sad2 "Hm... Instructor Wallace {i}does{/i} train a mean Ducklett..."
        bertha @happy2 "Don't let it bother you! Just dust yourself off and focus on your next try."

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide bertha with dis

elif (FindGenericClassScene(True)):#generic scene
    $ renpy.call(FindGenericClassScene())
    hide bertha with dis
else:# _really_ generic scene
    show bertha with dis
    bertha "Hello, children! Please, come up to the front of the class, and get a snack, if you wish."
    hide bertha with dis
    show berthabg with dis
    bertha "Once you've done that, let's talk about Ground-types. Perhaps no other type has as much influence over our geography! Now, can anyone..."
    narrator "Class proceeds without incident."

return

label movetutorground:
show bertha with dis
bertha @norm2 "Oh, you'd like to teach your Ground-type a new move? Certainly, kiddo. I can do that in a jiffy."
bertha @norm2 "I can teach Burial Ground, which is a move my sister and I made that slows and damages all grounded non-Ground and non-Ghost types on the field for five turns."
if (HasEvent("Instructor Bertha", 4.1)):
    bertha @happy2 "If you want some more immediate power, why not try Bulldoze? It hits everything around you, and lowers their speed, too!"

label aftertutorintroground:
$ taughtmove = None

menu:
    ">Learn Burial Ground":
        $ taughtmove = "Burial Ground"
    ">Learn Bulldoze" if (HasEvent("Instructor Bertha", 4.1)):
        $ taughtmove = "Bulldoze"
    "Nevermind":
        bertha @surprised2 "Change your mind?"

        if (passedclass):
            $ renpy.pop_call()
            jump aftertutoring
        else:
            jump aftergroundsetup
python:
    hidebattleui = True
    renpy.transition(dissolve)
    newindex = renpy.call_screen("switch", MakeRed())
    if (newindex != "back"):
        newmon = playerparty[newindex]
    hidebattleui=False
if (newindex == "back"):
    bertha @surprised2 "Change your mind?"
elif (MonCanLearn(newmon, taughtmove)):
    $ newmon.LearnNewMove([(1, taughtmove)])
    if (taughtmove in newmon.GetMoveNames()):
        jump endclass
else:
    bertha @sad2 "Oh, dearie me. I don't think that Pokémon can learn [taughtmove], youngster."

jump aftertutorintroground

label itemcraftground:
show bertha with dis

bertha @happy2 "Items are always a good thing to have on-hand in battle! That goes for Pokémon {i}and{/i} trainers."
bertha @norm2 "If you want some Soft Sand, I've got some special geodes you can grind up. They boost the power of Ground-type attacks by 10%%!"

menu:    
    ">Craft Soft Sand" if (HasEvent("Instructor Bertha", 3.1)):
        $ GetItem("Soft Sand", 1, "You grind up a shining geode to make some sparkling, soft, sand.")
        jump endclasscraft
    "Nevermind":
        bertha @norm4 "Ah, your hands are full already? That's alright, youngster."
        jump aftergroundsetup
