label Ethan1:

stop music fadeout 1.5

scene hall_A2b
with Dissolve(2.0)

show screen songsplash("Run Away, Fugitives", "Lazy Totodile")
queue music "audio/music/runawayfugitives_start.ogg" noloop
queue music "audio/music/runawayfugitives_loop.ogg"

narrator "You've been wandering the hallways aimlessly for a while, when you're suddenly hit by a strong wave of exhaustion."

red @closedbrow talking2mouth "Ugh. I've been doing too much. Burning the candle at both ends."
if (timeOfDay == "Evening"):
    red @sad2eyes angryeyebrows talking2mouth "Maybe I should just go to bed and call it early."
else:
    red @closedbrow talking2mouth "Maybe I should take a quick nap."

show hall_A2b with vpunch 

$ renpy.music.play("Audio/Pokemon/pikachu_angry1.ogg", channel="altcry", loop=None)
libpikachu @angryeyes frownmouth "Pika!"

red @surprised "Woah! Hey, buddy, easy with the biting."

if (timeOfDay == "Evening"):
    red @happy "What was that about, huh? Since when have {i}you{/i} cared if we go to bed a bit early?"
else:
    red @happy "What was that about, huh? Most of the time, you're the one trying to get me to take a nap!"

$ renpy.music.play("Audio/Pokemon/pikachu_sad.ogg", channel="altcry", loop=None)
libpikachu @sadeyes surprised2mouth "Pika..." 

red @happy "Jeez. Don't worry, bud. I'm fine. Just tired."

pause 1.0

narrator "Something about that casual dismissal sticks in your mind."
narrator "Your thoughts wander to where you've heard that phrase before..."

show blank with Dissolve(1.0)

show lobby behind blank at sepia
show ethan happy behind blank at sepia
show flashback behind blank at sepia 

hide blank with Dissolve(2.0)

ethan @talkingmouth "Jeez. Don't worry, man. I'm fine. Just tired."

pause 3.0

hide ethan
hide flashback
hide lobby
with Dissolve(1.0)

pause 2.0

red @talking2mouth "Maybe I should find Ethan?"

$ renpy.music.play("Audio/Pokemon/pikachu_norm1.ogg", channel="altcry", loop=None)
libpikachu @talkingmouth "Pikachu."

redmind @thinking "But... where is he? It's weird that I don't have his phone number after all this time."

narrator "You look at your dorm door, where your feet have unconsciously taken you."

redmind @confusedeyebrows frownmouth "No way. He couldn't actually be...?"

$ PlaySound("GenericDoorOpen.ogg")

scene blank with splitfade

pause 2.0

$ PlaySound("GenericDoorClose.ogg")

scene suite 
show ethan noshine frownmouth
with splitfade

pause 0.5 

if (IsWeekend()):
    ethan -noshine -frownmouth @happy "Hey, man! You're back early."

    red @talkingmouth "You are too."

    ethan @talkingmouth "Nah, I don't leave the dorm much on weekends, unless Leaf is dragging us somewhere."

else:
    ethan -noshine -frownmouth @happy "Hey, man! You're back early."

    red @talkingmouth "You are too."

    ethan @talkingmouth "Nah, I usually get back to the dorm earlier."
    ethan @happy "After classes, I pretty much just come back here."

ethan @talkingmouth "Anyway, what's the occasion? None of the others are here. Looking for one of them?"

show ethan surprisedbrow frownmouth with dis

red @talkingmouth "Nah, I just thought we could chat."

pause 1.0

ethan @unamusedbrow talking2mouth "That's never good."
ethan @confusedeyebrows talking2mouth "Is this an intervention? I swear, my gacha habit is under control. These are choices, and I can quit any time."

red @happy "What? No, dude. I just wanted to chat. Seriously. I remembered that talk we had in Argent Mountain, and I realized we don't hang out enough."

pause 1.0

red @confused "Wait, what's a gacha habit, and should I be concerned?"

ethan @surprised "Wait, you don't know what gacha is?"

red @confused "Um... no."

ethan @happy "That's crazy. The first Gacha game was literally invented in the Kanto region, man. 'Dragonite Collection.'"

red @talking2mouth "I feel like I'm missing out."

ethan -surprisedbrow @sweat closedbrow talking2mouth "Oh, no, honestly, this is pretty great. Once you know what it is, it's a total psychohazard. Better you never learn."
ethan @closedbrow talkingmouth "It's like 'The Game.' {size=30}Which I just lost.{/size}"

red @talkingmouth "You know, I thought we were basically identical, but it's starting to sound like our childhoods were a bit more different than I thought."

ethan @closedbrow talking2mouth "Eh, that's probably for the best. If it turned out we had the same kind of childhoods, I'd probably have to order some kinda genealogy test, just to be sure."

red @closedbrow talking2mouth "I'll be honest, the thought {i}has{/i} occurred to me, before."

show ethan downeyes with dis

narrator "Ethan looks down at his phone and quickly taps a couple places on the screen."

show ethan -downeyes with dis

ethan @talkingmouth "Alright. I set up my macros, so for the next twenty-two minutes, my phone'll just be running my dailies."

redmind @surprisedbrow frownmouth "I recognize some of those words."

ethan @upeyes talking2mouth "Can't believe the developers actually expect people to do it manually. They have {i}no{/i} respect for their players' time, seriously."
ethan @talkingmouth "Anyway, let's chat."
ethan @sadbrow talking2mouth "I kinda think I get the gist of your, uh, your childhood, but why don't you recap it for me?"

red @talkingmouth "Sure. Honestly, there's not much more to tell you that I didn't tell you on that first day."
red @closedbrow talking2mouth "I grew up in Pallet. Had a bunch of friends until..."

if (GetRelationshipRank("Blue") > 0):
    red @closedbrow talking2mouth "Well, until Blue made a mistake."
else:
    red @upeyes angryeyebrows talking2mouth "Well, until Blue decided to be a dick and tell everyone about Frienergy."

ethan @closedbrow talkingmouth "That's rough, buddy."

red @upeyes talking2mouth "Tell me about it. {i}Still{/i} dealing with the fallout from that one."

red @talkingmouth "It was just my mom and I. Still is, actually. She doesn't make a lot of money. Works for a call center based out of Saffron, but her job's remote, so she doesn't have to leave home."

red @talkingmouth "Anyway, what about you? You said you grew up in New Bark Town, right?"

ethan @talkingmouth "Yeah."
ethan @sadbrow talkingmouth "Never had to deal with, uh, the money thing, though. Sorry about that."

red @happy "Hey, it's just a part of life. Maybe I learned some lesson growing up poor. Maybe without that, I would've ended up a total prick."

ethan @sad2eyes talking2mouth "Maybe. I find that sometimes bad things just happen to good people for no reason, though."

pause 1.0

ethan @upeyes talking2mouth "But then you have to define 'bad' and 'good', and that's a level of philosophy I'm not prepared to get into in yesterday's pajamas."

red @surprised "Hm? You're just wearing your regular clothes, though."

ethan @winkbrow talkingmouth "As our old roommate Hilbie would say--your powers of observation of the obvious are unparalleled."

red @confused "Dude, you shouldn't sleep in your clothes."

pause 1.0

red @sadbrow sweat talkingmouth "Tell me you at least took your socks off."

ethan @closedbrow talking2mouth "I cannot tell a lie."

red @angry "Dude!"

ethan @surprised "[first_name], it's not a big deal! Like, do I smell?"

pause 1.0

red @sadbrow talking2mouth "I mean... I haven't smelled you recently."

pause 1.0

show ethan:
    ypos 1.0 zoom 1.0
    ease 0.5 ypos 1.1 zoom 1.2

narrator "You attempt to surreptitiously take a step closer to Ethan."

ethan frownmouth @talking2mouth noshine "You better not be about to sniff me, dude."

pause 2.0

show ethan:
    ypos 1.1 zoom 1.2
    ease 0.5 ypos 1.0 zoom 1.0

narrator "You attempt to surreptitiously take a step back away from Ethan."

pause 1.0

ethan @sadeyebrows talking2mouth "Nah, you're right. Sorry, I know it's a bit gross. Just seems like a bit of a waste to switch out outfits, you know?"

red @talkingmouth "It's alright, man. Maybe I came on a bit strong. My mother used to have a real thing about getting up every day, changing clothes, going outside, talking to neighbors, getting a bit of sunshine..."
red @sadbrow talkingmouth "Don't know if there was any science behind it, but those little rituals always made the days feel... full. Even though Pallet was a quiet, empty town, having something to do every day helped me make use of my time."

ethan @talking2mouth "Glad that worked for you."
ethan @closedbrow talking2mouth "I never really had anyone pushing me like that in my life. There was Kris--uh, Professor Cherry--but, I mean, she was my babysitter. It's not like a babysitter can be around all the time, like a mom."
ethan @talking2mouth "And then she went away for a couple of years, anyway."

red @sadbrow talking2mouth "I'm sorry."

ethan @happy "Can't miss what you never had, right? Who knows, maybe it would've been worse for me."

red @confused "If you don't mind me asking... what about your parents?"

ethan @sad2eyes talking2mouth "Eh. Dad's the only one there. Mom doesn't live with us. He makes a lot of money, but Dad sends her, like, ten percent of every paycheck he makes. Her divorce lawyer was pretty good."
ethan @upeyes angryeyebrows talking2mouth "Supposedly, she's saving that money for me, but if she's not coughing it up to help pay for the literal most expensive school in the world, I'm pretty sure we're never going to see it."

red @closedbrow talking2mouth "Hm."
red @talkingmouth "So it sounds like you were comfortable. What's your Dad do?"

ethan -frownmouth @talking2mouth "Mayor of Goldenrod."

pause 1.0

red @confused "Sorry?"

ethan @talkingmouth "Mayor of Goldenrod, dude. He's the mayor. Of Goldenrod. I mean, my great-great-great-whatever-grandpa founded the city, so it's kinda a family business."

pause 1.0

red @surprised "Oh my god. Your last name is Gold."

ethan @happy "Hey, you got it!"
ethan @talkingmouth "Confession time, I love seeing that look of realization on people's faces. But, yeah, that's it. The city's named after an ancestor of mine, actually."
ethan @winkbrow talkingmouth "Also lends itself to some pretty easy and shameless pick-up lines. I'm sure you can guess 'em."

red @unamusedbrow unamusedmouth "Great, I think you just ruined Goldenrod for me."

ethan @happy "Your loss, my guy."

red @confused "But didn't you say you grew up in New Bark Town? If your father was mayoring half a region away, how did that work out?"

ethan @sad2eyes sadeyebrows talkingmouth "That's why Professor-- ah, screw it, I'm just going to call her Kris."
ethan @talkingmouth "Anyway, that's why Kris and I spent so much time together. Sometimes I'd go to Professor Elm's lab and play there, too."
ethan @closedbrow talkingmouth "Mostly I'd just keep myself entertained, though. I figured out how the internet worked pretty young."
ethan @closedbrow sweat talking2mouth "Looking back on it, that was a blunder, but at least I wasn't bored."
ethan @sad2eyes angryeyebrows talking2mouth "And... sometimes... there was someone else."#FIX THIS: Fix this if/when Lyra shows up.

pause 1.0

ethan @talkingmouth "So, yeah, didn't spend a whole lot of time with my Dad. He's a cool guy, though. We chat online a bunch."

red @talkingmouth "You mentioned mayoring was a family business. Do you think you'll go for it?"

ethan @confused "Could you seriously see me as a politician? I guess I'm a bit more patriotic about Johto than the average Joe, but..."
ethan @closedbrow talkingmouth "Nah. Don't have much attachment to Goldenrod, honestly. I've only been there a couple times to visit my Dad, and one time with Kris when we were checking in on her sister."

red @talking2mouth "Why didn't you just live in Goldenrod, though?"

ethan @sad2eyes noshine frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
ethan @sadeyebrows talkingmouth "Dunno, man."

pause 1.0

red @sadbrow talking2mouth "Oh."

ethan @happy "Hey, come on. Don't gimme that kicked-Houndour look. I had the entire house all to myself. And it's not like I was being ignored--like I said, Dad and I would chat."
ethan @talking2mouth "Often."

red @confused "How often?"

ethan @sweat happy "Whoa, getting a bit interrogative, aren't we, Inspector Foyle? I dunno, man, like, once a m- you know, often."

red @sadeyebrows frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

ethan @angryeyebrows frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
ethan @sad2eyes angryeyebrows talking2mouth "I said don't look at me like that, dude."

red @downeyes sadeyebrows talking2mouth "Sorry."

ethan @closedbrow talking2mouth "...Nah, I'm just being grumpy. Sorry about that. Didn't get enough sleep last night."
ethan @happy "I'm fine, just tired."

red @sadeyebrows talking2mouth "How long have you been... {w=0.5}tired?"

ethan @confusedeyebrows talking2mouth "Hm? Bit of a weird question. Like, almost ten years, at this point?"
#FIX THIS: After 10 years have passed

red @surprised "Huh? Okay, maybe my thing was a weird question, but that's a weird answer. Ten years exactly?"

ethan @talkingmouth "Nah, {i}almost{/i} ten years."
#FIX THIS: After 10 years have passed

red @talking2mouth unamusedbrow "Okay, that's not what I was asking. How can you be so specific? What happened ten years ago?"

ethan @closedbrow talking2mouth "Beats me, man."

red @confused "But you can say exactly {i}when{/i} it happened?"

ethan @talkingmouth "Yup."

pause 1.0

red @talking2mouth "You want to talk about it?"

ethan @closedbrow talkingmouth "Only if you want to."

red @happy "I'm asking."

ethan @talking2mouth closedbrow "Your funeral, my guy."

pause 1.0

ethan @talking2mouth noshine "When I was a kid... I was better."

red @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

ethan @talking2mouth "My memory was better. It was easier to get myself to do things. I was smarter, friendlier, even kinder."
ethan @talking2mouth "I remember who I was. I can see it in the past, clear as glass. But now I'm... {i}this,{/i} and I don't know what happened."

pause 1.0

ethan @closedbrow talking2mouth "Elm used to say, you know, 'oh, he's so pleasant to have in class! He'll be a Professor someday!'"
ethan @talking2mouth "They tried to move me up a grade a couple times. I had tons of friends, man."
ethan @sad2eyes sadeyebrows talkingmouth "Sure that's hard to believe."

pause 0.5

ethan @closedbrow talking2mouth "But even other stuff. Like, patterns. I'm crap at recognizing patterns, you know? Figuring stuff out by myself."
ethan @sadbrow talkingmouth "You know those dumb questions I ask to get a laugh? Half of those aren't even jokes, man. To figure something out, I gotta sit down and spend, like, ten minutes on it."
ethan @sad2eyes talking2mouth "I used to be a whiz at math. And, like, I could read a whole book in an afternoon. Three-hundred pagers, easy. Now I barely remember how to divide, and haven't read anything without pictures in years."
ethan @closedeyes angryeyebrows angrymouth "I can tell my own Pokémon are angry at how I command them in battle. It's like they expect more of me, and..."

pause 0.5

ethan @sadbrow sadmouth "I mean, I expect more of myself too, man, you know? I don't want to be a screw-up in {i}everything{/i} I do. And I {i}know{/i} that I have more in me, because I used to be better."
ethan @closedbrow talking2mouth "But then... I just lost it. And I don't know what I lost. But it's some kind of ache, like I used to have a fifth limb, and it's just {i}gone{/i} now."

pause 0.5 

ethan closedbrow tears angrymouth "Shit. Sorry. Didn't mean to traumadump on you like this."

pause 1.0

narrator "You struggle to find the right words."

pause 0.5

narrator "Perhaps there are no words alone that are right enough."

ethan -tears -noshine -closedbrow frownmouth noshine @sad2eyes sadeyebrows talking2mouth "Hey, can you do me a solid and just forget this conversation ever happened?"

menu:
    ">Agree to forget":
        $ AddEvent("Ethan", "Forgotten")
        ethan downeyes noshine @talkingmouth sadeyebrows "Thanks, man."

        narrator "His gaze returns to his phone."

        ethan @happy "Oh, hey, that's our time. I should probably go do something. Maybe take a shower. Good talk, man."

        call clearscreens() from _call_clearscreens_178
        scene blank2 with Dissolve(2.0)

        narrator "In accordance with his wishes, you forget the content of the conversation you just had."
        narrator "Perhaps other memories, too, are forgotten."

        $ PlaySound("sav.ogg")

        narrator "Your heart stagnates as you become certain your relationship with Ethan '{color=#cf0000}will never change{/color}'."

        pause 1.0 

        narrator "But this was his wish."

    ">Deny his wish":
        show suite with vpunch

        show ethan surprisedbrow -noshine with dis

        red @angry "Never!"

        ethan @talking2mouth "Huh?"

        red @closedbrow talking2mouth "Never. I'm not going to forget this. I'll never forget any part of this."

        ethan -surprisedbrow @unamusedeyebrows sad2eyes talking2mouth "Grrrreaaaat."

        red @talking2mouth "I'm so sorry you feel like this, Ethan."
        red @talking2mouth sad2eyes sadeyebrows "If there's anything I can do to help... anyway I can show you how cool you are, now, then..."

        ethan -surprisedbrow @talkingmouth "Dude, we're talking. That's a huge help."

        red @talkingmouth "...I don't mean talking. I don't mean something I can {i}say{/i} to make you feel better. I'm asking about something I can {i}do{/i} to help you feel better."

        pause 1.0

        ethan @confused "{i}Do?{/i} I... I don't think there's anything that {i}can{/i} be done, dude. I mean, it's all in my head."
        ethan @talking2mouth "I mean, let's be real. I'm actually {i}hoping{/i} I've got some kinda 'problem' so that, maybe someday, a genie could just snap its fingers and undo it, you know?" 
        ethan @sadbrow talkingmouth "I just gotta get over it--"

        show ethan surprisedbrow frownmouth :
            ypos 1.0 zoom 1.0
            ease 0.5 ypos 1.1 zoom 1.2

        red @angry "Hey! Stop talking about my friend like that!"

        ethan -surprisedbrow -frownmouth -surprised @angry "Hey, I'm just talking about--"
        ethan @surprised "Oh."
        ethan @happy "Ah, see, that's what I'm talking about. Took me a second to figure out what you were saying, there. Back in the day, that'd be done, boom, easy as pie."
        ethan @closedbrow talking2mouth "Anyway, if there was anything that {i}could{/i} be done, I mean, yeah, I'd go for it. But there just isn't, my guy."

        red @closedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

        pause 1.0

        red @talking2mouth closedbrow "I'm thinking."

        ethan @talkingmouth "Godspeed."

        pause 1.0

        red @talking2mouth "You noticed this happened almost ten years ago, right?"
        #FIX THIS: After 10 years have passed

        ethan @talking2mouth "Yeah."

        red @closedbrow talkingmouth "Do you remember anything else happening around that time?"

        ethan @closedbrow talking2mouth "...Nah, not really, man. I was pretty young. I've kinda got a shitty memory on a good day, even for stuff that happened yesterday."
        ethan @happy "I think a decade ago's a bit out of reach."

        red @closedbrow frownmouth "Hm... maybe. {i}Maybe.{/i}"

        pause 1.0

        red @talking2mouth "Let's look it up."

        ethan @confused "Huh?"

        red @happy "I've kinda got a horrible memory for, like, dates and events, too, so if we look up stuff that happened about ten years ago--1993 to 1995--then maybe something will remind you."

        ethan @confused "What? You're going to just, like, look up world events for a two-year period and just see if they remind me of anything?"

        red @confused sweat "That... {i}does{/i} sound a bit excessive. But they don't need to be world events."
        red @closedbrow talking2mouth "Just stuff that happened in the area of New Bark Town around ten years ago. You didn't go anywhere, did you?"

        ethan @talkingmouth "Hm? Uh, not often. Like I said, Kris and I sometimes visited Goldenrod." 
        ethan @closedbrow talkingmouth "Honestly, though, I coulda been in a few places. I traveled a lot more back then, always volunteering for stuff, and signing up to go places."
        ethan @talkingmouth "School had a ton of field trips, where we'd go with Professor Elm. I even went to other regions."

        red @talking2mouth "...That sounds familiar. Have you told me that before?"

        ethan @talking2mouth "Nah, but when we first met, I mentioned there was that one field trip our class took to Pallet Town, when we first bumped into each other."

        $ PlaySound("idea.ogg")

        show ethan surprisedbrow frownmouth with dis

        red @surprised "That's something! I nearly forgot about that! Was that ten years ago?"

        ethan -surprisedbrow -frownmouth @closedbrow talkingmouth "Dude, I... have {i}no{/i} idea. Like I said, my memory's crap."
        ethan @talking2mouth "I can ask my Dad where--"
        ethan @closedbrow sweat talking2mouth "Actually, he probably wouldn't know where I was."

        pause 1.0

        ethan @talkingmouth "Tell you what. Next time all three of us have got some free time, let's ask Kris, alright?"

        red @confused "Kris?"

        ethan @talkingmouth "Yeah. Her mind's like a steel trap. She never forgets anything about anyone. She'd remember where I was, if she ever even knew."

        red @talking2mouth "Alright. We'll get to the bottom of this."

        ethan @upeyes sadeyebrows talking2mouth "Really nothing to get to the bottom of, dude. I'm just a loser."
        ethan @sad2eyes sadeyebrows talking2mouth "The sooner we both accept it, the sooner we can move on from it."

        red @talking2mouth angrybrow "I'm not moving on. You're funny, kind, and handsome, and if you can't see that, there's something {i}very{/i} wrong here."

        ethan @sad2eyes talking2mouth "I mean... I've been trying to figure it out myself for a decade. If you manage it before the school year's over, I'll be a little pissed, not gonna lie."
        ethan @happy "But hey. Maybe this is just another thing you're better at than me. At least I can [bluecolor]hope{/color}."

        $ RelationshipRankUp("Ethan", "Hope", 1)

return