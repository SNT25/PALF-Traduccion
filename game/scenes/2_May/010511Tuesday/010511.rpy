label day010511:

stop music fadeout 1.5

$ timeOfDay = "Morning"
call calendar(1) from _call_calendar_36

$ calDate = calDate.replace(day=11, month=5, year=2004)

show morning at vspaz

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)

show oakbg behind blank2
show homeroom behind oakbg

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 wth splitfade i   
hide morning

$ renpy.pause(0.6, hard=True)

if (not HasEvent("Blue", "RejectGame")):
    redmind tired uniform @frownmouth "We were up {i}way{/i} too late last night."

    show leaf uniform flirtbrow frownmouth with Dissolve(2.0)

    leaf "I{w=0.5}.{w=0.5}.{w=0.5}."

    show leaf closedbrow:
        linear 0.5 ypos 1.9 rotate 5

    show homeroom with vpunch

    pause 1.0

    show whitney uniform at rightside with dis

    pause 0.5

    whitney @confusedeyebrows talkingmouth "Late night?"

    red @talking2mouth tired "Yeah."

    pause 1.0

    whitney @talking2mouth "So... I feel a bit bad about this, but we were hoping you could help us."

    red @confusedeyebrows tired talking2mouth "'Us'?"

    show flannery uniform tired at leftside with dis

    flannery @tiredbrow talking2mouth "You look like I feel."

    red @closedbrow talkingmouth "Bleh. I probably feel worse. Anyway, what do you two want help with?"

    whitney @talking2mouth "Tia's gone. She's {i}been{/i} gone. For, like, a week. You were only gone for three days. So Flan and I are going to go out looking for her after school."

    red @surprisedbrow tired surprisedmouth "Huh?"
    red @tiredhappy happyeyes talkingmouth "Great minds... think like... something that fools don't differ?"

    show leaf flirtbrow:
        xpos 0.5 ypos 1.9 rotate 5
        parallel:
            ease 0.2 xpos 0.51
            ease 0.2 xpos 0.49
            ease 0.2 xpos 0.51
            ease 0.2 xpos 0.49
            ease 0.2 xpos 0.5
        parallel:
            ease 1.0 ypos 1.0 rotate 0

    pause 0.5

    leaf @talking2mouth "That was even more garbled than normal."

    red @closedbrow tired talkingmouth "Yeah, I'm not... I'm just going to... yeah."

    leaf @talking2mouth "Flan, Whit, let's talk during Gym class, okay? The caffeine should have hit my system by then."

    whitney @surprised "Uh... sure!"

    red @talkingmouth happyeyes tiredhappy "{cps=15}{size=30}Okay. I'm going to sleep now.{/size}"

    call clearscreens from _call_clearscreens_145

    scene blank2 with transeye

else:
    red uniform @talkingmouth "Morning, Leaf. Did you guys have fun?"

    show leaf uniform flirtbrow frownmouth with Dissolve(2.0)

    leaf "I{w=0.5}.{w=0.5}.{w=0.5}."

    show leaf closedbrow:
        ease 0.5 ypos 1.5 rotate 5

    show homeroom with vpunch

    show whitney uniform at rightside with dis

    whitney @confusedeyebrows talkingmouth "Late night?"

    red @talking2mouth "Guess so."

    pause 1.0

    whitney @talking2mouth "Well, you seem awake enough. I was hoping you could help us."

    red @confusedeyebrows talking2mouth "'Us'?"

    show flannery uniform tired at leftside with dis

    flannery @tiredbrow talking2mouth "Leaf, you look like I feel."

    leaf "Grrrn."

    red @closedbrow talkingmouth "What do you two want help with?"

    whitney @talking2mouth "Tia's gone. She's {i}been{/i} gone. For, like, a week. You were only gone for three days. So Flan and I are going to go out looking for her after school."

    red @surprised "Huh?"
    red @happybrow talkingmouth "Great minds... think like... something that fools don't differ?"

    show leaf flirtbrow:
        xpos 0.5 ypos 1.5 rotate 5
        ease 0.5 ypos 1.0 rotate 0

    leaf @talking2mouth "That was even more garbled than normal."

    red @sad2eyes talkingmouth "Hey, that's a difficult one in the best circumstances."

    leaf @talking2mouth "Flan, Whit, let's talk during Gym class, okay? The caffeine should have hit my system by then."

    whitney @surprised "Uh... sure!"

    hide whitney
    hide flannery
    with dis

    narrator "Just before Leaf falls asleep, the bell rings, sparing her a tongue-lashing from Professor Oak."

jump homeroom1transition