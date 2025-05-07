label secondhomeroom010518:

scene blank2 with splitfade

pause 1.0

stop music fadeout 1.5
queue music "audio/music/celebi_start.ogg" noloop
queue music "audio/music/celebi_loop.ogg"

scene homeroom 
show screen currentdate
show kris
with splitfade

kris @talkingmouth "Evening, class! You all look very awake. That's what getting up in the morning for a hike up the mountain will do for you!"

flannery uniform @surprised "{size=30}Oh, no, she's not going to make us do it {i}again{/i}, is she?{/size}"

whitney uniform @confusedeyebrows talking2mouth "{size=30}Why do you care? You're evening Flannery right now. Evening Flannery loves the outdoors and hikes in the wild.{/size}"

flannery @sweat happy "{size=30}Yeah, but morning Flannery is the one who's going to get to do it!{/size}"

whitney @closedbrow talkingmouth "{size=30}Girl, we {i}need{/i} to get you in a CAT scan.{/size}"

kris @talkingmouth "Let's talk about critical hits. Can anyone tell me the likelihood of landing one?"

show hilbert uniform with dis:
    xpos 0.75

pause 1.0

kris @talkingmouth "Yes, you, with your hand raised."

hilbert @talkingmouth "It's one in twenty-four."

kris @happy "Well done!"

hide hilbert with dis

leaf uniform @talkingmouth "That's weird. Hilbert never raises his hand in class. He just says the answer. Is it possible we've actually found a teacher Hilbert {i}respects{/i}?"

pause 1.0

leaf @sadbrow talking2mouth "Wait, [first_name], what's wrong? You look really upset. Did something happen when you followed Bianca...?"
leaf @surprised "Wait, actually, she didn't show up in our Normal elective, either! What happened?!"

red uniform @sadbrow talking2mouth "...It's not something I should share. But she'd probably appreciate a call from her old roommate right about now."

leaf @surprisedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
leaf @talking2mouth "Okay."

$ PlaySound("vibrate.ogg")
$ PlaySound("vibrate.ogg")
$ PlaySound("vibrate.ogg")

red @surprised "Wh-what?! What are you doing?"

leaf @surprised "What do you mean 'what am I doing?' I'm calling her!"

red @surprised "Not now! Not in the middle of class!"

leaf @angry "You said she'd appreciate a call 'right about now'!"

red @closedbrow sweat talking2mouth "It was a turn of phrase... give it a few more hours at least, geez. Also..."

narrator "Professor Cherry, and more than a few other students, are staring at you."

Character("Callow Youth") "{size=30}\"Ugh, I can't {i}stand{/i} that guy. Always interrupting class to say something stupid. He's worse than [oldblue_name].\"{/size}"

Character("Arrogant Slattern") "{size=30}\"Tell me about it. At least now our prof isn't constantly sucking his--\"{/size}"

narrator "You decide not to listen any further."

redmind @closedbrow frownmouth "Tune them out, [first_name]. Tune them out."

leaf @angrybrow talking2mouth "{size=30}I'll say something.{/size}"

red @sadbrow talking2mouth "{size=30}I know you would. Please don't.{/size}"

kris @talkingmouth "[first_name]?"

redmind @closedbrow frownmouth "Oh boy. Here comes a chewing-out. I knew I couldn't survive in a classroom {i}not{/i} taught by one of my best friends."
red @sadbrow talkingmouth "Yes, Professor?"

kris @happy "Try to stay engaged with the lesson, okay? It's actually {i}really{/i} important that you pay attention to this."
kris @talkingmouth "In fact, it's important you {i}all{/i} pay attention."
kris @talkingmouth "A lot of what I'll be teaching in these homerooms will help you on the exams."
kris @closedbrow talking2mouth "It looks like you had, previously, just been thrown tests without any preparation... I'm hoping I can fix that for you."

pause 1.0

kris @talkingmouth "So, just to make sure you were paying attention, what is the average critical hit ratio of a move, [first_name]?"

menu:
    "One in twelve.":
        kris @closedbrow talkingmouth "Not quite. Double that--it's one in twenty-four."

    "One in twenty.":
        kris @closedbrow talkingmouth "Not quite. Increase it by a fifth--it's one in twenty-four."

    "One in twenty-four.":
        kris @closedbrow talkingmouth "Perfect."

        $ ValueChange("Professor Cherry", 1, 0.5)

    "One in one hundred.":
        kris @closedbrow talkingmouth "Not quite. Quarter that, then one less--it's one in twenty-four."

kris @happy "Let's try to pay a bit more attention to the lectures from now on, okay? They're going to matter."
kris @angrybrow talkingmouth "And I'm not {i}always{/i} going to say the important part [bluecolor]in blue text.{/color}"

pause 1.0

redmind @unamusedbrow unamusedmouth "...She really {i}is{/i} Ethan's babysitter."

show blank2 with splitfade

kris @talkingmouth "Let's talk about critical hit {i}stages{/i}, now. When you have three different sources boosting your critical hit ratio, it's actually possible to {i}guarantee{/i} a critical hit." 
kris @talkingmouth "You generally need to set up a specific combination to make this happen, but if you manage it, then..."

narrator "Professor Cherry finishes the lecture, then sends you on your way when the bell rings. Leaf quickly excuses herself to call Bianca again."

$ PlaySound("BellChime.ogg")

kris @talkingmouth "I'll see you tomorrow. Go to bed on time! There's no point studying late into the night if you're too tired to think."

$ removestudents = { "Leaf", "Blue", "Bianca" }

call freeroam from _call_freeroam_25

$ removestudents = set()

call texting from _call_texting_20

if (texted):
    red hatless casual @thonk "Hm? Another text...?"

else:
    red hatless casual @thonk "Hm? A text...?"

show phone_B
show phone_A
show leaf hatless sadbrow frownmouth behind phone_A:
    zoom 0.95
with fadeinbottom

$ lowerfirst_name = first_name.lower()

leaf @talking2mouth "talked with bianca."
leaf @talking2mouth "cant believe it. couldnt have happened to a nicer person."

show leaf -frownmouth with dis

if (HasEvent("Bianca", "Comfort")):
    leaf "she said you talked to her."
    leaf "youre a good man, [lowerfirst_name]."

else:
    leaf "ive got a plan, but dont think i can provide much immediate comfort."
    leaf "maybe you could talk to her and frienergy her up. you know, be a shoulder to cry on."
    leaf "youre good at that."
    leaf "big shoulders."

pause 1.0

leaf @talking2mouth "gnight"

hide phone_B
hide phone_A
hide leaf
with fadeoutbottom

jump day010519