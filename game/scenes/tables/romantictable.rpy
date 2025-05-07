label romantictable:

$ randnum = Random()

hide brendan
hide may
hide calem
hide serena
show brendan uniform at farleftside with dis
show may uniform at midleftside with dis
show calem uniform at midrightside with dis
show serena uniform at farrightside with dis

label aftercharsromantic:

if (IsBefore(11, 4, 2004)):
    jump tabletalkromantic

menu:
    ">Study with Brendan":
        brendan @surprised "[ellipses]"
        brendan @happy "Well, it's your funeral, bro!"

        $ classtype = ""
        menu:
            ">Study Grass-types":
                $ classtype = "Grass"

            ">Study Ground-types":
                $ classtype = "Ground"

            ">Study Water-types":
                $ classtype = "Water"

            "Nevermind":
                brendan @happy "Not even gonna lie, that's a good idea."
                jump aftercharsromantic

        narrator "The process of studying with Brendan can only be described as excruciating for all parties involved, and involves a lot more physical activity than one would expect." 
        narrator "By the end of it, you're both sweating and puffing like you've just finished a wrestling match."

        brendan happy "Bro, that was {i}intense{/i}! Let's do it again sometime!"

        red uniform @sad "Er... I'll get back to you on that."

        $ ValueChange("Brendan", 1, 0.12)
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with May":
        may @happy "Sure thing, [first_name]! I've been doing a little studying of the material on the side, so I think I can help you out a bunch."

        $ classtype = ""
        menu:
            ">Study Fire-types":
                $ classtype = "Fire"

            ">Study Bug-types":
                $ classtype = "Bug"

            ">Study Fighting-types":
                $ classtype = "Fighting"

            "Nevermind":
                may @talkingmouth "Sure thing. Just let me know."
                jump aftercharsromantic

        narrator "May helps you study, recalling an impressive amount of the material from memory."
        $ ValueChange("May", 1, 0.37)
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Calem":
        calem @talkingmouth "Certainly. What would you like to study?"
        $ classtype = ""
        menu:
            ">Study Flying-types":
                $ classtype = "Flying"

            ">Study Fighting-types":
                $ classtype = "Fighting"

            ">Study Fairy-types":
                $ classtype = "Fairy"

            "Nevermind":
                calem @sad "Very well. I was hoping for the distraction, actually, but..."
                jump aftercharsromantic

        narrator "Calem studies with you. He makes clear what your priorities in understanding the material should be, and you learn quickly because of it."
        $ ValueChange("Calem", 1, 0.63)
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Serena":
        serena @happy "Why, it would be a pleasure! In Kalos, I often thought I may become a teacher."

        if (GetRelationship("Serena") == "Conspirator"):
            redmind uniform @thinking "Okay, but what did you think you would become in Kanto?" 
        $ classtype = ""
        menu:
            ">Be Tutored on Fire-types":
                $ classtype = "Fire"

            ">Be Tutored on Dark-types":
                $ classtype  = "Dark"

            ">Be Tutored on Ground-types":
                $ classtype = "Ground"

            "Nevermind":
                serena @talkingmouth "That's fine. {i}À plus tard.{/i}"
                redmind uniform @surprisedeyebrows frownmouth "What did she call me?"
                jump aftercharsromantic

        narrator "Serena cheerfully guides you through the material, though you catch her yawning once or twice."
        $ ValueChange("Serena", 1, 0.88)
        $ IncreaseProficiency(classtype, 0.25)

    ">Just join the conversation":
        label tabletalkromantic:
        narrator "You walk into the middle of a fervent discussion."

        if (randnum < 0.2):
            may @talkingmouth "Do you remember where we met, Brendan?"
            brendan @talking2mouth "For sure. It was right in your bedroom. Your Mom told me to just walk in, so I did. And waited, for like, half an hour."
            calem @surprised "Wait... your mother told a strange boy to go into your empty bedroom? And just stay there? For half an hour?"
            serena @closedbrow talking2mouth "I heard that Hoenn has more of an open-door policy than Kalos, but I didn't expect that."

            red uniform @closedbrow talking2mouth "It's pretty similar in Kanto, too, actually. People just leave their doors open for each other."

            may @angry "Guys! Do you mind if I finish my cute story?"

        elif (randnum < 0.4):
            brendan @talking2mouth "Man, this food is pretty good. With nosh this delish, we don't even need to go out to fancy restaurants!"
            may @talkingmouth "Sure, but we will, won't we?"
            calem @talkingmouth "Kobukan's fancy restaurants are all pretty much Kalosian. I'm sure Serena could cook for you if you wanted some {i}actual{/i} delicious food."
            serena @talkingmouth "They're talking about setting up a date, Calem. I don't think they want me there for that."

            red uniform @closedbrow talking2mouth "Sure, but I think Calem was mostly trying to say your cooking is delicious."

            brendan @talking2mouth "What? What's everyone saying? I was just saying we could save some money!"
        elif (randnum < 0.6):
            calem @talkingmouth "Do you have any plans this weekend, Serena?"
            serena @surprised "Oh? No! No, no plans. Are you asking, then, if I...?"
            brendan @talking2mouth "Oh, are you setting up a date?"
            may @talkingmouth "There's this super-cute little wooded area in the garden that's perfect for a picnic!"

            red uniform @happy "I think you guys might be jumping to conclusions..."

            calem @talkingmouth "Yes, I was actually enquiring about Student Council business. And {i}nothing{/i} else."

        elif (randnum < 0.8):
            serena @talkingmouth "Calem, I think we need to have a meeting about Student Council matters."
            calem @talkingmouth "Certainly. Could we do this now?"
            serena @talkingmouth "There's not quite enough time. But I've made plans for this weekend."
            may @talkingmouth "Oh, I can recommend this {i}cute{/i} little spot just in the city! They've got the most delicious couples' milkshakes there!"

            red uniform @happy "I think you might be on the wrong track there, May."

            serena @talkingmouth "No, no, I'm interested. Please, continue."

        else:
            may @talkingmouth "We should totally double-date!"
            calem @talkingmouth "That sounds like a splendid idea, aside from the fact that Serena and I aren't dating."
            serena @talkingmouth "{size=30}We could fix that...{/size}"
            brendan @talking2mouth "Oh, geez, May, I'm not sure I want to bring someone else into our relationship yet, never mind two!"

            red uniform @closedbrow talking2mouth "That's not actually what double-dating means, Brendan."

            brendan @talking2mouth "Oh, phew. Er, no offense, you two."

        narrator "You chat happily as lunch passes."

        $ ValueChange("Brendan", 1, 0.12, False)
        $ ValueChange("May", 1, 0.37, False)
        $ ValueChange("Calem", 1, 0.62, False)
        $ ValueChange("Serena", 1, 0.87)

return