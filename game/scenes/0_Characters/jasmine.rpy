label Jasmine1:
    scene pool 
    show jasmine swimsuit wethair closedeyes happyeyebrows:
        ypos 1.0
        block:
            ease 5.0 ypos 1.05
            ease 5.0 ypos 1.0
            repeat
    with Dissolve(2.0)
    show screen songsplash("Olivine City", "Zame")
    queue music "Audio/Music/olivine_start.ogg" noloop
    queue music "Audio/Music/olivine_loop.ogg"

    narrator "You walk into the pool and are somewhat surprised to see Jasmine in the water."
    narrator "She appears to be deep in relaxation, as her eyes are closed, and she doesn't seem to notice you, though she's still standing."

    pause 2.0

    jasmine @talkingmouth "Would you like to swim laps? I can get out."

    show jasmine -closedeyes -happyeyebrows with dis

    red @happy "'Fraid I don't have my trunks. And this vest soaks up water like a sponge."

    jasmine @talkingmouth "Oh, [first_name]! You should have called out. I'd have addressed you much sooner."

    red @happy "You looked like you were having fun."

    show jasmine:
        ease 0.5 ypos 1.2 zoom 1.3
        block:
            ease 5.0 ypos 1.25
            ease 5.0 ypos 1.2

    narrator "You sit down next to the pool."

    red @talkingmouth "Going for a swim? Or meditating?"

    jasmine @talkingmouth "Moreso the latter. The water is nice and cool. I feel as though I weigh less in it. I can relax for a while."

    pause 1.0

    jasmine @sadbrow sweat talkingmouth "...They do the same thing for elderly Pokémon, you know."
    jasmine @lightblush embarrassed "A bit embarrassing, isn't it?"

    red @talkingmouth "Whatever you need to get you through the day. If it works for an old Mabosstiff, I don't know why it wouldn't work for humans."

    jasmine @closedbrow talking2mouth "Ma... Mabosstiff? Who?"

    red @talkingmouth "Paldean Pokémon. Dark-Type Dog."

    jasmine closedbrow @talkingmouth "I see."

    pause 2.0

    jasmine -closedbrow @sadbrow talking2mouth "Well, I suppose I should be getting out. If it's not too much trouble, might I ask you to give me a hand?"

    red @happy "Not a problem."

    show jasmine:
        ease 0.5 ypos 1.0 zoom 1.0

    pause 1.0

    show jasmine sarong with dis

    pause 0.5

    jasmine @talkingmouth "Thank you. Now, let me just..."

    show jasmine bunch noties with dis

    pause 0.5

    show jasmine bunch hairtie with dis

    pause 0.5

    show jasmine bunches hairtie with dis

    pause 0.5

    show jasmine bunches hairties with dis

    narrator "You watch Jasmine tie her hair up with practiced grace. You'd never imagine that even those small arm movements exhaust her, save for a slight tightening of the lips."

    jasmine @happy "There. Hair up again. Don't I look presentable, now?"

    red @happy "You're certainly a gift."

    jasmine @happybrow talking2mouth "Hm."

    pause 1.0

    jasmine @closedeyes angryeyebrows frownmouth "...Hm."

    red @talking2mouth "Something wrong?"

    jasmine @talkingmouth "Nothing overly so. But it takes a while for my body to adapt to the new pressure, after getting out of the water."

    pause 0.5

    redmind @thinking "...I'm not sure I'd even be able to tell the difference. I wonder...?"

    pause 1.0

    jasmine @talkingmouth "You look inquisitive."

    menu:
        "How did this happen?":
            $ AddEvent("Jasmine", "AskedCondition")

            jasmine @closedeyes talking2mouth "...Hm."
            jasmine @talkingmouth "I suppose we've been through a good amount together? The whole Student Council fiasco..."
            jasmine @talkingmouth "Yes, I suppose there's no harm in telling you."

        "Would you like to go for a walk?":
            $ AddEvent("Jasmine", "AskedWalk")

            jasmine @happy "Certainly."

    jasmine @talkingmouth "Though I would ask a few moments to get changed first, if you don't mind."

    red @talkingmouth "'Course not. Go ahead."

    hide jasmine with dis

    pause 1.0

    narrator "Jasmine walks away, so you occupy yourself with your phone. You suddenly realize, however, that you only heard her take a few steps away."

    show jasmine swimsuit sarong lightblush embarrassedbrow embarrassedmouth with dis

    if (HasEvent("Jasmine", "AskedCondition")):
        jasmine @talkingmouth "...You asked me a somewhat personal question. 'How did this happen'. It's only fair that I ask such a question back to you, yes?"

    else:
        jasmine @talkingmouth "I apologize profusely, I'm being {i}very{/i} silly, but... do you mind if I ask a somewhat personal question?"

    red @confused "Yeah? Sure."

    jasmine embarrassedmouth @embarrassedeyes talkingmouth "When... {w=0.5}{i}ahem.{/i}{w=0.5} When you see my body, what do, um, what do you think?"

    pause 2.0

    redmind @surprisedbrow frownmouth "Oh."

    redmind @thinking "So that's where we're going with this."

    menu:
        "Well, you're beautiful.":
            $ AddEvent("Jasmine", "JamesBlunt")
            pause 1.0

            jasmine -embarrassedmouth @talkingmouth "I'm sorry? I think I must have misheard you."

            show jasmine surprisedbrow frownmouth mediumblush with dis

            red @happy "You're beautiful."

            pause 2.0

            jasmine @talking2mouth "Oh."

            pause 0.5

            jasmine -surprisedbrow -embarrassedeyes -frownmouth -mediumblush @sad2eyes lightblush sadeyebrows talkingmouth "I... please excuse that question. I was... just too curious."

        "Nothing in particular.":
            $ AddEvent("Jasmine", "NothingInParticular")
            jasmine -lightblush -embarrassedmouth @confusedeyebrows talking2mouth "Well, that's not very entertaining, is it?"

        "You're not {i}conventionally{/i} attractive.":
            $ AddEvent("Jasmine", "GirlYouUggo")

            jasmine -lightblush -embarrassedbrow -embarrassedmouth @sad2eyes sadeyebrows talking2mouth "...I see. That's... disheartening, but not entirely unexpected."

    pause 0.5 

    jasmine @talking2mouth "...That must seem terribly vain of me to ask a question like that out of thin air, no?"

    red @sadbrow talkingmouth "I think I get it."

    jasmine @confusedeyebrows talkingmouth "Oh?"

    red @talkingmouth "You probably have a difficult time getting a straight answer out of anyone, don't you?"

    jasmine @sadeyebrows talkingmouth "Yes, I must confess that's true. Very observant of you, [first_name]. I'm sure you can imagine why, given my various... circumstances, people sometimes act with more tact than I need or want."

    red @closedbrow talking2mouth "And you thought because of my Frienergy, that I, well,  that I'd {i}have{/i} to give you a straight answer."

    jasmine @talkingmouth "I'm afraid you're quite right. Put like that, it does seem rather mercenary of me, doesn't it?"

    red @happy "Nah, I get where you're coming from. Difficult, awkward questions, right? And if there's someone like me around who can't help but answer honestly... I can see why you'd want to use me. No offense taken."

    pause 0.5

    red @talkingmouth "Did I say what you expected?"

    if (HasEvent("Jasmine", "JamesBlunt")):
        jasmine @closedbrow talkingmouth "Not at all, [first_name]."

        jasmine @lightblush talkingmouth "I've never heard... {i}anything{/i} like that before. To be honest."

    elif (HasEvent("Jasmine", "NothingInParticular")):
        jasmine @angrybrow poutmouth "[first_name], you didn't say much of {i}anything.{/i} It was a perfectly tactful dodge."

        jasmine @closedbrow talkingmouth "I've no interest in dodging. If the blow is coming, I prefer to steel myself and block it, not dodge."

        pause 0.5

        jasmine @happy "Speaking metaphorically, of course. If an actual, physical, blow were to head my way, attempting to block it head-on may prove to be quite foolish."

        jasmine @talking2mouth "In any case, your answer was more of what I have heard from many others."

    else:
        jasmine @sadbrow talkingmouth "I'm afraid so. I've had enough people speak tactfully about one's 'inner beauty' around me for me to get the message."

        jasmine @sweat closedbrow talking2mouth "Of course, no-one's come outright and said it, but..."

    red @surprised "Really? What about Grusha? You two seem very close."

    jasmine @talkingmouth "We are. We truly, deeply, love each other. But it's the sort of love that comes from being forged in the same crucible of circumstance, and..."

    jasmine @sad2eyes talking2mouth "We... try to avoid talking about our health or appearance to each other. Both of us consider it a bit of a sore spot."

    red @closedbrow talking2mouth "Hm... That makes sense."

    $ ValueChange("Grusha", 3, 0.33)

    narrator "Your understanding of Grusha deepens..."

    jasmine @sweat talking2mouth "Also... personally, {i}I{/i} don't see the need to make the distinction, but Grusha prefers I specify that our love is platonic."

    red @happy "Yeah, I got those vibes. He probably just wanted to make sure people knew you weren't taken."

    jasmine @sadbrow talkingmouth "He's thoughtful like that."
    jasmine @talkingmouth "Now, please, pardon me. I should go get changed."

    red @happy "Don't let me stop you, this time."

    hide jasmine with dis

    pause 1.0

    call clearscreens() from _call_clearscreens_141
    scene blank2 with splitfade

    narrator "Jasmine comes back out, and begins to walk steadily in a particular direction, beckoning you to follow."

    pause 0.5

    red @talkingmouth "Where're we going?"

    if (HasEvent("Jasmine", "JamesBlunt")):
        jasmine sundress @talkingmouth "You'll see."

        show seaport 
        show jasmine sundress
        with splitfade

    else:
        jasmine @talkingmouth "You'll see."

        show seaport 
        show jasmine
        with splitfade

    pause 0.5

    red @talkingmouth "Oh, the seaport. Nice."

    if ("cramorantobj" in globals() and cramorantobj in AllPokemon()):
        red @happy "I got a Cramorant here. It tried to guzzle down [pika_name]."

        $ renpy.music.play("Audio/Pokemon/pikachu_angry1.ogg", channel="altcry", loop=None)

        libpikachu @angryeyes frownmouth "Pika!"

    jasmine @talkingmouth "I like to come out here once in a while. On good days. It reminds me of home."

    pause 1.0

    show jasmine:
        xpos 0.5 ypos 1.0 zoom 1.0
        ease 0.5 xpos 0.5 ypos 1.2 zoom 1.3

    jasmine @closedbrow talking2mouth "That being said... I'm utterly exhausted. It will take a while for me to gather the strength to make the return journey."
    jasmine @sadbrow talkingmouth "I don't suppose I might trespass upon you further, and ask you to keep me company for a while?"

    red @sadbrow talkingmouth "Of course. I wasn't planning on leaving anytime soon."

    if (HasEvent("Jasmine", "BrendanConnection")):
        red @closedbrow talking2mouth "You said this reminded you of home, right? I think I remember you saying you're from Johto?"

        jasmine @talkingmouth "That's right. A harbor town named Olivine City. Well, I suppose it's not so much of a town, it's a city, but it always felt like a town to me. It was smaller. Cozy."

    else:
        red @closedbrow talking2mouth "You said this reminded you of home, right? Do you come from a port city?"

        jasmine @talkingmouth "That's right. A harbor town named Olivine City, on the West Coast of mainland Johto." 
        jasmine @sweat closedbrow talking2mouth "Well, I suppose it's not so much of town, it's a city, but it always felt like a town to me. It was smaller. Cozy."

    red @talkingmouth "Olivine, huh? May I guess that your biggest exports were olives? Maybe grapes?"

    jasmine @happy "Oh, I see why you would think that, but not quite."
    jasmine @talkingmouth "Olivine is actually a type of mineral. It's a green, brittle, mineral with conchoidal fractures and poor cleavage."

    red @closedbrow talking2mouth "...Rock nerd?"

    jasmine @lightblush closedbrow talking2mouth "Admittedly, Olivine is the only mineral I {i}really{/i} know anything about. And those fancy words I said before basically boil down to 'it shatters.'"
    jasmine @talkingmouth "But I do find rocks and minerals interesting. Passingly."

    if (GetRelationshipRank("Sonia") > 0):
        red @talkingmouth "Nessa told me that the science club basically boils down to mostly just sitting around and studying rocks."
        red @happy "Maybe that'd be up your alley."

        jasmine @sadbrow talkingmouth "Perhaps. What I know about Olivine wasn't because of any sort of study, though, just frequent visits to Olivine's mining museum."

    jasmine @talkingmouth "Before Olivine became a city focused on shipping and transportation, it was famous for its mining industry."
    jasmine @happy "The first Steel-type gym in the world was founded in Olivine, and the very first Steelix was evolved there, as well."

    red @happy "The city must be very proud."

    pause 0.5

    jasmine @talking2mouth "Not... not exactly. The museum has much more of a 'gaze upon what happened here and let it never happen again' bent to it."

    red @confused "Hm?"

    jasmine @talking2mouth "The early days of Olivine's mining industry were much more unregulated. The metals from the mines would be flushed away with water gathered from the harbor."
    jasmine frownmouth @closedbrow talking2mouth "That water would then return to the harbor, or seep into the ground, poisoning our aquifers."

    red @surprised "What?"
    red @sadbrow talking2mouth "Oh. Oh, shit."

    jasmine @sad2eyes sadeyebrows talking2mouth "There were people who knew what the health effects would be, of course, but... they considered it an acceptable loss."
    jasmine @angrybrow shadow talking2mouth "Those cruel men were, largely, punished, and barred from the city."
    jasmine @talking2mouth "But... the damage was done. The last three generations grew up with trace metals in all their water for years, and the effects have been..."

    pause 0.5

    jasmine @talking2mouth "Well, I'm one of the lucky ones. I still have my mind, my reason. Not all were so lucky."

    red @talkingmouth "So then... your health...?"

    jasmine @sadbrow talking2mouth "Possibly. The contaminants caused many birth defects. The doctors think it likely that, perhaps, a genetic proclivity towards fatigue was triggered by the water."

    pause 1.0

    red @talking2mouth "How did this stop? Like, what triggered the change?"

    jasmine @talkingmouth "Science. Education. As the citizens of Olivine became more educated, more and more individuals started to notice the patterns emerging." 
    jasmine @sadbrow talkingmouth "The erratic, emotional behavior of our parents. The sickliness and frailness of ourselves, and our children."

    red @sadbrow talking2mouth "Jeez. That's awful."

    jasmine @talkingmouth "A class-action lawsuit was put together. In all fairness to the justice system, those affected earned a {i}considerable{/i} amount of money."
    jasmine @happy "...Which would be why I am now in Kobukan."
    jasmine @talking2mouth "But the town was still ruined. The cleanup operation would have cost billions, and the water would still take years to rid itself of the toxicants."
    jasmine @sadbrow talking2mouth "...People like to think that it's just bad luck that there are people like me, that I'm an unfortunate victim of the universe's dice."
    jasmine @closedbrow talking2mouth "More and more, though, it's clear there are {i}systems{/i} in place that have far more sway over the dice than those responsible would admit."
    jasmine @sadbrow talkingmouth "After all, you can't 'punish' bad luck. It's an easy scapegoat for those seeking to avoid punishment."

    red @sadbrow talking2mouth "That's so messed-up."

    pause 0.5

    red @sadbrow talkingmouth "But... pardon me if I'm wrong here... the way you were talking, it sounded like you haven't lost {i}all{/i} hope for Olivine? Was there more to this story?"

    jasmine @talkingmouth "Of course. Because for every sword that falls, there will be a shield to rise up and meet it."
    jasmine -frownmouth @talking2mouth "{i}This{/i} shield was my upperclassman, Eugene."

    pause 0.5

    jasmine @surprised "Oh, sorry, Eusine. He changed his name."
    jasmine @sweat closedbrow talking2mouth "Well, sort of. He was a performer, a magician. And his {i}stage name{/i} was Eusine, but then he started calling himself Eusine when {i}not{/i} performing, and..."

    red @talkingmouth "Jasmine. I'm really interested in your story. Just not {i}this{/i} part."

    jasmine @talkingmouth happybrow "Noted."
    jasmine @talkingmouth "The point is that, in Johto, there is a legend of a certain Pokémon. This Pokémon is known as 'Suicune.'"

    show jasmine surprisedbrow frownmouth with dis

    red @talkingmouth "What, like an almost-anagram of 'Eusine'?"

    pause 1.0

    jasmine -surprisedbrow -frownmouth @sweat closedbrow talkingmouth "Hm. I genuinely never noticed that."
    jasmine @talkingmouth "Anyway, yes."
    jasmine @talkingmouth "Now, the legend of Suicune says that it can purify any water it steps on. Eusine was determined to track it down and catch it, so he could purify Olivine."

    red @surprised "Oh my God. He succeeded?"

    jasmine @talkingmouth "In a way."
    jasmine @sweat talking2mouth closedbrow "Admittedly, he never... 'caught' Suicune. Not for lack of trying. But he {i}did{/i} find it, and he chased it all around Johto, and even Kanto."
    jasmine @talkingmouth "When telling the story later, he admits that for much of the chase, Suicune was always one step ahead." 
    jasmine @talkingmouth"But right before its journey to Olivine, he managed to get Suicune in one place long enough that he was able to explain what he wanted."

    red @talkingmouth "...So he thinks Suicune listened to him, and went to Olivine to purify the water on purpose?"

    jasmine @talkingmouth "He'd dare not suggest such a thing. But it seems likely, yes."

    red @surprisedbrow talking2mouth "Wow."

    jasmine @sad2eyes sadeyebrows talkingmouth "For his heroics, he was given the key to the city, and an invitation to join the local Pokémon Ranger team."

    jasmine @happy "He turned down both. All that mattered to him was that he eventually caught Suicune. Perhaps he forgot his initial goal in the thrill of the chase."

    red @talkingmouth "But... it's impossible to catch a legendary Pokémon, isn't it?"

    jasmine @talkingmouth "Conventional wisdom would seem to say so."

    pause 0.5

    jasmine @talking2mouth "Of course, conventional wisdom told the children of Olivine to stop overreacting, and that everything was fine."
    jasmine @shadow angrybrow talking2mouth "The wisdom of the elders killed the children."
    jasmine @talking2mouth "It was only... what could {i}only{/i} be considered a foolish action... that saved us."

    pause 0.5

    jasmine @sadbrow talkingmouth "So perhaps conventional wisdom's guidance can be discarded when it comes to matters of legend."

    red @talkingmouth "Seriously. I never could have imagined something like {i}that{/i} would happen."

    jasmine @talkingmouth "After that big fight in Hoenn, many people think of Legendary Pokémon as threats."
    jasmine @sad2eyes talkingmouth "And of course, there are those who, for thousands of years, have seen them as gods."
    jasmine @talkingmouth "I think the truth is probably somewhere in-between. I think they are largely helpers. When they feel like it."
    jasmine @closedbrow sweat talkingmouth "Not something we can rely on to pull us out of our messes. But not something we have to spend every waking moment on our knees to, or watching over our shoulders for."

    pause 0.5

    jasmine @happy "Just... 'helpers.' Sometimes."

    pause 0.5

    red @talkingmouth "Like people."

    pause 0.5

    jasmine @talkingmouth "{i}Exactly{/i} like people."

    pause 1.0

    narrator "You sit on the dock together, watching the local Aipom harass the sailors for a while."

    pause 1.0

    red @talkingmouth "Hey. Aipom is a Johto-native Pokémon, right?"

    jasmine @surprisedbrow talking2mouth "Hm? Yes, I believe so. I saw several in Olivine. They liked to hang out{w=0.5}--literally{w=0.5}--at the port there, too."

    pause 0.5

    red @confusedeyebrows talkingmouth "Why are they here? Like, at a port? Don't they normally live in trees?"

    jasmine @closedbrow "{w=0.5}.{w=0.5}.{w=0.5}."
    jasmine @talkingmouth "Perhaps it's the tall masts of the ships here. If they can steal enough food from restaurant garbage dumps in the area, the tall masts may be a suitable replacement for their native habitats."

    pause 0.5

    narrator "Some unidentifiable berry goes {i}splat{/i} as it lands on a sailor's head. He roars at the Aipom, swearing bloody vengeance in a heavy Sinnohan accent."

    $ PlaySound("pokemon/cries/{}.mp3".format(pokedexlookupname("Aipom", DexMacros.Id)))

    pause 0.5

    narrator "The Aipom just laughs."

    pause 1.0

    jasmine @talkingmouth "Or maybe they just find it fun to torment the sailors here."

    red @sweat talkingmouth "Maybe."

    pause 1.0

    $ PlaySound("splash.ogg")

    show jasmine frownmouth with dis

    pause 1.0

    jasmine @surprised "What was that?"

    red @talkingmouth "Hm?"

    jasmine angrybrow frownmouth @angrymouth "What was {i}that?{/i}"

    red @surprised "What, what happened?"

    show jasmine:
        xpos 0.5 ypos 1.2 zoom 1.3
        ease 0.2 xpos 0.66 ypos 1.0 zoom 1.0

    jasmine @talking2mouth "Excuse me! Excuse me, Sir!"

    narrator "Jasmine gets up and runs up to one of the sailors, who's futilely swatting a newspaper at one of the nearby Aipom. He holds a plastic cup in his hand."

    Character("Sailor") "\"Eh? Yeah, Miss, what's the issue?\""#sailor NPC, someday?

    jasmine sweat @talking2mouth "This ship. She just jettisoned a large amount of some clear liquid off the port side."

    Character("Sailor") "\"Clear liquid? I don't know. It's probably just water. We gotta balance the water intake and output, you know.\""

    jasmine @talking2mouth "Not when the ship is docked. You should be taking {i}in{/i} water when the ship is docked."

    narrator "Jasmine points towards some holes on the side of the ship, a few meters above the waterline."

    jasmine @talking2mouth "Besides, the ballast ports are {i}there.{/i} This fluid came off the deck of the ship."

    narrator "The sailor looks stumped. He shrugs and talks into a walkie-talkie."

    Character("Sailor") "\"Calling in, this is Eldritch, on the port. Uh, I'm getting a report... well, actually, there's a little girl here... who says we're emitting some sort of clear fluid off the top deck. Anyone check in on that?\""

    pause 0.3

    Character("Eldritch") "\"Yeah, no, I told her it was ballast, but she says it wasn't that.\""

    pause 0.3 

    Character("Eldritch") "\"Uh, huh. Okay. Gotcha.\""

    narrator "The sailor lets out a big sigh, and smiles disarmingly."

    Character("Eldritch") "\"Turns out they're just cleaning the top deck. That was just soapy water running off the top.\""

    jasmine @talking2mouth "...The force of the water was much stronger than simple runoff."

    narrator "The sailor snorts, starting to look a bit annoyed."

    Character("Eldritch") "\"Look, I don't know what you saw, so I can't tell you you didn't see it, but {i}I{/i} didn't see anything.\""

    narrator "The sailor looks directly at you."

    Character("Eldritch") "\"What about you? You see anything?\""

    menu:
        "No.":
            $ AddEvent("Jasmine", "IDidNotSee")

        "No, but Jasmine did.":
            $ AddEvent("Jasmine", "JasmineSaw")

    Character("Eldritch") "\"Well, that doesn't help us, does it? Now, mind if I get back to it? I'm taking my fifteen.\""

    jasmine -angrybrow @talkingmouth "...Who owns this ship?"

    Character("Eldritch") "\"I dunno. Corporate does. She's called the SS Iron Whale.\""

    narrator "Jasmine looks at you, then back at the water, then back at you, then back at the water. Her eyes harden as she seems to come to some sort of decision."

    pause 0.5

    show jasmine:
        xpos 0.66 ypos 1.0 zoom 1.0
        block:
            linear 0.2 xpos 0.67
            linear 0.2 xpos 0.66
            linear 0.2 xpos 0.65
            linear 0.2 xpos 0.66
        block:
            ease 1.0 ypos 1.3

    jasmine @closedeyes sadeyebrows talking2mouth "Ah. I... I overexerted myself. I'm sorry. I can't..."

    red @surprised "Jasmine!"

    jasmine @talkingmouth "Pl-please... sir... can I have... some water?"

    Character("Eldritch") "\"{size=30}Of course, during {i}my{/i} fifteen...{/size} Yeah, of course. Here.\""

    narrator "He offers the cup to Jasmine, who takes it gratefully..."

    show jasmine:
        xpos 0.66 ypos 1.3
        ease 0.5 rotate -90 ypos 1.5

    $ PlaySound("splash.ogg")

    narrator "And then dives into the harbor."

    red @surprised "Jasmine, what the hell?!"

    Character("Eldritch") "\"M-Miss?! What are--hold on! {size=+10}Man overboard!{/size}\""

    call clearscreens() from _call_clearscreens_142
    scene blank2 with splitfade 

    pause 1.0

    $ PlaySound("splash.ogg")
    $ PlaySound("splash.ogg")

    narrator "You and Eldritch both dive in after her. After making sure that she's okay, and after she had signed a waiver signifying she wasn't going to sue, you and Jasmine begin the long walk back to campus."

    if (HasEvent("Jasmine", "JamesBlunt")):
        show canal 
        show screen currentdate
        show jasmine sundress wetterhair
        with splitfade

    else:
        show canal 
        show screen currentdate
        show jasmine wetterhair
        with splitfade

    red neutralhatless @playfuleyes unamusedeyebrows unamusedmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    narrator "After getting soaking wet for no good reason, you're not in the best of moods."

    jasmine @happybrow talking2mouth "Hm hm hm.~"

    narrator "Jasmine, however, seems to be humming merrily, despite the fact she is relying {i}very{/i} heavily on your shoulder for support."

    red @playfuleyes unamusedeyebrows talking2mouth "It'd be cool if I knew what that was about."

    jasmine @closedbrow talkingmouth "This cup.~"

    red @talkingmouth "The plastic cup with sailor germs on it?"

    jasmine @talkingmouth "The very same."

    red @happy "Tell me you're not going to drink from it."

    jasmine @talkingmouth "If I'm right, I don't think {i}anyone{/i} should drink from it."

    red @talkingmouth "So you got a sample of that 'ballast water'. What are you going to do with it?"

    jasmine @talkingmouth "The first thing I'm going to do is refrigerate it. Grusha keeps a ton of popsicles in our room, so the freezer is a bit full, but there should probably be room in the fridge."
    jasmine @angrybrow talkingmouth "The second thing I'm going to do is find out which company or person owns the 'SS Iron Whale.'"
    jasmine @talkingmouth "The third thing I'm going to do is bring it directly to Instructor Byron." 
    jasmine @happy "He used to be a miner, you know, and he knows all too well the dangers of contaminants. I'm sure he has some sort of test he could perform to find out what's in here."

    red @talkingmouth "...Alright. But you need to not die of a cold, first."

    jasmine @sadbrow talkingmouth "Yes, this dress is far too thin for what I did. Perhaps not my brightest moment, but... well, I don't regret my actions."
    jasmine @lightblush talkingmouth "Perhaps... perhaps I could be someone else's shield for once."

    pause 1.0

    narrator "You sneak a peek at the cup Jasmine's holding. You're trying not to disbelieve her, but... no matter how you look at it, it really {i}does{/i} seem to be ordinary water."

    redmind @thinking "Well, whatever makes her happy."

    pause 1.0

    jasmine surprisedbrow talking2mouth "I'm about to fall."

    red @surprised "Huh?"

    jasmine surprised sweat "The cup, quickly, grab it!"

    menu: 
        ">Grab the cup":
            $ AddEvent("Jasmine", "GrabCup")
            narrator "You reach out to grab the cup, moments away from spilling its precious liquid, but Jasmine..."

            show jasmine:
                xpos 0.5 ypos 1.0 zoom 1.0
                ease 0.2 ypos 1.2 rotate 3

            show grusha angrybrow behind jasmine:
                xpos 1.2
                ease 0.2 xpos 0.55

            narrator "Is caught at the last second by Grusha."

            pause 1.0

            grusha -angrybrow @unamusedeyebrows playfuleyes "Tell me why it was {i}so important{/i} that [first_name] just caught a plastic cup full of water."

            show jasmine:
                xpos 0.5 ypos 1.2 rotate 3
                ease 0.5 ypos 1.0 xpos 0.66 rotate 0 zoom 1.0

            show grusha:
                xpos 0.55
                ease 0.5 xpos 0.33

        ">Grab Jasmine":
            $ AddEvent("Jasmine", "GrabJasmine")
            narrator "You reach out to grab Jasmine, and prevent her fall, but the cup..."

            show jasmine:
                xpos 0.5 ypos 1.0 zoom 1.0
                ease 0.2 ypos 1.2 zoom 1.3 rotate 3

            show grusha angrybrow behind jasmine:
                xpos -0.2
                ease 0.2 xpos 0.33

            narrator "Is caught at the last second by Grusha."

            pause 1.0

            grusha -angrybrow @unamusedeyebrows playfuleyes "Tell me why I just caught a plastic cup full of water."

            show jasmine:
                xpos 0.5 ypos 1.2 rotate 3
                ease 0.5 ypos 1.0 xpos 0.66 rotate 0 zoom 1.0

            show grusha:
                xpos 0.55
                ease 0.5 xpos 0.33

    jasmine -surprisedbrow -frownmouth -surprised -sweat @happy "Grusha! How good to see you."

    grusha @talkingmouth "Sorry to interrupt your date."

    jasmine @surprised "Oh, this? No, no. This isn't a date."

    grusha @sad2eyes sadeyebrows "Oh."

    pause 1.0

    red @talkingmouth "What's up, man? Were you just in the area?"

    grusha @talkingmouth "Yeah, a little bit. Going to head out to the seaport to get some training in."

    red @happy "Coincidences. We were just {i}coming{/i} from there."

    grusha @closedbrow talking2mouth "That would explain why you're both soaking."

    pause 1.0

    grusha @sadbrow talking2mouth "I'm sure there's some kind of story here, but I've gotta be honest, I {i}really{/i} don't want to be a part of it."

    if (HasEvent("Jasmine", "GrabJasmine")):
        grusha @closedbrow talking2mouth "So, {i}here's{/i} your water. I'm out."

    else:
        grusha @closedbrow talking2mouth "I'm out."

    hide grusha with dis

    pause 2.0

    red @surprised "That was sudden."

    jasmine @happy "That was {i}Grusha{/i}. He's a good man, but... well, it's fair to say he has some issues engaging with the world around him."

    pause 1.0

    jasmine @sadbrow talkingmouth "Of course, I can hardly judge. I know what he's been through. What he's {i}going{/i} through."

    pause 1.0

    red @talkingmouth "Should I carry the water the rest of the way?"

    jasmine @sadbrow talkingmouth "That may be for the best."

    pause 1.0

    jasmine @talkingmouth "When I make some progress on my investigation into this... fluid, would you like me to let you know?"

    show jasmine surprisedbrow frownmouth with dis

    red @blackglasses "Absolutely. Agent [last_name] is on the case."

    pause 1.0

    jasmine @confusedeyebrows talkingmouth "Where did you get those?"

    if (HasEvent("Instructor Karen", 3.1)):
        red @blackglasses talkingmouth "Dark-Type class."

        jasmine @sweat talkingmouth "...Oh."

    else:
        red @blackglasses talkingmouth "They were at the bottom of the harbor."

        jasmine @sweat unamusedeyebrows playfuleyes talkingmouth "You probably shouldn't wear those."

        red @blackglasses happy "That sounds like conventional wisdom to me, Miss Unconventional."

    jasmine -surprisedbrow -frownmouth @closedbrow talkingmouth "Well... it's been a pleasure. Thank you for aiding me so many times on this little misadventure. I find you very reliable, you know."

    red @happymouth happyeyes happyeyebrows "It was {i}my{/i} pleasure."

    jasmine @talkingmouth "Good day. Let's do it again... under drier circumstances."
    jasmine @closedbrow sweat talkingmouth "I may need your [bluecolor]support{/color} again... both physically and emotionally."

    red @happy "You got it."

    $ RelationshipRankUp("Jasmine", "Supporter", 1)

    hide jasmine with dis

return

label Jasmine2:
    scene lobby with splitfade

    narrator "You're walking in the lobby, aimlessly, when suddenly..."

    stop music fadeout 1.5

    queue music "Audio/Music/olivine_start.ogg" noloop
    queue music "Audio/Music/olivine_loop.ogg"

    $ PlaySound("vibrate.ogg", instant=True)
    $ renpy.pause(0.5, hard=True)

    redmind @thonk "Hmm?"

    show phone_B
    show phone_A
    with fadeinbottom

    show phone_C behind phone_A with dis

    show phone_msg1 behind phone_A with dis

    if (not persondex["Jasmine"]["Contact"]):
        $ jasmine_msg = Text("Unknown Number", size=30,font="fonts/consola_0.ttf",color="#313131")
    else:
        $ jasmine_msg = Text("Rock Nerd", size=30,font="fonts/consola_0.ttf",color="#313131")

    image infirmarymessage = Text("Come quick.\nInfirmary.\nIt's Jasmine.",size=21,color="#ffffff",line_spacing=5,text_align=0.0)

    show text jasmine_msg behind phone_A:
        alpha 0.0 xalign 0.51 yalign 0.34
        ease 0.25 alpha 1.0

    show infirmarymessage behind phone_A:
        alpha 0.0 xpos .41 ypos .4
        ease 0.25 alpha 1.0

    pause

    red @surprised "What?!"

    if (persondex["Jasmine"]["Contact"]):
        redmind @sadbrow frownmouth "This is Jasmine's phone number, but... is someone else using it to contact me? Why me? What's happening? I need to go to the infirmary right away!"

    else:
        redmind @surprisedbrow frownmouth "I don't recognize this number... but Jasmine's in the infirmary? What's wrong--why'd they contact me? I need to go!"

    scene academyhall_zoom with splitfadefaster

    narrator "You quickly run to the infirmary."

    show miriam angrybrow frownmouth with dis:
        xzoom -1

    if (HasEvent("Nurse Miriam", "KnowsName")):
        miriam @talking2mouth "[first_name]! Please refrain from running outside the infirmary!"

    else:
        miriam @talking2mouth "Young man! Please refrain from running outside the infirmary!"

    miriam @closedbrow talking2mouth "Someone could walk out these doors, you could slam into them, and send them right back to the bed they came from."

    if (not HasEvent("Nurse Miriam", "KnowsName") and persondex["Nurse Miriam"]["Named"]):
        $ rescuedstring = ""
        if (rescuedtia and rescuedsabrina):
            $ rescuedstring = "my student, Tia, and Sabrina"
        elif (rescuedwill and rescuedsabrina):
            $ rescuedstring = "Instructor Will and his student, Sabrina"
        elif (rescuedsabrina and rescuedwill):
            $ rescuedstring = "Instructor Will's students, Tia and Sabrina"
        elif (rescuedtia):
            $ rescuedstring = "my student, Tia"
        elif (rescuedwill):
            $ rescuedstring = "Instructor Will"
        elif (rescuedsabrina):
            $ rescuedstring = "Instructor Will's student, Sabrina"
            
        miriam @surprised "Oh? Aren't you the young man who rescued [rescuedstring]?"

        red @wince talking2mouth "Yeah, I am, but I don't have time to talk about that right now!"

    red @sadbrow talking2mouth "I'm sorry, but I heard Jasmine was in the infirmary."

    miriam surprisedbrow frownmouth @closedbrow talking2mouth "Yes, she is. But that's no excuse to--"

    red @sadbrow talking2mouth "Is she alright?! The text told me to come quick!"

    miriam "[ellipses]"

    show miriam:
        xzoom -1
        ease 0.5 xzoom 1

    miriam @talkingmouth "Jasmine? Did you text someone to come to the infirmary quickly?"

    pause 0.5

    $ showredonly = True

    show miriam happybrow -frownmouth with dis

    jasmine @talkingmouth "Yes, I did! Please, let him in!"

    red @closedbrow talking2mouth "Oh, thank god, she sounds fine."

    if (not persondex["Jasmine"]["Contact"]):
        red @closedbrow frownmouth "I guess that number that texted me was Jasmine's. Hell of a way to start a text chain."

        $ BecomeContacted("Jasmine")

    miriam -happybrow @talkingmouth "Please go on in, then{w=0.5}--but keep your voice down."

    scene infirmarycurtainevening with dis

    pause 0.5

    red @talking2mouth "Hm? Jasmine?"

    jasmine @talkingmouth "Oh, one second. I'm sorry, I'm here, let me just..."

    scene infirmaryevening
    show jasmine pale hospital longpale tired noties nobunches

    jasmine @talkingmouth "[first_name]! I'm so glad to see you here. I was worried that..."

    $ showredonly = False

    pause 1.0

    jasmine frownmouth sadbrow @talking2mouth "Oh no. What's wrong?"

    menu:
        "Are you okay?":
            $ AddEvent("Jasmine", "SickCare")
            jasmine -frownmouth @sadbrow talkingmouth "Oh... I must look {i}quite{/i} out-of-sorts if you're asking that."
            $ ValueChange("Jasmine", 1)
            jasmine @talkingmouth "I'm afraid that dip in the harbor didn't do me much good. Far better than Olivine's water, I'm sure, but ever since, I have the most awful scratching at the back of my throat, and... a slight cough... {i}ahem.{/i}"
            jasmine @talking2mouth "It's nothing you need worry about. I feel fi--{w=0.5}as well as usual."

        "You look like shit.":
            $ AddEvent("Jasmine", "SickRoast")
            show jasmine surprisedbrow frownmouth with dis

            pause 0.5

            jasmine sad2brow @talking2mouth "{size=30}Oh.{/size}"

            $ ValueChange("Jasmine", -1)

            pause 1.0
            
            if (HasEvent("Jasmine", "JamesBlunt")):
                jasmine @talking2mouth "There was a time...{w=0.5} when you called me beautiful. I suppose I didn't realize how fickle that estimation was."

            elif (HasEvent("Jasmine", "NothingInParticular")):
                jasmine @talking2mouth "The last time we talked on this theme, you said you had no particular feelings regarding my appearance. I suppose this is... at least more of a stance."

            elif (HasEvent("Jasmine", "GirlYouUggo")):
                jasmine @angrybrow talking2mouth "Perhaps it has escaped your memory that you have told me your thoughts on my appearance. I assure you that I have not forgotten, and need not be reminded."

        "Nothing. What were you saying?":
            $ AddEvent("Jasmine", "SickAvoid")

            jasmine @sadeyebrows talkingmouth "...Nothing? That's a very kind 'nothing.', [first_name]."

    pause 1.5

    jasmine @talking2mouth "In any case, I asked you here because I've made tremendous progress."

    red @talking2mouth "On the water?"

    jasmine -sadbrow -frownmouth @surprisedbrow talking2mouth "The water--{w=0.5}oh, no."
    jasmine @happy tiredhappy "I don't have the means to test that, yet. I'm certain Instructor Byron will, though."
    jasmine @talkingmouth "Rather, I learned who the S.S. Ironsides belongs to."

    red @talking2mouth "Yeah?"

    jasmine @talkingmouth "Yes, it's the Canalave Shipping Company."

    if (HasEvent("Instructor Byron", 1)):
        red @talking2mouth "Oh, that's a pretty big coincidence! Instructor Byron's a Gym Leader in Canalave, right? I bet he knows all about it!"

        jasmine @happy tiredhappy "My thoughts exactly. What a lovely bit of serendipity."

    else:
        jasmine @closedbrow talking2mouth "Of course, Instructor Byron is the Gym Leader in Canalave--much to the disappointment of his desire to retire--so I am certain he can shed some light on the matter."

    red @talkingmouth "Well, that's great. Should we go talk to him now?"

    jasmine @sadbrow talking2mouth "Ah... I'd love to, but I'm not sure that... I'd be 'up' for it at the present."

    red @talking2mouth "Oh. Right. When would be good, then?"
    
    if (HasEvent("Instructor Byron", 1)):
        jasmine @closedbrow sweat talking2mouth "Well, Instructor Byron, as you know, follows a fairly rigid timetable. It'll be a bit tricky finding a time when you, I, and Instructor Byron are all available at once..."

        red @happy "Nah, don't worry about it. We can just talk to him after Steel class one day."

        jasmine @talkingmouth "That's a very decent idea. Let's do so."

    else:
        jasmine @closedbrow sweat talking2mouth "Well, Instructor Byron follows a fairly rigid timetable. It'll be a bit tricky finding a time when you, I, and Instructor Byron are all available at once..."

        jasmine @sadbrow talkingmouth "I don't suppose I might ask you to drop in for one of his Steel-type electives one day? If I'm there, we could talk to him after class, when I know we'd all, briefly, be free."

        red @talkingmouth "Yeah, I can definitely do that."

        jasmine @closedbrow sweat talking2mouth "Thank you. I do hope you gain something from it, even if you're not overly interested in the Steel type itself."

    pause 1.0

    jasmine @happybrow talkingmouth tiredhappy "Ah... please pardon me. I think I need to lay back down. I will see you soon, yes?"

    red @happy "Here's hoping."

    jasmine @sad2brow talking2mouth "It {i}is{/i} always a matter of hope..."

    $ AddEvent("Jasmine", "Jasmine2Part1")

    hide jasmine with dis

    narrator "This quick conversation with Jasmine did not take much time. [bluecolor]You are free to do whatever you want with the rest of your [timeOfDay].{/color}"

    if sceneviewer:
        return

    $ renpy.pop_call()
    jump freeroam

return

label Jasmine2Part2:
    $ AddEvent("Jasmine", "Jasmine2Part2")
    scene classroom with dis
    show steeltype:
        xalign 0.5 yalign 1.0
    with dis
    $ location = "steel"

    show jasmine uniform angrybrow frownmouth with dis:
        xpos 0.66

    stop music fadeout 1.5
    
    queue music "Audio/Music/olivine_start.ogg" noloop
    queue music "Audio/Music/olivine_loop.ogg"

    jasmine @talking2mouth "Okay. Thank you for being here with me, [first_name]. It's time to talk to Instructor Byron."
    jasmine -angrybrow -frownmouth @sadbrow talking2mouth "Or... do you think he'd work better with us if we called him Instructor Wolfram?"

    if (HasEvent("Instructor Byron", 2)):
        red uniform @sweat unamusedbrow talking2mouth "Well, he's never asked us to call him that before, so I think 'Byron' is probably fine."

    else:
        red uniform @happy "You know more about him than I do. I'd say 'Byron' is probably fine, though."

    show byron with dis:
        xanchor 0.5 xpos 0.33 xzoom -1

    if (timeOfDay == "Morning"):
        byron @norm2 "Hey. What are you kids still doing here? Don't you need to get to Gym class?"

    else:
        byron @norm2 "Hey. What are you kids still doing here? Don't you need to get back to homeroom?"

    jasmine @talking2mouth "Yes, but we needed to ask you something first."

    if (not HasEvent("Instructor Byron", 2)):
        byron @norm4 "Hm... Jasmine, you're one of my best students. But I've barely seen {i}this{/i} kid before."
        byron @norm4 "No offense, [first_name]."

        red @sadbrow talkingmouth "None taken, it's true."

    byron @norm4 "Are you sure that you, plural, needed to ask me something? Or is this something {i}you{/i}, Jasmine, wanted to ask me?"

    jasmine @sad2brow talkingmouth "I... suppose it might be that one."

    byron @happy2 "Well, that's fine, then. If you got something to do, stand up straight and do it. No need to bring a friend."

    if (not HasEvent("Instructor Byron", 2)):
        byron @norm4 "Again, no offense, [first_name]."

        red @confused "Still none taken, at least for now."

    show byron surprised with dis

    jasmine @talkingmouth "We want to know everything you can tell us about the Canalave Shipping Company."

    byron @surprised2 "The CSC? Now, that's a hell of a question. I figured you were going to ask me how to Mega Evolve that Steelix of yours."
    byron -surprised @norm2 "But, sure, I can tell you about the CSC. They're a big transportation and logistics company based out of Sinnoh. I shouldn't have to tell you what port."
    byron @norm2 "They were responsible for transporting most of the ore out of Iron Island, before my folks turned it into a nature preserve."
    byron @norm4 "They focus more on shipping manufactured goods, now. You know Unova's bridges, the ones they're so proud of? The parts were shipped using Sinnohan freighters."

    show jasmine surprisedbrow frownmouth with dis

    byron @happy2 "It's a good company. They move what they say they will, at the speeds they say they should, and don't let anything slow 'em down. That's why I bought them out."

    jasmine @talking2mouth "Instructor Byron--do you mean that you own the company?"

    byron @norm2 "I'm the majority shareholder. I've just told them to keep doing exactly what they're doing, though."

    show jasmine -surprisedbrow frownmouth with dis

    byron @norm4 "Frankly, they didn't need me, and I didn't need them, but I was worried some young kid with 'big ideas' about revolutionizing the shipping industry would buy them out if I didn't."
    byron @angry2 "Not worth the hassle. Easier to just set up a big wall of cash to block anyone trying that."
    byron norm3 @sad2 "That's one thing all this money is good for, I guess."

    redmind @unamusedbrow unamusedmouth "If you have too much, I am {i}more{/i} than happy to take it off your hands."

    jasmine @sad2brow talkingmouth "Well... that makes this a bit awkward, but..."

    show byron surprised with dis

    jasmine angrybrow @angrybrow talking2mouth "Instructor Byron. I am confident the Canalave Shipping Company is practicing some sort of dirty business."

    pause 2.0

    show jasmine surprisedbrow with dis

    byron -surprised @happy2 "Nah, that's ridiculous."
    byron @norm2 "Go on, kids, you'll be late for you next classes."

    jasmine sadbrow @talking2mouth "How can you dismiss me so easily?"

    byron @norm2 "Because this isn't my first rodeo. Y'know how many environmental lawyers it took to clean up Iron Island?"
    byron norm3 @norm4 "Of course I had 'em check out the CSC. I wouldn't buy the kind of company that turned my pops' lungs black."
    byron @norm4 "But not even the {i}lawyers{/i} could find something to complain about. The CSC do their work quietly, professionally, boringly, and cleanly."
    byron @norm4 "If they were engaged in some sort of dirty business, I'd know about it, and I'd have shut it down already."

    jasmine @sadbrow talkingmouth "Instructor, I'm telling you now, I {i}saw{/i} it!"

    byron "[ellipses]"
    byron @norm4 "What did you see?"

    jasmine @talking2mouth "They were pouring some sort of clear liquid off the top of the deck. And when I asked them what it was, they tried to mislead me, and said it was ballast, or... or... just soapy water!"

    byron @norm4 "I'm not seeing it, kid. This 'dirty business' is... pouring water into the harbor?"

    jasmine angrybrow @talking2mouth "I'm certain it wasn't {i}just{/i} that. You remember what I said about Olivine, right? Your own parents were miners--you know what sort of contaminants could get into the harbor!"

    byron @norm4 "I'm sorry, Jasmine, but I can't do anything with this. What would I even do with this information? Call up the CEO and ask him if his sailors are pouring... I don't know, {i}vodka{/i} into the water?"
    byron @norm4 "You said yourself that it's a clear liquid. Let me tell you that the kind of liquids I'd be worried about are brown, or black, if coal's involved."

    jasmine "[ellipses]"

    byron sad @sad2 "You're a good girl, Jasmine. A great student, and a fun kid to have in my class. But I can't start raising hell because you thought you saw some transparent liquid fall off the top of {i}one{/i} ship."

    pause 1.0

    byron @sad2 "[first_name], did you see anything?"

    red @sad2eyes sadeyebrows frownmouth "[ellipses]"

    byron norm3 @norm4 "Well, that's all I can do for you, without any real proof, then."

    pause 1.0

    show byron surprised with dis

    jasmine -angrybrow @closedbrow sweat talking2mouth "I... have a sample of the liquid."

    byron @surprised2 "You do? Why didn't you start with that?"

    jasmine "[ellipses]"

    byron angry @angry2 "Wait. Where'd you get it from?"

    jasmine @sad2brow "[ellipses]"

    byron @angry2 "Oh, damn it to hell. You went too far. You jumped in the water for it, didn't you? That's why you were shivering up a storm and looked like death for a while."
    byron @angry2 "I visited you in the damn infirmary. I put my shovel down so Miriam would let me in. I told you to take care of yourself, and you said you were."
    byron @angry2 "You're telling me I did all that, and you jumped in the freezing harbor so you could get a sample of some water, on the off-chance it had some sort of poison in it?"

    jasmine @angrybrow talking2mouth "Instructor Byron, I know I'm right about this! You have the ability to test water for poisons and contaminants, don't you? Please, just test the sample I have, and you'll see I'm right."

    byron @angry2 "I'm not going to do one single part of that. You want me to reward you for gambling with your health?"
    byron @angry2 "You're a student. Both of you are. You should be focusing on keeping your head down, studying hard, training your Pokémon, and staying safe."
    byron @sad2 "Jasmine, you've got a great future ahead of you. Don't waste it by doing reckless stuff like jumping in the water, trying to play hero."
    byron norm @norm2 "Mind your own business, keep your eyes on the ground, and everything will be fine. Don't worry about what came off that ship--it'll distract you from what's {i}really{/i} important, which is {i}your{/i} health, and {i}your{/i} success."

    pause 1.0

    show byron surprised with dis

    jasmine shadow angrybrow @talking2mouth "You said, not ten minutes ago, that if I had something to do, I should stand up straight and do it."

    pause 1.0

    byron sad @sad2 "Look. That was more general advice. It's not--"

    jasmine tears @talking2mouth "It's not for everyone."
    jasmine @talking2mouth "It's not for those who {i}can't do it.{/i}"

    show jasmine sadbrow -shadow tears2
    show byron surprised
    with dis

    jasmine @sadmouth "Is that--Is that what you were going to say?"

    byron @surprised2 "N-no! No, it's just... you should..."
    byron sad @sad2 "You should pick and choose your battles. You're dealing with more than enough already."

    jasmine -tears2 cry "[ellipses]"
    jasmine @talking2mouth "I have never chosen a battle for myself. There have only been battles thrust upon me. Now, there is {i}one{/i} war I {i}wish{/i} to prosecute."
    jasmine angrybrow talking2mouth "And I will not take one single step back until I have won."

    hide jasmine with dis

    pause 2.0

    byron @sad2 "{size=30}Damn it all.{/size}"

    red tears @sadbrow frownmouth "[ellipses]"

    byron @sad2 "You got no reason to be here anymore, kid. Go on."

    pause 1.0

    red @talking2mouth "She's telling the truth, you know."

    byron @norm4 "Yeah. I know this isn't over. And I know she thinks she's doing the right thing, but... damn it."
    byron @sad2 "Why can't she just keep herself safe?"

    red @talking2mouth "She wants to help other people. You can't do that cowering behind your own shield."

    byron sad @sad2 "...Hell. Wish she would, though. If she's exposing herself to shield everyone else, who'll [bluecolor]shield{/color} her?"

    hide byron with dis

    pause 2.0

    redmind @angrybrow frownmouth "I will."

    $ RelationshipRankUp("Jasmine", "Shield", 2)

return 