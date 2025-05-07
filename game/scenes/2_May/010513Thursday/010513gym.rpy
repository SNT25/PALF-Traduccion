label gym010513:

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

alder @talkingmouth "...so Life Orb on a Pokémon with Sheer Force gives you all the benefits of the item, with none of the downsides! Do keep that in mind. It's a useful combo that's very easy to pull off."
alder @closedbrow talkingmouth "Now, it's time for the battles. Bruno?"

hide alder with dis

pause 1.0

show grusha uniform with dis:
    xpos 0.66

grusha @confusedeyebrows talking2mouth "{i}Ey. Que bueno verte.{/i}"

red uniform @talkingmouth "Same to you, I assume."

bruno @norm2 "Grusha, are you well enough to battle today?"

grusha @closedbrow talking2mouth "As far as I can tell."

bruno @think "Hrm."
bruno @norm2 "[first_name], your opponent will be Grusha."

hide bruno with dis
show grusha:
    ease 0.5 xpos 0.5

pause 0.5

grusha @sad2eyes talking2mouth "You're probably sick and tired of people talking about your speech, your Pikachu, or your power."

grusha @closedbrow talking2mouth "I'm sick of people asking if I'm okay and pretending to care that I didn't get to be some Student Council whatever."

menu:
    "Yeah, let's skip all that.":
        $ ValueChange("Grusha", 1, 0.5)

        grusha @closedbrow talking2mouth "{i}Finalmente.{/i}"

    "I kinda wanted to talk about it...":
        $ ValueChange("Grusha", -1, 0.5)

        grusha @upeyes talking2mouth "With all respect, find a wall to tell it to. I just want to battle."

        red @sadbrow talking2mouth "Alright, man..."

grusha @talkingmouth "{i}Sigh.{/i} ...I saw what you did to Dawn."

red @talkingmouth "Yeah?"

grusha @happymouth "...What you did was cold. Made a mockery of her, all her training, all her power, in front of the entire school."

red @angrybrow talking2mouth "Hey, I--"

grusha @closedeyes sadeyebrows "Chill. I liked it. And it's not like you had a choice, anyway."
grusha @happyeyes talking2mouth "Heh. You should see what people on the internet are saying about you and her, though. They're calling her Altaria 'Jobbird.'"

red @poutmouth "That doesn't seem very nice."

grusha @talkingmouth "People say that the internet's anonymity gives people the freedom to be dicks without repercussions, but I've seen people be dicks to each other, face-to-face, so I don't know, maybe people are just trash."

red @playfulbrow talking2mouth "...Is depressing me part of your battle strategy?"

grusha @closedbrow talking2mouth "...Heh."
grusha noscarf @talkingmouth "No. But I might keep that in my back pocket, for the future."

red @surprised "Your scarf-- are you...?"

grusha @sad2eyes talking2mouth "Gets hard to breathe with it on. Harder to yell commands, too. Don't worry about it."

pause 1.0

grusha @closedbrow talking2mouth "Alright. Let's go."
grusha angrybrow happymouth "One request. Don't make this exciting."

python:
    trainer1 = MakeRed(3)
    trainer2 = Trainer("grusha", TrainerType.Enemy, GetTrainerTeam("Grusha"), number=3)

call Battle([trainer1, trainer2], uniforms=[True, True], customexpressions=["red uniform", "red uniform angrybrow happymouth", "grusha uniform noscarf", "grusha uniform noscarf angrybrow happymouth"]) from _call_Battle_130
$ RecordBattle("Grusha1")

play music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

show grusha uniform noscarf with dis

grusha @talkingmouth ".{w=0.5}.{w=0.5}.{w=0.5}Hm."

if (WonBattle("Grusha1")):
    grusha -noscarf @talkingmouth "...That was alright."

    $ ValueChange("Grusha", 3, 0.5)

    grusha @talkingmouth "You're a good battler."

    red @talkingmouth "You're not too shabby yourself."

else:
    grusha -noscarf @talkingmouth "...Well, I {i}did{/i} ask you not to make it exciting."

pause 2.0

if (HasEvent("Jasmine", "TellGrushaThanks")):
    grusha "Oh. Yeah. Jasmine told me that you said 'thanks' for standing up for you. Before the speech, I mean. Now everyone is."
    grusha @upeyes talking2mouth "People love their bandwagon."

    red @talkingmouth "Really, it means a lot. It's nice knowing there were people who believed in me even before I could sort everything out."

    $ ValueChange("Grusha", 1, 0.5)

    grusha @closedbrow talking2mouth "Hm. I know you would've done the same for any of us."

else:
    red @talkingmouth "Uh, Jasmine told me that you, uh, you stood up for me. Or, at least, told Jasmine you didn't think I had mind-powers."

    grusha @upeyes talking2mouth "Yeah, well, I was obviously wrong about that."
    grusha @closedbrow talking2mouth "Whatever. The point is you're not evil. I got that part right, at least."

    red @happy "Thanks."

    grusha @closedbrow talking2mouth "I do what I can."

pause 2.0

redmind @poutmouth "He's... kinda hard to talk to, huh?"

pause 1.0

grusha @sad2eyes talking2mouth "...Getting kinda chilly in here."
grusha @closedbrow talking2mouth "I'm outsies."

hide grusha with dis

pause 1.0

show alder:
    xpos 0.66

show bruno:
    xpos 450
with dis

jump lunchtransition