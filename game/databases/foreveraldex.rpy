init python:
    class ForeveralTypes:
        AddType = 0
        Training = 1
        AddSTAB = 2
        AddProficiency = 3
        Scaling = 4
        TurnStartStatus = 5
        FormSwap = 6
        AddAbility = 7
        Mega = 8
        MoveBoost = 9
        ReplaceType = 10

    class FVLMacros:
        FVLName = 0
        FVLTrainer = 1
        FVLLevel = 2
        FVLType = 3
        FVLTypeData = 4
        FVLMoves = 5
        FVLDescription = 6

    def lookupforeveraldata(name, datatype):
        for entry in foreveraldex:
            if (entry[FVLMacros.FVLName] == name):
                return entry[datatype]
    
    def FVLAbbreviation(fvl):
        if ("Foreveral" in fvl):
            return "FVL"
        elif ("Diveral" in fvl):
            return "DVL"
        elif ("Megaveral" in fvl):
            return "MVL"
        elif ("Gigaveral" in fvl):
            return "GVL"
        else:
            return "EVL"

    def GetAllForeveralNames():
        return [entry[FVLMacros.FVLName] for entry in foreveraldex]      

    foreveraldex = []
    #Name, Trainer, Level, Type, typedata, movesimparted, Description, 
    foreveraldex.append(["Clobbopus Foreveral", "Bea", 3, ForeveralTypes.AddType, ["Water"], ["Aqua Jet", "Bulk Up"], "Adds Water-type"])
    foreveraldex.append(["Tyrogue Everal", "Bea", 3, ForeveralTypes.Training, None, ["Power-Up Punch", "Low Kick"], "Using punching moves increases Defense EVs. Using kicking moves increases Attack EVs"])
    foreveraldex.append(["Timburr Foreveral", "Bea", 3, ForeveralTypes.AddSTAB, ["Grass"], ["Branch Poke", "Karate Chop"], "Adds Grass-type STAB"])

    foreveraldex.append(["Shuckle Foreveral", "Bea", 5, ForeveralTypes.AddAbility, ["Solid Rock"], ["Sticky Web", "Shore Up"], "Grants Solid Rock"])
    foreveraldex.append(["Rockruff Everal", "Bea", 5, ForeveralTypes.AddProficiency, ["Normal", "Fighting", "Dark"], ["Bite", "Quick Attack", "Rock Smash"], "Gains Proficiency from Normal, Fighting, and Dark-types"])
    foreveraldex.append(["Nacli Everal", "Bea", 5, ForeveralTypes.Scaling, ["Naclstack", 24], ["Rock Throw", "Rock Smash"], "Base stats scale to Naclstack at level 24"])
#
    foreveraldex.append(["Eevee Everal", "Blue", 3, ForeveralTypes.AddProficiency, ["Fire", "Water", "Electric", "Grass", "Fairy", "Dark", "Psychic", "Ice"], ["Tackle"], "Gains Proficiency from Fire, Water, Electric, Dark, Psychic, Grass, Ice, and Fairy-types", "You know why Eevee are the best? It's because they can be {i}anything{/i}, if they put the effort in. Any foe can be overcome by an Eevee, if the Eevee just tries. Heck, you could make a team of Eevee evolutions, and that'd be a pretty good team!"])
    foreveraldex.append(["Bagon Everal", "Blue", 3, ForeveralTypes.Scaling, ["Shelgon", 30], ["Aerial Ace", "Headbutt"], "Base stats scale to Shelgon at level 30", "There aren't a ton of dragons that think becoming a dumb cocoon is a good idea before they turn into a badass dragon. Bagon's one of them, though. But you got to admire its tenacity. It'll jump off cliffs, over and over, and over, to get the feeling of flying. It actually {i}works{/i} for its dream! Even if it mostly just hurts itself.."])
    foreveraldex.append(["Charmander Everal", "Blue", 3, ForeveralTypes.AddProficiency, ["Dragon", "Flying"], ["Dragon Rage", "Dragon Dance"], "Gain Proficiency from Dragon and Flying-types"])
#
    foreveraldex.append(["Swablu Everal", "Dawn", 3, ForeveralTypes.AddProficiency, ["Dragon", "Fairy"], ["Fairy Wind", "Dragon Rage"], "Gains Proficiency from Dragon and Fairy-types", "U-um... I really like Swablu... because, um, they're... I mean, they're really cute. And the way they hum is so... but, you know? They can become really strong. And they're never afraid to sing. They don't worry about if they sing well, or not well... they just {i}do{/i} it. That's... I want to be like that"])
    foreveraldex.append(["Snover Everal", "Dawn", 3, ForeveralTypes.Scaling, ["Abomasnow", 40], ["Mega Drain", "Razor Leaf"], "Base stats scale to Abomasnow at level 40"])
    foreveraldex.append(["Comfey Foreveral", "Dawn", 3, ForeveralTypes.MoveBoost, ["Floral Healing"], ["Ingrain", "Wish"], "Boosts Floral Healing. Effect: Heals an ally 50% of their health, or 66% on Grassy Terrain. {i}Also heals the user, and clears status conditions on both{/i}"])

    foreveraldex.append(["Frigibax Everal", "Dawn", 5, ForeveralTypes.Scaling, ["Arctibax", 35], ["Icy Wind", "Dragon Rage"], "Base stats scale to Arctibax at level 35"])
    foreveraldex.append(["Ninetales Diveral", "Dawn", 5, ForeveralTypes.FormSwap, [38, 38.1], ["Flame Burst", "Icy Wind"], "Swap between Kantonian/Alolan forms"])
    foreveraldex.append(["Cryogonal Foreveral", "Dawn", 5, ForeveralTypes.AddAbility, ["Prism Armor"], ["Barrier", "Amnesia"], "Grants Prism Armor"])
#
    foreveraldex.append(["Darumaka Diveral", "Flannery", 3, ForeveralTypes.FormSwap, [554, 554.1], ["Ember", "Powder Snow"], "Swap between Unovan/Galarian forms"])
    foreveraldex.append(["Magby Everal", "Flannery", 3, ForeveralTypes.Scaling, ["Magmar", 30], ["Ember", "Smog"], "Base stats scale to Magmar at level 30"])
    foreveraldex.append(["Cubone Everal", "Flannery", 3, ForeveralTypes.AddProficiency, ["Fire", "Ghost"], ["Shadow Punch", "Flame Charge"], "Gains Proficiency from Ghost and Fire-types"])

    foreveraldex.append(["Darmanitan Diveral", "Flannery", 5, ForeveralTypes.FormSwap, [555, 555.2], ["Fire Punch", "Ice Punch"], "Swap between Unovan/Galarian forms"])
    foreveraldex.append(["Heatmor Foreveral", "Flannery", 5, ForeveralTypes.MoveBoost, ["Fire Lash"], ["Leech Life", "Giga Drain"], "Boosts Fire Lash. Power: 80 -> 90. Effect: Lowers Defense. {i}Also heals the user, by 50% of the damage dealt{/i}"])
    foreveraldex.append(["Marowak Diveral", "Flannery", 5, ForeveralTypes.FormSwap, [105, 105.1], ["Shadow Bone", "Bone Rush", "Bonemerang", "Bone Club"], "Swap between Kantonian/Alolan forms"])
#
    foreveraldex.append(["Snorunt Everal", "Hilbert", 3, ForeveralTypes.AddProficiency, ["Ghost"], ["Hex", "Powder Snow"], "Gains Proficiency from Ghost-type. Male Snorunt can become Froslass"])
    foreveraldex.append(["Dhelmise Foreveral", "Hilbert", 3, ForeveralTypes.MoveBoost, ["Anchor Shot"], ["Aqua Jet", "Aqua Cutter"], "Boosts Anchor Shot. Power: 80 -> 90. Effect: Prevents opponent from switching. {i}Also lowers the opponent's Speed by one stage{/i}"])
    foreveraldex.append(["Piplup Everal", "Hilbert", 3, ForeveralTypes.AddProficiency, ["Steel"], ["Bubble", "Mirror Shot"], "Gains Proficiency from Steel-type"])

    foreveraldex.append(["Bergmite Everal", "Hilbert", 5, ForeveralTypes.AddProficiency, ["Rock"], ["Rock Throw", "Icy Wind"], "Gains Proficiency from Rock-type"])
    foreveraldex.append(["Riolu Everal", "Hilbert", 5, ForeveralTypes.AddProficiency, ["Steel"], ["Metal Claw", "Power-Up Punch"], "Gains Proficiency from Steel-type"])
    foreveraldex.append(["Prinplup Everal", "Hilbert", 5, ForeveralTypes.AddProficiency, ["Steel"], ["Bubble Beam", "Metal Claw"], "Gains Proficiency from Steel-type"])
#
    foreveraldex.append(["Mareanie Everal", "Hilda", 3, ForeveralTypes.Scaling, ["Toxapex", 38], ["Baneful Bunker", "Spikes"], "Base stats scale to Toxapex at level 38"])
    foreveraldex.append(["Varoom Everal", "Hilda", 3, ForeveralTypes.AddProficiency, ["Fairy", "Dark", "Fighting", "Fire"], ["Low Sweep", "Flame Charge"], "Gains Proficiency from Fairy, Dark, Fighting, and Fire-types"])
    foreveraldex.append(["Aron Foreveral", "Hilda", 3, ForeveralTypes.AddAbility, ["Filter"], ["Iron Defense", "Metal Claw"], "Grants Filter"])

    foreveraldex.append(["Geodude Diveral", "Hilda", 5, ForeveralTypes.FormSwap, [74, 74.1], ["Spark", "Mud-Slap"], "Swap between Kantonian/Alolan forms"])
    foreveraldex.append(["Graveler Diveral", "Hilda", 5, ForeveralTypes.FormSwap, [75, 75.1], ["Thunder Punch", "Magnitude"], "Swap between Kantonian/Alolan forms"])
    foreveraldex.append(["Pawniard Everal", "Hilda", 5, ForeveralTypes.Scaling, ["Bisharp", 52], ["Pursuit", "Metal Claw"], "Base stats scale to Bisharp at level 52"])
#
    foreveraldex.append(["Nidoran-X Diveral", "Janine", 3, ForeveralTypes.FormSwap, [29, 32], ["Swagger", "Flatter"], "Swap between Male/Female forms"])
    foreveraldex.append(["Salandit Everal", "Janine", 3, ForeveralTypes.AddAbility, ["Cute Charm"], ["Attract", "Captivate"], "Male Salandit can become Salazzle"])
    foreveraldex.append(["Mankey Everal", "Janine", 3, ForeveralTypes.AddProficiency, ["Ghost"], ["Low Kick", "Astonish"], "Gain Proficiency from Ghost-type"])
    
    foreveraldex.append(["Nidorin-X Diveral", "Janine", 5, ForeveralTypes.FormSwap, [30, 33], ["Frustration", "Return"], "Swap between Male/Female forms"])
    foreveraldex.append(["Seviper Foreveral", "Janine", 5, ForeveralTypes.MoveBoost, ["Poison Tail"], ["Brick Break", "Poison Tail"], "Boosts Poison Tail. Power: 50 -> 65. Effect: High crit rate. 10% chance to poison. {i}Double power on Normal-types{/i}"])
    foreveraldex.append(["Falinks Foreveral", "Janine", 5, ForeveralTypes.MoveBoost, ["No Retreat"], ["No Retreat", "Power-Up Punch"], "Boosts No Retreat. Effect: Boosts stats, but prevents switching. {i}Grants same effect to allies{/i}"])
#
    foreveraldex.append(["Bidoof Everal", "Professor Cherry", 3, ForeveralTypes.AddProficiency, ["Water"], ["Water Gun", "Super Fang"], "Gain Proficiency from Water-type"])
    foreveraldex.append(["Sunkern Everal", "Professor Cherry", 3, ForeveralTypes.Scaling, ["Arceus", 100], ["Sunny Day", "Mega Drain"], "Base stats scale to Arceus at level 100"])
    foreveraldex.append(["Zigzagoon Diveral", "Professor Cherry", 3, ForeveralTypes.FormSwap, [263, 263.1], ["Headbutt", "Bite"], "Switch between Hoennian/Galarian forms"])
#
    foreveraldex.append(["Drampa Foreveral", "Leaf", 3, ForeveralTypes.AddAbility, ["Friend Guard"], ["Dragon Rage", "Return"], "Grants Friend Guard"])
    foreveraldex.append(["Tynamo Everal", "Leaf", 3, ForeveralTypes.Scaling, ["Eelektrik", 39], ["Bounce", "Dive"], "Base stats scale to Eelektrik at level 39"])
    foreveraldex.append(["Mareep Everal", "Leaf", 3, ForeveralTypes.AddProficiency, ["Dragon"], ["Dragon Breath", "Cotton Guard"], "Gain Proficiency from Dragon-type"])
#    
    foreveraldex.append(["Makuhita Everal", "May", 3, ForeveralTypes.AddProficiency, ["Electric"], ["Thunder Punch", "Charge"], "Gain proficiency from Electric-type"])
    foreveraldex.append(["Burmy Everal", "May", 3, ForeveralTypes.AddProficiency, ["Steel", "Grass", "Ground", "Flying"], ["Shore Up", "Camouflage"], "Gains Proficiency from Steel, Grass, Ground, and Flying classes"])
    foreveraldex.append(["Spidops Foreveral", "May", 3, ForeveralTypes.MoveBoost, ["Silk Trap"], ["Silk Trap", "Sticky Web"], "Boosts Silk Trap. Effect: Blocks damaging moves and lowers speed of foes that make contact. {i}Also blocks status moves{/i}"])

    foreveraldex.append(["Heracross Megaveral", "May", 5, ForeveralTypes.Mega, [Item.Heracronite, 214.1], ["Arm Thrust", "Pin Missile"], "Generates Heracronite at start of turn"])
    foreveraldex.append(["Mothim Foreveral", "May", 5, ForeveralTypes.MoveBoost, ["Bug Bite"], ["Bug Bite", "Leech Life"], "Boosts Bug Bite. Effect: Does damage and eats foe's berry. {i}In first move slot: Its secondary type becomes the type of the food item it is holding on switch-in{/i}"])
    foreveraldex.append(["Wormadam Diveral", "May", 5, ForeveralTypes.FormSwap, [413, 413.1, 413.2], ["Earth Power", "Energy Ball", "Flash Cannon"], "Swap between Wormadam forms"])
#
    foreveraldex.append(["Wooper Diveral", "Misty", 3, ForeveralTypes.FormSwap, [194, 194.1], ["Sludge", "Bubble Beam"], "Switch between Johtonian/Paldean forms"])
    foreveraldex.append(["Seel Everal", "Misty", 3, ForeveralTypes.AddProficiency, ["Ice"], ["Bubble Beam", "Powder Snow"], "Gain Proficiency from Ice-type"])
    foreveraldex.append(["Azurill Everal", "Misty", 3, ForeveralTypes.AddProficiency, ["Water"], ["Aqua Jet", "Bounce"], "Gain Proficiency from Water-type"])
    
    foreveraldex.append(["Frillish Everal", "Misty", 5, ForeveralTypes.Scaling, ["Jellicent", 40], ["Hex", "Will-O-Wisp"], "Base stats scale to Jellicent at level 40"])
    foreveraldex.append(["X-sire Diveral", "Misty", 5, ForeveralTypes.FormSwap, [195, 980], ["Waterfall", "Poison Jab"], "Swap between Quagsire and Clodsire"])
    foreveraldex.append(["Castform Foreveral", "Misty", 5, ForeveralTypes.MoveBoost, ["Sunny Day", "Rain Dance", "Hail", "Snowscape"], ["Sunny Day", "Rain Dance", "Hail", "Snowscape"], "Boosts Sunny Day, Rain Dance, Hail, and Snowscape. Effect: Sets up weather. {i}In first move slot: activates automatically on switch-in for three PP{/i}"])
#
    foreveraldex.append(["Bonsly Everal", "Nessa", 3, ForeveralTypes.AddType, ["Grass"], ["Branch Poke", "Ingrain"], "Adds Grass-type"])
    foreveraldex.append(["Binacle Foreveral", "Nessa", 3, ForeveralTypes.AddAbility, ["Sap Sipper"], ["Bug Bite", "Sludge"], "Grants Sap Sipper"])
    foreveraldex.append(["Wishiwashi Foreveral", "Nessa", 3, ForeveralTypes.AddAbility, ["Swift Swim"], ["Shore Up", "Fillet Away"], "Grants Swift Swim"])

    foreveraldex.append(["Slowpoke Diveral", "Nessa", 5, ForeveralTypes.FormSwap, [79, 79.1], ["Amnesia", "Yawn"], "Switch between Kantonian/Galarian forms"])
    foreveraldex.append(["Veluza Foreveral", "Nessa", 5, ForeveralTypes.MoveBoost, ["Fillet Away"], ["Fillet Away", "Heart Stamp"], "Boosts Fillet Away. Effect: Halves HP to boost stats. {i}Also purifies status conditions{/i}"])
    foreveraldex.append(["Chinchou Foreveral", "Nessa", 5, ForeveralTypes.AddAbility, ["Water Absorb"], ["Charge", "Aqua Ring"], "Grants Water Absorb"])
#
    foreveraldex.append(["Joltik Everal", "Rosa", 3, ForeveralTypes.Scaling, ["Galvantula", 36], ["Bug Bite", "Electroweb"], "Base stats scale to Galvantula at level 36"])
    foreveraldex.append(["Kricketot Foreveral", "Rosa", 3, ForeveralTypes.AddType, ["Normal"], ["Uproar", "Sing"], "Adds Normal-type"])
    foreveraldex.append(["Kricketune Foreveral", "Rosa", 3, ForeveralTypes.AddType, ["Normal"], ["Hyper Voice", "Perish Song"], "Adds Normal-type"])

    foreveraldex.append(["Paras Everal", "Rosa", 5, ForeveralTypes.AddProficiency, ["Ghost"], ["Rain Dance", "Recover"], "Gain Proficiency from Ghost-type"])
    foreveraldex.append(["Parasect Foreveral", "Rosa", 5, ForeveralTypes.ReplaceType, [("Grass", "Ghost")], ["Rain Dance", "Recover"], "Replaces Grass-type with Ghost"])
    foreveraldex.append(["Toxel Everal", "Rosa", 5, ForeveralTypes.AddAbility, ["Moody"], ["Poison Sting", "Thunder Shock"], "Grants Moody. Nature will change randomly at the end of every turn"])

    foreveraldex.append(["Toxtricity Gigaveral", "Rosa", 7, ForeveralTypes.Mega, [Item.MinigigaToxtricistar, 849.2], ["Overdrive", "Sludge Bomb"], "Generates Minigiga Toxtricistar at start of turn"])
    foreveraldex.append(["Galvantula Foreveral", "Rosa", 7, ForeveralTypes.MoveBoost, ["Electroweb"], ["Electroweb", "Zap Cannon"], "Boosts Electroweb. Power: 55 -> 80. Effect: Does damage and lowers speed. {i}Also lowers evasion and traps opponent{/i}"])
    foreveraldex.append(["Leavanny Foreveral", "Rosa", 7, ForeveralTypes.AddAbility, ["Sharpness"], ["Leaf Blade", "X-Scissor"], "Grants Sharpness"])
#
    foreveraldex.append(["Misdreavus Everal", "Sabrina", 3, ForeveralTypes.Scaling, ["Mismagius", 50], ["Mean Look", "Perish Song"], "Base stats scale to Mismagius at level 50"])
    foreveraldex.append(["Meditite Everal", "Sabrina", 3, ForeveralTypes.Training, None, ["Karate Chop", "Confusion"], "Using fighting moves increases Attack EVs. Using psychic moves increases Special Defense EVs"])
    foreveraldex.append(["Litwick Everal", "Sabrina", 3, ForeveralTypes.Scaling, ["Lampent", 41], ["Will-O-Wisp", "Hex"], "Base stats scale to Lampent at level 41"])

    foreveraldex.append(["Hypno Foreveral", "Sabrina", 5, ForeveralTypes.AddAbility, ["Bad Dreams"], ["Hypnosis", "Dream Eater"], "Grants Bad Dreams"])
    foreveraldex.append(["Espurr Foreveral", "Sabrina", 5, ForeveralTypes.AddAbility, ["Aftermath"], ["Calm Mind", "Stored Power"], "Grants Aftermath"])
    foreveraldex.append(["Shuppet Foreveral", "Sabrina", 5, ForeveralTypes.MoveBoost, ["Spite"], ["Spite", "Grudge"], "Boosts Spite. Effect: {i}Removes all PP from this move, and the opponent's most-recently used move{/i}"])
#
    foreveraldex.append(["Rhyhorn Foreveral", "Serena", 3, ForeveralTypes.AddAbility, ["Speed Boost"], ["Bulldoze", "Accelerock"], "Grants Speed Boost"])
    foreveraldex.append(["Sandile Foreveral", "Serena", 3, ForeveralTypes.AddAbility, ["Strong Jaw"], ["Fire Fang", "Thunder Fang"], "Grants Strong Jaw"])
    foreveraldex.append(["Litten Everal", "Serena", 3, ForeveralTypes.AddProficiency, ["Dark"], ["Flame Burst", "Bite"], "Gain Proficiency from Dark-type"])
#
    foreveraldex.append(["Zubat Foreveral", "Silver", 3, ForeveralTypes.AddAbility, ["Regenerator"], ["Parting Shot", "Baton Pass"], "Grants Regenerator"])
    foreveraldex.append(["Golbat Foreveral", "Silver", 3, ForeveralTypes.AddAbility, ["Regenerator"], ["Volt Switch", "Flip Turn"], "Grants Regenerator"])
    foreveraldex.append(["Nymble Everal", "Silver", 3, ForeveralTypes.AddProficiency, ["Dark"], ["Parting Shot", "U-turn"], "Gain Proficiency from Dark-type"])
    
    foreveraldex.append(["Crobat Foreveral", "Silver", 5, ForeveralTypes.AddAbility, ["Regenerator"], ["U-turn", "Teleport"], "Grants Regenerator"])
    foreveraldex.append(["Absol Megaveral", "Silver", 5, ForeveralTypes.Mega, [Item.Absolite, 359.1], ["Night Slash", "Spirit Break"], "Generates Absolite at start of turn"])
    foreveraldex.append(["Lokix Foreveral", "Silver", 5, ForeveralTypes.AddSTAB, ["Fighting"], ["Beat Up", "Retaliate"], "Adds Fighting-Type STAB"])
#    
    foreveraldex.append(["Ducklett Foreveral", "Skyla", 3, ForeveralTypes.AddAbility, ["Regenerator"], ["U-turn", "Flip Turn"], "Grants Regenerator"])
    foreveraldex.append(["Lapras Gigaveral", "Skyla", 3, ForeveralTypes.Mega, [Item.MinigigaLaprastar, 131.1], ["Aurora Veil", "Hail"], "Generates Minigiga Laprastar at start of turn"])
    foreveraldex.append(["Cramorant Foreveral", "Skyla", 3, ForeveralTypes.TurnStartStatus, ["gorging"], ["Stockpile", "Swallow", "Spit Up"], "Start in Gorging Form"])
#
    foreveraldex.append(["Yamper Foreveral", "Sonia", 3, ForeveralTypes.AddAbility, ["Fluffy"], ["Bite", "Attract"], "Grants Fluffy"])
    foreveraldex.append(["Togedemaru Foreveral", "Sonia", 3, ForeveralTypes.AddAbility, ["Rough Skin"], ["Spiky Shield", "Wide Guard"], "Grants Rough Skin"])
    foreveraldex.append(["Growlithe Foreveral", "Sonia", 3, ForeveralTypes.AddAbility, ["Strong Jaw"], ["Bite", "Thunder Fang"], "Grants Strong Jaw"])#On evolution, grant Psychic Fangs and Ice Fang 

    foreveraldex.append(["Stunfisk Diveral", "Sonia", 5, ForeveralTypes.FormSwap, [618, 618.1], ["Discharge", "Iron Head"], "Swap between Unovan/Galarian forms"])
    foreveraldex.append(["Boltund Foreveral", "Sonia", 5, ForeveralTypes.AddAbility, ["Speed Boost"], ["Electro Ball", "Baton Pass"], "Grants Speed Boost"])
    foreveraldex.append(["Turtonator Foreveral", "Sonia", 5, ForeveralTypes.AddAbility, ["Aftermath"], ["Mind Blown", "Explosion"], "Grants Aftermath"])
#
    foreveraldex.append(["Noibat Foreveral", "Tia", 3, ForeveralTypes.AddSTAB, ["Normal"], ["Uproar", "Disarming Voice"], "Grants Normal-type STAB"])
    foreveraldex.append(["Mime Jr. Everal", "Tia", 3, ForeveralTypes.AddProficiency, ["Ice"], ["Draining Kiss", "Powder Snow"], "Gain Proficiency from Ice-type"])
    foreveraldex.append(["Trapinch Everal", "Tia", 3, ForeveralTypes.AddProficiency, ["Bug", "Dragon"], ["Bug Bite", "Dragon Breath"], "Gain Proficiency from Dragon and Bug-types"])

    foreveraldex.append(["Baltoy Everal", "Tia", 5, ForeveralTypes.Scaling, ["Claydol", 36], ["Iron Defense", "Amnesia"], "Base stats scale to Claydol at level 36"])
    foreveraldex.append(["Claydol Foreveral", "Tia", 5, ForeveralTypes.AddAbility, ["Solid Rock"], ["Recover", "Rapid Spin"], "Grants Solid Rock"])
    foreveraldex.append(["Mr. Mime Diveral", "Tia", 5, ForeveralTypes.FormSwap, [122, 122.1], ["Draining Kiss", "Powder Snow"], "Swap between Kantonian/Galarian forms"])
#
    foreveraldex.append(["Munchlax Foreveral", "Whitney", 3, ForeveralTypes.AddAbility, ["Harvest"], ["Slack Off", "Uproar"], "Grants Harvest"])
    foreveraldex.append(["Ralts Everal", "Whitney", 3, ForeveralTypes.AddProficiency, ["Fighting"], ["Draining Kiss", "Vacuum Wave"], "Gain Proficiency from Fighting-type"])
    foreveraldex.append(["Happiny Everal", "Whitney", 3, ForeveralTypes.AddAbility, ["Regenerator"], ["Seismic Toss", "Soft-Boiled"], "Grants Regenerator"])

    foreveraldex.append(["Lopunny Megaveral", "Whitney", 5, ForeveralTypes.Mega, [Item.Lopunnite, 428.1], ["Return", "Power-Up Punch"], "Generates Lopunnite at start of turn"])#move this back later
    foreveraldex.append(["Chansey Everal", "Whitney", 5, ForeveralTypes.AddAbility, ["Regenerator"], ["Thunder Wave", "Encore"], "Grants Regenerator"])
    foreveraldex.append(["Audino Megaveral", "Whitney", 5, ForeveralTypes.Mega, [Item.Audinite, 531.1], ["Aqua Ring", "Grassy Terrain"], "Generates Audinite at start of turn"])
#
    foreveraldex.append(["Swinub Everal", "Jasmine", 3, ForeveralTypes.Scaling, ["Piloswine", 33], ["Ice Shard", "Bulldoze"], "Base stats scale to Piloswine at level 33"])
    foreveraldex.append(["Bunnelby Everal", "Jasmine", 3, ForeveralTypes.AddProficiency, ["Ground"], ["Dig", "Mud-Slap"], "Gain Proficiency from Ground-type"])
    foreveraldex.append(["Magnemite Everal", "Jasmine", 3, ForeveralTypes.Scaling, ["Magneton", 30], ["Magnet Bomb", "Thunder Shock"], "Base stats scale to Magneton at level 30"])

    foreveraldex.append(["Drilbur Everal", "Jasmine", 5, ForeveralTypes.AddProficiency, ["Steel"], ["Metal Claw", "Sand Tomb"], "Gain Proficiency from Steel-type"])
    foreveraldex.append(["Diggersby Foreveral", "Jasmine", 5, ForeveralTypes.AddAbility, ["Mold Breaker"], ["Extreme Speed", "Dig"], "Grants Mold Breaker"])
    foreveraldex.append(["Skarmory Foreveral", "Jasmine", 5, ForeveralTypes.MoveBoost, ["Steel Wing"], ["Steel Wing", "Roost"], "Boosts Steel Wing. Power: 70 -> 90. Effect: {i}Has a 30% chance of boosting Defense and Special Defense{/i}"])
#
    foreveraldex.append(["Tyrunt Everal", "Raihan", 3, ForeveralTypes.Scaling, ["Tyrantrum", 39], ["Ice Fang", "Thunder Fang"], "Base stats scale to Tyrantrum at level 39"])
    foreveraldex.append(["Minior Foreveral", "Raihan", 3, ForeveralTypes.MoveBoost, ["Shell Smash"], ["Shell Smash", "Power Gem"], "Boosts Shell Smash. Effect: Decreases defense to increase offense. {i}Will always move last{/i}"])
    foreveraldex.append(["Dreepy Everal", "Raihan", 3, ForeveralTypes.Scaling, ["Drakloak", 50], ["Shadow Sneak", "Dragon Rage"], "Base stats scale to Drakloak at level 50"])
#
    foreveraldex.append(["Sigilyph Foreveral", "Bianca", 3, ForeveralTypes.AddAbility, ["Simple"], ["Stored Power", "Calm Mind"], "Grants Simple"])
    foreveraldex.append(["Stantler Everal", "Bianca", 3, ForeveralTypes.AddProficiency, ["Psychic"], ["Return", "Psybeam"], "Gain Proficiency from Psychic-type"])
    foreveraldex.append(["Glameow Everal", "Bianca", 3, ForeveralTypes.Scaling, ["Purugly", 38], ["Covet", "Fake Out"], "Base stats scale to Purugly at level 38"])
#
    foreveraldex.append(["Cyndaquil Everal", "Ethan", 3, ForeveralTypes.AddProficiency, ["Ghost"], ["Defense Curl", "Rollout"], "Gain Proficiency from Ghost-type"])
    foreveraldex.append(["Quilava Everal", "Ethan", 3, ForeveralTypes.AddProficiency, ["Ghost"], ["Flame Burst", "Flame Charge"], "Gain Proficiency from Ghost-type"])
    foreveraldex.append(["Aipom Foreveral", "Ethan", 3, ForeveralTypes.AddAbility, ["Technician"], ["Covet", "Fake Out"], "Grants Technician"])
#
    foreveraldex.append(["Sandshrew Diveral", "Nate", 3, ForeveralTypes.FormSwap, [27, 27.1], ["Rollout", "Ice Ball"], "Swap between Kantonian/Alolan forms"])
    foreveraldex.append(["Skrelp Everal", "Nate", 3, ForeveralTypes.AddProficiency, ["Dragon"], ["Dragon Rage", "Dragon Breath"], "Gain Proficiency from Dragon-type"])
    foreveraldex.append(["Grimer Diveral", "Nate", 3, ForeveralTypes.FormSwap, [88, 88.1], ["Sludge", "Bite"], "Swap between Kantonian/Alolan forms"])

    foreveraldex.append(["Ferroseed Everal", "Nate", 5, ForeveralTypes.Scaling, ["Ferrothorn", 40], ["Ingrain", "Curse"], "Base stats scale to Ferrothorn at level 40"])
    foreveraldex.append(["Sandslash Diveral", "Nate", 5, ForeveralTypes.FormSwap, [28, 28.1], ["Avalanche", "Revenge"], "Swap between Kantonian/Alolan forms"])
    foreveraldex.append(["Trubbish Foreveral", "Nate", 5, ForeveralTypes.Scaling, ["Garbodor", 36], ["Fling", "Camouflage"], "Base stats scale to Garbodor at level 36"])
#
    foreveraldex.append(["Turtwig Everal", "Erika", 3, ForeveralTypes.AddProficiency, ["Ground"], ["Bite", "Withdraw"], "Gain Proficiency from Ground-type"])#Maybe swap these to Brendan later
    foreveraldex.append(["Grotle Everal", "Erika", 3, ForeveralTypes.AddProficiency, ["Ground"], ["Crunch", "Iron Defense"], "Gain Proficiency from Ground-type"])
    foreveraldex.append(["Foongus Everal", "Erika", 3, ForeveralTypes.Scaling, ["Amoonguss", 39], ["Rain Dance", "Moonlight"], "Base stats scale to Amoonguss at level 39"])# GIVE AMOONGUS IMPOSTER
#
    foreveraldex.append(["Frosmoth Foreveral", "Grusha", 3, ForeveralTypes.AddAbility, ["Fluffy"], ["Snowscape", "Aurora Veil"], "Grants Fluffy"])
    foreveraldex.append(["Archen Everal", "Grusha", 3, ForeveralTypes.Scaling, ["Archeops", 37], ["Wing Attack", "Rock Throw"], "Base stats scale to Archeops at level 37"])
    foreveraldex.append(["Drifloon Foreveral", "Grusha", 3, ForeveralTypes.AddType, ["Fire"], ["Flame Burst", "Will-O-Wisp"], "Adds Fire-type"])
#
    foreveraldex.append(["Eevee Diveral", "Blue", 11, ForeveralTypes.AddAbility, ["Tetra Element"], ["Leaf Blade", "Flare Blitz", "Surf", "Thunderbolt", "Ice Beam", "Moonblast", "Foul Play", "Psychic"], "Grants Tetra Element. Its power is imperfect"])
    foreveraldex.append(["Pichu Everal", "Ethan", 11, ForeveralTypes.Scaling, ["Pichu", 100], ["Zippy Zap", "Floaty Fall", "Splishy Splash"], "Base stats scale based on destined defeats by the opponent. Its power is imperfect"])
    foreveraldex.append(["Wimpod Foreveral", "Klara", 5, ForeveralTypes.AddAbility, ["Intimidate"], ["First Impression", "U-turn", "Flip Turn", "Aqua Jet"], "Grants Intimidate. Its power is imperfect"])
    foreveraldex.append(["Vespiquen Uneveral", "Klara", 11, ForeveralTypes.MoveBoost, ["Attack Order", "Defend Order", "Heal Order"], ["Attack Order", "Defend Order", "Heal Order"], "Boosts Attack Order. Effect: High crit rate. \n{i}Also boosts allied Beedrill's offense.{/i}\nBoosts Defense Order. Effect: Raises defenses. \n{i}Also summons allied Beedrill.{/i}\nBoosts Heal Order. Effect: Heals self. \n{i}Also heals allied Beedrill.{/i}\nForces unevolution. Its power is imperfect"])

