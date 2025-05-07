label day010501:
$ timeOfDay = "Morning"

call calendar(1) from _call_calendar_26
$ calDate = calDate.replace(day=1, month=5, year=2004)

show morning at vspaz

pause 3.5

$ renpy.music.play("Audio/Morning_ambience.ogg", channel='crowd', loop=True, fadein=1.0)

scene dorm_A 
show screen currentdate
show calem closedbrow
with transeye2

$ renpy.pause(1.0, hard=True)

red @talkingmouth "...Morning, Calem."

pause 1.0

calem @talkingmouth "Hm."

red @happy "You seem nervous."

calem @talking2mouth "I... am. Tremendously so."

red @talkingmouth "It'll be alright, man. People love you. Even Roxanne thinks you'd be the best bet for Student Council President."

pause 1.0

calem @talking2mouth "Even so."

pause 0.5

calem -closedbrow @talking2mouth "[first_name]. Do you have any secrets?"

red @surprised sweat "H-huh? What...{w=0.5} what do you mean?"

calem @talking2mouth "I... {w=0.5}{nw}"
extend @sadbrow talking2mouth " No, ignore me. My words are spurred by nothing more noble than jealousy."

pause 0.5

calem @talking2mouth "I apologize for doubting you."

pause 0.5

red @sad "Um... are you going to ask about how I've been doing so well in the Student Council election, without having seriously tried?"

calem surprisedbrow frownmouth @surprised "Oh! Er..."

pause 0.5

calem -surprisedbrow -frownmouth -surprised @closedbrow talking2mouth "Well, yes. But, as I say, you have no obligation to answer the question. Especially as I have not, in actuality, asked it."

red @closedbrow talking2mouth "...Right."

calem @talkingmouth "I'm sure you understand how my mind could be led to wander. There's charisma, and then there's...{w=0.5}{nw}" 
extend @happy " Well, there's you."

red @thinking "[ellipses]"

calem @closedbrow talking2mouth "[first_name], you want to be a Pokémon Champion, yes?"

red @talkingmouth "That's right."

calem @talkingmouth "I want to be a diplomat."

red @surprised "Really?"

calem @talking2mouth "Yes. It's a job that often shelves the personal desires of the one who does it. A good diplomat should have the exact functionality of a phone--no more or less."

red @talkingmouth "I can see why membership in Kobukan's Student Council would be a very strong starting point, then."

calem @talkingmouth "My thoughts, as well. This is an international school that accepts powerful trainers from all across the globe."
calem @closedbrow talking2mouth "It's no exaggeration to say our classmates could very well end up leading the nations I hope to serve."

red @talkingmouth "...Why Kobukan, though? It's an amazing school, but mostly for Pokémon trainers, right?"

calem @talkingmouth "Hm. Pokémon training is a required part of the modern diplomat's duties, though. You may be surprised by how many international disputes are handled through Pokémon battles."

pause 1.0

red @confused "How many?"

calem @talking2mouth "{i}Several.{/i}"

red @surprised "Huh, that {i}is{/i} surprising."

calem @talkingmouth "The other reason I chose to attend Kobukan was to make connections. To sever myself from the past, and form new bonds with people that I was  inevitably going to... {w=0.5}well, {i}leave,{/i} one day."

red @talking2mouth "I get that. We're only here for a year, after all. We're probably not forming any lifelong bonds during that time."

calem @talkingmouth "...Mm."
calem @closedbrow talking2mouth "And yet, I find... that not only did someone from my past follow me here, but {i}you{/i} are here."

red @confused "Huh?"

calem @talking2mouth "I urge you not to take this as any sort of... {i}confession.{/i} But I find my enjoyment of your company extends beyond the simple joy of being with a friend."

red @embarrassedeyebrows embarrassedeyes poutmouth lightblush "Um..."

calem @closedbrow talking2mouth "I said {i}do not{/i} take it as a confession, [first_name]." 
calem @talking2mouth "What I'm trying to say is... I came to this school with the express purpose of not caring too deeply about anyone I met here."

pause 0.5

calem @talking2mouth "And yet, less than a month in, I have found my plan derailed."

pause 0.5

red @sadbrow talking3mouth "Sorry, Calem."
red @surprised "Wait, should I be apologizing for this? I don't... I don't really know what the protocol here is."

pause 0.5

calem @talkingmouth "Well. Neither do I."
calem @closedbrow talking2mouth "I still feel as though I should apologize, though. I said what I did just now only to explain my suspicion is a trap entirely of my own making. You've done nothing wrong."

red @happy "Good to hear. Now, shouldn't we get dressed?"

calem @talkingmouth "Yes. The voting will be held in the auditorium this afternoon, so I might suggest we Student Council hopefuls head there early, so that we might prepare the room."

red @talkingmouth "Oh, yeah? What kinda prep do you think it'll need?"

calem @closedbrow talking2mouth "I'm not certain. Perhaps none. Hopefully Roxanne will let us use her podium."
calem @happy "If not, we might have to fetch milk crates from the cafeteria."
calem @talkingmouth "Ready?"

red @talkingmouth "Ready as I'll ever be."

ethan @surprised "Woah, hold on!"

show ethan with dis:
    xpos 0.85

if (mayhaslarvesta):
    show brendan with dis:
        xpos 0.65

if (GetRelationship("Hilbert") == "Light"):
    show hilbert with dis:
        xpos 0.25

pause 0.5

ethan @happy "Did you forget about me? Hey, guys, good luck! I'll show up to the election to vote for you two."

if (mayhaslarvesta):
    brendan @talking2mouth "Yeah! You two super-deserve to be up there. I'm sure you'll make all kinds of cool choices."
else:
    narrator "You notice Brendan shifts a bit in his bed, but he doesn't get up."

if (GetRelationship("Hilbert") == "Light"):
    red @surprised "I'm surprised to see you're up so early, Hilbert. You know it's the weekend, right?"

    pause 0.5

    hilbert @closedbrow talkingmouth "I... slept well."

    pause 0.5

    red @happy "Good."

    hilbert @talkingmouth "I just wanted to say 'good luck.'"

    pause 0.5

    hilbert @sadbrow talkingmouth "That was it."

calem @talkingmouth "Thank you for your support. We'll see you this afternoon!"

red @talkingmouth "Let's go!"

if (pikachuobj in playerparty):
    $ playerparty.remove(pikachuobj)

stop music fadeout 1.5
queue music "audio/music/ViridianCity_Start.ogg" noloop
queue music "audio/music/ViridianCity_Loop.ogg"

scene blank2 with splitfade

pause 1.0

show academyhall with splitfade

pause 0.5

show calem with dis

calem @closedbrow talking2mouth "I wonder if perhaps we should drop by the infirmary. Jasmine and Grusha may be--"

show calem surprisedbrow frownmouth
show leaf happy:
    xpos 0.66
with vpunch

leaf @talking2mouth "[first_name]!"

red @happy "Hey, Leaf."

show calem -surprisedbrow -frownmouth -surprised with dis:
    ease 0.5 xpos 0.33

leaf -happy @talking2mouth "Are you excited? Ready to march on in to that auditorium and claim your role as the rightful dictator of Kobukan?"

red @talking2mouth "Absolutely. My first order of business: appoint toadies and yes-men to key positions in the school's Diet. Second order of business--order them to approve my appointment for life and beyond."

leaf @surprised "'And beyond'?"

red @happy "Sure! You don't think killing me would be enough to end my political aspirations, did you?"

show leaf surprisedbrow frownmouth with dis

calem @talking2mouth "Historically, that often works, actually."

show leaf -surprisedbrow -frownmouth -surprised with dis

pause 1.0

calem @surprised "N-not that I condone assassination as a viable method of transferring power to a new regime."

pause 0.5

calem @talkingmouth "I'm just saying. Historically. It works."

pause 1.0

red @talking2mouth "{size=30}Psst. Co-conspirator. I think there's a rebellion a-brewing. We should probably quash that.{/size}"

leaf @flirttalk "{size=30}Don't worry. I've got an inside man in the rebellion. We'll be ready for these schoolboys. They'll wet themselves with blood.{/size}"

calem @talkingmouth "Well put, Inspector. But who, exactly, is this inside man?"

show serena with dis:
    xpos 0.25

show calem surprisedbrow frownmouth:
    ease 0.2 xpos 0.5 xzoom -1

show leaf:
    ease 0.5 xpos 0.75

serena @happy "{i}Bonjour!{/i}"

calem -surprisedbrow -frownmouth -surprised @talkingmouth "I might have guessed."

serena @talkingmouth "Are you and [first_name] going to the auditorium?"

calem @talkingmouth "{i}Les grands esprits se rencontrent.{/i} Or so it would seem, if you'll pardon the self-aggrandizement. Yes, we're heading there now."
calem @talking2mouth "We were planning on just going to drop by the infirmary. Just in case Jasmine and Grusha are... incapacitated, you know."

serena @talkingmouth "That seems like a lovely idea. Why don't we go?"

calem surprisedbrow frownmouth @surprised "Eh?"

serena @talkingmouth "Come along, Calem."

show calem: 
    ease 0.5 xpos 0.6
    pause 0.3
    ease 1.0 xpos -0.2

show serena:
    ease 0.5 xpos 0.55
    pause 0.3
    ease 1.0 xpos -0.2

pause 2.0

red @talkingmouth "Your work, I assume."

show leaf:
    ease 0.5 xpos 0.5

leaf @closedbrow talkingmouth "I am {i}shocked{/i} and {i}offended{/i}, good Sir."

red @talkingmouth "Far be it from me to cast doubts on the virtue of a lovely young lady."

pause 0.5

show leaf surprisedbrow frownmouth with dis

red @angrybrow talking3mouth "But that's not what I'm doing."

show leaf angrybrow happymouth with vpunch

leaf @talking2mouth "You jerk!"

red @happy "Hey, easy with the punches, there. You could break my arm, and I'm going to need that to shake hands and kiss babies and junk."

leaf -angrybrow -happymouth @talking2mouth "I really never would've pegged you as a politician, y'know."

red @talkingmouth "Yeah, I never really expected to be pegged, much less as a politician."
red @happy "But, hey, y'know, life's all about new experiences. If I suck at it, I at least know I was trying to help people."

leaf @closedbrow talking2mouth "Right. I know people have asked this before, but--what, again, are you going to help people with?"

red @happy "I'm just kinda hoping I figure that one out if I get elected."

leaf @talkingmouth "{i}When{/i} you get elected."

red @talkingmouth "Hey, arrogance doesn't beget strength. Alder said that. I assume it applies to political strength, too."

leaf @happy "You got this, [first_name]. I believe in you."

red @happymouth "Thanks, Leaf. That really means a lot."

leaf @talking2mouth "So. Hug for luck?"

if (HasEvent("Leaf", "RejectedConfession")):
    leaf @sadbrow happymouth "Totally platonic, friend hug? For good luck, with absolutely no strings attached? As I am being {i}very{/i} respectful of your decision to turn me down earlier?"

else:
    leaf @flirttalk "A totally chaste, pre-date hug, with absolutely no expectations or handsiness?"

red @happy "Totally."

show leaf closedbrow bigblush:
    ease 0.5 ypos 1.2 zoom 1.3

pause 2.0

show leaf surprisedbrow frownmouth with dis

pause 2.0

show leaf closedbrow -bigblush fullblush talkingmouth with dis

pause 2.0

red @confused "Uh... we almost done?"

pause 0.5

leaf @talking2mouth "...You're hard."

pause 1.0

red @confused "I beg your pardon?"

show leaf -closedbrow -fullblush blush -talkingmouth with dis:
    ease 0.5 ypos 1.0 zoom 1.0

leaf @talkingmouth "I thought you'd be soft and huggable. But your chest is hard."

red @talkingmouth "Oh, yeah, I work out, sometimes. Maybe you've noticed?"

leaf @talkingmouth "You were totally tensing your muscles."

red @talkingmouth "Maybe a little bit."

leaf -blush @sarcastic "Well, I guess it sucks for you I don't like muscles."

pause 0.5

red @confused "Wait. Really? I can't tell if this is a bit, or if you genuinely don't like muscles."

leaf @talking2mouth "Yeah, no, I'm serious."

red @happy "Is that why you're so easily winded? Why you never work out, and don't want to go swimming? You don't want to build muscles yourself?"

pause 0.5

leaf @talkingmouth "Well. That's it. A little bit."

red @talkingmouth "You really don't have to worry about swelling into some sort of beefcake, Leaf. Developing muscles takes sustained effort. It's not the sort of thing you can 'accidentally' into."

leaf @talking2mouth "I'll take your word for it."

red @happy "Well, you can--"

show academyhall
show leaf frownmouth
with vpunch

$ first_nameupper = first_name.upper()

blue frownmouth @angry "[first_nameupper]!"

red @closedbrow talking2mouth "Great."

show blue with dis:
    xpos 0.25

show leaf:
    ease 0.5 xpos 0.75

blue @talkingmouth "What are {i}you{/i} doing here?"

leaf @talking2mouth "Uh, I'm wishing [first_name] good luck before he gets elected Student Council President."

red @sweat happy "I'm not actually aiming for President..."

blue @closedbrow talkingmouth "Pah. Student Council?"
blue @talkingmouth "Sounds like lame nerd stuff. You should just quit."

red @confused "What?"

blue @talkingmouth "Yeah, there's no way anyone'll vote for you. You should just withdraw. Don't even show up to the election."

red @talking2mouth "Uh... no, I won't be doing that."

leaf @angrybrow talking2mouth "Yeah, and what do you mean 'no-one will vote for him'? You realize he's, like, really popular, right?"

blue "{w=0.5}.{w=0.5}.{w=0.5}."

blue @talkingmouth "Yeah, but you think you'll be popular after you win? C'mon, everyone hates politicians. You won't have any idea what to do, you'll screw up, and everyone will hate you."

red @confused "I mean... that's possible. Unlikely, though."

blue @angry "{w=0.5}.{w=0.5}.{w=0.5}."
blue @closedbrow angrymouth "Look, just don't do it, alright? You're already on the Battle Team, and you're doing alright there."
blue @talkingmouth "You don't have enough time. You need to just focus on one thing."

red @closedbrow talking2mouth "Yeah, uh, thanks for the concern, but you can shove off."

blue @sad "{w=0.5}.{w=0.5}.{w=0.5}."
blue @angry "I'm {i}telling you{/i} to butt out."

red @confused "Yeah? Well, I'm just confused as to why you're doing this now. You know I've been campaigning for a month now. I've had posters up all around the school for two weeks."
red @talking2mouth "I mean, heck, you were in homeroom when your grandfather told everyone to show up to the election."

blue @angry "It {i}doesn't{/i} matter why I'm telling you to butt out! Just do it! Don't go to that damn election! Don't give your damn speech! Just scratch your name off the ballot and sleep the day away."

red @confused "...Give me one good reason."

pause 1.0

blue @talkingmouth "Leaf. Get lost. [first_name] and I are going to settle things."

show blue surprisedbrow frownmouth with dis

leaf @sarcastic "Oh, wow, that's such a generous offer, but you know, I don't think I'm going to listen to someone who sucks toes."

blue @talkingmouth "Wh-what? I--{w=0.5} no, I don't, I--{w=0.5} {i}what?{/i}"

pause 0.5

redmind @thinking "Impressive. She {i}completely{/i} shut him down. I need to remember that one."

show showdown with Dissolve(1.0)

blue -surprisedbrow -frownmouth -surprised closedbrow angrymouth "Just... Just get out of here."

leaf @talking2mouth "Uh, no. Kinda thought I told you that one. Do I need to explain the concept of taking 'no' for an answer?"

if (HasEvent("Leaf", "RejectedConfession")):
    pause 0.5

    leaf @closedbrow talking2mouth "Yes, [first_name], I'm aware of the hypocrisy."

else:
    leaf @sadbrow talking2mouth "If I do, I really feel sorry for your first boyfriend."

blue @angry "Just... I need to talk to [first_name] {i}privately{/i}! Just get out of here!"

leaf @talking2mouth "No! I'm here to {i}support{/i} [first_name]. That means I have dibs on his company, as opposed to you, who's just here to tear him down!"

blue @talkingmouth "You idiot! I'm trying to {i}protect{/i} him!"

leaf @talking2mouth "Protect him from what? Having a sense of self-esteem?!"

blue @talkingmouth "You don't know a damn thing about him! You only met him a month ago!"

leaf @talking2mouth "I know him well enough to know that he can't {i}stand{/i} you! So why don't {i}you{/i} 'smell us later' and get out of here?!"

narrator "You suddenly become aware that you are no longer a part of this conversation about you."

blue @talkingmouth "Please! He's probably sick to death of you constantly hanging around him, he's just too much of a wimp to say anything!"

if (HasEvent("Leaf", "RejectedConfession")):
    leaf "...No, you're an idiot. I asked [first_name] out, and he said no, but he set up a boundary, which I'm respecting! Unlike you, who has no respect for {i}anyone's{/i} boundaries!"

else:
    leaf "Shows what you know, [blue_name]! We're going on a date on Sunday!"

show showdown with vpunch

show blue sad:
    ease 0.5 ypos 0.9 zoom 0.8

blue @surprised "What?"

leaf @talking2mouth "You heard me!"

hide showdown with Dissolve(2.0)

blue @talkingmouth "You don't...{w=0.5} You...{w=0.5} Look,{w=0.25} {i}I'm trying to--{/i}"

pause 1.0

red @confusedeyebrows "{w=0.5}.{w=0.5}.{w=0.5}."

blue -sad "{w=0.5}.{w=0.5}.{w=0.5}."

blue @angry "Fine! I'll {i}force{/i} you to quit! Get out your Poké Balls!"

red @closedbrow talkingmouth "Ugh... this is the way it always ends up, isn't it?"

leaf @surprised "Here? Are you crazy?"

blue @talkingmouth "I'm stopping you from running in that damn election right here, right now! You have enough damn wins! Just give this one up!"

red @talking2mouth "Yeah, you know I can't do that."

leaf @sadbrow talking2mouth "This is a non-combat zone..."

red @closedbrow talking2mouth "...We'll make this quick. We'll be done before any teachers show up."

leaf @surprisedbrow talkingmouth "We?"

red @happy "Sure! You didn't think I was going to have a battle in front of you and not invite you, huh?"

blue @angry "It doesn't matter! I'll beat both of you! Now take your beating like a man... and a woman!"

python:
    trainer1 = MakeRed()
    trainer2 = MakeTrainer("Blue", TrainerType.Enemy)
    trainer3 = MakeTrainer("Leaf", TrainerType.Ally)

call Battle([trainer1, trainer2, trainer3]) from _call_Battle_70
$ battlehistory["Blue4"] = _return

queue music "audio/music/ViridianCity_Start.ogg" noloop
queue music "audio/music/ViridianCity_Loop.ogg"

show blue angry at leftside
show leaf frownmouth at rightside
with dis

if (WonBattle("Blue4")):

    $ ValueChange("Leaf", 3, 0.75)

    leaf @closedbrow talkingmouth "Hm. When {i}will{/i} you learn?"

else:
    blue "There. I beat you! Now, you can't go to the election!"

    pause 1.0

    red @talking2mouth "I mean, I'm still going to."

    $ ValueChange("Blue", -1, 0.25)

    blue "WHAT?!"

    red @talkingmouth "Yeah. You beat me. Good job. But, like, you can't stop me from just walking down this hallway, unless you want to physically send your Pokémon to stop me."
    red @closedbrow talking2mouth "Which is, like, an {i}actual{/i} crime. So, y'know, good job for beating us. It doesn't {i}do{/i} anything, though."

blue sad "But... you... I..."

pause 0.5

blue angry "{i}This is {b}your{/b} fault.{/i}"

hide blue with Dissolve(2.0)

red @confused "...Hm."

leaf @talking2mouth "...Hey. Are you okay?"

red @closedbrow talking2mouth "Yeah. It'd take more than [blue_name] being a jerk to get me off my game."

leaf -frownmouth @talking2mouth "Right? If that was all it took, you never would've left Pallet Town."

red @closedbrow talking2mouth "Right. ...Oh, hey, I just remembered. What did Janine want to talk to you about yesterday?"

leaf @talking2mouth "Oh, nothing serious. Just a weird little thing about my Dratini. I'll tell you about it tomorrow, in the city. You're busy now, right?"

red @talkingmouth "Yeah, I should be going to the auditorium now."

leaf @talkingmouth "Alright. See you later?"

red @happy "You sure will. Don't forget to vote."

leaf @talking2mouth "Mmm, maaaaybe. Can't say I'll vote for {i}you{/i} though."

red @talkingmouth "Dang. Should've campaigned harder. The Leaf lobby was critical."

leaf happy "Hah, hah! I'll see you later, [first_name]!"

hide leaf with dis

narrator "You wait around in the hallway for Calem's return for a bit longer."

pause 2.0

red @closedbrow talking2mouth "...This is boring."

pause 1.0

narrator "Since he doesn't appear to be coming back, you decide to head to the auditorium."

scene orientation 
show auditorium_cover
show serena:
    xpos 1.0/6.0
show cheren smilemouth:
    xpos 2.0/6.0
show calem:
    xpos 3.0/6.0
show jasmine:
    xpos 4.0/6.0
show grusha:
    xpos 5.0/6.0
with splitfade

calem @talking2mouth "...{size=25}in{/size} {size=30}essence,{/size} {size=35}we{/size} {size=40}want{/size} to portray ourselves as a unified force."
calem @surprisedbrow talking2mouth "Oh?"
calem @talkingmouth "Hello, [first_name]. Good to have you. Apologies for starting the meeting early, we weren't sure how long Leaf was going to have you."

red @talkingmouth "It's alright. What're we doing?"

jasmine @talkingmouth "Discussing our upcoming speeches."

serena @talkingmouth "Calem was just impressing on us the importance of presenting a unified front."

calem @talkingmouth "Yes. There's only six of us. More than last year's Student Council, but not too many to be functional."
calem @talkingmouth "If none of us disagree with each other on any points, then there is absolutely no reason we shouldn't all be elected."
calem @closedbrow talking2mouth "However, if any of us {i}do{/i} disagree on each other's positions, we should make our deals now."
calem @talkingmouth "The absolute worst thing we could do for our chances is get into an argument onstage."

serena @talkingmouth "I'm certain that there will be no notable disagreements between us. Our policies are so uncontroversial, after all."

pause 1.0

redmind @thinking "...Everyone is side-eyeing Cheren."

grusha @confusedeyebrows talking2mouth "Cheren, you've been pretty silent."

cheren @happy "Look who's talking, Grusha!"
cheren @sadmouth "Yes, I've been silent. I simply don't have anything to contribute here. Calem is leading these proceedings well, and I don't object to any of the positions you hold."

jasmine @happy "Oh, how good to hear. And may I say that you're looking very sprightly?"

cheren @happymouth "Thank you. I have found a new resolution, and was finally able to sleep well, after almost a month."

jasmine @talkingmouth "Brilliant."

calem @talking2mouth "Apologies for harping on about this point, but you're certain that you're not going to bring up any issues that we might be obligated to disagree with, Cheren?"
calem @talking2mouth "Roxanne made quite clear that anything that interferes with the school's flow of cash would damage our cause significantly."

cheren @happy "Don't worry. I assure you, I'll be quite restrained. Perhaps another could fight for my causes later on in the year."

calem @closedbrow talkingmouth "Hm. Well, if that's that, then... I suppose the only thing we need to figure out is who will talk first."

serena @talkingmouth "Calem, why don't you introduce us? You can give an opening speech, we'll all discuss our goals for the upcoming year, then you can introduce your goals, with a closing speech."

calem @talking2mouth "I've no objections. Anyone else?"

pause 2.0

calem @closedbrow talkingmouth "I suppose the motion passes, then. {size=30}Hm. That's fun to say.{/size}"
calem @talkingmouth "So, if I'm beginning, then would you like to follow me, Serena?"

serena @talkingmouth "Always."

jasmine @sadbrow talkingmouth "If it's not too much trouble, I might suggest I go after Calem, actually."

serena @surprised "Oh?"

jasmine @talkingmouth "I think it might be most effective if we give our speeches in order of how excited the audience will be about them, so that we end on a high note."

pause 1.0

jasmine @sweat talkingmouth "It's, ah...{w=0.5} I know my positions and goals are important, but I'm trying to help a small minority that exists in the future. I can't imagine people will be overly excited about my speech."

calem @closedbrow talking2mouth "Hm, that makes sense. If we're going in order of voter appeal, then, perhaps we should go Me, Cheren, Jasmine, Serena, Grusha, [first_name], then me again for the wrap-up?"

pause 1.0

cheren @sadmouth "That certainly seems fine to me."
cheren @happymouth "Though I anticipate the crowd to go wild when I mention the five-ply toilet paper. Perhaps you should save that for your closing speech, Calem?"

calem @happy "Appreciated, but no, you can keep that one."

cheren @happy "Very well."

redmind @happy "Glad to see Cheren seems to be feeling better."

grusha @confusedeyebrows talking2mouth "...Not that I really care, but why are you all interested in the Student Council?"

jasmine @angrybrow poutmouth "Grusha!"

grusha @angrybrow talking2mouth "What? I'm trying to start a conversation! We've got a couple hours to kill, and I don't want to spend that time just going in circles about how we're going to get elected."
grusha @closedbrow talking2mouth "Literally all we have to do is go up there and not fall off the stage, and we'll be fine."

jasmine @talking2mouth "...There's a bit more to it than that."

calem @talkingmouth "It's alright, Jasmine. I can understand Grusha's impatience. I think we're all nervous about how things are proceeding. A word that comes to mind is 'glacially.'"

grusha @closedbrow talking2mouth "Things definitely aren't flying along."

pause 1.0

redmind @confusedeyebrows frownmouth "Was that a type pun?"

calem @talkingmouth "In any case, I aim to become an international diplomat after graduation, so Student Council, a quasi-governmental position that has authority over a great number of international students, seems like valuable 'job experience.'"

grusha @closedbrow talking2mouth "Hm."

jasmine @talkingmouth "I think everyone knows why I'm here. I just want to make sure the people who get into this school in the future receive the same kindness and support I have."

cheren @sadmouth "As was always the case, I want to modernize and uplift Kobukan Academy's staff, systems, and students."

red @talkingmouth "What Cheren said. Except I'd phrase it as 'I just wanna help people.'"
red @sweat sad2eyes talking2mouth "And, well, everyone kept telling me to do it, so..."

grusha @closedbrow talking2mouth "Personal reasons."

pause 1.0

jasmine @sweat talking2mouth "Serena?"

serena @surprised "Oh! Well, um..."

pause 1.0

serena @blush talkingmouth "Personal reasons."

calem @talkingmouth "What a mystery we are."
calem @closedbrow talkingmouth "Perhaps we'll have the time, and trust, necessary to confess fully to each other after we've been elected."

serena @poutmouth "{size=30}I'm ready to confess now, actually.{/size}"

jasmine @talkingmouth "Well, what should we do for now?"

grusha @talkingmouth "I'm starved. Skipped breakfast for this. Anyone want to head to the cafeteria?"

cheren @happy "A splendid idea. Let's go."

calem @talkingmouth "After we do that, we should probably don our school uniforms."

serena @surprised "Eh?"

calem @talkingmouth "What we want to emphasize, more than anything else, with this Student Council, is that we're working together. We're a united front."
calem @talking2mouth "I think, if we all wear our uniforms, it will emphasize that... well, uniformity."

serena @poutmouth "Oh."

jasmine @sadbrow talkingmouth "Do you have a problem, Serena?"

serena @closedbrow sadmouth "No, I just thought this outfit was rather cute."

calem @happy "It most certainly is. But if you can sacrifice your impeccable fashion sense for the rest of the council, we'd be very appreciative."

show grusha happy 
show calem happy
show cheren happy
show jasmine happy
with dis

serena sadbrow happymouth "Oh, alright, then."

scene black with Dissolve(2.0)

narrator "You head to the cafeteria together and eat a hearty breakfast."

calem "{w=0.5}.{w=0.5}.{w=0.5}."

grusha @closedbrow talking2mouth "Why are you staring?"

calem @closedbrow talking2mouth "Apologies. It's just... are you going to keep that scarf on for our entire meal?"

grusha @confusedeyebrows talking2mouth "That was the plan, yeah."

calem @talkingmouth "Are you planning on wearing it over your uniform, too?"

grusha @closedbrow talking2mouth "Pretty much."

calem @talkingmouth "Mm. Alright, then."

$ HealParty()

narrator "Eventually, the Student Council hopefuls start leaving. You head back to your dorm to grab your uniform, head to the student center to heal your party, then head back to the auditorium."
stop music fadeout 1.5
play music "audio/music/hoenn_start.ogg" noloop 
queue music "audio/music/hoenn_loop.ogg"
queue music "audio/bigcrowdloop.ogg" fadein 3.0 channel "crowd"

show noon at vspaz

pause 3.5

$ timeOfDay = "Noon"

scene orientation
show auditorium_cover
show serena uniform:
    xpos 1.0/6.0
show cheren uniform smilemouth:
    xpos 2.0/6.0
show calem closedbrow uniform:
    xpos 3.0/6.0
show jasmine uniform:
    xpos 4.0/6.0
show grusha uniform:
    xpos 5.0/6.0
with splitfade

narrator "By the time you arrive back at the auditorium, it's full of people milling around and talking animatedly."
narrator "Somehow, banners featuring the candidates have been put up. The entire room has the atmosphere of a party, moreso than a formal political event."

pause 1.0 

grusha @closedbrow talking2mouth "Good turnout."

calem @talking2mouth "Mm. Commendations to you, [first_name]. Your idea to run a voting campaign was clearly a success."

red uniform @happy "Hey. All I did was suggest it. You and Serena figured out how to make it happen."

calem @talking2mouth "Even so. Credit where it's due."

pause 0.5

jasmine @talkingmouth "Nervous, Calem?"

calem -closedbrow @talking2mouth "Quite so. This event could very well decide the trajectory of my future career. Possibly even multiple of our careers, depending on where you all want to be in the future."

pause 0.5

calem @talkingmouth "So... yes, nervous. But {i}excited{/i}, in equal measure. It's been a pleasure to go through this with all of you. Hopefully our efforts have paid off."
calem @talkingmouth "Especially you, Cheren. I'm sorry not everything went as you wanted it, but you set the pace for us, and your passion spurred us along. I'm grateful for that."

cheren @sadmouth "{w=0.5}{cps=30}It is my pleasure to help in any way I can.{/cps}"

show gardenia happy:
    xpos -0.1 xzoom -1 ypos 0.7
    ease 0.5 xpos 1.0/7.0 ypos 1.0
show serena surprisedbrow frownmouth:
    ease 0.5 xpos 2.0/7.0
show cheren surprisedbrow frownmouth:
    ease 0.5 xpos 3.0/7.0
show calem surprisedbrow frownmouth:
    ease 0.5 xpos 4.0/7.0
show jasmine surprisedbrow frownmouth:
    ease 0.5 xpos 5.0/7.0
show grusha surprisedbrow frownmouth:
    ease 0.5 xpos 6.0/7.0

gardenia @talkingmouth "Hey! Happy election day, you guys! Want to show your support for the candidates? Just buy these unoffical candidate badges!"

narrator "Gardenia brandishes a handful of pins, bearing slogans such as 'Calem Loves Clubs,' 'Serena's Squad,' 'Jasmine's no Joke,' and 'Cheren.'"

gardenia -happy @talkingmouth "Just $300! And{w=0.5} if{w=0.5} you{w=0.5}..."

show serena angrybrow poutmouth
show cheren angrybrow
show calem angrybrow
show jasmine angrybrow poutmouth
show grusha angrybrow

gardenia @talking2mouth "...Ah."

pause 1.0

gardenia @happy "What a {i}wonderful{/i} opportunity! I was just looking for you guys!"

show gardenia happy:
    ease 0.5 xpos 4.0/7.0
show serena surprisedbrow frownmouth:
    ease 0.5 xpos 1.0/7.0
show cheren surprisedbrow frownmouth:
    ease 0.5 xpos 2.0/7.0
show calem surprisedbrow frownmouth:
    ease 0.5 xpos 3.0/7.0
show jasmine surprisedbrow frownmouth
show grusha surprisedbrow frownmouth
with dis

gardenia @talkingmouth "So, I've taken the liberty of creating official unofficial badges supporting you guys, basically acting as a {i}pro bono{/i} campaign manager."

pause 1.0

show serena angrybrow poutmouth
show cheren angrybrow
show calem angrybrow
show jasmine angrybrow poutmouth
show grusha angrybrow

pause 1.0

gardenia -happy @happybrow talkingmouth "No, no, I won't take any payment. I insist. I do this out of love of democracy."
gardenia @angrybrow talkingmouth "However! I think we could {i}massively{/i} expand our operations in a mutually profitable way with just a bit of buy-in from you guys."

red @confused "I'm interested."

show serena -angrybrow -poutmouth
show cheren -angrybrow
show jasmine -angrybrow -poutmouth
show grusha -angrybrow
with dis

calem -angrybrow @closedbrow talkingmouth "[first_name]..."

gardenia @happy "Awesome!"
gardenia @angrybrow happymouth "See? Now, {i}this{/i} is a candidate with a head on his shoulders."
gardenia @talking2mouth "All I need is a little endorsement of these pins. Then I could advertise them as Official Unofficial Candidate Badges!"
gardenia @talkingmouth "I've done a bit of market research, and I predict that I could see an increase of profits by 34%% if you give me the go-ahead!"

red @surprised "All this for 34%%?"

gardenia @talkingmouth "Hey, it takes me, like, five minutes to get your endorsement. I'm still earning money per-hour right now."
gardenia @sad "But the time I'm spending trying to convince you will stop being worth it, as compared to potential extra profit, at the seven-minute mark, so I'm kinda going to have to rush you along."

pause 1.0

grusha @closedbrow talking2mouth "Yeah, sure, go ahead. Need me to sign anything?"

jasmine frownmouth @surprised "Grusha!"

show gardenia happy:
    ease 0.5 xpos 5.0/7.0
show jasmine:
    ease 0.5 xpos 4.0/7.0

gardenia @talkingmouth "Yeah, if you could just sign here..."

serena @sadbrow talkingmouth "I don't particularly... think there's anything {i}too{/i} wrong with it, Calem..."

calem @closedbrow talkingmouth "I'm always leery of allowing money to be involved in politics, but... well, I don't see anything {i}too{/i} offensive about the idea as a whole, either..."

grusha @confusedeyebrows talking2mouth "Stop being so serious. It's free money, and this is a school's Student Council. We're not going to break the democratic system by endorsing some badges with our faces on them."

jasmine @sweat talking2mouth closedbrow "I'm not sure..."

show gardenia:
    ease 0.5 xpos 0.5 ypos 1.2 zoom 1.3
show serena:
    ease 0.5 xpos 1.0/6.0
show cheren:
    ease 0.5 xpos 2.0/6.0
show calem:
    ease 0.5 xpos 3.0/6.0
show jasmine:
    ease 0.5 xpos 4.0/6.0
show grusha:
    ease 0.5 xpos 5.0/6.0

gardenia @talkingmouth "Well, what about you, [first_name]? You want a little cash? If you just give me your endorsement, I'll give you a nice $500!"
gardenia @talkingmouth "{size=30}Orrrr... if you've got the guts and brains to think {i}really{/i} long-term... I'll consider your endorsement worth a $1,000 investment in my side projects."

red @talkingmouth "It's always a hustle with you, isn't it?"

gardenia @talkingmouth "It's kinda like breathing, for me. 'If you're not hustling, then you're losing,' is my mantra."

red @confused "Sounds like an incredibly stressful life. {w=0.5}That being said..."

menu:
    "I'll take $500 now.":
        $ AddEvent("Gardenia", "EndorsedCash")
        $ ValueChange("Gardenia", 2, 0.5)
        $ money += 500
        gardenia @happy "Pleasure doing business with you!"

    "I'll take the $1000 investment.":
        $ AddEvent("Gardenia", "EndorsedInvestment")
        $ ValueChange("Gardenia", 3, 0.5)
        $ InvestmentChange(1000, True)
        gardenia @happy "Pleasure doing business with you!"

    "At $300 a badge, I think you can afford to pay a bit more.":
        gardenia surprised "Eh?"

        red @talking2mouth "You were selling the badges for $300. Based on the materials--the cardboard, the pins, the laminate--I can't imagine they cost any more than $100 to manufacture per unit."

        red @confused "Assuming you're making them yourselves, the largest cost is probably labor. And I could, at the very least, pin these together in thirty seconds each." 
        red @talking2mouth "Thirty seconds per $200 profit margin seems like it should leave you with plenty of room to pay a tad bit more than just under the cost of two badges."

        pause 1.0

        gardenia -surprisedbrow -frownmouth -surprised @angrybrow talkingmouth "I don't like savvy customers, y'know. But I respect that. So, sure, I'll double my offer. $1000 right now, or a $2000 investment."

        menu:
            "I'll take $1000 now.":
                $ AddEvent("Gardenia", "EndorsedCash")
                $ ValueChange("Gardenia", 1, 0.5)
                $ money += 1000
                gardenia @happy "Pleasure doing business with you!"

            "I'll take the $2000 investment.":
                $ AddEvent("Gardenia", "EndorsedInvestment")
                $ ValueChange("Gardenia", 2, 0.5)
                $ InvestmentChange(2000, True)
                gardenia @happy "Pleasure doing business with you!"

            "Is that really the best you can do?":
                $ ValueChange("Gardenia", -1, 0.5)
                gardenia frownmouth @angry "Uh, yeah. Negotiations are {i}over{/i}. Take it or don't."

                menu:
                    "I'll take $1000 now.":
                        $ AddEvent("Gardenia", "EndorsedCash")
                        $ ValueChange("Gardenia", 1, 0.5)
                        $ money += 1000
                        gardenia -frownmouth @happy "Pleasure doing business with you!"

                    "I'll take the $2000 investment." if (investment < 18000):
                        $ AddEvent("Gardenia", "EndorsedInvestment")
                        $ ValueChange("Gardenia", 2, 0.5)
                        $ InvestmentChange(2000, True)
                        gardenia -frownmouth @happy "Pleasure doing business with you!"

                    "I'm not doing this.":
                        gardenia @sad "Fine. You made it such a hassle, anyway. It's like trying to squeeze blood from a stone..." 
            
            "I'm not doing this.":
                $ ValueChange("Gardenia", -1, 0.5)
                gardenia @sad "Boo. You're no fun."

    "I'm not doing this.":
        $ ValueChange("Gardenia", -1, 0.5)
        gardenia @sad "Boo. You're no fun."

show blank2 
hide gardenia
with Dissolve(2.0)

narrator "Gardenia does her business with the other student council hopefuls who are willing to endorse her badges, then skips off happily before anyone can think of the long-term consequences of their actions."

show jasmine -frownmouth

narrator "Slowly, the afternoon approaches, as the moment for the speeches to be given arrives."

show afternoon at vspaz

pause 3.5

$ timeOfDay = "Afternoon"

hide blank2 with Dissolve(1.0)

stop music fadeout 10.0 channel "crowd2"

narrator "The students begin to quiet as they look at you expectantly."

pause 2.0

red @confused "Well... shall we?"

calem @surprised "Er... truth be told, I'm not quite sure what to..."

show calem surprisedbrow frownmouth
show cheren surprisedbrow frownmouth
show grusha surprisedbrow frownmouth
show serena surprisedbrow frownmouth
show jasmine surprisedbrow frownmouth
with dis

"{color=#a2254b}???{/color}" "\"Ahem!\""

pause 1.5

hide calem
hide cheren
hide jasmine
hide grusha
hide serena
with dis

pause 1.0

show roxanne uniform happy
show brawly uniform happy at leftside
show falkner uniform happy at rightside
with dis

serena uniform @happy "Roxanne!"

show brawly -happy
show falkner -happy
with dis

roxanne -happy @happy "I am so happy to see such a splendid turnout for your election. Whatever the result, whoever is elected, you have all done a great thing for the student body's representation already."

brawly @surprised "Yeah, bros! But how'd you do it? The auditorium's, like, full up! But when we ran, there were only, like, sixty or seventy people there!"

cheren uniform @disappointedmouth "[first_name] had the genuinely inspired idea to have part of our personal campaigns be a more general encouraging of participation in the voting process."

falkner @talkingmouth "That's a good idea. Perhaps we should have done something similar back in the day."

roxanne @talkingmouth "It's undeniable that your efforts have already endeared you to the student body. I have a good feeling about your council, Calem."

calem uniform @surprised "{i}My{/i} council... well, we'll see. We've yet to be elected."

pause 1.0

calem @talkingmouth "Speaking of which. What, exactly, should we do? Just... head on up to the stage?"

roxanne @talkingmouth "Yes, that would work... {w=0.5}{nw}"
extend @sadbrow talkingmouth "But, would you allow us one last indulgence?"

serena uniform @surprised "Indulgence?"

falkner @closedbrow talkingmouth "You do not know what mark we have had on Kobukan."
falkner @sad "Admittedly, it was not a large one."

brawly @sadbrow happymouth "But we still like the old school, y'know? And all our old friends left a month ago. So we... like... we wanna say goodbye."

falkner @closedbrow happymouth "Of course, Roxanne's preferred method of saying 'hello' and 'farewell' is speeches. While Brawly and I's preferred method is... {w=0.5}{nw}" 
extend @happy "Well, listening to Roxanne's speeches."

roxanne @sadbrow talkingmouth "Falkner..."

falkner @talkingmouth "I'll miss them, Roxanne. And I'll miss the humor and enthusiasm you brought to the job, Brawly. I hope to visit you two in Hoenn some day."
falkner @closedbrow happymouth "Perhaps if I am unable to become a police officer in Violet City, I'll move to Hoenn and try again. We might meet again, that way."

brawly @sadbrow talkingmouth "Aw, man. Is it bad if I kind of want you to fail, just so that can happen?"

falkner @closedbrow talkingmouth "Not at all. I rather do, as well."

roxanne @closedbrow talking2mouth "Of course, there's no chance of that. In one year, I've never seen you panic, exaggerate, lie, or abuse your powers."
roxanne @happy "There's quite legitimately no-one better suited to be a police officer than you, Falkner."
roxanne @sadbrow happymouth "Much as I might be tempted to selfishly root for your failure, too."

pause 1.0

cheren uniform @closedbrow sadmouth "{i}Ahem.{/i}"

roxanne @talkingmouth "Oh, sorry. So, yes, if you would permit it, we would like to give our farewell speech to open the event." 
roxanne @happymouth "Of course, our farewell speech will contain commendations of your virtue. Your, plural, naturally."

calem @talkingmouth "I've no objections. Council?"

serena uniform @talkingmouth "{i}Je vous en prie.{/i} Please, go ahead."
grusha uniform @closedbrow talking2mouth "Yeah, fine."
cheren uniform @happymouth "Why should I fight that?"
jasmine uniform @happymouth "It's a lovely idea."
red uniform @talkingmouth "No complaints here."

show roxanne:
    ease 0.5 ypos 1.2
    pause 0.5
    ease 0.5 ypos 1.0

pause 1.0

roxanne @sadbrow happymouth "Thank you very much, from the bottom of my heart."
roxanne @talkingmouth "I feel very confident knowing I'm leaving the ship in your capable hands."

hide roxanne
hide falkner
hide brawly
with dis

pause 2.0

scene roxie_orientation 
show auditorium_cover
with dis

red uniform @happy "Well. This feels familiar."

pause 1.0

redmind @happy "They've even got the same music playing, heh."

calem uniform @talkingmouth "Let's take our seats. The old Student Council will indicate when it's time for us to come up."

serena uniform @talkingmouth "Dibs on sitting next to you!"

grusha uniform @closedbrow talking2mouth "Dibs on an aisle seat. {size=30}Seriously, girl, chill.{/size}"

pause 1.0

roxanne uniform @happy "Good afternoon, my old friends!"

pause 0.5

stop music fadeout 5.0
queue music "audio/music/unwaveringemotions.ogg"

roxanne @sadbrow happymouth "I apologize for what is likely to be a drawn-out and excessively sentimental speech."
roxanne @closedbrow talkingmouth "I've been told my speeches flip-flop between 'inspirational' and 'insomnia-curing' with frightening suddenness, and I fear that today's will be no exception."
roxanne @talkingmouth "So, in the interest of brevity, and a graceful handing over of the reigns, I will summarize my thoughts in three two-word bytes."
roxanne @talkingmouth "And, to express my gratitude to the two men who have been by my side for the past year, men I have grown to trust and love, I will allow them to provide the first four words of the six."

pause 1.0

roxanne @talkingmouth "Falkner?"

pause 1.0

falkner uniform @closedbrow talkingmouth "...It seems a shame to only speak my mind now, at the end. What stories I might've been privy to, if I were to remain."
falkner @happymouth "What adventures you might have seen by my side, if only we'd been friends before it was time to leave. Oh, well."

pause 1.0

falkner @talkingmouth "Ladies, gentlemen, and distinguished others of Kobukan Academy. You have been here only one month. From this, you may believe that you have a great understanding of what life at Kobukan may entail."
falkner @happymouth "Allow me to assure you of one thing."
falkner @talkingmouth "Your eyes see only the tip of the iceberg. Your time at Kobukan will be far grander in scope, and massive in scale, than you might ever have dreamed."
falkner @talkingmouth "My two words are 'Thank You.' Thank you for allowing us to see you spread your wings at the very end of our time here."

pause 1.0

falkner @talkingmouth "Brawly?"

pause 1.0

brawly uniform @closedbrow sadmouth "{size=30}Man, I'm trying not to cry...{/size}"

pause 1.0

brawly @sadbrow happymouth "{size=30}Aw, hell, I'll cry in front of everyone here. I'm a man. I've earned that right.{/size}"

pause 1.0

brawly @angrybrow happymouth "Bros! My words are 'Carry On.'"
brawly @talkingmouth "This year is going to suck, sometimes. One-fifth of ya won't even graduate."
brawly @angrybrow talkingmouth "But that's why ya gotta keep going! Any wall that you come up against, you gotta just muscle through! There's no fight you can't win if you just don't stop punching!"
brawly @sadbrow happymouth "Sometimes, you're gonna fail. But that's alright. You can do everything right, and still come up short."
brawly @talkingmouth "Maybe you're not strong enough, or smart enough. Maybe even nine months in, your Pokémon still isn't listening to you."

pause 0.5

brawly @closedbrow talking2mouth "{i}Sigh.{/i}"

pause 1.0

brawly @angrybrow happymouth "That's alright, bros! Take it from big brother Brawly! You {i}can{/i} do this! You {i}can{/i} graduate! And you can do {i}anything{/i} you want as long as you're willing to break through everyone and everything in your way!"
brawly @angrybrow talking2mouth "And if one of you out there thinks that this doesn't apply to you, because the one in your way is {i}yourself{/i}..."

show roxie_orientation
show auditorium_cover
with vpunch

brawly @angry "Hey! Who the hell do you think you are? You think you can keep yourself down like that?" 
brawly @angrybrow happymouth "Hell no, brother-man! If you gotta break yourself to get where you want to go, you {i}can{/i}! Break through yourself and be the best you can be! I believe in you! {i}Carry on!{/i}"

pause 1.0

brawly @closedbrow talkingmouth "{i}Sigh.{/i}"
brawly @sadbrow happymouth "Alright. I'm done. Roxie?"

pause 1.0

roxanne @talkingmouth "You should have given speeches more often, Brawly."

brawly @happy "Nah, gotta keep all that passion in for when it matters. Now, go on. What're your two words?"

pause 1.0

roxanne @talkingmouth "{i}Stay true.{/i}"

pause 0.5

roxanne @closedbrow talking2mouth "We weren't the most successful Student Council. Now, at the end of our year, I can see clearly the mistakes we made, and the wrong paths we took."
roxanne @closedbrow happymouth "But..."

pause 1.0

roxanne @talkingmouth "But we stayed true. We kept our truth in the forefront of everything we did, as we strove towards our ideals."
roxanne @talking2mouth "It does not do for a leader to deny reality and seek out only what they believe should be."
roxanne @talking2mouth "By the same token, a leader with no imagination, no conception of an ideal world, has no reason to lead."

pause 0.5

roxanne @talking2mouth "This is not something that applies only to a student council. You--as Pokémon trainers, researchers, coordinators, breeders--you will all work with teams of Pokémon and people. You,{w=0.5} too,{w=0.5} are leaders."
roxanne @angrybrow talking2mouth "People will rely on you."
roxanne @closedbrow talkingmouth "The wills and desires of others will push you and pull you. Your fork in the road may lead off in dozens of different directions, and you'll have a dozen different people all urging you on a different road."

pause 0.5

roxanne @happy "When it is impossible to know which road to take, there's just one thing you need to remember. {i}Stay true.{/i} Believe in the truth you see, and follow the road that leads you to your ideals."

pause 1.0

roxanne @closedbrow happymouth "Thank you."

pause 0.5

narrator "For a moment, silence. Then--"

$ PlaySound("big applause.ogg")

stop music fadeout 1.5
play music "audio/music/hoenn_start.ogg" noloop 
queue music "audio/music/hoenn_loop.ogg"

pause 3.0

roxanne @surprised "Hm. That may have been the most positive feedback I've ever gotten for one my speeches."
roxanne @sadbrow happymouth "Lessons learned too late, I suppose."

pause 2.0

roxanne @talkingmouth "Well, we thank you for lending us your ears as we indulge our sentimentality. But let's not forget who this event is truly for."
roxanne @happymouth "We, the current Student Council of Kobukan are proud to present the Student Council hopefuls for this next year."
roxanne @talkingmouth "We believe, firmly, that they are the best possible students you could choose to represent, guide, and fight for you over the coming eleven months."

pause 1.0

roxanne @talking2mouth "Falkner?"

falkner @closedbrow talkingmouth "Aye."

roxanne @talking2mouth "Brawly?"

brawly @talking2mouth "Aye."

roxanne @talking2mouth "Very well."
roxanne @happy "These six Student Council hopefuls--Calem, [first_name], Serena, Jasmine, Grusha, and Cheren--have the unilateral, official, and unequivocal endorsement of we, the current Student Council."

calem uniform @closedbrow talkingmouth "{i}Phew.{/i} That's a weight off my mind."

roxanne @talkingmouth "Now, why don't you join me in inviting your Student Council hopefuls onto the stage?"

stop music fadeout 1.5

roxanne @talkingmouth "Please welcome..."

pause 0.5

roxanne @surprised "Hm?"

narrator "You turn around in your seat as you look behind yourself and see a student in the back of the room, out of breath, bent double and panting wildly."

red @confused "Wait... is that...?"

play music "audio/music/league_start.ogg" noloop 
queue music "audio/music/league_loop.ogg"

show silver surprisedbrow frownmouth:
    xpos 1.1 ypos 1.9 xzoom -1
    ease 3.0 xpos 0.8 ypos 1.0

silver @talkingmouth "{size=20}Hah... hah... there's... hah...{/size}"

pause 1.0

brawly @talkingmouth "Uh, I can't hear what that redheaded girl's saying. Falkner?"

falkner @talkingmouth "I believe that's a man."

pause 0.5

brawly @angrybrow talkingmouth "Okay, but what's he saying?"

falkner @closedbrow talking2mouth "I can't be sure. He's too far away to tell."

brawly @talking2mouth "...Like, how can you be sure she's a dude, then?"

falkner @talking2mouth "I can't, but based on the evidence, I--"

silver @talkingmouth "Outside! There's... you need to... get strong battlers, and..."

falkner @angrybrow talking2mouth "Wait, why do you care so much if he's a man or a woman?"

roxanne @talkingmouth closedbrow "Or something else. We musn't forget that possibility."

brawly @happy "Oh, yeah, I had a friend like that in Hoenn. Great surfer. You met them, right, Roxie?"

roxanne @happy "Yes, I--"

show roxie_orientation
show auditorium_cover
with vpunch

silver @angry "{size=40}Do you {i}mind?!{/i}{/size}"

pause 1.0

roxanne @talking2mouth "Not particularly, no. I stopped being a Student Council member about two minutes ago. So now I really have no obligation to listen to anyone's complaints ever again."
roxanne @closedbrow talking2mouth "...Well, I {i}do{/i} intend to become a teacher when I return to Hoenn, but until then, I--"

silver angry "Outside! People! Attacking the school! Thugs! Do something!"

roxanne @surprised "Oh! Well... yes, we should probably get a teacher, or..."

show silver happy with dis

pause 1.0

hide silver with dis

pause 1.0

show serena uniform with dis:
    xpos 1.0/6.0
show cheren uniform with dis:
    xpos 2.0/6.0
show calem uniform with dis:
    xpos 3.0/6.0
show jasmine uniform frownmouth with dis:
    xpos 4.0/6.0
show grusha uniform with dis:
    xpos 5.0/6.0

pause 1.0

grusha @confusedeyebrows talking2mouth "{size=30}What're we standing around for? Let's go.{/size}"

jasmine @surprised "{size=30}Hm? What do you mean?{/size}"

grusha @closedbrow talking2mouth "{size=30}C'mon. Some people are attacking the school. We're trying to prove to the school we'll fight for them.{/size}"
grusha @angrybrow talking2mouth "{size=30}Let's go out there, kick their asses, come back in and bask in the applause.{/size}" 

cheren @surprised "{size=30}Oh... shouldn't we leave that to the teachers?{/size}"

grusha @confusedeyebrows talking2mouth "{size=30}Of all of us, I kinda figured you could do with the boost most.{/size}"

cheren @disappointedmouth "{size=30}I... don't think I need it, really.{/size}"

jasmine @sad "{size=30}If those are actual criminals out there, I think we should probably just stay safe in here...{/size}"

serena @happymouth "{size=30}No, no, Grusha's right! This is an excellent opportunity for some showmanship, as well as the chance for us to test ourselves in a {i}real{/i} battle! We simply {i}must{/i} take advantage of it, right, Calem?"

calem uniform @closedbrow talking2mouth "{size=30}I'm not sure. [first_name], your input?{/size}"

pause 1.0

calem @surprised "{size=30}Wait, where did he go?{/size}"

grusha @confusedeyebrows talking2mouth "{size=30}Uh... I mean, the whole reason I suggested we go out and handle this was because he already ran out. So, yeah.{/size}"

pause 1.0

calem @closedbrow angrymouth "{i}Merde!{/i}"

pause 0.5

calem @talkingmouth "{size=30}He {i}is{/i} a bit of an instigator, isn't he? I suppose we'd better follow him, then...{/size}"

stop music fadeout 0.5
queue music "audio/music/dragondenstart_b.ogg" noloop 
queue music "audio/music/dragondenloop.ogg"

scene blank2 with splitfade

pause 1.0

scene relichall_A 
show roughneck angry
with splitfade

roughneck surprisedbrow @surprised "Hey! What're you doing here?!"

red uniform @angry "What am I-- {i}I'm{/i} a student here! What are {i}you{/i} doing here?"

roughneck happy "Heh! Wouldn't you like to know, punk?"

red @talking2mouth "Look, just get out of here! Your boss will blow his lid if he knows you're attacking the school in broad daylight!"

roughneck angry "What the boss don't know won't hurt him! And, actually... hey, don't I recognize you from somewhere?"

red @confused "I have no idea, but I might've beaten you in a battle before?"

roughneck @talkingmouth "Yeah, that was it! Well, I've been {i}real{/i} mad about that ever since, so I think I'm gonna give you a little what-for! How'd you like that, huh?"

red @angrymouth "Get {i}off{/i} of my campus!"

hide roughneck with dis

pause 1.0

show serena uniform surprised:
    xpos 4.0/6.0
show cheren uniform surprised:
    xpos 2.0/6.0
show calem uniform surprised:
    xpos 3.0/6.0
show jasmine uniform surprised:
    xpos 1.0/6.0
show grusha uniform surprised:
    xpos 5.0/6.0
with dis

cheren @sadmouth "...He's passionate."

show serena -surprisedbrow -frownmouth -surprised angrybrow frownmouth
show cheren angrybrow
show calem angrybrow
show jasmine sweat angrybrow frownmouth
show grusha angrybrow

grusha @confusedeyebrows talking2mouth "Alright, boss-man. What's the plan? Where are we going?"

calem @closedbrow "{w=0.5}.{w=0.5}.{w=0.5}."
calem @talking2mouth "They don't appear to be doing much more than minor property damage and intimidation. We should be safe."
calem @talking2mouth "[first_name] is doing well enough on his own for now. However, everyone else should split up into pairs. Seek out the attackers and defeat them. Obviously, do not hurt them." 
calem @talking2mouth "If you can get information from them--why they're doing this, who their leader is, then do so. Do not overextend. Stay within eyesight of another pair."

serena @talkingmouth "There's five of us here."

calem @talking2mouth "So there are."

cheren @disappointedbrow talking2mouth "I'll wait until [first_name] is done with his battle, then join him."

calem @talkingmouth "Thank you. Team, split up."

show serena:
    ease 3.0 xpos -0.1
show cheren:
    xpos 2.0/6.0
    ease 1.0 ypos 1.2 zoom 1.3 alpha 0.0
show calem:
    ease 2.0 xpos -0.1
show jasmine:
    ease 3.0 xpos 1.1
show grusha:
    ease 2.0 xpos 1.1

narrator "Meanwhile..."

python:
    trainer1 = MakeRed()
    trainer2 = Trainer("roughneck", TrainerType.Enemy, [GetTrainerTeam("Silver", "Skorupi"), GetTrainerTeam("Silver", "Stunky")], number=2)
    HealParty(trainer2)

call Battle([trainer1, trainer2], customexpressions=["red uniform angrybrow frownmouth", "red uniform angry", "roughneck", "roughneck angry"], specialmusic="Nothing", stopmusic=False, reanchor=[False, True], healParty=False) from _call_Battle_71
$ battlehistory["Roughneck2"] = _return

if (WonBattle("Roughneck2")):
    show roughneck surprisedbrow with dis

else:
    show roughneck angry with dis

redmind uniform @frownmouth "Right, I forgot that these guys don't play fair... another ambush double battle, huh?"

if (WonBattle("Roughneck2")):
    show roughneck surprisedbrow with dis

    roughneck "Wh... what? You're way too strong! Get outta here!"

    hide roughneck with dis

    narrator "The roughneck leaves in a panic, throwing his wallet behind himself."

    if (punkwins > 3):
        narrator "You assume this is out of habit, from your frequent visits to the alleyway."
    else:
        narrator "You assume this is out of habit, given Silver's report on the thugs' predilection for gamble battles."

    $ money += 277

    narrator "You gained $277!"

    redmind @thinking "Well, every little counts..."

    pause 1.0

    hide cheren

    show cheren uniform at leftside with dis

    cheren @sadmouth "[first_name], Calem told us to split up and take out the gang members. I'm here to provide backup."

    $ ValueChange("Cheren", 3, 0.25)

    cheren @disappointed "Though it appears my efforts were not necessary. Well-battled, [first_name]."

    red @talkingmouth "Nice! Good to have you, Cheren! This guy was no problem, but I'll appreciate your backup with the others!"

    cheren @sadmouth "Right. Take the lead, and I will follow."

else:
    show roughneck happy with dis

    roughneck "Hah! Beat ya! Now fork over your cash, redhat!"

    red @surprised "What? No! This isn't a gamble battle, idiot!"

    roughneck "Oh, yeah? Well, what's gonna stop me from just taking your money anyway, huh?"

    hide cheren

    show cheren uniform at leftside with dis

    cheren @sadmouth "[first_name], Calem told us to split up and take out the gang members. I'm here to provide backup."

    roughneck "Hah! Too late! I already beat your little boyfriend here!"

    pause 0.5

    cheren @closedbrow sadmouth "Hm."

    $ HealParty()

    cheren @sadmouth "Unfortunately, I have potions." 
    
    roughneck surprised "Huh?!"
    
    cheren @happy "So. It seems you'll have to defeat him again, with me by his side, this time."

    red @talkingmouth "Nice save, Cheren!"

    cheren @sadmouth "Hm."

    roughneck angry "Agh... screw this! I'm not taking on two at one, that's cheating!"

    hide roughneck with dis

red @angrybrow talking2mouth "Right... it looks like there's a couple in the gardens. {w=0.5}Let's go."

scene black with splitfade

pause 1.0

scene garden:
    zoom 0.625
show clouds behind garden
with splitfade

pause 1.0

show roughneck happy at centerside
show roughneck2 at rightside
with dis

roughneck @talkingmouth "Heh heh! With a handful of these Oran Berries, our salad tonight is going to be delish!"

show cheren uniform at leftside

cheren angry "Those berries are for Pokémon! Specifically, the Pokémon of students at this school!"

roughneck2 angry "Uh-oh, bro! Look, there's a couple punks here! We should probably handle 'em before we stuff our pockets full of these berries, y'know?"

roughneck @talkingmouth "Heh, I'll battle {i}and{/i} eat berries at the same time! No rules!"


python:
    trainer1 = MakeRed()
    trainer2 = MakeTrainer("Cheren", TrainerType.Ally)
    trainer3 = Trainer("roughneck", TrainerType.Enemy, [GetTrainerTeam("Silver", "Grimer"), GetTrainerTeam("Silver", "Scraggy")])
    trainer4 = Trainer("roughneck", TrainerType.Enemy, [GetTrainerTeam("Silver", "Croagunk"), GetTrainerTeam("Silver", "Sneasel")])

hide roughneck
hide roughneck2
with dis

call Battle([trainer1, trainer2, trainer3, trainer4], customexpressions=["red uniform angrybrow frownmouth", "red uniform angry", "cheren uniform closedbrow", "cheren uniform angry", "roughneck", "roughneck happy", "roughneck angry", "roughneck angry"], reanchor=[False, False, True, True], specialmusic="Nothing", stopmusic=False, healParty=False) from _call_Battle_72
$ battlehistory["Roughnecks2"] = _return

if (WonBattle("Roughnecks2")):
    show roughneck surprisedbrow at leftside with dis
    show roughneck2 surprised at rightside with dis

    roughneck angry "Hey, that ain't no fair! You guys're trained to battle, and we just figured it out on our own!"

    roughneck2 angry "Bloody elitists! If we didn't keep losin' Pokémon battles, we could afford to go to Kobukan, too!"

    hide roughneck
    hide roughneck2
    with dis

    narrator "The roughnecks leave in a panic, throwing a wad of cash behind them."

    show cheren uniform surprised with dis

    cheren "Why did they...? I mean, we didn't ask for that."

    red uniform @talking2mouth "No, but I'm not complaining. Want half?"

    $ ValueChange("Cheren", 3, 0.5)

    cheren -surprisedbrow -frownmouth -surprised @closedbrow disappointedmouth "...I... No. No, thank you, I'm good."

    $ money += 327

    narrator "You gained $327!"

    red @closedbrow talking2mouth "Alright. Where to, next?"

else:
    show roughneck happy at leftside with dis
    show roughneck2 happy at rightside with dis

    roughneck "Hah! Two of ya, and you still lost!"

    red uniform @angry "Hey, there are two of you two, too!"

    cheren uniform @disappointedbrow disappointedmouth "This really doesn't matter."

    roughneck surprised "Huh?"

    cheren @sadmouth "It's a simple question of logistics."

    cheren @disappointedbrow disappointedmouth "You're far away from your home base, and have no equipment, items, or support."

    $ HealParty()

    cheren @sadmouth "I, however, have potions." 

    show roughneck2 angry with dis
    
    roughneck surprised "Huh?!"
    
    cheren @happy "So. It seems you'll have to defeat us again. And again, and again, until I run out of potions."

    red @talkingmouth "Nice going, Cheren!"

    cheren @sadmouth "Hm."

    roughneck2 angry "Agh... screw this! You can't just spam items to win a battle, that's cheating!"

    cheren @sadmouth "I say this in full kindness: 'cope.'"

    hide roughneck with dis
    hide roughneck2 with dis

    red @talkingmouth "Hm. Nicely done."

    cheren @disappointedmouth "Let's not make a habit of it."

    red @sweat happy "Yeah, it was kinda embarrassing. Okay, where to next?"

cheren @disappointedmouth "I think I hear a commotion coming from the Battle Hall."

red @closedbrow talking2mouth "Right, let's go."

scene black with splitfade

pause 1.0

scene stadium_empty with splitfade

pause 1.0

show janine uniform:
    xpos 0.2
show roughneck:
    xpos 0.4
show roughneck2:
    xpos 0.6
show roughneck3:
    xpos 0.8
with dis

pause 2.0

redmind uniform @surprised "Oh my God, I need to see this."

roughneck angry "Hey, girlie! You better cough up your money!"
roughneck2 happy "Yeah, yeah! And your Pokémon, too!"
roughneck3 "Don't make this hard on us! Give us your stuff or we'll mug ya!"

janine "{w=0.5}.{w=0.5}.{w=0.5}."
janine @talking2mouth "I'm struggling to find the words to explain how much shit you're in."

roughneck2 surprised "...Hey, uh, guys, we outnumber her three to one, but she's, like, super-chill about this."
roughneck3 surprised "Yeah, actually, isn't she one of those people who comes to our alley and beats up on us?"
roughneck surprisedbrow @surprised "I'm kinda thinking that maybe we should, like, go..."

redmind @confusedeyebrows frownmouth "Huh, so she does that too."

janine @closedbrow talking2mouth "{i}Sigh.{/i} Look, attacking the school like this is a massive, idiotic, mistake."
janine @sadbrow talkingmouth "But I still want to be able to go to the alley to blow off steam every once in a while, and I can't do that if you guys get arrested."
janine @closedbrow talking2mouth "So I'm going to close my eyes, and when I open them, [first_name] and his friend over there will have kicked your ass, and you'll be gone. Got it?"

redmind @surprised "Oh, she saw us!"

hide janine 
show roughneck angry:
    ease 0.5 xpos 0.25
show roughneck2 angry:
    ease 0.5 xpos 0.5
show roughneck3 angry:
    ease 0.75 xpos 0.75
with dis

roughneck @talkingmouth "Hey! The scary lady told us ta fight you instead of her, so... uh... yeah!"
roughneck3 "Yeah, so, uh, give us your money! Or we'll mug ya!"
roughneck2 "{size=30}Bro, you {i}don't{/i} know what mugging is, do you?{/size}"

hide roughneck
hide roughneck2
hide roughneck3
with dis

python:
    trainer1 = MakeRed()
    trainer2 = MakeTrainer("Cheren", TrainerType.Ally)
    trainer3 = Trainer("roughneck", TrainerType.Enemy, [Pokemon("Beedrill", level=13, moves=[GetMove("Fury Attack"), GetMove("Twineedle"), GetMove("Poison Sting")], ability="Sniper")])
    trainer4 = Trainer("roughneck", TrainerType.Enemy, [Pokemon("Mightyena", level=18, moves=[GetMove("Howl"), GetMove("Bite"), GetMove("Roar"), GetMove("Sand Attack")], ability="Intimidate")])
    trainer5 = Trainer("roughneck", TrainerType.Enemy, [Pokemon("Dustox", level=13, moves=[GetMove("Gust"), GetMove("Confusion"), GetMove("Poison Sting")], ability="Shield Dust")])

call Battle([trainer1, trainer2, trainer3, trainer4, trainer5], customexpressions=["red uniform angrybrow frownmouth", "red uniform angry", "cheren uniform closedbrow", "cheren uniform angry", "roughneck", "roughneck happy", "roughneck surprised", "roughneck angry", "roughneck angry", "roughneck angry"], reanchor=[False, False, True, True, True], specialmusic="Nothing", stopmusic=False, healParty=False) from _call_Battle_73
$ battlehistory["Roughnecks3"] = _return

if (WonBattle("Roughnecks3")):
    show janine uniform closedbrow:
        xpos 0.2
    show roughneck surprisedbrow:
        xpos 0.4
    show roughneck2 surprised:
        xpos 0.6
    show roughneck3 surprised:
        xpos 0.8

    roughneck "Damn, redhat might be even scarier than the scary lady!"
    roughneck2 "Yeah, and I don't even get the fun tingles from his kind of scary!"
    roughneck3 "Well, I do."

    pause 2.0

    roughneck3 "What?!"

    hide roughneck
    hide roughneck2
    hide roughneck3
    with dis

    narrator "The roughnecks leave in a panic, dropping their wallets behind them."

    cheren uniform @surprised "...I don't suspect I'll ever understand the criminal mind."

    $ money += 456

    narrator "You gained $456!"

    pause 1.0

    janine @talking2mouth "Alright. Are they gone?"

    red uniform @talkingmouth "Uh, yeah."

    show janine:
        ease 0.5 xpos 0.5

    $ ValueChange("Janine", 3, 0.2)

else:
    show janine uniform closedbrow:
        xpos 0.2
    show roughneck happy:
        xpos 0.4
    show roughneck2 happy:
        xpos 0.6
    show roughneck3 happy:
        xpos 0.8

    roughneck "Hah! Beat them down, sicko mode!"
    roughneck2 "Yeah, we mugged them so hard!"
    roughneck3 "Yeah, uh, don't mean to bring down the mood, but doesn't that mean that scary lady's just going to kick our asses now?"

    pause 1.0

    show roughneck surprisedbrow
    show roughneck2 surprised
    show roughneck3 surprised
    with dis

    roughneck "Uh, I dunno. Is that what that means?"

    pause 0.5

    janine @talking2mouth "Yes."

    pause 0.5

    roughneck2 "Uh... yeah, we were, uh, we were just leaving..."

    hide roughneck
    hide roughneck2
    hide roughneck3
    with dis

    narrator "The roughnecks awkwardly shuffle out of the room."

    cheren uniform @surprised "...I don't suspect I'll ever understand the criminal mind."

    pause 1.0

    janine @talking2mouth "Alright. Are they gone?"

    red uniform @talkingmouth "Uh, yeah."

    show janine:
        ease 0.5 xpos 0.5

stop music fadeout 1.5
play music "audio/music/hoenn_start.ogg" noloop 
queue music "audio/music/hoenn_loop.ogg"

janine -closedbrow @talking2mouth "Good. Hopefully they ran off and told their buddies that they were in over their heads."

if (WonBattle("Roughneck2") and WonBattle("Roughnecks2") and WonBattle("Roughnecks3")):
    red @talking2mouth "I hope so. We beat three groups of them on the way here without healing."

    janine @surprised "Really? Three groups? Impressive."

    $ ValueChange("Janine", 5, 0.5)

    if (GetRelationshipRank("Janine") > 0):
        if (HasEvent("Janine", "Domming")):
            janine @smirkmouth "You might get your reward sooner than I thought, if you keep doing tricks like that."
        else:
            janine @talking2mouth "Exactly what I expected of my precious battler."
    else:
        janine @smirkmouth "Well done."

pause 1.0

janine @angrybrow talking2mouth "...I should probably get a little bit involved. Damn it, I was meant to be having a meeting with the Dean in a couple minutes, though..."

pause 0.5

janine @talking2mouth "Alright. Scram. I'll clean up here. You're doing that election, right? Go back to that, I've got the 'invasion' covered."

red @confused "You aren't going to vote?"

janine @talking2mouth "Sorry. I saw your posters, but none of that stuff affects me."

red @confused "Really? Even Grusha's international battle tournament? I would've thought that would be a great stepping-stone for your Champion attempt."

janine @talking2mouth "Yeah, I don't think I'm going to go for that, this year. You guys seem to have it covered. Hopefully I can appoint one of you Captain and finally launch my own attempt next year."

janine @smirkmouth "Besides. You know how many 'once-in-a-lifetime' international battle tournaments I've been through? Stay at Kobukan for three years like me, and even shooting stars seem common."

red @happy "Fair enough!"

cheren @disappointedmouth "Is it really alright to just leave the invasion in your hands, though, Ma'am?"

janine @talking2mouth "Not a Ma'am. And yes, don't worry. Just go."

cheren @sadbrow disappointedmouth "Well... if you say so."

pause 1.0

janine @talking2mouth "Wait. You, the one who's not [first_name]."

show cheren uniform at leftside with dis

show janine:
    ease 0.5 xpos 0.75 xzoom -1

cheren @disappointed "Cheren."

janine @smirkmouth "Your team... it has a pretty particular composition."

cheren @surprised "Er... yes?"

janine @smirkmouth "I see what you're going for. It's an older strategy, but it's pretty clever."

cheren @disappointed "...Thank you. My training skill is below average. Even with my roommate's help, I couldn't get up to the level I should be. So I hoped to offset that with some strategy."

janine @talking2mouth "Good luck."

redmind @thonk "Hm. What was that about?"

scene blank2 with splitfade

narrator "Heading outside of the Battle Hall, you can see the backs of several identically-dressed men and women quickly retreating from the school campus." 
narrator "It seems your efforts, in combination with Janine's reputation, have succeeded in driving away the 'invasion.'"

narrator "You and Cheren notice a gathering of people at the baseball field, and quickly sprint across campus to get there."

scene baseball 
show serena uniform:
    xpos 2.0/6.0
show calem uniform:
    xpos 3.0/6.0
show jasmine uniform:
    xpos 4.0/6.0
show grusha uniform:
    xpos 5.0/6.0
with splitfade

pause 1.0

show cheren uniform with dis:
    xpos 1.0/6.0

calem @talking2mouth "Welcome back. Is everyone alright?"

cheren @disappointed "Yes."

show silver behind serena:
    xpos -0.1 ypos 1.2 zoom 0.9
    ease 3.0 xpos 1.1

if (WonBattle("Roughnecks2") and WonBattle("Roughneck3")):
    cheren @happy "They were no trouble whatsoever. They were easily defeated by [first_name]'s efforts."

elif (WonBattle("Roughnecks2") or WonBattle("Roughneck3")):
    cheren @disappointed "We had a little trouble, but nothing that seemed excessively dangerous."

else:
    cheren @sad "We did... poorly, but we are unhurt."

calem @talkingmouth "I'm glad. From the reports we've heard, it seemed that the 'leader' of this little expedition was in the Battle Hall when he was driven off."

show silver behind serena:
    xpos 1.1 ypos 1.2 zoom 0.9 xzoom -1
    ease 3.0 xpos -0.1

red uniform @talkingmouth "Yeah, I think we fought him. He had a pretty big Mightyena."

jasmine @surprised "You fought him?"

if (WonBattle("Roughnecks3")):
    red @happy "Yeah, beat him, too. And two of his minions. Just now."

    jasmine @closedbrow talking2mouth sweat "That's... odd. We've already heard that... hm."

else:
    red @talking2mouth "Yeah. We didn't beat him, but Janine scared him off."

grusha @confusedeyebrows talking2mouth "Weird."

cheren @surprised "What is it?"

serena @talkingmouth "Well, someone must have gotten confused, because, about twenty minutes ago, we heard that [first_name] single-handedly defeated the leader of the invasion."

red @surprised "Huh?"

grusha @confusedeyebrows talking2mouth "Yeah, and we heard Cheren went out 'like a punk'. That's an exact quote."

pause 0.5

grusha @closedbrow talking2mouth "We also heard he 'didn't {i}do{/i} shit.' Another direct quote there."

show silver behind serena:
    xpos -0.1 ypos 1.2 zoom 0.9 xzoom 1
    ease 3.0 xpos 1.1

red @closedbrow talking2mouth "I mean..."

if (WonBattle("Roughnecks3")):
    cheren @angry "That's a libelous accusation. [first_name] and I beat the invaders {i}together{/i}, much like I'm certain you all did."

else:
    cheren @angry "That's a libelous accusation. [first_name] and I both lost against the invaders' boss."

calem @talking2mouth "I fully believe you. But the fact is, the rumor has spread quite far amongst the student body already, and..."

narrator "Looking over at the gathering of students at the baseball field, you see many admiring glances and bashful whispers thrown your way."
narrator "Even more than usual, that is."

show silver behind serena with dis:
    xpos 1.1 ypos 1.2 zoom 0.9 xzoom -1
    easeout 3.0 xpos 2.6/6.0
    pause 0.5
    "silver surprisedbrow"
    pause 0.5
    easein 3.0 xpos 1.1

serena @talkingmouth "Someone must have had some sort of motivation to spread a lie about who was most responsible for fighting off the invaders, then. But who could that be?"
serena @angrybrow happymouth "Who would have a reason to engage in such a conspiracy?"
serena @surprised "Ooh, is it one of us? Is there a Machiavellian bad actor--an evil imposter--among us?"

if (GetRelationship("Serena") == "Conspirator"):
    red @closedbrow talking2mouth "Serena, please, cool it with the conspiracy theories."

    serena @angrybrow poutmouth "But they're so fun!"

calem @talking2mouth "That seems unlikely. I'm sure one of the other students simply heard a report, and in the excitement and confusion, mis-reported it."

cheren @disappointedmouth "Does that seem like the most likely option to you? Does it, really?"

calem @talking2mouth "Well... yes. Yes, it does. More likely than someone having a vendetta against you, while wanting to prop up [first_name]. It's not like he needs it, anyway."

show serena frownmouth
show jasmine frownmouth
show grusha confusedeyebrows
with dis

cheren @angry "Fascinating. I look forward to hearing more of your wisdom and insights when you are my President, Calem."

calem @surprised "I'm... I'm sorry, did something happen that I'm unaware of?"

cheren "{w=0.5}.{w=0.5}.{w=0.5}."
cheren @disappointed "I will discuss it later. Now isn't the time. We still need to return to the auditorium, so that we can give our pre-election speeches, after all."

calem @talking2mouth "Very well. But if there's anything you'd like to discuss with us, please do let me know."

cheren @sadmouth "I assure you, I will."

scene blank2 with splitfade

narrator "The student council hopefuls march back to the auditorium, a large group of followers in tow. Upon opening the doors..."

scene blank with splitfade

pause 0.2

scene orientation 
show auditorium_cover
with splitfade

pause 0.2

$ PlaySound("crowd_cheer.ogg")

show orientation 
show auditorium_cover
with vpunch

show calem uniform at leftside with dis 

calem @surprised "Cheering? For us?"

show grusha uniform at rightside with dis

grusha @closedeyes talking2mouth "Not every day that the people trying to get sworn in as the student body's fighters and defenders actually prove they can do it."

pause 0.5

grusha @confusedeyebrows talking2mouth "Though it does look like they're mostly looking at you, [first_name]. Seems rumors spread quickly."

red uniform @sweat sadbrow happymouth "Ah, geez... Hey, should I just, like set the record straight? Just tell everyone what {i}really{/i} happened before we begin the actual thing?"

calem @closedbrow talking2mouth "Hm. Perhaps, but it also doesn't hurt to have a spotless figurehead, adored by the masses..."

red @confused sweat "Laying it on a bit thick, aren't we?"

show roxanne surprisedbrow frownmouth uniform with dis

roxanne @talkingmouth "You're back. Thank goodness! What happened? I looked away for half a second, and you were all gone, and Brawly had bent a skinhead into the shape of a pretzel."

grusha @closedbrow talking2mouth "Minor invasion of school grounds by some punks from the city. Must've known that, for a couple minutes, there wasn't going to be a Student Council, so they were hoping to capitalize on our moment of weakness."

show serena uniform surprised with vpunch:
    xpos 0.6

serena @talkingmouth "Are you suggesting there's a {i}mole{/i} in Kobukan? {i}Another{/i} imposter? How thrilling!"

grusha @closedbrow talking2mouth "Eh."

show serena -surprisedbrow -frownmouth -surprised
show jasmine uniform:
    xpos 0.4
with dis

jasmine @talkingmouth "Say, shouldn't we get on with the election? I think we've held it off long enough at this point."

calem @talkingmouth "Right you are."
calem @talking2mouth "Roxanne, thank you for the lovely introduction."

roxanne -surprisedbrow -frownmouth -surprised @talkingmouth "Mm. Remember: {w=0.5}Thank you. {w=0.5}Carry on. {w=0.5}Stay true."

calem @talkingmouth "Wise words, upperclassman. {i}{w=0.5}Merci. {w=0.5}Continuer. {w=0.5}Reste vrai.{/i}"

hide calem
hide roxanne
hide jasmine
hide serena
hide grusha 
with dis

pause 1.0

stop music fadeout 3.5

show calem uniform behind auditorium_cover as calemmodel:
    ypos 0.41 zoom 0.11 xpos 0.53 xzoom -1
show cheren uniform behind auditorium_cover as cherenmodel:
    ypos 0.41 zoom 0.11 xpos 0.56 xzoom -1
show jasmine uniform behind auditorium_cover as jasminemodel:
    ypos 0.41 zoom 0.11 xpos 0.59
show serena uniform behind auditorium_cover as serenamodel:
    ypos 0.41 zoom 0.11 xpos 0.62 xzoom -1
show grusha uniform behind auditorium_cover as grushamodel:
    ypos 0.41 zoom 0.11 xpos 0.65 
show red uniform behind auditorium_cover as redmodel:
    ypos 0.41 zoom 0.11 xpos 0.68
with Dissolve(2.0)

pause 1.0

calem uniform @closedbrow talking2mouth "{size=30}...Okay.{/size}"

queue music "audio/music/new_adventure_start.ogg" noloop
queue music "audio/music/new_adventure_loop.ogg"

show calem as calemmodel:
    ypos 0.41
    parallel:
        ease 2.0 xpos 0.5
    parallel:
        pause 1.0
        ease 1.0 ypos 0.4

calem @surprised "{size=30}Oh, there's a little step here. Hm.{/size}"

pause 1.0

calem @talking2mouth "{i}A-hem!{/i} Classmates and friends! Apologies for the delay. A group of vagabonds from the city seemed to think that now would be a good time to knock over our pottery."

redmind @thinking "...I mean, I agree with him entirely, but damn, this feels pretty classist."

calem @talkingmouth "Thankfully, the quick thinking, and measured response of the Student Council hopefuls, as well as many of you, was able to prevent things from spiraling out of control."
calem @happy "Well done, everyone."

$ PlaySound("crowd_cheer.ogg")

pause 2.0

calem @talkingmouth "It is {i}this{/i} exact collaborative spirit that we hope to continue and encourage in our future dealings."

pause 1.0

calem @talking2mouth "Let me be clear. We stand united. Every one of us seeks to support and uplift every other one of us. There is no reason to abstain from voting from any one of us--we even have experience working together, already."
calem @closedbrow talking2mouth "We all aim to work together to give you, the student body, more privileges, freedoms, powers, and security than before."
calem @talkingmouth "I, for my part, aim to massively increase funding to the clubs in this school."

$ PlaySound("short med applause.ogg")

calem @closedbrow talking2mouth "We all owe the Battle Team a great debt of gratitude, of course. It is internationally famous, and with champions such as Cynthia and Steven Stone graduating from it, its reputation is clearly well-deserved."
calem @happy "So {i}just{/i} imagine what we could do if some of our tuition money--even a fraction--was diverted into other clubs!" 
calem @talkingmouth "Imagine if Kobukan elected to hire champions to lead their other clubs, such as they did with Lance and the Battle Team!"

pause 1.0

calem @angrybrow happymouth "Hm! Yes, it's quite simple. The sky is the limit! And, if you vote for me, not only will I work to support and uplift my co-council members, I'll fight to spread the school's funding more equitably!"

$ PlaySound("big applause.ogg")

pause 2.0

calem @happy "{size=30}Well, that went well. Brevity is the soul of wit.{/size}"

calem @talkingmouth "Now, does anyone have any questions? ...Yes, you, in the red hat."

show calem as calemmodel:
    ypos 0.4
    parallel:
        ease 2.0 xpos 0.47
    parallel:
        ease 1.0 ypos 0.41

show cheren as cherenmodel:
    ypos 0.41 xpos 0.56
    pause 2.5
    parallel:
        ease 2.0 xpos 0.5
        pause 3.0
        ease 2.0 xpos 0.44
    parallel:
        pause 1.0
        ease 1.0 ypos 0.4
        pause 3.0
        ease 1.0 ypos 0.41

show jasmine as jasminemodel:
    ypos 0.41 xpos 0.59
    pause 7
    parallel:
        ease 2.0 xpos 0.5 
        pause 3.0
        ease 2.0 xpos 0.41
    parallel:
        pause 1.0
        ease 1.0 ypos 0.4
        pause 3.0
        ease 1.0 ypos 0.41

show serena as serenamodel:
    ypos 0.41 xpos 0.62
    pause 12.5
    parallel:
        ease 2.0 xpos 0.5 
        pause 3.0
        ease 2.0 xpos 0.38
    parallel:
        pause 1.0
        ease 1.0 ypos 0.4
        ease 0.2 ypos 0.395
        ease 0.2 ypos 0.4
        ease 0.2 ypos 0.395
        ease 0.2 ypos 0.4
        ease 0.2 ypos 0.395
        ease 0.2 ypos 0.4
        ease 0.2 ypos 0.395
        ease 0.2 ypos 0.4
        ease 0.2 ypos 0.395
        ease 0.2 ypos 0.4
        ease 0.2 ypos 0.395
        ease 0.2 ypos 0.4
        ease 0.2 ypos 0.395
        ease 0.2 ypos 0.4
        ease 0.2 ypos 0.395
        ease 1.0 ypos 0.41

show grusha as grushamodel:
    ypos 0.41 xpos 0.65
    pause 18.0
    parallel:
        ease 2.0 xpos 0.5 
        pause 3.0
        ease 2.0 xpos 0.35
    parallel:
        pause 1.0
        ease 1.0 ypos 0.4
        pause 3.0
        ease 1.0 ypos 0.41

pause 3.0

narrator "Each student council hopeful gives their speeches, one after another, making sure to emphasize the support each of them will give each other."

pause 3.0

narrator "Serena's speech was enthusiastic and passionate, Jasmine's was earnest and heartwarming, Grusha's was typically cool... and Cheren's was normal, though you thought you saw darkness cross his face once or twice."

pause 3.0

narrator "Finally, it was your time to speak. By this time, the audience has worked itself up into a complete frenzy, and they're practically salivating to hear what you have to say."

show red as redmodel:
    ypos 0.41 xpos 0.68
    parallel:
        ease 2.0 xpos 0.5
    parallel:
        pause 1.0
        ease 1.0 ypos 0.4

narrator "Admittedly... you could have prepared your speech a bit better, but you've been awfully busy, recently."

redmind @thinking "Alright. Just gotta wing this."

menu:
    "My fellow Kobukan Academyians...":
        pass

    "Alright, Kobukan, listen up! Here's what's happening...":
        pass

    "Um... Yeah. You guys are gonna, like, uh...":
        pass

$ PlaySound("short med applause.ogg")

redmind @thonk "Really? I haven't even said anything yet."

menu:
    "I know what you want!":
        pass

    "I'm going to fight for you! Nonviolently, of course.":
        pass

    "I will be your will on the Student Council.":
        pass

$ PlaySound("big applause.ogg")

redmind @happy "Hey, this speech-giving thing is easy."

menu:
    "I'll never give up!":
        pass

    "Kobukan Academy!":
        pass

    ">Yell unintelligible, but enthusiastic, gobbledygook":
        pass

$ PlaySound("crowd_cheer.ogg")

narrator "As you continue your speech, you notice Cheren, to your right, giving you a strange look."

pause 1.0

narrator "Upon further inspection, Calem and Serena are, too. It seems the overly-enthusiastic response your tepid speech received did not escape your fellow council hopefuls."

redmind @thinking "Sorry, guys. Frienergy. Not much I can do about it."

pause 1.0

redmind @closedbrow frownmouth "But, hey, this could be a good thing. At least I can use it to help people."

red @happymouth "And that's... pretty much it! Vote for us. We'll do good. Promise. Anyone have any questions?"

stop music

show grusha as grushamodel:
    xpos 0.35 ypos .41
    ease 1.0 xzoom -1

show jasmine as jasminemodel:
    xpos 0.41 ypos .41
    ease 1.0 xzoom -1

show serena as serenamodel:
    xpos .38 ypos .41
    ease 1.0 xzoom 1

cheren uniform @sadmouth "Yes."

calem uniform @surprised "Hm?"

cheren @closedbrow disappointedmouth "Please excuse me."

show calem as calemmodel:
    ypos 0.41 xpos 0.47
    ease 1.0 xpos 0.44 xzoom 1

show cheren as cherenmodel:
    ypos .41 xpos .44
    ease 1.0 xpos 0.48 xzoom 1

show red as redmodel:
    ypos .4 xpos .5
    ease 1.0 xpos 0.52 ypos .41 xzoom -1

red @talkingmouth "Uh, yeah. What's up, man?"

cheren @sad2eyes sadmouth "I was just wondering when you were going to tell us{cps=20} {i}about your power.{/i}"

pause 2.0

show screen songsplash("Drought", "Zame")

play music "audio/music/drought.ogg"

red noshine @surprisedeyes surprisedeyebrows talking2mouth "Wh-what...?"

cheren @disappointedmouth "I think we should discuss the way that you are so easily able to endear yourself to other students. The way you won this election without having given any effort towards it whatsoever."
cheren @angry "The way you command Pokémon you've never met before, and have them listen to you immediately. The way you even got {i}into{/i} this school."
cheren @closedbrow disappointedmouth "I think it's important the voters hear about this. This will definitely affect their votes, no?"

pause 1.0

red @surprisedeyes surprisedeyebrows frownmouth "I... I..."

cheren @sad2eyes sadmouth "It was a pleasure, for me, and for others, to watch your meteoric rise, [first_name]."

pause 1.0

cheren @shadow sad2eyes sadmouth "But there's something everyone seems to have forgotten. {w=0.5}Meteors don't {i}rise.{/i}{w=0.5} They {i}fall.{/i}"

calem @angrybrow talking2mouth "Cheren. What do you think you're doing?"

cheren @angry "My best. That's all I've ever been able to do."

calem @angrybrow talking2mouth "Whatever disagreements you may have with [first_name] can be handled offstage. You're just threatening your own chances. Come back here, and--"

cheren @disappointedbrow talking2mouth "I recuse myself."

calem @surprised "Huh?"

cheren @disappointedmouth "I no longer seek election. My {i}sole interest{/i} is uncovering the truth."

grusha uniform @surprisedeyes sweat shadow "Uh... guys, I... I don't think now's..."

pause 1.0

calem @talking2mouth "B-be that as it may... there's a time and place for everything, and now is not the place to toss out such wild accusations, with no backing or--"

cheren @angrybrow disappointedmouth "You ask for evidence?"

hide screen currentdate
show blank 
with vpunch

cheren @angry "I'll give you evidence!"

show cherenshatefultruth with vpunch

cheren @angry "Look at this man! Look at the guilt in his eyes! Do you {i}dare{/i} to tell me I'm wrong? {w=0.5}{i}{b}Does anyone?{/b}{/i}"
cheren @angry "His feelings are written as plainly as pen on paper!"

if (GetRelationship("Serena") == "Conspirator"):
    serena uniform @angry "Cheren, you must stop at once! [first_name] is a good friend--I know he would not do this sort of thing you're accusing him of!"

    cheren @angry "Do you think yourself unique in this, Serena? This man has dozens of 'good friends', all {i}convinced{/i} that they're the most important person in the world to him!"

else:
    serena uniform @sad "This can't possibly be true... right, [first_name]?"

    red @surprisedeyes surprisedeyebrows sadmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    cheren @closedbrow disappointedmouth "Silence. What a surprise."

cheren @angry "How do you think he gained so many friends, so quickly? It's been one month! And yet, seemingly {i}everybody{/i} in this school knows him--admires him--loves him!"

cheren @angry "We are all {i}throttled{/i} by his red string! Every one of us, hanging like puppets from his hands!"

cheren @closedbrow disappointedmouth "You're willing to entertain so many conspiracy theories, but not this one? You're unwilling to accept that you've been duped!"

jasmine uniform @angry "Cheren! What you're saying just isn't possible!"

cheren @angry "Isn't it? Do Espers not exist? Are their powers not known to take a great many forms?"

if (classstats["Psychic"] >= 10):
    cheren @angry "Has [first_name] not demonstrated {i}remarkable{/i} proficiency in his Psychic classes?"

elif (classstats["Ghost"] >= 10):
    cheren @angry "Has [first_name] not demonstrated {i}remarkable{/i} proficiency in his Ghost classes?"

if (GetRelationship("Sabrina") == "Friend"):
    cheren @sad2eyes sadmouth "Can anyone here claim they haven't seen [first_name] talking back and forth in his mind with his fellow Esper, Sabrina?"

cheren @disappointed "Yes, that's all circumstantial evidence... {i}but, if all I am saying is lies, why isn't he saying anything?{/i}"

cheren @angry "Well, [first_name]? Deny it!"

menu: 
    "[ellipses]":
        pass

    "[ellipses]":
        pass

    "[ellipses]":
        pass

narrator "Your tongue lies, heavy and powerless, in your mouth. {w=0.5}Your throat is dry. {w=0.5}Your lips crack under the scorching heat of the stagelights above."

pause 1.0

narrator "You cannot speak."

red @sad "{w=0.5}.{w=0.5}.{w=0.5}."

show cherenshatefultruth with vpunch

cheren @angry "Deny it!"

show cherenshatefultruth with vpunch

cheren @angry2brow disappointedmouth "Deny it!"

show cherenshatefultruth with vpunch

cheren @shadow angry2brow angrymouth "Damn you! Just deny it! Prove me wrong! Make of me a crackpot in front of this whole school! Ruin my reputation, my plans, my future--destroy me! {i}Just deny it!{/i}"

pause 1.0

narrator "You cannot speak."

pause 1.0

narrator "In the crowd, you see a lip begin to curl in disgust."

pause 0.5

narrator "Someone coughs awkwardly, and gets up to leave the auditorium."

if (not mayhaslarvesta):
    narrator "Brendan glares at you, and puts a protective arm around May, who seems to be sobbing."

else:
    "The sound of a camera clicking rings through the silence."

grusha uniform @surprisedeyes surprisedeyebrows sweat shadow "{size=30}Guys. Please. I need... I... I'm having...{/size}"

hide cherenshatefultruth with Dissolve(1.0)

pause 1.0

cheren @sadbrow shadow disappointedmouth "I'm begging you, [first_name]. Deny it. Please. I {i}need{/i} to be wrong."

pause 1.0

narrator "You cannot speak."

hide blank with dis

pause 1.0

cheren noshine @sad "...Well. That's that, then."

python:
    chars = []
    for key, value in persondex.items():
        if (key in ["Leaf", "Dawn", "Serena", "Hilda", "Rosa", "May", "Silver", "Nessa", "Skyla", "Misty", "Bea", "Flannery", "Sonia", "Whitney", "Hilbert"]):
            chars.append((value["Value"] + value["RelationshipRank"] * 100, key))
    chars.sort(reverse = True, key=(lambda entry : entry[0]))

$ charname = chars[2][1]

if (charname == "Leaf"):
    show leaf angry at leftside with dis

    leaf "Hey! No the hell it isn't! You need some proof!"

elif (charname == "Dawn"):
    show dawn angry at leftside with dis

    dawn "N-no! He's just not speaking because I'm--no, because {i}he's{/i} nervous! It could happen to anyone! Where's the actual proof?"

elif (charname == "Serena"):
    serena @angry "No! {i}Je refuse!{/i} These... allegations--they're hearsay and rumors! His refusal to defend himself does {i}not{/i} mean he's guilty!"

    serena @angry "Where is the proof, Cheren?"

elif (charname == "Hilda"):
    show hilda angry at leftside with dis

    hilda "You've gone too far, Cheren! I don't know what kinda shit's running through [first_name]'s head right now, but the fact he isn't saying anything doesn't mean you're right!"

    hilda "What happened to innocent until proven guilty, huh?"
    
elif (charname == "Rosa"):
    show rosa angry at leftside with dis

    rosa "Hey! Unless a camera recorded him doing any of the stuff you think he did, then he's innocent! I've seen trash like this in tabloids about me, and they {i}never{/i} have any proof!"

elif (charname == "May"):
    show may angry at leftside with dis

    may "Now, what kind of messed-up hypothesis is that? You're cooking up something real nasty, Cheren! Do you have {i}any{/i} proof to back up what you're saying? Silence isn't proof!"

elif (charname == "Silver"):
    show silver angry at leftside with dis

    silver "Hey! You bastard, what do you think you're doing, just throwing around accusations like that? You think you can just accuse your opponent of shit because he's doing better than you? You don't have {i}any{/i} proof!"

elif (charname == "Nessa"):
    show nessa angry at leftside with dis

    nessa "Yeah, this doesn't sound real. You've got, like, {i}no{/i} proof that what you're talking about is anything more than a sore loser's daydream."

elif (charname == "Skyla"):
    show skyla angry at leftside with dis

    skyla "Leave him alone! He's a hero, for saving the school from those thugs, and you're trying to punish him for that? You don't have any proof!"

elif (charname == "Misty"):
    show misty angry at leftside with dis

    misty "You're a lunatic! This guy's a bit of a wimp, but he's... he's nice and, patient, and... you're making stuff up to make him look bad! You don't have any proof!"

elif (charname == "Bea"):
    show bea angry at leftside with dis

    bea "You are insane. There is no such 'power' in this world that you are describing. You've no proof that these accusations you make have any weight whatsoever."

elif (charname == "Flannery"):
    show flannery furious at leftside with dis

    flannery "You're putting me in a {i}real{/i} bad mood, spouting all this bullshit! Sounds like you're just a sore loser, because I'm not seeing any proof!"

elif (charname == "Sonia"):
    show sonia angry at leftside with dis

    sonia "This isn't how an election's supposed to go, Cheren. You can't just accuse the other side of cheating because you did poorly. You've got no proof to back up this ludicrous claim."

elif (charname == "Whitney"):
    show whitney angry at leftside with dis

    whitney "Hey! You're picking on [first_name] just because he's more popular than you, and now that you're outta high school, you think the nerds should be able to pick on the jocks, aren't you?"

    whitney "You don't have {i}any{/i} proof of what you're saying!"

elif (charname == "Hilbert"):
    show hilbert angry at leftside with dis

    hilbert "Don't be ridiculous. There's no such thing as this 'power' you're talking about. You're making stuff up, and you have no proof. Pretending to care about the truth... that's pathetic."

cheren @angry "You want proof?! If you don't take [first_name]'s silence as proof, then your closeness to [first_name] blinds you!"

if (charname == "Leaf"):
    cheren @angrybrow disappointedmouth "Pardon me for not taking your character judgment of the person you are so obviously infatuated with seriously!"

elif (charname == "Dawn"):
    cheren @angrybrow disappointedmouth "You disappear with him into Instructor Melony's classroom for hours at a time! Who knows what you're doing in there, but I think it's fair to say that you're a bit too close to see your muse clearly!"

elif (charname == "Serena"):
    cheren @angrybrow disappointedmouth "Did you not ever wonder that as you started your own conspiracy, that a man who so willingly leapt into yours might have one of his own?"
    cheren @angrybrow disappointedmouth "I would think {i}very{/i} carefully about whether [first_name] has really joined your plan to help you achieve {i}your{/i} goals."

elif (charname == "Hilda"):
    cheren @angrybrow disappointedmouth "How lovely it is that you are now able to take a break from your own efforts and rely on him. Does that not seem like the first step to fostering an unhealthy dependency?"
    cheren @angry "You are far from the only one he 'helps out'!"
    
elif (charname == "Rosa"):
    cheren @angrybrow disappointedmouth "Rosa, the famous movie star. I'm sure you can't think of {i}any{/i} reasons why he'd want to get close to you!"
    cheren @angry "Sure, you think that he's an awful actor who barely knew you before you met a while ago. But did it never occur to you that someone might simply {i}act{/i} as though they're bad at lying?"

elif (charname == "May"):
    cheren @angrybrow disappointedmouth "One has to wonder what happens during the time you spend alone with him!" 
    cheren @angry "One has to {i}question{/i} if he's really helping you with {i}your{/i} issues, or if he has his own agenda, that your {i}current status{/i} does not comply with!"

elif (charname == "Silver"):
    cheren @angry "Silver, of course!"
    cheren @angrybrow disappointedmouth "I find it {i}highly{/i} suspect that your houseguests decided {i}now{/i} was the perfect time to visit our school. Especially given the rumors associated with [first_name]'s 'dominating victory.'"

elif (charname == "Nessa"):
    cheren @angrybrow disappointedmouth "Pardon me for not being overly swayed by the obviously-biased testimony of [first_name]'s {i}date.{/i} Perhaps you think that your relationship with him is less casual than it really is?"

elif (charname == "Skyla"):
    cheren @angrybrow disappointedmouth "Oh, yes. Isn't it odd, then, that those gentlemen from the city, the ones you {i}happen to know{/i} have a history with [first_name], showed up {i}just in time{/i} to be thoroughly trounced by our Superman here?"
    cheren @angry "I might look to see if it's really {i}justice{/i} your wingman fights for."

elif (charname == "Misty"):
    cheren @angrybrow disappointedmouth "Hm! So, the woman who is on bad terms with everyone, and leaps to physical assault the same way others might shake hands is defending him?"
    cheren @angry "Did you ever pause to think, even for a moment, {i}why{/i} this man might have engendered such uncharacteristic feelings of warmth in you?"

elif (charname == "Bea"):
    cheren @angrybrow disappointedmouth "This coming from the woman who can split rock with her bare feet? Powers exist, Bea, and you of all people should know how they can be wielded to harm!"

elif (charname == "Flannery"):
    cheren @angrybrow disappointedmouth "Hm! So, the woman who rages at the slightest provocation, whose anger is so legendary that her name has become a common phrase amongst the student body, is defending him?"
    cheren @angry "Did you ever pause to think, even for a moment, {i}why{/i} this man might have engendered such uncharacteristic feelings of warmth in you?"
    
elif (charname == "Sonia"):
    cheren @angrybrow disappointedmouth "Oh, and I suppose {i}you're{/i} the one most qualified to lecture on how we should handle loss, are you? I've evidence, and even if I didn't, I wouldn't give up until I found it!"

elif (charname == "Whitney"):
    cheren @angrybrow disappointedmouth "Unsurprising that the manipulators would stick together! We all know about your 'projects', Whitney! How you cry to get your way, how you snare people into your service!"
    cheren @angry "It's no surprise to me that you saw in [first_name] a kindred spirit!"

elif (charname == "Hilbert"):
    cheren @angrybrow disappointedmouth "As though you've ever cared about the truth!" 
    cheren @angry "Your 'dream' is far more well-known than you may want it to be, and I assure you, when {i}that{/i} is revealed to the world, the consequences will be far more dire than a mild social ostracization!"

cheren @disappointedmouth "There's no way anyone can deny that this 'debate' is over!"

$ charname = chars[1][1]

if (charname == "Leaf"):
    show leaf angry at rightside with dis

    leaf "Hey! No the hell it isn't! You need some proof!"

elif (charname == "Dawn"):
    show dawn angry at rightside with dis

    dawn "N-no! He's just not speaking because I'm--no, because {i}he's{/i} nervous! It could happen to anyone! Where's the actual proof?"

elif (charname == "Serena"):
    serena @angry "No! {i}Je refuse!{/i} These... allegations--they're hearsay and rumors! His refusal to defend himself does {i}not{/i} mean he's guilty!"

    serena @angry "Where is the proof, Cheren?"

elif (charname == "Hilda"):
    show hilda angry at rightside with dis

    hilda "You've gone too far, Cheren! I don't know what kinda shit's running through [first_name]'s head right now, but the fact he isn't saying anything doesn't mean you're right!"

    hilda "What happened to innocent until proven guilty, huh?"
    
elif (charname == "Rosa"):
    show rosa angry at rightside with dis

    rosa "Hey! Unless a camera recorded him doing any of the stuff you think he did, then he's innocent! I've seen trash like this in tabloids about me, and they {i}never{/i} have any proof!"

elif (charname == "May"):
    show may angry at rightside with dis

    may "Now, what kind of messed-up hypothesis is that? You're cooking up something real nasty, Cheren! Do you have {i}any{/i} proof to back up what you're saying? Silence isn't proof!"

elif (charname == "Silver"):
    show silver angry at rightside with dis

    silver "Hey! You bastard, what do you think you're doing, just throwing around accusations like that? You think you can just accuse your opponent of shit because he's doing better than you? You don't have {i}any{/i} proof!"

elif (charname == "Nessa"):
    show nessa angry at rightside with dis

    nessa "Yeah, this doesn't sound real. You've got, like, {i}no{/i} proof that what you're talking about is anything more than a sore loser's daydream."

elif (charname == "Skyla"):
    show skyla angry at rightside with dis

    skyla "Leave him alone! He's a hero, for saving the school from those thugs, and you're trying to punish him for that? You don't have any proof!"

elif (charname == "Misty"):
    show misty angry at rightside with dis

    misty "You're a lunatic! This guy's a bit of a wimp, but he's... he's nice and, patient, and... you're making stuff up to make him look bad! You don't have any proof!"

elif (charname == "Bea"):
    show bea angry at rightside with dis

    bea "You are insane. There is no such 'power' in this world that you are describing. You've no proof that these accusations you make have any weight whatsoever."

elif (charname == "Flannery"):
    show flannery furious at rightside with dis

    flannery "You're putting me in a {i}real{/i} bad mood, spouting all this bullshit! Sounds like you're just a sore loser, because I'm not seeing any proof!"

elif (charname == "Sonia"):
    show sonia angry at rightside with dis

    sonia "This isn't how an election's supposed to go, Cheren. You can't just accuse the other side of cheating because you did poorly. You've got no proof to back up this ludicrous claim."

elif (charname == "Whitney"):
    show whitney angry at rightside with dis

    whitney "Hey! You're picking on [first_name] just because he's more popular than you, and now that you're outta high school, you think the nerds should be able to pick on the jocks, aren't you?"

    whitney "You don't have {i}any{/i} proof of what you're saying!"

elif (charname == "Hilbert"):
    show hilbert angry at rightside with dis

    hilbert "Don't be ridiculous. There's no such thing as this 'power' you're talking about. You're making stuff up, and you have no proof. Pretending to care about the truth... that's pathetic."

cheren @angry "He refuses to speak on his own defense! Why would an innocent man ever refuse to defend himself? Is it for someone else? Is he defending {i}you?{/i} You might think so, but I very much doubt it!"
cheren @angrybrow disappointedmouth "You, specifically, are far too biased to speak clearly on this matter."

if (charname == "Leaf"):
    cheren @angrybrow disappointedmouth "Pardon me for not taking your character judgment of the person you are so obviously infatuated with seriously!"

elif (charname == "Dawn"):
    cheren @angrybrow disappointedmouth "You disappear with him into Instructor Melony's classroom for hours at a time! Who knows what you're doing in there, but I think it's fair to say that you're a bit too close to see your muse clearly!"

elif (charname == "Serena"):
    cheren @angrybrow disappointedmouth "Did you not ever wonder that as you started your own conspiracy, that a man who so willingly leapt into yours might have one of his own?"
    cheren @angrybrow disappointedmouth "I would think {i}very{/i} carefully about whether [first_name] has really joined your plan to help you achieve {i}your{/i} goals."

elif (charname == "Hilda"):
    cheren @angrybrow disappointedmouth "How lovely it is that you are now able to take a break from your own efforts and rely on him. Does that not seem like the first step to fostering an unhealthy dependency?"
    cheren @angry "You are far from the only one he 'helps out'!"
    
elif (charname == "Rosa"):
    cheren @angrybrow disappointedmouth "Rosa, the famous movie star. I'm sure you can't think of {i}any{/i} reasons why he'd want to get close to you!"
    cheren @angry "Sure, you think that he's an awful actor who barely knew you before you met a while ago. But did it never occur to you that someone might simply {i}act{/i} as though they're bad at lying?"

elif (charname == "May"):
    cheren @angrybrow disappointedmouth "One has to wonder what happens during the time you spend alone with him!" 
    cheren @angry "One has to {i}question{/i} if he's really helping you with {i}your{/i} issues, or if he has his own agenda, that your {i}current status{/i} does not comply with!"

elif (charname == "Silver"):
    cheren @angry "Silver, of course!"
    cheren @angrybrow disappointedmouth "I find it {i}highly{/i} suspect that your houseguests decided {i}now{/i} was the perfect time to visit our school. Especially given the rumors associated with [first_name]'s 'dominating victory.'"

elif (charname == "Nessa"):
    cheren @angrybrow disappointedmouth "Pardon me for not being overly swayed by the obviously-biased testimony of [first_name]'s {i}date.{/i} Perhaps you think that your relationship with him is less casual than it really is?"

elif (charname == "Skyla"):
    cheren @angrybrow disappointedmouth "Oh, yes. Isn't it odd, then, that those gentlemen from the city, the ones you {i}happen to know{/i} have a history with [first_name], showed up {i}just in time{/i} to be thoroughly trounced by our Superman here?"
    cheren @angry "I might look to see if it's really {i}justice{/i} your wingman fights for."

elif (charname == "Misty"):
    cheren @angrybrow disappointedmouth "Hm! So, the woman who is on bad terms with everyone, and leaps to physical assault the same way others might shake hands is defending him?"
    cheren @angry "Did you ever pause to think, even for a moment, {i}why{/i} this man might have engendered such uncharacteristic feelings of warmth in you?"

elif (charname == "Bea"):
    cheren @angrybrow disappointedmouth "This coming from the woman who can split rock with her bare feet? Powers exist, Bea, and you of all people should know how they can be wielded to harm!"

elif (charname == "Flannery"):
    cheren @angrybrow disappointedmouth "Hm! So, the woman who rages at the slightest provocation, whose anger is so legendary that her name has become a common phrase amongst the student body, is defending him?"
    cheren @angry "Did you ever pause to think, even for a moment, {i}why{/i} this man might have engendered such uncharacteristic feelings of warmth in you?"
    
elif (charname == "Sonia"):
    cheren @angrybrow disappointedmouth "Oh, and I suppose {i}you're{/i} the one most qualified to lecture on how we should handle loss, are you? I've evidence, and even if I didn't, I wouldn't give up until I found it!"

elif (charname == "Whitney"):
    cheren @angrybrow disappointedmouth "Unsurprising that the manipulators would stick together! We all know about your 'projects', Whitney! How you cry to get your way, how you snare people into your service!"
    cheren @angry "It's no surprise to me that you saw in [first_name] a kindred spirit!"

elif (charname == "Hilbert"):
    cheren @angrybrow disappointedmouth "As though you've ever cared about the truth!" 
    cheren @angry "Your 'dream' is far more well-known than you may want it to be, and I assure you, when {i}that{/i} is revealed to the world, the consequences will be far more dire than a mild social ostracization!"

cheren @disappointedbrow talking2mouth "Your arguments are weak and thin! I can tell you doubt him yourself! There's nothing else to prove!" 

$ charname = chars[0][1]

if (charname == "Leaf"):
    show leaf angry with dis

    leaf "Hey! No the hell it isn't! You need some proof!"

elif (charname == "Dawn"):
    show dawn angry with dis

    dawn "N-no! He's just not speaking because I'm--no, because {i}he's{/i} nervous! It could happen to anyone! Where's the actual proof?"

elif (charname == "Serena"):
    serena @angry "No! {i}Je refuse!{/i} These... allegations--they're hearsay and rumors! His refusal to defend himself does {i}not{/i} mean he's guilty!"

    serena @angry "Where is the proof, Cheren?"

elif (charname == "Hilda"):
    show hilda angry with dis

    hilda "You've gone too far, Cheren! I don't know what kinda shit's running through [first_name]'s head right now, but the fact he isn't saying anything doesn't mean you're right!"

    hilda "What happened to innocent until proven guilty, huh?"
    
elif (charname == "Rosa"):
    show rosa angry with dis

    rosa "Hey! Unless a camera recorded him doing any of the stuff you think he did, then he's innocent! I've seen trash like this in tabloids about me, and they {i}never{/i} have any proof!"

elif (charname == "May"):
    show may angry with dis

    may "Now, what kind of messed-up hypothesis is that? You're cooking up something real nasty, Cheren! Do you have {i}any{/i} proof to back up what you're saying? Silence isn't proof!"

elif (charname == "Silver"):
    show silver angry with dis

    silver "Hey! You bastard, what do you think you're doing, just throwing around accusations like that? You think you can just accuse your opponent of shit because he's doing better than you? You don't have {i}any{/i} proof!"

elif (charname == "Nessa"):
    show nessa angry with dis

    nessa "Yeah, this doesn't sound real. You've got, like, {i}no{/i} proof that what you're talking about is anything more than a sore loser's daydream."

elif (charname == "Skyla"):
    show skyla angry with dis

    skyla "Leave him alone! He's a hero, for saving the school from those thugs, and you're trying to punish him for that? You don't have any proof!"

elif (charname == "Misty"):
    show misty angry with dis

    misty "You're a lunatic! This guy's a bit of a wimp, but he's... he's nice and, patient, and... you're making stuff up to make him look bad! You don't have any proof!"

elif (charname == "Bea"):
    show bea angry with dis

    bea "You are insane. There is no such 'power' in this world that you are describing. You've no proof that these accusations you make have any weight whatsoever."

elif (charname == "Flannery"):
    show flannery furious with dis

    flannery "You're putting me in a {i}real{/i} bad mood, spouting all this bullshit! Sounds like you're just a sore loser, because I'm not seeing any proof!"

elif (charname == "Sonia"):
    show sonia angry with dis

    sonia "This isn't how an election's supposed to go, Cheren. You can't just accuse the other side of cheating because you did poorly. You've got no proof to back up this ludicrous claim."

elif (charname == "Whitney"):
    show whitney angry with dis

    whitney "Hey! You're picking on [first_name] just because he's more popular than you, and now that you're outta high school, you think the nerds should be able to pick on the jocks, aren't you?"

    whitney "You don't have {i}any{/i} proof of what you're saying!"

elif (charname == "Hilbert"):
    show hilbert angry with dis

    hilbert "Don't be ridiculous. There's no such thing as this 'power' you're talking about. You're making stuff up, and you have no proof. Pretending to care about the truth... that's pathetic."

cheren @angry "Stop demanding proof! Do I {i}need{/i} to provide proof when the accused doesn't even ask for it?"
cheren @angrybrow disappointedmouth "And I find it {i}rich{/i} that you, of all people, are asking for proof."

if (charname == "Leaf"):
    cheren @angrybrow disappointedmouth "Pardon me for not taking your character judgment of the person you are so obviously infatuated with seriously!"

elif (charname == "Dawn"):
    cheren @angrybrow disappointedmouth "You disappear with him into Instructor Melony's classroom for hours at a time! Who knows what you're doing in there, but I think it's fair to say that you're a bit too close to see your muse clearly!"

elif (charname == "Serena"):
    cheren @angrybrow disappointedmouth "Did you not ever wonder that as you started your own conspiracy, that a man who so willingly leapt into yours might have one of his own?"
    cheren @angrybrow disappointedmouth "I would think {i}very{/i} carefully about whether [first_name] has really joined your plan to help you achieve {i}your{/i} goals."

elif (charname == "Hilda"):
    cheren @angrybrow disappointedmouth "How lovely it is that you are now able to take a break from your own efforts and rely on him. Does that not seem like the first step to fostering an unhealthy dependency?"
    cheren @angry "You are far from the only one he 'helps out'!"
    
elif (charname == "Rosa"):
    cheren @angrybrow disappointedmouth "Rosa, the famous movie star. I'm sure you can't think of {i}any{/i} reasons why he'd want to get close to you!"
    cheren @angry "Sure, you think that he's an awful actor who barely knew you before you met a while ago. But did it never occur to you that someone might simply {i}act{/i} as though they're bad at lying?"

elif (charname == "May"):
    cheren @angrybrow disappointedmouth "One has to wonder what happens during the time you spend alone with him!" 
    cheren @angry "One has to {i}question{/i} if he's really helping you with {i}your{/i} issues, or if he has his own agenda, that your {i}current status{/i} does not comply with!"

elif (charname == "Silver"):
    cheren @angry "Silver, of course!"
    cheren @angrybrow disappointedmouth "I find it {i}highly{/i} suspect that your houseguests decided {i}now{/i} was the perfect time to visit our school. Especially given the rumors associated with [first_name]'s 'dominating victory.'"

elif (charname == "Nessa"):
    cheren @angrybrow disappointedmouth "Pardon me for not being overly swayed by the obviously-biased testimony of [first_name]'s {i}date.{/i} Perhaps you think that your relationship with him is less casual than it really is?"

elif (charname == "Skyla"):
    cheren @angrybrow disappointedmouth "Oh, yes. Isn't it odd, then, that those gentlemen from the city, the ones you {i}happen to know{/i} have a history with [first_name], showed up {i}just in time{/i} to be thoroughly trounced by our Superman here?"
    cheren @angry "I might look to see if it's really {i}justice{/i} your wingman fights for."

elif (charname == "Misty"):
    cheren @angrybrow disappointedmouth "Hm! So, the woman who is on bad terms with everyone, and leaps to physical assault the same way others might shake hands is defending him?"
    cheren @angry "Did you ever pause to think, even for a moment, {i}why{/i} this man might have engendered such uncharacteristic feelings of warmth in you?"

elif (charname == "Bea"):
    cheren @angrybrow disappointedmouth "This coming from the woman who can split rock with her bare feet? Powers exist, Bea, and you of all people should know how they can be wielded to harm!"

elif (charname == "Flannery"):
    cheren @angrybrow disappointedmouth "Hm! So, the woman who rages at the slightest provocation, whose anger is so legendary that her name has become a common phrase amongst the student body, is defending him?"
    cheren @angry "Did you ever pause to think, even for a moment, {i}why{/i} this man might have engendered such uncharacteristic feelings of warmth in you?"
    
elif (charname == "Sonia"):
    cheren @angrybrow disappointedmouth "Oh, and I suppose {i}you're{/i} the one most qualified to lecture on how we should handle loss, are you? I've evidence, and even if I didn't, I wouldn't give up until I found it!"

elif (charname == "Whitney"):
    cheren @angrybrow disappointedmouth "Unsurprising that the manipulators would stick together! We all know about your 'projects', Whitney! How you cry to get your way, how you snare people into your service!"
    cheren @angry "It's no surprise to me that you saw in [first_name] a kindred spirit!"

elif (charname == "Hilbert"):
    cheren @angrybrow disappointedmouth "As though you've ever cared about the truth!" 
    cheren @angry "Your 'dream' is far more well-known than you may want it to be, and I assure you, when {i}that{/i} is revealed to the world, the consequences will be far more dire than a mild social ostracization!"

stop music fadeout 2.0

cheren @closedbrow disappointedmouth "Enough!"

hide leaf
hide dawn
hide serena
hide hilda
hide rosa
hide may
hide silver
hide nessa
hide skyla
hide misty
hide bea
hide flannery
hide sonia
hide whitney
hide hilbert
with dis

pause 2.0

cheren @disappointedmouth "Enough."

pause 1.0

cheren @sad2brow talking2mouth "[first_name]. Any comments?"

pause 1.0

narrator "Your friends are doubting you."
narrator "A thousand repressed memories scream to be acknowledged. Years of loneliness wait behind the barrier of your presumed innocence."
narrator "But to maintain that innocence would require you to lie."
narrator "To speak."

pause 1.0

narrator "You cannot speak."

cheren @disappointedmouth "You ask for proof. You all {i}demand{/i} proof. Fine. {i}Fine.{/i}"

queue music "audio/music/lavenderintense_start.ogg" noloop
queue music "audio/music/lavenderintense_loop.ogg"

cheren @angry "You two."

show mace angrybrow happymouth at leftside
show face angrybrow happymouth at rightside
with Dissolve(1.0)

pause 1.0

nate @surprised "Those two?"

cheren @disappointed "These two have the proof you crave."

mace @surprisedbrow happymouth "Yes, we do! And believe us! We were terrified when we found out the truth!"

face @surprisedbrow happymouth "When we learned this seemingly-innocent man had been warping us and manipulating us from within our own minds this entire time, I nearly broke down!"

mace @angrybrow happymouth "He was a good friend. To think he'd betray us in this manner is... unconscionable."

cheren @disappointedmouth "...Where's the proof? You said you had it?"

mace @closedbrow talking2mouth "It might be more accurate to say... we know how to {i}take{/i} it."

redmind @surprisedeyebrows surprisedeyes frownmouth "...What?"

show face:
    xpos 0.75 ypos 1.0 zoom 1.0 alpha 1.0
    ease 0.5 xpos 1.1 ypos 1.3 zoom 1.3 alpha 0.0

pause 1.0

face @talkingmouth "Come on! Get up here, witch!"

show face:
    xpos 1.1 ypos 1.3 zoom 1.3 alpha 0.0
    ease 0.5 xpos 0.75 ypos 1.0 zoom 1.0 alpha 1.0

show sabrina sad:
    xpos 1.1 ypos 1.3 zoom 1.3 alpha 0.0
    ease 0.5 xpos 0.5 ypos 1.0 zoom 1.0 alpha 1.0

if (GetRelationship("Sabrina") == "Friend"):
    redmind @surprisedeyebrows surprisedeyes frownmouth "N-no! Not Sabrina!"

    pause 1.0

    redmind @sad "[sabrinacolor]{size=30}Help me.{/size}{/color}"

    narrator "You cannot speak."

show face:
    xpos 0.75 ypos 1.0 zoom 1.0 alpha 1.0

cheren @surprisedbrow surprised3mouth "Wait. What are you--what are you two doing?"

mace @talkingmouth "Oh, it's quite simple! This lovely lady here is an Esper, who has a bad habit of reading our minds!"

face @talkingmouth "Yes, she's like a wonderful piñata of secrets."

mace @talkingmouth "Now, what do you suppose will come out if we break this piñata, hm?"

cheren @surprised "{size=30}What?{/size}"
cheren @angry "No. Absolutely not. [first_name] is who we're trying to prove the guilt of, not-- not Sabrina, or--"

mace @happy "Terribly sorry, {i}partner{/i}, but this is the only proof we could find."

face @talkingmouth "So, why don't you just sit back and let us handle this, hm?"

show mace angry:
    xpos 0.25
    ease 0.3 xpos 0.35
show face angry:
    xpos 0.75
    ease 0.3 xpos 0.65
with vpunch

mace @talkingmouth "Well? Tell us about [first_name]! Tell us about his powers!"

face @talkingmouth "Don't spare {i}any{/i} details, or we'll know you're working with him!"

sabrina @talking2mouth "Y-you're... you're crazy, I don't know... he doesn't have anything..."

show mace angry:
    xpos 0.36
show face angry:
    xpos 0.64
with vpunch

mace @talkingmouth "Quit that bullshit!"

face @talkingmouth "Yeah, we know you're covering for him!"

roxanne uniform @surprised "{w=0.5}.{w=0.5}.{w=0.5}." 
roxanne @surprised "Calem?"

calem @surprised "...Huh? What? I mean... what do I...?"

roxanne @closedbrow angrymouth "Agh, fine..."

roxanne @angry "You two, stop that! Immediately! I'll report you to the Office of Student Conduct and Conflict Resolution!"

brawly uniform @angry "I'll break your heads!"

sabrina @talking2mouth "N-no! Don't fight! Please, just... leave me alone, and..."

show mace angry:
    xpos 0.37
show face angry:
    xpos 0.63
with vpunch

mace @talkingmouth "Spill, witch!"

face @talkingmouth "Tell us about the freak, or you're next!"

sabrina @talking2mouth "N-no, I... no, just..."

show mace surprisedbrow frownmouth with dis:
    ease 2.0 xpos 0.2
show face surprisedbrow frownmouth with dis:
    ease 2.0 xpos 0.8

pause 1.0

show blank3 behind sabrina
with spinfaderapid
show blank2 behind sabrina
with spinfaderapid
hide blank3
show blank3 behind sabrina
with spinfaderapid
hide blank2
show blank2 behind sabrina
with spinfaderapid
hide blank3
show blank3 behind sabrina
with spinfaderapid
hide blank2
show blank2 behind sabrina
with spinfaderapid

show sabrina neutralpowered poweredbrow talking2mouth with dis:
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

show thoughts1 behind sabrina:
    ypos random.uniform(0.1, 0.9) xpos random.uniform(1.1, 1.5)
    pause random.uniform(1.0, 10.0)
    ease random.uniform(5.0, 10.0) xpos -1.0
    repeat

show thoughts2 behind sabrina:
    ypos random.uniform(0.1, 0.9) xpos random.uniform(1.1, 1.5)
    pause random.uniform(1.0, 10.0)
    ease random.uniform(5.0, 10.0) xpos -1.0
    repeat

show thoughts3 behind sabrina:
    ypos random.uniform(0.1, 0.9) xpos random.uniform(1.1, 1.5)
    pause random.uniform(1.0, 10.0)
    ease random.uniform(5.0, 10.0) xpos -1.0
    repeat

show thoughts4 behind sabrina:
    ypos random.uniform(0.1, 0.9) xpos random.uniform(1.1, 1.5)
    pause random.uniform(1.0, 10.0)
    ease random.uniform(5.0, 10.0) xpos -1.0
    repeat

show thoughts5 behind sabrina:
    ypos random.uniform(0.1, 0.9) xpos random.uniform(1.1, 1.5)
    pause random.uniform(1.0, 10.0)
    ease random.uniform(5.0, 10.0) xpos -1.0
    repeat

show thoughts6 behind sabrina:
    ypos random.uniform(0.1, 0.9) xpos random.uniform(1.1, 1.5)
    pause random.uniform(1.0, 10.0)
    ease random.uniform(5.0, 10.0) xpos -1.0
    repeat

show thoughts7 behind sabrina:
    ypos random.uniform(0.1, 0.9) xpos random.uniform(1.1, 1.5)
    pause random.uniform(1.0, 10.0)
    ease random.uniform(5.0, 10.0) xpos -1.0
    repeat

show thoughts8 behind sabrina:
    ypos random.uniform(0.1, 0.9) xpos random.uniform(1.1, 1.5)
    pause random.uniform(1.0, 10.0)
    ease random.uniform(5.0, 10.0) xpos -1.0
    repeat

show thoughts9 behind sabrina:
    ypos random.uniform(0.1, 0.9) xpos random.uniform(1.1, 1.5)
    pause random.uniform(1.0, 10.0)
    ease random.uniform(5.0, 10.0) xpos -1.0
    repeat

show thoughts10 behind sabrina:
    ypos random.uniform(0.1, 0.9) xpos random.uniform(1.1, 1.5)
    pause random.uniform(1.0, 10.0)
    ease random.uniform(5.0, 10.0) xpos -1.0
    repeat

show thoughts11 behind sabrina:
    ypos random.uniform(0.1, 0.9) xpos random.uniform(1.1, 1.5)
    pause random.uniform(1.0, 10.0)
    ease random.uniform(5.0, 10.0) xpos -1.0
    repeat


sabrina @talking2mouth "Leave me [sabrinacolor]{i}ALONE!{/i}{/color}"

pause 10.0

narrator "Secrets flit through your mind as Sabrina's telepathy opens up, sending memories, shadows, dark, repressed desires, echoing in a thousand voices, through the heads of everyone present."

narrator "And then, in a familiar voice..."

"You" "I have a power. It makes people trust me, and my Pokémon obey my commands. I need to keep it a secret from everyone. If they found out about it, I'd lose all my friends."
"You" "And I'll do anything to make sure that never happens again."

pause 1.0

red @shadow sad "No..."

show blank with Dissolve(3.0)

pause 3.0

hide blank3
hide blank2
hide blank 
hide thoughts1
hide thoughts2
hide thoughts3
hide thoughts4
hide thoughts5
hide thoughts6
hide thoughts7
hide thoughts8
hide thoughts9
hide thoughts10
hide thoughts11
with Dissolve(2.0)

pause 2.0

mace -surprisedbrow -frownmouth -surprised @talkingmouth "Well. There you have it."

face -surprisedbrow -frownmouth -surprised @talkingmouth "Undeniable proof that [first_name] has a power that he's been hiding from us."

show sabrina -neutralpowered sadbrow sadmouth:
    ease 0.5 xpos 0.5 ypos 1.0

sabrina @talking2mouth "...Why? Why did you...? How could you be so cruel...?"

mace @angry "Us? You're the freak who reads our minds and hoards our secrets! It's your fault for even coming here in the first place!"

sabrina @talking2mouth "...Yes. Yes, this was foolish of me. To think I could have a life."

if (GetRelationship("Sabrina") == "Friend"):
    sabrina "To think that I could have friends."

pause 1.0

sabrina @talking2mouth "My mentor would tell me not to do this."

show mace surprisedbrow frownmouth
show face surprisedbrow frownmouth
with dis

sabrina @closedbrow talkingmouth "He would say... that this is revenge. That I'm proving myself the witch you think I am."
sabrina @talking2mouth "I suppose I no longer have a reason not to cast my spells."
sabrina @talking2mouth "...So, here is my curse. Your secret."

show mace angry with dis:
    ease 0.5 xpos 0.4

show face angry with dis:
    ease 0.5 xpos 0.6

mace @talkingmouth "Don't you--"

show mace surprisedbrow frownmouth
show face surprisedbrow frownmouth
with dis

sabrina @talking2mouth "They are siblings. {w=1.0}{i}And{/i} lovers."

hide sabrina with dis

pause 3.0

play music "<from 10>audio/crowdargue.ogg" channel "crowd"
play music "audio/crowdargue2.ogg" channel "crowd2"

$ AnimateValueChange(random.randint(-10, -1), random.uniform(0.1, 0.9), pausing=False)
$ AnimateValueChange(random.randint(-10, -1), random.uniform(0.1, 0.9), pausing=False)
$ AnimateValueChange(random.randint(-10, -1), random.uniform(0.1, 0.9), pausing=True)

mace angry "Wh-what? N-no! We're-- we're just step-siblings! There's no blood! There's--"

$ AnimateValueChange(random.randint(-10, -1), random.uniform(0.1, 0.9))

face angry "{i}Shut up, you idiot!{/i} Let's get out of here!"

hide mace 
hide face with dis

pause 1.0

$ AnimateValueChange(random.randint(-10, -1), random.uniform(0.1, 0.9))

hide cherenmodel

show cheren uniform noshine surprisedbrow at leftside with dis

cheren @disappointedmouth "This... this isn't what..."

$ AnimateValueChange(random.randint(-10, -1), random.uniform(0.1, 0.9))

hide serenamodel

show serena uniform angry at rightside with dis:
    xzoom -1

serena @talkingmouth "You are a... a... fuckin' shithead, you know that, Cheren? You {i}ASSHOLE!{/i}"

$ AnimateValueChange(random.randint(-10, -1), random.uniform(0.1, 0.9))

show calem uniform surprised with dis

calem surprisedbrow frownmouth @surprised "S-Serena? Why are you... what happened to your accent...?"

serena sad "Wait! Calem, wait, I can explain!"

hide serena
hide cheren
hide calem
with dis

pause 1.0

$ AnimateValueChange(random.randint(-10, -1), random.uniform(0.1, 0.9))

grusha @surprisedeyes surprisedeyebrows sweat shadow "Jasmine. Jasmine, help. It's happening. Again. My heart. It's happening."

jasmine @closedbrow frownmouth tears cry "Wh-wh-what?"

$ AnimateValueChange(random.randint(-10, -1), random.uniform(0.1, 0.9))

jasmine @surprised tears "N-no! Grusha, hold on, I'll get a nurse!"

grusha @deadeyes shadow surprisedeyebrows sweat "No time. No--{w=0.5} I can't breathe. I can't{w=0.5} breathe!"

show grusha noscarf as grushamodel with Dissolve(1.0)

grusha uniform @sad shadow noscarf sweat "...Gotta. Gotta get to... infirmary. Feeling... faint..."

show grusha as grushamodel:
    xpos 0.35 ypos .41
    ease 1.0 ypos 0.415 xpos 0.36
    ease 1.0 ypos 0.42 xpos 0.35
    ease 1.0 ypos 0.425 xpos 0.36
    ease 0.5 ypos 0.427
    ease 0.3 ypos 0.46 alpha 0.0 rotate 10

pause 4.0

show orientation
show auditorium_cover
with vpunch

jasmine @surprised shadow cry tears "Grusha!"

$ AnimateValueChange(random.randint(-10, -1), random.uniform(0.1, 0.9), pausing=False)
$ AnimateValueChange(random.randint(-10, -1), random.uniform(0.1, 0.9), pausing=False)
$ AnimateValueChange(random.randint(-10, -1), random.uniform(0.1, 0.9), pausing=True)

pause 1.0

$ AnimateValueChange(random.randint(-10, -1), random.uniform(0.1, 0.9))

show flannery angry at rightside with dis

flannery "Oh, I'm just a {i}project{/i}, is that it?!"

$ AnimateValueChange(random.randint(-10, -1), random.uniform(0.1, 0.9))

show whitney sad at leftside with dis

whitney sad "W-w-wait, Flan, c'mon, you know there's more to it than that!"

$ AnimateValueChange(random.randint(-10, -1), random.uniform(0.1, 0.9))

show flannery:
    xpos 0.75
    ease 0.5 xpos -0.3

$ AnimateValueChange(random.randint(-10, -1), random.uniform(0.1, 0.9))

show whitney:
    xpos 0.25
    ease 0.5 xpos -0.1

$ AnimateValueChange(random.randint(-10, -1), random.uniform(0.1, 0.9))

flannery furious "Nnnnngah!"

show erika angrybrow frownmouth with dis

$ AnimateValueChange(random.randint(-10, -1), random.uniform(0.1, 0.9))

erika @talking2mouth "...How very disappointing. If you wish to preserve what little dignity you have left, I trust you know what to do, [first_name]."

hide erika with dis

$ AnimateValueChange(random.randint(-10, -1), random.uniform(0.1, 0.9))
$ AnimateValueChange(random.randint(-10, -1), random.uniform(0.1, 0.9))
$ AnimateValueChange(random.randint(-10, -1), random.uniform(0.1, 0.9))

camera master at Transform(matrixcolor=SaturationMatrix(0.9))

narrator "{cps=20}You cannot speak.{/cps}"

camera master at Transform(matrixcolor=SaturationMatrix(0.8))

hide whitney
hide flannery

$ charname = chars[2][1]

if (charname == "Leaf"):
    show leaf sad at leftside with dis

    leaf "Hey. C'mon. Tell me this isn't true."

elif (charname == "Dawn"):
    show dawn sad at leftside with dis

    dawn "Please tell me that you can explain this... that there's something Cheren overlooked..."

elif (charname == "Serena"):
    show serena uniform sad at leftside with dis

    serena "You can explain this, right? Please... please tell me the conspirators are liars. Please?"

elif (charname == "Hilda"):
    show hilda angry at leftside with dis

    hilda "What the hell, dude?! You can explain this, right? Cheren's just full of shit, {i}right?!{/i}"

    pause 1.0
    
    hilda sad "Right...?"
    
elif (charname == "Rosa"):
    show rosa sad at leftside with dis

    rosa "Tell me this isn't true, [first_name]. Tell me this is just a... a bad script, and you're about to yell 'cut' any moment now..."

elif (charname == "May"):
    show may sad at leftside with dis

    may "C'mon, [first_name]. Please. Tell me that you can explain this."

elif (charname == "Silver"):
    show silver sad at leftside with dis

    silver sad "C'mon. I did the whole 'attack' for you. You don't really have these wacked-out powers, do you?"

elif (charname == "Nessa"):
    show nessa sad at leftside with dis

    nessa "...I knew you were too good to be true. But... just in case... do you have an explanation? Can you tell me that guy's wrong? ...Please?"

elif (charname == "Skyla"):
    show skyla sad at leftside with dis

    skyla "...C'mon, [first_name]. You don't actually have supervillain powers, right? You can reveal the plot twist now..."

elif (charname == "Misty"):
    show misty sad at leftside with dis

    misty "I thought... I thought I actually liked you... but it was really just an ability, this whole time? Tell me I'm wrong."

elif (charname == "Bea"):
    show bea sad at leftside with dis

    bea "I... I don't know how to process these feelings. I cannot hide them. You... you are... do you actually have these powers?"

elif (charname == "Flannery"):
    show flannery sad at leftside with dis

    flannery "C'mon, man. With Whitney being a fake friend this whole time, I need you to tell me that your powers aren't real. C'mon. Please."

elif (charname == "Sonia"):
    show sonia sad at leftside with dis

    sonia "I... never expected you to be the sort of fellow to meddle in these sorts of dealings. Will you tell me I'm wrong? I'd believe it. Promise."

elif (charname == "Whitney"):
    show whitney sad at leftside with dis

    whitney "Hey, man. I really thought we had something together, like... we understood each other. And now that guy is saying this is all just because of an ability?"
    whitney "Please tell me that he's crazy. You can do that, right?"

elif (charname == "Hilbert"):
    show hilbert sad at leftside with dis

    hilbert "Hmph. So, you really do have a power, huh?"

camera master at Transform(matrixcolor=SaturationMatrix(0.7))

$ ValueChange(charname, -3, 0.25)

pause 1.0

camera master at Transform(matrixcolor=SaturationMatrix(0.6))

narrator "{cps=20}You cannot speak.{/cps}"

camera master at Transform(matrixcolor=SaturationMatrix(0.5))

$ charname = chars[1][1]

if (charname == "Leaf"):
    show leaf sad at rightside with dis

    leaf "Hey. C'mon. Tell me this isn't true."

elif (charname == "Dawn"):
    show dawn sad at rightside with dis

    dawn "Please tell me that you can explain this... that there's something Cheren overlooked..."

elif (charname == "Serena"):
    show serena uniform sad at rightside with dis

    serena "You can explain this, right? Please... please tell me the conspirators are liars. Please?"

elif (charname == "Hilda"):
    show hilda angry at rightside with dis

    hilda "What the hell, dude?! You can explain this, right? Cheren's just full of shit, {i}right?!{/i}"

    pause 1.0
    
    hilda sad "Right...?"
    
elif (charname == "Rosa"):
    show rosa sad at rightside with dis

    rosa "Tell me this isn't true, [first_name]. Tell me this is just a... a bad script, and you're about to yell 'cut' any moment now..."

elif (charname == "May"):
    show may sad at rightside with dis

    may "C'mon, [first_name]. Please. Tell me that you can explain this."

elif (charname == "Silver"):
    show silver sad at rightside with dis

    silver sad "C'mon. I did the whole 'attack' for you. You don't really have these wacked-out powers, do you?"

elif (charname == "Nessa"):
    show nessa sad at rightside with dis

    nessa "...I knew you were too good to be true. But... just in case... do you have an explanation? Can you tell me that guy's wrong? ...Please?"

elif (charname == "Skyla"):
    show skyla sad at rightside with dis

    skyla "...C'mon, [first_name]. You don't actually have supervillain powers, right? You can reveal the plot twist now..."

elif (charname == "Misty"):
    show misty sad at rightside with dis

    misty "I thought... I thought I actually liked you... but it was really just an ability, this whole time? Tell me I'm wrong."

elif (charname == "Bea"):
    show bea sad at rightside with dis

    bea "I... I don't know how to process these feelings. I cannot hide them. You... you are... do you actually have these powers?"

elif (charname == "Flannery"):
    show flannery sad at rightside with dis

    flannery "C'mon, man. With Whitney being a fake friend this whole time, I need you to tell me that your powers aren't real. C'mon. Please."

elif (charname == "Sonia"):
    show sonia sad at rightside with dis

    sonia "I... never expected you to be the sort of fellow to meddle in these sorts of dealings. Will you tell me I'm wrong? I'd believe it. Promise."

elif (charname == "Whitney"):
    show whitney sad at rightside with dis

    whitney "Hey, man. I really thought we had something together, like... we understood each other. And now that guy is saying this is all just because of an ability?"
    whitney "Please tell me that he's crazy. You can do that, right?"

elif (charname == "Hilbert"):
    show hilbert sad at rightside with dis

    hilbert "Hmph. So, you really do have a power, huh?"

camera master at Transform(matrixcolor=SaturationMatrix(0.4))

$ ValueChange(charname, -5, 0.75)

pause 1.0

camera master at Transform(matrixcolor=SaturationMatrix(0.3))

narrator "{cps=20}You cannot speak.{/cps}"

camera master at Transform(matrixcolor=SaturationMatrix(0.2))

$ charname = chars[0][1]

if (charname == "Leaf"):
    show leaf sad with dis

    leaf "Hey. C'mon. Tell me this isn't true."

elif (charname == "Dawn"):
    show dawn sad with dis

    dawn "Please tell me that you can explain this... that there's something Cheren overlooked..."

elif (charname == "Serena"):
    show serena uniform sad with dis

    serena "You can explain this, right? Please... please tell me the conspirators are liars. Please?"

elif (charname == "Hilda"):
    show hilda angry with dis

    hilda "What the hell, dude?! You can explain this, right? Cheren's just full of shit, {i}right?!{/i}"

    pause 1.0
    
    hilda sad "Right...?"
    
elif (charname == "Rosa"):
    show rosa sad with dis

    rosa "Tell me this isn't true, [first_name]. Tell me this is just a... a bad script, and you're about to yell 'cut' any moment now..."

elif (charname == "May"):
    show may sad with dis

    may "C'mon, [first_name]. Please. Tell me that you can explain this."

elif (charname == "Silver"):
    show silver sad with dis

    silver sad "C'mon. I did the whole 'attack' for you. You don't really have these wacked-out powers, do you?"

elif (charname == "Nessa"):
    show nessa sad with dis

    nessa "...I knew you were too good to be true. But... just in case... do you have an explanation? Can you tell me that guy's wrong? ...Please?"

elif (charname == "Skyla"):
    show skyla sad with dis

    skyla "...C'mon, [first_name]. You don't actually have supervillain powers, right? You can reveal the plot twist now..."

elif (charname == "Misty"):
    show misty sad with dis

    misty "I thought... I thought I actually liked you... but it was really just an ability, this whole time? Tell me I'm wrong."

elif (charname == "Bea"):
    show bea sad with dis

    bea "I... I don't know how to process these feelings. I cannot hide them. You... you are... do you actually have these powers?"

elif (charname == "Flannery"):
    show flannery sad with dis

    flannery "C'mon, man. With Whitney being a fake friend this whole time, I need you to tell me that your powers aren't real. C'mon. Please."

elif (charname == "Sonia"):
    show sonia sad with dis

    sonia "I... never expected you to be the sort of fellow to meddle in these sorts of dealings. Will you tell me I'm wrong? I'd believe it. Promise."

elif (charname == "Whitney"):
    show whitney sad with dis

    whitney "Hey, man. I really thought we had something together, like... we understood each other. And now that guy is saying this is all just because of an ability?"
    whitney "Please tell me that he's crazy. You can do that, right?"

elif (charname == "Hilbert"):
    show hilbert sad with dis

    hilbert "Hmph. So, you really do have a power, huh?"

camera master at Transform(matrixcolor=SaturationMatrix(0.1))

$ ValueChange(charname, -10, 0.5)

pause 1.0

camera master at Transform(matrixcolor=SaturationMatrix(0.0))

red shadow noeyes frownmouth tears cry "{w=0.5}.{w=0.5}.{w=0.5}."

narrator "{cps=20}You cannot speak.{/cps}"

$ i = 0

show blank2:
    alpha 0.0

stop music fadeout 10.0 channel "crowd2"
stop music fadeout 10.0 channel "crowd"
stop music fadeout 15.0

while (i < 150):
    $ i += 1
    show blank2:
        alpha (i / 100)
    $ AnimateValueChange(random.randint(-10, -1), random.uniform(0.1, 0.9), pausing = (i == 150))
    pause 0.02

narrator "{cps=5}You cannot speak.{/cps}"

pause 10.0

jump day010502