label lunch010524:

stop music fadeout 1.5

narrator "You've only just walked into the cafeteria when you suddenly notice a commotion--a group of students are surrounding some sort of argument happening at a table in the center of the room."

red uniform @confusedeyebrows talking2mouth "Hm...?"

show melody on with dis:
    xpos 0.33

#KLARA NOTE: Yaaaay!~ I can finally make my big-screen debut! This is great. I hope everyone loves me! ;D
show klara sadbrow uniform frownmouth with dis:
    xpos 0.66

pause 1.0

queue music "audio/music/everyonesfavoritegirl_start.ogg" noloop
queue music "audio/music/everyonesfavoritegirl_loop.ogg"

melody @talkingmouth "...{size=15}In{/size} {size=20}my{/size} {size=25}way?{/size} Bad move."

$ BecomeNamed("Melody")

klara @surprisedbrow talking2mouth "Oh, no, I didn't mean anything by it, Melody! I just, {size=25}oh no,{/size} {size=20}everyone's{/size} {size=15}staring at me...{/size}"

redmind @angrybrow frownmouth "Hey, what's happening here? Is that girl in the sunglasses harassing that pink-haired girl?"

narrator "You scan the crowd for someone you know, and notice Yellow's signature straw hat just under your field of view."

red @talkingmouth "{size=30}Hey, Yellow, what's happening here?{/size}"

$ BecomeNamed("Klara")

yellow uniformhat @sadbrow talkingmouth "{size=30}Oh... I'm not sure. I think this new girl was talking to one of the cafeteria workers, and then when Klara said something to her, she started yelling at her, too...{/size}"

red @confusedeyebrows talkingmouth "{size=30}Klara is...?{/size}"

yellow @surprised "{size=30}One of Leaf's friends. You didn't know?{/size}"

red @happy "{size=30}Never seen her before.{/size}"

klara @sadmouth "Please, I {i}really{/i} didn't want to make you so angry."

melody @talkingmouth "Not angry. Confused, maybe? I guess I just can't get into your mindset and see {i}where{/i} you're coming from, that you think {i}any{/i} of this is a good idea."

klara @sadbrow talking2mouth "Please, please, {i}please{/i} stop being so angry."

melody angryeyebrows ".{w=0.5}.{w=0.5}.{w=0.5}"

melody @talkingmouth "Okay, {i}now{/i} you're ticking me off. Maybe you can't hear me through all that hair--I'm {i}not{/i} angry. Mark it, memorize it, get a tattoo of it."
melody @talkingmouth "You know why I'm not angry? Because you literally don't matter. Water off a duck's back. Say what you want."

klara @closedbrow talking2mouth "Why are you so mean...? Is it because of all those rumors about you...?"

melody angrymouth "Literally shut up."

klara @sadbrow talking2mouth "I just want you to know that {i}I{/i} never believed them. I really think there's good in everyone! Even if you {i}did-{/i}"

melody @talkingmouth "Eff you."

$ PlaySound("pokemon/ball sound.ogg")
$ PlaySound("pokemon/cries/79.mp3")

show melody:
    xpos 0.33
    ease 0.3 xpos 0.15

show slowpoke at pokeball:
    xpos 0.33 ypos 0.9 xzoom -1

melody @talkingmouth "Fight me."

klara @surprised "W-wait! Please, stop! I don't want to fight!"

$ PlaySound("pokemon/ball sound.ogg")
$ PlaySound("pokemon/cries/79.1.mp3")

show klara uniform:
    xpos 0.66
    ease 0.5 xpos 0.85

show gslowpoke at pokeball:
    xpos 0.66 ypos 1.0

pause 1.0

redmind @confusedeyebrows frownmouth "Two Slowpoke? This won't be a quick battle, then..."
redmind @surprised "Wait, that's not important! They can't be battling here!"

show blank2 with dis:
    alpha 0.3

show erika uniform surprisedbrow frownmouth with dis:
    xpos 0.75

erika @surprisedmouth "Should we... not call the disciplinary committee? They are breaking the rules, are they not?"

show misty uniform with dis:
    xpos 0.25 xzoom -1

misty surprised @talkingmouth "This isn't any of our business. Let's just stay out of this."

show gardenia:
    xpos 1.2 ypos 1.0
    parallel:
        easein 0.3 ypos 0.7
        easeout 0.3 ypos 1.0
    parallel:
        ease 0.6 xpos 0.5

show erika surprisedbrow frownmouth with dis

gardenia uniform @angrybrow talking2mouth "Did someone say 'business'?!"
gardenia @happy "Ladies and gentlemen, it's a battle of the babes! Who will win in this climactic cafeteria confrontation? The kind, cute, Klara, or the newcomer, the enigmatic and mysterious Melody?"
gardenia @talkingmouth "The betting pool is now open! Bets start at 3:1, with--"

show erika surprisedbrow frownmouth
show misty surprisedbrow frownmouth
show gardenia surprisedbrow frownmouth
with dis

cheren uniform @talking2mouth confusedeyebrows playfuleyes "What the devil is going on here?"

gardenia surprisedbrow frownmouth @surprised "Eep! Scram!"

hide gardenia with vpunch
hide misty with dis
hide erika with dis
hide blank2 with dis

$ PlaySound("pokemon/ball sound 2.ogg")

show slowpoke at backinpokeball:
    xpos 0.33 ypos 0.9 xzoom -1

show gslowpoke at backinpokeball:
    xpos 0.66 ypos 1.0

pause 1.0

show cheren uniform behind gslowpoke
show silver uniform behind cheren:
    xpos 0.6
show skyla uniform behind cheren:
    xpos 0.4 xzoom -1
with Dissolve(1.0)

Character("Aimless Anarchist") "\"Ugh, the disciplinary committee... I don't know who I'm rooting for {i}less{/i}, here.\""
Character("Bored Boy") "\"Guess the fun's over, now the bad-time brigade's shown up.\""

cheren @talking2mouth "Please explain what has occurred here."

klara @sadbrow talkingmouth "It's... it's really nothing. I'm very sorry, Cheren. Melody and I just lost our tempers a little bit. We were arguing, and she sent out her Pokémon first, starting the fight, and then I sent out my Pokémon, too..."

show cheren:
    ease 0.5 xzoom -1

cheren @talking2mouth "Is this correct? You instigated the conflict?"

melody -angrymouth "{w=0.5}.{w=0.5}.{w=0.5}."

skyla @happy "Sorry, we were asking you if you--"

show silver:
    xpos 0.6
    ease 0.5 xzoom -1

silver @angrybrow angrymouth "She heard. She's just not talking."

show klara surprisedbrow with dis:
    xpos 0.85
    ease 4.0 xpos 1.1

melody -angryeyebrows @talkingmouth "Disciplinary committee?"

cheren @talking2mouth "That is us. May I ask why you're not in uniform?"

melody @talkingmouth "...'Kay. Listen up."

pause 1.0

show cheren surprisedbrow
show skyla surprisedbrow frownmouth
show silver angrybrow
with dis

melody @angryeyebrows talkingmouth "You can't touch me."

pause 0.5

cheren angrybrow @shadow talking2mouth "Please elaborate."

melody @talkingmouth "No."

hide melody with dis

pause 2.0

redmind @poutmouth "...It's almost funny."

pause 1.0

cheren @talking2mouth "Stop."

stop music fadeout 0.5

melody on @surprisedbrow talkingmouth "...'Stop'?"

pause 0.5

show melody on with dis:
    xpos 0.25

show cheren:
    xpos 0.5
    ease 0.5 xpos 0.75
show skyla:
    xpos 0.4
    ease 0.5 xpos 0.65
show silver angrybrow:
    xpos 0.6
    ease 0.5 xpos 0.85
with dis

pause 1.0

show melody up with dis

narrator "'Melody' flips her glasses up. You're immediately struck by the piercing cold of her eyes--eyes that contain nothing but scorn."

pause 0.5

queue music "audio/music/silphco_intro.ogg" noloop
queue music "audio/music/silphco_loop.ogg"

melody @sadbrow talkingmouth "Guess {i}you're{/i} not in the know."

show cheren surprisedbrow
show skyla surprisedbrow frownmouth
show silver surprisedbrow
with dis

melody @angry "Listen up, you Disciplinary dork. I don't do what I'm told."
melody @talkingmouth "I've been pulled into Drayden's office so often I've got a timeshare there."
melody @closedbrow talking2mouth "You can run to Drayden, or the Student Council all you want. But I'm untouchable. You've got no grip, got it, guys?"
melody @angrybrow talkingmouth "I go where I want. I act how I feel. You may be sitting on the throne, but {i}my{/i} crown is real."
melody @angry "So I'm going to {i}run in the hallways.{/i} I'm going to {i}text in class.{/i} And if you want to die on that hill, you can just save us some trouble and off yourself right now."
melody @closedbrow talkingmouth "Mark it, memorize it."
melody @talkingmouth "I'm Melody. And I'm in charge."
melody on @talkingmouth "Clear?"

hide melody with dis

pause 3.0

play music "audio/crowdargue.ogg" channel "crowd" fadein 3.0
play music "audio/crowdargue2.ogg" channel "crowd2" fadein 9.0

cheren @talking2mouth "What...? What do we...?"
cheren @closedbrow talking2mouth "Well, obviously, we report this to the Student Council, but in a much more {i}real{/i} sense, what do we do?"

pause 0.5

silver @sad "At least she told us what to expect, I guess...?"

skyla sadbrow @talkingmouth "I love the confidence, but I have a feeling she's going to be a big problem for us..."

silver @angry "Oh, was it the manifesto she just recited telling us she's going to be a big problem? Is that what gave it away?"

skyla angry "Why are you always so rude?! You could at least {i}try{/i} to get along with me!"

silver @angry "You don't take our job seriously! We--"

narrator "You tune out of the Disciplinary Committee's argument as you begin to hear other arguments arise."

Character("Melody Stan") "\"Holy shit, dude! That was badass! She just tore the Disciplinary Committee a new one!\""

Character("Cautious Kiddo") "\"Uh... I don't know... aren't the school rules, like, kind of important?\""

show whitney uniform with dis:
    xpos 0.1

whitney @happy lightblush "Oh my {i}gosh{/i}, that girl-- Do you think Melody's going to join the nursing course?"

show flannery tiredbrow frownmouth uniform behind whitney with dis:
    xpos 0.2

flannery @talking2mouth "Ugh, you {i}liked{/i} that?"

show grusha uniform with dis:
    xpos 0.3    

grusha @closedbrow talkingmouth "Hm. That's interesting."

show jasmine angry uniform with dis:
    xpos 0.4

jasmine "'Horrendous' is more like it! How incredibly rude of her!"

show misty uniform surprised with dis:
    xpos 0.5

hide klara

misty uniform "Wait... 'Melody'? As in, {i}the{/i} Melody?!"

narrator "As you look around, you begin to realize the entire cafeteria has descended into a frenzy, with everyone arguing at the top of their lungs about Melody's actions."
narrator "The riotous, argumentative, nature gives you some unnerving flashbacks..."

pause 0.5

narrator "You put your hand on [pika_name]'s Poké Ball, and the moment passes."

red @closedbrow talking2mouth "Sheesh. Okay, let's get out of here, bud. There's no reason to stick around and deal with this. Let's go eat in the garden."


show blank2:
    alpha 0.3
show klara makeup angrybrow frownmouth hairpin uniform:
    ypos 1.0 zoom 1.0
    ease 0.5 ypos 1.2 zoom 1.3
with dis

pause 1.0

red @surprised "Woah! Uh, hi?"

klara sadbrow -frownmouth @talkingmouth "Come on, let's get out of here!"

red @surprised "Hold on!"

stop music channel "crowd" fadeout 1.5
stop music channel "crowd2" fadeout 1.5

narrator "Klara grabs your hand in a gesture that feels... {i}immensely{/i} similar to your first meeting with Leaf, and before it even occurs to you to protest..."

stop music fadeout 1.5

scene blank2 with splitfadefaster

pause 1.0

$ renpy.music.queue("Audio/Music/Pallet Town A.ogg", channel='music', loop=True, fadein=1.0, tight=None)

scene garden:
    zoom 0.625
show clouds behind garden
show klara makeup hairpin uniform
with Dissolve(2.0)

klara closedbrow sweat @talkingmouth "...Phew."

pause 0.5

klara -sweat -closedbrow @happy "Are you alright?"

red uniform @talkingmouth "Huh? I mean, yeah, of course. I mean, it was a bit loud in there..."
red @happy "But nothing too bad."

klara @surprisedbrow talking2mouth "Oh, really? I thought... I mean, with the way Cheren was {i}so{/i} mean to you..."

red @closedbrow talking2mouth "Yeah, that wasn't... great. But he didn't, like, turn me off of crowds or anything."

klara @sadbrow talkingmouth "You're very brave. I really admire you, you know?"

red @happy lightblush "Hey, what? That's a bit much! I mean, we've never talked before, right?"

klara blush @sadbrow talkingmouth "Oh... that's right. I'm sorry. I've... I've wanted to talk to you for so long. Ever since our first week of school."
klara surprisedbrow frownmouth @closedbrow talkingmouth "But you're so cool and handsome, that I just couldn't work up the guts! It's like I have little butterflies in my stomach every time I look at you."

pause 1.5

klara -surprisedbrow -frownmouth @sadbrow happymouth "I'm sorry. I shouldn't have said that. You probably think I'm weird, right?"

red @sad2eyes lightblush talkingmouth "N-no. That's, uh... that's very sweet of you."

pause 1.5

klara @surprised "Oh, gosh! I'm {i}so{/i} sorry. I just realized. I never even introduced myself, did I? I'm Klara."

red @happy "Yeah, I know."

show klara hardblush with dis:
    ypos 1.0 zoom 1.0
    ease 0.2 ypos 0.9 zoom 0.9

klara @surprised "Y-you {i}know{/i}?!"

red @talkingmouth "Well, uh, yeah. I--"

show klara hardblush with dis:
    ypos 0.9 zoom 0.9
    ease 0.5 ypos 1.0 zoom 1.0

$ ValueChange("Klara", value=10)

klara @puppybrow surprisedmouth "Does that mean... does that mean you've been watching {i}me{/i}, too? Is that... are you actually...?"
klara @happy "Have you been thinking about me all this time as well?"

red @happy "Sorry, I, uh, I didn't know you {i}that{/i} well."

show klara -hardblush puppybrow frownmouth with dis

klara @talkingmouth "{size=30}Oh...{/size}"

red @talkingmouth "I just heard your name from my friend Yellow. Apparently you know Leaf?"

klara -puppybrow -frownmouth @talkingmouth "Oh... yes! She's a {i}very{/i} good friend. We're besties!"

if (GetRelationshipRank("Leaf") > 0):
    red @happy "Huh. Thought Leaf and I were [bluecolor]besties.{/color}"

    klara @surprised "Oh!" 
    klara @sadbrow talkingmouth "Well... some people just say they're besties with everyone, you know...?"
    klara @happy "But I really mean it!"
    klara @happybrow talkingmouth "A bestie with Klara is a bestie for life!"

else:
    red @confusedeyebrows talking2mouth "I... don't think she's ever mentioned you before."

    klara @surprised "Oh!" 
    klara @sadbrow talkingmouth "Well... you know, some people like to keep their friends group separate, you know...?"
    klara @happy "But there's nothing wrong with that! If they want to act differently with different people, that's completely fine."
    klara @talkingmouth "It's just not for me. I like being... Klara."

red @talkingmouth "Well, Klara, thanks for being concerned about me in the cafeteria."
red @sadbrow talkingmouth "Means you've got a good heart. But I'll be fine."

klara @sadbrow talkingmouth "I'm glad. I don't want to think about anything bad happening to you after..."
klara @blush puppybrow talking2mouth "Well, you know."

pause 1.5

klara @talkingmouth "{size=30}OhgoshIcan'tbelieveI'msayingthisbut{/size} do you want to eat together?"

red @happy "Sure."

klara @happy "{size=30}Yyyes!{/size}"

pause 1.0

narrator "You and Klara sit down on a bench together. Klara unfolds an elaborately-wrapped lunchbox that looks like it has a lot of love and care put into it."

red @sweat talking2mouth "Hey, just to make sure we're on the same page--um, you're not, like, trying to get close to me because of [pika_name], are you?"

klara @surprised "Oh, your Pikachu? No, not at all!"
klara @sweat sadbrow talkingmouth "I liked you even before your Pikachu became special."
klara @happy "And I'm not much of a battler, anyway. I'm more focused on the contest circuit."

red @confusedeyebrows talking2mouth "Oh, yeah? Are you part of the Coordinator Club?"

klara @happy "Yes."

red @talkingmouth "You must know Brendan and May, then."

klara sadbrow frownmouth @talking2mouth "...Oh..."

red @confusedeyebrows talking2mouth "What?"

if (not mayhaslarvesta):
    klara @sadbrow talking2mouth "Well... I shouldn't say anything, you know?"

    red @confusedeyebrows talking2mouth "What is it?"

    klara @angrybrow talking2mouth "They just... they say really strange stuff, sometimes."
    klara angrybrow frownmouth @talking2mouth "Stuff about how a former friend of theirs stole something from them. And they act like they're still friends, but actually, they're badmouthing them all the time, and even {i}laughing{/i} at him..."

    pause 1.5

    klara -angrybrow -frownmouth @surprised "Oh! Um, not him! I meant 'them.' I mean, that friend could be, you know, a girl, too."

    pause 1.0

    red @sad2eyes angryeyebrows frownmouth "That's{w=0.5}.{w=0.5}.{w=0.5}. odd."

    klara @sadbrow talking2mouth "I suggested they just tell the person they're mad at how they feel, but... some people don't want to take the easy solution, I guess..."

    klara @sadbrow talkingmouth "And it doesn't seem fair that they're like that, when..."

else:
    klara @closedbrow talking2mouth "No, it's nothing. I shouldn't gossip."

    red @talkingmouth "Is it something about Brendan and May?"

klara @talkingmouth "It's just... when I see how happy they look as a couple, I..."
klara @happybrow happymouth "Please don't think any less of me! I'm {i}so{/i} jealous!"

red @happy "Nah, I know the feeling."

klara @sadbrow talking2mouth "I mean, I've never even had a boyfriend before."

red @talkingmouth "Same boat. {i}Or{/i} a girlfriend!"

klara blush @surprised "Really? But you're so tall and handsome!"

red @sadbrow talkingmouth "Yeah, uh, it just never happened, somehow."

klara @sadbrow talkingmouth "...So you and Leaf...?"

if (HasEvent("Leaf", "RejectedConfession")):
    red @happy "She asked me out on a date once. I rejected her."

    red @closedbrow talking2mouth "She talked about setting up, like, a platonic 'friend date', but that hasn't happened yet."

else:
    red @talkingmouth "Nah, we haven't even gone on our first date yet."

klara @surprised "Oh!"
klara @sadbrow talking2mouth "I heard that... that keeps getting delayed."

red @talkingmouth "Hm? Yeah, I guess. I mean, Leaf wants it to be perfect, but our schedules keep, kinda, like, missing."

klara @closedbrow talking2mouth "Well, if someone wanted something hard enough, I believe they'd have found a way to make it work."

red @happy "That's the spirit!"

pause 1.0

klara @sadbrow talkingmouth "Um...{w=0.5} {size=30}do you want to...{/size}{w=0.5} I mean... {size=20}with me...{/size}?"

red @talkingmouth "Sorry? Couldn't hear that."

klara -sadbrow -frownmouth hardblush @puppybrow talkingmouth "D-do you... want to go on a date? With me? I-if you're not... not busy. And if you don't hate me."
klara @talkingmouth "We can... we can go out tomorrow evening. I'll... I'll wear something nice. If you want to..."
klara blush puppybrow sadmouth "...Please?"

menu:
    "Sure.":
        pass
    "Absolutely.":
        pass
    "Yep.":
        pass
    "I hate you.":
        pause 2.0

        narrator "Obviously, you do not actually say that. But if you reject this earnest girl's plea for a date, then... doesn't it somewhat seem like that's what you're going to be saying? Maybe you should reconsider...?"

        menu:
            "Yes, let's go on a date.":
                pass

            "Yes, let's start a family.":
                pass

            "Yes, let's file our tax returns jointly.":
                pass

            "You disgust me, wretched creature. Wallow in the filth and muck.":
                pause 2.0

                narrator "It's not often such a beautiful girl approaches you so plainly and demurely with such an innocent request. Don't you think, maybe, you should give her a chance?"
                
                python:
                    highestbond = "Ethan"
                    secondhighestbond = "Leaf"
                    highestbondvalue = GetCharValue("Ethan")
                    secondhighestbondvalue = GetCharValue("Leaf")
                    for char in persondex.keys():
                        val = GetCharValue(char)

                        if (val > highestbondvalue):
                            secondhighestbond = highestbond
                            secondhighestbondvalue = highestbondvalue
                            highestbond = char
                            highestbondvalue = val
                        elif (val > secondhighestbondvalue and char != highestbond):
                            secondhighestbond = char
                            secondhighestbondvalue = val

                narrator "I mean, let's be honest, are you {i}really{/i} going to be able to do any better? Let's see, who's your highest-ranking bonds right now... [highestbond]? [secondhighestbond]? Do you {i}really{/i} see things working out with either of them?"
                narrator "Come on. Stay on the tracks."

                menu:
                    "I would kill for you.":
                        pass
                    "I would die for you.":
                        pass
                    "I would kill myself and die for you.":
                        pass
                    "I would like to play the game incorrectly.":
                        $ AddEvent("Klara", "BreakHeart")
                        jump afterklarapoursherheartouttoyou

$ ValueChange("Klara", 10)

klara -blush -puppybrow -sadmouth @happy "Yaaay! Thank you!"
klara @sadbrow talkingmouth "This really means the world to me. I'll meet you outside your dorm after classes are over, okay?"

red @talkingmouth "Uh, yeah. For sure."

show klara closedbrow kissmouth:
    xpos 0.5 ypos 1.0 zoom 1.0
    ease 3.0 ypos 1.2 zoom 1.3

show flashback with Dissolve(3.0):
    matrixcolor TintMatrix("#ff00005f")

narrator "As though in slow motion, you see Klara come in for a kiss, aimed for your cheek."

menu:
    ">Dodge it":
        $ AddEvent("Klara", "DodgeKiss")
        hide flashback
        show klara surprisedbrow with dis:
            xpos 0.5 ypos 1.2 zoom 1.3
            pause 1.0
            ease 0.5 ypos 1.0 zoom 1.0

        red @sadbrow talkingmouth "Hey, I appreciate it. But let's hold off for now. I mean, we just met each other, right?"

        klara hardblush sadbrow -kissmouth @talkingmouth "Oh, gosh, I'm sorry... I got {i}so{/i} caught up in the moment."

        red @talkingmouth "It's alright. No hard feelings. Let's think about it again at the end of our date, alright?"

    ">Kiss her first":
        $ ValueChange("Klara", 10)

        $ AddEvent("Klara", "KissFirst")
        $ RecordKiss("Klara")
        show klara surprisedbrow:
            xpos 0.5 ypos 1.2 zoom 1.3

        show blank2 
        hide flashback
        with transeye

        narrator "You close your eyes as your lips meet."
        narrator "Your heart beats at an unfamiliar rhythm as your hands intertwine with Klara's..."
        narrator "You feel warm, moist breath where your faces meet. And you're not even sure whose it is."

        pause 1.0

        narrator "This is not the first kiss you had always imagined." 
        narrator "But it's a pretty damn good one."

        pause 1.0 

        $ PlaySound("idea.ogg")

        narrator "You suddenly notice that Klara's hands are getting a bit 'exploratory', and sheepishly pull away."

        hide blank2 with transeye2

        klara hardblush sadbrow -kissmouth @talkingmouth "W-wow."

        red @closedbrow talking2mouth "Y-yeah. That's, uh, that's pretty..."

        klara blush @happy "My first kiss... was with you. I'm so happy...!"

        klara @sadbrow happymouth "I'll talk to you later... and then, maybe... again?"

        red @sadeyebrows sad2eyes talkingmouth "We can, uh, discuss it."

    ">Gently dissuade her":
        $ AddEvent("Klara", "DissuadeKiss")
        hide flashback
        show klara surprisedbrow with dis:
            xpos 0.5 ypos 1.2 zoom 1.3
            pause 1.0
            ease 0.5 ypos 1.0 zoom 1.0

        red @sadbrow talkingmouth "Hey, I appreciate it. But let's hold off for now. I mean, we just met each other, right?"

        klara hardblush sadbrow -kissmouth @talkingmouth "Oh, gosh, I'm sorry... I got {i}so{/i} caught up in the moment."

        red @talkingmouth "It's alright. No hard feelings. Let's think about it again at the end of our date, alright?"

klara happy "I... thank you...!"

hide klara with Dissolve(2.0)

jump afterthebestgirlleaves

label afterklarapoursherheartouttoyou:

python:
    readback_buffer = readback_buffer[:len(readback_buffer) - 9]
    readback_buffer.append(('Klara', "{font=fonts/comic.ttf}*Coolly* Hey I wondered if you wanted like a peice of my sandwich or whatever *its obvious shes super into you*{/font}", None ))
    readback_buffer.append((first_name, "{font=fonts/comic.ttf}Absolutely not klara even though you are very attractive and smart I do not accept generoisty and also haate puppies *WRONG ANSWER*{/font}", None ))

show klara -blush -puppybrow -sadmouth with dis:
    ypos 1.0 zoom 1.0
    ease 0.2 ypos 0.9 zoom 0.9

klara @talkingmouth "...Huh?"

red @happy "Sorry, Klara. You seem like a great girl, but I just met you, like, twenty minutes ago. I'm not sure I should be dating someone so soon, you know?"

klara @happy "Hah! [first_name], what are you talking about? I didn't ask you for a date!"

red @confusedeyebrows talking2mouth "Um... I'm pretty sure you..."

klara @sadbrow talkingmouth "Oh, you're really cute, I get it. But you don't need to pretend I said something I didn't. I know you heard me properly."
klara @happy "It's alright, I won't hold it against you! I'll just talk to you later, okay?"

hide klara with Dissolve(1.0)

redmind @thinking "Maybe I... misunderstood what she was saying? I could've sworn that... huh."

red @confused "Well, I don't have the {i}best{/i} memory, I guess."

label afterthebestgirlleaves:

narrator "Your stomach suddenly lets out a loud growl."

redmind @happy "Wait... I just realized... Klara ate, but I didn't have any food with me! I get lunch from the cafeteria! I should probably..."

$ PlaySound("BellChime.ogg")

show garden:
    matrixcolor SaturationMatrix(1.0)
    linear 6.0 matrixcolor SaturationMatrix(0.2)

show clouds:
    matrixcolor SaturationMatrix(1.0)
    linear 6.0 matrixcolor SaturationMatrix(0.2)

pause 4.0

redmind noeyes shadow @frownmouth "Just one missed lunch, and I'm suddenly wondering if Kobukan is worth it."

$ PlaySound("Pokemon/pikachu_sad.ogg", otherchannel="altcry")
libpikachu @sadeyes sadmouth "Pika..." 

jump PickElective