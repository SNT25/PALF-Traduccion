label lunch010429:

pause 0.5

show tia hat uniform at centerside 
with dis

pause 0.5

if (GetCharValue("Tia") >= 10):
    red uniform @happy "<Hey, Tia.>"

    tia "Hi, [first_name]."

    red @confusedeyebrows talkingmouth "<Whitney told me you wanted to talk to me?>"

    tia @closedbrow talking2mouth "Yeah..."

    pause 0.5

    tia @talkingmouth "Um... I have a secret. That I want to tell you."

    pause 0.5

    red @closedbrow talking2mouth "Hm. Is this about the bad person?"

    tia @sadbrow talkingmouth "Not exactly."
    tia @sad2eyes sadeyebrows talkingmouth "It's more about why I was sent here to {font=fonts/sign.ttf}fight them{/font}."

    red @talkingmouth "Sure thing. You want to go out into the garden, and tell me now?"

    tia @sad2eyes talking2mouth "I think... we {font=fonts/sign.ttf}might{/font} need more privacy."

    red @confused "Oh, yeah, the garden's always pretty full at lunchtime."
    red @talkingmouth "<After school, then?>"

    tia @talkingmouth "Would Sunday work? {font=fonts/sign.ttf}Sunday{/font} morning?"

    red @closedbrow talking2mouth "Well, my Sunday is pretty busy already, but I think I can manage that."

    tia @talkingmouth "Thanks, {font=fonts/sign.ttf}trainer{/font}."

    red @happy "<You're welcome.>"

else:
    red uniform @talkingmouth "Hey, Tia."

    show tia:
        ease 0.5 ypos 1.2 zoom 1.3
        pause 0.5
        ease 0.5 ypos 1.0 zoom 1.0 

    pause 1.0

    narrator "Tia places a piece of paper in your hands, then looks at you expectantly."

    tia "I have a secret I want to tell you. Please meet me in the garden on Sunday morning.\n-Tia"

    red @closedbrow talking2mouth "Well, my Sunday is pretty busy already, but I think I can manage that."

    show tia happy with dis

    narrator "Tia makes a spinning motion with her hand, and points at the paper. You turn it over, and on the back, it says..."

    tia "Thank you!"

    red @happy "Heh. You're welcome."

hide tia with dis

jump PickTable