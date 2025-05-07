init python:
    def ApplyForeveralLoadout(mon, dic):
        if not isinstance(mon, Pokemon):
            raise ValueError("{} is not a Pokemon object.".format(mon))
        if mon not in playerparty:
            raise ValueError("Can't modify Pokemon not in party.")
        if not dic["moves"] or not isinstance(dic["moves"], (list, tuple)):
            raise ValueError("Invalid moves.")
        
        if set(dic["moves"]) != set(mon.GetMoveNames()):
            sum_pp = sum([mv.PP for mv in mon.Moves])
            avg_pp = sum_pp // len(mon.Moves)
            
            new_move_objs = []
            move_obj = None
            for movename in dic["moves"]:
                move_obj = GetMove(movename)
                move_obj.PP = min(avg_pp, move_obj.MaxPP)
                new_move_objs.append(move_obj)
            
            mon.Moves = new_move_objs
            renpy.show_screen("generalsplashleft", "{}'s moves' PP balanced.".format(mon.GetNickname()))

        if "fvls" in dic and dic["fvls"]: # If I should make sure the FVL is equipped
            whohasfvls = WhoHasFVLs(True)
            for fvl, who in whohasfvls.items():
                if fvl not in dic["fvls"]: # We only want the relevant FVL
                    continue
                if not who[1]:
                    raise ValueError("Tried to remove FVL from `{}` who's in the PC.".format(who[0].GetNickname()))
                who[0].Foreverals.remove(fvl)
                foreveralinv.append(fvl)
                who[0].RecalculateStats()
            
            for fvl in mon.Foreverals:
                foreveralinv.append(fvl)

            mon.Foreverals = dic["fvls"]

            for fvl in dic["fvls"]:
                foreveralinv.remove(fvl)
        else: # If I should make sure the FVL is UNequipped
            for fvl in mon.Foreverals:
                foreveralinv.append(fvl)
            mon.Foreverals = []
        
        if "forme" in dic and dic["forme"] != mon.Id:
            mon.ChangeForme(dic["forme"])
        else:
            mon.ChangeForme(None, revert=True)
            mon.RecalculateStats()
    
    def GenerateCurrPokemonLoadout(mon):
        if not isinstance(mon, Pokemon):
            raise ValueError("{} is not a Pokemon object.".format(mon))
        
        return GeneratePikachuLoadout(None, mon.GetMoveNames(), copy.deepcopy(mon.GetForeverals()), copy.deepcopy(mon.GetFormeOverride()), direct_save=False)