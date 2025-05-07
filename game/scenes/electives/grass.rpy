label grasselective:

$ renpy.transition(dissolve)
show screen currentdate

scene map
show blank2:
    alpha 0.8

show classroom with dis

show grasstype:
    alpha 0.0 xalign 0.5 yalign 1.0
    ease 0.5 alpha 1.0

$ location = "grass"
$ passedclass = False

############################################################################################################################################################################################################################
#### 13. GRASS        #######################################################################################################################################################################################################
############################################################################################################################################################################################################################
$ renpy.pause(1.0, hard=True)

call erikaevent("Grass") from _call_erikaevent_1
call ethanevent from _call_ethanevent_9
call gardeniaevent from _call_gardeniaevent_1

label aftergrasssetup: 

if (HasEvent("Instructor Ramos", 2.1)):
    menu:
        "{b}>General Studies{/b}":
            pass

        ">Ask for move tutoring":
            jump movetutorgrass

        ">Craft items" if (HasEvent("Instructor Ramos", 3.1)):
            jump itemcraftgrass

if (not HasEvent("Instructor Ramos", 1)): #first class
    $ AddEvent("Instructor Ramos", 1)
    $ renpy.pause(1.0, hard=True)

    show leaf uniform happy:
        xpos 0.25 alpha 0.0
        ease 0.5 alpha 1.0

    pause 0.5

    show brendan uniform happy:
        xpos 0.75 alpha 0.0
        ease 0.5 alpha 1.0

    ethan uniform surprised "Hey, we know those guys!"
    ethan @closedbrow talking2mouth "Looks like they want us to sit next to them."
    show leaf surprisedbrow frownmouth with dis
    show brendan surprisedbrow frownmouth with dis
    red uniform @closedeyes talkingmouth "Then they should've sat closer to each other. Let's sit in the middle. As a compromise." 

    show leaf:
        alpha 1.0 xpos 0.25 
        ease 0.5 xpos 0.15 alpha 0.0

    show brendan:
        alpha 1.0 xpos 0.75
        ease 0.5 xpos 0.85 alpha 0.0

    pause 1.0

    hide leaf
    hide brendan

    show ramos:
        xpos 900 alpha 0.0
        parallel:
            ease 1.5 xpos 860
        parallel:
            ease 0.5 alpha 1.0

    ramos @happy "Good day, sprouts!"

    window hide
    
    show ramos:
        xpos 860 alpha 1.0
        ease 1.5 xpos 820
        
    $ renpy.pause(1.5, hard=True)

    ethan "Whoa, he looks {i}really{/i} old."

    show ramos:
        xpos 820 alpha 1.0
        ease 1.5 xpos 780
        pause 1.0
        ease 1.0 xpos 750
        ease 0.5 alpha 0.0
        
    $ renpy.pause(3.0, hard=True)

    ethan surprised "That's our teacher?{w=0.5} Is he going to be okay?{w=0.5} He's slowly shuffling his way to the front and his legs look like they're going to give out any second."

    hide ramos
    
    show ramosbg with dis

    $ BecomeNamed("Instructor Ramos")
    if (not (calDate.month == 4 and calDate.day == 5)):
        ramos "If there's anyone new out there, yer in the {color=#0048ff}Grass elective class!{/color} Ramos's the name."
        redmind "He can't tell if there's anyone new here...? Wait, does he just say this before {b}every{/b} class?!"
    else:
        ramos "Welcome to the {color=#0048ff}Grass elective class!{/color}{w=0.5} I'm yer teacher. Ramos's the name."

    ramos "Before I begin, let me..."

    window hide
    pause 1.5

    ramos "Aw, horse apples."
    ramos "I done fergot the dang attendance sheet."
    ramos "I'll be right back."

    window hide
    pause 0.5

    show ramosbg:
        subpixel True
        alpha 1.0 xpos 960
        parallel:
            ease 1.5 xpos 980
        parallel:
            pause 1.0
            ease 0.5 alpha 0.0

    $ renpy.pause(3.0, hard=True)

    ethan "Man, isn't this school meant to be, like, hyper-rigorous? Instructor Ramos isn't filling me with confidence."
    red happy "You're telling me."

    show ramosbg:
        subpixel True
        alpha 0.0 xpos 980
        parallel:
            ease 1.5 xpos 960
        parallel:
            ease 0.5 alpha 1.0

    pause 1.5

    ethan @closedbrow talking2mouth "And he's back. That took a while."
    red @closedbrow talking2mouth "Judging by how fast he moves, that's to be expected."

    ramos "Ho! Sorry 'bout the delay, sprouts!"
    ramos "Now where was I..."
    
    pause 1.0

    ramos "Oh, Shuckles, looks like we ain't got no time left.{w=0.5} I reckon I shouldn't keep yeh longer than I hafta."
    ramos "Class dismissed. Y'all run along now!"
    ethan surprised "...Uh-oh. I'm suddenly really worried about this class."
elif (not HasEvent("Instructor Ramos", 2.1) and classstats["Grass"] >= 10):#Bark Up
    show ramos with Dissolve(2.0)
    if (not HasEvent("Instructor Ramos", 2)):
        $ renpy.pause(1.0, hard=True)

        narrator "You've been dilligently studying, head down over your desk, as you become aware that Instructor Ramos has, very, {i}very{/i} slowly been making his way to your desk."

        ramos neutral "[ellipses]"

        red uniform @talkingmouth "Instructor Ramos?"

        ramos surprised "Eh...? Whazzat?"

        red @surprised "Uh... I'm not sure! You came up to me, Sir."

        ramos "Oh, that right? Gosh darn it. I don't know where I'd put m' head if I didn't have it attached to me."

        redmind @thinking "Hm... he kinda reminds me of Grandpa."

        pause 1.0

        redmind @thinking "Hopefully less racist."

        ramos happy "Oh, yeah, now I remember! I'm thinkin' it's about time for yer first crack at the 'vancement exam. Just a one-on-one battle, don't y'know?"

        red @surprised "Really? Already? Uh, well... wow! Okay!"

        red @talkingmouth "Did I do something to deserve this?"

        ramos neutral "Well, y'listen to my stories. I like that in a youngin' like you."
        ramos happy "Besides, I can tell you've learned a good amount about Grass-types already."

        red @talkingmouth "What happens when I advance in this class?"

        ramos neutral "Well, then I c'n teach you a new move. Youngsters nowadays've probably forgotten the dang thing exists, but not me."
        ramos happy "My ol' noggin's like a steel trap!"

        pause 2.0

        red @closedbrow talking2mouth "Um... what's the move, then?"

        ramos neutral "Bark Up! It'll root you in place, but you'll recover a mite o' health every turn, and your defenses will go up."

        red @closedbrow talking2mouth "That's a useful move. Good for defensive Grass-types."

        red @surprised "Oh! Does it work if you're already under its effect?"

        ramos @happy "Ayup. Those defenses'll keep on goin' up. Though you can't double your healing, now."

        red @closedbrow talking2mouth "Okay... wow. Thanks, Instructor Ramos. So, uh, shall we do it now?"

        ramos surprised "Eh? Do what?"

        pause 2.0

        red @surprised "Uh, do the advancement exam."

        ramos sad "I don't remember nothin' 'bout that..."

        red @sadeyes sadeyebrows talkingmouth "It's alright, Instructor. You just said I could take the class advancement exam, and you'd teach me Bark Up if I won."

        pause 2.0

        ramos happy "Did I say that? Sounds about right!"

        $ AddEvent("Instructor Ramos", 2)
    else:
        red uniform @talking2mouth "Ramos, I've studied since the last time we fought--and now I'm more than ready to beat you."

    ramos neutral "Now, if yer ready to get on with the doggone battle, pick your Pokémon! {color=#0048ff}A Grass-type'll do this one, fer sure.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    ramos happy "Show me whatcha got, young'un!"
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("ramos", TrainerType.Enemy, [
        Pokemon(194, level=11, moves=[GetMove("Water Gun"), GetMove("Mud Shot"), GetMove("Tail Whip"), GetMove("Rain Dance")], ability="Damp")
    ])

    call Battle([trainer1, trainer2], customexpressions=["red uniform", "red uniform angrybrow happymouth", "ramos", "ramos angry"], reanchor=[False, True]) from _call_Battle_33
    $ battlehistory["Instructor Ramos1"]  = _return

    show ramos with dis

    if (WonBattle("Instructor Ramos1")):
        $ AddEvent("Instructor Ramos", 2.1)

        ramos happy "Well done, young'un! Does my old heart good to see kids like you sprouting so fast. Keep going! You'll scrape the treetops someday."

        $ passedclass = True

        jump aftertutorintrograss
    
    else:
        ramos happy "Oh, don't pay it no mind. You did well enough, considerin' how young you are."
        ramos neutral "I can't pass you off that, but come back tomorrow, y'hear?"

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide ramos with dis
elif (not HasEvent("Instructor Ramos", 3.1) and classstats["Grass"] >= 20):#Miracle Seed
    show ramos with Dissolve(2.0)
    if (not HasEvent("Instructor Ramos", 3)):
        $ renpy.pause(1.0, hard=True)

        narrator "You suppress a yawn as you go over the material in the textbook for the tenth time. You're starting to reach the point where you've memorized almost the entire section, and look around for something to entertain yourself with."

        pause 0.5

        narrator "Your eyes alight on Instructor Ramos, and you sigh, as you know what your only option is."

        red uniform @talkingmouth "Instructor Ramos?"

        ramos @surprised "Eh? Whazzat?"

        red @talkingmouth "I was hoping I could take the class advancement exam."

        ramos @happy "The advancement exam? Now, what'n you want to do that for?"

        red @happy "I just think I pretty much have this section figured out, so I was hoping that you would move me up."

        ramos ".{w=0.5}.{w=0.5}.{w=0.5}Alright, then. That sounds good to me, ayup."

        redmind @confusedeyebrows frownmouth "Huh, it's that easy?"

        ramos @angry "Why don't you'n pick out a Pokémon to do this thing with?"

        red @talkingmouth "Would you mind telling me what I get for this advancement exam? I mean, if I pass?"

        ramos @happy "Oh, right."

        ramos "Y'pass this exam, and you get a fine ol' Miracle Seed. N' I'll let you get more of 'em in future class times, if that's what ya want."

        red @talkingmouth "Thank you, Instructor! I'm ready for battle, then."

        ramos happy "Peachy keen! {color=#0048ff}I'm fixin' to use a Grass-type this time.{/color}"

        $ AddEvent("Instructor Ramos", 3)
    else:
        red uniform @talking2mouth "Ramos, I've studied since the last time we fought--and now I'm more than ready to beat you."

        ramos surprised "...Last time? Well, whatever you say! {color=#0048ff}I'm fixin' to use a Grass-type this time.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    ramos happy "This battle's got me revved up like a tractor!"
    $ hidebattleui=False
    $ mustswitch = False
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("ramos", TrainerType.Enemy, [
        Pokemon("Skiddo", level=21, moves=[GetMove("Synthesis"), GetMove("Worry Seed"), GetMove("Razor Leaf"), GetMove("Leech Seed")], ability="Sap Sipper", item="Oran Berry")
    ])

    call Battle([trainer1, trainer2], customexpressions=["red uniform", "red uniform angrybrow happymouth", "ramos", "ramos angry"], reanchor=[False, True]) from _call_Battle_92
    $ battlehistory["Instructor Ramos2"]  = _return

    show ramos with dis

    if (WonBattle("Instructor Ramos2")):
        $ AddEvent("Instructor Ramos", 3.1)

        ramos @happy "Well, I'll be. Yeh've shown this ol' geezer what-for!"

        $ GetItem("Miracle Seed", 1, "Ramos digs around in his pockets and pulls out a shining yellow Miracle Seed. It has some moist soil on it.")

        $ renpy.pop_call()
        jump aftertutoring
    
    else:
        ramos @happy "Aw, yer face is lookin' longer than a Gogoat's!"
        ramos @happy "Don't you worry, young'un. Give it another shot sometime--it ain't over 'til the fat lady sings!"

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide ramos with dis
elif (not HasEvent("Instructor Ramos", 4.1) and classstats["Grass"] >= 30):#Magical Leaf
    show ramos with Dissolve(2.0)
    if (not HasEvent("Instructor Ramos", 4)):
        $ renpy.pause(1.0, hard=True)

        ramos neutral "Y'there. [first_name], wasn't it?"

        red uniform @happy "That's right!"

        ramos @happy "Heh heh. I knew it. My ol' noggin's still got some brains left in it."

        ramos "I've been looking through some o' your test results and homework and whatnot, and it's lookin' to me like you're probably ready to go up a level in this class."

        red @talkingmouth "Oh, really? Awesome!"

        ramos @happy "Yes, and if you pass the exam, I'll teach your Pokémon the move Magical Leaf. Providing they can learn it, o' course."

        red @talkingmouth "That would be awesome, Instructor."

        ramos "Yes, well, today's a good day. All my brains are still right up in my head today. So I figured I should get some stuff done."

        pause 0.5

        red @sadbrow talking2mouth "...Right."

        pause 0.5

        ramos @happy "Oh, don't look so sad about it, now. I'm still a spring chicken at heart, y'know. I won't keel over from throwin' a dang Pokémon Ball."

        red @happy "Right. Well, I'm ready to take the exam now."

        $ AddEvent("Instructor Ramos", 4)
    else:
        red uniform @talking2mouth "Ramos, I've studied since the last time we fought--and now I'm more than ready to beat you."

    ramos neutral "Now, if yer ready to get on with the dang battle, pick your Pokémon! {color=#0048ff}Don't you go using a Grass-type this time, or you'll get thrown onto the compost pile.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    ramos happy "Show me whatcha got, young'un!"
    $ hidebattleui=False
    $ mustswitch = False
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("ramos", TrainerType.Enemy, [
        Pokemon("Fletchinder", level=31, moves=[GetMove("Flame Charge"), GetMove("Acrobatics"), GetMove("Agility"), GetMove("Flail")], ability="Flame Body", item="Sitrus Berry")
    ])

    call Battle([trainer1, trainer2], customexpressions=["red uniform", "red uniform angrybrow happymouth", "ramos", "ramos angry"], reanchor=[False, True]) from _call_Battle_93
    $ battlehistory["Instructor Ramos3"]  = _return

    show ramos with dis

    if (WonBattle("Instructor Ramos3")):
        $ AddEvent("Instructor Ramos", 4.1)

        ramos @happy "Well done, young'un! That means you beat a Grass-type, a Pokémon that does well against Grass-types, and a... uh..."

        ramos @sad "What was that dang third one..."
        ramos @happy "Oh, I got that blighter! You also beat a Pokémon that Grass-types beat easily. So I reckon in future exams, I can take things a bit less easily, and use three Pokémon at once, eh?"

        $ passedclass = True

        jump aftertutorintrograss
    
    else:
        ramos happy "Almost got me--but you've still got some sprouting to do!"
        ramos happy "Don't you worry now, Brassius. Tomorrow's another day, and you'll have plenty of 'em."

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."
        redmind uniform @surprised "...Wait a minute. Who's Brassius?"

    hide ramos with dis

elif (FindGenericClassScene(True)):#generic scene
    $ renpy.call(FindGenericClassScene())
    hide ramos with dis
else:# _really_ generic scene
    show ramos with dis
    $ lowerDay = timeOfDay.lower()
    ramos "Good [lowerDay], sprouts! Ye ready to learn yer little heads off?"
    hide ramos with dis
    show ramosbg with dis
    ramos "So, back in the early days of the Pokémon League, when every fresh trainer wore an onion on their belt, 'cause that was the style at the time, Grass-types were..."
    narrator "Class proceeds without incident."

return

label movetutorgrass:
show ramos with dis
ramos @angry "Eh? You want me to teach your Grass-type Pokémon a new move? Well, why didn't you say so? Speak up, sonny!"
ramos @neutral "Bark Up is a move that raises your defenses, but roots you t' the ground. {w=0.5}...Oh, but you recover a bit of health every turn, too!"
if (HasEvent("Instructor Ramos", 4.1)):
    ramos @happy "If that don't do it for ya, then how 'bout a Magical Leaf? That move never misses, n'matter how fast yer opponent is!"

label aftertutorintrograss:
$ taughtmove = None

menu:
    ">Learn Bark Up":
        $ taughtmove = "Bark Up"
    ">Learn Magical Leaf" if (HasEvent("Instructor Ramos", 4.1)):
        $ taughtmove = "Magical Leaf"
    "Nevermind":
        ramos @sad "Huh...? What were we doin'?"

        if (passedclass):
            $ renpy.pop_call()
            jump aftertutoring
        else:
            jump aftergrasssetup
python:
    hidebattleui = True
    renpy.transition(dissolve)
    newindex = renpy.call_screen("switch", MakeRed())
    if (newindex != "back"):
        newmon = playerparty[newindex]
    hidebattleui=False
if (newindex == "back"):
        ramos @sad "Huh...? What were we doin'?"
elif (MonCanLearn(newmon, taughtmove)):
    $ newmon.LearnNewMove([(1, taughtmove)])
    if (taughtmove in newmon.GetMoveNames()):
        jump endclass
else:
    ramos @sad "Y'playing some sort of joke, sprout? That Pokémon can't learn [taughtmove]!"

jump aftertutorintrograss

label itemcraftgrass:
show ramos with dis

ramos @happy "There's nothing like a couple home-grown items to get yer garden lookin' nice."
ramos @talkingmouth "Why don'tcha try out a Miracle Seed? I don't remember what they grow into, but they boost the power of yer Grass-type moves by 10%%!"

menu:    
    ">Craft Miracle Seed" if (HasEvent("Instructor Ramos", 3.1)):
        $ GetItem("Miracle Seed", 1, "You water and feed a Budew until it bestows on you its singular and rare Miracle Seed.")
        jump endclasscraft
    "Nevermind":
        ramos @happy "Oh, nothin'? Well, hold yer hay, because I'm expecting a shipment o' fertilizer any day now."
        jump aftergrasssetup
