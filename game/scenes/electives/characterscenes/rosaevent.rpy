label rosaevent:

if (IsAbsent("Rosa", location.title())):
    return

if (not persondex["Rosa"]["Named"]):
    narrator "You spot an unfamiliar student and go to greet her."
    
    show rosa uniform with dis

    pause 0.5

    red uniform happy "Hey there!"

    rosa surprised sweat "Eh?!"

    redmind @surprised "Ok-ay, wasn't expecting that."

    rosa -sweat sadbrow "...Oh, hi. Can I help you?"

    red confusedeyebrows "Uh... no. I mean, I don't think so. I was just going to say hi?"

    rosa surprised "Wait, does that mean... um... you're {i}just{/i} saying hi?"

    red -confusedeyebrows @talkingmouth "Yeah. I'm [first_name]. What's your name?"

    rosa "You don't know my-- {size=30}no, of course not.{/size}"
    $ BecomeNamed("Rosa")
    rosa happy "It's Rosa!~ Here to steal the show, and your heart!"

    red surprised "Uh... wow! You often introduce yourself like that?"

    rosa -happy @talkingmouth "Six days a week."
    rosa "[ellipses]"
    rosa sadbrow frownmouth "It's... kinda embarrassing to say that, huh? I never really thought about it before."

    red happy "Well, I mean, you looked confident while saying it. I think you could play it off well enough."

    rosa -sadbrow -frownmouth @talkingmouth "Aw, thanks, [first_name]. I think I'd better think up a new way to introduce myself, though."
    rosa frownmouth "Hm..."
    rosa happy "It's Rosa!~ Stepping into the spotlight, all eyes on me!"

    pause 1.0

    red @closedbrow talking2mouth "I'd advise workshopping it."

    rosa @sad "Aw... I had a good feeling about that one."
    
    red -happy @talkingmouth "Have you considered, just, like, uh... saying 'Hi. I'm Rosa?'"

    rosa sweat surprised "Huh! Would you believe me if I said I hadn't?"

    red @closedbrow talking2mouth "Seems like a weird thing to lie about."

    rosa -sweat @angry "Well, I'm not! And if I was, you'd have no idea!"

    red @happy "Oh? Are you a good liar?"

    rosa happy "The absolute best! I don't know anyone who lies better than me."

    red @confusedeyebrows talkingmouth "Let's hear one, then."

    rosa sadbrow "...What, you don't trust me?"

    red @talkingmouth "Uh... well, I mean..."
    
    rosa frownmouth "I'm just telling you something about myself. Why do I need to prove it?"
    rosa sadmouth "It doesn't hurt you to believe it, even if I was lying, so why..."
    rosa angrybrow "Why do I always need to prove myself?!"
    
    show rosa:
        ypos 1.0 zoom 1.0
        ease 0.3 ypos 1.1 zoom 1.2

    rosa angry "Why won't somebody please just believe me?!"

    show rosa:
        ypos 1.1 zoom 1.2
        ease 0.3 ypos 1.2 zoom 1.4
    
    rosa "Why does everyone hate--"

    red sad "Wait, hold on! I was just curious, I was just--"

    show rosa:
        ypos 1.2 zoom 1.4
        ease 0.3 ypos 1.0 zoom 1.0

    rosa happy "Psych!~"

    pause 1.0

    red surprised "What?"

    rosa -happy @talkingmouth "That was a lie! I'm not upset at all."

    red @talkingmouth ".{w=0.5}.{w=0.5}.{w=0.5}Holy shit. That's potent."

    rosa happy "Why, thank you."

    red -surprisedbrow -frownmouth -surprised @talkingmouth "I'm seriously impressed. You're a pretty good actress."

    rosa surprised sweat "Eh?!"
    rosa -surprisedbrow -frownmouth -surprised @talkingmouth "Oh, you mean..."
    rosa -sweat @talkingmouth "Well, thanks!"

    red happy "No problem."

    pause 0.5

    red thinking "Hm... I wonder if you could use your acting skills in battle? Like, to misdirect your opponents?"
    rosa "Hm... probably! But my Pokémon would need to know I'm acting, too."
    rosa happy sweat "I'm not sure I'm a good enough trainer to be able to teach them that!"
    red happy "Well, hey, that's why we're at Kobukan, right?"
    rosa -sweat @talkingmouth "Right!"

    $ renpy.music.set_volume(0.1, delay=0.5, channel="music")
    $ renpy.music.play("Audio/Music/Theme snippet.ogg", channel="XYgame", loop=None, fadeout=0.5)

    $ renpy.pause(2.5, hard=True)

    red -happy @talkingmouth "Sounds like you've got a phone call."

    rosa sad "Oh, yeah, I need to answer this before class starts."

    $ renpy.music.stop(channel="XYgame", fadeout=1.5)
    $ renpy.music.set_volume(1.0, delay=0.5, channel="music")

    red @talkingmouth "Well, hey, good talking to you. We'll chat later!"

    rosa -sad @talkingmouth "Sure!"

    hide rosa with dis

    pause 2.0

    hide rosa

return