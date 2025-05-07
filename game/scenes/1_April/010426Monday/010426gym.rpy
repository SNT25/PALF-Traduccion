label gym010426:

play music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

$ renpy.transition(dissolve)
show screen currentdate

scene gym with dis

show blank2 behind gym

$ renpy.pause(2.0, hard=True)

hide blank2

show alder spunky2 with dis:
    xpos 0.66

show bruno think with dis:
    xpos 0.33

alder norm @spunky2 "And that pretty much finishes it!"
alder @norm2 "This week's unit will be continuing our double battle lessons. I think, {i}next week{/i}, maybe, we'll switch to Triple Battles."

bruno @norm2 "Mm. Alder, next week is the Quarter Qlashes."

alder @surprised2 "Oh, yeah. Wow, is it that time of year already? I swear, they seem to come earlier and earlier every year."

pause 1.0

alder @norm2 "Alright. Next week, we'll shift our classes' focus to whatever format the Quarter Qlashes are in."

rosa uniform @surprised "Oh, even a Champion doesn't know, yet?"

alder @happy2 "Nope! We'll know next Monday, though. You've got a couple days to prepare, then the battles are held from Wednesday through Friday."

leaf uniform @talking2mouth "One on each day?"

alder @norm2 "Well, assuming you get through the first two rounds, yes."

bruno -think @think2 "This year, the Quarter Qlashes for the greater Inspira area will be held in our own Battle Hall. This is a great honor."

redmind uniform @thinking "Makes sense. There probably aren't a whole lot of arenas in this area that can fit the number of battles that'll go into the first round of the Quarter Qlashes."

alder @norm2 "Now, time for the battles."

pause 1.0

alder @norm4 "Bruno?"

bruno @norm2 "Your partner, [first_name] [last_name], will be Sabrina."

hide alder
hide bruno 
with dis

pause 1.0

show sabrina uniform
with dis

pause 1.0

red uniform @talkingmouth "Oh, Sabrina! Hi! Somehow, I never noticed you in this class."

pause 1.0

show sabrina:
    xpos 0.5
    block:
        ease 0.02 xpos 0.49
        ease 0.02 xpos 0.5
        ease 0.02 xpos 0.51
        ease 0.02 xpos 0.5
        repeat 5

sabrina sadbrow "...Nngh."

pause 1.0

red @confused "What's wrong?"

show sabrina:
    xpos 0.5
    block:
        ease 0.01 xpos 0.49
        ease 0.01 xpos 0.5
        ease 0.01 xpos 0.51
        ease 0.01 xpos 0.5
        repeat 5

sabrina @talking2mouth "It's... it's so loud..."
sabrina @sadmouth "My... head hurts."

red @sadbrow talking2mouth "Wh-- well, we gotta help you! Uh, you need to get out of here, right?"

show sabrina:
    xpos 0.5
    block:
        ease 0.01 xpos 0.49
        ease 0.01 xpos 0.5
        ease 0.01 xpos 0.51
        ease 0.01 xpos 0.5
        repeat 10

sabrina @talking2mouth "N-no. No, that's not... {cps=20}I need to learn to... {cps=10}endure..."

if (GetRelationship("Sabrina") == "Friend"):
    red @angrybrow talking2mouth "Sabrina, that's {i}enough.{/i} I'm your friend. I'm not going to let you hurt yourself."

    pause 1.0

    show sabrina uniformpowered poweredbrow with dis:
        ypos 1.0
        ease 2.0 ypos 0.8
        parallel:
            ease 2.0 ypos 0.85
            ease 2.0 ypos 0.8
            repeat

        parallel:
            ease 2.0 xpos 0.52
            ease 2.0 xpos 0.5
            ease 2.0 xpos 0.48
            ease 2.0 xpos 0.5
            repeat

    redmind @surprised "{color=#600080}...That's not your choice.{/color}"

    pause 1.0

    show sabrina:
        ease 1.0 ypos 0.8 xpos 0.5
        parallel:
            ease 2.0 zoom 0.8
        parallel:
            ease 2.0 ypos 0.7
        pause 0.6
        parallel:
            ease 0.3 zoom 3.0
        parallel:
            ease 0.3 ypos 2.0
        parallel:
            pause 0.2
            ease 0.1 alpha 0.0

else:
    red sad "Are you... are you sure? Can you really battle like this?"

    sabrina @closedbrow talking2mouth "It's not about whether I 'can.' It's about whether I 'have to.'"

    pause 1.0

    sabrina @talking2mouth "I do. Forever and always."

    show sabrina:
        xpos 0.5
        block:
            ease 0.01 xpos 0.49
            ease 0.01 xpos 0.5
            ease 0.01 xpos 0.51
            ease 0.01 xpos 0.5
            repeat 10

    sabrina @closedbrow talkingmouth "Nngh."
    
    sabrina @talking2mouth "Let's do this quickly."

$ HealParty()
$ trainer1 = MakeRed(number=2)
$ trainer2 = MakeTrainer("Sabrina", number=2)

call Battle([trainer1, trainer2], uniforms=[True, False], customexpressions=["red surprised", "red angrybrow frownmouth", "sabrina uniformpowered poweredbrow", "sabrina uniformpowered poweredbrow talking2mouth"]) from _call_Battle_63
$ battlehistory["Sabrina1"]  = _return

$ HealParty()

stop music fadeout 1.0

hide alder
hide bruno

pause 1.0

show alder norm3 at leftside with dis
show sabrina uniformpowered poweredbrow with dis:
        ypos 0.8 xpos 0.5
        parallel:
            ease 2.0 ypos 0.85
            ease 2.0 ypos 0.8
            repeat

        parallel:
            ease 2.0 xpos 0.52
            ease 2.0 xpos 0.5
            ease 2.0 xpos 0.48
            ease 2.0 xpos 0.5
            repeat
show bruno surprisedbrow frownmouth at rightside with dis

queue music "audio/music/tension_start.ogg" noloop fadein 1.5
queue music "audio/music/tension_loop.ogg"
    
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

hide blank2

sabrina @talking2mouth "Nngh... nngh..."

alder @norm4 "Sabrina, listen carefully. I've seen something like this before, with a very powerful trainer from Unova's Elite Four. Even she couldn't stem the headaches." 
alder @angry2 "You're not in trouble, but you {i}need{/i} to remove yourself from this room."

sabrina @talking2mouth "Nn... no... I've... {cps=5}{i}endured{/i}{/cps} three weeks... I can do {i}one{/i} more! It's almost the end of class, isn't it...?"

bruno -surprisedbrow -frownmouth -surprised @norm2 "Sabrina, we are not asking. I sympathize, but you {i}must{/i} leave. You are hurting yourself. Injury does not build tolerance."

redmind "{color=#600080}N-no... all the faces... staring, watching... they...{/color}"
redmind "{color=#600080}I need to hide... I can't think about the secrets... Keep them safe, hide them... {/color}"

bruno @surprised "Telepathic speech?"

alder @norm4 "Caitlin would do that when the headaches got especially bad. Her thoughts started to broadcast."

alder @sad2 "Ugh... Bruno, be prepared to take Miss Sabrina to the infirmary."

show sabrina uniformpowered poweredbrow with dis:
        ypos 0.8 xpos 0.5
        parallel:
            ease 1.0 ypos 0.85
            ease 1.0 ypos 0.8
            repeat

        parallel:
            ease 1.0 xpos 0.52
            ease 1.0 xpos 0.5
            ease 1.0 xpos 0.48
            ease 1.0 xpos 0.5
            repeat

sabrina @talking2mouth "N-no! I don't need that! Just... go back to the lesson, please! We're almost done-- I-- I almost made it... I can--"

pause 1.0

show alder sad
show bruno sad
with dis

pause 1.0

show alder:
    ease 0.5 xpos 0.15

alder @sad2 "Now, Bruno."

bruno norm @norm2 "{i}Hai.{/i}"

show bruno:
    xpos 0.75
    ease 0.5 xpos 0.85
    pause 0.3
    ease 0.3 xpos 0.55

pause 0.9

show alder surprisedbrow frownmouth with dis
show bruno surprisedbrow frownmouth with dis:
    ease 0.3 xpos 0.85

show will happy behind sabrina:
    xpos 1.1
    ease 0.7 xpos 0.6

show sabrina -uniformpowered uniform closedbrow with dis:
    ease 2.0 xpos 0.4 ypos 1.0

stop music fadeout 1.0
queue music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

pause 0.5

will -happy @happy "Well, now, did someone call for the Great Will?!"

pause 1.0

sabrina @talking2mouth "...Instructor."

$ BecomeNamed("Instructor Will")

show will:
    ease 0.5 xpos 0.5 ypos 1.1

will frownmouth @sadbrow talking2mouth "Bri. What did I tell you about overdoing it?"

pause 1.0

sabrina -closedbrow @talking2mouth "...Not to."

show will:
    ease 0.5 xpos 0.6 ypos 1.0

will -frownmouth @happy "Brilliant! This is why she's my star pupil, ladies and gentlemen."

show alder norm3
show bruno norm 
with dis

alder @norm4 "Will. How did you get Sabrina to calm down?"

will @surprised "Oh? I didn't do anything!"

will @happy "No, my friends, the power was in {i}her{/i} all along. I simply provided myself as a comforting and familiar face."

bruno @surprised2 "...Your face is mostly hidden."

will @happy "So behold the world's most comforting chin!"

sabrina @closedbrow happymouth "Hmhm."

will @angrybrow talking2mouth "Now, what are we all doing standing around for? Shouldn't we be headed to lunch?" 
will @angrybrow angrymouth "You can't keep these fine young men and women locked up in your stuffy gym class forever, you two!"

alder @norm4 "...I mean. We need to wait for the bell first, so..."

will @surprised "Hold! The Great Will will now make a prediction!"

will @closedbrow talking2mouth "He predicts that the bell will ring...{w=1.0}{nw}"
$ PlaySound("BellChime.ogg")
extend @happy " now!"

pause 1.0

redmind uniform @confusedeyebrows frownmouth "That'd be impressive if he hadn't just looked at his watch."

will @surprised "Oh? In this crowd, I sense... a doubter! A {i}doubter{/i} of the Great Will!"

sabrina @sadbrow talking2mouth "Ah... no, Instructor, please don't..."

show sabrina behind will
show bruno behind will

show will:
    xpos 0.6
    ease 0.5 zoom 1.3 ypos 1.2

will @angry "You! You doubt my abilities!"

if (HasEvent("Instructor Will", 1)):
    red @confused "Um... no, Instructor Will. I've taken your class before."

    if (HasEvent("Instructor Will", 2.1)):
        red @closedbrow talking2mouth "Like, more than once."

    will @talking2mouth "{size=30}I know, [first_name], just go along with it.{/size}"

elif (GetRelationship("Sabrina") == "Friend"):
    red @confused "Not really? I mean, I'm Sabrina's friend, so--"

    will @surprised "Oh, {i}you're{/i} [first_name] [last_name]!"
    will @talking2mouth "{size=30}Okay, just go along with it.{/size}"

else:
    red @closedbrow talking2mouth "Um... Not really? I just kinda--"
    
    will @talking2mouth "{size=30}I know, [first_name], just go along with it.{/size}"

red @surprised "Uh... okay. Yup, I'm a doubter."

will @angry "I knew it! And this doubter requires correction! Come with me, and you too, Sabrina! You two clearly need direct tutoring from The Great Will!"

sabrina @closedbrow talking2mouth "Yes."

red @confused "...Okay."

hide alder
hide bruno
hide will
with dis

if (WonBattle("Sabrina1")):
    pause 1.0

    sabrina @talking2mouth "You... thank you. When you beat me, if only for a moment, I had a moment of control. I could lose myself in the battle."

    $ ValueChange("Sabrina", 3, 0.4)

    sabrina @closedbrow talking2mouth "I... wish it would happen again."

    show will at rightside with dis
        
    will @happy "Come along now, students! My tutelage doesn't often come this freely!"

show blank2 with dis

stop music fadeout 1.5

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_74

$ renpy.pause(2.0, hard=True)

scene blank2
    
show afternoon at vspaz
    
pause 3.5

$ timeOfDay = "Afternoon"

show academyhall_zoom behind blank2

queue music "audio/music/lavender_start.ogg" noloop
queue music "audio/music/lavender_loop.ogg"

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade
$ renpy.pause(0.5, hard=True)

hide afternoon

show will sadbrow frownmouth at rightside
show sabrina uniform at leftside
with dis

pause 1.0

will @talking2mouth "Bri. Are you alright?"

sabrina @talking2mouth "Yes, Instructor."

will @talkingmouth "...Hm."

will -sadbrow @talking2mouth "My ESP isn't nearly as strong as yours, disciple. If your thoughts differ from your words, you'll need to tell me."

pause 1.0

sabrina sadbrow @sadmouth "...Yes, Instructor."

pause 1.0

red uniform @talking2mouth "Instructor, why am {i}I{/i} here?"

will -frownmouth @surprisedbrow talking2mouth "Oh! Right."
will @happy "I just wanted to make sure you were alright. After hearing my disciple's distress, I immediately dashed to the rescue, of course, not just of her, but of her opponent."

sabrina @sad "Instructor..."

will @surprised "You see, Bri here is a tremendously powerful Esper, the pride of the Greater Inspira Esper community."

redmind "{color=#600080}That's three people.{/color}"

will @happy "It's fair to say her headaches can be quite a headache for other people!"

sabrina @sad "Instructor, please, let me explain."

will @surprised "Oh? Of course, be my guest."

pause 1.0

sabrina @closedbrow talking2mouth "When my headaches get especially bad, I... my telepathy inverts. And other people hear my thoughts."

red @surprised "Oh."

sabrina @sad "So. I... you know, I need to be careful of what I'm thinking. To ensure I don't reveal any secrets."

pause 1.0

show sabrina -sadbrow with dis

sabrina @sad "I understand this makes it hard to trust me."

red @closedbrow talking2mouth "...Have you ever spilled a secret like that before?"

sabrina @talking2mouth "...Yes. A friend's."

if (GetRelationship("Sabrina") == "Friend"):
    red @sad "Is that the friend you told me about before? The one who, uh... left you?"

    sabrina @sad "No. I have had... a handful of friends who have discarded their bonds with me after my powers became an inconvenience. This was but another."

will @talkingmouth "But it sounds like no secrets were spilled this time, so I suppose we can say all's well that ends well!"

pause 1.0

show will surprisedbrow frownmouth with dis

red @surprised "Wait. Instructor Will, if you came here to make sure that my secret wasn't shared, then... you know I have a secret?"

pause 1.0

will -surprisedbrow -frownmouth -surprised @happy "Well, I didn't until now!"

pause 1.0

red @closedbrow talking2mouth sweat "Oops."

will @happy "Think nothing of it, dear student. {i}Everyone{/i} has secrets. In my inestimable opinion, if there was one woman in this school who can be trusted with them all, it's dear Bri."

menu:
    ">Emphasize the importance of keeping your secret":
        $ ValueChange("Sabrina", -1, 0.25)

        pause 1.0

        sabrina @talking2mouth "Yes. I know. I will never willingly share your, or anyone else's, secrets."

    ">Stay silent":
        show sabrina happymouth with dis

        $ ValueChange("Sabrina", 2, 0.25)

        pause 1.0

        red @happy "What're you smiling for?"

        sabrina -happymouth @talking2mouth "You... elected not to remind me of the obvious. I appreciate that."

        if (GetRelationship("Sabrina") == "Friend"):
            red @happy "Like I said, Sabrina. Sometimes people have intrusive thoughts. Whether they {i}act{/i} on 'em is the mark of a good person."

pause 1.0

will @happy "Now, let's get you to the infirmary, Bri. You could do with a nap and some medicine."

sabrina @talking2mouth "Instructor? I don't need that. I'm fine."

will @surprisedbrow poutmouth "Isn't that for the nurse to decide?"

sabrina @closedbrow talkingmouth "I... {w=0.5}yes, I suppose."

redmind @thinking "Hm. If the infirmary's here, then..."

show jasmine uniform behind will:
    xpos -0.1
    ease 1.0 xpos 0.6

show grusha uniform behind will:
    xpos -0.1
    ease 1.0 xpos 0.4

show sabrina:
    ease 0.5 xpos 0.2

show will:
    ease 0.5 xpos 0.8

jasmine @talkingmouth "Oh, excuse us."

redmind @surprisedeyebrows frownmouth "Hm. Tall, skinny, that's Jasmine, I bet."

$ BecomeNamed("Jasmine")
$ BecomeNamed("Grusha")

redmind "{color=#600080}It is. The one accompanying her is Grusha.{/color}"

show jasmine uniform:
    xpos 0.6
    ease 1.0 xpos 1.1

show grusha uniform:
    xpos 0.4
    ease 1.0 xpos 1.1

redmind @thinking "Cool, thanks."

show sabrina happymouth with dis

redmind "{color=#600080}You are welcome.{/color}"

pause 1.0

will sadbrow poutmouth @sad "Are you two having a conversation without me?"

show sabrina sad with dis

red @surprised "Oh, uh, just a very short one! Not about anything important, honest! I just need to catch up to those people who ran out of the infirmary, and I was wondering who they were, so Sabrina told me, and--"

stop music fadeout 2.0

hide sabrina
hide will
with Dissolve(2.0)

pause 1.0

show mace at leftside
show face uniform at rightside
with dis

mace @talkingmouth "Hm."

face @talkingmouth "Yes, that's interesting. I think Cheren might want to know about this."

pause 1.0

mace @closedbrow talkingmouth "No, not yet. Cheren's too softhearted. He'd never approve of what we'd have to do to get this information."

face @surprised "Then...? We just go for it?"

mace @angrybrow happymouth "Oh, I think we can figure something out. It's just a matter of timing, really."

show blank2 with dis

stop music fadeout 1.5

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_75

$ renpy.pause(2.0, hard=True)

scene blank2
    
show afternoon at vspaz
    
pause 3.5

$ timeOfDay = "Afternoon"

show cafe behind blank2

queue music "Audio/Music/Route 1 Anime.ogg"

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade
$ renpy.pause(0.5, hard=True)

show grusha uniform at leftside:
    zoom 0.8 ypos 0.9
show jasmine uniform at rightside:
    zoom 0.8 ypos 0.9
with dis

pause 2.0

narrator "You walk into the cafeteria, in hot pursuit of Jasmine and Grusha."

redmind uniform "Hm. Jasmine sure walks fast for someone who spends a lot of time in the infirmary."

show grusha surprisedbrow frownmouth at leftside with dis:
    ease 0.5 zoom 1.0 ypos 1.0

show jasmine surprisedbrow frownmouth at rightside with dis:
    ease 0.5 zoom 1.0 ypos 1.0

red @happy "Hey there! My name's [first_name]. You two are... Jasmine and Grusha, right?"

show grusha -surprisedbrow -frownmouth -surprised with dis

jasmine -surprisedbrow -frownmouth -surprised @happy "Oh, {i}you're{/i} [first_name]! Lovely. {i}Lovely.{/i} Calem's told me all about you. I've wanted ever so badly to meet you, but I'm afraid my engagement with the infirmary kept me occupied."

red @sadbrow talking2mouth "Right, I heard about that. Um, I'm sorry for what you're going through. I don't know what it is, exactly, but..."

jasmine @sweat closedbrow talkingmouth "Well, I'm doing better for now, and that's most of what I can hope for."

pause 1.0

red @talkingmouth "And you... you {i}are{/i} Grusha, right?"

grusha @talkingmouth "Yeah. 'The Sub-zero Shredder.' From Montenevera, in North Paldea.{w=0.5}{nw}" 
extend @sadbrow talking2mouth " ...Glaseado Mountain, actually, but the post came to Montenevera."

pause 1.0

grusha @closedbrow talking2mouth "So. You're the one with the trash campaign. That's cool."

$ ValueChange("Grusha", 1, 0.25)

red @talkingmouth "I don't think I've seen you two around before."

grusha @closedbrow talkingmouth "We keep to ourselves."

jasmine @talking2mouth "We spend quite a bit of time in the infirmary, I'm afraid. Depending on how often you take the Steel or Ground electives for me, or the Ice and Flying electives for Grusha, we might just have never met each other."
jasmine @sadbrow talkingmouth "But I don't think I'll need to today."
jasmine @happy "It's a good day, today."

grusha @happymouth "Yeah."

pause 1.0

grusha @confusedeyebrows talkingmouth "So, why're you looking for us? Some Student Council business?"

red @talkingmouth "Yeah. Calem wants to put together a meeting of all the Student Council hopefuls tomorrow morning."

grusha @sad "Sounds like a waste of time. The voters are apathetic. Anyone with a pulse will get voted in. It's not like we're competing against each other."

jasmine @talkingmouth "Well, this sounds like an excellent opportunity to reinvigorate the voting population, no?"

red @talkingmouth "Yeah, that's one of the things I wanted to talk about. I think I know how we could get people to vote. We just need to get them excited about our positions."

grusha @closedbrow talking2mouth "True. Cheren would've had more luck if he hadn't started his campaign so early. At this point, everyone's bored of hearing from him."

jasmine @talkingmouth "Let's not speak ill of him, Grusha."

grusha @closedbrow talkingmouth "Meh."

jasmine @talkingmouth "In any case, we can definitely make it to the meeting tomorrow morning."

red @happy "Great! Mind if I ask a quick question before I go, though?"

jasmine @talkingmouth "Please."

red @closedbrow talking2mouth "What are you two running on? What are your positions?"

jasmine @talkingmouth "Oh. Well, I suffer from a somewhat common type of recurrent fatigue."
jasmine @sadbrow talking2mouth "I spent much of my childhood being shuttled between various schools that were ill-equipped to give me the extra inch I needed in order to flourish."
jasmine @closedbrow talking2mouth "When I arrived at Kobukan, I expected it to be much of the same. I imagined a school as old as this one would not budge, not even an inch, to accomodate its disadvantaged students."
jasmine @happy "However! Dean Drayden, I have found, is {i}most{/i} amenable to my position. We have managed to work out an alternate schedule that accomodates my issues quite well."
jasmine @angrybrow talkingmouth "So my desire is to have the advantages I've been given be given freely to others, and enshrined as protocol, instead of exception."
jasmine @happy "It only seems fair."

red @sadbrow talkingmouth "Wow."
red @happy "That's {i}really{/i} admirable, Jasmine. I'm impressed."

jasmine @talkingmouth "Why, thank you. I just hope I can give back. Education is the right of all who want to learn. I'm a massive accessibility advocate."

pause 1.0

red @talkingmouth "And what about you, Grusha?"

pause 1.0

grusha @closedbrow talking2mouth "Yeah, same as her."

jasmine @sadbrow poutmouth "Grusha..."

grusha @talkingmouth "You should sit down, Jasmine. I'll get us some food."

hide grusha with dis

pause 1.0

jasmine @sadbrow talkingmouth "Please excuse Grusha. It takes him a while to warm up to people."

red @closedbrow talking2mouth "Of course. I won't take it personally."

$ ValueChange("Jasmine", 3, 0.75)

jasmine @talkingmouth "It's been a pleasure to meet you, [first_name]. I look forward to our meeting tomorrow."

hide jasmine with dis

narrator "You have met Jasmine and Grusha! [bluecolor]They will begin showing up in elective classes, at lunch tables, and after school fifty percent of the time.{/color}"
narrator "[bluecolor]Though they are not always available, hanging out with them will reward double the amount of social points you would earn with another character.{/color}"

pause 1.0

$ jumpto = "lunch"
$ jumptoyear = "01"
$ jumptomonth = ("0" if calDate.month < 10 else "") + str(calDate.month)
$ jumptodate = ("0" if calDate.day < 10 else "") + str(calDate.day)
$ renpy.jump(jumpto + jumptoyear + jumptomonth + jumptodate)