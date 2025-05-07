label tiaevent:

if (IsAbsent("Tia", location.title())):
    return

if (((calDate.day > 12 and timeOfDay == "Afternoon") or not IsBefore(14, 4, 2004)) and not HasEvent("Tia", "Backstory")):
    $ AddEvent("Tia", "Backstory")
    narrator "You spot a familiar student and go to greet her."
    
    if (IsBefore(17, 4, 2004)):
        show tia uniform with dis
    else:
        show tia uniform hat with dis

    pause 0.5

    red uniform @happy "Oh, hey, Ti- Bianca! So, you decided to take this elective, huh?"

    show tiaintro with dis

    if (IsAfter(16, 4, 2004)):
        show tiaintrohat with dis

    pause 5.0

    show tia happy with dis

    narrator "Tia nods happily, pantomiming a dragon breathing fire, then puts her fingertips on her forehead and concentrates intensely."

    red @happy "Dragon and Psychic, got it."

    show tia -happy with dis

    hide tiaintro 
    hide tiaintrohat
    with dis

    red @talkingmouth "Well, uh, it's good to see that you're getting comfortable at Kobukan. Tell me if there's anything I can do to help you out."

    show tia:
        ease 0.5 xpos 0.85 alpha 0.0 zoom 1.3 ypos 1.2

    narrator "Tia immediately walks to your side and grabs your arm, motioning at you to sit beside her."

    red @surprised "Oh! Uh... yeah, okay. I can do that."

    narrator "You sit down quickly, hoping the other students don't notice the blush spreading to your cheeks."

    pause 1.0

    if (location == "psychic" and IsPresent("Sabrina", "Psychic")):
        show sabrina uniform with dis

        sabrina "{w=0.5}.{w=0.5}.{w=0.5}."

        sabrina "I have read thousands of minds across two decades."

        sabrina "I have witnessed every perverse desire imaginable. I have examined the depths of human depravity, and read the pure-hearted innocence of a child."

        sabrina "And even so... I must ask..." 
        
        sabrina talking2mouth sadbrow "What the hell is this?"

        hide sabrina with dis

    elif (location == "dragon" and IsPresent("Leaf", "Dragon")):
        show leaf uniform with dis

        leaf @surprised "Holy shit. I thought {i}I{/i} was forward."

        leaf @flirttalk "Well, I'm going to have to step it up!"

        hide leaf with dis

return