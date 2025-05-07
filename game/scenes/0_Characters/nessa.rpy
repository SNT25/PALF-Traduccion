label Nessa1:
    if (not IsBefore(1, 5, 2004)):
        $ persondex["Nessa"]["Events"].append("Level2SceneVer2")

    scene pool
    with Dissolve(2.0)
    stop music fadeout 1.5
    queue music "audio/music/LoFiMaxRaidBattle_start.ogg" noloop
    queue music "audio/music/LoFiMaxRaidBattle_loop.ogg"
    $ AddEvent("Nessa", "AdjustDateABase")
    if (not IsBefore(1, 5, 2004) and not HasEvent("Nessa", "DateDeny")):
        $ RecordDate("Nessa")
        narrator "Having texted Nessa, and arranged a time and place to meet up for your date, you make your way to the Recreation Center, where Nessa said she was hanging out by the pool."

    else:
        narrator "Having texted Nessa, and arranged a time and place to meet up to talk, you make your way to the Recreation Center, where Nessa said she was hanging out by the pool." 

    red @closedbrow talking2mouth "Let's see... where could she be...? Ah, there!"

    show nessa with Dissolve(1.0):
        xpos 0.33 ypos 0.54 zoom 0.05

    if (not HasEvent("Nessa", "DateDeny")):
        red @happy "{size=50}Hey, Nessa! Ready for our date?{/size}"
    else:
        red @happy "{size=50}Hey, Nessa! Ready?{/size}"


    show nessa:
        linear 30.0 xpos -0.7 ypos 0.85 zoom 0.3

    pause 5.0

    redmind @confusedeyebrows frownmouth "She's... taking her time, huh?"

    pause 5.0

    show nessa:
        xpos -0.5 ypos 1.0 zoom 1.0
        ease 2.0 xpos 0.5

    pause 2.0

    red @surprised "Woah. Did I catch you as you were about to go for a swim?"

    nessa @talkingmouth "Nah."

    red @confused "But... your outfit?"

    nessa @talkingmouth "Yeah, I just wear this."
    nessa @happy "Pretty hot, right?"

    red @happy "I mean... yeah."

    nessa @talkingmouth "Life's too short to not be as hot as you can. I've probably only got another... what, ten years of this?"
    nessa @angrybrow happymouth "I'm {i}going{/i} to milk it."

    red @talkingmouth "Cool. I'm definitely not complaining."

    if (not IsBefore(1, 5, 2004)):
        if (not HasEvent("Nessa", "DateDeny")):
            red @sadbrow talkingmouth "Is... your offer of a date still on the table?"
        else:
            red @sadbrow talkingmouth "So, uh... is your offer to hang out still on the table?"

        nessa @talkingmouth "Why wouldn't it be?"

        red @sadbrow talking2mouth "I mean, the whole Frienergy thing..."

        nessa @closedbrow talkingmouth "It's whatever. Old news, at this point."

        red @surprised "Really?"

        nessa @talkingmouth "I believed your speech. Most other people probably did as well."
        nessa @talkingmouth "...Hearing Sabrina's thoughts affected me way more than anything I learned about you."

        red @confusedeyebrows talking2mouth "Ouch?"

        nessa @closedbrow talkingmouth "That's a good thing."

    pause 1.0

    if (not HasEvent("Nessa", "DenyDate")):
        nessa @closedbrow talkingmouth "So. Where're you taking me?"

        red @happy "I actually spent a lot of time thinking about this. My first thought was a fancy restaurant, or maybe a movie."

        nessa @talkingmouth "Classic. Can't go wrong with that."

        red @talking2mouth "But you strike me as the kind of woman who's probably had a lot of dates like that."

        nessa @talkingmouth "Can't deny it."

        red @talking2mouth "So then I thought {i}really{/i} hard about what kind of date you've never been on, before..."
        
        pause 1.0

        red @happy "And I'm pretty sure I know where to take you, now."

    else:
        nessa @talkingmouth "So. You wanted to get to know me. Any particular place you wanted to go to do that?"

        red @talkingmouth "I find walking helps me talk. Up for a short walk?"

    nessa @talkingmouth "...Alright."

    redmind @thinking "...Phew. It's kinda an uphill battle to excite her, isn't it?"

    red @happy "Right! Let's go."

    scene fields2
    show clouds behind fields2:
        yalign 0.75
        ease 5.0 yalign 0.5
    with slideleft

    $ location = "fields"

    show nessa with dis

    pause 1.0

    nessa @surprised "The fields?"

    red @happy "Yeah! There's something pretty cool that I wanted to show you."

    nessa @closedbrow talkingmouth "Alright, I'm down. This is something new, at least."

    show venetiaintrobgnoglow with Dissolve(1.0)

    $ RecordKnownLocations("Nessa", "Meteor Hole")

    hide nessa

    nessa @surprised "Woah. What's this?"

    red @happy "This is a meteor crater!"
    red @closedbrow talking2mouth "It's... not quite as cool as it used to be, though. It used to be glowing orange and blue, but it looks like it's not anymore."
    red @talkingmouth "Still. Big hole in the ground. Kinda neat, right?"

    nessa "{w=0.5}.{w=0.5}.{w=0.5}."
    nessa @talkingmouth "Yeah. That's kinda neat."

    show nessa behind venetiaintrobgnoglow
    hide venetiaintrobgnoglow with dis

    nessa @happy "Alright. I'll give you a break. You've shown me something kinda cool, and that's enough for now."

    if (not HasEvent("Nessa", "DenyDate")):
        nessa @sad "I'm just glad you didn't take me to {i}another{/i} restaurant. I've had so many dates take me out for Kalosian food, I feel like I can speak the language at this point."

        red @happy "Phew! It was kinda a shot in the dark, but I guess I dodged a bullet, huh?"

        nessa @talkingmouth "Well, it wouldn't have been an instant turn-off, but yeah. I'm pretty used to those kinds of dates."

    show nessa:
        ease 0.25 xpos 0.55 ypos 1.1
        ease 0.25 xpos 0.5 ypos 1.2

    nessa @talkingmouth "Here, sit down with me. Let's chat."

    show nessa:
        ypos 1.2
        ease 1.0 zoom 1.3

    narrator "You sit down next to Nessa. Your legs dangle over the side of the pit."

    red @talkingmouth "Mind if I ask a question?"

    if (not HasEvent("Nessa", "DenyDate")):
        nessa @talkingmouth "Just ask. We're on a date."
    else:
        nessa @talkingmouth "That's why we're here."

    red @closedbrow talking2mouth "Right. When we first met, you basically asked {i}me{/i} out on a date. So, why?"

    nessa @talkingmouth "Fishing for compliments?"

    red @closedbrow talking2mouth "Nah, just trying to figure out what you saw in me."

    nessa @sad "You just seemed like a nice guy. You listened to me, you're good-looking, and you didn't stare at my chest too much."

    red @sad "Is that your criteria for a nice guy?"

    nessa @talkingmouth "You think I should have higher standards?"

    red @happy "Nessa, you're a model. You're gorgeous, you've got to be at least a little rich, and you're a good battler, too."
    red @confused "You can afford to have any standards you want, and {i}someone{/i} will rise to meet them."

    nessa @talkingmouth "Yeah, maybe."
    nessa @closedbrow talkingmouth "My standards for getting a second date are pretty high, though. I guess maybe my cutoff point is just later than it would be for others."

    red @talkingmouth "Right."

    nessa @talkingmouth "So, what's your goal here at Kobukan? What do you want to do when you graduate?"

    red @closedbrow talking2mouth "I want to be a Champion. That's always been my only goal."

    nessa @talkingmouth "Nice goal. I've heard it before, but you say it with conviction. Why do you want to be a Champion, though?"

    red @surprised "W-why?"

    nessa @talkingmouth "Yeah. Being a Champion is a short-term goal. What does being a Champion let you do?"

    red @confused "Being a Champion is a {i}short-term goal{/i}? Some people spend decades trying to do that."

    nessa @surprised "Oh. Yeah, I guess that's right."
    nessa @sad "Guess I was just thinking of Leon."

    red @closedbrow talking2mouth "Leon? Champion of Galar?"

    nessa @talkingmouth "Yeah. Friend of mine."

    pause 1.0

    show fields2 with vpunch

    red @surprised "You-- YOU'RE FRIENDS WITH LEON?!"

    nessa @sad "Was. He's... busy, now. Champion stuff."

    red @closedbrow talking2mouth "But, wait... Ethan told me something about Leon... isn't Leon, like, quite a bit older than you?"

    nessa @talkingmouth "Yeah. He became Champion five years ago, and has never lost a battle since."

    red @closedbrow talking2mouth "But you said you were a minor until recently. How could you be friends if you were so much younger than him?"

    nessa @surprised "Have you ever met the guy? He's a 10-year-old in a man's body. Out of the four of us, I was the most mature, even though I was the youngest."

    red @closedbrow talking2mouth "Wait... four of you?"

    nessa @talkingmouth "Yeah. Our group of friends. We used to call ourselves the Galarian Stars."
    nessa @sad "I was the youngest. The sensible one, the one who kept us all grounded."
    nessa @talkingmouth "Then there was Raihan. He always used to call me 'Lil Nessie.' An arrogant blowhard, but... he lifted you up. Butted heads with Leon every chance he got."
    nessa @closedbrow talkingmouth "Sonia was next. She was the granddaughter of a Pokémon Professor. Bit of a ditz, no self-esteem, but the smartest girl I know."
    nessa @talkingmouth "And... Leon was the oldest of us. He was pants with directions, but wherever he looked, he saw the stars, and followed them."

    red @happy "Sounds like a good group of friends."

    nessa @happy "We were inseparable. Went everywhere together, did everything. We all knew we would become Champions." 
    nessa @talkingmouth "They were just all waiting for me to become eighteen, then we'd take the Gym Challenge together."

    pause 1.0

    show nessa sad with dis

    pause 1.0

    red @sad "...But?"

    nessa "Leon got an endorsement from a bigwig in Galar. The Chairman of the entire league. It was a once-in-a-lifetime opportunity."
    nessa -sad @talkingmouth "I wasn't going to ask him to wait for me, obviously. So we changed the plan."
    nessa @closedbrow talkingmouth "Well, Leon became Champion within the year."
    nessa @talkingmouth "When a new Galarian Champion is crowned, they usually immediately endorse the person they feel is most likely to unseat them. It's a tradition."
    nessa @closedbrow talkingmouth "So Leon endorsed Raihan, of course. Raihan apologized to Sonia and I, but set off on his challenge."

    red @talking2mouth "He didn't make it to Champion, though."

    nessa @talkingmouth "No. But he managed to make it right up to the league, eventually securing the eighth major league Gym Leader spot."
    nessa @talkingmouth "So, at that point, we figured that he could endorse Sonia, and then Sonia could endorse me."

    pause 1.0

    nessa @talkingmouth "Sonia couldn't make it. She dropped out after the fifth gym."

    red @surprised "Oh, geez!"

    nessa @talkingmouth "We knew that the fifth Gym Leader was retiring soon, so we thought maybe Sonia could take over there, like Raihan did the eighth."
    nessa @talkingmouth "Trainer schools aren't really a thing in Galar. Most trainers just start their journeys and learn as they go. But we learned about Kobukan Academy, and heard it was a great place to get practical experience."

    if (IsBefore(20, 4, 2004)):
        nessa @talkingmouth "So Leon paid for her to go to Kobukan. She was here just last year, actually."

        red @happy "Oh, really? That's awesome! How'd she do?"

        nessa frownmouth @sad "She dropped out of that, too."

        red @surprised "...Huh?"

        nessa @talkingmouth "Yeah. She sent each of us hand-written letters apologizing for her failures, and then cut communications with us. Doesn't even respond to our texts."
        nessa @sad "God knows where she's gone."

        red @sad "Oh... I'm sorry to hear that."

    else:
        nessa @talkingmouth "So Leon paid for her to go to Kobukan. And... well, you already know. She dropped out of that, too."
        nessa @talkingmouth "She sent each of us hand-written letters apologizing for her failures, and then cut communications with us. Didn't even respond to our texts."
        nessa @sad "We all thought we'd never see her again until I saw her in the lunch hall."

        red @sad "But at least you've made contact again, right?"

    nessa @talkingmouth "Yeah. Well, I figured I wasn't going to be getting an endorsement any time soon from either Leon or Raihan, so I'd just try my own hand at this Kobukan thing."

    red @surprised "Why wouldn't they endorse you?"

    nessa @talkingmouth "I was a public figure, so were they. It was common knowledge that we were all friends before Leon ever became Champion."
    nessa @closedbrow talkingmouth "Wouldn't look good if the Champion was endorsing unproven trainers, just 'cause they were friends." 
    nessa @talkingmouth "Raihan could {i}always{/i} hold his own against Leon."
    nessa @talkingmouth "Sonia, despite her crippling insecurities, also knew more about the intricacies of battle than I think Leon does, even now."

    pause 1.0

    nessa @sad "And I looked good in a bikini."

    pause 1.0

    nessa @talkingmouth "The chain could've worked, though. Leon, through Raihan, through Sonia, to me, would have been enough degrees of separation."

    pause 1.0

    nessa @sad "But the chain broke."

    pause 1.0

    nessa closedbrow angrymouth "But we wouldn't have {i}had{/i} to rely on the chain if everyone had just {i}waited.{/i} If they'd just been {i}patient,{/i} if they'd just thought long-term about this... about {i}any{/i} of this..."

    red @sad "...I'm sorry."

    nessa -closedbrow -angrymouth frownmouth @talkingmouth "...Yeah. So... that's kinda the state of the Galarian Stars, now."
    nessa @talkingmouth "One got everything he wanted. One is still fighting for it. One disappeared. And I'm just starting my journey after everyone I care about is already finished."

    red "{w=0.5}.{w=0.5}.{w=0.5}."
    red @talking2mouth "Are you sure?"

    nessa @talkingmouth "What do you mean?"

    red @talkingmouth "Like, are you sure they're finished?"

    nessa @closedbrow talkingmouth "Um... pretty sure. Leon didn't really have a goal beyond becoming Champion."
    nessa @talkingmouth "Raihan's going to try and beat him, but that's kinda never happening."

    if (IsBefore(20, 4, 2004)):
        nessa @sad "And Sonia's already failed twice. She's probably taken a research job somewhere, and is planning on never coming back to Galar again."
    else:
        nessa @sad "And Sonia's already failed twice. I haven't asked her about it, but I don't think she's ever planning on coming back to Galar again."

    red @talkingmouth "...I don't think those sound like 'endings.'"

    nessa @surprised "How are they not?"

    red @happy "Well, maybe Leon continues to be undefeated for years. Does Raihan's story stop being told just 'cause he doesn't change that?"

    nessa @surprised "I guess not?" 
    nessa -frownmouth @talkingmouth "But I don't know who'd bother telling it. 'News flash: Nothing has changed.' Boring, right?"

    red @talking2mouth "Nessa, I {i}firmly{/i} believe the most important part of the adventure is the journey. Not the destination."
    red @closedbrow talking2mouth "I know you think the only 'run' that matters is the 'long run'..."
    red @happy "But I run every day. And I don't really care how much distance I cover, in total. All that matters is that I ran."

    pause 1.0

    nessa @talkingmouth "...So you're disagreeing with me?"

    red @sadbrow talkingmouth "Guess I am."

    if (not HasEvent("Nessa", "DenyDate")):
        nessa @happy "Good. Most dates just yes-man their way through."
        nessa @talkingmouth "Of course, most dates don't hear the whole Galarian Star shpiel..."
    else:
        nessa @closedbrow talkingmouth "First you turn me down for a date, then you disagree with me... you're full of surprises."

    $ lowertime = timeOfDay.lower()
    nessa @sad "Guess I'm off my game. It's been a weird [lowertime]."

    red @talkingmouth "I don't think you guys are done. I don't think {i}any{/i} of you are done."
    red @happy "I mean, you said you wanted to be a trainer because you were afraid that modeling wouldn't last for you, right?"
    red @talkingmouth "Every end is a new beginning. So maybe the Galarian Stars' collective dream burned out."
    red @happy "Sounds to me like you're all still pursuing your individual dreams."
    red @happy "Can't believe I'm saying this, but you should try seeing things a bit more long-term. For your friends, at least."

    pause 1.0

    red @talking2mouth "But you should totally try living in the moment more, too."

    nessa @talkingmouth "I'll think on that."

    if (not HasEvent("Nessa", "DenyDate")):
        red @happy "Cool. So what're my chances of another date?"

        nessa @closedbrow talkingmouth "...Well, I liked our conversation. Let's actually {i}do something{/i} next time, though."

        red @talkingmouth "Fair enough. I'll start brainstorming now."
        red @closedbrow talking2mouth "So... one date down, that wasn't a complete disaster. What does that make us?"

        nessa @closedbrow talkingmouth "...Mm. You're a {color=#0048ff}friend.{/color}"

        red @surprised "Wait, you'll date someone before you befriend them?"
    else:
        red @talkingmouth "So. I think I know a bit more about you. And I think you know about me, too. What are we?"

        nessa @closedbrow talkingmouth "...Mm. You're a {color=#0048ff}friend.{/color}"

        red @happy "You were willing to date me before we were even friends?"

    nessa @happy "Anything to open the door. Even a model has to try to grab people's interest, you know?"

    red @happy "Well. Color me interested."

    $ RelationshipRankUp("Nessa", "Friend")

    return

label Nessa2:
    $ location = "city"
    scene city_B
    with Dissolve(2.0)
    stop music fadeout 1.5
    queue music "audio/music/Inspira_start.ogg" noloop
    queue music "audio/music/Inspira_loop.ogg"
    $ renpy.music.play("Audio/bigcrowdloop.ogg", channel='crowd2', loop=True, fadein=0.5)

    narrator "You're in Inspira City, trying not to get run over by the bustling ever-present crowds when you suddenly hear a familiar voice."

    nessa @talkingmouth "You've got to try harder than {i}that{/i}."

    redmind @thinking "Hm. Wasn't that Nessa?"

    narrator "Following the sound of the voice, you turn onto a side street."

    scene city_A 
    show nessa:
        xpos 0.66
    show roughneck:
        xpos 0.33
    with splitfade

    stop music fadeout 1.5 channel "crowd2"
    stop music fadeout 1.5
    queue music "audio/music/LoFiMaxRaidBattle_start.ogg" noloop
    queue music "audio/music/LoFiMaxRaidBattle_loop.ogg"

    pause 1.0

    roughneck @happy "C'mon, girly, I'll make you an offer you can't refuse."

    nessa @talkingmouth "Believe it or not, I {i}have{/i} refused it. Several times, already."

    roughneck @angry "Man, you just don't want to give me a chance because I'm bald, isn't it? I'll have you know I shaved off all my hair! {i}On purpose!{/i}"

    nessa @talkingmouth "That's not why I'm saying no. I'm saying no because you look like you're about double my age."

    roughneck @surprised "What?!"

    nessa @talkingmouth "Think this through. What if I {i}do{/i} go on this date with you? What if we really hit it off, and decide to keep going?"
    nessa @talkingmouth "Then we decide to get married. Have kids. You'll grow old much sooner than I will. Men don't live as long, anyway."
    nessa @closedbrow sadmouth "I'm seeing fifteen, twenty years where I'll be all alone, then. Maybe more. Do you want to do that to me?"

    pause 1.0

    show nessa surprisedbrow frownmouth with dis

    show city_A with vpunch

    roughneck @angry "You {i}bitch!{/i} I'm twenty-four!"

    nessa "Oh."

    pause 1.0

    nessa @talkingmouth "Then I guess I {i}am{/i} turning you down because you're bald."

    roughneck @angry "That's it! Let's settle this in a Pokémon battle! You lose, you have to go on a date with me!"

    nessa @closedbrow angrymouth "Jeez, every time with them..."

    show nessa surprisedbrow frownmouth with dis

    red @talkingmouth "Hey, Nessa. Need some backup?"

    nessa -surprisedbrow -frownmouth @talkingmouth "Appreciate the timing. And yeah, I'd like that."

    python:
        trainer1 = MakeRed()
        trainer2 = MakeTrainer("Nessa", TrainerType.Ally)
        roughneckteam = GetTrainerTeam("Silver")[2:]
        trainer3 = Trainer("roughneck", TrainerType.Enemy, roughneckteam, number=2)

    call Battle([trainer1, trainer2, trainer3], reanchor=[False, False, True], customexpressions=["red", "red angrybrow happymouth", "nessa", "nessa angrybrow happymouth", "roughneck", "roughneck angry"]) from _call_Battle_121
    $ battlehistory["Roughneck4"] = _return

    show nessa:
        xpos 0.66
    show roughneck angry:
        xpos 0.33
    with dis

    if (WonBattle("Roughneck4")):
        nessa @talkingmouth "Nicely done, [first_name]. Thanks."

        $ ValueChange("Nessa", 1, 0.66)

        nessa @talkingmouth "Now, please leave me--"

        show nessa surprisedbrow frownmouth with dis

    else:
        nessa frownmouth @closedbrow talkingmouth "...Your Pokémon were more powerful than I thought. I guess I misjudged you."
        nessa @sad "Sorry, [first_name]."
        nessa @talkingmouth "Look, can you please just leave me--"

    roughneck "Here you were, leading me on, when you've already got a boyfriend! {w=0.5}{nw}"

    show city_A with vpunch
    show nessa sadbrow with dis

    extend "You {i}slut!{/i}"

    show roughneck:
        xpos 0.33 
        ease 0.5 xpos 1.3
    
    show nessa:
        xpos 0.66
        linear 0.1 xpos 0.75 ypos 1.05 rotate 3

    show city_A with vpunch

    pause 1.0

    show nessa:
        xpos 0.75 ypos 1.05
        ease 2.0 xpos 0.5 ypos 1.0 rotate 0

    pause 4.0

    menu:
        ">Run after him":
            narrator "You prepare to run, but--"

            nessa @closedbrow talkingmouth "Don't."

        ">Stay with Nessa":
            narrator "You watch Nessa's face carefully. There's a curious expression on it you can't quite interpret."
    
    queue music "audio/music/LoFiMaxRaidBattle_start.ogg" noloop
    queue music "audio/music/LoFiMaxRaidBattle_loop.ogg"

    red @talking2mouth angrybrow "That was {i}entirely{/i} uncalled for. You didn't do anything wrong. That guy's just a pig."

    pause 1.0

    nessa @talkingmouth "Yeah. I know."

    pause 1.0

    nessa -sadbrow @talkingmouth "What's that look for?"

    red @sadbrow talkingmouth "Are you alright?"

    nessa @talkingmouth "Of course. That's not the first time I've been called... {i}that.{/i}"

    pause 0.5

    nessa @sad "Though it's the first time in real life. I'd only seen that on the internet before."
    nessa @sadbrow happymouth "It's a lot easier to blow off the haters when you can't see the hate in their eyes."

    red @talking2mouth "...He was just jealous. A jealous idiot. I battle those guys all the time, you know? I know they're not firing on all cylinders."

    pause 0.5

    redmind @angrybrow frownmouth "That being said... his Pokémon were pretty strong. I think I might have to talk with Silver about the kind of ammunition he's providing his 'tenants' with."

    nessa @talkingmouth "...Are you doing anything?"

    red @talkingmouth "Hm? Like what?"

    nessa @talkingmouth "Just... anything."

    red @talkingmouth "Well, I was kind of looking for you, actually."

    nessa @talkingmouth "Oh."
    
    if (not HasEvent("Nessa", "DenyDate")):
        nessa @sad "Right. Sorry I haven't set up that second date. I've had a lot going on."
    else:
        nessa @sad "Right. Sorry I haven't been reaching out. I've had a lot going on."

    red @happy "Oh, it's nothing about that. I kinda wanted to ask you something. On, uh, Raihan's behalf."

    nessa @talkingmouth "Did he get someone pregnant?"

    red @surprised "What? No."

    nessa @talkingmouth "Did he crash one of his muscle cars?"

    red @confused "No?"

    nessa @talkingmouth "Did Rose kick him out of his gym?"

    red @happy "N-"
    red @surprised "Wait, y-"
    red @closedeyes angryeyebrows talking2mouth "Wait, n-"

    pause 0.5

    redmind @sadbrow frownmouth "Sorry, Raihan."

    red @sad2eyes sadeyebrows talkingmouth "I take the sixth."

    nessa @talkingmouth "It's 'take the fifth,' and you can't do that, you're Kantonian."

    red @talkingmouth "Damn."

    pause 0.5

    nessa -frownmouth @talkingmouth "You're silly. You know that?"

    red @sadbrow talkingmouth "Then if my Champion dream doesn't work out, maybe I can find work as a clown. I always wanted big shoes, and a small car."

    pause 0.5

    nessa @sadbrow talkingmouth "Look, it's ridiculous that I'm even asking this, but... you don't think of me like 'that', do you?"

    red @happy "What? No, of course not! Like I said, the dude was an idiot. You were even turning him down."

    nessa frownmouth @talkingmouth "...Like, you understand the difference between confidence and looseness, right?"

    red @sadbrow talkingmouth "Yeah, I do."

    pause 0.5

    redmind @sadbrow frownmouth "She... definitely doesn't seem convinced. She's trying to blow it off, but I can tell this really bothered her."

    pause 0.5

    nessa @sadbrow talkingmouth "Alright. I've made a decision."

    red @surprised "That was fast."

    nessa @talkingmouth "You tell me about what Rose's problem is with Raihan. And while you're doing that, we'll go shopping."

    red @happy "Shopping? Sure. Holding the stuff of only one shopper is a nice break after what Leaf put me through."
    red @talkingmouth "Oh, but there's one problem."

    nessa @surprisedbrow talkingmouth "Yeah?"

    red @talking2mouth "I don't know what Rose's problem with Raihan is. Neither does he. We were hoping you might have some kind of insight."

    nessa @closedbrow talkingmouth "...Hm."

    pause 0.5

    nessa @talkingmouth "Let's walk and talk. {i}Join{/i} is open."

    scene blank2 with splitfade

    narrator "While walking to the Inspira City Mall, formally named 'Join Avenue of Inspira', you tell Nessa, in very broad strokes, what Raihan's problem is."

    scene mall 
    show nessa
    with splitfade

    nessa @talkingmouth "That boy's ridiculous."
    nessa @talkingmouth "So you're saying that Chairman Rose, of the Galar League, gave Raihan a non-optional paid vacation."

    red @talking2mouth "And appointed a substitute in his place."

    nessa @sad "That isn't a good sign. You don't appoint a substitute if you expect your main guy to come right back."

    red @sweat talking2mouth surprisedbrow "That's what Raihan said!"

    nessa @talkingmouth "Well, I'm glad he decided to use his free time to visit Sunny and me."
    nessa @talkingmouth "And I'm glad that he was smart enough to realize he should come to me with this problem. Maybe he's not {i}totally{/i} hopeless."

    red @happy "So you know what Rose's problem is?"

    nessa @talkingmouth "No."

    red @closedbrow talking2mouth "Shoot."

    nessa @talkingmouth "I think I could figure it out, though. Follow me."

    scene insidemall
    show nessa
    with splitfade

    nessa @talkingmouth "I'm interested in hearing {i}your{/i} theory, though. What did {i}you{/i} say?"

    if (HasEvent("Raihan", "DislikeBeatLeon")):
        red @confused "I just said maybe Rose was worried that Raihan will beat him, one day."

        nessa @talkingmouth "...I'm sure that gave Raihan an ego boost. Not that he needed one."
        nessa @closedbrow talkingmouth "No, I don't think it's that. Leon's strong. He's {i}ridiculously{/i} strong."
        nessa @sad "I don't think Rose is afraid of anything Raihan can do to him."
        nessa @closedbrow talkingmouth "I think it must be something else."

    elif (HasEvent("Raihan", "DislikePopularity")):
        red @confused "I just said maybe Rose was irritated that Raihan was so popular."

        nessa @talkingmouth "...I could see that. He wants {i}Leon{/i} to be the figurehead of the league, after all."
        nessa @closedbrow talkingmouth "Any attention anyone else gets just takes away from Leon merchandise the league could be selling."
        nessa @closedbrow talkingmouth "Still, I feel like there must be more to it."

    elif (HasEvent("Raihan", "DislikeUnprofessional")):
        red @confused "I just said maybe Rose thinks that Raihan is unprofessional."

        nessa @talkingmouth "...I could see that. For as much ribbing as I give him, Raihan takes his job seriously."
        nessa @closedbrow talkingmouth "But he's not a serious person. At all. Maybe Rose can't see the effort Raihan's making in his gym."
        nessa @sad "Hard to see the grains of sand when you're on the top of that big, silver tower in Wyndon."
        nessa @closedbrow talkingmouth "Still, I feel like there must be more to it."

    elif (HasEvent("Raihan", "DislikeBody")):
        red @confused "I just said maybe Rose is irritated that Raihan's so sexy."

        nessa @surprised "Huh. I wouldn't have thought of that, but I guess that's actually possible."
        nessa @sadbrow talkingmouth "Some people... get {i}real{/i} jealous."
        nessa @closedbrow talkingmouth "Still, I feel like there must be more to it."

    else:
        red @confused "I had no idea. He didn't either."

        nessa @talkingmouth "I guess we're all in the same boat, then."

    nessa @talkingmouth "Give me a little bit more time to think on this."

    red @talkingmouth "Sure. I'll do my best to think on it, too."
    red @closedbrow talking2mouth "I think I know enough about Raihan, now, based on what he told me... what about Rose, though? I don't know a lot about him."

    nessa @talkingmouth "Not sure I could say much. Sonia worked with Macro Cosmos, his company, for a while, when she was helping with her Gran's Dynamax research. Maybe she'd know."
    nessa @closedbrow talkingmouth "All I know is that he's a creepy CEO who would rather die than let Leon have an ounce of attachment to anyone else."
    
    if (IsDate(year = 2004)):
        nessa @sadbrow talkingmouth "I mean, if that ridiculous stunt he pulled during last year's world championship didn't make that obvious, then..."
    else:
        nessa @sadbrow talkingmouth "I mean, if that ridiculous stunt he pulled during two years ago didn't make that obvious, then..."

    pause 1.0

    red @sadbrow sweat talkingmouth "Sorry?"

    pause 0.5

    nessa @talkingmouth "You know, the world championships of 2003. Can you believe what he did, then?"

    pause 0.5

    show nessa surprisedbrow frownmouth with dis    

    red @happy sweat "So, the thing is, I don't watch much TV."

    nessa -surprisedbrow -frownmouth -surprised @surprised "No way. You didn't see them? You didn't even hear about them?"

    red @sweat talkingmouth "I've heard them referenced, but... somehow, this is the first I've heard about them directly."

    nessa @talkingmouth "Oh, wow. So, here's what happened. This is one of the biggest scandals that's ever wracked a Pokémon League--any league--so you should definitely know about it."

    show nessa:
        xpos 0.5
        ease 0.5 ypos 1.2 zoom 1.3

    narrator "Nessa leans closer, and her voice takes on a conspiratorial whisper."

    nessa @talkingmouth "So, the World Championships have been held every four years since 1895, right?"

    nessa @talkingmouth "And there's always a massive bidding war between the regions and cities that want to host it."
    nessa @talkingmouth "Here's the thing. As early as the 1970s, even before I was born, Rose had been trying to get the World Championships to be held in Wyndon."
    nessa @talkingmouth "He constantly campaigned, and petitioned the Galarian league, and even the government, to get the WCs."

    red @confused "Okay. Where's the scandal?"

    nessa @talkingmouth "Getting there. You know rushing me doesn't work."

    red @sweat closedbrow talking2mouth "{i}Do{/i} I."

    nessa @talkingmouth "Well, in 1999, he won, finally. He had to leverage his entire financial empire, and every crumb of influence he had in Galar to make it happen, but he succeeded. The 2003 world championships were going to be held in Wyndon."
    nessa @talkingmouth "Everything went off without a hitch, at least at first. Everyone was there. Diantha, Steven, Alain, Lance. You know, the regulars."

    pause 1.0

    nessa @closedbrow talkingmouth "Of course, the 'big two' were there, as well. Cynthia, 'the strongest woman in the world.' And Leon, 'the undefeatable champion.'"

    red @surprised "Oh, man! I would have {i}loved{/i} to see that battle! Did Leon give you front-row tickets?"

    nessa @talkingmouth "He did. I was so close I could feel the heat coming from his Charizard's tail. I could count the scales on Cynthia's Garchomp, too. Those were {i}amazing{/i} seats."

    pause 0.5

    nessa @sad "...It was a once-in-a-lifetime opportunity. Not the kind of thing you can 'wait around' for. Not the kind of thing that time can solve, if you miss it, or... anything like that."

    red @surprised "Oh!"
    red @sad "Oh, crap. What happened?"

    nessa @talkingmouth "Leon's hand was on his Poké Ball. Cynthia was pulling her lipstick out. A really {i}legendary{/i} event was about to happen."

    pause 0.5

    nessa frownmouth @sad "And then Rose's big, stupid, ugly, mug popped up on the TV and said that the World Championships were over."

    redmind @surprisedbrow smirkmouth "Wait... is she... is she {i}pouting?{/i}"

    red @sadbrow talkingmouth "That sounds really frustrating."

    nessa @angry "It {i}was!{/i} Everyone was so excited! This was going to be the kind of battle we'd tell our grandkids about! And... and... it just stunk! The whole thing stunk!"

    red @talkingmouth "Why did he cancel it, though?"

    nessa @talkingmouth "Oh, that's the stupidest part. He said that he was 'summoning Eternatus' to solve Galar's energy crisis."

    red @talkingmouth "Hm? Eternatus? I've talked to Sonia about that, but I thought that was, uh, a massive spaceborne dragon Pokémon that's responsible for the existence of the Galarian Wishing Stars?"

    nessa @talkingmouth "Yeah. It is. And he said he was summoning it."

    pause 0.5

    nessa @talkingmouth "Which is, like, pick a {i}less{/i} obvious lie. Nothing happened. There was no dragon. The energy crisis wasn't solved, and although Rose insisted he {i}had{/i} summoned Eternatus, there was absolutely no evidence of it."
    nessa @angrybrow talkingmouth "Eventually, he just stopped saying he had. I guess he was only saying it for attention, all along."
    nessa @talkingmouth "Maybe that's why he hates Raihan. Raihan gets attention without resorting to pathetic lies."
    nessa @angry "...Tch."

    pause 0.5

    red @talkingmouth "Was he... punished, at all?"

    nessa @talkingmouth "Not directly. Since all he did was interfere with an event that he was running. The value of Macro Cosmos dropped a few billion, though, as everyone assumed its CEO had gone insane."

    red @confused "To be honest, I think I understand this 'Chairman Rose' even less now than I used to."

    nessa @talkingmouth "He's hard to figure out. Often acts without explaining his actions. Leon's practically his son, with how much time they spend together, and not even Leon knows what he's really thinking."

    pause 1.0

    nessa @talkingmouth "Oh, great. We're here. Wait here, and give me a second."

    show nessa:
        xpos 0.5 ypos 1.2 zoom 1.3
        ease 1.0 xpos -0.3

    narrator "Without waiting for a response, Nessa walks into a clothing store. The name, emblazoned on the top, is 'Forever 151.'"

    red @talkingmouth "...Hm."

    if ("Rosa" in GetStudents()):
        pause 2.0

        narrator "You tap your foot impatiently, about to follow Nessa into the clothes store, when you suddenly hear a voice."

        show rosa sweat at rightside with dis

        rosa @surprised "Oh! [first_name]! Hi!"

        red @happy "Hey, Rosa! What's up?"

        rosa @talkingmouth "I'm here on business, actually."
        rosa @sadbrow talking2mouth "I'm sort of an honorary manager of all the Join Avenue malls... they slapped my name on them to increase sales, anyway."
        rosa @sadbrow talkingmouth "Pretty sure they wouldn't be too happy if I actually started trying to make any decisions, but I need to show up once in a while. Contractual obligation."

        red @happy "I getcha. You look pretty run-over, though. What's up?"

        rosa @sadbrow talkingmouth "Guess you noticed? There's a guy a few halls back who's selling some kind of nose cream."
        rosa @sadbrow talking2mouth "He {i}really{/i} wants me to take a picture with his stand, but I'm not actually allowed to, so I'm just--"

        show rosa surprisedbrow frownmouth with dis

        Character("Creepy Salesman") "\"Hey! Hey, try out the cream! 99%% off if you buy now! Doesn't cause cancer!\""

        rosa sad "Crap! Gotta run!"

        show rosa:
            xpos 0.75
            ease 0.3 xpos -0.3

        pause 1.0

        if (GetRelationship("Rosa") == "Bodyguard"):
            narrator "You let out a big sigh and go off to block the creepy salesman's path. After all, you {i}are{/i} Rosa's [bluecolor]bodyguard{/color}."

            $ ValueChange("Rosa", 5, 0.5)

        else:
            redmind @poutmouth "Man. Famous people have weird problems. I never could have imagined the kind of things they had to deal with before I went to Kobukan..."

            $ ValueChange("Rosa", 3, 0.5)

        pause 2.0

    else:
        pause 5.0

        narrator "You tap your foot impatiently, about to follow Nessa into the clothes store, when you hear her voice."

    show nessa casual:
        xpos -0.5 ypos 1.0 zoom 1.0
        ease 1.0 xpos 0.5

    pause 3.0

    nessa @talkingmouth "Sorry for the wait. How do I look?"

    menu:
        "Fantastic.":
            nessa @talkingmouth "Thanks."

        "Classy.":
            nessa @talkingmouth "Thanks."

        "Beautiful.":
            nessa @talkingmouth "Thanks."

        "I want to lick you.":
            show nessa surprisedbrow frownmouth with dis

            $ ValueChange("Nessa", -5, 0.5)

            nessa @closedbrow talkingmouth "That's disappointing. I'm going to do you a favor and ignore what was obviously an intrusive thought."

        "With your eyes.":
            nessa @closedbrow talkingmouth "You've been spending too much time around Raihan."

    show nessa closedbrow talkingmouth with dis:
        xpos 0.5 xzoom 1
        ease 0.5 xzoom -1
        ease 0.5 xzoom 1

    narrator "Nessa does a happy twirl on the spot, holding her arms out like a ballerina. She looks like she's enjoying herself, but something about this is still niggling at you."

    pause 1.0

    show nessa surprisedbrow frownmouth with dis

    red @talking2mouth "Nessa. Did you buy this because of what that... that {i}thug{/i} said?"

    pause 0.5

    nessa -surprisedbrow -frownmouth -surprised frownmouth @sad "I... no. No, he didn't get to me. I just want to expand my wardrobe."

    menu:
        "You should go back to your old outfit.":
            pause 1.0

            narrator "Nessa's facial expression is hard to read."

            nessa @talkingmouth "...You remember what my job is, right?"

            red @talking2mouth "Yeah. Model."

            nessa @talkingmouth "That's right. And I get paid a ridiculous amount of money to listen to people telling me what to wear."

            pause 0.5

            nessa @angry "So I {i}don't{/i} let people who {i}aren't{/i} giving me a ridiculous amount of money tell me what to wear."

            redmind @sadbrow frownmouth "But... that thug..."

        "Well, alright, then.":
            pass

        "As long as you're comfortable.":
            pass

    nessa @frownmouth sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."

    nessa @surprised "What's that noise?"

    show wallace:
        xpos 1.3 
        ease 0.5 xpos 0.33

    show nessa:
        xpos 0.5
        ease 0.5 xpos 0.66

    wallace @happy "Ah-ha! I thought my fashion senses were tingling!~"

    $ BecomeNamed("Instructor Wallace")

    nessa @surprised "Instructor Wallace? What are you doing here?"

    wallace @happy "Oh? What do you think, Miss Nessa? Sho~o~o~pping, of course!"
    wallace @surprised "Oh, but I see I'm not the only one! What a lovely new outfit."
    wallace @closedbrow talkingmouth "Might that be the 2002 Fall collection of esteemed Galarian designer Dante Leone?"

    nessa @closedbrow talkingmouth "Yes. Pure Wooloo-wool fabric."

    wallace @talkingmouth "Such delightful taste! Why, if I were ten years younger, I'd try to set up a shoot with you."
    wallace @sad "Alas, time's caught up to me, and I fear that my dimness might distract from your shine."

    redmind @confusedeyebrows frownmouth "Time's caught up with him? That's a laugh. He doesn't look a day over twenty-five."

    wallace @talkingmouth "Did anything inspire this wardrobe change? A certain ripple in the waves, or perhaps the shimmer of a scale that caught your fancy?"

    show nessa sadbrow with dis

    pause 0.5

    show nessa -sadbrow with dis

    narrator "Nessa looks at you, then quickly looks away."

    nessa @talkingmouth "Nothing in particular. Just felt like a change might be nice."

    wallace @talkingmouth "Well, while we're on the topic, please, do tell me how you came by your other outfit."
    wallace @angry "Oh, it's such a shame that you students are all clamped into the standard Kobukan uniform during school hours."
    wallace @sadbrow talking2mouth "There's so little room for self-expression."

    nessa @talkingmouth "My normal outfit is the women's uniform of Hulbury Stadium."

    wallace @closedbrow talking2mouth "Ah... Stadiums. That's what gyms are called in Galar, yes?"

    nessa @talkingmouth "That's right."

    wallace @talkingmouth "Well, how did you happen to get your hands on a uniform? Surely, with your work, you were too busy to have worked there, too?"

    nessa @talkingmouth "The Gym Leader of Hulbury was my modeling instructor."

    show wallace surprisedbrow frownmouth with dis

    nessa @sadbrow talkingmouth "She wanted me to take over her gym. She was known as the 'Sapphire of Hulbury'. She was famous for her beauty. Maybe...?"

    wallace frownmouth @sad "Yes... I am familiar with The Sapphire's work."

    red @sad "I'm guessing there's a sad story here?"

    wallace @sad "Nothing that every model doesn't face eventually. But for her, it came... too swiftly."

    nessa @sadbrow talkingmouth "She did what she wanted, when she wanted, how she wanted. She {i}always{/i} wore her gym uniform, in case she felt like going for a swim."
    nessa @happy "Sometimes, if a conversation was boring her, she'd offer her conversation partner two choices: 'go jump in a lake', or 'go jump in a lake with me.'"

    pause 0.5

    nessa @sad "It was a freak accident. A lone Basculin in Hulbury bay. There shouldn't have been any there--Galar's Barraskewda fill that niche. She was... disfigured."

    wallace @sad "One of the greats, a model of talent and style unparalleled. Such a tragedy. Such a pity."

    nessa @talkingmouth "She stopped being able to find modeling jobs. And then... Rose removed her from her position."
    nessa @sadbrow talkingmouth "He didn't {i}say{/i} it was because she now had a face that could scare children, but..."

    pause 1.0

    nessa @talkingmouth "She left the region. I never saw her again."

    narrator "Nessa looks directly at you."

    nessa @talkingmouth "Before she left, she said... to live my most beautiful life at every single second. To never hide anything I could one day lose."

    pause 0.5

    nessa @angrybrow talkingmouth "She was an idealist."
    nessa @sadbrow talkingmouth "She lived in her own world. A world where practicality was a distant third consideration behind beauty and integrity."
    nessa @talkingmouth "She said that beauty was something to be shared with others. As often and as loudly as possibly."

    wallace -frownmouth @talkingmouth "Yes, she was a smart woman. Incredibly talented. Beautiful, inside and out. She understood, my darling students, that beauty is war."
    wallace @happy "If you're not screaming out what you have, then why have it?" 
    wallace @angrybrow happymouth "If you're not dragging the competition into your undertow, then why even try? That's what I say, quite right!"
    wallace @happy "Certainly, I live by that philosophy. Indeed, as all should."

    pause 0.5

    wallace @talkingmouth "Hm... perhaps you, Mr. [first_name], could do with a wardrobe change?"

    nessa @talkingmouth "That could be fun."

    red @sweat sadbrow talkingmouth "I'll pass."

    redmind @thinking "I might not get fashion, but I feel like if I let these two decide my outfit, they'll put me in a mankini..."

    wallace @happy "Ah, well. Perhaps next time. Toodle-oo!"

    hide wallace with dis

    pause 0.5

    red @talkingmouth "It sounds like The Sapphire meant a lot to you."

    pause 0.5

    nessa @sad "She told me that every moment in life where I wasn't flaunting what I have is a moment that I'll regret when I'm old."
    nessa @sadbrow talkingmouth "I've always lived under those guidelines. I try to think, with every decision I make, how I'll feel when I'm an old woman, closing her eyes for the last time, in front of a dying fireplace..."
    nessa @talkingmouth "I don't want to lose what I have. I don't want to fade away. But I know that I will. So I want to make use of it, now."

    pause 0.5

    nessa @sad "I'm not... I'm not a..."

    pause 0.5

    nessa @sadbrow talkingmouth "I'm sorry. None of this is your problem."

    red @sad "Nessa..."

    nessa @talkingmouth "We should head back to campus. Come on. Let's go."

    $ AddEvent("Nessa", "OutfitSwap")

    scene blank2 with Dissolve(2.0)

    nessa @sadbrow talkingmouth "...Thanks for your patience. I led you on, asking you out right away, didn't I?"
    nessa @talkingmouth "You probably thought you'd be bringing me back to your dorm by now."

    menu:
        "Kinda.":
            $ AddEvent("Nessa", "DormKinda")

        "I can wait.":
            $ AddEvent("Nessa", "DormWait")

        "Nah.":
            $ AddEvent("Nessa", "DormNah")

    pause 1.0

    nessa @sad "Sigh."

    nessa @sadbrow talkingmouth "You're... a [bluecolor]good friend.{/color}"

    $ oldrelationship = persondex["Nessa"]["Relationship"]
    $ persondex["Nessa"]["Relationship"] = "Good Friend"
    $ persondex["Nessa"]["RelationshipRank"] = 2

    $ PlaySound("sav.ogg")

    narrator "Your heart shifts as you feel your relationship with Nessa evolve from '{color=#0048ff}[oldrelationship]{/color}' to '{color=#0048ff}Good Friend{/color}'!"

    return

