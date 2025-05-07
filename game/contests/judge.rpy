init python:
    class Judge:
        def __init__(self, customcharacter, biases=None):
            self.CustomCharacter = customcharacter#the customcharacterobject that holds this character's stuff
            self.Name = customcharacter.name#a string that is the judge's name
            self.Sex = persondex[self.Name]["Sex"]#A Genders macro

            self.Seeking = None#A ContestMoveType macro
            self.JackpotLimit = 5# goes down to 1
            self.Sparks = 0#goes up to JackpotLimit

            self.Biases = biases

            if (not self.Biases):
                self.Biases = { ContestMoveType.Cute : 10, ContestMoveType.Beautiful : 10, ContestMoveType.Cool : 10, ContestMoveType.Clever : 10, ContestMoveType.Tough : 10 }

            self.LastSeekingDialog = []

        def GetImage(self):
            return self.CustomCharacter.image + " " + self.GetMood()

        def GetMood(self):
            sparkspercentage = self.GetSparks() / self.GetJackpotLimit()
            if (sparkspercentage >= 1):
                return "happy"
            elif (sparkspercentage >= .8):
                return "surprisedbrow happymouth"
            elif (sparkspercentage >= .6):
                return "closedbrow happymouth"
            elif (sparkspercentage >= .4):
                return "surprisedbrow"
            elif (sparkspercentage < 0):
                return "closedbrow sadmouth"
            else:
                return ""

        def SetSeeking(self):
            biasdict = copy.copy(self.Biases)
            for judge in Judges:
                sought = judge.GetSeeking()
                if (sought != None):
                    biasdict[sought] = 0
            self.Seeking = weighted_random_selection(biasdict)

        def GetSeeking(self):
            return self.Seeking

        def GetJackpotLimit(self):
            return self.JackpotLimit

        def GetSparks(self):
            return self.Sparks
            
        def GetName(self):
            return self.Name

        def IncreaseSparks(self):
            self.Sparks += 1

        def DecreaseSparks(self):
            self.Sparks -= 1
            if (self.Sparks < 0):
                self.Sparks = 0

        def ResetSparks(self):
            self.Sparks = 0
            self.JackpotLimit = max(1, self.GetJackpotLimit() - 1)
            self.SetSeeking()

        def GetSex(self):
            return self.Sex

        def GetHePronoun(self):
            return ("he" if self.GetSex() == Genders.Male else "she")

