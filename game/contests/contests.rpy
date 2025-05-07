label testcontest:

python:
    coordinators = [
        CoordinatorGroup([
            Coordinator(first_name, condition=0, isprotag=True)
        ]),
        CoordinatorGroup([
            Coordinator("Brendan", condition=30)
        ]),
        CoordinatorGroup([
            Coordinator("May", condition=15)
        ]),
        CoordinatorGroup([
            Coordinator("Jasmine", condition=5)
        ]),
        CoordinatorGroup([
            Coordinator("Dawn", condition=45)
        ])        
    ]

    judges = [
        Judge(wallace, biases={ ContestMoveType.Cute : 20, ContestMoveType.Beautiful : 30, ContestMoveType.Cool : 30, ContestMoveType.Clever : 10, ContestMoveType.Tough : 30 }),
        Judge(fantina, biases={ ContestMoveType.Cute : 10, ContestMoveType.Beautiful : 30, ContestMoveType.Cool : 30, ContestMoveType.Clever : 30, ContestMoveType.Tough : 20 }),
        Judge(phobos, biases={ ContestMoveType.Cute : 30, ContestMoveType.Beautiful : 30, ContestMoveType.Cool : 20, ContestMoveType.Clever : 30, ContestMoveType.Tough : 10 })
    ]

    contestconditions = {
        "Types" : ["Water", "Ghost", "Flying"],
        "Region" : range(252, 387),#Hoenn
        "Traits" : [ContestMoveType.Beautiful, ContestMoveType.Cool]
    }

call Contest("Test Contest", coordinators, judges, contestconditions) from _call_Contest

"reached here"

return

label Contest(contestname, coordinators, judges, contestconditions):

call clearscreens() from _call_clearscreens_233
scene blank
hide blank

python:
    InContest = True
    Turn = 1
    ContestConditions = contestconditions
    Judges = judges
    Coordinators = coordinators
    Coordinators = sorted(Coordinators, key=lambda coord: -coord.EvaluateCondition())
    ProtagCoordinator = None
    for coord in Coordinators:
        if (coord.IsProtag()):
            ProtagCoordinator = coord
            break

show screen ContestUI

#Animate the coordinators lining up like a boy band, then sending out their Pokémon

#iterate through the judges as each states what they're looking for in the following round

if (contestname == "Dorm 25 Central Suite Grand Open"):
    Character("Announcer") "\"The peasants are revolting, and they're not happy, either! Words and weapons won't work here! Only a stylish and cool Contest Performance can possibly soothe their aggravated hearts.\""

else:
    $ AddEvent("Professor Oak", "LearnedAboutContestColiseum")
    Character("Announcer") "\"It's a hot day in the Contest Coliseum! The judges look like they're in fine form, chatting and gossiping... the atmosphere is right for a showdown of coordinators!\""
    
Character("Announcer") "\"Let's see... what will the judges want to be seeing today?\""

python:
    for judge in judges:
        judge.SetSeeking()
        renpy.pause(0.3)

Character("Announcer") "\"Great! The judges are ready, and the crowd's raring to go! Let's see the performers!\""

python:
    renpy.show(Coordinators[0].GetImage(), at_list=[slideincontest(1/6)])
    renpy.say(Character("Announcer"), "\"In the first seed, it's [Coordinators[0].GetName()], performing with [Coordinators[0].GetFirstMonName()]! We all have high expectations for this one!\"")

    renpy.show(Coordinators[1].GetImage(), at_list=[slideincontest(2/6)])
    renpy.say(Character("Announcer"), "\"In the second seed, it's [Coordinators[1].GetName()], performing with [Coordinators[1].GetFirstMonName()]! Can the first seed be taken down?\"")

    pronouncalc = ("are they" if Coordinators[2].GetSex() == Genders.Unknown else ("is he" if Coordinators[2].GetSex() == Genders.Male else "is she"))
    renpy.show(Coordinators[2].GetImage(), at_list=[slideincontest(3/6)])
    renpy.say(Character("Announcer"), "\"In the third seed, it's [Coordinators[2].GetName()], performing with [Coordinators[2].GetFirstMonName()]! Beware the quiet ones! What tricks [pronouncalc] hiding?\"")

    renpy.show(Coordinators[3].GetImage(), at_list=[slideincontest(4/6)])
    renpy.say(Character("Announcer"), "\"In the fourth seed, it's [Coordinators[3].GetName()], performing with [Coordinators[3].GetFirstMonName()]! Quite a ways to climb--quite a bit to gain!\"")

    renpy.show(Coordinators[4].GetImage(), at_list=[slideincontest(5/6)])
    pronouncalc = ("these performers" if Coordinators[4].IsGroup() else "this performer")
    pronouncalc2 = ("them" if Coordinators[4].GetSex() == Genders.Unknown else ("him" if Coordinators[4].GetSex() == Genders.Male else "her"))
    renpy.say(Character("Announcer"), "\"In the final seed, it's [Coordinators[4].GetName()], performing with [Coordinators[4].GetFirstMonName()]! There's no doubt that [pronouncalc] has something to prove! Let's give [pronouncalc2] the chance!\"")

    for i, coord in enumerate(Coordinators):
        renpy.show(coord.GetImage(), at_list=[hidecontest((i + 1)/6)])

pause 1.0

Character("Announcer") "\"The performers are all ready! The lights are queued! The audience is on the edge of their seats... so, without any further ado, let's start the music!"

label ContestRound:

if (Turn == 11):
    jump ContestResults

elif (Turn > 1):
    python:
        for coord in Coordinators:
            coord.ResetCurrentPoints()
        announcer_dialog = {
            2: "Marvelous! Round two awaits--let the excitement continue!",
            3: "Splendid! We are now entering round three!",
            4: "How thrilling! Round four is upon us--let's dive in!",
            5: "Fantastic! It's time for round five to shine! As always, point values at the end of round five are doubled!",
            6: "Excellent! Let us embrace the challenge of round six!",
            7: "Remarkable! We move on to round seven--prepare yourselves!",
            8: "Incredible! Round eight begins--let the spectacle unfold!",
            9: "Fabulous! We now enter round nine--anticipation mounts!",
            10: "Superb! The grand finale of round ten is here--let's make it unforgettable! Remember, all point values at the end of round ten are tripled!"
        }

    # Display the correct announcement based on the current Turn
    Character("Announcer") "\"[announcer_dialog[Turn]]\""

python:
    PlannedMoves = []#has planned moves put in in-order. Elements are (coordinatorobj, moveeffect, moveused, predictedpoints)

    for i in range(len(Coordinators)):
        coord = Coordinators[i]
        coord.ResetCurrentPoints()
        if (not coord.IsProtag()):
            movevals = {}
            maxpointsearned = 0
            for move in coord.GetMoves():
                pointsearned = coord.CalculateMove(move)
                if (pointsearned > maxpointsearned):
                    maxpointsearned = pointsearned
                movename = move.Name
                movevals[move] = round(pointsearned)
                #print((movename, "Point value: " + str(pointsearned), "Safe: " + str(IsRoutineMove(move)), "Appeal bonus: " + str(appealstojudges), "Unappeal penalty: " + str(unappealstojudges), "Jackpot: " + str(jackpothit), "Effect: " +  GetMoveContestEffect(move)))
            moveselected = weighted_random_selection(movevals)
            #print(moveselected.Name + " was selected")
            PlannedMoves.append((coord, GetMoveContestEffect(moveselected), moveselected, maxpointsearned))
        else:
            renpy.say(None, "What will you do in the following round?")
            actiontype, movemon = renpy.call_screen("ContestChoices", coordinator=coord)
            PlannedMoves.append((coord, (GetMoveContestEffect(movemon) if contestaction == "Perform" else None), movemon, actiontype))

Character("Announcer") "\"The performers are ready to rock! Let's see the performances begin!"

python:
    for coord in Coordinators:
        coord.ResetCurrentPoints()

show screen ContestUIAbove with dis

python:
    DulledRound = False
    performancetypes = {}
    for i, plannedmove in enumerate(PlannedMoves):
        coord, effect, movemon, predictedpoints = plannedmove
        coord.ResetPriority()
        renpy.show(coord.GetImage("angrybrow"), at_list=[popupcontest((i + 1)/6)])
        if (isinstance(predictedpoints, str) and predictedpoints == "Switch"):
            coord.Reorder(movemon)
            coord.UnNoteReaction()
            renpy.say(Character("Announcer"), "\"What a twist! A contestant is switching out! You don't often see {i}that{/i} in contests! Points for audacity, at least! But maybe the crowd will like it...?\"")
            coord.AwardedPoints(3, None)
        elif (GetMoveContestEffect(movemon) == ContestEffects.Sneaky):
            if (i != 0):
                previouscoord = PlannedMoves[i - 1][0]
                renpy.show(coord.GetImage("angrybrow"))
                renpy.show(previouscoord.GetImage("angry"))
                coord.AwardedPoints(previouscoord.GetCurrentPoints(), None)
                renpy.say(Character("Announcer"), "\"How sneaky! [coord.GetName()] just stole [previouscoord.GetName()]'s spotlight! They might not stand out that way, but sometimes sharing is more than caring!\"")
            else:
                renpy.say(Character("Announcer"), "\"Oh? How embarrassing, folks! Looks like [coord.GetName()] tried to steal another Coordinator's spotlight--and failed!\"")
        
        else:
            repetitive = False
            if (RepeatedMove(coord, Turn, movemon)):
                repetitive = True
                isare = "is" if coord.IsSolo() else "are"
                renpy.say(Character("Announcer"), "\"Oh... it looks like [coord.GetName()] [isare] having [coord.GetFirstMonName()] use [movemon.Name] again... I'm not sure the judges will be excited to see that!\"")
            else:
                renpy.say(Character("Announcer"), "\"" + coord.GetPerformanceDialog(Turn) + "\"")

            totalpointsearned = 0

            for judge in Judges:
                pointsearned = 2
                if (repetitive):
                    pointsearned -= 1
                if (ContestStringToMacro(movemon.Contest) == judge.GetSeeking()):
                    pointsearned += 1
                    if (not DulledRound and not repetitive):
                        judge.IncreaseSparks()
                    if (judge.GetSparks() < judge.GetJackpotLimit()):
                        renpy.show(coord.GetImage("angrybrow"))
                    else:
                        pointsearned += 10
                        renpy.show(coord.GetImage("happy"))
                        renpy.say(None, "The performance went over incredibly well with [judge.GetName()]! [judge.GetHePronoun().title()]'s clapping and shouting! What a show!")
                        judge.ResetSparks()
                elif (IsUnappealing(judge.GetSeeking(), ContestStringToMacro(movemon.Contest))):
                    pointsearned -= 1
                    judge.DecreaseSparks()
                
                if (pointsearned != 0):
                    coord.AwardedPoints(pointsearned, judge)

            extrapoints = 0

            if (GetMoveContestEffect(movemon) == ContestEffects.Jamming):
                for otherplannedmove in PlannedMoves[:i]:
                    othercoord, othereffect, othermovemon, otherpredictedpoints = otherplannedmove
                    if (otherpredictedpoints != "Switch" and IsUnappealing(othermovemon.Contest, movemon)): 
                        if (GetMoveContestEffect(othermovemon) == ContestEffects.Unjammable):
                            renpy.say(Character("Announcer"), "\"Remarkable! Even in the face of a jamming [movemon.Name], [othercoord.GetName()] maintains [othercoord.GetHisPronoun()] routine! Such concentration!\"")
                        else:
                            renpy.say(Character("Announcer"), "\"Oh no! The jamming [movemon.Name] completely threw off [othercoord.GetName()]'s appeal! Can [othercoord.GetHePronoun()] recover from this?!\"")
                            othercoord.JamPoints()
            elif (GetMoveContestEffect(movemon) == ContestEffects.Unjammable):
                renpy.say(Character("Announcer"), "\"Look at [coord.GetName()] pull off that routine so flawlessly! There's something to be said for simple perfection, folks!\"")
            elif (GetMoveContestEffect(movemon) == ContestEffects.Dull and not DulledRound):
                DulledRound = True
                renpy.say(Character("Announcer"), "\"What's this?! Is it just me, or are the judges looking a bit listless? It might be hard to get them excited, now!\"")
            elif (GetMoveContestEffect(movemon) == ContestEffects.Showoff):
                renpy.say(Character("Announcer"), "\"What a flashy performance! I'd wager [coord.GetName()] will definitely be going to the first seed of the next round!\"")
                coord.SetPriority(i * 1000)
            elif (GetMoveContestEffect(movemon) == ContestEffects.Soothe):
                renpy.say(Character("Announcer"), "\"What's [coord.GetName()] hiding up their sleeve? If they're trying to grab the fifth seed of the next round, they've just done it!\"")
                coord.SetPriority(i * -1000)
            elif (GetMoveContestEffect(movemon) == ContestEffects.Finale and i == 4):
                renpy.show(coord.GetImage("angrybrow"))
                extrapoints += 3
                renpy.say(Character("Announcer"), "\"Wow! What an incredible way to wrap up the round, ladies and gentleman! [coord.GetName()]'s finale absolutely blew out the competition!\"")
            elif (GetMoveContestEffect(movemon) == ContestEffects.Spark and i == 0):
                renpy.show(coord.GetImage("angrybrow"))
                extrapoints += 3
                renpy.say(Character("Announcer"), "\"That's a {i}very{/i} strong start to the round, ladies and gentleman! [coord.GetName()]'s performance will be a tough act to follow!\"")

        if (coord.GetEnergy() == 1):
            extrapoints += 1
            renpy.say(Character("Announcer"), "\"[coord.GetName()] is showing great energy right now!\"")
        elif (coord.GetEnergy() == 2):
            extrapoints += 2
            renpy.say(Character("Announcer"), "\"[coord.GetName()] has seriously found [coord.GetHisPronoun()] flow! Look at that energy!\"")
        elif (coord.GetEnergy() == 3):
            extrapoints += 3
            renpy.say(Character("Announcer"), "\"[coord.GetName()] is absolutely bursting with energy! It's a runaway train, and we're all onboard!\"")

        if (not (isinstance(predictedpoints, str) and predictedpoints == "Switch")):
            if (movemon.Type in coord.GetMon().GetTypes(pureraw=True)):
                if (coord.GainEnergy()):
                    if (coord.IsProtag()):
                        renpy.show_screen("energyupleft", coord.GetName())
                    else:
                        renpy.show_screen("energyupright", coord.GetName())

                if (extrapoints > 0):
                    coord.AwardedPoints(extrapoints, None)

                if (coord.GetCurrentPoints() < 3):
                    renpy.show(coord.GetImage("sadbrow"))
                    renpy.say(None, "The judges don't seem impressed...")
                elif (coord.GetCurrentPoints() > 7 and coord.GetCurrentPoints() < 11):
                    renpy.show(coord.GetImage("happybrow"))
                    renpy.say(None, "The judges seem impressed!")
                elif (coord.GetCurrentPoints() > 10):
                    renpy.show(coord.GetImage("happy"))
                    renpy.say(None, "The judges are ecstatic!")

        renpy.show(coord.GetImage("-sadbrow -happy -angrybrow"), at_list=[hidecontest((i + 1)/6)])

    for plannedmove in PlannedMoves:
        coord, stance, movemon, predictedpoints = plannedmove
        suitability = EvaluateSuitability(coord.GetMon(), ContestConditions)

        if (coord.IsProtag()):
            if (coord.NotReactionNoted()):
                coord.NoteReaction()
                if (suitability == 1):
                    renpy.say(Character("Announcer"), "\"Oh? Listen to that crowd! It sounds like they like seeing [coord.GetName()]'s [coord.GetFirstMonSpeciesName()]!\"")
                elif (suitability == 2):
                    renpy.say(Character("Announcer"), "\"Wow! The crowd's really excited to see more of [coord.GetName()]'s [coord.GetFirstMonSpeciesName()]!\"")
                elif (suitability == 3):
                    renpy.say(Character("Announcer"), "\"Good golly! Listen to that roaring crowd! And everyone's cheering at the chance to see [coord.GetName()]'s [coord.GetFirstMonSpeciesName()]!\"")

        coord.RecordSuitability(Turn, suitability)

        if isinstance(predictedpoints, str):
            coord.RecordMove(Turn, None)
        else:
            coord.RecordMove(Turn, movemon.Name)

    if (Turn == 5):
        renpy.say(Character("Announcer"), "\"Did you forget? It's round five! And that means everyone's points get doubled! That'll matter at the end!\"")
        for plannedmove in PlannedMoves:
            coord, stance, movemon, predictedpoints = plannedmove
            coord.MultiplyCurrentPoints(2)
    if (Turn == 10):
        renpy.say(Character("Announcer"), "\"A remarkable finale, ladies and gentlemen! At the end of round ten, we {i}triple{/i} the contestants' points! Will this make the difference?!\"")
        for plannedmove in PlannedMoves:
            coord, stance, movemon, predictedpoints = plannedmove
            coord.MultiplyCurrentPoints(3)

    for plannedmove in PlannedMoves:
        coord, stance, movemon, predictedpoints = plannedmove
        coord.RecordRound(Turn, coord.GetCurrentPoints())
        
Character("Announcer") "\"The rankings are in for this round, folks! Let's see what the placings are, then...\""

python:
    positiondic = {}
    for i, coord in enumerate(Coordinators):
        positiondic[coord] = (i+1) / 6

    Coordinators = sorted(Coordinators, key=lambda x:x.GetCurrentPoints() + x.GetPriority(), reverse=True)

    for i, coord in enumerate(Coordinators):
        renpy.show(coord.GetImage(overridemood=11-5*i), at_list=[contestmovement(positiondic[coord], (i+1) / 6)])

pause 2.0

$ Turn += 1

jump ContestRound

label ContestResults:

hide screen ContestUIAbove with dis

Character("Announcer") "\"That's a wrap, everyone! The appeals are over! Nothing's left but the crying, now!\""

python:
    for i, coord in enumerate(Coordinators):
        coord.ResetCurrentPoints()
        renpy.transition(dis)
        renpy.hide(coord.GetImage())
        renpy.show(coord.GetImage("contest"), at_list=[contestmovement((i+1) / 6, (i+1) / 6)])

Character("Announcer") "\"The judges are deliberating...\""

Character("Announcer") "\"{w=0.5}.{w=0.5}.{w=0.5}.\""
Character("Announcer") "\"{w=0.5}.{w=0.5}.{w=0.5}.\""
Character("Announcer") "\"{w=0.5}.{w=0.5}.{w=0.5}.\""


Character("Announcer") "\"While we're waiting on them to reach a decision, let's check in with the audience! Points will be awarded based on how much the Coordinators' Pokémon resonated with the audience--let's find out!\""

show screen ContestUIAbove with dis

python:
    for coord in Coordinators:
        coord.CurrentPoints = coord.SumSuitability()

Character("Announcer") "\"Popular opinion isn't everything, but it sure helps! Let's reveal the results of the rounds, now!\""

Character("Announcer") "\"Round zero, the seeding round! The Coordinators and their Pokémon were evaluated on their physical condition!\""

python:
    highestval = 0
    for coord in Coordinators:
        conditionpoints = coord.GetPointsOnTurn(0)
        if (conditionpoints > highestval):
            highestval = conditionpoints
    
    for coord in Coordinators:
        coord.CurrentPoints += math.ceil(30 * (coord.GetPointsOnTurn(0) / highestval))

    for i in range(1, 11):
        renpy.say(Character("Announcer"), "\"Round [i]!\"")
        
        for coord in Coordinators:
            coord.CurrentPoints += coord.GetPointsOnTurn(i)


Character("Announcer") "\"And that's everything, ladies and gentlemen! As always, the Coordinator or Coordinators with the most points is the winner, and that means the winner can only be...!\""

$ InContest = False
    






                






#narrator states what the crowd's like right now, then says 'Round X begins! Make your move, and carve your glory into the hearts of all! How will you perform?!'

#pick whether you're going to perform or switch out

#if you pick perform
    # pick what sort of performance you want to make (audio/visual/props)

    # pick which move you want your pokemon to use (one/of/four/moves)

#if you pick switch out
    # pick which pokemon you're going to switch out to

#once your move is planned, it's put into the action queue.

#then the action queue is iterated through, and points are tallied and recorded
    #if a performer hits a jackpot, then the performer may get extra points
    #'jamming' effects also happen here 

#at the end of the turn, final point totals are tallied, and the order of the action queue is decided for the next turn. (Low-performers perform later. Performing later is a better position, as you can't be 'jammed', and know what roles previous actors are going to take.)
    #animate this, with characters acting happily if they 'moved up' in rank, and poorly if they 'moved down'

"reached pre-here"