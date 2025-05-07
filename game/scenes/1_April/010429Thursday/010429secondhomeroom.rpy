label secondhomeroom010429:

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=True, fadein=1.0, tight=None)

scene blank2

show oakbg behind blank2
show homeroom behind oakbg

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with dis

oak @talkingmouth "Good afternoon, students! Who's ready for today's quiz?"

$ PlaySound("class_groan.ogg", "crowd2")

pause 0.5

oak @talkingmouth "Well, there's no use complaining to me about it. Success in these classes is the surest way to graduating with honors."
oak @talkingmouth "Besides, do well enough in them, and the school may provide some tuition waivers. Which I'm sure {i}all{/i} of you would appreciate, regardless of your financial situation."
oak @talkingmouth "Remember, correct usage of items will be key to handling this test properly. I'll go ahead and tell you that {color=#0048ff}your opponent is not holding an item, and only knows Crunch.{/color}"
oak @talkingmouth "I cannot express, enough, the importance of looking over your team {i}very{/i} carefully before committing to any moves."
oak @talkingmouth "[bluecolor]Remember, you can see summaries of your party at any time by 'clicking' on the 'Pokémon' option in battle.{/color}"

pause 0.5

oak @talkingmouth "...Well, that's a metaphor, but you understand what I mean."

oak @talkingmouth "Remember, {color=#0048ff}this is graded!{/color}"

python:
    trainer1 = Trainer("red", TrainerType.Player, [
        Pokemon("Sneasel", level=20, moves=[GetMove("Taunt"), GetMove("Switcheroo"), GetMove("Leer"), GetMove("Protect")], ivs=[0, 0, 0, 0, 0, 0], item="Sticky Barb", ability="Pickpocket"),
        Pokemon("Togetic", level=20, moves=[GetMove("Growl"), GetMove("Yawn"), GetMove("Charm"), GetMove("Follow Me")], ivs=[0, 0, 0, 0, 0, 0], item="Pecha Berry", ability="Serene Grace")
    ], number=2)
    trainer2 = Trainer("oak", TrainerType.Enemy, [
        Pokemon("Sharpedo", level=30, moves=[GetMove("Crunch")], ability="Rough Skin", ivs=[0, 0, 0, 0, 0, 0])
    ])

    trainer1.GetTeam()[0].Health = 1
    trainer1.GetTeam()[1].Health = 1
    trainer1.GetTeam()[0].ApplyStatus("poisoned")
    trainer1.GetTeam()[1].ApplyStatus("burned")

    trainer2.GetTeam()[0].Health = 1
    trainer2.GetTeam()[0].ChangeStats(Stats.Speed, -6)


call Battle([trainer1, trainer2], clearstats=False, gainexp=False, healParty=False, uniforms=[True, False], lockbag=True) from _call_Battle_68
$ battlehistory["Oak7"] = _return

$ renpy.transition(dissolve)
show screen currentdate

if (WonBattle("Oak7")):
    red uniform @confused "Man. I'm pretty sure I figured that one out, but these tests are ramping up in difficulty quickly."

else:
    red uniform @closedbrow frownmouth "...That was bullshit. Just four weeks ago I was using Dragon Rage with a Deino. Could someone stop the school year, please? I'd like to get off."

oak @talkingmouth ".{w=0.5}.{w=0.5}.{w=0.5}"

pause 0.5

oak @talkingmouth "At a glance..."

pause 0.5

if (WonBattle("Oak7")):
    oak "It looks like everyone did quite well. Remember, there are many moves, such as Switcheroo, that are {i}intended{/i} to be used on an opponent. But there's absolutely nothing preventing you from using those moves on an ally."
else:
    oak "I recommend everyone brush up on the effects of items. You probably noticed that none of your Pokémon in that fight had damaging moves. Think! How could you inflict damage on the foe, then?"

oak @talkingmouth "Items are going to be a standard part of the curriculum, moving forward. Expect to see them on most future quizzes, and your classmates using them in battles."
oak @talkingmouth "Remember, [bluecolor]all items except berries return to the user at the end of battle.{/color}"

pause 0.5

oak @talkingmouth "Well, that's it for today, class.{w=0.5} You're all dismissed."

call freeroam from _call_freeroam_13

call texting from _call_texting_10

jump day010430