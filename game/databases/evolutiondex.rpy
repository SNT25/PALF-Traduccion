init python:
    
    # HOW THIS WORKS
    # LIST 1: Every entry is a list of two items, that starts with the Pokémon's form ID and is followed by as many lists (list 2) as this Pokémon has evos.
    # The last value is the priority with which the evolution is checked (for evolutions which have further condition than the preceding one).
    # LIST 2: The first is the evolution target. The others are tuples that describe the requirements.
    # TUPLE: Requirements come in two pairs: the first is the name, the second is the value. When a Pokémon has more requirements, all of them must be fulfilled together.
    
    # Example: [366, [367, ("Trade", None), ("HasItem", 52), 0], [368, ("Trade", None), ("HasItem", 53), 0]]       (Clamperl's evolutions)
    # Example: [562, [563, ("Level", 35), 0], [867, ("TravelToPlace", "Dusty Bowl"), ("DamageWithoutFaint", 49), 0]]                            (Whatever the hell Yamask needs)
    
    # REQUIREMENTS:
    # "Level" (int)
    # "TimeOfDay" (str)
    # "UsedItem" (str: item name)
    # "Place" (str)
    # "Friendship" (None)
    # "Trade" (None)
    # "LevelUp" (None)
    # "UseMove20Times" (str: move name)
    # "CriticalsInABattle" (int)
    # "KnowsMove" (str: move name)
    # "KnowsMoveOfType" (str: type name)
    # "Chance" (int)
    # "ChanceText" (int) (this value is only used for Pokédex information and is always considered true during parse)
    # "HasItem" (str: item name) (this does not check if the item is being given, but rather, if the item is had by the pokémon. do not use this as an event)
    # "HigherAtkThanDef" (None) (used with Tyrogue's evos)
    # "HigherDefThanAtk" (None) (used with Tyrogue's evos)
    # "SameAtkAndDef" (None) (used with Tyrogue's evos)
    # "Gender" (int: 0 if Male, 1 if Female)
    # "HasPokemonInParty" (int: Pokémon ID)
    # "RecoilDamageWithoutFaint" (int)
    # "TravelToPlace" (str) (this one is different from "Place" as this is an event that triggers the evolution, not a condition)
    # "DamageWithoutFaint" (int)
    # "TradeWith" (int: Pokémon id)
    # "DefeatThreeSameSpeciesWithItem" (str: item)
    # "HasTypeInParty" (str: type name)
    # "Nature" (list of str: nature names)
    # "InBattle" (None)
    
    # "Unimplemented" (None) (for Pokémon that cannot evolve yet)
    
    evolutions = []
    maxevopriority = 0
            
    def __addevo(mon, target, reqs, priority = 0): # the argument "reqs" is a list of tuples
        if not isinstance(reqs, list):
            raise TypeError("The requirements field " + str(reqs) + " must be a list.")
        for entry in evolutions:
            if entry[0] == mon:
                entry.append([target, *reqs, priority])
                maxpriority = max(maxevopriority, priority)
                return
        evolutions.append([mon, [target, *reqs, priority]])
        maxpriority = max(maxevopriority, priority)
    
    def GetPreevo(mon):
        for entry in evolutions:
            flattened_entry = [item for sublist in entry for item in (sublist[:-1] if isinstance(sublist, list) else [sublist])]
            if mon in flattened_entry[1:]:
                return entry[0]
        return None
    
    def GetEvos(mon):
        for entry in evolutions:
            if entry[0] == mon:
                flattened_entry = [item for sublist in entry for item in (sublist[:-1] if isinstance(sublist, list) else [sublist])]
                onlyevos = [item for item in flattened_entry[1:] if isinstance(item, (int, float))]
                return onlyevos
        return []
    
    def GetEvoRequirements(mon):
        requirements = []
        for entry in evolutions:
            flattened_entry = [item for sublist in entry for item in (sublist if isinstance(sublist, list) else [sublist])]
            if mon in flattened_entry[1:]:
                for evos in entry[1:]:
                    if evos[0] == mon:
                        requirements.append(evos[1:-1])
                break
        return requirements
    
    def HasTradeEvolution(mon):
        for evo in GetEvos(mon):
            for evomethod in GetEvoRequirements(evo):
                for requirement in evomethod:
                    if requirement[0] in ["Trade", "TradeWith"]:
                        return True
    
    __addevo(1, 2, [("Level", 16)]) # Ivysaur
    __addevo(2, 3, [("Level", 32)]) # Venusaur
    __addevo(4, 5, [("Level", 16)]) # Charmeleon
    __addevo(5, 6, [("Level", 36)]) # Charizard
    __addevo(7, 8, [("Level", 16)]) # Wartortle
    __addevo(8, 9, [("Level", 36)]) # Blastoise
    __addevo(10, 11, [("Level", 7)]) # Metapod
    __addevo(11, 12, [("Level", 10)]) # Butterfree
    __addevo(13, 14, [("Level", 7)]) # Kakuna
    __addevo(14, 15, [("Level", 10)]) # Beedrill
    __addevo(16, 17, [("Level", 18)]) # Pidgeotto
    __addevo(17, 18, [("Level", 36)]) # Pidgeot
    __addevo(19, 20, [("Level", 20)]) # Kantonian Raticate
    __addevo(19.1, 20.1, [("Level", 20), ("TimeOfDay", "Night")]) # Alolan Raticate
    __addevo(21, 22, [("Level", 20)]) # Fearow
    __addevo(23, 24, [("Level", 22)]) # Arbok
    __addevo(25, 26, [("UsedItem", "Thunder Stone")]) # Kantonian Raichu
    __addevo(25, 26.1, [("UsedItem", "Thunder Stone"), ("Place", "Alola")], 1) # Alolan Raichu
    __addevo(27, 28, [("Level", 22)]) # Kantonian Sandslash
    __addevo(27.1, 28.1, [("UsedItem", "Ice Stone")]) # Alolan Sandslash
    __addevo(29, 30, [("Level", 16)]) # Nidorina
    __addevo(30, 31, [("UsedItem", "Moon Stone")]) # Nidoqueen
    __addevo(32, 33, [("Level", 16)]) # Nidorino
    __addevo(33, 34, [("UsedItem", "Moon Stone")]) # Nidoking
    __addevo(35, 36, [("UsedItem", "Moon Stone")]) # Clefable
    __addevo(37, 38, [("UsedItem", "Fire Stone")]) # Kantonian Ninetales
    __addevo(37.1, 38.1, [("UsedItem", "Ice Stone")]) # Alolan Ninetales
    __addevo(39, 40, [("UsedItem", "Moon Stone")]) # Wigglytuff
    __addevo(41, 42, [("Level", 22)]) # Golbat
    __addevo(42, 169, [("LevelUp", None), ("Friendship", None)]) # Crobat
    __addevo(43, 44, [("Level", 21)]) # Gloom
    __addevo(44, 45, [("UsedItem", "Leaf Stone")]) # Vileplume
    __addevo(44, 182, [("UsedItem", "Sun Stone")]) # Bellossom
    __addevo(46, 47, [("Level", 24)]) # Parasect
    __addevo(48, 49, [("Level", 31)]) # Venomoth
    __addevo(50, 51, [("Level", 26)]) # Dugtrio
    __addevo(50.1, 51.1, [("Level", 26)]) # Rattata
    __addevo(52, 53, [("Level", 28)]) # Kantonian Persian
    __addevo(52.1, 53.1, [("LevelUp", None), ("Friendship", None)]) # Alolan Persian
    __addevo(52.2, 863, [("Level", 28)]) # Perrserker
    __addevo(54, 55, [("Level", 33)]) # Golduck
    __addevo(56, 57, [("Level", 28)]) # Primeape
    __addevo(57, 979, [("LevelUp", None), ("UseMove20Times", "Rage Fist")]) # Annihilape
    __addevo(58, 59, [("UsedItem", "Fire Stone")]) # Kantonian Arcanine
    __addevo(58.1, 59.1, [("UsedItem", "Fire Stone")]) # Hisuian Arcanine
    __addevo(60, 61, [("Level", 25)]) # Poliwhirl
    __addevo(61, 62, [("UsedItem", "Water Stone")]) # Poliwrath
    __addevo(61, 186, [("Trade", None), ("HasItem", Item.KingsRock)]) # Politoed
    __addevo(63, 64, [("Level", 16)]) # Kadabra
    __addevo(64, 65, [("Trade", None)]) # Alakazam
    __addevo(66, 67, [("Level", 28)]) # Machoke
    __addevo(67, 68, [("Trade", None)]) # Machamp
    __addevo(69, 70, [("Level", 21)]) # Weepinbell
    __addevo(70, 71, [("UsedItem", "Leaf Stone")]) # Victreebell
    __addevo(72, 73, [("Level", 30)]) # Tentacruel
    __addevo(74, 75, [("Level", 25)]) # Kantonian Graveler
    __addevo(74.1, 75.1, [("Level", 25)]) # Alolan Graveler
    __addevo(75, 76, [("Trade", None)]) # Kantonian Golem
    __addevo(75.1, 76.1, [("Trade", None)]) # Kantonian Golem
    __addevo(77, 78, [("Level", 40)]) # Kantonian Rapidash
    __addevo(77.1, 78.1, [("Level", 40)]) # Galarian Rapidash
    __addevo(79, 80, [("Level", 37)]) # Kantonian Slowbro
    __addevo(79.1, 80.2, [("UsedItem", Item.GalaricaCuff)]) # Galarian Slowbro
    __addevo(79, 199, [("Trade", None), ("HasItem", 71)]) # Johtonian Slowking
    __addevo(79.1, 199.1, [("UsedItem", Item.GalaricaWreath)]) # Galarian Slowking
    __addevo(81, 82, [("Level", 30)]) # Magneton
    __addevo(82, 462, [("LevelUp", None), ("Place", "Special Magnetic Field")]) # Magnezone
    __addevo(82, 462, [("UsedItem", "Thunder Stone")]) # Magnezone
    __addevo(83.1, 865, [("CriticalsInABattle", 3)]) # Sirfetch'd
    __addevo(84, 85, [("Level", 31)]) # Dodrio
    __addevo(86, 87, [("Level", 34)]) # Dewgong
    __addevo(88, 89, [("Level", 38)]) # Kantonian Muk
    __addevo(88.1, 89.1, [("Level", 38)]) # Alolan Muk
    __addevo(90, 91, [("UsedItem", "Water Stone")]) # Cloyster
    __addevo(92, 93, [("Level", 25)]) # Haunter
    __addevo(93, 94, [("Trade", None)]) # Gengar
    __addevo(95, 208, [("Trade", None), ("HasItem", Item.MetalCoat)]) # Steelix
    __addevo(96, 97, [("Level", 26)]) # Hypno
    __addevo(98, 99, [("Level", 28)]) # Kingler
    __addevo(100, 101, [("Level", 30)]) # Kantonian Electrode
    __addevo(100.1, 101.1, [("UsedItem", "Leaf Stone")]) # Hisuian Electrode
    __addevo(102, 103, [("UsedItem", "Leaf Stone")]) # Kantonian Exeggutor
    __addevo(102, 103.1, [("UsedItem", "Leaf Stone"), ("Place", "Alola")], 1) # Alolan Exeggutor
    __addevo(104, 105, [("Level", 28)]) # Kantonian Marowak
    __addevo(104, 105.1, [("Level", 28), ("Place", "Alola")], 1) # Alolan Marowak
    __addevo(108, 463, [("LevelUp", None), ("KnowsMove", "Rollout")]) # Lickilicky
    __addevo(109, 110, [("Level", 35)]) # Kantonian Wheezing
    __addevo(109, 110.1, [("Level", 35), ("Place", "Galar")], 1) # Galarian Wheezing
    __addevo(111, 112, [("Level", 42)]) # Rhydon
    __addevo(112, 464, [("Trade", None), ("HasItem", Item.Protector)]) # Rhyperior
    __addevo(113, 242, [("LevelUp", None), ("Friendship", None)]) # Blissey
    __addevo(114, 465, [("LevelUp", None), ("KnowsMove", "Ancient Power")]) # Tangrowth
    __addevo(116, 117, [("Level", 32)]) # Seadra
    __addevo(117, 230, [("Trade", None), ("HasItem", Item.DragonScale)]) # Kingdra
    __addevo(118, 119, [("Level", 33)]) # Seaking
    __addevo(120, 121, [("UsedItem", "Water Stone")]) # Starmie
    __addevo(122.1, 866, [("Level", 42), ("Place", "Galar")]) # Mr. Rime
    __addevo(123, 212, [("Trade", None), ("HasItem", Item.MetalCoat)]) # Scizor
    __addevo(123, 900, [("UsedItem", "Black Augurite")]) # Kleavor
    __addevo(125, 466, [("Trade", None), ("HasItem", Item.Electirizer)]) # Electivire
    __addevo(126, 467, [("Trade", None), ("HasItem", Item.Magmarizer)]) # Magmortar
    __addevo(129, 130, [("Level", 20)]) # Gyarados
    __addevo(133, 134, [("UsedItem", "Water Stone")]) # Vaporeon
    __addevo(133, 135, [("UsedItem", "Thunder Stone")]) # Jolteon
    __addevo(133, 136, [("UsedItem", "Fire Stone")]) # Flareon
    __addevo(133, 196, [("LevelUp", None), ("Friendship", None), ("TimeOfDay", "Day")]) # Espeon
    __addevo(133, 196, [("UsedItem", "Sun Shard")]) # Espeon
    __addevo(133, 197, [("LevelUp", None), ("Friendship", None), ("TimeOfDay", "Night")]) # Umbreon
    __addevo(133, 197, [("UsedItem", "Moon Shard")]) # Umbreon
    __addevo(133, 470, [("LevelUp", None), ("Place", "Moss Rock")]) # Leafeon
    __addevo(133, 470, [("UsedItem", "Leaf Stone")]) # Leafeon
    __addevo(133, 471, [("LevelUp", None), ("Place", "Ice Rock")]) # Glaceon
    __addevo(133, 471, [("UsedItem", "Ice Stone")]) # Glaceon
    __addevo(133, 700, [("LevelUp", None), ("KnowsMoveOfType", "Fairy"), ("Friendship", None)], 1) # Sylveon
    __addevo(137, 233, [("Trade", None), ("HasItem", 51)]) # Porygon2 - Item is Up-Grade
    __addevo(138, 139, [("Level", 40)]) # Omastar
    __addevo(140, 141, [("Level", 40)]) # Kabutops
    __addevo(147, 148, [("Level", 30)]) # Dragonair
    __addevo(148, 149, [("Level", 55)]) # Dragonite
    __addevo(152, 153, [("Level", 16)]) # Bayleef
    __addevo(153, 154, [("Level", 32)]) # Meganium
    __addevo(155, 156, [("Level", 14)]) # Quilava
    __addevo(155, 156, [("Level", 17), ("Place", "Hisui")], 1) # Quilava
    __addevo(156, 157, [("Level", 36)]) # Johtonian Typhlosion
    __addevo(156, 157.1, [("Level", 36), ("Place", "Hisui")], 1) # Hisuian Typhlosion
    __addevo(158, 159, [("Level", 18)]) # Croconaw
    __addevo(159, 160, [("Level", 30)]) # Feraligatr
    __addevo(161, 162, [("Level", 15)]) # Furret
    __addevo(163, 164, [("Level", 20)]) # Noctowl
    __addevo(165, 166, [("Level", 18)]) # Ledian
    __addevo(167, 168, [("Level", 22)]) # Ariados
    __addevo(170, 171, [("Level", 27)]) # Lanturn
    __addevo(172, 25, [("LevelUp", None), ("Friendship", None)]) # Pikachu
    __addevo(173, 35, [("LevelUp", None), ("Friendship", None)]) # Clefairy
    __addevo(174, 39, [("LevelUp", None), ("Friendship", None)]) # Jigglypuff
    __addevo(175, 176, [("LevelUp", None), ("Friendship", None)]) # Togetic
    __addevo(176, 468, [("UsedItem", "Shiny Stone")]) # Togekiss
    __addevo(177, 178, [("Level", 25)]) # Xatu
    __addevo(179, 180, [("Level", 15)]) # Flaaffy
    __addevo(180, 181, [("Level", 30)]) # Ampharos
    __addevo(183, 184, [("Level", 18)]) # Azumarill
    __addevo(187, 188, [("Level", 18)]) # Skiploom
    __addevo(188, 189, [("Level", 27)]) # Jumpluff
    __addevo(190, 424, [("LevelUp", None), ("KnowsMove", "Double Hit")]) # Ambipom
    __addevo(191, 192, [("UsedItem", "Sun Stone")]) # Sunflora
    __addevo(193, 469, [("LevelUp", None), ("KnowsMove", "Ancient Power")]) # Yanmega
    __addevo(194, 195, [("Level", 20)]) # Quagsire
    __addevo(194.1, 980, [("Level", 20)]) # Clodsire
    __addevo(198, 430, [("UsedItem", "Dusk Stone")]) # Honchkrow
    __addevo(200, 429, [("UsedItem", "Dusk Stone")]) # Mismagius
    __addevo(203, 981, [("LevelUp", None), ("KnowsMove", None), ("Unimplemented", None)]) # Farigiraf - Not implemented
    __addevo(204, 205, [("Level", 31)]) # Forretress
    __addevo(206, 982, [("LevelUp", None), ("KnowsMove", "Hyper Drill"), ("ChanceText", 0.99)]) # Dudunsparce Two-Segment
    __addevo(206, 982.1, [("LevelUp", None), ("KnowsMove", "Hyper Drill"), ("Chance", 0.01)], 1) # Dudunsparce Three-Segment
    __addevo(207, 472, [("LevelUp", None), ("HasItem", Item.RazorClaw), ("TimeOfDay", "Night")]) # Gliscor
    __addevo(209, 210, [("Level", 23)]) # Granbull
    __addevo(211.1, 904, [("LevelUp", None), ("KnowsMove", None), ("Unimplemented", None)]) # Overqwil - Not implemented
    __addevo(215, 461, [("LevelUp", None), ("HasItem", Item.RazorClaw), ("TimeOfDay", "Night")]) # Weavile
    __addevo(215.1, 903, [("LevelUp", None), ("HasItem", Item.RazorClaw), ("TimeOfDay", "Day")]) # Sneasler
    __addevo(216, 217, [("Level", 30)]) # Ursaring
    __addevo(217, 901, [("UsedItem", "Peat Block"), ("TimeOfDay", "Night")]) # Ursaluna
    __addevo(218, 219, [("Level", 38)]) # Magcargo
    __addevo(220, 221, [("Level", 33)]) # Piloswine
    __addevo(221, 473, [("LevelUp", None), ("KnowsMove", "Ancient Power")]) # Mamoswine
    __addevo(222.1, 864, [("Level", 38)]) # Cursola
    __addevo(223, 224, [("Level", 25)]) # Octillery
    __addevo(228, 229, [("Level", 16)]) # Houndoom
    __addevo(231, 232, [("Level", 25)]) # Donphan
    __addevo(233, 474, [("Trade", None), ("HasItem", Item.DubiousDisc)]) # Porygon-Z
    __addevo(234, 899, [("UseMove20Times", None), ("Unimplemented", None)]) # Wyrdeer - Not implemented
    __addevo(236, 106, [("Level", 20), ("HigherAtkThanDef", None)]) # Hitmonlee
    __addevo(236, 107, [("Level", 20), ("HigherDefThanAtk", None)]) # Hitmonchan
    __addevo(236, 237, [("Level", 20), ("SameAtkAndDef", None)]) # Hitmontop
    __addevo(238, 124, [("Level", 30)]) # Jynx
    __addevo(239, 125, [("Level", 30)]) # Electabuzz
    __addevo(240, 126, [("Level", 30)]) # Magmar
    __addevo(246, 247, [("Level", 30)]) # Pupitar
    __addevo(247, 248, [("Level", 55)]) # Tyranitar
    __addevo(252, 253, [("Level", 16)]) # Grovyle
    __addevo(253, 254, [("Level", 36)]) # Sceptile
    __addevo(255, 256, [("Level", 16)]) # Combusken
    __addevo(256, 257, [("Level", 36)]) # Blaziken
    __addevo(258, 259, [("Level", 16)]) # Marshtomp
    __addevo(259, 260, [("Level", 36)]) # Swampert
    __addevo(261, 262, [("Level", 18)]) # Mightyena
    __addevo(263, 264, [("Level", 20)]) # Hoennian Linoone
    __addevo(263.1, 264.1, [("Level", 20)]) # Galarian Linoone
    __addevo(264.1, 862, [("Level", 35), ("TimeOfDay", "Night")]) # Obstagoon
    __addevo(265, 266, [("Level", 7), ("Chance", 0.5)]) # Silcoon
    __addevo(266, 267, [("Level", 10)]) # Beautifly
    __addevo(265, 268, [("Level", 7), ("ChanceText", 0.5)]) # Cascoon
    __addevo(268, 269, [("Level", 10)]) # Dustox
    __addevo(270, 271, [("Level", 14)]) # Lombre
    __addevo(271, 272, [("UsedItem", "Water Stone")]) # Ludicolo
    __addevo(273, 274, [("Level", 14)]) # Nuzleaf
    __addevo(274, 275, [("UsedItem", "Leaf Stone")]) # Shiftry
    __addevo(276, 277, [("Level", 22)]) # Swellow
    __addevo(278, 279, [("Level", 25)]) # Pelipper
    __addevo(280, 281, [("Level", 20)]) # Kirlia
    __addevo(281, 282, [("Level", 30), ("Gender", 1)]) # Gardevoir
    __addevo(281, 475, [("UsedItem", "Dawn Stone"), ("Gender", 0)]) # Gallade
    __addevo(283, 284, [("Level", 22)]) # Masquerain
    __addevo(285, 286, [("Level", 23)]) # Breloom
    __addevo(287, 288, [("Level", 18)]) # Vigoroth
    __addevo(288, 289, [("Level", 36)]) # Slaking
    __addevo(290, 291, [("Level", 20)]) # Ninjask
    __addevo(290, 292, [("None", None)]) # Shedinja - Shedinja is not defined as an evolution, and should be added separately due to it not changing the starting Pokémon
    __addevo(293, 294, [("Level", 20)]) # Loudred
    __addevo(294, 295, [("Level", 40)]) # Exploud
    __addevo(296, 297, [("Level", 24)]) # Hariyama
    __addevo(298, 183, [("LevelUp", None), ("Friendship", None)]) # Marill
    __addevo(299, 476, [("LevelUp", None), ("Place", "Special Magnetic Field")]) # Probopass
    __addevo(299, 476, [("UsedItem", "Thunder Stone")]) # Probopass
    __addevo(300, 301, [("UsedItem", "Moon Stone")]) # Delcatty
    __addevo(304, 305, [("Level", 32)]) # Lairon
    __addevo(305, 306, [("Level", 42)]) # Aggron
    __addevo(307, 308, [("Level", 37)]) # Medicham
    __addevo(309, 310, [("Level", 26)]) # Manecrtic
    __addevo(315, 407, [("UsedItem", "Shiny Stone")]) # Roserade
    __addevo(316, 317, [("Level", 26)]) # Swalot
    __addevo(318, 319, [("Level", 30)]) # Sharpedo
    __addevo(320, 321, [("Level", 40)]) # Wailord
    __addevo(322, 323, [("Level", 33)]) # Camerupt
    __addevo(325, 326, [("Level", 32)]) # Grumpig
    __addevo(328, 329, [("Level", 35)]) # Vibrava
    __addevo(329, 330, [("Level", 45)]) # Flygon
    __addevo(331, 332, [("Level", 32)]) # Cacturne
    __addevo(333, 334, [("Level", 35)]) # Altaria
    __addevo(339, 340, [("Level", 30)]) # Whiscash
    __addevo(341, 342, [("Level", 30)]) # Crawdaunt
    __addevo(343, 344, [("Level", 36)]) # Claydol
    __addevo(345, 346, [("Level", 40)]) # Cradily
    __addevo(347, 348, [("Level", 40)]) # Armaldo
    __addevo(349, 350, [("UsedItem", "Prism Scale")]) # Milotic
    __addevo(353, 354, [("Level", 37)]) # Banette
    __addevo(355, 356, [("Level", 37)]) # Dusclops
    __addevo(356, 477, [("Trade", None), ("HasItem", Item.ReaperCloth)]) # Dusknoir
    __addevo(360, 202, [("Level", 15)]) # Wobbuffet
    __addevo(361, 362, [("Level", 42), ("Gender", 0)]) # Glalie
    __addevo(361, 478, [("UsedItem", "Dawn Stone"), ("Gender", 1)]) # Froslass
    __addevo(363, 364, [("Level", 32)]) # Sealeo
    __addevo(364, 365, [("Level", 44)]) # Walrein
    __addevo(366, 367, [("Trade", None), ("HasItem", Item.DeepSeaTooth)]) # Huntail
    __addevo(366, 368, [("Trade", None), ("HasItem", Item.DeepSeaScale)]) # Gorebyss
    __addevo(371, 372, [("Level", 30)]) # Shelgon
    __addevo(372, 373, [("Level", 50)]) # Salamence
    __addevo(374, 375, [("Level", 20)]) # Metang
    __addevo(375, 376, [("Level", 45)]) # Metagross
    __addevo(387, 388, [("Level", 18)]) # Grotle
    __addevo(388, 389, [("Level", 32)]) # Torterra
    __addevo(390, 391, [("Level", 14)]) # Monferno
    __addevo(391, 392, [("Level", 36)]) # Infernape
    __addevo(393, 394, [("Level", 16)]) # Prinplup
    __addevo(394, 395, [("Level", 36)]) # Empoleon
    __addevo(396, 397, [("Level", 14)]) # Staravia
    __addevo(397, 398, [("Level", 34)]) # Staraptor
    __addevo(399, 400, [("Level", 15)]) # Bibarel
    __addevo(401, 402, [("Level", 10)]) # Kricketune
    __addevo(403, 404, [("Level", 15)]) # Luxio
    __addevo(404, 405, [("Level", 30)]) # Luxray
    __addevo(406, 315, [("LevelUp", None), ("Friendship", None)]) # Roselia
    __addevo(408, 409, [("Level", 30)]) # Rampardos
    __addevo(410, 411, [("Level", 30)]) # Bastiodon
    __addevo(412, 413, [("Level", 20), ("Gender", 1)]) # Plant Cloak Wormadam
    __addevo(412, 414, [("Level", 20), ("Gender", 0)]) # Mothim
    __addevo(412.1, 413.1, [("Level", 20), ("Gender", 1)]) # Sandy Cloak Wormadam
    __addevo(412.1, 414, [("Level", 20), ("Gender", 0)]) # Mothim
    __addevo(412.2, 413.2, [("Level", 20), ("Gender", 1)]) # Sandy Cloak Wormadam
    __addevo(412.2, 414, [("Level", 20), ("Gender", 0)]) # Mothim
    __addevo(415, 416, [("Level", 21), ("Gender", 1)]) # Vespiquen
    __addevo(418, 419, [("Level", 26)]) # Floatzel
    __addevo(420, 421, [("Level", 25)]) # Cherrim
    __addevo(422, 423, [("Level", 30)]) # West Sea Gastrodon
    __addevo(422.1, 423.1, [("Level", 30)]) # East Sea Gastrodon
    __addevo(425, 426, [("Level", 28)]) # Drifblim
    __addevo(427, 428, [("LevelUp", None), ("Friendship", None)]) # Lopunny
    __addevo(431, 432, [("Level", 38)]) # Purugly
    __addevo(433, 358, [("LevelUp", None), ("Friendship", None), ("TimeOfDay", "Night")]) # Chimecho
    __addevo(434, 435, [("Level", 34)]) # Skuntank
    __addevo(436, 437, [("Level", 33)]) # Bronzong
    __addevo(438, 185, [("LevelUp", None), ("KnowsMove", "Mimic")]) # Sudowoodo
    __addevo(439, 122, [("LevelUp", None), ("KnowsMove", "Mimic")]) # Kantonian Mr. Mime
    __addevo(439, 122.1, [("LevelUp", None), ("KnowsMove", "Mimic"), ("Place", "Galar")]) # Galarian Mr. Mime
    __addevo(440, 113, [("LevelUp", None), ("HasItem", Item.OvalStone), ("TimeOfDay", "Day")]) # Chansey
    __addevo(443, 444, [("Level", 24)]) # Gabite
    __addevo(444, 445, [("Level", 48)]) # Garchomp
    __addevo(446, 143, [("LevelUp", None), ("Friendship", None)]) # Snorlax
    __addevo(447, 448, [("LevelUp", None), ("Friendship", None), ("TimeOfDay", "Day")]) # Lucario
    __addevo(449, 450, [("Level", 34)]) # Hippowdon
    __addevo(451, 452, [("Level", 40)]) # Drapion
    __addevo(453, 454, [("Level", 37)]) # Toxicroak
    __addevo(456, 457, [("Level", 31)]) # Lumineon
    __addevo(458, 226, [("LevelUp", None), ("HasPokemonInParty", 223)]) # Mantine
    __addevo(459, 460, [("Level", 40)]) # Abomasnow
    __addevo(495, 496, [("Level", 17)]) # Servine
    __addevo(496, 497, [("Level", 36)]) # Serperior
    __addevo(498, 499, [("Level", 17)]) # Pignite
    __addevo(499, 500, [("Level", 36)]) # Emboar
    __addevo(501, 502, [("Level", 17)]) # Dewott
    __addevo(502, 503, [("Level", 36)]) # Unovan Samurott
    __addevo(502, 503.1, [("Level", 36), ("Place", "Hisui")], 1) # Hisuian Samurott
    __addevo(504, 505, [("Level", 20)]) # Watchog
    __addevo(506, 507, [("Level", 16)]) # Herdier
    __addevo(507, 508, [("Level", 32)]) # Stoutland
    __addevo(509, 510, [("Level", 20)]) # Liepard
    __addevo(511, 512, [("UsedItem", "Leaf Stone")]) # Simisage
    __addevo(513, 514, [("UsedItem", "Fire Stone")]) # Simisear
    __addevo(515, 516, [("UsedItem", "Water Stone")]) # Simipour
    __addevo(517, 518, [("UsedItem", "Moon Stone")]) # Musharna
    __addevo(519, 520, [("Level", 21)]) # Tranquill
    __addevo(520, 521, [("Level", 32)]) # Unfezant
    __addevo(522, 523, [("Level", 27)]) # Zebstrika
    __addevo(524, 525, [("Level", 25)]) # Boldore
    __addevo(525, 526, [("Trade", None)]) # Gigalith
    __addevo(527, 528, [("LevelUp", None), ("Friendship", None)]) # Swoobat
    __addevo(529, 530, [("Level", 31)]) # Excadrill
    __addevo(532, 533, [("Level", 25)]) # Gurdurr
    __addevo(533, 534, [("Trade", None)]) # Conkeldurr
    __addevo(535, 536, [("Level", 25)]) # Palpitoad
    __addevo(536, 537, [("Level", 36)]) # Seismitoad
    __addevo(540, 541, [("Level", 20)]) # Swadloon
    __addevo(541, 542, [("Trade", None)]) # Leavanny
    __addevo(543, 544, [("Level", 22)]) # Whirlipede
    __addevo(544, 545, [("Level", 30)]) # Scolipede
    __addevo(546, 547, [("UsedItem", "Sun Stone")]) # Whimsicott
    __addevo(548, 549, [("UsedItem", "Sun Stone")]) # Unovan Lilligant
    __addevo(548, 549.1, [("UsedItem", "Sun Stone"), ("Place", "Hisui")], 1) # Hisuian Lilligant
    __addevo(550.2, 902, [("LevelUp", None), ("RecoilDamageWithoutFaint", 294)]) # Basculegion
    __addevo(551, 552, [("Level", 29)]) # Krokorok
    __addevo(552, 553, [("Level", 40)]) # Krookodile
    __addevo(554, 555, [("Level", 35)]) # Unovan Darmanitan
    __addevo(554.1, 555.2, [("UsedItem", "Ice Stone")]) # Galarian Darmanitan
    __addevo(557, 558, [("Level", 34)]) # Crustle
    __addevo(559, 560, [("Level", 39)]) # Scrafty
    __addevo(562, 563, [("Level", 34)]) # Cofagrigus
    __addevo(562.1, 867, [("TravelToPlace", "Dusty Bowl"), ("DamageWithoutFaint", 49)]) # Runerigus
    __addevo(564, 565, [("Level", 37)]) # Carracosta
    __addevo(566, 567, [("Level", 37)]) # Archeops
    __addevo(568, 569, [("Level", 36)]) # Garbodor
    __addevo(570, 571, [("Level", 32)]) # Unovan Zoroark
    __addevo(570.1, 571.1, [("Level", 32)]) # Hisuian Zoroark
    __addevo(572, 573, [("UsedItem", "Shiny Stone")]) # Cinccino
    __addevo(574, 575, [("Level", 32)]) # Gothorita
    __addevo(575, 576, [("Level", 41)]) # Gothitelle
    __addevo(577, 578, [("Level", 32)]) # Duosion
    __addevo(578, 579, [("Level", 41)]) # Reuniclus
    __addevo(580, 581, [("Level", 35)]) # Swanna
    __addevo(582, 583, [("Level", 35)]) # Vanillish
    __addevo(583, 584, [("Level", 47)]) # Vanilluxe
    __addevo(585, 586, [("Level", 34)]) # Spring Sawsbuck
    __addevo(585.1, 586.1, [("Level", 34)]) # Summer Sawsbuck
    __addevo(585.2, 586.2, [("Level", 34)]) # Fall Sawsbuck
    __addevo(585.3, 586.3, [("Level", 34)]) # Winter Sawsbuck
    __addevo(588, 589, [("TradeWith", 616)]) # Escavalier
    __addevo(590, 591, [("Level", 39)]) # Amoonguss
    __addevo(592, 593, [("Level", 40)]) # Jellicent
    __addevo(595, 596, [("Level", 36)]) # Galvantula
    __addevo(597, 598, [("Level", 40)]) # Ferrothorn
    __addevo(599, 600, [("Level", 38)]) # Klang
    __addevo(600, 601, [("Level", 49)]) # Klinklang
    __addevo(602, 603, [("Level", 39)]) # Eelektrik
    __addevo(603, 604, [("UsedItem", "Thunder Stone")]) # Eelektross
    __addevo(605, 606, [("Level", 42)]) # Beheeyem
    __addevo(607, 608, [("Level", 41)]) # Lampent
    __addevo(608, 609, [("UsedItem", "Dusk Stone")]) # Chandelure
    __addevo(610, 611, [("Level", 38)]) # Fraxure
    __addevo(611, 612, [("Level", 48)]) # Haxorus
    __addevo(613, 614, [("Level", 37)]) # Beartic
    __addevo(616, 617, [("TradeWith", 588)]) # Accelgor
    __addevo(619, 620, [("Level", 50)]) # Mienshao
    __addevo(622, 623, [("Level", 43)]) # Golurk
    __addevo(624, 625, [("Level", 52)]) # Bisharp
    __addevo(625, 983, [("DefeatThreeSameSpeciesWithItem", "Leader's Crest")]) # Kingambit
    __addevo(627, 628, [("Level", 54)]) # Unovan Braviary
    __addevo(627, 628.1, [("Level", 54), ("Place", "Hisui")], 1) # Hisuian Braviary
    __addevo(629, 630, [("Level", 54)]) # Mandibuzz
    __addevo(633, 634, [("Level", 50)]) # Zweilous
    __addevo(634, 635, [("Level", 64)]) # Hydreigon
    __addevo(636, 637, [("Level", 59)]) # Volcarona
    __addevo(650, 651, [("Level", 16)]) # Quilladin
    __addevo(651, 652, [("Level", 36)]) # Chesnaught
    __addevo(653, 654, [("Level", 16)]) # Braixen
    __addevo(654, 655, [("Level", 36)]) # Delphox
    __addevo(656, 657, [("Level", 16)]) # Frogadier
    __addevo(657, 658, [("Level", 36)]) # Greninja
    __addevo(659, 660, [("Level", 20)]) # Diggersby
    __addevo(661, 662, [("Level", 17)]) # Fletchinder
    __addevo(662, 663, [("Level", 35)]) # Talonflame
    __addevo(664, 665, [("Level", 9)]) # Spewpa
    __addevo(665, 666, [("Level", 12)]) # Vivillon
    __addevo(667, 668, [("Level", 35)]) # Pyroar
    __addevo(669, 670, [("Level", 19)]) # Floette
    __addevo(670, 671, [("Item", "Shiny Stone")]) # Florges
    __addevo(672, 673, [("Level", 36)]) # Gogoat
    __addevo(674, 675, [("Level", 32), ("HasTypeInParty", "Dark")]) # Pangoro
    __addevo(677, 678, [("Level", 25)]) # Meowstic
    __addevo(679, 680, [("Level", 35)]) # Doublade
    __addevo(680, 681, [("UsedItem", "Dusk Stone")]) # Aegislash
    __addevo(682, 683, [("Trade", None), ("HasItem", Item.Sachet)]) # Aromatisse
    __addevo(684, 685, [("Trade", None), ("HasItem", Item.WhippedDream)]) # Slurpuff
    __addevo(686, 687, [("Level", 30)]) # Malamar
    __addevo(688, 689, [("Level", 39)]) # Barbaracle
    __addevo(690, 691, [("Level", 48)]) # Dragalge
    __addevo(692, 693, [("Level", 37)]) # Clawitzer
    __addevo(694, 695, [("UsedItem", "Sun Stone")]) # Heliolisk
    __addevo(696, 697, [("Level", 39), ("TimeOfDay", "Day")]) # Tyrantrum
    __addevo(698, 699, [("Level", 39), ("TimeOfDay", "Night")]) # Aurorus
    __addevo(704, 705, [("Level", 40)]) # Kalosian Sliggoo
    __addevo(704, 705.1, [("Level", 40), ("Place", "Hisui")], 1) # Hisuian Sliggoo
    __addevo(705, 706, [("Level", 50)]) # Kalosian Goodra
    __addevo(705.1, 706.1, [("Level", 50)]) # Hisuian Goodra
    __addevo(708, 709, [("Trade", None)]) # Trevenant
    __addevo(710, 711, [("Trade", None)]) # Gourgeist
    __addevo(710.1, 711.1, [("Trade", None)]) # Gourgeist
    __addevo(710.2, 711.2, [("Trade", None)]) # Gourgeist
    __addevo(710.3, 711.3, [("Trade", None)]) # Gourgeist
    __addevo(712, 713, [("Level", 37)]) # Kalosian Avalugg
    __addevo(712, 713.1, [("Level", 37), ("Place", "Hisui")], 1) # Hisuian Avalugg
    __addevo(714, 715, [("Level", 48)]) # Noivern
    __addevo(722, 723, [("Level", 17)]) # Dartrix
    __addevo(723, 724, [("Level", 34)]) # Alolan Decidueye
    __addevo(723, 724.1, [("Level", 36), ("Place", "Hisui")], 1) # Hisuian Decidueye - Due to the required level being higher than the previous entry, this evolution is never triggered, unless the Pokémon's evolution is cancelled until level 36. This shouldn't be a problem for now, since the Pokémon is not in game
    __addevo(725, 726, [("Level", 17)]) # Torracat
    __addevo(726, 727, [("Level", 34)]) # Incineroar
    __addevo(728, 729, [("Level", 17)]) # Brionne
    __addevo(729, 730, [("Level", 34)]) # Primarina
    __addevo(731, 732, [("Level", 14)]) # Trumbeak
    __addevo(732, 733, [("Level", 28)]) # Toucannon
    __addevo(734, 735, [("Level", 20), ("TimeOfDay", "Day")]) # Gumshoos
    __addevo(736, 737, [("Level", 20)]) # Charjabug
    __addevo(737, 738, [("LevelUp", None), ("Place", "Special Magnetic Field")]) # Vikavolt
    __addevo(737, 738, [("UsedItem", "Thunder Stone")]) # Vikavolt
    __addevo(737, 738, [("LevelUp", None), ("Place", "Mount Lanakila")]) # Vikavolt
    __addevo(739, 740, [("UsedItem", "Ice Stone")]) # Crabominable
    __addevo(742, 743, [("Level", 25)]) # Ribombee
    __addevo(744, 745, [("Level", 25), ("TimeOfDay", "Noon")]) # Midday Lycanroc
    __addevo(744, 745.1, [("Level", 25), ("TimeOfDay", "Night")]) # Midnight Lycanroc
    __addevo(744, 745.2, [("Level", 25), ("TimeOfDay", "Evening")]) # Dusk Lycanroc
    __addevo(747, 748, [("Level", 38)]) # Toxapex
    __addevo(749, 750, [("Level", 30)]) # Mudsdale
    __addevo(751, 752, [("Level", 22)]) # Araquanid
    __addevo(753, 754, [("Level", 34), ("TimeOfDay", "Day")]) # Lurantis
    __addevo(755, 756, [("Level", 24)]) # Shiinotic
    __addevo(757, 758, [("Level", 33), ("Gender", 1)]) # Salazzle
    __addevo(759, 760, [("Level", 27)]) # Bewear
    __addevo(761, 762, [("Level", 18)]) # Steenee
    __addevo(762, 763, [("LevelUp", None), ("KnowsMove", "Stomp")]) # Tsareena
    __addevo(767, 768, [("Level", 30)]) # Golisopod
    __addevo(769, 770, [("Level", 42)]) # Palossand
    __addevo(772, 773, [("LevelUp", None), ("Friendship", None)]) # Silvally
    __addevo(782, 783, [("Level", 35)]) # Hakamo-o
    __addevo(783, 784, [("Level", 45)]) # Kommo-o
    __addevo(789, 790, [("Level", 43)]) # Cosmoem
    __addevo(790, 791, [("Level", 53), ("TimeOfDay", "Day")]) # Solgaleo - Edited due to the impossibility of replicating
    __addevo(790, 792, [("Level", 53), ("TimeOfDay", "Night")]) # Lunala - Edited due to the impossibility of replicating
    __addevo(803, 804, [("LevelUp", None), ("KnowsMove", "Dragon Pulse")]) # Naganadel
    __addevo(808, 809, [("Unimplemented", None)]) # Melmetal
    __addevo(810, 811, [("Level", 16)]) # Thwackey
    __addevo(811, 812, [("Level", 35)]) # Rillaboom
    __addevo(813, 814, [("Level", 16)]) # Raboot
    __addevo(814, 815, [("Level", 35)]) # Cinderace
    __addevo(816, 817, [("Level", 16)]) # Drizzile
    __addevo(817, 818, [("Level", 35)]) # Inteleon
    __addevo(819, 820, [("Level", 24)]) # Greedent
    __addevo(821, 822, [("Level", 18)]) # Corvisquire
    __addevo(822, 823, [("Level", 38)]) # Corviknight
    __addevo(824, 825, [("Level", 10)]) # Dottler
    __addevo(825, 826, [("Level", 30)]) # Orbeetle
    __addevo(827, 828, [("Level", 18)]) # Thievul
    __addevo(829, 830, [("Level", 20)]) # Eldegoss
    __addevo(831, 832, [("Level", 24)]) # Dubwool
    __addevo(833, 834, [("Level", 22)]) # Drednaw
    __addevo(835, 836, [("Level", 25)]) # Boltund
    __addevo(837, 838, [("Level", 18)]) # Carkol
    __addevo(838, 839, [("Level", 38)]) # Coalossal
    __addevo(840, 841, [("UsedItem", "Tart Apple")]) # Flapple
    __addevo(840, 842, [("UsedItem", "Sweet Apple")]) # Appletun
    __addevo(840, 1011, [("UsedItem", "Syrupy Apple")]) # Dipplin
    __addevo(843, 844, [("Level", 36)]) # Sandaconda
    __addevo(846, 847, [("Level", 26)]) # Barraskewda
    __addevo(848, 849, [("Level", 30), ("Nature", ["Hardy", "Brave", "Adamant", "Naughty", "Docile", "Impish", "Lax", "Hasty", "Jolly", "Naive", "Rash", "Sassy", "Quirky"])]) # Toxtricity (Amped Form)
    __addevo(848, 849.1, [("Level", 30), ("Nature", ["Lonely", "Bold", "Relaxed", "Timid", "Serious", "Modest", "Mild", "Quiet", "Bashful", "Calm", "Gentle", "Careful"])]) # Toxtricity (Low Key Form)
    __addevo(850, 851, [("Level", 28)]) # Centiskorch
    __addevo(852, 853, [("LevelUp", None), ("KnowsMove", "Taunt")]) # Grapploct
    __addevo(854, 855, [("UsedItem", Item.CrackedPot)]) # Polteageist (Phony Form)
    __addevo(854, 855, [("UsedItem", Item.ChippedPot)]) # Polteageist (Antique Form)
    __addevo(856, 857, [("Level", 32)]) # Hattrem
    __addevo(857, 858, [("Level", 42)]) # Hatterene
    __addevo(859, 860, [("Level", 32)]) # Morgrem
    __addevo(860, 861, [("Level", 42)]) # Grimmsnarl
    __addevo(868, 869, [("Unimplemented", None)]) # Alcremie - Unimplemented
    __addevo(872, 873, [("LevelUp", None), ("Friendship", None), ("TimeOfDay", "Night")]) # Frosmoth
    __addevo(878, 879, [("Level", 34)]) # Copperajah
    __addevo(884, 1018, [("UsedItem", Item.MetalAlloy)]) # Archaludon
    __addevo(885, 886, [("Level", 50)]) # Drakloak
    __addevo(886, 887, [("Level", 60)]) # Dragapult
    __addevo(891, 892, [("UsedItem", "Scroll of Darkness")]) # Single Strike Urshifu
    __addevo(891, 892.1, [("UsedItem", "Scroll of Waters")]) # Rapid Strike Urshifu
    __addevo(906, 907, [("Level", 16)]) # Floragato
    __addevo(907, 908, [("Level", 36)]) # Meowscarada
    __addevo(909, 910, [("Level", 16)]) # Crocalor
    __addevo(910, 911, [("Level", 36)]) # Skeledirge
    __addevo(912, 913, [("Level", 16)]) # Quaxwell
    __addevo(913, 914, [("Level", 36)]) # Quaquaval
    __addevo(915, 916, [("Level", 18)]) # Oinkologne
    __addevo(917, 918, [("Level", 15)]) # Spidops
    __addevo(919, 920, [("Level", 24)]) # Lokix
    __addevo(921, 922, [("Level", 18)]) # Pawmo
    __addevo(922, 923, [("LevelUp", None), ("Friendship", None)]) # Pawmot
    __addevo(924, 925, [("Level", 25), ("InBattle", None), ("ChanceText", 0.99)]) # Family of Four Maushold
    __addevo(924, 925.1, [("Level", 25), ("InBattle", None), ("Chance", 0.01)], 1) # Family of Three Maushold
    __addevo(926, 927, [("Level", 26)]) # Dachsbun
    __addevo(928, 929, [("Level", 25)]) # Dolliv
    __addevo(929, 930, [("Level", 35)]) # Arboliv
    __addevo(932, 933, [("Level", 24)]) # Naclstack
    __addevo(933, 934, [("Level", 48)]) # Garganacl
    __addevo(935, 936, [("UsedItem", Item.AuspiciousArmor)]) # Armarouge
    __addevo(935, 937, [("UsedItem", Item.MaliciousArmor)]) # Ceruledge
    __addevo(938, 939, [("UsedItem", "Thunder Stone")]) # Bellibolt
    __addevo(940, 941, [("Level", 25)]) # Kilowattrel
    __addevo(942, 943, [("Level", 30)]) # Mabosstiff
    __addevo(944, 945, [("Level", 28)]) # Grafaiai
    __addevo(946, 947, [("LevelUp", None), ("Friendship", None)]) # Brambleghast
    __addevo(948, 949, [("Level", 30)]) # Toedscruel
    __addevo(951, 952, [("UsedItem", "Fire Stone")]) # Scovillain
    __addevo(953, 954, [("LevelUp", None), ("Friendship", None)]) # Rabsca
    __addevo(955, 956, [("Level", 35)]) # Espathra
    __addevo(957, 958, [("Level", 24)]) # Tinkatuff
    __addevo(958, 959, [("Level", 38)]) # Tinkaton
    __addevo(960, 961, [("Level", 26)]) # Wugtrio
    __addevo(963, 964, [("Level", 38)]) # Palafin
    __addevo(965, 966, [("Level", 40)]) # Revavroom
    __addevo(969, 970, [("Level", 35)]) # Glimmora
    __addevo(971, 972, [("Level", 30), ("TimeOfDay", "Night")]) # Houndstone
    __addevo(974, 975, [("UsedItem", "Ice Stone")]) # Cetitan
    __addevo(996, 997, [("Level", 35)]) # Arctibax
    __addevo(997, 998, [("Level", 54)]) # Baxcalibur
    __addevo(999, 1000, [("Unimplemented", None)]) # Gholdengo - Unimplemented
    __addevo(1011, 1019, [("LevelUp", None), ("KnowsMove", "Dragon Cheer")]) # Hydrapple
    __addevo(1012, 1013, [("UsedItem", Item.UnremarkableTeacup)]) # Sinistcha (Counterfeit Form)
    __addevo(1012, 1013, [("UsedItem", Item.MasterpieceTeacup)]) # Sinistcha (Artisan Form)
