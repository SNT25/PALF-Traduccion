label Klara1:

$ RecordDate("Klara")

stop music fadeout 1.5

scene relichall_B with Dissolve(2.0)

narrator "Sneaking out of your dorm late at night, careful not to step on that one loose tile near the entryway, to avoid waking up your dormmates, you quickly make your way to the front of Relic Hall, where you expect to find Klara..."

show klara date makeup hardblush at night with Dissolve(3.0)

queue music "audio/music/everyonesfavoritegirl_start.ogg" noloop
queue music "audio/music/everyonesfavoritegirl_loop.ogg"

narrator "And find her you do."

red night @lightblush surprised "...Woah."

klara @sadbrow talkingmouth "H-hi."

pause 1.0

klara @talkingmouth "So... um... what do you think?"

red @sad2eyes sadeyebrows talkingmouth "I'm not sure where to look, to be honest."

klara @puppybrow blush "Oh! Is it... too much?"

menu:
    "It's very charming.":
        $ AddEvent("Klara", "VeryCharming")
        show klara happy with dis

        $ ValueChange("Klara", 10)

        klara @talkingmouth "Aw. You're so incredibly sweet, you know that, [first_name]?"

    "It might be a little bit much.":
        klara @talking2mouth sadbrow "I'm sorry... I just try to make myself look good during dates."
        klara @sadbrow talking2mouth "If I'd known you were just going to wear the same clothes you wear everyday, I wouldn't have put any effort in... that must be so embarrassing for you."
        klara @puppybrow talking2mouth "Can you forgive me for caring so much?"

        red @confused "Y-yeah...?"

red @sweat talking2mouth "A-anyway, where are we going?"

klara @talkingmouth "Oh, there's a little club that we can go into in Inspira! It's a great place to hang out late at night."

red @closedbrow talking2mouth "I think Leaf mentioned that place once or twice."

klara -happy @happy "Hah! Leaf? Like, {i}Leaf{/i} Leaf?"

red @confused "Yeah?"

klara @talkingmouth "That's a pretty funny thought. Um, imagining Leaf at this sort of place."

red @happy "What do you mean?"

klara @talkingmouth "Oh... you know. I mean, Leaf's not really very..."
klara @talking2mouth "Let's just say she couldn't really handle this sort of place."

red @confused "What, is it a rough neighborhood? Is it safe for {i}us{/i} to go here this late?"

klara surprisedbrow frownmouth @closedbrow talking2mouth "[first_name], [first_name]. It's..."

pause 1.0

klara @puppybrow frownmouth "Actually, it's {i}really{/i} scary."
klara @closedbrow talkingmouth "But I want to take you somewhere {i}really{/i} special. Not just some boring Kalosian restaurant you could go to anytime."
klara @puppybrow blush talkingmouth "Will you... protect me?"

red @happy "Of course! Don't worry about it."

if (HasEvent("Klara", "VeryCharming")):
    klara @talkingmouth "Great! Are you going to get changed, then?"

    red @confused "Hm?"

    klara @surprised "Oh! That's what you're going to wear to..."

    klara @talking2mouth sadbrow "I'm sorry... I just try to make myself look good during dates."
    klara @sadbrow talking2mouth "If I'd known you were just going to wear the same clothes you wear everyday, I wouldn't have put any effort in... that must be so embarrassing for you."
    klara @puppybrow talking2mouth "Can you forgive me for caring so much?"

    red @confused "Y-yeah...?"

    klara @happy "Thank you so much. You're so sweet. And don't worry, you don't have anything to be embarrassed about. People will understand."

klara @talkingmouth "The club's this way. Follow me...!"

scene blank2 with splitfade

pause 1.0

scene citystreetnight
show roughneck at night:
    xpos 0.33
show klara makeup date at night:
    xpos 0.66
with splitfade

$ RecordKnownLocations("Klara", "Shady Club")

$ location = "city"

roughneck @confused "You eighteen?"

red night @talkingmouth "Uh, yeah."

roughneck @angry "Hrmm..."

narrator "The burly bouncer looks over you and Klara carefully."

roughneck @talkingmouth "Cause no trouble. If you leave without buying at least two drinks, I'm checking your ids."

red @happy "What? You don't need to do that. I'll show you my ID now."

narrator "You show the unimpressed bouncer your ID."

red @sadbrow talkingmouth "See, eighteen. No problems here."

roughneck @surprised "[first_name] [last_name]. Recognize that name. You're the boss' friend, huh?"

red @happy "Oh, you're one of Silver's guys? Does he run this place?"

roughneck @angry "He ain't got nothin' to do with it. Y'hear?"

red @surprised "Oh... okay!"

redmind @thinking "He seems pretty adamant... maybe he doesn't want Silver to get in trouble for whatever they're doing here."

roughneck @talkingmouth "You're too young for the full package, but you can come inside and get some drinks. Dance, maybe. Just don't ask for anything more."

klara @happy "Alright, we get it. Now, {i}come on{/i}, let's go inside. It's freezing out here."

roughneck @surprised "...Cause no trouble."

scene blank2 with splitfade

pause 1.0

narrator "You step into the nightclub, find a booth, and sit down."

scene nightclub 
show klara makeup date
with splitfade

klara @talkingmouth "Have you ever been here before?"

red @happy "Not nearly cool enough for that. I think Leaf was planning to take me here at one point, though."

klara frownmouth @sadbrow talking2mouth "Are you sure?"

red @confused "Hm? Well, not exactly. But she mentioned it a few times, at the same time she was talking about us going out to the city together."

klara @sadbrow talkingmouth "You know... you shouldn't take everything she says at face value."

red @happy "Oh, jeez, I know. She's really sarcastic."

klara @talkingmouth "Not just that, though."

red @confused "Hm?"

klara @closedbrow talking2mouth "Look, she's a {i}great{/i} friend. Really, she's so... smart and pretty and strong."
klara @sadbrow talkingmouth "But sometimes she makes promises and just... forgets about them."
klara @sadbrow talking2mouth "Something she says matters {i}so{/i} much to her could just... not matter the next day."

red @sad2eyes talking2mouth sadeyebrows "That... doesn't sound like Leaf?"

klara -frownmouth @sadbrow talking2mouth "...Oh, nevermind. Sorry, I didn't want to bring the mood down."
klara @happy "Let's just forget about her. Get some drinks."

red @talking2mouth "The, uh, the drinking age in Kobukan's twenty-one, right?"

klara @surprised "Oh."
klara @happy "Of course! What was I thinking? I'm sorry, in Galar it's eighteen, and I just got confused--"

red @happy "Hey, I don't mind. Go ahead."

klara @talkingmouth "Aw... it's no fun to drink alone."
klara @sadbrow talkingmouth "You won't make me feel lonely when you're right here, will you?"

menu:
    ">Join in with Klara":
        $ AddEvent("Klara", "DrinkWithKlara")
        $ ValueChange("Klara", 10)

        klara @happy "Wow, really? You're so adventurous. I thought because you were so nice and smart that you would be super straight-laced, but..."
        klara @sadbrow talkingmouth "I guess you're a bit of bad boy, huh?"

        red @happy "Well, I don't mean to brag..."

        klara @sadbrow hardblush talkingmouth "I... I find bad boys a bit sexy, actually..."

    ">Leave Klara high and dry":
        klara @talkingmouth "That's alright. I understand that you don't want to take any risks."
        klara @happy "I won't judge you. I think it's really inspiring how you stick to your convictions, even when it might make you seem less cool."

        red @talking2mouth "...Thanks."

        klara @sadbrow hardblush talkingmouth "I... I find the way you don't give into peer pressure a bit sexy, actually..."

red @sad2eyes lightblush talkingmouth sadeyebrows "Ah, geez..."

show klara:
    xpos 0.5
    ease 0.5 xpos 0.66

show femthug angrybrow frownmouth with dis:
    xpos 0.33

femthug @talking2mouth "Yeah, you two going to order something, or just drink our air?"

klara @talking2mouth "I'll take a Lombrero-Schweiß, please."

femthug @closedbrow talking2mouth "Hmph."

redmind @thinking "That's a pretty fancy name."

pause 1.0

femthug @talking2mouth "Hey, what about you?"

if (HasEvent("Klara", "DrinkWithKlara")):
    red @talkingmouth "What do you recommend, Klara?"

    klara @talkingmouth "Oh... right. He'll take a Venoshock."

    red @surprised "Woah. Is that, uh, drinkable?"

    femthug @closedbrow talking2mouth "If you're not a bitch."

    red @sad2eyes angryeyebrows talking2mouth "...Alright."

else:
    red @happy "Just a water for me, please."

    femthug @closedbrow talking2mouth "Got it. Two w--"

    show femthug surprisedbrow frownmouth with dis

    klara @happy "Hey, thanks! That's enough!"

    femthug closedbrow @talking2mouth "...Whatever."

hide femthug with dis

show klara:
    xpos 0.66
    ease 0.5 xpos 0.5

pause 1.0

red @confused "So... what's a Lombrero-Schweiß?"#FIX THIS if they make a Germany region

klara @talkingmouth "Oh, it's a {i}really{/i} strong lager from a region just east of Galar."
klara @happy "But it's crystal clear, so you'd never know, just looking at it. But it's not actually water, it's poison."

pause 0.5

klara @talkingmouth "Tastes completely different, though."

red @closedbrow talking2mouth "Hm."
red @talkingmouth "Could I try a sip?"

klara @surprised "What? No! You're... that would be..."
klara @puppybrow talking2mouth "That would be an indirect kiss."

red @talkingmouth "Oh, right..."

klara @sadbrow talkingmouth "I'm really shy, you know."

red @sadbrow talkingmouth "Sorry."
red @confused "But, hey, how'd a shy girl like you learn about a place like this?"

klara @closedbrow talking2mouth "...Oh. Well, I just kinda... grew up around places like this."

red @talking2mouth "In Galar, right?"

klara @closedbrow talking2mouth "Yeah."
klara @surprisedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
klara @happy "Hah hah! I mean, 'yeppers!'"
klara @talking2mouth "I grew up in Spikemuth. It's a small town in Galar. Most people don't pay attention to it..."
klara @angrybrow shadow wrathmouth "{size=30}Especially after Rose built a {i}roof{/i} over it, just to cut us off from the Corviknight lines.{/size}"
klara @talking2mouth "Anyway, it's a dark place where there isn't much to do except drink, battle, and sing."

pause 0.5

klara @talkingmouth "So there's a {i}lot{/i} of places like this."

red @closedbrow talking2mouth "...Sounds rough."

klara @sadbrow talking2mouth "The Gym Leader, Piers, tries to keep our spirits up by holding concerts for us every week... but..."

pause 0.5

klara @angrybrow talking2mouth "...I guess {i}he's{/i} the only one allowed to sing."
klara @angrybrow wrathmouth shadow "{size=30}Even though {i}he's{/i} the entire reason Spikemuth is a dark shithole, because he's too damn stubborn to just do what Rose wants.{/size}"

red @surprisedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
red @sadbrow talking2mouth "I'm sorry... I don't really understand the situation there, but it sounds rough."

klara @sadbrow talkingmouth "...You really {i}are{/i} sweet."

red @closedbrow talking2mouth "I'm a bit confused, though. Raihan and Nessa wear Galarian gym uniforms, right? And I've seen you wear one, too. Does that mean you worked for Piers?"

klara @happy "Oh, no! No... no, no no. No. Piers trained Dark-types."
klara @sadbrow talkingmouth "I was a Gym Trainer for the {i}Poison-type{/i} gym. In the minor league."

red @confused "Galar has a minor league?"

klara @sadbrow shadow talking2mouth "...Yeah, that's what everyone says."

pause 1.0

redmind @thinking "...The Galarian league sounds complicated."

show klara surprisedbrow frownmouth with dis

red @talkingmouth "How come you're not taking Poison classes at Kobukan, then?"
red @confused "Come to think of it, how come you're at Kobukan at all?"

pause 1.0

klara -surprisedbrow -frownmouth @happybrow talkingmouth "Oh, look, here come our drinks!"

show klara:
    xpos 0.5
    ease 0.5 xpos 0.66

show femthug frownmouth angrybrow with dis:
    xpos 0.33

narrator "The 'hostess' tosses your drinks down on the counter, spilling a few drops, then stands there, waiting expectantly."

femthug @talking2mouth "You pay upfront."

red @talking2mouth "Uh, can we put them on our tab?"

femthug @talking2mouth "No. And there's a mandatory tip. 35%%. Comes out to $470."

redmind @thinking "I have... $[money] right now..."

menu:
    ">Pony up the cash" if (money >= 470):
        $ AddEvent("Klara", "PaidForDrinks")
        redmind @thinking "Well, I'm the guy, so it's the gentlemanly thing to do..."

        $ money -= 470

        narrator "You pay for the drinks."

        $ ValueChange("Klara", 10, 0.66)

        klara @happy "What a gentleman you are!"

    "I can't afford that." if (money < 470):
        $ AddEvent("Klara", "CouldNotAffordDrinks")
        show klara surprisedbrow frownmouth
        show femthug surprisedbrow frownmouth
        with dis

        pause 1.0

        klara @talkingmouth "Oh, you're {i}really{/i} broke."

        femthug @talking2mouth "At least you know girlie here isn't a gold digger."

        red @sad2eyes talking2mouth "Er... sorry. Klara, would you mind?"

        klara @happy "Of course not! I mean, you invited me on this date, and I tried to make myself look really nice for it, {i}and{/i} you're a guy, but that's fine!"
        klara @talking2mouth "I really believe in breaking down gender stereotypes, you know? Who said men have to be manly?"

        red @closedbrow sweat talking2mouth "Sorry."

        narrator "Klara pays for the drinks, though you swear you saw a tiny Dustox fly out of her wallet..."

    ">Look at Klara":
        femthug @talking2mouth "At least you know girlie here isn't a gold digger."

        red @sad2eyes talking2mouth "Er... sorry. Klara, would you mind?"

        klara @happy "Of course not! I mean, you invited me on this date, and I tried to make myself look really nice for it, {i}and{/i} you're a guy, but that's fine!"
        klara @talking2mouth "I really believe in breaking down gender stereotypes, you know? Who said men have to be manly?"

        red @closedbrow sweat talking2mouth "Sorry."

        narrator "Klara pays for the drinks, though you swear you saw a tiny Dustox fly out of her wallet..."

hide femthug with dis

show klara:
    xpos 0.66
    ease 0.5 xpos 0.5

klara @talking2mouth "Alright... bottoms up!"

show blank2:
    ypos 1.0
    linear 0.5 ypos 0.0

narrator "Klara quickly begins drinking, and her cheeks take on a red flush almost immediately."

hide klara

narrator "As for you..."

if (HasEvent("Klara", "DrinkWithKlara")):
    redmind @confusedeyebrows frownmouth "'Venoshock', huh...?"
    redmind @thinking "I'm... pretty sure it shouldn't be bubbling."

    klara blush date makeup @restrainedbrow hardblush talkingmouth "{size=30}No balls.{/size}"

    red @confused "Sorry?"

    klara @surprised "Huh? I didn't say anything."

    redmind @thinking "Okay..."

    narrator "You sniff the Venoshock, and you're pretty sure that its fumes have {i}measurably{/i} lowered your IQ."

    red @happy "Ah, what the hell. I only live once. Gotta be better than Grandpa's moonshine."

    narrator "You take a big swig of the Venoshock, and suddeknly realilsn thae youre havoisnfdn a go od time.. ."

else:
    narrator "You slowly sip your water, watching the other nightclub's patrons."

hide blank2 
show klara makeup date restrainedbrow
with Dissolve(2.0)

klara @restrainedbrow talkingmouth "Heyyyy. Why'ren't you-- why aren't you looking at me?"

if (HasEvent("Klara", "DrinkWithKlara")):
    red noshine @hardblush unamusedbrow talking2mouth "...Colorsh? Colors are... pretty?"
    red @confused "Is... there a window open? I feel coldy. Coldy. Col-dy."
    red @closedbrow talking2mouth "Not that word. I mean... not hot."
else:
    red @talkingmouth "Sorry. Just watching the club. Never been a place like this before. People are pretty, uh, open."

klara restrainedbrow @talkingmouth "Whaaatever. Just look at me. Look, we're on a date. You're dating {i}me.{/i} Before anyone else."

if (GetRelationshipRank("Nessa") > 0 and not HasEvent("Nessa", "DenyDate")):
    if (HasEvent("Klara", "DrinkWithKlara")):
        red @closedbrow talking2mouth "Mmmm... no. Nessha was... Nessa first."
    else:
        red @sadbrow talkingmouth "Sorry. Nessa beat you to the punch first."

    klara @closedbrow talking2mouth "Oh, sheee... she doesn't count. Nope. She doesn't count, and we {i}alllllll{/i} know why."

    if (HasEvent("Klara", "DrinkWithKlara")):
        narrator "yoush gotta big indignant feel but your word-mouthers aren't workign right now,,,"
    else:
        red @closedbrow talking2mouth "Baseless rumors. She's really nothing like what people say."

        narrator "Klara does not appear to be paying attention."

klara @talking2mouth "You knoooow. It's super-cool that you're heere with me now. I feel like I can tell you anything. Everything."

show klara:
    xpos 0.5 ypos 1.0 zoom 1.0
    ease 0.5 ypos 1.2 zoom 1.3

narrator "Klara leans forward provocatively."

klara @talkingmouth "Want to know a secret...?"

if (HasEvent("Klara", "DrinkWithKlara")):
    red @happy "Ssshhure."
else:
    red @confused "Sure?"

klara @happymouth "I'm... not wearing anything underneath this...?"

red @surprisedbrow frownmouth "Oh."

klara @surprised "Oh! ...I can't believe I said that."
klara @hardblush closedbrow talking2mouth "Wow, my drink must be {i}really{/i} strong. There's no way I'm going to remember anything that happens tonight... anything you tell me..."

pause 1.0

klara @puppybrow talking2mouth "I... I told you a really embarrassing secret... so... would you tell me about one of yours...? Since I won't remember, anyway..."

if (HasEvent("Klara", "DrinkWithKlara")):
    show klara surprisedbrow frownmouth with dis

    red @happy "I've gotta friendy-power. It makesh me able to... to make friends more easily."

    klara restrainedbrow @happy "Hah! Silly! I knew that..."
    klara @closedbrow talking2mouth "Everyone knows that..."

else:
    red @sadbrow talkingmouth "Sorry. Only one I can think of is the Frienergy thing. I'm pretty much an open book besides that."

    if (HasEvent("Instructor Karen", 2)):
        red @happy sweat "Instructor Karen's actually got on my case about that."

klara @closedbrow talking2mouth "No secrets... you really are perfect, then."
klara @angrybrow poutmouth "Hmph!"
klara @angrybrow talking2mouth "That'sh... no fun! Tell me something fun!"

if (HasEvent("Klara", "DrinkWithKlara")):
    red @talkingmouth "Shhure. What?"

else:
    red @talkingmouth "Uh-huh. Like what?"

klara @angrybrow happymouth "Tell me... {i}sniff{/i} tell me who youse gotta {i}crush{/i} on!"

if (HasEvent("Klara", "DrinkWithKlara")):
    red @closedbrow talking2mouth "Hm... I geuss there's nothing wrong with telling her..."

$ pickednames = []

label crushpick:

$ pronoun = "him"

menu:
    "A man...":
        $ pronoun = "him"
        menu:
            "Blue" if ("Blue" not in pickednames):
                $ pickednames.append("Blue")
                klara @surprised "Nooo way! He's such an arse... he's always {i}whining{/i}, and I think he's got some weird sub/dom thing going on with Yellow. He's the kind of tiny-dicked loser who'd buy a lifted truck."
                klara @sadbrow talkingmouth "Besides... you know he really hates you, right?"

            "Brendan" if ("Brendan" not in pickednames):
                $ pickednames.append("Brendan")
                klara @happy "You're not serious? Brendan's a {i}total{/i} wimp! He tries to seem like he's tough by working out, but he just lets May run all over him! And he knows how to {i}sew.{/i} C'mon. A guy who sews? We know what that means."
                klara @sadbrow talkingmouth "Besides... I've heard a lot of people say that Brendan's scared you'll steal May from him, and is only nice to you to get on your good side. That's a dead end."

            "Calem" if ("Calem" not in pickednames):
                $ pickednames.append("Calem")
                klara @sadbrow talking2mouth "Oh... that's not a good idea. Calem is really... I mean, he's nothing. He's so fake, just trying to get on {i}everyone's{/i} good side."
                klara @closedbrow talking2mouth "Besides... he's totally jealous of you. He was actually {i}happy{/i} when the Student Council thing happened, because now people like him more than you."

            "Cheren" if ("Cheren" not in pickednames):
                $ pickednames.append("Cheren")
                klara @surprised "Oh my god, I was right? Look, you don't want to mess with Cheren. He literally hates you for no reason."
                klara @sadbrow talking2mouth "I know what unrequited love feels like, but all he wants to do is kick you down and laugh at you... and not in a sexy way."

            "Ethan" if ("Ethan" not in pickednames):
                $ pickednames.append("Ethan")
                klara @sadbrow talking2mouth "That's sad. I just... I don't think you should get too comfortable with Ethan around. He's probably going to go away someday."
                klara @sadbrow talkingmouth "I mean, yeah, he's really jealous of you, but a lot of people have said they heard him say stuff... concerning stuff... he's kinda unreliable, you know? Always disappearing and changing his mind on stuff."

            "Grusha" if ("Grusha" not in pickednames):
                $ pickednames.append("Grusha")
                klara @surprised "What, seriously? But he's so... mopey."
                klara @closedbrow talking2mouth "Okay, maybe I'm being a bit unfair, but I've gone through some hard times, too, and I'm not just giving up like he is. Seeing him be such a quitter is kinda lame. Like, how hard is it to {i}smile{/i}?"

            "Hilbert" if ("Hilbert" not in pickednames):
                $ pickednames.append("Hilbert")
                klara @angry "No way! You deserve better! Hilbert's a whiny snot-nosed kid who can't even tie his own shoe laces."
                klara @sadbrow talkingmouth "He's always complaining about 'vengeance' this, and 'retribution' that... but he can't even make his own breakfasts without help, so it's kinda pathetic. Imagine if {i}you{/i} had to take care of him!"

            "Nate" if ("Nate" not in pickednames and not HasEvent("Klara", "DrinkWithKlara")):
                $ pickednames.append("Nate")
                klara @sadbrow talking2mouth "Nate? No way. he doesn't take anything seriously. And he spreads bad rumors about people, too."
                klara @surprised "Oh! I've heard a lot of rumors about you--I bet Nate was the one who spread them!"
                klara @angry "And he pretends to be your friend!"

            "Blake" if ("Blake" not in pickednames and HasEvent("Klara", "DrinkWithKlara")):
                $ pickednames.append("Blake")
                klara @angry "Oh, Blake! Blake is the worst! Blake is..."
                klara @surprised "Wait, who's Blake?"

                redmind @thinking "Oopsh."

                red @happy "I meant... Nate."

                klara @sadbrow talking2mouth "Nate? No way. He doesn't take anything seriously. And he spreads bad rumors about people, too."
                klara @surprised "Oh! I've heard a lot of rumors about you--I bet Nate was the one who spread them!"
                klara @angry "And he pretends to be your friend!"

            "Raihan" if ("Raihan" not in pickednames):
                $ pickednames.append("Raihan")
                klara @happy "Oh, gag me with a spoon! Okay, here's a bit of Galarian gossip--everyone knows that Leon goes way easy on him."
                klara @talkingmouth "It's kinda sad. He says he could be a champion in any region other than Galar, but Leon just lets him {i}think{/i} that."
                klara @sadbrow talkingmouth "Of course, influencers are just like that. It's all about the brand. So fake. Even if you think you're friends, you're just a novelty snapshot on his RotoPhotos, you know?"

            "Silver" if ("Silver" not in pickednames):
                $ pickednames.append("Silver")
                klara @surprised "Huh? Silver? That disciplinary committee guy?"
                klara @sadbrow talkingmouth "I'm pretty sure you should stay away from him... he's kinda a thug, you know? Some people say he uses his Pokémon to attack people outside of school, and even steals Pokémon."
                klara @sadbrow talking2mouth "How else did he get so many Pokémon? You should probably watch your Poké Balls when he's around."

            "Wally" if ("Wally" not in pickednames):
                $ pickednames.append("Wally")
                klara @closedbrow talking2mouth "Oh... sweetie, no. No, no, no. Don't do that."
                klara @sadbrow talking2mouth "He's one of those dating-game obsessed losers who always smell... funky. You know? He has way too many action figures for an 18-year-old guy."
                klara @talking2mouth "And, I mean, he's only getting close to you to get stronger. As soon as he can beat you, it's over. Besides, he's trying to break up May and Brendan."
                
            ">Go back":
                jump crushpick

    "A woman...":
        $ pronoun = "her"
        menu:
            "Bea" if ("Bea" not in pickednames):
                $ pickednames.append("Bea")
                klara @talking2mouth "Oof. I hate to say this, but, uh, little Galarian tip... Stow-On-Side girls aren't really... loyal."
                klara @sadbrow talkingmouth "They're pretty much all about, um... getting physical. But there isn't much going on upstairs, and when you aren't a 'new experience' anymore..."

            "Bianca" if ("Bianca" not in pickednames):
                $ pickednames.append("Bianca")
                if (IsBefore(31, 5, 2004)):
                    klara @surprised "Oh. You know what happened last week, right?"
                else:
                    klara @surprised "Oh. You remember what happened with her Dad a while ago, right?"
                klara @sadbrow talking2mouth "It's so sad. My heart breaks for her. ...But, like, that's a {i}really{/i} weird coincidence, that her father died {i}right{/i} after she told everyone she hated him, right?"
                klara @closedbrow talking2mouth "She does so much for so many people, but... like, I have to wonder {i}why{/i} she wants so many people in debt to her, you know?"

            "Dawn" if ("Dawn" not in pickednames):
                $ pickednames.append("Dawn")
                klara @closedbrow talking2mouth "Oh... that's a time bomb."
                klara @sadbrow talkingmouth "She kinda just does whatever the strongest person around her says, you know? Maybe that's you for a while, but what if someone bigger and stronger comes along, and decides they want her?"
                klara @closedbrow talking2mouth "Relationships shouldn't be based on fear or submission, because those fade. Only loyalty doesn't."

            "Erika" if ("Erika" not in pickednames):
                $ pickednames.append("Erika")
                klara @surprised "Wait... {i}Erika?{/i}"
                klara @sadbrow talkingmouth "What does she even have, besides her Daddy's money? I mean, even she knows that. She acts like the 'perfect daughter' so Daddy won't cut her off the credit card."
                klara @closedbrow talking2mouth "If she didn't have that, no-one would even tolerate her. She can't say 'hi' without quoting some dead Galarian!"

            "Flannery" if ("Flannery" not in pickednames):
                $ pickednames.append("Flannery")
                klara @talking2mouth "Aw, you're so kind! That's really great. Flannery could totally use a nice, stable, person like you to be around while she's waiting for her schizo meds to hit."
                klara @happy "Of course, that's just a short-term thing! Just like her lovely personality, every relationship with Flannery's going to disappear when morning comes."

            "Gardenia" if ("Gardenia" not in pickednames):
                $ pickednames.append("Gardenia")
                klara @talking2mouth "I mean, that's fine, if you want to have to pay her every time you want to shag."
                klara @sadbrow talkingmouth "She {i}only{/i} thinks of money, [first_name]. You should have someone who thinks of {i}you.{/i}"

            "Hilda" if ("Hilda" not in pickednames):
                $ pickednames.append("Hilda")
                klara @talkingmouth "Oooh... I wouldn't. She's so short-tempered, always yelling and screaming, and she talks like an eight-year-old who just looked up 'cuss words' on the internet."
                klara @sadbrow talkingmouth "Besides, there's something very unhealthy about whatever she's got going on with Hilbert. I think she {i}likes{/i} having him need her."

            "Janine" if ("Janine" not in pickednames):
                $ pickednames.append("Janine")
                klara @talkingmouth "...I mean, everyone says she's so cool and powerful, but she's been at Kobukan for three years. That's {i}the definition{/i} of a Super Senior."
                klara @sadbrow talkingmouth "I think she knows that she's hit her peak, and the only way she can feel relevant is by bullying brand-new trainers... and the way she runs the Battle Team is shit, anyway. She has no idea what she even wants."

            "Jasmine" if ("Jasmine" not in pickednames):
                $ pickednames.append("Jasmine")
                klara @surprised "Seriously?! Wow, you must be patient."
                klara @sadbrow talkingmouth "Look, I get that it's important to her, but I {i}hate{/i} how every single conversation with her, she has to bring up that she's sick. Like, yeah, we get it."
                klara @closedbrow talking2mouth "She doesn't have to make it her {i}whole personality.{/i} Everyone gets sick! It's not that interesting!"

            "Professor Cherry" if ("Professor Cherry" not in pickednames):
                $ pickednames.append("Professor Cherry")
                klara @surprised "Not touching that one with a ten-meter pole."
                klara @angrybrow talking2mouth "I mean, she's a Professor... and a weird one, besides. You know, everyone says she's stalking one of her students. Actually, maybe she'd go for it, after all... but that's not a good thing!"

            "Leaf" if ("Leaf" not in pickednames):
                $ pickednames.append("Leaf")
                klara @talking2mouth "...I'd be careful about her. She doesn't really mean the things she says, you know?"
                klara @closedbrow talking2mouth "Like, she'll say that she wants to go on a date... then push it off for a month, hoping you forget about it."
                klara @sadbrow talking2mouth "Or she'll say you're besties, then never mention you to her friends, like with me..."

            "May" if ("May" not in pickednames):
                $ pickednames.append("May")
                klara @sadbrow talking2mouth "Oh, no, that's a bad idea. I mean, have you seen what she did to Brendan? She's a total control freak."
                klara @closedbrow talking2mouth "She's got Brendan on a leash, and although I bet she wouldn't mind adding another puppy to her pack, you don't want to be there when she yanks the chain."

            "Misty" if ("Misty" not in pickednames):
                $ pickednames.append("Misty")
                klara @happy "Oh, I get it! You like tsunderes!"
                klara @sadbrow talkingmouth "I'm sorry, though, she... she's not one. She actually just hates everyone. If it ever seems like she's calmer, it's just her meds kicking in. I think she needs some stronger ones..."

            "Nessa" if ("Nessa" not in pickednames):
                $ pickednames.append("Nessa")
                klara @closedbrow talking2mouth "Why does the phrase 'dead fish' come to mind...?"
                klara @sadbrow talkingmouth "But you probably wouldn't want to get there, anyway. I mean, she's a 'model', and from Hulbury, besides. I guess you don't know, since you're not Galarian, but..."
                klara @closedbrow talking2mouth "Well, Hulbury gets a lot of {i}male{/i} tourists."

            "Rosa" if ("Rosa" not in pickednames):
                $ pickednames.append("Rosa")
                klara @sadbrow talkingmouth "...Next time you have a chance, take a look at her. Like, really, look at her. She wears enough makeup to drown in."
                klara @closedbrow talking2mouth "You can't trust actors. They spend their lives lying. And she's probably got dibs called on her by half of Pokéstar Studios, anyway..."

            "Sabrina" if ("Sabrina" not in pickednames):
                $ pickednames.append("Sabrina")
                klara @talking2mouth "Oh, no. Nuh-uh. She knows {i}everything{/i} we're thinking. Good luck ever trying to surprise her with flowers."
                klara @sadbrow talkingmouth "Besides... someone who can't control her powers, who gets angry so easily, who doesn't mind using her powers to hurt people... are you sure she should even be here at school?"
                klara @sad "I mean, I've put this thought in your head, so what if she reads it now, and gets angry? That's not your fault, but she'll still hate you for it."

            "Serena" if ("Serena" not in pickednames):
                $ pickednames.append("Serena")
                klara @talking2mouth "No way! Have you seen how she looks at Calem? I mean, if you're fine being a second choice..."
                klara @sadbrow talkingmouth "I don't think you should ever settle for someone who will give up as soon as she gets what she wants."

            "Skyla" if ("Skyla" not in pickednames):
                $ pickednames.append("Skyla")
                klara @happy "Hah! That's {i}so{/i} funny."

                pause 1.0

                klara @surprised "Wait, you were serious? But... she dresses like a stripper, has the mentality of a nine-year-old, and is part of the Disciplinary Committee..."

            "Sonia" if ("Sonia" not in pickednames):
                $ pickednames.append("Sonia")
                klara @closedbrow talking2mouth "...I'll just say it. They're not real. They put the {i}bolt{/i} in bolt-ons."
                klara @sadbrow talkingmouth "What's more, I mean, there has to be a reason Raihan and Nessa let her hang around them, right?"
                klara @talkingmouth "Maybe it's pity. Frankly, I'm not convinced she's a girl."

            "Tia" if ("Tia" not in pickednames):
                $ pickednames.append("Tia")
                klara @talking2mouth "If you told anyone else that, they'd put you on a list."
                klara @sadbrow talkingmouth "I mean, she doesn't speak, she's tiny, she's got some form of brain damage..."
                klara @sadbrow talking2mouth "She feels more like a collection of tags on an adult website than a person."

            "Whitney" if ("Whitney" not in pickednames):
                $ pickednames.append("Whitney")
                klara @surprised "Wh-Whitney?!"
                klara @sadbrow talkingmouth "Look, I have nothing against lesbians, but she's, like, {i}the definition{/i} of a predatory lesbian."
                klara @sadbrow talking2mouth "She's got more girls wrapped around her fingers than spaghetti around a fork. She just likes having them."

            "Yellow" if ("Yellow" not in pickednames):
                $ pickednames.append("Yellow")
                klara @closedbrow talking2mouth "...She's a good doormat, but I don't think you want to try doing anything serious with her."
                klara @sadbrow talkingmouth "I guess unless you're okay with never hearing the word 'no.' I guess some guys might be into that."
                klara @closedbrow talking2mouth "I just can't imagine interacting with someone with so little backbone like they're an actual person."

            ">Go back":
                jump crushpick

    "No-one, I guess." if (len(pickednames) > 0):
        jump aftercrushes

klara @surprised "Oh. I mean, that's just what I've {i}heard!{/i} I, personally, actually like [pronoun] a lot!"

jump crushpick

label aftercrushes:
    
klara @surprised "Noooo-one? So that means you..."
klara @happy "That means you're... available?"

if (HasEvent("Klara", "DrinkWithKlara")):
    narrator "shomeshing sheemssss ... SUS"

    red @happy hardblush "I guesss!"

else:
    red @confused "Well, we're... dating right now, so I guess?"

    show klara surprisedbrow frownmouth with dis

    red @talkingmouth "Also, wow, you sobered up quickly."

    klara @happy "Whaaa...? Noooo. I'm still totally drunk right now. Wow, I'm dizzy. But who says dating has aaaaa~nything to do with being available...?"

klara @happy "Hah, you're shoooo... innocent."
klara @talkingmouth "I... like that."

pause 1.0

klara @talkingmouth "But... I want to make you... {i}not.{/i}"

red @confusedeyebrows frownmouth "Hm?"

klara @talkingmouth "...Thish place is pretty boring, right? Why don't we go back to campus?"

if (HasEvent("Klara", "DrinkWithKlara")):
    red @happy hardblush "Sure! Mebbe... the cold air'll clear... our heads."

else:
    red @talkingmouth "Sure thing. It's a good thing I didn't get a drink. I'd be worried about you getting back to your dorm without being seen, the way you are now."
    red @talkingmouth "Maybe the cold air'll clear your head."

scene blank2 with splitfade

$ location = "school"

narrator "Klara leads you with confidence back to campus, humming a little song..."
narrator "The crisp night air quickly sobers you up, and you can tell your senses have almost entirely returned by the time you reach Relic Hall. To your surprise, though, Klara keeps striding forward, walking right past your dorm hall."

redmind night @confusedeyebrows frownmouth "...Huh. I think I recognize that tune. Doesn't it come from, like, a fast food commercial?"

pause 1.0

if ("Blue6" in battlehistory):
    red @confused "Wait... where are we going?"

    klara night makeup date hardblush @talkingmouth "Somewhere fun.~"
else:
    red @confused "Wait... are we going where I think we're going?"

    klara night makeup date hardblush @talkingmouth "Depends if you think we're going somewhere fun."

redmind @confusedeyebrows frownmouth "Somewhere fun...?"

pause 1.0

show midnight at vspaz 

pause 3.5

hide midnight

scene facultypoolnight 
show klara hardblush date makeup 
with splitfade

$ RecordKnownLocations("Klara", "Faculty Pool")

if ("Blue6" not in battlehistory):    
    red @talking2mouth "Wait. The pool? No... this isn't the student pool. What is this?"

    klara @talkingmouth "I... guess you don't know about this place, then."

    red @confused "Uh, no. I just established this."

    klara @closedbrow talkingmouth "This pool is... hm hm hm."
    klara @restrainedbrow talkingmouth "Private."
    klara @talkingmouth "And soundproof. And no-one ever comes in here, except to do one thing."

    red @sweat talking2mouth "Battle...?"

    klara @anger happymouth happybrow "You know that's not it."

else:
    red @surprisedbrow frownmouth hardblush "{w=0.5}.{w=0.5}.{w=0.5}."

    klara @talkingmouth "Oh, you... you know about this place, then."

red @talking2mouth "Well... geez, I mean, Klara, I'm really flattered, but we're moving pretty fast, aren't we?"

if (IsDate(25, 5, 2004)):
    redmind @thinking "I mean, I met her yesterday..."
elif (IsBefore(30, 5, 2004)):
    redmind @thinking "I mean, I only met her this week..."

klara @happy "Whhhhat are you being so serious about? C'mon. We're just going to have fun. We don't need to... {w=0.5}{i}*hic*{/i} make it {i}mean{/i} anything."

narrator "You suddenly become {i}very{/i} aware of your own breathing. Sweat begins to form on your brow, your hat's brim betraying you by keeping in the heat."

menu:
    ">Give in to desire":
        jump twobecomeone

    "Klara, you're drunk.":
        $ AddEvent("Klara", "YouAreDrunk")
        show klara surprisedbrow frownmouth with dis

        pause 1.0

        klara -surprisedbrow -frownmouth -surprised @happy "Oh, aren't you {i}such{/i} a gentleman. I'm not, though."

        red @talking2mouth "Huh? You were staggering the entire way back."

        klara @happy "Yyyyeah. I'm fine now, though. Lombrero-Schweiß wears off quickly."

        red @sad2eyes talking2mouth "I'm... not sure."

        klara @sadbrow talkingmouth "...[first_name]. Come on. It's fine."
        klara @puppybrow talkingmouth "I want this, okay? With you. Now."

        menu:
            ">Give in to desire":
                jump twobecomeone

            "I'm sorry, no.":
                show klara surprisedbrow frownmouth with dis

                pause 1.0

                klara angrybrow frownmouth shadow @talking2mouth "...Why?"

                red @sadbrow talkingmouth "Hey, it's nothing about you. It's just--"

                klara @closedbrow talking2mouth "I don't need to hear it. 'It's not you, it's me.' I've heard that eight times."
                klara @angrybrow talking2mouth "Fine. I put on the sluttiest thing I could find, basically {i}threw{/i} myself at you all night, but I get it. You're 'classier' than me, or whatever."

                pause 1.0

                klara -angrybrow -frownmouth -shadow @happy "Hah hah! {w=0.5}Just kidding! {w=0.5}It's {i}totally{/i} fine. I really love how you stick to your principles like that."
                klara @sadbrow talkingmouth "Maybe... just don't tell anyone about this? I don't want rumors spreading about, you know."

                red @sadbrow talkingmouth "Of course. Wouldn't dream of it." 

                klara restrainedbrow frownmouth @happy "Thanksee!~"

                hide klara with dis

                pause 3.0

                redmind fullblush surprisedbrow frownmouth "Holy shit. This is the craziest thing that has happened to me all year, and I'm counting the alien and extinct Super-Pikachu in that."

                scene blank2 with splitfade

                narrator "You quickly make your way back to your dorm, avoiding that one loose tile, and sneak back to your bedroom."

                pause 0.5

                narrator "Though, of course, you cannot sleep a wink, and end up staring at the ceiling for hours until your alarm goes off."

                $ oldrelationship = GetRelationship("Klara")
                $ persondex["Klara"]["Relationship"] = "Rejector"
                $ persondex["Klara"]["RelationshipRank"] = 1

                $ PlaySound("sav.ogg")

                narrator "Your heart shifts as you feel your relationship with Klara evolve from '{color=#0048ff}[oldrelationship]{/color}' to '{color=#0048ff}Rejector{/color}'!"

                return

label twobecomeone:
    
$ AddEvent("Klara", "FirstBase")
$ RecordCasualRelationship("Klara")

show klara closedbrow kissmouth:
    ypos 1.0 zoom 1.0
    ease 5.0 ypos 1.2 zoom 1.3

show blank:
    alpha 0.0
    linear 5.0 alpha 1.0

narrator "You approach Klara cautiously as she closes her eyes, lips parted expectantly..."

pause 2.0

narrator "And then a curtain of white descends on the scene."
narrator "The performances of the actors; the contents of the script; such things can only be guessed at from our seat in the audience."
narrator "Though the play is an act, a farce, and naught but show--"

pause 2.0

narrator "Lack of truth is not ineluctably a trammel to enjoyment."

pause 2.0

narrator "The night passes swiftly, and by the time the sun rises, it casts its judgmental rays on no trace of the memories made last night."

$ oldrelationship = GetRelationship("Klara")
$ persondex["Klara"]["Relationship"] = "L'Amour"
$ persondex["Klara"]["RelationshipRank"] = 1

$ PlaySound("sav.ogg")

narrator "Your heart shifts as you feel your relationship with Klara evolve from '{color=#0048ff}[oldrelationship]{/color}' to '{color=#0048ff}L'Amour{/color}'!"

return