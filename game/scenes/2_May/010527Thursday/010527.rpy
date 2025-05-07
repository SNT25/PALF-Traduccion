label day010527:

stop music fadeout 1.5

call calendar(1) from _call_calendar_52

python:
    calDate = calDate.replace(day=27, month=5, year=2004)
    timeOfDay = "Morning"
    renpy.pause(2.5, hard=True)
    renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)

scene homeroom
show screen currentdate
show oak
with splitfade

oak @talkingmouth "Good morning, class. In a departure from my traditional identity as Professor Oak, let me be Frank."

pause 0.5

oak @closedbrow sweat talking2mouth "Well, {i}I{/i} thought it was funny."

pause 1.0

oak @sweat happy "In any case...!"
oak @sweat closedbrow talking2mouth "Your test this evening is {i}not{/i} a simple one."
oak @talkingmouth "However, I fully expect a resounding success is within the abilities of each and every one of you."
oak @talkingmouth "This test will require you to understand the properties of the move {i}Camouflage,{/i} and how it interacts with terrains."
oak @closedbrow talking2mouth "It is not, I warrant, an overly popular move, but it is one every student should know, as there is rarely a better way to make use of your surroundings."

pause 1.0

oak @talkingmouth "There are four common types of terrain. Misty, Grassy, Psychic, and Electric."

flannery uniform @tiredbrow talking2mouth "What about Burial Ground? Instructor Bertha invented that one."

oak @talkingmouth "She did, and it's a marvelously clever move that assists both Ghost-types {i}and{/i} Ground-types--and, to a lesser extent, Flying and levitating Pokémon."
oak @closedbrow talking2mouth "However, you are unlikely to see that move in the wild unless it's being used by someone who had the pleasure of being taught directly by Bertha."

pause 0.5

oak @closedbrow talking2mouth "That being said, I do believe that Champion Cynthia was taught by Instructor Bertha, and I think her Spiritomb is a known user of the move... hm."
oak @happy "Something to keep in mind for the ambitious amongst you." 
oak @talking2mouth "However, this test will not cover that material."

pause 0.5

oak @talkingmouth "Now, {color=#EC8FE6}Misty Terrain{/color} halves the power of Dragon-type moves, and is used largely by Fairy-types."
oak @closedbrow talkingmouth "{color=#63BB5B}Grassy Terrain{/color}, perhaps unsurprisingly, increases the power of Grass-type moves."
oak @happy "And I trust in your intelligence enough to know which types {color=#F97176}Psychic{/color} and {color=#F3D23B}Electric{/color} Terrains boost!"
oak @talking2mouth "Now, these moves {i}do{/i} have other effects, but our interest here is in how Camouflage's effect changes when used on these Terrains."
oak @talkingmouth "You see, Camouflage changes the type of the user depending on their surroundings. In a forest, you're liable to turn into a Bug-type. In a field, a Grass-type." 
oak @sad2eyes talking2mouth "In Instructor Melony's frigid classroom, well, an Ice-type seems a reasonable choice for Camouflage."
oak @closedbrow talkingmouth "This effect is altered by Terrains, which take priority over whatever one's actual environs are."
oak @sweat closedbrow talking2mouth "I again trust in your intelligence to realize which type each Terrain shifts the effect of Camouflage toward."

pause 1.0

oak @surprised "Oh! Actually..."
oak @happy sweat "Apologies, students. I told you to disregard the effect of the Terrains themselves earlier, but it's somewhat important to remember that Psychic Terrain makes grounded Pokémon immune to priority moves."
oak @closedbrow talking2mouth sweat "Do keep that in mind."

pause 0.5

oak @talkingmouth "There are various other mechanisms that interact with terrains... Seeds and Extenders, for example... but I'd rather not confuse the issue."

pause 1.0

oak @talking2mouth "Right, then. Let's quickly ensure that you were listening. Ms. Milton, you ought to know this."

whitney uniform @surprised "Eh-eh?"

oak @talkingmouth "Of the Terrains I mentioned, which one does {i}not{/i} boost the power of moves of the corresponding type used on it?"

whitney @closedeyes sadeyebrows sweat talkingmouth "{size=30}Shoot, I was too surprised he was actually teaching, I kinda zoned out... Flan?{/size}"

flannery uniform @tiredbrow talkingmouth "{size=30}Not a chance.{/size}"

redmind uniform @thinking "...Looks like Whitney could use some help."

whitney @happy sweat "{size=30}Psst! Please, a hint, [first_name]?{/size}"

menu:
    "Moist Terrain":
        show oak closedbrow frownmouth sweat with dis
        
        narrator "Oak shakes his head with frustration."

        oak @talking2mouth "No, I'm afraid that's quite wrong. There is no such thing as 'Moist Terrain'--unless, perhaps, it is raining."
        oak -closedbrow -frownmouth -sweat @talkingmouth "For future reference, the correct answer would be Misty Terrain, which halves Dragon-type moves' power, instead of boosting Fairy-type moves' power."
                
        $ ValueChange("Whitney", -2, 0.25)

        whitney @angry "{size=30}Hey! What's up with the bogus info? I thought you were good at this class!{/size}"

        red @talking2mouth sad2eyes angryeyebrows "{size=30}You wouldn't have to ask me if you were paying attention...{/size}"

    "Grassy Terrain":
        show oak closedbrow frownmouth with dis

        narrator "Oak shakes his head."

        oak @talking2mouth "No, I'm afraid that's wrong. Grassy Terrain boosts the power of Grass-type moves by 30%%. Incidentally, it also halves the power of Magnitude, Earthquake, and Bulldoze."
        oak -closedbrow -frownmouth @talkingmouth "For future reference, the correct answer would be Misty Terrain, which halves Dragon-type moves' power, instead of boosting Fairy-type moves' power."

        $ ValueChange("Whitney", -1, 0.25)

        whitney @angry "{size=30}Hey! What's up with the bad info?{/size}"

        red @sadbrow talkingmouth "{size=30}Sorry, got a bit confused...{/size}"

    "Electric Terrain":
        show oak closedbrow frownmouth with dis

        narrator "Oak shakes his head."

        oak @talking2mouth "No, I'm afraid that's wrong. Electric Terrain boosts the power of Electric-type moves by 30%%. Incidentally, it also prevents grounded Pokémon from falling asleep."
        oak -closedbrow -frownmouth @talkingmouth "For future reference, the correct answer would be Misty Terrain, which halves Dragon-type moves' power, instead of boosting Fairy-type moves' power."

        $ ValueChange("Whitney", -1, 0.25)

        whitney @angry "{size=30}Hey! What's up with the bad info?{/size}"

        red @sadbrow talkingmouth "{size=30}Sorry, got a bit confused...{/size}"

    "Misty Terrain":
        narrator "Oak nods."

        oak @talking2mouth "Quite right, Ms. Milton. It is a curious move, being one that halves the damage of Dragon-type moves, even though it is primarily learned by Pokémon entirely immune to Dragon-type moves."
        oak @happy "But even such a contradictory move has its uses."

        $ ValueChange("Whitney", 1, 0.25)

        whitney @happy "{size=30}Thanks a bunch!{/size}"

        red @sadbrow talkingmouth "{size=30}Any time.{/size}"

    "Burial Ground":
        show oak surprisedbrow frownmouth sweat with dis

        narrator "Oak considers this."

        oak @talking2mouth "Well, that isn't the answer I was looking for, but I {i}did{/i} mention it, and it doesn't boost the power of Ground or Ghost-type moves, so I suppose that's technically correct. A point for thinking outside of the box, then."
        oak -surprisedbrow -frownmouth -sweat @talkingmouth "Though for future reference, the more commonly-accepted answer would be Misty Terrain."

        $ ValueChange("Whitney", 1, 0.25)

        whitney @happy "{size=30}Thanks a bunch!{/size}"

        red @sadbrow talkingmouth "{size=30}Any time.{/size}"

    "Psychic Terrain":
        show oak closedbrow frownmouth with dis

        narrator "Oak shakes his head."

        oak @talking2mouth "No, I'm afraid that's wrong. Psychic Terrain boosts the power of Psychic-type moves by 30%%. Incidentally, it also further boosts the power and range of the move Expanding Force."
        oak -closedbrow -frownmouth @talkingmouth "For future reference, the correct answer would be Misty Terrain, which halves Dragon-type moves' power, instead of boosting Fairy-type moves' power."

        $ ValueChange("Whitney", -1, 0.25)

        whitney @angry "{size=30}Hey! What's up with the bad info?{/size}"

        red @sadbrow talkingmouth "{size=30}Sorry, got a bit confused...{/size}"

stop music fadeout 2.5

oak @talking2mouth "Now, let's move on. I wish to make clear how Terrains can be set up--and removed."
oak neutralbrow neutralmouth @closedbrow talking2mouth "The traditional methodology is to use the moves that share the Terrains' names. However, there are various other methods... which I will go into in more detail later..."

narrator "Professor Oak lectures on the interaction of terrain-setting moves, terrain-setting abilities, and Camouflage at length."
narrator "His teaching style has not noticeably changed, but... the information being imparted seems {i}much{/i} more useful now, at least."

jump homeroom1transition