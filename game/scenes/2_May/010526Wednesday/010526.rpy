label day010526:

$ timeOfDay = "Morning"

call calendar(1) from _call_calendar_51

show morning at vspaz

$ calDate = calDate.replace(day=26, month=5, year=2004)

pause 3.0

$ renpy.music.play("Audio/Morning_ambience.ogg", channel='crowd', loop=True, fadein=1.0)

scene suite
show screen currentdate
show leaf uniform
with splitfade

leaf @happy "Morning, sleeping beauty!"

if (HasEvent("Leaf", "AcceptedConfession")):
    red uniform @talkingmouth "Morning, snoring beauty."
else:
    red uniform @talkingmouth "Morning, Leaf."

leaf @talkingmouth "Just wanted to let you know that we are {i}still{/i} on track for this evening."

red @sadbrow talkingmouth "Great. Uh, do you need to keep updating me every day...?"

leaf @talkingmouth "Honestly, at this point, yeah. Like, I don't want to make excuses, but if {i}one{/i} more thing goes wrong, I want, like, plenty of foreshadowing for me freaking out."

red @talking2mouth "You know--and I probably should've said this before--we could just, like, walk around for a bit. I'd be happy with that."

leaf @talkingmouth "...Yeah, I know."
leaf @sadbrow talkingmouth "...I've got excuses for why all those other ideas didn't work out, but I don't really have an excuse for that one."

if (GetRelationshipRank("Ethan") > 0):
    pause 1.0

    $ AddEvent("Leaf", "LeafEthanConnection")

    show leaf surprisedbrow frownmouth with dis

    red @closedbrow talking2mouth "You know... you and Ethan are kinda similar that way."

    show leaf -surprisedbrow frownmouth with dis

    red @talkingmouth "If something goes wrong in the morning, he feels like the day's a wash. I tell him that's not the case, of course..."

    show leaf sadbrow -frownmouth with dis

    red @happy "And now I'm telling you."
    red @talking2mouth sadbrow "Sometimes the most important part of running is just putting your shoes on. Maybe you didn't hit a new personal best, and maybe you cramped something ten meters out the door."
    red @happy "But you still did it."

    pause 1.0

    red @talkingmouth "Just something to think about. Now, c'mon, let's go to class."

    call clearscreens() from _call_clearscreens_218
    hide leaf with dis

    pause 1.0

    show ethan uniform with dis

    ethan @confusedeyebrows talking2mouth "Leaf and me? I never really thought about it like that before..."

    $ ValueChange("Ethan", 1, 0.5, False)
    $ ValueChange("Leaf", 1, 0.25)

    narrator "Your understanding of Ethan and Leaf increases... as does their understanding of each other!"

scene blank2 with splitfade

narrator "Homeroom passes uneventfully. Sam keeps an active eye on a thick book while teaching. Though the front is covered in thick duct tape, you recognize Sam's copy of 'Teaching for Geniuses.'"

jump homeroom1transition