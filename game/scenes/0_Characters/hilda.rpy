label Hilda1:
    if (not IsBefore(1, 5, 2004)):
        $ AddEvent("Hilda", "Level2SceneVer2")

    scene hall_B 
    show hilda
    with Dissolve(2.0)
    $ renpy.music.queue("Audio/Music/Nuvema2_Start.ogg", channel='music', loop=None, fadein=0.0, tight=None)
    $ renpy.music.queue("Audio/Music/Nuvema2_Loop.ogg", channel='music', loop=True, tight=None)

    red @talkingmouth "Hey, Hilda."

    hilda @surprised "[first_name]?"
    hilda @happy "Oh, shit, good to see you!"

    if (not IsBefore(1, 5, 2004)):
        red @surprised "Really?"

        hilda @surprised "Uh, yeah? What do you mean, 'really'?"

        red @sadbrow talkingmouth "Well... I just meant, you know, with the whole 'powers' thing..."

        hilda @talkingmouth "Water under the bridge."
        hilda @happy "I'll be real, I was {i}kinda{/i} on the fence at first, but after you explained the whole situation during the Quarter Qlashes..."
        hilda @sadbrow talkingmouth "I mean, how could I hold it against you? It's seriously effed up what you went through. I can't believe Cheren..."

        red @sadbrow talkingmouth "Thanks for being so understanding."

        hilda @sadbrow smirkmouth "That's me. Understanding to a fault." 
        hilda @talkingmouth "Are you doing anything big right now?"

        red @talkingmouth "Not really, no. What about you?"

    red @talkingmouth "What're you up to?"

    if (IsBefore(1, 5, 2004)):
        $ AddEvent("Hilda", "KetchupSpilledOnSerena")
        hilda @talkingmouth "Oh, I was just going to the Student Center. Bianca spilled a ton of ketchup on Serena's bed, so I'm going to the laundry rooms."

        red @confusedeyebrows talking2mouth "What was Bianca doing with ketchup on Serena's bed?"

        hilda @sad "Eh... the girls of Dorm 251 have agreed never to talk about it again, so I can't really tell you."

    else:
        $ AddEvent("Hilda", "KetchupSpilledOnBea")
        hilda @talkingmouth "Oh, I was just going to the Student Center. Bianca spilled a ton of ketchup on Bea's bed, so I'm going to the laundry rooms."

        red @confusedeyebrows talking2mouth "What was Bianca doing with ketchup on Bea's bed?"

        hilda @sad "Dorm 251 has agreed to never talk about it again, so I can't really tell you."

    red @happy "Aw, you tease."

    hilda @talkingmouth "Anyway, what's up with you? Mind if we walk and talk? I'm pretty busy."

    red @talkingmouth "Oh, yeah, sure."

    narrator "Hilda quickly strides ahead, and you need to speedwalk after her to keep up."

    red @happy "So, what're you doing after this?"

    hilda @closedbrow talking2mouth "Ugh, I don't even know."

    if (IsBefore(1, 5, 2004)):
        hilda @sad "I mean, after I do the laundry, I've got to restock the dorm fridge. May likes to make sure there's always a plate of cookies on the counter, and Leaf gets moody if there isn't. So I gotta help May with the cooking."
        hilda @closedbrow talking2mouth "After that, I've gotta research cute date restaurants in Inspira for Serena. She's got some sort of plan there, didn't have time to ask."
        hilda @talkingmouth "And Bianca's been really busy helping Nate and Cheren with their own projects, so her Pokémon need some walking. Said I'd do that for her. My Aron could do with a walk, too."
        hilda @happy "And, y'know, after {i}that,{/i} I've gotta do my own studying for class. Professor Sycamore's being a real hardass, says I'm not 'applying' myself."
        hilda @sad "And after {i}that...{/i} ugh, it's been like twelve hours since I checked in on Hilbert. He's probably choked to death on his own foot by now."

    else:
        hilda @sad "I mean, after I do the laundry, I've got to restock the dorm fridge. Hilbert and Bea both have insane sweet tooths, so any time I look away from the fridge for half a second, all the food disappears."
        hilda @closedbrow talking2mouth "After that, I've gotta do some research into Unovan mythology with Nate. He's got this project he's working on, and I promised I'd help."
        $ aron_name = GetTrainerTeam("Hilda", "Aron").GetNickname()
        hilda @talkingmouth "And Bianca's been really busy helping Nate with that project I mentioned, so her Pokémon need some walking. Said I'd do that for her. My [aron_name] could do with a walk, too."
        hilda @happy "And, y'know, after {i}that,{/i} I've gotta do my own studying for class. Professor Sycamore's being a real hardass, says I'm not 'applying' myself."
        hilda @sad "And after {i}that...{/i} ugh, it's been like twelve hours since I checked in on Hilbert. He's probably choked to death on his own foot by now."

    red @closedbrow talking2mouth "Hm."

    pause 2.0

    red @happy "Hey, my running shoes are getting pretty old. Do you think you could grab a new pair for me next time you're in Inspira?"

    hilda @happy "Sure, what size are you?"

    red @confusedeyebrows frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    hilda frownmouth @closedbrow sadmouth "Ah. That was, uh, a joke, then?"

    red @closedbrow talking2mouth "More like a point. We haven't talked that much, Hilda, but doesn't your schedule seem {i}very{/i} full?"

    hilda @sad "I mean, yeah, it is... but so what? I can handle it."

    red @closedbrow talking2mouth "It just seems to me... putting this delicately... that most of your to-do list is for other people."

    hilda @closedbrow talking2mouth "I can still handle it, though."

    red @confusedeyebrows talkingmouth "I don't doubt that. But do you really need to? Pretty sure your roommates could handle their own chores."

    hilda @sad "Yeah, probably."

    red @happy "Right? So how about the next time they ask you to do something, you remind them of the {i}last{/i} time you did something for them?"

    hilda @happy "Ah, yeah, nah, that won't work. They don't actually ask me to do this stuff for them."

    red @closedbrow talking2mouth "What do you mean?"

    hilda @talkingmouth "I, uh... I just do it. 'Cause they want it done, and it needs to be done. So I just do it."

    redmind @thinking "Oh, boy. So this is a self-inflicted lifestyle, then."
    redmind @thinking "I guess it makes sense. Hilda's not the kind of woman who's a pushover, and can be forced to do things."
    redmind @thinking "More like she pushes other people over, and forces them to let her do things."

    red @confusedeyebrows talking2mouth "Wow. You've got a pretty intense sense of responsibility."

    hilda @sad "More like obligation."

    red @talkingmouth "Hey, speaking of obligation, what's up with you and Hilbert?"

    hilda @surprised "What? I... "
    hilda @closedbrow talking2mouth "Eh, what the hell. I guess it's fine."

    if (not IsBefore(1, 5, 2004)):
        hilda @smirkmouth "After all, if you wanted this info, your mind powers could just take it from me, right?"

        red @closedbrow talking2mouth "Not in the slightest."

    hilda @talkingmouth "Basically, Hilbert and I were raised together. His parents were often gone, doing missions for this Pokémon-rights organization they were part of."

    red @closedbrow talking2mouth "Sounds noble."

    hilda @closedbrow talking2mouth "Yeah, it was. Anyway, I took care of him, since I was already used to taking care of my Dad."

    red @surprised "Aren't you the same age? You and Hilbert I mean, not your Dad."

    hilda @happy "Almost. I'm nineteen, he's eighteen. But girls mature faster than boys--and even for a boy, he's hopeless."

    red @angrybrow frownmouth "I resemble that remark."

    hilda @closedbrow talking2mouth "Right, so where was I... oh, yeah, I took care of him." 
    hilda @talkingmouth "He'd go out and train, and I'd stay home and cook, put his clothes out, made sure he did his homework."
    hilda @closedbrow talking2mouth "I mean, I never thought it'd be a long-term thing. One day, I figured, he'd grow up into, y'know, a 'proper young man' who could handle his own dirty underwear."
    hilda @talkingmouth "Or his parents would come back from their missions and just stay with their damn kid."

    pause 2.0

    hilda @sad "...But that never happened."

    red @surprised "Wait, which one? Hilbert never grew up, or his parents never came back from their missions?"

    hilda @closedbrow talkingmouth "Both."

    hilda @sad "Guess it's not really his fault. I mean, he was practically raised by another kid. How do you {i}really{/i} grow up in an environment like that? The guy still wants to eat ice cream for every meal."

    red @surprised "Uh..."

    hilda @closedbrow talkingmouth "Actually, he got worse. Like, he was always single-minded, but now he's just obsessive as hell about his 'dream.'"
    hilda @angrybrow talkingmouth "Like, he doesn't even care if he eats or sleeps, because all he can think about is that damn dream of his. I sometimes wish I had a Munna I could just slam on his head and {i}eat{/i} that dream out of him!"
    hilda angry "And, y'know, it's one thing to have a goal and a plan to get there, but he sees the world like a child! It's all black and white with him, there's absolutely no grey!"
    hilda "He completely ignores truth in pursuit of his ideals! He thinks that just because he wants something more than anything else, it'll just {i}happen{/i} for him! That he doesn't have to work for it!"

    red @sadbrow talking2mouth "...Maybe that's because he's never had to work for anything? Because you've always done it for him?"

    hilda "[ellipses]"

    hilda -angry frownmouth @sad "Shit, I don't know. Maybe. But if so, what the hell can I do about it? I can't just stop, even if I wanted to. He needs help."

    redmind @thinking "It seems to me more like he's {i}desperately{/i} trying to get away from you... but what do I know?"

    red @closedbrow talking2mouth "Well... maybe you could work on saying 'no' more often to your non-Hilbert friends? So you're only running the life of one other person?"

    hilda @angrybrow talkingmouth "...No."

    red @happy "Hey, that's a good start!"

    hilda @closedbrow talking2mouth "Uh, no, I'm saying 'no' to you saying I should say 'no' more often."

    red @surprised "...Oh."

    hilda @sad "Like, I appreciate what you're trying to do, but this is who I am, and how I've been for nineteen years."
    hilda @happy "It's gonna take a shitload more than a pep talk with a hot farmboy to get me to just {i}stop{/i} all that. This isn't some kinda cheesy greeting card company movie."

    red @frownmouth "[ellipses]"

    red @happy "Then a shitload you shall receive."

    hilda @surprised "Eh?"

    red @talkingmouth "I've got some free time today. And if I can't stop you from taking care of everyone else, I can at least take care of you."

    hilda @surprised "I have no idea what you're talking about."

    red @happy "You will, though. Seeya later?"

    hilda @surprised "Uh... sure?"

    call clearscreens from _call_clearscreens_26

    scene hall_A2:
        zoom 0.7
    with Dissolve(2.0)

    pause 1.5

    python:
        playercharacter = "Hilda"
        oldinventory = copy.copy(inventory)
        oldpersonalstats = copy.copy(personalstats)
        oldparty = copy.copy(playerparty)
        oldpersondex = copy.copy(persondex)
        oldclassstats = copy.copy(classstats)

        inventory = {
            Item.BikeKeys : 1,
            Item.SpareTennisShoes : 1,
            Item.PersonalPlanner : 1,
            Item.MetalPolish : 1,
            Item.HiPowerFlashlight : 1,
            Item.TheGuidetoCollegeDating : 1
        }

        personalstats = {
            "Charm" : -7,
            "Knowledge" : 13,
            "Courage" : 56,
            "Wit" : 6,
            "Patience" : 33
        }

        playerparty = GetTrainerTeam("Hilda")
        persondex = copy.deepcopy(defaultpersondex)

        persondex["Hilda"] = {"Named" : True, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Self", "RelationshipRank": 0, "Events": [], "Mood": 0 }
        persondex["Hilbert"] = {"Named" : True, "Value" : 65, "Contact": False, "Sex": Genders.Male, "Relationship": "Parent", "RelationshipRank": 0, "Events": [], "Mood": 0 }
        persondex["Bianca"] = {"Named" : True, "Value" : 24, "Contact": False, "Sex": Genders.Female, "Relationship": "Roommate", "RelationshipRank": 0, "Events": [] }
        persondex["May"] = {"Named" : True, "Value" : 13, "Contact": False, "Sex": Genders.Female, "Relationship": ("Roommate" if IsBefore(1, 5, 2004) else "Former Roommate"), "RelationshipRank": 0, "Events": [] }
        persondex["Leaf"] = {"Named" : True, "Value" : 9, "Contact": False, "Sex": Genders.Female, "Relationship": ("Roommate" if IsBefore(1, 5, 2004) else "Former Roommate"), "RelationshipRank": 0, "Events": [] }
        persondex["Serena"] = {"Named" : True, "Value" : 14, "Contact": False, "Sex": Genders.Female, "Relationship": ("Roommate" if IsBefore(1, 5, 2004) else "Former Roommate"), "RelationshipRank": 0, "Events": [] }
        persondex[first_name] = {"Named" : True, "Value" : oldpersondex["Hilda"]["Value"], "Contact": False, "Sex": Genders.Male, "Relationship": "Friend", "RelationshipRank": 0, "Events": [] }
        persondex["Nate"] = {"Named" : True, "Value" : 13, "Contact": False, "Sex": Genders.Male, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [] }
        persondex["Bea"] = {"Named" : True, "Value" : 13, "Contact": False, "Sex": Genders.Female, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [] }
        persondex["Dawn"] = {"Named" : True, "Value" : 6, "Contact": False, "Sex": Genders.Female, "Relationship": "Acquaintance", "RelationshipRank": 0, "Events": [] }

        classstats = { 
            "Normal" : 0,
            "Fire" : 0,
            "Water" : 0,
            "Grass" : 0,
            "Electric" : 0,
            "Ice" : 0,
            "Fighting" : 8,
            "Poison" : min(100, AimLevel() + 5),
            "Ground" : 3,
            "Flying" : 0,
            "Psychic" : 0,
            "Bug" : 0,
            "Rock" : min(100, AimLevel() + 3),
            "Ghost" : 0,
            "Dark" : AimLevel() - 11,
            "Dragon" : 0,
            "Steel" : min(100, AimLevel() + 5),
            "Fairy" : 0
        }

    show screen currentdate

    narrator "A few hours pass. Eventually, you arrive back at your dorm, cookie-making groceries and clean laundry in tow."

    $ aron_name = GetTrainerTeam("Hilda", "Aron").GetNickname()

    hilda @closedbrow talkingmouth "Ah, shit, I can't carry all this and open the door... [aron_name]!"

    $ sidemonnum = GetTrainerTeam("Hilda", "Aron").GetId()

    $ PlaySound("Pokemon/Ball sound.ogg")

    $ renpy.music.queue("Audio/pokemon/cries/{}.mp3".format(sidemonnum), channel="altcry", loop=None)

    sidemon "[aron_name]!"

    hilda @sadbrow happymouth "Yeah, hi, sweetie. I know, I haven't taken you on a walk in forever. Would you mind helping me carry these bags?"

    $ renpy.music.queue("Audio/pokemon/cries/{}.mp3".format(sidemonnum), channel="altcry", loop=None)

    if (sidemon == 304):
        sidemon "A... ron..."
    elif (sidemon == 305):
        sidemon "Lai... ron..."
    elif (sidemon == 306):
        sidemon "Agg... ron..."

    hilda @angry "Hey! I could use some goddamn help here! I..."

    pause 2.0

    hildamind surprisedbrow frownmouth "What's that smell?"

    show red with dis: 
        xpos 0.0
        ease 0.5 xpos 0.5

    pause 2.0

    hilda surprised "[first_name]? What the hell were you doing in my dorm?"

    red @happy "Not much. Need some help with those bags?"

    hilda @angry "What? No! Answer the goddamn question!"

    red @closedbrow talking2mouth "Mm. I would, but..."

    red @happy "I'm trying this new thing where I say 'no' to my friends. So... no!"

    $ PlaySound("fading_footsteps.ogg")

    show red:
        ease 0.25 xpos 1.5

    hilda angry "Hey! Get back here, you bastard! Answer me!"

    hilda "[ellipses]"

    hildamind sad "What the hell...?"

    $ renpy.music.queue("Audio/pokemon/cries/{}.mp3".format(sidemonnum), channel="altcry", loop=None)

    if (sidemon == 304):
        sidemon "Aronnnn...?"
    elif (sidemon == 305):
        sidemon "Laironnnn...?"
    elif (sidemon == 306):
        sidemon "Aggronnnn...?"

    hide hilda 
    show dorm_A
    with dis

    narrator "You slowly push open the door, and the strong scent of freshly-baked cookies quickly assails you."

    if (IsBefore(1, 5, 2004)):
        show leaf at midrightside with dis
        show may at farrightside with dis
        show serena at midleftside with dis
        show bianca at farleftside with dis

        bianca "Heyyyyy, Hilda! Welcome back!"

        hilda @surprised "...What the hell happened here?"

        leaf @talking2mouth "Oh, [first_name] dropped by."

        hilda @angry "I can tell that! What did he {i}do{/i}?"

        may @happy "Oh, he brought a bunch of groceries we needed! And he helped me bake and restock the cookie plate."
        leaf @closedbrow talkingmouth "Thank god. I was minutes away from a total cookie-less meltdown."
        serena @happy "Yes, he was quite charming. He also helped me research restaurants in Inspira. We found a couple together that should suit my plans quite nicely."
        bianca @happy "Yeah! And he took my little Moony on a walk while I was helping Cheren put up posters! I think she really liked being able to stretch her legs!"
        leaf @sarcastic "Munna? Walk? Legs?"
        serena @closedbrow talking2mouth "Oh, and he said he checked in on Hilbert. And that Hilbert has not, ah, 'choked to death on his own foot.' Apparently, he took Hilbert out for ice cream."

    else:
        show bea at leftside
        show bianca at farrightside
        show nate at midleftside 
        with dis

        bianca "Heyyyyy, Hilda! Welcome back!"

        hilda @surprised "...What the hell happened here?"

        bea @talkingmouth "[first_name] dropped by."

        hilda @angry "I can tell that! What did he {i}do{/i}?"

        bea @happy "He brought many groceries that we were running low on. The cookie jar has been replenished, thankfully."
        nate @happy "Yeah, and while he was here, he helped me find {i}just{/i} the piece of information on Unovan legends I was looking for. Guess you could call him my own genie, huh?"
        bianca @happy "Yeah! And he took my little Moony on a walk while I was helping Nate with his research! I think she really liked being able to stretch her legs!"
        bea @surprised "Munna? Walk? Legs?"
        nate @closedbrow talking2mouth "Oh, and he said he checked in on Hilbert. And that Hilbert didn't, uh, 'choke to death on his own foot.' Guess he took Hilbert out for ice cream?"

    $ ValueChange("Hilbert", 3, -0.5, adjustoldpersondex=True)

    narrator "You hear a 'ping' somewhere in your subconscious, as you suspect [first_name] has just gained three 'points' with Hilbert."
    narrator "...Whatever that means." 

    hilda @veins angry ".{w=0.5}.{w=0.5}.{w=0.5}That's. Very. Generous. Of. Him."

    bianca @happy "Right? It's so cool he just decided to do all this stuff for us for no reason!"

    pause 2.0

    hildamind @angrybrow frownmouth "That bastard. I'm going to kill him. What does he think he is, my... {color=#0048ff}caretaker{/color}?"

    python:
        inventory = oldinventory
        personalstats = oldpersonalstats
        playerparty = oldparty
        persondex = oldpersondex
        classstats = oldclassstats
        playercharacter = None
        RelationshipRankUp("Hilda", "Caretaker", 1)

    return

label Hilda2:
    scene sportsfield 
    show hilda angry veins sweat:
        block:
            xpos -0.2 xzoom -1
            linear 1.0 xpos 1.2
            pause 1.0
            repeat
    with Dissolve(2.0)
    $ renpy.music.queue("Audio/Music/Nuvema2_Start.ogg", channel='music', loop=None, fadein=0.0, tight=None)
    $ renpy.music.queue("Audio/Music/Nuvema2_Loop.ogg", channel='music', loop=True, tight=None)

    narrator "You've been going on an impromptu run around the campus grounds when you suddenly spot a dust tornado on the soccer field behind the baseball field. This place catches your interest, since you'd never seen it before."
    narrator "Also of interest is Hilda, running around the field. As the sweat flies off her brow, you notice that the way she's running is very aggressive." 
    narrator "She brings her feet down with a lot of weight, as though she's trying to crack the ground."

    pause 0.5

    narrator "You stay and watch for a while, unsure if you should interrupt."

    pause 0.5

    narrator "Eventually, your curiosity gets the better of you, given Hilda's aggressive running style had carved deep divots in the sandy field."

    show hilda surprisedbrow frownmouth -veins with dis:
        ease 0.5 xpos 0.5

    red @talkingmouth "Hey, Hilda."

    if (not HasEvent("Hilda", "Level2SceneVer2")):
        hilda @happy "Oh, shit, good to see you!"

        red @surprised "Really?"

        hilda @surprised "Uh, yeah? What do you mean, 'really'?"

        red @sadbrow talkingmouth "Well... I just meant, you know, with the whole 'powers' thing..."

        hilda @talkingmouth "Water under the bridge."
        hilda @happy "I'll be real, I was {i}kinda{/i} on the fence at first, but after you explained the whole situation during the Quarter Qlashes..."
        hilda @sadbrow talkingmouth "I mean, how could I hold it against you? It's seriously effed up what you went through. I can't believe Cheren..."

        red @sadbrow talkingmouth "Thanks for being so understanding."

        hilda @sadbrow smirkmouth "That's me. Understanding to a fault." 
        hilda @talkingmouth "Anyway, how long have you been there?"

    else:
        hilda @surprised "[first_name]? How long have you been there?"

    red @talkingmouth "Not long. Just a couple minutes."

    hilda @closedbrow angrymouth "Shit, sorry about that."

    red @happy "I just said I wasn't here long!"

    hilda @talking2mouth "Yeah, but you're a nice guy. I know you're probably understating it."

    pause 0.5

    hilda angry "Speaking of which!"

    redmind @sad "Oh, great. I'm about to get another tongue-lashing for helping her out with her insane workload."

    hilda -angry sadbrow frownmouth @closedbrow talkingmouth "I, uh, think I might have been a bit ungrateful, recently."

    red @surprised "Huh?"

    hilda @closedbrow talking2mouth "Don't 'huh!' me. You know exactly what I'm talking about. All that stuff you've been doing, and I've just been bitching at you about it."
    hilda @sadbrow talking2mouth "It's like, jeez, Hilda, if this is what you do when someone tries to help you out, no shit you've got so much on your plate."

    red @sadbrow talkingmouth "The thought {i}had{/i} occurred to me."

    pause 1.0

    hilda -sadbrow -frownmouth -sweat @talking2mouth "Anyway, since you've cleared up so much time for me, I've actually been able to, uh, get back to some of my earlier hobbies. Which is my explanation for... this."

    narrator "Hilda waves vaguely at the torn-up soccer field."

    red @talking2mouth "Yeah, that doesn't really explain anything. I kinda figured you just hated soccer?"

    hilda @surprisedbrow talkingmouth "Huh? Hate it? No. I mean, I'm not a fan of soccer, but I wouldn't destroy the field over it."

    pause 0.5

    show hilda sadbrow with dis

    red @confused "So, why {i}did{/i} you destroy the field?"

    hilda @talking2mouth "Guess I got, uh, a bit carried away. I was just blowing off some steam. Running. Good tennis training." 
    hilda @talking2mouth "People think about their hands and wrists, and sure, that shit's important, but being fast on your feet is most of the strategy."

    red @talkingmouth "You said earlier that you didn't think you'd have enough time to join the Tennis Team?"

    hilda sadbrow @happy "And I was {i}damn{/i} right. Don't want to fall out of practice, though. There's gotta be a day..."

    pause 1.0

    narrator "Hilda suddenly pauses and looks at Inspira City wistfully."

    red @sadbrow talkingmouth "Hilda?"

    hilda @talking2mouth "There's gotta be a day when all this is over, and I can pick up my own life again."

    pause 0.5

    narrator "You've talked with Hilda a decent amount at this point, but you'd never heard her say something so heavy with bitterness."

    pause 0.5

    hilda @surprisedbrow talkingmouth "Shit, sorry! Should've kept the gas cap on that one."

    red @talkingmouth sadbrow "Hey, Hilda. It's alright to want things for yourself."

    hilda @talking2mouth "Yeah, I know that. It's just... {i}sigh.{/i}"

    hilda @closedbrow talkingmouth "Taking care of Hilbert's been my number one priority for so long. I'm worried I'm going to forget what I was before that, when..."
    hilda -sadbrow frownmouth @sad "When it's over."

    narrator "Her tone of voice somewhat betrays her lack of faith in 'it' ever being 'over.'"

    hilda surprised @happy "But you don't want to hear me whine about that, right? Let's--"

    red @talking2mouth "I do."

    pause 0.5

    red @happy "And it's not whining. You're under a lot of pressure. You deserve to have some stress relief. Even if you release that stress by kicking the ass of a soccer field, or telling me about what's got you down."

    pause 0.5

    hilda -surprisedbrow -frownmouth -surprised @closedbrow talking2mouth "You're not bad with words, Farmboy. Anyone ever tell you that?"

    red @happy "Oh, yeah, Cheren told the entire school, and I'm still dealing with {i}that{/i}."

    hilda @sweat closedbrow talkingmouth "Point taken."
    hilda @sadbrow talking2mouth "Well, assuming you're not bullshitting me, and you {i}actually{/i} do want to hear about the kind of shit I've gotta put up with..."

    pause 1.0

    hilda @closedbrow talkingmouth "...You know how Hilbert has this 'dream' of his...?"

    red @talking2mouth "Yeah. Uh. He, uh, told me about it."

    hilda @surprised "No shit?!"

    red @happy "Yes shit."

    hilda @talking2mouth "Well, that cuts a hell of a lot of the vagueness and ambiguity out of this conversation."

    pause 1.0

    show hilda angry:
        ease 0.5 ypos 1.1 zoom 1.2

    show sportsfield with vpunch

    hilda "So what the {b}fuck{/b} is that about, huh?!"

    red @winkeyes angryeyebrows talking2mouth sweat "Uh..."

    hilda "That {i}kid{/i}'s been holding onto this grudge for over a decade! And I'm supposed to pretend like I'm worried about him because he {i}doesn't eat{/i}, or whatever!"
    hilda frownmouth @angry "No! I'm worried about him because he's been on a goddamn suicide mission for {i}most{/i} of his life!"

    pause 2.0

    hilda @closedbrow talking2mouth "Sorry. I'm not mad. Not at you. Just under a lot of stress."

    red @sadbrow talking2mouth "I can't begin to imagine."

    hilda @sadbrow talking2mouth "You're a smart guy. I bet you can."

    red @frownmouth sadbrow "[ellipses]"

    hilda @sadbrow talking2mouth "...What do I do?"
    hilda frownmouth @talkingmouth "For years, I always thought he'd just forget this 'dream' of his. I mean, it's impossible, right? So there's no way he could ever actually {i}do it.{/i}"

    pause 0.5

    hilda @closedbrow talkingmouth "That's what I thought. But... recently..."
    hilda @talkingmouth "He's become strong. So much stronger. I mean, he got onto the Battle Team. He's actually talking to other people. And I'm really happy for him. But that makes me..."
    hilda @closedbrow talkingmouth sweat "I'm scared, [first_name]. I'm seriously scared that he'll succeed. And then I'll lose him."

    pause 0.5

    hilda frownmouth @sadbrow talkingmouth "{size=30}Shit.{/size}"

    red @sadbrow talking2mouth "...What does he mean to you?"

    hilda @talkingmouth "He's my best friend. He's a callous, irreverent, prick, sometimes, but he's still a kid at heart."
    hilda @sadbrow talkingmouth "And I don't want to see that kid die. Or do something that makes life not worth living."

    red @talking2mouth "...I'm sorry. I told Hilbert I'd help him with his dream."

    hilda @sadbrow talking2mouth "It's alright. I did the same shit. You were just hoping you could get close to him and talk him out of it, right?"

    red @sweat talking2mouth closedbrow "Yeah."

    hilda @sadbrow talking2mouth "Good strategy. But two decades isn't enough time, I guess. I guess we're just enablers."

    pause 0.5

    red @talkingmouth "You've done everything you could, Hilda."

    hilda @talkingmouth "Yeah. But... I can't help but feel like maybe someone else could do something better."

    red @talking2mouth "I can't believe that. You care {i}so{/i} much about him, about everyone you meet. If you can't do it, who could?"

    hilda @sadbrow talking2mouth "...His actual parents."

    red @surprisedbrow frownmouth "Hm?"

    hilda @talking2mouth sadbrow "For those first few years, he was the one who looked out for me. If you can believe that."

    red @confused "Admittedly, I {i}am{/i} having difficulty seeing it."

    hilda @talking2mouth "Hilbert's family was a loving one. Their house was always full of smiles and warmth. Mr. & Mrs. von Schwarzdrachen loved their kid. You should've seen their Snowfall Day celebrations."
    hilda @closedbrow talking2mouth "I remember one time Hilbert wanted to build a cardboard box fort. His parents built him a castle out of cardboard. Multiple floors, too. They gave him a little cardboard crown, and declared him the 'Prince of Unova.'"
    hilda @happy "You should've seen him beam, then, [first_name]. Swear to God, his smile could melt ice."

    pause 0.5

    hilda @talkingmouth "I'd go over to their house whenever I could."

    pause 0.5

    red @talking2mouth "You said that his parents were often gone on missions, right? For some Pokémon-rights organization?"

    hilda @talkingmouth "Yeah. But that doesn't mean they didn't love him."
    hilda @sadbrow talkingmouth "I mean, my Dad was always home, but the only thing our house was full of was crushed beer cans and pin-ups of Diantha."

    red @closedbrow talking2mouth sweat "Eesh. I'm sorry."

    hilda @talkingmouth "Don't get the wrong idea. He wasn't a creep or anything. He was just a biker who ended up with a kid he didn't really want."
    hilda @sadbrow talking2mouth "That's what happens when you're a heartbreaker, I guess. Eventually, one of those hearts breaks you back."
    hilda @talking2mouth "There were some fun times, though. He taught me how to ride. And he caught me my first Pokémon."

    pause 0.5

    hilda @sadbrow talkingmouth "But it's hard to feel the love in a house where you know your parent would be happier if you didn't exist."

    red @angrybrow talking2mouth "I {i}cannot{/i} believe there's anyone in the world who would be happier if you didn't exist."

    hilda @talking2mouth "Sometimes I wonder if that's how Hilbert thinks of me..."

    pause 0.5

    hilda @closedbrow talkingmouth "Anyway, that's why I spent so much time over at his house. Didn't want to smell like beer, and there's only so many times you can deep-clean a house in a week."
    hilda @talking2mouth "Hilbert's house was my safe space. My respite. When it was just him, his parents, and me, I could forget everything I came from and believe in an ideal future."
    hilda @sadbrow talkingmouth "Of course, you already know how this story ends."

    pause 0.5

    hilda @talkingmouth "Hilbert's parents got really involved with Team Plasma. And then... well, you probably heard the reports."

    pause 0.5

    if (not HasEvent("Hilbert", "FerrisWheel") and GetRelationshipRank("Hilbert") < 2):
        red @sadbrow talking2mouth "I don't think I did. And I'm not sure what Team Plasma is."

    else:
        red @sadbrow talking2mouth "I don't think I did. And I've only heard the name of Team Plasma from Hilbert."

    hilda @surprised "No shit? Damn, you have {i}seriously{/i} never watched TV."

    red @sadbrow talkingmouth "If this is a Unovan thing, it's pretty unlikely that Kantonian TV would cover it, anyway."

    hilda @talking2mouth "Fair."

    pause 0.5

    hilda @closedbrow talkingmouth "Team Plasma attacked Opelucid."

    pause 0.5

    if (GetRelationshipRank("Nate") >= 2):
        red @sweat sadbrow talkingmouth "...I heard."

        hilda @closedbrow talkingmouth "When they attacked, they attacked with this massive aircraft that had these crazy... like... I don't even know what to call them. Weapons?"

    else:
        red @sweat sadbrow talkingmouth "I don't know what that is."

        hilda @closedbrow talking2mouth "{size=30}Farmboy...{/size} It's a big city in Unova. Dean Drayden's hometown."
        hilda @closedbrow talkingmouth "Anyway, when they attacked, they attacked with this massive aircraft that had these crazy... like... I don't even know what to call them. Weapons?"
    
    hilda @sadbrow talking2mouth "They were firing indiscriminately. As a show of force, before they made demands. That's what the news said."
    hilda @closedbrow talkingmouth "And... Hilbert's parents were at home when something from the airship froze the place solid."
    hilda @sad "In a city of hundreds of thousands of houses, where the terrorists were firing randomly, they landed a direct hit on Hilbert's home. One of only two buildings that were hit directly."

    pause 1.0

    hilda @sad "They died."

    pause 1.0

    red @surprised "Wait. I thought you lived in Nuvema Town?"

    hilda @sadbrow talking2mouth "We did. {i}After{/i} our homes were destroyed."

    red @sadbrow talking2mouth "Oh."

    hilda @talkingmouth "My Dad knew a woman who was looking to adopt, and she became Hilbert's guardian."
    hilda @talking2mouth "Having a literal binder of booty call numbers came in handy, I guess."

    red @talkingmouth "...Sounds like he pulled himself together when it counted."

    hilda @talkingmouth sadbrow "Yeah. I'm glad he didn't get iced."

    pause 1.0

    red @talkingmouth "I'm sorry for everything you've been through."

    hilda @sadbrow talking2mouth "Hey, you didn't do any of it."

    red @sadbrow talkingmouth "Sympathy, not culpability."

    pause 0.5

    hilda @talkingmouth "Mind if I ask {i}you{/i} a question?"

    red @surprisedbrow frownmouth "Hm? No, of course not."

    hilda @closedbrow talkingmouth "How are you, uh, paying for Kobukan? From what you've told me, it sounds like you didn't really come from money."

    red @sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."#FIX THIS: Update when you learn how you're paying for Kobukan. 

    hilda @surprised sweat "Shit, you don't know?"

    red @happy sweat "It's a work in progress."

    hilda @closedbrow talkingmouth "Crap. Sorry for asking."

    red @confused "It's fine. But what about you and Hilbert?"

    hilda @talking2mouth "Hilbert's guardian is pretty wealthy. Comes from a professorial family with a pretty cushy legacy."
    hilda @talkingmouth closedbrow "And, uh, it turns out that if your house is crushed and your family is killed in a terrorist attack, you're entitled to part of their assets when they get taken down."

    pause 0.5

    red @sweat talking2mouth "I don't think that'll work for me."

    hilda @sadbrow talking2mouth "I wouldn't recommend it."

    hilda @talkingmouth "Anyway, I got in because my Dad invented Triple Battles."

    red @surprised "What?!"

    show homeroom at sepia
    show flashback
    with dis

    $ renpy.pause(1.0, hard=True)

    show leaf uniform happy at sepia behind flashback with dis

    leaf "Yeah, there's tons of differences! People from Orre pretty much only do double battles. Unovan trainers love their Triple Battles." 
    
    show blank with splitfade

    hide leaf
    hide homeroom
    hide flashback
    hide blank with dis

    red @talkingmouth "Leaf told me that those are all the rage in Unova."

    hilda @closedbrow talking2mouth "She probably heard that from me. But yeah, it's true. You wouldn't think it'd take a fucking rocket scientist to put together that if sending out two Pokémon at once is a thing, you can also send out three."
    hilda @talking2mouth "Still, he was the first person to think of it. So credit where credit, and shit."
    hilda @sweat closedbrow talkingmouth "We don't talk about his other idea for 'rotation battles.'"

    pause 0.5

    red @talkingmouth "I guess I've got one more question."

    hilda surprisedbrow frownmouth @neutralbrow talking2mouth "Fire away, Columbo."

    red @confused "When I first arrived at this school, Hilbert was hiding from you. Like, {i}literally{/i} hiding. What was his plan there? Did he think he could just go to the same school as you and not be found?"

    hilda @sadbrow talking2mouth "...Ah. So, uh... I kinda didn't tell him that I was also coming here."

    red @confused "Huh?"

    hilda @closedbrow talking2mouth "Yeah. {i}I{/i} was the one who thought I could go to the same school as him and not be found."

    red @unamusedbrow talking2mouth "You're kidding me."

    hilda @closedbrow talking2mouth "Hey, I thought if I was here, but he didn't know, I might be able to stop looking after him every single second, but would still be close enough to watch over him if he really needed it."

    red @unamusedbrow unamusedmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    hilda @angrybrow talkingmouth "Alright, yes, I was a dumbass! What do you want me to say?"

    red @closedbrow sweat talkingmouth "I wasn't saying that."

    hilda @closedbrow talking2mouth "I know you were thinking it, though."

    red @closedbrow talking2mouth "I decline to comment."

    hilda happy "Oh, you ass!"

    pause 2.0

    hilda -happy @sadbrow talking2mouth "...Hey. Thanks for this. It made me feel a lot better."

    red @sadbrow talking2mouth "You deserve it."

    hilda @closedbrow talking2mouth "Flatterer."
    hilda @talking2mouth "But... seriously. I don't think 'better' is a strong enough word. I mean, just chatting with you makes me feel... uh..."
    hilda @closedbrow talkingmouth "Okay, don't look into this, but 'wanted' is the only word coming to mind."

    red @talkingmouth "Of course you're wanted."

    hilda @sadbrow talking2mouth "Yeah, 'dead or alive.'"

    pause 2.0

    red @confused "...You know, I never got that song."

    hilda @surprisedbrow frownmouth "Huh?"

    red @talkingmouth "The singer's talking about a 'Steel Horse', right?"
    red @closedbrow talking2mouth "But there aren't any Steel-type Horse Pokémon."

    hilda @surprisedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
    hilda @surprisedbrow talkingmouth "You're fucking with me."

    red @confused "Not to my knowledge?"

    hilda happy @talking2mouth "The 'steel horse' he was talking about is a motorcycle! It's a metaphor!"

    red @surprised "Oh!"
    red @closedbrow talking2mouth "I probably could've figured that out, given enough time..."

    hilda @talkingmouth "You're a fun guy, [bluecolor]farmboy{/color}."
    hilda -happy @sadbrow talking2mouth "Keep it up."

    red @talkingmouth "Sure thing, city girl."

    $ aronname = pokedexlookup(GetTrainerTeam("Hilda", "Aron").Id, DexMacros.Name)

    hilda @closedbrow talking2mouth "Now, I gotta stamp the ground back down, so unless you feel like stomping around on stuff, I'm just going to have my [aronname] run up and down the field for a bit."

    red @talkingmouth "I'll leave you to it."

    hilda sadbrow @talking2mouth "Seeya, [first_name]."

    $ oldrelation = GetRelationship("Hilda")
    $ persondex["Hilda"]["Relationship"] = "Farmboy"
    $ persondex["Hilda"]["RelationshipRank"] = 2

    $ PlaySound("sav.ogg")

    narrator "Your heart shifts as you feel your relationship with Hilda evolve from '{color=#0048ff}[oldrelation]{/color}' to '{color=#0048ff}Farmboy{/color}'!"

    hide hilda with dis

    return
