label silverevent:

if (IsAbsent("Silver", location.title())):
    return

if (not HasEvent("Silver", "Backstory") and IsBefore(8, 4, 2004)):
    $ AddEvent("Silver", "Backstory")
    narrator "You spot a familiar student and go to greet him."
    
    show silver uniform with dis

    pause 0.5

    red uniform happy "Hi ho, Silver!"

    silver angry "Piss off."
    silver surprised "Wait, it's you!"
    silver closedbrow sadmouth "Wait, that shouldn't matter."
    silver -closedbrow -sadmouth @sad "...Hi."

    red @confused "That was... a rollercoaster."

    silver closedbrow @talkingmouth "Yeah, I'm still working on... everything."

    red @talkingmouth "I didn't know you were a student here."

    silver @talkingmouth "Yeah, well, I am."

    red @confused "Right. Well, see you around."

    silver sad "Yeah."
    silver surprised "Uh... thanks."
    silver @talkingmouth "For talking to me."
    silver sad "[ellipses]"
    silver sadbrow @sad "I know it's, uh, it's difficult to get through the first five seconds of a conversation with me. But I appreciate that you've, uh, done it. A few times."

    red @sadbrow talkingmouth"Hey, anytime."

    silver @talkingmouth "Uh... yeah. That's all. Bye."

    hide silver with dis

    pause 2.0

return