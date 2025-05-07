label secondhomeroom010422:

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=True, fadein=1.0, tight=None)

scene blank2

show oakbg behind blank2
show homeroom behind oakbg

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with dis

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)
    
show homeroom behind oakbg

oak @talkingmouth "And with that, you should all be ready to handle today's lesson! We're doing things a bit differently for this one."
oak @talkingmouth "In this test, you'll have multiple opponents. Your victory condition is the same as it always is--simply knock your foes out before you're knocked out."
oak @talkingmouth "Don't forget to look over the battlefield {i}very{/i} carefully before committing to any moves! A real battle doesn't give you the luxury of sitting back and planning out your moves, but these tests do, so take advantage of it."

redmind uniform @thinking "Funny, I always feel like I have enough time to think through my moves in {i}my{/i} battles..."

oak @talkingmouth "Finally, there's one piece of information that's very vital. {color=#0048ff}It is not possible for you to faint on your first turn.{/color} As long as you remember that, you should easily be able to handle this challenge!"
oak @talkingmouth "Remember, {color=#0048ff}this is graded!{/color}"

python:
    trainer1 = Trainer("red", TrainerType.Player, [
        Pokemon(pokedexlookupname("Rhydon", DexMacros.Id), level=42, moves=[GetMove("Take Down"), GetMove("Earthquake"), GetMove("Horn Drill"), GetMove("Smack Down")], ivs=[0, 0, 0, 0, 0, 0])
    ])
    trainer2 = Trainer("oak", TrainerType.Enemy, [
        Pokemon(pokedexlookupname("Cryogonal", DexMacros.Id), level=10, moves=[GetMove("Ice Shard")], ability="Levitate"),
        Pokemon(pokedexlookupname("Meditite", DexMacros.Id), level=10, moves=[GetMove("Bide")], ability="Pure Power"),
        Pokemon(pokedexlookupname("Swinub", DexMacros.Id), level=10, moves=[GetMove("Endure")], ability="Oblivious")
    ], number=3)

    trainer1.GetTeam()[0].AdjustHealth(trainer1.GetTeam()[0].Health * 1/16 + 2, absolute=True)
    trainer2.GetTeam()[0].Health = 1
    trainer2.GetTeam()[0].ApplyStatus("asleep", 1)
    trainer2.GetTeam()[1].Health = 1
    trainer2.GetTeam()[2].Health = 1
    trainer2.GetTeam()[2].ApplyStatus("burned")

call Battle([trainer1, trainer2], clearstats=False, gainexp=False, healParty=False, uniforms=[True, False], currentWeather=("hailing", 5), lockbag=True) from _call_Battle_50
$ battlehistory["Oak5"] = _return

$ renpy.transition(dissolve)
show screen currentdate

red uniform @surprised "Geez! That was a bit of a difficulty spike, wasn't it?"

oak @talkingmouth ".{w=0.5}.{w=0.5}.{w=0.5}"

pause 0.5

oak @talkingmouth "At a glance..."

pause 0.5

if (WonBattle("Oak5")):
    oak "It looks like everyone did quite well. I'm glad you were all able to handle more advanced concepts, such as weather and ability-immunity."
else:
    oak "I recommend everyone brush up on the exact effects of weather. Hail, though not common in the Kobukan region, can be found in certain mountainous ranges."

oak @talkingmouth "Remember, weather conditions often have many effects that aren't explicit. Blizzard will never miss in hail or snow. Rock-types get a Special Defense boost in sandstorms."
oak @talkingmouth "There are many abilities that trigger under the effect of sun or rain, as well. Keep these in mind!"

oak @talkingmouth "That's it for today, class.{w=0.5} You're all dismissed."

call freeroam from _call_freeroam_8

scene dorm_B norm with Dissolve(2.0)
    
stop music fadeout 2.5

queue music "Audio/Music/Road to Viridian City.ogg"

show brendan at rightside
show calem at leftside 
show hilbert at midrightside
show ethan at midleftside
with dis

calem @happy "Ah, [first_name]. You're back. Good. Perhaps you could help us resolve this mild deliberation we're having."

red @closedbrow talking2mouth "Oh, yeah? What're you talking about?"

calem @talkingmouth "Well, Cheren has been surveying people across the school about the curfew issue."

calem @closedbrow talking2mouth "We've come to some different conclusions."

brendan @sad "Yeah. Like, I didn't know that there were gangsters out there 'n all, but since there are, we gotta keep the curfew, right? It's the only way to keep us safe."

hilbert @angry "You're a coward. We go to school {i}every day{/i} to learn how to battle better. If you aren't confident in your ability to defend yourself, just drop out now."

ethan @talking2mouth "Hey, man, lay off. Didn't you say you didn't think you'd get onto the Battle Team?"

hilbert @talkingmouth "I did, but I know I've enough power to beat down some untrained derelict from the city."

ethan frownmouth @talking2mouth "I mean, you said the same thing about your opponents in the Battle Tryouts..."

if (not WonBattle("Ethan1")):
    hilbert @angry "You won {i}one{/i} of your matches! The fact you got in at all is ridiculous."
else:
    hilbert @angry "You won {i}zero point zero{/i} of your matches! The fact you got in at all is ridiculous."

red @talking2mouth "Well, what do you think, Calem?"

calem @talkingmouth "Well, publically, I support the repeal, of course. I've already said as much officially."
calem @sad "Though... this new information about vagrants from the city is concerning..."

menu:
    "{color=#ff8412}[[Courage]{/color} They're no trouble.":
        $ ValueChange("Hilbert", 1, 0.63)
        $ TraitChange("Courage")
        calem @surprised "Oh? Do you have personal experience with them, then?"

        red @talkingmouth "Yeah. Ran into them last Saturday. They're pretty much just bluster. Even a new student should be able to handle them well enough."

        hilbert @closedbrow talkingmouth "See?"

        brendan @sad "Well... if you say so, dude. Still not sure I want May goin' out alone when it's all dark out, but I guess if we go together it'll be fine..."

    "{color=#60c2f8}[[Wit]{/color} Probably better safe than sorry.":
        $ ValueChange("Brendan", 1, 0.75)
        $ TraitChange("Wit")
        brendan @surprised "Oh, you agree with me, dude?{w=0.5} {i}Phew!{/i}{w=0.5} I was worried I was worryin' over nothing."

        if (WonBattle("Hilbert2")):
            hilbert @sadbrow talkingmouth "Tch. You beat me in the tryouts, [first_name]. You should know that, with your strength, there's nothing to fear."
        else:
            hilbert @angry "Your opinion is obviously influenced by your loss against me in the tryouts, [first_name]."

            hilbert @sadbrow talkingmouth "If you can't even beat me, no wonder you're afraid of some shiftless societal rejects living in the gutters."

        red @talking2mouth "Well, that's my opinion. Take it or leave it."

ethan @thinking "[ellipses]"

red @talkingmouth "What do you think, Ethan?"

ethan -frownmouth @sadbrow happymouth "Man, I don't think I can answer that unbiasedly. Now I'm just thinking about what you said." 
ethan @sadbrow happymouth "If I agree, then I'm just agreeing with you, and if I don't, then I'm purposefully disagreeing with you."

red @happy "Ah, I getcha. I'll let you answer first next time, then."

ethan @talkingmouth "Cool. I'm going to bed, though. G'night, guys!"

hide ethan with dis

calem @closedbrow talkingmouth "Goodnight, gentlemen. Sleep well."

hide calem
hide brendan
hide hilbert
with dis

redmind hatless casual "Alright, changed. Now, where's my phone...?"

call afterroomsetuptexting from _call_afterroomsetuptexting_3

jump day010423