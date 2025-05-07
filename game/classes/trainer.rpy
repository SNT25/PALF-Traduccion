init python:
    def MakeRed(number=1):
        trainer1 = Trainer("red", TrainerType.Player, playerparty, number=number)
        for mon in playerparty:
            mon.Owner = trainer1
        return trainer1

    def MakeTrainer(trainername, trainertype = TrainerType.Enemy, number=1):
        trainer1 = Trainer(trainername.lower(), trainertype, GetTrainerTeam(trainername.title()), number=number)
        for mon in trainer1.GetTeam():
            mon.Owner = trainer1
        return trainer1

    class Trainer:
        def __init__(self, name, trainertype, team, number=1, isPokemon=False, ignoresDungeons=False):
            self.Name = name.lower()#string
            self.Team = team#[Pokemon]
            self.Type = trainertype#TrainerType macro
            self.Number = number#1 for single battle, 2 for double, 3 for triple
            self.IsPokemon = isPokemon
            self.Motivation = 0#used in squad battles
            self.IgnoresDungeons = ignoresDungeons#ignores the cap of one 'mon in dungeons

        def GetMotivation(self):
            return self.Motivation

        def GetSkills(self):
            if (self.GetFormatName() in squadstats.keys()):
                return squadstats[self.GetFormatName()]["Skills"]
            elif (self.Name == "red"):
                return dungeonskills
            else:
                return []

        def GetDungeonClass(self):
            if (self.GetFormatName() in squadstats.keys()):
                return squadstats[self.GetFormatName()]["Class"]
            elif (self.Name == "red"):
                return dungeonclass
            else:
                return "Commoner"

        def ChangeMotivation(self, motivationchange):
            if (not hasattr(self, 'Motivation')):
                self.Motivation = 0
            self.Motivation = min(5, max(0, self.Motivation + motivationchange))

        def GetIsPokemon(self):
            return self.IsPokemon

        def GetFormatName(self):
            if (self.Name == "red"):
                return first_name
            else:
                return self.Name.title()

        def GetName(self):
            return self.Name

        def ReorderTeam(self):
            fainteds = []
            for mon in self.GetTeam():
                if (mon.GetHealthPercentage() <= 0):
                    fainteds.append(mon)
            self.Team = self.GetUnfaintedTeam() + fainteds

        def GetLead(self, addNones=True):
            leads = self.Team[:self.Number]
            if (addNones):
                for i in range(len(leads)):
                    if (leads[i].GetHealth() <= 0):
                        leads[i] = None
            else:
                removelist = []
                for mon in leads:
                    if (mon.GetHealth() <= 0):
                        removelist.append(mon)
                for mon in removelist:
                    leads.remove(mon)
            return leads

        def GetDungeonTeam(self):
            if (self.Name == "red"):
                return [playerparty[0]]
            else:
                highestlevel = 0
                highestmon = None
                for mon in self.Team:
                    if (mon.GetLevel() > highestlevel):
                        highestmon = mon
                        highestlevel = mon.GetLevel()
                return [highestmon]

        def GetTeam(self, heal=False):
            if (self.Team == None):
                if (self.Name == "red"):
                    self.Team = playerparty
                else:
                    self.Team = GetTrainerTeam(self.Name, None, heal)
            if (InDungeon() and not self.GetIsPokemon() and not self.IgnoresDungeons):
                return self.GetDungeonTeam()
            else:
                return self.Team

        def GetUnfaintedTeam(self):
            unfainteds = []
            for mon in self.GetTeam():
                if (mon.GetHealth() > 0):
                    unfainteds.append(mon)
            return unfainteds

        def GetType(self):
            return self.Type

        def ShiftTeam(self, swapto, swapfrom, force=False, positionswitch = False):
            global switchedmon
            
            swappingmon = self.GetTeam()[swapto]
            swappingtomon = self.GetTeam()[swapfrom]
            
            if (not positionswitch):
                if (swappingtomon.GetHealth() <= 0):
                    renpy.say(None, "{} is fainted, and can't switch in!".format(swappingtomon.GetNickname()))
                    return False
                elif (not CanSwitch(swappingmon, force)):
                    renpy.say(None, "Can't switch in!")
                    return False

                if (swappingmon.GetHealthPercentage() > 0 and swappingmon.HasAbility("Regenerator")):
                    swappingmon.AdjustHealth(swappingmon.GetStat(Stats.Health) * 0.33)
                if (swappingmon.HasNormalStatus() and swappingmon.HasAbility("Natural Cure")):
                    swappingmon.ClearStatus(None, all=True)    
                    
                swappingmon.ClearStatus(None, volatiles=True)
                swappingtomon.ClearStatus(None, volatiles=True)

            self.GetTeam()[swapto], self.GetTeam()[swapfrom] = self.GetTeam()[swapfrom], self.GetTeam()[swapto]

            if (not positionswitch):
                for mon in Battlers():
                    if (mon.GetStatusCount("infatuated") == swappingmon):
                        mon.ClearStatus("infatuated")
                    if (mon.GetStatusCount("menaced") == swappingmon):
                        mon.ClearStatus("menaced")

            if (self.Name == "red"):
                switchedmon = True

            return True

        def HasMons(self):
            for mon in self.GetTeam():
                if (mon.GetHealth() != 0):
                    return True
            return False

        def GetNumber(self):
            return self.Number