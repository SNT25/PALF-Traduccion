label day010406:
call calendar(1) from _call_calendar_1
$ calDate = calDate.replace(day=6, month=4, year=2004)

$ timeOfDay = "Morning"

$ renpy.music.play("Audio/Morning_ambience.ogg", channel='crowd', loop=True, fadein=1.0)

scene dorm_A with transeye2

$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

hide blank2

redmind casual hatless @thinking "Hmm... Parece que todos siguen dormidos. Bueno, quería llegar temprano para hablar con Sam antes de que comenzara la clase, así que esto me viene bien."

pause 2.0

red uniform -casual -hatless @happy "¡Me voy, [pika_name]!"

$ PlaySound("Pokemon/pikachu_pikapika1.ogg")

pikachu happy_2 "¡Pika, pika!"

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_15

show blank2 with splitfade
$ renpy.music.stop(channel='crowd', fadeout=1.5)
stop music fadeout 1.5

$ renpy.pause(2.5, hard=True)

show morning at vspaz

pause 3.5

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)

show oakbg at dissolvein behind blank2
show homeroom behind oakbg

hide blank2 with splitfade
hide dorm_A

$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

hide morning

narrator "Desafortunadamente, a pesar de tus intentos de entablar conversación con el Profesor Oak, él se niega rotundamente a responder cualquier pregunta, diciendo que lo hará más tarde."
narrator "Al fracasar en tu misión, esperas que Ethan tenga más suerte y te preparas para tu clase."

oak @talkingmouth "¿Cómo están todos esta mañana? Espero que hayan dormido bien, porque hoy cubriremos mucho material.{w=0.5} Esto estará en los exámenes, así que presten mucha atención."

show leaf uniform with dis:
    xpos 0.33 xzoom -1

leaf @talking2mouth "Profesor, todavía no nos ha explicado cómo funcionan los exámenes en esta clase."

oak @talkingmouth "Oh, ¿no lo hice?{w=0.5} Bueno, nunca hay mejor momento que el ahora."

hide leaf with dis

oak @talkingmouth "Como saben, además de entrenar Pokémon, también son responsables de {color=#0048ff}aprobar tanto los parciales como los exámenes finales de sus clases generales{/color}."
oak @talkingmouth "Además, en las clases generales deberán resolver un cuestionario {color=#0048ff} cada Lunes y Jueves antes de que termine el día{/color}."
oak @talkingmouth "No sólo {color=#0048ff}algunas de esas preguntas aparecerán en futuros exámenes, sino que acertarlas también les ayudará fuera de la academia/color}."
oak @talkingmouth "Tomen mi palabra. Si fuera ustedes, prestaría atención a estas clases.{w=0.5} Me lo agradecerán antes de lo que piensan."

redmind "Cuando Sam dice algo así, es porque habla en serio."
redmind "Probablemente debería seguir su consejo.{w=0.5} Nunca me ha defraudado antes."

oak @talkingmouth "Bien, ¿qué les parece si hacemos un cuestionario de práctica ahora? Se les dará un escenario hipotético de batalla, y el objetivo es simplemente ganar."

stop music

$ trainer1 = Trainer("red", TrainerType.Player, [Pokemon(pokedexlookupname("Rattata", DexMacros.Id), level=5, moves=[GetMove("Tackle"), GetMove("Tail Whip")])])
$ trainer2 = Trainer("oak", TrainerType.Enemy, [Pokemon(pokedexlookupname("Cherubi", DexMacros.Id), level=2, moves=[GetMove("Absorb")])])

call Battle([trainer1, trainer2], gainexp=False, uniforms=[True, False]) from _call_Battle
$ wonbattle = _return

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)

oak @talkingmouth "... Bien, creo que ya ha pasado suficiente tiempo. ¿Podrian pasar sus respuestas al frente?"

if (wonbattle):
    red uniform @happy "Hey, eso estuvo bastante fácil. Solo era una prueba de práctica, pero me gusta tener éxito en ellas."
else:
    red uniform @sad "No creo que me haya ido muy bien en esta prueba. Al menos solo era de práctica, pero... esto no es buena señal."

oak @talkingmouth ".{w=0.5}.{w=0.5}.{w=0.5}"

pause 0.5

oak @talkingmouth "A simple vista..."

pause 0.5


if (wonbattle):
    oak "Parece que a todos les fue bastante bien. No creo que esta clase tenga problemas para aprobar, ¡si siguen así! Aunque les pido que mejoren su caligrafía"
else:
    oak "Recomiendo que intenten no complicar demasiado las batallas simples. Los cambios de estadísticas no importan si ya están golpeando por más de la mitad de los PS del oponente."
    oak "Siendo totalmente franco, aunque esto fue solo una prueba de práctica, un desempeño así de continuo no será suficiente.{w=0.5} ¡Ejem! Así que tomen esto como una llamada de atención."

oak @talkingmouth "A partir de ahora, pueden esperar preguntas cada vez más dificiles que las anteriores.{w=0.5} {color=#0048ff} Además, tendrán exámenes de avance en cada una de sus electivas, aunque depende de cada instructor cuándo administrarlos.{/color}"
oak @talkingmouth "Aclarado eso, pasemos a la sección sobre arqueología."
oak @talkingmouth "Las primeras Poké Balls no aparecieron hasta el descubrimiento de los Bonguri en la región de Johto hace más de 500 años.{nw}"

show blank2 with dis

extend @talkingmouth " En 1925, el Profesor Westwood desarrolló la mecánica moderna de las Poké Ball..."

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_16

$ renpy.music.set_volume(0.1, delay=1.0, channel="music")
$ PlaySound("BellChime.ogg")

$ renpy.pause(2.5, hard=True)

$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

narrator "Desafortunadamente, la clase termina antes de que puedas hablar en privado con el Profesor Oak, y debes dirigirte a tu electividad...."

stop music fadeout 1.5

hide oakbg
hide homeroom

jump PickElective