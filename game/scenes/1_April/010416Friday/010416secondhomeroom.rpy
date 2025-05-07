label secondhomeroom010416:

scene blank2

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom behind blank2

show oakbg behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade

oak @talkingmouth "...needless to say, laws regarding the necessity of proper accreditation when training and possessing Pokémon were quickly passed."
oak @talkingmouth "After unlicensed trainers became unable to possess Pokémon, the fledgling child trainer population dropped to essentially zero." 
oak @talkingmouth "Given these children now had nothing to do, and confiscating all their newly 'illegal' Pokémon would have been an act to inspire riots, schools were instead founded to hurry them through the licensing process."
oak @talkingmouth "Kobukan Academy, though many miles away, was founded by a group of teachers, businessmen, and translators employed by the Tokugawa Shogunate, answering Kobukan's request for instruction."
oak "Indeed! Kobukan Academy is the {i}direct{/i} educational descendant of those licensing schools."
oak @talkingmouth "Some say the emperor's response to what was an isolated, if heartbreaking, tragedy was heavy-handed, but at the same time, our Pokémon-focused world nowadays is a direct result of his decisiveness."
oak "After all--can you imagine a world where children would be permitted to go out into the wild with Pokémon, and no education or training? What a scary thought!"

$ PlaySound("BellChime.ogg")

$ renpy.pause(2.0, hard=True)

oak @talkingmouth "Let us hope that we can all make the right decision when our moment to alter the future comes. For now, though, go home and enjoy the weekend!"

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.5)

hide oakbg with dis

show may uniform with dis

may @talkingmouth "Hey! Brendan told me you're going to be battling Hilbert?"

red uniform @happy "Yep. Want to come watch?"

may @happy "Totally! I think the guys are already heading to the Battle Hall."

show leaf uniform at rightside with dis

leaf @happy "Room for one more?"

red @happy "Ooh, sorry. {i}Just{/i} sold out of tickets."

leaf @surprised "What?! But I'm a VIP! I get the corner box! The penthouse suite! The... The mint on the pillow!"

red @talking2mouth "Sorry, Ma'am. I'm not seeing your name on this list."

leaf @happy "Hah. You better look a bit harder. It might be under 'Queen Leaf III, Long May She Reign'?"
leaf @flirttalk "I'm actually Galarian. On the royal side."

red @closedbrow talking2mouth "Oh, my mistake. Yup, there you are."

leaf @talking2mouth "There we go." 

show may surprisedbrow with dis

leaf @flirttalk "I'll give you a big tip."

show may -surprisedbrow with dis

may @talkingmouth "Are... are you two dating?"

leaf @surprised "Uh... no."

$ relationship = GetRelationship("Leaf").lower()
red @talkingmouth "Yeah, no. Just [relationship]s."

may @talkingmouth "Oh. Okay."
may @happy "Sorry, guess that was a weird question, right? I'm going to go meet up with Brendan."

hide may with dis

show leaf:
    ease 0.5 xpos 0.5

pause 2.0

red @happy "Soooo..."

menu:
    "Want to go on a date?":
        show leaf fullblush angry with dis

        $ ValueChange("Leaf", -1, 0.5)

        leaf frownmouth @angry "H-hey! Cool it, mister! I've known you for, like, two weeks!"

        leaf @angrybrow talking2mouth "That's moving way, {i}way{/i} too fast. I don't think you're a jerk or a creep or anything, but I need to..."

        leaf @closedbrow talking2mouth "You know. Figure some stuff out. I'll let you know when {i}I'm{/i} ready."

        red @sadeyes sadeyebrows talking2mouth "My bad."

        pause 1.0

        leaf -frownmouth -fullblush @talkingmouth "It's alright. I can tell you meant it. I just... that earnestness is cute, but freaks me out."

        red @talking2mouth "Still. Sorry about that."

    "I'm out.":
        leaf @closedbrow talkingmouth "...{i}Are{/i} we dating?"

        red @talkingmouth "I think I'd know if we were."

        leaf @happy "Yeah, you're right."

pause 1.0

red @closedbrow talking2mouth "Looks like Hilbert's already left for the Battle Hall, then. Meet up with you there?"

leaf @talking2mouth "Sure. See you there."

call clearscreens from _call_clearscreens_54
show blank2 with splitfade
$ AddPikachu()
$ HealParty()

show stadium_empty behind blank2
show janine at rightside behind blank2:
    xzoom -1
show lance at leftside behind blank2

play music "Audio/Music/League_Start.ogg" noloop
queue music "Audio/Music/League_Loop.ogg" 

pause 2.0

show screen currentdate
hide blank2 
with splitfade

redmind -uniform @happy "Hey, there's Janine!{w=0.5}{nw}"
extend @sad " ...And Lance."

lance @angry "{i}You.{/i}"

red @sadeyes sadeyebrows talkingmouth "Uh... hi, Si-"

show lance:
    ease 0.4 xpos 0.5 zoom 1.5 alpha 0.0 ypos 1.4

pause 0.2

red @surprised "Huh?"

$ PlaySound("Body Roll.ogg")

blue @surprised "Gah! What's the big idea?"

show lance:
    ease 1.0 xpos 0.25 zoom 1.0 alpha 1.0 ypos 1.0

show blue sad:
    alpha 0.0 zoom 1.5 ypos 1.4
    ease 1.0 alpha 1.0 zoom 1.0 ypos 1.0

lance sadbrow @talking2mouth "I genuinely cannot tell whether I am angrier at you for trying to get into the Battle Hall by hiding behind another student, or for doing so poorly at it."

janine @talking2mouth "Yeah, you've got two feet of hair on this guy. You kinda stick out."

blue -sad frownmouth @talkingmouth "Look, I'm not here to cause any trouble. I just heard this guy was battling, and wanted to check it out."

janine @angry "What part of {i}banned{/i} do you not get? You are banned until the tryouts! That's three days from now. B{w=0.25}A{w=0.25}N{w=0.25}N{w=0.25}E{w=0.25}D."

blue @talkingmouth "You were willing to make an exception last week!"

janine @sad "Yeah, and see if you ever catch me doing that again."

lance @talking2mouth "I will say this simply. Begone from this place. You have stacked the deck so far against yourself that your entrance into the Battle Team now would be an absolute miracle. Remove yourself from the hole you're digging, and be gone."

janine @talking2mouth "I'll say it simpler:{w=0.5}{nw}"
extend @angry " Get lost."

pause 1.0

blue angry "Watch your back, [first_name]."

hide blue with dis

pause 1.0

lance @sad "If you continue to bring drama into this Battle Hall every time you wish to battle, [first_name], then I will ban {i}you{/i} from this location, as well."
lance @talking2mouth "Begin your battle and get out. You've tarried enough."

hide lance with dis

pause 2.0

show hilbert at leftside with dis:
    xzoom -1

hilbert @talkingmouth "Are you ready?"

red @talkingmouth "Yep."

hilbert @talkingmouth "Good. Let's begin."

redmind "Oh, look. There's Ethan, Brendan, Calem, and May, up in the bleachers!"

brendan @happy "{size=50}Wooooo! You got this, bro!{/size}"
calem @talkingmouth "{size=30}Wait, which one are you cheering for?{/size}"
ethan @talkingmouth "{size=40}Dorm 151, rep-re-SENT!{/size}"
may @talkingmouth "{size=40}Do your best, you two!{/size}"

$ HealParty()

$ trainer1 = Trainer("red", TrainerType.Player, playerparty)
$ trainer2 = MakeTrainer("Hilbert")

call Battle([trainer1, trainer2]) from _call_Battle_21
$ battlehistory["Hilbert1"]  = _return

show hilbert at centerside with dis

$ renpy.music.play("Audio/bigcrowdloop.ogg", channel='crowd', loop=True, fadein=1.5)

pause 1.0

red @surprised "Hey, each of your Pokémon only used one move over and over! Do they actually listen to you?"

hilbert @talkingmouth "Not as such. Rather, I've made them forget all their moves except their most powerful."

red @happy "Hey, that's pretty clever! How did you do that?"

hilbert @talkingmouth "I cannot explain it.{w=0.5}{nw}" 
extend smilemouth @happymouth "...Forgetting has always come easily to me."

red @talkingmouth "Well, clearly, it worked. Good job."

if (WonBattle("Hilbert1")):
    hilbert -smilemouth @talkingmouth "Thank you. You've shown yourself to be a competent trainer, even without the obedience edge."
    hilbert @closedbrow talkingmouth "I'll lend you my Pokémon."
else:
    hilbert -smilemouth @sadbrow talkingmouth "Your praises mean nothing, as the defeated. I will not be lending you my Pokémon."

show lance at leftside 
show janine surprisedbrow frownmouth
with dis

$ renpy.music.queue("Audio/Music/DragonDenStart_B.ogg", channel='music', loop=False, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/DragonDenLoop.ogg", channel='music', loop=True, fadein=0.0, tight=None)

lance @talking2mouth "What's this about lending Pokémon?"

hilbert @talkingmouth "We were battling to see if [first_name] could borrow my Pokémon for the upcoming Battle Team tryouts."

lance @angrybrow shadow "{w=0.5}.{w=0.5}.{w=0.5}."

redmind @sadeyes sadeyebrows frownmouth "Oh, man, he's pissed."

hide hilbert with dis

lance -angry @talking2mouth "Janine, did you recommend this young man borrow Pokémon to use for his application to the Battle Team?"

janine -surprisedbrow -frownmouth -surprised @talking2mouth "Yes, I did."

lance @angry "Despite the fact I had explicitly declared he will {i}not{/i} get onto the Battle Team?"

janine @talking2mouth "Technically, Sir, I wasn't there when you said that, so I couldn't be blamed for not knowing."

lance @sadbrow talking2mouth "One of the Team has told you by now, though. So, I repeat."

janine @talking2mouth "Yes, Sir. I think he could be an amazing asset in battle. We'd be able to sweep the Quarter Qlashes this year with him."

pause 1.0

lance @talking2mouth "Carry on."

janine @closedbrow talkingmouth "He doesn't need to have even used a Pokémon before in order to be in perfect sync with them." 
janine @happymouth "As long as he knows how to battle, and his Pokémon {i}are{/i} stronger, there's no fight he can't win."
janine @talking2mouth "We can't just leave him on the table, Sir."

pause 1.0

lance @talking2mouth "However. I declared that he {i}would not{/i} make it into the Battle Team."

janine @sad "Sir... you know I really respect you, but... at the end of the day..."

lance @closedbrow talking2mouth "It is the Captain's decision."

pause 2.0

lance @talking2mouth "It {i}is{/i} the Captain's decision. However. The terms of the battle tryouts are set by the faculty. And 'borrowed' Pokémon will not be permitted."

janine @surprised "Lance?!"

lance @closedbrow talking2mouth "I have said it; it is so."

pause 1.0

janine @talking2mouth "Will you permit the usage of a strength equalizer then, Sir?"

show lance sadbrow with dis

pause 2.0

lance @sadbrow talking2mouth "Fine. But sticking your neck out for this child will only serve to hurt you."

hide lance with dis

pause 2.0

brendan @happy "{size=50}Wooooo! Great battle, guys! {/size}Wait, where'd Hilbert go?"

janine @closedbrow talkingmouth "Hm... thinking, thinking, thinking... okay."

stop music channel "crowd" fadeout 0.5

janine @angry "Everyone out. Now."

pause 2.0

redmind @surprised "Woah. I've never seen a room empty so fast. She didn't even yell."

show janine:
    ease 0.5 xpos 0.5

janine @talking2mouth "Look at me."

red @talkingmouth "Yes, Ma'am."

janine @closedbrow talkingmouth "And cut that out, I'm only twenty-one."

redmind "It's definitely more about how you present yourself than it is about your actual age."

janine @closedbrow talkingmouth "So, borrowing Pokémon is a bust, thanks to your dormmate."
janine @talking2mouth "But I got us a strength equalizer. That means, even if your opponents have much higher-level Pokémon, you'll all be fighting at the same level."

red @talking2mouth "But that doesn't cover movepools... or base stats, or items..."

janine thinking @talking2mouth "No. And you'll definitely be facing opponents who've been training a lot longer." 

pause 2.0

janine -thinking @talking2mouth "Alright, got it. You're going to go to Inspira tomorrow."

red @talkingmouth "Oh. Yes, I am! I was actually going to go there tomorrow with some friends."

janine @happy "Good. Go to the Pokémon Center, and use the PC there. As a registered trainer, I have access to the Pokémon Center's Pokémon storage database." 
janine @talking2mouth "Log in under the username xToxikxShadowx. Password is I<3Venonat. You--"

janine @angry "Write those down."

red @talkingmouth "Oh, okay!"

janine @talking2mouth "After you log in, create a new set of boxes for yourself. Then, go to the Pokémart in the same building, and buy as many Poké Balls as you can carry."

red @closedbrow talking2mouth "With you so far..."

janine @talking2mouth "Use those Poké Balls to catch a full team of six Pokémon. Your advantage is your ability to command multiple Pokémon at once." 
janine @talking2mouth "Your opponents might be stronger, but your best bet is to overwhelm them with sheer numbers."

red @talkingmouth "Like when I battled [blue_name]... or that Absol."

janine @surprised "You fought an Absol? Huh. Anyway, yeah, exactly."

janine @sad "Most of your opponents will be using Pokémon around level 20 or so, before the strength equalizer. Expect to see a few evolved Pokémon. And, uh..."
janine @talking2mouth "Your biggest advantage? That your Pokémon listen to you right away? Expect that to go away. Around level fifteen is when trainers can start commanding their Pokémon properly."

red @closedbrow talking2mouth "Geez. Guess the grace period is over, huh?"

janine @talking2mouth "Yeah."

red @happy "Thanks for doing all this for me, though. I really appreciate it."

janine @talking2mouth "You're worth it. If this Battle Team gets you... well, there's nothing stopping us from finally sweeping the National Tournament." 
janine @happy "And then I'll finally be free to try for Champion."

menu:
    "{color=#60c2f8}[[Wit]{/color} You want a dominating victory before you leave?":
        show janine surprisedbrow frownmouth with dis

        $ TraitChange("Wit")

        janine -surprisedbrow -frownmouth -surprised @talking2mouth "Figured it out? Yeah. We've done well the last few years, but Kobukan deserves more than 'well.'"
        janine @happy "I really love this school. And nothing would make me happier than if it got what it deserved--a brutal crushing of our opponents, and a straight shot to the Kobukan Championship."
    
    "{color=#ff8412}[[Courage]{/color} I'm going to beat you there.":
        show janine surprisedbrow frownmouth with dis

        $ TraitChange("Courage")

        janine -surprisedbrow -frownmouth -surprised @talking2mouth "Woah. Cocky, aren't you?"

        red @happy "Confident. I've heard that Kobukan doesn't even have a Champion right now. Seems like a good spot for me to fill."

        janine @happy "Well, I like your ambition. Keep that end-goal in mind."

        janine @smirkmouth "And don't be so disappointed when I hand you a crushingly brutal defeat."

red @happy "Is the brutality necessary?"

janine smilemouth @smirkmouth "If we're going to spend some time together, there's something you're going to need to learn."

pause 1.0

show janine:
    ease 2.5 xpos 0.5 ypos 1.2 zoom 1.3

pause 1.0

janine @smirkmouth blush "I don't like only having a piece of something. I want it {i}all.{/i}" 

red @surprisedeyes surprisedeyebrows talking2mouth "Un-- understood. Janine."

show janine:
    ease 0.5 xpos 0.5 ypos 1.0 zoom 1.0

janine @happy "Good."

janine -smilemouth @talking2mouth "Now get out of here. I've got some logistics to handle for the tryouts."

red @talkingmouth "See you Monday."

janine @closedbrow "Mm."

call freeroam from _call_freeroam_4

call texting from _call_texting_5

jump day010417