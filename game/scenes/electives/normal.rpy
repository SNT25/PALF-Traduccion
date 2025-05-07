label normalelective:

$ renpy.transition(dissolve)
show screen currentdate

scene map
show blank2:
    alpha 0.8

show classroom with dis

show normtype with dis:
    xalign 0.5 yalign 1.0

$ location = "normal"
$ passedclass = False

############################################################################################################################################################################################################################
#### 13. NORMAL      #######################################################################################################################################################################################################
############################################################################################################################################################################################################################
$ renpy.pause(1.0, hard=True)

call ethanevent from _call_ethanevent_12

label afternormalsetup:

if (HasEvent("Instructor Lenora", 2.1)):
    menu:
        "{b}>General Studies{/b}":
            pass

        ">Ask for move tutoring":
            jump movetutornormal

        ">Craft items" if (HasEvent("Instructor Lenora", 3.1)):
            jump itemcraftnormal

if (not HasEvent("Instructor Lenora", 1)): #first class
    $ AddEvent("Instructor Lenora", 1)

    show lenora with dis:
        xpos 900
        ease 0.5 xpos 800

    lenora "All right, all right. Settle down, everyone."

    if (not IsDate(5, 4, 2004)):
        lenora "I see we have some new faces. Let's see... Ethan and [first_name], right?"
    
    $ BecomeNamed("Instructor Lenora")

    lenora @talkingmouth "I'm Lenora, and I'm your teacher for the {color=#0048ff}Normal-type class,{/color} which is the one you're in right now."
    lenora @happy "I don't consider myself a very strict teacher, so I don't have many class 'rules.'"
    lenora @talking2mouth "You can bring food, water, whatever, just as long as you clean up after yourselves."
    lenora @closedbrow talking2mouth "The only thing I won't allow are cellphones.{w=0.5} I see you kids staring at those things all day. You're gonna go blind!"
    lenora @talkingmouth "The way I see it, you're all adults, so I shouldn't have to tell you these things."

    hide lenora with dis

    show lenorabg with dis

    redmind "This lady sounds a lot like my mom."

    if (not IsDate(5, 4, 2004)):
        lenora "Now, the first thing I want to do is have the both of you tell the class something about yourselves."
    else:
        lenora "Now, the first thing I want to do is have each of you tell the class something about yourselves."

    lenora "Who would like to go first?"

    red uniform @talkingmouth "I'll go. I'm, uh, [first_name], and I'm from Pallet Town. It's a tiny town in the Southwest of Kanto."
    
    if (IsAfter(1, 5, 2004)):
        narrator "You hear a couple voices grumble in recognition, and discontent... you're pretty well-known to the student body already."

    ethan uniform @talkingmouth "Yeah! And, uh, I'm Ethan! I'm from New Bark Town. It's a tiny town in the Southeast of Johto."
    lenora "Oh, how cute. Seems you two have a lot in common, then. Welcome to our little Normal-type family!"

    redmind "The atmosphere in this room is really homey.{w=0.5} I haven't felt this relaxed in a classroom in a really long time."

elif (not HasEvent("Instructor Lenora", 2.1) and classstats["Normal"] >= 10):#Simple World
    show lenora with dis
    if (not HasEvent("Instructor Lenora", 2)):
        $ renpy.pause(1.0, hard=True)

        lenora @talkingmouth "[first_name]."

        red uniform @surprised "Hm? Instructor?"

        lenora @talkingmouth "I think you're ready to take your advancement exam for this class. It'll be a one-on-one battle."

        red @happy "Oh. Cool! Thanks. What does advancing mean for this class?"

        lenora @closedbrow talkingmouth "I'll be able to teach your Normal-types the move Simple World."

        red @closedbrow talking2mouth "Woah. That's an out-there name. What does it do?"

        lenora @talkingmouth "It puts a terrain on the field that makes all grounded Pokémon Normal-type for five turns."

        red @surprised "Huh. I can see how that could be useful for a Normal-type. Sure, I'm ready for that."

        lenora @happy "Good."

        $ AddEvent("Instructor Lenora", 2)
    else:
        red uniform @talking2mouth "Instructor Lenora, I've done a bit of studying, and I'm ready to retake my advancement exam."

    lenora @talkingmouth "Pick one Pokémon from your party to battle with. I'll be honest--{i}anything{/i} should be able to win this one."

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    lenora @angrybrow happymouth "Alright, let's begin!"
    $ hidebattleui=False
    $ mustswitch = False
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("lenora", TrainerType.Enemy, [
        Pokemon(129, level=11, moves=[GetMove("Splash")], ability="Swift Swim")
    ])

    call Battle([trainer1, trainer2]) from _call_Battle_36
    $ battlehistory["Instructor Lenora1"]  = _return

    show lenora with dis

    if (WonBattle("Instructor Lenora1")):
        $ AddEvent("Instructor Lenora", 2.1)

        lenora @happy "Great job! I'm sure this isn't the last time I'll see you advance."

        $ passedclass = True
        jump aftertutorintronormal
    
    else:
        lenora @sad "Ah, that's too bad. Well, you can retake the exam anytime. Just train a bit beforehand!"

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide lenora with dis
elif (not HasEvent("Instructor Lenora", 3.1) and classstats["Normal"] >= 20):#Silk Scarf
    show lenora with dis
    if (not HasEvent("Instructor Lenora", 3)):
        $ renpy.pause(1.0, hard=True)

        lenora @talkingmouth "[first_name]. Do you know how to use items in battle?"

        red uniform @talkingmouth "Yep. Each of my Pokémon has a Battle Bag, too."

        lenora @happy "Good to hear! I'll be teaching you how to make Silk Scarves, then."

        red @closedbrow talking2mouth "Silk Scarves?"

        lenora @talkingmouth "That's right. They're a special type of scarf that boosts the power of your Normal-type moves by 10%%. They're a lot cheaper to make than to buy!"

        red @happy "Nice. But I have to pass an advancement exam first, right?"

        lenora @happy "You catch on fast. Are you ready?"

        red @talkingmouth "Ready as I'll ever be."

        $ AddEvent("Instructor Lenora", 3)
    else:
        red uniform @talking2mouth "Instructor Lenora, I've done a bit of studying, and I'm ready to retake my advancement exam."

    lenora @talkingmouth "Pick one Pokémon from your party to battle with. [bluecolor]I'll be using a Normal-type.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    lenora @happy "Ready, [first_name]?"

    $ hidebattleui=False
    $ mustswitch = False
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("lenora", TrainerType.Enemy, [
        Pokemon("Watchog", level=21, moves=[GetMove("Hypnosis"), GetMove("Crunch"), GetMove("Retaliate"), GetMove("Sand Attack")], ability="Illuminate", item="Oran Berry")
    ])

    call Battle([trainer1, trainer2]) from _call_Battle_98
    $ battlehistory["Instructor Lenora2"]  = _return

    show lenora with dis

    if (WonBattle("Instructor Lenora2")):
        $ AddEvent("Instructor Lenora", 3.1)

        lenora @happy "Alright! That's exactly what I want to see."

        $ GetItem("Silk Scarf", 1, "Lenora hands you a Silk Scarf. Its fabric has a strangely cooling effect.")
        $ renpy.pop_call()
        jump aftertutoring
    
    else:
        lenora @sad "Don't take it too hard--every defeat is just part of the learning process."

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide lenora with dis
elif (not HasEvent("Instructor Lenora", 4.1) and classstats["Normal"] >= 30):#Covet
    show lenora with dis
    if (not HasEvent("Instructor Lenora", 4)):
        $ renpy.pause(1.0, hard=True)

        lenora @talkingmouth "[first_name]."

        red uniform @surprised "Hm? Instructor?"

        lenora @closedbrow talking2mouth "I want to give you another advancement exam."

        red @happy "Oh, really? I feel like I just took the previous one, though."

        lenora @happy "Look, these early exams aren't meant to be hard. They're meant to help you grasp the fundamentals, since so many Pokémon start out Normal-type."

        red @talkingmouth "Well, I think it's achieving that for me."
        red @talkingmouth "What do I get if I pass this advancement exam?"

        lenora @talkingmouth "A pat on the back. And access to the move Covet."

        red @closedbrow talking2mouth "Covet?"

        lenora @talking2mouth "It's a Normal-type version of the move 'Thief.'"

        red @surprised "Oh. I think I knew that, actually. Um... okay."

        pause 1.0

        lenora @talking2mouth "So. Ready for the exam?"

        red @happy "Sure am!"

        $ AddEvent("Instructor Lenora", 4)
    else:
        red uniform @talking2mouth "Instructor Lenora, I've done a bit of studying, and I'm ready to retake my advancement exam."

    lenora @talkingmouth "Pick one Pokémon from your party to battle with. [bluecolor]Using a Normal-type will make this battle a lot harder on you.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    lenora @talkingmouth "Don't get cocky, now..."
    $ hidebattleui=False
    $ mustswitch = False
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("lenora", TrainerType.Enemy, [
        Pokemon("Aron", level=31, moves=[GetMove("Iron Head"), GetMove("Rock Slide"), GetMove("Protect"), GetMove("Headbutt")], ability="Study", item="Sitrus Berry")
    ])

    call Battle([trainer1, trainer2]) from _call_Battle_99
    $ battlehistory["Instructor Lenora3"]  = _return

    show lenora with dis

    if (WonBattle("Instructor Lenora3")):
        $ AddEvent("Instructor Lenora", 4.1)

        lenora @happy "Great job! After finishing this exam, you've beaten both a Normal-type and a Pokémon that Normal-types have trouble with."

        pause 1.0

        lenora @sad "Oh, and a Magikarp."

        pause 0.5

        lenora @talkingmouth "Anyway, you clearly have an understanding of the fundamentals, so it's time to crank things up a bit. Next time I'll be using three Pokémon, and I'll expect you to bring the same."

        $ passedclass = True
        jump aftertutorintronormal
    
    else:
        lenora @closedbrow talkingmouth "You're really getting somewhere, [first_name]--let me know when you're ready for another shot!"

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide lenora with dis

elif (FindGenericClassScene(True)):#generic scene
    $ renpy.call(FindGenericClassScene())
    hide lenora with dis
else:# _really_ generic scene
    show lenora with dis
    lenora @happy "[timeOfDay], dears! Let's all buckle down and work hard today!"
    lenora @talkingmouth "Now, before class begins, why don't we all say something nice that happened to us since our last class?"
    hide lenora with dis
    show lenorabg with dis
    narrator "Class proceeds without incident."

return

label movetutornormal:
show lenora with dis
lenora @surprisedbrow talking2mouth "You'd like me to teach your Pokémon a Normal-type move? Alright. Sure. Which one?"
lenora @talkingmouth "I can teach Simple World. That move sets a terrain for five turns that makes all normaled Pokémon become Normal-type."
if (HasEvent("Instructor Lenora", 4.1)):
    lenora @talkingmouth "If that's too niche for you, I can also teach Covet. It's just a Normal-type Thief. Steals the opponent's item, if you can."

label aftertutorintronormal:
$ taughtmove = None

menu:
    ">Learn Simple World":
        $ taughtmove = "Simple World"
    ">Learn Covet" if (HasEvent("Instructor Lenora", 4.1)):
        $ taughtmove = "Covet"
    "Nevermind":
        lenora @talkingmouth "Okay."

        if (passedclass):
            $ renpy.pop_call()
            jump aftertutoring
        else:
            jump afternormalsetup
python:
    hidebattleui = True
    renpy.transition(dissolve)
    newindex = renpy.call_screen("switch", MakeRed())
    if (newindex != "back"):
        newmon = playerparty[newindex]
    hidebattleui=False
if (newindex == "back"):
    lenora @talkingmouth "Okay."
elif (MonCanLearn(newmon, taughtmove)):
    $ newmon.LearnNewMove([(1, taughtmove)])
    if (taughtmove in newmon.GetMoveNames()):
        jump endclass
else:
    lenora @sad "I can't teach that Pokémon that move, sorry."

jump aftertutorintronormal

label itemcraftnormal:
show lenora with dis

lenora @closedbrow talking2mouth "Items are just as important a part of battle as anything else. When I'm out in the field, digging up fossils, I always make sure my Pokémon are wearing their Rocky Helmets."
lenora @talkingmouth "Now, if you want to boost your Normal-type Pokémon's attack by 10%%, I recommend the Silk Scarf. They're made of a special fabric that concentrates-- well, you don't need to hear that. Just trust me, they work."

menu:    
    ">Craft Silk Scarf" if (HasEvent("Instructor Lenora", 3.1)):
        $ GetItem("Silk Scarf", 1, "You silently plug away at a sewing machine as you sew the pieces of fabric that make up the scarf. When done, it's light, airy, and stylish.")
        jump endclasscraft
    "Nevermind":
        lenora @talkingmouth "Fine."
        jump afternormalsetup