label Nate1:
    stop music fadeout 1.5
    call clearscreens() from _call_clearscreens_179
    scene garden 
    show nate:
        xpos 0.33
    show anabel:
        xpos 0.66
    with Dissolve(2.0)

    show screen songsplash("Looker Theme Lofi Noir Remix", "AlmightyArceus")
    queue music "audio/music/anabel_start.ogg" noloop
    queue music "audio/music/anabel_loop.ogg"

    $ oldparty = copy.copy(playerparty)
    $ playerparty = []

    anabel @talkingmouth "Nate. It's a pleasure to see you."

    nate @talkingmouth "Anabel. The weather is pleasant."

    $ BecomeNamed("Anabel")

    if (IsAfter(17, 5, 2004)):
        narrator "An interesting scene unfurls here in the garden, as 'Nate' and 'Anabel' carry on an idle conversation of absolutely no importance."
    else:
        narrator "An interesting scene unfurls here in the garden, as 'Nate' and an unfamiliar woman carry on an idle conversation of absolutely no importance."

    narrator "You are not here, but if you were, you may notice something very particular about the particulars of the conversation."

    narrator "However, a keen observer of the scene may notice that the words they are saying are almost entirely different from the movement their lips are making."

    pause 1.0

    $ autoquote = False

    anabel @talkingmouth "\"Indeed. There is no rain.\"\n<You disobeyed orders.>" 

    nate @talkingmouth "\"I agree.\"\n<I did.>" 

    anabel @talkingmouth "\"Let us hope it continues to not rain.\"\n<Do you have no defense?>" 

    nate @talkingmouth "\"I do not have an umbrella.\"\n<I do not have a defense.>" 

    anabel @closedbrow talking2mouth "\"That is unfortunate.\"\n<That is unfortunate.>" 

    nate frownmouth @angrybrow talking2mouth "\"Look, if I'm going to get wet, I'm going to get wet. Why fight it?\"\n<Look, if you're going to punish me, you're going to punish me. Why fight it?>" 

    anabel @sadbrow talking2mouth "\"You may attract fireflies.\"\n<You exposed PW05 to civilian eyes.>" 

    nate @angrybrow talking2mouth "\"I love fireflies.\"\n<I saved civilian lives.>" 

    pause 1.0
    
    nate angrybrow @sadbrow talking2mouth "\"You do too. Right?\"\n<That's what we do. Right?>" 

    pause 1.0

    anabel @sadbrow talking2mouth "\"I do not like the big ones--they should be smaller than my hands.\"\n<We do not have the luxury of 'doing' anything other than what the moment demands.>" 

    nate @closedbrow talking2mouth "\"Of course. Insects are swift, right? They might bite you on your toe.\"\n<Of course. Ignorance is bliss, right? A bliss that people like us can never know.>"

    anabel @angrybrow talkingmouth "\"That's enough.\""

    pause 0.5

    anabel @talkingmouth "\"My, look at the time.\"\n<You are allowed to leave any time.>"

    nate @talking2mouth "\"Will you go?\"\n<No, I can't. None of us can. Not with our memories.>"

    anabel @closedbrow talking2mouth "\"We all must go eventually.\"\n<What memories are there worth keeping?>"

    nate @talking2mouth "\"Every {w=0.5}single {w=0.5}one. Every breath, every tear, every scar. To take them from me is to kill whoever I am underneath all these disguises.\""

    pause 0.5

    anabel @closedbrow talking2mouth "\"That was a strange outburst.\"\n<Please use coded language when speaking about work.>"

    $ autoquote = True

    nate @sadeyebrows talkingmouth "I already spend all my time lying to my classmates. Can't we just drop the act when there's no-one around?"

    anabel @closedbrow talking2mouth "There is {i}always{/i} someone around, Bl... Nate."

    pause 1.0

    nate @sadbrow talkingmouth "Can't even say my real name, huh?"
    nate @sad2eyes noshine talking2mouth "What are we doing here, Handler...?"

    anabel @closedbrow talkingmouth "Keeping people safe. That's our duty. That's what we shall always do." 

    pause 0.5

    anabel @sadbrow talking2mouth "I warned you not to go into this life..."

    nate @talking2mouth "...You can't warn a child. If you didn't want me to go, you had to stop me. Or better yet, never even offer."
    nate @talking2mouth noshine "And now... it's too late."
    nate @sad "I'm so lonely. No-one knows the real me. And the moment I get a chance to share anything true about myself, I have to wipe them."
    nate @angrybrow talking2mouth "It's not fair. Don't I deserve at least one friend? At least one person who knows me through the personas?"
    nate @talking2mouth "I don't want to do this job for seventy years and die without anyone knowing who I am."

    show anabel sadbrow with dis

    nate @sadbrow talkingmouth "...Well, there is {i}one{/i} way out of this. If I break a rule badly enough that the agency decides I'm not worth the risk."
    nate @closedbrow talking2mouth "You've been here for a while, Handler. Is that what you've come to say? Finally had enough time to deliver the bad news?"
    nate @happy "Frankly, I thought I'd get black-bagged that very evening, but I guess not. And enough time's passed that I'm not sure what kinda protocol we're following anymore."

    show nate surprisedbrow frownmouth with dis

    anabel @angry "Don't be cowardly."

    nate @talking2mouth "{size=30}...What?{/size}"

    anabel @talkingmouth "If you want to be free of this life, then remove yourself from it. Don't ask someone else--don't ask the agency--don't ask {i}me{/i}--to pull the trigger."

    pause 1.0

    show anabel surprisedbrow frownmouth with dis

    nate noshine -surprisedbrow @closedbrow talking2mouth "...I hate you."

    anabel @talking2mouth "...I'm..."
    anabel @closedbrow angrymouth "The... the agency has decided you should stay here at Kobukan to maintain a presence for future operations."
    anabel @sadbrow talkingmouth "You are... to have no further responsibility regarding the AZOTH1 project, and are to deny any involvement."
    anabel @closedbrow sadmouth "F-f-further, you, um, you are to continue utilizing the 'Nate' persona, an-and you... are to... operate under my direct supervision for the duration, so that..."
    anabel @sad "Excuse me. I must go."

    hide anabel with dis

    pause 2.0

    show nate tears with dis

    pause 2.0

    show nate cry with dis

    pause 2.0

    narrator "And that's when you walk in."

    show screen currentdate with dis

    show nate happy -cry -tears -noshine:
        xpos 0.33 
        ease 0.2 xpos 0.5 xzoom -1

    stop music
    show screen songsplash("Ranger School Theme", "Zame")
    show screen currentdate with dis
    queue music "audio/music/natechill.ogg"

    red @happy "Hey, Nate!"

    nate @happy "[nate_name]! How you doing? Looks like you found my secret bush base!"

    red @confusedeyebrows talkingmouth "A bush base? What?"

    nate @talkingmouth "Oh, you know, secret bases. They're all the rage in Hoenn. You set 'em up in trees, or carve 'em into hillside caves. And sometimes if you can find a bush that's {i}just{/i} right..."
    nate @talkingmouth "Everyone loves showing off their secret base."

    red @happy "That kinda sounds like the opposite of what the name of a secret base implies it should be."

    nate surprisedbrow frownmouth @winkbrow talkingmouth "Hey, don't {i}debase{/i} them. What they do with their secret bases is their own business."

    red @talking2mouth "Well, for a secret agent, your own secret base kinda sucks. I mean, I just walked in here."

    nate sweat @talkingmouth "...Eh-heh?"

    pause 1.0

    nate @closedbrow talking2mouth "Now, I may have the confidence, style, success in bed, and worldliness of a secret agent, but, uh, I'm not actually one."
    nate @happy "I mean, I've got more in common with a cleaning agent than a secret one. I'm like the computer bug equivalent of bleach."

    pause 1.0

    red @unamusedbrow unamusedmouth "Hm."

    pause 0.5

    red @closedbrow talkingmouth "The forest. The psychic disturbance on your Pokéradar. AZOTH1. The international police. 'Blake.' The--"

    show garden:
        align (0.5, 0.5)
        ease 0.2 rotate 3

    show nate angrybrow frownmouth with dis:
        ease 0.2 ypos 1.2 zoom 1.3

    narrator "Nate leaps towards you and forcefully puts his hand on your mouth, knocking you both backwards onto the ground."

    nate angrybrow frownmouth @angrymouth "{size=30}Shut up! What the hell, dude?! What are you doing?!{/size}"

    narrator "You attempt to answer, but the hand covering your mouth somewhat discourages such activities."

    red @poutmouth unamusedbrow "Mmph."

    nate @surprised "How do you know about all that? Have you been using a listening device?"

    red @poutmouth unamusedbrow "Mmph..."

    nate @closedbrow talking2mouth "Okay."
    nate @talking2mouth "I'm going to let you up. We're going to go somewhere private to continue this conversation."
    nate surprisedbrow frownmouth @angrybrow talking2mouth "{i}Don't{/i} scream. If you try to make a run for it, I will knock you out and drag you to where we need to go."

    red @unamusedbrow talking2mouth "...You're like, a foot shorter than me."

    nate @angryeyebrows closedeyes talking2mouth "Wha--no I'm not! And anyway, being shorter doesn't mean I can't twist you into a pretzel!"

    red @happy "Alright, man. Lead the way."

    nate @surprised "Why are you being so...?"
    nate @closedeyes angryeyebrows angrymouth "Whatever. Come on!"

    stop music fadeout 1.5

    scene blank2 with splitfadefast

    $ PlaySound("drill.ogg")

    queue music "audio/music/potown_start.ogg" noloop
    queue music "audio/music/potown_loop.ogg"

    narrator "Nate leads you through the campus, around the back of the baseball field, and into a warehouse that looks like it might have once held sports equipment."

    scene warehousedark 
    show nate angrybrow frownmouth at night
    with splitfade

    nate @talking2mouth "...So. Mr. [last_name], if that {i}is{/i} your real name..."

    if (last_name != "Sugimori"):
        red night @happy "My birth name was Sugimori, actually."

    nate @angrybrow talking2mouth "Would you {i}be serious{/i} for a moment?!"

    red @talking2mouth "You don't seem like the kind of guy who appreciates when things get too serious."

    nate @sad2eyes talking2mouth "...You don't know anything about me."

    red @unamusedbrow talking2mouth "If that was true, then I don't think you would've just body-checked me into a warehouse on the far side of the school."
    red @closedbrow talking2mouth sweat "On that note, can we open the windows in this thing? I can barely see you."

    pause 1.0

    nate @closedbrow talking2mouth "...Fine."

    scene warehouse
    show nate angrybrow frownmouth

    nate @talking2mouth "Tell me everything you know. And {i}how{/i} you know it."

    red @talkingmouth "Alright."

    narrator "You tell Nate the truth of your memory retention freely."

    red @talkingmouth "...And as far as I can tell, I'm the only one who still remembers. Not even my Pikachu remembers."

    pause 1.0

    nate @talking2mouth "I don't think you're lying."

    red @happy "That's a relief."

    nate @closedbrow talking2mouth "But if you're telling the truth, then BEM651 must have just screwed up the hypnosis, somehow..."

    pause 0.5

    nate @talking2mouth "I don't get it. Why didn't you just hide this information? Keep it to yourself? I had no idea the hypnosis didn't work."

    red @sadbrow talkingmouth "...Honestly, I just wanted to talk to you more, dude. And I'm bad enough with secrets that I figured the truth would come out at some point, so might as well take the initiative."

    nate @sadeyebrows closedeyes angrymouth "Geez. That Frienergy thing really did a number on you."

    pause 0.5

    red @talkingmouth "That's another thing. You knew about Frienergy before anyone else. But you didn't even seem to care."

    nate -angry @closedbrow talking2mouth "Powers like that... honestly, they're a dime a dozen. I can't turn a corner without running into someone with some sort of one-of-a-kind biological idiosyncrasy."

    red @happy "You're an interesting guy. So can you really blame me for wanting to talk to you more, even if it means I get my memories wiped after?"

    nate frownmouth surprisedbrow @talking2mouth "...Damn."

    pause 1.0

    nate @closedbrow talkingmouth "That might be the nicest thing that anyone's ever said to me."

    red @talkingmouth "Pay me back by {i}not{/i} wiping my mind?"

    nate -surprisedbrow @sadbrow talking2mouth "Sorry, [nate_name]. Can't do that."

    red @closedbrow sweat talking2mouth "Worth a shot."

    nate @talking2mouth "Go, BEM651."

    $ sidemonnum = 606
    $ PlaySound("pokemon/ball sound.ogg")
    $ PlaySound("pokemon/cries/606.mp3")

    sidemon "Beeeeheeeyem!"

    red @surprised sweat "Whoa-whoa! Wait, already? Can't we talk, first?"

    nate @sadbrow talkingmouth "What's the point?"

    pause 0.5

    show nate surprisedbrow frownmouth with dis

    red @talkingmouth "Well, what was the point that first time?"

    nate @closedbrow talking2mouth "I... it had been a long time since I'd been able to talk to anyone as myself."
    nate @sadbrow talkingmouth "Sorry. Guess I was just using you as an emotional dumping ground."

    red @talking2mouth "...Want to do it again?"

    nate @sadbrow talkingmouth "Yeah." 
    nate @closedbrow talking2mouth "But I shouldn't. Sorry. Don't know what kinda stuff hangs around in your subconscious."

    call clearscreens() from _call_clearscreens_180
    show blank2 with transeye

    pause 1.0

    narrator "You close your eyes."

    red @closedbrow talkingmouth "Alright. Wipe me."

    nate @closedbrow talking2mouth "I... yeah. Alright. Say 'hey' to the great beyond for me."

    pause 0.5

    nate @talkingmouth "BEM651, standard Lethe Protocol, second grade. Wipe all memory of events from the fifteenth of May, 2004, too."

    stop music fadeout 1.5
    show screen songsplash("Ranger School Theme", "Zame")
    queue music "audio/music/natechill.ogg"

    $ PlaySound("shine.ogg")

    show nate surprisedbrow frownmouth
    hide blank2 
    with transeye2

    nate @talkingmouth "Oh, hey, you're finally awake! That baseball hit you pretty hard, man. Are you alright?"

    pause 1.0

    red @talkingmouth "Yeah, fine, except the hypnosis didn't work again."

    nate @happy "Heh, what? You're such a kidder. I realize my sweet moves can be hypnotizing, but the only tricks here are my sick fakeouts."

    red @unamusedbrow talking2mouth "You're a secret agent working for the international police. Your name is Blake. You've tried to wipe my memories twice, now."

    pause 0.5

    nate angrybrow frownmouth @talking2mouth "Son of a..."
    nate @angry "Alright, sorry, let's try this again."

    red @confused "Do we have to?"

    $ sidemonnum = 606
    $ PlaySound("pokemon/ball sound.ogg")
    $ PlaySound("pokemon/cries/606.mp3")

    nate @talking2mouth "BEM651, standard Lethe Protocol, third grade. Do a deep wipe of all memories involving me--except the part where I sold him out to those ace-holes."

    red @closedbrow talking2mouth "I don't think that's a fair way of describing it."

    $ PlaySound("shine.ogg")

    pause 1.0

    nate -angrybrow -frownmouth @talkingmouth "Hm? Hey, are you alright? It looked like that baseball hit you pretty hard."

    red @talkingmouth "You know, that's funny, considering that my head doesn't hurt at all."

    pause 0.5

    show nate unamusedbrow frownmouth with dis

    red @talkingmouth "And also funny considering that I remember you're a member of interpol named Blake."

    pause 1.0

    show nate angry2eyes angryeyebrows angrymouth with dis
    show warehouse with vpunch

    nate @angry2eyes angryeyebrows angrymouth "Gaaaaah!{w=0.5} 651, do a--"

    show nate surprisedbrow frownmouth with dis:
        ease 0.5 ypos 1.1 zoom 1.2

    red @talking2mouth "Hey, knock it off. It's not working, and if you keep wiping me like that, you're going to give me brain damage or something."

    nate -surprisedbrow @sadbrow angrymouth "Why isn't it working?! How are you resisting this?!"

    red @talking2mouth "I... don't know. I honestly have no idea."
    red @sadbrow talkingmouth "Swear I'm not doing it on purpose."

    pause 0.5

    nate @closedbrow talking2mouth "Damn it. {i}Damn{/i} it."
    nate @sadbrow talking2mouth "If the agency realizes that I left a loose end, then they'll wipe {i}me,{/i} and they'll screw around in your head until they figure out how to remove the right memories."
    nate @angrybrow talking2mouth "And... they {i}won't{/i} stop until they figure out how to remove them."
    nate closedeyes sadeyebrows @talking2mouth "{size=30}What do I do...?{/size}"

    pause 0.5

    show nate surprisedbrow with dis

    red @talking2mouth "You mean what do {i}we{/i} do?"

    nate -surprisedbrow @closedeyes angryeyebrows talking2mouth "There's no 'we' here, [nate_name]."
    nate @sad2brow talking2mouth "I screwed up and now {i}I{/i} need to figure out how to get this mission back on track."

    show nate surprisedbrow with dis

    red @unamusedbrow talking2mouth "Uh, there actually {i}is{/i} a 'we.' You just said that if Interpol finds out I know about you, and them, they'll strap me to a table and pump amnestics into my head."

    nate @talkingmouth sweat "That's not {i}exactly{/i} what I said."

    red @talking2mouth "I read between the lines."

    nate -surprisedbrow @closedbrow talking2mouth "Saying stuff like that, I think you need to {i}lay off{/i} the lines for a bit."

    red @confused "I'm talking to a secret agent, who was sent here to investigate some sort of alien lifeform, and memory-wiped my dormmates."
    red @talkingmouth "I really don't think what I said was all that crazy, in comparison."

    nate @talkingmouth "Fair."

    pause 1.0

    nate @closedbrow talking2mouth "Alright, fine. What do {i}we{/i} do?"

    red @happy "Oh, I've got no idea. You're the secret agent, Blake. You tell me."

    nate @upeyes angryeyebrows talking2mouth "Okay, the {i}first{/i} thing we do is you never call me a secret agent again. Or 'Blake.' Especially in the same sentence. Literally the worst possible thing you could do for OPSEC."
    nate @closedeyes angryeyebrows talking2mouth "In fact, don't even {i}think{/i} of me as Blake. If you do, you might accidentally call me that."

    $ AddEvent("Nate", "NameRevert")

    red @talking2mouth sweat "Sure."

    nate @talkingmouth "Next, we need to contain the information breach. Does anyone else know about this?"

    red @talkingmouth "Like I said before, no. Even my dormmates and Pokémon seemed to have no idea what had just happened."

    nate @talking2mouth "Okay. And you haven't told them since, right?"

    red @talkingmouth "Right."

    nate @talkingmouth "What about the Pokémon on you right now?"

    red @talkingmouth "Left them all in the dorm."

    nate @surprised "Huh?"
    nate angrybrow frownmouth "Hm..."

    pause 1.0

    narrator "Nate inspects your belt, your vest, even looks at your hat closely."

    nate -angrybrow -frownmouth @surprised "You really did. You came here fully expecting to get wiped again."

    red @sadbrow talkingmouth "This isn't a trick. I just wanted to talk."

    nate @sad2eyes sadeyebrows talking2mouth "I... I see. Uh, sorry about being suspicious. Standard protocol."

    pause 0.5

    nate @closedbrow angrymouth "Oh, who am I kidding? There's no standard protocol for this! This has never happened before!"

    red @happy "Hey, focus up. We need to think of a plan, right?"
    red @talkingmouth "Number one: never refer to you by your title again. Number two: make sure no-one else knows. What's next?"

    nate @closedbrow talking2mouth "Right. Number three is, I guess, try to figure out a way to make you being wiped disadvantageous to the agency."

    red @confused "What do you mean?"

    nate @closedbrow talking2mouth "If they want you wiped, you will be."
    nate @sad2eyes angryeyebrows talking2mouth "So... we need to figure out a way to make it so they don't {i}want{/i} to wipe you."

    red @talkingmouth "How?"

    nate @talkingmouth "...Protocol states that if a civilian is a critical part in the success of a mission, then the civilian may be allowed to keep their knowledge, as long as they remain in contact with the agency."
    nate @sad2eyes sadeyebrows talkingmouth "That's how I was brought in. So if I tried to invoke that clause on the behalf of someone else, they'd have a hard time denying me."

    red @happy "Well, that's great, then!"
    red @talkingmouth "I already helped in a mission, right? The whole AZOTH1 thing."

    nate @sadeyebrows sadeyes talking2mouth "Yyyyyeah. You were, uh, at {i}best{/i}, a distraction there."

    red @unamusedbrow talking2mouth "Oi."

    nate @happy "But, hey, you were a really useful distraction! Arguably, though, Blue was even more useful. I mean, trying to punch an alien Pokémon in the face? Your ex has got some balls, if not some brains."

    red @surprised "What? He's not my ex!"

    nate @surprised "Really? With the way he always complained about you, I just assumed... uh, nevermind."

    pause 1.0

    red @closedbrow sweat talking2mouth "Well, which mission can I be a critical part in the success of, then?"

    nate @closedbrow talking2mouth "Good question. I've been sort of gathering side missions in the school year, so far."

    if (IsAfter(18, 5, 2004)):
        $ AddEvent("Nate", "LevelOneAfterBianca")
        nate @talkingmouth "B, Bea, and H have given me leads toward a certain someone that I've been hunting for a while."

    else:
        nate @talkingmouth "Bea and H have given me leads toward a certain someone that I've been hunting for a while."

    pause 0.5

    red @talkingmouth "Your roommates."

    nate @sad2eyes talking2mouth "Yeah."

    red @closedbrow talking2mouth "So even where you sleep at night is determined by your job..."

    nate @winkbrow talkingmouth "Hey, where I sleep at night is {i}my{/i} decision. Well, mine and one other's. Sometimes more than one."

    red @closedbrow talking2mouth "You know what I mean."

    nate @closedbrow sweat talking2mouth "Yeah... alright."
    nate @closedbrow talkingmouth "Truth be told, I've had this dormmate configuration planned for quite a while. Even before co-ed dorms were allowed, I campaigned on Serena's behalf, knowing she was trying to make them happen."

    pause 0.5

    nate @sadbrow talkingmouth "Of course, that didn't really work out, but the old student council was looking for a way to calm down the student body after that fallout, so it still worked out for me."

    pause 0.5

    nate @talkingmouth "Anyway... I can't drag you into one of those missions. At least not right now. I'm done sharing other people's information--if they want you in, then they'll have to ask."

    if (GetRelationshipRank("Hilbert") > 0 or GetRelationshipRank("Bea") > 0 or GetRelationshipRank("Bianca") > 0):
        show nate surprisedbrow frownmouth with dis

    if (GetRelationshipRank("Hilbert") > 0):
        red @talking2mouth "Hilbert's parents were murdered when he was young."

    if (GetRelationshipRank("Bea") > 0):
        red @talking2mouth "Bea and her friend were attacked by some maniac in Galar."

    if (GetRelationshipRank("Hilbert") > 0 or GetRelationshipRank("Bea") > 0):
        nate @talking2mouth "Oh. I guess, uh, you do know a bit."

        if (GetRelationshipRank("Hilbert") > 0 and GetRelationshipRank("Bea") > 0):
            $ ValueChange("Hilbert", 2, 0.25, False)
            $ ValueChange("Bea", 2, 0.75)

            narrator "Nate seems shocked at your knowledge of his own roommates."

            nate -surprisedbrow -frownmouth @talking2mouth "Actually... you know all of it. What's taken me months of research, even before I got into this school, they just... told you?"

            red @sadbrow talkingmouth "Yep."

            nate @talkingmouth "Damn, you're potent. Must have a silver tongue."

            red @talking2mouth "So... what do I do?"

            nate @winkbrow talkingmouth "With that tongue? You tell me."

            red @talkingmouth "Funny guy. I mean, about the mission."

        else:
            if (GetRelationshipRank("Hilbert") > 0):
                $ ValueChange("Hilbert", 3, 0.25)
                
                narrator "Nate seems shocked at your knowledge of his own roommate."

            else:
                $ ValueChange("Bea", 3, 0.75)

                narrator "Nate seems shocked at your knowledge of his own roommate."
            
            nate @talkingmouth "I mean, I guess you don't know {i}everything{/i}, but, still, what you mentioned took me months of research, even before I got into this school."
            
            red @talking2mouth "So... what do I do?"

    else:
        red @closedbrow talking2mouth "So what do I do?"

    if (IsAfter(17, 5, 2004)):
        $ AddEvent("Nate", "Lv1AfterMurder")
        red @sweat talking2mouth "Wait. You mentioned Bianca, as well."
        red @talking2mouth "I know that Bianca's father was murdered after she exposed his name and address on TV."
        red @closedbrow sweat talking2mouth "But everyone knows that, now. Do you think--are you saying..."

        if (GetRelationshipRank("Hilbert") > 0 or GetRelationshipRank("Bea") > 0):
            red @surprised "Are you saying Hilbert and Bea's problems have something to do with the murder of Bianca's father?"

        else:
            red @surprised "Are you saying that Hilbert and Bea have problems that have something to do with the murder of Bianca's father?"

        nate -surprisedbrow -frownmouth @sad2eyes talking2mouth "That's what these 'coincidences' are pointing towards."

        red @surprised "Geez! We need to tell them!"

        nate @talkingmouth "Not yet. I need more information. Knowledge is power."

        red @closedbrow talking2mouth "Kalos is bacon."

        nate @confused "What?"

        red @confused "What?"

        nate @talking2mouth "You're a silly guy, you know that? Anyway, that's our mission."

    else:
        nate @closedbrow talkingmouth "I'm not sure there's anything we {i}can{/i} do, yet. I've got two atrocities. But two that have similar traits can still be a coincidence. I think I need three before we do anything."

        red @confused "So... we're supposed to just sit around with our thumbs up our asses until something terrible happens to someone else?"

        nate @sadbrow talkingmouth "Ideally, nothing like that will happen."
        nate @noshine angryeyebrows talking2mouth "But if it does... that's our mission."

    red @talkingmouth "...Our mission. Okay."

    nate @closedbrow talking2mouth "I'll get in contact with you soon about our next steps."
    nate @talkingmouth "I'm going to talk to my roommates... and you should, too. But don't let them know we're working together, yet."

    pause 1.0

    red @talking2mouth "Hey, uh, thanks for being willing to work with me about this, and not just, like, hitting me on the head really hard."

    nate @sadbrow talkingmouth "I want to make a world where people forget they have fists. Can't start that by whacking off every joe who comes around, even if it's easy."

    red @talkingmouth "A world where people forget they have fists, huh?"

    nate sadbrow @talkingmouth "A peaceful world, [bluecolor]pal{/color}. The only thing that could make all this sacrifice worth it."

    pause 1.0

    nate @happy "Alright, now let's get out of this warehouse. People might think we're having too much of a good time if we stay here for too long, with the way you were banging around earlier."

    red @upeyes talkingmouth "Yeah, yeah. You're the expert on banging around."

    nate @happy "Man, you have no idea."

    scene blank2 with splitfade

    $ persondex["Nate"]["Relationship"] = "Pal"
    $ persondex["Nate"]["RelationshipRank"] = 1

    $ PlaySound("sav.ogg")

    narrator "Your heart shifts as you feel your relationship with Nate evolve from '{color=#0048ff}Friend{/color}' to '{color=#0048ff}Pal{/color}'!"

    stop music fadeout 4.5

    pause 3.0

    scene warehousedark with splitfade

    show anabel sadbrow with Dissolve(3.0)

    pause 3.0

    show anabel closedbrow sadmouth with dis

    pause 3.0

    anabel @talking2mouth "Oh, my boy, my {i}darling{/i} boy. {w=0.5}What have I made of you...?"

    $ playerparty = oldparty

    return

label Nate2:
    stop music fadeout 1.5
    call clearscreens() from _call_clearscreens_181
    scene hall_A2:
        xalign 0.0 yalign 1.0 xpos -100 ypos 1100 zoom 0.7
    with Dissolve(2.0)

    show screen songsplash("Looker Theme Lofi Noir Remix", "AlmightyArceus")
    queue music "audio/music/anabel_start.ogg" noloop
    queue music "audio/music/anabel_loop.ogg"

    stop music fadeout 1.5
    show screen songsplash("Sinis Trio", "Zame")
    queue music "audio/music/natetheme_start.ogg" noloop
    queue music "audio/music/natetheme_loop.ogg"

    narrator "You are heading to Dorm 251 on a mission. Your head is bowed, and your brow furrowed, as you try to think through the particulars of the outrageous plan you have before you."
    narrator "Arriving at the door, you raise your hand and knock."

    $ PlaySound("knock.ogg")

    nate @happy "Coming!"

    pause 1.0

    $ PlaySound("Door_Open1.ogg")

    scene blank with splitfade

    pause 0.5

    scene dorm_A 
    show nate surprisedbrow frownmouth
    with splitfade

    pause 1.0

    nate @talkingmouth "[first_name]? Pal! How are you?"
    nate -surprisedbrow -frownmouth -surprised angrybrow frownmouth @happy "What's the occasion?"

    red @talking2mouth "I want to talk about that project we were working on."

    nate @talking2mouth "Sure thing. That homework, right? Hilbert and Bea are still here, so let's find somewhere private."

    show hilbert angrybrow:
        xpos 1.2
        ease 1.5 xpos 0.75

    show bea angrybrow:
        xpos -0.2
        ease 1.5 xpos 0.25

    narrator "Bea and Hilbert silently walk up to Nate."
    narrator "The atmosphere in the room suddenly gets {i}significantly{/i} heavier. Nate laughs, attempting to defuse the strange heaviness in the air."

    nate -angrybrow -frownmouth @happy "Woah, guys. Looks like you're my bodyguards or something. What're we lining up for?"

    red @sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."

    nate frownmouth @closedbrow talkingmouth "Oh. You... you told them, huh?"

    red @talking2mouth "I understand you want to keep this secret. But secrets just hurt people. The person holding the secret, the person keeping the secret, and..."

    narrator "You nod at Hilbert and Bea."

    red @talking2mouth "The people the secret is about. They deserve to know."

    nate @closedbrow talking2mouth "...Sorry, but that's just not possible."
    nate @sadbrow talkingmouth "My identity's a matter of international security. My mission is, too."

    hilbert @talkingmouth "How can we {i}secure{/i} anything if we don't know anything?"

    bea @closedbrow talkingmouth "An opponent you have no knowledge of cannot be beaten."

    nate @angrybrow talking2mouth "I know! And it's not {i}your{/i} job! It's mine! I signed up for this!"
    nate @sad2eyes angryeyebrows talking2mouth "Ignorance is peace. I've given up my peace, but you two still have a chance."
    nate @talking2mouth sadbrow "Please, for the love of God, take it."

    narrator "Hilbert scoffs."

    hilbert @talkingmouth "If you think there's any peace for me, then you didn't do your research."

    bea @closedbrow talkingmouth "I don't know how I will find my peace, but it will not be through sitting on my arse and waiting for a spiky-haired Unovan to solve my problems."

    show nate closedbrow angrymouth with dis

    narrator "Nate closes his eyes and groans loudly."

    nate frownmouth @talking2mouth "I'm sorry. I can't accept that."
    nate @angrybrow talking2mouth "This is my sacrifice to make. And if you don't let me make it, then..."
    nate @closedbrow angrymouth "Everything I've been through is a waste."

    narrator "Nate suddenly grabs onto his Poké Balls."

    nate angry "Prepare yourself! I'm not holding back! I know I can't wipe you, [nate_name], but...!"

    hilbert @talkingmouth "Fool."

    bea @talking2mouth "You cannot best us in combat!"

    red @talking2mouth "Guys, watch out, he's got some seriously tough Pokémon."

    hilbert @closedbrow happymouth "And we do not?"

    python:
        trainer1 = MakeRed()
        trainer2 = MakeTrainer("Bea", TrainerType.Ally)
        trainer3 = MakeTrainer("Hilbert", TrainerType.Ally)
        nateparty = GetTrainerTeam("Nate") + [Pokemon("Genesect", AimLevel() + 10, moves=[GetMove("nothing")], nickname="PW05")]
        trainer4 = Trainer("Nate", TrainerType.Enemy, nateparty)

    call Battle([trainer1, trainer2, trainer3, trainer4]) from _call_Battle_142
    $ RecordBattle("Nate2")
    
    show screen songsplash("Looker Theme Lofi Noir Remix", "AlmightyArceus")
    queue music "audio/music/anabel_start.ogg" noloop
    queue music "audio/music/anabel_loop.ogg"

    if (not WonBattle("Nate2")):
        jump gameover

    show hilbert angrybrow:
        xpos 0.75
    show nate winkeyes angryeyebrows angrymouth sweat 
    show bea angrybrow:
        xpos 0.25
    with dis

    $ ValueChange("Hilbert", 2, 0.25, False)
    $ ValueChange("Nate", 2, 0.5, False)
    $ ValueChange("Bea", 2, 0.75)

    nate @talking2mouth "...I gotta admit, I was banking a lot on you just giving up when I sent out PW05."

    hilbert @closedbrow talkingmouth "That's the metal-looking one? I thought it was tough at first, but it didn't even do anything."

    bea -angrybrow @closedbrow talkingmouth "Perhaps your training is lacking?"

    nate -angryeyebrows -winkeyes -sweat frownmouth @closedbrow sweat talking2mouth "...You don't need to rub it in, geez."
    nate @sadbrow talkingmouth "I mean, I was up against three members of the Battle Team. That's kinda intense, you know?"

    hilbert @closedbrow talkingmouth "You talk big about protecting people, but you can't even beat three ordinary college students?"

    nate @closedbrow angrymouth "Again, you're {i}Battle Team{/i} members. There's only so much I can do!"

    red @talking2mouth "That's right. There's only so much you can do alone. That's why we're here. To work together."

    pause 0.5
    
    nate @talking2mouth "Well, it's not like I have much of a choice."
    nate @closedbrow talking2mouth "How much do you two know?"

    redmind @surprisedbrow frownmouth "Hm? He caved... that easily? I thought he'd keep arguing, or do some kind of secret agent martial arts on us..."

    bea @talkingmouth "All I know is that you have information about my attacker that you did not share with me."
    bea @sad "From... context clues, I assume he is not imprisoned in Lacunosa anymore."

    nate @closedbrow talking2mouth "...You're right."
    nate @sad2eyes talking2mouth "And H?"

    hilbert @closedbrow talkingmouth "I know you were researching ancient warfare at the Gray Library. You were particularly interested in cannons."
    
    show bea surprisedbrow with dis

    hilbert @sadbrow talkingmouth "...The thing that killed my parents."

    pause 0.5

    bea sadbrow @talkingmouth "Oh. Hilbert, I am deeply sorry for your loss. I cannot imagine your pain."

    hilbert sad @sadbrow talkingmouth "...Nor I yours."

    pause 1.0

    narrator "...A gloomy atmosphere settles onto the group. You think back on your own tragedies..."

    show blank with Dissolve(1.0)

    show cherenshatefultruth behind blank at sepia
    show flashback behind blank at sepia 

    hide blank with Dissolve(2.0)

    pause 3.0

    hide cherenshatefultruth 
    hide flashback
    with Dissolve(3.0)

    narrator "...and suddenly they don't seem so bad."

    pause 1.0

    show nate surprisedbrow frownmouth 
    show bea -sadbrow
    with dis

    red @talking2mouth "So they don't know anything about what happened in the forest, or what you told me then. Actually, they didn't even know about PW05 until you just sent it out."

    nate -surprisedbrow @closedeyes angryeyebrows angrymouth "Well, I really put my foot in it there..."

    red @talking2mouth "I only told them the information you were hiding from them."
    red @sadeyebrows sadeyes talkingmouth "And... Hilbert and I kinda found out about your research on accident."

    hilbert -sad @closedbrow talkingmouth "You should take better care of books, especially books in a public library. Other people need to use those."

    narrator "Nate's eyes flash with recognition."

    nate @closedbrow angrymouth "L'Encyclopédie de Kalos. Of course. I screwed up. Geez, what is the {i}deal?{/i}"
    nate @sadbrow talkingmouth "If the agency saw this laundry list of screwups, they'd really throw the book at me. {w=0.5}...Heh."

    pause 1.0

    nate @talkingmouth "Okay. H, Bea, let me make a long story short. I have a job that gives me access to various official records--police reports, arrest records, warrants, stuff like that."

    show bea talkingmouth
    show hilbert talkingmouth
    show nate surprisedbrow frownmouth
    with dis

    Character("{color=#F87816}Bea{/color} & {color=#353535}Hilbert{/color}") "\"You're a secret agent working for interpol.\""

    show bea -talkingmouth
    show hilbert -talkingmouth
    with dis

    nate -surprisedbrow @angrybrow talking2mouth "[nate_name], you said you didn't tell them about that!"

    red @surprisedbrow talking2mouth "Swear to God, I didn't! I have no idea how they figured it out!"

    hilbert @talkingmouth "I never bought that the suited woman who's been talking to Bianca is a lawyer. She moves too crisply, too purposefully. And I saw her showing a badge to Dean Drayden."

    nate @closedbrow talking2mouth "...You really notice everything, huh."

    bea @closedbrow talking2mouth "She moves with the purpose and precision of a person who is trained for combat. {i}True{/i} combat."

    hilbert @talkingmouth closedbrow "Put those together, and it seems clear she's some sort of agent. I suppose the concept of plainclothes eluded her."

    nate @confused "Okay, but what does {i}she{/i} have to do with me?"

    pause 1.0

    hilbert @talkingmouth "...I don't sleep. As you know. So I hear you... And ever since she arrived... you've been talking in your sleep. Calling out."

    pause 0.5

    hilbert @talkingmouth closedbrow "You've been calling for your mother."

    pause 1.0

    nate @talkingmouth "...I mean, I call a lot of girls Mommy, so that could mean anything."

    bea @surprised "I thought you were a homosexual?"

    nate @happy "Depends on the time of day."

    show dorm_A with vpunch

    hilbert @angry "Silence! We are discussing {i}important{/i} matters here!" 

    nate @confusedbrow talking2mouth "Did you just yell {i}silence{/i}? What is this, some sort of king's court? You some kinda pointy-hatted wizard sitting on a throne, brandishing your staff?"

    hilbert sad "{size=30}Sh-shut up...{/size}"

    bea @closedbrow talking2mouth "It is alright, Hilbert. I thought your 'silence' was very cool."

    nate @happy "Yeah, but you also think Instructor Marshal is cool, Bea."

    bea @surprisedbrow talkingmouth "Is he not?"

    hilbert -sad @closedbrow talkingmouth "Just... let's just get back on track."
    hilbert @talkingmouth "Am I right? Is that purple-haired woman your mother?"

    $ natenicknaming = False

    nate @sad2eyes talking2mouth "...Not exactly. I mean, she's, what, twenty-five? But she's the closest thing I have to one, I guess. Anabel. Not her real name, obviously."
    
    $ natenicknaming = True
    
    nate @closedbrow talkingmouth "If we're actually going to do this, 'together', then she's the one we need to watch out for. I'm a bit fast and loose with the agency's rules."
    nate @sadbrow talkingmouth "She's a fanatic. She's structured her life around them. They're... they're kinda what keeps her alive, gives her purpose."

    hilbert @talkingmouth "...I understand. My parents were also obsessed with their missions."
    hilbert @sadbrow talkingmouth "I remember clearly how they would vaunt and exalt 'Team Plasma's glorious purpose'. They, too, believed that they were going to make a better world."

    pause 0.5

    hilbert @closedbrow angrymouth "Until that better world killed them."

    pause 0.5

    hilbert @talkingmouth "You were the last person to see them alive. Explain, now. No more secrets, no more half-truths, no more omissions. Why did I see you, that day?"

    nate @sadbrow talking2mouth "...H, our deal was just so I could get info from you about my mission in the forest."

    hilbert @talkingmouth "We are beyond the deal now. Our missions are intertwined."
    hilbert @angrybrow angrymouth "I always wanted to do this alone, but thanks to [first_name], I no longer see that as an option."
    hilbert @sadbrow talkingmouth "And if it's not an option for me, then it's also not an option for you."

    nate @unamusedbrow talking2mouth "I don't remember agreeing to that dynamic."

    hilbert @talkingmouth "Your consent is not a necessary part of it."

    nate @closedbrow talkingmouth "{size=30}And {i}that's{/i} why you can never get a date.{/size}"
    nate @talking2mouth "Alright. I'll tell you. But... in front of Bea? [last_name]?"

    hilbert @closedbrow talkingmouth "I repeat. The insulation of my mission has long since been breached. We are all in this together."

    narrator "You raise an eyebrow. Hilbert, of all people, saying 'we're all in this together'? You inspect him closely--his youthful face, though his jaw is set defiantly, seems to be brimming with determination, and even... leadership?"

    pause 0.5

    narrator "You blink."

    pause 0.5

    narrator "And the moment passes."

    nate @closedbrow talking2mouth "Alright. Fine."
    nate @talking2mouth "It's like you said. I'm an agent for Interpol. In 1993, I was assigned to get information on higher-ups in the organization known as 'Team Plasma.'"
    
    bea @surprisedbrow talkingmouth "Um--"

    hilbert @talkingmouth "We can ask questions later. Let him finish."

    bea @closedbrow talking2mouth "Sir."

    nate @confused "...That was weird." 

    redmind @thinking "Oh, good, so I'm not the only person who noticed this."

    nate @talkingmouth "Those higher-ups... were your parents, H. Aldith and Barret von Schwarzdrachen."

    hilbert @closedbrow talkingmouth "So, they {i}were{/i} high-ranking members."
    hilbert @sadbrow talkingmouth "I'd suspected. The organization seemed to put too much responsibility on them for them to be common volunteers, as they claimed."

    nate @sad2eyes talking2mouth "While you were at school... I broke into your house. 679 Stratos Drive. Opelucid City, 10008."

    hilbert "{w=0.5}.{w=0.5}.{w=0.5}."

    nate @closedbrow talkingmouth "I was looking for evidence to link them to a series of Pokémon thefts."

    hilbert @closedbrow talkingmouth "You found it, I assume."

    nate @sadbrow talking2mouth "...I didn't. The house looked, for all the world, like an ordinary, happy, family home."

    hilbert @sadbrow talkingmouth "Appearances can be deceiving."

    nate @closedbrow talkingmouth "I didn't want to come back empty-handed, though. I'd scoped out your house and knew you would come back in several hours, and your parents were away on a business trip. I thought I had plenty of time."
    nate @talkingmouth "I found the study. The drawers were locked--I picked the locks. Nothing but tax forms and mortgage payments." 
    nate @sadbrow talkingmouth "At this point, I was starting to wonder if I even had the right house, you know?"    
    nate @talkingmouth "I went to their laptops and hacked into them. They didn't have any kind of special security, just a standard thumbprint biometric passcode. Easily replicable, even back in 1993."

    nate @talking2mouth "But their laptops didn't have anything either. Emails, files, downloads, even browser history--{i}all{/i} clean."
    nate @closedbrow talking2mouth sweat "Though there were a surprisingly high amount of searches for antique swords."

    hilbert @talkingmouth "My father collected them. Continue."

    nate @talkingmouth "I decided I needed to copy the data from the laptops. Maybe the files were heavily encrypted, or under a layer a cursory hack couldn't breach."
    nate @closedbrow talking2mouth "I removed the motherboard from the laptops and started copying the data from it onto a Black Box. They're a type of indestructible data chip that can store an immense amount of data in a wafer the size of a thumbnail."

    bea @closedbrow talkingmouth "They are not boxes?"

    nate @sadbrow talkingmouth sweat "No, it's just the name."

    bea @talkingmouth "Confusing. Carry on."

    nate @sadbrow talkingmouth "While that was happening, I searched through the rest of the house. I was desperate, at this point, y'know?"
    nate @talking2mouth "A cupboard with a Plasma uniform. A memo on the fridge using Plasma stationary. Even a bottle of orange hair dye! I'd take anything at that point."
    nate @talkingmouth "And that's when I found your bedroom."

    hilbert @closedbrow talking2mouth "...Hmph."

    nate @sadbrow talking2mouth "I never opened the door. I figured a kid's bedroom wouldn't have what I was looking for. That's the kind of sloppiness I grew out of... but back then, I was new to this."

    hilbert @closedbrow talkingmouth "You were right. There was nothing of worth there."

    nate @closedbrow talking2mouth "Well, maybe. I was returning to the office when I suddenly heard a 'whirring' sound coming from outside, in the sky."

    hilbert @talkingmouth "...Yes. I remember that."
    hilbert @talkingmouth "Everyone who lived in Opelucid City that day does."

    nate @talking2mouth "Up in the sky... I could barely believe it... was a giant, flying, airship. Some sort of flying frigate."

    hilbert @talkingmouth "Yes. The Plasma frigate. A secret weapon built by Team Plasma to assist in their goal of..."
    hilbert @closedbrow talkingmouth "Whatever their goal was."

    nate @closedbrow talking2mouth "There was barely a second's warning. It fired. And the {i}very{/i} first house it fired on was yours."
    nate @sadbrow talking2mouth "And {i}right{/i} as its cannon went off, you opened the front door. Back home a whole four hours early."

    hilbert @closedbrow talkingmouth "I remember."

    nate @sadbrow talking2mouth "Why were you back so early? I've never been able to figure that out."

    hilbert @closedbrow talkingmouth "It was a Tuesday. Tuesdays were half-days at my school."

    nate @closedbrow talking2mouth "Damn. Half days, huh..."

    show nate:
        ease 0.5 xzoom -1

    narrator "Nate turns to Bea, and begins addressing her."

    nate @talking2mouth "There was this kid, right there, a civilian, in front of me, and some sort of unidentified projectile was being fired at the house."
    nate @talking2mouth "I knew it meant giving up the Black Box, but I couldn't let him die. So I ran at him at full speed and tackled him. We skidded on the cobblestones for a few feet, and then..."

    hilbert @talkingmouth "And then my home was destroyed."
    hilbert @sadbrow talkingmouth "When Nate tackled me, I hit my head on the ground. Seeing my house become encased in a solid crystal of ice a moment later was too much... I passed out."

    nate @talking2mouth "...We only looked in each other's eyes for a moment, I guess."

    hilbert @talkingmouth "But I never forgot how you looked. You looked at me without any feeling. I could see a machine behind those eyes."

    nate sad "A... a machine?"

    pause 1.0

    nate -sad @talking2mouth "I never forgot how you looked, either. You were afraid. Just a little kid, terrified of me. Who was I? What was I doing?"
    nate @sad2brow sadmouth "I'd broken into your house, rummaged through your stuff, I was trying to get your parents arrested... and when I tackled you, you thought I was trying to hurt you."
    nate @closedbrow talking2mouth "I remember seeing that fear and thinking 'that's not who I want to be'. 'I want to be someone who makes people feel safe.'"
    nate @talking2mouth "I'd been trained for years to act a certain kind of way. To discard things like 'emotions' or 'self' unless they helped in the mission."
    nate @sadbrow talkingmouth "One look at your eyes undid all that for me."

    hilbert @sadbrow talkingmouth "I apologize. I'm sure that has made your job harder."

    nate sadbrow @happy "You don't know half of it, H."

    pause 0.5

    nate @talkingmouth "...So, that's how we met. It's a funny coincidence that, a decade later, we'd learn each other's names."

    hilbert @closedbrow talkingmouth "I have a question."
    hilbert @sadbrow talkingmouth "But I believe Bea has dibs."

    bea @talkingmouth "Yes. Please pardon me for this question, as I am sure the answer is very personal."
    bea @talkingmouth "If this happened in 1993, then... you, Nate, must have been... {i}quite{/i} young?"

    nate @closedbrow talking2mouth "...Yeah."

    bea @talking2mouth "May I assume there's a story there?"

    nate @talking2mouth "Well... I'm a bit older than I look. Makeup and contouring does wonders for changing the shape of your face."
    nate @talkingmouth "But that can't explain all of it, of course."

    pause 1.0

    show nate angryeyebrows sad2eyes frownmouth with dis

    narrator "Nate looks at you meaningfully."
    narrator "What meaning you're supposed to derive from this, you're not sure."

    nate -sad2eyes -angryeyebrows @talking2mouth "Have you ever heard of Blake Hall?"

    show bea surprisedbrow frownmouth
    show hilbert surprisedbrow frownmouth
    with dis

    $ PlaySound("idea.ogg")

    pause 1.0

    hilbert -surprisedbrow -frownmouth -surprised @talkingmouth "No."

    bea -surprisedbrow -frownmouth -surprised @talkingmouth "Is he a country singer?"

    nate @confused sweat "Why does everyone say that...?"
    nate @closedbrow talking2mouth "No, he's not a country singer. He {i}was{/i} the President of Altru Inc."

    pause 1.0

    hilbert @talkingmouth "That means nothing to anybody here."

    nate @angrybrow talking2mouth "...They're an energy company in Almia."

    bea @talkingmouth "Beg pardon? Alola?"

    nate angry "Wha--no, Almia! {i}Almia?!{/i} You know, the region with the most energy-efficient power grid?! The highest number of Pokémon Rangers per capita?! The home of the world's largest Wailord?!"

    pause 1.0

    nate -angry @sadbrow sweat talking2mouth "Really? Nothing?"

    hilbert @talkingmouth "I don't pay attention to regions that don't have Pokémon Leagues."

    bea @closedbrow talkingmouth "And I am not very good at geography."

    redmind @sadbrow frownmouth "My people."

    nate frownmouth @closedbrow talking2mouth "Fine, fine, whatever, I guess it doesn't matter. I mean, I gave up everything to {size=30}bring the region peace{/size}{size=27}, and keep the world{/size}{size=24} safe, but sure, I guess{/size}{size=21} it's fine if{/size}{size=18} no-one knows.{/size}{size=15} Probably for the best.{/size}"

    narrator "Nate trails off, muttering discontentedly."

    pause 1.0

    bea @sadbrow talking2mouth "Please continue. Now's your chance to tell us what you did."

    nate -frownmouth@closedbrow talking2mouth "...Yeah, you're right."

    pause 0.5

    nate @talkingmouth "Blake Hall was my father."

    hilbert surprised @closedbrow talking2mouth "Hm."

    nate @closedbrow talkingmouth "And he was an evil megalomaniac."

    hilbert -surprisedbrow -frownmouth -surprised @surprisedbrow talkingmouth "Oh."

    nate frownmouth @closedbrow talkingmouth "...He used his energy company to put a stranglehold on the region. He jacked up prices for competitors, charged the Ranger bases exorbitant rates, and drove enemies out of business without even offering to buy them."
    nate @sadbrow talkingmouth "But that's just being a good businessman. The 'really' evil part was when he tried to get control over all the wild Pokémon in the region."

    nate @talking2mouth "...Almia doesn't have a lot of trainers. Many people don't even use Poké Balls. He would have been able to tell almost any Pokémon in the region to do anything, and they would."
    nate @closedbrow talkingmouth "He wouldn't even have to jack up prices on people he didn't like. He could just send the Pokémon to attack their shops, their homes, and their family..."
    nate @sad2eyes talking2mouth "And because they were wild Pokémon, there was no way they could be traced back to him."

    pause 1.0

    hilbert @talkingmouth "What do you mean... 'gain control'?"

    nate @closedbrow sweat talking2mouth "He had a giant tower that emitted brainwashing beams."

    hilbert @closedbrow talking2mouth "That beggars belief."

    nate @angrybrow talking2mouth "{i}Your{/i} story involved a giant flying ship armed with a weapon that hasn't been used for thousands of years."
    
    hilbert @sadbrow talkingmouth "Fair point."

    bea @talkingmouth "What did you do?"

    nate @talking2mouth "...He groomed me to be his successor. My great-grandfather, Doyle M. Hall, founded Altru, and my grandfather Brighton took up the reigns after. My father, Blake, inherited the company when he was only sixteen." 
    nate @sadbrow talkingmouth "I was meant to be next."
    nate @sadbrow talkingmouth "He told me to be cold. To calculate the face I showed the world, to be whichever person could make the most profit out of whatever moment I found myself in."
    nate @talkingmouth "And I believed in that philosophy. But my profit is peace."

    pause 1.0

    nate @talkingmouth "...I calculated that a life spent looking over my shoulder for Rangers was one that would have less profit, in terms of peace, than a normal life as a Ranger, helping people."
    nate @closedbrow talking2mouth "I ratted him out. The Rangers arrested him, tied him up a smidgen on the tight side, and took him off somewhere else."
    nate @closedbrow talking2mouth "That should've been the end of it. But... I knew too much. I knew the schematics for the Incredible Machine. I'd been in communications with the Rangers for several months, too, so I knew a bit about how they operated."
    nate @sad2eyes talking2mouth "Finally... I knew just how close the shadows were to Almia. And anyone who sees under society's blanket of peace is a threat to that peace."

    pause 0.5

    nate @talking2mouth "Interpol contacted me. They asked me if I wanted to help other regions like I had Almia."

    pause 1.0

    nate @talkingmouth noshine "And like a dumbass, I said 'yes.'"

    pause 1.0

    nate @closedbrow talking2mouth "So. That's my story. That's how it happened. And that's... I ended up as a secret agent."
    nate @talkingmouth sadbrow "Betrayed by his own child. His only family. Must've sucked. Almost as much as having him as a Dad did."
    nate @closedbrow talking2mouth "Good riddance, honestly."

    hilbert @talkingmouth "Seems we have something in common. Both our parents worked for shadowy organizations that decided our fate without our consent."

    pause 0.5

    nate @sad2eyes talking2mouth "...H, I think you're being a bit hard on your family."

    hilbert @angrybrow talkingmouth "Elaborate."

    nate @talkingmouth "I went through your entire house with a fine-toothed comb, and didn't find {i}anything{/i} about their work."

    hilbert @closedbrow talkingmouth "They were careful."

    nate @sadbrow talkingmouth "I think they were {i}caring{/i}, H. They didn't bring their work home because they didn't want you caught up in it. Maybe they didn't even want you to know what they did?"
    nate @sad2eyes angryeyebrows talking2mouth "That's a far cry from my Dad, who thought it was more important to teach me how to blackmail someone than it was to teach me how to play baseball."

    hilbert @closedbrow talkingmouth "They said, to my face, that their mission was the most important thing in their life."
    hilbert @talkingmouth "I'm under no delusions as to what their priorities were."

    nate @closedbrow talking2mouth "Alright. Well, you said you had one more question, right?"

    hilbert @talkingmouth "Yes. In your story about breaking into my house, you never saw my parents."

    nate @talking2mouth "Right. They were at work."

    hilbert @talkingmouth "That's what I thought, too. But their bodies were found in the rubble of my house, once the ice melted."

    nate @sad2eyes talking2mouth "I... I can't explain that. I'm not aware of the particulars of that situation, though I could look up the autopsy reports from then, if you give me a while."

    hilbert @talkingmouth "Their bodies were found {i}in the house.{/i}"
    hilbert @closedbrow talkingmouth "How can it be you searched the entire house and didn't find them?"

    nate @sad2eyes talking2mouth "I suppose there's a very small chance that they were in your bedroom... but they would've had to have been there, completely silent, for four-ish hours."
    nate @closedbrow talkingmouth "That doesn't seem likely."

    hilbert @closedbrow angrymouth "Damn your lack of curiosity."

    nate @upeyes talking2mouth "Believe me, I'm kicking myself about it, too."

    bea @talkingmouth "I apologize for the interruption, but I would still like my question to be answered, if at all possible."

    nate @surprisedbrow talking2mouth "Oh, yeah, sorry! You were so quiet, I, uh, forgot you were there. What question was this?"

    pause 0.5

    bea @angrybrow talkingmouth "...Is the person who ruined my brother and I's life in prison or not?"

    nate @sadbrow talking2mouth "Oh. Right. Sorry..."
    nate @closedbrow sweat talkingmouth "I don't have any hard evidence yet. I'm still waiting for my Lacunosan contacts to get back to me."
    nate @talking2mouth "But... the way Melvin Whittaker was killed... is consistent with a certain man associated with Team Plasma."
    nate @talking2mouth "Further, I believe that the Unovan national who was deported back to Unova--the one who attacked you--is that same man."
    nate @talking2mouth "Finally, I believe that the person who ordered the attack on Opelucid is the same man responsible for the first two crimes."

    pause 1.0

    nate @talking2mouth "It's all a bunch of coincidences so far, but the coincidences are lining up in a way that they usually don't if they're {i}actually{/i} just coincidences."

    pause 0.5

    show nate surprisedbrow
    show hilbert surprisedbrow
    with dis

    bea @talkingmouth "...When are we going to bring Hilda and Bianca into this, then?"

    hilbert -surprisedbrow @talkingmouth "What?"

    bea @talkingmouth "This monster's actions have influenced their lives just as much as ours, no? We should tell them everything we know."

    nate @sadbrow talkingmouth "Look, I get where you're coming from, but {i}everyone{/i} who knows something about this is another liability--another link in the chain that could break under pressure."

    pause 0.5

    bea @talkingmouth "Why do you think Bianca and Hilda will break?"

    nate -surprisedbrow frownmouth @surprisedbrow talking2mouth "I... I mean, I didn't say that--"

    bea @angrybrow talking2mouth "Hilbert is profoundly mentally unstable." 
    
    hilbert @closedbrow talkingmouth "{size=30}Rude.{/size}"
    
    bea @talkingmouth "I am, to put it lightly, scatterbrained. On a {i}good{/i} day."
    bea @closedbrow talking2mouth "Hilda is responsible, competent, and kind. Bianca is intelligent, generous, and has suffered just as much as any of us."
    bea @talkingmouth "We will bring them in."

    nate @sweat talkingmouth "Wait, I thought you were asking?"

    bea @talkingmouth "I was. But it appears that, occasionally, I {i}can{/i} come to a decision by myself."
    bea @closedbrow talkingmouth "I suppose I have {i}you{/i} to thank for that, [first_name]."

    red @sadbrow talkingmouth "Happy to help."
    red @talking2mouth "And I agree with Bea. If anything, I should be the one who {i}isn't{/i} part of this mission. But you can't wipe me, so..."

    hilbert @sadbrow talkingmouth "I... don't think we should get Hilda involved. But I agree about Bianca. And I suppose I'm outvoted on the Hilda front."

    nate @sadbrow talkingmouth "...God, what have I gotten myself into? What have I gotten {i}these civilians{/i} into?"

    hilbert @talkingmouth "We've always been a part of it."
    hilbert @closedbrow talkingmouth "The only difference is now we do not have the luxury of doing it alone."

    bea @talkingmouth "Now we do not {i}have to{/i} do it alone."

    pause 1.0

    nate @talking2mouth "Alright."

    pause 1.0

    nate @closedbrow talking2mouth "I'll message everyone to meet up later. Might be hours, might be weeks, might be months. I can't know yet."
    nate @sadbrow talkingmouth "Stay safe until then. Not a word of this to anyone. Keep your head down, eyes on the ground. If Anabel gets a whiff of this, it's all over. You guys get wiped, [first_name] gets recruited, and I get reassigned to Orre under the name 'Skrub.'"

    pause 0.5

    nate @sad2eyes talking2mouth "...This isn't going to be safe. When it's time to move, we'll need to go hard and fast."
    nate @talking2mouth "Stay on your toes. Keep your [bluecolor]blades{/color} sharp."

    pause 1.0

    nate closedbrow frownmouth @talkingmouth "H?"

    hilbert @talkingmouth "Let's move."

    hide hilbert 
    hide bea
    hide nate
    with dis

    $ oldrelationship = GetRelationship("Nate")
    $ persondex["Nate"]["Relationship"] = "Blade"
    $ persondex["Nate"]["RelationshipRank"] = 2

    $ PlaySound("sav.ogg")

    narrator "Your heart shifts as you feel your relationship with Nate evolve from '{color=#0048ff}[oldrelationship]{/color}' to '{color=#0048ff}Blade{/color}'!"

    return