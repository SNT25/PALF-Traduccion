label gameover:

play sound "audio/shovel.ogg" fadein 30.0 loop

show blank2:
    alpha 0.0
    ease 6.0 alpha 1.0

narrator "As your last Pokémon falls in battle, you get a sinking feeling in your stomach that this was not how your story was supposed to end."

pause 2.0

narrator "Yet end it does."

scene blank2
call clearscreens from _call_clearscreens_83

show gameover at truecenter

pause 10

$ MainMenu(confirm=False)()