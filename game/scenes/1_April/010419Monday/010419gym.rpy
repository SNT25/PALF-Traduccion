label gym010419:

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

alder @talkingmouth "And that concludes the lecture!"

pause 2.0

alder norm @norm2 "[first_name]. Let's talk before you have your battle."

red uniform @happy "Yes, Sir!"

alder @surprised2 "You seem chipper."

red @talkingmouth "I guess I'm just excited about the battle tryouts later today, Sir."

alder @norm4 "Ah. You'll be trying out for them, then?"

red @talkingmouth "I'm going to be winning them, Sir."

alder @angry2 "Be careful of what you say.{w=0.5} Arrogance and strength do not go hand in hand." 

red @sadbrow happymouth "Er... right, Sir. It was meant to be confidence. Not arrogance."

alder @sad2 "The lines {i}are{/i} often blurred, aren't they?" 
alder @norm2 "Well, that doesn't matter. If you're going for the battle tryouts already, you need this advice even more."

red @talkingmouth "All your advice has been really helpful so far. What can I do to get better?"

alder @happy2 "It's not so much a 'do this to get better,' this time. Just consider this a check-in. Like at the doctor's." 
alder @norm2 "I just want to make sure you're on the right track to succeed."

pause 1.0

alder @norm3 "{w=0.5}.{w=0.5}.{w=0.5}.Hm."

$ hadproblem = False
$ excusesecondelective = False
$ excusesecondhomeroom = False

if (GetElective(GetStatRank(0)) < 7):
    $ hadproblem = True
    alder @norm2 "Well, I think you could do with a bit more studying."
    alder @norm2 "Early in the school year, like this, it's better to focus on one or two types, so you can make one Pokémon as strong as you can get it."
    alder @norm4 "It's tempting to take a whole bunch of different classes, to meet as many people as you can, but it's better to go deep before you go wide."

if (len(playerparty) < 4):
    if (hadproblem):
        alder @norm2 "That's not all, though."
    $ hadproblem = True
    alder @norm2 "Your party looks a bit small, doesn't it?"
    alder @norm4 "Early on, it's good to focus on having one or two strong party members, but I can't overstate how important it is to have multiple backup plans."
    alder @happy2 "Having another Pokémon in your reserve means you have many more options for you to get an advantageous type matchup. And more options to switch into if your Pokémon has its attack, defense, or accuracy lowered."
    alder @norm2 "Plus, there are some strong wild Pokémon out there. Even if you don't plan on raising them as part of your final team, you might want to catch them until some better options present themselves."
    alder @spunky2 "It's important to know what your Pokémon are capable of, of course, but power's power. If a Pokémon is immediately strong, even if you don't have a long-term plan for them, you might want to battle with them, anyway."
    alder @norm2 "In short... try to get a full team."

if (GetHighestLevel() < 10):
    if (hadproblem):
        alder @norm2 "One more thing."
    $ hadproblem = True
    alder @norm2 "Your Pokémon are a bit underleveled."
    alder @norm4 "After a while, your Pokémon will barely get any experience from battling against untrained 'mons, in the wild. So while you've both barely got any experience, take advantage of it!"

    red @confused "...Sir, are you telling me to go into the wild and beat up the Pokémon I find there?"

    alder @spunky2 "Ah-ah-ah! 'Train' against the Pokémon you find there."

    red @confused "...Right."

if (not hadproblem):
    alder @spunky2 "Well, sorry to get your hopes up! Looks like you're completely on-course."

    red @happy "Well, I'm not going to complain about that. Thanks, Sir. Guess all my studying paid off."

    $ TraitChange("Knowledge")

else:
    alder @norm2 "But that's all."

    red @confused "{i}That's all?{/i} Geez, Sir. I definitely don't have time to do that before the Battle Tryouts later today."

    alder @norm4 "Hm... well, I don't normally do this, but I {i}would{/i} be willing to grant you an excused absence for your second homeroom and elective class."

    red @surprised "What?"

    alder @happy2 "If you want, I'll let you go from class early to handle that. Obviously, there's only so much you can do, but I'll give you that time."

    red @closedbrow talking2mouth "Well... what about my classes?"

    alder @sad2 "Yes, you would be missing an elective class, and your second homeroom."

    red @sad "I've got a quiz in my second homeroom..."

    alder @norm2 "Well, you can afford to miss one quiz." 
    alder @sad2 "Er... don't tell Oak I said that."
    alder @happy2 "Obviously, it won't count as a success on your final grade, but with an excused absence, it won't count as wrong, either."
    alder @norm2 "So. What'dya say?"

    menu:
        ">Take an Excused Absence for your second elective":
            $ excusesecondelective = True
            red @happy "Thanks, Sir. I think I can probably skip my second elective to go train a bit more."
        ">Take an Excused Absence for your second homeroom":
            $ excusesecondhomeroom = True
            red @happy "Thanks, Sir. I think I can probably skip my second homeroom to go train a bit more."
        ">Take an Excused Absence for both":
            $ excusesecondelective = True
            $ excusesecondhomeroom = True
            red @happy "Thanks, Sir. I think I'll take you up on that offer."
        ">Don't take an Excused Absence":
            red @happy "Thanks, Sir. But I think I'll be fine."

    alder @happy2 "Alright. Just remember, this was your decision."

alder @norm2 "Anyway, that's enough of that. You've got to do a gym class battle before you can try to join the Battle Team! And remember, we're starting double battles this week!"

bruno @norm2 "Your opponent will be--"

show alder surprisedbrow frownmouth
show bruno surprisedbrow frownmouth
with dis

show gym with vpunch

red @surprised "Ah!"

bruno @surprised2 "[first_name]?"

red @happy "Sorry, Sir! You were so still and quiet, I forgot you were here."

show alder happy
show bruno happy
with dis

bruno @happy2 "Hm. I've often heard that. No matter. Here's your opponent for today."

hide alder
hide bruno 
with dis

show hilda uniform with dis

if (GetRelationship("Hilda") == "Caretaker"):
    hilda angry "[first_name]! You've got a lot to answer for!"

    red @happy "Ah. Guess you saw that stuff I did for you, then."

    hilda @closedbrow talking2mouth "Yeah, you could say that. Copying my keys? Ironing my uniforms? Putting new de-scenter in my shoes?"

    red @talkingmouth "Oh, so I guess you didn't find the pasta yet?"

    hilda @surprised "That was you?! I thought it was May!"

    red @talkingmouth "Nope. Guilty as charged."

    hilda frownmouth -angry @surprised "How do you even find time for all this?!"

    red @sadbrow talkingmouth "Gotta admit, it's a struggle. But every time I feel like giving up, I just remember that if I don't do it, you'll have to. And that gives me the motivation to keep going."

    hilda @surprised "{w=0.5}.{w=0.5}.{w=0.5}."

    hilda angry veins "Dumbass. I never asked you to do any of this shit!"

    red @happy "Yeah, but no-one asked {i}you{/i} to do any of it, either."

    hilda @closedbrow talking2mouth "How do you even know this stuff needs to be done?"

    red @sadbrow talkingmouth "No matter how much you threaten them to keep quiet to me, Dorm 251 is full of your friends. And they want you to take a break, too."

    hilda @angry veins "Oh, I'll take a break.{w=0.5} I'll break your face in, farmer! Get over here!"

else:
    hilda angry "Alright, who's next?!"

    red surprised "Huh? Hilda?"

    hilda -angry @closedbrow talking2mouth "Oh, it's you..."

    hilda @talkingmouth "Well, you better be warned that when I battle, I {i}really{/i} let loose."

    red @happy "Sounds good. No need to hold back against me. Go wild."

    hilda @angrybrow happymouth "Believe me, I will! Get over here!"

$ HealParty()
$ trainer1 = Trainer("red", TrainerType.Player, playerparty, number=2)
$ trainer2 = MakeTrainer("Hilda")

call Battle([trainer1, trainer2], uniforms=[True, True]) from _call_Battle_44
$ battlehistory["Hilda1"]  = _return

$ HealParty()

stop music fadeout 1.0

hide alder
hide bruno

pause 1.0

show alder norm at centerside with dis
show bruno think at leftside with dis
show hilda uniform at rightside with dis

$ renpy.music.queue("Audio/Music/Gym_Loop.ogg", channel='music', loop=True, fadein=1.25, tight=None)
    
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

hide blank2

if (WonBattle("Hilda1")):
    hilda @happy "Phew. Getting to go all-out like that was goddamn therapeutic! You should open a clinic."

    $ ValueChange("Hilda", 3, 0.75)

else:
    hilda @sadbrow frownmouth "Eh... didn't feel like I got to go all-out that time."

if (GetRelationship("Hilda") == "Caretaker"):
    hilda @sad "Anyway, sorry about... blowing up at you before the battle. I get kinda intense when I battle. Letting off some steam, you know."

    red @happy "It's cool."

hilda @closedbrow talking2mouth "Hey, are you going to the Battle Team tryouts?"

red @talkingmouth "Going to? I'll be {i}in{/i} them."

hilda @surprised "No shit? Hilbert's mentioned them a couple times, but he didn't say you were going to be there."
hilda @sad "I actually have something to do off-campus. I want to be there to watch Hilbert, but... I gotta go into the city."
hilda @talkingmouth "Would you mind streaming a couple of his battles to me? I know this is a massive thing for him."

red @talkingmouth "'Course not. Not a problem. My phone's kinda crappy, so I can't promise it'll be smooth, but I'll try to hold it up for better service."

hilda @talkingmouth "Cool. Thanks."

pause 1.0

red @sadbrow talkingmouth "I'll need your contacts, though."

hilda @surprised "Crap, I thought I'd given you that already. Yeah, sure, here."

$ BecomeContacted("Hilda")

red @happy "Cool. I'll keep you informed."

hilda @happy "Yeah, thanks."

if (GetRelationship("Hilda") == "Caretaker"):
    hilda @talkingmouth "But you better not use that phone number to try and take more of my jobs, got it?"

    red @confused "How would I even do that?"

    hilda @closedbrow talkingmouth "Ugh, you'd find a way."

jump lunchtransition