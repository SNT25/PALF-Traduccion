label clearcontestscreens:
hide screen ContestUI
hide screen ContestUIAbove
hide screen ContestMonData
hide screen ContestChoices
with dis
return

screen ContestUI():
    layer "undermaster"

    for i, judge in enumerate(Judges):
        python:
            yadjust = 0.1 * (1 - (i % 2))
            xadjust = 0.3 + i * 0.2

        add judge.GetImage() ypos 0.35 + yadjust zoom 0.3 xcenter xadjust

        if (judge.GetSeeking() == ContestMoveType.Cool): 
            add "gui/contest/coolrequest.png" xcenter xadjust ypos yadjust
        elif (judge.GetSeeking() == ContestMoveType.Cute):
            add "gui/contest/cuterequest.png" xcenter xadjust ypos yadjust
        elif (judge.GetSeeking() == ContestMoveType.Clever): 
            add "gui/contest/cleverrequest.png" xcenter xadjust ypos yadjust
        elif (judge.GetSeeking() == ContestMoveType.Beautiful):
            add "gui/contest/beautifulrequest.png" xcenter xadjust ypos yadjust
        elif (judge.GetSeeking() == ContestMoveType.Tough):
            add "gui/contest/toughrequest.png" xcenter xadjust ypos yadjust

        text "★" * judge.GetSparks() + "☆" * (judge.GetJackpotLimit() - judge.GetSparks()) font "fonts/DejaVuSans.ttf" xcenter xadjust ycenter 0.3 size 70 color "#fff" outlines [ (absolute(5), "#000", absolute(0), absolute(0)) ]

    add "#676767" ypos 0.35

    add "gui/contest/hint.png" xalign 1.0 yalign 0.0

screen ContestUIAbove():
    for i, coord in enumerate(Coordinators):
        vbox:
            xcenter ((i + 1) / 6) 
            yalign 1.0
            text "★" * coord.GetEnergy() + "☆" * (3 - coord.GetEnergy()) font "fonts/DejaVuSans.ttf" xalign 0.5 size 70 color "#fff" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
            text str(coord.GetCurrentPoints()) + " Pts" xalign 0.5 size 70 color "#fff" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

screen ContestMonData(mon):
    frame:
        xalign 0.5
        background Frame("gui/button/choice_idle_background.webp", 6, 6)
        vbox:
            text mon.GetNickname() xalign 0.5 size 60
            hbox:
                for move in mon.GetMoves():
                    textbutton (move.Name if contestmove != move else "[[" + move.Name + "]") action SetVariable("contestmove", move) text_font "fonts/pkmndp.ttf" xmaximum 370 text_xalign .5 text_size 60 text_color GetDimContestTypeColor(move.Contest) text_hover_color GetContestTypeColor(move.Contest) style "menu_choice_button" hovered Show("movedata", None, move) unhovered Hide("movedata")
            textbutton "Close" action Hide("ContestMonData") text_color "#000" text_hover_color "#f0f" xalign 0.5

screen energyupleft(coordname):
    zorder 100
    add "GUI/double-arrow.webp" yalign 0.5 at swipeinleft, Transform(yzoom = 0.3, xzoom=-0.3)
    text "{size=60}" + coordname + "'s{/size}\nenergy increased!" color "#fff" yalign 0.5 size 80 outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] at swipeinleft
    timer 2.0 action Hide("energyupleft")

screen energyupright(coordname):
    zorder 100
    add "GUI/double-arrow.webp" yalign 0.5 xalign 1.0 at swipeinright, Transform(zoom = 0.3)
    text"{size=60}" + coordname + "'s{/size}\nenergy increased!" color "#fff" yalign 0.5 size 80 xalign 1.0 outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] at swipeinright
    timer 2.0 action Hide("energyupright")

screen ContestChoices(coordinator):
    $ currentMon = coord.GetMon()

    #$ showteraoption = False
    #if (currentMon != None and Item.TeraOrb in inventory.keys()):
    #    $ showteraoption = True
    #    for allymon in currentMon.GetTrainer().GetTeam():
    #        if (allymon.IsTerad() and (allymon != currentMon or allymon == currentMon and allymon.GetTerastallized() != Turn)):
    #            $ showteraoption = False

    #$ hasdiveral = False
    #if (currentMon != None):
    #    for fvl in currentMon.GetForeverals():
    #        if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.FormSwap):
    #            $ hasdiveral = True

    vbox:
        xalign .5
        yalign .5
        textbutton "          Step 1: Decide whether your Pokémon will perform or switch!           " text_color "#FF69B4" background Frame("gui/button/choice_idle_background.webp") xalign 0.5
        hbox:
            xalign 0.5
            textbutton (" Perform " if contestaction != "Perform" else "[[Perform]") action [Hide("ContestMonData"), SetVariable("contestaction", "Perform"), SetVariable("contestmon", None)] xalign 0.5 text_font "fonts/pkmndp.ttf" xmaximum 270 text_xalign .5 text_size 60 text_color "#9b5151" text_hover_color "#d03b3d" style "menu_choice_button"
            textbutton (" Switch " if contestaction != "Switch" else "[[Switch]") action [SetVariable("contestaction", "Switch"), SetVariable("contestmove", None)] xalign 0.5 text_font "fonts/pkmndp.ttf" xmaximum 270 text_xalign .5 text_size 60 text_color "#437128" text_hover_color "#459426" style "menu_choice_button"
        if (contestaction != None):
            if (contestaction == "Perform"):
                textbutton "         Step 2: Pick the move your Pokémon will use!       " text_color "#FF69B4" background Frame("gui/button/choice_idle_background.webp") xalign 0.5
                hbox:
                    for move in currentMon.GetMoves():
                        textbutton (move.Name if contestmove != move else "[[" + move.Name + "]") action SetVariable("contestmove", move) text_font "fonts/pkmndp.ttf" xmaximum 370 text_xalign .5 text_size 60 text_color GetDimContestTypeColor(move.Contest) text_hover_color GetContestTypeColor(move.Contest) style "menu_choice_button" hovered Show("movedata", None, move) unhovered Hide("movedata")
            elif (contestaction == "Switch"):
                textbutton "       Step 2: Pick the Pokémon you'll send out!       " text_color "#FF69B4" background Frame("gui/button/choice_idle_background.webp") xalign 0.5
                hbox:    
                    for mon in coordinator.GetTeam():
                        textbutton (mon.GetNickname() if contestmon != mon else "[[" + mon.GetNickname() + "]") action SetVariable("contestmon", mon) text_font "fonts/pkmndp.ttf" xmaximum 270 text_xalign .5 text_size 40 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" hovered Show("ContestMonData", None, mon)
            if (contestaction == "Perform" and contestmove != None):
                textbutton "      Step 3: Lock it in!      " text_color "#FF69B4" background Frame("gui/button/choice_idle_background.webp") xalign 0.5
                textbutton "{gradient2=3-#f00-#0f0-11-#0f0-#00f-11-#00f-#f00-11}{size=75}Perform!{/size}{/gradient2}" action [Hide("ContestMonData"), Return((1, contestmove))] xalign 0.5 text_font "fonts/pkmndp.ttf" xmaximum 370 text_xalign .5 top_padding 17 style "menu_choice_button"
            elif (contestaction == "Switch" and contestmon != None):
                textbutton "      Step 3: Lock it in!      " text_color "#FF69B4" background Frame("gui/button/choice_idle_background.webp") xalign 0.5
                textbutton "{gradient2=3-#f00-#0f0-11-#0f0-#00f-11-#00f-#f00-11}Switch!{/gradient2}" action [Hide("ContestMonData"), Return(("Switch", contestmon))] xalign 0.5 text_font "fonts/pkmndp.ttf" xmaximum 360 text_xalign .5 text_size 60 style "menu_choice_button"

screen ContestHelp():
    modal True

    vbox:
        align (0.5, 0.5)
        textbutton "Back to the show!" action Hide("ContestHelp") padding (30, 10) xminimum 200 text_xalign .5 xalign 0.5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" 
        frame:
            # pokémon list
            background "pokedex_background"
            xsize 1500
            ysize 700
            padding (20, 20)

            viewport id "contesthelpport":
                draggable True
                scrollbars "vertical"

                vbox:
                    spacing 50
                    $ beautiful = "{color=" + GetContestTypeColor("Beautiful") + "}Beautiful" + "{/color}"
                    $ cute = "{color=" + GetContestTypeColor("Cute") + "}Cute" + "{/color}"
                    $ tough = "{color=" + GetContestTypeColor("Tough") + "}Tough" + "{/color}"
                    $ clever = "{color=" + GetContestTypeColor("Clever") + "}Clever" + "{/color}"
                    $ cool = "{color=" + GetContestTypeColor("Cool") + "}Cool" + "{/color}"
                    text "{b}Condition{/b}: At the beginning of each Contest, the Coordinator-Pokémon pair that is in the best visual condition will earn 20 points, with runners-up winning linearly fewer. This is tied to [contestcolor]Coordinating Knowledge.{/color}" color "#000"
                    text "{b}Popularity{/b}: Every turn, a Coordinator-Pokémon pair can earn up to three points depending on how popular their species of Pokémon is. This popularity is based on whether the Pokémon has one of three types, whether the Pokémon is from a specific region, and whether the Pokémon has a certain Contest Trait. ([pika_name] will always be considered an Electric-type from Unova, with the [cool] contest type.)" color "#000"
                    text "{b}Contest Move Types{/b}: The five kinds of Contest Move Types are [cute], [clever], [cool], [beautiful], and [tough]. Every move falls into one of these categories." color "#000"
                    text "{b}Appealing Moves{/b}: If you use a move with a Contest Move Type a Judge wants to see, they will award you an extra point, and they will become more excited." color "#000"
                    text "{b}Unappealing Moves{/b}: If you use a move with a Contest Move Type very different from what a Judge wants to see, they will subtract one point from your evaluation, and become less excited. [cute] is opposite [cool]. [cool] is opposite [clever]. [clever] is opposite [beautiful]. [beautiful] is opposite [tough]. [tough] is opposite [cute]." color "#000"
                    text "{b}Jackpots{/b}: If a move makes a Judge as excited as they can possibly be, they will award the user of the move a bonus 13 points! They will then start looking for something else--and be permanently easier to excite." color "#000"
                    text "{b}Energy{/b}: Using a move that is the same type as the Coordinator performing grants a Coordinator 'Energy'. Every point of Energy a Coordinator has increases the value of their appeals." color "#000"
                    text "{b}Jamming Moves{/b}: Some moves are capable of 'jamming' a competitor who moved prior. If jammed, they will lose a third of their points (min 1), and lose all their energy." color "#000"
                    text "{b}Special Rounds{/b}: On round five, after all points are tallied up, including points from energy and jamming, your score for the round is doubled. On round ten, your score for the round is tripled. Make sure to make those rounds count!" color "#000"
