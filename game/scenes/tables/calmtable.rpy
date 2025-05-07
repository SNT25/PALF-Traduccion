label calmtable:

python:
    randnum = Random()

    npcs = GetCharsInTable("Calm Table")

    renpy.transition(dissolve)
    for i, npc in enumerate(npcs):
        renpy.hide(npc.lower())
        renpy.show(npc.lower() + " uniform", [Transform(xpos=((i + 1) / (len(npcs) + 1)))])

label aftercharscalm:

if (IsBefore(11, 4, 2004)):
    jump tabletalkcalm

menu:
    ">Study with Sabrina" if "Sabrina" in npcs:
        sabrina @talking2mouth "Fine."
        $ classtype = ""
        menu:
            ">Study Psychic-types":
                $ classtype = "Psychic"

            ">Study Ghost-types":
                $ classtype = "Ghost"

            "Nevermind":
                sabrina @sad "I saw this coming..."
                jump aftercharscalm

        narrator "Sabrina quietly helps you study. Not a word is spoken, but your thoughts go back and forth as you compare notes."

        show sabrina happymouth with dis

        $ ValueChange("Sabrina", 1, ((npcs.index("Sabrina") + 1) / (len(npcs) + 1)))
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Bea" if "Bea" in npcs:
        bea @talkingmouth "Training the mind is a worthy endeavor. Let us commence."
        $ classtype = ""
        menu:
            ">Study Fighting-types":
                $ classtype = "Fighting"

            ">Study Rock-types":
                $ classtype = "Rock"

            "Nevermind":
                bea @angrybrow talkingmouth "Dishonor!"
                jump aftercharscalm

        narrator "Bea's studying style is no-nonsense and relentless. By the end, you feel as exhausted from studying as you would had you just run a 5k."
        red uniform @sadeyebrows sadeyebrows talking2mouth "Please... no more..."
        bea @happy "This is acceptable, for now."
        $ ValueChange("Bea", 1, ((npcs.index("Bea") + 1) / (len(npcs) + 1)))
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Hilda" if "Hilda" in npcs:
        hilda @talkingmouth "Sure, I've got some time. I can probably help you with Poison, Steel, and Rock-type Pokémon. Which are you looking for some help with?"
        $ classtype = ""
        menu:
            ">Study Poison-types":
                $ classtype = "Poison"

            ">Study Steel-types":
                $ classtype = "Steel"

            ">Study Rock-types":
                $ classtype = "Rock"

            "Nevermind":
                hilda @happy "Oh, you're cancelling? Great. Actually, there are a couple other things I should be doing right now..."
                jump aftercharscalm

        narrator "Hilda patiently guides you through some of the tougher material, but her energy is clearly flagging towards the end, so you call it early."
        hilda sad "Goddamn, I need a nap... hope that helped."
        $ ValueChange("Hilda", 1, ((npcs.index("Hilda") + 1) / (len(npcs) + 1)))
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Cheren" if "Cheren" in npcs:
        cheren @happy "Oh, of course! The Student Council's ears are always open to help students!{w=0.5}{nw}" 
        extend @sad " ...Even if I'm not in the Student Council yet."
        $ classtype = ""
        menu:
            ">Study Dark-types":
                $ classtype = "Dark"

            ">Study Normal-types":
                $ classtype = "Normal"

            "Nevermind":
                cheren @sadmouth "Very well. Let me know if you change your mind."
                jump aftercharscalm

        narrator "Cheren does his best to teach you the material, but you end up helping him far more. You sense he might not be very good at the 'Pokémon' part of 'Pokémon Arts and Sciences'."
        $ ValueChange("Cheren", 1, ((npcs.index("Cheren") + 1) / (len(npcs) + 1)))
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Jasmine" if "Jasmine" in npcs:
        jasmine @happy "Well, of course! While I have the energy, I'd love to help."
        $ classtype = ""
        menu:
            ">Study Steel-types":
                $ classtype = "Steel"

            ">Study Ground-types":
                $ classtype = "Ground"

            "Nevermind":
                jasmine @talkingmouth "That's alright. You don't need to justify calling something off to me."
                jump aftercharscalm

        narrator "Jasmine helps you with the material with steely determination. By the end of lunch, however, her forehead is beaded with sweat, and she faintly excuses herself."
        $ ValueChange("Jasmine", 2, ((npcs.index("Jasmine") + 1) / (len(npcs) + 1)))
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Grusha" if "Grusha" in npcs:
        grusha @happy "Yeah, alright. If you're cool with it, we can study."
        $ classtype = ""
        menu:
            ">Study Ice-types":
                $ classtype = "Ice"

            ">Study Flying-types":
                $ classtype = "Flying"

            "Nevermind":
                grusha @talkingmouth "Got something better to do?"
                jump aftercharscalm

        narrator "Grusha helps you with the material with a cold and unreadable expression. By the end of lunch, his jaw is tightly clenched, and he abruptly leaves the table without saying goodbye."
        $ ValueChange("Grusha", 2, ((npcs.index("Grusha") + 1) / (len(npcs) + 1)))
        $ IncreaseProficiency(classtype, 0.25)

    ">Just join the conversation":
        label tabletalkcalm:
        narrator "You walk into the middle of a quiet discussion."

        if ("Cheren" in npcs):
            if (randnum < 0.2):
                cheren @sadmouth "Might I ask you to join me in my attempts to move a certain Student Council initiative through the administration?"
                hilda @talkingmouth "I'd like to help, but what the hell can we do about it?"
                bea @talkingmouth "I will defeat the administration in single combat and demand their surrender as a token of victory."
                sabrina @talking2mouth "Cheren appreciates your 'ride-or-die attitude,' but he'd actually prefer we just send emails to the administration."

                red uniform @closedbrow talking2mouth "I dunno, I like Bea's idea more."

                cheren @sadmouth "Truthfully, so do I. But we run against the issue of 'legality' with that plan."

            elif (randnum < 0.4):
                bea @talkingmouth "I would ask one of you to act as my sparring partner tomorrow."
                hilda @talkingmouth "Shit no. I remember what happened last time I agreed to that. My ass {i}still{/i} hurts."
                sabrina @talking2mouth "I am not a suitable opponent for your specialty."
                cheren @sadmouth "Er... I suppose that leaves me, then, but, er..."

                red uniform @closedbrow talking2mouth "You're afraid of being folded like an old napkin?"

                bea @talkingmouth "Do not worry. I do not fold old napkins. I rip them apart and throw them away."

            elif (randnum < 0.6):
                hilda @talkingmouth "I can't tell you how much I appreciate getting away from Hilbert, even for one lunch."
                cheren @sadmouth "Is he giving you trouble? If he's harrassing you, you can report him to the Student Council."
                bea @talkingmouth "It seems more as though Hilda is the one harrassing him. He's the one hiding from you most of the time."
                sabrina @talking2mouth "Yes. If you were to just leave him alone, you would never see him again."

                red uniform @closedbrow talking2mouth "Sure, but just 'cause you can't see a problem doesn't mean it doesn't exist."

                hilda @talkingmouth "This guy gets it."

            elif (randnum < 0.8):
                sabrina "[ellipses]"
                cheren @sadmouth "What's on your mind?"
                bea @talkingmouth "That was a poor choice of words."
                hilda @talkingmouth "Yeah, kinda an 'open mouth; insert foot' moment."
                
                red uniform @closedbrow talking2mouth "But since it's been asked, might as well answer it. Sabrina?"

                sabrina @talking2mouth "...Everything, everywhere, all at once."

            else:
                hilda @talkingmouth "Hey, do you guys need help with anything? I've got some time off from Hilbert."
                bea @talkingmouth "You spend your time off of doing something for a person doing more things for other people?"
                sabrina @talking2mouth "I truly wish I could somehow put the concept of selfishness into your mind."
                cheren @sadmouth "Er... I was going to ask if you would help with some Student Council business, but now I feel rather..."
                
                red uniform @closedbrow talking2mouth "Hm... I mean, this is a great opportunity. I can't think of how I could take advantage of it, though."

                hilda @talkingmouth "Then I guess I'll help you figure out what I can help you out with."

        else:
            if (IsDate(26, 4, 2004)):
                grusha @talkingmouth "Hey, you two."

                hilda @talkingmouth "Grush. How the hell are you? Hilbert not being too much of a pain in your ice classes?"

                grusha @closedbrow talking2mouth "He's fine."

                bea @talkingmouth "You look flushed and upright today, Jasmine. I suppose it's a good day, then."

                jasmine @happy "Oh, it's always a good day when I meet someone new. I finally met [first_name], and that was such a pleasure."

                red uniform @happy "Hey, the pleasure's mine."

                if (GetRelationship("Sabrina") == "Friend"):
                    pause 1.0

                    redmind @thinking "Sabrina's... still in the infirmary, I guess..."

            elif (randnum < 0.2):
                sabrina @sadmouth "I appreciate that you are willing to let me sit here with you, even with your reservations."
                if ("Grusha" in npcs):
                    grusha @closedbrow "{w=0.5}.{w=0.5}.{w=0.5}."
                hilda @talkingmouth "I mean, I'm not even sure I believe that you can read minds, so you can sit anywhere you want. I won't fight you."
                bea @talkingmouth "I {i}will{/i} fight you. But because I want to get stronger, not because I dislike your course of action."

                if ("Jasmine" in npcs):
                    jasmine @happy sweat "Everyone has their struggles. I wouldn't want you to ever feel unwelcome."
               
                
                red uniform @closedbrow talking2mouth "Hey, you can sit wherever you want, Sabrina. We know you can't help the mind-reading."

                sabrina @happymouth "Mm. ...[first_name], Bea wants a bite of your food."
                bea surprised "Wh- Sabrina!"

            elif (randnum < 0.4):
                bea @talkingmouth "I would ask one of you to act as my sparring partner tomorrow."
                if ("Grusha" in npcs):
                    grusha @closedbrow talking2mouth "No thanks. Sounds like a pain."
                hilda @talkingmouth "Shit no. I remember what happened last time I agreed to that. My ass {i}still{/i} hurts."
                sabrina @talking2mouth "I am not a suitable opponent for your specialty."

                if ("Jasmine" in npcs):
                    jasmine @happy sweat "I think I would quite literally die."

                red uniform @closedbrow talking2mouth "I'm afraid of being folded like an old napkin."

                bea @talkingmouth "Do not worry. I do not fold old napkins. I rip them apart and throw them away."

            elif (randnum < 0.6):
                hilda @talkingmouth "I can't tell you how much I appreciate getting away from Hilbert, even for one lunch."
                bea @talkingmouth "It seems more as though Hilbert wants to get away from you. He's the one hiding from you most of the time."
                if ("Grusha" in npcs):
                    grusha @closedbrow talking2mouth "I'd listen to the guy."
                sabrina @talking2mouth "Yes. If you were to just leave him alone, you would never see him again."

                red uniform @closedbrow talking2mouth "Sure, but just 'cause you can't see a problem doesn't mean it doesn't exist."

                hilda @talkingmouth "This guy gets it."

                if ("Jasmine" in npcs):
                    jasmine @talkingmouth sweat "I believe your efforts in regard to Hilbert are admirable, Hilda. Him making helping him difficult is all the more reason to try."

            elif (randnum < 0.8):
                sabrina "[ellipses]"
                red @happy "What's on your mind?"
                if ("Grusha" in npcs):
                    grusha "Wow."

                bea @talkingmouth "That was a poor choice of words."
                hilda @talkingmouth "Yeah, kinda an 'open mouth; insert foot' moment."
                if ("Jasmine" in npcs):
                    jasmine @talkingmouth "Everyone misspeaks once in a while. Let's not harp on it."

                red uniform @closedbrow talking2mouth "But since it's been asked, might as well answer it. Sabrina?"

                sabrina @talking2mouth "...Everything, everywhere, all at once."

            else:
                hilda @talkingmouth "Hey, do you guys need help with anything? I've got some time off from Hilbert."
                bea @talkingmouth "You spend your time off of doing something for a person doing more things for other people?"
                sabrina @talking2mouth "I truly wish I could somehow put the concept of selfishness into your mind."

                if ("Grusha" in npcs):
                    grusha @closedbrow talking2mouth "You should take a break. Go snowboarding, or something."
                
                red uniform @closedbrow talking2mouth "Hm... I mean, this is a great opportunity. I can't think of how I could take advantage of it, though."

                if ("Jasmine" in npcs):
                    jasmine @happy sweat "Is taking advantage of it really necessary?"

                hilda @talkingmouth "Then I guess I'll help you figure out what I can help you out with."

        narrator "You talk seriously as lunch passes."

        python:
            for i, npc in enumerate(npcs):
                ValueChange(npc, (1 if npc not in ["Jasmine", "Grusha"] else 2), ((i + 1) / (len(npcs) + 1)), i == len(npcs) - 1)

return