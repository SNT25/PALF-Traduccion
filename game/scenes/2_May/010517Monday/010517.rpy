label day010517:

stop music fadeout 1.5

call calendar(1) from _call_calendar_42
$ calDate = calDate.replace(day=17, month=5, year=2004)

$ timeOfDay = "Morning"

$ PlaySound("Alarm.ogg")
$ renpy.pause(4.0, hard=True)

$ renpy.music.play("Audio/Morning_ambience.ogg", channel='crowd', loop=True, fadein=1.0)

pause 1.0

scene bedroom with transeye2

redmind @swimsuithatless tired unamusedeyebrows playfuleyes frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

pause 1.0

redmind @swimsuithatless tired unamusedeyebrows closedeyes frownmouth "...Coffee."

stop music fadeout 1.5 channel "crowd"

$ renpy.music.queue("Audio/Music/Pallet Town A.ogg", channel='music', loop=True, fadein=1.0, tight=None)

scene kitchen 
show screen currentdate
show ethan uniform:
    xpos 0.25
show yellow uniformbraid:
    xpos 0.5
show leaf uniform:
    xpos 0.75
with splitfade

leaf @happy "Good morning!"

ethan @closedbrow talking2mouth "Is it? You look like you died in your sleep and came back out of anger."

red @tired unamusedeyebrows talking2mouth "I feel like I did."

ethan @confusedeyebrows talking2mouth "Nightmares?"

red @surprisedbrow tired frownmouth "Hm?"
red @closedbrow tired talking2mouth "No. Blue and I just had an argument last night before we came back to the dorm."

red @closedbrow talking2mouth "Is he here?"

yellow @talkingmouth "He went straight to homeroom. He wants to talk to his Grandpa, I think."

red @talkingmouth "Yeah. Makes sense."

show hall_B_night at sepia
show flashback
with dis

$ renpy.pause(1.0, hard=True)

show blue surprisedbrow frownmouth at sepia behind flashback with dis

blue @talkingmouth "I... I did it. Not my Pidgeotto, but... I... {i}finally{/i} have something. I {i}finally...!{/i} And now Gramps will...!"

show blank with splitfade

hide blue
hide hall_B_night
hide flashback
hide blank
with Dissolve(2.0)

pause 2.0

show yellow sadbrow frownmouth with dis

red @sad2eyes angryeyebrows talking2mouth "...Heads up, Leaf. Blue's going to be {i}insufferable{/i} in class today."

leaf @closedbrow talking2mouth "Oh, when {i}isn't{/i} he?"

show ethan sad2eyes with dis

pause 1.0

show ethan -sad2eyes with dis

pause 1.0

show yellow surprisedbrow frownmouth with dis

ethan @talkingmouth "Hey, let's not badmouth the guy when he isn't here."

show yellow happybrow with dis

red @closedbrow talking2mouth "You're right. That was wrong of me. It's just... frustrating."

leaf @sadbrow talkingmouth "Might as well get it over with, then?"

red @closedbrow talking2mouth "Yeah, let's go."

pause 1.0

leaf @happy "You forgot to put your uniform on."

red @surprised "Huh?"

show yellow happy
show ethan happy
show leaf happy
with dis

red @closedbrow talking2mouth sweat "Ah, geez."
red @happy "Swear I'd lose my own head if it wasn't attached."

$ PlaySound("Pokemon/pikachu_happy3.ogg")

libpikachu @happy "Pi-i-i-ka!"

call clearscreens from _call_clearscreens_182
scene blank2 with splitfade
stop music fadeout 1.5

$ renpy.pause(2.5, hard=True)

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)

scene homeroom
show screen currentdate
show blue uniform:
    xpos 0.75
with splitfade

redmind uniform @frownmouth "Hm. Looks like Sam isn't here. But Blue is."
redmind @closedbrow frownmouth "...I remember what he said before 'Nate' wiped our minds. If those were his true feelings, then...?"

pause 1.0

redmind @sweat closedbrow frownmouth "I guess all I can do is wait for the storm. The moment Sam walks through that door, Blue's going to go crazy."

$ renpy.music.play("Audio/bigcrowdloop.ogg", channel='crowd', loop=True, fadein=10.5)
$ renpy.music.play("Audio/bigcrowdloop.ogg", channel='crowd2', loop=True, fadein=20.5)

show blank2 with splitfade

pause 1.0

narrator "You wait for a while as students start to filter in. Oddly, the persistently punctual Professor is nowhere to be seen."

pause 0.5

narrator "You notice Blue's hand is tapping rapidly on his desk."

hide blank2
hide blue
show leaf uniform at leftside:
    ypos 1.1 zoom 1.2
with dis

leaf @talking2mouth "Hey, did Sam tell you anything about him being late today? The bell's {i}just{/i} about to ring."

red @confusedeyebrows talking2mouth "Yeah, no, I'm at a loss, too. Maybe he's doing some last-minute tests on the Foreverals? Or..."
red @surprised "Wait, what if Blue already got to him?! What if he's in the lab now with Eevee, and--"

leaf @surprised "Whoa, whoa, what? Slow down! Explain what you mean! Blue getting to Oak? Eevee? What's this about?"

red @talking2mouth "...{i}Sigh.{/i} Yeah, alright. So here's what happened last night..."

show leaf surprisedbrow frownmouth with dis

narrator "You explain to Leaf the events surrounding Blue last night."

pause 1.0

leaf -surprisedbrow @talking2mouth "Oh. Wow. No wonder you looked rough this morning."

red @sad2eyes talking2mouth angryeyebrows "We were {i}so{/i} close to finally having a way to pay for Kobukan, but if Blue can just make the Foreverals, too, then..."

$ PlaySound("Door_Open1.ogg")

stop music fadeout 1.5
stop music fadeout 1.5 channel "crowd"
stop music fadeout 1.5 channel "crowd2"
queue music "audio/music/celebi_start.ogg" noloop
queue music "audio/music/celebi_loop.ogg"

show kris behind leaf:
    xpos -0.3 
    ease 0.5 xpos 0.5

kris @happybrow talkingmouth "Students! Hi. Sorry about my lateness. I didn't get my lesson plan from Doctor Oak until... well, nevermind. I'm here now."

show leaf surprisedbrow frownmouth with dis

red @surprised "Doctor Cherry?!"

show blue uniform:
    xpos 1.5
    ease 0.2 xpos 0.75

blue @surprised "What?! Where's Gramps?"

kris @surprised "Gramps? Oh, you must be Samuel's grandson. Hold on, I'll explain this to everyone."

kris @happy "Sit down, please."

hide leaf with dis

blue @closedbrow angrymouth "Nnrggh."

hide blue with dis

kris @talkingmouth "It's a pleasure to meet you all. My name is Doctor Kris Cherry. You can call me Professor Kris, or Doctor Cherry, or any combination of titles and names."
kris @closedbrow talking2mouth "Just... please {i}do{/i} use a title. I spent too much studying for my degree to not get as much use out of it as I can."
kris @talkingmouth "Doctor Oak asked me to swap classes with him for a short time. It's just a simple experiment about our efficacies as instructors."
kris @happy "You shouldn't notice any interruption, don't worry! Doctor Oak provided me a full and comprehensive lesson plan, so I should be able to pick up right where he left off."

redmind "That must be the folder she's holding. It looks a bit small though, doesn't it...?"

kris @sadbrow talkingmouth "Now, I'm afraid that Doctor Oak {i}just{/i} handed me the lesson plan, so I haven't had time to review it yet, so please bear with me for a couple moments while I get situated."

narrator "Saying so, Professor Cherry cheerfully opens the folder she's holding..."

show kris surprisedbrow angrymouth with dis

pause 1.0

show kris sadbrow sadmouth with dis

narrator "And pulls out a single piece of paper."

pause 1.0

narrator "She futilely flips it over, making apparent that there is text on only one side."

pause 2.0

kris "{w=0.5}.{w=0.5}.{w=0.5}."
kris -sadbrow -sadmouth @happy "Right, well, let's get started on the lecture Professor Oak has prepared."

narrator "Professor Cherry walks to the center of the classroom, ignoring the podium at the end, and starts lecturing, her earlier dismay seemingly forgotten."

kris @happy "I see you were learning about the history of champions. That's great, actually--Kobukan is the perfect place to learn about them, given how many of our alumni and instructors are, or were, champions."

kris @talkingmouth "Now, one especially prominent Champion, the youngest Champion of a major region to date is--"

show kris surprisedbrow frownmouth with dis

pause 1.0

kris -surprisedbrow -frownmouth -surprised surprisedbrow "Oh."

leaf uniform @talking2mouth "What is it? Do you think she learned something new?"

pause 1.0

kris sadbrow @closedbrow angrymouth "This... is wrong."

blue uniform @angry "What?!"

pause 1.0

blue uniform @glanceeyes wistfuleyebrows wistfulmouth "I mean... are you sure? My Gramps wrote it..."

kris -sadbrow @sadbrow talkingmouth "Yes. I'm afraid it's a bit out of date."
kris @happy "I'm sure it was just a case of overzealous copy-and-pasting. Even world-famous geniuses like Professor Oak can sometimes get things mistaken!"
kris @talkingmouth "Well, let me just make an edit here. I'm sure there aren't any more."

kris @talkingmouth "So, the youngest regional Champion, as of 2003, is not {i}this{/i} fellow, but is actually Iris Blanc, our very own Dean's daughter."

show kris surprisedbrow frownmouth 
with dis

red surprisedbrow frownmouth @surprised "{b}WHAT?!{/b}"

#Character("{color=#cf0000}[first_name]{/color} & {color=#00b23f}Leaf{/color} & {color=#3110dd}Blue{/color}") "{b}WHAT?!{/b}"

kris -surprisedbrow -frownmouth -surprised @talkingmouth "Is that especially surprising, for some reason?"

red @sweat talkingmouth "Oh, sorry for the outburst. I just spent all Springsday with her. I had no idea she was a Champion! She's so young..."

kris @happy "Yes, her nickname in Unova is 'the Child Champion.'"

red @closedbrow talking2mouth "I think I might've heard of her, actually. She unseated Alder, right?"

show gym at sepia
show flashback
with dis

$ renpy.pause(1.0, hard=True)

show bruno at sepia, leftside behind flashback 
show alder at sepia behind flashback
show tia uniform hat at sepia, rightside behind flashback 
with dis

bruno happy @happy2 "Perhaps that's why you were unseated by a toddler."

alder sad @sad2 "...She was {i}twelve{/i}, Bruno."

show blank with splitfade

hide alder
hide bruno
hide tia
hide gym
hide flashback
hide blank
with Dissolve(2.0)

red @happy "That's crazy. If she's a champion at twelve, already, I've really got no excuse to not hurry up."

kris @happy "Well, not all of us can be {i}quite{/i} at Iris Blanc's level, but that's a very good mindset to have. Doing everything she did, while so young... she's a bit of an inspiration to me."
kris @talkingmouth "Anyway, let's see, what did Doctor Oak want to teach next? He--"

pause 1.0

kris sadbrow @closedbrow talkingmouth "Oh. Well, that's not quite right, either..."

blue @cryingeyebrows glanceeyes glancemouth "...What?"

show blank2 with splitfade

narrator "This continues for about half an hour, with Professor Cherry trying valiantly to follow the lesson plan, while seemingly having to correct or add context to every third data point."

hide blank2 with splitfade

kris @happy "Well, that was the end of the lecture!"

narrator "A deafening silence fills the classroom."

flannery uniform @tiredeyes tiredeyebrows eyebags talking2mouth frazzled "Uh... Doc? We've still got an hour and a half of class left."

narrator "You look at the clock. It's closer to an hour and forty minutes. Admittedly, despite the many corrections Professor Cherry had to make, the lesson seemed to have flown by far faster than Professor Oak's lectures."

kris @closedbrow talkingmouth "...Right. Well, I'm sorry about this, but Professor Oak didn't share what he normally does after the lecture is over. I know what {i}my{/i} lesson plan is, but I don't want to disrupt your learning processes, so..."

narrator "The students in the classroom look around in a sort of confused stupor, waiting for someone to speak up."
narrator "You notice the very energetic Whitney is stock-still, staring at Professor Cherry with what looks like fascinated horror."

leaf @talkingmouth "Um... Doctor? The thing is, see... there isn't normally an 'after the lecture'. He lectures 'til the bell rings."

kris @happy "Hah hah! Yes, it can seem like that, can't it? But I'm referring to the practical parts of the class." 
kris @talkingmouth "You know, Poké Ball construction, damage mathematics olympiads, Pokédex usage and upgrading. And that's not even counting the live battles, of course."

show kris surprisedbrow angrymouth with dis

pause 2.0

blue @glanceeyes talking2mouth "We don't do that here."

pause 1.0

kris @talking2mouth "Oh."
kris -surprisedbrow -angrymouth @talkingmouth "Well, Doctor Oak is a genius beyond compare. I'm sure he's just teaching on a level that a new teacher like myself couldn't possibly begin to understand. I mean, if your grades are high, then what do we have to worry about, right?"

pause 1.0

kris @surprised "{size=30}Actually... maybe I should just...{/size}"
kris @happy "Blue. Would you mind telling me where Professor Oak keeps his tests?"

narrator "Blue nods sullenly at a cabinet on the side of the room. Kris nods politely and heads toward it."

show kris:
    xpos 0.5 
    ease 0.5 xpos 1.2

pause 0.5

hide kris

kris @surprised "{size=30}Oh, locked... he probably should have given me the password...{/size}"
kris @happy "Well, this seems like an excellent opportunity to demonstrate some of the practical skills that our Pokémon partners have."

$ sidemonnum = pokedexlookupname("Rotom", DexMacros.Id)

$ PlaySound("pokemon/ball sound.ogg")
$ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))

kris @talkingmouth "Rotee, would you mind popping in this electric lock for me and giving it a little kick?"

sidemon @talkingmouth "Rotototo-rotototom!"

narrator "With a click, the lock opens easily."

$ PlaySound("Door_Open1.ogg")

leaf @talking2mouth "Woah. Is Doctor Cherry a master thief?"

kris @surprised "Of course not!"

leaf @embarrassedbrow talkingmouth "Ooops."

kris @happy "But I {i}would{/i} be a good one, if I had the inclination."

narrator "Kris looks through the pile of paperwork, then walks back to the middle of the room, scanning through the pages."

show kris with dis

if (WonBattle("IgnoredOak")):
    kris @closedbrow talkingmouth "Oh, there we go, this isn't as bad as I feared. On top of the list--Blue Oak. Perfect marks."

else:
    kris @closedbrow talkingmouth "Oh, there we go, this isn't as bad as I feared. On top of the list--Blue Oak. Excellent marks."

blue @closedbrow talking2mouth "Heh."

kris @talkingmouth "Right underneath..."

$ grade = GetGrade()

if (grade >= 9):
    $ ValueChange("Professor Cherry", 9, 0.5)

    kris @happy "[first_name] [last_name]. Perfect marks."
    
    kris @talkingmouth "Phew, nothing to worry about! Let's see, what's underneath..."

elif (grade > 4):
    $ ValueChange("Professor Cherry", grade, 0.5)

    kris @happy "[first_name] [last_name]. Great marks."

    kris @talkingmouth "Phew, nothing to worry about! Let's see, what's underneath..."

show kris surprisedbrow angrymouth with dis

pause 1.0

kris sadbrow @talking2mouth "Uh-oh."

leaf @surprised "{size=30}Uh-oh?! What does she mean by uh-oh?!{/size}"

narrator "Kris flips through the papers faster and faster. She returns to the filing cabinet, pulls out more papers, and begins to dig through them with feverish abandon."

pause 1.0

blue @angrybrow angrymouth "Hey! What's going on?!"

pause 2.0

kris @closedbrow talking2mouth "...It's... okay. With the understanding I have {i}full{/i} respect for everything Professor Oak does, that he is my mentor, in many ways, that I'm only a fraction of the teacher he is..."

pause 1.0

kris @closedbrow talking2mouth "{size=30}How do I say this...{/size}"

kris @sadbrow talkingmouth "At this rate, very few of you are going to graduate?"

show blank2 with Dissolve(2.0)

narrator "With that bombshell dropped, Professor Cherry instructs you all toward independent study while she frantically writes up a more all-encompassing catchup lesson plan for the rest of the week."

pause 1.0

narrator "You and your friends try to focus on your textbooks, but the ominous feeling of the academic guillotine hanging over your head somewhat dulls the mood."

jump homeroom1transition