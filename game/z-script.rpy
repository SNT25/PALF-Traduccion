# The game starts here.
label start:
$ _game_menu_screen = "game_menu"
$ yvalue = 1.0

jump prologue

# Show a background. This uses a placeholder by default, but you can
# add a file (named either "bg room.png" or "bg room.jpg") to the
# images directory to show it.

scene classroom

# This shows a character sprite. A placeholder is used, but you can
# replace it by adding a file named "eileen happy.png" to the images
# directory.

show red angry uniform

show mom angryeyes angryeyebrows sadmouth at leftside

show oak angrybrow happymouth at rightside

# These display lines of dialogue.

red "YOU LOST THE GAME"

label testdungeon:
    $ _rollback = False
    scene blank2
    python:
        trainer1 = MakeRed()
        trainer2 = MakeTrainer("Cheren", TrainerType.Ally)
        trainer3 = MakeTrainer("Skyla", TrainerType.Ally)
        trainer4 = MakeTrainer("Nessa", TrainerType.Ally)
        trainer5 = MakeTrainer("Raihan", TrainerType.Ally)
        fullsquad = [trainer1, trainer2, trainer3, trainer4, trainer5]

        wildpool = [pokedexlookupname("Budew", DexMacros.Id), pokedexlookupname("Turtwig", DexMacros.Id), pokedexlookupname("Phantump", DexMacros.Id)]

        squadleader = trainer1
        squadleadermon = GetSquadLeaderRandomPokemon()
        fullsquadminusleader = copy.copy(list(set(fullsquad) - set([squadleader])))
        randsquad = RandomChoice(fullsquadminusleader)
        dungeonlevel = 10
        genpokemon = RandomChoice(wildpool)
        wildpoolcopy = copy.copy(wildpool)
        genpokemons = [genpokemon] + [random.choice(wildpool) for x in range(4)]
        ugenpokemons = [genpokemon]
        wildpoolcopy.remove(genpokemon)
        for x in range(4):
            newmon = random.choice(wildpoolcopy)
            wildpoolcopy.remove(newmon)
            ugenpokemons.append(newmon)
            if (wildpoolcopy == []):
                wildpoolcopy = copy.copy(wildpool)

        activedungeon = Dungeon("forest", "Windswept Woods", fullsquad, wildpool, "toweringarborage", "forestdungeonloss", 9, AimLevel() + 1, 
            dungeoncutscenefunc=None, 
            fudgerollfunc=None, 
            eventfunc=None,
            generateitems=[(20, "Gimmighoul Coin"), (10, "Chesto Berry"), (10, "Oran Berry"), (9, "Sitrus Berry"), (5, "Sharp Beak"), (5, "Miracle Seed")])


    jump StartDungeon

label StartDungeon:

if (activedungeon == None):
    jump errorlabel

python:
    location = activedungeon.Name.lower()
    _rollback = False
    squadleader = activedungeon.Party[0]
    squadleadermon = GetSquadLeaderRandomPokemon()
    fullsquadminusleader = copy.copy(list(set(fullsquad) - set([squadleader])))
    randsquad = RandomChoice(fullsquadminusleader)
    genpokemon = RandomChoice(wildpool)
    wildpoolcopy = copy.copy(wildpool)
    genpokemons = [genpokemon] + [random.choice(wildpool) for x in range(4)]
    ugenpokemons = [genpokemon]
    wildpoolcopy.remove(genpokemon)
    dungeonlevel = activedungeon.DungeonLevel
    for x in range(4):
        newmon = random.choice(wildpoolcopy)
        wildpoolcopy.remove(newmon)
        ugenpokemons.append(newmon)
        if (wildpoolcopy == []):
            wildpoolcopy = copy.copy(wildpool)
    instantcutscene = False
    seenscenes = []
    if (activedungeon.DungeonCutsceneFunc):
        instantcutscene = activedungeon.DungeonCutsceneFunc(activedungeon)

if (not instantcutscene):
    scene blank2
    hide blank2
    call clearscreens() from _call_clearscreens_223
    show screen DungeonBackground
    show screen DungeonUI
    with pixellate

else:
    scene blank2
    hide blank2
    call clearscreens() from _call_clearscreens_224
    show screen DungeonBackground
    with pixellate

label postdungeonscreen:

python:
    event = activedungeon.GenerateEvent()
    alreadydisplayed = False
    afterevent = False
    if (ReturnEventTag("RegenCriteria") != None):
        genpokemon = RegenWithPriority(ReturnEventTag("RegenCriteria"))
    else:
        genpokemon = RandomChoice(wildpool)
    cutscene = False
    if (activedungeon.DungeonCutsceneFunc):
        cutscene = activedungeon.DungeonCutsceneFunc(activedungeon)
    if (cutscene):
        activedungeon.ShownScenes.append(cutscene)
        renpy.call(cutscene)

label beforeintrotext:

if (ReturnEventTag("IntroText") != None):
    $ renpy.say(dungeonnarrator, DisplayDungeonText(ReturnEventTag("IntroText") + ("{fast}" if alreadydisplayed else "")), interact=False)

label beforedungeonoptions:

python:
    options = GetOptionsForMenu(event)
    result = renpy.call_screen("dungeonchoice", options, not alreadydisplayed)
    renpy.sound.stop(channel="bipbop")
    alreadydisplayed = True
    if (isinstance(result, str)):
        renpy.show_screen("dungeonchoice", options, False)
        DungeonSay(result)
        renpy.jump("beforeintrotext")
    elif (isinstance(result, bool)):
        renpy.hide_screen("diceroll")
        renpy.hide_screen("enddiceroll")
        DungeonSay("You head off in a different direction, but are ambushed on the way! [bluecolor](You can gain no morale or progress from this battle.){/color}")
        genpokemon = RandomChoice(wildpool)
        DungeonFight(lastbattler = False)
        if (squadleader.GetTeam()[0].Health == 0):
            squadleader.GetTeam()[0].Health = 1
            DemotivateSquadder(change=-5)
        leadername = squadleader.Name
        if (leadername == "red"):
            leadersex = Genders.Male
        else:
            leadersex = persondex[squadleader.GetFormatName()]["Sex"]
        squadleaderpronoun = "him" if leadersex == Genders.Male else "her"
        squadleadername = squadleader.GetFormatName()
        DungeonSay("[squadleadername]'s loss afflicted [squadleaderpronoun] with melancholy...")
        squadleadermon.Health = max(1, squadleadermon.Health)
        renpy.jump("postdungeonscreen")

    option = result[1]
    success, threshold, randnum, bonus = EvaluateEvent(result)

    if (event in GenericEvents):
        outcomekey = (event, option)
        if (outcomekey not in outcomedex.keys()):
            outcomedex[outcomekey] = {"Rewards" : None, "Penalties" : None}
        if (outcomekey in outcomedex):
            if (success):
                outcomedex[outcomekey]["Rewards"] = ReturnOptionTag(option, "Rewards")
            else:
                outcomedex[outcomekey]["Penalties"] = ReturnOptionTag(option, "Penalties")

    afterevent = True

if (threshold > 0):
    if (not renpy.get_skipping()):
        show screen diceroll(success, threshold, randnum, bonus)

        pause 5.0
    else:
        $ dicematrix = SaturationMatrix(1.2) * TintMatrix(GetCharColor(squadleader.GetFormatName()))
        show screen enddiceroll(success, threshold, randnum + bonus, dicematrix)

    if (randnum == 20):
        $ DungeonSay("A {gradient2=3-#f00-#0f0-11-#0f0-#00f-11-#00f-#f00-11}{font=fonts/AncientModernTales.ttf}critical{/font}{/gradient2} success!")

    elif (randnum == 1):
        $ DungeonSay("A {color=#f00}critical{/color} fumble...")

#else:
#    $ renpy.show_screen("dungeonchoice", options, False)

if (ReturnOptionTag(option, "BattleFunction") != None):
    $ ReturnOptionTag(option, "BattleFunction")()
    $ success = _return

if (success):
    if (ReturnOptionTag(option, "SuccessMessage") != None):
        $ DungeonSay(ReturnOptionTag(option, "SuccessMessage"))

    if (ReturnOptionTag(option, "SuccessFunction") != None):
        $ ReturnOptionTag(option, "SuccessFunction")()

else:
    if (ReturnOptionTag(option, "FailureMessage") != None):
        $ DungeonSay(DisplayDungeonText(ReturnOptionTag(option, "FailureMessage"))) 

    if (ReturnOptionTag(option, "FailureFunction") != None):
        $ ReturnOptionTag(option, "FailureFunction")()

$ renpy.transition(dungeondis)
$ activedungeon.CreateMapDict()
hide screen dungeonchoice with dis

$ lastfoe = activedungeon.GetLastBattledFoe()
$ lastround = activedungeon.GetLastBattledRound()
if (lastfoe != None and lastround == activedungeon.GetProgress()):
    python:
        leadername = squadleader.Name
        if (leadername == "red"):
            leadersex = Genders.Male
        else:
            leadersex = persondex[squadleader.GetFormatName()]["Sex"]
        squadleaderpronoun = "him" if leadersex == Genders.Male else "her"
        squadleadername = squadleader.GetFormatName()
    if (activedungeon.WonlastFight()):
        $ MotivateSquadder(change=3)
        $ DungeonSay("[squadleadername]'s victory spurs [squadleaderpronoun] onward!")
    elif (squadleader.GetTeam()[0].Health == 0):
        python:
            squadleader.GetTeam()[0].Health = 1
            DemotivateSquadder(change=-5)
            DungeonSay("[squadleadername]'s loss afflicted [squadleaderpronoun] with melancholy...")

$ DungeonProg()

if (ReturnEventTag("PostText") != None):
    $ DungeonSay(DisplayDungeonText(ReturnEventTag("PostText")))

if (activedungeon.GetProgress() < activedungeon.GetMaxProgress()):
    jump postdungeonscreen

call cleardungeonscreens() from _call_cleardungeonscreens_5

scene blank2 with Dissolve(3.0)

python: 
    maxmorale = activedungeon.MaxMorale()
    totalmorale = max(1, activedungeon.TallyMorale())
    numstars = math.ceil(totalmorale / maxmorale * 5)
    if (numstars == 5):
        DungeonSay("The party, ecstatic, leaves the dungeon with arms overflowing with goodies! Their bonds have been greatly strengthened! Their wallets bulge with Gimmighoul coins!")
    elif (numstars == 4):
        DungeonSay("The party cheers and whoops as they leave the dungeon, crowing over their victories. All party members' bonds have increased, and the victorious heroes return home with items and Gimmighoul Coins aplenty!")
    elif (numstars == 3):
        DungeonSay("The party emerges from the dungeon, tired but satisfied. High-fives are shared all around! With packs full of items and wallets thick with Gimmighoul Coins, this excursion can easily be considered a success.")
    elif (numstars == 2):
        DungeonSay("The party, thoroughly spent, emerges from the dungeon. Though wobbly on their feet, their packages contain a decent number of treasures, and their bonds have grown stronger through hardship...")
    elif (numstars == 1):
        DungeonSay("The party trods out of the dungeon, battered but standing. The members can manage, at most, a couple grimaces at each other.")

python:
    DungeonItem(numitems=max(1, numstars), mandate=["Gimmighoul Coin"])

    for i, member in enumerate(activedungeon.Party):
        if (member.Type == TrainerType.Ally):
            membername = member.GetFormatName()

            if (GetNature(membername) != TrainerNature.Special):
                ValueChange(membername, numstars, ((i + 1) / (len(activedungeon.Party) + 1)), False)

    DungeonSay("All party members' bonds increased!")

    if (numstars > 1 and not isgame):
        DungeonItem(numitems=numstars, exclude=["Gimmighoul Coin"])

call screen dungeontally with dis

pause 2.0

python:
    dungeonhistory.append((activedungeon.Name, activedungeon.TallyMorale(), activedungeon.MaxMorale(), activedungeon.ItemHistory, activedungeon.BattleHistory))
    isgame = False
    activedungeon.DungeonWon = True
    activedungeon.DungeonLost = False
    _rollback = True
    renpy.block_rollback()
    renpy.suspend_rollback(False)
    renpy.jump(activedungeon.WinLabel)

return


label testbattle:
$ newparty = [Pokemon(25.2, level=50, moves=[GetMove("Frost Breath"), GetMove("Power-Up Punch"), GetMove("Bullet Seed"), GetMove("No Retreat")], foreverals=["Absol Megaveral"]), 
    Pokemon("Ralts", level=1, moves=[GetMove("Confusion"), GetMove("Karate Chop"), GetMove("Splinter Shield"), GetMove("Ingrain")], foreverals=["Meditite Everal"]),
    Pokemon("Dreepy", nickname="Mimikyu", moves=[GetMove("Confusion"), GetMove("Karate Chop"), GetMove("Shadow Sneak"), GetMove("Round")], foreverals=["Meditite Everal"]),
    Pokemon(774, nickname="Minior3", moves=[GetMove("Teleport"), GetMove("Leech Seed"), GetMove("Uproar"), GetMove("Mist")]),
    Pokemon(568, level=3, gender=Genders.Female, moves=[GetMove("Pound"), GetMove("Poison Gas")], ability="Aftermath")]

$ trainer1 = Trainer("red", TrainerType.Player, newparty, number=3)
$ trainer2 = Trainer("blue", TrainerType.Enemy, [
    Pokemon(pokedexlookupname("Tyrunt", DexMacros.Id), moves=[GetMove("Shed Tail")], ability="Mold Breaker", level=100, intelligence = 1),
    Pokemon("Ralts", level=1, moves=[GetMove("Confusion"), GetMove("Karate Chop"), GetMove("Splinter Shield"), GetMove("Ingrain")], foreverals=["Meditite Everal"])])

call Battle([trainer1, trainer2], currentWeather=("sunny", 3)) from _call_Battle_11

red @talkingmouth "End of battle."

# This ends the game.

return

label randombattle:

if (not persistent.testwarning):
    narrator "This testing feature may contain massive spoilers for game content, including characters and Pokémon. Are you sure you want to use it?"

    menu:
        "Yes, and don't warn me again.":
            $ persistent.testwarning = True
            pass

        "Never mind.":
            return

show stadium_empty

show screen abortbattletester

python:
    testbattle = True
    random.seed()
    numallies = random.randint(1, 3)
    numfoes = random.randint(1, 3)
    allynums = (1 if numallies != 1 else random.randint(1, 3))
    foenums = (1 if numfoes != 1 else random.randint(1, 3))
    trainers = []

    for i in range(numallies):
        teamnumber = random.randint(1, 6)
        newteam = []
        for i in range(teamnumber):
            newteam.append(Pokemon(random.choice(GetAllPokemonIn()), level = random.choice(range(5, 15))))
        random.seed()
        newtrainer = Trainer(random.choice(list(classdex.keys())).lower(), (TrainerType.Player if len(trainers) == 0 else TrainerType.Ally), newteam, allynums)
        trainers.append(newtrainer)

    for i in range(numfoes):
        teamnumber = random.randint(1, 6)
        newteam = []
        for i in range(teamnumber):
            newteam.append(Pokemon(random.choice(GetAllPokemonIn()), level = random.choice(range(5, 15))))
        random.seed()
        newtrainer = Trainer(random.choice(list(classdex.keys())).lower(), TrainerType.Enemy, newteam, foenums)
        trainers.append(newtrainer)

call Battle(trainers, gainexp=False) from _call_Battle_42

$ testbattle = False

red @talkingmouth "End of battle."

return
