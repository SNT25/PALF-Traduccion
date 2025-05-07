label lunch010513:

show leaf uniform with dis

leaf @talkingmouth "Heya."

red uniform @talkingmouth "Hey. What's up?"

leaf @talkingmouth "The sky, last time I checked."

red @talkingmouth "It {i}does{/i} tend to stay up. I think it's got a bunch of balloons keeping it up there."

leaf @surprised "Balloons? Are you crazy? You can't hold up an entire sky with balloons. Besides, they'd go into space and pop."

red @confused "Oh, yeah? What is it, then?"

leaf @talking2mouth "The sky's obviously balanced on the top of Blue's ego. A solid, invisible, unbreakable force that's the size of the entire world."

red @closedbrow talking2mouth "Probably a good thing that he never seems to get discouraged, then. We might all be crushed."

leaf @happy "Yep, he's a hero."

pause 1.0

red @closedbrow talkingmouth "Man, you're crazy."

if (HasEvent("Leaf", "AcceptedConfession")):
    leaf @talkingmouth "You know you love me."

    red @winkeyes talking2mouth "Hey, save that kind of talk for after our date. We already live in the same dorm. People might talk."

else:
    leaf @talkingmouth "You know you tolerate me."

    red @closedbrow happymouth "Can't think of why I'd be in the same dorm as you if I didn't."

leaf @closedbrow frownmouth "Hmm..."

red @talkingmouth "What?"

leaf @talking2mouth "You know, I actually don't know {i}why{/i} we're in the same dorm."

red @upeyes talking2mouth "I assume because Falkner thought it would be funny to put all of us together."

leaf @closedbrow talking2mouth "...Maybe."

pause 1.0

red @talkingmouth "Anyway, what's up?"

leaf @talking2mouth "Well... I'm thinking of switching classes."

$ sidemonnum = pokedexlookupname("Jigglypuff", DexMacros.Id)

$ PlaySound("Pokemon/Ball sound.ogg")
$ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))

show leaf:
    xpos 0.5
    ease 0.5 xpos 0.33

show sideportraitfull at pokeball:
    xpos 0.66 ypos 0.8
    pause 1.0
    block:
        ease 0.5 xpos 0.68
        ease 0.5 xpos 0.66
        ease 0.5 xpos 0.64
        ease 0.5 xpos 0.66
        repeat
    block:
        ease 0.2 ypos 0.7
        ease 0.8 ypos 0.8
        repeat

red @confusedeyebrows talkingmouth "Really?"

leaf @closedbrow talkingmouth "Yeah, I think I can do it. Maybe not permanently, and I don't think I want to do the crazy thing you and Ethan are doing, but I'm seriously considering it."

red @talkingmouth "Okay. Which classes?"

$ AddEvent("Leaf", "ClassSwap")

leaf @talkingmouth "I'm thinking of ditching Dragon for Normal."
leaf @closedbrow talking2mouth "I already told Blue about my plan, and he said, quote, 'thank God, maybe now Instructor Clair won't have to stop the lesson every five seconds to yell at you!'"
leaf @angrybrow talking2mouth "Which is totally inaccurate and unfair, by the way. She yells at {i}everyone.{/i}"

pause 1.0

leaf @closedbrow talkingmouth "Well, not him, I guess."

if (HasEvent("Instructor Clair", 2.1)):
    leaf @happy "But you know how she is."

    red @closedbrow sweat talking2mouth "Yeah, I do. I {i}sure{/i} do."

    red @talkingmouth "Well, I'll miss you in class, but if you want to swap, that's up to you."

else:
    red @talkingmouth "Well, if you want to swap, that's up to you."

red @talkingmouth "I guess you want to pay a bit more attention to your new Jigglypuff?"

$ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))

leaf @sadbrow talkingmouth "Pretty much. She's a pretty easy train, all things considered, but I don't know a whole lot about her species. Hopefully Instructor Lenora can teach me more about her."

red @talkingmouth "Any particular reason you didn't go for Fairy? That's one of Jigglypuff's types, too."

leaf @talkingmouth "Just have more experience with Normal-type Pokémon."

red @talkingmouth "Hm... Drampa, Helioptile... yeah, I can see it."

pause 1.0

show leaf embarrassed with dis

red @surprised "Wait. What about... what about your Dratini?"

pause 1.0

red @playfulbrow talking2mouth "...I do {i}not{/i} like that look."

leaf @sadbrow talking2mouth "Okay, now, {i}please{/i} don't be mad, but..."

pause 1.0

red @surprised "Oh my god, you're letting Blue train it."

leaf @closedbrow talking2mouth "Yes."

red @angrybrow talking2mouth "Leaf!"

$ leafdratiniobj = GetTrainerTeam("Leaf", "Dratini")
$ pronoun = "he" if leafdratiniobj.Gender == Genders.Male else "she"
$ pronoun2 = "him" if leafdratiniobj.Gender == Genders.Male else "her"

leaf @sadbrow talking2mouth "Look, it wasn't {i}my{/i} idea! Dratini {i}wanted{/i} it! Ever since Blue borrowed Dratini last Wednesday, [pronoun]'s been trying to sneak into Blue's bag!"
leaf @sadbrow talkingmouth "Honestly, I was kinda offended at first, but... I mean, just one afternoon with Blue made [pronoun2] {i}way{/i} stronger, so I can kinda understand where [pronoun]'s coming from."
leaf @closedbrow talking2mouth "Anyway, [pronoun]'s still {i}my{/i} Dratini, and always will be, while we're all still breathing."

red @closedbrow talkingmouth "Mannnn... does that mean the next time I fight Blue, I'm going to have to fight your Dratini, too?"

leaf -embarrassed @sadbrow talkingmouth "Maybe."

$ renpy.music.play("Audio/bigcrowdloop.ogg", channel='crowd', loop=True, fadein=10.0)

red @upeyes talking2mouth "Bah."
red @talkingmouth "Well, thanks for the heads-up, at least."

stop music fadeout 1.0

pause 1.0

$ PlaySound("asteroidwoosh.ogg")

$ renpy.music.queue("Audio/Music/brandnewworld.ogg", channel='music', loop=True, fadein=1.5, tight=None)

pause 3.0

red @confused "What's that sound?"

Character("Gossiping Dude") "\"Did I just hear something fly over the school?\""

Character("Chatty Chick") "\"Yeah, I thought I heard something's wings, like, flapping...\""

red @talkingmouth "It sounds like it's coming from the garden."

leaf @talkingmouth "Are we checking it out?"

red @happy "I mean, obviously."

stop music fadeout 1.0 channel "crowd"

call clearscreens() from _call_clearscreens_159
scene blank2 with splitfade

pause 1.0

scene garden:
    zoom 0.625
show clouds behind garden
show screen currentdate
with splitfade

narrator "You emerge out into the garden, and blink up at the sky. Your eyes are still adjusting to the light, so it's hard to make out, but...?"

show raihan:
    ypos 0.0
    ease 0.2 ypos 2.0

show garden with vpunch

show blank2 with transeyefast

red uniform @surprised "Gah!"

show raihanchasesclout behind blank2

hide blank2 with transeye2slow

narrator "Kneeling above you is a strange man dressed in a familiar outfit. He lets out a soft breath, and licks his lips as he looks you over."

pause 1.0

narrator "Something about his hungry gaze sends chills down your spine."

raihan @talkingmouth "Well, well, well... look who I just dropped in on. The Kobukan Pikachu wielder. Slayer of the Jobbird."

red @surprised "J-Jobbird? Wait, you're-- you're from the internet!"

pause 1.0

raihan @closedbrow talking2mouth "Heh, heh, heh. That's not far off, actually."

pause 1.0

raihan @happy "Want me to get off?"

red @lightblush sad2eyes talking2mouth "That's a very tricky question to answer, given my current position."

raihan @angrybrow happymouth "Sharp, too. Guess your victory wasn't a fluke."

$ BecomeNamed("Raihan")

if (HasEvent("Leaf", "AcceptedConfession")):
    leaf uniform @surprisedbrow talkingmouth "U-u-u-um...? Raihan? Big fan. I follow your RotoPhoto account. What are you doing here, kneeling on my date?"

else:
    leaf uniform @surprisedbrow talkingmouth "U-u-u-um...? Raihan? Big fan. I follow your RotoPhoto account. What are you doing here, kneeling on my roommate?"

raihan @happy "Not much, besides that."

if (GetRelationshipRank("Nessa") > 0):
    red @surprised "Raihan?! {i}You're{/i} Raihan?"

    raihan @talking2mouth "What, were you expecting someone taller?"

    show raihan surprisedbrow frownmouth with dis

    red @happy "No, I just... Nessa told me about you!"

    $ ValueChange("Raihan", 1, 0.5)

    show raihan -surprisedbrow -frownmouth with dis

    red @talkingmouth "You're the strongest Gym Leader of the Galar Region. You've fought Leon more than anyone else. And you're strong enough to be a Champion in any other region!"
    
    leaf @talking2mouth "Plus, he's got this really popular RotoPhoto account where he posts pictures and videos of himself in battles, and during meals, and... {w=0.5}uh..."
    leaf @blush talkingmouth "{size=30}Pool parties.{/size}"
    leaf @happy "His fans are called the Fang Gang!"

    raihan @talking2mouth "Hey, you {i}are{/i} a fan."

raihan @happybrow talking2mouth "Oh, this is a good one. First steps in Kobukan? First friends met? Gotta memorialize this one. Smile for the selfie, you two."

leaf @surprised "Friends?!"

narrator "Raihan pulls out a stylish-looking smartphone and flips it around, grinning at it."

menu:
    ">Smile for the camera":
        $ AddEvent("Raihan", "SelfieSmile")
        scene blank

    ">Throw Raihan off":
        $ AddEvent("Raihan", "ThrowOff")
        scene blank2 with splitfadefaster

$ PlaySound("photo.ogg")

pause 2.0

scene garden:
    zoom 0.625
show clouds behind garden
show raihan phone:
    xpos 0.66
show leaf uniform surprisedbrow frownmouth:
    xpos 0.33
with splitfade

if (HasEvent("Raihan", "SelfieSmile")):
    $ ValueChange("Raihan", 1, 0.66)

    raihan @happy "Nice. Might not even post this one. Feels more important than a photographer like me could do justice to."

else:
    raihan @sad "Tch, can't use this one, now. I look blurry."
    raihan @talkingmouth closedbrow "Don't want my followers thinking I'm blurry, now, do I?"

if (GetRelationshipRank("Nessa") == 0):
    red uniform @talkingmouth "Hey... Leaf? You called this guy Raihan? How do you know him?"

    leaf @surprised "You don't-- oh, no, of course you don't."
    leaf @talkingmouth "This is {i}Raihan.{/i} He's the strongest Gym Leader of the Galar Region! He's fought Leon more than anyone else! He's strong enough to be a Champion in any other region!"
    leaf @talking2mouth "Plus, he's got this really popular RotoPhoto account where he posts pictures and videos of himself in battles, and during meals, and... {w=0.5}uh..."
    leaf @blush talkingmouth "{size=30}Pool parties.{/size}"
    leaf @happy "His fans are called the Fang Gang!"

    raihan @talking2mouth "Hey, you {i}are{/i} a fan."

    leaf @sadbrow talking2mouth "But... why are you {i}here{/i}, in Kobukan?"

    raihan @sadbrow talkingmouth ".{w=0.5}.{w=0.5}.{w=0.5}Hey, I'm a bit busy right now. Don't really have time to answer all these questions."
   
else:
    red uniform @talkingmouth "Wait, wait, I've got a question. ...Why are you {i}here{/i}, in Kobukan?"

    raihan @sadbrow talkingmouth ".{w=0.5}.{w=0.5}.{w=0.5}Hey, I feel bad blowing off a friend of Ness, but... Don't really have time to answer all these questions."

raihan -phone @talkingmouth "Influencer shit. You know how it is. Always gotta chase that clout around the corner."
raihan @happy "Know where I can talk to the guy in charge of this place?"

hide leaf with dis

play music "audio/music/DragonDenStart_B.ogg"

show lance:
    xpos -0.1
    ease 1.0 xpos 0.25

show raihan surprisedbrow frownmouth with dis:
    xpos 0.66
    ease 0.5 xpos 0.75

show drayden angry with vpunch

drayden "That would be {i}me{/i}, young man!"

pause 2.0

play music "<from 60>audio/music/brandnewworld.ogg"

raihan -surprisedbrow -frownmouth -surprised @talkingmouth "Oh. {w=0.5}Hey."

drayden "May I ask what you think you're doing, flying into my school in the middle of the day? No appointment, no forewarning, no introduction?"

raihan @sadclosedbrow sadmouth "In my defense, I was just asking who was in charge. Wanted to talk with you."

drayden "And {i}who{/i} are you, to ask this of me, Drayden, in the middle of a workday?"

raihan @surprisedbrow sadmouth "{size=30}Drayden, huh?{/size}"
raihan @closedbrow talking2mouth "I guess you aren't a fan, then. Heh. My name's Raihan, Eighth Gym Leader of Galar. Strongest member of the Galarian league aside from Leon, you know?"

pause 1.0

drayden @closedbrow "The name is familiar."

pause 1.0

drayden @angry "So, Raihan, eighth Gym Leader of Galar, and strongest member of the Galarian league aside from Leon, may I ask you for the courtesy of an explanation as to what you are doing here?"

raihan @talking2mouth "Got a bunch of reasons. Heard Sonia finally stuck her head up out of the dunes, and I'd like to reconnect with my old circle."

narrator "Raihan looks pointedly in your direction."

raihan @happybrow talking2mouth "Besides, I needed to talk to {i}this{/i} guy. You {i}did{/i} see what his Pikachu did, right? That might be just the kind of thing that gets me over Leon."

pause 1.0

drayden @closedbrow "And you thought that doing this {i}now{/i}, in the middle of a school day, would be the best way to achieve these goals?"

show raihan surprisedbrow frownmouth with dis

if (not rescuedwill):
    if (rescuedsabrina + rescuedtia == 0):
        drayden @sadbrow "Our school was very recently attacked, and multiple students and faculty are still missing."

    elif (rescuedsabrina + rescuedtia == 1):
        drayden @sadbrow "Our school was very recently attacked, and both a student and faculty member are still missing."

    else:
        drayden @sadbrow "Our school was very recently attacked, and a member of the faculty is still missing."

else:
    if (rescuedsabrina + rescuedtia == 0):
        drayden @sadbrow "Our school was very recently attacked, and multiple students are still missing."

    elif (rescuedsabrina + rescuedtia == 1):
        drayden @sadbrow "Our school was very recently attacked, and a student is still missing."

    else:
        drayden @sadbrow "Our school was very recently attacked, and multiple students and faculty went missing, though they have, thankfully, been recovered by now."

drayden @angry "Perhaps you can understand why I would be a bit {i}twitchy{/i}, Raihan!"

show raihan -sadbrow with dis

raihan @sadmouth "Hey, I'm sorry, mate. I didn't know that."

pause 1.0

show raihan surprisedbrow frownmouth with dis

drayden -angry @unamusedeyebrows "Lance, it appears your skill is not needed here. You may take your leave."

show lance surprisedbrow with dis

raihan -surprisedbrow -frownmouth @surprisedbrow talkingmouth "Wait. Lance? That's you?"

lance @sad2eyes talking2mouth "I am he."

raihan @talking2mouth "Bloody hell! {i}You're{/i} Lance! I knew I'd seen you before! You're my hero, mate!"

pause 1.0

lance -surprisedbrow @sad2eyes talking2mouth "There must be some sort of mistake."

raihan @talking2mouth "No mistake, Lance. You've got the world record for the most league challenge attempts, nah? Well, I'm coming for your record!"

lance @talking2mouth "My failures are nothing to emulate."

raihan @happy "Nah, nah, it's not that! You kept getting back up! Over and over! And then you {i}won{/i}, twice!"
raihan @talkingmouth "You're my idol. I even get my gym trainers to dress like you!"

pause 1.0

show raihan surprisedbrow frownmouth with dis

lance @angrybrow shadow talking2mouth "About that."
lance @sad2eyes talking2mouth "I wear the honorable dress of a Draconic Knight of the Blackthorn Dragon Clan."

show raihan sadbrow with dis

lance @closedbrow shadow angrymouth "To see the patterns and emblems of my ancient ancestors emblazoned on this... {i}sportswear{/i}{w=0.5} is no trifling insult."

drayden @surprisedeyebrows "Lance, I think you may be missing the point of the boy's sentiment."

lance @sadeyes talking2mouth "If he sees anything within me worthy of emulation, then it is {i}he{/i} who misses the point. I take my leave."

hide lance with dis

pause 1.0

raihan @sadmouth "...Well, that went to pot."

show raihan:
    ease 0.5 xpos 0.66

show drayden:
    ease 0.5 xpos 0.33

drayden @closedbrow "Apologies for Lance's irascibility."
drayden @angrybrow "However, his temper does not remove the fact that you ought not to be here. Flying over the gates, as you did, is absolutely not permitted."

raihan @sadmouth "I can fly back over, then walk through the front, if you want, but it sounds like a bit of a bother."

drayden "I would request that you fly back over, and {i}stay{/i} over. If you wish to talk to certain students, you can make plans to meet up with them in Inspira. {i}Off{/i} campus grounds."

raihan -sadbrow -frownmouth @sadmouth "Ah, c'mon, mate, don't be like that."
raihan @happy "Tell you what. I've got a bit of a following. I'll put in a good word for you if you let me hang around for a bit, eh?"

drayden @surprisedeyebrows "This is a historic centuries-old school. Our programs are world-famous, and more of our alumni are champions than Blueberry and Naranjuva Academies put together."
drayden @closedbrow "May I ask who you could possibly 'put in a good word for us' for that is not already aware of our accomplishments?"

show raihan closedbrow with dis

pause 2.0

raihan @talkingmouth "Gimme a moment."

pause 2.0

raihan -closedbrow @surprised "...Isn't Chairman Rose a board member here?"

drayden -surprisedbrow -surprised @sad "Well... yes. I suppose my reputation with the board {i}could{/i} do with some aggrandizement, in light of recent events."

pause 1.0

raihan @happy "There we go, mate. Knew we could do something for each other."

drayden @angrybrow "However. This agreement is conditional."

raihan @talkingmouth "Oh? Yeah, go on."

drayden "Chairman Rose has been hinting that he is considering launching an inquiry into how this school has been run."
drayden @closedbrow "I would have you attend classes. Join clubs. I would ask that you treat this experience as though you were just another student."
drayden "And then I would ask that you report back to the esteemed Chairman Rose, honestly, about what you have experienced."

raihan @happy "Seriously, I can be in and out. It's no problem. C'mon, I'm the great Raihan! I don't need to go to school. "

show raihan surprisedbrow frownmouth with dis

drayden @surprisedeyebrows "...Correct me if I'm wrong, but did you not attempt to win the last Galarian Champion's cup with a team that utilized four different types of weather?"

pause 2.0

raihan -surprisedbrow -frownmouth -surprised @sad "Mate, I was trying something different. Lose to Leon twelve times, and anyone'll start thinking outside of the box."

drayden "I understand that Galarians do not typically undertake formal education in Pokémon training, but I must insist it would benefit you."
drayden @happy "There's no doubt you are a powerful trainer. But even the child champion of Unova attends her middle school during the day."
drayden "A thorough education exercises soft skills that you may have no other opportunity to develop."
drayden @surprisedeyebrows sadeyes "Such as humility, 'great Raihan.'" 

raihan @closedbrow sadmouth "Alright, alright, I get it. You don't need to go on."
raihan @talkingmouth "Look, I was planning on making this a get-in, get-out kind of thing. I'm not going to need to pay a full year's tuition, am I?"

drayden "You will only need to pay tuition for as long as you are here."

raihan @talkingmouth "Great."

pause 1.0

raihan @sadbrow talkingmouth "How much is that per day? Finances've been a little bit tight, ever since I bought that new muscle car. It was a risky purchase, but the clickthroughs on that post were so worth it."

drayden "Your first tuition payment will be due on the fourth of October. I may suggest you not buy any new cars until that time, but with a Gym Leader's salary, I see no reason you should struggle to pay."

pause 1.0

$ PlaySound("idea.ogg")

drayden @happy "Of course, perhaps I am getting too ahead of myself. You still need to pass the entrance exam, after all!"

raihan @surprised "Hold on. I didn't know there was any kind of entrance exam."

drayden @closedbrow "Well, of course there is. We wouldn't admit a student to this academy without proof positive they will not waste our instructors' time."

raihan @surprisedbrow talkingmouth "Mate, I'm the eighth Gym Leader of--"

drayden "Yes, yes, I know. Eighth Gym Leader of Galar. You {i}did{/i} mention."

drayden @happy "In any case, this should be a very simple exam to pass for someone of your pedigree. Just defeat Mr. [last_name] here."

red uniform @surprised "What?!"

leaf uniform @surprised "What again?!"

raihan @surprised "...You serious, mate?"

drayden @happy "As the grave, Mr. Raihan."

raihan frownmouth @sad "But... this guy's just a kid, you know?"

drayden @closedbrow "I do not expect that you are any more than a couple years older than him, no?"

raihan @sad "You know what I'm saying."

menu:
    "Don't dismiss me.":
        raihan @surprised "Huh? Mate, it's not that, I totally respect where you are, it's just... uh..." 

        $ ValueChange("Raihan", 1, 0.66)

        raihan @closedbrow talking2mouth "Ah, you got me on the defensive! Nice blow, nice."

    ">Stay silent":
        pass

raihan @talkingmouth "Hey, [last_name]. I saw your battle with Berlitz. And it was some serious shit you pulled off. Impressive. But the raw numbers aren't there."
raihan @sad "Drayden, I'm not a bully. I'm not going to go all-out against a student."

drayden @closedbrow "One might point out that this student has had more battle education than you, but I concede your point. This was a test, anyway."

raihan @happy "Ah, so you {i}wanted{/i} me to turn down the battle? Sneaky. Did I pass?"

drayden @happy "Oh, no, you {i}are{/i} still going to battle Mr. [last_name]. But perhaps now, in the middle of lunch, is not the proper time for that."
drayden "You have until classes' cessation to prepare a team that you think will allow you to face Mr. [last_name] on an equal footing."
drayden @closedbrow "I may suggest heading to the fields--I've been told the Cyclizar population there is strong, and plentiful."

raihan @closedbrow talking2mouth "Cyclizar, huh? Okay... that's only four hours, but I think I can manage this."

pause 1.0

drayden "Then, after you finish your evening classes, will you join us in the Battle Hall, Mr. [last_name]? I will gladly referee your battle myself."

red @happy "Sure. Can't miss the opportunity to battle an actual Gym Leader, after all."

drayden @closedbrow "One more thing, Mr. Raihan. It is true that [first_name] is a much-less experienced battler than you, but..."
drayden @angryshadow angrybrow "Do {i}not{/i} do him the discourtesy of bringing a team that cannot pull their own weight."

raihan @closedbrow talking2mouth "Wouldn't dream of it, mate. The Great Raihan always goes 110%%, no matter what."

redmind @confusedeyebrows frownmouth "He... literally {i}just{/i} said that he wasn't going to fight me with his real team."

drayden @happy "Excellent. Now, I imagine Lance should be back any moment now."

raihan @surprised "Huh? I thought he just buggered off because he didn't fancy my outfit."

drayden @closedbrow "Yes, well, Lance is never one to make clear his intentions."

hide drayden with dis

pause 1.0

show lance:
    xpos -0.2
    ease 0.5 xpos 0.23

show sonia uniform surprised:
    xpos -0.3 xzoom -1
    ease 0.5 xpos 0.13

show nessa uniform surprised:
    xpos -0.1 xzoom -1
    ease 0.5 xpos 0.33

pause 2.0

nessa @surprisedbrow talkingmouth "...Rai?"

raihan @happy "Hey, Ness!"

nessa -surprisedbrow -frownmouth -surprised @talkingmouth "...It's good to see you again."

sonia -surprisedbrow -frownmouth -surprised @talking2mouth "Rai, why didn't you tell us you were coming?"

raihan @happy "Ness only just told me that you were here, Sunny. I came as soon as I heard, of course."
raihan @closedbrow talking2mouth "Besides, I was hoping to surprise you."

sonia @happy "Well, consider me proper surprised, you cad! What are you doing here?"

raihan @talkingmouth "Didn't you know? I'm a student. Well, I will be after I defeat [last_name], here."

show lance surprisedbrow with dis

nessa @talkingmouth "You want to fight [first_name]? Using your Gym Leader team?"

raihan @happy "Nah, I'm going to go out and catch some others."

if (GetRelationshipRank("Nessa") > 0):
    nessa @closedbrow talkingmouth "Oh. I wouldn't be so sure that you can beat him, then."

    raihan @sad "There's Nessa, with that icy-cold splash of reality, as always..."

lance @talking2mouth "Pardon me. What is this? You need to... {i}defeat{/i} Mr. [last_name] in order to become a student?"

raihan @closedbrow talkingmouth "Yeah, it's kinda a pain, but whatever, I wanted to battle this guy anyway."

show lance shadow angrybrow frownmouth with dis

narrator "Lance's eyes drill into yours as he stares, unblinking."

redmind @confusedeyebrows frownmouth "Come to think of it, this {i}is{/i} the first time since Friday we've been face-to-face, isn't it...?"
redmind @happy "Man, I can't begin to imagine how furious he is."

lance @sad2eyes talking2mouth "Utterly ridiculous."

hide lance with dis

sonia @surprised "Oh! Advisor Lance, thanks for... um... {size=30}getting us...{/size}"

pause 1.0

nessa @talkingmouth "Think he's gone, Sunny."

show raihan:
    xpos 0.66
    ease 0.5 xpos 0.75

show nessa:
    xpos 0.33
    ease 0.5 xpos 0.5

show sonia:
    xpos 0.13
    ease 0.4 xpos 0.25

raihan @happy "It's really great to see you two again. What've you been up to? And, Sunny, where the bloody hell did you get off to?"

sonia @sadbrow talking2mouth "Oh. Well... that's a bit of a tricky question, honestly. But, er, the short of it is... I was still here."

raihan @sadbrow talking2mouth "You cut me, when you left, you know. Thought I'd done something wrong. Thought we all had."

nessa @happy "Oh, Rai, you {i}definitely{/i} did something wrong, but it didn't have anything to do with Sunny this time."

raihan @happy "Man, you're just hating 'cause I'm prettier than you."

nessa @talkingmouth "I think you'll find that's the only reason I {i}tolerate{/i} you."

raihan @happy "Hah! But, no, really, what's up? You called me out here for a reason, right?"
raihan @surprised "Oh, wait, should we do this in private?"

if (GetRelationship("Nessa") == 0 and not rescuedsabrina):
    narrator "Nessa looks over at you and Leaf. She seems troubled."

    sonia @sadbrow talkingmouth "Sorry, teammates. Would you mind giving us Galarians a bit of space?"
    sonia @happy "Just got some private matters to talk about, you know."

    leaf @sarcastic "Aw, {i}right{/i} as it was getting fun, too."

    red @happy "Not a problem. Talk to you later."

else:
    $ AddEvent("Raihan", "KnowsWhyHere")
    nessa @talkingmouth "Nah, [first_name]'s already in this."
    nessa @talkingmouth "I called you out because I thought we needed your help rescuing a missing student."

    raihan @surprised "Huh?!"

    if (rescuedsabrina):
        nessa @talkingmouth "But... we already rescued her."

        raihan @closedbrow sadmouth "Cripes. Here I was thinking you were in mortal danger or something, but you already solved it?"

        nessa @talkingmouth "[first_name] works fast. I didn't expect that."

        raihan @happy "Well, I can't complain that the hard work's already been done."

        $ ValueChange("Raihan", 3, 0.75)

        raihan @talking2mouth "Actually... I'm looking forward to our battle even more, now, [last_name]."

    else:
        nessa @talkingmouth "She's lost in the woods. Has been, for a few days. There's a bigger story, but the long of it is that the forest is full of Grass-types, and I'm basically dead weight in there."
        nessa @talkingmouth "I know you love to brag about how 'well hard' you are. Thought you might be able to put that stone head of yours to use and help us."

        raihan @closedbrow talking2mouth "Hm. Yeah, I saw the woods when I was flying over. Didn't look like there was anything too challenging in there, but I see why you'd have trouble, Ness."

        sonia @talking2mouth "Nessa's dual proficiencies of Rock and Water leave her very vulnerable to Grass-types."

        raihan @talking2mouth "Alright. So when do we start this thing?"

        sonia @talking2mouth "Tonight."
        sonia @surprisedbrow happymouth "Assuming you can even beat [first_name], of course. He's not only the wielder of the Liberation-Form Pikachu, he's also a member of the Kobukan Battle Team."

        raihan @surprised "On god?"
        raihan @happy "Well, I guess I'm looking forward to our battle even more, now, [last_name]."

    raihan @angrybrow talkingmouth "Don't leave me hungry. The Great Raihan's got quite an appetite."

    nessa @closedbrow talkingmouth "{size=30}Matched only by his ego...{/size}"

    sonia @happy "C'mon. Let's show you around the place for a bit before you become an {i}official{/i} student."
    sonia @sadbrow happymouth "And... maybe you could tell me how you're paying for it...?"

call clearscreens() from _call_clearscreens_160
scene blank2 with splitfade

stop music fadeout 1.5

$ renpy.music.play("Audio/bigcrowdloop.ogg", channel='crowd', loop=True, fadein=0.5)

queue music "Audio/Music/Route 1 Anime.ogg"

pause 1.0

narrator "You return to the cafeteria room, somewhat bewildered by the sudden arrival of this strange new character."

scene cafe 
show screen currentdate
with splitfade

pause 1.0

jump PickTable