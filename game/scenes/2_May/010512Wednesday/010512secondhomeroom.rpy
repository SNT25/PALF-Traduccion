label secondhomeroom010512:

scene blank2

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom behind blank2

show oakbg behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade

oak @talkingmouth "And... oh, it appears that the lecture's over a bit before the bell. Well, I'm {i}loath{/i} to let you kids go before the bell rings, but..."

pause 1.0

oak @talkingmouth "Well, I suppose there's nothing too wrong with a couple extra minutes. Go off, then! And remember to study for your test tomorrow. It'll be a doozy!"

redmind uniform @thinking "Hm... if even Professor Oak is saying it's a doozy, this could be pretty serious..."

call clearscreens from _call_clearscreens_158
scene blank2 with splitfade

pause 1.0

show suite 
show screen currentdate
with splitfade

pause 1.0

$ PlaySound("knock.ogg")

red @confused "Hm?"

redmind @thinking "Oh, right, May said Brendan would be around to pick up his stuff."

red @happy "Come in!"

show brendan:
    xpos 1.0
    ease 0.5 xpos 0.66
show calem:
    xpos 0.0
    ease 0.5 xpos 0.33
with dis

red @talkingmouth "Hey, guys!"

calem @talkingmouth "Hello, [first_name]. You look... well."

pause 1.0

calem @closedbrow talking2mouth "Sorry, this is a tad awkward. We haven't really had a proper chance to chat since before the student council elections."

red @sadbrow talking2mouth "Yeah... sorry about that, by the way."

calem @closedbrow talkingmouth "Think nothing of it. We all played our foolish parts. Some more than others, but you are definitely in the lesser category."

brendan @sadbrow talking2mouth "Man, I just want to say I'm really sorry for doubtin' you. I totally believed what Cheren was saying."

calem @talkingmouth "Well... to be fair, what Cheren was saying {i}was{/i} right. It wasn't mind control, but he never claimed it was."

pause 1.0

calem @surprised "Er... not that I'm accusing you of anything! I mean, you {i}did{/i} keep a secret from us, but I fully understand why a person in your situation would."
calem @closedbrow talkingmouth "I mean, I wouldn't have, but it's not that I hold it against you or anything. I simply--"

brendan @talking2mouth "Bro."

calem @surprised "Yes?"

brendan @sadbrow talking2mouth "You keep digging that hole, you're going to hit the other side of the planet."

calem @closedbrow talkingmouth "Noted. I'll shut up now."

brendan @talking2mouth "So, hey, I just gotta ask, uh, do you have some of my stuff in here?"

calem @talkingmouth "Oh, yes, mine, too?"

red @closedbrow talkingmouth "Yeah. Blue was a bit too excited to pack my stuff, it looks like."

calem @surprised "Blue? Not [oldblue_name]?"

menu:
    "{color=#e226a6}[[Patience]{/color} Someone had to be the bigger man.":
        $ TraitChange("Patience")

    "{color=#b7669e}[[Charm]{/color} Nah, I'm over that. It was childish, anyway.":
        $ TraitChange("Charm")

calem @closedbrow smilemouth "Hm."

red @talkingmouth "C'mon, let's go to my room. You can pick out your stuff there."

scene bedroom with splitfade

pause 1.0

show brendan:
    xpos 0.66
show calem:
    xpos 0.33
with dis

pause 1.0

brendan @talking2mouth "Dude, your new dorm is freakin' {i}sweet!{/i}"

red @happy "Nah, it's just a regular suite."

brendan @closedbrow talking2mouth "Huh?"

calem @surprised "Ah! Yes, there's my jacket, my wristwatch, my... oh {i}dear{/i}, that definitely shouldn't be out in the open..."

brendan @talking2mouth "Yeah, let's grab our stuff."

show blank2 with dis

pause 1.0

show brendan sad

narrator "Calem and Brendan gather armfuls of their possessions, though it looks like it's going to take multiple trips."

hide blank2 with dis

brendan @talking2mouth "{size=30}Aw, man, May's gonna be pretty mad if I can't find it...{/size}"

red @talkingmouth "What's wrong?"

brendan @talking2mouth "There's meant to be a hot-pink suitcase here. It's got some, uh, some important stuff for May and I."

red @talkingmouth "Oh, right, May mentioned that. I don't think I've seen it, though. It sounds like it'd stand out, huh?"

brendan @talking2mouth "Yeah, probably."

red @talkingmouth "Maybe my roommates have seen it?"

show phone_B
show blue uniform:
    zoom 0.95 ypos 1.1
show phone_A
with fadeinbottom

blue @talkingmouth "I'm taking some extra lessons. What is it?"

red @talkingmouth "Extra lessons? You?"

blue @happy "What, you thought I was this awesome {i}naturally{/i}?"

red @playfulbrow talking2mouth "I've got to confess I've never put too much thought into it."

blue @talkingmouth "Yeah, anyway, I'm trying to figure out how the hell Dragon-types survive at the lower levels. It just doesn't--"

show brendan surprisedbrow frownmouth
show calem surprisedbrow frownmouth
show blue surprisedbrow frownmouth:
    zoom 0.95 ypos 1.1
    ease 0.5 xpos 0.42 zoom 0.7 ypos 1.0
show clair angry behind blue:
    xpos 0.54 zoom 0.8
with dis

clair @talkingmouth "Mr. Oak! Is there something you want to share with the class?!"

blue surprisedbrow frownmouth @surprised "Crap! What is it?"

red @surprised "Uh... pink suitcase?"

blue @angry "Ethan's room!"

hide blue
hide clair
hide phone_A
hide phone_B
with fadeoutbottom

pause 1.0

show calem -surprisedbrow -frownmouth -surprised
show brendan -surprisedbrow -frownmouth -surprised
with dis

red @talkingmouth "Well, it's in Ethan's room, apparently. Let's go."

calem @talkingmouth "Oh, that's fortuitous. We wanted to talk to Ethan, as well."

brendan sad @talking2mouth "I think he was a little bit mad at us for leaving Dorm 151..."

show calem sad with dis

pause 1.0

brendan @talking2mouth "Hey, [first_name], you're not mad at us, are ya?"

menu:
    "A little bit, but I'll get over it.":
        $ AddEvent("Calem", "WillGetOverBeingPissed")
        $ ValueChange("Calem", 1, 0.33, False)
        $ ValueChange("Brendan", 1, 0.66)

        calem @sadbrow talkingmouth "You have every right to be. I'm sorry. Now that I am situated in my new dorm with Serena and Brendan, I wouldn't want to leave, but..."

        calem @sadbrow talkingmouth "I understand how you must feel. I can only offer my most heartfelt apologies."

        red @closedbrow talking2mouth "I get it. You had no idea if I was even coming back, and I know you and Serena have your own thing happening."

    "Nah.":
        $ AddEvent("Calem", "NotPissed")
        $ ValueChange("Calem", 1, 0.33, False)
        $ ValueChange("Brendan", 1, 0.66)

        calem @sadbrow talkingmouth "Even so, you have every right to be. I'm sorry. Now that I am situated in my new dorm with Serena and Brendan, I wouldn't want to leave, but..."

        calem @sadbrow talkingmouth "I understand how you must feel. I can only offer my most heartfelt apologies."

        red @happy "Really, dude, it's alright. I get it. You had no idea if I was even coming back, and I know you and Serena have your own thing happening."

    "Kinda pissed, actually.":
        $ AddEvent("Calem", "StillPissed")
        calem @sadbrow talkingmouth "You have every right to be. I'm sorry. Now that I am situated in my new dorm with Serena and Brendan, I wouldn't want to leave, but..."

        calem @sadbrow talkingmouth "I understand how you must feel. I can only offer my most heartfelt apologies."

        red @closedbrow talking2mouth "I don't like it, but I get it. You had no idea if I was even coming back, and I know you and Serena have your own thing happening."

brendan -sad @talking2mouth "Actually, dude, what {i}is{/i} that thing you and Serena have going on? Are you finally dating?"

calem -sad @closedbrow talkingmouth "{size=30}'Finally?'{/size} No, we're not dating. We're just... cohabiting."

brendan @talking2mouth "{w=0.5}.{w=0.5}.{w=0.5}.'Kay, man. I'm pretty sure that's what you start doing {i}after{/i} you've been dating for a while, but maybe things are different in Kalos."

calem @sadbrow talkingmouth "Yes. Yes, they are."

brendan @talking2mouth "Okay, so, uh, tell me if I'm crossing any lines here, but what base have you gotten to?"

calem @angrybrow talking2mouth "My aim is not {i}bases{/i}, Brendan. My aim is to understand and help Serena more than I could previously, as a {i}true friend{/i}."

brendan @talking2mouth "...'Kay. ...So you're still at home base, right?"

calem @closedbrow talking2mouth "I am still at home base, yes. But, again, I am not particularly {i}trying{/i} to hit the ball, I only want an emotional connection with it."

red @confusedeyebrows frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

calem @talkingmouth "I didn't think my metaphor was {i}that{/i} inaccessible."

brendan @happy "Whatever, man. I don't get it, but as long as both of you are getting what you want, that's all I need to know."

calem @sadbrow talkingmouth "{size=30}Well...{/size}"

brendan @talking2mouth "So where's Ethan's room?"

red @talkingmouth "Oh, right, c'mon."

scene suite with splitfade

pause 1.0

show brendan:
    xpos 0.75

show calem:
    xpos 0.25

pause 1.0

show ethan uniform with dis

pause 1.0

ethan @talkingmouth "Oh, hey! I just got back from classes. What're you doing here?"

brendan @talking2mouth "Some of our stuff got mixed up with Blue's. He said that he, uh, he put a hot-pink suitcase in your room? That was mine."

ethan @happy "Oh, yeah, that explains it!"
ethan @closedbrow talking2mouth "{size=30}Wait, why did Blue think the girly suitcase was mine? He put everything else in [first_name]'s room...{/size}"

brendan @talking2mouth "You've seen it, bro?"

ethan @talkingmouth "Sure. I just shoved it underneath my bed."

brendan @happy "Awesome!"

pause 1.0

brendan @closedbrow talking2mouth "Okay, uh, just to be sure, you didn't, like {i}look{/i} in it, did you?"

pause 1.0

show ethan playfuleyes happyeyebrows playfulmouth with dis

pause 1.0

brendan @talking2mouth "Damn, that's embarrassin'. You won't tell anybody, will you?"

ethan -playfuleyes -happyeyebrows -playfulmouth @talkingmouth "Nah, you're good."

red @talkingmouth "Alright. You guys said you wanted to talk with Ethan, right? Mind if I step out? I've got some stuff I want to do before the evening's over."

calem @talkingmouth "Of course. Go ahead."

brendan @happy "Seeya later, bro!"

call freeroam from _call_freeroam_19

scene blank2 with Dissolve(2.0)

call nightroam from _call_nightroam_1

scene blank2

pause 2.0

jump day010513