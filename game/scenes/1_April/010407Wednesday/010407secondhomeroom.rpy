label secondhomeroom010407:

$ timeOfDay = "Evening"

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=True, fadein=1.0, tight=None)

scene blank2

show homeroom behind blank2

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with dis

show oak with dis

narrator "Corres hacia tu salón de clases, logrando interceptar al Profesor Oak antes de que empiece la clase."

red uniform @angrybrow talkingmouth "¡Sam! Tenemos que hablar."

oak @talkingmouth "Eso haremos, [first_name]. Pero este no es ni el momento ni el lugar."

red @sad "¿Pero por qué, Sam? ¿Hice algo mal?"

oak @happyeyes happyeyebrows talkingmouth "Tú más que nadie deberías saber que si creyera que hiciste algo mal, te lo diría."
oak @talkingmouth "No chico, no hiciste nada malo." 
oak @closedeyes talkingmouth "Simplemente necesito tiempo para ordenar mis pensamientos. Dada la importancia de esta conversación, no quiero decirte nada... incorrecto."

hide oak 
show oakbg 
with dis

redmind @closedbrow frownmouth sweat "Así es Sam. Un hombre brillante, brillante, pero nada menos que un milagro puede hacer que se mueva en el horario de cualquier otra persona..."

show blank2
hide oakbg 
with dis

pause 2.0

$ PlaySound("BellChime.ogg")
$ renpy.pause(1.5, hard=True)

$ renpy.music.play("Audio/Music/Beyond2.ogg", channel='music', loop=True, fadein=1.0)

$ renpy.pause(2.0, hard=True)

hide blank2 with splitfade

$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

$ PlaySound("vibrate.ogg", instant=True)
$ renpy.pause(0.5, hard=True)

redmind @thonk "Hmm?"

show phone_B
show phone_A
with fadeinbottom

show phone_C behind phone_A with dis

show phone_msg1 behind phone_A with dis

$ roommate_msg = Text("Calem",size=30,font="fonts/consola_0.ttf",color="#313131")

image calem_msg = Text("Tengo que ocuparme de algo en el\nSalón Reliquia antes de ir. B&E iran\nconmigo. Ve tú primero, nos vemos en un rato.",size=21,color="#ffffff",line_spacing=5,text_align=0.0)

show text roommate_msg behind phone_A:
    alpha 0.0 xalign 0.51 yalign 0.34
    ease 0.25 alpha 1.0

show calem_msg behind phone_A:
    alpha 0.0 xpos .41 ypos .4
    ease 0.25 alpha 1.0

pause 5.0

redmind "¿B&E? ... Ah, Brendan y Ethan. Bueno, qué se le va a hacer.{w=0.5} Supongo que voy a ver el lugar solo."

hide phone_A
hide phone_B
hide phone_C
hide phone_msg1
hide text roommate_msg
hide calem_msg 
with fadeoutbottom
    
$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_28
stop music fadeout 1.5

window hide

show blank2 with splitfade
$ renpy.pause(1.5, hard=True)
show stadium_empty behind blank2

play music "Audio/Music/League_Start.ogg" noloop
queue music "Audio/Music/League_Loop.ogg"

$ renpy.transition(dissolve)
show screen currentdate
hide blank2 with splitfade

$ renpy.pause(0.5, hard=True)

############################################################################################################################################################################################################################
#### JANINE INTRO ##########################################################################################################################################################################################################
############################################################################################################################################################################################################################

scene stadium_empty

redmind uniform "Hombre, justo cuando pensaba que ya me estaba acostumbrando a la extravagancia de esta academia..."
redmind "Sé que nuestro equipo de batalla es súper exitoso y todo, pero ¿exactamente cuánto dinero usaron para hacer este estadio?{w=0.5} ¡Es enorme!"

blue uniform angry "{size=18}¡T{/size}{size=20}E{/size} {size=22}ES{/size}{size=24}TOY{/size} {size=26}DI{/size}{size=28}CI{/size}{size=30}EN{/size}{size=32}DO{/size} {size=34}QUE{/size} {size=36}TE{/size} {size=38}QUI{/size}{size=40}TES{/size} {size=42}DEL{/size} {size=44}ME{/size}{size=46}DIO{/size}{size=48}!{/size}"

redmind @unamusedbrow unamusedmouth "Ah, genial. [blue_name].{w=0.5} ¿Qué estará intentando hacer ahora?"

show blue with dis:
    xpos 0.66 xzoom -1

show janine with dis:
    xpos 0.33

janine @talking2mouth "¡Y yo te estoy diciendo que todavía no aceptamos nuevos miembros!{w=0.5} Tanta cantidad de pelo debe estar aplastando ese cerebro diminuto tuyo!"

red @talkingmouth "Eh, hola. ¿Aquí es donde se reúne el equipo de batalla?"
    
janine @angrybrow talking2mouth "¿Otro más?"
janine @closedbrow talking2mouth "Mira, si vienes a quejarte del proceso de selección, no quiero ni escucharlo."

red @talkingmouth "¿Yo? No, no estoy tratando de unirme... por ahora.{w=0.5} ¿Eso es lo que está intentando hacer [blue_name]?"

janine @closedbrow talking2mouth "Sí, ¿lo conoces?{w=0.7}{nw}"
extend @angrybrow talkingmouth " Por favor, ¡dile que lo único que está logrando acosándome es que lo ponga en mi lista de 'ni en sueños'!"

red @happy "¿Oíste eso, [blue_name]? Dijo que--"

blue @angry "¡Cállate y déjame entrar!{w=0.5} ¿Tienes idea de lo que puedo hacer?"

janine @talking2mouth "Sí, ser insoportable a más no poder."
janine angry "Esta conversación se acabó."

$ renpy.music.stop(channel="crowd")

show blank2
call clearscreens from _call_clearscreens_29
$ PlaySound("Metal Door Slam.ogg")

stop music fadeout 2.0

hide janine
hide blue
hide stadium_empty

$ renpy.pause(2.0, hard=True)

show map behind blank2
show map_corner behind blank2:
    xalign 0.0 yalign 1.0
    
$ renpy.transition(dissolve)
show screen currentdate

show blank2:
    alpha 1.0
    ease 2.0 alpha 0.0
    
play music "Audio/Music/Beyond2.ogg" loop fadein 2.0
$ renpy.pause(2.5, hard=True)

hide blank2

blue uniform angry "¡Psh! Se cree la gran cosa solo porque es hija de un miembro del Alto Mando."
blue @talkingmouth "¿Y tú qué haces aquí?{w=0.5}{nw}"
extend @angrybrow talkingmouth " Espera, déjame adivinar. Tú también intentas unirte al equipo de batalla, ¿verdad?"

red @talkingmouth "No, solo estaba--"

if WonBattle("Blue1"):
    blue @angry "¡Ni lo intentes!{w=0.5} Debes creer que eres un peso pesado solo porque me ganaste en esa pelea de práctica."
    blue @angry "¡Pues adivina qué! Ni siquiera lo estaba intentando.{w=0.5} Sí, me ganaste con los Pokémon que nos dio la escuela para empezar, ¡gran cosa!"
    blue @angry "¡Ya verás! Mis Pokémon van a ser los más fuertes de esta escuela.{w=0.5} {i}Ahí{/i} veremos quién es el mejor Entrenador."

else:
    blue @talkingmouth "¡JA! Eres aún más tonto de lo que pensaba.{w=0.5} Te falta un siglo para siquiera {i}pensar{/i} en entrar."
    blue @happy "Fui suave contigo en la pelea de práctica y ni así pudiste ganarme."
    blue @closedbrow talkingmouth "Si intentas entrar ahora, serás la burla de toda la escuela.{w=0.5} ¡Solo arruinarías la reputación de nuestro pueblo!"

    redmind @confusedeyebrows frownmouth "¿Qué reputación?"

    blue @closedbrow talkingmouth "Espera… si descubren que los dos somos de Pueblo Paleta, entonces.{w=0.25}.{w=0.25}.{w=0.5} y yo..."
    
    pause 1.0
    
    blue "[ellipses]"
    
    pause 1.5
    
    show map:
        parallel:
            xalign 0.0
            ease 0.03 xpos -15
            ease 0.03 xpos 15
            ease 0.03 xpos 0
            repeat 3
        parallel:
            yalign 0.0
            ease 0.03 ypos -30
            ease 0.03 ypos 30
            ease 0.03 ypos 0
            repeat 3
    
    blue angry "¡Escucha, [first_name]! Más te vale ponerte las pilas.{w=0.5} Si sigues siendo tan mediocre como ahora, ¡vas a arruinar mi reputación!"
    
    red @talkingmouth "No creo que tengas que preocuparte por eso."
    
red @confused "En fin, ¿qué esperabas?{w=0.5} No me digas que realmente pensaste que te dejarían entrar así como así..."

blue @angry "¿Y qué tiene que ver eso?{w=0.5} Es obvio que yo debería enfrentarme a los mejores Entrenadores de esta academia."
blue @closedbrow talkingmouth "Bah, da igual si no quieren pelear.{w=0.5} Voy a ver sus estrategias con mis propios ojos en unas horas."
blue @closedbrow talkingmouth "Apuesto a que ni idea tienes, pero la Capitana del equipo de batalla va a hacer una exhibición esta noche.{w=0.5} Toda la escuela va a estar ahí."

red @talking2mouth "Es mucho revuelo para una simple exhibición."

blue @angry "¿Eres tonto o te caíste  cuando eras un bebe?{w=0.5} Estamos hablando del {i}equipo de batalla de la Academia Kobukan{/i}."
blue @closedbrow talkingmouth "Tch, ¿por qué rayos sigues en esta academia?"
blue @angrybrow talkingmouth "Bah, qué más da. ¡Alguien tiene que representar a Pueblo Paleta, y definitivamente no serás tú! ¡Me piro, vampiro!"

pause 2.0

redmind "Dejando de lado las payasadas de [blue_name], esa exhibición suena como una forma interesante de pasar la noche.{w=0.5} Ciertamente mejor que quedarme encerrado en mi habitación."
redmind @thinking "De todos modos, esta puerta no parece que se vaya a abrir pronto."
redmind "Debería avisarle a los chicos sobre la exhibición."

pause 1.0

show blue angry with vpunch

blue frownmouth @talkingmouth "¡Hey!"

red @unamusedbrow talking2mouth "Oh, dios mio. Volviste."

blue angry "Cuando esté en esa exhibición... ¡ni se te ocurra buscarme ni hacer nada raro! No quiero que mis otros amigos piensen que te conozco."

hide blue with dis

redmind @thonk "Ha estado... actuando raro últimamente. Es cierto que dejamos de hablar durante un tiempo en Pueblo Paleta, pero aun así, era un pueblo diminuto. Siempre estábamos a la distancia de un grito, salvo cuando iba a Ciudad Verde."
redmind @thonk "Sé que no está pasando el rato con otro amigo o algo por el estilo. Entonces, ¿qué está {i}realmente{/i} haciendo?"

pause 1.0

redmind @sigh "No es mi circo y tampoco es mi Grookey."


stop music fadeout 1.0
$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_30
    
show blank2 with splitfadefast
$ renpy.pause(1.0, hard=True)

hide map
hide map_corner

############################################################################################################################################################################################################################
#### ROOMMATES' Pokémon ####################################################################################################################################################################################################
############################################################################################################################################################################################################################

queue music "Audio/Music/SoaringIllusions_Intro.ogg" noloop
queue music "Audio/Music/SoaringIllusions.ogg"

show lobby behind blank2

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade
$ renpy.pause(0.5, hard=True)

scene lobby

pause 1.0

show brendan at rightside with dis
show ethan at centerside with dis
show calem at leftside with dis

red uniform @talkingmouth "¡Hey, chicos! Los estaba buscando."

calem @happy "[first_name], justo estábamos a punto de ir a buscarte a {i}ti{/i}."

red @happy "¿Y qué los ha tenido tan ocupados?"

brendan @happy "¡Deja que te los mostremos!"

brendan @talking2mouth "¿Preparados, chicos?"

ethan @talkingmouth "Tres..."
calem @talkingmouth "Dos..."
brendan @talking2mouth "Uno..."

play sound ["Audio/Pokemon/Ball sound.ogg", "audio/pokemon/cries/669.mp3", "audio/pokemon/cries/172.mp3"]
show pichu at pokeball, centerside:
    yalign 1.0 xanchor 0.5
show flabebe at pokeball, leftside:
    yalign 1.0 xanchor 0.5

pause 2.0

brendan @surprised "¡Oh! Creí que contaríamos hasta 'ahora'."
play sound ["Audio/Pokemon/Ball sound.ogg", "audio/pokemon/cries/285.mp3"]
show shroomish at pokeball, rightside:
    yalign 1.0 xanchor 0.5

red @happy "¡Hola, pequeñines! Estos deben ser tus Pokémon de casa, ¿no?"

calem @talkingmouth "En efecto."
ethan @sadbrow talking2mouth "Nos ha tomado una eternidad traerlos hasta aquí, y ni hablemos de los costos de envío..."
calem @talking2mouth "Al menos no estamos en Galar. Si ese fuera el caso, no se nos permitiría traerlos aquí en absoluto."
brendan @closedbrow talking2mouth "Creo que mi pequeñín me echaba de menos.  ¡En cuanto lo solté en el Centro Pokémon, tiro esporas por doquier!"
brendan @surprised "Me metí en un pequeño problema por eso..."
calem @closedbrow talking2mouth "Sí, y mi Flabébé está actuando de forma muy... tsundere."

narrator "Te das cuenta de que el Flabébé de Calem no le presta atención a propósito."

ethan @happy "¡Supongo que a los pequeñitos no les gustó que los dejaran solos durante un tiempo!"

calem @happy "Eso parece."

show flabebe:
    xpos 0.25
    ease 1.0 xpos -0.5

show shroomish:
    xpos 0.75
    ease 1.0 xpos 1.5

show brendan surprisedbrow frownmouth
show calem surprisedbrow frownmouth
with dis

brendan @talking2mouth "¡Shroomish, espera! ¿A dónde crees que vas? ¡Esperame!"
calem @talkingmouth "¿Flabébé? Por favor, no ahora, ¿sí? ¡Te daré toda la atención del mundo más tarde, lo prometo!"

show brendan:
    xpos 0.75
    ease 1.0 xpos 1.5

show calem:
    xpos 0.25
    ease 1.0 xpos -0.5

pause 2.0

ethan "{w=0.5}.{w=0.5}.{w=0.5}."
ethan @talkingmouth "¿Y tú, Pichu? ¿También vas a escaparte?"

$ PlaySound("pokemon/cries/172.mp3")

Character("Pichu") "\"¡Pi-chu!\""

narrator "El Pichu de Orejas Picudas se aferra con fuerza a la pierna de Ethan, dejando en claro que no tiene la menor intención de moverse. No parece asustado, solo... inusualmente afectuoso."

ethan @happy "¡Eres un pan de Dios!"

pause 1.0

ethan @talkingmouth "Ah, cierto, [first_name], habías dicho que querías hablarnos de algo. ¿De qué se trata?"

red @happy "¡Van a hacer una batalla de exhibición en el Salón Batalla! Parece que la capitana del equipo de batalla va a hacer una demostración. Pensé que les gustaría ir a verla."

ethan @happy "¿En serio? ¡Eso suena genial! Deberías volver corriendo a nuestra habitación y traer a [pika_nombre]. Así podremos verla con todos nuestros Pokémon de casa."

red @talkingmouth "¡Gran idea! Aunque... Los Pokémon de Brendan y Calem podrían..."

ethan @closedbrow talking2mouth "Sí... aún no hay suerte averiguando qué nos pasa. O a nuestros Pokémon, supongo. Estuve intentando preguntarle a la profesora Cherry varias veces, pero no he podido averiguar nada."

red @sigh "Yo igual, aunque creo que el Profesor Oak está a punto de decirme algo."

ethan @happy "Bueno, toca cruzar los dedos y ver que pasa."

red @happy "Esperemos que salga bien. Bueno, me voy a buscar a nuestro cuarto. ¿Nos vemos en un rato?"

ethan @talkingmouth "Nos vemos, bro."

hide ethan
hide pichu 
with dis

redmind "Me pregunto qué opinará [pika_name] sobre ver batallas Pokémon competitivas...{w=0.5} Si algún día va a ser el Pokémon de un Campeón, más vale que nos acostumbremos a esto. Lo mismo va para [starter_name]."

hide flabebe
hide brendan
hide shroomish
hide calem
hide blue
hide janine

show blank2 with dis

stop music fadeout 1.5

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_31

$ renpy.pause(3.0, hard=True)
    
show evening at vspaz
$ timeOfDay = "Evening"
    
pause 3.5

hide lobby

$ playerparty.append(Pokemon(25, level=7, nickname=pika_name, ivs=[3, 2, 5, 6, 3, 4], nature=Natures.Lax, gender=Genders.Male, ability="Freelectric"))

show blank as firstblank behind blank2
show stadium_full behind blank2
show blank as secondblank behind blank2
$ renpy.music.play("Audio/Stadium_crowd.ogg", channel='crowd', loop=True, fadein=1.5)
$ renpy.music.play("Audio/Stadium_chant.ogg", channel='crowd2', loop=True, fadein=1.5)

$ renpy.pause(0.75, hard=True)

$ renpy.music.queue("Audio/Music/Indigo_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/Indigo_Loop.ogg", channel='music', loop=True, tight=None)

$ renpy.pause(1.0, hard=True)

hide blank2 with transball
$ renpy.pause(0.25, hard=True)
show blank as secondblank:
    alpha 1.0
    ease 0.5 alpha 0.0

show stadium_full:
    subpixel True
    zoom 3.0 alpha 0.65 xalign 0.15 ypos 2600
    ease 1.25 alpha 1.0 xalign 0.0 ypos 3000
    xalign 0.85 alpha 0.65 ypos 2600
    ease 1.25 alpha 1.0 xalign 1.0 ypos 3000
    xalign 0.5 alpha 0.4 ypos 2400
    ease 1.0 alpha 1.0 zoom 1.0 ypos 1080

show lightbeam1 as beam1:
    pause 2.75
    zoom 0.6 alpha 0.0 yalign 0.9 xpos 0 rotate 40
    block:
        ease 0.25 alpha 0.5
    pause 0.3
    block:
        ease 1.0 rotate -40
        pause 0.5
        ease 1.0 rotate 40
        pause 0.5
        repeat
    
show lightbeam1 as beam2:
    pause 2.75
    zoom 0.6 alpha 0.0 yalign 0.9 xpos -300 rotate -40
    block:
        ease 0.25 alpha 0.5
    pause 0.1
    block:
        ease 1.0 rotate 40
        pause 0.5
        ease 1.0 rotate -40
        pause 0.5
        repeat

show lightbeam1 as beam3:
    pause 2.75
    alpha 0.0 yalign 0.8 xpos -400 rotate -40
    block:
        ease 0.25 alpha 0.6
    pause 0.2
    block:
        ease 1.0 rotate 40
        pause 0.5
        ease 1.0 rotate -40
        pause 0.5
        repeat
        
show lightbeam1 as beam4:
    pause 2.75
    alpha 0.0 yalign 0.8 xpos -1400 rotate 40
    block:
        ease 0.25 alpha 0.6
    block:
        ease 1.0 rotate -40
        pause 0.5
        ease 1.0 rotate 40
        pause 0.5
        repeat
        
pause 3.5

hide blank as firstblank
hide evening
hide blank

$ renpy.transition(dissolve)
show screen currentdate

show stadium_full:
    alpha 1.0 zoom 1.0 yalign 1.0 xalign 0.5

redmind -uniform @surprisedbrow frownmouth "¡Guau, está toda la escuela aquí!{w=0.5} Supongo que al final fue buena idea llegar temprano."

$ renpy.music.stop(channel='crowd2', fadeout=7.0)

show brendan at rightside with dis

brendan @surprised "Sí, sabía que iba a estar a esta hasta arriba, pero esto es una locura."

show calem at leftside with dis

calem @talking2mouth "Y aún hay gente intentando entrar, espero que nadie termine aplastado."

show ethan at centerside with dis

ethan @sadbrow talkingmouth "Es como la semana de orientación otra vez.{w=0.5} Nunca me acostumbro a multitudes así de grandes."

brendan @talking2mouth "Oh, cierto, tú eres de Pueblo Primavera.{w=0.5} ¿No es que ahí viven menos de 1,000 personas o algo así?"

ethan @happy "Algo por el estilo."

if (classstats["Ground"] == 0):
    brendan @happybrow talkingmouth "Por cierto, traje unas Galletas Lava.{w=0.5} Perdón si no te gustan las cosas dulces, a mí tampoco me encantan, ¡pero son una especialidad de Hoenn!"
    
else:
    brendan @happybrow talkingmouth "Por cierto, traje unas Galletas Lava.{w=0.5} No sé si ya probaste alguna en la clase de Bertha, pero son una especialidad de Hoenn y May está {i}obsesionada{/i} con ellas."

show lavacookie at itemhover

$ PlaySound("item_get.ogg")

pause 1.0

show lavacookie at itemhide
$ renpy.pause(1.5, hard=True)

hide lavacookie

calem @happybrow talkingmouth "Imagino que trajiste suficientes para compartir con el grupo, ¿verdad?"

brendan @happy "¡Por supuesto! Y también para nuestros Pokémon. Incluso traje algunas para Hilbert, si es que aparece."

ethan @talking2mouth "Sería raro que no viniera. No hay forma de que se pierda un evento de batallas tan importante, ¿verdad?"

calem @closedbrow talking2mouth "Sin embargo, su presencia no garantiza que lo veamos."

$ renpy.music.play("Audio/Pokemon/pikachu_pikapika1.ogg", channel="altcry", loop=None)

pikachu happy_3 "¡Pika-pika!"

ethan @surprised "¡Oh, hey, [pika_name]! ¿Tú también tienes hambre?"

$ renpy.music.stop(channel='crowd', fadeout=2.0)
$ renpy.music.stop(channel='crowd2', fadeout=2.0)
$ renpy.music.play("Audio/Stadium_murmur.ogg", channel='crowd3', loop=True, fadein=1.5)
stop music fadeout 1.0

pause 1.0

$ renpy.music.play("Audio/Pokemon/pikachu_confused.ogg", channel="altcry", loop=None)
pikachu neutral_4 "¿Pika?"

red @confusedeyebrows talking2mouth "¿Soy yo o de repente todos se quedaron callados?"

brendan surprisedbrow frownmouth @surprised "¡Oye, mira allá, [first_name]!"

hide brendan at rightside with dis
hide calem at leftside with dis
hide ethan at centerside with dis
    
$ renpy.music.queue("Audio/Music/DragonDenStart_B.ogg", channel='music', loop=None, tight=None)
$ renpy.music.queue("Audio/Music/DragonDenLoop.ogg", channel='music', loop=True, tight=None)

$ PlaySound("crowd_cheer.ogg")

$ renpy.music.stop(channel='crowd3', fadeout=2.0)
$ renpy.music.play("Audio/Stadium_crowd.ogg", channel='crowd', loop=True, fadein=1.5)

show lance with dis:
    xpos 200
    ease 1.0 xpos 500

pause 1.5

hide calem
hide brendan
hide ethan

calem @closedbrow talkingmouth "Hmm, Lance.{w=0.5} Tiene sentido que esté aquí."
brendan @surprisedbrow talking2mouth "Sí. Quiero decir, {i}es{/i} el manager del equipo de batalla."

hide lance with dis
show brendan at rightside
show calem at leftside
show ethan at centerside 
with dis

ethan @closedbrow talking2mouth "Es una locura pensar que un Campeón Nacional tiene el tiempo para dirigir el equipo de batalla de una academia cualquiera."
calem @angrybrow talkingmouth "Sería una locura, pero esto es {i}la Academia Kobukan.{/i} Nuestro equipo de batalla es básicamente una fábrica de Campeones."
brendan @happy "Hilbert me dijo que en realidad ganó dos Campeonatos Nacionales. ¡Ganar dos veces es algo casi imposible!"
red @talking2mouth "Sí... No recuerdo bien los detalles, pero creo que por eso las ligas de Kanto y Johto se fusionaron en la Liga Índigo hace como tres años."
ethan @sad "Es impresionante, pero escuché que lo que realmente quiere es ser el Campeón Mundial."
calem @sad "En efecto, escuche que no ha tenido mucha suerte en eso... Aunque, honestamente, ¿cómo se supone que alguien derrote a Leon y Cynthia?" 
calem @closedbrow talking2mouth "Sacando de lado el cuarto puesto, el último Campeonato Mundial fue una masacre a cielo abierto."

red @happy "¡Pareces molesto, Calem! ¿No quedó Diantha en el cuarto puesto, más arriba que Lance?"

calem @happy "Oh, claro, claro. Y fue un momento de orgullo nacional, sin duda. Pero Lance es algo así como un héroe personal para mí." 
calem @closedbrow happymouth "De hecho, aprendí el idioma solo para poder hablar con él algún día."

brendan @happy "¡Bro! ¡Podrías haber tenido tu oportunidad en la clase de gimnasia!"

calem @sadbrow talkingmouth "Eh... sí. Y todavía sigo golpeando mi cabeza contra la pared por no haberla aprovechado."

redmind "Vaya. Si este tipo es tan famoso, me pregunto por qué nunca antes había oído a [blue_name] parlotear sobre él."
redmind "En cualquier caso, Lance suena como el tipo de persona que me hace cuestionar qué estoy haciendo con mi vida..."

$ renpy.music.play("Audio/Pokemon/pikachu_excite5.ogg", channel="altcry", loop=None)

pikachu happy_3 "¡Pikachu~!"

narrator "[pika_name] comienza a llenarse las mejillas con los bocadillos de Brendan."

show brendan surprisedbrow frownmouth
show ethan surprisedbrow frownmouth
show calem surprisedbrow frownmouth
with dis

show lance:
    alpha 0.0 zoom 1.25 xpos 0 ypos 1270
    pause 1.5
    parallel:
        ease 1.5 zoom 1.0 ypos 1080 xpos 250
    parallel:
        ease 0.5 alpha 1.0

red @talkingmouth "¡Heyy, despacio, [pika_name]!{w=0.5} Vas a dejar migas por toda mi ropa."

show lance:
    ease 0.75 alpha 1.0 zoom 1.0 ypos 1080 xpos 250
    
show brendan:
    xpos 0.75
    ease 0.5 xpos 0.85
show ethan:
    xpos 0.5
    ease 0.5 xpos 0.75
show calem:
    xpos 0.25
    ease 0.5 xpos 0.65

lance  @talking2mouth "Tú."

$ renpy.music.stop(channel='crowd', fadeout=1.0)

show lance:
    zoom 1.0 xpos 250 alpha 1.0
    
red @talkingmouth "¿Eh?"

$ renpy.music.play("Audio/Pokemon/pikachu_question.ogg", channel="altcry", loop=None)
pikachu neutral_4 "Pika?"

show brendan:
    xpos 0.85
    ease 0.5 xpos 0.95
show ethan:
    xpos 0.75
    ease 0.5 xpos 0.85
show calem:
    xpos 0.65
    ease 0.5 xpos 0.75

redmind @wince frownmouth "... Siento la mirada de todos sobre mí.{w=0.5} ¿Qué hice?"
red @confusedeyebrows talkingmouth "Eh... ¿Puedo ayudarlo, señor Lance?"

lance @talking2mouth "Inaceptable."
lance @sadbrow talking2mouth "Alimentar a tu Pokémon con...{w=0.5}{nw}"
extend @angrybrow talkingmouth " esta {i}bazofia{/i}."

lance @sadbrow talking2mouth "¿Acaso no tienes la menor idea de las necesidades alimenticias de un Pokémon?"

red @talking2mouth confusedeyebrows "Yo.{w=0.25}.{w=0.25}.{w=0.25} ¿Creia que sí?"

redmind @angrybrow frownmouth "¡Vamos, chicos, qué demonios! ¡Todos lo estábamos haciendo! ¡Ayúdenme!"

show brendan thinking with dis:
    xpos 0.95
    pause 1.5
    ease 0.2 xpos 1.5

show ethan thinking with dis:
    xpos 0.85
    pause 1.5
    ease 0.2 xpos 1.5

show calem thinking with dis:
    xpos 0.75
    pause 1.5
    ease 0.2 xpos 1.5

$ renpy.pause(3.0, hard=True)

redmind @angrybrow frownmouth ".{w=0.5}.{w=0.5}.{w=0.5} Son unos hijos de puta."

show lance angry with dis:
    zoom 1.0 xpos 250/1920.0 ypos 1080
    ease 0.5 xpos 450/1920.0 zoom 1.25 ypos 1270
    pause 1.25
    ease 0.5 xpos 0.5 zoom 1.0 ypos 1080
    
show lavacookie:
    alpha 0.0 xpos 700 ypos 300 zoom 0.75 rotate 0
    pause 0.5
    parallel:
        ease 0.25 rotate 360
        ease 0.25 rotate 0
        repeat
    parallel:
        ease 0.3 xpos 600 ypos 100 zoom 0.5
        ease 0.5 xpos 550 ypos 700 zoom 0.1
    parallel:
        ease 0.15 alpha 1.0
    parallel:
        pause 0.55
        ease 0.25 alpha 0.0
            
narrator "{color=#e70000}Lance le arrebata las Galletas Lava a [pika_name].{/color}"

$ renpy.music.play("Audio/Pokemon/pikachu_confused2.ogg", channel="altcry", loop=None)
pikachu surprisedbrow frownmouth @surprised "Pika?!"

show lance -angry with dis:
    xpos 0.5 zoom 1.0
    
lance @talking2mouth "La comida chatarra solo sirve para pudrir su cuerpo y su mente.{w=0.5} Si tus Pokémon quieren bocadillos, dales Pokéhabas o bayas."

pause 1.0

$ renpy.music.set_volume(0.25, delay=0.5, channel="music")

redmind @thinking "... Tengo que decir algo, pero..."
redmind @sad "No puedo. Si al menos mis amigos se hubieran quedado aquí... pero, frente a toda la escuela, y con Lance siendo un Campeón Nacional..."
redmind @sad "No puedo."

$ renpy.music.set_volume(1.0, delay=2.0, channel="music")

red talking2mouth angryeyes angryeyebrows "Entendido.{w=0.5} Señor.{w=0.5} Me aseguraré de recordarlo."

show lance sadbrow with dis

$ renpy.music.play("Audio/Pokemon/pikachu_angry3.ogg", channel="altcry", loop=None)
pikachu angry_3b "¡Pi-pika...!"

lance @talking2mouth "Espera."

show lance -sadbrow with dis:
    xpos 0.5
    ease 0.6 xpos 0.6
    
red talking2mouth angryeyes angryeyebrows "¿Qué?"

lance @talking2mouth "Este Pikachu.{w=0.5} ¿Piensas incluirlo en tus evaluaciones de la academia?"

red @talkingmouth "Sí, por supuesto, es mi compañero.{w=0.5} Si hay alguien en quien confío, es{nw}"

show lance closedbrow with dis:
    xpos 0.6
    ease 0.6 xpos 0.5

lance @talking2mouth "Descártalo de inmediato."

red surprisedbrow talking2mouth @noshine "¿Qué dijiste?"

lance @talking2mouth "Tu Pikachu es inadecuado.{w=0.5} Usar un Pokémon tan débil no te llevará a ninguna parte en esta academia."
lance @talking2mouth "Si, por ejemplo, un estudiante intentara unirse al equipo de batalla con este Pokémon en su equipo..."
lance @angrybrow talking2mouth "Lo descalificaría de inmediato sin importar sus habilidades en combate."

$ renpy.music.play("Audio/Stadium_murmur.ogg", channel='crowd3', loop=True, fadein=1.0)

pause 1.5

lance -closedbrow @talking2mouth "Aunque se te permita tener seis Pokémon, tener siquiera uno como este sería una carga totalmente innecesaria y prescindible."
lance @talking2mouth "Su naturaleza es subóptima, su linaje claramente deficiente... podrías lanzar una piedra en el Bosque Verde y conseguir una mejor alternativa."

redmind @sad "¿Q-qué...? Vamos... Brendan, Ethan, Calem... Alguien, ayúdenos... ¿alguien?"

pause 2.0

redmind @surprised "Espera... escucho pasos corriendo. ¿Será--?{nw}"

show silver:
    xpos -0.5
    ease 0.2 xpos 0.25

show lance angry with dis:
    xpos 0.5
    ease 0.5 xpos 0.75

silver angry "¡No tienes ni la más puta idea de lo que estás diciendo, bastardo hijo de puta!"

red @surprised "¡¿S-Silver?!"

silver @talkingmouth "¿Crees que por ser un Campeón puedes decir qué Pokémon son buenos o malos? ¡¿Que puedes juzgar su valor de un solo vistazo?!"

silver @angrybrow talkingmouth "Bueno, soy de Johto, y déjame decirte que todo Johto sabe que te carrean esos tres Dragonite que llevas en la cintura. ¡Qué gran habilidad para armar equipos!"
silver @talkingmouth "¡¿Sabes cuál es tu problema?! No puedes sentirte realizado a menos que seas un Campeón Mundial. Y como fallaste en eso, buscas a alguien más a quien culpar como un mocoso."
silver @angrybrow talkingmouth "Entérate, fracasado. No es culpa de tus Pokémon. {i}Ningún{/i} Pokémon es un lastre. {i}Ningún{/i} Pokémon es inadecuado."
silver @sadbrow talkingmouth "La instructora Karen dice que solo los entrenadores egoístas llaman a los Pokémon 'fuertes' o 'débiles'. Pero tú no eres egoísta. Solo eres un cobarde que no puede admitir que su fracaso es {i}su{/i} culpa."
silver @talkingmouth "Conocí a otro tipo que no pudo aceptar su fracaso y tomó un viaje por las Cataratas Tohjo por el camino corto."

pause 2.0

redmind @surprised "S-Santo cielo. No importa lo que Lance me diga ahora... o lo que me haya dicho antes... {i}yo{/i} no voy a ser el que la gente recuerde aquí."

silver @talkingmouth "¡Y tú! ¡[first_name]!"

red @surprised "¡¿E-eh?!"

silver -angry @closedbrow talkingmouth "Deberías alzar la voz y defender a tus Pokémon."

red @talking2mouth "Eh... v-vale..."

pause 2.0

lance -angry @talking2mouth "Silver, ¿verdad?{w=1.0} Por favor, dime. ¿Cuál crees que es el castigo adecuado para esta flagrante muestra de falta de respeto?"

show silver -angry with dis

pause 2.0

silver @closedbrow talkingmouth "Expúlsame. No sería la primera vez que me pasa en la vida."

lance closedbrow @talking2mouth "Como empleado a medio tiempo de esta academia, no puedo hacer eso."

pause 1.0

lance @talking2mouth "Así que, en su lugar, escuchen esto atentamente." 
lance -closedbrow @talking2mouth "Independientemente de sus habilidades,{w=0.5} independientemente de los Pokémon que tengan en mano,{w=0.5} independientemente de que se lo {i}merezcan{/i}."
lance @angrybrow talking2mouth "Ustedes dos {i}nunca{/i} se unirán al equipo de batalla."

silver surprisedbrow @surprised "E-espera. [first_name][first_name] también? ¡Yo fui el que--{nw}"

lance @closedbrow talking2mouth "Ya lo he dicho{w=1.0} y así será."

red @angrybrow frownmouth "[ellipses]"

show silver sadbrow with dis

redmind angrybrow neutralmouth "Sé que debería callarme e irme, pero no puedo dejarlo pasar."
redmind "No me importa si este tipo es un bicampeón nacional o lo que sea. No voy a dejar que me pisotee a mí, a Silver y a [pika_name] cuando no sabe nada de nosotros."

red @talking2mouth "Con todo el respeto, señor, no hay forma de que eso vaya a suceder."

$ renpy.music.play("Audio/Stadium_crowd.ogg", channel='crowd', loop=True, fadein=1.0)

pause 1.5

show lance angrybrow
show silver -sadbrow 
with dis

pause 1.5

lance @talking2mouth "¿Y que te hace pensar eso?"

red @talking2mouth "[pika_name] y yo hemos sido mejores amigos desde que éramos niños.{w=0.5} Sé que no somos los más experimentados en cuanto a batallas y entrenamientos, pero no hacemos nada sin el otro."
red @talking2mouth "Para bien o para mal, vamos a llegar hasta el final juntos, y vamos a entrar en ese equipo de batalla. Vamos a ser tan buenos que no podrás ignorarnos."

red @closedbrow talking2mouth "El Instructor Bruno dijo que necesitábamos el voto del capitán del equipo de batalla, no dijo nada sobre tu voto."
red @angrybrow talking2mouth "Así que adelante, 'aconseja' al equipo que no nos acepten. A mí, a Silver, a [pika_name]. De todos modos, vamos a entrar porque somos amigos."

show lance sadbrow with dis

$ renpy.music.play("Audio/Pokemon/pikachu_excite3.ogg", channel="altcry", loop=None)
pikachu neutral_2b "¡Pika, pika!"

lance @closedbrow talking2mouth "... Ingenuo."
lance @angrybrow talking2mouth "El mundo no funciona así. {w=0.5} Di lo que quieras sobre tus Pokémon, la 'amistad' no te va a servir de nada, solo para perder tu tiempo."
lance @angrybrow talking2mouth "Consigue Pokémon más fuertes y aprende a reconocer las peleas que {i}no{/i} puedes ganar. En este mundo, solo los mejores de los mejores pueden sobrevivir,{w=0.5} mientras que los débiles y los tontos son eliminados."
    
red @thinking "[ellipses]"

lance @closedbrow talking2mouth "Yo que tú seguiría mi consejo. En cuanto a ti, Silver... aprende a contener la lengua, si no es probable que la pierdas."
lance @talking2mouth "Con permiso."

hide lance with dis

$ renpy.music.stop(channel='crowd3', fadeout=2.0)

$ renpy.pause(2.0, hard=True)

hide lance

stop music fadeout 2.5

red @sad "¿Silver...?"

silver @angry "Ni te molestes."

$ PlaySound("fading_footsteps.ogg")
hide silver at leftside with dis

pause 1.5

show brendan sadbrow frownmouth at rightside
show ethan sadbrow frownmouth at centerside 
show calem sadbrow at leftside 
with dis

ethan @sadbrow talking2mouth "H-hey... [first_name]. {w=0.5} ¿Estás bien?"
    
brendan @sadbrow talking2mouth "Eso se vio muy doloroso."

red @talking2mouth "... Estoy bien. Silver se llevó la mayor parte del golpe."

show brendan thinking 
show ethan thinking
with dis

redmind "Parece que no me creen.{w=0.5} Yo tampoco lo creo."

calem @talking2mouth "Nunca imaginé que ese era el tipo de persona que era Lance..."
ethan -thinking frownmouth @talking2mouth "Como dice el dicho, 'nunca conozcas a tus héroes'."
brendan -thinking frownmouth @angry "¡Es un tremendo imbécil!"

red @closedeyes talking2mouth "No es gran cosa, estoy contento de que no haya ido a más..."

redmind @thinking "Aún así, Lance tenía algo de razón.{w=0.5} Odio admitirlo, pero todos los demás en esta academia son mucho más fuertes que nosotros en casi todos los aspectos."
redmind @thinking "Pero él no sabe nada de mí ni de [pika_name].{w=0.5} Le mostraremos de lo que realmente somos capaces si estamos juntos."

brendan @talking2mouth "Pero en serio, realmente me sorprendió cuando ese chico de cabello rojo le dijo todo eso. {w=0.5} ¡Fue increíble!"

show ethan sadbrow frownmouth
show brendan sadbrow frownmouth 
show calem sadbrow frownmouth
with dis

red @angrybrow talking2mouth "Sí, bueno, alguien tenía que defender a [pika_name] y a mí."

brendan @talking2mouth "Oh, claro. Je,je,je...{w=0.5}{nw}"
extend @sad " Ya sabes, Lacen es alguien muy importante, y si hubiera dicho algo malo, podría haberte hecho quedar aún peor y..."

calem @sadbrow talking2mouth "Te pido mil disculpas, fallé en mi prioridad número uno como tu compañero de cuarto... como tu amigo."
ethan @sadbrow talking2mouth "Sí, yo también pensé que si me metía, él empezaría a gritarme... porque estoy un poco en la misma situación que tú..."

red @angrybrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}." 

show brendan -sadbrow -frownmouth
show calem -sadbrow -frownmouth
show ethan -sadbrow -frownmouth
with dis

red @closedeyes talking2mouth "Todavía sigo enojado, pero lo superaré. Vamos a tomar nuestros asientos."

may @talkingmouth "¡Hey, Brendan, [first_name]!"
    
$ renpy.music.queue("Audio/Music/Indigo_Loop.ogg", channel='music', loop=None, fadein=3.0, tight=None)
    
show may at midrightside with dis

show leaf at midleftside with dis

may @talkingmouth "¡Los estuvimos buscando por todas partes!"

leaf @talking2mouth "Sí, este lugar está tan lleno que llegar aquí fue como tratar de navegar por un laberinto."

window hide
pause 1.0

show leaf surprisedbrow frownmouth with dis

pause 1.0

show may surprisedbrow frownmouth 
show brendan surprisedbrow frownmouth
with dis

show leaf at getcloser, midleftside

leaf @talking2mouth "¿Quién es este pequeñin? {w=0.5} ¿Es uno de tus Pokémon de casa?"

show brendan happy
show may happy 
with dis

red happy "Sí, se llama [pika_name]."

show leaf -surprisedbrow -frownmouth -surprised 
show brendan -happy
show may -happy
with dis

may @talkingmouth "¡Aww! ¿Y [pika_name] se lleva bien con tu pequeño Shroomy, Brendan?"
brendan @happy "Bueno, eh, en realidad no se han conocido aún. No pensé que fuera buena idea dejarlo salir aquí."
may @closedbrow talking2mouth "Oh, eso sería lo más prudente..."

$ renpy.music.play("Audio/Pokemon/pikachu_norm1.ogg", channel="altcry", loop=None)

pikachu neutral_2 "¡Pikachu!"

show leaf at getfurther, midleftside

may @happybrow talkingmouth "¡Es tan lindo!"

show may at getcloser, midrightside

pause 0.5

show brendan surprisedbrow frownmouth with dis
    
narrator "May acaricia suavemente la cabeza de [pika_name]."

may @happybrow talkingmouth "¡Awww, su pelaje es tan suave!"
show may happy
show leaf happy
with dis

$ renpy.music.play("Audio/Pokemon/pikachu_happy1.ogg", channel="altcry", loop=None)

pikachu happy_2 "Chaaa~"

show may surprisedbrow frownmouth
show leaf surprisedbrow frownmouth
with dis

brendan surprisedbrow frownmouth @surprised "Hey, ¡¿por qué no le está dando una descarga a {i}ella{/i}?!"

leaf @surprisedbrow talking2mouth "¿Eh?"

may @talkingmouth "¿Y [pika_name] se esta llevando bien con tu [starter_species_name]?"

show brendan -surprisedbrow -frownmouth -surprised
show may -surprisedbrow -frownmouth -surprised
show leaf -surprisedbrow -frownmouth -surprised
with dis

red @talkingmouth "Por el momento, sí.{w=0.5} Creo que todavía no saben bien cómo sentirse el uno con el otro."
red @talking2mouth "[pika_name] ha sido mi único Pokémon desde que lo conseguí, así que supongo que no está acostumbrado a que le dé atención a otro."

show may at getfurther, midrightside
    
may @talkingmouth "Eso es comprensible.{w=0.5} Estoy segura de que una vez que pasen más tiempo juntos se llevarán genial."
    
leaf @talking2mouth "¿Cuánto tiempo han estado tú y [pika_name] juntos?"
    
red @closedbrow talking2mouth "Desde que tenía 10 años.{w=0.5} Sam nos dio un Pokémon a [blue_name] y a mí como regalo."

may @surprised "¿'[blue_name]'? ¿Ese raro que tiene cabello puntiagudo y esta que esta nuestra clase?"

red @talkingmouth "Sí, ese mismo. De todos modos, hemos sido los mejores amigos desde entonces.{w=0.5} [pika_name], no [blue_name].{w=0.5} [pika_name] y yo hacemos todo juntos."
red @happy "... ¡Incluso si él intenta evitar que salgamos a correr juntos!"

leaf @talking2mouth "Entonces, ¿por qué no lo has evolucionado aún?"

$ renpy.music.play("Audio/Pokemon/pikachu_confused.ogg", channel="altcry", loop=None)

pikachu neutral_4 "¿Pika?"

red @closedeyes talking2mouth "Bueno... es un poco embarazoso, pero los Raichu comen mucho más que los Pikachu, y en casa, realmente no podíamos permitirnos eso."
leaf @surprised "¿De verdad? Bueno, si estás en Kobukan, deberías poder permitirte eso ahora, ¿no?"
redmind @thinking "Eh... no tanto. Digo, puedo alimentarlo lo suficientemente bien con la comida gratis que Kobukan proporciona, pero no sé cuánto tiempo pasará antes de que la escuela se dé cuenta de que no puedo pagar..."
redmind @happy "¿Y qué haría yo con un Raichu entonces? ¡Tendría que regalarlo! ¡Ni de broma!"
redmind @thinking "[ellipses]"
redmind @thinking "Aunque... ¿qué haré con [starter_name] cuando me expulsen?"

may @happy "¡Apuesto a que serías una excelente adición al club de coordinadores!{w=0.5} Los Pikachu son muy populares en los concursos Pokémon."

$ renpy.music.play("Audio/Pokemon/pikachu_pikapika1.ogg", channel="altcry", loop=None)

pikachu happy_2 "¡Pika, pika~!"
    
may @happybrow talkingmouth "¿Ves? Hasta [pika_name] cree que sería genial."

leaf @happybrow talkingmouth "Bueno, está bien siempre y cuando no lo uses para batallar.{w=0.5} Los Pikachu son {i}mucho{/i} más lindos que los Raichu, de todos modos."
    
leaf @talkingmouth "Hablando de batallar, ¿están emocionados por ver a Janine?"

red @talkingmouth "¿Quién es Janine?"

leaf @surprisedbrow talking2mouth "¿No lo sabes?{w=0.5} ¡Ella es la capitana del equipo de batalla durante dos años consecutivos! Todos piensan que será la próxima Campeona de Kobukan."

brendan @surprised "¿Espera? ¿Capitana del equipo de batalla durante dos años seguidos? ¿Cómo funciona eso? Esta academia tiene un programa de solo un año."

calem @talkingmouth "Al igual que en el Consejo de Estudiantil, los alumnos pueden elegir quedarse para formar a los nuevos y tal parece ser que ella decidió hacerlo durante dos años seguidos."

ethan @talkingmouth "Escuché que Janine no se irá hasta encontrar a alguien mejor que ella para ser capitán del equipo de batalla."

red @surprised "¿Cómo puede permitírselo?"

may @surprised "{i}Escuché{/i} que es hija de uno de los profesores de la academia."

red @closedbrow talking2mouth "Oh, sí, creo que [blue_name] mencionó que es hija de un miembro del Alto Mando..."

calem @closedbrow talkingmouth "Parece que hay muy poco que Janine {i}no{/i} tenga a su favor."

leaf @closedbrow talkingmouth "Ella es una chica muy dura. {i}Escuché{/i} que tiene poderes magicos de ninja."

red @confused "Espera...  ¿ninja? Ahora que lo pienso, {i}vi{/i} a una mujer que vestia de una forma muy rara y..."

$ renpy.music.play("Audio/Stadium_chant.ogg", channel='crowd2', loop=True, fadein=0.5)

pause 1.5

show leaf surprisedbrow frownmouth
show may surprisedbrow frownmouth
show brendan surprisedbrow frownmouth
show calem surprisedbrow frownmouth
show ethan surprisedbrow frownmouth
with dis

brendan @talking2mouth "¡Hey, creo que ya están comenzando!"

hide leaf surprised at midleftside with dis
hide may surprised at midrightside with dis
hide brendan surprised at rightside with dis
hide calem surprised at leftside with dis
hide ethan surprised at centerside with dis

$ renpy.music.stop(channel='crowd2', fadeout=1.0)
$ renpy.pause(0.5, hard=True)

$ PlaySound("crowd_cheer.ogg")

$ renpy.pause(0.5, hard=True)

show janine uniform:
    alpha 0.0 xpos 300
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        ease 1.0 xpos 720
        
$ renpy.pause(1.0, hard=True)

$ BecomeNamed("Janine")
redmind neutralbrow neutralmouth "Esa debe ser Janine, y, como pensaba, es la mujer que echó a Blue del Salón Batalla."
redmind @angrybrow frownmouth "Y, más importante aún, es la mujer a la que tengo que convencer para que me deje entrar al equipo de batalla."

show janine thinking:
    alpha 1.0 xpos 720
    pause 0.5
    ease 1.0 alpha 0.0 xpos 670

show stadium_full:
    parallel:
        xalign 0.0
        ease 0.02 xpos -15
        ease 0.02 xpos 15
        ease 0.02 xpos 0
        repeat 6
    parallel:
        yalign 0.0
        ease 0.02 ypos -15
        ease 0.02 ypos 15
        ease 0.02 ypos 0
        repeat 6

Character("Announcer") "\"¡Bienvenidos, damas y caballeros, chicos y chicas, a este combate de exhibición especial organizado por el equipo de batalla de la Academia Kobukan! ¿Cómo se sienten esta noche?\""

show janine -thinking:
    alpha 0.0 xpos 670

$ PlaySound("crowd_cheer.ogg")

show stadium_full:
    pause 0.75
    parallel:
        xalign 0.0
        ease 0.02 xpos -15
        ease 0.02 xpos 15
        ease 0.02 xpos 0
        repeat 25
    parallel:
        yalign 0.0
        ease 0.02 ypos -15
        ease 0.02 ypos 15
        ease 0.02 ypos 0
        repeat 25

pause 1.5

$ renpy.music.play("Audio/Stadium_chant.ogg", channel='crowd2', loop=True, fadein=3.0)

show stadium_full:
    xalign 0.5 yalign 1.0

Character("Announcer") "\"¡Genial! ¡Entonces, vamos directo al combate!\""
Character("Announcer") "\"Vaya, pero qué espectáculo tenemos preparado para ustedes!{w=0.5} La primera en entrar al campo de batalla es nada menos que nuestra capitana del equipo de batalla, ¡Janine!\""

$ PlaySound("crowd_cheer.ogg")

show janine:
    alpha 0.0 xpos 500
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        ease 0.75 xpos 300

pause 1.0

$ renpy.music.play("Audio/Pokemon/Venomoth_Ball.ogg", channel="altcry", loop=None)

show venomoth at pokeball behind beam3:
    xanchor -1.0 alpha 0.0 xzoom 0.0 yzoom 0.0 yalign 1.0 ypos 1380 xpos 500
    block:
        parallel:
            ease 0.33 alpha 1.0 ypos 600 xpos 650
            ease 0.67 ypos 1080 xpos 700
        parallel:
            ease 0.5 xzoom -1 yzoom 1.0

$ renpy.pause(1.0, hard=True)

show venomoth:
    subpixel True
    alpha 1.0 ypos 1080 xpos 700
    block:
        parallel:
            ease 1.1 ypos 820
            ease 1.0 ypos 960
            ease 1.1 ypos 850
            ease 1.0 ypos 1000
            ease 1.1 ypos 825
            ease 1.0 ypos 980
            repeat
        parallel:
            ease 0.52 xpos 630
            ease 0.6 xpos 730
            ease 0.62 xpos 620
            ease 0.7 xpos 725
            ease 0.58 xpos 600
            ease 0.65 xpos 700
            repeat

show janine:
    alpha 1.0 xpos 300

Character("Announcer") "\"¡Janine comienza fuerte con su Pokémon insignia, Venomoth!{w=0.5} ¡Estos dos han dominado las clasificaciones de Kobukan desde su llegada y no muestran señales de detenerse!"

pause 0.25

show janine thinking:
    alpha 1.0 xpos 300
    parallel:
        ease 0.75 alpha 0.0
    parallel:
        ease 1.0 xpos 100

show venomoth:
    subpixel True
    parallel:
        ease 2.0 xpos 0
    parallel:
        ease 0.5 ypos 1000
        ease 0.5 ypos 840
        ease 0.5 ypos 900
        ease 0.5 ypos 800

$ renpy.pause(2.0, hard=True)

show venomoth:
    subpixel True
    xpos 0 ypos 800 xzoom -1 yzoom 1.0
    block:
        parallel:
            ease 1.1 ypos 620
            ease 1.0 ypos 760
            ease 1.1 ypos 650
            ease 1.0 ypos 800
            ease 1.1 ypos 625
            ease 1.0 ypos 780
            repeat
        parallel:
            ease 0.52 xpos 80
            ease 0.6 xpos 30
            ease 0.62 xpos 120
            ease 0.7 xpos 25
            ease 0.58 xpos 100
            ease 0.65 xpos 0
            repeat
        parallel:
            ease 1.0 xzoom -0.5 yzoom 0.5


$renpy.music.play("audio/pokemon/ball sound.ogg", channel="altcry", loop=None)
$ renpy.music.queue("audio/pokemon/cries/419.mp3", channel="altcry", loop=None)

show floatzel at pokeball behind beam3:
    alpha 0.0 zoom 0.0 yalign 1.0 ypos 1000 xpos 1900
    block:
        parallel:
            ease 0.33 alpha 1.0 ypos 200 xpos 1500
            ease 0.67 ypos 850 xpos 1400
        parallel:
            ease 0.5 zoom 0.5

$ renpy.pause(1.0, hard=True)

show floatzel:
    alpha 1.0 zoom 0.5 xpos 1400 ypos 850
    parallel:
        ease 0.3 ypos 820
        ease 0.15 ypos 850
        repeat
    parallel:
        ease 0.3 xpos 1370
        ease 0.15 xpos 1340
        ease 0.3 xpos 1370
        ease 0.15 xpos 1400
        repeat

show venomoth:
    subpixel True
    xanchor -1.0 ypos 620 xpos 30
    block:
        parallel:
            ease 1.0 xanchor -1.5
        parallel:
            ease 1.1 ypos 620
            ease 1.0 ypos 760
            ease 1.1 ypos 650
            ease 1.0 ypos 800
            ease 1.1 ypos 625
            ease 1.0 ypos 780
            repeat
        parallel:
            ease 0.52 xpos 80
            ease 0.6 xpos 30
            ease 0.62 xpos 120
            ease 0.7 xpos 25
            ease 0.58 xpos 100
            ease 0.65 xpos 0
            repeat

Character("Announcer") "\"Del otro lado, su oponente envía a un Floatzel, ¡un Pokémon conocido por su agilidad en el campo de batalla!{w=0.5} ¿Podrá este dúo estar a la altura del desafío?"

hide janine

janine uniform @talking2mouth "Va a necesitar mucho más que solo velocidad para igualar a mi Venomoth."

$ renpy.music.play("Audio/Pokemon/Venomoth.ogg", channel="altcry", loop=None)

show venomoth:
    subpixel True
    parallel:
        block:
            parallel:
                ease 1.0 ypos 450
            parallel:
                ease 0.05 xpos 20
                ease 0.05 xpos 40
                repeat 10
    parallel:
        pause 1.0
        block:
            parallel:
                ease 1.1 ypos 620
                ease 1.0 ypos 760
                ease 1.1 ypos 650
                ease 1.0 ypos 800
                ease 1.1 ypos 625
                ease 1.0 ypos 780
                repeat
            parallel:
                ease 0.52 xpos 80
                ease 0.6 xpos 30
                ease 0.62 xpos 120
                ease 0.7 xpos 25
                ease 0.58 xpos 100
                ease 0.65 xpos 0
                repeat

Character("Venomoth") "\"¡Vennn!\""

stop music fadeout 3.0

Character("Announcer") "\"Y ahora el momento que todos han estado esperando!{w=0.5} ¡La primera ronda de la exhibición anual del equipo de batalla de la Academia Kobukan!\""

$ renpy.music.queue("Audio/Music/KantoGym_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/KantoGym_Loop.ogg", channel='music', loop=True, tight=None)

$ renpy.music.stop(channel='crowd2', fadeout=2.0)

$ PlaySound("crowd_cheer.ogg")

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_32

show blank with transball

$ renpy.pause(2.0, hard=True)

show exhibition01 behind blank:
    zoom 1.1
show exhibit01veno behind blank:
    zoom 1.1
show exhibit01float behind blank:
    zoom 1.1

$ renpy.pause(0.5, hard=True)

show blank:
    alpha 1.0
    ease 1.0 alpha 0.0

show exhibition01:
    subpixel True
    zoom 1.1
    ease 5.0 zoom 1.0
show exhibit01veno:
    subpixel True
    zoom 1.1
    ease 5.0 zoom 1.0
show exhibit01float behind exhibit01veno:
    subpixel True
    zoom 1.1
    ease 5.0 zoom 1.0
show exhibit01aqua behind exhibit01veno:
    subpixel True
    zoom 1.1 alpha 0.0
    parallel:
        ease 5.0 zoom 1.0
    parallel:
        ease 2.0 alpha 1.0
show exhibit01aquaglow:
    subpixel True
    zoom 1.1 alpha 0.0
    parallel:
        ease 5.0 zoom 1.0
    parallel:
        ease 2.0 alpha 1.0
    
Character("Announcer") "\"¡Y comienza el combate!{w=0.5} ¡Floatzel se lanza de inmediato con Aqua Jet!\""

hide floatzel
hide venomoth
hide leaf
hide brendan
hide may
hide calem
hide ethan
hide leaf
hide janine

$ PlaySound("Pokemon/Moves/AquaJet.ogg")
$ renpy.pause(1.9, hard=True)

show exhibition01
show exhibit01veno
show exhibit01float
show exhibit01aqua
show exhibit01aquaglow
with vpunch

Character("Announcer") "\"... ¡Bueno, eso no pareció servir de mucho!\""

show exhibit01aqua:
    alpha 1.0
    ease 1.0 alpha 0.0
show exhibit01aquaglow:
    alpha 1.0
    ease 1.0 alpha 0.0

leaf @talking2mouth "Sabes, con la velocidad de Floatzel, probablemente pueda atacar primero, incluso sin el impulso de Aqua Jet."

hide exhibit01aqua
hide exhibit01aquaglow

leaf @surprised "Uno pensaría que el tipo intentaría otro movimiento para empezar."


$ PlaySound("Pokemon/Moves/StunSpore.ogg")

show exhibit01spore behind exhibit01veno with dis:
    alpha 1.0
    pause 4.0
    ease 1.0 alpha 0.0

show stunspore:
    subpixel True
    alpha 0.0 zoom 1.5 yalign 0.5 xpos -500
    parallel:
        ease 1.0 alpha 1.0
        pause 3.0
        ease 1.0 alpha 0.0
    parallel:
        ease 6.0 xpos 0

Character("Announcer") "\"¡¿Qué es esto?!{w=0.5} ¡La arena se está llenando con las esporas paralizadoras de Venomoth! ¡Los espectadores cercanos al ring, por favor eviten inhalar demasiado!\""

$ PlaySound("Pokemon/Moves/Paralyzed.ogg")

show exhibition01:
    parallel:
        xalign 0.0
        ease 0.02 xpos -10
        ease 0.02 xpos 10
        ease 0.02 xpos 0
        repeat 8
    parallel:
        yalign 0.0
        ease 0.02 ypos -10
        ease 0.02 ypos 10
        ease 0.02 ypos 0
        repeat 8
show exhibit01veno:
    parallel:
        xalign 0.0
        ease 0.02 xpos -10
        ease 0.02 xpos 10
        ease 0.02 xpos 0
        repeat 8
    parallel:
        yalign 0.0
        ease 0.02 ypos -10
        ease 0.02 ypos 10
        ease 0.02 ypos 0
        repeat 8
show exhibit01para behind exhibit01veno:
    parallel:
        xalign 0.0
        ease 0.02 xpos -10
        ease 0.02 xpos 10
        ease 0.02 xpos 0
        repeat 8
    parallel:
        yalign 0.0
        ease 0.02 ypos -10
        ease 0.02 ypos 10
        ease 0.02 ypos 0
        repeat 8
hide exhibit01float

Character("Announcer") "\"Oh no, ¡parece que Floatzel está paralizado!{w=0.5} ¡Las cosas definitivamente no pintan bien para nuestro retador!\""

show exhibit01spore:
    ease 0.5 alpha 0.0
show stunspore:
    ease 0.5 alpha 0.0

calem @talkingmouth "Fue una buena estrategia reducir la velocidad de Floatzel, y su oponente reaccionó muy mal ante eso."
calem @closedbrow talking2mouth "Ahora Venomoth puede eliminar a Floatzel a su propio ritmo."
ethan @closedbrow talking2mouth "Ese Floatzel... ¿es tipo agua, verdad? Creo que he visto Venomoths que pueden usar Energibola."
    
hide exhibit01spore
hide stunspore
    
show energyball:
    alpha 0.0 zoom 1.5 xalign 0.8 yalign 0.5
    parallel:
        ease 2.0 xalign 0.5 yalign 1.0 zoom 1.0
    parallel:
        ease 1.0 alpha 0.9
        pause 0.75
        ease 0.5 alpha 0.0

$ renpy.music.play("Audio/crowd_cheer.ogg", channel='crowd3', loop=None, fadein=0.0)
$ PlaySound("Pokemon/Moves/EnergyBall.ogg")
$ renpy.pause(1.9, hard=True)

$ renpy.music.play("Audio/Stadium_chant.ogg", channel='crowd2', loop=True, fadein=1.0)

$ renpy.music.play("Audio/pokemon/cries/419.mp3", channel="altcry", loop=None)
show exhibition01
show exhibit01veno
show exhibit01para
show energyball
with vpunch

show exhibit01para:
    alpha 1.0
    ease 0.5 alpha 0.0

Character("Announcer") "\"¡Espectacular! ¡Con un Energibola sorpresa, Floatzel está fuera de combate de un solo golpe!{w=0.5} ¿Cómo responderá el oponente de Janine ante este despliegue de poder?\""   

hide exhibit01para
hide energyball

show exhibition02 behind exhibition01:
    zoom 1.1
show exhibit02veno behind exhibition01:
    zoom 1.1
show exhibit02clay behind exhibition01:
    zoom 1.1

brendan @surprised "Bueno, ahí lo tienen."
brendan @happybrow talkingmouth "Je, ¿para qué molestarse con tantas tácticas cuando puedes simplemente dar un golpe demoledor, eh?"
may @surprised "¡No sabía que Venomoth podía aprender ese movimiento! Los tipo Bicho sí que son versátiles, ¿no?"
red @talkingmouth "No creo que pueda aprenderlo por sí mismo, pero puedes enseñárselo."
leaf @talking2mouth "Fue inteligente de su parte no revelarlo tan pronto.{w=0.5} El entrenador de Floatzel fue completamente tomado por sorpresa."
leaf @talkingmouth "Pero... ¿por qué molestarse en usar Paralizador?"
calem @closedbrow talking2mouth "Quizás no estaba segura de poder hacer un KO directo. Si no conoces la fuerza de tu oponente, es una buena estrategia reducir su potencial antes de atacar."
    
$ renpy.music.stop(channel='crowd2', fadeout=3.0)

$renpy.music.play("audio/pokemon/ball sound.ogg", channel="altcry", loop=None)
$ renpy.music.queue("audio/pokemon/cries/344.mp3", channel="altcry", loop=None)
$ renpy.pause(0.6, hard=True)

show exhibition01:
    alpha 1.0
    ease 1.0 alpha 0.0
show exhibit01veno:
    alpha 1.0
    ease 1.0 alpha 0.0

show exhibition02:
    subpixel True
    zoom 1.1
    ease 5.0 zoom 1.0
show exhibit02veno:
    subpixel True
    zoom 1.1
    ease 5.0 zoom 1.0
show exhibit02clay:
    subpixel True
    zoom 1.1
    ease 5.0 zoom 1.0

Character("Claydol") "\"Clay.{w=0.33} Dol.\""

Character("Announcer") "\"Y el siguiente Pokémon en salir al campo es Claydol, un Pokémon de tipo Tierra y Psíquico!{w=0.5} ¿Qué estará planeando el retador con un Pokémon tan peculiar?\""

hide exhibition01
hide exhibit01veno

red @talking2mouth "Hmm. Claydol, nativo de Hoenn. En el mejor de los casos, tiene muy buenas defensas. Su única habilidad es Levitar, pero probablemente no importará aquí..."
    
leaf @talking2mouth "Si tuviera que apostar, iria all-in por Venomoth.{w=0.5}{nw}"
extend leaf @closedbrow talking2mouth " Claydol tiene la ventaja defensiva por naturaleza, pero ese Venomoth podría tener otro as bajo la manga."

may surprisedbrow frownmouth @surprised "¿De verdad crees que Venomoth es tan fuerte?"

leaf happy "Oye, estamos hablando de {i}Janine{/i}.{w=0.5} Nunca se sabe."

calem @closedbrow talking2mouth "Mucha gente destaca a Claydol como un excelente tanque, pero también cuenta con un arsenal ofensivo respetable.{w=0.5} No olviden sus movimientos Psíquicos súper efectivos contra Venomoth."

brendan @talking2mouth "Nah, sigo apostando por Venomoth."

ethan @happy "Sí, ¿viste cómo eliminó a Floatzel? Además, si cuentas los ataques Psíquicos de Claydol, ¡no olvides los ataques Bicho de Venomoth!"

calem @closedbrow happymouth "Por supuesto, solo estoy jugando al abogado del diablo."
    
redmind @thinking "Parece que nadie sabe quién tiene la ventaja clara, ambos tienen ventaja de tipo ofensivo sobre el otro, pero..."
redmind @thinking "Teniendo en cuenta todos los factores de ambos Pokémon en el enfrentamiento contra Venomoth... debería estar cincuenta y cincuenta."
redmind @angrybrow frownmouth "Pero no lo está, ni siquiera esta cerca."

$ renpy.music.play("Audio/crowd_cheer.ogg", channel='crowd3', loop=False, fadein=0.0)
    
Character("Announcer") "\"¡Y comienza la segunda ronda!{w=0.5} ¡Veamos qué tiene preparado el Claydol de nuestro retador contra el Venomoth de Janine!\""

show exhibit02dance1 orb1 with dis:
    alpha 1.0
show exhibit02dance1 orb1 with dis:
    alpha 1.0

$ PlaySound("Pokemon/Moves/QuiverDance_Base.ogg")
$ renpy.pause(2.0, hard=True)
$ PlaySound("Pokemon/Moves/QuiverDance_Boost.ogg")

Character("Announcer") "\"¡Oh! ¡Parece que Venomoth abre la ronda con dos Danzas Aleteo consecutivas!{w=0.5} ¡Está aumentando su fuerza rápidamente! ¿Cómo responderá nuestro retador?\""

show exhibit02dance1 base:
    alpha 1.0
show exhibit02dance2 floor1:
    alpha 1.0

$ renpy.music.play("Audio/crowd_cheer.ogg", channel='crowd3', loop=False, fadein=0.0)
$ PlaySound("Pokemon/Moves/Psybeam.ogg")

show exhibition02:
    parallel:
        xalign 0.0
        ease 0.033 xpos -12
        ease 0.033 xpos 12
        ease 0.033 xpos 0
        repeat 20
    parallel:
        yalign 0.0
        ease 0.033 ypos -5
        ease 0.033 ypos 5
        ease 0.033 ypos 0
        repeat 20
show exhibit02veno:
    parallel:
        xalign 0.0
        ease 0.033 xpos -12
        ease 0.033 xpos 12
        ease 0.033 xpos 0
        repeat 20
    parallel:
        yalign 0.0
        ease 0.033 ypos -5
        ease 0.033 ypos 5
        ease 0.033 ypos 0
        repeat 20
show exhibit02dance1 base:
    parallel:
        xalign 0.0
        ease 0.033 xpos -12
        ease 0.033 xpos 12
        ease 0.033 xpos 0
        repeat 20
    parallel:
        yalign 0.0
        ease 0.033 ypos -5
        ease 0.033 ypos 5
        ease 0.033 ypos 0
        repeat 20
show exhibit02dance2 floor1:
    parallel:
        xalign 0.0
        ease 0.033 xpos -12
        ease 0.033 xpos 12
        ease 0.033 xpos 0
        repeat 20
    parallel:
        yalign 0.0
        ease 0.033 ypos -5
        ease 0.033 ypos 5
        ease 0.033 ypos 0
        repeat 20
show exhibit02clay:
    parallel:
        xalign 0.0
        ease 0.033 xpos -12
        ease 0.033 xpos 12
        ease 0.033 xpos 0
        repeat 20
    parallel:
        yalign 0.0
        ease 0.033 ypos -5
        ease 0.033 ypos 5
        ease 0.033 ypos 0
        repeat 20
show exhibit02psy behind exhibit02clay:
    alpha 0.0
    parallel:
        ease 0.25 alpha 1.0
        pause 3.0
        ease 0.75 alpha 0.0
    parallel:
        xalign 0.0
        ease 0.033 xpos -12
        ease 0.033 xpos 12
        ease 0.033 xpos 0
        repeat 20
    parallel:
        yalign 0.0
        ease 0.033 ypos -5
        ease 0.033 ypos 5
        ease 0.033 ypos 0
        repeat 20
        
show psybeam behind exhibit02psy:
    alpha 0.0
    parallel:
        ease 0.25 alpha 1.0
        pause 1.5
        ease 0.25 alpha 0.0
    parallel:
        parallel:
            xalign 0.4
            ease 0.033 xpos -30
            ease 0.033 xpos 30
            ease 0.034 xpos 0
            repeat 20
        parallel:
            pause 1.9
            ease 0.1 xalign 1.0
    parallel:
        parallel:
            yalign 0.33
            ease 0.033 ypos -10
            ease 0.033 ypos 10
            ease 0.034 ypos 0
            repeat 20
        parallel:
            pause 1.9
            ease 0.1 yalign 0.5
        

$ renpy.pause(2.0, hard=True)

Character("Announcer") "\"¡Y Claydol ataca con un potente Psicorrayo!{w=0.5} ¡Señoras y señores, creo que eso es todo para Venomoth!"

$ renpy.music.play("Audio/Pokemon/Venomoth.ogg", channel="altcry", loop=None)
$ renpy.music.play("Audio/crowd_cheer.ogg", channel='crowd3', loop=False, fadein=0.0)

Character("Venomoth") "\"¡Vennt!\""

Character("Announcer") "\"Esperen un segundo, ¡¿qué es esto?!{w=0.33} ¡No lo puedo creer! ¡Venomoth lo ha soportado completamente!{w=0.5} ¡Apenas tiene un rasguño gracias a Danza Aleteo!\""

hide venomoth
hide psybeam

show exhibit02dance1 orb2
show exhibit02dance2 floor2
with dis

$ PlaySound("Pokemon/Moves/QuiverDance_Boost.ogg")

Character("Announcer") "\"¡Y Venomoth sigue potenciándose con su {i}tercera{/i} Danza Aleteo!{w=0.5} ¡Si nuestro retador no tiene una respuesta, Venomoth será imparable!\""

$ PlaySound("Pokemon/Moves/CosmicPower_Boost.ogg")

show exhibit02psy with dis:
    alpha 1.0

Character("Announcer") "\"Parece que Claydol responde usando Masa Cósmica para reforzar su defensa, ¡pero podría ser demasiado tarde!{w=0.5} ¿Podría ser el fin para Claydol?\""

show exhibition02:
    parallel:
        xalign 0.0
        ease 0.033 xpos -12
        ease 0.033 xpos 12
        ease 0.033 xpos 0
        repeat 10
    parallel:
        yalign 0.0
        ease 0.033 ypos -5
        ease 0.033 ypos 5
        ease 0.033 ypos 0
        repeat 10
show exhibit02veno:
    parallel:
        xalign 0.0
        ease 0.033 xpos -12
        ease 0.033 xpos 12
        ease 0.033 xpos 0
        repeat 10
    parallel:
        yalign 0.0
        ease 0.033 ypos -5
        ease 0.033 ypos 5
        ease 0.033 ypos 0
        repeat 10
show exhibit02clay:
    parallel:
        xalign 0.0
        ease 0.033 xpos -12
        ease 0.033 xpos 12
        ease 0.033 xpos 0
        repeat 10
    parallel:
        yalign 0.0
        ease 0.033 ypos -5
        ease 0.033 ypos 5
        ease 0.033 ypos 0
        repeat 10
show exhibit02dance1 orb2:
    parallel:
        xalign 0.0
        ease 0.033 xpos -12
        ease 0.033 xpos 12
        ease 0.033 xpos 0
        repeat 10
    parallel:
        yalign 0.0
        ease 0.033 ypos -5
        ease 0.033 ypos 5
        ease 0.033 ypos 0
        repeat 10
show exhibit02dance2 floor2:
    parallel:
        xalign 0.0
        ease 0.033 xpos -12
        ease 0.033 xpos 12
        ease 0.033 xpos 0
        repeat 10
    parallel:
        yalign 0.0
        ease 0.033 ypos -5
        ease 0.033 ypos 5
        ease 0.033 ypos 0
        repeat 10
        
show greenorb1 as orb1:
    alpha 1.0 xpos 1750 ypos 900 zoom 0.0
    block:
        ease 0.12 zoom 1.0 xpos 700 ypos 700
        ease 0.1 xpos 550 ypos 250
        ease 0.15 zoom 0.0
    repeat 4
show greenorb1 as orb2:
    alpha 1.0 xpos 1750 ypos 900 zoom 0.0
    block:
        ease 0.14 zoom 1.2 xpos 800 ypos 200
        ease 0.14 xpos 550 ypos 250
        ease 0.12 zoom 0.0
    repeat 5
show greenorb2 as orb3:
    alpha 1.0 xpos 1750 ypos 900 zoom 0.0
    block:
        ease 0.09 zoom 0.9 xpos 600 ypos 500
        ease 0.13 xpos 550 ypos 250
        ease 0.12 zoom 0.0
    repeat 4
show greenorb2 as orb4:
    alpha 1.0 xpos 1750 ypos 900 zoom 0.0
    block:
        ease 0.13 zoom 1.25 xpos 740 ypos 50
        ease 0.14 xpos 550 ypos 250
        ease 0.11 zoom 0.0
    repeat 5
show greenorb3 as orb5:
    alpha 1.0 xpos 1750 ypos 900 zoom 0.0
    block:
        ease 0.12 zoom 1.25 xpos 650 ypos 300
        ease 0.1 xpos 550 ypos 250
        ease 0.14 zoom 0.0
    repeat 3
show greenorb3 as orb6:
    alpha 1.0 xpos 1750 ypos 900 zoom 0.0
    block:
        ease 0.15 zoom 1.0 xpos 700 ypos 100
        ease 0.1 xpos 550 ypos 250
        ease 0.11 zoom 0.0
    repeat 5

$ renpy.music.play("Audio/crowd_cheer.ogg", channel='crowd3', loop=False, fadein=0.0)
$ PlaySound("Pokemon/Moves/GigaDrain.ogg")
$ renpy.pause(1.5, hard=True)
$ renpy.music.play("Audio/pokemon/cries/344.mp3", channel="altcry", loop=None)
$ renpy.pause(0.25, hard=True)
$ renpy.music.play("Audio/Stadium_chant.ogg", channel='crowd2', loop=True, fadein=0.5)

show exhibit02dance1 base:
    alpha 1.0
    ease 0.5 alpha 0.0
show exhibit02dance2 floor1:
    alpha 1.0
    ease 0.5 alpha 0.0
show exhibit02psy:
    alpha 1.0
    ease 0.5 alpha 0.0
show exhibit02clay:
    alpha 1.0
    ease 0.75 alpha 0.0

show venomoth behind beam3:
    subpixel True
    xanchor -1.5 xzoom -0.5 yzoom 0.5 yalign 1.0 ypos 620 xpos 30 alpha 1.0
    block:
        parallel:
            ease 1.1 ypos 620
            ease 1.0 ypos 760
            ease 1.1 ypos 650
            ease 1.0 ypos 800
            ease 1.1 ypos 625
            ease 1.0 ypos 780
            repeat
        parallel:
            ease 0.52 xpos 80
            ease 0.6 xpos 30
            ease 0.62 xpos 120
            ease 0.7 xpos 25
            ease 0.58 xpos 100
            ease 0.65 xpos 0
            repeat

Character("Announcer") "\"¡Ouch!{w=0.3} ¡Ahí está! ¡Un golpe directo con Gigadrenado!{w=0.5} ¡Claydol está fuera de combate! ¡Janine y Venomoth se llevan la segunda ronda sin problemas!\""
Character("Announcer") "\"¡Al retador le queda su último Pokémon!{w=0.5} ¿Será este Pokémon la clave para dar una remontada sorpresiva o se tratará de una nueva victoria de Janine?\""

hide greenorb1 as orb1
hide greenorb1 as orb2
hide greenorb2 as orb3
hide greenorb2 as orb4
hide greenorb3 as orb5
hide greenorb3 as orb6    
hide exhibit02dance1
hide exhibit02dance2
hide exhibit02clay
hide exhibit02psy

show exhibition02:
    alpha 1.0
    ease 1.5 alpha 0.0
show exhibit02veno:
    alpha 1.0
    ease 1.5 alpha 0.0

leaf @happy "¡Brutal! ¡Esto es lo que me gusta ver de la capitana del equipo de batalla de la Academia Kobukan!"
calem @closedbrow talking2mouth "Espléndido, no cometió ningún error. Es como ver a un pintor experto en acción..."
ethan @closedbrow talking2mouth "Sí, pero ¿por qué tenía Gigadrenado {i}y{/i} Energibola? No sé si esa fue la mejor jugada."
may @happy "Bueno, en cualquier caso, ¡le salió bien!"

hide exhibition02
hide exhibit02veno

redmind @thinking "Esa ronda terminó en un abrir y cerrar de ojos, aunque, en teoría, Claydol debería haber durado mucho más que Floatzel."
redmind @thinking "¿Puede ser tan grande la diferencia entre dos Pokémon?"
redmind @thinking "¿Esto es lo que Lance intentaba decirme?"

$ renpy.music.stop(channel='crowd2', fadeout=4.0)

Character("Announcer") "\"¡Y ahora pasamos a la tercera ronda!{w=0.5} ¿Habrá encontrado el retador una forma de lidiar con el Venomoth de Janine?\""

$ renpy.music.play("Audio/Pokemon/Victreebel_Ball.ogg", channel="altcry", loop=None)

show victreebel at pokeball behind beam3:
    alpha 0.0 zoom 0.0 yalign 1.0 ypos 600 xpos 1800
    block:
        parallel:
            ease 0.33 alpha 1.0 ypos 300 xpos 1500
            ease 0.67 ypos 850 xpos 1300
        parallel:
            ease 0.5 zoom 0.5

$ renpy.pause(1.0, hard=True)

show victreebel:
    alpha 1.0 zoom 0.5 xpos 1300 ypos 850
    parallel:
        ease 0.4 ypos 845
        ease 0.2 ypos 850
        repeat
    parallel:
        ease 0.6 xpos 1280
        ease 0.6 xpos 1300
        repeat

Character("Announcer") "\"¡Es un... Victreebel!{w=0.5} ¿Podrá este Pokémon ser la salvación de nuestro retador, o sumará Janine otra victoria a su historial?\""

may @surprised "Dos Pokémon de Kanto... No los conozco bien, pero esto parece otro combate parejo, ¿no?"
leaf @closedbrow talking2mouth "Para nada.{w=0.5} Con esas Danzas Aleteo, Venomoth tiene todo lo que necesita para barrer a Victreebel."

$ renpy.music.play("Audio/Pokemon/Veno-Victree.ogg", channel="altcry", loop=None)

show venomoth:
    subpixel True
    parallel:
        ease 2.0 ypos 450
    parallel:
        ease 0.05 xpos 20
        ease 0.05 xpos 40
        repeat 20

show victreebel:
    parallel:
        block:
            ease 0.4 ypos 845
            ease 0.2 ypos 850
        block:
            ease 0.6 xpos 1000
    parallel:
        block:
            pause 0.5
            parallel:
                ease 0.4 ypos 845
                ease 0.2 ypos 850
                repeat
            parallel:
                ease 0.6 xpos 1020
                ease 0.6 xpos 1000
                repeat
    
show blank2 with dis:
    alpha 1.0

show revjan:
    subpixel True
    alpha 0.0 xpos -100
    parallel:
        pause 1.5
        ease 1.5 alpha 1.0
    parallel:
        pause 1.5
        ease 7.0 xpos 0

show revveno:
    subpixel True
    alpha 0.0 xpos 100
    parallel:
        pause 1.5
        ease 1.5 alpha 1.0
    parallel:
        pause 1.5
        ease 7.0 xpos 0
        
show revred:
    alpha 0.0 zoom 1.0 xalign 0.5 yalign 1.0
    parallel:
        pause 0.75
        ease 1.5 alpha 1.0

redmind @sad "¿Es así de simple?{w=0.5} Quien tiene el Pokémon más débil, sin importar las circunstancias y sin importar cuánto se esfuerce por luchar..."

Character("Announcer") "\"¡Y aquí vamos, damas y caballeros!{w=0.5} ¡Venomoth y Victreebel se enfrentan en la tercera y posiblemente última ronda de este combate de exhibición!\""

hide venomoth
hide victreebel

$ renpy.music.play("Audio/crowd_cheer.ogg", channel='crowd3', loop=False, fadein=0.0)
$ PlaySound("Pokemon/Moves/Psychic.ogg")

show psychattack behind revred:
    alpha 0.0 zoom 1.0 xalign 0.5
    parallel:
        ease 0.75 alpha 0.75 zoom 1.1
        pause 0.25
        ease 0.25 zoom 1.0
    parallel:
        block:
            parallel:
                xalign 0.0
                ease 0.033 xpos -9
                ease 0.033 xpos 9
                ease 0.033 xpos 0
                repeat 25
            parallel:
                yalign 0.0
                ease 0.033 ypos -3
                ease 0.033 ypos 3
                ease 0.033 ypos 0
                repeat 25
    
show revjan:
    alpha 1.0
    pause 0.75
    ease 0.25 alpha 0.0

show revveno:
    alpha 1.0
    pause 0.75
    ease 0.25 alpha 0.0

Character("Announcer") "\"¡Venomoth ataca con un poderoso ataque Psíquico, pero Victreebel intenta recuperarse con Síntesis!{w=0.6}{nw}"

$ PlaySound("Pokemon/Moves/Synthesis.ogg")

extend @talkingmouth " ¿Podrá nuestro retador resistir?"


hide revjan
hide revveno

show psychattack:
    alpha 0.85
    ease 1.5 alpha 0.0

show revlance with dis:
    alpha 1.0

redmind -happy frownmouth sadbrow "Están en perfecta sincronía. ¿Es solo porque Janine entrenó bien a su Venomoth?{w=0.5} Mientras tanto, su oponente solo puede intentar mantenerse a flote."

if (classstats["Dark"] > 0):
    redmind "Lance habla sobre la fuerza de un Pokémon como si fuera el único factor decisivo en la batalla, pero la Instructora Karen diría que esa es una filosofía egoísta.{w=0.5} ¿Quién tiene razón?"
    redmind "Tiene que haber más en una batalla que solo el poder puro.{w=0.5} {i}Tiene{/i} que haberlo."
elif (classstats["Poison"] > 0):
    redmind "Lance habla sobre la fuerza de un Pokémon como si fuera el único factor decisivo en la batalla, pero el Instructor Koga no estaría de acuerdo.{w=0.5} ¿Quién tiene razón?"
    redmind "Tiene que haber más en una batalla que solo el poder puro.{w=0.5} {i}Tiene{/i} que haberlo."
else:
    redmind "Lance habla sobre la fuerza de un Pokémon como si fuera el único factor decisivo en la batalla, pero tiene que haber más que solo eso.{w=0.5} {i}Tiene{/i} que haberlo."

$ PlaySound("Pokemon/Moves/Psychic.ogg")

$ renpy.music.play("Audio/crowd_cheer.ogg", channel='crowd3', loop=False, fadein=0.0)
$ renpy.music.play("Audio/Stadium_chant.ogg", channel='crowd2', loop=True, fadein=0.5)

Character("Announcer") "\"¡Y Victreebel cae! ¡Otra victoria absolutamente aplastante para Janine!\""

show janine uniform:
    alpha 0.0 xpos 300
    ease 0.75 alpha 1.0

show venomoth:
    subpixel True
    alpha 0.0 yalign 1.0 ypos 1080 xpos 700
    parallel:
        ease 0.75 alpha 1.0
    parallel:
        block:
            parallel:
                ease 1.1 ypos 820
                ease 1.0 ypos 960
                ease 1.1 ypos 850
                ease 1.0 ypos 1000
                ease 1.1 ypos 825
                ease 1.0 ypos 980
                repeat
            parallel:
                ease 0.52 xpos 630
                ease 0.6 xpos 730
                ease 0.62 xpos 620
                ease 0.7 xpos 725
                ease 0.58 xpos 600
                ease 0.65 xpos 700
                repeat

show blank2:
    alpha 1.0
    ease 1.0 alpha 0.0
show revred:
    alpha 1.0
    ease 1.0 alpha 0.0
show revlance:
    alpha 1.0
    ease 1.0 alpha 0.0

Character("Announcer") "\"¿Alguien está sorprendido con el resultado?{w=0.5} ¡Una vez más, Janine demuestra por qué es la capitana del equipo de batalla de la Academia Kobukan!\""

show janine thinking with dis:
    alpha 1.0 xpos 300
    ease 0.75 alpha 0.0
show venomoth:
    alpha 1.0
    ease 0.75 alpha 0.0 xpos 610 ypos 830
    
hide blank2
hide revred
hide revlance

pause 0.5

hide brendan
hide may
hide calem
hide leaf
hide ethan

show brendan surprisedbrow frownmouth at rightside with dis
show may at farrightside with dis
show leaf at farleftside with dis
show calem at leftside with dis
show ethan at centerside with dis

may @angrybrow talkingmouth "¡Dios! No sé qué esperaba cuando dijiste 'combate de exhibición', pero {i}esto{/i} definitivamente no fue eso.{w=0.5} ¿Por qué querías ver esto?"

hide janine
hide venomoth

show leaf happy
show may -surprisedbrow -frownmouth -surprised 
with dis
    
brendan -surprisedbrow -frownmouth -surprised @sadbrow happymouth "¡Oye, esta tambíen era mi primera vez viendo uno!{w=0.5} ¿Cómo iba a saber que los Pokémon del tipo iban a ser aplastados así?"

show leaf surprisedbrow with dis

red @frownmouth "[ellipses]"

leaf -surprisedbrow @talkingmouth surprisedbrow "¿Estás bien, [first_name]?{w=0.5} Te ves muy pálido."

red @wince talking2mouth "¿Eh?{w=0.25} Oh, sí, estoy bien.{w=0.5} Probablemente sea por toda la emoción de hace un momento."

leaf @happy "¿Eso? ¿Tú llamas a eso emocionante?{w=0.5} ¡Encontrar nuestros asientos fue más emocionante que eso!"

calem @surprised "¡!"

calem @closedbrow talkingmouth "Oh, miren, los siguientes combates están por empezar."
    
$ PlaySound("crowd_cheer.ogg")

show blank2 with dis

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_33

narrator "Te quedas a ver el resto de los combates de exhibición, pero ese primer combate sigue destacando por encima de los demás."

scene blank2

$ renpy.music.stop(channel='crowd2', fadeout=10.0)

redmind frownmouth "No puedo dejar de repasarlo en mi cabeza.{w=0.5} La diferencia de poder entre los dos entrenadores y sus Pokémon era abismal."

$ renpy.music.stop(channel='crowd', fadeout=10.0)

redmind "Me pregunto si [pika_name], [starter_name] y yo podríamos..."

stop music fadeout 7.5

redmind @thinking "Ugh, no puedo pensar en cosas como esta ahora.{w=0.5} Tengo cosas más importantes en las que preocuparme."
redmind "Pero aún así..."

jump day010408