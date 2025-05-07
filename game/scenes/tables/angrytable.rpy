label angrytable:

$ randnum = Random()

hide blue
hide misty
hide flannery
hide hilbert
show blue angry uniform at farleftside with dis
show misty angry uniform at midleftside with dis
show flannery angry uniform at midrightside with dis
show hilbert angry uniform at farrightside with dis

label aftercharsangry:

if (IsBefore(11, 4, 2004)):
    jump tabletalkangry

menu:
    ">Study with Blue":
        blue happy "Help you study?! Hah! You must be really desperate! But sure, I might be the only person who can actually teach you anything!"
        $ classtype = ""
        menu:
            ">Study Flying-types":
                $ classtype = "Flying"

            ">Study Dragon-types":
                $ classtype = "Dragon"

            "Nevermind":
                blue angry "Oh, piss off."
                jump aftercharsangry

        narrator "[blue_name] crows obnoxiously the entire time you're studying together, but you do manage to learn a few new concepts. [blue_name] clearly enjoys the opportunity to lord this over you."
        $ ValueChange("Blue", 1, 0.12)
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Misty":
        misty surprised "Huh? Me, help you study? I mean, I guess..."
        $ classtype = ""
        menu:
            ">Study Water-types":
                $ classtype = "Water"

            ">Study Ice-types":
                $ classtype = "Ice"

            "Nevermind":
                misty angry "What's your problem?! Just jerking me around, huh?"
                jump aftercharsangry

        narrator "Misty loses her temper while teaching a few concepts, but manages to calm herself down enough to be a helpful study partner, culminating in a sheepish..."
        misty closedbrow talking2mouth "Thanks, I guess."
        $ ValueChange("Misty", 1, 0.37)
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Flannery":
        flannery angry "WHAT?! Can't you see I'm in the middle of an argument?! This is important!"
        $ classtype = ""
        menu:
            ">Study Fire-types":
                $ classtype = "Fire"

            ">Study Ground-types":
                $ classtype = "Ground"

            "Nevermind":
                flannery furious "Then stop wasting my time!"
                jump aftercharsangry

        narrator "Flannery deftly helps you study as she carries on a furious screaming match with the rest of the table.{nw}" 
        
        show flannery happy with dis
        
        extend " By the end of lunch, she seems quite content and cheerful."

        $ ValueChange("Flannery", 1, 0.63)
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Hilbert":
        hilbert sad "Ugh... I have better things to be doing with my time. Let's make this quick."
        $ classtype = ""
        menu:
            ">Study Ghost-types":
                $ classtype = "Ghost"

            ">Study Steel-types":
                $ classtype = "Steel"

            ">Study Ice-types":
                $ classtype = "Ice"

            "Nevermind":
                hilbert angry "Fine. But, frankly, you need the help."
                jump aftercharsangry

        narrator "Hilbert reluctantly helps you study as the argument rages around you, though you suspect he likes the opportunity to show off."
        $ ValueChange("Hilbert", 1, 0.88)
        $ IncreaseProficiency(classtype, 0.25)

    ">Just join the conversation":
        label tabletalkangry:
        narrator "You walk into the middle of a raucous argument."

        if (randnum < 0.2):
            flannery "It's a GODDAMN SOUP!"
            misty "Are you stupid?! It's a broth!"
            blue @closedbrow talking2mouth "Idiots! Why can't you get that it's a stew?"
            hilbert "It's an oatmeal. Why are we even having this discussion?"

            red uniform happy "Hey, guys! What're you talking about?"

            flannery furious "We're arguing about what cereal is, but THESE IDIOTS--"

        elif (randnum < 0.4):
            flannery "Arceus was the first Pokémon, and that's final!"
            misty "That's completely wrong! The DNA evidence says that Mew is the ancestor of every Pokémon!"
            blue "It's Bulbasaur! The first recorded Pokémon ever recorded in a Pokédex is Bulbasaur, and we don't have any proof that Arceus or Mew even exist!"
            hilbert "It's Rhydon."

            pause 2.0

            red uniform surprised "...Uh... Care to elaborate, Hilbert?"

            hilbert "No."

        elif (randnum < 0.6):
            flannery "If you can't acknowledge Professor Birch's advancements in Pokémon habitat research, I don't even know how to talk to you!"
            misty "Who cares about Pokémon habitat research? Professor Oak researches the Pokémon themselves! And he's done more in that field than anyone else!"
            hilbert "Professor Juniper's research into the origins of Pokémon covers Oak's field, and more. Two generations of Junipers have shown up anything Kanto could offer."
            blue "You better shut your mouth! Professor Oak's a good enough professor to cover both Kanto and Johto!"

            red uniform surprised "Uh... what about Professor Elm?"

            blue @surprisedbrow talking2mouth "What {i}about{/i} him?"

        elif (randnum < 0.8):
            flannery "Dexit was an awful idea! Can you even imagine how many trainers can't go to Galar now, just because the government arbitrarily said certain Pokémon can't enter the region?"
            misty "Do you know the first thing about invasive species?! If they didn't keep those species out, their own wildlife would be crowded out and driven to extinction!"
            hilbert "Then perhaps they simply aren't fit to exist in Galar in the first place."
            blue "Who cares about invasive species or whatever? I just wanna catch all of the Pokémon, not just some of them!"

            red uniform closedbrow talking2mouth "I heard some people are refusing to visit Galar over Dexit, actually..."

            misty "Well, screw them, then! I'll buy {i}two{/i} plane tickets!"

        else:
            flannery "Hoenn is obviously the best region for trainers! It's got dozens of different climates, all in a tiny area!"
            misty "Yeah, but seventy percent of those climates are different types of oceans. I like water, but that's too much."
            hilbert "Call me sheltered, but I don't like having to hack through a jungle or smash up rocks to get to places. Unova actually keeps its routes clear."
            blue "Oh, so you don't like actually {i}going on an adventure{/i}? Breaking down obstacles is what makes it worth it!"

            red uniform happy "None of us are actually trainers yet, though..."

            flannery furious "We WILL BE! And then you'll all see I'm right!"

        narrator "You tactfully keep quiet, and manage to avoid taking a side as the argument rages around you."

        $ ValueChange("Blue", 1, 0.12, False)
        $ ValueChange("Misty", 1, 0.37, False)
        $ ValueChange("Hilbert", 1, 0.62, False)
        $ ValueChange("Flannery", 1, 0.87)

return