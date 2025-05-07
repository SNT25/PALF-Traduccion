label secondhomeroom010525:

scene blank2

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

show oak 
hide blank2 
with splitfade

$ PlaySound("bellchime.ogg")

oak @closedbrow sweat talking2mouth "And that's the end of the lecture."

redmind uniform @thinking "He really is making an effort. This was another one of his class-long lectures, but it was actually about modern, practical, competitive battle strategies..."
redmind @sad2eyes sadeyebrows frownmouth "I wonder if I could've helped him, and my classmates, if I'd said something earlier..."

oak @talking2mouth "You're all free to go. Enjoy your evenings."

narrator "Sam's eyes linger on Melody, who has been on her phone for the entire class."

oak frownmouth @talking2mouth "Miss Melody."

show melody uniform on with dis:
    xpos 0.75

melody @talking2mouth "I'm texting."

pause 1.0

oak angrybrow @talking2mouth "That's the issue. You {i}should not be.{/i}"

pause 1.0

show melody:
    xzoom 1 xpos 0.75
    ease 0.5 xzoom -1

melody @bubblemouth "{w=0.5}.{w=0.5}.{w=0.5}."
melody @talking2mouth "Whatever. What is it?"

oak @talking2mouth "Thursday's test will be extremely difficult. I recommend you pay attention to the lectures I give."

melody @talking2mouth "I had {i}Rowan's{/i} class last year. I think I'll be fine."

hide melody with dis

pause 0.5

oak closedbrow frownmouth sweat "Hrm..."

narrator "Sam seems conflicted. He furrows his brow and rubs his forehead."

menu:
    "{color=#b7669e}[[Charm]{/color} >Reach out to Sam":
        $ TraitChange("Charm")

        red @talkingmouth "Hey, Sam."

    "{color=#e226a6}[[Patience]{/color} >Wait for Sam to calm down":        
        $ TraitChange("Patience")

        narrator "After a couple moments, Sam's brow unfurrows, and he lets out a mighty sigh. "

oak -closedbrow -sweat @talking2mouth "Lad."
oak @closedbrow talking2mouth "I don't believe I've had an opportunity to apologize, yet, for... my teaching methods thus far."

red @sadbrow talkingmouth "You don't need to. You're new to this. I mean, it worked for me. You got me to memorize {i}every single Pokémon{/i}'s data, you know?"
red @happy "No way we could have known how much went into teaching."

oak @talking2mouth "I believe I should have, though. I thought simply having the knowledge, then sharing it, would be enough. But... it seems that I don't even necessarily have the knowledge I thought I did."
oak @talking2mouth "Immensely frustrating. And now there's this 'human' element, with a new, troubled, student..."

red @sadbrow talkingmouth "It was pretty bad timing."

oak @closedbrow talking2mouth "I didn't create the digital Pokédex on my first try, nor on my thirtieth. Persistence is all that's required of me now."
oak @happy sweat "Still, it's rather demoralizing to realize that a field I thought I'd mastered, I had really no proficiency in at all!"
oak @sadbrow talking2mouth "I used to scoff at Doctor Katsura's insistence he study the science of teaching before he became a teacher. I imagined a man of his intellect was far past the need to do such things."
oak @closedbrow sweat talking2mouth "...Foolish of me, in hindsight."

red @talkingmouth "Well, we're in a school. There's never a better place to learn new things."

oak sad2eyes sadeyebrows talking2mouth "True... but I'd rather it's not at your expense."

hide oak with dis

pause 0.5

redmind @thinking "...Sam..."

pause 1.0

redmind @closedbrow frownmouth "Well, there's nothing I can do about it now."

if (not HasEvent("Klara", "AcceptCoordinatorClub")):
    scene blank2 with splitfade

    $ removestudents = { "May", "Brendan", "Klara", "Jasmine", "Yellow", "Misty", "Serena", "Dawn", "Tia", "Calem", "Grusha", "Gardenia" }

    if (HasEvent("Klara", "BreakHeart")):
        red @closedbrow talking2mouth "Since I'm not going to the Coordinator Club meeting, I can enjoy my free time for a while..."

    else:
        red @closedbrow talking2mouth "Since I'm not going to the Coordinator Club meeting, I can enjoy my free time until it's time to meet up with Klara..."

    call freeroam from _call_freeroam_31

    $ removestudents = set()

    if (HasEvent("Klara", "BreakHeart")):
        call texting from _call_texting_26

        jump day010526

    else:
        scene blank2 with splitfade

        redmind @thinking "Hm... it's pretty late, right? Where did Klara say we were going to meet? Outside Relic Hall, right?"

        pause 0.5

        narrator "You go back to your dorm, where everything is still weirdly still and quiet. Thankfully, since the common area is empty, you're able to sneak back out with much trouble, and make your way to the front of Relic Hall."

        call Klara1 from _call_Klara1_1

        jump day010526

red @talking2mouth "I should go meet up with Klara, right? Where does the Coordinator Club normally meet up?"

show may uniform with dis

may @talkingmouth "Oh, you're going to watch a Coordinator Club meeting?"

red @surprised "Oh! I... didn't realize I said that out loud. But yeah, that's the plan."

$ AddEvent("Professor Oak", "LearnedAboutContestColiseum")

may @happy "That's so great! It's about time we Coordinators get the chance to show you Battle Team guys what we can do in {i}our{/i} arena."
may @talkingmouth "We have our meetings in the [bluecolor]Contest Coliseum.{/color} I'm going there now, if you'd like to come with me?"

red @talking2mouth "Sure. Let me just go get changed."

may @happy "Of course! Brendan and I will meet you outside Relic Hall, since both our dorms are there."

red @talkingmouth "You got it."

call clearscreens() from _call_clearscreens_215
scene blank2 with splitfade 

narrator "You go back to your dorm, and explain to Leaf and Ethan where you're going."

leaf @surprised "Contests? Yeah, sure. Have fun, I guess..."

ethan @unamusedbrow talking2mouth "Could you sound {i}less{/i} enthusiastic?"

leaf @angrybrow talking2mouth "There's like two things you can do with Pokémon, and that's the less interesting one! Get off my back!"

narrator "Ethan seems to be in a grumpy mood, and you're privately thankful for the excuse to step out."

scene blank2 with splitfade 

pause 0.5

scene relichall_A with splitfade

redmind @confusedeyebrows frownmouth "Hm... Where are they?"

$ showredonly = True

may @talkingmouth "Hey! Sorry we were late--we couldn't find my scrunchie."

pause 0.2

$ showredonly = False

red @talkingmouth "Completely fine! I wasn't here long. I just--"

show brendan contest:
    xpos 1.2
    ease 0.5 xpos 0.75

show may contest:
    xpos -0.2
    ease 0.5 xpos 0.25

red @surprisedbrow frownmouth lightblush "{w=0.5}.{w=0.5}.{w=0.5}."

brendan @happy "Hey, you ready to go, bro?"

may @surprised "[first_name]? Are you alright? Your face is all flushed...?"

menu:
    "You guys look amazing!":
        $ AddEvent("Brendan", "ComplimentContestOutfit")
        $ AddEvent("May", "ComplimentContestOutfit")
        $ ValueChange("May", 1, 0.25, False)
        $ ValueChange("Brendan", 1, 0.75)
        
        brendan @happy "Hey! Thanks, bro! You too. From one brother who puts in the work to look good to another; respect."

        may @happy "Thanks, [first_name]. Do you like my contest outfit? Brendan sewed it for me himself!"

        brendan @happy sweat "I mean, I just used a pattern. I didn't create the design. May's dress is based on something Lisia wore earlier in her career. But I guess it's pretty good."
        brendan @talkingmouth "Don't require repairs all the time. Most contest outfits are built to be light, so they fall apart pretty often."
        brendan @closedbrow talking2mouth "I try to make outfits that bring out the best in the wearer, {i}and{/i} don't require bucketloads of cash to keep runnin'."

        may @sadbrow talkingmouth "You're so practical, sweetheart."

    "Brendan, you're seriously hot.":
        $ AddEvent("Brendan", "ComplimentContestOutfit")
        $ ValueChange("Brendan", 1, 0.75)

        brendan @happy "Hey! Thanks, bro! You too. From one brother who puts in the work to look good to another; respect."

        may @talkingmouth "Do you like our outfits? Brendan sewed them himself!"

        brendan @happy sweat "I mean, I just used a pattern. I didn't create the designs--this one's based on the outfit of a Kanto Rock Star called Ryuki. But I guess they're pretty good."
        brendan @talkingmouth "Don't require repairs all the time. Most contest outfits are built to be light, so they fall apart pretty often."
        brendan @closedbrow talking2mouth "I try to make outfits that bring out the best in the wearer, {i}and{/i} don't require bucketloads of cash to keep runnin'."

        may @sadbrow talkingmouth "You're so practical, sweetheart."

    "May, you're absolutely adorable.":
        $ AddEvent("May", "ComplimentContestOutfit")
        $ ValueChange("May", 1, 0.25)

        may @happy "Awww! Thanks, [first_name]. Do you like my contest outfit? Brendan sewed it for me himself!"

        brendan @happy sweat "I mean, I just used a pattern. I didn't create the design. May's dress is based on something Lisia wore earlier in her career. But I guess it's pretty good."
        brendan @talkingmouth "Don't require repairs all the time. Most contest outfits are built to be light, so they fall apart pretty often."
        brendan @closedbrow talking2mouth "I try to make outfits that bring out the best in the wearer, {i}and{/i} don't require bucketloads of cash to keep runnin'."

        may @sadbrow talkingmouth "You're so practical, sweetheart."

    ">Just continue sweating in silence":
        brendan @closedbrow talkingmouth "I think I've got a fresh water somewhere here... hold up."

        show brendan contest:
            xpos 0.75 ypos 1.0 zoom 1.0
            ease 0.5 xpos 0.66 ypos 1.2 zoom 1.3

        show may contest:
            xpos 0.25 ypos 1.0 zoom 1.0
            ease 0.5 xpos 0.33 ypos 1.2 zoom 1.3

        brendan @sadbrow talking2mouth "Don't go passin' out on us, bro. You got to stay hydrated when you're running in May. It's seriously hot out here."

        redmind @mediumblush frownmouth surprisedbrow "You're telling me."

        narrator "The two extremely attractive coordinators look at you with earnest concern. You attempt to hitch an unflustered grin onto your face. May and Brendan exchange a curious look."

        show brendan contest:
            xpos 0.66 ypos 1.2 zoom 1.3
            ease 0.5 xpos 0.75 ypos 1.0 zoom 1.0

        show may contest:
            xpos 0.33 ypos 1.2 zoom 1.3
            ease 0.5 xpos 0.25 ypos 1.0 zoom 1.0

brendan @talking2mouth "We're running a bit late, though, and Liz'll tear our heads off if we're not there and in-position in time..."

may @closedbrow talking2mouth "I swear, the only one who can keep up with her is Dawn."

brendan @talking2mouth "Well, Liz did specially recruit her. Dawn's the entire reason we've even got Liz."
brendan @talkingmouth "Well, Dawn and Calem, anyway."

may @closedbrow talking2mouth "And we're... {i}so{/i} grateful."

brendan @talking2mouth "I get that, but what Liz said about needing to try harder to be taken seriously than battlers is real true. I see where she's coming from, honestly."

may @talking2mouth "Yeah. She's not {i}wrong.{/i} Just... intense."

brendan @talking2mouth "Anyway, that's why we gotta hurry to the Contest Coliseum! C'mon!"

red @sad2eyes lightblush talkingmouth "Y-yeah. Sure thing. Just one question."

show brendan surprisedbrow frownmouth
show may surprisedbrow frownmouth
with dis

red @confused "Where is it?"

pause 1.0

brendan @talking2mouth "What?"

may @talking2mouth "[first_name], it's right behind the Battle Hall."

red @talking2mouth "That's not on my map."

may @closedbrow talking2mouth "[first_name], can I see that map?"

red @talking2mouth "Sure."

show mapdemo with dis

pause 0.5

show may -surprisedbrow -frownmouth:
    rotate 0 xpos 0.25
    ease 1.0 rotate -50

show brendan -surprisedbrow -frownmouth:
    rotate 0 xpos 0.75
    ease 1.0 rotate 50

pause 2.0

may @talkingmouth "Okay... you're right. It's {i}not{/i} on there. But, um..."

narrator "Brendan points at a big silver building that is, as the Hoennians said, behind the Battle Hall."

brendan @talking2mouth "It's there, bro."

pause 0.5

red @closedbrow sweat talking2mouth "I thought... that was part of the city."

may @talkingmouth "A little bit! But the campus extends into the city for a few blocks. That map you have is pretty zoomed-in."

red @unamusedbrow talking2mouth "...I've been here two months, and I'm just now learning this?"
red @closedbrow talking2mouth "Jeez. {i}Please{/i} don't tell Leaf. I'd never hear the end of it."

stop music fadeout 1.5

$ PlaySound("idea.ogg")

brendan @talking2mouth "Hm?"

show may surprisedbrow frownmouth with dis

brendan surprisedbrow frownmouth @surprised "Oh, crap, we gotta go! Like, triple-time!"
brendan surprisedbrow frownmouth @surprised "Run, babe! Run, bro!"

queue music "Audio/Music/Show Me Around.ogg"

scene blank2 with splitfadefaster

pause 0.5

scene colosseum with splitfadefaster

show brendan contest surprised: 
    xpos 1.3
    ease 0.6 xpos -0.2

show may contest surprised: 
    xpos 1.2
    ease 0.6 xpos -0.2

narrator "Brendan and May lead you to a familiar location, first... the outside of the Battle Hall..."

scene concerthall with splitfadefaster

show brendan contest surprised: 
    xpos 1.3
    ease 0.6 xpos -0.2

show may contest sadbrow frownmouth: 
    xpos 1.2
    ease 0.8 xpos -0.2 

narrator "Then to a new location, the outside of a shining silver building that you must assume is the Contest Coliseum..."

scene concerthallback with splitfadefaster

show brendan contest surprised: 
    xpos 1.3
    ease 0.4 xpos -0.2

show may contest sad: 
    xpos 1.2
    ease 1.0 xpos -0.2 

narrator "Before pulling a sharp turn around the back of the building."

brendan @talkingmouth "Through the back! It leads directly to the practice room, and Liz might not see us come in this way!"

scene concerthallhallway with splitfadefaster

red @surprised "Directly? You didn't mention the hallway!"

brendan contest @surprised "It's just at the end of this! We're almost there! We're--"

stop music fadeout 3.0

scene blank with transeye2

pause 2.0

show concerthallpracticeroom
show serena contest surprisedbrow frownmouth:
    xpos 1.0/8.0
show misty contest surprised:
    xpos 2.0/8.0 xzoom -1
show klara neutralcoat surprisedbrow frownmouth behind misty:
    xpos 3.0/8.0 xzoom -1
show lisia incognito angrybrow frownmouth:
    xpos 4.0/8.0
show dawn contest surprisedbrow frownmouth behind dawn:
    xpos 5.0/8.0
show tia contest surprisedbrow frownmouth:
    xpos 6.0/8.0
show jasmine contest surprisedbrow frownmouth behind tia:
    xpos 7.0/8.0
    
pause 3.0

brendan contest @sadbrow talkingmouth "We're... too late."

queue music "audio/music/littleroot_start.ogg" fadein 1.5 noloop
queue music "audio/music/littleroot_loop.ogg"

show screen currentdate with dis

if (GetRelationshipRank("Tia") > 0):
    $ ValueChange("Tia", 1, 6.0/8.0)
    tia -surprisedbrow -frownmouth @happy "Hi, [first_name]!"

else:
    tia -surprisedbrow -frownmouth @happy "Hi, [tiafont][first_name]{/font}!"

if (GetRelationshipRank("Jasmine") > 0):
    jasmine @talking2mouth "You're here...? I didn't know you were going to watch one of our practices, [first_name]!"
    
    $ ValueChange("Jasmine", 1, 7.0/8.0)

    jasmine -surprisedbrow -frownmouth @happy "How lovely."

if (GetRelationshipRank("Misty") > 0):
    misty @talkingmouth "[first_name]? What are you doing here? This is the Contest Club. Did you get lost on the way to the Battle Hall?"

    $ ValueChange("Misty", 1, 2.0/8.0)

    misty -surprisedbrow -frownmouth -surprised @sadbrow talking2mouth "Uh... I mean, I don't {i}hate{/i} that you're here..."

if (GetRelationshipRank("Dawn") > 0):
    dawn @happy "Oh, I'm so glad you're here, [first_name]! I thought about inviting you for a while, now, but..."

    $ ValueChange("Dawn", 1, 5.0/8.0)

    dawn -surprisedbrow -frownmouth @sadbrow talkingmouth "Well, I was worried you'd find it boring, I guess..."

if (GetRelationshipRank("Serena") > 0):
    $ ValueChange("Serena", 1, 1.0/8.0)

    serena -surprisedbrow -frownmouth @happy "So it seems you have an interest in contests, too? Aren't {i}you{/i} the renaissance man. A versatile mind is an attractive quality on its own merits."

klara -surprisedbrow -frownmouth @happy "Oh, you actually came! I'm sooo glad!~ I hope you keep your eyes on me!~"
    
$ ValueChange("Klara", 10, 3.0/8.0)

lisia @talking2mouth "...[first_name], right?"

red @talking2mouth "That's me."

lisia @closedbrow talking2mouth "Why do I know you...?"

red @happy sweat "Uh, I beat Dawn in the Quarter Qlashes..."

lisia @surprised "Oh, that's right!"
lisia -angrybrow frownmouth @happy "Right, and there's that Pikachu. I remember now."

pause 1.0

lisia @talking2mouth "Well, thank you for bringing my clubmembers here. I'm afraid I'm going to have to ask you to step out of the practice room for now, though."
lisia @talkingmouth "We're just about to discuss strategies for the Millennium Drop Water Festival Contest, and we don't want to let any secrets spill out."

red @talking2mouth "Totally fine."

serena -surprisedbrow -frownmouth @talkingmouth "If you would like to watch our practice performance, you can head out to the open-air stage. It's directly down the hallway."
serena @talkingmouth "Grusha and Calem are there, I believe. To cheer on Jasmine and I."

red @sadbrow talkingmouth "Sounds like a plan. Sorry for interrupting, everyone."

brendan @sadbrow talkingmouth "Totally fine, bro. Thanks for running with us."

may contest @happy "We'll see you in a bit! And remember, it's a straight line down the hallway!"

red @happy "I don't think I'm going to get lost just going down the--{nw}"

scene concerthallmakeuproom2

red @unamusedbrow unamusedmouth "I don't think I'm going to get lost just going down the--{fast}and I'm lost." 
red @closedbrow talking2mouth "I swear, the {i}exact{/i} moment I step off the map Leaf gave me..."

$ PlaySound("Pokemon/pikachu_sad.ogg")
libpikachu sad "Piiiika."

red @talking2mouth "Okay. I just need to retrace my steps, right? Let's just..."

stop music fadeout 1.5

queue music "audio/music/potown_start.ogg" noloop
queue music "audio/music/potown_loop.ogg"

narrator "You turn around to grab the door handle, and leave this 'ready room' you found yourself in, when, strangely..."

show concerthallmakeuproom2midnight

pause 0.1

hide concerthallmakeuproom2midnight

pause 0.5

red @closedbrow talking2mouth "Huh? Did... did the lights just flicker?"

$ PlaySound("Pokemon/pikachu_scared.ogg")
libpikachu surprisedbrow frownmouth @surprised "Pika?!"

red @confused "Yeah, let's... get out of here, bud."

pause 1.0

Character("Doorknob") "*{i}Clunk.{/i}*"

red @surprised "Wait, what? Why isn't the door opening?! What's happening? Is it--!"

narrator "Before you have the time to panic {i}too{/i} much, you twist the doorknob the other direction, and the door easily opens."

red @sad2eyes lightblush talking2mouth "...No-one saw that. You're cool. You're still cool."

narrator "You leave the room."

show concerthallmakeuproom2:
    matrixcolor SaturationMatrix(1.0)
    linear 6.0 matrixcolor SaturationMatrix(0.2)

show flashback 
hide screen currentdate
with Dissolve(6.0)

Character("???") "\"{glitch=40.00}Zzt?{/glitch}{w=0.5} {glitch=30.00}Zzzt?{/glitch}{w=0.5} {glitch=20.00}is there anyoneanyoneanyoneanyone{/glitch}{w=0.5} {glitch=10.00}there-here-ere-re-e---?{w=0.5}{/glitch}\""
Character("???") "\"{glitch=5.00}Is there anyone there...?{/glitch}\""

pause 1.0

Character("???") "\"{glitch=60.00}WHY NOT?{/glitch}\""

scene blank2 with splitfade

pause 1.0

scene concerthallhallway with splitfade

stop music fadeout 1.5
queue music "audio/music/littleroot_start.ogg" fadein 1.5 noloop
queue music "audio/music/littleroot_loop.ogg"

red @talkingmouth "Oh, phew! Here we are. Found our way back to the hallway. Should just be at the end of this, May said, right? Let's go."

scene concerthallstage with splitfade 

red @confusedeyebrows talking2mouth "...Hm?"

show may contest happy:
    xpos 1.0/10.0
show brendan contest angrybrow happymouth behind may:#god i wish that was me
    xpos 2.0/10.0 xzoom -1
show serena contest:
    xpos 3.0/10.0
show misty contest closedbrow behind serena:
    xpos 4.0/10.0 xzoom -1
show lisia:
    xpos 5.0/10.0
show dawn contest happy behind lisia:
    xpos 6.0/10.0
show tia contest frownmouth angrybrow:
    xpos 7.0/10.0
show klara neutralcoat hairpin makeup behind tia:
    xpos 8.0/10.0
show jasmine contest winkbrow talkingmouth:
    xpos 9.0/10.0
with dis

red @talkingmouth "It looks like the coordinators are here already...?"

hide may
hide brendan
hide serena
hide misty
hide lisia
hide dawn
hide tia
hide klara
hide jasmine
with dis

pause 0.5

show calem with dis:
    xpos 0.5

calem surprisedbrow @neutralbrow talkingmouth "Yes, they arrived onstage about half an hour ago."

red @surprised "What! No way! I left the practice room before them, like... five minutes ago!"

calem @talkingmouth "Oh? Well, I'm not sure what laws of logic would allow that to be a possibility."

red @sad2eyes sadeyebrows talking2mouth "I mean... yeah, obviously, it's impossible, but..."

calem -surprisedbrow @talking2mouth "In any case, Serena informed me that you were coming here when the coordinators arrived. We supposed that you had some urgent business that dragged you away."

red @sadbrow talkingmouth "No. I just... got turned around, and ended up in a ready room, but... I swear it wasn't for more than a couple minutes."

calem @closedbrow talkingmouth "I fully believe you. Perhaps it's just my own perception of time that's flawed."

narrator "Calem quickly checks his phone's clock. Whatever he saw did not seem to impress him, and he puts his phone back in his pocket."

calem @talking2mouth "Well, whatever the case, it's not worth thinking of. Look, Grusha's coming back."

show grusha:
    xpos 1.2
    ease 0.5 xpos 0.66

show calem:
    xpos 0.5
    ease 0.5 xpos 0.33

grusha @talkingmouth "Oh. You showed up."
grusha @closedbrow talkingmouth "Thought you'd skipped out."

narrator "In Grusha's hands, he holds a couple of slushies."

grusha @talkingmouth "Sorry, [first_name]. Only got two. Didn't know you'd be here."

red @sadbrow talkingmouth "Nah, it's fine. My stomach feels weird, anyway. Not sure I {i}could{/i} drink right now."

calem @talking2mouth "...Hm? Grusha, where did you get those? Is someone running a store here?"

grusha @talkingmouth "Only who you'd expect."

calem @surprisedbrow talking2mouth "Er... I'm not sure..."

grusha @closedbrow talking2mouth "'Business'."

show grusha playfulbrow:
    xpos 0.66
    ease 0.3 xpos 0.75
show calem surprisedbrow:
    xpos 0.33 xzoom 1
    ease 0.3 xpos 0.5 xzoom -1
show gardenia behind calem:
    xpos 1.2 ypos 1.0
    parallel:
        easein 0.3 ypos 0.7
        easeout 0.3 ypos 1.0
    parallel:
        ease 0.3 xpos 0.25
    parallel:
        pause 0.3
        ease 0.5 xzoom -1
with dis

gardenia @angrybrow talking2mouth "Did someone say 'business'?!"

calem -surprisedbrow -frownmouth @surprised "That's uncanny."

grusha -playfulbrow @playfulbrow talking2mouth "I've tried that four times ever since the election. Works every time."

gardenia surprised @surprisedbrow talkingmouth "Uh... I guess no-one did?"

red @talkingmouth "Seriously, how do you do that? You're like a ghost. You just phase into reality when there's a chance to make a buck."

gardenia @happy "Hah! No! No, definitely not a ghost. But I appreciate the compliment."
gardenia -surprisedbrow -frownmouth -surprised @angrybrow happymouth "The only invisible hand {i}I'm{/i} about is the free market's."

pause 0.5

show grusha confusedeyebrows
show calem surprisedbrow 
show gardenia surprisedbrow frownmouth
with dis

red @closedbrow talking2mouth "Well, I'm glad {i}you're{/i} mortal. Pretty sure I just ran into a ghost. Or I'm going crazy."

pause 0.5

grusha -confusedeyebrows @closedbrow talking2mouth "Got a family history of psychosis?"

red @talkingmouth "My grandpa thought we were still at war with Unova."

grusha @sad2eyes talking2mouth "Not a good sign."

show calem -surprisedbrow with dis

gardenia -surprisedbrow @talkingmouth "Wait. What do you mean you're pretty sure you ran into a ghost?"

red @sadbrow talkingmouth "Oh, nothing, really. I'm just joking. I got lost, and found this empty ready room." 
red @sadbrow talking2mouth "The lights flickered, and I couldn't figure out how the doorknob worked. It only took a couple minutes, but somehow I ended up staying there for, like, half an hour."

gardenia angrybrow frownmouth @talkingmouth "...In {i}this{/i} building?"

red @talkingmouth "Y-yeah...? Just in the hallway out that door."

redmind @thinking "She seems {i}really{/i} serious about this..."

gardenia @talkingmouth "Alright. Well, if no-one's in the mood to buy the lint in my pockets right now, I've got another business engagement to handle."
gardenia @happy "Seeya! Stay thrifty!"

hide gardenia with dis

narrator "As Gardenia walks away, she pulls out her phone. You don't hear what she says into it, but you can make out one word..."
narrator "'Commission.'"

redmind @confusedeyebrows frownmouth "Hm...? Is she making something for someone?"

calem @talkingmouth "...How bizarre."

grusha @talkingmouth "Sinnohans. Think they see spirits, gods, fairies, whatever, around every corner."

calem @talking2mouth "That's just a stereotype. Instructor Winona's a devout Arceist, and she's not Sinnohan."

grusha @talkingmouth "Eh. Instructor Winona {i}needs{/i} to believe the universe has some sort of plan to not have a nervous breakdown every ten minutes."

pause 1.0

narrator "The conversation trails off as Grusha, Calem, and you all turn your attention to the stage, where the coordinators are performing rigorous drills of segments of their performances."

pause 2.0

show yellow neutrallowponytail with dis:
    xpos 0.25 xzoom -1

yellow @talkingmouth "...Hi, [first_name]."

red @happy "Oh, hey, Yell'! Couldn't find something to do again?"

yellow @talkingmouth "Guess not."

calem @talkingmouth "Please, take a seat with us."

yellow @happy "Thanks."

pause 1.0

calem @talkingmouth "I must confess... I said I'd come out here to support Serena, but I'm not quite certain what we're watching."

grusha @talkingmouth "Same. I don't think Paldea even has a contest league. I've seen Johtonian contests before--Jasmine's done those, and I came to watch them, then..."
grusha @confusedeyebrows talking2mouth "But Kobukanian contests are different, aren't they?"

yellow @talking2mouth "Yes. In Kobukan, instead of having five different contest tracks, there's only one kind of contest. Whether you try to appeal through showing off the toughness of your Pokémon, or their beauty, or their coolness..."
yellow @talkingmouth "That's up to you. You don't even need to stick to doing a specific kind of appeal throughout the entire contest."

calem @talking2mouth "Interesting... that's not how it works in other regions, is it?"

grusha @closedbrow talking2mouth "Nope. Kobukan likes to be contrarian like that."

hide grusha
hide calem
hide yellow
with dis

pause 1.0

show may contest happy: 
    xpos 1.2 xzoom 1
    pause 2.0
    parallel:
        linear 3.0 xpos -0.2
    parallel:
        ease 0.5 xzoom -1
        ease 0.5 xzoom 1
        repeat

show brendan contest closedbrow talkingmouth with dis:
    xpos 0.33 xzoom -1

show misty contest happy with dis:
    xpos 0.66

narrator "You gaze at the stage, trying to make out the performers. You can't hear anything that's being said, though it looks like a few of them are singing."

redmind @thinking "Guess they didn't hook their mics up...?"

calem @talkingmouth "...Pardon my ignorance, but they all seem to be performing simultaneously. Are these team-based contests, then?"

yellow neutrallowponytail @closedbrow talkingmouth "Um... no."

show jasmine contest angrybrow talkingmouth:
    xpos 1.2
    ease 0.5 xpos 0.85

show klara neutralcoat hairpin makeup ojoubrow talkingmouth:
    xpos -0.2 xzoom -1
    ease 0.5 xpos 0.15 

hide may
show may contest happy: 
    xpos -0.2 xzoom 1
    pause 2.0
    parallel:
        linear 3.0 xpos 1.2
    parallel:
        ease 0.5 xzoom -1
        ease 0.5 xzoom 1
        repeat
        
yellow @talkingmouth "Five performers all perform simultaneously in Kobukanian contests. They all fight for the judges' attention."

show tia contest happy with gaussdis:
    zoom 0.0
    parallel:
        linear 0.2 xzoom -1
        linear 0.2 xzoom 1
        repeat 10
    parallel:
        ease 1.0 zoom 1.0

yellow @happy "But... it's not really fighting. Because you can get points for making your rivals' appeals look better."

calem @talking2mouth "Fascinating. What a wonderful spirit of cooperation."

grusha @shadow sweat surprised "Are we not going to acknowledge that Venetia just appeared out of thin air?!"

calem @talkingmouth "It's amazing what they can do with special effects nowawdays, isn't it?"

narrator "You and Yellow share a look."

redmind @thinking "There really is such a thing as being {i}too{/i} unflappable..."

show brendan happy with dis:
    xpos 0.33
    ease 0.5 xpos 1.2

show misty angrybrow happymouth with dis:
    xpos 0.66
    pause 0.5
    ease 0.5 xpos -0.2

show klara happy with dis:
    xpos 0.15
    pause 1.0
    ease 0.5 xpos 1.2

show jasmine happy with dis:
    xpos 0.85
    pause 1.5
    ease 0.5 xpos -0.2

show tia:
    pause 2.0
    ease 1.0 ypos -0.7

yellow @surprised blush "U-u-um, anyway, I... yes, so, they all perform at the same time."
yellow @closedbrow talkingmouth "In this region, the performances of the trainers are considered just as important as those of the Pokémon..."
yellow @talkingmouth "So every appeal has two parts to it. The performer's performance, and the Pokémon's move."

calem @talkingmouth "Curious. Seems there's a sort of science to this. It appears the human performers' appeals fall into three different categories..."

grusha @talkingmouth "Hm. Audio's one of them. Singing and playing instruments."

calem @talkingmouth "Physical appeals are important, too. Dancing and acrobatics. Perhaps even feats of strength could be considered."

yellow @talkingmouth "The third kind of appeals are 'prop-based appeals'. Or just 'Props'. These appeals use external factors, like... um, juggling, pyrotechnics, or magic tricks."

calem @talkingmouth "Ah. Like those hidden wires that just allowed Tia to fly."

yellow @scaredeyes "{w=0.5}.{w=0.5}.{w=0.5}."
yellow @talkingmouth scaredeyes "Yes.{w=0.5} That is correct."

hide may
hide serena
hide jasmine

show may contest happy: 
    xpos -0.2 xzoom 1
    pause 2.0
    parallel:
        linear 3.0 xpos 1.2
    parallel:
        ease 0.5 xzoom -1
        ease 0.5 xzoom 1
        repeat

show serena contest closedbrow talkingmouth:
    xpos 0.33
show jasmine contest closedbrow sweat talking2mouth:
    xpos 0.66
with dis

grusha @talkingmouth "...So who's judging this thing?"

yellow @talkingmouth "Oh, Kobukanian contests have three judges. I think Instructrice Fantina will be one of the judges for the Millennium Drop."
yellow @happy "It's pretty useful to know who the judges are ahead of time, so you can tailor your performance to them."

calem @talkingmouth "Sensible. They'll be wanting to see specific kinds of appeals, won't they? Techniques that demonstrate your Pokémon's toughness might not go over well for a judge who's in the mood to see a cute Pokémon display."

grusha @sad2eyes talking2mouth "...I've been there before. When I still boarded, there'd be some judges you knew weren't in a good mood. Nothing you did would squeeze a point out of them."
grusha @closedbrow talking2mouth "That's why you needed to keep an eye on which judges seemed most excited. If you managed to push a judge over the edge, they'd award you a ton of points."
grusha @sad2eyes sadeyebrows "Of course, after they were satisfied, they'd want to see something else, so you couldn't rely on the same trick forever."

calem @sad "Probably for the best. A contest where one performant does the same thing over and over sounds rather dull."

grusha @closedbrow talking2mouth "I could have lived with it."

yellow @talkingmouth "It sounds like it's the same for Pokémon contests as it is in snowboarding, then." 
yellow @talking2mouth "Once a judge awards a jackpot, they usually start looking for something else... though they become easier to get excited, since they've been 'warmed up.'"

red @talkingmouth "You know a {i}ton{/i} about these contests, Yellow! Are you sure you don't have any interest?"

yellow @blush closedbrow talkingmouth "I couldn't do it." 
yellow @surprisedbrow talkingmouth "I mean, even if I was interested."
yellow @blush sadbrow talking2mouth "The coordinators... everyone up on stage... they're so brave. And beautiful."

pause 1.0

grusha @confusedeyebrows talking2mouth "?"
calem @angrybrow talking2mouth "."
red @angrybrow talking2mouth "!"

narrator "A moment passes, as Grusha, Calem, and you all lock eyes and communicate in the universal man-language of eyebrow waggles."
narrator "You nod, and come to a silent agreement."

hide serena
hide jasmine

show calem talkingmouth:
    xpos 0.25
show grusha happybrow:
    xpos 0.75
show yellow neutrallowponytail blush surprised
show red happy at Transform(xpos=0.08, yanchor=0.35)
with vpunch

Character("The Boys") "\"You're beautiful, too, Yellow.\""

show calem smilemouth
show grusha -happybrow
hide red with dis
with dis

pause 1.0

yellow @heavyblush sad2eyes talking2mouth "Th-thanks... but... please don't say that..."

calem @closedbrow talking2mouth "Of course."

grusha @closedbrow talking2mouth "{i}Como desees.{/i}"

red @sadbrow talkingmouth "We meant it, though."

show yellow:
    parallel:
        ease 0.5 xpos 0.52
        ease 1.0 xpos 0.48
        ease 0.5 xpos 0.5
        repeat 3
    parallel:
        ease 6.0 ypos 1.3

show calem happy
show grusha happy 
with dis

yellow cryingeyes talkingmouth "{size=30}Dooooooon't...{/size}"

scene blank2 with splitfade

narrator "Yellow, you, and the boys watch the contests with passive interest."
narrator "You start to notice little oddities, though..."

pause 0.5

narrator "Perhaps two singers are singing at slightly different rhythms."
narrator "May's dance steps are not perfectly coordinated, and she stumbles once or twice."
narrator "After a while, Jasmine has to excuse herself from the stage, and sits down in the front row as she recovers her breath."
narrator "And... Klara's sportswear clashes somewhat with the other coordinators' formal outfits, even with the addition of her mink coat."
narrator "Meanwhile, Tia seems to be entirely unaware of the other performers, dancing to a tune only she can hear."
narrator "Lisia dashes between the performers, providing advice, straightening outfits, providing guiding notes for their vocal performances..."
narrator "But she's clearly sweating."

pause 1.0

narrator "Only Dawn has a performance you could call 'flawless,' but you can't help but feel that her performance is lacking in some originality."
narrator "Of course, you don't recall ever seeing a Pokémon contest of {i}any{/i} nature before, so you're not sure where this impression is coming from."

pause 1.0

scene concerthallstage
show calem:
    xpos 0.25
show grusha:
    xpos 0.75
show yellow neutrallowponytail
with dis

pause 1.0

calem @talkingmouth "Hm."

pause 0.5

yellow @sadbrow talkingmouth "Ooh, that looked like it hurt. Should I...? Oh, no, she's okay."

pause 0.5

grusha @closedbrow talkingmouth "I'm just going to say it."
grusha @sad2eyes sadeyebrows "I mean, we're all thinking it."
grusha @closedbrow talking2mouth "They're trying very hard, and we should be proud of them."

calem @surprised "Oh?"

grusha @talkingmouth "What, did you think I was going to say something else? Have more faith."

calem @angrybrow "{w=0.5}.{w=0.5}.{w=0.5}."
calem @closedbrow talking2mouth "...I suppose Lisia has only had them for less than a month."

yellow @talkingmouth "There were a lot of coordinators who were part of the club before, who just joined as, um, hobbyists."
yellow @closedbrow talking2mouth "After you convinced Lisia to take over, most of the club dropped out. There used to be... about forty of them..."

calem @talkingmouth "And now there's less than a fourth of that number."
calem sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."
calem @talkingmouth "Did I... do something wrong by asking Lisia to teach?"

yellow @closedbrow talkingmouth "You did something you thought was right, that you thought would help people, at the time."
yellow @sadbrow talking2mouth "That's all anyone can do, really..."

grusha @closedbrow talking2mouth "{i}No te preocupes.{/i} The only reason they're worrying about making a splash at the {i}Millennium{/i} is because now there's actually a chance they might. Before Lisia? Nah."

pause 1.0

red @happy "Making a splash?"

grusha @talkingmouth "I do more than ice puns."

red @talkingmouth "Anyway, what Yellow and Grusha say is right. You helped the coordinators--the ones who wanted to work for it--out."
red @closedbrow sweat talking2mouth "I guess you might've upset a few hobbyists, but..."

narrator "You gesture vaguely at the large building you're in."

red @talking2mouth "It seems like a bit of a waste for the school to have spent {i}this much{/i} money on a club that doesn't get stuff done."

calem @closedbrow talkingmouth "I suppose there's some truth amongst your points. Thank you for your support, you two."

red @talking2mouth "Anytime."

pause 1.0

yellow frownmouth @angrybrow talkingmouth "Looks like they're wrapping up. It's getting kinda late, so we should probably head back to the dorm, [first_name]..."

red @talking2mouth "You don't look excited."

pause 1.0

red @confused "Come to think of it, Ethan was in a bad mood earlier as well. Did something happen between you two?"

yellow @sad2eyes talkingmouth "Not between us..."

pause 0.5

redmind @closedbrow frownmouth "Hm. Looks like Yellow's actually... 'mad.' I didn't think that was possible. I wonder what happened?"

calem @talkingmouth "Yes, let's--" 
extend @surprised "hm? Grusha, what is it?"

grusha @angrybrow talking2mouth "...What's she doing here?"

redmind @thinking "Who?"

show melody on with dis:
    xpos 0.2

show calem:
    xpos 0.25 xzoom 1
    ease 0.5 xpos 0.4 xzoom -1

show yellow:
    xpos 0.5 
    ease 0.5 xpos 0.6

show grusha:
    xpos 0.75
    ease 0.5 xpos 0.8

pause 1.0

redmind @frownmouth "Oh."

melody @talkingmouth "...Watching the coordinators. Not a crime."
melody @bubblemouth "{w=0.5}.{w=0.5}.{w=0.5}."
melody @talkingmouth "What're you doing here?"

calem @angrybrow talkingmouth "I'm here to support Serena."

grusha @talkingmouth "Keeping an eye on Jasmine."

melody @talkingmouth "Got it. Your girlfriends dragged you here."

calem @surprisedbrow talking2mouth "Hold on, now--!"

grusha @closedbrow talking2mouth "You kidding? Her and me?"

calem @talkingmouth "We're friends, nothing more. There is not even the potential for more."

grusha @confusedeyebrows talking2mouth "Can you see that working? Really? There's so many reasons that's not happening."

calem @surprised "I mean, the {i}very idea{/i} beggars the imagination, with a {i}multitude{/i} of... of... factors!"

grusha @closedbrow talking2mouth "Not happening. Ever."

melody @bubblemouth "{w=0.5}.{w=0.5}.{w=0.5}."
melody @talkingmouth "This is so effing high school."
melody @sadbrow talking2mouth "Fine. Your friends, who are girls, but not girlfriends, dragged you here."
melody @talkingmouth "What about you, Blondie?"

yellow @sadbrow talkingmouth "{size=30}...I just think they're pretty...{/size}"

melody @sadbrow talkingmouth "...This is so sad. You're literally going to make me cry."

pause 1.0

melody @talkingmouth "Right. I'm going to join the team. Be right back."

if (melody_name == None):
    $ melody_name = first_name

melody @talkingmouth "Later, [melody_name]."

red @surprised "Huh?"

hide melody with dis

pause 1.0

calem @surprisedbrow talking2mouth "...Join the team? What did she mean by that?"

redmind @thinking "And... why didn't she ask me why I'm here?"

show studentcouncil at sepia with dis
show flashback with dis

$ renpy.pause(1.0, hard=True)

show cheren upeyes talking2mouth at sepia behind flashback with dis

cheren @talkingmouth "You've grown far too comfortable being the most interesting person in every room."
cheren sad2eyes talkingmouth "You're going to have to learn to realize that occasionally people wish to interact with each other {i}without{/i} using you as a medium."

hide cheren
hide studentcouncil
hide flashback
with Dissolve(1.0)

redmind @upeyes frownmouth angryeyebrows "If you keep living in my head, I'm going to start charging you rent."

call clearscreens() from _call_clearscreens_216
scene blank2 with splitfade

narrator "Meanwhile, backstage..."

python:
    playercharacter = "Lisia"
    timeOfDay = "Night"
    oldinventory = copy.copy(inventory)
    oldpersonalstats = copy.copy(personalstats)
    oldparty = copy.copy(playerparty)
    oldpersondex = copy.copy(persondex)
    oldclassstats = copy.copy(classstats)

    inventory = {
        Item.WallaceBrandPokemakeupKit : 1,
        Item.InstantCoffee : 1,
        Item.BrownWig : 1,
        Item.MegaTiara : 1,
        Item.RibbonCase : 1,
        Item.KeytoSootopolis : 1,
    }
    personalstats = {
        "Charm" : 334,
        "Knowledge" : 78,
        "Courage" : 64,
        "Wit" : 49,
        "Patience" : 22
    }
    playerparty = GetTrainerTeam("Lisia")
    persondex = copy.deepcopy(defaultpersondex)
    #battle teammates
    persondex["Lisia"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Female, "Relationship": "Self", "RelationshipRank": 0, "Events": [] }
    persondex["Grandad"] = {"Named" : True, "Value" : 125, "Contact": True, "Sex": Genders.Male, "Relationship": "Granddaughter", "RelationshipRank": 0, "Events": [] }
    persondex["Wallace"] = {"Named" : True, "Value" : 247, "Contact": True, "Sex": Genders.Male, "Relationship": "Niece", "RelationshipRank": 0, "Events": [] }
    persondex["Dawn"] = {"Named" : True, "Value" : 98, "Contact": False, "Sex": Genders.Female, "Relationship": "Mentor", "RelationshipRank": 0, "Events": [] }
    persondex["May"] = {"Named" : True, "Value" : 20, "Contact": False, "Sex": Genders.Female, "Relationship": "Mentor", "RelationshipRank": 0, "Events": [] }
    persondex["Brendan"] = {"Named" : True, "Value" : 56, "Contact": False, "Sex": Genders.Male, "Relationship": "Mentor", "RelationshipRank": 0, "Events": [] }
    persondex["Jasmine"] = {"Named" : True, "Value" : 23, "Contact": False, "Sex": Genders.Male, "Relationship": "Mentor", "RelationshipRank": 0, "Events": [] }
    persondex["Serena"] = {"Named" : True, "Value" : 47, "Contact": False, "Sex": Genders.Male, "Relationship": "Mentor", "RelationshipRank": 0, "Events": [] }
    persondex["Tia"] = {"Named" : True, "Value" : 28, "Contact": False, "Sex": Genders.Male, "Relationship": "Mentor", "RelationshipRank": 0, "Events": [] }
    persondex["Klara"] = {"Named" : True, "Value" : 12, "Contact": False, "Sex": Genders.Female, "Relationship": "Mentor", "RelationshipRank": 0, "Events": [] }
    persondex["Misty"] = {"Named" : True, "Value" : 50, "Contact": False, "Sex": Genders.Female, "Relationship": "Mentor", "RelationshipRank": 0, "Events": [] }

    classstats = { 
        "Normal" : 35,
        "Fire" : 23,
        "Water" : 42,
        "Grass" : 13,
        "Electric" : 47,
        "Ice" : 6,
        "Fighting" : 3,
        "Poison" : 2,
        "Ground" : 2,
        "Flying" : 19,
        "Psychic" : 6,
        "Bug" : 1,
        "Rock" : 1,
        "Ghost" : 24,
        "Dark" : 1,
        "Dragon" : 52,
        "Steel" : 6,
        "Fairy" : 50
    }

narrator "{color=#71BBA2}You{/color} are fretting over the rapidly-approaching [bluecolor]Millennium Drop Water Festival Contest.{/color}"

scene concerthallbackstage
show may contest closedbrow sadmouth:
    xpos 1.0/9.0
show brendan contest closedbrow frownmouth sweat behind may:
    xpos 2.0/9.0 xzoom -1
show serena contest closedbrow sadmouth:
    xpos 3.0/9.0
show misty contest closedbrow behind serena:
    xpos 4.0/9.0 xzoom -1
show dawn contest:
    xpos 5.0/9.0
show tia contest closedbrow sweat frownmouth:
    xpos 6.0/9.0
show klara winkbrow talking2mouth neutralcoat hairpin behind tia:
    xpos 7.0/9.0
show jasmine contest sweat closedbrow talking2mouth:
    xpos 8.0/9.0
show screen currentdate
with splitfade

Character("Coordinators") "\"{size=50}...Phew.{/size}\""

lisia @happy "Great work, everyone! I'm really proud of you. I can definitely see the diamonds that you'll become!"

dawn @happy "Thanks, Lisia!"

may @closedbrow talking2mouth "{size=30}...I can't feel my legs.{/size}"

brendan @sadbrow talking2mouth "{size=30}I can give you a massage when we get back to the dorm.{/size}"

may @sadbrow talkingmouth "{size=30}Thanks, sweetie...{/size}"

lisiamind @closedbrow frownmouth "...Hm. That Birch girl. Brendan takes his contests seriously, but it feels like May's just along for the ride..."
lisiamind @sadbrow frownmouth "I hope I don't have to give him a different training partner. Their rapport's fantastic, but I'm not sure they're effective at training together... too soft on each other."

misty @sadbrow talkingmouth "I think I... lost my voice. I've never sung that long. Not even at the theater..."

lisia @talking2mouth "You might want to hold off on your theater appearances in the lead-up to the [bluecolor]Millennium Drop Water Festival Contest{/color}."

misty @surprised "Huh?"

lisia @sadbrow talking2mouth "...Other people might see your performances, and come up with a performance that totally overshadows you."
lisia @talkingmouth "Since you focus a lot on audio appeals, using Pokémon moves that draw attention away from audio-based performances could really mess with you."

serena -closedbrow -frownmouth @talkingmouth "Ah... yes. You've been focusing on training your voice, haven't you, Misty?"

misty @talkingmouth "As much as I can. But projecting my voice only works so much. I'll still never be louder than a sound-based move, a move that causes a massive explosion, a move that changes the weather, or a move that uses wind in some way..."

lisia @angrybrow talking2mouth "All it takes is one guy with a vendetta against you and an Exploud to completely drown out any chance of the judges noticing you."
lisia @talkingmouth "That's why it's so important to practice routines! Simple physical moves, like biting, kicking, punching, and slicing moves are really easy and fast to execute." 
lisia @happy "Even if someone tries to throw off your performance, you can stay focused if you're just doing a simple routine like that."

jasmine -closedbrow -sweat -talking2mouth @talkingmouth "Such simple routines are not likely to be notably impressive, though, no?"

lisia @talkingmouth "No... but it's better to pull off an unimpressive technique flawlessly than to fall on your face while trying to pull off a trickier one."

show tia happy with dis

tia "[tiafont]Thanks, Liz! You're incredibly knowledgeable about contests, you know? I really admire you!{/font}"

lisia @happy "Hah hah! Same to you, Venetia!"

pause 1.0

lisiamind @sadbrow frownmouth "I still have no idea what she's saying."
lisiamind @thinking "I just don't have time to hire an interpreter for her, but I really don't see her having much success in the contest, anyway... she doesn't pay attention to the other performers at all."

Character("???") "\"Excuse me.\""

lisia @talkingmouth "Hm?"

show may surprisedbrow frownmouth:
    xpos 1.0/9.0
    ease 0.5 xpos -0.5
show brendan surprisedbrow frownmouth:
    xpos 2.0/9.0
    ease 0.5 xpos -0.5
show klara surprisedbrow frownmouth:
    xpos 7.0/9.0 xzoom 1
    ease 0.5 xzoom -1
    pause 0.2
    ease 0.3 xzoom -1
    ease 0.5 xpos -0.2
show tia -angrybrow -sweat confusedeyebrows frownmouth:
    xpos 6.0/9.0
    ease 0.5 xpos 4.0/9.0
show serena surprisedbrow frownmouth
show jasmine surprisedbrow frownmouth:
    xpos 8.0/9.0 xzoom 1
    ease 0.5 xzoom -1
    pause 0.2
    ease 0.3 xzoom 1
    ease 1.0 xpos 2.0/9.0
    ease 0.3 xzoom -1
show dawn surprisedbrow frownmouth:
    xpos 5.0/9.0
    ease 0.5 xpos 1.0/9.0
show misty angrybrow:
    xpos 4.0/9.0
    ease 0.5 xpos 5.0/9.0
with dis

may @talkingmouth "Ah! It's her!"

pause 1.0

show melody on at night:
    xpos 1.2 xzoom -1
    ease 0.5 xpos 0.9

melody @surprisedbrow bubblemouth "{w=0.5}.{w=0.5}.{w=0.5}."
melody @surprisedbrow talkingmouth "Wow. Guess I made a splash."

pause 0.5

melody @talkingmouth "Water pun."

pause 1.0

melody @talking2mouth "What, what's the deal? I don't bite."

lisiamind @closedbrow frownmouth "Hm... I've never seen this girl before, but it looks like my pupils are familiar with her... and not in a good way."
lisiamind @angrybrow frownmouth "Alright, Liz. You can get along with everybody. Build that bridge!"

lisia @happy "Hi! I'm Lisia, the Coordinator Club's advisor!~ We just finished practice, so I'm afraid the other clubmembers need to go back to their dorms now, but is there something I can help you with?"

show tia surprisedbrow frownmouth
show misty angry
show serena surprisedbrow frownmouth
show jasmine surprisedbrow frownmouth
show dawn surprisedbrow frownmouth
with dis

melody @talkingmouth "Yeah, I'd like to join."

pause 0.5

lisiamind @talkingmouth "Okay... this wasn't a part of the script I expected."

lisia @talkingmouth "O... kay. Um, I'm not sure we're accepting any new members right now."
lisia @happy "But, if you think you have a strong case, and you're not afraid to work {i}really{/i} hard at it, I'll hear you out."

melody @talkingmouth "...Okay."

melody up @talkingmouth "I've spent years mastering my singing technique. My breath control is precise, and my vibrato is consistent at 5-6 oscillations per second. I can sing from G2 to C6 with perfect pitch accuracy." 
melody @closedbrow talkingmouth "I control dynamics flawlessly, ranging from 30 to 90 decibels, and my melismatic runs can execute 15 notes per second with precise intonation." 
melody @talking2mouth "With perfect relative pitch, I can harmonize instantly, and my understanding of harmonic overtones adds measurable depth, as confirmed by spectrogram analysis." 
melody @closedbrow talking2mouth "Finally, I've participated in every contest in the Orange Archipelago, with a seventy-five percent winning rate."
melody @bubblemouth "{w=0.5}.{w=0.5}.{w=0.5}."
melody @talkingmouth "That's {i}every{/i} contest. The Tangelo Open, the Pinkan Junior Cute and Beauty Contests, the Kinnow Memorial Festival, the Pummel-Hamlin Unity Concert, the Mandarin Island Orange Archipelago Grand Open..."
melody @closedbrow talkingmouth "Et cetera."
melody on @talkingmouth "And I was the Festival Maiden for seven years running in the Shamouti Island Legend Festival. Which is a big thing in Shamouti." 

lisia @surprisedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

$ BecomeNamed("Melody")

lisia @happy "Well, that's a {i}very{/i} impressive resume, you must be Melody, then! I remember hearing about a young woman who was clearing the Orange Archipelago's contest league a couple years ago."

melody surprisedbrow @neutralbrow talkingmouth "I was also a member of the Coordinator Club during the 2003-2004 school year. I never placed anywhere but first."

misty @talkingmouth "That's a lie! I don't know about all the other stuff you said, but I know that last one's a lie!"

show tia surprisedbrow frownmouth:
    ease 0.5 xpos -0.2
show misty angry:
    ease 0.5 xpos 0.33
show serena surprisedbrow frownmouth:
    ease 0.5 xpos -0.2
show jasmine surprisedbrow frownmouth:
    ease 0.5 xpos -0.2
show dawn surprisedbrow frownmouth:
    ease 0.5 xpos -0.2
with dis

melody @bubblemouth "{w=0.5}.{w=0.5}.{w=0.5}."
melody @talkingmouth "...Why do I know you?"

misty @talkingmouth "We take classes together!"

melody -surprisedbrow @surprisedbrow talkingmouth "...Bug?"

misty @talkingmouth "I hate bugs! I'm in a Goldeen-print swimsuit {i}right now!{/i} Water, dumbass!"

lisia @angry "Language!"

melody @talkingmouth "It's fine. I get it now."
melody @angry "Red hair and a hand-me-down contest outfit? You must be Misty."

misty @talkingmouth "What is {i}that{/i} supposed to mean?!"

melody @talkingmouth "Apple doesn't fall far from its tree, I guess. You're the spitting image of your sisters."

show misty surprisedbrow frownmouth with dis

melody @talkingmouth "Although they were prettier, taller, and apparently smarter."

misty angry "You shut up!"
misty @sadbrow talkingmouth "Liz, you can't {i}seriously{/i} be thinking about bringing her into the club?"
misty @talkingmouth "She's... she's the {i}worst!{/i}"

melody @talkingmouth "Not the worst at contests."
melody @talking2mouth "Besides, I'm not the one causing problems here."

pause 0.5

melody @talkingmouth "I'm qualified. Practiced. I'll win the Millennium Drop for you, Lisia. Phobos will give you a blank check. That means a new round of outfits for everyone, on the school's dime."
melody @talking2mouth "You'd have the money to hold {i}any{/i} contest you want, right here in Kobukan. Build a new contest hall that isn't haunted to hell and back. Want to make 'World Contest Champion' mean more?" 
melody @talkingmouth surprisedbrow "Ten billion would go a long way towards that."
melody @talkingmouth "That's Tamamushi-level money."
melody @talking2mouth "I know you won't leave it on the table."

lisiamind @closedbrow frownmouth "It's true that having Phobos' support would make my dreams of expanding the influence and importance of contests {i}much{/i} easier."
lisiamind @frownmouth "And, truthfully, I think she probably {i}could{/i} win the Millennium Drop Water Festival Contest. Even now. Her resume is legendary, for such a young girl."
lisiamind @closedbrow frownmouth "But half my pupils are terrified of her, and the other half hate her."
lisiamind @closedbrow talking2mouth "She makes a good point... but is it worth the drama? Of course, coordinators thrive on drama, but is it worth {i}that much{/i}...?"

melody @talkingmouth "...Having difficulty deciding. Fine. Expected."

show melody at night:
    xzoom -1 xpos 0.9
    ease 0.5 xzoom 1

melody @bubblemouth "{w=0.5}.{w=0.5}.{w=0.5}." 
melody @talkingmouth "I respect you a lot, Lisia. So I'm not going to let you make a wrong decision."
melody @talking2mouth "If you can't decide, check your phone. You have a voicemail. Listen to it."
melody @talkingmouth "That'll make the decision for you."

pause 0.5

melody @talkingmouth "{i}Adiós.{/i}"
melody @talking2mouth "See you in Bug class, Misty."

hide melody with dis

pause 1.0

misty sad "No way... you can't really be...?"

pause 1.0

lisia @closedbrow frownmouth "...I think I need to listen to that voicemail."

call clearscreens() from _call_clearscreens_217
scene blank2 with splitfade

python:
    inventory = oldinventory
    personalstats = oldpersonalstats
    playerparty = oldparty
    persondex = oldpersondex
    classstats = oldclassstats
    playercharacter = None

narrator "Meanwhile, {color=#f00}You{/color} are back at your dorm..."

if (HasEvent("Klara", "BreakHeart")):
    call texting from _call_texting_27

    jump day010526

else:
    scene blank2 with splitfade

    redmind @thinking "Hm... it's pretty late, right? Where did Klara say we were going to meet? Outside Relic Hall, right?"

    pause 0.5

    narrator "You go back to your dorm, where everything is still weirdly still and quiet. Thankfully, since the common area is empty, you're able to sneak back out with much trouble, and make your way to the front of Relic Hall."

    call Klara1 from _call_Klara1_2

    jump day010526
