label clearscreens:
    call cleardungeonscreens() from _call_cleardungeonscreens_6
    call clearcontestscreens() from _call_clearcontestscreens

    hide screen currentdate
    hide screen movedata
    hide screen mondata
    hide screen nonbattlemoves
    hide screen fieldinventory
    hide screen partyviewerpopup
    scene onlayer arrowlayer
    with dis
return

label silence:
    stop music fadeout 1.5
    stop music fadeout 1.5 channel "crowd"
    stop music fadeout 1.5 channel "crowd2"
    stop music fadeout 1.5 channel "crowd3"
    stop music fadeout 1.5 channel "misc"
return