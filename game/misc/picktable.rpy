call PickTable() from _call_PickTable#this exists purely so the bug fixer has somewhere to go when it gets stuck.

label PickTable():

hide blank2
show blank2 with dis:
    alpha 0.8

if (IsBefore(10, 5, 2004)):
    call screen tables(_with_none=False) with dissolve
    with dissolve
else:
    call screen newtables(_with_none=False) with dissolve
    with dissolve
hide blank2 with dissolve
if (_return == None):
    jump PickTable
elif (_return == "Melody's Table"):
    narrator "This is a bad idea."
else:
    narrator "You chose the [_return]?"

$ tablecalled = _return
if (IsBefore(10, 5, 2004)):
    menu:
        ">Go to the [_return]":
            if (_return == "Angry Table"):
                call angrytable from _call_angrytable
            elif (_return == "Cheerful Table"):
                call cheerfultable from _call_cheerfultable
            elif (_return == "Busy Table"):
                call busytable from _call_busytable
            elif (_return == "Romantic Table"):
                call romantictable from _call_romantictable
            elif (_return == "Calm Table"):
                call calmtable from _call_calmtable
            elif (_return == "Quiet Table"):
                call quiettable from _call_quiettable
            elif (_return == "Sleeping Table"):
                call sleepingtable from _call_sleepingtable

            if (IsDate(14, 4, 2004) and tablecalled != "Cheerful Table"):
                scene cafe with Dissolve(2.0)

                show whitney uniform angry:
                    xpos 0.66
                show tia uniform angry:
                    xpos 0.33
                with dis

                narrator "You sense Tia and Whitney's glares boring into the back of your head as you prepare to leave the lunchroom."

                $ ValueChange("Tia", -3, 0.33, False)
                $ ValueChange("Whitney", -3, 0.66)

                redmind uniform @thinking "Sorry, ladies. Just don't have the spoons for this right now."

            jump PickElective

        ">Rethink your choice":
            jump PickTable

else:
    menu:
        ">Go to Melody's Table" if (tablecalled == "Melody's Table"):
            call newtable(tablecalled) from _call_newtable_2

            jump PickTable

        ">Go to the [tablecalled]" if (not tablecalled == "Melody's Table"):
            call newtable(tablecalled) from _call_newtable

            $ removelunchstudents = set()

            jump PickElective
        ">Rethink your choice":
            jump PickTable