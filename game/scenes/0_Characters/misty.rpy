label Misty1:
    if (not IsBefore(1, 5, 2004)):
        $ persondex["Misty"]["Events"].append("Level2SceneVer2")

    scene pool 
    show misty
    with Dissolve(2.0)
    queue music "Audio/Music/CeruleanCity.ogg"

    red @happy "Hi."

    show misty surprisedbrow frownmouth with dis

    pause 1.0

    misty -surprisedbrow -frownmouth -surprised @sadmouth "What do you want?"

    red @closedbrow talking2mouth "Hmm... to become a Pokémon Champion, mostly."

    misty @angry "Yeah, good luck with that. You can do that somewhere else, can't you?"

    red @happy "Probably, but I thought it might be more fun to do it in your company."

    misty sweat @surprised "Huh? Something wrong with you? I'm not exactly pleasant company."

    red @closedbrow talking2mouth "{size=30}Well, I can't deny that...{/size}"
    red @closedbrow talking2mouth "But I thought maybe I could do something to help you out. And then you might be... uh..."

    pause 1.0

    misty -sweat @sad "Less of a bitch?"

    red @closedbrow talking2mouth "I was going to say 'more comfortable around me.'"

    if (not IsBefore(1, 5, 2004)):
        misty @surprised "What, you're still on about the whole mind control thing?"

        misty @closedbrow talkingmouth "Give it a rest. I already know you don't have that thing. You told the entire school, remember?"

        red @talkingmouth "Do I ever. But I didn't mean that kind of 'more comfortable.' I just meant, like, generally."

    misty closedbrow @talking2mouth "Whatever. I don't even know what you could do for me, anyway."

    red @happy "Then you're in luck, because I totally do!"

    misty -closedbrow @surprised "Oh, this'll be good. What is it?"

    red @closedbrow talking2mouth "Well, I've been thinking about your Psyduck, ever since we battled in Gym Class."

    misty @sad "...Yeah? What about him?"

    red @talkingmouth "I was thinking I might be able to help you make him listen to you."

    if (IsBefore(1, 5, 2004)):
        misty @talkingmouth "Oh, what, like you're some kinda Pokémon whisperer?"
    else:
        misty @closedbrow talking2mouth "Oh, yeah, that was one of your powers or whatever, wasn't it? You're a Pokémon whisperer."

    red @closedbrow talking2mouth "Well... I don't talk to them, but I am pretty good with them, yeah."

    if (IsBefore(1, 5, 2004)):
        $ renpy.music.play("Audio/Pokemon/pikachu_happy2.ogg", channel="altcry", loop=None)
        pikachu happy_2 "Pika!"
    else:
        $ renpy.music.play("Audio/Pokemon/pikachu_happy2.ogg", channel="altcry", loop=None)
        libpikachu happy "Pika!"

    red @happy "Thanks for the support, bud."

    misty @closedbrow talkingmouth "Well, fine. What are you going to do?"

    red @talkingmouth "Would you mind sending out your Psyduck?"

    $ PlaySound("Pokemon/Ball sound.ogg")
    queue sound "audio/pokemon/cries/54.mp3"

    $ sidemonnum = pokedexlookupname("Psyduck", DexMacros.Id)

    show sideportraitfull at dormdesk, pokeball
    show misty:
        easein 0.5 xpos 0.75

    Character("{color=#c4a300}Psyduck{/color}") "Psy?"

    red @closedbrow talking2mouth "Hey, little man! How're you doing?"

    queue sound "audio/pokemon/cries/54.mp3"

    Character("{color=#c4a300}Psyduck{/color}") "Psy-ai-ai!"

    red @happy "Really? Wow. To shreds, you say?"

    red @closedbrow talking2mouth "And how's her bike holding up?"

    Character("{color=#c4a300}Psyduck{/color}") "Psy."

    red @closedbrow talking2mouth "Really? Wow. To shreds, you say?"

    show sideportraitfull:
        ease 0.5 xpos 0.75 ypos 1.1 zoom 0.8 xzoom 1
        pause 0.5
        parallel:
            ease 1.0 xpos .65
            ease 1.0 xpos .75
            ease 1.0 xpos 0.85
            ease 1.0 xpos 0.75
            repeat
        parallel:
            pause 0.8
            ease 0.2 xzoom -1
            pause 1.0
            pause 0.8
            ease 0.2 xzoom 1
            pause 1.0
            repeat
        parallel:
            pause 1.2
            ease 0.2 ypos 1.07
            ease 0.2 ypos 1.1
            repeat

    misty @surprised "Uh... are you {i}actually{/i} talking to my Psyduck?"

    red @happy "Nah, just messing with you."

    misty @angry "Ugh! Get serious, you jerk!"

    red @happy "Sorry, sorry."

    pause 1.0

    misty @sad "Well? What's wrong with him?"

    pause 1.0

    red @closedbrow talking2mouth "I mean... I'm not a doctor or a psychologist or anything. Professor Oak would actually be the perfect person to talk to about this."
    red @closedbrow talking2mouth "He's a Poké-homo Psychosociologist, after all. Human-Pokémon relationships are literally his field of study."
    red @talking2mouth "But, if I were to give my best guess, Psyduck feels like you don't love him."

    pause 1.0

    misty @angry "Dummy! That's exactly what Alder said! If you're not going to tell me anything useful or new, what are you even doing here?"

    red @closedbrow talking2mouth "That's not exactly what Alder said. Alder said you don't give your Psyduck enough attention. But I've been hanging out with you for a while, and I'm not sure that's entirely correct."

    misty @surprised "Huh?"

    red @talking2mouth "Misty, I think you {i}do{/i} give your Pokémon attention. But I don't think it's positive attention."

    misty @surprised "What?"

    red @closedbrow talking2mouth "Maybe I'm making some assumptions here, but you {i}do{/i} love your Pokémon, right?"

    misty @angry "Of... of course! I'm a bitch, not {i}evil{/i}."

    red @closedbrow talking2mouth "I really wish you wouldn't call yourself that. But that's not the point. The point is, well..."
    red @talkingmouth "Misty, do you treat your Pokémon, even a little bit, like you treat people?"

    pause 1.0

    show misty sadbrow with dis

    misty @sadmouth "I..."

    pause 1.0

    red @closedbrow talking2mouth "Pokémon tend to act very still and quiet around me. They usually just sit at my feet and wait for my orders. But what's your Psyduck doing?"

    misty @angry "Just... running around randomly?"

    red @talkingmouth "Not exactly."

    misty @closedbrow talkingmouth "Fine, what?"

    red @happy "How about you walk over here?"

    misty @angry "What kind of dumb game is this?"

    red @sadbrow talkingmouth "Humor me?"

    misty @closedbrow talkingmouth "Ugh... fine."

    show misty:
        ease 1.0 xpos 0.25

    pause 2.0

    show sideportraitfull:
        ease 0.2 xzoom 1
        pause 1.0
        ease 0.2 ypos 1.05
        ease 0.2 ypos 1.1
        parallel:
            ease 1.0 xpos .15
            ease 1.0 xpos .25
            ease 1.0 xpos 0.35
            ease 1.0 xpos 0.25
            repeat
        parallel:
            pause 0.8
            ease 0.2 xzoom -1
            pause 1.0
            pause 0.8
            ease 0.2 xzoom 1
            pause 1.0
            repeat
        parallel:
            pause 1.2
            ease 0.2 ypos 1.07
            ease 0.2 ypos 1.1
            repeat

    pause 2.0

    red @happy "See?"

    misty @talkingmouth "He's... following me?"

    red @talkingmouth "He's showing off."

    misty @surprised "Huh?"

    red @happy "Your Psyduck is going through its paces. It's shadowboxing, it's working on its footing."

    red @talking2mouth "It's trying to show you that it'll fight for you. I mean, it lets itself out of its own Poké Ball--so it can {i}literally{/i} fight for you."

    red @talking2mouth "Yeah, it might look a bit silly, like it's bouncing around aimlessly, but there's a thinking brain, and a feeling heart, in that duck."

    pause 1.0

    $ PlaySound("pokemon/cries/54.mp3")
    $ PlaySound("pokemon/ball sound.ogg")

    show sideportraitfull at backinpokeball:
        zoom 0.8

    pause 2.5

    show misty:
        ease 0.5 xpos 0.5

    misty @talking2mouth "Oh."

    red @closedbrow talking2mouth "Misty, you know that your attitude drives people away. And that's fine, I'm sure you've got a reason for not wanting anyone to get close to you. But you can't do that to your Pokémon. They're innocent."

    misty @sad "{size=30}I mean, so are you...{/size}"

    pause 1.0

    red @confusedeyebrows frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    red @closedbrow talking2mouth "That's another thing. {w=0.5}{nw}"

    show misty surprisedbrow frownmouth with dis

    extend "People can hear you when you mutter under your breath."

    misty "Wha-{w=0.5}wha-{w=0.5}wha-{w=0.5}"

    red @confused "C'mon. You know people can. So you're, like, trying to let people know you don't {i}actually{/i} hate them. But you feel like you can't do it outright, for some reason."

    misty -surprisedbrow -frownmouth -surprised @closedbrow talking2mouth "Mmmmph."

    pause 1.0

    misty @angry "You... jerk! Dummy! Idiot! What are you even doing here? Just walking into my life and telling me I need to change who I am?!"

    red @closedbrow talking2mouth "No. I'm telling you you need to {i}show{/i} who you are."

    misty @talkingmouth "Or what?"

    red @confused "...Well, you'll, uh, have a pretty hard time making friends. I mean, maybe you don't care about that, but... I think you do? Correct me if I'm wrong."

    misty @angry "You're wrong! Wrong, wrong, very wrong!"

    red @happy "Ah, alright, then! My bad."

    call clearscreens from _call_clearscreens_59

    show misty surprisedbrow frownmouth with dis

    show blank2 with Dissolve(2.0)

    hide blank2

    show screen currentdate

    misty sadbrow @sad "W-wait!"

    red @confused "Yeah?"

    pause 1.0

    misty @sad "Uh... what if... Like, what if you weren't completely wrong? What do I do to fix this? {w=0.5}{size=30}To fix me?{/size}"

    pause 1.0

    red @happy "Oh, I have no idea."

    misty @angry "Wha--well, what good are you?!"

    red @talkingmouth "Look, I'm not a therapist. Whatever's made you feel like you need to be hostile and argumentative all the time isn't something I can figure out in a twenty-minute chat."

    pause 1.0

    red @confused "Scratch that, a thirty-minute chat. Wow, we've really been going on at it, haven't we?"

    pause 1.0

    misty @talkingmouth "...Why do you know all this? All this stuff about me? And about how I treat people?"
    misty @sad "I've been trying to put my problem into words for... years. Ever since I was a child. But you just walked in here and told me what was wrong."

    red @closedbrow talking2mouth "Well... you're kinda like your Psyduck, I think."

    misty @surprised "Huh?"

    red @closedbrow talking2mouth "You know. Acting out for attention."

    misty @angry "Hey!"

    red @talkingmouth "It reminds me of an old friend of mine. He felt like he had to do more and more outrageous things to stand out."

    $ ValueChange("Blue", 3, -0.5)

    red @closedbrow talking2mouth "Actually, I think I get him a bit more now... He definitely wanted his grandpa's attention."
    red @closedbrow talking2mouth "So... is there anyone out there whose attention you're specifically trying to get?"

    pause 1.0

    misty @closedbrow talking2mouth "God, this is so stupid."
    misty @talkingmouth "Look, my parents--"

    red @surprised "Wait! Hold on! I have something for this."

    pause 1.0

    red glasses @talkingmouth "Dr. [last_name] is ready."

    pause 1.0

    misty @talkingmouth "Where did you get those?"

    red @happy "Bianca gave them to me. She had some extras."

    pause 1.0

    misty angry "UGH! You {i}idiot!{/i} I thought you were going to take me seriously, but you're just making a big joke out of this, like everyone else!"

    misty "You... {w=0.7}{nw}"

    show blank2 behind pool

    $ PlaySound("Slap.ogg")
    pause 0.1

    show misty:
        xpos 0.5 ypos 1.0 zoom 1.0 rotate 0
        ease 0.2 xpos 0.25 ypos 1.1 zoom 1.33 rotate -3

    show pool at hall_move1

    extend "jerk!{w=1.0}{nw}"

    show misty:
        xpos 0.25 ypos 1.1 zoom 1.33 rotate -3
        ease 0.4 xpos -0.5 ypos 1.0 zoom 1.25 rotate 0

    show pool at hall_move2

    red @closedbrow talking2mouth "...Okay. Yeah, that one was a little on me. Maybe not the time for a bad joke."

    show misty:
        ease 0.5 xpos 0.25

    misty @angry "When you feel like taking me {i}seriously{/i}, give me a call, you {nw}"

    $ PlaySound("Slap.ogg")

    show misty angry:
        xpos 0.25 ypos 1.0 zoom 1.0 rotate 0
        ease 0.2 xpos 0.5 ypos 1.1 zoom 1.33 rotate -3

    show pool at hall_move1

    extend "{color=#0048ff}jerk{/color}!{w=1.0}{nw}"

    show misty angry:
        xpos 0.5 ypos 1.1 zoom 1.33 rotate -3
        ease 0.4 xpos 1.5 ypos 1.0 zoom 1.25 rotate 0

    show pool at hall_move2

    red @angry "Now, see, that-- {size=40}{i}that{/i} was excessive!{/size}"

    pause 1.0

    redmind @thonk "What did she just throw at me...?"

    $ BecomeContacted("Misty")

    redmind @closedbrow frownmouth "Of course."

    $ persondex["Misty"]["Relationship"] = "Jerk"
    $ persondex["Misty"]["RelationshipRank"] = 1

    $ renpy.music.set_volume(0.1, delay=0.0, channel="music")
    $ PlaySound("sav.ogg")
    $ renpy.music.set_volume(1.0, delay=1.0, channel="music")

    narrator "Your heart shifts as you feel your relationship with Misty evolve from '{color=#0048ff}Classmate{/color}' to '{color=#0048ff}Jerk{/color}'!"

    pause 2.0

    red @talkingmouth "...Damn, I look good in glasses. Shame I can't see anything."

    return

label Misty2:
    scene pool 
    show misty swimsuit wetbody closedbrow smilemouth:
        ypos 1.0
        block:
            ease 5.0 ypos 1.05
            ease 5.0 ypos 1.0
            repeat
    with Dissolve(2.0)
    queue music "Audio/Music/CeruleanCity.ogg"

    pause 2.0

    redmind @thinking "I thought I'd find her here..."
    if (GetRelationshipRank("Rosa") > 0):
        redmind @confusedeyebrows closedeyes frownmouth "What was it that that detective said in {i}Provoked{/i}? 'They always return to the scene of the crime?'"

    show blank 
    hide misty
    hide pool
    with Dissolve(1.0)

    show pool behind blank at sepia 
    show misty behind blank at sepia
    show flashback behind blank

    hide blank with Dissolve(2.0)

    misty @closedbrow talking2mouth "God, this is so stupid."
    misty @talkingmouth "Look, my parents--"

    red sepia @surprised "Wait! Hold on! I have something for this."

    pause 1.0

    red glasses @talkingmouth "Dr. [last_name] is ready."

    pause 1.0

    misty @talkingmouth "Where did you get those?"

    red @happy "Bianca gave them to me. She had some extras."

    pause 1.0

    misty angry "UGH! You {i}idiot!{/i} I thought you were going to take me seriously, but you're just making a big joke out of this, like everyone else!"

    misty "You... {w=0.7}{nw}"

    show blank2 behind pool

    $ PlaySound("slap.ogg")

    pause 0.1

    show misty:
        xpos 0.5 ypos 1.0 zoom 1.0 rotate 0
        ease 0.2 xpos 0.25 ypos 1.1 zoom 1.33 rotate -3

    show pool at hall_move1
    show flashback at hall_move1

    extend "jerk!{w=1.0}{nw}"

    show misty:
        xpos 0.25 ypos 1.1 zoom 1.33 rotate -3
        ease 0.4 xpos -0.5 ypos 1.0 zoom 1.25 rotate 0

    show pool at hall_move2
    show flashback at hall_move2

    red @closedbrow talking2mouth "...Okay. Yeah, that one was a little on me. Maybe not the time for a bad joke."

    show misty:
        xpos -0.5 ypos 1.0 zoom 1.25 rotate 0

    misty @angry "When you feel like taking me {i}seriously{/i}, give me a call, you {nw}"

    $ PlaySound("slap.ogg")

    show misty angry:
        xpos 0.25 ypos 1.0 zoom 1.0 rotate 0
        ease 0.2 xpos 0.5 ypos 1.1 zoom 1.33 rotate -3

    show pool at hall_move1
    show flashback at hall_move1

    extend "{color=#0048ff}jerk{/color}!{w=1.0}{nw}"

    show misty angry:
        xpos 0.5 ypos 1.1 zoom 1.33 rotate -3
        ease 0.4 xpos 1.5 ypos 1.0 zoom 1.25 rotate 0

    show pool at hall_move2
    show flashback at hall_move2

    red @angry "Now, see, that-- {size=40}{i}that{/i} was excessive!{/size}"

    pause 1.0

    redmind @thonk "What did she just throw at me...?"

    pause 1.5

    scene pool 
    show misty swimsuit wetbody closedbrow smilemouth:
        ypos 1.0
        block:
            ease 5.0 ypos 1.05
            ease 5.0 ypos 1.0
            repeat
    with Dissolve(1.0)

    pause 2.0

    redmind @confusedeyebrows frownmouth "It's amazing the difference that not screaming at me, or slapping me, makes."

    red @happy "Hey, Misty!"

    misty @surprised "Huh?! What are you--"

    misty angry anger "You--"

    show flashback with Dissolve(1.0)

    show misty:
        ease 10.0 ypos 1.3 zoom 1.4

    narrator "Time seems to slow down as Misty's telegraphed slap comes towards you. This time, however, you were expecting it."

    if (GetRelationshipRank("Bea") > 0):
        redmind @frownmouth angrybrow "Alright... what was it that Bea said when we were sparring? Stay aware of your feet, but keep your eye on your opponent's hands. Stepping back is an unbreakable defense. Keep your eye level steady, and..."

    show misty surprisedbrow frownmouth -anger
    hide flashback
    with vpunch

    show misty:
        xpos 0.5 ypos 1.4 zoom 1.0 rotate 0
        linear 0.2 ypos 0.95 zoom 0.95 rotate 1

    misty "Huh?!"

    red @happy "Dodged it!"

    pause 0.5

    red @surprised "Oh, hey, be careful! You're--"

    show misty:
        xpos 0.5 ypos 0.95 zoom 0.95
        ease 0.3 rotate -90 ypos 1.5

    $ PlaySound("splash.ogg")

    pause 0.5

    show pool with vpunch

    pause 1.0

    redmind @unamusedbrow unamusedmouth "I'm going to get blamed for this, somehow, aren't I?"

    show misty -surprisedbrow -frownmouth -surprised:
        ypos 1.5 rotate -90
        parallel:
            ease 1.0 rotate 0
        parallel:
            ease 5.0 ypos 1.05
            ease 5.0 ypos 1.0
            repeat

    pause 2.0

    red @sadbrow talkingmouth "Sorry."

    misty @closedbrow talkingmouth "For what?"

    menu:
        "For pushing you into the pool.":
            $ AddEvent("Misty", "ApologizedForPool")
            misty @angry "Idiot. I'm already in a swimsuit. That's {i}not{/i} what I want you to apologize for."

        "For making fun of you when you were trying to open up.":
            $ AddEvent("Misty", "ApologizedForFun")
            misty @surprisedbrow "{w=0.5}.{w=0.5}.{w=0.5}."
            misty @sad2brow talkingmouth "You remember that, huh?"

            red @sadbrow talkingmouth "Yeah. It's kinda been... biting at me, to be honest."

            misty @closedbrow talkingmouth "Hmph. Good."

            $ ValueChange("Misty", 1)

    red @talkingmouth "Can we talk?"

    misty @closedbrow talkingmouth "I'm not done swimming."

    pause 0.5

    red @talkingmouth "I figured."

    $ PlaySound("Thud.ogg")

    pause 0.15

    show misty surprisedbrow heavyblush with dis

    pause 0.15

    red swimsuithatless "But I came prepared."

    pause 1.5

    red @confused "What? I {i}am{/i} wearing my swimsuit, right?"
    red @downeyes frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
    red @talkingmouth "Yeah, I am."

    misty mediumblush -surprisedbrow @angry anger "Don't just drop your clothes like that. Warn people before you do something like that! Everyone knows this!"

    red @happy "Sorry. Must have slipped my mind."

    pause 1.5

    misty @closedbrow talkingmouth "Fine, then. Get in. Don't just stand on the edge, like some sort of weirdo."

    redmind @sadbrow frownmouth "...I'm really going to have to talk to her about this..."

    $ PlaySound("splash.ogg")

    show misty lightblush:
        parallel:
            ease 2.0 zoom 1.3
        parallel:
            ease 5.0 ypos 1.25
            ease 5.0 ypos 1.2
            repeat

    narrator "You slide into the pool, finding the water soothingly cool."

    misty @talkingmouth "Alright. You said you wanted to talk or whatever. And apparently you thought it was important enough to strip in front of me--"

    red @talking2mouth "Not exactly what happened."

    misty @talkingmouth "So what did you want to talk about?"

    pause 1.0

    red @talkingmouth "A while ago, we met at this pool. You probably remember. We talked about how your Psyduck was acting out for attention."

    misty @closedbrow talkingmouth "That was your theory."

    red @sadbrow talkingmouth "And then we decided that... maybe it's the same way with you?"

    misty @angry anger "That was {i}your{/i} theory!"

    red @closedbrow talking2mouth "And then you were going to tell me about your parents."
    red @unamusedbrow talking2mouth "But... instead, you slapped me twice and threw your phone number at me. Literally threw."

    misty @talkingmouth "Yeah, I remember all this. What's your point?"

    red @talkingmouth "Well, I'd like to know what you were going to say about your parents."

    misty @angry anger "Oh, so {i}now{/i} you care?!"

    pause 1.0

    redmind @thinking "Right. For my own mental health, this is {i}not{/i} tenable. I need to say something."

    menu:
        ">Be sharp":
            show misty sad2brow mediumblush with dis

            $ AddEvent("Misty", "WasSharp")
            red @angrybrow talking2mouth "Misty. Cut it out. I'm here to help you. I care about you. If you keep yelling at me, slapping me, or pushing me away, then I'm leaving."
            red @angrybrow talking2mouth "I'm sorry, but I'm not {i}that{/i} patient. If you want to keep having me as a friend, I need you to meet me at least a third of the way."

        ">Be kind":
            show misty sad2brow with dis

            $ AddEvent("Misty", "WasKind")
            red @sadbrow talkingmouth "Misty... I'm sorry. I really want to help you, because I care about you. But if you keep yelling at me, slapping me, or pushing me away, then I can't do that. And it's not good for me to... spend time with someone who treats me like that."
            red @sadbrow talkingmouth "You're a good person. I know this. And I {i}want{/i} to be your friend. But I can't cross the whole distance just to get slapped again. Please, meet me at least a third of the way."

    misty -sad2brow -mediumblush @talkingmouth "...Okay."

    red @happy "Great! Glad we're on the same page."

    pause 0.5

    red @talkingmouth "So, your parents?"

    misty @closedbrow talkingmouth "...Yeah, alright. But this is a long story." 
    misty @closedbrow talking2mouth "Don't fall asleep, or you'll drown."

    red @happy "Aw, look at that. You're already looking out for {i}me.{/i}"

    misty smilemouth @closedbrow talking2mouth "Hmph."

    pause 1.0

    misty -smilemouth @talkingmouth "I guess you already know I'm from Cerulean City."

    red @talkingmouth "I picked it up, yeah."

    misty @talkingmouth "Well... I'm not {i}just{/i} from Cerulean. I'm from the Cerulean Gym."

    red @surprised "No way? Were you a kid of the Gym Leader?"

    misty @sad2brow talkingmouth "...I {i}was{/i}."

    red @sadbrow talkingmouth "Oh. Past tense. That's not good."

    misty @closedbrow talkingmouth "My three older sisters are all a year older than me. They're triplets." 

    if (IsAfter(29, 1, 2005)):
        misty @talkingmouth "So, they're twenty."
    else:
        misty @talkingmouth "So, they're nineteen."

    misty @sad2brow talkingmouth "I only turned eighteen a couple months before the school year began..."
    misty @talkingmouth "But when {i}they{/i} turned eighteen, my parents left."

    pause 1.0

    red @surprised "Come again?"

    misty @closedbrow talkingmouth "You heard me! They just... they just {i}left!{/i} They thought that since I had three older sisters that were all 'legal adults', that they didn't need to be around any more."

    pause 1.0

    show misty sad2brow with dis

    red @confusedeyebrows talking2mouth "Wow. Dicks."

    pause 0.5

    red @sadbrow talkingmouth "Sorry. Is that not what you wanted me to say?"

    misty -sad2brow @sadbrow talkingmouth "...I don't know. I hate them for leaving. Some lame excuse about how they wanted to 'see the world'... how they didn't want to be 'tied down', and they were tired of 'raising children'..."
    misty @sadbrow talkingmouth "But... It's not easy to hate them."

    red @sadbrow talkingmouth "...I understand. People who leave their families... I can't imagine doing that."

    misty @sad2brow talkingmouth "I guess you've got a perfect one, then? Nothing exciting happening down in Pattel?"

    show misty surprisedbrow with dis

    red @sadbrow talking2mouth "Pallet. And... not exactly. My father's dead. He died in the Cinnabar explosion. It's just my Mom and I."

    misty -surprisedbrow @sad2brow talking2mouth "Well, now I look like a bitch for complaining that {i}my{/i} parents just decided to leave..."

    red @sadbrow talkingmouth "I think two things can be sad at once."

    misty @talkingmouth "...I guess."

    pause 1.0

    misty @talkingmouth "Before they left, though... I always thought that they paid more attention to my sisters than me." 
    misty @talkingmouth "Whenever they wanted to go somewhere, they got what they wanted. We went to the schools they preferred, we bought from the stores they liked..."

    pause 0.5

    red @sadbrow talkingmouth "Just playing Giratina's advocate here, but... there {i}were{/i} three of them compared to one of you, right?"

    misty @angry "That doesn't matter! They're... they're like... they're a single unit! You'd understand if you met them!"
    misty @talkingmouth "But they would always act like {i}I{/i} was the one taking things from them... they acted like they were jealous of me, even though I was always the fourth one in line."
    misty @sad2brow talkingmouth "And then my parents left. And it's not like I had a chance to tell them how I felt before then. I mean, kids can't put this stuff into words, you know?"

    red @sadbrow talkingmouth "Yeah. I understand."

    misty @sadbrow talkingmouth "I grew up around Water-types. I've pretty much only ever handled Water-types. At Kobukan, I took the Ice elective... but that's only because I'd used Water/Ice types before, back home."
    misty @angrybrow talkingmouth "This Water-type gym is our family's future. It's everything we've got left, after our parents."
    misty @sadbrow talkingmouth "It's the biggest business in Cerulean. My sisters have made it incredibly popular. We host events, shows, even weddings... it's the jewel of Cerulean."
    misty @sadbrow talkingmouth "But... when I graduate... I know exactly what'll happen. And that'll be the end."

    pause 0.5

    misty @closedbrow talkingmouth "...So, yeah, maybe your idea that I'm 'acting out for attention' or whatever isn't {i}completely{/i} wrong."

    pause 0.5

    misty @angry "Even if you're right, that still doesn't help me get my Psyduck under control, though!"

    python:
        PlaySound("Pokemon/Ball sound.ogg")
        PlaySound("pokemon/cries/54.mp3")
        sidemonnum = pokedexlookupname("Psyduck", DexMacros.Id)

    sidemon "Psy?!"

    misty @closedbrow talkingmouth "Yeah. I'm talking about {i}you{/i}."

    pause 1.0

    misty @talkingmouth "He'd be a good gym Pokémon, but I don't think he has what it takes for contests..."

    narrator "Misty's Psyduck paddles frantically in the water, before Misty scoops him up and puts him on the side of the pool."

    misty @talkingmouth "Idiot duck. Can't even swim without a floaty."

    pause 1.5

    red @talkingmouth "You mentioned contests?"
    red @happy "Tell me about that."

    misty @sad2brow talkingmouth "Not much to say. I like singing. Water's an easy type to do well with in contests. I just had a couple of advantages."
    misty @closedbrow talking2mouth "When my sisters attended Kobukan, they were the top act of the Coordinator Club."
    misty @angry "Whenever they didn't place first, it was because {i}another{/i} coordinator cheated."

    if (IsBefore(28, 5, 2004)):
        if (HasEvent("Klara", "AcceptCoordinatorClub")):#FIX THIS: If you have the chance to see more coordinator club meetings
            red @talkingmouth "...I saw you during that Coordinator Club meeting. You're a good singer."

            $ ValueChange("Misty", 1)

            misty @closedbrow talkingmouth "Yeah. They're alright. Mostly. Lisia clearly knows what she's doing."

        elif (HasEvent("Dawn", "BirthdayTheater")):
            red @talkingmouth "...I saw you at the theater in Inspira. You're a good singer."
            
            $ ValueChange("Misty", 1)

            misty @closedbrow talkingmouth "It's a hobby. It gets me some extra money. Not something I like to spread around, though."
            misty @closedbrow talking2mouth "Lisia wouldn't want me 'revealing my routines' to other people, anyway..."
            
        elif (IsAfter(24, 5, 2004)):
            red @talkingmouth "I saw you with the rest of the Coordinator Club at lunch."

            misty @closedbrow talkingmouth "Yeah. They're alright. Mostly. Lisia clearly knows what she's doing."

    else:
        misty @talkingmouth "I call them once in a while. They're pretty jealous that I'm getting taught by Lisia. They only had instructor Juan, last year..."

    red @talkingmouth "What do you think of Lisia?"

    misty @surprised "Huh? She's World Contest Champion. What else is there to say about her?"

    red @happy "Ah, just wondering. It's crazy to me that we have an actual World Champion of {i}anything{/i} at this school."

    misty smilemouth @smugbrow smugmouth "This is {i}the{/i} place for World Champions. I'm not surprised at all."

    red @happy "Well, aren't {i}you{/i} fancy, city girl?"

    misty @closedbrow talking2mouth "Hmph."

    pause 1.0

    misty @talkingmouth "Not so fancy now. I'm getting pruney. I should get out and dry off."

    red @talkingmouth "Sure."

    $ PlaySound("splash.ogg")

    show misty:
        ease 0.5 ypos 1.0 zoom 1.0

    narrator "You follow Misty up the ladder and get out of the pool."

    red @talking2mouth "Didn't bring a towel?"

    misty @closedbrow talkingmouth "Nah. Towels are often made of synthetics that stick to you, degrade, and can get in Pokémon-safe water, ruining it."

    red @talkingmouth "Hm."

    misty @talkingmouth "Hand me my jacket?"

    red @talkingmouth "Sure."

    show misty jacket with dis

    pause 1.0

    misty @surprisedbrow talkingmouth "What are you looking at me like that for?"

    red @talkingmouth "I think I get it."
    red @happy "And by 'it', I mean you. I think I understand you!"

    misty @sadbrow talking2mouth "Great, all my problems are solved."
    misty surprisedbrow -smilemouth @neutralbrow talkingmouth "What do you think you get?"

    red @talkingmouth "Well, based on what you've said... you care a lot about Pokémon conservation, but your gym back home is a massive business."

    show misty sadbrow with dis

    red @talkingmouth "You like contests--that's your true passion. You want to follow in your sisters' footsteps, and be a great coordinator."

    show misty sad2brow with dis

    red @sadbrow talkingmouth "But when you graduate, you're going to have to run that very same gym, right? Your sisters are going to force it on you, like your parents forced you on your sisters."
    
    show misty closedbrow angrymouth with dis
    
    red @sadbrow talkingmouth "And that's going to be what you have to do for the rest of your life..."

    pause 1.0

    show misty cry2 with dis:
        xpos 0.5
        block:
            linear 0.1 xpos 0.49
            linear 0.1 xpos 0.51
            repeat 5
        pause 1.0
        xpos 0.5

    red @sadbrow talking2mouth "I guess..."

    show misty angry anger with vpunch
    
    misty "No! You... you... you... {i}idiot!{/i} That's the complete opposite of everything that I feel! You don't understand even a single thing about me! You {i}don't{/i} understand! {size=40}{i}Nobody understands!{/i}{/size}"

    show misty:
        xpos 0.5 
        ease 0.3 xpos -0.1

    pause 2.0

    red @surprised "...What?"
    red @sadbrow talkingmouth "But... I thought, that..."

    pause 1.0

    red @sadbrow talkingmouth "I'm... I'm so confused."

    pause 1.0

    $ AddEvent("Misty", "Scene2Part1")

    narrator "It seems your understanding of Misty cannot increase at this time..."

    if (GetMood("Misty") > -4):
        $ mood = GetMood("Misty")
        $ persondex["Misty"]["Mood"] = -4
        $ AddEvent("Misty", "FormerMood" + str(mood))
        narrator "Misty's mood has fallen to {color=#f00}{i}Unhappy.{/i}{/color}"

    narrator "[bluecolor]Perhaps you should text her when you get the chance.{/color}"

    return

label Misty2Part2:
    if sceneviewer:
        $ texting = True
        call clearscreens() from _call_clearscreens_238
        if (IsBefore(5, 5, 2004)):
            scene dorm_B norm with Dissolve(2.0)
        else:
            scene bedroommidnight with Dissolve(2.0)
        queue music "Audio/Music/Road to Viridian City.ogg"
        if (IsBefore(5, 5, 2004)):
            redmind casual "...I should text someone before I head to bed."
        else:
            redmind casual night "...I should text someone before I head to bed."
        show phone_B behind blank2
        show phone_A behind blank2
        with fadeinbottom
    show misty sad2brow behind phone_A with fadeinbottom 

    misty "hi"
    misty "kinda blew up at you huh?"
    misty "sorry."
    misty "its jsut that"
    misty "everyone thinks that."
    misty "*just"
    misty "and its not true"
    misty "i love the gym. i love it more than anything else"
    misty "but"
    misty "i know i'll never be a part of it."
    misty "that kills me."

    pause 1.0

    misty "sory for traumadumping"
    misty "*sorry"

    pause 1.0

    hide phone_A
    hide phone_B
    hide misty 
    with fadeoutbottom

    narrator "Misty's status light disappears, indicating she's settled in for the night... Perhaps you should leave her be."

    pause 2.0

    $ PlaySound("vibrate.ogg")

    narrator "Oh? A new text?"

    show phone_B
    show phone_A
    with fadeinbottom

    show phone_C behind phone_A with dis

    show phone_msg1 behind phone_A with dis
        
    $ title = Text("SHE GOT HANDS",size=30,font="fonts/consola_0.ttf",color="#313131")

    image msg5 = Text("ur [bluecolor]not a jerk{/color}\njust an fyi",size=21,color="#ffffff",line_spacing=5,text_align=0.0)

    show text title behind phone_A:
        xalign 0.51 yalign 0.34
    show msg5 behind phone_A:
        xpos .41 ypos .4
    with dis

    pause

    scene blank2 with splitfade
    
    python:
        for event in persondex["Misty"]["Events"]:
            if "FormerMood" in event:
                eventlevel = int(event.replace("FormerMood", ""))
                if (eventlevel > -2):
                    persondex["Misty"]["Mood"] = 0
                    MoodChange("Misty", eventlevel + 2)
        renpy.say(None, "Misty's mood has been restored, and...")
        RelationshipRankUp("Misty", "Not a Jerk", 2)
        AddEvent("Misty", "Misty2Part2")

    return