label day010407:
call calendar(1) from _call_calendar_2
$ calDate = calDate.replace(day=7, month=4, year=2004)

$ timeOfDay = "Morning"

$ PlaySound("Alarm.ogg")
$ renpy.pause(4.0, hard=True)

redmind hatless casual tired @closedeyes frownmouth "Ughh..."

$ renpy.music.play("Audio/Morning_ambience.ogg", channel='crowd', loop=True, fadein=1.0)

scene dorm_A with transeye2

$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

hide blank2

show ethan uniform at centerside with dis
show calem uniform at leftside with dis
show brendan uniform at rightside with dis

$ renpy.music.stop(channel='crowd', fadeout=1.0)

ethan @happy "¡Buenos días, dormilón!"

calem @talkingmouth "¿Dormiste bien?"

red hatless casual @sadbrow talkingmouth "Ugh. Demasiado bien. Probablemente no tengo mucho tiempo para cambiarme y llegar a clases, ¿verdad?"

brendan @talking2mouth "Me temo que no. Nos quedamos un poquitin más solo para asegurarnos de que te despertaras."
brendan @happy "¡Roncaste como un Exploud!"

calem @closedbrow talkingmouth "¿Exploud? Yo habría pensado que Snorlax sería una comparación más acertada."

brendan @happy "Sí, probablemente, pero no sé qué es eso."

red -tired @talkingmouth "Hey, concéntrense. ¿Alguien notó a qué hora me fui a dormir anoche?"

ethan @confused "¿Qué, como si nos quedáramos viéndote dormir? No, bro."

pause 2.0

show ethan surprisedbrow frownmouth with dis:
    xpos 0.5
    ease 0.5 xpos 0.6
show brendan surprisedbrow frownmouth with dis:
    xpos 0.75
    ease 0.5 xpos 0.8
show calem surprisedbrow frownmouth with dis:
    xpos 0.25
    ease 0.5 xpos 0.4
show hilbert uniform:
    xpos -0.2 xzoom -1
    ease 0.5 xpos 0.2

hilbert @talkingmouth "1:12 de la mañana, obviamente."

pause 1.5

hilbert @surprised "¿Qué?"
hilbert @angry "Ustedes simplemente no prestan atención."

show ethan surprisedbrow frownmouth with dis:
    xpos 0.6
    ease 0.5 xpos 0.5
show brendan surprisedbrow frownmouth with dis:
    xpos 0.8
    ease 0.5 xpos 0.75
show calem surprisedbrow frownmouth with dis:
    xpos 0.4
    ease 0.5 xpos 0.25
show hilbert uniform:
    xpos 0.2
    ease 0.5 xpos 1.2

pause 1.0

$ PlaySound("Door_Slam.ogg")

pause 1.0

show ethan -surprisedbrow -frownmouth 
show brendan -surprisedbrow -frownmouth
with dis

calem @closedbrow talking2mouth "Si sigue azotando esa puerta, vamos a tener que pagar para arreglarla..."

brendan @surprised "Bueno, como sea, amigo. ¡La una de la mañana es demasiado tarde para quedarse despierto! Tienes que priorizar tu salud."

red @closedeyes talkingmouth "Sí, fue una mala idea. No volverá a pasar."

ethan @happy "¡Genial! Y ahora que te salvamos la vida, vendrás con nosotros al Salón Batalla después de clases, ¿verdad?"

red @confused "¿Eh? Bueno, supongo que sí."

calem @closedbrow talkingmouth "Para ponerte en contexto, estuvimos hablando y decidimos que queríamos ver algunas batallas."

brendan @talkingmouth "Sí, el equipo de batalla va a estar ahí, ¿no? {w=0.5}{nw}"
extend @talkingmouth "No es que me interese demasiado el gran EB, pero son bastante importantes en la academia."

ethan @happy "¡Sí! Y a mí sí me interesan. Así que, ¿vendrás, no?"

red @happy "Sí, ¿por qué no? Será divertido."

ethan @talkingmouth "¡Genial! Pero primero, deberíamos ir a clase. Ya es...{w=0.5}{nw}"

show calem surprisedbrow frownmouth 
show brendan surprisedbrow frownmouth
with dis

extend surprisedbrow frownmouth @surprised "Esperen, ¡¿{i}qué{/i} hora es?!"

red surprisedbrow frownmouth @surprised "¡Mierda! ¡Vayan ustedes sin mí, sino van a llegar tarde por mi culpa!"

scene blank2 with splitfadefast

jump PickElective