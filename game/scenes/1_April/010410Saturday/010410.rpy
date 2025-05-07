label day010410:

$ timeOfDay = "Morning"
call calendar(1) from _call_calendar_6
$ calDate = calDate.replace(day=10, month=4, year=2004)

show blank2
queue music "Audio/Music/Show Me Around.ogg"
show morning at vspaz

pause 3.5

$ renpy.transition(dissolve)
show screen currentdate

scene relichall_A with Dissolve(2.0)

hide morning    
hide blank2

show leaf at midleftside with dis:
    xzoom -1

leaf @happy "Ah, another perfect day!"
leaf @closedbrow talkingmouth "Is everyone here?"

show ethan at farleftside with dis

ethan @happy "Yeah, c'mon, let's go!"

show calem at farrightside with dis:
    xzoom -1
show serena at midrightside with dis:
    xzoom -1

calem @happymouth "Kalos contingent, reporting in."
serena @happy "{i}Allons-y!{/i}"

show brendan surprisedbrow frownmouth behind leaf at leftside with dis:
    xzoom -1
show may surprisedbrow frownmouth behind leaf at centerside with dis

brendan @talking2mouth "H-hey, wait for us!"
may @talkingmouth "Yeah, we brought the snacks!"

show brendan -surprisedbrow -frownmouth -surprised
show may -surprisedbrow -frownmouth -surprised
with dis

red @talkingmouth "You ready, [pika_name]?"

show leaf happy
show may happy
show serena happy
with dis

$ renpy.music.play("Audio/Pokemon/pikachu_excite4.ogg", channel="altcry", loop=None)
pikachu happy_3 "Pika!"

leaf @happy "Sweet. I've got the extra Poké Balls. Use as many as you want, you guys!"

show leaf -happy
show may -happy
show serena -happy
with dis

leaf @blush sadbrow happymouth "Sorry I don't have anything stronger than Poké Balls."

serena @talkingmouth "I imagine we're probably not going to encounter anything that warrants a Great Ball."

ethan @happy "Speak for yourself, I'm going to catch a Tyranitar!"

if (starter_species_name == "Larvitar"):
    ethan @closedbrow talking2mouth "Although my Larvitar will evolve into one. Maybe two Tyranitar would be too much."

calem @happy "Priorities, people. Let's not cross the bridge of what Poké Balls we need until we reach the river of 'actually encountering a Pokémon.'"

show calem surprisedbrow frownmouth with dis

brendan surprisedbrow frownmouth @surprised "Woah, there's a river where you can encounter Pokémon?"

calem @sad "Er... that's not--"

may @happy "Yeah! That's all of them, sweetie!"

brendan angrybrow happymouth "Hey, let's go there!"

ethan happy "Hell yeah! Race you!"

show serena surprisedbrow frownmouth with dis

serena @talkingmouth "Ah, wait... it's quite a long way!"

show brendan:
    ease 0.5 xpos 1.5
show may:
    ease 0.9 xpos 1.5
show ethan:
    ease 0.7 xpos 1.5
show leaf:
    ease 1.2 xpos 1.5

pause 2.0

red @happy "This is fun."

show serena happy
show calem happy
with dis

calem @talkingmouth "Isn't it?"

show calem:
    ease 0.5 xpos 1.5
show serena:
    ease 0.5 xpos 1.5
    
$ renpy.pause(1.0, hard=True)

show blank2 with dis:
    alpha 1.0

stop music fadeout 2.5

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_45

pause 3.5

hide brendan
hide may
hide ethan
hide calem
hide serena

############################################################################################################################################################################################################################
#### 2. FIELDS #############################################################################################################################################################################################################
############################################################################################################################################################################################################################

show clouds behind leaf:
    yalign 0.75
    ease 5.0 yalign 0.5
show fields1 behind leaf:
    xalign 0.0
    ease 10.0 yalign 0.33 xalign 0.95

$ renpy.music.play("Audio/Morning_ambience.ogg", channel='crowd', loop=True, fadein=1.0)

play music "Audio/Music/Fieldstheme_Start.ogg" noloop
queue music "Audio/Music/Fieldstheme_Loop.ogg"

$ renpy.transition(dissolve)
show screen currentdate

show blank2:
    alpha 1.0
    ease 1.0 alpha 0.0
$ renpy.pause(1.5, hard=True)

hide blank2

$ renpy.pause(8.5, hard=True)

$ renpy.music.play("Audio/Pokemon/pikachu_happy3.ogg", channel="altcry", loop=None)
pikachu happy_3 "Pika!"

show fields1:
    yalign 0.33 xalign 0.95
    
red @happy "You doing okay, [pika_name]?"

$ renpy.music.play("Audio/Pokemon/pikachu_sad.ogg", channel="altcry", loop=None)

pikachu yawn "Pika..."

show brendan at midrightside with dis
show may at leftside with dis

brendan @talking2mouth "Hey, [first_name]. Taking a break?"

red @happy "Nah, just slowing down for [pika_name]. He's a bit of a couch potato." 
red @talkingmouth "Back home, I tried to convince him to go on runs with me. Didn't really work. I ended up carrying him most of the way."

show leaf at midleftside with dis

leaf @talkingmouth "You know, you should really see if you can fix that."

red @surprisedbrow talking2mouth "What do you mean?"

leaf @closedbrow talkingmouth "I mean, he's going to be a Champion's Pokémon someday, right?"
leaf @happy "You don't want your Pokémon falling asleep in the middle of a Champion match."

red @happy "Hey, how do you know about the Champion thing?"

show ethan at centerside behind brendan with dis

ethan @happy "{i}Everyone{/i} knows about that one, dude! You talk about it in your sleep. At least, that's what {i}Hummina{/i} said. He bought new headphones just to drown you out."

red @surprised "Seriously?"

brendan @closedbrow talking2mouth "Seriously, bro. I never noticed, but Hilbert was always complaining. Dunno how Hilbert heard when he's as far away from your bed as possible, but maybe he's just got good ears."

show calem at farrightside with dis:
    xzoom -1

calem @talkingmouth "Seconded."

red @happy "Huh. Well, yeah, guilty as charged. I'll be a Champion someday."

may @happybrow talkingmouth "You sound confident!"

red @happy "Why shouldn't I be? I've got the best team in the world."

leaf @sarcastic "...Two. You have two Pokémon."

red @closedbrow talking2mouth "Yeah, but they're great ones."

leaf @happy "[first_name], I'm serious. I know that [pika_name] is your little buddy, but you've gotta recognize that {i}something{/i} about him needs to change, right?"

red @happy "Nah, I don't think so."

show serena at rightside behind calem with dis:
    xzoom -1

serena @closedbrow talkingmouth "Being able to identify the weaknesses of your friends is just as valuable a skill as being able to analyze your opponent's weaknesses."

red @sadeyes sadeyebrows talking2mouth "I'll... take that under advisement."

$ renpy.music.play("Audio/Pokemon/pikachu_norm2.ogg", channel="altcry", loop=None)
pikachu neutral_2 "Piii-ka!"

brendan @happy "Hey! Enough of the serious faces! We gotta find that river, right? C'mon!"

show brendan:
    ease 0.5 xpos 1.5

show may:
    ease 1.2 xpos 1.5

calem @closedbrow talking2mouth "I fear I may have started something that can't be stopped."

show calem:
    ease 1.2 xpos 1.5

show serena:
    ease 1.3 xpos 1.5

show leaf:
    ease 1.6 xpos 1.5

pause 2.0

red @talkingmouth "Yeah, Ethan?"

ethan @closedbrow talking2mouth "Uh... I just want to say, like... I get it."

red @confusedeyebrows talking2mouth "What do you mean?"

ethan @closedbrow talking2mouth "Well, I've never really had any, uh, friends. But if I did, I'd be so happy, I'd never criticize them, or tell 'em to do anything different."

red @happy "Hey, Ethan, what are you saying? C'mon, we're {i}all{/i} friends here!"

ethan @sadbrow happymouth "Hey. You and me, we're friends. Everyone else? They're {i}your{/i} friends."

red @thinking "[ellipses]"

red @talkingmouth "Well, maybe for now. But hang around. Mitosis'll help you."

pause 0.5

show may:
    ease 0.5 xpos 0.75

show ethan surprisedbrow frownmouth with dis

may surprisedbrow frownmouth @surprised "Osmosis!"

ethan @talkingmouth "What?"

may happy "Osmosis is the process where a high-concentration body equalizes with a low-concentration body. You said mitosis, which is when a cell reproduces by cloning itself."

ethan -surprisedbrow frownmouth @angry "No, I'm saying 'what' because you were eavesdropping on a serious conversation."

may surprisedbrow frownmouth @surprised "Oh."

show may:
    ease 0.5 xpos 1.5

red @happy "C'mon, Ethan. Let's get going. Don't want to let the others catch all their Pokémon before us."

ethan @happy "Yeah! Let's go."

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_46

show blank2 with splitfade

pause 2.0

show fields2 behind fields1:
    xalign 0.0 zoom 0.85
    ease 6.0 xalign 0.4

hide fields1
hide ethan

$ renpy.pause(1.0, hard=True)

hide blank2 
show screen currentdate
with splitfade
    
pause 3.5

show leaf at rightside with dis

leaf @happy "There you guys are!{w=0.5} I never would've expected you to be the straggler, [first_name]."

red @happy "Swear it's not me. I'm just waiting for [pika_name] to catch up."

show calem at leftside with dis

calem @talking2mouth "May I ask a question, [first_name]?"

red @talkingmouth "Sure!"

calem @closedbrow talkingmouth "Have you... ever caught a Pokémon in the wild before?"

red @sadeyes sadeyebrows talkingmouth "Can't say I have."

show serena at farleftside with dis

serena @happy "Well, that's not a problem! We can teach you how to do that."

red @happy "Oh, uh, I know how. You just have to tire out the Pokémon, without hurting it, then throw a Poké Ball at it."

leaf @sarcastic "Yeah, there's slightly more to it than that."

red @surprisedeyebrows talking2mouth "Really? Name two things."

leaf @happy "Well, there's{w=0.25}.{w=0.5}.{w=1.0}."

pause 1.0

leaf @closedbrow talkingmouth "Er. Well, if it's affected by a status condition, it becomes easier to catch. Especially if it's Sleeping or Frozen."

red @closedbrow talking2mouth "Huh. I didn't know that, actually. Thanks."

leaf @happy "That's what I'm here for!"

red @angrybrow happymouth "But that's still only one thing."

leaf embarrassed bigblush @embarrassedbrow angrymouth "Okay, fine! It's actually really simple! Is that what you wanted to hear?"

red @happy "That'll do it, yeah."

show leaf -embarrassed -bigblush with dis

show brendan at centerside with dis

brendan @talking2mouth "Hey, time's wasting. Maybe we should let our Pokémon out, and see if they can root out any wild Pokémon for us."

show ethan at midleftside with dis

ethan @talkingmouth "Won't you guys' Pokémon just run away if you do that, though?"

serena @closedbrow talking2mouth "Possibly, but we can always call them back to their Poké Ball if they get too far away."
calem @talkingmouth "Yes. They're truculent, but not to the point they'd actually try to get away from us."
calem @sad "...One hopes."

show blank2 with splitfade

pause 1.0

play sound ["Audio/Pokemon/Ball sound.ogg", "audio/pokemon/cries/669.mp3", "audio/pokemon/cries/172.mp3", "audio/pokemon/cries/285.mp3"]

pause 1.0

narrator "Your friends release their Pokémon. Predictably, they quickly take the opportunity to scamper away--hopefully in pursuit of some scent."

pause 2.0

hide brendan
hide may
hide ethan
hide calem
hide serena
hide leaf

red @talkingmouth "Well, [pika_name]? [starter_name]? Any directions?"

$ renpy.music.play("Audio/Pokemon/pikachu_question.ogg", channel="altcry", loop=None)
pikachu neutral_4 "Pika...?"

red @happy "Y'know, like a smell. Can you smell any other Pokémon out there? I'm trying to get you a friend."

$ renpy.music.play("Audio/Pokemon/pikachu_happy1.ogg", channel="altcry", loop=None)
pikachu neutral_4 "Chu!"

red @closedbrow talking2mouth "...And there they go. Let's see if they actually understood what I was saying."

pause 1.0

narrator "Shortly after, you hear a familiar voice."

blue @angry "...{size=20}Telling{/size} {size=23}you{/size} {size=26}it's{/size} {size=29}messed{/size} {size=32}up{/size}!"

red @surprised "[blue_name]?"

red @closedbrow talking2mouth "Oh, man, not what I was looking forward to."

$ timeOfDay = "Noon"

show blue surprisedbrow frownmouth at centerside behind blank2 with dis

hide blank2 with splitfade

pause 2.0

blue -surprisedbrow -frownmouth -surprised frownmouth @angry "[first_name]? What are {i}you{/i} doing here?"

red @talkingmouth "Uh... finding new Pokémon. I mean, that's my plan, anyway."

stop music fadeout 5.0 channel "crowd"
stop music fadeout 5.0 

blue surprised @angry "Of course you are. Well, you better stay away from--"

pause 1.0

red @confused ".{w=0.25}.{w=0.25}.{w=0.25}?"

blue @angry "Actually, come with me! Make yourself useful for once in your life, and convince these idiots to not be so stupid."

hide blue with dis

narrator "Blue drags you by the arm to a different part of the fields, bordering a denser forest."

scene forest with dis

show face angry at farleftside with dis
show mace angry at midleftside with dis

show nate angry at midrightside with dis:
    xzoom -1
show cheren angry at farrightside with dis:
    xzoom -1

narrator "You emerge into a clearing. In the center of the clearing is a visibly-injured Charmander, with four trainers standing around arguing."

$ renpy.music.play("Audio/pokemon/cries/4.mp3", channel="altcry", loop=None)

queue music "audio/music/tension_start.ogg" noloop
queue music "audio/music/tension_loop.ogg"

cheren  "You {i}cannot!{/i} Don't you understand that it's far too hurt for further battle?"
mace "A likely story! As soon as we turn our backs, you're just going to catch it yourself!"
nate "Look, swear we won't. We need to bring it to a Pokémon Center."
face "How about {i}we{/i} bring it to the Pokémon Center--after we catch it!"

redmind @thinking "...Wow, okay, there's clearly a lot of context I'm missing here, but the first thing I need to do is make sure that Charmander's okay."

blue @surprised "Well? Do something!"

redmind @thinking "Why's he asking me?"

red @talkingmouth "Uh, hey, uh, what's happening here?"

show face surprisedbrow frownmouth
show mace surprisedbrow frownmouth
show nate surprisedbrow frownmouth
show cheren surprisedbrow frownmouth
with dis

cheren @talkingmouth "Ah? Blue? You're back?"
nate "Hey! [first_name]. Surprised to see you here."

blue @closedbrow talking2mouth "Yeah, yeah. Figured the Pokécenter was too far away, so this idiot could do something for us."

nate @closedbrow talking2mouth "{size=30}Wait... that person you meet up with, why didn't you get--{/size}"

show face angry
show mace angry
with dis

mace @talkingmouth "Hmph. Big surprise that you lot are friends with the nepotism baby."

red @surprised "H-huh?"

face @talkingmouth "Don't play dumb. No money, no academics, no connections? You said that you only knew one other person at this school."

mace @talkingmouth "You might have mentioned that 'one person' was the world-famous Professor you're on a first-name basis with."

face @talkingmouth "And now I see you're friends with another Oak."

show blue angry at rightside behind nate with dis:
    xzoom -1

red @sad "I... I mean... I don't..."

blue @talkingmouth "You idiots don't know what you're talking about. My gramps had nothin' to do with this loser getting in. And we're {i}not{/i} friends."

cheren angry "How dare you cast aspersions on this innocent man? I promise, as part of my campaign to modernize and uplift this school, I will thoroughly examine whether anyone got in through untoward means."

mace @talkingmouth "Well, that doesn't help us much {i}now{/i}, does it?"

nate closedbrow talking2mouth "Hey, guys, the Charmander? It's pretty hurt. Maybe we could table this discussion?"

red @closedbrow talking2mouth "Look, just let me..."

show face surprisedbrow frownmouth
show mace surprisedbrow frownmouth
show nate surprisedbrow frownmouth
show cheren surprisedbrow frownmouth
show blue surprisedbrow frownmouth 
with dis

narrator "Before anyone can react, you reach out to the Charmander, pulling out the Rage Candy Bar Silver gave you a while ago."

show charmanderintro with Dissolve(2.0)

pause 3.0

hide face
hide mace
hide nate
hide cheren
hide blue

red @sadeyes sadeyebrows talkingmouth "Hey, little guy. I'm pretty sure Lance wouldn't want me to give you this..."

narrator "The Charmander, which had previously been cowering, curled up in a circle, slowly looks up at you, taking a few tentative steps."

nate @closedbrow talking2mouth "So, that's how it works..."

red @sadeyes sadeyebrows talkingmouth "Yeah, there we go. See? Nothing to be afraid of. We're all friends here. Just eat up, and we'll get you to a Pokémon Center."

blue @closedbrow angrymouth "Tch."

mace surprisedbrow frownmouth @surprised "How...?"

face @sadbrow talking2mouth "When we tried to get closer to it, it just snapped at us, and spat fire..."

cheren @closedbrow talking2mouth "Yes, it's quite peculiar."
cheren @surprised "Oh! But that's not a bad thing!"

show face behind charmanderintro at farleftside
show mace behind charmanderintro at midleftside
show nate behind charmanderintro at midrightside:
    xzoom -1
show cheren behind charmanderintro at farrightside:
    xzoom -1
show blue behind charmanderintro at rightside:
    xzoom -1

hide charmanderintro with dis

red @talkingmouth "Okay. I think it's calm enough to carry it to the Center now."

show face angry
show mace angry
with dis

mace @talkingmouth "I think not. It's well enough to be captured, now. So we can continue what we were doing before you interrupted."

cheren angry "Ah, yes, continue your {i}very fair{/i} two-on-one."

blue angry "[first_name] just gave it a chocolate bar! He calmed it down, he didn't magically heal it!"

nate angry "Yeah, back off. This is your last warning."

face @talkingmouth "Nuh-uh! This is {i}your{/i} last warning. We're graduates of the Anistar City School for the Gifted."

blue happy "Hah! I thought you seemed a bit 'special!'"

mace @talkingmouth "Enough of this! If you insist on standing between us and that Charmander, we'll go {i}through{/i} you!"

face @talkingmouth "Yeah! We won't be intimidated by your tough talk!"

blue surprised @angry "Fine, I'll take you both on! [first_name], watch and learn. This is how a real pro battles!"

nate @talkingmouth "Yeah, nah, B. These guys were fine with outnumbering their opponent."

cheren closedbrow talking2mouth "Yes, I see no reason why we should feel guilty for doing the same."

blue @talkingmouth "Ugh... fine. [first_name]! Watch and learn. This is how a pro, and his two hangers-on, battle!"

python:
    HealParty()
    trainer1 = MakeTrainer("Cheren", TrainerType.Ally)
    trainer2 = MakeTrainer("Blue", TrainerType.Ally)
    GetTrainerTeam("Blue", "Pidgeotto").Level = 20
    GetTrainerTeam("Blue", "Eevee").Level = 7
    trainer3 = MakeTrainer("Nate", TrainerType.Ally)

    trainer4 = Trainer("face", TrainerType.Enemy, [
        Pokemon(207, level=7, gender=Genders.Male, moves=[GetMove("Poison Sting"), GetMove("Sand Attack"), GetMove("Harden")], ability="Hyper Cutter"),#Gligar
        Pokemon(127, level=7, gender=Genders.Male, moves=[GetMove("Vise Grip"), GetMove("Focus Energy"), GetMove("Bind")], ability="Hyper Cutter")])#Pinsir
    trainer5 = Trainer("mace", TrainerType.Enemy, [
        Pokemon(215, level=7, gender=Genders.Female, moves=[GetMove("Scratch"), GetMove("Leer"), GetMove("Taunt")], ability="Inner Focus"),#Sneasel
        Pokemon(123, level=7, gender=Genders.Female, moves=[GetMove("Focus Energy"), GetMove("Leer"), GetMove("Vacuum Wave"), GetMove("Quick Attack")], ability="Technician")])#Scyther

call Battle([trainer1, trainer2, trainer3, trainer4, trainer5], gainexp=False, specialmusic=("audio/music/UnovaTrainerStart_rock.ogg", "audio/music/UnovaTrainerLoop_Rock.ogg")) from _call_Battle_8
$ battlehistory["Aces1"]  = _return

play music "Audio/Music/Fieldstheme_Start.ogg" noloop
queue music "Audio/Music/Fieldstheme_Loop.ogg"

if (WonBattle("Aces1")):
    show face angry at farleftside
    show mace angry at midleftside
    show nate happy at midrightside:
        xzoom -1
    show cheren happy at farrightside:
        xzoom -1
    show blue happy at rightside behind nate:
        xzoom -1
    with dis

    blue "Hah! Suck it, you pathetic excuses for Pokémon trainers!"

    $ ValueChange("Blue", 1, 0.75, False)
    $ ValueChange("Nate", 1, 0.63, False)
    $ ValueChange("Cheren", 1, 0.88)

    mace "This was clearly an unbalanced fight!"

    face "Yes, my Pokédex said that was a {i}level 20{/i} Pokémon!"

    show cheren surprisedbrow frownmouth
    show nate
    with dis

    cheren -surprisedbrow -frownmouth -surprised @closedbrow talking2mouth "Is that right? I thought it seemed a bit too powerful."

    nate -surprisedbrow -frownmouth -surprised @talkingmouth "*Whistle.* You been holding out on us, B?"

    blue -happy @angry "No! You imbeciles just haven't been listening when I tell you that I'm the best trainer at this school!"

    red @surprised "...Blue, your Eevee and Pidgeotto have both gained two levels since we last battled."

    blue @talkingmouth "Yeah? So what?"

    red @closedbrow talking2mouth "That was {i}last night.{/i}"

    blue @angry "What part of {i}I'm the best trainer at this school{/i} do people not get? Yeah, we trained all night! And we were out here training more until these 'gifted students' screwed things up!"

    cheren @angrybrow sadmouth "Speaking of. We've beaten you fair and square. Abide by the terms of the Pokémon battle, and leave this Charmander alone."

    mace "[ellipses]"

    face "[ellipses]"

    mace "Your victory here is not the end."

    face "We'll be back! And we'll expose you for the unmerited dullards you are!"

    show mace:
        ease 0.5 xpos -0.5
    show face:
        ease 0.5 xpos -0.5

    nate @happy "Seeya!"
    cheren @happy "Good riddance."

else:
    show face happy at farleftside
    show mace happy at midleftside
    show nate angry at midrightside
    show cheren angry at farrightside
    show blue angry at rightside behind nate
    with dis

    blue "Guh...! Nate, Cheren, you guys {i}suck!{/i} You were dragging me down!"

    cheren @closedbrow talking2mouth "Now, now. Everyone gave their best."

    nate @closedbrow angrymouth "{size=30}Not everyone...{/size}"

    mace "As expected. Our victory was never in doubt."

    face "Hmph! It's really rather sad. After talking up such a big game, and using--according to my Pokédex--a level 20 Pokémon, you still couldn't beat us?"

    show cheren surprisedbrow frownmouth
    show nate
    with dis

    cheren -surprisedbrow -frownmouth -surprised @closedbrow talking2mouth "Is that right? I thought it seemed a bit too powerful."

    nate -angry frownmouth @talkingmouth "*Whistle.* You been holding out on us, B?"

    blue -happy @angry "No! You imbeciles just haven't been listening when I tell you that I'm the best trainer at this school!"

    red @surprised "...Blue, your Eevee and Pidgeotto have both gained two levels since we last battled."

    blue @talkingmouth "Yeah? So what?"

    red @closedbrow talking2mouth "That was {i}last night.{/i}"

    blue @angry "What part of {i}I'm the best trainer at this school{/i} do people not get? Yeah, we trained all night! And we were out here training more until these 'gifted students' screwed things up!"

    cheren @sad "...Ah. I hate to bring this up, but... we lost fair and square. We should abide by the terms of the Pokémon battle, and leave this Charmander with our opponents."

    redmind @thinking "Alright. Desperate times call for desperate measures."

    pause 1.0

    red @surprised "{cps=*0.5}...Oh, no!{w=0.5} It escaped in the confusion!{/cps}"

    pause 1.0

    show mace angry
    show face angry
    with dis

    pause 2.0

    mace "You are clearly lying."

    face "Yeah, you suck at it."

    red @sadbrow talking2mouth "Damn. I really thought that'd work."

    nate @closedbrow talking2mouth "{i}...Sigh.{/i} I really didn't want to have to do this. But, if this is the only way to keep the li'l guy safe..."

    show nate angrybrow happymouth

    nate "C'mon! Let's fight."

    mace @surprised "...Did we not just do that? If you didn't realize, that would certainly explain the poor showing you put up, but..."

    show face surprisedbrow frownmouth
    show cheren surprisedbrow frownmouth
    show blue surprisedbrow frownmouth
    with dis

    show nate:
        ease 0.2 xpos 0.37 rotate -40
        ease 0.7 rotate 0.0

    show mace surprisedbrow frownmouth with dis:
        pause 0.1
        ease 0.3 xpos -0.3

    show forest with vpunch

    pause 2.0

    red @surprised "Holy shit."

    mace "Agh! You fucking dick! You broke my nose, you-- you goddamn {i}peasant!{/i}"

    nate happy "Hey, I'm part of a military family! That puts me in upper-middle class, at least!"

    face "We're... we're telling someone about this! You won't get away with this!"

    show face:
        ease 1.0 xpos -0.5

    show cheren sad
    show blue -surprisedbrow -frownmouth -surprised
    show nate -happy
    with dis

    pause 2.0

    nate @happy "Phew. Sorry about that. Been ages since I threw a punch. My technique was all sloppy."

    cheren @closedbrow talking2mouth "...You shouldn't have done that. As a hopeful Student Council member, I cannot turn a blind eye to that sort of rule-breaking."

    nate @closedbrow talking2mouth "Hmmm... we're off-campus right now. And you aren't a StuCo member yet, C. Sure you couldn't defer your report?"

    cheren @sad "Not even for a friend. Especially not."

    cheren @closedbrow talking2mouth "But I have been extraordinarily busy lately. I'll give you a little time to... prepare yourself."

    nate frownmouth @angry "Gee, so generous."

    blue angry "Yeah, what the hell, Cheren? We wouldn't have lost if your weak-ass cat wasn't dragging us down. Have you trained it {i}at all?!{/i}"

    cheren @angry "I have, as I might have mentioned, been very busy. I make time to assist in {i}your{/i} training. I could certainly give that up to focus on my own."

    blue @surprised "Wait, you actually haven't trained it? Feh, how'd you even get into this school?"

    cheren @closedbrow talking2mouth "Excellent academics."

    blue @angry "Ugh, of course. Goddamn nerd."

pause 2.0

show blue angry:
    ease 0.5 xpos 0.5
show cheren surprisedbrow frownmouth:
    ease 0.5 xpos 0.75
show nate surprisedbrow frownmouth:
    ease 0.5 xpos 0.25 xzoom 1
with dis

pause 0.5
hide blue
show blue angry at getcloser

blue @talkingmouth "And you! Some help you were! You just stood around like a fat lump while {i}we{/i} did all the battling."

red @talkingmouth "Wow, I really can't win with you, can I?"

pause 2.0

blue @closedbrow angrymouth "Gah!"

hide blue with dis

pause 2.0

$ initial = first_name[0]
nate -surprisedbrow -frownmouth @happy "Hey, [initial]."

red @happy "Nate. I'd say 'long time,' but it hasn't been that long, really."

cheren -surprisedbrow -frownmouth @closedbrow talking2mouth "May I ask what you are doing out here?"

red @talkingmouth "Oh, just seeing if there are any wild Pokémon to catch."

red @surprised "I think the real question is what are you two doing out here? With [blue_name]?"

cheren @sad "Er... he prefers to be called 'Blue.'"

red @happy "Yeah, I know!"

nate @talkingmouth "Well, when B came back to our dorm last night, he seemed super steamed about something. Demanded that we get out of bed and help him train."

nate @happy "Poor C fell asleep on his feet after, like, twenty minutes."

cheren @sad "Yes, I'm afraid I've been burning the candle at both ends for too long. Student Council campaigning is getting... difficult."

red @talkingmouth "So you three are dormmates?"

nate @talkingmouth "Yeah. Us and two other guys."

cheren @closedbrow talking2mouth "They mostly keep to themselves, however."

nate @happy "Yeah, after the first time B blew his lid, they just put on their headphones and tuned out of dorm life."

red @confusedeyebrows talking2mouth "But you two haven't?"

cheren @closedbrow talking2mouth "A student council member must always keep his ears open to his peers. Even if he suffers permanent hearing loss."

nate @happy "And I just think he's hilarious!"

red @talking2mouth "It gets old quickly."

nate @happy "So, just out of curiosity, did you manage to talk with Professor Oak on Thursday? By the time I came back to the lab, you were gone."

red @surprised "Oh. Yeah! Uh, I don't think I told you that, though?"

show nate angrybrow frownmouth

pause 0.5

nate -angrybrow -frownmouth @happy "Yeah, duh. Bianca told me."

red @closedbrow talking2mouth "Oh, right, that makes sense. Yeah, he just wanted to talk about some stuff. Pallet stuff."

cheren surprisedbrow frownmouth @surprised "Er... wait. Am I right in understanding that you {i}do{/i} personally know Professor Oak?"

redmind @surprised "Crap."

red @talkingmouth "Uh, yep. We're friends. I used to play chess with him back home. Always lost, but that's because black was missing a pawn and both bishops."

cheren -surprisedbrow -frownmouth -surprised @closedbrow talking2mouth "Hm."

nate @sweat surprised "You didn't play white, too?"

red @happy "Nah. I got attached to black, you know? They were the underdogs. My little buddies."

red @sadeyes sadeyebrows happymouth "Guess I was just sentimental."

if (council_campaigning):
    cheren @closedbrow talking2mouth "Unrelatedly, how's campaigning for the student council going?"

    red @happy "Oh, I haven't actually done {i}any{/i} of that."

else:
    cheren @closedbrow talking2mouth "Unrelatedly, I hear you've changed your mind regarding the student council?"

    red @surprised "Huh? No, not at all. Like, I haven't done anything about the council."

show cheren surprisedbrow frownmouth with dis

pause 2.0

show cheren shadow sadeyes with dis

cheren @disappointedmouth "Ah. I... see."

nate @surprised "Seriously? From how C's been talking about you, I kinda figured you were opponent numero uno."

if (council_campaigning):
    red @surprised "Er, really? I thought we were on the same side."

    cheren @sadmouth "Ah... yes, we are."

else:
    red @sadeyes sadeyebrows talkingmouth "I told you I wasn't really interested in student council stuff, though..."

    cheren @sadmouth "Yes... yes, you did."

cheren @closedbrow talking2mouth "Apologies. I've been polling the student body. Your name comes up surprisingly often."

red @closedbrow talking2mouth "...But, like, less than Calem and Serena, right?"

cheren "[ellipses]" 

red @surprised "Oh, geez."

if (council_campaigning):
    cheren -shadow -sad2eyes -sadeyes @closedbrow talking2mouth "Ah, enough of that."

    cheren @sadmouth "I'm certain when you begin campaigning in earnest, as I have, things will start to shake themselves out."

else:
    cheren -shadow -sad2eyes -sadeyes @closedbrow talking2mouth "Ah, enough of that."

    cheren @sadmouth "It's a little frustrating, my greatest challenger being someone not even competing... but I'll simply have to work twice as hard."

red @sadeyes sadeyebrows happymouth "Hey. Don't over do it."

cheren @closedbrow talking2mouth "Mm."

nate @closedbrow talking2mouth "So, uh, what're we going to do with the Charmander?"

if (starter_species_name == "Charmander"):
    red @closedbrow talking2mouth "Well, I already have one, so..."

red @talkingmouth "Take him back to the Pokémon Center, right? That was the plan."

nate @talkingmouth "Oh, yeah, sure. But are you cool to just leave here? You didn't come here alone, right?"

show cheren sadbrow with dis

red @closedbrow talking2mouth "Oh, I did actually come with a big group of friends."

nate @closedbrow talking2mouth "Looks like B is heading back to the school, anyway, based on that storm cloud over there. Guess he doesn't need us anymore. Why don't you let us take the Charmander back to the Pokécenter?"

red @happy "Can you?"

pause 1.0

red @confusedeyebrows talking2mouth "Actually, {i}can you?{/i} I mean, he might freak out."

nate @happy "Yeah, it'll be fine. Probably. Give 'im here, and we'll find out."

narrator "You hand off the clingy Charmander. It protests weakly, but seems only marginally more squirmy in Nate's arms."

nate @talkingmouth "Looks like we can do this, then."

red @talkingmouth "Thanks a bunch."

nate @talkingmouth "Don't worry about it. Oh, but we should exchange contact deets, in case it gets loose, and we need you to wrangle it again."

$ BecomeContacted("Nate")

nate @happy "Alright! Seeya, [first_name]!"

show blank2 
hide nate
hide blue
hide cheren
with splitfade

$ renpy.pause(2.0, hard=True)
    
show text "{color=#ffffff}.{/color}" as text1:
    alpha 1.0
    pause 0.5
    linear 0.0 alpha 0.0
show text "{color=#ffffff}..{/color}" as text2:
    alpha 0.0
    pause 0.5
    block:
        linear 0.0 alpha 1.0
        pause 0.5
        linear 0.0 alpha 0.0
show text "{color=#ffffff}...{/color}" as text3:
    alpha 0.0
    pause 1.0
    block:
        linear 0.0 alpha 1.0
        pause 1.5
        linear 1.0 alpha 0.0
$ renpy.pause(4.0, hard=True)

show clouds:
    yalign 0.5
show fields1:
    yalign 0.33 xalign 0.95

$ timeOfDay = "Afternoon"

hide text1
hide text2
hide text3
hide blank2
show brendan at farleftside:
    xzoom -1
show may at leftside
show ethan at midleftside behind may
show calem at farrightside:
    xzoom -1
show serena at rightside:
    xzoom -1
show leaf at midrightside behind serena
with splitfade

serena @surprised "Ah, [first_name]? Where did you get off to?"

calem @surprisedbrow talkingmouth "Yes, you were gone for so long, we thought you'd gone home."

leaf @sarcastic "I just thought you ran ahead of us and got lost again."

red @happy "Nah, just found a wild Charmander in the forest."

show may surprisedbrow frownmouth
show ethan surprisedbrow frownmouth
show serena surprisedbrow frownmouth
with dis

if (starter_species_name == "Charmander"):
    ethan @talking2mouth "WHAT?! Another one?!"

ethan @talking2mouth "Did you catch it, dude?"

red @talkingmouth "Nah. Actually, no-one did. It had gotten hurt pretty bad when some scumbags from the school two-on-one'd it."
red @closedbrow talking2mouth "I met some friends in the forest, though, and they took the Charmander back to the Pokémon Center."

show ethan -surprisedbrow -frownmouth -surprised
show serena -surprisedbrow -frownmouth -surprised
with dis

may -surprisedbrow -frownmouth -surprised @sadbrow happymouth "Wow... I can't believe you found a Charmander. I've always wanted to study them! The way their tail-flame works is super-interesting."

brendan @talking2mouth "Seriously. If I were you, I woulda caught the guy."

red @closedbrow talking2mouth "Yeah... well, like I said, it was injured."

red @happy "And besides that, I don't have any balls."

pause 2.0

leaf @sarcastic "Really? No-one? No-one's going to say anything? Fine."

red @talkingmouth "So, what are you guys doing now?"

serena @talkingmouth "My Houndour has caught a scent. We're following it."

red @happy "Sounds good. Let's go!"

$ renpy.music.play("Audio/pokemon/cries/228.mp3", channel="altcry", loop=None)
$ sidemonnum = 228
sidemon @talkingmouth "Hound! Dour!"

serena @happy "Yes, boy? Have you discovered something?"

$ renpy.music.play("Audio/pokemon/cries/228.mp3", channel="altcry", loop=None)
sidemon @talkingmouth "Dooooour!"

leaf @happy "Awesome! I just hope it's not something really common.{w=0.5}{nw}"
extend @sarcastic " I didn't walk all this way just to find some silly Rattata."

ethan happy "Yeah, Sentret are {i}way{/i} better! {color=#377CAB}#JohtoLife{/color}"

pause 2.0

show brendan:
    ease 0.8 xpos 1.2
show calem:
    ease 0.9 xpos 1.2
show leaf: 
    ease 0.6 xpos 1.2
show brendan:
    ease 0.7 xpos 1.2
show serena:
    ease 0.5 xpos 1.2
show may:
    ease 0.7 xpos 1.2

pause 0.5

show ethan -happy surprised with dis
    
$ renpy.pause(1.0, hard=True)

ethan "Wha-guys! Wait up!"

hide ethan with dis

pause 2.0

show brendan at farleftside
show may at leftside
show ethan at midleftside behind may
show calem at farrightside
show serena at rightside
show leaf at midrightside behind serena
with dis

calem @talkingmouth "Quite curious.{w=0.5} Your Houndour is clearly tracking {i}something{/i}, but I certainly don't see any Pokémon around here."

leaf @sarcastic "Hmm... have you considered using your nose?"

calem @talkingmouth "Believe it or not, no."

brendan @talking2mouth "That's the problem, man. You need to really get your nose in there!"

show brendan thinking with dis:
    ease 1.0 xzoom -1 xpos 0.3 ypos 1.5 rotate 35

brendan "{w=1.0}{i}*SNIFF*{/i} {w=1.0}{i}*SNIFF*{/i} {w=1.0}{i}*SNIFF*{/i}"

may @sadbrow happymouth "Oh... sweetie, I don't think..."

show brendan angrybrow frownmouth with dis:
    ease 0.4 xpos .5 ypos 1.0 rotate 0

show fields1 with vpunch

brendan @angrybrow talking2mouth "Hey! That rock bit me!"

ethan @surprised "What? A {i}rock{/i} bit you?"

brendan @talking2mouth "Yeah! That round one there, with the brick-like pattern!"

pause 2.0

$ PlaySound("idea.ogg")

show brendan surprisedbrow frownmouth
show may surprisedbrow frownmouth
show ethan surprisedbrow frownmouth
show calem surprisedbrow frownmouth
show serena surprisedbrow frownmouth
show leaf surprisedbrow frownmouth
with dis

red @talkingmouth "That's no rock!"

play music "Audio/Music/RBY_Pokemon_Start.ogg" noloop
queue music "Audio/Music/RBY_Pokemon_Loop.ogg"
    
leaf @talking2mouth "Wait, don't tell me..."

$ renpy.music.play("Audio/pokemon/cries/27.mp3", channel="altcry", loop=None)
$ sidemonnum = 27
sidemon @talkingmouth "Sandshrew!"

serena -surprisedbrow -frownmouth -surprised @happy "I knew Houndour's nose wouldn't lead us wrong!"

calem -surprisedbrow -frownmouth -surprised @closedbrow talking2mouth "So this was the Pokémon Houndour found.{w=0.5} It seems we disturbed its midday nap."

ethan -surprisedbrow -frownmouth -surprised @happy "Sweet! I've never seen a Sandshrew up this close before!"

show leaf -surprisedbrow -frownmouth -surprised
show may -surprisedbrow -frownmouth -surprised 
with dis

ethan @angrybrow happymouth "All right, stand back. This one's m--"

brendan @angrybrow happymouth "Hold it!{w=0.5} I called that one!"
    
brendan @closedbrow talkingmouth "May and I had a deal.{w=0.5} She got the Venonat, so I get the next Pokémon we find!"

ethan @confused "Okay, sure, but do I look like April?"

leaf @sarcastic "You might look cute in her clothes."

ethan @happy "Really? I was thinking the same thing, actually! Hey, April, could I--"

may @angrybrow talking2mouth "Absolutely not."

ethan @sad "Aw..."

redmind @confused "Well, that's a part of our personalities that are... {i}very{/i} different."

calem @closedbrow talking2mouth "I'm afraid I'll have to side with Brendan here, Ethan. He {i}did{/i}, technically, find the Sandshrew. With his nose."

ethan @sad "Aw, et tu, Calamari? What about you, Serena? I mean, it was your Houndour that brought us here."

serena @sad "Apologies, but I agree with Calem."

ethan @closedbrow talking2mouth "{size=30}There's a surprise...{/size}"

red @talkingmouth "Don't worry, Ethan, I'm sure there are plenty of other Pokémon out there for you to catch."

ethan @closedbrow talking2mouth "Fiiiiiine..."

brendan angrybrow happymouth "C'mon, Mudkip!{w=0.5} Let's show this Sandshrew what a great team we'll be!"

$ renpy.music.play("Audio/pokemon/cries/258.mp3", channel="altcry", loop=None)
$ sidemonnum = 258
sidemon @talkingmouth "Mudkip!"

$ inventory[Item.PokeBall] = 20

$ trainer1 = Trainer("brendan", TrainerType.Player, [GetTrainerTeam("Brendan", "Mudkip"), GetTrainerTeam("Brendan", "Shroomish")])
$ trainer2 = Trainer("sandshrew", TrainerType.Enemy, [GetTrainerTeam("Brendan", "Sandshrew")], isPokemon=True)

call Battle([trainer1, trainer2], gainexp=False, specialmusic="Nothing", unrunnable=True) from _call_Battle_9
$ battlehistory["Sandshrew1"] = _return
if (GetTrainerTeam("Brendan", "Sandshrew", False) in playerparty):
    $ AddEvent("Brendan", "CaughtSandshrew")
else:
    $ AddEvent("Brendan", "NotCaughtSandshrew")
$ ballsused = 20 - GetItemCount("Poké Ball")
if (Item.PokeBall in inventory.keys()):
    $ del inventory[Item.PokeBall]

if (GetTrainerTeam("Brendan", "Sandshrew", False) in playerparty):
    $ playerparty.remove(GetTrainerTeam("Brendan", "Sandshrew", False))

play music "Audio/Music/Fieldstheme_Start.ogg" noloop
queue music "Audio/Music/Fieldstheme_Loop.ogg"

if (WonBattle("Sandshrew1")):
    show brendan happy with dis

    brendan "Yeah! I beat it!"

    if (HasEvent("Brendan", "CaughtSandshrew")):
        may @happy "Congratulations on catching your new Sandshrew, sweetheart!"

        $ ValueChange("Brendan", 3, 0.5)
        
        brendan -happy @surprised "Yeah, I really didn't think I'd be able to do it!"

        if (ballsused != 1):
            brendan @happy "And it only took [ballsused] Poké Balls!"
        else:
            brendan @happy "And it only took one Poké Ball!"

        may @talkingmouth "Here, sweetie, I've got some potions. Let's heal the little guy up."

        $ PlaySound("Heal_A.ogg")

    else:
        may @sadbrow happymouth "Er... sweetheart? Weren't you trying to catch it?"

        $ ValueChange("Brendan", -1, 0.5)

        brendan @surprised "Ah, geez. I completely forgot about that, and got carried away..."
        
        may @sadbrow happymouth "It's alright, babe. We can go out another day and get one!" 

else:
    show brendan surprisedbrow frownmouth with dis

    brendan "Uh... did I just get my butt kicked by a wild Sandshrew?"

    $ ValueChange("Brendan", -3, 0.5)

    brendan -surprisedbrow -frownmouth -surprised @closedbrow talkingmouth "That's kinda embarrassing."

    may @talkingmouth "Here, sweetie, I've got some potions. Let's heal your little guys up."

    $ PlaySound("Heal_A.ogg")

pause 1.0

leaf @happy "I can't hold it in anymore! That looked so exciting!"

red @surprised "Huh?"

leaf @happy blush "The battle, [first_name]! {i}I{/i} really want to battle now."

ethan @closedbrow talking2mouth "Uh... okay. Well, why don't you?"

leaf @happy blush "That's a great idea, Ethan!"

ethan @surprised "Huh? What's gotten into you?"

leaf @flirttalk "C'mon, [first_name]. You're not going to make me battle against May and Brendan alone, are you?"

red @talkingmouth "I wasn't aware you were battling in the first place, but I guess not?"

brendan @angrybrow happymouth "Huh, no offense, you two, but you've got no chance. May 'n I've been battling together since we were kids!"

may @angrybrow happymouth "But we're more than happy to show you the power of a long-term relationship in action!"

redmind @thinking "Who says that?"

leaf @angrybrow blush happymouth "Oh, I'm pretty sure you're going to eat those words!"

$ trainer1 = Trainer("red", TrainerType.Player, playerparty)
$ trainer2 = MakeTrainer("Leaf", TrainerType.Ally)
$ trainer3 = MakeTrainer("May")
$ trainer4 = MakeTrainer("Brendan")
call Battle([trainer1, trainer2, trainer3, trainer4]) from _call_Battle_10
$ battlehistory["BrendanMay1"] = _return

$ timeOfDay = "Evening"
    
play music "Audio/Music/Fieldstheme_Start.ogg" noloop
queue music "Audio/Music/Fieldstheme_Loop.ogg"

show brendan
show may at leftside
show leaf at midrightside behind serena
with dis

show fields1b behind ethan with dis:
    alpha 1.0

show fields1:
    alpha 1.0
    ease 10 alpha 0.0

if (WonBattle("BrendanMay1")):
    brendan @happy "Hey! Nice battlin', dude!"

    may @surprised "Wow, you two make a great team already!"

    leaf @happy "It's because our Pokémon are best friends, just like their trainers. And {i}nothing{/i} beats the power of friendship!"

    brendan -happy @talking2mouth "Yeah, well, it was fun. Let's battle again soon, yeah? I gotta patch up my wounded pride, y'know!"

    python:
        ValueChange("Leaf", 1, 0.63, False)
        ValueChange("May", 1, 0.25, False)
        ValueChange("Brendan", 1, 0.5)

else:
    leaf -happy @angrybrow angrysmilemouth "Aw, what? C'mon, [first_name]. And after I talked you up?"

    red @sadbrow happymouth "Sorry. Swear I did my best."

    leaf @flirttalk "Well, you know, performance issues. One out of every five or something like that, right?"

    red @closedbrow talking2mouth "Ugh. Low blow."

serena @closedbrow talking2mouth "{i}*Yawn*{/i} Oh dear.{w=0.5} Please pardon my yawn. The sun is setting, though, is it not? What time is it?"

calem @closedbrow talking2mouth "By my estimate..."
calem @surprised "Wait, what am I thinking? I have a phone. I'll just check that."
calem @frownmouth "[ellipses]"
calem @talkingmouth "Seven."

brendan @closedbrow talkingmouth "We should probably start headin' back then. Sorry you guys didn't all get to catch some new 'mons."

may @sadbrow happymouth "Aw, we barely got to break into the snacks!"

brendan @happy "Eh, they're probably all just, like, cookies and things, right?"

may frownmouth @talking2mouth "...Yes."

leaf @happy "Hey, I'll take your snacks."

may @closedbrow talking2mouth "Well, I'm glad {i}someone{/i} will.{w=0.5} Hold on, let me get one for you."
    
$ renpy.pause(1.5, hard=True)

$ PlaySound("Unzip.ogg")

may @surprised "[ellipses]"

$ renpy.pause(1.0, hard=True)

may @closedbrow talking2mouth "Huh. That's weird...{w=0.5} I could've sworn I packed some cookies in here..."

calem @closedbrow talking2mouth "...Did you ever leave your bag unattended when we were letting the Pokémon roam freely, May?"

may @sad "...I think so."

$ renpy.music.play("Audio/pokemon/cries/228.mp3", channel="altcry", loop=None)
$ sidemonnum = 228
sidemon @talkingmouth "Hound..."

redmind "That's a guilty-looking Houndour, if I've ever seen one."

serena @angrybrow poutmouth "Houndour! You didn't!"

may @happy "It's fine! I put some extra cookies in Brendan's bag, just in case something like this happened!"

brendan surprisedbrow frownmouth @surprised "Huh? W-wait!"

$ PlaySound("Unzip.ogg")

brendan closedbrow frownmouth @surprisedmouth "Eh... yeah. I, uh, fed those to Mudkip and Shroomish a while ago."

may angrybrow frownmouth @angry "Brendan! I made those for {i}you!{/i}"

brendan @surprised "I know that! But I don't like sweet things, May!"

may "[ellipses]"

brendan sadbrow -frownmouth @happymouth "E-except for you, sweetheart?"

may closedbrow poutmouth "Hmph."

redmind "{w=0.25}.{w=0.25}.{w=0.25}.Bit awkward. This is usually where Calem changes the subject."

show brendan -sadbrow -happymouth
show may -closedbrow -poutmouth
with dis

calem @talkingmouth "Well, our first priority--to get more wild Pokémon--may have been less than a resounding success. But this is fine. We'll simply come back another day."

serena @talkingmouth "Yes, that sounds like a good plan. In addition to catching wild Pokémon, this could also be a good place to train. Though other trainers are, of course, best for that."

red @closedbrow talking2mouth "Yeah, I might come back here another day. I'll have to see how my schedule is."

leaf @talking2mouth "If you're going out somewhere, give one of us a call!"

red @surprised "Oh, yeah. I forgot I could do that, I guess. Back in Pallet, if I wanted to talk to someone, I'd just walk to their house. I might actually have a use for this phone, now."

leaf @happy "That's right! So get to calling, skippy! What's the point of having friends all over the school if they're not blowing your phone up to make you seem popular?"
    
red @sadbrow happymouth "I really couldn't say."

pause 0.75

call clearscreens from _call_clearscreens_47

hide leaf
hide ethan
hide brendan
hide calem
hide serena
show blank2 
with splitfade

$ renpy.pause(1.0, hard=True)

red @happy "Well, we didn't end up with any new friends today, but there's always next time, right, buddy?"

$ renpy.music.play("Audio/Pokemon/pikachu_norm1.ogg", channel="altcry", loop=None)
pikachu neutral "Pikachu!"

$ renpy.music.stop(channel='crowd', fadeout=1.0)
scene dorm_B norm with Dissolve(2.0)
    
stop music fadeout 2.5

queue music "Audio/Music/Road to Viridian City.ogg"

red @talkingmouth "Okay. Texting. Using a phone for anything but pictures is kinda a weird concept for me, but Leaf told me to, so... let's see, who can I get in contact with?"

call texting from _call_texting_1

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_48

show blank2 with dis:
    alpha 1.0
    
$ renpy.pause(2.5, hard=True)

jump day010411
