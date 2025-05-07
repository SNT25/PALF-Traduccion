label day010421:

$ timeOfDay = "Morning"

if (pikachuobj in playerparty):
    $ playerparty.remove(pikachuobj)

call calendar(1) from _call_calendar_16
$ calDate = calDate.replace(day=21, month=4, year=2004)

show morning at vspaz

pause 3.5

scene blank2 with Dissolve(2.0)

stop music fadeout 1.5

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)

show homeroom behind oakbg

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade    
hide morning

show oakbg with dis

$ renpy.pause(0.6, hard=True)

oak @talkingmouth "...So I suppose you could say that things are really becoming exciting. Who could have guessed that extraterrestrial rock would contain such a fascinating energy?"
oak @talkingmouth "The implications are wondrous. Or, as my new Galarian assistant might say, 'right brilliant!' Hoho."

pause 1.0

oak @talkingmouth "That reminds me. Who here thinks they can name the legendary Pokémon of Galarian myth? Hm... how about you, Miss Birch?"

may surprised uniform "Me? Shoot. I don't know much about myths... {size=25}Psst. [first_name], a little help?{/size}"

menu:
    "{color=#66b77d}[[Knowledge]{/color} >Tell her straight-out":
        red uniform @closedeyes talking2mouth "{size=30}Zacian and Zamazenta. The Warrior Pokémon.{/size}"

        $ TraitChange("Knowledge")

        may @happy "Thanks, [first_name]!"

        may @talkingmouth "Zacian and Zamazenta, Professor Oak!"

        oak "Quite correct. Though I wonder if the confidence with which you said that has anything to do with your proximity to Mr. [last_name]?"

    "{color=#b7669e}[[Charm]{/color} >Give a hint":
        red uniform @closedeyes talking2mouth "They're often called the legendary dogs."

        $ TraitChange("Charm")

        may @happy "{size=30}Oh, I know those!{/size}"

        may @angrybrow happymouth "Raikou, Suicune, and Entei, right, Professor?"

        oak "Not quite. Raikou, Suicune, and Entei are the legendary beasts of Johto, not Galar. And, incidentally, quite feline in their anatomy, as opposed to canine."

        oak "The correct answer to that question is 'Zacian and Zamazenta.' The Warrior Pokémon."

may @sad "Oops..."

oak @talkingmouth "In any case, Zacian and Zamazenta's existence was considered only a historical fancy--a myth not to be taken seriously--until a few years ago, when they made a reappearance in Galar." 
oak @talkingmouth "In fact, there are a great many Pokémon that were thought to be naught but myths and legends until recently. We are certainly living in interesting times... for all the good, and bad, that entails."

jump homeroom1transition