label hildaevent:

if (IsAbsent("Hilda", location.title())):
    return

if (not persondex["Hilda"]["Named"]):
    narrator "You spot an unfamiliar student and go to greet her."
    
    show hilda uniform with dis

    pause 0.5

    red uniform happy "Hi there!"

    hilda happy "Hi."

    red @talkingmouth "What's your name?"

    $ BecomeNamed("Hilda")
    hilda surprised "Uh, Hilda. Can I help you?"

    red -happy @talkingmouth "Not really, just learning who my new classmates are."
    red @closedbrow talking2mouth "Wait, Hilda?"
    red @talkingmouth "Hey, Hilda! You're the girl who terrifies the hell out of Hilbert, right?"

    hilda surprised "Oh my god. You're [first_name]."

    red @surprised "Huh? Has he told you about me?"

    hilda happy "Yeah, he hates you least!"
    hilda -happy "[ellipses]"
    hilda sad sweat "I'm... seriously sorry about his {i}everything{/i}, by the way."

    red @happy "Hey, no need to apologize on his behalf."

    hilda closedbrow smirkmouth -sweat @talkingmouth "I kinda do... we go way back. And if I'd known which lever to pull way back then, I sure as hell would have."

    red @talkingmouth "Well, trolley problems always look easiest from an omniscient perspective. Don't beat yourself up for past decisions."

    hilda sad "...Yeah, uh, I'll take that under advisement."
    show hilda -sad with dis

    red @confused "So, uh, just out of curiosity, how do you keep Hilbert... uh... in-line? Like, how do you make him heel?"

    hilda frownmouth "I wish there was a single trick that worked all the time. Sometimes I have to bribe him, sometimes I have to threaten him, sometimes both..."

    red @talkingmouth "The ol' carrot and stick. Got it. Well, all I know about you, I've heard Hilbert muttering under his breath."
    red @happy "What's the real Hilda like?"
    
    hilda closedbrow talking2mouth "Well, ignoring my full-time job as a Hilbert wrangler, then..."
    hilda ".{w=0.5}.{w=0.5}.{w=0.5}"
    hilda sad "I play tennis. Sometimes."

    red @talkingmouth "Oh, yeah? I used to play. Are you any good?"

    hilda happy "Not really! I just liked hitting the ball. Feels good to just {i}smash{/i} something in the face, you know?"

    red @talkingmouth "I'd figure you'd be more of a Baseball girl, then."

    hilda sadbrow -happymouth @talkingmouth "I did try that. Couldn't keep up with the speed, though. And that tiny little ball heading at you at, like, five hundred miles per hour?"
    hilda closedbrow talking2mouth "A baseball hit my ass once, left a bruise for weeks. I beat the hell out of the pitcher--because the punk totally did it on purpose--but that definitely sealed me as a tennis girl."
    hilda sad "God, though, it's been so long since I've actually played..."

    red @talkingmouth "Want to?"

    hilda @happy "Believe me, {i}god yes{/i}. I just don't have any free time."
    hilda thinking veins "I'm a full-time student at Kobukan Academy {i}and{/i} Hilbert's goddamn mom. I don't even have time to breathe my own air."

    red @talkingmouth "Mmm. Well, if I found you outside of classes, and asked if you had some time then... would you hate that?"

    hilda -thinking -veins @talkingmouth ".{w=0.5}.{w=0.5}.{w=0.5}"
    hilda happy "Nah. I wouldn't hate that."

    red @talkingmouth "Sounds like a plan, then. See you around, Hilda."
    hilda -happy @talkingmouth "Yeah, see ya."

    hide hilda with dis

    pause 2.0

return