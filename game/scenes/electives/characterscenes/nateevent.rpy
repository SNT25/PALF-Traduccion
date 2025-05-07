label nateevent:

if (IsAbsent("Nate", location.title())):
    return

if (not persondex["Nate"]["Named"]):
    narrator "You spot an unfamiliar student and go to greet him."
    
    show nate uniform with dis

    pause 0.5

    red uniform @happy "Hi there!"

    nate @happy "Oh, hey! Nice hat."

    red @talkingmouth "Thanks! I got it from--"

    nate angrybrow frownmouth @talking2mouth "Hold it!"

    pause 1.5

    red @surprised "Um... okay? For how long?"

    nate @closedeyes confusedeyebrows talkingmouth "About... seven more words, I'd say?"

    red @confused "Seven more words? What does that mean?"

    nate -angrybrow -frownmouth @happy "{size=30}Locked on.{/size} Southwest Kanto!"

    red @surprised "Huh?!"

    nate @happy "I'm right, right?"

    red @talkingmouth "I mean... yeah. I lived in Pallet Town my whole life. And I got the hat from there. Well, I mean, I actually got it from Sam, but he lives there too, so..."
    red @surprised "Wait, that doesn't matter. How'd you know?"

    nate @talkingmouth "I'm pretty good at reading accents! As soon as you said 'hi there,' I knew you had to be from Kanto, but I couldn't tell where until I had a bit more to go off of."

    red @talkingmouth "Cool. Is that useful?"

    nate @happy sweat "Not at all! It's a neat party trick, though."

    red @talkingmouth "Well, it {i}is{/i} pretty neat. What's your name? I'm [first_name]."

    $ BecomeNamed("Nate")
    nate @talkingmouth "Nate!"

    red @happy "So how'd you end up with that ability?"

    nate @talkingmouth "Oh, I've lived all over. Military mom, you know. Guess you could call me inter-Nate-ional!"

    pause 1.0

    red @unamusedbrow talking2mouth "No pun intended?"

    nate @angry "What? Hell no! I intend every one of my puns."
    nate @closedbrow talkingmouth "Puns are the most valid form of humor out there! Only cowards don't intend their puns!"

    red @happymouth "Interesting perspective. Not sure I agree, but, hey, whatever floats your boat."

    nate surprisedbrow frownmouth @happy "Water, mostly!"

    $ PlaySound("vibrate.ogg")
    pause 1.5

    nate surprised "Oop, gotta go handle something. Seeya, [first_name]!"
    show nate happy with dis

    red @talkingmouth "See you around."

    hide nate with dis

    pause 2.0

return