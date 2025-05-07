label gym010430:

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

alder @norm2 "And that... pretty much brings us to the end of the lecture. And the week!"
alder @norm4 "Well, I suppose you students still have lunch, an elective class, and second homeroom, but... well, you catch my drift."

pause 0.5

alder @norm2 "[first_name], a word, for a moment?"

red uniform @talkingmouth "Sure thing, Sir."

alder @norm2 "Let me just look at your team..."

pause 1.0

$ topname = GetStatRank(0)
$ topval = math.floor(classstats[topname])
$ aimlevel = AimLevel()

if (topval > aimlevel + 2):
    alder @norm4 "It looks like you've been doing a good bit of studying. Your best proficiency right now seems to be your [topname] class. Looks like you're about [topval]%% of the way there..."
    alder @happy2 "Good for you. Remember, though, that you've got the entire rest of the year to get your types up."
    alder @norm4 "[bluecolor]If your proficiency in a type is higher than you can realistically get your Pokémon, try spreading your studies around a bit.{/color}"

    red @closedbrow talking2mouth "Right. And, Professor, what would you recommend my levels be around?"

    alder @spunky2 "You're a member of the Battle Team, aren't you? Ask Janine. That youngster's smart as a whip, she'll keep you on track."
    alder @norm2 "You can pretty much always find her in the battle hall, of course."

    pause 0.5 

    alder @norm4 "Although, just to answer your question, level [aimlevel] would be a safe level to aim for right now."

elif (topval < aimlevel):
    alder @norm4 "It looks like you've been doing a good bit of studying, but you're spreading your studies around." 
    alder @norm2 "Your best proficiency right now seems to be your [topname] class. Looks like you're about [topval]%% of the way there..."
    alder @happy2 "You've got the entire rest of the year to get your types up, but it doesn't hurt to apply a little more focus to one or two of them."
    alder @norm4 "[bluecolor]If your proficiency in a type is lower than the levels your Pokémon should be, try focusing on a single type for a few days.{/color}"

    red @closedbrow talking2mouth "Right. And, Professor, what would you recommend my levels be around?"

    alder @spunky2 "You're a member of the Battle Team, aren't you? Ask Janine. That youngster's smart as a whip, she'll keep you on track."
    alder @norm2 "You can pretty much always find her in the battle hall, of course."

    pause 0.5 

    alder @norm4 "Although, just to answer your question, level [aimlevel] would be a safe level to aim for right now."

else:
    alder @happy2 "Mmyep! Looks like there's no issues here! You're doing well, balancing your studies with your training, and pacing yourself for the rest of the school year."

    alder @spunky2 "Well done, kid."

    alder @spunky2 "Here. Take a couple of these, on me."

    $ GetItem("Potion", 3, "Alder tosses a bundle of three Potions at you!")

    alder @norm2 "One of my students convinced me to get into this business plan of hers." 
    
    alder @norm2 "I didn't understand most of what she was saying about 'compacted income' or 'daily pro rations', but she's dropping money into my mailbox every day, so I can't complain. Spent it on teaching supplies."

    red @closedbrow talking2mouth "Hm... that sounds like Gardenia..."

    if (investment == 0):
        redmind @frownmouth "If even Alder is investing in Gardenia's scheme, it's got to be safe, right?"

        redmind @thinking "[bluecolor]Maybe I should pay her a visit at the baseball field.{/color}"

alder @happy2 "Anyway. Time for battles, right? Bruno, who's up?"

bruno @think2 "[first_name], you will be fighting Skyla."

red @talkingmouth "Sounds good!"

pause 1.0

hide bruno
hide alder
show skyla uniform
with dis

if (GetRelationship("Skyla") == "Wingman"):
    skyla @winkbrow smirkmouth "Heya there, sidekick."

    red @angrybrow happymouth "I'm pretty sure we agreed I'd be your wingman, not sidekick."

    skyla @talkingmouth "Alright, alright. Ready to get this battle started?"

else:
    skyla @winkbrow smirkmouth "Heya there, [first_name]."

    red @angrybrow happymouth "Hey. Fly anywhere good recently?"

    skyla @surprised "I did, actually! I went back home to Mistralton to do the Lentimas flight for a while. There were all sorts of weird lights coming from the forest when I flew over campus!"

    red @confused "Huh. I heard there was a forest fire there. Maybe you saw that?"

    skyla @closedbrow talkingmouth "Maybe. I thought it was after the forest fire, actually, but I don't know what else it could've been."

    red @happy "Maybe someone was just holding a rave in the forest."

    skyla @happymouth "Hah, maybe! Ready to get this battle started?"

red @happy "Sure am!"

python:
    trainer1 = MakeRed(2)
    trainer2 = MakeTrainer("skyla", number=2)

call Battle([trainer1, trainer2], uniforms=[True, True]) from _call_Battle_69
$ battlehistory["Skyla1"]  = _return

show alder norm at leftside with dis
show bruno think at centerside with dis
show skyla uniform at rightside with dis

$ renpy.music.queue("Audio/Music/Gym_Loop.ogg", channel='music', loop=True, fadein=1.25, tight=None)
    
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

skyla @surprised "Huh?"

red @talkingmouth "What is it?"

skyla @talkingmouth "It's... um... well, where's your Pikachu?"

red @happy "Oh, that? [pika_name] doesn't like going in his Poké Ball, so I can't take him to gym class. Not enough time to go from my elective back to the dorm, then back here."

skyla @sad "Oh... I was kinda excited to fight him. I know my team's got a massive weakness to him, but I figured that'd be fun to fight against..."

red @sadbrow happymouth "Ah, sorry to disappoint."

if (WonBattle("Skyla1")):
    $ ValueChange("Skyla", 3, 0.75)

    skyla @sweat happy "Ah, it's alright! You didn't need him to beat me, obviously. I could tell you were strong from when we fought that Absol together, anyway."

    if (not WonBattle("Absol1")):
        red @confused "...Skyla, we {i}lost{/i} that battle."

        skyla @sweat happy "Yeah, but we went down fighting!"

skyla @surprised "But, there's, like, a bigger problem here, isn't there? Gym class is the class where you train your Pokémon most. Won't your Pikachu end up really underleveled if you can't bring him to class?"

pause 0.5

red @closedbrow talking2mouth "{w=0.5}...Yeah."

skyla @talkingmouth "Do you know what you're going to do about that?"

pause 0.5

red @talking2mouth "Not... yet. But I'm thinking on it."

skyla @smirkmouth "Alright. Let me know if I can help!"

red @happy "Will do. Thanks!"

jump lunchtransition