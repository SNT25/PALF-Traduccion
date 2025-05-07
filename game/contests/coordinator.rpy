init python:
    class CoordinatorGroup:
        def __init__(self, coordinators):
            self.Coordinators = coordinators
            self.ActionRecord = {}#has a series of entries, where the 'turns' are recorded. Each key is an int with the turn number, and the value is an int of how many points they won at end of turn. Turn zero is the initial condition factor
            self.CurrentPoints = 0
            self.MovesMade = { 0 : None }#has a series of entries, where the 'turns' are recorded. Each key is an int with the turn number, and the value is the name of the move used, or None
            self.ReactionNoted = False
            self.SuitabilityRecord = { 0 : 0 }
            self.PriorityAdjustment = 0
            self.Energy = 0
            self.SpendingEnergy = 0

        def GetPerformanceDialog(self, turn):
            return f"Placeholder text for turn {turn} and performer {self.GetName()}"

        def GetActions(self):
            return self.ActionRecord

        def GetAction(self, round):
            if (round in self.GetActions().keys()):
                return self.GetActions()[round]
            else:
                return 0

        def EvaluateCondition(self):
            totalcondition = 0
            for trainer in self.Coordinators:
                totalcondition += trainer.GetCondition()
            self.RecordRound(0, totalcondition)
            return self.GetAction(0)

        def GetPriority(self):
            return self.PriorityAdjustment

        def SetPriority(self, priority):
            self.PriorityAdjustment = priority

        def ResetPriority(self):
            self.SetPriority(0)

        def RecordRound(self, turn, points):
            self.ActionRecord[turn] = points

        def RecordMove(self, turn, movename):
            self.MovesMade[turn] = movename

        def RecordSuitability(self, turn, pts):
            self.SuitabilityRecord[turn] = pts

        def SumSuitability(self):
            total = 0
            for key, val in self.SuitabilityRecord.items():
                total += val
            return total

        def GetMoveRecord(self):
            return self.MovesMade

        def GetPointsOnTurn(self, turn):
            if (turn in self.ActionRecord):
                return self.ActionRecord[turn]
            else:
                return 0

        def NotReactionNoted(self):
            return not self.ReactionNoted

        def NoteReaction(self):
            self.ReactionNoted = True

        def UnNoteReaction(self):
            self.ReactionNoted = False

        def GetCoordinators(self):
            return self.Coordinators

        def GroupSize(self):
            return len(self.GetCoordinators())

        def GetHisPronoun(self):
            return ("his" if self.GetSex() == Genders.Male else ("her" if self.GetSex() == Genders.Female else "their"))
        
        def GetHimPronoun(self):
            return ("him" if self.GetSex() == Genders.Male else ("her" if self.GetSex() == Genders.Female else "them"))

        def IsGroup(self):
            return self.GroupSize() > 1

        def IsSolo(self):
            return not self.IsGroup()

        def IsProtag(self):
            for coordinator in self.GetCoordinators():
                if (coordinator.IsProtag()):
                    return True
            return False

        def GetName(self):
            if (not self.IsGroup()):
                return self.GetSoloCoordinator().GetName()
            else:
                names = [coordinator.GetName() for coordinator in coordinators]
                if len(names) == 2:
                    return " and ".join(names)
                else:
                    return ", ".join(names[:-1]) + ", and " + names[-1]

        def GetSoloCoordinator(self):
            if (self.IsGroup()):
                raise ValueError("Can't run 'GetSoloCoordinator' on group.")
            return self.GetCoordinators()[0]

        def GetImage(self, additionals="", overridemood=0):#1964x3316
            if (not self.IsGroup()):
                return self.GetSoloCoordinator().GetImage(additionals, overridemood)
            else:
                baseimage = Null()
                for i, coordinator in enumerate(self.GetCoordinators()):
                    baseimage = Composite((1964 + 1964 * 0.5 * (self.GroupSize() - 1), 3316),
                    (0, 0), baseimage,
                    (1964 * 0.5 * i, 0), coordinator.GetImage(additionals, overridemood))
                return baseimage

        def Reorder(self, mon):#this function puts the monster at the start of the getteam function
            leadercoord = None
            for coord in self.GetCoordinators():
                if (mon in coord.GetTeam()):
                    leadercoord = coord
                    break
            self.Coordinators.remove(leadercoord)
            self.Coordinators.insert(0, leadercoord)
            swapfrom = leadercoord.Trainer.GetTeam().index(mon)
            swapto = 0
            leadercoord.Trainer.ShiftTeam(swapto, swapfrom, force=True, positionswitch=False)

        def GetTeam(self):
            fulllist = []
            for coordinator in self.GetCoordinators():
                fulllist += coordinator.GetTeam()
            return fulllist

        def GetFirstMonName(self):
            return self.GetMon().GetNickname()

        def GetFirstMonSpeciesName(self):
            return pokedexlookup(self.GetMon().Id, DexMacros.Name)

        def GetSex(self):
            if (self.IsGroup()):
                return Genders.Unknown
            else:
                return self.GetSoloCoordinator().GetSex()

        def MultiplyCurrentPoints(self, multiple):
            self.CurrentPoints *= multiple

        def GetMon(self):
            return self.GetTeam()[0]

        def GetMoves(self):
            return self.GetMon().GetMoves()

        def CalculateMove(self, moveobj):
            contesttype = ContestStringToMacro(moveobj.Contest)
            effect = GetMoveContestEffect(moveobj)
            routine = effect == ContestEffects.Unjammable
            jams = effect == ContestEffects.Jamming
            index = Coordinators.index(self)

            pointevaluation = 6

            if (index < 2 and routine):
                pointevaluation += 3
            elif (routine):
                pointevaluation -= 1

            if (index > 2 and jams):
                pointevaluation += 3
            elif (jams):
                pointevaluation -= 1

            for i, judge in enumerate(Judges):
                if (contesttype == judge.GetSeeking()):
                    pointevaluation += 5 * (judge.GetSparks() + 1)
                    if (judge.GetJackpotLimit() - judge.GetSparks() == 1 + index):
                        pointevaluation += (4 - index) * 10
                elif (IsUnappealing(judge.GetSeeking(), contesttype)):
                    pointevaluation -= 2 * (judge.GetSparks() + 1)

            if (RepeatedMove(self, Turn, moveobj)):
                pointevaluation -= 3

            pointevaluation = max(0, pointevaluation)

            return pointevaluation

        def AwardedPoints(self, points, judge):
            if (judge != None):
                index = Judges.index(judge)
                AnimateValueChange(points, (0.3 + index * 0.2, 0.25), changemood=False, pausing = (index == 2))
            else:
                index = Coordinators.index(self)
                AnimateValueChange(points, (((1 + index) / 6), 0.75), changemood=False, pausing=True)

            self.CurrentPoints += points

        def JamPoints(self):
            index = Coordinators.index(self)
            losepoints = min(-1, -math.floor(self.CurrentPoints / 3))
            AnimateValueChange(losepoints, (((1 + index) / 6), 0.75), changemood=False, pausing=True)
            self.CurrentPoints += losepoints

        def GetCurrentPoints(self):
            return self.CurrentPoints

        def ResetCurrentPoints(self):
            self.CurrentPoints = 0

        def GainEnergy(self):
            preenergy = self.Energy
            self.Energy = min(3, self.Energy + 1)
            return preenergy != self.Energy

        def GetEnergy(self):
            return self.Energy

        def ResetEnergy(self):
            self.Energy = 0

        def SetSpendingEnergy(self, val):
            self.SpendingEnergy = val

        def GetSpendingEnergy(self):
            return self.SpendingEnergy

    class Coordinator:
        def __init__(self, name, condition = 0, isprotag = False):
            self.Name = name#the coordinator's name, as read in the persondex
            if (not isprotag):
                self.Trainer = MakeTrainer(name)#the trainer object that contains all the expected information for a trainer
            else:
                self.Trainer = MakeRed()
            self.Condition = condition#basically their rizz score
            self.IsProtagonist = isprotag

        def GetCondition(self):
            return self.Condition

        def GetName(self):
            return self.Name

        def GetImage(self, additionals="", overridemood=0):
            return GetCharacterSprite(self.GetName(), overridemood, extras="contest" + " " + additionals, protag=self.IsProtagonist)

        def GetTeam(self):
            return self.Trainer.GetTeam()

        def GetSex(self):
            if (self.IsProtag()):
                return Genders.Male
            return persondex[self.GetName()]["Sex"]

        def IsProtag(self):
            return self.IsProtagonist
            

            
