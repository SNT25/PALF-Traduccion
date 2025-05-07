label secondhomeroom010511:

scene blank2

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom behind blank2

show oakbg behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade

oak @talkingmouth "Good afternoon, ladies and gentlemen!" 

oak @talkingmouth "Let's talk about Pokémon morality. Now, it is a common sentiment that Pokémon are inherently good. Certainly, they only seem capable of doing classically 'evil' acts when being coerced, or enraged."
oak @talkingmouth "That being the case, how do we rationalize this truth against the destruction that has famously been caused by various Legendary Pokémon? Well, various..."

if (HasEvent("Cheren", "RejectCherenMeeting")):
    oak "...Eh?"

    redmind uniform @thinking "Hm? It's not like Sam to just stop lecturing like that."

    hide oakbg

    pause 0.5

    show oak with dis

    pause 0.5

    oak @talkingmouth "Mr. [last_name]? It seems the Disciplinary Committee wants to, er, wants to see you."

    red @angrybrow angrymouth "Seriously? He's going to drag me out in the middle of homeroom?"

    oak @talking2mouth "I don't know what this is about, but I think you should, er, probably go attend to it."

    red @closedbrow talking2mouth "Unbelievable."

    show leaf uniform at leftside with dis:
        ypos 1.2 zoom 1.3

    leaf @sadbrow talkingmouth "I'll take notes for you."

    red @upeyes talking2mouth "Thanks."

    oak @happy "Hurry up, now. If you can finish your meeting swiftly enough, perhaps you can come back before the end of class."

    call clearscreens from _call_clearscreens_147
    scene blank2 with splitfade 

    narrator "You grudgingly trudge toward the Disciplinary Committee's office."

    show screen songsplash("Embracing One's Duty", "Zame")
    stop music fadeout 1.5
    queue music "audio/music/embracingonesduty.ogg"

    scene studentcouncil
    show cheren uniform noshine
    show skyla uniform surprised at leftside
    with splitfade

    pause 1.0

    skyla -surprisedbrow -frownmouth -surprised @surprised "W-woah! Boss! He actually came!"

    cheren @talking2mouth "I told you he would."

    if (GetRelationshipRank("Skyla") > 0):
        $ skylarelationship = GetRelationship("Skyla")
        red uniform @sadbrow talking2mouth "Skyla? You're working with {i}him?{/i} Aren't I meant to be {i}your{/i} [skylarelationship]?"

        skyla @talkingmouth "...Yes. But it's not because of you! It's because of Sabrina! What happened to her was {i}awful,{/i} and I want to make sure nothing like that happens again."

        cheren @talking2mouth "Relatedly, it is the matter of Sabrina that made me bring [first_name] here today."

    cheren @closedbrow talking2mouth "When you're done with the paperwork, you can go."

    skyla @sweat happy "Uh... I think it might be a {i}long{/i} time before I'm done with this paperwork... Should I just go into the side office?"

    cheren @talking2mouth "{w=0.5}.{w=0.5}.{w=0.5}.I suppose you might as well stay. This concerns you, too. Is Silver not around?"

    red uniform @angryeyebrows talking2mouth "Right... Silver's working with you, too."

    cheren @sad2eyes talking2mouth "Yes."

    pause 0.5

    if (HasEvent("Cheren", "StrongHate")):
        cheren @closedbrow talking2mouth "If it's any consolation, he despises me as much as you do."
    else:
        cheren @talking2mouth "If it's any consolation, he despises me as much as any other student."

    cheren @sad2eyes talkingmouth "The Disciplinary Committee is certainly not formed around the charisma of its head."

    pause 1.0

    cheren @talking2mouth "Skyla, Silver?"

    skyla @surprised "Oh, right! Um... I don't know. He said he was heading out for a smoke."

    cheren @talking2mouth "I do not believe he smokes."

    skyla @happy sweat "Yeah, I've never seen that."

    cheren @talking2mouth "Whatever. Enough ado."

    pause 0.5

    cheren @talking2mouth "[first_name], Sabrina Natsume is missing. Bianca Vongole is too."

    redmind @confusedeyebrows frownmouth "{i}Natsume?{/i}"

    cheren @talking2mouth "They are likely in the burned forest. Instructor Will was sent in after them. He has also failed to return."

    red @talking2mouth "...Well?"

    cheren @closedbrow talking2mouth "It would reflect poorly on the Disciplinary Committee if we were unable to retrieve these missing personnel."
    cheren @talking2mouth "Even moreso if another unaffiliated student {i}were{/i} to do so."

    red @angryeyes frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    cheren @talking2mouth "For this reason, it is instructed that you do not leave the campus at night to venture into the forest. Such an activity would be foolhardy, dangerous, and {i}not{/i} endorsed."
    cheren @talking2mouth "Of course, as is always the case, there is no way I could stop you from doing what you want."

    pause 0.5

    red @talking2mouth angryeyes "I understand."

    cheren @talking2mouth "The exception to this, of course, is if you were to assist in the Disciplinary Committee's own retrieval efforts."
    cheren @sad2eyes talking2mouth "We aim to bring back Instructor Will--perhaps his knowledge could be of some use to us in retrieving the other two."

    if (GetRelationshipRank("Sabrina") > 0):
        red @talkingmouth "Really? You did all that shit to Sabrina, and you're not trying to rescue {i}her?{/i}"

        cheren @talking2mouth "I am trying to rescue {i}everyone.{/i} Instructor Will is the logical person to seek out first--he will give us greater odds in the other pursuits."
        cheren @closedbrow talking2mouth "I do not expect you to believe, nor understand me, but my guilt for what my actions have done to Sabrina is immense."
        cheren @upeyes talking2mouth "Clearly, though, because I am attempting to pursue the path that gives everyone the greatest chance for a happy ending, I am a monster."

    red @talking2mouth "...At night, you said?"

    cheren @talking2mouth "That would be preferable. Though if you can manage it in your evenings, more power to you."
    cheren @talkingmouth "We also cannot stop you from bringing any accomplices along on these excursions. That being said..."
    cheren @closedbrow talking2mouth "There may be... {i}complications{/i}, if others were to see how dire the situation is."
    cheren @talking2mouth "For that reason, if you choose to callously disregard the Disciplinary Committee's instructions and succeed in rescuing someone, we ask you bring them straight to the infirmary, and inform us at your leisure."
    cheren @talking2mouth "There is no need to involve any except the minimum required to rescue everyone in this mess."

    pause 1.0

    cheren @talking2mouth "...I'd recommend doing it soon, too. They've already been missing quite a while. I shudder to imagine what might happen if they were left there any longer than Friday." 
    cheren @closedbrow sadmouth "Sunday is the absolute last day they have before... Dean Drayden's backup plan arrives."

    pause 0.5
    
    cheren @talkingmouth "Speaking of, given that the Disciplinary Committee spent all week, last week, looking for the missing students and faculty, and failed, I managed to secure a reprieve of penalty from Dean Drayden."
    cheren @talkingmouth "The students who missed the Quarter Qlashes will not be punished. Unfortunately, they will still not be able to participate in any future Quarter Qlashes, but that's a matter for the Kobukan league, not our academy."
    cheren @sad2eyes talkingmouth "Of course, Drayden was disappointed to hear that the Disciplinary Committee had failed to find the people in question. He would be further disappointed to hear we have failed again."

    pause 1.0 

    cheren @closedbrow talking2mouth "But that's a consequence we Disciplinary Committee members will face. Live as you wish."

    pause 0.5

    cheren @closedbrow talking2mouth "Do you have any questions?"

    menu:
        "Why'd you do it?":
            cheren @sad2eyes talkingmouth "Why?"

            pause 1.0

            cheren @talking2mouth "Skyla, would you please give us some time?"

            hide skyla with dis

            pause 0.5

            red @sadbrow talking2mouth "I thought we were friends, man. I trusted you. I even supported you. I was going to {i}vote{/i} for you."

            cheren @talking2mouth "And I to you."

            pause 0.5

            cheren @talking2mouth "So why didn't you tell me about your power?"
            cheren @angryeyes talking2mouth "Why didn't you tell {i}anyone{/i}?"

            pause 1.0

            cheren @talking2mouth "You may not believe this, but I felt no ill will to you. I still do not. But I absolutely cannot understand you. And, as it seems everyone else can, I cannot understand them, either."

            red @talking2mouth "I only wanted to help people, man. People would be weirded out if they knew I had a power. I didn't want to do that to them."

            cheren @talking2mouth "So your silence was for the greater good."

            red @talking2mouth "Yes."

            cheren @talking2mouth "Then my lack of silence was for the same."
            cheren @sad2eyes talking2mouth "They adored you. Everyone. And they didn't even know why. You could have given them the courtesy of giving them a choice as to whether they loved you."

            red @closedbrow talkingmouth "Look, it's not mind control-"

            cheren @angryeyes angrymouth "I {i}know{/i} it's not mind control! It was never about if it was mind control or not! It was about the way people fawned over you with little to no effort on your own part!"
            cheren @sad2eyes angryeyebrows angrymouth "Certainly, I feared that it {i}may{/i} be mind control, but regardless of what it was, it clearly had to {i}stop!{/i}"

            pause 1.0

            cheren @upeyes talking2mouth "And, somehow, the speech you gave to the entire student body has convinced them that {i}I{/i} was wrong--as though you were not admitting to exactly what I accused you of."

            pause 1.0

            red @talkingmouth "Does it matter if people like me a little more easily? I'm not a bad guy. I'll only help people."

            pause 0.5

            cheren @talking2mouth "There is a story from Galar. Perhaps you're familiar with it."
            cheren @closedbrow talking2mouth "There was a noble king, wise and fair. He gathered about him eleven honorable knights, brave and just, and one more. These knights followed the king's every word, and never questioned his goodness."
            cheren @talking2mouth "With him, he had a wife. But the king was a busy man, as he had many adoring citizens to appease. He could not pay attention to his wife. So this wife's heart strayed, and she fell in love with the twelfth knight."
            cheren @talking2mouth "The king's wife, and this knight, eloped. The punishment for leaving the king was death. So the king, with a heavy heart, ordered his men to find and murder his wife and knight."

            pause 1.0

            cheren @sad2eyes talking2mouth "So they obeyed."
            cheren @talking2mouth "Isn't it interesting? These eleven knights, who were good men, expressed loyalty, a virtue. But these good men, driven by a virtue, did evil work."

            red @talking2mouth playfuleyes unamusedeyebrows "I don't get it."

            cheren @talking2mouth "It is a {i}danger{/i}, [first_name], for there to be any man whose goodness is unquestioned. Who engenders loyalty beyond logic."
            cheren @talking2mouth "Even with all I've done, I only managed to slow you down. I now rely on my classmates' ability to stop themselves from becoming hopelessly dependent on you."

            pause 0.5

            cheren @upeyes talkingmouth "I may as well rely on a Magikarp to climb a waterfall. But I've done all I can."
            cheren @talking2mouth "...I do not expect us to speak again, except when necessary. We are fated, I believe, to misunderstand each other forevermore."

            red @sadbrow talking2mouth "I don't want that."

            cheren @talking2mouth "We don't always get what we want, [first_name]."

            pause 1.0

            cheren @talking2mouth "Oh, and one more thing."

            if (ninetalesobj in playerparty):
                cheren @talking2mouth "I'm aware of that Ninetales you carry on your belt."

            else:
                cheren @talking2mouth "You may recall that Ninetales that was outside Pledge Hall."

            cheren @talking2mouth "In the event that any more of these 'wild' Pokémon attack the school, I will be turning over every leaf and stone in order to find proof you are the one doing it."

            red @upeyes talking2mouth "I'm not."

            cheren @surprisedeyebrows talking2mouth "Hm?"

            pause 1.0

            cheren @closedbrow talking2mouth "Well... perhaps it is no surprise that I believe you. But that does {i}not{/i} mean you are telling the truth."

            redmind @thinking "Geez."

            cheren @talking2mouth "That is all. You may go back to class."

            pause 2.0

            $ ValueChange("Cheren", -5, 0.5)

            cheren shadow sad2eyes talking2mouth "I just don't understand that man..."

        ">Leave without a word":
            show skyla surprisedbrow frownmouth with dis

            pause 0.5

            cheren closedbrow shadow "Hm."

    call clearscreens from _call_clearscreens_148
    scene blank2 with splitfade

    pause 1.0

    scene homeroom 
    show screen currentdate
    with splitfade

    narrator "You make it back to class moments before the bell rings."

    redmind uniform @upeyes frownmouth "Great. Now I've gotta use {i}Leaf's{/i} notes. I can't read those."

elif (HasEvent("Cheren", "PunchCheren")):
    $ persistent.cherenpunchend = True

    oak "...Eh?"

    redmind uniform @thinking "Hm? It's not like Sam to just stop lecturing like that."

    hide oakbg

    pause 0.5

    show oak with dis

    pause 0.5

    oak @talkingmouth "Mr. [last_name]? It seems that Dean Drayden wants to, er, wants to see you."

    red @angrybrow angrymouth "Seriously? He's going to drag me out in the middle of homeroom?"

    oak @talking2mouth "I don't know what this is about, but I think you should, er, probably go attend to it. He said he's in the Disciplinary Committee's office."

    red @closedbrow talking2mouth "Unbelievable."

    show leaf uniform at leftside with dis:
        ypos 1.2 zoom 1.3

    leaf @sadbrow talkingmouth "I'll take notes for you."

    red @upeyes talking2mouth "Thanks."

    oak @happy "Hurry up, now. If you can finish your meeting swiftly enough, perhaps you can come back before the end of class."

    call clearscreens from _call_clearscreens_149
    scene blank2 with splitfade 

    narrator "You grudgingly trudge toward the Disciplinary Committee's office."

    stop music fadeout 1.5

    scene studentcouncil
    show drayden angry
    with splitfade

    show screen songsplash("Drought", "Zame")

    play music "audio/music/drought.ogg"

    show drayden:
        ease 0.5 ypos 1.2 zoom 1.3

    show studentcouncil with vpunch

    drayden "Mr. [last_name]! Do you realize what you've done?!"

    red uniform @surprised "Wo-wo-woah! What happened?!"

    drayden "You have assaulted another student--a student {i}I,{/i} Drayden, put into a position of responsibility--{i}on school grounds!{/i}"

    red @surprised "I--"

    drayden "There are {i}no{/i} excuses for this! There is {i}no{/i} justification, and there can be {i}no{/i} leniency!"

    show drayden:
        ease 0.5 ypos 1.0 zoom 1.0

    drayden @sadbrow "You foolish child..." 

    drayden "You punched him in the middle of a crowded cafeteria! Hundreds of students saw! The news has spread! And my position here was already hanging by a {i}thread{/i}, after the fiasco two weeks ago!"

    red @sadbrow talking2mouth "I'm sor-"

    drayden @sadbrow "It is clear to me now that keeping you at this school is more trouble than your tuition is worth. I have sorely misjudged you."

    red @surprised "W-w-w-wait! No, don't!"

    drayden -angry "[first_name] [last_name], you are no longer welcome on these premises. Pack your bags and leave these grounds immediately. If you have not evacuated by the end of Friday, then you will be removed."

    red @sad "Wait, wait, wai-"

    drayden "The amount of your tuition that is due, after subtracting the amount of school you will {i}not{/i} be attending, is $1.2 million."
    drayden "See that you pay that amount expediently. There will be no waivers or scholarship offered, obviously."

    red @sadbrow talking2mouth "I... I can't..."

    drayden "If you cannot pay, then Kobukan Academy will have no recourse but to initiate legal proceedings against you, to make your insurance pay."

    pause 0.5

    drayden sad "{size=30}Damn it, boy.{/size}"

    drayden "This was... all {i}so{/i} avoidable..."

    pause 1.0

    drayden @angry "There {i}is{/i} a time for violence. This was not it. This was not even {i}approximate{/i} to it."

    drayden "...I am {i}so{/i} disappointed in you."

    stop music fadeout 5.0

    call clearscreens from _call_clearscreens_150
    scene blank2 with Dissolve(5.0)

    play sound "audio/shovel.ogg" fadein 30.0 loop 

    narrator "[first_name] [last_name]'s life ends here."
    narrator "Not in the literal sense, but in the figurative sense, where his dreams fail to ever receive as much traction as before."
    narrator "Without friends around, [first_name] quickly regresses to the silent shell of who he was before."
    narrator "Without friends, [pika_name] stops producing Foreverals, and even his somewhat-unique form soon becomes nothing more than mere novelty."

    pause 1.0

    narrator "All from one decision."

    pause 1.0

    narrator "Isn't that fucked up? Like, a single decision can ruin your life? You can make a single decision and end up in jail, or homeless, or poor, or dead."
    narrator "But it's not like you could ever make a single decision that would make you a millionaire, or a muscular, leather-clad adonis."
    narrator "You can accidentally make a baby, but you can't accidentally make a sandwich. That's totally unfair."

    pause 1.0

    narrator "...Anyway, this is"

    show gameover at truecenter

    pause 10

    $ MainMenu(confirm=False)()

else:
    narrator "Professor Oak continues to lecture, though the topic doesn't seem very relevant to battles or training. You're tired... will you take a nap?"

    menu:
        "{color=#ff8412}[[Courage]{/color} I can read up later.":
            $ learnedaboutlegendaries = 0

            $ TraitChange("Courage")
            
            redmind uniform @happy "There's nothing wrong with a little nap."

            scene blank2 with transeye

            pause 2.0

            $ PlaySound("BellChime.ogg")

            scene homeroom with transeye2

        "{color=#66b77d}[[Knowledge]{/color} Education is important!":
            $ learnedaboutlegendaries = 1

            $ TraitChange("Knowledge")

            redmind uniform @angrybrow frownmouth "I'm paying way too much to be at this school to waste a second of it."
            redmind @closedbrow sweat frownmouth "...Well, I {i}would{/i} be paying way too much if I had any money to pay with."

            narrator "You stay wide awake for the lecture and learn more about legendary Pokémon."

            $ PlaySound("BellChime.ogg")

oak @talkingmouth "And that's the bell. You run along now! Enjoy your evening!"

narrator "You stand up to leave, when..."

show leaf angrybrow happymouth uniform:
    xpos -0.2
    ease 0.5 xpos 0.75

show flannery angrybrow happymouth uniform:
    xpos 1.2
    ease 0.5 xpos 0.25

show whitney angrybrow happymouth uniform:
    ypos 2.0
    ease 0.5 ypos 1.0

stop music fadeout 1.5
queue music "audio/music/goldenrod_start.ogg" noloop
queue music "audio/music/goldenrod_loop.ogg"

flannery @talking2mouth "Not so fast, [first_name]!"

whitney @talking2mouth "Yeah! We talked it over at lunch, and we're hella motivated now! We're going to rescue Tia, no matter what!"

leaf @talking2mouth "I agree with what those two said!"

pause 1.0

red uniform @talkingmouth "Okay. And the posing is...?"

show leaf -angrybrow -happymouth
show flannery -angrybrow -happymouth
show whitney -angrybrow -happymouth
with dis

whitney @talking2mouth "For fun, mostly."

leaf @talking2mouth "The [first_name] Rescue Team has been reformed! We're now the Tia Rescue Team!"

flannery @talkingmouth "Yeah. And we're going out to save Tia tonight, no matter what happens! No matter how much trouble we get in!"

whitney @talking2mouth "She's like our little sister. And I never leave my little sister in the lurch for {i}seven{/i} days."

red @confusedeyebrows talking2mouth "You seem weirdly calm about her being missing for that long."

whitney @talking2mouth "Oh, yeah, I know about her. You know. {i}About{/i} her."

red @surprised "What?! Since when?!"

whitney @talking2mouth "Since I found out that Yellow, who can speak Pokémon, can talk to her. That was kinda a giveaway."

leaf @talking2mouth "She can't talk to Pokémon."

whitney @closedbrow talkingmouth "Whatever, she {i}basically{/i} can."

flannery @upeyes talking2mouth "Well, {i}I{/i} learned a couple minutes ago. I'll believe it when I see it."

red @talkingmouth "Well, I've got some good news for the Tia Rescue Team."

show whitney frownmouth with dis

leaf @sadbrow talking2mouth "Oh, thank god. We honestly really needed it. We're acting all gung-ho about it, but I'm pretty sure we're all terrified of what this'll take."

whitney @sad "Yeah..."

flannery @talking2mouth "...Wait, you guys aren't actually excited about this?"

whitney @closedbrow talkingmouth "Hey, you train Fire-types. It's a forest. It makes sense {i}you'd{/i} be excited."

red @talking2mouth "Guys."

leaf @talkingmouth "Right, good news. Lay it on us, skippy."

red @talkingmouth "I have permission to go out into the forest and search. Even at night, if you wanted."
red @happy "And I can take people with me, too. So... yeah, you guys won't get in any trouble."

leaf @talking2mouth "Wait... you got permission to go out? Even at night?"

red @talking2mouth "Yup."

leaf @talkingmouth "Uh... {i}how?{/i}"

red @sad2eyes talking2mouth "I think that Cheren thinks if I get eaten by a wild Ursaring, I won't be his problem anymore."

pause 0.5

red @happy "Joke's on him, I'm totally going to haunt him."

whitney -frownmouth @happy "That's suspicious, weird, and irresponsible, but hey, it's good for us!"

whitney @talking2mouth "Anyway, we're ready to go pretty much anytime. You know how to contact us when you're ready, right?"

red @talkingmouth "Yeah."

whitney @happy "Cool!"
whitney @talking2mouth "...Um. For the record... I'm sure Tia's fine out there... but don't leave her too long, alright? She's strong, but she doesn't like to be alone for too long."

red @talkingmouth "Don't worry. I'll save all three of them before the week's over."

red @closedbrow talking2mouth "...Or... I'll try, at least."

hide flannery
hide whitney
hide leaf
with dis

pause 1.0

show blank2 with splitfade

pause 1.0

narrator "You go back to your dorm and change."

pause 1.0

stop music fadeout 1.5
queue music "audio/music/joinavenue_start.ogg" noloop
queue music "audio/music/joinavenue_loop.ogg"

show screen songsplash("Join Avenue", "Zame")

show hall_B with splitfade

pause 1.0

show ethan with dis:
    xpos -0.2
    ease 1.0 xpos 0.75

show rosa with dis:
    xpos -0.2
    ease 1.0 xpos 0.5

show nessa with dis:
    xpos -0.2
    ease 1.0 xpos 0.25

rosa @talkingmouth "{size=30}And{/size} {size=26}I{/size} {size=27}know{/size} {size=28}they're{/size} {size=29}kinda{/size} {size=30}small{/size} and weird-looking, but... I don't know... I like them!"

ethan @happy "Hey, you don't need to justify why you love your Scrimblo McDingus. We've all got one."

rosa @talking2mouth "Yeah, but it's different with me, 'cause--"

if (GetRelationshipRank("Rosa") > 1):
    rosa @surprised "[first_name]! Oh! I was looking for you!"

    ethan sad2eyes sadmouth "{size=30}And... end scene.{/size}"

else:
    ethan @surprised "Oh, here's your guy."

    rosa @happy "Oh, right! Thanks, Ethan."

    ethan @happy "No problem, Rosa."

hide ethan with dis

show nessa:
    ease 0.5 xpos 0.66

show rosa:
    ease 0.5 xpos 0.33 xzoom -1

rosa @talkingmouth "[first_name], this is going to sound crazy, but--"

show nessa surprisedbrow frownmouth
show rosa surprisedbrow frownmouth

red @talkingmouth "You've formed a rescue team to go into the forest and retrieve Sabrina?"

pause 1.0

show nessa -surprisedbrow -frownmouth -surprised with dis

if (GetRelationshipRank("Nessa") > 0 and not HasEvent("Nessa", "DenyDate")):
    $ AddEvent("Rosa", "KnowsNessaDate")

    nessa @talkingmouth "So you're a mind-reader. You might've mentioned that on our date."

    red @closedbrow talkingmouth "Yeah, there was just a whole parcel of different psychic powers I was keeping hidden from you."

else: 
    nessa @talkingmouth "So he's a mind-reader."

    red @closedbrow talking2mouth "Jeez, don't even joke about that. Someone might hear you and start this whole thing over again."

pause 1.0

nessa @talkingmouth "Your speech on Friday..."

pause 0.5

nessa @sadbrow talkingmouth "That was real. It mattered. That was the kind of thing Leon would do. I'm impressed."

red @surprised "Oh. Well, uh--"

rosa -surprisedbrow -frownmouth -surprised @talkingmouth "Wait, wait, wait! How did you know about the Sabrina Salvation Squad?"

red @talkingmouth "Because I've already talked with the Will Wardens and the Bianca Brave Brigade?"

rosa @closedbrow talking2mouth "Bianca? Oh, you mean Tia?"

red @surprised "Wha-- you definitely aren't in the nursing program! How do you know that?"

rosa @talking2mouth "Everyone in the Psychic class knows about her. She's the only one who can block out Sabrina."

red @closedbrow talking2mouth "{size=30}I didn't know other people knew about this...{/size}"

show studentcouncil at sepia with dis
show flashback with dis

$ renpy.pause(1.0, hard=True)

show cheren upeyes talking2mouth at sepia behind flashback with dis

cheren @talkingmouth "You are not the center of the universe, [first_name]. People have conversations without you."

hide cheren
hide studentcouncil
hide flashback
with Dissolve(1.0)

pause 1.0

red @angryeyes talking2mouth "I do {i}not{/i} need {i}you{/i} in my head."

rosa @sadbrow talkingmouth "Sorry?"

red @surprised "Oh, no, sorry, I wasn't talking to you!"

nessa @surprisedbrow talkingmouth "Talking to Sabrina?"

red @talkingmouth "No, I haven't heard from her since Saturday."

nessa @talkingmouth "Damn. I was really hoping I could avoid going into the forest."

rosa @talkingmouth "Oh, right, you're not good against Grass-types..."

pause 1.0

rosa @angrybrow happymouth "Well, my new Dottler will make short work of them! Don't worry about it!"
rosa @sweat talkingmouth "But my Dottler can't do it alone. So we were hoping you'd come with us."

rosa @talkingmouth "Plus, Pikachu-trainer to Pikachu-trainer, I'm insanely curious about your Pikachu. How does it do what it does? That's crazy!"

red @talkingmouth "Sure. But between the other two rescue teams, I'll be pretty busy."

nessa @talkingmouth "It's fine. I spent all weekend preparing, so we're ready at a moment's notice. I knew that Rosa would end up making us do something like this."

rosa @surprised "What does {i}that{/i} mean?"

nessa @happy "It means you've got a good heart."
nessa @closedbrow talkingmouth "Anyway, I've packed rations, medical equipment, and set up a GPS on my phone, with a dead-man's switch to call the school if we're gone too long."

menu:
    "You really thought ahead, Nessa.":
        $ ValueChange("Nessa", 1, 0.66)

        nessa @sadbrow happymouth "Most just say I'm a worrywart. Thanks. I {i}am{/i} trying to help."

    "Rosa, I'm sure Sabrina really appreciate this.":
        $ ValueChange("Rosa", 1, 0.33)

        rosa @talkingmouth "I hope so. I've barely talked to her. But I really don't want her to just be a bit part--she needs more screentime."
        rosa @sadbrow talkingmouth "The least I can do is bring her back on."

    "[bluecolor][[Nessa Rank 1]{/color} I think Rosa brings out the best in you, Nessa." if GetRelationshipRank("Nessa") > 0:
        $ ValueChange("Nessa", 1, 0.66, False)
        $ ValueChange("Rosa", 3, 0.33)

        nessa @closedbrow happymouth "Maybe. She certainly lives in the moment. Typical yankee behavior."

        rosa @sweat sadbrow surprisedmouth "No, no, not that nickname! Not 'Yankee Buns!' No more!"

    "[bluecolor][[Rosa Rank 1]{/color} Looks like Nessa's a serious help to you, Rosa." if GetRelationshipRank("Rosa") > 0:
        $ ValueChange("Nessa", 3, 0.66, False)
        $ ValueChange("Rosa", 1, 0.33)

        rosa @sadbrow talkingmouth "I'll admit... I don't think I'd even be doing this without her."
        rosa @happy "And I {i}definitely{/i} wouldn't be surviving it!"

        nessa @closedbrow happymouth "Nah, you'd be fine. I'm just a worrywart."

pause 0.5

nessa @talkingmouth "...Oh, yeah, Sonia will be coming, too."
nessa @closedbrow talkingmouth "We're just heading to the lab to get her now, actually."

pause 1.0

nessa @talkingmouth "Give us a call when you're ready to go. You've got my number."

red @talkingmouth "Sure thing."

show sonia surprisedbrow frownmouth:
    xpos 1.2
    ease 0.5 xpos 0.75

show rosa surprisedbrow frownmouth:
    xpos 0.33 xzoom 1
    ease 0.5 xpos 0.25 xzoom -1

show nessa surprisedbrow frownmouth:
    xpos 0.66 xzoom -1
    ease 0.5 xpos 0.5

pause 0.3

sonia @talking2mouth "Wait!"

nessa -surprisedbrow -frownmouth -surprised @closedbrow talkingmouth "Speak of the devil."

rosa -surprisedbrow -frownmouth -surprised @talkingmouth "Hey, Sonia. What's up?"

sonia -surprisedbrow -frownmouth -surprised @angry "I learned something really important about the forest. It's got trace amounts of Mysteriosity!"

pause 1.0

rosa @sadbrow sweat talkingmouth "So, pretending that I don't know what that is..."

show rosa surprisedbrow frownmouth
show nessa surprisedbrow frownmouth
with dis

red @happy "A natural phenomenon that certain wild locations seem to exhibit. Woods, caves, oceans. Emeras can coalesce there." 

pause 1.5

red @confused "What? I can know stuff, too."

nessa -surprisedbrow -frownmouth -surprised @talkingmouth "Full of surprises, this one."

rosa -surprisedbrow -frownmouth -surprised @talkingmouth "Okay, but why's this important?"

sonia @talking2mouth "Right. The issue is that the Mysteriosity is extremely unpredictable. It can do pretty much anything, given half the chance."

nessa @closedbrow talkingmouth "What, specifically, can it do?"

sonia @sad "There's no specifics when it comes to Mysteriosity. It's not really a phenomenon even the best researchers understand, since it's so hard to study."
sonia @closedbrow talkingmouth "It might help you or hurt you. Sometimes it just drops random objects, or even entire places, in the middle of other places."
sonia @talking2mouth "But there's one thing that {i}is{/i} consistent. Pokémon exposed to it start to lose their reason and go crazy."
sonia @closedbrow talking2mouth "They become {i}Frenzied.{/i}"

nessa @talkingmouth closedbrow "Not ideal. What about our Pokémon? Are they immune?"

sonia @talkingmouth "I'm afraid not. Having a trainer around to guide them and command them is helpful, but the frenzying effect is even greater if there's more Pokémon, so bringing in a full team of six might be the worst thing you could do."

rosa @sadbrow talkingmouth "Even the ones in our Poké Balls...?"

sonia @talking2mouth "That won't stop it, no. If we're going in, bringing in more than one Pokémon per trainer is just going to be a hindrance."

red @sweat talking2mouth "Damn. I don't think the other teams know this..."

redmind @thinking "Guess I'd better tell them."

nessa @talkingmouth "Are there any workarounds? Can we {i}catch{/i} Pokémon in the Mysteriosity?"

sonia @talking2mouth "'Fraid not. I mean, you {i}can{/i} catch them, but keeping them on-hand is too risky. You should just teleport them to the PC."

rosa @closedbrow talkingmouth "Alright. That's something we'll need to keep track of, then."
rosa @happy "But it's fine! If we all bring a really different kind of Pokémon with us, we'll still be able to beat all the baddies and save the day!"

nessa @closedbrow talkingmouth "{size=30}I'm not sure... I might need to call {i}him{/i} in for this one.{/size}"

sonia @sad "Sorry to be, er, the bad news Bewear."

nessa @closedbrow talkingmouth "Better than us going in there and immediately having our Pokémon turn on us."
nessa @talkingmouth "You're good, Sunny. Don't worry about it."

rosa @talkingmouth "Alright! Let's make plans! I think..."

hide sonia
hide rosa
hide nessa
with dis

pause 1.0

show nessa talkingmouth with dis

nessa @talkingmouth "Hey."

red @talkingmouth "...Yeah?"

if (GetRelationshipRank("Nessa") > 0 and not HasEvent("Nessa", "DenyDate")):
    nessa "You remember our date?"

    red @happy "Can't forget it."

    nessa @sadbrow talkingmouth "If that meant... {i}anything{/i} to you... even a little bit... I need to ask a favor."

else:
    nessa @talkingmouth "I need to ask a favor."

red @talking2mouth "Yeah?"

nessa @talkingmouth "Wait until Thursday to go rescue Sabrina. I'm going to call someone who I think will be a massive help on this, but it'll take a while for them to get here."
nessa @closedbrow talkingmouth "If you can just wait {i}two{/i} more days, then we're much more likely to succeed."
nessa @sadbrow talkingmouth "Please. Show me you can be patient."

menu:
    "Alright, but this better pay off.":
        $ ValueChange("Nessa", 1, 0.5)

        nessa @talkingmouth "...It will. Promise."

        hide nessa with dis

    "I'll think about it.":
        $ ValueChange("Nessa", 1, 0.5)

        nessa @talkingmouth "...Thanks."

        hide nessa with dis

    "Sabrina needs help {i}now.{/i}":
        nessa @sad "...Alright."

        hide nessa with dis

narrator "[bluecolor]You can now access the three sections of the {b}Burned Forest.{/b}{/color} You can access it from the same area you access the fields."

narrator "[bluecolor]You are able to venture into the burned forest during your free time, or at night. You cannot currently do anything during nighttime except text someone, or go on a rescue mission.{/color}"

narrator "Now is a good time to SAVE, if you haven't already."

narrator "Finally, it is typically [bluecolor]{i}VERY{/i}{/color} strongly advised to utilize multiple save slots, when dealing with any sort of Visual Novel that permits it."

pause 0.5

narrator "Like this one."

pause 0.5 

narrator "{i}Hint hint.{/i}"

call freeroam from _call_freeroam_18

scene blank2 with Dissolve(2.0)

call nightroam from _call_nightroam

scene blank2

pause 2.0

jump day010512