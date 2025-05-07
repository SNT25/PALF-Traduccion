label nightroam:

$ HealParty() 

label beforemusicnight:

stop music fadeout 2.5

$ renpy.music.queue("audio/music/Eterna_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
$ renpy.music.queue("audio/music/Eterna_Loop.ogg", channel='music', loop=True)

label aftersetupnight:

$ freeroaming = True
scene blank2 as blackground
show nightmap with splitfade

show screen currentdate 
hide blackground
with dissolve
$ trainer1 = Trainer("red", TrainerType.Ally, playerparty)
$ actionperformed = False

menu:
    ">Go out into the forest":
        $ actionperformed = True
        menu:
            "{color=#0f0}[[Easy]{/color} >Rescue Instructor Will from the Unhallowed Holt" if not rescuedwill:
                jump unhallowedholt

            "{color=#00f}[[Medium]{/color} >Rescue Tia from the Shattered Glades" if not rescuedtia:
                if (IsDate(14, 5, 2004)):
                    show phone_B
                    show phone_A
                    show leaf flirtbrow frownmouth hatless behind phone_A:
                        zoom 0.95
                    with fadeinbottom

                    leaf "What...? [first_name], I was asleep..."

                    red @talking2mouth "Tia rescue team, remember?"

                    leaf @surprised "But... Janine said to go right back to the dorm!"

                    red @talkingmouth "It's fine. We have permission, remember?"

                    leaf @closedbrow talkingmouth "...Alright. Be there soon."

                    hide phone_B
                    hide phone_A
                    hide leaf
                    with fadeoutbottom

                jump shatteredglades

            "{color=#f00}[[Hard]{/color} >Rescue Sabrina from the Windswept Woods" if not rescuedsabrina:
                jump windsweptwoods

            ">Nevermind":
                $ actionperformed = False

    ">Heal Pokémon":
        $ HealParty()

    ">Return to your dorm":
        $ actionperformed = True
        call texting from _call_texting_16

label afternightroam:

if (not actionperformed):
    jump beforemusicnight
else:
    $ freeroaming = False

scene blank2

python:
    added = UpdateForeverals()
    if (len(added) > 0 and pikachuobj in playerparty):
        renpy.say(None, "What? [pika_name] started coughing... something's coming out!")
        for key, value in added.items():
            count = len(value)
            if count == 1:
                reward = value[0]
                renpy.say(None, f"Your bond with {key} earned you the {reward}!")
            else:
                rewards = ', '.join(value[:-1])
                last_reward = value[-1]
                exclamation_marks = '!' * math.ceil(count / 3)
                renpy.say(None, f"Your bond with {key} earned you the {rewards}, and {last_reward}{exclamation_marks}")
            
        if (IsAfter(8, 5, 2004) and persondex["Yellow"]["Value"] != 0):
            persondex["Yellow"]["Value"] = len(claimedforeverals)
            renpy.say(None, "Yellow is overjoyed!")

return