init python:
    def GetTrainerTeam(name, specific=None, heal=True):#when adding teams, unless you've got a good reason, make ace offset +1, and nothing higher
        name = name.title()
        teammembers = []
        if (name not in npcteams.keys()):
            npcteams[name] = {}
        level = AimLevel()
        
        if (name == "Jasmine"):#give her a skarmory eventually
            teammembers = ["Hippopotas", "Steelix", "Magnemite", "Drilbur", "Pineco"] #"Skarmory",//this is already going to be a hard fight, let's not go crazy
            for teammate in ([specific] if specific != None else teammembers):#base level here is level >= 16
                if (teammate == "Drilbur"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Drilbur", level=level, moves=["Metal Claw", "Dig", GetMove('Mud-Slap'), "Rapid Spin"], ability="Sand Force", intelligence=1, offset=0)
                elif (teammate == "Steelix"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Steelix", level=level + 1, moves=["Curse", "Bulldoze", GetMove('Rock Tomb'), "Thunder Fang"], ability="Sheer Force", intelligence=1, offset=1)
                #elif (teammate == "Skarmory"):
                #    npcteams[name][teammate] = Pokemon("Skarmory", level=level, moves=["Metal Claw", "Peck", GetMove('Sand Attack'), "Whirlwind"], ability="Sturdy", intelligence=1, offset=0)
                elif (teammate == "Magnemite"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Magnemite", level=level - 1, moves=["Magnet Rise", "Light Screen", GetMove('Thunder Shock'), "Magnet Bomb"], ability="Magnet Pull", intelligence=1, offset=-1)
                elif (teammate == "Pineco"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Pineco", level=level - 2, moves=[GetMove("Self-Destruct"), "Bug Bite", GetMove('Rapid Spin'), "Protect"], ability="Sturdy", intelligence=1, offset=-2)
                elif (teammate == "Hippopotas"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Hippopotas", level=level - 2, moves=["Bite", "Yawn", GetMove('Sand Attack'), "Sandstorm"], gender=Genders.Male, ability="Sand Stream", intelligence=1, offset=-2)
                npcteams[name][teammate].UpdateLevel(level, False)

        elif (name == "Blue"):
            level = GetHighestLevelAll()
            teammembers = ["Eevee"]
            if (IsAfter(8, 4, 2004)):
                teammembers += ["Pidgeotto"]
            if (AimLevel() >= 9):
                teammembers += ["Charmander"]
            if (AimLevel() >= 13):
                teammembers += ["Magikarp", "Exeggcute"]
            if (HasEvent("Leaf", "LentDratini")):
                teammembers.append("Dratini")
            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Magikarp"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Magikarp", level=15, moves=["Bounce", "Tackle"], nature=Natures.Rash, gender=Genders.Male)
                    if (level >= 20):
                        npcteams[name][teammate].Id = pokedexlookupname("Gyarados", DexMacros.Id)
                        npcteams[name][teammate].Ability = "Intimidate"
                        npcteams[name][teammate].UpdateMoves(["Bounce", "Tackle", "Thrash", "Bite"])
                elif (teammate == "Dratini"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = GetTrainerTeam("Leaf", "Dratini", heal)
                elif (teammate == "Pidgeotto"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Pidgeotto", level=18, offset = 3, moves=["Quick Attack", "Sand Attack", "Gust"], gender=Genders.Male, ability="Keen Eye")
                    if (level >= 22):
                        npcteams[name][teammate].UpdateMoves(["Twister", "Roost", "Wing Attack", "Sand Attack"])
                    elif (level >= 9):
                        npcteams[name][teammate].UpdateMoves(["Tackle", "Quick Attack", "Sand Attack", "Gust"])
                elif (teammate == "Eevee"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Eevee", level=5, moves=["Tackle", "Sand Attack", "Tail Whip", "Growl"], gender=Genders.Male, ability="Run Away")
                    if (level >= 20):
                        npcteams[name][teammate].UpdateMoves(["Swift", "Bite", "Quick Attack", "Sand Attack"])
                    elif (level >= 17):
                        npcteams[name][teammate].UpdateMoves(["Bite", "Quick Attack", "Swift", GetMove("Baby-Doll Eyes")])
                    elif (level >= 8):
                        npcteams[name][teammate].UpdateMoves(["Tackle", "Sand Attack", "Tail Whip", "Growl"])
                    if (IsAfter(23, 5, 2004) or (IsDate(23, 5, 2004) and timeOfDay == "Midnight")):
                        npcteams[name][teammate].Foreverals = ["Eevee Diveral"]
                elif (teammate == "Exeggcute"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Exeggcute", level=13, moves=["Leech Seed", "Hypnosis", "Reflect", "Uproar"], nature=Natures.Jolly, gender=Genders.Female, offset=-1)
                    if (level >= 17):
                        npcteams[name][teammate].UpdateMoves(["Hypnosis","Bark Up","Leech Seed","Bullet Seed"])
                elif (teammate == "Charmander"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Charmander", level=10, nature=Natures.Timid, moves=["Smokescreen", "Ember", "Growl", "Scratch"], gender=Genders.Male, ability="Blaze")
                    if (level >= 16):
                        npcteams[name][teammate].Id = 5
                        npcteams[name][teammate].UpdateMoves(["Ember","Dragon Rage","Smokescreen","Steady Flame"])
                npcteams[name][teammate].UpdateLevel(level, False)

        elif (name == "Leaf"):
            teammembers = ["Helioptile", "Bulbasaur", "Dratini"]
            if (level >= 13):
                teammembers += ["Drampa"]
            if (IsAfter(4, 5, 2004)):
                teammembers += ["Jigglypuff"]

            if (HasEvent("Leaf", "LentDratini")):
                teammembers.remove("Dratini")
            
            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Helioptile"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon(694, level=11, gender=Genders.Female, moves=["Pound", "Tail Whip", "Thunder Shock"], nature=Natures.Quirky, ability="Solar Power")#Leaf's Helioptile
                    if (level >= 16):
                        npcteams[name][teammate].UpdateMoves(["Quick Attack", "Mud-Slap", "Energize", "Thunder Shock"])
                    elif (level >= 13):
                        npcteams[name][teammate].UpdateMoves(["Pound","Mud-Slap","Thunder Shock","Charge"])
                    elif (level >= 11):
                        npcteams[name][teammate].UpdateMoves(["Pound","Tail Whip","Thunder Shock","Charge"])
                elif (teammate == "Dratini"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Dratini", level=15, offset=1, moves=["Dragon Rage", "Thunder Wave", "Leer", "Twister"], nature=Natures.Jolly, ivs=[31, 31, 31, 31, 31, 31], ability="Shed Skin")
                    if (level >= 16):
                        npcteams[name][teammate].UpdateMoves(["Dragon Rage", "Twister", "Dragon Tail", "Legacy"])
                    elif (level >= 15):
                        npcteams[name][teammate].UpdateMoves(["Wrap","Thunder Wave","Twister","Dragon Rage"])
                elif (teammate == "Bulbasaur"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon(1, level=7, gender=Genders.Male, moves=["Tackle", "Growl", "Vine Whip"], nature=Natures.Modest, ability="Chlorophyll")
                    if (level >= 16):
                        npcteams[name][teammate].Id = 2
                        npcteams[name][teammate].UpdateMoves(["Leech Seed", "Vine Whip", "Bark Up", "Bad Breath"])
                    elif (level >= 13):
                        npcteams[name][teammate].UpdateMoves(["Sleep Powder","Poison Powder","Tackle", "Vine Whip"])
                elif (teammate == "Drampa"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Drampa", level=14, moves=["Glare", "Protect", "Twister", "Echoed Voice"], nature = Natures.Gentle, ability="Berserk", offset=-1)
                    if (level >= 16):
                        npcteams[name][teammate].UpdateMoves(["Legacy","Echoed Voice","Protect","Twister"])
                elif (teammate == "Jigglypuff"):
                    npcteams[name][teammate] = Pokemon("Jigglypuff", AimLevel() - 1, moves=["Pound", "Sing", "Disarming Voice", "Disable"], gender=Genders.Female, nature=Natures.Lonely, ability="Friend Guard", offset = -1, intelligence = 1)
                npcteams[name][teammate].UpdateLevel(level, False)

        elif (name == "Ethan"):
            teammembers = []
            for mon in playerparty:
                if (mon.Id != 25.2):
                    teammembers.append(mon.GetId())
                    movecopies = []
                    for move in mon.GetMoves():
                        movecopies.append(GetMove(move.Name))
                    npcteams[name][mon.GetId()] = Pokemon(mon.GetId(), AimLevel() - 1, offset=0, ability=mon.GetAbility(), nature=mon.GetNature(), moves=movecopies, gender=mon.GetGender(), ivs=[1, 1, 1, 1, 1, 1], intelligence = 1)
                    npcteams[name][mon.GetId()].ShinyValue = 2#prevent his 'mons from being shiny
                else:
                    teammembers.append("Pichu")
                    npcteams[name]["Pichu"] = Pokemon(172.1, AimLevel(), ability="Small World", nature=Natures.Naughty, gender=Genders.Female, ivs=[1, 1, 1, 1, 1, 1], intelligence = 1)
                    npcteams[name]["Pichu"].ShinyValue = 2#prevent his 'mons from being shiny

                    if (IsAfter(26, 5, 2004)):
                        npcteams[name]["Pichu"].Foreverals = ["Pichu Everal"]
                        npcteams[name]["Pichu"].UpdateMoves(["Splishy Splash", "Zippy Zap", "Floaty Fall", "Nuzzle"])
                        npcteams[name]["Pichu"].IVs = [31, 31, 31, 31, 31, 31]
                
            if (GetRelationshipRank("Ethan") > 0):
                teammembers.remove("Pichu")
                teammembers.remove(random.choice(teammembers))
                teammembers.append("Quilava")
                if ("Quilava" not in npcteams[name]):
                    npcteams[name]["Quilava"] = Pokemon("Quilava", level = AimLevel() + 1, moves=["Flame Wheel", "Quick Attack", "Smokescreen", "Steady Flame"], gender=Genders.Male, nature=Natures.Impish, offset=1, intelligence=1)#Exbo
                teammembers.append("Pichu")

        elif (name == "Yellow"):
            teammembers = ["Rattata", "Pichu"]
            for teammate in ([specific] if specific != None else teammembers):#base level here is level >= 16
                if (teammate == "Rattata"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Rattata", AimLevel() - 2, moves = ["Pursuit", "Bite", "Tackle", "Quick Attack"], gender=Genders.Male, offset=-2, ability="Run Away", ivs=[31, 31, 31, 31, 31, 31], intelligence=1)
                elif (teammate == "Pichu"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon(172.1, AimLevel() - 3, moves = ["Nasty Plot", "Sweet Kiss", "Charm", "Tail Whip"], gender=Genders.Female, offset=-3, nickname = "Chuchu", ability="Small World", nature=Natures.Mild, ivs=[31, 31, 31, 31, 31, 31], intelligence=1)
                npcteams[name][teammate].UpdateLevel(level, False)

        elif (name == "Erika"):
            teammembers = ["Nidorina", "Glimmet", "Gloom"]
            if (level >= 16):
                teammembers += ["Poltchageist", "Turtwig", "Wooper"]
            for teammate in ([specific] if specific != None else teammembers):#default is level >= 16
                if (teammate == "Nidorina"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Nidorina", level=20, offset=1, gender=Genders.Female, moves=["Toxic Spikes", "Growl", "Tail Whip"], ability="Rivalry", intelligence=1)
                    if (level >= 16):
                        npcteams[name][teammate].UpdateMoves(["Toxic Spikes", "Growl", "Poison Sting", "Double Kick"])
                elif (teammate == "Glimmet"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Glimmet", level=20, offset=2, gender=Genders.Female, moves=["Toxic Spikes", "Stealth Rock", "Rock Polish", "Spikes"], ability="Toxic Debris", intelligence=1)
                    if (level >= 16):
                        npcteams[name][teammate].UpdateMoves(["Toxic Spikes", "Stealth Rock", "Spikes", "Ancient Power"])
                elif (teammate == "Gloom"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Gloom", level=21, offset=3, gender=Genders.Female, moves=["Toxic", "Protect", "Stun Spore"], ability="Stench", intelligence=1)
                    if (level >= 16):
                        npcteams[name][teammate].UpdateMoves(["Bad Breath", "Protect", "Bark Up", "Mega Drain"])
                elif (teammate == "Poltchageist"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Poltchageist", AimLevel() - 1, moves = ["Absorb", "Astonish", "Life Dew", "Withdraw"], gender=Genders.Unknown, offset=-1, ability="Hospitality", intelligence=1)
                elif (teammate == "Turtwig"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Turtwig", AimLevel() - 2, moves = ["Stealth Rock", "Roar", "Razor Leaf", "Absorb"], gender=Genders.Female, offset=-2, ability="Shell Armor", intelligence=1)
                elif (teammate == "Wooper"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon(194.1, AimLevel() - 3, moves = ["Spikes", "Stealth Rock", "Toxic Spikes", "Mud Shot"], gender=Genders.Female, offset=-3, ability="Unaware", intelligence=1)
                npcteams[name][teammate].UpdateLevel(level, False)

        elif (name == "Cheren"):
            teammembers = ["Purrloin"]
            if (level >= 13):
                teammembers += ["Pidove", "Lillipup", "Carvanha"]
            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Purrloin"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon(509, gender=Genders.Female, ability="Prankster", offset=-1)
                    if (level >= 16):
                        npcteams[name][teammate].UpdateMoves(["Pursuit", "Assist", "Scratch", "Growl"])
                    elif (level >= 13):
                        npcteams[name][teammate].UpdateMoves(["Growl", "Assist", "Sand Attack", "Scratch"])
                elif (teammate == "Pidove"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Pidove", level=8, moves=["Fly"], nature=Natures.Bashful, gender=Genders.Male, ability="Rivalry", offset=-2)
                elif (teammate == "Lillipup"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Lillipup", level=6, moves=["Dig"], nature=Natures.Adamant, gender=Genders.Male, ability="Vital Spirit", offset=-2)
                    if (level >= 18):
                        npcteams[name][teammate].Id = pokedexlookupname("Herdier", DexMacros.Id)
                        npcteams[name][teammate].Ability = "Intimidate"
                elif (teammate == "Carvanha"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Carvanha", level=6, moves=["Dive"], nature=Natures.Naughty, gender=Genders.Female, ability="Rough Skin", offset=-2)
                if (AimLevel() > 7):
                    npcteams[name][teammate].UpdateLevel(level, False)

        elif (name == "Skyla"):
            teammembers = ["Ducklett", "Ledyba"]
            if (level > 11):
                if (skylahasmantyke):
                    teammembers += ["Mantine", "Remoraid"]
                else:
                    teammembers += ["Emolga", "Skarmory"]               

            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Ducklett"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon(580, level=13, moves=["Water Sport", "Water Pulse", "Wing Attack"], nature=Natures.Jolly, gender=Genders.Female, ability="Big Pecks", offset=1)
                    if (level >= 17):
                        npcteams[name][teammate].Intelligence = 1
                        npcteams[name][teammate].UpdateMoves(["Aerial Ace", "Defog", "Water Pulse", "Wing Attack"])
                elif (teammate == "Ledyba"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon(165, level=13, moves=["Light Screen", "Reflect", "Comet Punch", "Supersonic"], ability="Iron Fist", gender=Genders.Male, offset=0)
                    if (level >= 18):
                        npcteams[name][teammate].Id = 166#ledian
                        npcteams[name][teammate].Intelligence = 1
                        npcteams[name][teammate].UpdateMoves(["Light Screen", "Reflect", "Comet Punch", "Mach Punch"])
                elif (teammate == "Mantine"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Mantine", level=8, moves=["Bubble Beam", "Roost", "Bullet Seed", "Psybeam"], gender=Genders.Female, nature=Natures.Jolly, ability="Swift Swim")
                    npcteams[name][teammate].Offset = -1
                    npcteams[name][teammate].Intelligence = 1
                    npcteams[name][teammate].UpdateMoves(["Wing Attack", "Psybeam", "Bubble Beam", "Bullet Seed"])
                elif (teammate == "Remoraid"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Remoraid", level=13, moves=["Psybeam", "Water Gun", "Protect", "Rain Dance"], gender=Genders.Female, nature=Natures.Serious, ability="Moody")
                    npcteams[name][teammate].Offset = -6
                    npcteams[name][teammate].Intelligence = 1
                    npcteams[name][teammate].UpdateMoves(["Aurora Beam", "Psybeam", "Water Gun", "Protect"])
                elif (teammate == "Emolga"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Emolga", level=13, moves=["Spark", "Charge", "Quick Attack", "Tail Whip"], gender=Genders.Female, nature=Natures.Jolly, ability="Static")
                    npcteams[name][teammate].Offset = -2
                    npcteams[name][teammate].Intelligence = 1
                    npcteams[name][teammate].UpdateMoves(["Nuzzle", "Spark", "Quick Attack", "Pursuit"])
                elif (teammate == "Skarmory"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Skarmory", level=13, moves=["Air Cutter", "Sand Attack", "Peck", "Metal Claw"], gender=Genders.Female, nature=Natures.Jolly, ability="Sturdy")
                    npcteams[name][teammate].Offset = -2
                    npcteams[name][teammate].Intelligence = 1
                    npcteams[name][teammate].UpdateMoves(["Metal Claw", "Air Cutter", "Sand Attack", "Leer"])
                npcteams[name][teammate].UpdateLevel(level, False)

        elif (name == "Silver"):#give him an absol eventually
            teammembers = ["Stunky", "Skorupi"]
            if (level >= 13):
                teammembers += ["Croagunk", "Grimer", "Scraggy", "Sneasel"]
            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Stunky"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Stunky", level=10, gender=Genders.Male, moves=["Poison Gas", "Acid Spray", "Screech", "Fury Swipes"], ability="Aftermath")
                    if (level >= 16):
                        npcteams[name][teammate].UpdateMoves(["Bad Breath", "Enshroud", "Screech", "Fury Swipes"])
                elif (teammate == "Skorupi"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon(451, level=10, gender=Genders.Male, moves=["Poison Sting", "Bite", "Pin Missile", "Acupressure"], ability="Sniper")
                    if (level >= 16):
                        npcteams[name][teammate].UpdateMoves(["Acupressure", "Chrysalize", "Pin Missile", "Knock Off"])
                    elif (level >= 13):
                        npcteams[name][teammate].UpdateMoves(["Acupressure", "Knock Off", "Pin Missile", "Poison Sting"])
                elif (teammate == "Sneasel"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Sneasel", level=13, moves=["Feint Attack","Leer","Quick Attack","Taunt"], nature=Natures.Quiet, gender=Genders.Male, ability="Pickpocket")
                    if (level >= 16):
                        npcteams[name][teammate].UpdateMoves(["Fury Swipes", "Icy Wind", "Feint Attack", "Quick Attack"])
                elif (teammate == "Scraggy"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Scraggy", level=13, moves=["Headbutt","Rock Smash","Feint Attack","Swagger"], nature=Natures.Brave, gender=Genders.Male, ability="Intimidate")
                    if (level >= 16):
                        npcteams[name][teammate].UpdateMoves(["Feint Attack", "Low Kick", "Disabling Poke", "Enshroud"])
                elif (teammate == "Grimer"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon(88.1, level=13, moves=["Poison Gas", "Harden", "Bite", "Disable"], nature=Natures.Bashful, gender=Genders.Female, ability="Power of Alchemy")
                    if (level >= 16):
                        npcteams[name][teammate].UpdateMoves(["Bite", "Disable", "Poison Gas", "Pound"])
                elif (teammate == "Croagunk"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Croagunk", level=13, moves=["Taunt", "Poison Sting", GetMove("Mud-Slap"), "Astonish"], nature=Natures.Impish, gender=Genders.Male, ability="Poison Touch")
                    if (level >= 16):
                        npcteams[name][teammate].UpdateMoves(["Disabling Poke", "Poison Sting", "Astonish", "Mud-Slap"])
                npcteams[name][teammate].UpdateLevel(level, False)

        elif (name == "Rosa"):
            teammembers = ["Pikachu", "Charmander", "Eevee"]
            if (level >= 15):
                teammembers += ["Dottler"]
            if (level >= 16):
                teammembers += ["Gastly"]
            if (rosahastoxel or HasEvent("Nate", "ClassSwap")):
                teammembers += ["Toxel"]

            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Pikachu"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon(25, level=18, offset=3, gender=Genders.Female, moves=["Thunder Wave", "Electro Ball", "Quick Attack", "Thunder Shock"], ability="Static")
                elif (teammate == "Dottler"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Dottler", level = AimLevel() + 2, moves=["Reflect", "Confusion", "Struggle Bug", "Light Screen"], gender=Genders.Male, nature=Natures.Relaxed, offset=2, intelligence=1)
                elif (teammate == "Eevee"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Eevee", level=5, ivs=[31, 31, 31, 31, 31, 31], ability="Adaptability")#go go overused rangers!
                    if (level >= 19):
                        npcteams[name][teammate].Id = pokedexlookupname("Jolteon", DexMacros.Id)
                        npcteams[name][teammate].Ability = "Volt Absorb"
                        npcteams[name][teammate].UpdateMoves(["Thunder Shock", "Double Kick", "Quick Attack", "Energize"])
                elif (teammate == "Charmander"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Charmander", level=5, ivs=[31, 31, 31, 31, 31, 31], ability="Blaze")#form of: a shillmon!
                elif (teammate == "Gastly"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Gastly", level=5, ivs=[31, 31, 31, 31, 31, 31])#and I'll form the head!
                elif (teammate == "Toxel"):
                    if (teammate not in npcteams[name]):
                        if (rosahastoxel):
                            npcteams[name][teammate] = Pokemon("Toxel", level = AimLevel() + 2, moves=["Growl", "Acid", "Flail", "Nuzzle"], gender=Genders.Male, nature=Natures.Rash, offset=2, intelligence=1)
                        else:
                            npcteams[name][teammate] = Pokemon("Toxel", level = AimLevel() + 2, moves=["Growl", "Acid", "Flail", "Nuzzle"], gender=Genders.Female, nature=Natures.Mild, offset=2, intelligence=1)
                            
                if (teammate not in ["Charmander", "Gastly"]):
                    npcteams[name][teammate].UpdateLevel(level, False)
    
        elif (name == "Nessa"):
            if (HasEvent("Nessa", "HasBonsly")):
                teammembers = ["Drednaw", "Corsola", "Sudowoodo", "Bruxish"]
            else:
                teammembers = ["Drednaw", "Corsola", "Bruxish"]

            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Drednaw"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Drednaw", level=22, moves=["Bite", "Headbutt", "Rock Tomb", "Protect"], gender=Genders.Female, nature=Natures.Lax, ability="Shell Armor", intelligence=1, offset=1)
                    if (level >= 17):
                        npcteams[name][teammate].UpdateMoves(["Bite", "Headbutt", "Rock Tomb", "Splinter Shield"])
                elif (teammate == "Sudowoodo"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Sudowoodo", level = AimLevel() - 1, moves=["Rock Throw", "Mimic", "Low Kick", "Wood Hammer"], offset=-1, intelligence=1, ability="Rock Head")
                elif (teammate == "Bruxish"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Bruxish", level = AimLevel() - 1, moves=["Bite", "Astonish", "Confusion", "Water Gun"], offset=-1, intelligence=1, ability="Dazzling")
                elif (teammate == "Corsola"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon(222, level=11, gender=Genders.Female, moves=["Tackle", "Harden", "Bubble Beam", "Recover"], ability="Hustle")
                    if (level >= 17):
                        npcteams[name][teammate].UpdateMoves(["Toxic", "Recover", "Healing Spring", "Splinter Shield"])
                npcteams[name][teammate].UpdateLevel(level, False)

        elif (name == "Sonia"):
            teammembers = ["Yamper", "Dedenne", "Growlithe"]
            if (level >= 20):
                teammembers += ["Electrike"]

            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Yamper"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Yamper", level=20, offset=1, moves=["Bite", "Spark", "Nuzzle", "Fire Fang"], ability="Rattled", intelligence=1)
                    if (level >= 17):
                        npcteams[name][teammate].UpdateMoves(["Bite", "Spark", "Nuzzle", "Fire Fang"])
                elif (teammate == "Dedenne"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Dedenne", level=14, moves=["Charge", "Thunder Shock"], ability="Cheek Pouch", intelligence=1)
                    if (level >= 17):
                        npcteams[name][teammate].UpdateMoves(["Thunder Shock","Charge","Charm","Parabolic Charge"])
                elif (teammate == "Growlithe"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Growlithe", level=23, moves=["Psychic Fangs", "Thunder Fang", "Fire Fang", "Bite"], ability="Intimidate", intelligence=1)
                    if (level >= 17):
                        npcteams[name][teammate].UpdateMoves(["Psychic Fangs", "Thunder Fang", "Fire Fang", "Bite"])
                elif (teammate == "Electrike"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Electrike", level = AimLevel() - 1, moves=["Thunder Fang", "Fire Fang", "Ice Fang", "Psychic Fangs"], offset=-1, intelligence=1, ability="Static")
                npcteams[name][teammate].UpdateLevel(level, False)

        elif (name == "Sabrina"):
            teammembers = ["Abra"]
            if (level >= 12):
                teammembers += ["Gastly", "Misdreavus", "Inkay"]
            if (level >= 17):
                teammembers += ["Espurr"]

            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Abra"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Abra", level=12, gender = Genders.Male, nature=Natures.Modest, moves=["Teleport", "Light Screen", "Reflect", "Hidden Power"], ability="Magic Guard", offset=1)
                    if (level >= 17):
                        npcteams[name][teammate].UpdateMoves(["Confusion", "Calm Mind", "Signal Beam", "Charge Beam"])
                    if (level >= 15):
                        npcteams[name][teammate].Id = pokedexlookupname("Kadabra", DexMacros.Id)
                elif (teammate == "Gastly"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Gastly", level=12, gender = Genders.Male, nature=Natures.Timid, moves=["Hypnosis", "Lick", "Curse", "Mean Look"], ability="Levitate")
                    if (level >= 17):
                        npcteams[name][teammate].UpdateMoves(["Mean Look","Curse","Lick","Hypnosis"])
                elif (teammate == "Misdreavus"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Misdreavus", level=12, gender = Genders.Female, nature=Natures.Lonely, moves=["Perish Song", "Astonish", "Spite", "Psywave"], ability="Levitate", offset=-1) 
                    if (level >= 17):
                        npcteams[name][teammate].UpdateMoves(["Perish Song", "Astonish", "Spite", "Psywave"])
                elif (teammate == "Inkay"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Inkay", level=12, gender = Genders.Female, nature=Natures.Adamant, moves=["Pluck", "Payback", "Hypnosis", "Wrap"], ability="Contrary", offset=-1)
                    if (level >= 17):
                        npcteams[name][teammate].UpdateMoves(["Pluck", "Payback", "Hypnosis", "Wrap"])
                elif (teammate == "Espurr"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Espurr", level = AimLevel(), moves=["Psybeam", "Light Screen", "Confusion", "Covet"], offset=0, intelligence=1, ability="Own Tempo")
                npcteams[name][teammate].UpdateLevel(level, False)

        elif (name == "Flannery"):#give her a Scovillain eventually
            teammembers = ["Numel", "Onix"]
            if (level >= 11):
                teammembers += ["Darumaka"]
            if (level >= 16):
                teammembers += ["Quilava"]
            if (HasEvent("Flannery", "HasMagby")):
                teammembers.append("Magby")

            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Numel"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Numel", level=7, offset=1, gender=Genders.Male, ability="Oblivious")
                    if (level >= 16):
                        npcteams[name][teammate].UpdateMoves(["Steady Flame", "Magnitude", "Flame Burst", "Focus Energy"])
                    if (level >= 12):
                        npcteams[name][teammate].UpdateMoves(["Focus Energy", "Ember", "Tackle", "Magnitude"])
                elif (teammate == "Darumaka"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Darumaka", level=11, moves=["Fire Fang", "Rage", "Rollout"], gender=Genders.Female, ability="Inner Focus", intelligence=1, item="Air Balloon")
                    if (level >= 16):    
                        npcteams[name][teammate].UpdateMoves(["Fire Fang","Rage","Rollout","Headbutt"])
                elif (teammate == "Onix"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Onix", level=8, gender=Genders.Female, ability="Sturdy", offset=-1)
                    if (level >= 16):
                        npcteams[name][teammate].UpdateMoves(["Stealth Rock", "Rage", "Rock Tomb", "Curse"])
                    elif (level >= 11):
                        npcteams[name][teammate].UpdateMoves(["Rock Tomb", "Rock Throw", "Curse", "Bind"])
                elif (teammate == "Quilava"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Quilava", level = AimLevel() - 1, moves=["Quick Attack", "Ember", "Smokescreen", "Tackle"], offset=-1, intelligence=1, ability="Flash Fire")
                elif (teammate == "Magby"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Magby", level = AimLevel(), moves=["Fire Spin", "Ember", "Feint Attack", "Smog"], offset=0, intelligence=1, ability="Flame Body")
                
                npcteams[name][teammate].UpdateLevel(level, False)

        elif (name == "Whitney"):
            teammembers = ["Cleffa", "Miltank"]
            if (level >= 13):
                teammembers += ["Ralts", "Audino"]            
                if (HasEvent("Whitney", "HasHappiny")):
                    teammembers += ["Chansey"]  
                else:
                    teammembers += ["Munchlax"]
                
            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Cleffa"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon(173, level=1, gender=Genders.Male, moves=["Sing", "Pound", "Copycat"], nickname="Treble", ability="Magic Guard", offset=-5)
                    if (level >= 13):
                        npcteams[name][teammate].offset = -2
                        npcteams[name][teammate].Id = 35
                        npcteams[name][teammate].UpdateMoves(["Follow Me", "Sing", "Ardent Gaze", "Defense Curl"])
                elif (teammate == "Miltank"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon(241, level=14, gender=Genders.Female, moves=["Rollout", "Defense Curl", "Stomp", "Milk Drink"], nickname="Milty", ability="Scrappy")
                elif (teammate == "Munchlax"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Munchlax", level=AimLevel() - 2, gender=Genders.Male, moves=["Tackle", "Defense Curl", "Amnesia", "Lick"], nickname="Guzzles", ability="Pickup", offset=-2, item="Sitrus Berry", intelligence=1)
                elif (teammate == "Chansey"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Chansey", level=AimLevel() - 2, gender=Genders.Female, moves=["Double Slap", GetMove("Double-Edge"), "Tail Whip", "Refresh"], nickname="Sunnyside", ability="Healer", offset=-2, intelligence=1)
                elif (teammate == "Ralts"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Ralts", level=AimLevel() - 2, gender=Genders.Female, moves=["Disarming Voice", "Confusion", "Double Team", "Lucky Chant"], nickname="Queenie", ability="Synchronize", offset=-2, intelligence=1)
                elif (teammate == "Audino"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Audino", level=AimLevel() - 2, gender=Genders.Male, moves=["Simple World", "Disarming Voice", "Hyper Voice", "Helping Hand"], nickname="Dr. Doctor", ability="Healer", offset=-2, intelligence=1)
                npcteams[name][teammate].UpdateLevel(level, False)

        elif (name == "Tia"):
            teammembers = ["Mime Jr.", "Noibat"]

            if (level >= 11):
                if (HasEvent("Tia", "HasWynaut")):
                    teammembers += ["Wobbuffet"]  
                else:
                    teammembers += ["Chimecho"]

            if (level >= 16):
                teammembers += ["Jangmo-o"]
 
            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Mime Jr."):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Mime Jr.", level=AimLevel() + 1, moves=["Barrier", "Tickle", "Copycat", "Confusion"], gender=Genders.Male, ability="Filter", offset=1)
                    if (level >= 14):
                        npcteams[name][teammate].Id = 122.1
                        npcteams[name][teammate].Ability = "Vital Spirit"
                    if (level >= 21):
                        npcteams[name][teammate].UpdateMoves(["Confusion", "Icy Wind", "Ardent Gaze", "Slow Freeze"])
                    elif (level >= 14):
                        npcteams[name][teammate].UpdateMoves(["Confusion", "Rapid Spin", "Ice Shard", "Slow Freeze"])
                elif (teammate == "Noibat"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Noibat", level=AimLevel(), moves=["Tackle", "Supersonic", "Screech", "Absorb"], gender=Genders.Male, ability="Infiltrator", intelligence=1)
                    if (level >= 21):
                        npcteams[name][teammate].UpdateMoves(["Bite", "Wing Attack", "Wing It", "Absorb"])
                    elif (level >= 16):
                        npcteams[name][teammate].UpdateMoves(["Wing Attack", "Bite", "Gust", "Absorb"])
                elif (teammate == "Jangmo-o"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Jangmo-o", level=AimLevel(), moves=["Legacy", "Bide", "Tackle", "Protect"], gender=Genders.Male, ability="Soundproof", intelligence=1)
                    if (level >= 21):
                        npcteams[name][teammate].UpdateMoves(["Legacy", "Dragon Breath", "Protect", "Dragon Tail"])
                elif (teammate == "Wobbuffet"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Wobbuffet", level=AimLevel() - 1, moves=["Counter", "Mirror Coat", "Destiny Bond", "Safeguard"], ability="Shadow Tag", offset=-1, intelligence=1)
                elif (teammate == "Chimecho"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Chimecho", level=AimLevel() - 1, moves=["Confusion", "Astonish", "Yawn", "Healing Wish"], ability="Synchronize", offset=-1, intelligence=1)
                npcteams[name][teammate].UpdateLevel(level, False)

        elif (name == "Dawn"):
            if (ninetalesobj in AllPokemon()):
                teammembers = ["Frigibax", "Vulpix", "Swinub", "Tinkatink"]  
            else:
                teammembers = ["Frigibax", "Ninetales", "Swinub", "Tinkatink"]

            if (IsAfter(23, 5, 2004)):
                teammembers.append("Cyclizar")
                
            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Frigibax"):#35->58
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Frigibax", level=AimLevel() + 1, moves=["Icy Wind", "Dragon Tail", "Dragon Breath", "Legacy"], gender=Genders.Male, ability="Thermal Exchange", intelligence=1)
                elif (teammate == "Vulpix"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon(37.1, level=AimLevel(), moves=["Powder Snow", "Ice Shard", "Icy Wind", "Ardent Gaze"], gender=Genders.Female, ability="Snow Warning", intelligence=1)
                elif (teammate == "Ninetales"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon(38.1, level=AimLevel(), moves=["Aurora Beam", "Draining Kiss", "Aurora Veil", "Charm"], gender=ninetalesobj.Gender, ability="Snow Warning", intelligence=1)
                elif (teammate == "Swinub"):#33->any level, really
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Swinub", level=AimLevel() - 1, moves=["Powder Snow", GetMove("Mud-Slap"), "Endure", "Slow Freeze"], ability="Oblivious", offset=-1, intelligence=1)
                    if (level >= 21):
                        npcteams[name][teammate].UpdateMoves(["Powder Snow", "Mud Bomb", "Slow Freeze", "Endure"])
                elif (teammate == "Tinkatink"):#24->38
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Tinkatink", level=AimLevel(), moves=["Metal Claw", "Covet", "Rock Smash", "Draining Kiss"], ability="Mold Breaker", intelligence=1)
                elif (teammate == "Cyclizar"):#temporary team member
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Cyclizar", level=AimLevel() - 2, moves=["Breaking Swipe", "Quick Attack", "Simple World", "Legacy"], gender=Genders.Female, ability="Regenerator", intelligence=1)
                npcteams[name][teammate].UpdateLevel(level, False)

        elif (name == "Wally"):
            teammembers = ["Swablu", "Budew", "Magnemite", "Skitty", "Ralts"]
                
            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Swablu"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Swablu", level=AimLevel() - 3, moves=["Disarming Voice", "Safeguard", "Fury Attack", "Sing"], offset=-3)
                elif (teammate == "Budew"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Budew", level=AimLevel() - 3, moves=["Mega Drain", "Growth", "Stun Spore"], offset=-3)
                elif (teammate == "Magnemite"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Magnemite", level=AimLevel() - 3, moves=["Light Screen", "Magnet Bomb", "Thunder Shock", "Thunder Wave"], offset=-3)
                elif (teammate == "Skitty"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Skitty", level=AimLevel() - 3, moves=["Disarming Voice", "Attract", "Sing", "Tackle"], offset=-3)
                elif (teammate == "Ralts"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Ralts", level=AimLevel(), moves=["Disarming Voice", "Magical Leaf", "Confusion", "Double Team"], gender=Genders.Male, ability="Synchronize", intelligence=1)
                npcteams[name][teammate].UpdateLevel(level, False)

        elif (name == "Grusha"):
            teammembers = ["Snom", "Cetoddle", "Swablu", "Delibird", "Archen"]# i gave him the defeatist bird. I'm so goddamn smart
            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Snom"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Snom", level=AimLevel(), moves=["Powder Snow", "Struggle Bug"], gender=Genders.Female, ability="Shield Dust", intelligence=1)
                    if (level >= 20):
                        npcteams[name][teammate].Id = 873
                        npcteams[name][teammate].UpdateMoves(["Icy Wind", "Powder Snow", "Struggle Bug", "Stun Spore"])
                elif (teammate == "Cetoddle"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Cetoddle", level=AimLevel() + 1, moves=["Ice Shard", "Rest", "Powder Snow", "Slow Freeze"], gender=Genders.Female, ability="Thick Fat", item="Chesto Berry", intelligence=1)
                elif (teammate == "Swablu"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Swablu", level=AimLevel(), moves=["Disarming Voice", "Safeguard", "Fury Attack", "Sing"], gender=Genders.Female, ability="Natural Cure", intelligence=1)
                elif (teammate == "Delibird"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Delibird", level=AimLevel() - 1, moves=["Acrobatics", "Icy Wind", "Seed Bomb", "Thief"], gender=Genders.Male, ability="Insomnia", intelligence=1)
                elif (teammate == "Archen"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Archen", level=AimLevel() - 1, moves=["Wing Attack", "Rock Throw", "Double Team", "Pluck"], intelligence=1)
                npcteams[name][teammate].UpdateLevel(level, False)
    
        elif (name == "Raihan"):#give him a tyrunt & Duraludon eventually 
            teammembers = ["Trapinch", "Cyclizar", "Roggenrola"]
            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Trapinch"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Trapinch", level=AimLevel(), moves=["Rock Slide", "Bulldoze", "Sand Tomb", "Feint Attack"], ability="Sheer Force", intelligence=1)
                elif (teammate == "Roggenrola"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Roggenrola", level=AimLevel(), moves=["Rock Blast", GetMove("Mud-Slap"), "Harden", "Headbutt"], ability="Sturdy", intelligence=1)
                elif (teammate == "Cyclizar"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Cyclizar", level=AimLevel() + 1, moves=["Breaking Swipe", "Rapid Spin"], gender=Genders.Male, ability="Shed Skin", item="Air Balloon", intelligence=1)        
                npcteams[name][teammate].UpdateLevel(level, False)

        elif (name == "Bianca"):# give her a girafarig, indeedee, and galarian ponyta at some point. girl deserves a pony
            teammembers = ["Munna", "Minccino"]

            if (level >= 15):
                teammembers.append("Solosis")
            
            if (biancahaswynaut):
                teammembers.append("Wobbuffet")

            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Munna"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Munna", moves=["Psybeam", "Defense Curl", "Moonlight", "Clear Mind"], level=AimLevel() + 1, offset = 1, nickname="Moony", gender=Genders.Female, ability="Synchronize")
                elif (teammate == "Minccino"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Minccino", moves=["Sing", "Echoed Voice", "Helping Hand", GetMove("Baby-Doll Eyes")], level=AimLevel(), offset = 0, nickname="Minnie", gender=Genders.Female, ability="Skill Link")
                elif (teammate == "Solosis"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Solosis", moves=["Psybeam", "Recover", "Charm", "Protect"], level=AimLevel(), offset = 0, nickname="Mushii", gender=Genders.Female, ability="Magic Guard")
                elif (teammate == "Wobbuffet"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Wobbuffet", level=AimLevel() - 1, moves=["Counter", "Mirror Coat", "Destiny Bond", "Safeguard"], nickname="Mobbe", ability="Shadow Tag", offset=-1, intelligence=1)
                npcteams[name][teammate].UpdateLevel(level, False)

        elif (name == "Gardenia"):#give her a Gimmighoul, Sableye, and Cofagrigus eventually
            teammembers = ["Budew", "Phantump"]
            if (level >= 19):
                teammembers += ["Grotle"]

            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Grotle"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Grotle", level=AimLevel() + 2, moves=["Curse", "Razor Leaf", "Bark Up", "Shell Smash"], offset = 2, ability="Shell Armor", intelligence=1)
                elif (teammate == "Budew"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Budew", level=7, gender=Genders.Female, ability="Poison Point", offset = 1)
                    if (level >= 19):
                        npcteams[name][teammate].Id = 315
                    if (level >= 19):
                        npcteams[name][teammate].Item = Item.SitrusBerry
                        npcteams[name][teammate].UpdateMoves(["Bad Breath", "Magical Leaf", "Mega Drain", "Leech Seed"])
                elif (teammate == "Phantump"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Phantump", level=8, gender=Genders.Male, nature="Lonely", ability="Frisk", offset=-(level - 8))#phantump should not level up for a while
                npcteams[name][teammate].UpdateLevel(level, False)

        elif (name == "Brendan"):
            teammembers = ["Shroomish", "Mudkip"]
            if (HasEvent("Brendan", "CaughtSandshrew")):
                teammembers += ["Sandshrew"]
            if (level >= 19):
                teammembers += ["Wailmer", "Grovyle"]

            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Sandshrew"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon(27, level=4, gender=Genders.Female, ability="Sand Veil")
                    if (level >= 19):
                        npcteams[name][teammate].UpdateMoves(["Bulldoze", "Rapid Spin", "Fury Cutter", "Sand Attack"])
                    elif (level >= 11):
                        npcteams[name][teammate].UpdateMoves(["Rapid Spin", "Defense Curl", "Rollout", "Poison Sting"])
                elif (teammate == "Shroomish"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon(285, level=8, nature=Natures.Docile, gender=Genders.Male, ability="Poison Heal")
                    if (level >= 19):
                        npcteams[name][teammate].UpdateMoves(["Bad Breath", "Mega Drain", "Headbutt", "Leech Seed"])
                    elif (level >= 12):
                        npcteams[name][teammate].UpdateMoves(["Mega Drain", "Leech Seed", "Stun Spore"])
                elif (teammate == "Mudkip"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon(258, level=7, nature=Natures.Hardy, gender=Genders.Male, ability="Torrent", offset=1)
                    if (level >= 15):
                        npcteams[name][teammate].Id = 259
                    if (level >= 19):
                        npcteams[name][teammate].UpdateMoves(["Mud Shot", "Rock Smash", "Rock Throw", "Water Pulse"])
                    elif (level >= 10):
                        npcteams[name][teammate].UpdateMoves([GetMove("Mud-Slap"), "Water Gun"])
                elif (teammate == "Wailmer"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Wailmer", level=AimLevel() -1, moves=["Healing Spring", "Water Pulse", "Mist", "Astonish"], offset = -1, ability="Oblivious", intelligence=1)
                elif (teammate == "Grovyle"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Grovyle", level=AimLevel() -1, moves=["Detect", GetMove("X-Scissor"), "Energy Ball", "Low Sweep"], offset = -1, ability="Unburden", item="Sitrus Berry", intelligence=1)
                npcteams[name][teammate].UpdateLevel(level, False)

        elif (name == "Hilda"):
            teammembers = ["Aron"]
            if (level >= 11):
                teammembers += ["Varoom", "Pawniard"]
            if (level >= 16):
                teammembers += ["Larvitar", "Qwilfish"]
            if (HasEvent("Hilda", "HasBonsly")):
                teammembers += ["Sudowoodo"]
            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Aron"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon(304, level=9, gender = Genders.Male, nature=Natures.Relaxed, ability="Sturdy")
                    if (level >= 15):
                        npcteams[name][teammate].UpdateMoves(["Metal Claw", "Rock Tomb", "Splinter Shield", "Mud-Slap"])
                    elif (level >= 11):
                        npcteams[name][teammate].UpdateMoves(["Metal Claw", "Headbutt", "Rock Throw", GetMove("Mud-Slap")])
                elif (teammate == "Varoom"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Varoom", level=11, offset=1, moves=["Sludge", "Assurance", "Taunt"], gender=Genders.Female, nature=Natures.Rash, ability="Overcoat")
                    if (level >= 15):
                        npcteams[name][teammate].UpdateMoves(["Bad Breath", "Gyro Ball", "Sludge", "Assurance"])
                elif (teammate == "Pawniard"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Pawniard", level=11, moves=["Fury Cutter", "Leer", "Scratch"], gender=Genders.Male, nature=Natures.Adamant, ability="Defiant")
                    if (level >= 15):
                        npcteams[name][teammate].UpdateMoves(["Metal Claw", "Fury Cutter", "Enshroud", "Leer"])
                elif (teammate == "Larvitar"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Larvitar", level=AimLevel() -1, moves=["Burial Ground", "Bite", "Rock Throw", "Sandstorm"], offset = -1, ability="Sand Veil", intelligence=1)
                elif (teammate == "Qwilfish"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Qwilfish", level=AimLevel() -1, moves=["Bubble", "Rollout", "Minimize", "Poison Sting"], offset = -1, ability="Intimidate", intelligence=1)
                elif (teammate == "Sudowoodo"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = GetTrainerTeam("Nessa", "Sudowoodo", heal)
                
                npcteams[name][teammate].UpdateLevel(level, False)

        elif (name == "Hilbert"):
            teammembers = ["Cubchoo", "Honedge", "Snorunt"]
            if (level >= 19):
                teammembers += ["Prinplup"]
            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Cubchoo"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Cubchoo", level=9, moves=["Powder Snow"], nature=Natures.Adamant, ability="Slush Rush")
                    if (level >= 19):
                        npcteams[name][teammate].Item = Item.ChoiceScarf
                elif (teammate == "Prinplup"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Prinplup", level = AimLevel(), moves = ["Bubble Beam"], nature = Natures.Mild, gender=Genders.Male, item="Choice Specs", ability="Competitive", intelligence=1)
                elif (teammate == "Honedge"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Honedge", level=9, moves=["Shadow Sneak"], nature=Natures.Quiet, ability="No Guard", offset=1)
                    if (level >= 19):
                        npcteams[name][teammate].Item = Item.ChoiceBand
                elif (teammate == "Snorunt"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Snorunt", level=9, moves=["Powder Snow"], gender=Genders.Female, nature=Natures.Rash, ability="Moody")
                    if (level >= 19):
                        npcteams[name][teammate].Item = Item.Leftovers
                        npcteams[name][teammate].UpdateMoves(["Protect", "Powder Snow", "Double Team"])
                npcteams[name][teammate].UpdateLevel(level, False)

        elif (name == "Bea"):
            teammembers = ["Clobbopus", "Rolycoly", "Machop", "Falinks"]
            if (beahastyrogue):
                teammembers.append("Tyrogue")

            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Clobbopus"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Clobbopus", level=12, gender = Genders.Male, moves=["Rock Smash", "Leer", "Bind", "Feint"], nature=Natures.Serious, ability="Technician", offset=1)
                    if (level >= 12):
                        npcteams[name][teammate].UpdateMoves(["Brick Break", "Bind", "Detect", "Dive"])
                elif (teammate == "Rolycoly"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Rolycoly", level=12, gender = Genders.Female, moves=["Tackle", "Rapid Spin", "Smack Down", "Smokescreen"], nature=Natures.Serious, ability="Flash Fire")
                    if (level >= 18):
                        npcteams[name][teammate].Id = 838
                    if (level >= 17):
                        npcteams[name][teammate].UpdateMoves(["Flame Charge", "Smack Down", "Rapid Spin", "Splinter Shield"])
                elif (teammate == "Machop"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Machop", level=12, gender = Genders.Male, moves=["Karate Chop", "Leer", "Low Kick", "Focus Energy"], nature=Natures.Serious, ability="No Guard", offset=-1)
                    if (level >= 12):
                        npcteams[name][teammate].UpdateMoves(["Knock Off", "Low Sweep", "Focus Energy", "Revenge"])
                elif (teammate == "Falinks"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Falinks", level=12, moves=["Tackle", "Protect", "Focus Energy", "Rock Smash"], nature=Natures.Serious, ability="Defiant")
                    if (level >= 12):
                        npcteams[name][teammate].UpdateMoves(["Bulk Up", "Headbutt", "Protect", "Rock Smash"])
                elif (teammate == "Tyrogue"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Tyrogue", level=6, gender = Genders.Male, moves=["Tackle", "Fake Out", "Helping Hand", "Foresight"], nature=Natures.Quirky, ability="Steadfast")
                    if (level >= 20):
                        npcteams[name][teammate].Id = 237
                        npcteams[name][teammate].Ability = "Intimidate"
                    if (level >= 20):
                        npcteams[name][teammate].UpdateMoves(["Triple Kick", "Fake Out", "Gyro Ball", "Helping Hand"])
                npcteams[name][teammate].UpdateLevel(level, False)

        elif (name == "Nate"):
            teammembers = ["Klink", "Trubbish"]
            if (level >= 11):
                teammembers += ["Magnemite"]
            if (level >= 12):
                teammembers += ["Grimer"]
            if (HasEvent("Nate", "HasToxel") and not HasEvent("Nate", "ClassSwap")):
                teammembers.append("Toxel")

            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Magnemite"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Magnemite", level=11, moves=["Thunder Wave", "Thunder Shock", "Magnet Bomb", "Supersonic"], nature=Natures.Quiet, ability="Sturdy", offset=1)
                    if (level >= 16):
                        npcteams[name][teammate].UpdateMoves(["Spark", "Thunder Wave", "Light Screen", "Magnet Bomb"])
                    elif (level >= 11):
                        npcteams[name][teammate].UpdateMoves(["Thunder Wave", "Thunder Shock", "Magnet Bomb", "Supersonic"])
                elif (teammate == "Trubbish"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon(568, level=4, gender=Genders.Female, moves=["Pound", "Poison Gas"], ability="Aftermath", offset=1)
                    if (level >= 12):
                        npcteams[name][teammate].Item = Item.SitrusBerry
                    if (level >= 16):
                        npcteams[name][teammate].UpdateMoves(["Sludge", "Recycle", "Acid Spray", "Bad Breath"])
                    elif (level >= 12):
                        npcteams[name][teammate].UpdateMoves(["Poison Gas","Recycle","Toxic Spikes","Acid Spray"])
                    elif (level >= 11):
                        npcteams[name][teammate].UpdateMoves(["Toxic Spikes", "Pound", "Poison Gas"])
                elif (teammate == "Klink"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon(599, level=3, gender=Genders.Unknown, moves=["Vise Grip"], ability="Clear Body", offset=-1)
                    if (level >= 16):
                        npcteams[name][teammate].UpdateMoves(["Gear Grind", "Thunder Shock", "Charge", "Vise Grip"])
                    elif (level >= 11):
                        npcteams[name][teammate].UpdateMoves(["Thunder Shock", "Charge", "Vise Grip"])
                elif (teammate == "Grimer"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon(88.1, level=AimLevel() - 1, moves=["Bite", "Sludge", "Bad Breath", "Enshroud"], ability="Power of Alchemy", intelligence=1, offset=-1)
                elif (teammate == "Toxel"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Toxel", level = AimLevel() + 2, moves=["Growl", "Acid", "Flail", "Nuzzle"], gender=Genders.Female, nature=Natures.Mild, offset=2, intelligence=1)
                npcteams[name][teammate].UpdateLevel(level, False)

        elif (name in ["Kris", "Professor Cherry"]): # don't forget arcee & megaree
            teammembers = ["Smoochum", "Natu", "Hitmonchan", "Cubone", "Paras", "Rotom"]
            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Smoochum"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Smoochum", level = AimLevel() - 1, nickname="Chumee", moves = ["Mean Look", "Icy Wind"], nature = Natures.Calm, gender=Genders.Male, ability="Oblivious", offset=-1, intelligence=1)
                elif (teammate == "Natu"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Natu", level = AimLevel() - 1, nickname="Natee", moves = ["Peck", "Leer", "Night Shade", "Lucky Chant"], nature = Natures.Quiet, gender=Genders.Female, offset = -1, ability="Early Bird", intelligence=1)
                elif (teammate == "Hitmonchan"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Hitmonchan", level = AimLevel() + 1, nickname="Monlee", moves = ["Mach Punch", "Bullet Punch", "Pursuit"], nature = Natures.Adamant, gender=Genders.Male, offset = -1, ability="Iron Fist", intelligence=1)
                elif (teammate == "Cubone"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Cubone", level = AimLevel(), nickname="Bonee", moves = ["Bone Club", "Headbutt", "Leer", "Focus Energy"], nature = Natures.Lonely, gender=Genders.Male, ability="Lightning Rod", item="Thick Club", intelligence=1)
                elif (teammate == "Paras"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Paras", level = AimLevel(), nickname="Parasee", moves = ["Stun Spore", "Poison Powder", "Absorb", "Fury Cutter"], nature = Natures.Brave, gender=Genders.Female, ability="Dry Skin", intelligence=1)
                elif (teammate == "Rotom"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Rotom", level = AimLevel(), nickname="Rotee", moves = ["Thunder Shock", "Thunder Wave", "Astonish", "Confuse Ray"], nature = Natures.Quirky, gender=Genders.Unknown, ability="Levitate", intelligence=1)
                elif (teammate == "Growlithe"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Growlithe", level = AimLevel(), nickname="Growlee", moves = ["Flame Wheel", "Reversal", "Bite", "Leer"], nature = Natures.Hasty, gender=Genders.Male, ability="Intimidate", intelligence=1)
                npcteams[name][teammate].UpdateLevel(level, False)

        elif (name == "Alder"):
            teammembers = ["Volcarona"]
            if (level >= 19):
                teammembers += ["Braviary", "Bouffalant"]
            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Volcarona"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Volcarona", ivs=[31, 14, 31, 31, 31, 31], evs=[0, 0, 4, 252, 252, 0], nature=Natures.Timid, gender=Genders.Female, level=85, moves=["Bug Buzz", "Quiver Dance", "Flamethrower", "Hurricane"], item="Heavy-Duty Boots", ability="Flame Body")
                    if (level >= 19):
                        npcteams[name][teammate].Level = 84
                elif (teammate == "Braviary"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Braviary", level = 82, moves = ["Crush Claw", "Superpower", "Rock Slide", "Aerial Ace"], nature = Natures.Brave, gender=Genders.Male, ability="Defiant", intelligence=1)
                elif (teammate == "Bouffalant"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Bouffalant", level = 82, moves = ["Wild Charge", "Earthquake", "Megahorn", "Head Charge"], nature = Natures.Hardy, gender=Genders.Male, ability="Sap Sipper", intelligence=1)

        elif (name == "Bruno"):
            teammembers = ["Onix", "Machamp", "Poliwrath"]
            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Onix"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Onix", level = 73, moves = ["Rock Slide", "Iron Tail", "Earthquake", "Stealth Rock"], nature = Natures.Calm, gender=Genders.Male, ability="Sturdy", intelligence=1)
                elif (teammate == "Machamp"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Machamp", level = 76, moves = ["Earthquake", "Dynamic Punch", "Rock Slide", "Bullet Punch"], nature = Natures.Adamant, gender=Genders.Male, ability="No Guard", intelligence=1)
                elif (teammate == "Poliwrath"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Poliwrath", level = 73, moves = ["Waterfall", "Superpower", "Body Slam", "Hypnosis"], nature = Natures.Quirky, gender=Genders.Female, ability="Water Absorb", intelligence=1)
                npcteams[name][teammate].UpdateLevel(level, False)

        elif (name == "Calem"):#eventually have him Simple World with Togekiss and Flying Press Spam with Hawlucha
            teammembers = ["Fletchling", "Flabébé"]
            if (level >= 11):
                teammembers += ["Falinks"]
            if (level >= 21):
                teammembers += ["Hawlucha"]
            if ("calemhastogepi" in globals() and calemhastogepi):
                teammembers.append("Togetic")#-1

            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Fletchling"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon(661, level=11, moves=["Peck", "Quick Attack", "Growl", "Tackle"], nature=Natures.Naughty, ability="Gale Wings", intelligence=1)
                    if (level >= 16):
                        npcteams[name][teammate].Id = pokedexlookupname("Fletchinder", DexMacros.Id)
                    if (level >= 16):
                        npcteams[name][teammate].UpdateMoves(["Peck", "Ember", "Wing It", "Quick Attack"])
                elif (teammate == "Flabébé"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon(669, level=8, moves=["Lucky Chant", "Fairy Wind", "Vine Whip"], nature=Natures.Naughty, ability="Flower Veil", offset=1)
                    if (level >= 21):
                        npcteams[name][teammate].UpdateMoves(["Wish", "Razor Leaf", "Ardent Gaze", "Fairy Wind"])
                elif (teammate == "Falinks"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon(870, level=11, moves=["Focus Energy", "Rock Smash", "Protect"], nature=Natures.Lonely, ability="Defiant", intelligence=1)
                    if (level >= 21):
                        npcteams[name][teammate].UpdateMoves(["Bulk Up", "Headbutt", "Disabling Poke", "Rock Tomb"])
                elif (teammate == "Hawlucha"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Hawlucha", level=AimLevel() - 1, moves=["Aerial Ace", "Roost", "Hone Claws", "Karate Chop"], ability="Unburden", item = "Oran Berry", offset=-1, intelligence=1)
                elif (teammate == "Togetic"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Togetic", level=AimLevel(), moves=["Magical Leaf", "Fairy Wind", "Ardent Gaze", "Simple World"], ability="Serene Grace", offset=-1, intelligence=1)
                npcteams[name][teammate].UpdateLevel(level, False)
        
        elif (name == "Lisia"):
            teammembers = ["Altaria"]

            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Altaria"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Altaria", level=52, moves=["Dazzling Gleam", "Dragon Pulse", "Hyper Voice", "Dragon Dance"], nickname="Ali", nature=Natures.Serious, gender=Genders.Male, item="Altarianite", ability="Natural Cure", intelligence=1)
                npcteams[name][teammate].UpdateLevel(level, False)

        elif (name == "Serena"):#...sigh. give her a zoroark, eventually...
            teammembers = ["Houndour", "Rhyhorn", "Sandile", "Braixen"]

            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Houndour"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Houndour", level=level, offset=0, gender=Genders.Male, moves=["Enshroud", "Roar", "Ember", "Bite"], nature=Natures.Impish, ability="Flash Fire", intelligence=1)
                elif (teammate == "Rhyhorn"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Rhyhorn", level=level + 1, offset=1, gender = Genders.Female, moves=["Smack Down", "Bulldoze", "Stomp", "Splinter Shield"], nature=Natures.Hardy, ability="Lightning Rod", intelligence=1)
                elif (teammate == "Sandile"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Sandile", level=level - 1, moves=["Mud-Slap", "Assurance", "Bite", "Sand Tomb"], ability="Intimidate", item = "Black Glasses", offset=-1, intelligence=1)
                elif (teammate == "Braixen"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Braixen", level=level, moves=["Steady Flame", "Psybeam", "Ember", "Flame Charge"], ability="Blaze", offset=0, intelligence=1, gender = Genders.Female)#I AM MAKING IT FEMALE SO IT'S EASIER TO REFER TO IT IN THE SCRIPT AND FOR NO OTHER REASON
                npcteams[name][teammate].UpdateLevel(level, False)

        elif (name == "Misty"):
            teammembers = ["Psyduck", "Staryu"]
            if (level >= 19):
                teammembers += ["Brionne", "Amaura"]

            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Psyduck"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon(54, level=16, offset=1, moves=["Surf", "Amnesia", "Calm Mind", "Confusion"], gender=Genders.Male, ability="Damp")
                    if (level >= 16):
                        npcteams[name][teammate].UpdateMoves(["Surf", "Amnesia", "Calm Mind", "Confusion"])
                elif (teammate == "Staryu"):
                    if (teammate not in npcteams[name]):
                        if (teammate not in npcteams[name]):
                            npcteams[name][teammate] = Pokemon(120, level=12, moves=["Water Gun", "Harden", "Rapid Spin", "Recover"], nature=Natures.Sassy, intelligence=1, ability="Analytic")
                        if (level >= 16):
                            npcteams[name][teammate].UpdateMoves(["Bubble Beam", "Swift", "Psywave", "Recover"])
                elif (teammate == "Brionne"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Brionne", level=level, moves=["Disarming Voice", "Aqua Jet", "Healing Spring", "Encore"], gender=Genders.Female, ability="Torrent", intelligence=1)
                elif (teammate == "Amaura"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Amaura", level=level, moves=["Slow Freeze", "Aurora Beam", "Rock Throw", "Thunder Wave"], ability="Refrigerate", offset=-1, intelligence=1, gender=Genders.Male)
                npcteams[name][teammate].UpdateLevel(level, False)

        elif (name == "Melody"):#give her a Masquerain, eventually. Take away the Falinks
            teammembers = ["Wimpod", "Lombre", "Finneon", "Slowpoke", "Falinks"]

            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Wimpod"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Wimpod", level=AimLevel() + 1, offset=1, moves=["First Impression", GetMove("U-turn"), "Aqua Jet", "Flip Turn"], gender=Genders.Male, foreverals=["Wimpod Foreveral"], intelligence=1)
                elif (teammate == "Lombre"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Lombre", level=AimLevel(), moves=["Fake Out", "Fury Swipes", "Bubble", "Absorb"], gender=Genders.Male, ability="Swift Swim", intelligence=1)
                #elif (teammate == "Masquerain"):
                #    if (teammate not in npcteams[name]):
                #        npcteams[name][teammate] = Pokemon("Masquerain", level=AimLevel(), moves=["Air Cutter", "Gust", "Quick Attack", "Bubble Beam"], ability = "Intimidate", intelligence=1)
                elif (teammate == "Finneon"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Finneon", level=AimLevel() - 1, offset=-1, moves=["Gust", "Rain Dance", "Attract", "Water Gun"], gender=Genders.Female, ability="Swift Swim", intelligence=1)
                elif (teammate == "Slowpoke"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Slowpoke", level=AimLevel(), moves=["Disable", "Confusion", "Water Gun", "Yawn"], gender=Genders.Male, ability = "Own Tempo", intelligence=1)#boy needs some pants
                elif (teammate == "Falinks"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Falinks", level=10, gender=Genders.Male)
                
                if (teammate != "Falinks"):
                    npcteams[name][teammate].UpdateLevel(level, False)

        elif (name == "May"):
            teammembers = ["Torchic", "Venonat"]
            if (level >= 11):
                teammembers += ["Heracross"]
                if (level >= 16):
                    if (mayhaslarvesta):
                        teammembers += ["Larvesta"]
                    else:
                        teammembers += ["Sizzlipede"]
                    teammembers += ["Cutiefly"]

            for teammate in ([specific] if specific != None else teammembers):
                if (teammate == "Heracross"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Heracross", level=9, gender=Genders.Male, moves=["Feint", "Bullet Seed", "Arm Thrust", "Endure"], nature=Natures.Calm, ability="Moxie", offset=1)
                    npcteams[name][teammate].Offset = 1
                    npcteams[name][teammate].Intelligence = 1
                    if (level >= 16):
                        npcteams[name][teammate].UpdateMoves(["Night Slash", "Counter", "Arm Thrust", "Aerial Ace"])
                    if (level >= 11):
                        npcteams[name][teammate].UpdateMoves(["Aerial Ace", "Bullet Seed", "Arm Thrust"])
                elif (teammate == "Torchic"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon(255, level=6, gender=Genders.Female, moves=["Scratch", "Growl", "Ember"], nature=Natures.Adamant, ability="Speed Boost")
                    if (level >= 16):
                        npcteams[name][teammate].Id = 256
                    if (level >= 16):
                        npcteams[name][teammate].UpdateMoves(["Double Kick", "Flamethrower", "Detect", "Peck"])
                    elif (level >= 11):
                        npcteams[name][teammate].UpdateMoves(["Sand Attack", "Ember", "Growl", "Scratch"])
                elif (teammate == "Venonat"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon(48, level=4, gender=Genders.Male, moves=["Tackle", "Disable", "Foresight", "Supersonic"], nature=Natures.Docile, ability="Compound Eyes", offset=-1)#May's Venonat
                    if (level >= 16):
                        npcteams[name][teammate].UpdateMoves(["Leech Life", "Struggle Bug", "Psybeam", "Chrysalize"])
                    elif (level >= 11):
                        npcteams[name][teammate].UpdateMoves(["Confusion", "Supersonic", "Disable"])
                elif (teammate == "Larvesta"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Larvesta", level=AimLevel(), moves=["Leech Life", "Flame Charge", "Flame Wheel", "Take Down"], gender=Genders.Male, ability = "Flame Body", intelligence=1)
                elif (teammate == "Sizzlipede"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Sizzlipede", level=AimLevel(), offset = -1, moves=["Bug Bite", "Flame Wheel", "Bite", "Steady Flame"], gender=Genders.Female, ability = "Flash Fire", intelligence=1)
                elif (teammate == "Cutiefly"):
                    if (teammate not in npcteams[name]):
                        npcteams[name][teammate] = Pokemon("Cutiefly", level=AimLevel() - 1, offset = -1, moves=["Draining Kiss", "Silver Wind", "Stun Spore", "Absorb"], gender=Genders.Male, ability = "Shield Dust", intelligence=1)

                npcteams[name][teammate].UpdateLevel(level, False)

        else:
            return None

        returnedteam = []
        if (specific == None):
            for monname in teammembers:
                if (heal):
                    npcteams[name][monname].Heal()
                returnedteam.append(npcteams[name][monname])
            for mon in returnedteam:
                mon.ShinyValue = 1#make it so enemy trainers can't get shinies
        else:
            if (specific not in npcteams[name].keys()):
                return None
            if (heal):
                npcteams[name][specific].Heal()
            returnedteam = npcteams[name][specific]
            returnedteam.ShinyValue = 1

        return returnedteam

    def GetTrainerBrain(name):
        if (name == "Jasmine"):
            if (AimLevel() >= 16):
                return jasminebrain1
        
        if (AimLevel() == "Cheren"):
            if (level >= 16):
                return cherenbrain1

        return None
