label Bea1:
    if (not IsBefore(1, 5, 2004)):
        $ persondex["Bea"]["Events"].append("Level2SceneVer2")

    scene gym 
    with Dissolve(2.0)
    queue music "Audio/Music/StowOnSide_start.ogg" noloop
    queue music "Audio/Music/StowOnSide_loop.ogg"

    pause 1.0

    show balloonbot at rightside:
        yalign 0.5
        block:
            ease 1.0 yalign 0.4
            ease 1.0 yalign 0.5
            ease 1.0 yalign 0.6
            ease 1.0 yalign 0.5
            repeat

    show bea at leftside
    with dis

    narrator "Walking into the gym, you see that, unusually for this time of day, there seems to be only one other person here."

    pause 1.0

    bea @closedbrow talkingmouth "Hah..."

    show bea:
        easein 0.2 xpos 0.75

    show balloonbot:
        pause 0.15
        ease 0.2 xpos 1.5

    bea @angry "Hah!"

    pause 1.0

    show bea:
        ease 0.5 xpos 0.5

    bea "{w=0.5}.{w=0.5}.{w=0.5}."
    bea @talkingmouth "'Lo."

    red @happy "Hey, Bea. Doing some training?"

    bea @talkingmouth "Yes. Living in Kobukan has weakened me."
    bea @closedbrow talkingmouth "At my home in Stow-On-Side, I used to wake up every morning and climb the mountains north of us."

    red @talkingmouth "Cool. Cool. So, hey, you told me to find you so we could work on your, uh, face training?"

    if (IsBefore(1, 5, 2004)):
        bea @talkingmouth "Yes. Are you ready?"

    else:
        bea sad "{w=0.5}.{w=0.5}.{w=0.5}."

        red @sad "...It's... it's fine if you don't want to, anymore. I know things have changed, since you made that offer."

        pause 1.0

        bea -sad @closedbrow talkingmouth "...Yes, things have changed. The reveal of your power was... unexpected. For both of us."

        red @sadbrow talkingmouth "If it helps, I didn't know about it until about two weeks into the school year."

        bea @closedbrow talkingmouth "That is of no consequence. I was moved by the speech you gave."

        redmind @thinking "Moved? You could've fooled me."

        pause 1.0

        bea @talkingmouth "I understand the pain that those with power can inflict. I think it shows strength of character and will to restrain yourself--as I believe you have."

        red @sadbrow talkingmouth "Thanks."
        red @closedbrow talking2mouth "Although, the way this power works, I don't think I could have used it in a negative way."

        bea @sad "There are... those who are 'creative' in their application of their natural talents. I trust that you are not that sort."
        bea @talkingmouth "In any case, I am friends with Sabrina, and if I do not fear her, there is less than nothing to fear from you."

        redmind @thonk "...I mean, that's great, but I feel a tiny bit offended."

        pause 1.0

        bea @talkingmouth "Therefore, I would ask you to join me in my training, as originally requested."

    red @happy "Absolutely! So, how does this work, exactly?"

    bea @talkingmouth "It's quite simple. Attack me, and I will attempt to block or dodge. If I express any fear, uncertainty, or panic, then I fail."
    bea @closedbrow talkingmouth "Of course, I also fail if I cannot fend off your attack."

    red @confused "Uh... attack you? I don't know any martial arts."

    bea surprised "Oh."

    pause 1.0

    bea -surprisedbrow -frownmouth -surprised @talkingmouth "I assumed from your muscle definition that you knew a bit of Muay Thai."

    red @closedbrow talking2mouth "I think I had that at a bar once..."

    bea @talkingmouth "Well, in that case, just try to grab me."

    redmind @thinking "Man, this is a {i}weird{/i} conversation to have."

    red @talkingmouth "Just, like... 'grab?' Uh, where?"

    bea @closedbrow talkingmouth "The extremities of the limbs are the hardest to find purchase on. However, they're the easiest to {i}keep{/i} in your possession."
    bea @talkingmouth "If you were to grab onto my wrist, I would understandably jerk my arm inwards to try and slip out of your grasp." 
    bea @closedbrow talkingmouth "You should counter that, not by resisting, but by following my arm's movement." 
    bea @talkingmouth "After I am incapable of pulling my arm back any further, you can similarly jerk your arm backward at the same time, throwing me off balance, if my footing is not secure."
    bea @closedbrow talkingmouth "However, my footing {i}will{/i} be secure. You'll want to unsteady me with a firm kick to my inner right ankle. However, I'll be expecting that, so aim higher, as I'll--"


    red @surprised "Uh, Bea? I'm pretty sure none of this is relevant."
    if (IsBefore(23, 4, 2004)):
        red @surprised "I mean, just looking at you, I can tell you're tough, and trained."
    else:
        red @surprised "You did, like, two hundred push-ups during the Battle Team meeting. With a Clobbopus on your back."

    red @happy "There's no way I'm laying a hand on you."

    bea @talking2mouth "...Training may not be enough to overcome the additional ninety pounds of muscle you're bringing to our bout."

    red @happy "Fair enough."

    show gym:
        xalign 0.5 yalign 0.5
        ease 2.0 zoom 1.2

    show bea:
        ease 2.0 ypos 1.2 zoom 1.3

    bea @closedbrow talking2mouth "Now..."

    bea angry "Begin!"

    show bea:
        ease 0.3 ypos 2.0 zoom 3.0 alpha 0.0

    pause 0.35

    $ PlaySound("body roll.ogg")
    queue sound "audio/body crash.ogg"

    show blank2 with vpunch
    hide bea

    red @surprised "OOF!"
    red @talkingmouth "Woah--I thought I was going to attack you, and you were going to defend?"

    bea @talkingmouth "Yes." 
    bea @angry "And the best defense is an unweatherable offense!"

    red @happy "Well, I can't argue with that. Gimme a second to--"

    show blank2 with vpunch

    red @surprised "Oh, shit! We're still going?"

    bea @angry "Attack me!"

    narrator "You end up wrestling with Bea for more than ten minutes. Though she is clearly more skilled than you, you notice her stamina is starting to flag, and you suspect that you might be able to successfully grab her wrist."
    narrator "You push through your tiredness, and--"

    show bea surprisedbrow angrymouth behind blank2:
        ypos 1.2 zoom 1.3
    hide blank2

    red @happy "Gotcha!"

    bea "Ah!"

    pause 1.0

    red "{w=0.5}.{w=0.5}.{w=0.5}."

    pause 1.0

    red @confused "Uh... aren't you going to, like, pull your arm back? What happened to that big plan?"

    bea -angrymouth sadbrow @sadmouth "...Please let go."

    show bea:
        ease 0.5 ypos 1.0 zoom 1.0

    red @surprised "Huh? Oh, yeah, of course!"

    pause 1.0

    red @sad "I'm sorry. Did I... did I hurt you?"

    bea @sadmouth "No."

    pause 1.0

    red @talkingmouth "Um... you kinda froze, there. Is that something you'd like to tell me about?"

    bea @closedbrow sadmouth "With... the understanding that you tell no-one else?"

    red @talking2mouth "I promise."

    pause 1.0

    bea @talkingmouth "I was a trainer once before. In Galar, trainer schools aren't typically a thing. Most people just start their journey after getting an endorsement."

    if (GetRelationshipRank("Nessa") > 0):
        red @closedbrow talking2mouth "Yeah, Nessa explained that to me."

    bea @closedbrow talking2mouth "I wasn't alone on that journey. With me, there was... another."

    pause 1.0

    bea @talkingmouth "A boy I loved like a brother. He didn't actually want to go on an adventure. And he was too young, too. But I dragged him along, and..." 
    bea @closedbrow talking2mouth "We had just started our journey when we were attacked."

    pause 1.0

    bea @sadmouth "My brother was timid and shy. I promised to protect him. It was the only way I could have gotten him to leave his library. I {i}promised.{/i}"
    bea @angry "But... I froze. I panicked. I {i}failed.{/i}"

    if (not IsBefore(1, 5, 2004)):
        bea @sad "When Cheren was saying those awful things to you, up on that stage..."
        bea @talkingmouth "I saw a fear in your eyes that I recognized. Blind panic. Betrayal. Hurt and noncomprehension the world could be so cruel."
        bea @closedbrow talking2mouth "I felt the same from Sabrina. Of course, using her powers, she {i}could{/i} have defended herself. But she, like others, cannot comprehend of the {i}need{/i} to defend oneself."
        bea @sad "I can. I should have done so. But, once again... I froze, and panicked, and failed."
        
        pause 1.0

        bea @sad "I thought... after years had passed... that my strength would be enough. That I could save another from the fate that befell my brother. But absolutely nothing has changed."

    pause 1.0

    bea @sad "And now my brother barely leaves his room, and can't bear to show his face to anyone. He lives with a poisonous, caustic, shame."
    bea @closedbrow talking2mouth "A shame that should be mine."

    red @angrybrow talking2mouth "Hey. {i}No.{/i} You have nothing to be ashamed of. Neither does your brother. You were {i}kids{/i}."
    red @closedbrow talking2mouth "And even if you were fully grown, you still have nothing to be ashamed of."

    pause 1.0

    red @sad "What happened next?"

    bea @talkingmouth "We went back home. My brother retreated into his library, hiding himself ever deeper in the shadows."
    bea @sadmouth "Then, after returning home from school one day, he brought home a papier-mâché mask he made in art class... and I've never seen his face since."

    red @sad "Is that why you wear a mask, too, then?"

    bea -sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."
    bea @talkingmouth "Yes. I must train myself so my weakness does not cause more tragedies like this to happen again. For that, eliminating uncontrolled movement in my body is practical."
    bea @talkingmouth "But removing all traces of emotion from my face is not strictly necessary for that. {i}That{/i} is... my penance."

    pause 1.0

    red @talking2mouth "Okay."

    bea @surprised "Oh?"

    red @talkingmouth "Okay. I understand."

    bea @talkingmouth "I'm happy, but surprised. {i}Why{/i} do you understand? No-one but my brother ever has. Ever {i}could.{/i}"

    red @closedbrow talking2mouth "When bad stuff happens to us, we all have different coping methods. It's not my place to judge yours. If it makes you feel like you're 'paying off' some sort of debt, then carry on. Forever, if you need to."

    bea @surprised "That's the exact opposite of what my therapist said."

    red @happy "Well, I don't have a degree."
    red @talkingmouth "The way I see it, as long as you're not hurting anyone, you can do whatever you want."
    red @happy "If you want to keep your emotions hidden, go ahead."

    bea @happymouth "Hm. No-one has ever said that's fine before... I'm interested, now."
    bea @talkingmouth "Who {i}are{/i} you, [first_name] [last_name]?"

    red @happy "Just a guy who's going to be a Pokémon Champion."

    bea @talking2mouth "Hm."

    red @talkingmouth "What about you, Bea?"

    if (IsBefore(23, 4, 2004)):
        bea @talkingmouth "I intend to join the Battle Team. I'll leverage my position as a member of the Battle Team to return to Galar and get a second endorsement, beginning my journey again."

    else:
        bea @talkingmouth "I intend to leverage my position as a member of the Battle Team to return to Galar and get a second endorsement, beginning my journey again."

    red @surprised "Oh! You're going to try the Galarian league again?"

    bea @closedbrow talkingmouth "Yes. The first part of my penance is to wear my brother's mask. The second part is to finish my journey alone."

    red @closedbrow talking2mouth "And after that, you'll... be satisfied?"

    bea @talkingmouth "After that, I'll feel I have done enough to deserve the chance to beg for my brother's forgiveness."

    red @confusedeyebrows talking2mouth "Aren't you being a bit hard on yourself?"

    pause 1.0

    bea @talkingmouth "There's an old Galarian story my brother told me about a Rolycoly. This Rolycoly was very small, and weak, and all the other Rolycoly used to mock and shun her."
    bea @closedbrow talkingmouth "...Actually, in the original story, the Rolycoly was male, but I like to imagine it was female."
    bea @talkingmouth "Anyway. Because this Rolycoly was never able to participate in the coal-running along with the others, it was left behind when they evolved into Carkol."
    bea @talkingmouth "So it started training itself. It would ram itself into walls, over and over, to toughen its shell."
    bea @closedbrow talkingmouth "It did this for ages. Until, one day, it rammed itself into the wall of the abandoned mine so hard that it caused a cave-in."
    bea @surprisedbrow talkingmouth "The other Carkol and Coalossal were wracked with grief as they saw what their bullying and shunning had done."
    bea @talkingmouth "As they wept above the pile of rubble that was their home, and now marked their sister's grave, one of them noticed a shining light coming from the debris."
    bea @talkingmouth "The Coal Pokémon quickly began excavating the rubble, and beneath, they saw something remarkable--the lone Rolycoly's body, through its intense training, and the pressure of the collapsed mine, had become shining diamond."

    pause 1.0

    red @confused "So... the Rolycoly survived, right?"

    bea @surprised "Hm?"
    bea @talkingmouth "Oh, no, she was quite dead."

    pause 1.0

    red @confused "I guess I don't get the moral of the story."

    bea @closedbrow talking2mouth "I think the moral is that Galar is a dim, rainy, place where everybody has very grim outlooks on life."

    pause 1.0

    red @confused "Why did you tell me this story? I asked you if you were being a bit hard on yourself."

    bea @surprised "Oh."
    bea @closedbrow talkingmouth "Right. I'd forgotten the point I was trying to make."
    bea @talkingmouth "The point is, it's always easiest to see one's best qualities after they've been broken."
    bea @talking2mouth "So that's my goal. I will become an unbreakable, unflinching fist, then shatter myself against the stones."
    bea @talkingmouth "I will eliminate my weakness, and temper my strength."

    red @confused "So you'll make yourself strong... and then weak?"

    bea @closedbrow talkingmouth "I will show my brother that even the strong can be broken. His shame comes because he believes that his weakness caused the attack. But I will teach him that even the strong can be weakened." 
    bea @sadbrow talkingmouth "And then, perhaps, after my penance has been paid, and he sees that his misfortunes are not his fault, things can go back... back to how they were before."

    red @confused "See, I was with you for the 'wearing a metaphorical mask' part of your plan, but I think I'm a bit lost on some of the details now."

    bea @talkingmouth "Elaborate?"

    red @closedbrow talking2mouth "Like, when you say you're going to make yourself stronger, you mean, you will become {i}physically{/i} stronger, right? As in, put on more muscle, learn new martial arts?"

    bea @talkingmouth "Yes."

    red @confused "Okay, so I get how you'll do that. Exercise and training. Simple enough. But what about the 'breaking?' How are you going to do that--to prove to your brother that even the strong can be broken?"

    bea "By begging for forgiveness."

    red @closedbrow talking2mouth "Right. This is... this is kinda a complicated plan."

    bea @surprised "What?"

    bea @talkingmouth "No, it has two steps. Get strong, then ask for forgiveness. It's very simple."

    red @closedbrow talking2mouth "Sure, but what about hiding your emotions? How long will that last? And how strong is strong enough? I mean, you're already pretty strong." 

    show bea surprisedbrow frownmouth with dis

    red @confused "And what's the point of finishing your Pokémon journey in Galar if you're focused on becoming {i}physically{/i} stronger?"
    red @closedbrow talking2mouth "What happens if you actually do, like, {i}really{/i} well in Kobukan? Are you just going to quit wherever you ended up and become a beginner trainer again in Galar?"
    red @talkingmouth "And if you {i}were{/i} going to do that, then what about the Pokémon you trained in Kobukan? Are you just going to leave them in a PC and pick up a Farfetch'd somewhere in the wilds?"

    pause 1.0

    bea sad "Um."

    red @sadbrow talking2mouth "You've been thinking about this plan for a long time, haven't you?"

    bea "Yes..."

    red @sadbrow talking2mouth "I can tell. You've added so much to this plan, you lost your original goal."

    pause 1.0

    red @closedbrow talking2mouth "The number one thing you want is to get your brother to open up again?"

    bea -sad @talkingmouth "I want him to feel safe again."

    red @talkingmouth "Okay. Let's focus on that. And let's come up with a plan for how we're going to do that."

    bea @talking2mouth "We?"

    red @talkingmouth "Sure! I want to help you. And even though you tossed me around this gym for ten minutes, it seems like you could do with a little help on the planning front."

    bea "{w=0.5}.{w=0.5}.{w=0.5}."
    bea @closedbrow talkingmouth "That's fair. What do you have in mind?"

    red @talking2mouth "I don't know yet. But I'll seek you out when I can, alright?"

    bea @happymouth "...Yes."

    $ BecomeContacted("Bea")

    bea @talkingmouth "Please contact me as soon as you feel we could begin our discussion of this plan."

    red @happy "Sure thing. Oh, by the way, Bea?"

    bea @surprised "Hm?"

    red @confused "You've been kinda... 'loose' with your face for this entire conversation."

    bea "{w=0.5}.{w=0.5}.{w=0.5}."

    if (IsBefore(1, 5, 2004)):
        bea @closedbrow talkingmouth "I find it difficult to hide my feelings around you, for some reason. I just need more practice."
    else:
        bea @closedbrow talkingmouth "I find it difficult to hide my feelings around you, for some reason. I imagine this is a side-effect of your power."

        pause 1.0

        redmind @thinking "Yeah, maybe."

    red @happy "Yeah, alright. Seeya, Bea."

    hide bea with dis

    pause 2.0

    redmind @thinking "Eeesh. That was {i}intense.{/i}"

    show smoke:
        animation
        alpha 0.0 yalign 3.0 xalign 0.5
        parallel:
            ease 3.0 yalign 0.5
        parallel:
            ease 0.5 alpha 1.0
            pause 0.5
            ease 3.0 alpha 0.0 

    pause 3.0

    show blank
    show janine behind blank

    pause 0.1

    $ renpy.transition(None)
    hide smoke
    hide blank

    if (GetRelationship("Janine") == "Good Boy"):
        red @surprised "Woah! Miss Janine!"
    else:
        red @surprised "Woah! Janine!"

    janine @talking2mouth "Yeah, hi. What were you talking about?"

    red @confused "Um... she was just telling me about her past, and her home in Galar, really..."

    pause 1.0

    red @confused "Why?"

    if (IsBefore(23, 4, 2004)):
        janine @talking2mouth "I want that girl in the Battle Team."

        red @happy "Oh, you're in luck, then! She said she wants to join."

        janine @closedbrow talkingmouth "Hm. Good."

        janine @happy "If you have any influence over her... keep her that way. She'll be useful. Almost as useful as you, I bet."

        $ ValueChange("Janine", 3, 0.5)

        red @confused "Uh... thanks?"

        janine closedbrow talking2mouth "The girl's strong, but doesn't think long-term. And when she does, she just confuses herself. She needs, like... a notebook, or a {color=#0048ff}planner{/color} or something..."
    else:
        janine @talking2mouth "She's part of my Battle Team. I just want to know how my battlers are doing."
        janine @happy "And keep an eye out for possible mutiny, of course."

        red @talkingmouth "Well, she's doing fine. She's a bit confused, but... she's alright. Figuring it out."

        janine @sad "Right... from what she told me, she..."

        pause 1.0

        janine @talking2mouth "Nevermind. If she wants to tell you, she will. Not everyone's as much of an open book as I am."
        janine @happy "Hey. She's your teammate, she's been through a lot, and I care about her."
        janine @angrybrow talking2mouth "Be nice to her. Or else. And not in the fun way."

        red @talking2mouth "Of course. I wouldn't dream of anything else."

        $ ValueChange("Janine", 3, 0.5)

        janine @happy "Good!"

        janine closedbrow talking2mouth "The girl's strong, but doesn't think long-term. And when she does, she just confuses herself. She needs, like... a notebook, or a {color=#0048ff}planner{/color} or something..."

    $ RelationshipRankUp("Bea", "Planner", 1)

    return

label Bea2:
    show classroom
    show fighttype
    show bea
    with Dissolve(2.0)
    queue music "Audio/Music/StowOnSide_start.ogg" noloop
    queue music "Audio/Music/StowOnSide_loop.ogg"

    red @talkingmouth "...so that brings us to next week. Based on your schedule, if you get up at 7:15 every morning, you should have enough time to get a workout in before your first class. Shower included, of course."
    red @closedbrow talking2mouth "You're doing well on your Fighting elective, but it looks like your Rock elective is slacking a little bit."

    pause 0.5

    if (HasEvent("Instructor Olivia", 1)):
        red @closedbrow sweat talking2mouth "I know they're not the most fun things to attend, but Instructor Olivia's office hours are probably your best bet for patching up those weak spots."
        red @happy "She may be depressing, but she {i}really{/i} knows Rock-types."

    else:
        red @talking2mouth "I'd recommend attending the rock instructor's office hours to patch up those weak spots."

    bea @closedbrow talking2mouth "Hm."

    if (not HasEvent("Bea", "Level2SceneVer2")):
        narrator "You were worried at first that Bea might react negatively to the reveal of your Frienergy."
        narrator "You shouldn't have worried. She had almost immediately dismissed it, expressing her sympathy for what you had gone through."

    narrator "After your first talk with Bea, you took Janine's words to heart, and vowed that you would become Bea's [bluecolor]planner.{/color}" 
    narrator "As a result, whenever you've had a free moment, you've been going over Bea's schedule, doing your best to help her make plans."

    pause 0.5

    narrator "This has proven to be surprisingly difficult. It is not that Bea lacks the discipline to follow the plans--not even close."
    narrator "Nor is it that she is in any way unappreciative." 
    narrator "Rather, her gestures of gratitude have gotten more and more embarrassingly grandiose."

    bea @talking2mouth "For your aid, I swear a debt that I shall carry with my life."

    red @lightblush sad2eyes talking2mouth "Bea, this is the third life-debt you've sworn this week."

    if (getRWDay(0) in ["Monday", "Tuesday", "Wednesday"]):
        $ dayname = getRWDay(0)
        red @closedbrow talking2mouth "And it's only [dayname]."

    bea @closedbrow talkingmouth "I would not have you think I am not incredibly grateful for your companionship and your kindness."

    redmind @confusedeyebrows frownmouth "She says that, but she's still as stony-faced as ever..."

    pause 1.0

    bea @talkingmouth "I will follow this schedule to the letter. Goodbye."

    show bea:
        xpos 0.5
        ease 0.5 xpos -0.2

    pause 1.0

    red @playfuleyes confusedeyebrows talking2mouth "Hey, Bea?"

    show bea surprisedbrow frownmouth:
        xpos -0.2
        ease 0.5 xpos 0.5

    bea "Hm?"

    red @happy "You might find it a bit hard to follow this plan, considering, uh, that I'm still holding it."

    pause 1.0

    bea @closedbrow talkingmouth "Oh. Apologies. I was... distracted."

    red @confused "That's not like you. Want to talk about it?"

    bea @sadbrow frownmouth "[ellipses]"
    bea surprised @talkingmouth "Yes. But first, let us find a more private place to talk."

    red @talkingmouth "This classroom is completely empty."

    bea @surprisedbrow talkingmouth "Oh."
    bea -surprisedbrow -frownmouth -surprised @closedbrow sweat talkingmouth "So it is. This will do, then."

    show bea:
        ease 0.5 ypos 0.9 zoom 0.9
        ease 0.5 xpos 0.75
        pause 1.0
        ease 0.2 xzoom -1
        ease 1.0 xpos 0.25
        pause 1.0
        ease 0.2 xzoom 1
        ease 0.5 xpos 0.5
        ease 0.5 ypos 1.0 zoom 1.0

    narrator "Bea fidgets for a while, standing up and sitting down on various desks, as though she couldn't find a place to get comfortable."

    pause 1.0

    narrator "Privately, you think it's somewhat hypnotic."

    pause 0.5

    narrator "Eventually, though, she comes to a stop, exactly where she started dithering from."

    show bea:
        ypos 1.0 zoom 1.0 xpos 0.5
    
    bea @talkingmouth "It's Nate."

    red @surprised "Hm?!"

    redmind @thinking "What about Nate? Does this have anything to do with that conversation we had in the warehouse...?"

    show warehouse at sepia
    show flashback
    with dis

    $ renpy.pause(1.0, hard=True)

    show nate frownmouth at sepia behind flashback with dis

    if (HasEvent("Nate", "LevelOneAfterBianca")):
        nate @talkingmouth "Bianca, Bea, and Hilbert have given me leads toward a certain someone that I've been hunting for a while."
    else:
        nate @talkingmouth "Bea and Hilbert have given me leads toward a certain someone that I've been hunting for a while."
    
    show blank with splitfade

    hide nate
    hide warehouse
    hide flashback
    hide blank with dis

    redmind @thinking "He... {i}did{/i} mention that he thought Bea might have a clue towards someone he's been trying to track..."

    red @talking2mouth "Well, what is it?"

    bea @closedbrow talkingmouth "I think I have become fond of him. And I would like to know how to demonstrate that."

    red @unamusedbrow unamusedmouth "...That's great, but I'm not going to write a love letter for you."

    bea @talking2mouth "That was a joke."

    pause 1.0

    red @confused "Well, they say it's all in the delivery."

    bea @closedbrow talkingmouth "This is the part where I jovially punch you in the shoulder. Given that I would rather not shatter your arm, I will simply state my intent to do so, in lieu of execution."

    red @talkingmouth sweat "I appreciate that. After that one time I managed to grab you during training, I don't think I've managed to land a hand on you--unless you let me, to get a better grip on me."

    bea @talking2mouth "I have you to thank for that. You have been an invaluable practice partner."

    red @talking2mouth sweat closedbrow "I feel like I've been about as valuable as a bag of potatoes would be, when it comes to training, but..."

    narrator "You attempt to steer the conversation back in its original direction. You know all too well that Bea gets distracted very easily from topics of conversation, and once the thread is lost, it takes a {i}long{/i} time to get it back."

    red @talking2mouth "But, seriously, what is it about Nate?"

    bea @sad "...This is a difficult thing for me to say."
    bea @closedbrow talkingmouth "It is difficult, even, for me to think of."

    pause 0.5

    bea @talkingmouth "Nate has informed me that... my attacker was imprisoned."
    
    red @surprised "Huh? That's-- that's great news! Right?"

    bea @talkingmouth "Perhaps. Certainly, seeing the perpetrator of my family's grief punished could bring closure, but..."
    bea @closedbrow talkingmouth "I am undecided."

    red @talkingmouth "Well, tell me. What happened? What did Nate say?"

    bea @talkingmouth "After I told you the story of my past, I felt... more comfortable divulging these painful memories."
    bea @talkingmouth "When Hilbert was having a bad day, in an attempt to empathize with him, I shared my own story."
    bea @sad "I think... he did not feel any better."
    bea @closedbrow talkingmouth "Nevertheless, something about my recounting piqued Nate's interest. He said he had a friend who had access to police records."
    bea @talkingmouth "After cross-referencing the details of my story with his friend's records, he thinks that the person that attacked me was arrested. Still in Galar, even."

    red @angrybrow talking2mouth "He never left?"

    bea @talkingmouth "That... man, that beast, thought he had gotten away with it. Or so it seems."
    bea @sad "In a way... he had."
    bea angrybrow @angrymouth "Years passed without justice or retribution. While we hurt, his feet trod Galarian soil, uninhibited, unregretful."

    pause 0.5

    bea sadbrow @talkingmouth "He was eventually arrested in Hulbury. Not for what he did to me. Or to my brother. But for..."
    bea @angry "For violations of the Galarian Invasive Species Act."
    bea @angry "He'd brought in non-native Galarian Pokémon. He was a foreigner."
    bea @closedbrow angrymouth "For {i}this{/i} crime, he was brought to justice. But nothing else."

    red @talking2mouth "...I guess he just got a slap on the wrist, then?"

    bea @surprised "Hm?"
    bea @talkingmouth "No, no. Galar metes out {i}serious{/i} punishments for that sort of wrongdoing."
    bea @closedbrow talkingmouth "Unless there are extenuating circumstances I'm not yet aware of, he should still be imprisoned."

    red @surprised "What? Okay, he's a complete scumbag who deserves to rot, obviously, but... years in prison for violation of a wildlife ordinance?"

    bea @closedbrow talkingmouth "Galar staked its cultural identity on that law. Enforcement is necessary. And there's certainly no way he could have gotten into the region with foreign Pokémon unless he snuck in."

    pause 1.0

    bea @sad "...Do you think he snuck in to... to find victims?"

    red @sad2eyes angryeyebrows talking2mouth "...I don't know. But the thought makes me sick."

    bea @closedbrow talkingmouth "Yes. I will never be able to forget what he did. Nor do I seek the strength to forgive."
    bea @sad "But... I seek to move on. And I am uncertain if visiting this man... looking in his eye, for the first time, truly... would help me, or chain me to him again."
    bea @angrybrow talkingmouth "Should I bring my case before the courts? With no evidence, except two children testifying to a years-old crime?"

    pause 1.0

    bea @talkingmouth "I am tempted, for the first time in my life, to {i}not{/i} add something to the plan."
    bea @talkingmouth "The risks seem too great. The gains too marginal. The chance of everything becoming worse... nonzero."

    pause 0.5

    red @talking2mouth "Well... it's up to you, of course."

    bea @sad "What would you advise? If there was someone you once hated obsessively, someone who came closer than anyone else to ruining your life?"

    pause 0.5

    show bea surprisedbrow frownmouth with dis

    red @closedbrow sweat talking2mouth "I'm... dorming with him."

    bea @talkingmouth sweat "That may be going a little far."

    red @closedbrow talking2mouth "Wasn't exactly my choice."

    pause 0.5

    bea -surprisedbrow -frownmouth -surprised @talkingmouth "...Sensei Marshal says one's instincts are a fighter's greatest weapon and guide."
    bea @angrybrow talkingmouth "And my instincts tell me that this man is a danger who can only serve to hurt me further if I let him, even a little bit, into my life."

    red @talking2mouth "Good advice."

    bea @sad "But... Sensei Marshal also says that the strongest fighters are those who can crush the instinct to flinch from danger, and face it head-on."
    bea @closedbrow talkingmouth "Fighters who have the inner focus to avoid flinching when a fist comes their way, and the presence of mind to strike back, faster..."
    bea @talkingmouth "Perhaps that is what I should be doing now."

    pause 0.5

    bea @talkingmouth "But, then, which path should I take? I do not want to be hurt again. I see no advantage to facing this monster once more."
    bea @sad "But... I also cannot help but feel the shame of leaving this business unsorted may be even more caustic a mark on my life."

    pause 0.5

    bea @closedbrow angrymouth "Cruel fate that pushes me between... between a... some sort of... hard object, and..."

    red @sadbrow talkingmouth "A rock and a hard place?"

    bea @closedbrow talking2mouth "That works."

    pause 1.0

    bea @talking2mouth "No. I will not let this corrupt disembodiment of a man assail me any longer, not in body, nor in mind. I shall forget him entirely, and focus on my brother, who still needs my strength."

    red @happy "That's a great idea."

    bea @talkingmouth "And in focusing on my brother, I need to ensure this world is kept safe from monsters like the one who attacked us. I will return to Galar and see him justly punished."

    red @talkingmouth "O... kay."

    bea @talkingmouth "Though, on second thought, is the best justice not living well? I will grant him no satisfaction. If he does not remember me, I shall not grant him the courtesy of being remembered. I stay here."

    red @talking2mouth "Right."

    bea @closedbrow talking2mouth "But perhaps there is a way to see justice done, and not grant him the courtesy of an audience with me. If I were to operate using an intermediary, someone who is willing to testify on the behalf of my brother and I..."

    red @unamusedbrow unamusedmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    show bea surprisedbrow frownmouth with dis

    red @talkingmouth "Bea. You're spiraling."

    bea -surprisedbrow -frownmouth -surprised @closedbrow talking2mouth "Oh. So I am."

    pause 0.5

    bea @closedbrow talkingmouth sweat "Perhaps this news is still too fresh for me to come to a solid conclusion."
    bea @sad "Perhaps I... have been relying on you too much, as of late."
    bea @sad "Cheren did warn of such things..."

    red @sadbrow talkingmouth "Hey. Don't worry about that. You {i}can{/i} rely on me, alright? As much as you need. We're teammates."

    bea @talking2mouth "Perhaps. Though I feel different about you than I do about most teammates. Sonia, Ethan, Erika... they are worthy teammates, certainly. But you spark something different in me, something I cannot easily name."

    red @winkbrow talkingmouth "What, got a bit of a crush?"

    bea @talkingmouth "I think so, yes."

    red @surprised "Oh."

    bea @talking2mouth "You seem surprised."

    red @talking2mouth "I, uh, I honestly wasn't expecting you to be so... I dunno. Forward."

    bea @closedbrow talkingmouth "Perhaps it is only the lack of consequence to my words that allows me to be so free with them."
    bea @talkingmouth "Crush or not, I must put this issue of my attacker to rest before any sort of dalliance with anyone I may or may not, hypothetically, fancy."
    
    red @sweat talkingmouth "On the one hand, bummer. On the other hand, good job at prioritizing!"

    bea @closedbrow talking2mouth "Thank you. It is a skill I have been practicing. It is only your influence that allows me to do so."

    red @happy "Nice."

    pause 0.5

    redmind @sad2eyes poutmouth "Hoisted by my own petard, huh..."

    bea @talkingmouth "Well... let's discuss this. I do not wish to dither on this topic any longer. Will I go and seek justice? Will I stay and seek peace?"
    bea @angrybrow talking2mouth "It is decided, now, in this classroom. We have only our words to carve our futures, but it shall be carved nonetheless."

    show bea:
        ease 0.5 ypos 1.1 zoom 1.2

    bea @talkingmouth "[first_name] [last_name]. Let us debate."

    red @unamusedbrow talking2mouth "...Alright."

    scene blank2 with splitfade

    narrator "You and Bea talk for a very, {i}very{/i} long time about the pros and cons of either going or staying."
    narrator "The conversation swings back and forth, and forth and back, and back and forth, as you attempt to gently guide Bea into a conclusion that is truly her own."
    narrator "And, finally, you do, as she proudly declares:"

    show classroom
    show fighttype
    show bea
    with splitfadefast

    bea @talking2mouth "I will not go."

    red @surprised "What? But you just said that you would. Wasn't that what we were arguing towards for the past half hour?"

    bea @talking2mouth "It may have been. But I am now confident that not going is the correct course of action."

    red @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
    red @closedbrow talking2mouth "Alright. As long as you're satisfied."

    bea @talkingmouth "I am."

    pause 2.0

    bea @talking2mouth "So, now that {i}that's{/i} been dealt with--"

    show nate surprisedbrow frownmouth:
        xpos -0.2
        ease 0.4 xpos 0.6
        ease 0.3 xpos 0.7
        ease 1.0 xpos 0.25

    show bea surprisedbrow frownmouth:
        xpos 0.5
        ease 0.2 xpos 0.75

    nate angryeyebrows winkeyes angrymouth @surprised "Wait!"

    narrator "Nate bursts into the room, panting."

    nate @talking2mouth "Pah... pah... pah..."

    bea @surprisedbrow talkingmouth "Nate? Is there something wrong?"

    nate @talking2mouth "The... pah... the information I gave you... it's... pah..."

    $ PlaySound("idea.ogg")

    show blank

    pause 0.1

    hide blank

    nate @talking2mouth "Outdated."

    pause 2.0

    red @talkingmouth "Okay. Uh, outdated how?"

    nate -angryeyebrows -winkeyes -angrymouth @sweat closedbrow talking2mouth "Uh, the guy isn't in Galar anymore."

    pause 1.0

    show bea angrybrow with dis

    bea @talkingmouth "You're sure?"

    nate @closedbrow talking2mouth "Yeah. He was transferred to the Maximum-Security Lacunosa Correctional facility a few months ago."
    nate @talkingmouth "...Pending further sentencing for crimes committed on Unovan soil years previously."

    bea @closedbrow "{w=0.5}.{w=0.5}.{w=0.5}."
    bea @angrymouth "Bugger."

    pause 1.0

    nate @winkeyes angryeyebrows talking2mouth "...Yeah. Sorry. My contact only just updated me." 

    red @confused "But... you said you weren't even going to try and see him, right, Bea?"

    bea @closedbrow talkingmouth "That is the conclusion I came to when I had the choices presented in front of me equally, yes..."
    bea @sad "But now the circumstances have changed."
    bea @angrybrow talkingmouth "I do not like the idea of this depraved beast facing justice in another country's jurisdiction, when his worst crime was doubtlessly committed on Galarian soil."

    show nate sad2eyes sadeyebrows frownmouth with dis

    redmind @confusedeyebrows frownmouth "Hm? Nate just looked away... there's no way he disagrees, right?"

    nate -sad2eyes -sadeyebrows @talking2mouth "Well... if it's any consolation, Lacunosa tends to be pretty draconian in their sentencing laws."
    nate @happy "I mean, legends say they kept a big icy dragon locked up just outside their walls for centuries, so they can keep one man in there."
    nate @sadbrow talkingmouth "...And make sure he's not happy, you know?"

    bea @closedbrow talkingmouth "This is not a consolation. I am sorry, Nathaniel."

    nate @closedbrow talking2mouth "{size=30}It's just Nate.{/size}"
    nate @talking2mouth "Well... with you being a foreign national, the severity of the crimes he's been imprisoned for, and the fact it's a Lacunosan penitentiary, it doesn't seem likely you'll be able to visit him."

    bea @sadbrow talkingmouth "Yes."
    bea @closedbrow talkingmouth "I suppose... I should consider my next move, then."

    pause 1.0

    nate @talking2mouth sweat "You probably should, yeah."

    bea @sadbrow talking2mouth "I'll spare you two the burden of helping me through the labyrinth of my mind."

    red @talking2mouth "It's not a burden. {i}You're{/i} not a burden."

    nate @talking2mouth "Yeah, what [nate_name] said. Don't talk about yourself like that, Bea."

    bea @sadbrow talking2mouth "I'm unsure. I find myself back at square one again. When I thought I had the chance to make something of this atrocity, I prioritized my own peace of mind."
    bea closedbrow sadmouth "And after all this, I still find myself no closer to providing any sort of strength or comfort to my brother."

    pause 1.0

    bea -closedbrow -sadmouth @closedbrow talkingmouth "...I must go."

    red @talking2mouth "Bea, I..."

    show nate sad with dis

    bea @talkingmouth "I think some separation of ourselves is needed. I have managed to accomplish nothing of my true goals in the time that you and I have been allied in this fashion, [first_name]."
    bea @sadbrow talking2mouth "...You almost made me feel as though it is okay to be vulnerable. {i}This{/i} is too sharp a reminder that such a thing is not true--and never will be."
    bea @talkingmouth "I have felt such comfort around you, I nearly forgot my pursuit of strength."
    bea @sadbrow talkingmouth "It seems... you breed a [bluecolor]weakness{/color} in me."

    pause 1.0

    bea sad "Please excuse me."

    $ RelationshipRankUp("Bea", "Weakness", 2)

    $ naterelation = GetRelationship("Nate")

    nate @talking2mouth "...[naterelation], this is what I fight for."

    red @talking2mouth "...Huh?"

    nate @talking2mouth "It's not an abstract sense of peace. I fight for a world where Bea would never have to go through this."
    nate @sad2eyes talking2mouth "I fight for a world where kids in your neighborhood can go out late at night and play."
    nate @closedbrow talking2mouth "I fight for a world where a child could go on a league challenge by herself, and explore the entire region with nothing but her Pokémon."

    pause 1.0

    nate @talking2mouth "I hate my job, sometimes... but I want to protect the Beas out there way more."

    $ ValueChange("Nate", 3, 0.25)

    nate @talking2mouth "Do you think I should go after her?"

    red @surprised "Huh? What are you asking me for?"

    nate @sadbrow talkingmouth "You're better with people than I am, [nate_name]."
    nate @sad2eyes talking2mouth "I even got in a pretty big argument, and still haven't patched that up."
    nate @talking2mouth "Anyway, what do you think Bea wants right now?"

    redmind @thinking "Hm..."

    menu:
        "You should talk to Bea later tonight, in your dorm.":
            $ AddEvent("Nate", "FollowBeaLater")

            red @talking2mouth closedbrow sweat "I might have been overdoing it with the help a bit. She's mostly irritated with me."
            red @sadbrow talkingmouth "I'm sure she'd appreciate a chat with her roommate. And while you're in there, maybe remind her I was just trying to help?"

            nate @talking2mouth sadbrow "You got it, [naterelation]."

        "You should go after her.":
            $ AddEvent("Nate", "FollowBea")

            red @talking2mouth closedbrow sweat "I might have been overdoing it with the help a bit. She's mostly irritated with me."
            red @sadbrow talkingmouth "I'm sure she'd appreciate a chat with her roommate. And while you're in there, maybe remind her I was just trying to help?"

            nate @talking2mouth sadbrow "You got it, [naterelation]."

        "She needs her space.":
            $ AddEvent("Nate", "LeaveBeaAlone")

            red @talking2mouth "She's very straightforward. If she tells you she wants to be left alone, we can trust her words."

            nate @sad2eyes sadeyebrows talking2mouth "Yeah, I guess you're right. Here I am, just trying to look through everyone's words, as usual, when sometimes, people just wear their hearts."

    pause 1.0

    nate @sadbrow talking2mouth "Seeya."

    pause 0.5 

    red @talking2mouth "Wait."

    nate @surprisedbrow frownmouth "Hm?"

    if (HasEvent("Nate", "Lv1AfterMurder")):
        red @talking2mouth "You thought that the murder of Bianca's father had something to do with the person who attacked Bea and her brother, right?"

        pause 1.0

    else:
        red @talkingmouth "You said that you needed something terrible to happen to someone else before you could move forward with your plan, right?"

        nate @sad2eyes talking2mouth "...Yeah."

        red @talking2mouth "Well. Bianca's father was just murdered."
        red @talking2mouth "I don't want to jump to conclusions, but... is there a connection there?"

        pause 1.0

        nate @talking2mouth sad2eyes "There's no evidence of it, right now, but based on what I've heard, and various patterns..."

    nate @sad2eyes talking2mouth "It's a working theory."

    red @talking2mouth "So, you lied to Bea right now?"

    nate @sad2eyes talking2mouth "It's the International Police's policy not to inform anyone about something they don't have the power to change."

    pause 0.5

    nate @talking2mouth "Ignorance isn't strength, but it {i}sure is{/i} peace."
    nate @sadbrow talking2mouth "Poor Bea needs that more than anyone else right now."

    pause 1.0

    red @talking2mouth "Bea wanted peace. She was willing to buy it at the expense of others. Are you sure it's Bea's peace you're lying to keep?"

    pause 1.0

    nate @talking2mouth "Please. Don't tell her anything until I have a plan of action."

    red @sweat closedbrow talking2mouth "I can't promise that. But I agree, it might be for the best if we keep her from the 'planning' part of the mission."

    nate @sadbrow talking2mouth "Okay. Guess that's the best I can get from you for now, then..."

    red @closedbrow talking2mouth "Keep in contact."

    nate @closedbrow talking2mouth "Yeah, see you later."

    hide nate with dis

    pause 1.0

    return

label Bea2Part2:
    $ AddEvent("Bea", "Bea2Part2")
    stop music fadeout 1.5
    queue music "Audio/Music/StowOnSide_start.ogg" noloop
    queue music "Audio/Music/StowOnSide_loop.ogg"
    call clearscreens() from _call_clearscreens_212
    scene blank2 with splitfade

    show midnight at vspaz    

    python:
        timeOfDay = "Midnight"
        playercharacter = "Bea"
        oldinventory = copy.copy(inventory)
        oldpersonalstats = copy.copy(personalstats)
        oldparty = copy.copy(playerparty)
        oldpersondex = copy.copy(persondex)
        oldclassstats = copy.copy(classstats)

        inventory = {
            Item.MachoBrace : 1,
            Item.Protein : 23,
            Item.ProteinForHumans : 36,
            Item.UnusedJournal : 1,
            Item.CherishedPicture : 1,
            Item.RedWhistle : 1
        }
        personalstats = {
            "Charm" : 1,
            "Knowledge" : 8,
            "Courage" : 45,
            "Wit" : -9,
            "Patience" : 23
        }
        playerparty = GetTrainerTeam("Bea")
        persondex = copy.deepcopy(defaultpersondex)
        #battle teammates
        persondex["Bea"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Female, "Relationship": "Self", "RelationshipRank": 0, "Events": [] }
        persondex["Allister"] = {"Named" : True, "Value" : 291, "Contact": True, "Sex": Genders.Male, "Relationship": "Sister", "RelationshipRank": 0, "Events": [] }
        persondex["Janine"] = {"Named" : True, "Value" : 33, "Contact": True, "Sex": Genders.Female, "Relationship": "Mentee", "RelationshipRank": 0, "Events": [] }
        persondex[first_name] = {"Named" : True, "Value" : oldpersondex["Bea"]["Value"], "Contact": True, "Sex": Genders.Male, "Relationship": "Burden", "RelationshipRank": 0, "Events": [], "Mood": 0 }
        persondex["Leaf"] = {"Named" : True, "Value" : 33, "Contact": False, "Sex": Genders.Female, "Relationship": "Teammate", "RelationshipRank": 0, "Events": [] }
        persondex["Sonia"] = {"Named" : True, "Value" :33, "Contact": False, "Sex": Genders.Female, "Relationship": "Teammate", "RelationshipRank": 0, "Events": [] }
        persondex["Hilbert"] = {"Named" : True, "Value" : 33, "Contact": False, "Sex": Genders.Male, "Relationship": "Teammate", "RelationshipRank": 0, "Events": [] }
        persondex["Blue"] = {"Named" : True, "Value" : 33, "Contact": False, "Sex": Genders.Male, "Relationship": "Teammate", "RelationshipRank": 0, "Events": [] }
        persondex["Silver"] = {"Named" : True, "Value" : 33, "Contact": False, "Sex": Genders.Male, "Relationship": "Teammate", "RelationshipRank": 0, "Events": [] }
        persondex["Ethan"] = {"Named" : True, "Value" : 32, "Contact": False, "Sex": Genders.Male, "Relationship": "Teammate", "RelationshipRank": 0, "Events": [] }
        persondex["Erika"] = {"Named" : True, "Value" : 33, "Contact": False, "Sex": Genders.Female, "Relationship": "Teammate", "RelationshipRank": 0, "Events": [] }
        persondex["Dawn"] = {"Named" : True, "Value" : 23, "Contact": False, "Sex": Genders.Female, "Relationship": "Former Teammate", "RelationshipRank": 0, "Events": [] }
        
        #roommates
        persondex["Hilda"] = {"Named" : True, "Value" : 44, "Contact": True, "Sex": Genders.Female, "Relationship": "Dormmate", "RelationshipRank": 0, "Events": [] }
        persondex["Nate"] = {"Named" : True, "Value" : 44, "Contact": True, "Sex": Genders.Male, "Relationship": "Dormmate", "RelationshipRank": 0, "Events": [] }
        persondex["Bianca"] = {"Named" : True, "Value" : 44, "Contact": True, "Sex": Genders.Female, "Relationship": "Dormmate", "RelationshipRank": 0, "Events": [] }
       
        #sabrina
        persondex["Sabrina"] = {"Named" : True, "Value" : 11, "Contact": True, "Sex": Genders.Female, "Relationship": "Confidant", "RelationshipRank": 0, "Events": [] }

        classstats = { 
            "Normal" : 0,
            "Fire" : 0,
            "Water" : 0,
            "Grass" : 0,
            "Electric" : 0,
            "Ice" : 0,
            "Fighting" : min(100, AimLevel() + 5),
            "Poison" : 0,
            "Ground" : 8,
            "Flying" : 3,
            "Psychic" : 0,
            "Bug" : 0,
            "Rock" : min(100, AimLevel() + 3),
            "Ghost" : AimLevel() - 11,
            "Dark" : 0,
            "Dragon" : 0,
            "Steel" : 6,
            "Fairy" : 0
        }

    pause 3.5

    scene beabedroommidnight 
    show screen currentdate
    with splitfade

    pause 2.0

    narrator "You cannot sleep."

    pause 1.0

    narrator "You lie awake in bed, staring up at the ceiling. The rhythmic snoring of your roommates is the only sound."

    beamind casual "{w=0.5}.{w=0.5}.{w=0.5}."
    beamind @closedbrow talking2mouth "You are unduly affected by that [first_name] boy's actions."

    pause 1.0

    narrator "You shift in your bed uncomfortably. The springs creak."

    pause 1.0

    hilbert night hatless @talkingmouth "Can't sleep?"

    narrator "Hilbert's voice calls out from through the wall. You pause for a second to consider how to answer."

    beamind @closedbrow talking2mouth "Should I stay silent? No, there's no reason for that. He's just a friend, inquiring about my current state. But if I do not respond, then he will be unsure as to whether he really heard my mattress. However, I must consider that this is Hilbert, who is generally {i}very{/i} confident in himself, and his answers. Perhaps he will not be uncertain. But even if he is, what advantage would this uncertainty provide? I should give him information freely. Trust is paramount. We are roommates, after all. Very well, I have decided. I will say..."

    bea @talkingmouth "Yes."

    pause 1.0

    hilbert @closedbrow talkingmouth "Don't stay awake all night. You don't want to be tired for our training tomorrow."

    bea @talkingmouth "It is not my intention to."

    pause 1.0

    hilbert @talkingmouth "Try talking to someone."

    bea @surprisedbrow talking2mouth "Hm?"

    hilbert @talkingmouth "If you're feeling restless, try talking to someone about it. Maybe they could help you sort through your thoughts."

    bea @surprisedbrow talkingmouth "Am I not talking to you?"

    hilbert @closedbrow talkingmouth "No. I'm putting my headphones on. I can't get to sleep with you twisting and turning, anyway."

    pause 2.0

    bea @surprised "{w=0.5}.{w=0.5}.{w=0.5}."

    beamind @closedbrow talking2mouth "Honestly. Unovans. Onion would have such a laugh if he knew that my new dorm was four Unovans and myself."

    pause 1.0

    beamind @surprisedbrow talking2mouth "It... {i}has{/i} been a while since I've called him, hasn't it?"
    beamind @closedbrow talking2mouth "What time is it in Galar right now? They're... five hours behind Kobukan, right?"
    beamind @happy "So, that should be... 7 P.M.? I'm sure he's still awake."

    show phone_B behind blank2
    show phone_A behind blank2
    with fadeinbottom

    $ renpy.sound.play("audio/outgoingcall.ogg", loop=True)

    narrator "The phone rings. {w=0.5}Once. {w=0.5}Twice. {w=0.5}Thrice."

    pause 1.0

    narrator "Halfway across the world, a small hand clumsily swipes on the screen of a ringing phone."

    $ renpy.sound.stop()

    show allister behind phone_A with Dissolve(2.0):
        ypos 0.8

    allister "...Beatroot?"

    bea @happy "Onion! I hope I didn't stop you from going to bed."

    narrator "Allister blearily wipes some sleep out of his eyes. Not an easy task, given the mask."

    allister "Beatroot... it's 5 AM here."

    bea @surprised "Oh."

    pause 1.0

    bea @closedbrow talkingmouth "So... five hours behind, but actually... I see."
    bea @sadbrow talking2mouth "Apologies."

    allister "'Salright."

    pause 1.0

    show allister maskneutraleyes with Dissolve(2.0)

    allister "You okay?"

    bea @surprisedbrow talking2mouth "Hm?"

    allister @masksadeyes "You're calling at... about midnight."
    allister @maskclosedeyes "Bit late."
    allister @maskpuppyeyes "Something you want?"

    bea @talkingmouth "I just..."

    pause 1.0

    beamind @closedbrow talking2mouth "I shouldn't burden him with my problems."

    pause 1.0

    bea @sadbrow talkingmouth "I was hoping you might tell me about your day."

    allister @masksurprisedeyes "You... wanted to hear about my day?"

    bea @talkingmouth "Yes."

    allister @maskclosedeyes "I just woke up."

    bea @surprised "Oh. {w=0.5}Right. {w=0.5}Of course."
    bea @sadbrow talkingmouth "Yesterday, then, maybe?"

    allister "...'Kay."

    pause 1.0

    allister "...Yesterday, in class, I learned about the kings."
    allister "Teach said they fought back the Darkest Day alone. Just the two of them. And they didn't get anything for it, either."

    pause 1.0

    allister masksadeyes "...Where did the heroes go?"

    bea @sadbrow talkingmouth "What do you mean?"

    allister "What they did back then was wicked. But no-one'd do anything like that nowadays."
    allister -masksadeyes @maskangryeyes "If the Darkest Day happened again, bet no-one'd even fight it. They'd just let it happen."

    pause 1.0

    allister maskneutraleyes "I asked Mr. Leon who'd protect us, and he said he would."

    bea @talking2mouth "Of course. He's the King of Champions. He'd fight for Galar to the bitter end!"

    allister @maskclosedeyes "Galar, okay. B-but... Galar's got people in it."
    allister @masksideeyes "I wonder if you can really help the pieces if you're trying to handle the entire whole."

    pause 1.0

    allister @masksideeyes "I read a new story."

    bea @happy "You're such an intelligent boy. Always picking up new stories." 
    bea @talkingmouth "What was this one about?"

    allister "'Sabout a Skwovet."
    allister @maskclosedeyes "See, there was a Skwovet. And this Skwovet was packing up nuts for Winter."
    allister "But Winter was coming soon. Very soon. Because the Skwovet didn't do it when he oughta."
    allister "So he needed a lot of nuts. Right quick. He knew he oughtn't've done it, but he decided to steal from another Skwovet's tree."

    bea @surprised "Oh no! What happened next?"

    allister @masksadeyes "He started stuffing his cheeks. Full up. More and more nuts. But he couldn't carry them all."
    allister @maskangryeyes "So the little thing thought he'd take advantage of its position, and started just eating the nuts it couldn't fit. Might as well, since he couldn't take them with him."

    show allister masksurprisedeyes with dis

    bea @surprisedbrow talkingmouth "How rude! But why did the Skwovet not just take multiple trips?"

    allister masksideeyes @maskclosedeyes "...I dunno. Teach didn't say that part."

    pause 1.0

    narrator "Allister seems troubled."

    bea @talkingmouth "What happened next?"

    allister maskneutraleyes "He ate so many he became fat. Really fat. Fat enough 'til he evolved into a Greedent."
    allister @masksadeyes "And then... he was too big. Greedent are pretty fat. He couldn't move, so he was stuck in the hollow tree."

    bea @surprised "Oh no!"

    allister @maskclosedeyes "He tried to escape, but he was too squished in. He couldn't move. It was hopeless."
    allister "And then... the other Skwovet came back. They saw him there, and laughed at him."

    pause 1.0

    allister -maskneutraleyes "And because he couldn't move, he couldn't feed himself. So, even though he was surrounded by food, he died."

    pause 2.0

    allister maskneutraleyes @maskclosedeyes "...That's the story."

    bea @surprised "{w=0.5}.{w=0.5}.{w=0.5}."

    pause 1.0

    bea @sadbrow talkingmouth "Onion, do all your stories end with the protagonist dying?"

    allister @masksideeyes "Only the ones I like."

    pause 1.0

    bea @talkingmouth "Well... what did your teacher say the moral of that story was?"

    allister "To not be a Greedy Gus."

    bea @sadbrow talking2mouth "I... see."

    allister @masksadeyes "I like those stories. Because the bad stuff happens to the bad people. And the good stuff happens to the good people. It all makes sense."

    bea @sadbrow talkingmouth "I understand how you feel."

    allister @maskclosedeyes "Mr. Rose says that's called 'Karma.'"

    pause 1.0

    bea @talking2mouth "Speaking of, how is the Gym?"

    allister @masksadeyes "...I still don't wanna be a leader."

    bea @sadbrow talkingmouth "Oh. Even now?"

    allister @masksideeyes "All the people... they're so loud... and they get really upset when I lose."
    allister @maskpuppyeyes "But sometimes they get really upset when I win, too. I don't know."
    allister @maskclosedeyes "And the music is too loud... and Mr. Rose wants me to do signatures for two hours every weekend..."
    allister @masksadeyes "But then the people come up... and they want to talk... and I don't want to talk to them... and I don't wanna be rude..."

    pause 1.0

    allister @masksideeyes "But Mum thinks it's good for me. And I don't want Dad to have to be on the dole."

    bea @closedbrow talkingmouth "...It's just a temporary position. At the end of this year, I'll return, and take over the gym."

    allister @masksadeyes "...Mr. Rose says it takes a lot of money to change the merch when a Gymmie drops."
    allister @masksideeyes "He showed me a warehouse full of Allister Plushes. Me Plushes."
    allister @masksadeyes "He said if I left the Gym, he'd have to get Miss Oleana to burn all those."

    bea @angrybrow talkingmouth "Well, that's a nasty trick for him to try to pull on you. He {i}won't{/i} burn them."
    bea @closedbrow talkingmouth "He will probably just donate them to the Pokémon League Museum in Hammerlocke."

    allister "{w=0.5}.{w=0.5}.{w=0.5}."

    bea @happy "Wouldn't that be nice, Onion? You'd get to be part of Galar's history."

    pause 1.0

    allister @masksideeyes "I want to leave Galar."

    bea @surprised "What? Why?"

    allister @masksadeyes "You did."

    bea @talkingmouth "Well, yes, but... it's our homeland!"

    allister @maskpuppyeyes "You left."

    bea @sadbrow talkingmouth "Well, yes... but there was... it was part of a larger plan. Leaving was just a step to... the bigger picture."

    pause 1.0

    show allister -maskneutraleyes with Dissolve(2.0)

    allister -maskneutraleyes "I wonder if you can really help the pieces if you're trying to handle the entire whole."

    bea @sadbrow talkingmouth "...Onion."

    allister "That's a kiddy nickname. I'm Allister now. Gym Leader Allister."

    pause 1.0

    allister "Mr. Rose told me. I've got a lot of responsibility. He said I should use the same name all the time. Otherwise the markets get confused."

    pause 1.0

    bea @sadbrow talkingmouth "...I'm still Beatroot."

    allister "...I need to get away. But I feel like I'm Shadow-Tagged. Like there's something trapping me here. In Galar, in Stow-On-Side. In the gym." 
    allister "Trapped. Just like that fatty Greedent."
    allister "And... every day... the other Skwovet come to my gym and point at me, and cheer, and laugh, and boo... and I'm stuck."

    pause 1.0

    allister "...I want to go."

    bea @sadbrow talkingmouth "I-"

    hide allister with dis

    narrator "Allister hangs up."

    pause 1.0

    narrator "You close your eyes and focus on your deep-breathing exercises. Oddly, [first_name]'s face surfaces in your mind."

    show blank2 as secondblank with dis:
        alpha 0.5

    show red sadbrow with dis

    red @talkingmouth "...Hey, Bea."
    red @happy "You'll make it through. You're strong, you know? In every way that matters. And I'm here to help you."
    red @talkingmouth "C'mon. Let me help you."

    python:
        oldpersondex["Bea"]["Value"] += 3
        oldpersondex["Bea"]["Mood"] += 3

        AnimateValueChange(3, 0.5, True)

    pause 1.5

    hide secondblank
    hide red
    with dis

    pause 2.0

    narrator "After a moment, the tightness in your chest passes."

    hide phone_B
    hide phone_A
    with fadeoutbottom

    bea @sadbrow talkingmouth "Goodnight, Onion. {w=0.5}My beloved brother."
    bea @closedbrow talkingmouth "{size=30}Sleep well.{/size}"
    bea @sadbrow talkingmouth "I love you. And... if you give me just a little more time... I {i}will{/i} be your strength."

    call clearscreens() from _call_clearscreens_213
    scene blank2 with Dissolve(3.0)

    python:
        inventory = oldinventory
        personalstats = oldpersonalstats
        playerparty = oldparty
        persondex = oldpersondex
        classstats = oldclassstats
        playercharacter = None

    return
