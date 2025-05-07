init python:
    def ChangeLeaderRegenText(newleader):
        global squadleader
        global randsquad
        global alreadydisplayed
        if (not afterevent):
            squadleader = newleader
            squadleadermon = GetSquadLeaderRandomPokemon()
            fullsquadminusleader = copy.copy(list(set(fullsquad) - set([squadleader])))
            randsquad = RandomChoice(fullsquadminusleader)
            alreadydisplayed = True
            renpy.jump("beforeintrotext")

    def GetSquadderPosition(squadder):
        index = fullsquad.index(squadder)
        xpos = (index % 3) * 0.17 + 0.47
        ypos = (math.floor(index / 3)) * 0.25 + 0.175
        return (xpos, ypos)

screen showtooltip(squadder):
    python:
        position = GetSquadderPosition(squadder)
        squadname = squadder.GetFormatName()

        if (not afterevent):
            if (squadder != squadleader):
                displaytext = "Left-Click: Make leader.\nRight-Click: View sheet."
            else:
                displaytext = "Current Leader\nRight-Click: View sheet."

        else:
            if (squadder != squadleader):
                displaytext = "Right-Click: View sheet."
            else:
                displaytext = "Current Leader\nRight-Click: View sheet."

    add "gui/longpaperframe.png" pos (position[0] - 0.1, position[1] - 0.1)    
    text displaytext pos (position[0] + 0.025 - 0.1, position[1] - 0.1 + 0.019) font "fonts/DungeonFont.ttf"

screen DungeonUI():
    layer "undersayer"
    zorder -6
    python:
        prog = float(activedungeon.GetProgress())
        maxprog = float(activedungeon.GetMaxProgress())
        squadsize = len(fullsquad)
        matrix = TintMatrix(GetCharColor(squadleader.GetFormatName())) * BrightnessMatrix(1.0) * ContrastMatrix(0.0)
        #squadleader = already defined
        #fullsquad = already defined

    for i, squadder in enumerate(fullsquad):
        python:
            chibi = Transform(GetChibi(squadder.GetFormatName()), align=(0.5, 0.5))
            squadder = fullsquad[i]
            position = GetSquadderPosition(squadder)
            chibutton = Transform(Composite((600, 600),
                (25, 25), ((Null() if squadder != squadleader else Transform(chibi, matrixcolor=matrix, zoom=1.1))),
                (50, 50), chibi), zoom=0.25)

        if (squadder == squadleader):
            add "gui/PaperFrame.png" pos (position[0], position[1] + 0.115) xalign 0.5 zoom 1.1 matrixcolor matrix  
        imagebutton idle chibutton pos position xalign 0.5 action [Function(ChangeLeaderRegenText, squadder) if not afterevent else NullAction()] hovered Show("showtooltip", None, squadder) unhovered Hide("showtooltip") alternate Show("CharacterSheet", Dissolve(0.2), squadder)
        imagebutton idle "gui/PaperFrame.png" pos (position[0], position[1] + 0.12) xalign 0.5 action [Function(ChangeLeaderRegenText, squadder) if not afterevent else NullAction()] hovered Show("showtooltip", None, squadder) unhovered Hide("showtooltip") alternate Show("CharacterSheet", Dissolve(0.2), squadder)
        vbox:
            pos (position[0], position[1] + 0.125)
            xalign 0.5
            text squadder.GetFormatName() font "fonts/DungeonFont.ttf" xalign 0.5
            text "★" * squadder.GetMotivation() + "☆" * min(5, (5 - squadder.GetMotivation())) font "fonts/DejaVuSans.ttf" xalign 0.5 size 25

    hbox:
        pos (0.45, 0.7)
        for i in range(12):
            if (i / 12 < prog / maxprog):
                imagebutton idle "gui/gem.png" action NullAction() hovered Show("progresscount") unhovered Hide("progresscount")
            else:
                imagebutton idle "gui/gemunlit.png" action NullAction() hovered Show("progresscount") unhovered Hide("progresscount")

screen DungeonBackground():
    layer "undermaster"
    zorder 20
    for position, value in activedungeon.GetMapDict().items():
        $ x = math.floor(position[0] * 96 - 1)
        $ y = math.floor(position[1] * 96 - 1)
        add value nearest True pos (x, y)
    
    #add "bg/blank2.webp" alpha 0.6

screen progresscount():
    python:
        floorsleft = activedungeon.GetMaxProgress() - activedungeon.GetProgress()
    add "gui/longpaperframe.png" pos (0.45, 0.63) zoom 0.7
    text str(floorsleft) + " floor" + ("s" if floorsleft != 1 else "") + " left!" pos (0.48, 0.65) font "fonts/DungeonFont.ttf"

init python:
    def chance_of_exceeding_threshold(bonus, threshold):
        guaranteed_success_chance = 5
        guaranteed_failure_chance = 5
        regular_chance = 90
        
        successful_outcomes = 0
        total_outcomes = 20
        
        for random in range(1, 21):  # random ranges from 1 to 20 inclusive
            if bonus + random > threshold:
                successful_outcomes += 1
        
        # Calculate the percentage of regular successful outcomes
        regular_success_percentage = (successful_outcomes / total_outcomes) * regular_chance
        
        # Add the guaranteed success and failure chances
        total_percentage_chance = regular_success_percentage + guaranteed_success_chance
        
        return total_percentage_chance

screen bonuspreview(skill, threshold):
    layer "undersayer"
    zorder -5
    for i, squadder in enumerate(fullsquad):
        python:
            position = GetSquadderPosition(squadder)
            bonus = GetSkill(squadder, skill, total=True)
            color = "#404040"
            if (bonus == 2):
                color = "#003d07"
            elif (bonus == 3):
                color = "#006158"
            elif (bonus == 4):
                color = "#002a95"
            elif (bonus == 5):
                color = "#bd00c1"
            elif (bonus == 6):
                color = "#e9da00"
            elif (bonus == 7):
                color = "#e90000"
            elif (bonus == 8):
                color = "#ffc800"

            percentage = math.floor(chance_of_exceeding_threshold(bonus, threshold))
        
        text "+" + str(bonus) + " (" + str(percentage) + "%)" pos (position[0], position[1] + 0.19) xalign 0.5 font "fonts/DungeonFont.ttf" color color

default dotposx = 0
default dotposy = 0

screen CharacterSheet(squadder):
    modal True

    imagebutton idle Null() xysize (1920, 1080) action [Hide("CharacterSheet", Dissolve(0.2)), Hide("mondata")]

    add "BG/Blank2.webp" alpha 0.6

    add "scrollunfurl" align (0.5, 0.5) zoom 1.0/0.9

    add "gui/ScrollOverlay.png" align (0.5, 0.5) at scrollfadein

    text squadder.GetFormatName() align (0.5, 0.5) pos (848, 420) font "fonts/DungeonFont.ttf" at scrollfadein
    text GetClass(squadder) align (0.5, 0.5) pos (1088, 420) font "fonts/DungeonFont.ttf" at scrollfadein

    text str(GetSquadStat(squadder, "Wit")) pos (1146, 486) anchor (0.5, 0.5) font "fonts/DungeonFont.ttf" at scrollfadein
    text str(GetSquadStat(squadder, "Knowledge")) pos (1146, 526) anchor (0.5, 0.5) font "fonts/DungeonFont.ttf" at scrollfadein
    text str(GetSquadStat(squadder, "Courage")) pos (1146, 566) anchor (0.5, 0.5) font "fonts/DungeonFont.ttf" at scrollfadein
    text str(GetSquadStat(squadder, "Charm")) pos (1146, 606) anchor (0.5, 0.5) font "fonts/DungeonFont.ttf" at scrollfadein
    text str(GetSquadStat(squadder, "Patience")) pos (1146, 646) anchor (0.5, 0.5) font "fonts/DungeonFont.ttf" at scrollfadein

    for i in range(GetSquadStat(squadder, "Wit")):
        add "gui/ScrollOverlayDot.png" pos (978 + 32 * i, 486) anchor (0.5, 0.5) at scrollfadein
    for i in range(GetSquadStat(squadder, "Knowledge")):
        add "gui/ScrollOverlayDot.png" pos (978 + 32 * i, 526) anchor (0.5, 0.5) at scrollfadein
    for i in range(GetSquadStat(squadder, "Courage")):
        add "gui/ScrollOverlayDot.png" pos (978 + 32 * i, 566) anchor (0.5, 0.5) at scrollfadein
    for i in range(GetSquadStat(squadder, "Charm")):
        add "gui/ScrollOverlayDot.png" pos (978 + 32 * i, 606) anchor (0.5, 0.5) at scrollfadein
    for i in range(GetSquadStat(squadder, "Patience")):
        add "gui/ScrollOverlayDot.png" pos (978 + 32 * i, 646) anchor (0.5, 0.5) at scrollfadein

    add GetSprite(squadder) pos (1108, 281) anchor (0.5, 0.5) zoom 1.6 matrixcolor SaturationMatrix(0.0) at scrollfadein

    text squadder.GetSkills()[0].replace("é", "{font=fonts/AncientModernTales.ttf}é{/font}") pos (730, 736) anchor (0.5, 0.5) font "fonts/DungeonFont.ttf" at scrollfadein
    text squadder.GetSkills()[1].replace("é", "{font=fonts/AncientModernTales.ttf}é{/font}") pos (960, 736) anchor (0.5, 0.5) font "fonts/DungeonFont.ttf" at scrollfadein
    text squadder.GetSkills()[2].replace("é", "{font=fonts/AncientModernTales.ttf}é{/font}") pos (1190, 736) anchor (0.5, 0.5) font "fonts/DungeonFont.ttf" at scrollfadein

    $ mon = squadder.GetTeam()[0]
    imagebutton idle Transform(mon.GetImage(), zoom=0.2, matrixcolor=(ContrastMatrix(1.0) if mon.GetHealthPercentage() > 0 else ContrastMatrix(0.0))) action NullAction() pos (733 + 3 * 95 - 43, 839 - (43 if mon.Id != 25.2 else 58)) hovered [Show("mondata", None, mon, False), Show("nonbattlemoves", None, mon, False, False)] unhovered [Hide("mondata"), Hide("nonbattlemoves")] at scrollfadein

screen dungeonchoice(items, unfurl=True):
    layer "undersayer"
    zorder -1
    frame:
        background ("scrollunfurl" if unfurl else "plainscroll")

        vbox:
            null 
            pos (0.25, 0.35)
            spacing 20

            $ firstchoice = True
            for skill, stat, color, threshold, caption, returnable in items:
                vbox:
                    xminimum 550
                    if (skill != None):
                        hbox:
                            text "{size=50}DL: " + str(threshold) + "{/size}" font "fonts/AncientModernTales.ttf" yalign 0.5 at (scrollfadein if unfurl else None)
                            null width 50
                            text "[[{color=" + color + "}" + skill + ", " + stat + "{/color}]" font "fonts/AncientModernTales.ttf" outlines [ (absolute(2), "#404040", absolute(0), absolute(0)) ] yalign 0.5 at (scrollfadein if unfurl else None)
                    elif (firstchoice):
                        null height 75

                    button:
                        action [Hide("diceroll"), Hide("rewardpreview"), Return(returnable)]
                        hovered ([Show("bonuspreview", None, skill, threshold) if skill != None else NullAction(), Show("rewardpreview", None, returnable)])
                        unhovered ([Hide("bonuspreview"), Hide("rewardpreview")])
                        text ">" + ("" if not isinstance(returnable, str) else "{s}") + caption hover_color "#fff" font "fonts/AncientModernTales.ttf" yalign 0.5 xmaximum 550 at (scrollfadein if unfurl else None)
                
                $ firstchoice = False

init python:
    def interpretrewardpenalty(box):
        finalstring = ""
        for i, string in enumerate(box):
            if (len(string) > 5):
                return string
            elif (string[0] == "D"):
                finalstring += "Demotivate "
            elif (string[0] == "M"):
                finalstring += "Motivate "
            elif (string[0] == "I"):
                finalstring += "Item "
            elif (string[0] == "F"):
                finalstring += "Fight! "

            if (string[0] in ["D", "M"] and len(string) == 1):
                finalstring += "Leader "
            elif (string[0] in ["D", "M", "I"] and len(string) > 1):
                if (string[1] == "P"):
                    finalstring += "Party "
                    if (len(string) > 2):
                        if (string[2] == "X"):
                            if (len(string) > 3):
                                if (string[3].isdigit()):
                                    finalstring = string[1] + "x " + finalstring
                                elif (string[2:4] == "XL"):
                                    finalstring += "Except Leader "
                                elif (string[2:4] == "XR"):
                                    finalstring += "Except Random "
                            
                elif (string[1].isdigit()):
                    finalstring = string[1] + "x " + finalstring

            if (len(box) > 1 and i < len(box) - 1):
                finalstring = finalstring[:-1] + ", "

        return finalstring

screen rewardpreview(returnable):
    python:
        showsomething=True
        rewardsstring = "Rewards: Unknown"
        penaltiesstring = "Penalties: Unknown"
        if (returnable in outcomedex.keys()):
            rewards = outcomedex[returnable]["Rewards"]
            penalties = outcomedex[returnable]["Penalties"]
            if (rewards != None or penalties != None):
                showsomething = True
                if (rewards != None):
                    rewardsstring = "Success: " + interpretrewardpenalty(rewards)
                if (penalties != None):
                    penaltiesstring = "Failure: " + interpretrewardpenalty(penalties)
        elif (returnable is False):
            rewardsstring = "Re-roll event"
            penaltiesstring = "and start a battle!"

    if (showsomething):
        #add "gui/dungeontextbox.png" xanchor 1.0 xpos 1.5 xzoom -1 yzoom 0.8
        frame:
            background Frame("gui/PaperFrame.png", 0, 0)
            padding (70, 25)
            #anchor (0.5, 0.5)
            #pos (0.75, 0.05)
            vbox:
                spacing 20
                text rewardsstring:
                    font "fonts/pmdfont.ttf"
                    size 55
                text penaltiesstring:
                    font "fonts/pmdfont.ttf"
                    size 55

screen diceroll(success, threshold, randnum, bonus):
    layer "undersayer"
    zorder -1
    modal True

    python:
        xpos = 0.14 + 160.0 / 1920.0
        ypos = 0.25 + 160.0 / 1080.0
        dicematrix = SaturationMatrix(1.2) * TintMatrix(GetCharColor(squadleader.GetFormatName()))
        total = randnum + bonus
        if (renpy.get_skipping()):
            renpy.hide_screen("diceroll")
            renpy.show_screen("enddiceroll", success, threshold, total, dicematrix)

    add "plainscroll"
    add "diceroll" at dicerolltrans, Transform(matrixcolor=dicematrix)
    
    text "Challenge Level " + str(threshold) size 70 font "fonts/DungeonFont.ttf" align (0.5, 0.5) pos (0.14 + 160 / 1920, 0.05 + 160 / 1080) at scrollfadein

    text str(randnum) align (0.5, 0.5) pos (xpos, ypos) font "fonts/DungeonFont.ttf" color "#fff" outlines [ (absolute(0), "#1b1b1b", absolute(5), absolute(5)) ] size 70 at varfadein(2.0), collide(xpos, xpos - 0.05, xpos)

    if (bonus != 0):
        vbox at varfadein(3.0), collide(xpos + 0.06, xpos + 0.11, xpos):
            align (0.5, 0.5) 
            pos (xpos + 0.06, ypos)
            spacing -20
            text "+" + str(bonus) align (0.5, 0.5) font "fonts/DungeonFont.ttf" color "#fff" outlines [ (absolute(0), "#1b1b1b", absolute(5), absolute(5)) ] size 70
            text "Bonus!" align (0.0, 0.5) font "fonts/DungeonFont.ttf" color "#fff" outlines [ (absolute(0), "#1b1b1b", absolute(5), absolute(5)) ] size 30

    text str(total) align (0.5, 0.5) pos (xpos, ypos) size 90 font "fonts/DungeonFont.ttf" color "#fff" outlines [ (absolute(0), "#1b1b1b", absolute(5), absolute(5)) ] at totalnum 

    if (success):
        text "Success!" align (0.5, 0.5) pos (xpos, ypos + 0.2) size 70 font "fonts/DungeonFont.ttf" at varfadein(5)
    else:
        text "Failure..." align (0.5, 0.5) pos (xpos, ypos + 0.2) size 70 font "fonts/DungeonFont.ttf" at varfadein(5)

    timer 5.3 action [Show("enddiceroll", None, success, threshold, total, dicematrix), Hide("diceroll")]

screen enddiceroll(success, threshold, total, dicematrix):
    layer "undersayer"
    zorder -2
    add "plainscroll"
    add "gui/D20-2.png" at Transform(align=(0.5, 0.5), pos=(0.14 + 160 / 1920, 0.25 + 160 / 1080), matrixcolor=dicematrix)

    text "Challenge Level " + str(threshold) size 70 font "fonts/DungeonFont.ttf" align (0.5, 0.5) pos (0.14 + 160 / 1920, 0.05 + 160 / 1080)

    python:
        xpos = 0.14 + 160.0 / 1920.0
        ypos = 0.25 + 160.0 / 1080.0

    text str(total) align (0.5, 0.5) pos (xpos, ypos) size 90 font "fonts/DungeonFont.ttf" color "#fff" outlines [ (absolute(0), "#1b1b1b", absolute(5), absolute(5)) ]

    if (success):
        text "Success!" align (0.5, 0.5) pos (xpos, ypos + 0.2) size 70 font "fonts/DungeonFont.ttf"
    else:
        text "Failure..." align (0.5, 0.5) pos (xpos, ypos + 0.2) size 70 font "fonts/DungeonFont.ttf"

init python:
    class AnimatedNumber(renpy.Displayable):
        def __init__(self, new_value, old_value = None, post_append="", animation_time = 1.0, format = "{:.0f}", **kwargs):
            text_prop, prop  = renpy.easy.split_properties(kwargs, "text_", "")
            super(AnimatedNumber, self).__init__(**prop)

            self.new_value = new_value
            if old_value:
                self.old_value = old_value
            else:
                self.old_value = new_value
            self.text = Text("", **text_prop)
            self.animation_time = animation_time
            self.format_str = format
            self.str_new_value = self.format(self.new_value)
            self.update = True
            self.post_append = post_append

        def format(self, value):
            return self.format_str.format(value)

        def get_value(self, st):
            t = st/self.animation_time
            t = max(0.0, min(t, 1.0))                           # clamp
            t = round(t,1)                                      # smooth the number change
            value = max(0, (1-t)*self.old_value + t*self.new_value)     # lerp
            return self.format(value)

        def render(self, width, height, st, at):
            if self.update == True:
                self.st = st
                self.update = False
            str_value = self.get_value(st - self.st)
            self.text.set_text(str_value + self.post_append)
            cr = renpy.render(self.text, width, height, st, at)
            w, h = cr.get_size()
            r = renpy.Render(w, h)
            r.blit(cr, (0, 0))
            if self.str_new_value != str_value:
                renpy.redraw(self,0)
            return r

screen dungeontally():
    python:
        maxmorale = activedungeon.MaxMorale()
        totalmorale = activedungeon.TallyMorale()
        numberstars = math.ceil(totalmorale / maxmorale * 5)
        rank = ""
        if (numberstars == 5):
            rank = "Secret Guildmaster Rank!"
        elif (numberstars == 4):
            rank = "Master Rank"
        elif (numberstars == 3):
            rank = "Hyper Rank"
        elif (numberstars == 2):
            rank = "Super Rank"
        elif (numberstars == 1):
            rank = "Gold Rank"
        elif (numberstars == 0):
            rank = "Bronze Rank"

    hbox:
        align (0.5, 0.5)
        vbox:
            vbox:
                for key, value in activedungeon.ItemHistory.items():
                    text str(value) + "x " + key xalign 0.5 size 40 color "#fff" outlines [ (absolute(5), "#000", absolute(0), absolute(0)) ] at pausethendis(3.0)
            text "Loot" xalign 0.5 size 70 color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] at pausethendis(3.0)

        vbox:
            align (0.5, 0.5)
            text "Morale" xalign 0.5 size 70 color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]
            add AnimatedNumber(new_value=totalmorale, old_value=0, post_append= "/" + str(maxmorale), animation_time=5.0, text_size=50, text_color="#fff", text_outlines=[ (absolute(10), "#000", absolute(0), absolute(0)) ]) xalign 0.5

            if (len(outcomedex)):
                text "Outcomes Seen: " + str(len(outcomedex)) + "/" + str(GetTotalOutcomes()) xalign 0.5 size 40 color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] at pausethendis(1.8) 

            text ("★" * numberstars + "☆" * (4 - numberstars) if numberstars != 5 else "★★★★★") font "fonts/DejaVuSans.ttf" xalign 0.5 size 70 color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] at pausethendis(2.3)

            text "Evaluation: " + rank xalign 0.5 size 70 color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] at pausethendis(3.0)

        vbox:
            vbox:
                for progress, battle in activedungeon.BattleHistory:
                    if (battle in playerparty or battle in box):
                        text "Caught - " + battle.GetNickname() xalign 0.5 size 40 color "#fff" outlines [ (absolute(5), "#000", absolute(0), absolute(0)) ] at pausethendis(3.0)
                    elif (battle.Health != 0):
                        text "Lost - " + battle.GetNickname() xalign 0.5 size 40 color "#fff" outlines [ (absolute(5), "#000", absolute(0), absolute(0)) ] at pausethendis(3.0)
                    else:
                        text "Won - " + battle.GetNickname() xalign 0.5 size 40 color "#fff" outlines [ (absolute(5), "#000", absolute(0), absolute(0)) ] at pausethendis(3.0)
            text "Battles" xalign 0.5 size 70 color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] at pausethendis(3.0)

    textbutton ">Back to reality..." at pausethendis(4.0):
        text_font "fonts/pkmndp.ttf"
        style "menu_choice_button"
        xysize (350, 90)
        text_color "#000000fe"
        text_hover_color "#ff00fffe"
        xmaximum 360 
        text_xalign .5 
        text_yalign .5
        text_size 30
        action [Return()]