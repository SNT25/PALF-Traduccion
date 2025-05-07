label day010425:
$ timeOfDay = "Morning"
call clearscreens from _call_clearscreens_70
call calendar(1) from _call_calendar_20
$ calDate = calDate.replace(day=25, month=4, year=2004)

$ HealParty()

stop music

scene blank2
show morning at vspaz

pause 3.5

queue music "Audio/Music/Road to Viridian City.ogg"

scene hall_A with Dissolve(2.0)
$ renpy.transition(dissolve)
show screen currentdate

show sonia frownmouth at rightside 
show dawn frownmouth at leftside:
    ypos 1.0 rotate 0
with dis

sonia @talking2mouth "Yeah, so, that's... that's my situation. Um. So, if you, y'know, have any odd jobs for me... I'd be right chuffed if you let me know."

dawn @sad "Yeah, I... I don't think that'll happen, but, uh, I'll mind you in keep."
dawn @surprised "Keep! I'll keep you in mind! Uh, sorry! Sorry. Is what I meant to say. Sorry that I can't think of anything I could hire you for."

sonia @sadbrow happymouth "N-no. No need to worry about that. Um... just, you know... 'mind me in keep,' heh heh..."

pause 1.0

redmind @frownmouth confusedeyebrows "This is...{w=0.5} {i}physically{/i} painful. Maybe I should step in."

sonia @closedbrow talkingmouth "I just... Since we're on the Battle Team together, I thought I'd mention. I just {i}really{/i} need to get some money quick, or else... in five months..."

show dawn surprisedbrow frownmouth
show sonia surprisedbrow frownmouth
show gardenia behind sonia:
    xpos 1.2 ypos 1.0
    parallel:
        easein 0.3 ypos 0.7
        easeout 0.3 ypos 1.0
    parallel:
        ease 0.6 xpos 0.5
with dis

pause 1.0

gardenia @angrybrow happymouth "Did someone say 'money quick?!'"

sonia -surprisedbrow -frownmouth -surprised @surprised "Um, yes, I--"

show gardenia happy with dis:
    ease 0.4 xpos 0.25 xzoom -1

show dawn behind gardenia:
    xpos 0.25
    pause 0.3
    ease 0.3 xpos -0.2 rotate -40

$ PlaySound("thud2.ogg")

gardenia @talkingmouth "Fantastic!"
gardenia -happy @angrybrow happymouth "Sonia, you and I, we're going to rule this school. You know what we're surrounded by?"

show sonia:
    xpos 0.75
    pause 0.2
    ease 0.5 xzoom -1
    pause 0.5
    ease 0.5 xzoom 1

pause 1.5

sonia @surprised "Paintings?"

gardenia @surprised "Huh... yeah, they're probably worth something, too. But no, not that."
gardenia @happy "I'm surprised you haven't thought of it first, actually."
gardenia @angrybrow happymouth "We're surrounded by {w=0.5}thick, {w=1}oversized, {w=1.5}bulging, {w=2.0}{i}wallets.{/i}"

sonia @sad "I... I don't..."

gardenia @happy "{i}Everyone{/i} in this school is filthy rich. Besides you. And it sounds to me like you might appreciate a little redistribution of assets."

sonia @surprised "Are you trying to get me to join a campus political group?"

gardenia @happy "Not even! Politics is the small man's game. They can paint the car any color they want, but it's the people with the money who decide how it drives."

sonia @sad "I'm {i}so{/i} lost."

gardenia @talkingmouth "Then it's a good thing I found you. Sonia, I'm offering you my hand in collaboration. I'm the only self-made woman in this entire school."
gardenia @talking2mouth "Everyone else? They're here on Mommy or Daddy's money. I'm here because I raised the funds myself, and worked hard for it, for over a decade."

sonia @angrybrow talking2mouth "You must be very proud, but I don't see..."

gardenia @happy "Take it from this self-made woman, Sonia of the Battle Team. There are a dozen different ways you could make the money needed to pay off your tuition before the deadline."

pause 1.0

sonia @angrybrow talking2mouth "I'm not going to sell my body."

pause 1.0

gardenia @happy "There are {i}eleven{/i} different ways you could make the money needed!"

sonia @closedbrow talkingmouth "...Like?"

python:
    """
    gardenia @talking2mouth "If you want to stay legal with it, investment's your best bet." 
    gardenia @happymouth "I have a deal with a bunch of stores in town. I give them a bunch of money, they place orders for new product lines, students go to the stores, and the stores share a split of the revenue with me."
    gardenia @angrybrow happymouth "[bluecolor]I get more money, and the more money I get, the more products they sell! Poké Balls, potions, even stat enhancers!{/color} It's a win-win! And it could be a win-win-win if you join in!"

    sonia @talking2mouth "...And this is profitable?"

    gardenia @happy "To the tune of $300,000 a month! And that number's only growing."
    gardenia @talkingmouth "If you get in on the ground level now, the dividends will be {i}immense.{/i}"

    sonia @sad "This... sounds a lot like a pyramid scheme."

    gardenia @talking2mouth "Oh, yeah, it totally is. But you'd be on the second layer of it. Don't you know the rules? Never join a pyramid scheme {i}unless{/i} you're the first to join."

    pause 1.0

    gardenia @happy "Oh, and you {i}would{/i} be. I may be a little bit obsessed with money, but I can promise you I'm not a liar."

    pause 1.0
    """

gardenia @happy "Banking! I've got a little bank myself, the 'Felicity Bank', that I decided to run out of the goodness of my own heart, for all the Kobukan Students."
gardenia @talking2mouth "Tired of wiping out against wild Pokémon and dropping money on the way out? Afraid of getting into Gamble Battles against stronger opponents? This is the solution!"
gardenia @closedbrow talking2mouth "Plus, there's an {i}extremely{/i} generous interest plan attached. The more money you put in, the more I'll automatically deposit into your bank every day."
gardenia @talkingmouth "Obviously, you can deposit or withdraw money from it whenever you want--I don't hold inconvenient, customer-unfriendly hours like the banks in town."

sonia @closedbrow sadmouth "*Sigh*.{w=0.5} How much to join?"

gardenia @happy "I'll let you buy in for a modest $1,000 fee. You literally {i}can't{/i} get a better deal than that. For the price of a small burger, I'll loop you into a deal with an {size=25}(almost){/size} [bluecolor]{i}guaranteed{/i} 1%% rate of return every day.{/color}"

#sonia @surprised "Every school day... so weekends are out."

#gardenia @sadbrow talking2mouth "Well, yeah. I mean, I hand-deliver your dividends. That's a quality service, you know! And I'm busy on weekends."

pause 1.0

gardenia @happybrow frownmouth "Actually, how would you feel about signing up for my gym class? I run it on weekends. We could work on burning off some of that excess fat, eh?"

sonia @sad "...I like my 'excess fat.'"

gardenia @surprised "Huh! And here I was, thinking you just couldn't find a shirt that fit."

pause 1.0

sonia @closedbrow talking2mouth "Look, about the investment, I..."

menu:
    "Sonia, don't!":
        show sonia surprisedbrow frownmouth
        show gardenia surprisedbrow frownmouth
        with dis

        gardenia -surprisedbrow -frownmouth -surprised @surprised "Eh?"

        #red @closedbrow talking2mouth "Yeah, I've been here the whole time. Sonia, c'mon. It's a pyramid scheme. Gardenia even {i}admitted{/i} it's a pyramid scheme. Don't fall for that."

        red @closedbrow talking2mouth "Yeah, I've been here the whole time. Sonia, c'mon. This is shady as hell. We have no idea what Gardenia's going to do with our money."

        sonia -surprisedbrow -frownmouth -surprised @talking2mouth "I'm... I'm just... I'm desperate, [first_name]."

        menu:
            "I'll pay for you.":
                sonia @surprised "Really?"

                if (money >= 1000):
                    red @happy "Yeah. Money's a bit tight for me, too, but what's it for, if not for helping friends?"

                    $ money -= 1000

                    show sonia happy with dis

                    $ ValueChange("Sonia", 3, 0.75)

                    redmind @thinking "Ow. That hurt my wallet. But at least she's happy now."
                else:
                    red @surprisedbrow "{w=0.5}.{w=0.5}.{w=0.5}."

                    red @sad "Ah... sorry. I don't actually have enough money..."

                    show sonia sad with dis

                    $ ValueChange("Sonia", -1, 0.75)

                    sonia "Oh..."

                gardenia @surprised "Well, that was weirdly gallant."

                gardenia @happy "Damn, I need to get a shirt like that. Then I can get myself a guy who'll pay for stuff!"

                if (not WonBattle("FlanneryGardenia1")):
                    red @confused "Didn't you take enough of my money in that gamble battle last Friday?"

                    gardenia @happy "Not nearly enough, no."
                
                else:
                    red @happy "Sure. I'll be paying with your money, if that gamble battle from last Friday is any indication."

                    gardenia @angrybrow happymouth "Well, aren't you {i}cocky.{/i} I'll get that money back, believe me."

                gardenia @talkingmouth "Anyway, if either of you want to chat, [bluecolor]find me at the baseball field! I'm always down to talk business.{/color}"

            "There's another way.":
                sonia sad "...Yeah. Probably..."

                pause 1.0

                gardenia happy "Well, that sucks. [bluecolor]But if either of you change your mind and want to invest smartly, meet me at the Baseball Field!{/color}"

                hide gardenia with dis

                sonia "I..."

                pause 1.0

                hide sonia with dis

    "Wait, I want in!" if money >= 1000:
        show sonia surprisedbrow frownmouth
        show gardenia surprisedbrow frownmouth
        with dis

        gardenia -surprisedbrow -frownmouth -surprised @surprised "Eh?"

        $ ValueChange("Gardenia", 3, 0.25)

        gardenia @happy "Well, sure! Not a problem with me! The more we all bank, the more we all get!"

        #sonia -surprisedbrow -frownmouth -surprised @sad "Wait... will that mean... would I get less, then?"

        #gardenia @talking2mouth "Nah, don't worry about that. You'd enter in on the same level."

        red @happy "$1,000, right? I'll pay that right now."

        $ money -= 1000
        $ bank += 1000
        $ highestbank = 1000

        gardenia @happy "Pleasure doing business with you!"

        sonia @talking2mouth "Ah... right. I'm... I'm not sure if I..."

        pause 1.0

        sonia @sad "I don't have any money on me."

        menu:
            "I'll pay for you.":
                sonia @surprised "Really?"

                if (money >= 1000):
                    red @happy "Yeah. Money's a bit tight for me, too, but what's it for, if not for helping friends?"

                    $ money -= 1000

                    show sonia happy with dis

                    $ ValueChange("Sonia", 3, 0.75)

                    redmind @thinking "Ow. That hurt my wallet. But at least she's happy now."
                else:
                    red @surprisedbrow "{w=0.5}.{w=0.5}.{w=0.5}."

                    red @sad "Ah... sorry. I don't actually have enough money..."

                    show sonia sad with dis

                    $ ValueChange("Sonia", -1, 0.75)

                    sonia "Oh..."

                gardenia @surprised "Well, that was weirdly gallant."

                gardenia @happy "Damn, I need to get a shirt like that. Then I can get myself a guy who'll pay for stuff!"

                if (not WonBattle("FlanneryGardenia1")):
                    red @confused "Didn't you take enough of my money in that gamble battle last Friday?"

                    gardenia @happy "Not nearly enough, no."
                
                else:
                    red @happy "Sure. I'll be paying with your money, if that gamble battle from last Friday is any indication."

                    gardenia @angrybrow happymouth "Well, aren't you {i}cocky.{/i} I'll get that money back, believe me."

                gardenia @talkingmouth "Anyway, if either of you want to chat, [bluecolor]find me at the baseball field! I'm always down to talk business.{/color}"

            ">Stay silent":
                gardenia @happy "Totally fine! When you get the money together, just [bluecolor]find me at the baseball fields.{/color}"

                sonia @closedbrow talkingmouth "Right-o. I'll keep that in mind, then."
                sonia @sadbrow talkingmouth "Ah... thanks for the hand."

                gardenia @happy "Hey, the invisible hand of the free market gave me a boost up. It's only right I spread the love."

    ">Stay silent":
        sonia @talking2mouth "Alright. I... I don't have the money on me, right now. When I get it, where should I find you?"

        gardenia @happy "I knew you had some business savvy about you! [bluecolor]If you want to deposit or withdraw any money, you can find me at the baseball fields.{/color}"

        sonia @closedbrow talkingmouth "Right-o. I'll keep that in mind, then."
        sonia @sadbrow talkingmouth "Ah... thanks for the hand."

        gardenia @happy "Hey, the invisible hand of the free market gave me a boost up. It's only right I spread the love."

        #redmind @thonk "Hm... sounds kinda sketchy, but it might be worth checking out. The stock of the shops in-town could definitely do with a bit more attention."

hide gardenia 
hide sonia
with dis

pause 2.0

dawn @talkingmouth "Guys? I fell into a vase, and I can't get out."

pause 1.0

dawn @talkingmouth "Hello?"

pause 1.0

dawn @talkingmouth "Somebody?"

pause 1.0

dawn @talkingmouth "I guess this is my life now..."

call freeroam from _call_freeroam_10

stop music fadeout 1.5

queue music "audio/music/eterna_start.ogg" noloop
queue music "audio/music/eterna_loop.ogg"

scene dorm_B norm with Dissolve(2.0)

narrator "You arrive in your dorm. You bring out your phone to text someone, out of habit, when you suddenly see a new text."

"{color=#55b13c}???{/color}" "Hi~ya! The Dean of the school wants to talk to you! Don't leave him waiting, o~kay?"

red @confusedeyebrows frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

show ethan at rightside with dis

ethan @talkingmouth "Hey, man. Did you just get a weird text?"

red @closedbrow talking2mouth "Uh, yeah. You too? Who was it from?"

ethan @talkingmouth "Beats me, man."

pause 1.0

red @surprised "Oh, there's bubbles. Hold on, there's bubbles. They're saying something..."

pause 2.0

"{color=#55b13c}Bianca{/color}" "This is Bianca, by the way!~ Nate gave me your number! Hope you aren't too~oo mad. <3 <3"

$ BecomeContacted("Bianca")

red @confusedeyebrows talking2mouth "What? {i}Nate{/i} gave her my number?"

ethan @closedbrow frownmouth "Hm..."
ethan @talking2mouth "I don't remember ever giving him my number."

red @closedbrow talking2mouth "Yeah, come to think of it..."

show forest at sepia with dis
show flashback with dis

$ renpy.pause(1.0, hard=True)

show nate happy at sepia behind flashback with dis

nate @talkingmouth "Don't worry about it. Oh, but we should exchange contact deets, in case it gets loose, and we need you to wrangle it again."

hide nate
hide forest
hide flashback
with Dissolve(1.0)

red @talkingmouth "I gave him my number a while ago. Definitely didn't say that he could share my number with other people, though."

ethan @sadbrow happymouth "What, are you upset?"

red @happy "Nah. Would've appreciated a heads-up, though."

ethan @happy "Understandable." 
ethan @talkingmouth "Well... guess we should go."

red @closedbrow talking2mouth "Yeah, but where to?"

pause 1.0

red @talkingmouth "...She's not responding."

ethan @closedbrow talking2mouth "Maybe she went to bed already? 'Studying dreams'?"

red @happy "Maybe. The Dean's office has got to be somewhere in the academy building, right? Let's just head out. Maybe she'll text us on the way."

ethan @closedbrow talking2mouth "Hm."
ethan @sadbrow happymouth "You sure it's safe for us to go out?"

red @happy "What, you worried about people from the city?"

ethan @closedbrow talking2mouth "Nah, mostly just worried about the curfew. It's {i}really{/i} soon."

red @talkingmouth "Bianca says the Dean wants us. If the Dean can't get us out of curfew, no-one can."

ethan @sad "Yeah, but... what if Beatrice is... well, lying?"

red @surprised "Ethan! What? Bianca's a sweetheart. Why would she lie?"

ethan @closedbrow talking2mouth "I mean... she's pretty close to Chadwick, right? And Chadwick isn't exactly happy with you, if what Nigerundayo's been telling me is correct."

redmind @thinking "Oh, that's a difficult one to parse. Uh... Chadwick is Cheren, and Nigerundayo is Nate, I think?"

red @surprised "Huh. What {i}has{/i} Nate been telling you?"

ethan @sadbrow talkingmouth "Bad puns, mostly. But he {i}did{/i} say that Chadwick's becoming desperate to figure out why you're doing so well."
ethan @happy "Honestly, I kinda get the feeling!"

red @talkingmouth "Bianca's my friend. And friends don't lie to each other. Right, Ethan?"

ethan @sad "...Right."

red @happy "Cool. Let's go, then."

hide ethan with dis

$ PlaySound("door_close1.ogg")
$ PlaySound("fading_footsteps.ogg")

show calem at leftside
show hilbert
show brendan at rightside
with dis

pause 1.0

hilbert @talkingmouth "Have you two noticed anything strange about Ethan? Ever since the Battle Team tryouts?"

calem @surprised "Huh? What was that? Sorry, I'm just busy with these campaign documents."

brendan @talkingmouth "Ah, yeah, sorry, Hilbert. Didn't hear that, either. I was on the phone with May. What'd you say?"

pause 1.0

hilbert sad "You're all so unobservant."

show hilbert:
    ease 0.5 xpos 1.2

pause 0.4

$ PlaySound("door_close1.ogg")
$ PlaySound("fading_footsteps.ogg")

scene garden night with Dissolve(2.0)

red night @closedbrow talking2mouth "Hm... remember when those Lopunny and Buneary attacked us?"

show ethan at night with dis

if (lopunnyobj in playerparty):
    ethan @happy "Yeah! I've got the one I caught in my party right now."
elif (lopunnyobj in box):
    ethan @talkingmouth "Yeah. The one I caught's in the PC right now."
else:
    ethan @talkingmouth "Yeah."

ethan @closedbrow talking2mouth "It's weird that they came so far out of the forest. And so many of them, too. Lopunny normally live there, right?"

redmind @thinking "It reminds me of that Absol that ran out of the mountains... they have to be connected somehow, right?"

red @closedbrow talking2mouth "Maybe something moved into their territory."

ethan @talkingmouth "Beats me, dude. That'd make sense, but it still doesn't explain the hot cross bunny going all Mega on us."

red @confused "'Hot Cross Bunny'?"

ethan @talkingmouth "Yeah, you know, like the Springsday snack."

red @happy "Oh, so you're not saying that the Lopunny is..."

ethan @talkingmouth "Hah, no! No."

pause 1.0

ethan @happy "{size=30}Unless...?{/size}"

red @angrybrow talking2mouth "What?"

show ethan:
    ease 0.5 xpos 1.2

ethan @surprised "Nothing!"

pause 1.0

drayden @sadbrow "You there. Young men."

hide ethan

red @surprised "Huh?"

show drayden at night with Dissolve(1.0)

drayden @surprisedeyebrows "Are you [first_name] [last_name] and Ethan Gold?"

red @happy "Yes, Sir. That we are."

drayden @happybrow "It is well that you are; else I would send you scurrying back to your dorm, with an admonishment to observe the curfew."

drayden @angryeyebrows "But."

drayden "As you are, in fact, who I seek, I have other business with you."

drayden @happybrow "You may not know me, though you may know my work; I seek to diminish my direct interference in matters of academics." 
drayden @sadeyes "I am the column that holds aloft the stakeholders' gilded mezzanine and prevents them from altogether crushing this place of learning."

red @surprised "Uh... Sir, I'm a country boy from Kanto. I can't quite understand everything you're saying."

drayden @surprised "Oh. Sorry. I always put on airs to impress new students, but... let me speak plainly." 

$ BecomeNamed("Dean Drayden")

drayden @angryeyebrows "I am Drayden. The Dean of Academics of Kobukan Academy of Advanced Pokémon Arts & Sciences. And current acting President."

red @surprised "Oh!"

pause 1.0

ethan night @sad "Uh-oh..."

drayden @happy2eyebrows "Why do you quake?"

redmind @thinking "You mean besides the fact your thighs are thicker than my torso?"

red @talkingmouth "If I might go out on a limb here, I think the reason Ethan is concerned is because, well... if the Dean of the Academy wants to talk to us directly, we probably did something {i}pretty{/i} wrong."

pause 1.0

drayden @happy2eyebrows "Have you any recollection of doing so?"

pause 1.0

redmind @thinking "I hid in the women's bathroom on my first day here? That's probably the only 'rule' I've broken..."

ethan @closedbrow talking2mouth "Not really, Sir."

drayden @happy "Then it would seem you have nothing to fear. No, I come to meet and {i}thank{/i} you."

red @surprised "Huh? What did we do?"

drayden @happy "You have gained entrance into the school's Battle Team. As, I believe, has another one of your roommates, Hilbert von Schwarzdrachen."

red @surprised "Von Schwarzdrachen?"

ethan @happy "{i}That's{/i} a mouthful."

red @happy "It sounds like a prince's name! I thought Unova didn't have kings?"

drayden @angry "Indeed, we do not. The effort required to ensure that remains the case, even in the modern day, cannot be overstated."

drayden @happy2eyebrows "But I'm not here to teach of Unovan history, much as the topic might excite."

drayden @sad "I've come to express my thanks for the torch you will carry for the Battle Team--carry proudly and with honor, no doubt--but that alone would not drag me down from my office."

drayden @happy2eyebrows "I understand that, in this very garden, you two fought a herd of wild Lopunny and Buneary, headed by one that Mega-Evolved. Seemingly without a trainer."

red @surprised "Wha-- well, yes, Sir. We did. But how did you know? Who told you?"

ethan @surprised "Wait, [first_name], I get it! This guy's 'Daddy!'"

show drayden sad with dis

"{color=#583C68}Daddy{/color}" "\"Please do not call me that.\""

show drayden -sad with dis

red @happy "What he {i}meant{/i} was that we met your daughter. Iris. She must've been the one who told you, right?"

drayden @happy "She did. She told me that she had a good time. I would thank you for that. And for... 'protecting' her from the Lopunny attack."

red @happy "Hey, it's what we're here for."

pause 1.0

red @closedbrow talking2mouth "Actually, we're here to study, but that just felt right to say in the moment."

drayden @sad "I must ask you, young men, to scratch your brains for absolutely {i}anything{/i} you can think of that might shed some light onto why that Lopunny possessed the power of Mega Evolution."

if (lopunnyobj in playerparty or lopunnyobj in box):
    red @closedbrow talking2mouth "I mean... I caught it, Sir. If it would help, I could give it to Professor Oak to study for a while?"

ethan @closedbrow talking2mouth "Besides what your daughter's told you, I'm not sure that I can think of anything else."

drayden @sad "Hm..."

red @closedbrow talking2mouth "There was a meteor that landed outside of campus a while ago. But, right before that, there was an Absol that came down from the mountains. Almost like it was warning us about the meteor."

red @closedbrow talking2mouth "That Absol was outside of its habitat, and it was acting really crazy, too. Like the Lopunny."

drayden @sad "Hm. But that Absol was not Mega-Evolved, correct?"

red @talking2mouth "No, Sir."

if (absolobj in playerparty):
    red @talkingmouth "I have it with me, actually, Sir."

elif (absolobj in box):
    red @closedbrow talking2mouth "The Absol's in my PC box... well, Janine's, actually... in case you want to see it, Sir."

drayden @sad "Mm. Perhaps something to consider later."

drayden @happy2eyebrows "I've taken enough of your time for now. Please, be on your way back to your dorm."

drayden @happy "Wouldn't want security to misunderstand your benign intentions."

red @happy "Sure thing, Sir."

pause 1.0

ethan @talkingmouth "...Sir? I have a question."

drayden @surprisedeyebrows "Mm?"

ethan @sadbrow happymouth "Why did you meet us out here instead of... I dunno... calling us to your office?"

drayden @happy "Hm! The stars, young man. It's important, when it seems like life is rushing by your ears, to plant your feet and look up at the stars."
drayden sad "How fleeting are all human passions in comparison to the massive continuity of the astral bodies. No man may think himself grand when scaled to the universe."

pause 1.0

red @sadbrow happymouth "Are you alright, Sir?"

drayden -sad @surprisedeyebrows "Oh?"
drayden @happy "Of course, young man. How could I be anything but when I see young people such as yourself grabbing the baton of the future?" 
drayden @sad "I'm not despondent, young man. I'm in awe. Overwhelmed, and in awe of it all. In awe of the youth, of Pokémon, of the miracle that we get to live."

pause 1.0

drayden @sad "...There was a time when I believed that, as I was a large man, a powerful man, a man who could handle any challenge thrown my way, that I knew what power was. That I knew what my place and path in life was."
drayden @happy "And then I had a daughter. And there is nothing more humbling than that."

pause 1.0

drayden @sad "Though... perhaps my {i}specific{/i} daughter is slightly more humbling than others."
drayden @happy "Hohoho."

red @confused "I gotta say, Sir, I don't see the family resemblance."

drayden @sad "I was not blessed with the ability to be her father, no. But she is, in every way that matters, my daughter."

drayden @happy "Much as she is my chosen family, I hope I can prove myself as a reliable chosen mentor over the next year."

redmind @sad "...He seems like a nice guy, but... how would he react if he knew that I wasn't able to pay my tuition here?"

red @talkingmouth "Sir, I have a question about one of my Battle Teammates."

drayden @surprisedeyebrows "Mm?"

red @closedbrow talking2mouth "Um... Sonia Magnolia. It seems like Mr. Lance talked to you and you worked out some sort of deal. Since she was a student last year, she isn't available for most of the tuition waivers, right?"

drayden @sad "Mm."

red @happy "Well, uh... is there some special payment plan that she has access to? Some sort of scholarship I don't know about?"

drayden @sad "Nothing that you two, as Battle Team members, don't have access to."

ethan @closedbrow talking2mouth "What do you mean, Sir?"

drayden @surprised "Surely you must know?"
drayden @angry angryshadow "What's that Student Council doing during orientation if not covering this sort of information? Bah. They drive me to distraction!"

pause 1.0

drayden @happy "Kobukan Academy offers many scholarships, both before, and {i}during{/i}, the school year. Your tuition can be reduced for excelling in many different fields--sports, academics, battling."

red @sadbrow happymouth "That's... very good to know. I was just kinda surprised that you could bend the rules like that to let Sonia in."

drayden @sad "...Rules exist to protect. If a rule is harming someone, then the rule must be changed. And if the rule cannot be changed quickly enough to help the person it would otherwise harm..."

pause 1.0

drayden @angry angryshadow "Well, I'm the dean! And I'd like to talk with whoever decided that!"

drayden @happy "No, no, exceptions can always be made for those with a story. She proved herself the first time she got into this school, and I counted it as a deep, personal, shame when she left last year."

drayden @sad "Though perhaps that isn't my story to tell."

pause 1.0

drayden @sad "Run along now, students. As I said. It's getting late."

red @talkingmouth "Alright. Goodnight, Sir."

drayden happy "Mmm."

scene blank2 with Dissolve(1.0)
scene dorm_B norm with Dissolve(1.0)

show calem at leftside
show brendan at rightside
with dis

red @happy "Hey, guys! We're back! And guess what? We met the Dean!"

calem @surprised "Will wonders never cease?"

brendan @talking2mouth "Did you guys run into Hilbert as well? He went out after you guys."

show ethan with dis

ethan @surprised "Huh? No, we didn't see him at all. It's past curfew now, isn't it?"

calem @closedbrow talking2mouth "Hm... concerning. One can only imagine what he's getting himself into now."

call clearscreens from _call_clearscreens_71
scene blank2 with Dissolve(3.0)

scene garden night with dis

pause 1.0

show nate frownmouth at night with dis

nate @talking2mouth "Yes, Sir.{w=0.5} I understand.{w=0.5} Two, no more.{w=0.5} I believe the forest fire was unrelated, MC² didn't know anything.{w=0.5} Two more weeks?{w=0.5} Fine, I understand.{w=1.0} Goodnight."

pause 1.0

nate @closedbrow angrymouth sweat "Damn. He's so up my ass I'm almost {i}enjoying{/i} it."

nate @closedbrow talking2mouth "Things are getting weirder and weirder. And it's all centered around that meteor. If {i}my{/i} team wasn't the first there... who was?"

show hilbert at night, leftside:
    xzoom -1
with dis

pause 1.0

show nate surprisedbrow frownmouth with dis:
    ease 0.5 xzoom -1 xpos 0.75 

hilbert @talkingmouth "You. What are you doing out so late?"

nate -surprisedbrow -frownmouth -surprised @happy "Hey, H! Just enjoying the night air. What about you?"

hilbert @sadbrow talkingmouth "Following some... acquaintances. They just--"

show hilbert surprisedbrow frownmouth with dis

stop music fadeout 1.5

pause 1.5

hilbert @talkingmouth "{size=30}...You?{/size}"

nate @happy "No, I usually go by 'N'. Can I help you?"

queue music "audio/music/tension_start.ogg" noloop
queue music "audio/music/tension_loop.ogg"

show garden night with vpunch
show nate surprisedbrow frownmouth with dis

hilbert angry "YOU."

nate @talkingmouth "Woah, buddy, what?"

hilbert @talkingmouth "I've been watching you for weeks now. Every single Steel-type class. I {i}knew{/i} I had seen you before. I might have forgotten, like so much else in my life, but my subconscious knew."

pause 1.0

hilbert @sadbrow talkingmouth "I thought I'd dreamed it, to be honest. No way a... a {i}child{/i} could be responsible for what happened."

hilbert @talkingmouth "But I recognize that hair. That undersuit. Those glassy, dark eyes of yours."

nate @happy "H-hey, man, getting a bit personal there..."

show hilbert at night:
    xpos 0.25
    ease 10.0 xpos 0.5

hilbert @talkingmouth "You'll tell me what those eyes saw. {i}Now.{/i}"

nate @closedbrow talking2mouth "I... what... {i}what{/i} did I see?"

hilbert @talkingmouth "{cps=30}My parents.{w=0.5} You were the last one to see my parents.{w=0.5}{/cps}{nw}" 

show blank2

extend @talkingmouth "{w=0.5} {cps=15}{i}Alive.{/i}{/cps}"

stop music fadeout 3.0

pause 3.0

jump day010426