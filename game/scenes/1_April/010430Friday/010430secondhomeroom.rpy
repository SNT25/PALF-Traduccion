label secondhomeroom010430:

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=True, fadein=1.0, tight=None)

scene blank2

show oakbg behind blank2
show homeroom behind oakbg

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with dis

$ PlaySound("BellChime.ogg")

oak @talkingmouth "...And that seems to wrap up the lecture! I hope to see you all in Relic Hall's auditorium on Saturday, yes?"

hide oakbg with dis

pause 0.5

redmind uniform @thinking "It's cool that our campaign was successful enough that even the teachers are paying attention to it."

redmind @happy "I guess the only thing left is the voting tomorrow."

pause 0.5

redmind @thinking "Well, that doesn't matter right now. If what Sabrina said about some sort of imminent battle is true, I should spend as much time as I can training before I have to go to the Battle Team meeting."

call freeroam from _call_freeroam_14

scene stadium_empty
show screen currentdate
with Dissolve(2.0)

$ AddPikachu()
$ HealParty()

pause 0.5

show blue:
    xpos 1.0/10.0
show leaf:
    xpos 6.0/10.0
show sonia:
    xpos 9.0/10.0
show erika:
    xpos 7.0/10.0
show ethan:
    xpos 4.0/10.0
show silver:
    xpos 2.0/10.0
show bea behind ethan:
    xpos 3.0/10.0
show dawn behind ethan:
    xpos 5.0/10.0
show hilbert behind sonia:
    xpos 8.0/10.0
with dis

pause 1.0

show blue surprisedbrow frownmouth
show leaf surprisedbrow frownmouth 
show erika surprisedbrow frownmouth 
show ethan surprisedbrow frownmouth 
show silver surprisedbrow frownmouth 
show bea surprisedbrow frownmouth 
show dawn surprisedbrow frownmouth
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
    ease 0.5 xpos 0.75

show janine behind lance:
    ease 0.5 xpos 0.25

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
show dawn:
    ease 0.2 xpos -0.5
show sonia:
    ease 0.5 xpos 1.5
show hilbert:
    ease 0.5 xpos -0.5

pause 1.0

janine @talking2mouth "Alright. Let's talk movesets."

janine @closedbrow talking2mouth "Who here has heard of the 'Flareon Theorem?'"

hide bea
hide leaf
hide erika
hide ethan
hide silver
hide blue
hide dawn
hide sonia
hide hilbert

bea @talkingmouth "{i}Hai.{/i} Flareon was a Pokémon who, for many years, was not thought to be able to learn a number of key moves."

janine happyneutralmouth @smirkmouth "That's right. Only in recent years did battle tutors learn how to teach Flareon the moves it needed to succeed."
janine @sad "...Of course, by that time, it had been pretty heavily powercrept out of the meta."
janine @closedbrow talking2mouth "Damn shame. They're insanely fluffy. I would have liked to use one."
janine @smirkmouth "Anyway, the reason I bring up Flareon is because you all need to understand how important movesets are for your Pokémon."

janine @closedbrow talking2mouth "My dad, the Indigo Elite Four Koga, would say that debuffing status moves are the most important kind."

lance @closedbrow talking2mouth "I would say that powerful moves are the most important kind."

janine @talking2mouth "Yes. And I would say that buffing status moves are the most important."

hilbert @closedbrow talkingmouth "You don't agree?"

janine @talking2mouth "It's not about agreeing or disagreeing. Different moves serve different battle strategies more or less effectively."

janine @smirkmouth "I look forward to seeing how all of you develop your battle strategies."

janine @talking2mouth "Anyway, for this lesson, Lance and I are going to teach your Pokémon how to remember moves they've forgotten."

show janine surprisedbrow with dis
show lance closedbrow with dis
show stadium_empty with vpunch

ethan @surprised "Woah! For real?"

show janine -surprisedbrow with dis
show lance -closedbrow with dis

show lance:
    ease 2.0 xpos 0.125

lance @talking2mouth "It is a valuable skill. If you are not powerful enough to overcome a foe with raw strength, you may consider altering your strategy to best them."

show lance:
    ease 2.0 xpos 0.5 ypos 1.2 zoom 1.3

lance @angrybrow talking2mouth "You may also consider dropping moves from your repertoire that are useless, or provide nothing but a burden."

show lance with dis:
    ease 2.0 ypos 1.0 zoom 1.0 xpos 0.875

lance @talking2mouth "Finally, you might elect to learn moves that are able to hit a foe's weakness, whether it be their types, or the flaws in their strategies."

show lance:
    ease 2.0 xpos 0.5

lance @closedbrow talking2mouth "There is no set of Pokémon moves that can beat every other Pokémon. It follows that there is no team that can beat every other team."

lance @angry "In lieu of perfection, the only guarantee is {i}strength{/i}."

pause 1.0

lance @sadbrow talking2mouth "You'd do well to remember this."

janine @talking2mouth "Lance and I will be providing this service every Friday, during our Battle Team meetings."

janine @closedbrow talkingmouth "We have a limited amount of time, though. Even though there's only about a dozen of you, this year, we don't have time to go over {i}every{/i} Pokémon you have on hand. We'll teach one move, and that's it."

janine @closedbrow talkingmouth "Maybe, later on in the year, if some of you start dropping due to the Quarter Qlashes, we'll be able to focus more attention on those who are left. So we could teach more moves at one club meeting."

lance @closedbrow talking2mouth "Do not count on that. It is the Battle Team's aim to get everyone through the fourth Quarter Qlash, and into the national tournament."

pause 1.0

lance @angrybrow talking2mouth "{i}Almost{/i} everyone."

pause 1.0

redmind @confusedeyebrows frownmouth "Can the man {i}give me a break?{/i}"

silver @talkingmouth "...This'll be something you do for us every Friday, then?"

janine @talking2mouth "Every meeting, yeah. We might hold meetings on non-Fridays, if we're in a rush. Like last Monday."

lance @sadbrow talking2mouth "My apologies for my absence then. I had an engagement with the Dean.{w=0.5} And his daughter."

erika @talkingmouth "Am I to understand, then, that the Battle Team's training will consist of either move tutelage or experience training?"

janine @smirkmouth "This isn't the hobbyist battlers' club, Erika. We're doing both. And next week, I'll probably introduce something else, that we'll do every week after, too."

erika @surprised "Oh my."

janine @talking2mouth "I'll take the trainers on the right side of the arena. Lance?"

lance @closedbrow talking2mouth "I will take the left."

pause 1.0 

red @surprised "Wait, I'm on the left!"

pause 0.5

lance @sadbrow talking2mouth "How wonderful. You are capable of recognizing obvious truths before your nose. I had started to think otherwise."

redmind @closedbrow sweat frownmouth "Oops. I said that out loud, didn't I?"

pause 0.5

janine @talking2mouth "While you're waiting for us to get around to you, start training."

hide janine
hide lance
with dis

pause 1.0

narrator "Lance and Janine split up and begin tutoring the other Battle Team members' Pokémon."

narrator "You look around for someone to train with, and..."

$ seenblue = False

label trainwith430:

menu:
    ">Train with [blue_name]" if (not seenblue):
        if (GetRelationship("Blue") == "Rival"):
            show blue with dis

            red @happy "Hey, [blue_name]! You want to train?"

            blue @angry "Seriously? You're going to call me [blue_name], then ask for a favor? Bug off."

            red @confused "Uh, it's not a favor. We'd both get stronger."

            blue @happy "Hah! Believe me. When you're at {i}my{/i} level, teaching someone like you {i}is{/i} a favor."

            red @angrybrow happymouth "That's a lot of talk. How about you back it up?"

            $ ValueChange("Blue", -1, 0.5)

            blue @angry "Don't jerk me around, [first_name]. You know I've got the skills to back up my words."

            hide blue with dis

            $ seenblue = True

            jump trainwith430

        else:
            show blue with dis

            red @happy "Hey, [blue_name]! You want to train?"

            blue @closedbrow talkingmouth "Psh. You'll just slow me down, but I'm feeling generous."

            $ ValueChange("Blue", 3, 0.5)

            blue @angrybrow happymouth "Pay attention, and you might just learn something."

    ">Train with Leaf":
        show leaf with dis

        $ ValueChange("Leaf", 3, 0.5)

        if (HasEvent("Leaf", "RejectedConfession")):
            leaf @sadbrow happymouth "Sure.{w=0.5} Thanks, [first_name].{w=0.5} Glad things aren't awkward between us."

        else:
            leaf @happy "Sure!"

    ">Train with Ethan":
        show ethan with dis

        $ ValueChange("Ethan", 3, 0.5)

        ethan @talkingmouth "Sure thing, man. Since we've got such similar teams, we should be pretty good at helping each other train."

        red @happymouth "Yeah, that's what I was thinking."
    
    ">Train with Dawn":
        show dawn with dis

        $ ValueChange("Dawn", 3, 0.5)

        dawn @surprisedbrow talkingmouth "O-oh! You want to train with me?"
        dawn @sadbrow talkingmouth "I'm... I'm not sure about that... I don't think there's anything I can help you with, really..."

        red @confused "You have a Mega Altaria! That's pretty interesting to me. I'd love to see it."

        dawn @happy "Oh, well, I would, but, you know, she's really shy."

        pause 1.0

        red @confused "Really?"

        dawn @closedbrow talkingmouth "{size=30}No, just me...{/size}"

    ">Train with Bea":
        show bea with dis

        $ ValueChange("Bea", 3, 0.5)

        bea @closedbrow talking2mouth "Very well. Let us commence."

        show stadium_empty:
            xalign 0.5 yalign 0.5
            ease 2.0 zoom 1.2

        show bea:
            ease 2.0 ypos 1.2 zoom 1.3

        bea @closedbrow talking2mouth "Now..."

        bea angry "Begin!"

        show bea:
            ease 0.3 ypos 2.0 zoom 3.0 alpha 0.0

    ">Train with Erika":
        show erika with dis

        $ ValueChange("Erika", 3, 0.5)

        erika @closedbrow happymouth "Oh, you wish to train with me? I'm honored."

        red @happy "Hey, I wanted to thank you for buying those Experience Shares for the team."

        erika @talkingmouth "It was just pocket change. If I'm to get my position on this team for primarily monetary reasons, I'm going to use that money to help everyone else out."

    ">Train with Sonia":
        show sonia with dis

        $ ValueChange("Sonia", 3, 0.5)

        sonia @talking2mouth "Right-o. I remember a few techniques Janine taught us at the end of last year. If you wouldn't overly mind skipping ahead a bit...?"

        red @happy "Lay it on me."

    ">Train with Silver":
        show silver with dis

        $ ValueChange("Silver", 3, 0.5)

        silver @surprisedbrow talking2mouth "Huh? What brought this up?"

        if (GetRelationship("Silver") == "Friend"):
            red @happy "Do I need a reason to hang out with you? You're my friend."

            silver @happymouth "Psh. Nothing gets you down, huh?"

            red @talkingmouth "Besides, if you're training a full team of someone else's Pokémon, you must be a pretty good trainer."

        else:
            red @happy "You're training a full team of someone else's Pokémon. You must be a pretty good trainer."

        pause 1.0

        silver @happymouth "Let's see."

    ">Train with Hilbert":
        show hilbert with dis

        $ ValueChange("Hilbert", 3, 0.5)

        hilbert @closedbrow talking2mouth "Fine. Just don't slow me down."

scene black with dis

narrator "You train while waiting for Lance to make room for you. You notice he goes out of his way to teach the rest of the Battle Team members first."

$ BattleTeamTraining()

scene stadium_empty
show lance 
with dis

pause 1.0

lance @talking2mouth "It appears that you are the last person I need to teach these valuable skills to."

pause 1.0

red @talkingmouth "Yeah."

lance @closedbrow talking2mouth "And the Battle Team meeting is still ongoing."

pause 1.0

red @confused "Yeah."

pause 0.5

lance @angrybrow talking2mouth "Tch."

lance @talking2mouth "Fine, then. Pick a Pokémon that could stand to learn a new move. Once you've selected a Pokémon, I'll tell you what it's capable of relearning."

red @closedbrow talking2mouth "How gracious."

label movetutor430:

call screen SelectMon

if (_return == 'back'):
    lance @angry "You reject my generosity?"

    menu:
        "I don't want to teach any of my Pokémon one of their old moves.":
            lance @closedbrow talking2mouth "Foolishness."

        "On second thought...":
            jump movetutor430

else:
    $ tutormon = _return
    $ tutormonname = pokedexlookup(tutormon.GetId(), DexMacros.Name)

    lance @talking2mouth "Oh, you want me to teach your [tutormonname]?"
    lance @sadbrow talking2mouth "Why am I not surprised?"
    
    $ rememberablemoves = GetRememberableMoves(tutormon)

    if (len(rememberablemoves) == 0):
        lance @talking2mouth "This Pokémon has no moves it can remember. Avoid wasting my time, if you are capable of such a thing."

        jump movetutor430

    else:        
        lance @talking2mouth "Fine. What do you want me to re-teach this Pokémon?"

        $ learnmove = renpy.call_screen("rememberablemoves", tutormon)

        if (learnmove == "Back"):
            lance @talking2mouth "You have a scant few days before the first Quarter Qlash, where you will doubtlessly be the first Kobukan Battle Team member to ever be eliminated."
            lance @sadbrow talking2mouth "I wouldn't waste these precious moments with indecision."

            jump movetutor430

        else:
            $ tutormon.LearnNewMove([(0, learnmove)])

            if (learnmove not in tutormon.GetMoveNames()):
                jump movetutor430

lance @sadbrow talking2mouth "Well, this has been a dreadful experience for everyone. I hope you and your team learned something valuable today. Such as, perhaps, the fights you cannot win."

show lance:
    ease 0.5 xpos 0.25

show janine with dis:
    xpos 0.75

janine @angrybrow talking2mouth "Lance."

lance @closedbrow talking2mouth "I think it's about time we wrap this meeting up, don't you? You know where to find me."

hide lance with dis

pause 1.0

janine @talking2mouth "Yeah, he's right. Everyone head home. Go {i}straight{/i} to your dorms. If you abuse our nighttime exception, the school might revoke our privileges."

pause 0.5

janine @talking2mouth "...Except you. Leaf, you stay."

show leaf at leftside with dis

leaf frownmouth @surprised "Huh?"

janine @closedbrow talking2mouth "You heard me, and I don't like repeating myself. I just want a quick chat. Everyone else can go."

red @confused "Um... stay safe?"

show leaf:
    ease 0.5 xpos 0.25 ypos 1.2 zoom 1.3

leaf @sadbrow happymouth "{size=30}Yeah, uh, this is kinda scary... but sure, I'll try!{/size}"

scene black with splitfade

narrator "You leave the Battle Hall and head back to your dorm."

call texting from _call_texting_11

jump day010501