label skylaevent:

if (IsAbsent("Skyla", location.title())):
    return

if (not persondex["Skyla"]["Named"]):
    narrator "You spot an unfamiliar student and go to greet her."
    
    show skyla uniform with dis

    pause 0.5

    red uniform happy "Hi there!"

    skyla "Hey there, [first_name]!"

    red @surprised "...Okay, so how'd you do that?"

    skyla "Your name's on your bag."

    red -happy @talkingmouth "All the way over there? You've got good eyes."

    skyla surprised "Really?"

    red @talkingmouth "What? I mean, you {i}must{/i} know."

    skyla happy "No, I know, it's just..."
    skyla -happy @talkingmouth "I don't think anyone's ever told me that. Normally I'm the one who tells people I've got good eyes!"

    red @happy "Well, glad I could save you the trouble. Does that come in handy? Are you, uh, a birdwatcher? A sniper?"

    skyla @angry "Do I look like a sniper?"

    red @talkingmouth "No. So you must be a pretty good one. Don't want to be a sniper who looks like a sniper, right?"

    skyla closedbrow talking2mouth "Oh, yeah... that'd be like a ninja who wears bright orange, right?"

    red @talkingmouth "Yeah, or one of those spandexed teens with attitude."

    skyla sweat surprised "Wh-what? Who's talking about Pokémon Rangers? I'm not!"

    red confusedeyebrows frownmouth ".{w=0.5}.{w=0.5}.{w=0.5}"

    pause 1.0

    red @talkingmouth "Yeah. Neither am I."
    
    skyla closedbrow talking2mouth "Um... anyway, to answer your first question, I'm actually a pilot."

    red @surprised "What? How old are you?"

    skyla -sweat @angry "What?! You don't ask a girl that!"

    red @happy "Oops, sorry! I just... don't you need to be, like, twenty-five to get a pilot's license?"

    skyla -thinking @talkingmouth "Not sure what the rules are in Kobukan, but in Unova, where I come from, you only need to be seventeen. And I was flying solo since I was sixteen."

    red @talkingmouth "Hey, that's pretty impressive. How'd you end up doing that?"
    
    $ AddEvent("Skyla", "Backstory")

    skyla closedbrow talking2mouth "Well, I'm from Mistralton City, in the West, but there's a town on the East side of the region called Lentimas, and they were, like, really isolated, so..."
    skyla happy sweat "I learned to fly so I could, uh, transport stuff over there. Food and medicine and stuff."

    pause 1.0

    red @talkingmouth "Uh... so you had family there, or something?"

    skyla -happy -sweat talkingmouth "Nope. No connection. Well, before I got my pilot's license, anyway."

    red @talkingmouth "So you just... learned to fly planes... to help out a town on the opposite side of the region? That you had no connection to?"

    skyla closedbrow sweat -talkingmouth @talkingmouth "Yyyyyep."

    red happy "That's insane."

    skyla happy sweat "Yeah, I've heard that a lot. But it worked! Lentimas is now officially connected to Mistralton. Since the only other way into Mistralton is through Reversal Mountain, my plane is {i}the{/i} way to get there."

    red -happy @talkingmouth "I'm really impressed. I came up to chat, just expecting a casual conversation, but now... wow."

    skyla -sweat angrybrow smirkmouth "Well, if you thought that was impressive, you should hear what I'll drop on you in our second conversation!"

    red @angrybrow talking2mouth "Is that an invitation?"

    skyla winkbrow "Think of it more like a threat."

    pause 1.0

    skyla -winkbrow @talkingmouth "Soooo...?"

    pause 1.0

    red @closedeyes talkingmouth "Ah, jeez. Sorry. I feel like I've already learned so much about you, I forgot the obvious. What's your name?"

    $ BecomeNamed("Skyla")
    skyla "That'd be Skyla. And it's a pleasure to meet you, [first_name]."

    red @talkingmouth "...Skyla? And you're a pilot?"

    skyla @angry "Yeah, I've heard that one before."

    red @talkingmouth "Forgive me. It was too easy."

    skyla happy "Forgiven! Talk to you later, okay, [first_name]?"

    red @happy "Keep your eyes on me!"

    hide skyla with dis

    pause 2.0

    hide skyla

return