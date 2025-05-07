label newtable(tabletype):

python:
    randnum = Random()
    chars = list(set(GetTables()[tabletype]).intersection(GetStudents()))
    studychars = list(set(chars).intersection(WillStudy()))
    for i, character in enumerate(chars):
        xposition = 1.0 / (len(chars) + 1) * (i + 1) - 0.05
        renpy.show(GetCharacterSprite(character, uniform=True), [Transform(xpos=xposition + 0.05)])
    yellowcharacter = RandomChoice(GetYellowStudents(), True)

label newtablestart:

if (tabletype == "Melody's Table"):
    show melody on uniform with dis

menu:
    ">Sit at the table." if tabletype == "Melody's Table":
        if (not HasEvent("Melody", "SatAtTable1")):
            $ melody_name = first_name
            $ AddEvent("Melody", "SatAtTable1")

            narrator "You walk up to Melody's table, but no sooner had you swung a leg over the bench, then..."

            melody @talkingmouth "You can't sit here."

            pause 1.0

            red @confused "Excuse me?"

            melody @talkingmouth "You know what I said."

            pause 1.0

            red @angrybrow talking2mouth "Why {i}can't{/i} I sit here, Melody?"

            melody @bubblemouth ".{w=0.5}.{w=0.5}.{w=0.5}"
            melody @talking2mouth "Think of a reason."

            pause 0.5

            red @confused "What? You want me to... {i}think of a reason?{/i} A reason I'm not allowed to sit here?"

            melody @bubblemouth ".{w=0.5}.{w=0.5}.{w=0.5}"
            melody @talking2mouth "That's what I said."

            pause 0.5

            red @unamusedbrow talking2mouth "Surely you can't be serious."

            melody @talkingmouth "I am serious."
            melody @bubblemouth "[ellipses]"

            $ melody_name = "Shirley"

            melody @talking2mouth "And don't call me, Shirley."

            if (first_name == "Shirley"):
                red @closedbrow talking2mouth "Fine. Whatever. I won't call you."#haha very funny

            else:
                red @talking2mouth "...I wasn't."
                
                melody @talkingmouth "Guess you didn't hear the comma."
                melody @talking2mouth "'Don't call me, Shirley.' You're Shirley. And I'm telling you not to call me."

                pause 1.0

                melody @talkingmouth "Or talk to me. Or look at me. Or even really think about me."

                $ oldfirst_name = first_name
                $ first_name = "Shirley"

                red @talking2mouth "My name's not Shirley."

                melody @talkingmouth "Sure."

                pause 1.0

                melody @talkingmouth "Are you done, Shirley?"

                pause 0.5

                red @upeyes angryeyebrows talking2mouth "...For now."

                $ first_name = oldfirst_name

        else:
            narrator "Melody ignores you. Eventually, you leave the table of your own accord, in search of more hospitable pastures."

        hide melody with dis

    "{b}>Study the Psychic-type{/b}" if tabletype == "Remedial Table":
        rosa @angrybrow happymouth "We've got this, guys! Instructor Will will be so impressed when he comes back!"

        bianca @happy "I've got snacks, so we can keep our energy up while studying!"

        rosa @surprisedbrow talkingmouth "We're... in the cafeteria?"

        pause 0.5

        if (GetRelationshipRank("Rosa") > 0):
            rosa @happy "Hey there, fanboy! Study with us!"

            red uniform @closedbrow talking2mouth "You're not worried a manager's hiding under the table, ready to swat you for helping a classmate?"

            rosa @surprised "{w=0.5}.{w=0.5}.{w=0.5}."

            rosa @angry "Well, I wasn't until now!"

        else:
            rosa @talkingmouth "Hi, [first_name]. Want to do some Psychic-type studying?"

            red uniform @talkingmouth "Sure enough."

        $ IncreaseProficiency("Psychic", 1)
        
        python:
            for i, char in enumerate(chars):
                renpy.transition(dis)
                renpy.show(GetCharacterSprite(char, 10, uniform=True), [Transform(xpos=(chars.index(char) + 1) / (len(chars) + 1))])
                ValueChange(char, 1, ((chars.index(char) + 1) / (len(chars) + 1)), i == len(chars) - 1)

        narrator "Bonds increased!"

    ">Study with Cheren" if "Cheren" in chars:
        if ("Cheren" not in studychars):
            narrator "Cheren does not seem willing to study with you right now."

            jump newtablestart

        cheren sad2eyes noshine @sadmouth "[first_name]. How can I help you?"
        $ classtype = ""
        menu:
            ">Study Dark-types":
                $ classtype = "Dark"

            ">Study Normal-types":
                $ classtype = "Normal"

            "Nevermind":
                cheren @sadmouth "Very well. Let me know if you change your mind."
                jump newtablestart

        narrator "You study together, tensely. Though neither of you say a word against the other, the air is thick enough to cut with a knife. You come away understanding the material more, but each other less."
        $ ValueChange("Cheren", -1, ((chars.index("Cheren") + 1) / (len(chars) + 1)))
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Silver" if "Silver" in chars:
        if ("Silver" not in studychars):
            narrator "Silver does not seem willing to study with you right now."

            jump newtablestart

        silver @surprisedbrow talkingmouth "What? I didn't hear that right, right?"
        $ classtype = ""
        menu:
            ">Study Dark-types":
                $ classtype = "Dark"

            ">Study Poison-types":
                $ classtype = "Poison"

            "Nevermind":
                silver @talkingmouth "Ah, yeah, I must've misheard you."
                jump newtablestart

        narrator "Silver seems baffled you're going to him for study help, but walks you through the material anyway. He's a surprisingly patient teacher."

        $ ValueChange("Silver", 1, ((chars.index("Silver") + 1) / (len(chars) + 1)))
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Gardenia" if "Gardenia" in chars:
        if ("Gardenia" not in studychars):
            narrator "Gardenia does not seem willing to study with you right now."

            jump newtablestart
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
                jump newtablestart

        narrator "Gardenia struggles through some of the material with you before you switch roles entirely, teaching her. Still, you learned something."
        $ ValueChange("Gardenia", 1, ((chars.index("Gardenia") + 1) / (len(chars) + 1)))
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Skyla" if "Skyla" in chars:
        if ("Skyla" not in studychars):
            narrator "Skyla does not seem willing to study with you right now."

            jump newtablestart
        skyla @happy "Oh, sure! Helping people in need is my policy...{nw}"
        extend @winkbrow smirkmouth " And you look like you're {i}seriously{/i} in need."
        $ classtype = ""
        menu:
            ">Study Flying-types":
                $ classtype = "Flying"

            ">Study Bug-types":
                $ classtype = "Bug"

            "Nevermind":
                skyla @surprised "Er... wait, wait! That was a joke!"
                skyla @sad "You're not offended, are you...?"
                jump newtablestart

        narrator "Skyla gleefully helps you go over a few concepts. You notice her voice and bearing get more and more dramatic with each successful impartment of knowledge, until she is all but posing like a superhero."
        skyla @closedbrow happymouth "...And that should cover pretty much everything you need to know!"
        red uniform @happy "Thanks!"
        skyla @happy "Just doing my duty!"
        $ ValueChange("Skyla", 1, ((chars.index("Skyla") + 1) / (len(chars) + 1)))
        $ IncreaseProficiency(classtype, 0.25)



    ">Study with Leaf" if "Leaf" in chars:
        if ("Leaf" not in studychars):
            narrator "Leaf does not seem willing to study with you right now."

            jump newtablestart
        leaf @flirtbrow talking2mouth "Oh, you want a 'private lesson' with Professor Leaf? Then please, step into my office..." 
        $ classtype = ""
        menu:
            ">Study Grass-types":
                $ classtype = "Grass"

            ">Study Electric-types":
                $ classtype = "Electric"

            ">Study Dragon-types" if (not HasEvent("Leaf", "ClassSwap")):
                $ classtype = "Dragon"
            
            ">Study Normal-types" if (HasEvent("Leaf", "ClassSwap")):
                $ classtype = "Normal"

            "I'm going to report you to University Human Resources.":
                leaf @sad "What? No, don't do that! I'm so close to tenure!"
                jump newtablestart

        narrator "Leaf helps you study, though she maintains the 'Professor Leaf' persona the entire time with frightening consistency."
        $ ValueChange("Leaf", 1, ((chars.index("Leaf") + 1) / (len(chars) + 1)))
        $ IncreaseProficiency(classtype, 0.25)
    
    ">Study with Blue" if "Blue" in chars:
        if ("Blue" not in studychars):
            narrator "Blue does not seem willing to study with you right now."

            jump newtablestart
        blue @happy "Help you study?! Hah! You must be really desperate! But sure, I might be the only person who can actually teach you anything!"
        $ classtype = ""
        menu:
            ">Study Flying-types":
                $ classtype = "Flying"

            ">Study Dragon-types":
                $ classtype = "Dragon"

            "Nevermind":
                blue @angry "Oh, piss off."
                jump newtablestart

        narrator "[blue_name] crows obnoxiously the entire time you're studying together, but you do manage to learn a few new concepts. [blue_name] clearly enjoys the opportunity to lord this over you."
        $ ValueChange("Blue", 1, ((chars.index("Blue") + 1) / (len(chars) + 1)))
        $ IncreaseProficiency(classtype, 0.25)
    
    ">Talk with Yellow about [yellowcharacter]" if "Yellow" in chars:
        python:
            yellowcharacterpronoun = "he" if persondex[yellowcharacter]["Sex"] == Genders.Male else "she"
            yellowcharacterpronoun2 = "him" if persondex[yellowcharacter]["Sex"] == Genders.Male else "her"

        yellow @happy "Hiya! I've been talking to [yellowcharacter] recently. Would you like to hear what [yellowcharacterpronoun] said?"
       
        menu:
            ">Talk about [yellowcharacter]":
                pass

            "Nevermind":
                yellow @sadbrow talking2mouth "Alright. Maybe later...?"
                jump newtablestart

        show yellow happy with dis

        if (yellowcharacter != "Cheren"):
            narrator "You learn some new information about [yellowcharacter]. You feel like you understand [yellowcharacterpronoun2] better now."
        else:
            narrator "Everything Yellow tells you about Cheren just contradicts what you thought you knew about him..."

        $ ValueChange(yellowcharacter, 7, -0.5, changemood=False)

    ">Study with Ethan" if "Ethan" in chars:
        ethan @confusedeyebrows talking2mouth "Hm? Dude, you know that I, like, can't really teach you anything you don't already know, right? We take the exact same classes."
        red @happy "Hey, I just wanted to hang out."
        ethan @closedbrow talkingmouth "Ah, you're too nice, you know that?"
        $ classtype = ""
        $ rank1 = GetStatRank(0)
        $ rank2 = GetStatRank(1)
        $ rank3 = GetStatRank(2)
        menu:
            ">Study [rank1]-types":
                $ classtype = rank1

            ">Study [rank2]-types":
                $ classtype = rank2

            ">Study [rank3]-types":
                $ classtype = rank3

            "Nevermind":
                ethan @talking2mouth "Seeya 'round."
                jump newtablestart

        show ethan happy with dis

        narrator "Ethan, true to his word, can't teach you anything new, but you still manage to get in some helpful review together."
        $ ValueChange("Ethan", 1, ((chars.index("Ethan") + 1) / (len(chars) + 1)))
        $ IncreaseProficiency(classtype, 0.25)



    ">Study with Rosa" if "Rosa" in chars:
        if ("Rosa" not in studychars):
            narrator "Rosa does not seem willing to study with you right now."

            jump newtablestart
        rosa @sadbrow talkingmouth sweat "Oh, um... I think I'm not allowed to give any of my peers any advice... about anything, actually... so if anyone asks, you were helping {i}me{/i} study!"
        $ classtype = ""
        menu:
            ">Study Electric-types":
                $ classtype = "Electric"

            ">Study Psychic-types":
                $ classtype = "Psychic"

            ">Study Bug-types":
                $ classtype = "Bug"

            "Nevermind":
                rosa @happy sweat "Yeah, it's probably best not to risk it!"
                jump newtablestart

        narrator "Rosa spends the entire study session peeking around furtively, presumably looking for hidden cameras. As such, you actually {i}do{/i} end up helping her more than she helps you."
        $ ValueChange("Rosa", 1, ((chars.index("Rosa") + 1) / (len(chars) + 1)))
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Nessa" if "Nessa" in chars:
        if ("Nessa" not in studychars):
            narrator "Nessa does not seem willing to study with you right now."

            jump newtablestart
        nessa @surprised "...Uh, weird, but sure? I mean, people don't really come to me for my brains, you know..."
        $ classtype = ""
        menu:
            ">Study Water-types":
                $ classtype = "Water"

            ">Study Rock-types":
                $ classtype = "Rock"

            "Nevermind":
                nessa @sad "Yeah, I figured."
                jump newtablestart

        show nessa happy with dis

        narrator "Nessa calmly points out some of your weaker spots in the material and guides you towards ways to even them out. She seems impressed, both at you, and herself."

        $ ValueChange("Nessa", 1, ((chars.index("Nessa") + 1) / (len(chars) + 1)))
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Raihan" if "Raihan" in chars:
        if ("Raihan" not in studychars):
            narrator "Raihan does not seem willing to study with you right now."

            jump newtablestart
        raihan @happy "Hey, [last_name]! Ready to study at the altar of the Great Raihan?"
        raihan @talkingmouth "I promise you, I didn't get my Gym Leader position by being pretty. I can really teach you something."

        $ classtype = ""
        menu:
            ">Study Dragon-types":
                $ classtype = "Dragon"

            ">Study Rock-types":
                $ classtype = "Rock"

            "Nevermind":
                raihan @talking2mouth "...Aight."
                jump newtablestart

        show raihan happy with dis

        narrator "Raihan expertly guides your understanding of the material. Though he's undeniably a blowhard, he's clearly {i}extremely{/i} knowledgeable in his chosen fields."

        $ ValueChange("Raihan", 1, ((chars.index("Raihan") + 1) / (len(chars) + 1)))
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Sonia" if "Sonia" in chars:
        if ("Sonia" not in studychars):
            narrator "Sonia does not seem willing to study with you right now."

            jump newtablestart
        sonia @happy "Sure, mate. I've taken these classes before, so I reckon I can give you a proper education."
        $ classtype = ""
        menu:
            ">Study Electric-types":
                $ classtype = "Electric"

            ">Study Fire-types":
                $ classtype = "Fire"

            "Nevermind":
                nessa @surprised "Oi. Don't be cheeky."
                jump newtablestart

        show sonia sadbrow with dis

        narrator "Sonia starts out strong, guiding you in the material without issue. Her confidence quickly falters as time passes, though, and it seems clear she wishes she could pull out."

        $ ValueChange("Sonia", 1, ((chars.index("Sonia") + 1) / (len(chars) + 1)))
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Sabrina" if "Sabrina" in chars:
        if ("Sabrina" not in studychars):
            narrator "Sabrina does not seem willing to study with you right now."

            jump newtablestart
        sabrina @talking2mouth "Fine."
        $ classtype = ""
        menu:
            ">Study Psychic-types":
                $ classtype = "Psychic"

            ">Study Ghost-types":
                $ classtype = "Ghost"

            "Nevermind":
                sabrina @sad "I saw this coming..."
                jump newtablestart

        narrator "Sabrina quietly helps you study. Not a word is spoken, but your thoughts go back and forth as you compare notes."

        show sabrina happymouth with dis

        $ ValueChange("Sabrina", 1, ((chars.index("Sabrina") + 1) / (len(chars) + 1)))
        $ IncreaseProficiency(classtype, 0.25)
    
    ">Study with Nate" if "Nate" in chars:
        if ("Nate" not in studychars):
            narrator "Nate does not seem willing to study with you right now."

            jump newtablestart
        nate @happy "Studying with you? Talk about mission impossible! Nah, it's cool, [nate_name], let's do it!"
        $ classtype = ""
        menu:
            ">Study Dark-types" if (HasEvent("Nate", "ClassSwap")):
                $ classtype = "Dark"

            ">Study Electric-types" if (not HasEvent("Nate", "ClassSwap")):
                $ classtype = "Electric"

            ">Study Steel-types":
                $ classtype = "Steel"

            ">Study Poison-types":
                $ classtype = "Poison"

            "Nevermind":
                nate @surprised "Oh, you're pulling out? Alright, let's check back in later, I guess."
                jump newtablestart

        narrator "Nate cheerfully helps you study, until..."

        $ PlaySound("vibrate.ogg")

        nate @angrybrow frownmouth "Oh, it's my phone..."

        nate @happy "Sorry, gotta take this! It's been real. It's been fun! Wouldn't say it's been {i}real fun{/i}, though."

        $ ValueChange("Nate", 1, ((chars.index("Nate") + 1) / (len(chars) + 1)))
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Hilbert" if "Hilbert" in chars:
        if ("Hilbert" not in studychars):
            narrator "Hilbert does not seem willing to study with you right now."

            jump newtablestart
        hilbert @sadbrow talkingmouth "Ugh... I have better things to be doing with my time. Let's make this quick."
        $ classtype = ""
        menu:
            ">Study Ghost-types":
                $ classtype = "Ghost"

            ">Study Steel-types":
                $ classtype = "Steel"

            ">Study Ice-types":
                $ classtype = "Ice"

            "Nevermind":
                hilbert @angry "Fine. But, frankly, you need the help."
                jump newtablestart

        narrator "Hilbert reluctantly helps you study, though you suspect he likes the opportunity to show off."
        $ ValueChange("Hilbert", 1, ((chars.index("Hilbert") + 1) / (len(chars) + 1)))
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Hilda" if "Hilda" in chars:
        if ("Hilda" not in studychars):
            narrator "Hilda does not seem willing to study with you right now."

            jump newtablestart
        
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
                jump newtablestart

        narrator "Hilda patiently guides you through some of the tougher material, but her energy is clearly flagging towards the end, so you call it early."
        hilda sad "Goddamn, I need a nap... hope that helped."
        $ ValueChange("Hilda", 1, ((chars.index("Hilda") + 1) / (len(chars) + 1)))
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Bea" if "Bea" in chars:
        if ("Bea" not in studychars):
            narrator "Bea does not seem willing to study with you right now."

            jump newtablestart
        bea @talkingmouth "Training the mind is a worthy endeavor. Let us commence."
        $ classtype = ""
        menu:
            ">Study Fighting-types":
                $ classtype = "Fighting"

            ">Study Rock-types":
                $ classtype = "Rock"

            "Nevermind":
                bea @angrybrow talkingmouth "Dishonor!"
                jump newtablestart

        narrator "Bea's studying style is no-nonsense and relentless. By the end, you feel as exhausted from studying as you would had you just run a 5k."
        red uniform @sadeyebrows sadeyebrows talking2mouth "Please... no more..."
        bea @happy "This is acceptable, for now."
        $ ValueChange("Bea", 1, ((chars.index("Bea") + 1) / (len(chars) + 1)))
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Bianca" if "Bianca" in chars:
        if ("Bianca" not in studychars):
            narrator "Bianca does not seem willing to study with you right now."

            jump newtablestart
        $ xposition = ((chars.index("Bianca") + 1) / (len(chars) + 1))
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
                bianca @talking2mouth "Oh, okay. Maybe another time."
                jump newtablestart

        show bianca happy:
            xpos xposition
            linear 0.1 ypos 1.1
            linear 0.1 ypos 1.0
            repeat
        narrator "Bianca's vibrating gets even faster as you study together, until you're concerned about the possibility of her achieving liftoff."
        $ ValueChange("Bianca", 1, xposition)
        $ IncreaseProficiency(classtype, 0.25)


    
    ">Study with Calem" if "Calem" in chars:
        if ("Calem" not in studychars):
            narrator "Calem does not seem willing to study with you right now."

            jump newtablestart
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
                jump newtablestart

        narrator "Calem studies with you. He makes clear what your priorities in understanding the material should be, and you learn quickly because of it."
        $ ValueChange("Calem", 1, ((chars.index("Calem") + 1) / (len(chars) + 1)))
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Serena" if "Serena" in chars:
        if ("Serena" not in studychars):
            narrator "Serena does not seem willing to study with you right now."

            jump newtablestart
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
                redmind uniform @confusedeyes frownmouth "What did she call me?"
                jump newtablestart

        narrator "Serena cheerfully guides you through the material, though you catch her yawning once or twice."
        $ ValueChange("Serena", 1, ((chars.index("Serena") + 1) / (len(chars) + 1)))
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Wally" if "Wally" in chars:
        if ("Wally" not in studychars):
            narrator "Wally does not seem willing to study with you right now."

            jump newtablestart
        wally @sadbrow talkingmouth "M-me? Oh... Um, sure. Thanks, [first_name]."

        $ classtype = ""
        menu:
            ">Study Fairy-types":
                $ classtype = "Fairy"

            ">Study Fighting-types":
                $ classtype = "Fighting"

            "Nevermind":
                wally @surprised "Oh. Okay. {size=30}Did I...?{/size}" 
                wally @sadbrow talkingmouth "{i}Cough.{/i}"
                jump newtablestart

        narrator "Wally helps you study, though he seems tense. He's knowledgeable--moreso than you in some ways--but often second-guesses himself."
        $ ValueChange("Wally", 1, ((chars.index("Wally") + 1) / (len(chars) + 1)))
        $ IncreaseProficiency(classtype, 0.25)
    
    ">Study with May" if "May" in chars:
        if ("May" not in studychars):
            narrator "May does not seem willing to study with you right now."

            jump newtablestart
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
                jump newtablestart

        narrator "May helps you study, recalling an impressive amount of the material from memory."
        $ ValueChange("May", 1, ((chars.index("May") + 1) / (len(chars) + 1)))
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Brendan" if "Brendan" in chars:
        if ("Brendan" not in studychars):
            narrator "Brendan does not seem willing to study with you right now."

            jump newtablestart
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
                jump newtablestart

        narrator "The process of studying with Brendan can only be described as excruciating for all parties involved, and involves a lot more physical activity than one would expect." 
        narrator "By the end of it, you're both sweating and puffing like you've just finished a wrestling match."

        brendan happy "Bro, that was {i}intense{/i}! Let's do it again sometime!"

        red uniform @sad "Er... I'll get back to you on that."

        $ ValueChange("Brendan", 1, ((chars.index("Brendan") + 1) / (len(chars) + 1)))
        $ IncreaseProficiency(classtype, 0.25)


    ">Ask Professor Cherry for Tutoring" if "Professor Cherry" in chars:
        kris @surprised "Oh? {w=0.5}{nw}"
        extend @happy "Well, sure! I always like to see my students take an active interest in their education." 

        $ classtype = RandomChoice(list(altclassdex.keys()), True)

        kris @closedbrow talking2mouth "Hm... My research recently has been mostly on [classtype] Pokémon. How about that?"
        menu:
            ">Be Tutored on [classtype]-types":
                pass

            "Nevermind":
                kris @happy "Alright! If you want tutoring on another type, just check in later."
                jump newtablestart

        narrator "Professor Cherry delivers an impromptu lecture. You nod and take notes, diligently."
        $ ValueChange("Professor Cherry", 3, ((chars.index("Professor Cherry") + 1) / (len(chars) + 1)))
        $ classstats[classtype] += 1
        $ newtotal = FormatNum(classstats[classtype])
        narrator "Your [classtype] proficiency increased to [newtotal]!"

    ">Study with Misty" if "Misty" in chars:
        if ("Misty" not in studychars):
            narrator "Misty does not seem willing to study with you right now."

            jump newtablestart
        misty @surprised "Huh? Me, help you study? I mean, I guess..."
        $ classtype = ""
        menu:
            ">Study Water-types":
                $ classtype = "Water"

            ">Study Ice-types":
                $ classtype = "Ice"

            "Nevermind":
                misty @angry "What's your problem?! Just jerking me around, huh?"
                jump newtablestart

        narrator "Misty loses her temper while teaching a few concepts, but manages to calm herself down enough to be a helpful study partner, culminating in a sheepish..."
        misty @closedbrow talking2mouth "Thanks, I guess."
        $ ValueChange("Misty", 1, ((chars.index("Misty") + 1) / (len(chars) + 1)))
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Klara" if "Klara" in chars:
        klara @happy "Oh my gosh, yes! I'd {i}love{/i} to help you study!"
        $ classtype = ""
        menu:
            ">Study Water-types":
                $ classtype = "Water"

            ">Study Bug-types":
                $ classtype = "Bug"

            "Nevermind":
                klara @puppybrow talking2mouth "Oh, no... I mean, that's fine, I guess... if you want to just go back on what you said, I don't mind..."
                jump newtablestart

        if (classtype == "Water"):
            narrator "Klara does her best to teach you the material, but even you're able to tell she barely understands it herself. You do not make much progress, despite Klara's assertions she {i}loves{/i} Water-types."
            $ ValueChange("Klara", 10, ((chars.index("Klara") + 1) / (len(chars) + 1)))
            $ IncreaseProficiency(classtype, 0.1)

        else:
            narrator "Klara proves surprisingly knowledgeable about Bug-types, actually teaching you far more, far more quickly, than you would normally be able to gain. She claims she's only 'passingly interested' in Bug-types, though."
            $ ValueChange("Klara", 10, ((chars.index("Klara") + 1) / (len(chars) + 1)))
            $ IncreaseProficiency(classtype, 0.5)

    ">Study with Dawn" if "Dawn" in chars:
        if ("Dawn" not in studychars):
            narrator "Dawn does not seem willing to study with you right now."

            jump newtablestart
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
                jump newtablestart

        narrator "Dawn studies with you dispassionately. However, her lack of excitement over the subject matter doesn't affect her mastery of it, which is significant."
        $ ValueChange("Dawn", 1, ((chars.index("Dawn") + 1) / (len(chars) + 1)))
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Erika" if "Erika" in chars:
        if ("Erika" not in studychars):
            narrator "Erika does not seem willing to study with you right now."

            jump newtablestart
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
                jump newtablestart

        narrator "Erika masterfully educates you on the finer points of the material. You are thoroughly educated in a short amount of time."
        $ ValueChange("Erika", 1, ((chars.index("Erika") + 1) / (len(chars) + 1)))
        $ IncreaseProficiency(classtype, 0.25)



    ">Study with Flannery" if "Flannery" in chars:
        if ("Flannery" not in studychars):
            narrator "Flannery does not seem willing to study with you right now."

            jump newtablestart
        flannery @tiredbrow talking2mouth "What? I've only got, like, half an hour until noon..."
        $ classtype = ""
        menu:
            ">Study Fire-types":
                $ classtype = "Fire"

            ">Study Ground-types":
                $ classtype = "Ground"

            "Nevermind":
                flannery @closedbrow talkingmouth "Ugh. Not in the mood, dude."
                jump newtablestart

        narrator "Flannery deftly helps you study as her mood improves.{nw}" 
        
        show flannery happy with dis
        
        extend " She seems to appreciate you taking the time to work through the last of the morning fog."

        $ ValueChange("Flannery", 1, ((chars.index("Flannery") + 1) / (len(chars) + 1)))
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Whitney" if "Whitney" in chars:
        if ("Whitney" not in studychars):
            narrator "Whitney does not seem willing to study with you right now."

            jump newtablestart
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
                jump newtablestart

        narrator "Whitney happily helps you studying, bragging about her prowess the whole time. It's {i}mostly{/i} warranted."

        if (calDate.day > 13 or calDate.month > 4):
            $ ValueChange("Whitney", 1, ((chars.index("Whitney") + 1) / (len(chars) + 1)))
        else:
            $ ValueChange("Whitney", 1, ((chars.index("Whitney") + 1) / (len(chars) + 1)))
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Tia (and Whitney)" if "Tia" in chars and "Whitney" in chars:
        if ("Tia" not in studychars):
            narrator "Tia does not seem willing to study with you right now."

            jump newtablestart
        if ("Whitney" not in studychars):
            narrator "Whitney does not seem willing to study with you right now."

            jump newtablestart
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
                tia sadbrow frownmouth "Dick."
                red @surprised "I feel like Tia didn't say that."
                whitney "Yeah, that was me. Don't get her hopes up like that!"
                show whitney frownmouth with dis
                jump newtablestart

        if (classtype == "sign"):
            narrator "You study a few simple signs with Tia and Whitney, until you can carry on a very, {i}very{/i} basic silent conversation with the two of them."
            $ ValueChange("Tia", 3, ((chars.index("Tia") + 1) / (len(chars) + 1)), False)
            $ ValueChange("Whitney", 1, ((chars.index("Whitney") + 1) / (len(chars) + 1)))
            narrator "Tia seems to really appreciate your efforts, and Whitney enjoys the opportunity to show off her knowledge."
        else:
            narrator "Let's not mince words--you help Tia study. You barely learn anything, though your knowledge of sign language improves somewhat."
            $ ValueChange("Tia", 1, ((chars.index("Tia") + 1) / (len(chars) + 1)), False)
            $ ValueChange("Whitney", 1, ((chars.index("Whitney") + 1) / (len(chars) + 1)))
            $ IncreaseProficiency(classtype, 0.1)

    ">Study with Tia" if "Tia" in chars and "Whitney" not in chars:
        if ("Tia" not in studychars):
            narrator "Tia does not seem willing to study with you right now."

            jump newtablestart
        if (GetRelationshipRank("Tia") > 0):
            tia @happy "You're going to study with me? Yay! Thank you, [first_name]!"

            $ classtype = ""
            menu:
                ">Study Psychic-types":
                    $ classtype = "Psychic"

                ">Study Dragon-types":
                    $ classtype = "Dragon"

                ">Study Johtonian Sign Language":
                    $ classtype = "sign"

                "Nevermind":
                    tia @sad "Oh... okay..."
                    jump newtablestart

            if (classtype == "sign"):
                narrator "You study a few simple signs with Tia, until you can carry on a very, {i}very{/i} basic silent conversation with her."
                $ ValueChange("Tia", 3, ((chars.index("Tia") + 1) / (len(chars) + 1)), False)
                narrator "Tia seems to really appreciate your efforts, and you can tell your proficiency is increasing."
            else:
                narrator "Let's not mince words--you help Tia study. You barely learn anything, though your knowledge of sign language improves somewhat."
                $ ValueChange("Tia", 1, ((chars.index("Tia") + 1) / (len(chars) + 1)), False)
                $ IncreaseProficiency(classtype, 0.1)
        
        else:
            narrator "You attempt to strike up a conversation, but without a translator, you simply can't communicate..."
            
            jump newtablestart

    ">Study with Jasmine" if "Jasmine" in chars:
        if ("Jasmine" not in studychars):
            narrator "Jasmine does not seem willing to study with you right now."

            jump newtablestart
        jasmine @happy "Well, of course! While I have the energy, I'd love to help."
        $ classtype = ""
        menu:
            ">Study Steel-types":
                $ classtype = "Steel"

            ">Study Ground-types":
                $ classtype = "Ground"

            "Nevermind":
                jasmine @talkingmouth "That's alright. You don't need to justify calling something off to me."
                jump newtablestart

        narrator "Jasmine helps you with the material with steely determination. By the end of lunch, however, her forehead is beaded with sweat, and she faintly excuses herself."
        $ ValueChange("Jasmine", 2, ((chars.index("Jasmine") + 1) / (len(chars) + 1)))
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Grusha" if "Grusha" in chars:
        if ("Grusha" not in studychars):
            narrator "Grusha does not seem willing to study with you right now."

            jump newtablestart
        grusha @happy "Yeah, alright. If you're cool with it, we can study."
        $ classtype = ""
        menu:
            ">Study Ice-types":
                $ classtype = "Ice"

            ">Study Flying-types":
                $ classtype = "Flying"

            "Nevermind":
                grusha @confusedeyebrows talkingmouth "Got something better to do?"
                jump newtablestart

        narrator "Grusha helps you with the material with a cold and unreadable expression. By the end of lunch, his jaw is tightly clenched, and he abruptly leaves the table without saying goodbye."
        $ ValueChange("Grusha", 2, ((chars.index("Grusha") + 1) / (len(chars) + 1)))
        $ IncreaseProficiency(classtype, 0.25)


    ">Just join the conversation" if (not tabletype == "Melody's Table"):
        narrator "You chat with the people at the table as lunch passes."
        if ("Yellow" in studychars):
            narrator "Yellow talks about [yellowcharacter], and you learn a little more about your classmates."

        if (randnum < 0.01):
            narrator "You might even say that lunch passes uneventfully."

        python:
            for i, char in enumerate(chars):
                renpy.transition(dis)
                renpy.show(GetCharacterSprite(char, 10, uniform=True), [Transform(xpos=(chars.index(char) + 1) / (len(chars) + 1))])
                valuechange = 2
                if (char != "Yellow"):
                    if (char in ["Jasmine", "Grusha"]):
                        valuechange *= 2
                    ValueChange(char, valuechange, ((chars.index(char) + 1) / (len(chars) + 1)), i == len(chars) - 1)
                else:
                    ValueChange(yellowcharacter, 4, ((chars.index("Yellow") + 1) / (len(chars) + 1)), i == len(chars) - 1, changemood=False)

return