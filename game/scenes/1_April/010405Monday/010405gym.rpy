label gym010405:

$ timeOfDay = "Noon"

play music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.0)

$ renpy.transition(dissolve)
show screen currentdate

scene gym with Dissolve(2.0)

$ renpy.pause(1.0, hard=True)

ethan uniform @talkingmouth "Así que este es el gimnasio.{w=0.5} Me pregunto si es un gimnasio oficial aprobado por la Liga Pokémon."

red uniform @talking2mouth "Lo más probable es que no. No leí nada de eso en la página web de la academia cuando estuve investigando."
red @closedbrow talkingmouth "Lo más seguro es que es solo otra sala lujosa para la colección de la academia.{w=0.5} Aunque, aparte de algunos estandartes viejos en las paredes, este lugar está bastante vacío en comparación con los demás."

ethan @surprised "¡¿Estandartes viejos?! Amigo, ¡esos son banderines de Campeones! ¡Solo se los dan a los ganadores de {i}al menos{/i} torneos nacionales!"

red @happy "Sí, pero al final del día, siguen siendo solo estandartes. Si fueran los Campeones reales colgando ahí arriba, tal vez me impresionaría."

pause 2.0

red @sad "Eso no sonó como lo imaginé."

ethan @talking2mouth "Sí, mejor... hagamos como que eso nunca pasó."

hide blank2

show brendan uniform happy with vardis(0.5):
    xpos (1/6) xzoom -1

show may uniform happy with vardis(0.75):
    xpos (2/6)

show leaf uniform flirt behind may with vardis(1.0):
    xpos (3/6)

show calem uniform happy behind leaf with vardis(1.25):
    xpos (4/6)

show hilbert uniform sad with vardis(1.5):
    xpos (5/6)

ethan @happy "¡Eh, mira, ahí está el resto de nuestro grupo!"

pause 1.0

show misty uniform with vardis(1.0):
    xpos (4.5/6)

red @talkingmouth "Oh, y ahí está Misty...{w=0.5} Espero que esté un poco mejor desde la última vez que la vi."

ethan @talkingmouth "¿Cuál es su historia?"

red @happy "Ojalá lo supiera."

if (GetElective("Water") > 0 or GetElective("Ice") > 0):
    red @talkingmouth "Aprendí más en nuestra electividad juntos de lo que sabía antes."

hide misty 
hide calem
hide cheren
hide hilda
hide hilbert
hide brendan
hide leaf
hide may
with dis

show flannery uniform with vardis(0.5):
    xpos (1/6)

show whitney uniform happy with vardis(0.75):
    xpos (2/6)

show gardenia uniform cocky with vardis(1.0):
    xpos (4/6)

show sabrina uniform behind gardenia with vardis(1.25):
    xpos (5/6) 

show skyla uniform with vardis(1.5):
    xpos 850 alpha 0.0
    pause 1.0
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        ease 0.3 xpos 950
        ease 0.3 xpos 900
        pause 0.3
        ease 0.3 xpos 870
        ease 0.3 xpos 920
        
show text "{size=70}{b}¿?{/b}{/size}":
    xpos 1200 ypos 400 alpha 0.0 zoom 1.0
    pause 2.5
    parallel:
        ease 0.5 alpha 1.0
        pause 1.0
        ease 0.5 alpha 0.0
    parallel:
        ease 2.5 xpos 1120 ypos 300 rotate 30 zoom 1.5

$ renpy.pause(1.5, hard=True)

ethan @talkingmouth "Guau, esta clase es enorme.{w=0.75} Ya empiezo a reconocer algunas caras."

hide flannery
hide whitney
hide gardenia
hide sabrina
hide skyla
with dis

show blue uniform with dis

red @talkingmouth "Mirá, [blue_name] está sentado solo. Eso sí que es sorprendente, a estas alturas, pensé que ya habría intentado rodearse de gente."

ethan @talkingmouth "¿Lo conocés?"

red @talkingmouth "Sí, tenemos algo de historia."

ethan @confused "Oh, ¿fueron pareja?"

red @happy "¡Ja! No, todavía conservo algo de dignidad. Créeme, su personalidad {i}no{/i} lo vale."

ethan @happy "No sé, siento que mis estándares podrían aprender a hacer limbo por ese tipo..."

pause 1.0

red @angrybrow talking2mouth "Ethan."
ethan @surprised "¿Eh? ¿Por qué tan serio de repente...?"
red @angrybrow talking2mouth "Te lo digo {i}completamente en serio{/i}, no te hagas eso a ti mismo."
ethan @winkeyes sadeyebrows sweat talking2mouth "¡Está bien, está bien! Te tomo la palabra."

hide flannery
hide whitney
hide gardenia
hide sabrina
hide skyla
hide text

hide blue with dis

red @talkingmouth "En fin, vayamos con nuestro grupo.{w=0.5} No quiero terminar como el Señor-Demasiado-Genial-Para-Tener-Amigos"

$ renpy.pause(1.0, hard=True)

hide blue

show bruno with dis:
    xpos 0.33

show alder happy with dis:
    xpos 0.66

alder @happy2 "Muy bien, muy bien. Cálmense."

$ renpy.music.stop(channel='crowd', fadeout=1.5)

redmind @thonk "¿Estos son estos nuestros profesores?{w=0.5} El tipo de la izquierda definitivamente lo parece..."

show bruno think with dis:
    xpos 0.33

ethan @closedbrow talkingmouth "Pero el otro parece uno de esos ermitaños de montaña que ves en foros de supervivencia."

$ BecomeNamed("Alder")
$ BecomeNamed("Bruno")

alder @norm2 "¡Bienvenidos a la clase de gimnasia!{w=0.5} Yo soy Alder y él es Bruno."
alder @happy2 "Seremos sus instructores este año."
alder @norm2 "Apuesto a que se están preguntando qué van a hacer en esta clase.{w=0.5} Bueno, será como cualquier otra clase de gimnasia que hayan tenido en sus escuelas anteriores."    
alder @happy2 "Excepto que no los vamos a hacer cambiarse de ropa y jugar deportes.{w=0.5} Nos enfocaremos más en entrenar a sus Pokémon, y no sus cuerpos."    
alder norm @norm2 "¡Pero entrenar el cuerpo también es importante, ja, ja!"

pause 1.5

alder @norm2 "Ejem. De todas formas, la verdadera razón por la que esta escuela tiene una clase de gimnasia de este tipo es para prepararlos para los gimnasios Pokémon reales cuando se gradúen.{w=0.5} Al menos para aquellos interesados en desafiar la Liga."
alder @happy2 "¿Alguien puede decirme por qué existen los Gimnasios en primer lugar?"

hide alder 
hide bruno 
with dis

show cheren uniform with dis:
    xpos 0.25
        
show hilda uniform behind cheren with dis:
    xpos 0.75
    
show serena uniform behind cheren with dis:
    xpos 0.5

cheren @talking2mouth "Los Gimnasios fueron creados para impedir que entrenadores sin la fuerza suficiente puedan desafiar las Ligas Pokémon."
    
serena @talkingmouth "Exacto. Sin los Gimnasios, cualquier entrenador podría intentar desafiar la Liga, saturando sus recursos."

hilda @closedbrow talking2mouth "Sí, ¡y también son un buen golpe de realidad para los que creen que pueden llegar a la Liga sin entrenar de verdad!"

hide hilda
hide cheren
hide serena
show alder happy:
    xpos 0.66
show bruno:
    xpos 0.33
with dis

alder @winkbrow talkingmouth "Bien, buenas respuestas...{w=0.5} pero el propósito principal de un Gimnasio es permitir que entrenadores menos experimentados pongan a prueba sus habilidades contra otros más experimentados en igualdad de condiciones."

hide cheren
hide hilda
hide serena

alder @happy2 "Y eso es exactamente lo que haremos en esta clase."
alder @talkingmouth "Todos tendrán al menos una batalla al día. Pero no empezaremos con eso {i}de inmediato{/i}."
alder @spunky2 "Primero, tenemos que repasar lo básico.{w=0.5} Todos ustedes están tan ocupados tratando de aprender cosas nuevas que a veces se olvidan de las habilidades más fundamentales."

leaf uniform @surprised "¿Qué, nos vas a enseñar a atrapar Pokémon o algo así?"

show bruno think with dis

alder norm @happy2 "¡Sí! ¡Es una parte muy importante del plan de estudios!"

leaf @sadmouth "Ay, por favor..."

alder @happy2 "Incluso si algunos creen que ya saben todo sobre las batallas Pokémon, créanme cuando les digo que no es así."
alder @happy2 "Llevamos mucho más tiempo en esto que ustedes, y aun así, ni {i}nosotros{/i} lo tenemos dominado a la perfección, ¡ja, ja!"

show alder happy with dis

show blue uniform angry behind alder with dis:
    xpos 0.95 xzoom -1 zoom 0.9

redmind @thinking "Como esperaba, [blue_name] parece un poco molesto por lo que acaba de decir Alder."
redmind @sad "Espero que no haga una escena como en la clase general."

hide blue with dis

alder @surprised2 "Oh, perdón por hablar tanto."        
alder @happy2 "Uhhh, ¡Bruno!{w=0.5} ¿Por qué no les cuentas más sobre esta clase?"

bruno @think2 "Muy bien."    
bruno @norm2 "Este gimnasio fue diseñado principalmente como un campo de entrenamiento para los estudiantes, y como tal, está disponible para su uso gratuito fuera del horario de clases."
bruno @think2 "Solo deben traer su identificación de estudiante y tendrán acceso ilimitado a sus instalaciones."
bruno @talkingmouth "Además de las máquinas disponibles, el gimnasio cuenta con varios simuladores de batalla para que los estudiantes experimenten en tiempo real cómo se siente un combate Pokémon."
bruno @sadbrow talkingmouth "Son útiles en caso de que quieran entrenar con escenarios fuera de su dominio actual."
bruno @talkingmouth "En su tiempo libre, también pueden realizar batallas aquí, ya sean simuladas o reales. Otro lugar donde pueden realizar combates es en el Salón Batalla."
bruno @think2 "Sin embargo, los miembros del equipo de batalla tienen prioridad para usar el Salón Batalla."

blue uniform @talkingmouth "¿Equipo de batalla? ¿De qué trata eso?"

bruno @closedbrow talkingmouth "Nuestra academia tiene un equipo de combate competitivo para los estudiantes que quieren llevar su entrenamiento al siguiente nivel."
bruno @closedbrow happymouth "Tienen el honor y privilegio de representar a Kobukan en competiciones nacionales e internacionales."
bruno @angrybrow talkingmouth "Es un club muy selectivo, así que no piensen en inscribirse tan a la ligera."

blue @angrybrow talking2mouth "¿Ah, sí?{w=0.5} ¿Y qué se necesita para entrar? ¿Calificaciones impecables? ¿Un equipo fuerte?"

bruno @think2 "Nada tan concreto, solo deben impresionar al capitán del equipo de batalla."

blue @happy "¡Ja! ¡Eso es fácil!"

bruno @closedbrow talking2mouth "Hmm."
bruno -think @closedbrow smilemouth "Puedes poner a prueba esa suposición cuando gustes."

blue @happy "Vamos, ¿qué tan difícil puede ser? Solo tengo que impresionar al capitán. ¡Si tiene ojos, se va a impresionar cuando me vea!"

alder -happy @sadbrow talkingmouth "Ten cuidado con lo que dices.{w=0.5} La arrogancia y la fuerza no van de la mano."

blue @happy "Te digo que va a ser pan comido.{w=0.5} ¿Quién está a cargo del equipo?"

$ showredonly = True

lance @talking2mouth "Mi ahijada."

show bruno: 
    xpos 0.33
    ease 0.5 xpos 0.25

show alder:
    xpos 0.66
    ease 0.5 xpos 0.75

show lance with dis:
    xpos 0.9 zoom 1.15
    ease 0.75 xpos 0.5 zoom 1.0

pause 1.5

$ showredonly = False

calem uniform @surprised "¿Q-qué?"

red @confused "Espera, ¿quién es este tipo? Me resulta familiar. ¿Lo vi en un periódico?"

$ BecomeNamed("Lance")

ethan @surprised "¡Bro! ¡¿Qué no usás internet?! ¡Ese es Lance, el campeón de la Liga Índigo! {i}Nuestra{/i} Liga."

red @happy "Entonces, supongo que [blue_name] debería cuidar lo que dice frente a él."
    
lance @talking2mouth "Ser aceptado en el equipo de batalla es uno de los mayores honores que un estudiante puede recibir en esta academia.{w=0.5} No es algo que deba tomarse a la ligera."

bruno @norm2 "Lance.{w=0.5} ¿Cuánto tiempo llevas ahí parado?"

lance @talking2mouth "Solo estaba de paso.{w=0.5} Ha pasado un buen tiempo, Bruno. Alder."

alder @happy2 "¡Ja! Sí que ha pasado."

alder @happy2 "Oh, dónde están mis modales...{w=0.5} Estudiantes, él es Lance, el asesor del equipo de batalla."

lance @talking2mouth "Un placer conocerlos a todos."
lance @closedbrow talking2mouth "Así que estos son los nuevos estudiantes...{w=0.5} Parecen bastante capaces."
lance angrybrow @talking2mouth "Espero grandes cosas de algunos de ustedes.{w=0.5} Janine ciertamente--"
    
blue cocky "¡Oye!, ¿tú eres el que dirige el equipo de batalla?"

lance @angrybrow talking2mouth "...{w=0.5} Sí. Y deberías prestar atención a los consejos de Alder y Bruno."

lance @closedbrow talking2mouth "Para alguien en tu nivel actual, sería imposible entrar."
    
blue angry "...{w=0.5} ¿Qué acabas de decir?"

redmind @upeyes frownmouth angryeyebrows "Aquí vamos..."
    
blue @angry "¡Solo porque eres un gran campeón no significa que puedes menospreciarme!"

lance @closedbrow talking2mouth "No soy un 'gran campeón', ni te estoy menospreciando.{w=0.5} Simplemente expongo los hechos."

lance @talking2mouth "... De todos modos, voy con prisa.{w=0.5} Tengo asuntos que atender y no puedo llegar tarde."

alder @happy2 "Está bien, fue bueno verte de nuevo, Lance." 
alder @sadbrow happymouth "Sabes, podrías pasarte por los dormitorios del personal de vez en cuando. Lenora dara una fiesta antes del Día Primaveral, y--"

lance @talking2mouth "Mi opinion sobre estas cosas es muy evidente. Cuídense, Alder. Bruno."

hide lance with dis

pause 0.5

show bruno:
    xpos 0.25
    ease 0.5 xpos 0.33

show alder:
    xpos 0.75
    ease 0.5 xpos 0.66

blue angrybrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
blue angry "{size=30}Ya verás, aclamado 'campeón'.{/size}"

alder @happy2 "¡Ya lo escucharon!{w=0.5} ¡El equipo de batalla es cosa seria!"
alder @talkingmouth "Después de todo, no es coincidencia que nuestra academia haya formado a la mayor cantidad de Campeones Mundiales y miembros del Alto Mando, además de ser la que más victorias tiene en el Torneo Nacional."

alder @happy "Pero bueno, no deberían preocuparse por esas cosas. ¡Al menos no todavía!"
alder @closedbrow talking2mouth "Hay cosas mucho más importantes de las que ocuparse, después de todo."

show bruno think with dis

alder @happy2 "¡Como graduarse a tiempo, je je!"

pause 1.5

alder @happy2 "Bueno, eh, creo que eso cubre todas las cosas aburridas. Sigamos adelante."

show blank2 with dis

narrator "A pesar de que Alder afirma que ya terminaron con la 'parte aburrida y formal', notas que más de un compañero de clase lucha por contener un bostezo mientras la lección continúa."
    
hide blank2 with dis

window hide
$ renpy.music.set_volume(0.1, delay=1.0, channel="music")
$ PlaySound("BellChime.ogg")

$ renpy.music.stop(channel='misc', fadeout=1.0)

$ renpy.pause(2.0, hard=True)
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

alder norm @happy2 "Muy bien, eso es todo por hoy. Créanme, me {i}encantaría{/i} saltar directamente a las batallas, pero las clases deben seguir hasta que mejoren los ánimos."

show bruno think with dis

alder @talkingmouth "En la próxima clase hablaremos sobre los fundamentos de las batallas Pokémon y cómo lidiar con Pokémon salvajes."

show bruno with dis
    
bruno @think2 "Será una revisión, pero no subestimen la importancia de los fundamentos."

alder @happy2 "De acuerdo.{w=0.5} Bueno, ¡hasta luego, estudiantes! Disfruten el resto de su día."

call clearscreens from _call_clearscreens_237
hide alder
hide bruno
show blank2
with dis

ethan uniform @talkingmouth "Parece que... ¡lo siguiente en nuestra agenda es el almuerzo! Tengo que ocuparme de algo en las oficinas, así que vayan ustedes sin mí, ¿vale?"

red @talkingmouth "Okay, cuidate."

hide bruno
hide alder
hide bianca
hide cheren

window hide
stop music fadeout 1.0
$ renpy.pause(1.0, hard=True)

show cafe behind blank2
show afternoon at vspaz
    
pause 3.5

call freeroam from _call_freeroam_18