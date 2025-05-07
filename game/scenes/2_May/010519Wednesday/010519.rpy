label day010519:

stop music fadeout 1.5

call calendar(1) from _call_calendar_44
$ calDate = calDate.replace(day=19, month=5, year=2004)

$ timeOfDay = "Morning"

scene homeroom
show screen currentdate
show kris sadbrow angrymouth
with splitfade

stop music fadeout 1.5
queue music "audio/music/celebi_start.ogg" noloop
queue music "audio/music/celebi_loop.ogg"

kris @talking2mouth "...Good morning, students."

leaf uniform @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

show whitney uniform sadbrow frownmouth:
    xpos 0.25
show hilbert uniform sad:
    xpos 0.75
with dis

Character("{color=#e47282}Whitney{/color} & {color=#353535}Hilbert{/color}") "\"{w=0.5}.{w=0.5}.{w=0.5}.\""

redmind uniform @closedbrow frownmouth "The mood of the classroom feels... subdued. I guess the news spread quickly."

hide whitney
hide hilbert
with dis

kris @talkingmouth "Regardless of what else is happening, we need to work hard to prepare you for tomorrow's test."
kris -sadbrow -angrymouth @talkingmouth "We were talking about critical hits, yes? Does anyone remember what the reading said?"

pause 1.0

kris @talkingmouth "Hm... [first_name], could you summarize? Your own words, please."

menu:
    "{color=#60c2f8}[[Wit]{/color} Critical hits are a way to punch through defense buffs.":
        $ TraitChange("Wit")

        kris @happy "Good. Brief answer, but correct."
        kris @talkingmouth "As [first_name] said, class--if your opponent has boosted defense or special defense stats, a critical hit will just ignore that, allowing you to hit for full damage."

    "{color=#ff8412}[[Courage]{/color} Critical hits are a way to ignore attack debuffs.":
        $ TraitChange("Courage")

        kris @happy "Good. Brief answer, but correct."
        kris @talkingmouth "As [first_name] said, class--if you have decreased attack or special attack, a critical hit will just ignore that, allowing you to hit for full damage."

kris @talkingmouth "{w=0.5}.{w=0.5}.{w=0.5}.Although that's not actually quite right, is it, [first_name]?"

redmind @surprisedbrow frownmouth "Um."

kris @talkingmouth "I said something a little bit wrong there. Do you know what it was?"

menu:
    "You don't hit for full damage.":
        $ ValueChange("Professor Cherry", 1)

        kris @happy "That's right! You hit for {i}more{/i} than full. 150%% of the damage, to be exact."
        
    "Critical hits don't ignore stat changes.":
        kris @sadbrow talkingmouth "Oh, I'm sorry, I must've confused you with this follow-up question."
        kris @talkingmouth "You were right the first time. Critical hits {i}do{/i} ignore stat changes."
        kris @talkingmouth "In actuality, the wrong thing I said was that you {i}don't{/i} hit for full damage, you hit for {i}more{/i} than full. 150%% of the damage, to be exact."

    "You need to roll a crit confirm before you hit for full damage.":
        kris @happy "Oh, you really {i}are{/i} Ethan's dormmate, aren't you?"
        kris @talkingmouth "I'm afraid that's not it, though."
        kris @talkingmouth "In actuality, the wrong thing I said was that you {i}don't{/i} hit for full damage, you hit for {i}more{/i} than full. 150%% of the damage, to be exact."

kris @talkingmouth "Of course, that's not counting standard damage variation, but let's assume a spherical cow, for now."

show whitney uniform surprised with dis:
    xpos 0.25

whitney @talking2mouth "Huh? A spherical cow?"

show hilbert uniform with dis:
    xpos 0.75

hilbert @talkingmouth "A 'spherical cow' is a joke concept referencing physicists' and mathematicians' tendencies to simplify complex problems down to an easily-parsable and understandable model..."
hilbert @sadbrow talkingmouth "Even if that model is simplified to the point it has no bearing on reality."

if (GetRelationshipRank("Hilbert") > 0):
    redmind @sadbrow frownmouth "You'd know about that, wouldn't you...?"

whitney -surprisedbrow -frownmouth -surprised @talkingmouth "Oh."

pause 1.0

whitney @talking2mouth "So we're not--"

hilbert @closedbrow talkingmouth "We're not going to take an angle grinder to your Miltank, no."

whitney @sweat closedbrow talking2mouth "{i}Phew.{/i}"

jump homeroom1transition