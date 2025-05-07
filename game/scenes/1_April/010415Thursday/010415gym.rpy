label gym010415:

  

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

alder @talkingmouth "And that's why Dracovish is such a common threat in competitive battling circuits!"
alder angry @angry2 "I'll remind you, though, {i}purposefully{/i} creating one is not only illegal, but {i}very{/i} immoral."

pause 2.0

alder spunky2 "But I'm sure none of you will do that. So that's the end of the lecture!"

pause 1.0

alder norm @norm2 "Bruno, who'll [first_name] be battling today?"

bruno norm @norm2 "[first_name], you'll be battling Cheren today."

red uniform @closedbrow talking2mouth "Huh, Cheren again, so soon? Alright."

hide bruno
hide alder
show cheren uniform
with dis

cheren @talkingmouth "[first_name]. Hello."

red @happy "Hi! How's the Student Council campaign going?"

cheren @sad "Could be better. Brawly recently told me some... disquieting news."
cheren @closedbrow talking2mouth "And Professor Samuel Oak has asked me to visit him in his laboratory after school today, so I'm afraid as to what that might entail."
cheren @sad "I'm not even in his homeroom, so this must relate to some of my positions. And if the faculty is asking to talk to me one-on-one about them..."

red @sadeyes sadeyebrows talkingmouth "Sounds scary. But I'm sure it's nothing. I actually know Sam, and he's a great guy. He probably just wants to let you know he supports you."

cheren @disappointed "So fervently do I wish for that to be the case."
cheren @talking2mouth "But the time to talk about that is not now. Are you ready to battle, [first_name]?"

red @happy "Born ready!"

$ trainer1 = MakeRed()
$ trainer2 = MakeTrainer("Cheren")

call Battle([trainer1, trainer2], uniforms=[True, True]) from _call_Battle_17
$ battlehistory["Cheren2"]  = _return

$ HealParty()

stop music fadeout 1.0

hide alder
hide bruno

pause 1.0

show alder surprisedbrow frownmouth at centerside 
show bruno think at leftside
show cheren uniform at rightside
with dis

$ renpy.music.queue("Audio/Music/Gym_Loop.ogg", channel='music', loop=True, fadein=1.25, tight=None)
    
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

hide blank2

if (WonBattle("Cheren2")):
    cheren @closedbrow talking2mouth "An expected outcome, but a well-deserved victory."

    $ ValueChange("Cheren", 3, 0.75)

else:
    cheren @surprised "That's interesting. Er, but well-fought."

alder @surprised2 "Cheren, what's happening here?"

cheren @surprised "Sir?"

alder @angry2 "Your Pokémon {i}still{/i} aren't improving. Haven't you been critiquing them, like I said? And keeping up on your studies?"

cheren @closedbrow talking2mouth "Certainly. I am amongst the top students for both my electives."

alder @angry2 "Then why do you still have only a level five Purrloin?"
alder @sad2 "No, hold on--"
alder norm3 @angry2 "Why do you still have {i}only{/i} a level five Purrloin?"

cheren @angry "I have found my time to train and catch new Pokémon limited, given the many other important activities I am engaging in."

bruno @norm2 "There is nothing more important than your training. You cannot succeed in this school without it."

cheren @sadmouth "Perhaps my metrics for success are different to yours."

alder @surprised2 "Young man, we {i}literally{/i} decide what this school's metrics for success are."

pause 1.0

cheren sadbrow @sad "That is a fair point."

pause 1.0

bruno @think2 "You must learn to pick your battles. Right now, you are aiming to cleave the mountain in two, before practicing a single strike."

alder @sad2 "I wouldn't normally say this, young man, but this is a dire situation... you really need to focus on your schoolwork. Which {i}includes{/i} training."

cheren @closedbrow talking2mouth "Yes, Sir. Apologies for my brusqueness earlier, Sir."

alder @spunky2 "It's alright. I expect to see you win your next battle, though!"

bruno @surprised2 "He... may need a bit more training before that, Alder."

alder @sad2 "Oh, yeah... okay. I expect to see you win your battle on Monday, then."

cheren @closedbrow talking2mouth "{size=30}Even so, that's only four days... I doubt even Blue and his friend could train hard enough to get me combat-ready in that amount of time... Hm.{/size}"

hide cheren with dis

jump lunchtransition