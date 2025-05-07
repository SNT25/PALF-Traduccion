label Dawn1:
    if (not IsBefore(1, 5, 2004)):
        $ persondex["Dawn"]["Events"].append("Level2SceneVer2")

    scene lobby 
    show dawn thinking
    with Dissolve(2.0)
    $ renpy.music.queue("Audio/Music/snowpoint.ogg", channel='music')

    if (IsBefore(1, 5, 2004)):
        redmind @thinking "Okay, there's Dawn. From what I know of her, she handles pressure about as well as a frozen-over pond, so I should do my best to not startle her."
    else:
        redmind @thinking "Okay, there's Dawn. Despite how crazy strong she is, she handles pressure about as well as a frozen-over pond, so I should do my best to not startle her."

    red @happy "{size=30}Hi.{/size}"

    show lobby at vpunch

    dawn frownmouth @surprised "A-ah! [first_name]! I didn't see you there."

    redmind @thinking "Well, I tried."

    red @talkingmouth "You looked like you were pretty deep in your thoughts. Penny for one of them?"

    dawn @sadbrow happymouth "Oh. Just, um... thinking about Pokémon. Y'know, same as always."

    red @happy "Really? That's so cool! So was I!"

    dawn @angrybrow sadmouth "Wait, you couldn't tell I was lying there?"

    red @surprised "Why would you lie? You're my friend."

    show lobby at vpunch

    dawn surprised "We're f-friends?! I'm sorry, this is all moving way too fast! I- I- I-"

    show lobby with vpunch

    dawn closedbrow angrymouth "{size=40}I need to go!{/size}"

    show dawn:
        ease 0.5 xpos 1.5

    redmind "...Hm."

    $ rantolounge = False

    menu:
        ">Run after her":
            $ rantolounge = True
            scene lounge with splitfadefaster

            show dawn surprisedbrow frownmouth with dis

            dawn "Ah-ah...!"

            red @talking2mouth "Why are you running?"

            dawn "Ahhhh!"

            red @angrybrow talking2mouth "{i}Why{/i} are you running?"

            dawn sad "I...{w=0.5} I...{w=0.5} I don't knoooow!"

        ">Wait for her to come back":

            redmind ".{w=0.5}.{w=0.5}.{w=0.5}"

            pause 2.0

            show dawn frownmouth:
                ease 1.5 xpos 0.75

        ">Call out to her":
            red @talkingmouth "Wait, Dawn. Please. I'm just trying to talk with you. I can slow things down."

            pause 2.0

            show dawn frownmouth:
                ease 1.5 xpos 0.75

    red @sadeyes sadeyebrows happymouth "C'mon. Let's talk, Dawn. Just talk. It doesn't have to be about Pokémon."

    if (not IsBefore(1, 5, 2004)):
        red @happy "I mean, I'm {i}dying{/i} to find out what's the whole deal with your Mega Altaria--and the fact you {i}fought Cynthia?!{/i}"

        pause 1.0

        red @sweat sadbrow talkingmouth "But... I mean, from our battle in the Quarter Qlash's third round, it's pretty clear that that might not be an easy topic."

    red @happy "Though I'm pretty bad at talking about anything that {i}isn't{/i} about Pokémon, fair warning."

    dawn -sad frownmouth @closedbrow talking2mouth "{size=30}You and {i}everyone{/i} else.{/size}"

    red @talking2mouth "...Mind if I ask the obvious question?"

    dawn @closedbrow talking2mouth "No..."

    red @closedbrow talking2mouth "How come you don't like Pokémon?"

    dawn @sadbrow happymouth "I don't know. I don't {i}dislike{/i} them. And the ones I have, I love. They're my best friends."

    red @talking2mouth "I sense a large 'but' approaching."

    dawn @sad "Yeah. But everything that makes other people excited about them, I just don't get. Contests are fine. Battles are fine."

    if (not IsBefore(24, 4, 2004) and IsBefore(1, 5, 2004)):
        dawn @sad "I mean, even though Janine's forced me into the Battle Team... I don't really hate that, even."

    dawn @sadbrow happymouth "But none of that feels... like 'it,' for me. None of that's what I want to do with my life."

    red @surprised "You're here in Kobukan, though?"

    dawn @sad "Yeah, my mother, Johanna, is a pretty famous contest star in Sinnoh. She... doesn't like what I spend my free time doing. She was hoping that Kobukan might change my mind about Pokémon."

    red @closedbrow talking2mouth "Hm. What do you spend your free time doing?"

    show dawn sad with dis

    pause 1.0

    red @surprised "Woah, hey, you don't have to tell me! I mean, if it's embarrassing or something."

    dawn -sad frownmouth @sadbrow happymouth "I... I don't know. I kinda want to tell {i}someone,{/i} but right now, nobody at Kobukan knows except Instructor Melony."

    red @happy "Well, I'll be here if you decide you want to tell me later."

    dawn @talkingmouth "Al... alright." 

    dawn @happy "Thank you."

    dawn @happy "It's um, alright, I guess, if you want to call yourself my friend. I mean, I wouldn't.{nw}" 
    extend @surprised " Because I can't. I mean, you can't be your own friend. Well maybe you can, but I can't. Oh god, I'm rambling."

    dawn @angry "The point is we're friends now! For real! Two-way street!"

    red @surprised "Really?"

    if (IsBefore(1, 5, 2004)):
        dawn @closedbrow talking2mouth "Yeah. For some reason, I... I trust you. So you're my {color=#0048ff}trusted friend{/color}."

    else:
        dawn @closedbrow talking2mouth "Yeah. It's probably just because of your power, but... I... I trust you." 
        dawn @sadbrow happymouth "Well, maybe not entirely because of your power. I really appreciate what you did for me in the Quarter Qlashes. I can't stop thinking about that battle..."
        dawn @closedbrow talking2mouth "So you're my {color=#0048ff}trusted friend{/color}."

    $ renpy.music.set_volume(0.1, delay=0.0, channel="music")
    $ PlaySound("sav.ogg")
    $ renpy.music.set_volume(1.0, delay=1.0, channel="music")

    narrator "Your heart shifts as you feel your relationship with Dawn evolve from '{color=#0048ff}Classmate{/color}' to {w=0.5}{nw}"

    if (rantolounge):
        show lounge with vpunch

    else:
        show lobby with vpunch

    dawn surprised "W-wait!"

    dawn @closedbrow sadmouth "I- I- I- I want to show you! What I do in my free time! I changed my mind. Which is why I want to show you now."
    dawn -surprisedbrow -frownmouth -surprised @sad "P-please...?"

    red @happy "Hey, you can show me anything."

    dawn @closedbrow talking2mouth "Okay. Now, how do I take you there without you knowing how to get back there? Do I have a blindfold or anything?"

    red @happymouth shadow noeyes noshine "Hm... I could just wear my cap really low, so it covers my eyes."

    dawn @angry "Stop making fun of me!"

    red @happy "Sorry. But you already said Instructor Melony knows about this. So I figure that it's her classroom, right?"

    if (classstats["Ice"] == 0):
        red @surprised "I mean, I've never been to her class, but I'm pretty sure I can just look it up on the school website."

    dawn @closedbrow talking2mouth "Oh. Um... yes. {size=30}Good going, Dawn.{/size}"

    red @happy "Alright, let's go."

    if (rantolounge):
        scene lounge
        show blank2 
        with splitfade

    else:
        scene lobby
        show blank2 
        with splitfade

    show classroom behind blank2
    show icetype behind blank2
    show iceglow behind blank2:
        alpha 0.5 xalign 0.5 yalign 1.0
        block:
            ease 2.0 alpha 0.25
            ease 1.8 alpha 0.7
            repeat

    hide blank2 with splitfade

    if (classstats["Ice"] > 0):
        red @surprised "Brr. I'll never get used to how cold Instructor Melony keeps her classroom. It's like the top of a mountain!"
    else:
        red @surprised "Brr. It's really chilly in here. It's like the top of a mountain!"

    red @confusedeyebrows talking2mouth "Hey, how come you're not cold?"

    dawn @talkingmouth "Well, I grew up in Snowpoint City, in Sinnoh."

    red @closedbrow talking2mouth "Hm. I'm not familiar, but I think the name tells me everything I need to know."

    redmind @thinking "Still, you're showing quite a bit of leg for someone stepping into a freezer."

    narrator "Dawn goes to the back of the classroom and unlocks a door. A moment later, she begins wheeling something out on a cart, with visible effort."

    show dawn:
        xpos -0.2
        ease 7.0 xpos 0.45

    show altariasculpture behind dawn:
        xpos -0.7 zoom 2.0 yanchor 1.0 ypos 1.2 alpha 0.95
        ease 7.0 xpos 0.3

    pause 5.0

    red @surprised "Holy shit."

    narrator "You stare at a massive ice sculpture, an almost perfect replica of a Mega Altaria."

    if (IsBefore(1, 5, 2004)):
        red @surprised "That's insane. How long did that take?"

    else:
        red @surprised "That's insane. It looks {i}exactly{/i} like your Altaria. How long did that take?"

    dawn @happy "About nine days. I'm kinda proud of it."
    dawn @angry "Some of the details are a bit off, and I don't like the lack of definition between the Altaria's tail and wingfeathers."
    dawn @sadbrow angrymouth "Also, her claws totally have the wrong texture. Her beak looks more like a Staraptor's."
    dawn @sad "It's pretty much just a bad copy of D'Gelato's work from the 1700s. And I had to make the tail way thicker to work as a base, so--"

    show dawn surprisedbrow frownmouth
    show classroom
    show icetype
    with vpunch

    red @happy "It's beautiful!"

    dawn "I... wha... really?"

    red @happy "I don't know art, but that's it, right there. You should be very proud. And that should be very public! Like, display it in the gardens, or something!"

    dawn -surprisedbrow -frownmouth -surprised @sad "...It'd melt."

    red @closedbrow talking2mouth "Oh, yeah. Uh, what do you do with a sculpture after you finish it?"

    dawn @closedbrow talking2mouth "Back home, I'd just put it outside."

    dawn @sadbrow happymouth "I guess, here at Kobukan, I'll just put it in Instructor Melony's storage closet forever."

    red @closedbrow talking2mouth "Hm... well, maybe we'll think of something better to do with it later."

    red @happy "So, what's next?"

    dawn @sadbrow talking2mouth "Well... I still need to study feather textures more, but, um, I was kinda thinking about doing something with food, but..."

    dawn @surprised "What are you doing?"

    red @shadow noeyes noshine talkingmouth "Huh? What do you mean?"

    dawn "That thing with your hat. What're you doing with your hat?"

    red @shadow noeyes noshine talkingmouth "Oh, just lowering it. Your statue is so bright, it's kinda glaring in my eyes. If I lower my hat, I can--"

    dawn angrybrow surprisedmouth "Don't move!"

    red @shadow noeyes noshine surprisedmouth "Huh?"

    dawn happymouth "Yes, that's great! Now, keep your arm just like that. Twist your head a bit to the side..."

    red @confusedeyebrows shadow noeyes noshine talking2mouth "Okaaaay?"

    dawn @closedbrow talkingmouth "Not quite. What was it you said before? That this room was like the top of a mountain? ...No, no, you need to be higher. Um... can you get on top of that desk for me?"

    red @confusedeyebrows shadow noeyes noshine talking2mouth "Just, like, climb up? Uh, sure."

    dawn "Yes, almost there. The trainer standing on top of the mountain, hat lowered, unphased by the freezing winds..."

    redmind @shadow noeyes noshine frownmouth "Actually, I'm very phased."

    dawn "...What do you say to that?"

    red @shadow noeyes noshine frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    dawn @happy "I got it! Yes, perfect! '...' is {i}perfect{/i}!"

    red @shadow noeyes noshine talkingmouth "Uh... great. I feel kinda ridiculous, though. (And cold.)"

    dawn happy "Don't! You look... so inspiring! Yeah, this--you'll be my next piece!"

    dawn sad "...Um, with your permission?"

    red @shadow noeyes noshine happymouth "Pfft. If you look at me like that, I can't say no to you. Besides, I've always wanted to be an artist's muscle."

    dawn happy @surprised "Muscle?"

    red @surprisedeyebrows shadow noeyes noshine surprisedmouth "Yeah, isn't that what you call someone who inspires an artist?"

    dawn @happy "...You're thinking of a 'muse,' [first_name]."

    red @surprisedeyebrows shadow noeyes noshine surprisedmouth "Oh."

    pause 2.0

    red @confusedeyebrows shadow noeyes noshine talking2mouth "Can I get down, now? My arm's cramping."

    dawn happy "Not yet... my {color=#0048ff}muse{/color}!"

    $ RelationshipRankUp("Dawn", "Muse", 1)

    return

label Dawn2:
    scene classroom 
    show icetype 
    show iceglow:
        alpha 0.5 xalign 0.5 yalign 1.0
        block:
            ease 2.0 alpha 0.25
            ease 1.8 alpha 0.7
            repeat
    show dawn date closedbrow
    with Dissolve(2.0)
    $ renpy.music.queue("Audio/Music/snowpoint.ogg", channel='music')

    dawn @happymouth "Hm, hm, hm...~"

    pause 0.5

    dawn -closedbrow @talkingmouth "Okay! That's enough. I... {i}think.{/i}"

    red @sweat talkingmouth "Thanks. My arms are pretty sore."
    red @talkingmouth "Y'know, when I said I was ready to be your muscle, you corrected me, and said the word was [bluecolor]muse.{/color}"
    red @sadbrow talkingmouth "But I've spent so much time holding poses and flexing, I think being your 'muscle' might have been more accurate."

    dawn @talkingmouth "I... don't think this sculpture should take {i}too{/i} much longer..."

    red @talkingmouth "Great! That means I can see it, right?"

    dawn @talkingmouth "Yep. I think it's time. One second..."

    show dawn:
        xpos 0.5
        ease 0.5 xpos -0.2

    narrator "You absent-mindedly massage your sore muscles as you wait for Dawn to come back." 
    narrator "The two of you have settled into a familiar routine--whenever you have some spare time, Dawn will find you, and you'll sneak off together to the Ice-type classroom."
    narrator "Dawn would then ask you to strike a variety of poses for her, asking you to hold particular positions for a while, while she transferred them to a sketch--which she then supposedly based her sculptures on." 
    narrator "You had never been present for the actual carving of a sculpture, though... Dawn seemed to find the idea terrifying."
    narrator "You also wondered, privately, what the point of all the posing and flexing was, given that you had always stayed {i}fully{/i} dressed throughout the process." 
    narrator "This isn't necessarily something you were disappointed over--but it did raise questions. Some quirk of the artistic process, perhaps."

    dawn "Okay. Um... here it is. Please don't laugh."

    show dawn:
        xpos -0.2
        ease 7.0 xpos 0.33

    show redsculpture behind dawn:
        xpos -0.7 xanchor 0.5 yanchor 0.6 ypos 1.0 alpha 0.95 zoom 0.5
        ease 7.0 xpos 0.66

    pause 8.0

    red @surprisedbrow talking2mouth "Mm?"
    red @surprisedbrow talking2mouth "MMMMMMMMMMMMMM?"

    dawn sadbrow @talkingmouth "What... what noise is that?"

    red @surprisedbrow talkingmouth "Nothing! It's nothing! I... I..."

    dawn frownmouth @sadbrow sadmouth "You... think it's ridiculous."

    red @winkeyes sadeyebrows sweat "I wouldn't say 'ridiculous', but..."

    pause 1.0

    dawn @sadbrow talkingmouth "What's wrong with it?"

    red @sad2brow talking2mouth "I... don't know how to say this, but my crotch has become a cube, my forearms disappeared, and I gained about one hundred pounds of muscle."
    red @closedbrow talking2mouth "Come to think of it, I'm pretty sure I recognize this body..."

    dawn @sadmouth "...Sorry."

    red @sadbrow talkingmouth "It's very flattering. I'm just not sure it's, uh, really 'me'. If 'me' is what you were going for, I mean."

    dawn @sadmouth "Yeah... I was."

    pause 1.0

    dawn @closedbrow talking2mouth "I'm sorry. I... I should've just asked you to take your shirt off. But..."
    dawn @sadbrow talking2mouth "It's... a bit embarrassing."

    show dawn:
        xpos 0.45
        ease 7.0 xpos -0.2
        pause 3.0
        ease 0.5 xpos 0.5

    show redsculpture:
        xpos 0.66 xanchor 0.5 yanchor 0.6 ypos 1.0 alpha 0.95 zoom 0.5
        ease 7.0 xpos -0.2

    dawn @sadmouth "Most sculptors... painters... people like that, {i}real{/i} artists... they work with nude models for a long time before ever trying something like I did."
    dawn @sadmouth "They get used to it. Seeing... 'it', I mean."
    dawn @sad "But I never got the chance to do that. All I've really learned, I just learned from practice... or the occasional video on the internet."

    red @sadbrow talkingmouth "Well, your Altaria sculpture was absolutely amazing."

    dawn @sadbrow talkingmouth "I guess... it's not as embarrassing, asking a Pokémon to undress, hah hah..."

    red @closedbrow talkingmouth "...On the bright side, it shouldn't be too hard to just shave away at the muscle and the cube to just make it smaller. It {i}would{/i} be a problem if you had to make it bigger."

    dawn -frownmouth @sadbrow talkingmouth "Yeah... but I think I'm just going to put this in the freezer."

    red @sadbrow talkingmouth "To keep the Altaria company?"

    dawn @talkingmouth "Yep! We'll just let them chill out together."

    red @happy "Hah."

    red @sadbrow talkingmouth "But, you know, if you wanted to do something {i}more{/i} with these sculptures you spend so long on, then..."

    dawn @angry "[first_name], I told you I don't. We've talked about this."

    red @talkingmouth "Okay, yeah, I know. You don't want to transport them overseas, you don't want to submit them to anything in Inspira, and you don't want to bring them to Unova, because--"

    dawn @closedbrow talkingmouth "Because Sinnohan artists have never won {i}anything{/i} in Unova since the Cold War."

    red @sweat talking2mouth "Right. But what if it wasn't necessarily a competition? I know you aren't great with crowds, or, uh, competition."

    dawn @sadbrow talkingmouth "I... actually don't mind crowds."

    red @surprised "Huh? Really?"

    dawn @talkingmouth "When I was touring the Sinnohan contest circuit... well, if I hadn't gotten used to crowds then, I would've died."
    dawn @happy "No, I'm actually more okay with crowds than one-on-one conversations."

    red @sadbrow talkingmouth "Like the one we're having?"

    dawn @sadbrow talkingmouth "Like the one we're having. When it's a crowd, what you say doesn't really matter, as long as you look like you're doing well. But when it's just one person, your words need to be perfect."

    red @talkingmouth "Well, you're mixing your words up around me less. I hope that means you're feeling more comfortable?"

    dawn @sadbrow talkingmouth "I hope so, too."

    pause 1.0

    dawn @talkingmouth "Um. And... since we're talking about it... I guess I should probably mention I don't really mind competition, either."

    red @happy "Seriously? Man, I was just {i}wrong{/i} on so many counts, then."

    dawn @talkingmouth "It's alright. I get why you'd think that. But I don't mind competing."
    dawn @closedbrow sadmouth "What I don't like is {i}having{/i} to compete. Feeling like I {i}have to{/i} fulfill some sort of 'purpose'... and that purpose is just to beat someone."
    dawn @sadbrow talkingmouth "I'd like to think that Arceus has more in store for me than just beating somebody up. Whether it's in a contest, a battle, or, I guess, an exhibit."
    dawn @closedbrow talking2mouth "Instructor Valerie says that nothing great was ever accomplished by someone who wasn't having fun."
    dawn @sadbrow talkingmouth "I'm not sure if that's completely true... but I know I'm not having fun when I {i}have{/i} to do something, even if it's something I normally enjoy doing."

    pause 1.0

    dawn @happy "That's probably pretty weird, right?"

    red @talkingmouth "Nah. I think a lot of people feel like that. Duty's the death of love."

    dawn @surprised "Hm?"

    red @talkingmouth "Something I read about. Last time we were here, you mentioned that you were pretty inspired by that Sinnohan playwright, right? You even carved a scene from {i}The Red Chain.{/i}" 
    red @happy "I looked into his stories, and... it was pretty heavy stuff. I kinda couldn't get through it. That line stuck with me, though."

    dawn @sadbrow talkingmouth "...I really appreciate you listening to me when I hobby about my blabs."

    pause 1.0

    dawn -sadbrow @angry "Aw! That was almost a whole fifteen minutes!"

    red @talking2mouth "'Blab' is definitely a new one, though. Not sure I've even heard you {i}use{/i} that word before, nevermind mess it up. That's a fun one."

    dawn @angry "Careful. I can still decide to give your sculpture a silly nose."

    red @closedbrow talking2mouth sweat "Noted."
    red @closedbrow talkingmouth "Or should I say 'Nose-d?'"

    dawn @happy "Hah!"

    narrator "You and Dawn eventually get back into a casual conversation, and the topic circles back around to competition. Suddenly, Dawn offers up..."

    dawn @talkingmouth "My philosophy in competition is: 'don't beat your opponent. Beat who you were yesterday.'"

    red @talkingmouth "Hm? That's a pretty good philosophy, sure."

    dawn @sadbrow talkingmouth "It's what Cynthia said to me after she beat me."

    red @closedbrow talking2mouth "Oh."

    pause 0.5

    red @sad2brow talkingmouth "Kinda takes on a different tone, knowing it came from {i}her{/i}, then."

    dawn @sadbrow talkingmouth "Yeah, a little bit. I don't think she's ever had to deal with {i}not{/i} beating an opponent."
    dawn @closedbrow sadmouth "I wonder..."
    dawn @sadbrow talkingmouth "Anyway, I try to follow that philosophy, but it's hard. I actually get kinda competitive."

    red @happy "Oh, I know! I've battled you."

    dawn @talkingmouth "I hope one day it's as easy for me to 'beat myself' as it was for Cynthia."

    red @happy "I'll be there to push you forward 'til that day."
    red @winkeyes talkingmouth "Of course, that doesn't mean you're going to be beating {i}me{/i}."

    if (AimLevel() < 65):
        dawn @closedbrow talkingmouth "We'll see."

        redmind @surprisedbrow frownmouth "Why did I feel a shiver run down my spine...?"
    else:
        dawn @talkingmouth "Maybe not. But I'd like to try."

    pause 1.0

    dawn @closedbrow talking2mouth "What were you trying to convince me of before?"

    red @surprised "Wait, are you thinking--"

    dawn angry "No!"

    pause 1.5

    dawn -angry @sadbrow talkingmouth "Well, {i}maybe{/i}. I want to know what it is first, of course."

    red @happy "Great! It's an art exhibition that Kobukan holds near the end of the year for their more artistic students."
    red @sadbrow talkingmouth "I think there {i}are{/i} prizes, but it's a pretty low-stakes sort of thing."
    
    if (persondex["Instructor Melony"]["Named"]):
        red @talkingmouth "And I talked with Instructor Melony. She says that ice exhibits have been shown before, and there are cooling glass cupboards we can display them in."
    else:
        red @talkingmouth "And I talked with the Ice instructor. She said that ice exhibits have been shown before, and there are cooling glass cupboards we can display them in."

    red @talkingmouth "It seems like a great idea, right?"

    dawn @sadbrow talkingmouth "I guess... why do you want me to show them off, though? Your muscles won't be {i}that{/i} big when I'm done, you know."

    red @happy "Yeah, no, I know. It's not about me. Honestly, I think the Altaria is way more impressive. No, I just think that such awesome sculptures should be seen by other people."

    dawn @sadbrow talkingmouth "You're very nice."

    pause 1.0

    red @sadbrow talkingmouth "Come on. I can't be the {i}only{/i} person to say your statues are awesome, right?"

    dawn @sadbrow talkingmouth "My Mom never has..."

    red @sadbrow talkingmouth "Okay. Friends, then."

    dawn @sadbrow talkingmouth "There were three people my age in Snowpoint."

    red @surprised "What? Wasn't it a city?"

    dawn @talkingmouth "In the technical sense. Most families moved away if they had kids, though. Especially during Winter. It would get so cold that your windows would crack."

    pause 1.0

    dawn @surprised "Oh, I didn't mind that, though! It just got lonely sometimes."

    pause 0.5

    red @sadbrow talkingmouth "So... you {i}really{/i} didn't have any friends?"

    pause 1.0

    dawn @sadbrow talkingmouth "There was {i}one{/i} girl I spent a lot of time with. Her name was Mindy."
    dawn @closedbrow talkingmouth "She... was not the best person, in retrospect. But she never tried to stop me from doing what I was doing. And she never tried to get me to do anything else. So I hung out with her. All the time, actually."

    red @confused "What do you mean she 'wasn't the best person?' Did she do something wrong?"

    dawn @talkingmouth "Nothing specifically. But... every time I did something, no matter what it was, she'd make fun of me, and criticize even the smallest things. For no reason."
    dawn @sadbrow talking2mouth "I think she was just bored. But {i}everyone{/i} in Snowpoint was bored. I don't think that was really fair of her."

    pause 0.5

    dawn @angry "And she'd always pull pranks by having her Gastly jump out at people to scare them... and then they'd fall in the snow, and get all wet!"

    pause 0.5

    dawn @sadbrow talkingmouth "And she did this to other people too. Not just me. In case it sounded like she was only bullying me."

    pause 0.5

    dawn @closedbrow talking2mouth "{size=30}She wasn't.{/size}"

    red @sad2brow talking2mouth "Geez, I'm sorry. That sounds grossly unfair."

    dawn @talkingmouth "Yeah. She called herself my rival in Coordinating, but... she didn't do what rivals are {i}supposed{/i} to do."
    dawn @sadbrow talkingmouth "We're rivals, right?"

    red @talkingmouth "Of course."

    dawn @talkingmouth "So we push each other forward."

    dawn @sadbrow talkingmouth "But Mindy just dragged me back, and..."

    pause 1.0

    dawn @talkingmouth "Well, that's what my Mom said when she banned Mindy from ever seeing me again."

    pause 1.0

    red @talking2mouth "How did you feel about that?"

    dawn @talkingmouth "I... don't know. I think it might have been for the best, but... after that, I was so lonely. I didn't have {i}anyone{/i} to talk to about anything {i}except{/i} Pokémon." 
    dawn @sadbrow talkingmouth "It was the only thing {i}anyone{/i} had in common."
    dawn @sad "I guess, after that, I might have started resenting Pokémon a little bit, since I {i}had{/i} to talk about them, if I wanted to talk about anything, with anyone, ever."

    redmind @thinking "Hm. So, it seems like, more than anything, Dawn doesn't like being forced to do something."

    pause 0.5

    dawn @sadbrow talkingmouth "At least I could talk about sculpture, fashion, and theater with Mindy, even if she insulted my taste every time we talked."

    red @sadbrow talkingmouth "I can get how there would be some conflicting emotions there."

    pause 1.0

    red @happy "But, hey, I'm here now! And, uh, I don't know {i}anything{/i} about the stuff that interests you... but, I mean, I can learn."

    dawn @sadbrow talkingmouth "Thank you."

    pause 0.5

    dawn @happy "Thank you, [first_name]. You're really a fantastic [bluecolor]rival{/color}."

    red @winkbrow talkingmouth "Don't mention it. I'm not even trying."

    pause 1.5

    dawn @sadbrow talkingmouth "...Okay. I'm not promising anything, but this exhibition you mentioned... when is it?"

    red @happy "February 19th."

    dawn @closedbrow talkingmouth "Okay. Again, I'm not anything promising, but I--"
    dawn @surprised "{w=0.5}.{w=0.5}.{w=0.5}."
    dawn @angry "Dang it."

    red @talkingmouth "You used to look really embarrassed whenever you did that. Now you just seem annoyed."

    pause 0.5

    dawn @sadbrow talkingmouth "Progress?"

    red @happy "I'd call it that."

    dawn @happy "It may just be inches... but it's progress."

    pause 0.5

    dawn @closedbrow talkingmouth "You know... I have some more time. Maybe I'll pull that sculpture out, and see about shaving off a bit of the, um, extra muscle."

    red @sadbrow talkingmouth "Alright, but let's take a picture of it first. I want to hang that up in my future weights room."
    red @winkbrow talkingmouth "Something to work towards, you know?"

    $ RelationshipRankUp("Dawn", "Rival", 2)

    return

