label gym010428:

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

alder @norm2 "And that's the end of the lecture. Time to put our lessons into practice with some battles! Bruno?"

bruno @norm2 "[first_name], you'll be facing Nate."

red uniform @closedbrow talking2mouth "Again? Alright, I guess we'll see what pun he's got in mind this time."

hide alder
hide bruno 
show nate angrybrow frownmouth uniform:
    xpos 0.4
show hilbert angrybrow uniform:
    xpos 0.6
with dis

hilbert @talkingmouth "{size=30}That's all I can tell you. Now give me what you promised.{/size}"

nate @talking2mouth "{size=30}I can't, yet, H. I'm dealing with massively sensitive intel here. I sympathize, I really do, but even with your help on the meteor case, I can't tell you what...{/size}"

show nate surprisedbrow with dis

pause 1.0

show hilbert -angrybrow with dis

$ firstinitial = first_name[0]
nate -frownmouth -surprisedbrow @happy "Heya, [firstinitial]! You're my partner in class today?"

red @talkingmouth "Sure am. Surprised to see you talking with someone else, though, Hilbert. I guess you've been introduced to Nate?"

hilbert @talkingmouth "I've always known him."

red @frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
red @confusedeyebrows talkingmouth "Ohhhhkay. Well, Nate, are you ready for a battle?"

nate @happy "Sure am. Let's do this thing."

hilbert @closedbrow talking2mouth "Wait."

nate @surprised "Huh?"

hilbert @talkingmouth "I want to join you."

nate @happymouth "I mean, I'm flattered, but--"

hilbert @talkingmouth "Instructor Alder! I wish to fight alongside 'Nate' against [first_name] [last_name]!"

pause 1.0

alder @talkingmouth "Sounds good!"

pause 1.0

hilbert @closedbrow talkingmouth "There we go. There's no problem."

nate @talkingmouth "Uh... well, what about [firstinitial]? Are you cool with it?"

red @talkingmouth "Yeah! Let's do it."

if (WonBattle("Roughnecks1") or WonBattle("LeafNateRosa1")):
    red @happy "I mean, I beat {i}three{/i} guys at once before. I think I can handle you two."

hilbert @talkingmouth "...So far, Nate, you've done a lot of {i}talking{/i} about what you can do. Let's see if you have the battle skills to back up your claims."

nate surprisedbrow frownmouth @surprised "Uh..."

hilbert @angry "It doesn't matter {i}what{/i} you know, if you can't protect that knowledge with your power. So show me your power before I agree to be your partner."

red @confused "Uh... what did I walk into?"

hilbert @talkingmouth "Beat us, and you might find out."

redmind @thonk "You're an 'us'?"

# give him choice items
$ nateteam = [GetTrainerTeam("Hilbert", "Honedge"), GetTrainerTeam("Nate", "Trubbish"), GetTrainerTeam("Nate", "Magnemite")]
$ hilbertteam = [GetTrainerTeam("Nate", "Klink"), GetTrainerTeam("Hilbert", "Cubchoo"), GetTrainerTeam("Hilbert", "Snorunt")]

$ HealParty()
$ trainer1 = Trainer("red", TrainerType.Player, playerparty, number=2)
$ trainer2 = Trainer("hilbert", TrainerType.Enemy, hilbertteam, number = 1)
$ trainer3 = Trainer("nate", TrainerType.Enemy, nateteam, number = 1)

call Battle([trainer1, trainer2, trainer3], uniforms=[True, True, True]) from _call_Battle_66
$ battlehistory["HilbertNate1"]  = _return

$ HealParty()

stop music fadeout 1.0

hide alder
hide bruno

pause 1.0

show alder norm at midleftside with dis
show bruno think at farleftside with dis
show hilbert uniform at farrightside with dis
show nate uniform at midrightside with dis

$ renpy.music.queue("Audio/Music/Gym_Loop.ogg", channel='music', loop=True, fadein=1.25, tight=None)
    
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

hide blank2

red @confused "Uh... Nate, how come you had Hilbert's Honedge? And Hilbert, why did you have Nate's Klink?"

nate @talkingmouth "Oops! We must've accidentally swapped Poké Balls at some point."

hilbert @talkingmouth "There was an... altercation. My possessions were scattered around. I guess I just misplaced them."

red @surprised "An altercation? What do you mean? What, did you guys get into a fight?"

nate @happy "Nah!"

hilbert @closedbrow talkingmouth "Yes."

show nate angrybrow frownmouth with dis

nate @talking2mouth "{size=30}Hilbert.{/size}"

hilbert @talkingmouth "It doesn't matter. We realized we had some common ground. And I was entirely incapable of laying a finger on him, anyway."

nate -frownmouth -angrybrow @talkingmouth "Hah, hah! Yeah! Lots of people try to lay fingers on me, so I've gotten pretty good at turning them down. That's the curse of a heartbreaker!"

nate @talkingmouth "Anyway, good battle, man. I'm impressed."

red @talkingmouth "Thanks. Same to you."

pause 1.0

if (WonBattle("HilbertNate1")):
    hide alder
    hide bruno 
    with dis

    show hilbert:
        ease 0.5 xpos 0.6
    show nate frownmouth angrybrow with dis:
        ease 0.5 xpos 0.4

    hilbert @talkingmouth "He's a powerful battler. We should have him join us."

    nate @angrybrow talking2mouth "Absolutely not. This job doesn't need a strong battler, never mind two."

    hilbert @talkingmouth "I trust him. Which is more than I can say for you."

    nate @closedbrow angrymouth "Great. Tell me when your trust yields {i}any{/i} kind of tactical advantage."

    hilbert @thinking "[ellipses]"

    hilbert @happymouth "You like him."

    $ ValueChange("Nate", 3, 0.4)

    nate @talking2mouth "Sure, and Rosa's my favorite movie star, but that doesn't mean I'd ask her to be part of what I'm-- {w=0.5}what {i}we're{/i} dealing with."

    hide nate with dis

    hilbert "[ellipses]"

    hilbert @closedbrow talking2mouth "Hmph."

    $ ValueChange("Hilbert", 3, 0.6)    

    pause 1.0

    hide hilbert with dis

    show alder at rightside
    show bruno at leftside
    with dis

jump lunchtransition