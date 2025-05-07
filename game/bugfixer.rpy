label after_load:
python:
    renpy.music.stop("ctc")
    renpy.music.stop("altcry")
    renpy.music.stop("XYgame")
    renpy.music.stop("crowd")
    renpy.music.stop("crowd2")
    renpy.music.stop("crowd3")
    renpy.music.stop("points")
    renpy.music.stop("misc")
    changemade = False

    if ("calDate" not in globals()):
        calDate = datetime.datetime(2004, 4, 2)
        print("creating new calDate")
        changemade = True

    if ("persondex" not in globals()):
        changemade = True
        print("rebuilding persondex")
        persondex = copy.deepcopy(defaultpersondex)

    for keyname in defaultpersondex.keys():
        if (keyname in CurrentPersondex().keys()):
            for key in defaultpersondex[keyname]:
                if (key not in CurrentPersondex()[keyname].keys()):
                    print("adding {} to persondex for {}".format(key, keyname))
                    CurrentPersondex()[keyname][key] = copy.deepcopy(defaultpersondex[keyname][key])
                    changemade = True
            if ("ClassesKnown" in CurrentPersondex()[keyname].keys()):
                print("removing classesknown for " + keyname)
                if (keyname in classtaught.keys()):
                    for classtype in CurrentPersondex()[keyname]["ClassesKnown"]:
                        AddEvent(keyname, classtype) 
                del CurrentPersondex()[keyname]["ClassesKnown"]
                changemade = True
        else:
            print("adding " + keyname + " to persondex")
            CurrentPersondex()[keyname] = copy.deepcopy(defaultpersondex[keyname])
            changemade = True

    if ("battlehistory" in globals() and not WonBattle("BrendanMay2") and "mayhaslarvesta" in globals() and not mayhaslarvesta):
        print("fixing brendan/may discontinuity")
        changemade = True
        mayhaslarvesta = True

    if ('taughtmove' in globals() and taughtmove != None):
        print("disabling taughtmove")
        taughtmove = None
        changemade = True

    if ('activeitem' in globals()):
        print("deleting activeitem")
        del(activeitem)
        changemade = True

    if ("Instructeur Fantina" in persondex.keys()):
        print("deleting Instructeur Fantina")
        del CurrentPersondex()["Instructeur Fantina"]
        changemade = True

    if ("Kris" in CurrentPersondex().keys()):
        print("deleting Kris")
        del CurrentPersondex()["Kris"]
        changemade = True

    if (playercharacter == None and CurrentPersondex()["Yellow"]["Value"] != len(claimedforeverals)):
        print("resetting yellow foreverals value")
        CurrentPersondex()["Yellow"]["Value"] = len(claimedforeverals)
        changemade = True

    if (randseedtime == None):
        print("setting randseedtime")
        randseedtime = time.localtime()
        changemade = True

    if ("Togedemaru Everal" in claimedforeverals):
        print("setting togedemaru everal to foreveral")
        claimedforeverals.remove("Togedemaru Everal")
        claimedforeverals.append("Togedemaru Foreveral")
        changemade = True
        
    if ("gymbattles" in globals() and len(battlehistory) < len(gymbattles)):
        print("setting gymbattles to battlehistory")
        for key, value in gymbattles.items():
            battlehistory[key] = value
            changemade = True
        gymbattles = []

    if (CurrentPersondex()["Brawly"]["Mood"] != 0 or CurrentPersondex()["Brawly"]["Value"] != 0 or CurrentPersondex()["Brawly"]["Nature"] != TrainerNature.Special):
        print("setting brawly to nothing")
        AddEvent("Brawly", "Covered")
        CurrentPersondex()["Brawly"]["Nature"] = TrainerNature.Special
        CurrentPersondex()["Brawly"]["Mood"] = 0
        CurrentPersondex()["Brawly"]["Value"] = 0
        changemade = True

    if (CurrentPersondex()["Falkner"]["Mood"] != 0 or CurrentPersondex()["Falkner"]["Value"] != 0 or CurrentPersondex()["Falkner"]["Nature"] != TrainerNature.Special):
        print("setting Falkner to nothing")
        CurrentPersondex()["Falkner"]["Nature"] = TrainerNature.Special
        CurrentPersondex()["Falkner"]["Mood"] = 0
        CurrentPersondex()["Falkner"]["Value"] = 0
        changemade = True

    if (CurrentPersondex()["Roxanne"]["Mood"] != 0 or CurrentPersondex()["Roxanne"]["Value"] != 0 or CurrentPersondex()["Roxanne"]["Nature"] != TrainerNature.Special):
        print("setting Roxanne to nothing")
        CurrentPersondex()["Roxanne"]["Nature"] = TrainerNature.Special
        CurrentPersondex()["Roxanne"]["Mood"] = 0
        CurrentPersondex()["Roxanne"]["Value"] = 0
        changemade = True

    if (CurrentPersondex()["Erika"]["Relationship"] == "Friend" and IsAfter(1, 5, 2004)):
        print("erika's Relationship resetting")
        CurrentPersondex()["Erika"]["Relationship"] = "Teammate"
        changemade = True

    if (CurrentPersondex()["Hilbert"]["Relationship"] == "Dormmate" and IsAfter(1, 5, 2004)):
        print("hilbert's Relationship resetting")
        CurrentPersondex()["Hilbert"]["Relationship"] = "Teammate"
        changemade = True

    if ("starter_id" in globals() and "starterobj" in globals() and starterobj != None and starter_id != starterobj.Id):
        print("updating starter_id")
        starter_id = starterobj.Id
        changemade = True

    if ("starter_name" in globals() and "starterobj" in globals() and starterobj != None and starter_name != starterobj.GetNickname()):
        print("updating starter_name")
        starter_name = starterobj.GetNickname()
        changemade = True

    if ("starter_species_name" in globals() and "starterobj" in globals() and starterobj != None and starter_species_name != pokedexlookup(starterobj.Id, DexMacros.Name)):
        print("updating starter_species_name")
        starter_species_name = pokedexlookup(starterobj.Id, DexMacros.Name)
        changemade = True

    if ("whitneyhashappiny" in globals() and whitneyhashappiny and not HasEvent("Whitney", "HasHappiny")):
        AddEvent("Whitney", "HasHappiny")
        print("Added event to replace whitneyhashappiny")
        del whitneyhashappiny
        changemade = True

    if ("nessahasbonsly" in globals() and nessahasbonsly and not HasEvent("Nessa", "HasBonsly") and not HasEvent("Hilda", "HasBonsly")):
        AddEvent("Nessa", "HasBonsly")
        print("Added event to replace nessahasbonsly")
        del nessahasbonsly
        changemade = True
    elif ("nessahasbonsly" in globals() and not nessahasbonsly and not HasEvent("Nessa", "HasBonsly") and not HasEvent("Hilda", "HasBonsly")):
        AddEvent("Hilda", "HasBonsly")
        print("Added event to replace not nessahasbonsly")
        del nessahasbonsly
        changemade = True

    if ('hildahasbonsly' in globals()):
        del hildahasbonsly
        print("deleting hildahasbonsly var")
        changemade = True

    if ("autoquote" not in globals()):
        autoquote = True
        changemade = True
        print("Added autoquote")

    if (GetRelationship("Hilbert") == "Finisher" and GetRelationshipRank("Hilbert") == 1):
        print("Adjusting hilbert rank")
        changemade = True
        persondex["Hilbert"]["RelationshipRank"] = 2

    if (SecureShareAndEggAmount()):
        print("secure share and egg amount triggered")
        changemade = True

    if (not HasLocation("Faculty Pool") and GetRelationshipRank("Blue") > 0 and IsAfter(22, 5, 2004)):
        RecordKnownLocations("Blue", "Faculty Pool")
        print("Adding Blue as the first person you went to the faculty pool with")
        changemade = True

    if (GetRelationshipRank("Nessa") > 0 and not HasEvent("Nessa", "AdjustDateABase") and not HasEvent("Nessa", "DenyDate")):
        RecordKnownLocations("Nessa", "Meteor Hole")
        RecordDate("Nessa")
        AddEvent("Nessa", "AdjustDateABase")
        print("Adding Nessa to DateABase")
        changemade = True

    if ("janinedomming" in globals() and janinedomming and not HasEvent("Janine", "Domming") and not HasEvent("Janine", "RemovedDomming")):
        print("add janinedommingevent to replace variable")
        AddEvent("Janine", "Domming")
        changemade = True

    if ("losttestbattles" in globals() and losttestbattles == { }):
        print("replacing losttestbattles with list")
        losttestbattles = []
        changemade = True

    if (HasEvent("Rosa", "GiveToLeaf")):
        changemade = True
        print("removing rosa give pikachu to leaf")
        RemoveEvent("Rosa", "GiveToLeaf")

    if (HasEvent("Rosa", "GiveToSabrina")):
        changemade = True
        print("removing rosa give pikachu to sabrina")
        RemoveEvent("Rosa", "GiveToSabrina")

    if (HasEvent("Rosa", "ClassSwap")):
        changemade = True
        print("removing rosa swap classes")
        RemoveEvent("Rosa", "ClassSwap")

    if (IsAfter(18, 5, 2004) and not HasEvent("Nate", "ClassSwap")):
        changemade = True
        print("making nate swap classes")
        AddEvent("Nate", "ClassSwap")

    if (IsAfter(21, 5, 2004) and HasEvent("Yellow", "LostHat")):
        changemade = True
        RemoveEvent("Yellow", "LostHat")
        print("removing yellow losthatevent")

    if (activedungeon != None and not hasattr(activedungeon, 'Party')):
        activedungeon = None
        print("removing old-style activedungeon")
        changemade = True

    if ('starter_species_name' in globals() and not isinstance(starter_species_name, str)):
        starter_species_name = pokedexlookup(starter_id, DexMacros.Name)
        print("fixing species name error")
        changemade = True

    if ("Red" in persondex.keys()):
        if ("Events" in persondex["Red"].keys()):
            if ("SawGlitch" in persondex["Red"]["Events"]):
                AddEvent("Instructor Blaine", "SawGlitch")
                print("replaced red sawglitch for instructor blaine sawglitch")
            if ("Coordinator" in persondex["Red"]["Events"]):
                coordinating = True
                print("replaced red coordinatorevent for coordinating variable")
        del persondex["Red"]
        print("deleting red in persondex")
        changemade = True

    if (IsAfter(9, 4, 2004) and not HasEvent("Ethan", "Serendipity5")):
        AddEvent("Ethan", "Serendipity1")
        AddEvent("Ethan", "Serendipity2")
        AddEvent("Ethan", "Serendipity3")
        AddEvent("Ethan", "Serendipity4")
        AddEvent("Ethan", "Serendipity5")
        print("Added catch-up ethan serendipity events")
        changemade = True
    
    if ('movestatuses' in globals() and len(movestatuses) < 15):
        movestatuses = {
            "ice ball": ["Ice Ball"],
            "rollout": ["Rollout"],
            "thrashing": ["Thrash"],
            "uproaring": ["Uproar"],
            "outraged": ["Outrage"],
            "dug in": ["Dig"],
            "diving": ["Dive"],
            "airborne": ["Fly", "Bounce"],
            "ethereal": ["Phantom Force"],
            "cloaked in light": ["Sky Attack"],
            "charging light": ["Solar Beam"],
            "hardheaded": ["Skull Bash"],
            "whipping up winds": ["Razor Wind"],
            "petal dancing": ["Petal Dance"],
            "biding": ["Bide"]
        }
        changemade = True
        print("updating move statuses")

    removefvls = []
    for fvl in claimedforeverals:
        if (fvl not in GetAllForeveralNames()):
            removefvls.append(fvl)
    for fvl in removefvls:
        claimedforeverals.remove(fvl)
        print("removing " + fvl + " from claimedlist")
        if (fvl in foreveralinv):
            foreveralinv.remove(fvl)
            print("removing " + fvl + " from foreveralinv")
        for mon in AllPokemon():
            if (fvl in mon.GetForeverals()):
                mon.GetForeverals().remove(fvl)
                print("removing " + fvl + " from being equipped to " + mon.GetNickname())

        changemade = True

    if ("technicaldungeon" in globals() and technicaldungeon):
        technicaldungeon = False
        changemade = True
        print("turning off technicaldungeon")

    if (HasEvent("Bea", "NightScene") and not HasEvent("Bea", "Bea2Part2")):
        AddEvent("Bea", "Bea2Part2")
        RemoveEvent("Bea", "NightScene")
        print("replacing bea nightscene event with bea2part2")
        changemade = True

    if (GetRelationshipRank("Jasmine") > 1 and not HasEvent("Jasmine", "Jasmine2Part2")):
        AddEvent("Jasmine", "Jasmine2Part2")
        print("Added Jasmine2Part2")
        changemade = True

    if (GetRelationshipRank("Grusha") > 0 and not HasEvent("Grusha", "Grusha1Part2")):
        AddEvent("Grusha", "Grusha1Part2")
        print("Added Grusha1Part2")
        changemade = True

    if (GetRelationshipRank("Tia") > 1 and not HasEvent("Tia", "Tia2Part2")):
        AddEvent("Tia", "Tia2Part2")
        print("Added Tia2Part2")
        changemade = True

    if (GetRelationshipRank("Misty") > 1 and not HasEvent("Misty", "Misty2Part2")):
        AddEvent("Misty", "Misty2Part2")
        print("Added Misty2Part2")
        changemade = True

    if (invpage == "Healing"):
        invpage = "Medicines"
        print("healing invpage -> medicines")
        changemade = True

    if ("Nessa" in persondex.keys() and "RelationshipRank" in persondex["Nessa"].keys() and isinstance(persondex["Nessa"]["RelationshipRank"], str)):
        persondex["Nessa"]["RelationshipRank"] = 0
        persondex["Nessa"]["Relationship"] = "Classmate"
        print("setting nessa relationshiprank to a number")
        changemade = True

    if (GetTrainerTeam("Ethan", "Pichu", False) != None and GetTrainerTeam("Ethan", "Pichu", False).Id == 172):
        print("updating Ethan's Pichu")
        GetTrainerTeam("Ethan", "Pichu", False).Id = 172.1
        changemade = True

    if (IsAfter(26, 5, 2004) and not HasLocation("Cafe")):
        print("adding cafe to dateabase")
        RecordKnownLocations("Leaf", "Cafe")
        changemade = True

    if (playercharacter == None and rescuedtia and rescuedsabrina and rescuedwill and not HasEvent("Nurse Miriam", "KnowsName")):
        print("adding miriam knowsname event")
        AddEvent("Nurse Miriam", "KnowsName")
        changemade = True

    if ((rescuedtia or rescuedsabrina or rescuedwill) and not persondex["Nurse Miriam"]["Named"]):
        print("Making sure you know Miriam's name")
        BecomeNamed("Nurse Miriam")
        changemade = True        
    
    if ("Pink Bow" in CurrentInventory()):
        CurrentInventory()["Fairy Feather"] = CurrentInventory()["Pink Bow"]
        del CurrentInventory()["Pink Bow"]
        print("replacing inventory Pink Bow with Fairy feather")
        changemade = True

    if (GetTrainerTeam("Tia", "Mime Jr.", False).Id == 122.1 and GetTrainerTeam("Tia", "Mime Jr.", False).Ability != "Vital Spirit"):
        GetTrainerTeam("Tia", "Mime Jr.", False).Ability = "Vital Spirit"
        print("Fixing the ability of Tia's Mr. Mime")
        changemade = True

    if (not HasEvent("Brendan", "CaughtSandshrew") and not HasEvent("Brendan", "NotCaughtSandshrew") and IsAfter(10, 4, 2004)):
        AddEvent("Brendan", "CaughtSandshrew")
        print("added event to indicate brendan caught shrew")
        changemade = True

    if (not HasEvent("Tia", "HasWynaut") and not HasEvent("Tia", "NotHasWynaut") and IsAfter(24, 4, 2004)):
        AddEvent("Tia", ("HasWynaut" if "tiahaswynaut" in globals() and tiahaswynaut else "NotHasWynaut"))
        print("added event to indicate tia got wynaut")
        changemade = True

    if (not HasEvent("Nate", "HasToxel") and not HasEvent("Nate", "NotHasToxel") and IsAfter(24, 4, 2004)):
        AddEvent("Nate", ("HasToxel" if "natehastoxel" in globals() and natehastoxel else "NotHasToxel"))
        print("added event to indicate nate (temporarily) got toxel")
        changemade = True

    if (not HasEvent("Flannery", "HasMagby") and not HasEvent("Flannery", "NotHasMagby") and IsAfter(24, 4, 2004)):
        AddEvent("Flannery", ("HasMagby" if "flanneryhasmagby" in globals() and flanneryhasmagby else "NotHasMagby"))
        print("added event to indicate flannery got magby")
        changemade = True

    if (HasEvent("Klara", "AcceptCoordinatorClub") and not HasEvent("Professor Oak", "LearnedAboutContestColiseum")):
        AddEvent("Professor Oak", "LearnedAboutContestColiseum")
        print("added thing to indicate you've learned about the Contest Coliseum from the first time that Klara invites you")
        changemade = True

    if any(isinstance(item, str) for item in CurrentInventory().keys()): # inventory conversion
        stringinventory = copy.deepcopy(CurrentInventory())
        AssignCurrentInventory({})
        for itemname in stringinventory.keys():
            itemid = GetItemEntryFromName(itemname)[0]
            print("Converting inventory item {} to ID {}".format(itemname, itemid))
            if (itemid != -1):
                CurrentInventory()[itemid] = stringinventory[itemname]
            changemade = True

    for mon in AllPokemon(): # pokémon items conversion
        if isinstance(mon.GetItem(), str):
            itemid = GetItemEntryFromName(mon.GetItem())[ItemdexMacros.Id]
            print("Converting Pokémon item {}, held by {}, to ID {}".format(mon.GetItem(), mon.GetNickname(), itemid))
            if (itemid != -1):
                mon.Item = itemid
            changemade = True

        if (len(mon.Moves) > 4):
            print("shortening movelist for 'mon " + mon.GetNickname())
            mon.Moves = mon.Moves[:4]
            changemade = True

        preevs = copy.deepcopy(mon.EVs)
        mon.EVs = adjust_digits(mon.EVs)
        if (preevs != mon.EVs):
            print("sorting overflowing EVs")
            changemade = True
    
    for name, team in npcteams.items():
        for mon in team.values():
            if isinstance(mon.Item, str):
                itemid = GetItemEntryFromName(mon.Item)[ItemdexMacros.Id]
                print("Converting {}'s {}'s {} to ID {}".format(name, mon.GetNickname(), mon.Item, itemid))
                mon.Item = itemid
                changemade = True

            if (name == "Tia"):
                if (mon.GetLevel() > AimLevel() + 10):
                    print("downgrading the level of Tia's {} from {} to 1".format(mon.GetNickname(), mon.GetLevel()))
                    mon.UpdateLevel(1, False, True, False)
                    changemade = True

    if (not HasEvent("Professor Oak", "CelebiWing1")):
        AddEvent("Professor Oak", "CelebiWing1")
        CurrentInventory()[Item.CelebiWing] = 1
        print("Adding celebi wing")
        changemade = True

    if (money + investment + bank >= 200000 and IsBefore(1, 6, 2004)):#FIX THIS: Remove this eventually
        changemade = True
        print("normalizing money amounts")
        money = math.floor(money / 10.0)
        bank = math.floor(bank / 10.0)
        investment = min(investment, money)
        changemade = True

    performedbankreplacement = False
    if (not HasEvent("Gardenia", "BankReplacement") and highestbank == 0 and investment != 0):
        performedbankreplacement = True
        newmoney = math.ceil(investment / 5)
        money += newmoney
        investment -= newmoney
        AddEvent("Gardenia", "BankReplacement")
        print("Performing the gardenia bank replacement")
        changemade = True

    if ("melody_name" in globals() and melody_name in [None, "first_name"]):
        melody_name = first_name
        print("making sure melody won't call you 'None'")
        changemade = True

    if ('pika_loadouts' not in globals()):
        pika_loadouts = {}
        print("if pika loadouts is nothing, set it")
        changemade = True

    if (not HasEvent("Leaf", "LentDratini") and IsAfter(4, 5, 2004)):
        AddEvent("Leaf", "LentDratini")
        print("adding lentdratini event to leaf")
        changemade = True

    if (changemade):
        renpy.block_rollback()

    pkmnlocked = -1
    randcount = randcount % 1000000

    if (performedbankreplacement):
        renpy.say(None, "The economy of Kobukan has been rebalanced. [newmoney] of your investment with Gardenia has been returned. The rest is invested in Gardenia's market, which is separate from the mechanic of the bank. [bluecolor]Talk with her for more details.{/color}")
        renpy.block_rollback()

    if (dungeonclass == "" and IsAfter(10, 5, 2004)):
        renpy.block_rollback()
        renpy.call("dungeonclassbugfix")
        renpy.block_rollback()

if persistent.sceneviewer:
    call sceneviewerafterload from after_load_sceneviewer
    $ MainMenu(confirm=False)()

return

label errorlabel:
    "Apologies. It appears this save file is {color=#f00}corrupted.{/color}"
    "You can continue playing on it, but certain errors may occur--item duplication, unavoidable crashes, etc."
    "Alternatively, you can utilize a bugfix feature."
    "This bugfix should have little to no visual impact on the game, though it may grant you extra points in a class."
    "This bugfix is my personal recommendation."
    "The safest, third, option is to start a new game over, but I understand you may not have the time or inclination to do so."
    "Again, please accept my apologies for this inconvenience."

    pause 1.0

    "What would you like to do?"

    menu:
        "Continue playing.":
            pass

        "Try the bugfix.":
            "Understood. Please be aware certain aspects of the game, such as time of day or date, may not line up, though these errors should fix themselves after going to bed."
            python:
                classtype = GetStatRank(0)
                timeOfDay = "Bugfix"
                while (renpy.call_stack_depth() > 1):
                    renpy.pop_call()

        "Start a new game.":
            $ MainMenu(confirm=False)()

    return

label dungeonclassbugfix:
    $ _rollback = False
    $ renpy.block_rollback()

    "It appears this save file is loading data from before the dungeon re-work. In the new system, you are required to select a 'class', which comes with corresponding abilities based on your traits."
    "Your options are Warlock, Fighter, Paladin, Ranger, Berserker, and, unfortunately, Bard."

label dungeonclassbugfixoptions:

menu:
    "Tell me more about Warlocks.":
        "Warlocks' special skills are [knowledgecolor]Lore Smarts{/color}, [witcolor]Cunning{/color}, and [patiencecolor]Learning.{/color}"
        "They're best for players with a lot of [knowledgecolor]Knowledge{/color}, [witcolor]Wit{/color}, and [patiencecolor]Patience.{/color}"

        $ charactertype = "Warlock"
        $ characterskills = ["Lore Smarts", "Cunning", "Learning"]

    "Tell me more about Fighters.":
        "Their special skills are [couragecolor]Physicality{/color}, [knowledgecolor]World Smarts{/color}, and [witcolor]Strategy.{/color}"
        "They're best for players with a lot of [couragecolor]Courage{/color}, [knowledgecolor]Knowledge{/color}, and [witcolor]Wit.{/color}"

        $ charactertype = "Fighter"
        $ characterskills = ["Physicality", "World Smarts", "Strategy"]

    "Tell me more about Paladins.":
        "Their special skills are [couragecolor]Resilience{/color}, [patiencecolor]Leadership{/color}, and [charmcolor]Persuasion.{/color}"
        "They're best for players with a lot of [couragecolor]Courage{/color}, [patiencecolor]Patience{/color}, and [charmcolor]Charm.{/color}"

        $ charactertype = "Paladin"
        $ characterskills = ["Resilience", "Leadership", "Persuasion"]

    "Tell me more about Rangers.":
        "Their special skills are [charmcolor]Pokémon Handling{/color}, [patiencecolor]Healing{/color}, and [knowledgecolor]Pokémon Smarts.{/color}"
        "They're best for players with a lot of [charmcolor]Charm{/color}, [patiencecolor]Patience{/color}, and [knowledgecolor]Knowledge.{/color}"

        $ charactertype = "Ranger"
        $ characterskills = ["Pokémon Handling", "Healing", "Pokémon Smarts"]

    "Tell me more about Berserkers.":
        "Their special skills are [couragecolor]Risk-Taking{/color}, [witcolor]Adaptability{/color}, and [charmcolor]Pokémon Handling.{/color}"
        "They're best for players with a lot of [couragecolor]Courage{/color}, [witcolor]Wit{/color}, and [charmcolor]Charm.{/color}"

        $ charactertype = "Berserker"
        $ characterskills = ["Risk-Taking", "Adaptability", "Pokémon Handling"]

    "Tell me more about Bards.":
        "They are only good at [charmcolor]Deception.{/color} You cannot convincingly play one. Selecting this option will make the game slightly harder."
        
        $ charactertype = "Bard"
        $ characterskills = ["Deception", "Deception", "Deception"]

menu:
    "I want to be a [charactertype].":
        $ dungeonclass = charactertype
        $ dungeonskills = characterskills

        "It is done."

        $ _rollback = True
        $ renpy.block_rollback()

    "Let me hear about other options.":
        jump dungeonclassbugfixoptions

return

label notfoundlabel:
    "{color=#f00}Note:{/color} This save appears to have an error. Attempting a bugfix routine now."
    
    python:
        classtype = GetStatRank(0)
        timeOfDay = "Bugfix"
        while (renpy.call_stack_depth() > 1):
            renpy.pop_call()
        
        jumptoyear = "01"
        jumptomonth = ("0" if calDate.month < 10 else "") + str(calDate.month)
        jumptodate = ("0" if calDate.day < 10 else "") + str(calDate.day)
        labelname = jumpto + jumptoyear + jumptomonth + jumptodate
        if (timeOfDay == "Bugfix"):
            renpy.jump("day" + jumptoyear + jumptomonth + jumptodate)
        elif (renpy.has_label(labelname)):
            renpy.jump(labelname)
        else:
            renpy.jump("day" + jumptoyear + jumptomonth + jumptodate)

init python:#eventually, you're going to want to delete these old variables in the store
    class Mob:
        pass

    class Floor:
        pass

    class SpecialTile:
        pass

    class MapTile:
        pass

    def rescuescenes():
        pass

    def tutorialscenes():
        pass

    def tutorialscenes2():
        pass

    def adjust_digits(digits):
        # Step 1: Set any digit greater than 252 to 252
        digits = [min(digit, 252) for digit in digits]
        
        # Step 2: Sum the digits
        total = sum(digits)
        
        # Step 3: If the total is greater than 510, reduce random digits
        while total > 510:
            # Find indices of digits that are greater than 0
            non_zero_indices = [i for i, digit in enumerate(digits) if digit > 0]
            
            # Randomly select one of these indices
            if non_zero_indices:
                random_index = random.choice(non_zero_indices)
                # Reduce the selected digit by 1
                digits[random_index] -= 1
                # Recalculate the total
                total = sum(digits)
        
        return digits
