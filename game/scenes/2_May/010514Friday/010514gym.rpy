label gym010514:

$ HealParty()

play music "Audio/Music/Gym_Start.ogg" noloop
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

alder @talkingmouth "...and that's the end of the lecture!"
alder @happy2 "Personally, I think the practical experience of a battle's worth a half-dozen lectures, but we have to get through them. You know how it is."

bruno @norm2 "Hm. Battle training only reinforces what the lecture imparts. If there was one aspect to forgo, it would be battles."

alder @winkbrow talkingmouth "Bruno, once again proving that trainers don't need to see eye-to-eye on everything to get along. Hah hah!"

pause 1.0

alder @happy2 "But on a serious note, Bruno, I've heard your lectures, and they're drier than a Krookodile's backside."

bruno @happy2 "I was not aware one's ability to moisten one's speech made one any more efficacious as an instructor."

alder @talking2mouth "You'd be surprised. Anyway, let's move onto the battles."

hide alder with dis

pause 1.0

bruno @norm2 "[first_name]. It is time for your rematch with Whitney."

show bruno:
    xpos 450
    ease 0.5 xpos 200

show whitney uniform with dis:
    xpos 0.66

bruno @norm4 "I trust this will be a more honorable battle than last time?"

whitney @closedbrow lightblush happymouth "Ahehehe...{w=0.5} Yes, instructor."

bruno @happy2 "Good."

hide bruno with dis

pause 0.5

show whitney:
    ease 0.5 xpos 0.5

if (DungeonEntries("Shattered Glades") == 0):
    whitney @angrybrow talking2mouth "[first_name]! Why haven't you called together the Tia rescue team?!"

    red uniform @sadbrow talkingmouth "It's on my mind, promise. I'm just a bit busy, you know?"

    whitney @sadbrow talkingmouth "Okay... but I'm getting real worried. It's getting late, you know?"

    red @talkingmouth "It'll be alright. Tia's strong. And, you know, she has some particular advantages out there."

    whitney @closedbrow talking2mouth "I... guess that's right..."

    red @happy "Don't worry about it. Let's just battle."

elif (not rescuedtia):
    whitney @angrybrow talking2mouth "[first_name]! Why haven't we rescued Tia?!"

    red uniform @sadbrow talkingmouth "Hey, we tried! And we got our butts kicked. We'll try again, promise. I'm just a bit busy, you know?"

    whitney @sadbrow talkingmouth "Okay... but I'm getting real worried. It's getting late, you know?"

    red @talkingmouth "It'll be alright. Tia's strong. And, you know, she has some particular advantages out there."

    whitney @closedbrow talking2mouth "I... guess that's right..."

    red @happy "Don't worry about it. Let's just battle."

else:
    whitney @angrybrow happymouth "[first_name]! Just because you helped me find Tia, don't think that I'm going to go easy on you!"

    red uniform @happy "Wouldn't dream of it."

whitney @angrybrow happymouth "I'm going all-out this time! No sandbagging, no tricks, just me and 160 pounds of cow on your face!"

menu:
    "You're going to sit on me?":
        show whitney surprisedbrow frownmouth with dis

        pause 1.5

        $ ValueChange("Whitney", -3, 0.5)

        whitney @angry "You jerk! Milty, make him pay for that!"

    "Sounds like it's time to make burgers!":
        whitney @angrybrow happymouth "By the time I'm finished with you, you'll be a vegetarian!"

    "[bluecolor][[Whitney Rank 1]{/color} Let's see you try to hit a home run!" if (GetRelationshipRank("Whitney") > 0):
        $ ValueChange("Whitney", 1, 0.5)

        whitney @happy "Hah! You should know that's my specialty!"

python:
    trainer1 = MakeRed(3)
    trainer2 = Trainer("whitney", TrainerType.Enemy, GetTrainerTeam("Whitney"), number=3)

call Battle([trainer1, trainer2], uniforms=[True, True]) from _call_Battle_133
$ battlehistory["Whitney2"] = _return

play music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

if (WonBattle("Whitney2")):
    show whitney uniform sadbrow frownmouth with dis

    whitney @sadmouth tears "I... I lost...?"

    pause 1.0

    if (GetRelationshipRank("Whitney") > 0):
        show gym with vpunch

        whitney @angry "Aaaargh! That {i}stinks.{/i}"

        whitney @closedeyes angryeyebrows talking2mouth "Everyone tried really hard, this time... but we still...?"

        whitney @closedbrow talking2mouth "I guess since it's you, I don't feel so bad about it, but... bleh."

    else:
        whitney @closedeyes sadeyebrows poutmouth tears "I'm not going to cry. I'm {i}not{/i} going to cry..."

    $ ValueChange("Whitney", 3, 0.5)

    whitney @sadbrow talking2mouth "Well fought. Or... whatever I should say..."

    redmind @sadbrow frownmouth "Well... she's not the most gracious loser."

    if (WonBattle("Whitney1")):
        redmind @happy "Still, she's a lot better than she was last time."

    else:
        redmind @happy "Of course, she wasn't the most gracious {i}winner{/i}, either."

else:
    show whitney uniform with dis

    whitney @happy "Hah hah! I won! Yes!"

    pause 1.0

    whitney @surprised "Oh!"

    whitney @playfuleyes playfulmouth "Well fought, challenger.~"

    redmind @playfuleyes confusedeyebrows frownmouth "...I'd expect this level of smugness from Leaf, not from you."

hide whitney with dis

pause 1.0

show alder:
    xpos 0.66

show bruno:
    xpos 450
with dis

jump lunchtransition