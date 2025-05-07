label Janine1:
    if (not IsBefore(1, 5, 2004)):
        $ persondex["Janine"]["Events"].append("Level2SceneVer2")

    scene lobby 
    with Dissolve(2.0)

    stop music fadeout 1.5

    queue music "Audio/Music/fuchsia_start.ogg" noloop
    queue music "audio/music/fuchsia_loop.ogg"

    show screen songsplash("Fuchsia City", "Zame")

    show smoke:
        animation
        alpha 0.0 yalign 3.0 xalign 0.5
        parallel:
            ease 3.0 yalign 0.5
        parallel:
            ease 0.5 alpha 1.0
            pause 0.5
            ease 3.0 alpha 0.0 

    pause 2.0

    red @closedbrow talking2mouth "Wait... isn't that...?"

    pause 1.0

    show blank
    show janine behind blank

    pause 0.1

    $ renpy.transition(None)
    hide smoke
    hide blank

    janine @talking2mouth "You're coming with me."

    red @talkingmouth "So I am. Can you just ninjutsu me over there, or is that a one-person kind of thing?"

    janine @closedbrow talking2mouth "Hm. How much do you weigh?"

    red @closedbrow talking2mouth "Uh... about 185, I think?"

    janine @talking2mouth "Right. Can you compress yourself into a 3-foot cube?"

    red @confused "Nnnno."

    janine @smirkmouth "Then I guess we're walking. Hop to it."

    red @talkingmouth "Sure thing."

    scene stadium_empty with splitfade

    pause 0.5

    show janine with dis

    janine @talking2mouth "So. What's your goal? Why are you here in the Battle Team?"

    red @surprised "Huh? This isn't where I thought this was going."

    janine @smirkmouth "Change your thoughts. That's where it's going now."

    red @talkingmouth "Well... I mean, I'm kinda in the Battle Team because you opened the door so wide for me, it smacked a bunch of other people on the way."

    janine @smirkmouth "Funny. Yeah, I know why {i}I{/i} wanted you in the Battle Team. But why'd you join?"

    red @closedbrow talking2mouth "I want to be a Pokémon Champion."

    janine @talking2mouth "Of Kanto?"

    red @talkingmouth "Any region. Kanto's my home, so that'd be really cool, but... as long as I'm a Champion, I'll be happy."

    janine @talking2mouth "Alright."
    janine @smirkmouth "Thanks. You can go now, if you want."

    red @confused "Really? You brought me all the way out here just to ask me one question?"

    if (not IsBefore(1, 5, 2004)):
        janine @sad "If I'd asked Dawn what she wanted before forcing her into the team, then you wouldn't have been matched up against her."

        janine @angrybrow talking2mouth "That was a dumb move of me. I really... ugh. I really screwed up there."

        red @sadbrow happymouth "Hey, you can't beat yourself up over that forever. I know you want perfection, but..."

        janine @talking2mouth "I don't {i}want{/i} perfection. I {i}need{/i} it. And now it's permanently unattainable."

        red @sadbrow talking2mouth "Well... I'd like to say thanks for sticking up for me when all that stuff about my power came out."
        red @sad2eyes talking2mouth "Also... I probably never would've been able to make that speech if you hadn't, uh, kinda pushed me into it."

        janine @closedbrow talking2mouth "It's fine. I made a big mistake with Dawn. Two big mistakes. Forcing her into the team, then letting you two get matched up. I didn't want to make another."

        pause 1.0

        janine @talking2mouth "I've got time. ...Why don't you ask me a couple questions?"

        red @talkingmouth "Sure."

    else:
        janine @talking2mouth "You want me to ask more?"

        red @talking2mouth "How about I ask you a couple, Captain? I want to know about my fearless leader."

        janine @sad "...Mm. Sure. I have time. Go ahead."

    red @closedbrow talking2mouth "You also want to be a Champion, right? Why?"

    janine @smirkmouth "It was either this or take over my Dad's old gym. And... I don't know."
    janine @closedbrow talkingmouth "A Gym Leadership isn't big enough. If I was a Gym Leader, I'd be one of eight. Sixteen, actually, since the Indigo League merged."

    pause 1.0

    janine @smirkmouth "I told you I don't want a part of something. I want the {i}whole{/i} thing. I'm not going to be the fifth, or thirteenth, stop on some random trainer's journey."
    janine @talking2mouth "I'm going to {i}be{/i} their journey. I'm going to be the one they climb the mountain to defeat."

    red @surprised "Wow. That's pretty intense. But why does being number one matter so much to you?"

    janine @closedbrow talkingmouth "...I come from a small city. A city, sure, but a small one. After they closed the Safari Zone, the only thing that city had was its gym, and its most famous Gym Leader left to join the Elite Four."
    janine @talking2mouth "Pretty much since I was a kid, I knew my future was set. I could have taken that Gym Leader position easily. But I also have {i}every{/i} possible advantage."
    janine @smirkmouth "I'm the daughter of an Elite Four member. I called a two-time Regional Champion uncle. Before the Safari Zone closed down, it made my Dad a ton of money, so we lived very comfortably."
    janine @closedbrow talking2mouth "Oh, and I'm the heiress to Ransei-period shinobi techniques."

    red @confused "Beg pardon?"

    janine @talking2mouth "The point is, I literally don't have a single reason why I shouldn't be able to be number one. I have no weakness. {i}Nothing{/i} is holding me back."
    janine @happy "That answer your question, [first_name]?" 
    janine @happy "I'll be number one because I have no reason not to be. And I'm not going to stop at Number One in Kobukan. I'll defeat Lance, too, and become the first three-time Regional Champion. Then I'm going for World Champion."

    red @happy "You sound like [blue_name]."

    janine @sad "Ugh... yeah. Don't tell anyone, but I saw a lot of myself in him."

    red @closedbrow talking2mouth "I've got a question, though. You said you called Lance 'uncle?'"

    if (not IsBefore(1, 5, 2004)):
        red @talking2mouth "He mentioned that when he was yelling at me during the Quarter Qlashes, but I didn't think much of it at the time."

    janine @talking2mouth "Yeah. He actually visited Fuchsia a lot when I was younger." 
    janine @closedbrow talkingmouth "When I was younger, I thought he was just visiting because he had a crush on my Aunt Aya. But he later told me he actually visited because he was trying to get my Dad to leave his gym position and join the Elite Four."

    red @happy "So he did?"

    janine @happy "Hah! No! No way. My Dad turned him down for years. {i}Years.{/i}"

    red @closedbrow talking2mouth "But... isn't Koga a member of the Indigo Elite Four now?"

    janine @talking2mouth "Well, not right {i}now.{/i} He's taking a quick break to teach at this school. But he is, yeah."

    red @talking2mouth "So what changed?"

    janine @talking2mouth "Nothing, really. Lance just asked enough that my Dad gave in."

    red @happy "Woah. That worked?"

    janine @talking2mouth "He asked every day. No matter {i}what{/i}. Rain, shine, no matter where Lance started his day, at 5 PM, he would show up at my family's door. We had him over for dinner a lot."
    janine @happy "I think what made my Dad eventually cave was Lance became... well, my friend. I was a third his age, but he liked my determination, and I thought he was the coolest guy ever. He was so kind."

    pause 1.0

    show janine sad with dis

    pause 1.0

    red @sad "What happened?"

    janine @talking2mouth "I'm not sure there's anything specific I can point at and say 'that's when Lance changed.'"

    janine @talking2mouth "He just got beaten down by losing so often, I think. I mean, he's one of the top five strongest trainers in the world. But he had to lose so many times to get there... I wonder if it was worth it."
    janine @closedbrow talkingmouth "I wonder if {i}he{/i} wonders if it was worth it."

    pause 1.0

    red @talkingmouth "I'm kinda surprised you're so... open."

    janine -sad @talking2mouth "Hm?"

    red @happy "Like, you're pretty terse during practices. And you're kinda an intimidating woman, you know? But you're just telling me all this stuff about you."
    red @confusedeyebrows talkingmouth "I guess the whole 'you will obey' persona is just to keep us in line?"

    janine @happy "Oh! Yeah, I see what you mean. {w=0.5}Hah {w=0.5}hah."

    show janine blush with dis:
        ease 0.5 ypos 1.2 zoom 1.3

    janine @smirkmouth "But let me be very clear. I'm {i}choosing{/i} to be open with you. Because I think you're a good listener. And not a word of this conversation will leave this battle hall."

    pause 1.0

    janine @smirkmouth "Oh, also. You {i}will{/i} obey. Okay?"

    narrator "Although the butterflies in your stomach seem all but ready to burst out at a moment's notice, you're cognizant that this moment could very easily define your future relationship with Janine."

    narrator "{color=#0048ff}Anything less than enthusiastic, verbal, consent will probably get Janine to back off.{/color}"

    menu:
        "Yes, Ma'am.":
            $ AddEvent("Janine", "Domming")
            janine @angry "Tch. You really don't listen, do you? What {i}am{/i} I going to have to do to make you remember?"

            show janine:
                ease 0.5 ypos 1.3 zoom 1.4

            janine @smirkmouth "I'm not a Ma'am. If you really can't bear to call me by my name, how about... 'Miss'?"

            red @surprised "{size=30}Yeahsurethatseemsfinemiss.{/size}"

            pause 1.0

            janine @smirkmouth "Right answer."

        ">Sputter frantic, flustered gibberish":
            janine @smirkmouth "Cute, but I think you probably meant to say 'yes, Miss'?"

            menu: 
                "Yes, Miss.":
                    $ AddEvent("Janine", "Domming")
                    pause 1.0

                    janine @smirkmouth "Right answer."

                "No, I don't think so.":
                    janine @surprised "Oh, seriously? My bad. Kinda disappointing, but I'll back off."

        "Could you not do that?":
            janine @surprised "Oh, seriously? My bad. Kinda disappointing, but I'll back off."

    show janine -blush with dis:
        ypos 1.0 zoom 1.0

    janine @closedbrow talking2mouth "Anyway, it's not really a persona. It's just... well, it's who I am."
    janine @smirkmouth "My first year as Battle Team leader. Do you remember how many team members I said I had?"

    red @closedbrow talking2mouth "Sixty-two, right?"

    if (HasEvent("Janine", "Domming")):
        janine @blush smirkmouth "You were paying attention. Good boy."

    else:
        janine @talking2mouth "Yeah, that's right."

    janine @talking2mouth "I accepted a ton of people into the Battle Team. Pretty much because I was too afraid to turn anyone down. And I just picked whoever I thought were the strongest battlers."
    janine @closedbrow talking2mouth "...Which, looking back on it, was pretty much the people who talked about being the strongest the most."

    red @confused "Eesh."

    janine @talking2mouth "Yeah. Imagine sixty-two [blue_name]s, who all think they know how to run the team, all of them convinced that they're the only one on the team who matters."

    red @surprised "How did you survive?"

    janine @talking2mouth "I stopped giving them choices."

    red @confused "Seriously? There's gotta be more to it than that."

    janine @smirkmouth "No, I'm serious. I treated the team like it was a democracy that first year, and that was the biggest mistake I could have made."
    janine @closedbrow talkingmouth "{i}I'm{/i} in charge. {i}I{/i} make the decisions. If I know what's best for someone, I'm not going to sit on my hands and let them make a mistake."
    janine @smirkmouth "Actually, my Dad was the one who told me to, uh... well, basically, remember I was in charge. I tried too hard to make everyone happy. Then he just sat me down and said..."
    janine @koga "Janine! My daughter! Shinobi Heiress! You must not let yourself be cowed by the masses! You must cut through their awful opinions like a {i}shuriken!{/i}"
    janine @happy "I mean, at the time I was kinda an edgy teen, so I didn't really--"

    red @surprised "WHAT THE HELL WAS THAT?!"

    janine @talking2mouth "Huh?"

    red @surprised "Your face! It just--it became--you looked--"

    if (HasEvent("Janine", "Domming")):
        janine @blush talking2mouth "Stop stuttering."

    pause 1.0

    red @closedbrow talking2mouth "Sorry. What I meant to say was you, uh, you looked {i}exactly{/i} like your father there."

    janine @smirkmouth "Oh, that? Basic kunoichi disguise technique. Don't worry about it."

    red @talkingmouth "Uh... even if I try, I think I'm going to see that in my nightmares."

    janine @closedbrow talkingmouth "Get over it."

    red @sadbrow talking2mouth "I... yeah. Okay."

    pause 1.0

    red @talkingmouth "So it was your Dad who told you to stop giving the other Battle Team members choices?"

    janine @talking2mouth "Kind of. What he really said was that I needed to have more confidence in my own, but it was the same outcome, really."

    red @happy "So, you've got a good relationship with him?"

    janine @happy "Yeah, good enough. I mean, we butt heads all the time, but he's the one who laid out the red carpet for me." 
    janine @talking2mouth "He's a bit disappointed I'm not trying to be the new Fuchsia Gym Leader, but he can't exactly fault me for aiming higher."

    red @talkingmouth "...What about your Mom?"

    janine @talking2mouth "Killed by a rival ninja clan."

    red @surprised "WHAT?"

    if (HasEvent("Janine", "Domming")):
        janine @blush happy "Oh, you are {i}fun{/i} to tease."

    else:
        janine @happy "God, you're too easy."

    janine @talking2mouth "Nah, my Mom wasn't really in the picture. Aunt Aya kinda hinted that my Dad might not have been married when I was born, so, yeah. Never knew her. Never cared, really."

    red @talkingmouth "And what about Lance? Sounds like he was almost family to you. What does he think about you attempting to be World Champ? Everyone knows he wants that, too, and he's been trying for a long time."

    janine @sad "...He's fine with it."

    pause 1.0

    red @talkingmouth "Huh. I guess I finally hit the wall."

    janine @surprised "Run that by me again?"

    red @talkingmouth "I've been asking more and more personal questions, just {i}waiting{/i} for you to eventually shut me down. And this is the first question I've asked that I don't think you're being entirely straight with me about."

    if (HasEvent("Janine", "Domming")):
        janine surprised "Wait... you've been waiting for me to shut you down?"

        red @talkingmouth "Yeah, just testing my boundaries. Seeing what I can get away with, you know."

        pause 1.0

        janine -surprisedbrow -frownmouth -surprised happyneutralmouth blush @smirkmouth "Well. {w=0.5}Isn't that {i}interesting{/i}."

        janine @closedbrow talkingmouth "Just out of curiosity, what made you think you could get away with {i}that{/i}?"

        red @talkingmouth "It was less a 'I want to see if I can get away with this' and more a 'I want to see what happens if I {i}don't{/i} get away with this."

        janine @happy "Ah... it's {i}very{/i} refreshing, finally meeting someone who can just play the game and be honest about it."

        janine @smirkmouth "Let me just set expectations here. You get this Battle Team into the National Tournament, you do anything I tell you to, and you get...?"

        red @happy "To spend time with you?"

        pause 1.0

        janine -blush -happyneutralmouth @smirkmouth "Hm. You're almost too cute. I'd feel guilty, if I tore into you like I want to."

        red @surprised "What?"

        janine @closedbrow talking2mouth "I don't think you're ready for this just yet."

        red @sad "Oh..."

        janine @smirkmouth "Mmm... let me rephrase. I don't think you {i}deserve{/i} this just yet."

        red @talkingmouth "Oh! Okay. Much more into that."

        janine @talking2mouth "You be a good boy and win me some more battles, okay?" 
        janine @blush smirkmouth "And if you do that... I'll give you your reward."

        pause 1.0

        red @confused "I just, I like to track my progress. Can you, uh, make clear the number of battles I need to win to make that happen?"

        janine @happy "Oh, you'll know. And you'll know when I let you know, and not a moment before. Understood?"

        red @happy "Yes, Miss."

        janine @happy "Hmhmhmhm."

        janine @blush smirkmouth "{color=#0048ff}Good boy.{/color}"

        $ persondex["Janine"]["Relationship"] = "Good Boy"
        $ persondex["Janine"]["RelationshipRank"] = 1

        $ PlaySound("sav.ogg")

        narrator "Your heart shifts as you feel your relationship with Janine evolve from '{color=#0048ff}Tool{/color}' to '{color=#0048ff}Good Boy{/color}'!"

    else:
        janine @smirkmouth "Hm. Aren't you perceptive. I hope you keep that up in your battles."

        red @talking2mouth "I'll do my best. I'm really going to try to win."

        janine @talking2mouth "I ask for nothing less."

        red @confused "Uh... do you mean 'more'?"

        janine @happy "How about you just handle the battling, and leave the figuring out who-means-what to me?"

        red @closedbrow talking2mouth "Jeez. Alright."

        janine @blush smirkmouth "Now, shouldn't you get back to training? I don't want my precious {color=#0048ff}battler{/color} resting on his laurels, after all. "

        $ persondex["Janine"]["Relationship"] = "Battler"
        $ persondex["Janine"]["RelationshipRank"] = 1

        $ PlaySound("sav.ogg")

        narrator "Your heart shifts as you feel your relationship with Janine evolve from '{color=#0048ff}Tool{/color}' to '{color=#0048ff}Battler{/color}'!"

return

label Janine2:
    scene colosseum 
    with Dissolve(2.0)

    stop music fadeout 1.5

    queue music "Audio/Music/fuchsia_start.ogg" noloop
    queue music "audio/music/fuchsia_loop.ogg"

    show screen songsplash("Fuchsia City", "Zame")

    narrator "You're walking by the Battle Hall when you suddenly hear the sounds of a whispered argument."
    narrator "Straining your ears, you try to listen to what's being said, but... the sound cuts out immediately."
    narrator "A moment later, you hear footsteps, and Janine's face appears in the doorway."

    show janine with dis

    if (HasEvent("Janine", "Domming")):
        janine @talking2mouth "Naughty. Eavesdropping? Thought you knew better than that."

    janine @talking2mouth "Get in here."

    red @surprised "Huh? How did you--"

    janine @talking2mouth "I'm a ninja, [first_name]. I heard you breathing from halfway across campus."

    pause 1.0

    red @confused "I can't tell if you actually have magic powers or not."

    janine @closedbrow talkingmouth "As much as you do. Now, as I said--get in here."

    red @talking2mouth closedbrow sweat "Right."

    scene stadium_empty 
    show janine:
        xpos 0.33
    show lance:
        xpos 0.66
    with splitfade

    redmind @thonk "Lance is here...?"

    janine @talkingmouth "It's a good thing you dropped by, actually."
    janine @closedbrow talking2mouth "I don't want to have to listen to this argument anymore, so we're settling it now."

    red @sadbrow talking2mouth "Is it something about [pika_name]?"

    lance @upeyes talking2mouth "Against my better judgment, I have decided to lay down my arms against that {i}particular{/i} battle."
    lance @talking2mouth "The war, however, is far from over."

    janine @talking2mouth "Lance has been trying to convince me to remove you from the team."

    lance @closedbrow talking2mouth "And you may be pleased to hear, boy, that Janine has proved {i}frustratingly{/i} unaccommodating on that matter."

    red @sad2eyes talkingmouth "Uh... thanks, Janine."

    lance @talking2mouth "However, we have reached an impasse."
    lance @talking2mouth "I have made a claim I know to be true. Janine does not believe me, however."
    lance @closedbrow talking2mouth "Ergo, we need ask for your... 'opinion'."

    red @confused "Well... you're the heads of the Battle Team, so--"

    lance @angrybrow talking2mouth "Incorrect. Janine is the Captain of the Battle Team. All I may do is provide advice."
    lance @sad2eyes talking2mouth "I assure you, if your statement had even a molecule of accuracy to it, you would not sully our meetings with your presence."

    red @unamusedbrow unamusedmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    redmind @thinking "He's impossible when he's like this. He doesn't want to argue, he just wants to get the last word in."

    pause 1.0

    janine @talking2mouth "The question, Lance?"
    janine @closedbrow talkingmouth "Honestly, though, it's obvious. You're too angry at him to see the clear answer."

    lance @talking2mouth "Save your commentary as a response to the answer {i}I know{/i} is coming."

    red @talking2mouth confusedeyebrows unamusedeyes "Which is?"

    lance @talking2mouth "Assuming, somehow, you stumbled your way into the National Championship, and were to face down a single opponent in order to claim the Champion's throne..."
    lance @talking2mouth "Who would you be willing to defeat?"

    red @surprised "Huh?"
    red @happy "What kind of question is that, Advisor Lance? Anyone!"

    janine @closedbrow talkingmouth "See? I know my battlers, Lance."

    if (HasEvent("Janine", "Domming")):
        lance @upeyes talking2mouth "Believe me, I am sickeningly aware of your... {w=0.5}{i}familiarity{/i} with Mr. [last_name], and it is only my oath as your godfather that keeps me from indulging in my urge to vomit."
        lance @talking2mouth "But that is not the point of the matter here."
        
    lance @closedbrow talking2mouth "Those are idealistic words spouted without thought of consequence."
    lance @angrybrow talking2mouth "Define 'anyone', boy."

    red @confused "Define anyone? I mean... anyone who wants to battle me, I guess..."

    lance @closedbrow talking2mouth "And so the cracks appear."
    lance @talking2mouth "And what about an unwilling foe?"

    pause 0.5

    red @sad2eyes talkingmouth "I mean, I don't think someone who doesn't want to battle could ever reach the finals of the National Championships..."

    lance @closedbrow talking2mouth "Doesn't want to battle {i}you.{/i}"
    lance @talking2mouth "What if it is a friend? A cherished friend who has trusted you, supported you, and uplifted you throughout your journey?"
    lance surprisedbrow @angrybrow talking2mouth "A beloved mentor. An instructor? Your own mother? Could you dash their hopes against the rocks? Could you repay their generosity with brutality?"

    red @angry "You leave my Mom out of this."

    pause 1.0

    lance -surprisedbrow @sad2eyes talking2mouth "In lieu of apology, I will not make such comparisons again."

    red @closedeyes angryeyebrows talking2mouth "Anyway, it doesn't matter if I'd battle those people or not. I'm never going to be in that situation."

    lance @talking2mouth "But you aim to be Champion."

    show janine sadbrow with dis

    red @confused "Well, yeah. But they don't."

    lance @sadeyes talking2mouth "So you hold that my hypothetical has merit if both parties want to be Champion?"

    red @angrybrow talking2mouth "Well, yeah! But then we'd still want to battle each other, right? So what you said before about us not wanting to battle each other can't be true."

    lance @talking2mouth "Can you not see any situation in which two individuals who both want to be champion would be unwilling to battle each other?"

    red @talking2mouth "No."

    lance @closedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
    lance @talking2mouth "Then I've one more question for you."

    pause 1.0

    lance @talking2mouth "Would you be willing to defeat Janine?"

    red @surprised "Huh...?"

    if (AimLevel() < 70):
        red @closedbrow sweat talking2mouth "That's... it doesn't matter. I couldn't beat her."

        janine @closedbrow talking2mouth "{size=30}Worst possible thing you could've said there, [first_name].{/size}"

        lance @talking2mouth "Assume that you can. Assume you somehow crawled your way up to the level of Champions."
        lance @talking2mouth angrybrow "Assume that you know, if you defeat Janine today, she will never achieve her dream."
        lance @talking2mouth angrybrow shadow "Assume that there is only room for a single Number One. Will that be you?"
        lance @talking2mouth "Will you take the trophy from the person who trained you to?"

    pause 1.0

    python:
        answeredyes = False
        answeredno = False

    label beatjaninequestion:

    if (answeredno or answeredyes):
        lance @angry "I ask you again. Would you, [first_name] [last_name], be willing to prevent Janine Koga from reaching her goal for no reason other than your own ambition?"

    menu:
        "Yes.":
            narrator "You want to say that, but... are you sure?"
            $ answeredyes = True
            jump beatjaninequestion

        "No.":
            narrator "You want to say that, but... are you sure?"
            $ answeredno = True
            jump beatjaninequestion

        "..." if (answeredyes and answeredno):
            pass

    lance @talking2mouth "...And there we have it."

    janine @talking2mouth "Lance..."

    lance @talking2mouth "My past will instruct you. Do not make waste of the lessons my failures have garnered."

    pause 1.0

    lance @talking2mouth "Think on this result, goddaughter. I take my leave of you."

    hide lance with dis

    pause 1.0

    show janine closedbrow:
        xpos 0.33
        ease 0.5 xpos 0.5

    pause 1.0

    red @sadbrow talkingmouth "...Hey. Sorry."

    pause 1.0

    janine angrybrow @talking2mouth "Why the {w=0.5}{i}fuck{/i} didn't you say 'yes'?"

    red @surprised "H-huh...?"

    show janine with dis:
        ypos 1.0 zoom 1.0
        ease 0.3 ypos 1.2 zoom 1.3

    janine @angrymouth "Do you think this is a {i}joke{/i}, [first_name]?"

    if (HasEvent("Janine", "Domming")):
        redmind @sadbrow frownmouth "This isn't her persona... she's actually just pissed right now."

    janine @angrymouth "I've spent {i}two{/i} extra years at this school so I could {i}make{/i} the perfect successor."
    janine @angrymouth "So I could {i}leave{/i} this school, finally, stronger than I found it."
    janine @talking2mouth "You're not doing me a favor by holding {i}anything{/i} back!"
    janine @sad "Do you think... even for a second... there's even a {i}chance{/i} that I wouldn't crush {i}you{/i} to be Champion?"

    pause 1.0

    show janine surprisedbrow with dis

    red @sadbrow talkingmouth "I do."

    show janine closedbrow with dis

    janine @talking2mouth "Explain. And choose your words carefully."

    call clearscreens() from _call_clearscreens_139
    scene blank with Dissolve(1.0)

    show stadium_empty at sepia behind blank
    show janine at sepia behind blank
    show flashback behind blank

    pause 1.0

    hide blank with Dissolve(1.0)

    red sepia @talkingmouth "And what about Lance? Sounds like he was almost family to you. What does he think about you attempting to be World Champ? Everyone knows he wants that, too, and he's been trying for a long time."

    janine @sad "...He's fine with it."

    pause 1.0

    red sepia @talkingmouth "Huh. I guess I finally hit the wall."

    janine sepia @surprised "Run that by me again?"

    show blank with splitfade

    pause 1.0

    scene stadium_empty
    show janine
    show screen currentdate
    with Dissolve(1.0)

    red @sadbrow talking2mouth "I remember... I once asked you what Lance thought about you wanting to be World Champion."
    red @sadbrow talkingmouth "You didn't really answer."

    pause 1.0

    janine @talking2mouth "And because of that, you think I might have some kind of... restraint when it comes to fighting him?"
    janine @closedbrow talking2mouth "And you think I might have the same sort of restraint when it comes to fighting you?"
    
    pause 0.5

    red @sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."

    janine @sadbrow talkingmouth "God, stop looking at me with those puppy-dog eyes. I'm sorry I snapped at you, alright? I was just surprised."
    janine @talking2mouth "I don't want... any of my battlers to have {i}any{/i} inhibitions about facing anyone. Definitely not me."

    pause 1.0

    janine @closedbrow talkingmouth "Dad once told me that the ancient ninja heads of old would appoint their greatest rivals to their bodyguard squadron."
    janine @angrybrow talking2mouth "If the Clan head became weak, then his worthy successors would be in the perfect position to take advantage of that weakness."

    pause 0.5

    janine @angrybrow talking2mouth "But that's not important. What's important is that you don't hold back in battle. {i}Ever.{/i}"
    janine @closedbrow talking2mouth "Do you think [pika_name] could have ever found his true power if you'd held back against Dawn?"

    $ PlaySound("Pokemon/pikachu_happy3.ogg")

    libpikachu @angrybrow happymouth glowing "Pi-i-i-ka!"

    red @sadbrow talkingmouth sweat "Probably not."

    pause 0.5

    janine @closedbrow talkingmouth "Look. My Dad still lives on battlefields from hundreds of years ago. One with knives, and spike pits, and poisons."
    janine @talking2mouth "But the {i}real{/i} battlefield is right here. In the distance between us. And if you can't cross this distance and tear down all my hopes, I'm a failure as a Battle Team Captain."

    pause 1.0

    janine @angrybrow talking2mouth "You won't let me be a failure, will you?"

    red @sadbrow talkingmouth "Janine, you're not one."

    janine @closedbrow talking2mouth "I know. But I need Kobukan--I need the {i}world{/i} to know. Kobukan deserves the best, and the best I can give it is you."

    pause 1.0

    red @surprisedbrow talking2mouth lightblush "Oh."

    janine @talking2mouth "I knew what the plan was from the moment I met you. I'm a woman who knows what she wants. And what I want is for you to sweep the Quarter Qlashes, get through the National Championships, and become Kobukan's champion."

    red @surprised "That's... that's a tremendous amount of pressure!"

    janine @talking2mouth "I know that. But is it enough to break you?"

    menu:
        "Yes.":
            $ AddEvent("Janine", "WillBreakMe")
            janine @closedbrow "{w=0.5}.{w=0.5}.{w=0.5}."
            janine @talking2mouth "Then it's simple. You need more training."

        "No.":
            $ AddEvent("Janine", "WillNotBreakMe")
            janine @talking2mouth "Then there's no problem."

    red @talkingmouth "But... what about you? Don't you want to be Kobukan's Champion? Don't you want to be World Champion?"
    red @talking2mouth "You said you were planning on becoming Kobukan's Champion, then beating Lance, and becoming the world's first three-time regional Champion. And then you'd become World Champion."

    pause 1.0 

    red @sadbrow talkingmouth "I'm sorry. I'm not sure how I fit into that plan."

    janine @talking2mouth "...I'm not, either."

    red @surprised "Huh?"

    janine @closedbrow talking2mouth "There can only ever be one winner, and one loser. I will be the winner. Because I always get what I want."
    janine @sadbrow talking2mouth "And you... are who I think has the greatest chance of giving Kobukan the glory it deserves. So you will be. Because I always get what I want."

    pause 1.0

    janine smilemouth @happy "Hah! This'd be a lot easier to figure out if I wasn't so good!"

    pause 0.5

    if (IsBefore(1, 1, 2005)):
        janine @sadbrow talkingmouth "But that's not something we need to figure out right now. The National Championship isn't until next year."

    elif (IsBefore(1, 2, 2005)):
        janine @sadbrow talkingmouth "But that's not something we need to figure out right now. The National Championship isn't for months."
    
    elif (IsBefore(1, 3, 2005)):
        janine @sadbrow talkingmouth "But that's not something we need to figure out right now. The National Championship isn't for a while."

    janine @closedbrow talkingmouth "Let's just focus on what I can control {i}right now.{/i}"

    red @confused "Oh, yeah? What's that?"

    if (HasEvent("Janine", "Domming")):
        janine @surprisedbrow talking2mouth "About you?"
        janine talkingmouth angrybrow blush "Everything."

        red @surprisedbrow frownmouth lightblush "{size=30}OhrightIforgotsorry.{/size}"

        pause 0.5

        red @sadbrow talkingmouth "{size=30}Miss.{/size}"

        janine -blush @closedbrow blush talkingmouth "Good boy."

    else:
        janine @closedbrow talking2mouth "The performance of my battlers."

    janine -talkingmouth -angrybrow @talking2mouth "Now listen up. Were you paying attention that time we talked in the Battle Hall? Do you remember what I said, about why {i}I'll{/i} be number one?"

    red @talking2mouth "Yeah. I was. And I do."
    red @closedbrow talking2mouth "You said you didn't have an excuse not to."

    janine @closedbrow "{w=0.5}.{w=0.5}.{w=0.5}."

    red @talking2mouth "You said that you... were the daughter of an Elite Four member. The goddaughter of a Champion. The heir to a gym, yours for the taking at any point."
    red @confused "And, uh, you may or may not have actual magical powers from your Ninja ancestry?"

    janine @closedbrow talkingmouth "I'm leaving that ambiguous."

    redmind @thinking "Wouldn't be any weirder than my classmate, the Mythical Pokémon."

    janine @talking2mouth "Anyway, you're right. You {i}were{/i} listening."
    janine @closedbrow talkingmouth "I appreciate that. A lot of my Battle Team members only listen to me about stuff that makes them stronger. Obviously, that's what I'm here for, but I don't like to think my teammates are just... {i}using{/i} me."
    janine @sadbrow talkingmouth "No-one likes to feel like a [bluecolor]tool{/color}."

    pause 1.0

    janine @talking2mouth "Now, we'll talk about that. Sit."

    show janine surprisedbrow:
        linear 0.3 xpos 0.5 ypos 0.8

    pause 1.0

    janine -surprisedbrow @talking2mouth "I meant 'let's go sit down on a bench.'"
    janine @talkingmouth "But I can't fault the enthusiasm."

    red @talkingmouth angryeyebrows sad2eyes "You can't just say 'sit' like that and expect me to {i}not{/i} sit, Janine."

    if (not HasEvent("Janine", "Domming")):
        janine @talkingmouth "And here I was thinking you weren't into this."

        menu:
            "I'm not.":
                janine @closedbrow talkingmouth "Then you're giving me some mixed signals."

            "I might be wavering...":
                red @confused "I... guess. Maybe a little. It's kind of a... a process of self-discovery, I guess."

                pause 1.0

                janine @talking2mouth "Stand up."

                show janine:
                    xpos 0.5 ypos 1.0

                pause 1.0

                janine @talking2mouth "This isn't something I take casually, or handle lightly. You're putting your trust in me. I'm putting my trust in you. We both have a lot to lose if we don't handle this properly."

                red @confused "Guessing you're not talking about the Quarter Qlashes, or the National Championship?"

                pause 0.5

                janine @talkingmouth "No."

                pause 1.0

                janine @talking2mouth "Let me ask you something, then. And answer honestly."
                janine @talkingmouth "Do you want me to control you? Do you want me to make you mine? To treat you as I like, without requiring permission to do so?"
                janine @closedbrow talkingmouth "I can't promise it'll be fun. But I {i}can{/i} promise you'll enjoy it."

                narrator "A familiar feeling of butterflies in your stomach returns. You're cognizant that this moment could very easily define your future relationship with Janine."

                narrator "{color=#0048ff}Anything less than enthusiastic, verbal, consent will probably get Janine to back off.{/color}"

                menu:
                    "Yes, Ma'am.":
                        $ AddEvent("Janine", "Domming")
                        janine @angry "Tch. You really don't listen, do you? What {i}am{/i} I going to have to do to make you remember?"

                        show janine:
                            ease 0.5 ypos 1.3 zoom 1.4

                        janine @smirkmouth "I'm not a Ma'am. If you really can't bear to call me by my name, how about... 'Miss'?"

                        red @surprised "{size=30}Yeahsurethatseemsfinemiss.{/size}"

                        pause 1.0

                        janine @smirkmouth "Right answer."

                    ">Sputter frantic, flustered gibberish":
                        janine @smirkmouth "Cute, but I think you probably meant to say 'yes, Miss'?"

                        menu: 
                            "Yes, Miss.":
                                $ AddEvent("Janine", "Domming")
                                pause 1.0

                                janine @smirkmouth "Right answer."

                            "No, again.":
                                janine @surprised "What? Then what was the point of...?"
                                janine @sad "Whatever. This is too confusing to deal with, anyway."

                    "No, again.":
                        janine @surprised "What? Then what was the point of...?"
                        janine @sad "Whatever. This is too confusing to deal with, anyway."
    else:
        janine "{w=0.5}.{w=0.5}.{w=0.5}."

        janine @talkingmouth blush "So mouthy. Didn't think you wanted to be disciplined {i}this{/i} much."

        red @surprisedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

        janine @talking2mouth "Stand up."

        show janine:
            xpos 0.5 ypos 1.0

        pause 1.0

        janine @sadbrow talking2mouth "Hm. Actually..."
        janine @closedbrow talking2mouth "Okay, dropping the persona. Let's talk about this. Are you still comfortable? Have I crossed any lines?"

        menu:
            "I'm feeling pretty uncomfortable, actually. I want to bow out.":
                $ RemoveEvent("Janine", "Domming")
                $ AddEvent("Janine", "RemoveDomming")
                janine @closedbrow talking2mouth "I understand. Thank you for telling me."
                janine @sadbrow talking2mouth "I... sorry. If I'd known sooner, I would have stopped sooner."
                janine @closedbrow talking2mouth "I'm not at all blaming you. It was my responsibility to check in, and I waited too long."

                pause 0.5

                janine @sadbrow talking2mouth "Are you okay? Do you need to talk to Nurse Miriam?"

                red @happy "Nah, it's nothing that bad. Just didn't want this to go any further."

                janine @closedbrow talking2mouth "Alright."

                pause 1.0

            "I'm fine as-is.":
                janine @closedbrow talking2mouth "{w=0.5}.{w=0.5}.{w=0.5}.Okay. Putting the persona back on."

                pause 0.5

                janine @angrybrow blush talkingmouth "Then what do you think you're doing, complaining about my commands?"
                janine @closedbrow talkingmouth "I really thought you would have known better..."
                
                red @talking2mouth "I don't suppose an apology would, uh, cover my ass in this case?"
                
                janine @closedbrow talkingmouth "...No. But I can think of something a bit more physical that just might do it."

            "Ramp it up!":
                janine @closedbrow talkingmouth "...God, you're so fun."
                janine @closedbrow talking2mouth "{w=0.5}.{w=0.5}.{w=0.5}.Okay. Putting the persona back on."

                pause 0.5

                janine @angrybrow blush talkingmouth "Then what do you think you're doing, complaining about my commands?"
                janine @closedbrow talkingmouth "I really thought you would have known better..."

                red @talking2mouth "I don't suppose an apology would, uh, cover my ass in this case?"

                janine @closedbrow talkingmouth "...No. But I can think of something a bit more physical that just might do it."
    
    janine @talkingmouth "Let's get back on-topic. I'll be Number One because I have no excuse not to be."

    pause 1.0

    janine @angrybrow talking2mouth "So what's your excuse?"

    red @confused "Huh?"

    janine @talking2mouth "This isn't a {i}choice.{/i} Like I said, I don't 'believe in' people. That includes myself."

    redmind @closedbrow frownmouth "Janine's got to be the most confident person I know. To say she doesn't believe in herself..."

    janine @talking2mouth "I'll be Number One because I have every advantage. Now, what's your excuse for not being Number One?"

    red @sadbrow talkingmouth "I mean, I'm a brand-new student."

    janine @talking2mouth "I haven't improved much from my first year at Kobukan. I could have done it then. Maybe I should have. I didn't. That's not an excuse. Next."

    red @confused "Okay, well, I have basically no training experience prior to Kobukan--"

    janine @talking2mouth "Lance never attended Kobukan. He was trained by the Blackthorn Dragon Clan."
    janine @talkingmouth "That pennant that has his name on it in the Gym? That was earned after he came here as an instructor."
    janine @closedbrow talkingmouth "He became champion twice without ever stepping foot in a classroom that even acknowledged the existence of non Dragon-types."
    janine @angrybrow talking2mouth "Not.{w=0.5} An.{w=0.5} Excuse."

    redmind @thinking "Well... I guess..."
    red @sadbrow talkingmouth "I guess I'd have to beat you."

    janine @closedbrow talking2mouth "We've come full circle, then..."
    janine @talking2mouth "...Take a walk with me. This is an idea I {i}need{/i} to get into your head. And people think better when they're walking."
    janine @closedbrow talkingmouth "In fact, connecting a memory with a physical sensation is proven to help recall tremendously."

    show janine:
        xpos 0.5 
        ease 0.5 xpos 1.2

    red @surprised "Oh... okay!"

    scene blank2 with splitfadefast

    narrator "You quickly follow after Janine, as she leads you to the little-visited greenhouse." 
    narrator "Though you're fit and healthy, you have difficulty keeping up with her, and she seems to be relishing in her ability to disappear every time you turn a corner."
    narrator "At the end of a long set of stairs, you emerge, panting slightly, onto the roof..."

    scene rooftop with splitfade

    pause 1.0

    red @confused "Janine? Where'd you go?"

    show janine:
        ypos 0.15 rotate 180

    show rooftop with vpunch

    janine @talking2mouth "Hey."

    red @closedbrow sweat talking2mouth "Jeez, that was a heart attack and a half."

    pause 1.0

    red @talking2mouth "Wait, what are you hanging from?"

    pause 1.0

    janine @closedbrow talking2mouth "I'm going to need you to stop asking questions about ancient Shinobi secrets."

    redmind @unamusedbrow unamusedmouth "Right. Ninja magic."

    show janine:
        rotate 180 ypos 0.15
        ease 0.3 rotate 0 ypos 1.0

    pause 1.0

    janine surprised @talking2mouth "Right, now--"

    red @happy "That was extremely cool."

    pause 1.0

    janine -surprisedbrow -frownmouth -surprised @sadbrow blush talkingmouth "Eh... thanks."

    pause 0.5

    janine @talking2mouth "Now {i}listen to me.{/i}"
    janine @talkingmouth "Ariados-Man once said that 'with great power comes great responsibility.'"
    janine @talking2mouth "So you get responsibility from power."

    red @talking2mouth "I'm with you."

    janine @closedbrow talkingmouth "But where does the power come from?"

    pause 0.5

    red @confused "Huh?"

    pause 0.5

    janine @talking2mouth "It's privilege."

    red @unamusedbrow unamusedmouth "{w=0.5}.{w=0.5}.{w=0.5}."
    red @closedbrow talking2mouth "I'm poor as hell."

    janine @talking2mouth "That's not what I'm talking about."

    red @confused "Well, then what are you talking about? You told me what your privileges were. Godfather Lance, father Koga, ancient ninja techniques..."
    red @sadbrow talkingmouth "I'm not sure that stuff applies to me."

    janine @talking2mouth "I believe that. But that means you're not taking advantage of all the opportunities you have."
    janine @talkingmouth "This school is staffed by, literally, the most powerful people in the world. It's a safe place, to explore your strength, to train it, to become the best version of yourself."
    janine @talking2mouth "You are surrounded, {i}right now{/i}, by the class that will decide the future of this planet. We're standing on a roof that {i}multiple{/i} champions snuck up to, to make out on."

    if (HasLocation("Faculty Pool")):
        redmind @thinking "I guess they didn't have the faculty pool back then..."

    janine @talkingmouth "Your gym class is taught by a Champion and an Elite Four member that {i}Lance{/i} thought was good enough to keep when the Kanto and Johto leagues were merged."
    janine @talking2mouth "Yes, Kobukan's costs are ridiculous. But it gets you so much. It gets you privilege."
    janine @talking2mouth "It gets you power."
    janine @talking2mouth "It gets you responsibility."
    janine @closedbrow talking2mouth "And that responsibility is for you to kick my ass."

    pause 1.0

    janine @closedbrow talkingmouth "I mean, eventually. You're a {i}long{/i} way from ever getting a shot at that."

    pause 1.0

    red @sadbrow talkingmouth "I understand. You don't want me to waste my opportunities, by holding back. You don't want me to waste what Kobukan's given me."
    red @happy "There's one privilege you didn't mention, though."

    janine surprisedbrow @talkingmouth "Enlighten me."

    red @happy "The leader of my Battle Team is Janine Koga. Daughter of an Elite, Goddaughter of a Champion, and heiress to ancient magic ninja powers."

    pause 1.0

    janine -surprisedbrow @closedbrow blush talkingmouth "...It's a good thing I've never given a damn about playing favorites."

    pause 1.0

    red @talking2mouth "I've... got a question, though."

    janine @talking2mouth "Go ahead."

    red @sadbrow talkingmouth "Everything you said about me needing to beat you, because it's... it's my responsibility..."

    show janine surprisedbrow neutralmouth with dis

    red @sadbrow talkingmouth "Wouldn't that apply to you and Lance, as well?"

    pause 1.0

    janine sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."
    janine @talking2mouth "Yes."

    pause 1.0

    red @sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."

    janine -sadbrow @closedbrow talking2mouth "We're not talking about this now."

    red @talking2mouth "I understand."

    pause 0.5

    janine @sadbrow talking2mouth "Thank you."

    pause 1.0

    janine @closedbrow talkingmouth "Alright. Let's get back."

    scene blank2 with splitfade

    pause 1.0

    janine @talking2mouth "Hey, when Lance brought up your mother..."
    janine @talking2mouth "Is there a story there?"

    red @sadbrow talkingmouth "Not one beyond the fact I love her, and don't want to hear her be used, even in an argumentative hypothetical."

    if (HasEvent("Janine", "Domming")):
        janine @closedbrow talkingmouth "Hm. Mommy's boy, huh? That gives me some ideas."

        redmind @surprisedbrow frownmouth "{i}HOO BOY.{/i}"

    else:
        janine "{w=0.5}.{w=0.5}.{w=0.5}."
        janine @talkingmouth "That's sweet. Kind hearts were definitely missing in previous years' Battle Teams. This is... refreshing."

    pause 1.0

    janine @talking2mouth "I'm more than your Captain. Consider me a [bluecolor]rival{/color}, [first_name]. I am absolutely going to defeat you. Just as you are absolutely going to defeat me."

    pause 0.5

    red @confused "How will that work?"

    pause 0.5

    janine @closedbrow talkingmouth "I can't wait to find out."

    $ oldrelationship = GetRelationship("Janine")
    $ persondex["Janine"]["Relationship"] = "Rival"
    $ persondex["Janine"]["RelationshipRank"] = 2

    $ PlaySound("sav.ogg")

    narrator "Your heart shifts as you feel your relationship with Janine evolve from '[bluecolor][oldrelationship]{/color}' to '[bluecolor]Rival{/color}'!"

    narrator "Also..."

    narrator "By understanding your Battle Team Captain better, you feel like your understanding of your Battle Teammates has increased!"

    $ ValueChange("Bea", 1, 1/9, False, True)
    $ ValueChange("Blue", 1, 2/9, False, True)
    $ ValueChange("Erika", 1, 3/9, False, True)
    $ ValueChange("Ethan", 1, 4/9, False, True)
    $ ValueChange("Hilbert", 1, 5/9, False, True)
    $ ValueChange("Leaf", 1, 6/9, False, True)
    $ ValueChange("Sonia", 1, 7/9, False, True)
    $ ValueChange("Silver", 1, 8/9, True, True)

    narrator "That's a lot of +1s!"

return