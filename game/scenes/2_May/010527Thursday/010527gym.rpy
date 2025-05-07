label gym010527:

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

narrator "You are listening intently to the lecture, when, suddenly..."

blue uniform @closedbrow talkingmouth "{size=30}Psst.{/size}"

red uniform @surprised "{size=30}Huh? What is it?{/size}"

if (HasEvent("Leaf", "AcceptedConfession")):
    blue @talkingmouth "{size=30}I'm calling in that favor you owe me.{/size}"

    red @surprised "{size=30}Already?!"

elif (GetRelationshipRank("Blue") > 0):
    blue @closedbrow talkingmouth "{size=30}Remember that time we were training in the fields? And you apologized for your... you know?{/size}"

    red @talking2mouth "{size=30}Yeah. I apologized for not realizing you needed attention from your grandfather too.{/size}"

    blue @lightblush angry "{size=30}Don't phrase it like that!{/size}"

    red @confused "{size=30}That's exactly what happened, though...{/size}"
    red @closedbrow talking2mouth "{size=30}Anyway, you didn't actually accept that apology.{/size}"

    blue @closedbrow talkingmouth "{size=30}Yeah. I'm willing to reconsider that. I just need you to do me a favor.{/size}"

else:
    blue @closedbrow talkingmouth "{size=30}I need you to do me a favor.{/size}"

    red @unamusedbrow talking2mouth "{size=30}I see absolutely no reason to.{/size}"

    blue @angry "{size=30}At least hear me out! This is something that will benefit you too!{/size}"

red @closedbrow talking2mouth sweat "{size=30}Geez... alright, what is it?{/size}"

blue @wistfulbrow talkingmouth "{size=30}Uh... Ethan and Yellow are pissed at me.{/size}"

red @confused "{size=30}Huh? Them? No way. I mean, I don't really know Yellow as well as you do, but she always seems so gentle, and I'm pretty sure Ethan doesn't ever get angry.{/size}"

blue @closedbrow talkingmouth "{size=30}You're wrong.{/size}"

pause 1.0

redmind @confusedeyebrows frownmouth "Just that? 'You're wrong?' No insults, no sarcasm?"

pause 0.5

redmind @thinking "Maybe this {i}is{/i} real, then."

red @talking2mouth "{size=30}Okay. Assuming they really {i}are{/i} angry at you, why? And how do I fit into this?{/size}"

blue @closedbrow talkingmouth "{size=30}...So, my Eevee can make those Foreverals, right? But they're based on 'bonds' or 'understanding' or whatever.{/size}"
blue @wistful "{size=30}So... Ethan and I were having a conversation. Like, a good one. No screaming. And I kinda started to get him a bit more.{/size}"
blue @angry "{size=30}But then Eevee threw up those stones, and now Ethan and Yellow both think I was just trying to get the damn stones! And I mean, I am, but not {i}then{/i}, and not with him!{/size}"

pause 0.5

blue @closedbrow talkingmouth "{size=30}So... I need you to explain what's what to them.{/size}"

red @closedbrow talking2mouth sweat "{size=30}Dude, this is {i}your{/i} problem. Just tell them the truth, and--{/size}"

blue @angry "{size=30}I {i}did!{/i} And they didn't believe me! Can you believe that?{/size}"

pause 1.0

redmind @sadbrow frownmouth "...I can't. Which is the problem, I guess."

red @closedbrow talking2mouth "{size=30}Alright. I can't promise anything, but I'll talk to them after school. Do you know where they'll be?{/size}"

blue @closedbrow talkingmouth "{size=30}They've been spending a lot of time alone together... just in the dorm, though.{/size}"

red @talking2mouth "{size=30}Alright. But, again, I can't promise anything.{/size}"

pause 1.0

blue @closedbrow talkingmouth lightblush "{size=30}Uh... thanks.{/size}"

narrator "Blue quickly walks away, as Alder finishes lecturing..."

redmind @closedbrow frownmouth "Hm... Ethan and Yellow, huh? I don't think it should be {i}too{/i} hard to explain to them what really happened..."
redmind @surprisedbrow frownmouth "Oh! I wonder if that's why Blue hasn't been around for lunch for the past couple days?"

alder @happy2 "And that's it for today. Ah, my throat's sore. I need some water, if I'm going to be talking for so long. Bruno, who are our battlers for today?"

bruno @norm2 "[first_name]. Today, you are matched against Bianca."

hide bruno 
hide alder
with dis

pause 1.0

show tia uniform hat with dis

if (GetRelationshipRank("Tia") > 0):
    tia @happy "Hi, [first_name]!"

else:
    tia @happy "[tiafont]Hi, [first_name]{/font}!"

red @happy "Hey."

if (HasEvent("Klara", "AcceptCoordinatorClub")):
    red @talkingmouth "You looked like you were having a lot of fun in that Coordinator Club meeting on Tuesday."

    $ ValueChange("Tia")

    if (GetRelationshipRank("Tia") > 0):
        tia @happy "Thank you!"
        tia @sadbrow talking2mouth "Lisia is really, {i}really{/i} [tiafont]passionate{/font} about her work. I always thought that [tiafont]contests{/font} were more about having fun..."
        tia @happy "But I'm doing my best! I really want to help her win the... the... [tiafont]Million Doodle Weirdo Fantasy Cricketmatch!{/font}"

        red @happy "I'm sure you'll do great."

    else:
        tia @happy "Thank you! [tiafont]I did my best{/font}!"

        narrator "Tia looks like she intends to sign some more, but hesitates, and her hands remain still. Perhaps she doesn't think you'd be able to understand."

        redmind @thinking "Well, that's progress. When we first met, it seemed like she expected {i}everyone{/i} to know JSL."

red @talkingmouth "Now, shall we battle?"

if (GetRelationshipRank("Tia") > 0):
    $ AddEvent("Tia", "InternetBadInfluence")
    tia @happy "Let's bust this day's [tiafont]balls{/font}!"

    pause 1.0

    red @surprised "Uh, where did you learn that?"

    tia @talkingmouth "There's a [tiafont]person{/font} on the [tiafont]internet{/font} who makes really funny videos."
    tia @happy "She says it a lot!"

    red @closedbrow talking2mouth sweat "You... might want to not say that around people."

    tia @surprised "Oh? But Whitney likes when I say it."

    red @sad2eyes sadeyebrows talking2mouth "...I think she should be monitoring your internet usage a bit more carefully."

    tia @happy "Oh, no, she [tiafont]introduced{/font} me to the funny [tiafont]internet{/font} woman!"

    red @unamusedbrow talking2mouth "Great. Then maybe I should be."

    pause 1.0

    tia frownmouth @angrybrow poutmouth "You know, I'm not a kid."

    red @surprised "Wha--no, I know that! I wasn't saying you were."

    tia -frownmouth @closedbrow frownmouth "Okay."
    tia @happy "Let's battle, [tiafont]then{/font}!"

    red @sadbrow sweat talkingmouth "Y-yeah. Let's bust this day's balls."

else:
    tia @happy "[tiafont]Let's bust this day's balls{/font}!"

    red @talkingmouth sadbrow sweat "Ah-ha... yeah, you said it!"

    red @sadbrow sweat talkingmouth "Let's, uh, battle now."

python:
    trainer1 = MakeRed()
    trainer2 = MakeTrainer("Tia")

call Battle([trainer1, trainer2], uniforms=[True, True]) from _call_Battle_162
$ RecordBattle("Tia2")

show tia uniform hat with dis

stop music fadeout 1.5
queue music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

if (WonBattle("Tia2")):
    $ ValueChange("Tia", 3)

    if (GetRelationshipRank("Tia") > 0):
        tia @happy "Wow! You're so good at battling..."
        tia @sadbrow talkingmouth "I guess I have a lot to learn."

    else: 
        narrator "Tia signs a few complicated symbols before pausing..."

        show tia sadbrow with dis

        narrator "And giving you a thumbs-up."

        redmind uniform @closedbrow frownmouth "Well, I know what {i}that one{/i} means." 


else:
    if (GetRelationshipRank("Tia") > 0):
        tia @happy "Wow! I can't believe I won that!"

        red uniform @closedbrow talkingmouth "Well, you and your Pokémon can communicate on a level even better than me. It's not surprising."

    else: 
        narrator "Tia signs a few complicated symbols before pausing..."

        show tia sadbrow with dis

        narrator "And giving you a thumbs-up."

        redmind @closedbrow frownmouth "Well, I know what {i}that one{/i} means."

hide tia with dis

pause 1.0

show alder:
    xpos 0.66
show bruno think:
    xpos 0.33
with dis

jump lunchtransition