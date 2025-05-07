label secondhomeroom010405:

$ timeOfDay = "Evening"

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

scene homeroom with Dissolve(2.0)

show oakbg with dis

$ renpy.transition(dissolve)
show screen currentdate
$ renpy.pause(1.5, hard=True)

narrator "Regresas a tu salón de clases generales mientras el primer día llega a su fin."
redmind uniform "El día no se sintió tan largo, pero considerando todo, estoy listo para darlo por terminado.{w=0.5} Y por las caras de todos, parece que también lo están."
narrator "La última clase pasa rápidamente mientras escuchas al Profesor Oak hablar de cosas muy triviales."
redmind @thonk "Es extraño, esperaba que la clase con el profesor fuera un poco más... ¿cómo decirlo?... ¿satisfactoria?{w=0.5} Al menos, eso es lo que mis compañeros dieron a entender más temprano."
redmind @thinking "Pero hasta ahora no he sacado nada especialmente memorable de esta clase, sacando el discurso aterrador sobre la tasa de graduación."

hide blank2

oak @talkingmouth "Puedo ver en sus ojos que están bastante cansados de escucharme divagar."
oak @talkingmouth "Para ser honesto, yo también estoy cansado, ¡ja, ja, ja!"
oak @talkingmouth "Pero antes de dejarlos ir, quiero darles un regalo de bienvenida como celebración por haber sido aceptados en la Academia Kobukan."

show pokeballs_full:
    alpha 0.0 xalign 0.5 yalign 1.0
    ease 1.0 alpha 1.0

$ renpy.pause(2.0, hard=True)

redmind @surprisedbrow frownmouth "¿Son lo que creo que son?{w=0.5} Si es así, entonces esta clase acaba de volverse mucho más emocionante."

oak @talkingmouth "Hoy, cada uno de ustedes se llevará un Pokémon a casa, ¡cortesía de la academia!"

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.0)

oak @talkingmouth "En cada una de estas Poké Balls que recibirán, hay un Pokémon no evolucionado y sin domesticar.{w=0.5} Considérenlo su tarea para el próximo año."

show pokeballs_full:
    alpha 1.0
    ease 0.5 alpha 0.0

show blue uniform with dis

blue @talkingmouth "Hey, yo ya tengo un montón de Pokémon en casa.{w=0.5} No necesito más, y mucho menos unos sin evolucionar."

oak @talkingmouth "{color=#0048ff}Independientemente de los Pokémon que ya posean, estos Pokémon deberán permanecer con ustedes durante el resto de su tiempo en la Academia Kobukan.{/color}"
oak @talkingmouth "{color=#0048ff}Al final del año, este Pokémon será evaluado junto con ustedes y otros posibles Pokémon en su equipo para determinar si pueden graduarse.{/color}"

blue @angry "¡GENIAL!{w=0.6} ¡Me {i}ENCANTA{/i} que me obliguen a aceptar responsabilidades adicionales!"
show blue surprisedbrow frownmouth with dis

oak @talkingmouth "¡Esa es la actitud, [blue_name]!"

hide blue with dis

redmind "Así parece ser como va la mano.{w=0.5} Ya suponía que esta academia no se centraría unicamente en las buenas notas, así que esto no me toma tan por sorpresa."

oak @talkingmouth "Los llamaré uno por uno para que reciban su Pokémon.{w=0.5} Recuerden, ¡lo que les toca, les toca!"

red @talkingmouth "Esto me hace acordar cuando era un niño y el Profesor Oak me dio a [pika_name]."

$ renpy.music.play("Audio/pokemon/cries/37.mp3", channel="altcry", loop=None)

Character("Estudiante emocionado") "\"¡¿Me toco un Vulpix?!{w=0.5} ¡WOOHOO!\""

redmind "Genial, los Vulpix son bastante raros, por lo seguro que el que me toque será al menos igual de raro."

oak @talkingmouth "¡[first_name]!"

$ renpy.music.set_volume(0.0, delay=1.0, channel="music")

redmind "Uff, muy bien..."
redmind @sweat closedbrow frownmouth "Aquí vamos.{w=0.5} ¡El momento de la verdad!"

show pokeballs_emptyA:
    alpha 0.0 xalign 0.5 yalign 1.0
    ease 1.0 alpha 1.0

redmind @sadbrow sweat "Con mi suerte, {i}seguro{/i} que voy a terminar con un Rattata o un Bidoof."
redmind @closedbrow frownmouth "Sean quienes sean los dioses que me estén mirando, por favor, ¡no me fallen!"
redmind @thinking ".{w=0.5}.{w=0.5}.{w=0.5} Un momento."
redmind "Las Poké Balls aquí están marcadas con números de la Dex Nacional. Me he memorizado {i}todos{/i} los Pokémon y sus números. Puedo, simplemente... ¡elegir el que quiera!"

pause 1.0

redmind "Eso significa que... puedo influir en mi elección. Sam sabe que me sé los números de cada Pokémon de la Dex Nacional, ¿no? Tal vez me está dando una ventaja."

menu:
    ">Elegir entre tres Poké Balls al azar":
        $ starter_id = renpy.call("PickPokemon", "all")

    ">Elegir entre tres Pokémon de tus electividades":
        $ starter_id = renpy.call("PickPokemon", "electives")

    ">Elegir entre tres Pokémon de un tipo específico":
        call PickType() from _call_PickType
        $ starter_id = renpy.call("PickPokemon", _return)

    ">Elegir un Pokémon específico":
        $ starter_id = renpy.call("PickPokemon", "every")

$ starter_id = _return
$ starter_name = pokedexlookup(starter_id, DexMacros.Name)

show blank with dis:
    alpha 1.0

pause 0.5

$ PlaySound("Pokemon/Ball sound.ogg")

oak @talkingmouth "Hmmm..."

hide pokeballs_emptyA

pause 1.5

$ startercry = "Audio/pokemon/cries/{}.mp3".format(starter_id)
$ renpy.music.play(startercry, channel="altcry", loop=None)

show pokeballs_emptyB behind blank:
    xalign 0.5 yalign 1.0

show blank:
    alpha 1.0
    ease 1.0 alpha 0.0

pause 1.0

$ renpy.music.play("Audio/Get.ogg", channel="XYgame", loop=None, fadeout=0.5)

show starterportraitfull at pokeball:
    align (0.5, 0.5)
    zoom max(1, (ReadHeight(starter_id) / 40.0))

$ starterobj = Pokemon(starter_id, shinylock=False)
$ playerparty.append(starterobj)
$ starter_species_name = playerparty[0].GetNickname()
oak @happy "¡Felicidades, es un [starter_name]!"
oak @talkingmouth "Este Pokémon tiene mucha energia."

if (ReadHeight(starter_id) > 48):
    oak @angry "... Sin embargo, también es bastante grande para ser un Pokémon bebé. ¿Podrías sacarlo de mi mesa?"
    red @surprised "Oh, vaya, lo siento Sa-- quiero decir, Profesor Oak. Es que..."

$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

red @surprised "Yo...{w=0.5} ¿En se--"
red @happy sweat"No me estás jugando una broma, ¿verdad?"

oak @talkingmouth "No le estoy jugando una broma a nadie.{w=0.5} Ahora está bajo tu cuidado."

red @happy "¡MUY BIEN!"
redmind @closedeyes frownmouth "¡¿Un [starter_name]?!{w=0.5} ¡Hoy es mi día de suerte!"
redmind @closedeyes frownmouth "No sabía qué esperar, pero de alguna manera todo salió mejor de lo que imaginé."
redmind happy "¡Gracias dioses! Sabía que me estaban cuidando."

hide pokeballs_emptyB
hide starterportraitfull
hide blank2 
with dis

$ PlaySound("BellChime.ogg")

show leaf uniform at leftside with dis:
    xzoom -1

leaf @happy "¡Buen Pokémon, [first_name]!"

red @happy "¡Gracias!{w=0.5} En realidad, siempre quise uno así. ¿Tú también conseguiste el que querías?"

leaf @talkingmouth "¡Por supuesto que sí!{w=0.5} ¡Saluda a Bulbasaur!"

$ DisplayPokemon("Bulbasaur")

leaf @happy "Tu [starter_name] debería jugar con mi Bulbasaur alguna vez."
leaf @flirttalk "Es natural que nuestros Pokémon sean mejores amigos, ¡igual que sus Entrenadores!"

$ PlaySound("pokemon/ball sound.ogg")
show sideportraitfull at backinpokeball

red @confused "¿Desde cuándo somos mejores ami--"
show leaf surprisedbrow frownmouth with dis

hide blue
show blue uniform at rightside with dis:
    xzoom -1

blue @happy "¿Te tocó un [starter_name], [first_name]?{w=0.5} ¡JA! ¡Esto es perfecto!"

show leaf flirtbrow with dis

red @sweat talking2mouth "Voy a arrepentirme de preguntar esto, pero... {w=0.5}{nw}" 
extend @confused " ¿Qué tiene de malo un [starter_name]?"

blue @happy "Oh, nada en realidad..."
show leaf angrybrow frownmouth with dis
blue @angrybrow happymouth "¡Excepto que no es tan raro como mi {i}Eevee!{/i} ¡Ja, ja, ja, ja!"

red @surprised "¿Qué?"

blue @happy "¡Debe ser un castigo divino!"
blue @closedbrow talkingmouth "Nunca me vas a ganar, ¡ni siquiera en sorteos! ¡Ja, ja!"
blue @happy "¡Una vez que mi Eevee evolucione, podré vencer cualquier equipo que intentes formar contra mí! ¡No tienes ninguna posibilidad!"

red @closedbrow talking2mouth "Claro, si quieres evolucionar tu Eevee para vencer al equipo de un entrenador en particular, adelante."

blue @angry "¡Hey! ¡Ahora vamos a probar a nuestros nuevos Pokémon!{w=0.5} ¡Te reto a un combate!"
show blue surprisedbrow frownmouth with dis

oak @talkingmouth "¡Blue! ¡Este no es el momento ni el lugar para eso!"

blue @sad2eyes talkingmouth "Bah. Como sea, mi Pokémon se ve mucho más fuerte de todos modos."
show blue surprisedbrow frownmouth with dis
show leaf surprisedbrow frownmouth with dis

show may uniform angrybrow frownmouth with dis

may @angry "Hey, déjalo en paz!{w=0.5} ¡No está bien acosar a los demás!"

blue @closedbrow sweat talkingmouth "Oh, ehh, yo..."

may @angry "¡Y para tu información, ganar batallas no se trata solo de tener la ventaja de tipo!"

leaf -surprisedbrow -frownmouth @talkingmouth "Solo ignóralo.{w=0.5} ¿Qué te toco, May?"

hide blue with dis

$ renpy.pause(1.0, hard=True)

may -angrybrow -frownmouth @happy "¡Un Torchic!{w=0.5} Me encantan los Pokémon de Fuego, así que ella y yo seremos mejores amigas, ¡tengo ese presentimiento!"

leaf @happy "¡Ja, ja! ¡Un Torchic te queda de perlas, May!{w=0.5} De hecho, tu moño me hacen acordar a sus cabecitas peludas."

may @surprised "¡Oye... tienes razón!" 
may @happy "Escuchaste eso, Torchic? ¡Esto es nuestro destino!{w=0.5} ¡Estábamos destinadas a estar juntas!"

$ showredonly = True

whitney uniform @smile "¿Conseguieron iniciales? ¡Suertudaas!"

show may:
    xpos 0.5
    ease 0.5 xpos 0.8

show leaf:
    xpos 0.25 xzoom -1
    ease 0.5 xpos 0.6 xzoom 1

show whitney uniform:
    xpos -0.5
    ease 0.4 xpos 0.4

show flannery uniform:
    xpos -0.5
    ease 1.0 xpos 0.2

pause 1.0

$ showredonly = False

red @talkingmouth "Los iniciales son geniales, pero cualquier Pokémon puede ser genial con el entrenador adecuado.{w=0.5} ¿Qué Pokémon consiguieron ustedes?"

whitney @happy "¡Un Cleffa!{w=0.5} Es un tipo de ternura diferente a mi Miltank, ¡pero la aceptaré!"
whitney @winkbrow talkingmouth "Escuché que estos pequeños son realmente raros."

flannery @happybrow talkingmouth "Conseguí un pequeño y adorable Numel.{w=0.5} Estoy tomando las clases electivas de Fuego y Tierra, ¡así que esto es perfecto!"
flannery @closedbrow talkingmouth "Mi familia en Lavacalda tenía montones de estos, pero por alguna razón, nunca tuve uno. No será el mejor en batalla, pero aun así, lo adoro."

whitney @talking2mouth "¿De veras? ¿No es uno de los pocos Pokémon en el mundo que puede aprender Estallido?"
whitney @surprised "No sé todo lo que debería sobre Pokémon de Fuego, pero ¿ese movimiento no es buenísimo?"

flannery @happy "¡Claro!{w=0.5} Pero, quiero decir, los Camerupt son {i}realmente{/i} lentos. Aun así, ¡son súper divertidos para acurrucarse!"

redmind @thinking "Entonces... ¿vamos a pasar por alto el giro de personalidad en 180 grados de Flannery?"

show hilbert uniform sad behind leaf with dis:
    xpos 0.5 zoom 0.8

pause 2.0 

redmind @thonk "... ¿Solo se va a quedar merodeando?"

pause 1.0

show hilbert surprisedbrow with dis
red @happy "¿Qué hay de ti, Hilbert?"

hilbert @surprised "¿Ah?"

show hilbert uniform sad behind whitney:
    xpos 0.5 zoom 0.8
    ease 0.5 zoom 1.0

show may:
    xpos 0.8
    ease 0.5 xpos 0.9

show leaf:
    xpos 0.6
    ease 0.5 xpos 0.7

show whitney uniform:
    xpos 0.4
    ease 0.5 xpos 0.3

show flannery uniform:
    xpos 0.2
    ease 0.5 xpos 0.1

hilbert @sadbrow talkingmouth "Oh...{w=0.5} Solo obtuve un Cubchoo."

red @confused "Hey, un Pokémon de Teselia.{w=0.5} Territorio antiguo para ti, ¿eh?"

whitney @happy "¡Ay, los Cubchoo son tan adorables...!"
whitney @talking2mouth sadbrow "Hasta que se convierten en Beartic."

whitney @sadbrow talking2mouth "¿Vas a evolucionar a tu Cubchoo?"

hilbert @angrybrow talkingmouth "Probablemente."

whitney @sad "Aw, que mal..."

hide hilbert with dis

show may:
    xpos 0.9
    ease 0.5 xpos 0.8

show leaf:
    xpos 0.7
    ease 0.5 xpos 0.6

show whitney uniform:
    xpos 0.3
    ease 0.5 xpos 0.4

show flannery uniform:
    xpos 0.1
    ease 0.5 xpos 0.2


$ renpy.pause(0.6, hard=True)

may @happy "¡No puedo esperar para jugar con mi Torchic!{w=0.5} ¡Ella se va a divertir mucho con mi Nincada cuando llegue!"

flannery @surprised "¿Podemos traer nuestros Pokémon de casa?"

leaf @talking2mouth "El Profesor dijo que no importa qué otros Pokémon tengamos en nuestro equipo, así que sí."
leaf @talkingmouth "Mañana por la mañana me enviarán mi Dratini y Helioptile."

leaf @closedbrow talking2mouth "Es tan difícil conseguir que envíen cosas a Kobukan, pero ahorré algo de dinero hace un tiempo, así que deberíamos estar bien."

whitney @angrybrow talking2mouth "¡Dímelo a mí! ¿Sabes cuánto cuesta encontrar una Piedra Lunar en esta región? ¡Tal vez sea más barato volar a Teselia."

may @talkingmouth "Bueno, la industria minera está--"

show leaf surprisedbrow frownmouth with dis
show may surprisedbrow frownmouth with dis
show whitney surprisedbrow frownmouth with dis
show flannery surprisedbrow frownmouth sweat with dis
oak @talkingmouth "¿Qué siguen haciendo todos aquí?{w=0.5} La clase ya termino, ya pueden retirarse."

show leaf:
    alpha 1.0 xpos 0.6
    ease 0.5 alpha 0.0

show flannery:
    alpha 1.0 xpos 0.2
    ease 0.5 alpha 0.0

show whitney:
    alpha 1.0 xpos 0.4
    ease 0.5 alpha 0.0

show may:
    alpha 1.0 xpos 0.8
    ease 0.5 alpha 0.0

$ renpy.music.stop(channel='crowd', fadeout=0.5)
$ renpy.pause(0.5, hard=True)

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_10

window hide

stop music fadeout 2.5

scene blank2 with spinfade
$ renpy.pause(1.0, hard=True)

$ renpy.music.play("Audio/hall_crowd.ogg", channel='crowd', loop=True, fadein=1.75)
$ renpy.pause(2.0, hard=True)

scene academyhall with spinfade
$ renpy.pause(1.5, hard=True)

$ renpy.transition(dissolve)
show screen currentdate

show leaf uniform with dis

show may uniform at leftside with dis

leaf @happy "Mmm, dulce libertad!{w=0.5} ¿Qué quieren hacer ahora?"

may @sadbrow happymouth "Lo siento, pero tengo planes.{w=0.5} Brendan dijo que tenía hambre y quería que nos encontráramos en la cafetería después de clases."

leaf @surprised "¡Pero si acabamos de almorzar!"

leaf @flirttalk "¿Van a seguir atiborrándose?{w=0.5} ¡Van terminar a engordando!"

may @sadbrow happymouth "Bueno, {i}yo{/i} no tengo hambre, pero Brendan quiere que vaya con él, así que...{w=0.5} A menos que quieran acompañarme."

leaf @talkingmouth "Nah, estoy bien. {w=0.5}{nw}"
extend @flirttalk "¡Seguro que [first_name] y yo podemos encontrar algo más que hacer!"

red uniform @confused "¿Eh?"
red @happy "Parece que acabas de decidir algo por ti misma otra vez."

leaf @angrybrow talking2mouth "Te reto a que me digas que tienes planes hoy."

red @closedeyes happymouth "... Te tomo el punto."

show brendan uniform happybrow at rightside with dis

brendan @happymouth "¡Hey!{w=0.5} ¿Vamos, May?"

may @happy "¡Oh, claro!{w=0.5} ¡Que se diviertan, ustedes dos!"

show may:
    xpos 0.25
    ease 0.5 xpos 0.4

may @flirtbrow talkingmouth "Llámenme si... {i}necesitan algo{/i}, Leaf. {size=30}Tengo una gran reserva en nuestro dormitorio.{/size}"

leaf @flirttalk "{size=30}Es bueno saberlo.{/size}"

hide may
hide brendan
with dis

leaf @happy "Bueno, nos vemos. ¡Adiosin!"

$ renpy.pause(1.5, hard=True)

leaf happybrow @happy "Entonces, ¿qué quieres hacer?{w=0.5} Ni siquiera sé qué tipo de cosas te gustan."

red @happy "Soy un aficionado de salir a correr."

leaf @happy "¡Genial!{w=0.5} Yo ni loca voy a hacer eso."
leaf @closedbrow talking2mouth "Umm... {w=0.5}{nw}"
extend -happybrow @talking2mouth "¿Quieres pasar el rato en el vestíbulo mientras pensamos a donde ir?"

show leaf surprisedbrow frownmouth with dis

red @sadbrow talkingmouth "Claro, pero no conozco ningún sitio de por aquí."

leaf @surprised "¿A qué te refieres?"
leaf @happybrow talkingmouth"Podemos ir {color=#0048ff}al jardín, al Centro de Recreación, al Centro de Investigación,{/color} o..."

pause 1.5

leaf -surprisedbrow -frownmouth @sarcastic "... ¿Algo de esto te suena familiar?"

red @confused "Algunos amigos míos hablaron del jardín antes, pero para el resto... {w=0.5}{nw}"
extend @closedbrow talking2mouth sweat "Para ser honesto, mi investigación sobre Kobukan fue más sobre lo académico e histórico que sobre la geografía del lugar."

leaf @happy "Hmmmm, pensé que tal vez habrías aprendido desde la última vez, pero tal vez tu sentido de la orientación sea innatamente inútil."
leaf @flirttalk "Por suerte, ¡me tienes a mí!{w=0.5} Saquemos el viejo y confiable mapa, y echemos un vistazo a la zona."

$ renpy.music.play("Audio/Music/Show Me Around.ogg", channel='music', loop=True, fadein=1.0)

show academyhall_blur 
show mapdemo 
with dis

$ renpy.pause(1.5, hard=True)

leaf @talking2mouth "Estamos aquí, en el edificio principal arriba del Centro Estudiantil."
leaf @flirttalk "¿Ves todos los caminos en el mapa?{w=0.5} Esos son caminos que podemos tomar para llegar a los otros..."

red @unamusedbrow talking2mouth "Mira, a pesar de la evidencia en contra, {i}sí{/i} sé leer un mapa."

leaf @happy "¡Está bien, pero si tienes alguna pregunta sobre la zona en general, solo avísame!"

jump map_tutorial

label map_tutorial:

menu:
    extend ""
    "¿Qué edificios están abiertos para los estudiantes?":
        leaf @talkingmouth "Bueno, en este momento, más o menos todos. Con la excepción del Battle Hall, {color=#0048ff}todos están abiertos durante el día, pero cierran por la noche.{w=0.5} Después de eso, necesitarás un permiso especial.{/color}"

        red @talkingmouth "En resumen, una vez que cierran, voy a tener que esperar hasta mañana para poder entrar."

        leaf @talking2mouth "Sí, es un poco molesto, pero {color=#0048ff}una vez que cierran, solo podrás quedarte en tu dormitorio.{/color}{w=0.5} Deberías aprovechar el día al máximo antes de que termine el día."
        leaf @talkingmouth "¿Algo más que quieras saber?"

        jump map_tutorial

    "¿Qué actividades hay por aquí??":
        red @talkingmouth "¿Hay algo en particular que a todos les guste hacer?"

        leaf @talking2mouth "No que yo recuerde.{w=0.5}"

        leaf @talkingmouth "Hay muchas cosas para hacer, pero {color=#0048ff}depende de a dónde vayas.{/color}"
        leaf @talking2mouth "{color=#0048ff}Dependiendo de lo que hagas, algunas actividades pueden quitarte un poco de tiempo o ocuparte todo el día.{/color}{w=0.5} Intenta gestionar bien tu tiempo y planifica con antelación lo que vayas a hacer."

        leaf @flirttalk "O si estás cansado o simplemente te da pereza, {color=#0048ff}puedes volver a tu dormitorio después clases y pasar el resto del día ahí.{/color}"
        leaf @surprised "Digo, eso es sólo si {i}realmente{/i} no se te ocurre nada que hacer...{w=0.5} o si no tienes amigos."
        leaf @talking2mouth "A mí me encantaría salir y hacer cosas, pero esta academia tiene un toque de queda estricto.{w=0.5}{nw}"
        extend @talking2mouth " Así que {color=#0048ff}una vez que sea de noche, no puedes salir del dormitorio.{/color}"
        
        red @talkingmouth "Sí, recuerdo que lo mencionaron en la orientación."

        leaf @talkingmouth "¿Algo más que quieras saber?"

        jump map_tutorial

    "¿Qué puedes decirme sobre Ciudad Inspira?":
        red @talkingmouth "¿Qué puedes decirme sobre Ciudad Inspira?"

        leaf @happy "¡Tiene un montón de tiendas y mercados geniales para visitar!"
        leaf @talking2mouth "Es el paraíso de cualquier chica."

        leaf @flirttalk "Pero para alguien como tú...{w=0.5} Yo esperaría {color=#0048ff}hasta conocer bien el campus.{/color}"
        
        red @closedbrow talking2mouth "De todas formas, no se me ocurre ninguna razón para ir a la ciudad por ahora."

        leaf @talking2mouth "¿Algo más que quieras saber?"

        jump map_tutorial

    "Estoy bien.":
        red @talkingmouth "De acuerdo, lo tengo.{w=0.5} Gracias por la ayuda."

        leaf @happy "¡De nada!"

hide academyhall_blur
hide mapdemo
with dis

$ renpy.pause(1.5, hard=True)

leaf @talking2mouth "Bueno, ahora que ya resolvimos eso, ¿a dónde quieres ir?"

red @confused "¿Yo?{w=0.25} No dije nada sobre ir a ningún lado."

leaf @flirttalk "¡Oh, no seas tímido! Vamos, vamos, ¡vamos a algún lugar divertido!"  
leaf @happy "De todas formas, no es como si tuvieras otros planes ahora mismo."

red @talkingmouth "Ah, ¿por qué no? Tu mandas."

leaf @happy "¡Genial!"
leaf @closedbrow talking2mouth "Veamos...{w=0.5} ¿qué tal el gimnasio?{w=0.5} Como el Salón Batalla requiere permiso para pelear ahí, apuesto a que podemos ver algunas peleas geniales en el gimnasio."
leaf @flirttalk blush "Además, parece que te vendría bien un buen entrenamiento."

red @upeyes angryeyebrows talking2mouth "¡Oye!"

leaf @happy "¡Estoy bromeando!{w=0.5} Es obvio que te mantienes en forma. Probablemente vas al gimnasio todos los días, ¿verdad? Seguro terminas todo sudado y jadeando como un Slowpoke cansado."

pause 2.0

red @closedbrow talking2mouth sweat "Leaf, te lo ruego, quien sea que te enseñó a coquetear, necesitas dejar de escucharle."

leaf @happy "¡Oye, esto no lo saqué de {i}nadie{/i}! ¡Mi técnica es 100\% original de Leaf! ¡De cosecha propia y casera, directo de mi huerto!"

red @unamusedbrow talking2mouth "Tu 'técnica' me da ganas de comer comida rápida."

pause 1.0

leaf @sad "... ¿Qué sería comida rápida en este contexto?"

red @sigh "Mejor no--"

leaf happy "¡No importa, vamos!"

hide leaf with dis

pause 0.5

window hide

show blank2 with dis

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_11
$ renpy.music.stop(channel='crowd', fadeout=1.5)
stop music fadeout 1.5
$ renpy.pause(2.0, hard=True)

############################################################################################################################################################################################################################
#### KORRINA INTRO #########################################################################################################################################################################################################
############################################################################################################################################################################################################################
#### NO IT ISN'T ###########################################################################################################################################################################################################
############################################################################################################################################################################################################################

play music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.0)

$ renpy.transition(dissolve)
show screen currentdate

scene gym with Dissolve(2.0)

hide blank2

$ renpy.pause(1.0, hard=True)

show leaf uniform with dis

leaf @talkingmouth "Guau, hay muuucha gente aquí." 

red uniform @talkingmouth "Supongo que tiene sentido, es un buen lugar para combatir {i}y{/i} hacer ejercicio. Viene bien a todo tipo de personas."

leaf @closedbrow talkingmouth "Está un poco lleno,{w=0.5} tal vez deberíamos intentar en otro lugar..."
show leaf surprisedbrow frownmouth with dis

pause 1.5

red @confused "¿Hmm? ¿Qué pasa?"

leaf surprisedbrow frownmouth @surprised "¡Detén la puerta delantera! ¡¿Ella es la jodida {i}ROSA{/i}?!"

$ rosanamed = persondex["Rosa"]["Named"]

if (rosanamed):
    if (classstats["Electric"] > 0):
        red @confused "¿Eh? {w=0.5}{nw}" 
        extend @talkingmouth "Oh, sí, lo es. Quiero decir, tomamos juntos la electividad de tipo Eléctrico, ¿verdad?"

        leaf @angry "¡Qué! ¡Eso es mentira! No hay {i}forma{/i} de que no me diera cuenta."

    else:
        red @confused "¿Eh? {w=0.5}{nw}" 
        red @talkingmouth "Oh, sí, lo es. La conocí antes en mi clase electiva."

        leaf @angry "¡{i}Cállate{/i}! ¡{i}No{/i} lo hiciste!"

    red @happy "Claro que sí."

    leaf @angry "Bueno... ¡como sea! ¡Voy a hablar con ella!"

    red @confused "¿De qué la conoces?"

else:
    red @confused "¿Quién es ella?"

leaf @surprised "¡No puede ser! ¿No conoces a Rosa? ¿La Reina de Pokéstar Studios? ¡¿Una de las actrices más talentosas {i}de todos los tiempos{/i}?!"

red @talking2mouth "Bueno, no vi muchas películas en Pueblo Paleta. Y la mayoría de las que vi estaba en VHS, las cuales supongo que son un poco más viejas que ella."

leaf -surprisedbrow -frownmouth @happy "¡Oh, Dios mío, tengo {i}tantas{/i} películas que mostrarte! Es legendaria. Hay una escena en {i}Cronodisea{/i} donde su personaje queda enterrado bajo escombros, le arrancan un brazo..."
leaf @happy "¡Y grita y llora de forma {i}tan realista{/i} que si el volumen de tu televisor está demasiado alto, tus vecinos llamarán a la policía!"

red @confused "Eso es... ¿genial?"

leaf @embarrassedbrow talkingmouth "Oh, y una vez, cuando estaba filmando {i}Amor a Primera Vista{/i}, ¡el actor que interpretaba a su interés amoroso {i}realmente se enamoro de ella!{/i} ¡Incluso le propuso matrimonio!"
leaf @happy "Lo leí en una revista."

red @confused "Aja..."

pause 1.0

leaf @talking2mouth angrybrow "Espero más que un 'aja' por presentarte a la mejor actriz que haya existido."

red @talking2mouth "Es solo que... tiendo a preferir películas como las de Diantha, ¿sabes?"

leaf surprisedbrow frownmouth @surprised "{w=0.5}.{w=0.5}.{w=0.5}."
leaf surprisedbrow @talking2mouth "¿Como... películas antiguas en blanco y negro?"

red @confused "¿Cuántos años crees que tiene? No, me refiero a un cine moderno."
red @closedbrow talkingmouth "Aunque supongo que también me gustan los viejos westerns de nieve de Brycen."

leaf "{w=0.5}.{w=0.5}.{w=0.5}."
leaf -surprisedbrow -frownmouth @closedbrow talking2mouth "Voy a ser la mujer más grande de esta conversación y te dejaré con tu pésimo gusto."
leaf @happy "¡Oh! ¡Esa es otra de sus películas! '¡La Mujer Gigante!'"

red @wince talking2mouth "Incluso sin haberla visto, puedo decir que es el fetiche del director pobremente disimulado."

leaf @closedbrow talkingmouth "Sí, en realidad lo era..."

pause 2.0

leaf @happy "¡Bueno, como sea! ¡Voy a hablar con Rosa! ¡Nos volveremos las mejores amigas, y me pondrá como extra en sus películas!"

red @happy "Qué oportunista."

show rosa with dis:
    xpos 0.66

show leaf:
    xpos 0.5 xzoom 1
    ease 0.5 xpos 0.33 xzoom -1

leaf @happy "¡Rosa!"

$ BecomeNamed("Rosa")

show leaf:
    xpos 0.33 xzoom -1

show rosa:
    xpos 0.66

rosa @surprised "¿Eh?"
rosa @talkingmouth "Oh, hola. Debes ser una fan."

leaf @surprised "¡Totalmente, soy tu mayor fan! ¡Oh, Dios mío! ¡Es Rosa!{w=0.25} ¡Eres realmente tú!"

leaf @happy "[first_name], ¡¿puedes creerlo?!"

red @happy "¡Seguro que no!"

show rosa happybrow sweat with dis

leaf @embarrassedbrow talkingmouth "He visto {i}todas{/i} tus entrevistas! ¡Eres increíble! ¿Es cierto que cuando estabas filmando {i}Juncobot{/i}, la Policía Internacional visitó el estudio porque pensaron que {i}realmente eras{/i} una ladrona de joyas?"

rosa @talkingmouth "¡Ja, ja! ¡Quizás!"
rosa @closedbrow sweat talking2mouth "... Pero, por razones legales, no."

leaf @happy "¡Soy como, tu mayor fan {i}de todos los tiempos{/i}! ¿Ya no lo había dicho? No importa, sigue siendo verdad."

if (not rosanamed):
    leaf @happy "¿Qué haces aquí? ¿Eres una oradora invitada? ¿Te contrataron para dar clases?"

    rosa @happy "Jaja, ¿qué? No. Solo tengo veinte años, ¿sabes? Solo estoy estudiando aquí--"

    leaf @surprised "¡{i}AH!{/i}! ¡¿Estás inscrita aquí?!{w=0.5} ¡Pellízquenme, estoy soñando!"
    
leaf @flirttalk "Oye, ¿en qué dormitorio vives? ¿Puedo ver tu habitación alguna vez? ¿Qué tal ahora?"

redmind @unamusedbrow unamusedmouth "Bueno, {b}ahora{/b} es momento de intervenir."

show leaf surprisedbrow frownmouth with dis

red @sadbrow talkingmouth "Leaf,{w=0.5} calmate."
    
leaf @surprised "Pero..."

rosa -sweat -happybrow @talkingmouth "Nah, está bien.{w=0.5} Aprecio el entusiasmo, pero soy solo una estudiante aquí, ¡como tú!"
rosa @happy "Si no estoy frente a una pantalla verde, no hay razón para tratarme diferente a los demás."

leaf @sadbrow talkingmouth "Oh, Dios, lo siento." 
leaf -surprisedbrow -frownmouth @happy "Es solo que nunca pensé que mi ídola estaría tan cerca de mí, y hablándome cara a cara..."

rosa @happy "¡No te preocupes!"

pause 0.75

if (rosanamed):
    rosa @talkingmouth "... Ah, hola, [first_name]."

    red @happy "Hola."

    rosa @sadbrow talkingmouth "Supongo que ahora entiendes por qué estaba un poco rara en clase antes, ¿eh?"

    red @happy "No diría eso, pero si que {i}explica{/i} un par de cosas."
    
rosa @talkingmouth "Bueno, señorita, creo que no escuché bien tu nombre.s{w=0.5} ¿Me lo podrías repetir?"

leaf surprisedbrow frownmouth @surprised "¡Oh, soy Leaf! Leaf es mi nombre. ¡Y este es [first_name]! Puedes llamarlo [first_name]. Es un nombre un poco tonto, ¿verdad?"
      
rosa @surprised sweat "¿Tonto? Um, yo no diría... O sea, eso no es lo primero que diría..."

leaf @happy "Lo sé! ¡{i}Suuuuper{/i} tonto! ¿Ja,ja,ja? ¡Ja!"

show leaf surprisedbrow frownmouth with dis

red @closedeyes talkingmouth "Es una regla implícita no tirar a tus amigos debajo del autobús, Leaf. {w=0.5}{cps=*0.2}{nw}" 
extend @noeyes shadow frownmouth "{color=#f00}Voy a recordar esto.{/color}"

show leaf sadbrow -frownmouth with dis

pause 1.5
    
rosa @surprisedbrow talking2mouth sweat "¡Guau, miren la hora!{w=0.5}{nw}" 
extend @sadbrow talkingmouth " Se termino mi descanso, ¡debo de volver a mi entrenamiento! Cada gramo extra son cinco semanas más de trabajo para el equipo de CGI."
rosa @happy "Lo siento, chicos, tengo que salir corriendo...{w=0.5} ¡Literalmente!"

show rosa happybrow sweat with dis
    
leaf -sadbrow @happy "¡Ja! ¡Esa fue buena, Rosa! {w=0.5} ¡Ja,ja,ja! ¡Me duele el estómago de la risa!"

rosa @talkingmouth "Bueno, encantada de conocerte, Leaf. {w=0.5} ¡Nos vemos!"

hide rosa at rightside with dis

pause 1.0

hide rosa

red @happy "Parece ser alguien agradable."

leaf -happy @talkingmouth "¡Ella es {i}muy{/i} agradable!"
leaf @happy "Escuche mcuhas historias sobre actores que son unos completos idiotas fuera de la pantalla, pero Rosa obviamente no es así."

leaf @talkingmouth "Si pudiera terminar el año siendo amiga de Rosa, sería tan feliz."

red @talkingmouth "Parece que ustedes dos se llevarían bien."

leaf @surprised "¿De verdad lo crees?"

red @happy "Claro, solo tal vez deberías bajar un poco la intensidad del fanatismo."

leaf thinking @angrybrow talking2mouth "¡¿Disculpa?! ¡Yo no...!"

pause 2.0

leaf -thinking @sadbrow talkingmouth ".{w=0.25}.{w=0.25}.{w=0.25}Intentaré controlarlo."

red @confused "Entonces, ¿todavía quieres quedarte aquí?{w=0.5} Se ve bastante lleno."

leaf @talking2mouth "Sí...{w=0.5} Definitivamente no."
leaf @talkingmouth "Probemos otro lugar."

hide leaf with dis

window hide

show blank2 with Dissolve(1.5)

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_12
$ renpy.music.stop(channel='crowd', fadeout=1.5)
stop music fadeout 1.5
$ renpy.pause(2.5, hard=True)

show night at vspaz

pause 3.5

############################################################################################################################################################################################################################
#### END OF DAY ############################################################################################################################################################################################################
############################################################################################################################################################################################################################

play music "Audio/Music/SoaringIllusions_Intro.ogg" noloop
queue music "Audio/Music/SoaringIllusions.ogg"

$ renpy.transition(dissolve)
show screen currentdate

$ timeOfDay = "Night"

scene relichall_B with Dissolve(2.0)

hide blank2
hide night

show leaf uniform happy at night with dis

narrator "Terminas deambulado por el campus durante un rato, hablando de nada en particular con Leaf."
narrator "Bajo la cobertura de esta charla trivial, la noche cae."

leaf frownmouth @surprised "¿Ya es esa hora del día?{w=0.5} Mierda, tenemos que volver a los dormitorios antes de meternos en problemas."

red night uniform @sigh "Estaba pensando... ¿es realmente un gran problema si nos atrapan afuera después del anochecer?"

leaf -surprisedbrow -frownmouth -surprised @sarcastic "Si lo haces muy seguido, la academia podría suspenderte o incluso expulsarte.{w=0.5} Personalmente, me encantaría salir y hacer cosas, pero con tanto tiempo y dinero en juego, simplemente no vale la pena."
leaf @talking2mouth "De todos modos, Kobukan es súper elegante y todo eso, pero Ciudad Inspira está llena de delincuentes y matones que a veces merodean por la noche."
leaf -frownmouth @happy "Aunque mis habilidades en batalla son de élite y puedo derrotar a cualquiera que intente algo, tú quizás deberías mantenerte alejado."

red @talking2mouth "Sí, sí, soy muy delicadito."

leaf @surprised "...{w=0.5} ¡Oh, mira la hora! No quería extenderme tanto con eso."
leaf @happy "Fue divertido mientras duró, pero realmente deberíamos regresar."

red @sadbrow talkingmouth "or mí está bien. Gracias por el recorrido y, eh, por el tutorial sobre cómo usar mapas."

leaf happy "¡Buenas noches!"

hide leaf at night with dis

pause 2.0

redmind @thinking "Leaf no bromeaba.{w=0.5} Este lugar parece un pueblo fantasma cuando se acerca la hora del toque de queda."

window hide

show blank2 with dis

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_13

$ renpy.pause(2.0, hard=True)

$ renpy.transition(dissolve)
show screen currentdate

$ PlaySound("Door_Open1.ogg")
scene dorm_B norm with Dissolve(2.0)

hide blank2
hide relichall_B

red uniform @talkingmouth "Phew!"

$ PlaySound("Door_Close1.ogg")

red @happy "Por fin de vuelta.{w=0.5} Es solo el primer día de clases y ya siento que podría dormir el resto de la semana."
red @happy "¡Hola, chicos, ya volvi!"

$ renpy.music.play("Audio/Pokemon/pikachu_norm1.ogg", channel="altcry", loop=None)

pikachu happy_3 "¡Pi-KA-chu!"

red @happy "¡Hola, [pika_name]! ¿Me extrañaste?"

$ renpy.music.play("Audio/Pokemon/pikachu_norm4.ogg", channel="altcry", loop=None)

pikachu happy_3 "Pika-pika."

show calem at leftside with dis

calem @talkingmouth "Yo diría que sí te extrañó.{w=0.5} Desde que volví, no ha dejado de mirar la puerta."

show brendan at rightside with dis

brendan @happy "¡Es como un pequeño robot!"

calem @closedbrow talkingmouth "Es muy tierno de ver, aunque un poco inquietante."
calem smilemouth @talkingmouth "En fin, ¿cómo te fue en el día?"

red @happy "Considerado todo, estuvo bien.{w=0.5} Conseguí un nuevo Pokémon, así que eso fue bastante genial."

calem @surprised "¿Oh? ¿Un nuevo Pokémon? ¡Fantástico!" 
calem @happy "Yo recibí un Fletchling en mi salón con el Profesor Ciprés."

brendan @happy "¡El Profesor Birch me dio un Mudkip! Cuando este pequeño evolucione a Swampert, ¡será uno de los mejores tipo tierra de Hoenn!"

red @talkingmouth "Comparto clases generales con Hilbert, y dijo que consiguió un Cubchoo. Aunque estoy bastante seguro de que lo va a evolucionar en Beartic lo antes posible."

show ethan with dis

ethan @happy "Bueno, ¿qué conseguiste tú?"

show ethan surprisedbrow frownmouth with dis
show calem surprisedbrow with dis
show brendan surprisedbrow frownmouth with dis
red @happy "¡Yo conseguí un [starter_name]! Lo cual es una locura, porque siempre quise uno cuando era niño."
if (starter_name == "Mudkip"):
    red @happy "¡Parece que tenemos dos Mudkip en este dormitorio ahora!"

pause 2.0

red @confused "¿Qué pasa?"

show calem happy with dis
show brendan happy with dis
ethan happy "Bro, ¡yo también tengo un [starter_name]!"

show brendan -happy with dis
show calem -happy with dis
red @happy "¿En serio? ¡Guau! Las coincidencias entre nosotros no paran de acumularse."
if (starter_name == "Mudkip"):
    red @talkingmouth "No puedo creer que tres de nosotros cinco termináramos con Mudkip, es una locura."

ethan @talkingmouth "Totalmente."
ethan @happy "Oigan chicos, hoy pasó algo loquísimo. ¡Resulta que yo y [first_name] elegimos las mismas electividades! ¡En el mismo orden y todo!"

calem @closedbrow talkingmouth "Hmm... las probabilidades de que ocurra algo así son bastante bajas."

if (GetStatRank(0) in classdex["Calem"] and GetStatRank(1) in classdex["Calem"]):
    calem @happy "Aunque, de hecho, [first_name] y yo también estuvimos en las mismas electividades."
elif (GetStatRank(0) in classdex["Brendan"] and GetStatRank(1) in classdex["Brendan"]):
    brendan @surprised "Vaya, ¿qué probabilidades hay de que Ethan, [first_name] y yo hayamos tomado las mismas electividades?"

    calem @happy "Son incluso más bajas."

red @talkingmouth "Cambiando de tema, ¿qué les parecieron las clases?"

calem @closedbrow talking2mouth "Hasta ahora han sido bastante tranquilas.{w=0.5} No muy diferentes de la preparatoria, para ser honesto."
calem @happy "Pero muchas personas dicen que el cambio no siempre es bueno, así que tal vez debería sentirme afortunado."

brendan @sadbrow talking2mouth "Hombre, sé que estas clases van a matarme en cualquier segundo."
brendan @closedbrow sweat talking2mouth "¡Nunca había sentido tanta presión académica en mi vida!"

calem @sad "¿En serio? {i}Apenas{/i} es el primer día de clases.{w=0.5} ¿No crees que es demasiado pronto para declararlo una causa perdida?"

brendan @sad "Hombre, no soy la herramienta más afilada de este cobertizo, por lo que cualquier clase de este lugar es difícil para mí en este momento."

ethan @confused "Yo básicamente siento... bueno, como si nada hubiera comenzado todavía."
ethan @happy "Quiero decir, no hemos tenido exámenes, no hemos tenido batallas y ni siquiera hemos tenido que atrapar nuevos Pokémon... ¡Es como si todavía estuviéramos en el tutorial!"

brendan frownmouth sadbrow @sad "Oh, no... ¿y yo ya estoy teniendo problemas en el {i}tutorial{/i}? Estoy perdido, hombre..."

narrator "Tú y tus compañeros de cuarto pasan un rato asegurándole a Brendan que, de hecho, no está perdido."

show brendan -frownmouth -sadbrow with dis

narrator "Eventualmente, la conversación vuelve a girar en torno a tu nuevo Pokémon, y..."

$ starter_name = pokedexlookup(starter_id, DexMacros.Name)
red @happy "Come on out, [starter_name]!"

$ PlaySound("Pokemon/Ball sound.ogg")

show starterportraitfull at pokeball, dormdesk
show calem:
    xpos 0.25
    ease 0.5 xpos 0.1

show ethan:
    xpos 0.5
    ease 0.5 xpos 0.25

show brendan:
    xpos 0.75
    ease 0.5 xpos 0.8

$ renpy.pause(0.5, hard=True)
$ renpy.music.play("Audio/pokemon/cries/{}.mp3".format(starter_id), channel="altcry", loop=None)

$ startercrop = starter_name[:3]
starter @talkingmouth "¡[startercrop]!"

redmind "Hmm... Ahora que lo pienso, ¿debería ponerte un apodo?"

label nicknamestarter:

$ starter_name = renpy.input("{color=#e70000}¿Cuál es el apodo de tu inicial? (Presiona Enter para utilizar el predefinido){/color}", length=12, exclude="{}[[]%<>",)
$ starter_name = starter_name.strip()

if starter_name == "" or starter_name == pokedexlookup(starter_id, DexMacros.Name).lower():
    $ starter_name = pokedexlookup(starter_id, DexMacros.Name)

red @closedbrow talking2mouth "Hmm... Creo que [starter_name] te queda perfecto."

menu:
    "Sí, suena bien, [starter_name].":
        pass

    "Espera, tengo una mejor idea.":
        jump nicknamestarter

$ playerparty[0].Nickname = starter_name

red @talkingmouth "¡Bienvenido al equipo, [starter_name]!"
    
$ renpy.music.play("Audio/pokemon/cries/{}.mp3".format(starter_id), channel="altcry", loop=None)

$ species_name = pokedexlookup(starter_id, DexMacros.Name)
starter @talkingmouth "¡[species_name]!"

$ startergender = "él" 
if (playerparty[0].GetGender() == Genders.Female):
    $ startergender = "ella"
elif (playerparty[0].GetGender() == Genders.Unknown):
    $ startergender = "él"

brendan @happy "¡Wow! Miren eso, ¡[startergender] ya te tiene cariño!"
brendan @talking2mouth "No es común que un Pokémon se encariñe tan rápido con su entrenador justo después de conocerlo."

red @confused "¿Deberás?{w=0.5}. No lo había notado, [starter_name] actúa prácticamente igual que [pika_name] hace unos años atrás."

brendan @surprised "¿E-en serio?{w=0.5} Entonces, ¿será que mis Pokémon no confían en mí?"

calem @closedbrow talkingmouth "No creo que sea eso. De hecho, me sorprendió que soltaras a [starter_name] aquí en la habitación, [first_name]. Pensé que tendríamos que ponernos a cubierto."

$ startergendercap = startergender.capitalize()
red @confused "¿A qué te refieres? [startergendercap] es un bebé Pokémon. No puede causar {i}tantos{/i} destrozos."

calem @sad "Es cierto, pero, más allá de eso... [startergender] no está causando {i}ningún{/i} destrozo."

$ startergenderpronoun = "él" 
if (playerparty[0].GetGender() == Genders.Female):
    $ startergenderpronoun = "ella"
elif (playerparty[0].GetGender() == Genders.Unknown):
    $ startergenderpronoun = "él"

ethan @confused "Esperen un segundo, ahora estoy confundido. Estan actuando como si esperaban que el amiguito de [first_name] se volviera loco cuando lo dejara salir."

calem @surprised "¿Acaso tú no? [startergendercap] es un Pokémon bebé, como dijiste. No ha recibido ni una pizca de entrenamiento. Pero [startergender] simplemente está ahí... {i}quieto{/i}, esperando."

ethan @happy "Calem, ¿nos estás tomando el pelo? Así son los Pokémon."

calem @angrybrow talking2mouth "Te aseguro que los numerosos Pokémon bebé que el Profesor Ciprés me endilgó durante mi pasantía estarían en desacuerdo."

brendan @closedbrow talkingmouth "Hombre, ya no sé qué pensar. Todos mis Pokémon tardaron semanas en acostumbrarse a mí." 
brendan frownmouth @sad "Pensé que eso era lo normal, pero ahora que ustedes dicen lo contrario, tal vez soy malo con los Pokémon."

show brendan:
    xpos 0.8
    ease 0.5 xpos 0.7

show hilbert at dissolvein:
    xpos 0.8

hilbert @talkingmouth "Probablemente lo seas."

calem @angry "¡Hilbert!"

hilbert @talkingmouth "Déjame terminar."

hilbert @talkingmouth "Independientemente de si alguien aquí es bueno o malo con los Pokémon, la experiencia de Ethan y [first_name] no es típica." 
hilbert @talkingmouth "Si todos soltáramos a nuestros Pokémon nuevos ahora mismo, esta habitación sería un desastre."
hilbert @talkingmouth "... Así que no eres el raro aquí, Brendan."

brendan happy "¡Ja! ¡Genial!"

pause 1.0

brendan -happy @closedbrow talking2mouth "Un momento... ¿no se supone que ser el raro en este caso es algo bueno?"

red @confused "Quizá podamos preguntarle al profesor Oak. Quería hacerle algunas preguntas antes, de todos modos."

red @surprised "De hecho... Ethan, ¿con qué profesor tienes clases generales? Ya que tenemos el mismo inicial y las mismas electivas, me sorprende que no estemos en la misma clase general."

ethan @surprised "¡Oh, cierto! Estoy con Kr--{w=0.5} digo,{w=0.25} uh,{w=0.25} la Profesora Cherry."

red @closedbrow talking2mouth "Hmm... no recuerdo a nadie con ese nombre en la lista de profesores."

ethan @happy "Sí, la contrataron hace poco. Y es... bueno, es bastante peculiar."

red @talkingmouth "En fin, veré si mañana llego temprano a la clase general para preguntarle al Viejo O--{w=0.5} digo,{w=0.25} al Profesor Oak,{w=0.25} sobre por qué nuestros Pokémon son raros."

redmind @thinking "O del porqué no lo son, supongo."

ethan @happy "¡Suena como un plan! Ahora me voy a dormir. ¡Buenas noches a todos!"

hide hilbert
hide brendan
hide calem
hide ethan
with dis

red @talkingmouth "Suena bien.{w=0.5} ¿Qué hay de ustedes dos? ¿Listos para ir a la cama?"

$ renpy.music.play("Audio/Pokemon/pikachu_norm3.ogg", channel="altcry", loop=None)

pikachu happy "Pika."

$ renpy.music.play("Audio/pokemon/cries/{}.mp3".format(starter_id), channel="altcry", loop=None)

$ starter_fragment = pokedexlookup(starter_id, DexMacros.Name)[:3]
starter @talkingmouth "[starter_fragment]!"

window hide

$ PlaySound("Pokemon/Ball sound.ogg")

show starterportraitfull at backinpokeball, dormdesk

pause 1.0

show dorm_B lightsout

pause 1.0

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_14

show blank2 with transeye

narrator "Mientras te acomodas en la cama, ni siquiera tienes tiempo de darte cuenta de lo agotado que estás.{w=0.5} Ni un minuto después de que tu cabeza toca la almohada, caes en un sueño profundo."

window hide

stop music fadeout 1.0
$ renpy.pause(1.0, hard=True)

hide dorm_empty_B
hide blank2

jump day010406
