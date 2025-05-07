label gym010511:

$ HealParty()

play music "Audio/Music/Gym_Start.ogg" noloop
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

alder @talkingmouth "And {i}that{/i}'s the end of the lecture! Let's get onto the battles."

bruno @norm2 "[first_name], you will be battling Erika."

red uniform @downeyes sadeyebrows sadmouth "Oh."

hide alder
hide bruno 
with dis

pause 0.5

show erika uniform frownmouth with dis

erika @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

red @angryeyebrows sad2eyes frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

erika @sadbrow talkingmouth "'To define true madness, what is't but to be nothing else but mad? But let that go.'"

pause 0.5

red @confusedeyebrows playfuleyes talking2mouth "I don't have any idea what that means, but it sounds to me like you're quoting an old book at me to apologize?"

erika @sadmouth "That... {i}was{/i} my intent, yes."

red @closedbrow talking2mouth "You're going to need to dumb it down for me, then."

erika @sadmouth "Then... I beg of you, or, rather, as the famous author Heath would say--"

menu:
    "Use your own words.":
        $ AddEvent("Erika", "InterruptQuote")
        erika @surprised "M-my... my {i}own{/i} words? I'm afraid I'm not sure what those would be."

        red @closedbrow talking2mouth "I'm not going to accept an apology from a guy who's been dead a hundred years."

        erika @sadbrow talking2mouth "Two hundred, but I get your meaning."

        pause 0.5

        $ ValueChange("Erika", 3, 0.5)

        erika @closedbrow surprisedmouth "{size=30}My own words...?{/size}"

        pause 0.5

        erika @talkingmouth "Then...{w=0.5} from my own pen...{w=0.5} 'my bad'?"

    ">Stay silent":
        $ AddEvent("Erika", "LetQuote")
        erika @sadmouth "'I found myself in a world unknown, bewildered, and acted on information later proven malformed.'"

        erika @sadmouth "'For that, I am desperately sorry.'"

pause 0.5

red @closedbrow talking2mouth "The first time we met, you thought I was attacking you, and you slapped me in the face."
red @talking2mouth "A week ago, you thought I was mind-controlling you, and you tried to get me kicked from the battle team."
red @sad2eyes talkingmouth "What's going to happen next month? You think I'm stealing priceless art, and you call the cops on me?"

erika @sadmouth "I... I don't think..."

pause 0.5

erika @sadmouth "That that is likely."

$ appearances = ["red uniform", "red uniform angrybrow happymouth", "erika uniform", "erika uniform angrybrow happymouth"]

menu:
    "I accept your apology.":
        $ AddEvent("Erika", "AcceptApology")

        show erika happy with dis

        $ ValueChange("Erika", 10, 0.5)
        erika -sadbrow -frownmouth @talkingmouth "I... am overjoyed to hear that."

        red @talking2mouth "Don't go too crazy. I {i}forgive{/i} you. That doesn't mean I'm going to forget."

        erika -happy @closedbrow talkingmouth "I would not expect you to. But I appreciate you giving me this chance."

        pause 0.5 

        erika @sadbrow talkingmouth "...Again."
        
        red @closedbrow talkingmouth "For now, let's just battle. Ready?"

        erika @happy "Yes, let's."

    "I reject your apology.":
        $ appearances = ["red uniform frownmouth", "red uniform angrybrow frownmouth", "erika uniform sad", "erika uniform sad"]
        $ AddEvent("Erika", "RejectApology")

        $ ValueChange("Erika", -3, 0.5)
        erika @sadmouth "I... understand. I am ashamed of my conduct. I have dishonored my-"

        red @closedbrow talking2mouth "Let's get this battle over with. Ready?"

        erika sadmouth "Yes..."

    "I'm going to need time to think on this.":
        $ AddEvent("Erika", "ThinkOnApology")

        erika @sadmouth "I... understand."

        red @closedbrow talkingmouth "For now, let's just battle. Ready?"

        erika @talkingmouth "Yes, let's."

$ HealParty()
$ trainer1 = Trainer("red", TrainerType.Player, playerparty, number=3)
$ trainer2 = Trainer("erika", TrainerType.Enemy, GetTrainerTeam("Erika"), number = 3)

call Battle([trainer1, trainer2], uniforms=[True, True], customexpressions=appearances) from _call_Battle_124
$ battlehistory["Erika2"]  = _return

play music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

show screen currentdate with dis

pause 1.0

show erika uniform with dis

if (WonBattle("Erika2")):
    if (WonBattle("Erika1")):
        erika @surprised "Oh? I lost again? ...I changed my team, this time, though...."

        red @closedbrow talkingmouth "You're still using a stall strategy. Stall gets weaker the more Pokémon there are on the field."

    else:
        erika @surprised "Oh? I lost? I did not lose last time, though..."

        red @closedbrow talkingmouth "My team's become stronger since the last time we battled."

    erika @talkingmouth "I would say... er... though I advocated for your dismissal from the Battle Team... I always acknowledged your strength and knowledge."

    $ ValueChange("Erika", 3, 0.5)

    erika @talkingmouth "Perhaps it is a good thing that my efforts failed."

else:
    if (WonBattle("Erika1")):
        erika @surprised "Oh? I won? How pleasant. I did not win last time."

        red @closedbrow talkingmouth "Your team's become stronger since the last time we battled. It just makes sense."

    else:
        erika @surprised "Oh? I won? How pleasant. I believe that means I've won twice?"

        red @sad2eyes angryeyebrows talking2mouth "Yeah, yeah. You don't need to rub it in."

    erika @talkingmouth "...Apologies."

show alder at rightside
show bruno at leftside
with dis

pause 1.0

alder @talkingmouth "Everything good here? I saw how you two were battling. You looked pretty intense."

red @angryeyebrows sad2eyes talking2mouth "Yeah, everything's fine."

bruno @norm4 "Anger clouds the mind and weakens the soul. There is nothing to be gained by it in battle."
bruno @think2 "It is a poor man's replacement for discipline. Allow it to strengthen you, steel your resolve, then pass through."

red @closedbrow talking2mouth "I'll... keep that in mind."

jump lunchtransition