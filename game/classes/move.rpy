init python:
    class Move:
        #movedex/      Name/Type/Category/Contest/PP/Power/Accuracy/Effect/Description
        #      0          1    2        3       4  5     6        7      8           9
        def __init__(self, id, name, element, category, contest, maxpp, power, accuracy, effect, description, pp=None):
            self.Id = id#int
            self.Name = name#string
            self.Type = element#string
            self.Category = category#string
            self.Contest = contest#string
            self.MaxPP = maxpp#int
            self.Power = power#power
            self.Accuracy = accuracy#int
            self.Effect = effect#Effect Macro
            self.Description = description#string
            self.PP = pp#int
            self.Range = GetMoveRange(self)#Range Macro

            if (not isinstance(self.Accuracy, float) and not isinstance(self.Accuracy, int) and not self.Accuracy in ["-", "?", "", "—", "~"]):
                print("Move " + self.Name + " has broken accuracy. Is \"" + str(self.Accuracy) + "\"." + "(Should be float 0-1 or int 1.) Fix it in the movedex.")

            if (not isinstance(self.Power, int)):
                print("Move " + self.Name + " has broken power. (Should be int.) Fix it in the movedex.")

            if (self.PP == None):
                self.PP = self.MaxPP

            #Translates move.
            if self.Name in translate_movedex:
                self.TranslatedName = translate_movedex[self.Name] [0]
                self.Description = translate_movedex[self.Name] [1]
            else: # If this happens, a move was not correctly translated. Setting as English.
                self. TranslatedName = self.Name
            self.Category = category_translation.get(category, category)

    hurtself = Move(999, "Buffet", "None", "Physical", "Tough", 99, 40, "—", -1, "Hit yourself in the face")
    struggle = Move(999, "Struggle", "None", "Physical", "Tough", 99, 50, 1, -1, "Vain struggling, when nothing else works.")