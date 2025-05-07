label gym010421:

  

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

alder @talkingmouth "...And that's why it's important to memorize your type matchups! At the very least, memorize what the Rock-type is super effective against."
alder @norm4 "It'll seriously help you avoid Stealth Rocks. Or at least mitigate its effects. As someone who relies heavily on my partner Volcarona, I know more than anyone how much of a threat those rocks pose."
alder @talkingmouth "Anyway, that's the end of this lecture. Just remember to pack a Rapid Spinner!"
alder @norm4 "I'd also advise you look into Defog."
alder @norm2 "There's also a couple more options, like Tidy Up and Mortal Spin, but--"

show alder surprisedbrow frownmouth with dis

bruno @norm2 "Alder."

pause 1.0

alder -surprisedbrow -frownmouth -surprised @happy2 "Ah, there I go again. I guess I tend to overstate how much Stealth Rocks matter."

pause 1.0

alder @angry2 "It's a lot."

pause 1.0

bruno @norm2 "Enough. [first_name], your partner for this class will be... Bianca."

hide alder
hide bruno 
with dis

show bianca uniform at leftside
show tia uniform hat at rightside
with dis

pause 1.0

red uniform @confused "...Wait, which one?"

show tia happy with dis

bianca @happy "I dunno! Guess you're fighting both of us!"

show tia -happy with dis

red @happy "Well, alright. Not sure this is totally fair, but I'll take you both on."

pause 1.0

if (GetRelationshipRank("Tia") != 1):
    red @confused "Hey, shorter Bianca, you're not going to, like, punch [starter_name] in the face, are you? You {i}do{/i} have Pokémon, right?"
else:
    red @confused "Hey, shorter Bianca, you're not going to, like, punch [starter_name] in the face, are you? I know your Pokémon can dance, but can they battle?"

show tia surprisedbrow frownmouth with dis

pause 1.0

show tia angrybrow poutmouth with dis

pause 1.0

red @happy "Alright, just making sure."

bianca @talkingmouth "That's a good thing to make sure of, yup."

red @angrybrow happymouth "Let's do this, then!"

python:
    playerlevel = max(8, GetHighestLevel() - 3)
    trainer1 = MakeRed(2)
    trainer2 = MakeTrainer("Tia")
    trainer3 = Trainer("bianca", TrainerType.Enemy, [
        Pokemon(pokedexlookupname("Munna", DexMacros.Id), moves=[GetMove("Psywave"), GetMove("Defense Curl"), GetMove("Lucky Chant"), GetMove("Yawn")], level=playerlevel + 1, nickname="Moony", gender=Genders.Female, ability="Synchronize"),
        Pokemon(pokedexlookupname("Minccino", DexMacros.Id), moves=[GetMove("Pound"), GetMove("Tickle"), GetMove("Baby-Doll Eyes"), GetMove("Helping Hand")], level=playerlevel, nickname="Minnie", gender=Genders.Female, ability="Skill Link")
    ])

call Battle([trainer1, trainer2, trainer3], uniforms=[True, True, True]) from _call_Battle_48
$ battlehistory["BiancaTia1"]  = _return

$ HealParty()

stop music fadeout 1.0

hide alder
hide bruno

pause 1.0

show alder norm at centerside 
show bruno think at leftside
show tia uniform hat:
    xpos 0.7
show bianca uniform behind tia:
    xpos 0.8
with dis

$ renpy.music.queue("Audio/Music/Gym_Loop.ogg", channel='music', loop=True, fadein=1.25, tight=None)
    
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

hide blank2

if (WonBattle("BiancaTia1")):
    bianca @surprised "Aw! I thought we were going to win that one. Oh, well!"

    $ ValueChange("Tia", 3, 0.7, False)
    $ ValueChange("Bianca", 3, 0.8)

else:
    bianca @happy "Yesss! I knew all my studying would pay off. Good job, other Bianca!"

alder @spunky2 "You know, normally, you should ask Bruno or I who you're meant to battle, if there's some confusion there."

alder @norm2 "But it looks like everything worked out well enough this time. So you're both named Bianca, huh?"

show tia happy with dis

narrator "Tia begins signing at Alder before suddenly pausing, as though she realized something. She looks at you, sheepishly, and nods towards Alder."

show tia lightblush sadbrow -happy with dis

pause 1.0

redmind @thinking "Huh. She's figured out she can't just sign at anyone and expect to be understood. That's new."

red @happy "Yes, Sir. They're both named Bianca. Um, the shorter Bianca doesn't speak, though."

alder @surprised2 "Oh? And yet you communicated pretty well with your Pokémon in that battle just now. Was that all just based on your hand-signs?"

alder @spunky2 "Amazing the techniques and tricks the young ones come up with. I wouldn't have dreamed of half the stuff your generation treats as normal."

bruno @happy2 "Perhaps that's why you were unseated by a toddler."

alder @sad2 "...She was {i}twelve{/i}, Bruno."

bianca @surprised "Oh! That reminds me. Cheren wanted to talk to you after school, [first_name]!"

red @talking2mouth "Oh? Yeah... I wanted to talk to him, too. Anywhere in particular?"

redmind @thinking "Maybe next to a lake, where he could fit me with a nice pair of concrete shoes...?"

bianca @talkingmouth "Just in the garden, he said!"

red @talkingmouth "Right. Thanks for letting me know."

jump lunchtransition