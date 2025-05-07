label day010528:

$ timeOfDay = "Morning"

call calendar(1) from _call_calendar_53

show morning at vspaz

$ calDate = calDate.replace(day=28, month=5, year=2004)

pause 3.0

$ renpy.music.play("Audio/Morning_ambience.ogg", channel='crowd', loop=True, fadein=1.0)

scene suite
show screen currentdate
show leaf flirtbrow frownmouth uniform
with splitfade

red uniform @happy "Good..."

pause 1.0

red @confused "Okay, I was {i}going{/i} to say good morning, but I'm worried what you'll do to me if I finish that sentence."
red @sadbrow talkingmouth "What's up?"

leaf @talking2mouth "I... did it."

pause 0.5

red @happy "Never doubted it for a moment."

pause 0.5

red @confused "What was it you did, again?"

leaf @closedbrow talkingmouth "I figured out how to patch the Ethan/Yellow/Blue bridge. I stayed up all night working on a plan, but I have it figured out."
leaf @talkingmouth "And it's one of my best ones, if I do say so myself. We'll subtly execute it across a timespan of four days, and it involves a local escape room, Nate owing me a favor, and seven pounds of smoked carrots."

pause 1.0

red @closedbrow talking2mouth "That's... great. There's, uh, just one issue."

leaf @angrybrow angrymouth "There {i}better not be.{/i}"

show leaf surprisedbrow frownmouth:
    xpos 0.5
    ease 0.5 xpos 0.8

show blue uniform:
    xpos -0.2 
    ease 0.5 xpos 0.2

show yellow uniform:
    xpos -0.2 xzoom -1
    ease 0.5 xpos 0.4

show ethan uniform:
    xpos -0.2
    ease 0.5 xpos 0.6

pause 0.5

blue @closedbrow talking2mouth "Hey, you two! We're going to get breakfast together. Get your asses in gear, slowpokes!"

leaf @sadbrow talking2mouth "W-we...?"

blue @surprised "Huh? Yeah. We. The dorm. Us. That means you two, as well."

show leaf angrybrow angrysmilemouth with dis

blue @closedbrow talking2mouth "What, did you stay up all night again? You really gotta start taking this school seriously. No way you'll make a dent if you keep half-assing it like this."

blue @happy "We'll be in the cafeteria. But I'm {i}not{/i} saving you slackers a seat!"

ethan @winkbrow talkingmouth "{size=30}I will, don't worry.{/size}"

red @closedbrow talkingmouth sweat "Thanks, man."

show blue:
    xpos 0.2
    ease 0.5 xpos 1.2

show yellow:
    xpos 0.4
    ease 0.5 xpos 1.2

show ethan:
    xpos 0.6
    ease 0.5 xpos 1.2

pause 1.0

leaf "{w=0.5}.{w=0.5}.{w=0.5}."

menu:
    "[knowledgeoption]Can I know what the plan was?":
        scene blank2 with splitfade

        narrator "Leaf sullenly hands you a twenty-page document with bookmarks, titles, an outline, and an index."

        narrator "...Though impressive, it's clear the author was becoming more and more delirious as it was written."

        $ TraitChange("Knowledge")

    "[witoption]Keep the plan in your back pocket.":
        red @sadbrow talkingmouth "Knowing Blue, we might need it in the future."

        $ TraitChange("Wit")

        leaf @talking2mouth "...Ugh."

        narrator "It seems Leaf is not in the mood to appreciate your [witcolor]wit{/color}."

        scene blank2 with splitfade

narrator "You help Leaf get to the cafeteria, scarf down some Charjabug-shaped waffles, then head to Professor Oak's homeroom, where he continues to surprise by teaching somewhat relevant information..."
narrator "Besides an unexpected and unasked-for tangent detailing the breeding habits of Wailord."

whitney uniform mediumblush @surprised "W-with a... {w=0.5}a {i}Skitty?!{/i}"

jump homeroom1transition