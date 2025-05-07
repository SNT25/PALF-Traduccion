init python:
    
    #### ---- OTHER HELPER STUFF ------ ####

    # This might actually be the dumbest function I've ever "written". ~Adingo
    def GetMaxForeveralCount():
        return 1

    #### ------ LOADOUT-SPECIFIC SORTING ------ ####
    # Parallels to foreveralsort and foreveralsortinverse, to ensure independence. As they're defined in init python, they're cross-use but aren't saved - and really, they shouldn't be saved.
    loadoutsortdict = {"Moves":["Límite", "Tipo", "Categoría", "Alfabético"], "Foreverals":["Dex Nacional", "Tipo", "Categoría", "Alfabético"], "Forms":["Dex Nacional", "Límite", "Tipo", "Alfabético"]}
    loadoutsort = "Límite"
    loadoutsortinverse = False
    loadoutscreen = "Loadouts"

    def LoadoutWhoHasFVLs(dic):
        fvlwho = {} # FVL : [holder, is in party]

        if "fvls" in dic: # Just do nothing if no "fvls" key, equivalent to empty list
            for fvl in dic["fvls"]:
                for mon in AllPokemon():
                    if mon is not pikachuobj and fvl in mon.GetForeverals():
                        fvlwho[fvl] = [mon, mon in playerparty]

        return fvlwho

    def WhoHasFVLs(includepika=False): # Independent of the above - returns everything
        fvlwho = {} # FVL : [holder, is in party]

        for fvl in claimedforeverals:
            for mon in AllPokemon():
                if (mon is not pikachuobj or includepika) and fvl in mon.GetForeverals():
                    fvlwho[fvl] = [mon, mon in playerparty]
        
        return fvlwho

    def LoadoutDiveralForms(dic, return_all=True, notpages=False): # All returns the entire list if true and it's empty otherwise.
        if "fvls" not in dic or not dic["fvls"]:
            return SortedLoadoutForms(notpages)

        divs = []
        for fvl in dic["fvls"]:
            if lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.FormSwap:
                for divid in lookupforeveraldata(fvl, FVLMacros.FVLTypeData):
                    divs.append((divid, fvl))

        return divs if divs or not return_all else SortedLoadoutForms(notpages)

    def LoadoutFVLWithForm(dic):
        if not LoadoutDiveralForms(dic, False) or ("forme" not in dic or not dic["forme"]):
            return SortedLoadoutForeverals()

        validfvls = []

        for fvl in claimedforeverals:
            if lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.FormSwap and dic["forme"] in lookupforeveraldata(fvl, FVLMacros.FVLTypeData):
                validfvls.append(fvl)
        
        return validfvls

    def SortedLoadoutForeverals():
        obtainfvldex = copy.deepcopy(claimedforeverals) # No need to remove anything, as this only contains owned stuff!

        if (loadoutsort == "National Dex"):
            obtainfvldex.sort(reverse = loadoutsortinverse, key=(lambda entry : pokedexlookupname(GetForeveralMonname(entry, True), DexMacros.Id)))
        elif (loadoutsort == "Type"):
            obtainfvldex.sort(reverse = loadoutsortinverse, key=(lambda entry : pokedexlookupname(GetForeveralMonname(entry, True), DexMacros.Type1)))
        elif (loadoutsort == "Category"):
            obtainfvldex.sort(reverse = loadoutsortinverse, key=(lambda entry : entry.replace(GetForeveralMonname(entry, False), "")))
        elif (loadoutsort == "Alphabetical"):
            obtainfvldex.sort(reverse = loadoutsortinverse, key=(lambda entry : entry))

        return obtainfvldex[foreveralpage * 20:foreveralpage * 20 + 20]

    def SortedLoadoutMoves():
        finallist = AllMoves()

        if (loadoutsort == "Type"):
            finallist.sort(reverse = loadoutsortinverse, key=(lambda entry : GetMove(entry[0]).Type))
        elif (loadoutsort == "Category"):
            finallist.sort(reverse = loadoutsortinverse, key=(lambda entry : GetMove(entry[0]).Category))
        elif (loadoutsort == "Alphabetical"):
            finallist.sort(reverse = loadoutsortinverse, key=(lambda entry : GetMove(entry[0]).Name))
        elif (loadoutsort == "Limit"):
            finallist.sort(reverse = loadoutsortinverse, key=(lambda entry : -GetCalculatedMovePower(entry[0])))

        return finallist[foreveralpage * 30:foreveralpage * 30 + 30]

    def SortedLoadoutForms(return_all=False):
        finallist = []
        for fvl in claimedforeverals:
            if ("Diveral" in fvl): # Only diveral-based forms are interesting in loadouts
                for mon in lookupforeveraldata(fvl, FVLMacros.FVLTypeData):
                    if (not isinstance(mon, str)):
                        finallist.append((mon, fvl))

        if (loadoutsort == "Type"):
            finallist.sort(reverse = loadoutsortinverse, key=(lambda entry : pokedexlookup(entry[0], DexMacros.Type1)))
        elif (loadoutsort == "National Dex"):
            finallist.sort(reverse = loadoutsortinverse, key=(lambda entry : entry[0]))
        elif (loadoutsort == "Category"):
            finallist.sort(reverse = loadoutsortinverse, key=(lambda entry : entry[1]))
        elif (loadoutsort == "Alphabetical"):
            finallist.sort(reverse = loadoutsortinverse, key=(lambda entry : pokedexlookup(entry[0], DexMacros.Name)))
        elif (loadoutsort == "Limit"):
            finallist.sort(reverse = loadoutsortinverse, key=(lambda entry : -pokedexlookup(entry[0], DexMacros.Total)))
        
        if return_all:
            return finallist
        return finallist[foreveralpage * 20:foreveralpage * 20 + 20]


    #### ------ LOADOUT MANAGEMENT ------ ####

    def SavePikachuLoadout(name, dic):
        pika_loadouts[name] = dic
    
    def DeletePikachuLoadout(name):
        if name in pika_loadouts:
            del pika_loadouts[name]
    
    def RenamePikachuLoadout(old, new):
        if old not in pika_loadouts:
            raise KeyError("Loadout named `{}` doesn't exist.".format(old))
        if new in pika_loadouts:
            raise KeyError("Loadout named `{}` already exists.".format(new))
        new_loadout = pika_loadouts[old]
        del pika_loadouts[old]
        pika_loadouts[new] = new_loadout
    
    def PromptLoadoutSave(dic): # old is an existing loadout's name, if renaming a loadout.
        name = renpy.input("Please enter the loadout's name:", exclude="{}[[]%<>", length=12)
        overwrite = True
        if name in pika_loadouts:
            overwrite = renpy.confirm("Are you sure you want to overwrite loadout `{}`?".format(name))
        
        if overwrite:
            SavePikachuLoadout(name, dic)
        
    def PromptLoadoutRename(old, new):
        if old not in pika_loadouts:
            raise ValueError("Key `{}` isn't a loadout name.".format(old))
        
        confirm = renpy.confirm("Are you sure you want to rename loadout `{}`?".format(old))

        if not confirm:
            return

        name = renpy.input("Please enter the loadout's new name:", exclude="{}[[]%<>", length=12)

        while name in pika_loadouts: # If new name is already there, see how to handle this. Input until not in there?
            break
        
        RenamePikachuLoadout(old, new)

    def PromptLoadoutDelete(name):
        if name not in pika_loadouts:
            raise ValueError("There is no loadout `{}` to delete.".format(name))
        
        if renpy.confirm("Are you sure you want to delete loadout `{}`?".format(name)):
            DeletePikachuLoadout(name)


    # Only one of fvl or forme may be not-None - one is for the FVL, one is for a diveral forme change.
    def GeneratePikachuLoadout(name, moves, fvls = [], forme = None, direct_save=True):
        # Data validation - ensure that if there's a forme provided, one of the provided everals is a diveral providing it
        if fvls and forme:
            found_div = False
            for fvl in fvls:
                if lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.FormSwap:
                    if forme in lookupforeveraldata(fvl, FVLMacros.FVLTypeData):
                        found_div = True
                        break
            
            if not found_div:
                raise ValueError("Forme ID {} cannot be supplied by any foreveral from {}".format(forme, fvls))
        
        # Data validation - no empty moveset
        if not moves or not isinstance(moves, (list, tuple)):
            raise ValueError("Empty or non-list or tuple moveset provided.")

        loadout_dict = {}
        loadout_dict["moves"] = moves
        if fvls:
            loadout_dict["fvls"] = fvls
        if forme:
            loadout_dict["forme"] = forme
        
        if name == None:
            direct_save = False
        
        if direct_save:
            SavePikachuLoadout(name, loadout_dict)
        
        return loadout_dict
    
    def GenerateCurrPikachuLoadout(name=None, direct_save=True):
        return GeneratePikachuLoadout(name, pikachuobj.GetMoveNames(), copy.deepcopy(pikachuobj.GetForeverals()), copy.deepcopy(pikachuobj.GetFormeOverride()), direct_save=direct_save)

    def ApplyPikachuLoadout(name):
        if name not in pika_loadouts.keys():
            raise ValueError("Loadout name `{}` doesn't exist.".format(name))
        
        if set(pika_loadouts[name]["moves"]) != set(pikachuobj.GetMoveNames()):
            sum_pp = sum([mv.PP for mv in pikachuobj.Moves])
            avg_pp = sum_pp // len(pikachuobj.Moves)

            new_move_objs = []
            move_obj = None
            for movename in pika_loadouts[name]["moves"]:
                move_obj = GetMove(movename)
                move_obj.PP = min(avg_pp, move_obj.MaxPP)
                new_move_objs.append(move_obj)

            pikachuobj.Moves = new_move_objs
            renpy.show_screen("generalsplashleft", "{}'s moves' PP balanced.".format(pikachuobj.GetNickname()))

        if "fvls" in pika_loadouts[name]:
            whohasfvls = LoadoutWhoHasFVLs(pika_loadouts[name])
            for fvl, who in whohasfvls.items():
                if not who[1]:
                    raise ValueError("Tried to remove FVL from `{}` who's in the PC.".format(who[0].GetNickname()))
                who[0].Foreverals.remove(fvl)
                foreveralinv.append(fvl)
                who[0].RecalculateStats()
            
            for fvl in pikachuobj.Foreverals:
                foreveralinv.append(fvl)
            
            pikachuobj.Foreverals = pika_loadouts[name]["fvls"]
            
            for fvl in pika_loadouts[name]["fvls"]:
                foreveralinv.remove(fvl)
        else:
            for fvl in pikachuobj.Foreverals:
                foreveralinv.append(fvl)
            pikachuobj.Foreverals = []
        
        if "forme" in pika_loadouts[name] and pika_loadouts[name]["forme"] is not None: # To ensure revert is called with reverting in the case of pika_loadouts[name]["forme"] = None
            pikachuobj.ChangeForme(pika_loadouts[name]["forme"])
        else:
            pikachuobj.ChangeForme(None, revert=True)
            pikachuobj.RecalculateStats()
    
    def ApplyNamelessPikachuLoadout(dic):
        if not isinstance(dic, dict):
            raise TypeError("Parameter {} is not a dictionary.".format(dic))
        
        if "moves" not in dic.keys():
            raise ValueError("No `moves` key in dict {}".format(dic))
        
        if not dic["moves"]:
            raise ValueError("No moves supplied by dict {}".format(dic))
        
        if set(dic["moves"]) != set(pikachuobj.GetMoveNames()):
            sum_pp = sum([mv.PP for mv in pikachuobj.Moves])
            avg_pp = sum_pp // len(pikachuobj.Moves)

            new_move_objs = []
            move_obj = None
            for movename in dic["moves"]:
                move_obj = GetMove(movename)
                move_obj.PP = min(avg_pp, move_obj.MaxPP)
                new_move_objs.append(move_obj)

            pikachuobj.Moves = new_move_objs
            renpy.show_screen("generalsplashleft", "{}'s moves' PP balanced.".format(pikachuobj.GetNickname()))

        if "fvls" in dic: # if no FVLs, dic["fvls"] may be [], which is functionally identical to no fvls key at all
            whohasfvls = LoadoutWhoHasFVLs(dic)
            for fvl, who in whohasfvls.items():
                if not who[1]:
                    raise ValueError("Tried to remove FVL from `{}` who's in the PC.".format(who[0].GetNickname()))
                who[0].Foreverals.remove(fvl)
                foreveralinv.append(fvl)
                who[0].RecalculateStats()
            
            for fvl in pikachuobj.Foreverals:
                foreveralinv.append(fvl)

            pikachuobj.Foreverals = dic["fvls"]

            for fvl in dic["fvls"]:
                if (fvl in foreveralinv):
                    foreveralinv.remove(fvl)
        else:
            for fvl in pikachuobj.Foreverals:
                foreveralinv.append(fvl)
            pikachuobj.Foreverals = []
        
        if "forme" in dic and dic["forme"] is not None: # To ensure revert is called with reverting in the case of dic["forme"] = None
            pikachuobj.ChangeForme(dic["forme"])
        else:
            pikachuobj.ChangeForme(None, revert=True)
            pikachuobj.RecalculateStats()
    
    def GetLiberationLimitFromLoadout(dic):#returns a tuple with the raw value and a breakdown. Copypasta'd and modified from GetLiberationLimit.
        if (not usingliberationlimit):
            return (0, [])
        ll = 0
        breakdown = []
        for move in dic["moves"]:
            newpower = GetCalculatedMovePower(move)
            ll += newpower
            breakdown.append(("Move", move, newpower))#"Move", movename, ll increase
        if ("forme" in dic and dic["forme"] and ("fvls" not in dic or dic["fvls"] == [])):
            scalingmonbst = pokedexlookup(dic["forme"], DexMacros.Total)
            bstfifth = math.floor(scalingmonbst / 5)
            ll += bstfifth
            breakdown.append(("Diveral", dic["forme"], bstfifth))#"Diveral", mon diveral'd into, ll increase
        if "fvls" in dic:
            for fvl in dic["fvls"]:
                if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.Scaling):
                    scalingmon, scalinglevel = lookupforeveraldata(fvl, FVLMacros.FVLTypeData)
                    scalingmonbst = pokedexlookupname(scalingmon, DexMacros.Total)
                    bstfifth = scalingmonbst / 5
                    ll += bstfifth
                    breakdown.append(("Stat Scale", scalingmon, bstfifth))#"Stat Scale", mon scaling to id, ll increase
                elif (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.Mega):
                    scalingmon = lookupforeveraldata(fvl, FVLMacros.FVLTypeData)[1]
                    scalingmonbst = pokedexlookup(scalingmon, DexMacros.Total)
                    bstfifth = scalingmonbst / 5
                    ll += bstfifth
                    breakdown.append(("Transformation", scalingmon, bstfifth))#"Transformation", mon transforming into id, ll increase
                elif (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.FormSwap):
                    maxbst = 0
                    bestmon = 25.2
                    for mon in lookupforeveraldata(fvl, FVLMacros.FVLTypeData):
                        thisbst = pokedexlookup(mon, DexMacros.Total)
                        if (thisbst > maxbst):
                            maxbst = thisbst
                            bestmon = mon
                    bstfifth = maxbst / 5
                    ll += bstfifth
                    breakdown.append(("Transformation", bestmon, bstfifth))#"Transformation", mon transforming into id, ll increase
                else:
                    ll += 30
                    breakdown.append((fvl, pokedexlookupname(GetForeveralMonname(fvl, True), DexMacros.Id), 30))#fvl name, dummy value, ll increase
        return (math.floor(ll), breakdown)
