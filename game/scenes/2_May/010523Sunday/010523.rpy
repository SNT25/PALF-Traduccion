label day010523:

$ timeOfDay = "Morning"
call clearscreens() from _call_clearscreens_209
call calendar(1) from _call_calendar_48

$ calDate = calDate.replace(day=23, month=5, year=2004)

$ HealParty()

stop music

scene blank2
show morning at vspaz

pause 3.5

show screen songsplash("Pallet Town", "Zame")
queue music "audio/music/palletpiano.ogg"

scene kitchen 
show leaf hatless:
    xzoom -1
with splitfade

leaf @talkingmouth "Welcome back. How was your run?"

red @talkingmouth "Alright. Rained a bit last night, I think, so the grass was really mushy. Got my shoes all dirty, so I figured I'd scrub them off before heading back out to polite company."

leaf @sadbrow talkingmouth "You know, if you want a new pair, you can just ask."

red @happy "I know. But you know what I'd say to that."

leaf @closedbrow talking2mouth "Yeah, yeah, you don't want to be dependent..."

red @sadbrow talkingmouth "Save 'em for my birthday."

leaf @talkingmouth "Alright."

pause 1.0

red @closedbrow talkingmouth "On the topic of things you're going to do for me--"

leaf @surprisedbrow talkingmouth "That's a hell of a segue. My heart just went from zero to a hundred."

red @confused "I'm pretty sure neither of those numbers are healthy."
red @unamusedbrow talking2mouth "Anyway, do you mind if I finish?"

leaf @blush flirtbrow talkingmouth "Go ahead."

red @talkingmouth "Weren't we meant to be going somewhere? Doing something?"

if (HasEvent("Leaf", "RejectedConfession")):
    red @confused "I mean, after straight-up rejecting my rejection, I kinda figured you'd be pushing this outing harder."

    leaf @angrybrow angrymouth "I did {i}not{/i} reject your rejection. I said I was going to accept it! For now! That's the opposite of a rejection!"

    red @unamusedeyebrows talkingmouth sweat "Yeah, except for the 'for now' part."

    leaf @closedbrow talking2mouth "That's a minor detail."
    leaf @talking2mouth "Anyway, I'm going to get around to it. It's just not super-high on my priority list."

    red @confused "Really?"

    leaf @sarcastic "Dude. I flew across an ocean for you, and last week I was looking for Tia. I can take a break, right?"

    red @talkingmouth closedbrow sweat "My bad."

else:
    red @confused "I mean, after flying across an ocean to get me, I kinda figured you'd be pushing this date harder."

    leaf @blush embarrassedbrow "{w=0.5}.{w=0.5}.{w=0.5}."
    leaf @blush embarrassedbrow talking2mouth "So... when you were a kid, did you rip into your Snowfall Day presents as soon as you woke up, or did you sort of dance around them for hours, trying to predict what was inside?"

    red @confusedeyebrows frownmouth "Hm?"
    red @closedbrow talking2mouth "Well, we didn't have a lot of presents on Snowfall day, so I wanted to make them last. I'm not sure I'd say I danced around them, but, yeah, I made them last. Opened one every few hours."

    leaf @blush talkingmouth sadbrow "Well... there you go."

    red @happy blush "Aw. I'm flattered."

leaf @talking2mouth "Anyway, I should be able to get things sorted sometime next week. How's Wednesday sound?"

red @talking2mouth "I'll have to clear my schedule--I've got high tea with the queen of Galar booked then--but I can probably shuffle some things around."

leaf @flirtbrow blush talkingmouth "Very gracious of you. I'd say it'll be worth the wait, but if Dawn's birthday was any indication..."

red @happy "Dawn's birthday was great. She loved it!"

leaf @talking2mouth "That was a fraction of a fraction of a fraction of what I can do, Skippy. I was operating at level five, there. I'm a level eighty, at least."

red @sweat talkingmouth "Yeah, Dawn {i}does{/i} like her level differences."

leaf @closedbrow talkingmouth "Dork. I'm going out. See you later?"

red @talkingmouth "See ya."

call freeroam() from _call_freeroam_29

call texting() from _call_texting_24

scene blank2 with dis

stop music fadeout 1.5

show midnight at vspaz
$ timeOfDay = "Midnight"

pause 3.5

if (GetRelationshipRank("Blue") > 0):
    $ renpy.music.queue("audio/music/Eterna_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
    $ renpy.music.queue("audio/music/Eterna_Loop.ogg", channel='music', loop=True)

    scene bedroommidnight 
    show screen currentdate
    with Dissolve(3.0)

    pause 2.0

    red night swimsuithatless @closedbrow talking2mouth "Zzz... zzz... zzz..."

    $ PlaySound("knock.ogg")

    pause 1.0

    redmind @unamusedbrow unamusedmouth tired "...Swear to god, if that's Leaf trying to organize a midnight booty call..."

    if (HasEvent("Leaf", "AcceptedConfession")):
        redmind @happy tiredhappy "Oh, who am I kidding, that'd be great!"

    red @talkingmouth tired "Yeah?"

    blue night og @closedbrow talkingmouth "It's me."

    pause 1.0

    red @surprised "Woah, that woke me up. I didn't expect that. What's up?"

    stop music fadeout 1.5

    show screen songsplash("A Rival Appears!", "Zame")

    queue music "audio/music/rivalchill_start.ogg" noloop
    queue music "audio/music/rivalchill_loop.ogg"

    blue @wistful "I want to battle."

    red @sadbrow talking2mouth "Geez, Blue. We battled last week."

    blue @angry "We're rivals! We should be battling every day!"

    if (GetRelationship("Blue") == "Listener"):
        red @confused "I thought I was your 'listener'?"

        blue @angry "If you are, then listen to me when I say we need to battle!"

    red @closedbrow talkingmouth "I don't know. It's late, curfew's up. We can't battle in the suite, it's too small. We'd have to go out, and then Cheren would catch us."

    show bedroommidnight with vpunch

    blue @angry "Look!"

    pause 1.0

    blue @closedbrow wistfulmouth "Look. I screwed up yesterday. Ethan and Yellow are mad at me. I still haven't talked to Gramps. Not once all week." 
    blue @wistful "I'm confused, and I don't know how to make friends, and now that I'm {i}trying{/i}, people think I'm just doing it to get the damn kidney stones."
    blue @wistfulmouth "And I am! But not towards the only people that Eevee's {i}actually{/i} created the stones for."

    red @talkingmouth "Wait, so... earlier this week, when you gave me the Soothe Bell... you were {i}actually{/i} trying to patch things over?"

    blue @wistful "And then Eevee threw up the stones, and I didn't know what to do but pick them up and leave."
    blue @angry "{i}I{/i} was trying to be the bigger man, but then you had to screw up my plan by apologizing to {i}me!{/i}"

    red @unamusedbrow unamusedmouth "[ellipses]"
    red @upeyes talking2mouth "That must have been very hard for you."

    blue @angry "Thank you! Finally, someone who's reasonable about this stuff!"

    redmind @confusedeyebrows poutmouth "...Nate might have fried Blue's brain with that memory-wipe. This isn't the Blue I remember... {i}at all.{/i}"

    blue @talkingmouth "So... I'm confused. I don't know what's going on. I'm frustrated, and everything I'm working on is failing and I need to get back to what I'm good at--beating you!"

    red @unamusedbrow frownmouth "{i}Sigh.{/i}"
    red @upeyes angryeyebrows talking2mouth "Where were you planning on battling? We can't go to the Battle Hall at this time of night."

    blue @talkingmouth "The recreation center. There's a pool there for faculty that they {i}never{/i} use. It's open at night, too."

    if ("Water" in [GetStatRank(0), GetStatRank(1), GetStatRank(2)]):
        blue @talkingmouth "You've taken a bunch of Water-type classes. That's practically a free advantage for you."

    blue @talkingmouth "Come on."

    menu:
        "[bluecolor][[Blue Rank 1]{/color} Fine, but I want to be thanked.":
            $ AddEvent("Blue", "ThankMe")
            blue @surprised "What?"

            red @talkingmouth "You heard me. There's a serious chance we'll get busted for this. That might screw up my scholarships, which I seriously need."
            red @talkingmouth "If I'm going to risk all that for you, at 1 AM in the morning, I'm going to need you to at least acknowledge it."

            blue @scaredeyes angryeyebrows frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
            blue @closedbrow talkingmouth "Yeah, fine."

            red @happy "Cool. You can thank me after I beat you."

            blue @angrybrow happymouth "Hah! Fat chance."

        ">Take him up on the challenge":
            red @talkingmouth "Fine. But if you're pulling me out of bed at this time of night to go break school rules, I'm going to mop the pool with you."

            blue @angrybrow happymouth "It's 'sweep the floor', and fat chance!"

        ">Reject the challenge":
            red @talking2mouth "No."

            blue @angrybrow talking2mouth "What?"

            red @upeyes talking2mouth "You don't need a battle to clear your head, you need to take an online seminar on communication." 
            red @closedbrow talking2mouth "I'm going to bed. If you want to battle at a {i}normal{/i} time, when we {i}won't{/i} get in trouble for it, hit me up."

            $ ValueChange("Blue", -1, -0.5)

            blue @angry "Tch."

            show blank2 with transeye

            pause 1.0

            narrator "You close your eyes, ignoring Blue's frustrated grunts outside, and eventually drift off to sleep."

            jump endweek7

    red @closedbrow talking2mouth "Just give me a second to get changed."

    call clearscreens() from _call_clearscreens_210
    scene blank2 with splitfade

    narrator "You and Blue quickly make your way from the dorm room to the recreation center pool, loudly whispering at each other to make less noise."

    scene facultypoolnight 
    show blue og 
    show screen currentdate
    with splitfade

    red @confused "Geez. I think this pool is even nicer than ours."
    red @closedbrow talking2mouth "Not happy about how bright it is, though... electric costs aside, we're pretty lit up. I don't want to stay here for too long."

    blue @closedbrow talking2mouth "It's fine. It won't take long for me to beat you."
    blue @talkingmouth "Come on. No more chatting. Let's do this."

    if (HasEvent("Blue", "ThankMe")):
        red @talking2mouth "Win or lose, I'm getting my thanks, right?"

        blue scaredeyes surprisedeyebrows frownmouth @surprised "Wha-yes! Why are you so fixated on this? It's just words!"

        red @confused "Believe it or not, I actually care about what you say."

        pause 1.0

        $ ValueChange("Blue")

        blue -scaredeyes -frownmouth -surprisedeyebrows @closedbrow talkingmouth "You can't throw me off like that."

        red @upeyes talking2mouth "Whatever, man."

    else:
        red @talkingmouth "You're on."

    red @talkingmouth "[pika_name], time to wake up. We've got a battle to do."

    $ PlaySound("Pokemon/pikachu_sad.ogg")
    libpikachu sad "Piiiika."

    red @happy "Don't suppose you'd be willing to tell what the Foreverals your Eevee made do?"

    blue @angrybrow talkingmouth "Oh, you'll find out!"

    red @sweat closedbrow talking2mouth "Fair enough."

    python:
        trainer1 = MakeRed()
        trainer2 = MakeTrainer("Blue")

    call Battle([trainer1, trainer2], customexpressions=["red", "red angrybrow happymouth", "blue og", "blue og angrybrow happymouth"], dialogfunc=firsteeveebattle) from _call_Battle_157
    $ RecordBattle("Blue6")

    show screen songsplash("A Rival Appears!", "Zame")
    
    queue music "audio/music/rivalchill_start.ogg" noloop
    queue music "audio/music/rivalchill_loop.ogg"

    show blue og with dis

    blue @happy "Hah... hah hah hah! Hahahaha!"

    red @confused "Are you laughing at me, or...?"

    if (WonBattle("Blue6")):
        $ ValueChange("Blue", 3)

        blue @closedbrow talking2mouth "You won! Even now, even with Eevee, you {i}still{/i} won!"
        blue @talkingmouth "Guess I was worried over nothing. This Eevee isn't some end-all be-all supermon, like I thought. It's just a regular Pokémon that can win or lose like anything else."
        blue @closedbrow talking2mouth "Guess I can talk to Gramps about this after all. As soon as I tell him it lost to your Pikachu, he probably won't give it a second thought."

        redmind @unamusedbrow unamusedmouth "I am... {i}so{/i} confused as to what he wants."

    else:
        blue @talkingmouth "I won. I can't believe it. Is {i}this{/i} what it took? Bruised knuckles, a magic rock, and Gramps to be out of class for a week?"
        blue @closedbrow talking2mouth "I feel like I was just throwing stuff at the board to get that combination, but, hey, at least it worked."

        red @upeyes talking2mouth "You've won before."

        if (not WonBattle("Blue1") or not WonBattle("Blue2") or not WonBattle("Blue3") or not WonBattle("Blue4") or ("Blue5" in battlehistory and not WonBattle("Blue5"))):
            blue @closedbrow talkingmouth "Yeah... but I {i}should{/i} be winning {i}every{/i} time."
        else:
            blue @talkingmouth "Not since Kobukan."

    if (HasEvent("Blue", "ThankMe")):
        blue @wistful lightblush "Oh, yeah. Uh, I'm only saying this because you forced me to, but, uh, thanks."

        $ ValueChange("Blue", 1)

    blue @talkingmouth "Anyway, let's get out of here. Your battle style's so showy, you've probably called the entire Disciplinary Committee on our asses."

    red @upeyes talking2mouth "Sure, blame my Pokémon's moves, and not your constant yelling."

    blue surprisedbrow frownmouth @talkingmouth "Hey, this place is absolutely soundproof! Don't--"

    $ PlaySound("idea.ogg")

    stop music fadeout 1.5

    Character("{color=#493bff}???{/color}") "{size=30}Yip!{/size}"

    red @confused "Huh? Did someone just... {i}bark{/i}?"

    Character("{color=#db4039}???{/color}") "{size=30}Shh! We gotta... ah, crap, I think they heard.{/size}"

    red @confused "It sounds like there's someone else here...? Behind the bleachers, there...?"

    show blue:
        xpos 0.5
        ease 0.5 xzoom -1 xpos 0.75

    blue @angry "Hey! Who's there?"
    
    $ renpy.music.queue("Audio/Music/Littleroot_Start.ogg", channel='music', loop=False, fadein=1.0, tight=None)
    $ renpy.music.queue("Audio/Music/Littleroot_Loop.ogg", channel='music', loop=True, fadein=0.0, tight=None)

    show brendan sadbrow:
        xpos -0.5 xzoom -1
        ease 0.5 xpos 0.5

    show may sadbrow:
        xpos -0.5
        ease 0.5 xpos 0.25

    brendan @happy "Hey, bros! Fancy, uh, fancy seeing you two here. Didn't know you guys were like that. Guess you didn't see the warning, huh?"

    blue @angry "'Like that'? 'Warning'? What the hell are you talking about?"

    may @talkingmouth "Oh, I guess you don't know... it's weird, most people don't know about this place unless they know the full story."

    red @unamusedbrow talking2mouth "I have a terrible feeling I know where this is going."

    blue @talkingmouth "What do you mean, 'this place'? Stop being so damn obtuse and just speak straight!" 

    red @confused "Blue, how did you learn about this place?"

    blue @talkingmouth "Nate told me this was a place where a couple of guys could go at night to make a lot of noise in private!"

    pause 2.0

    brendan @closedbrow talking2mouth "Yup, now I see it."

    may @closedbrow talkingmouth "I get it now."

    red @closedbrow talking2mouth "Hoo boy."

    blue @angry "What?! What is it?! Explain, damn you!"

    may @talkingmouth "Only {i}you{/i} could hear that and immediately think of battling, Blue..."

    blue @scaredbrow furiousmouth "What is it? {i}What am I missing?!{/i}"

    brendan -sadbrow @talking2mouth "Okay, bro, here's the deal. Only Instructor Wallace uses the faculty pool, and he comes here exactly once a week, on Monday nights."
    brendan @talking2mouth "All the rest of the time, students, uh, usually in pairs..."

    may -sadbrow @happy "Sometimes in groups!"

    brendan @talking2mouth "Sometimes in groups, come here to, uh..."

    pause 1.0

    show blue scaredbrow with dis

    brendan @happy "Well, make love."

    pause 1.0

    $ PlaySound("idea.ogg")

    blue -scaredbrow frownmouth @talkingmouth "Oh."

    redmind @happy "And the shoe drops."

    brendan @closedbrow talking2mouth "Yeah, so, that's how it is. People hang their uniform's ties on the handle to the building, to let anyone else know that it's occupied."

    red @closedbrow talkingmouth "I, uh, I didn't see yours."

    blue @wistfulbrow talkingmouth "...I scoped this place out, earlier, and saw two ties hanging on the doors. I thought they were just lost, so I, uh, I put them in lost-and-found."

    brendan @closedbrow talking2mouth "Ah, damn. We'll have to get them back tomorrow, then. Make up some story about how we dropped them..."
    brendan @talking2mouth "Well, it's alright, man, you didn't know."

    pause 1.0

    blue @surprised "Wait, that means Nate was flirting with me."

    red @talking2mouth "He flirts with everyone, dude."

    blue @wistfulbrow talkingmouth "Tch. I knew that."

    brendan @talking2mouth "Anyway, now you know the story of, uh, the faculty pool, so I guess you can tell other people who might be interested."

    may @happy "Since this is a one-year academy, there aren't any seniors to fill us in on this kind of stuff, so we have to learn all these mysteries and traditions on our own!"

    red @confused "...Quick question, though. Where did {i}you{/i} learn this from?"

    if (GetRelationshipRank("May") > 0):
        may @closedbrow talkingmouth "Well... don't tell anyone this, but Brawly, Falkner, and Roxanne often come here, and Brawly told Brendan."

        brendan @talking2mouth "Yeah, we were out running in the fields when he just casually dropped this knowledge bomb on me. But, hey, like May said, don't tell anyone!"

        red @happy "My lips are sealed."

        blue @surprised "Even the former student council...? How deep does this conspiracy run?!"

        may @happy "Don't stress about it."

    else:
        may @happy "Sorry, that's a bit of a secret!"

        red @happy "You tease."

    brendan @talking2mouth "Anyway, if our ties are gone, we probably shouldn't stick around here any longer. Guess we'll be heading out."

    red @talkingmouth "Thanks for the info. I'll keep it in mind."

    show brendan sadbrow with dis
    show may sadbrow with dis
    show blank2:
        alpha 0.0
        linear 10 alpha 1.0

    blue og @closedbrow talking2mouth "Psh. Like {i}you'd{/i} ever be able to bring a girl here."

    red @happy "Who said it has to be a girl?"

    blue @happy "All I'm hearing is that you've got at least {i}two{/i} genders who are going to reject you."

    red @talking2mouth "And all {i}I'm{/i} hearing is that you thought Nate's flirting was him giving you a hot tip on a battle spot, so, really, who's got less game...?"

    narrator "Your bickering continues as you sneak back to the dorm, avoiding campus security and the Disciplinary Committee's patrols."

    pause 1.0

    narrator "You think."

    pause 1.0

label endweek7:

narrator "Meanwhile... not too far away..."

stop music fadeout 1.5

$ renpy.music.queue("Audio/Music/DragonDenStart_B.ogg", channel='music', loop=False, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/DragonDenLoop.ogg", channel='music', loop=True, fadein=0.0, tight=None)

scene draydenoffice 
show anabel angrybrow headset:
    xpos 0.25 xzoom -1
show iris champion angrybrow frownmouth
show drayden angrybrow:
    xpos 0.75
with splitfade

anabel @talkingmouth "Drayden, you're being unreasonable."

drayden "No, Miss Anabel, I am finally behaving as reason dictates."

anabel @talkingmouth "You {i}must{/i} close down the school. The children are in danger."

drayden @sadbrow "There are no children at this school, Miss. Only young men and women."
drayden @closedbrow "If we were to disrupt their learning now, it could be catastrophic for their grades, their futures. That's not even touching on how furious the parents would be."
drayden -angrybrow @surprisedeyebrows "Do you know how much a single hour of tuition at Kobukan costs?"

anabel -angrybrow @talkingmouth "No, but I don't see-"

drayden @closedbrow "Too damn much."

iris -angrybrow @sadbrow talking2mouth "...Bad word."

drayden @sadbrow "I... you're right, I'm sorry. I'll put a coin in the jar."

anabel @talkingmouth "I'm not suggesting you close the school without compensating the students, the parents."
anabel @closedbrow talking2mouth "Just send them a bill for the classes they've taken, then invite them back when we have ensured the school is safe."

drayden @closedbrow "Your work with the International Police has made you forget common ways of life. I cannot simply 'send them a bill'. Many students are relying on the six months before tuition is due to pay it."
drayden @sadbrow "In any case, what you're suggesting... simply wouldn't be allowed by the board."
drayden "They are a flock of vultures, but I happen to agree that, in this case, closing Kobukan would do far more harm than good."

anabel @angrybrow talkingmouth "Why aren't you listening? My agent was {i}attacked!{/i}"

drayden "I am just as concerned about that as you are. He is my student, in addition to your agent. I would not--"

anabel @surprisedbrow talkingmouth "Hm? No, not Black No. 2. I'm referring to the truck driver. The one who was transporting the specimen."

drayden @closedbrow "I find your callous disregard of Nathaniel's plight upsetting."

anabel @closedbrow talkingmouth "{size=30}It's just Nate.{/size} And he's our best agent--he's never been so much as {i}scratched.{/i} But the truck was attacked en-route to the airport, and the specimen inside is still unaccounted for!"
anabel @angry "It {i}will{/i} return to Kobukan. To guarantee everyone's safety, you must send everyone home."

pause 1.0

drayden @closedbrow "It is interesting, this appeal to safety you've brought up. I think perhaps you are not being entirely truthful with your intentions."

anabel @surprised "What?"

drayden @surprisedeyebrows "Well, from a logical standpoint, there is no safer place than Kobukan. The best trainers in the world are here."
drayden @happy "Why, I could shout 'champion', and no less than three people in any given room are liable to look at me."
drayden @surprisedeyebrows "So, pardon my suspicions, but this appeal to safety feels, to me, like an argument you make only because you think it will appeal to me."
drayden @closedbrow "Unnecessary, of course. If you want the school shut down for a different reason, we can talk of what your true reason is."
drayden @sadbrow "Though I am no less reticent to acquiesce to your plea, it must be said."

pause 1.0

anabel @closedbrow talkingmouth "May we speak in private?"

drayden @surprisedeyebrows "So, this performance was for my daughter's benefit, as well? Noted."
drayden @closedbrow "In any case, there is nothing you can tell me that I would not share with my daughter after, so I see no reason for further privacy."

anabel @closedbrow talkingmouth "...Okay. Here's the truth. When AZOTH1 returns, it will almost certainly do so in a {i}very{/i} public fashion." 
anabel @sad "The transport truck was attacked. That's proof enough that there are bad actors who seek the specimen's power. We have eyes on them."
anabel @talkingmouth "We want to hide the existence of AZOTH1 at all costs. I cannot do that in a public, insecure location, such as the middle of this school."

drayden @sadbrow "It appears our philosophies are at odds. I would protect people by educating them as to the threat, and giving them the tools they need to fight it."
drayden @closedbrow "And you, it appears, would protect them by hiding the threat, and handling it in the shadows."

anabel @talkingmouth "Your ideal is noble. It befits an educator. But society stands on the tip of a needle. People need their peace of mind to keep going."

drayden @sadbrow "...So little of you has changed, Anabel. Even when you were a student, you, too, wanted to shoulder the world's burdens."
drayden @closedbrow "Your intermittent relationship with time and space has not changed your heart as much as your body, I see."

pause 1.0

drayden @closedbrow "I may consider an evacuation of the campus for up to two days. But I would have you tell me, and Unova's Champion, what you know, before I agree to anything."

anabel @talkingmouth "That's... {w=0.5}fair."

call clearscreens() from _call_clearscreens_211
scene blank2 with Dissolve(2.0)

$ hideside = True
stop music fadeout 1.5

drayden "Tell us, then. What is it that has the International Police so concerned? What do we have to fear?"

pause 3.0

anabel @talking2mouth "Eternity."

pause 3.0

show threeeyes with Dissolve(1.0):
    xalign 0.55 ypos 0.0 zoom 0.5

pause 3.0

show threemouth with Dissolve(1.0):
    xalign 0.55 ypos 0.0 zoom 0.5

Character("???") "\"{w=0.333}Heh heh heh... {w=0.333}heh heh heh... {w=0.333}heh heh heh!!!\""

scene blank2 with Dissolve(3.33)

$ hideside = False

jump day010524