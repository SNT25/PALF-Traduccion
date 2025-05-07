label secondhomeroom010521:

scene blank2 with splitfade

pause 1.0

stop music fadeout 1.5
queue music "audio/music/celebi_start.ogg" noloop
queue music "audio/music/celebi_loop.ogg"

scene homeroom 
show screen currentdate
show kris sadbrow
with splitfade

narrator "The mood in your homeroom is subdued. Everyone is acutely aware that this might be the last homeroom you get with Professor Cherry."
narrator "...Which means, soon, you'll go back to being taught by Professor Oak... who, although you love, it's become apparent that he may not be the best teacher."

kris @talkingmouth "I wish that I had more time with you."

show whitney uniform frownmouth with dis:
    xpos 0.25

whitney @talking2mouth "What happens when you leave, though?"

kris -sadbrow @talkingmouth "Well, Doctor Oak will come back, resuming classes just like before."

show hilbert uniform with dis:
    xpos 0.75

show kris sadbrow angrymouth 
hide whitney
with dis

hilbert @talkingmouth "And what? We're just supposed to endure this subpar education, when you've shown us what we {i}could{/i} be having?"

kris @talkingmouth "...Doctor Oak is a genius."

hilbert @closedbrow talkingmouth "He's incompetent."

show blue angry uniform:
    xpos 0.85

show hilbert uniform:
    xpos 0.75
    ease 0.5 xpos 0.65 xzoom -1

show kris surprisedbrow angrymouth with dis

blue @talkingmouth "You shut up. That's {i}our teacher{/i} you're talking about."

hilbert @sadbrow talkingmouth "Our teacher? What has he taught us? Oak has taught fifty-four homerooms. That amounts to one hundred and eight hours."
hilbert @talkingmouth "What would you do with an extra one hundred and eight hours, if they were yours to spend as you wish?"
hilbert @closedbrow talkingmouth "Would you attend one of Oak's classes? Or do something else?"

hide hilbert with dis

pause 1.0

blue closedbrow angrymouth "{size=30}Tch. You'll pay for that during the Battle Team meeting.{/size}"

hide blue with dis

pause 1.0

show kris closedbrow with dis

pause 2.0

kris -closedbrow -angrymouth @talkingmouth "Please... don't argue."

blue uniform @closedbrow talkingmouth "I'm over it."

hilbert uniform @closedbrow talkingmouth "We've moved on."

redmind uniform @upeyes frownmouth "'...And other fun lies to tell yourself.'"

kris @talkingmouth "Well, given this is my last class with you all, I think I should probably give you something that I think will help you in the future. I've found them to be very useful when it comes to capturing Pokémon."

show flannery uniform with dis:
    xpos 0.15

flannery @talking2mouth "Hm? Something like the TM for False Swipe, or maybe Hold Back?"

show whitney uniform with dis:
    xpos 0.35

whitney @talking2mouth "It's gotta be some kind of powerful status move, right?"

hide whitney
hide flannery
with dis

kris @talkingmouth "Good guesses, everyone. But it's something with a bit more versatility."
kris @happy "Here. Why don't I just show you?"

show pokeballs_full with Dissolve(2.0):
    xalign 0.5

red uniform @talkingmouth "Woah! We're going to get a new Pokémon?"

kris @talkingmouth "Absolutely. An old neighbor of mine breeds them for me, for catching purposes, and, um..."
kris @sadbrow talkingmouth "Apparently, the male of this litter was a bit overenthusiastic."
kris @happy "So there's more than enough for each of you to pick one. I've trained each of them a little bit so that their levels aren't too low. Go ahead!"

pause 1.0

kris @talkingmouth "[first_name], why don't you come up first?"

$ sidemonnum = pokedexlookupname("Smeargle", DexMacros.Id)

show blank with dis

pause 0.5

$ PlaySound("Pokemon/Ball sound.ogg")

kris @talkingmouth "Oh, lovely!"

hide pokeballs_full

pause 1.5

$ renpy.music.play("Audio/pokemon/cries/{}.mp3".format(sidemonnum), channel="altcry", loop=None)

pause 1.0

$ renpy.music.play("Audio/Get.ogg", channel="XYgame", loop=None, fadeout=0.5)

hide blank with dis

show sideportraitfull at pokeball:
    pos (0.75, 0.85)

red @surprised "A... a {i}Smeargle?!{/i}"

kris @talkingmouth "That's right!"

red @talkingmouth "Aren't they incredibly rare, though?"

kris @talkingmouth "Not particularly. As I said, I got these from a breeder. But even back in Johto, you can find many of them in the ruins to the Southwest of Violet City."

red @sadbrow talkingmouth "I don't know what to say."

kris @talkingmouth "Then don't worry about saying anything. I hope you find it useful."
kris @talkingmouth "Now... Whitney, why don't you come here, now?"

whitney uniform @fullblush surprisedbrow frownmouth "{size=30}Yes, Miss.{/size}"

kris @happy "'Doctor', please!"

$ smeargleobj = Pokemon("Smeargle", level=20)
$ AddMon(smeargleobj, True)

call clearscreens() from _call_clearscreens_194
scene blank2 with splitfade

narrator "One-by-one, everyone comes up to collect their Smeargle from Professor Cherry."

pause 1.0

$ PlaySound("BellChime.ogg")

narrator "Soon, the bell rings, bringing an end to the class."
narrator "Professor Cherry gathers up a stack of papers, lifts the tray of leftover Poké Balls off the desk, and heads to the door."

kris @happy "Goodbye, class 1-B! It's been a pleasure."

narrator "And then she's gone."

pause 0.5

narrator "Though she {i}does{/i} take one more look back."

if (GetRelationshipRank("Professor Cherry") > 0):
    narrator "You've been investigating Professor Cherry for long enough that you recognize the expression on her face..."

    pause 0.5

    narrator "She's scared for you. And for what comes next."

    pause 0.5

    redmind uniform @sadbrow frownmouth "We'll be fine, Doctor. You've shown us the way. We'll figure this out ourselves from now on."
    redmind @thinking "And... just in case we can't..."
    redmind @happy "You're only a classroom away."

scene homeroom 
show screen currentdate
with dis

show leaf uniform with dis

pause 1.0

leaf @talking2mouth "...I'll miss her."
leaf @talkingmouth "What about you, [first_name]? I know you're good friends with Oak, so maybe it's not as clear-cut for you."

menu:
    "I'll miss her, too.":
        $ AddEvent("Professor Cherry", "IllMissHer")
        leaf @closedbrow frownmouth "Hm."
        leaf @talkingmouth "Maybe we can drop in on Ethan's class once in a while."

    "I don't know.":
        $ AddEvent("Professor Cherry", "UnsureMissHer")
        leaf @talkingmouth "That's fair. I get it. You've got lots of stuff pulling you in multiple directions."

    "I'm looking forward to Professor Oak coming back.":
        $ AddEvent("Professor Cherry", "WontMissHer")
        leaf @talkingmouth "That's fair. I get it. You've been friends with him for years. Professor Cherry was only our Professor for a Week."

leaf @talking2mouth "...Anyway, do you know what's up with Blue?"

red uniform @confused "Hm? What do you mean?"

leaf @talkingmouth "Like, he's being weirdly... {i}nice?{/i}"

leaf @sarcastic "Like, he asked me how my day was yesterday. And he was clearly bored as hell when I actually answered the question, but the fact he even asked it is something."

redmind @closedbrow frownmouth "I guess he's still trying to get more Foreverals, then..."

show leaf surprisedbrow frownmouth with dis

red @happy sweat "Maybe he's just trying to turn over a new Leaf."

pause 1.0

leaf -surprisedbrow @talkingmouth "That... was an {i}incredibly{/i} lame pun."

red @talkingmouth "Well, they can't all be winners. See you at the Battle Team meeting?"

leaf @happy "See you then!"

call freeroam() from _call_freeroam_28

scene stadium_empty
show screen currentdate
with Dissolve(2.0)

$ AddPikachu()
$ HealParty()

pause 0.5

show blue battleteam:
    xpos 1.0/9.0
show leaf battleteam:
    xpos 5.0/9.0
show sonia battleteam:
    xpos 8.0/9.0
show erika battleteam:
    xpos 6.0/9.0
show ethan battleteam:
    xpos 4.0/9.0
show silver battleteam:
    xpos 2.0/9.0
show bea battleteam behind ethan:
    xpos 3.0/9.0
show hilbert battleteam behind sonia:
    xpos 7.0/9.0
with dis

pause 1.0

show blue surprisedbrow frownmouth
show leaf surprisedbrow frownmouth 
show erika surprisedbrow frownmouth 
show ethan surprisedbrow frownmouth 
show silver surprisedbrow frownmouth 
show bea surprisedbrow frownmouth 
show sonia surprisedbrow frownmouth
show hilbert surprisedbrow frownmouth
with dis

stop music fadeout 4.0

show smoke:
    animation
    alpha 0.0 yalign 3.0 xalign 0.5
    parallel:
        ease 3.0 yalign 0.5
    parallel:
        ease 0.5 alpha 1.0
        pause 0.5
        ease 3.0 alpha 0.0 

pause 2.0

stop music
show screen songsplash("Fuchsia City", "Zame")

queue music "Audio/Music/fuchsia_start.ogg" noloop
queue music "audio/music/fuchsia_loop.ogg"


pause 1.0

show blank
show janine behind blank

pause 0.1

hide smoke
hide blank

show lance:
    xpos 1.1 ypos 1.0
    ease 0.5 xpos 0.66

show janine behind lance:
    ease 0.5 xpos 0.33

pause 1.0

janine @closedbrow talking2mouth "Line up."

show blue:
    ease 0.8 xpos 1.5
show leaf:
    ease 0.5 xpos -0.5
show erika:
    ease 1.0 xpos 1.5
show ethan:
    ease 0.4 xpos 1.5
    pause 0.2
    ease 0.4 xpos -0.5
show silver:
    ease 0.5 xpos -0.5
show bea:
    ease 0.5 xpos 1.5
show sonia:
    ease 0.5 xpos 1.5
show hilbert:
    ease 0.5 xpos -0.5

pause 1.0

hide blue
hide leaf
hide erika
hide ethan
hide silver
hide bea
hide sonia
hide hilbert

lance @angrybrow talking2mouth "Absolutely ridiculous. The notion that Drayden is even entertaining the thought of {i}that child{/i} returning to Kobukan..."

janine @angrybrow talking2mouth "{size=30}Lance, calm down. Now isn't the time.{/size}"

lance @upeyes talking2mouth "Not once in the high history of humanity has a person 'calmed down' when instructed to."

janine @talking2mouth "That's a fair point."
janine @talking2mouth "Let's just move on. As I mentioned, we need to begin training for Squad Battles."
janine @talkingmouth "I wasn't able to get a timeslot for earlier this week, so we'll do it now."

pause 0.5

janine @talking2mouth "I want all of you to be able to battle with, or against, each other."
janine @closedbrow talking2mouth "There is a nonzero chance that two or more of you will end up battling each other... again."

pause 0.5

janine @talking2mouth "So, I want all of you to battle three random teammates."

silver battleteam @surprisedbrow sadmouth "At {i}once?!{/i}"

janine @talking2mouth "No, one at--"

pause 0.5

janine @closedbrow talkingmouth "Hm. Actually, that might not be a bad idea."

silver @sad "Urgh... shouldn't've said anything..."

janine @smirkmouth "I'll go easy on you. It's... 'optional.'"

ethan battleteam @talking2mouth unamusedbrow "I heard those quotation marks."

janine @smirkmouth "I have 'no idea' what you mean."

pause 1.0

janine @talking2mouth "Alright, enough playing around. Let's start the allotments. [first_name], you're up first."

python:
    battlers = ["Sonia", "Hilbert", "Erika", "Leaf", "Silver", "Bea", "Ethan"]
    battler1 = random.choice(battlers)
    battlers.remove(battler1)
    battler2 = random.choice(battlers)
    battlers.remove(battler2)
    battler3 = random.choice(battlers)
    battlers.remove(battler3)
    chosenbattlers = [battler1, battler2, battler3]

pause 1.0

janine @talking2mouth "Looks like your opponents are... [battler1], [battler2], and [battler3]."

$ reactiontochosen = 0

label chosenreactions:

if (chosenbattlers[reactiontochosen] == "Sonia"):
    sonia battleteam @talking2mouth "Right. Let's have a good one, then."
    
elif (chosenbattlers[reactiontochosen] == "Hilbert"):
    hilbert battleteam @closedbrow talkingmouth "This should be good."

    blue battleteam @closedbrow talkingmouth "{size=30}Give him one for me, would you?{/size}"
 
elif (chosenbattlers[reactiontochosen] == "Erika"):
    if (HasEvent("Erika", "AcceptApology")):
        erika battleteam @happy "'Cry havoc and let loose the dogs of war!' Or so it is said."
    else:
        erika battleteam @sad "{w=0.5}.{w=0.5}.{w=0.5}."

elif (chosenbattlers[reactiontochosen] == "Leaf"):
    leaf battleteam @happy "Awesome! I think I've been helping you in battle a bit too long, [first_name]."
    leaf @angrybrow happymouth "I think it's about time I remind you who's the best battler in Dorm 25, [first_name]!"

    pause 1.0

    leaf @surprised "Uh, Blue? That was your key to butt in."

    blue battleteam @wistfulbrow wistfulmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    ethan battleteam @closedbrow talking2mouth "Guess he's distracted."

elif (chosenbattlers[reactiontochosen] == "Silver"):
    silver battleteam @talkingmouth "Good. It's been a while."

elif (chosenbattlers[reactiontochosen] == "Bea"):
    bea battleteam @talkingmouth "You are a worthy opponent. I have no objections."

    bea @talking2mouth "...Though it is amusing we will duel each other twice, today."

elif (chosenbattlers[reactiontochosen] == "Ethan"):
    ethan battleteam @talkingmouth "Hey, alright, let's do this."

    if (GetRelationshipRank("Ethan") > 0):
        ethan @winkbrow talkingmouth "I've got a new Pokémon that I bet you aren't expecting."

        if (156 in GetPartySpecies()):
            ethan @closedbrow sweat "Wait. You already have a Quilava. I'm an idiot."
            ethan @sad2eyes talkingmouth "Okay, so the gimmick here is that I {i}finally{/i} caught a Pokémon that you didn't already have, at least, I thought I did..."
            ethan @closedbrow talkingmouth "But I forgot you caught a Cyndaquil, so, yeah, that's on me. Just pretend this is a lot cooler than it actually is, okay?"

$ reactiontochosen += 1

if (reactiontochosen != 3):
    jump chosenreactions

janine @talking2mouth "And now, time to ask the big question. Think you can take on three of your teammates at once? In a 3v3 battle?"

menu:
    "I'll give it a try.":
        $ AddEvent("Janine", "ThrowThemAtMe")
        show lance angrybrow
        show janine surprisedbrow 
        with dis

        pause 1.0

        janine @smirkmouth "I'll be honest, I was just teasing you. But if you can actually pull this off..."

        if (HasEvent("Janine", "Domming")):
            janine -surprisedbrow @blush angrybrow smirkmouth "I might have to think outside of the box for your reward."

            redmind battleteam @surprisedbrow frownmouth lightblush "{w=0.5}.{w=0.5}.{w=0.5}."

            lance @sadbrow talking2mouth "I beg of you to move on."

            janine @talking2mouth "Right. Ready?"
            
        else:    
            janine @smirkmouth "I'll be very happy."

            janine @talking2mouth "Ready?"

        red battleteam @talking2mouth "Yes."

        python:
            trainer1 = MakeRed(3)
            trainer2 = MakeTrainer(chosenbattlers[0])
            trainer3 = MakeTrainer(chosenbattlers[1])
            trainer4 = MakeTrainer(chosenbattlers[2])

        call Battle([trainer1, trainer2, trainer3, trainer4], customoutfits=["battleteam", "battleteam", "battleteam", "battleteam"]) from _call_Battle_151
        $ RecordBattle("TeamBattleGroup1")
        
        show screen songsplash("Fuchsia City", "Zame")
        
        queue music "Audio/Music/fuchsia_start.ogg" noloop
        queue music "audio/music/fuchsia_loop.ogg"

        if (WonBattle("TeamBattleGroup1")):
            janine @closedbrow "{w=0.5}.{w=0.5}.{w=0.5}."

            redmind battleteam @thinking "Wait... did I do something wrong? I won, so..."

            $ ValueChange("Janine", 10, 0.25)

            janine @blush angrybrow smirkmouth "{i}Perfect.{/i}"

            if (HasEvent("Janine", "Domming")):
                redmind @surprisedbrow frownmouth lightblush "...Tingles."

            else:
                redmind @happy lightblush "Um... thanks."

        else:
            janine @closedbrow "{w=0.5}.{w=0.5}.{w=0.5}."
            janine @talking2mouth "Well, it was a long shot. Let's move on."

            redmind battleteam @closedbrow frownmouth "Ugh..."

    "Break it up for me, please.":
        show lance closedbrow with dis

        janine @talking2mouth "Alright. No shame in that."

        python:
            trainer1 = MakeRed()
            trainer2 = MakeTrainer(chosenbattlers[0])

        call Battle([trainer1, trainer2], customoutfits=["battleteam", "battleteam", "battleteam", "battleteam"]) from _call_Battle_152
        $ RecordBattle("TeamBattle1")

        show screen songsplash("Fuchsia City", "Zame")
        
        queue music "Audio/Music/fuchsia_start.ogg" noloop
        queue music "audio/music/fuchsia_loop.ogg"

        if (WonBattle("TeamBattle1")):
            $ ValueChange("Janine", 3)

            janine @talking2mouth "Well done. Next battle."

        else:
            janine @closedbrow talking2mouth "Hm. Next battle."

        python:
            trainer1 = MakeRed()
            trainer2 = MakeTrainer(chosenbattlers[1])

        call Battle([trainer1, trainer2], customoutfits=["battleteam", "battleteam", "battleteam", "battleteam"]) from _call_Battle_153
        $ RecordBattle("TeamBattle2")
        
        show screen songsplash("Fuchsia City", "Zame")
        
        queue music "Audio/Music/fuchsia_start.ogg" noloop
        queue music "audio/music/fuchsia_loop.ogg"

        if (WonBattle("TeamBattle2")):
            $ ValueChange("Janine", 3)

            janine @talking2mouth "Well done. Next battle."

        else:
            janine @closedbrow talking2mouth "Hm. Next battle."

        python:
            trainer1 = MakeRed()
            trainer2 = MakeTrainer(chosenbattlers[2])

        call Battle([trainer1, trainer2], customoutfits=["battleteam", "battleteam", "battleteam", "battleteam"]) from _call_Battle_154
        $ RecordBattle("TeamBattle3")

        show screen songsplash("Fuchsia City", "Zame")
        
        queue music "Audio/Music/fuchsia_start.ogg" noloop
        queue music "audio/music/fuchsia_loop.ogg"

        if (WonBattle("TeamBattle3")):
            $ ValueChange("Janine", 3)

            janine @talking2mouth "Well done. Overall..."

        else:
            janine @closedbrow talking2mouth "Overall..."

        $ battleswon = WonBattle("TeamBattle1") + WonBattle("TeamBattle2") + WonBattle("TeamBattle3")

        if (battleswon == 3):
            janine @smirkmouth "Well done."

        elif (battleswon == 2):
            janine @talking2mouth "...Alright."

        elif (battleswon == 1):
            janine @closedbrow talking2mouth "You can do better."

        else:
            janine @closedbrow talking2mouth "I'm sure I don't need to say anything."

            red battleteam @closedbrow talking2mouth "Yeah, sorry."

janine @talking2mouth "I'll assign some other groups now. Lance, please teach the trainers who just battled their rememberable moves."

lance @closedbrow talking2mouth "Of course."

pause 1.0

lance @upeyes talking2mouth "Let's just get this over with."
lance @talking2mouth "[first_name]. You know the routine."

label movetutor521:

call screen SelectMon
$ tutormon = _return

if (tutormon == 'back'):
    lance @closedbrow talking2mouth "Are you certain?"

    menu:
        "I don't want to teach any of my Pokémon one of their old moves.":
            lance @closedbrow talking2mouth "Very well."

        "On second thought...":
            jump movetutor521

elif (tutormon == pikachuobj):
    lance @talking2mouth "I am unable to teach this... creature. I cannot begin to determine what skills it may have possessed in the past."

    jump movetutor521

else:
    $ tutormon = _return
    $ tutormonname = pokedexlookup(tutormon.GetId(), DexMacros.Name)

    lance @talking2mouth "Your [tutormonname]. Very well."
    
    $ rememberablemoves = GetRememberableMoves(tutormon)

    if (len(rememberablemoves) == 0):
        lance @talking2mouth "This Pokémon has no moves it can remember. Avoid wasting my time, if you are capable of such a thing."

        jump movetutor521

    else:        
        lance @talking2mouth "Fine. What do you want me to re-teach this Pokémon?"

        $ learnmove = renpy.call_screen("rememberablemoves", tutormon)

        if (learnmove == "Back"):
            lance @talking2mouth "Avoid wasting my time, if you are capable of such a thing."

            jump movetutor521

        else:
            $ tutormon.LearnNewMove([(0, learnmove)])

            if (learnmove not in tutormon.GetMoveNames()):
                jump movetutor521

if (HasEvent("Rosa", "GiveToLeaf")):
    lance @talking2mouth "We are finished. However..."
    lance @sadeyes talking2mouth "It has not escaped me that Leaf Green, your battle teammate, is now sporting a {i}Pikachu{/i} on her team."
    lance @angrybrow talking2mouth "May I assume you had something to do with that?"

    red battleteam @happy "Actually, no! That was all Rosa."

    lance @shadow angrybrow "{w=0.5}.{w=0.5}.{w=0.5}."

    red @confused "What, you don't believe me?"

    lance @sadeyes talking2mouth "I {i}very{/i} much {i}wish{/i} I could disbelieve you."
    lance @closedbrow talking2mouth "As it happens, it seems I am forced to--though take this as no reprieve of my opinion of you."

hide lance with dis

if (HasEvent("Rosa", "GiveToLeaf")):
    redmind battleteam @unamusedbrow unamusedmouth "...Man's a full-time hater."

janine @closedbrow talking2mouth "...He was out of there in a hurry. Hm."

pause 1.0

janine @talking2mouth "Alright, now it's time to move to the general training."
janine @closedbrow talking2mouth "Focus especially hard on your battlefield awareness. In squad battles, opponents can come from any direction. You can't always guarantee yourself a 'fair' fight."
janine @talkingmouth "Of course, that doesn't mean you need to give your opponents a fair fight, either."
janine @talking2mouth "Get the drop on your opponent, and you've already won. Those of you taking my Dad's class should know that."
janine @talking2mouth "Anyway, in order to make you appreciate your normal awareness of the battlefield, we're going to be doing today's scrum battles with blindfolds on."

red battleteam @surprised "What?!"

janine @talkingmouth "I'll know if you're peeking. So don't."

call clearscreens() from _call_clearscreens_195
scene blank2 with splitfade

narrator "What follows is an hour of running into people, walls, and Pokémon at top speed. It is only a miracle that your nose does not end up broken."

$ BattleTeamTraining()

narrator "Tired and sore, you return to your dorm."

ethan battleteam @talking2mouth "...Dude, where did she get so many blindfolds?"

red battleteam @talking2mouth "I'm not going to think too hard about that."

jump day010522