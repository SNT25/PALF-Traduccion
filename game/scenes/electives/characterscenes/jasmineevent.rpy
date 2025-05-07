label jasmineevent:

if (IsAbsent("Jasmine", location.title())):
    return

if (((IsDate(26, 4, 2004) and timeOfDay == "Afternoon") or not IsBefore(27, 4, 2004)) and "ClassMeet" not in GetEvents("Jasmine") and not HasEvent("Jasmine", "Jasmine2Part1")):
    $ AddEvent("Jasmine", "ClassMeet")
    
    narrator "You spot a familiar student and go to greet her."
    
    show jasmine uniform with dis

    red uniform happy "Hey, Jasmine."

    jasmine "Hello, [first_name]! Having a good day?"

    red @talkingmouth "Sure am! I see you are, too."
    
    jasmine @talkingmouth "I'm a tad surprised to see you in this class."

    red @surprised "Really? I was going to say the same thing about you!"

    jasmine @happy "Is that a joke about my frequent absences, or about the hardiness of the type in comparison to my, ah, personal hardiness?"

    red @sadbrow happymouth "Ah... whichever one you're less offended by?"

    jasmine @happy "Oh, don't worry about offending me. If I couldn't endure some light ribbing from a friend, I quite simply couldn't endure anything."

    red @talkingmouth "That's very clearly not the case, though."

    jasmine @talkingmouth "No. I'm blessed that it isn't."

    if (IsBefore(1, 5, 2004)):
        red @happy "It's really cool how you're advocating for other people with your accessibility push in the Student Council."
    else:
        red @happy "It's really cool how you're advocating for other people with your accessibility push, even though we didn't get into the Student Council."

    jasmine @talkingmouth "I've met many people in physical therapy. Some are so overwhelmed by their personal challenges that they simply don't have the energy or strength to..."

    show jasmine closedbrow frownmouth

    pause 1.0

    red @sadbrow talking2mouth "...Are you okay?"

    pause 1.0

    jasmine -closedbrow -frownmouth @sadmouth "Yes, apologies. I just... ah. No, no. Today {i}is{/i} a good day. I can continue what I was saying."

    pause 0.5

    jasmine @talkingmouth "Right. As I was saying. Many don't have the ability to fight for anything except their own survival." 
    jasmine @angrybrow happymouth "So, while I'm lucky enough to have the strength within to plant my feet on solid ground, and steel myself for the challenges ahead, I have an obligation to fight for others."

    pause 0.5

    jasmine @lightblush talkingmouth "Oh dear. That sounded a bit pretentious, didn't it?"

    red @talkingmouth "Hey, I have {i}no{/i} room to judge. What you're doing is great. You can say it any way you want."

    jasmine @talkingmouth "...I appreciate your support. Thank you. Now, I should probably sit down before Instructor--"

    show jasmine frownmouth sadbrow:
        ease 0.2 rotate 40 ypos 1.5

    pause 0.2

    show classroom with vpunch

    pause 0.5

    jasmine @talking2mouth "Oh, bother."

    red @surprised "Are... are you okay? I'm sorry, I would've caught you! You just fell so fast that..."

    jasmine @talkingmouth "Oh, it's nothing to be worried about on your end. Minor muscle failure."

    jasmine @happy "Though if it's not too much trouble, I'd take your hand."

    show jasmine closedbrow sweat lightblush with dis:
        ease 2.0 rotate 0 ypos 1.3
        ease 4.0 ypos 1.0

    jasmine @talking2mouth "{i}Phew.{/i}"
    jasmine @talkingmouth "I appreciate that. Thank you."

    red @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    jasmine @sadbrow talking2mouth "{w=0.5}.{w=0.5}.{w=0.5}.Oh, no. I recognize that face. You're pitying me, Mr. [last_name]."

    red @surprised "Wh-what? No! No way. I wouldn't. I, uh..."

    jasmine @happy "That's alright. The real challenge of my life has never been my weakness. It's been proving myself as more than my weakness."

    jasmine @talkingmouth "I hope I can prove that to you, too."

    jasmine -frownmouth @talkingmouth "I'm not an Esper, but I bet I know your thoughts right now. You're thinking 'wow, it's amazing what this girl has done despite her challenges,' right?"

    red @talkingmouth "A little bit."

    jasmine @happy "Then, my goal, quite simply, is to cut off those last three words."

    jasmine @talkingmouth "'Wow, it's amazing what this girl has done.'"

    red @talkingmouth "...Yeah, okay."

    jasmine @talkingmouth "Have a good day, [first_name]."

    hide jasmine with dis

    pause 2.0

return