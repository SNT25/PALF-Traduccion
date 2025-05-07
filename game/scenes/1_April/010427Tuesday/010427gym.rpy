label gym010427:

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

alder @norm2 "...And if there's anything more you want to hear about, then let me or Bruno know."

alder @happy2 "In the meantime, it's time to do some battles! Bruno?"

bruno @norm2 "Bea. You will be fighting [first_name] today."

hide alder
hide bruno 
show bea uniform
with dis

bea @talkingmouth "'Lo."

red uniform @happy "Hey, Bea. We didn't end up battling each other during the Battle Team tryouts, did we? I guess this is our first battle, then."

bea @closedbrow talkingmouth "I'm looking forward to it."

if (GetRelationship("Bea") == "Planner"):
    bea @talkingmouth "Through battle, I hope to convey to you my gratitude for the help you have provided me. Your assistance in my training has been most enlightening."

    red @happy "Hey, I haven't done that much."

    bea @closedbrow talking2mouth "But what you {i}have{/i} done means a lot to me."

    if (beahastyrogue):
        bea @talkingmouth "That isn't even mentioning how you helped talk me through what I would evolve my Tyrogue into. Without your presence, I would doubtlessly still be muddling it over in the Battle Hall."

    red @happy "Well, I'm happy to help. Repay me by giving me a good battle."

    pause 0.5

    bea @happymouth "{i}Hai.{/i} {w=0.5}{nw}"
    extend @angry "Begin!"
else:
    bea @talkingmouth "I have spent much time preparing for battle against you. I have formulated a dozen strategies, each designed to take down your Pokémon with unflawed precision."

    red @happy "Oh, yeah? Care to share any of those plans?"

    bea @talkingmouth "No. They all suck beans."

    red @confused "Beg pardon?"

    bea @talkingmouth "It's a Galarian expression that means 'they're rotten.'"

    red @confused "Yeah, no, I got that from context. Uh, why are they rotten?"

    bea @closedbrow talking2mouth "They're far too complicated. After a while, each of my plans that related to defeating you now required me to have set events in motion several weeks before our battle."

    red @happy "Oof. Well, unless you have a time machine, that might be a bit of a problem."

    bea @talkingmouth "Rather."

    if (beahastyrogue):
        bea @talkingmouth "You helped me make my mind up about my Tyrogue, and I'm grateful for that. But I can understand why you would not help me come up with a plan to beat you."

        red @talkingmouth "Thanks."

    bea @talkingmouth "In any case, in lieu of a plan guaranteeing victory, I'm confident in my raw strength."

    red @happy "Well, so am I. Guess there's only one way to solve this, huh?"

    bea @talkingmouth "{i}Hai.{/i} {w=0.5}{nw}"
    extend @angry "Begin!"

$ HealParty()
$ trainer1 = Trainer("red", TrainerType.Player, playerparty, number=2)
$ trainer2 = MakeTrainer("Bea", number=2)

call Battle([trainer1, trainer2], uniforms=[True, True]) from _call_Battle_65
$ battlehistory["Bea1"]  = _return

$ HealParty()

stop music fadeout 1.0

hide alder
hide bruno

pause 1.0

show alder norm at centerside with dis
show bruno think at leftside with dis
show bea uniform at rightside with dis

$ renpy.music.queue("Audio/Music/Gym_Loop.ogg", channel='music', loop=True, fadein=1.25, tight=None)
    
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

hide blank2

if (WonBattle("Bea1")):
    bea @happy "A worthy battle. It brought palpitations even to my heart."

    $ ValueChange("Bea", 3, 0.75)

else:
    bea @happy "Hm. Perhaps the importance of a solid plan was overstated by our instructors."

python:
    playerhastyrogue = False
    for mon in playerparty:
        if (mon.GetId() == pokedexlookupname("Tyrogue", DexMacros.Id)):
            playerhastyrogue = True

if (beahastyrogue):
    red @talkingmouth "I see you've been training that Tyrogue of yours."

    bea @talkingmouth "Yes. His personality is... a bit quirky, compared to the rest of my team. However, he trains diligently. I am pleased enough with his progress so far."

    bea @closedbrow happymouth "I am certain he will make an excellent Hitmontop."

elif (playerhastyrogue):
    bea @talkingmouth "I see you've been training that Tyrogue from the egg."

    red @talkingmouth "Yeah. Strong little guy. You know, for a baby."

    bea @closedbrow happymouth "I am certain, when he evolves into your chosen Hitmon, he will be a valuable contributor to your team."

    red @talkingmouth "Bet he will!"

else:
    bea @talkingmouth "Still. This only outlines the importance of further training. I encourage you to join me some time."

    red @closedbrow talking2mouth "Oh, so it's no longer a 'you must take responsibility' kinda thing?"

    bea @closedbrow talkingmouth "It occurred to me that getting angry over being forced to emote was self-defeating."

    red @closedbrow talkingmouth "Yeah, I can see that."

jump lunchtransition