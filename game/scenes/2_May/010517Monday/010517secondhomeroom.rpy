label secondhomeroom010517:

scene blank2

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade

narrator "You've only just stepped into the class, when--"

stop music fadeout 1.5
queue music "audio/music/celebi_start.ogg" noloop
queue music "audio/music/celebi_loop.ogg"

$ PlaySound("Door_Slam.ogg")

show kris angrybrow angrymouth with dis

kris @talking2mouth "Alright, that's enough talking! Sit down! We have an {i}incredible{/i} amount of work to do, and a ridiculously short amount of time to do it!"

red uniform @surprised "{size=30}Woah. What's gotten her so agitated?{/size}"

dawn uniform @sadbrow talkingmouth "{size=30}I heard that, between homerooms, she confronted Professor Oak, and he... um... was less than helpful.{/size}"

kris @talking2mouth "Midterms are coming up faster than anyone can guess, and the way things are going right now, it would be a {i}miracle{/i} if you managed to pass." 
kris @closedbrow talking2mouth"Your knowledge of anything outside of whatever Doctor Oak felt like lecturing about on a particular day is practically nonexistent."

narrator "You notice there's a significant curtness to the way Professor Cherry says 'Doctor Oak' that was not present in the morning."

redmind @closedbrow frownmouth "Still, I know he wouldn't intentionally blow her off or anything like that... he probably just didn't realize how big an issue this was."

kris @talking2mouth "We've got a test that we need to take today. And after this we need to have a serious discussion about all your academic futures."

pause 1.0

kris @sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."

kris @sadbrow talkingmouth "Sorry. I shouldn't say that right before a test, should I? That's probably not very comforting."
kris -angrybrow @talkingmouth "The test itself should be easy enough, especially compared to the sorts of exams you've taken recently. Just do your best, and think carefully about the effects of moves and abilities that modify them, and how they interact."
#kris @talkingmouth "[bluecolor]Also, remember the effect of blinding fog: If a move {i}can{/i} miss, it will.{/color}"

pause 0.5

kris @talkingmouth "Remember that [bluecolor]this is a graded test.{/color} Take it seriously."
kris @sad "You... {i}really{/i} can't afford not to."

python:
    trainer1 = Trainer("red", TrainerType.Player, [
        Pokemon("Torterra", level=60, moves = [GetMove("Leaf Storm"), GetMove("Earthquake"), GetMove("Stone Edge"), GetMove("Giga Drain")], ivs=[0, 0, 0, 0, 0, 0], ability = "Overgrow"),
        Pokemon("Sableye", level=60, moves = [GetMove("Recover"), GetMove("Will-O-Wisp"), GetMove("Knock Off"), GetMove("Quash")], ivs=[0, 0, 0, 0, 0, 0], ability = "Stall"),
        Pokemon("Maractus", level=60, moves = [GetMove("Sucker Punch"), GetMove("Solar Beam"), GetMove("After You"), GetMove("Worry Seed")], ivs=[0, 0, 0, 0, 0, 0], ability = "Storm Drain")
    ], number=3)

    trainer2 = Trainer("kris", TrainerType.Enemy, [
        Pokemon("Quagsire", level=60, moves = [GetMove("Earthquake")], ivs=[0, 0, 0, 0, 0, 0], ability = "Unaware")
    ])

    trainer1.GetTeam()[0].Health = 1
    trainer1.GetTeam()[1].Health = 1
    trainer1.GetTeam()[2].Health = 1
    trainer1.GetTeam()[2].ChangeStats(Stats.Speed, 1)
    trainer2.GetTeam()[0].ChangeStats(Stats.Speed, 2)

call Battle([trainer1, trainer2], gainexp=False, healParty=False, clearstats=False, uniforms=[True, False], lockbag=True) from _call_Battle_144
$ battlehistory["Kris1"] = _return

$ renpy.transition(dissolve)
show screen currentdate
show kris 
with dis

queue music "audio/music/celebi_start.ogg" noloop
queue music "audio/music/celebi_loop.ogg"

kris @talkingmouth "...Okay. Okay, this is about what I expected." 

if (WonBattle("Kris1")):
    $ ValueChange("Kris", 3)

    kris @closedbrow talkingmouth "[first_name], nicely done. You too, Blue. Whitney, that was a very creative answer. Please meet with me after class to discuss it more."

else:
    kris @closedbrow talkingmouth "Hilbert, excellent work, no comments. You too, Blue. Whitney, that was a very creative answer. Please meet with me after class to discuss it more."

whitney uniform surprisedbrow lightblush frownmouth "{size=30}{w=0.5}.{w=0.5}.{w=0.5}.Ekk.{/size}"

redmind @confusedeyebrows frownmouth "...Seriously, what's up with her?"

kris @talkingmouth "I'd like to spend a little more time on these quizzes, but, frankly, we need to move {i}on.{/i}"

kris @talkingmouth closedbrow "Tomorrow morning, I want everyone to come to class early. Be prepared, and in class, by 7:15."

$ PlaySound("class_groan.ogg", "crowd2")

pause 0.75

kris @angrybrow talking2mouth "Don't give me that. You {i}need{/i} it. We're going to take a class trip out to Argent Mountain."

redmind @surprisedbrow frownmouth "Hm? Suddenly, I'm a lot more interested."

kris @talkingmouth "A large part of the curriculum is capturing Pokémon in hostile environments. According to Doctor Oak, he hasn't introduced you to... {i}any{/i} wild areas. Is that correct?"

blue uniform @glanceeyes wistfulmouth "...Yeah."

hilbert uniform @sadbrow talkingmouth "We're going to be hiking up a mountain at {i}7:15{/i}? In the morning?"

kris @talkingmouth "We're not going to be hiking up a mountain. I've rented out the school's {i}entire{/i} Ride Cyclizar fleet."

leaf uniform @surprised "What?!"

kris @talking2mouth "I want you all to use that time battling and capturing. Field experience is valuable, and it sounds like you haven't gotten {i}any{/i} school-sanctioned experience in your homeroom yet."
kris @talking2mouth "Argent Mountain has a lot of Ice and Rock-types. Anyone specializing in those types, now might be a good time to stock up on Poké Balls."

pause 1.0

kris @closedbrow talkingmouth "Also... I don't like making this request, but I'm paying for this trip out of my own pocket. If you happen to have your own Cyclizar, or even multiple Cyclizar, you'd be willing to let me borrow..."
kris @talkingmouth "Well, I can't provide any extra credit at this time, but I'll be extremely thankful, and if you ever want me to write a letter of recommendation for you, I'll keep that in mind."

leaf @talking2mouth "Sure, I can go out to the fields and catch a few Cyclizar today. Question, though. Since we can only have, like, six Pokémon on us at once, and one of them needs to be our starter, can we just, like keep the Poké Balls in a sack?"

kris @happy "Oh, no need for that. Tomorrow morning, you can just use the PC in this room to swap out your Pokémon."

pause 1.0

narrator "There's another deafening silence."

show kris surprisedbrow frownmouth with dis

flannery uniform @sadbrow talking2mouth "Um, Doctor? There's no PC in this room."

kris @talkingmouth "What? No, that can't be right, there's..."

show kris:
    ease 0.5 xzoom -1
    pause 0.5
    ease 0.5 xzoom 1

pause 1.5

kris surprisedbrow angrymouth @talking2mouth "There's no PC in this room."

pause 0.5

kris sadbrow @talkingmouth "I'm afraid to ask, but how have you been swapping out members of your parties?"

pause 0.5

show kris surprisedbrow frownmouth with dis

red @sadbrow talking2mouth "We, uh... go to the city."

kris @talkingmouth "Th-the city. You walk... about half an hour... to the city? To use the Pokécenter there?"

leaf uniform @happy "Yeeeep. Was there another option?"

pause 1.0

kris -surprisedbrow -frownmouth -surprised sadbrow angrymouth @closedbrow talkingmouth "Every single homeroom is equipped with a PC system."

pause 1.0

blue uniform @angry "Obviously not."

kris @sadbrow talkingmouth "Okay, well, you know, it's good that this is coming out now, as opposed to, I don't know, {i}two{/i} months in."

pause 0.5

kris @closedbrow talkingmouth "I don't understand. When it came time for the practical tests that used your Pokémon, how did you have the right Pokémon on hand? Did you just have to go to the city ahead of time?"

pause 1.0

kris surprisedbrow frownmouth @surprised "Oh no."

blue @closedbrow talkingmouth "Look, Gramps forgot a couple minor things! He forgot my own name, and I didn't {i}whine{/i} this much. Can we stop {i}harping{/i} on him?!"

kris -surprisedbrow -frownmouth -surprised @closedbrow talking2mouth "Okay."
kris @talkingmouth "You're right. Let's just look forward, and see how we can improve from where we are now."

pause 0.5

kris @talkingmouth "Any student who wants to use the PC system in my homeroom, 1-C, is free to."
kris @happy "[bluecolor]Just go to the academy building in your free time.{/color} Speaking of which, I believe the bell is just about to ring..."

pause 1.0

kris @talkingmouth "Remember, everyone, early tomorrow. I can't force you to come, and I won't be taking attendance, but this is honestly the best I can do for you right now."
kris @closedbrow talkingmouth "Also, if you have any Cyclizar on hand... I'll be really grateful. The more the better, of course, though I wouldn't ask you to catch any more than five."

pause 1.0

kris @happy "Alright. Thanks for being patient with my freakouts today. I think we're in a good spot to turn this around, though."

$ PlaySound("BellChime.ogg")

kris @talkingmouth "I'll see you tomorrow. Bright and early!"

hide kris with dis

pause 1.0

show blue uniform frownmouth wistfulbrow with dis:
    xpos 0.6 xzoom -1

pause 1.0

leaf uniform @frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

pause 1.0

show leaf uniform:
    xzoom -1 xpos 0.33

leaf @happy "Hey, Blue."

blue @surprisedeyebrows talking2mouth "Hm?"
blue @closedbrow talkingmouth "Oh, hi."

leaf @talking2mouth "You thinking about going to see your grandpa now? [first_name] told me about your Eevee."

pause 1.0

show leaf surprisedbrow frownmouth with dis

blue @talkingmouth "...I... maybe. I don't know."

leaf @talking2mouth "Really? Why wouldn't you?"

blue @talkingmouth "...I don't know. All that shit we learned in class today. I didn't think he was... I mean, that makes him look bad. Really bad."
blue @closedbrow talkingmouth "...Whatever. I'll talk to him eventually, obviously. I don't need to rush him."

pause 1.0

leaf sadbrow @talking2mouth "...Alright. Well, I'm going out to the fields to see if I can catch some Cyclizar for Professor Cherry. If you want to join--"

blue @closedbrow talkingmouth "Nah. We're not even getting extra credit. No point to it."

leaf @talking2mouth "...Alright."

hide leaf with dis

pause 0.5

show blue glancebrow frownmouth with dis

pause 1.0

hide blue with dis

$ removestudents = { "Leaf", "Blue", "Dawn" }

call freeroam from _call_freeroam_24

$ removestudents = set()

stop music fadeout 1.5

show screen songsplash("Pallet Town", "Zame")
$ renpy.music.queue("Audio/Music/palletpiano.ogg", channel='music', loop=True, tight=None)

scene suitenight 
show yellow neutralbraidfront 
with splitfade

red @happy "Hey, Yell'."

yellow @talkingmouth "Hello."

pause 0.5

yellow @talkingmouth "Um... do you know where Blue is?"

red @talkingmouth "Hm? I thought he'd be here with you."

yellow @closedbrow talkingmouth "It {i}is{/i} odd. He never misses game night."

red @talkingmouth "We could pull out a board game 'til he gets here."

show ethan:
    xpos 0.33
with dis

show yellow:
    xpos 0.5
    ease 0.5 xpos 0.66

ethan @talkingmouth "We gaming? Count up one vote for Monopoly. I need to get my mind off homeroom today."
ethan @talkingmouth "For real, though, I've got {i}tons{/i} of boardgames in my bedroom. Anything you want."

show ethan:
    xpos 0.33
    ease 0.5 xpos 0.25

show yellow:
    xpos 0.66
    ease 0.5 xpos 0.5

show leaf:
    xpos 0.75
with dis

leaf @talking2mouth "Woah, wait, if we're playing a board game, then it's gotta be the Pokémon Master Trainer boardgame!"

ethan @happy "You battle-holic! That's basically just our daily lives, anyway!"

leaf @talking2mouth "It's something I {i}actually{/i} enjoy. I'm not just picking it ironically."

ethan @sad2eyes sadeyebrows talkingmouth "Fair enough."

pause 0.5

show yellow surprisedbrow frownmouth fullblush
show leaf surprisedbrow frownmouth
with dis

ethan @talkingmouth "Hey, cutie. We haven't heard from you. What do {i}you{/i} want to play?"

pause 1.0

leaf @talking2mouth "What the fuck?"

ethan @confusedbrow talkingmouth "C'mon. That, was, like, the most basic level of flirting."

yellow @talkingmouth "Y-y-you're flirting? With me?"

ethan @closedbrow talkingmouth "Damn. If you didn't get that, maybe I really {i}do{/i} suck at flirting."

show yellow:
    xpos 0.5
    ease 0.5 xpos 0.75

show leaf:
    xpos 0.75
    ease 0.5 xpos 0.5

leaf -surprisedbrow -frownmouth -surprised angrybrow frownmouth @talking2mouth "Look, I don't know what you're doing here, but you should {i}really{/i} cut it out."

ethan @noshine frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

pause 1.0

ethan closedbrow @talkingmouth "Pfft. Can't believe you took that seriously. Look at you, Yellow, you're redder than a tomato."
ethan -closedbrow @happy "C'mon, it was a joke! Lighten up, guys."

show yellow sadbrow heavyblush -fullblush -frownmouth with dis

leaf -angrybrow -frownmouth @surprised "Oh... that was a joke?"
leaf @happy "Hah... hah! Hahaha! Oh, okay, that was pretty funny, after all!"

ethan @closedbrow sweat talkingmouth "Yeah, see? Not like we need to make a federal issue out of it. Geez. So serious."

ethan @talkingmouth "Anyway, what do you want to play, [first_name]?"

hide blank2

menu:
    "{color=#66b77d}[[Knowledge]{/color} Trivial Pursuit-Trap":
        $ AddEvent("Ethan", "Trivial Pursuit-Trap")
        $ TraitChange("Knowledge")

        ethan @talkingmouth "Oh, that's a good one. Think they removed it from sale, though, but I bet I have a copy in my room..."

    "{color=#60c2f8}[[Wit]{/color} Cards Against Pokémonity":
        $ AddEvent("Ethan", "Cards Against Pokémonity")
        $ TraitChange("Wit")

        ethan @talkingmouth "Heh. I'm going to have to hide my power level, then. Don't want you guys calling the cops."

    "{color=#ff8412}[[Courage]{/color} Krookodile Dentist":
        $ AddEvent("Ethan", "Krookodile Dentist")
        $ TraitChange("Courage")

        ethan @surprised "Oh, geez, when that thing snaps on your fingers, that seriously stings. You're into some hardcore stuff, huh, [first_name]?"

scene blank2
with splitfade

narrator "After a bit of awkward laughter, the four of you sit down and play a game together."
narrator "Eventually, Blue comes back."

yellow neutralbraidfront @surprisedbrow talkingmouth "Oh! Blue. It's late. Um, we didn't want to start {i}Inferno & Logos{/i} without you..."

blue @wistfulmouth wistfulbrow "...Thanks. I'm not in the mood, though. I think I might just go to bed."

narrator "The game wraps up shortly after, and you go back to your room."

call texting from _call_texting_19 

jump day010518