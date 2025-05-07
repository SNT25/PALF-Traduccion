label day010524:

stop music fadeout 1.5

call calendar(1) from _call_calendar_49

python:
    calDate = calDate.replace(day=24, month=5, year=2004)
    timeOfDay = "Morning"
    renpy.pause(2.5, hard=True)
    renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)

scene homeroom
show screen currentdate
show oak frownmouth
with splitfade

redmind uniform "...Sam is back."

pause 1.0

redmind @happy "Great! I missed him."

pause 0.5

redmind @sad2eyes frownmouth "But... I {i}am{/i} concerned about how the other students will react."

pause 1.0

oak closedbrow @talking2mouth "...{i}Sigh.{/i}"

pause 0.5

oak -closedbrow @talkingmouth "Class, I'd like to teach you, possibly, the most important thing I will ever teach this year."

show flannery tired uniform:
    xpos 0.1
show whitney uniform frownmouth:
    xpos 0.3
show blue uniform:
    xzoom -1 xpos 0.9
show hilbert uniform:
    xpos 0.7
with dis

pause 1.0

redmind @thinking "You could hear a pin drop."

pause 0.5

oak -frownmouth @talkingmouth "If there's anything that my years of study of Pokémon-human Psychosociology has taught me, it's that reputation is worth less than nothing."
oak @closedbrow talking2mouth "One should be judged by their actions, their skills, and their words. Reputation is attributing value to something based on nothing but what one believes other people consider its value to be."
oak @happy "Why, if that was the sort of anti-scientific thought I was interested in, I would have invested in the stock market!"

pause 1.0

oak frownmouth @closedbrow talking2mouth "Ahem."

pause 0.5

oak @talkingmouth "Professor Cherry has done all of you a great service. And she has done an even greater one for me."
oak @sad2eyes talking2mouth "And it seems that I... in my hubris, and in my belief in what others say of me... thought my procedures and methods infallible."
oak @closedbrow talking2mouth "The data that is so apparent to me now is not one I'd considered until Professor Cherry... er, and her class, in all honesty... made clear what some of my blind spots have been."

pause 1.0

oak -frownmouth @talkingmouth "Well, that was all I intended to say on that matter. I can't work on my abilities as a teacher if I spend all my time engaged in self-flagellation."

show flannery surprisedbrow frownmouth
show whitney surprisedbrow frownmouth
show blue surprisedbrow frownmouth
show hilbert surprisedbrow frownmouth
with dis

oak @closedbrow talking2mouth "Now, it's become apparent to me that I have not been adequately preparing you for the tests you are taking."
oak @talkingmouth "I will now remedy that."

hide flannery
hide whitney
hide blue
hide hilbert
with dis

redmind @surprised "Huh? Did Sam have some sort of epiphany...?"

oak @talkingmouth "Your test this evening is a simple one, in contrast to the test that will be given on Thursday."
oak @talkingmouth "Who here can explain the concept of coverage moves?"

pause 0.5

oak @talkingmouth "Ms. Berlitz?"

show dawn uniform with dis:
    xpos 0.25

dawn uniform @surprised "M-m-m-me?! Oh, geez, I, um, I..."

pause 0.5

dawn @sadbrow talkingmouth "Sorry. Yes. Yes, I can. Coverage moves are moves a Pokémon is trained to learn to be able to compete with Pokémon that aren't weak to their primary type... or types."

oak @talkingmouth "Correct. The list of coverage moves every Pokémon might have is massive, and is not something I would recommend one try to memorize."
oak @talking2mouth "Many matchups that seem like foregone victories can easily become lost causes if one of the two has a single, key, move that turns the tide in the opposite direction."

dawn @talkingmouth "I keep Earthquake on my Altaria to deal with Steel-types that she would normally have difficulty dealing with!"

oak @happy "That's an excellent example, yes."

hide dawn happy with dis

oak @talkingmouth "Doctor Katsura--Instructor Blaine, to you--mentioned once he was battling a trainer who possessed a Feraligatr. Only Blaine's Rapidash and the foe's Feraligatr were strong enough to battle."
oak @closedbrow talkingmouth "Doctor Katsura's Rapidash had the speed advantage, but that advantage does not mean much if one is not capable of landing a finishing blow before becoming knocked out oneself."
oak @talkingmouth "However, his Rapidash had a trick up its sleeve--Wild Charge. By using a move the challenger did not expect, a move that many Rapidash do not know, Doctor Katsura was able to take his challenger off-guard and defeat him."
oak @closedbrow talkingmouth "It may interest you to know that challenger was none other than Champion Lance himself."

leaf uniform @surprised "What?"

oak @talkingmouth "This expresses the importance of coverage moves. They allowed a Gym Leader to beat a Champion!" 
oak @happy "Doctor Katsura's Fire-type moves would have failed to have any impact on Champion Lance's dragons and Water-type, but through clever moveset creation, he was able to pull out a victory." 
oak @talking2mouth "Granted, Lance was {i}not{/i} a champion at that time."

blue uniform @confused "Lance doesn't use a Feraligatr."

oak @closedbrow talking2mouth sweat "No, not anymore. I am not certain, but I believe he retired that member of his team shortly before his attainment of the Kanto Champion title."
oak @sad2eyes talkingmouth "Perhaps he would divulge more details to members of his Battle Team, if you were to ask."

blue uniform @closedbrow frownmouth "Hm."

oak @talkingmouth "Now, some Pokémon have far more coverage options than others. My specialty, Normal-types, are particularly--"

pause 1.0

stop music fadeout 3.33

oak sweat @talking2mouth "Hm?"

$ PlaySound("clap.ogg")

Character("???") "{w=0.333}*Clap.*" 

$ PlaySound("clap.ogg")

extend @talkingmouth "{w=0.333}*Clap.*"

$ PlaySound("clap.ogg")

extend @talkingmouth "{w=0.333}*Clap.*"

leaf uniform @surprised "Huh? Who's that?"

red @confused "I don't know. Is it--?"

queue music "audio/music/lawrencetheme_start.ogg" noloop
queue music "audio/music/lawrencetheme_loop.ogg" 

narrator "You turn around in your seat to see who the mysterious clapper at the back of the room is."

show phobosintroduction
show phobosintroductionclapping
show phobosintroductioneyes
show phobosintroductionmouth
show phobosintroductioneyebrows
with Dissolve(3.333)

phobos @talkingmouth "{i}Brava{/i},{w=0.333} {i}bravo{/i}{w=0.333} and {w=0.333}{i}bravi!{/i}"

pause 3.333

redmind @confusedeyebrows frownmouth "Hm? Who's this guy? Is he on a... a floating chair?"

show phobos:
    xpos 0.333

show oak:
    xpos 0.66

hide phobosintroduction
hide phobosintroductionclapping
hide phobosintroductioneyes
hide phobosintroductionmouth
hide phobosintroductioneyebrows
with dis

phobos @closedbrow talkingmouth "Magnificent, magnificent, and magnificent, my esteemed Sam Oak!"
phobos @happy "Truly, you are a genius atop your field! An intellect beyond compare! A paragon of education!"

oak @talking2mouth "Why... I appreciate the compliment, er, thank you. But I'm afraid I'm in the middle of a lesson right now, so--"

phobos @sadbrow talking2mouth "Sam, Sam, Sam! Surely you have three seconds to spare for your generous benefactor?"
phobos @winkbrow talkingmouth "Why, if you put me off, I may be concerned you've forgotten who recommended your appointment as a teacher here!"

oak @confusedeyebrows talking2mouth "Er... I suppose I had, actually. That was you?"

phobos @happy "Of course! Oh, Sam, Sam, Sam, you wound me."
phobos @talkingmouth "In any case, please, this will only take three minutes."

oak @talkingmouth "Well, what can I help you with, then?"

$ autoquote = False

phobos @happy "\"Oh, it's just the {i}most{/i} delightful thing. Why, this class of yours, I can't help but notice it has thirty"
extend @shadow angrybrow angrymouth "-two"
extend @happy " students!\""

$ autoquote = True

oak @surprised "Well, yes, thirty-two is within the range of class sizes recommended by Dean--"

phobos @happy "Oh, splendid, it's exactly the illustrious Drayden I wanted to talk to you about." 
phobos @talkingmouth "You see, you see, of course you see, he's said that my darling niece, who had a very hard time last year, may rejoin the school if I could find a teacher that would take her into his homeroom."

oak @surprised sweat "Er..."

phobos @sadbrow talking2mouth "Why, think about it, Dear Sam Oak. Consider this. Who else could I go to? Kris?" 
phobos @happy "Hahaha!"
phobos @happy "No, no, no, such a suggestion is prepondorous." 
phobos @sadbrow talkingmouth "And since you weren't here last year, I'm certain you wouldn't have any of those {i}nasty{/i}, {i}awful{/i}, {i}distracting{/i} prejudices, no?"

oak @sadbrow sadmouth sweat "No...?"

phobos @happy "No! Splendid. I'll send her along for afternoon homeroom, then."
phobos @talkingmouth "Really, this is more of my generosity. She's a fantastic student. Quite simply the best. More importantly, this brings your class size up to thirty-three. A much better number, wouldn't you say?"

oak @closedeyes angryeyebrows sweat talking2mouth "I'm... not seeing how this number, thirty three, is any 'better' than--"

phobos @happy "Hahaha! Well, Dear Sam Oak, for a genius, you are surely bad at numbers. I'm sure you'll see it at some point."

oak -surprisedbrow -frownmouth -surprised frownmouth @talking2mouth "*Sigh.* Yes, I suppose. Let's discuss a few details first, if you wouldn't mind."

phobos @closedbrow talkingmouth "I have three minutes, perhaps."

hide phobos
hide oak 
with dis

narrator "Professor Oak and the strange man retreat to a corner of the room, discussing logistical arrangements. Slowly, the quiet whispers between your classmates become a dull hum."

show whitney uniform frownmouth:
    xpos 0.33

whitney uniform @talking2mouth "Hey, does anyone know that guy?"

show leaf uniform frownmouth:
    xpos 0.15 xzoom -1 

leaf @angrybrow talking2mouth "No, but I don't like him. Only {i}I{/i} get to run rings around Professor Oak."

show blue uniform frownmouth:
    xpos 0.85 xzoom -1

blue @talkingmouth "You couldn't run rings around an onion. If Gramps is letting this guy get what he wants, there's something in it for him. Or us."

show flannery tiredbrow frownmouth uniform behind blue:
    xpos 0.66 xzoom -1

flannery @talking2mouth "Dunno. He seemed pretty good before this guy showed up, but as soon as that chair guy started his fast-talk, the Prof kinda folded."

blue @angrybrow talkingmouth "He knows what he's doing! Just give him a second!"

show hilbert uniform with dis

hilbert @talkingmouth talkingmouth "You're biased."

blue angrybrow angrymouth "And you're stupid!"

hilbert @talkingmouth "...I feel like I should know this man. I'm sure I've seen his face before."

redmind @thinking "Hm..."

red @talkingmouth "I feel like we'd remember him if we knew him. There can't be too many people who use floating chairs to get around."

narrator "You wrack your brain for any sort of connection, but you're pretty sure you've never seen him before. Though... {i}something{/i} about him still feels oddly familiar..."

show flannery:
        xpos 0.66
        ease 0.5 xpos 0.85

show hilbert:
    xpos 0.5
    ease 0.5 xpos 0.75

show leaf:
    xpos 0.15
    ease 0.5 xpos 0.05

show whitney:
    xpos 0.33
    ease 0.5 xpos 0.15

show blue:
    xpos 0.85
    ease 0.5 xpos 0.95

if (GetRelationshipRank("Tia") > 0):
    show flattia with dis:
        alpha 0.5

    redmind @thinking "Wait..."

    pause 1.0

    show flatphobos with Dissolve(3.0):
        alpha 0.5 xpos 0.525 ypos 1.038

    redmind @surprised "Oh, shit. I'll never be able to unsee that."

    hide flattia 
    hide flatphobos
    with dis

    redmind @confusedeyebrows frownmouth "I wonder if he's also Altomarese?"

    pause 1.0

show phobos:
    xpos 0.333
show oak:
    xpos 0.66
hide leaf
hide hilbert
hide flannery
hide whitney
hide blue
with dis

oak angryeyebrows frownmouth @happybrow talkingmouth "Alright, students, let's continue the lecture. I have a lot of ground to make up, and I can think of no better way to do that than to talk about the ground itself. Terrains, that is. Now--"

phobos @happy "Oh, but Dear Sam Oak, where are your manners? You haven't introduced me to your delightful students."

pause 1.0

oak @talking2mouth "...Right you are. I suppose it slipped my mind."

$ BecomeNamed("Lawrence")

oak -angryeyebrows @talkingmouth "Students, this is Lawrence, a board member and--"

phobos @closedeyes talkingmouth "{w=0.333}Tut, {w=0.333}tut, {w=0.333}tut."

oak @surprised "Er... is there some sort of issue?"

phobos @sadeyebrows talkingmouth "An issue, Dear Sam Oak? No, no, perish the thought. I'm just concerned that if you, well, as you say, introduce me as 'Lawrence', your students may, well, be misled to think that that is my name."
phobos @happy "I'm sure you can see my concern, Dear Sam Oak. You're a professional yourself, no?"

oak @closedeyes talking2mouth "Perhaps I continue to fail to see the issue. I may recommend that you introduce yourself, then."

phobos @talkingmouth "Ah, yes, well... I understand that your time in Pallet Town left you relatively isolated from society. It's understandable that certain modes of address may {i}slip{/i} from your mind."
phobos @happy "Then, very well, it appears I have the pleasure of introducing myself to all these fine, fine, {i}fine{/i} young students."

pause 1.0

show oak surprisedbrow frownmouth with dis

phobos @sadbrow talkingmouth "If you wouldn't mind giving me some room to, ah, 'spread my legs', as it were? To coin a phrase. If you'll pardon the wit."

show oak closedbrow frownmouth sweat with dis

oak @talking2mouth "Excuse me."

hide oak with dis

pause 0.333

show phobos:
    xpos 0.333
    ease 0.333 xpos 0.5

phobos @talkingmouth "Well, well, well, Class 1-B! Such a pleasure it is to be before you here today. May I assume at least three of you recognize me?"

narrator "May and Dawn quickly share a glance, but no-one says anything."

phobos @happy "Ah, so wonderful! My legacy precedes. This is fun!~"
phobos @talkingmouth "For those who haven't had the pleasure, my name is Baron{w=0.333} Lawrence{w=0.333} Phobos{w=0.333} III."
phobos @happy "I am a collector, coordinator, philanthropist, and many more titles besides."
phobos surprised @winkbrow happymouth "But for those of you with short attention spans, you are permitted to call me Baron Phobos. I won't--"

show hilbert uniform with dis:
    xpos 0.75

pause 1.0

phobos -surprisedbrow -frownmouth -surprised @sadeyebrows happymouth "Talking? Wasn't it clear I was talking? Could you not {i}hear{/i} me talking?"

hilbert @talkingmouth "Where did you get your title from?"

phobos frownmouth @surprisedbrow sweat talking2mouth "Beg your pardon?"

hilbert @angrybrow talkingmouth "You said your name was {i}Baron{/i} Phobos. A baronship is a title of prestige, a title of nobility. Which lineage gave it to you?"

phobos -frownmouth @closedbrow happymouth "Ohoho! Such an intriguing question. You see, my prestigious bloodline is descended from {i}three{/i} separate royal families."

pause 1.0

hilbert @talkingmouth "So where did you get your title from? Was your father a baron?"

phobos @winkbrow talkingmouth "You're not paying attention, young man. As I said, I {i}am a baron.{/i} Why, I could easily lay claim to a title far higher than Baron, if I wished! I could be a King!"

narrator "[pika_name]'s Poké Ball suddenly rocks."

redmind @surprisedbrow frownmouth "Woah, there, buddy. Don't fall."

hilbert @talkingmouth "...Where are you from?"

phobos confusedeyebrows sweat frownmouth @happy "I am a proud Orange Islander, from Shamouti Island, though my citizenship is that of Kobukan, which--"

hilbert @talkingmouth "'No Title of Nobility shall be granted by Kobukan: And no Person holding any Office of Profit or Trust under it, shall accept of any present, Emolument, Office, or Title, from any King, Prince, or foreign State.'"
hilbert @closedbrow talkingmouth "Kobukan's constitution. Same as Unova's. You either are {i}not{/i} a baron, you are not a Kobukanian, or you are in violation of the law. Which is it?"

pause 0.5

phobos -confusedeyebrows -sweat @sad2eyes angryeyebrows talking2mouth "...Ah. I think I understand, now."
phobos @anger happy "You're a member of the 'Battle Team', aren't you?"

hilbert @talkingmouth "That doesn't answer my question."

phobos @happy "Sit down, friend."

pause 2.0

hide hilbert with dis

phobos @happy "I was a student here once upon a year. 'Oh, my beloved Kobukan, whose walls sing songs of ancient collections yet to be completed...'"
phobos @talkingmouth "That was the school song from back when I attended. Ah, but, you see, when I joined, I focused primarily on my work as a Coordinator."
phobos @happy "And the... 'Battle Team', at that time, well, they struck up quite a fuss. Why, bullies, louts, and thugs, the lot of them!"
phobos @talkingmouth "'Coordinators? Aren't they those girls who dress in skirts and dance with their Pokémon?' Yes, I heard such things thrice a week."
phobos @closedeyes talking2mouth "And, of course, the Battle Team constantly soaked up every other club's budget, such that the noble, fine, and elegant art of coordinating was entirely sublimated to... their inelegantable whims."

pause 0.5

phobos @sadbrow talkingmouth "I must confess that Kobukan's hallowed halls haven't always been a welcoming place for me. But I {i}did{/i} love it. I loved it greatly."
phobos @happy "I hope to show that love for Kobukan again. I've heard, for example, that the Coordinator Club has recently hired Lisia as its club advisor. A fantastic pick." 
phobos @winkbrow talking2mouth "I couldn't have chosen better. Aside from Champion Wallace Waters, of course."
phobos @winkbrow talkingmouth "Seems perhaps somebody forgot the obvious hire."

redmind @frownmouth confusedeyebrows "I... am not sure what he's saying anymore."

phobos @talkingmouth "So, yes, to make a long story short, I think it's fair to say that my history with the Battle Team may be a tad contentious, but I won't hold that against you, my friend." 
phobos @happy "Just do keep in mind my board membership affords me certain privileges."

pause 1.0

leaf uniform @talking2mouth "{size=30}...What does {i}that{/i} mean?{/size}"
leaf @angrybrow talking2mouth "{size=30}Swear to god, if he tries to mess with the Battle Team...{/size}"

phobos @happy "In any case, I believe that's all I need say for introductions today. Ta-ta, now!"
phobos @talkingmouth "Do give my beloved, darling, kindhearted niece a warm welcome, if you please. I'm sure you'll all be the best of friends."

hide phobos with Dissolve(3.33)

pause 1.0

show oak frownmouth with dis

oak @talking2mouth "Right. That was an unforeseen interruption. I apologize for that. I've got some more material to cover, so let's--"

narrator "Oak attempts to continue lecturing on important coverage moves, but is never truly able to regain his classroom from the many whispers that arise after the chairbound coordinator's interruption..."

jump homeroom1transition