label secondhomeroom010408:

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=True, fadein=1.0, tight=None)

scene blank2

show oakbg behind blank2
show homeroom behind oakbg

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with dis

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)
    
show homeroom behind oakbg

oak @talkingmouth "... Y con esto concluimos la lección de hoy."

redmind uniform @thinking "¡Por fin! Sam siempre es entretenido de escuchar, pero después de veinte minutos de clase ya empiezo a soñar despierto, y ni hablar de cuatro horas."
redmind @thonk "Espera... ¿Hoy no tocaba uno resolver un cuestionario?"

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.5)
narrator "A pesar de tus dudas, todos empiezan a levantarse de sus asientos y se dirigen a la salida."

$ renpy.music.stop(channel='crowd', fadeout=1.5)
oak @talkingmouth "¡No tan rápido! Aún no termina la clase.{w=0.5} Espero que no hayan olvidado los {color=#0048ff}cuestionarios de los Lunes y Jueves{/color}."

show flannery uniform with dis:
    xpos 0.66

flannery @surprised "Oh... ¡¿Qué!?{w=0.6}{nw}"

extend sadbrow frownmouth @angry " ¡Whitney! Dijiste que eran los Lunes y los {i}Viernes{/i}."

show whitney uniform with dis:
    xpos 0.33

whitney @talking2mouth "Oops, ¿de verdad dije eso?{w=0.6}{nw}"

extend happybrow @happy " Oh bueno, ¡si estudiaste, no tendrías de qué preocuparte!"

flannery @sad "Oh noooo..."

hide flannery
hide whitney
with dis
    
oak @talkingmouth "Bien, clase. Limpien sus escritorios y saquen sus lápices." 
oak @talkingmouth "El cuestionario de hoy es bastante sencillo. Aun así, asegúrense de analizar el estado del campo, su oponente y ustedes mismos antes de elegir un movimiento."
oak @talkingmouth "Recuerden, {color=#0048ff}¡esto cuenta para la nota final!{/color}"

$ trainer1 = Trainer("red", TrainerType.Player, [Pokemon(pokedexlookupname("Deino", DexMacros.Id), level=5, moves=[GetMove("Tackle"), GetMove("Dragon Rage"), GetMove("Focus Energy"), GetMove("Draco Meteor")])])
$ trainer2 = Trainer("oak", TrainerType.Enemy, [Pokemon(pokedexlookupname("Klink", DexMacros.Id), level=15, moves=[GetMove("Vise Grip")], ability="Plus")])

$ trainer1.GetTeam()[0].Health = 1
$ trainer2.GetTeam()[0].ChangeStats(Stats.Speed, -6, trainer2.GetTeam()[0])
$ trainer2.GetTeam()[0].Health = 40
$ trainer2.GetTeam()[0].Stats[Stats.Health] = 40

call Battle([trainer1, trainer2], clearstats=False, gainexp=False, healParty=False, uniforms=[True, False], lockbag=True) from _call_Battle_5
$ battlehistory["Oak1"] = _return

$ renpy.transition(dissolve)
show screen currentdate

if (WonBattle("Oak1")):
    red uniform @happy "¡Eso estuvo bastante fácil! Menos mal que ese Klink estaba ralentizado, porque cualquier ataque suyo me habría dejado fuera de combate si atacaba primero."
else:
    red uniform @sad "Oh, hombre... Sabía que tenía que debilitar a ese Klink antes de que me atacara, pero pensé que tenía más tiempo..."

oak @talkingmouth ".{w=0.5}.{w=0.5}.{w=0.5}"

pause 0.5

oak @talkingmouth "A simple vista..."

pause 0.5

if (WonBattle("Oak1")):
    oak "Parece que a todos les fue bastante bien. Veo que entendieron la importancia de los movimientos de daño fijo. También hay otros ataques que ignoran las defensas."
    oak "Estoy deseando ver como los pueden llegar a utilizar."
else:
    oak "Les recomiendo que presten más atención al estado del campo de batalla antes de elegir un movimiento." 
    oak "Dependiendo de cuantos PS les quede o los cambios de estadísticas entre ustedes y su oponente, deberán determinar si deben luchar manera más o menos agresiva."

oak @talkingmouth "Eso es todo por hoy, clase. {w=0.5} Ahora sí, pueden retirarse."

show oakbg:
    alpha 1.0
    ease 0.5 alpha 0.0

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.5)

redmind @thinking "¡Por fin! Estoy tan agotado que, por primera vez, ni siquiera me importa hablar con Sam, solo quiero salir de aquí."

hide oakbg

show oak:
    xpos 450 alpha 0.0
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        ease 1.5 xpos 720
    
pause 0.5

oak @talkingmouth "[first_name], es hora. {w=0.5} Ven a mi laboratorio en el Centro de Investigación ahora, por favor."

show oak:
    alpha 1.0 xpos 720
    
red @talkingmouth "Eh… Claro, profesor."

show oak:
    xpos 720 alpha 1.0
    parallel:
        ease 0.75 alpha 0.0
    parallel:
        ease 1.0 xpos 900

pause 1.5

hide oak

show blue uniform:
    alpha 0.0 xpos 400
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        ease 0.75 xpos 720
    
blue @talkingmouth "Ni siquiera ha pasado una semana y ya te metiste en problemas.{w=0.5} ¿Qué hiciste ahora?"
    
red @angrybrow talking2mouth "Oh, déjame en paz. Seguro no es nada."

show blue happy:
    alpha 1.0 xpos 720
    ease 0.5 alpha 0.0 xpos 500
    
redmind @thinking "... De repente, todo mi cansancio desapareció."
redmind @happy "De acuerdo, dijo el Centro de Investigación, ¿no?{w=0.5} Si empiezo a correr ahora, podría recorrer todo el campus en--"

show hall_A2b at sepia with dis

$ renpy.pause(1.0, hard=True)

show leaf angrybrow angrysmilemouth at sepia, dissolvein behind flashback

pause 0.5

leaf @talking2mouth "Usa. El. Folleto. ¡Tiene un mapa!"

show blank with splitfade

hide leaf
hide hall_A2b
hide flashback
hide blank with dis

pause 1.5

redmind @happy "...Sí, tienes razón, Leaf que vive en mi cabeza."

redmind @thinking "[ellipses]"
redmind @thinking "Pensándolo bien, Leaf ha estado invitándome a salir desde que empezó el semestre. Tal vez esta vez debería invitarla yo."

menu:
    ">Invitar a Leaf":        
        show leaf uniform with dis:
            xpos 700
            
        red @talkingmouth "Hey."

        leaf @happy "Oh, ¡hola [first_name]!{w=0.5} ¿Qué hay?"
        
        red @talkingmouth "Voy a ir al Centro de Investigación, quería dar una vuelta y luego hablar con Sam."

        show leaf surprisedbrow frownmouth with dis

        red @happy "El otro día parecías sorprendida de lo cercanos que somos Sam y yo, así que pensé que tal vez te interesaría acompañarme."
        
        leaf -surprisedbrow -frownmouth @happy "¡Oh, me encantaría ir!{w=0.5}{nw}"
        
        show leaf:
            xpos 700
            ease 0.5 xpos 750
            
        extend @talkingmouth " ¿Sabías que cuando era niña me encantaban las cosas científicas?{w=0.5}{nw}"
    
        show leaf:
            xpos 750
            ease 0.5 xpos 700
        
        extend @happy " Sobre todo paleobiología, ¡pero apuesto a que las otras 'ologías' son igual de geniales!"
        
        red @happy "Genial, entonces, ¿vamos?"
        
        leaf @embarrassedbrow talkingmouth "Me encantaría, peeero... hoy no puedo.{w=0.5}{nw}"
        extend @blush embarrassedbrow talking2mouth " Le pedí a May que estudiara conmigo después de que fallar en el cuestionario. La instructora Clair mencionó algo sobre Furia Dragon, pero... ¡Lo siento mucho!"
        
        red @talkingmouth "No te preocupes, siempre hay otra ocasión."
        
        leaf @flirttalk "Sí, lo haremos la próxima vez.{w=0.5} Te lo prometo."
        
        $ ValueChange("Leaf", 1, 700/1920)
        $ BecomeContacted("Leaf")

        leaf @happy "Y ahora, la próxima vez que quieras invitarme a algo, puedes simplemente llamarme."
        leaf @flirttalk blush "¿No eres un chico afortunado?{w=0.5} ¡Nos vemos, [first_name]!"
        
        hide leaf with dis
            
        pause 1.0
        
        redmind @happy "Je, probablemente no me había invitado antes porque tenía cosas que hacer.{w=0.5} Bueno, al menos lo intenté."
        redmind "Muy bien, debería ir yendo."       
        
        hide leaf
        
    ">Pensándolo bien...":        
        redmind @thinking "Nah, voy a hablar con Sam sobre cosas serias, cosas como: '¿cómo diablos logré entrar en esta academia?'"
        redmind @thinking "Francamente, no estoy seguro si quiero que ella escuche eso..."

window hide

show blank2:
    alpha 0.0
    pause 0.5
    ease 1.5 alpha 1.0

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_36
$ renpy.music.stop(channel='crowd', fadeout=1.5)
stop music fadeout 1.5
$ renpy.pause(2.5, hard=True)

############################################################################################################################################################################################################################
#### 2. RESEARCH CENTER ####################################################################################################################################################################################################
############################################################################################################################################################################################################################

queue music "audio/music/power plant_start.ogg" noloop fadein 1.0
queue music "audio/music/power plant_loop.ogg"

$ renpy.transition(dissolve)
show screen currentdate

scene research with Dissolve(2.0)

hide blank2

pause 0.5

redmind uniform "¡Estoy impresionado! Es como el laboratorio del Profesor Oak en casa, pero diez veces más grande y limpio. ¿Por qué demonios Sam siempre vuelve a Pueblo Paleta?"

show bianca uniform happy:
    alpha 0.0 xpos -250 ypos 1.1 zoom 1.0
    ease 0.3 alpha 1.0 xpos 740
    ease 0.2 zoom 1.2 xpos 700 ypos 1.0

bianca @talkingmouth "¡[first_name]!{w=0.5} ¿Eres tú?"

show bianca happy:
    xpos 700 zoom 1.2 alpha 1.0
    
red @talkingmouth "El único e inigualable,{w=0.5} no esperaba verte por aquí."

bianca -happy @talkingmouth "¡Yo tampoco! Bueno, quiero decir, ¡no esperaba verte a {i}ti {/i} here!{w=0.5} aquí! ¡Siempre estoy por aquí ayudando a Nate en el laboratorio! Bueno, siempre y cuando no estoy ayudando a Cheren."
$ natenamed = persondex["Nate"]["Named"]
if (natenamed):
    red @talkingmouth "Oh, ¿Nate está aquí?"

    show bianca:
        xpos 700 zoom 1.2
        ease 0.5 xpos 720 zoom 1.0

    bianca @talkingmouth "¡Sí!"

else:
    red @talkingmouth "¿Ah, sí? Eh... ¿Quién es Nate?"

    show bianca:
        xpos 700 zoom 1.2
        ease 0.5 xpos 720 zoom 1.0
    
    bianca @talkingmouth "Es un amigo de Teselia.{w=0.5} ¡Es súper inteligente!"

show bianca:
    xpos 720 zoom 1.0
    
bianca @talkingmouth "Pero bueno, ¿qué te trajo al Centro de Investigación tan de repente?"

red @talkingmouth "Bueno, Sam me pidió que viniera a hablar sobre algo. Eh, quiero decir, el Profesor Oak."

bianca @talkingmouth "¡Oh, qué genial!{w=0.5}{nw}"

show bianca happybrow talkingmouth:
    subpixel True
    
    block:
        ease 0.12 ypos 1.12 xpos 650
        ease 0.1 ypos 1.0
        repeat

extend @talkingmouth " {cps=140}{size=30}¡Estoy aquí porque hoy el Centro de Investigación ha traído a Magnemite y Voltorb y vamos a ver cuánta energía pueden almacenar en una bombilla! Oh, pero no vamos a usarlos como mano de obra esclava ni nada de eso, caramba, Dios, no, eso sería horrible...{/size}{/cps}"

redmind "[ellipses]"

bianca @talkingmouth "{cps=140}{size=30}iensa en esto como un tipo de entrenamiento o acondicionamiento para Pokémon como Magnemite o Voltorb. También escuché que, como técnicamente no tienen fibras musculares ni nada de eso, el uso de su electricidad aumenta su afinidad natural con...{/size}{/cps}"

show bianca -happybrow -talkingmouth:
    xpos 650 ypos 1.0
    ease 0.5 xpos 720 zoom 1.0

$ showredonly = True
    
nate uniform "¡Eh, B! ¿Estás mareando a otro invitado con tu verborrea?"

#### Nate INTRO ################################################################################################

show bianca:
    xpos 720 zoom 1.0
    ease 0.5 xpos 900

show nate uniform with dis:
    xpos -100
    ease 1.25 xpos 450

nate @happy "¡Tienes que bajar un poco tus decibeles, B! Nunca voy a conseguir otro asistente si sigues dandole a los invitados mucho texto."

$ showredonly = False

bianca @happy "¡Pero no necesitas otro asistente! ¡Me tienes a mí!"

nate @talking2mouth "Solo a medio tiempo." 
nate @winkbrow talkingmouth "Por mucho que me encantaría tener toda tu atención solo para mí, sé que tienes algo con Cheren."
nate @happy "A {i}mí{/i} no me importa compartir, pero creo que a Cheren sí."

pause 2.0

show bianca surprisedbrow frownmouth
show nate surprisedbrow frownmouth
with dis

red @talkingmouth "Ejem."

show bianca -surprisedbrow -frownmouth -surprised
show nate -surprisedbrow -frownmouth -surprised
with dis

$ name_fragment = first_name[0]
if (persondex["Nate"]["Named"]):
    nate @talkingmouth "¡Hola! [first_name], ¿verdad?"

else:
    $ BecomeNamed("Nate")

    nate @talkingmouth "¡Hola! Lo siento, pero ¿qué sigue despues de conocer a alguien? Nombres, ¿verdad? Me llamo Nate. ¿Qué tal?"

    red @talkingmouth "[first_name], es un placer conocerte."

nate @happy "¡Me alegro de tenerte aquí! Veo que tú y Bianca ya se conocen."

red @closedbrow talking2mouth "Sí, Bianca me ha atrapado un par de veces para hablar con Cheren."

nate @talkingmouth "Genial, genial... En fin, bienvenido al Centro de Investigación."
nate @happy "Aunque, para un estudiante promedio, no hay mucho aquí. Pero si estás interesado en computadoras o en hacer experimentos, este es el lugar indicado."

show nate surprisedbrow frownmouth with dis

red @confused "Bueno, ¿tú en cuál de esas categorías entras?"

pause 1.0

nate -surprisedbrow -frownmouth @closedbrow talking2mouth "Observador, ¿eh? Bueno, básicamente estoy aquí solo para usar las computadoras. Trabajo en temas de redes y esas cosas."
nate @happy "¡Piensa en mí como el técnico no reconocido y sin sueldo de la academia!"

show bianca:
    subpixel True xpos 900
    block:
        ease 0.15 ypos 1.12
        ease 0.1 ypos 1.0
        repeat 3

bianca @talkingmouth "¡Sí! ¡Nate es un súper genio! ¡Sabe programar, hackear, reparar, depurar, desfragmentar, desfibrilar, defenestrar y...!"

nate sweat @angrybrow talking2mouth "B, ¿por qué no... hablamos un poquito menos, sí?"

bianca @happy "O-kay!~"

nate -sweat surprisedbrow frownmouth @neutraleyes talkingmouth "Lo siento por eso, [name_fragment]. La verdad, solo soy un simple técnico, así que, si tienes una tostadora que necesita arreglo, {i}ese es{/i} el tipo de cosas que sé hacer."

$ PlaySound("vibrate.ogg")
pause 1.5

nate @surprised "Oh, es para mí. Lo siento, pero tengo que atender esto."
show nate happy with dis

red @talkingmouth "Nos vemos."

show nate at dissolveaway:
    xpos 450

pause 2.0

nate @closedbrow talking2mouth "{size=35}¿Diga? {size=32}Por {size=29}supuesto, {size=26}señor... {size=23}Todo {size=20}está {size=17}en orden..."

pause 2.0

bianca @happy "¡A Nate siempre lo molestan con llamadas!" 
bianca @surprised "¡Y luego se pone súper serio por un par de minutos!"
bianca -happy @happy "¡Y ya a lo último, vuelve a la normalidad!"

pause 1.0

red @talkingmouth "Entonces, ¿cómo se conocieron? Pensé que tú y Cheren eran amigos de la infancia, pero parece que tú y Nate también."

bianca @talkingmouth "¡Sípi! De hecho, Cheren y yo somos de Pueblo Arcilla. Luego nos mudamos a Ciudad Engobe, y ahí conocimos a Nate."
bianca @surprised "Nate was barely ever home, though! I think I've talked to him more in the last four days than I ever had before!"

red @closedeyes talkingmouth "Así que... en realidad no lo conoces tan bien. ¿Pero igual lo ayudas con su 'cosa de computadoras'?"

bianca @happy "¡Supongo que no! ¡Y supongo que sí!"

red @confusedeyebrows talkingmouth "¿Y lo de estar aquí todos los días es por qué...?"

bianca @happy "¡He venido todos los días desde que inició el semestre hasta ahora!"

red @closedbrow talking2mouth "Hmm. Bueno, eh... {w=0.5}{nw}" 
extend @happy " ¡Me alegra saber que nos veremos más seguido!"
    
bianca @talkingmouth "¡Yay!"
bianca @surprised "¡Oh! Dijiste que querías ver al Profesor Oak, ¿verdad? Está por el pasillo, a la izquierda."

red @happy "¡Gracias!"

bianca @happy "¡No hay de qué!~♪"

show bianca happy:
    alpha 1.0 xpos 900
    ease 0.5 alpha 0.0 xpos 300

pause 0.5

show blank2 with splitfade

$ renpy.pause(1.5, hard=True)

stop music fadeout 1.0

show text "{color=#ffffff}.{/color}" as text1:
    alpha 1.0
    pause 0.5
    ease 0.0 alpha 0.0
show text "{color=#ffffff}..{/color}" as text2:
    alpha 0.0
    pause 0.5
    block:
        ease 0.0 alpha 1.0
        pause 0.5
        ease 0.0 alpha 0.0
show text "{color=#ffffff}...{/color}" as text3:
    alpha 0.0
    pause 1.0
    block:
        ease 0.0 alpha 1.0
        pause 1.5
        ease 1.0 alpha 0.0
    
$ renpy.pause(3.0, hard=True)

hide nate
hide bianca

hide text
hide text1
hide text2
hide text3

$ renpy.music.queue("Audio/Music/OakTheme_Start.ogg", channel='music', loop=None, tight=None)
$ renpy.music.queue("Audio/Music/OakTheme_Loop.ogg", channel='music', loop=True, tight=None)

hide blank2 with splitfade

#### MEET OAK ################################################################################################

show oak with dis:
    xpos 0.5

oak @talkingmouth "Ah [first_name],{w=0.5} gracias por haber venido."

red @talking2mouth "Hey Sam,{w=0.5}" 
extend @talkingmouth " Hey Sam, me alegra que por fin podamos hablar. ¿Qué vas decirme?"

oak @happy "Déjame responder esa pregunta con otra pregunta.{w=0.5} ¿Sobre qué crees que {i}tenemos{/i} que hablar?"

red frownmouth @talking2mouth "... Sobre el porqué estoy en esta academia."

oak @closedeyes talkingmouth "Sí, puedo imaginar que pensarías que sería necesario discutirlo."

red @talking2mouth "Sam, por favor, solo dame una respuesta directa. ¿Por qué estoy aquí? y ¿Por qué no me dijiste que estarías aquí?"

oak @angrybrow frownmouth "[ellipses]"

oak @talking2mouth "Te daré una respuesta, [first_name] [last_name]. Pero tendrás que ganártela."

red @angrybrow frownmouth "[ellipses]"

red @happy "Sí, claro. Típico movimiento de Samuel Oak. Nunca entregas nada fácilmente, ¿verdad?"

oak @closedeyes talkingmouth "No, no lo hago."

show flashback with dis

red @closedbrow talking2mouth "Bien, aquí están los hechos: estoy en la Academia Kobukan y tú enseñas aquí. No me lo dijiste, aunque tuviste mucho tiempo para hacerlo."
red @closedbrow talking2mouth "Así que no {i}querías{/i} que lo supiera. Sin embargo, sabías cuánto significaba para mí entrar en Kobukan."
red @closedbrow talking2mouth "Y sabías que si yo supiera que trabajabas aquí, te pediría ayuda para entrar."
red @closedbrow talking2mouth "Entonces, no querías que te pidiera ayuda. Eso significa que o no querías ayudarme, o... no querías que te pidiera ayuda."

pause 1.0

$ PlaySound("idea.ogg")

hide flashback with dis

red @happy "¡Oh, claro, ahora lo entiendo!"

show oak surprisedbrow frownmouth with dis

red @talkingmouth "No querías que te pidiera ayuda para entrar porque entonces tendrías que elegir entre recomendar a Blue o a mí."

pause 2.0

oak -surprisedbrow -frownmouth -surprised @closedeyes talkingmouth "En realidad, estas completamente equivocado..."

red @surprised "¿Qué?"

oak angrymouth @talking2mouth "Chico, nunca tuve intención de recomendar a mi nieto a esta escuela."

red @surprised "¡¿QUÉ?! Pero... ¿por qué...? ¿Por qué no?"

oak @angrybrow frownmouth "[ellipses]"
oak @angrybrow talking2mouth "Haz tu mejor esfuerzo para responder esa pregunta y, solo entonces, te daré mi respuesta."

redmind @thinking "Ugh, otra vez con esto..."

red @closedeyes talking2mouth "Bueno... ¿Pensaste que podría entrar en esta escuela sin tu ayuda? ¿Y querías darle confianza, hacerle saber que no necesita depender de tu nombre?"

oak @closedeyes talking2mouth "Una vez más, totalmente incorrecto."

red @sad "Entonces... ¿por qué?"

oak @closedeyes talkingmouth "¿Por qué no intentas responder eso? Solo entonces--"

show oak surprisedbrow frownmouth with dis

red @angry "¡Solo responde la pregunta, Sam!"

pause 1.0

show oak angry with dis

pause 2.0

red @sad "¿Por favor?"

oak angrybrow angrymouth @talking2mouth "No creo que mi nieto merezca su lugar en esta academia."

red @surprised "¿Eh?"

oak @talking2mouth "Es arrogante, cruel y se niega por completo a aprender, incluso de aquellos que saben más que él."
oak @closedeyes talking2mouth "Además, aunque lo he intentado, apenas tengo una relación con el chico. Me llama en los días festivos en los que se supone que debo enviarle dinero, y eso es todo."
oak @talking2mouth "Su habilidad para entrenar Pokémon es innegable, pero eso no excusa su cruel desprecio hacia los demás."

oak @sad "Lamentablemente, sé muy bien de dónde sacó estas actitudes. No fui el mejor padre para {i}su{/i} padre... pero aun así."

oak -angrybrow -angrymouth @closedeyes talking2mouth "En cualquier caso, chico, no considere a Blue como un factor en mi silencio sobre este asunto."

red @surprised "Entonces... ¿no me lo dijiste porque, de todas formas, ibas a recomendarme?"

oak @happy "¡Ahí lo tienes!"

red @sad "Pero Sam, pasé tanto tiempo escribiendo esas cartas, solicitando, preocupándome por si entraría o no..."

oak @happy "Bueno, si te hubiera dicho que iba a recomendarte, quizás no te habrías esforzado tanto." 
oak @angrybrow happymouth "En cualquier caso, tienes dieciocho años, terminaste el bachillerato y estás desempleado. No puedo imaginarme que ese tiempo perdido hubiera tenido un buen uso. Asumo que lo máximo que esto produjo fue que te perdieras una o dos carreras matutinas, ¿no?"

red @angry "¡De hecho, sí!."

oak @closedeyes talking2mouth "Difícilmente es algo por lo que valga la pena preocuparse en este punto."

red @closedeyes talking2mouth ".{w=0.25}.{w=0.25}.{w=0.25} ¿Podrías ser un poco más empático?"

oak @talking2mouth "No con lo limitado que es {i}mi{/i} tiempo."
oak @talkingmouth "Hablando de eso, creo que ahora tienes suficiente evidencia para responder tu primera pregunta: '¿Por qué estás aquí?'"
oak @talking2mouth "Piénsalo bien."

red @thinking ".{w=0.25}.{w=0.25}.{w=0.25}{nw}"
extend @talkingmouth " stoy aquí porque me recomendaste. Pero, espera..." 
red @closedbrow talking2mouth "Kobukan está preparado para enseñar a un completo novato en entrenamiento Pokémon, pero aún exige altas calificaciones en matemáticas, ciencias, literatura... y una vida fuera de lo academico también."
red @talkingmouth "Yo no tengo eso. No hay manera de que pudiera haber entrado solo con {i}tu{/i} recomendación."
red @surprised "Tú... de alguna manera forzaste mi entrada."

oak @closedeyes talkingmouth "Sí, y el 'cómo' no es algo relevante, así que puedes dejar de pensar en ello."

red @sad "Entonces... ¿por qué? {w=0.5}{nw}"
extend @closedeyes talking2mouth "No importa, solo me dirás que lo descubra por mi cuenta."

oak @happy "Cierto."

red @closedeyes talking2mouth "Entonces... tuvo que haber alguna razón por la que me querías aquí en la escuela. Si no son las calificaciones, ni las actividades extracurriculares... ¿qué tengo?"
red @surprisedeyes talking2mouth "¡Oh! Es mi memoria, ¿verdad? El poder memorizar todos los Pokémon, todas sus estadísticas y movimientos y esas cosas, ¿no?"

oak @talking2mouth "No. Está relacionado, pero la mayoría de los profesores de esta escuela han hecho eso. Además, es algo que cualquiera con una Pokédex podría hacer."
oak @talkingmouth "Por supuesto, tu aptitud para la memorización es impresionante. La mayoría de la gente necesita una Pokédex para eso, así que tenerlo todo memorizado es conveniente... aunque recuerdo que no fue porque tú quisieras, ¿verdad?"

red @sad "Sí... Realmente quería una Pokédex, pero ni mi mamá ni yo éramos entrenadores, así que no parecía valer la pena gastar el dinero en eso."

oak @talkingmouth "Bueno, tomo tu memorización como prueba de que mi decisión de no darte una Pokédex fue la correcta."

red @surprised "Espera, ¡¿no me diste una Pokédex a propósito?!"

oak @happy "Ahora, chico, ¿cuál es tu siguiente suposición?"

red @closedbrow talking2mouth "Hm..."
red @surprised "¡Oh! Es por lo de los Pokémon, ¿no es así? La forma en que todos están tranquilos alrededor mío."

oak @talkingmouth "Ah, así que te has dado cuenta de eso. Bueno, eso es parcialmente correcto, pero es un síntoma de una razón más compleja."

pause 2.0

redmind @unamusedbrow unamusedmouth "Esta conversación podría haber sido un email."

pause 2.0

oak @talking2mouth "¿Y bien, muchacho?"

red @closedeyes talking2mouth "Sam, entiendo que eres inteligente, todos lo saben, eres literalmente famoso por eso, pero por favor solo dime..."

pause 1.0

oak @talkingmouth "Muy bien. Sabes que el enfoque de mi investigación ha sido sobre las relaciones entre los Pokémon y los humanos, ¿verdad?" 
oak @talking2mouth "Bueno, tú representas un gran avance, algo que podría fortalecer más que nunca los lazos entre los Pokémon y los humanos." 
oak @angrybrow talkingmouth "Muchacho, creo que podrías poseer una habilidad especial."

red @surprised "¿Eh? ¿Como una habilidad Pokémon?"

oak @talkingmouth "Es muy similar a eso, sí. Mi colega en Sinnoh tiene algunas teorías interesantes sobre las similitudes entre los ancestros de los humanos y los Pokémon... {w=0.5}pero eso no es relevante en este momento."

red @confusedeyebrows talkingmouth "Okay, entonces ¿O estoy teniendo un descenso total a la locura o los humanos no tienen habilidades? Es imposible que lo humanos tengan esa capacidad, ¿no? Quiero decir, ¿no estoy equivocado?"

oak @talkingmouth "La respuesta a esa pregunta ha sido el sujeto de mi investigación durante casi dos décadas. Ciertamente, hay muchos casos documentados de humanos con poderes psíquicos." 
oak @closedeyes talkingmouth "Algunos han sido conocidos por hablar con los Pokémon, o sanar sus heridas solamente con un toque."
oak @talkingmouth "Algunos muestran una fuerza física extrema, más allá de lo común, y otros tienen una capacidad cerebral que supera nuestra comprensión de la anatomía. La respuesta a la que estoy llegando es... bueno, {i}sí{/i}, [first_name], es posible."
oak @angrybrow talking2mouth "[first_name], las personas y los Pokémon te quieren de inmediato, desde el momento en que te miran, quieren conocerte. Yo llamo a esto habilidad 'Energistad.'"

red @surprised "¿No es eso algo normal?"

oak @sadeyes sadeyebrows talking2mouth "Es difícil de decir. En mi vida recluida como académico, luego investigador, puedo afirmar con certeza que la gente no suele iniciar conversaciones conmigo, pero eso podría ser fácilmente mi propia falla."

red @closedeyes talking2mouth "Lo siento, Profesor, pero no creo que estés en lo correcto con esto. No tengo alguna especie de... superpoder, ni algún tipo de aura. Yo simplemente me acerco a las personas, me presento y luego les pregunto su nombre. Es realmente así de simple."

oak @talking2mouth "Muchacho, la diferencia entre tú y otras personas es mucho mayor de lo que se puede explicar solo con extroversión. No, mantengo que mi hipótesis es correcta y, a menos que los datos me demuestren lo contrario, pienso mantenerla."

red @confusedeyebrows talking2mouth "¿Los datos? ¿Qué quieres decir con--?"
red @surprised "¡Eso es!"

show oak surprisedbrow frownmouth with dis

red @angry "¡¿Me trajiste aquí solo para probar tu teoría?! No por algo que yo pueda hacer o por lo que merezca, ¿solo querías demostrar que tienes razón?"

oak sad "Eh... sí. No entiendo, ¿por qué estás molesto conmigo?"

red @angry "¡¿Por qué estoy molesto?! Estoy molesto porque--"

redmind @thinking "Está bien, cálmate, [first_name]. Sabes que debes ser paciente con Sam."

red @closedeyes talking2mouth "Estoy molesto, Sam, porque suena como si no pensaras que merezco estar aquí, que me trajiste solo para que pudieras responder tus propias preguntas personales."

oak -sad @angrybrow angrymouth "[ellipses]"
oak @angrybrow talking2mouth "No sé si mereces estar aquí, tú tampoco lo sabes. Nadie lo sabe hasta que te gradúes o fracases."

red @closedeyes talking2mouth "{i}Agh...{/i} Sí, tienes razón, como siempre."
red @talkingmouth "Bueno, entonces, ¿cómo puedo ayudarte en tu investigación?"

oak @happy "¡Graduandote! En cuatro días, has conocido a más personas de las que conociste en toda tu vida en Pueblo Paleta."
oak @happy "Si mi hipótesis es correcta, para cuando te gradúes, deberías tener muchos amigos y un equipo de Pokémon fuertes y leales."

pause 2.0

red @angrybrow talking2mouth "Sam... si realmente tienes razón, ¿significa eso que estoy controlando mentalmente a la gente para que les guste?"

oak @closedeyes talking2mouth "Pensé que podrías estar preocupado por eso, así que me aseguré de descubrir la respuesta antes de que alguna vez tuviera la oportunidad de contarte mi teoría."
oak @talkingmouth "No, muchacho, nada de eso. Más bien, lo que realmente sientes se hace evidente para cualquiera con quien hables. No es solo mostrar tus sentimientos, es compartirlos genuinamente con ese otro."
oak @talkingmouth "La gente y los Pokémon subconscientemente saben cómo te sientes, e incluso lo que estás pensando, hasta cierto grado. Y por eso, saben que eres solo un chico amigable, alguien seguro con quien estar cerca."
oak @closedeyes talking2mouth "En cualquier caso, me atrevería a decir que esta habilidad sería activamente perjudicial en las manos de alguien que no fuera tan amable como tú, e inútil para cualquiera que no fuera tan extrovertido." 
oak @angrybrow talking2mouth "Repito, esto no es control mental, ni {i}hace{/i} que le caigas bien a la gente de forma automática. Simplemente significa que tus intenciones no serán malinterpretadas. Y cuando dices la verdad, la gente lo cree."
oak @sad "En un mundo donde todos quieren algo de alguien más, y nadie dice lo que realmente quiere decir, poder saber las intenciones de la persona con la que hablas es... reconfortante."

red @talking2mouth "Vaya, entonces... ¿mis Pokémon no se asustan porque saben que no voy a intentar controlarlos, explotarlos o ser un simple idiota?"

oak @talkingmouth "Esa es mi teoría. Basándome en ese Pikachu especial que te di, y en cómo he visto a los Pokémon salvajes interactuar contigo, el efecto parece especialmente pronunciado en los Pokémon."

red @sad "¿Y que tal si... intentara mentirle a alguien? ¿Me creerían también?"

oak @happybrow ".{w=0.5}.{w=0.5}.{w=0.5}{nw}"
extend @talking2mouth "Muchacho, ¿cuándo fue la última vez que le mentiste a alguien sobre algo?"

red @closedeyes talkingmouth "Supongo que es un buen punto."

oak @talking2mouth "No te preocupes por cosas que no sucederán. Aunque si lo haces de igual forma, podría teorizar que las personas son mucho más propensas a {i}no creer{/i} tus mentiras."

red @closedbrow talking2mouth "Igualmente... todavía se siente un poco incómodo, como si hubiera tenido una ventaja injusta en la vida."

oak @closedeyes talkingmouth "Entonces, siéntete libre de olvidarlo. Ignora mis divagaciones, asume que eres un estudiante común y corriente y simplemente da lo mejor de ti en la academia, a la que ingresaste de forma justa y legítima."

red @happy "No puedo hacer eso ahora."

oak @happy "Bueno, ahí lo tienes. Ahora, si me disculpas, realmente debo volver al trabajo."

show oak:
    xpos 720
    ease 1.0 xpos 200

red @surprised "¡Espera!"

show oak surprisedbrow frownmouth with dis:
    xpos 200
    ease 0.5 xpos 960

oak -surprisedbrow -frownmouth -surprised @surprisedeyes surprisedeyebrows talking2mouth "¿Sí, muchacho?"

red @talking2mouth "No todos me quieren. Conocí a un par de entrenadores en mi primer día aquí, les hablé sobre mis... circunstancias y, claramente, perdieron el interés. Pero eso no es todo."

oak @surprised "¿Oh?"

if (persondex["Sabrina"]["Named"]):
    red @talkingmouth "Sí, hay una chica en una de mis clases electivas. Sabrina. Y básicamente me dijo que me alejara de ella."

    oak @closedeyes talkingmouth "Mmm, la chica Esper, ¿verdad? Estoy familiarizado con su caso."
    oak @talkingmouth "Creo que su situación es única. Probablemente ni siquiera se da cuenta de tu propia habilidad empática sutil, dado lo fuerte que es su propia telepatía."

    red @talking2mouth "Bueno, esa es solo una explicación, pero hay otras personas."

red @closedbrow talking2mouth "Por ejemplo, está Lance.{w=0.5} Digo,{w=0.25} el señor Lance,{w=0.25} ¿supongo? Como sea, él realmente se enfadó conmigo."

oak @happy "¿Oh? Estoy seguro de que eso no es cierto. Lance es un hombre estricto y terco, pero estoy seguro de que está lejos de ser capaz de disgustarse de un joven prometedor como tú."

redmind @thinking "Supongo que Sam no estuvo en la Exhibición de Batalla..."

red @talking2mouth "Bueno, hay alguien más."

red @closedeyes talking2mouth "Blue. Él me odia, siempre lo ha hecho."

oak @closedeyes talking2mouth "Mi nieto es...{w=0.75} una anomalía estadística que entra perfectamente dentro del margen de error. Además, si voy a demostrar que mi hipótesis de hace dieciocho años es correcta, no vale la pena considerarlo."

red @frownmouth "Hmm..."

redmind @thinking "Me siento un poco mal por Blue cada vez que escucho lo que su abuelo dice de él... pero no es como si no se lo mereciera."

red @closedeyes talkingmouth "Bueno, supongo que solo me queda una última pregunta."

show oak surprisedbrow frownmouth with dis

red happy "¿Cómo voy a pagar por estar en la academia? El primer pago de la matrícula vence en seis meses."

stop music

pause 2.0

hide red
oak sad "{cps=10}Eh... para ser honesto, muchacho, no lo pensé...{/cps}"

pause 2.0

show research 
show red surprisedmouth deadeyes surprisedeyebrows at Transform(xpos=0.08, yanchor=0.35), monochrome
with vpunch

red "¡¿QUÉ?!"

show red at Transform(xpos=0.08, yanchor=0.35):
    xpos 0.08 ypos 1.0
    parallel:
        ease 2.0 ypos 1.5
    parallel:
        ease 0.5 xpos 0.12
        ease 0.5 xpos 0.04
        repeat 5

pause 3.0

show research with vpunch

pause 2.0

hide red
redmind uniform @thinking "{cps=10}... Mierda, estoy totalmente jodido.{/cps}"

pause 1.0

show blank2 with dis:
    alpha 1.0

show oak:
    xpos 960 alpha 1.0
    ease 0.5 xpos 0 alpha 0.0

$ renpy.pause(1.5, hard=True)

hide oak

redmind @thinking "[ellipses]"
redmind @thinking "¿Es cierto lo que dijo el Profesor Oak? ¿Realmente tengo algún tipo de... habilidad?"
redmind "Cheren dijo que tenía un... 'Carisma inofensivo.' ¿Es eso a lo que se refería?"
redmind "Y lo más importante... ¿Hay alguna manera de usarlo para no ser expulsado de Kobukan en seis meses?"

window hide

stop music fadeout 1.5

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_37

$ renpy.pause(3.0, hard=True)

show night at vspaz

pause 3.5

hide night

############################################################################################################################################################################################################################
#### 3. END OF DAY #########################################################################################################################################################################################################
############################################################################################################################################################################################################################

play music "Audio/Music/SoaringIllusions_Intro.ogg" noloop
queue music "Audio/Music/SoaringIllusions.ogg"

$ renpy.transition(dissolve)
show screen currentdate

$ PlaySound("Door_Open1.ogg")
scene dorm_B norm with Dissolve(2.0)

show dorm_table

hide blank2

redmind uniform @thinking "Bien, todavía no volvió nadie.{w=0.5} Quiero hablar en privado con [pika_name] sobre mi.{w=0.25}.{w=0.25}.{w=0.25} condición."

$ renpy.music.play("Audio/Pokemon/pikachu_excite2.ogg", channel="altcry", loop=None)

pikachu neutral_2 "¡Pika!"

red @talkingmouth "¡Hola, amiguito!{w=0.5} ¿Me extrañaste?"

$ renpy.music.play("Audio/Pokemon/pikachu_sad.ogg", channel="altcry", loop=None)

pikachu angry_2 "Pikaaaa."

red @talkingmouth "Sí, lo sé, pero vas a tener que acostumbrarte.{w=0.5} Tengo que seguir con esto el resto del año, ¿recuerdas?"

$ renpy.music.play("Audio/Pokemon/pikachu_angry2.ogg", channel="altcry", loop=None)

pikachu angry_3 "¡Pi!"

red @sadbrow talkingmouth "¡Oh, vamos, no te pongas así!"
red @talkingmouth "Cuando mi carga de estudios empiece a aligerarse, ni siquiera vas a notar que me fui.{w=0.5} ¡Será como en la secundaria!"

$ renpy.music.play("Audio/Pokemon/pikachu_norm3.ogg", channel="altcry", loop=None)

pikachu happy_2 "Pika."

redmind @thinking "Hablo en serio, pero si el Profesor Oak tiene razón, tengo que empezar a reevaluarme como Entrenador Pokémon...{w=0.5} Y como persona."

$ renpy.music.play("Audio/Pokemon/pikachu_question.ogg", channel="altcry", loop=None)

pikachu "¿Pika?"

red @closedbrow talking2mouth "Sí, tengo noticias. Noticias importantes. Dame un segundo para sentarme,{w=0.5} fue un día muy largo."

show dorm_B behind dorm_table:
    yalign 0.0
    ease 0.04 ypos -10
    ease 0.04 ypos 10
    ease 0.04 ypos 0
show dorm_table:
    yalign 0.0
    ease 0.04 ypos -10
    ease 0.04 ypos 10
    ease 0.04 ypos 0

pause 0.1
$ PlaySound("Thud2.ogg")

pause 1.5

redmind hatless casual @thinking "Ahora mismo, siento que podría hundirme en la cama..."
red @closedbrow talking2mouth "{i}Agh...{/i}"

pikachu neutral_3 "[ellipses]"

redmind @thinking "[ellipses]"
redmind @angry "¡Argh, qué demonios!{w=0.5} ¡No puedo quedarme quieto después de escuchar todo eso!"

$ renpy.music.play("Audio/Pokemon/pikachu_pikapika1.ogg", channel="altcry", loop=None)

pikachu neutral_4 "¿Pika, pika?"

red @wince talkingmouth "Mirá... Sam cree que tengo algún tipo de 'habilidad' que hace que la gente... {i}me quiera{/i}."

$ renpy.music.play("Audio/Pokemon/pikachu_confused.ogg", channel="altcry", loop=None)

pikachu neutral_4 "¿Piiika...?"

red @talking2mouth "Bueno, está bien, dijo explícitamente que {i}no{/i} era una habilidad que hace que la gente me quiera, pero aun así... ¡Se siente así!"

$ renpy.music.play("Audio/Pokemon/pikachu_confused2.ogg", channel="altcry", loop=None)

pikachu surprisedbrow frownmouth @surprised "¡¿Piii-KA?!"

pause 2.0

red @talking2mouth ".{w=0.25}.{w=0.25}. Hey, amiguito... ¿eres realmente mi amigo? Lo que quiero decir es, ¿no te estoy obligando con algún poder mental raro?"

$ renpy.music.play("Audio/Pokemon/pikachu_happy2.ogg", channel="altcry", loop=None)

pikachu happy_2 "Piiiikaaaa.~"

red @thinking "[ellipses]"
red @happy "Sí, está bien. Confío en ti. Y si Sam tiene razón... y nunca lo he visto equivocarse... entonces no hay nada turbio ni malo en esto." 
red @talking2mouth "... Quizás lo mejor sea asumir que está equivocado y seguir mi vida como lo estaba haciendo antes."

$ startergenderpronoun = "él " 
if (playerparty[0].GetGender() == Genders.Female):
    $ startergenderpronoun = "ella"
elif (playerparty[0].GetGender() == Genders.Unknown):
    $ startergenderpronoun = "él"
redmind "In any case, [startergenderpronoun] sure looks happy to get out of that ball for some fresh air."
red @talkingmouth "Hmm..."
red @talkingmouth "Dime, [pika_name]. No pasaste mucho tiempo con [starter_name], ¿verdad?{w=0.5} ¿Te gustaría pasar el rato con [startergenderpronoun]?"

$ renpy.music.play("Audio/Pokemon/pikachu_norm1.ogg", channel="altcry", loop=None)

pikachu neutral_2b "¡Pika chu!"

red @talkingmouth "Muy bien, ¡sal, [starter_name]!"

$ PlaySound("Pokemon/Ball sound.ogg")

$ renpy.pause(0.5, hard=True)
$ renpy.music.play(startercry, channel="altcry", loop=None)

starter @talkingmouth "¡[starter_species_name]!"

redmind "Ahora que lo pienso, este es el primer Pokémon que mantengo en una Poké Ball." 
redmind "Sé que están perfectamente cómodos, pero después de vivir tanto tiempo con [pika_name], me hace sentir mal mantener a un Pokémon en su Poké Ball..."

redmind "En cualquier caso, [starter_name] se ve feliz de salir de la Poké Ball y respirar aire fresco."

$ renpy.music.play("Audio/Pokemon/pikachu_norm1.ogg", channel="altcry", loop=None)
pikachu neutral_2 "¡Pika! ¡Pi Pikachu!{w=0.5}{nw}"

extend pikachu " ¿Pika pi...?"

$ renpy.music.play(startercry, channel="altcry", loop=None)

$ starter_species_name = pokedexlookup(starter_id, DexMacros.Name)
$ starter_fragment = starter_species_name[:3]
starter @talkingmouth "¡[starter_fragment]! ¡[starter_species_name]!"

$ renpy.music.play("Audio/Pokemon/pikachu_excite2.ogg", channel="altcry", loop=None)

pikachu happy_2 "¡Pika!"

redmind "Que conversación tan fascinante."
redmind "Al menos [pika_name] parece feliz de tener otro Pokémon con quien estar.{w=0.5} Es un alivio."
redmind "Me preocupaba que [pika_name] tuviera problemas para conocer nuevos Pokémon.{w=0.5} O que se pusiera celoso por sentirse 'reemplazado' o algo por el estilo."

$ renpy.music.play("Audio/Pokemon/pikachu_happy3.ogg", channel="altcry", loop=None)

pikachu happy_3 "Pipipi... ¡Pika!"

show starterportraitfull behind dorm_table:
    subpixel True
    alpha 0.0 xzoom -0.4 yzoom 0.4 ypos 575 xpos 330
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        pause 0.12
        block:
            parallel:
                ease 0.25 ypos 565
                ease 0.1 ypos 575
                repeat
            parallel:
                ease 0.25 xpos 320
                ease 0.1 xpos 315
                ease 0.25 xpos 320
                ease 0.10 xpos 330
                repeat
    
show pikachu happy_3 behind dorm_table:
    subpixel True
    alpha 0.0 xzoom -0.45 yzoom 0.45 ypos 650 xpos 640
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        pause 0.1
        block:
            parallel:
                ease 0.32 ypos 640
                ease 0.15 ypos 650
                repeat
            parallel:
                ease 0.32 xpos 630
                ease 0.15 xpos 630
                ease 0.32 xpos 630
                ease 0.15 xpos 640
                repeat

redmind "Me pregunto qué pensaría mamá si viera esto.{w=0.5} Probablemente diría que solo están haciendo ruidos, pero yo sé que están hablando entre ellos."
redmind "Ahora que lo pienso, mamá nunca entendió lo que decía [pika_name]."
redmind "Solo hacia suposiciones según si suena feliz, triste o enojado.{w=0.5} A veces acierta... pero la mayoría de las veces, no."
redmind "...{w=0.5} ¿Esto será solo porque [pika_name] y [starter_name] confían en mí? ¿Será que los demás entrenadores están tan ocupados intentando que sus Pokémon {i}obedezcan{/i} en vez de aprenden a escucharlos?"

show starterportraitfull:
    ease 0.2 ypos 575 xpos 330
    pause 0.5
    ease 0.5 alpha 0.0
    
show pikachu:
    ease 0.15 ypos 650 xpos 640 alpha 1.0
    pause 0.25
    ease 0.5 alpha 0.0

$ renpy.pause(0.75, hard=True)

red @talkingmouth "Bueno, es hora de dormir, chicos. Mañana tengo un día ocupado fingiendo que todo es normal, así que mejor me acuesto temprano. También quiero salir a correr temprano para despejarme un poco."
red @happy "Hora de volver, [starter_name]."

$ PlaySound("Pokemon/Ball sound.ogg")

pause 1.0

red @talkingmouth "Tú también, [pika_name]. Intenta dormir un rato. Mañana podrás jugar con [starter_name], ¿sí?"

hide pikachu

pikachu neutral_2b "¡Pika!"

red @talkingmouth "¡Buenas noches!"

window hide

pause 1.0

hide dorm_table
show dorm_B lightsout

pause 1.0

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_38

show blank2 with transeye

stop music fadeout 1.0
$ renpy.pause(1.0, hard=True)

hide pikachu
hide starterportraitfull

hide dorm_empty_B
hide blank2

jump day010409