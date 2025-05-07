label Serena1:
    if (not IsBefore(1, 5, 2004)):
        $ AddEvent("Serena", "Level2SceneVer2")

    scene hall_B 
    show serena
    with Dissolve(2.0)
    $ renpy.music.queue("Audio/Music/Vaniville_Start.ogg", channel='music', loop=None, fadein=0.0, tight=None)
    $ renpy.music.queue("Audio/Music/Vaniville_Loop.ogg", channel='music', loop=True, tight=None)

    narrator "As you turn the corner, you see Serena struggling under the weight of several large books."

    red @talkingmouth "Serena! What're you up to?"

    serena @surprised "Ah? {w=0.5}{nw}"
    extend @happy "Oh, hello. I was just going to the library. I need to catch up on my studying, I'm afraid."

    red @closedbrow talking2mouth "Yeah, that'd explain the stack of books."

    menu:
        "Would you appreciate a study partner?":
            pass

        "Need any help carrying those?":
            pass

    serena @happy "Why, certainly. That would be splendid, thank you."

    red @happy "Cool. Let's head off to the library, then."

    scene library with splitfade

    show serena with dis

    pause 2.0

    red @closedbrow talking2mouth "You've got a pretty wide variety of subjects here. Pokémon breeding, battling, training... looks like a shark cutlery bored."

    serena surprisedbrow frownmouth @surprised "{i}...Qu'est-ce que c'est?{/i}"

    red @surprised "Huh?"

    serena closedbrow talking2mouth "What is... a 'shark cutlery bored'?"

    red @happy "Oh, you know! One of those things where there's all kinds of meats and cheeses, and you eat them down with a bunch of wine."

    serena sad "Are... are you referring to a {i}charcuterie board{/i}?"

    red @surprised "Oh, shit, that's what it's called? That's {i}way{/i} more Kalosian than I was expecting."

    serena -sad "[ellipses]"

    serena @happy "Hee hee hee. You are quite entertaining, [first_name] [last_name]."

    red @closedbrow talking2mouth "Uh, thanks. Kinda feel like I'm the butt of a joke here, but... thanks."

    serena @happy "{i}Non, non!{/i} I'm not laughing at you. I am laughing, ah, {i}with{/i} you. Shark cutlery... hee hee!"

    red @angrybrow happymouth "Yeah, well, I bet a hoity-toity upper-class woman like yourself has her blind spots as well."

    serena angrybrow @happymouth "Oh? Do you challenge me?"

    red @happy "You bet your lavender-scented bedsheets I do."

    serena @happymouth "Then, please, ask me anything you think might be in my blind spot. You may find me surprisingly well-informed."

    red @talkingmouth "Sure. This is something everyone who's ever had to go for a hike on a sweltering forest trail would know. What's in bug juice?"

    serena -angrybrow frownmouth surprisedbrow @surprised "Eh?"

    red @happy "Oh, you don't know? Washing out that early, huh?"

    serena -frownmouth -surprisedbrow @closedbrow talking2mouth "No, I know this. I just thought your questions would be more... agrarian in nature."

    red @confusedeyebrows talking2mouth "Why does everyone think I'm a farmer?"

    serena -thinking @closedbrow talking2mouth "In any case, bug juice is 25 percent purple grape juice, 25 percent raspberry juice, 45 percent lemon-lime soda, and 5 percent vodka, if no-one's watching. With a bit of ice."

    red @surprised "Uh... okay, that is genuinely surprising."

    serena angrybrow @happymouth "Please, keep them coming."

    red @closedbrow talking2mouth "Okay. Uh, what's the best way to catch catfish Pokémon from lakes or ponds?"

    serena @happy "Noodling, of course. Why waste money on bait, when they're just as liable to chow down on your hands?"

    red @surprised "Shit. Okay, your car's battery is dying, it keeps going down, won't charge up even when you drive. What's the problem?"

    serena @happy "Well, it could be any number of things, but the first thing I'd do is check the alternator." 
    serena @closedbrow talking2mouth "If it's broken, then you can just get a new one from pretty much any auto parts store."

    red @surprised "And what if it doesn't fit?"

    serena @happy "Well, that means the bushing is probably a bit too large. So you can just sandpaper the alternator's rear end down."

    red @surprised "...How the hell...?"
    red @closedbrow talking2mouth "Wait. I got it. No, I got it, now. There's absolutely {i}no way{/i} that an upper-class Kalos girl will get this one."
    red @angrybrow happymouth "There's a sport that's pretty popular in Kanto. It's slow, dangerous, and {i}very{/i} dirty."
    red @closedbrow talking2mouth "I don't think even middle-class Kantonians watch it, even though it originated there."
    red @talking2mouth "So--"

    serena @happymouth "Rhyhorn Racing."

    red @surprised "...Uh. A-and... who's the best Rhyhorn Racer...?"

    serena -angrybrow @closedbrow happymouth "That would be Grace Umaoka."

    red @wince talking2mouth "...Damn. I've been completely beaten."

    serena @talkingmouth "Why, thank you. What do I win?"

    pause 2.0

    $ PlaySound("idea.ogg")

    red @angrybrow talking2mouth "Hey. Wait a minute."

    serena surprisedbrow frownmouth @surprised "Oh?"

    red @closedbrow talking2mouth "You're from Kanto."

    serena @talkingmouth "Er... why do you think that?"

    red @talkingmouth "Give me a better reason for you to know Grace Umaoka."

    serena @talkingmouth "Uh... Well, I mean, there are plenty of possible reasons, such as..."

    red @confusedbrow frownmouth "...?"

    serena -surprisedbrow -frownmouth -surprised @sad "I could be related to her?"

    red @closedeyes talking2mouth "Yeah, that doesn't seem likely. Anyway, even if you were, that'd just {i}prove{/i} you're from Kanto."

    serena @surprised "How so?"

    red @happy "Well, I mean, she's Kantonian. She lived there her whole life before she moved...{w=0.5} to...{w=0.5} Kalos...{w=0.5}"

    pause 2.0

    show serena happybrow with dis

    show library with vpunch

    red @surprised "OH MY GOD."

    red @surprised "{i}You're{/i} Serena Umaoka?! Grace's daughter?!"

    serena -happybrow @closedbrow talkingmouth "Shhh. We're in a library."

    red @wince talking2mouth "Sorry."

    serena @sad "But, ah... yes, I am."

    red @talkingmouth "I had a poster of your Mom on my wall at home!"

    serena @talkingmouth "Many did, yes."

    red @talkingmouth "I don't get it, though. Your mom only left Kanto, like, two years ago. What happened?"

    serena @surprised "Could you clarify?"

    red @talkingmouth "Yeah. I mean, I didn't really follow you, no offense, but I sometimes went to your Mom's races, and saw glimpses of you."

    serena @surprised "I'm... not offended that you did not follow me."

    red @closedbrow talking2mouth "But, just, like, two years ago, I remember... you were all... overalls and pigtails. You wore a baseball cap."
    red @closedbrow talking2mouth "You were whooping and hollering at those races. Yelling out like the reddest-necked farmer anywhere in Southwest Kanto."
    red @happy "I mean, I recognize the sunglasses, but everything else... I mean, if you hadn't just told me, I would {i}never{/i} have recognized you."

    serena @sad "Well... a lot can happen in two years."

    red @closedbrow talking2mouth "Yeah, but... {i}that much{/i}? There's gotta be more than just the new environment, right?"

    serena @talkingmouth "As a fan of my mother, I assume you heard about the silicon mine we discovered under our ranch?"

    red @talkingmouth "Yeah, didn't Silph Co. buy it from you for, like, a billion?"

    serena @talkingmouth "Very slightly less. In any case, with that much money... and since we no longer had our ranch... well, we'd always wanted to visit Kalos."

    red @closedbrow talking2mouth "Hm... that explains {i}why{/i}, and {i}how{/i}, you moved... but just moving wouldn't cause such a dramatic change."

    red @sadeyes sadeyebrows happymouth "I mean, I think. I've obviously never moved anywhere before coming to Kobukan."

    serena @sad "...People change for the oddest reasons."

    pause 2.0

    show serena surprisedbrow frownmouth with dis

    red @closedbrow talking2mouth "Does this have anything to do with Calem?"

    show serena sad2brow poutmouth with dis

    pause 2.0

    serena -sad2brow frownmouth @sad2brow talking2mouth "What would make you think that?"

    red @sadeyes sadeyebrows happymouth "Not much. I've just got two dots, and I'm trying to connect them."
    red @talkingmouth "Calem and you knew each other before coming here. Calem didn't know you'd be here, but it seems like you {i}did{/i} know he'd be here."
    if (not IsBefore(1, 5, 2004)):
        red @closedbrow talking2mouth "And now you dorm together."
    red @closedbrow talking2mouth "That's, it just... never made sense to me."

    serena sad "I'm sorry. I don't think... I don't feel comfortable telling you about this. Perhaps one day. But not now."

    pause 1.0

    red @talkingmouth "That's fine. I just want to know something. Are you alright? You're not... forcing yourself to be something you're not, are you?"

    serena @happymouth "If I was, how would I know?"
    serena @sadbrow happymouth "What is the 'true self' beyond the entirety of the memories and thoughts that make up a person?"
    serena @closedbrow talking2mouth "To demonstrate the fullness of the true self at all times sounds exhausting."
    serena @talkingmouth "Though I abhor when one is forced to pretend to be a person they're not..."
    serena -sad @happy "I don't see anything wrong with simply, temporarily, not demonstrating certain parts of yourself. For convenience's sake."

    redmind @sad "That sounds... very much like pretending to be a person you're not."

    red @talkingmouth "Well... I'll leave it there then, Serena Umaoka." 
    red @closedbrow talking2mouth "But if you ever change your mind, and want to tell me about the real Serena, whatever that means, I'll be here."

    serena @talkingmouth "I appreciate it."

    pause 2.0

    serena @closedbrow talkingmouth "I must say, [first_name] [last_name], I am surprised."

    red @surprised "Oh?"

    serena @closedbrow talkingmouth "Yes. I didn't realize you were so perceptive. So intelligent."

    red @happy "C'mon, don't I just give off the vibes of a brainiac?"

    serena @happy "Not particularly, no."

    red @sad "Ouch."

    serena @talkingmouth "But to be able to figure out my background from those few questions... I think, perhaps, you too are hiding your light under a bushel somewhat."

    red @happy "What? Me? No way! I'm a genuine dumbass."

    serena @happy "Hee hee. If you insist."

    pause 2.0

    red @talkingmouth "So, hey, what now? Now that I know your big secret?"

    serena @sadbrow happymouth "I would ask that you please not mention it to anyone else. Calem knows, of course, but it would complicate my plans if he knew there was a third party involved."

    red @talkingmouth "Sure. My lips are sealed."

    red @happy "Uh... what kind of plans are those? Can I know?"

    serena @talkingmouth "Not right now, please."

    red @closedeyes talking2mouth "Ugh, I seriously want to know, though... Oh well. Anything I can do to help with those plans?"

    serena @poutbrow talkingmouth "Um... there is actually, one thing. It might not be possible, but..."

    red @talkingmouth "Sure, name it!"

    if (IsBefore(1, 5, 2004)):
        serena @closedbrow talking2mouth "Would it be possible for you to, ah... make sure Calem stays single?"

        red @surprised "Oh, wow, that's where we're going with this? I mean, I don't know what I can do about that."

        serena poutbrow poutmouth @talking2mouth "...I mean, ah... could you make sure that he stays single, in regards to... ah..."

        redmind @thonk "What's the problem? It looks like she's trying to say something she doesn't know how to say."

        serena frownmouth angrybrow @furybrow angrymouth "Oh, what-{i}ever!{/i} Listen up, [first_name]. You start datin' Calem, and we're going to have {i}big problems{/i}, y'hearin' me?"

    else:
        serena @closedbrow talking2mouth "Would it be possible for you to, ah... perhaps find Calem a... woman?"

        red @surprised "Oh, wow, that's where we're going with this? I mean, I don't know what I can do about that."
        red @confused "Wait, I thought {i}you{/i} wanted to date him?"

        serena @sad "I did! Er... I thought I did? But then I moved in with him, and everything has become so much more difficult, and... I don't know if... that is, to say, I'm unsure if..."

        serena poutbrow poutmouth @talking2mouth "...I mean, ah... it would be easier if he were {i}not{/i} single, since... in regards to... ah..."

        redmind @thonk "What's the problem? It looks like she's trying to say something she doesn't know how to say."

        serena @angry "Oh, what-{i}ever!{/i} Listen up, [first_name]. We'all need to get that boy hitched to some other chick--or man, it don't matter--before I have a nervous breakdown!" 
        serena frownmouth angrybrow @furybrow angrymouth "He's too damn kind, and didn't even {i}mention{/i} the fact I've been lyin' to his face for ages! Y'hearin' me?"

    redmind @surprised "Woah. Her facade completely broke there."

    red @surprised "Uh... yeah, absolutely. I'm hearin' ya."

    pause 2.0

    red @surprised "Wait, he likes men too?"

    serena -angrybrow @closedbrow talking2mouth "That's very clearly not the point."

    redmind @thinking "Huh. I was definitely getting the opposite vibes from him, but, uh... good to know."

    if (IsBefore(1, 5, 2004)):
        red @talkingmouth "Yeah, uh, noted. I'll do my best to avoid dating him. And if I can pull off some wacky hi-jinks to make sure he doesn't date anyone else, I'll see what I can do about that, too."

    else:
        red @talkingmouth "I don't get it, though. {i}You{/i} aren't dating, are you?"

        serena @sad "No."

        red @talkingmouth "Then... why don't you... just tell him you need some space?"

        serena @sadbrow talking2mouth "It is {i}not{/i} that easy. I was chasing after him for so long, and now that he's stopped and turned around to face me, I've run right into him."
        serena @sadbrow talkingmouth "...I have what I wanted. But everything I was chasing after has come too quickly, and... I cannot process my feelings properly when I wake up every morning staring into his gorgeous eyes."

        pause 2.0

        red @playfulbrow talking2mouth "So your plan is to get him a girlfriend--or boyfriend--so that he's no longer an option for yourself?"

        serena @talkingmouth "Rather."

        red @confused "And what if this substitute boyfriend/girlfriend is his {i}one?{/i}"

        serena @sadbrow talkingmouth "Then he will be happy. Consequently, so will I."

        pause 1.0

        red @happy "Well, hell, sign me up."

    serena happybrow neutralmouth "Splendid. I've always wanted to be part of a conspiracy."

    if (not persondex["Serena"]["Contact"]):
        serena "You'll need this, then, to report your success."

        $ BecomeContacted("Serena")

    pause 1.0

    red @talkingmouth "Hey. Uh, I can tell this is really important to you, but... are you sure you have time for this? I mean, Kobukan is really competitive, and everyone's so busy all the time..."

    serena @closedbrow talkingmouth "Hee hee hee."

    serena @talkingmouth "There's always time for true love, my {color=#0048ff}conspirator{/color}."

    $ RelationshipRankUp("Serena", "Conspirator", 1)

    return