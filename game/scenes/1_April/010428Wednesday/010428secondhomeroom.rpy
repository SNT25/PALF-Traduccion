label secondhomeroom010428:

scene blank2

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom behind blank2

show oakbg behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade

$ PlaySound("BellChime.ogg")

pause 2.0

oak @talkingmouth "Mm? Oh, that was the bell. Well, I suppose it's for the best. I wanted to get back to the lab as soon as I could, anyway."
oak @talkingmouth "That meteor isn't going to inspect itself!"

hide oakbg with dis

pause 0.5

show hilbert uniform with dis

pause 0.5

red uniform @talkingmouth "Hey, Hilbert."

hilbert @talkingmouth "[first_name]. There's something I need to tell you about."

show hilbert surprisedbrow frownmouth with dis

red @confused "Oh, man, are you going to ask me on a date, too?"

hilbert -surprisedbrow -frownmouth -surprised @angry "What? No. I'm closer to achieving my dream than I've ever been before, so I--"

pause 1.0

hilbert @closedbrow talkingmouth "...Actually, no. Now isn't the time or place for it."

hilbert @talkingmouth "We'll talk about this later."

pause 0.5

red @confused "Uh... sure. Back at the dorm?"

hilbert @talkingmouth "No. I still need to figure some things out with Nate, and I want some privacy when it's time. Are you free Sunday night?"

red @talkingmouth "Sure. For a little bit."

hilbert @talkingmouth "We'll talk then."

red @closedbrow talking2mouth "Uh, sure."

hide hilbert with dis

call freeroam from _call_freeroam_12

call texting from _call_texting_9

jump day010429