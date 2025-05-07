label gym010414:

  

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

alder @talkingmouth "...And that, I believe, is the end of the lecture!"

pause 1.0

alder norm @norm2 "Bruno, do you have a partner for [first_name]?"

bruno happy @happy2 "Yes. Miss, please come here."

redmind uniform "Huh? Bruno looks... uncharacteristically happy. Wait, is he {i}blushing?{/i}"

hide alder
hide bruno 
with dis

show nessa uniform with dis

pause 1.0

if (not persondex["Nessa"]["Named"]):
    red uniform happy "Hi there! Don't think we've met."

    nessa @talkingmouth "Don't think so, no. What's up?"

    red @talkingmouth "I was thinking you looked kinda familiar. Have I seen you somewhere?"

    nessa @closedbrow talkingmouth "Maybe. I've been a model for a few magazines."

    red @talkingmouth "Oh, is that right? I'm [first_name]."

    $ BecomeNamed("Nessa")
    nessa @talkingmouth "Nessa, but I often went under other names. I was a minor until recently, so, you know. Privacy concerns."

    red @talkingmouth "Sure, sure. So how come a model like you is here at Kobukan?"
    red surprised "Ah, shit, that wasn't rude, was it?" 
    red -surprisedbrow -frownmouth -surprised @talkingmouth "I just meant that you've already got a career path, and at such a young age, you know?"

    nessa happy "It's cool."
    nessa -happy "[ellipses]"
    nessa closedbrow talkingmouth "I think... I'm here because I'm afraid it won't last."

    red @thinking "[ellipses]"

    nessa "You know how water erodes rocks over millions of years? Time does the same thing to beauty. Which I guess doesn't sound very modest."
    nessa happy "Sorry, not sorry. I know I'm hot."
    nessa sad "But, you know, I'm not going to have what I have now forever. So I need a backup plan."

    red @talkingmouth "Makes a lot of sense."

    nessa happy "Besides, I always had an interest in Pokémon. I was actually on my way to get my first Pokémon when a recruiter saw me in the street."
    nessa -happy @talkingmouth "After the guy talked to my parents, we went back down to the beach and I caught my Drednaw. Back then, I figured that modeling would be something I'd do to fund my Pokémon career..."
    nessa @talkingmouth "And now it's the opposite."
    nessa happy "Heh."
    nessa -happy @talkingmouth "You're a good listener. You're probably only tolerating me 'cause I'm gorgeous, but, hey, thanks anyway."

    red happy "Hey, if I'm going to beat you in battle, I want to know who I'm beating."

    nessa @talkingmouth "Confident, aren't you? That's good."

    nessa @thinking "[ellipses]"
    nessa @talking2mouth "Look, I'm going to be really busy this year, so I don't have time for anything serious, but if you ask me on a date, I'll say yes."

    red @surprised "Woah. Uh..."

    menu:
        "I'm flattered.":
            red @talkingmouth "Cool. I'm not going to ask you in the gym, though."
            
            nessa @talkingmouth "Thank god. Do {i}not{/i} want to associate this place with dates."

        "Could we get to know each other first?":
            $ AddEvent("Nessa", "DateDeny")
            nessa @frownmouth surprisedbrow "{w=0.5}.{w=0.5}.{w=0.5}."

            nessa @talkingmouth "That's new. But sure."

            red @talkingmouth "Cool. I'll call you later?"

            nessa @talkingmouth "Okay."

            $ persondex["Nessa"]["Relationship"] = "Classmate"

    $ BecomeContacted("Nessa")

    nessa @talkingmouth "When you have some free time, just call me. I'm free whenever."

else:
    red @happy "Hey, Nessa!"

    if (not HasEvent("Nessa", "DateDeny")):
        nessa @talkingmouth "Hey. Good to see you. Noticed you haven't invited me out on that date yet."
    else:
        nessa @talkingmouth "Hey. Good to see you. Noticed that you haven't invited me to hang out, yet."

    red @sadeyes sadeyebrows happymouth "Uh... would you be offended if I said I've been really busy?"

    nessa @talkingmouth "Nah, I get it. Just keep it in mind."

if (not HasEvent("Nessa", "DateDeny")):
    red @closedbrow talking2mouth "Of course. But battles now, dates later, right?" 
else:
    red @closedbrow talking2mouth "Of course. But battles now, hanging out later, right?" 

nessa @happy "Got a good set of priorities there. I appreciate it."

red @happy "I gotta admit, I'm a bit scared of facing you. Not looking forward to fighting that Drednaw of yours."

nessa @talkingmouth "I'm not going to be using her in this battle."

red @surprised "Really? Isn't Drednaw a really powerful Pokémon, though?"

nessa @talkingmouth "Yeah. So I need to get the rest of my team to her level."

red @closedbrow talking2mouth "Don't you want to have the best chance of winning, though?"

nessa frownmouth @sad "...What would winning get me? We learn more from losing."

red @talkingmouth "Well, uh... in my personal experience, people like you more if you're a tough opponent who gives them a good battle."

nessa @closedbrow talkingmouth "Yeah, I guess so. Well, I'm not going to tryhard this."

redmind @thinking "What's up with her...? It feels like she doesn't even care if she wins or loses." 
redmind @thinking "If she doesn't care about people liking her more... but she basically asked me out on a date..."
redmind @thinking "What does this all mean?"

nessa @talkingmouth "Hey. You still with us?"

red @closedbrow talking2mouth "Yeah, I guess. Alright. Let's, uh, battle..."
redmind @thinking "Somehow, she's sucked all the fun out of this..."

$ trainer1 = Trainer("red", TrainerType.Player, playerparty)
$ trainer2 = Trainer("nessa", TrainerType.Enemy,
    [Pokemon(222, level=8, gender=Genders.Female, moves=[GetMove("Tackle"), GetMove("Harden"), GetMove("Bubble"), GetMove("Recover")], ability="Hustle")])#corsola

call Battle([trainer1, trainer2], uniforms=[True, True]) from _call_Battle_16
$ battlehistory["Nessa1"]  = _return

$ HealParty()

stop music fadeout 1.0

hide alder
hide bruno

pause 1.0

show alder norm at centerside 
show bruno think at leftside
show nessa uniform at rightside
with dis

$ renpy.music.queue("Audio/Music/Gym_Loop.ogg", channel='music', loop=True, fadein=1.25, tight=None)
    
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

hide blank2

if (WonBattle("Nessa1")):
    nessa @talkingmouth "Mm. Good job. You're pretty tough."

    $ ValueChange("Nessa", 1, 0.75)

else:
    nessa @sad "Huh. Thought you'd win that one."

red uniform @confusedeyebrows talking2mouth "...That's it?"

nessa @talkingmouth "What do you mean?"

red @closedbrow talking2mouth "I mean... a battle's a back-and-forth. It's all about passion, and fire, and emotions!"
red @sadeyebrows sadeyes talkingmouth "But, uh... you don't seem to care. Before, or after."

red @surprised "Wait, do you not like Pokémon, or battles?" 

if (persondex["Dawn"]["Named"]):
    red @surprised "Are there {i}two{/i} people like that in this school?"

nessa @talkingmouth "No, battles are fun. I like Pokémon, too. I wanted to be a trainer before I wanted to be a model, remember."
nessa @closedbrow talkingmouth "Hm... how to explain this..."
nessa @happy "Oh, I know. So, you know how I mentioned how water erodes rock over millions of years?"

red @closedbrow talking2mouth "Yeah?"

nessa @sad "Well, that's how I see... everything?"

red @surprised "Huh?"

nessa @talkingmouth "Yeah. Everything. The only run that matters is the long-run. So what if I win or lose this battle? It's not even graded."

red @confusedeyebrows talkingmouth "I think... I'm confused."

nessa @talkingmouth "That's fine. It doesn't matter." 
nessa @sadbrow talkingmouth "Try not to take everything so seriously. You'll give yourself wrinkles."
nessa @closedbrow talkingmouth "If you really want to talk more about this... I'm a phone call away."

jump lunchtransition