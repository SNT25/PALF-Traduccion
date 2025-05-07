init python:
    class ContestEffects:
        Unjammable = "Unjammable"
        Jamming = "Jamming"
        Showoff = "Showoff"
        Soothe = "Soothe"
        Finale = "Finale"
        Spark = "Spark"
        Dull = "Dull"
        Sneaky = "Sneaky"
    
    class ContestMoveType:
        Cool = 0
        Beautiful = 1
        Cute = 2
        Clever = 3
        Tough = 4
    
    def ContestStringToMacro(conteststring):
        contesttypedict = {
            "Cool" : ContestMoveType.Cool,
            "Beautiful" : ContestMoveType.Beautiful,
            "Cute" : ContestMoveType.Cute,
            "Clever" : ContestMoveType.Clever,
            "Tough" : ContestMoveType.Tough,
        }
        return contesttypedict[conteststring]

    def weighted_random_selection(biases):
        # Get the keys and the weights from the dictionary
        move_types = list(biases.keys())
        weights = list(biases.values())
        
        # Ensure the total of weights is greater than zero
        total_weight = sum(weights)
        if total_weight <= 0:
            # Select a random move ignoring weights
            return random.choice(move_types)
        
        # Use random.choices to select a move type based on the weights
        selected_move = random.choices(move_types, weights=weights, k=1)[0]
        
        return selected_move

    def IsUnappealing(soughtcontesttype, actualcontesttype):
        if (soughtcontesttype == ContestMoveType.Cool):
            return actualcontesttype == ContestMoveType.Cute
        elif (soughtcontesttype == ContestMoveType.Cute):
            return actualcontesttype == ContestMoveType.Tough
        elif (soughtcontesttype == ContestMoveType.Tough):
            return actualcontesttype == ContestMoveType.Beautiful
        elif (soughtcontesttype == ContestMoveType.Beautiful):
            return actualcontesttype == ContestMoveType.Clever
        elif (soughtcontesttype == ContestMoveType.Clever):
            return actualcontesttype == ContestMoveType.Cool
    
    def Jams(soughtcontesttype, actualcontesttype):
        if (soughtcontesttype == ContestMoveType.Cool):
            return actualcontesttype in [ContestMoveType.Clever, ContestMoveType.Cute]
        elif (soughtcontesttype == ContestMoveType.Beautiful):
            return actualcontesttype in [ContestMoveType.Clever, ContestMoveType.Tough]
        elif (soughtcontesttype == ContestMoveType.Cute):
            return actualcontesttype in [ContestMoveType.Cool, ContestMoveType.Tough]
        elif (soughtcontesttype == ContestMoveType.Clever):
            return actualcontesttype in [ContestMoveType.Beautiful, ContestMoveType.Cool]
        elif (soughtcontesttype == ContestMoveType.Tough):
            return actualcontesttype in [ContestMoveType.Beautiful, ContestMoveType.Cute]

    def IsJammingMove(moveobj):
        return JamsAudio(moveobj) or JamsPhysical(moveobj) or JamsProps(moveobj)

    def EvaluateSuitability(pkmn, contestconditions):
        hastype = False
        for element in pkmn.GetTypes(pureraw=True):
            if element in contestconditions["Types"]:
                hastype = True
                break

        formename = pokedexlookup(pkmn.Id, DexMacros.Forme)
        override = -1
        if ("Kanto" in formename):
            override = 1
        elif ("Johto" in formename):
            override = 152
        elif ("Hoenn" in formename):
            override = 252
        elif ("Sinnoh" in formename):
            override = 387
        elif ("Unova" in formename):
            override = 494
        elif ("Kalos" in formename):
            override = 650
        elif ("Alola" in formename):
            override = 722
        elif ("Galar" in formename):
            override = 810
        elif ("Paldea" in formename):
            override = 906

        regioncheck = (pkmn.Id if override < 1 else override)
        if (pkmn.Id == 25.2):
            regioncheck = 494

        hasregion = contestconditions["Region"][0] <= regioncheck and regioncheck <= contestconditions["Region"][-1]

        hastrait = pokedexlookup(pkmn.Id, DexMacros.ContestTrait) in contestconditions["Traits"]

        return hastype + hasregion + hastrait

    #determines if a move is 'safe', and cannot be jammed in contests
    def IsRoutineMove(moveobj):
        return IsSliceMove(moveobj) or IsBiteMove(moveobj) or IsPunchMove(moveobj) or IsKickMove(moveobj)

    #determines if a move jams audio performances
    def JamsAudio(moveobj):
        return IsSoundMove(moveobj) or IsExplosion(moveobj) or IsWeatherMove(moveobj) or IsWindMove(moveobj)

    #determines if a move jams physical performances
    def JamsPhysical(moveobj):
        return IsDanceMove(moveobj) or IsRecklessMove(moveobj) or IsSwitchingMove(moveobj) or IsPriorityMove(moveobj)

    #determines if a move jams prop performances
    def JamsProps(moveobj):
        return IsAuraPulseMove(moveobj) or IsBallBombMove(moveobj) or IsChargeRechargeMove(moveobj) or IsPowderSporeMove(moveobj)

    def GetContestTypeColor(typestring):
        contesttypecolors = {
            "Cool": "#CE5343",
            "Beautiful": "#5AAFE6",
            "Cute": "#E66F91",
            "Clever": "#A1C319",
            "Tough": "#E5B43B",
            "???": "#000"
        }
        return contesttypecolors[typestring]

    def GetDimContestTypeColor(typestring):
        dimcontesttypecolors = {
            "Cool": "#943d31",
            "Beautiful": "#3f7ba3",
            "Cute": "#9c4a62",
            "Clever": "#607410",
            "Tough": "#9a7927",
            "???": "#000"
        }

        return dimcontesttypecolors[typestring]

    def RepeatedMove(coordinator, turn, moveobj):
        return coordinator.GetMoveRecord()[turn - 1] == moveobj.Name

    def GetMoveContestEffect(moveobj):
        if (IsRoutineMove(moveobj)):
            return ContestEffects.Unjammable
        elif (IsJammingMove(moveobj)):
            return ContestEffects.Jamming
        elif (moveobj.Type in ["Ice", "Fairy", "Fire"]):
            return ContestEffects.Showoff
        elif (moveobj.Type in ["Water", "Grass", "Psychic"]):
            return ContestEffects.Soothe
        elif (moveobj.Type in ["Steel", "Dragon", "Ground"]):
            return ContestEffects.Finale
        elif (moveobj.Type in ["Flying", "Electric", "Fighting"]):
            return ContestEffects.Spark
        elif (moveobj.Type in ["Normal", "Poison", "Rock"]):
            return ContestEffects.Dull
        elif (moveobj.Type in ["Dark", "Ghost", "Bug"]):
            return ContestEffects.Sneaky
    
init -2:
    define contest_translation = {
    "Cool": "Carisma",
    "Beautiful": "Belleza",
    "Cute": "Dulzura",
    "Clever": "Ingenio",
    "Tough": "Dureza"
}