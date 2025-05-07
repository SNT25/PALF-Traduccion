label quiettable:

$ randnum = Random()

hide silver
hide erika
hide dawn
hide kris
show silver uniform at farleftside with dis
show erika uniform at midleftside with dis
show dawn uniform at midrightside with dis
show kris at farrightside with dis

label aftercharsquiet:

if (IsBefore(11, 4, 2004)):
    jump tabletalkquiet

menu:
    ">Study with Silver":
        silver @surprisedbrow talkingmouth "What? I didn't hear that right, right?"
        $ classtype = ""
        menu:
            ">Study Dark-types":
                $ classtype = "Dark"

            ">Study Poison-types":
                $ classtype = "Poison"

            "Nevermind":
                silver @talkingmouth "Ah, yeah, I must've misheard you."
                jump aftercharsquiet

        narrator "Silver seems baffled you're going to him for study help, but walks you through the material anyway. He's a surprisingly patient teacher."

        $ ValueChange("Silver", 1, 0.12)
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Erika":
        erika @happy "Certainly, I can help you study. What topics are you interested in? Botany? Historical figures?"
        erika @surprised "...Oh, Pokémon? Yes, that makes more sense, in hindsight."
        $ classtype = ""
        menu:
            ">Study Grass-types":
                $ classtype = "Grass"

            ">Study Poison-types":
                $ classtype = "Poison"

            "Nevermind":
                erika @talkingmouth "Very well. But feel free to come back another time."
                jump aftercharsquiet

        narrator "Erika masterfully educates you on the finer points of the material. You are thoroughly educated in a short amount of time."
        $ ValueChange("Erika", 1, 0.37)
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Dawn":
        dawn @talkingmouth "Oh... yeah, okay. I guess that's fine. I could use a study partner as well."
        $ classtype = ""
        menu:
            ">Study Ice-types":
                $ classtype = "Ice"

            ">Study Dragon-types":
                $ classtype = "Dragon"

            ">Study Fairy-types":
                $ classtype = "Fairy"

            "Nevermind":
                dawn @sad "{size=30}Oh no.{/size} What did I say?"
                jump aftercharsquiet

        narrator "Dawn studies with you dispassionately. However, her lack of excitement over the subject matter doesn't affect her mastery of it, which is significant."
        $ ValueChange("Dawn", 1, 0.63)
        $ IncreaseProficiency(classtype, 0.25)

    ">Ask Professor Cherry for Tutoring":
        kris @surprised "Oh? {w=0.5}{nw}"
        extend @happy "Well, sure! I always like to see my students take an active interest in their education." 

        $ classtype = RandomChoice(list(altclassdex.keys()), True)

        kris @closedbrow talking2mouth "Hm... My research recently has been mostly on [classtype] Pokémon. How about that?"
        menu:
            ">Be Tutored on [classtype]-types":
                pass

            "Nevermind":
                kris @happy "Alright! If you want tutoring on another type, just check in later."
                jump aftercharsquiet

        narrator "Professor Cherry delivers an impromptu lecture. You nod and take notes, diligently."
        $ ValueChange("Professor Cherry", 3, 0.88)
        $ classstats[classtype] += 1
        $ newtotal = FormatNum(classstats[classtype])
        narrator "Your [classtype] proficiency increased to [newtotal]!"

    ">Just join the conversation":
        label tabletalkquiet:
        narrator "You walk into the middle of Professor Cherry's awkward pleading to the rest of the table."

        if (randnum < 0.2):
            kris @talkingmouth "Come on, guys! Why don't we talk about fashion?"
            silver @talkingmouth "I don't even know where to begin."
            erika @talkingmouth "Well... kimonos are nice... and the only thing I wear, actually..."
            dawn @talkingmouth "Back home, I had to dress really warmly all the time. So it's nice that it's warm here."

            red uniform @happy "Heh. N{i}ice.{/i}"

            kris @happy "There we go! We're getting somewhere!"

        elif (randnum < 0.4):
            kris @talkingmouth "Come on, guys! Why don't we talk about Pokémon?"
            dawn @talkingmouth "{i}Sigh...{/i} I saw that coming."
            erika @talkingmouth "Grass-types are nice. They smell pleasant."
            silver @talkingmouth "Anyone who doesn't think Pokémon are the best things ever is a freak without a human heart."

            red uniform @closedbrow talking2mouth "Bit extreme there, Silver."

            kris @happy "There we go! We're getting somewhere!"

        elif (randnum < 0.6):
            kris @talkingmouth "Come on, guys! Why don't we talk about food?"
            erika @talkingmouth "A nice cup of tea is always pleasant in the morning."
            dawn @talkingmouth "Mm. Biscuits and cocoa for me. A warm cup of cocoa on a snowy day in Snowpoint City is the best."
            silver @talkingmouth "Coffee. Black."
            
            red uniform @closedbrow talking2mouth "My Mom thinks I've got an energy bar addiction. And, well, she's kinda right."

            kris @happy "There we go! We're getting somewhere!"

        elif (randnum < 0.8):
            kris @talkingmouth "Come on, guys! Why don't we talk about your futures?"
            silver @talkingmouth "What future?"
            erika @talkingmouth "I don't quite know. My parents haven't told me what it is to be, yet."
            dawn @talkingmouth "I guess I'll be a Pokémon Trainer. Like everyone else."

            red uniform @happy "I'm going to be a Champion!"

            kris @happy "There we go! We're getting somewhere!"

        else:
            kris @talkingmouth "Come on, guys! Why don't we talk about your friends?"
            silver "[ellipses]"
            erika "[ellipses]"
            dawn "[ellipses]"

            redmind uniform @surprised "Wait, they're all looking at me?"

            kris @happy "Well... maybe that one was a bust."

        narrator "You finish the rest of lunch in silence."

        $ ValueChange("Professor Cherry", 1, 0.12, False)
        $ ValueChange("Erika", 1, 0.37, False)
        $ ValueChange("Silver", 1, 0.62, False)
        $ ValueChange("Dawn", 1, 0.87)

return