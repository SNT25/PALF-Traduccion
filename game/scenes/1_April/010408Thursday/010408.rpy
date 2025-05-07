label day010408:
python:
    for mon in playerparty:
        if (mon.GetId() == 25):
            pikachuobj = mon
    playerparty.remove(pikachuobj)
    timeOfDay = "Morning"
call calendar(1) from _call_calendar_3
$ calDate = calDate.replace(day=8, month=4, year=2004)


show morning at vspaz

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)

show homeroom behind oakbg

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade    
hide morning

$ renpy.pause(0.6, hard=True)

redmind uniform @thinking "Y ahora, de vuelta a la rutina.{w=0.5} Si recuerdo bien, Sam dijo que hoy tendríamos un cuestionario."
redmind "No debería ser un problema...{w=0.5} Eso espero."

Character("Estudiante Chismoso") "\"Oye, ¿ese no es el tipo al que Lance regañó ayer?\""
Character("Estudiante Ruidoso") "\"¿Qué? No, ese tenía el pelo rojo. Y se veía... amenazante.\""
Character("Estudiante Chismoso") "\"Espera, ¿el estudiante del pelo rojo era un chico? Pero tenía el cabello súper largo, ¿no?\""
Character("Estudiante Ruidoso") "\"No sé, tal vez había dos estudiantes gritándole a Lance. No estaba lo suficientemente cerca para ver bien.\""
Character("Estudiante Chismoso") "\"Dios, ¿te imaginas gritarle así a un profesor? Algunos idiotas tienen más dinero que sentido común y creen que pueden hacer lo que quieran en esta academia.\""

pause 1.0

redmind @angrybrow frownmouth "[ellipses]"    
redmind @thinking "... Bueno, supongo que lo que pasó ayer fue delante de un montón de estudiantes, así que no puedo decir que me sorprenda."

menu:
    "{color=#ff8412}[[Valentía]{/color} Será mejor que me ocupe de esto.":
        redmind @angrybrow frownmouth "... Aun así, será mejor que me encargue de esto."

        $ TraitChange("Courage")

        red @closedeyes talking2mouth "Chicos, yo--"

    "{color=#e226a6}[[Paciencia]{/color} Será mejor que me mantenga al margen.":

        $ TraitChange("Patience")

        redmind @angrybrow frownmouth "... Será mejor que me mantenga al margen."

show whitney uniform angrybrow frownmouth with dis:
    xpos 850
    ease 0.25 alpha 1.0 xpos 650
    
whitney @angrymouth "Diría que los verdaderos idiotas aquí son ustedes dos."

show whitney angry with dis:
    alpha 1.0 xpos 650

Character("Estudiante Chismoso") "\"¿Eh?\""

redmind @surprisedeyes surprisedeyebrows frownmouth "Bueno, supongo que la decisión ya fue tomada por mí."

Character("Estudiante Ruidoso") "\"¿Que acabas de decir?\""

show flannery uniform angry:
    alpha 0.0 xpos 1200
    ease 0.5 alpha 1.0 xpos 1050

flannery @talking2mouth "Así que además de chismosos son sordos, ¿eh?{w=0.5}{nw}"

show flannery angry veins with dis:
    alpha 1.0 xpos 1050

extend @talkingmouth " No me sorprende, cualquiera con audición normal se arrancaría las orejas después de escuchar a dos idiotas como ustedes."

Character("Estudiante Ruidoso") "\"¡¿Cu-cuál es tu problema?!\""

show whitney surprisedbrow frownmouth with dis:
    xpos 650
    ease 0.7 xpos 720

whitney @angrymouth "¿{i}Su {/i} problema?{w=0.5} ¿Cúal es el problema de {i}ustedes{/i}?"

show whitney angry with dis:
    xpos 720
    ease 0.3 xpos 670

whitney @talking2mouth "Ni siquiera saben bien lo que pasó, pero se ponen del lado de Lance."

show whitney angry:
    xpos 670

flannery @talking2mouth "¿De verdad creen que un Campeón regional necesita a dos idiotas como ustedes defendiéndolo? ¡Son unos payasos!"

whitney @angry "¡Exacto! Ni siquiera saben quién tenía la razón, solo quieren quedar bien con el que parece más fuerte."

flannery furiousmouth angrybrow "Realmente {i}odio{/i} lidiar con cosas como esta tan temprano en la mañana, así que más les vale largarse antes de que me enoje de verdad."

show flannery furious with dis:
    xpos 1050
    ease 0.5 xpos 1000
    
flannery @talking2mouth "¡Fuera de aquí!{w=0.5} ¡Vamos, LÁRGUENSE!"

show flannery:
    xpos 1000
    
Character("Estudiante Ruidoso") "\"¡Este también es nuestro salón, loca de...! {w=0.5}{size=30}Olvídalo.{/size}\""

show whitney -angry with dis

show flannery angrybrow frownmouth with dis:
    xpos 1000
    ease 0.75 xpos 1100

flannery @talking2mouth "Cretinos..."

show flannery:
    xpos 1100
    
pause 1.5

redmind @surprisedbrow frownmouth "[ellipses]"

show whitney:
    xpos 670
    ease 0.5 xpos 720

whitney @happy "¡Oh, hola, [first_name]!{w=0.5}{nw}"

show whitney happybrow with dis:
    xpos 720

extend @talkingmouth " ¿Listo para otro maravilloso día lleno de aprendizaje?"

show flannery -veins -angrybrow 
show whitney happy
with dis

red @sigh "Yo, eh... sí. Sí. Oigan, Whitney, Flannery.{w=0.5} Gracias por eso."
red @happy "Me gustaría decir que prefiero pelear mis propias batallas, pero de verdad lo aprecio"

show whitney -happy with dis:
    xpos 720
    pause 0.75
    ease 0.2 xpos 980
    ease 0.25 xpos 820
  
flannery tiredbrow @talking2mouth "No sé de qué estás hablan--{w=0.2}{nw}"

$ PlaySound("Body punch.ogg")

show flannery surprisedbrow frownmouth with dis:
    xpos 1100
    pause 0.25
    ease 0.1 xpos 1150
extend @talkingmouth " {i}¡Ugh!{/i}"

show flannery:
    xpos 1150

whitney @happybrow smilemouth "Ella quiso decir, '¡No hay problema, [first_name]!'"
whitney @talking2mouth "Lo siento, a veces se pone tímida.{w=0.5} Especialmente en situaciones como esta."

flannery -surprisedbrow -frownmouth -surprised frownmouth @angry "¡No es cierto!"

whitney @talking2mouth "En fin, cuídate tigre.{w=0.5} Y no dejes que esos inseguros te afecten."
whitney happy "¡Tienes que vivir como tú quieras!"
whitney -happy @happybrow smilemouth "Además, no íbamos a dejar que esos idiotas hablaran mal de esa chica de pelo rojo."

flannery @closedbrow talkingmouth "Las pelirrojas tenemos que cuidarnos entre nosotras."

redmind @thinking "¿Debería decirles que Silver es un chico?"

pause 1.0

redmind @happy "Nah, es más gracioso así."

show leaf uniform with dis:
    xpos 0
    ease 0.75 xpos 270

leaf @happybrow talkingmouth "¡Buenos días, [first_name]!{w=0.5} Y buenos días para ustedes también, Whitney y Flannery."

whitney @talking2mouth "¡Buenos días, Leaf!"
flannery tiredbrow frownmouth @talking2mouth "No, no lo es."

leaf @happy "Deberías ir a tu asiento, [first_name].{w=0.5}{nw}"
extend -happy @talkingmouth "¡La clase está por empezar!"

red @happy "Sí, ya lo sé."

hide leaf with dis
    
pause 1.0

redmind @thinking "Sé que no he pasado mucho tiempo con Whitney antes, pero nunca pensé que fuera tan...{w=0.33} carismática."

flannery @talking2mouth "Whitney, la clase empieza."

hide flannery with dis

whitney happy "Okay, ¡nos vemos luego, [first_name]!"

hide whitney with dis

pause 1.5

redmind @sadbrow frownmouth "Tengo que decirlo, esas dos restauraron mi fe en la humanidad, al menos un poco."

$ renpy.music.set_volume(0.0, delay=1.0, channel="music")
$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_34

$ PlaySound("BellChime.ogg")
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

show blank2 with Dissolve(1.5)

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_35
$ renpy.music.stop(channel='crowd', fadeout=1.5)
stop music fadeout 1.5
$ renpy.pause(2.5, hard=True)

jump PickElective