label May1:
    if (not IsBefore(1, 5, 2004)):
        $ persondex["May"]["Events"].append("Level2SceneVer2")

    scene research
    show may at leftside:
        zoom 0.8
    with Dissolve(2.0)
    stop music fadeout 1.5
    $ renpy.music.queue("Audio/Music/RSE_Rival_start.ogg", channel='music', loop=False, tight=None)
    $ renpy.music.queue("Audio/Music/RSE_Rival_loop.ogg", channel='music', loop=True, tight=None)

    red @happy "Oh, hey, May! Didn't expect to see you here. What are you up to?"

    may @happy "[first_name]! Hiya. I'm just doing some research."

    show may:
        ease 0.5 xpos 0.5 zoom 1.0

    if (not IsBefore(1, 5, 2004)):
        red @talkingmouth "Cool. Is it alright if I join you?"

        may @happy "Of course! It's not like I'm worried about you using your mind control powers on me or anything."

        red @sadbrow talkingmouth sweat "The ones I don't have."

        may @angrybrow happymouth "Yeah, those ones."

        red @closedbrow talkingmouth sweat "Alright, just making sure we're on the same page." 
        red @talkingmouth "So, you said you're doing research?"

    red @talkingmouth "What about? School stuff?"

    may @talkingmouth "Yeah, I'm trying to figure something out for Bug class." 
    may @surprisedbrow sadmouth "Instructor Burgh mentioned that the way Bug-types create their webs is more an art than a science..."
    may @happy "But my dad always says that art is just science people haven't put a formula to, yet!"

    red @closedbrow talking2mouth "Your Dad... oh, Professor Birch, right?"

    may @talkingmouth "The one and only."

    red @talkingmouth "I guess you were raised in a pretty science-y household, then?"

    may @talkingmouth "Yup. Science and research have been in the Birch family line for generations."
    may @happy "My Dad moved to Hoenn to study the biodiversity there a few years before I was born."

    red @closedbrow talking2mouth "So, is that what you want to do when you graduate?"

    may @talkingmouth "Nah. I could never do better than my Dad, anyway. I want to be a contest coordinator, with Brendan."

    red @surprised "Oh, right! I think you might've mentioned that..."
    red @closedbrow talking2mouth "How did you and Brendan end up becoming interested in coordinating, anyway?"

    may @talkingmouth "{i}Contest{/i} coordinating. Musical coordinating is a different thing."

    red @talkingmouth "Oh, right. My bad."

    may @happy "It's no problem! Anyway, contests are {i}really{/i} popular in Hoenn. Actually, that's where they were invented."
    may @talkingmouth "I guess we both just kinda grew up watching coordinators on TV, instead of trainers. So that's who we wanted to become."

    red @talkingmouth "Kinda funny that you're going to enter an arts field instead of a science field, huh?"

    may @sadbrow happymouth "I guess it is. My Dad was surprised, actually. He always thought that I'd take over the Birch Lab when he retired."
    may @closedbrow talking2mouth "Actually, I think he's a bit angry at Brendan, because he thinks Brendan made me want to be a coordinator."

    red @confused "Really? But Brendan's always talked so highly about your Dad."

    may @happy "Yeah... my Dad's a really big softie. When he's angry at someone, the worst he'll do is not offer them extra cornbread at dinner."

    red @happy "The horror!"

    may @talkingmouth "Besides, Brendan's so nice, I don't think he'd even notice if someone were {i}furious{/i} with him."

    red @sadbrow talkingmouth "I don't know what Brendan could even do to make someone furious with him."

    if (IsBefore(1, 5, 2004)):
        may @happy "Yeah. I mean, the only arguments we ever have, really, are about something I cook."

        red @closedbrow talking2mouth "Right... I kinda clued into that, actually. What's the deal there?"

    else:
        may @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

        may @sad "...Well..."

    may frownmouth @talkingmouth "Oh, it's... well... hm."
    may @closedbrow talking2mouth "Hmm..."

    red @talkingmouth "Trying to decide something?"

    may @talkingmouth "Yeah. I'm wondering if I should tell you... but I guess I can? We know each other well enough, and you're friends with Brendan."

    red @talkingmouth "Well, there we go, th--"

    may -frownmouth @happy "But I think I'm going to leave it up to this coin!"

    pause 1.0

    red @confused "...Wait, for real?"

    may @talkingmouth "Yeah!"

    red @wince talking2mouth "Um... isn't flipping a coin to decide this kinda irresponsible? I mean, if you don't trust me, that's fine, but I wouldn't leave it up to chance."

    may @happy "It's totally irresponsible. But that's a good thing. I'm not responsible at all--the coin is!"

    red @confused "That's... an interesting interpretation of how responsibility works."

    $ PlaySound("coinflip.ogg")

    pause 1.0

    may @surprised "Okay. So that's a heads." 
    may @happy "So, sure, I guess I'll tell you!"

    red @confused "Sure."

    may @talkingmouth "So... I like to cook. I do pretty much all of the cooking for my dorm, and whenever Brendan and I have picnics or whatever, I cook for those, too."

    red @talkingmouth "With you so far."

    may @happy "I learned back home in Hoenn. Taught myself, actually. My dad's great with a grill, but... he can also, kinda, {i}only{/i} grill."
    may @talkingmouth "So I learned to cook and bake, just so we had a bit more variety in our food. And I got really, really, good at it, too."
    may @sad "But... um. Pretty much the only things I know how to make are... meat and sweets..."

    if (IsBefore(1, 5, 2004)):
        may @happy "And Brendan's a vegetarian who doesn't like sweet things."

        red @surprised "Eesh. That's unfortunate."

        may @angry "Yeah, and the weird part is that he wasn't always like that. We've been dating for years, known each other for ten, and for the first nine, he couldn't get enough of my cooking!"
        may @sadbrow talkingmouth "I know that nobody can help it if his tastes changed... but I don't know what to do, now. I can't cook nearly as often as I used to, since there's not a lot I know how to make that he can actually eat at this point."

    else:
        may frownmouth @sad "And Brendan was... well, sick of it."

        red @confused "Huh?"

        may @sadbrow happymouth "He said he loved my cooking at first, and... I can tell he's telling the truth. I saw how his eyes sparkled for the first few years."

        redmind @confusedeyebrows frownmouth "First few {i}years?{/i}"

        may @sad "But... I drove him to the point where he felt he had to {i}lie.{/i} Lie that he was a vegetarian, lie that he didn't like sweet things!"
        may @sad "And... I mean, I was a {i}little{/i} bit mad at him for that, but I was mostly even more upset with myself..."

        may @closedbrow sadmouth "I only found out when Sabrina... you know."

        may @sadbrow happymouth "So I confronted him, and he confessed. Like, right away, he didn't try to hide it. And he said he felt really bad he lied in the first place."

        red @closedbrow talking2mouth "So... you're not sure you can trust him, now?"

        may @surprised "What?"
        may @angry "No! I can {i}absolutely{/i} trust him!"

        pause 1.0

        may @angry "Lying was wrong, but... If I hadn't..."

        pause 1.0

        may @sadmouth "I... I just don't know what to do, now. I don't want to force him into another situation where he feels like he needs to lie."

    red @closedbrow talking2mouth "Hmm... "
    red @talking2mouth "You {i}do{/i} like cooking for him, right? Like, you're not just doing it out of a sense of obligation?"

    may -frownmouth -sadbrow @happy "Of course! It's really fun. And besides, it's how I tell him I love him."

    red @happy "Cute."

    pause 1.0

    red @sadbrow talkingmouth "Forgive me for asking a dumb question, but have you considered learning some new recipes?"

    show may sad with dis

    pause 1.0

    red @sad "Oh, sorry. Did I say something I shouldn't have?"

    may -sad frownmouth @closedbrow sadmouth "No... It's just... I've known five recipes for ten years."
    may @happybrow sadmouth "And I'm good at them!"
    may @closedbrow talking2mouth "What if it turns out I'm not good at any others?"

    red @closedbrow talking2mouth "Well... then you could practice, I guess."

    may @angry "Practice on Brendan? I'm not going to give my sweetheart crappy food just so I can get better."

    if (not IsBefore(1, 5, 2004)):
        red @confusedeyebrows talking2mouth "May, trust me. As a dude, he'll probably really appreciate seeing you taking steps to improve."

        may @closedbrow talking2mouth "No. I have standards for my boyfriend."

        red @sweat closedbrow talkingmouth "Worth a shot. Well, then, alternative idea."

    red @happy "You can practice on me! I'll eat pretty much anything."

    may @closedbrow talking2mouth "Mm... maybe. Maybe I should flip a coin for this..."

    pause 2.0

    $ PlaySound("idea.ogg")

    show may surprisedbrow frownmouth with dis

    red @happy "Oh, I get it!"

    may @talkingmouth "Huh?"

    red @talkingmouth "This isn't about cooking at all."
    red @angrybrow happymouth "You're afraid of change, aren't you?"

    may -surprisedbrow -frownmouth -surprised angry "Hey! That's a bit rude!"

    red @happy "It's the only thing that makes sense. You don't want to make big decisions, so you let other people, or that coin, make them for you."
    red @talkingmouth "And you don't want to learn new recipes, because, right now, you're good at everything you make." 
    red @talkingmouth "Even if Brendan's overexposed to it, you know that the food is, objectively, good. So why change it, right?"

    show may angrybrow frownmouth with dis

    pause 1.0

    redmind @wince frownmouth "Uh-oh. Did I blow it?"

    may -angry -angrybrow frownmouth @closedbrow talking2mouth "I guess you aren't entirely wrong..."

    if (IsBefore(1, 5, 2004)):
        may @sad "But you can't tell Brendan this! He just thinks I'm really forgetful."

        red @closedbrow talking2mouth "...I don't think couples should have secrets from each other. I won't tell Brendan, but you should."

        may @sad "Yeah, you're right, {w=0.5}of course." 

    else:
        may @sad "And... on top of all this... now Brendan is walking on eggshells around me, because he thinks I'm mad. And I am. But only a little bit? I don't know..."

        pause 1.0

        may @sadmouth "I guess you're right."

    may @sad "I {i}am{/i} afraid of change."
    may @closedbrow talking2mouth "I never thought that was a bad thing, though. Everything's going fine now, so why try to fix what isn't broken?"

    red @talkingmouth "Change isn't always about fixing a broken thing. Change sometimes just lets you get better."
    red @happy "I mean, you're in the Bug-type elective. You know this, right? A bug's gotta mash all its insides up into gross goop before it can become a butterfly."

    may @angrybrow talking2mouth "Are you saying I need to enter my gross goop phase?"

    red @talkingmouth "Well... yeah. A Caterpie might think its life is perfect, but I'm pretty sure there's no Butterfree that would want to go back to being a Caterpie."
    red @happy "Also, your Dad's a scientist, and you've been around science-y stuff your whole life. You know how important evolution is, right? Not just for Pokémon. People have to evolve, too."
    red @winkbrow talkingmouth "But if you want to evolve, that means you need to {i}actively{/i} make the choice to. And you need to decide what you're evolving into. You can't just flip a coin on that."

    may @talkingmouth "Actually, Wurmple randomly evolve into either Silcoon or Cascoon."

    red @happy "Correct me if I'm wrong, but I don't think you're a Wurmple?"

    may @happy "I used to pretend to be one! My Dad bought me a sleeping bag that looked like a Cascoon. I loved that thing."
    may @sad "...But then I got too big for it."

    red @happy "Evolution does have its downsides--like not fitting in your cozy Cascoon sleeping bag any more. But the upsides are too big to turn down."

    if (pikachuobj.GetId() == 25):
        may -frownmouth @angrybrow happymouth "Pretty big of Mr. I'm-Never-Evolving-My-Pikachu to be lecturing {i}me{/i} on evolution."

        red @talkingmouth "Hey, I would if I could. And he wanted to evolve, of course."

    else:
        may -frownmouth @angrybrow happymouth "Pretty big of the former Mr. I'm-Never-Evolving-My-Pikachu to be lecturing {i}me{/i} on evolution."

        red @talkingmouth "Well, I've changed, too. And so has [pika_name]. 'Cause change is good."

    may @talkingmouth "It's kinda weird that I'm telling you this stuff before everyone else... but I really want Brendan to see me as better than I am." 
    may @happy "You know?"
    may @sad "I mean, the scientists' daughter and entomologist who doesn't want to go through her own metamorphosis? It sounds like a bad joke."

    red @happy "I don't think there's anything to worry about there. Brendan is the most non-judgmental guy I know. And it's obvious that he loves you just as much as you love him."
    red @talkingmouth "The fact you're so worried about making this work is proof that even if you're afraid of changing what you have, and messing up, you'd find a way to fix it."

    if (not IsBefore(1, 5, 2004)):
        red @sweat talkingmouth "Besides. You mentioned he's walking on eggshells around you, right? He probably wants to fix this just as much as you do."

    may @happy "Aw. Thanks, [first_name]. You're a good friend."

    red @talkingmouth "I try my best. But, again, the best way to fix any issues you think you might be having is to just tell Brendan everything you've told me."

    pause 2.0

    may @talkingmouth "[first_name], have you ever had a girlfriend?"

    red @happy "Hah! No, I have not." #FIX THIS: Change when Red has possibility to get girlfriend/boyfriend

    may @closedbrow talking2mouth "What about a boyfriend?"

    red @talkingmouth "Nope. Though I {i}would{/i} be open to it."

    may @angrybrow happymouth "Maybe I should be worried about how much time you're spending around Brendan, then!"

    red @happy "Nah, I'm not a homewrecker. Don't worry about me."

    may @talkingmouth "Phew. That's a relief."

    red @talkingmouth "Anyway, why do you ask? About whether I've ever had a, uh, partner, I mean?"

    may @angrybrow happymouth "It's just that you're giving a lot of advice for someone who's never actually {i}been{/i} in this situation. Where'd this come from, huh?"

    pause 1.0

    show may surprisedbrow frownmouth with dis

    red @confused "Will you be offended if I say 'common sense'?"

    may angrybrow @angry "A little bit, yeah!"

    red @happy "Sorry! But that's where this is coming from. I mean, communication works. And it's the {i}only{/i} thing that works. If you can't Pokémon battle it into submission, then you just gotta talk to it, and if that doesn't work, nothing will."

    show may thinking with dis

    pause 1.0

    red @angrybrow talking2mouth "No, you can't Pokémon battle away your fear of change."

    may sad "Dang it."

    show may thinking with dis

    pause 1.0

    red @closedbrow talking2mouth "You also can't Pokémon {i}contest{/i} away your fear of change."

    may sad "Double-dang it."

    if (IsBefore(1, 5, 2004)):
        red @talkingmouth "If the idea of just explaining why you make the same meals for Brendan over and over is {i}really{/i} that terrifying, though, then you can just practice your new recipes on me."
        red @closedbrow talking2mouth "Maybe a bit less spicy than you would normally do, though."

        may -sad @talkingmouth "Mm..."
        may @happy "Alright! Thank you. But {i}please{/i} don't tell Brendan about this."

        red @talkingmouth "I won't. As long as you promise you, eventually, will."

        pause 1.0

    else:
        red @talkingmouth "The way I see it, you've already handled that hardest part of this. Or... Sabrina did, anyway."

        red @sadbrow talkingmouth "Now the secret's out, and everyone can be truthful with each other. This could be a good thing, if you choose to see it that way."

        may -sad @talkingmouth "Okay. I will."

        red @happy "Cool. Also, can I say... I'm kinda jealous?"

        may @talking2mouth "About what?"

    red @talkingmouth "It's really obvious how much you and Brendan care for each other. I want that someday."

    may @happy "Aw. That's sweet of you. And I'm sure you'll find someone who loves you as much as I love Brendan."

    red @happy "What do you love about the guy? I mean, I know why I like him, but what's your reason?"

    may @sadbrow happymouth "I'm not even sure I could say them all."
    may @closedbrow talking2mouth "He's so kind. If he thinks anybody is feeling lonely, or needs help with something, he's always there. Even if he's not actually good at the thing he's helping with."
    may @happy "And he's so funny. He's got such an innocent mind, and we can look at the same thing and see two completely different things. He always sees the world in a different way than I do, and I love finding out how he feels about things."
    may @talkingmouth "It's been years since we started dating, but I still learn new things about his mind every day. And I love that."

    red @confused "...Okay, but when are you going to mention that he's hot and fit as hell?"

    may @angrybrow happymouth "I was {i}getting{/i} to that! Let me fawn over my boyfriend at my own pace, please!"

    red @happy "{i}Mea culpa.{/i}"

    may @happy "Well, I don't usually mention that, because I don't want to seem shallow, but I really do love how much effort he puts into his appearance."
    may @talkingmouth "Part of it is just that Pokémon coordinators need to look good if they want to win, but he goes above and beyond."
    may @talkingmouth "He wakes up at six in the morning every day, just so he can work out, take a shower, brush his teeth, and do his hair."

    red @talkingmouth "I {i}have{/i} noticed. Brendan's pretty fastidious for such a big guy."

    may @happy "Yeah. I love that about him. He's so disciplined, and when he's got his mind on something, he'll never let go, and he works {i}so{/i} hard on anything he tries to..."

    $ ValueChange("Brendan", 3, -0.5)

    narrator "Extolling Brendan's virtues with May makes you feel as though you both have a better understanding of Brendanity. You gained three points with Brendan!"

    show may closedbrow frownmouth with dis

    pause 1.0

    red @confusedbrow talkingmouth "May? You with us?"

    may -closedbrow -frownmouth @sadbrow happymouth "I'm sorry, I need to go cuddle my boyfriend. I just remembered how much I love him."

    if (IsBefore(1, 5, 2004)):
        red @happy "Aw. Love him enough to tell him why you don't want to make any new meals?"

        may @sadbrow happymouth "...Maybe after I practice."

        red @talkingmouth "I'll take it. And I'm here to help. You got any noxious, steaming piles of Mystery Food X? I'll try them before they get anywhere near Brendan's delicate palate."

    else:
        red @happy "Sounds good. And remember--if you've got any noxious, steaming piles of Mystery Food X? I'll try them before they get anywhere near Brendan's delicate palate."

    may @happy "Thanks! I bet you'll be a great {color=#0048ff}taster{/color}!"

    $ persondex["May"]["Relationship"] = "Taster"
    $ persondex["May"]["RelationshipRank"] = 1

    $ renpy.music.set_volume(0.1, delay=0.0, channel="music")
    $ PlaySound("sav.ogg")
    $ renpy.music.set_volume(1.0, delay=1.0, channel="music")

    narrator "Your heart shifts as you feel your relationship with May evolve from '{color=#0048ff}Friend{/color}' to '{color=#0048ff}Taster{/color}'!"

    return