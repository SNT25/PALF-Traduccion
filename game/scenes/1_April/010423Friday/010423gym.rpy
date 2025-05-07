label gym010423:

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
    xpos 350

show bruno think with dis:
    xpos 950

alder norm @spunky2 "And that's pretty much it! Expect that most official battles you'll participate in will have some combination of the item, species, and sleep clauses."
alder @norm2 "It's also pretty common in other regions to ban evasion strategies, but it's a bit less common here."
alder @happy2 "Largely because Kobukan puts a lot more emphasis on non-single battles. Still, make sure you've got a team that can withstand any ruleset they throw at you!"

bruno norm @norm2 "That concludes the lecture."

pause 1.0

bruno @norm2 "Alder, do you have a partner for [first_name] [last_name]?"

redmind uniform @surprised "Whoa. Did I step into Bizarro World? Bruno's doing Alder's job!"

alder @happy2 "I reckon I do. Miss Birch, if you please?"

hide alder
hide bruno 
with dis

pause 1.0

show may uniform
with dis

pause 1.0

red uniform @talkingmouth "Hey, May!"

if (GetRelationship("May") == "Taster"):
    red @talkingmouth "Ready to serve up a delicious heaping helping of red-hot battles?"

    may @talkingmouth "Absolutely. And this one should actually be edible."
    may @sad "...Ah, sorry about those spring rolls I made, by the way. I really appreciate you taste-testing them."

    red @happy "Hey, I said I would. And they didn't make me absolutely want to die."

    redmind @thinking "More like I just thought I was going to die..."

    may @talkingmouth "Well, failed experiments notwithstanding, I'm pretty sure I know how to execute this battle correctly! Let's go!"

else:
    red @happy "Ready to battle?"

    may @angrybrow happymouth "Absolutely! But I hope you like cold dishes, because that's what I'm serving!"

    pause 1.0

    red @confused "Cold dishes...? What, like sherbert? Or revenge?"

    if (WonBattle("BrendanMay1")):
        may @angrybrow happymouth "Yeah! You defeated my boyfriend and I before, so I'm ready to take you down for that!"

        may @angrybrow happymouth "Prepare yourself for a loving girlfriend's fury!"

        pause 1.0

        redmind @thonk "No, seriously, who {i}says{/i} that?"

    else:
        may @surprised "Oh! Right... that's revenge. I think I was thinking of defeat. Like... defeat is a dish best served cold."

        red @talkingmouth "I'm pretty sure that's not the phrase."

        may @angrybrow happymouth "You're one to talk, Mr. malaphor factory!"


python:
    trainer1 = Trainer("red", TrainerType.Player, playerparty, number=2)
    trainer2 = MakeTrainer("May", number = 2)

call Battle([trainer1, trainer2], uniforms=[True, True]) from _call_Battle_51
$ battlehistory["May1"]  = _return

$ HealParty()

stop music fadeout 1.0

hide alder
hide bruno

pause 1.0

show alder norm at centerside 
show bruno think at leftside
show may uniform at rightside
with dis

$ renpy.music.queue("Audio/Music/Gym_Loop.ogg", channel='music', loop=True, fadein=1.25, tight=None)
    
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

hide blank2

if (WonBattle("May1")):
    may @sad "Oh, boo. I really thought I could do that one with my new Heracross..."
    $ ValueChange("May", 3, 0.75)
else:
    may @talkingmouth "Yes! Instructor Alder, did you see that?"

alder @happy2 "That was some good battling, you two."

may @talkingmouth "Instructor Alder, can I ask you a question?"

alder @norm2 "Of course. That's what I'm here for."

may @happy "I really, {i}really{/i} want a Volcarona. Ever since the first day you brought yours out in class."

alder @spunky2 "Oh, you want her?"

may @surprised "R-really?"

alder @happy2 "Nah, nah. Sorry, just kidding."

may @talkingmouth "Oh, that makes more sense. Okay. I just wanted to know if you knew where I could get one."

alder @sad2 "Hm... well, this particular one came from an egg my {i}first{/i} Volcarona laid."

alder @norm4 "You'll definitely want to get a Larvesta. No offense, but I don't think anybody, save a Champion, should try to wrangle a Volcarona without a lot of trust built up. And the best way to do that is to raise it from an egg."

may @closedbrow sadmouth "Okay, okay... And this 'Larvesta,' I'm guessing it's Volcarona's pre-evolution?"

alder @norm2 "Right."

may @closedbrow talking2mouth "So where could I get a Larvesta egg?"

alder @sad "Hm{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}"

alder @spunky2 "Tell you what. Springsday's tomorrow, and that means the big Kobukan egg hunt is happening. I'll let you know that there'll be a Larvesta egg somewhere out there."

may @surprised "Really?"

alder @happy2 "Yep. And you'll know it's a Larvesta egg because it's very warm, and much bigger than the others. In fact, ancient Unovans used to keep Larvesta eggs in their houses, to warm them."

may @happy "Thanks, Sir!"

hide may with dis

alder @norm2 "Well, if I'm giving out hints, would you like any?"

menu:
    "What's the best way to gather the most eggs?":
        alder @norm3 "Hm... just ignoring the other hunters and grabbing every egg you see, mostly. It's meant to be a fun community thing, but you can blow off the other hunters, if you want."

    "What kind of Pokémon are in the eggs?":
        alder @norm2 "Just baby Pokémon, that I know of. The kind of baby Pokémon that normally require incenses to get. These ones were bred in Paldea, though, so no incense required."

    "How can I tell what's in the eggs?":
        alder @norm2 "Oh, there's lots of different ways. Texture, weight, size, patterns. If you keep an eye on the egg's details, you should be able to figure out the Pokémon--or at least its type--pretty easily."

red @talkingmouth "Thanks for the advice, Sir. I'll take it to heart."

jump lunchtransition