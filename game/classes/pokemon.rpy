init python:
    class Pokemon:
        def __init__(self, id, level=5, moves=None, nickname=None, ivs=None, evs=None, nature=None, gender=None, item=None, ability=None, intelligence=0, teratype=None, foreverals=None, offset=0, trained=None, frenzynerf=None, shinylock=True):
            self.Nickname = nickname#string
            if (isinstance(id, str)):
                id = pokedexlookupname(id, DexMacros.Id)
            self.Id = id#int
            self.Level = level#int
            self.IVs = ivs#[int]
            if (self.IVs == None):
                self.IVs = []
                for i in range(0, 6):
                    self.IVs.append(RandInt(0, 31))
            self.EVs = evs#[int]
            if (self.EVs == None):
                self.EVs = [0, 0, 0, 0, 0, 0]
            self.Moves = moves#[Move]
            if (self.Moves == None):
                if (self.Level == 5):
                    self.Moves = GetStartingMoves(self)
                else:
                    self.Moves = GetMovesForLevel(self)
            else:
                self.Moves = []
                for move in moves:
                    if (isinstance(move, str)):
                        self.Moves.append(GetMove(move))
                    else:
                        self.Moves.append(move)
            movenames = []
            removemoves = []
            for newmove in self.Moves:
                if (newmove.Name in movenames):
                    removemoves.append(newmove)
                else:
                    movenames.append(newmove.Name)
            for oldmove in removemoves:
                self.Moves.remove(oldmove)
            self.Nature = nature#Natures macro
            if (self.Nature == None):
                self.Nature = RandInt(0, 24)
            self.Item = GetItemEntryFromName(item)[0] if isinstance(item, str) else item #string or None
            self.Gender = gender#Genders Macro
            if (self.Gender == None and not IsGenderless(self)):
                self.Gender = RandomChoice([Genders.Male, Genders.Female])
            if (self.GetId() in [957, 958, 959, 669, 670, 671, 548, 549, 29, 30, 31, 413, 413.1, 413.2, 629, 630, 440, 113, 242, 238, 124, 440, 113, 242, 592.1, 593.1]):
                self.Gender = Genders.Female
            if (self.GetId() in [32, 33, 34, 414, 627, 628, 236, 237, 106, 107, 592, 593]):
                self.Gender = Genders.Male
            if (self.Gender == None):
                self.Gender = Genders.Unknown

            self.Stats = [0, 0, 0, 0, 0, 0]
            self.RecalculateStats()
            
            self.Health = self.Stats[Stats.Health]
            self.StatChanges = {}
            self.Status = {}#statuses that begin with "." don't get printed
            self.Ability = ability
            if (self.Ability == None):
                self.Ability = random.choice(GetAbilities(id))
            self.Personality = random.random()
            self.Image = None
            self.Experience = self.CalculateAllExperienceNeededForLevel(math.floor(self.Level))
            self.Owner = None#Trainer object, defined during battle
            self.TrainerType = None#TrainerType Macro, defined during battle
            self.WasCaught = 0#int, defined during battle
            self.DamagedThisTurn = False#bool, defined during battle
            self.TurnSwitchedIn = 0#int, defined during battle
            self.Intelligence = intelligence
            self.FaintedOnTurn = -10
            self.ItemHistory = []#list of item changes in battle--set at the start of every battle. List of tuples formatted like ("Started", None, 0), ("Gained", "Oran Berry", 1), ("Lost", "Oran Berry", 2), ("Gained", "Oran Berry", 3), ("Used", "Oran Berry", 4)
            if (teratype == None):
                self.TeraType = pokedexlookup(self.GetId(), DexMacros.Type1)#The 'mon's inherent tera type
            else:
                self.TeraType = teratype
            self.Terastallized = -1#-1 if not terastallized. Otherwise, it's the turn you terastallized
            self.Changedformename = None
            self.FormeOverride = None#keeps track of the current form you're taking
            self.AbilityOverride = None#keeps track of the current ability you have
            self.Foreverals = foreverals
            if (self.Foreverals == None):
                self.Foreverals = []#keeps track of what foreverals are active for you

            self.Offset = offset#keeps track of how many levels up or down the aimlevel this pokemon is when updatelevel is adjusted automatically

            self.Trained = trained
            if (self.Trained == None):
                self.Trained = []#keeps track of what special moves the pokemon has learned

            self.ShinyLock = shinylock
            self.ShinyValue = random.random()
            if (shinylock):
                self.ShinyValue += 1

            self.FrenzyNerf = frenzynerf# in the format (Level, [Movename, Movename, Movename, Movename], (optional)Id)

            self.TimesHit = 0#used primarily for Rage Fist

            self.Pokeball = "Poké Ball"

            self.ClearMarks()

            self.PreTurnAbility = self.GetAbility()#the ability the Pokémon had at the start of the run, before Diveralization, Mega, whatever.

        def SetPreTurnAbility(self):
                self.PreTurnAbility = self.GetAbility()

        def GetPreTurnAbility(self):
            if (not hasattr(self, 'PreTurnAbility')):
                self.PreTurnAbility = self.SetPreTurnAbility()
            return self.PreTurnAbility

        def GetShinyLock(self):
            if (not hasattr(self, 'ShinyLock')):
                self.ShinyLock = True
            return self.ShinyLock

        def GetPokeball(self):
            if (not hasattr(self, 'Pokeball')):
                self.Pokeball = 0
            if isinstance(self.Pokeball, str):
                self.Pokeball = GetItemEntryFromName(self.Pokeball)[ItemdexMacros.Id]
            return GetItemName(self.Pokeball)

        def GetFrenzyNerf(self):
            if (not hasattr(self, 'FrenzyNerf')):
                self.FrenzyNerf = None
            return self.FrenzyNerf

        def GetTrained(self):
            if (not hasattr(self, 'Trained')):
                self.Trained = []
            return self.Trained

        def GetForeverals(self):
            if (not hasattr(self, 'Foreverals')):
                self.Foreverals = []
            return self.Foreverals

        def HasForeveral(self, foreveralname):
            return foreveralname in self.GetForeverals()

        def GetFaintedTurn(self):
            if (not hasattr(self, 'FaintedOnTurn')):
                self.FaintedOnTurn = -10
            return self.FaintedOnTurn

        def ResetFaintedTurn(self):
            self.FaintedOnTurn = -10

        def GetIntelligence(self):
            if (not hasattr(self, 'Intelligence')):
                self.Intelligence = 0
            return self.Intelligence

        def GetTurnSwitchedIn(self):
            if (not hasattr(self, 'TurnSwitchedIn')):
                self.TurnSwitchedIn = 0
            return self.TurnSwitchedIn

        def SetTurnSwitchedIn(self, turnnum):
            self.TurnSwitchedIn = max(0, turnnum)

        def GetDamagedThisTurn(self):
            if (not hasattr(self, 'DamagedThisTurn')):
                self.DamagedThisTurn = False
            return self.DamagedThisTurn

        def SetDamagedThisTurn(self, bool):
            self.DamagedThisTurn = bool

        def GetPersonality(self):
            return self.Personality

        def Trade(self, checksuccess=False):
            evolveid = None

            if (self.GetId() == 137 and self.HasItem(Item.UpGrade)):
                evolveid = 233
            elif (self.GetId() == 233 and self.HasItem(Item.DubiousDisc)):
                evolveid = 474
            elif (self.GetId() == 366 and self.HasItem(Item.DeepSeaTooth)):
                evolveid = 367
            elif (self.GetId() == 366 and self.HasItem(Item.DeepSeaScale)):
                evolveid = 268
            elif (self.GetId() == 112 and self.HasItem(Item.Protector)):
                evolveid = 464
            elif (self.GetId() == 682 and self.HasItem(Item.Sachet)):
                evolveid = 683
            elif (self.GetId() == 684 and self.HasItem(Item.WhippedDream)):
                evolveid = 685
            elif (self.GetId() == 125 and self.HasItem(Item.Electirizer)):
                evolveid = 466
            elif (self.GetId() == 126 and self.HasItem(Item.Magmarizer)):
                evolveid = 467
            elif (self.GetId() == 356 and self.HasItem(Item.ReaperCloth)):
                evolveid = 477
            elif (self.GetId() == 117 and self.HasItem(Item.DragonScale)):
                evolveid = 230
            elif (self.GetId() == 61 and self.HasItem(Item.KingsRock)):
                evolveid = 186
            elif (self.GetId() == 79 and self.HasItem(Item.KingsRock)):
                evolveid = 199

            if (evolveid != None):
                self.Item = None

            if (checksuccess):
                return evolveid != None
            else:
                self.Evolve(evolveid)

        def MakeCaught(self, hp):
            self.WasCaught = hp
            frenzynerf = self.GetFrenzyNerf()
            if (frenzynerf != None):
                if (len(frenzynerf) > 2):
                    self.Id = frenzynerf[2]
                self.Level = 1
                self.UpdateLevel(frenzynerf[0])
                self.Moves = []
                for move in frenzynerf[1]:
                    self.Moves.append(GetMove(move))
                self.RecalculateStats()
                if (self.Foreverals != []):
                    self.Foreverals = []
                    renpy.say(None, "The Pokémon calmed down from its frenzy, but its Foreveral shattered!")
                else:
                    renpy.say(None, "The Pokémon calmed down from its frenzy...")
                if (self.Image != None):
                    self.Image = None
                if (self.Nickname != None):
                    self.Nickname = None
            if (len(playerparty) != 6):
                playerparty.append(self)
            else:
                AddMon(self)
        
        def TryCatchDitto(target, probability=.01):
            if (random.random() <= probability):
                renpy.say(None, "Oh...?")
                renpy.music.stop(fadeout=1)
                renpy.pause(1)
                renpy.music.play("audio/music/evolution.ogg", fadein=1, loop=True)
                renpy.pause(1)
                screen_center = [Transform(yalign=.5, xalign=.5), ditto]
                renpy.show("ditto", screen_center)
                renpy.pause(2.5)
                # ditto's attributes
                target.Id = 132
                target.Moves = []
                target.Moves.append(GetMove("Transform"))
                target.Gender = Genders.Unknown
                target.Ability = "Limber"
                target.RecalculateStats()
                renpy.say(None, "The Pokémon was a Ditto!")
        
        def Untransform(self):
            if self.HasStatus("transformed"):
                self.ClearStatus("transformed")
                self.ChangeForme(132)
            if self.HasStatus("illusion"):
                self.ChangeForme(self.Id, revert = True)
                self.ClearStatus("illusion")
            self.ClearStatus(".fixated")

        def ResetCaught(self):
            self.WasCaught = 0

        def GetShinyValue(self):
            if self.HasStatus("illusion"):
                self = self.GetStatusCount("illusion")
            if (not hasattr(self, 'ShinyValue')):
                self.ShinyValue = random.random()
            return self.ShinyValue

        def IsShiny(self):
            return self.GetShinyValue() <= 1.0/8192.0

        def GetCaught(self):
            if (not hasattr(self, 'WasCaught')):
                self.ResetCaught()
            return self.WasCaught

        def RecalculateStats(self, updateHealth = True):
            for i in range(6):
                if not (self.Id == 132 and i == 0): # Ditto's health doesn't change during transformation, so it should not be recalculated from its form but from itself
                    basestat = pokedexlookup(self.GetId(), i + DexMacros.Health)
                else:
                    basestat = pokedexlookup(self.Id, i + DexMacros.Health)
                for fvl in self.GetForeverals():
                    if (fvl == "Pichu Everal"):
                        basestat += GetWinLoss("Ethan")[0] * 10#calm down. I'll change this formula later on. It's not going to be linear forever
                    elif (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.Scaling):
                        scalingmon, scalinglevel = lookupforeveraldata(fvl, FVLMacros.FVLTypeData)
                        scalingstat = pokedexlookupname(scalingmon, i + DexMacros.Health)
                        newstat = basestat * max((scalinglevel - self.GetLevel()) / scalinglevel, 0) + scalingstat * min(self.GetLevel() / scalinglevel, 1)
                        if (newstat > basestat):
                            basestat = newstat

                self.Stats[i] = math.floor((math.floor(0.01 * (2 * basestat + self.IVs[i] + math.floor(0.25 * self.GetEV(i))) * self.Level) + 5) * NatureToBonus(self.Nature, i))

            if (self.GetId() == 292):#Shedinja
                self.Stats[Stats.Health] = 1
            else:
                if not (self.Id == 132): # Ditto's health doesn't change during transformation, so it should not be recalculated from its form but from itself
                    basestat = pokedexlookup(self.GetId(), DexMacros.Health)
                else:
                    basestat = pokedexlookup(self.Id, DexMacros.Health)
                for fvl in self.GetForeverals():
                    if (fvl == "Pichu Everal"):
                        basestat += GetWinLoss("Ethan")[0] * 15#calm down. I'll change this formula later on. It's not going to be linear forever
                    elif (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.Scaling):
                        scalingmon, scalinglevel = lookupforeveraldata(fvl, FVLMacros.FVLTypeData)
                        scalingstat = pokedexlookupname(scalingmon, i + DexMacros.Health)
                        newstat = basestat * max((scalinglevel - self.GetLevel()) / scalinglevel, 0) + scalingstat * min(self.GetLevel() / scalinglevel, 1)
                        if (newstat > basestat):
                            basestat = newstat

                maxhealth = math.floor(math.floor(0.01 * (2 * basestat + self.IVs[Stats.Health] + math.floor(0.25 * self.GetEV(Stats.Health))) * self.Level) + self.Level + 10)
                self.Stats[Stats.Health] = maxhealth
                self.Health = min(self.GetHealth(), maxhealth)

        def CalculateExperienceNeededForLevel(self, level):
            if (level < 2):
                return 0
            return pow(level, 3) / 25

        def CalculateAllExperienceNeededForLevel(self, level):
            totalval = 0
            for i in range(1, level + 1):
                totalval += self.CalculateExperienceNeededForLevel(i)
            return totalval

        def CalculateGivingExperience(self, othermon):
            ownlevel = min(AimLevel(), self.GetLevel())
            return math.floor(10 + self.CalculateExperienceNeededForLevel(ownlevel) * ownlevel / (othermon.GetLevel() + max(0, (othermon.GetLevel() - self.GetLevel())) * 10) * pokedexlookup(self.GetId(), DexMacros.Total) / 300 * 0.1)

        def GetLevelCap(self):
            highest = 1
            if (self.Ability == "Freelectric" and 1 in freelectricphases):
                highest = classstats[GetStatRank(0)] + 1

            elements = self.GetTypes(True)
            for fvl in self.GetForeverals():
                if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.AddProficiency or lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.AddType):
                    for proficientelement in lookupforeveraldata(fvl, FVLMacros.FVLTypeData):
                        elements.append(proficientelement)
                elif (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.FormSwap):
                    for mon in lookupforeveraldata(fvl, FVLMacros.FVLTypeData):
                        elements.append(pokedexlookup(mon, DexMacros.Type1))
                        elements.append(pokedexlookup(mon, DexMacros.Type2))
                elif (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.AddType):
                    for mon in lookupforeveraldata(fvl, FVLMacros.FVLTypeData):
                        elements.append(pokedexlookup(mon, DexMacros.Type1))
                        elements.append(pokedexlookup(mon, DexMacros.Type2))
                elif (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.Mega):
                    elements.append(pokedexlookup(lookupforeveraldata(fvl, FVLMacros.FVLTypeData)[1], DexMacros.Type1))
                    elements.append(pokedexlookup(lookupforeveraldata(fvl, FVLMacros.FVLTypeData)[1], DexMacros.Type2))
            for element in elements:
                if (element != None):
                    if (classstats[element] > highest):
                        highest = classstats[element]
            return math.floor(highest)

        def GetMaxLevel(self):
            for i in range(100):
                if (self.GetExperience() < self.CalculateAllExperienceNeededForLevel(i)):
                    return i - 1
            return 100

        def LearnNewMove(self, newmoves, fullpp = True):
            if (len(newmoves) > 0):
                for movetuple in newmoves:
                    newmove = movetuple[1]
                    moveconfirmed = False
                    equalizedpp = False
                    hidescreen = False
                    
                    if (newmove not in self.GetMoveNames()):
                        newmoveobj = GetMove(newmove)
                        self.Moves.append(newmoveobj)
                        if (not fullpp):
                            totalpp = 0
                            newmoveobj.PP = 0
                            for move in self.Moves:
                                totalpp += move.PP
                            fragmentpp = math.floor(totalpp / min(len(self.Moves), 4))
                            for move in self.Moves:
                                move.PP = min(move.MaxPP, fragmentpp)
                            equalizedpp = True

                        hidescreen = renpy.get_screen("currentdate") != None
                        if (hidescreen):
                            renpy.hide_screen("currentdate")
                    
                        while (not moveconfirmed):
                            if (len(self.GetMoves()) > 4):
                                renpy.say("", self.GetNickname() + " wants to learn " + newmove + ", but " + self.GetNickname() + " already knows four moves. Which move should " + self.GetNickname() + " forget?")
                                removal = renpy.call_screen("nonbattlemoves", self, True, True)
                                moveconfirmed = renpy.display_menu([("Forget " + removal.Name, True), ("Keep " + removal.Name, False)], interact=True, screen="choice")
                                if (moveconfirmed):
                                    self.Moves.remove(removal)
                                    if (removal.Name != newmove):
                                        renpy.say("", self.GetNickname() + " forgot " + removal.Name + " and learned " + newmove + "!")
                                        if (newmove != "Liberage"):
                                            newmoveobj.PP = min(removal.PP, newmoveobj.MaxPP)
                                    else:
                                        renpy.say("", self.GetNickname() + " did not learn " + newmove + "!")
                            else:
                                moveconfirmed = True
                                renpy.say("", self.GetNickname() + " learned " + newmove + "!")
                        if (equalizedpp):
                            renpy.say(None, "All moves' PP balanced.")
                        if (hidescreen):
                            renpy.show_screen("currentdate")
            
            self.HandleLiberationOverflow()

        def HandleLiberationOverflow(self):
            hidescreen = False
            if (self.Id == 25.2):
                ll = GetLiberationLimit()
                hidescreen = False
                while (ll[0] > maxliberationlimit):
                    hidescreen = (renpy.get_screen("currentdate") != None or hidescreen)
                    if (hidescreen):
                        renpy.hide_screen("currentdate")
                    renpy.say(None, pika_name + " is overflowing with power! Something's gotta give! " + pika_name + " is " + str(math.floor(ll[0] - maxliberationlimit)) + " over the limit!")

                    changes = []
                    for category, specific, increase in ll[1]:
                        name = ""
                        if (not isinstance(specific, str)):
                            specific = pokedexlookup(specific, DexMacros.Name)
                        if (specific not in category):
                            name = category.lower() + " (" + specific +"): " + str(math.floor(increase))
                        else:
                            name = category.lower() + ": " +  str(math.floor(increase))
                        returnable = (category, specific)
                        changes.append((">Remove " + name.title(), returnable))

                    returned = renpy.display_menu(changes)
                    if (returned[0] == "Move"):
                        removeobj = None
                        for move in self.GetMoves():
                            if (move.Name == returned[1]):
                                removeobj = move
                        self.Moves.remove(removeobj)
                    elif (returned[0] == "Diveral"):
                        self.ChangeForme(25.2, revert=True)
                    else:
                        RemoveForeverals(self)

                    ll = GetLiberationLimit()

            if (hidescreen):    
                renpy.show_screen("currentdate")

        def GainExperience(self, newexp, fainting=False, show_screen=None, ignorescaling=False):
            global starter_id
            global starter_name
            global starter_species_name

            if (show_screen != None):
                renpy.show_screen(show_screen)

            if (not hasattr(self, 'Experience')):
                self.Experience = self.CalculateAllExperienceNeededForLevel(self.Level)

            newexp = RunItemFunction("gainExp", self, [newexp])
            if (not ignorescaling):
                if (newexp > 10 and self.GetMaxLevel() > AimLevel()):
                    newexp /= (self.GetMaxLevel() - AimLevel())
                    newexp = max(10, newexp)

            posttext = ""
            if (self.Level >= self.GetLevelCap()):
                posttext = " The experience has been stored for later!"
            renpy.say("", self.GetNickname() + " gained " + str(math.floor(newexp)) + " experience!" + posttext)
            self.Experience += newexp
            priorlevel = self.GetLevel()
            while (self.GetExperience() > self.CalculateAllExperienceNeededForLevel(self.Level + 1) and self.Level < self.GetLevelCap()):
                self.Level += 1
                OldHp = self.Stats[Stats.Health]
                self.RecalculateStats()
                if (not fainting):
                    NewHp = self.Stats[Stats.Health]
                    self.AdjustHealth(NewHp - OldHp, directdamage=True)
                renpy.say("", self.GetNickname() + " leveled up to level " + str(self.GetLevel()) + "!")
                if (self.Id != 25.2):
                    newmoves = GetLevelMoves(self, self.GetLevel(), True)
                    self.LearnNewMove(newmoves, True)   

            if (self.GetLevel() != priorlevel and self.Id != 25.2 and not fainting):
                evoconditions = []

                for mon in pokedex.values():
                    if (mon[DexMacros.Prevo] == pokedexlookup(self.GetId(), DexMacros.Forme)):
                        evocondition = mon[DexMacros.Evolve]
                        if (evocondition != None and len(evocondition) <= 6 and "Lv." in evocondition):
                            evoconditions.append(mon[DexMacros.Evolve])

                if (evoconditions != []):
                    evocondition = evoconditions[0]
                else:
                    evocondition = ""

                passesevocondition = (self.GetId() in [412, 412.1, 412.2] and self.GetLevel() >= 20# burmy
                    or self.GetId() == 439 and "Mimic" in self.GetMoveNames()#Mime Jr.
                    or self.GetId() == 438 and "Mimic" in self.GetMoveNames()#Bonsly
                    or self.GetId() == 852 and "Taunt" in self.GetMoveNames()#Clobbopus
                    or self.GetId() == 190 and "Double Hit" in self.GetMoveNames()#Aipom
                    or self.GetId() == 744 and (IsMidday() or IsEvening() or IsNight()) and self.GetLevel() >= 25#Rockruff
                    or self.GetId() == 236 and self.GetLevel() >= 20#Tyrogue
                    or self.GetId() == 458 and 223 in GetPartySpecies()#Mantyke
                    or self.GetId() == 848 and self.GetLevel() >= 30#Toxel
                    or self.GetId() == 440 and self.HasItem(Item.OvalStone) and IsEarlier() # Happiny
                    or self.GetId() == 215 and self.HasItem(Item.RazorClaw) and IsLater() # Sneasel
                    or self.GetId() == 215.1 and self.HasItem(Item.RazorClaw) and IsEarlier()
                    or self.GetId() == 207 and self.HasItem(Item.RazorFang) and IsLater() # Gligar
                    or evocondition != "" and int(evocondition.split("Lv. ")[1]) <= self.GetLevel())

                evolveinto = self.GetId() + 1
                if (self.GetId() in [412, 412.1, 412.2] and self.GetGender() == Genders.Male):#male burmy -> mothim
                    evolveinto = 414
                elif (self.GetId() == 439):#Mime Jr -> Mr. Mime
                    evolveinto = 122
                elif (self.GetId() == 194.1):#Paldean Wooper
                    evolveinto = 980
                elif (self.GetId() == 744):
                    if (IsEvening()):#dusk lycanroc
                        evolveinto = 745.2
                    elif (IsNight()):#midnight lycanroc
                        evolveinto = 745.1
                elif (self.GetId() == 677):
                    if (self.GetGender() == Genders.Female):#female meowstic
                        evolveinto = 678.1
                elif (self.GetId() == 236):
                    if (self.GetStat(Stats.Attack, absolute=True) > self.GetStat(Stats.Defense, absolute=True)):#hitmonlee 
                        evolveinto = 106
                    elif (self.GetStat(Stats.Attack, absolute=True) < self.GetStat(Stats.Defense, absolute=True)):#hitmonchan
                        evolveinto = 107
                elif (self.GetId() == 240):
                    evolveinto = 126#magmar
                elif (self.GetId() == 238):
                    evolveinto = 124#jynx
                elif (self.GetId() == 360):
                    evolveinto = 202#wobbuffet
                elif (self.GetId() == 194.1):
                    evolveinto = 980#clodsire
                elif (self.GetId() == 190):
                    evolveinto = 424#ambipom
                elif (self.GetId() == 438):
                    evolveinto = 185#sudowoodo
                elif (self.GetId() == 458):
                    evolveinto = 226#Mantine
                elif (self.GetId() == 848 and self.GetNature() in [Natures.Lonely, Natures.Bold, Natures.Relaxed, Natures.Timid, Natures.Serious, Natures.Modest, Natures.Mild, Natures.Quiet, Natures.Bashful, Natures.Calm, Natures.Gentle, Natures.Careful]):
                    evolveinto = 849.1
                elif (self.GetId() == 440):
                    evolveinto = 113
                elif (self.GetId() == 215):
                    evolveinto = 461
                elif (self.GetId() == 215.1):
                    evolveinto = 903
                elif (self.GetId() == 207):
                    evolveinto = 472

                if (passesevocondition):
                    self.Evolve(evolveinto)
                    
            expleft = math.floor(self.GetExperience() - self.CalculateAllExperienceNeededForLevel(self.Level))
            if (posttext == "" and self.Level >= self.GetLevelCap() and expleft != 0):
                renpy.say("", str(expleft) + " experience has been stored for later!") 

            if (show_screen != None):
                renpy.hide_screen(show_screen)

        def Evolve(self, evolveinto):
            oldname = self.GetNickname()
            damagebefore = self.GetStat(Stats.Health, absolute=True) - self.Health
            oldabilityslot = GetAbilities(self.Id).index(self.Ability)
            renpy.say(None, "What?")
            renpy.pause(1.0)

            renpy.music.set_volume(0.0, 0.5)
            renpy.music.set_volume(0.0, 0.5, channel="crowd")
            renpy.music.set_volume(0.0, 0.5, channel="crowd2")
            renpy.music.set_volume(0.0, 0.5, channel="misc")
            renpy.music.queue("audio/music/evolution_cut.ogg", channel="evolution")

            evolved = renpy.call_screen("evolution", self.GetId(), evolveinto)
            if (evolved):
                renpy.music.set_volume(1.0, 0.5)
                renpy.music.set_volume(1.0, 0.5, channel="crowd")
                renpy.music.set_volume(1.0, 0.5, channel="crowd2")
                renpy.music.set_volume(1.0, 0.5, channel="misc")
                renpy.music.stop(channel="evolution")
                PlaySound("Get.ogg")

                if (self.GetId() == 440 and self.HasItem(Item.OvalStone)
                    or self.GetId() == 215 and self.HasItem(Item.RazorClaw)
                    or self.GetId() == 215.1 and self.HasItem(Item.RazorClaw)
                    or self.GetId() == 207 and self.HasItem(Item.RazorFang)):
                    self.Item = None

                newspeciesname = pokedexlookup(evolveinto, DexMacros.Name)
                oldspeciesname = pokedexlookup(self.GetId(), DexMacros.Name)
                self.Id = evolveinto
                self.RecalculateStats()
                self.Ability = GetAbilities(self.Id)[min(oldabilityslot, len(GetAbilities(self.Id)) - 1)]
                self.AdjustHealth(self.GetStat(Stats.Health, absolute=True) - damagebefore, True)
                
                preposition = "a"
                if (newspeciesname[0].lower() in ["a", "e", "i", "o", "u"]):
                    preposition += "n"

                renpy.say(None, "{} evolved into {} {}!".format(oldname, preposition, newspeciesname))
                
                if (self.GetNickname() == oldspeciesname):
                    self.Nickname = newspeciesname
                if (len(self.GetForeverals()) > 0):
                    renpy.say(None, "But its Foreveral is no longer in tune with {}'s wishes!".format(self.GetNickname()))
                    for fvl in self.GetForeverals():
                        foreveralinv.append(fvl)
                    self.Foreverals = []
                self.ChangeForme(None, revert=True)
                newmoves = GetLevelMoves(self, self.GetLevel(), True)
                self.LearnNewMove(GetEvoMoves(self) + newmoves)

                if (self.GetId() == 291 and len(playerparty) < 6):#Ninjask
                    playerparty.append(Pokemon(292, level=self.GetLevel(), ivs=copy.copy(self.IVs), moves=self.GetMoveNames(), evs=copy.copy(self.EVs), nature=self.GetNature(), gender=Genders.Unknown))

                if (self == starterobj):
                    starter_id = self.Id
                    starter_name = self.GetNickname()
                    starter_species_name = newspeciesname
                
            else:
                renpy.music.set_volume(1.0, 0.5)
                renpy.music.set_volume(1.0, 0.5, channel="crowd")
                renpy.music.set_volume(1.0, 0.5, channel="crowd2")
                renpy.music.set_volume(1.0, 0.5, channel="misc")
                renpy.music.stop(channel="evolution")

                renpy.music.queue("audio/music/evolution_cut.ogg")

                renpy.say(None, "{} didn't evolve...".format(self.GetNickname()))

        def CanSetEV(self, stat, amount):
            evscopylist = copy.deepcopy(self.EVs)
            if (evscopylist[stat] == amount):#can't set to what it already is
                return False
            evscopylist[stat] = amount
            return not (sum(evscopylist) > 510 or evscopylist[stat] > 252)

        def CanModifyEV(self, stat, amount):
            return not (sum(self.EVs) + amount > 510 or self.GetEV(stat) + amount > 252)

        def SetEV(self, stat, amount):
            if (self.CanSetEV(stat, amount)):
                self.EVs[stat] = amount

        def ModifyEV(self, stat, amount):
            amount = RunItemFunction("gainEVs", self, [amount])
            if (self.CanModifyEV(stat, amount)):
                self.EVs[stat] += amount

            for i, item in enumerate(self.EVs):
                if (item > 252):
                    self.EVs[i] = 252

        def GetItem(self):
            return self.Item

        def GetItemName(self):
            return GetItemName(self.GetItem())

        def GetItemHistory(self):
            if (not hasattr(self, 'ItemHistory')):
                self.ItemHistory = []
            return self.ItemHistory

        def AdjustItemHistory(self, action, item):
            if (not hasattr(self, 'ItemHistory')):
                self.ItemHistory = []
            self.ItemHistory.append((action, item, Turn))

        def UsedStartingItem(self):
            for action, item, turn in self.GetItemHistory():
                if (action == "Used" and item == self.GetStartingItem()):
                    return True
            return False

        def GetStartingItem(self):
            try:
                return mon.GetItemHistory()[0][1]
            except:
                return None

        def TakeItem(self):
            if (dawnbattle and self.Item == 249):
                return "Dawn's Altaria holds onto the Altarianite firmly!"
            if (not self.HasItem(None)) and not self.HasStatus("substitute"):
                olditem = self.GetItem()
                self.Item = None
                self.AdjustItemHistory("Lost", olditem)
                return "{} lost its {}!".format(self.GetNickname(), GetItemName(olditem))
                RunItemFunction("removed", self, [], item = olditem)
            elif (self.HasStatus("substitute")):
                return "The substitute isn't holding anything!"
            else:
                return "But {} isn't holding anything!".format(self.GetNickname())

        def GiveItem(self, item, overwrite=False):
            global itemDialogText
            if (item != None and (not self.HasItem(None)) and not overwrite):
                return "But {} is already holding the {}!".format(self.GetNickname(), self.GetItemName())
            elif (item != None):
                self.Item = item
                self.AdjustItemHistory("Gained", item)
                if inbattle:
                    RunItemFunction("received", self, [], item)
                else:
                    itemDialogText = ""
                return "{} gained the {}! {}".format(self.GetNickname(), GetItemName(item), itemDialogText)
            elif not self.HasItem(None):
                self.TakeItem()

            return ""

        def GetFormeOverride(self):
            if (not hasattr(self, 'FormeOverride')):
                self.FormeOverride = None
            return self.FormeOverride
        
        def GetFormeName(self):
            if (not hasattr(self, 'Changedformename')):
                self.Changedformename = None
            return self.Changedformename

        def GetId(self):
            return (self.Id if self.GetFormeOverride() == None else self.GetFormeOverride())

        def GetStatusKeys(self):
            return self.Status.keys()

        def GetStatusCount(self, status):
            if (self.HasStatus(status)):
                return self.Status[status]
            return 0

        def HasStatus(self, status):
            try:
                return status.lower() in self.GetStatusKeys()
            except:
                return False

        def HasNormalStatus(self):
            for status in normalstatuses:
                if (self.HasStatus(status)):
                    return True
            return False

        def GetNormalStatus(self):
            for status in normalstatuses:
                if (self.HasStatus(status)):
                    return status
            return False 

        def GetOffset(self):
            if (not hasattr(self, 'Offset')):
                self.Offset = 0
            return self.Offset

        def GetNature(self):
            return self.Nature

        def GetAbilityChanged(self):
            return self.GetPreTurnAbility() != self.GetAbility()

        def ApplyStatus(self, status, count=1, applier=None, overwrite=False):
            if (self.GetHealthPercentage() <= 0):
                return ""

            returnable = ""
            if (applier == None):
                applier = self

            if (status == ".tracing"):#don't need to set preturnability, because it's automatic
                ReactivateAbility(self, True)

            if (applier != self and self.HasStatus("substitute") and not IsSoundMove(ActiveMove) and not applier.HasAbility("Infiltrator")):
                return "The substitute absorbed the status!"
            elif (BattlefieldExists("Misty Terrain") and (status in normalstatuses or status == "confused")):
                return "Misty Terrain prevented the affliction!"
            elif (BattlefieldExists("Electric Terrain") and status in ["asleep", "drowsy"]):
                return "Electric Terrain prevented the affliction!"
            elif (WeatherIs("sunny") and (status in normalstatuses) and self.HasAbility("Leaf Guard")):
                return "The leaf guard prevented the affliction!"
            elif (applier != self and EffectOnOwnField(self, "safeguard") and (status in normalstatuses or status == "confused")):
                return "The safeguard prevented the affliction!"
            elif (status == "asleep" and self.HasAbility("Sweet Veil")):
                return "Sweet Veil prevented sleep!"
            elif (status == "asleep" and (self.HasAbility("Insomnia") or self.HasAbility("Vital Spirit") or StatusInBattlers("uproaring"))):
                return "{} can't fall asleep!".format(self.GetNickname())
            elif (status == "confused" and self.HasAbility("Own Tempo")):
                return "Own Tempo prevented confusion!"
            elif (status == "flinching" and self.HasAbility("Steadfast")):
                self.ChangeStats(Stats.Speed, 1, self)
            elif (status == "flinching" and self.HasAbility("Inner Focus")):
                return "{} didn't flinch!".format(self.GetNickname())
            elif (status == "paralyzed" and self.HasAbility("Limber")):
                return "{} is too limber to be paralyzed!".format(self.GetNickname())
            elif (status == "paralyzed" and self.HasType("Electric")):
                return "{} cannot be paralyzed!".format(self.GetNickname())
            elif (status == "taunted" and self.HasAbility("Oblivious")):
                return "{} is oblivious to the taunt!".format(self.GetNickname())
            elif (status == "infatuated" and self.HasAbility("Oblivious")):
                return "{} is oblivious to the foe's charms!".format(self.GetNickname())
            elif (status == "burned" and self.HasType("Fire")):
                return "{} cannot be burned!".format(self.GetNickname())
            elif (status == "frozen" and self.HasType("Ice")):
                return "{} cannot be frozen!".format(self.GetNickname())
            elif (status == "frostbitten" and self.HasType("Ice")):
                return "{} cannot be frostbitten!".format(self.GetNickname())
            elif ((status == "poisoned" or status == "badly poisoned") and (self.HasType("Poison") or self.HasType("Steel")) and not applier.HasAbility("Corrosion")):
                return "{} cannot be poisoned!".format(self.GetNickname())
            elif (self.Image == None and (status in normalstatuses or status == "drowsy") and self.HasAbility("Shields Down")):
                return "But {}'s shield is up!".format(self.GetNickname())
            elif ((status in normalstatuses or status == "drowsy") and self.HasAbility("Purifying Salt")):
                return "But {}'s salt is pure!".format(self.GetNickname())
            elif (status == "burned" and self.HasAbility("Water Veil")):
                return "Water Veil prevents burns!"
            elif (status in ["poisoned", "badly poisoned"] and self.HasAbility("Immunity")):
                return "{} is immune to poison!".format(self.GetNickname())
            elif (status == "burned" and self.HasAbility("Thermal Exchange")):
                return "{} vents the heat, and is not burned!".format(self.GetNickname())

            if (not overwrite):
                for affliction in normalstatuses:
                    if (status[0] != "."):
                        if ((status in normalstatuses or status == "drowsy") and affliction in self.Status.keys()):
                            return "But {} is already {}!".format(self.GetNickname(), affliction)
                        elif (self.HasStatus(status)):
                            return "But {} is already {}!".format(self.GetNickname(), status)
            
            if (applier != self and status in ["burned", "paralyzed", "poisoned", "badly poisoned"] and self.HasAbility("Synchronize")):
                applier.ApplyStatus(status, count)
                returnable = "Synchronize copied the status!"

            if (status == "asleep" and self.HasAbility("Early Bird")):
                count = math.floor(count / 2.0)

            self.Status[status] = count
            RunItemFunction("receivedStatus", self, [status])

            if (status == "raging"):
                return "{} started raging!".format(self.GetNickname())
            elif (status == "stockpiled"):
                return "{} stockpiled {}!".format(self.GetNickname(), self.GetStatusCount("stockpiled"))
            elif (status == "substitute"):
                return "{} hid behind a substitute!".format(self.GetNickname())
            elif (status == "flinching" or status[0] == "."):
                return ""
            elif (status == "aqua ring"):
                return "{} set up an Aqua Ring!".format(self.GetNickname())
            elif (status == "gorging" and self.HasStatus("frenzied")):
                return "The frenzied Cramorant is trying to swallow [pika_name]!"
            return "{} became {}! {} {}".format(self.GetNickname(), status, returnable, itemDialogText).strip()

        def DecrementStatus(self, status):
            returnable = ""
            if (self.HasStatus(status)):
                self.Status[status] = self.GetStatusCount(status) - 1
                if (status == "wrapped" and self.Status["wrapped"] == 0):
                    returnable += "{} was freed from Wrap!".format(self.GetNickname())
                if (status == "bound" and self.Status["bound"] == 0):
                    returnable += "{} was freed from Bind!".format(self.GetNickname())
                if (status == "firespun" and self.Status["firespun"] == 0):
                    returnable += "{} was freed from Fire Spin!".format(self.GetNickname())
                if (status == "whirlpooled" and self.Status["whirlpooled"] == 0):
                    returnable += "{} was freed from Whirlpool!".format(self.GetNickname())
                if (status == "entombed" and self.Status["entombed"] == 0):
                    returnable += "{} was freed from Sand Tomb!".format(self.GetNickname())
                if (status == "clamped" and self.Status["clamped"] == 0):
                    returnable += "{} was freed from Clamp!".format(self.GetNickname())
                if (status == "infested" and self.Status["infested"] == 0):
                    returnable += "{} was freed from Infestation!".format(self.GetNickname())
                if (status == "perishing"):
                    returnable += "{}'s perish count fell to {}!".format(self.GetNickname(), self.GetStatusCount(status))
            return returnable

        def HasItem(self, item):
            if isinstance(item, str):
                item = GetItemEntryFromName(item)[0]
            return self.GetItem() == item

        def MarkItemUsed(self):
            self.AdjustItemHistory("Used", self.GetItem())
            for ally in GetBattlers(self):
                if (ally.GetItem() == None and ally.HasAbility("Symbiosis")):
                    ally.GiveItem(self.GetItem())
                    break
            if (IsBerry(self.GetItem()) and self.HasAbility("Cheek Pouch")):
                self.AdjustHealth(self.GetStat(Stats.Health) / 3.0)
            self.Item = None

        def ClearStatus(self, status, all=False, volatiles=False, nonvolatilesandconfusion=False):
            returntext = ""
            if (volatiles):
                copystatus = self.Status.copy()
                for existingstatus in copystatus.keys():
                    if (existingstatus not in nonvolatiles):
                        del self.Status[existingstatus]
            elif (nonvolatilesandconfusion):
                copystatus = self.Status.copy()
                for existingstatus in copystatus.keys():
                    if (existingstatus in normalstatuses + ["confused"]):
                        del self.Status[existingstatus]
            elif (all):
                keepstatuses = {}
                if (self.HasStatus("busted disguise") and self.GetHealthPercentage() < 1):
                    keepstatuses["busted disguise"] = 1
                if (self.HasStatus("transformed")):
                    keepstatuses["transformed"] = 1
                if (self.HasStatus("illusion")):
                    keepstatuses["illusion"] = 1
                self.Status = keepstatuses
            elif (status in self.Status):
                if (status == "thrashing" and self.GetStatusCount("thrashing") == 0):
                    returntext += self.ApplyStatus("confused", RandInt(4, 5), self)
                del self.Status[status]
                return self.GetNickname() + " is no longer " + status + "!" + returntext

        def AdjustHealth(self, adjustment, absolute=False, directdamage=False):
            global AutoLose
            diddamage = False
            if (absolute):
                if (not self.HasStatus("unhealthy") or adjustment < self.Health):
                    self.Health = (math.floor(adjustment) if not allowfractions else adjustment)
                    diddamage = True
            elif (directdamage or adjustment > 0 or not self.HasAbility("Magic Guard")):
                if (adjustment < 0):
                    self.SetDamagedThisTurn(True)
                    if (directdamage):
                        self.TimesHit += 1
                    if not (mon in FaintedMons or mon.GetHealthPercentage() <= 0):
                        RunItemFunction("takingDamage", self, [])
                if (not self.HasStatus("unhealthy") or adjustment < 0):
                    self.Health += math.floor(adjustment)
                if (self.Health <= 0):
                    self.Health = 0
                elif (self.Health > self.Stats[Stats.Health]):
                    self.Health = self.Stats[Stats.Health]    
                diddamage = True 

            if (self.GetId() == 774 and self.GetHealthPercentage() > 0.5):#Minior
                self.ChangeForme("Minior (Meteor Form)")

            if (self.GetId() in [334, 334.1] and dawnbattle and self.GetHealth() < 1 and self not in playerparty):
                self.Health = 1
                #I'm genuinely sorry I had to do this. If it's any consolation, you're very smart.
                #EDIT: Okay, that's what I wrote last release, but at this point, the constant whining has quite turned me off from any compliments.
            elif (self.GetId() == 352 and HasEvent("Professor Oak", "KecleonTest") and adjustment < 0):
                AutoLose = True

            return diddamage

        def GetMarks(self):
            if (not hasattr(self, 'Marks')):
                self.ClearMarks()
            return self.Marks

        def ClearMarks(self):
            self.Marks = {"❤": False, "🧡": False, "💛": False, "💚": False, "💙": False, "💜": False, "⭐": False}

        def GetHealth(self):
            if (not hasattr(self, 'Health')):
                self.Health = 1
            return self.Health

        def GetHealthPercentage(self):
            return self.GetHealth() / self.Stats[Stats.Health]

        def GetStat(self, stat, ignorepositive=False, ignorenegative=False, triggerAbilities = True, absolute=False):
            if (absolute):
                return self.Stats[stat]

            if (BattlefieldExists("Wonder Room")):
                if (stat == Stats.Defense):
                    stat = Stats.SpecialDefense
                elif (stat == Stats.SpecialDefense):
                    stat = Stats.Defense

            rawstat = self.Stats[stat]
            if (self.HasStatus("guard split")):
                if (stat == Stats.Defense):
                    rawstat = self.GetStatusCount("guard split")[0]
                elif (stat == Stats.SpecialDefense):
                    rawstat = self.GetStatusCount("guard split")[1]

            if (self.HasStatus("power split")):
                if (stat == Stats.Defense):
                    rawstat = self.GetStatusCount("power split")[0]
                elif (stat == Stats.SpecialDefense):
                    rawstat = self.GetStatusCount("power split")[1]

            if (self.HasStatus("power tricked")):
                if (stat == Stats.Attack):
                    rawstat = self.Stats[Stats.Defense]
                elif (stat == Stats.Defense):
                    rawstat = self.Stats[Stats.Attack]

            modifier = self.GetStatChanges(stat)
            if (modifier > 0):
                modifier = (modifier + 2) / 2.0
            elif (modifier < 0):
                modifier = 2.0 / (-modifier + 2)
            
            if (modifier == 0 or (modifier > 1 and ignorepositive) or (modifier < 1 and ignorenegative)):
                modifier = 1
            
            if (stat == Stats.Speed):
                if (self.HasStatus("paralyzed")):
                    if (self.HasAbility("Quick Feet")):
                        modifier *= 1.5
                    else:
                        modifier /= 2.0
                if (WeatherIs("sunny") and self.HasAbility("Chlorophyll", triggerAbilities)):
                    modifier *= 2.0
                if (WeatherIs("sandstorm") and self.HasAbility("Sand Rush", triggerAbilities)):
                    modifier *= 2.0
                if (WeatherIs("rainy") and self.HasAbility("Swift Swim", triggerAbilities)):
                    modifier *= 2.0
                if (self.HasAbility("Slow Start") and self.GetTurnSwitchedIn() + 5 > Turn):
                    modifier *= 0.5
                if (EffectOnOwnField(self, "tailwind")):
                    modifier *= 1.5
                modifier = RunItemFunction("checkingSpeedStat", self, [modifier])
            elif (stat == Stats.Attack):
                if (self.HasAbility("Hustle")):
                    modifier *= 1.5
                if (self.HasNormalStatus() and self.HasAbility("Guts", triggerAbilities)):
                    modifier *= 1.5
                if (self.GetHealthPercentage() <= 0.5 and self.HasAbility("Defeatist", triggerAbilities)):
                    modifier *= 0.5
                if (self.HasAbility("Pure Power") or self.HasAbility("Huge Power")):
                    modifier *= 2.0
                if (self.HasAbility("Slow Start") and self.GetTurnSwitchedIn() + 5 > Turn):
                    modifier *= 0.5
                if (self.HasAbility("Gorilla Tactics")):
                    modifier *= 1.5
                modifier = RunItemFunction("checkingAttackStat", self, [modifier])
            elif (stat == Stats.SpecialAttack):
                if (WeatherIs("sunny") and self.HasAbility("Solar Power", triggerAbilities)):
                    modifier *= 1.5
                if (self.GetHealthPercentage() <= 0.5 and self.HasAbility("Defeatist", triggerAbilities)):
                    modifier *= 0.5
                if ((self.HasAbility("Plus") and AbilityOnOwnField(self, "Minus")) or (self.HasAbility("Minus") and AbilityOnOwnField(self, "Plus"))):
                    modifier *= 1.5
                if (self.HasStatus("burned") and self.HasAbility("Flare Boost")):
                    modifier = 1.5
                modifier = RunItemFunction("checkingSpAtkStat", self, [modifier])
            elif (stat == Stats.SpecialDefense):
                if (self.HasType("Rock") and WeatherIs("sandstorm")):
                    modifier = 1.5
                modifier = RunItemFunction("checkingSpDefStat", self, [modifier])
            elif (stat == Stats.Defense):
                if (self.HasType("Ice") and WeatherIs("snowy")):
                    modifier *= 1.5
                modifier = RunItemFunction("checkingDefenseStat", self, [modifier])

            return rawstat * modifier

        def GetEV(self, stat):
            if (not self.HasStatus("transformed")):
                return self.EVs[stat]
            else:
                return self.GetStatusCount("transformed").GetEV(stat)

        def GetIV(self, stat):
            return self.IVs[stat]

        def GetMoves(self):
            if (self.HasStatus("mimicking")):
                moveslist = []
                for move in self.Moves:
                    if (move.Name != "Mimic"):
                        moveslist.append(move)
                moveslist.append(self.GetStatusCount("mimicking"))
                return moveslist
            return self.Moves

        def GetMoveNames(self):
            movenames = []
            for move in self.Moves:
                movenames.append(move.Name)
            return movenames

        def GetMove(self, moveid):
            return self.GetMoves()[moveid]

        def GetMoveByName(self, movename):
            for move in self.Moves:
                if (move.Name == movename):
                    return move
            return None

        def HasPPLeft(self):
            for mymove in self.Moves:
                if (mymove.PP > 0):
                    return True
            return False

        def HasFullPP(self):
            for mymove in self.Moves:
                if (mymove.PP != mymove.MaxPP):
                    return False
            return True

        def GetNickname(self, affectedByIllusion = True):
            if not (self.HasStatus("illusion") and affectedByIllusion == True):
                nick = self.Nickname if self.Nickname != None else pokedexlookup(self.Id, DexMacros.Name)

                if ("♀" in nick):
                    nick = nick.replace("Nidoran♀", "Nidoran")

                if ("♂" in nick):
                    nick = nick.replace("Nidoran♂", "Nidoran")

                if (self.IsShiny()):
                    nick = "{font=fonts/DejaVuSans.ttf}{size=-5}✧{/size}{/font}" + nick
                
                return nick
            else:
                return self.GetStatusCount("illusion").GetNickname()

        def GetLevel(self):
            return self.Level

        def GetGender(self, affectedByIllusion = False):
            if (self.Gender == None):
                self.Gender = Genders.Unknown

            if (not self.HasStatus("transformed")):
                if affectedByIllusion and self.HasStatus("illusion"):
                    return self.GetStatusCount("illusion").Gender
                return self.Gender
            else:
                return self.GetStatusCount("transformed").Gender

        def GetAllStatChanges(self):
            if (not self.HasStatus("transformed")):
                return self.StatChanges
            else:
                return self.GetStatusCount("transformed").StatChanges

        def GetStatChanges(self, keyname):
            if (keyname in self.StatChanges):
                return self.StatChanges[keyname]
            else:
                return 0

        def GetTotalStatChanges(self, positiveonly=False):
            totalchanges = 0
            for keyname in self.GetAllStatChanges().keys():
                if (not positiveonly or self.GetStatChanges(keyname) > 0):
                    totalchanges += self.GetStatChanges(keyname)
            return totalchanges

        def GetMovePP(self, movename):
            for move in self.GetMoves():
                if (move.Name == movename):
                    return move.PP
            return 0

        def GetWeight(self):
            return max(0.2, pokedexlookup(self.GetId(), DexMacros.Weight) * (2.0 if self.HasAbility("Heavy Metal") else 1.0) - self.GetStatusCount("nimble") * 220)

        def ResetStatChanges(self):
            self.StatChanges = {}

        def ChangeStats(self, keyname, change, inflicter=None):
            if (self.GetHealthPercentage() <= 0):
                return ""
            
            selfinflicted = inflicter in [None, self]
            if (selfinflicted):
                inflicter = self

            if (inflicter != self and self.HasStatus("substitute") and not IsSoundMove(ActiveMove) and not inflicter.HasAbility("Infiltrator")):
                return "The substitute absorbed the stat changes!"

            if (self.HasAbility("Contrary")):
                change = -change
            elif (self.HasAbility("Simple")):
                change = math.floor(change * 2)

            if (change < 0 and not selfinflicted):
                if (self.HasType("Grass") and AbilityOnOwnField(self, "Flower Veil")):
                    return "The Flower Veil prevented the stat decreases!"
                elif (EffectOnOwnField(self, "mist") and not inflicter.HasAbility("Infiltrator")):
                    return "The Mist prevented the stat decreases!"
                elif (self.HasAbility("White Smoke")):
                    return "The White Smoke prevented the stat decreases!"
                elif (self.HasAbility("Clear Body")):
                    return "{}'s Clear Body can't be blemished!".format(self.GetNickname())
                elif (keyname == Stats.Attack and self.HasAbility("Hyper Cutter")):
                    return "{} is a Hyper Cutter!".format(self.GetNickname())
                elif (keyname == Stats.Defense and self.HasAbility("Big Pecks")):
                    return "{} has Big Pecks!".format(self.GetNickname())
                elif (keyname == Stats.Accuracy and self.HasAbility("Keen Eye")):
                    return "{} has Keen Eyes!".format(self.GetNickname())
            if (keyname in self.StatChanges):
                if (change > 0 and self.StatChanges[keyname] == 6):
                    return "¡{} {} no puede subir más!".format(self.GetNickname(), StatToString(keyname))
                elif (change < 0 and self.StatChanges[keyname] == -6):
                    return "¡{} {} no puede disminuir más!".format(self.GetNickname(), StatToString(keyname))
                else:
                    returnable = "¡El {} de {} {}!".format(StatToString(keyname), self.GetNickname(), ("aumento" if change > 0 else "disminuyo")) 
                    self.StatChanges[keyname] += change
                    if (self.StatChanges[keyname] == 0):
                        del self.StatChanges[keyname]
                    renpy.sound.play(("audio/Stat_Increase.ogg" if change > 0 else "audio/Stat_Decrease.ogg"))
                    if (change < 0 and not selfinflicted):
                        if (self.HasAbility("Defiant")):
                            returnable += " " + self.ChangeStats(Stats.Attack, 2)
                        elif (self.HasAbility("Competitive")):
                            returnable += " " + self.ChangeStats(Stats.SpecialAttack, 2)
                    
                    deletechanges = []
                    for stat in self.StatChanges.keys():
                        self.StatChanges[stat] = max(min(self.StatChanges[stat], 6), -6)
                        if (self.StatChanges[stat] == 0):
                            deletechanges.append(stat)

                    for stat in deletechanges:
                        del self.StatChanges[stat]
                    
                    return returnable 
            else:
                renpy.sound.play(("audio/Stat_Increase.ogg" if change > 0 else "audio/Stat_Decrease.ogg"))
                self.StatChanges[keyname] = change
                returnable = "¡{} {} de {} {}!".format(stat_pronoun.get(StatToString(keyname)), StatToString(keyname), self.GetNickname(), ("aumento" if change > 0 else "disminuyo")) 
                if (change < 0 and not selfinflicted):
                    if (self.HasAbility("Defiant")):
                        returnable += " " + self.ChangeStats(Stats.Attack, 2)
                    elif (self.HasAbility("Competitive")):
                        returnable += " " + self.ChangeStats(Stats.SpecialAttack, 2)
                
                deletechanges = []
                for stat in self.StatChanges.keys():
                    self.StatChanges[stat] = max(min(self.StatChanges[stat], 6), -6)
                    if (self.StatChanges[stat] == 0):
                        deletechanges.append(stat)

                for stat in deletechanges:
                    del self.StatChanges[stat]
                
                return returnable

        def GetTeraType(self):
            if (not hasattr(self, 'TeraType')):
                self.TeraType = pokedexlookup(self.GetId(), DexMacros.Type1)
            return self.TeraType

        def GetTerastallized(self):
            if (not hasattr(self, 'Terastallized')):
                self.Terastallized = -1
            return self.Terastallized

        def IsTerad(self):
            return self.GetTerastallized() != -1

        def GetTypes(self, raw=False, ignoreTera=False, pureraw = False):
            types = []
            if (pureraw):
                raw = True
            if (not self.IsTerad() or ignoreTera or raw):
                if (self.GetId() == 25.2 and not pureraw):
                    if (libtypes == []):
                        for fvl in self.GetForeverals():
                            types.append(pokedexlookupname(GetForeveralMonname(fvl), DexMacros.Type1))
                        if (types == []):
                            types = ["Electric"]
                    else:
                        for element in libtypes:
                            types.append(element)
                else:
                    types.append(pokedexlookup(self.GetId(), DexMacros.Type1))
                    type2 = pokedexlookup(self.GetId(), DexMacros.Type2)
                    if (type2 != None):
                        types.append(type2)
                if (raw):
                    return types
                for fvl in self.GetForeverals():
                    if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.AddType):
                        types = types + lookupforeveraldata(fvl, FVLMacros.FVLTypeData)
                    elif (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.ReplaceType):
                        for replacetype, newtype in lookupforeveraldata(fvl, FVLMacros.FVLTypeData):
                            if (replacetype in types):
                                types.remove(replacetype)
                                types.append(newtype)
                if (self.HasAbility("Mimicry", False)):
                    if (BattlefieldExists("Misty Terrain")):
                        return ["Fairy"]
                    elif (BattlefieldExists("Grassy Terrain")):
                        return ["Grass"]
                    elif (BattlefieldExists("Electric Terrain")):
                        return ["Electric"]
                    elif (BattlefieldExists("Psychic Terrain")):
                        return ["Psychic"]
                    elif (BattlefieldExists("Burial Ground")):
                        return ["Ground", "Ghost"]
            else:
                types.append(self.GetTeraType())

            if (BattlefieldExists("Simple World") and IsGroundedSimpleWorld(self, "Flying" in types)):
                types = ["Normal"]
            if (self.HasStatus("trick-or-treating")):
                types.append("Ghost")
            elif (self.HasStatus("forest curse")):
                types.append("Grass")
            if (self.HasStatus("metallic")):
                types.append("Steel")
            if (self.HasStatus("roosted") and "Flying" in types):
                types.remove("Flying")
            if (self.HasStatus("camouflaged")):
                types = [self.GetStatusCount("camouflaged")]
            if (self.HasStatus("colorized")):
                types = [self.GetStatusCount("colorized")]
            if (self.HasStatus("versatile")):
                types = [self.GetStatusCount("versatile")]
            if (self.HasStatus("soaked")):
                types = ["Water"]
            if (self.HasStatus("burnt out") and "Fire" in types):
                types.remove("Fire")

            if (self.HasStatus("satiated")):
                if (len(types) > 1):
                    types[1] = self.GetStatusCount("satiated")
                else:
                    types.append(self.GetStatusCount("satiated"))

            return types

        def HasType(self, element):
            return element in self.GetTypes()

        def HasAbility(self, abilityname, triggersplash=True):
            fvlability = False
            for fvl in self.GetForeverals():
                if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.AddAbility and abilityname in lookupforeveraldata(fvl, FVLMacros.FVLTypeData)):
                    fvlability = True
            if (self.GetAbility() == abilityname or fvlability):
                foeignoringabilities = UsingMove and MoveUser != None and MoveUser != self and MoveUser.HasAbility("Mold Breaker")

                if (foeignoringabilities and self.GetAbility() not in ["Prism Armor"]):
                    return False

                if (triggersplash):
                    if (self in FriendlyPokemon()):
                        renpy.hide_screen("abilitysplashleft")
                        renpy.show_screen("abilitysplashleft", (self.GetNickname(False), abilityname))
                    else:
                        renpy.hide_screen("abilitysplashright")
                        renpy.show_screen("abilitysplashright", (self.GetNickname(False), abilityname))
                return True
            return False 

        def UpdateLevel(self, level, updateMoves=True, force=False, intellect=True):
            if (level + self.GetOffset() > self.Level or force):
                self.Level = min(100, max(1, level + self.GetOffset()))
                if (updateMoves):
                    self.Moves = GetMovesForLevel(self)
            if (intellect):
                self.Intelligence = self.Level >= 15
            self.Experience = self.CalculateAllExperienceNeededForLevel(self.Level)
            self.RecalculateStats()

        def UpdateMoves(self, moves):
            newmoves = []
            for move in moves:
                if (move in self.GetMoveNames()):
                    newmoves.append(self.GetMoveByName(move))
                else:
                    if (isinstance(move, str)):
                        newmoves.append(GetMove(move))
                    else:
                        newmoves.append(GetMove(move.Name))
            self.Moves = newmoves

        def Heal(self):
            self.AdjustHealth(self.GetStat(Stats.Health), absolute = True)
            self.ClearStatus("All", all=True)
            self.ResetStatChanges()
            self.ResetFaintedTurn()
            for move in self.GetMoves():
                move.PP = move.MaxPP

        def GetAbilities(self):
            fvlabilities = []
            for fvl in self.GetForeverals():
                if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.AddAbility):
                    fvlabilities += lookupforeveraldata(fvl, FVLMacros.FVLTypeData)
            fvlabilities += [self.GetAbility()]
            return fvlabilities

        def GetAbility(self):
            ownability = self.Ability
            if (self.GetAbilityOverride() != None):
                ownability = self.GetAbilityOverride()
            tracedability = self.GetStatusCount(".tracing")
            alchemizedability = self.GetStatusCount("alchemized")
            if (alchemizedability != 0):
                ownability = alchemizedability
            if (tracedability != 0):
                ownability = tracedability
            if (self.HasStatus("worried")):
                ownability = "Insomnia"
            if (self.HasStatus("simplified")):
                ownability = "Simple"
            return ownability

        def GetAbilityOverride(self):
            if (not hasattr(self, 'AbilityOverride')):
                self.AbilityOverride = None
            return self.AbilityOverride

        def ChangeForme(self, formename, revert=False):#reactivateAbilityEvenOnRevert=False
            self.ClearStatus("soaked")
            self.Changedformename = formename
            if (formename == self.Id):
                revert = True
            if (revert):
                self.Image = None
                self.FormeOverride = None
                self.AbilityOverride = None
                if (self.Id == 132): # Readd Transform if it's Ditto
                    self.Moves = []
                    relearnTransform = GetMove("Transform")
                    if (not hasattr(self, 'TransformPP')):
                        self.TransformPP = 10
                    relearnTransform.PP = self.TransformPP
                    self.Moves.append(relearnTransform)
            elif (isinstance(formename, float) or isinstance(formename, int)):
                self.FormeOverride = formename
                oldabilityslot = GetAbilities(self.Id).index(self.Ability)
                self.AbilityOverride = GetAbilities(self.GetId())[min(oldabilityslot, len(GetAbilities(self.GetId())) - 1)]
            elif (formename == "Minior (Meteor Form)"):
                self.Image = None
                self.FormeOverride = 774
            elif (formename == "Minior (Red Core)"):
                self.Image = "Pokemon/774-red.webp"
                self.FormeOverride = 774.1
            elif (formename == "Minior (Orange Core)"):
                self.Image = "Pokemon/774-orange.webp"
                self.FormeOverride = 774.1
            elif (formename == "Minior (Yellow Core)"):
                self.Image = "Pokemon/774-yellow.webp"
                self.FormeOverride = 774.1
            elif (formename == "Minior (Green Core)"):
                self.Image = "Pokemon/774-green.webp"
                self.FormeOverride = 774.1
            elif (formename == "Minior (Blue Core)"):
                self.Image = "Pokemon/774-blue.webp"
                self.FormeOverride = 774.1
            elif (formename == "Minior (Indigo Core)"):
                self.Image = "Pokemon/774-indigo.webp"
                self.FormeOverride = 774.1
            elif (formename == "Minior (Violet Core)"):
                self.Image = "Pokemon/774-violet.webp"
                self.FormeOverride = 774.1
            elif (formename == "Wishiwashi (School Form)"):
                self.FormeOverride = 746.1
            elif (formename == "Castform (Rainy Form)"):
                self.FormeOverride = 351.2
            elif (formename == "Castform (Sunny Form)"):
                self.FormeOverride = 351.1
            elif (formename == "Castform (Snowy Form)"):
                self.FormeOverride = 351.3
            elif (formename == "Castform (Normal)"):
                self.FormeOverride = 351
            elif (formename == "Darmanitan (Standard Mode)"):
                self.FormeOverride = 555
            elif (formename == "Darmanitan (Zen Mode)"):
                self.FormeOverride = 555.1
            elif (formename == "Burmy (Plant Cloak)"):
                self.FormeOverride = 412
            elif (formename == "Burmy (Sandy Cloak)"):
                self.FormeOverride = 412.1
            elif (formename == "Burmy (Trash Cloak)"):
                self.FormeOverride = 412.2
            elif (formename == "Rotom (Rotom)"):
                self.FormeOverride = 479
            elif (formename == "Rotom (Heat Rotom)"):
                self.FormeOverride = 479.1
            elif (formename == "Rotom (Wash Rotom)"):
                self.FormeOverride = 479.2
            elif (formename == "Rotom (Frost Rotom)"):
                self.FormeOverride = 479.3
            elif (formename == "Rotom (Fan Rotom)"):
                self.FormeOverride = 479.4
            elif (formename == "Rotom (Mow Rotom)"):
                self.FormeOverride = 479.5
            elif (formename == "DittoTransform"):
                self.FormeOverride = self.GetStatusCount("transformed").GetId()
                self.AbilityOverride = self.GetStatusCount("transformed").GetAbility()
                self.Moves = []
                self.StatChanges = self.GetStatusCount("transformed").GetAllStatChanges()
                for learntmove in self.GetStatusCount("transformed").GetMoveNames():
                    newmoveobj = GetMove(learntmove)
                    self.Moves.append(newmoveobj)
                    if newmoveobj.PP > 5: # if the move has more than 5 PP, set it to 5
                        newmoveobj.PP = 5
            elif (formename == "Illusion"):
                self.Image = self.GetStatusCount("illusion").GetImage()
            else:
                self.Image = None

            self.RecalculateStats(False)

            if (math.floor(self.GetId()) == 479):# rotom move changes
                removemove = None
                oldpp = -1
                for move in self.GetMoves():
                    if (move.Name in ["Air Slash", "Leaf Storm", "Overheat", "Hydro Pump", "Blizzard"]):
                        removemove = move
                        oldpp = removemove.PP
                        self.Moves.remove(removemove)
                        break
                if (self.Moves == []):
                    self.LearnNewMove([(0, "Thunder Shock")])
                if (self.GetId() == 479.1):
                    self.LearnNewMove([(0, "Overheat")])
                elif (self.GetId() == 479.2):
                    self.LearnNewMove([(0, "Hydro Pump")])
                elif (self.GetId() == 479.3):
                    self.LearnNewMove([(0, "Blizzard")])
                elif (self.GetId() == 479.4):
                    self.LearnNewMove([(0, "Air Slash")])
                elif (self.GetId() == 479.5):
                    self.LearnNewMove([(0, "Leaf Storm")])
                if (oldpp != -1):
                    self.GetMoves()[len(self.GetMoves()) - 1].PP = oldpp

            if (self.Id == pokedexlookupname("Eevee", DexMacros.Id) and self.HasAbility("Tetra Element") and not revert):
                removemove = None
                for move in self.GetMoves():
                    if (move.Name in ["Swift", "Leaf Blade", "Flare Blitz", "Surf", "Thunderbolt", "Ice Beam", "Moonblast", "Foul Play", "Psychic"]):
                        self.Moves.remove(move)
                        break
                self.Nickname = pokedexlookup(formename, DexMacros.Name)
                if (formename == pokedexlookupname("Flareon", DexMacros.Id)):
                    self.LearnNewMove([(0, "Flare Blitz")])
                elif (formename == pokedexlookupname("Vaporeon", DexMacros.Id)):
                    self.LearnNewMove([(0, "Surf")])
                elif (formename == pokedexlookupname("Jolteon", DexMacros.Id)):
                    self.LearnNewMove([(0, "Thunderbolt")])
                elif (formename == pokedexlookupname("Espeon", DexMacros.Id)):
                    self.LearnNewMove([(0, "Psychic")])
                elif (formename == pokedexlookupname("Umbreon", DexMacros.Id)):
                    self.LearnNewMove([(0, "Foul Play")])
                elif (formename == pokedexlookupname("Glaceon", DexMacros.Id)):
                    self.LearnNewMove([(0, "Ice Beam")])
                elif (formename == pokedexlookupname("Leafeon", DexMacros.Id)):
                    self.LearnNewMove([(0, "Leaf Blade")])
                elif (formename == pokedexlookupname("Sylveon", DexMacros.Id)):
                    self.LearnNewMove([(0, "Moonblast")])
                elif (len(self.Moves) == 3):
                    self.LearnNewMove([(0, "Swift")])
                self.GetMoves()[len(self.GetMoves()) - 1].PP = 1

            self.HandleLiberationOverflow()

            return "{} changed forme!".format(self.GetNickname())

        def GetImage(self):
            seminvuls = ["diving", "airborne", "ethereal", "dug in"]
            for status in seminvuls:
                if (self.HasStatus(status)):
                    return "GFX/empty.webp"
            if (self.HasStatus("substitute")):
                return "Pokemon/substitute.webp"
            if (self.Image == None):
                image = None
                if (self.GetId() == 845):#cramorant's two forms
                    if (self.HasStatus("gulping")):
                        image = "Pokemon/845.1.webp"
                    elif (self.HasStatus("gorging")):
                        image = "Pokemon/845.2.webp"
                    else:
                        image = "Pokemon/845.webp"
                elif (self.GetId() == 25 and self.GetGender() == Genders.Female):
                    image = "Pokemon/25.1.webp"
                elif (self.Id == 25.2):
                    image = Composite((510, 510),
                        (0, 0), "Pokemon/25.2.webp",
                        (0, 0), Transform("Pokemon/25.2-1.webp", matrixcolor=TintMatrix(GetLiberaColor())),
                        (0, 0), Transform("Pokemon/25.2-2.webp", matrixcolor=TintMatrix(GetLiberaColor(False))))
                else:
                    image = "Pokemon/" + str(self.GetId()) + ".webp"
                if (not self.IsShiny()):
                    return image
                else:
                    return Transform(image, matrixcolor=SaturationMatrix(1.3) * HueMatrix(max(0.2, min(self.Personality, 0.8)) * 360.0))
            else: 
                return self.Image

        def GetMiniorForme(self):
            if (self.Personality < 1.0/7.0):
                return "Minior (Red Core)"
            elif (self.Personality < 2.0/7.0):
                return "Minior (Orange Core)"
            elif (self.Personality < 3.0/7.0):
                return "Minior (Yellow Core)"
            elif (self.Personality < 4.0/7.0):
                return "Minior (Green Core)"
            elif (self.Personality < 5.0/7.0):
                return "Minior (Blue Core)"
            elif (self.Personality < 6.0/7.0):
                return "Minior (Indigo Core)"
            else:
                return "Minior (Violet Core)"

        def GetExperience(self):
            if (not hasattr(self, 'Experience')):
                self.Experience = self.CalculateAllExperienceNeededForLevel(self.Level)
            return (self.Experience if self.Experience != None else CalculateAllExperienceNeededForLevel(self.GetLevel()))

        def GetTrainer(self):
            return self.Owner

        def GetTrainerType(self):
            return self.TrainerType

        def PlayCry(self):
            if self.HasStatus("illusion"):
                self = self.GetStatusCount("illusion")
            if renpy.exists("pokemon/cries/{}.mp3".format(self.GetId())):
                PlaySound("pokemon/cries/{}.mp3".format(self.GetId()), otherchannel="altcry")
            else:
                PlaySound("pokemon/cries/{}.mp3".format(math.floor(self.GetId())), otherchannel="altcry")

        def GetSpeciesname(self):
            return pokedexlookup(self.Id, DexMacros.Name)
