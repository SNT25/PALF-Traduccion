label gym010406:

$ timeOfDay = "Noon"

  

play music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

$ renpy.transition(dissolve)
show screen currentdate

scene gym with dis

show blank2 behind gym

$ renpy.pause(2.0, hard=True)

hide blank2

show alder norm2 with dis:
    xpos 0.66

show bruno think with dis:
    xpos 0.33

alder @talkingmouth "Bienvenidos de nuevo, todos.{w=0.5} ¿Están listos para un día productivo en el gimnasio?"
alder happy2 "Bueno, en realidad no importa si lo están o no, porque van a tenerlo quieran o no.{w=0.5} ¡Para eso nos paga la escuela, ja, ja!"
alder norm2 "Apuesto a que todos ustedes se preguntan exactamente de qué estoy hablando."
alder spunky2 "Bueno, se los mostraré."

show bruno think:
    xpos 0.33
    ease 0.7 xpos 0.25

show alder norm2:
    xpos 0.66
    ease 0.5 xpos 0.5
    
alder @talkingmouth "¡Sal ahora!"

show alder norm:
    xpos 0.5

$ renpy.music.play("Audio/Pokemon/Volcarona_Ball.ogg", channel="altcry", loop=None)

show volcarona at pokeball behind alder:
    xpos 800 + 800 ypos 1080 zoom 1.8

$ renpy.pause(1.0, hard=True)

show volcarona:
    subpixel True
    zoom 1.8 ypos 1080 xpos 800 + 800
    block:
        parallel:
            ease 1.0 ypos 900
            ease 1.3 ypos 1040
            ease 0.9 ypos 930
            ease 1.5 ypos 1080
            ease 1.2 ypos 905
            ease 1.4 ypos 1160
        parallel:
            ease 0.8 xpos 750 + 800
            ease 1.4 xpos 825 + 800
            ease 1.1 xpos 860 + 800
            ease 1.6 xpos 830 + 800
            ease 1.25 xpos 775 + 800
            ease 1.3 xpos 800 + 800
        repeat

show bruno think:
    xpos 0.25

pause 1.0

blue uniform surprised "¡¿Un Volcarona?!"

hilbert uniform @talkingmouth "Tal y como se espera del Campeón de Teselia..."

bianca uniform @excitedeyes talkingmouth "¡Guau...!{w=0.5} {cps=200}¡Eso es increíble! Oh, Dios, miren sus alas, ¡son las cosas más bonitas que he visto en mi vida!{/cps}{w=0.4}"
show alder happy with dis
bianca @happy "¿Puedo tomarle una foto rápida?"

may uniform angrybrow ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
extend @talkingmouth "Voy a conseguir un Volcarona."

alder norm2 "Tranquilos, clase, solo la estoy usando como demostración."
alder norm2 "Bruno, trae el maniquí."
show alder norm with dis

hide bruno with dis

pause 1.5

show balloonbot with dis:
    subpixel True
    yalign 0.5 xpos -0.5#    xalign -2.0
    parallel:
        ease 0.9 xpos 0.05
    parallel:
        ease 1.5 yalign 0.4
        ease 1.3 yalign 0.8
        ease 1.6 yalign 0.5
        ease 1.4 yalign 0.7
        repeat

show bruno norm with dis:
    xpos -100
    parallel:
        ease 0.75 xpos 200

pause 1.0

show bruno norm2:
    xpos 200

show balloonbot:
    block:
        ease 1.5 yalign 0.4
        ease 1.3 yalign 0.8
        ease 1.6 yalign 0.5
        ease 1.4 yalign 0.7
        repeat

bruno @talkingmouth "¿Así está bien?"
show bruno norm with dis
alder norm2 "Está perfecto."
show alder norm

calem uniform @surprised "¿Un balloon bot?{w=0.5}  ¿Vamos a tener un Superentrenamiento hoy?"

hide ethan
ethan uniform @closedbrow talkingmouth "'¿Superentrenamiento?'{w=0.5} Eso suena a algo sacado de un videojuego."

alder happy2 "Ja, ja, no, hoy no. Todavía es demasiado pronto para eso.{w=0.5}{nw}"
extend norm2 " Hoy haremos algo un poco más sencillo."
show alder norm with dis

ethan @surprised "¿Así que el Superentrenamiento es real...?"

show bruno think with dis
alder happy2 "¡Comencemos!"

hide alder          
hide bruno
hide volcarona
hide balloonbot
with dis

$ trainer1 = MakeTrainer("Alder", TrainerType.Ally)
$ trainer2 = Trainer("bruno", TrainerType.Enemy, [Pokemon(pokedexlookupname("Balloon Bot", DexMacros.Id), level=70, moves=[GetMove("Splash")], gender="Unknown")])

call Battle([trainer1, trainer2], customexpressions=["alder", "alder spunky2", "bruno", "bruno angry3"], gainexp=False) from _call_Battle_1

stop music fadeout 1.0
pause 1.0

show alder norm3 with dis:
    xpos 0.66

show bruno think with dis:
    xpos 0.33

$ renpy.music.play("Audio/Music/Gym_Loop.ogg", channel='music', loop=True, fadein=1.25, tight=None)
    
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

$ _game_menu_screen = "game_menu"

hide blank2

show alder norm4
alder @talkingmouth "Ahora... ¿quién fue el que dijo que los niños de 10 años pueden arreglárselas aquí{w=0.25}.{w=0.25}.?{w=0.7}{nw}"

extend happy2 " Ah-ja, ahí estás."

show alder norm:
    xpos 0.66 xzoom 1
    ease 0.75 xpos 0.5 xzoom -1

show bruno norm:
    xpos 0.33
    ease 1.0 xpos 0.25

show blue uniform with dis:
    xpos 0.75 xzoom -1

$ renpy.pause(1.0, hard=True)

show alder:
    xzoom -1 xpos 0.5

show bruno:
    xpos 0.25

alder norm3 "Hmm..."
alder norm2 "¡Oh, casi lo olvido!{w=0.5} Tú eres el que quiere unirse al equipo de batalla de la academia."

show blue angry with dis

alder @talkingmouth "¿Hablabas en serio sobre eso, chico?"

show alder norm with dis

show bruno norm with dis

blue @talkingmouth angrybrow "¡Sí, es cierto!{w=0.5} ¿Por qué no lo estaría?"

blue @happybrow talking2mouth "Obviamente es el trampolín perfecto para mí en mi camino a convertirme en el Campeón Mundial."
show blue -angry with dis

$ renpy.music.play("Audio/hall_crowd.ogg", channel='crowd', loop=True, fadein=0.5)
pause 1.5

alder @talkingmouth "Hmm.{w=0.25}.{w=0.25}.{w=0.5}{nw}"
extend norm2 " Así que ese es tu objetivo.{w=0.5} Ser el Campeón Mundial."

alder norm "Hmm.{w=0.25}.{w=0.25}.{w=0.5}{nw}"
extend happy2 " Lo siento, hay demasiados en esta clase y aún no he memorizado todos sus nombres."

alder norm2 "¿Cómo te llamas?"
show alder norm with dis

blue @talkingmouth "Blue."

redmind uniform @thonk "Me sorprende que no haya dicho su apellido.{w=0.5} Apuesto a que al menos habría provocado alguna reacción en Alder o Bruno."

alder norm2 "¡Tú! ¡El del sombrero rojo!"
show alder norm with dis

red @surprised "¿E-Eh?"

calem uniform @talkingmouth "Definitivamente no me está mirando a mí."
hilbert uniform @closedbrow talkingmouth "Ni a mí."
bianca happy uniform "¿Verdad? Es confuso, ¿no?"

red @talkingmouth "Uh, ¿señor?"

show blue surprisedbrow frownmouth with dis

alder happy2 "¡Sí! Sí, tú.{w=0.5}{nw}"    
extend norm2 " ¿Cuál es tu nombre?"
show alder norm with dis

show blue -surprisedbrow -frownmouth -surprised with dis

red @talkingmouth "Uh, me llamo [first_name]. [first_name] [last_name]."

show blue surprisedbrow frownmouth with dis
alder happy2 "¡[first_name]!{w=0.6} ¿Por qué no tienes un combate con Blue aquí mismo, frente a todos tus compañeros?"
show alder happy with dis

show blue happybrow with dis

red surprisedbrow frownmouth @surprised "¿Qué?"

show bruno think with dis
alder happy2 "Ya me escuchaste."
show alder happy with dis

blue @happy "¡Perfecto!{w=0.5} ¡He estado esperando esto desde hace mucho!"
show blue -happy with dis
    
ethan uniform surprised "Oh, cielos, ¿Alder realmente va a hacerte pelear? Supongo que no sabe sobre tu historia con [blue_name]."
ethan happy "Aun así, ¡tú puedes!"

calem uniform happy "Buena suerte, [first_name]. Confío en tu destreza."
brendan uniform happy "¡Patéale el culo, bro!"
may uniform happy "¡Todos te apoyamos!"
hilbert uniform angrybrow "No deshonres a nuestro dormitorio."
serena uniform happymouth closedbrow "Por favor, danos un buen espectáculo."

show blue scaredbrow frownmouth with dis

Character("{color=#f2a634}???{/color}") "{size=30}¡Tú puedes, Blue! ¡Confió en ti!{/size}"

show blue angry with dis

redmind @thonk "¿Ah? ¿Quién dijo eso?"
redmind @thonk "...{w=0.5} No veo a nadie. ¿Serán... bajitos?"

leaf uniform talkingmouth "¿La primera batalla del nuevo año escolar? Más te vale que hagas que cuente."
leaf flirttalk "Sin presiones."

red @confused "Ninguna recibida."

hide alder happy           
hide bruno think
hide blue
with dis
    
$ trainer1 = Trainer("red", TrainerType.Player, playerparty)
$ trainer2 = Trainer("blue", TrainerType.Enemy, [Pokemon(pokedexlookupname("Eevee", DexMacros.Id), level=5, moves=[GetMove("Tackle"), GetMove("Sand Attack"), GetMove("Tail Whip"), GetMove("Growl")], gender=Genders.Male, ability="Run Away")])#Eevee

call Battle([trainer1, trainer2], uniforms=[True, True], gainexp=False) from _call_Battle_2
$ battlehistory["Blue1"] = _return

stop music fadeout 1.0
pause 1.0

show alder norm with dis:
    xpos 0.5 xzoom -1

show bruno norm with dis:
    xpos 0.25
    
if WonBattle("Blue1"):
    show blue uniform angry with dis:
        xpos 0.75 xzoom -1
else:
    show blue uniform with dis:
        xpos 0.75 xzoom -1

$ renpy.music.queue("Audio/Music/Gym_Loop.ogg", channel='music', loop=True, fadein=1.25, tight=None)

hide blank2 with dis
    
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

hide blank2

if WonBattle("Blue1"):
    blue @angry "¡N-No puede ser!{w=0.5} ¡Solo fui descuidado!"
    red uniform @happy "¡Gran trabajo, [starter_name]!"

else:
    blue @happy "¡Sí! ¿Soy increíble o qué?"
    red uniform @sad "Oh, no... Lo siento, [starter_name]."

alder happy2 "¡Muy bien hecho! Fue una gran batalla.{w=0.5}{nw}"
extend norm2 " Ambos deberían sentirse orgullosos de ustedes mismos y de sus Pokémon."

alder @talkingmouth "Hablando de eso, vamos a curarlos."

show alder norm with dis

pause 0.5

$ renpy.music.set_volume(0.0, delay=0.0, channel="music")
$ PlaySound("recovery.ogg")
$ HealParty()
pause 2.5
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

show alder norm2:
    xpos 0.5 xzoom -1
    ease 0.5 xpos 0.66 xzoom 1

show bruno norm:
    xpos 0.25
    ease 0.5 xpos 0.33

hide blue with dis

alder @talkingmouth "Una vez más, gracias, Blue y [first_name], por mostrarnos una excelente batalla Pokémon.{w=0.5}{nw}"

extend norm2 " Los Pokémon realmente parecían estar disfrutando cada segundo de la batalla."

alder @talkingmouth "Recuerden siempre esto. Las batallas Pokémon no se tratan solo de ganar.{w=0.5} Lo más importante es cómo tú y tu Pokémon trabajan juntos como equipo."
show alder norm with dis

$ PlaySound("BellChime.ogg")

show bruno think with dis
alder happy2 "Y eso es todo por hoy.{w=0.5} ¡Disfruten el resto del día!"
show alder norm with dis

show blank2 with dis

stop music fadeout 1.5

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_17 

$ renpy.pause(2.0, hard=True)

scene blank2
    
show afternoon at vspaz
    
pause 3.5

jump lunch010406