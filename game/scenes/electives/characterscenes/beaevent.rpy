label beaevent:

if (IsAbsent("Bea", location.title())):
    return

if (not persondex["Bea"]["Named"]):
    narrator "You spot an unfamiliar student and go to greet her."
    
    show bea uniform with dis

    pause 0.5

    red uniform @happy "Hi there!"

    bea @talkingmouth "Hello."
    
    $ BecomeNamed("Bea")
    bea @talkingmouth "My name is Bea. What's yours?"

    red @talkingmouth "It's [first_name]. From Pallet Town in Kanto. You?"

    bea @talkingmouth "Stow-on-Side in Galar. It's a pleasure to meet you."

    red @thinking "[ellipses]"
    red @confused "...Are you sure?"

    bea @talkingmouth "What do you mean?"

    red @talking2mouth "Uh, I mean, I don't want to assume, but you're kinda..."

    pause 1.0

    bea @talkingmouth "Stony-faced?"

    red @happy "That's a ballpark."

    bea @talkingmouth "Apologies. Due to my extensive physical training, my body and face barely have any involuntary movements."

    red @confused "Oh, yeah? How's that work?"

    bea @talkingmouth "Essentially, I have absolute control over every physical aspect of my being. I do not flinch, I do not recoil, and I do not stumble."
    bea @sad "Consequently, I also do not emote."

    red @surprised "Wait, a minute! You just looked sad there!"

    bea sweat "You must be imagining things."

    red @happy "No, you're totally sweating now."

    bea angrybrow frownmouth "[ellipses]"

    pause 1.0

    bea @angry "...DAMN IT!"

    red @surprised "Woah, what?"

    bea @closedbrow talking2mouth "I thought I'd gotten to the point where I had entirely discarded my involuntary reflexes!"

    red @confused "Wait, you WANT this?"

    bea @angry "You! You better take responsibility for making me lose my two-week streak!"

    red @confused "You went two weeks without showing emotions?!"

    bea @angry "I will accept no excuses! Whenever your schedule is unoccupied, meet me in the gym. You'll assist in my training."

    red @talkingmouth "I don't get what you--"

    hide bea with dis

    pause 2.0

    red thinking "...What the hell?"

    hide bea

return