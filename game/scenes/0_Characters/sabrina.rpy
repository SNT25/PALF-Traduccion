label Sabrina1:
    if (IsAfter(1, 5, 2004)):
        queue music "audio/music/lavender_start.ogg" noloop
        queue music "audio/music/lavender_loop.ogg"

        scene academyold with Dissolve(1.0)

        narrator "You're walking across campus when you suddenly get a strange feeling, somewhat like static, in the back of your mind."

        redmind @sadbrow frownmouth "...Oh, man, am I about to have a stroke? I'm way too young for that."

        redmind @surprised "[sabrinacolor]...It is not a stroke.{/color}"

        redmind @surprised "Sabrina? You're...?"

        pause 1.0

        redmind "[sabrinacolor]I wished to... I thought that...{/color}"

        redmind @sad "[sabrinacolor]N-nevermind. This was a foolish idea. I should not have reached out.{/color}"

        pause 1.0

        redmind @sad2eyes frownmouth "Are you... sure?"

        narrator "You wait for a bit, but hear no response."

        redmind @sadbrow frownmouth "Alright."

        narrator "You carry on, doing your best to avoid thinking about Sabrina, in case that made your mind 'louder.'"

        redmind @closedbrow frownmouth "I don't know, exactly, if this'll work, but hopefully she appreciates it."

        pause 1.0

        show academyold with vpunch

        redmind @surprised "[sabrinacolor]I do.{/color}"

        redmind @confusedeyebrows frownmouth "Sabrina, you're giving me some mixed messages here. If you want me to stay away, I will."

        if (GetRelationship("Sabrina") == "...?"):
            redmind @sweat closedbrow frownmouth "I mean, I didn't the first time, but I will {i}now.{/i}"

        redmind @closedbrow frownmouth "If you want me to reach out, I'll do that, even more happily. But I'm going to need you to pick a lane."

        pause 1.0

        redmind @poutmouth upeyes "I mean, you can see how it's a bit unfair to tell me to stay away, then pop into my head whenever you want to say something?"
        redmind @frownmouth "Like, I get you can't help but read my thoughts, but these long-range connections are a voluntary thing, right?"

        redmind @surprised "[sabrinacolor]This is not a long-range connection.{/color}"

        red @talkingmouth "Hm? Oh, but that must mean..."

        narrator "You see a flash of steel-blue hair around the corner of the academy building."

        red @talkingmouth "Oh. Hey."

        show sabrina casualoldhair:
            xpos 1.2
            ease 2.0 xpos 0.8

        pause 1.0

        sabrina @talking2mouth "Hello."

        pause 1.0

        red @talkingmouth "You look good."

        sabrina @sad2eyes talking2mouth "I cannot begin to describe how tiresome and overplayed such a compliment is to me."

        red @unamusedeyesbrows playfuleyes unamusedmouth "{w=0.5}.{w=0.5}.{w=0.5}."
        red @unamusedeyesbrows playfuleyes talking2mouth "Great. That's... that's fantastic. Love it."

        show sabrina:
            xpos 0.8
            ease 0.5 xpos 0.5

        sabrina @talking2mouth "...I wished to talk to you."

        red @happy "We're talking."

        if (HasEvent("Sabrina", "Apologized")):
            sabrina @talkingmouth "So we are."

        else:
            $ AddEvent("Sabrina", "Apologized")
            sabrina @sad2eyes talking2mouth "I think... maybe... I was a bit harsh before. When I told you to 'stay away.' You were only trying to help me."
            
            if (rescuedsabrina and GetRelationshipRank("Sabrina") >= 1 or GetRelationship("Sabrina") == "...?"):
                sabrina @sadmouth "And then I yelled at you for rescuing me. Yelled, instead of thanking you. That was... wrong of me."

            red @sadeyebrows sadeyes talkingmouth "High-stress situation. I get it."

            pause 1.0

            sabrina @talking2mouth "I want to say... 'thank you.' Properly."

            call clearscreens() from _call_clearscreens_144
            show sabrinatakesabreath with Dissolve(2.0)

            pause 6.0

            sabrina @talking2mouth "{i}Thank you, [first_name].{/i}"

            pause 1.0

            red @happy "Hey, it's nothing."

            hide sabrinatakesabreath
            show screen currentdate
            with dis

        if (GetRelationship("Sabrina") == "...?"):
            red @talkingmouth "So. Are we still friends? I realize that we only became friends because I, uh, ignored your request--"

            sabrina @sad2eyes talking2mouth "Command."

            show sabrina surprisedbrow with dis

            red @happy "You're not Janine. It doesn't really {i}feel{/i} like a command, coming from you."

            show sabrina sadbrow poutmouth poutface with dis

            sabrina "Hmph."

            red @talkingmouth "Anyway, I ignored your request to stay away. And, correct me if I'm wrong, you didn't seem to {i}hate{/i} it."

            show sabrina sadbrow -poutmouth -poutface with dis

            pause 0.5

            red @happy "Right, not hearing a correction. Moving on, then."

        else:
            red @talkingmouth "So. What's my current status? You made that request that I stay away--"

            sabrina @sad2eyes talking2mouth "Command."

            show sabrina surprisedbrow with dis

            red @happy "You're not Janine. It doesn't really {i}feel{/i} like a command, coming from you."

            show sabrina sadbrow poutmouth poutface with dis

            sabrina "Hmph."

            red @talkingmouth "Anyway, you made that request. Is it still valid? Is that what you want? Because if so, you're doing a pretty bad job of making me believe it."
            red @talkingmouth "Like, it would be super-easy to get me to drop everything. Just say 'stay away' again. Right now."

            show sabrina sadbrow -poutmouth -poutface with dis

            pause 0.5

            red @happy "Right, I'm not hearing anything. Moving on, then."

        sabrina @talking2mouth "Wait. I don't... I don't want to have to make a decision."

        red @sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."

        sabrina @talking2mouth "Not right now. Please. Give me some more time to understand... how I feel."

        red @talking2mouth "...Alright."

        pause 1.0

        red @sadbrow talkingmouth "Well, how {i}do{/i} you feel? I mean, what happened with those two ace trainers, and all..."

        sabrina @talking2mouth "A symptom of a larger threat. They were merely the hand that acted on society's behalf."

        red @confused "What?"

        sabrina @talking2mouth "It's not the first time I've heard thoughts about how people might seek to... to 'use' me."
        sabrina @sad2eyes talking2mouth "I paid them no heed. Surely their cruel thoughts were just idle fantasy, as so many others had been."

        pause 0.5

        sabrina @talking2mouth "Perhaps if I had read their thoughts more deeply, I would have seen the full extent of their malignance. Perhaps I should have embraced my nature as a witch much sooner."

        red @sadbrow talking2mouth "Well, you certainly got back at them."

        sabrina -sadbrow @talking2mouth "What I did was petty and underhanded. It is beneath me. I should have..."

        pause 0.5

        sabrina @closedbrow talking2mouth "Well, I cannot deny it was satisfying in the moment. But the momentary pleasures of others have plagued my mind for too long. I seek not to stoop to their level."

        red @talkingmouth "Don't be so hard on yourself."

        sabrina @talking2mouth "Perhaps it is a remnant of my upbringing."

        red @surprisedbrow frownmouth "Hm?"

        sabrina @talking2mouth "In the Esper village where I was born, we were taught to be caretakers for the rest of humanity."

        red @confused "Caretakers? What, like Euthymics are sheep, and you're the shepherds?"

        sabrina @talking2mouth "Quite like that, actually."
        sabrina @sadbrow talking2mouth "Of course, these infantile philosophies that propped us up as saviors and guiders of the common man are nothing I subscribe to any more."

        pause 0.5

        sabrina @talking2mouth "Though, besides the arrogance it might instill in its adherents, it was a non-harmful belief. Its core tenet was that we must never use our blessings against the Euthymics."

        pause 0.5

        red @talkingmouth "...So, uh, how did that work with your, uh, inability to turn it off?"

        sabrina @talking2mouth "About as well as you could imagine."

        red @talkingmouth "...Is it, uh, is it wrong of me to ask what your relationship with your parents is like?"

        sabrina @talking2mouth "...I do not know of them."

        red @surprised "What?!"

        sabrina @talking2mouth "I was deposited on the doorstep of an orphanage in Saffron City. My powers were discovered when a spoon I carelessly tossed bent."
        sabrina @closedbrow talking2mouth "I do not remember my time at the orphanage. Emissaries from an Esper village on Mount Silver claimed me, and brought me back."

        pause 1.0

        sabrina @talking2mouth "I lived in that village until I was... removed."

        red @talkingmouth "Removed?"

        sabrina @talking2mouth "I would leave the village and stay in Johto once in a while. To try and acclimatize myself to the people around me."
        sabrina @sadbrow talking2mouth "During these trips, I found myself some friends of a... a fouler bent. The Esper village taught me restraint. To conceal." 
        sabrina @talkingmouth "My new friends allowed me to use my powers as I wanted. They encouraged me to see them as a tool, not as a burden."

        pause 1.0

        sabrina @talkingmouth "We were free. Free of societies' restraints and rules. I found myself gravitating towards those who were as shunned by society as I. Misfits and outcasts. Criminals, even."
        sabrina @talking2mouth "They saw me as a good luck charm, or a mascot of the company, perhaps. They knew of my powers, but did not fear them. They sought to use them, as I did."

        pause 0.5

        sabrina @talking2mouth "But then... one day... we received orders to march on Saffron City. The place of my birth, I'd assumed. I did not wish to leave Johto. I did not wish to permanently leave the village. I refused."

        pause 0.5

        sabrina @talking2mouth "None of my new friends came back."
        sabrina @sadbrow talking2mouth "Perhaps that is why I did not go with them. But I had not the strength to tell them to stay. We were not a group that allowed ourselves to be 'told' anything."

        pause 0.5

        sabrina @talking2mouth "The village elder received a letter. The day after my eighteenth birthday, he informed me as to its contents."
        sabrina @sadbrow talking2mouth "I had been found out. One of my friends from the city had dropped my name. The Kanto and Johto police force were now aware of a powerful, unregistered, Esper who was working alongside a group that had..."
        sabrina @talking2mouth "Had attempted something dreadful in Saffron."
        sabrina @sadbrow talking2mouth "It was only the delicate political situation regarding jurisdiction over Mount Silver that prevented the authorities from marching up the mountain to claim me."

        pause 1.0

        sabrina @talking2mouth "The Elder, then, knew what I had done. How I had used my powers. He knew that I was not the victim of my telepathy, but that I revelled in the power it gave me over others."

        pause 0.5

        red @sadbrow talking2mouth "Is that true? Did you really feel that way?"

        sabrina @sad2brow sadmouth "I find... much comfort in your inability to pluck the answer from my mind, as I would certainly have done to you."
        sabrina @talking2mouth "I fled. I fled instantly, giving no thought to my village, nor to the home I might have had in Saffron."

        sabrina @talking2mouth "I ended up as far away from the Indigo League as I could. I ended up in Kobukan. And I continued as I had. Sneaking, stealing, cheating and scamming, until..."

        pause 1.0

        red @talkingmouth "Until Instructor Will."

        sabrina @talkingmouth "Until Instructor Will."

        pause 1.0

        sabrina @talking2mouth "My village had taught me that my powers were a burden. That they were the instrument of ascendancy for the lesser peoples around me."
        sabrina @talking2mouth "My friends from the city taught me that my powers were a weapon. That they enabled me to take what I wanted, from whoever I wanted--even from their minds."

        pause 0.5

        sabrina @talking2mouth "But Instructor Will used his to entertain. When I felt the psychic hum of another Esper at that blackjack table, I was certain that I'd been found out, and I would finally go to prison."
        sabrina @sadbrow talkingmouth "Perhaps {i}that{/i} is where I could finally be at home."

        show blank2
        show will 
        with dis

        will @happy "'Well, now, seems like you've had quite a lucky streak, Miss! How about a drink? On the house, of course.'"
        will @winkbrow talkingmouth "'Oh, but... I'll need to see some ID. Just routine, of course. I can't imagine what skincare routine you use to keep yourself looking so young and fresh, but I am {i}jealous!{/i}'"

        hide blank2
        hide will 
        with dis

        pause 1.0

        sabrina @talking2mouth "It was a ridiculous show. But he got me out of that room without any of the other, angry, patrons ever guessing. I retained my freedom for one more day. I returned to my apartment baffled by his generosity."

        pause 0.5

        sabrina @talking2mouth "I'd... heard some of my old friends had a hideout somewhere in Inspira. I was on my way to find them when Instructor Will tracked me down."
        
        redmind @thinking "A hideout in Inspira... why is this ringing a bell?"

        $ ValueChange("Silver", 3, 0.75)

        narrator "Your understanding of Silver increased!"

        red @talking2mouth "You said Instructor Will {i}tracked you down?{/i}"
        
        sabrina @talking2mouth "I was. Am. Unaccustomed to people able to get the drop on me. A strange man, at night, who I didn't hear coming... I'm sure you can imagine my fear."

        pause 0.5

        sabrina @talkingmouth sadbrow "I had nothing to fear. He asked me if I had a place to stay for the night. I responded I did, and he gave me a phone number to call if I ever wanted more out of life."
        sabrina @closedbrow talking2mouth "The next day, I called it."
        sabrina @talkingmouth "And the day after, I had a job at the casino."

        pause 0.5

        sabrina @talkingmouth "It turns out they will hire Espers pretty much on-sight. I wasn't even old enough to gamble there, but I {i}was{/i} old enough to work, so they taught me how to shuffle a deck of cards, and... well, that was that."
        sabrina @talking2mouth "It was a fun job, though I hesitate to call listening to a chorus of rapacious crows and cries of financial despair fun... but it was. 'Fun.'"
        sabrina @talking2mouth "I suppose I've no room to judge. My avarice was comparable, and mine was for no greater reason than that I didn't want to feel constrained."

        pause 0.5

        red @talkingmouth "...You quit the job, though."

        sabrina @talking2mouth "I did. When I left the school after..."

        pause 0.5

        sabrina @closedbrow talking2mouth "Well, you know."
        sabrina @talking2mouth "I did it on the spur of the moment, but... Instructor Will doesn't work there anymore, and I must confess I find it a lot less fun when I'm not aside him."
        sabrina @talking2mouth "I think I will remain gone, though I'm certain they'd hire me back."

        pause 1.0

        if (IsBefore(4, 10, 2004)):
            sabrina @talking2mouth "I should look for something else, though. A new job. I have enough from my previous work... and other sources... to pay my way through the first semester of Kobukan, but I still need a job to pay through the second."

        else:
            sabrina @talking2mouth "I should look for something else, though. A new job. I had enough from my previous work... and other sources... to pay my way through the first semester of Kobukan, but I still need a job to pay through the current."

        red @talkingmouth "Need help on the job hunt?"

        sabrina @talkingmouth "It's actually quite easy to find a job for someone with my skillset."

        red @closedbrow talking2mouth "Must be nice.{w=0.5} Aside from all the parts that aren't, I mean."

        pause 1.0

        sabrina @talking2mouth "Yes."

        pause 1.0

        sabrina @sadbrow talking2mouth "...I've now revealed myself to you."

        red @lightblush frownmouth surprisedbrow "{w=0.5}.{w=0.5}.{w=0.5}."

        sabrina @closedeyes angryeyebrows angrymouth "Perverted man."

        red @confusedeyebrows playfuleyes talking2mouth "That was {i}entirely{/i} on you. My mind was chaste and dry as a monk's wine cellar before you said that."

        sabrina @sadbrow talking2mouth "...Enough of that. I've revealed the truth of myself. If it were you who had exposed my secrets, instead of the other way around, this is what you would know."

        pause 0.5

        sabrina @talking2mouth "I have no right, now, to ask you to keep this secret. But as penance, I place my faith in your hands."

        red @confusedeyebrows talkingmouth "What? Sabrina? What are you saying?"

        sabrina @sadbrow talking2mouth "I am saying that the guilt I have felt for the part I played in the events of the first of May have torn me apart ever since." 
        sabrina @sadbrow talking2mouth "I can no longer bear to carry that guilt without giving you something to pierce me with just as deeply as I pierced you."

        pause 1.0

        red @unamusedeyebrows playfuleyes talking2mouth "Okay, now you're doing it on purpose."

        sabrina @angrybrow talking2mouth blush "Can I not use theatrical language without... without {i}everything{/i} I say being intepreted in the {i}horniest{/i} possible context?!"

        red @happy "If it's any consolation, I'd give all of my friends a hard time about that kinda bone-headed word choice."

        sabrina @talking2mouth "...Friends?"

        red @talkingmouth "Yeah, you took too long to decide what we are. So I figured I'd go ahead and pull the trigger on that."
        red @happy "I mean, come on, both of us were dragged in front of the entire school, and had everyone say that we've got crazy mind powers. We're power buddies, you know?"

        sabrina @closedbrow talking2mouth "...Power buddies. A ridiculous notion. Our powers can only serve to divide us."

        red @sadbrow talkingmouth "...I think that's a self-fulfilling prophecy. But you're the one who can see the future. So what do I know?"

        pause 1.0

        sabrina @talkingmouth "You {i}do{/i} know more than you let on. It is foolish of me to continually underestimate you. Every time we talk, I am caught off-guard by your flashes of insight, seemingly without thinking about them."

        pause 0.5

        sabrina @sadbrow talking2mouth "...What is this all in service of?"

        red @happy "C'mon. You don't need to be a mind reader to know that. It's the only thing I've ever wanted, besides to be a Pokémon Champion."

        pause 1.0

        if (GetRelationship("Sabrina") != "...?"):
            red @sadbrow talkingmouth "I want to be your friend, Sabrina. For real."

        else:
            red @sadbrow talkingmouth "I want to be your friend, Sabrina. For real, this time. No takesie-backsies, no backing out, no oaths of friendship that anyone revokes after we disappear into a forest for a week."

            sabrina @talking2mouth "It seems unlikely that'll happen again."

            red @happy "Just covering all my bases!"

        pause 0.5

        if (GetRelationship("Sabrina") == "...?"):
            sabrina @talking2mouth "...Alright. Friends. We are [bluecolor]friends again{/color}, then."
        else:
            sabrina @talking2mouth "...Alright. Friends. We are [bluecolor]friends{/color}, then."

        sabrina @sadbrow talking2mouth "For all the {i}misery{/i} it will bring us."

        pause 1.0

        if (GetRelationship("Sabrina") != "...?"):
            red @talkingmouth "I don't know what it'll bring me. Admittedly, the Student Council business wasn't the best first showing. But I'm willing to try again."

        red @talkingmouth "Sabrina, if there's one thing that incredibly distressing story you just told me convinced me of, in addition to that Student Council stuff, it's this."
        red @sadbrow talkingmouth "The worst thing that could happen to you has already happened. It can only go uphill from here."

        if (GetRelationship("Sabrina") == "...?"):
            $ persondex["Sabrina"]["Relationship"] = "Friend Again"
            $ persondex["Sabrina"]["RelationshipRank"] = 1

            $ PlaySound("sav.ogg")

            narrator "Your heart shifts as you feel your relationship with Sabrina evolve from '{color=#0048ff}...?{/color}' to '{color=#0048ff}Friend Again{/color}'!"

        else:
            sabrina @happymouth "...Very well. Is it alright, then, if I contact you in the future? Through your mind? If you think of me, I will know."

            redmind @happy "Kinda scary to hear that, but sure!"

            $ BecomeContacted("Sabrina")

            sabrina happy "Thank you. My {color=#0048ff}friend{/color}."

            $ persondex["Sabrina"]["Relationship"] = "Friend"
            $ persondex["Sabrina"]["RelationshipRank"] = 1

            $ PlaySound("sav.ogg")

            narrator "Your heart shifts as you feel your relationship with Sabrina evolve from '{color=#0048ff}Classmate{/color}' to '{color=#0048ff}Friend{/color}'!"
    
    else:
        if (not IsBefore(1, 5, 2004)):
            $ persondex["Sabrina"]["Events"].append("Level2SceneVer2")

        scene library
        show sabrina
        with Dissolve(2.0)

        queue music "audio/music/lavender_start.ogg" noloop
        queue music "audio/music/lavender_loop.ogg"
            
        red @talking2mouth "Sabrina. We need to talk."

        pause 2.0

        redmind @thinking "...Did she hear me?"

        sabrina @talking2mouth "Yes. I am waiting for you to tell me what you want to talk about."

        red @confusedeyebrows talking2mouth "Wait, don't you know?"

        sabrina @sad "Yes. But I am trying to pretend to be {w=0.5}ignorant."

        sabrina @talking2mouth "It comforts most people."

        redmind @thinking "Geez."

        sabrina "[ellipses]"

        red @closedbrow talking2mouth "Look. You said you didn't want me trying to help you. And you also said that I didn't need to worry about you telling people about Frienergy."

        sabrina @talking2mouth "That is correct, yes."

        red @talkingmouth "Well, why?"

        sabrina @talking2mouth "To which part?"

        red @talkingmouth "Both. But I figure the first one is a more sensitive topic, so I guess you can answer the second one first."

        sabrina @closedbrow talking2mouth "You presume to have access to my time."

        red @confusedeyebrows talkingmouth "Are you busy?"

        sabrina @sad "...No."

        red @happy "Then, yeah, I presume the hell out of my access to your time. Or whatever you said."

        sabrina @happymouth "...Hm. Amusing."

        sabrina @closedbrow talkingmouth "My lack of desire to expose your secret is very simple."
        sabrina @talking2mouth "I do not have any reason to."

        sabrina @sad "Doing so would be a malicious act, and you have done nothing wrong to me."

        red @sad "Er... even that thought I had when we first met? The, uh, 'inappropriate' one?"

        sabrina @talking2mouth "I have been hearing thoughts far worse than that since I was far too young to handle them."
        sabrina @sad "It is a reprieve, in some ways, to hear that sort of thought from someone who is not utterly detestable to the eye."

        red @confusedeyebrows talkingmouth "'Not utterly detestable to the eye?' Gotta put that one in my book of compliments."

        sabrina @sad "Besides, even if I did intend to act with malice towards you... I believe exposing your power is a bridge too far."

        red @confusedeyebrows talking2mouth "What do you mean?"

        sabrina @talking2mouth "I am aware of the effect I have on people."

        pause 2.0

        sabrina @neutralpowered poweredbrow "...No, {i}not{/i} that effect. The effect of fear."
        sabrina @closedbrow talking2mouth "They feel discomfort around me. And I cannot blame them. Secrets, fantasies, shadows... the very core of people's identities... are laid bare to me the moment they become aware of my power."

        red @closedbrow talking2mouth "Yeah, I guess most people can't help thinking of something the moment they realize they shouldn't think of it."

        sabrina @sad "I have resigned myself to this fate of isolation. To the point I now volunteer the truth of my power."
        sabrina @talking2mouth "I used to attempt to hide it. In vain."
        sabrina "[ellipses]"
        sabrina @closedbrow talking2mouth "No more. I will live as myself amongst others, or live as myself, by myself. I will discard my cares of another's thoughts."
        sabrina @sad "Destiny burdens me too much to ask me to wear a mask, too."

        red @closedbrow talking2mouth "So... you really have given up."

        sabrina @talking2mouth "Entirely."

        pause 2.0

        red @happy "Man, that's a load of shit!"

        sabrina neutralpowered poweredbrow "...I beg your pardon?"

        red @talkingmouth "You haven't given up. Not yet. And there are three ways I can tell, even without reading your mind."

        sabrina "Do share your theory with me. But speak carefully. Telepathy is only one of my many psychic skills, and amongst my least invasive."

        red @talking2mouth "The first is that you're telling me all this. When you told me about your powers, and now, you've been apologetic. You know what an apology is, right?"
        red @happy "It's asking someone to overlook something you've done wrong. Now, you haven't done anything wrong, but the fact you want me to overlook something means you care about what I think. Literally."

        pause 2.0

        red @talking2mouth "The second thing is that you're here in Kobukan. It's not easy to get in. And--correct me if I'm wrong--I don't think anyone forced you to come here."

        if (GetRelationship("Dawn") != "Classmate"):
            red @closedbrow talking2mouth "I know one girl was forced to come here, but you're basically as different from her as I could imagine."

        red @closedbrow talking2mouth "Am I right?"

        sabrina -neutralpowered -poweredbrow @talking2mouth "You are correct. I was not forced to come here."

        red @happy "Cool. Kobukan's a school with tons of busy people with strong ambitions and goals, and very active minds, all crammed into a single campus. You probably dorm with four other girls, right?"
        red @sad "...I don't know how your power works, exactly, but I have to imagine being around a lot of people doesn't make things any quieter."

        sabrina @talking2mouth "And why do you think that?"

        red @talkingmouth "You're here, in the back corner of the library, alone."

        sabrina "[ellipses]"

        redmind @thinking "Am I right?"

        redmind @happy "{color=#600080}Yes.{/color}"

        red @happy "Nice."

        sabrina @talking2mouth "What's the third thing, then?"

        red @talkingmouth "Well, it's, uh...{w=0.5}{nw}" 
        extend @happy "You're beautiful."

        show sabrina blush with Dissolve(2.0)

        sabrina @talking2mouth "I don't see how that's relevant to anything."

        red @happy "Well, I might be totally off-base, here, but... your hair is really shiny and straight, so you gotta be using some kind of special shampoo. And you comb it every day, too, right? Hair that long, probably multiple times a day."
        red @talkingmouth "Your posture is, like, incredible. I've never seen someone with a straighter back."
        red @happy "And, well, your outfit is... very flattering. And you know it. You know what people think when they see you."

        sabrina @closedbrow talking2mouth "It is typical of a man to believe I adorn myself for his pleasure."

        red @talking2mouth "I don't think it's for me. I think you heard people mentally needle and point out tiny flaws in your appearance over and over, until you eliminated them."

        sabrina "[ellipses]"

        sabrina @talking2mouth "Even if that's true, how would that indicate that I haven't fully discarded the thoughts and opinions of others?"

        red @happy "Well, you heard people's thoughts, and changed yourself. Unless I'm meant to believe that you were born this way."

        sabrina -blush @talking2mouth "...You are...{w=0.5}{nw}"
        extend @sad " Not entirely incorrect."

        pause 2.0

        redmind @thinking "Well? Tell me more."

        pause 2.0

        sabrina @talking2mouth "Espers are not uncommon. Not as uncommon as many would think, in any case."
        sabrina @closedbrow talkingmouth "There are communities of Espers that live together in every region. Sometimes, they even manage to develop a culture and society that can exist alongside Euthymics'."
        sabrina @talking2mouth "A 'Euthymic' is what Espers call non-Espers."
        sabrina @sad "But... I could not live in one of those communities."

        red @confusedeyebrows talking2mouth "...?"

        sabrina @talking2mouth "Espers live together in peace, taking advantage of their abilities without suffering the downsides as I do."
        sabrina @closedbrow talking2mouth "For the vast majority of Espers, their powers are voluntary. Mine are not. I do not believe they ever will be."
        sabrina @closedbrow talkingmouth "When I am forced to read the mind of an Esper, reading the mind of another, who was possibly reading another... it was an excruciating feedback loop. Debilitating headaches followed. I cannot be around them."

        red @surprised "Oh, wow. Like when Roxanne blasted out our ears during orientation?"

        sabrina @closedbrow talkingmouth "Yes. Constantly."
        sabrina @talking2mouth "...So I sought a place in the Euthymic world. And still seek it now, as you have proven. As much as I may try to deny it, or tell myself that I've given up caring."

        red @talking2mouth "...Maybe you should try {i}not{/i} immediately telling people that you read minds? It might be easier to fit in."

        sabrina @sad "I have tried that. My precious friend felt betrayed. She hated me, then. And I could feel her thoughts turn from love to poison."
        sabrina @talking2mouth "No. If I am to imbibe poison, then I will prepare the chalice for myself, at a time of my choosing."

        red @sad "Oh... I'm really sorry to hear about your friend..."
        red @closedbrow talking2mouth "But you can't give up just because one person reacted negatively!"

        sabrina "[ellipses]"
        sabrina @talking2mouth "Would you risk letting a single one of your friends know of your... 'Frienergy?'"
        sabrina @sad "I know it is not mind control. It's a conduit for empathy, at its strongest."
        sabrina @talking2mouth "But my power is also not mind control. Nor is it 'soul-stealing,' 'witchcraft,' or 'evil.'"
        sabrina @sad "And yet... it has been described as such by many."

        red @closedbrow talking2mouth "...Hm. Was it described as that aloud? Or did you get that from peoples' minds?"

        sabrina @closedbrow talkingmouth "None have ever chosen to state those sorts of true feelings to my face. I don't see what difference it makes, though."

        red @happy "I think it makes a huge difference, actually."

        sabrina ".{w=0.5}.{w=0.5}.{w=0.5}{nw}"
        extend @talkingmouth "Oh?"

        red @closedbrow talking2mouth "Yeah. I mean, people have all kinds of intrusive thoughts, you know?" 
        red @talkingmouth "You know, more than anyone, that people can't help but think of the worst things at the worst possible times when they're around you."
        red @happy "But if they choose not to say it, then they're making a choice to be better than their instincts. Sure, maybe they're just trying not to make you angry or whatever..."
        red @talkingmouth "But I bet if that was the case, you would know what their intentions were, too, right?"

        sabrina @talking2mouth "Are you trying to convince me that there is something governing peoples' actions other than their thoughts?"
        sabrina @sad "Pity. I thought this conversation was going somewhere."

        red @talking2mouth "...People aren't machines, Sabrina. You can't just read the code from their heads and know exactly what they're going to do."
        red @happy "Sometimes, even if they're thinking one thing, they're going to do the exact opposite."

        sabrina @talking2mouth "I challenge you to name one situation in which that's the case."

        red @happy "Well, you're pretty difficult to talk to, right?"

        sabrina @sad "As you have constantly been thinking, yes."

        pause 2.0

        red @talkingmouth "I'm still here, aren't I?"

        sabrina @closedbrow talkingmouth "...Now, that {i}is{/i} strange. Why?"

        red @talkingmouth "Because I want to help you. And I have no idea how, and I don't even know where to begin, and I might not ever be able to help you with your powers."
        red @happy "But I can at least be your friend. We can be weird power buddies!"

        sabrina @sad "Our powers are in no way comparable."

        red @talkingmouth "Uh-huh."

        sabrina "{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}{nw}"
        extend @talkingmouth "Fine."

        red @happy "Sweet! So--"

        sabrina @closedbrow talkingmouth "No, I will not help you cheat on tests. No, I will not help you win at cards. No, I will not..."
        sabrina "[ellipses]"
        sabrina @talking2mouth "You want me to send you the lyrics to songs while you're doing karaoke, so you can pretend to have memorized them?"

        red @happy "Yeah!"

        sabrina @sad "A person with my powers could be ruling nations, or upending dynasties. And you want me to use my powers to make you seem better at karaoke."

        red @confusedeyebrows talking2mouth "Be honest with me--what have you actually used your powers for? On purpose? Because it sounds to me like you've mostly been trying to avoid them."

        pause 2.0

        sabrina @closedbrow talkingmouth "...I used them to win at blackjack once. I needed some money, shortly after I moved to Inspira."
        sabrina @sad "I wasn't allowed to keep my winnings, though. Not because I read the dealer's mind, but because I was under twenty-one, and shouldn't have been in the casino in the first place."

        red @surprised "Geez. Did you get arrested?"

        sabrina @closedbrow talkingmouth "...No. The dealer was also an Esper, actually. He said he wouldn't turn me in as long as I became his protégé."
        sabrina @talking2mouth "Eventually, he got me a job at the same casino. Which is where this particular outfit comes from."
        sabrina @happymouth "He is bombastic, and showy, and ridiculous... not to mention a weak Esper... but he does give me hope that life amongst the Euthymics is possible."

        red @happy "Well, see? The one time you used your powers, instead of trying to hide from their effects, everything turned out fine."

        sabrina @talking2mouth "We'll see. The future has yet to arrive."
        sabrina "{w=0.5}.{w=0.5}.{w=0.5}."
        sabrina @talking2mouth "I would ask two questions, which I have not been able to figure out, even as I search your mind."

        red @talkingmouth "Oh, sure. What is it?"

        sabrina @closedbrow talkingmouth "When you were stating those three facts, which proved to you that I still hold onto some vain hope of 'normalcy...' I could never see what your next argument would be until you were already saying it. How?"

        red @happy "Oh, that? Yeah, I was just improvising like crazy there. I pretty much only came up with each argument after I'd already started saying it."

        sabrina @sad "So when you said you had three things...?"

        red @closedbrow talking2mouth "It might've been more accurate to say that I was {i}going to figure out{/i} three things."

        sabrina @happymouth "{w=0.5}.{w=0.5}.{w=0.5}."
        extend @closedbrow happymouth "Remarkable. Your mind works fast, considering how empty it is."

        red @angrybrow frown2mouth "Hey. It might be mostly empty, but I've got enough wrinkles in the ol' thinkmeat to get offended."
        red @happy "...But not for long. So what was your second question?"

        sabrina @sad "Why is that song about the baby Sharpedo playing in your head? Just... over and over...?"

        red @closedbrow talking2mouth "Oh, yeah, I, uh... I heard it, like, a week or two ago."

        sabrina "[ellipses]"

        red @talking2mouth "So it'll probably be another month or so before it leaves."

        sabrina @sad "If we are to spend more time together, could you not... perhaps... get some classical piano stuck in your head? Something that fades into the background?"

        red @happy "I mean, I could try."
        redmind @surprised "Wait! We're going to be spending more time together?"

        show sabrina blush with dis

        redmind "{color=#600080}You said that you would be my friend. I am given to understand friends... 'hang out.'{/color}"
        redmind @happy "We sure do. Give me some time to figure out where we should go, alright?"

        sabrina @happymouth "...Very well. Is it alright, then, if I contact you in the future? Through your mind? If you think of me, I will know."

        redmind @happy "Kinda scary to hear that, but sure!"

        $ BecomeContacted("Sabrina")

        sabrina happy "Thank you. My {color=#0048ff}friend{/color}."

        $ persondex["Sabrina"]["Relationship"] = "Friend"
        $ persondex["Sabrina"]["RelationshipRank"] = 1

        $ renpy.music.set_volume(0.1, delay=0.0, channel="music")
        $ PlaySound("sav.ogg")
        $ renpy.music.set_volume(1.0, delay=1.0, channel="music")

        narrator "Your heart shifts as you feel your relationship with Sabrina evolve from '{color=#0048ff}Classmate{/color}' to '{color=#0048ff}Friend{/color}'!"

        return