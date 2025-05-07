init -3 python:
    #general rules for deciding thresholds
    #assume a four-person party
    #Take ten, 
    # add potential morale gains * 1.5 (rounding up), 
    # add two per potential item gained
    # subtract potential morale losses 
    # subtract three if there's a requirement or damage penalty.
    # do not adjust threshold for battles unless in extenuating circumstances
    # do not adjust threshold for damage/status penalty

    DungeonEvents = {
        "DungeonEvent1" : {
            "IntroText" : "&0 comes up to a rickety rope bridge spanning a chasm. The ropes and wood that comprise it appear to be rotting, but there does not appear to be another way to pass... how should &0 proceed?",
            "Options" : {
                "Just dash across!" : {#+6 (4*1.5),
                    "Threshold": -2+ 18, 
                    "Skill": "Physicality", 
                    "SuccessMessage" : "&0 manages to dash across the bridge, the rest of the party shortly behind, though it crumbles as soon as the last party member passes over. The thrill of escaping the danger boosts the party's morale!",
                    "FailureMessage" : "&0 takes only a couple steps onto the bridge before the wood gives way. Thankfully, &* manages to grab &im and bring &im back onto the ledge, though the close encounter is not easily forgotten.",
                    "SuccessFunction" : (lambda: MotivateParty()),
                    "Rewards" : ["MP"],
                },
                "Reinforce the bridge with ropes" : {#-1
                    "Threshold": -2+ 11, 
                    "Skill": "Adaptability", 
                    "SuccessMessage" : "&0 searches the &l and is able to find some natural resources that could serve as makeshift ropes. Time passes swiftly, and by the time &e is finished, the bridge is in better shape than ever.",
                    "FailureMessage" : "&0 tries valiantly, but isn't able to find any materials that could serve as suitable ropes. Hanging &is head, &e admits defeat. &* tries not to laugh.",
                    "FailureFunction" : (lambda: DemotivateSquadder(squadleader)),
                    "Penalties": ["D"],
                },
                "Use a Pokémon to cross the chasm" : {#-4, -3 (requirement),
                    "Threshold": -2+ 8, 
                    "Skill": "Pokémon Handling",  
                    "SuccessMessage" : "Hanging tightly to &is &0m, &0 gets to the other side, then sends &is &0m back to pick up the rest of the party.",
                    "FailureMessage" : "Despite &is best efforts, &0 is not able to convince &is &0m to attempt the voyage. Further, &0's &0m's refusal has made the other Pokémon in the party skittish.",
                    "FailureFunction" : (lambda: DemotivateParty()),
                    "Penalties": ["DP"],
                    "ExcludeFunction" : ("Partner cannot learn Fly and does not have Levitate!", (lambda: not HasFlyingPokemon(squadleader)))
                }
            }
        },
        "DungeonEvent2" : {
            "IntroText" : "&0 discovers a large, sleeping, &p blocking the path. It's significantly larger than normal, tossing fretfully in its sleep, and it looks like it might make a tough fight. What should &0 do?",
            "Options" : {
                "Tiptoe around" : {#+2 (item),
                    "Threshold": -2+ 14, 
                    "Skill": "Risk-Taking",  
                    "SuccessMessage" : "&0 holds &is breath, and manages to walk around the Pokémon without disturbing it. For a moment, &e is worried, as it rolls over in its sleep... but it stays sound asleep, now that the item it was sleeping on is no longer there.",
                    "FailureMessage" : "&0 steps on a loose stone, and the sharp 'clack' wakes up the &p! It attacks in a grumpy rage!",
                    "SuccessFunction" : (lambda: DungeonItem()),
                    "Rewards" : ["I"],
                    "FailureFunction" : (lambda: DungeonFight()),
                    "Penalties": ["F"]
                },
                "Soothe the &p into a deeper sleep" : {
                    "Threshold": -2+ 12, 
                    "Skill": "Healing",
                    "SuccessMessage" : "&0 whispers to it, and gently pats it. After a while, its fretful fits subside, and it starts snoring loudly. The party moves past it, shushing each other loudly.",
                    "FailureMessage" : "&0 tries to lull the &p into a deeper sleep, but &e'd only just opened &is mouth when it awakens and attacks! &E's caught flat-footed!",
                    "FailureFunction" : (lambda: DungeonFight({
                        "AllyBoosts" : [(Stats.Speed, -1)],
                    })),
                    "Penalties": ["F"]
                },
                "Attack it!" : {
                    "BattleFunction": (lambda: DungeonFight({
                        "EnemyBoosts" : [(Stats.Attack, 1), (Stats.SpecialAttack, 1), (Stats.Speed, 1)],
                        "EnemyStatus" : [("asleep", 1)],
                        "Offset" : 3}))
                }
            }
        },
        "DungeonEvent3": {
            "IntroText": "&0 suddenly notices a piece of some item sticking out of the ground in front of &im. &* goes forward to grab it, but &0 puts a hand out in caution... What action should &0 take?",
            "RegenCriteria": (lambda x: Pokemon(x).HasType("Ground") * 2 + Pokemon(x).HasType("Bug") * 2 + Pokemon(x).HasType("Rock") - Pokemon(x).HasType("Flying")),
            "Options": {
                "Attempt to carefully extract the item": {#+2 (item)/-1
                    "Threshold": -2+ 13,
                    "Skill": "Cunning",
                    "SuccessMessage": "With quick hands, &0 is able to pull the item out of the ground without disturbing the surrounding soil.",
                    "FailureMessage": "&0 yanks on the item, but it's stuck fast in the ground. Further effort may result in damage, so &e gives up.",
                    "SuccessFunction" : (lambda: DungeonItem()),
                    "Rewards" : ["I"],
                    "FailureFunction": (lambda: DemotivateSquadder()),
                    "Penalties" : ["D"],
                },
                "Identify the item first": {
                    "Threshold": -2+ 12,
                    "Skill": "Lore Smarts",
                    "SuccessMessage": "&0's caution pays off. &e recognizes it as a buried Blast Seed, definitely not something one should be yanking out of the ground willy-nilly. The party moves on, relieved at a possible disaster averted.",
                    "FailureMessage": "&0 is unable to recognize the item from a glance. Deciding to take a closer look, &e walks closer, promptly detonating the buried Blast Seed. &0m takes the brunt of the blast, but the party is nevertheless unnerved.",
                    "FailureFunction": (lambda: squadleadermon.AdjustHealth(-squadleadermon.GetStat(Stats.Health) * 1/2.0)),
                    "Penalties" : ["Damage"]
                },
                "Toss something at it": {#+2 (1 * 1.5)/-1
                    "Threshold": -2+ 13,
                    "Skill": "Strategy",
                    "SuccessMessage": "&0 squints at the item, and tosses a small rock at it. The so-called 'item' turns out to be a mostly-buried Pokémon, which attacks angrily!",
                    "FailureMessage": "The tossed rock falls limply next to the item, making no impact whatsoever. &0 turns back in shame, but &* can't stop laughing.",
                    "SuccessFunction" : (lambda: DungeonFight()),
                    "Rewards": ["F"],
                    "FailureFunction": (lambda: [DemotivateSquadder(), MotivateSquadder(randsquad)]),
                    "Penalties" : ["D", "DR"]
                }
            }
        },
        "DungeonEvent4": {
            "IntroText": "&* starts yawning loudly, and complaining of an unnatural tiredness. &0 isn't necessarily tired, but is concerned about fatigue in the party... what should &e do?",
            "Options": {
                "Set up a camp and rest": {#+6 (4*1.5)/-4
                    "Threshold": -2+ 14,
                    "Skill": "Resilience",
                    "SuccessMessage": "&0 instructs the party to take a break and rest. Under &0's watchful gaze, the party regains their strength and feels refreshed, ready to face whatever challenges lie ahead.",
                    "FailureMessage": "&0 instructs the party to take a break and rest. However, the eerie atmosphere of their environs prevents them from truly relaxing. Exhausted, the party continues their journey, feeling worn out.",
                    "SuccessFunction" : (lambda: MotivateParty()),
                    "Rewards" : ["MP"],
                    "FailureFunction": (lambda: DemotivateParty()),
                    "Penalties" : ["DP"]
                },
                "Convince &* it's not much farther": {#-1
                    "Threshold": -2+ 11,
                    "Skill": "Persuasion",
                    "SuccessMessage": "&* seems doubtful, but takes &0's argument at face value.",
                    "FailureMessage": "&* seems unconvinced, but gets up and continues anyway, though clearly expecting to be in it for the long haul.",
                    "FailureFunction": (lambda: DemotivateSquadder()),
                    "Penalties" : ["D"],
                },
                "Motivate &* to keep going": {#+2 (1*1.5)/-4
                    "Threshold": -2+ 10,
                    "Skill": "Leadership",
                    "SuccessMessage": "&0 delivers a motivational speech, and convinces &* to go just a bit further. &* continues on with renewed morale and faith in &0.",
                    "FailureMessage": "&0 delivers a motivational speech, but it fails to land. Eventually, &* gets back on &*is feet, but a lot of time has been wasted, and now the other party members are yawning, too.",
                    "SuccessFunction" : (lambda: MotivateSquadder(randsquad)),
                    "Rewards": ["MR"],
                    "FailureFunction": (lambda: DemotivateParty()),
                    "Penalties" : ["DP"]
                }
            }
        },
        "DungeonEvent5": {
            "IntroText": "&0 stumbles upon a mysterious shrine in a shadowy corner of the &l. The shrine has a red roof and is made of painted wood that is chipped and peeling with age. What should &0 do?",
            "RegenCriteria": (lambda x: -pokedexlookup(x, DexMacros.Weight) + 20 * Pokemon(x).HasType("Flying")),
            "Options": {
                "Inspect the shrine closely": {#+6(4*1.5)/-1
                    "Threshold": -2+ 16,
                    "Skill": "Lore Smarts",
                    "SuccessMessage": "&0 carefully examines the shrine and recognizes it as a shrine built in reverence to a minor deity from the Johto region. Though unclear how it got here, the party is emboldened by the discovery!",
                    "FailureMessage": "&0 places a hand on the shrine, and a large chunk of the wood on the sidewall falls off, clearly not able to withstand anymore physical examination. &0 sheepishly puts &is hand back in his pocket.",
                    "SuccessFunction" : (lambda: MotivateParty()),
                    "Rewards" : ["MP"],
                    "FailureFunction": (lambda: DemotivateSquadder()),
                    "Penalties" : ["D"]
                },
                "Offer a tribute to the shrine": {#+2
                    "Threshold": -2+ 14,
                    "Skill": "Pokémon Handling",
                    "SuccessMessage": "&0 attempts to place a valuable item within the shrine, only to discover a &p living inside. It inspects &0 curiously, then takes the proffered item and gives &0 something it pulls out of its nest. 'Business' done, it closes the door and goes back to sleep.",
                    "FailureMessage": "&0 attempts to place a valuable item within the shrine, only to discover a &p living inside. It does not appreciate having its sleep disturbed, and attacks!",
                    "SuccessFunction" : (lambda: DungeonItem()),
                    "Rewards" : ["I"],
                    "FailureFunction": (lambda: DungeonFight()),
                    "Penalties" : ["F"]
                },
                "Knock over the shrine": {#+4(2*2)/-7
                    "Threshold": -2+ 9,
                    "Skill": "Risk-Taking",
                    "SuccessMessage": "&0 kicks over the shrine, easily shattering the old wood. It makes a sad 'sighing' sound as it breaks. A couple small items fall out--tributes from some unseen worshipper, perhaps. &0 gathers the items, but the rest of the party is horrified.",
                    "FailureMessage": "&0's weak kick makes no impact. The rest of the party is filled with equal parts scorn and pity as &0 slinks away in embarrassment.",
                    "SuccessFunction" : (lambda: [DungeonItem(2), DemotivateParty(exclude=[squadleader])]),
                    "Rewards" : ["I2", "DPXL"],
                    "FailureFunction": (lambda: DemotivateParty()),
                    "Penalties" : ["DP"]
                }
            }
        },
        "DungeonEvent7": {
            "IntroText": "&0 hears a faint, eerie melody echoing through the &l. It's haunting and melancholic, seeming to come from nowhere and everywhere at once. What should &0 do?",
            "RegenCriteria": (lambda x: WildMonCanVocalize(x)),
            "Options": {
                "Quietly listen to the melody": {#+12(4 * 2 * 1.5),
                    "Threshold": -2+ 24,
                    "Skill": "Healing",
                    "SuccessMessage": "Perhaps its source is not important. The eerie tune eventually turns into a more joyful one, as though its source was aware it had an audience, and was performing for them. Time passes as the party takes in the music, allowing it to refresh and reinvigorate them... and then it is gone.",
                    "FailureMessage": "&0 simply cannot contain &is urge to progress, and, eventually, &e moves to continue. The melody abruptly ends, leaving only a sad echo of a performance cut short. The party moves on.",
                    "SuccessFunction" : (lambda: MotivateParty(2)),
                    "Rewards": ["MP2"]
                },
                "Harmonize with the melody": {#+5(3 * 1.5),
                    "Threshold": -2+ 17,
                    "Skill": "Learning",
                    "SuccessMessage": "&0 listens intently to the melody, then joins in. The source cuts out, but &0 is able to carry the melody alone for a few bars, before it joins back in. &0 and the mysterious source work their way to the song's crescendo, then it ceases. Taking a bow, &0 basks in the party's applause.",
                    "FailureMessage": "&0 listens intently to the melody, then joins in. The source cuts out, and &0 is not able to remember how the melody continues, so is not able to carry it alone. Eventually, &e gives up, and the party moves on.",
                    "SuccessFunction" : (lambda: MotivateSquadder(squadleader, 3)),
                    "Rewards": ["M3"]
                },
                "Identify the source": {#+2(1*1.5),
                    "Threshold": -2+ 14,
                    "Skill": "Pokémon Smarts",
                    "SuccessMessage": "&0 is able to recognize the source as the cry of a &p. Pushing towards it, &0 comes across, as predicted, a &p quietly singing. It walks towards &0 and headbutts &is leg, before promptly fleeing off, leaving nothing but a pleasant memory.",
                    "FailureMessage": "&0 fails to recognize the source of the melody until &e stumbles across a wild &p singing. Offended that its performance had been disrupted, it attacks!",
                    "SuccessFunction" : (lambda: MotivateSquadder()),
                    "Rewards" : ["M"],
                    "FailureFunction": (lambda: DungeonFight()),
                    "Penalties": ["F"]
                }
            }
        },
        "DungeonEvent8": {
            "IntroText": "&0 encounters a series of ancient runes carved into a large, flat, stone sitting in the middle of an open area. They glow faintly with an otherworldly light, emanating an aura of power. What should &0 do?",
            "RegenCriteria": (lambda x: Pokemon(x).HasType("Psychic") + Pokemon(x).HasType("Ghost")),
            "Options": {
                "Study the runes closely": {#+4/-1
                    "Threshold": -2+ 15,
                    "Skill": "Lore Smarts",
                    "SuccessMessage": "&0 carefully examines the runes, deciphering their meaning and history. They seem Sinnohan in origin, strongly resembling runes that one might find in the walls of the ancient Celestic Town, and such runes were commonly considered to keep the viewer safe from disruptions to their time and space. Quietly regarding the runes, the Mysteriosity seems to thin.",
                    "FailureMessage": "&0 struggles to make sense of the intricate symbols, feeling a headache coming on from the effort. Frustrated, the party decides to move on, leaving the mysterious runes behind.",
                    "SuccessFunction" : (lambda: MotivateParty()),
                    "Rewards" : ["MP"],
                    "FailureFunction": (lambda: DemotivateSquadder()),
                    "Penalties" : ["D"],
                },
                "Activate the runes": {#+2
                    "Threshold": -2+ 14,
                    "Skill": "Risk-Taking",
                    "SuccessMessage": "&0 bravely reaches out to touch the glowing runes, attempting to trigger some form of reaction. The rune resounds with a crack, and as the rock shatters, an item drops from its rocky cocoon.",
                    "FailureMessage": "&0 bravely reaches out to touch the glowing runes, attempting to trigger some form of reaction. The rune resounds with a crack, and as the rock shatters, there's a flash of light and a &p appears, confused and dazed. In its confusion, it attacks!",
                    "SuccessFunction" : (lambda: DungeonItem()),
                    "Rewards" : ["I"],
                    "FailureFunction": (lambda: DungeonFight({"EnemyStatus" : [("confused", 3)]})),
                    "Penalties" : ["F"],
                },
                "Bypass the runes cautiously": {
                    "Threshold": -2+ 11,
                    "Skill": "Adaptability",
                    "SuccessMessage": "&0 carefully navigates around the glowing runes, avoiding any potential risks they might pose. The party proceeds cautiously but without incident.",
                    "FailureMessage": "&0 misjudges the distance and accidentally brushes against one of the runes. A jolt of magical energy courses through &im, leaving &0 momentarily stunned and vulnerable.",
                    "FailureFunction": (lambda: DemotivateSquadder()),
                    "Penalties" : ["D"],
                }
            }
        },
        "DungeonEvent9": {
            "IntroText": "&0 stumbles across a Kecleon sitting on a mat. The Kecleon has its eyes closed and legs crossed, with some small items lying next to it. It cracks an eye open as &0 approaches, appraising &im cautiously.",
            "Options": {
                "Pay one Gimmighoul Coin for an item": {
                    "SuccessMessage": "The Kecleon acknowledges &0's payment, and hands &im a small bundle before sweeping its rug up and scampering off.",
                    "ExcludeFunction": ("No Gimmighoul Coins!", (lambda: gimmighoulcount < 1)),
                    "SuccessFunction" : (lambda: DungeonItem(exclude=["Gimmighoul Coin"])),
                    "Rewards": ["1x Non-Gimmighoul Coin Item"]
                },
                "Sell an item for Gimmighoul Coins": {
                    "SuccessMessage": "The Kecleon acknowledges &0's offer, and hands &im a small bundle of coins before sweeping its rug up and scampering off.",
                    "SuccessFunction" : (lambda: DungeonItem(numitems=3, mandate=["Gimmighoul Coin"])),
                    "Rewards": ["3x Gimmighoul Coins"]
                },
                "Attempt to steal from the Kecleon...?": {
                    "Threshold": -2+ 28,#special, because Kecleon is bullshit.
                    "Skill": "Cunning",
                    "SuccessMessage": "&0 manages to misdirect the Kecleon, and snatch an item off the rug without it noticing. The party quickly leaves before their theft is discovered.",
                    "FailureMessage": "&0's clumsy attempt to steal is spotted immediately. The Kecleon attacks in a frenzied rage!",
                    "SuccessFunction" : (lambda: DungeonItem()),
                    "Rewards" : ["I"],
                    "FailureFunction": (lambda: DungeonFight({
                        "EnemyBoosts" : [(Stats.Attack, 2), (Stats.SpecialAttack, 2), (Stats.Speed, 2), (Stats.Defense, 2), (Stats.SpecialDefense, 2), (Stats.Evasion, 2), (Stats.Accuracy, 2)],
                        "EnemyStatus" : [("Frenzied", 1)]},
                        assignmon = Pokemon("Kecleon", level=90, moves=["Camouflage", "Double-Edge", "Knock Off", "Drain Punch"], frenzynerf=(20, ["Lick", "Quick Attack", "Fury Swipes", "Camouflage"]), shinylock=False))),
                    "Penalties" : ["Annihilation"]
                }
            }
        },
        "DungeonEvent10": {
            "IntroText": "&0 suddenly spots a cloud of dust in the distance! It looks like an angry &p is charging straight towards &im! What should &0 do?",
            "Options": {
                "Wait until it's right upon &im before battling!": {#+4
                    "Threshold": -2+ 16,
                    "Skill": "Resilience",
                    "SuccessMessage": "&0 waits for the &p to be within striking distance, then unflinchingly throws out &is Poké Ball, catching it off-guard! The party is inspired by the show of bravery!",
                    "FailureMessage": "&0 attempts to wait for the &p to be within striking distance, but chickens out at the last second. The &p continues its charge!",
                    "SuccessFunction" : (lambda: [MotivateParty(), DungeonFight()]),
                    "Rewards": ["MP", "F"],
                    "FailureFunction": (lambda: DungeonFight({ "EnemyBoosts" : [(Stats.Speed, 2)] })),
                    "Penalties": ["F"]
                },
                "Send out &is Pokémon immediately!": {
                    "BattleFunction": (lambda: DungeonFight())
                },
                "Lure the &p into a disadvantageous position!": {
                    "Threshold": -2+ 12,
                    "Skill": "Strategy",
                    "SuccessMessage": "&0 recognizes the &p is charging wildly, and manages to trick it into running against a wide, flat, surface. While it's dazed and confused, &e strikes!",
                    "FailureMessage": "&0 tries to trick the &p into running into a wide, flat surface, but it veers left and continues its charge!",
                    "SuccessFunction" : (lambda: DungeonFight({"EnemyStatus" : [("confused", 2)]})),
                    "Rewards": ["F"],
                    "FailureFunction": (lambda: (lambda: DungeonFight({ "EnemyBoosts" : [(Stats.Speed, 2)] }))),
                    "Penalties": ["F"],
                }
            }
        },
        "DungeonEvent11": {
            "IntroText": "A large rock suddenly crashes down and starts rolling toward the party! They'll be squished if they don't move quickly. What should &0 do?",
            "Options": {
                "Send out a Pokémon to block it!": {#+6 (1.5 * 4),
                    "Threshold": -2+ 18,
                    "Skill": "Leadership",
                    "SuccessMessage": "&0 sends out &0m, which braces itself and shatters the rock before it could crush its trainer! Everyone is very relieved that no-one got hurt.",
                    "FailureMessage": "&0 sends out &0m, which is too terrified to do anything as the massive boulder slams into it, causing massive damage! &0 mutters a sheepish apology as the party carries on, more banged-up and bruised than before.",
                    "SuccessFunction" : (lambda: MotivateParty()),
                    "Rewards" : ["MP"],
                    "FailureFunction": (lambda: squadleadermon.AdjustHealth(-squadleadermon.GetStat(Stats.Health) * 1/2.0)),
                    "Penalties": ["Damage"]
                },
                "Send out a Pokémon to break it!": {#+6 (1.5 * 4) /-3 (requirement),
                    "Threshold": -2+ 15,
                    "Skill": "Adaptability",
                    "SuccessMessage": "&0 sends out &0m, which delivers a mighty blow, shattering the rock into pieces! The party is hugely relieved, and moves on.",
                    "FailureMessage": "&0 sends out &0m, but it doesn't have enough time to react before the boulder slams into it, causing massive damage! &0 mutters a sheepish apology as the party carries on, more banged-up and bruised than before.",
                    "ExcludeFunction": ("Partner cannot learn Rock Smash!", (lambda: not HasRockBreaker())),
                    "SuccessFunction" : (lambda: MotivateParty()),
                    "Rewards" : ["MP"],
                    "FailureFunction": (lambda: squadleadermon.AdjustHealth(-squadleadermon.GetStat(Stats.Health) * 1/2.0)),
                    "Penalties": ["Damage"]
                },
                "Vault over the rock!": {#+2(1*1.5)/-1
                    "Threshold": -2+ 13,
                    "Skill": "Physicality",
                    "SuccessMessage": "&0 crouches and leaps over the boulder in a single fluid motion! Luckily, the rest of the party managed to get out of the way, too. The party continues, unscathed, as &0 brags about &is near escape.",
                    "FailureMessage": "&0 tries to leap over the rock, but &is foot gets caught and &e slams face-first into it. Luckily, besides &is battered pride and bruised nose, &e is unhurt.",
                    "SuccessFunction" : (lambda: MotivateSquadder()),
                    "Rewards" : ["M"],
                    "FailureFunction": (lambda: DemotivateSquadder()),
                    "Penalties" : ["D"],
                }
            }
        },
        "DungeonEvent12": {
            "IntroText": "The party suddenly comes across a large treasure chest sitting in a conspicuous opening! &* moves towards it, eager to open it. What should &0 do?",
            "Options": {
                "Attempt to pick the lock": {#+6 (3 * 2)/-1
                    "Threshold": -2+ 17,
                    "Skill": "Cunning",
                    "SuccessMessage": "&0 manages to use some makeshift tools--a paperclip, a twig, and the edge of &is credit card--to work open the chest's lock. It pops open without incident, and the party greedily gathers the goods inside.",
                    "FailureMessage": "Lacking the proper tools, or the time to devote to &is lock-picking effort, the chest remains undeflowered, refusing to yield its precious goods. &0 kicks it and walks away grumpily.",
                    "SuccessFunction" : (lambda: DungeonItem(3)),
                    "Rewards" : ["I3"],
                    "FailureFunction": (lambda: DemotivateSquadder()),
                    "Penalties" : ["D"],
                },
                "Take the chest with &im": {#+6 (3*2) /-4
                    "Threshold": -2+ 14,
                    "Skill": "Resilience",
                    "SuccessMessage": "&0 simply pulls the chest out of the ground and throws it over &is shoulder. It's extremely heavy, and carrying it slows &im down greatly, but once &e gets back to safety, &e can take the items within!",
                    "FailureMessage": "&0 attempts to lift the chest up, and manages to pull it a couple feet, but soon realizes that carrying this thing through the rest of the dungeon simply isn't tenable. &E gives up with a sigh.",
                    "SuccessFunction" : (lambda: [DungeonItem(3), DemotivateSquadder(change=-3)]),
                    "Rewards" : ["I3", "D3"],
                    "FailureFunction": (lambda: DemotivateSquadder()),
                    "Penalties" : ["D"],
                },
                "Send out a Pokémon to bust the chest": {#+2/-1
                    "Threshold": -2+ 13,
                    "Skill": "Pokémon Smarts",
                    "SuccessMessage": "&0 sends out &0m, which easily smashes the wooden chest. Though it appears some of the items in the chest were destroyed, there is one that is still in perfect condition.",
                    "FailureMessage": "&0 sends out &0m, which easily smashes the wooden chest. Too easily, in fact--the chest, and everything inside, is completely destroyed. &0m is embarrassed as &0 hangs &is head and sighs.",
                    "ExcludeFunction": ("Partner cannot learn Rock Smash!", (lambda: not HasRockBreaker())),
                    "SuccessFunction" : (lambda: DungeonItem()),
                    "Rewards" : ["I"],
                    "FailureFunction": (lambda: DemotivateSquadder()),
                    "Penalties" : ["D"],
                }
            }
        },
        "DungeonEvent13": {
            "IntroText": "&*'s stomach suddenly starts rumbling loudly. Perhaps now would be a good time to rest and gather some food. The party looks to &0 for direction--what should &e do?",
            "Options": {
                "Share prepared food": {#+6 (4*1.5) /-1
                    "Threshold": -2+ 17,
                    "Skill": "Strategy",
                    "SuccessMessage": "Planning ahead, &0 had brought plenty of food for the trip, and easily shares it with &is companions. The party continues on, refreshed.",
                    "FailureMessage": "&0 looks in &is pack for food &e knows isn't there, as &e guiltily recalls the lack of planning that went into this delve. &E shrugs in a 'oh well, guess there's nothing we can do about it' gesture, which does little to raise morale.",
                    "SuccessFunction" : (lambda: MotivateParty()),
                    "Rewards" : ["MP"],
                    "FailureFunction": (lambda: DemotivateSquadder(randsquad)),
                    "Penalties" : ["DR"],
                },
                "Find food in the dungeon": {#+3 (2*1.5)/-1
                    "Threshold": -2+ 14,
                    "Skill": "World Smarts",
                    "SuccessMessage": "&0 searches for something edible from the natural resources around &im, and comes across a handful of human-edible berries, which &e shares with &*. The duo are refreshed!",
                    "FailureMessage": "&0 searches for something edible from the natural resources around &im, and comes across a handful of berries. &* takes a cautious bite, but immediately spits them out--they're far too sour, and not edible. The party continues in spite of &*'s protests.",
                    "SuccessFunction" : (lambda: [MotivateSquadder(squadleader), MotivateSquadder(randsquad)]),
                    "Rewards" : ["M", "MR"],
                    "FailureFunction": (lambda: DemotivateSquadder(randsquad)),
                    "Penalties" : ["DR"],
                },
                "Insist the party continue onwards": {#-4
                    "Threshold": -2+ 8,
                    "Skill": "Persuasion",
                    "SuccessMessage": "&0 rallies the party and convinces them to ignore their rumbling bellies... at least for now. Though &* continues to grumble, &*e continues along the path.",
                    "FailureMessage": "&0 attempts to convince the party to ignore their rumbling bellies... but is met with little success. &* continues to grumble, and &*is discontent spreads to the rest of the party.",
                    "SuccessFunction" : (lambda: DemotivateSquadder(randsquad)),
                    "Rewards" : ["DR"],
                    "FailureFunction": (lambda: DemotivateParty(exclude=[squadleader])),
                    "Penalties": ["DPXL"]
                }
            }
        },
        "DungeonEvent14": {
            "IntroText": "A wild &p appears, out of the darkness of the &l, and it appears to be on the prowl for a fight. Its eyes are red with anger. What should &0 do?",
            "Options": {
                "Just observe it": {#+2 (item),
                    "Threshold": -2+ 14,
                    "Skill": "Learning",
                    "SuccessMessage": "&0 patiently watches it, and the cause of its anger soon becomes clear--two more &p appear, and they appear to be intentionally keeping an item away from the first &p! After tormenting it for a while, the three of them run off, leaving the item behind.",
                    "FailureMessage": "&0 attempts to stay quiet and catalog its behavior, but makes too much noise, and alerts the &p to &is presence. It attacks in a rage!",
                    "SuccessFunction" : (lambda: DungeonItem()),
                    "Rewards" : ["I"],
                    "FailureFunction": (lambda: DungeonFight({"EnemyBoosts": [(Stats.Attack, 1), (Stats.SpecialAttack, 1)], "Offset": 3})),
                    "Penalties" : ["F"]
                },
                "Lead it away": {
                    "Threshold": -2+ 12,
                    "Skill": "Deception",
                    "SuccessMessage": "&0 tosses a stick in an opposite direction, while masking &is own presence. The wild &p takes note of it, and darts in the opposite direction of the party, which breathes a sigh of relief.",
                    "FailureMessage": "&0 tosses a stick in an opposite direction, while trying to mask &is own presence. The &p immediately notices, though, and leaps to attack!",
                    "FailureFunction": (lambda: DungeonFight({"EnemyBoosts": [(Stats.Attack, 1), (Stats.SpecialAttack, 1)], "Offset": 3})),
                    "Penalties" : ["F"],
                    "ExcludeFunction" : ("[first_name] cannot deceive!", (lambda: squadleader.Type == TrainerType.Player))
                },
                "Bring the fight to it!": {
                    "BattleFunction": (lambda: DungeonFight({"EnemyBoosts": [(Stats.Attack, 1), (Stats.SpecialAttack, 1)], "Offset": 3}))
                }
            }
        },
        "DungeonEvent15": {
            "IntroText": "The party suddenly realizes they are quite lost--even for a Mystery Dungeon. A sense of nervousness settles on the party as they attempt to reorient themselves. What should &0 do?",
            "Options": {
                "Use the position of the sun": {#+6 (4 * 1.5)/-4
                    "Threshold": -2+ 14,
                    "Skill": "World Smarts",
                    "SuccessMessage": "&0 recalls something &e read once about the position of the sun, and how it relates to the cardinal directions. Trusting vague memories, &0 is able to lead the party back onto the path, much to their relief.",
                    "FailureMessage": "&0 tries to recall something &e read once about the position of the sun, and how it relates to the cardinal directions. Trusting vague memories, &0 succeeds in nothing but getting the party even further lost.",
                    "ExcludeFunction": (lambda: IsNight()),
                    "SuccessFunction" : (lambda: MotivateParty()),
                    "Rewards" : ["MP"],
                    "FailureFunction": (lambda: DemotivateParty()),
                    "Penalties" : ["DP"],
                },
                "Use the position of the stars": {#+6 (4 * 1.5)/-4
                    "Threshold": -2+ 14,
                    "Skill": "World Smarts",
                    "SuccessMessage": "&0 recalls something &e read once about the position of the stars, and how it relates to the cardinal directions. Trusting vague memories, &0 is able to lead the party back onto the path, much to their relief.",
                    "FailureMessage": "&0 tries to recall something &e read once about the position of the stars, and how it relates to the cardinal directions. Trusting vague memories, &0 succeeds in nothing but getting the party even further lost.",
                    "ExcludeFunction": (lambda: not IsNight()),
                    "SuccessFunction" : (lambda: MotivateParty()),
                    "Rewards" : ["MP"],
                    "FailureFunction": (lambda: DemotivateParty()),
                    "Penalties" : ["DP"],
                },
                "Use a Pokémon to scout it out" : {#+5 (3 * 1.5)/-3 (requirement),
                    "Threshold": -2+ 14, 
                    "Skill": "Pokémon Handling",  
                    "SuccessMessage" : "&0 sends &0m as high as it can go, and it reports back, pointing the party in the right direction. After a round of praise for &0m, the party moves on.",
                    "FailureMessage" : "&0 sends &0m as high as it can go. However, &0 is unable to interpret its report when it comes back, and the party wanders off in a random direction, just as confused as before.",
                    "SuccessFunction" : (lambda: MotivateParty()),
                    "Rewards" : ["M3"],
                    "ExcludeFunction" : ("Partner cannot learn Fly and does not have Levitate!", (lambda: not HasFlyingPokemon(squadleader)))
                },
                "Retrace &is steps": {#+2 (1 * 1.5)/-4
                    "Threshold": -2+ 10,
                    "Skill": "Leadership",
                    "SuccessMessage": "&0 leads the party back the way they came, eventually finding a part of the path everyone recognizes. Patting &im on the back, the party continues with renewed faith in &0 and their direction.",
                    "FailureMessage": "&0 attempts to lead the party back the way they came, but is unable to find a part of the path that everyone recognizes, succeeding in nothing but sowing discontent as everyone points in a different direction.",
                    "SuccessFunction" : (lambda: MotivateSquadder()),
                    "Rewards" : ["M"],
                    "FailureFunction": (lambda: DemotivateParty()),
                    "Penalties" : ["DP"],
                }
            }
        },
        "DungeonEvent16": {
            "IntroText": "&0 steps awkwardly on a rock, and &is ankle twists painfully. The party's progress could be very much hindered if &e is forced to walk on it as-is. What should &0 do?",
            "Options": {
                "Craft a rudimentary splint": {#+5 (3 * 1.5)/-3
                    "Threshold": -2+ 14,
                    "Skill": "Healing",
                    "SuccessMessage": "&0 manages to use items in &is pack, and natural resources, to bind &is foot in a way that takes much of the pressure off of it. After a couple minutes of walking on the splint, it becomes clear the ankle is not sprained, and &0 is able to progress with a new spring in &is step.",
                    "FailureMessage": "&0 tries to use the items in &is pack to craft a rudimentary splint, but it falls apart in &is hands. Grimacing through the agony, &e trudges along, regardless of the growing, sharp, pain.",
                    "SuccessFunction" : (lambda: MotivateSquadder(change=3)),
                    "Rewards" : ["M3"],
                    "FailureFunction": (lambda: DemotivateSquadder(change=-3)),
                    "Penalties" : ["D3"],
                },
                "Power through": {#+5 (3* 1.5)/-6
                    "Threshold": -2+ 11,
                    "Skill": "Resilience",
                    "SuccessMessage": "&0 grimaces and bears it, defying all conventional wisdom. Despite the awkward angle &is foot is at, &0 progresses along, earning the admiration of the rest of the party, even as the injury gnaws at &im inside.",
                    "FailureMessage": "&0 attempts to grimace and bear it, but can only make it a few steps before collapsing. The party spends a lot of time waiting around for &is pain to subside before continuing, lowering morale.",
                    "SuccessFunction" : (lambda: [MotivateParty(exclude=[squadleader]), DemotivateSquadder(-2)]),
                    "Rewards": ["MPXL", "D2"],
                    "FailureFunction": (lambda: DemotivateParty()),
                    "Penalties" : ["DP"],
                },
                "Convince a Pokémon to carry &im" : {#+2(1*1.5)/-1/-3 (requirement),
                    "Threshold": -2+ 10, 
                    "Skill": "Persuasion",  
                    "SuccessMessage" : "They say delegation is the key to any successful enterprise. &0's &0m is more than capable of transporting &im the distance until &is foot feels good enough to put weight on again. The quick trip break &im refreshed and ready to face the dungeon anew!",
                    "FailureMessage" : "&0 sends out &0m, but it's too jittery and nervous, due to the Mystery Dungeon. It briefly picks up &0, but then just as quickly drops &im. &0 resigns &imself to just powering through.",
                    "SuccessFunction" : (lambda: MotivateSquadder()),
                    "Rewards" : ["M"],
                    "FailureFunction": (lambda: DemotivateSquadder()),
                    "Penalties" : ["D"],
                    "ExcludeFunction" : ("Partner cannot learn Strength or Rock Climb!", (lambda: not HasStrongPokemon(squadleader) and not HasRockClimbingPokemon(squadleader)))
                }
            }
        },
        "DungeonEvent16": {
            "IntroText": "&0 walks around a corner and finds the party's progress blocked by a looming, great, wall of stone. Ivy criss-crosses its surface, but it's unclear if it's strong enough to support a person. It stretches off into the distance on both sides... what should &0 do?",
            "Options": {
                "Attempt to create indentations in the rock": {#+6 (3 * 2)/-2
                    "Threshold": -2+ 16,
                    "Skill": "Learning",
                    "SuccessMessage": "Using a combination of tools, Pokémon, and natural resources, &0 bangs away at the rock face, quickly realizing that the wall is hollow. Smacking away at it, once more, the rock crumbles to reveal an empty cavern with a pile of trinkets. The party swipes the valuable items and proceeds through the cavern, coming out on the other side.",
                    "FailureMessage": "&0 attempts to break through the rock face, but succeeds only in slamming a hammer on &is thumb. &E hops around, spewing profanities, before eventually insisting the party takes the long way around.",
                    "SuccessFunction" : (lambda: DungeonItem(3)),
                    "Rewards" : ["I3"],
                    "FailureFunction": (lambda: DemotivateSquadder(-2)),
                    "Penalties": ["D2"]
                },
                "Search for indentations under the ivy": {#+6 (4 * 1.5)/-4
                    "Threshold": -2+ 14,
                    "Skill": "Cunning",
                    "SuccessMessage": "Ignoring the ivy, which would likely tear under mild pressure, &0 is able to identify a path to the top of the wall that utilizes natural footholds. The party ascends, exhilarated.",
                    "FailureMessage": "&0 tears off the ivy from the wall, deeming it just a distraction. Unfortunately, now that the wall is exposed, it is clear that there are no natural footholds, and the ivy, which was the party's best bet is in no state to carry anyone anymore. &0 sighs, as the party resolves to go the long way around.",
                    "SuccessFunction" : (lambda: MotivateParty()),
                    "Rewards" : ["MP"],
                    "FailureFunction": (lambda: DemotivateParty()),
                    "Penalties" : ["DP"],
                },
                "Use a Pokémon to scale the wall." : {#+6(4*1.5)/-4/-3 (requirement),
                    "Threshold": -2+ 11, 
                    "Skill": "Pokémon Smarts",  
                    "SuccessMessage" : "&0 sends out &0m, which uses its natural strength to scale the wall, pulling &0 up after it. It then goes back down and picks up the rest of the party. An easy ride, if not necessarily a comfortable one.",
                    "FailureMessage" : "&0 sends out &0m, but cannot convince it to climb the wall. It stares up dubiously, clearly doubting its own abilities, before retreating into its Poké Ball. &0 sighs, as the party resolves to go the long way around.",
                    "SuccessFunction" : (lambda: MotivateParty()),
                    "Rewards" : ["MP"],
                    "FailureFunction": (lambda: DemotivateParty()),
                    "Penalties" : ["DP"],
                    "ExcludeFunction" : ("Partner cannot learn Rock Climb!", (lambda: not HasRockClimbingPokemon(squadleader)))
                }
            }
        },
        "DungeonEvent17": {
            "IntroText": "A swarm of Gimmighoul appear before the party! They appear to be fighting over Gimmighoul coins, those strange flat discs that they seem to crave so much. The shortest path to the party's destination goes straight through their brawl... what should &0 do?",
            "Options": {
                "Mislead the Gimmighoul and swipe their coins": {#+6 (3 * 2),
                    "Threshold": -2+ 18,
                    "Skill": "Deception",
                    "SuccessMessage": "Dramatically tossing an item of little value off in another direction, &0 manages to swipe the precious Gimmighoul coins before they realize they'd been had. Even now, the evil seed of what you've done germinates within you.",
                    "FailureMessage": "Dramatically tossing an item of little value off in another direction, &0 succeeds in nothing but making &* laugh slightly at &is pitiful attempt at distraction. The party moves on.",
                    "SuccessFunction" : (lambda: DungeonItem(3, mandate=["Gimmighoul Coin"])),
                    "Rewards": ["3x Gimmighoul Coins"],
                    "ExcludeFunction" : ("[first_name] cannot deceive!", (lambda: squadleader.Type == TrainerType.Player))
                },
                "Support one of the Gimmighoul": {#+2
                    "Threshold": -2+ 14,
                    "Skill": "Healing",
                    "SuccessMessage": "Giving one particular Gimmighoul a healing berry is enough to turn the tide of the melee. It defeats its foes, gathers up the Gimmighoul coins, and gives one to &0 before quickly running away with the rest of the loot.",
                    "FailureMessage": "&0 attempts to give a particular Gimmighoul a healing berry, but in the fracas, it's hard to tell them apart, and it's unclear what benefit, if any, &0's actions had.",
                    "SuccessFunction" : (lambda: DungeonItem(1, mandate=["Gimmighoul Coin"])),
                    "Rewards": ["1x Gimmighoul Coin"]
                },
                "Try to convince the Gimmighoul to share" : {#+4(2*2)/-4
                    "Threshold": -2+ 12, 
                    "Skill": "Strategy",  
                    "SuccessMessage" : "Though the notion of a shared market system is a bit beyond the Gimmighoul's understanding, they quiet down and listen, eventually taking one coin each from the pile and absconding, leaving two left for &0's party.",
                    "FailureMessage" : "The Gimmighoul simply refuse to listen as you in vain to lecture on the merits of a mutually-beneficial econcomic system. Demotivated, the party continues, in search of lands where their economic ideals may be more appreciated.",
                    "SuccessFunction" : (lambda: DungeonItem(2, mandate=["Gimmighoul Coin"])),
                    "Rewards" : ["2x Gimmighoul Coins"],
                    "FailureFunction": (lambda: DemotivateParty()),
                    "Penalties" : ["DP"],
                }
            }
        },
        "DungeonEvent18": {
            "IntroText": "An elderly-looking &p is sitting on a rock, calling out to a crowd of other &p surrounding it. The funny scene reminds &0 of some of &is Instructors' lectures. What should &e do?",
            "Options": {
                "Send out &0m to listen to the 'lecture.'" : {#+8 (4 * 2),
                    "Threshold": -2+ 20, 
                    "Skill": "Strategy",  
                    "SuccessMessage" : "Though the gathering startles a bit at the sound of &0's Poké Ball, they accept the newcomer into their ranks, and &0m seems to get {i}something{/i} from whatever the elderly &p is imparting. It returns to &0 at the end with renewed, contagious, determination.",
                    "FailureMessage" : "The gathering startles at the sound of &0's Poké Ball, and the younger &p run off in terror! Believing &0m to be a threat, the elder leaps at &0 with grim determination!",
                    "SuccessFunction" : (lambda: MotivateParty()),
                    "Rewards" : ["MP"],
                    "FailureFunction": (lambda: DungeonFight({ "EnemyBoosts" : [(Stats.Speed, -1)], "Offset" : 5 })),
                    "Penalties": ["F"]
                },
                "Listen in on the 'lecture.'": {#+6 (3 * 2),
                    "Threshold": -2+ 18,
                    "Skill": "Learning",
                    "SuccessMessage": "&0 sits down quietly and listens intently to the elder &p as it shows off its moves for the younger ones around it. Though the noises it makes mean little, &0 feels as though &e understands more about its species, and leaves the lecture satisfied and knowledgeable.",
                    "FailureMessage": "&0 had only just sat down when the elder &p looks up sharply, notices &im, and quickly absconds from the scene. &0 sighs and moves on.",
                    "SuccessFunction" : (lambda: MotivateSquadder(change=3)),
                    "Rewards" : ["M3"],
                },
                "Attack the gathering!": {#+2
                    "SuccessMessage": "The younger &p flee in panic, but the elder leaps at &0 with grim determination!",
                    "BattleFunction": (lambda: DungeonFight({ "EnemyBoosts" : [(Stats.Speed, -1)], "Offset" : 5 }))
                }
            }
        },
        "DungeonEvent19": {
            "IntroText": "The mysteriosity fluctuates, and a large crack starts opening up in the ground! &* is on the other side... what should &0 do?",
            "Options": {
                "Grab &* and pull &*im over!": {#+8 (4 * 2)/-1
                    "Threshold": -2+ 19,
                    "Skill": "Physicality",
                    "SuccessMessage": "&0 digs &is feet into the ground and pulls with all &is strength, sending &* soaring over to safety! Everyone is very thoroughly impressed by &0's feat, even the scratched-up &*.",
                    "FailureMessage": "&0 digs &is feet into the ground and pulls with all &is strength, but quickly realizes that &* is pulling &0im more than the other way around. &E lets go, and the parties go their separate ways before reuniting later--much later. &* gives a &0 a well-deserved ribbing about &is lackluster rescue attempt.",
                    "SuccessFunction" : (lambda: MotivateParty()),
                    "Rewards" : ["MP"],
                    "FailureFunction": (lambda: DemotivateSquadder()),
                    "Penalties" : ["D"],
                },
                "Encourage &* to jump across!" : {#+4 (2 * 2)/-3
                    "Threshold": -2+ 13, 
                    "Skill": "Leadership",  
                    "SuccessMessage" : "&* closes &*is eyes and jumps across the gap! Letting out a big sigh of relief, &0 helps &* back onto &*is feet, and dusts &*im off. The two continue, with renewed faith in each other's abilities.",
                    "FailureMessage" : "&* runs up the edge, but hesitates. &* backs off apologetically, signalling &*e'll meet back up with the rest of the party later. Eventually, &*e does, but the rest of the party has lost a lot of time waiting for &*im.",
                    "SuccessFunction" : (lambda: [MotivateSquadder(), MotivateSquadder(randsquad)]),
                    "Rewards": ["M", "MR"],
                    "FailureFunction": (lambda: [DemotivateParty(exclude=[randsquad])]),
                    "Penalties": ["DP"]
                },
                "Wait out the quakes" : {#+2 (1 * 2)/-2
                    "Threshold": -2+ 12, 
                    "Skill": "Lore Smarts",  
                    "SuccessMessage" : "&0 remembers reading that Mysteriosity-caused chasms such as these often seal themselves up over time, without any intervention required. A couple minutes later, &0 is proven correct when the split earth abruptly rejoins itself. Satisfied in &is knowledge, &0 continues on.",
                    "FailureMessage" : "&0 remembers reading that Mysteriosity-caused chasms such as these often seal themselves up over time, without any intervention required. However, even after a long time has passed, the chasm is still wide and impenetrable. Sighing, &0 agrees to rejoin &* elsewhere, instead of wasting more time here.",
                    "SuccessFunction" : (lambda: [MotivateSquadder()]),
                    "Rewards" : ["M"],
                    "FailureFunction": (lambda: [DemotivateSquadder(), DemotivateSquadder(randsquad)]),
                    "Penalties": ["D", "DR"]
                }
            }
        },
        "DungeonEvent20": {
            "IntroText": "The mysteriosity fluctuates, and the terrain beneath &0's feet suddenly turns to quicksand! The party starts sinking swiftly, their struggles only hastening their descent. What should &0 do?",
            "Options": {
                "Grab the 'shore' and pull &imself out!" : {#+8 (4 * 2)/-4
                    "Threshold": -2+ 16, 
                    "Skill": "Physicality",  
                    "SuccessMessage" : "&0 manages to pull &imself out of the sand, then reaches out for the rest of &is party, pulling them up with &im. Everyone breathes a sigh of relief as they get back on their feet.",
                    "FailureMessage" : "&0 tries to pull &imself out of the sand, but the suction is too strong. &E loses &is grip, and sinks into the sand, as do the others. After a moment of darkness, the sand drops them, promptly and unceremoniously, back where they were before. Frustrated, they prepare for the long trudge back.",
                    "SuccessFunction" : (lambda: [MotivateParty()]),
                    "Rewards": ["MP",],
                    "FailureFunction": (lambda: [DemotivateParty()]),
                    "Rewards": ["DP",]
                },
                "Stay calm and maximize surface area!": {#+2 (1 * 2)/-4
                    "Threshold": -2+ 10,
                    "Skill": "Adaptability",
                    "SuccessMessage": "&0 spreads out &is limbs and lays back, looking for all the world like a normal person at the pool. &E quickly stops sinking, and the rest of the party follows suit. From this new, stable, position, the party are able to help each other out of the pit, praising &0 for keeping a cool head.",
                    "FailureMessage": "&0 attempts to stabilize &is position, but can't find an angle that doesn't cause &im to tip even more. The party sinks into the quicksand--which drops them, promptly and unceremoniously, back where they were before. Frustrated, they prepare for the long trudge back.",
                    "SuccessFunction" : (lambda: MotivateSquadder()),
                    "Rewards" : ["M"],
                    "FailureFunction": (lambda: DemotivateParty()),
                    "Penalties" : ["DP"],
                },
                "Get a Pokémon to pull &im out!" : {#+4 (2 * 2)/-4/-3
                    "Threshold": -2+ 9, 
                    "Skill": "Pokémon Handling",  
                    "SuccessMessage" : "&0 quickly sends out &0m, which pulls &im out of the mire, then returns for the other party members. Praising &0m for its bravery, and &0 for &is quick thinking, the party continues on.",
                    "FailureMessage" : "&0 quickly sends out &0m, but it isn't eager to approach the quicksand itself, and that moment of hesitation is too much for the party. They sink into the quicksand--which drops them, promptly and unceremoniously, back where they were before. Frustrated, they prepare for the long trudge back.",
                    "SuccessFunction" : (lambda: MotivateSquadder(2)),
                    "Rewards" : ["M2"],
                    "FailureFunction": (lambda: DemotivateParty()),
                    "Penalties" : ["DP"],
                    "ExcludeFunction" : ("Partner cannot learn Fly and does not have Levitate!", (lambda: not HasFlyingPokemon(squadleader)))
                }
            }
        },
        "DungeonEvent21": {
            "IntroText": "The party comes across a pile of Gimmighoul coins lying on the ground. They look to &0 for direction. What should &0 do?",
            "Options": {
                "Invest in the pile" : {#+6 (3 * 2)/-1
                    "Threshold": -2+ 17, 
                    "Skill": "Risk-Taking",  
                    "SuccessMessage" : "&0, to the bafflement of the others, adds a couple of &is own Gimmighoul coins to the pile. Though &* insists that's not how economics works, &0 seems happy.",
                    "FailureMessage" : "&0, to the bafflement of the others, adds a couple of &is own Gimmighoul coins to the pile. By the time &* has explained that's not how economics works, the party is too far gone to return to the pile...",
                    "SuccessFunction" : (lambda: MotivateSquadder(3)),
                    "Rewards" : ["M3"],
                    "FailureFunction": (lambda: DemotivateSquadder()),
                    "Penalties" : ["D"],
                },
                "Attempt to take an extra coin": {#+2/-1
                    "Threshold": -2+ 13,
                    "Skill": "Deception",
                    "SuccessMessage": "When the rest of the party isn't looking, &0 sneakily pulls an extra coin from the bag, before sharing them around 'equally.'",
                    "FailureMessage": "&0 attempts to sneakily take a coin from the bag, but &* notices. Though &* doesn't say anything, the atmosphere gets notably chillier...",
                    "SuccessFunction" : (lambda: DungeonItem(numitems=2, mandate=["Gimmighoul Coin"])),
                    "Rewards" : ["2x Gimmighoul Coin"],
                    "FailureFunction": (lambda: DemotivateSquadder(randsquad)),
                    "Penalties" : ["DR"],
                    "ExcludeFunction" : ("[first_name] cannot deceive!", (lambda: squadleader.Type == TrainerType.Player))
                },
                "Share the coins equally" : { 
                    "SuccessMessage" : "Avoiding a conflict, everyone shares the coins amongst each other.",
                    "SuccessFunction" : (lambda: DungeonItem(mandate=["Gimmighoul Coin"])),
                    "Rewards": ["1x Gimmighoul Coin"]
                }
            }
        },
        "DungeonEvent22": {
            "IntroText": "The party has gone without water for a while, and they're starting to be quite parched. In the distance, &0 thinks &e sees a natural pool of water... what should &e do?",
            "Options": {
                "Approach the pool" : {#+8 (4 * 2)/-4/+2
                    "Threshold": -2+ 18, 
                    "Skill": "Risk-Taking",  
                    "SuccessMessage" : "Yes, it wasn't an illusion! The pool is full of pristine, clean, water. Everyone takes several grateful gulps, and continues onwards, more motivated than before.",
                    "FailureMessage" : "As the party approaches the water, it becomes clear that it's not water, at all, but a pile of glimmering Gimmighoul Coins, that merely looked like water from a distance. The party spreads the pile amongst themselves, but really wishes they had some water with them, instead of useless metal...",
                    "SuccessFunction" : (lambda: MotivateParty()),
                    "Rewards" : ["MP"],
                    "FailureFunction": (lambda: [DemotivateParty(), DungeonItem(mandate=["Gimmighoul Coin"])]),
                    "Penalties": ["DP", "1x Gimmighoul Coin"]
                },
                "Throw something into the pool": {#+4 (2 * 2)/-1
                    "Threshold": -2+ 15,
                    "Skill": "Cunning",
                    "SuccessMessage": "&0 tosses an item towards the 'pool', making sure it's not a trap of some kind. The pool makes a strange, metallic, 'clinking' sound, revealing it's not a pool at all, but a pile of Gimmighoul coins! The party spreads the pile amongst themselves, and carries on.",
                    "FailureMessage": "&0 tosses an item towards the 'pool', and hits an unsuspecting &p that was taking a drink! It charges at &0, angry at the interruption!",
                    "SuccessFunction" : (lambda: DungeonItem(numitems=2, mandate=["Gimmighoul Coin"])),
                    "Rewards": ["2x Gimmighoul Coin"],
                    "FailureFunction": (lambda: DungeonFight()),
                    "Penalties" : ["F"],
                },
                "Convince everyone to avoid the pool.": {#+6 (3 * 2)/-3/-3
                    "Threshold": -2+ 12,
                    "Skill": "Persuasion",
                    "SuccessMessage": "Knowing the many invisible dangers that might be lurking in the pool--bacteria, Pokémon, contaminants--&0 convinces everyone to stay away from it, though they're not happy about it. &0 feels confident &e made the right choice, though.",
                    "FailureMessage": "Knowing the many invisible dangers that might be lurking in the pool--bacteria, Pokémon, contaminants--&0 tries to convince everyone to stay away from it. They refuse to listen, and end up getting a pretty severe stomach bug from the water.",
                    "SuccessFunction" : (lambda: [MotivateSquadder(3), DemotivateParty(exclude=[squadleader])]),
                    "Rewards": ["M3", "DPXL"],
                    "FailureFunction": (lambda: DemotivateParty(exclude=[squadleader])),
                    "Rewards": ["DPXL"],
                }
            }
        },
        "DungeonEvent23": {
            "IntroText": "The sound, of echoing, giggling, laughter begins to emanate from every dark corner of the &l. &* starts getting quite nervous, and &0 finally stops walking, intent on doing something about it. But what?",
            "Options": {
                "Thank the laughter for the company": {#+4 (4 * 2),
                    "Threshold": -2+ 20,
                    "Skill": "Healing",
                    "SuccessMessage": "Laughter is the best medicine, after all. By reframing &is paradigm, &0 begins to appreciate the laughter--even feeling energized by it. When &0 thanks the mysterious laughter, it lets out one last chuckle, then fades away. The party breathes a sigh of relief.",
                    "FailureMessage": "&0 attempts to thank the laughter, but as soon as &e starts talking, it abruptly cuts out. &0's gratitude meets nothing but open air...",
                    "SuccessFunction" : (lambda: MotivateParty()),
                    "Rewards": ["MP"]
                },
                "Laugh louder" : {#+2 (1 * 2)/-1
                    "Threshold": -2+ 13, 
                    "Skill": "Leadership",  
                    "SuccessMessage" : "&0 throws &is shoulders back and lets out a confident, hearty guffaw that echoes out into the &l. The laughter abruptly ceases. A moment later, there's a sound of cheering, and even a bit of applause... it seems this laughing force, whatever it was, be it Pokémon or something else, was just trying to entertain.",
                    "FailureMessage" : "&0 throws &is shoulders back and tries to let out a hearty guffaw that echoes out into the &l. Unfortunately, given &is nervousness, &0's voice cracked, and a pitiful half-laugh is left echoing around the &l, leaving &im feeling quite awkward.",
                    "SuccessFunction" : (lambda: MotivateSquadder()),
                    "Rewards" : ["M"],
                    "FailureFunction": (lambda: DemotivateSquadder()),
                    "Penalties" : ["D"],
                },
                "Tell a joke": {#-4
                    "Threshold": -2+ 8,
                    "Skill": "Persuasion",
                    "SuccessMessage": "&0 recites a shaggy-dog joke &e remembered from a book. It's long, meandering, and altogether actively unfunny. Nevertheless, the laughter fades away. Mission... accomplished?",
                    "FailureMessage": "&0 recites a shaggy-dog joke &e remembered from a book. It's long, meandering, and altogether actively unfunny. Unfortunately, the laughter just gets louder. Perhaps this wasn't a good idea.",
                    "FailureFunction": (lambda: DemotivateParty()),
                    "Penalties" : ["DP"],
                }
            }
        },
        "DungeonEvent24": {
            "IntroText": "The party comes across a wild &p, trapped underneath a boulder. It appears to be in pain, but it's lashing out wildly, and getting close might prove dangerous. Still, &0 can't just leave it there... what should &0 do?",
            "Options": {
                "Use a long object to push the rock off of it": {#+4 (4 * 2),
                    "Threshold": -2+ 20,
                    "Skill": "Physicality",
                    "SuccessMessage": "Grabbing whatever &e can, &0 wedges the object underneath the large boulder, using the fulcrum to push it to the side. The party gives &0 a round of applause for &is heroism.",
                    "FailureMessage": "Grabbing whatever &e can, &0 wedges the object underneath the large boulder, using the fulcrum to push it to the side. Unfortunately... the boulder rolls off directly in &is direction! &E yelps and runs off as the boulder gives chase, the rest of the party in hot pursuit.",
                    "SuccessFunction" : (lambda: MotivateSquadder(change=3)),
                    "Rewards" : ["M3"],
                    "FailureFunction": (lambda: DemotivateSquadder()),
                    "Penalties" : ["D"],
                },
                "Endure the blows and push the boulder off" : {#+6 (3 * 2),
                    "Threshold": -2+ 18, 
                    "Skill": "Resilience",  
                    "SuccessMessage" : "&0 grits &is teeth, and pushes against the boulder, even as the &p flails and lashes out. &0 takes a couple blows, but is eventually able to free the &p. &E grins through a bruised face, as the rest of the party watches in admiration.",
                    "FailureMessage" : "&0 grits &is teeth, and pushes against the boulder, even as the &p flails and lashes out. &0 takes a couple blows... but the &p is rather ungrateful, and just attacks!",
                    "SuccessFunction" : (lambda: MotivateParty(exclude=[squadleader])),
                    "Rewards" : ["MPXL"],
                    "FailureFunction": (lambda: DungeonFight()),
                    "Penalties" : ["F"],
                },
                "Send out a strong Pokémon to push the boulder": {#+4 (2 * 2)/-3 (Requirement),
                    "Threshold": -2+ 13,
                    "Skill": "Pokémon Handling",
                    "SuccessMessage": "&0 sends out &0m, which easily knocks the boulder over to the side. The &p quickly scampers away, as everyone cheers on &0m and &0.",
                    "FailureMessage": "&0 sends out &0m, which easily knocks the boulder over to the side. However, &0 isn't able to control &p's instincts in this Mysteriosity zone, and &0 charges into battle with the &p!",
                    "SuccessFunction" : (lambda: MotivateSquadder(2)),
                    "Rewards" : ["M2"],
                    "FailureFunction": (lambda: DungeonFight()),
                    "Penalties" : ["F",],
                    "ExcludeFunction" : ("Partner cannot learn Strength!", (lambda: not HasStrongPokemon(squadleader)))
                }
            }
        },
        "DungeonEvent25": {
            "IntroText": "The party suddenly encounters a map sitting on an altar in the middle of a clearing. It appears old and yellowed, and its position rouses suspicion... what should &0 do?",
            "Options": {
                "Follow the map": {#+4 (4 * 2)/-2
                    "Threshold": -2+ 18,
                    "Skill": "World Smarts",
                    "SuccessMessage": "The map does not lie, and guides the party through the &l at a much faster pace. However, as soon as they find the next area, the map crumbles to dust, its mission complete...",
                    "FailureMessage": "The map uses too many obscure symbols and glyphs for &0 to easily parse, and as &e frustratedly hands it off to &*, it crumbles to dust, leaving nothing behind...",
                    "SuccessFunction" : (lambda: MotivateParty()),
                    "Rewards" : ["MP"],
                    "FailureFunction": (lambda: [DemotivateSquadder(), DemotivateSquadder(randsquad)]),
                    "Penalties" : ["D", "DR"]
                },
                "Determine the cartographer": {#+8 (4 * 2)/-4
                    "Threshold": -2+ 16,
                    "Skill": "Pokémon Smarts",
                    "SuccessMessage": "Taking a closer look at the map, &0 determines from the narrow, colorful, brushstrokes it has clearly been drawn by a Grafaiai. Being highly territorial, this map is a perfect demarcator of where {i}not{/i} to go, and the party avoids an unnecessary fight with relief.",
                    "FailureMessage": "Taking a closer look at the map, &0 determines from the narrow, colorful, brushstrokes it has clearly been drawn by a Smeargle. This belief is quickly disproven when several highly-territorial Grafaiai chase the party out of their territory, screeching and howling.",
                    "SuccessFunction" : (lambda: MotivateParty()),
                    "Rewards" : ["MP"],
                    "FailureFunction": (lambda: DemotivateParty()),
                    "Penalties" : ["DP"],
                },
                "Study the map from a distance" : {#+2 (2 * 1)/-1
                    "Threshold": -2+ 13, 
                    "Skill": "Learning",  
                    "SuccessMessage" : "Fearing some sort of trap, &0 eyeballs the map for several minutes, attempting to memorize as much of it as possible. The knowledge serves the party well for several more areas.",
                    "FailureMessage" : "Fearing some sort of trap, &0 eyeballs the map for several minutes, attempting to memorize as much of it as possible. However, the knowledge &e preserves seems less than reliable, and the party gets led off in the wrong direction more than once.",
                    "SuccessFunction" : (lambda: MotivateSquadder()),
                    "Rewards" : ["M"],
                    "FailureFunction": (lambda: DemotivateSquadder()),
                    "Penalties" : ["D"],
                }
            }
        },
        "DungeonEvent26": {
            "IntroText": "The party suddenly comes across a small river. There's a Sitrus Berry, a Totodile, and a Wooloo on one side, and they all need to get to the other side. What should &0 do?",
            "Options": {
                "Have each party member grab a different Pokémon or item": {#+8 (4 * 2)/-3 (Requirement),
                    "Threshold": -2+ 17,
                    "Skill": "World Smarts",
                    "SuccessMessage": "Cutting the Gordian knot, &1 grabs the Sitrus Berry, &2 grabs the Totodile, and &3 grabs the Wooloo as they all travel across the river without incident. On the other side, though, they wonder why, exactly, they did that. Shrugging, the party carries on, with &0 at least happy the party 'solved' the puzzle.",
                    "FailureMessage": "A good plan, save for the fact the Totodile will not permit &3 to get close to it. As soon as it sees movement, it quickly grabs the cabbage and runs off with it. Apparently they're omnivorous. &0 shrugs, and the party carries on, no worse for wear.",
                    "SuccessFunction" : (lambda: MotivateParty()),
                    "Rewards" : ["MP"],
                    "ExcludeFunction": ("Not enough party members!", (lambda: len(fullsquad) < 3))
                },
                "Never leave the cabbage and Wooloo, or the Totodile and Wooloo, alone": {#+4 (4 * 2)/-2
                    "Threshold": -2+ 14,
                    "Skill": "Strategy",
                    "SuccessMessage": "&0 manages to transport all three Pokémon and items to the other side without incident. &E pauses as &e considers {i}why{/i} exactly, &e did that. Shrugging, the party carries on, with &0 at least happy &e solved the puzzle.",
                    "FailureMessage": "&0 cannot figure out a way to do this, and, when &is back is turned, the cabbage is devoured--by the Totodile, funnily enough. Apparently they're omnivorous. &0 shrugs, and the party carries on, no worse for wear.",
                    "SuccessFunction" : (lambda: MotivateSquadder())
                },
                "Who cares about the puzzle?! I want the Pokémon!" : {#+2 (2 * 1)/-1 
                    "SuccessMessage" : "The Pokémon quickly flee at &0's approach. Perhaps they sensed their role as abstract puzzle representations was coming to an end. However, the Sitrus Berry on the ground does not have legs, and is much less metaphorical. &0 takes it as a consolation prize.",
                    "SuccessFunction" : (lambda: DungeonItem(mandate=["Sitrus Berry"])),
                    "Rewards" : ["1x Sitrus Berry"]
                }
            }
        },
        "DungeonEvent27": {
            "IntroText": "A tiny &p timidly approaches the party. It's so incredibly small that &0 didn't even notice it until it was right in front of &im. What should &0 do?",
            "RegenCriteria": (lambda x: -pokedexlookup(x, DexMacros.Weight) + 20 * Pokemon(x).HasType("Flying")),
            "Options": {
                "Feed the tiny &p": {
                    "Threshold": -2+ 17,
                    "Skill": "Pokémon Smarts",
                    "SuccessMessage": "&0, using &is knowledge of Pokemon diets, is able to procure a satisfying meal for the &p. It eats quickly, nods in gratitude, then flees the scene. Curiously, other &p seem to be less aggressive towards the party now...",
                    "FailureMessage": "&0 attempts to use &is knowledge of Pokemon diets to procure a satisfying meal for the &p. Unfortunately, it turns up its nose at the proffered plate, and disappears into the shadows of the &l as quickly as its diminutive frame can manage. &0 is disgruntled at its ingratitude",
                    "SuccessFunction" : (lambda: MotivateParty()),
                    "Rewards" : ["MP"],
                    "FailureFunction" : (lambda: DemotivateSquadder()),
                    "Penalties" : ["D"],
                },
                "Shoo it away": {#+2 (2 * 1) / -4
                    "Threshold": -2+ 8,
                    "Skill": "Lore Smarts",
                    "SuccessMessage": "&0 recalls a story about how some wild Pokémon packs will send their weakest member out to beg from a trainer, then, once they have confirmed the trainer has food, jump them. With &0 refusing to yield to the tiny &p's charms, it eventually gives up and sneaks back into the shadows, where two significantly larger &p are skulking.",
                    "FailureMessage": "&0 recalls a story about how some wild Pokémon packs will send their weakest member out to beg from a trainer, then, once they have confirmed the trainer has food, jump them. With &0 refusing to yield to the tiny &p's charms, it eventually turns away, stumbling as it drags itself back into the shadows. How sad...",
                    "SuccessFunction" : (lambda: MotivateSquadder()),
                    "Rewards" : ["M"],
                    "FailureFunction" : (lambda: DemotivateParty()),
                    "Penalties" : ["D"],
                },
                "Battle it!": {
                    "SuccessMessage": "&* furrows &*is brow at &0's aggression towards the tiny Pokémon, but no-one tries to stop &im.",
                    "SuccessFunction" : (lambda: DemotivateSquadder(randsquad)),
                    "Rewards": ["DR"],
                    "BattleFunction": (lambda: DungeonFight({ "Offset" : -99 })),
                    "Rewards": ["F"],
                }
            }
        },
        "DungeonEvent28": {
            "IntroText": "The party suddenly comes across a moss and ivy-covered old-style school bus sitting in the middle of a clearing. Clearly, the mysteriosity had dropped it here, as there's no sensible way for a school bus to have ended up in the middle of the &l. What should &0 do?",
            "Options": {
                "Attempt to fix the bus' engine": {#+6 (2 * 3),
                    "Threshold": -2+ 18,
                    "Skill": "World Smarts",
                    "SuccessMessage": "&0 manages to pop the hood of the bus, but it's entirely lacking an engine, with the spacious area instead containing a pile of random junk items. Sifting through the debris, &0 is able to find a few items of use...",
                    "FailureMessage": "&0 looks around in the bus' cabin, but isn't able to even figure out how to pop the hood to get to the engine. Shrugging, &e carries on.",
                    "SuccessFunction" : (lambda: DungeonItem(3)),
                    "Rewards" : ["I3"]
                },
                "Rest in the bus": {#+6 (1.5 * 4)/-3
                    "Threshold": -2+ 15,
                    "Skill": "Risk-Taking",
                    "SuccessMessage": "Grateful for the shelter, bizarre as it is, &0 directs the party to put their feet up and relax. Though nervous at first, the bus proves to be safe and stable, and everyone takes the time to eat a snack, recover their breath, and increase their morale.",
                    "FailureMessage": "Grateful for the shelter, bizarre as it is, &0 directs the party to put their feet up and relax. Unfortunately, only &e is able to relax in this old, creaky, vehicle--everyone else is far too nervous, and emerge from their break far more tired than before.",
                    "SuccessFunction" : (lambda: MotivateParty()),
                    "Rewards" : ["MP"],
                    "FailureFunction" : (lambda: [DemotivateParty(exclude=[squadleader]), MotivateSquadder(squadleader)]),
                    "Penalties" : ["DPXL", "M"]
                },
                "Search for salavageable parts": {#+2 (2 * 1),
                    "Threshold": -2+ 14,
                    "Skill": "Adaptability",
                    "SuccessMessage": "&0 looks around the body of the bus, but finds everything to be too corroded or old to be of any real value. About to give up, &e suddenly notices that there's a single Gimmighoul coin hanging on a string from the rearview mirror. Shrugging, &e takes it.",
                    "FailureMessage": "&0 looks around the body of the bus, but finds everything to be too corroded or old to be of any real value, and gives up.",
                    "SuccessFunction" : (lambda: DungeonItem(mandate=["Gimmighoul Coin"])),
                    "Rewards": ["1x Gimmighoul Coin"]
                },
            }
        },
        "DungeonEvent29": {
            "IntroText": "The party finds a broken top-like object nestled in a small pit in the floor of the &l. The rest of the party looks to &0 for direction. What should &0 do with the top?",
            "RegenCriteria": (lambda x: Pokemon(x).HasType("Bug") * 3 + Pokemon(x).HasType("Ground") * 3 + Pokemon(x).HasType("Rock") + Pokemon(x).HasType("Grass")),
            "Options": {
                "Study its structure": {#+5 (3 * 1.5)/-1
                    "Threshold": -2+ 16,
                    "Skill": "Learning",
                    "SuccessMessage": "&0 examines it intently, and is able to conclude it's some sort of device that is capable of conveying the emotions of a user to a Pokémon. Of course, it's useless without its stylus-like counterpart, so &0 leaves it there, satisfied with &is knowledge.",
                    "FailureMessage": "&0 examines it intently, but is unable to determine what it is--except, perhaps, a high-tech dreidel, or perhaps a Beyblade. Either way, unlike the broken top, &0's head is now spinning.",
                    "SuccessFunction" : (lambda: MotivateSquadder(3)),
                    "Rewards" : ["M3"],
                    "FailureFunction" : (lambda: DemotivateSquadder()),
                    "Penalties" : ["D"],
                },
                "Pocket it": {#+4 (2 * 2),
                    "Threshold": -2+ 16,
                    "Skill": "Pokémon Smarts",
                    "SuccessMessage": "&0 plucks the top from the ground, being careful not to disturb the soil around it too much, as &e knows that burrowing Ground, Bug, and Rock-types will often plug their burrows with random manmade trash. &0's caution is rewarded, when it turns out this top plugged not a Pokémon-burrow, but a storehole for items.",
                    "FailureMessage": "&0 plucks the top from the ground, but quickly realises this 'top' served as the 'doorway' for a Pokémon's burrow! The grumpy &p attacks!",
                    "SuccessFunction" : (lambda: DungeonItem(2)),
                    "Rewards" : ["I2"],
                    "FailureFunction" : (lambda: [DungeonFight()]),
                    "Penalties" : ["F"],
                },
                "Identify it": {#-1
                    "Threshold": -2+ 11,
                    "Skill": "World Smarts",
                    "SuccessMessage": "&0 easily recognizes this as one half of a Capture Styler. The question is begged, then--what happened to the ranger who owned it? The party continues on, hoping that this Styler's presence was a trick of the Mysteriosity, and not an indicator of tragedy.",
                    "FailureMessage": "&0 is certain &e had seen something like this on TV before, but just cannot place &is finger on it, and leaves disappointed.",
                    "FailureFunction" : (lambda: DemotivateSquadder()),
                    "Penalties" : ["D"],
                },
            }
        },
        "DungeonEvent30": {
            "IntroText": "The party suddenly encounters a dark crystal floating in the air, pulsing and thrumming with energy. Aggression springs forth in every member of the party, as they begin to resent &0's commanding role...",
            "Options": {
                "Quickly smash it": {#+12 (2 * 4 * 1.5)/-4(4 * 1),
                    "Threshold": -2+ 20,
                    "Skill": "Physicality",
                    "SuccessMessage": "&0 doesn't wait a second before grabbing the crystal and smashing it on the ground. The rest of the party suddenly seems to snap out of their fugue, and cheers on &0's quick thinking. Everyone leaves together, bonds reforged and strengthened.",
                    "FailureMessage": "&0 attempts to smash the crystal, but succeeds in nothing but scratching &is knuckles. &* laughs meanly, and an argument starts as the party stomps off further into the &l, leaving the dark crystal humming quietly behind them...",
                    "SuccessFunction" : (lambda: MotivateParty(2)),
                    "Rewards" : ["MP2"],
                    "FailureFunction" : (lambda: DemotivateParty()),
                    "Penalties" : ["D"],
                },
                "Maintain order": {#+6 (4 * 1.5)/-4
                    "Threshold": -2+ 14,
                    "Skill": "Leadership",
                    "SuccessMessage": "&0 maintains control of the group, convincing them to realize the malignant aura of the crystal is influencing them unduly. The party begins to wake up from their fugue, and thanks &0 as they continue on.",
                    "FailureMessage": "&0 attempts to maintain control of the group, but succeeds in nothing but starting an argument. The party stomps off further into the &l, leaving the dark crystal humming quietly behind them...",
                    "SuccessFunction" : (lambda: MotivateParty()),
                    "Rewards" : ["MP"],
                    "FailureFunction" : (lambda: DemotivateParty()),
                    "Penalties" : ["D"],
                },
                "Sneakily pocket the gem": {#+5 (3 * 1.5)/-7
                    "Threshold": -2+ 10,
                    "Skill": "Deception",
                    "SuccessMessage": "&0 distracts the rest of the party, but as soon as &e touches the gem, it disappears, leaving only a lingering aura that sticks to &im. &0 is filled with confidence, aggression, ambition... and becomes an intolerable jackass to the rest of the party, until the effect wears off.",
                    "FailureMessage": "&0 attempts to distract the rest of the party, but &* notices the deception, and a large argument ensues. Everyone is left grumpy and dissatisfied.",
                    "SuccessFunction" : (lambda: [DemotivateParty(exclude=[squadleader]), MotivateSquadder(3)]),
                    "Rewards": ["DPXL", "M3"],
                    "FailureFunction" : (lambda: DemotivateParty()),
                    "Penalties": ["DP"],
                    "ExcludeFunction" : ("[first_name] cannot deceive!", (lambda: squadleader.Type == TrainerType.Player))
                },
            }
        },
        "DungeonEvent31": {
            "IntroText": "The party comes across a small bush, bursting with berries. Their deep blue color easily identifies them as Oran Berries, and the party's Pokémon greedily begin moving toward the bush, intent on liberating it of its fruity contents.",
            "Options": {
                "Wait for someone else to try it first": {#+5 (3 * 1.5)/-3
                    "Threshold": -2+ 14,
                    "Skill": "Deception",
                    "SuccessMessage": "&0 feigns interest in a nearby patch of ground as &* takes a big gulp of the berries. &*'s face immediately turns sour, signaling to the rest of the party these are, in fact, poisonous Oren Berries, and not their healing twins. The rest of the party salutes &*'s sacrifice.",
                    "FailureMessage": "&0 feigns interest in a nearby patch of ground, but &* notices the act and hesitates. After all's said and done, no-one is willing to be the first to try the berries, so everyone leaves the bush behind. unpicked.",
                    "SuccessFunction" : (lambda: [MotivateParty(exclude=[randsquad]), DemotivateSquadder(randsquad, -3)]),
                    "Rewards" : ["MPXL", "DR3"],
                    "ExcludeFunction" : ("[first_name] cannot deceive!", (lambda: squadleader.Type == TrainerType.Player))
                },
                "Identify the berries": {#+6 (4 * 1.5)/-8(2 * 4),
                    "Threshold": -2+ 10,
                    "Skill": "Healing",
                    "SuccessMessage": "&0 cautions the party to hold back until &e confirms the berries' identity. After a moment, &0 steps back and reveals the disappointing news: they're actually Oren Berries, which are quite poisonous. The party grumbles, but thanks &0 for warding them off from a dangerous mistake.",
                    "FailureMessage": "&0 cautions the party to hold back until &e confirms the berries' identity. After a moment, &0 cheerily announces that they are, as they appear to be, safe and healthy Oran Berries. Unfortunately, they're actually Oren Berries, which are quite poisonous. The entire party suffers from explosive diarrhea for the rest of the voyage through the &l.",
                    "SuccessFunction" : (lambda: MotivateParty()),
                    "Rewards" : ["MP"],
                    "FailureFunction" : (lambda: DemotivateParty(-2)),
                    "Penalties" : ["DP2"]
                },
                "Pick a few berries for later analysis": {
                    "SuccessMessage": "&0 pockets a few of the Oran Berries, in case &is Pokémon want them later.",
                    "SuccessFunction" : (lambda: DungeonItem(numitems = 3, mandate=["Oran Berry"])),
                    "Rewards" : ["3x Oran Berry"]
                },
            }
        },
        "DungeonEvent32": {
            "IntroText": "The party suddenly notices a thick mist swirling around them, quickly cutting their visibility. &* starts panicking, and the party seems as though it may fall apart from within if this situation is not resolved...",
            "Options": {
                "Tell everyone to remain calm": {#+6 (4 * 1.5)/-1
                    "Threshold": -2+ 17,
                    "Skill": "Persuasion",
                    "SuccessMessage": "&0 buries &is own feelings of unease, and convinces everyone to join hands. With the fear of getting separated no longer present, the party is able to find their way out of the mist safely.",
                    "FailureMessage": "&0 is unable to overcome &is own feelings of unease, and it comes out in the pitiful speech &e gives, which has zero motivating effect. The party remains together, but things are now more awkward.",
                    "SuccessFunction" : (lambda: MotivateParty(exclude=[randsquad])),
                    "Rewards" : ["MPXR"],
                    "FailureFunction" : (lambda: DemotivateSquadder()),
                    "Penalties" : ["D"],
                },
                "Create a plan to regroup and join hands": {#+6 (4 * 1.5)/-4
                    "Threshold": -2+ 12,
                    "Skill": "Strategy",
                    "SuccessMessage": "&0 convinces everyone to stay still long enough to hear &is plan. Calming down and regrouping, the party is able to leave the fog together.",
                    "FailureMessage": "&0 is unable to come up with a comprehensive plan in the disorienting mist, so everyone ends up bumping into each other until by pure chance, they emerge into a mistless area. Everyone has suffered minor bruises.",
                    "SuccessFunction" : (lambda: MotivateParty()),
                    "Rewards" : ["MP"],
                    "FailureFunction" : (lambda: DemotivateParty()),
                    "Penalties" : ["D"],
                },
                "Use a Pokémon to blow away the mist" : {#+5 (3 * 1.5), -4, -3 (requirement),
                    "Threshold": -2+ 10, 
                    "Skill": "Adaptability",  
                    "SuccessMessage" : "&0 keeps a cool head, and sends out &0m, who is easily able to dispel the mysterious fog that blocks the area. Everyone in the party cheers on &0 and &0m.",
                    "FailureMessage" : "&0 sends out &0m, but the fog has a panic-inducing effect that makes it unable to dispel the fog properly. The party carries onwards blindly, bumping into something every few minutes.",
                    "SuccessFunction" : (lambda: MotivateSquadder(3)),
                    "Rewards" : ["M3"],
                    "FailureFunction" : (lambda: DemotivateParty()),
                    "Penalties" : ["DP"],
                    "ExcludeFunction" : ("Partner cannot learn Defog!", (lambda: not HasDefogger(squadleader)))
                }
            }
        },
        "DungeonEvent33": {
            "IntroText": "The party encounters a small clay doll, some ancient toy, sitting in a pile of sand. Likely deposited here by the Mysteriosity, the item lays dormant on the ground.",
            "Options": {
                "Identify the toy": {
                    "Threshold": -2+ 20,
                    "Skill": "Lore Smarts",
                    "SuccessMessage": "&0 recognizes it as a plaything of a long-lost Hoennian civilization, referred to as a {i}Yajilon{/i} in the ancient language. As soon as &0 says the word 'Yajilon', the toy suddenly springs to life, attacking &im!",
                    "FailureMessage": "&0 is unable to identify the strange toy, and the party moves on, unaffected by the odd encounter.",
                    "SuccessFunction" : (lambda: DungeonFight(assignmon=Pokemon("Baltoy", level=dungeonlevel, shinylock=False))),
                    "Rewards" : ["F"]
                },
                "Clean off the toy": {
                    "Threshold": -2+ 16,
                    "Skill": "Pokémon Handling",
                    "SuccessMessage": "&0 gently picks it up, and traces the strange lines and fading paint that cover its body. To the party's surprise, at &0's touch, the toy starts moving around, jumping out of &is hands and challenging &im to a battle!",
                    "FailureMessage": "&0 picks up the toy, but time has not been kind to it--even a small impact causes its sandy body to crumble. The party is filled with a sense of melancholy as a gentle wind blows the toy's dust around the &l.",
                    "SuccessFunction" : (lambda: DungeonFight(assignmon=Pokemon("Baltoy", level=dungeonlevel, shinylock=False))),
                    "Rewards" : ["F"],
                    "FailureFunction" : (lambda: DemotivateParty()),
                    "Penalties" : ["D"],
                },
                "Attempt to carefully extract the toy": {#+2 (item)/-4
                    "Threshold": -2+ 10,
                    "Skill": "Cunning",
                    "SuccessMessage": "With quick hands, &0 is able to pull the toy out of the ground, and realizes that it is actually a decorative jar! Opening the jar, there is an item inside, which &0 takes.",
                    "FailureMessage": "&0 tries to pick up the toy, but time has not been kind to it--even a small impact causes its sandy body to crumble. The party is filled with a sense of melancholy as a gentle wind blows the toy's dust around the &l.",
                    "SuccessFunction" : (lambda: DungeonItem()),
                    "Rewards" : ["I"],
                    "FailureFunction": (lambda: DemotivateParty()),
                    "Penalties" : ["DP"],
                }
            }
        },
        "DungeonEvent34": {
            "IntroText": "A pink mist wafts through the chamber the party enters. Instantly, all party members feel more sensitive, as their breathing becomes more labored, and naughty ideas spring forth in their mind. Though the temptation is terrible, indulging in such fantasies would massively delay the mission--what should &0 do?",
            "Options": {
                "Hold &is breath and pass through": {#+6 (4 * 1.5)/-4
                    "Threshold": -2+ 14,
                    "Skill": "Resilience",
                    "SuccessMessage": "&0 takes a deep breath outside the room, then drags the rest of the party through the room, refusing to breathe, squinting through the mist as &e passes through. On the other side, the party regains their breath, and thanks &0 for his steadfastness, though &* looks back wistfully.",
                    "FailureMessage": "&0 takes a deep breath outside the room, but isn't able to hold &is breath all the way through, eventually gasping for breath halfway through. Though the party makes it through without incident, all party members have a certain itching, a certain heat, underneath their skin that just won't go away, and proves very distracting.",
                    "SuccessFunction" : (lambda: MotivateParty()),
                    "Rewards" : ["MP"],
                    "FailureFunction" : (lambda: DemotivateParty()),
                    "Penalties" : ["D"],
                },
                "Create rudimentary masks": {
                    "Threshold": -2+ 16,
                    "Skill": "Healing",
                    "SuccessMessage": "Using natural materials, and spare strips of cloth, &0 is able to create a series of masks that filter out the pink mist, allowing safe passage. Few like wearing them, but &0 is quite proud of &is quick thinking.",
                    "FailureMessage": "Using natural materials, and spare strips of cloth, &0 attempts to create a series of masks that filter out the pink mist, allowing safe passage. Unfortunately, they do not work as intended, and though the party makes it through without incident, all party members have a certain itching, a certain heat, underneath their skin that just won't go away, and proves very distracting.",
                    "SuccessFunction" : (lambda: MotivateSquadder(change=3)),
                    "Rewards" : ["M3"],
                    "FailureFunction" : (lambda: DemotivateParty()),
                    "Penalties" : ["D"],
                },
                "Dash through, running at top speed": {#+1 (item)/-4
                    "Threshold": -2+ 13,
                    "Skill": "Risk-Taking",
                    "SuccessMessage": "&0 dashes through the gaseous room, and though the acrid smoke burns at &is nostrils, &e gets through unharmed, and uninfluenced by the gas.",
                    "FailureMessage": "&0 tries to dash through the gaseous room, but the acrid smoke burnings at &is nostrils proves too strong to bear, and &* has to drag &im out of the room when &is giggling becomes uncontrollable.",
                    "SuccessFunction" : (lambda: MotivateSquadder()),
                    "Rewards" : ["M"],
                    "FailureFunction": (lambda: [MotivateSquadder(), DemotivateSquadder(randsquadder, -2)]),
                    "Penalties" : ["M", "DR2"],
                }
            }
        },
        "DungeonEvent35": {
            "IntroText": "There's a Poké Ball on the floor... everyone in the party rolls their eyes, not falling for such an old trick.",
            "Options": {
                "It's obviously a Voltorb!": {
                    "SuccessMessage": "As &0 sends out a Pokémon to battle the Voltorb, it suddenly uproots itself, sending a cloud of poisonous spores all around the area! This is no Voltorb, it's a Foongus!",
                    "SuccessFunction" : (lambda: DungeonFight(assignmon=Pokemon("Foongus", level=dungeonlevel, shinylock=False))),
                    "Rewards" : ["F"]
                },
                "Could this Foongus be more obvious?!": {
                    "SuccessMessage": "As &0 sends out a Pokémon to battle the Foongus, it suddenly starts sparking, sending paralyzing waves all around the area! This is no Foongus, it's a Voltorb!",
                    "SuccessFunction" : (lambda: DungeonFight(assignmon=Pokemon("Voltorb", level=dungeonlevel, shinylock=False))),
                    "Rewards" : ["F"]
                },
                "That's a Galarian Stunfisk, if I've ever seen one!": {
                    "SuccessMessage": "&0 sends out a Pokémon to battle the Stunfisk... and then realizes that, no, it really is just a Poké Ball, surrounded by some sharp rocks. Oops. &E pockets the Poké Ball, and moves on quickly.",
                    "SuccessFunction" : (lambda: DungeonItem(mandate=["Poké Ball"])),
                    "Rewards" : ["1x Poké Ball"]
                }
            }
        },
        "DungeonEvent36": {
            "IntroText": "{glitch=5.00}&0 sees something that &is eyes cannot comprehend. A bizarre backwards 'L' hovers before the party, casting no shadow, having no presence, but indescribably there.{/glitch}",
            "Options": {
                "Study it": {# +5 (3 * 1.5)/-1
                    "Threshold": -2+ 16,
                    "Skill": "Learning",
                    "SuccessMessage": "There is nothing to study. The harder &0 tries to understand it, the less &e knows. Eventually, enough of &is memory is erased that all &e can remember is a vague feeling of contentedness, perhaps the feeling of existence before life. Luckily, this haze does not last long.",
                    "FailureMessage": "There is nothing to study. &0 is staring intently at open air. Eventually, &* taps &im on the shoulder, shaking &im out of &is stupor, and the party proceeds onwards.",
                    "SuccessFunction" : (lambda: MotivateSquadder(change=3)),
                    "Rewards" : ["M3"],
                    "FailureFunction" : (lambda: DemotivateSquadder(-1)),
                    "Penalties" : ["D"]
                },
                "Reach out to it": {# +6 (3 * 2)/-4
                    "Threshold": -2+ 14,
                    "Skill": "Risk-Taking",
                    "SuccessMessage": "There is nothing to reach out to. However, when &e checks &is bag, &e notices some of &is items have duplicated.",
                    "FailureMessage": "There is nothing to reach out to. The party leaves, unsettled.",
                    "SuccessFunction" : (lambda: DungeonItem(numitems=3)),
                    "Rewards": ["I3"],
                    "FailureFunction" : (lambda: DemotivateParty(-1)),
                    "Penalties" : ["DP"]
                },
                "Ignore it": {# +6 (3 * 2)/-4
                    "Threshold": -2+ 20,
                    "Skill": "Resilience",
                    "SuccessMessage": "There is nothing to ignore. The moment &0 grits &is teeth and resolves to pass it up unhindered, it never was. {glitch=5.00}But you'll remember, won't you?{/glitch}",
                    "FailureMessage": "There is nothing to ignore. The nothing demands &is attention, and though &e does not look at it, it occupies a permanent part of &is memory.",
                    "SuccessFunction" : (lambda: AddEvent("Instructor Blaine", "SawGlitch")),
                    "Rewards" : ["Nothing."],
                    "FailureFunction" : (lambda: DemotivateSquadder(-1)),
                    "Rewards" : ["D"],
                }
            }
        },
        "DungeonEvent37": {
            "IntroText": "The party comes up on a Kangaskhan-shaped rock. The area here feels soothing, and &0 is tempted to rest up against the rock for a moment, and catch &is breath...",
            "RegenCriteria": (lambda x: Pokemon(x).HasType("Ground") * 2 + Pokemon(x).HasType("Bug") * 2 - pokedexlookup(x, DexMacros.Weight)),
            "Options": {
                "Search for items": {# +6 (3 * 2)/-1
                    "Threshold": -2+ 17,
                    "Skill": "Lore Smarts",
                    "SuccessMessage": "Knowing these Kangaskhan statues were often used as banks by ancient people, &0 searches around the base and pouch of the statue, until, as expected, &e finds a small bundle of items wrapped up in a handkerchief.",
                    "FailureMessage": "Fumbling blindly around the statue, the rest of the party watches &0 as &e awkwardly palms the statue. They leave to give &im some privacy, which does nothing to alleviate &is embarrassment.",
                    "SuccessFunction" : (lambda: DungeonItem(3)),
                    "Rewards" : ["I3"],
                    "FailureFunction" : (lambda: DemotivateSquadder()),
                    "Penalties" : ["D"],
                },
                "Take a picture": {#+3 (2 * 1.5)/-1
                    "Threshold": -2+ 14,
                    "Skill": "World Smarts",
                    "SuccessMessage": "&0 takes a picture of the statue, figuring that a museum, or perhaps one of the instructors, would be interested in seeing evidence of this strange and ancient structure. Of course, the Mysteriosity hurries the statue away as soon as the party moves on... but it's a momentary ego boost.",
                    "FailureMessage": "&0 takes a picture of the statue, but upon checking in on the picture later, sees that &is phone only took a screen full of static. Another unkind trick of the Mysteriosity, one supposes.",
                    "SuccessFunction" : (lambda: MotivateSquadder(2)),
                    "Rewards" : ["M2"],
                    "FailureFunction" : (lambda: DemotivateSquadder(-1)),
                    "Penalties": ["D"],
                    "ExcludeFunction" : ("Tia has no phone!", (lambda: squadleader.Name in ["tia", "latias"]))
                },
                "Tip it over": {# -1
                    "Threshold": -2+ 11,
                    "Skill": "Physicality",
                    "SuccessMessage": "The party jumps in surprised as the heavy stone statue falls over. Underneath, a disgruntled &p that was napping yaps loudly as it seeks retribution for its toppled home!",
                    "FailureMessage": "&0 heaves and hos, but isn't able to get the heavy stone statue to move an inch. On reflection, though, &e's not sure why &e would want to...",
                    "SuccessFunction" : (lambda: DungeonFight()),
                    "Rewards": ["F"],
                    "FailureFunction" : (lambda: DemotivateSquadder(-1)),
                    "Rewards": ["D"],
                }
            }
        },
        "DungeonEvent38": {
            "ExcludeFunction": (lambda x: x.Name not in ["Unhallowed Holt", "Splintered Glades", "Windswept Woods"]),
            "IntroText": "The party stumbles over a mossy rock, laid deep into the ground. It has clearly been sitting there for a long time, untouched by the ages... or perhaps it was only placed there moments ago by the Mysteriosity.",
            "Options": {
                "Rest on the rock": {# +6 (3 * 2)/-4
                    "Threshold": -2+ 14,
                    "Skill": "Leadership",
                    "SuccessMessage": "Seeing the tiredness of the party, &0 calls for everyone to take a break, which they gratefully do, resting in the soft moss.",
                    "FailureMessage": "Though &is heart was in the right place, &0's call for a break puts the rest of the party more on edge, and the rock, though covered in moss, is still an uncomfortable seat.",
                    "SuccessFunction" : (lambda: MotivateParty()),
                    "Rewards" : ["MP"],
                    "FailureFunction" : (lambda: DemotivateParty()),
                    "Penalties" : ["DP"],
                },
                "Smash the rock": {#+2 (1 * 2)
                    "Threshold": -2+ 14,
                    "Skill": "Pokémon Handling",
                    "SuccessMessage": "&0 commands &0m to shatter the stone, just to be on the safe side. It splits apart, revealing nothing but a couple of broken fragments of stone... and a seed that seemed to have been encased in the rock.",
                    "FailureMessage": "&0 commands &0m to shatter the stone, but the Pokémon refuses. Perhaps it does not wish to desecrate nature's beauty...",
                    "SuccessFunction" : (lambda: DungeonItem(1, mandate=["Hard Stone", "Miracle Seed"])),
                    "ExcludeFunction": ("Partner cannot learn Rock Smash!", (lambda: not HasRockBreaker()))
                },
                "Let Eevee explore it...": {# -1
                    "SuccessFunction" : (lambda: GetSquadLeaderRandomPokemon().Evolve(470)),
                    "ExcludeFunction": ("Partner is not an Eevee!", (lambda: GetSquadLeaderRandomPokemon().Id != 133))
                }
            }
        }
    }

    GenericEvents = list(DungeonEvents.keys())