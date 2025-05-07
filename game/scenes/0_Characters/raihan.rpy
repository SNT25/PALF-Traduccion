label Raihan1:

if (not IsBefore(1, 5, 2004)):
    $ persondex["Raihan"]["Events"].append("Level2SceneVer2")

scene academyold
with Dissolve(2.0)
stop music fadeout 1.5
$ renpy.music.queue("Audio/Music/brandnewworld.ogg", channel='music', loop=True, fadein=1.5, tight=None)

narrator "You're walking across campus, when you suddenly hear the sound of heavy footfalls behind you, as though someone's running up."

show raihan:
    xpos 3.0 rotate 0
    ease 0.5 xpos 0.25 rotate 5
    pause 0.3
    ease 0.5 rotate 0 xpos 0.5

raihan @happy "[last_name]! You don't look busy."

menu:
    "Actually, I am.":
        raihan @happy "Oh, alright."

        hide raihan with dis

        if sceneviewer:
            return

        $ renpy.pop_call()
        jump freeroam

    "You're right.":
        raihan @talkingmouth "Brill."

if (not WonBattle("Raihan1")):
    $ AddEvent("Raihan", "HadSecondBattle")
    raihan @talkingmouth "I want to battle with you."

    red @talkingmouth "Huh? Uh... any particular reason?"

    raihan @talkingmouth "Your Pikachu, mate! I have to see more of it in action."

    red @talkingmouth "Well... sure. I said I wasn't busy, so, yeah, let's go to the battle hall."

    call clearscreens() from _call_clearscreens_143
    scene blank2 with splitfade

    pause 1.0

    scene stadium_empty 
    show screen currentdate
    show raihan angrybrow
    with splitfade

    raihan @talkingmouth "You ready? I'm not holding back, mate. The full force of the desert dragon's going against you this time!"
    
    red @talkingmouth "Wait, you mean you're using your {i}real{/i} team?"

    raihan @happy "Nah, nah, nothing like that. I just mean that when we fought in the Battle Hall, I was off my game."

    red @confused "You... won?"

    raihan @talking2mouth "There's bad wins. There's good losses, too. Mate of mine said that one."

    red @happy "Well, alright! I'm certainly alright with taking another crack at you. Let's go!"

    python:
        trainer1 = MakeRed(2)
        trainer2 = MakeTrainer("Raihan", number=2)

    call Battle([trainer1, trainer2]) from _call_Battle_122

    $ battlehistory["Raihan2"] = _return

    show raihan with dis

    pause 1.0

    raihan @talkingmouth "Well... that's that, then."

if (WonBattle("Raihan1") or WonBattle("Raihan2")):
    raihan @happy "Think fast!"

    show dragonbadge with dis:
        xalign 0.4 yalign 0.5 zoom 0.0
        ease 0.5 xalign 1.5 yalign -0.5 zoom 1.0

    if (WonBattle("Raihan1")):
        show academyold with vpunch
    else:
        show stadium_empty with vpunch

    raihan @talkingmouth "Good catch."

    red @talkingmouth "What... what is this?"

    if (WonBattle("Raihan2")):
        raihan @talkingmouth "It's what you get for beating a Gym Leader."

    else:
        raihan @talkingmouth "It's what you get for winning against me in the Battle Hall."
    
    $ DisplayGetItem("dragonbadge")

    narrator "[bluecolor]You gained the Dragon Badge of Galar!{/color}"

    red @surprised "Wh-what?! Really? Wait, that wasn't an {i}official{/i} gym challenge, right?"

    raihan @happy "Might as well have been. You don't have any badges, right?"

    $ badgenums = len(badgeslist)

    if (badgenums == 0):
        red @talking2mouth "Well, no."

    elif (badgenums > 0):
        red @talkingmouth "I actually have [badgenums]."

    if (badgenums < 2):
        raihan @happy "Well, the team I fought you with is the kind of team I might use against a trainer who already has a badge, so you beat me at my better."

    else:
        raihan @surprised "Huh. Well, I might've go in on you a bit harder, then..."

        raihan @closedbrow talking2mouth "But what's past is buried, and you buried me."

    raihan @talkingmouth "Fair play, mate."

    red @sadbrow talkingmouth "I don't... I don't know if I can accept this."

    raihan @talkingmouth "There aren't a lot of clear wins out there, mate. Kinda nettles me to see someone turning one down, you know?"

    if (badgenums == 0):
        raihan @talkingmouth "Consider it the start of your collection. If you end up where I think you will, I'd like to say you earned your first badge off me."

    red @talkingmouth "...Alright. Thanks a lot, Raihan."

    raihan @happy "Don't thank me, mate! You beat me, fair as square. Seems I could learn from you."

    red @happy "What? No way! You're the eighth Gym Leader of the major circuit in Galar, right? I'm sure there's {i}tons{/i} I could learn from you."

else:
    narrator "There's a distant look in Raihan's eyes."

    pause 1.0

    raihan @sadbrow talking2mouth "It's alright, mate. You did well, that first time we battled, and now. Don't hold it against yourself."

    red @talkingmouth "I won't. I mean, you're the eighth Gym Leader of the major circuit in Galar, right? I'm sure there's tons I could learn from you."

raihan @sadclosedbrow talkingmouth "Learn from me, huh..."
raihan @talkingmouth "I don't know about that. You know what my record is against Leon?"

show raihan surprisedbrow frownmouth with dis

red @talkingmouth "Hm. Seventeen-nothing?"

raihan -surprisedbrow -frownmouth -surprised @happy "Hey, give me a {i}little{/i} credit! It's only ten-nil!"

red @happy "Oops! Sorry. I don't really keep up to date on champion affairs."

raihan @talking2mouth "Probably saves you a lot of time, yeah."
raihan @happy "Oh, that reminds me!"
raihan phone @talkingmouth "Selfie time?"

red @talkingmouth "Sure."

show blank

$ PlaySound("photo.ogg")
pause 0.5

hide blank with dis

raihan @talkingmouth "Nice smile. You're pretty photogenic."

show raihan -phone with dis

red @talkingmouth "When I was younger, I was really self-conscious about my teeth. So I just brushed 'em really well every day, and trained myself to show all my teeth when I smile."

raihan @closedbrow happymouth "Heh. Cute story."

pause 0.5

red @talkingmouth "Feel like telling me one?"

raihan @talkingmouth "Hm?"

red @happy "A story."

raihan @talkingmouth "...Trade you for more info on your Pikachu?"

red @talkingmouth "Sure."

raihan @talkingmouth "Started taking 'em after I became a Gym Leader. Actually, if you scroll back far enough on my RotoPhoto account, you can see my first few pictures."
raihan @closedbrow happymouth "Blurry, out-of-focus... shoddy work. I was a total amateur back then. Didn't even have a custom photography lens, I was just using a bog-standard Rotom phone at the time."
raihan @talkingmouth "I've got a granddad. Right ferocious fellow. Takes battling seriously. More than anything else."
raihan @talkingmouth "He asked me to take a picture of myself after my battle with Leon."
raihan @happy "Something to remember my win by, you know?"

pause 0.5

raihan @sadmouth "...Well, I didn't. That blasted Charizard of his... I'm sure you've heard about it."

pause 0.5

raihan @talkingmouth "But I wasn't going to let him down, right? I took that picture anyway."

pause 1.0

raihan @talking2mouth "The old codger asked me why I was smiling. I'd lost, right? I'd nothing to be smiling about."
raihan @closedbrow sadmouth "Truth is, I didn't even think about the fact I was smiling. You smile when you have a picture taken. Didn't think it through more than that."
raihan @talkingmouth "Anyway, my granddad told me to stick that picture up where I'll see it every day."

pause 0.5

raihan @talkingmouth "So I did. Right there on my office wall at the gym. Something to look at when my mind wanders."
raihan @happy "I stuck the next one there, too. And the next one."

pause 0.5

raihan @talkingmouth "I think granddad wanted me to use those pictures as a reminder of my failures. I dunno. He's a hard man, harder than my Duraludon."
raihan @happy "But, you know, all I saw was a handsome guy smiling at me. And in the background of each one of them, my rival--my best friend--Leon, was there."

pause 0.5

raihan @happy "And you'd never notice this unless you were looking {i}really{/i} close, but... he looked more tired in each photo."
raihan @talkingmouth "I ran him harder each time. I got a bit closer. Those pictures weren't reminders of my failure at all. They were reminders of my progress."

pause 0.5

raihan @happy "Still, I wanted a couple pictures that {i}weren't{/i} of failure, you know? Not good for your brain to just be seeing your losses over and over."
raihan @talkingmouth "I took more pictures. Of wins. Sometimes of other losses. Of really good meals, sometimes. Nessa would drop by once in a while, and she noticed."

raihan @talkingmouth "She suggested I start posting stuff online. I was a new Gym Leader. Untested, unknown. Hammerlocke Stadium could do with a PR boost, you know?"

pause 0.5

raihan @talkingmouth "She talked to some of her people, some of the photographers and website designers she worked with, and they set me up with some better equipment."
raihan @talkingmouth "Got me on RotoPhotos, and the rest... guess the rest is history."

pause 0.5

red @talkingmouth "Huh."

raihan @closedbrow talkingmouth "Yeah, I guess you could say I kinda fell into it. I think a lot of people out there--at least the ones who comment on my photos--think that I'm kinda mad about all those losses I've racked up."
raihan @talking2mouth "And that's 'mad' in the Galarian sense. 'Mad' as in 'potty', 'loony', 'off my rocker.'"
raihan @closedbrow talking2mouth "But nah. I keep it real. I'm having fun. Leon's the best rival a guy could ask for. And I'm still young. I got time."

pause 1.0

red @talkingmouth "You mentioned when we first met that Lance was an idol of yours?"

raihan @sad "...Yeah. I'd never met the guy, of course. Shame how he turned out."
raihan @sadbrow talkingmouth "Guess I saw him as a kindred spirit. But there are a few big differences between us."
raihan @happy "I never stopped having fun. And I never tried the same strategy twice."

red @surprised "Really?"

raihan @talkingmouth "Real. I've tried weather teams, I've tried double, single, even rotation battles. I went in with a team of five Level 1 Rattata, and my Duraludon, once."

pause 0.5

raihan @closedbrow sadmouth "That one was embarrassing."

pause 0.5

raihan @talkingmouth "Anyway, I guess that's the big difference between Lance and I. He tries the same thing over and over. And, fair play, it worked for him."
raihan @closedbrow talkingmouth "Not sure I want to get into his number of attempts. Not that there's anything wrong with that, of course. I'll just run out of space on my wall."

red @happy "Hah! You know, Raihan, you {i}really{/i} surprised me."

raihan @talkingmouth "Oh, yeah? How so, mate?"

red @sadbrow talkingmouth "I'm kind of a country boy, so I didn't really know what an influencer did... or what it {i}was{/i}, to be honest... but I hadn't heard good stuff. But you seem great."

raihan @talkingmouth "There are a lot of bad apples out there that give us bad names. It's kinda like being a street performer, at the end of the day. Only difference is, our street is the entire world."

red @confused "What do you mean?"

raihan @talkingmouth "Think of it like this. What does the Great Raihan produce? Like, what product do I sell?"

pause 0.5

red @confused "I have no idea."

raihan @happy "Trick question, anyway. I mean, besides the odd water bottle or commemorative jumper, I don't make anything tangible."
raihan @talkingmouth "Food critics or movie critics do similar stuff. They provide opinions. In theory, they help you guide your own."
raihan @sadbrow talking2mouth "Now, a lot of blokes just take the critics' or influencers' opinion and make it their own, but we would {i}hope{/i} that our opinions are just a foundation, not a whole structure."
raihan @happy "A lot of influencers, then, provide opinions. Right?"

redmind "He's weirdly passionate about this, huh?"

raihan @talkingmouth "I like to think that my unique position as a Gym Leader means that I get to provide something of even more value than an opinion, though."
raihan @happy "I want to give people hope. Leon's undefeatable. He really is. But as long as I keep battling him, I give all the kids in Galar hope."
raihan @talkingmouth "You should see my demo info."

red @confused "Demo info?"

raihan @talkingmouth "Right, 'demographics information'. Means the kind of people that follow my accounts. Young, old, men, women, jobs, that kind of stuff."
raihan @talking2mouth "There's a {i}lot{/i} of middle-aged housewives there. Bunch of businessmen who are over the hill. Little kids who dream that they'll be the next Leon."

pause 1.0

raihan @happy "I want to give them all the hope that I have. Not the hope that they can beat Leon. But that, one day, {i}I'll{/i} beat Leon--and then they can beat {i}me.{/i}"

pause 0.5

raihan @talkingmouth "'Course, there's only so much I can do just taking pictures and popping on captions. But accepting defeat against the undefeatable Leon would be letting down the Fang Gang."
raihan surprisedbrow frownmouth @happy "That's not going to happen anytime soon, no matter what--"

pause 1.0

$ PlaySound("idea.ogg")

raihan @sadbrow talkingmouth "Huh. That's weird. Why was I about to say that?"

red @talkingmouth "What?"

raihan -surprisedbrow -frownmouth @talkingmouth "I was just all but ready to tell you something I generally keep pretty close to my chest. Wonder what that's about?"

red @surprised "Oh."
red @closedbrow sweat talking2mouth "Right, I guess you weren't here, then. Look, I have this thing called 'Frienergy,' and--"

raihan @happy "You're pulling my leg? C'mon, you told everyone in the {i}world{/i} about Frienergy. I watched you defeat Berlitz, remember."

red @surprised "...Oh. Oh, right!"

raihan @talkingmouth "Interesting to see its effects for myself, though. Or 'feel' them, I guess. I {i}do{/i} feel pretty chill around you."

red @sadbrow talkingmouth "I don't know. You seem like a pretty chill guy. Maybe that's just you."

raihan @talkingmouth "...Heh. Well, you've seen me in battle. You know how unchill I get, then."

red @confusedeyebrows talkingmouth "Is the roaring you do in battle a marketing thing?"

raihan @talkingmouth "Sort of. Did it once in battle without really thinking about it. Got, like, seventy messages on my RotoPhoto account the next day telling me how sexy it was."
raihan @closedbrow talking2mouth "The Great Raihan {i}always{/i} listens to fan feedback."
raihan @sad "Though sometimes my gym trainers need to drag me out of my office to take on other challengers. Busy managing my accounts, or planning my next run at Leon." 
raihan @happy "Heh, but it's fun. And I've never left a challenger waiting for more than ten minutes."

pause 1.0

raihan @talkingmouth "Actually, Hammerlocke Stadium has such a good record, even the Chairman of the Galar League used to commend us."

show raihan surprisedbrow frownmouth

stop music
queue music "<from 28>audio/music/rose_start.ogg"
queue music "audio/music/rose_loop.ogg"

pause 2.0

raihan closedbrow talkingmouth "Speak of the devil. Sorry, gotta take this phone call."

stop music fadeout 1.5
$ renpy.music.queue("Audio/Music/brandnewworld.ogg", channel='music', loop=True, fadein=1.5, tight=None)

show raihan -closedbrow frownmouth with dis:
    xpos 0.5
    ease 0.5 xpos 0.75 zoom 0.8 ypos 0.9

narrator "As Raihan holds his phone up to his ear, his voice takes on a much more flat and uninterested tone."

raihan @sadmouth "Kaasib speaking."

redmind @thinking "Kaasib?"

pause 1.0

raihan @talkingmouth "Yes. As I said in my last report, everything's fine here."

pause 1.0

raihan @sadmouth "Drayden is steady-headed, competent, and respected by his students and co-workers."

pause 1.0

raihan @angrybrow sadmouth "Yes, that's the situation as I've seen it. If you don't believe my report, I'd ask why you sent me out here?"

pause 1.0

raihan @sadmouth "No, Chairman. I'm very... {w=0.5}{nw}"
extend @angrybrow sadmouth "grateful."

pause 1.0

raihan @sadmouth "That won't be necessary. My reports are accurate and full."

pause 1.0

raihan @talkingmouth "And how's the substitute doing?"

pause 1.0

raihan closedbrow sadmouth @angry "Great. Raihan out."

pause 2.0

narrator "You wait patiently as Raihan breathes out deeply, a rumbling growl in his throat. His foot bounces rapidly, before finally slowing to a stop as he stomps on the ground, huffing."

show raihan -closedbrow -sadmouth with dis:
    xpos 0.75
    ease 0.5 xpos 0.5 zoom 1.0 ypos 1.0

raihan @sadmouth "Right. I've had just about enough of that man, mate."

red @confused "From context... Chairman Rose?"

raihan @angry "Bigwig of the Galar League. My boss, and a bloody fascist, if you ask me."

red @talking2mouth "He sent you here to check up on Kobukan Academy's status?"

raihan @sadmouth "No. It was just... 'good luck' that I happened to be near something he wanted an eye on."
raihan @sad "Since I was already off of gym duties, I figured I'd drop by and see Sunny and Ness. I didn't plan to stay here, as you know, but I guess it works out..."

red @talkingmouth "Why were you off of your gym duties, though?"

raihan @sad "...Rose doesn't like me. He didn't like when Leon endorsed me, years ago, doesn't like how I run my gym, doesn't like anything about me."
raihan @sadmouth "He calls this a paid vacation, but... he appointed a substitute. Some rock star twink he picked up in Alola."
raihan @angry "You don't appoint a substitute if you're expecting the old guy to come back. It's frustrating, 'cause I don't even know what I'm doing wrong!"

pause 0.5

raihan @closedbrow sadmouth "I mean, I don't win too often, don't lose too often. We keep the stadium swept and clean. I wear the logos he pins up everywhere. Never said a bad word about him in public."
raihan @surprisedbrow sadmouth "I don't think it's even a class thing. Sure, he's rich as a dragon now, but he used to be a {i}coal{/i} miner."

pause 0.5

red @surprised "Wait, so... Rose kicked you out of your gym?!"

raihan @surprised "Hey, hey, keep it down, please! That's not the kind of story I want to post up on my photos, you get it?"
raihan @closedbrow talkingmouth "It's not like I can give people hope if they figure out I'm one bad day away from losing that job."

red @talking2mouth "Ah. Sorry."

raihan -frownmouth @talkingmouth "It's alright. No harm done."

pause 0.5

raihan @talkingmouth "{w=0.5}.{w=0.5}.{w=0.5}.[last_name]?"

red @talkingmouth "Yeah?"

raihan @talkingmouth "Can you think of a reason why Rose might not like me? I get a feeling you've got more of a handle on specific people's feelings, even if I have more experience with groups."

red @talking2mouth "That's tough to say. Without more details about your case, the best I can give is a guess. But I think..."

menu:
    "He's worried you'll beat Leon.":
        $ AddEvent("Raihan", "DislikeBeatLeon")
        raihan @surprised "Seriously? I mean, I like hearing that, but I really don't know about that one..."

    "He dislikes your popularity.":
        $ AddEvent("Raihan", "DislikePopularity")
        raihan @surprised "Maybe? Leon's way more popular than I am, though. Heck, even Rose himself is."

    "He thinks you're unprofessional.":
        $ AddEvent("Raihan", "DislikeUnprofessional")
        raihan @surprised "Maybe? I guess I {i}do{/i} have fun in battle, but so does Leon..."

    "He's jealous of your sexy, sexy, body.":
        $ AddEvent("Raihan", "DislikeBody")
        raihan @surprised "Seriously? I don't know. He has a bit of a dad bod, but he doesn't look bad for his age at all."

    "I have no idea.":
        $ AddEvent("Raihan", "DislikeUnknown")
        raihan @sad "Then I guess we're in the same quicksand."

red @talkingmouth "I might need to put in a bit more thought."

raihan @talkingmouth "Maybe I should ask Ness. She has a way of cutting to the bone of any issue. If there's an inconvenient truth, she knows it."
raihan @closedbrow talkingmouth "...And is {i}always{/i} willing to share it."
raihan @talking2mouth "...Yeah, maybe. Hey, think you could talk to her for me?"

red @happy "What? You're friends! You knew each other since you were kids, right? Why don't you just ask her yourself?"

pause 0.5

raihan @sadbrow talkingmouth "...Truth is, I don't really want her to know the whole thing going on with my job right now. And if {i}I{/i} asked her, she'd immediately know what was up."

red @confused "Hm?"

raihan @sad "Back in the day, when we were the Galarian Stars... she told us not to do what we did. Well, not exactly that."
raihan @sadbrow talkingmouth "She didn't say 'don't do this.' She said 'this is what will happen if you {i}do{/i} do it.'"

pause 0.5

raihan @sadbrow talkingmouth "She's a Cassandra, you know. Always right, eventually. Probably wishes she wasn't."
raihan @closedbrow talkingmouth "And I'm totally fine admitting when I lost, but if I could find a way to patch this all over {i}before{/i} I tell her..."
raihan @sadbrow happymouth "You feel me?"

$ ValueChange("Nessa", 3, 0.33)

narrator "Your understanding of Nessa deepened!"

red @talkingmouth "Little bit."
red @sadbrow talkingmouth "One problem, though. Historically, I've been pretty awful at keeping secrets. Like, second to Sabrina, in terms of awfulness."

raihan @sadbrow talkingmouth "Well... do your best, if you can."

red @closedbrow sweat talking2mouth "Alright. But no promises."

raihan @talkingmouth "Thanks. Hey, you know how to contact me--I'm just a quick search away on the internet. Ping me whenever, if you just want to chat. I still got a few more questions about that Pikachu of yours."

$ BecomeContacted("Raihan")

red @talkingmouth "Sure. I'll reach out."

raihan @talkingmouth "Cool. Thanks, [bluecolor]mate.{/color}"

$ oldrelationship = persondex["Raihan"]["Relationship"]
$ persondex["Raihan"]["Relationship"] = "Mate"
$ persondex["Raihan"]["RelationshipRank"] = 1

$ PlaySound("sav.ogg")

narrator "Your heart shifts as you feel your relationship with Raihan evolve from '{color=#0048ff}[oldrelationship]{/color}' to '{color=#0048ff}Mate{/color}'!"

return