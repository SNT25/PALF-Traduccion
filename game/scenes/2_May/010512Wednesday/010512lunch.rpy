label lunch010512:

show may uniform with dis

pause 1.0

may @surprised "[first_name]!"

red uniform "Hey. What's up?"

may @talkingmouth "I need to know--that Pikachu of yours, what's it about? My Dad's been absolutely dragging me for answers, and all I can do is just keep telling him I have no idea!"

red @closedbrow talking2mouth "Oh, right, Professor Birch would probably be interested in that..."
red @talkingmouth "Okay, well, here's the gist."

show blank2 with Dissolve(1.0)

show may surprisedbrow frownmouth

narrator "You give May a short description of [pika_name]'s new power."

hide blank2 with dis

may "{w=0.5}.{w=0.5}.{w=0.5}."

may -surprisedbrow -frownmouth -surprised @talkingmouth "Wow. I never would've expected {i}that.{/i}"

red @happy "Yeah, I was pretty surprised, too. Was that all, though?"

if (GetRelationshipRank("May") > 0 and not HasEvent("May", "Level2SceneVer2")):
    may @surprised "Oh, no! No, there were two more things."
    may @talkingmouth "Um... the first thing is... well, you remember how I was having you taste my food so I could practice making new stuff for Brendan without him noticing?"

    red @talkingmouth "Yeah, sure."

    may @happybrow talkingmouth "Well... you don't need to do that any more!"

    red @confusedeyebrows frownmouth "Hm?"

    may @sadbrow talkingmouth "Brendan and I... after the student council elections, I mean... we talked through what we were both feeling, and I told him the truth about my cooking."

    may @talkingmouth "And he told me the truth about his vegetarianism. {w=0.5}...Which was that he wasn't a vegetarian."

    red @surprised "Huh?"

    may @sadbrow happymouth "He said he loved my cooking at first, and... I can tell he's telling the truth. I saw how his eyes sparkled for the first few years."

    redmind @confusedeyebrows frownmouth "First few {i}years?{/i}"

    may @sad "But... I drove him to the point where he felt he had to {i}lie.{/i} Lie that he was a vegetarian, lie that he didn't like sweet things!"
    may @sad "And... I mean, I was a {i}little{/i} bit mad at him for that, but I was mostly even more upset with myself..."

    may @closedbrow sadmouth "I only found out when Sabrina... you know."

    may @sadbrow happymouth "So I confronted him, and he confessed. Like, right away, he didn't try to hide it. And he said he felt really bad he lied in the first place."

    red @closedbrow talking2mouth "So... you're not sure you can trust him, now?"

    may @surprised "What?"
    may @angry "No! I can {i}absolutely{/i} trust him!"

    pause 1.0

    may @angry "Lying was wrong, but... If I hadn't..."

    pause 1.0

    may @sadmouth "I... I just don't know what to do, now. I don't want to force him into another situation where he feels like he needs to lie."

    red @closedbrow talking2mouth "I getcha."

    pause 1.0

    red @happy "Well, the way I see it, how about we just continue our previous arrangement?"
    red @talkingmouth "You can practice your cooking without poisoning Brendan, but now we can do it all aboveboard. Maybe we can even invite Brendan along a couple times. He could help with the cooking."

    may @talkingmouth "...Yeah. Yeah, that'd be nice!"

    red @happy "Great! Glad it's settled, then. I didn't want to miss out on more of your cooking, after all."

    may @talkingmouth "Speaking of which, what did you think of the lime meringue I made the other day? Serena taught me how to make it."

    red @sweat happyeyes talkingmouth "Enough salt to kill a Garganacl."

    may @sad "Oh..."

    pause 1.0

    may @surprised "Oh, right, there was one other thing!"

else:
    may @surprised "Oh, no! No, there was one more thing."

may @talkingmouth "Um... I think some of Brendan's stuff ended up in your new dorm."

red @sad2eyes talkingmouth "Yeah."

may @happy "Okay, great! Would you mind looking around for a hot-pink suitcase in there? It's got some stuff that's really important to Brendan and I."

red @talkingmouth "Sure."
red @talking2mouth "Does Brendan want to just drop by the dorm this evening? I could pass it off to him."

may @talkingmouth "Sure. Which dorm?"

red @talkingmouth "25."

may @surprised "Ooh, you got one of the {i}fancy{/i} suites."

red @confusedeyebrows frownmouth "Hm?"

may @talkingmouth "Erika told Brendan that the dorms underneath #50 are fancy. Double-sized, four-bedroom, bigger kitchens... must be nice!"

red @happy "It's not bad. Maybe you should come over with Brendan, so you can check it out."

may @sadbrow talkingmouth "Oh, I'd love to, but after class, I have Coordinator Club. It used to be a really stress-free thing, but..."
may @sad "Ever since Lisia became our new club advisor, she's been working us to the bone! How can a girl so cute be so mean?"
may @sadbrow happymouth "Brendan only got out of it because one of my pyrotechnics shot him in the face while we were practicing our routines."

red @happy "Guess she just takes her job seriously. It's about time that every other club gets to feel what we Battle Team members are going through."

may @closedbrow talkingmouth "I guess I should be thankful to Calem for getting her onto the team..."

may @angry "Ooooh, but sometimes I {i}really{/i} wish he'd just been like every other politician, and {i}not{/i} done anything he said he would!"

red @happy "I'm sure he appreciates knowing he stands out like that."
red @talkingmouth "Anyway, I'm going to get some lunch."

may @talkingmouth "Alright. Enjoy!"

if (GetRelationshipRank("May") > 0):
    red @talkingmouth "Sure. Won't be as good as {i}your{/i} cooking, though."

hide may with dis

jump PickTable