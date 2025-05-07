label Rosa1:
    if (not IsBefore(1, 5, 2004)):
        $ persondex["Rosa"]["Events"].append("Level2SceneVer2")

    scene city_B
    with Dissolve(2.0)
    stop music fadeout 1.5
    queue music "audio/music/joinavenue_start.ogg" noloop
    queue music "audio/music/joinavenue_loop.ogg"

    show screen songsplash("Join Avenue", "Zame")

    $ renpy.music.play("Audio/bigcrowdloop.ogg", channel='crowd', loop=True, fadein=1.5)

    narrator "While walking through Inspira City, you suddenly hear a loud hubbub coming from around the corner."

    red @confusedeyebrows talking2mouth "Hm? What's happening here...?"

    show rosa sweat happy with Dissolve(2.0):
        ease 1.5 xpos 0.7
        ease 0.2 ypos 1.1
        ease 0.2 ypos 1.0
        ease 1.5 xpos 0.3
        ease 0.2 ypos 1.1
        ease 0.2 ypos 1.0
        ease 1.5 xpos 0.9
        ease 0.2 ypos 1.1
        ease 0.2 ypos 1.0
        ease 1.5 xpos 0.1
        ease 0.2 ypos 1.1
        ease 0.2 ypos 1.0
        ease 1.5 xpos 0.5
        ease 0.2 ypos 1.1
        ease 0.2 ypos 1.0
        repeat

    rosa "Hi! Rosa here, yep! Thank you so much, all of you! I really can't thank you enough for your support!"

    narrator "You suddenly spy Rosa, desperately dashing between a multitude of people who all seem to be clamoring for her attention."
    narrator "She signs autographs, notebooks, one young boy's shorts..."

    redmind @happy "Ah. Well, that's the problem with being a world-famous actress, I guess. Any time you step outside, you're going to have people clamoring for your attention."

    rosa surprised "Oh! That's--"

    redmind @thonk "Hm. It looks like she just saw me, and...?"

    show rosa:
        ease 0.5 xpos 0.5

    rosa -sweat -surprisedbrow -frownmouth -surprised @talkingmouth "Alright, everyone! Sorry to end it early, but the show's over!"
    rosa @star winkbrow talkingmouth "Got a big night of filming, so I really have to get my shopping done before then."
    rosa @happy "Bodyguard? Mind clearing a path?"

    redmind @confusedeyebrows frownmouth "Bodyguard? Really, me? Who would buy that?"

    $ renpy.music.stop(channel='crowd', fadeout=1.0)

    pause 1.0

    redmind @surprisedbrow frownmouth "Huh. Well, she {i}is{/i} convincing."
    redmind @thinking "Right, now, what would a bodyguard say in this situation...?"

    show rosa surprisedbrow frownmouth with dis

    red @angrybrow talking2mouth "Uh... right you are, miss. {nw}{w=0.5}"

    show rosa closedbrow sweat frownmouth with dis

    extend @angrybrow talking2mouth "You've got an appointment. {nw}{w=0.75}"

    show rosa winkeyes sadeyebrows sweat sadmouth with dis

    extend @angrybrow talking2mouth "With the director. {nw}{w=1.0}"

    show rosa -sweat vacanteyes vacantmouth with dis

    extend @angrybrow talking2mouth "Of movies."

    pause 2.0

    narrator "Upon the conclusion of your performance, Rosa's expression is one that can only be described as 'cringing.'"

    show rosa happybrow frownmouth sweat with dis

    pause 2.0

    $ renpy.music.play("Audio/bigcrowdloop.ogg", channel='crowd', loop=True)

    Character("Unruly Crowdmember") "\"Hey! That guy's not actually a bodyguard!\""
    Character("Brutally Honest Crowdmember") "\"Yeah! He's just a crappy actor!\""
    Character("Aghast Crowdmember") "\"Just... indescribably bad, actually.\""

    rosa -happybrow -frownmouth -sweat @happy "Hey, hey, guys! Alright, he's not my bodyguard, but he {i}is{/i} going to help me shop. So say goodbye to your favorite Rosa, and tune in for my next movie, {i}Broken Bird{/i}, coming to theaters near you soon!"

    $ PlaySound("class_groan.ogg", "crowd2")

    pause 1.0

    rosa @sadbrow talkingmouth "Aw, I love you guys, too! But I really need to leave now!"

    $ renpy.music.stop(channel='crowd', fadeout=1.0)

    narrator "It takes another ten minutes for Rosa to successfully disperse the crowd. You do your best to move them away, as well."

    rosa @happy "Phew. That was fun!"

    red @happy "Imagine it gets exhausting, though."

    rosa @happybrow talkingmouth "Nah, I'm totally used to it!"

    red @happy "Oh, good."

    pause 2.0

    rosa @sad "Aw, it's becoming an instinct. I actually meant to say 'yes, very.' But I'm so good at lying, I guess I've gotten to the point that I can't stop."
    rosa @surprised "Wait... oh!"
    rosa @happy "That's a super-fun idea for a character! I need to text this to my manager. Like, the heroine is forced to only tell lies? It'd probably work as a romantic comedy."
    rosa @closedbrow talking2mouth "Although, depending on how we play it out, we could probably have it work as a horror." 
    rosa @talkingmouth "Maybe we'll cut it two different ways--release the horror version in the East markets, and the comedy version in the Western markets?"

    red @talkingmouth "So, you're involved in the writing of your movies as well?"

    rosa @talkingmouth "Some of them. Usually just up to the ideation stage, though."

    red @confusedeyebrows talking2mouth "Ideation?"

    rosa @talkingmouth "Yeah, that's the first part of making a movie. Ideation is the stage where we think up what the script will be."
    rosa @happy "After that is writing, then pre-marketing, then shooting, then post-marketing, then market research!"

    red @closedbrow talking2mouth "Lots of markets there."

    rosa @happy sweat "Yeah, the business side of my industry gets pretty intense. I'm pretty lucky that I get to just work on movies I want to, though."
    rosa @talkingmouth "A lot of actresses don't get to do that. They end up just doing coffee commercials for ten years, and then they're too old to be leading ladies."

    red @closedbrow talking2mouth "Huh. How did you avoid that?"

    rosa @happy "Oh, it's kinda a long and boring story. Plus, you can read the whole thing on pretty much any of my wiki pages. You sure you want to hear it?"

    red @talkingmouth "You need to shop, right? Why don't you tell me while we do that?"

    rosa @surprised "Oh. Um, no, I don't need to shop at all. Actually, my manager has people do that for me."
    rosa @sad "Plus... it's difficult for me to figure out what I'm even allowed to buy. Most things are off-limits for me, since buying them could be seen as unsanctioned endorsement."

    red @confused "Damn. Rosa, uh, forgive me for asking, but... how do you even live like this? It sounds like you're not allowed to breathe air that hasn't been approved by Pokéstar Studios."

    rosa happy sweat "Oh, it's not a hassle! There aren't that many rules. And I can--"

    pause 1.0

    rosa -sweat angry "Gah, I did it again!"

    pause 1.0

    rosa -angry frownmouth @sad "Okay, no characters--just Rosa.{w=0.5} It's pretty hard sometimes. But I also get to do the best job ever, so I think it's a fair trade-off. And if it ever became too much, I could just leave."

    red @talkingmouth "You really love being an actress, then?"

    rosa -frownmouth @happy "I couldn't begin to imagine a better job. I love everything about it. The fame. The attention. The money."

    red @surprised "Uh... I was kinda expecting you to say something..."

    rosa @sad "More noble?"

    red @closedbrow talking2mouth "Maybe a little bit."

    rosa @happy "Hah! If I was going to be noble, I would have become a firefighter, instead of just playing one in {i}Heartburn{/i}!"
    rosa @talkingmouth "Of course, you know, if interviewers ask me why I do it, I'll say it's because I want to leave something for the next generation, but..."
    rosa @closedbrow talking2mouth "I mean, have you seen my films? {i}Every{/i} actor says they're doing it for the kids, but I'm not sure I want kids watching my movies."

    red @talkingmouth "I did watch one of your films, actually. Leaf recommended I watch, uh, {i}Provoked{/i}. She said it was required for cultural literacy."

    rosa @surprised "Oh, wow! She's a {i}really{/i} hardcore fan, then. With a strong stomach. I wonder how she even got a copy? A parents' organization started buying them up to destroy them, last I heard."

    red @confused "Yeah. About that. Uh, that one scene..."

    rosa @sadmouth "Yup, it was a prosthetic."

    red @closedbrow talking2mouth "Oh, phew."

    rosa @happy "Anyway, I don't want kids watching that, for obvious reasons. That's {i}one thing{/i} those parents got right."

    red @confusedeyebrows talking2mouth "So, this is kinda a weird question--and tell me if I'm getting too personal--but why are you at Kobukan?"
    red @closedbrow talking2mouth "It seems like everything about your time here is really restricting, and you're not getting the same experience as other students. So... why come?"

    pause 1.0

    rosa @sad "Well... that's kinda connected to how I became an actress."

    red @happy "Aw, shucks. Guess you {i}do{/i} have to tell me the full story, then."

    rosa @happy "Oh, well."
    rosa @talkingmouth "It kinda happened on accident."

    if (IsBefore(23, 7, 2005)):
        rosa @talkingmouth "I was just a regular, registered, Pokémon trainer five years ago. I was going on my adventure. I'd even gotten a gym badge."
        red @surprised "Wait, five years ago? Aren't you twenty?"
    else:
        rosa @talkingmouth "I was just a regular, registered, Pokémon trainer six years ago. I was going on my adventure. I'd even gotten a gym badge."
        red @surprised "Wait, six years ago? Aren't you twenty-one?"

    rosa @talkingmouth "Yeah, but Unova lets you become a trainer earlier."

    red @happy "Huh. Neat. How much earlier?"

    rosa @winkbrow sweat talking2mouth "Depends on the city. Driftveil lets {i}six-year-olds{/i} have Pokémon. But they're kind of a national embarrassment."
    rosa @closedbrow talking2mouth "Anyway, I got my badge, and was just about to face Roxie, the Virbank City Gym Leader. But she'd had some sort of big argument with her Dad, so I had to go patch that over for them."

    red @confused ".{w=0.5}.{w=0.5}.{w=0.5}Why?"

    rosa @happy "Roxie's a pretty intense rocker. When she gets angry, the only way to get it out of her system is to let her play her music for a few hours. I couldn't wait that long, so I tracked down her Dad."
    rosa @sad "Well, as it happened, her Dad was a frequent extra at Pokéstar Studios. He'd just got his first starring role, and..."

    show rosa happybrow frownmouth sweat with dis

    pause 1.0

    red @surprised "Eesh. That bad?"

    rosa -happybrow -frownmouth -sweat @talkingmouth "He wasn't going to be winning any Pokéys, I can tell you that much."
    rosa @closedbrow talking2mouth "He actually handled the disaster that was his first movie with dignity. Like, he was really good about it."
    rosa @sad "Anyway, I just happened to be in the area when the director, who I think was a bit frantic to get people to forget Pop Roxie's movie, grabbed me and asked if I wanted to be a star."

    red @surprised "Uh-oh."

    rosa @happy "Yeah, not a good start, is it? But I didn't have to do anything weird. They were actually shooting a music video there for Piers' song, 'Black2/White2.'"
    rosa @talkingmouth "They just wanted me to stand in the background, but a bunch of people on the internet saw my hair, and wanted to know who I was."

    red @closedbrow talking2mouth "Your hair?"

    rosa @happy "Yeah, it's kinda my trademark. I always wear it like this, even before I became known for wearing it like this."

    red @happy "Huh. What was the original reason?"

    rosa @happy "Mmm... that's a secret. And you won't find that on any of my wiki pages, either."

    red @talkingmouth "Ooh. Mysterious."

    rosa @talkingmouth "Anyway, I was about to go back to Virbank and challenge Roxie--the music video only took three days to shoot--but there were a few other jobs for extras at the studios, and since I was on-set, they just re-hired me."
    rosa @happy "And by the time those extra positions were done with, Piers' band's video page was just drowned in comments asking about 'Yankee Buns.'"
    rosa @talkingmouth "Well, Mr. Deeoh, the director, wanted to capitalize on my popularity, so he put me in a couple more videos. And then a few longer-form documentaries."
    rosa @happybrow sadmouth "Luckily, as I became more popular, I lost the 'Yankee Buns' nickname. But my Galarian fans still call me that, mostly. I try not to go to Galar too often."
    rosa @closedbrow talking2mouth "Anyway, after that, I started getting bigger and bigger roles, and..."
    rosa @sad "Well, now it's like this." 
    rosa @happy "It's Rosa! World-famous star, stealer of hearts, and putter of butts in seats!"

    pause 1.5

    rosa @talkingmouth "And that's my story." 
    rosa @happy sweat "But, for real, the people on my wikis do a much better job of telling it. I think the mods on MovieWiki are all English PhDs."

    red @talkingmouth "Maybe. But it's cool to hear it from the source."

    rosa @happy "Anyway, does that answer your question?"

    red @talking2mouth "Actually, it answered pretty much every question except the one I asked."

    rosa frownmouth surprisedbrow @surprised "Eh?"

    red @talkingmouth "Why are you {i}here?{/i} At Kobukan? You've explained how you got started as an actress, but, if anything, that just makes me wonder why you're trying to become a trainer even more."

    pause 1.0

    rosa -surprisedbrow -frownmouth @sideeyes sadmouth sadeyebrows "Well. I'm kinda... it's kinda embarrassing to admit this. But, um..."
    rosa @sadbrow sweat happymouth "I didn't mean to become so famous, and get all this attention and money and movies and stuff. It was kinda an accident."
    rosa @sadbrow sweat happymouth "Maybe it's silly of me, but in my head, I still think of myself as a trainer first, and an actress second. This whole... world-famous star thing... is just a sidequest. A scene that'll be cut in the biography of my life."

    pause 1.0

    red @sad "Wow."

    rosa @surprised "N-now, I'm not sure that, um, you know. That I can actually still be a trainer. I'm {i}very{/i} out of practice."
    rosa @happy "You, in gym class, were the first fight I've had in a long time where you were genuinely trying to beat me."
    rosa @talkingmouth "Honestly, I was kinda surprised when I hit your Pokémon, and they didn't fly back dramatically on invisible wires. I'm so used to pretending to be a trainer, that..."

    pause 2.0

    rosa @happy "Well. I'm here at Kobukan, because I want to find out for myself if I can still be a trainer." 
    rosa @closedbrow talking2mouth "Or if I've just flipped the script, and have to play this new role forever now."

    pause 1.0

    rosa @happy "Which wouldn't be a bad thing, of course! I mean, world-famous actress? You're never going to hear me complain about that."
    rosa @talkingmouth "It'd just be... {i}so{/i} awesome... if I could be both a brilliant trainer and a famous actress."

    red @talkingmouth "Well, we know it's possible."

    rosa @talkingmouth "Yeah. Diantha's a huge idol of mine. I'd die if I could meet her someday. Actually, I got into Psychic-types because of her Mega Gardevoir."
    rosa @happy "I'd say that's probably the {i}most{/i} iconic Pokémon in the world."

    red @happy "Guess I've got one more question, then, and I don't think the wiki will answer this one for me."

    rosa @happy "Oh, yeah? I think the guys on WikiHair know me better than I know myself, but go ahead."

    red @closedbrow talking2mouth "If you didn't actually come out here to shop, why {i}did{/i} you come out here?"

    rosa @sweat happybrow sadmouth "Oh. Um... actually, I was trying to get away from my fans. There's a big group of them back on campus, and..."
    rosa @happy sweat "I love them, of course. And everything they do. But every time I meet one, they act like it's the most important day of their life."
    rosa @happy "I tell them I'm really nothing special when I'm not in front of a green screen, but I also don't want to ruin their mental image of me, so..."
    rosa @talkingmouth "Sometimes it's nice to just get lost in the crowd once in a while."

    red @confused "Looks like you didn't do too well this time, though."

    rosa @closedbrow talking2mouth "It would probably be easier to blend in if I wore my hair differently..."
    rosa @angrybrow happymouth "But that's {i}just not happening.{/i}"

    red @happy "I bet your hair is the source of your powers. If your hair is cut, you lose your ability to act, right?"

    rosa @happy "Haha! Maybe!"
    rosa @closedbrow talking2mouth "Actually, my hair is pretty heavily insured. I think the studio actually {i}does{/i} think my hair is the source of my power."
    rosa @closedbrow talking2mouth "Hm... that'll mess with the timeskip design we had planned for {i}Broken Bird{/i}. But they can probably cut it out in post."

    pause 1.0

    red @happy "Hey, you know Leaf?"

    rosa @closedbrow talking2mouth "Hm? Oh, yeah. She's a big fan of mine, right?"

    red @talkingmouth "Yeah. Would it be alright if I told her about this conversation? I think she'd be really interested in hearing a personal story like this."

    rosa @happy "Oh, go ahead! And thanks for asking. A lot of people think that they can just tell anyone any part of a public figure's life."

    red @happy "Cool."

    $ ValueChange("Leaf", 3, -0.5)

    narrator "Later, you will tell Leaf about this encounter. Though it's a story she heard before, she grills you on the details for hours. You gained three points with Leaf!"

    pause 1.0

    rosa @happy "Hey, is it cool if I ask {i}you{/i} a question?"

    red @surprised "Sure. Be my guest. But what could a star like you want to ask someone like me?"

    rosa @sadmouth "When you were pretending to be my bodyguard... I've never seen someone so bad at acting."
    rosa @closedbrow talking2mouth "It's like... like you conveyed the idea that you were trying to trick people into thinking you were a bodyguard way more than you did the idea that you actually {i}were{/i} one."
    if (not IsBefore(1, 5, 2004)):
        rosa @closedbrow talking2mouth "Is that because of your empathy power? Or are you just a {i}really{/i} terrible actor?"

    red @angrybrow talking2mouth "Hey. Kinda offended. I was playing a role I had absolutely no rehearsal for. What would even make you think I could pretend to be a bodyguard, anyway?"

    rosa @talkingmouth "Well, you're tall, fit, and you've got a ferocious attack Pikachu on your heels."

    red @confused "Ferocious attack Pikachu?"

    if (IsBefore(1, 5, 2004)):
        $ renpy.music.play("Audio/Pokemon/pikachu_angry1.ogg", channel="altcry", loop=None)
        pikachu cocky "Pika!"
    else:
        $ renpy.music.play("Audio/Pokemon/pikachu_angry1.ogg", channel="altcry", loop=None)
        libpikachu angryeyes happymouth "Pika!"

    rosa @happy "Yep!"

    if (IsBefore(1, 5, 2004)):
        red @talkingmouth "Well. I guess I'm just really, really, {i}really{/i} bad at acting."

    else:
        red @talkingmouth "I think it might be, partially, my Frienergy. But I think the other part is... well, I'm just really, really, {i}really{/i} bad at acting."

    rosa @talkingmouth "I could give lessons!"

    red @surprisedeyes surprisedeyebrows talkingmouth "Really? Why? Of all the things that your manager could not let you do, that feels like it makes the most sense."

    rosa @sweat happy "Well... I might not be {i}allowed{/i} to, technically..."

    if (not IsBefore(1, 5, 2004)):
        rosa @talkingmouth "Maybe it's just part of your power, but I feel comfortable around you."
        
    else:
        rosa @talkingmouth "I just like talking with you."

    rosa @sweat happymouth "You don't freak out over me, which is... actually pretty rare. And pretty cool, too."

    red @talkingmouth "Maybe I'll start freaking as I watch more of your movies."

    rosa @closedbrow talking2mouth "Hope not!"

    red @talkingmouth "I gotta say, though. You're pretty bad at getting away from your fans."

    rosa @surprised "Huh?"

    red @talkingmouth "Because, at some point during this conversation, you turned me into one. Hope that doesn't ruin anything."

    rosa @sadbrow happymouth "Not at all. As long as you're not the weird kind of fan who obsesses over my feet." 

    red @closedbrow talking2mouth "As far as I can tell, I don't have a foot thing."

    rosa @happy "Then welcome to the show, {color=#0048ff}fanboy{/color}!"

    $ persondex["Rosa"]["Relationship"] = "Fanboy"
    $ persondex["Rosa"]["RelationshipRank"] = 1

    $ PlaySound("sav.ogg")

    narrator "Your heart shifts as you feel your relationship with Rosa evolve from '{color=#0048ff}Friend{/color}' to '{color=#0048ff}Fanboy{/color}'!"
    
    return

label Rosa2:
    if (not IsBefore(1, 5, 2004)):
        $ persondex["Rosa"]["Events"].append("Level2SceneVer2")

    scene library with Dissolve(2.0)
    stop music fadeout 1.5
    queue music "audio/music/joinavenue_start.ogg" noloop
    queue music "audio/music/joinavenue_loop.ogg"
    show screen songsplash("Join Avenue", "Zame")

    narrator "You're walking past the library, when, suddenly, you notice Rosa bent over a stack of books. Sweat is beading on her brow, and she seems extremely focused on something."

    show rosa sweat frownmouth angrybrow with dis

    redmind @surprisedbrow frownmouth "Huh."

    narrator "You watch her for a moment, as she intently writes something down on a paper, checks something in a book, and scratches her nose." 
    narrator "She fiddles unconsciously with her hair as she does so, and sticks a pen in her bun to hold it when not using it."

    red @happy "Heh. That's the Rosa you never get to see on-screen, I bet."

    pause 1.0

    show rosa surprisedbrow -sweat with dis

    red @happy "Yo."

    rosa -surprisedbrow -frownmouth @happy "Hiya, [first_name]! It's Rosa!~"

    red @closedbrow talkingmouth sweat "Yeah. I know."

    rosa @happy sweat "Sorry. Force of habit."

    red @talkingmouth "You look like you're pretty into something. Mind sharing?"

    rosa @talkingmouth "Not at all."

    show rosa surprisedbrow frownmouth:
        xpos 0.5
        ease 0.5 ypos 1.2 zoom 1.3

    narrator "You take a seat on the library bench next to Rosa."

    red @talkingmouth "Hm? Sorry, you look surprised. Did I...?"

    rosa @surprisedmouth "No, no, it's alright. I guess..."
    rosa -surprisedbrow frownmouth @sadbrow talkingmouth "I guess I just wasn't expecting that. Again, it's... you know, it's {i}wild{/i} to me that you don't know who 'Rosa' is."

    red @happy "Hey, I know who Rosa is. I'm sitting next to her."

    rosa @talkingmouth "Well, you're sitting next to {i}me.{/i} Sometimes I feel like Rosa and I are separate people, though."

    pause 1.0

    rosa -frownmouth @surprised "Ooh! That's a plot idea!"

    narrator "Rosa quickly scribbles something on a loose piece of paper next to her. Looking at the paper, you see it's titled 'movie ideas.'"

    narrator "There are a few bullet points, such as 'Hot Wet Bikini Summer 2: Hotter and Wetter', 'The Giant Woman! 5: An Even Bigger Woman', and 'Everlasting Memories 5: We killed F-00 {i}Again{/i}.'"

    redmind @confusedeyebrows frownmouth "Hm."

    rosa @surprised "Oh, no, don't look at that! That's just trash. I was working on my Bug class assignment."

    red @talkingmouth "You looked like you were {i}really{/i} into it."

    rosa @talking2mouth "Well... given how my Pokémon cast is pretty limited, I need to work especially hard on the ones I {i}can{/i} co-star with."

    $ scrimblobingus = GetTrainerTeam("Rosa", "Dottler")
    $ scrimbloid = scrimblobingus.GetId()
    $ scrimblonick = scrimblobingus.GetNickname()

    red @talkingmouth "I get that. Studying to beef up your [scrimblonick]?"

    rosa @talkingmouth "Or at least understand how he battles better. He's a bit relaxed, so I have to put in most of the effort."

    pause 1.0

    rosa @angry "A bit {i}too{/i} relaxed, I might add."

    $ sidemonnum = scrimbloid

    $ PlaySound("pokemon/cries/{}.mp3".format(scrimbloid))

    sidemon "[scrimblonick]..."

    pause 1.0

    rosa @sadbrow happymouth "I love him so much."

    red @happy "I get that. I love [pika_name], too."

    $ PlaySound("pokemon/pikachu_happy1.ogg")

    libpikachu "Pika!"

    rosa @talkingmouth "Anyway, what's up? I'm almost done with my studying, anyway. Want to chat about something?"

    red @talkingmouth "Sure. You got anything in mind?"

    rosa @sweat talkingmouth "Well... yeah, sure. But aren't you going to ask?"

    red @confusedeyebrows talkingmouth "Ask about what?"

    pause 1.0

    rosa @sadbrow sweat talking2mouth "Wait. I lied. I forgot about that."
    rosa @sadbrow talkingmouth "Um... that piece of paper wasn't actually trash. I thought you'd ask me about it, since I told such an obvious lie, but..."
    rosa @happy "Forgot I was an actress for a moment!"

    red @talking2mouth "It happens. Sometimes I forget I'm wearing a hat."

    rosa @surprisedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
    rosa @surprisedbrow frownmouth "Y-yes. Those {i}are{/i} similar concepts."

    red @happy "Right? Anyway, since it seems like you wanted me to ask, what was on that paper?"

    rosa @sadbrow surprisedmouth "It was... well, movie ideas."

    red @talkingmouth "Oh yeah?"

    rosa @talkingmouth "Yeah. I've been working with some of my producers, and they think they might be ready to let me begin my directorial debut soon."
    rosa @happy "That'll be {i}really{/i} exciting!"

    red @confused "Okay. I think I know what a director does, but just to make sure, could you explain what a directorial debut is?"

    rosa @talkingmouth "Of course. You only need to ask."
    rosa @happy "A directorial debut is the first movie that an actor acts as a director on. A lot of directors start out as actors, actually."
    rosa @talking2mouth "Not all of them, but a bunch do. Having been in the actor's shoes before helps the director tell the actors what to do more effectively."

    red @talkingmouth "So that paper was ideas for something you might want to direct?"

    rosa @talkingmouth "Yep."

    pause 1.0

    rosa @sweat talking2mouth "Well, {i}want{/i} to direct might be a bit of a strong phrase. I guess I think these are the movies that my producers might let me work on."
    rosa @sadbrow sadmouth "Of course, they're not really in the mood to give me anything else right now. I had to beg and bargain for a long time to even get to go to Kobukan, and my contracts there are {i}very{/i} specific about what I could do."

    pause 0.5

    rosa @angrybrow talking2mouth "Of course, even if I {i}sat{/i} in the director's seat, they'd still have all these rules..."
    rosa @sadbrow talking2mouth "I couldn't decide what the story is--that's the scriptwriter's job. I couldn't decide who to cast--that's the casting director's job."
    rosa frownmouth @sadbrow talking2mouth "Costuming is handled by the costuming department, visuals are the production designer's job, sound mixing is the sound designer's job."

    pause 0.5

    red @confused "Maybe I'm confused. What does the director do, then?"

    rosa @sweat talking2mouth "Well, {i}normally{/i}, all those other jobs would report to me. Um, the director."
    rosa @sadbrow talking2mouth "But given that I'm a first-time director, my producers would have me on an even tighter leash, and whatever I made would probably come out perfect and boring."

    pause 0.5

    rosa -frownmouth @talkingmouth "But I still want to do it. I'll never get to do what I {i}really{/i} want--to be an amazing Pokémon Trainer, to direct an awesome movie, to star alongside Diantha--unless I go through the tough stuff first."
    rosa @sweat sadbrow talkingmouth "And it's not like I'm being forced to work in the mines or anything. I'll still be paid a ridiculous amount to just listen to what the committee of producers say and relay their orders to everyone else."

    pause 0.5

    rosa @sadbrow talkingmouth "It's just kinda frustrating, though. I feel like I could make a {i}really{/i} good movie if they just let me have a bit more control. It's not like I want to do anything {i}but{/i} make them money, you know?"

    red @talking2mouth sadbrow "Yeah, I can imagine how that can be irritating. But then... why do you think they'd even let you direct in the first place?"

    rosa @sweat talkingmouth "They can slap 'The First Movie Directed by Rosa Whitley!' on the bottom of the movie poster."

    red @talking2mouth "Ah."

    rosa frownmouth @angry "And, you know, even {i}that{/i} is kind of insulting. It's like those big 'L' stickers they slap on the back of cars in Galar. Like, 'this is a learning director! Don't expect her to be good!'"

    red @talking2mouth "...I'm sorry."

    rosa -frownmouth @happy "Oh, you didn't have anything to do with it."
    rosa @sadbrow talkingmouth "Honestly, being able to just talk about these problems like this makes me feel a bit better."
    rosa @sadbrow talkingmouth "I guess I sound pretty ridiculous to you, though, right? These are seriously first-world problems."

    if (sawwallyellow):
        red @sadbrow talkingmouth "I heard someone say, once, that pain isn't a competition. The existence of others' hurt doesn't invalidate yours."

    else:
        red @sadbrow talkingmouth "I'll be real, I can't imagine being in a situation where I could even have this problem... but I know for sure that it's a real one."

    red @sadbrow talkingmouth "And I'm sorry you're going through it."

    rosa @sadbrow talkingmouth "...Thank you, [first_name]. That seriously means a lot."

    red @talkingmouth "Don't worry about it."

    pause 0.5

    red @talkingmouth "If you could direct {i}whatever{/i} you wanted... what would you make?"

    rosa @sadbrow talkingmouth "A difference."

    pause 0.5

    rosa @surprised "Oooh, good line. I need to write that down."

    pause 0.5

    rosa @talkingmouth "Anyway, I think I'd probably just direct a, like, a tv series. Something about investigating ancient myths and stories about aliens."
    rosa @talkingmouth "They're really silly, but I love those programs that try to figure out how, like, ancient structures were built. And maybe they reuse the 'it was aliens' bit too often, but..."
    rosa @happy "I don't know. Isn't it fun to imagine it {i}was{/i} aliens?"

    red @talkingmouth "Absolutely. Though I think it's also pretty cool to realize that even ancient people without Pokémon were capable of such incredible feats."

    rosa @talkingmouth "That's very true. I'd also want to talk about the feats of engineering that went into them."

    pause 1.0

    rosa @angrybrow talkingmouth "Hm. Didn't I promise to give you some lessons?"

    red @surprised "Oh, yeah! I forgot about that!"

    rosa @talkingmouth "Hm... let's go somewhere better for this, though. I'm going to want you to speak {i}loudly{/i}, and the library might not be the best place for this."

    red @talkingmouth "Sure, the gym?"

    rosa @talkingmouth "Way too crowded and noisy. I actually only went there that one time. That's when you and Leaf bumped into me."

    red @happy "Oh, I remember that? That was{w=0.5}.{w=0.5}.{w=0.5}."

    show rosa surprisedbrow frownmouth with dis

    red @shadow noshine noeyes talking2mouth "She made fun of my name.{fast}"

    rosa @surprised "Er... yes. But let's not hold a grudge!"

    scene blank2 with splitfade

    pause 1.0

    scene musicroom 
    show rosa
    with splitfade

    red @talkingmouth "The music room?"

    rosa @talkingmouth "Sure. The second-best acoustics in this school."

    red @confused "Second-best?"

    rosa @talkingmouth "Sure."

    red @talkingmouth "Why don't we go to the first?"

    rosa @talkingmouth sweat sadbrow "Well... the first is the auditorium, and..."

    show blank with Dissolve(1.0)

    show cherenshatefultruth behind blank at sepia
    show flashback behind blank at sepia 

    hide blank with Dissolve(2.0)

    show rosa sadbrow frownmouth

    pause 3.0

    hide cherenshatefultruth 
    hide flashback
    with Dissolve(3.0)

    red @talkingmouth sadbrow "I gotcha. Thanks, that's pretty considerate. I'm fine, though, it's not like the auditorium's off-limits or anything."

    rosa -frownmouth -sadbrow @talkingmouth "Well, we're here now. Let's just get started here."

    show rosa:
        xpos 0.5 zoom 1.0 ypos 1.0
        ease 0.75 xpos 0.75 zoom 0.8
        ease 0.2 ypos 0.9
        ease 0.2 ypos 1.0
        ease 0.2 ypos 0.9
        ease 0.2 ypos 1.0
        ease 1.0 xpos 0.25
        ease 0.2 ypos 0.9
        ease 0.2 ypos 1.0
        ease 0.2 ypos 0.9
        ease 0.2 ypos 1.0
        ease 0.75 xpos 0.5 zoom 1.0

    red @talkingmouth "Sure. So. Acting lessons. Now we...{w=0.5} what are you doing?"

    rosa @talkingmouth "Oh, just... checking for hidden cameras."

    red @surprised "What?!"

    rosa @talkingmouth "It's one of the first rules of being an actress. You gotta watch for hidden cameras everywhere."

    red @confused "What, from, like, pervs?"

    rosa @talkingmouth "Maybe. Or maybe just someone who thinks they could get me in some sort of trouble with my managers."
    rosa @sweat talkingmouth "Giving someone else an acting lesson, and not even asking for payment, is a bit... well, my managers wouldn't like it, you know?"

    red @confused "Geez."

    rosa @sadbrow talking2mouth "Of course, that doesn't mean that there aren't perverts around as well. Or people who want to sell to perverts, anyway."
    rosa @surprised "Did you know they make cameras built into shoes nowadays? They're used for getting upskirt shots."

    red @angrybrow talking2mouth "That's {i}sick.{/i}"

    rosa @sweat talkingmouth "Yeah, I can't trust anyone who wears black shoes anymore."
    rosa @talkingmouth "That's one of the reasons I wear this wetsuit all the time, when not in my school uniform, actually."

    pause 0.5

    rosa @sweat talkingmouth "It's almost kinda funny. I saw a thread once about one of my movies, and there were a bunch of pictures of me on-set, including one that was taken just outside my camper." 
    rosa @sadbrow sweat sadmouth "Don't know how the photographer got in. Anyway, I was actually taking my wetsuit off, then." 

    red @surprisedeyes confusedeyebrows surprisedmouth "What the {i}hell?!{/i}"

    rosa @talkingmouth "It wasn't that bad. All they could see was my back. Nothing worse than what I showed off in {i}Hot, Wet Bikini Summer.{/i} Anyway, the funny part is that the thread was full of people theorizing why I wear this wetsuit all the time."
    rosa @happy "I mean, like, have a bit of self-awareness, you know?"

    red @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    rosa frownmouth @surprised "What? What's wrong?"

    red @talking2mouth "That's awful, Rosa. I'm so sorry."

    rosa @sadbrow talkingmouth "What? No, it's a funny story. I wasn't trying to complain {i}again.{/i}"

    red @sad2eyes talkingmouth "...What did they think?"

    rosa @surprisedbrow frownmouth "Hm?"

    red @talkingmouth "You said they were theorizing why you wear your wetsuit all the time."

    rosa @talkingmouth "Oh, yeah. Well, the most {i}popular{/i} theory is that I'm trying to hide chest scars. From, um, 'enhancement' surgery."

    red @surprised "WHAT?!"

    rosa @happy "Ridiculous, right? Like, if I was going to get surgery, I'd be {i}way{/i} bigger!"

    pause 1.0

    red @talkingmouth "And these are your {i}fans{/i}?"

    rosa @sweat sadbrow talkingmouth "Well, yeah. I mean, you should see what my {i}haters{/i} do."

    pause 0.5

    redmind @sadbrow frownmouth "The life of an actress is horrifying."

    rosa @happy "But enough of that, really! You're here for an acting lesson, right?"

    red @talking2mouth "Y-yeah."
    red @happy "Yeah. Let's do it."

    rosa @talkingmouth "Okay. So, I need to know exactly what I'm working with here."
    rosa @talking2mouth "Here's a mock script I wrote up. Just read this out loud, okay?"

    red @talkingmouth "Sure. Um, what's my character?"

    rosa @talking2mouth "You're a small-town detective working with the international police. You and your partner, 'Kay, are hot on the trail of an alien life-form."
    rosa @angrybrow happymouth "But! Your scanner's just stopped working, and you're hopelessly lost in the woods! Out of the corner of your eye, you spot him--"
    rosa @angrybrow talkingmouth "Actual cannibal Brycen!"
    rosa @surprised "You're fearful, at first, but then you notice a certain tenderness to his eyes. A sort of romantic soul seeking desperately for a human connection."
    rosa @sadbrow talking2mouth "Yes, he eats hearts... but surely you can spare one for him? And perhaps open yourself up to receiving his?"
    rosa @talkingmouth "And then, as you draw closer together, the background becomes pink and white, and we hear church bells, as the scene fades into your wedding day, and..."

    red @unamusedeyebrows playfuleyes unamusedmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    rosa @sweat talking2mouth "Well, that's just background info. All that's important is that you're a middle-aged detective with a dead wife and a neglected daughter."

    red @talkingmouth "Sure. Alright, let me see here..."

    pause 0.5

    narrator "You begin to read the script. You try to deepen your voice, furrow your brow, and put everything you can into your interpretation of Detective Dodge Jammer."

    pause 0.5

    show rosa surprisedbrow with dis

    pause 0.5

    show rosa frownmouth with dis 

    pause 0.5

    show rosa sadbrow with dis

    pause 0.5

    show rosa sadmouth with dis

    pause 0.5

    narrator "Despite your best efforts, though, and despite the fact you feel like you're {i}really{/i} embodying the character, Rosa's expression just gets more and more distraught."

    red @talkingmouth "{i}There's a limit to coincidence. You're always there. Before my team, before my squad, before we know when or--"

    rosa @angry "{i}Cut!{/i}"

    pause 1.0

    red @happy "So, how soon should I prepare my speech to thank the academy?"

    rosa -sadbrow -sadmouth @sadbrow talkingmouth "Well, you know, I don't think that was the worst thing ever. There's something you can definitely do to hone that."

    red @talkingmouth "Oh, cool? I didn't think I did {i}that{/i} well, actually."

    pause 1.0

    rosa @sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."

    pause 1.0

    red @unamusedbrow talking2mouth "Oh. That was a lie."

    rosa @sadbrow talkingmouth "I'm sorry. You're... a {i}really{/i} bad actor."

    red @talkingmouth "Guess I shouldn't be expecting my own star on Virbank Boulevard anytime soon, then."

    rosa @talkingmouth "If it's any consolation, it might just be because of your power."

    red @talkingmouth sadbrow "Maybe. I don't know, though. It might just be that this is one thing I'm legitimately awful at."
    red @happy "Which, y'know, hey. Everyone has weak spots, right? It's like a Pokémon. Just 'cause Volcarona is super-weak to Rock-type attacks doesn't mean it's bad."

    rosa @talkingmouth "I guess. So, can you even lie?"

    red @talkingmouth "Well, yeah. I mean... 'The sky is red.'"

    rosa @talkingmouth "Hm. That's cheating, though. That's not a real lie, because I already know that's not true."
    rosa @sadbrow talking2mouth "Well... unless it's sunset, I guess."
    rosa @talkingmouth "Okay, tell me something that's not true that {i}doesn't{/i} depend on atmospheric conditions."

    menu:
        "My favorite sandwich is gravel and bleach.":
            $ AddEvent("Rosa", "SandwichLie")

        "I'm actually a Zoroark in human form.":
            $ AddEvent("Rosa", "ZoroarkLie")

        "I have, like, a gazillion dollars.":
            $ AddEvent("Rosa", "GazillionLie")

        "My Dad works at Nintendo.":
            $ AddEvent("Rosa", "NintendoLie")

    rosa @sweat talkingmouth "...C'mon, [first_name], be serious. Tell me something I might {i}actually{/i} believe."

    red @happy "Okay, okay. Sorry, just having a bit of fun."

    pause 0.5

    redmind @thinking "I say that, but... am I? Really? Why is it so hard for me to think up a convincing lie?"

    red @talkingmouth "Okay. A real lie this time. One that you might {i}actually{/i} believe."

    pause 1.0

    narrator "You wrack your brains, but the most you can come up with is..."

    red @confusedbrow talking2mouth "We're not alone?"

    rosa @talkingmouth "...Like, in this room? Or on this planet?"

    red @talkingmouth "I guess... both."

    rosa @sadbrow talking2mouth "[first_name].{w=0.5} Both of those are {i}true.{/i}"

    $ PlaySound("pokemon/pikachu_happy1.ogg")

    libpikachu "Pika!"

    narrator "[pika_name] gently nibbles your ear, as though to remind you that he'd been on your shoulder this whole time."

    red @sadbrow talking2mouth "Damn."
    red @happy "Well. I guess I just can't do it. I don't have it in me to be an actor. I'm sorry."

    rosa @talkingmouth "Oh, it's alright. Maybe there's something else I can teach you?"

    red @talkingmouth "Well, hold on a little bit. You {i}tried{/i} to teach me something here, right? And, admittedly, you might not have had the {i}most{/i} luck, but the effort was there."

    rosa @talkingmouth "Okay. What are you thinking?"

    red @talkingmouth "What if I try to teach you something in exchange?"

    rosa @talkingmouth "What do you mean?"

    if (classstats["Psychic"] >= AimLevel() - 3):
        red @talkingmouth "You're in the Psychic elective. I'm pretty good with Psychic, myself. Maybe we could trade notes. Study together."
    elif (classstats["Electric"] >= AimLevel() - 3):
        red @talkingmouth "You're in the Electric elective. I'm pretty good with Electric, myself. Maybe we could trade notes. Study together."
    elif (classstats["Bug"] >= AimLevel() - 3):
        red @talkingmouth "You're in the Bug elective. I'm pretty good with bugs, myself. Maybe we could trade notes. Study together."
    else:
        red @talkingmouth "I'm on the Kobukan Battle Team, you know? You're at a slight disadvantage, due to having your team hampered by your managers."

        red @happy "Maybe I could show you a bit of what we've learned in our Battle Team sessions."

    red @talkingmouth "And the next time some {i}creep{/i} tries to stick a camera where it doesn't belong, you can just whip out your [scrimblonick] and tell them to bug off."

    rosa @happy "Pun, nice!"

    rosa @talkingmouth "That sounds pretty fun. And we wouldn't have to hide away in a room like this, for that."

    red @talkingmouth "True."

    pause 0.5

    red @happy "Well, want to get started?"

    rosa @talkingmouth "Huh?"

    red @talkingmouth "We can go to the Battle Hall right now. As a Battle Team member, I can use it any time, even if there are other students present."

    rosa @talkingmouth "Well... okay! Sure!"

    scene blank2 with splitfade 

    pause 1.0

    if ("Janine" in GetStudents()):
        scene stadium_empty
        show janine:
            xpos 0.33
        show rosa:
            xpos 0.66
        with splitfade

        red @talkingmouth "Hey, Janine!"

        janine @talking2mouth "Hey."

        pause 0.5

        janine @surprised "Hm? Rosa?"

        rosa @talkingmouth "Hi! You must be a fan?"

        janine smilemouth @talking2mouth "A little bit. I liked {i}Samurai vs. Ninja: The Ultimate Kapowdown!!!{/i}"
        janine @smirkmouth "I'm mostly just surprised to see [first_name] with someone so famous hanging on his arm."

        rosa @sweat sadbrow talkingmouth "That's not exactly what's happening."

        janine @talking2mouth "Just having fun hanging out together, then?"

        red @talkingmouth "Yeah, pretty much."
        red @surprised "Oh, wait--we were going to use the Battle Hall. Do you need it for anything?"

        janine @talking2mouth "Nah. Go ahead."
        janine @talking2mouth "My Dad tells me that you're one of his favorite students, Rosa. That nobody knows the art of misdirection better than you."
        janine @talkingmouth "Maybe consider taking his class one day. It'd mean a lot to him."

        pause 0.5

        janine @talkingmouth "I'm excited to see what you can do."

        pause 1.0

        rosa @talkingmouth "Oh! You're... going to stay here?"

        if (GetRelationshipRank("Janine") >= 1 and HasEvent("Janine", "Domming")):
            janine @talking2mouth "Yeah. It's my battle hall. And you're battling {i}my{/i}..."

            narrator "Janine gives you a curious look."

            janine @talkingmouth "...{i}Battler.{/i}"

            redmind @surprisedbrow frownmouth lightblush "She was totally considering saying 'good boy' there, wasn't she?"

        else:
            janine @talking2mouth "Yeah. It's my battle hall. And you're battling {i}my{/i} battler."

        rosa @talkingmouth "That's fair."

        janine @smirkmouth "Be careful. She's got a level 200 Charizard, you know."

        rosa @talkingmouth "Hah, not really! That was only in {i}Leon: An Undefeatable Story{/i}."

        red @talkingmouth "I'm not familiar with that one?"

        rosa @talkingmouth "I played Leon's childhood friend."
        rosa @surprised "Actually, come to think of it, I think my character was based on Sonia."
        rosa @talking2mouth "I wonder if Sonia got royalties for that movie...?"

        show rosa surprisedbrow frownmouth with dis

        janine @talking2mouth "Battle."

        rosa @talkingmouth "Oop! Okay! Sorry, Miss!"

        hide janine with dis

    else:
        scene stadium_empty 
        show side rosa 
        with splitfade

        red @talkingmouth "Ready?"

        rosa @angrybrow talking2mouth "That's what I should be asking {i}you!{/i}"

        red @talkingmouth "I was born ready!"

        pause 0.5

        red @talkingmouth "Well, actually, I was born naked, screaming, and crying, so I guess that wouldn't make me ready for a lot of things, but it would make me {i}very{/i} ready for a few particular circumstances."

        rosa @angrybrow talkingmouth "Well, when I beat you, that's what you'll end up as!"

        red @confused "...Huh."

    python:
        trainer1 = MakeRed()
        trainer2 = Trainer("rosa", TrainerType.Enemy, GetTrainerTeam("Rosa"))

    call Battle([trainer1, trainer2]) from _call_Battle_123
    $ battlehistory["Rosa3"] = _return

    queue music "audio/music/joinavenue_start.ogg" noloop
    queue music "audio/music/joinavenue_loop.ogg"

    show rosa with dis:
        xpos 0.5

    if (WonBattle("Rosa3")):
        rosa @angrybrow talking2mouth "Aw, poo!"

        pause 0.5

        red @happy "Hey, it was close. I can see a few points where you can improve, though."

        $ ValueChange("Rosa", 3, 0.5)

        rosa @happy "Great! That's exactly what I was looking for!"
        rosa @talkingmouth "What've you got for me?"

    else:
        rosa @surprised "Wwwwait. I just won? I just {i}won?{/i} Against you?"

        red @closedbrow sweat talking2mouth "Well... that's a bit embarrassing. Yeah. I mean, I see a couple points where you could improve, but you still kicked my ass, so fair play."

        rosa @happy "Great! I guess I'm not as far behind as I thought!"
        rosa @talkingmouth "So, what've you got for me?"

    red @talkingmouth "It's the way you command your Pokémon. You almost seem... uh... uncertain. Like you're not sure if they know how to do what you're telling them to."

    rosa @sadbrow talking2mouth "Hm... I get it."

    red @happy "Pokémon are super-responsive to their trainers' feelings, you know?"
    red @talkingmouth "If you're not sure if your Pokémon can do something, your Pokémon won't know if they can, either."

    rosa @talkingmouth "But... what if I genuinely don't know if my Pokémon can do something? Like, how should I command them, then?"

    red @winkeyes talkingmouth "Lie."

    rosa @surprised "Oh!"

    red @happy "Or, you know, fake it 'til you make it. Whichever way you want to phrase it."

    rosa @talkingmouth "Okay. I can {i}definitely{/i} do that."

    red @talkingmouth "Cool. Let's heal up our guys and try again."

    scene blank2 with splitfade

    narrator "You continue to battle with Rosa. Gradually, her command over her Pokémon gets a bit better."
    
    if ("Janine" in GetStudents() and WonBattle("Rosa3")):
        narrator "You also notice that Janine nods approvingly every time you mark up a win, which you continue to do."

        $ ValueChange("Janine", 3, 0.5)

    narrator "Eventually, Janine leaves the Battle Hall, leaving you two alone."

    pause 1.0

    narrator "Alone, you assume, until you hear..."

    $ PlaySound("photo.ogg")

    show stadium_empty
    show rosa surprisedbrow frownmouth
    with vpunch

    pause 1.0

    red @angry "Hey! Who's there?!"

    narrator "There's no response, but you hear the sound of someone scurrying amongst the bleachers."

    rosa "Woah! What's up?"

    red @surprised "Didn't you hear that? Someone's taking pictures!"

    rosa @sweat talking2mouth "Oh."

    rosa @sadbrow sweat talkingmouth "I... kinda have to pick my battles, you know? I'm not going to chase down everyone who takes a picture of me."
    rosa @talking2mouth "My entire {i}job{/i} is having videos taken of me, so it'd be a bit hypocritical to-"

    red @talking2mouth "No! No, it wouldn't. You {i}agree{/i} to have videos taken of you, you know what's going to be done with those videos, and you get paid ridiculous amounts {i}for{/i} those videos."
    red @sad2eyes angryeyebrows talking2mouth "{i}This{/i} is... I don't know what this is, but it's not {i}that{/i}, and I don't like it."

    pause 1.0

    rosa -surprisedbrow -frownmouth -surprised sadbrow @happymouth "That's really sweet, [first_name]."

    red @poutmouth sad2eyes "...Mrmph."

    rosa @talkingmouth "Don't worry about it, though. All that picture got was me battling you with my [scrimblonick]. It's not like there's anything scandalous there."

    red @talkingmouth "...I guess."

    rosa -sadbrow @talkingmouth "I'm still wearing all my clothes this time, after all. And battling isn't against my contracts. I was recording the footage, just like they asked. Everything's fine, assuming..."

    pause 0.5

    rosa @talking2mouth "...Hm."

    red @confused "Assuming?"

    rosa @sweat talkingmouth "Well... you know what, never mind. I'm sure it's nothing."
    rosa @happy "Thanks a lot, [first_name]. I'll talk to you later, alright?"

    red @talking2mouth "...Alright."

    pause 1.0

    rosa @talkingmouth "You know, it's kind of funny. When I asked you to be my bodyguard, you were absolutely {i}awful{/i} at pretending to be one. But when you heard that camera flash go off..."
    rosa happy "Well, you looked like a {i}real{/i} one, then! Maybe you'd make a better real [bluecolor]bodyguard{/color} than a fake one!"

    hide rosa with dis

    $ persondex["Rosa"]["Relationship"] = "Bodyguard"
    $ persondex["Rosa"]["RelationshipRank"] = 2

    $ PlaySound("sav.ogg")

    narrator "Your heart shifts as you feel your relationship with Rosa evolve from '{color=#0048ff}Fanboy{/color}' to '{color=#0048ff}Bodyguard{/color}'!"
    
    return

label Rosa3:
    stop music fadeout 1.5
    queue music "audio/music/joinavenue_start.ogg" noloop
    queue music "audio/music/joinavenue_loop.ogg"
    show screen songsplash("Join Avenue", "Zame")
    scene mall 
    show rosa streetwear
    with Dissolve(2.0)

    narrator "You're currently in Inspira City, nearing the end of today's unofficial 'bodyguard' duties for Rosa."
    narrator "As honorary manager of Join Avenue, Rosa is frequently expected to make public appearances, wave at the salesclerks, kiss some cash registers..."
    narrator "And you've taken it upon yourself to make sure that creeper guys with cameras and body pillows stay {i}away{/i} from her while she does so."

    rosa @happy sweat "You know, ever since you've started coming with me to these mall visits, they feel like they've gone {i}so{/i} much faster."

    red @talkingmouth "Oh, yeah? I hope that's a good sign."

    rosa @talkingmouth "Totally. Time flies when you're having fun, right?"
    rosa @happy "And whenever we're together, I have a {i}lot{/i} of fun."

    redmind @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
    redmind @thinking "Rosa's been saying a lot of stuff like that. I'm pretty sure she likes me, but..."

    show rosa surprisedbrow sweat with dis

    $ PlaySound("vibrate.ogg")

    pause 1.0

    redmind @happy "But if sorting that out takes more than thirty seconds, it'll be a no-go. She doesn't have thirty seconds without {i}someone{/i} calling her, or needing her eyes on something."

    rosa @happy "Sorry! Rosa's gotta take this. But she'll be back after this commercial break!"

    red @closedbrow talkingmouth "Yeah, yeah. I'll stay tuned."

    show rosa:
        xpos 0.5
        ease 0.5 xpos 1.2

    pause 0.3

    redmind @sadbrow frownmouth "Well, even if we just stay as friends, because she doesn't have time for anything else, I'm fine with that. She's a pretty great one, after all."

    rosa @talkingmouth "{size=30}Hm? Yes, the marketable plushies. Didn't I already...? Oh, a live signing? Yes, I think I can do that. When? Oh, that's pretty busy, but I'll try to move some of my schedule around for it.{/size}"

    redmind @confusedeyebrows frownmouth "Man. Don't those guys get enough money out of her? They gotta slap her face on a plushy, too?"

    pause 1.0

    redmind @poutmouth sad2eyes "I wonder how much they cost...?"

    narrator "You've begun to understand Leaf's obsession with Rosa. You have {i}also{/i} fallen fully under her sway, at this point... though you'd wager you still know less about her than the moderators on her MovieWiki page."

    show rosa:
        xpos 1.2
        ease 0.5 xpos 0.5

    pause 0.3

    rosa -surprisedbrow -sweat @talkingmouth "Alright, I'm back! Sorry about that. Should be the last one for today."

    red @happy "Seven."

    rosa angrybrow frownmouth @angry "Agh! Seven? What the heck?!"

    narrator "Another habit the two of you have picked up is pointing out when Rosa tells inadvertent white lies--at her request."

    rosa -angrybrow -frownmouth @closedbrow sweat talking2mouth "I don't even know why I said that. Of course it's not going to be the last one today."

    red @talkingmouth "You're just trying to make the people around you feel comfortable. It's really not that bad a thing."

    rosa @sadbrow talkingmouth "It {i}becomes{/i} a bad thing if I end up telling people I'm fine, or {i}something{/i} is fine, all the time, though... even if it's not."
    rosa @closedbrow talking2mouth "Nessa says I should complain more."

    if (GetRelationshipRank("Nessa") > 0):
        red @talkingmouth "Hah. Yeah, that sounds a lot like her."

        rosa @sadbrow talkingmouth "The actual word she said wasn't 'complaining'... but I'm not allowed to say the {i}actual{/i} word she said."

    else:
        red @talkingmouth "Was the exact word she used 'complaining'?"

        rosa @closedbrow talking2mouth "No, but I'm not allowed to say the {i}actual{/i} word she said."

    red @winkbrow talkingmouth "Pretty sure I get it."

    pause 0.5

    red @talkingmouth "Alright. Ready to go back?"

    rosa @talkingmouth "Yeah, I think so. If we take the backstreet past Fourth and East, we might be able to get to campus without going on any main roads."

    red @talkingmouth "Sounds like a plan."

    scene residentialstreet with splitfade

    pause 0.5
    
    show rosa streetwear with Dissolve(1.0)

    red @talkingmouth "...And what about your favorite {i}action{/i} movie you were in? It's gotta be one of the {i}Riolu Girl{/i}s, right?"

    rosa @sadbrow talkingmouth "Don't let anyone know I said this, but... honestly, I think the {i}Riolu Girl{/i} movies are a bit overrated."

    red @surprised "No way!"

    rosa @happy "I mean, Riolu Girl is a {i}great{/i} character. I'm not denying that. But she... you know, she doesn't really ever get the chance to show off everything that's in the character bio they gave me, you know?"
    rosa @surprised "Like, did you know the entire reason she doesn't evolve her Riolu is because her father is evil, and he uses a Lucario, and if she evolves her Riolu, then its Fighting-type moves will be Super-Effective on {i}her{/i} Lucario?"
    rosa @talking2mouth "Like, that shows actual strategy. It shows tactical thinking." 
    rosa @angrybrow happymouth "But it {i}also{/i} shows how obsessed she is with beating her father, specifically, because having a Riolu instead of a Lucario is a disadvantage in almost every other situation!"
    rosa sideeyes frownmouth @sadbrow talkingmouth "That's a really interesting character flaw."

    pause 1.0

    rosa -sideeyes -frownmouth @talkingmouth "But I never get to show that side of her. I just have to stand there in that skintight suit with the boob window and yell about justice."
    rosa @closedbrow sweat talkingmouth "I swear there's some disconnect between the writer and the director--sometimes I wonder if they actually care about the character, or just the flashy stunts and the name recognition I bring."
    rosa @sadbrow talkingmouth "...And I don't do my own stunts, so it's really just the name. I {i}swear{/i} I could do a conflicted character well, though."

    red @happy "I know you could. And {i}have{/i}. In {i}Everlasting Memories{/i}, when Manuelo betrayed you... you broke hearts all across Unova."

    rosa @talkingmouth "Yeah... but the {i}real{/i} emotional lead of that series was F-00. And he was completely CGI."

    pause 0.5

    rosa @poutsadmouth "...Did you know that Iono voiced him?"

    red @surprised "Who?"#FIX THIS

    rosa @talkingmouth "She's a streamer from Paldea."

    red @confused "Not an actress?"

    rosa @closedbrow talking2mouth "Yeah... she didn't have any voice acting experience, but... you know, name recognition."
    rosa @happy "But she was great. People loved F-00. It's just that, {i}most{/i} of the time, when a celebrity famous for something other than their acting ability is hired to act, it doesn't work out well."
    rosa @sadbrow talkingmouth "And then there's me. Being hired for everything {i}except{/i} my acting ability."

    pause 0.5

    red @talkingmouth "Well... you'll be able to create the character {i}you{/i} want to play when Pokéstar lets you make your directorial debut, right?"

    rosa @talkingmouth "Yeah. Shouldn't be a long time from now. I've been getting a {i}lot{/i} of good feedback from my managers. I think I'm just one good PR moment away from getting that chance."
    rosa @sadbrow talkingmouth "Of course, they've been looking for an excuse to cancel my debut, but I was smart. I got their agreements down on paper. It's in my contracts!"
    rosa @sideeyes talkingmouth sweat "That's what all these years of toeing the line and following the rules have been for. So I can {i}finally{/i} make something {i}really{/i} worth being in."

    pause 0.5

    rosa @closedbrow talkingmouth "Oh, I must sound {i}so{/i} spoiled, don't I? 'I had to make millions of Pokédollars for really light work for {i}years{/i} before I was allowed to make even more money doing the exact same thing!'"

    red @sadbrow talking2mouth "A tragedy beyond compare, truly."

    rosa surprisedbrow frownmouth @sadbrow talkingmouth "I think I'll go cry into a bathtub full of money about it."

    red @surprised "You have one of those?!"

    rosa -surprisedbrow -frownmouth @happy "No, silly! That was a joke!"

    red @talkingmouth "Well, that's gotta be proof you're the best actor out there, to say that with a straight face. I totally believed you."

    rosa @angrybrow talkingmouth "That might say more about you than it does about me."

    red @angrybrow talkingmouth "Woah there. Don't forget I'm on the Battle Team, while you only play the part."
    red @winkbrow talkingmouth "Remember what happened when we battled that time in the Battle Hall?"

    if (WonBattle("Rosa3")):
        rosa @lightblush sideeyes poutsadmouth "Hmph! It was close. I {i}almost{/i} won..."

    else:
        rosa @happy "Of course! I {i}won{/i} that one."

        red @sad2eyes talking2mouth "It was close."

        rosa @talkingmouth "No way! I totally dominated that fight, from Act 1 to the Finale!"

    show rosa surprisedbrow frownmouth with dis

    red @winkbrow talkingmouth "Eight." 

    rosa @angrybrow surprisedmouth "Y-you...! That wasn't a lie! That one was {i}not{/i} a lie!"

    red @happy "Sure, tell yourself that."

    rosa happy "Hahaha!"

    pause 1.0

    show rosa -happy with dis

    pause 1.5

    red @talkingmouth "Something up?"

    rosa @talkingmouth "Oh... just thinking."

    red @talkingmouth "Anything in particular?"

    rosa @sideeyes talking2mouth "Well... um. Sort of."

    pause 1.0

    rosa surprisedbrow frownmouth mediumblush @closedbrow talking2mouth "In, um, my industry, 'us' is a pretty loaded word, but--"

    $ PlaySound("vibrate.ogg")

    pause 1.0

    rosa -surprisedbrow -frownmouth lightblush @happy sweat "Oops! Sorry. Looks like I've gotta take this."

    red @sweat closedbrow talkingmouth "Of course. Go ahead."

    show rosa closedbrow frownmouth with dis:
        xpos 0.5
        pause 1.0
        ease 0.5 xpos -0.2

    rosa "{size=30}Mmhm. Yep. Okay. Mmhm. Can I-- no? Okay, so...{/size}"

    pause 1.5

    narrator "While Rosa takes the call, you entertain yourself by taking a closer look at the houses nearby." 
    narrator "This is an unfamiliar area--though you and Rosa have taken it a couple times before to avoid main streets on the way back from Inspira, but unfamiliar areas have started to make you a bit uncomfortable."

    redmind @sad2brow frownmouth "She isn't wearing her wetsuit right now, after all..."

    stop music fadeout 1.5

    scene musicroom at sepia
    show flashback
    with dis

    $ renpy.pause(1.0, hard=True)

    show rosa at sepia with dis

    rosa @sadbrow talking2mouth "Of course, that doesn't mean that there aren't perverts around as well. Or people who want to sell to perverts, anyway."
    rosa @surprised "Did you know they make cameras built into shoes nowadays? They're used for getting upskirt shots."

    red sepia @angrybrow talking2mouth "That's {i}sick.{/i}"

    rosa @sweat talkingmouth "Yeah, I can't trust anyone who wears black shoes anymore."
    rosa @talkingmouth "That's one of the reasons I wear this wetsuit all the time, when not in my school uniform, actually."

    show blank with splitfade

    scene residentialstreet
    show raihan:
        ypos 1.7 zoom 2.0
    with Dissolve(2.0)

    redmind @thinking "It's bad enough that Rosa has to even {i}think{/i} about that, nevermind that I do now, too."
    redmind @thinking "But if my thinking about it can help ease her worries even a bit, then..."

    pause 1.0

    show residentialstreet with vpunch

    show raihan surprisedbrow frownmouth:
        ypos 1.7 zoom 2.0
        ease 0.2 ypos 1.0 zoom 1.0

    red @surprised "Gah!"

    rosa streetwear @sadbrow talking2mouth "Shh! {size=30}On a call!{/size}"

    red @closedbrow talking2mouth "{size=30}Sorry.{/size}"

    red @confused "Raihan, what're you doing here?"

    $ renpy.music.queue("Audio/Music/brandnewworld.ogg", channel='music', loop=True, fadein=1.5, tight=None)

    raihan -surprisedbrow -frownmouth -surprised @happy "Ah, sorry, mate, got ahead of myself a bit. I saw some guy walking into a backstreet with our Rosa, and got myself all worked up, you know?"
    raihan @closedbrow talking2mouth "Habit I picked up in Galar, looking after Sunny and Ness. When you look like those two, you get a lot of weirdoes following you into a lot of backstreets. Helps to have a seven-foot early bloomer following the weirdo, in that case."
    raihan @talkingmouth "Silly of me, all considered. Shoulda known it was you. You two have been real chummy recently, yeah?"

    red @sadbrow talkingmouth "I'd like to think so. She's pretty busy, though. Hard to be chums with someone when the entire world wants a piece of her."

    raihan @happy "Don't I know {i}that.{/i} My mate Leon's got an entire region who'd throw themselves into muddy puddles for him to walk over them, but those puddles never seem to lead him to time with me."
    raihan @surprised "Come to think of it, I'm not sure if we'd ever get the chance to chat if it weren't for me constantly having a go at that champion's cape of his."
    raihan @closedbrow talkingmouth "Ah, but we don't choose our friend's schedules. Best way to work with it is to just be a part of whatever's taking up their time. So, the Galarian league, for Leon."
    raihan @happy "And for our very own Rosa? Well, mate, I'll be honest and say I'm not sure you're quite cut out for Pokéstar Studios--"

    red @happy "{i}Total{/i} agreement."

    raihan @talkingmouth "--But I reckon there's something out there for you."
    raihan @closedbrow talkingmouth "Y'know, Galarian gyms have waterboys. There's an entrance on the ground floor for anyone who's not too proud."

    red @closedeyes sadeyebrows talkingmouth sweat "Easy for you to say. You've been on top of that Dynamax-sized dragon-shaped skyscraper for a {i}long{/i} time. The ground floor's quite a ways away."

    raihan @playfulbrow talkingmouth "Eh, I'd like to think I still remember the view from down there."

    red @confused "...Is that a short joke? Because you're, like, the {i}only{/i} guy in the school who could actually make that joke at me." 

    raihan @happy "Not intentional, mate."

    pause 1.0

    raihan sadbrow frownmouth @talking2mouth "Eh? What's got our Rosa looking like that?"

    show raihan:
        xpos 0.5
        ease 0.5 xpos 0.66

    show rosa sadbrow cry frownmouth with dis:
        xpos -0.3 xzoom -1
        ease 0.5 xpos 0.33

    pause 0.5

    red @sad "Rosa? What's wrong?"

    pause 0.5

    rosa @talking2mouth "Nothing. I'm fine."

    pause 0.5

    raihan @talking2mouth "No-one could sell that one, Whitley. Not even you."

    rosa @closedbrow sad2mouth "It's..."

    pause 1.0

    rosa @sideeyes sadmouth "The photographer."

    raihan angrybrow @angrymouth "What's this about a photographer? This better not be what I'm reckoning it is."

    rosa @talking2mouth "No... it's..."

    pause 1.0

    redmind @sadbrow frownmouth "She seems speechless..."

    red @talking2mouth "A while ago, we were battling together, and somebody took a picture of us. We weren't doing anything wrong. We were in the Battle Hall. Rosa was even recording the battles, like her contract asks her to."
    red @closedbrow talking2mouth "So what happened?"

    python:
        scrimblobingus = GetTrainerTeam("Rosa", "Dottler")
        scrimbloid = scrimblobingus.GetId()
        scrimblonick = scrimblobingus.GetNickname()

    rosa @talking2mouth "...The photographer caught a photo of my [scrimblonick]."

    raihan @surprised "Come again? Is that some sort of euphemism?"

    rosa @sideeyes talking2mouth "No... I actually have a {i}[scrimblonick]{/i}. And I love him. But I... I can't... I'm {i}not allowed{/i}..."

    rosa cry2 @closedbrow talking2mouth "The photographer posted my picture to one of those image-sharing websites, and now... now people are saying that..."

    pause 1.0

    show raihan:
        xpos 0.66
        ease 1.0 ypos 1.2 zoom 1.3 xpos 0.66

    narrator "Rosa wordlessly hands you her phone. On the phone is a picture of an email, with a few attachments--screenshots from social media. Raihan peers over your shoulder and reads."

    Character("User631") "\"bugs? gross. you know what they say about bug girls (imagine the smell)\""
    Character("User071") "\"Yet another Pokéstar Studios elite virtue-signaling. No one actually likes bugs. It's just a psyop.\""
    Character("User752") "\"lol gay\""

    narrator "The email itself is terse and condemnatory, stating that Rosa's actions have irreparably damaged her brand, and while Pokéstar is running damage control, Rosa should expect her directorial debut to be on indefinite hiatus."

    rosa sadbrow @talking2mouth "It's just... it's just a silly bug. He's just a silly spaceship bug. Why are they... why can't I just...?"

    narrator "You hand the phone off to Raihan."

    show raihan:
        xpos 0.66 ypos 1.2 zoom 1.3
        ease 1.0 ypos 1.0 zoom 1.0 xpos 0.66

    red @sadbrow talkingmouth "Rosa. Don't let them get to you. They're just dumb internet haters. What they think doesn't matter! And you smell fine!"

    rosa @closedbrow talking2mouth "I don't care about {i}them{/i}. But... my debut... I worked so hard, for so long, to get that... it's so unfair."

    show rosa:
        xpos 0.33
        ease 0.3 ypos 1.2 zoom 1.3 xpos 0.33

    rosa angry "Loving [scrimblonick] was the {i}only{/i} thing I ever did wrong! And there's nothing wrong with that!"

    pause 1.5

    show rosa closedbrow cry3 angrymouth with dis

    red @sadbrow talkingmouth "I know, Rosa. I know."

    show blank2 with slowdis

    narrator "It seems that there is nothing that can be done at this time."
    narrator "Perhaps you will have the chance to provide comfort to Rosa later, when--"

    hide blank2

    show rosa cry surprisedbrow frownmouth with dis

    raihan @closedbrow talking2mouth "Nah, this is bollocks."

    rosa @talking2mouth "Huh? It's--is it a fake email?"

    raihan @sad "Sorry, nah. It's a real email, true enough, even if it was sent from a fake man."
    raihan @closedbrow talking2mouth "But it's not something you've gotta put up with. Man's gotta take a stand, and I'll be {i}seven{/i} bloody feet under before I let some fat tosser in Unova (no offense) make a pretty girl like you cry."

    pause 1.0

    raihan -frownmouth @talkingmouth "[last_name], you're with me, yeah?"

    red @surprised "Huh? Y-yeah, of course! Absolutely!"

    pause 0.5

    redmind @closedbrow frownmouth "Damn it, he's so much more charming than me..."

    rosa @sadbrow talkingmouth "Thank you, you two... but it's not like we can do anything about it. I... violated my contract. I used a Pokémon I shouldn't have. In public, even."
    rosa @sadbrow talking2mouth "I just thought I could get away with it."

    raihan @talkingmouth "Now, I'm going to need to run this legalese by Sonia, but it looks like there might be a way out of this."
    raihan @talking2mouth "I've seen enough contracts Rose has pushed in front of me to know that there's always a way out of them if you're willing to work for it."

    show raihan:
        xpos 0.66
        ease 1.0 ypos 1.2 zoom 1.3 xpos 0.66

    raihan @talkingmouth "Look at this. Down at the bottom, where they highlighted the part of your contract that you 'violated', or whatnot. Looks like the Pokémon you're allowed to use are sorted into tiers, right?"

    rosa @talking2mouth "Yeah. They're based on a variety of factors, but mostly how much they've been used on champions' teams, or in other movies."

    raihan @talkingmouth "Right. So, up here at the top, we've got the Kanto classics--Gengar, Charizard, of course, Alakazam. Few others, like Lucario and Garchomp up there, right..."
    raihan @closedbrow talking2mouth "And at the bottom... Lumineon, Maractus, Eiscue... and a fair shake of Bug-types."
    raihan @closedbrow talking2mouth "So, I'm just thinking, but if, suddenly, Alakazam dropped from the top tiers, you'd probably have to stop training them if you had one, right?"

    rosa @talking2mouth "Yes... these lists are kept {i}very{/i} up-to-date."

    raihan @talkingmouth "Killer. [last_name], I see that spark in your eye. You know what I'm getting at, right?"

    red @surprised "I... yeah. I think I actually do."
    red @closedbrow talkingmouth "If a popular Pokémon becoming unpopular means you can't use it anymore, then that {i}has{/i} to mean that an unpopular Pokémon becoming popular means you {i}can{/i} use it, right?"

    rosa @surprised "I guess so."

    rosa @sadbrow talkingmouth "But... I can't do that. These Pokémon are popular because they belonged to Champions. Plural. And they've been in some of the biggest movies. They're huge. My [scrimblonick] is just..."

    raihan @closedbrow talkingmouth "Y'know what the first Pokémon I ever Dynamaxed was? A Dreepy. One of the smallest Dragon-types out there." 
    raihan -angrybrow @sadbrow talkingmouth "We all start out small, Whitley. But there's nothing in the world stopping us from getting as big as we want to be, if we're willing to push through."

    red @talkingmouth "Besides, what was it you said about these popular Pokémon? They're popular because they belonged to Champions?"

    raihan @closedbrow talkingmouth "I'll be a champion, Whitley."

    red @talkingmouth "So will I."

    raihan @talkingmouth "Carry on. What was the second thing? They've been in big movies?"

    red @closedbrow talking2mouth "If only we had a world-famous movie star with us. Someone who knows a ton about every part of the pipeline, but never had the chance to {i}really{/i} show off."

    raihan @happy "'Course, casting's a problem. We'll need other actors, right? How do the two most gorgeous ladies in Galar sound?"

    red @happy "And if we're worried about the special effects budget--I have a feeling Sabrina might be able to help us out there. She's pretty special, {i}and{/i} effecting."

    pause 1.5

    raihan @talking2mouth "Go on, Whitley. What've you got to lose?"
    raihan @closedbrow talkingmouth "I'll be honest, I don't know what you see in [scrimblonick]. Just a common bug, where I'm from."
    raihan @angrybrow talkingmouth "But you can show me. You can show the world."

    red @talkingmouth "This is your chance to make what you want. You don't need your managers' permission to make a small indie movie. You can decide when your {i}own{/i} debut is. Right?"
    red @happy "We'll all help you. Your dormmates and I. I mean... I don't know what I can do, honestly. Maybe I'll just be an [bluecolor]extra{/color} pair of hands. But I'll use 'em to make [scrimblonick] a Pokémon people will remember above Charizard."

    pause 0.5

    raihan @happy "Bloody well said."

    red @sadbrow talkingmouth "Well? You ready to make a movie?"

    rosa "{w=0.5}.{w=0.5}.{w=0.5}."

    rosa idwineyes idwineyebrows idwinmouth "Let's get rolling."

    show blank2 

    $ PlaySound("photo.ogg")

    pause 1.5

    $ formerrelationship = persondex["Rosa"]["Relationship"]
    $ persondex["Rosa"]["Relationship"] = "Extra"
    $ persondex["Rosa"]["RelationshipRank"] = 3

    $ PlaySound("sav.ogg")

    narrator "Your heart shifts as you feel your relationship with Rosa evolve from '{color=#0048ff}[formerrelationship]{/color}' to '{color=#0048ff}Extra{/color}'!"
    
    return