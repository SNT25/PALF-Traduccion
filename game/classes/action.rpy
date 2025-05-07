init python:
    class Action:
        def __init__(self, priority, speed, actionType, userTrainer, user, move, targetTrainers, targets, turn, moveOwners = None):
            self.Priority = priority#int
            self.Speed = speed#int
            self.ActionType = actionType#ActionType Macro
            self.UserTrainer = userTrainer#Trainer Class
            self.User = user#Pokemon Class
            self.Move = move#Move Class OR None
            self.TargetTrainers = targetTrainers#[Trainer Class]
            self.Targets = targets#[Pokemon Class]
            self.Succeeded = True#bool
            self.Turn = turn#int
            self.MoveOwners = moveOwners if moveOwners != None else targets
            self.TargetSlots = GetSlots(self.MoveOwners)#[int] the slot the targets were in. Useful if the targets become invalid
            self.Performed = False

        def SetTarget(self, target):
            self.Target = target

        def GetPriority(self):
            return self.Priority

        def SetPriority(self, newpriority):
            self.Priority = newpriority

        def ChangePriority(self, prioritychange):
            self.Priority += prioritychange

        def GetSpeed(self):
            return self.Speed

        def SetSpeed(self, speed):
            self.Speed = speed

        def GetActionType(self):
            return self.ActionType

        def GetUser(self):
            return self.User

        def GetUserTrainer(self):
            return self.UserTrainer

        def GetTargets(self):
            return self.Targets
        
        def GetTargetTrainers(self):
            return self.TargetTrainers

        def GetMove(self):
            return self.Move

        def ChangeSuccess(self, success):
            self.Succeeded = success

        def GetSuccess(self):
            return self.Succeeded

        def GetTurn(self):
            return self.Turn

        def GetTargetSlots(self):
            targetslots = []
            for i, slot in enumerate(self.TargetSlots):
                if (self.Targets[i] != None and slot >= len(self.Targets[i].GetTrainer().GetLead())):
                    targetslots.append(len(self.Targets[i].GetTrainer().GetLead()) - 1)
                else:
                    targetslots.append(slot)
            return targetslots

        def GetPerformed(self):
            return self.Performed

        def SetPerformed(self):
            self.Performed = True
