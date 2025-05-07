label gym010416:

  

$ HealParty()

play music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

$ renpy.transition(dissolve)
show screen currentdate

scene gym with dis

show blank2 behind gym

$ renpy.pause(2.0, hard=True)

hide blank2

show alder spunky2 with dis:
    xpos 0.66

show bruno think with dis:
    xpos 0.33

alder @talkingmouth "And that's the end of the lecture! We'll be moving onto the double battle unit shortly, so you can expect next week's battles to have a lot more variety."
alder norm @spunky2 "For today, though, it'll be a standard single battle."

pause 1.0

alder @norm2 "Bruno?"

bruno @norm2 "[first_name], you will be battling Calem."

red uniform @happy "Oh, awesome!"

hide bruno
hide alder
show calem uniform
with dis

calem @happy "Excellent to see you. I wondered when I would face you in this class."

red @happy "Yeah, surprised it took this long! I battled Cheren twice, first."

calem @talkingmouth "Well, let's get right into it. No further preamble is necessary."

red @happy "Aw, but what if I like preamble?"

calem @happy "Well, you'll simply have to make do without."

$ trainer1 = Trainer("red", TrainerType.Player, playerparty)
$ trainer2 = MakeTrainer("Calem")

call Battle([trainer1, trainer2], uniforms=[True, True]) from _call_Battle_20
$ battlehistory["Calem1"]  = _return

$ HealParty()

stop music fadeout 1.0

hide alder
hide bruno

pause 1.0

show alder surprisedbrow frownmouth at centerside 
show bruno think at leftside
show calem uniform at rightside
with dis

$ renpy.music.queue("Audio/Music/Gym_Loop.ogg", channel='music', loop=True, fadein=1.25, tight=None)
    
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

hide blank2

if (WonBattle("Calem1")):
    calem @happy "Haha! Perhaps I should have expected this. You're really a natural."

    $ ValueChange("Calem", 3, 0.75)

    redmind uniform @happy "Oh, if only you knew..."

    $ sidemonnum = 669

    $ PlaySound("pokemon/cries/669.mp3")

    sidemon "Fla! Flabébé!"

    calem @surprised "N-no, I know, I'm sorry!" 

    $ PlaySound("pokemon/cries/669.mp3")

    sidemon "Flabéééééééébé!"

    calem @sad "Please don't chastise me, I tried..."

else:
    calem @closedbrow talking2mouth "Well, that was a fun battle. Well done."

    $ firstpokemon = playerparty[0].GetNickname()

    red uniform @closedbrow talking2mouth "Oh. Sorry, [firstpokemon]."

    $ sidemonnum = 669

    $ PlaySound("pokemon/cries/669.mp3")

    sidemon "Fla! Flabébé!"

    narrator "Calem's Flabébé is laughing at you brattily."

    calem @surprised "Now, Flabébé! Don't be so crass. They were worthy opponents." 

    $ PlaySound("pokemon/cries/669.mp3")

    sidemon "Flabéééééééébé!"

    calem @sad "Er... you really shouldn't... that is, to say..."

red @surprised "Uh... Calem, I think you need to set boundaries."

calem @closedbrow talking2mouth "Such a thing is {i}much{/i} easier said than done. I promise you, regardless of your natural affinity for Pokémon, you've never had one quite as willful as her."


jump lunchtransition