label gym010521:

$ HealParty()

stop music fadeout 1.5
queue music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

$ renpy.transition(dissolve)
show screen currentdate

scene gym with dis

show blank2 behind gym

$ renpy.pause(2.0, hard=True)

hide blank2

show alder with dis:
    xpos 0.66

show bruno think with dis:
    xpos 0.33

alder @happy2 "Well, that's the end of the lecture. Time for the big show, eh? We {i}did{/i} promise, after all."

raihan uniform @talkingmouth "Blimey. A real battle between an Elite Four and a Champion... and it's happening in a bog-standard gymnasium."

misty uniform @talkingmouth "That's how we do it everywhere but Galar."

raihan @happy "Oh, I know! I'm not complaining! It's just crazy to me that people can still have real battles like this without someone slapping a camera down, and trying to sell merch off it."

rosa uniform @surprisedbrow talking2mouth "...Oh. I was planning on recording this fight, actually..."

alder @happy2 "Haha! Video is fine, but no flash photography in the gymnasium, please! Bruno gets jumpy."

bruno @happy2 "Alder, you're stalling. Are you perhaps afraid of facing the strongest Fighting-type Master in Kanto?"

alder @happy2 "Not a chance, friend! Just building up the audience with a bit of trash talk."

bruno @happy2 "Hm. Trash talk, eh?"

show alder surprisedbrow frownmouth with dis

bruno @norm2 "Well... I am given to understand that your skills are subpar."
bruno @think2 "Further, your movements are sluggish and unpracticed."

pause 2.0

bruno @sad2 "I'm... not good at trash talk, am I?"

alder -surprisedbrow -frownmouth @happy2 "You're a hell of a lot better at battling than you are at trash-talking."

bruno @happy2 "Perhaps this is a new discipline in which I must train."

alder @sadbrow happymouth "Hey, if there's a man out there who I trust to master something new, it'd be you."

bruno @happy2 "You are too kind. I almost regret this trouncing I am about to deliver."

alder @happy2 "Hey, there we go! That's better."
alder @talkingmouth "Alright, let's get this started. This is still part of the team battle unit, so would anyone like to volunteer to partner with me?"

narrator "Alder seems to be looking in your direction..."

menu:
    ">Volunteer":
        $ AddEvent("Alder", "Volunteer")
        narrator "You raise your hand."

        alder @happy2 "[first_name], sure. Why don't you give it a shot? This is your chance to battle alongside a champion."

        red uniform @happy "I'm very grateful, Sir. I'll do my best not to let you down."

        alder @happy2 "None of that, now. We're partners on the battlefield. Your success is just as important as mine."
    
    ">Do not volunteer":
        narrator "You keep still, and after a moment, Alder's eyes slide over to Leaf."

        alder @happy2 "Leaf. Why don't you give it a shot? This is your chance to battle alongside a champion."

        show leaf uniform:
            xpos 0.85 xzoom -1

        leaf uniform @happy "Yyyyes!"

bruno @norm2 "Hm... Bea. Assist me in this battle, please."

show bea uniform with dis:
    xpos 0.15

pause 1.0

bea @talkingmouth "Sir."

if (HasEvent("Alder", "Volunteer") and GetRelationshipRank("Bea") > 0):
    pause 1.0

    bea @talkingmouth "I hope you understand that this battle demands my full force, [first_name]. Regardless of our connection as teammates, and the help you have provided aside, I will come at you with my full force."

    red @talkingmouth "I expected nothing less."

alder @happy2 "Let's make this a nice, clean, fight."
alder happybrow happymouth @closedbrow talking2mouth "{size=30}Psst. Go for the eyes.{/size}"

if (HasEvent("Alder", "Volunteer")):
    red @surprised "What?!"

else:
    leaf @surprised "What?!"

if (not HasEvent("Alder", "Volunteer")):
    call clearscreens() from _call_clearscreens_192
    scene blank2 with splitfade

    narrator "The Team of Alder and Leaf easily defeats Bea and Bruno. Truthfully... even though you know Leaf to be a strong battler, it didn't seem like her presence was even required."

    stop music fadeout 1.5

    $ renpy.transition(dissolve)
    call clearscreens from _call_clearscreens_193

    $ renpy.pause(2.0, hard=True)

    $ HealParty()

    scene blank2
        
    show afternoon at vspaz
        
    pause 3.5

    $ timeOfDay = "Afternoon"

    show cafe behind blank2
    $ renpy.music.play("Audio/bigcrowdloop.ogg", channel='crowd', loop=True, fadein=0.5)

    queue music "Audio/Music/Route 1 Anime.ogg"

    $ renpy.transition(dissolve)
    show screen currentdate

    hide blank2 with splitfade
    $ renpy.pause(0.5, hard=True)

    hide afternoon

    $ jumpto = "lunch"
    $ jumptoyear = "01"
    $ jumptomonth = ("0" if calDate.month < 10 else "") + str(calDate.month)
    $ jumptodate = ("0" if calDate.day < 10 else "") + str(calDate.day)
    $ renpy.jump(jumpto + jumptoyear + jumptomonth + jumptodate)

python:
    trainer1 = MakeTrainer("Alder", TrainerType.Ally)
    trainer2 = MakeRed()
    trainer3 = MakeTrainer("Bea")
    trainer4 = MakeTrainer("Bruno")

call Battle([trainer1, trainer2, trainer4, trainer3], uniforms=[False, True, False, True], customexpressions=["alder", "alder angrybrow happymouth", "red uniform", "red uniform angrybrow happymouth", "bruno", "bea uniform", "bruno angry", "bea uniform angrybrow happymouth"]) from _call_Battle_150
$ RecordBattle("BeaBruno1")

show alder:
    xpos 0.66
show bruno think:
    xpos 0.33
show bea uniform:
    xpos 0.15
with dis

if (WonBattle("BeaBruno1")):
    bea @closedbrow talking2mouth "As expected of my worthy teammate. Sir, Bruno, I apologize."

    bruno @norm2 "There is nothing to apologize for. With further training, it will be {i}me{/i} who has the honor of partnering with you."
    bruno @norm4 "Stand proud. You are strong."

    $ ValueChange("Bea", 3, 0.15)

    bea @closedbrow talkingmouth "Thank you, Sir."

    hide bea with dis

    alder @happy2 "I'm afraid that a compliment from me just won't seem as impactful as one from Bruno, but you did real good, [first_name]. Keep battling like that, and I don't see any reason why you couldn't be a champion."

else:
    alder @surprisedbrow frownmouth "Eh? I didn't see that coming..."

    bruno @norm2 "Hm. This is not how our battles normally resolve. Were you distracted, my friend?"

    alder @closedbrow talking2mouth "Guess I was. I suppose everyone has off days... been having them a lot more recently, it seems."

    narrator "Alder seems troubled, but the moment passes."

    alder @happy2 "Ah, but it wasn't just my own missteps that caused this. You two are strong. Very strong. Seems you might have found an apprentice, eh, Bruno?"

    bruno @happy2 "Perhaps. Bea, with further training, it will be {i}me{/i} who has the honor of partnering with you."

    bea @closedbrow talkingmouth "Thank you, Sir."

    hide bea with dis

    alder @happy2 "I'm afraid that a compliment from me just won't seem as impactful as one from Bruno, but you did real good, [first_name]. Even though we lost, keep battling like that, and I don't see any reason why you couldn't be a champion."

red uniform @surprisedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

red @sadbrow talkingmouth "Thanks. Thank you so much."

alder @happy2 "You earned it, kid. Well done."

jump lunchtransition