label iceelective:

$ renpy.transition(dissolve)
show screen currentdate

scene map
show blank2:
    alpha 0.8

show classroom with dis

show icetype:
    alpha 0.0 xalign 0.5 yalign 1.0
    ease 0.5 alpha 1.0
show iceglow:
    alpha 0.5 xalign 0.5 yalign 1.0
    block:
        ease 2.0 alpha 0.25
        ease 1.8 alpha 0.7
        repeat

$ location = "ice"
$ passedclass = False

############################################################################################################################################################################################################################
#### 13. Ice       #######################################################################################################################################################################################################
############################################################################################################################################################################################################################
$ renpy.pause(1.0, hard=True)

call ethanevent from _call_ethanevent_11
call dawnevent from _call_dawnevent_2
call grushaevent from _call_grushaevent_1

label aftericesetup:

if (HasEvent("Instructor Melony", 2.1)):
    menu:
        "{b}>General Studies{/b}":
            pass

        ">Ask for move tutoring":
            jump movetutorice

        ">Craft items" if (HasEvent("Instructor Melony", 3.1)):
            jump itemcraftice

if (not HasEvent("Instructor Melony", 1)): #first class
    $ AddEvent("Instructor Melony", 1)
    $ renpy.pause(1.0, hard=True)

    ethan uniform surprised "Man, it's chilly!"
    red uniform happy "Someone's committed to their theme!"

    show hilbert uniform at rightside with dis

    show misty uniform at leftside with dis

    red @thinking "[ellipses]"

    red @talkingmouth "Looks like we're getting... a bit of a chilly reception."
    ethan happy "Yeah, I think they're giving us the cold shoulder!"

    hide hilbert at rightside with dis
    hide misty at leftside with dis

    red @talkingmouth "I guess we can't expect to have an ice time here?"
    ethan "Oh, hail no."
    red @talkingmouth "Hahaha!"
    ethan -happy @talkingmouth "Hah. C'mon, let's--"

    show dawn uniform happy
    show classroom with vpunch

    dawn "Icy what you did there!"

    ethan closedbrow frownmouth "[ellipses]"
    red thinking "[ellipses]"

    dawn sad "...Oh, no, I killed it, didn't I?"
    red @talkingmouth "Uh... well, it wasn't the most graceful of--"
    dawn surprised "Glacial! Glacial sounds like graceful. I..."
    
    pause 1.0

    dawn sad "{size=30}Why am I like this?{/size}"

    show dawn:
        ease 0.3 xpos 1.5

    ethan "{i}Sigh.{/i} I wish I could say that that's the first woman that's {i}literally{/i} run away from me today, but..."
    red @talkingmouth "Well, I'm going to go check in on Hilbert."
    ethan closedbrow happymouth "Your funeral!"

    hide hilbert

    pause 1.0

    red @talkingmouth "Hey, Hilbert."

    show hilbert uniform at rightside with dis

    hilbert "Oh...{w=0.5} [first_name]."
    hilbert "I didn't expect to see you here."

    red @talkingmouth "Well, it seemed kind of interesting.{w=0.5} I know you're taking it because 'it's the best' or whatever..."
    hilbert sad "[ellipses]"
    hilbert closedbrow "Well, you're more tolerable than Ethan."
    red @angrybrow talking2mouth "Flattered."

    hide hilbert at rightside with dis

    show melony:
        xpos 800 alpha 0.0
        parallel:
            ease 1.0 xpos 750
        parallel:
            ease 0.5 alpha 1.0

    hide hilbert
    hide misty

    melony @happy "Sweethearts! Sooooo happy to see you all here looking hale and hearty."
    melony @closedbrow happymouth "Or should I say hail and hearty? Ooh, that's a good one."
    misty uniform closedbrow "Ice puns are so lazy."

    if (not (calDate.month == 4 and calDate.day == 5)):
        melony @surprised "Oh? I see we have some scrumptious new faces. What're your names, my darling popsicles?"
    else:
        melony @surprised "How lovely to see so many scrumptious new faces. What're your names, my darling popsicles?"
    
    redmind "...Scrumptious popsicles? Is she going to teach us, or eat us?"
    ethan "Hey! I'm Ethan, this guy's [first_name]."
    $ BecomeNamed("Instructor Melony")
    melony @happy "Now, isn't that just darling! Momma Melony's so happy to have you join her."

    melony @talkingmouth "I hope you enjoy my class! If you have any concerns, please feel free to join me in my office hours."
    misty "Are your office hours held in here?"
    melony @happy "Yes! But there's hot chocolate!"
    red @talkingmouth "Sounds like a good deal."

    melony @talkingmouth "Now, why don't we all go through the roll call? Let's see, the attendance sheet must be somewhere in all this fluff..."

    narrator "Melony begins digging through her puffy coat, looking for the attendance sheet."
    narrator "As she does so, you hear a scornful scoff from Hilbert's location."

    hide hilbert
    show hilbertintro:
        subpixel True
        alpha 0.0 xalign 0.5 zoom 1.0
        parallel:
            ease 0.5 alpha 1.0
        parallel:
            ease 5.0 zoom 0.75

    hide melony

    hilbert uniform sad "...Pathetic."
    melony @sad "Oh? Is there something wrong, sweetheart?"
    hilbert -sad @talkingmouth "We're seven minutes into the class, and all you've done is tell a lame pun and admit you don't know where your attendance sheet is."
    hilbert @angrybrow talking2mouth "Is this really the look you want to present to new students?"
    melony @sad "Oh, Hilbert, sweetie, why do you say such hurtful things? Maybe I don't have the most rock-solid head, but I just want to mother all of you kids!"

    hilbert sad "Ugh. The last thing I need is {i}another{/i} mother."

    melony @sad "Oh... Hilbie, you're so mean..."

    narrator "You and your classmates spend the rest of the class trying to console the disconsolate Melony."

    hide melony
    hide hilbertintro with dis
elif (not HasEvent("Instructor Melony", 2.1) and classstats["Ice"] >= 10):#Slow Freeze
    show melony with dis
    if (not HasEvent("Instructor Melony", 2)):
        $ renpy.pause(1.0, hard=True)

        red uniform @talkingmouth "Mrs. Melony?"

        melony @happy "Yes, my scrumptious little popsicle?"

        red @surprised "Um..."
        red @closedeyes talking2mouth "Well, I was just thinking. I've been taking this class for a while now, and I'm wondering what else there is."

        melony @surprised "What... else there is?"

        red @talkingmouth "Yeah. Like, when can I advance?"

        melony @sadbrow happymouth "Oh, darling, why would you want to? You're doing so well right now!"

        red @surprised "Huh? I mean, yeah, I guess... but I want to do better. I want to be challenged, you know?"

        melony frownmouth @sad "Oh, no... you're trying to finish the class fast, so you don't need to spend time with Momma Melony anymore..."

        pause 2.0

        red @angrybrow talking2mouth "That's {i}definitely{/i} not it, Instructor. I just want--"

        melony tears frownmouth @closedbrow tears "I'm sorry! I know I might be overbearing, but I just love you all so much! Can you blame me for wanting to keep you with me?"

        red @confusedeyebrows talking2mouth "I mean... no judgement, but, as a teacher, I feel like you kinda need to let students move on? That seems like an important part of a teacher's job."

        melony @sad "Oh... I wish I was good at that. But I never have been. I tried to keep my children by me for too long, and I hate to let any student leave... I'm so awful at letting go."
        melony @happy "I wish I could just {i}freeze{/i} us all together, so nothing would ever change, and we'd always be close."

        redmind @surprised "Uh... okay. That's some serious attachment issues there."

        red @happy "Well, I promise I won't leave this class until you've taught me absolutely everything you can."
        red @closedeyes talking2mouth "...But that {i}does{/i} mean you need to start teaching some new material."

        melony -tears @closedbrow talking2mouth "Ohhh... alright, alright."

        pause 1.0

        melony @talking2mouth "I'll give you this class' advancement exam. It'll be a one-on-one battle. And, if you pass that, then I'll teach you something new."

        red @happy "Specifically?"

        melony @talkingmouth "I'll teach your Ice-types the special move {i}Slow Freeze{/i}!"

        red @closedbrow talking2mouth "I'm not familiar with that, I think."

        melony @happy "Oh, it's a move that leaves the enemy frozen. You'll move after everyone else, but it's the only way to guarantee a frozen opponent!"

        red @closedeyes talkingmouth "Huh. Okay, yeah. It's odd that there aren't any other ways to do that, isn't it?"

        melony @closedbrow talking2mouth "Well, freezing {i}is{/i} a very powerful status."

        red @happy "Well, I'm not going to freeze now! Let me show you a scorching-hot battle!"

        $ AddEvent("Instructor Melony", 2)
    else:
        red uniform @talking2mouth "Mrs. Melony, I'm ready to retake my advancement exam. And I {i}will{/i} advance this time."

    melony @sadbrow happymouth"Oh, my delicious gelato... you're growing up too fast. Which Pokémon are you going to use, though? {color=#0048ff}Momma Melony recommends you pick an Ice-type.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    melony @angrybrow happymouth "Prove to me you are strong enough to survive!"
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("melony", TrainerType.Enemy, [
        Pokemon(207, level=11, moves=[GetMove("Poison Sting"), GetMove("Sand Attack"), GetMove("Harden")], ability="Hyper Cutter")
    ])

    call Battle([trainer1, trainer2], uniforms=[True, False]) from _call_Battle_35
    $ battlehistory["Instructor Melony1"]  = _return

    show melony with dis

    if (WonBattle("Instructor Melony1")):
        $ AddEvent("Instructor Melony", 2.1)

        pause 2.0

        melony closedbrow sadmouth tears cry "*Sniff.* W-well done... popsicle..."
        red uniform @sadeyes sadeyebrows talkingmouth "Aw, Mrs. Melony... don't cry..."

        $ passedclass = True
        jump aftertutorintroice
    
    else:
        melony @happy "Aw! I suppose that means you'll be staying here with me for a bit longer, then."

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide melony with dis
elif (not HasEvent("Instructor Melony", 3.1) and classstats["Ice"] >= 20):#Never-Melt Ice
    show melony with dis
    if (not HasEvent("Instructor Melony", 3)):
        show melony sadbrow frownmouth with dis

        $ renpy.pause(1.0, hard=True)

        red uniform @talkingmouth "Mrs. Melony?"

        melony @happymouth "Yes, my popsicle?"

        red @closedbrow talking2mouth "You've been looking at that picture for a while now. Staring at it pretty intently."

        melony -sadbrow @closedbrow surprisedmouth "Oh, yes. Just reliving some memories..."

        pause 1.0

        red @confused "One of your kids?"

        melony @talkingmouth "Yes, that's right. A lovely young man named Gordie. He was so handsome."
        melony @talking2mouth "I tried to convince him to come to Kobukan, you know. I said he could take classes with me."
        melony tears sadbrow @talking2mouth "But... he preferred to head out on his journey alone. Trainer schools aren't common in Galar, so it's not unusual for boys his age, but... oh... I miss him so."
        melony @closedbrow talking2mouth "He was the first one of my children to leave home, and after he blazed the trail, my other children started to filter out one by one..."

        red @sadbrow happymouth "All boys leave home some day. It said so on TV."

        melony @angry "But do they have to leave home so soon? Surely he could have stayed with me until he was thirty-five! He'd still be young enough to go out and find a wife then! And she could move in with him until he was forty-five!"

        pause 2.0

        redmind @surprised "This is a {i}serious{/i} case of empty nest syndrome." 

        melony @talking2mouth "Oh... I'm sorry, I shouldn't be taking up your time with my tears."

        melony @happymouth "Let's just... freeze these in place..."

        pause 0.5

        melony -tears -frownmouth happy "Boop! There we go. All happy, no sadness!"

        pause 0.5

        melony sweat -happy @talkingmouth "...If I let you take the advancement exam for this class, will you not tell any of the other teachers about this?"
        melony @happy "If you pass the exam, I'll let you hack off some Never-Melt Ice from the cold locker. It boosts your Ice-type attacks by 10%%!"

        red @sweat closedbrow talking2mouth "Uh... yeah. Sure."

        $ AddEvent("Instructor Melony", 3)
    else:
        red uniform @talking2mouth "Mrs. Melony, I'm ready to retake my advancement exam. And I {i}will{/i} advance this time."

    melony @sadbrow happymouth"Oh, my delicious gelato... you're growing up too fast. Which Pokémon are you going to use, though? {color=#0048ff}Momma Melony's going to use an Ice-type this time.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    melony @angrybrow happymouth "I'm going to keep you riiiight by my side!"
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("melony", TrainerType.Enemy, [
        Pokemon("Lapras", level=21, moves=[GetMove("Ice Shard"), GetMove("Mist"), GetMove("Sing"), GetMove("Water Gun")], ability="Shell Armor", item="Oran Berry")
    ])

    call Battle([trainer1, trainer2], uniforms=[True, False]) from _call_Battle_96
    $ battlehistory["Instructor Melony2"]  = _return

    show melony with dis

    if (WonBattle("Instructor Melony2")):
        $ AddEvent("Instructor Melony", 3.1)

        pause 2.0

        melony closedbrow sadmouth tears cry "*Sniff.* W-well done... popsicle... H-here's... a Never-Melt Ice... since I couldn't freeze my tears..."
        red uniform @sadeyes sadeyebrows talkingmouth "Aw, Mrs. Melony... don't cry..."

        $ GetItem("Never-Melt Ice", 1, "Instructor Melony hands you a lump of sheer ice that burns to the touch. You quickly stash it in your bag.")

        $ renpy.pop_call()
        jump aftertutoring
    
    else:
        melony @happy "Oh dear! Why don't we enjoy some hot chocolate, to celebrate that you'll be sticking around? Tee-hee!"

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide melony with dis
elif (not HasEvent("Instructor Melony", 4.1) and classstats["Ice"] >= 30):#Ice Shard
    show melony with dis
    if (not HasEvent("Instructor Melony", 4)):
        $ renpy.pause(1.0, hard=True)

        red uniform @talkingmouth "Mrs. Melony?"

        melony @happy "Yes, my splendid sorbet?"

        red @closedbrow talking2mouth "I was just wondering why you, uh, became a teacher."

        melony @happy "Oh! Well, that's quite simple."
        melony @talkingmouth "You see, I'm getting on in my years."

        redmind @thinking "No you're not."

        melony @talkingmouth "So, all of my children have moved away. But I've spent so much of my life taking care of children, I couldn't possibly imagine stopping now."
        melony @happy "So I went back to school to get my teaching certificate. That was a good few years ago, though. I was actually only just hired by Kobukan this year."
        melony @closedbrow talking2mouth "I thought about going to work at Naranjuva Academy, but I wasn't sure if I'd get along well with the adult students Naranjuva accepts."

        pause 1.0

        red @confused "Mrs. Melony, this is a university. We're all adults here."

        melony @happy "Oh, no you're not, sweetheart."

        red @angry "Hey! I--"

        melony @happy "Now, now, let's not lose our tempers, sweetie. Why don't you take the advancement exam, instead? If you pass, I'll teach you the move Ice Shard."

        red @confused "I feel like I'm being bribed, but sure, I guess."

        $ AddEvent("Instructor Melony", 4)
    else:
        red uniform @talking2mouth "Mrs. Melony, I'm ready to retake my advancement exam. And I {i}will{/i} advance this time."

    melony @sadbrow happymouth "Oh, my delicious gelato... you're growing up too fast. Which Pokémon are you going to use, though? {color=#0048ff}Momma Melony can't recommend you pick an Ice-type, this time.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    melony @angrybrow happymouth "Mommy's going to teach you a little lesson!"
    $ hidebattleui=False
    $ mustswitch = False
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("melony", TrainerType.Enemy, [
        Pokemon("Combusken", level=31, moves=[GetMove("Bounce"), GetMove("Slash"), GetMove("Flame Charge"), GetMove("Double Kick")], ability="Blaze", item="Sitrus Berry")
    ])

    call Battle([trainer1, trainer2], uniforms=[True, False]) from _call_Battle_97
    $ battlehistory["Instructor Melony3"]  = _return

    show melony with dis

    if (WonBattle("Instructor Melony3")):
        $ AddEvent("Instructor Melony", 4.1)

        pause 2.0

        melony closedbrow sadmouth tears cry "*Sniff.* W-well done... popsicle..."
        red uniform @sadeyes sadeyebrows talkingmouth "Aw, Mrs. Melony... don't cry..."

        melony sadbrow -cry @talkingmouth "Since you've beaten an Ice-type, a Pokémon that Ice-types do well against, and one they don't do well against... I can move you up a level."

        pause 0.5

        melony "And even further from my grasp..."

        pause 0.5

        melony @angry "But I'll keep you here! For future exams, I'll be using {i}three{/i} Pokémon! And I'll stop you from advancing then!"

        $ passedclass = True
        jump aftertutorintroice
    
    else:
        melony @happy "There, see? If you just stop advancing, you won't have to lose anymore! Tee-hee!"

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide melony with dis

elif (FindGenericClassScene(True)):#generic scene
    $ renpy.call(FindGenericClassScene())
    hide melony with dis
else:# _really_ generic scene
    show melony with dis
    $ lowerDay = timeOfDay.lower()
    melony @happy "Good [lowerDay], you delectable sherberts! You've all grown so big since the last time I saw you!"
    melony @surprised "Now, it's a bit chilly in here, so why don't we all push our chairs into a circle while we do the reading?"
    hide melony
    show melonybg 
    with dis
    narrator "Class proceeds without incident."

return

label movetutorice:
show melony with dis
melony @happy "Of course, my little popsicle! I'd be more than happy to teach you a new move."
melony @talkingmouth "I can teach Slow Freeze, which is a move that moves after your opponent, but is guaranteed to freeze them!"
if (HasEvent("Instructor Melony", 4.1)):
    melony @surprisedbrow happymouth "If you don't want to go slow, though, why not try out Ice Shard? It'll move before any foes!"

label aftertutorintroice:
$ taughtmove = None

menu:
    ">Learn Slow Freeze":
        $ taughtmove = "Slow Freeze"
    ">Learn Ice Shard" if (HasEvent("Instructor Melony", 4.1)):
        $ taughtmove = "Ice Shard"
    "Nevermind":
        melony @sad "Oh... leaving already?"

        if (passedclass):
            $ renpy.pop_call()
            jump aftertutoring
        else:
            jump aftericesetup
python:
    hidebattleui = True
    renpy.transition(dissolve)
    newindex = renpy.call_screen("switch", MakeRed())
    if (newindex != "back"):
        newmon = playerparty[newindex]
    hidebattleui=False
if (newindex == "back"):
    melony @sad "Oh... leaving already?"
elif (MonCanLearn(newmon, taughtmove)):
    $ newmon.LearnNewMove([(1, taughtmove)])
    if (taughtmove in newmon.GetMoveNames()):
        jump endclass
else:
    melony @sad "Oh... sorry, sweetie. That Pokémon can't learn [taughtmove]."

jump aftertutorintroice

label itemcraftice:
show melony with dis

melony @sadbrow happymouth "When my kids were at home, we'd always used to work on craft projects together... oh, we made some wonderful things back then..."
melony @happy "For example, we used to deep-freeze chunks of ice to make Never-Melt Ice! These unmelting chunks of ice boost the power of Ice-type moves by a whole 10%%."

menu:    
    ">Craft Never-Melt Ice" if (HasEvent("Instructor Melony", 3.1)):
        $ GetItem("Never-Melt Ice", 1, "You hack away at a chunk of ice in the classroom's deep freezer. After an hour of work, you extract a chunk of ice so cold it burns to touch.")
        jump endclasscraft
    "Nevermind":
        melony @closedbrow tears sadmouth "Oh... you don't want to make anything with me, then...?"
        jump aftericesetup
