label gardeniaevent:

if (IsAbsent("Gardenia", location.title())):
    return

if (not persondex["Gardenia"]["Named"]):
    narrator "You take this time to stretch your arms. In doing so, you inadvertently knock over a pencil."

    $ PlaySound("Body Roll.ogg")

    show gardeniaintro with vpunch

    red uniform @surprised "Holy-! What a dive!"

    ethan uniform @surprised "Woah, that girl was sitting two rows behind us!{w=0.5} How did she react that fast?"

    red @happy "That was a nice catch!"

    hide gardeniaintro 
    show gardenia uniform
    with dis

    gardenia @happy "Thanks! But it was nothing."
    
    red @happy "No, I'm serious! Your reaction time is insane.{w=0.5} I barely reacted myself."
    
    gardenia @sadbrow sadmouth "Seriously? Partner, you need to be more careful!"
    gardenia @angrybrow talking2mouth "This was just a pencil, but what if you were dropping a genuine antique Galarian teapot? That'd be the end of your financial future!"

    red @confused "I'd mostly be confused as to how I got my hands on a Galarian teapot in the first place."

    gardenia @happy "Dude, once you have something in your hands, make sure it {i}stays{/i} in your hands. Don't drop it, don't trade it, don't give it away. The only thing you should be doing is {i}investing{/i} it!"
    
    red @closedbrow talking2mouth "Oh. Is this a sales pitch of some kind?"

    gardenia @happybrow happymouth "Depends. Do you want to be a boss babe? Work from your dorm? Bring in 10k a week?"

    red @upeyes frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    gardenia @surprised "Oh, shit, you're actually considering it. You must be pretty desperate."

    red @closedbrow sweat talking2mouth "Financial security has a pretty low catch rate, in my experience."

    gardenia @happy "Well, why didn't you tell me so? I can {i}actually{/i} help you."

    red @confused "How do you figure?"

    gardenia @sadbrow talkingmouth "Well, I can't just say it here in class, in front of everyone else, can I? Just grab me outside of class at some point, and we can talk business. Oh, even better, sign up for one of my Yoga classes, and we can talk then."

    $ BecomeNamed("Gardenia")

    gardenia @happy "Orrrrr you could buy my book. 'Green with Envy, by Gardenia,' available in most retail bookstores, and the number one guide to business written by a self-made woman born in Middle Sinnoh from the years of 1985 to 1987."

    red @confused "That's pretty specific."

    gardenia surprisedbrow frownmouth @happy "Yeah, it's not a great book. Besides, who has time to read nowadays? I'd try the first thing. Time is money, and--"
            
    $ PlaySound("vibrate.ogg")

    pause 2.0

    gardenia happy "--that's our time!"

    show gardenia:
        xpos 0.5 ypos 1.1 zoom 1.0 alpha 1.0
        ease 0.4 xpos -0.5 ypos 1.3 zoom 1.5 alpha 0.0

    narrator "Gardenia nimbly goes back{w=0.3}--or more like {i}jumps{/i} back--into her seat."

    pause 1.5

    redmind @thonk "Hm. She didn't ask my name."

    hide gardenia

    pause 2.0

return