label gym010520:

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

alder @happy2 "And thus concludes the lecture! Bruno, who shall our courageous students be contending against in today's challenge?"

bruno @happy2 "I see you opened that thesaurus I bought you for your birthday."

alder @happy2 "I indeed did! That was an exceedingly generous gesture. And I acquired numerous enjoyable novel vocabulary!"

bruno @think2 "In any case, the partners for today's battles will be..."

pause 1.0

bruno @norm2 "Hm. [first_name] and Yellow."

show yellow uniformbraidfront with dis

hide alder
hide bruno 
with dis

pause 1.0

show yellow uniformbraidfront with dis

pause 1.0

yellow @sadbrow challengingmouth "I'd like to apologize in advance."

red uniform @happy "Hey, it's alright."

yellow @sadbrow challengingmouth "N-no, I'm, um, I'm actually {i}really{/i} bad at battling. And training."
yellow @happy "I used to get through the tall grass in Viridian Forest by just running at top speed before the Pokémon could jump out at me."
yellow @sadbrow challengingmouth "I can count the number of battles I've won on one finger."
yellow @happy "I sometimes {i}lose{/i} fake arguments in the shower."
yellow @sadbrow challengingmouth "I once battled a Magikarp, and it swept my whole team."

pause 1.0

yellow @closedbrow talkingmouth "But it {i}was{/i} Blue's Magikarp, so..."

red @happy "C'mon. It can't really be {i}that{/i} bad, can it?"

yellow @sad2eyes sadeyebrows challengingmouth "I... I guess you'll find out!"
yellow @closedbrow frownmouth "{size=30}Maybe we'll be paired up with someone just as weak...{/size}"

show yellow:
    xpos 0.5
    ease 0.5 xpos 0.25 xzoom -1

show sonia uniform:
    xpos 0.5
show nessa uniform:
    xpos 0.75
with dis

pause 2.0

yellow @closedbrow talkingmouth "{size=30}No such luck.{/size}"

nessa @talkingmouth "Hey."

sonia @talking2mouth "So we're battling you two? Right, then. Let's get on with it."

narrator "Nessa looks at Yellow, then back at you."

nessa @talkingmouth "Here's an idea. How about we just use one Pokémon for this battle? All of us just using one?"

yellow @surprised "Oh! That's... that's an idea. What do you think, [first_name]?"

redmind @thinking "Hm. Nessa must know that Yellow didn't pass the last Quarter Qlashes... or maybe she just overheard our conversation."
redmind @thinking "Either way, she's trying to do something to even the odds. Nice of her."
redmind @thinking "If I take the deal, then I'll probably have to contend with Nessa's Drednaw and Sonia's Yamper... well, should I do it?"
redmind @thinking "[bluecolor]I'll use the first Pokémon in my party, if I do...{/color}"

menu:
    "Nah, let's go all-out.":
        python:
            trainer1 = MakeRed()
            trainer2 = MakeTrainer("Yellow", TrainerType.Ally)
            trainer3 = MakeTrainer("Sonia")
            trainer4 = MakeTrainer("Nessa")

    "Sounds like a plan.":
        $ AddEvent("Nessa", "TookYellowDeal")
        python:
            trainer1 = Trainer("red", TrainerType.Player, [playerparty[0]])
            trainer2 = Trainer("yellow", TrainerType.Ally, [GetTrainerTeam("Yellow", "Pichu")])
            trainer3 = Trainer("sonia", TrainerType.Enemy, [GetTrainerTeam("Sonia", "Yamper")])
            trainer4 = Trainer("nessa", TrainerType.Enemy, [GetTrainerTeam("Nessa", "Drednaw")])

sonia @talking2mouth "Right-o. Let's have at it, then."

call Battle([trainer1, trainer2, trainer3, trainer4], customexpressions=["red uniform", "red uniform angrybrow happymouth", "yellow uniformbraidfront", "yellow uniformbraidfront angrybrow happymouth", "sonia uniform", "nessa uniform", "sonia uniform angrybrow happymouth", "nessa uniform angrybrow happymouth"], dialogfunc=battlewithyellowdialog) from _call_Battle_147
$ RecordBattle("NessaSonia1", _return)

stop music fadeout 1.5
queue music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

show yellow uniformbraidfront:
    xpos 0.25 xzoom -1
show sonia uniform:
    xpos 0.75
show nessa uniform:
    xpos 0.5
with dis

if (WonBattle("NessaSonia1")):
    if (HasEvent("Nessa", "TookYellowDeal")):
        $ ValueChange("Nessa", 2, 0.5, False)
        $ ValueChange("Sonia", 2, 0.75)

        nessa @talkingmouth "Nice. That was actually kinda fun."

        sonia @happy "Solid, all-around. You surprised me!"

    else:
        $ ValueChange("Nessa", 3, 0.5, False)
        $ ValueChange("Sonia", 3, 0.75)
        
        nessa @talkingmouth "Impressive. You aren't bad at all."

        sonia @talking2mouth "Forgive me for this one, but I honestly didn't expect you to pull it off."

else:
    sonia @talking2mouth "Oops. Sorry about that one. Suppose I should've gone a bit easier."

red uniform @happy "Hey, what's that mean? We're Battle Teammates, right?"

sonia @talking2mouth "Sure, but I've got a whole year of experience on you."

nessa @talkingmouth "Come to think of it, Sunny, what happened to your Pokémon last year?"

sonia @surprised "What do you mean, Ness?"

nessa @talkingmouth "Well, your Pokémon are a bit low-level, aren't they? And they're unevolved, too."

sonia @sad "Er... that's sort of what happens when you fall out of practice, when you don't pick up a Poké Ball for a year. And I never evolved most of my Pokémon because... well..."
sonia @happy "Would you throw something at me if I said it was because Yamper's too bloody cute to give up?"

nessa @closedbrow talkingmouth "You're impossible."

sonia @sadbrow talking2mouth "It wasn't {i}really{/i} that, though. Truth be told, evolved Pokémon are harder to command, and I wasn't sure... if, you know..."

nessa @frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
nessa @closedbrow talkingmouth "Well, no wonder you lost, then."

sonia @angry "Ness!"

yellow @sadbrow talkingmouth "I-if it helps at all, I, um... I understand where you're coming from, Sonia. I don't really want to evolve my Pokémon, either."

sonia @talking2mouth "Er... thanks. But you failed to clear the first round of the Quarter Qlashes, didn't you?"

yellow @closedbrow talkingmouth "Yes."

nessa @talkingmouth "Wonder if there's a connection there."

sonia @angry "Ness! Honestly, when did you get so sassy?"

nessa @talkingmouth "Being around Raihan again's reforged all the 'sass' synapses in my mind, I think. I didn't have anyone to match up against before now."

redmind @thinking "I think I just realized the importance of keeping Nessa and Leaf away from each other..."

hide nessa
hide sonia
hide yellow
with dis

pause 1.0

show alder:
    xpos 0.66
show bruno think:
    xpos 0.33
with dis

jump lunchtransition