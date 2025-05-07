label gym010517:

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

alder @happy2 "Good morning, everyone! Great to see you in class again."

bruno @norm2 "It is a pleasure."

alder @talkingmouth "We've been through single, double, and triple battles this semester, so let's start working on team-based battles. We'll assign you a partner, and you'll battle two other trainers."
alder @happy2 "How does that sound?"

sonia uniform @talking2mouth "It's all random, then?"

alder @happy2 "Not quite. We try to match up pairs based on skill level, as well as fights we think might be interesting to watch."

nate uniform @happy "I'm game! Let's see how we end up being paired!"

may uniform @happy "Oh, wow, we're getting paired up randomly? That's so fun!"

brendan uniform @talking2mouth "Wouldn't it be crazy if we ended up getting paired up together, anyway?"

may @talkingmouth "You're right! It totally would be! I'll cross my fingers, though!"

redmind uniform "Hm... I wonder who I'll get paired up with?"

bruno norm @norm2 "[first_name], you will be battling alongside Bianca."
bruno @surprised2 "Uh, the one in the green hat."

hide alder 
show bianca uniform:
    xpos 0.66
    block:
        ease 0.4 ypos 1.1
        ease 0.4 ypos 1.0
        repeat
with dis

bianca @happy "Hi-i-i-i, red hat!~"

red @happy "That's a flashback to simpler times. Hey, Bianca. Good to see you. Looking forward to battling alongside you!"

show bianca:
    xpos 0.66
    block:
        ease 0.3 ypos 1.1
        ease 0.3 ypos 1.0
        repeat

bianca @talkingmouth "Same! It's super-super-super-cool that I get to battle alongside a member of the {i}actual{/i} battle team!"

red @talkingmouth "I think it's pretty cool that I get to battle alongside {i}you.{/i} What you said during the Quarter Qlashes was pretty brave."

show bianca:
    xpos 0.66
    block:
        ease 0.2 ypos 1.1
        ease 0.2 ypos 1.0
        repeat

bianca @happy "Aw, thanks! I just wanted my old man to know how much better I'm doing without him in my life, and I hope the regret wells up inside him and chokes him like a snake until he's begging me to come back home and get his life in order again!"

pause 2.0

show bianca:
    xpos 0.66
    ease 0.5 ypos 1.0

bianca @happy "Oopsie! There I go, oversharing again!"
bianca @sadbrow talkingmouth "Sorrrry. I hope you won't hold it against me?"

pause 1.0

red @sweat closedbrow "N-no, of course not."

pause 1.0

redmind @thinking "This girl's... kinda scary."

bruno @norm2 "You two will be battling Gardenia and Brendan."

hide bruno with dis

show bianca:
    ease 0.5 xpos 0.25

show brendan uniform:
    xpos 0.75

show gardenia uniform:
    xpos 0.5

brendan @closedbrow talking2mouth "{i}Yawn.{/i}{w=0.5} Hey, man."

if (investment > 0):
    gardenia @talkingmouth "Partner! You're looking good today. Got a nice, healthy glow to your cheeks."

else:
    gardenia @talkingmouth "Hey there, Bianca! You're looking good today. Got a nice, healthy glow to your cheeks."

red @talkingmouth "Hi, you two. Don't think I've battled you guys in Gym Class before, have I?"

brendan @talking2mouth "Nah. {w=0.5}{i}Yawn.{/i}"

red @confused "'Sup with the yawning? Late nights?"

brendan @talking2mouth "Little bit, yeah. Lisia's having us work harder than ever before. It's kinda crazy."

gardenia @surprised "Ooh, yeah, didn't Calem convince her to stay here and advise the coordinator club? Do you know how much she's being paid?"

brendan @talking2mouth "Nah. Must be a nice amount, though. She's really going all-in on us."

brendan @sadbrow happymouth "Which is a good thing. It's just, uh... exhausting."

red @happy "Well, maybe we can wake you up with a nice battle."

gardenia @talkingmouth "I think you'll find I'm an absolutely {i}excellent{/i} battle partner, Brendan. I know you're pretty much only used to battling with May, but my Grass-types are something else."

brendan @happy "Hey, I just want us all to have fun."

gardenia @angrybrow happymouth "Oh? Well, if we want to have some {i}real{/i} fun, why don't we put a little wager on--"

show gardenia surprisedbrow frownmouth with dis

bianca @animepleasedeyes tonguemouth "Nope!~ Not in gym class. We'd get in trooooouble!~"

gardenia @surprised "Oh, fair enough." 
gardenia @angrybrow happymouth "Just a regular battle, then... with nothing on the line but our honor!"

red @angrybrow happymouth "And that's something you {i}can't{/i} buy!"

python:
    trainer1 = MakeRed()
    trainer2 = MakeTrainer("Bianca", TrainerType.Ally)
    trainer3 = MakeTrainer("Brendan")
    trainer4 = MakeTrainer("Gardenia")

call Battle([trainer1, trainer2, trainer3, trainer4], uniforms=[True, True, True, True]) from _call_Battle_143
$ battlehistory["BrendanGardenia1"] = _return

stop music fadeout 1.5
queue music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

show gardenia uniform:
    xpos 0.5
show brendan uniform:
    xpos 0.75
show bianca uniform:
    xpos 0.25
with dis

if (WonBattle("BrendanGardenia1")):
    $ ValueChange("Brendan", 1, 0.75, False)
    $ ValueChange("Bianca", 1, 0.25, False)
    $ ValueChange("Gardenia", 1, 0.5)

    gardenia @surprised "Oof! Guess it's a good thing we didn't put any money on the table, after all!"

    brendan @talking2mouth "Man... I'm more of a coordinator, but I thought I'd gotten a little bit better at battles."
    brendan @happy "Ah, but I can't be mad, man. You did seriously well, both of you."

    bianca @happy "Yay! You're a {i}great{/i} partner, [first_name]!"

    red uniform @happy "Hey, you were pretty good yourself!"

else:
    show bianca sadbrow frownmouth with dis

    brendan @happy "Hah! Good job, Gardenia!"

    show gardenia:
        ease 0.5 xzoom -1
    
    gardenia @talkingmouth "You didn't do bad yourself! I thought you were just a coordinator, but you can put up a pretty good face in battles too, huh?"

    brendan @talking2mouth "Well, a Pokémon that's good at battling has better control over their moves, for stunts 'n stuff."
    brendan @talking2mouth "Oh, but hey, you two did good, too!"

    bianca @talking2mouth "I'm sorry... I kinda feel like I let you down..."

    red uniform @sweat talkingmouth "Ah, it's alright. I know you did your best. And I didn't battle perfectly, either."

    bianca @sadeyes talking2mouth "Still, sorry..."

    red @sadbrow talkingmouth "H-hey, really, it's alright. Don't beat yourself up over it."

    pause 0.5

    redmind @sadbrow frownmouth "She's really taking this hard. Guess she's used to being able to help people..."

brendan @talking2mouth "Hey, Gardenia--that Grotle of yours was pretty tough. Do you guys have a history, or anything?"

gardenia @talkingmouth "Not really. Why, looking for a trade?"

brendan @closedbrow talking2mouth "I {i}was{/i} thinkin' about it..."
brendan sweat happy "But I'm pretty sure I couldn't afford your prices!"

hide brendan
hide gardenia
hide bianca
with dis

pause 1.0

show alder:
    xpos 0.66
show bruno think:
    xpos 0.33
with dis

jump lunchtransition