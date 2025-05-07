label gym010413:

  

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

alder @talkingmouth "And that's the end of the lecture!"

pause 2.0

alder norm @norm2 "[first_name]. Eyes up here."

red uniform @surprised "Huh?! Oh, uh, yes, Sir?"

alder @spunky2 "You seem distracted."

red @closedbrow talking2mouth "Very much so, Sir."

alder @norm2 "Well, as long as you're aware. You've been paying attention well in  all other classes, so I'll let this slide."

red @closedeyes talking2mouth "Thank you."

alder happy @happy2 "Just don't doze off again. You're paying too much to be here for that."

redmind @sadeyes sadeyebrows "I'm not paying to be here at all..."

bruno norm @norm2 "Whitney. Come here."

hide alder
hide bruno 
with dis

show whitney uniform with dis

red @happy "Oh, hey, Whitney! What's up?"

whitney @happy "Oh, gosh, I'm going to fight {i}you{/i}? But you're so strong, and so good at battling... I don't know if I even have a chance!"

red @confusedeyebrows talking2mouth "Uh... okay."

whitney @happy "Go easy on me! I'm very delicate!"

$ trainer1 = Trainer("red", TrainerType.Player, playerparty)
$ trainer2 = MakeTrainer("Whitney")

call Battle([trainer1, trainer2], uniforms=[True, True]) from _call_Battle_15
$ RecordBattle("Whitney1")

$ HealParty()

stop music fadeout 1.0

hide alder
hide bruno

pause 1.0

show alder norm at centerside with dis
show bruno think at leftside with dis

if (WonBattle("Whitney1")):
    show whitney sadbrow frownmouth uniform at rightside with dis
else:
    show whitney uniform at rightside with dis

$ renpy.music.queue("Audio/Music/Gym_Loop.ogg", channel='music', loop=True, fadein=1.25, tight=None)
    
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

hide blank2

if (WonBattle("Whitney1")):
    red uniform @surprised "Holy cow!"
    red @happy "...Heh. Nate would like that."

    whitney sad @tears "...Wha... wha... what...? My M-Miltank..."

    red @surprised "Oh. Um... Whitney...?"

    whitney closedbrow sadmouth cry "Waaaaaah!"

    show whitney:
        ease 0.25 xpos 1.5

    show alder surprisedbrow frownmouth with dis
    show bruno surprisedbrow frownmouth with dis

    pause 2.0

    hide whitney

    alder surprised2 "...Well, that's a new one." 

    pause 1.0

    alder sad @sad2 "C'mon, Bruno, let's go talk to her. [first_name], you come, too."

    pause 2.0

    show whitney tears uniform sadbrow frownmouth at rightside with dis

    pause 1.0

    whitney "{i}Sniff.{/i}"

    bruno norm @angry2 "That was dishonorable."

    whitney @sad cry "Waaaah..."

    alder sad @sad2 "Tactful, Bruno."

    pause 1.0

    alder sad @sad2 "Listen, Whitney. I know you've won every battle you've had in this class so far. But you can't win all of them. {i}No-one{/i} can."

    whitney @sadmouth "B-but... but I {i}really{/i} wanted to! I tried so hard! And so did li'l Treble and tough Milty!"

    alder @angry2 "And how do you think Treble and Milty feel, seeing their trainer crying after they gave their all?"
    alder @sad2 "When you lose, smile. And when you win, then you can cry."
    alder @norm2 "There's nothing wrong with being true to your emotions, but you need to let your Pokémon know that you're proud of them, and you need to let your opponent know you respect them."
    alder -sad @happy2 "There's no shame in a battle well lost. Your efforts are only wasted if you fail to appreciate the outcome."

    red @talkingmouth "...Okay..."

    red @happy "Might not be my place to say this, but you're probably the toughest opponent I've fought all year. And [blue_name] ambushed me with a level 18 Pidgeotto."

    blue uniform angry "Would you give that a rest?!"

    pause 1.0

    whitney @happymouth "Okay. Okay, I won't cry anymore. {i}Sniff.{/i} Sorry, [first_name]. You did really well. I shouldn't be upset."

    red @talkingmouth "It's alright. I know being defeated is disappointing, especially if you're not used to it. And, from how strong you are, I can tell you're {i}definitely{/i} not used to it."

    whitney "Mmm."

    whitney -frownmouth -sadbrow -tears @happy "Hee hee. Thanks, [first_name]. You're pretty cool."

    $ ValueChange("Whitney", 3, 0.75)

else:
    red uniform @surprised "What the hell?!"

    whitney @happy "Sorrr-ry!~ I might've lied a little bit about how strong I am."

    redmind @thinking "Even with all the progress my team has made, it seems like all my classmates are way further than me..."

    whitney @talking2mouth "Aw, don't worry about it. You did really well. And if I hadn't taken you by surprise, I might've lost."

    pause 2.0

    bruno norm @angry2 "That was dishonorable."

    whitney @surprised "Huh? But shouldn't I take every advantage I can get?"

    bruno @think2 "There are some advantages that cause you to lose more than you gain."

    alder @spunky2 "Ah... this is going to be a bit awkward, but I actually think hiding your power is a perfectly fine strategy." 
    alder @norm2 "If you mislead your opponent a bit, well, it's fine if you do that {i}during{/i} the battle, so why not before? I do it all the time."

    bruno @norm2 "It's dishonorable when you do it, too."

    alder @happy2 "Hah! Bruno and I've been good friends for many years, but we don't agree on everything."

    alder @norm2 "Since we can't agree what we should be teaching here, I hope the lesson you learn is that everyone has different ideas of what a 'good victory,' or a 'good loss' are."

    whitney frownmouth @talking2mouth "Oh... okay."

    red @happy "Well, whether it was a good win, or a good loss, it was fun. Never had so much fun getting my face stomped in by a cow."

alder happy2 "That's the spirit."

hide alder 
hide bruno
with dis

show whitney:
    ease 0.5 xpos 0.5

whitney -frownmouth @happy "You know, most people can't give me a really tough fight. And some don't even try. So it's cool that you went all-out like that."

red @talkingmouth "Oh, yeah? How come?"

whitney @talking2mouth "Don't mean to brag or nothin', but I'm kinda popular! Not, like, {i}Rosa{/i} popular, but well-known enough. And I guess people think beating me would make them look bad?"

if (WonBattle("Whitney1")):
    redmind @thinking "Maybe they were worried you'd burst into tears?"
else:
    redmind @thinking "Are you sure that they lost on purpose? That cow of yours is crazy."

red @surprised "Wait! So, uh, you know a lot of people, right?"

whitney @talking2mouth "Pretty much, yeah."

red @closedbrow talking2mouth "Weird question, but there's a student I want to talk with, and she doesn't speak. Do you know anyone in this school who knows sign language?"

whitney @surprised "Do I? Totally. Which region's?"

red @surprised "Uh... I have no idea."

whitney @closedbrow talkingmouth "Well, if you want to head to lunch together, maybe we can find this girl of yours, and I might recognize her signs."

red @closedbrow talking2mouth "You have experience with sign language?"

whitney @talking2mouth "Yeah, I even know the Johto variant."

red @surprised "No shit? How'd that happen?"

whitney @happy "Wahahaha! I'm a woman of {i}many{/i} talents!"

pause 2.0

red @confusedeyebrows talking2mouth "No, but for real."

whitney @happy "Oh, a girlfriend of mine in Johto was deaf-mute. We basically grew up together, so I learned it pretty young."

red @talkingmouth "Huh. Was that friend named Bianca?"

whitney @happy "{i}Girl{/i}friend. Like 'GF' girlfriend."

red @surprised "Oh. Oh!"

whitney @closedbrow talkingmouth "Anyway, Bianca? Like that blonde who hangs out around the Unovans? Nah, my girlfriend was blue-haired. And her name was... well, it wasn't Bianca."

red @talkingmouth "Huh. Past tense, I'm noticing."

whitney @closedbrow talking2mouth "All good things come to an end. {i}Sigh...{/i}"

pause 2.0

red @happy "So, you and Flannery...?"

whitney @happy "Hah! Nooooo. She's a {i}project.{/i}"

red @happy "I won't tell her that."

whitney @sadbrow talking2mouth "Thank you."

show alder at leftside 
show bruno at rightside
with dis

jump lunchtransition