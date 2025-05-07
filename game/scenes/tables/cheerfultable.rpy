label cheerfultable:

$ randnum = Random()

if (IsBefore(14, 4, 2004)):
    hide whitney
    hide gardenia
    hide bianca
    hide leaf
    show whitney happy uniform at farleftside with dis
    show gardenia happy uniform at midleftside with dis
    show bianca happy uniform at midrightside with dis
    show leaf happy uniform at farrightside with dis
else:
    hide whitney
    hide gardenia
    hide bianca
    hide leaf
    hide tia
    show bianca happy uniform: 
        xpos 1.0/6.0
    show leaf happy uniform:
        xpos 2.0/6.0
    show tia happy uniform:
        xpos 3.0/6.0
    show whitney happy uniform:
        xpos 4.0/6.0
    show gardenia happy uniform: 
        xpos 5.0/6.0
    with dis

label aftercharscheerful:

if (IsBefore(11, 4, 2004)):
    jump tabletalkcheerful

menu:
    ">Study with Whitney":
        whitney @talking2mouth "Sure, happy to help.{w=0.5}{nw}"
        extend @happy " I'm the {i}best{/i} study partner out there, after all!"
        $ classtype = ""
        menu:
            ">Study Normal-types":
                $ classtype = "Normal"

            ">Study Fairy-types":
                $ classtype = "Fairy"

            "Nevermind":
                whitney @sad "Aw, what? Boo... don't underestimate my study skills, [first_name]!"
                jump aftercharscheerful

        narrator "Whitney happily helps you studying, bragging about her prowess the whole time. It's {i}mostly{/i} warranted."

        if (calDate.day > 13 or calDate.month > 4):
            $ ValueChange("Whitney", 1, 4.0/6.0)
        else:
            $ ValueChange("Whitney", 1, 0.12)
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Gardenia":
        gardenia @surprised "Oh, you're asking me? I dunno, my grades aren't the best, to be honest..."
        $ classtype = ""
        menu:
            ">Study Grass-types":
                $ classtype = "Grass"

            ">Study Ghost-types":
                gardenia @sad "Ugh... I guess..."

                $ classtype = "Ghost"

            "Nevermind":
                gardenia @happy "Not gonna lie? Probably a good move."
                jump aftercharscheerful

        narrator "Gardenia struggles through some of the material with you before you switch roles entirely, teaching her. Still, you learned something."
        if (calDate.day > 13 or calDate.month > 4):
            $ ValueChange("Gardenia", 1, 5.0/6.0)
        else:
            $ ValueChange("Gardenia", 1, 0.37)
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Bianca":
        $ xposition = 1.0/6.0
        if (IsBefore(14, 4, 2004)):
            $ xposition = 0.63
        show bianca:
            xpos xposition
            ease 0.2 ypos 1.1
            ease 0.2 ypos 1.0
            repeat
        bianca @happy "Oh, sure! I help all kinds of people study, all the time!"
        $ classtype = ""
        menu:
            ">Study Normal-types":
                $ classtype = "Normal"

            ">Study Psychic-types":
                $ classtype = "Psychic"

            "Nevermind":
                show bianca:
                    xpos xposition
                    ypos 1.0
                bianca "Oh, okay. Maybe another time."
                jump aftercharscheerful

        show bianca:
            xpos xposition
            linear 0.1 ypos 1.1
            linear 0.1 ypos 1.0
            repeat
        narrator "Bianca's vibrating gets even faster as you study together, until you're concerned about the possibility of her achieving liftoff."
        if (not IsBefore(14, 4, 2004)):
            $ ValueChange("Bianca", 1, 1.0/6.0)
        else:     
            $ ValueChange("Bianca", 1, 0.63)
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Leaf":
        leaf @flirtbrow talking2mouth "Oh, you want a 'private lesson' with Professor Leaf? Then please, step into my office..." 
        $ classtype = ""
        menu:
            ">Study Grass-types":
                $ classtype = "Grass"

            ">Study Electric-types":
                $ classtype = "Electric"

            ">Study Dragon-types":
                $ classtype = "Dragon"

            "I'm going to report you to University Human Resources.":
                leaf @sad "What? No, don't do that! I'm so close to tenure!"
                jump aftercharscheerful

        narrator "Leaf helps you study, though she maintains the 'Professor Leaf' persona the entire time with frightening consistency."
        if (calDate.day > 13 or calDate.month > 4):
            $ ValueChange("Leaf", 1, 2.0/6.0)
        else:        
            $ ValueChange("Leaf", 1, 0.88)
        $ IncreaseProficiency(classtype, 0.25)
    
    ">Study with Tia (and Whitney)" if not IsBefore(14, 4, 2004):
        tia @happy "You're going to study with me? Yay! Thank you, [first_name]!"
        whitney @closedbrow talkingmouth "Girl, tone it down."

        $ classtype = ""
        menu:
            ">Study Psychic-types":
                $ classtype = "Psychic"

            ">Study Dragon-types":
                $ classtype = "Dragon"

            ">Study Johtonian Sign Language":
                $ classtype = "sign"

            "Nevermind":
                show whitney angry with dis
                tia sad "Dick."
                red @surprised "I feel like Tia didn't say that."
                whitney "Yeah, that was me. Don't get her hopes up like that!"
                show whitney frownmouth with dis
                jump aftercharscheerful

        if (classtype == "sign"):
            narrator "You study a few simple signs with Tia and Whitney, until you can carry on a very, {i}very{/i} basic silent conversation with the two of them."
            $ ValueChange("Tia", 3, 0.5, False)
            $ ValueChange("Whitney", 1, 2.0/3.0)
            narrator "Tia seems to really appreciate your efforts, and Whitney enjoys the opportunity to show off her knowledge."
        else:
            narrator "Let's not mince words--you help Tia study. You barely learn anything, though your knowledge of sign language improves somewhat."
            $ ValueChange("Tia", 1, 0.5, False)
            $ ValueChange("Whitney", 1, 2.0/3.0)
            $ IncreaseProficiency(classtype, 0.1)

    ">Just join the conversation":
        label tabletalkcheerful:
        narrator "You walk into the middle of a fervent discussion."

        $ convo = RandomChoice(range(9 if (calDate.day > 13 or calDate.month > 4) else 5))

        if (convo == 0):
            whitney @surprised "And the crazy thing is, I was just sitting there on the steps--"
            gardenia "Just outside your apartment, right?"
            bianca @surprised "Oh my gosh, I'm so in suspense! What happened next?"
            leaf @flirttalk "Wait, don't tell me. They were roommates?"

            red uniform @surprised "Oh my god, they were {i}roommates{/i}?"

            whitney @angry "Leaf! Don't spoil the story!"

        elif (convo == 1):
            gardenia "You girls look like you could use a bit of exercise! I could be your trainer, for a fee?~"
            leaf @sad "Ugh, no thanks. I work hard on this effortless-looking physique. Don't want to add muscles to it."
            whitney "You don't have to become some roided-out rage monster, Leaf! A bit of exercise just makes you feel better, even if you look exactly the same!"
            bianca "When I started working out, it was really hard! That's why I started rewarding myself with a tub of ice cream every time I finished!"

            red uniform @surprised "I'm in awe of your metabolism."

            gardenia "Well, for those of us who can't shove calories into the Distortion World, my offer's still available!"

        elif (convo == 2):
            whitney "Anyone planning to catch the baseball team's next game? I'll be playing."
            leaf @sad "Ew, no. When I get a boyfriend, I've only got one criteria for him--we're not watching, going to, or talking about sports. Ever."
            bianca "Oh, I love baseball! It's really big back home in Unova, but I heard that it's also popular in some of the other regions."
            gardenia "Sure, I'll watch you, Whitney! Any chance I can get some nice seats, as a friend of a player?"

            red uniform @happy "Ditto to that. Don't suppose you could split open the coupon book for a friend?"

            whitney "Fat chance! Your full-price tickets pay for our bats, you cheapskates!"

        elif (convo == 3):
            leaf @sad "Ugh. That last test was brutal."
            whitney @sad "I know! Flan punched a hole through her desk when she saw her score... scary..."
            gardenia @surprised "Uh... which test was this?"
            bianca "I didn't think it was that hard! I mean, I took a couple hits, but none of my Pokémon fainted, at least!"

            red uniform @closedbrow talking2mouth "You're really good at tests, huh, Bianca?"

            leaf "Dude, it's cause she stays up until three in the morning, studying..."

        elif (convo == 4):
            bianca "What's the cutest Pokémon? I think it's Munna! It's round and pink!"
            gardenia "Hm. Cute? Budew, I guess."
            leaf @surprised "Have none of you {i}seen{/i} a Jigglypuff before? C'mon, that's objective!"
            whitney "I used to think it was Miltank, but ever since I got a Cleffa, I've changed my mind!"

            $ starter_species_name = pokedexlookup(starter_id, DexMacros.Name)
            red uniform @closedbrow talking2mouth "I think [starter_species_name] is pretty cute."
            $ starter_contest_trait = pokedexlookup(starter_id, DexMacros.ContestTrait)
            if (starter_contest_trait == "Cute"):
                bianca @happy "Oh, you know what? You're right, that's a great choice!"

            else:
                bianca @surprised "Really? I'd say it's more... [starter_contest_trait]-looking."

        elif (convo == 5):
            bianca "Bianca's so cute! I'm so glad she joined our table!"
            leaf @closedbrow talkingmouth "Are you talking about her? Or about yourself, in third person?"
            whitney "Both would be true. This table's just fulla cuties."
            tia "Thanks, Bianca! You're really cute as well. And thanks for having me here!"
            gardenia @surprised "Gkkk. I think I'm developing diabetes. Cool it with the cuteness, girls."

            red uniform @happy "I don't mind. It's worth the price of insulin."

            leaf @sarcastic "{i}Nothing{/i}'s worth that. Not even staying alive."

        elif (convo == 6):
            leaf @happy "I gotta hear this one. How did you end up being short Bianca's interpreter?"
            whitney "Oh... you know. An ex."
            gardenia "Oh, gotcha. Man, I've got a Kalosian army knife of things I learned for exes."
            bianca "I'd like an ex someday! I've never had one."

            red uniform @closedbrow talking2mouth "I think you might want to start off with having a boyfriend, first?"

            tia @surprised "N-no! She can have an ex first. That's fine!"

        elif (convo == 7):
            bianca "Other-Bianca, you're so good at battling!"
            tia @surprised "Thank you! I'm trying {i}really{/i} hard."
            gardenia "Yeah, I saw a battle you had in Gym Class. Crazy skill you got there."
            whitney @closedbrow talkingmouth "Yeah, and you didn't even bring any Pokémon from home, right?"
            leaf @happy "Yes, it's like you speak your Pokémon's language! But you don't even say anything!"
            tia sad "Ah-ha... what? Speak their language? No, no, that's crazy!"

            red uniform @happy "Hey, people say the same thing about me. It's cool."

            tia @happy "Really? Well, if people say it about you, then it {i}must{/i} be cool!"

        elif (convo == 8):
            bianca "Hey, I see everyone brought their own food today! I've got a massive hot dog. I love them!"
            leaf @sarcastic "Yeah, I've got this, uh, sandwich, that Hilda made. I think it's watercress?"
            gardenia "Nice! Health food! I approve. I've got a protein shake. The secret ingredient is raw eggs."
            whitney "You don't get a towering stature like mine without a steady diet of meringues! What about you, brunette Bianca?"
            tia surprised "Um... breadcrumbs?"

            redmind uniform @thinking "She just hid it, but... that looked a lot like Pokémon food?"

            tia happy "Maybe next time we all bring food from home, I can cook for everyone!"

        narrator "You chat happily as lunch passes."

        if (IsBefore(14, 4, 2004)):
            $ ValueChange("Bianca", 1, 0.12, False)
            $ ValueChange("Gardenia", 1, 0.37, False)
            $ ValueChange("Whitney", 1, 0.62, False)
            $ ValueChange("Leaf", 1, 0.87)
        else:
            $ ValueChange("Bianca", 1, (1.0/6.0), False)
            $ ValueChange("Leaf", 1, (2.0/6.0), False)
            $ ValueChange("Tia", 1, (3.0/6.0), False)
            $ ValueChange("Whitney", 1, (4.0/6.0), False)
            $ ValueChange("Gardenia", 1, (5.0/6.0))

        if (IsBefore(14, 4, 2004)):
            show whitney happy uniform at farleftside with dis
            show gardenia happy uniform at midleftside with dis
            show bianca happy uniform at midrightside with dis
            show leaf happy uniform at farrightside with dis
        else:
            show bianca happy uniform: 
                xpos 1.0/6.0
            show leaf happy uniform:
                xpos 2.0/6.0
            show tia happy uniform:
                xpos 3.0/6.0
            show whitney happy uniform:
                xpos 4.0/6.0
            show gardenia happy uniform: 
                xpos 5.0/6.0
            with dis
return