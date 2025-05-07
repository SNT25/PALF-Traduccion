label gym010518:

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

alder @happy2 "...and I think that's the end of the lecture, unless I missed something?"

bruno @norm2 "No, I think that covers everything. Though I'm not sure it was completely necessary to list {i}every{/i} single way one could knock out a Shedinja."

alder @happy2 "That's what everyone says, right up until you don't have access to the first twenty ways. And I should know, I use one myself!"

bruno @sad2 "Shameful."

alder @norm2 "Anyway, let's get those battle partners assigned."

bruno @think2 "Mm. [first_name], please battle alongside Rosa."

hide alder with dis

show rosa uniform:
    xpos 0.66

rosa @happy star "Hiiiya! It's Rosa! Battling queen extraordinaire, master of screens and hearts!"

if (GetRelationship("Rosa") == "Fanboy"):
    rosa @talkingmouth "How's my newest fanboy doing?"

    red uniform @happy "I {i}cannot{/i} be your newest fanboy. There are definitely hundreds of people who watched your movies for the first time since I became a fan."

    rosa @sweat talking2mouth "Thousands a day, yes... but the thought is there."

elif (GetRelationship("Rosa") == "Bodyguard"):
    rosa @talkingmouth "How's my bodyguard doing?"

    red uniform @talking2mouth "Alright. Haven't made any progress on figuring out who the phantom photographer in the Battle Hall was, though."

    rosa @closedbrow sweat talking2mouth "I don't think that's really something you need to worry about..."
    rosa @sadbrow lightblush happymouth "But it makes me weirdly happy that you {i}are{/i} worrying about it."

    red @sadbrow talkingmouth "It's what I do. I'm a worrier."

bruno @norm2 "Rosa, you and your partner will be battling Skyla and Silver."

hide bruno with dis

show rosa:
    xpos 0.66
    ease 0.5 xpos 0.25 xzoom -1

show silver uniform:
    xpos 0.75 xzoom -1

show skyla uniform:
    xpos 0.5 xzoom -1

pause 1.0

if (GetRelationshipRank("Silver") > 0):
    silver @closedbrow talkingmouth "Hi, red."

    red @sadbrow talkingmouth "Hi, red."

    skyla @happy "Aw, you guys have cute nicknames for each other! Can I be 'red', too? Because of my red hair?"

    rosa @happy "I think this is already confusing enough. Maybe let's keep it at two reds."

    silver @talkingmouth "...You got any plans?"

    red @talkingmouth "What, you mean, like, to hang out?"

    silver @sadbrow talkingmouth "Just in general."

    red @playfuleyes confusedeyebrows talking2mouth "Well, I'm {i}not{/i} planning on using my charisma to sublimate everyone's wills to mine and rule this school with an iron fist."

    silver @angry "Yeah, it's funny, 'til you {i}see it happen.{/i}"

    red @confused "Hm?"

    silver @talkingmouth "Nevermind. Let's just battle. Show our Pokémon a good time."

else:
    redmind "Silver is staring at me as though he's trying to read my thoughts."

    pause 1.0

    show silver surprisedbrow with dis

    redmind @happy "Sorry, red! Should've been born an Esper."

    show silver -surprisedbrow with dis

skyla @happy "You two! Prepare to get rocked by the full force of two-thirds of the disciplinary committee's strength!"

silver @angrybrow happymouth "Honestly, we're more like nine-tenths of the Disciplinary Committee's strength."

skyla @surprised "Er... yeah, I guess..."

show silver surprisedbrow with dis

rosa @happy "And you, Skyla, are nine-tenths of its charisma."

show silver closedbrow smilemouth with dis

skyla @happy "Aw! That's so nice of you to say, Rosa. Thank you!"

silver @happymouth "{size=30}Airhead.{/size}"

skyla @angrybrow talkingmouth "{size=30}Grimdork.{/size}"

skyla @talkingmouth "Anyway, did I ever tell you, Rosa, that your Riolu girl character is one of my {i}favorite{/i} characters in all of fiction?" 
skyla @angrybrow happymouth "The way she just stands up for justice, even when the going gets rough... it's {i}peak{/i} cinema! I could cry!"

rosa @talkingmouth "Well, I hope you can show me your thanks by giving me a good time in this battle!"

skyla angrybrow happymouth "Count on it!"

silver angrybrow happymouth "You're {i}both{/i} going down."

python:
    trainer1 = MakeRed()
    trainer2 = MakeTrainer("Rosa", TrainerType.Ally)
    trainer3 = MakeTrainer("Silver")
    trainer4 = MakeTrainer("Skyla")

call Battle([trainer1, trainer2, trainer3, trainer4], uniforms=[True, True, True, True]) from _call_Battle_145
$ battlehistory["SilverSkyla1"] = _return

stop music fadeout 1.5
queue music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

show rosa uniform:
    xpos 0.25 xzoom -1
show silver uniform:
    xpos 0.75 xzoom -1
show skyla uniform:
    xpos 0.5 xzoom -1
with dis

if (WonBattle("SilverSkyla1")):
    $ ValueChange("Rosa", 1, 0.75, False)
    $ ValueChange("Silver", 1, 0.25, False)
    $ ValueChange("Skyla", 1, 0.5)

    rosa @happy "And that's a wrap! Great show, guys!"

    silver @closedbrow talkingmouth "...I'm pissed, but you did alright. I'm just mad at myself. I let down my Pokémon..."

    skyla @happy "What? No you didn't, Silver! Your Pokémon were having a great time!"

    silver @angrybrow talkingmouth "You can't know that."

    skyla @angrybrow talkingmouth "I totally can. Don't you know I have the best eyes in the entire school?"

    skyla @happymouth "They were smiling, laughing, and having fun that entire time. I saw them."

    silver @sad "Well, I didn't see any of that."

    rosa @sweat sadeyebrows poutsadmouth "That might be because you were locked onto us with a deadly Kubrick stare that entire time..."

    silver @surprisedbrow "{w=0.5}.{w=0.5}.{w=0.5}."
    silver @talkingmouth "That's just how my face looks."

    rosa @surprisedbrow frownmouth "...Oh!"

    pause 0.5

    rosa @happy sweat "Rosa, exit stage left."

else:
    rosa @sadbrow sweat talkingmouth "Aw... I guess I need a bit more time training these new Pokémon to get over my handicap."

    red uniform @happy "Good effort, though!"

    skyla @happy "Hahaha! The heroes of justice have prevailed!"

    silver @sad "It was a battle in gym class. Calm down."

    skyla @talkingmouth "And are you saying that a fight between worthy adversaries, in order to make us stronger and enhance our bonds with our Pokémon, isn't a just cause?"

    silver @closedbrow talkingmouth "...You're exhausting to talk to."

    skyla frownmouth @angrybrow talking2mouth "And you're so gloomy to talk to!"

    silver @talkingmouth "[first_name], do me a favor. Next time you battle us, just {i}beat{/i} us, so I don't have to deal with {i}this.{/i}"

    red @closedbrow talking2mouth sweat "I'll... do my best."

hide rosa
hide skyla
hide silver
with dis

pause 1.0

show alder:
    xpos 0.66
show bruno think:
    xpos 0.33
with dis

jump lunchtransition