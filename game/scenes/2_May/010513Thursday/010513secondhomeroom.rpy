label secondhomeroom010513:

scene blank2

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom behind blank2

show oakbg behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade

oak @talkingmouth "...so the Shogun created the position of 'Champion', such that, if his political power ever waned, and evil men ever attempted to grasp at power, the inherent goodness of Pokémon would always come to Kanto's defense." 

show hilbert uniform at rightside with dis

hilbert @talkingmouth "Are we seriously meant to believe that Pokémon are {i}pure{/i} good? That seems naive."

oak @talkingmouth "Well, in all of our recorded history, we've no solid proof of a Pokémon willingly performing a cruel act without coercion."

hide hilbert with dis

oak @talkingmouth "That's not to say that Pokémon are harmless, of course. Everyone knows you should never walk out into the tall grass without a Pokémon."
oak @talkingmouth "But, even though Pokémon have been known to rampage, sometimes with disastrous results, a Pokémon under complete control of its mental faculties never attacks without reason."

pause 1.0

oak @talkingmouth ".{w=0.5}.{w=0.5}.{w=0.5}But perhaps that's a level of pedantry that we need not get into right now."
oak @talkingmouth "If a wild Pokémon attacks you, rely on your own Pokémon to defend yourself, not their {i}inherent goodness.{/i} But do keep it in mind."

pause 1.0

oak @talkingmouth "{size=30}Now, let's see...{/size} Ah! Yes, it's about time for our test, isn't it?"

pause 0.5

oak @talkingmouth "This test won't introduce any new concepts. All I ask is that you defeat your opponent." 
oak @talkingmouth "[bluecolor]The opponent Gardevoir only knows Psychic, the opponent Meganium only knows Giga Drain, and the opponent Dugtrio only knows Stomping Tantrum.{/color}" 
oak @talkingmouth "Finally, in this test... [bluecolor]you {i}will{/i} be able to gain experience.{/color} That may be relevant."
oak @talkingmouth "Take out your pencils... and remember, [bluecolor]this is graded!{/color}"

python:
    oldpoisoncap = classstats["Poison"]
    classstats["Poison"] = 100
    skorupiobj = Pokemon("Skorupi", level=40, moves=[GetMove("Cross Poison"), GetMove("Acupressure"), GetMove("Crunch"), GetMove("X-Scissor"),], ivs=[0, 0, 0, 0, 0, 0], ability="Battle Armor", nature=Natures.Adamant)
    skorupiobj.Experience = skorupiobj.CalculateAllExperienceNeededForLevel(41)
    trainer1 = Trainer("red", TrainerType.Player, [skorupiobj], number=3)
    trainer2 = Trainer("oak", TrainerType.Enemy, [
        Pokemon("Gardevoir", level=60, moves=[GetMove("Psychic")], ability="Trace", ivs=[0, 0, 0, 0, 0, 0], nature=Natures.Serious),
        Pokemon("Meganium", level=60, moves=[GetMove("Giga Drain")], ability="Overgrow", ivs=[0, 0, 0, 0, 0, 0], nature=Natures.Serious),
        Pokemon("Dugtrio", level=60, moves=[GetMove("Stomping Tantrum")], ability="Arena Trap", ivs=[0, 0, 0, 0, 0, 0], nature=Natures.Serious)
    ], number=3)
    for mon in trainer2.GetTeam():
        mon.AdjustHealth(10, absolute=True)
        mon.ChangeStats(Stats.Speed, -6, mon)

call Battle([trainer1, trainer2], clearstats=False, healParty=False, uniforms=[True, False], lockbag=True) from _call_Battle_131
$ battlehistory["Oak9"] = _return
$ classstats["Poison"] = oldpoisoncap

$ renpy.transition(dissolve)
show screen currentdate

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

if (WonBattle("Oak9")):
    redmind uniform @happy "Hm... mid-battle evolution, huh? In most regions, trainers are required to stop their Pokemon from evolving mid-battle, at least in official matches, but I guess Kobukan is fine with it."
else:
    redmind uniform @sad "Uh-oh. I think we might be hitting the point where these tests aren't quite as easy as they seemed at the beginning of the year."

    redmind @thinking "Damn, when Advisor Lance said things were about to get harder, he {b}wasn't{/b} kidding."

oak @talkingmouth ".{w=0.5}.{w=0.5}.{w=0.5}"

pause 0.5

oak @talkingmouth "At a glance..."

pause 0.5

oak @talkingmouth "Well, at a glance, actually, it looks like a lot of you are struggling. I thought the concepts were simple enough, but perhaps... hrm."

narrator "Though he's up at the front of the classroom, you can tell Professor Oak looks concerned."

pause 0.5

$ PlaySound("BellChime.ogg")

pause 2.0

oak @talkingmouth "Well, that seems to be the bell. Perhaps I should... perhaps..."

hide oakbg with dis

narrator "Professor Oak seems troubled. You consider going after him, but..."

show leaf uniform:
    xpos 0.33 ypos 1.2 zoom 1.3

leaf @talking2mouth "Hey. Going to battle Raihan?"

show blue uniform:
    xpos 0.66 ypos 1.2 zoom 1.3 

blue @surprised "{i}Raihan?{/i} The Eighth Gym Leader of Galar? Strongest member of the Galarian league aside from Leon?"

red @talkingmouth "Apparently. He showed up in the garden at lunch today. Jumped off a Flygon. Landed on me, actually."

blue @closedbrow talkingmouth "...Getting real sick of random powerful people and things falling out of the sky into your lap."

show leaf surprisedbrow frownmouth with dis

red @closedbrow talking2mouth "Yeah, he was kneeling on my dick. It still hurts."

pause 1.0

blue @talkingmouth "No-one needs to know that."

hide blue with dis

pause 2.0

show leaf -surprisedbrow -frownmouth with dis

red @talkingmouth "So, are-"

show blue uniform with dis:
    xpos 0.66 ypos 1.2 zoom 1.3 

blue @talkingmouth "Where?"

red @confused "Huh?"

blue @talkingmouth "Where are you battling? The Battle Hall?"

red @talking2mouth "Yeah, in a couple minutes."

hide blue with dis

pause 1.0

red @confused "What do you think that was about?"

leaf @talking2mouth "Oh, he probably just wants to watch you battle. Anything to get more information on you, you know."
leaf @talkingmouth "Sometimes I think he wouldn't mind being the second-weakest trainer in the world, as long as you were the weakest."

red @happy "Man, you're right."

pause 0.5

red @talkingmouth "Alright. I'm going to the dorm to get changed, then to the Battle Hall. Want to come with?"

if (rescuedtia):
    leaf @talking2mouth "Sorry, I'm going to meet up with Tia. She's gotten better since her stay in the infirmary, but she's still a bit slow. I'm helping her catch up on her lessons."

    red @happy "Hey, that was nice of you. But shouldn't you be worried about your own academics most? I mean, you skipped class to grab me, then you took Monday off to look for her..."

else:
    leaf @talking2mouth "Sorry, I'm going to meet up with Flan and Whit. We're going to try and work on our Tia Rescue Team strategy."

    red @happy "Hey, that was nice of you. But shouldn't you be worried about your own academics? I mean, you skipped class to grab me, then you took Monday off to look for her..."

red @talkingmouth "Not to mention you're going to start taking Normal classes."
red @confused "Aren't you worried you'll fall behind?"

leaf @talkingmouth "Nah, not really."
leaf happy "Talk to you later!"

hide leaf with dis

pause 0.5

redmind @thinking "...She seems very cavalier about missing school, huh...?"

call clearscreens from _call_clearscreens_161
scene blank2 with splitfade

pause 1.0

$ renpy.music.play("Audio/bigcrowdloop.ogg", channel='crowd', loop=True, fadein=1.5)
$ renpy.music.play("Audio/hall_crowd.ogg", channel='crowd2', loop=True, fadein=1.5)
$ renpy.music.play("Audio/bigcrowdloop.ogg", channel='crowd3', loop=True, fadein=1.5)

pause 2.0

stop music fadeout 1.5

$ renpy.music.queue("Audio/Music/DragonDenStart_B.ogg", channel='music', loop=False, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/DragonDenLoop.ogg", channel='music', loop=True, fadein=0.0, tight=None)

redmind @thinking "Hm? What's that noise?"

scene stadium_empty
show screen currentdate
show raihan angrybrow:
    xpos 0.66
show lisia incognito incogbrow incogshades:
    xpos 0.33
with splitfade

pause 1.0

narrator "You walk into the Battle Hall. Though still largely empty, a small crowd has gathered around Raihan. He's busy flexing and bragging to the crowd."
narrator "A familiar-looking woman stands at the front of the crowd, her confidence in front of this famous trainer at odds with her unassuming clothing and posture."

raihan @talkingmouth "{size=22}...{/size}{size=25}ready{/size} {size=28}to{/size} {size=31}see{/size} me {i}roar?!{/i}"

show lisia happyincogbrow happymouth with dis:
    xpos 0.33

Character("Unassuming Lass") "\"Hell yeah!\""

show lisia incogbrow -happymouth with dis:
    xpos 0.33

raihan -angrybrow @talkingmouth "Well, you're in luck! Because in just a few minutes, you're going to get to see how the great and mighty Raihan battles!"

show lisia talkingmouth with dis:
    xpos 0.33

Character("Unassuming Lass") "\"That's {i}so{/i} cool. I'm a big fan of yours! But I read {i}all{/i} your RotoPhoto stories, and you didn't say anything about coming here?\""

show lisia -talkingmouth with dis:
    xpos 0.33

raihan @closedbrow talking2mouth "Well, I gotta leave {i}some{/i} things as surprises for the fans, don't I?"
raihan @happy "Besides, I'm not one of those obnoxious influencers who want all their fans to know where they are {i}100%%{/i} of the time."
raihan @angrybrow happymouth "I'd settle for just 95%%!"

show lisia sadincogbrow talking2mouth with dis:
    xpos 0.33

Character("Unassuming Lass") "\"Wow, really? I... some people I know... try to get away from their fans.\""

show lisia incogbrow -talking2mouth with dis:
    xpos 0.33

raihan @surprised "Huh?"
raihan @closedbrow sadmouth "Man, why would I do that? If they care about me enough to want to know where I am or what I'm doing, then of course I'm going to be open to them."
raihan @happy "Besides, when I finally beat Leon, I want the whole world to be watching! That means you gotta start gathering the fans early!"

show lisia happyincogbrow talkingmouth with dis:
    xpos 0.33

Character("Unassuming Lass") "\"That's a very cool way of thinking about it. I guess there really is more to you than an eight-pack and muscle cars, huh, Raihan?\""

show lisia incogbrow -talkingmouth with dis:
    xpos 0.33

raihan @happybrow talkingmouth "Of course! I own {i}Pride's Pariah{/i}, you know."

pause 1.0

raihan @closedbrow talkingmouth "I mean, I haven't read it, but I {i}do{/i} have it."

pause 1.0

raihan @happy "It's a signed copy, too."

pause 2.0

red @talkingmouth "Hey!"

raihan @happy "Hey, [last_name]! Pikachu-wielder. Ready to get things started?"

red @talkingmouth "Shouldn't we wait for Dean Drayden to arrive?"

raihan @surprisedbrow sadmouth "Oh, yeah, I guess so."

red @talkingmouth "Who's your friend?"

raihan @happy "Oh, right, I don't think I got your name. Lay it on me."

show lisia talkingmouth with dis:
    xpos 0.33

Character("Unassuming Lass") "\"Liz.\""

show lisia -talkingmouth with dis:
    xpos 0.33

red @talkingmouth "Nice to meet you."

pause 1.0

redmind @thinking "Okay, it's extremely obvious that this is Lisia, but if she doesn't want to be recognized outside of her role as announcer, I'm not going to blow this for her."

lisia @talkingmouth "Oh... wait, Raihan, you said {i}Pikachu-wielder{/i}, right? I thought I recognized you!"
lisia @happyincogbrow talkingmouth "You're the student who fought Dawn last Friday, right?"

red @talkingmouth "Yup."
redmind @thinking "And you're the one who announced it."

lisia @talkingmouth "I'm in the Coordinator Club. Dawn's been talking about you a lot. Fair warning, she might try to recruit you."

red @happy "Well, I'm a bit busy with the Kobukan Battle Team, but I might drop in."
red @winkeyes talkingmouth "I heard the new instructor for the Coordinator Club is pretty great."

lisia @surprisedincogbrow talkingmouth "Oh, you..."
lisia @xdincogbrow talkingmouth "Ah, don't do that! If you know who I am, just say it!"

red @sadbrow talkingmouth "Sorry, Liz. That's not my job."

raihan @sadbrow talkingmouth "Feel like I'm... missing something..."

red @happy "Nah, it's nothing serious. Let's just... hm?"

show drayden with dis:
    xpos -0.2
    ease 0.5 xpos 0.25

show lisia:
    xpos 0.33
    ease 0.5 xpos 0.5

show raihan:
    xpos 0.66
    ease 0.5 xpos 0.75

pause 1.0

drayden "Hello."
drayden @surprisedbrow "...Seems you've gathered a bit of an audience already."

raihan @angrybrow happymouth "Yeah, I just seem to gather fans wherever I go. We're all, alone, like little grains of sand, but my fans have built these sands up into a mighty gale... and the desert wind'll blow down anyone who stands in my way!"

$ PlaySound("crowd_cheer.ogg")

hide lisia with dis

drayden @closedbrow "Hm. This may prove... complicated."

pause 1.0

redmind @thinking "That was actually pretty cunning. By getting the crowd hyped up and on his side, Drayden will have a harder time rejecting him."
redmind @thinking "I guess, as an influencer, he knows the power of popular opinion."

red @talkingmouth "Pretty sneaky."

raihan @talking2mouth "The desert's got all kinds of tricks."

drayden @surprisedeyebrows "Forgive me for speaking out of turn, but do you not come from Hammerlocke? A city surrounded by lush green fields, swampy marshland, and an average rainfall of 23 inches per year?" 
drayden @closedeyes surprisedeyebrows "Your numerous references to the desert seem out-of-place."

raihan @sad "It's... a branding thing."

drayden @closedbrow "Hrm. I suppose I still do not understand."

pause 0.5

drayden "Students. If you are not a part of this battle, please make your way to the bleachers."

stop music channel "crowd" fadeout 1.5
stop music channel "crowd2" fadeout 2.0
stop music channel "crowd3" fadeout 2.5

pause 1.5

drayden "Very well. You may begin at your leisure. Terms, rules, restraints--you may decide these freely between yourselves."

raihan @talkingmouth "Neat."
raihan @happy "I'm going to be real with you, [last_name]--we can do this however you want. I've got my preferences, 'course, but, hey, I'm the Great Raihan. And only Leon beats me, even if I'm using three newly-caught Pokémon."

red @talkingmouth "Alright, but just to be certain, you aren't going to pull out a Pokémon that's, like, a dozen levels higher than anything I could reasonably have at this time, right?"

raihan @surprised "What? No, of course not. What kind of dick would do that?"

show stadium_empty with vpunch

blue @angry "{size=30}That was uncalled for!{/size}"

pause 1.0

raihan @talkingmouth "...Something in the wind? Alright, so, what're you thinking, [last_name]? Have you got taste?"

$ battletype = 1

menu:
    "Let's do a single battle.":
        raihan @talkingmouth "Alright. Singles. Classic. Can't hate it."

    "Let's do a double battle.":
        $ battletype = 2
        $ ValueChange("Raihan", 1, 0.66)

        raihan @happy "Now you're speaking my language."

    "Let's do a triple battle.":
        $ battletype = 3
        raihan @talkingmouth "Oh, yeah, those are popular over here in the territories, aren't they?"

        show stadium_empty with vpunch

        nessa @sadbrow talkingmouth "{size=30}Rai, they haven't been territories for a couple hundred years.{/size}"

        pause 1.0

        raihan @closedbrow sadmouth "...More wind?"

hide raihan with dis

show drayden:
    xpos 0.33
    ease 0.5 xpos 0.5

drayden "I, Drayden, will referee. Remember, both of you, your intent is to {i}win.{/i}"
drayden @happy "Please do your best."

python:
    trainer1 = MakeRed(battletype)
    trainer2 = Trainer("raihan", TrainerType.Enemy, GetTrainerTeam("Raihan"), number=battletype)

call Battle([trainer1, trainer2]) from _call_Battle_132
$ battlehistory["Raihan1"] = _return

$ renpy.music.queue("Audio/Music/brandnewworld.ogg", channel='music', loop=True, tight=None)

show drayden:
    xpos 0.5
    ease 0.5 xpos 0.33

show raihan with dis:
    xpos 0.66

pause 1.0

raihan @happy "Nice battle."

pause 1.0

redmind @confusedeyebrows frownmouth "Nice battle? That's all?"

if (WonBattle("Raihan1")):
    $ ValueChange("Raihan", 3, 0.66)

    raihan @sadbrow talkingmouth "You won, fair and square, mate. You made the right moves, I made the wrong ones."

    red @talkingmouth "That's not totally fair to you. You were using new Pokémon."

    raihan @closedbrow talking2mouth "Nah, there was a way I could have won that."

    raihan @happy "Seems we won't be seein' much of each other after all. Hope you drop by Galar some time, though. I'd love a rematch in a couple years."

    drayden @closedbrow "...You are giving up that easily?"

    raihan @sad "I don't like it, but taking a loss to the chin is nothing new to me."
    raihan @happy "You can complain all you want that the wind didn't blow your way, but if you do that, people'll blow you off."
    raihan @talkingmouth "Only when you {i}accept{/i} your losses can you move past them."

    blue @frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    raihan @happy "Besides, what would the Fang Gang think if any video of me whining about being beat got onto the internet?"
    raihan @happy "They'd think I'm a right poser, and I'd have to agree with them. A dragon only roars louder after a defeat. That's the way it is."

    raihan @talkingmouth "Besides, I got to battle [last_name], got to talk to Sunny and Ness. From where I'm standing, I feel like I got everything I wanted done."
    raihan @talking2mouth "Don't worry about our deal, Drayden. I'll tell Big Man Rose that everything you're doing here is on the up-and-up."

else:
    raihan @talkingmouth "You did really well. I see your battle against Berlitz wasn't a fluke at all. You just have a bit less experience with your Pokémon."
    
    red @talkingmouth "That's not totally fair to you. You were using new Pokémon."

    raihan @closedbrow talking2mouth "Sure, but the skills are transferrable. Now, I'm not saying there was no way you could have won that, but, still, a couple mistakes have to be expected for a beginning trainer, right?"

    red @sad2eyes angryeyebrows talking2mouth "...Right."

    pause 1.0

    raihan @talkingmouth "Hey. Don't be mad, mate. Believe, me I know how you're feeling. I still don't like it, but taking a loss to the chin is nothing new to me."
    raihan @happy "You can complain all you want that the wind didn't blow your way, but if you do that, people'll blow you off."
    raihan @talkingmouth "Only when you {i}accept{/i} your losses can you move past them."

    blue @frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    raihan @sadmouth "I wasn't great at that, at first, but I learned. I get the feeling you're already better than me there."

    raihan @talkingmouth "So, Dean, did I pass?"

pause 1.0

drayden @closedbrow "...There is no entrance exam."

raihan @talkingmouth "Yeah, I knew. Ness told me, but I knew even in the garden. I've got a hard head, not a thick one."

drayden @surprisedeyebrows "So you correctly interpreted this as a test of character."

raihan @talking2mouth "Seems like it."

drayden @closedbrow "This speech, then... was it to appeal to the hidden criteria you were aware existed?"

raihan @talkingmouth "I'd like you to believe that's just who I am as a person."

drayden @closedbrow "I sensed words spoken from the heart. But at the same time, you used the crowd, and your leverage on Rose, as an advantage over me."
drayden @sadbrow "You put on the airs of a force from the desert, yet you hail from Hammerlocke." 
drayden @sadbrow "You speak of humility and accept losses with grace and dignity, but title yourself 'The Great Raihan' and continue challenging your greatest rival over and over..."
drayden "You are quite a study in contradiction, Master Raihan."

raihan @talkingmouth "Sand that settles becomes rock. Then some geologist slaps a name on it, and everyone thinks they know everything there is to know about it. Gotta keep shifting to keep people interested."

pause 1.0

drayden @surprisedeyebrows "That's not how rocks work. Rocks are eroded by wind or water, then {i}become{/i} sand."

raihan @talking2mouth "Counterpoint.{w=0.5} Sandstone."

drayden @closedbrow "I do not know enough about geology to dispute this."

pause 1.0

raihan @talkingmouth "...So, what's the decree, Dean? I'm at your feet, here. I don't usually beg, but I'll give it a fair shot."

drayden "You are... permitted to join as a provisional student. Given your experience and fame in Galar, a lot will be expected of you from your classmates and instructors. Please set a good example."

raihan @happy "Always do. Just check my RotoPhotos. I'm squeaky clean."
raihan phone @surprised "Oh, that reminds me! [last_name]! Victory selfie?"

menu:
    "I'll pass.":
        raihan -phone @closedbrow sadmouth "...Eh, fine. But we're not through yet. When you have the time, I need to know more about that Pikachu of yours."

    "Cheese!":
        $ ValueChange("Raihan", 1, 0.66)

        show blank with dis

        pause 1.0

        hide blank with Dissolve(3.0)

        raihan -phone @talkingmouth "That's a good one."

        show raihan:
            xpos 0.66
            ease 0.5 ypos 1.2 zoom 1.3

        raihan @talkingmouth "Hey. That was a good battle. But we're not through yet. When you have the time, I need to know more about that Pikachu of yours."

raihan @talkingmouth "I've got a feeling... call it a whisper on the wind... that that Pikachu might be the key to defeating Leon. The King of Champions."

$ PlaySound("pokemon/pikachu_angry1.ogg")
libpikachu @angryeyes talking2mouth "Pika!"

raihan @talkingmouth "Seems like the little guy agrees."

drayden @closedbrow "Thank you for your aid in this matter, Mr. [last_name]. You are free to go."

red @happy "Anytime."

pause 1.0

red @talkingmouth "Um... are there any scholarships for, like, helpfulness?"

drayden @sadbrow "No."

red @sweat closedbrow talkingmouth "Right, just thought I'd check."

scene blank2 with splitfade

call freeroam from _call_freeroam_20

scene blank2 with Dissolve(2.0)

call nightroam from _call_nightroam_2

scene blank2

pause 2.0

jump day010514