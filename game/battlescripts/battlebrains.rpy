#battlebrains
init python:#brainaction makes the function return True or False, to determine whether to use the brain or not
    def dawndragonitebrain(pkmn):
        movechosen = ""
        if (pkmn.GetHealthPercentage() <= 0.2):
            return (Item.FullRestore, [pkmn])
        elif (pkmn.GetHealthPercentage() >= 0.66):
            if (pkmn.GetStatChanges(Stats.Defense) < 6):
                movechosen = "Cotton Guard"
            else:
                if (pkmn.GetMovePP("Hyper Voice") > 1):
                    movechosen = "Hyper Voice"
                else:
                    movechosen = "Dragon Pulse"
        else:
            movechosen = "Roost"

        return (movechosen, [FriendlyBattlers()[0]])

    def dawnpikachubrain(pkmn):
        movechosen = ""
        target = None
        usespreadmoves = False
        if ("Liberage" not in pikachuobj.GetMoveNames() and pkmn.GetHealthPercentage() <= 0.5):
            return (Item.FullRestore, [pkmn])
        elif ("Liberage" not in pikachuobj.GetMoveNames() and (pkmn.Moves[0].PP == 0 or pkmn.Moves[1].PP == 0 or pkmn.Moves[2].PP == 0 or pkmn.Moves[3].PP == 0)):
            return (Item.MaxElixir, [pkmn])
        elif (len(FriendlyBattlers()) == 2):
            noswitch = True
            for action in CurrentActions:
                if (action.GetActionType() == ActionTypes.Pokemon and action.GetTargets()[0].GetId() == 25):
                    noswitch = False
                    if (action.GetUser() == FriendlyBattlers()[0]):
                        target = [FriendlyBattlers()[1]]
                    else:
                        target = [FriendlyBattlers()[0]]
            if (target == None):
                if (noswitch and FriendlyBattlers()[0].GetId() == 292):#Shedinja continjancy
                    return ("Ominous Wind", [FriendlyBattlers()[0]])
                elif (noswitch and FriendlyBattlers()[1].GetId() == 292):#Shedinja continjancy part 2: the reckoning
                    return ("Ominous Wind", [FriendlyBattlers()[1]])
                elif (noswitch and FriendlyBattlers()[0].GetId() != 25 and FriendlyBattlers()[1].GetId() != 25):
                    usespreadmoves = True
                    target = [FriendlyBattlers()[0], FriendlyBattlers()[1]]
                elif (FriendlyBattlers()[0].GetId() == 25):
                    target = [FriendlyBattlers()[1]]
                elif (FriendlyBattlers()[1].GetId() == 25):
                    target = [FriendlyBattlers()[0]]
                else:
                    problematicmoves = ["Perish Song", "Metronome", "Leech Seed", "Dragon Rage", "Sand Attack", "Thunder Wave", "Thunder Shock", "Whirlwind", "Roar", "Toxic", "Bad Breath", "Poison Powder", "Poison Sting", "Sludge Bomb", "Ember", "Steady Flame", "Will-O-Wisp"]
                    for move in problematicmoves:
                        if (move in FriendlyBattlers()[0].GetMoveNames()):
                            target = [FriendlyBattlers()[0]]
                    if (target == None):
                        target = [FriendlyBattlers()[1]]
            maxbonus = 0
            maxmove = "Dragon Pulse"
            for move in pkmn.GetMoveNames():
                newbonus = GetTypeBonus(move, GetMove(move).Type, target[0], pkmn) * GetMove(move).Power
                
                if (MoveValid(pkmn, GetMove(move)) and newbonus > maxbonus and (move not in ["Earthquake", "Hyper Voice"] and not usespreadmoves or move in ["Earthquake", "Hyper Voice"] and usespreadmoves)):
                    maxmove = move
                    maxbonus = newbonus

            return (maxmove, target)

        else:
            target = FriendlyBattlers()[0]
            movechosen = None
            if (movesdodged.count("Dragon Pulse") < 5):
                movechosen = "Dragon Pulse"
            elif ("Earthquake" not in movesdodged):
                movechosen = "Earthquake"
            elif ("Ominous Wind" not in movesdodged):
                movechosen = "Ominous Wind"
            else:
                movechosen = "Hyper Voice"

            return (movechosen, [target])

    def jasminebrain1(pkmn):
        if (pkmn.GetNickname() in ["Magnemite", "Magneton", "Magnezone"]):
            if (HasAlly(pkmn, "Steelix") and not pkmn.HasStatus("levitating")):
                return ("Magnet Rise", [pkmn])
        elif (pkmn.GetNickname() in ["Pineco", "Forretress"]):
            if (HasAlly(pkmn, "Steelix") and not pkmn.HasStatus(".protections")):
                return ("Protect", [pkmn])

    def cherenbrain1(pkmn):
        if (pkmn.GetNickname() in ["Purrloin", "Liepard"] and MoveValid(pkmn, pkmn.GetMoveByName("Assist"))):
            return ("Assist", [pkmn])

    def oakkecleontestbrain(pkmn):
        return (pkmn.GetMoveNames()[0], [FriendlyBattlers()[0]])

    def oakkecleontestswitchbrain(trainer):
        for mon in trainer.GetUnfaintedTeam():
            if (mon.GetNickname() == "Tangela"):
                return mon
        return None#this just means it's giving up trying to make a choice, not that you switch in "nothing"

    def combeebrain(pkmn):
        if (pkmn.GetId() == 416):
            if (pkmn.GetHealthPercentage() <= 0.666):
                return ("Heal Order", [pkmn])
            elif (len(GetBattlers(pkmn)) < 3):
                return ("Defend Order", [pkmn])
        return None
