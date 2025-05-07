label lunch010518:

show leaf uniform with dis

leaf @talking2mouth "Heya, roomie."

red uniform @talkingmouth "'Sup."

leaf @talking2mouth "I've got a plan."

red @sadbrow talkingmouth "Oh, God. Can't we just have a nice, relaxing, laid-back week for once?"

leaf @flirtbrow talkingmouth "Be honest. Would you want one?"

show leaf surprisedbrow frownmouth with dis

red @talking2mouth "Yes, absolutely, 100%%, without question, and, furthermore, indeed."

pause 0.5

leaf -surprisedbrow -frownmouth @closedbrow talkingmouth "You seem conflicted."

red @sweat closedbrow talking2mouth "What's the plan?"

if (HasEvent("Dawn", "CyclizarHunt")):
    leaf @talking2mouth "Well, yesterday, when you, Dawn, and I were in the fields hunting Cyclizar, she let slip a certain key piece of information."

else:
    leaf @talking2mouth "Well, yesterday, when Dawn and I were in the fields hunting Cyclizar, she let slip a certain key piece of information."

if (HasEvent("Dawn", "MountainTalk")):
    show leaf surprisedbrow frownmouth with dis

    red @happy "Oh, her birthday?"

    leaf -surprisedbrow -frownmouth @sarcastic "...You just gotta suck the wind out of my sails, don't you? Like a hype vacuum."
    leaf @closedbrow talking2mouth "I should've known there was nothing I could tell you about one of your friends you didn't already know, anyway..."

else:
    red @talkingmouth "Her social security number?"

    leaf @talking2mouth "No, I'm still working on that one. Also, if you happen to learn her mother's maiden name, let me know."

    red @happy "Will do."

    leaf @talking2mouth "No, what I learned was that her birthday is this Saturday!"

leaf @closedbrow talkingmouth "So, I thought... drumroll please..."

pause 1.0

show leaf surprisedbrow frownmouth with dis

red @sad2eyes poutmouth "Brbrbrbrbrbrbr...?"

leaf @talking2mouth "What? Brbrbrbr? What was that?"

red @talkingmouth "That was a drumroll."

leaf @sarcastic "That was the sound a Jigglypuff makes when someone hugs it a bit too fast."

red @upeyes talking2mouth "So you thought you'd throw Dawn a birthday party."

leaf @surprised "Hey! That was supposed to be {i}my{/i} dramatic reveal!"

red @confused "Screw you, I took it. That's for making fun of my drumroll."

show leaf:
    xpos 0.5 alpha 1.0
    ease 20.0 xpos 0.25 alpha 0.3

leaf @sad "No! Not my dramatic reveal! However will I live, now? I literally {i}live{/i} on drama, [first_name]! {size=30}I can feel myself fading away...{/size}"

stop music fadeout 1.5 channel "crowd"
stop music fadeout 1.5 channel "crowd2"
stop music fadeout 1.5 channel "crowd3"
stop music fadeout 3.5

pause 1.0

red @closedbrow talking2mouth "Hm? Why did it get quiet...?"

show leaf:
    ease 0.2 xpos 0.5 alpha 1.0

leaf @surprised "Wait, look, over there, by the entrance to the cafeteria!"

show leaf:
    xpos 0.5 alpha 1.0

show screen songsplash("Looker Theme Lofi Noir Remix", "AlmightyArceus")
queue music "audio/music/anabel_start.ogg" noloop
queue music "audio/music/anabel_loop.ogg"

hide leaf with dis

show anabel with dis:
    xpos 0.75

anabel "{w=0.5}.{w=0.5}.{w=0.5}."

narrator "A purple-haired woman in a suit stands at the doorway, eyes scanning the crowd."

anabel @sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."

anabel @talking2mouth "Bianca Whittaker."

narrator "Her voice is much softer than you were expecting, but it still carries clearly throughout the whole cafeteria."

show bianca uniform with dis

bianca @sadeyebrows talkingmouth "Hi~i...? That's me, Miss?"

anabel @closedbrow talking2mouth "{i}Sigh.{/i}"
anabel @talking2mouth "Please come with me."

bianca frownmouth @sadeyebrows talking2mouth "Um, am I in trouble...?"

anabel @closedbrow talking2mouth "Please come with me."

hide anabel with dis

pause 1.0

bianca @surprised "O-oh... okay. Okay!"

show bianca:
    xpos 0.5
    ease 0.3 xpos 1.2

pause 1.0

show leaf uniform with dis:
    xpos 0.25

leaf @happy "Well, that's enough drama. I'm alive again."

redmind uniform @thinking "...Who was that? She looked like some sort of lawyer, but... maybe she's an agent...?"

narrator "You scan the cafeteria for Nate--Blake--and spot him sitting at his regular table, staring rigidly at the spot where the purple-haired woman disappeared."

hide leaf with dis

show nate uniform noshine surprisedbrow frownmouth with dis

redmind @thinking "...Oh, yeah, he {i}definitely{/i} recognizes her."

hide nate with dis

show leaf angrybrow frownmouth uniform with dis

leaf @talking2mouth "Hey, don't even think about it."

red @confused "What?"

leaf @talking2mouth "You're thinking of going after Bianca and Grape Hair, Esquire, aren't you?"

red @closedbrow talkingmouth "I actually {i}wasn't.{/i} I'm not that nosey. Besides, I can't really afford to be caught skulking around the school, given how in the toilet my reputation is right now."

leaf -angrybrow -frownmouth @talking2mouth "Oh, good."

pause 1.0

leaf @talking2mouth "Because we know a dragon with invisibility powers. So it'd be really easy for you, if you wanted to."

pause 1.0

leaf @flirtbrow talkingmouth "Just saying."

red @talkingmouth "If you're so curious, why don't {i}you{/i} go?"

leaf @talkingmouth "I don't want to get caught."

red @angrybrow talking2mouth "I don't want to get caught either!"

leaf @happy "And that's why I'm telling you not to go!"

red @sad2eyes talking2mouth "Okay, I realize that's what you're {i}saying{/i}, but I feel like what you {i}mean{/i} is very different."

leaf @sarcastic "I cannot be held responsible for your trust issues, Skippy. If you want to go, go, but if you don't, then--"
leaf frownmouth @surprisedbrow talkingmouth "Hm?"

python:
    rustiestsword = "Nate"
    rustiestswordvalue = 0
    for char in ["Nate", "Hilbert", "Hilda", "Bea"]:
        charvalue = GetRelationshipRank(char) * 100 + GetValue(char)
        if (charvalue > rustiestswordvalue):
            rustiestswordvalue = charvalue
            rustiestsword = char

if (rustiestsword == "Nate"):
    $ AddEvent("Nate", "AnabelFollow")
    show nate uniform with dis:
        xpos 0.75

    nate @talkingmouth "Heya, [nate_name]. Mind if I grab you for a sec?"

    red @confused "Are you coming onto me?"

    nate @winkbrow talkingmouth "I could be, if things go well."

    leaf @angrybrow talkingmouth "Ahem. I'm already taking the aggressively-sexual slot, please and thank you."

    show leaf blush surprisedbrow frownmouth with dis

    nate @happy "No need to fight. You can join in, if you want."

    show flashback with Dissolve(1.0)

    redmind @frownmouth "I don't understand. He seems so casual, now, but just last Saturday... is this really the same guy? The guy who fights aliens and wipes memories, making dumb sex jokes and kidding around like any other student?"

    hide flashback with dis

    red @talkingmouth "Anyway, yeah, you can grab me. What's up?"

    nate @talkingmouth "I'd just like to see what's up with Bianca."

    leaf @happy "{i}Hah!{/i}"

    nate @sad2eyes talking2mouth "She's helped me a {i}lot{/i} in the lab. She's gentle, kind. If {i}that woman{/i} wants to talk to her specifically, then... well, we should be around."

    red @closedbrow talking2mouth "Well, I guess if you're {i}asking{/i} me."
    red @confused "Does that mean you know her? The purple-haired woman, I mean?"

    show nate frownmouth with dis

    pause 1.0

    nate @sad2eyes talking2mouth "...No. But I {i}do{/i} know her name."

    nate @talking2mouth "And I guess I know enough to be worried. You'll come with me, right?"

    red @winkbrow talkingmouth "If you ask nicely."

    $ ValueChange("Nate", 1, 0.75)

    nate @happy "You flirt."

    leaf @sarcastic "Really. Right in front of my salad? Get out of here, you gayboys."

    hide leaf 
    hide nate
    with dis

elif (rustiestsword == "Hilda"):
    $ AddEvent("Hilda", "AnabelFollow")
    show hilda uniform with dis:
        xpos 0.75

    hilda @talkingmouth "Heya, [first_name]."

    if (GetRelationshipRank("Hilda") > 0):
        hilda @talkingmouth "You know how you're doing all that shit for me? Stuff I never asked for?"

        red @happy "Yes, I remember."

        hilda @talkingmouth "Well, now I'm actually {i}asking{/i} for something."
        hilda @sweat closedbrow talkingmouth "So... uh... it would mean a hell of a lot if you helped me out here."

    else:
        hilda @talkingmouth "I need a favor."
        hilda @sweat closedbrow talkingmouth "So... uh... it would mean a hell of a lot if you helped me out here."

    red @talkingmouth "Sure. What's up?"

    hilda frownmouth @talkingmouth "I want to follow Bianca."

    leaf @happy "{i}Hah!{/i}"

    hilda @sad "She's the only one in the dorm who actually does any goddamn work, besides myself. She's really sweet. And that purple-haired broad scares the hell out of me."

    red @confused "Scares you? What?"

    hilda @surprised "You saw her eyes, right? Those are the eyes of a woman who is {i}very{/i} used to cleaning up everyone's shit. Those were {i}not{/i} gentle eyes."
    hilda @sad "And... Bianca is basically a balloon crossed with a marshmallow. I just want to make sure she's alright."

    red @closedbrow talking2mouth "Alright. Fine, then. Let's follow her."

    $ ValueChange("Hilda", 1, 0.75)

    leaf @sarcastic "Oh, so when {i}I{/i} tell-don't-tell you to follow Bianca, it's a no-go, but the moment Hilda does, you're all for it."
    
    show hilda surprisedbrow frownmouth with dis
    
    leaf @sarcastic "Is it the booty shorts? I could totally buy some."

    hilda -surprisedbrow -frownmouth -surprised @happy "Damn, Leaf. I forgot what a riot you are. My new dorm is great, but it doesn't have the same humor you brought to the table."

    leaf @sad "And my new dorm is great, but it doesn't have the same cookies you and May brought to the table..." 

    hilda @smirkmouth "I'm sure I could make some more in the next batch and drop them by your dorm."

    show hilda surprisedbrow frownmouth with dis

    show leaf:
        xpos 0.5
        ease 0.5 xpos 0.33 ypos 1.2 zoom 1.1

    leaf @angry "[first_name]. {i}Keep Hilda alive.{/i}"

    hide leaf 
    hide hilda
    with dis

elif (rustiestsword == "Hilbert"):
    $ AddEvent("Hilbert", "AnabelFollow")
    show hilbert uniform with dis:
        xpos 0.75

    hilbert @talkingmouth "[first_name]."

    red @talkingmouth "What's up?"

    hilbert @talkingmouth "I want to follow Bianca."

    leaf @happy "{i}Hah!{/i}"

    red @confused "Really? How come?"

    hilbert @closedbrow talking2mouth "She's nice. And she's scared."

    red @confused "Scared?"

    hilbert @talkingmouth "Yes. She was shivering when she followed that purple-haired woman."

    red @talking2mouth "She had a huge smile on her face, though."

    hilbert @talkingmouth "She always does. That doesn't mean she's happy. You should know this. You're roommates with Ethan."

    pause 0.5

    red @sadbrow talkingmouth "That's really nice of you."

    hilbert @sadbrow talkingmouth "She's my dormmate. There's nothing more to it than that."

    if (GetRelationshipRank("Hilbert") > 0):
        hilbert @talkingmouth "When... that light you gave me... broke."
        hilbert @sadbrow talkingmouth "She helped me fix it."

    $ ValueChange("Hilbert", 1, 0.75)

    hilbert @talkingmouth "Let's go."

    hide hilbert with dis

    red @closedbrow talking2mouth "Jeez. He really hasn't gotten any more approachable since we were roommates."

    leaf sadbrow talkingmouth "Good luck. Stay alive."

    hide leaf 
    hide hilbert
    with dis

elif (rustiestsword == "Bea"):
    $ AddEvent("Bea", "AnabelFollow")
    show bea uniform with dis:
        xpos 0.75

    bea @talkingmouth "'Lo."

    red @talkingmouth "Bea. What's up?"

    bea @talkingmouth "Please accompany me as I follow Bianca."

    leaf @happy "{i}Hah!{/i}"

    red @confused "I mean, sure, but... why?"

    bea @closedbrow talkingmouth "I can sense a dangerous pressure emanating from the purple-haired woman."
    bea @talkingmouth "Bianca is gentle, and kind. I want to ensure no harm befalls her."
    bea @closedbrow talkingmouth "She is my roommate, after all."

    red @talkingmouth "...Alright, sure. But what do you mean, 'a dangerous pressure'?"

    bea @sad "I feel... as though this woman has knowledge of how to cause pain. True pain. This is..."

    narrator "Bea looks at Leaf somewhat awkwardly."

    leaf @happy "Oh, gotcha, private convo. I'll back off."
    leaf sadbrow @talkingmouth "Stay alive, you two."

    hide leaf with dis

    bea @sad "This is something I recognize. It is a sort of 'distance' in one's eyes. I would prefer to not see it in Bianca's."

    red @talking2mouth "Say no more. Let's go."

    $ ValueChange("Bea", 1, 0.75)

    bea @talkingmouth "Thank you."

    hide bea with dis

call clearscreens() from _call_clearscreens_184
scene blank2 with splitfade

narrator "You sneak out of the cafeteria, following [rustiestsword]."

narrator "You don't have to walk long before you hear Bianca and the purple-haired woman's voices coming from a classroom. You nod at [rustiestsword], questioningly."

if (rustiestsword == "Nate"):
    nate uniform @closedbrow talking2mouth "{size=30}Press yourself against the wall, here. And if I tell you to split, listen to me, and just do it.{/size}"

    red uniform @confused "{size=30}So commanding, all of a sudden.{/size}"

elif (rustiestsword == "Hilda"):
    hilda uniform @closedbrow talking2mouth "{size=30}Shit, there's nowhere to hide here... okay, just stay against the wall, and be prepared to book it.{/size}"

elif (rustiestsword == "Hilbert"):
    narrator "Hilbert ignores you and presses his ear up against the wall. You awkwardly do the same."

elif (rustiestsword == "Bea"):
    narrator "Bea presses a finger to your lips, then puts her ear up against the wall."

    redmind uniform @surprisedbrow frownmouth lightblush "Um."

    pause 1.0

    redmind @thinking "She didn't seem to think anything of that..."

narrator "You listen intently to the discussion in the classroom.{w=0.5}.{w=0.5}.{w=0.5}"

stop music fadeout 1.5
queue music "audio/music/nuvema1_start.ogg" noloop
queue music "audio/music/nuvema1_loop.ogg"

call clearscreens() from _call_clearscreens_185
show classroom 
show bianca uniform:
    xpos 0.25
show anabel:
    xpos 0.75
with Dissolve(3.0)

anabel @talkingmouth "{size=-20}is a{/size} {size=-15}matter of{/size} {size=-10}some interest{/size} to my {size=-5}employers{/size} and I."

bianca @happy "Well, Officer, I'm more than happy to answer any questions you might have!"

$ BecomeNamed("Anabel")

anabel @talkingmouth "Please, call me Anabel. Don't think of me as a police officer. Just think of me as... someone who has a couple questions for you."

redmind uniform @thinking "Anabel? From her appearance, I was expecting something like... Terminatrix, or something..."

bianca @confusedeyebrows talking2mouth "Ohhhh-kay?~"

anabel @closedbrow talkingmouth "{i}Sigh.{/i} One second."

anabel headset @talking2mouth "Headset on. Start recording. Interview: BW01."
anabel @talkingmouth "Bianca, can you confirm the name of your father?"

bianca @surprisedbrow frownmouth "Hm?"
bianca @happy "Well, of course! Daddy's name is Melvin Whittaker."

anabel sadbrow @talking2mouth "I see."

pause 1.0

anabel -sadbrow @talking2mouth "Can you describe the nature of his occupation?"

bianca @happy "Yup! Daddy's a brain surgeon."

anabel @talkingmouth "A well-paid profession."

bianca @talkingmouth "Sure is."

anabel @closedbrow talkingmouth "That would certainly explain how it is that you are here at Kobukan."
anabel @talking2mouth "However, our records show you have not lived under your father's roof for several months. Was he paying for you to attend?"

bianca @sadbrow talkingmouth "No way. Daddy wasn't really big on the idea of girls 'getting an education' or 'having lives.'"
bianca @happy "Actually, he kicked me out of the house as soon as I hit eighteen! Because I wouldn't 'shut up about going to college.'"
bianca @happy "Hiii~iiis words!~"

anabel @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
anabel @talking2mouth "Where have you been living, then?"

bianca @talkingmouth "Living with a coworker of his. Um, her name's Professor Fennel, and she's a scientist who works on Dream--"

anabel @talkingmouth "I'm familiar with her work."

bianca @talkingmouth "Her sister, Doctor Amanita, paid for me to go here, when Professor Fennel said I could be the best Oneirologist in the region if I got a proper education."
bianca @happy "And now I'm here! And I'm getting that education! And my pig of a Daddy can't stop me now!"

stop music fadeout 1.5

pause 1.0

show screen songsplash("Drought", "Zame")

queue music "audio/music/drought.ogg"

anabel @talking2mouth "Why?"

bianca @confusedeyebrows talking2mouth "Hm?"

anabel @talking2mouth "Why can't he stop you?"

bianca @sweat confusedeyebrows talkingmouth "Is this some kind of trick question? Because I'm here, and he's still in Nuvema Town."

anabel surprisedbrow @closedbrow talking2mouth "Let me start a new train of questioning. Do you remember where you were on the sixth of May, twelve days ago?"

bianca @happy "Nope! I never remember {i}anything{/i} unless I write it down!"

pause 1.0

anabel -surprisedbrow @closedbrow talking2mouth "You were participating in the second round of this region's 'Quarter Qlashes.'"

bianca @talkingmouth "Okay. I believe you."

anabel -surprisedbrow @sadbrow talkingmouth "...Thanks."
anabel @talking2mouth "During that time, you were interviewed by Lisabeth Lutia."
anabel @talking2mouth "...'Lisia.'"

bianca @surprised "Woaaah, that's her real name? That's so pretty!"

anabel @closedbrow talking2mouth "{size=30}{i}Please{/i} let me get through this...{/size} Look, during this time, you mentioned your father on internationally-broadcast television."
anabel @talkingmouth "Admittedly, it was just one of many channels covering the Quarter Qlashes, but what you said was very important. Do you remember what you said?"

bianca @closedbrow talking2mouth "Hm... yeah, I think so. I said my father was a pig, right? Then I said his address."
bianca @happy "Oh, actually, I tried to, but Lisia cut me off, so I don't think anyone heard me!"

anabel @closedbrow talking2mouth "She didn't cut you off fast enough. Someone heard you."

bianca @confused "Hm?"

pause 1.0

anabel sadbrow @talking2mouth "Bianca. What you did was a crime."

show bianca sadeyebrows sadeyes embarrassedmouth with Dissolve(2.0)

anabel -sadbrow @talkingmouth "In Unova, and Kobukan, it is a felony to link, then share, information with the intent of intimidation or harassment. Both pieces were public information, but linking them together is an offense."
anabel @sadbrow talking2mouth "Your father would be fully within his rights to press charges, as would the Town of Nuvema's Prosecutor's Office."

pause 0.5

bianca -embarrassedmouth frownmouth "...Am I going to jail?"

pause 0.5

anabel @sadmouth "Every crime has consequences, Bianca Whittaker."

pause 0.5

anabel sad "I'm sorry. I'm terrible with words. The consequence of this crime is that... is that your father..."

show blank

pause 0.1

hide blank

show bianca soullesseyes talking2mouth:
    xpos 0.25 ypos 1.0 zoom 1.0 rotate 0
    linear 0.1 ypos 0.95 zoom 0.95

stop music

anabel -sad @talking2mouth "Your father {color=#f00}was murdered.{/color}"

show glasses:
    xpos 0.25 ypos 0.9255 zoom 0.95 * 0.5 yanchor 0.6 xanchor 0.5
show bianca soullesseyes talking2mouth noglasses 
with dis

anabel @sadbrow talking2mouth "We... we believe that your revealing of his name and location may have..."

show glasses:
    ypos 0.95 rotate 0
    ease 2.0 ypos 0.96 rotate 1
    pause 0.2
    ease 0.5 ypos 2.0 rotate 2

pause 2.3

$ PlaySound("shatter.ogg")

pause 1.0

show bianca:
    ypos 0.95 zoom 0.95 xpos 0.25
    ease 1.5 ypos 1.2 zoom 1.0

pause 2.0

anabel @talking2mouth "...I'm sorry for your loss."

pause 1.0

anabel @surprisedbrow talking2mouth "Bianca?"

pause 1.0

bianca @talkingmouth "...My glasses. My glasses broke."
bianca @talkingmouth "I need to... I need to..."
bianca @shockedeyebrows soullesseyes sad2mouth "Ah! The glass--"

show blank

pause 0.1

show biancacannotsee with Dissolve(5.0)

bianca @sad3mouth "I... I {i}did{/i} this. I killed Daddy."

pause 5.0

anabel sad @talkingmouth "...There are other feasible explanations."

hide biancacannotsee 
hide blank
with Dissolve(2.0)

pause 1.0

show bianca sad2eyes frownmouth cry with dis:
    ypos 1.2 xpos 0.25
    ease 0.5 ypos 1.0

bianca @talking2mouth "...Leave me alone." 

anabel @closedbrow talking2mouth "I'm sorry. I need to ask you some more questions. You are under investigation--"

show bianca -cry blankeyes cry:
    xpos 0.25
    ease 2.5 xpos 0.55

bianca @talking2mouth "What? What left is there to ask? What can you even say right now?"

anabel @talkingmouth "...It is possible, given your stated poor relationship with your father, that... that you may have been working with..."

show bianca surprisedeyebrows:
    xpos 0.65
    linear 0.1 xpos 0.5

pause 1.0

bianca angryeyebrows furiouseyes "How dare you."
bianca furiouseyebrows furious2eyes furiousmouth cry2 "How {w=0.5}{i}dare{/i} you?"
bianca shadow cry3 furious2mouth "Get {w=0.5}{nw}"

show classroom with vpunch

$ PlaySound("thud2.ogg")

extend @talkingmouth "{size=40}{i}out!{/i}{/size}"

pause 0.5

anabel @closedbrow talking2mouth "...I'm sorry. We'll need to talk later. But I'll leave you alone for now."

hide anabel with dis

pause 2.0

show bianca -shadow sadeyebrows sadeyes talking2mouth with dis:
    xpos 0.5 ypos 1.0
    parallel:
        ease 0.5 xpos 0.52
        ease 1.0 xpos 0.48
        ease 1.0 xpos 0.52
        ease 0.5 xpos 0.5

    parallel:
        ease 3.0 ypos 1.2

bianca @talkingmouth "Daddy... no, no, no... {i}Daddy...{/i}"

scene blank2 with splitfade

pause 0.5


if (GetMood("Bianca") > -10):
    $ persondex["Bianca"]["Mood"] = -10

    narrator "Bianca's mood has fallen to {color=#f00}{i}Desolate.{/i}{/color}"

else:
    narrator "Bianca's mood is {color=#f00}{i}Desolate.{/i}{/color}"

scene academyhall 
show screen currentdate
if (rustiestsword == "Nate"):
    show nate uniform closedbrow tears frownmouth
elif (rustiestsword == "Hilda"):
    show hilda uniform sad
elif (rustiestsword == "Hilbert"):
    show hilbert uniform sad
elif (rustiestsword == "Bea"):
    show bea uniform sad
with splitfade

if (rustiestsword == "Nate"):
    nate @sadmouth "Sh-shit. Anabel's coming. We need to... we need to get out of here, [nate_name]. Come on."

    hide nate with dis
elif (rustiestsword == "Hilda"):
    hilda "Shit. What the fuck was that? Bianca doesn't deserve that..."
    hilda @angry "Damn it! I feel so goddamn powerless! What are we supposed to do here?"

    pause 1.0

    hilda "That woman's coming. C'mon. We need to go."

    hide hilda with dis
elif (rustiestsword == "Hilbert"):
    hilbert @angry "...This... this can't be fair. Bianca was innocent. She's kind. This shouldn't have..."
    hilbert @closedbrow talkingmouth "Not... not to her. Why did it have to be her...?"

    pause 1.0

    hilbert @talkingmouth "That woman's coming. I'm leaving. You should, too."

    hide hilbert with dis

elif (rustiestsword == "Bea"):
    bea "I... I cannot stop myself from weeping."
    bea @talkingmouth "This is too unfair. Such reckless hate could not have been laid on a more undeserving head." 
    bea "...I have no words to allay this pain. No plan I could conceive of could lift a single of Bianca's burdens..."

    pause 1.0

    bea @closedbrow talkingmouth "The agent is about to leave the classroom. Perhaps we should make ourselves scarce."

    hide bea with dis

$ removestudents = { rustiestsword, "Bianca" }

menu:
    ">Confront Anabel":
        jump confrontanabel

    ">Hide from Anabel, then comfort Bianca":
        jump comfortbianca

    ">Follow [rustiestsword] back to the cafeteria":
        show blank2 
        show screen currentdate
        with splitfade

        $ pronoun = "he" if rustiestsword in ["Nate", "Hilbert"] else "she"
        $ pronoun2 = "his" if rustiestsword in ["Nate", "Hilbert"] else "her"

        narrator "You follow [rustiestsword] back to the dining hall."
        narrator "However, as soon as you get there, [pronoun] says [pronoun]'s going back to [pronoun2] dorm to think."

        pause 1.0

        narrator "...You're unsure what to do, and decide to continue on as you were."

        scene cafe with splitfade
        $ renpy.music.play("Audio/bigcrowdloop.ogg", channel='crowd', loop=True, fadein=0.5)

        jump PickTable

label confrontanabel:
stop music fadeout 1.5

show screen songsplash("Looker Theme Lofi Noir Remix", "AlmightyArceus")
queue music "audio/music/anabel_start.ogg" noloop
queue music "audio/music/anabel_loop.ogg"

$ AddEvent("Nate", "ConfrontAnabel")

narrator "You grit your teeth and prepare to give Anabel a piece of your mind as she walks out of the classroom."

show anabel sad with dis

narrator "She doesn't seem to notice you."

show anabel surprisedbrow frownmouth with dis

red uniform @angrybrow talking2mouth "Hey."

show anabel -surprisedbrow -frownmouth with dis

narrator "Anabel immediately reaches for a Poké Ball on her belt, but pauses."

anabel @talking2mouth "Hello. Can I help you?"

red @angrybrow talking2mouth "There was a much better way to do that."

anabel @closedbrow talking2mouth "I'm afraid I have no idea what you're talking about."

red @talking2mouth sadbrow "Your conversation with Bianca. First you tell her, out of nowhere, that her father is dead, then you accuse her of having a part in it?"

anabel @angrybrow talking2mouth "My delivery was lacking, this I acknowledge. But I am not in the habit of discussing the execution of my duties with strangers."
anabel @closedbrow talking2mouth "Especially given that you were not intended to be privy to that conversation."
anabel @talking2mouth "It is fortunate for you that nothing of any relevance to national security was discussed in that room. If you had heard something you shouldn't have..."

redmind @frownmouth "That's an empty threat. I'm confident this woman works with Nate. And Nate wouldn't discuss anything important in an unsecured room like that, so she definitely wouldn't, either."

red @closedbrow talking2mouth "Fine. Sorry for bothering you."

pause 0.5

anabel @talking2mouth "...I understand you are upset for your friend. I am upset, too."
anabel @closedbrow talking2mouth "To act on this upset is a privilege not afforded to me. I must consider every possible outcome. This is a matter of life and death, even now."

pause 0.5

anabel @closedbrow talking2mouth "Pardon me."

hide anabel with dis

redmind @confusedeyebrows frownmouth "...Even now? That seems to imply that this isn't over, somehow... what could that mean?"

pause 1.0

menu:
    ">Go back to the cafeteria":
        show blank2 
        show screen currentdate
        with splitfade

        narrator "You decide to give Bianca some space and go to the cafeteria."

        scene cafe with splitfade
        $ renpy.music.play("Audio/bigcrowdloop.ogg", channel='crowd', loop=True, fadein=0.5)

        jump PickTable

    ">Go into the classroom, to comfort Bianca":
        pass

label comfortbianca:

show blank2 with splitfade

pause 1.0

show afternoon at vspaz

pause 3.5

$ timeOfDay = "Afternoon"

stop music fadeout 1.5
show screen songsplash("An Unwavering Heart", "Zame/Pokestir")
queue music "audio/music/unwaveringheart.ogg"

$ AddEvent("Bianca", "Comfort")

call clearscreens() from _call_clearscreens_186
show blank2 with splitfade

pause 1.0

show classroom 
show bianca uniform closedbrow frownmouth cry noglasses
with splitfade

pause 0.5

red uniform @sadbrow talking2mouth "...Bianca?"

bianca @sadbrow talking2mouth "...Red hat?"

red @sadbrow talkingmouth "That's me. Red hat number three."

pause 0.5

red @sadbrow talkingmouth "...Do you want to talk?"

pause 0.5

bianca shadow "...No."

pause 0.5

red @sad "Would you like me to leave?"

pause 0.5

bianca -shadow -closedbrow sadeyebrows @sideeyes sadeyebrows talking2mouth "No."

$ ValueChange("Bianca", 3)

red @talkingmouth "Okay."

show bianca:
    ease 0.5 ypos 1.0 zoom 1.1

narrator "You take a seat at a desk two away from Bianca, stepping around the broken glass."

pause 1.0

narrator "And you wait. For a {i}very{/i} long time."

pause 1.0

narrator "You're unsure what to say. When a person dies, you generally speak well of them. You remember their life, their accomplishments, the marks they left on the living."
narrator "But, in this case, you don't know who Bianca's father was. And what you {i}do{/i} know of him doesn't paint a good picture."

pause 0.5

red @talking2mouth "Sorry for listening in."

bianca @sadeyes talking2mouth "It's alright. I-- {w=0.5}{i}hiccup.{/i} I don't mind."

pause 0.5

red @sadbrow talking2mouth "...What does this change?"

bianca @closedbrow talking2mouth "N-nothing. {w=0.5}{i}Sniff.{/i} I'm still living with Professor Fennel. Doctor Amanita is still paying for me to be here. He wasn't a part of my life--a part of {i}anything{/i}."

pause 0.5

bianca @sideeyes sadeyebrows talking2mouth "...Why am I sad? I shouldn't be sad. I should just hook a smile onto my face, like I always do. This is a goo-- {w=0.5}a goo--"
bianca @closedbrow sadmouth "...I can't say it."

pause 0.5

bianca @closedbrow talkingmouth "I... didn't {i}lose{/i} anything. So why am I sad?"

red @talking2mouth "...You don't always love your family. You don't even always like them. But I think you always wish you could, and hope that one day, they might do the same for you."
red @sad "And you... you lost that hope. That's where your pain is coming from."

bianca @sideeyes talking2mouth "...I guess you're right."

pause 0.5

bianca @sadbrow talkingmouth "Thank you. I know you're trying to make me feel better."

red @sadbrow talkingmouth "'Trying?' Not succeeding?"

bianca @sadeyes talking2mouth "...Sorry. It's too new. I don't think I'm even past 'denial', yet."

red @sadbrow talkingmouth "I understand."

pause 0.5

bianca @closedbrow angrymouth "I just wanted to prove to him that he was wrong. I wanted to prove to him that I could be more than what he thought I was."
bianca @sadbrow talking2mouth "And now... now he's dead. And I've missed my chance. Forever."

red @talking2mouth "I know you didn't like him. Your performance at the QQs made that pretty clear."
red @closedbrow talking2mouth "But... who {i}was{/i} he?"

bianca @sideeyes talking2mouth "He was a brain surgeon. He was really good at it... and because he was good at cutting open people's brains, he thought he knew how everyone's brains worked."
bianca @sadeyes talkingmouth "He thought he could tell, from a short list of demographics information, everything about you. He saw patterns everywhere, patterns where they didn't exist."
bianca @talkingmouth "He wanted to know everything. But you can't. So he'd just make wide generalizations--assumptions--and treat them like they were facts."

pause 0.5

bianca @talkingmouth "Over time, those patterns drove away Mom. Daddy got worse, after that. He thought that if I went to university, they'd radicalize me, and... and I'd leave him too."
bianca @closedbrow cry angrymouth "But... but then he kicked me out of the house! If he was afraid of me leaving, then why would he kick me out of the house?! I didn't {i}want{/i} to go!"
bianca @sadbrow talking2mouth "...On that day, I begged him to let me stay. I cried for a week before. I hugged him so hard, because I didn't want to leave, but he called the police, and they dragged me away from him..."

pause 0.5

bianca @shadow angryeyebrows talking2mouth "And now the police have taken him away from me {w=0.5}{i}again.{/i}"

pause 1.0

bianca sad3mouth sad2eyes cry2 -cry "It's not fair. It's {i}so{/i} not fair. I didn't hate him. I {i}didn't{/i} hate him. I just wanted to get back at him a little bit. I never thought... I never thought anyone would..."

narrator "Bianca seems to be hyperventilating."

menu:
    "Take deep breaths, Bianca.":
        show bianca frownmouth -sadeyes cry -cry2 with dis

        red @talkingmouth "It's alright, Bianca. I won't say 'calm down', but you'll get through this. No-one thinks you hated him, or wanted this. Even Anabel doesn't. It's obvious."

    ">Hug her":
        $ AddEvent("Bianca", "BiancaHug")
        show bianca surprisedbrow -cry2 cry frownmouth with dis:
            ease 0.5 zoom 1.3 ypos 1.1

        red @talkingmouth "It's alright, Bianca. I won't say 'calm down', but you'll get through this. No-one thinks you hated him, or wanted this. Even Anabel doesn't. It's obvious."

        show bianca closedbrow lightblush with dis

        pause 1.0

        red @sad2eyes lightblush talking2mouth "Er, sorry, should I--?"

        $ ValueChange("Bianca", 3)

        bianca @closedbrow talking2mouth "Please don't let go."

        pause 0.5

        red @closedbrow talkingmouth "Alright. {size=30}It'll be alright.{/size} {size=20}There, there. It'll all be fine.{/size}"

pause 2.0

bianca -lightblush -closedbrow @sad "How can you say that? What if Anabel comes back and wants to put me in prison?"
bianca @closedeyes sadeyebrows talking2mouth "Maybe... maybe I {i}should{/i} be in prison."

red @sad2eyes frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
red @talking2mouth "No. I don't know what the law says, or what 'the rules' are, or whatever, but I know you. You're a kind, friendly, good-hearted, girl that everyone loves."
red @sadeyebrows talkingmouth "If you 'should be' in prison, then there's not a person in this school who shouldn't be locked up."

pause 0.5

bianca @closedbrow talking2mouth "...I wish Cheren was here."

red @angryeyebrows surprisedeyes frownmouth "...Woah, I think that just gave me whiplash." 
red @sadbrow sweat talking2mouth "Why Cheren?"

bianca @talkingmouth "Cheren... knew Daddy."

red @surprised "Hm? Oh, that's right..."

show cafeB_CG at sepia, dissolvein behind flashback:
    subpixel True
show flashback
with dis

pause 0.5

$ hideside = True

cheren @talkingmouth "In many ways her focus surpasses mine."

bianca @talkingmouth "Aw, thanks! I knew I'd have to take this seriously after that big brouhaha with my Dad, though."

cheren @talkingmouth "Er... yes. That was quite a 'brouhaha.'"

show blank with splitfade

hide flashback
hide cafeB_CG
hide blank
with dis

$ hideside = False

pause 1.0

red uniform @closedbrow talkingmouth "What was this 'brouhaha,' then?"

bianca @sadbrow talkingmouth "Oh... it was when Daddy was kicking me out of the house."
bianca @talkingmouth "Cheren came over to try and talk some sense into him. A week of me crying and begging hadn't done anything, so I told him not to bother, but..."
bianca @happybrow talkingmouth "But Cheren doesn't stop fighting just because the battle's lost."

pause 0.5

bianca @talking2mouth "He tried to convince Daddy that he was making a mistake, that I could absolutely go to college, that he was going to ruin his relationship with his daughter."
bianca @sideeyes talking2mouth "...But Daddy refused to listen, and demanded that Cheren leave his property."
bianca @closedbrow talking2mouth "...And when Cheren refused, Daddy sent out his Lampent to force him to leave."

pause 0.5

bianca @sadbrow talkingmouth "Cheren's Snivy was no match for my Dad's Lampent. He lost. Badly."
bianca @sadbrow talking2mouth "He looked... {i}so{/i} guilty."
bianca @talking2mouth "I think he's the only one who could really understand how I felt about Daddy, having met him..."

pause 0.5

redmind @closedbrow frownmouth sweat "I can't believe I'm going to say this."

red @sadbrow talkingmouth "Do you want me to get him?"

bianca @talking2mouth "...No. I don't want him to see me like this."

pause 1.0

bianca @talkingmouth "Before my Mom left... she told me to always keep a smile on my face. That there are people out there who can only win by making you cry."
bianca @closedbrow talking2mouth "Cheren's... the only one who knows what my Dad was like. So if he sees me cry, then... then Daddy wins."

pause 1.0

red @sad2eyes sadeyebrows talking2mouth "...Look. Cheren and I aren't best buds, exactly, but if you need a friend, he can be there for you."

$ pronoun = "he" if rustiestsword in ["Nate", "Hilbert"] else "she"

red @sadbrow talkingmouth "And, I mean, I can, too. And don't forget about [rustiestsword]. I know [pronoun] cares about you."

pause 0.5

bianca -cry @talking2mouth "...Yeah. Yeah, I guess so. {i}Sniff.{/i}"

pause 1.0

bianca @sadeyebrows closedeyes talking2mouth "I miss him already."

pause 0.5

red @sadbrow talking2mouth "It's only been... half an hour or so."

pause 1.0

bianca @surprised "Half an hour? Oh, no! You need to get back to class, right? You should be in your elective class."

red @happy "Bianca, c'mon. A friend of mine is crying in an empty classroom, and you think I can just go to class and focus on studying damage formulas?"

bianca @sadeyebrows talking2mouth "...Are we friends?"

red @sadeyebrows talkingmouth "'Friend' is kind of my default relationship with everyone I meet."

bianca @sadbrow talkingmouth cry "I actually thought... {i}Sniff.{/i} I thought you might hate me for what Cheren did."

red @happy "Nah. Those were {i}his{/i} choices. I'm not going to blame someone for their friend's actions."

bianca @sideeyes talking2mouth "...Well. I, um... I was actually the one who suggested to him you might have some kind of power."

red @surprisedeyes angryeyebrows frownmouth "{w=0.5}What?"

bianca @sadeyes talking2mouth "{i}Please{/i} don't be mad."

red @sad2eyes talking2mouth "I... I can't be mad, of course, not now, but... what's this about?"

bianca @sadeyes talking2mouth "Nurse Miriam was teaching us about Aura-wielders in our Human Physiologies class, and she mentioned that Aura-Wielders are able to connect with people on a deeper, subconscious level."
bianca @sideeyes talking2mouth "Then, when we were hanging up campaign posters..."

scene academy:
    xpos -700 ypos -525
show bianca 
show flashback
with splitfade

cheren @closedbrow talkingmouth "I swear, it's the oddest thing. Serena and Calem's campaign is doing well enough, but [first_name]'s is absolutely soaring."
cheren @talkingmouth "He has a way of touching the hearts and minds of the voters that I can't help but envy. It's a shame he doesn't seem overly enthused about his own progress."
cheren @happy "Oh, well. I suppose I might as well just cheer him on. What do you think, Bianca?"

show bianca:
    ypos 1.0
    block:
        ease 0.3 ypos 1.1
        ease 0.3 ypos 1.0
        repeat 5

bianca @happy "I dunno. You should be doing waaaa~aaay better than him. I mean, he's not trying {i}at alllll.{/i} Ooh, I bet [first_name]'s an Aura-user!"

cheren @surprised "Beg pardon?"

bianca @talkingmouth "'Aura' is a mental and physical power that some people have. They're like Espers, except they train to get their powers, instead of being born with 'em."
bianca @happy "Nurse Miriam just taught us about Aura-Users! Most of 'em come from Sinnoh."

cheren @closedbrow talking2mouth "I don't understand. How would this power help?"

show bianca:
    ypos 1.0
    block:
        ease 0.2 ypos 1.1
        ease 0.2 ypos 1.0
        repeat 5

bianca @talkingmouth "Apparently, Aura-Users can share their emotions with people, and read the emotions of others."

cheren @talking2mouth "I don't see how that would help in his campaign efforts."

show bianca:
    ypos 1.0
    block:
        ease 0.1 ypos 1.1
        ease 0.1 ypos 1.0
        repeat 5

bianca @happy "Because if you know how people feel about what you're saying, you know exactly what to say to make them happy!"

cheren @closedbrow "{w=0.5}.{w=0.5}.{w=0.5}."
cheren @closedbrow talkingmouth "No, that's silly, Bianca. Besides, Aura is--you said it's a trained power? Mostly from Sinnoh?"
cheren @talkingmouth "[first_name] can't be much older than eighteen. And he certainly isn't Sinnohan."
cheren @happy "No, I'm afraid I've got nothing to blame for my failings but an inability to get my message across clearly!"

pause 0.5

cheren @talkingmouth "Besides, we're not competing for seats. There's no reason for us to come into conflict."
cheren @happy "Although, if there was, I should be quite glad that he doesn't have a Lampent!"
cheren @talkingmouth "I still shudder whenever I see one of them. Oof. That was quite a beating I received."

bianca @happy "Yeah, I guess you're right."

hide bianca

cheren @talkingmouth "Hm."

pause 0.5

cheren @sad2eyes noshine "{w=0.5}.{w=0.5}.{w=0.5}."
cheren @sad2eyes noshine talking2mouth "Surely not."

scene classroom
show bianca uniform noglasses sadeyebrows frownmouth
with dis

pause 1.0

bianca @talking2mouth "...Are you mad?"

menu:
    "A little, yeah.":
        $ AddEvent("Bianca", "LittleMad")
        
        red uniform @closedbrow talking2mouth "...Now isn't the time. I'm trying to make you feel better, right now."

    "Nah.":
        $ AddEvent("Bianca", "NotMad")
        $ ValueChange("Bianca", 3)

        red uniform @closedbrow talking2mouth "...I might've been mad at one point, but I'm over it now. Besides, it doesn't matter if you put the idea in his head. He was the one who acted on it."

        red @talkingmouth "And even if I {i}was{/i} mad, now wouldn't be the time for it. I'm trying to make you feel better, right now."

pause 1.0

bianca @talkingmouth "I think... actually... I {i}do{/i} feel a little better."

pause 0.5

bianca @talking2mouth "Thank you for letting me cry on you."

red @talkingmouth "It's alright. I'm sorry you had to cry in the first place, but if you need to, my shoulders are ready to serve."

bianca @talking2mouth sadbrow "...Thanks."

pause 1.5

show bianca:
    ypos 1.0
    block:
        ease 0.5 ypos 1.1
        ease 0.5 ypos 1.0
        repeat 2

bianca @sadbrow talkingmouth "You have excellent [bluecolor]shoulders.{/color}"

red @talkingmouth "...They're all yours. Keep your chin up. And call me whenever you want to talk, okay? We're all here for you."

bianca @closedbrow talking2mouth "...Okay."

python:
    haslitwick = False
    haslampent = False
    haschandelure = False
    
    for mon in AllPokemon():
        if (mon.GetId() == pokedexlookupname("Litwick", DexMacros.Id)):
            haslitwick = True
        elif (mon.GetId() == pokedexlookupname("Lampent", DexMacros.Id)):
            haslampent = True
        elif (mon.GetId() == pokedexlookupname("Chandelure", DexMacros.Id)):
            haschandelure = True

if (haslampent):
    red @talkingmouth "...So Cheren's afraid of Lampent, huh?"
    red @happy "It just so happens that I have one..."
    
    bianca @poutmouth sadbrow "Don't be a meanie."
    
    red @sadbrow talkingmouth "Sorry. Just joking."

elif (haschandelure):
    red @talkingmouth "...So Cheren's afraid of Lampent, huh?"
    red @happy "It just so happens that I have a Chandelure..."
    
    bianca @poutmouth sadbrow "Don't be a meanie."

    red @sadbrow talkingmouth "Sorry. Just joking."

elif (haslitwick):
    red @talkingmouth "...So Cheren's afraid of Lampent, huh?"
    red @happy "It just so happens that I have a Litwick..."

    bianca @poutmouth sadbrow "Don't be a meanie."

    red @sadbrow talkingmouth "Sorry. Just joking."

hide bianca with dis

$ oldbond = GetRelationship("Bianca")
$ persondex["Bianca"]["Relationship"] = "Shoulder"
$ persondex["Bianca"]["RelationshipRank"] = 1

$ PlaySound("sav.ogg")

narrator "Your heart shifts as you feel your relationship with Bianca evolve from '{color=#0048ff}[oldbond]{/color}' to '{color=#0048ff}Shoulder{/color}'!"

pause 1.0

call clearscreens() from _call_clearscreens_187
show blank2 
with Dissolve(1.0)

show evening at vspaz

pause 3.5

$ timeOfDay = "Evening"

narrator "However... you have missed an elective class, and the rest of lunch. You should probably hurry to homeroom before you miss that, too."

jump secondhomeroom010518