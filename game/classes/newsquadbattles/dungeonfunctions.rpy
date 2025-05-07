#auto-defined party variables
#lastdungeontext = the unconverted string that was converted and displayed last
#activedungeon = the current dungeon. Dungeon class object
#squadleader = the "active" squad member. Trainer class object
#squadleadermon = a random unfainted pokemon from the squad leader
#randsquad = a squadder who is not the leader
#fullsquad = list of Trainer class objects. all active squad members
#dungeonlevel = the aim level of the dungeon Can wobble up or down two, without offsets
#wildpool = a list of floats. all pokemon that can appear in the dungeon
#genpokemon = a float. the generated pokemon for the encounter. 
#genpokemons = a list of floats 5 long. genpokemon is the first element
#ugenpokemons = a list of floats 5 long. Tries very hard not to repeat species. genpokemon is the first element

#variablename - defaultvalue - description

#--variables that can be set in an eventdict--:
#ExcludeActors - a list of party members who cannot perform this event. Can be either objects or names.
#ExcludeFunction - if this function returns False, then this event cannot be run.
#IntroText - an introductory narration played before the scene label is called, if there is one to call
#PostText - a post narration played after an option is chosen, and the result occurs
#RegenCritera - when this event is begun, runs through the lambda function in this and sets genpokemon to the highest returner

#--variables that *must* be set in an eventdict--:
#options - [] - a list of option classes

#--variables that can be set in an Option--:
#excludeactors - [] - a list of party members who cannot perform this event. Can be either objects or names.
#excludefunction - (lambda: return True) - A tuple with a failure message and a function. if this function returns False, then this event cannot be run. Failure message can be None, in which case the option won't be shown
#successfunction = (lambda: DungeonProg(1))
#threshold - 10 - The amount you need to roll to pass

#--variables that *must* be set in an Option--:
#name - "Option Name" - what to put on the option button

#string replacements for DisplayDungeonText
#&0 = squad leader's name
#&e = leader's pronouns (he/she)
#&E = leader's pronouns (He/She)
#&im = leader's pronouns (him/her)
#&is = leader's pronouns (his/hers)
#&fp = leader's flying pokemon's nickname
#&rb = leader's rock breaker pokemon nickname
#&sp = leader's strong pokemon nickname
#&rc = leader's rock climbing pokemon nickname
#&rcsp = leader's rock climbing or strong pokemon nickname
#&df = leader's defogger pokemon nickname
#&0m = squadleadermon's name
#&* = any squad member that is not the leader
#&*e = the he/she pronoun for randsquad
#&*is = the his/her pronoun for randsquad
#&*im = the him/her pronoun for randsquad
#&1 = squad member 1's name
#&2 = squad member 2's name
#&3 = squad member 3's name
#&4 = squad member 4's name
#&5 = squad member 5's name
#&l = location's name
#&p = generated Pokémon name for the encounter

init python:
    def GetSquadLeaderRandomPokemon():
        return RandomChoice(squadleader.GetUnfaintedTeam())

    def DisplayDungeonText(originaltext):
        global lastdungeontext
        global genpokemon
        lastdungeontext = originaltext
        leadername = squadleader.GetFormatName()
        if (squadleader.Name == "red"):
            leadersex = Genders.Male
        else:
            leadersex = persondex[leadername]["Sex"]
        randsquadname = randsquad.GetFormatName()
        if (randsquad.Name == "red"):
            randsquadsex = Genders.Male
        else:
            randsquadsex = persondex[randsquadname]["Sex"]

        squadleadermon = squadleader.GetTeam()[0]
        originaltext = originaltext.replace("&0m", squadleadermon.GetNickname())
        originaltext = originaltext.replace("&0", leadername)
        originaltext = originaltext.replace("&e", "he" if leadersex == Genders.Male else "she")
        originaltext = originaltext.replace("&E", "He" if leadersex == Genders.Male else "She")
        originaltext = originaltext.replace("&im", "him" if leadersex == Genders.Male else "her")
        originaltext = originaltext.replace("&is", "his" if leadersex == Genders.Male else "her")        
        originaltext = originaltext.replace("&*im", "him" if randsquadsex == Genders.Male else "her")
        originaltext = originaltext.replace("&*is", "his" if randsquadsex == Genders.Male else "her")
        originaltext = originaltext.replace("&*e", "he" if randsquadsex == Genders.Male else "she")
        originaltext = originaltext.replace("&*", randsquadname)
        originaltext = originaltext.replace("&1", fullsquad[0].GetFormatName())
        if (len(fullsquad) > 1):
            originaltext = originaltext.replace("&2", fullsquad[1].GetFormatName())
            if (len(fullsquad) > 2):
                originaltext = originaltext.replace("&3", fullsquad[2].GetFormatName())
                if (len(fullsquad) > 3):
                    originaltext = originaltext.replace("&4", fullsquad[3].GetFormatName())
                    if (len(fullsquad) > 4):
                        originaltext = originaltext.replace("&5", fullsquad[4].GetFormatName())
        originaltext = originaltext.replace("&l", activedungeon.GetName())
        originaltext = originaltext.replace("&p", pokedexlookup(genpokemon, DexMacros.Name))

        return originaltext

    def HasFlyingPokemon(squadder = None):
        if (squadder == None):
            squadder = squadleader
        for mon in squadder.GetTeam(False):
            if (CanLearn(mon.GetId(), "Fly") or mon.HasAbility("Levitate", False)):
                return mon
        return False

    def HasDefogger(squadder = None):
        if (squadder == None):
            squadder = squadleader
        for mon in squadder.GetTeam(False):
            if (CanLearn(mon.GetId(), "Defog")):
                return mon
        return False

    def HasRockBreaker(squadder = None):
        if (squadder == None):
            squadder = squadleader
        for mon in squadder.GetTeam(False):
            if (CanLearn(mon.GetId(), "Rock Smash")):
                return mon
        return False

    def HasStrongPokemon(squadder = None):
        if (squadder == None):
            squadder = squadleader
        for mon in squadder.GetTeam(False):
            if (CanLearn(mon.GetId(), "Strength")):
                return mon
        return False

    def HasRockClimbingPokemon(squadder = None):
        if (squadder == None):
            squadder = squadleader
        for mon in squadder.GetTeam(False):
            if (CanLearn(mon.GetId(), "Rock Climb")):
                return mon
        return False

    def WildMonCanVocalize(wildmon):
        count = 0
        for move in GetLevelMoves(wildmon):
            if (IsSoundMove(move[1])):
                count += 1
        return count

    def DungeonProg(val=1):
        activedungeon.AlterProgress(val)

    def AnimateMotivation(value, position):
        AnimateValueChange(value, position, changemood=False, pausing=False)

    def MotivateSquadder(squadder=None, change=1):
        if (squadder == None):
            squadder = squadleader
        if (isinstance(squadder, int)):
            change = squadder
            squadder = squadleader
        squadder.ChangeMotivation(change)
        AnimateMotivation(change, GetSquadderPosition(squadder))

    def MotivateParty(change=1, exclude=None):
        if (exclude == None):
            exclude = []
        for squadder in fullsquad:
            if (squadder not in exclude):
                MotivateSquadder(squadder, change)

    def DemotivateSquadder(squadder=None, change=-1):
        if (squadder == None):
            squadder = squadleader
        if (isinstance(squadder, int)):
            change = squadder
            squadder = squadleader
        if (change > 0):
            change = -change
        squadder.ChangeMotivation(change)
        AnimateMotivation(change, GetSquadderPosition(squadder))

    def DemotivateParty(change=-1, exclude=None):
        if (exclude == None):
            exclude = []
        for squadder in fullsquad:
            if (squadder not in exclude):
                DemotivateSquadder(squadder, change)

    def ReturnEventTag(tag, specificevent = None):
        if (specificevent == None):
            event = activedungeon.GetCurrentEvent()
        else:
            event = specificevent
        if (event != None and tag in DungeonEvents[event].keys()):
            return DungeonEvents[event][tag]
        else:
            return None

    def ReturnOptionTag(option, tag, overrideevent=None):
        if (overrideevent == None):
            event = activedungeon.GetCurrentEvent()
        else:
            event = overrideevent
        if (event != None and tag in DungeonEvents[event]["Options"][option].keys()):
            return DungeonEvents[event]["Options"][option][tag]
        else:
            return None

    def GenericEventNames():
        return GenericEvents

    def GetOptionsForMenu(event):
        tupleopts = []
        opts = DungeonEvents[event]["Options"]
        for optionkey in opts.keys():
            option = opts[optionkey]
            excludethis = False
            if ("ExcludeFunction" in option.keys()):
                if (isinstance(option["ExcludeFunction"], tuple)):
                    excludethis = option["ExcludeFunction"][1]()
                else:
                    excludethis = option["ExcludeFunction"]()

            skill = None
            stat = None
            color = None
            threshold = None

            skillcategory = ""
            if "Skill" in option.keys():
                skill = option["Skill"]
                stat = GetSkillStat(skill)
                color = TraitColor(stat)
                threshold = ReturnOptionTag(optionkey, "Threshold")
                skillcategory += "[[{color=" + color + "}" + stat + "{/color}][[{color=" + color + "}" + skill + "{/color}] "

            if (not excludethis):
                tupleopts.append((skill, stat, color, threshold, DisplayDungeonText(optionkey), (event, optionkey)))

            else:
                skillcategory = "{s}" + skillcategory
                if (isinstance(option["ExcludeFunction"], tuple)):
                    returnthis = option["ExcludeFunction"][0]
                    tupleopts.append((skill, stat, color, threshold, DisplayDungeonText(optionkey), returnthis))

        if (ReturnEventTag("GiveUp") in [None, True]):
            tupleopts.append((None, None, None, None, "Ignore this and pick a fight!", False))
        
        return tupleopts

    def DungeonItem(numitems=1, exclude=None, mandate=None):#roll the number of items on the list and give them to the player
        global gimmighoulcount
        itemlist = activedungeon.GenerateItems
        if (mandate != None):
            itemlist = []
            for item in mandate:
                if (isinstance(mandate, tuple)):
                    itemlist.append(item)
                else:
                    itemlist.append((1, item))
        if (exclude != None):
            removelist = []
            for weight, item in itemlist:
                if item in exclude:
                    removelist.append((weight, item))
            for item in removelist:
                itemlist.remove(item)
        if (len(itemlist) == 0):
            return

        givenitems = []
        for _ in range(numitems):
            givenitems.append(WeightedRandomChoice(itemlist))

        itemcounts = {}
        for item in givenitems:
            if item not in itemcounts.keys():
                itemcounts[item] = 1
            else:
                itemcounts[item] += 1
                
        for item, count in itemcounts.items():
            if (item in activedungeon.ItemHistory.keys()):
                activedungeon.ItemHistory[item] += count
            else:
                activedungeon.ItemHistory[item] = count
            if (item == "Gimmighoul Coin"):
                gimmighoulcount += count
                PlaySound("item_get.ogg")
                DungeonSay("Ye hath acquired Gimmighoul Coins of {} count! You haveth now {} in total.".format(count, gimmighoulcount))
            else:
                GetItem(item, count, text="default")

    def RegenWithPriority(prioritizegen):
        global genpokemon
        if (prioritizegen != None):
            maxscore = 0
            newgenpokemon = genpokemon
            for monid in wildpool:
                newscore = prioritizegen(monid)
                if (newscore > maxscore):
                    newgenpokemon = monid
                    maxscore = newscore
            genpokemon = newgenpokemon
        return genpokemon

    def DungeonFight(modifiers = None, assignmon = None, lastbattler = True):
        global sidemonnum
        global genpokemon
        #pick the active Pokémon generated for the encounter and start a battle with it
        #modifier is a dict
        #modifier can contain the following keys:
        #EnemyBoosts - a list of (Stats.Attack, bonus) //Also store penalties here
        #AllyBoosts - a list of (Stats.Attack, bonus) //Also store penalties here
        #EnemyStatus - a list of (status, statuscount)
        #Offset - an int that offsets the dungeon's "intended level" for the enemy

        portraitname = squadleader.Name.lower()
        if (assignmon != None):
            genpokemonobj = assignmon
            genpokemon = assignmon.GetId()
        else:
            genpokemonobj = Pokemon(genpokemon, level=RandInt(dungeonlevel - 2, dungeonlevel + 2), shinylock=False)
        leaderparty = GetTrainerTeam(squadleader.Name, heal=False)
        trainer1 = squadleader
        trainer2 = Trainer("sideportraitfull", TrainerType.Enemy, [genpokemonobj], isPokemon=True)
        squadleaderpkmnobj = trainer1.GetUnfaintedTeam()[0]
        sidemonnum = genpokemon

        if (lastbattler):
            activedungeon.SetLastBattler(squadleader)

        if (modifiers != None):
            for key, value in modifiers.items():
                if (key == "EnemyBoosts"):
                    for stat, boost in value:
                        genpokemonobj.ChangeStats(stat, boost)
                elif (key == "AllyBoosts"):
                    for stat, boost in value:
                        squadleaderpkmnobj.ChangeStats(stat, boost)
                elif (key == "EnemyStatus"):
                    for status, count in value:
                        genpokemonobj.ApplyStatus(status, count)
                elif (key == "Offset"):
                    genpokemonobj.UpdateLevel(genpokemonobj.Level + value, force=True)
                    genpokemonobj.Heal()

        activedungeon.BattleHistory.append((activedungeon.GetProgress(), genpokemonobj))

        renpy.call_in_new_context("Battle", [trainer1, trainer2], healParty = False, clearstats=False)

    def EvaluateEvent(menureturn):
        eventname, optionname = menureturn
        threshold = ReturnOptionTag(optionname, "Threshold")
        if (threshold == None):
            return (True, 0, 0, 0)

        randnum = None
        if (activedungeon.FudgeRollFunc):
            randnum = activedungeon.FudgeRollFunc(activedungeon)
        if (randnum == None):
            randnum = RandInt(1, 20)
        
        bonus = GetSkill(squadleader, ReturnOptionTag(optionname, "Skill"), total=True)

        total = randnum + bonus

        success = randnum + bonus >= threshold
        if (randnum == 1):
            success = False
        elif (randnum == 20):
            success = True

        return (success, threshold, randnum, bonus)

    def GetSprite(squadder):
        if (squadder.GetType() != TrainerType.Player):
            return "images/sprites/characters/" + squadder.GetFormatName().lower() + "field.webp"
        else:
            return "images/sprites/characters/redfield.webp"

    def GetTotalOutcomes():
        numoutcomes = 0
        for key in GenericEvents:
            for option in DungeonEvents[key]["Options"]:
                numoutcomes += (1 if ReturnOptionTag(option, "Rewards", key) != 0 else 0)
                numoutcomes += (1 if ReturnOptionTag(option, "Penalties", key) != 0 else 0)
        return numoutcomes

    def DungeonSay(what):
        renpy.say(dungeonnarrator, DisplayDungeonText(what))
        renpy.sound.stop(channel="bipbop")

    def DungeonEntries(dungeon):
        count = 0
        if (not isinstance(dungeon, str)):
            dungeon = dungeon.Name
        for dive in dungeonhistory:
            if dive[0] == dungeon:
                count += 1
        return dungeon

label cleardungeonscreens:
hide screen DungeonUI
hide screen dungeonchoice
hide screen bonuspreview
hide screen diceroll
hide screen enddiceroll
hide screen rewardpreview
hide screen showtooltip
#hide screen DungeonBackground
with dis

return