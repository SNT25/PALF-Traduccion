label windsweptwoods: #flying-type dungeon, should be hard-difficulty, partners are Rosa, Nessa, Raihan and Sonia
$ HealParty(Trainer("rosa", TrainerType.Enemy, GetTrainerTeam("Rosa")))
$ HealParty(Trainer("nessa", TrainerType.Enemy, GetTrainerTeam("Nessa")))
$ HealParty(Trainer("sonia", TrainerType.Enemy, GetTrainerTeam("Sonia")))
$ HealParty(Trainer("raihan", TrainerType.Enemy, GetTrainerTeam("Raihan")))

if (timeOfDay == "Night"):
    if ("Raihan" in GetStudents("All")):
        show rosa at night:
            xpos 0.2
        show nessa at night:
            xpos 0.4
        show raihan at night:
            xpos 0.6
        show sonia at night:
            xpos 0.8
        with dis
    else:
        show rosa at leftside, night
        show sonia at rightside, night
        show nessa at night
        with dis

else:
    if ("Raihan" in GetStudents("All")):
        show rosa:
            xpos 0.2
        show nessa:
            xpos 0.4
        show raihan:
            xpos 0.6
        show sonia:
            xpos 0.8
        with dis

    else:
        show rosa at leftside
        show sonia at rightside
        show nessa
        with dis

rosa @talkingmouth "Okay, are we all ready?"

nessa @talkingmouth "Not so fast. Sonia, what did your survey say?"

sonia @talking2mouth "Looks like this part of the forest is called the 'Windswept Woods.' The especially tall trees cause wicked air currents up top. Flying-types make this place their home, in addition to the expected Grass-types."

rosa @surprised "Huh?"

nessa @talkingmouth "We staked the place out to figure out what kind of wild Pokémon we might find. Honestly, Rosa, you could stand to think ahead a bit."
nessa @closedbrow talkingmouth "There's no stunt double to take your place. No reshoots on this stage, if anything goes wrong."

rosa @sadbrow sweat sadmouth "I'm... yeah. You're right."

nessa @closedbrow talkingmouth "You're doing the right thing. Let's just do it smartly."

if ("Raihan" in GetStudents("All")):
    raihan @happy "We don't need to do this smartly, girls. You've got The Great Raihan here. My Rock-types will make these Flying-types embarrassed to have wings!"

sonia @talking2mouth "Right, [first_name]. If you've got any Foreverals that give [pika_name] the Ice-type, now might be a good time to use them."
sonia @closedbrow talking2mouth "Or... perhaps Electric, or Rock, or Flying, or Fire...? Hm..."

menu:
    "I'm ready.":
        rosa @talkingmouth "Allllright! We're {i}totally{/i} going to write a story here! A {i}real{/i} adventure!"

        nessa @talkingmouth "...This'd all sort itself out in the end, but... why wait?"

        sonia @talking2mouth "[first_name]. Reckon you could use [pika_name] in battle a good bit? I'd like to get some more data on him."

        if ("Raihan" in GetStudents("All")):
            raihan @talking2mouth "Seconding that. I'd like to see what the slayer of Jobbird can do up-close."

            if (timeOfDay == "Night"):
                red night @closedbrow talkingmouth sweat "Maybe don't call Dawn's Altaria that anymore..."

            else:
                red @closedbrow talkingmouth sweat "Maybe don't call Dawn's Altaria that anymore..."

    "Hold on a mo'.":
        hide rosa
        hide nessa
        hide sonia
        hide raihan
        with dis

        if (timeOfDay == "Night"):
            jump aftersetupnight

        else:
            jump aftersetup

python:
    fullsquad = [MakeRed(), MakeTrainer("Rosa", TrainerType.Ally), MakeTrainer("Nessa", TrainerType.Ally), MakeTrainer("Sonia", TrainerType.Ally)] + ([MakeTrainer("Raihan", TrainerType.Ally)] if "Raihan" in GetStudents("All") else [])
    wildpool = [
        pokedexlookupname("Swablu", DexMacros.Id), 
        pokedexlookupname("Rowlet", DexMacros.Id), 
        pokedexlookupname("Hoothoot", DexMacros.Id),
        pokedexlookupname("Hoppip", DexMacros.Id),
        pokedexlookupname("Paras", DexMacros.Id)
    ]
    activedungeon = Dungeon("forest", "Windswept Woods", fullsquad, wildpool, "toweringarborage", "forestdungeonloss", 9, AimLevel() + 1, 
        dungeoncutscenefunc=None, 
        fudgerollfunc=None, 
        eventfunc=None,
        generateitems=[(20, "Gimmighoul Coin"), (10, "Chesto Berry"), (10, "Oran Berry"), (9, "Sitrus Berry"), (5, "Sharp Beak"), (5, "Miracle Seed")])

stop music fadeout 1.5
queue music "audio/music/duskforest.ogg"

$ HealParty()

jump StartDungeon

label toweringarborage:

$ technicaldungeon = True

stop music fadeout 1.5
queue music "audio/music/potown_start.ogg" noloop
queue music "audio/music/potown_loop.ogg"

if (timeOfDay == "Night"):
    if ("Raihan" in GetStudents("All")):
        scene midnightforest
        show rosa at night:
            xpos 0.2
        show nessa at night:
            xpos 0.4
        show raihan at night:
            xpos 0.6
        show sonia at night:
            xpos 0.8
        with dis
    else:
        scene midnightforest
        show rosa at leftside, night
        show sonia at night
        show nessa at rightside, night
        with dis

else:
    if ("Raihan" in GetStudents("All")):
        scene eveningforest
        show rosa:
            xpos 0.2
        show nessa:
            xpos 0.4
        show raihan:
            xpos 0.6
        show sonia:
            xpos 0.8
        with dis
    else:
        scene eveningforest
        show rosa at leftside
        show sonia 
        show nessa at rightside
        with dis

rosa @sweat sadbrow talking2mouth "Oh man... we're through... I'd rather spend seven months shooting in the jungles of Fiore than do that again."

sonia @sadbrow talkingmouth "...Brr. It's chilly."

nessa @talkingmouth "Are you two seriously whining about this? It was just a short hike."

if ("Raihan" in GetStudents("All")):
    raihan @happy "Yeah, I'm with Ness! That was nothing."

rosa @angrybrow talking2mouth "Speak for yourself! I'm used to having my air-conditioned trailer whenever I'm within fifty feet of a tree!"

nessa @closedbrow talkingmouth "What a surprise. You're more of a princess than I thought."

rosa @surprised "P-Princess?! I-- {i}why, I never!{/i}"

stop music fadeout 1.5

show rosa surprised
show nessa surprised
show sonia surprised
with dis

if ("Raihan" in GetStudents("All")):
    show raihan surprised with dis

redmind @surprised "[sabrinacolor]Help.{/color}"

sonia sadbrow frownmouth @talking2mouth "You lot heard that, right?"

rosa sadbrow frownmouth @talking2mouth "Yeah. That was definitely Sabrina."

if ("Raihan" in GetStudents("All")):
    raihan @surprised "...So, this is the girl you called me to help? Alright."

nessa angrybrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

queue music "audio/music/lavenderintense_start.ogg" noloop
queue music "audio/music/lavenderintense_loop.ogg"

nessa @talkingmouth "There."

hide sonia
hide rosa
hide nessa
hide raihan
with dis

pause 1.0

if (timeOfDay == "Night"):
    show sabrina poweredbrow casualoldhair at night with Dissolve(1.0):
        ypos 0.9 xpos 0.5
        parallel:
            ease 2.0 ypos 0.95
            ease 2.0 ypos 0.9
            repeat

        parallel:
            ease 2.0 xpos 0.52
            ease 2.0 xpos 0.5
            ease 2.0 xpos 0.48
            ease 2.0 xpos 0.5
            repeat

else:
    show sabrina poweredbrow casualoldhair with Dissolve(1.0):
        ypos 0.9 xpos 0.5
        parallel:
            ease 2.0 ypos 0.95
            ease 2.0 ypos 0.9
            repeat

        parallel:
            ease 2.0 xpos 0.52
            ease 2.0 xpos 0.5
            ease 2.0 xpos 0.48
            ease 2.0 xpos 0.5
            repeat

if (timeOfDay == "Night"):
    rosa night @talkingmouth "...Sabrina!"
else:
    rosa @talkingmouth "...Sabrina!"

if (timeOfDay == "Night"):
    nessa night @surprised "She looks different." 
else:
    nessa @surprised "She looks different." 

if (timeOfDay == "Night"):
    sonia night @sadbrow talking2mouth "Did you do something new with your hair?"
else:
    sonia @sadbrow talking2mouth "Did you do something new with your hair?"

if ("Raihan" in GetStudents("All")):
    if (timeOfDay == "Night"):
        raihan night @closedbrow talking2mouth "Hey, I'm suddenly a {i}lot{/i} more into this rescue mission."
    else:
        raihan @closedbrow talking2mouth "Hey, I'm suddenly a {i}lot{/i} more into this rescue mission."

rosa @angrybrow talking2mouth "Now's not the time for jokes! We have to save her!"

nessa @talkingmouth "Granted, but from what? She looks fine... if a bit exposed."

if (not HasEvent("Nessa", "OutfitSwap")):
    sonia @talkingmouth "{i}You're{/i} saying that, Ness?"

    nessa @closedbrow talkingmouth "It's {i}my{/i} choice. I just want to make sure that that was hers."

if (timeOfDay == "Night"):
    red night @angrybrow talking2mouth "...Sabrina?"
else:
    red @angrybrow talking2mouth "...Sabrina?"

sabrina @talking2mouth "{font=fonts/alien.ttf}We come ... ... ... ... ... ... ... ... ... for ...!{/font}"

red @surprised "What? What are you coming for...?"

sabrina @talking2mouth "{font=fonts/alien.ttf}... ... a great treasure ... us ... ... coming for ... ... ... ... our treasure!{/font}"

if (GetRelationshipRank("Sabrina") > 0):
    red @sad "This... isn't her. Something's controlling her."

else:
    rosa @sad "This... isn't her. Something's controlling her."

sonia @angrybrow talkingmouth "I reckoned. We might need to prepare for a nasty fight, then."

red @angrybrow talking2mouth "Alright. Let's go."

python:
    nessabattles = False
    soniabattles = False
    rosabattles = False
    raihanbattles = False
    redbattles = True
    cheer = None
    raihanalive = False
    nessaalive = False
    soniaalive = False
    rosaalive = False
    if (activedungeon != None):
        for mob in activedungeon.Party:
            if (mob.Name == "nessa" and mob.GetTeam()[0].Health > 1):
                nessaalive = True
                nessabattles = True
            elif (mob.Name == "sonia" and mob.GetTeam()[0].Health > 1):
                soniaalive = True
                soniabattles = True
            elif (mob.Name == "rosa" and mob.GetTeam()[0].Health > 1):
                rosaalive = True
                rosabattles = True
            elif (mob.Name == "raihan" and mob.GetTeam()[0].Health > 1):
                raihanalive = True
                raihanbattles = True

if (not nessaalive):
    nessa @sad "...I'm sorry, I can't. My Drednaw was wiped out in the forest."

if (not soniaalive):
    sonia @sad "I... feel right awful about this, honest, but Yamper's a bit knackered right now..."

if (not rosaalive):
    rosa @sad "Sorry, but my partner's exhausted from the forest. I gotta step out for this one."

if ("Raihan" in GetStudents() and not raihanalive):
    raihan @sad "My new mon's wiped out. Sorry. Hadn't trained it well enough, yet."

$ battlers = redbattles + nessaalive + soniaalive + rosaalive + raihanalive
$ cheer = []

if (battlers > 3):
    red @closedbrow talking2mouth "Wait... there's more than three of us. We'll probably get in each other's way if we all fight at once."

    nessa @talkingmouth "Someone should step out."

    rosa @surprised "Sh-she's coming fast! [first_name], what's the script?"

    while (battlers > 3):
        menu:
            "Rosa, exit stage left." if (rosabattles):
                $ rosabattles = False
                $ cheer.append(Stats.Accuracy)

                narrator "Rosa stands back and directs the scene! Your Accuracy increased!"

            "Nessa, step back for this one." if (nessabattles):
                $ nessabattles = False
                $ cheer.append(Stats.SpecialDefense)

                narrator "Nessa steps behind and guards your back! Your Special Defense increased!"

            "Sonia, sit this one out." if (soniabattles):
                $ soniabattles = False
                $ cheer.append(Stats.Attack)

                narrator "Sonia stands back and cheers you on! Your Attack increased!"

            "Raihan, take a picture of this." if ("Raihan" in GetStudents() and raihanbattles):
                $ raihanbattles = False
                $ cheer.append(Stats.SpecialAttack)

                narrator "Raihan stands back and cheers you on! Your Special Attack increased!"

            "I'll back off here." if (redbattles):
                $ redbattles = False

                if ("Raihan" in GetStudents("All")):
                    $ ValueChange("Nessa", 3, 0.2, False)
                    $ ValueChange("Rosa", 3, 0.4, False)
                    $ ValueChange("Sonia", 3, 0.6, False)
                    $ ValueChange("Raihan", 3, 0.8)

                    narrator "You stand back and cheer everyone on! Bonds increased!"
                    
                else:
                    $ ValueChange("Nessa", 3, 0.25, False)
                    $ ValueChange("Rosa", 3, 0.5, False)
                    $ ValueChange("Sonia", 3, 0.75)

                    narrator "You stand back and cheer on the girls! Bonds increased!"

        $ battlers = redbattles + nessabattles + soniabattles + rosabattles + raihanbattles  

narrator "Sabrina's emotions fluctuate through everyone's minds! The Mysteriosity empowers her Pokémon, while driving them crazy! Her Pokémon become [bluecolor]moody!{/color}"

python:
    sabrinaparty = GetTrainerTeam("Sabrina")
    trainer1 = MakeRed()
    trainer2 = Trainer("rosa", TrainerType.Ally, GetTrainerTeam("Rosa"))
    trainer3 = Trainer("nessa", TrainerType.Ally, GetTrainerTeam("Nessa"))
    trainer4 = Trainer("sonia", TrainerType.Ally, GetTrainerTeam("Sonia"))
    trainer5 = Trainer("sabrina", TrainerType.Enemy, GetTrainerTeam("Sabrina"), number=1, ignoresDungeons=True)
    trainer6 = Trainer("raihan", TrainerType.Ally, GetTrainerTeam("Raihan"))

    for mon in sabrinaparty:
        mon.ApplyStatus(".moody")

    trainers = []
    if (raihanbattles):
        trainers.append(trainer6)
    if (redbattles):
        trainers.append(trainer1)
    if (rosabattles):
        trainers.append(trainer2)
    if (nessabattles):
        trainers.append(trainer3)
    if (soniabattles):
        trainers.append(trainer4)
    trainers.append(trainer5)

    customexpressions = []
    for trainer in trainers:
        if (trainer.Name == "rosa"):
            customexpressions.append("rosa sad sweat")
            customexpressions.append("rosa angrybrow frownmouth")

        elif (trainer.Name == "nessa"):
            customexpressions.append("nessa frownmouth")
            customexpressions.append("nessa angry")

        elif (trainer.Name == "sonia"):
            customexpressions.append("sonia frownmouth")
            customexpressions.append("sonia angrybrow frownmouth")

        elif (trainer.Name == "sabrina"):
            customexpressions.append("sabrina casualoldhair poweredbrow")
            customexpressions.append("sabrina casualoldhair poweredbrow angrymouth")
        
        elif (trainer.Name == "raihan"):
            customexpressions.append("raihan frownmouth")
            customexpressions.append("raihan sad")

        elif (trainer.Name == "red"):
            customexpressions.append("red frownmouth")
            customexpressions.append("red angrybrow frownmouth")

        if (trainer.GetType() != TrainerType.Enemy):
            for mon in trainer.GetTeam():
                for cheertype in cheer:
                    mon.ChangeStats(cheertype, 1, mon)


call Battle(trainers, customexpressions=customexpressions, healParty = False, clearstats = False, specialmusic="Nothing", unrunnable=True, dialogfunc=possessedsabrinadialog, gainexp=(redbattles)) from _call_Battle_126
$ battlehistory["Sabrina2"]  = _return

if (not WonBattle("Sabrina2")):
    jump forestdungeonloss

queue music "audio/music/lavender_start.ogg" noloop
queue music "audio/music/lavender_loop.ogg"

if ("Raihan" in GetStudents("All")):
    if (timeOfDay == "Evening"):
        show rosa frownmouth:
            xpos 1.0/6.0
        show sabrina casualoldhair closedbrow:
            xpos 2.0/6.0
        show sonia frownmouth:
            xpos 3.0/6.0
        show nessa frownmouth: 
            xpos 4.0/6.0
        show raihan frownmouth:
            xpos 5.0/6.0
        with dis
    else:
        show rosa frownmouth at night:
            xpos 1.0/6.0
        show sabrina casualoldhair closedbrow at night:
            xpos 2.0/6.0
        show sonia frownmouth at night:
            xpos 3.0/6.0
        show nessa frownmouth at night: 
            xpos 4.0/6.0
        show raihan frownmouth at night:
            xpos 5.0/6.0
        with dis

else:
    if (timeOfDay == "Evening"):
        show rosa frownmouth: 
            xpos 0.2
        show sabrina casualoldhair closedbrow: 
            xpos 0.4
        show sonia frownmouth: 
            xpos 0.6
        show nessa frownmouth: 
            xpos 0.8
        with dis
    else:
        show rosa frownmouth at night: 
            xpos 0.2
        show sabrina casualoldhair closedbrow at night: 
            xpos 0.4
        show sonia frownmouth at night: 
            xpos 0.6
        show nessa frownmouth at night: 
            xpos 0.8
        with dis

pause 1.0

rosa @sadmouth "...Sabrina?"

if ("Raihan" in GetStudents("All")):
    if (timeOfDay == "Evening"):
        show sabrina:
            xpos 0.4
            block:
                ease 0.02 xpos 2.0/6.0 - 0.01
                ease 0.02 xpos 2.0/6.0
                ease 0.02 xpos 2.0/6.0 + 0.01
                ease 0.02 xpos 2.0/6.0
                repeat 5
    else:
        show sabrina at night:
            xpos 0.4
            block:
                ease 0.02 xpos 2.0/6.0 - 0.01
                ease 0.02 xpos 2.0/6.0
                ease 0.02 xpos 2.0/6.0 + 0.01
                ease 0.02 xpos 2.0/6.0
                repeat 5

else:
    if (timeOfDay == "Evening"):
        show sabrina:
            xpos 0.4
            block:
                ease 0.02 xpos 0.39
                ease 0.02 xpos 0.4
                ease 0.02 xpos 0.41
                ease 0.02 xpos 0.4
                repeat 5
    else:
        show sabrina at night:
            xpos 0.4
            block:
                ease 0.02 xpos 0.39
                ease 0.02 xpos 0.4
                ease 0.02 xpos 0.41
                ease 0.02 xpos 0.4
                repeat 5

sabrina "{size=30}Nngh.{/size}"

sonia @happy "She's snapping out of it!"

sabrina -closedbrow @sadbrow talking2mouth "Where..."

if ("Raihan" in GetStudents("All")):
    if (timeOfDay == "Evening"):
        show raihan surprisedbrow:
            xpos 5.0/6.0
        show nessa surprisedbrow:
            xpos 4.0/6.0
        show rosa surprisedbrow:
            xpos 1.0/6.0
        show sonia surprisedbrow:
            xpos 3.0/6.0
        with dis

    else:
        show raihan surprisedbrow at night:
            xpos 5.0/6.0
        show nessa surprisedbrow at night:
            xpos 4.0/6.0
        show rosa surprisedbrow at night:
            xpos 1.0/6.0
        show sonia surprisedbrow at night:
            xpos 3.0/6.0
        with dis

else:
    if (timeOfDay == "Evening"):
        show nessa surprisedbrow:
            xpos 0.8
        show rosa surprisedbrow:
            xpos 0.2
        show sonia surprisedbrow:
            xpos 0.6
        with dis

    else:
        show nessa surprisedbrow at night:
            xpos 0.8
        show rosa surprisedbrow at night:
            xpos 0.2
        show sonia surprisedbrow at night:
            xpos 0.6
        with dis

sabrina @closedbrow angrymouth "Ah! My head, ow...{w=0.5} ow...{w=0.5}"

if ("Raihan" in GetStudents("All")):
    if (timeOfDay == "Evening"):
        show raihan -surprisedbrow:
            xpos 5.0/6.0
        show nessa -surprisedbrow:
            xpos 4.0/6.0
        show rosa -surprisedbrow:
            xpos 1.0/6.0
        show sonia -surprisedbrow:
            xpos 3.0/6.0
        with dis

    else:
        show raihan -surprisedbrow at night:
            xpos 5.0/6.0
        show nessa -surprisedbrow at night:
            xpos 4.0/6.0
        show rosa -surprisedbrow at night:
            xpos 1.0/6.0
        show sonia -surprisedbrow at night:
            xpos 3.0/6.0
        with dis

else:
    if (timeOfDay == "Evening"):
        show nessa -surprisedbrow:
            xpos 0.8
        show rosa -surprisedbrow:
            xpos 0.2
        show sonia -surprisedbrow:
            xpos 0.6
        with dis

    else:
        show nessa -surprisedbrow at night:
            xpos 0.8
        show rosa -surprisedbrow at night:
            xpos 0.2
        show sonia -surprisedbrow at night:
            xpos 0.6
        with dis

rosa @talking2mouth "Sabrina? You're safe, now. We came here to get you back."

sabrina @sadbrow talking2mouth "Get... get me back? What do you...? No, I came out here on purpose..."
sabrina @sadbrow talking2mouth "This... this was all part of the plan, but then... headaches, and... I was attacked. But... the plan..."

nessa @talkingmouth "Was being out here for almost a week part of your plan?"

sonia @surprisedbrow talkingmouth "What have you been {i}eating?{/i}"

sabrina @sadbrow talking2mouth "I... I..."

if ("Raihan" in GetStudents()):
    sabrina @surprisedbrow talking2mouth "Wait, {i}Raihan?{/i}"

    raihan @happy "Hey, another fan. Yeah, it's Raihan. You one of the Fang Gang?"

    $ ValueChange("Sabrina", 10, 2.0/6.0)

    sabrina @talking2mouth "I... follow your RotoPhoto stories..."

    nessa @talkingmouth "Sabrina. Don't blow up his head any more than it already is, okay? I need you to think back. What do you remember?"

pause 2.0

sabrina @closedbrow talking2mouth "I don't... remember. I remember the yelling, and the anger, then running out here, and... nothing."

if (GetRelationshipRank("Sabrina") > 0):

    sabrina @surprised "Wait... [first_name]?"

    if (timeOfDay == "Night"):
        red @happy "'Bout time you noticed. Just cause I'm not a supermodel doesn't mean I'm not here."

    else:
        red night @happy "'Bout time you noticed. Just cause I'm not a supermodel doesn't mean I'm not here."

    sabrina @talking2mouth "I... I thought you were leaving... I read-- I heard--"

    red @happy "Yeah, I did leave. And then I came back. What'd I say? You can't trust people's thoughts."

    sabrina @closedbrow talking2mouth "I'm... glad."

if ("Raihan" in GetStudents("All")):
    if (timeOfDay == "Evening"):
        show raihan surprised:
            xpos 5.0/6.0
        show nessa surprised:
            xpos 4.0/6.0
        show sonia surprised:
            xpos 3.0/6.0
        with dis

    else:
        show raihan surprised at night:
            xpos 5.0/6.0
        show nessa surprised at night:
            xpos 4.0/6.0
        show sonia surprised at night:
            xpos 3.0/6.0
        with dis

else:
    if (timeOfDay == "Evening"):
        show nessa surprised:
            xpos 0.8
        show sonia surprised:
            xpos 0.6
        with dis

    else:
        show nessa surprised at night:
            xpos 0.8
        show sonia surprised at night:
            xpos 0.6
        with dis

rosa @angry "Hold on! We've got something serious to discuss before we take you one step further, Sabrina!"

sabrina @sad "I... I know. I'm so sorry. I didn't mean to reveal everyone's secrets. I shouldn't have snapped at-"

if ("Raihan" in GetStudents("All")):
    if (timeOfDay == "Evening"):
        show raihan -surprised:
            xpos 5.0/6.0
        show nessa -surprised:
            xpos 4.0/6.0
        show sonia -surprised:
            xpos 3.0/6.0
        with dis

    else:
        show raihan -surprised at night:
            xpos 5.0/6.0
        show nessa -surprised at night:
            xpos 4.0/6.0
        show sonia -surprised at night:
            xpos 3.0/6.0
        with dis

else:
    if (timeOfDay == "Evening"):
        show nessa -surprised:
            xpos 0.8
        show sonia -surprised:
            xpos 0.6
        with dis

    else:
        show nessa -surprised at night:
            xpos 0.8
        show sonia -surprised at night:
            xpos 0.6
        with dis

rosa @happy "Where did you get that {i}adorable{/i} tank top?"

sabrina surprised "Huh?"

nessa @talkingmouth "Seriously, a crop/tank-top with low-rise jeans? That's fashion, if I've ever seen it. You're more daring than I thought."

sabrina sadbrow surprisedmouth "I... it's just... a grocery store..."

sonia @surprised "Hold on, you're telling me you picked out {i}that{/i} cute outfit at a grocery store? What could you do in an actual clothes store?!"

nessa @closedbrow talkingmouth "I don't know, but I want to find out."

rosa @happy "Sounds like a trip to Forever 151 is in order!"
rosa @sadbrow talkingmouth "I... can't buy anything, but I can lend an eye, and--"

if ("Raihan" in GetStudents("All")):
    if (timeOfDay == "Evening"):
        show eveningforest with vpunch
        show sabrina poweredbrow angrymouth with dis:
            xpos 1.0/3.0
    else:
        show midnightforest with vpunch
        show sabrina poweredbrow angrymouth at night with dis:
            xpos 1.0/3.0
else:
    if (timeOfDay == "Evening"):
        show eveningforest with vpunch
        show sabrina poweredbrow angrymouth with dis:
            xpos 0.4
    else:
        show midnightforest with vpunch
        show sabrina poweredbrow angrymouth at night with dis:
            xpos 0.4

sabrina "N-no! You don't understand! I'm a witch--a curse! I'll only hurt you if you try to get closer to me! I'll expose everything about you!"

pause 1.0

if (GetRelationshipRank("Sabrina") > 0):
    red @talkingmouth "Sabrina."

    if (timeOfDay == "Evening"):
        show sabrina sadbrow with dis:
            xpos (0.4 if "Raihan" not in GetStudents("All") else 1.0/3.0)
    else:
        show sabrina sadbrow at night with dis:
            xpos (0.4 if "Raihan" not in GetStudents("All") else 1.0/3.0)

    red @talkingmouth "Yeah, you exposed me. But it wasn't your fault. And, in the long run, I think you did me a favor."

rosa @talking2mouth "Sabrina. You know what my darkest secret is?"

if (timeOfDay == "Evening"):
    show sabrina sadbrow -angrymouth with dis:
        xpos (0.4 if "Raihan" not in GetStudents("All") else 1.0/3.0)
else:
    show sabrina sadbrow -angrymouth at night with dis:
        xpos (0.4 if "Raihan" not in GetStudents("All") else 1.0/3.0)

sabrina @sadbrow talking2mouth "...Yes."

rosa @happy "And so does everyone else. It's literally on every single one of my wiki pages."

nessa @talkingmouth "I've made a couple of mistakes. Most of them involving Raihan. And he told {i}everyone.{/i} He didn't even have Esper powers as an excuse."

if ("Raihan" in GetStudents()):
    raihan @sad "Guilty as charged. Not proud of it, though. I just have trouble keeping my mouth shut when something great happens."

sonia @talkingmouth "I'm not quite sure I have anything like a 'secret,' but... well, I reckon I've already done the most embarrassing thing that could happen to me this year, what with begging Janine to let me back into the Battle Team."

sabrina @talking2mouth "I... maybe, then, but..."

nessa @talkingmouth "Come on. You don't need to make any decisions right now. The thing we need to do now is get you back to the school."

if ("Raihan" not in GetStudents()):
    if (timeOfDay == "Evening"):
        show nessa:
            xpos 0.8
            ease 0.2 xpos 0.85
        show rosa:
            xpos 0.2
            ease 0.2 xpos 0.05
        show sonia:
            xpos 0.6
            ease 0.2 xpos 0.75
        with dis

    else:
        show nessa at night:
            xpos 0.8
            ease 0.2 xpos 0.85
        show rosa at night:
            xpos 0.2
            ease 0.2 xpos 0.05
        show sonia at night:
            xpos 0.6
            ease 0.2 xpos 0.75
        with dis

    pause 1.0

    red @confusedeyebrows frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    red @talkingmouth "Oh, so just because I'm the only guy here, I'm the one who has to carry her."

    nessa @talkingmouth "Go on. Be a gentleman."

else:
    sonia @talking2mouth "Rai, could you give her a hand?"

    if (GetRelationshipRank("Sabrina") > 0):
        raihan @closedbrow talking2mouth "Sure, but... I dunno... [last_name], maybe I'm being presumptuous, but I get the feeling you'd rather do it?"

    else:
        raihan phone @talking2mouth "Sorry. Gotta keep my hands free for this victory selfie I'm about to snap. [last_name], think you've got a hand free for a pretty girl?"

        nessa @closedbrow "{size=30}Ugh. The only thing worse than Raihan's flirting is when he tries to wingman for you.{/size}"

        show raihan -phone with dis

sabrina @sadbrow talking2mouth "I... I can walk by myself..."

menu:
    "Take my hand.":
        $ ValueChange("Sabrina", -3, (0.4 if "Raihan" not in GetStudents("All") else 1.0/3.0))

    "You don't need to, though.":
        pass

    "Alright.":
        $ ValueChange("Sabrina", 3, (0.4 if "Raihan" not in GetStudents("All") else 1.0/3.0))

        sabrina @closedbrow talking2mouth "Thank you, but..."

pause 1.0

sabrina @sadbrow talking2mouth "No."

pause 1.0

red @confused "No?"

sabrina @talking2mouth "They... those students... they targeted me {i}because of you.{/i}"

sonia sad "Steady on, Sabrina." 

nessa sad "That wasn't his fault."

sabrina @closedbrow angrymouth "I know! It wasn't anyone's fault but my own. But I... I..."

if (GetRelationshipRank("Sabrina") > 0):
    sabrina @closedbrow angrymouth "I {i}told{/i} you to stay away from me! The very first time we met, that was {i}all{/i} I asked for!"

    sabrina @sad "Why... why didn't you...?"

    red @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    redmind @sadbrow frownmouth "...She did, didn't she...?"
    redmind @sadbrow frownmouth "I... I guess I thought... that I could make you happier than leaving you alone would make you."

    pause 2.0

    rosa sad "I understand you're upset, Sabrina. [first_name] does, too. Don't take it out on him. You two were friends, right? You told me about him in our classes together." 

    sabrina @talking2mouth "I didn't think through the consequences. I thought... I thought I knew what kinds of heartbreak the future held. {size=30}I couldn't have predicted this.{/size}"

else:
    sabrina @closedbrow sadmouth "I know."

    sabrina @sadbrow talking2mouth "You did everything right."

    $ ValueChange("Sabrina", 10, (0.4 if "Raihan" not in GetStudents("All") else 1.0/3.0))

    sabrina @closedbrow angrymouth "You even stayed away from me, which was all I asked for. If I can't keep people safe when they do everything right, when {i}I{/i} do everything right, then what can I..."

    rosa sad "I understand you're upset, Sabrina. [first_name] does, too. Don't take it out on him, or yourself."

menu:
    "It was Cheren's fault.":
        $ AddEvent("Sabrina", "CherenFault")
        $ ValueChange("Sabrina", -1, (0.4 if "Raihan" not in GetStudents("All") else 1.0/3.0))

        sabrina @talking2mouth "...Not wholly."

        if (timeOfDay == "Evening"):
            show sabrina sad with dis:
                xpos (0.4 if "Raihan" not in GetStudents("All") else 1.0/3.0)
        else:
            show sabrina sad at night with dis:
                xpos (0.4 if "Raihan" not in GetStudents("All") else 1.0/3.0)

        redmind @sadbrow frownmouth "[sabrinacolor]I'm sorry. I need... I need space. And time.{/color}"

    "It was those two students' fault.":
        $ AddEvent("Sabrina", "AceFault")
        $ ValueChange("Sabrina", -1, (0.4 if "Raihan" not in GetStudents("All") else 1.0/3.0))

        sabrina @talking2mouth "...Not wholly."

        if (timeOfDay == "Evening"):
            show sabrina sad with dis:
                xpos (0.4 if "Raihan" not in GetStudents("All") else 1.0/3.0)
        else:
            show sabrina sad at night with dis:
                xpos (0.4 if "Raihan" not in GetStudents("All") else 1.0/3.0)

        redmind @sadbrow frownmouth "[sabrinacolor]I'm sorry. I need... I need space. And time.{/color}"

    "It was your fault.":
        $ AddEvent("Sabrina", "YourFault")
        $ ValueChange("Sabrina", -5, (0.4 if "Raihan" not in GetStudents("All") else 1.0/3.0))

        sabrina @talking2mouth "...Not wholly."

        if (timeOfDay == "Evening"):
            show sabrina sad with dis:
                xpos (0.4 if "Raihan" not in GetStudents("All") else 1.0/3.0)
        else:
            show sabrina sad at night with dis:
                xpos (0.4 if "Raihan" not in GetStudents("All") else 1.0/3.0)

        redmind @sadbrow frownmouth "[sabrinacolor]I'm sorry. I need... I need space. And time.{/color}"

    "It was my fault.":
        $ AddEvent("Sabrina", "MyFault")
        $ ValueChange("Sabrina", 3, (0.4 if "Raihan" not in GetStudents("All") else 1.0/3.0))
        if (GetRelationshipRank("Sabrina") > 0):
            redmind sadbrow frownmouth "I'm sorry, Sabrina. You're right. I should have listened. But now the damage has been done, and I don't want to stop being friends with you."

            redmind "[sabrinacolor]Have you considered what {i}I{/i} want?{/color}"

            redmind "Do {i}you{/i} want to stop being friends?"

            if (timeOfDay == "Evening"):
                show sabrina sad with dis:
                    xpos (0.4 if "Raihan" not in GetStudents("All") else 1.0/3.0)
            else:
                show sabrina sad at night with dis:
                    xpos (0.4 if "Raihan" not in GetStudents("All") else 1.0/3.0)

            redmind "[sabrinacolor]...No. Maybe. I don't know. I just need... I need space. And time.{/color}"
        else:
            sabrina @talking2mouth "...Not wholly."

if (GetRelationshipRank("Sabrina") > 0):
    $ PlaySound("sav.ogg")
    $ AddEvent("Sabrina", "WasFriend")
    $ persondex["Sabrina"]["Relationship"] = "...?"
    $ persondex["Sabrina"]["RelationshipRank"] = 0
    narrator "Your heart shifts as you feel your relationship with Sabrina evolve from '{color=#0048ff}Friend{/color}' to '{color=#0048ff}...?{/color}'!"

pause 1.0

rosa @talkingmouth "I think we could all do with some space. And some time. Let's head back to the campus grounds, alright?"

sabrina -sad @closedbrow talking2mouth "Alright."

pause 1.0

sabrina @sad "I... I don't want to seem ungrateful."

sonia -sad @talking2mouth "You've been through a lot. Anyone would get it."

nessa @talkingmouth "I'm sure I'd feel the same."

if ("Raihan" in GetStudents()):
    raihan @talkingmouth "I just joined up to help a friend."
    raihan @closedbrow talking2mouth "I'm not really sure what your deal is, but we've got no beef. I don't expect any thanks. Just doing what I do."

sabrina @closedbrow sadmouth "I... I really am... I..."

rosa @sadbrow talkingmouth "Hey. It's alright. We understand."

pause 1.0

$ ValueChange("Sabrina", 3, 0.4)

pause 1.0
    
if (timeOfDay == "Evening"):
    show eveningforest with vpunch
else:
    show midnightforest with vpunch

rosa @happy "Yahahaha!"

if (rosaalive):
    rosa -sad @talkingmouth "Oh, man, I can't believe we pulled that off! This was so risky, but so exciting, but so dangerous, but so {i}fun!{/i} This could be a new movie!"

    if ("Raihan" not in GetStudents()):
        $ ValueChange("Rosa", 5, 0.05)

    else:
        $ ValueChange("Rosa", 5, 1.0/6.0)

else:
    rosa @sadbrow talkingmouth "That was amazing! I... really hurt right now, and I've got all kinds of bumps and aches and stuff, but we pulled it off!"

if (nessaalive):
    nessa -sad @talkingmouth "...I'm not going to say you were right, Rosa, but maybe doing the proactive thing was the right call. {i}This{/i} time."

    if ("Raihan" not in GetStudents()):
        $ ValueChange("Nessa", 5, 0.85)

    else:
        $ ValueChange("Nessa", 5, 4.0/6.0)

else:
    nessa @sadbrow angrymouth "I... {i}nngh{/i}. Oh, I'm going to feel that in the morning. Guess one of them got a lucky blow on me."

if (soniaalive):
    if ("Raihan" not in GetStudents()):
        $ ValueChange("Sonia", 5, 0.75)
    else:
        $ ValueChange("Sonia", 5, 3.0/6.0)

    sonia -sad @happy "The important thing is that we succeeded. Worse for wear or not, we set up a plan, and saw it through to the end. No quitting mid-way."

    sonia @sadbrow talkingmouth "Kinda reminds you of the Galarian Stars, Ness?"

    nessa @closedbrow talkingmouth "Hm."

else:
    sonia @closedbrow talking2mouth "Well... we may not be whole... but we made it through all the way, without quitting. {size=30}{i}Ah.{/i} That's a nasty bruise.{/size}"

if ("Raihan" in GetStudents()):
    if (raihanalive):
        $ ValueChange("Raihan", 5, 5.0/6.0)

        raihan @happy "So, uh, I'm glad that I got to be part of this wicked adventure and all. Really does remind me of the Galarian Stars, and how we all were in the beginning..."
        raihan @surprised "But could someone explain what this was all about? Who are you, Sabrina? Why did you run out here? What did you mean, exposing secrets?"
        raihan @closedbrow sadmouth "I kinda got the idea that you're a Mental, but--"

        nessa @talkingmouth "Uh, ixnay on the ental-May. They call them 'Espers' in this region."

        raihan @talking2mouth "Okay. ...Context?"

        sonia @sadbrow happymouth "Oh, where do we start...?"

    else:
        raihan @happy "So, uh, I'm glad that I got to be part of this wicked adventure and all. Really does remind me of the Galarian Stars, and how we all were in the beginning..."
        raihan @sadmouth "But I got my ass kicked up and down that forest for hours, and I'd like some context, now. Only Leon can kick my ass. Not... birds, or mushrooms, or whatever."
        raihan @confused "Could someone explain what this was all about? Who are you, Sabrina? Why did you run out here? What did you mean, exposing secrets?"
        raihan @closedbrow sadmouth "I kinda got the idea that you're a Mental, but--"

        nessa @talkingmouth "Uh, ixnay on the ental-May. They call them 'Espers' in this region."

        raihan @talking2mouth "Okay. ...Context?"

        sonia @sadbrow happymouth "Oh, where do we start...?"

call clearscreens() from _call_clearscreens_152
show blank2 with splitfade

pause 1.0

narrator "Everyone makes their way back to the infirmary, battered and bruised."

$ AddEvent("Sabrina", "Rescued")

if ("Raihan" in GetStudents()):
    $ AddEvent("Raihan", "WasRescueTeam")

$ rescuedsabrina = True
$ lastsaved = "Sabrina"
$ technicaldungeon = False
$ _rollback = True
$ renpy.block_rollback()

jump infirmary