label rockelective:

$ renpy.transition(dissolve)
show screen currentdate

scene map
show blank2:
    alpha 0.8

show classroom with dis

show rocktype:
    alpha 0.0 xalign 0.5 yalign 1.0
    ease 0.5 alpha 1.0

$ location = "rock"
$ passedclass = False

############################################################################################################################################################################################################################
#### 13. Rock        #######################################################################################################################################################################################################
############################################################################################################################################################################################################################
$ renpy.pause(1.0, hard=True)

call hildaevent from _call_hildaevent_1
call beaevent from _call_beaevent_1
call nessaevent from _call_nessaevent
call ethanevent from _call_ethanevent_15

label afterrocksetup:

if (HasEvent("Instructor Olivia", 2.1)):
    menu:
        "{b}>General Studies{/b}":
            pass

        ">Ask for move tutoring":
            jump movetutorrock

        ">Craft items" if (HasEvent("Instructor Olivia", 3.1)):
            jump itemcraftrock

if (not HasEvent("Instructor Olivia", 1)): #first class
    $ AddEvent("Instructor Olivia", 1)
    $ renpy.pause(1.0, hard=True)

    show olivia with dis

    olivia @talkingmouth "Hello, students."

    ethan uniform surprised "(Holy crap, she's gorgeous!)"

    olivia @talking2mouth "I heard that. What's your name?"

    ethan "Uh... Ethan, Ma'am!"

    olivia @closedbrow talking2mouth "Ethan. Well, I'd like to make something clear to you."

    pause 1.0

    hide olivia with dis
    show oliviabg with dis

    olivia "I really needed that. Thank you."

    ethan "E-eh? Uh, you're... you're welcome, Missus...?"

    $ BecomeNamed("Instructor Olivia")
    olivia "Olivia. {i}Just{/i} Olivia, and definitely not Missus. Not ever, with my luck."

    redmind uniform closedbrow frownmouth "I think our teacher needs therapy..."

    olivia @angry "What am I doing wrong? I stay in shape. I've got a fancy job and an empty ring finger. There's only one explanation..."

    olivia @sad "...Which brings me back to Rock-types. You know 'em; you... probably don't love 'em. They're hard. Solid. Unbreakable. Unlike my heart..."

    show nessa uniform at rightside with dis
    show bea uniform with dis
    show hilda uniform at leftside with dis

    olivia "Now, here's the thing about Rock-types. Despite their reputation as strong defenders, almost all of the strong ones focus mainly on offense."
    olivia @talking2mouth "Can anyone think of why that might be?"

    hilda @talkingmouth "Is it that Rock-types have unfavorable elemental matchups against several powerful types?"

    olivia @talkingmouth "Yes, that's right. Rock can be destroyed by Fighting, Water, and Ground, easily. That's not even mentioning Grass and Steel."
    olivia "With so many weaknesses to powerful types, one might wonder why you'd even want to train Rock-types..."
    olivia @talking2mouth "...Anyone?"

    bea @talkingmouth "Their offensive prowess is unmatched."
    
    olivia "Well, matched by Fighting, maybe, but yes. Despite how many of them present themselves, the best strategy for a Rock-type is to hit fast, hard, and get out."

    pause 1.0

    olivia "Just like my exes..."

    show nessa sad with dis
    show bea sad with dis
    show hilda sad with dis

    red @talkingmouth "Oh boy. This is going to be a depressing class."

    hide nessa uniform at rightside with dis
    hide bea uniform with dis
    hide hilda uniform at leftside with dis

    narrator "Despite Olivia's pitiable mood, you learn quite a bit about battling with Rock-type Pokémon."

    hide olivia
elif (not HasEvent("Instructor Olivia", 2.1) and classstats["Rock"] >= 10):#Splinter Shield
    show olivia with dis
    if (not HasEvent("Instructor Olivia", 2)):
        hide olivia with dis

        $ renpy.pause(1.0, hard=True)

        show oliviabg with dis

        narrator "Rock class began five minutes ago, but Instructor Olivia is still sitting behind her desk, staring blankly out at the class."

        redmind uniform @thinking "...Well, I guess she had a bad date last night."

        redmind @thinking "Still. It must have been a {i}really{/i} bad one. Normally she snaps out of it before class begins."

        red @sadeyes sadeyebrows talkingmouth "Hey... Ms. Olivia?"

        olivia "[ellipses]"

        red @surprised "Ms. Olivia!"

        olivia "Oh? Oh. Oh, yes. Right, Rock class..."

        red @sad "Are you alright, Instructor?"

        olivia "...Like {i}that{/i} even matters. I've got a job to do."

        hide oliviabg with dis

        pause 2.0

        show olivia frownmouth with dis

        red @happy "Um, if it makes you feel any better, I think you're doing really well at your job! Like, I definitely know way more about Rock-types than I did before!"

        olivia @talking2mouth "...What's your name?"

        redmind @thinking "Ow."

        red @talkingmouth "[first_name] [last_name], Ms. Olivia."

        olivia @closedbrow talking2mouth "And how old are you?"

        red @surprised "Uh..."

        olivia @sad "No, nevermind. {size=25}I'm not that desperate yet.{/size} [first_name], you've been doing pretty well in this class so far, so I think you can take the advancement exam."

        red @happy "Really? Awesome, thank you!"

        olivia @talking2mouth "It's a one-on-one battle, so both Pokémon will be fighting against each other alone."

        olivia sad "Always alone..."

        pause 2.0

        red @surprised "Um. And what happens if I win?"

        olivia -sad @talking2mouth "Oh. I'll teach you Splinter Shield. It protects your Pokemon for a turn. And if the shield is hit by a contact move, sharp, rocky shards cover the opponent's field."

        red @closedbrow talking2mouth "I'd never heard of that move before."

        olivia @surprised "I invented it. To impress a guy back home. He was a move fanatic."

        pause 1.0

        olivia @sad "...And married, it turned out."

        red @talkingmouth "Oof."

        $ AddEvent("Instructor Olivia", 2)
    else:
        red uniform @talking2mouth "Ms. Olivia, I've trained some more. I'm pretty sure I can win this time, if you'd let me try again."

    olivia @talking2mouth "Okay. Let's get this battle over with, so you can advance. {color=#0048ff}You're going to want to pick a Rock-type.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    olivia @sad "Don't let me down..."
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("olivia", TrainerType.Enemy, [
        Pokemon(165, level=11, moves=[GetMove("Tackle"), GetMove("Supersonic"), GetMove("Swift")], ability="Early Bird")
    ])

    call Battle([trainer1, trainer2]) from _call_Battle_39
    $ battlehistory["Instructor Olivia1"]  = _return

    show olivia with dis

    if (WonBattle("Instructor Olivia1")):
        $ AddEvent("Instructor Olivia", 2.1)

        olivia @talkingmouth "Okay. Good job. {size=25}See, Olivia? At least you're still good at your job...{/size}"

        $ passedclass = True
        jump aftertutorintrorock
    
    else:
        olivia frownmouth @sad "Oh, no... am I getting worse at teaching?"

        red uniform @surprised "N-no, Miss! I'm just a dumbass, honest!"

        redmind @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide olivia with dis
elif (not HasEvent("Instructor Olivia", 3.1) and classstats["Rock"] >= 20):#Hard Stone
    show olivia with dis
    if (not HasEvent("Instructor Olivia", 3)):

        narrator "Rock Class is wrapping up, and you're coming to the end of the lesson, when you notice Instructor Olivia is somewhat aimlessly meandering in the corner of the room."

        redmind uniform @confused "{w=0.5}.{w=0.5}.{w=0.5}."

        red @talkingmouth "Instructor Olivia?"

        olivia @talkingmouth "Hm?"

        red @closedbrow talking2mouth "I was just wondering about those crystals you're wearing."

        olivia @closedbrow talking2mouth "{w=0.5}.{w=0.5}.{w=0.5}.I've heard that line before."

        red @sweat closedbrow talking2mouth "Oh, yeah, it does kinda sound like a line, doesn't it?"

        olivia @talkingmouth "They're just rocks. Minerals. No special powers. They don't influence my chakras, they don't heal. They're just rocks."

        pause 1.0

        red @closedbrow talking2mouth "Well, as a Rock-type specialist..."

        olivia @sad "Yeah. I'm expected to wear rocks, aren't I? I've spent so much time, so many years, studying rocks, that unless I physically {i}wear{/i} them all the time, it's just a waste."
        olivia @closedbrow talking2mouth "...Though it might have been a waste already."
        olivia @talkingmouth "If I could go back in time and tell young Olivia one thing... and I {i}wasn't{/i} going to tell her which dates to avoid... I'd tell her to study something, {i}anything{/i} other than rocks."

        pause 1.0

        olivia @closedbrow talking2mouth "{i}Sigh.{/i}"

        pause 1.0

        olivia @talkingmouth "You're doing well-enough, though. Just don't get too into it."

        red @confused "Um. Okay."

        olivia @talkingmouth "I'll give you this class' advancement exam. If you pass, you can have a Hard Stone, and I'll let you extract more of them in future classes. I have a whole stack of geodes underneath my desk."
        olivia @sad "Rocks with rocks in them..."

        red @closedbrow talking2mouth "Why would I want a Hard Stone?"

        olivia @talkingmouth "Beats me. But they {i}do{/i} increase the power of Rock-type moves by 10%%."

        pause 1.0

        olivia @sad "{i}Sigh.{/i}"

        olivia @talkingmouth "Are you ready?"

        red @confused "Ready as I can be."

        $ AddEvent("Instructor Olivia", 3)
    else:
        red uniform @talking2mouth "Ms. Olivia, I've trained some more. I'm pretty sure I can win this time, if you'd let me try again."

    olivia @closedbrow talkingmouth "Okay. Let's get this battle over with, so you can advance. {color=#0048ff}I'm using, big surprise, a Rock-type.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    olivia @sad "Here we go again..."
    $ hidebattleui=False
    $ mustswitch = False
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("olivia", TrainerType.Enemy, [
        Pokemon("Rockruff", level=21, moves=[GetMove("Bite"), GetMove("Howl"), GetMove("Rock Throw"), GetMove("Double Team")], ability="Keen Eye", item="Oran Berry")
    ])

    call Battle([trainer1, trainer2]) from _call_Battle_105
    $ battlehistory["Instructor Olivia2"]  = _return

    show olivia with dis

    if (WonBattle("Instructor Olivia2")):
        $ AddEvent("Instructor Olivia", 3.1)

        olivia @talkingmouth "Well, I guess that's good enough. Here's your rock, for whatever it's worth."

        $ GetItem("Hard Stone", 1, "Instructor Olivia limply drops a Hard Stone into your hands.")

        $ renpy.pop_call()
        jump aftertutoring
    
    else:
        olivia frownmouth @sad "Let me guess. You're gonna want a rematch?"

        redmind @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide olivia with dis
elif (not HasEvent("Instructor Olivia", 4.1) and classstats["Rock"] >= 30):#Rock Tomb
    show olivia with dis
    if (not HasEvent("Instructor Olivia", 4)):
        
        olivia frownmouth @talking2mouth "...[first_name], do you ever have one of those days where everything just seems to be going really slowly? Like you're trapped underneath a heavy blanket, and no matter how much you move, you can't shake it off?"

        pause 2.0

        redmind uniform @confusedeyebrows frownmouth "Who the hell starts a conversation like that?!"

        red @talkingmouth "Uh. Yes, occasionally. Mondays, usually."

        olivia @closedbrow talking2mouth "...I see."

        pause 1.0

        olivia @closedbrow talking2mouth "Well, I need to keep moving. Can't let myself be slowed down."
        olivia @talkingmouth "Do you want to take this class' advancement exam? If you pass, I'll teach you the move Rock Tomb. It slows a foe. ...Ironically."

        red @surprised "Oh! Yes, absolutely."

        redmind @thinking "I don't think that's actually irony, though."

        olivia @sad "Great."

        $ AddEvent("Instructor Olivia", 4)
    else:
        red uniform @talking2mouth "Ms. Olivia, I've trained some more. I'm pretty sure I can win this time, if you'd let me try again."

    olivia @talking2mouth "Okay. Let's get this battle over with, so you can advance. {color=#0048ff}Don't pick a Rock-type.{/color} That's something I should have said to myself twenty years ago..."

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    olivia @sad "Just... one more day..."
    $ hidebattleui=False
    $ mustswitch = False
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("olivia", TrainerType.Enemy, [
        Pokemon("Quagsire", level=31, moves=[GetMove("Yawn"), GetMove("Slam"), GetMove("Mud Shot"), GetMove("Water Gun")], ability="Oblivious", item="Sitrus Berry")
    ])

    call Battle([trainer1, trainer2]) from _call_Battle_106
    $ battlehistory["Instructor Olivia3"]  = _return

    show olivia with dis

    if (WonBattle("Instructor Olivia3")):
        $ AddEvent("Instructor Olivia", 4.1)

        olivia @closedbrow talking2mouth "Okay. Good job. Now, you've beaten a Rock-type, a Pokémon that's good against Rock-types, and a Pokémon that's weak to Rock-types."
        olivia @talkingmouth "Since you've got a rock-solid understanding of the basics, I'll..."

        pause 1.0

        olivia @surprised "God. Did I just make a rock pun? Is that how far I've fallen?"

        pause 1.0

        olivia @sad "Anyway. For future exams, I'll be using three Pokémon at once. Yay... more rocks..."

        $ passedclass = True
        jump aftertutorintrorock
    
    else:
        olivia @sad "Yeah... I think we were both expecting more out of that."

        redmind @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide olivia with dis

elif (FindGenericClassScene(True)):#generic scene
    $ renpy.call(FindGenericClassScene())
    hide olivia with dis
else:# _really_ generic scene
    show olivia with dis
    olivia @talkingmouth "Hello, all. Do anything fun since our last class?"
    olivia @sad "...Nevermind, don't tell me. That'd just depress me further."
    hide olivia 
    show oliviabg 
    with dis
    narrator "Class proceeds without incident."

return

label movetutorrock:
show olivia with dis
olivia @surprisedbrow talking2mouth "You want me to teach one of your Pokémon a move? Alright, I guess..."
olivia @talking2mouth "I can teach Splinter Shield. It protects you from damage, and puts sharp rocky shards on the opponent's field, if it's hit by a contact move."
if (HasEvent("Instructor Olivia", 4.1)):
    olivia @closedbrow talking2mouth "If that's too passive, there's Rock Tomb. It'll lower your foe's speed... making it even harder for them to get where they want to be."

label aftertutorintrorock:
$ taughtmove = None

menu:
    ">Learn Splinter Shield":
        $ taughtmove = "Splinter Shield"
    ">Learn Rock Tomb" if (HasEvent("Instructor Olivia", 4.1)):
        $ taughtmove = "Rock Tomb"
    "Nevermind":
        olivia @sad "Yeah, that's probably for the best."

        if (passedclass):
            $ renpy.pop_call()
            jump aftertutoring
        else:
            jump afterrocksetup
python:
    hidebattleui = True
    renpy.transition(dissolve)
    newindex = renpy.call_screen("switch", MakeRed())
    if (newindex != "back"):
        newmon = playerparty[newindex]
    hidebattleui=False
if (newindex == "back"):
    olivia @sad "Yeah, that's probably for the best."
elif (MonCanLearn(newmon, taughtmove)):
    $ newmon.LearnNewMove([(1, taughtmove)])
    if (taughtmove in newmon.GetMoveNames()):
        jump endclass
else:
    olivia @surprised "...Huh? No, I... that Pokémon, I don't know... sorry."

jump aftertutorintrorock

label itemcraftrock:
show olivia with dis

olivia @surprised "...You want rocks? Sure, I got rocks. I've got some large rocks here. And if you break them apart, there might be smaller, more useful, rocks inside."
olivia @talking2mouth "The most common kind of rock is the Hard Stone. They boost Rock-type moves by 10%%. Woo. Rocks."

menu:    
    ">Excavate Hard Stone" if (HasEvent("Instructor Olivia", 3.1)):
        $ GetItem("Hard Stone", 1, "You take a chisel to a large slab of rock and extract its diamond-hard core.")
        jump endclasscraft
    "Nevermind":
        olivia "I {i}do not{/i} blame you."
        jump afterrocksetup
