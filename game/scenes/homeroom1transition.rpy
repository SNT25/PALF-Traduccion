label homeroom1transition:

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_49

$ PlaySound("bellchime.ogg")
hide blank2
show blank2 with splitfade

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_50
$ renpy.music.stop(channel='crowd', fadeout=1.5)
stop music fadeout 1.5

jump PickElective