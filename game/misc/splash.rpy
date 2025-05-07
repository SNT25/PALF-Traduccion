init python:
    def calculate_Z(X, Y):
        z_values = {(0, 1): 0, (0, 2): -0.075, (0, 3): -0.125,
                    (1, 2): 0.075, (1, 3): 0, (2, 3): 0.125}
        if (X, Y) in z_values:
            return z_values[(X, Y)] + 0.15 + 0.02 * Y
        else:
            return 0

label CreateSplash(players, challengers, customexpressions=[], reanchor=[], uniforms=[], pkmnlist=[], pkmnids=[], customoutfits=[]):        
    # setup art
    hide blank2
    show blank2 zorder 0:
        alpha 0.0
        ease 0.5 alpha 1.0
        
    show speedlines zorder 1:
        yalign 0.5 xalign 0.5 alpha 0.0 zoom 1.0 rotate 0
        parallel:
            ease 0.25 alpha 1.0
            pause 1.0
            ease 1.0 alpha 0.0
        parallel:
            ease 2.5 zoom 3.25
        parallel:
            ease 2.5 rotate 270

    python:
        uniforms += [False]*6
        reanchor += [False]*6
        for i, player in enumerate(players):
            renpy.hide(player)
            xbuffer = calculate_Z(i, len(players))
            extrazorder = 1 if i == 1 and len(players) == 3 else 0
            charname = player.split(' ')[0]
            charcolor = GetCharColor(charname.capitalize()) if player not in pkmnlist and player != "sideportraitfull" else GetColor(pokedexlookupname(player.title(), DexMacros.Id))
            finalmatrix = TintMatrix(charcolor) * BrightnessMatrix(1.0) * ContrastMatrix(0.0)
            playersprite = (player if len(customexpressions) == 0 else customexpressions[i * 2]) + (" uniform" if uniforms[i] else "") + (" hat" if player == "tia" else "") + " " + ("" if len(customoutfits) == 0 else customoutfits[i])
            newtransforms = [Transform(yanchor=(1.0 if reanchor[i] else 0.65), xanchor=0.5), fadeinleft(xbuffer)] + ([Transform(ypos=0.7)] if player in pkmnlist or player == "sideportraitfull" else [])
            if ("roughneck" in playersprite):
                newtransforms.append(Transform(yanchor=0.8))
            renpy.show(playersprite, newtransforms + [Transform(matrixcolor=finalmatrix, xanchor=0.54, zoom=1.04)], zorder=2, tag="leftsilhouette" + charname + str(i) + "p")
            renpy.show(playersprite, newtransforms + [Transform(matrixcolor=InvertMatrix() * finalmatrix, xanchor=0.52, zoom=1.02)], zorder=3, tag="leftinversion" + charname + str(i) + "p")
            renpy.show(playersprite, newtransforms, zorder=4 + extrazorder, tag=charname + str(i) + "p")

        for i, challenger in enumerate(challengers):
            renpy.hide(challenger)
            xbuffer = 1.0 - calculate_Z(i, len(challengers))
            extrazorder = 1 if i == 1 and len(challengers) == 3 else 0
            charname = challenger.split(' ')[0]
            challengername = challenger if challenger != "sideportraitfull" else pkmnids[i]
            charcolor = GetCharColor(charname.capitalize()) if challenger not in pkmnlist and challenger != "sideportraitfull" else GetColor(challengername)
            finalmatrix = TintMatrix(charcolor) * BrightnessMatrix(1.0) * ContrastMatrix(0.0)
            challengersprite = (challenger if len(customexpressions) == 0 else customexpressions[i + len(players) * 2]) + (" uniform" if uniforms[i + len(players)] else "") + (" hat" if challenger == "tia" else "") + " " +  ("" if len(customoutfits) == 0 else customoutfits[i + len(players)])
            if (challenger == "sideportraitfull" and i == 1):
                challengersprite = "sideportraitfull2"
            elif (challenger == "sideportraitfull" and i == 2):
                challengersprite = "sideportraitfull3"
            newtransforms = [Transform(yanchor=(1.0 if reanchor[i + len(players)] else 0.65), xanchor=0.5), fadeinright(xbuffer)] + ([Transform(ypos=0.7)] if challenger in pkmnlist or challenger == "sideportraitfull" or challenger == "latias" else [])
            if ("roughneck" in challengersprite):
                newtransforms.append(Transform(yanchor=0.8))
            renpy.show(challengersprite, newtransforms + [Transform(matrixcolor=finalmatrix, xanchor=0.46, zoom=1.04)], zorder=2, tag="rightsilhouette" + charname + str(i)+ "e")
            renpy.show(challengersprite, newtransforms + [Transform(matrixcolor=InvertMatrix() * finalmatrix, xanchor=0.48, zoom=1.02)], zorder=3, tag="rightinversion" + charname + str(i)+ "e")
            renpy.show(challengersprite, newtransforms, zorder=4 + extrazorder, tag=charname + str(i)+ "e")
        
    # wait half a second
    pause 0.575
    
    # show the versus symbol
    show versus zorder 6:
        zoom 2.0 / (max(len(players), len(challengers)) + 1)
        xalign 0.5 yalign -0.5
        ease 0.35 yalign 0.85
        ease 0.25 yalign 0.45
        ease 0.15 yalign 0.5

    pause 1.0

    python:
        for i, player in enumerate(players):
            if (player not in pkmnlist):
                xbuffer = calculate_Z(i, len(players))
                newtransforms = [Transform(yanchor=(1.0 if reanchor[i] else 0.65), xpos=xbuffer), dissolvein]
                extrazorder = 1 if i == 1 and len(players) == 3 else 0
                renpy.transition(dissolve)
                renpy.show(((player + " uniform angrybrow happymouth" if uniforms[i] else player + " angrybrow happymouth") if len(customexpressions) == 0 else customexpressions[i * 2 + 1]), tag=player + str(i)+ "p")
        
        for i, challenger in enumerate(challengers):
            if (challenger not in pkmnlist):
                xbuffer = 1 - calculate_Z(i, len(challengers))
                newtransforms = [Transform(yanchor=(1.0 if reanchor[i + len(players)] else 0.65), xpos=xbuffer), dissolvein]
                extrazorder = 1 if i == 1 and len(challengers) == 3 else 0
                renpy.transition(dissolve)
                renpy.show(((challenger + " uniform angrybrow happymouth" if uniforms[len(players) + i] else challenger + " angrybrow happymouth") if len(customexpressions) == 0 else customexpressions[i + len(players) * 2 + len(challengers)]), tag=challenger + str(i)+ "e")
    
    pause 1.5
    
    # hide images
    python:
        for i, name in enumerate(players):
            renpy.hide(name+ str(i)+ "p") 
            renpy.hide("leftsilhouette" + name+ str(i)+ "p")
            renpy.hide("leftinversion" + name+ str(i)+ "p")
        
        for i, name in enumerate(challengers):
            renpy.hide(name+ str(i)+ "e")
            renpy.hide("rightsilhouette" + name+ str(i)+ "e")
            renpy.hide("rightinversion" + name+ str(i)+ "e")

    hide versus
    with Dissolve(0.5)
    show blank2:
        alpha 0.0
        ease 0.5 alpha 0.5
    return
    