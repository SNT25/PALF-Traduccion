label busytable:

python:
    randnum = Random()

    npcs = ["Nate", "Skyla", "Nessa", "Rosa"] 
    if (not IsBefore(20, 4, 2004)):
        npcs = ["Nate", "Skyla", "Nessa", "Sonia", "Rosa"] 
    if (IsDate(20, 4, 2004)):
        npcs = ["Nate", "Skyla", "Rosa"] 


    renpy.transition(dissolve)
    for i, npc in enumerate(npcs):
        renpy.hide(npc.lower())
        renpy.show(npc.lower() + " uniform", [Transform(xpos=((i + 1) / (len(npcs) + 1)))])

label aftercharsbusy:

if (IsBefore(11, 4, 2004)):
    jump tabletalkbusy

menu:
    ">Study with Nate" if "Nate" in npcs:
        $ firstinitial = first_name[0]
        nate happy "Studying with you? Talk about mission impossible! Nah, it's cool, [firstinitial], let's do it!"
        $ classtype = ""
        menu:
            ">Study Electric-types":
                $ classtype = "Electric"

            ">Study Steel-types":
                $ classtype = "Steel"

            ">Study Poison-types":
                $ classtype = "Poison"

            "Nevermind":
                nate @surprised "Oh, you're pulling out? Alright, let's check back in later, I guess."
                jump aftercharsbusy

        narrator "Nate cheerfully helps you study, until..."

        $ PlaySound("vibrate.ogg")

        nate @angrybrow frownmouth "Oh, it's my phone..."

        nate "Sorry, gotta take this! It's been real. It's been fun! Wouldn't say it's been {i}real fun{/i}, though."

        $ ValueChange("Nate", 1, 0.12)
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Skyla" if "Skyla" in npcs:
        skyla happy "Oh, sure! Helping people in need is my policy...{nw}"
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
                jump aftercharsbusy

        narrator "Skyla gleefully helps you go over a few concepts. You notice her voice and bearing get more and more dramatic with each successful impartment of knowledge, until she is all but posing like a superhero."
        skyla closedbrow happymouth "...And that should cover pretty much everything you need to know!"
        red happy "Thanks!"
        skyla happy "Just doing my duty!"
        $ ValueChange("Skyla", 1, 0.37)
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Nessa" if "Nessa" in npcs:
        nessa surprised "...Uh, weird, but sure? I mean, people don't really come to me for my brains, you know..."
        $ classtype = ""
        menu:
            ">Study Water-types":
                $ classtype = "Water"

            ">Study Rock-types":
                $ classtype = "Rock"

            "Nevermind":
                nessa -surprisedbrow -frownmouth -surprised @sad "Yeah, I figured."
                jump aftercharsbusy

        show nessa happy with dis

        narrator "Nessa calmly points out some of your weaker spots in the material and guides you towards ways to even them out. She seems impressed, both at you, and herself."

        $ ValueChange("Nessa", 1, 0.63)
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Sonia" if "Sonia" in npcs:
        sonia @happy "Sure, mate. I've taken these classes before, so I reckon I can give you a proper education."
        $ classtype = ""
        menu:
            ">Study Electric-types":
                $ classtype = "Electric"

            ">Study Fire-types":
                $ classtype = "Fire"

            "Nevermind":
                nessa @surprised "Oi. Don't be cheeky."
                jump aftercharsbusy

        narrator "Sonia starts out strong, guiding you in the material without issue. Her confidence quickly falters as time passes, though, and it seems clear she wishes she could pull out."

        $ ValueChange("Sonia", 1, 0.63)
        $ IncreaseProficiency(classtype, 0.25)

    ">Study with Rosa" if "Rosa" in npcs:
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
                jump aftercharsbusy

        narrator "Rosa spends the entire study session peeking around furtively, presumably looking for hidden cameras. As such, you actually {i}do{/i} end up helping her more than she helps you."
        $ ValueChange("Rosa", 1, 0.88)
        $ IncreaseProficiency(classtype, 0.25)

    ">Just join the conversation":
        label tabletalkbusy:
        narrator "You walk into the middle of a casual discussion."

        if (calDate.day == 20 and calDate.month == 4 and calDate.year == 2004):
            skyla @talkingmouth "Hey, did anyone catch why Nessa just ran off with that redhead?"
            rosa @talkingmouth "Don't know, but they were putting on a real show. I kinda expected Nessa to start swinging!"
            skyla @surprised "[first_name], you were up there with them. What were they saying?"

            red uniform @happy "Sorry, I don't think they'd want me sharing that."

            nate @happy "Yeah, keeping opsec is probably a good call here."

        elif (randnum < 0.2):
            nate @talkingmouth "And then I said, 'where are my pants?' And the crazy part, is he'd kept them for a whole year!"
            skyla @talkingmouth "Seriously? Why didn't he, like, just send them to you through the mail?"
            rosa @talkingmouth "I mean, it sounds like he just {i}stole{/i} your pants... on purpose. I've had that happen to me before..."
            nessa @talkingmouth "Yeah, I've had someone steal my {i}bathwater{/i} before. There're real weirdoes out there."

            red uniform @surprised "So, uh, how did he get the pants in the first place?"

            nate @happy "Well, that's a long story that can be summarized as 'the drinking age in Orre is 16!'"

        elif (randnum < 0.4):
            nessa @talkingmouth "So you're a pilot? That's pretty crazy. I didn't realize you could be a pilot at our age."
            nate @talkingmouth "Yeah, it's amazing what kinda jobs kids like us can fall into nowadays."
            skyla @talkingmouth "Well, it's not much harder than getting a driver's license. Becoming a pilot is easy, actually. The hard part is getting people to trust you."
            rosa @talkingmouth "Huh, I feel like I could get people to trust I know how to fly much more easily than I could {i}actually{/i} learn to fly..."
            
            red uniform @closedbrow talking2mouth "So, who's handling your flights in Unova now?"

            skyla @talkingmouth "Oh, still me! I mean, Unova's only like an hour away by plane. I just fly over on weekends."

        elif (randnum < 0.6):
            rosa @talkingmouth "I'm surprised I hadn't heard of you before, Nessa. We're in similar industries, and you're so gorgeous."
            nessa @talkingmouth "Thanks. But modeling is a much smaller field than acting. I'm just pebbles at the foot of your mountain."
            nate @talkingmouth "I'm not sure that's true. I could probably name way more models than I could actors."
            skyla @winkbrow talkingmouth "I think that may say more about you than it does about their fields."
            
            red uniform @closedbrow talking2mouth "I can probably name one actor, one pilot, and one model. And they're all at this table."

            rosa @talkingmouth "Oh, come on! {i}Everyone{/i} knows about Diantha! That makes at least two."

        elif (randnum < 0.8):
            skyla @talkingmouth "So what's it like being a model?"
            nessa @talkingmouth "Pretty much like being like you. Except I get paid to be hot, and you're doing it for free."
            nate @talkingmouth "Yeah, you should never do something for free if someone'll pay you for it! Everyone at this table should become a model."
            rosa @talkingmouth "I think that's against my contract, actually..."
            
            red uniform @closedbrow talking2mouth "Yeah, I'm pretty sure that no-one wants me to be a model."

            skyla @winkbrow talkingmouth "Take your shirt off, and I'll let you know."

        else:
            nessa @talkingmouth "Hey, Nate, how are you always so loaded?"
            nate @talkingmouth "Hah, what do you mean? I live off instant food and water, just like anyone else."
            skyla @talkingmouth "Sure, but you've got a super-fancy phone I've never seen before, and I've never seen you hesitate to buy {i}anything{/i}."
            rosa @talkingmouth "Also, you're constantly telling us that you're loaded. That's the main thing."
            
            red uniform @closedbrow talking2mouth "You don't strike me as a guy with a rich family..."

            nessa @talkingmouth "I'm just going to assume you sell Slowpoke Tails behind the bleachers and leave it at that."

        narrator "You chat happily as lunch passes."

        python:
            for i, npc in enumerate(npcs):
                ValueChange(npc, 1, ((i + 1) / (len(npcs) + 1)), i == len(npcs) - 1)

return