label nessaevent:

if (IsAbsent("Nessa", location.title())):
    return

if (not persondex["Nessa"]["Named"]):
    narrator "You spot a somewhat-familiar student and go to greet her."
    
    show nessa uniform with dis

    pause 0.5

    red uniform happy "Hi there!"

    nessa @talkingmouth "Hey. What's up?"

    red @talkingmouth "I was thinking you looked kinda familiar. Have I seen you somewhere?"

    nessa @closedbrow talkingmouth "Maybe. I've been a model for a few magazines."

    red @talkingmouth "Oh, is that right? What's your name? I'm [first_name]."

    $ BecomeNamed("Nessa")
    nessa @talkingmouth "Nessa, but I often went under other names. I was a minor until recently, so, you know. Privacy concerns."

    red @talkingmouth "Sure, sure. So how come a model like you is here at Kobukan?"
    red surprised "Ah, shit, that wasn't rude, was it?" 
    red -surprisedbrow -frownmouth -surprised @talkingmouth "I just meant that you've already got a career path, and at such a young age, you know?"

    nessa happy "It's cool."
    nessa -happy "[ellipses]"
    nessa closedbrow talkingmouth "I think... I'm here because I'm afraid it won't last."

    red @thinking "[ellipses]"

    nessa "You know how water erodes rocks over millions of years? Time does the same thing to beauty. Which I guess doesn't sound very modest."
    nessa happy "Sorry, not sorry. I know I'm hot."
    nessa sad "But, you know, I'm not going to have what I have now forever. So I need a backup plan."

    red @talkingmouth "Makes a lot of sense."

    nessa happy "Besides, I always had an interest in Pokémon. I was actually on my way to get my first Pokémon when a recruiter saw me in the street."
    nessa -happy @talkingmouth "After the guy talked to my parents, we went back down to the beach and I caught my Drednaw. Back then, I figured that modeling would be something I'd do to fund my Pokémon career..."
    nessa "And now it's the opposite."
    nessa happy "Heh."
    nessa -happy @talkingmouth "You're a good listener. You're probably only tolerating me 'cause I'm gorgeous, but, hey, thanks anyway."

    red happy "Hey, I may've come up to you 'cause you're hot, but now I'm interested in your story."

    nessa "I respect that. Whatever opens the door, right?"
    nessa @thinking "[ellipses]"
    nessa "Look, I'm going to be really busy this year, so I don't have time for anything serious, but if you ask me on a date, I'll say yes."

    menu:
        "I'm flattered.":
            red @talkingmouth "Cool. I'm not going to ask you in the classroom, though."
            
            nessa @talkingmouth "Thank god. Do {i}not{/i} want to associate this place with dates."

            $ BecomeContacted("Nessa")

            nessa @talkingmouth "Call me. I'm free whenever."

        "Could we get to know each other first?":
            $ AddEvent("Nessa", "DateDeny")
            nessa @frownmouth surprisedbrow "{w=0.5}.{w=0.5}.{w=0.5}."

            nessa @talkingmouth "That's new. But sure."

            red @talkingmouth "Cool. I'll call you later?"

            nessa @talkingmouth "Okay."

            $ BecomeContacted("Nessa")

            nessa @talkingmouth "Now you will. I'm free whenever."

            $ persondex["Nessa"]["Relationship"] = "Classmate"

    nessa happy "See you around."
    hide nessa with dis

    pause 2.0

    ethan uniform surprised  @talkingmouth "...Dude, {i}teach me.{/i}"

    hide nessa

return