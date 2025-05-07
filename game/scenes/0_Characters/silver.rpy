label Silver1:
    if (not IsBefore(1, 5, 2004)):
        $ persondex["Silver"]["Events"].append("Level2SceneVer2")

    scene abandonedhouse
    with Dissolve(2.0)
    stop music fadeout 1.5
    $ renpy.music.queue("Audio/Morning_ambience.ogg", channel='music', loop=True, fadein=1.5, tight=None)

    show roughneck at night with dis

    red night "...Hey."

    roughneck @angry "You here to talk to the boss?"

    red @talkingmouth "Sure am. Mind letting him know I'm here?"

    roughneck @angry "Tch."

    hide roughneck with dis

    narrator "You've come back to the city to talk with Silver, carefully retracing your steps until you find your way to the abandoned house that Silver lives in."

    show silver angry at night with dis

    silver "The hell do you want?"

    red @confusedeyebrows talking2mouth "...Um. To talk?"

    silver -angry @sad "Right. Sorry. Force of habit."

    stop music fadeout 1.5
    queue music "audio/music/DontEverForget_start.ogg" noloop
    queue music "audio/music/DontEverForget_loop.ogg"

    pause 1.0

    silver @talkingmouth "Well. What do you want to talk about?"

    red @talkingmouth "I want to talk about you."

    pause 1.0

    silver @sad "There's nothing to say."

    if (not IsBefore(1, 5, 2004)):
        silver @talkingmouth "If it's about the mind-powers stuff... whatever. I'm obviously outnumbered when it comes to not trusting you." 
        silver @closedbrow talkingmouth "Anyway, my position in the Disciplinary Committee lets me make sure you don't get too powerful."

        pause 1.0

        silver @happymouth "Remember, if I see you trying to start your own little gang, there's a Crobat with your name on it."

        red @confused "Noted. Terrifying. But that wasn't what I wanted to talk about at all."

        silver @closedbrow talkingmouth "Yeah? What, then?"

    red @confused "Silver. You live in the city, in a run-down shack, hiding from the cops, with twenty older guys who all treat you like you're their boss."

    pause 1.0

    silver @closedbrow talkingmouth "...Yeah."

    red @happy "Can you honestly tell me there's no story there?"
    red @talkingmouth "If you say that, I'll believe you. But I don't think you're going to say that."

    pause 1.0

    silver @sad "Fine. There's a story. But I'm not telling it."

    red @confused "Why not?"

    silver @angry "Well, aren't you all goddamn nosy all of a sudden!"

    red @sad "{w=0.5}.{w=0.5}.{w=0.5}."

    silver @sad "Sorry."

    red @talking2mouth "Silver, I just want to get to know you. In a stadium of hundreds of people, you were the only person who stood up to help me when Lance was being a dick."
    red @talking2mouth "I want to know why. {i}Why{/i} you helped me. What gave you the motivation to."
    red @happy "I want to know {i}who{/i} helped me. Who the Silver that stood up and acted as my shield was...{w=0.5} {i}is.{/i}"

    silver @smilemouth "{w=0.5}.{w=0.5}.{w=0.5}."
    silver @happymouth "Well, don't you think you're important?"

    red @surprised "Huh?"

    if (IsBefore(1, 5, 2004)):
        silver @talkingmouth "I wasn't doing it for you. You seem like a nice guy. You'd probably deserve it, if I did defend you."
    else:
        silver @talkingmouth "I wasn't doing it for you. Powers aside, you're nice enough, and you'd probably deserve it if I {i}did{/i} do it for you."

    silver @angry "But I was doing it for your Pikachu."

    if (IsBefore(1, 5, 2004)):
        $ renpy.music.play("Audio/Pokemon/pikachu_question.ogg", channel="altcry", loop=None)
        pikachu neutral_4 "Pika?"

    else:
        $ renpy.music.play("Audio/Pokemon/pikachu_question.ogg", channel="altcry", loop=None)
        libpikachu @surprisedbrow frownmouth "Pika?"

    silver @angrybrow sadmouth "My entire life, I've heard weak men blame others for their incompetence." 
    silver @sad "People just can't take any goddamn {i}responsibility{/i} for their own failure."
    silver "I'm... better, now. But the life I lived before... when I lived with my Dad..."

    pause 1.0

    silver @sad "Some mistakes you can't roll back."
    silver @closedbrow talkingmouth "But I can dream. And work as hard as I can to bury my past in the new me."

    pause 1.0

    silver @sad "And... I don't want others making the same mistakes I have. So... when I see or hear a trainer blame a Pokémon for their failure..."
    silver @angry "I need to let them know what they're doing wrong."

    pause 1.0

    red @surprised "Wait, you were trying to {i}help{/i} Lance?!"

    silver @angry "I think we've established at this point that I'm not exactly the picture of eloquence! Yes, I was trying to help the bastard."

    red @talkingmouth "...You might want to work on your communication skills."

    silver @sad "If that's really all you came here to tell me, you can piss off back to the campus, now."

    red @sadbrow happymouth "C'mon, Silver. Work with me, here."

    silver @smilemouth "{w=0.5}.{w=0.5}.{w=0.5}.You're a patient guy."

    red @happy "One of my many positive qualities."

    if (IsBefore(1, 5, 2004)):
        silver @talkingmouth "How can I work with you, then? I already agreed to help you get elected. You agreed to beat up my goons. Not sure what else we can do for each other."
    
        red @talkingmouth "Well, if we're going to be on the Battle Team together, we could stand to learn a little bit more about each other, right?"

    else:
        silver @talkingmouth "How can I work with you, then? I already agreed to help you get elected. And we all know how well that worked. Not sure what else we can do for each other."

        red @talkingmouth "What you did to help me out that day... I mean, it was kinda crazy. It probably would have worked, if Cheren hadn't... you know. Where'd you come up with that? Staging an attack on the school?"

        silver @sad "{w=0.5}.{w=0.5}.{w=0.5}."

    silver @closedbrow talkingmouth "I've talked enough. Tell me more about yourself."

    red @happy "Sure! So, I'm from a little town called Pallet Town, in Southwest Kanto. My Pikachu here is called [pika_name], and he was my first friend."
    red @closedbrow talking2mouth "Um... I lived with my Mom my whole life. My father wasn't in the picture--he died when I was young. We were pretty poor. Not 'cause he died, even before that."

    pause 1.0

    silver @talkingmouth "What kind of place was Pallet Town?"

    red @happy "Small!"
    red @talkingmouth "Peaceful, though. The people were kind. The grass was green, and the ocean was just south of us. And everyone knew everyone."

    pause 1.0

    red @sad "The one bad thing was... well, everyone knew everyone. It would be pretty much impossible to get a fresh start, there. Anything you do sticks with you until you move away."

    silver @talkingmouth "Mm. I get that."
    silver @sad "I grew up in Kanto as well, actually. In Celadon."

    red @happy "Really? Huh! I would've thought Celadon would be big enough to find a new start wherever you turned."

    silver @angrybrow happymouth "Not when you never leave your... {i}house.{/i} I probably got fresh air three times for the first twelve years of my life."
    silver @talkingmouth "And one of those times was when we were evacuating the building. Alarms flashing, cops pulling up... heh."

    red @surprised "Geez! Sounds intense. Was there a fire?"

    silver @sad "Something like that."
    silver @talkingmouth "...So, your Pokémon have always trusted you, huh?"

    red @happy "Pretty much. I mean, I've had [pika_name] for a long time, but I think he trusted me when we first met."

    silver @sad "And you don't have... you don't have any skeletons in your closet? No memories you want to bury in the dark?"

    red @confused "Uh... no."

    if (not IsBefore(1, 5, 2004)):
        red @talkingmouth "Well, there {i}was{/i} the whole Frienergy thing, but... that's off my chest now, so... besides that, I don't think so."

    silver @closedbrow talkingmouth "Damn."

    red @confused "Damn? Why?"

    silver "[ellipses]"

    silver @talkingmouth "You... are good."

    red @happy "Aw, thanks."

    silver @angry "Shut up. I mean you're {i}good.{/i}"
    silver @closedbrow talkingmouth "You're kind, you know all kinds of shit about Pokémon, you're a great battler, you're fit, and you can make friends with anyone."

    red @talkingmouth "Wow. Are you just writing my dating website profile for me? Make sure to note I like guys, too."

    silver @sad "Ugh... of course you do."
    silver @talkingmouth "Look, no-one has all that unless they're trying to make up for something. There's gotta be something in your past. {i}Something.{/i}"
    silver @angry "Like, you used to be a fatass who didn't know anything about Pokémon, and you had no friends, right?"

    red @closedbrow talking2mouth "Well... there was a time when I didn't have any friends, yeah. After that, I definitely became a lot more social."
    red @talkingmouth "Or at least a lot more willing to take risks. Socially."

    silver smilemouth @talkingmouth "Hmph. Knew it."

    red @happy "Hey, is that a smile?"

    silver @talkingmouth "Yeah. It's a hell of a relief to hear that you aren't as perfect as I thought you were. What's this all in service of, anyway?"

    red @closedbrow talking2mouth "Huh?"

    silver @sad "Why bother being everything you are? It'd be so much easier to just... hide away, right? Be mediocre. Fade into the background."

    red @closedbrow "{w=0.5}.{w=0.5}.{w=0.5}."
    red @talking2mouth "I want to be a Champion."

    silver -smilemouth @talkingmouth "...So? Not like you need friends to do that. Look at Lance. Bastard's done it twice, and what does he have going for him, besides an overcompensatory hairstyle?"

    red @sadbrow happymouth "Maybe he doesn't need friends. But I do."

    silver @closedbrow sadmouth "Psh."

    red @happy "I'm serious. I'm nothing without my friends. And I'm not being modest. I freeze up. I can't speak for myself. I can barely remember anything about Pokémon, and everything I know about battling goes out the window."
    red @closedbrow talking2mouth "I spent four years in Pallet Town without any friends, and..."
    red @sadbrow happymouth "Well, I can barely remember anything I did then. I think I was kinda just in a dull haze."

    if (not IsBefore(1, 5, 2004)):
        silver @sad "So... like up there on the stage, then..."

    silver @talkingmouth "...Well, you need to get over that."

    red @angry "Oh, gee, thanks. Wish I'd thought of that."

    silver @closedbrow talkingmouth "If you can't do it for yourself, do it for your Pokémon. They're relying on you. And if you can leave this world with at least one Pokémon you haven't disappointed, then you've won."

    red @talkingmouth "What about one human?"

    silver @sad "Yeah, that's... not going to happen."

    red @happy "I dunno. I think you can do it."

    silver @happymouth "Then prepare to be disappointed."

    pause 1.0

    red @confused "Was that a joke?"

    silver @smilemouth "Are you so surprised? I'm a funny guy."

    red @happy "I'm kinda surprised, yeah! I didn't know you told jokes."

    silver @talkingmouth "...Most people don't get them. My humor's a bit dry."

    red @talkingmouth "Well, what's your dream? International comedian?"

    silver @closedbrow talkingmouth "...Whenever I close my eyes at night, I only ever have one dream." 
    silver @sad "And I dream of an absolution."

    if (IsBefore(3, 6, 2004)):
        red @happy "...C'mon. You're, what, eighteen?"

        silver @talkingmouth "Seventeen."
    else:
        red @happy "...C'mon. You're eighteen."

    red @happy "What do you have to be absolved of?"

    silver @angry "Are you so privileged that you think just because you've never had a nightmare, they don't exist?"

    pause 1.0

    silver @closedbrow talkingmouth "I've got a lot of nightmares in my dream journal, red. I can't tear out those pages. I can only keep writing."

    pause 1.0

    silver @talkingmouth "So that's my dream. I'll never be able to forget what I was. But if I can outweigh it, then maybe I can die happy."

    red @closedbrow talking2mouth "Hm."
    red @talkingmouth "So, your first step in this absolution is to try and rehabilitate your father's former employees."

    silver @talkingmouth "Yeah, these idiots."

    red @confused "...That's not normally the kind of thing the son of a CEO has to do, even if his Dad's company fails {i}really{/i} hard."

    silver @happymouth "Yeah, well, my Dad's company was always a {i}family{/i} business. Like he liked to remind me."

    red @closedbrow talking2mouth "What's your end-goal with these guys?"

    silver @surprised "Huh?"

    red @closedbrow talking2mouth "Like, what's your rehabilitation plan? What goalposts are you setting? How long do they have? What's your exit strategy?"

    silver @angry "I yell at them when they act up."

    red @talking2mouth "Not much of a plan."

    silver @closedbrow talkingmouth "No, not much of one."
    silver @sad "I guess I'm just kinda hoping that... one day... they'll just wander away, and not be my problem anymore."
    silver @closedbrow talkingmouth "Maybe when I'm not looking, they'll get a long-term job somewhere. Maybe even buy an apartment and leave."

    pause 1.0

    silver @talkingmouth "They bring me a lot of money. I don't ask where it comes from. I just try to invest it--get it out of this house--as soon as I can."

    silver @smilemouth "Here, take a wad."

    $ PlaySound("Get.ogg")

    $ money += 2000

    narrator "Silver tosses you a brown paper bag filled with $2,000."

    red @surprised "W-woah. I don't really like to accept money from... wait, where'd this come from?"

    silver @sad "Didn't you hear? I said I don't ask where it comes from."

    pause 1.0

    silver @sad "It's more likely they'll try to rob a cop and get put away for a couple years. Still not my problem."

    red @closedbrow talking2mouth "You've been talking a lot about how your Dad's employees are... well, criminals. And I first met them when they stole Tia's hat."

    pause 1.0

    silver @talkingmouth "Yeah."

    red @sadbrow happymouth "What... kind of business did your Dad run, exactly?"

    pause 1.0

    silver @talkingmouth "Let me put it this way."
    silver @sad "When he did well, he was the only one who was happy about it. And when he went 'out of business...' well, no-one cared."

    red @talkingmouth "...Silver."

    silver @sad "He was a bastard, but he was the only one who knew how to handle these people. And they're disappointed in me, because I'm not as cruel or tough as he was."
    silver @talkingmouth "Isn't that fucked up?"

    red @sadbrow happymouth "...You have trouble enforcing discipline, huh?"

    silver @closedbrow talkingmouth "Yeah, you could say that."
    silver @sad "I mean, some of these guys knew me when I was in diapers. The fact they live in my house now doesn't change that."

    red @closedbrow talking2mouth "Do you think you could use some help with your job here, then?"

    silver @talkingmouth "Well, yeah. But you're already helping, by coming here to beat them up every once in a while."

    red @talkingmouth "Glad I could be your {color=#0048ff}enforcer{/color}, then!"

    silver @sad "I don't want that."

    red @surprised "Huh?"

    silver @sad "Everything about my life is drenched in violence, and authority, and shouting, and absolution, and painful memories."
    silver @talkingmouth "I don't want to drag anyone--you--into that."

    pause 1.0

    silver @sad "I don't need an enforcer. I don't need {i}more{/i} people who want to beat up others on my behalf. I just need a..."

    pause 2.0

    red @sad "Silver?"

    silver @closedbrow sadmouth "{size=30}I just need a {color=#0048ff}friend.{/color}{/size}"

    pause 2.0

    silver @surprisedbrow sadmouth "{size=30}Please?{/size}"

    red @happy "Silver. Did you really need to ask? C'mon. I wouldn't have come out here if I didn't want to be your friend."

    silver @smilemouth "...Thank you."

    $ persondex["Silver"]["Relationship"] = "Friend"
    $ persondex["Silver"]["RelationshipRank"] = 1

    $ renpy.music.set_volume(0.1, delay=0.0, channel="music")
    $ PlaySound("sav.ogg")
    $ renpy.music.set_volume(1.0, delay=1.0, channel="music")

    narrator "Your heart shifts as you feel your relationship with Silver evolve from '{color=#0048ff}Classmate{/color}' to '{color=#0048ff}Friend{/color}'!"

    return

label Silver2:    
    stop music fadeout 1.5
    show relichall_A with Dissolve(1.5)
    
    queue music "audio/music/DontEverForget_start.ogg" noloop
    queue music "audio/music/DontEverForget_loop.ogg"

    redmind @thinking "Hm. Let's see, what should I do...? I've got some time, so..."

    show silver winter with vpunch 

    silver @talkingmouth "Red."

    red @talkingmouth "Red."

    silver @closedbrow talkingmouth "Need you to come with me."

    red @confused "Uh... sure. Is that about the Disciplinary Committee?"

    silver @closedbrow talkingmouth "Only that I'm about to jump into the harbor if I have to listen to one more of Cheren's 'duty' and 'responsibility' speeches."
    silver @sad "And that airhead's always nodding along, hanging on his every word, like he isn't just forcing us to listen to ten minutes of self-flagellation."

    red @confused "Huh?"

    silver @sad "Means 'punishment.' Swear he goes out of his way to embarrass himself as much as he can."

    $ ValueChange("Skyla", 2, 0.25, False)
    $ ValueChange("Cheren", 2, 0.75)

    narrator "Your understanding of Skyla increased! ...And your understanding of Cheren is further muddied."

    silver @closedbrow talkingmouth "But unlike that guy, I'm not going to sit in a dark room writing emo poetry."
    silver @talkingmouth "Got something to do. And I could use you to do it."

    red @sadbrow talkingmouth "...Does that mean you trust me again?"

    silver @closedbrow talkingmouth "Not even close, red. But if you're going to use that power anyway, I want to put it toward something good."

    pause 1.0

    show silver sadbrow with dis

    red @sadbrow talkingmouth "I do too, man."

    silver @talkingmouth "Well, I'm giving you a chance to prove it."

    pause 0.5

    silver -sadbrow @talkingmouth "We're going up the mountain. Will you be warm enough in that?"

    red @talkingmouth "Uh, should be, I think."

    silver @angrybrow talkingmouth "...Don't try to act tough. You can't 'friend' your way out of a cold."
    silver @talkingmouth "Come with me."

    hide silver with dis

    pause 0.3

    redmind @thinking "Hm? He's not heading towards the mountain... are we going somewhere else first?"

    scene blank2 with splitfade

    pause 0.5

    narrator "You follow Silver closely, though he doesn't look back at all. You soon realize that you're heading toward the Disciplinary Committee's office, and start to pull back a bit."

    red @confused "Hold on--"

    silver winter @talkingmouth "This doesn't have anything to do with the Committee. It's just where lost and found is."

    red @sadbrow talking2mouth "...Alright."

    scene studentcouncil 
    show silver winter closedbrow 
    with splitfade

    silver @talkingmouth "...Right. Bunch of clothes here, left over. Take something warm. Take a whole outfit, if you want."

    red @surprised "Oh. Uh, is that alright?"

    silver @talkingmouth "This box has been here since last year."
    silver @sad "Whoever this shit belonged to doesn't remember it exists anymore. They're not coming back. It's just lost, not found."

    pause 0.5

    silver @angry "So take something!"

    red @sadbrow talkingmouth "Uh... I don't want to sound ungrateful, but if this stuff has been sitting here for a year, shouldn't I probably wash it before putting it on?"

    silver @talkingmouth "Already done. Put it in with the washing at the shack."

    red @surprised "!"

    silver @angry "What?"
    silver @sad "You think any of those idiots I live with are the kind to wash their own damn clothes? I'm their landlord, but sometimes I feel more like their mother, they're so hopeless."

    red @closedbrow talkingmouth sweat "Alright. I'll find something, then..."

    narrator "You rummage through the clothing for a while, until you find a coat you like the look of."

    red @talkingmouth "Awesome! These'll work."

    silver @talkingmouth "Alright. Bathroom in the corner. Get changed there, then we can go."

    red @talkingmouth "Sure."

    narrator "You lean down to put the box of clothing away, then notice something strange. A black shirt with a big red \"R\" on it is folded within the clothing."

    show silver surprisedbrow with dis

    red @confused "Huh, what's--"

    show silver:
        xpos 0.5
        ease 0.2 ypos 1.2 zoom 1.3

    silver angry "It's {i}nothing.{/i}"

    pause 1.0

    show silver:
        ypos 1.2 zoom 1.3
        ease 0.5 ypos 1.0 zoom 1.0

    silver -angry @talkingmouth "Just some trash. One of my tenants' old clothes must've gotten mixed in."

    pause 0.5

    silver @sad "Go on. Get changed."

    red @sad "Okay."

    scene blank2 with splitfade

    narrator "You walk into the bathroom, and put your new change of clothes on the floor next to you, taking a look at yourself in the mirror."

    pause 0.5
    
    redmind swimsuithatless @thinking "Well, that definitely explains a couple things. {i}Rocket{/i}, huh...?"
    redmind @sad2eyes frownmouth "I might be a Pallet Town boy, but even I recognize their logo. So, if that was one of Silver's goons' clothes, and that goon was a member of Team Rocket, then that means Silver must have been..."

    pause 0.5

    redmind @closedbrow frownmouth "Well, he was definitely involved, somehow."

    scene studentcouncil 
    show silver winter 
    with splitfade

    silver @talkingmouth "You're back."
    silver @closedbrow talkingmouth "Something up? You look like you've seen a ghost."

    red winter @talkingmouth "Not really."

    silver @talkingmouth "Right. Let's go."
    silver @talking2mouth "I'll cover the Ride Cyclizar fee."

    python:
        hascyclizar = False
        for mon in playerparty:
            if (mon.GetId() == pokedexlookupname("Cyclizar", DexMacros.Id)):
                hascyclizar = True
                break

    if (hascyclizar):
        red @happy "It's fine. I've got one."

        silver @talkingmouth "Alright."

        python:
            rideable = None
            for mon in playerparty:
                if (pokedexlookupname("Cyclizar", DexMacros.Id) == mon.Id):
                    rideable = mon
                    break

        $ PlaySound("pokemon/ball sound.ogg")
        $ sidemonnum = pokedexlookup("Cyclizar", DexMacros.Id)
        $ sidemonoverride = rideable.GetNickname()
        $ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))
        
        sidemon "Cyc! Lizar!"

        $ sidemonoverride = None

    else:
        red @talkingmouth "Thanks."

        silver @talkingmouth "Don't mention it."

    scene icepath with splitfade

    pause 0.5

    show silver winter with dis

    red winter @talkingmouth "So, uh, what're we doing here?"

    silver @talkingmouth "One of my tenants told me about an Absol she spotted out here. Looked like a really tough one, she said, too."

    $ absolinparty = absolobj in playerparty
    $ caughtabsol = absolinparty or absolobj in box
    $ absolsex = "him" if absolobj.Gender == Genders.Male else "her"

    if (caughtabsol):
        red @talkingmouth "Oh, was that a while ago? Because I caught that Absol."
        if (absolinparty):
            red @happy "I've got [absolsex] with me now, actually."

            $ PlaySound("pokemon/ball sound.ogg")
            $ sidemonnum = pokedexlookup("Absol", DexMacros.Id)
            $ sidemonoverride = absolobj.GetNickname()
            
            $ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))
            sidemon "Absoooool."

            $ sidemonoverride = None

        silver @talkingmouth "Nice. They're good Pokémon. But no, this was more recent."

    else:
        red @talkingmouth "Oh, was that a while ago? Because I fought that Absol."

        silver @talkingmouth "Nah. More recent."

    silver @talkingmouth "Lot of trainers out there... don't respect Absol."
    silver @closedbrow talkingmouth "Either they're superstitious idiots that think Absol {i}bring{/i} disaster, or they're even bigger idiots trying to monetize their ability to sense disasters."
    silver @talking2mouth "You get a lot of trainers trying to use them, or 'cheat' their disaster sense for some kinda profit."
    silver @sadbrow talking2mouth "They're living creatures. Not smoke detectors, not earthquake sirens..."
    silver angry "Scum."

    pause 1.0
            
    silver -angry @sad "Since Absol don't let themselves be exploited, the trainers call 'em 'difficult to train', and just drop them. Or... {i}worse.{/i}"

    pause 0.5

    silver sadbrow @talkingmouth "I had one once."

    red @happy "Cool! Is it with your Crobat?"

    silver sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."
    silver @sadmouth "It was difficult to train."

    pause 1.5

    silver @talkingmouth "Now you see why you're here."
    silver @closedbrow talkingmouth "We're not here to catch the Absol. My tenant told me the Absol looked like it was wounded. It'd be dangerous for {i}anyone{/i} to try and catch it right now."
    silver @talkingmouth "I can't calm it down. Not like I am. That's what I need you for."

    red @sadbrow talkingmouth "...Alright."

    scene blank2 with splitfade

    pause 1.0

    $ sidemonnum = pokedexlookup("Absol", DexMacros.Id)
    $ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))

    if (caughtabsol):
        red winter @talking2mouth "Yeah, I definitely recognize that cry. The Absol's this way. Sounds like it's wounded, like you said."

        silver winter @talkingmouth "We should hurry."

    else:
        silver winter @talkingmouth "Yeah, I recognize that cry. The Absol's this way."
        silver @sad "Sounds... pained."

    scene icecave with splitfade

    narrator "You emerge into a cave, where you see an Absol shivering up against a wall. It moves dizzily, and sweat pours down its forehead, slicking its softly lucent fur."

    if (not caughtabsol):
        red winter @surprised "Wait... that's the Absol! The one Skyla, Brendan, and I fought!"

        show silver winter angry with vpunch

        silver "And you left it like this?!"

        red @sadbrow talking2mouth "No. I promise. It just ran away after the battle. It didn't look injured then, at all."

        silver -angrymouth angrybrow "{w=0.5}.{w=0.5}.{w=0.5}."
        silver -angrybrow @sadbrow talkingmouth "Fine. Let's just help it."

    else:
        show silver winter angry with dis
        
        silver "Some trainer... just left it like this. Look, they battled it way past the point at which you should just call it quits on trying to catch it."
        silver "I swear, if I got my hands on that worthless shithead, I'd... I'd..."

        pause 1.0

        red winter @confused "What?"

        silver -angry @sad "Nevermind. Let's just help it."

    show silver:
        xpos 0.5
        ease 0.5 xpos 0.25

    narrator "You cautiously approach the Absol, who seems to calm down at your presence."

    red @sadbrow talkingmouth "Hey, big man. Big girl? Not sure. Don't worry--we're here to help. We've got some medicines that should make you feel better."

    narrator "Silver pulls a ball of red thread and a couple of bandages out of his coat."

    silver @talkingmouth "Doesn't look like you're going to need stitches, but you'd probably appreciate a Full Restore, and a bandage for that leg."

    $ sidemonnum = pokedexlookup("Absol", DexMacros.Id)
    $ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))

    sidemon "Absol... sol!"

    pause 1.5

    silver @talkingmouth "Alright. Looks like we're done here."

    red @confused "That's all?"

    silver @talkingmouth "That's all."

    red @talkingmouth "Aren't... you going to catch it?"

    silver @closedbrow talkingmouth "I don't catch Pokémon. Not anymore. Especially not an Absol."

    red @surprised "Really? But you have so many of them!"

    silver @sad "Told you. They're my tenants'. Haven't thrown a Poké Ball since I lived in Kanto."
    silver @closedbrow talkingmouth "You need Pokémon in this world, just to exist, but I ain't catching any more."
    silver @sadbrow talkingmouth "That's one thing my tenants are good for, I guess."

    pause 0.5

    red @sadbrow talkingmouth "Where {i}is{/i} your Crobat, Silver?"

    silver @closedbrow talkingmouth "Safe. Away from me."

    pause 1.0

    red @sadbrow talkingmouth "You know, I heard that Golbat won't evolve unless they have a strong bond with their trainer."

    silver @angry "Yeah? Well, {i}I{/i} heard being a shit judge of character isn't something exclusive to humans."

    red @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
    red @talking2mouth "I don't know a lot of... your story."

    silver @talkingmouth "That's right. You don't."

    red @talkingmouth "But I feel like you need to forgive yourself."

    silver @sadbrow happymouth "Oh, I have. That's why I don't go near waterfalls anymore."
    silver @sadbrow talkingmouth "Everything else, though... that's not mine to forgive."

    pause 1.0

    silver @angrybrow talkingmouth "Hey, what're you still doing here? Go on. We're done."

    narrator "Silver turns his attention to the Absol, which is standing steadfastly in front of you two. A small red string tying down a bandage on its foreleg is the only sign that you had ever interacted."
    narrator "Your eyes trace the string's path, and realize with a start it leads to Silver's hand."

    red @happy "Hey, red. You forgot to cut the string."

    silver @surprisedbrow talking2mouth "Hm?"
    silver @talkingmouth "Oh. No wonder it's still here, then." 
    
    narrator "Silver reaches into his boot, and pulls out a small switchblade. You cock an eyebrow, but don't question it. He raises the knife towards the red string, and..."

    silver @sad "{w=0.5}.{w=0.5}.{w=0.5}."

    narrator "Hesitates."

    silver @closedbrow talkingmouth "Looks familiar."
    silver @sadbrow talkingmouth "Just in my head, though. No way."

    narrator "Silver swings the knife down, and..."

    show silver surprisedbrow with dis

    $ sidemonnum = pokedexlookup("Absol", DexMacros.Id)
    $ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))

    sidemon "Ab!"

    narrator "Absol blocks the blade, deflecting it with its own bladed horn."

    silver @sadbrow talkingmouth "C'mon. What are you trying to say, Absol?"

    red @sadbrow talkingmouth "I think it's pretty obvious what it's saying, Silver."
    red @happy "It's not a very subtle metaphor."

    silver closedbrow angrymouth "{size=30}Damn it.{/size}"

    pause 1.0

    silver @angry "Go on. {i}Leave.{/i} You don't want this. I don't want this. {i}Anyone{/i} else would be better."

    sidemon "{w=0.5}.{w=0.5}.{w=0.5}."

    silver sadbrow -angrymouth @talkingmouth "[first_name]. Get out of here. I need to show this Absol what's what, and I can't have you staring at me with those moon eyes."

    red @sadbrow talkingmouth "...Alright."

    pause 0.5

    red @sadbrow talkingmouth "I know you voted to keep me on the Battle Team, when Erika was trying to kick me out. And I appreciate that."
    red @talkingmouth "I don't know what you were thinking, then... but maybe you were thinking I deserved another chance?"

    pause 0.5

    red @talkingmouth "If I had the ability to, I'd give you another [bluecolor]chance{/color}, too."

    pause 1.0

    red @sadbrow talkingmouth "I don't, though."

    pause 1.0

    red @happy "But maybe there's someone here who {i}does{/i}."
    
    $ sidemonnum = pokedexlookup("Absol", DexMacros.Id)
    $ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))

    sidemon "Sol!"

    pause 1.0

    silver @angrybrow talkingmouth "Out."

    scene blank2 with splitfadefast

    pause 1.0

    narrator "You leave the cave, and a few minutes later, you hear the sound of battle."

    scene icepath with splitfade

    pause 1.0

    show silver winter with dis

    silver @talkingmouth "We're done here. Let's go back."

    narrator "Your eyes flit down to Silver's waistline, and notice a Luxury Ball that was not there before."

    red winter @talkingmouth "A Luxury Ball?"

    silver @sadbrow talkingmouth "Had one lying around."

    red @closedbrow talking2mouth "Hm."

    show silver sadbrow with dis

    red @talkingmouth "Looks good on you."

    scene blank2 with splitfade 

    red winter @talkingmouth "Oh, about the clothes--"

    silver winter @talkingmouth "Keep 'em."

    pause 1.0

    silver @closedbrow talkingmouth "They look good on you."

    $ oldrelationship = GetRelationship("Silver")
    $ persondex["Silver"]["Relationship"] = "Chance"
    $ persondex["Silver"]["RelationshipRank"] = 2

    $ PlaySound("sav.ogg")

    narrator "Your heart shifts as you feel your relationship with Silver evolve from '[bluecolor][oldrelationship]{/color}' to '[bluecolor]Chance{/color}'!"

    return