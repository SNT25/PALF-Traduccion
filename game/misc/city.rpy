label city:

stop music fadeout 2.5

$ location = "city"

queue music "audio/music/Inspira_start.ogg" noloop
queue music "audio/music/Inspira_loop.ogg"

show city_B with Dissolve(2.0)

show screen currentdate
hide blackground
with dissolve

label citysetup:
$ trainer1 = Trainer("red", TrainerType.Ally, playerparty)
if (not trainer1.HasMons()):
    narrator "You quickly sprint back to campus, protecting your hurt and fainted Pokémon from further harm."
    $ location = "school"
else:
    menu:
        "{b}Track down Tia at her part-time job{/b}" if (GetRelationshipRank("Tia") == 1 and HasEvent("Tia", "Tia2Part1") and IsWeekday()):
            jump Tia2Part2

        "{b}Seek out the Tough Pokémon at the Seaport{/b}" if not seaportunlocked and not IsBefore(28, 4, 2004) and IsBefore(1, 5, 2004):
            call cramorantscene from _call_cramorantscene
            jump city

        "{b}Seek out Yellow and her Friend at the Café{/b}" if not sawwallyellow and not IsBefore(7, 5, 2004) and IsBefore(10, 5, 2004):
            call wallyellowscene from _call_wallyellowscene
            jump city

        "{b}Seek out Silver's Gang{/b}" if (not beatgrunts):
            show abandonedhouse
            show roughneck 
            with dis

            pause 1.0

            $ location = "alley"

            $ dialog = RandomChoice(
                ["What, a gamble battle? Hah! Punk, I've been gamble battling since before you were born!",
                "A gamble battle? Finally! No more instant ramen for me!",
                "Hey, you looked at me funny! Come on, I'll take you on!",
                "You. Me. A gamble battle. Ready?",
                "I'm in a real bad mood, and you look like the perfect person to take it out on, scrub!",
                "You don't have a chance in a gamble battle against me! My lucky numbers are hella auspicious today!"])
            roughneck "[dialog]"

            python:
                beatgrunts = True
                gruntmons = [pokedexlookupname("Stunky", DexMacros.Id), 
                    pokedexlookupname("Zubat", DexMacros.Id), 
                    pokedexlookupname("Scraggy", DexMacros.Id), 
                    pokedexlookupname("Skrelp", DexMacros.Id), 
                    pokedexlookupname("Rattata", DexMacros.Id), 
                    pokedexlookupname("Nidoran♂", DexMacros.Id), 
                    pokedexlookupname("Sandile", DexMacros.Id), 
                    pokedexlookupname("Nymble", DexMacros.Id)]
                numallies = 1
                numfoes = RandInt(1, 3)
                foenums = (1 if numfoes != 1 else RandInt(1, 3))
                allynums = max(foenums, numfoes)
                trainers = []
                numenemymons = 0
    
                trainers.append(Trainer("red", TrainerType.Player, playerparty, allynums))
                highestlevel = PlayerHighestLevel()

                for i in range(numfoes):
                    teamnumber = RandInt(1, 3)
                    numenemymons += teamnumber
                    newteam = []
                    for i in range(teamnumber):
                        newpokemon = Pokemon(RandomChoice(gruntmons), level = RandomChoice(range(AimLevel() - 3, AimLevel())))
                        newpokemon.ShinyValue = 1
                        newteam.append(newpokemon)
                    newtrainer = Trainer("roughneck", TrainerType.Enemy, newteam, foenums)
                    trainers.append(newtrainer)

            call Battle(trainers, customexpressions=["red", "red angrybrow happymouth"] + ["roughneck", "roughneck angry"] * numfoes, reanchor=[False] + [True] * numfoes) from _call_Battle_43
            if (_return):
                show roughneck angry with dis

                $ punkwins += 1

                $ totalwinnings = math.floor((1 + numfoes / 10.0) * (1 + numenemymons / 10.0) * 70 * highestlevel)
                $ money += totalwinnings
                narrator "You won $[totalwinnings]!"

                if (punkwins == 1):
                    narrator "{color=#0048ff}You discovered the alleyway!{/color} In the alleyway, you'll be able to find new Pokémon, and battle for as long as you want."
                    narrator "However, leaving will cause this period of free time to end."
            else:
                show roughneck happy with dis
                
                $ totallosses = math.floor(money / 10.0)
                $ money -= totallosses
                narrator "You lost $[totallosses]..."

            hide roughneck
            hide abandonedhouse
            with dis

            jump city

        "Visit Alleyway" if punkwins > 0:
            $ wildcount = 0
            call wildarea("alley") from _call_wildarea_3

        "Visit Seaport" if seaportunlocked or not IsBefore(1, 5, 2004):
            $ wildcount = 0
            call wildarea("seaport") from _call_wildarea_4

        "Buy Items":
            call screen shopkeep(shopitems)
            $ boughtitem = _return
            if (boughtitem == "Back"):
                jump city
            else:
                $ totalcost = boughtitem[0] * boughtitems
                if (totalcost > money):
                    narrator "You can't afford that!"
                else:
                    $ itemname = GetItemName(boughtitem[1])
                    $ money -= totalcost 
                    if (boughtitems > 1):
                        narrator "You bought [boughtitems] [itemname]s for $[totalcost]!"
                    else:
                        narrator "You bought a [itemname] for $[totalcost]!"
                    $ GetItem(itemname, boughtitems)
                    if (boughtitems >= 10 and ItemHasCategory(boughtitem[1], "Poké Balls")):
                        narrator "You also got a Premier Ball as an added bonus!"
                        $ GetItem("Premier Ball", 1)
                    $ boughtitems = 1

                jump citysetup

        "Heal Party":
            $ HealParty()
            jump citysetup

        "Access Janine's PC":
            $ currentbox = max(0, currentbox)
            show screen partymons
            call screen pokemonswap
            hide screen partymons
            jump citysetup

        "Head Back to Campus":
            narrator "Are you sure you want to head back to campus? Doing so will end this free time."

            menu:
                "Yes, I'm sure.":
                    $ location = "school"
                    pass

                "Never mind.":
                    jump citysetup
return

label nopikachu:
    if (pikachudenial == 0):
        red @angry "Boxing [pika_name] is the one thing I'll {i}never{/i} do."
        if (IsBefore(1, 5, 2004)):
            red @sad "It's bad enough I can't take my little buddy with me to gym class..."

    elif (pikachudenial == 1):
        red @angry "No means no. Get it? [pika_name] was there for me when I was alone."

    elif (pikachudenial == 2):
        red @angry "Boxing [pika_name] is the one thing I'll {i}never{/i} do."
        red @angry "He was there when I lost all my friends, and before I even had any."

    elif (pikachudenial == 3):
        red @angry "Boxing [pika_name] is the one thing I'll {i}never{/i} do."
        red @angry "He was there when my Mom and I had to skip meals."

    elif (pikachudenial == 4):
        red @angry "Boxing [pika_name] is the one thing I'll {i}never{/i} do."
        red @angry "He was there when I got in fights with the other kids for making fun of my mom."

    elif (pikachudenial == 5):
        red @angry "Boxing [pika_name] is the one thing I'll {i}never{/i} do."
        red @angry "He was there when I got my first human friend, Blue. And he was there when I lost him, too."
        
    elif (pikachudenial == 6):
        red @sad "...I feel sad for you. Haven't you ever had a friend that you never wanted to be parted from?"
        red @sad "Someone you'd move heaven and hell for? Someone you'd spit in the eye of god to keep by your side?"
        red @sad "[ellipses]"
        red @happy "I hope you do, someday. But [pika_name]'s staying. That's non-negotiable."

    else:
        red @talkingmouth "Nah."   

    $ pikachudenial += 1

    if (location == "city"):
        jump citysetup

    else:
        jump aftersetup

label cramorantscene:
    scene seaport with splitfade

    pause 1.0

    if (not seencramorant):
        red @closedbrow talking2mouth "Hm... looks like the seaport isn't super-busy right now. I don't see any signs of a Frenzied Pokémon around, either..."
        
        $ PlaySound("Pokemon/pikachu_norm1.ogg")

        pikachu neutral_2 "Pika?"

        red @talkingmouth "Right."

        red @happy "Well, whatever it is, it's got to be weak to you, buddy. There's plenty of Flying-types and Water-types around here, so you've probably got the advantage."

        if (pikachuobj in playerparty):
            $ playerparty.remove(pikachuobj)

        red @closedbrow talking2mouth "Of course, that Absol and Lopunny were both pretty far out of their territory. I guess there's no guarantee that whatever stole Tia's hat came from this area."

        red @confused "On the other hand, this is still a pretty industrial area. There's a power plant over there, and dumpsters all around. The sewers lead out here, too, I think."

        red @talking2mouth "And with all the ships around here, it could've been something even brought over from a different region..."

        if (GetRelationship("Bea") == "Planner"):
            red @happy "Ah, geez. I'm sounding like Bea, now, trying to figure out every possibility."

        red @talkingmouth "What do you think, buddy?"

    else:
        red @closedbrow talking2mouth "Okay. We need to make sure that Cramorant doesn't get the drop on us again. With your electric-type moves, it wouldn't stand a chance. Ready, buddy?"

        if (pikachuobj in playerparty):
            $ playerparty.remove(pikachuobj)

    $ seencramorant = True

    pause 1.0

    $ PlaySound("idea.ogg")

    red @confused "Buddy?"

    pause 1.0

    stop music

    $ renpy.music.queue("Audio/Music/RelicCastle_Start.ogg", channel='music', loop=None, tight=None)
    $ renpy.music.queue("Audio/Music/RelicCastle_Loop.ogg", channel='music', loop=True, tight=None)

    $ PlaySound("pokemon/cries/845.2.mp3")

    show cramorantthroatgoat:
        xpos 1.1 zoom 0.0 ypos 0.0 yanchor 1.0 xanchor 0.5
        ease 1.0 xpos 0.5 zoom 2.0 ypos 1.0
        ease 1.0 xpos 0.2 zoom 0.5 ypos 0.3
        easeout 1.0 xpos 0.5 zoom 1.0 ypos 0.4
        easein 1.0 zoom 3.0 ypos 1.2

    pause 3.0

    red @surprised "Buddy?! Get out of there!"

    $ PlaySound("Pokemon/pikachu_confused2.ogg")
    $ PlaySound("Pokemon/pikachu_scared.ogg")

    pikachu swallowed "Pika?! Pikapikapika!"

    red @sweat closedbrow talkingmouth "Right... I guess you're trying, huh?"

    redmind @sad "It looks like the wild Cramorant really wants to chow down on [pika_name]! [bluecolor]Even if I get the Cramorant to spit him back up, he'll probably just try to gobble him down again.{/color}"

    python:
        trainer1 = Trainer("red", TrainerType.Player, playerparty, number=3)

        cramorantobj = Pokemon("Cramorant", level=25, moves=[GetMove("Surf"), GetMove("Dive"), GetMove("Fly"), GetMove("Roost")], frenzynerf=(12, ["Stockpile", "Swallow", "Spit Up", "Water Gun"]), shinylock=False)
        cramorantobj.ApplyStatus("frenzied")
        cramorantobj.ApplyStatus("gorging")
        trainer2 = Trainer("sideportraitfull", TrainerType.Enemy, [cramorantobj], isPokemon=True)
        sidemonnum = 845.2

    hide cramorantthroatgoat with dis

    call Battle([trainer1, trainer2], healParty = False, specialmusic="Nothing") from _call_Battle_38
    $ battlehistory["Cramorant1"]  = _return

    $ AddPikachu()

    if (cramorantobj in (AllPokemon())):
        python:
            seaportunlocked = True
            cramorantobj.Level = 12
            cramorantobj.Moves = [GetMove("Stockpile"), GetMove("Swallow"), GetMove("Spit Up"), GetMove("Water Gun")]
            cramorantobj.Experience = cramorantobj.CalculateAllExperienceNeededForLevel(10)
            cramorantobj.ClearStatus("all", True)
            cramorantobj.RecalculateStats()

            pronoun = "him" if cramorantobj.GetGender() == Genders.Male else "her"
            pronoun2 = "he" if cramorantobj.GetGender() == Genders.Male else "she"

        red @happy "Yes! I caught [pronoun]."
        
        $ PlaySound("Pokemon/pikachu_angry1.ogg")

        pikachu angry "Pika."

        red @sadbrow happymouth "Oh, cheer up, buddy. I'm sure you'll warm up to [pronoun]." 
        if (cramorantobj in playerparty):
            red @happy "Look, [pronoun2]'s calmer already."
        elif (absolobj in (AllPokemon()) or lopunnyobj in (AllPokemon())):
            red @happy "I bet [pronoun2]'ll probably stop trying to eat you. These Frenzied Pokémon always calm down after a while."
        else:
            red @closedbrow talking2mouth "As long as [pronoun2] stops trying to eat you, anyway."

        $ PlaySound("Pokemon/pikachu_angry2.ogg")

        pikachu angry "Pika!"

        $ cramorantname = cramorantobj.GetNickname()

        red @closedbrow talking2mouth "I get the feeling that [pika_name] would rather not hang out around [cramorantname] any more than absolutely necessary..."   

        narrator "{color=#0048ff}You discovered the seaport!{/color} In the seaport, you'll be able to find new Pokémon, and battle for as long as you want."
        narrator "However, leaving will cause this period of free time to end."

    elif (WonBattle("Cramorant1")):
        $ seaportunlocked = True
        red @talkingmouth "Phew! That was tough. But that big, bad, bird won't be bothering anyone else anytime soon."

        red @happy "Well? How did it feel to be a missile?"

        $ PlaySound("Pokemon/pikachu_angry2.ogg")

        pikachu angry "Pika!"

        narrator "{color=#0048ff}You discovered the seaport!{/color} In the seaport, you'll be able to find new Pokémon, and battle for as long as you want."
        narrator "However, leaving will cause this period of free time to end."

    else:
        red @surprised "Crap! It's too strong! Retreat, [pika_name]!"

    $ PlaySound("Pokemon/pikachu_angry2.ogg")

    pikachu angry "Pika!"

    return

label wallyellowscene:
    $ sawwallyellow = True
    scene citycafe with splitfade

    show screen songsplash("Relic Song", "Zame")
    play music "audio/music/relicsong.ogg"

    pause 1.0

    narrator "You walk into an unfamiliar cafe. You actually remember this cafe from the impromptu restaurant tour that Leaf dragged you on a while ago, though you're looking forward to enjoying it at your own pace."
    narrator "In the corner, you see a familiar woman talking with someone slightly less-familiar, though still recognizable."

    show wally:
        xpos 0.33
    show yellow:
        xpos 0.66

    yellow @talkingmouth "...And how were your Quarter Qlash matches?"

    wally @sideeyes talkingmouth "Fine. I wasn't... it wasn't easy, though. I only barely scraped out a win on my third match."
    wally @sadeyes talkingmouth "I think I made a mistake coming here."

    pause 1.0

    yellow @talkingmouth "Why?"

    wally @surprised2eyes surprisedeyebrows surprisedmouth "Why?"
    wally @closedeyes angryeyebrows angrymouth "Because I only barely won!"

    yellow @happy "I didn't win, though. Does that mean I made a mistake coming here, Wally?"

    $ BecomeNamed("Wally")

    wally @sideeyes talkingmouth "N-no, of course not. But... you want to be a Pokémon nurse, right? You don't {i}need{/i} to be a strong battler."
    wally @talkingmouth "I do. If I'm going to... {w=0.5}{nw}"

    show yellow sadbrow frownmouth with dis

    extend @sideeyes talkingmouth "{i}cough.{/i}"

    pause 1.0

    wally @talkingmouth "Sorry. I meant I need to get stronger if I'm going to... to get what I want."

    pause 1.0

    yellow @sadbrow talkingmouth "It looks like your cough's getting worse."

    wally @sadbrow happymouth "It's just... a little bug going around. That time of year, you know?"

    yellow @angrybrow talkingmouth "It's May."

    show citycafe with vpunch

    wally @surprisedeyes talkingmouth "What about her?!"

    yellow -sadbrow -frownmouth @surprised "What?"

    wally @talkingmouth "What?"

    pause 1.0

    wally @closedeyes talkingmouth "Sorry. I thought you were saying something about May."

    yellow @talkingmouth "I don't know who that is. Is she in the nursing course?"

    wally @sideeyes talkingmouth "No, she wants to be a coordinator."

    yellow @talkingmouth "Oh."

    pause 1.0

    yellow @closedbrow talking2mouth "Actually... I think Leaf might have mentioned one of her old roommates was named May..."
    yellow @talkingmouth "Is May Brendan's girlfriend?"

    wally @talkingmouth "...Yes. Last I checked."
    wally @sideeyes talkingmouth "Actually, I dorm with those two. May, Brendan, and I were all friends back in Hoenn, but... as they became a couple, you know... there wasn't really room for me."

    wally @sideeyes talkingmouth "I hoped we could reconnect here in Kobukan, but it looks like they're still a thing. And their thing... {w=0.5}{nw}"

    show yellow sadbrow frownmouth with dis

    extend @sideeyes talkingmouth "{i}cough.{/i}"

    pause 1.0

    show yellow surprisedbrow frownmouth blush with dis

    wally @lightblush sadbrow talkingmouth "It gets loud at night, if you catch my drift."

    yellow @sadbrow talkingmouth "Oh... oh! I, ha, I see..."
    yellow @happy "My dorm also gets pretty loud, too..."

    wally @closedbrow talkingmouth "Ugh. I don't get why the Student Council decided to let men and women dorm together. I was perfectly happy with the old arrangement."

    yellow -surprisedbrow -frownmouth -blush @surprised "Oh-oh! I didn't mean it like that. I meant, um, Leaf snores really loudly, and Blue sneaks out of the dorm at midnight, and... um... well, I think it's better if I don't mention the noises I hear from Ethan's room..."

    wally @talkingmouth "...Gotcha. You dorm with [first_name], too, right? The one who gave that big speech in front of everyone? I've heard some weird stories about him."

    if (not mayhaslarvesta):
        wally @talkingmouth "It sounded like he did something that really pissed off Brendan. I don't know what that was, though..."

    yellow @talkingmouth "Yes. But he's really nice in-person. He even tolerates Blue."

    wally @happy "Hah! You've told me how hard {i}that{/i} is. Maybe I'd like to meet this guy."

    pause 1.0

    wally @sideeyes talkingmouth "Hey... he's not, like, a blabbermouth, is he? He won't tell anyone about me being here? I've been trying to stay pretty unnoticed so far."
    wally @closedbrow angrymouth "That thing with Lisia was too close. If someone back home saw me on TV, then..."

    yellow @sadbrow talkingmouth "I haven't had a whole lot of time to talk to him, but I don't think he's like that."

    wally @talkingmouth "Alright."

    pause 1.0

    show yellow sadbrow frownmouth with dis

    wally @closedbrow talkingmouth "{i}Cough.{/i}"

    pause 2.0

    wally @happy "Cheer up, Yellow."
    wally @talkingmouth "It was just all the excitement of the Quarter Qlashes. As soon as we go back to classes, I should be fine again."
    wally @sideeyes talkingmouth "...Maybe I should wear a mask."

    yellow @sadbrow talkingmouth "I wish I could heal you..."

    wally @sadeyebrows talkingmouth "It's not that bad. It's really just a cough." 
    wally @sadeyebrows happymouth "Every time I walk into the infirmary and see Grusha laid out on the table, or Jasmine shivering under her blankets, I gotta ask myself if I should even be there."

    yellow -sadbrow -frownmouth @closedbrow talkingmouth "Pain isn't a competition. The existence of others' hurt doesn't invalidate yours."

    show yellow happy with dis

    wally happy "Ha-{i}cough{/i}-ha! Which fortune cookie did you get {i}that one{/i} off of?"

    $ ValueChange("Wally", 3, 0.33)

    return

label cramorantscene2:
    pause 0.5

    $ PlaySound("pokemon/cries/845.mp3")
    $ sidemonnum = 845
    sidemon "Craw! Cram!"

    red @surprised "Hm? Wait, is that...?"

    libpikachu @angrybrow happymouth glowing "Pi-i-i-ka!"

    red @surprised "Looks like a Cramorant! They're pretty rare around here... this might be an important opportunity! Alright, [pika_name], let's go!"

    python:
        trainer1 = Trainer("red", TrainerType.Player, playerparty, number=3)
        cramorantobj = Pokemon("Cramorant", level=15)
        trainer2 = Trainer("sideportraitfull", TrainerType.Enemy, [cramorantobj], isPokemon=True)

    call Battle([trainer1, trainer2], healParty = False, specialmusic="Nothing") from _call_Battle_167
    $ RecordBattle("Cramorant1")
