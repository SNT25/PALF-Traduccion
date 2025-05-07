label day010522:
$ timeOfDay = "Morning"

call calendar(1) from _call_calendar_47

$ calDate = calDate.replace(day=22, month=5, year=2004)

show morning at vspaz

pause 3.5

$ renpy.music.play("Audio/Morning_ambience.ogg", channel='crowd', loop=True, fadein=1.0)

$ RemoveEvent("Yellow", "LostHat")

scene kitchen 
show yellow neutralhat closedbrow frownmouth
show screen currentdate
with splitfade

$ renpy.pause(1.0, hard=True)

red @talkingmouth "Hey, Yellow. I see you got a new hat."

show yellow -closedbrow -frownmouth with dis

yellow @talkingmouth "Oh. Yes, Uncle Wilton sent me a spare last Sunday. It took a while to get here, though, given the distance."
yellow @happy "And good morning!"

red @talkingmouth "Just us here?"

yellow @talkingmouth "Ethan's sleeping in. But Blue and Leaf left early."

red @closedbrow talking2mouth "Blue's kinda been avoiding me all week. Like, I can get him in a room, but if he sees me walk in, he'll walk to the other side. Any idea what that's about?"

yellow @sadbrow talkingmouth "I think he's very conflicted about if he should talk to his grandpa, and seeing you probably just confuses him further."

red @closedbrow talking2mouth "I wasn't expecting such a literal answer, but, uh, yeah, I guess you're right."

pause 0.5

red @talkingmouth "...Sorry for the subject change, but how's Bianca? You two are both in the nurse course, right?"

yellow @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
yellow @talkingmouth "...I think this party today will be very good for her."
yellow @sad2eyes talkingmouth "She does so much for everyone else... but when she needs help, who's there to help her?"

if (GetRelationshipRank("Bianca") > 0):
    show yellow surprisedbrow frownmouth with dis

    red @happy "Me."

    yellow -surprisedbrow -frownmouth @talkingmouth "Oh... that's right. She did say you talked with her. She appreciated that."

    red @sadbrow talkingmouth "It was the least I could do."
    red @talkingmouth "Still, with Leaf throwing this party, at least she's got something to take her mind off things for a while."

else:
    red @closedbrow talkingmouth "...Yeah. Poor girl. Well, with Leaf throwing this party, at least she's got something to take her mind off things for a while."

yellow @talkingmouth "I've heard Leaf's parties can get fairly wild. I hope Leaf can keep things low-key for Dawn and Bianca..."

red @happy "I'm sure she can! There's nothing to worry..."
red @closedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

pause 1.0

red @talkingmouth "...Actually, maybe we should check in on her?"

yellow @talkingmouth "That's a good idea."

pause 1.0

yellow @sadbrow blush happymouth "Um... maybe we could also wake up Ethan?"

red @confusedeyebrows playfuleyes smirkmouth "Oh?"
red @confusedeyebrows talkingmouth "Was his flirting on Monday more effective than it seemed?"

yellow @scaredeyes surprisedeyebrows heavyblush surprised2mouth "N-n-n-n-no! I just don't like seeing him sleeping away all his weekends."

red @happy "Hey, he doesn't sleep them all away. I mean, last weekend, he went out into the forest to look for you."
red @closedeyes angryeyebrows talking2mouth "Although... Leaf {i}did{/i} have to drag him out of bed for that... alright, I see your point."
red @talkingmouth "Mind waking him up? I'm going to get some coffee."

yellow @talkingmouth "Sure. I thought you didn't need it, though?"

red @talkingmouth "I'm not going to lie, I may be developing a bit of an addiction."

yellow @sadbrow talkingmouth "...Ah. There are programs to help with caffeine rehab, you know."

red @happy "Yeah, my current coping strategy is to deny that I have a problem. That's all my health insurance covers."

hide yellow with dis

pause 2.0

red @talkingmouth "Hm, hm.~"
red @talkingmouth "Hey, [pika_name], you want a sip of coffee? Maybe it'll, like, energize you?"

$ PlaySound("pokemon/pikachu_happy1.ogg")
libpikachu @happyeyes happymouth "Piiika!"

pause 1.0

libpikachu @talkingmouth "{i}Sip.{/i}"

pause 1.0

$ PlaySound("pokemon/pikachu_confused2.ogg")
libpikachu @surprisedeyes surprised2mouth "Pikerachu?!"

red @confusedbrow talking2mouth "Or maybe you'll just have a spiritual experience. You doing okay, buddy?"

$ PlaySound("pokemon/pikachu_happy3.ogg")
libpikachu @happyeyes happymouth "Pika! Pikerachu!"

red @happy "Oh, that was a good reaction, then."

show yellow neutralhat with dis:
    xpos 1.2
    ease 0.5 xpos 0.75

pause 1.0

yellow @talkingmouth "Um, you two?"

red @talkingmouth "Yup?"

$ PlaySound("pokemon/pikachu_confused.ogg")
libpikachu @talkingmouth "Pi?"

yellow @blush talkingmouth "I can't, um, get Ethan up."

red @surprised "Hm? What do you mean?"

yellow @closedbrow talkingmouth "Well, I can hear him snoring in his room, but... I... um... I guess I'm not knocking on his door hard enough."

show yellow surprisedbrow frownmouth heavyblush with dis

red @happy "You can go in. Just shake him a bit."

yellow @talkingmouth "N-no, I definitely couldn't! What-- what if he's {size=30}{i}naked{/i}{/size}?"

red @talkingmouth "That's a benefit. He's a handsome guy!"

yellow @cryingeyes sadeyebrows sadmouth "Don't make fun of me... I'm shy."
yellow frownmouth @closedeyes angryeyebrows angrymouth "Besides, you shouldn't walk into someone's room without their permission. Even if they're not {size=30}{i}naked.{/i}{/size}"

red @confusedeyebrows frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
red @talkingmouth "Why are you whispering the word 'naked?'"

yellow fullblush -heavyblush @talkingmouth "D-don't say it so loudly! It's-- it's {i}embarrassing!{/i}"

red @talkingmouth "What, 'naked'?"

yellow sadbrow sadmouth @talkingmouth "...Ssssstooooop."

red @happy "Dude, it's a perfectly normal word. People use it to describe, like, non-GMO fruit."
red @talkingmouth "Besides, even if we were talking about people, I mean..."

red @talkingmouth "People get naked, you know? It's a fact. Nothing to be embarrassed about. Sometimes people get naked for business, sometimes people get naked for pleasure--"

show kitchen with vpunch

yellow -fullblush heavyblush surprised @scaredeyes angryeyebrows angrymouth "Stop saying {size=+10}{i}NAKED!{/i}{/size}"

show ethan underwear:
    xpos -0.2
    ease 0.5 xpos 0.25

ethan @talkingmouth "Did someone say naked?"

show yellow:
    xpos 0.75
    ease 2.0 xpos 0.8 rotate 1 ypos 1.03
    ease 0.5 xpos 0.8 rotate 5 ypos 2.0

pause 3.0

show kitchen with vpunch

red @confused "...You good?"

ethan @talking2mouth "She's dead, Jim."

red @talkingmouth "Damn. I was really starting to like her."

ethan @talkingmouth "Yeah, and we're going to have to spend the rest of our lives on the run from Blue, now."

red @happy "So, no difference for me."

ethan @closedbrow talking2mouth "He's {i}really{/i} not that bad, dude."

red @sideeyes angryeyebrows talking2mouth "I know."

pause 1.0

red @talkingmouth "So, were you just waiting to come in at--"

ethan @talking2mouth "At the appropriate comedic timing, yeah."

pause 0.5

red @happy "I'm impressed by your commitment."

ethan @talkingmouth "Thanks, man. Maybe I should be a comedian when I graduate."

red @talkingmouth "Really? You're on the Battle Team--I guess I just assumed you'd want to become a Pokémon Trainer."

ethan @closedbrow talking2mouth "I wouldn't say I don't. It's still on the table."
ethan @sadbrow talkingmouth "Got my whole life ahead of me, after all."

pause 1.0

ethan @talkingmouth "...Anyway, I'm going to go put my clothes back on. Don't go anywhere, I want to come with you two."

red @happy "Sounds good. Nice trunks, by the way."

ethan happy "Yeah, you too."

hide ethan with dis

pause 2.0

red @talkingmouth "Yellow? You alright down there?"

yellow @talkingmouth "Zzz..."

redmind @surprisedbrow frownmouth "Oh, she actually fell asleep. Huh."

stop music fadeout 1.5 channel "crowd"

call clearscreens() from _call_clearscreens_196
scene blank2 with splitfade

narrator "You, Yellow, and Ethan walk across campus to the Battle Hall, where, apparently, Leaf is setting up Dawn's party."

ethan @talkingmouth "Wonder what Leaf said to get access to the Battle Hall for a birthday party, of all things."

if (GetRelationshipRank("Janine") > 0):
    red @talkingmouth "Given how guilty Janine feels about the whole Dawn battle fiasco, probably just 'it's for Dawn.'"

    ethan @happy "Probably!"

yellow neutralhat @talkingmouth "I haven't been here since the Quarter Qlashes..."
yellow @happy "I hope it's a bit less scary without all those people in the stands screaming."

red @talkingmouth "I'm sure it'll be fine."

pause 0.5

if (HasEvent("Leaf", "AcceptedConfession")):
    red @happy "Oh, speaking of fine, there's Leaf now. She--"
else:
    red @happy "Oh, speaking of which, there's Leaf now. She--"

red @confusedeyebrows frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
red @confused "She does {i}not{/i} look happy."

stop music fadeout 1.5
queue music "audio/music/mansion_start.ogg" noloop
queue music "audio/music/mansion_loop.ogg"

scene relichall_A
show leaf angry
show ethan sad2eyes frownmouth:
    xpos 0.25
show yellow sadbrow frownmouth neutralhat:
    xpos 0.75
show screen currentdate
with splitfade

leaf @talking2mouth "I'm going to {i}kill{/i} Dean Drayden."

red @confused "You could try. I'm pretty sure he could bench-press your entire family with his pinky, though."

ethan @talking2mouth "What happened? Dean Draymond's cool."

leaf -angry angrybrow angrysmilemouth @closedbrow talking2mouth "Okay, so, I guess it's {i}technically{/i} not his fault, but I was planning this entire thing around the Battle Hall being open this weekend."
leaf @angry "I even asked ahead of time with Lance and Janine, and they said they'd make sure that the Battle Hall would be unoccupied."
leaf @closedbrow talking2mouth "But {i}apparently,{/i} today of all days, that purple-haired lawyer we saw at lunch on Tuesday {i}needs{/i} the entire Battle Hall to herself."
leaf @surprised "And when I complained, Drayden said his hands were tied! {i}His{/i} hands! The man breaks rules like it's going out of fashion, but now he's listening to some fancy purple-haired woman in a suit?"
leaf @angry "They even got a truck in there! I wasn't supposed to see that, but I had Jigglypuff float me up to a window..."

yellow @surprised "A... truck?"

leaf @talking2mouth "It looked like they were moving something out of it. Or maybe into it, I'm not sure. I didn't stay up there for very long."

leaf @talking2mouth "Still! I put {i}all{/i} this thought into the party, and now Drayden's completely stomped on my efforts!"
leaf @sadbrow talking2mouth "...My old roommates are going to be so disappointed. And Dawn..."
leaf @sadbrow talking2mouth "She told me this really sad story about her twelfth birthday. When I heard it, I practically burst into tears, and I swore I wouldn't let anything ruin this one..."

pause 1.0

yellow @talkingmouth "Well... why should we let it?"

show ethan -sad2eyes
show leaf surprisedbrow frownmouth
with dis

leaf @talking2mouth "What do you mean?"

yellow @talkingmouth "Is there any particular reason that the party {i}has{/i} to happen in the Battle Hall?"

leaf sadbrow @talkingmouth "I thought it'd be a neat 'full circle' kind of moment for Dawn, since she used to be a Battle Team member..."

show leaf angrybrow frownmouth
show yellow angrybrow frownmouth
with dis

ethan @talkingmouth "Yeah, but Blanca was in the Battle Hall when she got her Dad {w=0.5}{i}aaaaand{/i} I'm not finishing that thought."

leaf -angrybrow -frownmouth @angrybrow talking2mouth "{i}Good call.{/i}"

yellow -angrybrow -frownmouth @talkingmouth "My point is that if the Battle Hall isn't an absolutely mandatory part of the planning, then we can still turn this around."

leaf @talking2mouth "...[first_name], you still have that cake, right?"

red @talkingmouth "Right. It's just in the cooking club's room right now. But I can bring it anywhere you need."

leaf @talking2mouth "Okay. There's a club in town we could go to. Renting it out would be pricey, but not impossible. But..."
leaf @sadbrow talkingmouth "I think that might be a bit much for Dawn and Bianca. Want to keep it lower-key."

yellow @closedbrow talkingmouth "Bianca really likes, um, plush toys and carnival games. And Dawn likes high art, like sculpture and theater."
yellow @sadbrow talkingmouth "I'm not seeing a way we can mash these two together, though..."

ethan @closedbrow talking2mouth "Well... who says we have to?"

$ PlaySound("idea.ogg")

stop music fadeout 1.5

ethan closedbrow frownmouth @talking2mouth "Hold on, let me look something up."

pause 3.0

$ renpy.music.queue("Audio/Music/Cinnabar_Start.ogg", channel='music', loop=None, fadein=0.0, tight=None)
$ renpy.music.queue("Audio/Music/Cinnabar_Loop.ogg", channel='music', loop=True, tight=None)

ethan -closedbrow -frownmouth @talkingmouth "Sweet. There's a theater nearby showing {i}The Goddess of 1,000 Arms.{/i}" 
ethan @talkingmouth "It's this epic musical drama about a priestess who climbs up a mountain, dealing with her inner demons the entire way. It's a psychological thriller."
ethan @happy "Sounds just artsy enough for Daybreak, right?"

yellow @surprisedbrow talkingmouth "That might work!"

leaf @happy "Oh, and then, and {i}then{/i}, the county fair is going on! They've got, like, games, and rollercoasters, and all that stuff! We could totally go there with Bianca!"

red @talkingmouth "Sounds like we're going to have to split up, though. Unless you think subjecting Bianca to the drama of the mountainside is a good idea."

leaf @sadbrow talkingmouth "Yeah, I'm pretty sure Dawn wouldn't be a big fan of the rollercoasters, or the crowds at the fair, either."

ethan @closedbrow talking2mouth "Not to be a psycho therapist or anything, but Biatta might not be in the mood either."

yellow @talkingmouth "That's a good observation, Ethan. But presenting her the option is important. If she doesn't want to take us up on it, then... well, that's fine. Everyone recovers at their own pace."

ethan @happy "Dorm 25's most well-adjusted person has spoken. It's canon, now."

leaf @surprised "Most well-adjusted? Uh, excuse you, I'm--"

ethan @closedbrow talking2mouth "{i}Dangerously{/i} obsessive, about, like, a {i}lot{/i}, yes."

leaf @angrybrow talkingmouth "I agree with you, but, {i}oooh,{/i} I sure don't want to."

yellow @happy "Agreeing with a point that makes you look bad shows strength of character."

leaf @closedbrow talkingmouth "Please. {i}Nothing{/i} can make me look bad."

ethan @talkingmouth "Oh, yeah? What about, like, a trash bag? Just a regular old bag of trash, with some holes ripped in it?"

leaf @flirtbrow talkingmouth "That's high fashion on me, Ethan. Try a bit harder."

ethan @talkingmouth "...Dean Draythan's clothes."

leaf @talkingmouth "Well, besides the fact you could fit three of me in them, I think I'd rock them pretty well, yeah."

ethan @closedbrow talking2mouth "Alright. What about my clothes?"

leaf @sarcastic "Oh, I get it. This is just a really long-run ploy to try and swap clothes with me for a while, isn't it?"

ethan @happy "You can't prove it. {w=0.5}{size=30}(Cute skirt, bee tee dubs.){/size}"

leaf @happy "God, Ethan, you're {i}so{/i} weird. And that's coming from {i}me.{/i}"

yellow @talkingmouth "Weirdness is often correlated with uniqueness. Dorm 25 is, I think, a {i}very{/i} unique dorm."

red @happy "It's better than being boring."

leaf @angrybrow talkingmouth "Hell yeah, it is. And now, we, the least-boring students in Kobukan, are going to throw two awesome parties for two girls who {i}seriously{/i} need it."

show leaf surprisedbrow frownmouth blush with dis

red @talkingmouth "Preach, girlfriend."

pause 1.0

leaf -surprisedbrow -frownmouth @talkingmouth "Okay. Let's go over the details of the plan."

leaf @closedbrow talking2mouth "I've already sent out invitations. My old dormmates are coming."
leaf @talking2mouth "I figured Dawn knows May from the Coordinator Club, and Hilda and Serena are just super-nice, anyway."
leaf @sadbrow talkingmouth "If we're trying to get Dawn some new friends, I figured those three would be good options, and they already want to help Bianca, so it's the best of both worlds."
leaf sadbrow @happy "{size=30}AndIalsoinvitedCheren.{/size}"

red @sad2eyes angryeyebrows frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
red @talking2mouth "I won't start anything as long as he doesn't."

leaf @happy "Great. Was worried that this entire plan was going to collapse, again, when I said that."

red @happy "You think so little of me?"

leaf @talkingmouth "You're the nicest guy I've ever met, but, uh, you {i}do{/i} kinda hold a grudge."

red @surprised "What? Really?"

yellow @closedbrow talkingmouth "'Holding grudges is like drinking poison, and expecting the other person to die.'"

ethan @talkingmouth "Nah, that's voodoo."

show yellow surprisedbrow frownmouth with dis

red @closedbrow talking2mouth "I don't think I'm a vengeful guy... I mean, I even apologized to Blue on Thursday, about the whole meteorite shard thing..."

leaf @happy "Great! That's progress."

yellow -surprisedbrow -frownmouth @happy "And now I get why he was so happy Thursday afternoon. I was wondering what had snapped him out of his funk!"

red @confused "He was happy? How can you tell?"

leaf @sarcastic "There's this weird thing he does where the corners of his mouth bend {i}upwards.{/i}"

ethan @closedbrow talking2mouth "Sounds fake."

leaf @happy "Might be, but I'm still going to sell tickets to see it!"

red @talkingmouth "Guys, focus up. Dawn's birthday, remember."

leaf closedbrow frownmouth @neutralbrow talkingmouth "I remember, I remember. Alright, so... let me think for a moment."

pause 1.0

leaf -closedbrow -frownmouth @talking2mouth "The invitations will be calling people out to the Battle Hall, since that's where I {i}thought{/i} this was going to happen."
leaf @talking2mouth "We'll wait until everyone gets there, then split the party--literally--and go our separate ways."

yellow @closedeyes angryeyebrows talkingmouth "I think Dawn might actually prefer that... she's in class with Hilbert, but I don't think she knows any of Bianca's other roommates. She might be overwhelmed."

leaf @talking2mouth "Dawn's group will go to the theater Ethan mentioned. And Bianca's group will go to the fair outside of the city."
leaf @talkingmouth "Then, at 4:00 PM, we'll all meet back here on-campus, give Dawn our presents, and share the cake that [first_name] made. Sounds good?"

red @happy "Sounds like a 100%% classic Leaf plan."

leaf @talkingmouth "I'm... not sure what that is, but alright!"

ethan @talkingmouth "Hey, you're not going to make us put our hands in and do one of those cheesy four-person fist bumps or anything, are you?"

leaf @surprisedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
leaf @happy "Well, I sure am {i}now!{/i}"

pause 1.0

leaf @sadbrow talking2mouth "{size=30}Kinda a shame Blue isn't here, though...{/size}"

show leaf happy with dis:
    xpos 0.5
    ease 0.5 xpos 0.5 ypos 1.1 zoom 1.2

leaf @happy "But put 'em in! Dorm 25!"

show yellow happy with dis:
    xpos 0.75
    ease 0.5 xpos 0.75 ypos 1.1 zoom 1.2

yellow @happy "To friends and fun! Dorm 25!"

show ethan happy with dis:
    xpos 0.25
    ease 0.5 xpos 0.25 ypos 1.1 zoom 1.2

ethan @talkingmouth "This is so incredibly corny. Dorm 25!"

menu:
    "Inspirational message! Dorm 25!":
        show ethan surprisedbrow frownmouth
        show yellow surprisedbrow frownmouth
        show leaf surprisedbrow frownmouth
        with dis

        pause 1.0

        leaf happy "Wow, you're {i}terrible{/i} at this! I love it!"

        redmind @sadeyebrows closedeyes sweat "It's nice to be appreciated."

    "For gold and glory! Dorm 25!":
        show ethan surprisedbrow frownmouth
        show yellow surprisedbrow frownmouth
        show leaf surprisedbrow frownmouth
        with dis

        pause 1.0

        leaf happy "Not sure where the gold's coming from, but this will definitely be glorious!"

        redmind @sadeyebrows closedeyes sweat "Yeah, I'm not sure where the gold's coming from either..."

    "Rock and stone! Dorm 25!":
        show ethan surprisedbrow frownmouth
        show yellow surprisedbrow frownmouth
        show leaf surprisedbrow frownmouth
        with dis

        pause 1.0

        ethan happy "Rock and stone! To the bone!"

        leaf sadbrow sadmouth "...It's too late. [first_name]'s become Ethanized. We're going to have to amputate."

        yellow happy "I have a bone saw!"

    "Let's split up! Dorm 25!":
        show ethan surprisedbrow frownmouth
        show yellow surprisedbrow frownmouth
        show leaf surprisedbrow frownmouth
        with dis

        pause 1.0

        leaf happy "Okay, I realize that that's what the plan is, but there {i}had{/i} to be a better way to say that."

        red @happy "Why choose good word when time short and bad word work also?"

        ethan closedbrow talking2mouth "Love him or hate him, man's spitting facts."

call clearscreens() from _call_clearscreens_197
scene blank2 with splitfade

pause 1.0

$ partyviewer = False

show noon at vspaz

pause 3.5

scene colosseum 
show screen currentdate
with splitfade

pause 1.0

show leaf:
    xpos 0.75
show ethan:
    xpos 0.85
show yellow:
    xpos 0.95
with dis

narrator "The four of you have returned to the Battle Hall, waiting for Dawn's partyguests to arrive."
narrator "In order to pass the time, you've turned towards various games..."

ethan @talkingmouth "And that's 'Toe.' I win. Again. Good try, Yellow."

leaf @closedbrow talkingmouth "I don't get it. It's literally Tic-Tac-Toe. How do you keep winning?"

ethan @happy "King of Games, like I said."

yellow @talkingmouth "I know there's some rule he's following to keep winning like this."

ethan @sadbrow talkingmouth "It's more of a character flaw that I'm exploiting."

yellow @talkingmouth "Hm? What do you mean?"

ethan @happy "Hey, is it cool if I go first again?"

yellow @sad "I mean... you've gone first the past three times?"

ethan @talkingmouth "Yeah, but, like... please?"

yellow @happy "Oh, alright. Maybe I could go first next time, though?"

ethan @happy "Yeah, we'll consider that."

leaf sadbrow talkingmouth "Oh, I get it."

pause 1.0

show yellow surprisedbrow frownmouth with dis

show colosseum with vpunch

leaf -sadbrow -talkingmouth @angry "Hey! Stop bullying Yellow!"

ethan @angryeyes confusedeyebrows talking2mouth "You were totally fine with it a second ago!"

show yellow -surprisedbrow -frownmouth -surprised with dis

leaf @talking2mouth "Well, that's just because I wanted to know how you were doing it. I know, now, so you-- hm?"

stop music fadeout 1.5
$ renpy.music.queue("Audio/Music/New_Adventure_Start.ogg", channel='music', loop=None, tight=None)
$ renpy.music.queue("Audio/Music/New_Adventure_Loop.ogg", channel='music', loop=True, tight=None)

show hilda:
    xpos -0.2 xzoom -1
    ease 0.5 xpos 0.5

hilda @smirkmouth "Hey! Interrupting anything?"

leaf @happy "Nope! Just Ethan being a--"

ethan @talkingmouth "King of Games."

hilda @smirkmouth "Cool."

pause 1.0

hilda @talkingmouth "I'm the first one here?"

leaf @happy "Of course you are! You always were. You had a to-do list bigger than any of our schedules, but you always got everything done sooner than the rest of us, too."
leaf @sadbrow talkingmouth "I never realized how good I had it with you as a dormmate. I love these new guys, but, besides Yellow, they're kinda hopeless when it comes to keeping the dorm running."

yellow @closedbrow talkingmouth "{size=30}We might have an easier time if you did any of the chores...{/size}"

hilda @closedbrow talking2mouth "Same. I missed you. Dorm 251 isn't the same without you."
hilda @closedbrow talkingmouth "I dormed with Hilbert because I figured he needed it, but... uh..."
hilda @sad "I forgot that would mean I'd have to {i}live{/i} with him."
hilda @happy "Don't know how you managed it, [first_name]. At least I've learned a few tricks over the years."

red @happy "He's alright. Just don't talk to him before seven, and put little pieces of rubber on the door to dampen the impact when he slams it."

hilda @happy "Oh, you figured out the rubber thing, too?"

red @happy "Yeah! Still got a bunch of them, in case you want some extras, if he wears them out."

hilda @happy "It's more of a question of 'when' he wears them out."

show may sadbrow behind hilda:
    xpos -0.2
    ease 0.5 xpos 0.35
show lisia incognito incogbrow incogshades:
    xpos -0.2
    ease 0.5 xpos 0.25

hilda @smirkmouth "Speaking of wearing them out..."

leaf @happy "May! So glad you could make it. Did the Coordinator Club release its clutches 'pon you?"

may @talkingmouth "A little bit. {size=30}See, Liz? I told you it's a real party. Prior commitment. Can't do anything about it...{/size}"

lisia @closedincogbrow talking2mouth "Hm... well, Dawn {i}did{/i} say that today was her birthday."

lisia @angryincogbrow talking2mouth "Alright! I believe you! But I'll expect to see you in the contest hall extra early on Monday!"

may @closedbrow sadmouth "Yes, Liz..."

lisia @happyincogbrow talkingmouth "Thanks for throwing this party for Dawn, everyone! I think she'll really appreciate it."
lisia @sadincogbrow talkingmouth "She told me this story about her twelfth birthday party, and... well, frankly, I'm surprised she's even willing to have another."

pause 0.5

lisia @happyincogbrow happymouth "Suppose you can't help getting older, though!"

hide lisia with dis

pause 1.0

may frownmouth "{size=30}Ugh...{/size}"

show hilda surprisedbrow frownmouth with dis:
    xpos 0.5 xzoom -1
    ease 0.5 xzoom 1

hilda @talkingmouth "Shit, you okay?"

may @sadbrow talkingmouth "Lisia's... {i}always{/i} running after Brendan and I... and..."

pause 1.0

may -frownmouth @closedbrow sadmouth "Brendan runs faster."

show hilda -surprisedbrow -frownmouth with dis:
    xpos 0.5 xzoom 1
    ease 0.5 xzoom -1

leaf @talking2mouth "No loyalty in matters of contests or battles, I guess."

show serena with dis:
    xpos 0.25

serena @talkingmouth "{i}Bonjour.{/i}"

leaf @happy "{i}Buongiorno!{/i}"

yellow @talkingmouth "{i}Hola.{/i}"

ethan @talkingmouth "{i}こんにちは。{/i}"

serena @happy "It's good to be back amongst you again."
serena @sadbrow talkingmouth "Reminds me of simpler days."

leaf @talking2mouth "Yeah, and you guys finally have a chance to catch up with each other again!"

hilda @closedbrow talkingmouth "We're pretty caught up, actually. Serena's our connector."

serena @talkingmouth "Yes. I have Fire Classes with May, so there's little catching-up to do."

leaf @sadbrow talkingmouth "Aw. Guess I'm the odd woman out, then. The only one who doesn't have some bond to the old dorm."

may -sadbrow @talkingmouth "Well, not entirely, right? You're taking Normal classes now, right? And Bianca is there. Plus, Bianca and Hilda are... still roommates... so..."

pause 1.0

may @closedbrow sadmouth "Oh. I just put my foot in my mouth, didn't I?"

leaf @sadbrow talkingmouth "Nah. We'd need to cross that bridge eventually."

pause 0.5

leaf @sadbrow talkingmouth "So... does anyone know if Bianca's planning on coming? It'd be really great if we got the whole dorm together, but if she's, you know, not in the mood..."

hilda @sad "She was still in bed when I left the dorm. She said she was planning on coming, but, I mean... no-one would blame her if she skipped out, you know?"

ethan @talkingmouth "Don't mean to butt in, but, uh, are Yellow, [first_name], and I actually {i}invited?{/i}"

may @surprisedbrow sadmouth "{size=30}Did he just get two people's names right in the same sentence?{/size}"

leaf @happy "I mean, duh! You're... you are..."
leaf @closedbrow talking2mouth "Come to think of it, [first_name] made the cake, but you two didn't really do anything, did you?"

ethan @sadbrow talkingmouth "I'll be real with you, I don't even have a present."

yellow @sadbrow talkingmouth "The last time I saw Dawn, I was, um, healing Blue's Pokémon while she beat him over and over."
yellow @happybrow talkingmouth "She probably doesn't like me a whole lot."

ethan @happy "Don't be silly, Yellow, everyone likes you. And besides, Daybreak's kinda starved for friends. She's not in any position to be turning anyone down."

show dawn with dis:
    xpos 0.15

dawn @talkingmouth "H-hi."

ethan @closedbrow talking2mouth "...It's almost funny, in a cosmic sense."

leaf @happy "Dawn! Maiden of honor. Happy Birthday, sweetheart!"

dawn @happy "Thank you."
dawn @talkingmouth "Um... thank you {i}very{/i} much for putting this together. It really means a lot to me..."
dawn @sadmouth "I hope it wasn't... too much trouble?"

leaf @talkingmouth "For you? Not at all!"

hilda @happy "How does it feel, Dawn? A year older! Any grey hairs yet?"

dawn @happy "Haha! Nope!"

pause 1.0

dawn @sadbrow talkingmouth "I'm... I'm sorry, I think there are a few faces I don't know here? I know that you're in my homeroom, May, and I know you, Leaf and Ethan, from the Battle Team, but...?"

serena @talkingmouth "Of course! My name is Serena. A pleasure to make your acquaintance. I am one of Leaf's former roommates."

leaf @talkingmouth "And the fanciest girl you'll ever meet. And on the other side of the spectrum is..."

hilda @happy "Hilda's my name. I saw that shit you pulled in the Battle Hall, during the Quarter Qlashes. You might've lost, but that was a hell of a show. Good work."

yellow @sadbrow challengingmouth "And I'm... Yellow. You probably recognize me."

dawn @happy "Of course I do! Good to see you again. And I'm glad to meet you two, too."

yellow @happy "{size=30}Good to see me again! That's what she said!{/size}"

ethan @closedbrow talkingmouth "{size=30}Of course it is. C'mon. You're {i}Yellow.{/i}{/size}"

may @talkingmouth "Well, looks like we're just about all here..."

pause 1.0

hilda @talkingmouth "I guess Bianca decided not to come, then."
hilda @closedbrow talkingmouth "Shit sucks, but not much we can do about it. Guess she just needs more time."

red @confused "Come to think of it, didn't Hilbert say he'd be coming, too?"
red @closedbrow talking2mouth "Besides, you said you also invited Cheren?"

serena @surprised "In truth? That's rather brassy."

hilda @closedbrow talking2mouth "Not my first pick, but I see where you're coming from. They're friends."

red @angryeyebrows sad2eyes talking2mouth "I can't imagine him being late to something without a good reason."

leaf @surprised "Oh!"
leaf @closedbrow talkingmouth "So you think..."

red @talkingmouth "I don't know. But maybe we should all go check on Bianca?"
red @sadbrow talkingmouth "I mean, if you're cool with that, Dawn? It's your party, after all."

dawn @happy "Oh! Yes, absolutely. We should check on her. Bianca was you guys' fifth roommate, right, Hilda?"

hilda @talkingmouth "Yep."

dawn @talkingmouth "It'd be a shame if only the four of you were here. The set's incomplete. 'Gotta Catch 'em All', you know?"
dawn @closedbrow sadmouth "...That's something an old TV Show I used to watch said."

red @talkingmouth "Sounds catchy. I like it."

scene blank2 with splitfade

narrator "You, Ethan, and Yellow, split off as Leaf and her old roommates head off in a different direction, searching for Bianca, Cheren, and Hilbert."

pause 1.0

ethan @talkingmouth "I'm calling it now. We're going to have to go into the forest again."

yellow neutralhat @sadbrow talkingmouth "Oh no..."

red @happy "Nah, Hilbert probably's still asleep, and Bianca's probably just getting ready."

ethan @closedbrow talking2mouth "Uh-huh. And Chowder?"

red @upeyes talking2mouth "I have no idea what he's doing. Don't want to waste any brain cells on trying to figure it out, either."

ethan  @talking2mouth "...Aight."

scene hall_A2:
    xalign 0.0 yalign 1.0 xpos -480 ypos 1250 zoom 0.85
show screen currentdate
show ethan:
    xpos 0.33
show yellow neutralhat:
    xpos 0.66
with splitfade

ethan @talkingmouth "Hey. I just realized something."

red @talkingmouth "Hm?"

if (HasEvent("Bianca", "Comfort")):
    ethan @happy "We broke the echo this week."

    red @closedbrow talking2mouth "Huh?"

    ethan @talkingmouth "After lunch, you didn't show up to electives. I did. That means I attended an elective you didn't."

    red @happy "Oh, seriously? That's pretty funny. You know, some day, we should make a plan to see if we can purposefully avoid taking the same elective."

else:
    ethan @talkingmouth "So I was thinking about 'the echo', you know? How we keep ending up doing the same things?"

    red @talkingmouth "Sure."

yellow @confusedeyebrows unamusedeyes talkingmouth "I'm sorry, what are you talking about?"

ethan @talkingmouth "Oh, it's the weirdest thing. We--"
ethan @surprisedbrow frownmouth "Hm?"

red @talkingmouth "What is it?"

ethan talking2mouth "Look."

hide ethan
hide yellow
with dis

show hilbert smilemouth:
    xpos 0.75
show cheren happybrow smilemouth:
    xpos 0.25
show bianca happy:
    ypos 1.0
    block:
        ease 1.0 ypos 1.05
        ease 1.0 ypos 1.0
with dis

pause 2.0

redmind @surprisedbrow frownmouth "They look... happy."

cheren @talkingmouth "I admit, I was worried at first when you didn't respond to my knocking. I thought you might still be asleep."

bianca @happy "Haha! No waaaaaay. Hilbert doesn't sleep. He just stares."

hilbert @happymouth "That's mostly true."

cheren surprisedbrow -smilemouth @sadbrow sadmouth "Well, I'm glad to see you're feeling better. I know this was a--"

bianca @angrybrow poutmouth "Mmmmnope."

cheren @talkingmouth "Beg pardon?"

bianca @closedbrow talking2mouth "No sad thoughts today. Today is Dawn's birthday! That means happy faces only."

cheren -surprisedbrow @sad2eyes talkingmouth "It's not... {i}healthy{/i} to bury these things, but..."

bianca @talkingmouth confusedeyebrows "Sorry, which one of us has been studying to be a psychologist again?"

cheren surprisedbrow @talkingmouth "Er, well..."

bianca @happy "Come on! Let's go."

hide bianca with dis

pause 2.0

show cheren -surprisedbrow with dis

hilbert -smilemouth @talkingmouth "She's not as fragile as you think."

cheren @upeyes sadmouth "I was simply attempting to ensure my good friend was taken care of--"

hilbert @closedbrow talkingmouth "I think we've all had enough of your brand of 'care', Cheren."

hide hilbert with dis

show cheren sad2eyes angryeyebrows shadow with dis

pause 2.0

hide cheren with dis

pause 2.0

show ethan:
    xpos 0.7
show yellow neutralhat:
    xpos 0.85
show bianca:
    xpos 0.45 ypos 1.0
    block:
        ease 1.0 ypos 1.05
        ease 1.0 ypos 1.0
        repeat 3
show hilbert behind bianca:
    xpos 0.3 xzoom -1
show cheren:
    xpos 0.15
with dis

bianca @talkingmouth "Hiii~iii~ya, you guys! Sorry I kept you waiting."

show yellow surprisedbrow frownmouth with dis

bianca @happy "Makeup took a bit longer than usual. You get it, right, Yellow?~"

yellow -surprisedbrow -frownmouth @talkingmouth "Oh... yes. My hair takes ages in the morning."
yellow @happy "Most of the time, I just stuff it in my hat, so I don't have to bother with it, though."

bianca @surprisedbrow talkingmouth "Ooh! That's clever! {w=0.5}{size=30}I don't think I could do that with my hair down, though. Maybe if I put it up in a bun--but I don't think my hair's actually long enough for that, and if I did that then my hat might seem a bit lumpy, or people might think I'm smuggling food in my hat, which I'm not, and that would just be awful, I don't want that, but I could do with a haircut, and--{/size}"

narrator "You zone out slightly, as you look over Cheren and Hilbert. Both of them seem tense, but that's to be expected."

red @talkingmouth "Hi."

hilbert @closedbrow talkingmouth "We saw each other yesterday."

red @upeyes talking2mouth "I was saying 'hi', not 'it's been three thousand years, how desperately I have missed you.'"

cheren @closedbrow smilemouth "{size=30}Heh.{/size}"

hilbert @sadbrow sadmouth "Et tu, Cheren?"

cheren @sad2eyes talkingmouth "We have no connection beyond your very minor insult two minutes ago. This does not apply."

show hilbert:
    xpos 0.3
    ease 0.5 xzoom 1

hilbert @angrybrow talkingmouth "It just seems awfully convenient that you're willing to put all your grudges aside the moment there's a chance to laugh at--"

show hilbert:
    xpos 0.3
    ease 0.5 xzoom -1

yellow @sadbrow happymouth "H-hey! How about we just leave this conversation here, and, um, go meet up with the rest of the girls?"

ethan @talkingmouth "All your old roommates were talking about how they missed you, Bel."
ethan @sadbrow happymouth "Couldn't start the party without you."

bianca @happy "Aw! They're so sweet."
bianca @closedbrow talking2mouth "My new dorm is so full of testosterone, it's sometimes hard to breathe. I miss them, too."

ethan @happy "Really? Hitchcock doesn't strike me as the 'full of testosterone' kind."

hilbert @angry "Why am {i}I{/i} the one being made fun of here?!"

bianca @happy "Don't worry, Hillie~bert! I wasn't talking about you."

hilbert @closedbrow sadmouth "Good."

pause 1.0

hilbert surprisedbrow frownmouth @surprised "Wait, but then--"

bianca @happy "I was talking about Bea!"
bianca @happy "She's way manlier than you!"

pause 2.0

hilbert @sadbrow talkingmouth "I'm going back to the dorm."

show bianca:
    xpos 0.45
    block:
        linear 0.2 ypos 1.05
        linear 0.2 ypos 1.0
        repeat 10

bianca sadbrow sadmouth "What? Noooo! {w=0.5}{size=30}If you leave then I'll be so upset in my moment of need and I won't be able to stop crying and then the party will be absolutely ruined and your Ice classes will be super awkward and everyone will hate me and you and I won't be able to endure the social pressure, so I'll have to drop out and no-one will miss me and then we'll know what it's like to be Cheren!{/size}"

ethan @confusedeyebrows talking2mouth "Wow. She's just firing wildly today, huh? Nobody's safe."

cheren @talkingmouth sad2eyes "Well, she's not wrong."

hilbert angry "Fine! Fine! You've convinced me, alright?! Just... stop being so... {i}sentimental!{/i}"

stop music fadeout 1.5

pause 2.0

show cheren sad
show ethan sad
show yellow sad

hilbert sad ".{w=0.5}.{w=0.5}.{w=0.5}"

bianca soullesseyes frownmouth @talking2mouth "My father was murdered {i}four days ago.{/i}"

pause 2.0

$ renpy.music.queue("Audio/Music/New_Adventure_Loop.ogg", channel='music', loop=True, tight=None)

bianca happy "So I'll be whatever I want to be, okaaaaaaay?~"

hide bianca with dis

redmind @surprisedbrow frownmouth "I am quickly realizing that Bianca is an absolutely loose cannon."

ethan -sad @talking2mouth "Let's, uh... let's go... [first_name], mind telling Loaf we found Blanka?"

red @talkingmouth "You got it."

call clearscreens() from _call_clearscreens_198
scene blank2 with splitfade

pause 1.0

scene colosseum 
show screen currentdate
show cheren:
    xpos 1/11
show hilbert behind cheren:
    xpos 2/11 xzoom -1
show bianca:
    xpos 3/11
show serena behind bianca:
    xpos 4/11
show may behind serena:
    xpos 5/11
show hilda:
    xpos 6/11
show dawn:
    xpos 7/11
show leaf behind dawn:
    xpos 8/11
show ethan:
    xpos 9/11
show yellow neutralhat:
    xpos 10/11
with splitfade

pause 1.0

ethan @talkingmouth "Bit tight in here."

leaf @talking2mouth "Yeah, we're kinda blocking the path..."

show blank2 with dis:
    alpha 0.2

hide bianca
hide dawn
show bianca with dis:
    xpos 3/11 ypos 1.0
    ease 0.5 xpos 0.33 ypos 1.1 zoom 1.2

show dawn surprisedbrow frownmouth with dis:
    xpos 7/11 ypos 1.0
    ease 0.5 xpos 0.66 ypos 1.1 zoom 1.2

bianca @happy "Heeeeey, Dawn!~ Happy Birthday! Soooo~rrry I was late!"

dawn @sadbrow talkingmouth "N-no, it's completely fine. I understand that--"

show bianca:
    xpos 0.33
    block:
        ease 0.3 ypos 1.15
        ease 0.3 ypos 1.1
        repeat 5

bianca @happy "Yep! Makeup just takes {i}sooooo{/i} long. Oh well!~ I'm here now."

show bianca:
    xpos 0.33 ypos 1.1 zoom 1.2
    ease 0.5 xpos 3/11 ypos 1.0 zoom 1.0

show dawn -surprisedbrow -frownmouth with dis:
    xpos 0.66 ypos 1.1 zoom 1.2
    ease 0.5 xpos 7/11 ypos 1.0 zoom 1.0

hide blank2 with dis

dawn @talkingmouth sadbrow "I, uh, I see you're here, too, Hilbert."

hilbert @talkingmouth "I am. {w=0.5}Happy Birthday."

pause 1.0

cheren @surprised "Oh. Right."
cheren @talkingmouth "Happy Birthday. I don't believe we've had the pleasure of an introduction. I am Cheren."

if (HasEvent("Dawn", "Level2SceneVer2")):
    dawn @sad "I remember. I was there in the auditorium."

    show cheren surprisedbrow with dis

    pause 1.0

    cheren -surprisedbrow @talkingmouth "...Yes. I recall that now. I... said a lot of things I should not have that day."
    cheren @sad "I apologize. From the bottom of my heart. There was no reason to say what I had... paranoia and suspicion fueled my actions."

    pause 1.0

    cheren @talkingmouth "If you would like me to... leave, I will, absolutely."

    dawn @sadbrow talkingmouth "N-no. It's fine. You can... you can stay."

    cheren @sad "I do not deserve this, but I am grateful."

else:
    dawn @surprised "{i}You're{/i} Cheren? I thought..."
    dawn @sadbrow talkingmouth "On second thought, I probably shouldn't say that."

    cheren @upeyes talkingmouth "No, I do not possess horns, nor a pointed tail."
    cheren @sad2eyes talkingmouth "The forked tongue, I do possess, but I keep that well hidden."

leaf @talkingmouth "Enough chatting! Let's get this show on the road!"

pause 1.0

leaf @talking2mouth "If that's cool with the birthday girl?"

dawn @happy "Of course! Um, you kinda seem to know how this 'birthday' thing works... and I don't... so you can go ahead and take control."

leaf @flirtbrow talkingmouth "You hear that, everyone? Birthday girl says I can 'take control.' Change of plans, this is now a costume party. Skimpiest outfit wins a prize."

ethan @confusedeyebrows talkingmouth "No other criteria?"

leaf @surprised "Huh? I mean, I didn't think through the bit this far, but I guess not..."

pause 1.0

leaf @angrybrow angrymouth "You're trying to game the system, aren't you?"

if (HasEvent("Instructor Wallace", 1)):
    ethan @closedbrow talkingmouth "Pretty sure Instructor Wallace has a spare Speedo I could borrow."

    may @surprised "{size=30}There! He did it again! He got someone's name right! What's the pattern here?!{/size}"

else:
    ethan @closedbrow talkingmouth "Pretty sure the Water-type instructor has a Speedo I could borrow."

leaf @closedbrow talkingmouth "Okay, well, all y'all have got {i}that{/i} in your minds now, and I've never been happier to be aphantastic."

show bianca talkingmouth
show yellow talkingmouth
with dis

Character("{color=#55b13c}Bianca{/size} & {color=#f2a634}Yellow{/size}") "\"It's actually 'aphantasic'.\""

show bianca surprisedbrow frownmouth
show yellow surprisedbrow frownmouth
with dis

Character("{color=#55b13c}Bianca{/size} & {color=#f2a634}Yellow{/size}") "\"Huh.\""

show bianca happy
show yellow happy
with dis

Character("{color=#55b13c}Bianca{/size} & {color=#f2a634}Yellow{/size}") "\"Hah, jinx!\""

hilda @closedbrow talking2mouth "Medical course, I swear. Every time I try to say something casual about what I'm thinking or feeling, Bianca tells me exactly what chemical's making me feel that way."

bianca @talkingmouth "That's because we're all just pieces of meat powered by electricity and chemical reactions! Nothing we experience is real, it's just how we consistently misinterpret sensory input!"

serena @sadbrow talkingmouth "Well, that's a rather... eh... depressing way of looking at it, no?"

bianca @surprised "You think so?" 
bianca happy "I find it kind of liberating!"

show cheren closedbrow smilemouth
show may happy
show serena happy
show ethan happy
show yellow happy
show dawn happy
show leaf happy
show hilbert closedbrow smilemouth
with dis

$ PlaySound("pokemon/pikachu_happy3.ogg")
libpikachu @happyeyes happymouth "Pika! Pikerachu!"

red @happy "Not talking about you, buddy!"

stop music fadeout 1.5

call clearscreens() from _call_clearscreens_199
scene blank2 with splitfade

pause 1.0

show noon at vspaz
$ timeOfDay = "Noon"

pause 3.5

queue music "audio/music/evolution.ogg"

narrator "After explaining the plan to the partygoers, and obtaining Dawn's consent, everyone agrees to follow Ethan's plan of splitting off and rejoining."
narrator "{color=#f2a634}Yellow{/color}, {color=#c1861e}Ethan{/color}, {color=#353535}Hilbert{/color}, {color=#1f67df}Cheren{/color}, and {color=#55b13c}Bianca{/color} will go to the fair."
narrator "{color=#00b23f}Leaf{/color}, {color=#493bff}May{/color}, {color=#cc8fdb}Dawn{/color}, {color=#ea5091}Hilda{/color}, and {color=#cb6e8b}Serena{/color} will go to the theater."
narrator "Which group would you like to go with?"

menu:
    ">Go to the theater":
        $ AddEvent("Dawn", "BirthdayTheater")

    ">Go to the fair":
        $ AddEvent("Dawn", "BirthdayFair")
        jump parkgo

label theatergo:
    stop music fadeout 1.5
    $ renpy.music.queue("Audio/Music/snowpoint.ogg", channel='music')

    narrator "You walk with the girls to the theater."

    scene city_A
    show may:
        xpos 2/6
    show dawn:
        xpos 3/6
    show hilda:
        xpos 4/6
    show serena:
        xpos 1/6
    show leaf:
        xpos 5/6
    with splitfade

    dawn @happy "I'm surprised you all wanted to go to the theater! I didn't realize that Kobukan had such a thriving drama community."

    hilda @talking2mouth "You kidding? This school's practically built on drama."

    dawn @talkingmouth "That's fantastic. In Sinnoh, I used to love watching this playwright's works. He's penned a couple more, all sort of set in the same world."
    dawn @closedbrow talkingmouth "Let's see... there was 'The Red Chain'. That was a good one. Then there was 'Moonlit Dance of Dreams.'"
    dawn @happy "Most of his works are based on some form of Sinnohan mythology."

    if (GetRelationshipRank("Dawn") > 0):
        redmind @thinking "I know she takes a lot of inspiration from Sinnohan mythology in her sculptures..."

    else:
        red @talkingmouth "I didn't know you had an interest in Sinnohan mythology."

        dawn @talkingmouth "Yeah, it's useful for, um, inspiration."
        dawn @sadbrow talkingmouth "Inspiration for nothing in particular."

        red @happy "Sounds legitimate!"

    may @talkingmouth "Does that mean you've already seen {i}Goddess of 1,000 Arms{/i}, then?"

    dawn @talkingmouth "No!"
    dawn @sadbrow talkingmouth "But I've already had the twist at the end spoiled for me."

    serena @angry "Ooooh, I hate that! Inconsiderate cretins who rip all the suspense out of a well-foreshadowed story... unmarked spoilers are {i}the worst.{/i}"

    hilda @talkingmouth "Same. Worst part is when they give you spoilers {i}when{/i} you're watching the movie."
    hilda @angry "It's like, I don't {i}care{/i} how it happened in the comics, I'm never going to read them. I'm just watching the movie, and want to see how the movie does it!"

    may @talkingmouth "I feel like you're speaking from experience."

    hilda @sad "It was more of a problem when Hilbert was younger. He doesn't read many comics nowadays."

    pause 1.0

    hilda @talking2mouth "Anyway, I gotta stop thinking about him. For the next four hours, he's someone else's problem."

    may @talkingmouth "That's the spirit! I have a brother who's a bit like that. When it comes to spoilers, I mean."

    serena @talkingmouth "Oh, I think you mentioned him a while ago. Max, correct?"

    may @talkingmouth "Yeah, that's his name. Cute as a button, but he can {i}kinda{/i} be a bit insufferable about movies..."
    may @closedbrow sadmouth "He's impossible to surprise, and will always predict what's about to happen next in them. The worst part is, he's always right."

    leaf @happy "Aw, but that's cute. It's a sign of an active, engaged mind."

    may @happy "I'm not saying it's not cute! And he {i}really{/i} is super-smart. Much more of a scientist's kid than I am. Just... frustrating to watch movies with."
    may @angry "Like, one time, we were watching Volcarona vs. Rillaboom Raja, and he said in the opening five minutes that Volcarona would lose, and he was right! And I hated that!"
    may @closedbrow sadmouth "And not just because the writers totally ignored Volcarona's type advantage over Rillaboom Raja..."

    leaf @talking2mouth "I get that. I was watching {i}Hot, Wet, Bikini Summer{/i} recently, and some jerk totally spoiled that the uptight teacher turns into a good guy at the end."

    hilda @surprised "Wait, haven't you watched that movie, like, a hundred times?"

    leaf @closedbrow talking2mouth "Sure, but I wasn't the only person in the cinema."

    serena @talkingmouth "They were showing that movie in a cinema? I thought such a thing was only for adult video stores."
    serena @closedbrow sadmouth "Perhaps Kobukan is a more permissive nation than I had thought."

    leaf @happy "What? No, you totally have the wrong idea! Rosa's in it! HWBS isn't {i}that{/i} kind of movie {w=0.5}{size=30}unfortunately{/size}, {w=0.5}it's actually this great musical about letting loose of who you {i}think{/i} you should be and being whoever makes you happy! And Rosa's in it!"

    serena @sadbrow talkingmouth "I see. Perhaps I should watch this, then."

    pause 1.0

    hilda @talkingmouth "...Speaking of movies, aren't we going the wrong way for the cinema?"

    dawn @talkingmouth "Hm? Yeah, but we're going to the theater."

    hilda @talkingmouth "Huh."

    pause 1.0

    show dawn surprisedbrow frownmouth with dis

    hilda @talkingmouth "Okay, so, like, I guess I don't know what the difference between a theater and a cinema is."

    dawn @talkingmouth "Oh."

    pause 1.0

    dawn @talkingmouth "So that's why you were all talking about movies."
    dawn -surprisedbrow @sadbrow talkingmouth "I'm really sorry. I messed up. I thought we were going to the theater, as in the place they put on plays, not the cinema, where they show movies."

    may @surprised "Oh! Now I get it."

    serena @surprised "I didn't realize this was a point of confusion. I was aware we were going to see a play."

    leaf @talkingmouth "I'll be real, even though this was my plan, I thought {i}Goddess{/i} was a movie."

    red @talkingmouth sweat "Yeah, same here."

    dawn @talkingmouth "Well, that's alright. We can go the cinema instead."

    leaf @happy "No way, girlfriend! You were really excited about this fancy-schmancy play, right? It's your birthday, so we're doing it, come hell or high water!"

    hilda @talkingmouth "Yeah, what Leaf said. Fuck giving up what you want to do just because we aren't cultured enough to understand it."
    hilda @happy "It's your day, Dawn. We're here to hang out as a group again, but we're mostly here for you."

    may @talkingmouth "Who knows! Maybe we'll really end up liking this sort of thing!"

    serena @talkingmouth "And I quite enjoyed the plays I saw in Kalos. It would be fun, I believe, to see what a play borne of Sinnohan culture may be like. As a point of contrast."

    dawn happy "{size=30}...Okay.{/size} Okay! That sounds really fun. Let's, um, let's do it, then!"

    leaf happy "To the theater! {size=30}Which is, apparently, different from a cinema!{/size}"
    leaf sarcastic "{size=30}Serena? Mind telling us what to expect?{/size}"

    call clearscreens() from _call_clearscreens_200
    scene blank2 with splitfade

    pause 1.0

    scene theaterlobby 
    show screen currentdate
    show may:
        xpos 2/6
    show dawn:
        xpos 3/6
    show hilda:
        xpos 4/6
    show serena:
        xpos 1/6
    show leaf:
        xpos 5/6
    with splitfade

    serena @talkingmouth "...So that's what I remember of the musicals I saw performed in Lumiose."
    serena surprised @happy "Ah, but how I am envious of you, Hilda! You must have been able to see musicals in their very birthplace. I imagine our Kalosian imitations pale to the true thing, from Nimbasa."

    hilda @smirkmouth "Get real. Serena, do I look like the kind of person who's {i}ever{/i} been to a musical?"

    serena @surprisedmouth "Oh? But I recall you saying that you've been to Nimbasa before..."

    hilda @closedbrow smirkmouth "Yeah. To see a football game."

    serena @sadbrow talkingmouth "You mean to say you... went to Nimbasa... passed up on the chance to watch a true Nimbasan musical... and saw a sporting event?"

    hilda @happy "Damn right. And I'd do it again!"

    pause 1.0

    hilda @sadbrow smirkmouth "Uh, not that I've got anything against the theater, Dawn. I'm just more of a fan of, you know, stuff with action in it."

    may @talkingmouth "Musicals can have action, too, you know."

    leaf @talkingmouth "Yeah, like, Les Mís. That one's got tons of fighting and action and stuff. You've seen that, right, Serena?"

    serena @happy "You simply haven't enjoyed theater until you've seen it in its original Kalosian! It's--"

    show leaf surprisedbrow frownmouth
    show may surprisedbrow frownmouth
    show hilda surprisedbrow frownmouth
    show dawn surprisedbrow frownmouth
    show serena angrybrow frownmouth
    with dis

    stop music fadeout 1.5

    Character("{color=#665787}???") "\"Rather tiresome and overplayed.\""

    queue music "Audio/Music/League_Start.ogg" noloop
    queue music "Audio/Music/League_Loop.ogg"

    serena @angrymouth "{i}Excusez-moi?{/i}"

    show may:
        xpos 2/6
        ease 0.5 xpos 2/8
    show dawn:
        xpos 3/6
        ease 0.5 xpos 3/8
    show hilda:
        xpos 4/6
        ease 0.5 xpos 4/8
    show serena:
        xpos 1/6
        ease 0.5 xpos 1/8
    show leaf:
        xpos 5/6
        ease 0.5 xpos 5/8
    show mace with dis:
        xpos 1.5
        ease 0.5 xpos 7/8

    redmind @unamusedbrow unamusedmouth "Oh, brother. This guy again."

    show may angrybrow frownmouth:
        xpos 2/8
    show dawn sadbrow sadmouth:
        xpos 3/8
    show hilda angrybrow frownmouth:
        xpos 4/8
    show serena:
        xpos 1/8
    show leaf angrybrow frownmouth:
        xpos 5/8
    with dis

    pause 1.0

    redmind @happy "Hah. 'Oh, brother'. That's a good one."

    mace @closedbrow talkingmouth "I see they truly are letting in anyone nowadays. What an unpleasant surprise to see you here again, [last_name], clogging up one of my few havens of relaxation."
    mace @sadbrow talkingmouth "And, really, Serena? A Kalosian such as yourself? I would have thought you'd have more class than to sully yourself with these... philistines."

    serena @talkingmouth "And I would have thought you'd have the class to keep your bedroom habits out of the public eye, but perhaps we are both destined to be disappointed."

    mace @angrybrow talkingmouth "That {i}incident{/i} was clearly not my, or my step-sister's, fault. Further, our relationship is our own. I would ask you to not make judgments about something you know {i}nothing{/i} about."

    hilda @talkingmouth "Yeah, no, you shitheads brought it onto yourself when you tried to--"

    mace @talkingmouth "Ugh, stop {i}talking{/i} to me. I can smell your {i}odious{/i} breath from over here."

    hilda angry @angrybrow talkingmouth "...The fuck you say?"

    mace @talkingmouth "You heard me, {w=0.5}{i}skank{/i}. The stench of whatever trailer park you rolled out of is stinking up this entire lobby."
    mace @angrybrow happymouth "Of all the people who {i}least{/i} deserve to be in this theater, you are by far the worst offender. Look at what you're {i}wearing.{/i}"
    mace @angrybrow happymouth "I can't even imagine how {i}you{/i} could afford the tickets. I suppose you were able to find a good number of catalytic convertors over the past month?"

    pause 1.0

    narrator "Hilda's fists ball, and for a second, you're worried she's about to lunge at the purple-clad prick."

    if (GetRelationshipRank("Hilda") > 0):
        narrator "You subtly touch Hilda's wrist."

        red @sadbrow talkingmouth "{size=30}Please. Don't.{/size}"

    else:
        narrator "Dawn, very subtly, touches Hilda's wrist."

        dawn @sad "{size=30}Don't, please.{/size}"

    pause 1.0

    hilda @talkingmouth "I'll make you regret those words. Let's battle."

    mace @surprised "What? You couldn't stand a little criticism, so your first recourse is violence?"
    mace @closedbrow talkingmouth "I've better things to do than humor your hurt feelings, but if you insist."
    mace @talkingmouth "Let's go outside, though. We don't want to damage something {i}actually{/i} valuable with our carelessness."

    serena @sadmouth "...The show starts in half an hour."

    hilda @angrybrow talkingmouth "I only need five minutes."

    call clearscreens() from _call_clearscreens_201
    scene blank2 with splitfade

    pause 1.0

    scene theateroutside 
    show hilda angrybrow frownmouth:
        xpos 0.25 xzoom -1
    show mace:
        xpos 0.75 xzoom -1
    show screen currentdate
    with splitfade

    mace @talkingmouth "Send out your Pokémon so that we can get this over with quickly."
    mace @closedbrow talkingmouth "It goes without saying, of course, that the loser will have to forego their spot in the theater."

    hilda @angrybrow talkingmouth "Of course. But I'm not losing to some pretentious stick-up-their-asshole like you."

    mace @closedbrow talkingmouth "So mouthy. Clearly, no-one's ever told you that vulgar women aren't attractive."

    hilda -angrybrow -frownmouth @closedbrow smirkmouth "Attractive?"
    hilda @talkingmouth "Where I come from, beauty is a reflection of one's personality, and the impact they leave on the people around them. Beauty is measured by the hearts you've touched, and how much better the world is for you having lived in it."

    show mace surprisedbrow frownmouth with dis

    mace @talkingmouth "...Eh?"

    redmind @surprised "Where did that come from?"

    hilda @closedbrow talkingmouth "Maybe you're happy to dress up in your fancy clothes and look in your fancy mirror and tell yourself that you've got it made..."
    hilda @talkingmouth "But if no-one else's looking at you, what the hell does it matter?"

    pause 1.0

    hilda @angrybrow talkingmouth "You know what people did when you were pulled from the school?"

    mace @closedbrow talkingmouth "Oh, cheered, probably. I can't imagine what--"

    hilda @smirkmouth "Nothing."

    mace "Hm?"

    hilda @smirkmouth "Nothing, fancy-pants. Literally no-one gave a shit. Don't think anyone missed you, or even noticed you were gone."
    hilda @closedbrow talking2mouth "Beauty's in the eye of the beholder, shithead. There's not a single person in this school who wants to behold you."

    pause 1.0

    hilda @closedbrow talkingmouth "In fact... I don't think I even want to battle you anymore."

    mace angry "What?!"

    if (GetRelationshipRank("Hilda") > 0):
        hilda @talkingmouth "Sorry, I just don't think you could really satisfy me. Besides, I've got a friend who wants to settle something with you."

        hilda @talkingmouth "[first_name], think you could handle this one for me?"

    else:
        hilda @talkingmouth "Sorry, I just don't think you could really satisfy me. Anyone else want to take this guy?"

        red shadow angryeyebrows talking2mouth "Absolutely."

    mace "I will {i}not{/i} battle that undeserving swine in your place! I object to this!"

    red @confused "Swine?"

    hilda @talkingmouth "Then I guess you surrender. Damn, you really {i}are{/i} Kalosian."

    serena @angry "Hilda!"

    mace @talkingmouth "{i}Suce ma bite,{/i} Unovan!"

    hilda @closedbrow smirkmouth "You'd have to find it first. Besides, isn't that your sister's job?"

    mace @talkingmouth "How {i}dare{/i} you! Fine, I'll defeat this Esper freak, {i}then{/i} you as well!"

    redmind @angrybrow shadow frownmouth "...Normally, I enjoy Pokémon battles. I think I'm going to {i}really{/i} enjoy this one."

    python:
        trainer1 = MakeRed()
        trainer2 = Trainer("mace", TrainerType.Enemy, [
            Pokemon(461, level=AimLevel(), gender=Genders.Female, moves=[GetMove("Revenge"), GetMove("Assurance"), GetMove("Feint Attack"), GetMove("Icy Wind")], ability="Inner Focus"),#Weavile
            Pokemon(212, level=AimLevel() + 1, gender=Genders.Female, moves=[GetMove("Bullet Punch"), GetMove("Quick Attack"), GetMove("Metal Claw"), GetMove("Roost")], ability="Technician"),#Scizor
            Pokemon("Sawk", level=AimLevel(), gender=Genders.Male, moves=[GetMove("Karate Chop"), GetMove("Counter"), GetMove("Low Sweep"), GetMove("Double Kick")], ability="Inner Focus"),
            Pokemon(336, level=AimLevel() - 1, gender=Genders.Female, moves=[GetMove("Glare"), GetMove("Poison Tail"), GetMove("Swagger"), GetMove("Bite")], ability="Infiltrator")])#Seviper

    call Battle(trainers=[trainer1, trainer2], customexpressions=["red angrybrow shadow frownmouth", "red angrybrow shadow frownmouth", "mace angry", "mace angry"]) from _call_Battle_155
    $ RecordBattle("MAce1")

    stop music fadeout 1.5
    $ renpy.music.queue("Audio/Music/snowpoint.ogg", channel='music')

    if (WonBattle("MAce1")):
        show hilda angrybrow:
            xpos 0.25
        show mace angry:
            xpos 0.75
        with dis

        $ ValueChange("May", position=-0.5, pausing=False)
        $ ValueChange("Hilda", value=3, position=0.25, pausing=False)
        $ ValueChange("Dawn", position=-0.5, pausing=False)
        $ ValueChange("Leaf", position=-0.5, pausing=False)
        $ ValueChange("Serena", position=-0.5)

        narrator "The girls were impressed!"

    else:
        show hilda angrybrow frownmouth:
            xpos 0.25
        show mace angrybrow happymouth:
            xpos 0.75
        with dis

        mace "So fails your 'great defender!' How embarrassing for you!"

        hilda @closedbrow talkingmouth "Still less embarrassing than exposing you and your sister's secret in front of the whole school."

        mace @talkingmouth "Is that really the only thing you can bring to bear against me? What a tired quip."
        mace @closedbrow talkingmouth "I suppose it's too much to ask for one so lacking in class and intelligence to come up with an original jab."
        mace @talkingmouth "Now, may I defeat you and keep the theater clean of your stench, or do you intend to throw yet another obstacle in my path?"


        hilda sad "{w=0.5}.{w=0.5}.{w=0.5}."

        show dawn with dis

        dawn @talkingmouth "I... want to battle."

        mace @talkingmouth "Noted. I don't care." 
        mace @closedbrow talkingmouth "Move aside."

        dawn @angrybrow sadmouth "I... I {i}want{/i} to battle. I don't like how you've been talking to Hilda, and... and I'm going to... I'm going to..."

        mace @talkingmouth "To stutter? To stammer? To do nothing of consequence?"

        dawn @talkingmouth "I'm... going to..."
        dawn @sad "...You don't have a Garchomp or a Pikachu, do you?"

        mace surprised "What? No. What manner of idiocy is this?"

        dawn @sadbrow talkingmouth "Just making sure. "
        dawn @angry "Just making sure that I'm going to win."

        mace "What?!"

        scene blank2 with splitfadefast

        pause 2.0

        scene theateroutside 
        show screen currentdate
        show may surprisedbrow frownmouth:
            xpos 4/8
        show dawn happybrow:
            xpos 3/8
        show hilda surprisedbrow frownmouth:
            xpos 2/8
        show serena surprisedbrow frownmouth:
            xpos 1/8
        show leaf surprisedbrow frownmouth:
            xpos 5/8
        show mace surprisedbrow frownmouth with dis:
            xpos 7/8
        with splitfade

        dawn @talkingmouth "{size=30}...Carved a path.{/size}"

        hilda @talkingmouth "{i}Damn,{/i} Dawn. That was some serious battling."

        mace angry @talkingmouth "That's... that's inhuman. You're an ogre! Some sort of battling freak!"

    mace @talkingmouth "...This means nothing! Uncultured brutes such as yourself have always held the edge in strength--it doesn't prove your correctness!"

    red @upeyes talking2mouth "Just get out of here. You're embarrassing yourself."

    pause 1.0

    mace "...Peasant! My father will hear of this!"

    hide mace with dis

    pause 2.0

    hilda @talkingmouth "Uh... so... should we go back in, then?"

    dawn @happy "Yeah! The show starts soon, and we don't want to miss our seats!"

    scene blank2 with splitfade

    pause 1.0

    red @talking2mouth "Actually... that purple-haired asshole did raise a good question. How did we pay for this? Do we pay after?"

    leaf @blush sadbrow talkingmouth "Seriously, [first_name]? I paid for you. Like, ten minutes ago."

    red @surprised "Oh! Um, thanks. I guess I didn't notice."

    leaf @happy blush "Dork. You don't have to pretend to not notice if I do something for you. I'm happy to do it."
    leaf @talking2mouth "C'mon. Let's go watch someone struggle through a metaphor for depression for four hours."

    pause 2.0

    redmind @confusedeyebrows frownmouth "But... I really don't remember her buying me the tickets... I don't even remember going to the ticket booth...?"

    pause 1.0

    scene theater with splitfade
    show theaterlightsoff:
        alpha 0.0
        ease 30 alpha 1.0

    may @talkingmouth "...Stage looks a bit empty? Don't they have any props, or scenery? Holes for the pyrotechnics?"

    serena @talkingmouth "You're thinking of contests, May. In theater, the performances of the Pokémon and the actors are meant to stand alone. The audience is expected to {i}imagine{/i} what's happening, guided by the narrator and the music."

    narrator "You reflexively look at Leaf, who purses her lips."

    leaf @closedbrow talking2mouth "Guess I'll just be watching a fat lady singing on a stage for four hours, then..."

    may @talkingmouth "...Not that fat, it looks like."

    dawn @surprised "Hm? Shouldn't the {i}prima donna{/i} be a bit older?"

    red @angryeyes talking2mouth "Wait a moment. Don't I recognize her...?"

    show misty contest with dis

    if (GetRelationshipRank("Misty") > 0):
        red night @happy "Oh, shit! That's Misty!"

        leaf night @sarcastic "Who?"

        red @happy "You know, Misty! She's responsible for three-fourths of the physical injuries I've taken this year."

        may night @sad "Why do you look so happy about that?"

        hilda night @closedbrow smirkmouth "I think I've got an idea."

        serena night @talkingmouth "Ah, {i}un masochiste.{/i} Such a thing is common in Kalos."

    else:
        dawn night @surprised "Oh, wow! That's Misty!"

        leaf night @sarcastic "Who?"

        dawn night @sadbrow talkingmouth "We, um... we have ice classes together. I didn't know she was a singer, though..."
        
    narrator "You take a better look at Misty."

    show misty smilemouth with dis

    narrator "She looks calm, composed, and even seems to be enjoying herself..."

    if (GetRelationshipRank("Misty") > 0):
        narrator "A far cry from the woman who had angrily called you a jerk before storming out of the recreation center."

    else:
        narrator "A far cry from the woman who had slammed into you at full tilt, then blamed you for it, all those weeks ago."

    leaf night @talking2mouth "You'd catch me dead going up a mountain in {i}that{/i} getup."

    serena night @surprisedbrow talkingmouth "Is the expression not 'you would {i}not{/i} catch me dead'?"

    leaf @sarcastic "Normally, but if I was wearing that, I'd freeze to death."

    dawn night @angrybrow angrymouth "It's art! It's a metaphor! It shows how she's vulnerable and exposed!"

    leaf @closedbrow talkingmouth "{size=30}{i}Exposed{/i} is right...{/size}"

    narrator "The orchestra begins to play, as the narrator's voice rings out, deep, firm and unyielding. You could believe it was the snowy mountain itself narrating the scene."

    Character("Narrator") "\"This is it, Priestess.\""
    Character("Narrator") "\"Just Breathe.\""
    Character("Narrator") "\"Why are you so nervous?\""

    show misty closedbrow with dis
    stop music fadeout 1.5

    queue music "Audio/opera.ogg" channel "crowd" noloop

    narrator "Misty does not speak, though a lilting, musical, tune begins to slowly escape her throat. Other characters are introduced, and Misty, as The Priestess, begins her long journey up the mountain."

    pause 1.0 

    Character("Narrator") "\"The mountain is treacherous.\""

    show misty closedbrow angrymouth:
        xpos 0.5 ypos 1.0 rotate 0
        ease 0.5 ypos 1.1 rotate -3

    narrator "On cue, Misty stumbles, her voice jumping an octave higher in a musical imitation of a scream."

    Character("Narrator") "\"The mountain is treacherous. And The Priestess' faith wavers. She recalls her past. The faith her family has placed in her. The burden of pride. The ecstasy of failure. The pain of success.\""

    may night @closedbrow talkingmouth "{size=30}I think he's just mixing together random words now.{/size}"

    hilda night @surprisedbrow smirkmouth "{size=30}What? No way! I'm actually getting this shit! This is seriously good!{/size}"

    Character("Patron") "\"{size=30}Shh, please. It's a great play, I agree, but try to keep your excitement down.{/size}\""

    hilda @sweat closedbrow talkingmouth "{size=30}Shit, my bad.{/size}"

    Character("Narrator") "\"The ice bites into The Priestess' flesh. It hurts like a Houndoom's bite--it demands its toll from her fortitude.\""

    queue music "Audio/opera.ogg" channel "crowd" noloop

    misty @closedbrow talkingmouth "Ah!~♪ Ah~hh~hh~hh!♫♪"

    pause 1.0

    red @sadeyebrows sweat talking2mouth "{size=30}I just realized she's not going to sing, is she?{/size}"

    dawn night @talkingmouth "{size=30}What do you mean? This {i}is{/i} singing.{/size}"

    red @closedbrow talking2mouth "{size=30}Not in Japanese.{/size}"

    dawn @happy "{size=30}No, of course not! It's Altomarese!{/size}"

    red @talking2mouth "{size=30}No, she's, like, she's literally just saying the sound 'Ah' over and over. I'm not saying it's not beautiful! It is! But it's not {i}words.{/i}{/size}"

    dawn @closedbrow sadmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    dawn @sad "{size=30}Well... everyone gets something different from art.{/size}"

    pause 1.0

    redmind @surprisedbrow frownmouth "Did {i}Dawn{/i}, of all people, just give me the cold shoulder?"

    call clearscreens() from _call_clearscreens_202
    scene blank2 with Dissolve(3.0)

    narrator "Eventually, the curtains draw closed and people start filing out of the theater."

    pause 2.0

    $ PlaySound("idea.ogg")

    narrator "Of course, that was only for the intermission. So after {i}another{/i} two hours, the play finally ends. Misty and the other performers take a bow..."

    show misty with dis

    narrator "And you notice that as soon as she stopped singing, her standard surly expression came back to her."

    stop music fadeout 1.5 channel "crowd"
    stop music fadeout 1.5

    redmind sadeyebrows "Couldn't keep it hidden 'til you were offstage, huh?"

    scene theater
    show screen currentdate
    show hilda happybrow:
        xpos 4/6
    show may sadbrow:
        xpos 3/6
    show serena closedbrow:
        xpos 2/6
    show leaf frownmouth flirtbrow:
        xpos 1/6
    show dawn happy:
        xpos 5/6
    with splitfade

    hilda @talkingmouth "That was {i}great!{/i} Man, we gotta come back here again, sometime. Dawn, next time you go, call me, right?"

    dawn "I-- I'd love that! Yes!"

    may @talkingmouth "It was... definitely an experience."

    serena @talkingmouth "Yes... though the full impact will not be felt for a few days yet. You must let the experience matriculate and percolate within your subconscious, like a fine wine."
    serena @happy "You may be astounded now, but the full impact will make this current euphoria pale in comparison."

    may @closedbrow sadmouth "Great."

    leaf @happy "Well, I'm glad that most of us had a good time!"

    redmind -frownmouth -flirtbrow @closedbrow frownmouth "Subtle. I saw her yawning throughout that entire thing."

    leaf @talking2mouth "Of course, the party's not over yet, Dawn! Time to head back to the school!"

    dawn @surprised "Oh? Oh, really? There's more?" 
    dawn happy "I... wow... thank you!"

    call clearscreens() from _call_clearscreens_203
    scene blank2 with splitfade

    show afternoon at vspaz
    $ timeOfDay = "Afternoon"

    pause 3.5

    jump dawnpartyrejoin

label parkgo:
    stop music fadeout 1.5
    
    queue music "Audio/Music/Road to Viridian City.ogg"

    narrator "You decide to go with Bianca's group to the county fair. However, a problem soon makes itself apparent."

    scene colosseum
    show yellow:
        xpos 5/6
    show ethan:
        xpos 4/6
    show cheren:
        xpos 2/6
    show hilbert:
        xpos 1/6 xzoom -1
    show bianca:
        xpos 3/6
    with splitfade

    ethan @talking2mouth "So, yeah, when Leafa said the county fair was 'outside of the city', she didn't mention that it's, like, fifteen miles out."

    hilbert @closedbrow talkingmouth "...How many Cyclizar did you catch for Professor Cherry, [first_name]? Perhaps we could use them again."

    cheren @closedbrow talking2mouth "There's no need for that. I have a car."

    ethan @surprised "What? You've got a car?"

    cheren @talkingmouth "Yes."

    ethan @happy "Huh. Didn't think you were the type, Charity. You're a rulebreaker after all, huh?"

    cheren @confusedeyebrows talking2mouth "I'm clearly misinterpreting something."

    bianca @talkingmouth "Oh, I get it."
    bianca @happy "The driving age in Unova is sixteen!~"

    cheren @surprised "Oh? Is it not sixteen in Johto, as well?"

    yellow @talkingmouth "No, it's eighteen in both Kanto and Johto."

    ethan @closedbrow talking2mouth "Didn't have any time after High School to get my license. Came straight to Kobukan."
    ethan @sadbrow talkingmouth "Kinda a shame, too. I really wanted a car. One of those sporty yellow ones with the open tops and the gold rims."

    hilbert @closedbrow talkingmouth "You might as well shoot a flare into a police station, for as quickly as you'd get pulled over driving that."
    hilbert @talkingmouth "A plain black car with a functioning airbag system and a spacious glove box is all you need."

    bianca @happy "I'd like a pink car! Something round, with a floral pattern, maybe..."

    pause 1.0

    ethan @talkingmouth "Yell'?"

    yellow @surprised "Oh!"
    yellow @closedbrow challengingmouth "I think... I think I'd just like a bike, really..."

    redmind @frownmouth "...This polite conversation is covering the very obvious elephant in the room."
    
    red @talking2mouth "Are you the {i}only one{/i} with a car, Cheren?"

    cheren @talking2mouth "I'm not sure. Bianca does not have one, I know that. Hilbert?"

    hilbert @sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."

    pause 1.0

    hilbert @closedbrow talkingmouth "If I need to go somewhere, I... I ride in Hilda's bike's sidecar."

    ethan @happy "Hah!"

    hilbert @angry "{size=30}Shut up.{/size}"

    ethan @talkingmouth "Well, I already said my piece."

    yellow @closedbrow talking2mouth "And... I don't have a car... {i}or{/i} a license."

    ethan @surprisedbrow talking2mouth "What? But you're nineteen, right? That would have given you a full year to get your license."

    yellow @closedbrow blush talkingmouth "I never really had a reason to need either. Before Kobukan, the furthest I ever went from home was into Viridian Forest, and you can't take a car in there."

    red @closedbrow talking2mouth "Not without irritating a lot of wild Beedrill, anyway."

    redmind @thinking "So it sounds like Cheren is my only option."

    pause 1.0

    narrator "Cheren watches you curiously."

    red @talkingmouth "I obviously don't have a car. Or a license, for that matter. So I guess you're it."

    cheren @sad2eyes talkingmouth "I'm not going to drive us into a ditch."

    red @talking2mouth "I'm sure your driving record is impeccable."

    cheren @sad2eyes talkingmouth "You've no idea."

    red @talking2mouth "Explain, then."

    show cheren surprisedbrow with dis

    pause 1.0

    cheren -surprisedbrow @closedbrow talking2mouth "I have no idea how to continue this repartee. I was stating, quite drily, that my driving record has no blemishes."
    cheren @talkingmouth "I've never even had so much as a parking ticket."

    ethan @talkingmouth "Wow, the head of the disciplinary committee follows rules. Big shocker. More at eleven."

    cheren @sad2eyes talkingmouth "Keep that up and I won't give you shotgun."

    ethan surprised "What?! You can't do that! I called it!"

    yellow @confusedeyebrows talkingmouth "Actually--"

    ethan -surprisedbrow -frownmouth -surprised @happy "I call shotgun!"

    cheren @talkingmouth "I suppose my hands are tied, then." 
    cheren @talking2mouth "Let's go. My car is parked behind Phobos Hall."

    hilbert @talkingmouth "Phobos?"

    cheren @talkingmouth "It's the staff's dorm. Named after an alumnus, and a wealthy donator, supposedly."

    bianca @talkingmouth "You're allowed to park in staff parking?"

    cheren @closedbrow talkingmouth "Besides Instructor Surge's Jeep, I'm not sure if any of the other staff members even have vehicles."
    cheren @talking2mouth "Pokémon are the typical method of locomotion for our school's faculty. Sensibly."

    call clearscreens() from _call_clearscreens_204
    scene blank2 with splitfade

    pause 1.0

    cheren @talkingmouth "Ah, here we go. Let's load up, then."

    scene carbase
    show carback
    show hilbert: 
        xpos 0.45 ypos 0.8
    show bianca:
        xpos 0.65 ypos 0.8
    show yellow neutralhat:
        xpos 0.95 ypos 0.7
    show carfront
    show ethan:
        xpos 0.8 zoom 1.2
    show cheren:
        xzoom -1 xpos 0.4 zoom 1.2
    show carwheel
    with splitfade

    cheren @talkingmouth "There. Everyone comfortable? Seatbelts on."

    red @closedbrow talking2mouth "There's only room for five people in this car."

    ethan @winkbrow talkingmouth "Guess {i}someone's{/i} going to have to sit on my lap, then."

    cheren @talkingmouth "Nonsense. The trunk folds up into another set of three seats. I wouldn't load this car past capacity."

    ethan @closedbrow talking2mouth "{size=30}Damn.{/size}"

    cheren smilemouth @talkingmouth happybrow "Run, Shadowfax. Show us the meaning of haste."

    narrator "Cheren pats the steering wheel affectionately."

    $ PlaySound("Bus_stop.ogg")

    pause 2.0

    hilbert @talkingmouth "You named your car 'Shadowfax?'"

    cheren @talking2mouth "I did."

    pause 1.0

    hilbert @talkingmouth "So why is it white?"

    ethan @surprised "Oh my God, Hillenbrand, you can't just ask someone why their car is white."

    hilbert @talkingmouth "It's a valid question."

    yellow @talkingmouth "It's more of a silvery-gray, I think."

    cheren @talkingmouth "Really? I thought so too."

    hilbert @angry "No, it's {i}white.{/i} It--"

    if (GetRelationshipRank("Hilbert") > 0):
        redmind @upeyes frownmouth "Classic Hilbert. Refusing to see the gray."

    show bianca:
        xpos 0.65 ypos 0.8
        block:
            ease 1.0 ypos 0.85
            ease 1.0 ypos 0.8
            repeat 3

    bianca @happy "So what are we all going to do at the fair?~"

    cheren @sad2eyes talking2mouth "I appreciate the change of topic, but please remember your seatbelt, Bianca."

    bianca @talkingmouth "It's alright! I'm bouncy."

    cheren @talking2mouth closedbrow "Granted, but that doesn't make you exempt from the law."

    yellow @talkingmouth "I think... maybe if they have one of those 'fishing' games... I might try that. I'm pretty good at fishing."
    yellow frownmouth @happy "Well, real fishing, anyway."

    show cheren sad2eyes with dis

    hilbert @closedbrow talking2mouth "Tch. Those games are all rigged, and chance-based, to boot. Skill means nothing."

    bianca frownmouth @happy "I'm going to stuff my face with cotton candy! Did you know cotton candy is actually pretty low in calories, compared to how much of it you eat?"

    ethan @surprised "What? It's pure sugar, right?"

    show cheren sad2eyes angryeyebrows with dis

    hilbert @talkingmouth "A couple teaspoons of sugar could make an entire tub of cotton candy. You're paying for sweetened air."

    ethan frownmouth @unamusedbrow talking2mouth "Well, {i}I'm{/i} planning on riding one of those rollercoasters, which {w=0.5}oh god you're about to say something, aren't you?"

    show cheren sad2eyes angryeyebrows shadow with dis

    hilbert @talkingmouth "You spend $700 for two minutes of excitement and twenty minutes of waiting. It's a waste of time {i}and{/i} money."

    cheren @closedbrow talking2mouth "Thank you, Hilbert. That's quite enough."

    hilbert @closedbrow talkingmouth "We're not on campus. You don't have any power."

    cheren -angryeyebrows -shadow -sad2eyes @confusedeyebrows talkingmouth "And you think I do {i}on-campus{/i}? I thought you were meant to be observant."

    show yellow -frownmouth
    show bianca -frownmouth
    show ethan -frownmouth
    with dis 

    hilbert @closedbrow angrymouth "...Guh."

    ethan @talkingmouth "So are you actually going to {i}do{/i} anything when we get there, or just complain about what we're all doing?"

    hilbert @talkingmouth "I'm going to look at the carnival games."

    ethan @confused "You said those were rigged."

    hilbert @talkingmouth "They are. But I know how they're rigged."

    ethan @closedbrow talking2mouth "Fair enough."
    ethan @talkingmouth "What about you, Cherie? What will you do?"

    cheren @closedbrow talking2mouth "...Hm. I suppose I'll just..."

    narrator "He glances, for a moment, at Bianca, in the rearview mirror. You don't think anyone else saw."

    cheren @talkingmouth "The cotton candy sounds nice."

    ethan @talkingmouth "And what about you, [first_name]?"

    red @talkingmouth "...Hm."

    menu:
        "Probably get some cotton candy.":
            $ ValueChange("Cheren", -1, 0.4, False)
            $ ValueChange("Bianca", 1, 0.65)
            $ AddEvent("Ethan", "CottonCandy")

        "The rollercoasters sound fun.":
            $ ValueChange("Ethan", 1, 0.8)
            $ AddEvent("Ethan", "Rollercoasters")

        "Carnival games, maybe.":
            $ ValueChange("Hilbert", 1, 0.45)
            $ AddEvent("Ethan", "CarnivalGames")

    pause 1.0

    ethan @talkingmouth "...What, nothing from you, Hilbereth?"

    hilbert @talkingmouth "I've already made my thoughts known."

    redmind @closedbrow frownmouth "Boy, has he."

    show hilbert angry
    show cheren sad2eyes smilemouth 
    with dis

    ethan @winkbrow talkingmouth "You sure? If you got killstreak rewards for every mood you've butchered, you'd have an airstrike by now."

    cheren "Hm."

    hilbert @talkingmouth "You're laughing at me again."

    cheren @talking2mouth "I have no intention of stopping."

    pause 1.0

    hilbert closedbrow @sad "...I'm going to sleep. Wake me when we get there."

    pause 5.0
    
    cheren @talkingmouth "We're here."

    yellow @surprised "Hm? Already?"

    ethan @talkingmouth "Sure. It was only fifteen miles from campus, after all."
    ethan closedbrow talking2mouth "Fifteen miles at an average of forty miles an hour is, uh..."

    pause 1.0

    ethan @talking2mouth "Give me a minute."

    pause 1.0

    bianca @happy "It's twen--"

    ethan @happy "Hey, hey, I got this!"

    pause 1.0

    ethan @talkingmouth "Okay, I'm thinking, I'm thinking. Like, it's fractions, right? So if you put the fifteen over the forty, then, that's..."
    ethan @talking2mouth "Wait, no, other way. Forty over fifteen. Then if you simplify that down, you get, uh... eight over three. So eight divided by three is, uh..."

    call clearscreens() from _call_clearscreens_205
    show blank2 with splitfade

    pause 1.0

    narrator "I'll spare you from the rest of that."

    pause 1.0

    scene fairentrance 
    show hilbert surprisedbrow:
        xpos 1/6
    show ethan closedbrow frownmouth:
        xpos 4/6
    show yellow neutralhat sadbrow:
        xpos 5/6
    show cheren sad2eyes shadow:
        xpos 2/6
    show bianca happyeyes:
        xpos 3/6
    with splitfade 

    ethan @talking2mouth "...okay, so, like, my phone calculator says it'll take, uh, one hundred and sixty hours to get here, but I think I might have done the math wrong, somehow."

    bianca @happy "Ooh, he's close! I think he'll get it next time!"

    ethan @happy "Hey, thanks! Uh... let's see... so one-sixty hours is twenty-four hundred minutes, so..."

    redmind @unamusedbrow unamusedmouth "I think I'd prefer to go for another five hundred bottles of beer on the wall than hear one more minute of this..."
    redmind @confusedeyebrows frownmouth "It's not like Hilbert to stay silent about something when someone's wrong. {i}Especially{/i} about math. What's up with him?"

    if (GetRelationshipRank("Hilbert") > 0):
        pause 1.0

        red @talkingmouth "Hey, Hilbie."

        hilbert -surprisedbrow @talkingmouth "Absolutely not."

        red @talkingmouth "Alright. You just seemed a bit out of it."

        hilbert @closedbrow talking2mouth "I was just... nothing. It's nothing."

        redmind @confusedeyebrows frownmouth "I'm not sure I believe that. He was clearly staring at... what was he staring at?"

        redmind @thinking "...I think he was looking at the ferris wheel...?"

    else:
        redmind @thinking "I should probably stay out of his business. Guy's clearly got something serious going on, the way he's staring at that... what's he staring at?"
    
        redmind @thinking "...It looks like he's looking at the ferris wheel...?"

    yellow @talkingmouth "Um, [first_name], do you have enough for tickets?"

    red @surprised "Oh! Uh, I think I... {i}probably{/i} do..."

    ethan @talking2mouth "No need. Loaf gave me a bunch of cash before we split. Said to buy the tickets with that."

    red @talkingmouth closedbrow sweat "...That sounds like Leaf."

    ethan @happy "You make it sound like a bad thing."

    red @sadbrow talking2mouth "I don't want to be dependent on my friends."

    if (GetRelationshipRank("Bianca") > 0):
        bianca @talkingmouth "...You're not."
        bianca @sadbrow talkingmouth "Actually, your friends are probably a bit dependent on you."

        show cheren upeyes with dis

        cheren @talkingmouth "Let's quickly drop that line of thought before you end up becoming a social pariah, too, Bianca."

        ethan @happy "Yeah. Let's get in there!"

    else:
        yellow @talkingmouth "You're not. Everyone needs helps sometimes."
        
        ethan @happy "Yeah. You're cool, man, don't worry about it. Now, let's get in there!"

    scene blank2 with splitfade

    pause 1.0

    scene fair
    show hilbert:
        xpos 1/6
    show ethan:
        xpos 4/6
    show yellow:
        xpos 5/6
    show cheren:
        xpos 2/6
    show bianca:
        xpos 3/6
    with splitfade

    bianca @happy "Wooooow! This is so pretty. Look, there's Argent Mountain in the distance!"

    hilbert @talkingmouth "This is bigger than country fairs I've been to before."
    hilbert @closedbrow talkingmouth "Smaller than Nimbasa's theme parks, though."

    yellow @talkingmouth "They probably have to keep the rides and attractions relatively smaller so they can be brought in on trucks."

    bianca @talkingmouth "Yep! But because we're so close to the city, they can probably make them bigger than the kind of country fairs you'd see in the countryside."

    cheren @talkingmouth "...Similar in size and scope to the Undella Boardwalk."

    ethan @talking2mouth confusedeyebrows "Guys, are we seriously going to come to a country fair with games and stuff and just stand around being impressed by its {i}logistics?{/i}"

    yellow @happy blush "Sorry! I just think it's really inspiring what people can create when they work together."

    cheren @talkingmouth "I concur. The indomitable urge for collaboration is--"

    hilbert @talkingmouth "The only urge that created this place was the urge to profit."

    ethan @unamusedbrow talking2mouth "Oh, great, you're back to normal."

    hilbert @closedbrow talking2mouth "Let's go to the games. I'll show you what I mean."

    show hilbert:
        xpos 1/6
        ease 0.5 xpos -0.3

    ethan @happy "No complaints here!"

    show ethan:
        xpos 4/6
        ease 1.0 xpos -0.3

    pause 1.0

    bianca happy "Wait up!"

    scene blank2 with splitfade

    pause 1.0

    stop music fadeout 1.5

    queue music "audio/music/gamecorner_start.ogg" noloop
    queue music "audio/music/gamecorner_loop.ogg" 

    scene arcade
    show hilbert:
        xpos 1/6
    show ethan:
        xpos 4/6
    show yellow neutralhat:
        xpos 5/6
    show cheren:
        xpos 2/6
    show bianca:
        xpos 3/6
    show screen currentdate
    with splitfade

    red @surprisedbrow talkingmouth "Woah. This place is pretty flashy."

    hilbert @talkingmouth "And as long as you're distracted by the flash, you aren't thinking about how the odds are stacked against you."

    cheren @talkingmouth "You've talked a lot about the odds being stacked against us. Where's the proof?"

    hilbert @closedbrow talkingmouth "Look."

    narrator "Hilbert simply points at the bottom of a claw machine nearby, where there's a stylized 'R' visible."

    hilbert @talkingmouth "This machine was manufactured by 'Rocket Industries.' The user manual is available online. It says that the claw is only strong enough in one of every eighteen plays to actually win anything."

    ethan @confused "What? That can't be right..."

    narrator "Ethan immediately pulls out his phone. Hilbert doesn't wait for Ethan to confirm or deny his assertion, and keeps talking."

    hilbert @talkingmouth "That machine there, the one that tries to get you to make a tower of light blocks. You see it?" 
    hilbert @talkingmouth "Each layer increases in speed, and the last five tiles, the ones that you need to match to win a Pokédex, are moving at a speed that requires a reaction time of 150 milliseconds to hit."

    bianca @talking2mouth "Most people only have a reaction time of two hundred to three hundred milliseconds..."

    hilbert @closedbrow talkingmouth "You need to hit the button exactly a fifth of a second before there's any visual indication you need to hit it, and you need to do that five times in a row."

    ethan @surprised "Wait, hold on, I'm still trying to verify the first thing you said!"

    narrator "Hilbert ignores Ethan and points at another game."

    hilbert @talkingmouth "You see that horizontal ladder? The rungs are a distraction." 
    hilbert @talkingmouth "If you step on the rungs, the entire thing will flip. You need the upper body strength to pull yourself up on the ropes alone, and the coordination to move opposite limbs at the exact same time."

    ethan @angry "Dude!"

    hilbert @talkingmouth "Ring toss. Requires you to minimize horizontal momentum, but the setup of the game makes you think that's the end-all be-all of velocity."
    hilbert @talkingmouth closedbrow "Coin toss. The plates are covered in silicone spray. The coins will just bounce off. Assuming that the carnies don't have an electromagnet underneath the plate."
    hilbert @talkingmouth "Balloon dart toss. The balloons are underinflated. The darts are dull. The best prizes are on the sides of the board."

    pause 1.0

    ethan @happy "Ah-ha!"

    cheren @surprised "What?"

    ethan @talkingmouth "I looked it up."

    pause 1.0

    ethan @talkingmouth "Uh, yeah, Hitcher was right about the claw machines. Turns out the machine just changes the psi every round."
    ethan @talkingmouth "Alright, what was the next thing?"

    yellow @talkingmouth "The light tower."

    ethan @happy "Aw, what? No way, man, those things aren't rigged. I can win them every time, without fail."

    hilbert smilemouth @surprisedbrow happymouth "I don't believe that for a second, but I {i}do{/i} want to see you try."

    ethan @talkingmouth "No sweat, man. How much is this? $300? I got that. Stand aside and let the King of Games do his magic."

    redmind @unamusedbrow unamusedmouth "Cripes. Leaf's gotten to him."

    hide cheren
    hide hilbert
    hide bianca
    hide yellow
    with dis

    narrator "Everyone backs away, watching Ethan with anticipation."
    narrator "You take a quick glance at Bianca."
    narrator "She seems... genuinely enthralled."

    if (GetRelationshipRank("Bianca") > 0):
        redmind @thinking "After that talk we had... I know she's still upset. But maybe she can put her feelings of hurt aside for a while..."
        redmind @sadbrow frownmouth "She's very strong."

    else:
        redmind @thinking "I don't know how she can keep such a smiley face after her father's death. I mean, when my father died..."

        pause 1.0

        redmind @thinking "Hm."

    $ PlaySound("Chime.ogg")

    ethan @talkingmouth "Alright, that's round five. Those are the easy ones. From now to round ten, I have to actually pay attention a little bit. Don't distract me too much!"

    cheren @confusedeyebrows sadmouth "We were not talking."

    ethan @talking2mouth "Dude, seriously, quiet."

    cheren @upeyes shadow "{w=0.5}.{w=0.5}.{w=0.5}."

    narrator "Ethan's hand taps on the button in a steady rhythm, and then, right before the light squares align, he taps harder, freezing the square in place and continuing his game."

    $ PlaySound("Chime.ogg")

    ethan @talkingmouth "Alright! That's round ten complete. I could back out now and we could get a Poké Doll, if anyone's interested in that?"

    yellow neutralhat @happy "Keep going! You've done really well so far."

    ethan angryeyebrows noshine frownmouth @closedbrow talkingmouth "Aight. I gotta lock in now, though."

    narrator "Ethan's posture shifts, and he leans forward, eyeball almost pressed against the glass case. Suddenly, you feel a strange chill run up your spine."

    ethan @talking2mouth "{cps=3}Absolute focus."

    narrator "Ethan begins to chant some strange gamer mantra."

    ethan @talking2mouth "I am the mountain of my dew."
    ethan @talking2mouth "Plastic is my body. Silicone is my blood. I have created..."

    narrator "Ethan presses the button rhythmically. For the first time, he doesn't end up aligning the tower of light blocks {i}exactly{/i}, and the new layers start to lose blocks one by one. He doesn't so much as wince at this."

    redmind @surprisedbrow brown "Is this... is this what Ethan's passionate about?"
    redmind @thinking "He's always seemed so passive before, but this is... it looks like he's taking it {i}really{/i} seriously."

    yellow @surprised "{size=30}He's on the last round with three lives left! He can't possibly lose!{/size}"

    hilbert @surprised "{size=30}This shouldn't be mathematically possible...{/size}"

    show ethan -frownmouth with dis

    narrator "Ethan's mouth curls into a cocky smile."

    narrator "He presses the button..."

    pause 1.0

    narrator "And the final layer pauses right above the light tower, a perfect fit."

    ethan -noshine -angryeyebrows @happy "Yes!"

    show ethan surprisedbrow frownmouth with dis

    narrator "...And then, though it had definitely stopped for at least half a second before, it keeps going, one painful square after another, until the tower is completely misaligned."

    $ PlaySound("Bzzt.ogg")

    ethan noshine sad "What...? C'mon, I..."

    pause 1.0

    ethan -noshine -sad @happy "Oh, well! Guess I messed up at the end there."

    show ethan surprisedbrow frownmouth with dis
    show arcade with vpunch
    show hilbert angry:
        xpos 1/6
    show yellow angry neutralhat:
        xpos 5/6
    show cheren angry:
        xpos 2/6
    show bianca angry:
        xpos 3/6
    
    bianca "Nuh-uh!"
    
    hilbert "You did {i}not!{/i}"

    cheren "That was foul play!"

    yellow "That machine cheated!"

    red @angry "You had that in the bag!"

    pause 1.0

    ethan @happy sweat "Jeez, guys. Don't you think you're going in a bit hard? I just choked, that was all. Skill issue, for real."

    hilbert -angry @talkingmouth "Every single one of us saw you win that game. They must be cheating even harder than I knew."

    cheren -angry @sad2eyes sadmouth shadow noshine "This is an absolute miscarriage of justice."

    yellow -angry frownmouth @talkingmouth "We need to talk to someone about this. I bet they didn't know that the machine was broken."

    hilbert @closedbrow talkingmouth "Naive."

    bianca -angry frownmouth angrybrow @angry "Hilbert's right. Someone absolutely set this up on purpose so you couldn't win."
    bianca @soullesseyes angryeyebrows talking2mouth "We need {i}revenge.{/i}"

    pause 1.0

    ethan "...Scary."
    ethan -surprisedbrow -frownmouth -surprised frownmouth @talkingmouth "I mean, fine, we can wave someone over, I guess, but..."

    Character("{color=#C89BE3}???{/color}") "\"I'm sorry, is there some sort of problem here?\""

    cheren @talkingmouth "Yes. My companion here {i}quite{/i} clearly won... won..."
    cheren surprisedbrow frownmouth @surprised "You."

    show face:
        xpos -0.3
        ease 0.5 xpos 1/8
    show cheren:
        xpos 2/6 xzoom 1
        ease 0.5 xpos 4/8 xzoom -1
    show hilbert:
        xpos 1/6
        ease 0.5 xpos 3/8
    show bianca:
        xpos 3/6
        ease 0.5 xpos 5/8 xzoom -1
    show ethan:
        xpos 4/6
        ease 0.5 xpos 6/8
    show yellow:
        xpos 5/6
        ease 0.5 xpos 7/8

    face @talkingmouth "Hm. Cheren. It's been a while."

    cheren noshine angryeyebrows shadow @talking2mouth "You dare speak as though we are friends?"

    face @closedeyes sadeyebrows talkingmouth "You're so dramatic."

    cheren @talking2mouth "You assaulted an innocent woman. You very nearly ruined the peace and education of an entire year's worth of Kobukan students. I would posit this is an {i}adequate{/i} amount of drama."

    face @winkeyes angryeyebrows talking2mouth "Please. Don't pretend my brother and I were in any way at fault. We only did what you told us to."

    cheren @talking2mouth "'Just following orders' is not an excuse, and I {i}gave{/i} no orders! I asked for your help in learning if [first_name] even {i}had{/i} a power!"
    cheren @angrymouth "I did not think it necessary to state that you not {i}burn down the school{/i} to do so!"

    face @talkingmouth haughtyeyes sadeyebrows "Clearly, we did not burn down the school. {i}He{/i} is still here, and I've heard that witch is, too. Seems you couldn't even do that right."

    cheren @sad2eyes talking2mouth "Firstly, call Sabrina that again, and you will sorely regret it." 
    cheren @closedbrow talking2mouth "Secondly, make no mistake, I want him gone, but keeping you and your brother from Kobukan's grounds is a much higher priority."

    face @happy "Hah! As though my brother and I would ever be caught dead on that ungrateful campus again." 
    face @angryeyebrows angryeyes talkingmouth "The quality of education has declined so fast we're learning more from self-study than the incompetents there could ever manage."

    cheren @confusedeyebrows "{w=0.5}.{w=0.5}.{w=0.5}."
    cheren @talkingmouth "Yes, you're clearly doing quite well for yourself, working a job at a county fair. I suppose your parents cut you off of the family credit card?"
    
    face @angryeyebrows angryeyes talkingmouth "That's... that's none of your business! And for what it's worth, my brother is at the theater right now!"

    cheren @confusedeyebrows talking2mouth "Cleaning popcorn off the floor, I assume."

    face @angry "You smug little worm. You can talk all you want, but we both know you're a complete failure. And for the record, this 'fair' is a prestigious establishment! It's cultural outreach by the Games and Entertainment Bureau of Pasio!"

    cheren @talkingmouth sad2eyes "I don't mean to diminish the noble and necessary work that goes into being a carnie, but being a security guard to an allotment of rigged carnival games doesn't quite give off the impression you tried so hard to project before."
    cheren @closedbrow talkingmouth "Certainly, my failures are tremendous, and half the school goes to sleep every night cursing my name..."

    pause 1.0

    cheren @talkingmouth "But they {i}do{/i} remember it."

    face @surprised "What?"

    cheren @talking2mouth sad2eyes "I have been blamed for everything that happened. There's not a student in this school who does not hold ill feelings towards me. And yet... you, my former partner, have been entirely forgotten."
    
    show face surprisedeyes angryeyebrows with dis
    
    cheren @talking2mouth closedbrow "I envy that. But I suspect that to be forgotten, a meaningless speedbump in the school year's journey, would aggravate you far more than any measure of success you might have had."

    face @angrymouth "I... I don't care at all! You're the fool, then, for taking all the blame!"

    cheren @sad2eyes talking2mouth "Hmph. At least {i}you{/i} never lied, [first_name]."

    red @unamusedbrow talking2mouth "Don't compliment me, Cheren."

    cheren @closedbrow talkingmouth "Mote of praise duly withdrawn."

    cheren @talking2mouth "In any case, we can exchange toothless jabs back and forth for as long as we want, but we {i}do{/i} have a directive."
    cheren @talking2mouth "Ethan absolutely won that last game, the stacking light tower one. The pillar of light stopped entirely flush with the top row before continuing to move a second later."

    face @talkingmouth "Ethan? Which one of you is Ethan?"

    narrator "Ethan raises his hand."

    face @talkingmouth "Hmph. Is what Cheren's saying true?"

    ethan @talkingmouth "I mean, it {i}kinda{/i} looked like I won the game, but maybe I was a bit slow...?"

    red @angrybrow talking2mouth "Ethan!"

    face @happy "Hah! So even this nonsense amounts to nothing. For shame. You really are an incompetent, Cheren."

    cheren @angryeyebrows "{w=0.5}.{w=0.5}.{w=0.5}."
    cheren @talking2mouth "Ethan undersells himself. Everyone here will vouch for his abilities."

    face @closedeyes sadeyebrows happymouth "Well, I'm sorry, but there's just no proof of what you're saying."
    face @winkeyes happymouth "And I {i}know{/i} how much you love your {i}proof{/i}, Cheren."

    cheren @closedbrow talkingmouth "Hm. Actually, there is proof. I was recording the entire thing."

    show face surprisedeyes surprisedeyebrows with dis

    narrator "Cheren points at the tie-clip he always wears."

    cheren @talkingmouth "Surely you didn't think that ostentatious green ornament was purely for decoration? There's a camera concealed in there."
    cheren @closedbrow talkingmouth "So I'm afraid that we have all the proof we need that that game is rigged--as are many of the others here, I'm sure."
    cheren @sad2eyes talking2mouth "Perhaps you should reconsider the position you're in."

    narrator "The Ace Arcade Attendant's eyes flit between Cheren's tie-clip and the security cameras."
    narrator "Her hand slides towards her Poké Ball..."

    cheren @surprised -noshine -shadow "What? Don't be a fool!"

    face @angry "The foolish one here is you, making threats you don't have the power to fulfill. I'll be taking that clip."

    cheren @sad2eyes talking2mouth "I may not have the power, but..."

    red @angrybrow shadow talking2mouth "I'll take her. I've been wanting to settle things with her, anyway."

    cheren @closedbrow talking2mouth "Thank you."

    python:
        trainer1 = MakeRed()
        trainer2 = Trainer("face", TrainerType.Enemy, [
            Pokemon("Gliscor", level=AimLevel(), gender=Genders.Male, moves=[GetMove("Knock Off"), GetMove("Quick Attack"), GetMove("Fury Cutter"), GetMove("Feint Attack")], ability="Poison Heal"),#Gliscor
            Pokemon("Pinsir", level=AimLevel() + 1, gender=Genders.Male, moves=[GetMove("Revenge"), GetMove("Vital Throw"), GetMove("Seismic Toss"), GetMove("Harden")], ability="Hyper Cutter"),#Pinsir
            Pokemon("Throh", level=AimLevel(), gender=Genders.Male, moves=[GetMove("Storm Throw"), GetMove("Revenge"), GetMove("Vital Throw"), GetMove("Seismic Toss")], ability="Inner Focus"),
            Pokemon("Zangoose", level=AimLevel() - 1, gender=Genders.Male, moves=[GetMove("Slash"), GetMove("Hone Claws"), GetMove("Pursuit"), GetMove("Fury Cutter")], ability="Immunity")])#Zangoose

    call Battle(trainers=[trainer1, trainer2], customexpressions=["red angrybrow shadow frownmouth", "red angrybrow shadow frownmouth", "face angry", "face angry"]) from _call_Battle_156
    $ RecordBattle("FAce1")

    queue music "audio/music/gamecorner_start.ogg" noloop
    queue music "audio/music/gamecorner_loop.ogg" 

    if (WonBattle("FAce1")):
        show face angry:
            xpos 1/8
        show cheren confusedeyebrows
        with dis

        $ ValueChange("Hilbert", value=2, position=3/8, pausing=False)
        $ ValueChange("Bianca", value=2, position=5/8, pausing=False)
        $ ValueChange("Ethan", value=2, position=6/8)

        narrator "Hilbert, Bianca, and Ethan were impressed!"

        pause 1.0

        $ ValueChange("Cheren", value=-2, position=4/8)

        narrator "And Cheren just seems confused."

        cheren @talkingmouth "Well done."

        red @unamusedbrow talking2mouth "Cheren. I already said. Don't compliment me."

        cheren -confusedeyebrows @upeyes talking2mouth "Noted, compliment withdrawn."

    else:
        show face happy:
            xpos 1/8
        with dis

        face @talkingmouth "Hah! That's the difference between a lowborn hick such as yourself, and an elite trainer, graduate of Anistar City School for the Gifted!"

        hilbert @talkingmouth "...Alright. My turn."

        face -happy @surprised "Wh-what?"

        hilbert @talkingmouth "You beat my Battle Teammate. Great. But it's a Battle {i}Team.{/i} You don't win unless you beat Ethan and I, too."

        ethan @happy "Aw, you softie."

        hilbert @closedbrow talkingmouth "I'm only trying to preserve the Battle Team's dignity." 

        face @angry "That's... that's cheating! I never agreed to this."

        cheren @sad2eyes talkingmouth "It is unlikely you would agree to be in a situation you could not possibly win in, but I've managed fairly well..."

    cheren @talkingmouth "In any case, you, my old partner, once again demonstrate the lack of thought or preparation you put into your so-called 'plans.'"
    cheren @talking2mouth "Truly, it is a baffling intellect that looks at a party consisting of {i}three{/i} Battle Team members and thinks it could take them."

    face @talkingmouth "...Urgh! You brute! Your strength proves nothing except that you're willing to throw your weight around to get what you want!"
    face @angry "And you don't even have the decency to throw around your own weight! Relying on assists... you'll never succeed like that!"

    cheren @talking2mouth closedbrow "No, I suppose not."
    cheren @talkingmouth sad2eyes shadow "But I can be {i}very{/i} annoying before my final failure."

    pause 1.0

    cheren @talking2mouth "Ethan, I'm afraid I must apologize for something. I do not actually have any proof that that machine is rigged." 

    show bianca surprisedbrow frownmouth with dis

    cheren @talkingmouth "My tie-clip is just a simple piece of plastic and metal. I bought it at the student store my first day at Kobukan, because the gem reminded me of Bianca's eyes."

    show bianca -surprisedbrow -frownmouth with dis

    ethan @surprised "Huh? Oh, no, man, it's, uh..."

    narrator "Ethan catches your eye."

    ethan @talking2mouth "It's whatever."

    face -angry @surprisedeyebrows talkingmouth "So... so there's no proof. Nothing you can pin on the arcade?"
    face @closedeyes talking2mouth "Fool. Wasting my time with your pathetic lies."
    face @talkingmouth "Get out of here."

    cheren @sad2eyes talkingmouth "I'm all too happy to."

    bianca @talkingmouth "Um. Mind if I say something?"

    face @talkingmouth "Hm? Aren't you that little blonde twerp who helped Cheren with his pathetic campaign? And now you're with [first_name]... seems you can't stay away from losing causes."

    show hilbert:
        xpos 3/8
        ease 0.5 xpos 4/8

    show cheren with dis:
        xpos 4/8
        ease 0.5 xpos 5/8

    show bianca:
        xpos 5/8
        ease 0.5 xpos 3/8

    bianca @talkingmouth "It's just... um... well, you've been saying a lot of mean stuff to my friends."

    face @surprised "What? I've been 'saying mean stuff'? What are you...? Am I speaking to a toddler?"

    bianca @talking2mouth "So I really think you should apologize. To [first_name], to Ethan, and to Cheren, too."

    face @surprised "{w=0.5}.{w=0.5}.{w=0.5}."
    face @talkingmouth "You're kidding me."

    bianca @closedbrow talking2mouth "No, I'm actually pretty serious."

    face @angrymouth "I don't owe {i}anyone{/i} an apology. If anything, Cheren should apologize to {i}me{/i} for what he put my brother and I through! We worked tirelessly on {i}his{/i} plan, and the moment we step outside of his box, he turns on us!"

    bianca @talkingmouth "...Everyone deserves respect."

    face @closedeyes sadeyebrows talkingmouth "Respect? Hah! Respect is earned, not given freely to those who don't deserve it."

    bianca frownmouth @sadeyes talking2mouth "Why do you get to decide who deserves respect?"

    face @talkingmouth "Because I am {i}superior.{/i} To you, to that incompetent, to that nepotee. To everyone who continues to flail in that sinking ship of an academy."
    face @angryeyebrows angryeyes happymouth "The waves are coming, Bianca. And I know enough to know that {i}none{/i} of you can swim."

    bianca @closedbrow talking2mouth "From a psychologic perspective, I think maybe you--"

    face @angry "Enough! I'm done listening to this nonsense. You can drown in your self-righteousness, for all I care."

    bianca @talkingmouth "Kindness costs nothing."

    show ethan angrybrow
    show yellow angrybrow
    show cheren angrybrow 
    show bianca soullesseyes
    show hilbert angrybrow
    with dis

    face @angryeyebrows angryeyes talkingmouth "To be kind to you would cost my dignity. I give you nothing. I shall have nothing to do with you, that incompetent schemer, that country hick, or that freak of a {w=0.5}{i}witch.{/i}"
    
    cheren @angry "I told you not to call her that!"

    face @angryeyebrows angryeyes happymouth "You have even less power over me now than you did before."
    
    face @angryeyebrows angryeyes talkingmouth "Simply stay out of my way."

    stop music fadeout 3.0

    pause 1.0

    bianca @closedbrow talking2mouth "I don't think I will."

    face @angryeyebrows angryeyes talkingmouth "What on earth are you trying to imply by {i}that{/i}?!"

    bianca @talking2mouth "Let's just say, if you keep disrespecting people, you might find yourself in a situation you can't handle."

    pause 1.0

    face surprised "Are you threatening me?"

    pause 1.0

    show ethan surprisedbrow frownmouth
    show yellow surprisedbrow frownmouth
    show cheren sad2eyes sadeyebrows 
    show face surprisedbrow frownmouth
    with dis

    bianca @soullesseyes angryeyebrows talking2mouth "I've already killed one person this week."

    face @talkingmouth "T-t-that's... that's ridiculous. You lie."

    show screen songsplash("An Unwavering Heart", "Zame/Pokestir")
    queue music "audio/music/unwaveringheart.ogg"

    show ethan -surprisedbrow frownmouth
    show yellow -surprisedbrow frownmouth
    show cheren -sad2eyes sadeyebrows 
    show face surprisedbrow frownmouth
    with dis

    if (GetRelationshipRank("Bianca")):
        show bianca surprisedbrow frownmouth with dis

        narrator "You put a hand on Bianca's shoulder. She jolts a bit, surprised."

        show bianca sadeyebrows -frownmouth with dis

        red @talking2mouth "C'mon. She's not worth it. Let's go get you some cotton candy."

    else:
        show bianca surprisedbrow frownmouth with dis

        narrator "Cheren puts a hand on Bianca's shoulder. She jolts a bit, surprised."

        show bianca sadeyebrows -frownmouth with dis

        cheren @talking2mouth "Thank you. Truly. But this forgettable creature is not worth your time." 
        cheren -shadow @talkingmouth happybrow "Come. You wanted some cotton candy, right?"

    face angry "You... you threatened me! This is... my mother will hear of this, you {i}peasants!{/i}"

    hide face with dis

    pause 2.0

    cheren @sad2eyes talking2mouth "...Hopefully, that's the last we see of her or her odious brother, but I'm not hopeful."

    ethan @closedbrow talking2mouth "Those two are like the world's most annoying boomerang."

    yellow @sadeyebrows happymouth "Let's just try to put them out of mind. There's plenty of other fun stuff to do here."

    hilbert @closedbrow talkingmouth "You go ahead. I want a moment."

    bianca @confusedeyebrows talkingmouth "You're not going to start something, are you?"

    hilbert @happymouth "{i}You're{/i} asking that?"
    hilbert @talkingmouth "...Anyway, no. Actually, I just wanted to talk to you."

    bianca @talkingmouth "Oh, sure."

    pause 1.0

    show ethan surprisedbrow frownmouth
    show yellow surprisedbrow frownmouth
    show cheren surprisedbrow
    with dis

    hilbert @talkingmouth "Everyone else can go."

    ethan @talking2mouth "Oh. Uh, okay, sure."

    hide ethan
    hide yellow 
    hide cheren
    with dis

    show bianca:
        xpos 3/8
        ease 0.5 xpos 0.33

    show hilbert:
        xpos 4/8
        ease 0.5 xpos 0.66 xzoom -1

    pause 2.0

    bianca surprisedbrow frownmouth @talkingmouth "So, what was it?"

    show hilbert:
        xpos 0.66 xzoom -1
        ease 0.5 xzoom 1

    hilbert @closedbrow talkingmouth "It's not your fault. Don't ever say you killed him. Don't {i}ever{/i} say that."
    hilbert @sadbrow talkingmouth "Because... the moment you say it, even if you're just threatening someone..."

    show bianca sadbrow talking2mouth with dis

    hilbert @closedbrow talkingmouth "...You start believing it. It becomes 'truth'. And it doesn't matter if it's not true, you'll keep believing it. You can't stop. And truth starts to mean nothing to you but pain."
    hilbert @talkingmouth "You don't deserve that. Don't do that to yourself. And if someone reaches out... grab their hand. Grab and hold on tight. Hold on like you're holding onto your own life."

    pause 1.0

    bianca sadeyebrows talking2mouth "Hilbie..."

    pause 1.0

    hilbert @talkingmouth "That's all. I'm going now."

    hide hilbert with dis

    show bianca closedbrow cry with dis

    pause 2.0

    scene blank2 with splitfade

    pause 1.0

    narrator "Though it takes some time, the mood eventually returns to normal, and the group makes small talk as they chow down on their cotton candy."

    stop music fadeout 1.5
    queue music "Audio/Music/Road to Viridian City.ogg" fadein 1.5

    ethan @talkingmouth "Oh my {w=0.5}{i}(chew){/i} God, cavities never tasted so good."

    hilbert @talkingmouth "Less sugar {w=0.5}{i}(chew){/i} than a soda."

    yellow neutralhat @talkingmouth "That's not saying {w=0.5}{i}(chew){/i} much. If soda wasn't so delicious, it would be considered abuse to give it to your child."

    bianca @happy "That's a bit {w=0.5}{i}(chew){/i} of an exaggeration! But you really shouldn't have too much of it."

    red @closedbrow talking2mouth "Noted. Not that I {w=0.5}{i}(chew){/i} do, anyway. Though sometimes I'd gather up my neighbor's cans, for the $0.1 refund."

    ethan @closedbrow talking2mouth "Eesh. Sounds {w=0.5}{i}(chew){/i} rough."

    red @happy "Nah. I was running around Pallet anyway. Eventually, people just put their {w=0.5}{i}(chew){/i} cans in boxes on their porches, and I became, like, a voluntary garbage man."
    red @happy "[pika_name] joined me. He usually just rode on my head, though. Lil' guy's really slimmed down, huh?"

    $ PlaySound("Pokemon/pikachu_happy1.ogg")
    libpikachu @blush happy "Pika-{w=0.5}{i}(chew){/i}!"

    ethan @closedbrow talkingmouth "Heh."

    scene fairferriswheel with splitfade

    show bianca:
        xpos -0.5
        ease 0.5 xpos 4/6

    bianca @happy "I want to go on the Ferris wheel!"

    show cheren:
        xpos -0.5 
        ease 0.5 xpos 2/6

    cheren @talkingmouth "Of course. Go right ahead."

    show ethan:
        xpos -0.5
        ease 0.5 xpos 3/6

    ethan @talkingmouth "Looks like the cabins only hold four people. How should we split it? Unovans in one cabin, Dorm 25 in another?"

    show yellow:
        xpos 1.5
        ease 0.5 xpos 5/6

    yellow @talkingmouth "Might as well."

    show hilbert:
        xpos -0.5 xzoom -1
        ease 0.5 xpos 1/6

    if (GetRelationshipRank("Hilbert") > 0):
        $ AddEvent("Hilbert", "FerrisWheel")
        hilbert @talkingmouth "Alternate proposal. [first_name] and I take one cabin. Everyone else takes another."

        ethan @winkbrow talkingmouth "Oh? Looking for a bit of privacy?"

        hilbert @talkingmouth "Yes."

        ethan @surprisedbrow talking2mouth lightblush "Oh. Fair enough!"

        hilbert @talkingmouth "Do you have any objections, [first_name]?"

        red @happy "Aw. You're even asking my opinion? I didn't realize we were so close."

        hilbert @angry "If you fall out of the cabin when we're alone, I can claim it was an accident."

        red @sweat talking2mouth "Gotcha."

        scene blank2 with splitfade

        narrator "You board the Ferris wheel with Hilbert."

        scene ferrisinside 
        show hilbert
        with Dissolve(2.0)

        stop music fadeout 1.5

        show screen songsplash("An Unwavering Heart", "Zame/Pokestir")
        queue music "audio/music/unwaveringheart.ogg"

        narrator "Hilbert is staring directly at you. Given the tight quarters, you don't have much choice but to stare back at him, too."

        red @happy "So. What'd you ask me into the cabin for?"
        red @sadeyebrows talkingmouth "Scared of heights?"

        hilbert @talkingmouth "...I've been on a Ferris wheel before."

        pause 1.0

        hilbert @talkingmouth "Once."

        pause 0.5

        hilbert @talkingmouth "Aurea took me to an amusement park in Nimbasa."

        red @talking2mouth "Aurea. I remember her. She's your guardian, right?"

        narrator "Hilbert nods in acknowledgement."

        hilbert @talkingmouth "It was a couple months after my parents were murdered."

        red @surprisedbrow frownmouth "...Oh."

        hilbert @closedbrow talkingmouth "She thought it would cheer me up. I... my heart... it was frozen solid." 
        hilbert @sadbrow talkingmouth "When they were killed, I couldn't feel. I couldn't think. I could barely breathe."
        hilbert @sadbrow talkingmouth "So she took me to an amusement park. {i}To cheer up.{/i}"

        red @sad "I'm sure she was doing the best she could..."

        hilbert @closedbrow talkingmouth "I'm not criticizing her."

        pause 1.0

        hilbert @sadbrow talkingmouth "It was late in the evening. I saw the orange sun streaming over the top of the Nimbasa musical theater."
        hilbert @sadbrow talkingmouth "And that sun... melted my heart."

        pause 0.5

        hilbert @closedbrow talkingmouth "It was the first time I felt the pain of my loss. I wept. A breakthrough... though not a pleasant memory." 
        
        red @sad "That's when you decided you needed to kill?"
        
        hilbert @sadbrow talkingmouth "That was when death gripped me, and when I knew that another's death was all there was left to live for."

        pause 1.0

        narrator "Hilbert looks out the window and heaves a great sigh."

        if (GetRelationshipRank("Hilbert") < 2):
            hilbert @talkingmouth "...[first_name], there is something I must confess to you."

            pause 1.0

            hilbert @talkingmouth "I am the king of Team Plasma."

            pause 3.0

            red @surprised "What?"

            hilbert surprised @closedbrow talkingmouth "You're probably surprised. It's because--"

            red @talkingmouth sweat "N-no, I just, uh, [pika_name] was chewing on my ear. What did you just say?"

            hilbert -surprisedbrow -frownmouth -surprised @surprised "Oh."
            hilbert @closedbrow talking2mouth "I said 'I am going to kill the king of Team Plasma.'"

            red @unamusedbrow unamusedmouth "...Okay, I guess I didn't mishear you this time."

            hilbert @talkingmouth "As I was saying. You're probably surprised. It's because the king of Team Plasma is responsible for my parents' deaths."

            red @talkingmouth "I thought you said... it was the dragon of the meteor?"

            hilbert @closedbrow talkingmouth "Every king needs a sword. As I said, the dragon will fall, then the king will die."

            $ PlaySound("Pokemon/pikachu_happy3.ogg")
            libpikachu @happy "Pi-i-i-ka!"

            red @sweat talking2mouth "{size=30}Not the time, bud.{/size}"

            pause 1.0

            if (GetRelationshipRank("Hilbert") < 2 and GetRelationshipRank("Hilda") < 2):
                red @confused "What's Team Plasma?"

                hilbert @talkingmouth "My enemy. That's all you need to know."

            red @sadbrow talking2mouth "Well... I'm glad you're telling me this. But {i}why{/i} are you telling me this?"

            hilbert @talkingmouth "You insisted on being part of my mission. I believe the second part is coming up... very soon."

            redmind @sadbrow frownmouth "Shit. I thought I had more time to talk him out of this."

            hilbert @sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."
            hilbert @talkingmouth "I will continue to appreciate your support."

        else:
            hilbert sadbrow @talkingmouth "I appreciate you being... {w=0.5}here."

        narrator "Hilbert looks out the window and doesn't say a word for the rest of the ride."

        stop music fadeout 1.5
        queue music "Audio/Music/Road to Viridian City.ogg" fadein 1.5
        
        call clearscreens() from _call_clearscreens_206
        scene blank2 with splitfade

    else:
        hilbert @talkingmouth "I'll pass. I don't much care for Ferris wheels."

        ethan @talking2mouth "Oh, yeah? Well, I guess I'll stay down here on the ground with you, then."
        ethan @happy "I'm not crazy about heights myself."

        hilbert @closedbrow talkingmouth "You can go. Don't have less fun on my account."

        ethan @unamusedbrow talking2mouth "You spent the entire drive here trying to convince us that all our fair ideas were terrible."

        hilbert @sadbrow talkingmouth "...Whatever."

        ethan @happy "Besides, we should catch up more. Talk about Dorm 151. Heh, remember when [first_name] was going to call you 'Edgelord' for the year?"

        hilbert @angry "On second thought, maybe we {i}should{/i} go on the Ferris wheel. Alone. And if you happen to fall out of the cabin..."

        ethan @sad2eyes talking2mouth "...Right."

        call clearscreens() from _call_clearscreens_207
        scene blank2 with splitfade

        narrator "After boarding the Ferris wheel, you and Cheren stare at each other from opposite sides of the cabin for ten minutes as Bianca and Yellow chat cheerfully."

        if (profanity):
            menu:
                ">Shrug":
                    narrator "Cheren nods."
                ">Nod":
                    narrator "Cheren shrugs."
                ">Continue staring":
                    narrator "There have been more awkward moments in your life, but you struggle to think of them."
                ">Jump out the damn window":
                    narrator "You manage to fight back against the intrusive thoughts. Not today."

        else:
            menu:
                ">Shrug":
                    narrator "Cheren nods."
                ">Nod":
                    narrator "Cheren shrugs."
                ">Continue staring":
                    narrator "There have been more awkward moments in your life, but you struggle to think of them."
                ">Jump out the **** window":
                    narrator "You manage to fight back against the intrusive thoughts. Not today."

        narrator "Eventually, mercifully, the ride comes to an end, and you rejoin with Hilbert and Ethan, who are arguing about something in some sort of video game."

    show afternoon at vspaz
    $ timeOfDay = "Afternoon"

    pause 3.5

    scene blank2 
    show screen currentdate
    with splitfade

label dawnpartyrejoin:

narrator "You and your companions rejoin with the other group and make your way back to the campus ground."

red @sadeyebrows talking2mouth "Alright. Let's see the damage."

leaf @angrybrow angrymouth "And what exactly are you implying by that?"

red @sadbrow talkingmouth "I'm just having difficulty imagining you toning it down a notch."

leaf @closedbrow talkingmouth "Well, prepare to be pleasantly surprised."

scene birthday 
show screen currentdate
with splitfade

narrator "You are."
narrator "You walk into a modestly-decorated classroom, where simple school desks have been covered with tablecloths, and a moderate amount of streamers and balloons cover the ceiling."

red @happy "Hey! Good job, Leaf. I seriously thought there was going to be, like, a fog machine, a disco ball, and a DJ set up here."
red @talkingmouth "But this is really nice. It's not overwhelming, it's comforting."

redmind @happy "And not a single Pokémon-themed decoration in sight. {i}That{/i} can't have been easy. She was really thinking about Dawn, here."

show leaf blush with dis:
    xpos 0.33

leaf @talkingmouth "Hardest part was just transferring all the stuff from the Battle Hall here in time."
leaf @sarcastic "Dean Drayden helped, though, so I guess he's been spared from my wrath for now."

red @closedbrow talking2mouth "Thank goodness."

show dawn with dis:
    xpos 0.66

dawn @talkingmouth "Leaf, thank you so much. This is fantastic. The decorations, and the room, and the theater..."
dawn @happy "This is the best birthday I've ever had."

leaf @closedbrow talkingmouth "Then we need to raise your standards a bit."
leaf @sadbrow talkingmouth "But I'm glad."

dawn @talkingmouth "Um... what else do you do on birthdays?"

show may with dis:
    xpos 0.15

may @happy "We give you presents, of course!"

show yellow with dis:
    xpos 0.85 

yellow @happy "Here, Dawn! Your hands are always bright pink after you leave Instructor Melony's classroom, so I knitted you some mittens."

if (GetRelationshipRank("Dawn") > 0):
    redmind @thinking "Oh, right. Carving ice sculptures must be a cold process. I should've thought of that..."

dawn @happy "Oh, thank you! {i}You{/i} knitted these?"

yellow @happy "Yep. Johtonian wool. If you rub them together fast enough, they spark."

dawn @sadbrow talkingmouth "That's so thoughtful..."

may @happy "My turn, my turn!"
may @happy "I wanted to get my new Coordinator Clubmate a gift that could help in contests!"
may @sadbrow talkingmouth "I'm sorry it's not something handmade, but I didn't have enough time..."

narrator "May hands Dawn a sky-blue box."

may @talkingmouth "It's a makeup set! Pokémon-safe, too, so you can use it on both you and your Pokémon."

dawn @happy "Oh! I heard that they were making these in Hoenn... I didn't know that--"

show dawn surprisedbrow with dis

narrator "Dawn turns the box upside-down, revealing a man's very-identifiable figure on the bottom. The man is nude, sitting on the floor, covered only by a wisp of aqua silk stretched strategically over his well-toned body."
narrator "His expression can only be described as one that screams 'come hither.'"

if (HasEvent("Instructor Wallace", 1)):
    redmind @unamusedbrow unamusedmouth "Hello again, Instructor Wallace."

may @sadbrow talkingmouth "Um... yeah... it's part of Instructor Wallace's personal brand. If you ignore the packaging, they're really great!"

show hilda behind leaf with dis:
    xpos 0.45

hilda @happybrow talking2mouth "Don't know about you, but I'm not ignoring that box. In fact, if you don't want the packaging, I'll take it off your hands."

show hilbert behind hilda with dis:
    xpos 0.55

hilbert @sadbrow talkingmouth "Hilda, you're embarrassing us."

hilda @talking2mouth "Us who? {i}I'm{/i} not embarrassed."

hilbert @closedbrow talkingmouth "Whatever."
hilbert @talkingmouth "Here's my gift. It's a Choice Specs."

dawn @surprised "Wh-wh-what?! Really?"

hilbert @talkingmouth "In your battle with [first_name], I saw you seemed to like using the same move repeatedly. Dragon Pulse."

dawn sadbrow @talkingmouth "Oh."

redmind @happy "That might have been more due to a general lack of strategy in her battling than any particular preference... but it's still a nice thought."

hilbert @closedbrow talkingmouth "If you try that again, your moves will be more powerful with this."
hilbert @sadbrow talkingmouth "And if you don't like it, one of my classmates, Gardenia, will buy it off of you. Orange hair, wears green. Can't miss her."

hide hilbert with dis

hilda @closedbrow talkingmouth "...Sorry about him."

dawn @happy "No, no, it's fine! I loved this gift. {size=40}Thank you, Hilbert!{/size}"

hilbert @closedbrow talking2mouth "Mm."

hilda @talkingmouth "Anyway, my gift isn't as fancy as his, but I hope you still like it."

show dawn surprisedbrow frownmouth:
    xpos 0.66
    linear 0.3 xpos 0.72 ypos 1.03 rotate 3

narrator "Hilda casually tosses Dawn a white box with a smiling Vanilite on the cover. Dawn stumbles a bit to catch it."

show dawn -surprisedbrow -frownmouth with dis:
    xpos 0.72 ypos 1.03 rotate 3
    ease 0.5 xpos 0.66 ypos 1.0 rotate 0

hilda @talkingmouth "Hilbert said that you liked ice cream, so I got you this. It, uh, it's one of those make-your-own Casteliacone kits."
hilda @sadbrow talking2mouth "Sorry it's not handmade on my end, either. {size=30}We shouldn't've let Yellow go first...{/size}"

dawn @happy "Oh, that's fantastic! I always wanted one of these when I was a kid."

show hilda surprisedbrow frownmouth
show may sadbrow frownmouth
show leaf sadbrow frownmouth
show yellow sadbrow frownmouth 
with dis

dawn @sadbrow talkingmouth "My mother said I couldn't have one, though, because then I'd eat nothing but ice cream, and I'd get fat..."

pause 1.0

show ethan behind dawn with dis:
    xpos 0.55

ethan @happy "Okay, Ethan time! I've got a--"

scene blank2 with splitfadefast

narrator "With Ethan's quick thinking, you manage to steer the conversation away from the subject of Dawn's tragic childhood."

pause 1.0

narrator "Though Leaf, Ethan, and Yellow {i}do{/i} have to do it one more time each before all the presents are handed out. During this time, you quickly slip away to the cooking clubroom to grab the cake you have stored there."

mallow @happy "Alola! Are you here to--"

red @happy "Sorry, just grabbing this cake and making my way back to the party. No time to chat. Seeya!"

mallow @surprised "A-ah..."

pause 1.0

mallow @angrybrow poutmouth "Hmph. {i}Haole.{/i}"

scene birthday 
show dawn happy
with Dissolve(2.0)

dawn @talkingmouth "This is so fantastic... thank you! Thank you so much, everyone!"

leaf @happy "The party's not over yet, though! [first_name], why don't you show Dawn what you've got?"

narrator "As you round the corner with the cake, candles lit, Leaf takes a deep breath, and everyone attending the birthday party immediately knows what that means."

stop music fadeout 1.5

show cheren happy:
    xpos 1/11
show hilbert happy behind cheren:
    xpos 2/11 xzoom -1
show bianca happy:
    xpos 3/11
show serena happy behind bianca:
    xpos 4/11
show may happy behind dawn:
    xpos 5/11
show hilda happy behind dawn:
    xpos 7/11 xzoom -1
show dawn surprisedbrow frownmouth:
    xpos 6/11
show leaf happy behind dawn:
    xpos 8/11
show ethan happy:
    xpos 9/11
show yellow happy neutralhat:
    xpos 10/11
with vpunch

stop music fadeout 1.5 channel "crowd"

queue music "Audio/birthday.ogg" channel "crowd" noloop

pause 0.3

Character("Everyone") "{cps=11}\"{size=50}Happy Birthday to you! ♪ {w=0.5}Happy Birthday to you! ♪ {w=0.5}Haaaaappy Birthday, dear Daaaawn!~ ♪ {w=0.5}Happy Birthday to you!\""

show dawn closedbrow -frownmouth with dis

narrator "Dawn blows out the candles and closes her eyes tightly, making a wish."

pause 1.0

show dawn -closedbrow with dis

dawn @happymouth "Thank you. Thank you so much. I, um... I don't know what to say, but..."
dawn @surprisedbrow sadmouth "Wait."
dawn @closedbrow talkingmouth "Um... the candles on that cake..."

red @happy "Yeah, sorry. I'm more a fan of cakes that have individual candles, but the cooking club only had the numbered kind."

dawn @happy "Oh, that's not the issue. Um... it's just that they say '19.'"

red @sadbrow talkingmouth "Well, yeah."

dawn @sadbrow talkingmouth "I... just turned {w=0.5}{i}eighteen.{/i}"

red @surprisedbrow talking2mouth "Oh. Huh, okay."

pause 1.0

red @happy "I mean, I can run back and get some new candles, but I'd, personally, just want to eat it, right?"

dawn @sadbrow talkingmouth "I... I guess."

pause 0.5

redmind @thonk "What's the issue? She seems more bothered by that than I'd expect."

if (GetRelationshipRank("Dawn") > 0):
    dawn @sadbrow talking2mouth "It's just... I still look young, right? I'm not, um, I'm not 'aging' yet, am I? I mean, to you?"

    red @happy "Dawn. I thought you had to be nineteen because you fought the strongest woman in the world. Nothing more than that."

    pause 1.0

    red @talkingmouth "Wait, when {i}did{/i} you fight Cynthia, then?"

else:
    ethan @confused "Wait, then, how old were you when you fought Cynthia?"

dawn @talkingmouth "I was sixteen."

red @surprisedbrow talking2mouth "Holy {i}shit!{/i} Dawn, slow down! Who said you had to speedrun life?"

show cheren sadbrow:
    xpos 1/11
show hilbert sad behind cheren:
    xpos 2/11 xzoom -1
show bianca sadbrow frownmouth:
    xpos 3/11
show serena sadbrow frownmouth behind bianca:
    xpos 4/11
show may sadbrow frownmouth behind serena:
    xpos 5/11
show hilda sad:
    xpos 7/11 xzoom -1
show leaf sadbrow frownmouth behind dawn:
    xpos 8/11
show ethan sad2eyes frownmouth:
    xpos 9/11
show yellow sadbrow frownmouth neutralhat:
    xpos 10/11
with dis

dawn sadbrow sadmouth "My mom."

pause 1.0

redmind @closedbrow frownmouth sweat "...Dawn, we're seriously trying here. You gotta stop shooting holes in the mood like that."

pause 1.0

show cheren happy:
    xpos 1/11
show hilbert happy behind cheren:
    xpos 2/11 xzoom -1
show bianca happy:
    xpos 3/11
show serena happy behind bianca:
    xpos 4/11
show may happy behind serena:
    xpos 5/11
show hilda happy:
    xpos 7/11 xzoom -1
show dawn sadbrow -sadmouth:
    xpos 6/11
show leaf happy behind dawn:
    xpos 8/11
show yellow happy neutralhat:
    xpos 10/11
with dis

ethan happy "Alright, who wants cake?! Let's get the ceremonial birthday knife and start slicing!"

call clearscreens() from _call_clearscreens_208
scene blank2 with Dissolve(5.0)

narrator "Slowly, the party unwinds... and the day ends."

show night at vspaz
$ timeOfDay = "Night"

pause 3.5

narrator "Everyone goes to bed contented, this day, looking forward to what the future might hold." 
narrator "So contented you are, you go to bed early, and don't even notice when Blue eventually comes back, long after curfew."

scene suitenight 
show yellow:
    xpos 0.66
show ethan:
    xpos 0.33
with splitfade

stop music fadeout 1.5

$ renpy.music.queue("audio/music/Eterna_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
$ renpy.music.queue("audio/music/Eterna_Loop.ogg", channel='music', loop=True)

yellow @talkingmouth "...Ethan, earlier this week, when you were flirting with me..."

ethan @talkingmouth "Hm? I think I kinda remember that, sure."

yellow surprisedbrow blush @sad2eyes talkingmouth "Well, um, you said it was a joke. And I was just curious, um... if you..."

$ PlaySound("GenericDoorOpen.ogg")

show blue with dis
show ethan:
    xpos 0.33
    ease 1.0 xpos 0.25
show yellow:
    xpos 0.66
    ease 0.2 xpos 0.85
    pause 1.0
    ease 0.5 xpos 0.75

blue @talkingmouth "Hm? What are you two still doing up?"

show yellow -surprisedbrow -blush with dis

ethan @talkingmouth "It's the weekend, my guy. No reason to go to bed yet."
ethan @confused "More important question, where have you been all day? You totally missed Daybreak's party."

blue @closedbrow talkingmouth "Not like I would've been invited anyway. Dawn hates me."

yellow -blush @closedbrow talkingmouth "I don't think Dawn has it in her to hate anyone, regardless of your... history."

ethan @talkingmouth "And besides, Daybreak didn't actually invite anyone. It was all Loaf."

blue @happy "Hah! That just seals it, then."

ethan @upeyes talkingmouth "Whatever, man. Are you going to answer the actual question?"

show ethan surprisedbrow frownmouth
show yellow surprisedbrow frownmouth
with dis

blue @closedbrow talkingmouth "I've been trying to {w=0.5}make friends."

ethan @talking2mouth "Uh..."

show blue surprisedbrow frownmouth behind yellow

show yellow:
    xpos 0.75
    ease 0.5 xpos 0.6

yellow happy "That's fantastic!"

narrator "Yellow throws her arms around Blue."

blue -surprisedbrow -frownmouth -surprised @surprised lightblush "What? What are you doing?!"

show yellow:
    xpos 0.6
    ease 0.5 xpos 0.75

yellow -happy @surprisedbrow happymouth blush "Oh. I... um..."
yellow @happy blush "I'm just really, really proud of you, Blue!"
yellow @sadbrow talkingmouth "But going to that birthday party would have been a great way to do that, don't you think?"

blue @closedbrow talkingmouth "I... maybe, yeah."

ethan -surprisedbrow @unamusedbrow talking2mouth "Dude, did you seriously not think of that yourself?"

blue @angry "I'm new to this! Lay off! And you're one to lecture me about friends. You've got the superpower that makes it easier for you, and you're still mooching off of [first_name]'s!"

ethan @closedbrow talking2mouth "Hurtful {i}and{/i} correct. Well-played."

ethan @confused "Though you gotta take it easy on me, too. I mean, you knew the guy for over a decade, right? Where could I even find friends that aren't already his?"
ethan @upeyes talking2mouth "I mean, I've got a bunch of weirdoes on the internet who know my name, but I wouldn't call them 'friends.'"

blue @wistful "...Yeah, it's tricky to find someone [first_name] hasn't already met."

show blue surprisedbrow frownmouth
show yellow surprisedbrow frownmouth
with dis

ethan @unamusedbrow talkingmouth "That why you tried to hide Yellow from him? You were worried he'd take her, too?"

yellow @sadbrow talkingmouth "N-no! That's not what happened."

show blue wistful with dis

ethan @closedbrow talking2mouth "I'm not judging you. Maybe I should, but it's not my job, and I don't work for free."
ethan @talking2mouth "I'm just saying, there's another way. You don't have to see him as an enemy."
ethan @closedbrow talking2mouth "Like, I {i}get{/i} that you're frustrated he's better than you, but--"

blue wistfulbrow frownmouth @angry "He is {i}not{/i}."

ethan @closedbrow talking2mouth "--but I am too, and I'm not blowing up on the guy about it."

blue @surprised "Wait, what? You're... frustrated... too?"

ethan @unamusedbrow talking2mouth "Of course I am. My dormmate and best friend at this school is basically me, just better in every way."
ethan @sad2eyes happyeyebrows talking2mouth "Well, I guess I've got a better sense of fashion."
ethan @closedbrow talkingmouth "Anyway, that'd frustrate {i}anyone{/i}. I'm not a saint."
ethan @talkingmouth "But it's not like the guy brags about it or anything. All he ever does is try to help people."

blue @closedbrow talkingmouth "It's annoying."

show yellow surprisedbrow frownmouth with dis

ethan @happy "Yellow does the same thing. You seriously think {i}she's{/i} annoying?"

show yellow blush sadeyebrows lovingeyes -frownmouth with dis

blue @angry "Of course not!"

ethan @talkingmouth "There you go, then."

show yellow -lovingeyes with dis

blue @talkingmouth ".{w=0.5}.{w=0.5}.{w=0.5}Compared to [first_name] and I, you're practically a stranger. I don't know why I'm even listening to you."

ethan @talking2mouth "Sometimes, being so close to the problem, you can't tell what it actually is. It helps to keep the issue at arm's reach."
ethan @closedbrow talkingmouth "If you can avoid getting invested, it doesn't matter what happens."
ethan @happy "Though it's obviously too late for that, for you."

blue @talkingmouth "You're... different than I thought you were."

ethan surprised @closedbrow talkingmouth "You're [bluecolor]exactly who I thought you were.{/color}"

show yellow surprisedbrow frownmouth -blush 
show blue surprisedbrow frownmouth
with dis

$ PlaySound("pokemon/ball sound.ogg")
$ sidemonnum = pokedexlookup("Eevee", DexMacros.Id)
$ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))

sidemon @talkingmouth "{i}Hack!{/i} {w=0.5}{i}Bleh!{/i} {w=0.5}Eev."

narrator "A small handful of Foreverals drops onto the suite's floor. Blue's Eevee chirps disgruntledly, blinking sleep out of its eyes."

pause 2.0

stop music fadeout 1.5

show screen songsplash("Run Away, Fugitives", "Lazy Totodile")
queue music "audio/music/runawayfugitives_start.ogg" noloop
queue music "audio/music/runawayfugitives_loop.ogg"

show yellow sad with dis

ethan unamusedbrow frownmouth @talking2mouth "Oh, you can do that, too, huh? Guess that explains all this."
ethan @closedbrow talking2mouth "My bad. Thought we were getting somewhere."

blue sad "W-wait! Hold on, that wasn't--"

ethan @talking2mouth "Whatever, man. After Nathaniel, I should've known no-one would talk to me unless they wanted something."
ethan @sad2eyes talking2mouth "Guess I'm just waiting to find out what [first_name] wants, at this point."

hide ethan with dis

pause 1.0

yellow sad @talkingmouth "Blue... that was cruel."

blue @surprised "Wait! C'mon, Yellow, please! I had no idea that Eevee was going to throw up those rocks--I don't even really get how it works!"

show yellow unamusedeyes seriouseyebrows frownmouth with dis

blue sad "I just know that I need to talk to people and, and... and..."

yellow @closedbrow talkingmouth "I can't keep doing this. I'm tired. I'm {i}so{/i} tired, Blue."
yellow @tears surprisedmouth cryingeyes "I've been trying so hard, Blue. I've been trying {i}so{/i} hard to get you to show that you're a better person. And it's exhausting. Every inch of progress is something I have to fight for, for ages."
yellow @unamusedeyes unamusedeyebrows talkingmouth "And I hate fighting."

blue @talkingmouth "B-but... But I didn't mean...!"

yellow @surprisedmouth cryingeyes tears "I need... I {i}need{/i} you to try harder. I know there's good in you. I've seen it. But saving me one time doesn't mean I'm going to try and save you for the rest of your life."
yellow @closedbrow talkingmouth "Doctors get sick, too."

blue @talkingmouth "Wait! I promise, this wasn't just about getting stronger. I mean, yeah, that's what I've been trying to do all week, but that's why I've been staying away from everyone in this dorm! I screwed up with [first_name], but--"

yellow @unamusedbrow talking2mouth "Blue."

pause 1.0

yellow closedbrow cryingeyebrows sadmouth tears @cryingeyes talkingmouth "I can't care."

scene blank2 with Dissolve(3.0)

stop music fadeout 1.5

jump day010523