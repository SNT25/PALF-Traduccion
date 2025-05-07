init python:
    import functools

    def CurrentPersondex():
        if (playercharacter == None):
            return persondex
        else:
            return oldpersondex

    def AssignCurrentInventory(newval):
        if (playercharacter == None):
            global inventory
            inventory = newval
        else:
            global oldinventory
            oldinventory = newval

    def CurrentInventory():#returns either inventory or oldinventory
        if (playercharacter == None):
            return inventory
        else:
            return oldinventory

    def SecureShareAndEggAmount():
        changemade = False
        luckyeggcount = 0
        for mon in AllPokemon():
            if (mon.Item == Item.LuckyEgg):
                luckyeggcount += 1
        luckyeggcount += GetItemCount(Item.LuckyEgg)
        if (luckyeggcount > 1):
            changemade = True
            for mon in AllPokemon():
                if (mon.Item == Item.LuckyEgg):
                    mon.Item = None
            CurrentInventory()[Item.LuckyEgg] = 1

        experiencesharecount = 0
        for mon in AllPokemon():
            if (mon.Item == Item.ExperienceShare):
                experiencesharecount += 1
        experiencesharecount += GetItemCount(Item.ExperienceShare)
        if (experiencesharecount > 1):
            changemade = True
            for mon in AllPokemon():
                if (mon.Item == Item.ExperienceShare):
                    mon.Item = None
            CurrentInventory()[Item.ExperienceShare] = 1

        mysterygiftcount = 0
        for mon in AllPokemon():
            if (mon.Item == Item.MysteryGift):
                mysterygiftcount += 1
        mysterygiftcount += GetItemCount(Item.MysteryGift)
        if (mysterygiftcount > 1):
            for mon in AllPokemon():
                if (mon.Item == Item.MysteryGift):
                    mon.Item = None
            CurrentInventory()[Item.MysteryGift] = 1
        
        return changemade

    def SetRandSeed(staySame = False, extraseed = ""):
        global randcount
        if (IsAfter(5, 4, 2004)):
            random.seed(timeOfDay + str(randseedtime) + str(calDate.day) + str(calDate.month) + str(calDate.year) + ("" if staySame else str(randcount)) + str(extraseed))
            if (not staySame):
                randcount += 1

    def RandomUniform(min, max):
        SetRandSeed()
        return random.uniform(min, max)

    def Random(staySame = False, extraseed = ""):
        SetRandSeed(staySame, extraseed)
        return random.random()

    def RandomChoice(options, staySame = False, extraseed=""):
        SetRandSeed(staySame, extraseed)
        return random.choice(options)

    def WeightedRandomChoice(weighted_list):
        finallist = []

        for weight, item in weighted_list:
            finallist.append((weight, item))

        SetRandSeed()
        # Unpack the weighted list into two separate lists
        weights, objects = zip(*finallist)

        # Use random.choices to select a random object based on weights
        selected_object = random.choices(objects, weights=weights)[0]

        return selected_object
    
    def RandomChoices(options, k):
        SetRandSeed()
        return random.choices(options, k=k)

    def RandInt(min, max, staySame = False):
        SetRandSeed(staySame)
        return random.randint(math.floor(min), math.ceil(max))

    def BecomeNamed(name):
        if name in persondex.keys():
            persondex[name]["Named"] = True
        else:
            renpy.say(None, "{color=#f00}Character [name] not found for naming. Please report this error. ErrorData: [calDate], [timeOfDay]")
    
    def BecomeContacted(name):
        if name not in persondex.keys():
            renpy.say(None, "{color=#f00}Character [name] not found for contacting. Please report this error. ErrorData: [calDate], [timeOfDay]")
            return

        renpy.music.set_volume(0.0, delay=0.0, channel="music")
        renpy.sound.play("Audio/PhoneNumber.ogg")

        if name in persondex:
            persondex[name]["Contact"] = True
        else:
            persondex[name] = copy.deepcopy(defaultpersondex[name])
            persondex[name]["Contact"] = True

        renpy.music.set_volume(1.0, delay=1.5, channel="music")
        if (name != "Sabrina"):
            renpy.say("", "{{color=#e70000}}{{cps=0}}¡Has recibido el número de {}!{{/cps}}{{w=2.0}}{{/color}}".format(name))
        else:
            renpy.say("", "{{color=#e70000}}{{cps=0}}¡Sabrina ha establecido un vínculo psíquico contigo!{{/cps}}{{w=2.0}}{{/color}}".format(name))
        renpy.pause(2.0, hard=True)

    def darken_hex_color(hex_color, factor=0.7):
        """
        Darkens a hex color by a given factor.
        
        Parameters:
        hex_color (str): The color in hex format, e.g., '#RRGGBB' or '#RGB'.
        factor (float): The factor by which to darken the color. 
                        Should be between 0 and 1. Default is 0.7.
                        
        Returns:
        str: Darkened hex color in '#RRGGBB' format.
        """
        # Ensure the hex string starts with '#'
        hex_color = hex_color.lstrip('#')

        # If shorthand format is provided (#RGB), convert it to long format (#RRGGBB)
        if len(hex_color) == 3:
            hex_color = ''.join([ch * 2 for ch in hex_color])

        # Convert hex to RGB
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)

        # Apply darkening factor to each channel
        r = int(r * factor)
        g = int(g * factor)
        b = int(b * factor)

        # Ensure the values are within 0-255
        r = max(0, min(255, r))
        g = max(0, min(255, g))
        b = max(0, min(255, b))

        # Convert back to hex and format with leading zeros if necessary
        darkened_hex = f'#{r:02x}{g:02x}{b:02x}'

        return darkened_hex

    def AnimateValueChange(value, position, changemood=True, differentmood=0, specialcolor=None, pausing=True):
        if (isinstance(position, tuple)):
            xpos, ypos = position
        else:
            xpos = position
            ypos = 0.33

        if (usingmoods and changemood):
            moodvalue = (value if differentmood == 0 else differentmood)
            moodimagelist = ["point" + d for d in str(moodvalue)]
            huecolor = ["#00b2fe", "#7774ff"]
            if (moodvalue >= 0):
                moodimagelist = ["pointplus"] + moodimagelist
            else:
                moodimagelist[0] = "pointminus"
            for i, moodimagename in enumerate(reversed(moodimagelist)):
                tagname = moodimagename + ''.join(RandomChoices(string.ascii_lowercase, 10))
                atlist = [pointsup((xpos + (len(moodimagelist) - i) * 0.015 + 0.05, ypos - 0.02)), linear_gradient(huecolor[:2], angle=90, thresholds=[0.0, 0.75]), Transform(zoom=0.5), outline_transform(width=4, color="#000", end_color="#00000000")]
                renpy.show(moodimagename, atlist, tag=tagname, layer="arrowlayer")
            
        imagelist = ["point" + d for d in str(value)]
        if (value >= 0):
            huecolor = ["#FECC00", "#ff9d00"]
            imagelist = ["pointplus"] + imagelist
        else:
            huecolor = ["#ff0000", "#970000"]
            imagelist[0] = "pointminus"
        if (specialcolor != None):
            huecolor = specialcolor
        if (isinstance(huecolor, str)):
            huecolor = [huecolor, darken_hex_color(huecolor)]

        for i, imagename in enumerate(reversed(imagelist)):
            tagname = imagename + ''.join(RandomChoices(string.ascii_lowercase, 10))
            atlist = [pointsup((xpos + (len(imagelist) - i) * 0.03, ypos)), linear_gradient(huecolor[:2], angle=90, thresholds=[0.0, 0.75]), outline_transform(width=4, color="#000", end_color="#00000000")]
            renpy.show(imagename, atlist, tag=tagname, layer="arrowlayer")

        if (value > 0):
            PlaySound("PointsUp.ogg", instant=True)
        else:
            PlaySound("PointsDown.ogg", instant=True)

        if (pausing):
            renpy.pause(2.0)
            renpy.scene(layer='arrowlayer')

    def MoodChange(name, value, adjustoldpersondex=False):
        global coordinatingknowledge
        moodchangevalue = max(-10, min(value, 10))
        if (name == "Klara" and value > 0):
            moodchangevalue = 1
        
        if (adjustoldpersondex):
            oldpersondex[name]["Mood"] += moodchangevalue
        else:
            persondex[name]["Mood"] += moodchangevalue

        if (coordinating and name in ["May", "Brendan", "Jasmine", "Serena", "Misty", "Dawn", "Tia", "Klara"] and moodchangevalue > 0):
            coordinatingknowledge += moodchangevalue

        return moodchangevalue

    def ValueChange(name, value=1, position=0.5, pausing=True, changemood=True, adjustoldpersondex=False):        
        if (name.lower() == "kris"):
            name = "Professor Cherry"
        name = name.title()
        if name not in persondex:
            persondex[name] = copy.deepcopy(defaultpersondex[name])

        if (name == "Cheren" and IsAfter(1, 5, 2004) and value > 0):
            value = -value
        elif (name == "Klara"):
            value = 10
    
        if (adjustoldpersondex):
            oldpersondex[name]["Value"] += value
        else:
            persondex[name]["Value"] += value

        changemood = changemood and usingmoods and GetNature(name) != TrainerNature.Special

        differentmood = value
        if (changemood):
            differentmood = MoodChange(name, value, adjustoldpersondex)

        if (isinstance(position, float) and position > 0 or isinstance(position, tuple)):
            AnimateValueChange(value, position, changemood, differentmood, None, pausing)
        elif (isinstance(position, float) and position < 0):
            if (value > 0):
                PlaySound("PointsUp.ogg", instant=True)
            else:
                PlaySound("PointsDown.ogg", instant=True)

    def InvestmentChange(value, ignoremoney = False):
        global money
        global investment
        if (money >= value or ignoremoney):
            if (not ignoremoney):
                money -= value
            investment += value
            PlaySound("PointsUp.ogg")
            renpy.say(narrator, "¡Has invertido ${}! Tu inversión total es de ¡${}!".format(value, investment))
        else:
            PlaySound("PointsDown.ogg")
            renpy.say(narrator, "¡No tienes suficiente dinero para invertir ${}!".format(value))

    def GetTrait(name):
        return personalstats[name.title()]

    def TraitColor(name):
        if (name == "Charm"):
            return "#b7669e"
        elif (name == "Knowledge"):
            return "#66b77d"
        elif (name == "Courage"):
            return "#ff8412"
        elif (name == "Wit"):
            return "#60c2f8"
        elif (name == "Patience"):
            return "#e226a6"
        else:
            return "#fff"

    def TraitChange(name, increase=1):
        personalstats[name] += increase
        color = TraitColor(name)
        AnimateValueChange(increase, (0.5, 0.33), changemood=False, differentmood=0, specialcolor = color, pausing=True)
        renpy.say("", "¡Tu {{color={}}}{}{{/color}} aumento hasta el nivel {}!".format(color, name, personalstats[name]))

    def WonBattle(battle_id):
        if (battle_id in battlehistory.keys()):
            return battlehistory[battle_id]
        else:
            return False

    def RecordBattle(battle_id, won=None):
        if (won == None):
            won = _return
        battlehistory[battle_id] = won

    def HealParty(trainer = None):
        if (trainer == None):
            for pkmn in playerparty:
                pkmn.Heal()
        else:
            for pkmn in trainer.GetTeam():
                pkmn.Heal()

    def GetColor(monid):
        formatcolor = "#000"
        dexcolor = pokedexlookup(monid, DexMacros.Color)
        if (dexcolor == "Red"):
            formatcolor = "#880000"
        elif (dexcolor == "Blue"):
            formatcolor = "#000088"
        elif (dexcolor == "Yellow"):
            formatcolor = "#c4a300"
        elif (dexcolor == "Green"):
            formatcolor = "#008800"
        elif (dexcolor == "Brown"):
            formatcolor = "#ba5d00"
        elif (dexcolor == "Purple"):
            formatcolor = "#880088"
        elif (dexcolor == "Gray"):
            formatcolor = "#6b6b6b"
        elif (dexcolor == "Pink"):
            formatcolor = "#b457a0"
        elif (dexcolor == "White"):
            formatcolor = "#282828"
        return formatcolor

    renpy.music.register_channel("ctc", mixer="sfx", loop=False)
    renpy.music.register_channel("altcry", mixer="sfx", loop=False)
    renpy.music.register_channel("XYgame", mixer="music", loop=False)
    renpy.music.register_channel("crowd", mixer="sfx", loop=True)
    renpy.music.register_channel("crowd2", mixer="sfx", loop=True)
    renpy.music.register_channel("crowd3", mixer="sfx", loop=False)
    renpy.music.register_channel("points", mixer="sfx", loop=False)
    renpy.music.register_channel("misc", mixer="sfx", loop=False)
    renpy.music.register_channel("evolution", mixer="music", loop=True)
    renpy.music.register_channel("bipbop", mixer="sfx", loop=False)
    renpy.music.register_channel("bipbop2", mixer="sfx", loop=False)

    def callbackcontinue(ctc, **kwargs):
        if ctc == "end":
            renpy.sound.play("Audio/Button_A.ogg", channel="ctc")

    # Function is for BipBop voice lines.
    def boopy_voice_dungeonnarrator(event, interact=True, boopfile="Audio/pmd_speak.ogg", **kwargs):
        if event == "begin":
            renpy.sound.queue(["Audio/pmd_speak.ogg"]*40, channel="bipbop")
        elif event == "slow_done":
            renpy.sound.stop(channel="bipbop")

    def boopy_voice(event, interact=True, boopfile="Audio/pmd_speak.ogg", **kwargs):
        if event == "end":
            renpy.music.play("Audio/Button_A.ogg", channel="ctc")
            renpy.sound.stop(channel="bipbop") # This line is a fix for when user hits skip while dialogue is still incomplete. Don't remove. Seriously. It will end badly.
        
        if not interact:
            return
        
        if event == "show_done":
            renpy.sound.play(boopfile, channel="bipbop", loop=True)
        elif event == "slow_done":
            renpy.sound.stop(channel="bipbop")


    def donothing():
        pass

    def GetCharColor(findname):
        if (findname == "Gramps"):
            return "#5e5e5e"
        elif (findname == "Grandad"):
            return "#C68C28"
        elif (findname == "Wallace"):
            return "#46897c"
        elif (findname == "You" and playercharacter == None):
            return "#cf0000"
        for char in charlist:
            if ((findname.lower() in char.name.lower())
            or (char.image == "red" and findname == first_name) 
            or (char.image == "pikachu" and findname == pika_name) 
            or (char.image == "blue" and findname == blue_name)
            or (char.image == "latias" and findname.lower() == "latias")
            or (char.image == "kris" and findname.lower() == "kris")):
                return char.color
        return "#000"
    
    def getTotalElectives():
        return classstats["Normal"] + classstats["Fire"] + classstats["Water"] + classstats["Grass"] + classstats["Electric"] + classstats["Ice"] + classstats["Fighting"] + classstats["Poison"] + classstats["Ground"] + classstats["Flying"] + classstats["Psychic"] + classstats["Bug"] + classstats["Rock"] + classstats["Ghost"] + classstats["Dark"] + classstats["Dragon"] + classstats["Steel"] + classstats["Fairy"]

    def GetElective(element):
        return classstats[element]

    def GetStatRank(rank):
        return sorted(classstats.items(), key=lambda x:x[1], reverse=True)[rank][0]

    def GetHighestProficiency(rank):
        return sorted(classstats.items(), key=lambda x:x[1], reverse=True)[rank][1]

    def GetCharacterLevel(character):
        x = GetCharValue(character)
        iterations = 0
        iterator = 0
        totalsize = 0

        while (x >= totalsize):
            iterations += 1
            iterator += 10
            totalsize += iterator

        return iterations

    def GetEXPRequiredForLevel(character):
        level = GetCharacterLevel(character)

        iterations = 0
        iterator = 0
        totalsize = 0
        for i in range(0, level):
            iterations += 1
            iterator += 10
            totalsize += iterator

        return totalsize

    def GetHighestLevel():
        highestlevel = 0
        for mon in playerparty:
            if (mon.GetLevel() > highestlevel):
                highestlevel = mon.GetLevel()
        return highestlevel

    def GetHighestLevelAll():
        highestlevel = 0
        for mon in AllPokemon():
            if (mon.GetLevel() > highestlevel):
                highestlevel = mon.GetLevel()
        return highestlevel

    def GetAllPokemonIn():
        return [418, 419, 100, 101, 590, 591, 352, 343, 344, 234, 899, 776, 86, 87, 459, 460, 74.1, 75.1, 76.1, 712, 713, 739, 740, 757, 758, 220, 221, 473, 225, 337, 338, 872, 873, 425, 426, 624, 625, 983, 996, 997, 998, 27.1, 28.1, 703, 129, 130, 79.1, 80.2, 199.1, 618.1, 163, 164, 187, 188, 189, 56, 57, 979, 296, 297, 708, 709, 723, 724, 46, 47, 932, 933, 934, 531.1, 122.1, 866, 131.1, 88, 89, 359.1, 263.1, 264.1, 862, 554.1, 555.2, 555.3, 38, 38.1, 446, 143, 427, 428, 428.1, 359, 870, 506, 4, 258, 387, 179, 363, 532, 41, 328, 396, 280, 540, 246, 551, 371, 304, 669, 206, 554, 194, 548, 170, 361, 447, 747, 529, 198, 290, 566, 200, 696, 597, 742, 531, 631, 746, 781, 479, 615, 214, 336, 618, 357, 561, 213, 774, 778, 302, 780, 227, 303, 263, 155, 399, 191, 835, 133, 919, 406, 29, 32, 333, 307, 401, 111, 710, 659, 967, 777, 764, 431, 607, 767, 412, 81, 351, 559, 568, 104, 629, 677, 917, 744, 353, 88.1, 714, 965, 439, 507, 5, 259, 388, 180, 364, 533, 42, 329, 397, 281, 541, 247, 552, 372, 305, 670, 982, 555, 195, 549, 171, 362, 448, 748, 530, 291, 567, 429, 697, 598, 743, 264, 156, 400, 192, 836, 134, 920, 315, 30, 33, 334, 308, 402, 112, 711, 660, 432, 608, 768, 413, 82, 560, 569, 105, 630, 678, 918, 745, 354, 89.1, 715, 966, 122, 508, 6, 260, 389, 181, 365, 534, 169, 330, 398, 282, 542, 248, 553, 373, 306, 671, 478, 430, 678.1, 292, 157, 135, 407, 31, 34, 464, 609, 414, 462, 745.1, 745.2, 136, 196, 197, 470, 471, 700, 636, 637, 175, 176, 468, 236, 237, 106, 107, 238, 124, 240, 126, 467, 360, 202, 438, 185, 440, 113, 242, 458, 226, 848, 849, 849.1, 79, 80, 199, 215, 461, 725, 726, 727, 633, 634, 635, 556, 298, 58, 59, 602, 603, 604, 131, 852, 853, 690, 691, 194.1, 980, 580, 581, 976, 595, 596, 688, 689, 592, 593, 318, 319, 885, 886, 887, 393, 394, 395, 183, 184, 190, 424, 223, 224]
    
    def GetImplementedSpecialEvos():
        return [414, 413, 413.1, 413.2, 292, 122, 745, 745.1, 745.2, 678.1, 106, 107, 237, 124, 126, 202, 980, 424, 853, 185, 226, 849, 849.1]

    def GetPartySpecies():
        partyids = []
        for mon in playerparty:
            partyids.append(mon.GetId())
        return partyids

    def GetGrade():
        grade = 0
        for key in battlehistory.keys():
            if (key[:3] == "Oak" and WonBattle(key)):
                grade += 1
        return grade

    def GetWinLoss(char):
        wins = 0
        losses = 0
        for key in battlehistory.keys():
            if (char in key):
                if (WonBattle(key)):
                    wins += 1
                else:
                    losses += 1
        return (wins, losses)

    def IncreaseProficiency(type, amount):
        classstats[type] = round(classstats[type] + amount, 2)
        newtotal = FormatNum(classstats[type])
        levelcap = str(math.floor(classstats[type]))
        renpy.say(narrator, "¡Tu competencia en tipo {} aumento hasta el nivel {}! Tus Pokémon de tipo {} ahora pueden llegar hasta el nivel {}.".format(type, newtotal, type, levelcap))

    def GetAverageProficiency():
        avgprof = 0
        for value in classstats.values():
            avgprof += value
        return round(avgprof / 18, 2)

    def GetRememberableMoves(partymon):
        moveslist = GetLevelMoves(partymon, partymon.GetLevel())
        justmoves = []
        for move in moveslist:
            if (move[1] not in partymon.GetMoveNames() and move[1] not in justmoves):
                justmoves.append(move[1])
        return justmoves

    def AddPikachu():
        if (pikachuobj not in playerparty):
            pikachuobj.Heal()
            AddMon(pikachuobj)

    def BattleTeamTraining():
        renpy.transition(dissolve)
        renpy.hide_screen("currentdate")
        for mon in playerparty:
            mon.GainExperience(pow(AimLevel(), 3) / 25 * (1 + max(0, (AimLevel() - mon.GetLevel()) / 10)))
        renpy.transition(dissolve)
        renpy.show_screen("currentdate")

    def AddMon(newmon, nickname = False):
        global hidebattleui
        global mustswitch
        playerparty.append(newmon)
        if (nickname):
            newmon.Nickname = renpy.input("Would you like to give it a nickname?", default=pokedexlookup(newmon.GetId(), DexMacros.Name), exclude="{}[[]%<>", length=12)
            if (newmon.Nickname == "" or newmon.Nickname == pokedexlookup(newmon.GetId(), DexMacros.Name).lower()):
                newmon.Nickname = pokedexlookup(newmon.GetId(), DexMacros.Name)
        if (InDungeon()):
            playerparty.remove(newmon)
            box.append(newmon)
            renpy.say(None, "El Pokémon capturado fue enviado al PC.")
        elif (len(playerparty) > 6):
            hidebattleui = True
            mustswitch = True
            renpy.say(None, "Elige un Pokémon para enviarlo al PC. Puedes pasar el ratón por encima de los Pokémon de tu grupo para ver sus estadísticas.")
            sendtopc = renpy.call_screen("SendToPC")
            playerparty.remove(sendtopc)
            box.append(sendtopc)
            hidebattleui = False
            mustswitch = False

    def PlaySound(soundname, otherchannel="misc", instant=False):
        renpy.music.set_volume(0.25, delay=0.0, channel="music")
        if (not instant):
            renpy.sound.queue("Audio/" + soundname, channel=otherchannel)
        else:
            renpy.sound.play("Audio/" + soundname, channel=otherchannel)
        renpy.music.set_volume(1.0, delay=2.0, channel="music")

    def DisplayGetItem(itemname):
        if isinstance(itemname, int):
            itemname = GetItemName(itemname)
        itemdict = {
            "Larvesta Egg" : "larvestaegg",
            "Togepi Egg" : "togepiegg",
            "Tyrogue Egg" : "tyrogueegg",
            "Magby Egg" : "magbyegg",
            "Wynaut Egg" : "wynautegg",
            "Bonsly Egg" : "bonslyegg",
            "Mantyke Egg" : "mantykeegg",
            "Toxel Egg" : "toxelegg",
            "Deino Egg" : "deinoegg",
            "Lucky Egg" : "basicegg",
            "Soothe Bell" : "soothebell",
            "Manaphy Egg" : "manaphyegg",
            "Mirage Research #4" : "ludicolobook"
        }

        if (itemname in itemdict):
            itemname = itemdict[itemname]
        else:
            itemname = "dungeonitems"

        renpy.show(itemname, [itemhover])
        renpy.pause(1.0)
        renpy.show(itemname, [])
        renpy.pause(1.5)
        renpy.show(itemname, [itemhide])
        renpy.pause(1.5)
        renpy.hide(itemname)

    def RemoveForeverals(pkmn):
        if (pkmn.GetForeverals() != []):
            if (inbattle):
                renpy.invoke_in_new_context(renpy.say, None, "Por favor, espera a que termine la batalla para desequipar las Foreverals.")
            elif (InDungeon()):
                renpy.invoke_in_new_context(renpy.say, None, "or favor, espera a salir de la mazmorra para desequipar las Foreverals.")
            else:
                foreveralinv.append(pkmn.GetForeverals()[0])
                pkmn.Foreverals = []
                pkmn.RecalculateStats()

    def FormatNum(num):
        return f'{num:g}'

    def GetCharsInPlace(place):
        if (excusesecondelective or excusesecondhomeroom):
            return []

        additive = set()
        base = set(availablechars[place])

        if (place == "Battle Hall"):
            additive.add("Raihan")
        elif (place == "Garden"):
            additive.add("Tia")
        elif (place == "Research Center"):
            additive.add("Sonia")
        elif (place == "Academy"):
            additive.add("Jasmine")
            additive.add("Grusha")
        elif (place == "Student Center"):
            additive.add("Yellow")
        elif (place == "Pledge Hall"):
            additive.add("Wally")

        return list((base.union(additive)).intersection(GetStudents()))

    def GetCharsInTable(table):
        npcs = []
        if (table == "Angry Table"):
            npcs = ["Blue", "Flannery", "Misty", "Hilbert"]
        elif (table == "Cheerful Table"):
            npcs = (["Whitney", "Gardenia", "Bianca", "Leaf"] if IsBefore(13, 4, 2004) else ["Bianca", "Leaf", "Tia", "Whitney", "Gardenia"])
        elif (table == "Busy Table"):
            npcs = ["Nate", "Skyla", "Nessa", "Rosa"] 
            if (IsAfter(20, 4, 2004)):
                npcs = ["Nate", "Skyla", "Nessa", "Sonia", "Rosa"] 
            elif (IsDate(20, 4, 2004)):
                npcs = ["Nate", "Skyla", "Rosa"] 
        elif (table == "Romantic Table"):
            npcs = ["Serena", "Calem", "Brendan", "May"]
        elif (table == "Calm Table"):
            npcs = ["Sabrina", "Bea", "Hilda", "Cheren"]
            if (IsAfter(15, 4, 2004)):
                npcs = ["Sabrina", "Bea", "Hilda"]
                if (IsAfter(26, 4, 2004)):
                    npcs = ["Sabrina", "Bea", "Hilda", "Jasmine", "Grusha"]
                    if ("Jasmine" not in GetStudents()):
                        npcs.remove("Jasmine")
                    if ("Grusha" not in GetStudents()):
                        npcs.remove("Grusha")

                elif (IsDate(26, 4, 2004)):
                    npcs = ["Bea", "Hilda", "Jasmine", "Grusha"]
        elif (table == "Quiet Table"):
            npcs = ["Silver", "Erika", "Dawn", "Professor Cherry"]

        return npcs
    
    def GetCharValue(char):
        if ("Value" not in persondex[char].keys()):
            persondex[char]["Value"] = 0
        if (IsAfter(1, 5, 2004) and char == "Cheren" and playercharacter == None):
            return -persondex["Cheren"]["Value"]
        return persondex[char]["Value"]

    def GetCharTypes(char):
        char = char.title()
        if (char in classdex.keys()):
            base = list(classdex[char])
            if (char == "Leaf" and HasEvent("Leaf", "ClassSwap")):
                return ["Normal", "Grass", "Electric"]
            elif (char == "Nate" and HasEvent("Nate", "ClassSwap")):
                return ["Dark", "Steel", "Poison"]
            return base
        elif (char == "Yellow"):
            return ["Normal", "Electric"]
        elif (char == "Ethan"):
            return [GetStatRank(0), GetStatRank(1), GetStatRank(2)]
        elif (char == "Janine"):
            return ["Poison", "Fighting"]
        elif (char == "Brawly"):
            return ["Fighting", "Water"]
        else:
            return []

    def strip_numbers(string):
        return "".join([char for char in string if not char.isdigit()])

    def strip_letters(string):
        return "".join([char for char in string if char.isdigit()])     

    def PrintSceneConditions(scene):
        if (scene == None):
            return ""
        sceneconditionsdict = sceneconditions[scene]
        character = strip_numbers(scene)
        if (character == "Kris"):
            character = "Professor Cherry"
        rank = int(strip_letters(scene))
        conditions = ""
        for condition, value in sceneconditionsdict.items():
            skipcomma = False
            if (condition == "Level"):
                conditions += "Lv. {}".format(value)
            elif (condition == "Date"):
                if (IsBefore(value[0], value[1], value[2])):
                    return "The future is cloudy..."
                skipcomma = True
            elif (condition == "Event"):
                conditions += value[2]
            elif (condition == "Time"):
                conditions += value
            elif (condition == "NotEvent"):
                if (HasEvent(value[0], value[1])):
                    return value[2]
                skipcomma = True
            elif (condition == "Others"):
                for other in value:
                    if (other not in GetStudents()):
                        return "The future is cloudy..."
                skipcomma = True
            else:#handles character locks
                if (not persondex[condition]["Named"]):
                    return "The future is cloudy..."
                conditions += "Rank {} w/{}".format(value, condition)
            if (not skipcomma):
                conditions += ", "
        return conditions[:-2]

    def EvaluateSceneConditions(scene):
        sceneconditionsdict = sceneconditions[scene]
        character = strip_numbers(scene)
        if (character == "Kris"):
            character = "Professor Cherry"
        rank = int(strip_letters(scene))
        if (GetRelationshipRank(character) >= rank):
            return False
        for condition, value in sceneconditionsdict.items():
            if (condition == "Level"):
                if (GetCharacterLevel(character) < value):
                    return False
            elif (condition == "Date"):
                if (IsBefore(value[0], value[1], value[2])):
                    return False
            elif (condition == "Event"):
                if (not HasEvent(character, value[1])):
                    return False
            elif (condition == "NotEvent"):
                if (HasEvent(character, value[1])):
                    return False
            elif (condition == "Time"):
                if (timeOfDay != value):
                    return False
            elif (condition == "Others"):
                for other in value:
                    if (other not in GetStudents()):
                        return False
            else:#handles character locks
                if (GetRelationshipRank(condition) < value):
                    return False
        return True

    def GetNextScene(character):
        if (character == None):
            return None
        for scene in sceneconditions.keys():
            if ((character in scene or (character == "Professor Cherry" and "Kris" in scene)) and "Part" not in scene):#Part2/3/4 whatever scenes are hidden, and have special activation criteria
                rank = int(strip_letters(scene))
                if (GetRelationshipRank(character) < rank):
                    return scene
        return None

    def GetScenes(characters):
        scenes = []
        for character in characters:
            sceneappended = False
            for scene in sceneconditions.keys():
                if (GetNextScene(character) == scene and EvaluateSceneConditions(scene)):
                    scenes.append(scene)
                    sceneappended = True
                    break
            if (not sceneappended):
                scenes.append(False)

        for i in range(len(scenes)):
            scenes[i] = (characters[i], scenes[i])
        return scenes

    def GetSeenScenes():
        scenes = []
        for scenename in list(sceneconditions.keys()) + part2scenes:
            pattern = r"^(.*?)(\d)Part(\d)$"
            match = re.match(pattern, scenename)
            if match:
                character, rank, scenepart = match.groups()
                rank = int(rank)
                scenepart = int(scenepart)
            else:
                rank = int(strip_letters(scenename))
                character = strip_numbers(scenename)
                scenepart = 1
            if scenepart > 1 and not HasEvent(character, scenename):
                continue
            if (character == "Kris"):
                character = "Professor Cherry"
            if (GetRelationshipRank(character) >= rank):
                scenes.append(scenename)
        return sorted(scenes)

    def GetRelationship(character):
        if "Relationship" in persondex[character].keys():
            return persondex[character]["Relationship"]
        else:
            return "Acquaintance"

    def GetValue(character):
        if "Value" in persondex[character].keys():
            return persondex[character]["Value"]
        else:
            return 0

    def GetEvents(character):
        if "Events" not in persondex[character].keys():
            persondex[character]["Events"] = []
        return persondex[character]["Events"]

    def GetRelationshipRank(character):
        if "RelationshipRank" in persondex[character].keys():
            return persondex[character]["RelationshipRank"]
        else:
            return 0

    def GetNature(character):
        if (character == "Kris"):
            character = "Professor Cherry"
        if (playercharacter != None and character == first_name):
            return TrainerNature.Friendly
        elif (character == "Grandad"):
            return TrainerNature.Friendly
        elif (character == "Wallace"):
            return TrainerNature.Moody
        elif "Nature" not in persondex[character].keys():
            persondex[character]["Nature"] = copy.copy(defaultpersondex[character]["Nature"])
        return persondex[character]["Nature"]

    def GetMood(character):
        character = character.title()
        
        if (playercharacter != None and character == first_name.title()):
            return math.floor(persondex[playercharacter]["Mood"] * 3)
        elif (character not in defaultpersondex.keys()):
            return 0
        elif (playercharacter == "Blue" and character == "Gramps"):
            character = "Professor Oak"
        elif (playercharacter == "Lisia" and character == "Uncle W"):
            character = "Instructor Wallace"

        if "Mood" not in persondex[character].keys():
            persondex[character]["Mood"] = copy.copy(defaultpersondex[character]["Mood"])
        return persondex[character]["Mood"]

    # leave static, altered by GetStudents
    altclassdex = {
        "Normal" : {"Bianca", "Whitney", "Cheren"},
        "Fire" : {"May", "Serena", "Flannery"},
        "Water" : {"Nessa", "Misty", "Brendan"},
        "Grass" : {"Brendan", "Leaf", "Gardenia"},
        "Electric" : {"Nate", "Leaf", "Rosa"},
        "Ice" : {"Hilbert", "Misty", "Dawn"},
        "Fighting" : {"Calem", "May", "Bea"},
        "Poison" : {"Hilda", "Silver", "Nate"},
        "Ground" : {"Brendan", "Serena", "Flannery"},
        "Flying" : {"Calem", "Skyla", "Blue"},
        "Psychic" : {"Bianca", "Sabrina", "Rosa"},
        "Bug" : {"Rosa", "Skyla", "May"},
        "Rock" : {"Nessa", "Bea", "Hilda"},
        "Ghost" : {"Sabrina", "Gardenia", "Hilbert"},
        "Dark" : {"Cheren", "Serena", "Silver"},
        "Dragon" : {"Dawn", "Leaf", "Blue"},
        "Steel" : {"Hilbert", "Hilda", "Nate"},
        "Fairy" : {"Dawn", "Whitney", "Calem"}
    }

    def GetYellowStudents():
        baseset = GetStudents("All") - {"Yellow"}
        finallist = []
        for student in baseset:
            if (GetNature(student) != TrainerNature.Special):
                finallist.append(student)
        return finallist
    
    def GetStudents(element = "All", ignoreabsences = False):
        if (element == "All"):
            totalset = set()
            for otherelement in altclassdex.keys():
                totalset.update(GetStudents(otherelement))
            additions = {"Professor Cherry", "Ethan", "Janine"}
            if (IsAfter(1, 5, 2004)):
                additions.update({"Yellow"})
            return (totalset | additions) - (RemoveStudents(element) if not ignoreabsences else set())
        else:
            return (((altclassdex[element] 
            | ({"Erika"} if element in ["Grass", "Poison"] and IsAfter(10, 4, 2004) else set()) 
            | ({"Tia"} if element in ["Dragon", "Psychic"] and ((IsDate(13, 4, 2004) and timeOfDay == "Afternoon") or IsAfter(13, 4, 2004)) else set())
            | ({"Sonia"} if element in ["Electric", "Fire"] and ((IsDate(20, 4, 2004) and timeOfDay == "Afternoon") or IsAfter(19, 4, 2004)) else set())
            | ({"Jasmine"} if element in ["Steel", "Ground"] and (IsAfter(26, 4, 2004) and (Random(True, "JasmineElective") > (0.5 - GetRelationshipRank("Grusha") * .1) or ignoreabsences) or IsDate(26, 4, 2004) and timeOfDay == "Afternoon") else set())#the jasmine/grusha swap is *not* a typo
            | ({"Grusha"} if element in ["Ice", "Flying"] and (IsAfter(26, 4, 2004) and (Random(True, "GrushaElective") > (0.5 - GetRelationshipRank("Jasmine") *.1) or ignoreabsences) or IsDate(26, 4, 2004) and timeOfDay == "Afternoon") else set())#the jasmine/grusha swap is *not* a typo
            | ({"Wally"} if element in ["Fairy", "Fighting"] and IsAfter(9, 5, 2004) else set()))
            | ({"Raihan"} if element in ["Dragon", "Rock"] and (IsAfter(13, 5, 2004) or IsDate(13, 5, 2004) and timeOfDay in ["Evening", "Night"]) else set())
            | ({"Leaf"} if element in ["Normal"] and IsAfter(12, 5, 2004) else set())
            | ({"Nate"} if element in ["Dark"] and IsAfter(18, 5, 2004) else set())
            | ({"Klara"} if element in ["Bug", "Water"] and IsAfter(24, 5, 2004) else set()))
            - (RemoveStudents(element) if not ignoreabsences else set()))

    def WillStudy(element = "All"):
        basegroup = GetStudents(element)
        if ("Yellow" in basegroup):
            basegroup.remove("Yellow")
        if ("Professor Cherry" in basegroup):
            basegroup.remove("Professor Cherry")
        if ("Ethan" in basegroup):
            basegroup.remove("Ethan")
        if ("Janine" in basegroup):
            basegroup.remove("Janine")
        newset = set()
        for student in basegroup:
            if (persondex[student]["Named"] and persondex[student]["Value"] >= 1 and GetMood(student) >= 0):
                newset.add(student)
        return newset

    def RemoveStudents(element):
        removedict = {
            "Leaf": [IsDate(10, 5, 2004),#when she skips a day of school to search for Tia
                    IsAfter(12, 5, 2004) and element == "Dragon",#after leaving dragon class
                    IsDate(13, 5, 2004) and timeOfDay == "Morning" and element == "Normal"],#doesn't take normal class for first period 
            "Sabrina": [IsAfter(1, 5, 2004) and not rescuedsabrina and IsBefore(16, 5, 2004)],#when she is missing in the forest
            "Tia": [IsAfter(1, 5, 2004) and not rescuedtia and IsBefore(16, 5, 2004)],#when she is missing in the forest
            "Cheren": [IsAfter(9, 5, 2004) and (not rescuedsabrina or not rescuedwill or not rescuedtia) and IsBefore(16, 5, 2004)],#when he's spending all his time searching for will/sabrina/tia
            "Nessa": [IsDate(13, 5, 2004) and timeOfDay == "Afternoon"],#when they're showing raihan around the school
            "Sonia": [IsDate(13, 5, 2004) and timeOfDay == "Afternoon"],#when they're showing raihan around the school
            "Bianca": [IsAfter(17, 5, 2004) and IsBefore(23, 5, 2004)],
            "Nate": [IsAfter(18, 5, 2004) and element == "Electric"],
            "Blue": [IsAfter(23, 5, 2004) and IsBefore(28, 5, 2004) and timeOfDay == "Afternoon"]#when Yellow and Ethan are pissed at him
        }
        newset = set()
        for key, value in removedict.items():
            for func in value:
                if (func):
                    newset.add(key)
                    break
        return newset.union(removestudents).union(removelunchstudents)

    def IsPresent(character, element = "All"):
        return not IsAbsent(character, element)

    def IsAbsent(character, element = "All"):
        return character not in GetStudents(element)

    def PartyHasType(element):
        for mon in playerparty:
            if mon.HasType(element):
                return True
        return False

    def PlayerHighestLevel():
        highestlevel = 0
        for mon in AllPokemon():
            if (mon.GetLevel() > highestlevel):
                highestlevel = mon.GetLevel()
        return highestlevel

    def MonCanLearn(mon, move):
        if (move in mon.GetMoveNames()):
            return False
        specialmoves = {
            "Simple World": ["Normal"],
            "Steady Flame": ["Fire"],
            "Healing Spring": ["Water"],
            "Bark Up": ["Grass"],
            "Energize": ["Electric"],
            "Slow Freeze": ["Ice"],
            "Disabling Poke": ["Fighting"],
            "Bad Breath": ["Poison"],
            "Burial Ground": ["Ground", "Ghost"],
            "Wing It": ["Flying"],
            "Clear Mind": ["Psychic"],
            "Chrysalize": ["Bug"],
            "Splinter Shield": ["Rock"],
            "Deathless": ["Ghost"],
            "Enshroud": ["Dark"],
            "Legacy": ["Dragon"],
            "Metallize": ["Steel"],
            "Ardent Gaze": ["Fairy"]
        }
        if (move in specialmoves.keys()):
            for element in specialmoves[move]:
                if (mon.HasType(element)):
                    return True
        return move in str(GetLearnset(mon.GetId()))

    def PartyCanLearn(move):
        count = 0
        for mon in playerparty:
            if (MonCanLearn(mon, move)):
                count += 1
        return count

    ##TESTING FEATURES##
    def MaxAll():
        for keyname in defaultpersondex.keys():
            persondex[keyname]["Value"] = 350
        for stat in personalstats.keys():
            personalstats[stat] = 100
        for stat in classstats.keys():
            classstats[stat] = 100

    def GetUnimplementedPokemon():
        unimplemented = []
        for mon in GetAllPokemonIn():
            found = False
            for entry in pokedex.values():
                if (entry[DexMacros.Id] == mon):
                    found = True
                    break
            if (not found):
                unimplemented.append(mon)
        return unimplemented

    def GetUnimplementedLearnsets():
        unimplemented = []
        for mon in GetAllPokemonIn():
            found = False
            for entry in learndex:
                if (entry[0] == mon):
                    found = True
                    break
            if (not found):
                unimplemented.append(mon)
        return unimplemented

    def GetEvolutions():
        for mon in GetAllPokemonIn():
            if (mon not in GetImplementedSpecialEvos()):
                evoconditions = pokedexlookup(mon, DexMacros.Evolve)
                if (evoconditions != None and len(evoconditions) != 6 or pokedexlookup(mon, DexMacros.Prevo) != None and pokedexlookup(mon, DexMacros.Prevo) != pokedexlookup(mon - 1, DexMacros.Name)):
                    print(pokedexlookup(mon, DexMacros.Name) + ": " + (evoconditions if evoconditions != None else "None"))

    def GetImplements(levels):
        finalmoves = set()
        unimplementedmons = set()
        if (isinstance(levels, int)):
            levels = range(levels)
        for level in levels:
            for mon in GetAllPokemonIn():
                if (pokedexlookup(mon, DexMacros.Id) == None):
                    unimplementedmons.add(mon)
                else:
                    newmoves = GetLevelMoves(Pokemon(mon), level, True)
                    for move in newmoves:
                        if (not MoveIsIn(move[1])):
                            finalmoves.add(move[1])

        for fvl in foreveraldex:
            for move in fvl[FVLMacros.FVLMoves]:
                if (not MoveIsIn(move)):
                    finalmoves.add(move)

        finalabilities = set()
        for mon in GetAllPokemonIn():
            if (pokedexlookup(mon, DexMacros.Id) == None):
                unimplementedmons.add(mon)
            else:
                for ability in GetAbilities(mon):
                    if (not AbilityIsIn(ability)):
                        finalabilities.add(ability)

        for fvl in foreveraldex:
            if (fvl[FVLMacros.FVLType] == ForeveralTypes.AddAbility):
                for ability in fvl[FVLMacros.FVLTypeData]:
                    if (not AbilityIsIn(ability)):
                        finalabilities.add(ability)

        finalmovestring = ""
        for move in finalmoves:
            finalmovestring += move + ", "

        finalmovestring += "\n\n\nabilities after this\n\n\n"

        for ability in finalabilities:
            finalmovestring += ability + ", "

        finalmovestring += "\n\n\n'mons after this\n\n\n"

        for mon in unimplementedmons:
            finalmovestring += str(mon) + ", "

        print(finalmovestring)
        with open("../Moves.txt","w") as egg:
            egg.write(finalmovestring)
        egg.closed

    def RankUpClasses():
        for classkey in classstats.keys():
            classstats[classkey] += 10

    def eb():
        return EnemyBattlers()[0]

    def ebm(movename):
        eb().Moves = [GetMove(movename)]

    def fb():
        return FriendlyBattlers()[0]

    def fbm(movename):
        fb().Moves = [GetMove(movename)]

    ##END TESTING FEATURES##
    def IsAfter(day, month, year):
        return not IsBefore(day, month, year) and not IsDate(day, month, year)

    def IsBefore(day, month, year):
        return (calDate.year < year 
            or calDate.month < month and calDate.year == calDate.year
            or calDate.day < day and calDate.month == month and calDate.year == calDate.year)

    def IsDate(day = None, month = None, year = None):
        return (day == None or day == calDate.day) and (month == None or month == calDate.month) and (year == None or year == calDate.year)

    def GetSocialPoints():
        value = 0
        for keyname in persondex.keys():
            value += GetCharValue(keyname)
        return value

    def InDungeon(includetechnical = True):
        return ("activedungeon" in globals() and activedungeon != None and not activedungeon.IsFinished()) or (includetechnical and technicaldungeon)

    def AimLevel():
        index = (calDate - datetime.datetime(2004, 4, 5)).days
        levels = [5, 5, 5, 5, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 20, 20, 21, 21, 21, 21, 22, 22, 22, 22, 23, 23, 23, 23, 24, 24, 24, 24, 25, 25, 25, 25, 26, 26, 26, 26, 27, 27, 27, 27, 28, 28, 28, 28, 29, 29, 29, 29, 30, 30, 30, 30, 30, 31, 31, 31, 31, 31, 32, 32, 32, 32, 32, 33, 33, 33, 33, 33, 34, 34, 34, 34, 34, 35, 35, 35, 35, 35, 36, 36, 36, 36, 36, 37, 37, 37, 37, 37, 38, 38, 38, 38, 38, 39, 39, 39, 39, 39, 40, 40, 40, 40, 40, 41, 41, 41, 41, 41, 42, 42, 42, 42, 42, 43, 43, 43, 43, 43, 44, 44, 44, 44, 44, 45, 45, 45, 45, 45, 46, 46, 46, 46, 46, 47, 47, 47, 47, 47, 48, 48, 48, 48, 48, 49, 49, 49, 49, 49, 50, 50, 50, 50, 50, 51, 51, 51, 51, 51, 52, 52, 52, 52, 52, 53, 53, 53, 53, 53, 54, 54, 54, 54, 54, 55, 55, 55, 55, 55, 56, 56, 56, 56, 56, 57, 57, 57, 57, 57, 58, 58, 58, 58, 58, 59, 59, 59, 59, 59, 60, 60, 60, 60, 60, 61, 61, 61, 61, 61, 62, 62, 62, 62, 62, 63, 63, 63, 63, 63, 64, 64, 64, 64, 64, 65, 65, 65, 65, 65, 66, 66, 66, 66, 66, 67, 67, 67, 67, 67, 68, 68, 68, 68, 68, 69, 69, 69, 69, 69, 70, 70, 70, 70, 70, 71, 71, 71, 71, 71, 72, 72, 72, 72, 72, 73, 73, 73, 73, 73, 74, 74, 74, 74, 74, 75, 75, 75, 75, 75, 76, 76, 76, 76, 76, 77, 77, 77, 77, 77, 78, 78, 78, 78, 78, 79, 79, 79, 79, 79, 80, 80, 80, 80, 80, 81, 81, 81, 81, 81, 82, 82, 82, 82, 82, 83, 83, 83, 83, 83, 84, 84, 84, 84, 84, 85, 85, 85, 85, 85]
        return levels[index]

    def GetLiberaColor(firstcolor = True):
        if (pikachuobj.GetTypes() in [[], ["Electric"]]):
            return "#fff"
        if (libtypes == []):
            if (firstcolor):
                return GetTypeColor(pikachuobj.GetTypes()[0])
            else:
                if (len(pikachuobj.GetTypes()) > 1):
                    return GetTypeColor(pikachuobj.GetTypes()[1])
                else:
                    return GetTypeColor(pikachuobj.GetTypes()[0]) 
        elif (firstcolor):
            return GetTypeColor(libtypes[0])
        else:
            if (len(libtypes) > 1):
                return GetTypeColor(libtypes[1])
            else:
                return GetTypeColor(libtypes[0]) 

    def UpdateForeverals():
        added = {}
        for fvl in foreveraldex:
            requiredrank = 0
            level = fvl[FVLMacros.FVLLevel]
            trainer = fvl[FVLMacros.FVLTrainer]
            name = fvl[FVLMacros.FVLName]
            requiredrank = math.floor(level / 2.0)
            if (GetCharacterLevel(trainer) >= level
            and GetRelationshipRank(trainer) >= requiredrank
            and name not in claimedforeverals):
                foreveralinv.append(name)
                claimedforeverals.append(name)
                if (trainer not in added.keys()):
                    added[trainer] = [name]
                else:
                    added[trainer].append(name)
        return added

    def GetCharacterSprite(character, overridemood = None, uniform = False, extras="", protag=False):
        character = character.title()
        if (character == "Klara"):
            overridemood = 151#KLARA NOTE: Your favorite number, right? I'll always smile for you!~ <3

        if (character == first_name and playercharacter != None):
            return "red shadow noeyes frownmouth"
        if (protag):
            character = "red"
        spritename = character.lower().strip()
        mood = GetMood(character)
        moodname = ""
        outfitname = "uniform" if uniform else ""

        if (character == "Professor Cherry"):
            spritename = "kris"
            if (outfitname == "uniform"):
                outfitname = ""
        elif (character in ["Professor Oak", "Gramps"]):
            spritename = "oak"
        elif (character == "Grandad"):
            spritename = "oldman"

        if (character == "Tia" and IsAfter(16, 4, 2004)):
            outfitname += " hat"
        elif (character == "Yellow"):
            if (uniform):
                if (HasEvent("Yellow", "LostHat")):
                    outfitname = "uniformbraidfront"
            else:
                if (HasEvent("Yellow", "LostHat")):
                    outfitname = "neutralbraidfront"
        elif (character == "Sabrina" and outfitname == "" and (IsAfter(11, 5, 2004) and rescuedsabrina or IsAfter(15, 5, 2004))):
            outfitname = "gen2"
        elif (character == "Klara"):
            outfitname += " makeup hairpin"
        elif (character == "Melody"):
            outfitname += " on"
        elif (character == "Grandad"):
            outfitname += " milotic"

        if (overridemood != None):
            mood = overridemood
        elif (character == "Bianca" and ((IsDate(18, 5, 2004) and timeOfDay in ["Afternoon", "Noon", "Evening", "Night"]) or (IsAfter(18, 5, 2004) and IsBefore(23, 5, 2004)))):
            mood = -4

        if (mood <= -5):
            moodname = "angry"
            if (character == "Cheren"):
                moodname = "sad2eyes noshine shadow smilemouth"
        elif (mood < 0):
            moodname = "sad"
        elif (mood >= 5):
            moodname = "happy"
            if (character in ["Hilbert", "Silver", "Sabrina"]):
                moodname = "smilemouth"

        return spritename + " " + moodname + " " + outfitname + " " + extras

    def GetTables():
        if (IsAfter(24, 5, 2004)):
            return {
                "Disciplinary Table": ["Cheren", "Silver", "Gardenia", "Skyla"], 
                "Home Table": ["Leaf", "Blue", "Yellow", "Ethan"],
                "Famous Table": ["Rosa", "Nessa", "Raihan", "Sonia", "Sabrina"],
                "Scheming Table": ["Nate", "Hilbert", "Hilda", "Bea", "Bianca"],
                "Romantic Table": ["Calem", "Serena", "Wally", "May", "Brendan"],
                "Independent Table": ["Professor Cherry", "Misty", "Klara", "Dawn", "Erika"], 
                "Medical Table": ["Flannery", "Whitney", "Tia", "Jasmine", "Grusha"],
                "Melody's Table": ["Melody"]
            }
        elif (IsBefore(17, 5, 2004) and not rescuedwill):
            return {
                "Disciplinary Table": ["Cheren", "Silver", "Gardenia", "Skyla"], 
                "Home Table": ["Leaf", "Blue", "Ethan", "Yellow"],
                "Famous Table": ["Nessa", "Raihan", "Sonia"],
                "Scheming Table": ["Nate", "Hilbert", "Hilda", "Bea"],
                "Romantic Table": ["Calem", "Serena", "Wally", "May", "Brendan"],
                "Independent Table": ["Erika", "Misty", "Dawn", "Professor Cherry"], 
                "Medical Table": ["Flannery", "Whitney", "Jasmine", "Grusha"],
                "Remedial Table": ["Rosa", "Bianca", "Sabrina", "Tia"]
            }
        else:
            return {
                "Disciplinary Table": ["Cheren", "Silver", "Gardenia", "Skyla"], 
                "Home Table": ["Leaf", "Blue", "Yellow", "Ethan"],
                "Famous Table": ["Rosa", "Nessa", "Raihan", "Sonia", "Sabrina"],
                "Scheming Table": ["Nate", "Hilbert", "Hilda", "Bea", "Bianca"],
                "Romantic Table": ["Calem", "Serena", "Wally", "May", "Brendan"],
                "Independent Table": ["Professor Cherry", "Misty", "Dawn", "Erika"], 
                "Medical Table": ["Flannery", "Whitney", "Tia", "Jasmine", "Grusha"],
                None: []
            }

    def GetLiberationLimit():#returns a tuple with the raw value and a breakdown
        if (not usingliberationlimit):
            return (0, [])
        ll = 0
        breakdown = []
        for move in pikachuobj.GetMoveNames():
            newpower = GetCalculatedMovePower(move)
            ll += newpower
            breakdown.append(("Move", move, newpower))#"Move", movename, ll increase
        if (pikachuobj.GetId() != 25.2 and pikachuobj.GetForeverals() == []):
            scalingmonbst = pokedexlookup(pikachuobj.GetId(), DexMacros.Total)
            bstfifth = math.floor(scalingmonbst / 5)
            ll += bstfifth
            breakdown.append(("Diveral", pikachuobj.GetId(), bstfifth))#"Diveral", mon diveral'd into, ll increase
        for fvl in pikachuobj.GetForeverals():
            if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.Scaling):
                scalingmon, scalinglevel = lookupforeveraldata(fvl, FVLMacros.FVLTypeData)
                scalingmonbst = pokedexlookupname(scalingmon, DexMacros.Total)
                bstfifth = scalingmonbst / 5
                ll += bstfifth
                breakdown.append(("Stat Scale", scalingmon, bstfifth))#"Stat Scale", mon scaling to id, ll increase
            elif (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.Mega):
                scalingmon = lookupforeveraldata(fvl, FVLMacros.FVLTypeData)[1]
                scalingmonbst = pokedexlookup(scalingmon, DexMacros.Total)
                bstfifth = scalingmonbst / 5
                ll += bstfifth
                breakdown.append(("Transformation", scalingmon, bstfifth))#"Transformation", mon transforming into id, ll increase
            elif (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.FormSwap):
                maxbst = 0
                bestmon = 25.2
                for mon in lookupforeveraldata(fvl, FVLMacros.FVLTypeData):
                    thisbst = pokedexlookup(mon, DexMacros.Total)
                    if (thisbst > maxbst):
                        maxbst = thisbst
                        bestmon = mon
                bstfifth = maxbst / 5
                ll += bstfifth
                breakdown.append(("Transformation", bestmon, bstfifth))#"Transformation", mon transforming into id, ll increase
            else:
                ll += 30
                breakdown.append((fvl, pokedexlookupname(GetForeveralMonname(fvl, True), DexMacros.Id), 30))#fvl name, dummy value, ll increase
        return (math.floor(ll), breakdown)

    def GetTypeEssentiarum(element):
        typedex = {
            "Grass": "g",
            "Fire": "r",
            "Water": "w",
            "Electric": "l",
            "Fighting": "f",
            "Psychic": "p",
            "Dark": "d",
            "Steel": "m",
            "Dragon": "n",
            "Fairy": "y",
            "Normal": "c",
            "Flying": "v",
            "Poison": "o",
            "Ground": "a",
            "Rock": "k",
            "Bug": "b",
            "Ghost": "h",
            "Ice": "i"
        }
        fontcolor = GetTypeColor(element)
        return "{font=fonts/icons.ttf}Z{color=" + fontcolor + "}" + typedex[element] + "{/color}{/font}"

    def PokeRound(num):
        if (num%1) == 0.5:
            num = num - 0.5
        return round(num, 0)

    def AddEvent(char, event):
        if (char not in CurrentPersondex().keys()):
            CurrentPersondex()[char] = copy.deepcopy(defaultpersondex[char])
        if ("Events" not in CurrentPersondex()[char].keys()):
            CurrentPersondex()[char]["Events"] = []
        if (event not in CurrentPersondex()[char]["Events"]):
            CurrentPersondex()[char]["Events"].append(event)

    def HasEvent(char, event):
        if (char not in CurrentPersondex().keys()):
            CurrentPersondex()[char] = copy.deepcopy(defaultpersondex[char])
        if ("Events" not in CurrentPersondex()[char].keys()):
            CurrentPersondex()[char]["Events"] = []
        return event in CurrentPersondex()[char]["Events"]

    def RemoveEvent(char, event):
        if (char not in CurrentPersondex().keys()):
            CurrentPersondex()[char] = copy.deepcopy(defaultpersondex[char])
        if ("Events" not in CurrentPersondex()[char].keys()):
            CurrentPersondex()[char]["Events"] = []
        if (event in CurrentPersondex()[char]["Events"]):
            CurrentPersondex()[char]["Events"].remove(event)

    def SortBySize(studentslist):
        sizedict = {}
        for student in studentslist:
            if (student in ["Wally", "Tia", "Whitney", "Erika"]):#tiny
                sizedict[student] = 3
            elif (student in ["Blue", "Flannery"]):#big
                sizedict[student] = 15
            elif (student in ["Raihan"]):#OH LAWD HE RAIHAN
                sizedict[student] = 20
            elif (student in ["Klara", "Jasmine"]):#tall girls
                sizedict[student] = 7
            elif (student in ["May"]):#this would be Brendan, hey-o!
                sizedict[student] = 8#she's small, but her hair is delightfully puffy
            elif (persondex[student]["Sex"] == Genders.Male):#large
                sizedict[student] = 10
            else:
                sizedict[student] = 5#small

        return sorted(sizedict.keys(), key=lambda x: sizedict[x], reverse=True)

    def ValidCharacterNum(mode = "social", targettype = None):
        valid_chars = 0
        for char in persondex:
            person = persondex[char]
            pointvalue = person["Value"]
            if (mode == "social" and person["Named"] and (pointvalue != 0 or GetMood(char) != 0)):
                valid_chars += 1
            elif (mode == "phone" and ((targettype == None or (targettype != None and char in GetStudents(targettype))) and person["Contact"])):
                valid_chars += 1
        return valid_chars

    def FriendshipValues(mon, evomon):
        evomon = Pokemon(evomon)
        numtypes = len(evomon.GetTypes(raw=True))
        value = 0
        typestring = ""
        for i, element in enumerate(evomon.GetTypes(raw=True)):
            typestring += element
            if (i == 0 and numtypes == 2):
                typestring += " and "
            for char in GetStudents(element, ignoreabsences=True):
                valueaddition = GetValue(char) * 2 / numtypes
                if (char == "Cheren"):
                    valueaddition = -valueaddition
                value += valueaddition
        target = pokedexlookup(evomon.GetId(), DexMacros.Total) + 150
        if (value >= target):
            return (True, "{} reacts strongly to the bell!".format(mon.GetNickname()))
        else:
            return (False, "{} seems to ignore the bell... perhaps you should spend more time with {} specialists. ({}%%)".format(mon.GetNickname(), typestring, str(FormatNum(value / target * 100))[:5]))

    def EthanNameFilter(originalstring):
        if (playercharacter == "Ethan" or not ethanmisname):
            return originalstring
        misnames = {
            "Leaf": "Loaf",
            "Silver" : "Bronze",
            "Brawly" : "Broly",
            "Roxanne" : "Roxie",
            "Falkner" : "Walkner",
            "Calem" : "Calamari",
            "Hilbert" : "Hillenbrand",
            "Brendan" : "Brentham",
            "May " : "April ",
            "Flannery" : "Mannerly",
            "Whitney" : "Whittaker",
            "Sabrina" : "Samantha",
            "Serena" : "Serene",
            "Cheren" : "Chowder",
            "Misty" : "Foggy",
            "Bianca" : "Bel",
            "Dawn" : "Daybreak",
            "Nate" : "Nathaniel",
            "Bea " : "Beef ",
            "Hilda" : "Hildaleth",
            "Gardenia" : "Greenhousia",
            "Skyla" : "Eartha",
            "Brock" : "Brotatoes",
            "Erika" : "Lindbeck",
            "Janine" : "Janny",
            "Tia" : "Tea",
            "Sonia" : "Sonny",
            "Jasmine" : "Jazzercise",
            "Grusha" : "Gru", 
            "Lenora" : "Nora",
            "Blaine" : "Blame",
            "Ramos" : "Gramps",
            "Surge" : "Jolt",
            "Melony" : "Honeydew",
            "Marshal" : "Weeaboo",
            "Koga" : "Ninja",
            "Bertha" : "Kitt",
            "Burgh" : "Buggy",
            "Olivia" : "Big O",
            "Fantina" : "Antasma",
            "Karen" : "Janice",
            "Clair" : "Clear",
            "Byron" : "Ron",
            "Valerie" : "Valor",
            "Winona" : "Windy",
            "Bruno" : "Borat",
            "Drayden" : "Draymond",
            "Wally" : "Walmart",
            "Miriam" : "Mary-Ann",
            "Raihan" : "Rhyhorn",
            "Eri" : "Erina",#this'll probably cause some sort of problem with Erika later on... fuck it.
            "Anabel" : "Annie",#are you okay?
            "Mallow" : "Marsh"
        }
        for name, replacement in misnames.items():
            originalstring = originalstring.replace(name, replacement) 
        return originalstring

    def extract_last_word_with_no_spaces(input_string):
        # Remove trailing spaces
        input_string = input_string.rstrip()
        
        # Split the string by spaces
        words = input_string.split()
        
        # Iterate from the end to find the last word with no spaces
        for word in reversed(words):
            if ' ' not in word:
                return word
        
        # If no word with no spaces is found, return an empty string
        return ''

    def NateNameFilter(originalstring):
        if (not natenicknaming):
            return originalstring
        setnames = { }
        if (IsAfter(24, 4, 2004)):
            setnames["Leaf"] = "LG"
            setnames["Ethan"] = "MC²"
        if (IsAfter(5, 5, 2004)):
            setnames["Bea"] = "Bea"
        for name in persondex.keys():
            shortenedname = extract_last_word_with_no_spaces(name)
            if (shortenedname not in setnames.keys() and shortenedname not in ["Will", "May", "Nate"]):
                originalstring = originalstring.replace(shortenedname, shortenedname[0])
        for name, replacement in setnames.items():
            originalstring = originalstring.replace(name, replacement)
        return originalstring

    def count_non_brace_chars(text):
        # Pattern to find text within curly braces
        pattern = re.compile(r'{[^{}]*}')
        
        # Remove all text within curly braces
        text_without_braces = pattern.sub('', text)
        
        # Count the number of characters in the remaining text
        non_brace_char_count = len(text_without_braces)
        
        return non_brace_char_count

    def RelationshipRankUp(character, newrelationship, newrank = 0):
        character = character.title()
        renpy.transition(dis)
        renpy.hide(GetCharacterSprite(character))
        renpy.pause(1.0)
        formertitle = GetRelationship(character)
        persondex[character]["Relationship"] = newrelationship
        persondex[character]["RelationshipRank"] = (newrank if newrank > 0 else GetRelationshipRank(character) + 1)
        PlaySound("sav.ogg")
        renpy.say(None, "¡Tu corazón cambia al sentir que tu relación con {} evoluciona de '{{color=#0048ff}}{}{{/color}}' a '{{color=#0048ff}}{}{{/color}}'!".format(character, formertitle, newrelationship))

    def DisplayPokemon(pokemonname):
        global sidemonnum
        monnum = pokedexlookupname(pokemonname, DexMacros.Id)
        sidemonnum = monnum
        PlaySound("Pokemon/ball sound.ogg")
        PlaySound("pokemon/cries/{}.mp3".format(monnum))
        renpy.show("sideportraitfull", [pokeball, dormdesk])

    def HidePokemon():
        PlaySound("pokemon/ball sound.ogg")
        renpy.show("sideportraitfull", [backinpokeball])

    def GetNextInvestmentThreshold():
        global highestbank
        for inv in investmentthresholds:
            if (inv > highestbank and bank >= inv):
                highestbank = inv
        return highestbank

    def GetNextInvestmentPrize():
        for cost, item in marketitems.items():
            purchaseprice, itemid = item
            description = GetItemEntry(itemid)[ItemdexMacros.Description]
            if (investment < cost):
                return (cost, purchaseprice, itemid, description)
    
    def CalculateFling(mon):
        item = mon.GetItem()
        if item == None or ItemHasTag(item, ("type gem", "megastone", "pov switch", "unflingable")) or ItemHasCategory(item, "Poké Balls"):
            return 0
        elif ItemHasTag(item, ("berry", "choice item", "terrain seeds")) or item in [Item.AirBalloon, Item.FairyFeather, Item.FocusSash, Item.Leftovers, Item.MuscleBand, Item.ReaperCloth, Item.SilkScarf, Item.SilverPowder, Item.SmoothRock, Item.SoftSand, Item.SootheBell]:
            return 10
        elif item in [Item.IcyRock]:
            return 40
        elif item in [Item.DubiousDisc, Item.SharpBeak]:
            return 50
        elif item in [Item.DampRock, Item.HeatRock, Item.MachoBrace, Item.RockyHelmet, Item.TerrainExtender]:
            return 60
        elif item in [Item.DragonFang, Item.PoisonBarb]:
            return 70
        elif item in [Item.AssaultVest, Item.ChippedPot, Item.CrackedPot, Item.Electirizer, Item.HeavyDutyBoots, Item.Magmarizer, Item.MasterpieceTeacup, Item.OddKeystone, Item.OvalStone, Item.Protector, Item.RazorClaw, Item.Sachet, Item.SafetyGoggles, Item.StickyBarb, Item.UnremarkableTeacup, Item.WhippedDream]:
            return 80
        elif ItemHasTag(item, "plate") or item in [Item.DeepSeaTooth, Item.ThickClub]:
            return 90
        elif ItemHasTag(item, "fossil") or item in [Item.HardStone]:
            return 100
        elif item in [Item.IronBall]:
            return 130
        else:
            return 30

    def IsEarlier():
        return IsMorning() or IsMidday()

    def IsLater():
        return IsEvening() or IsNight()

    def IsMorning():
        return timeOfDay in ["Early Morning", "Morning"]

    def IsMidday():
        return timeOfDay in ["Noon", "Afternoon"]

    def IsEvening():
        return timeOfDay in ["Evening"]

    def IsNight():
        return timeOfDay in ["Night", "Late Night", "Midnight"]

    def HasPokemon(variablestring):
        return variablestring in globals() and globals()[variablestring] in (AllPokemon())

    def AllPokemon():
        return (playerparty if playercharacter == None else (oldparty if 'oldparty' in globals() else [])) + box

    def IsWeekend():
        return getRWDay(0) in ["Saturday", "Sunday"]

    def IsWeekday():
        return not IsWeekend()

    def LastHangout(char):
        if (char in HangOutsThisWeek):
            return HangOutsThisWeek[char]
        return datetime.datetime(1, 1, 1)

    def LastHangoutWasToday(char):
        return LastHangout(char).day == calDate.day

define mooddict = {
    -10: { TrainerNature.Distant: (-5,0), TrainerNature.Moody: (-5,1), TrainerNature.Neutral: (-5,1), TrainerNature.Friendly: (-5,0), TrainerNature.Devoted: (0,2)},
    -9: { TrainerNature.Distant: (-3,1), TrainerNature.Moody: (-3,1), TrainerNature.Neutral: (-3,1), TrainerNature.Friendly: (-5,0), TrainerNature.Devoted: (0,2)},
    -8: { TrainerNature.Distant: (-3,1), TrainerNature.Moody: (-3,1), TrainerNature.Neutral: (-3,1), TrainerNature.Friendly: (-5,0), TrainerNature.Devoted: (0,2)},
    -7: { TrainerNature.Distant: (-3,1), TrainerNature.Moody: (-3,1), TrainerNature.Neutral: (-3,1), TrainerNature.Friendly: (-5,0), TrainerNature.Devoted: (0,2)},
    -6: { TrainerNature.Distant: (-3,1), TrainerNature.Moody: (-3,1), TrainerNature.Neutral: (-3,1), TrainerNature.Friendly: (-5,0), TrainerNature.Devoted: (0,2)},
    -5: { TrainerNature.Distant: (-3,1), TrainerNature.Moody: (-3,1), TrainerNature.Neutral: (-3,1), TrainerNature.Friendly: (-3,1), TrainerNature.Devoted: (0,2)},
    -4: { TrainerNature.Distant: (-3,1), TrainerNature.Moody: (-3,1), TrainerNature.Neutral: (-2,1), TrainerNature.Friendly: (-3,1), TrainerNature.Devoted: (0,2)},
    -3: { TrainerNature.Distant: (-3,1), TrainerNature.Moody: (-3,1), TrainerNature.Neutral: (-2,1), TrainerNature.Friendly: (-3,1), TrainerNature.Devoted: (0,2)},
    -2: { TrainerNature.Distant: (-3,1), TrainerNature.Moody: (-3,1), TrainerNature.Neutral: (-1,1), TrainerNature.Friendly: (-1,1), TrainerNature.Devoted: (0,2)},
    -1: { TrainerNature.Distant: (0,0), TrainerNature.Moody: (-3,1), TrainerNature.Neutral: (-1,1), TrainerNature.Friendly: (-1,1), TrainerNature.Devoted: (0,1)},
    0: { TrainerNature.Distant: (0,-1), TrainerNature.Moody: (0,0), TrainerNature.Neutral: (0,0), TrainerNature.Friendly: (1,0), TrainerNature.Devoted: (2,0)},
    1: { TrainerNature.Distant: (1,-1), TrainerNature.Moody: (2,-1), TrainerNature.Neutral: (1,-1), TrainerNature.Friendly: (3,-1), TrainerNature.Devoted: (3,-1)},
    2: { TrainerNature.Distant: (1,-1), TrainerNature.Moody: (2,-1), TrainerNature.Neutral: (1,-1), TrainerNature.Friendly: (3,-1), TrainerNature.Devoted: (3,-1)},
    3: { TrainerNature.Distant: (1,-1), TrainerNature.Moody: (2,-1), TrainerNature.Neutral: (2,-1), TrainerNature.Friendly: (3,-1), TrainerNature.Devoted: (3,-1)},
    4: { TrainerNature.Distant: (1,-1), TrainerNature.Moody: (2,-1), TrainerNature.Neutral: (2,-1), TrainerNature.Friendly: (3,-1), TrainerNature.Devoted: (3,-1)},
    5: { TrainerNature.Distant: (1,-2), TrainerNature.Moody: (3,-1), TrainerNature.Neutral: (3,-1), TrainerNature.Friendly: (3,-1), TrainerNature.Devoted: (3,-1)},
    6: { TrainerNature.Distant: (1,-2), TrainerNature.Moody: (3,-1), TrainerNature.Neutral: (3,-1), TrainerNature.Friendly: (3,-1), TrainerNature.Devoted: (3,-1)},
    7: { TrainerNature.Distant: (3,-2), TrainerNature.Moody: (3,-1), TrainerNature.Neutral: (3,-1), TrainerNature.Friendly: (3,-1), TrainerNature.Devoted: (3,-1)},
    8: { TrainerNature.Distant: (3,-3), TrainerNature.Moody: (3,-1), TrainerNature.Neutral: (3,-1), TrainerNature.Friendly: (3,-1), TrainerNature.Devoted: (3,-1)},
    9: { TrainerNature.Distant: (3,-3), TrainerNature.Moody: (5,-2), TrainerNature.Neutral: (3,-1), TrainerNature.Friendly: (3,-1), TrainerNature.Devoted: (3,-1)},
    10: { TrainerNature.Distant: (5,-3), TrainerNature.Moody: (5,-2), TrainerNature.Neutral: (5,-1), TrainerNature.Friendly: (5,-1), TrainerNature.Devoted: (5,-1)}
}

define liberizefirstsentence = {
    "Normal": "Everyone",
    "Fire": "The torch of revolution",
    "Water": "The primordial sea",
    "Grass": "The circle of life",
    "Electric": "A bolt from the blue",
    "Ice": "The frigid sky",
    "Fighting": "A just fist",
    "Poison": "Every option",
    "Ground": "An ancient nation",
    "Flying": "Freedom's wing",
    "Psychic": "A brilliant mind",
    "Bug": "A union of millions",
    "Rock": "The earth itself",
    "Ghost": "An ancient soul",
    "Dark": "A necessary evil",
    "Dragon": "A legendary power",
    "Steel": "Justice's blade",
    "Fairy": "The people's hope"
}

define liberizesecondsentence = {
    "Normal": "moves toward liberty!",
    "Fire": "ignites the flames of liberty!",
    "Water": "crashes down for liberty!",
    "Grass": "restores liberty!",
    "Electric": "surges towards liberty!",
    "Ice": "preserves liberty!",
    "Fighting": "fights for liberty!",
    "Poison": "removes obstacles to liberty!",
    "Ground": "unearths liberty!",
    "Flying": "soars toward liberty!",
    "Psychic": "concludes with liberty!",
    "Bug": "joins for liberty!",
    "Rock": "carves liberty into stone!",
    "Ghost": "empowers undying liberty!",
    "Dark": "fights dirty for liberty!",
    "Dragon": "roars for liberty!",
    "Steel": "gilds the banner of liberty!",
    "Fairy": "wishes for liberty!"
}

define nonvolatiles = ["burned", "frozen", "paralyzed", "poisoned", "badly poisoned", "asleep", "busted disguise", "frenzied", "mega evolved", "minigigamaxed", "annihilating", "transformed", "bitter", "illusion"]
define normalstatuses = ["burned", "frozen", "paralyzed", "poisoned", "badly poisoned", "asleep"]
define bluecolor = "{color=#0048ff}"
define sabrinacolor = "{color=#600080}"
define charmcolor = "{color=#b7669e}"
define patiencecolor = "{color=#e226a6}"
define witcolor = '{color=#60c2f8}'
define knowledgecolor = "{color=#66b77d}"
define couragecolor = '{color=#ff8412}'
define contestcolor = "{color=#FF69B4}"
define charmoption = charmcolor + "[Charm]" + "{/color} "
define patienceoption = patiencecolor + "[Patience]" + "{/color} "
define witoption = witcolor + "[Wit]" + "{/color} "
define knowledgeoption = knowledgecolor + "[Knowledge]" + "{/color} "
define courageoption = couragecolor + "[Courage]" + "{/color} "
define tiafont = "{font=fonts/sign.ttf}"
define ellipses = "{w=0.25}.{w=0.25}.{w=0.25}."
define movesin = ["Forest's Curse", 'Defense Curl', 'Tackle', 'Echoed Voice', 'Trick', 'Play Nice', 'Thunder Shock', 'Tail Whip', 'Play Rough', 'Copycat', 'Mega Drain', 'Bullet Seed', 'Constrict', 'Rage', 'Confusion', 'Poison Sting', 'Sharpen', 'Sandstorm', 'Absorb', 'Fake Tears', 'Wing Attack', 'Last Resort', 'Pound', 'Spite', 'Double Team', 'Minimize', 'Pursuit', 'Sticky Web', 'Wrap', 'String Shot', 'Mud Sport', 'Sand Attack', 'Razor Leaf', 'Vine Whip', 'Iron Head', 'Growth', 'Splash', 'Leaf Storm', 'Bubble', 'Supersonic', 'Peck', 'Swagger', 'Misty Terrain', 'Flail', 'Charge', 'Covet', 'Mud-Slap', 'Rock Throw', 'Sheer Cold', 'Bind', 'Taunt', 'Quick Attack', 'Harden', 'Discharge', 'Growl', 'Helping Hand', 'Hyper Voice', 'Scratch', 'Rollout', 'Icy Wind', 'Wood Hammer', 'Fairy Wind', 'Encore', 'Feint Attack', 'Astonish', 'Switcheroo', 'Fissure', 'Ember', 'Gust', 'Smog', 'Water Gun', 'Bide', 'Foresight', 'Rapid Spin', 'Bite', 'Focus Energy', 'Confuse Ray', 'Baby-Doll Eyes', 'Leer', 'Ice Shard', 'Twister', 'Miracle Eye', 'Arm Thrust', 'Incinerate', 'Psywave', 'Headbutt', 'Horn Attack', 'Powder Snow', 'Night Slash', 'Hone Claws', 'Odor Sleuth', 'Withdraw', 'Endure', 'Thunder Wave', 'Hypnosis', 'Lick', 'Poison Powder', 'Vise Grip', 'Dragon Rage', 'Draco Meteor', 'Poison Gas', 'Whirlwind', 'Roar', 'Disable', 'Vacuum Wave', 'Stun Spore', 'Counter', 'Sweet Scent', 'Night Shade', 'Seismic Toss', 'Feint', 'Fire Spin', 'Leech Seed', 'Uproar', 'Bulldoze', 'Bug Bite', 'Refresh', 'Mud Shot', 'Electro Ball', 'Mist', 'Haze', 'Poison Tail', 'Teleport', 'Protect', 'Curse', 'Metal Claw', 'Smokescreen', 'Spore', 'Sleep Powder', 'Aerial Ace', 'Stomp', 'Screech', 'Torment', 'Lucky Chant', 'Struggle Bug', 'Acid', 'Rock Smash', 'Disarming Voice', 'Leafage', 'Yawn', 'Wide Guard', 'Rest', 'Facade', 'Detect', 'Agility', 'Shadow Sneak', 'Heal Pulse', 'Light Screen', 'Reflect', 'Toxic Spikes', 'Trick-or-Treat', 'Pluck', 'Swift', 'Nuzzle', 'Flame Burst', 'Camouflage', 'Chip Away', 'Gyro Ball', 'Pin Missile', 'Magical Leaf', 'Metal Sound', 'Take Down', 'Wake-Up Slap', 'Natural Gift', 'Worry Seed', 'Ancient Power', 'Tailwind', 'Synthesis', 'Sweet Kiss', 'Fire Fang', 'Poison Fang', 'Ice Fang', 'Thunder Fang', 'Safeguard', 'Stealth Rock', 'Sand Tomb', 'Endeavor', 'Scary Face', 'Iron Defense', 'Acid Armor', 'Sing', 'Force Palm', 'Hidden Power', 'Double Slap', 'Aqua Ring', 'Assurance', 'Flame Wheel', 'Dig', 'Work Up', 'Venoshock', 'Low Kick', 'Psybeam', 'Cotton Spore', 'Slam', 'Brine', 'Glare', 'Wish', 'Grass Whistle', 'Meditate', 'Mimic', 'Slash', 'Drill Run', 'Fury Swipes', 'Fake Out', 'Attract', 'Ice Ball', 'Payback', 'Round', 'Mud Bomb', 'Draining Kiss', 'Body Slam', 'Hyper Fang', 'Smack Down', 'Water Sport', 'Ingrain', 'Silver Wind', 'Bubble Beam', 'Mean Look', 'Block', 'Fury Attack', 'Water Shuriken', 'Air Cutter', 'Charm', 'Rock Tomb', 'Spark', 'Aurora Beam', 'Will-O-Wisp', 'Breaking Swipe', 'Flower Shield', 'Double Kick', 'Toxic', 'Dragon Breath', 'Rock Slide', 'Milk Drink', 'Recover', 'Mach Punch', 'Chrysalize', 'Enshroud', 'Legacy', 'Energize', 'Ardent Gaze', 'Disabling Poke', 'Rain Dance', 'Steady Flame', 'Wing It', 'Deathless', 'Bark Up', 'Burial Ground', 'Slow Freeze', 'Simple World', 'Bad Breath', 'Clear Mind', 'Splinter Shield', 'Metallize', 'Lightning Rod', 'Magnitude', 'Acid Spray', 'Acupressure', 'Howl', 'Spikes', 'Bone Rush', 'Bonemerang', 'First Impression', 'Hex', 'Bone Club', 'Tearful Look', 'Brave Bird', 'Boomburst', 'Shock Wave', 'Ice Punch', 'Double-Edge', 'Freeze-Dry', 'Dragon Pulse', 'Air Slash', 'Grass Knot', 'Dragon Claw', 'Explosion', 'Power-Up Punch', 'Pain Split', 'Power Whip', 'Power Trip', 'Electrify', 'Dragon Tail', 'Tickle', 'Zap Cannon', 'Heat Wave', 'Poison Jab', 'Fury Cutter', 'Petal Blizzard', 'Quick Guard', 'Fly', 'Power Swap', 'Flatter', 'Embargo', 'Megahorn', 'Rock Climb', 'Magnet Bomb', 'Stored Power', 'Superpower', 'Rototiller', 'Magnetic Flux', 'Barrier', 'Weather Ball', 'Head Smash', 'Brick Break', 'Recycle', 'Healing Wish', 'Flare Blitz', 'Nasty Plot', 'Laser Focus', 'Mirror Move', 'Calm Mind', 'False Swipe', 'Teeter Dance', 'Accelerock', 'Future Sight', 'Eerie Impulse', 'Aura Sphere', 'Hail', 'Sunny Day', 'Silk Trap', 'Destiny Bond', 'Baneful Bunker', 'Sky Attack', 'Dragon Dance', 'Tri Attack', 'Sonic Boom', 'Crunch', 'Quiver Dance', 'Thunder Punch', 'Earthquake', 'Magnet Rise', 'Morning Sun', 'Moonlight', 'Moonblast', 'Roost', 'Perish Song', 'Swords Dance', 'Sucker Punch', 'Petal Dance', 'Fire Punch', 'Water Spout', 'Eruption', 'Electric Terrain', 'Sludge', 'Bulk Up', 'Grassy Terrain', 'Shift Gear', 'Pollen Puff', 'Phantom Force', 'Hammer Arm', 'Mirror Shot', 'Swallow', 'Ion Deluge', 'Spit Up', 'Aromatherapy', 'Water Pulse', 'Close Combat', 'Cross Poison', 'Venom Drench', 'Knock Off', 'Mirror Coat', 'Power Gem', 'Giga Drain', 'Amnesia', 'Mystical Fire', 'Guard Swap', 'Self-Destruct', 'Aqua Jet', 'Lunge', 'Shadow Claw', 'Ominous Wind', 'Zen Headbutt', 'Horn Drill', 'Guillotine', 'Stockpile', 'Rock Wrecker', 'Hyper Beam', 'Giga Impact', 'Blast Burn', 'Hydro Cannon', 'Frenzy Plant', 'Roar of Time', 'Bounce', 'Frustration', 'Return', 'Magic Coat', 'Dizzy Punch', 'Sludge Bomb', 'Me First', 'Rage Powder', 'Synchronoise', 'Triple Kick', 'Power Trick', 'Memento', 'Substitute', 'Leaf Tornado', 'Mind Reader', 'Bullet Punch', 'Dark Pulse', 'Retaliate', 'Shell Smash', 'Dive', 'Steel Wing', 'U-turn', 'Razor Shell', 'Noble Roar', 'Clear Smog', 'Extreme Speed', 'Reversal', 'Ice Beam', 'Belly Drum', 'Psychic', 'Follow Me', 'Whirlpool', 'Bestow', 'High Jump Kick', 'Soft-Boiled', 'Secret Power', 'Psych Up', 'Razor Wind', 'Spike Cannon', 'Captivate', 'Charge Beam', 'Coil', 'Entrainment', 'Solar Beam', 'Shadow Ball', 'Metronome', 'Comet Punch', 'Iron Tail', 'Skill Swap', 'Psyshock', 'Psystrike', 'Mega Kick', 'Hyper Drill', 'Gastro Acid', 'Autotomize', 'Defog', 'Imprison', 'Fell Stinger', 'Zing Zap', 'Focus Punch', 'Fiery Dance', 'Dynamic Punch', 'Beat Up', 'Acrobatics', 'Heart Stamp', 'Thrash', 'Dazzling Gleam', 'Anchor Shot', 'After You', 'Flame Charge', 'Super Fang', 'Bug Buzz', 'Lava Plume', 'Earth Power', 'Rolling Kick', 'Baton Pass', 'Shed Tail', 'Snatch', 'Jump Kick', 'Belch', 'Flash Cannon', 'Assist', 'Lovely Kiss', 'Revenge', 'Cotton Guard', 'Signal Beam', 'Leech Life', 'Rock Blast', 'Punishment', 'Fling', 'X-Scissor', 'Snore', 'Avalanche', 'Thief', 'Throat Chop', 'Hurricane', 'Darkest Lariat', 'U-turn', 'Lock-On', 'Electroweb', 'Crush Claw', 'Octazooka', 'Outrage', 'Skull Bash', 'Aqua Cutter', 'Feather Dance', 'Needle Arm', 'Spiky Shield', 'Stone Edge', 'Spider Web', 'Aqua Tail', 'Clamp', 'Rock Polish', 'Gunk Shot', 'Dual Chop', 'Sludge Wave', 'Double Hit', 'Wring Out', 'Infestation', 'Twineedle', 'Branch Poke', 'No Retreat', 'Scale Shot', 'Headlong Rush', 'Spirit Break', 'Flip Turn', 'Liberage', 'Stomping Tantrum', 'Psycho Cut', 'Drill Peck', 'Sleep Talk', 'Foul Play', 'Cross Chop', 'Gravity', 'Grudge', 'Shadow Punch', 'Obstruct', 'Hydro Pump', 'Aurora Veil', 'Icicle Crash', 'Parting Shot', 'Slack Off', 'Extrasensory', 'Leaf Blade', 'Fillet Away', 'Flamethrower', 'Cosmic Power', 'Energy Ball', 'Submission', 'Muddy Water', 'Dream Eater', 'Floral Healing', 'Inferno', 'Low Sweep', 'Ally Switch', 'Shore Up', 'Snarl', 'Circle Throw', 'Karate Chop', 'Role Play', 'Fire Blast', 'Blizzard', 'Mega Punch', 'Frost Breath', 'Psychic Fangs', 'Salt Cure', 'Heavy Slam', 'Heat Crash', 'Stone Cold Stunner', 'Life Dew', 'Horn Leech', 'Final Gambit', 'Heal Block', 'Dragon Rush', 'Rage Fist', 'Wild Charge', 'Psycho Shift', 'Sky Uppercut', 'Vital Throw', 'Smelling Salts', 'Spirit Shackle', 'Surf', 'Thunderbolt', 'Crabhammer', 'Seed Bomb', 'Snowscape', 'Guard Split', 'Metal Burst', 'Egg Bomb', 'Fire Lash', 'Steamroller', 'Quash', 'Icicle Spear', 'Overdrive', 'Present', 'Freeze-Dry', 'Overheat', 'Ice Hammer', 'Skitter Smack', 'Psycho Boost', 'Fleur Cannon', 'V-create', 'Make It Rain', 'Spin Out', 'Clanging Scales', 'Dragon Ascent', 'Floaty Fall', 'Zippy Zap', 'Magic Room', 'Blaze Kick', 'Soft-Boiled', 'Attack Order', 'Thunder', 'Trick-Or-Treat', 'Wonder Room', 'Simple Beam', 'Power Split', 'Mind Blown', 'Burn Up', 'Dual Wingbeat', 'Liquidation', 'Volt Switch', 'Strength Sap', 'Defend Order', 'Wake-Up Slap', 'Spotlight', 'Waterfall', 'Heal Order', 'Soak', 'Splishy Splash']
define abilitiesin = ['Stall', 'Trace', 'Shell Armor', 'Chlorophyll', 'Steelworker', 'Hustle', 'Keen Eye', 'Plus', 'Healer', 'Merciless', 'Sweet Veil', 'Rock Head', 'Iron Fist', 'Overgrow', 'Tinted Lens', 'Shield Dust', 'Volt Absorb', 'Disguise', 'Magic Guard', 'Weak Armor', 'White Smoke', 'Synchronize', 'Overcoat', 'Own Tempo', 'Prankster', 'Sheer Force', 'Contrary', 'Iron Barbs', 'Telepathy', 'Blaze', 'Serene Grace', 'Run Away', 'Pickup', 'Steadfast', 'Levitate', 'Mold Breaker', 'Shed Skin', 'Shields Down', 'Strong Jaw', 'Reckless', 'Illuminate', 'Intimidate', 'Regenerator', 'Sap Sipper', 'Hyper Cutter', 'Guts', 'Solar Power', 'Flash Fire', 'Swarm', 'Damp', 'Cloud Nine', 'Leaf Guard', 'Limber', 'Rattled', 'Wonder Skin', 'Anger Point', 'Harvest', 'Ice Body', 'Compound Eyes', 'Insomnia', 'Arena Trap', 'Defeatist', 'Gluttony', 'Klutz', 'Vital Spirit', 'Flame Body', 'Super Luck', 'Water Absorb', 'Sand Force', 'Honey Gather', 'Moody', 'Unaware', 'Infiltrator', 'Heavy Metal', 'Sturdy', 'Thick Fat', 'Oblivious', 'Berserk', 'Flower Veil', 'Torrent', 'Inner Focus', 'Symbiosis', 'Sand Rush', 'Sand Veil', 'Moxie', 'Static', 'Schooling', 'Sniper', 'Aftermath', 'Clear Body', 'Speed Boost', 'Technician', 'Frisk', 'Simple', 'Rivalry', 'Early Bird', 'Anticipation', 'Lightning Rod', 'Natural Cure', 'Poison Point', 'Pure Power', 'Cheek Pouch', 'Adaptability', 'Triage', 'Huge Power', 'Quick Feet', 'Ball Fetch', 'Scrappy', 'Gale Wings', 'Toxic Debris', 'Defiant', 'Magic Bounce', 'Tough Claws', 'Cute Charm', 'Soundproof', 'Slow Start', 'Big Pecks', 'Pixilate', 'No Guard', 'Wimp Out', 'Power of Alchemy', 'Sand Stream', 'Emergency Exit', 'Forecast', 'Sticky Hold', 'Cursed Body', 'Vital spirit', 'Stakeout', 'Unnerve', 'Filter', 'Stench', 'Pressure', 'Justified', 'Hydration', 'Poison Touch', 'Magnet Pull', 'Wonder Guard', 'Competitive', 'Scrappy', 'Battle Armor', 'Solid Rock', 'Zen Mode', 'Snow Cloak', 'Analytic', 'Drizzle', 'Drought', 'Snow Warning', 'Minus', 'Shadow Tag', 'Swift Swim', 'Dry Skin', 'Punk Rock', 'Unburden', 'Water Veil', 'Forewarn', 'Friend Guard', 'Suction Cups', 'Pickpocket', 'Skill Link', 'Storm Drain', 'Rough Skin', 'Sharpness', 'Prism Armor', 'Parental Bond', 'Fluffy', 'Tangled Feet', 'Immunity', 'Gorilla Tactics', 'Screen Cleaner', 'Purifying Salt', 'Hospitality', 'Thermal Exchange', 'Long Reach', 'Effect Spore', 'Bad Dreams', 'Mimicry', 'Quick Draw', 'Curious Medicine', 'Supreme Overlord', 'Flare Boost', 'Corrosion', 'Ice Scales', 'Slush Rush', 'Galvanize', 'Color Change', 'Tetra Element', 'Protean', 'Libero']

define nightmatrix = BrightnessMatrix(-0.2) * ContrastMatrix(1.3)

default persondex = copy.deepcopy(defaultpersondex)

default classstats = {
    "Normal" : 0,
    "Fire" : 0,
    "Water" : 0,
    "Grass" : 0,
    "Electric" : 0,
    "Ice" : 0,
    "Fighting" : 0,
    "Poison" : 0,
    "Ground" : 0,
    "Flying" : 0,
    "Psychic" : 0,
    "Bug" : 0,
    "Rock" : 0,
    "Ghost" : 0,
    "Dark" : 0,
    "Dragon" : 0,
    "Steel" : 0,
    "Fairy" : 0
}

default personalstats = {
    "Charm" : 0,
    "Knowledge" : 0,
    "Courage" : 0,
    "Wit" : 0,
    "Patience" : 0
}

default battlehistory = { }
default losttestbattles = []

default council_campaigning = False
default leafwindowjump = False
default lastclass = ""
default chosenindex = -247
default starter_id = 0
default starter_name = ""
default playerparty = []
default pkmnlocked = -1
default profanity = False
default money = 0
default sidemonnum = 0
default sidemonnum2 = 0
default sidemonnum3 = 0
default inventory = { }
default location = ""
default mustswitch = False
default hidebattleui = False
default randcount = 0
#the list that all Pokemon in the PC are kept in
default box = []
default freelectricphases = []
default boughtitems = 1
default pikachudenial = 0
default testbattle = False
default persistent.testwarning = False
default excusesecondelective = False
default excusesecondhomeroom = False
default punkwins = 0
#hide the sideportraits
default hideside = False
#hide all sideportraits except red
default showredonly = False
# keeps track of the amount of money you've invested
default investment = 0
# keeps track of the amount of money your investment has returned
default gains = 0
default patiencefix = False
default starterobj = None
default invpage = "Medicines"
default invoverwrite = None
default activemon = None
default activerepel = None
default activetreat = None
default repelstepsleft = 0
default freeroaming = False
default usinginventory = False
#variables for sorting pc boxes
default currentbox = 0
default currentsort = None
default reversesort = True
#variables for sorting social screen
default socialsort = None
#turned on at start of battle, turned off at end
default inbattle = False
#turns true when you defeat/catch Cramorant
default seaportunlocked = False
#turns true the first time you challenge Cramorant
default seencramorant = False
#counts the number of conscutive battles you've had in the wild area
default wildcount = 0
default highestwildcount = 0
# triggers if you've just passed a battle exam in an elective
default passedclass = False
# used to display item messages
default ItemText = ""
default itemDialogText = ""
#used to keep track of who you've given gifts to. Resets weekly on Monday
default GiftsGiven = []
#used to keep track of who you've hung out with this week. Resets weekly on Monday
default HangOutsThisWeek = {}
#keeps track of if you've ever performed a critical capture
default CritCaptures = 0
#keeps track of the move you're teaching for overriding the "switch" menu
default taughtmove = None
#keeps track of who you're playing as for gimmick days. None = "Red"
default playercharacter = None
#keeps track of the eggs you took and hatched. Also counts the Happiny.
default eggshatched = []
#keeps track of when the random seed was created
default randseedtime = time.localtime()
#blue's nickname, after you start calling him Blue
default oldblue_name = "Blueberry"
#activated once Ethan teaches you about moods
default usingmoods = False
#keeps track of the button text for the tera button
default terabuttontext = "Terastallize"
#used to keep track of which moves have been avoided in the first Dawn fight
default movesdodged = []
#keeps track of which dialog has already been shown in a battle with cutscenes
default dialogshown = []
#allows the usage of fractions for dramatic effect in dawn fight
default allowfractions = False
#keeps track of the button text for the liberize button 
default libbuttontext = "Liberize"
#keeps track of which types you're Liberized into
default libtypes = []
#true if it's the first dawn battle
default dawnbattle = False
#keeps track of the max number of types you can liberize into (2 in first Dawn battle)
default libtypesnum = 1
#keeps track of when you're allowed to use Foreverals
default usingforeverals = False
#the foreveral inventory
default foreveralinv = []
default claimedforeverals = []
#keeps track of how we're sorting the foreveral inventory page
default foreveralsort = None
default foreveralsortinverse = False
default foreveralpage = 0
default examinedf = None
#keeps track of if I'm currently explaining how a foreveral works
default explainingf = False
#mystery gift variables to prevent exploitation
default soldmysterygift = False
default giftedmysterygift = False
#saw wallyellow scene
default sawwallyellow = False
#walkthroughwalls for squad battles
default wtw = False
#variables to tell if you rescued the psychics
default rescuedwill = False
default rescuedsabrina = False
default rescuedtia = False
#a dictionary of npc teams
default npcteams = {}
#variables used to determine if a battle was hard/easy
default tookdamage = False
default pokemonfainted = False
default switchedmon = False
#variables used to keep track of how much power Pikachu currently has
default liberationlimit = 0
default maxliberationlimit = 200
default usingliberationlimit = False
default foreveralinvsubmenu = "Foreverals"
#variable used to keep track of what nate calls you
default nate_name = "Bud"
#variable used to keep track of when you're not in the real world
default isgame = False
#to see if you got the end that comes from punching Cheren
default persistent.cherenpunchend = False
#gimmighoul coins
default gimmighoulcount = 0
#disposable array that does not require cleanup
default seencutscenes = []
#wally nickname
default wally_name = "Senpai"
#flintlock ui variables
default pkmnswapitem = -1
default partyviewer = True
default pkmnlockedmove = -1
#remove characters from GetStudents for the short term
default removestudents = set()
#remove characters from GetStudents specifically for lunch
default removelunchstudents = set()
#scholarships gained
default scholarshipslist = []
#badges gained
default badgeslist = []
#nessa outfit swap
default nessaoutfitswap = False
#freeroam but for texting
default texting = False
#triggered if the player just did a normal text at night, for use in scenes after
default texted = True
#prevents th dungeon "controls" option from stacking
default indungeontutorial = False
#disables inventory/foreverals
default disableinventory = False
#swap style
default newdatabase = False
#determines if the soothe bell has been rung
default bellrung = False
#variables for club credit
default cookingcredit = 0
#variable for if you're automatically quoting characters
default autoquote = True
#variable to keep track of current dungeon
default activedungeon = None
#variable to keep track of dungeon progress
default dungeonprog = True
#variable to keep track of who's leading the party in squads
default squadleader = None
#variable to keep track of one person who isn't leading the party in squads
default randname = None
#variable to keep track of last string that was converted and displayed in dungeons
default lastdungeontext = ""
#disables nate name filter
default natenicknaming = True
#keeps track of genpokemon.
default genpokemon = None
#keeps track of the level of uifuckery
default uifuckery = 0
#variable used to keep track of what melody calls you
default melody_name = "first_name"
#used to keep track of your class and skills in dungeons
default dungeonclass = ""
default dungeonskills = ["Resilience", "Leadership", "Persuasion"]
#a dictionary used to keep track of custom events
default customdungeonevents = dict()
#keeping track of if you're still 'technically' in a dungeon
default technicaldungeon = False
#keeps track of your dungeon history and scores
default dungeonhistory = []
#keeps track of your coordination knowledge
default coordinatingknowledge = 0
#keeps track of outcomes to options in dungeon functions
default outcomedex = {}
#keeps track of if you have finished an event in the fungeon system
default afterevent = False
#keeps track of moves being boosted by foreverals
default moveboosts = []
#override sidemon's name, if necessary
default sidemonoverride = None
#keep track of if you're a coordinator
default coordinating = False
#keeps track of if lowspecs mode is on or not
default lowspecs = False
#keeps track of if you've beaten the grunts this week
default beatgrunts = False
#passes the sceneviewer variable to a loaded file
default persistent.sceneviewer = False
#keeps track of if the game is being run via the sceneviewer
default sceneviewer = False
#keeps track of the amount of money is Gardenia's bank
default bank = 0
#keeps track of highest amount of money invested in Gardenia's bank
default highestbank = 0
#a variable to override the moods at the end of quasi-generic class scenes
default classmood = 10
#variables used to keep track of what your contest moves will be
default contestspecial = None
default contestaction = None#"Perform" or "Switch"
default contestmove = None
default contestmon = None
#variable used to keep track of if you're in a contest
default InContest = False
#variable used to keep track of if you're looking at move info
default previewingmoves = False
#variable used to turn off Ethan name filter
default ethanmisname = True
#variable used to make showredonly actually work
default lastsi = Null()
#variable used to make treatboost and escape rope validation nicer
default inwildarea = False
#variable used to keep track of, uh, pika loadouts
default pika_loadouts = {}

define type_translation = {
    "Normal": "Normal",
    "Fire": "Fuego",
    "Water": "Agua",
    "Electric": "Eléctrico",
    "Grass": "Planta",
    "Ice": "Hielo",
    "Fighting": "Lucha",
    "Poison": "Veneno",
    "Ground": "Tierra",
    "Flying": "Volador",
    "Psychic": "Psíquico",
    "Bug": "Bicho",
    "Rock": "Roca",
    "Ghost": "Fantasma",
    "Dragon": "Dragón",
    "Dark": "Siniestro",
    "Steel": "Acero",
    "Fairy": "Hada",
    "???": "???"
}

define nature_translation = {
    "Special": "Especial",
    "Devoted": "Devota",
    "Neutral": "Neutral",
    "Distant": "Distante",
    "Friendly": "Amistosa",
    "Moody": "Errática"
}

define relationship_translate = {
    "Student": "Estudiante",
    "Rival": "Rival",
    "Classmate": "Compañero/a de clases",
    "Underclassman": "Graduado",
    "Friend": "Amigo/a",
    "Dormmate": "Compañero/a de cuarto",
    "Political Rival": "Rival político",
    "Training Partner": "Compañera de entrenamiento",
    "Date": "Cita",
    "Tool": "Herramienta",
    "Protector": "Protector",
    "Grasshopper": "Pequeño saltamontes",
    "Mentor": "Mentor/a",
    "Mentee": "Aprendiz",
    "Patient": "Paciente",
    "Liability": "Lastre",
    "None": "Ninguna",
    "Benefactee": "Benefactor",
    "Crush": "Atraído",
    "Citizen": "Ciudadano",
    "Acquaintance": "Conocido",
    "Planner": "Planificador",
    "Weakness": "Debilidad",
    "Shoulder": "Hombro",
    "Listener": "Oyente",
    "Anathema": "Maldecida.",
    "Muse": "Musa",
    "Rival": "Rival",
    "Thief": "Ladrón",
    "Hope": "Esperanza",
    "Challenger": "Retador",
    "Terrible Influence": "Mala influencia",
    "Honey": "Calabacita",
    "Light": "Luz",
    "Finisher": "Continuador",
    "Caretaker": "Niñera",
    "Farmboy": "Chico de campo",
    "Good Boy": "Buen chico",
    "Battler": "Combatiente",
    "Supporter": "Soporte",
    "Shield": "Escudo",
    "Rejector": "Rechazada",
    "L'Amour": "Enamorado",
    "Investigator": "Investigador",
    "Bestie": "Mejor amigui",
    "Bestie & Date": "Mejor amigui y cita",
    "Taster": "Catador",
    "Jerk": "Idiota",
    "Pal": "Bro",
    "Blade": "Espada",
    "Good Friend": "Buen amigo",
    "Mate": "Colega",
    "Fanboy": "Fanático",
    "Bodyguard": "Guardaespaldas",
    "Extra": "Extra",
    "...?": "¿...?",
    "Friend Again": "Amigos nuevamente",
    "Conspirator": "Conspirador",
    "Chance": "Nueva oportunidad",
    "Wingman": "Escolta",
    "Junior": "Menor",
    "{font=fonts/sign.ttf}Trainer{/font}": "{font=fonts/sign.ttf}Entrenador{/font}",
    "Trainer": "Entrenador",
    "HUMAN": "HUMANA",
    "Project": "Proyecto",
    "Relationship Counselor":"Consejero de relaciones",
    "Teammate": "Compañero de equipo"

}

define ability_translation = {
    "Stall": "Rezagado",
    "Trace": "Rastro",
    "Shell Armor": "Caparazón",
    "Chlorophyll": "Clorofila",
    "Steelworker": "Acero Templado",
    "Hustle": "Entusiasmo",
    "Keen Eye": "Vista Lince",
    "Plus": "Más",
    "Healer": "Almasana",
    "Merciless": "Ensañamiento",
    "Sweet Veil": "Velo Dulce",
    "Rock Head": "Cabeza Roca",
    "Iron Fist": "Puño Férreo",
    "Overgrow": "Espesura",
    "Tinted Lens": "Cromolente",
    "Shield Dust": "Polvo Escudo",
    "Volt Absorb": "Absorbe Electricidad",
    "Disguise": "Disfraz",
    "Magic Guard": "Muro Mágico",
    "Weak Armor": "Armadura Frágil",
    "White Smoke": "Humo Blanco",
    "Synchronize": "Sincronía",
    "Overcoat": "Funda",
    "Own Tempo": "Ritmo Propio",
    "Prankster": "Bromista",
    "Sheer Force": "Fuerza Bruta",
    "Contrary": "Respondón",
    "Iron Barbs": "Punta Acero",
    "Telepathy": "Telepatía",
    "Telepahty": "Telepatía",
    "Blaze": "Mar Llamas",
    "Serene Grace": "Dicha",
    "Run Away": "Fuga",
    "Pickup": "Recogida",
    "Steadfast": "Impasible",
    "Levitate": "Levitación",
    "Mold Breaker": "Rompemoldes",
    "Shed Skin": "Mudar",
    "Shields Down": "Escudo Limitado",
    "Strong Jaw": "Mandíbula Fuerte",
    "Reckless": "Audaz",
    "Illuminate": "Iluminación",
    "Intimidate": "Intimidación",
    "Regenerator": "Regeneración",
    "Sap Sipper": "Herbívoro",
    "Hyper Cutter": "Corte Fuerte",
    "Guts": "Agallas",
    "Solar Power": "Poder Solar",
    "Flash Fire": "Absorbe Fuego",
    "Swarm": "Enjambre",
    "Damp": "Humedad",
    "Cloud Nine": "Aclimatación",
    "Leaf Guard": "Defensa Hoja",
    "Limber": "Flexibilidad",
    "Rattled": "Nerviosismo",
    "Wonder Skin": "Piel Milagro",
    "Anger Point": "Ira",
    "Harvest": "Cosecha",
    "Ice Body": "Cuerpo Gélido",
    "Compound Eyes": "Ojo Compuesto",
    "Insomnia": "Insomnio",
    "Arena Trap": "Trampa Arena",
    "Defeatist": "Flaqueza",
    "Gluttony": "Gula",
    "Klutz": "Zoquete",
    "Vital Spirit": "Espíritu Vital",
    "Flame Body": "Cuerpo Llama",
    "Super Luck": "Afortunado",
    "Water Absorb": "Absorbe Agua",
    "Sand Force": "Poder Arena",
    "Honey Gather": "Recogemiel",
    "Moody": "Veleta",
    "Unaware": "Ignorante",
    "Infiltrator": "Allanamiento",
    "Heavy Metal": "Metal Pesado",
    "Sturdy": "Robustez",
    "Thick Fat": "Sebo",
    "Oblivious": "Despiste",
    "Berserk": "Cólera",
    "Flower Veil": "Velo Flor",
    "Torrent": "Torrente",
    "Inner Focus": "Foco Interno",
    "Symbiosis": "Simbiosis",
    "Sand Rush": "Ímpetu Arena",
    "Sand Veil": "Velo Arena",
    "Moxie": "Autoestima",
    "Static": "Electricidad Estática",
    "Schooling": "Banco",
    "Sniper": "Francotirador",
    "Aftermath": "Resquicio",
    "Clear Body": "Cuerpo Puro",
    "Speed Boost": "Impulso",
    "Technician": "Experto",
    "Frisk": "Cacheo",
    "Simple": "Simple",
    "Rivalry": "Rivalidad",
    "Early Bird": "Madrugar",
    "Anticipation": "Anticipación",
    "Lightning Rod": "Pararrayos",
    "Natural Cure": "Cura Natural",
    "Poison Point": "Punto Tóxico",
    "Pure Power": "Energía Pura",
    "Cheek Pouch": "Carrillo",
    "Adaptability": "Adaptable",
    "Triage": "Primer Auxilio",
    "Huge Power": "Potencia",
    "Quick Feet": "Pies Rápidos",
    "Ball Fetch": "Recogebolas",
    "Scrappy": "Intrépido",
    "Gale Wings": "Alas Vendaval",
    "Toxic Debris": "Restos Tóxicos",
    "Defiant": "Competitivo",
    "Magic Bounce": "Espejo Mágico",
    "Tough Claws": "Garra Dura",
    "Cute Charm": "Gran Encanto",
    "Soundproof": "Insonorizar",
    "Slow Start": "Inicio Lento",
    "Big Pecks": "Sacapecho",
    "Pixilate": "Piel Feérica",
    "No Guard": "Indefenso",
    "Wimp Out": "Huida",
    "Power of Alchemy": "Reactivo",
    "Sand Stream": "Chorro Arena",
    "Emergency Exit": "Retirada",
    "Forecast": "Predicción",
    "Sticky Hold": "Viscosidad",
    "Cursed Body": "Cuerpo Maldito",
    "Stakeout": "Vigilante",
    "Unnerve": "Nerviosismo",
    "Filter": "Filtro",
    "Stench": "Hedor",
    "Pressure": "Presión",
    "Justified": "Justiciero",
    "Hydration": "Hidratación",
    "Poison Touch": "Toque Tóxico",
    "Magnet Pull": "Imán",
    "Wonder Guard": "Superguarda",
    "Competitive": "Tenacidad",
    "Battle Armor": "Armadura Batalla",
    "Solid Rock": "Roca Sólida",
    "Zen Mode": "Modo Daruma",
    "Snow Cloak": "Manto Níveo",
    "Analytic": "Cálculo Final",
    "Drizzle": "Llovizna",
    "Drought": "Sequía",
    "Snow Warning": "Nevada",
    "Minus": "Menos",
    "Shadow Tag": "Sombra Trampa",
    "Swift Swim": "Nado Rápido",
    "Dry Skin": "Piel Seca",
    "Punk Rock": "Punk Rock",
    "Unburden": "Liviano",
    "Water Veil": "Velo Agua",
    "Forewarn": "Alerta",
    "Friend Guard": "Amigo Guardián",
    "Suction Cups": "Ventosas",
    "Pickpocket": "Carroñero",
    "Skill Link": "Encadenado",
    "Storm Drain": "Colector",
    "Rough Skin": "Piel Tosca",
    "Sharpness": "Filo",
    "Prism Armor": "Armadura Prisma",
    "Parental Bond": "Amor Filial",
    "Fluffy": "Pelaje Recio",
    "Tangled Feet": "Tumbos",
    "Immunity": "Inmunidad",
    "Gorilla Tactics": "Táctica G",
    "Screen Cleaner": "Limpiador",
    "Purifying Salt": "Sal Purificadora",
    "Hospitality": "Hospitalidad",
    "Thermal Exchange": "Intercambio Térmico",
    "Long Reach": "Remoto",
    "Effect Spore": "Efecto Espora",
    "Bad Dreams": "Mal Sueño",
    "Mimicry": "Mimetismo",
    "Quick Draw": "Desenfreno",
    "Curious Medicine": "Curandero",
    "Supreme Overlord": "Soberanía",
    "Flare Boost": "Ímpetu Ardiente",
    "Corrosion": "Corrosión",
    "Ice Scales": "Escamas de Hielo",
    "Slush Rush": "Quitanieves",
    "Galvanize": "Electrogénesis",
    "Color Change": "Cambio Color",
    "Tetra Element": "Tetraelemento",
    "Protean": "Mutatipo",
    "Rain Dish": "Cura Lluvia",
    "Surge Surfer": "Cola Surf",
    "Tangling Hair": "Rizos Rebeldes",
    "Fur Coat": "Pelaje Recio",
    "Liquid Ooze": "Viscosecreción",
    "Neutralizing Gas": "Gas Reactivo",
    "Aerilate": "Piel Celeste",
    "Imposter": "Impostor",
    "Download": "Descarga",
    "Marvel Scale": "Escama Especial",
    "Multiscale": "Multiescamas",
    "Light Metal": "Metal Liviano",
    "Magma Armor": "Escudo Magma",
    "Poison Heal": "Antídoto",
    "Truant": "Pereza",
    "Normalize": "Normalidad",
    "Toxic Boost": "Ímpetu Tóxico",
    "Flower Gift": "Don Floral",
    "Heatproof": "Ignífugo",
    "Motor Drive": "Electromotor",
    "Mummy": "Momia",
    "Illusion": "Ilusión",
    "Bulletproof": "Antibalas",
    "Magician": "Prestidigitador",
    "Grass Pelt": "Manto Frondoso",
    "Stance Change": "Cambio Táctico",
    "Aroma Veil": "Velo Aroma",
    "Mega Launcher": "Megadisparador",
    "Refrigerate": "Piel Helada",
    "Gooey": "Baba",
    "Liquid Voice": "Voz Fluida",
    "Battery": "Batería",
    "Dancer": "Pareja de Baile",
    "Stamina": "Firmeza",
    "Water Bubble": "Pompa",
    "Queenly Majesty": "Regia Presencia",
    "Receiver": "Receptor",
    "Water Compaction": "Hidrorrefuerzo",
    "Innards Out": "Revés",
    "Comatose": "Letargo Perenne",
    "Dazzling": "Cuerpo Vívido",
    "Grassy Surge": "Herbogénesis",
    "Steam Engine": "Combustible",
    "Ripen": "Maduración",
    "Gulp Missile": "Tragamisil",
    "Psychic Surge": "Psicogénesis",
    "Well-Baked Body": "Cuerpo Horneado",
    "Guard Dog": "Perro Guardián",
    "Libero": "Líbero"
}