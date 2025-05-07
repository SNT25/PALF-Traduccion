label secondhomeroom010406:

$ timeOfDay = "Evening"

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=True, fadein=1.0, tight=None)

narrator "Desafortunadamente, en tu camino a clase, varias personas que presenciaron tu combate con [blue_name] te detienen, y apenas logras entrar a clases justo antes de que suene la campana, dejándote sin tiempo para hablar con Sam."

scene blank2

show homeroom behind blank2
    
show oakbg at dissolvein behind blank2

hide blank2 with dis

$ renpy.transition(dissolve)
show screen currentdate

$ PlaySound("BellChime.ogg")
$ renpy.pause(1.5, hard=True)

hide blank2

oak @talkingmouth "¡Buen trabajo hoy, clase!{w=0.5} Todos pueden retirarse, pero recuerden leer el material asignado."

hide oakbg with dis

redmind uniform @sad "Okay. Sam literalmente me miró y salió pitando de la clase. ¿Cuál es su problema? ¿Hice algo mal?"

show leaf uniform with dis:
    xpos 100
    ease 0.5 xpos 700

leaf @talkingmouth "Hey, [first_name]!{w=0.33} ¿Tienes planes para hoy?"

hide oakbg

red @talkingmouth "No, nada en especial.{w=0.5} ¿Supongo que quieres ir a algún lado otra vez?"

leaf @happybrow talkingmouth "Jeje, ¿fui tan obvia?"

leaf @flirttalk "Sabes que no voy a ser la tercera rueda con May y Brendan, así que te toca a ti entretenerme esta tarde."

red @happy "Ignorando el hecho de que básicamente me estás diciendo que soy tu segunda opción, haré lo que pueda."

show leaf -happy with dis
red @talkingmouth "¿A dónde querías ir?{w=0.5} ¿Al gimnasio otra vez? Puede que veas a Rosa de nuevo."

leaf @closedbrow talking2mouth "Hmm, ¿por qué no decides tú esta vez?{w=0.5} Es lo justo, ya que yo elegí la última vez."

red @talkingmouth "Bien, veamos el mapa de nuevo...{w=0.5} ¿qué tal el Centro Recreativo? No está muy lejos.{w=0.3}{nw}"
show leaf surprisedbrow frownmouth with dis
extend @talkingmouth " ¿Ese lugar no tiene una piscina?"

leaf -surprisedbrow -frownmouth @talking2mouth "Eh... supongo que sí."

red @talkingmouth "No me importaría echarle un vistazo.{w=0.5} Nadar es divertido, quizá pase por ahí en algún momento."

show leaf happybrow happymouth blush with dis:
    xpos 700
    ease 0.5 xpos 500

leaf @talking2mouth "...{w=0.5} ¡Ups! Justo recordé que tengo que ir a otro lado ahora mismo.{w=0.5} Lo siento, pero hoy no puedo."

show leaf fullblush with dis:
    xpos 500
    ease 1.0 xpos 200

leaf @talking2mouth "Es súper importante, así que tengo que correr. ¡Perdón!"

red @confused "Eh... está bien.{w=0.5} No tienes que disculparte si es algo urgente."

leaf @talking2mouth "¡Tal vez para la próxima!{w=0.5}{nw}"

show leaf:
    xpos 200 alpha 1.0
    ease 0.5 xpos -100 alpha 0.0
    
extend @talkingmouth " ¡Nos vemos!"

hide leaf

redmind @thonk "¿Qué bicho le picó?{w=0.5} Nunca la había visto tan nerviosa."
redmind @thonk "¿Será que {b}realmente{/b} no le gustan las piscinas? Yo prefiero el billar, pero..."

redmind @happy "Bueno, da igual. Igual voy a ver la piscina."

show hilda uniform with dis:
    xpos 100
    ease 1.0 xpos 500

pause 1.0

red @talkingmouth "¿Hilda? ¿Qué haces aquí?"

show hilda:
    xpos 500
    ease 0.7 xpos 750
    
hilda @talkingmouth "¿Qué más?{w=0.5} Estoy buscando a Hilbert."
hilda angrybrow  frownmouth @talkingmouth "Esta {i}es{/i} su clase, ¿no?"

red @closedbrow talking2mouth "Sí, pero está escondido debajo de aquel escritorio."

show hilbert angry uniform with dis:
    xpos 1700 zoom 0.5
    ease 1.25 xpos 1300 zoom 1.0

hilbert @talkingmouth "Eres un {i}traidor.{/i}"
         
hilda angrybrow talkingmouth "Ahí estás.{w=0.5}{nw}"

show hilda angry with dis:
    xpos 750
    ease 0.5 xpos 800
    
extend @talkingmouth " ¿Pensabas saltarte el entrenamiento otra vez?"

pause 2.0

hilbert sad @talkingmouth "Lo estaba...{w=0.5} considerando, sí."

show hilda:
    xpos 800
    ease 0.5 xpos 850
    
hilda @closedbrow talkingmouth "Pues ya no.{w=0.5} ¡Sabes lo que pasa cuando pasas demasiado tiempo sin entrenar!"

red @confused "¿Qué es esto del entrenamiento?"

show hilda:
    xpos 850
    ease 0.75 xpos 750

hilda sad "Ugh, ¿por dónde empiezo?"
hilda closedbrow talkingmouth "Hilbert tiene este... 'sueño' con el que está obsesionado. Y por estar tan metido en eso, se olvida de comer, dormir, hidratarse..."
hilda angry "O hacer ejercicio. Por eso se queda dormido a mitad de una conversación que no le interesa, porque tiene la resistencia de un Cleffa."

hilbert @talkingmouth "{size=30}¿O tal vez me duermo en medio de conversaciones aburridas porque son aburridas?/size}"

red @sadbrow talkingmouth "Eres una buena amiga."

hilda @sad "No, pero soy una buena madre, si es que eso cuenta para algo."

menu:
    "Eres una mamá muy guapa.":
        show hilda surprisedbrow frownmouth
        show hilbert surprisedbrow
        with dis

        pause 1.5

        $ ValueChange("Hilda", 1, 750.0/1920.0)

        hilda -surprisedbrow -frownmouth @happy "Mierda, eres todo un playboy. ¿Le dices eso a todas las mamás adolescentes?"

        red @unamusedbrow talking2mouth "Curiosamente, eres la única que he conocido"

    "[ellipses]":
        pass

    "Creo que eres un poco dura con Hilbert.":
        show hilda surprisedbrow frownmouth
        show hilbert surprisedbrow
        with dis

        $ ValueChange("Hilda", -2, 750.0/1920.0)
        hilda @closedbrow talkingmouth "Yo... literalmente no puedo ni empezar a describir lo malditamente equivocado que estás en esto."

        $ ValueChange("Hilbert", 1, 1300.0/1920.0)

hilbert sadbrow @talkingmouth "Ugh..."

hide hilbert with dis

hilda angrybrow frownmouth @angry "¡Hey! ¡Más te vale que vayas al Centro Recreativo, Hilbert!"

$ showredonly = True

hilbert @talkingmouth "¡Ya voy, ya voy! ¡Déjame en paz!"

$ showredonly = False

show hilda -angrybrow -frownmouth with dis

pause 1.0

red @talkingmouth "¿Así que tú también vas al Centro Recreativo?{w=0.5} Yo estaba pensando en ir a verlo."

hilda @talkingmouth  "Entonces vamos juntos. ¿Estas listo?"

red @talkingmouth "Tanto como puedo estarlo."

show hilda:
    xpos 750 alpha 1.0
    ease 1.0 xpos 100 alpha 0.0
    
$ renpy.pause(0.5, hard=True)
    
stop music fadeout 1.5
$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_19

window hide

show blank2 with splitfade
$ renpy.pause(1.5, hard=True)

play music "Audio/Music/Beyond2.ogg" loop fadein 1.0
show map behind blank2

hide homeroom
hide hilbert

$ renpy.transition(dissolve)
show screen currentdate

hide hilda
hide blank2 with splitfade
pause 0.5

hilda uniform happy "Hilbert y yo estaremos en las canchas.{w=0.5} ¿Quieres unirte?"

red @talkingmouth "Nah, pensaba revisar la piscina.{w=0.5} Pero gracias por la invitación."

hilda -happy @talking2mouth "Vale, pásala bien.{w=0.5} Estaremos ahí un par de horas, pero si terminas antes, puedes irte."

red @talkingmouth "Okay, me parece bien.{w=0.5} ¡Nos vemos luego!"

hide hilda

stop music fadeout 1.0
$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_20

show blank2 with splitfadefast
$ renpy.pause(1.0, hard=True)
hide map

play music "Audio/Music/Ocean Waltz_Start.ogg" noloop
queue music "Audio/Music/Ocean Waltz_Loop.ogg"

show pool behind blank2

$ renpy.transition(dissolve)
show screen currentdate
hide blank2 with splitfade

$ renpy.pause(0.5, hard=True)

redmind "¡Esta piscina es enorme! Me recuerda a la que esta en el gimnasio de Ciudad Celeste."
redmind "Con una piscina asi de lujosa, pensaba que habría estudiantes por todas partes.{w=0.5} Seguro que cuando empiecen las actividades de los clubes, el equipo de natación tomará el control de este lugar."

show misty with dis:
    xpos 800
    ease 0.75 xpos 700

redmind "Espera, ¿esa es Misty arrodillada junto al agua?{w=0.5} Parece que está revisando la temperatura con la mano."

show misty surprisedbrow with dis

red @talkingmouth "¿Comprobando la temperatura del agua?"
            
show misty angry with dis:
    xpos 700
    ease 0.5 xpos 620

misty @talkingmouth "¡Tú otra vez!"
misty @talkingmouth "¡¿Intentas matarme?!{w=0.5} ¡No me asustes así!"

red @talkingmouth "Eh... Solo hice una pregunta. No es como si estuviera acechándote."

misty angry ".{w=0.5}.{w=0.5}.{w=0.5}{nw}"
extend sadbrow @talkingmouth "Creo que exageré un poco."
misty -sadbrow @closedbrow talkingmouth "Ehm, perdón por...{w=0.5} gritarte así."

red @talkingmouth "No pasa nada.{w=0.5} Empecemos de nuevo."
red @talking2mouth "¿Qué estabas haciendo?{w=0.5} No parece que fueras a nadar con ese conjunto caro de Ciudad Celeste."

misty @closedbrow talkingmouth "Sí, no. Estaba comprobando si la piscina es segura para los Pokémon. Así es como puedes saber si es una buena piscina o no."

red @talking2mouth "¿Ah, sí? ¿Y qué hace que una piscina sea segura para los Pokémon?"

misty @talking2mouth "Básicamente, que no tenga químicos agresivos ni limpiadores fuertes. Muchos Pokémon nadan con los ojos abiertos o absorben agua a través de la piel."
misty @happy "Ellos no quieren que ácidos o bases fuertes se filtren en su cuerpo. No los mataría, pero un Wooper podría enfermarse gravemente con eso."
misty @closedbrow talkingmouth "Bueno, un Wooper de Johto sí. Los de Paldea pueden filtrarlos. Diferencias en la estructura de las branquias."

red @talking2mouth "Pareces muy bien informado. ¿Tienes mucha experiencia con los tipos de agua?"

misty @angrybrow talkingmouth "¿Y quién no? ¡Están por {i}todas{/i} partes!{w=0.5} Son el tipo más común."

red @happy "Estas desviando el tema."

pause 1.0

misty surprisedbrow frownmouth @surprised "Uh, no, no estoy des--"

$ showredonly = True

brock @talkingmouth "{size=40}{i}¡Achú!{/i}{/size}"

show pool_corner

pause 1.0

show tinybrock behind pool_corner:
    subpixel True
    xpos 150 ypos 620
    ease 1.0 xpos 110 ypos 600

$ renpy.pause(1.5, hard=True)

misty angrybrow @talkingmouth "¡¿Quién esta...?!"

brock @talkingmouth "Uhhhh.{w=0.25}.{w=0.25}."

misty @talkingmouth "¿Qué haces escondido detrás de esa pared?{w=0.5}{nw}"
extend angry " ¡¿Estabas espiándonos?!"

show tinybrock:
    subpixel True
    xpos 110 ypos 600
    ease 0.5 xpos 105 ypos 570

brock @talkingmouth "¡Nngh! ¡Espera!{w=0.33} No es lo que parece..."

misty @talkingmouth "Pues, ¿qué parece?{w=0.5} Porque a mí,{nw}"
extend @talkingmouth " me da la impresión de que estabas esperando a que{w=0.25}.{w=0.25}.{w=0.5}{nw}"
extend @surprised sweat " a que.{w=0.25}.{w=0.25}."

pause 1.5

show misty:
    xpos 620
    ease 0.25 xpos 800

misty angry "... ¡¿Pensaste que me iba a meter a la piscina?! ¡¿Me estabas espiando por eso?!"

show misty surprisedbrow frownmouth with dis:
    xpos 800

brock @talkingmouth "Uhhhhh.{w=0.25}.{w=0.25}."

pause 1.5

brock @talkingmouth "Je,je,je."

show tinybrock:
    subpixel True
    xpos 105 ypos 570
    ease 0.2 xpos -100 ypos 575

misty surprisedbrow angrymouth "¡HEY! ¡Vuelve aquí!"

show misty:
    xpos 800 alpha 1.0
    parallel:
        ease 0.4 alpha 0.0
    parallel:
        ease 0.4 xpos -150

red @surprised "¡Espera!"

pause 1.0

redmind @thonk "Demasiado tarde.{w=0.5} Mierda, sí que corre rápido."
redmind @thinking "Creo que ya tuve suficiente de la piscina por hoy.{w=0.5} Mejor vuelvo otro día."

window hide

show blank2 with dis:
    alpha 1.0

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_21

stop music fadeout 1.5
$ renpy.pause(2.0, hard=True)

show night at vspaz

hide misty
hide tinybrock
hide pool_corner
hide pool

pause 3.5

############################################################################################################################################################################################################################
#### END OF DAY ############################################################################################################################################################################################################
############################################################################################################################################################################################################################

play music "Audio/Music/SoaringIllusions_Intro.ogg" noloop
queue music "Audio/Music/SoaringIllusions.ogg"

$ renpy.transition(dissolve)
show screen currentdate

$ showredonly = False

$ PlaySound("Door_Open1.ogg")
scene dorm_B norm with Dissolve(2.0)

hide blank2
hide night

$ renpy.music.play("Audio/Pokemon/pikachu_pikapika1.ogg", channel="altcry", loop=None)

pikachu happy_2 "¡Pika, pika!"

red uniform @talkingmouth "¡Hola! Ya volví."

show brendan at rightside with dis

brendan @happy "¡Hey, bro! Bienvenido de vuelta."

show calem at leftside with dis

calem @talking2mouth "Bienvenido de vuelta."
calem @closedbrow talkingmouth "[pika_name] estuvo esperando junto a la puerta otra vez.{w=0.5} Nunca he visto a un Pokémon tan ansioso por recibir a su entrenador."

red @sadbrow talkingmouth "¿Qué puedo decir?{w=0.5} Supongo que somos muy buenos amigos, ¿verdad, amiguito?"

$ PlaySound("pokemon/pikachu_fun1.ogg")

pikachu happy_3 "¡Pi-ka!"
    
calem @surprisedbrow frownmouth "[ellipses]"
calem @talkingmouth "Solo por curiosidad, [first_name], ¿pero siempre le hablas así a [pika_name]?"

red @confused "¿Así cómo?"

brendan @talking2mouth "Es como si...{w=0.5} asumieras que entiende todo lo que le dices."

calem @closedbrow talking2mouth "Lo he notado antes, con [starter_name] también, pero me parece que... ¿ambos realmente se entienden?"
    
red @talkingmouth "Bueno... sí. O sea, no entiendo todo lo que dice, pero hay tono de voz, lenguaje corporal, expresiones."

show calem surprisedbrow with dis
show brendan surprisedbrow frownmouth with dis

pause 1.0

calem -surprisedbrow @talkingmouth "¿Y también pasa con [starter_name]?"

brendan -surprisedbrow -frownmouth @talking2mouth "Amigo, lo tuyo es otro nivel..."
    
red @sadeyes confusedeyebrows talkingmouth "¿Es tan raro?{w=0.5} No he conocido a muchos entrenadores antes, así que siempre asumí que todos eran como [pika_name] y yo."
red @happy "¿Quizá porque [pika_name] y yo llevamos juntos desde que era niño?"

calem @talkingmouth "No, no creo que sea eso.{w=0.5} Eso no explicaría lo de [starter_name], al cual acabas de conseguir. Además, mi Pokémon y yo también tenemos cierta historia juntos."

red @talking2mouth "¿Tú también tienes un Pokémon de casa?"

calem @talkingmouth "Sí, mi Flabébé.{w=0.5} Me la regalaron mis padres después de uno de sus eventos en el extranjero cuando estaba en la primaria."
calem @happy "Aunque es algo... obstinada, los días son un poco menos monótonos con ella cerca."

brendan @talking2mouth "Sí, y yo tengo a mi Shroomish desde que era un niño.{w=0.5} May y yo lo atrapamos juntos en el Bosque Petalia cuando fuimos a visitar a mi papá."

brendan @happy "Ja, ja, ni siquiera sabíamos qué era un Shroomish, ¡pero queríamos un Pokémon sí o sí!{w=0.5} Nos tardamos días en decidir quién se lo quedaba."

red @talkingmouth "Vaya, es genial que tengan historias así. En mi caso, un día mi vecino me invitó a su casa y me entregó a [pika_name].{w=0.5} No tengo una historia emocionante como la de ustedes. De hecho, casi ni recuerdo ese día."
    
brendan @angrybrow happymouth "¡Vamos, no puedes pensar eso!{w=0.5} Todo el mundo tiene una historia que contar. Cómo conseguí mi Pokémon no debería afectar a nadie más."

calem @talking2mouth "Exacto, es absurdo compararnos. No hay dos vínculos entre humanos y Pokémon iguales.{w=0.5} Nuestra conexión con ellos es especial, y eso es lo que la hace valiosa."
calem @closedbrow talkingmouth "Cómo dos criaturas tan diferentes pueden entenderse y confiar la una en la otra tan implícitamente...{w=0.5} es un verdadero milagro del mundo. Lo siento por ponerme tan poético."

$ PlaySound("vibrate.ogg")
pause 1.5

calem @talkingmouth "Oh, es mi teléfono. Ya se está haciendo tarde, así que me iré a dormir.{w=0.5} No se queden despiertos hasta muy tarde, Brendan, [first_name].{nw}"
extend happy " Dicen que trasnochar es malo para la piel."

brendan @happy "Sí. Tengo que levantarme temprano para mi trote matutino.{w=0.5} ¡Buenas noches, ustedes dos!"
    
hide brendan
hide calem 
with dis

red @talkingmouth "De acuerdo, buenas noches, chicos."
red @happy "Ustedes también deberían dormir.{w=0.5} Yo iré a la cama en seguida."

$ renpy.music.play("Audio/Pokemon/pikachu_norm3.ogg", channel="altcry", loop=None)

pikachu neutral_2 "¡Pika!"

$ renpy.music.play(startercry, channel="altcry", loop=None)

$ starter_species_name = pokedexlookup(starter_id, DexMacros.Name)
$ starter_fragment = starter_species_name[:3]
starter @talkingmouth "¡[starter_fragment]!"

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_22

show blank2 with dis

redmind casual hatless @thinking "Pero antes, tengo que repasar mis trabajos de clase.{w=0.5} Todavía no sé cómo voy a pagar esto... ¡así que creo que lo mejor es hacer mis trabajos lo mejor que pueda!"
redmind @sadbrow frownmouth "Seguro hay algún tipo de beca para los mejores estudiantes... o al menos eso espero."

stop music fadeout 1.0
$ renpy.pause(0.5, hard=True)

jump day010407