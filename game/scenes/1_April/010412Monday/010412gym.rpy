label gym010412:

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

alder norm @norm2 "[first_name]. Let's have a quick chat."

redmind uniform @thinking "Again? I thought I was doing alright..."

red @talkingmouth "Yes, Sir?"

alder @norm2 "Just a quick question. Pardon me for forgetting, but you said you wanted to be a Champion one day, right? 'Like you,' I think you said."

red @happy "Yes, Sir!"

alder @spunky2 "That's great, kid, great. Well, I just thought you might appreciate some feedback."
alder @norm2 "Your Pokémon are learning now, which is a massive improvement. But you're going to want to work on yourself, too."

red @closedeyes talking2mouth "Yeah, I've been noticing that I seem to be what's holding my Pokémon back... they're growing faster than I am."

alder @norm2 "Yes, but that's just to be expected. Pokémon don't live as long as us, so they have to learn faster than us."
alder @happy2 "Anyway! I just want to recommend that you study a bit outside of classes."

red @sadeyes sadeyebrows happymouth "Jeez... Sir, I've been so busy. I'm not sure when I'd even be able to find the time..."

alder @sad2 "Hmm... yes, that makes sense. Kobukan does somewhat rush you through, doesn't it?"
alder @spunky2 "Well, if you're having trouble finding time to study, the best I can do is recommend that you take some time during your free time--{color=#0048ff}lunch or after school{/color}--to study."
alder @norm2 "See if you can get a friend to help you, too. Studying alone is boring, and actually isn't as effective as studying with someone."
alder @happy2 "Just temper your expectations. Studying with fellow students is necessary, and useful, but it isn't as effective as being taught directly by an instructor or Professor."
alder @spunky2 "...Though, if it was, I'd be out of a job!"

red @happy "Alright, Sir! I'll do that. Thank you."

alder happy @happy2 "Hey, it's what I'm paid to do! Now, how about a battle? Bruno, do you have a partner picked out?"

bruno norm @norm2 "Yes. Come here."

hide alder
hide bruno 
with dis

show rosa uniform with dis

red @happy "Oh, hey, Rosa!"

$ firstletter = first_name[0]
rosa @happy "Hiya, [first_name]! First time we've battled against each other, right?"

show rosa:
    xpos 0.5 zoom 1.0 ypos 1.0
    ease 0.75 xpos 0.75 zoom 0.8
    ease 0.2 ypos 0.9
    ease 0.2 ypos 1.0
    ease 0.2 ypos 0.9
    ease 0.2 ypos 1.0
    ease 1.0 xpos 0.25
    ease 0.2 ypos 0.9
    ease 0.2 ypos 1.0
    ease 0.2 ypos 0.9
    ease 0.2 ypos 1.0
    ease 0.75 xpos 0.5 zoom 1.0

red @happy "Yeah, I think so! I'm looking forward to{w=0.5}{nw}"
extend @confusedeyebrows talking2mouth "-- what are you doing?"
rosa sweat happybrow @happymouth "Oh, I'm just, uh, setting up a camera. It's actually in my contract that I have to record {i}every{/i} time I battle. Could make good footage for future films."
red @confusedeyebrows talking2mouth "In your contract? What, did you have to sign a contract to come here?"
rosa @happymouth "That's under NDA, so, legally, no!"
red @closedbrow talking2mouth "Man, being an actress sounds complicated. And you're a trainer on top of that?"
rosa -sweat angrybrow @happymouth "Well, that's the role I'm in right now. So you better play your part!"
red @angrybrow happymouth "Oh, believe me, I will. I'll be the dark horse in this performance!"
rosa happymouth "That's what I like to hear!"

pause 1.0

show blank
pause 0.1
hide blank

rosa @talkingmouth "Lights!"

show blank
pause 0.1
hide blank

rosa @talkingmouth "Camera!"

show blank
pause 0.1
hide blank

rosa @talkingmouth "Action!"

$ HealParty()
$ trainer1 = Trainer("red", TrainerType.Player, playerparty)
$ trainer2 = Trainer("rosa", TrainerType.Enemy, [Pokemon(25, level=7, gender=Genders.Female, moves=[GetMove("Tail Whip"), GetMove("Growl"), GetMove("Quick Attack"), GetMove("Thunder Wave")], ability="Static")])#Pikachu

call Battle([trainer1, trainer2], uniforms=[True, True]) from _call_Battle_12 
$ battlehistory["Rosa1"]  = _return

$ HealParty()

stop music fadeout 1.0

hide alder
hide bruno

pause 1.0

show alder norm at centerside with dis
show bruno think at leftside with dis
show rosa uniform at rightside with dis

$ renpy.music.queue("Audio/Music/Gym_Loop.ogg", channel='music', loop=True, fadein=1.25, tight=None)
    
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

hide blank2

if (WonBattle("Rosa1")):
    rosa @happy "Hey, that was great footage! Thanks for that."

    $ ValueChange("Rosa", 3, 0.75)

else:
    rosa @sadbrow frownmouth "Aw... that footage wasn't very good."

    rosa @surprised "Oh, but not 'cause of you! I just wasn't feeling it. You were great!"

red uniform @happy "Thanks! I was pretty surprised to see that you had a Pikachu. I have one as well, actually. I can't bring him out while school's in session, though, since he won't go in his ball."

rosa @happy "Oh, really? That's weird, but it's a good gimmick! Audiences love those." 

show alder surprisedbrow frownmouth
show bruno surprisedbrow frownmouth 
with dis

rosa @happy "I got this sweetie when I was touring Alola to promote {i}Hot, Wet Bikini Summer{/i}."

pause 2.0

redmind @thinking "I'm just going to skip that."

show alder norm
show bruno norm 
with dis

red @closedbrow talking2mouth "So your Pikachu isn't your school-assigned starter?"

rosa @talkingmouth "Nope. Actually, I didn't get one of those. It's part of my contract that I can only use agency-approved Pokémon. So they have to be marketable, you know? Like, imagine if I ended up with... I dunno... a Blipbug!"

red @closedbrow talking2mouth "...You did come here to learn how to be a Pokémon trainer, right? Not to promote a film?"

rosa @sadbrow happymouth "...Yeah. But, y'know, limitations of showbiz..."

jump lunchtransition