label day010510:

stop music fadeout 1.5

call calendar(1) from _call_calendar_35
$ calDate = calDate.replace(day=10, month=5, year=2004)

$ timeOfDay = "Morning"

$ PlaySound("Alarm.ogg")
$ renpy.pause(4.0, hard=True)

redmind @swimsuithatless closedeyes frownmouth "Ughh..."

$ renpy.music.play("Audio/Morning_ambience.ogg", channel='crowd', loop=True, fadein=1.0)

scene dorm_A with transeye2

pause 1.0

redmind @swimsuithatless closedbrow frownmouth "Wait..."

scene blank2 with transeye

pause 1.0

scene bedroom with transeye2

redmind @swimsuithatless sadeyebrows "Right... that's right. This is the new normal, now."

pause 2.0

$ renpy.transition(dissolve)
show screen currentdate

red uniform @happy "Hey, ready, bud?"

$ renpy.music.play("Audio/Pokemon/pikachu_happy2.ogg", channel="altcry", loop=None)
libpikachu happy "Pika!"

red @talkingmouth "Great. Let's get some coffee first, okay?"

stop music fadeout 1.5 channel "crowd"

$ renpy.music.queue("Audio/Music/Pallet Town A.ogg", channel='music', loop=True, fadein=1.0, tight=None)

scene kitchen 
show blue closedbrow uniform frownmouth at leftside
show yellow uniformhat at rightside
with splitfade

yellow @talkingmouth "{size=15}don't{/size} {size=20}mind{/size}. {size=25}We{/size} {size=30}could{/size} do with some more, anyway, since you... um..."
yellow @sadbrow talkingmouth "Since you scared your other dormmates off."

blue @talkingmouth "Yeah, but no way they'd go for it."

yellow @surprisedbrow frownmouth ".{w=0.5}.{w=0.5}.{w=0.5}"
yellow @surprisedbrow talkingmouth "Blue, you're the one who suggested it."

blue -closedbrow @surprisedbrow talkingmouth "Huh? Yeah, I know {i}that!{/i} I'm just..."

pause 1.0

show blue:
    ease 0.5 xpos 0.5 ypos 1.2 zoom 1.3

blue @angrybrow talkingmouth "What do {i}you{/i} want?"

red uniform @happy "Cup of Joe. You got any to share?"

blue frownmouth angrybrow @talkingmouth "Tch. You know where the coffee maker is."

show blue:
    ease 0.5 xpos 0.25 ypos 1.0 zoom 1.0

show yellow:
    ease 0.5 xpos 0.66
    ease 0.3 ypos 1.1
    ease 0.3 ypos 1.0
    ease 0.3 ypos 1.1
    ease 0.3 ypos 1.0
    ease 0.8 xpos 0.75

narrator "As you pour yourself a cup of coffee, offering some to Yellow, you notice Blue is staring at you. ...In a way that is different to how he normally does, anyway."

pause 1.0

red @talkingmouth "{w=0.5}.{w=0.5}.{w=0.5}.{i}Sip.{/i}"

pause 1.0

red @talkingmouth "I'll be here all week. You can spread your staring out a bit."

pause 1.0

blue @talkingmouth "{i}What{/i} is your Pikachu?"

red @sadbrow talkingmouth "I... don't know. He's just [pika_name]. My buddy."

pause 1.0

show blue:
    ease 0.5 xpos 0.33 ypos 1.2 zoom 1.3

blue @closedbrow talkingmouth "Can I touch him?"

red @surprised "Huh?"

$ cantouch = True

menu:
    "No way. Hands off.":
        show blue:
            ease 0.5 xpos 0.33 ypos 1.0 zoom 1.0

        $ cantouch = False
        $ ValueChange("Blue", -1, 0.33)

        blue @angry "You always have to make things difficult, don't you? {i}Fine.{/i}"

    "Are you okay with this, [pika_name]?":
        $ renpy.music.play("Audio/Pokemon/pikachu_question.ogg", channel="altcry", loop=None)
        libpikachu confusedeyes talkingmouth "Pika...?"

        pause 0.5 

        narrator "[pika_name] seems confused, but nods after a moment."

        red @talkingmouth "Go ahead."

        $ ValueChange("Blue", 2, 0.33)

    "Go ahead.":
        $ ValueChange("Blue", 1, 0.33)

if (cantouch):
    narrator "Blue rubs his hands carefully around [pika_name]'s cheeks and neck, before feeling his tail. [pika_name] seems bewildered by the physical attention."
    
    show blue:
        ease 0.5 xpos 0.33 ypos 1.0 zoom 1.0

red @confusedeyebrows talkingmouth "What's this about? Just in a huggy mood?"

blue @closedbrow talkingmouth "No. I'm trying to figure out how this thing works."

red @sadeyebrows talkingmouth "If you figure it out, let me know."

blue @closedbrow talkingmouth "I have no idea. Yellow?"

show yellow:
    ease 0.3 xpos 0.66 ypos 1.2 zoom 1.3

yellow @surprised "Y-yes?"

blue @talkingmouth "Do you know how [pika_name]'s new form works? I know a {i}lot{/i} about Pikachu, but I've never seen or heard anything about a Pikachu like this."
blue @closedbrow talkingmouth "I don't even know how it changed form mid-battle like that..."

red @confused "You know a lot about Pikachu?"

blue @happy "Obviously. You were the trainer I fought most often in Pallet Town. I learned everything I could about your Pokémon."

show yellow:
    xpos 0.66 ypos 1.2 zoom 1.3
    pause 0.5
    ease 0.5 xpos 0.66 ypos 1.0 zoom 1.0

yellow @closedbrow talkingmouth "I'm... I'm sorry, I don't. But maybe there's another way we could find out?"

blue @surprised "Yeah?"

pause 1.0

yellow @sadbrow happymouth "We could ask [first_name]?"

pause 1.0

show yellow happy with dis

blue @talkingmouth "...Well, yeah, obviously, I was going to try that {i}eventually.{/i}"

redmind @closedbrow sweat "Sure he was."

red @sweat closedbrow happymouth "Alright, Blue, here's how it works..."

scene blank2 with Dissolve(1.0)

narrator "You explain everything Sam and Sonia told you about [pika_name]'s newfound abilities."

narrator "Blue listens intently, though he doesn't seem happy."

scene kitchen 
show blue closedbrow uniform frownmouth:
    xpos 0.33
show yellow surprisedbrow frownmouth uniformhat:
    xpos 0.66
with Dissolve(1.0)

red uniform @happy "...and that's pretty much what happened. So I've gotta be on the lookout for any more kidney stones he hucks up."

red @closedbrow talking2mouth "I think they have something to do with people I've been hanging out with recently, weirdly enough."

blue @talkingmouth "Is there one for me?"

red @surprised "Huh?"

blue @talkingmouth "These gems. Is there one that you think [pika_name] threw up because I was around?"

if ("Eevee Everal" in claimedforeverals or "Charmander Everal" in claimedforeverals or "Bagon Everal" in claimedforeverals):
    red @happy "Yeah. I think so. Three of them, I think."

else:
    red @talkingmouth "No, I don't think so."

blue @talkingmouth "Hmph. I bet mine are the most powerful out of everyone's."

show yellow -surprisedbrow -frownmouth -surprised with dis

red @sweat closedeyes sadeyebrows happymouth "Of course you do."

pause 1.0

blue -closedbrow -frownmouth @talkingmouth "I want to battle. Your new [pika_name] against my team."

red @talkingmouth "Wait... {i}just{/i} [pika_name]? Against your whole team?"

blue @talkingmouth "Yeah. Chicken?"

red @talkingmouth "I mean... the odds are {i}very{/i} against me there, aren't they?"

blue @closedbrow talkingmouth "I was talking with Leaf. Every time I've battled you this year, the odds were against me. You had some kind of advantage. Now, once again, you've got an advantage. This freakin'... chimerachu that Gramps made."

$ renpy.music.play("Audio/Pokemon/pikachu_angry1.ogg", channel="altcry", loop=None)
libpikachu angryeyes frownmouth "Pika!"

blue @talkingmouth "This'll be like that battle when I brought out my Pidgeotto. Except this time I'll have the greater numbers, and you'll have the single, overpowered, Pokémon."

red @sad2eyes unamusedeyebrows talking2mouth "Right, and what will {i}this{/i} battle be for? To finally prove, ultimately, truthfully, definitely, beyond a shadow of a doubt, who the better trainer is?"

blue @closedbrow talkingmouth "Hah. No way! We can't do that like this. Are you crazy?"

red @surprised "What?"

yellow @happy "Well... if you battle like that, your teams are totally unbalanced, right?"
yellow @talkingmouth "I think the only way you could have a fair fight is if you both used your full teams {i}and{/i} one of those team members was a special Pokémon, like [pika_name]."

red @talkingmouth "...Ah."

red @sweat happy "I'll keep an eye out for any other special Pikachu. You can have the next one."

blue @talkingmouth "Please. I don't need some new \"special\" Pokémon to beat you. My entire team's special. Because they're {i}mine.{/i} And that means they're a match for any special Pokémon, no matter {i}what{/i} dead politician or general or whatever owned it."

pause 1.0

blue @angry "Well? I want to battle! Are you seriously going to turn me down {i}now{/i}? C'mon, we can do it after school, in the Battle Hall!"

menu:
    ">Agree to battle":
        $ ValueChange("Blue", 3, 0.33)

        $ AddEvent("Blue", "SingleBattle")

        blue angrybrow happymouth "Hah. This'll be a stomp! I don't even need to pull any tricks, this time--you just {i}let{/i} me win!"

        hide blue with dis

        pause 0.5

        show yellow:
            ease 0.5 xpos 0.5 

        yellow @talkingmouth "Thank you. That means a lot to him."

        red @happy "It's not a problem. Will you come watch?"

        yellow @surprised "Hm?"
        yellow @talkingmouth "Oh, well... sure. Yes, I'll do that."

        red @happy "Cool. Seeya then."

    ">Say you'll battle if you can use your full team":
        $ bluebattle = "Team"

        $ AddEvent("Blue", "TeamBattle")

        show blue angrybrow frownmouth with dis

        pause 1.0

        $ ValueChange("Blue", -1, 0.33)

        blue angrybrow talkingmouth "Fine."

        blue @closedbrow talkingmouth "{i}Fine.{/i} Will you at least use [pika_name] in the battle?"

        red @unamusedeyebrows talkingmouth "No promises."

        blue @angry "Hah! I don't {i}need{/i} your promises. I'll defeat every single one of your other Pokémon, so you {i}have{/i} to use him!"

        hide blue with dis

        pause 0.5

        show yellow:
            ease 0.5 xpos 0.5 

        pause 0.5

        yellow @sadbrow talkingmouth "It might be hard to tell, but... Blue's trying very hard."

        red @sadbrow talking2mouth "That'd mean more if it was coming from him."

        yellow @closedbrow talkingmouth "Well... we're not there {i}just{/i} yet. Give me some more time."

        hide yellow with dis

        pause 0.5

        redmind @confusedeyebrows frownmouth "I really need to ask what that's about at some point."

    ">Refuse to battle":
        $ bluebattle = "No"

        $ AddEvent("Blue", "NoBattle")

        show yellow sad 
        show blue angrybrow frownmouth 
        with dis

        pause 1.0

        $ ValueChange("Blue", -3, 0.33)

        blue @talkingmouth "Chicken."

        hide blue with dis

        pause 0.5

        show yellow:
            ease 0.5 xpos 0.5 

        pause 0.5

        yellow @sadbrow talkingmouth "It might be hard to tell, but... Blue's trying very hard."

        red @sadbrow talking2mouth "That'd mean more if it was coming from him."

        yellow @closedbrow talkingmouth "Well... we're not there {i}just{/i} yet. Give me some more time."

        hide yellow with dis

        pause 0.5

        redmind @confusedeyebrows frownmouth "I really need to ask what that's about at some point."

call clearscreens from _call_clearscreens_130
scene blank2 with splitfade

scene suite 
show screen currentdate
show ethan uniform
with splitfade

pause 0.5

red uniform @happy "Morning!"

ethan @talkingmouth "Hey, man. How's the coffee?"

red @talkingmouth "I'm pretty sure it's burning a hole in my tongue. Leaf told me on Friday she hated me when I said I preferred running in the morning to drinking coffee, so I thought I'd try it."
red @closedbrow talking2mouth "Maybe this stuff is just much stronger than I'm used to, but I think I'll take the hate."

ethan @talking2mouth "I probably should've grabbed some."

red @talkingmouth "Yeah?"

ethan @closedbrow talking2mouth "I meant to talk to you this morning. Set my alarm and everything. But when it went off, I just turned it off and got back into bed."

red @happy "Oof. Been there. Wanna talk during lunch?"

ethan @talkingmouth "Nah, let's just punt it to tomorrow."

pause 1.0

red @sadeyebrows talkingmouth "You know, just 'cause something goes wrong in the morning, that doesn't mean the whole day's a wash."

ethan @sad2eyes talking2mouth "Eh. There wasn't any hurry for this. Tomorrow morning, man."
ethan @happy "Promise."

menu:
    "No, let's talk now.":
        show ethan angryeyebrows frownmouth with dis

        $ AddEvent("Ethan", "TalkNow")
        
        ethan @talking2mouth "...No."

        $ ValueChange("Ethan", -1, 0.5)

        ethan @closedbrow talkingmouth "I get what you're trying to do. Appreciate it, or whatever. But we'll talk tomorrow. That's {i}my{/i} decision."

        pause 0.5

        red @closedbrow talking2mouth "Right. Sorry."

        hide ethan with dis

    "Alright. Talk to you later, then.":
        $ ValueChange("Ethan", 1, 0.5)
        
        $ AddEvent("Ethan", "TalkLater")

        ethan @happy "Seeya!"

        hide ethan with dis

pause 0.5

redmind "Alright. Time to go to class, then."

pause 0.5

red @closedbrow talking2mouth "Where's Leaf...?"

pause 1.0

red closedbrow frownmouth @sweat "Oh... man. I'm nervous. I know I shouldn't be... I gave a big speech in front of a bunch of people, and that was way more terrifying than just going back to class..."

$ PlaySound("pokemon/pikachu_happy3.ogg")

libpikachu @happy "Pikaaa!~"

pause 0.5

red @surprised "Huh?"
red @talkingmouth "Oh, that's right! You're going to come with me, buddy, aren't you?"

$ PlaySound("pokemon/pikachu_happy1.ogg")
libpikachu @talkingmouth "Pikachu."

red @sadeyebrows talkingmouth "Tell you what. Anytime I feel scared, or like I can't talk, I'll put my hand on your Poké Ball, alright? And you let me know you're there by rocking the ball."
red @happy "Sounds good?"

$ PlaySound("pokemon/pikachu_happy2.ogg")
libpikachu @talkingmouth "Pikerachu!"

red @happy "Love you too, buddy."

call clearscreens from _call_clearscreens_131
scene blank2 with splitfade
$ renpy.music.stop(channel='crowd', fadeout=1.5)
stop music fadeout 1.5

$ renpy.pause(2.5, hard=True)

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)

scene homeroom
show screen currentdate
show oak
with splitfade

oak @talkingmouth "Lad. How are you?"

red uniform @talkingmouth "Trucking along. Thought I'd get here before anyone else and take my seat."
red @sweat sadeyebrows talkingmouth "Maybe if I stay really, really, still, people won't notice I'm here."

oak @sadeyebrows talkingmouth "Lad, there's no future to be gained by hiding away from people. I did that, and look at me!"

red @confusedeyebrows talkingmouth "Uh... a world-famous, filthy-rich genius who pretty much everyone loves and respects?"

oak @closedbrow talkingmouth "Well, yes, I suppose that's one way to look at it."
oak @sad2eyes talking2mouth "But you know just as well as I do my failings."

red @sad "Still guilty over what you said on Friday?"

oak @talking2mouth "Very much so."
oak @closedbrow talkingmouth "But I suspect I know a way I might make it up to you."

red @confusedeyebrows talking2mouth "Oh, yeah? It's not sending me away to a different school, is it?"

oak @talkingmouth "No, not this time. Perhaps, if you have time to drop by the research laboratory later today, I can show you."

red @talkingmouth "Alright."

oak @surprised "Oh! Speaking of which, have you made much progress in figuring out how Foreverals work?"

menu:
    "No, I honestly have no idea.":
        $ AddEvent("Professor Oak", "ForeveralsNoIdea")
        show oak surprisedbrow frownmouth with dis

        pause 1.0
        
        oak -surprisedbrow -frownmouth @sweat closedbrow happymouth "Oh. Well, yes, I'm sure you were quite busy over the weekend. Days just fly by, don't they?"

    "I understand a little bit.":
        $ AddEvent("Professor Oak", "ForeveralsALittleBit")
        oak @talkingmouth "That's good."

    "Yeah, I figured it out.":
        $ AddEvent("Professor Oak", "ForeveralsFiguredOut")

        show oak surprisedbrow frownmouth with dis

        pause 1.0
        
        oak -surprisedbrow -frownmouth @sweat closedbrow happymouth "Oh! Already? That's... well, that's quite impressive!"

        red @happy "Thanks, Sam."

oak @sweat talkingmouth sadeyebrows "I must confess I haven't quite grasped it yet myself. Perhaps their effects are more apparent when used in battle than when played with in a laboratory."
oak @happy "I believe Miss Magnolia is currently running tests in the laboratory right now. If we're lucky, perhaps we'll walk in on a breakthrough."

red @happy "I'll cross my fingers."

show oak:
    ease 1.0 xpos 0.2
    pause 0.5
    ease 0.5 xpos 0.5 zoom 1.3 ypos 1.2

pause 1.5

oak @talking2mouth "Lad."

red @talkingmouth "Yes, Sam?"

oak sadeyebrows frownmouth @talking2mouth "You know I care about you, yes? You know I think of you as my own grandson, and always try to do right by you, yes?"

menu:
    "Of course, Sam.":
        $ AddEvent("Professor Oak", "KnowYouCare")
        
        oak @closedbrow talkingmouth "Good. I'm quite happy to hear that."

        oak @happy "Now, take your seat, Mr. [last_name]. Class is about to begin!"

    "...I know you try.":
        $ AddEvent("Professor Oak", "KnowYouTry")
        
        oak @talking2mouth "...Yes. I do. Very much so."

        narrator "You walk away."

    "[bluecolor][[Blue Rank 1]{/color} I think Blue should hear that." if (GetRelationshipRank("Blue") > 0):
        $ AddEvent("Professor Oak", "TalkToBlue")
        
        oak frownmouth @surprised "Eh?"

        red @talkingmouth "Blue. You know. Your {i}real{/i} grandson. Thank you for everything you do, and everything you've done for me, but... Blue feels like you only ever pay attention to {i}me.{/i}"

        oak @surprised "Oh."
        oak @sadbrow talking2mouth "I'll... er... I'll talk to him, then."

        pause 1.0

        oak @confusedeyebrows talking2mouth "Has this been going on for a long time?"

        red @sadeyes talkingmouth "Sam...{w=0.5} why don't you try and guess that, and I'll give you an answer?"

        oak @sad2eyes angryeyebrows talking2mouth "Yes, yes, very funny."
        oak @talking2mouth "Well, as I said, I'll talk to him."

        oak @happy "Now, take your seat, Mr. [last_name]. Class is about to begin!"

call clearscreens from _call_clearscreens_132
scene blank2 with Dissolve(1.0)

scene homeroom
show oakbg
show screen currentdate
with Dissolve(1.0)

narrator "As people file into class, you hear more than a few whispered comments directed at you."

Character("Nasty Lad") "\"{size=30}...can't believe he's still here...{/size}\""

Character("Sassy Wench") "\"{size=30}...freak. Tricked everyone...{/size}\""

Character("Unfair Trollop") "\"{size=30}...should be a law...{/size}\""

redmind uniform @sadbrow frownmouth "...Well, if there's any proof I needed that Frienergy isn't absolute, I guess this is it."

pause 1.0

oak @talkingmouth "Welcome back to class, everyone! Feels like it's been a long time, given all the hullabaloo over the Quarter Qlashes."

redmind uniform @sadeyebrows frownmouth "That feels very directed."

oak @talkingmouth "I hope you're all ready to listen sharp, once more, though. We've a lot of material to cover!"

show whitney uniform with dis:
    xpos -0.2 
    ease 0.5 xpos 0.23

whitney @surprised "Psst! Hey, hey!"

red @talkingmouth "Hay's for horses, but go ahead."

if ("Level2SceneVer2" in persondex["Whitney"]["Events"]):
    whitney @closedeyes talkingmouth "I can't believe I forgot to ask you when we hung out over the weekend. I just got so distracted with my own stuff."

whitney @talking2mouth "What's up with your Pikachu? How did you {i}do{/i} that to Dawn?"

red @sweat talkingmouth "Still figuring that out myself, to be honest."

whitney @closedbrow talkingmouth "I don't believe it. Not only do you have the crazy people powers, you've got a Pikachu that can defeat {i}Dawn{/i}? I've seen her in my Fairy classes. She's {i}really{/i} strong."

red @sad2eyes talking2mouth "Uh, Ixnay on the 'Crazy People Powers'-ay, please. It's just 'Frienergy,' and it's a very passive, {i}not harmful{/i}, power."

whitney @talking2mouth "Yeah, I know that! Tia told me!"

red @surprised "What? Have you seen her recently?"

whitney @surprised "What? No, have you?"

show flannery uniform tired behind whitney:
    xpos -0.2
    ease 0.8 xpos .43

pause 1.0

flannery @surprisedbrow talking2mouth "Wait, {i}neither{/i} of you have seen her? We thought she was with you, [first_name]."

red @confusedeyebrows talking2mouth "Sorry. Have you checked the roofs?"

flannery @tiredbrow talking2mouth "Ugh, so you've also seen her climb onto the roof before..."

red @talkingmouth "Once, yeah."

whitney @closedbrow talking2mouth "We haven't checked the roofs yet. Maybe we should do that after class...?"

red @talkingmouth "Good luck. I'll call you if I see her."

whitney playfulmouth @winkeyes talkingmouth "Will you?"

red @confusedeyebrows talking2mouth "Uh... yeah, I think so? What, am I missing something?"

flannery neutralmouth tiredbrow @closedbrow talkingmouth "Heh."

whitney @happy "[first_name], do you have {i}either{/i} of our numbers?"

red @closedbrow talking2mouth "{w=0.5}.{w=0.5}.{w=0.5}.Upon reflection.{w=0.5} No.{w=0.5} No, I do not."

whitney @playfulbrow playfulmouth "Well... let's make this a little fun, then. Whose number do you want more, [first_name]?"

menu:
    "Flannery's, no question.":
        $ ValueChange("Flannery", 3, 0.43)

        flannery @closedbrow talkingmouth "Mm. Fine."

        whitney -playfulmouth @angrybrow poutmouth "Aw, what?! Come onnnnn..."

        $ BecomeContacted("Flannery")

    "Yours, of course.":
        $ ValueChange("Whitney", 3, 0.23)

        whitney -playfulmouth @happy "Right answer!"
        whitney @sad2eyes sadeyebrows talking2mouth "{size=30}Sorry, Flan.{/size}"

        $ BecomeContacted("Whitney")

    "[bluecolor][[Whitney Rank 1]{/color} Whitney, gimme a break. We're close, aren't we?" if (GetRelationshipRank("Whitney") > 0):
        flannery @talking2mouth "Yeah, don't tease the guy, Whit. You two hang out all the time anyway. It's weird that you don't already have each other's numbers."

        whitney -playfulmouth @sad2eyes angryeyebrows poutmouth "Oh, alright... {size=30}steal my fun, why don't you...{/size}"

        $ BecomeContacted("Whitney")

        whitney @talking2mouth "For serious, though, you want to give him your number, too, Flannery? Like, this is for {i}Tia.{/i}"

        flannery @closedbrow talking2mouth "Yeah, fine."

        $ BecomeContacted("Flannery")

    "[bluecolor][[Flannery Rank 1]{/color} C'mon, Flannery, ask her to gimme a break." if (GetRelationshipRank("Flannery") > 0):
        flannery @talking2mouth "Yeah, don't tease the guy, Whit. He and I hang out all the time, anyway. It's weird that we don't already have each other's numbers."

        whitney -playfulmouth @sad2eyes angryeyebrows poutmouth "Oh, alright... {size=30}steal my fun, why don't you...{/size}"

        $ BecomeContacted("Whitney")

        whitney @talking2mouth "For serious, though, you want to give him your number, too, Flannery? Like, this is for {i}Tia.{/i}"

        flannery @closedbrow talking2mouth "Yeah, fine."

        $ BecomeContacted("Flannery")

red @happy "Alright, thanks. Now, we should probably pay attention to the lesson, you know? We can't find Tia if we don't know how to calculate the damage of a seventh-turn Fury Cutter with a Metronome."

whitney sad "Ugggggh. I hate math."

hide whitney 
hide flannery
with dis

jump homeroom1transition