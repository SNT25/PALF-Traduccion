label secondhomeroom010420:

scene blank2

scene blank2

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom behind blank2

show oakbg behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade

$ renpy.music.set_volume(0.1, delay=1.0, channel="music")
$ PlaySound("BellChime.ogg")

$ renpy.pause(2.0, hard=True)
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

oak @talkingmouth "Oh? Looks like we're out of time. I get so caught up in my lectures on sound-based moves. I can hardly stop talking about them, hah hah!"

pause 1.0

oak @talkingmouth "Well, I thought that was funny. Dismissed!"

hide oakbg with dis

pause 2.0

show oak with dis

if (wins > 5):
    oak @talkingmouth "Lad. I wanted to commend you on your performance in the Battle Team tryout yesterday."
    
else:
    oak @talkingmouth "Lad. Despite the difficulties you faced, your battle performance yesterday was quite striking."

red uniform @happy "Aw, thanks. My classmates were seriously tough, though."

oak @happy "Hm. Nothing compared to you, though, my boy. Why, I hardly care to remember their faces."

red @talking2mouth "But, actually, about that... there was something I wanted to ask you."

oak @surprised "Oh?{w=0.5} Well...{w=0.5} I suppose I have time.{w=0.5} Would you follow me to my lab?"

red @talking2mouth "Sure."

show blank2 with splitfade

stop music fadeout 2.5
queue music "audio/music/power plant_start.ogg" noloop fadein 1.0
queue music "audio/music/power plant_loop.ogg"

scene research
show oak
show blank2

pause 1.0

hide blank2 with splitfade

pause 1.0

oak @talkingmouth "Well, lad, what did you want to talk about?"

show oak surprisedbrow frownmouth with dis

red uniform @sad "Sam, I'm worried about the effect my Frienergy might be having on the people around me."

pause 2.0

oak -surprisedbrow -frownmouth -surprised @talking2mouth "Please explain."

red @happy "Why don't you guess what I'm saying, and I'll tell you if you're right?"

oak @angry "I clearly don't have time for these games, lad."

red @closedbrow talking2mouth "No sense of humor..."
red @talking2mouth "Look, even ignoring that my Pokémon listen to me, I'm concerned that people are being affected more by my Frienergy than you said they would."

oak @talking2mouth "What do you mean?"

show research:
    xalign 0.0 zoom 1.0
    ease 0.5 xalign 0.1 zoom 1.3
    pause 1.0
    ease 1.0 xalign 0.9
    pause 1.0
    ease 2.0 xalign 0.0 zoom 1.0

pause 5.0

red @closedbrow talking2mouth "Okay, no-one else is here... Janine basically confessed that the Battle Team tryouts weren't {i}really{/i} for me. All I needed to do was show up, and she would let me in."
red @sad "Doesn't that feel messed up? And, like, hugely unfair? I've got an overwhelming advantage."

oak @angry "Lad, you have no evidence her decision was not made based purely on the fact you represent an incalculable asset to the Battle Team."

red @talking2mouth "I mean, true. But I'm also doing {i}really{/i} well on the Student Council elections, from what I've heard. And I haven't really tried at those, either."

oak @talkingmouth "Oh, that reminds me, lad! I wanted to let you know you needn't worry about that 'Cheren' boy anymore."

red @surprised "Huh?"

oak @talking2mouth "Yes, I had a chat with him, and made it clear that he should not be looking into the circumstances of your admittance into this school."

pause 1.0

show research 
show oak surprisedbrow frownmouth
with vpunch

red @surprised "WHAT?!"

oak @talkingmouth "Eh? What's wrong?"

red @sad "Sam, if you tell him not to look into something, that's basically admitting that there's something there you're trying to hide!"

oak -surprisedbrow -frownmouth -surprised @happy "Oh, there's no need to worry about that. He said he had the utmost respect for my professorial position, and understood me loud and clear. His exact words."

red @closedbrow frownmouth "Shit, shit, shit."

oak @talkingmouth "In any case, is that all you wanted to say? I've been analyzing the shards of the meteorite, and it's giving off a most wonderful energy I'd like to study further."

red @closedbrow talking2mouth "Okay. One crisis at a time. I need to handle this soon... but about my Frienergy, I was wondering if there was a way I could... I don't know...{w=0.5}{nw}"

show oak angry with dis 
stop music

extend @talkingmouth " Turn it off?" 

pause 2.0

oak @talking2mouth "I believe there is, Lad. But, if you were to no longer have this ability..."

pause 1.0

oak @talking2mouth "There would be no reason for me to have brought you here to this school."

pause 1.0

red @talking2mouth "...Sam?"

queue music "audio/music/power plant_start.ogg" noloop fadein 1.0
queue music "audio/music/power plant_loop.ogg"

oak @talking2mouth "Lad, you need to understand how important this is. You represent a possible breakthrough in humanity's very understanding of bonds."
oak @talking2mouth "This research will affect every man, woman, and child in every region. Your Frienergy could possibly upend society as we know it."

pause 1.0

oak -angry @happy "We can't let humanity's future be jeopardized by silly reasons such as fear of unearned success, can we?"
oak @talkingmouth "Lad, people stumble into success without deserving it {i}every day{/i}. For a myriad of reasons. Just look at [blue_name]."

pause 1.0

red @talkingmouth "...Even so. If someone did want to turn off my Frienergy. How could they even do that? Could a Gulpin just throw its Gastro Acid over me?"

oak @closedeyes talking2mouth "No, that would just make you very sticky and uncomfortable."

pause 1.0

oak @talkingmouth "I'll tell you this, lad, only because I trust you. And I trust you won't use the knowledge I'm about to give you."

redmind @sad "Yeah, that's kinda the problem... You {i}shouldn't{/i} trust me."

oak @talkingmouth "Based on prior research, the effect of Frienergy can be vastly diminished through one of two ways."
oak @closedbrow talking2mouth "If the person with Frienergy is aware of their power, and trying to keep it a secret, then its effect is lessened."
oak @talkingmouth "Similarly, if the target of the Frienergy is aware of the user's power, and regards them with suspicion, Frienergy is not, typically, enough to override those natural feelings."

red @confused "Wait. Then why did you tell me about Frienergy? If you knew that me having to keep it a secret would make it weaker, then..."

oak @talking2mouth "Well, I'll admit that wasn't totally logical. But we've built up enough of a rapport over the years that I thought you deserved to know, regardless of how it might skew the data."
oak @closedbrow talking2mouth "Besides. I'm fairly certain that a boy as good-natured as you doesn't truly {i}want{/i} to keep it a secret. You probably want to tell everyone, right? Get that weight off your conscience?"

red @sad "Well... yeah."

oak @talkingmouth "There we go, then. There's no problems."

pause 1.0

oak @talking2mouth "As long as you don't {i}actually{/i} tell anyone, of course."

pause 1.0

$ PlaySound("Auto-Door.ogg")

sonia uniform @surprisedmouth "O-oh! I didn't realize that... I'm sorry, I didn't realize this was an automatic door."

show oak:
    ease 0.5 xpos 0.25
show sonia uniform at rightside with dis

sonia @talking2mouth "Er... Am I interrupting something, Professor?"

oak @talkingmouth "No, we were just finishing. What can I help you with, Miss...?"

sonia @talking2mouth "Magnolia. Sonia Magnolia."

sonia @sad "Um, I have some resumes... I've worked as a research assistant for a few firms in Inspira... and I'm kind of short on money..."

oak @closedbrow talking2mouth "Hmmm. Did you say Magnolia? Are you by any chance related to the Professor Magnolia, famed Dynamax scholar of the Galar region?"

sonia @talking2mouth "Right. She's my Gran, actually."

oak @happy "Oh, why didn't you say so? I could certainly use a research assistant with your pedigree! I met your grandmother at a few conferences, and she always speaks quite highly of you."

sonia @surprised "Really? She mostly just nags me about not living up to my potential when we're talking."

oak @closedeyes happymouth "Her way of showing affection, I imagine. Don't worry about it at all." 
oak @talkingmouth "Tell me, have you any experience with astrogeology?"

sonia @talking2mouth "Well... I've been a bit involved in the study of Wishing Stars in Galar. Actually, I was part of the team that proved they weren't fragments of celestial rock, like we thought, but parts of a massive, unknown, Pokémon."
sonia @sad "...So I guess I was responsible for proving that Galar's most popular astrogeological topic was actually in the realm of astrobiology."

oak @talkingmouth "Well, it may still be relevant. Until my coworkers from Hoenn get here, I'd welcome your expertise."

pause 1.0

show sonia sad with dis

oak @sadeyes sadeyebrows talking2mouth "I must ask, though. Isn't your uniform rather tight?"

red @surprised "Oh my god, Sam. You can't just say that!"

oak @talking2mouth "Why not? Look at the poor girl! She's clearly suffocating to death."

sonia @talking2mouth "Ah... this was my uniform last year, and... yes, it's a bit tight."

oak @talking2mouth "Well, I might suggest that, with the money I pay you, you buy a uniform more fitting!"
oak @talkingmouth "I hardly want you passing out while you're handling a chunk of extraterrestrial rock. You might drop the thing!"

sonia -sad @happy "If it made it all the way here from the exosphere, it should jolly well survive a couple feet from a countertop."

oak @talkingmouth "Ah, there's a smile. Much better. A research laboratory is no place for frowns. Not when we have the exciting work of science to be doing."

pause 1.0

red @sad "{w=0.5}.{w=0.5}.{w=0.5}."

oak @talkingmouth "Well, [first_name]? Anything else?"

red @closedbrow talking2mouth "No, Professor Oak. I'll be going now."

call freeroam from _call_freeroam_6

scene dorm_B norm
show screen currentdate
with Dissolve(2.0)

stop music fadeout 2.5

queue music "Audio/Music/Road to Viridian City.ogg"

show brendan:
    xpos 0.8
show ethan behind brendan:
    xpos 0.4
show calem behind brendan:
    xpos 0.2
show hilbert behind brendan:
    xpos 0.6
with dis

brendan @happy "Hey, dude!"

red @happy "Hi, Brendan. What's happening, you guys?"

calem @talkingmouth "Well, while you were gone, a box arrived. It's addressed to you, Ethan, and Hilbert."

red @surprised "Huh. Maybe it's Battle Team stuff?"

ethan @closedbrow talking2mouth "I dunno, man. With my win ratio, I don't think I'm even getting a rejection letter."

hilbert @talkingmouth "Yeah. And I was only... mediocre, myself."

if (wins < 5):
    red @sad "Yeah, same here..."
    redmind @thinking "Not that that'll affect me getting into the team. But I {i}do{/i} wonder what's in the box."

red @confused "Weird. Any idea who it's from?"

ethan @closedbrow talking2mouth "Bibarel delivered it, but she does stuff for everyone. Ran off before we could ask her."

calem @talkingmouth "He means Bianca."

redmind @thinking "Does things for everyone? So they mean green-hat Bianca. Not Tia Bianca."

ethan @talkingmouth "Well, should we open it?"

red @closedbrow talking2mouth "Yeah. Anyone got any scissors?"

brendan angrybrow happymouth "No need! I'll cut it in half with my Brendan-style judo chop!"

calem @sad "Oh dear... I've had quite enough of the faux-martial nonsense from Instructor Marshal."

show brendan:
    ease 1.5 xpos 0.5 ypos 0.9
    linear 0.1 ypos 1.2 

brendan @talking2mouth "Haaaai{w=1.3}{nw}"   

$ PlaySound("body crash.ogg")
show dorm_B norm with vpunch

extend @talkingmouth "-ya!"

show brendan -angrybrow -happymouth with dis:
    ease 0.5 xpos 0.8 ypos 1.0

narrator "As the box splits in half, a couple papers fly out. You, Ethan, and Hilbert all catch one."

red @confused "Hm? Okay, uh..."

if (wins > 4):
    "The Letter" "You did well enough I would have considered you even without your ability to make Pokémon listen to you, but since you have that, I'm obviously not letting go of you."
else:
    "The Letter" "I'll be honest, you didn't do very well in those tryouts. If it wasn't for your ability to make Pokémon listen to you, I wouldn't give you a second look, but since you have that, I'm obviously not letting go of you."

show hilbert surprisedbrow frownmouth with dis

"The Letter" "As a heads-up, the Battle Team is going to be {i}intense{/i}. I'm going to put you through champion-level training. Dropping you from the team is not an option, so you're {i}going{/i} to make it through. In one piece, or otherwise."

show ethan surprisedbrow frownmouth with dis

"The Letter" "Still, I have faith you'll pull through. Also, I need you to. I've been here three years. I'm leaving {i}this year.{/i} This year, there will be {i}NO RETREAT.{/i} And you're going to make that happen for me."
"The Letter" "Welcome to the team. Battle Team meetings are Fridays, after school, at night. Don't worry about curfew, BT meetings are exempt. Attendance is mandatory.\n{w=0.5}--Janine"

redmind @thinking "And I thought Leaf was pushy..."

calem @talkingmouth "Well? Enlighten us."

"{color=#cf0000}[first_name]{/color} & {color=#c1861e}Ethan{/color} & {color=#353535}Hilbert{/color}" "{w=0.5}.{w=0.5}.{w=0.5}.I got in."

show brendan surprisedbrow frownmouth
show calem surprisedbrow frownmouth
with dis

"{color=#cf0000}[first_name]{/color} & {color=#c1861e}Ethan{/color} & {color=#353535}Hilbert{/color} & {color=#4d7ac4}Calem{/color} & {color=#db4039}Brendan{/color}" "{size=50}What?!{/size}"

pause 1.0

ethan -surprisedbrow -frownmouth -surprised @closedbrow talking2mouth "Oh, wow, that {i}could{/i} blow the ears out of a Loudred. You were right."

show calem -surprisedbrow -frownmouth -surprised
show brendan -surprisedbrow -frownmouth -surprised
show hilbert -surprisedbrow -frownmouth -surprised
with dis

hilbert -surprisedbrow -frownmouth -surprised @talkingmouth "If the Battle Team is letting in mediocre trainers like myself, I'm not sure I care to be part of it anymore..."

red @talkingmouth "Well, what did your letter say? Janine must have had a good reason."

hilbert @sadbrow talkingmouth "Just some nonsense about how my strategy to ensure obedience was very creative, and out-of-the-box thinking like that has been sorely lacking in the team's previous rosters."

red @confused "Dude, that's a massive compliment."

hilbert @closedbrow talkingmouth "Creativity is the crutch of those lacking power. If I had power, I would not {i}need{/i} creativity."

red @talkingmouth "And what about you, buddy? What did Janine say about you?"

ethan @closedbrow talking2mouth "{w=0.5}.{w=0.5}.{w=0.5}.{nw}"
extend @talkingmouth "Uh, nothing much. Just some stuff about how she liked that my Pokémon listened to me."

red @confused "...Huh. Alright, then."

ethan @sadbrow happymouth "Yeah, I'll just throw this in the trash. I mean, I half expect her to say she made a mistake when I show up for practice, you know?"

red @sad "Aw, c'mon, Ethan. She wants you. That letter is proof."

brendan @talking2mouth "Oh, guys, look! There's some items and stuff in here! Maybe those're your awards for joining the Battle Team?"

if (wins == 7):
    narrator "You gained 5 Ultra Balls!"

    $ GetItem("Ultra Ball", 5)

if (wins > 5):
    narrator "You gained 10 Great Balls!"

    $ GetItem("Great Ball", 10)

if (wins > 4):
    narrator "You gained 1 Poké Ball!"

    redmind @frownmouth "One Poké Ball? Really? That's it? Wait... there's another note here..."

    "The Letter" "P.S. I breed these little guys in my spare time. They're kinda a Battle Team mascot. Maybe you'll find them useful."

    red @surprised "Huh?"

    python:
        falinksobj = Pokemon(870, level=11)
        AddMon(falinksobj)

else:
    hilbert "Ugh... looks like she gave me a Pokémon."

$ sidemonnum = 870

$ PlaySound("Pokemon/Ball sound.ogg")
queue sound "Audio/pokemon/cries/870.mp3"

show calem:
    ease 0.5 xpos 0.1
show ethan:
    ease 0.5 xpos 0.3
show brendan:
    ease 0.5 xpos 0.9
show hilbert:
    ease 0.5 xpos 0.7

show sideportraitfull at pokeball, dormdesk behind ethan

calem @talkingmouth "Oh? Curious."

brendan @happy "Woah, that's a Pokémon? It looks like a bunch of smaller Pokémon, though."

queue sound "Audio/pokemon/cries/870.mp3"

red @talkingmouth "Yeah, that's Falinks, the Formation Pokémon. The one at the front, with the crest, is called 'The Brass,' and all the other Falinks listen to its commands."

if (wins > 4):
    hilbert @sadbrow talkingmouth "Yeah... she gave one to me, too."

calem @surprised "Oh? But you don't seem happy about that, Hilbert."

hilbert @talkingmouth "I don't deserve this. This is... this is {i}pity.{/i}"

calem @talkingmouth "Well, what do you intend to do with it? Release it into the wild?"

red @closedbrow talking2mouth "Not a great idea. It's a Fighting-type. It'd decimate the local population in the fields. Maybe the forest? But even then, it should live in mountains."

hilbert @talkingmouth "...Calem, you're taking the Fighting elective, right?"

calem @surprised "Well, yes, I suppose, but..."

hilbert @closedbrow talkingmouth "Take it."

show calem surprisedbrow frownmouth with dis

hilbert @talkingmouth "I'm going to bed."

hide hilbert with dis

pause 2.0

calem -surprisedbrow -frownmouth -surprised @talkingmouth "Oh. Well... thank you!"

pause 1.0

if (wins > 4):
    red @happy "Well, I'm not giving mine away!"

    red @closedbrow talking2mouth "Let's see... what kinda name should I give you?"

    label falinksnickname:

    $ falinks_name = renpy.input("{color=#e70000}Your Falinks' nickname? (Press Enter for the default){/color}", length=12, exclude="{}[[]%<>")
    $ falinks_name = falinks_name.strip()

    if falinks_name == "" or falinks_name == "falinks":
        $ falinks_name = "Falinks"

    red @talkingmouth "Hm... I think [falinks_name] would suit you just fine."

    menu:
        "Yeah, that'll do, [falinks_name].":
            red @happy "Yeah, that'll do, [falinks_name]."

        "Wait, I've got a better idea.":
            jump falinksnickname

    $ falinksobj.Nickname = falinks_name

red @closedbrow talking2mouth "I should probably get to bed soon, too. Got some awkward conversations to have tomorrow."

calem @closedbrow talking2mouth "Oh? Care to elaborate?"

red @talkingmouth "I've just gotta have a chat with Cheren. About some Student Council stuff."

calem @sad "Say no more. Godspeed."

ethan @happy "Goodnight, you two!"

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_62

show sideportraitfull at backinpokeball, dormdesk

hide calem
hide brendan
hide ethan
with dis

pause 2.0

redmind hatless casual "Right... where's my phone? Ah, there."

call afterroomsetuptexting from _call_afterroomsetuptexting_2

show blank2 with transeye

pause 2.0

redmind "Alright. Now..."

menu:
    "{color=#60c2f8}[[Wit]{/color} >Look through the trash for Ethan's letter":

        $ TraitChange("Wit")

        "The Letter" "I'll be honest, you did awfully in those tryouts. In fact, I don't think I've ever seen a worse tryout record."
        "The Letter" "But your Pokémon followed you flawlessly. Even if you told them to do something actively disadvantageous to them, they still followed your commands."
        "The Letter" "You were holding back. That much is obvious. You were purposefully battling worse than you could. Doing your worst to stand out. I don't get why, and I don't really care right now."
        "The Letter" "However, let me be {i}absolutely{/i} clear. If you don't quit that, I'm dropping you."
        "The Letter" "I want you to know that, of all the people I saw at the tryouts, you're my second choice. Take that as a compliment. I'm impressed. But I want to be {i}more{/i} impressed."
        "The Letter" "Welcome to the team. Battle Team meetings are Fridays, after school, at night. Don't worry about curfew, BT meetings are exempt. Attendance is mandatory.\n{w=0.5}--Janine"

        redmind @thinking "...So, Janine also wanted Ethan, regardless of how well he did. Guess I'm not completely special, then."

        pause 1.0

        redmind @happy "In a way, that's reassuring."

    "{color=#e226a6}[[Patience]{/color} >Just go to sleep":

        $ TraitChange("Patience")

        redmind "Nah. I'm not going to dig through the trash to read Ethan's private letter. That'd be messed up."

jump day010421