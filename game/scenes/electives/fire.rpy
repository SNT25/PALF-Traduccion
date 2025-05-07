label fireelective:

$ renpy.transition(dissolve)
show screen currentdate

scene map
show blank2:
    alpha 0.8

show classroom with dis

show fireclass:
    alpha 0.0 xalign 0.5 yalign 1.0
    ease 0.5 alpha 1.0

$ location = "fire"
$ passedclass = False

############################################################################################################################################################################################################################
#### 13. FIRE #######################################################################################################################################################################################################
############################################################################################################################################################################################################################
$ renpy.pause(1.0, hard=True)

call soniaevent from _call_soniaevent_1
call ethanevent from _call_ethanevent_6

label afterfiresetup:

if (HasEvent("Instructor Blaine", 2.1)):
    menu:
        "{b}>General Studies{/b}":
            pass

        ">Ask for move tutoring":
            jump movetutorfire

        ">Craft items" if (HasEvent("Instructor Blaine", 3.1)):
            jump itemcraftfire

if (not HasEvent("Instructor Blaine", 1)): #first class
    $ AddEvent("Instructor Blaine", 1)
    $ renpy.pause(1.0, hard=True)

    show may uniform happy:
        alpha 0.0 xpos 900
        ease 0.5 alpha 1.0

    show serena uniform behind may:
        alpha 0.0 xpos 500
        pause 0.5
        ease 0.5 alpha 1.0

    redmind "Oh, looks like May and Serena are here."

    show may:
        alpha 1.0 xpos 900
        ease 0.5 alpha 0.0

    show serena:
        alpha 1.0 xpos 500
        pause 0.5
        ease 0.5 alpha 0.0

    pause 0.75

    show flannery uniform tired:
        alpha 0.0 zoom 0.7 xpos 0.75
        ease 0.5 alpha 1.0

    redmind "And... there's Flannery, near the back.{w=0.5} She doesn't seem to notice me yet."

    show flannery:
        alpha 1.0 xpos 0.75
        ease 0.5 alpha 0.0

    pause 1.0

    hide flannery

    show blaine:
        xpos 900 alpha 0.0
        ease 1.25 xpos 800 alpha 1.0

    if (not IsDate(5, 4, 2004)):
        blaine "Ah, it looks like we've got some new faces! Ethan and [first_name], I believe? I hope you're excited to be in my class!"
    else:
        blaine "Hello, students! I'll wager you're all excited to be here, yes?"

    show blaine:
        xpos 800 alpha 1.0
        
    blaine "Well, it doesn't matter if you are or not. I'm sure you will be, once you see how much we've got to learn!"
    if (not IsDate(5, 4, 2004)):
        blaine @surprised "This is the {color=#0048ff}Fire class,{/color} in case either one of you two dozed off and wandered into the wrong room."
    else:
        blaine @surprised "This is the {color=#0048ff}Fire class,{/color} for those of you who might have wandered into the wrong room.{w=0.5} And I'll be your instructor for the year."
    
    $ BecomeNamed("Instructor Blaine")
    blaine happy "You can call me Blaine--or Dr. Katsura, if you must.{w=0.5} I've been researching Fire Pokémon for almost half a century."

    show blaine:
        alpha 1.0 xpos 800
        ease 0.5 alpha 0.0
    
    pause 0.5

    show blainebg with dis

    blaine "Fire is one of the most popular Pokémon types, and this class is always jam-packed!"
    blaine "Why, back in the day, at least one Fire Pokémon was found on the World Champion's team for twenty years running! No other type has that honor!"
    blaine "Of course, many credit that to the strength of Fire Pokémon. But that gives short shrift to their versatility and intelligence."
    blaine "Here you'll learn to apply firepower with subtlety and precision: to use your noggin, in addition to raw strength."
    blaine "Now, I'm speaking of tactical wisdom, not statistical optimization. There's no need for any of that silly effort training this generation is so obsessed with!"
    blaine "I remember when I was your age, my Magby and I used to..."

    narrator "This goes on for over half an hour."
    narrator "You can barely keep your eyes open. Combined with the warmth of the room, this produces an immensely soporific effect."

    redmind @closedeyes talkingmouth "Surely just a little shut-eye won't hurt...?"

    narrator "Your head slowly tips forward as you drift into unconsciousness."

    pause 1.0

    $ PlaySound("Wood Kick.ogg")

    pause 0.5
    narrator "You are jolted from your doziness by a sharp kick to the back of the knee."

    show serena uniform at leftside:
        alpha 0.0
        ease 0.5 alpha 1.0

    red @talkingmouth "Uh... what's up, Serena?"

    serena @sad "Do you really think it's acceptable to fall asleep in your first Fire-type class?"

    redmind "Was it that obvious?"

    red @happy "Oh, that's what you were doing.{w=0.5} Sorry, I appreciate the help."

    serena "Don't mention it. I can see why you would feel a bit drained listening to all of...{w=0.5} this."
    show serena happy with dis

    red @talkingmouth "No kidding."

    redmind "Speaking of feeling a bit drained..."

    show flanintro:
        subpixel True
        xalign 0.6 yalign 0.8 alpha 0.0 zoom 1.0
        parallel:
            ease 1.5 alpha 1.0
        parallel:
            ease 6.0 xalign 1.0 yalign 1.0

    pause 1.5

    if (timeOfDay == "Morning"):
        redmind "She wasn't kidding when she said she couldn't handle mornings."

        flannery closedbrow tiredmouth uniform "[ellipses]"

        $ PlaySound("Snore_F.ogg")
        flannery "{size=40}...ZZZ{/size}."

        redmind "...!"

        hide serena
        serena uniform surprised "Oh, my."

        $ PlaySound("Snore_F2.ogg")
        flannery "{size=45}ZZZ{/size}."

        blaine "What is that dreadful noise?"

        Character("Male Student") "\"Is it coming from that girl over there?\""

        red surprised "Flannery! Hey!"

        $ PlaySound("Snore_F.ogg")
        flannery "{size=40}ZZZ{/size}."

        red @angrymouth "Flannery, wake up! Your snoring is really loud!"

        $ PlaySound("Snore_F3.ogg")

        pause 0.5

        show flanintro:
            alpha 1.0
            ease 0.75 alpha 0.0
            
        $ renpy.pause(0.75, hard=True)

        $ PlaySound("Wood Kick.ogg")
        
        show flannery furious veins uniform:
            alpha 0.0 xpos -270 ypos 1.1 zoom 1.2
            ease 0.25 alpha 1.0 xpos 300 ypos 1.0

        flannery "Wh--I DON'T SNORE!"
            
        flannery surprised -veins "[ellipses]"

        blaine "Pardon me? Sorry, my hearing's not as good as it used to be, little missy."

        flannery sweat sadbrow talking2mouth "U-Uh, I said, 'I love Boldore'...{w=0.3} or something..."

        blaine "I see."
        blaine "Thank you for sharing that with us, but this is the Fire class, not the Rock class.{w=0.5} If you want to discuss Rock Pokémon, you'd best see Instructor Olivia."

        show flannery:
            xpos 300 ypos 1.0
            ease 1.0 xpos 100 ypos 1.2
            
        flannery thinking -sweat @talking2mouth "Right, sorry..."
        blaine "Moving on! When the wonders of trading was first invented, the capsule system..."

        redmind "Is Flannery embarrassed?"
        flannery angry veins "What are you staring at?!"
        red happymouth happyeyes "Nothing!"

    elif (timeOfDay == "Afternoon"):
        redmind "She said she couldn't handle mornings, but it looks like she can't handle afternoons, either!"
        flannery uniform closedbrow tiredmouth "[ellipses]"

        $ PlaySound("Snore_F.ogg")
        flannery "{size=40}...ZZZ{/size}."

        redmind "...!"

        hide serena
        serena uniform surprised "Oh, my."

        $ PlaySound("Snore_F2.ogg")
        flannery "{size=45}ZZZ{/size}."

        blaine "What is that dreadful noise?"

        Character("Male Student") "\"Is it coming from that girl over there?\""

        red surprised "Flannery! Hey!"

        $ PlaySound("Snore_F.ogg")
        flannery "{size=40}ZZZ{/size}."

        red @angrymouth "Flannery, wake up! Your snoring is really loud!"

        $ PlaySound("Snore_F3.ogg")

        pause 0.5

        show flanintro:
            alpha 1.0
            ease 0.75 alpha 0.0
            
        $ renpy.pause(0.75, hard=True)

        $ PlaySound("Wood Kick.ogg")
        
        show flannery surprisedbrow frownmouth uniform:
            alpha 0.0 xpos -270 ypos 1.1 zoom 1.2
            ease 0.25 alpha 1.0 xpos 300 ypos 1.0

        flannery "Oh, what? What happened? I just closed my eyes for a second, and..."
        
        redmind "Woah. Her voice just became super-gentle."

        blaine "Pardon me? Sorry, my hearing's not as good as it used to be, little missy."

        flannery sweat sadbrow talking2mouth "O-oh. I'm very sorry, Professor. This class is so warm, and your voice is so soothing, I dozed off.{w=0.5}{nw}"
        extend -sweat happy " Please forgive me?"

        blaine "I see."
        blaine "Well, given your manners, I'm willing to look over it this one time.{w=0.5} Still, you're paying too much to doze off in class again!"

        show flannery:
            xpos 300 ypos 1.0
            ease 1.0 xpos 100 ypos 1.2
            
        flannery happy -sweat @talking2mouth "Of course, Sir! Sorry."
        blaine "Moving on! When the wonders of trading was first invented, the capsule system..."

        if (persondex["Flannery"]["Value"] == 0):
            redmind "Wow. Flannery's {i}really{/i} different in the afternoon.{w=0.5} She's kind of cute to watch."
        flannery @sadbrow happymouth "Hey, [first_name]! Stop staring... geez, it's embarrassing!"
        red happymouth happyeyes "Sorry!"

    hide flannery with dis

    blaine "...But, luckily the PC changed all that.{w=0.5} No more Carrier Pidgey!"

    pause 1.0

    blaine "Hmm, looks like our time is up.{w=0.5} Just this once I'll spare you any homework. Class is dismissed!"

    hide flanintro
elif (not HasEvent("Instructor Blaine", 2.1) and classstats["Fire"] >= 10):#Steady Flame
    show blaine with dis
    if (not HasEvent("Instructor Blaine", 2)):
        $ renpy.pause(1.0, hard=True)

        narrator "The class is coming to the end of one of Instructor Blaine's snore-inducing lectures, when... "

        blaine happy "...and that's the story of Cinnabar Island! I'd love to go back some day. Once the lava's cooled, of course."

        blaine neutral "Now for something completely different. Who here could venture a guess as to the most important part of battling with a Fire-type? Is it power? Skill?"

        pause 2.0

        redmind uniform @thinking "Unless the answer is 'Zzzz,' I don't think he's going to hear one."

        blaine sad "Hrm. You, [first_name]. Perhaps you would hazard a guess?"

        red @surprised "Oh! Uh, sure, Sir. Well... with Fire-types, it's power, right?"
        red @closedbrow talking2mouth "Fire types have really strong offensive matchups, and their moves are often very powerful."

        blaine surprised "Is that your final answer, then?"

        red @closedbrow talking2mouth "Hm... well, actually... Fire is a pretty good defensive typing. It's got more resistances than any other type except Steel."
        red @happy "So maybe it's balance?"

        blaine happy "That's closer! The secret is {i}consistency.{/i}"

        red @surprised "Consistency?"

        blaine angry "Hmph! That's right! Kids nowadays... they think Fire-types are all about powerful moves that absolutely cripple you." 
        
        red @closedbrow talking2mouth "Are there a lot of them?"

        blaine "Overheat! Burn Up! Blast Burn. Eruption--you can't get a more inconsistent move than that. And don't get me started on 'Mind Blown,' the signature of that Alolan monstrosity."

        blaine "I'll be cold and in the ground before I recognize those {i}things{/i} as Pokémon."

        red @talkingmouth "Huh. I always figured that Fire-types were all about those big blasts of power."

        blaine neutral "Then it's a good thing you're in this class. Fire can be an amazingly destructive tool, but it can also be focused to a point, and used for precision work."

        blaine happy "A candle flame that lasts for a minute puts out more than a thousand times as much heat as an explosion which only lasts for a second."

        red @happy "Alright, Professor. Thanks."

        blaine sad "Thank {i}you{/i} for bothering to stay awake for my lectures! Some of these kids, I swear. It's like they don't appreciate their own money."

        redmind @thinking "Oops. Probably shouldn't tell him I nearly fall asleep in every single lesson..."

        blaine happy "Anyway, you've actually been paying attention enough that I think you could take the advancement exam. It's a simple one-on-one Pokémon battle."

        red @happy "Really, Sir? Wow! What does that mean, for this class?"

        blaine neutral "I'll be able to teach you Steady Flame. A decade's worth of scientific research led to a {i}consistent{/i} way for Fire-types to burn a foe--without relying on any of that Ghost-type hokum."

        red @closedbrow talking2mouth "That sounds really useful."

        blaine happy "That it is! Now, are you ready to take the exam?"

        red @happy "Um... in here? Isn't that kind of a fire hazard?"

        blaine neutral "Oh, I won't be using a Fire-type for this battle."

        $ AddEvent("Instructor Blaine", 2)
    else:
        red uniform @talking2mouth "Sir, I'm ready to re-take my advancement exam. I'm not going to lose again."

    blaine happy "If you're ready to burn brighter than ever, pick a Pokémon to face me! {color=#0048ff}A Fire-type would be the best option here.{/color}"

    python:
        trainer1 = Trainer("Red", TrainerType.Player, playerparty)
        for mon in playerparty:
            mon.Owner = trainer1
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", trainer1)

    blaine happy "Let's see what you can do, then! Hoo haa!"
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("blaine", TrainerType.Enemy, [
        Pokemon(46, level=11, moves=[GetMove("Scratch"), GetMove("Stun Spore"), GetMove("Poison Powder"), GetMove("Absorb")], ability="Dry Skin")
    ])

    call Battle([trainer1, trainer2], uniforms=[True, False]) from _call_Battle_30
    $ battlehistory["Instructor Blaine1"]  = _return

    show blaine with dis

    if (WonBattle("Instructor Blaine1")):
        $ AddEvent("Instructor Blaine", 2.1)

        blaine happy "Brilliant, m'boy! You might just be a candle for now, but if you keep progressing like that, I see you becoming an eternal flame!"

        $ passedclass = True

        jump aftertutorintrofire
    
    else:
        blaine sad "Hrmm... seemed you failed to ignite."
        blaine happy "No worries, m'boy, I suppose I failed to give you the right fuel."
        blaine neutral "Train a bit, then come back. I'm certain you'll light up next time."

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide blaine with dis
elif (not HasEvent("Instructor Blaine", 3.1) and classstats["Fire"] >= 20):#Charcoal
    show blaine with dis
    if (not HasEvent("Instructor Blaine", 3)):
        $ renpy.pause(1.0, hard=True)

        blaine @neutral "M'boy!"

        red uniform @talkingmouth "Instructor Blaine?"

        blaine @happy "You seem alert and awake. Good to see, good to see!"

        blaine @surprised "Tell me, what's the most important item a Pokémon can hold in battle?"

        red @closedbrow talking2mouth "Hm... I'm not sure, Instructor Blaine."
        red @confused "Something that makes them better at what they do? Or maybe it's something that covers up a weakness?"

        blaine @happy "Yes, yes, I'd say those are both good answers."

        red @surprised "Oh, you were asking my opinion?"

        blaine @happy "More or less. I just wanted to see what you'd say."

        red @closedbrow talking2mouth "Well, I think I'd have to take it on a case-by-case basis. There's no one item that is the best option for {i}every{/i} Pokémon."
        red @closedbrow talking2mouth "The closest item I can think of that fits that description would be... I dunno, Leftovers?"
        red @happy "But even then, there are plenty of Pokémon that would prefer the safety that comes with a Focus Sash. I mean, a Weavile isn't going to be able to do anything with Leftovers that it can't do otherwise."

        blaine @surprised "{w=0.5}.{w=0.5}.{w=0.5}."

        red @surprised "Oh, Instructor. Did I say something wrong?"
        
        blaine @happy "Not at all, m'boy. I was just impressed by your understanding of high-level item theory."

        red @happy "Oh, thanks! My Mom and I used to study how to use items most efficiently. They're pretty expensive, you know, so... we just wanted to make sure when I became a trainer, I wasn't wasting any money."

        blaine @sad "{w=0.5}.{w=0.5}.{w=0.5}."

        blaine "Right. Well, it's about high time I give you the advancement exam for this class, isn't it?"

        blaine @happy "When you pass, I'll give you class time to make Charcoals! They may seem like useless lumps of burnt wood, but they increase the power of Fire-type moves by 10%%!" 
        blaine "And they sell for a pretty penny, too, if you can find someone who wants them!"

        red @talkingmouth "I certainly wouldn't complain!"

        $ AddEvent("Instructor Blaine", 3)
    else:
        red uniform @talking2mouth "Instructor Blaine, I've studied a bunch since our last battle, and I've got a pretty solid theory of how I could beat you, now!"

    blaine "[bluecolor]I'll be using a single Fire-type.{/color} Pick your Pokémon accordingly, m'boy!"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    blaine @happy "Let's conduct the experiment!"
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("blaine", TrainerType.Enemy, [
        Pokemon("Ponyta", level=21, moves=[GetMove("Agility"), GetMove("Flame Charge"), GetMove("Ember"), GetMove("Growl")], ability="Flame Body", item="Oran Berry")
    ])

    call Battle([trainer1, trainer2], uniforms=[True, False]) from _call_Battle_86
    $ battlehistory["Instructor Blaine2"]  = _return

    show blaine with dis

    if (WonBattle("Instructor Blaine2")):
        $ AddEvent("Instructor Blaine", 3.1)

        blaine @happy "Brilliant, m'boy! Take this charcoal. But be careful--it's fresh!"

        $ GetItem("Charcoal", 1, "You gained a Charcoal! It's still warm to the touch.")

        $ renpy.pop_call()
        jump aftertutoring
    
    else:
        blaine sad "Hrmm... seemed you failed to ignite."
        blaine happy "No worries, m'boy, I suppose I failed to give you the right fuel."
        blaine neutral "Train a bit, then come back. I'm certain you'll light up next time."

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide blaine with dis
elif (not HasEvent("Instructor Blaine", 4.1) and classstats["Fire"] >= 30):#Flame Charge
    show blaine with dis
    if (not HasEvent("Instructor Blaine", 4)):
        $ renpy.pause(1.0, hard=True)

        narrator "Class is in session, and Instructor Blaine has just finished a particularly long lecture, leaving the class to do some practice questions in their textbooks."
        narrator "Due to the soporific warmth, you've been drifting in and out of consciousness for the past ten minutes. Suddenly, Instructor Blaine appears in your field of vision."

        blaine @happy "[first_name] [last_name]."

        red uniform @surprised "{size=30}*Snrrk...*{/size} Huh? Yes! Yes, Sir. Instructor Blaine. Sir."

        blaine @angry "Have you been sleeping well?"

        red @sadbrow sweat talkingmouth "Oh, you mean, um... just now? Sorry, it's {i}pretty{/i} warm in this class, and..."

        blaine "I don't mean that, m'boy. In your dorm, are you sleeping well?"

        red @confused "Huh?"

        blaine @surprised "I'm a scientist. When I see an effect, I hypothesize as to the cause. If you're tired in class, then it's possible you're not sleeping well at night."

        red @closedbrow talking2mouth "Oh! I see. I {i}think{/i} I'm sleeping well enough, yeah..."

        blaine @surprised "You have enough pillows? ...Blankets? Have you been eating?"

        red @happy "Yeah! I'm alright, really, Instructor. Thanks for checking in on me, though."

        pause 0.5

        red @confused "Um. May I ask where this is coming from?"

        blaine @sad "Hm..."

        blaine @surprised "Very well, m'boy. But let's go over here, so we don't disturb the other students with our prattling."

        hide blaine with dis

        pause 2.0

        show blaine with dis

        pause 0.5

        blaine @sad "I assume a boy from Kanto such as yourself is familiar with the Cinnabar Island disaster?"

        red @closedbrow talking2mouth "Yeah. I remember it was a really big thing a few years back. It happened just a few miles south of where I lived, in Pallet Town."

        blaine @happy "Ah, I thought I recognized your accent." 
        blaine @surprised "Yes, well, in the aftermath of the disaster, many of the survivors had trouble sleeping, or couldn't find the motivation to eat."
        blaine @sad "It was... an awful, but very human tragedy. Even after they were out of the actual danger, the threat they felt they were in..."
        blaine "In any case, I had to keep myself quite vigilant of my neighbors' health for a while. I never considered myself a medical doctor, far from it, but I know that staying up twenty-four hours isn't good for man or beast."

        pause 1.0

        red @closedbrow talking2mouth "Wow. Well... I guess that explains it. But I {i}really{/i} am fine. It's just the warmth of the classroom."

        blaine "Alright, then."

        pause 1.0

        show blaine with vpunch

        blaine @angry "So you have no excuse for falling asleep in class!"

        red @surprised "Gah?!"

        blaine @sad "I've half a mind not to offer this, but I was {i}going{/i} to suggest you take the class advancement exam."

        red @happy "Oh! That'd be... um, yes please."

        blaine @sad "Hmph."

        blaine @happy "Fine then, m'boy. Pass this exam, and I'll teach your Pokémon Flame Charge."

        red @talkingmouth "I'm ready!"

        $ AddEvent("Instructor Blaine", 4)
    else:
        red uniform @talking2mouth "Instructor Blaine, I've studied since the last time we fought--and now I'm more than ready to beat you."

    blaine @norm2 "Go on, then, pick one Pokémon. {color=#0048ff}But don't pick a Fire-type, or you'll be snuffed out.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    blaine @happy "Let's get this test started!"
    $ hidebattleui = False
    $ mustswitch = False
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("blaine", TrainerType.Enemy, [
        Pokemon("Drednaw", level=31, moves=[GetMove("Counter"), GetMove("Headbutt"), GetMove("Rock Tomb"), GetMove("Razor Shell")], ability="Shell Armor", item="Sitrus Berry")
    ])

    call Battle([trainer1, trainer2], uniforms=[True, False]) from _call_Battle_87
    $ battlehistory["Instructor Blaine3"]  = _return

    show blaine with dis

    if (WonBattle("Instructor Blaine3")):
        $ AddEvent("Instructor Blaine", 4.1)

        blaine @happy "Well done, m'boy! The knowledge of Flame Charge is yours. I hope it gives you a boost--"

        blaine @angry "And encourages you to {i}stay awake{/i} in my class from now on!"

        red uniform @sweat happy "Haha! I'll try, Instructor!"

        blaine "You've beaten a Fire-type, a Pokémon strong against Fire-types, and a Pokémon weak to Fire-types. This means you've passed the beginner segment of the class."
        blaine @surprised "Future exams will have me using three Pokémon, so be prepared for that."

        $ passedclass = True

        jump aftertutorintrofire
    
    else:
        blaine sad "Hrmm... seemed you failed to ignite."
        blaine happy "No worries, m'boy, I suppose I failed to give you the right fuel."
        blaine neutral "Train a bit, then come back. I'm certain you'll light up next time."

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide blaine with dis

elif (FindGenericClassScene(True)):#generic scene
    $ renpy.call(FindGenericClassScene())
    hide blaine with dis
else:# _really_ generic scene
    show blaine with dis
    $ lowerDay = timeOfDay.lower()
    blaine "Good [lowerDay], students! Sweltering today, isn't it?"
    hide blaine with dis
    show blainebg with dis
    blaine "Actually, that reminds me of a particular encounter I had with a Magcargo in Johto. It's a funny story! You see..."
    narrator "Class proceeds without incident."

return

label movetutorfire:
show blaine with dis
blaine @happy "You'd like to bolster your Fire-type Pokémon's repertoire with science? That's what it's for, m'boy!"
blaine @neutral "I can tutor a willing student in Steady Flame, a move that will consistently burn the foe."
if (HasEvent("Instructor Blaine", 4.1)):
    blaine @happy "If that doesn't strike your fancy, then why not Flame Charge? That might be more your speed. And it'll boost your speed, too!"

label aftertutorintrofire:
$ taughtmove = None

menu:
    ">Learn Steady Flame":
        $ taughtmove = "Steady Flame"
    ">Learn Flame Charge" if (HasEvent("Instructor Blaine", 4.1)):
        $ taughtmove = "Flame Charge"
    "Nevermind":
        blaine @angry "I don't have all day, m'boy."

        if (passedclass):
            $ renpy.pop_call()
            jump aftertutoring
        else:
            jump afterfiresetup
python:
    hidebattleui = True
    renpy.transition(dissolve)
    newindex = renpy.call_screen("switch", MakeRed())
    if (newindex != "back"):
        newmon = playerparty[newindex]
    hidebattleui=False
if (newindex == "back"):
        blaine angry "I don't have all day, m'boy."
elif (MonCanLearn(newmon, taughtmove)):
    $ newmon.LearnNewMove([(1, taughtmove)])
    if (taughtmove in newmon.GetMoveNames()):
        jump endclass
else:
    blaine @sad "Current research indicates that [taughtmove] and that Pokémon species are incompatible. Sorry, m'boy."

jump aftertutorintrofire

label itemcraftfire:
show blaine with dis

blaine @happy "Science isn't just skills and moves! Gadgets and gizmos make up the second half of it!"
blaine @neutral "A simple piece of specially-synthesized charcoal has been proven to boost the power of Fire-type moves by over 10%% in specialized trials!"

menu:    
    ">Craft Charcoal" if (HasEvent("Instructor Blaine", 3.1)):
        $ GetItem("Charcoal", 1, "You synthesize a piece of charcoal... by burning a piece of wood. Very scientific.")
        jump endclasscraft
    "Nevermind":
        blaine @happy "Ah, afraid to pop the lid on the unlimited power of science? Well, you'll have to eventually, m'boy!"
        jump afterfiresetup