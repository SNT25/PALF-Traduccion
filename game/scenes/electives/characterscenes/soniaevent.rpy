label soniaevent:

if (IsAbsent("Sonia", location.title())):
    return

if (not IsBefore(20, 4, 2004) and "ClassMeet" not in GetEvents("Sonia")):
    $ AddEvent("Sonia", "ClassMeet")

    narrator "You spot a familiar student and go to greet her."
    
    show sonia uniform with dis

    red uniform happy "Hi, Sonia."

    sonia @closedbrow talkingmouth "Oh... hello. [first_name], right?"

    red @talkingmouth "That's me. I'm not forgetting your name, though, not with the entrance you made in the Battle Hall."

    sonia @sad "Ah. That was a rather... big fuss, wasn't it?"

    sonia @closedbrow talking2mouth "Just thinking about the kerfuffle I caused is... rather embarrassing."

    red @talkingmouth "Hey, you got what you wanted. Seems like the embarrassment was worth it."

    sonia @sad "Yes, well. Did I get what I wanted? Suppose that remains to be seen."

    red @frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
    red @talkingmouth "So, have you taken this class before?"

    sonia @talking2mouth "Oh, yes."

    if (location == "electric"):
        sonia @happy "Lieutenant Surge is a real barrel of laughs. He's a fantastic teacher."

        sonia @talking2mouth "My partner, Yamper, has been with me for many years. He's a good boy." 
        sonia @sad "I wanted so desperately to help him become strong, and I certainly ought to have been able to, given the instruction I received. That didn't quite pan out, though."
    elif (location == "fire"):
        sonia @happy "Instructor Blaine is a splendid teacher. His contributions to science--his invention of TMs... he's a remarkable man, who really helps people."

        sonia @sad "There was a thought, back in Galar, that I might become a scientist like my gran at some point. That didn't quite pan out, though."

    pause 0.5

    red @talkingmouth "...What have you been doing after you left Kobukan?"

    sonia @closedbrow sadmouth "Oh... just odd jobs. Anything people would hire me for. Ended up doing a lot of studies on Kobukanian wildlife."

    sonia @sadbrow happymouth "I kept thinking that I should battle... to ensure I didn't forget anything I'd learned, you know?"

    sonia frownmouth @sad "...That didn't happen. I couldn't bear to even look for a battle. And my poor Pokémon are so out of practice, now."

    pause 0.5

    sonia @talking2mouth "Ugh. I'm a wreck."

    pause 1.0

    red @talkingmouth "I think you're being too hard on yourself."

    sonia @surprisedbrow talking2mouth "Oh, you do, do you? I've had three once-in-a-lifetime chances, and I've bungled all of them. What descriptor asides from 'wreck' fits me, then?"

    red @talkingmouth "Determined. You didn't give up."

    sonia @talking2mouth "Ugh. I gave up my dignity, though..."

    pause 0.5

    red @confused "Have you been talking to Erika?"

    sonia @surprised "Well, yes. How'd you know?"

    pause 0.5

    red @talkingmouth "She made her opinions on persistence pretty well known shortly before we got onto the Battle Team."

    sonia @talking2mouth "Ah. Well. She's... not a fan. Of me. I can't say that anything she said was wrong, necessarily, but..."

    sonia sadbrow @sadmouth "I would have appreciated the, ah... break. Just a break would have been all I needed. Just a break..."

    pause 0.5

    sonia @closedbrow talkingmouth "{i}...Sigh.{/i}"

    sonia @sadbrow happymouth "Sorry. I'm not being a very good role model, am I?"

    red @confused "...Would it help if I told you that I don't consider you a role model?"

    pause 0.5

    sonia @surprised "No, not really."

    red @closedbrow sweat "Ooh. Sorry."

    sonia -sadbrow @talking2mouth "Well. I don't know what I can do. Or if I can even do anything. But I, at the very least, have been through this school before. So I might be able to give you a bit of advice."

    red @closedbrow talking2mouth "I'll keep that in mind."

    sonia @talking2mouth "Mm."

    pause 0.5

    sonia @happy "If it helps, I've got a pretty good memory, and I remember most of the assignments I was given last year."

    sonia @talking2mouth "So... like, if you want me to help you... I can."
    sonia @closedbrow talkingmouth "No need to pay, of course. I just want to help my teammates. Reckon that might make up for last year."

    red @happy "Hey, don't worry about it. If I need help, I'll reach out. Good to know I can rely on you."

    sonia @surprisedbrow happymouth "Well, I wouldn't go {i}that{/i} far, now."

    hide sonia with dis

    pause 2.0

return