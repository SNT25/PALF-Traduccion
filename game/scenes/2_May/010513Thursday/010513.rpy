label day010513:

$ timeOfDay = "Morning"

call calendar(1) from _call_calendar_38

$ calDate = calDate.replace(day=13, month=5, year=2004)

show morning at vspaz

pause 5.0

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)
show oakbg behind blank2
show homeroom behind oakbg

$ renpy.transition(dissolve)
show screen currentdate

$ HealParty()

hide blank2 with splitfade    
hide morning

pause 1.0

oak @talkingmouth "Good morning, students! Who's ready to continue our survey into the history of Champions?"

show hilbert uniform with dis:
    xpos 0.66

hilbert @talkingmouth "Wait."

hide oakbg with dis

pause 0.5

show oak surprisedbrow frownmouth with dis:
    xpos 0.33

oak @talkingmouth "Mr. Von Schwarzdrachen?"

hilbert @closedbrow talkingmouth "{size=30}Don't say that, it sounds ridiculous...{/size}"

hilbert @talkingmouth "I want to know about [first_name] [last_name]'s Pikachu. You obviously know more about it than any of us, possibly except him."

oak @talkingmouth "Oh? Well, er... I don't think that's entirely relevant to the course I'm teaching right now..."

hilbert @talkingmouth "It's relevant to battle, and relevant to our chances in the Pokémon League. Our first day here, you said only a third of us would qualify. That number will be even lower if we don't know what our opponents can do."
hilbert @angrybrow talkingmouth "You're a teacher. {i}Teach{/i} us."

oak @talkingmouth "Er, well, I..."

menu:
    "{color=#b7669e}[[Charm]{/color} You could have just asked me, Hilbert.":
        $ TraitChange("Charm")

        hilbert @surprised "You would... tell us?"

        pause 1.0

        $ ValueChange("Hilbert", 1, 0.66)

        hilbert @closedbrow talkingmouth "I didn't expect that. Thank you."

    "{color=#60c2f8}[[Wit]{/color} >Summarize what you know about [pika_name]'s new powers":
        $ TraitChange("Wit")

show hilbert surprisedbrow frownmouth 
show oak -surprisedbrow -frownmouth -surprised
with dis

narrator "You quickly explain to the class what you know about [pika_name], with Professor Oak chiming in to provide details occasionally."

hilbert closedbrow "Hmph."

Character("Edgy Bairn") "\"{size=30}...of course the freak would have a freaky Pokémon...{/size}\""

Character("Uncaring Sod") "\"{size=30}...You think he controls his Pokémon, too?{/size}\""

Character("Felonious Prick") "\"{size=30}...probably another special privilege...{/size}\""

hide oak
hide hilbert 
with dis

show leaf uniform at leftside with dis:
    ypos 1.2 zoom 1.3

leaf @talking2mouth "{size=30}You're really just going to come out and tell everybody, huh?{/size}"

red uniform @sweat closedbrow talkingmouth "{size=30}I've learned my lesson. No more secrets.{/size}"

leaf @closedbrow talkingmouth "{size=30}{i}Damn,{/i} you're cool.{/size}"

$ PlaySound("BellChime.ogg")

pause 1.0

oak @talkingmouth "Ah, well, it seems that we may have gotten slightly distracted... no matter. We'll pick this up during our next lesson. Don't forget to prepare for your test, too!"

jump homeroom1transition