label gym010420:

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

alder @talkingmouth "And that concludes the lecture! I hope you were keeping a keen eye on the Battle Team tryouts yesterday--you can tell the battlers there were listening to their lessons!"

alder norm3 @norm4 "Odd ruleset they chose, though."

alder happy @happy2 "Anyway, it's time for double battles again."

bruno @norm2 "Hm. Your battling partner is meant to be Hilbert today, but since you just fought him in the tryouts, I'll find another for you."

red uniform @happy "Oh, cool, thanks. That'd be a bit redundant, wouldn't it?"

bruno @norm4 "There is little use in fighting the same opponent over and over."

bruno @norm2 "Your substitute opponent will be... {i}hm.{/i}"

pause 1.0

bruno @norm2 "Serena will do."

hide alder
hide bruno 
with dis

show serena uniform with dis

if (GetRelationship("Serena") == "Conspirator"):
    serena @happy "Ah, [first_name]! My conspirator!"

    red @confused "I... wouldn't say that so loudly."

    serena @talkingmouth "Oh, Calem gets quite focused when he battles or paints. He really tunes out everything and everyone else."

    serena @happy "We should be fine. Now, do you have any updates for me, regarding your mission?"

    red @closedbrow talking2mouth "Um... he's still single. And no wacky hi-jinx have been required to maintain that status."

    serena @talkingmouth "Splendid job. May I give you a pat on the head?"

    menu:
        ">Accept the pat":
            show serena:
                ease 0.3 ypos 1.2 zoom 1.3
                pause 0.5
                linear 0.3 ypos 1.25
                linear 0.3 ypos 1.2
                pause 0.5
                ease 0.3 ypos 1.0 zoom 1.0

            pause 0.8

            $ AnimateValueChange(1, (0.5, 0.33), False, specialcolor="#ff3b90")
            
            narrator "Your {color=#ff3b90}Headpats{/color} increased to 1!"

        ">Do not accept the pat":
            red @confused "I'll... turn that down, if you don't mind."

            serena @sadbrow talking2mouth "Ah, of course. Pardon my forwardness."

        ">Pat her head":
            show serena blush surprised with dis:
                ease 0.3 ypos 1.2 zoom 1.3

            serena "Eh? Wha- are you--"

            show serena:
                ease 0.3 ypos 1.0 zoom 1.0

            red @sadbrow talkingmouth "Sorry. Too forward?"

            serena closedbrow poutmouth "You should always get permission before laying hands on a lady, [first_name]."

            pause 1.0

            serena talkingmouth "However... I did not {i}hate{/i} that. Still. Only headpat with consent. It's only common courtesy."

else:
    serena @talkingmouth "[first_name]. Splendid to see you. Have you come any closer to unveiling the culprit behind your guerilla campaign?"

    red @happy "Nope. Actually, it wasn't the person I thought it was, so now I basically have {i}no{/i} leads."

    serena @surprised "How curious."
    serena @closedbrow talkingmouth "It seems quite unlikely that someone would spend so much time and effort campaigning on your behalf without your knowledge... but perhaps that is simply what happened. I cannot fathom why, though."

    red @talkingmouth "I've kinda got this vague idea that maybe it wasn't meant to be positive? Like, maybe someone was trying to make fun of me?"

    serena @surprised "For picking up trash?"

    red @sadbrow happymouth "Doing anything with your hands really offends some people. It's not hard to imagine, in this school, there's a couple people who don't want someone like me on the Student Council."

    serena @happy "Well, it's a delightful conspiracy, but I can't imagine that's it."

    red @talkingmouth "Yeah, you're probably right."

serena @talkingmouth "Well, shall we battle now?"

red @happy "Let's."

$ HealParty()
$ trainer1 = Trainer("red", TrainerType.Player, playerparty, number=2)
$ trainer2 = Trainer("serena", TrainerType.Enemy,
[Pokemon(pokedexlookupname("Houndour", DexMacros.Id), level=9, gender = Genders.Male, nature=Natures.Impish, ability="Flash Fire"),
Pokemon(pokedexlookupname("Rhyhorn", DexMacros.Id), level=9, gender = Genders.Female, nature=Natures.Hardy, ability="Lightning Rod")],
number = 2)

call Battle([trainer1, trainer2], uniforms=[True, True]) from _call_Battle_47
$ battlehistory["Serena1"]  = _return

$ HealParty()

stop music fadeout 1.0

hide alder
hide bruno

pause 1.0

show alder norm at centerside with dis
show bruno think at leftside with dis
show serena uniform at rightside with dis

$ renpy.music.queue("Audio/Music/Gym_Loop.ogg", channel='music', loop=True, fadein=1.25, tight=None)
    
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

hide blank2

if (WonBattle("Serena1")):
    serena @happy "Ah, well done. The synchronicity of your Pokémon and yourself is really something to be admired."

    $ ValueChange("Serena", 3, 0.75)

else:
    serena @happy "Hm, hm!~ I won. Lovely."

red uniform @happy "Hey, that was fun. I like the flourishes you add when you let your Pokémon out."

serena @talkingmouth "Ah. Yes, I have some aspirations as a Musical Coordinator. Minor ones, though. Who knows what the future holds, really?"
serena @happy "I find the path one walks is much less important than who you walk it with."

jump lunchtransition