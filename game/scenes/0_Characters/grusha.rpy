label Grusha1:
    $ location = "city"

    scene city_B 
    show grusha scarf
    with Dissolve(2.0)
    queue music "audio/music/montenevera_start.ogg" noloop
    queue music "audio/music/montenevera_loop.ogg"

    narrator "You're walking through Inspira, near a part of the city you do not normally go to, when you see a familiar figure. You're about to call out to him, when..."

    show grusha sad2eyes angryeyebrows with dis

    pause 0.5

    show grusha playfuleyes with dis

    pause 0.5

    show grusha angrybrow shadow with dis:
        xzoom 1
        ease 0.5 xzoom -1

    pause 1.0

    show grusha:
        alpha 1.0 xpos 0.5 xzoom -1
        ease 0.3 xpos 1.0 alpha 0.0

    pause 1.0

    hide grusha

    redmind @thonk "Huh? That was... really weird. What did Grusha look so suspicious for?"

    narrator "You decide to follow Grusha at a distance."

    scene blank2 with splitfade

    narrator "For a second, you're worried he's going to walk down the alleyway leading to Silver's shack, but he passes that alley as he moves further into the outskirts of the city... stopping by a convenience store."

    scene seveneleven with splitfade

    red @surprised "Wait. That's--!"

    narrator "You quickly duck behind a dumpster, peeking your head out around the corner as a large, thuggish, man walks up to Grusha with obvious familiarity."

    stop music fadeout 1.5
    queue music "audio/music/potown_start.ogg" noloop
    queue music "audio/music/potown_loop.ogg"

    scene sevenelevenside
    show grusha unamusedbrow:
        xpos 0.33
    show roughneck:
        xpos 0.66
    with splitfade

    grusha "{i}Finalmente.{/i} Let's get this done."

    roughneck @happy "Heh. The boss told me you were a fiend for this stuff, but it's really something else, seein' it in person. Seeing the mighty 'Sub-Zero Shredder' behind some big city gas station... how the mighty have fallen."

    grusha @sad2eyes "Snow isn't always a soft landing."
    grusha -unamusedbrow @closedbrow "Whatever. I didn't come out here to be judged. I've got the money. Just hand over our regular deal."

    roughneck @talkingmouth "Don't know about that one. Boss is raisin' the prices."

    grusha @angry "What?"

    roughneck @angrybrow talking2mouth "C'mon, where else would you go for this stuff? You know we're the sole producers. We can charge anythin' we want."

    grusha @closedbrow talking2mouth "I've spent too much on this already... Jasmine's getting suspicious."

    roughneck @closedbrow talkingmouth "I don't care about your lady troubles, I care about makin' the boss happy, and the boss is only happy if he gets paid."

    grusha @wince "I... fine. What's your price? I can't do more than $250."

    roughneck @talkingmouth "You'll do what we tell you to do. And boss isn't raisin' the prices like that."

    grusha @surprised "What?"

    roughneck @talkingmouth "He ain't chargin' more money. He wants you to do something for us."

    grusha @angrybrow talking2mouth "[ellipses]{i}¿Qué?{/i}"

    show grusha surprisedbrow with dis

    roughneck @happy "You want any more, you need to start promoting it." 

    grusha "Wait, you mean--"

    roughneck @talkingmouth "We got the Sub-Zero Shredder drinking out of our cups. Word gets out, we'll be the talk of the town. Biggest business on the block."
    roughneck @happy "Besides, you got a pretty face. Bet you've done this kinda stuff before."

    grusha angrybrow shadow "[ellipses]"
    grusha @talkingmouth "I want to talk directly to your boss."

    roughneck @surprised "Eh? Alright, but you know how he gets. Go in a room with him, you might not be coming out."

    grusha @closedbrow "I can handle myself."

    roughneck @talkingmouth "Yeah, alright."
    roughneck @closedbrow talking2mouth "Boss clocks in at night. Past eight. Come then."

    grusha @talkingmouth "I've got curfew at eight."

    roughneck @surprised "What are you, a kid? Sneak out."

    grusha @sad2eyes "[ellipses]"

    roughneck @angrybrow happymouth "Boss'll be waiting for you. Don't wait too long to visit. I know you can't go without this stuff for more'n a week."
    roughneck @talkingmouth "Oh, yeah. We don't want people recognizing you while we're, uh, 'onboarding' you. Put on something other than that big coat you always wear. Something you won't be recognized in."

    hide roughneck with dis

    pause 1.0

    grusha furiousbrow "{i}¡Mierda!{/i}"

    pause 0.5

    grusha @sad2brow "What did I get myself into...? Maybe I shouldn't... I mean, I've taken so much already, and I know it's bad for me, but..."
    grusha sad2brow noshine "...But I don't have a choice, huh?"

    $ AddEvent("Grusha", "Scene1Part1")

    hide grusha with dis

    narrator "Grusha walks away, head hung in defeat, as you're left reeling at the massive implications of what you've just heard."
    narrator "You decide to sneak out at night at some point and follow Grusha, so you can keep an eye on him."
    narrator "[bluecolor]The next time you are able to text someone, if you elect not to, you can instead sneak out and follow Grusha."

    if sceneviewer:
        return

    $ renpy.pop_call()
    jump freeroam

label Grusha1Part2:
    $ AddEvent("Grusha", "Grusha1Part2")
    stop music fadeout 1.5
    queue music "audio/music/potown_start.ogg" noloop
    queue music "audio/music/potown_loop.ogg"

    scene blank2 with splitfade

    narrator "You quickly change back into your regular clothes, and prepare to sneak out into the city."

    scene nightmap with splitfade

    redmind night @thinking "Sorry, Skyla, Silver. Gotta break the rules a little bit. Grusha might be in some serious trouble here."

    narrator "You sneak off-campus without incident, and eventually find your way back to the convenience store you saw Grusha outside of." 

    scene sevenelevennight with splitfade

    $ location = "city"

    narrator "However, he doesn't appear to be here. The only other person near the gas station is a tired-looking teen pumping gas into her car."

    redmind night @sad2brow frownmouth "Oh, man... I'm getting really nervous. What will I even say when I see him?"
    redmind @thinking "'Hey, I stalked you a while ago, and I'm pretty sure that you're involved with some sort of criminal gang, possibly run by Silver, and I'm worried about you, so could you, like, stop?'"
    redmind @upeyes angryeyebrows frownmouth "...Yeah, that doesn't seem like the play, but I can't figure out anything better. I'll just say the first thing that comes to mind when I see him."

    show grusha unamusedbrow frownmouth uniformf noscarf at night with dis:
        xpos 0.0
        ease 0.7 xpos 0.5 

    grusha @talking2mouth "[first_name]? What are you doing here?"

    show sevenelevennight 
    show grusha surprisedbrow 
    with vpunch

    stop music fadeout 1.5

    red @surprised lightblush "GRUSHA?! You're a {i}woman?!{/i}"

    pause 1.0

    grusha -surprisedbrow @unamusedbrow talking2mouth "No. No, I am not."

    red @wince talking2mouth "Oh."

    queue music "audio/music/montenevera_start.ogg" noloop
    queue music "audio/music/montenevera_loop.ogg"

    pause 1.0

    red @talkingmouth sweat "But, uh, the skirt...?"

    grusha -frownmouth @talkingmouth "Breezy, lightweight, and fun to spin in."

    red @sad2brow talkingmouth "Okay, but the tights...?"

    grusha frownmouth unamusedbrow @closedbrow talking2mouth "It's cold out. What do you want me to say, [first_name]? Yes, I'm wearing the women's uniform. I'm a man. That's the end of it."

    red @talkingmouth "I... yeah, no, I guess I don't have anything else to say about that. Sorry, I was just surprised."

    grusha @closedbrow talking2mouth "It's nothing. But {i}my{/i} question was what are you doing here?"

    red @surprisedbrow talking2mouth "Oh. Right."

    show grusha frownmouth sad2brow with dis

    red @closedbrow talking2mouth "Look, I... uh... I heard you talking with that tough-looking guy a while ago."

    grusha @talking2mouth "...Okay."

    red @sadbrow talking2mouth "It sounds like they were forcing you to do something you weren't really comfortable with in order to get something you needed. It sounded like they were asking you to sell something..."

    grusha @closedbrow talking2mouth "It's fine. I've done it before. I'm pretty used to it by now."
    grusha @sad2brow talking2mouth "Besides. I don't have a choice. I need what they're giving me. So that means if I have to plaster on a smile and take my classmates' money as I sell them poison, then..."

    red @angrybrow talking2mouth "Grusha, I don't know what's going on here, but I'm pretty sure you're making a big mistake."

    grusha -sad2brow @closedbrow talking2mouth "Whatever. I didn't come out here to be judged."

    red @talking2mouth "Grusha, for your own safety, and the safety of my classmates, I need you to leave this gas station, and not come back."

    grusha @confusedbrow frownmouth "[ellipses]"
    grusha @confusedeyebrows talking2mouth "Now, why {i}en el diablo{/i} would I do that?"

    red @talking2mouth "You know this isn't good for you."

    grusha @talkingmouth "True."

    red @talking2mouth "And you know it's not good for our classmates."

    grusha @sad2brow talkingmouth "True, but I care less about that."

    red @angrybrow frownmouth "[ellipses]"

    show grusha surprisedbrow frownmouth with dis

    red @talking2mouth angrybrow "What would Jasmine say?"

    pause 1.5

    grusha @angrybrow shadow talking2mouth "How dare you?"
    grusha angrybrow frownmouth @angry "Leave, now."

    red @talking2mouth "I'll leave with you. Not alone."

    pause 1.0

    grusha @talking2mouth "Then get out your Poké Balls. We'll settle this. Single battle. Even if you're on the Battle Team, I'm a pretty tough trainer myself."

    red @talking2mouth "Fine. And if I win, you come back to the school with me?"

    grusha @talking2mouth "And if I win, you go back to the school alone, and don't bother me anymore."

    red @angrybrow talking2mouth "Fine."

    grusha closedbrow talking2mouth "Don't make this exciting."

    python:
        trainer1 = MakeRed()
        trainer2 = MakeTrainer("Grusha")

    call Battle([trainer1, trainer2], customoutfits=["", "uniformf noscarf"]) from _call_Battle_169
    $ RecordBattle("Grusha2")

    if (WonBattle("Grusha2")):
        show grusha surprisedbrow frownmouth uniformf noscarf with dis
        
        grusha @surprisedbrow talking2mouth "You're... tougher than I thought."
        
        queue music "audio/music/montenevera_start.ogg" noloop
        queue music "audio/music/montenevera_loop.ogg"

        red @talkingmouth "I was fighting for something important."

        grusha -surprisedbrow @closedbrow talking2mouth "You can say that with a straight face?"

        red @talkingmouth sadbrow "You're important, man."

        grusha unamusedbrow @sad2brow talking2mouth "Ugh..."

        $ ValueChange("Grusha", 3)

    else:
        show grusha unamusedbrow frownmouth uniformf noscarf with dis

        pause 1.0
        
        queue music "audio/music/montenevera_start.ogg" noloop
        queue music "audio/music/montenevera_loop.ogg"

        grusha @talking2mouth "Well... I guess I asked you not to make it exciting."

    grusha @closedbrow talking2mouth "I just don't get why you even care so much."
    grusha @talking2mouth "It's just a little fun, alright? I don't have a lot left. Do you really need to get on my ass for this?"

    show grusha surprisedbrow frownmouth with dis

    red @angrybrow talking2mouth "A little fun?! Grusha, you're ruining your life! They want you to ruin other peoples' lives!"

    pause 1.5

    grusha @confusedbrow talking2mouth "Okay. I was cool just blowing you off, before, but now I've gotta question--what exactly do you think I'm doing here?"

    red @surprisedbrow frownmouth "[ellipses]"
    red @sad2brow lightblush talking2mouth "Uh... I definitely know exactly what you're doing, so why don't you just tell me, so I know we're on the same page?"

    grusha smirkmouth -surprisedbrow @closedbrow talkingmouth "Tch. Aren't you nosy?"
    grusha @talking2mouth "Come with me."

    if (WonBattle("Grusha2")):
        red @talkingmouth "Woah, hey. I won our battle. That means {i}you{/i} come with me."
        
        grusha @closedbrow talking2mouth "Just do it, {i}amigo.{/i} You're barking up the wrong tree, okay? Let me show you what's really going on."

        red @closedbrow talking2mouth "...Fine. But just remember that I beat you in a battle."

        grusha @upeyes talking2mouth "Yeah, yeah, I know. Don't worry,{w=0.5} you're {i}very{/i} scary."

    else:
        red @talkingmouth "Wait, hold on. Didn't you want me to go back to school?"

        grusha @talkingmouth "Yeah, changed my mind. You're barking up the wrong tree, okay? Let me show you what's really going on."

        red @closedbrow talking2mouth "Fine. But, even without my Pokémon, I'm going to try and help you here."

        pause 1.0

        grusha @upeyes talking2mouth "My hero."

    scene seveneleveninside with splitfade

    red @confused "What are we doing inside?"

    show grusha uniformf noscarf 

    grusha @talkingmouth "Whatever you want. Grab a bag of doughnuts. Or... you seem more like an energy drink guy? Whatever you want, I'll pay."

    redmind @thinking "He's totally got me pegged..."

    pause 1.0

    redmind @sad2eyes sadeyebrows frownmouth lightblush "Maybe a bad choice of words. Don't think about pegging."

    red @closedbrow talking2mouth "I'll, uh, pass."

    grusha @closedbrow talkingmouth "You're really suspicious, you know that?"

    red @confused "I think it's less that I'm suspicious and more that you're acting suspiciously."

    grusha @closedbrow talking2mouth "We can point fingers all we want. But I don't want to, so let's stop."

    red @angrybrow talking2mouth "Hey-"

    grusha @talkingmouth "Hey, Manager. I'm here."

    show grusha:
        xpos 0.5 
        ease 0.5 xpos 0.66 
    show oldman blush alcohol:
        xzoom -1 xpos 0.33
    with dis

    oldman @happy "Ah, so you are. How good to--{w=0.5}{nw}"
    extend @surprisedbrow frownmouth "What are you wearing?"

    grusha @closedbrow talking2mouth "Figured a sneaky wino like you might try to snap some pictures of me before I agreed to anything. Hope this doesn't ruin any plans you had."

    oldman @angrybrow frownmouth "[ellipses]"
    oldman @happy "No, of course not! I wouldn't try to take any pictures or... eh-heh... anything like that before you agreed."

    pause 1.0

    oldman @talkingmouth "Who's you're friend? I don't think I've ever seen you with someone beyond that tall girl. I figured you'd be coming alone?"

    grusha @talkingmouth "So did I. This is [first_name]. He's in the Kobukan Battle Team."

    red @confused "I am also in a state of confusion."

    grusha @talkingmouth "Mm. Guess I've had my fun, now. Manager, why don't you tell my friend here what you want with me? I'll be by the Slurpz."

    hide grusha with dis

    pause 1.0

    red @talkingmouth "Uh, hi. You look familiar."

    oldman @happy "Oh, I've just got one of those faces."

    show oldman surprisedbrow frownmouth with dis

    red @closedbrow talking2mouth "So, uh, like Grusha said, I'm... kinda incredibly lost here. I thought you were, um, withholding some kind of vital medicine from him? Or asking him to sell something suspicious to other Kobukan students?"

    pause 1.0

    oldman @talkingmouth "Young man, why would my humble convenience store have anything approximating vital medicine?"

    red @sad2eyes sadeyebrows talking2mouth lightblush "{size=30}I also kinda thought it might have been drugs...{/size}"

    oldman -surprisedbrow @happy "Ah, well, what the part-timers do on their lunch breaks is none of my business. But no, I promise, I'm not trying to do anything malicious to the legendary Sub-Zero Shredder. Quite the opposite, in fact!"

    redmind @thonk "Sub-Zero Shredder..."

    show gym at sepia:
        subpixel True
    show flashback
    with dis

    pause 0.5

    show grusha uniform at sepia with dis

    grusha @talkingmouth "Yeah. 'The Sub-zero Shredder.' From Montenevera, in North Paldea.{w=0.5}{nw}" 
    extend @sadbrow talking2mouth " ...Glaseado Mountain, actually, but the post came to Montenevera."

    show blank with splitfade

    hide flashback
    hide gym
    hide blank
    hide grusha 
    with dis

    pause 1.0

    red @talkingmouth "I've heard that name before. That's Grusha?"

    oldman @talkingmouth "Of course! And he'll always be. He's a famous snowboarder, you know? The best in Paldea--some would say the world!" 
    oldman @happy "Grusha Golondrina, the Maestro of Montenevera, the Prince of the Peaks, the Sub-Zero Shredder, the Commander of Cold, the Tsar of Tsnow, the--"

    show grusha frownmouth uniformf noscarf with dis:
        xpos 0.66

    grusha @unamusedbrow talking2mouth "Stop, you're making me blush."

    pause 1.0

    narrator "Grusha takes a long sip of some sort of blended ice drink. It says 'Slurpz' on the side."

    grusha @lightblush talking2mouth sad2brow "Crazy part is, he didn't even make any of those titles up. People actually called me that."

    oldman @angrybrow talkingmouth "And people'll call you that again, Shredder! Why, my own grandson, a student at Naranjuva, thinks you're just moments away from returning to the spotlight."

    grusha @talking2mouth "Your grandson's going to be disappointed."

    pause 1.0

    oldman @talkingmouth "Well... [first_name], was it? The Sub-Zero Shredder was famous for two things. The first was how he barely touched the snow when he boarded. It was like he was flying--like the board was a pair of wings."

    grusha @closedbrow talking2mouth "Felt like it, too."

    oldman @happy "And the second thing he was famous for was his consumption of Slurpz! Which we are proud to sell at this location, by the way. The only sellers in Inspira, in fact!"

    grusha @talkingmouth "Yeah, they were a lot more common in Paldea."
    grusha @talkingmouth "Basically flavored ice. Sugar, a little fruit juice, some sugary flavoring, some artificial fruit juice, and a pinch of sugar to wash it all down."
    grusha @sad2brow talking2mouth "This stuff is bad for me... but damn, if I can't live without it. Used to down one before every race, every trial, every competition."

    redmind @surprisedbrow frownmouth "Wait... so when I heard him say he can't live without it before, he was just..."

    pause 0.5 

    redmind @unamusedbrow unamusedmouth "He was just exaggerating. And I took him seriously."

    pause 1.0

    redmind @poutmouth sad2eyes angryeyebrows "In my defense, his humor is very dry. It's hard to tell if he's joking or not!"

    grusha @closedbrow talking2mouth "Used to be a lot easier to burn off the calories from this stuff, though. Back when I boarded."

    red @talkingmouth "So you two know each other because..."

    grusha @closedbrow talking2mouth "I come here to get my Slurpz fix. Manager here's a fan of mine. He gave me a good deal on bulk purchases."
    grusha @angrybrow talking2mouth "...He {i}gave{/i} me a good deal, emphasis mine. You've told him what you're asking me to do now, right, Manager?"

    oldman @sadbrow talking2mouth "Well... the Sub-Zero Shredder coming to {i}my{/i} store for his Slurpz fix is something pretty special, you know? I'd like to capitalize on that." 
    oldman @happy "Maybe take a couple pictures, shoot an advertisement for a poster--I've got an in-law who works at a print shop."

    grusha @sad2brow talking2mouth "Personally, I'd rather he just charged me more money."

    oldman sadbrow frownmouth @angrybrow happymouth "Think about it, Shredder! You've got fans all over the world who are clamoring for your return. Maybe..."

    narrator "The old manager's eyes linger on Grusha's scar, now prominently visible."

    oldman -sadbrow -frownmouth @talkingmouth "Maybe you can't return to the slopes, maybe you can't get back on the board, but a small, low-commitment promotional advertisement like this could be a way to get a foot back in the game!"

    grusha @talking2mouth "...What game? People wanted to see me board. I can't do that anymore. I've got nothing left for anyone. Game Over."

    oldman @sadbrow talkingmouth "People didn't just want to see you board. They wanted to see {i}you{/i}. They wanted to see you fly. They loved watching you battle, they loved watching you talk, they loved watching you pose and sing and commentate..."
    oldman @happy "Why, you could return to that scene any moment you wanted! You could become a commentator! A celebrity judge!"

    grusha @closedbrow frownmouth "[ellipses]"
    grusha @closedeyes angryeyebrows talking2mouth "I don't..."

    show oldman sadbrow frownmouth with dis

    grusha tears @sad2eyes sadeyebrows talking2mouth  "I don't want to watch people doing something I can't anymore. {size=30}I can't do that.{/size}"

    pause 1.0

    grusha -tears @closedbrow talking2mouth "I can't do your promotional campaign, manager. It wouldn't help you, anyway. Nobody knows who I{w=0.5}--remembers who I was."
    grusha @talking2mouth sad2brow "Grab some other twink to smile and pose with your sugar concentrates. Kobukan's full of them."

    oldman @closedbrow talking2mouth "...Grusha, you have fans. Still. I'm one of them."

    grusha surprisedbrow frownmouth @sad2eyes angryeyebrows talking2mouth "Yeah? And how old are you? You've probably got less time to live than I do."

    red @angrybrow talking2mouth "Grusha!"

    grusha @sad2eyes sadeyebrows talking2mouth "I... I'm sorry. I shouldn't have--"

    hide grusha with dis

    pause 1.0

    oldman @closedbrow talking2mouth "Oh... that poor, troubled, boy."
    oldman @sadbrow talkingmouth "Please excuse that slip of his, [first_name]. He's normally very friendly and outgoing."

    red @confused "We're talking about the same guy?"

    if (IsBefore(22, 1, 2005)):
        oldman @talkingmouth "For most of his life, he was exactly as I said. He earned his title, 'Little Prince.' He's a young man. Only nineteen."
        oldman @closedbrow talking2mouth "...That terrible accident on Montenevera changed everything."
    else:
        oldman @talkingmouth "For most of his life, he was exactly as I said. He earned his title, 'Little Prince.' He's a young man. Only twenty."
        oldman @closedbrow talking2mouth "...That terrible accident on Montenevera changed everything."

    red @sadbrow talking2mouth "What terrible accident?"

    oldman @closedbrow "Oh... I shouldn't say. Besides, the one who can tell you best--"

    narrator "The Old Manager nods towards Grusha's retreating form, skirt flapping in the cold night wind."

    oldman @talkingmouth "--left his Slurpz behind."

    red @sadbrow frownmouth "[ellipses]"

    oldman @talkingmouth "Go on, then. And if he seems to be in a better mood, maybe raise the poster idea again?"

    red @sadbrow talkingmouth "I'll see what I can do."

    scene blank2 with splitfade

    pause 0.5

    narrator "You follow Grusha, and quickly catch up to him, noticing that his pace is slower than you might have thought. You hand him back his Slurpz... which he accepts without a word."

    scene seaportnight with splitfade

    $ location = "seaport"

    pause 0.5

    show grusha uniformf noscarf at night with Dissolve(1.0)

    pause 0.5

    grusha @talking2mouth "You're following me again."

    red night @sadbrow talkingmouth "Guess it's a bad habit of mine."

    grusha @closedbrow talking2mouth "Tch."

    pause 1.0

    grusha @sad2brow talking2mouth "I was such a dick. I need to go back and apologize to the Manager. I can't believe I said that crap to him..."

    pause 0.5

    red @talking2mouth sadbrow "I don't think apologizing would hurt. But he doesn't hold it against you."

    grusha @closedbrow talking2mouth "He told you that?"

    red @talking2mouth "More or less. He mentioned an accident on Montenevera."

    grusha @talking2mouth "...Yeah."

    $ grushacetoddleobj = GetTrainerTeam("Grusha", "Cetoddle")
    $ monname = pokedexlookup(grushacetoddleobj.GetId(), DexMacros.Name)
    $ DisplayPokemon(monname)

    if (grushacetoddleobj.Id == 974):
        grusha @talking2mouth "This little lady."

    else:
        grusha @talking2mouth "This big girl."

    red @confused "Your [monname] was the accident?"

    $ HidePokemon()

    grusha @closedbrow talking2mouth "I was at the end of a race. Not a big one. Had a solid... ten or so meters between myself and the guy behind me. Carlos, I think."
    grusha @sad2brow talking2mouth "And then this little lady walked onto the course. I swerved, and..."

    hide sideportraitfull

    pause 0.5

    grusha @closedbrow talking2mouth "They say you should never swerve. Boarding, driving, skiing. 'Don't swerve.'" 
    grusha @sadbrow talking2mouth "They say that if you need to put yourself in danger to save someone else, just {i}don't{/i}, because there's a chance you'll end up putting yourself {i}and{/i} the original person in danger. I didn't think about that, though."

    pause 0.5

    grusha @talking2mouth "I swerved. My feet flew out from under me, my boots unlocked from the board, the board got stuck in the snow and snapped..."
    grusha @shadow sad2eyes noshine talking2mouth "And the next thing I was conscious of was my own snowboard sticking out through my chest while my jacket turned red."

    pause 0.5

    grusha sad2brow @closedbrow talkingmouth "Huh. It's funny the things that go through your mind in moments like that. I remembered thinking the red looked like my mother's gazpacho."

    pause 0.5 

    grusha @talking2mouth "I expected to die. I whispered a prayer to Arceus. I asked that my friends, my family, the people I left behind could find their peace."

    pause 1.0

    grusha @unamusedbrow talking2mouth "I didn't ask Him to save me."
    grusha -sad2brow @closedbrow talking2mouth "But I guess that's on me for not being specific enough."

    red @talking2mouth "So... you caught the [monname]?"

    if (monname == "Cetitan"):
        grusha @talking2mouth "She was a Cetoddle at the time, but yeah."

    grusha @sad2brow talking2mouth "Apparently, she refused to leave my side. Did you know Pokémon can feel guilty? I didn't."
    grusha @closedbrow happymouth "Hah, the hospital wanted to give me a therapy Pokémon, but the Cetoddle would keep fighting them off. They eventually decided to just leave me with her."

    pause 0.5

    grusha @sad2brow talking2mouth "I... wasn't thrilled about that, at first. But I've gotten more comfortable with her now. I mean, accidents happen." 
    grusha @sad2brow talkingmouth "I saw some other boarders--well, ice is dangerous, even when you're not racing down it at one hundred and fifty kilometers per hour."

    pause 1.5

    grusha unamusedbrow @talking2mouth "There. That's my story. That's literally everything you might want to know about me. I've got nothing else to tell you. So fly off."

    pause 1.0

    red @sad2brow talking2mouth "You wanted to tell me that story."

    grusha @closedbrow talking2mouth "Not you, {i}specifically{/i}."

    red @talking2mouth "But you did want to tell someone. You feel alone."

    grusha @talking2mouth "I {i}am{/i} alone, and that's how I should be. I was told I could die within the week after the accident. Every day is a miracle. And I'm the only one who won't have to deal with the consequences when those miracles run out."
    grusha @talkingmouth sad2brow "I screwed up by getting close to Jasmine. But, c'mon, it's impossible to push her away. That woman doesn't take a single step in any direction other than the one she wants to."

    $ ValueChange("Jasmine", 3, -0.5)

    narrator "Your understanding of Jasmine increased!"

    red @talking2mouth "...You seemed pretty close with that store's manager. You even wanted to apologize to him."

    grusha @talking2mouth "Yeah, well, I'm not a robot. I'm just... spinning my wheels until I run out of oil, I guess."

    red @thinking "[ellipses]"
    red @talkingmouth "So you're still making friends. Even if you don't want to. You're still keeping up your Slurpz routine. You're still wearing fun clothes--and I don't buy for a second you did it {i}just{/i} to ruin any pictures the manager might take."
    red @sadbrow talkingmouth "That doesn't sound like the behavior of someone who hates life."

    grusha -unamusedbrow @talking2mouth "I don't."
    grusha @sad2brow talking2mouth "I don't hate life, {i}amigo.{/i} I love it. I love every breath of fresh air I get to have. I love every smile I see. I love every gram of sugar I can drink."
    grusha @closedbrow tears2 talking2mouth "I--{w=0.5} I {i}love{/i} every single part of life. And I {i}used to{/i} live it. This torn-up heart isn't what's killing me. My inability to {i}live{/i} is what's killing me."

    pause 0.5

    red @talking2mouth "Grusha... you {i}are{/i} living."

    grusha @confused "Yeah? I used to fly down mountains. I could raise my fist and thousands would cheer. There was a group of fans that would come to most of my races, and {i}every time{/i} they had my name painted on their stomachs." 
    grusha @sadbrow happymouth "All sixteen letters, one for each of them. The second 'o' was the sexiest woman I'd ever seen."
    grusha @sad2brow talking2mouth "That was living, [first_name]. What I've got now is just... {w=0.5}waiting."

    pause 1.0

    grusha @talkingmouth sadbrow "I had something to live for. Now, I'm alive, but... I don't."

    pause 1.0

    show grusha:
        ypos 1.0
        ease 0.5 ypos 1.2

    narrator "Grusha sits down on the dock, staring down at the black water. The air is filled with nothing but the quiet sound of lapping waves... and the occasional sniffle emanating from Grusha's direction."

    grusha sad2brow @talking2mouth "If you're not going to leave, then sit here with me. I'm not supposed to stand for too long. I should sit before I go back to campus."

    show grusha:
        ypos 1.2 zoom 1.0
        ease 0.5 zoom 1.3 ypos 1.2

    pause 1.5

    grusha @closedbrow talking2mouth "{i}Maldita sea{/i}. I was trying so hard not to fall under your spell."

    if (GetRelationshipRank("Jasmine") > 0):
        grusha @talking2mouth "When Jasmine told me about you... I told myself I wouldn't end up like her, spilling my guts out and caring what you think."

        grusha @upeyes talking2mouth "Now look at me. I'm even at the same dock."

    red @sadbrow talking2mouth "Frienergy, I guess."

    grusha @closedbrow talking2mouth "Maybe. But I knew you were a good person from the start. The exact kind that could make me crack. I should've tried harder to push you away."

    pause 1.0

    red @sadbrow talkingmouth "It's not too late. It's never too late. For anything."

    grusha @sad2brow talking2mouth "...Pretty sure it's too late to become the world's best weightlifter."

    red @talking2mouth "Grusha, if that's what you decide you want to live for, then it isn't."

    grusha -sad2brow @talking2mouth "You make it sound so easy. Just 'decide' what to live for. You don't have any idea what you're talking about."

    red @talkingmouth "I don't pretend to understand what you're going through. But I know what it's like to pick something to live for, and just do it. I decided, one day, I wanted to be a Champion. And that's been my life ever since."

    grusha @talking2mouth "Yeah? And what if you caught Nuzlocke? What if you couldn't use Pokémon anymore, without them dying?"

    red @sadbrow talkingmouth "I'd pick a new thing to live for."

    grusha @upeyes talking2mouth "Ugh. Talking to you is like trying to tell a Fidough it's already had dinner. Do you ever give it up?"

    pause 1.0

    grusha smirkmouth sad2brow @upeyes talkingmouth "Nevermind. Dumb question."

    pause 1.5

    grusha @talkingmouth "I... wish I had your heart. I feel like yours could break and keep going. Maybe things would be fine that way."

    red @sadbrow talkingmouth "Respectfully, I'm not sure we're close enough to consider swapping hearts yet."

    grusha @closedbrow talking2mouth "I was known to be quite a heartbreaker, back when I was the Shredder. Second O can attest to that."
    grusha @sadbrow talkingmouth "Guess this is karma."

    pause 1.5

    grusha @talking2mouth "Alright. Enough moping for today. I've fulfilled my quota. Ready to head back to... {w=0.5}{nw}"
    extend confusedbrow frownmouth "hm?"

    red @confused "What is it?"

    narrator "Grusha reaches his hands out to the water, where some ovaloid object just bumped into his foot."

    red @surprised "Woah, careful, don't fall in!"

    grusha -confusedbrow -frownmouth @closedbrow talking2mouth "I'm not going to drown."

    pause 1.0

    show grusha:
        ypos 1.2 zoom 1.3
        ease 0.5 ypos 1.0 zoom 1.0

    grusha @talkingmouth "It's... huh?"
    grusha @confused "I thought it was a Tentacool at first, but...?"

    $ DisplayGetItem("Manaphy Egg")

    narrator "You immediately recognize what it is."

    red @happy "Hey, that's a Phione egg!"

    grusha @talkingmouth "{i}¿Qué?{/i}"

    red @talkingmouth "They're a pretty rare Pokémon. Mostly seen in warmer seas--this egg must have drifted a long ways to end up here."

    grusha @talkingmouth "Is it a Flying-type or an Ice-type?"

    red @closedbrow sweat talking2mouth "Uh... no. Pure water."

    grusha @closedbrow talking2mouth "Not much I can do with it, then. Maybe I'll give it to Lisia. That might earn Jasmine some brownie points."

    red @talking2mouth "...Yeah, I guess."

    grusha @confused "Oh, unless you want it? I guess we found it together."

    red @closedbrow talking2mouth "No, it's... it's fine. I just thought you might be excited. Like, Phione are {i}really{/i} rare. They were even considered Mythical in Sinnoh for a while!"

    grusha @unamusedbrow talking2mouth "That doesn't mean anything. Sinnohans think everything's a Mythical or a legend. You've seen what they say about Bidoof, right?"

    red @talking2mouth "Fine, fine. I guess I'm the only one excited about it."

    pause 0.5

    grusha @closedbrow talking2mouth "{i}*Sigh.*{/i}"
    grusha @talkingmouth "Of course, Lisia probably doesn't really have the time to take care of an egg. So I {i}guess{/i} I can take care of it until it hatches."

    red @surprised "You will?"

    grusha @upeyes talking2mouth "I've never seen someone so disappointed over an unhatched egg before. I felt bad."
    grusha @unamusedbrow talkingmouth "Although that means you're on the hook for it if I kick the bucket before it hatches."

    red @sadbrow talking2mouth "You won't."

    grusha @closedbrow talkingmouth "We'll see. You know about this Phione, right? So you know how to take care of the egg?"

    red @talking2mouth "...Kinda. I know keeping it warm, and rocking it gently, is a good idea. Normally, warm oceans would do that, but..."

    grusha @talking2mouth "I guess I could start wearing a fanny pack."

    red @happy "Stylish. Dad fashion never goes out of style."

    grusha surprisedbrow @talkingmouth unamusedbrow "For the record, you're the mom here."

    red @unamusedbrow sweat talkingmouth "Says the guy wearing the skirt."

    grusha -surprisedbrow @talkingmouth "Touché."
    grusha sad2eyes smirkmouth @talking2mouth "Oh, yeah. I'm probably going to need to ask you a bunch of questions about this egg, so it'd be easier if we had each other's cell numbers."

    red @talkingmouth "Gotcha."

    $ BecomeContacted("Grusha")

    grusha unamusedbrow talkingmouth "Thanks. Now, [bluecolor]'honey'{/color}, let's go home. And wait until you hear what The Little Prince did at school today!"

    hide grusha with dis

    red @surprisedbrow frownmouth "[ellipses]"
    redmind @surprisedbrow frownmouth "He's already named it?!"

    $ RelationshipRankUp("Grusha", "'Honey'", 1)

    call clearscreens() from _call_clearscreens_25
    scene blank2 with splitfade

    pause 3.0

    show midnight at vspaz

    $ timeOfDay = "Midnight"

    pause 3.5

    scene seaportnight with splitfade

    pause 1.0

    show summer angrybrow goggles2 frownmouth at night with Dissolve(2.0):
        xpos 0.66 xzoom -1 

    summer @talking2mouth "...We've chased that egg all the way to Kobukan."
    summer @closedbrow talking2mouth "Damn. I never thought I'd end up in this tiny region again."

    show summer at night:
        xpos 0.66
        ease 0.5 xpos 0.33

    show kate surprisedbrow frownmouth at night with dis:
        xpos 1.5 xzoom -1
        ease 0.5 xpos 0.66

    kate @talking2mouth "Miss Ranger? You've been to Kobukan before?"

    summer @talking2mouth "More than that. I graduated from here."

    kate @surprised "From the region?!"

    show summer at night:
        xzoom -1 xpos 0.33
        ease 0.5 xzoom 1

    summer goggles -angrybrow @surprisedbrow talking2mouth "Huh? Wha--no. No, from Kobukan Academy."

    kate -surprisedbrow -frownmouth @closedbrow talking2mouth "Oh, okay. Hold on, let me make a note of that."

    summer @sadbrow talking2mouth "You really don't have to."

    kate @talkingmouth "'Miss Ranger{w=0.5} graduated from{w=0.5} Kobukan Academy.'"

    summer @closedbrow talking2mouth "That's not important."

    kate @angrybrow talkingmouth "It might be! I'll only get one chance to shadow a real Rank 10 Ranger!"

    summer @talking2mouth "Oblivia doesn't rank Rangers."

    kate @happy "I know! You're so skilled, Miss Ranger, that you don't even need a rank! You're above Top Ranger status--you're Toppest Ranger!"

    summer @unamusedbrow unamusedmouth "[ellipses]"

    summer @talking2mouth "...How much longer will your internship last?"

    kate @happy "It ends April 4th, 2005."

    pause 0.5

    kate @talkingmouth "Why?"

    summer @unamusedbrow talking2mouth "Just curious."

    pause 1.0

    summer @closedbrow talking2mouth "Alright, let's get on with it. That egg is extremely important, and we have no idea who could have picked it up." 
    summer @angry "If it was the Pinchers, the egg could go underground, and then we'd never be able to find it. What does your gizmo say?"

    kate @happy "Oh! The Ovitrace AquaScan says the egg's right here, in the harbor!"

    pause 1.0

    show kate surprisedbrow frownmouth with dis

    summer @unamusedbrow talking2mouth "It clearly isn't, though."

    kate @surprised "That can't be right! The OAS can detect {i}any{/i} egg in water! It must be..."

    pause 1.0

    kate @shadow angrybrow talking2mouth "It's invisible!"

    summer @closedbrow talking2mouth "It's not invisible. It's just not there."
    summer @unamusedbrow talking2mouth "So what you're telling me is that your doohickey can only detect the egg if it's actively {i}in{/i} water?"

    kate "[ellipses]"
    kate -surprisedbrow @confusedbrow talking2mouth "Um. What did you think AquaScan meant?"

    summer @unamusedbrow unamusedmouth "[ellipses]"
    summer @talking2mouth "Fine. That one's on me. At least we ended up in the right {i}region.{/i} We have contacts here. If someone at that Academy picked it up, then we should know soon."

    show kate sadbrow frownmouth with dis

    summer @talkingmouth "In the meantime, see if you can make that gizmo of yours work {i}outside{/i} of water."

    pause 2.0

    summer surprisedbrow frownmouth @surprisedbrow talking2mouth "What, what is it?"

    kate @talking2mouth "I'm just... I'm worried that the OAS will feel upset that he couldn't get the job done."
    kate @sad2eyes sadeyebrows talking2mouth "I don't want him to think we don't appreciate him."

    show summer unamusedbrow unamusedmouth with dis

    kate @talking2mouth "Maybe you could tell him you're proud of him? Just to make him feel a bit better before I disassemble him?"

    $ autoquote = False

    summer "([ellipses]It was either this or administrative leave.)"

    $ autoquote = True

    pause 0.5

    show kate -sadbrow -frownmouth with dis

    summer @closedbrow talkingmouth "I... I'm proud of you, OAS. You did a good job."

    pause 0.5

    kate @happy "Hm! Hear that? He's happy!"

    summer @talking2mouth "I'm psyched."

    kate @happy "Alright! I'll get the OAS reconfigurated in a jiffy, and we'll be back on the tail of that Manaphy Egg faster than you can say 'Guardian Signs, give me strength.'"

    pause 0.5

    kate @confused "Hey, why {i}do{/i} you say that all the time?"

    summer @talking2mouth "I'm very religious."

    show kate at night:
        xpos 0.66
        ease 10.0 xpos -1.0

    kate @happy "Oh, okay! Now, what color do you think the Ovitrace AeroTerraScan should be? {size=30}The color you paint your machine changes its personality, you know!{/size}{size=26} I think a sort of cool detachment might fit OATS{/size}{size=22}--or maybe a hostile ne'er-do-well attitude,{/size}{size=18} or perhaps a rebel without a cause, or...{/size}"

    pause 3.0

    hide kate with dis

    summer sad "Guardian Signs, give me strength."

    show blank2

return