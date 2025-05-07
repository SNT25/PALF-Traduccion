label electricelective:

$ renpy.transition(dissolve)
show screen currentdate

scene map
show blank2:
    alpha 0.8

show classroom with dis

show elecclass:
    alpha 0.0 xalign 0.5 yalign 1.0
    ease 0.5 alpha 1.0
show classlights:
    alpha 0.0 xalign 0.5 yalign 1.0
    parallel:
        pause 0.65
        ease 0.25 alpha 0.75
        pause 0.2
        ease 0.25 alpha 0.25
        pause 0.5
        ease 0.25 alpha 0.5
        pause 0.5
        ease 0.25 alpha 0.2
        pause 0.7
        ease 0.25 alpha 0.75
        pause 0.65
        ease 0.25 alpha 0.25
        repeat
show zap_A as zap1A:
    xpos 520 yalign 0 alpha 0.75
    parallel:
        pause 0.15
        ease 0.0 xpos 540 yalign 0 rotate 90
        pause 0.15
        ease 0.0 xpos 500 yalign 0 rotate 270
        pause 0.15
        ease 0.0 xpos 520 yalign 0 rotate 0
        repeat
    parallel:
        pause 0.1
        ease 0.0 alpha 0.75
        pause 0.2
        ease 0.0 alpha 0.0
        pause 0.1
        ease 0.0 alpha 0.75
        pause 0.1
        ease 0.0 alpha 0.0
        pause 0.2
        ease 0.0 alpha 0.75
        pause 0.1
        ease 0.0 alpha 0.0
        repeat
show zap_A as zap2A:
    xpos 690 yalign 0.23 alpha 0.75 zoom 0.66
    parallel:
        pause 0.12
        ease 0.0 xpos 710 yalign 0.23 rotate 94
        pause 0.16
        ease 0.0 xpos 670 yalign 0.23 rotate 265
        pause 0.14
        ease 0.0 xpos 690 yalign 0.23 rotate 5
        repeat
    parallel:
        pause 0.1
        ease 0.0 alpha 0.0
        pause 0.2
        ease 0.0 alpha 0.75
        pause 0.1
        ease 0.0 alpha 0.0
        pause 0.1
        ease 0.0 alpha 0.75
        pause 0.2
        ease 0.0 alpha 0.0
        pause 0.1
        ease 0.0 alpha 0.75
        repeat
show zap_A as zap3A:
    xpos 810 yalign 0.35 alpha 0.75 zoom 0.33
    parallel:
        ease 0.0 xpos 830 yalign 0.35 rotate 0
        pause 0.13
        ease 0.0 xpos 790 yalign 0.35 rotate 250
        pause 0.13
        ease 0.0 xpos 810 yalign 0.35 rotate 80
        pause 0.13
        repeat
    parallel:
        pause 0.1
        ease 0.0 alpha 0.75
        pause 0.2
        ease 0.0 alpha 0.0
        pause 0.1
        ease 0.0 alpha 0.75
        pause 0.1
        ease 0.0 alpha 0.0
        pause 0.2
        ease 0.0 alpha 0.75
        pause 0.1
        ease 0.0 alpha 0.0
        repeat
show zap_B as zap1B:
    xpos 1180 yalign 0 alpha 0.75
    parallel:
        pause 0.16
        ease 0.0 xpos 1200 yalign 0 rotate 45
        pause 0.2
        ease 0.0 xpos 1160 yalign 0 rotate 180
        pause 0.13
        ease 0.0 xpos 1180 yalign 0 rotate 90
        repeat
    parallel:
        pause 0.1
        ease 0.0 alpha 0.0
        pause 0.2
        ease 0.0 alpha 0.75
        pause 0.1
        ease 0.0 alpha 0.0
        pause 0.1
        ease 0.0 alpha 0.75
        pause 0.2
        ease 0.0 alpha 0.0
        pause 0.1
        ease 0.0 alpha 0.75
        repeat
show zap_B as zap2B:
    xpos 1080 yalign 0.23 alpha 0.75 zoom 0.66
    parallel:
        pause 0.12
        ease 0.0 xpos 1100 yalign 0.23 rotate 100
        pause 0.14
        ease 0.0 xpos 1060 yalign 0.23 rotate 250
        pause 0.12
        ease 0.0 xpos 1080 yalign 0.23 rotate 10
        repeat
    parallel:
        pause 0.1
        ease 0.0 alpha 0.75
        pause 0.2
        ease 0.0 alpha 0.0
        pause 0.1
        ease 0.0 alpha 0.75
        pause 0.1
        ease 0.0 alpha 0.0
        pause 0.2
        ease 0.0 alpha 0.75
        pause 0.1
        ease 0.0 alpha 0.0
        repeat
show zap_B as zap3B:
    xpos 1040 yalign 0.35 alpha 0.75 zoom 0.33
    parallel:
        ease 0.0 xpos 1060 yalign 0.35 rotate 90
        pause 0.15
        ease 0.0 xpos 1020 yalign 0.35 rotate 270
        pause 0.15
        ease 0.0 xpos 1040 yalign 0.35 rotate 0
        pause 0.15
        repeat
    parallel:
        pause 0.1
        ease 0.0 alpha 0.0
        pause 0.2
        ease 0.0 alpha 0.75
        pause 0.1
        ease 0.0 alpha 0.0
        pause 0.1
        ease 0.0 alpha 0.75
        pause 0.2
        ease 0.0 alpha 0.0
        pause 0.1
        ease 0.0 alpha 0.75
        repeat

$ location = "electric"
$ passedclass = False

############################################################################################################################################################################################################################
#### 13. Electric     #######################################################################################################################################################################################################
############################################################################################################################################################################################################################
$ renpy.pause(1.0, hard=True)

call soniaevent from _call_soniaevent
call rosaevent from _call_rosaevent_1
call nateevent from _call_nateevent
call ethanevent from _call_ethanevent_3

label afterelectricsetup:

if (HasEvent("Lieutenant Surge", 2.1)):
    menu:
        "{b}>General Studies{/b}":
            pass

        ">Ask for move tutoring":
            jump movetutorelectric
        
        ">Craft items" if (HasEvent("Lieutenant Surge", 3.1)):
            jump itemcraftelectric

if (not HasEvent("Lieutenant Surge", 1)): #first class
    $ AddEvent("Lieutenant Surge", 1)
    $ renpy.pause(1.0, hard=True)

    if (IsPresent("Leaf", "Electric")):
        show leaf uniform happy with dis:
            xpos 450 ypos 1.3 zoom 1.35

        pause 0.5

        ethan uniform surprised "Huh? Looks like Leaf is patting the empty seat next to her." 
        ethan happy "You dog! Go on, get in there."
        red uniform @closedbrow talking2mouth "...I'm not going to 'get in there.' I'm just going to talk."
        ethan "Sure, sure."

        pause 1.0

        leaf flirt "Hey, another class together!{w=0.5} You must feel so happy to spend {i}so much time{/i} with such a beautiful girl!"
        red @talkingmouth "I'm kind of feeling something different."
        leaf @talking2mouth "Oh, yeah? Let me guess, is it blessed?{w=0.5} Lucky?"
        red @happy "You're.{w=0.25}.{w=0.25}.{w=0.25} in the ballpark."

        hide leaf with dis

        pause 1.0

    $ PlaySound("ExitBuilding.ogg")

    stop music
    play music "Audio/Music/Vermillion_Start.ogg" noloop
    queue music "Audio/Music/Vermillion_Loop.ogg"

    show surge with Dissolve(0.2):
        xpos 1200
        ease 0.5 xpos 720

    show elecclass:
        parallel:
            xalign 0.0
            ease 0.03 xpos -20
            ease 0.03 xpos 20
            ease 0.03 xpos 0
            repeat 2
        parallel:
            yalign 0.0
            ease 0.03 ypos -20
            ease 0.03 ypos 20
            ease 0.03 ypos 0
            repeat 2

    surge @angrymouth "{size=44}ATTENT{cps=12}IIIOOOON{/cps}!!{/size}"

    redmind surprised "Wha-what? This army-looking guy just burst into the room yelling for no reason." 
    redmind sad "Is.{w=0.25}.{w=0.25}.{w=0.25} Is this guy our teacher?"
    
    surge @angrymouth anger "What are you maggots still sitting around for?! You got Diglett shit stuck in your ears?"
    
    $ BecomeNamed("Lieutenant Surge")
    
    surge @angrymouth anger "There's an officer on deck in this {color=#0048ff}Electric-type class{/color} and his name is Lt. SURGE!"
    surge @angrymouth biganger "That means {size=40}GET YOUR ASSES OUT OF YOUR CHAIRS! NOW!!{/size}"

    if (not IsDate(5, 4, 2004)):
        redmind thinking "Does he do this every day...?"

    $ renpy.music.play("Audio/Wood Kick.ogg", channel="misc", loop=None)
    redmind surprised "Geez! I don't know what's going on, but I better do what he says before he kicks the crap out of me!"

    hide surge with dis

    show elecclass:
        parallel:
            xalign 0.0
            ease 0.03 xpos -20
            ease 0.03 xpos 20
            ease 0.03 xpos 0
            repeat 3
        parallel:
            yalign 0.0
            ease 0.03 ypos -20
            ease 0.03 ypos 20
            ease 0.03 ypos 0
            repeat 3

    $ renpy.music.play("Audio/Wood Kick.ogg", channel="misc", loop=None)

    surge "{size=44}UP! UP! UP!{/size}{w=0.2}{nw}"
    $ renpy.music.play("Audio/Wood Kick.ogg", channel="misc", loop=None)
    extend " {size=44}UP! UP!{/size}{w=0.2}{nw}"

    $ renpy.music.play("Audio/Wood Kick.ogg", channel="misc", loop=None)
    extend " {size=44}GET UP!{/size}"

    show surgebg with dis

    surge "You recruits better start gettin' your acts together, unless you {i}WANT{/i} to feel my boots up your adolescent colons!"

    Character("Spineless Student") "\"H-hey! Y-y-y-you can't treat us l-like this!\""
    
    if (not IsDate(5, 4, 2004)):
        redmind thinking "Guess Ethan and I aren't the only students taking this class for the first time..."

    hide surgebg with dissolve

    show surge frownmouth with dis:
        xpos 0.25
        ease 0.5 xpos 0.25

    $ renpy.pause(1.5, hard=True)

    redmind "Uh oh.{w=0.5} I don't like that look one bit."

    Character("Spineless Student") "\"Y-you're a teacher here, right?{w=0.5} Teachers c-can't treat s-students like this!\""
    Character("Spineless Student") "\"That's against school p-p-policy...{w=0.5} isn't it?\""

    pause 2.0

    show elecclass:
        parallel:
            xalign 0.0
            ease 0.03 xpos -20
            ease 0.03 xpos 20
            ease 0.03 xpos 0
            repeat 3
        parallel:
            yalign 0.0
            ease 0.03 ypos -20
            ease 0.03 ypos 20
            ease 0.03 ypos 0
            repeat 3

    surge angrybrow anger @angrymouth "Do you think I'm being cute, boy?!{w=0.5} Do you think I'm playing JOKES?!"

    "Spineless Student" "\"{cps=18}W-Wha--{/cps}\""

    surge @angrymouth "I've got PLENTY of clearance to teach you skidmarks about DISCIPLINE and RESPECT!"
    surge -anger biganger @angrymouth "If you can't handle that, just crawl back home to your mama's udders, and have a good suck!"
    
    "Spineless Student" "\"{cps=18}I- nngh--{/cps}\""

    surge @angry "Stand up straight!{nw}"

    show surge:
        xpos 0.25
        ease 0.4 xpos 0.3

    extend " I said STAND UP!"

    surge @angry "Now, OUT! I won't have goddamn infants in my classroom!"

    pause 1.0

    redmind "Is this for real right now?"

    if (IsPresent("Nate", "Electric")):
        pause 1.0

        nate uniform @happy "{size=30}...Hah.{/size}"
        
        surge -biganger -angrybrow -anger surprised ".{w=0.75}.{w=0.75}.{w=0.75}"
        surge -surprisedbrow -frownmouth -surprised angry biganger "{cps=*0.2}WHO LAUGHED?"

        nate uniform @happy "Hah. Hahahahaha! That'd be me, Sir!"

        show nate happy uniform:
            xpos 1.5
            ease 1.0 xpos 0.75

        nate "And, geez, I'm super-sorry about it, but--"

        show elecclass:
            parallel:
                xalign 0.0
                ease 0.03 xpos -20
                ease 0.03 xpos 20
                ease 0.03 xpos 0
                repeat 3
            parallel:
                yalign 0.0
                ease 0.03 ypos -20
                ease 0.03 ypos 20
                ease 0.03 ypos 0
                repeat 3

        show nate surprisedbrow frownmouth with dis

        surge "Just what in the hell do you think you're doing, maggot?!"
        
        nate "Uh.{w=0.5}.{w=0.5}.{w=0.5} laughing, Sir?"
        nate closedbrow talking2mouth "I thought that was obvious, actually."

        pause 1.0

        nate happy "Oh, wait, now I get it! I'm laughing at {i}you{/i}, Sir. I'm sure that came off as confusing."

        surge "You--! What's your name, boy?!"
        if (not IsDate(5, 4, 2004)):
            nate sad "Sir! I've been in your class before..."
            surge "DID I ASK?!"
            nate "Right, Sir! Sorry, Sir!"

        nate "My name is Nate, Sir! Aspertia City's my home."
        surge "Nate, disrespect me one more time, and you'll be shitting out your TEETH!"
        nate surprised "Wait, what did I do?"

        show surge:
            xpos 0.3
            ease 0.25 xpos 0.65

        surge "I'M asking the questions! Now just what makes you think {i}YOU{/i} have the right to disrespect {i}ME{/i} in {i}MY CLASSROOM?!{/i}"
        
        nate happy "Oh, sorry about that! Just... all this explosive yelling and screaming, and that big mouth of yours? I couldn't help but think that you looked like an Electrode!"
        
        pause 1.5

        surge "[ellipses]"
        redmind "He's... he's going to die. He's straight-up going to die."

        pause 1.5

        show surge -angry -biganger -anger with dis:
            xpos 0.65
            ease 0.5 xpos 0.5

        surge @happy "Well, no shit. I admire your honesty, Private!{w=0.5} In fact, I like you!"
        nate "Thanks, Sir! I like you, too!"
        
        pause 1.0

        surge @sadmouth "Don't push it."

        show nate surprisedbrow frownmouth:
            xpos 0.75
            ease 0.5 xpos 1.5

        ethan uniform surprised "What?"

        surge @happy "Take a note from Nate, ladies!"
        surge @angrybrow happymouth "This man has no fear!{w=0.5} Therefore, he has no weakness!"

    surge @angry anger "I hear you whimpering like that other maggot and my Raichu will unscrew your head and shit down your neck 'til it pushes out every hole in your body!"
    surge @happy "Now, let's start with a quick two-mile run at the track!{w=0.5}{nw}"

    hide surge with dis
        
    extend " Let's go! I've seen legless Shuckle move faster than you assbags!"

    red @talkingmouth "Oh, god. If this is how it's gonna be every class, I might just end it all."

    if (IsPresent("Rosa", "Electric")):
        show rosa uniform with dis

        rosa sad "Seriously. You kinda just have to keep your head down, and hope he doesn't notice."

        if (not IsDate(5, 4, 2004)):
            red happy "Is he like this often?"
        else:
            red happy "Think every day will be like this?"

        rosa happybrow talkingmouth "No... I recognize an actor when I see one, and he was definitely putting a show."

        if (not IsDate(5, 4, 2004)):
            red thinking "Geez, I didn't think he even noticed Ethan and I were new. And I was happy that way!"

        red @talkingmouth "Well, Rosa, we should probably head out now. Don't want him yelling at us. Talk to you later?"
        rosa happy "Sure!"

        hide rosa with dis

    else:
        show sonia uniform with dis

        sonia sad "Right... you rather just have to keep your head down, and hope he doesn't notice."

        if (not IsDate(5, 4, 2004)):
            red happy "Is he like this often?"
        else:
            red happy "Think every day will be like this?"

        sonia happybrow talking2mouth "No... he was rather infamous last year for these little shows he puts on. His bark is worse than his bite."

        if (not IsDate(5, 4, 2004)):
            red thinking "Geez, I didn't think he even noticed Ethan and I were new. And I was happy that way!"

        red @talkingmouth "Well, Sonia, we should probably head out now. Don't want him yelling at us. Talk to you later?"
        sonia happy "Right-o!"

        hide sonia with dis

    hide surge
elif (not HasEvent("Lieutenant Surge", 2.1) and classstats["Electric"] >= 10):#Energize
    show surge with dis
    if (not HasEvent("Lieutenant Surge", 2)):
        $ renpy.pause(1.0, hard=True)

        narrator "Lieutenant Surge seems to be in a particularly good mood today, having devolved into a screeching, yelling, fit only once."

        show elecclass with vpunch

        surge @happy "LISTEN UP, LADIES!"

        redmind @thinking "God, I've been in this class so long, I'm actually starting to respond to 'ladies.'"

        surge @talkingmouth "You taint-scrubbers have been here long enough to learn the good stuff!"

        red @happy "Oh? Maybe something good's about to happen!"

        surge angry anger "HEY! Wipe that dumbass smile off your face, Private! Do you think you've got the stuff to advance in my class?"

        red @surprised "Uh..."
        
        surge -anger @biganger "Uh?! What the HELL does 'uh' mean, Private?"

        surge @anger "I want to hear 'Sir, YES Sir!' Or 'Sir, NO Sir!' Or 'I DO NOT KNOW, BUT I WILL FIND OUT, Sir!' Those are your only options! Am I understood?!"

        red @angry "Sir, YES Sir!"

        surge "I can't hear you! You scream like a goddamn Whismur! Put your lungs into it!"

        red @angry "{size=40}Sir, YES Sir!{/size}"

        surge "That's better! Now, do you think you're good enough to advance in {i}MY{/i} class?!"

        red @angry "{size=40}Sir, YES Sir!{/size}"

        surge @anger "Good! Then you should be ready to learn the move Energize!"

        red @surprised "{size=40}I DO NOT KNOW, BUT I WILL FIND OUT, Sir!{/size}"

        surge -anger -biganger -angry @happy "You're goddamn right, you will! The Snowbelle Conventions BANNED this one for being too powerful!"
        surge @surprised "ENERGIZE not only powers up your next Electric-type move, it also increases BOTH your attack stats!"
        surge surprised @angry angry "Now, ain't that just better than your mama's breakfast?!"

        red @angry "{size=40}Sir, NO Sir!{/size}"

        pause 2.0

        surge -surprisedbrow -frownmouth -surprised @happy "...That's what I like to hear! A real man always defends his mama's cooking!"
        surge angrybrow happymouth "Now, do you know what I'm going to do to you next?"

        red @angry "{size=40}Sir, NO Sir!{/size}"

        surge "I'm going to kick your ass all across this classroom in a one-on-one Pokémon battle! How do you like that?"

        red @angry "{size=40}Sir, NO Sir!{/size}"

        surge anger angrymouth "Oh, you don't like that? Punk kid doesn't like that? Then what are you going to do about it?"

        red @angry "{size=40}I DO NOT KNOW, BUT I WILL FIND OUT, Sir!{/size}"

        surge -anger -angrybrow -angrymouth @happy "Right answer!"

        $ AddEvent("Lieutenant Surge", 2)
    else:
        red uniform @talking2mouth "Lieutenant Surge, I'm prepared to battle you again, Sir!"

    surge @happy "Pick one Pokémon to save your ass from this beating! {color=#0048ff}If you pick anything but an Electric-type, Daddy's gonna take you out behind the woodshed!{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    surge "If you can't beat me, then you haven't been paying attention in my classes! Wanna guess how I'll feel about THAT, Private?!"
    $ hidebattleui=False
    $ mustswitch = False
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("surge", TrainerType.Enemy, [
        Pokemon(278, level=11, moves=[GetMove("Growl"), GetMove("Water Gun"), GetMove("Quick Attack"), GetMove("Supersonic")], ability="Keen Eye")
    ])

    call Battle([trainer1, trainer2]) from _call_Battle_27
    $ battlehistory["Lieutenant Surge1"]  = _return

    show surge with dis

    if (WonBattle("Lieutenant Surge1")):
        $ AddEvent("Lieutenant Surge", 2.1)

        surge @happy "You are GODDAMN adequate, Private!"
        surge angry "And don't let ANYONE take that from you!"

        red uniform @angry "{size=40}Sir, YES Sir!{/size}"

        $ passedclass = True

        jump aftertutorintroelectric
    
    else:
        surge angry "That was GODDAMN pathetic, Private!"
        surge @anger "They'd have weeded you out in boot camp! Get the hell outta my classroom until you've trained more!"

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide surge with dis
elif (not HasEvent("Lieutenant Surge", 3.1) and classstats["Electric"] >= 20):#Magnet
    show surge with dis
    if (not HasEvent("Lieutenant Surge", 3)):
        $ renpy.pause(1.0, hard=True)

        surge angry @anger "Private [last_name]!"

        red uniform @angry "{size=40}Sir, YES Sir!{/size}"

        surge "Do you know what you scored on your most recent test?!"

        red @angry "{size=40}Sir, NO Sir!{/size}"

        surge "Do you think you did well? Do you think you EARNED your spot at this academy?"

        red @angry "{size=40}Sir, YES Sir!{/size}"

        surge -angry @happy "GOOD! Because you got a 100%%! Listen up, LADIES! Private [first_name] has just volunteered to tutor you asswipes who can't keep up with the program!"

        redmind @thinking "Ugh. Great."

        surge @talkingmouth "What's the matter, PRIVATE? You seem DISCONTENT! Are you, maybe, not looking forward to MORE work without equal RENUMERATION?"

        red @surprised "{size=40}S-Sir, YES... Sir?{/size}"

        surge @happy "GOOD! I don't want to hear any of my troops accepting raw deals!"
        surge @angry "So HERE'S what I'm going to do for you, Private! Do you know how magnets work?"

        red @angry "{size=40}I DO NOT KNOW, BUT I WILL FIND OUT, Sir!{/size}"

        surge @angry "Well, I DON'T KNOW EITHER! But I DO know they boost the power of your Electric-type attacks by a whole 10%%!"
        surge @happy "You pass this advancement exam, and I'LL GIVE you one!"
        surge @angrybrow happymouth "And I'll even let you make more of them in FUTURE classes! Ain't I GENEROUS?!"

        red @angry "{size=40}Sir, YES Sir!{/size}"

        surge angry "Then show me your WAR FACE, Private!"

        $ AddEvent("Lieutenant Surge", 3)
    else:
        red uniform @talking2mouth "Lieutenant Surge, my Pokémon and I have trained, and are ready to take the advancement exam again."

    surge angry anger "{color=#0048ff}I'll be using one ELECTRIC-type.{/color} Get your ass in-gear, and pick which Pokémon you think can stand up to ME!"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    surge @happy "Enough bullshitting around! Let's get a {i}real{/i} battle going, Private!"
    
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("surge", TrainerType.Enemy, [
        Pokemon("Raichu", level=21, moves=[GetMove("Thunder Punch"), GetMove("Nuzzle"), GetMove("Sweet Kiss"), GetMove("Iron Tail")], ability="Static", item="Oran Berry")
    ])

    call Battle([trainer1, trainer2]) from _call_Battle_80
    $ battlehistory["Lieutenant Surge2"]  = _return

    show surge with dis

    if (WonBattle("Lieutenant Surge2")):
        $ AddEvent("Lieutenant Surge", 3.1)

        surge @angry anger "Private [last_name]! Do you know what you just did?!"

        red @angry "EXACTLY WHAT YOU TOLD ME TO, Sir!"

        surge @happy "That's GODDAMN right! And you didn't do it half bad, either! Take note of this one, ladies! Or you'll be WATCHING his BACK, soon!"

        $ GetItem("Magnet", 1, "Lieutenant Surge casually tosses a Magnet your way. It shocks you a bit.")

        $ renpy.pop_call()
        jump aftertutoring
    
    else:
        surge angry "DISGRACEFUL! Next time I'll let my seven-year-old beat your sorry ass!"
        surge @anger "Now get back to TRAINING. What are you waiting for, your participation trophy?!"

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide surge with dis
elif (not HasEvent("Lieutenant Surge", 4.1) and classstats["Electric"] >= 30):#Shock Wave
    show surge with dis
    if (not HasEvent("Lieutenant Surge", 4)):
        $ renpy.pause(1.0, hard=True)

        surge @angry "Private [last_name]! HOW does your VOICE feel?!"

        red uniform @sadbrow talking2mouth "{size=30}Hoarse, Sir.{/size}"

        surge @angry anger "I'm NOT SURPRISED! All that YELLING must have done a number on your WIMPY vocal CHORDS!"
        surge @happy "You need to TRAIN those puppies, Private! SCREAM your heart out until you can't hear yourself any LONGER!"

        red @sadbrow talking2mouth "{size=30}I think that might make things worse...{/size}"

        surge @surprised "WHAT WAS THAT?! Speak the HELL up!"

        surge @angry "What you DON'T UNDERSTAND is that screaming is a POWERFUL combat strategy!"

        red @surprised "{size=30}Huh?{/size}"

        surge @happy "OUT-YELL your opponent, and their Pokémon won't be able to hear their commands!"
        surge @angry "Scream loud enough and you can CONTROL the battlefield's current!"
        surge @talkingmouth "It BOOSTS morale! It ENFORCES discipline! It fills your opponent with SHOCK and AWE!"

        red @confused "{size=30}I guess... that's a valid strategy, actually...{/size}"

        surge @happy "You're GODDAMN right it's VALID! AND you know what a WIMP your opponent sounds like if they try to STOP YOU?"
        surge @sad "'WAH! WAH! MY EARS HURT!' Baby-ass whining! That's WHAT THEY'LL SOUND LIKE!"
        
        redmind "Oh, geez, I'm getting a headache. Just smile and nod."

        surge @angry "...YOU'RE blowing me off, huh, PRIVATE?"

        red @surprised "{size=30}N-no! I'd never dream of that.{/size}"

        surge @angry "You AREN'T BEING CHALLENGED ENOUGH!"
        surge @angry "You know what that MEANS?"

        red @confused "{size=30}I couldn't guess.{/size}"

        surge @happy "ADVANCEMENT EXAM TIME! If you don't completely FAIL this one, I'll teach your Pokémon Shock Wave!"

        red @surprised "{size=30}Oh...{/size}{w=0.5} Okay!"

        $ AddEvent("Lieutenant Surge", 4)
    else:
        red uniform @talking2mouth "Lieutenant Surge, I've studied since the last time we fought--and now I'm more than ready to beat you."

    surge @angry "You think you can pass this exam?! Well, you GODDAMN better, after EVERYTHING I've taught you! [bluecolor] Don't use an Electric-type for this battle, unless you want to take a dirt nap!{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    surge @happy "I'm going to go HARD at you, Private!"

    $ hidebattleui=False
    $ mustswitch = False
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("surge", TrainerType.Enemy, [
        Pokemon("Excadrill", level=31, moves=[GetMove("Rock Slide"), GetMove("Crush Claw"), GetMove("Sandstorm"), GetMove("Bulldoze")], ability="Sand Force", item="Sitrus Berry")
    ])

    call Battle([trainer1, trainer2], customexpressions=["red uniform", "red uniform angrybrow happymouth", "surge", "surge"], reanchor=[False, False]) from _call_Battle_81
    $ battlehistory["Lieutenant Surge3"]  = _return

    show surge with dis

    if (WonBattle("Lieutenant Surge3")):
        $ AddEvent("Lieutenant Surge", 4.1)

        surge @happy "Well, SHIT, Private! Color me IMPRESSED! You kicked the ass of a Pokémon that's weak to Electric-types, one that's strong against Electric-types, and an Electric-type itself!"

        surge @angry "Guess that MEANS you're getting a PROMOTION! How does PRIVATE SECOND CLASS sound, [last_name]?"

        red @angry "Sir, YES Sir!"

        surge @happy "Good answer!"

        $ passedclass = True

        jump aftertutorintroelectric
    
    else:
        surge angry "Now what the GODDAMN was THAT?!"
        surge @anger "Get the hell out of here! And don't come back until the puberty fairy pays you a VISIT!"

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide surge with dis

elif (FindGenericClassScene(True)):#generic scene
    $ renpy.call(FindGenericClassScene())
    hide surge with dis
else:# _really_ generic scene
    show surge with dis
    surge @talkingmouth "ATTTTENTION, maggots! You all better look alive, or else you'll be looking dead real soon. YOU! Recap our last lesson in sixty seconds or less!"
    surge @angry "If you stammer, stutter, or piss yourself, start the whole thing over! Now, GET RECAPPING!!!"
    hide surge with dis
    show surgebg with dis
    narrator "Class proceeds without incident."

return

label movetutorelectric:
show surge with dis
surge @happy "You want to expand your arsenal? Alright! But be careful, this shit is military-grade tactics!"
surge @talkingmouth "I can teach Energize, which will double the power of your next Electric-type move, and increase BOTH your attack stats!"
if (HasEvent("Lieutenant Surge", 4.1)):
    surge @happy "Why not follow it up with a Shock Wave? This point-blank electric attack NEVER misses a target!"

label aftertutorintroelectric:
$ taughtmove = None

menu:
    ">Learn Energize":
        $ taughtmove = "Energize"
    ">Learn Shock Wave" if (HasEvent("Lieutenant Surge", 4.1)):
        $ taughtmove = "Shock Wave"
    "Nevermind":
        surge @angry biganger "MAKE UP YOUR GODDAMN MIND, PRIVATE!"

        if (passedclass):
            $ renpy.pop_call()
            jump aftertutoring
        else:
            jump afterelectricsetup
python:
    hidebattleui = True
    renpy.transition(dissolve)
    newindex = renpy.call_screen("switch", MakeRed())
    if (newindex != "back"):
        newmon = playerparty[newindex]
    hidebattleui=False
if (newindex == "back"):
    surge @angry biganger "MAKE UP YOUR GODDAMN MIND, PRIVATE!"
elif (MonCanLearn(newmon, taughtmove)):
    $ playerparty[newindex].LearnNewMove([(1, taughtmove)])
    if (taughtmove in newmon.GetMoveNames()):
        jump endclass
else:
    surge @angry biganger "Are you special?! That Pokémon can't learn [taughtmove]!"
    
jump aftertutorintroelectric

label itemcraftelectric:
show surge with dis

surge @happy "You want some REAL armaments? They're not just for humans, y'know! Slap one of these on your troops, and blow away the competition!"
surge @talkingmouth "Magnets? Yeah, I don't know how they work! BUT IT DOESN'T MATTER! All you need to know about magnets is that they boost your Electric-type power by 10%%!"

menu:    
    ">Obtain Magnet" if (HasEvent("Lieutenant Surge", 3.1)):
        $ GetItem("Magnet", 1, "You quietly energize a piece of metal, instilling it with magnetic charge. Lieutenant Surge seems baffled.")
        jump endclasscraft
    "Nevermind":
        surge @surprised "Just throwing away military-grade equipment, Private? Dumb move!"
        jump afterelectricsetup