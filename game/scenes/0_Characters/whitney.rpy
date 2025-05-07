label Whitney1:
    if (not IsBefore(1, 5, 2004)):
        $ persondex["Whitney"]["Events"].append("Level2SceneVer2")

    scene baseball
    with Dissolve(2.0)
    queue music "audio/music/goldenrod_start.ogg" noloop
    queue music "audio/music/goldenrod_loop.ogg"

    narrator "You're walking past the baseball field to get to Inspira City when you suddenly hear a shouting voice from far away."

    whitney @surprised "{size=15}W{/size}{size=18}a{/size}{size=21}t{/size}{size=24}c{/size}{size=27}h{/size} {size=30}o{/size}{size=33}u{/size}{size=36}t{/size}{size=39}!{/size}"

    show baseballitem:
        xanchor 0.5 yanchor 0.5 xpos 1.1 ypos -0.1 zoom 0.2 alpha 1.0
        easeout 0.5 xpos 0.3 ypos 1.6 zoom 1.0 alpha 0.3

    if (IsBefore(1, 5, 2004)):
        $ PlaySound("Pokemon/pikachu_angry3.ogg")
        pikachu angry_4 "Pika!"

    else:
        $ PlaySound("Pokemon/pikachu_angry3.ogg")
        libpikachu glowing angry sparks "Pika!"

    narrator "Moments before the ball would hit you, [pika_name] jumps off your shoulder and deflects the ball with his tail, slamming it into the dirt."

    red @surprised "Woah. [pika_name]?"

    if (IsBefore(1, 5, 2004)):
        $ PlaySound("Pokemon/pikachu_norm2.ogg")
        pikachu neutral_2 "Pi... ka."

    else:
        $ PlaySound("Pokemon/pikachu_angry3.ogg")
        libpikachu angrybrow happymouth -sparks @talkingmouth "Pi... ka."

    red @happy "That was actually--"

    show whitney:
        xpos 1.1
        ease 0.3 xpos 0.5

    whitney @surprisedbrow happymouth "That was {i}so{/i} cool!"

    red @happy "Yeah, what she said."

    whitney @talking2mouth "Your Pikachu totally just deflected that ball! Like he'd trained, even! Has your Pikachu ever been in a Pokéathlon, or something?"

    red @talkingmouth "Nah. He's just very motivated by not taking a baseball to the face."

    whitney @smilemouth "Yeah, I get that! It's not as bad after the first couple times, though!"
    whitney @surprised "Try taking a {i}bat{/i} to the face! Now, {i}that's{/i} pain."

    red @happy "Has that happened to you?"

    whitney @happy "It happens to everyone if you play this game long enough! But, I..."

    pause 0.5

    whitney @surprised "Oh, I need to get back to the game! Want to watch?"

    red @closedbrow talking2mouth "I was planning on heading into Inspira, actually."

    whitney @closedbrow talkingmouth "Hm."
    whitney @talking2mouth "Tell ya what. You stay here for half an hour and watch me clean up this game, then we can go into Inspira together."
    whitney @smilemouth "Sounds good?"

    red @talkingmouth "Sure."

    whitney happy "Cool! See ya in a bit."

    hide whitney with dis

    pause 1.0

    narrator "You take a seat in the outfield, with [pika_name] nestled snugly in your lap."
    narrator "You watch the game unfold as you pat [pika_name], keeping a careful eye on Whitney."
    narrator "You're not too familiar with the rules of baseball, but it's impossible to ignore that Whitney is doing {i}very{/i} well."
    narrator "Every time she hits the ball, a resounding {i}crack{/i} echoes across the Kobukan campus, hinting at the strength hidden with Whitney's self-proclaimed 'tiny, but dense' frame."

    pause 1.0

    narrator "Eventually, the game wraps up with a dominating victory for Whitney's team, and Whitney trudges over, sweaty but beaming."

    pause 0.5

    show whitney with dis

    whitney @happy "Did you {i}see{/i} me out there? Woo! I hit {i}three{/i} home runs!"

    red @talkingmouth "Very impressive."
    red @confused "Are you still good to go to Inspira, though? I imagine you're pretty tired."

    whitney @talking2mouth "Nah, I've got tons of energy! I just don't get tired anymore, now that I'm on Tia duty pretty much 24/7."

    red @happymouth confusedeyebrows "Tia duty?"

    whitney @closedbrow talkingmouth "Yeah, you know. Reminding her to wake up in the mornings, making sure she eats more than just fish, reminding her to take showers."
    whitney @surprised "Like, she is 100%% okay with just jumping in public fountains, or diving into the seaport in Inspira, but showers just always slip her mind."

    red @closedbrow talking2mouth "Huh."

    whitney @sad "Man, where did you even {i}find{/i} that girl?"

    red @sadbrow happymouth "Um... she sorta just fell out of the sky."

    whitney @smilemouth "Alright, keep your secrets. Just means I get to ask you for more when it comes time to repay me."

    red @confusedeyebrows talkingmouth "I trust you won't abuse that privilege?"

    whitney @surprised "Ooh! Bad move. You definitely shouldn't trust me. I'm going to abuse the {i}hell{/i} out of it, actually."

    red @closedbrow talking2mouth "Great."

    pause 0.5

    red @confused "Well, what can I do for you?"

    whitney @closedbrow talkingmouth "Hmmm... figuring that out sounds like a lot of work."
    whitney @angrybrow happymouth "How about I delegate that to a real expert in the field?"

    red @confused "Are you talking about--"

    whitney @closedbrow talking2mouth "Yes, I'm {i}obviously{/i} talking about you."

    pause 0.5

    red @closedbrow talking2mouth "Well, I, uh, I gotta be honest, I'm not sure what I can do to pay you back for your Tia-wrangling. Maybe if I knew you a bit better, I'd be able to figure out something you need help with?"

    whitney @talking2mouth "Mmm... alright. Let's walk to Inspira, and I'll give you an unabridged history of Whitney."

    red @talkingmouth "I'll grab the popcorn."

    if (IsBefore(1, 5, 2004)):
        $ PlaySound("Pokemon/pikachu_sad.ogg")
        pikachu sad_2 "Piiiika."

    else:
        $ PlaySound("Pokemon/pikachu_sad.ogg")
        libpikachu sad "Piiiika."

    scene city_A with splitfade

    pause 0.5

    show whitney with dis 

    pause 0.5

    whitney @happy "Anyway, that brings us to {i}Cathy{/i}, and you've already heard about Cathy from when I told you about when I was dating Samantha--"

    red @surprised "Oh my god, you dated Cathy? {i}Right{/i} after Carrie?"

    whitney @angry "Hey! It was a revenge date! She cheated on me with a {i}boy{/i}, so the sis code does {i}not{/i} apply there."

    red @sadbrow talking2mouth "That's more than a violation of the sis code, Whitney. You dated Carrie's literal sister."

    whitney @closedbrow talking2mouth "{i}For revenge,{/i} though."

    red @angrybrow talking2mouth "That does {i}not{/i} make it better."

    whitney @closedbrow talkingmouth "Come to think of it, I think there might have been a couple weeks where I was dating both of them..."

    red @surprised "Oh my god."

    whitney @happy "Did I mention they were twins?"

    red @closedbrow talking2mouth "Oh my {i}god.{/i}"

    narrator "While walking to Inspira, Whitney has, true to her promise, been giving you a {i}very{/i} unabridged history of Whitney."

    red @talkingmouth "What's your secret?"

    whitney @closedbrow talkingmouth "Hm?"

    red @talkingmouth "How have you had {i}so many{/i} exes? It sounds like you've dated more people than were in my entire hometown."

    whitney @talking2mouth "Well, I did live in Goldenrod. It's a really big city, with a very young population, so there's all sorts of stuff to go to for high schoolers."
    whitney @talking2mouth "Besides, when you're the most popular girl in high school, you don't really need to try very hard to find people who want to date you."

    red @confused "...You, uh, you aren't humble about that, are you?"

    whitney @smilemouth "Nope. False modesty is gross."
    whitney @sadbrow talking2mouth "...I wasn't the best person in high school, though. If I was, I might not have so many exes."

    pause 1.0

    whitney @talking2mouth "Actually, this probably comes as a surprise to you, given how awesome I am, and how everyone loves me, but--"

    redmind @surprisedbrow frownmouth "Really?"

    whitney @closedbrow talking2mouth "When I got to Kobukan, I'd... kinda..."

    pause 1.0

    whitney @sadbrow talking2mouth "Burned all my bridges back home."

    pause 0.5

    red @talking2mouth "That {i}does{/i} surprise me."

    whitney @talking2mouth "Surprised me, too. One day, people loved that I was loud, popular, did my own thing, and was awesome at everything I did. All that mattered was that I was Prom Queen, and I was in charge of Goldenrod High's gossip engine."
    whitney frownmouth @closedbrow talking2mouth "...And the next day, everyone was talking about going to University, and 'being an adult', and boring stuff like that, and I wasn't cute anymore."

    pause 0.5

    whitney @smilemouth "I didn't really notice the change until people got tired of me."

    pause 0.5

    whitney @talking2mouth "Or maybe I {i}did{/i} notice the change, but was hoping that I could ignore it. More this one, I guess."

    red @talkingmouth "Well, regardless of what mistakes you made in the past, you've clearly cemented yourself into Kobukan's social fabric."

    whitney @talking2mouth "{size=30}Cemented into fabric?{/size}"

    red @happy "Everyone knows Whitney. And you know everyone. You're the one people go to when they need to find someone, or get a favor done."
    red @talkingmouth "You're like the Godfather of Kobukan."

    whitney -frownmouth @smilemouth "You really like your old movies, don't you?"

    red @happy "What can I say? I've an appreciation for the classics."

    whitney @smilemouth "Anyway... thanks. I mean, I'm over all that stuff in the past. No use moping over it. There's tons more bridges in front of me. Can't worry about the ones burning behind me, right?"

    red @talkingmouth "Sure."

    whitney @happy "Anyway, I've found that I really like helping people with their problems."

    red @talkingmouth "Right, your 'projects.' Flannery's one. Tia's another."

    whitney @talking2mouth "Yup. I think I might become a Nurse when I graduate Kobukan."

    red @confused "Huh? Aren't you going to be... a trainer? Or a coordinator, at least?"

    whitney @talking2mouth "Nah! Nurses use Pokémon too, silly."

    red @confused "They do?"

    whitney @happy "Sure. Like, Ralts are really good at sensing people's emotions, right? Blissey eggs are pretty much {i}pure{/i} endorphins. Audino are great at communicating with hearing-impaired or nonverbal people." 
    whitney @smilemouth "Miltank milk is hyper-nutritious, and Togekiss can literally shower people with something called 'Joy Dust,' which is a super-thin down that triggers immense dopamine rushes in people."

    red @surprised "Wow. Almost all those Pokémon are Fairy or Normal-type."

    whitney @angrybrow happymouth "Uh, yeah! That's why I'm in those classes, silly!"

    red @happy "I just... wow, this is a whole new side of you, Whit. Is it cool if I call you Whit?"

    whitney @smilemouth "It's cool."

    red @closedbrow talking2mouth "After our battle in Gym Class, I kinda thought you were... I don't know. I didn't think you'd want to be a nurse. I didn't think you'd want to be so... helpful, if that makes sense."

    pause 1.0

    whitney frownmouth "Hm."

    red @sadbrow talking2mouth "Sorry. That was rude of me."

    whitney @talking2mouth "Maybe a little bit, but... well, why do you say that?"

    red @closedbrow talking2mouth "Well, it's... when we battled, you kinda used your Cleffa as a sandbag to trick me into a false sense of security. And the way you refer to some people as 'projects'... I don't know. It feels a bit... utilitarian?"

    whitney @talking2mouth "...Yeah. You got me."

    red @surprised "Huh?"

    whitney @closedbrow talkingmouth "[first_name], can you keep a secret?"

    red @talkingmouth "Very, {i}very{/i} well, actually."

    if (not IsBefore(1, 5, 2004)):
        red @closedbrow talking2mouth "As long as it's not about me. You know, the whole 'Frienergy' thing..."

    pause 1.0

    hide whitney with dis

    show seaport with Dissolve(2.0)

    narrator "Whitney is silent for a long while as you walk through Inspira. Her head is down, deep in thought, as she leads you through the city, seemingly on autopilot."

    pause 1.0

    narrator "After a while, you end up at the seaport."

    if (not seaportunlocked):
        narrator "The harsh cries of some angered bird Pokémon ring in your ears, but Whitney doesn't seem to notice."

    narrator "Slowly, Whitney sits down on the dock and pats the ground next to her."

    show whitney frownmouth with dis:
        xpos 0.5 ypos 1.2 zoom 1.3

    whitney @talking2mouth "...I don't do good things because they're the right thing to do."

    red @frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    whitney @closedbrow talking2mouth "I never have. And I feel bad about that."
    whitney @sadbrow talking2mouth "...Do you get what I mean?"

    red @sad "I'm not sure I do."
    red @closedbrow talking2mouth "Do you... do good things because you think people expect them of you?"

    whitney @talking2mouth "No, that's Hilda."

    red @confused "Then you do them because you just don't mind doing them?"

    whitney @talking2mouth "Bianca."

    pause 0.5

    red @talking2mouth "Please explain."

    whitney @closedbrow talking2mouth "...{i}Sigh{/i}."
    whitney @sadbrow talking2mouth "I'm helping Flannery with her problems because she's fascinating." 
    whitney @sadbrow talkingmouth "She knows so much about tons of obscure things, and you could talk to her for hours without getting bored. She's friendly, kind, hot as hell... I guess I'm just selfish."
    whitney @talking2mouth "I'm helping Tia because as long as I look out for her, and don't ask questions, you kinda have to do whatever I say. And Tia's hilarious. I like being around her because she's really, really funny."

    red @confused "That wasn't {i}exactly{/i} our deal."

    whitney @sadbrow talking2mouth "I learned sign language just so I could flirt with a girl. And I want to be a nurse because... I like the feeling of people needing my help."

    pause 1.0

    whitney @talking2mouth "Yeah. That's the problem. I like when people need my help, or owe me something."
    whitney @angrybrow talkingmouth "And I don't like that about myself."

    pause 0.5

    whitney -shadow @happy "Isn't that screwed up?"

    red @closedbrow "{w=0.5}.{w=0.5}.{w=0.5}."

    pause 0.5

    whitney @sadbrow talking2mouth "If... you want to leave now, that's totally fair. I'd get that."

    red @closedbrow talking2mouth "No, that's not it. I think I get what's happening here."

    whitney @surprised "Hm?"

    red @talking2mouth "You were a super-popular girl back in high school, right? But as everyone started thinking about college, they started losing interest in high school stuff, your domain, and left."

    red @talking2mouth "I get that. Something similar happened to me. And... I mean, I was just a kid back then, but kids can feel, just like adults. And kids can be hurt."

    pause 0.5

    red @confused "That probably... hurt, right?"

    whitney "{w=0.5}.{w=0.5}.{w=0.5}."
    whitney sadbrow @talking2mouth "I had to chase them down to sign my yearbook."

    pause 0.5

    red @talkingmouth "I think, Whitney, that you don't want your friends to be able to leave you."

    whitney @surprised "Hm?"

    red @talkingmouth "You want your friends to owe you something, or be dependent on you for something. So they can't just 'lose interest', and ghost you."
    red @sad "And... based on some of the stories you've told me about your exes... it might be that you're afraid of being treated like you treated some of the women you dated."

    pause 0.5

    whitney @talking2mouth "I'm an awful person."

    pause 0.5

    red @closedbrow talking2mouth "Nah. An awful person wouldn't feel awfully about the awful things she's done."

    whitney @angrybrow "{w=0.5}.{w=0.5}.{w=0.5}."
    whitney @talking2mouth "I don't like losing. I {i}rarely{/i} do. I'm lucky like that. But the thing I like losing least is a friend."

    red @talkingmouth "Whitney, I know {i}exactly{/i} how you feel."

    if (not IsBefore(1, 5, 2004)):
        red @talkingmouth "It's happened to me twice. But you can always bounce back."

    whitney "{w=0.5}.{w=0.5}.{w=0.5}."
    whitney -sadbrow -frownmouth @closedbrow talking2mouth "Okay. I've gotten {i}way{/i} too personal. How about we change the topic a bit?"

    if (IsBefore(1, 5, 2004)):
        red @happy "Sure. Want to know my darkest secrets, too? Maybe it'd make you feel better."

    else:
        red @happy "Sure. I'd offer to tell you about my darkest secrets, too, but... I think the whole school already knows that one."

    whitney @happy "Nah, but thanks for the offer. Let's just talk about Pokémon."

    red @talkingmouth "Alright. So, you're a big fan of the emotion and happiness Pokémon, huh? Have you ever heard of that legend from the Sinnoh region, Mesprit?"

    show black with Dissolve(1.0)

    narrator "Time passes as you and Whitney chat about inconsequential things, slowly bringing the mood back to room temperature."
    narrator "However, the mood suddenly spikes once more, when..."

    show whitney -frownmouth
    hide black with dis

    whitney @smilemouth "So, we've been talking for, like, two hours now, and you haven't asked me out. What's up with that?"

    red @confused "I... kinda assumed you were a lesbian."

    whitney @closedbrow frownmouth "Well, you shouldn't assume."

    red @happy "Ah, but you thought, because I'm a guy, that I would've asked you out by now. So aren't you the assumer here, while I am the innocent assumee?"

    whitney @surprised "Those... aren't words.{w=0.5} {size=30}Are those words?{/size} No, those aren't words."

    red @talkingmouth "Baseball star, polyglot, owner of an ultimate weapon in the form of a cow, aspiring nurse, and now apparent linguist."
    red @happy "Whitney really does have it all. I'm sure your next Ex will tell stories about you for a long time."

    whitney @angrybrow happymouth "Hey! That's mean!"

    red @happy "Sorry, Whitney. But, um... well, besides assuming you were a lesbian, which you haven't denied..."
    red @sadbrow happymouth "I like you, but I've heard how you treated your exes, and... well, I don't really want to be a project."

    if (IsBefore(1, 5, 2004)):
        whitney @closedbrow talking2mouth "Mm. I guess that makes sense. I'm not sure how I even could projectify you, anyway. You seem perfect. Popular, good at everything, attractive enough. For a guy."

        red @happy "Well, hey, so did you, before you told me all that stuff about pre-Kobukan Whitney. I'm just not dumping all {i}my{/i} dark secrets on you, so you'd have to work a little harder to make me a project."

    else:
        whitney @closedbrow talking2mouth "Mm. I guess that makes sense. I'm not sure how I even could projectify you, anyway. You seem perfect. Kind, good at everything, attractive enough. For a guy."

        red @happy "Well, hey, I still sometimes just clam up in front of people. I'm sure I could pay a therapist's kids through college if they took a crack at that. Interested?"

    whitney @surprised "Ugh, {i}work?{/i} Yeah, I'll pass."

    red @happy "Hah. Seeya, Whit. It's been good talking with you."

    whitney @smilemouth "Seeya, [first_name]."

    narrator "You depart the seaport, leaving Whitney sitting on the dock, feet trailing in the high tide."

    pause 2.0

    whitney @angrybrow frownmouth "He can't turn down being my [bluecolor]project{/color}!"

    whitney closedbrow talkingmouth "I mean, he's the most interesting person I've met since Flan, so... yeah, I'm going to make this happen."

    pause 1.0

    whitney closedbrow talkingmouth "But I'm still a lesbian. {w=0.5}...Pretty sure."

    python:
        character = "Whitney"
        renpy.transition(dis)
        renpy.hide(GetCharacterSprite(character))
        renpy.pause(1.0)
        formertitle = GetRelationship(character)
        persondex[character]["Relationship"] = "Project"
        persondex[character]["RelationshipRank"] = 1
        PlaySound("sav.ogg")
        renpy.say(None, "Your heart shifts as you your relationship with {} unknowingly evolves from '{{color=#0048ff}}{}{{/color}}' to '{{color=#0048ff}}{}{{/color}}'!".format(character, formertitle, "Project"))

return

label Whitney2:
    scene baseball
    with Dissolve(2.0)
    queue music "audio/music/goldenrod_start.ogg" noloop
    queue music "audio/music/goldenrod_loop.ogg"

    show whitney casual with dis

    whitney @talkingmouth "...so then I figured that there {i}probably{/i} wasn't a shiny Eevee out there, after all."
    whitney @closedbrow talkingmouth "Which, you know, {i}major bummer{/i}, but I always knew it was a long shot."
    whitney @happy "I decided to just kinda give up on that and go to orientation."

    red @happy "Right! And that's when Roxanne used Boomburst on the microphone, and landed a critical hit on the entire student body."

    whitney @talkingmouth "Yeah! Flan got {i}super{/i} mad at that. I thought she was going to pull her Poké Balls out and throw down with Roxanne right then!"
    whitney @closedbrow happymouth "Luckily, I was there to be the big, squishy, pillow between her rage and the outside world."
    whitney @winkbrow talkingmouth "You know, if you really think about it, I'm a hero."

    red @sadbrow talkingmouth "You're even more of one when I don't think about it."

    whitney @happy "Wahahaha!~{w=0.5} You know just what to say to get on my good side."

    red @talking2mouth "Well, that seems like a pretty safe side to be on."

    pause 1.0

    whitney frownmouth @confused "What do ya mean?"

    red @sad2brow talkingmouth "Well, some of the stories you've told me... putting it delicately, it's clear no-one would want you as an enemy."

    whitney sad2eyes @sadeyebrows talkingmouth "Oh."

    pause 1.5

    whitney talking2mouth "I mean... I didn't want to hurt anyone..."

    scene city_A at sepia 
    show flashback
    with splitfade

    pause 0.5

    show whitney at sepia behind flashback with dis 

    red sepia @surprised "Oh my god, you dated Cathy? {i}Right{/i} after Carrie?"

    whitney @angry "Hey! It was a revenge date! She cheated on me with a {i}boy{/i}, so the sis code does {i}not{/i} apply there."

    red @sadbrow talking2mouth "That's more than a violation of the sis code, Whitney. You dated Carrie's literal sister."

    whitney @closedbrow talking2mouth "{i}For revenge,{/i} though."

    red @angrybrow talking2mouth "That does {i}not{/i} make it better."

    whitney @closedbrow talkingmouth "Come to think of it, I think there might have been a couple weeks where I was dating both of them..."

    red @surprised "Oh my god."

    whitney @happy "Did I mention they were twins?"

    red @closedbrow talking2mouth "Oh my {i}god.{/i}"

    scene blank with splitfade

    pause 1.0

    scene baseball 
    show whitney casual frownmouth
    with dis

    red @sadbrow talkingmouth "Carrie might see it another way."

    whitney "[ellipses]"
    whitney sad2brow frownmouth "[ellipses]{w=0.5}{nw}"
    extend @sadeyebrows "Iunno."

    whitney @talkingmouth "I mean, she hurt me too. And she started it, even."

    red @talking2mouth "Sure."
    red @sadbrow talkingmouth "But did you feel {i}better{/i} for seducing her sister? Or did you just feel {i}even?{/i}"

    whitney poutmouth @talkingmouth lightblush angryeyebrows "I didn't {i}seduce{/i} her. We just started chatting, and one thing lead to another, so..."

    pause 1.0

    show whitney surprisedbrow frownmouth with dis

    red @angryeyebrows talking2mouth "Whitney."

    pause 0.5

    red @talking2mouth "You said you felt awful about how you've treated some of the people in your past. Was that true?"

    whitney -surprisedbrow @sadbrow talkingmouth "What? Of course."

    red @talking2mouth "You don't want to feel awful anymore, right?"

    whitney @talkingmouth sadbrow "Of course not."

    red @talkingmouth sadbrow "Then you gotta make a choice."

    whitney @confused "Um... okay. What choice?"

    red @talking2mouth closedbrow "Either you reach out to the people you hurt, the people living in the scars in your heart, and apologize, or--"

    whitney @surprisedbrow talkingmouth "The other one."

    pause 2.0

    red @surprisedbrow frownmouth "[ellipses]"

    red @talking2mouth "Uh."

    red @talking2mouth "Don't you want to hear the other option?"

    whitney @wince talkingmouth "I can't do the first one. I just can't. Absolutely not. So the {i}only{/i} option is the other one."

    pause 1.0

    red @sad2eyes angryeyebrows talking2mouth "Uh, the issue with that is, uh, the rest of this speech was kinda predicated on you accepting that rebuilding those bridges was the only option."

    whitney @talkingmouth "Oh."

    pause 2.0

    whitney @sad2eyes talkingmouth "You... don't know me very well, do you?"

    red @wince talking2mouth "I'm working on it."

    pause 1.0

    whitney surprisedbrow @neutraleyes neutraleyebrows talkingmouth "Okay. I'm too curious. What {i}is{/i} the second option?"

    red @talking2mouth "You resolve to move on, without letting your past negative experiences affect how you act now."

    pause 1.0

    whitney -frownmouth @happy "Wahahaha!~ I thought this would be something {i}hard!{/i} I can totally do that!"

    red @unamusedbrow talking2mouth "If you think about it for a moment, I can almost guarantee that you'll reconsider that."

    pause 1.0

    whitney @confusedeyebrows "Hm?"
    whitney closedbrow frownmouth "Hm..."
    whitney shadow poutmouth "Hrrrrrmmm..."

    pause 2.0

    whitney -shadow -closedbrow -poutmouth @happy sweat "Sorry! I'm not seeing it. Like, at all."

    red @closedbrow talking2mouth sweat "Well, I did say almost."
    red @talkingmouth sadbrow "Whitney, that means you can't be scared of losing people. That means you have to engage with friends, girlfriends, {i}everyone{/i}, as {i}people.{/i} People capable of making their own choices."
    red @talking2mouth "You'll need to be okay with them leaving you. You'll need to be okay with them not loving you. You'll need to be okay with them hating you--including the people in your past."

    pause 1.5

    red @talkingmouth "If you can't make the past right, then you need to be ready to accept the future. And you can't control that."
    red @happy "See? That's way harder. So making up with everyone in your past is--"

    whitney @talkingmouth "No, genuinely, I'm fine with it. I can totally just forget all that stuff in the past."

    red @unamusedbrow tired unamusedmouth "[ellipses]"
    red @talking2mouth tired unamusedbrow "I very much doubt that."

    whitney surprisedbrow frownmouth @happy "Shows what you know! The past is dead to me! I don't give a {i}hoot{/i} about anything that happened before this exact moment! In fact, I don't even remember it! Whitney is the moving-on girl, and I--"

    show shauna frownmouth:
        xpos -0.2 xzoom -1
        ease 0.5 xpos 0.25

    shauna talking2mouth "Miss Whitney?"

    stop music fadeout 2.0

    show flashback 
    show baseball at grayscale
    show whitney at grayscale:
        xpos 0.5
    show shauna at grayscale:
        xpos 0.25
    with Dissolve(2.0)

    $ PlaySound("ticktock.ogg")

    pause 1.0

    narrator "One-third of a second has passed. You make eye contact with this new person, and open your mouth to say 'hi.'"

    show whitney surprisedeyebrows feareyes frownmouth shadow with dis

    $ PlaySound("ticktock.ogg")

    pause 1.0

    narrator "Two-thirds of a second has passed. In order to greet the new person, you raise up your arm, and Whitney can now see past you, to the woman behind you. Her eyes dilate with terror."

    show whitney surprisedeyebrows feareyes surprised2mouth shadow with dis

    $ PlaySound("ticktock.ogg")

    pause 1.0

    narrator "One full second has passed. Your mouth has just formed the shape required to exhale the 'H' in 'Hey there.' Whitney screams silently."

    show whitney at grayscale:
        xpos 0.5
        ease 0.05 xpos 1.5

    $ PlaySound("ticktock.ogg")

    pause 1.0

    narrator "It takes only one further second for Whitney to cross the breadth of the baseball field, traveling the one hundred and forty-eight feet to the dugout before sliding in on her stomach." 
    narrator "This puts her speed at approximately 101 Miles Per Hour, or 162 Kilometers Per Hour."
    narrator "Such a feat of speed would surely have broken every world record known to man, woman, and most Pokémon, had it been recorded." 
    narrator "Unfortunately, no-one present noticed, and this incredible feat will likely be attributed to comedic exaggeration forevermore."

    hide flashback 
    show baseball:
        matrixcolor IdentityMatrix()
    show shauna -talking2mouth:
        xpos 0.25 matrixcolor IdentityMatrix()
    hide whitney
    with Dissolve(2.0)

    red @talkingmouth "Hey{fast} there."
    red @happy "I don't think we've met?"

    $ BecomeNamed("Shauna")

    queue music "audio/music/vaniville.ogg"

    shauna @talkingmouth "{i}Bonjour!{/i} Hello, hello! You're [first_name], right? I remember. From the Battle Team? I'm Shauna."
    shauna @talking2mouth "Sorry, but did I just hear Whitney here?"

    red @happy "Yeah, she's..."

    pause 2.0

    red @noeyes shadow talking2mouth "She just left."

    shauna frownmouth @talking2mouth "Oh."

    pause 1.0

    red @talking2mouth "What, uh, what's your connection?"
    redmind @closedbrow sweat frownmouth "Please don't say--"

    shauna -frownmouth @talking2mouth "I'm her girlfriend."

    redmind @frownmouth "Damn it, Whitney."

    shauna @sadbrow talkingmouth "Well, maybe more of an ex-girlfriend. We haven't talked in a while."
    shauna @talking2mouth sad2brow "Buuuut we never actually broke up, so I guess I'm just trying to see where we stand, and maybe figure out what happened."
    shauna @sweat talkingmouth sadbrow "I've got some memories I can't really figure out, so I'd like to close them out with her."

    redmind @thinking "...You poor girl."

    shauna @talkingmouth "If you see her again, would you mind telling her that Shauna's looking for her?"

    red @talkingmouth "Of course, not a problem. I'll definitely say that."

    redmind @angrybrow frownmouth "And probably a lot more."

    shauna @happy "Thanks! She can usually find me in the Pokémon Groomer's club. Or taking Instructor O'Nare's Normal-type elective class."

    red @talkingmouth "I'll, uh, let her know."

    shauna @talkingmouth "Alrighty. Bye!"

    hide shauna with Dissolve(1.0)

    show whitney casual2 sadbrow frownmouth with dis:
        ypos 2.0 xpos 1.5 rotate -5
        ease 3.0 xanchor 0.5 yanchor 0.5 ypos 1.0 xpos 0.9

    pause 3.0

    stop music fadeout 1.5
    queue music "audio/music/goldenrod_start.ogg" noloop
    queue music "audio/music/goldenrod_loop.ogg"

    whitney @talkingmouth "Okay, so, I know that {i}sounds{/i} bad--"

    red @angrybrow talking2mouth "Whitney, I'm not going to lie, it's pretty bad. You need to--"

    pause 2.0

    red @confused "Did you just tie your shirt up?"

    whitney -frownmouth @sadbrow talkingmouth "It's a defense mechanism. I try to make myself look cuter before I get in trouble."

    red @sad2eyes angryeyebrows frownmouth "[ellipses]"

    whitney @sadbrow talkingmouth "I guess it didn't work?"

    redmind @sad2eyes angryeyebrows frownmouth lightblush "It did, but I absolutely {i}cannot{/i} let her know that."

    pause 1.0

    red @closedbrow talking2mouth "Come on. Get out of the dugout. You're being ridiculous."

    show whitney:
        xanchor 0.5 yanchor 0.5 ypos 1.0 xpos 0.9 rotate -5
        ease 1.5 xpos 0.5 yanchor 0.6 ypos 1.0 rotate 0

    pause 2.0

    red @talking2mouth "What happened?"

    whitney @talking2mouth "...Have you ever met someone that you thought made you perfect?"
    whitney @sad2eyes sadeyebrows talking2mouth "Like, you know there's parts of yourself you don't like. Then you meet someone that... doesn't make 'em go away, doesn't make you forget about them..."
    whitney @talkingmouth "But they seem like they're really going to try and help you with them? And, in the meantime, they don't care about your bumps, or if you're rough around the edges?"

    red @closedbrow talkingmouth "I know, more or less, what you're talking about."

    whitney @talking2mouth "Shauna was that for me."

    pause 1.0

    whitney @talking2mouth "And that's all she wanted to be."

    red @confused "What do you mean?"

    whitney @talking2mouth "I wasn't happy when I met her. There were parts of myself I needed to work on. Like, um, I... y'know, I was really sensitive about my parents being farmers."
    whitney @sad2eyes talking2mouth "And... when people made fun of them for that... I'd kinda... um. Destroy them."
    whitney @angrybrow talking2mouth "Those gossipers, I mean. Not my parents."

    pause 0.5

    whitney @surprised "Which, for the record, I realize was really bad and wrong of me! Like, I'm not proud of that at all!"

    red @unamusedbrow talking2mouth "Yeah, that, uh, sounds like a bad habit."

    whitney @talking2mouth "Shauna helped me become a better version of myself."

    red @talking2mouth unamusedbrow "And for that heinous crime, you ghosted her. When did you even meet? I know it can't have been here at Kobukan. Was it in Goldenrod?"

    whitney @talking2mouth "Summer Break 2003. I went to Kalos. That's when I got really into Fairy-types..."
    whitney @talking2mouth "We dated for three months, over the Summer. Then another three online. You know, video call dates."
    whitney @sad2eyes talking2mouth "But she stopped calling eventually."

    red @talking2mouth "{i}She{/i} stopped calling?"

    whitney angrybrow poutmouth @talking2mouth "Hey, why do you assume {i}I'm{/i} the one who stopped calling?"

    red @sadbrow talkingmouth "What you've told me about your past relationships kinda leans me in that direction."

    whitney "Hmph."

    whitney frownmouth @talking2mouth "Well, that's not true."
    whitney -angrybrow @sad2eyes talking2mouth "Mmmmostly. We might have stopped calling around the same time. Just, kinda... drifted out of contact."

    red @talking2mouth "For no reason? You just stopped calling each other? I'm not sure I can believe that."

    whitney @talking2mouth sad2eyes sadeyebrows "Look, she... she became really controlling, okay? She helped me fix a part of myself I didn't like. But she didn't want to stop there. She wanted to fix parts of me I was happy with--I was okay with."
    whitney @sadbrow talking2mouth "Like, she said that I shouldn't go into nursing. She said that I'd be a better Gym Leader than a nurse! Can you imagine, me, a Gym Leader? That would never work!"
    whitney @sadbrow talkingmouth "Honestly, given what Flan's told me about being a Gym Leader, I'm pretty sure I'd cry every time I lost."

    red @talking2mouth "...I guess. Maybe it's a bit on her, then. But I haven't gotten her side of the story, and {i}your{/i} side of the story isn't putting you in the best light."

    whitney @angrybrow frownmouth "[ellipses]"
    whitney @angrybrow talking2mouth "I'm telling the truth."

    red @talking2mouth "I believe you. I believed you from the very beginning, when you said you felt bad about how some of your past relationships worked out. And, after learning that one of your exes is actually {i}here{/i} at Kobukan, I..."

    red @sadbrow talkingmouth "Come on, Whitney. Think about this. This is the perfect opportunity to patch up one of your regrets, and--"

    whitney @angrybrow talking2mouth "Nonononono! You don't know what Shauna was like--or what I was like!"
    whitney @sadbrow talking2mouth "There are some things you can't just patch up, okay? The only thing I can do is[ellipses] {w=0.5}{nw}"
    extend sad2eyes sadeyebrows @talking2mouth "Move on."

    red @sadbrow talkingmouth "Whitney, I--"

    whitney angrybrow frownmouth @talking2mouth "Move on."

    pause 1.5

    red @closedbrow talking2mouth "Fine. You're right. I don't know what happened. I'll probably never know. And I don't want to push this so hard I push you away."
    red @talking2mouth "But if you're going to move on, that means you {i}really{/i} need to move on."
    red @talking2mouth "That means you need to {i}actually{/i} break up with Shauna. And, I dunno, maybe try dating someone you {i}aren't{/i} keeping near you for 'project' reasons."
    
    whitney angrybrow poutmouth "Hmph."
    whitney surprisedbrow @neutraleyes talking2mouth "If every time we hang out, you're just going to lecture me about being a better person, I'm not sure we should be hanging out."

    red @unamusedbrow talking2mouth "Whitney, how many relationships have you had that survived a minor argument?"

    whitney @angry "All of them! {w=0.5}{nw}"
    extend @angrybrow talking2mouth "Most of them. {w=0.5}{nw}" 
    extend @sad2eyes sadeyebrows talking2mouth "Some of them."

    red @unamusedbrow talking2mouth "Name one."

    whitney -poutmouth -surprisedbrow @playfuleyes unamusedeyebrows talking2mouth "Really? Okay, I'll admit, I appreciate you gave me a low bar, but I can totally do {i}one.{/i}"

    red @wince talking2mouth "Yeah, I realize now. Flannery. Duh."

    whitney @sad2eyes sadeyebrows talkingmouth "I guess you weren't really there for that, but we kinda had an argument after the elections. Well... it was less of an argument and more of me asking Flannery to come back after..."

    pause 1.0

    whitney surprisedbrow frownmouth "Hm."
    whitney @closedbrow talking2mouth "I... tried, for multiple days... to get her to forgive me."

    pause 1.5

    whitney confusedeyebrows @talking2mouth "Why did I do that?"

    red @sadbrow talkingmouth "Because you, like ninety-nine percent of the world's population, feel bad when someone you care about doesn't care about you."

    whitney -confusedeyebrows @talking2mouth "Sure, but, like, I've had girlfriends break up with me before, and I never tried to get them back."
    whitney @closedbrow sweat talking2mouth "In fact, I generally prefer to never think about them again."
    whitney @wince talking2mouth "But said in a way that doesn't make me sound clinically heartless."

    red @talking2mouth "I'm not sure there's a way to do that, but I get what you mean. You'd rather move on than handle whatever you left behind. You'd rather get something new then reclaim what you lost."
    red @talkingmouth sadbrow "You said you didn't like losing. And what you liked losing least is a friend. Some people would try to get back lost friends. But you... I guess you just cry and move on."

    whitney @talking2mouth "I guess... except this time I didn't."

    pause 1.0

    whitney @sad2eyes sadeyebrows talking2mouth "I guess... that's the difference between dating someone and actually being friends with someone."

    whitney -surprisedbrow @happy sweat "Wahahaha! I should've tried being friends with some of my girlfriends before! Maybe some of them would've worked out."

    red @talking2mouth "I'm horrified that this is apparently a realization for you."
    red @sadbrow talkingmouth "Look, if you go into a relationship looking for something--a partner, self-betterment, a project, or even just nighttime company--it won't work out, unless you broaden your aim {i}quickly.{/i}"
    red @talking2mouth "Being in a relationship with a person means you want that person. Not just a part of them, not just what they can do for you, not even what you can do for {i}them.{/i} Just them."

    pause 1.0

    red @talking2mouth "Like... uh, I dunno. Imagine all you were interested in, when it came to Flannery, was her fanfic-writing."

    whitney @talking2mouth "I'm not."

    red @sadbrow talkingmouth "It's a hypothetical. If that were the case, though, would you still be friends with her when you got what you wanted?"

    whitney angrybrow frownmouth @talking2mouth "Yes! Because she's awesome, patient, pretty, kind, and hilarious!"

    pause 2.0

    red @surprisedbrow frownmouth "[ellipses]"
    red @talking2mouth "Okay. Maybe I'm making a different point here than I thought I was."

    pause 1.0

    red @confused "Does Flannery know how you feel?"

    whitney -angrybrow @talking2mouth "...All I feel is that she's a good friend. A good, {i}straight{/i}, friend."

    red @closedbrow frownmouth "Hm."

    pause 1.5

    red @talkingmouth "Look, I think you should talk with Shauna. But I'm curious to see what this story is from both sides, so either way, I'm going to have a chat with her."

    whitney @surprised "What?"

    red @talking2mouth "C'mon, you're the school's number one gossipmonger. You know what it feels like to want to know about people's pasts, right?"

    whitney @talking2mouth "I... guess."
    whitney @sad2eyes talking2mouth "Just don't talk about me. I {i}can't{/i} talk to her, and if you make her want to talk to me, that'll just make things more awkward."

    redmind @unamusedbrow unamusedmouth "It's pretty clear that she already wants to talk to you."
    red @talking2mouth "Fine. I'll try to avoid the topic of our one connection."

    whitney @talking2mouth "Alright."

    pause 2.0

    red @talkingmouth "Hey, question."

    whitney @talkingmouth "Hm?"

    red @talkingmouth "Summer Break 2003 was the summer before you joined Kobukan. Have you dated anyone since then?"

    whitney @surprised "What?"
    whitney @angry "[first_name], no! Stop asking questions like that! I'm {i}not{/i} a monster! I'd definitely break up with Shauna officially before dating anyone new."

    pause 1.0

    whitney @sad2eyes sadeyebrows talking2mouth "{size=30}Maybe by text...{/size}"

    red surprisedbrow frownmouth "[ellipses]"
    red -surprisedbrow @unamusedbrow sweat talking2mouth "Right, I'm sorry, I think that's where I need to call it."
    red @closedbrow talking2mouth "I'm going to go talk to your ex. Whitney, I'm sorry, but--being brutally honest here--there are some things you need to work out. 'Moving on' isn't going to fix everything."
    red @talkingmouth sadbrow "I'm here to help you, if I can. But I'm not going to turn {i}you{/i} into a project and 'fix you.' I can give you tips, directions, but you're going to need to put in the legwork."

    whitney @talking2mouth "[ellipses]'Kay."

    pause 1.0

    whitney @sad2eyes talking2mouth "Um. Thanks."

    red @sadbrow talkingmouth "You can thank me by not dating anyone new until I have half a second to wrap my head around your past relationships."
    
    pause 0.5

    show whitney angrybrow poutmouth with dis

    red @unamusedbrow talking2mouth "You can also thank me by paying me. How much does a [bluecolor]relationship counselor{/color} earn per session, again?"

    whitney angry @angrybrow talking2mouth "If I was paying you, I'd expect you to be a lot nicer! Tough love doesn't work on me, you know--I'm very sensitive!"

    red @talking2mouth sweat closedbrow "Yeah, like an exposed nerve."

    whitney "Hey! You don't run away from me with a line like that! You come back here and--"

    scene blank2 with splitfadefast

    narrator "You quickly abscond from the baseball field before Whitney gets any creative ideas about what she could do with her baseball bat."

    $ RelationshipRankUp("Whitney", "Relationship Counselor", 2) 

return

label Whitney2Part2:
    $ AddEvent("Whitney", "Whitney2Part2")
    stop music fadeout 1.5
    queue music "Audio/Music/unwaveringheart.ogg"
    call clearscreens() from _call_clearscreens_235
    scene blank2 with splitfade

    show midnight at vspaz    

    python:
        timeOfDay = "Midnight"
        playercharacter = "Whitney"
        oldinventory = copy.copy(inventory)
        oldpersonalstats = copy.copy(personalstats)
        oldparty = copy.copy(playerparty)
        oldpersondex = copy.copy(persondex)
        oldclassstats = copy.copy(classstats)

        inventory = {
            Item.HowtoWinFriendsandInfluencePeople : 1,
            Item.MiltankCollar : 1,
            Item.Collar : 1,
            Item.NurseKit : 1,
            Item.Lipstick : 1,
            Item.Audinite : 1,
            Item.SocketedBat : 1 # FIX THIS: Change this when Whitney gets a key stone
        }
        personalstats = {
            "Charm" : 56,
            "Knowledge" : 13,
            "Courage" : -8,
            "Wit" : 34,
            "Patience" : 2
        }
        playerparty = GetTrainerTeam("Whitney")
        persondex = copy.deepcopy(defaultpersondex)
        
        #flannery
        persondex["Flannery"] = {"Named" : True, "Value" : 101 + oldpersondex["Whitney"]["Value"], "Contact": True, "Sex": Genders.Female, "Relationship": "Best Friend", "RelationshipRank": 0, "Events": [] }
        persondex[first_name] = {"Named" : True, "Value" : oldpersondex["Whitney"]["Value"], "Contact": True, "Sex": Genders.Male, "Relationship": "Project", "RelationshipRank": 0, "Events": [] }

        for key, value in defaultpersondex.items():
            if (key != "Flannery" and value["Nature"] != TrainerNature.Special):
                persondex[key] = value
                persondex[key]["Value"] = RandInt(1, 7)
                persondex[key]["Named"] = True
                persondex[key]["Relationship"] = RandomChoice(["Bud", "Pal", "Chum", "Mate"])

        classstats = { 
            "Normal" : min(100, AimLevel() + 5),
            "Fire" : 0,
            "Water" : 0,
            "Grass" : AimLevel() - 11,
            "Electric" : 7,
            "Ice" : 0,
            "Fighting" : 0,
            "Poison" : 0,
            "Ground" : 0,
            "Flying" : 12,
            "Psychic" : 0,
            "Bug" : 0,
            "Rock" : 0,
            "Ghost" : 0,
            "Dark" : 2,
            "Dragon" : 0,
            "Steel" : 0,
            "Fairy" : min(100, AimLevel() + 3)
        }

    pause 3.5

    scene whitneybedroomlightsoff 
    show screen currentdate
    with splitfade

    pause 2.0

    narrator "You cannot sleep."

    pause 1.0

    narrator "There are nights, occasionally, when you resent the spacious bed you have--when the soft pillows remind you only of how wide the space is between you and anyone else, and how {i}empty{/i} your bed is at the present."
    narrator "Not even the stitched smile of Alto, your stuffed Cleffa, is enough to keep away the dark thoughts right now."

    whitneymind night sleepwear hairdown @sad2eyes frownmouth "Hm... I wonder if Flannery's awake? I could go bother her."

    pause 1.0

    whitneymind @closedbrow frownmouth "...She'll definitely be awake. It's only barely after midnight. I can still hear her typing."

    pause 1.0

    whitneymind @angrybrow poutmouth "This sucks. I'm too pretty to be feeling bad about myself."
    whitneymind @angrybrow poutmouth "It's all that darned [first_name]'s fault. Gettin' all up in my beeswax about 'mending bridges' and 'making amends' and junk."

    pause 1.0

    whitneymind @sad2eyes frownmouth "Easy for him to say. People'd probably just forgive him for anything."
    whitneymind @sadeyebrows frownmouth "...I can't be forgiven for the stuff I've done, though."

    pause 1.0

    whitneymind @upeyes frownmouth "Hm... maybe I should take a shower? Just to pass the time?"

    pause 1.0

    whitneymind @closedbrow frownmouth "No, that might wake up Jasmine and Grusha."
    whitneymind @playfuleyes unamusedeyebrows unamusedmouth "I guess I'll just stare up at the ceiling until the guilt knocks me out, then."

    pause 1.0

    show ceilingmidnight with dis

    pause 2.0

    whitneymind @frownmouth "That ceiling light looks kinda like a boob."

    pause 2.0

    whitneymind @sad2eyes lightblush frownmouth "Well[ellipses] I guess I {i}could{/i}[ellipses]"

    show flannery sleepwear hairdown frownmouth sleepmask at night with Dissolve(1.0):
        xpos -0.5 xpos 0.0 yanchor 0.45 zoom 2.0 rotate 15
        ease 2.0 xpos 0.2

    pause 1.0

    flannery @talking2mouth "Whit?"

    show flannery surprised with dis
    show ceilingmidnight with vpunch

    whitney @surprised "AH!"

    scene blank2 with splitfadefast

    flannery sleepwear hairdown sleepmask night @angry "Hey, what's the big idea, screaming like that at this hour of the night?"

    whitney sleepwear hairdown night @sadbrow talkingmouth "Ah, ah, ah... I'm sorry, I just didn't expect to see you there!"
    whitney @sadbrow talkingmouth "Let me turn the lights on."

    scene whitneybedroom
    show flannery tiredmouth sleepwear sleepmask hairdown 
    with splitfade

    flannery @talking2mouth "Sorry. Guess I should've knocked."

    show flannery surprisedbrow frownmouth sleepwear sleepmask with dis:
        xpos 0.5 xzoom 1
        ease 0.5 xpos 0.75 xzoom -1

    show jasmine surprisedbrow frownmouth sleepwear:
        xpos -0.5 xzoom -1
        ease 0.5 xpos 0.5

    show grusha tired unamusedmouth unamusedeyebrows sleepwear noscarf:
        xpos -0.5 xzoom -1
        ease 0.5 xpos 0.25

    pause 0.3

    jasmine @talking2mouth "Is everyone alright? We heard the most awful screaming!"

    whitney sleepwear hairdown @sad2eyes angryeyebrows talking2mouth "{size=30}It wasn't {i}that{/i} bad...{/size}"
    whitney @happy sweat "I, uh, I just had a bit of a nightmare. Flan's here now, though, so I'm good."

    jasmine @sweat talking2mouth "Oh, thank goodness. I feared the worst. I wasn't sure, exactly what I could do, but I thought I should at least check on you."

    flannery -surprisedbrow -frownmouth @talking2mouth "Uh... thanks."

    pause 1.0

    whitney @angrybrow angrymouth "Hey, wait, Grusha! You can't be in here, you're a guy! Get out of here!"

    grusha @unamusedbrow talking2mouth "Really? But the sight of your granny blouse fills me with such lust and ecstasy."

    whitney @angrybrow talking2mouth "You jerk, this is not a granny blouse! It's cute and airy!"

    grusha @talkingmouth "{i}Mi abuela{/i} says the same thing."

    whitney @angrybrow poutmouth "Hmph!"
    whitney @angrybrow talking2mouth "Jasmine, take your femboy out of my bedroom!"

    jasmine closedbrow sweat talking2mouth "Ah... sorry. Come on, Grusha, let's leave these two alone."

    show jasmine:
        xpos 0.5
        ease 0.5 xpos -0.5

    grusha @closedbrow talking2mouth "{i}Adiós.{/i}"

    show grusha:
        xpos 0.25
        ease 0.5 xpos -0.5

    pause 2.0

    whitney @talking2mouth "Phew."

    pause 1.0

    show flannery surprisedbrow frownmouth with dis

    whitney @sadbrow talkingmouth "Flan, you're still wearing your sleep mask."

    show flannery:
        xpos 0.75
        ease 0.5 xpos 0.5

    flannery @talking2mouth "Yeah, it's a loose mesh. I can see through it well enough."

    flannery -surprisedbrow -frownmouth -sleepmask @talkingmouth "Sometimes when I know I'm going to be typing 'til the early morning, I just put it on. Blocks out the blue light from my laptop--I don't want to go blind before I'm thirty."

    pause 1.0

    flannery @tiredeyes talking2mouth "Of course, I was staring at computer screens eight hours a night for {i}years{/i} before I met you, so it might be too late at this point..."

    whitney @sadbrow talking2mouth "Sorry. Nurse course. We're contractually obligated to tell our friends they've been doing something that kills them for years."

    flannery @closedbrow talking2mouth "I still can't believe that soda's bad for you. I mean, it has bubbles. Bubbles are always good."

    whitney @angrybrow talkingmouth "You could've known that one by reading the back of the can!"

    flannery @happy "Whit, I'm a writer! You know we don't read."

    pause 1.0

    flannery @talking2mouth "Uh, so, you're still up."

    whitney @talking2mouth "Yup. You are too, it looks like. But that's not as surprising."

    pause 2.0

    flannery @talkingmouth "Scooch over. I wanna chat."

    whitney @surprisedbrow "Hm? Sure."

    show flannery:
        ypos 1.0 zoom 1.0 xzoom -1
        ease 0.5 ypos 1.2 zoom 1.3 xzoom 1

    pause 1.5

    show flannery sad2eyes with dis

    flannery frownmouth @closedbrow "Hmhmhm..."

    narrator "Flannery runs a hand through her hair. She seems distracted."

    flannery @lightblush frownmouth sad2eyes "[ellipses]"

    pause 1.0

    flannery @talkingmouth "I, uh, talked to [first_name] a while back."

    whitney @talking2mouth "So did I."

    flannery @talking2mouth "My meeting with him ended with me screaming at him as he ran away from me."

    pause 1.0

    whitney @sad2eyes talking2mouth "Same. He's really good at running, isn't he?"

    flannery @tiredeyes talking2mouth "Ugh... such a pain."

    whitney @angryeyebrows upeyes talking2mouth "Right?"

    $ ValueChange("Whitney", 3, -0.5, False, adjustoldpersondex=True)
    $ ValueChange("Flannery", 3, -0.5, True, adjustoldpersondex=True)

    narrator "Yours and Flannery's understanding of [first_name], borne out of mutual irritation, increased by three!"

    pause 2.0

    flannery @talking2mouth "He said some weird stuff when we were talking."
    flannery @talking2mouth "Like, he said... that I deserved to be angry. And that talking with someone... like an actual professional... might help."

    whitney @sadbrow talkingmouth "Flan, I've said that for years."

    flannery @sadbrow talkingmouth "Yeah. I know. Sorry. I just... I guess I needed to hear it from someone who wasn't you."

    whitneymind @noshine "...Oh."

    flannery @surprisedbrow talking2mouth "Uh, sorry! That's not what I meant to say! I... damn it, I'm so much better with words when I'm writing."
    flannery @talking2mouth "Whitney, what I'm trying to say is that... you're always there for me. You've always been there for me. And, so, I guess... when you look out for me... I didn't think much of it. I just accepted it."

    pause 1.0

    flannery lightblush @talking2mouth "But now [first_name]'s been chatting with me about some of this stuff, and I'm starting to realize what, uh, you know. What you actually do for me. And I just took it for granted before."
    flannery @happymouth sadbrow "I guess I'm here to apologize? And thank you. For everything you've done. I needed you to feel normal, but I'm not sure I ever really appreciated you for it, so..."
    flannery @closedbrow talking2mouth "Ah, damn it, I can't do this. Look, Whitney, you're my best friend, and I love you, alright?"
    flannery @talkingmouth "But don't misunderstand me, I--"

    whitney @sadbrow talkingmouth "I know, I know. Sororal love, friendly love, the kind of the love that doesn't let me take a peek at you in the shower."
    whitney @happy "You've told me before. And I've told {i}you{/i} before that I'm very disappointed, but I can live with it."

    flannery mediumblush @embarrassedmouth "[ellipses]"

    pause 2.0

    whitney @confused "Huh? Wait."

    pause 2.0

    whitneymind @feareyes surprisedeyebrows frownmouth "{size=40}Waitwaitwaitwaitwait!{/size} No, no, {i}no!{/i} Not now! This can't be happening! Not now! Abort mission! Abort mission, you stupid pink-haired nitwit! This is your best friend! {i}ABORT!{/i}"

    whitney @sweat happymouth closedbrow "Whatcha... whatcha talking about, there Flan?"

    flannery @closedbrow talking2mouth "Okay. Look, I'm not saying anything. I'm just... curious. But you know how [first_name] likes, you know, girls and boys?"

    whitneymind @feareyes surprisedeyebrows frownmouth "Do not encourage her, you idiot! You will literally ruin the one meaningful relationship you have! Do {i}not{/i} encourage her!"

    whitney @talking2mouth "Sure. It's pretty common. About 1%% of people, last time I checked."

    whitneymind @feareyes surprisedeyebrows frownmouth "Don't normalize it! Shame her! Tell her she's crazy! Tell her she's a freaking weirdo! Turn her down {i}right now!{/i}"

    flannery @talking2mouth "Okay. That's... I dunno, I guess one percent is still a lot, if it's {i}all{/i} people."
    flannery @upeyes talking2mouth "Well, look, maybe you've just had me writing a few too many Cynthia-themed fics, but I've been thinking, recently, and, you know, I've whined about how my dates haven't been going great, so..."

    pause 1.0

    flannery @talking2mouth "Uh. Do you get what I'm getting at?"

    whitneymind @feareyes surprisedeyebrows frownmouth "Say no. Say {i}no!{/i} If you care about Flannery even a little bit, say you have no idea!"

    show flannery heavyblush surprisedbrow frownmouth with dis

    whitney @talking2mouth "Um, yeah. You're thinking you might like girls, too?"

    flannery @closedbrow talking2mouth "I... that's... {size=30}ugh.{/size}"
    flannery -heavyblush -surprisedbrow -frownmouth @happy sweat "You know what, I've been up {i}way{/i} too long, and my head's going to weird places. I should get to bed. Maybe just finish up the scene I was working on, and--"

    whitneymind @feareyes surprisedeyebrows frownmouth "Good! Good, you can work with this. Just let her leave. She'll never mention it again, you know she won't--she'll be too embarrassed. Just say {i}nothing{/i}, and you can make this work."

    show flannery heavyblush surprisedbrow frownmouth with dis

    whitney @talking2mouth "Flan, are you confessing to me?"

    flannery @talkingmouth "{size=30}Nnnno.{/size} Maybe? I... am on the fence."

    whitney @talking2mouth "Okay."

    pause 1.0

    whitney @happy "Why're you on the fence?"

    flannery @sad2eyes talking2mouth "I... don't know. It's not that you're my best friend, or anything like that. I know we'd work. And it's not that you're not, like, perfect for me. I mean, I always thought you were cute. I just didn't think you were, you know, 'cute.'"
    flannery @sadeyebrows talkingmouth "But, like, how do I even know if I like girls? I mean, the old folks back at Lavaridge told me everything changes when you go to college, but I didn't think it would happen to {i}me.{/i}"
    flannery @closedbrow talking2mouth "And I kinda thought they meant I'd, like, start training Ice-types or something, not {i}this.{/i}"

    whitneymind @feareyes surprisedeyebrows frownmouth "Please. I'm begging you. Don't do this. Shut her down. We can keep her if you don't get greedy. You'll be cheating on Shauna, technically. Don't you care? Don't you care that you'll be a monster?"

    whitney @talkingmouth "Does it matter if you like girls? Because it sounds like you like me."
    whitney @winkbrow talkingmouth "And I'm a girl, in case ya didn't notice!"

    flannery -surprisedbrow @sad2eyes surprisedeyebrows talkingmouth "Yeah, I, uh, {i}definitely{/i} noticed."

    pause 2.0

    flannery @talking2mouth "How did you learn you liked girls?"

    whitney @frownmouth upeyes "Hm..."
    whitney @talking2mouth "I'm not sure I remember. I remember my first crush was Miss Priscilla, though. She was a teacher at Earl's Pokémon Academy in Violet City."
    whitney @happybrow talkingmouth "Maybe it was her?"

    whitneymind @feareyes surprisedeyebrows frownmouth "What are you doing, Whitney? [first_name] {i}specifically{/i} said you should avoid dating anyone new. You {i}specifically{/i} said you'd break up with Shauna before you dated anyone new."
    whitneymind @feareyes sadeyebrows frownmouth "This is your last chance."

    flannery @sweat closedbrow talking2mouth "Look, uh, I'm not smooth, or good with words unless I'm in front of a laptop, really. So I'm just going to be straight-up about this."

    pause 2.0

    flannery @talking2mouth "Can we make out? I need to know if this is real, and, uh, the only thing fanfic has taught me about relationships is that if we don't do this now, we'll be stuck will-they-won't-they-ing for, like, fifty chapters."

    whitneymind @feareyes sadeyebrows frownmouth "Please. No. {i}No.{/i}"

    show flannery sadbrow -frownmouth with dis

    whitney @sadbrow tears talkingmouth "Flan, I've waited {i}so{/i} long to hear you say that."

    call clearscreens() from _call_clearscreens_236
    scene blank with Dissolve(2.0)

    pause 2.0 

    scene blank2 with Dissolve(1.0)

    pause 1.0

    show secondwhitney angryeyebrows frownmouth noshine hairdown sleepwear shadow with Dissolve(2.0)

    secondwhitney @talking2mouth "Well done. That's another relationship you've ruined."

    whitney sleepwear hairdown @talking2mouth sad2eyes sadeyebrows "...I don't know. This one might work out."

    secondwhitney @talking2mouth "Get real. The only lasting relationship you've ever had is with your Miltank. Flannery's going to see how awful you really are by the second date."

    whitney @sadbrow frownmouth "[ellipses]"

    secondwhitney @sad2eyes talking2mouth "You could have stopped this. You could have kept someone for once. But you were too selfish."
    secondwhitney @talking2mouth "You don't deserve her. She doesn't deserve you. And I mean both of those in the most hurtful way."
    secondwhitney @talking2mouth "And because I'm you... I can be {i}very{/i} hurtful. Like Flannery's going to find out far too soon. It's only a matter of time."

    pause 1.0

    secondwhitney @talking2mouth "Tick-tock, Whitney Milton. Tick-tock."

    hide secondwhitney with Dissolve(5.0)

    pause 2.0

    $ PlaySound("sav.ogg")
    
    narrator "Guilt overtakes you as you feel your relationship with Flannery evolve from '{color=#0048ff}Best Friend{/color}' to '{color=#0048ff}Future Ex{/color}'!"

    python:
        inventory = oldinventory
        personalstats = oldpersonalstats
        playerparty = oldparty
        persondex = oldpersondex
        classstats = oldclassstats
        playercharacter = None

return
