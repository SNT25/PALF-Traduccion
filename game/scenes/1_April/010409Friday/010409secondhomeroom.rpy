label secondhomeroom010409:

scene blank2

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom behind blank2

show oakbg behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade

oak @talkingmouth "... Y con el final de la Segunda Revolución Industrial, nuevas tecnologías se volvieron accesibles al público, incluyendo las máquinas de restauración de fósiles."
oak @talkingmouth "Ahora, ¿quién puede decirme cuál fue el primer fósil restaurado?"

$ renpy.music.set_volume(0.1, delay=1.0, channel="music")
$ PlaySound("BellChime.ogg")

$ renpy.pause(2.0, hard=True)
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

oak @talkingmouth "Parece que han sido{w=0.25}.{w=0.25}.{w=0.5} ¡salvados por la campana!"

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.5)

oak @talkingmouth "Muy bien, estudiantes. Asegúrense de revisar el material en línea esta noche.{w=0.5} Voy a subir textos complementarios para aquellos que no entendieron bien la clase de hoy."

redmind uniform @thinking "Por los suspiros de resignación que escuché en la clase, creo que eso nos incluye a casi todos."

call clearscreens from _call_clearscreens_40

show blank2 with dis

pause 1.0
hide blank2 with dis

show screen currentdate with dis

hide oakbg with dis

show leaf uniform embarrassed with dis:
    xpos 0.66
    
show may uniform closedbrow sadmouth with dis:
    xpos 0.33

may @talkingmouth "¡Menos mal que termino!{w=0.5} Después de esta clase, hasta yo misma me siento como un fósil."

leaf -embarrassed @closedbrow talkingmouth "Sí, no veo cómo esto nos sirve a nosotros.{w=0.5} Además, yo ya sé todo lo básico sobre fósiles."

red @closedeyes talkingmouth "¿Eh? ¿Sabes sobre fósiles pero no te emocionan?"

if (starter_species_name in ["Tyrunt", "Archen"]):
    $ startergenderpronoun = "Él" 
    if (playerparty[0].GetGender() == Genders.Female):
        $ startergenderpronoun = "Ella"
    red @closedbrow talking2mouth "Digo, solo mira a [starter_name]. ¡[startergenderpronoun] es un fósil viviente! A mí me parece algo bastante genial."

leaf @closedbrow talkingmouth "Sí, revivirlos es genial, pero conseguirlos... ¡Puaj! ¿De verdad puedes imaginarme cavando en una cueva polvorienta en busca de piedras sin valor?"

show leaf surprisedbrow frownmouth with dis

may @sad "¡Ahh~! ¿Podemos dejar el tema de los fósiles para otra ocasión? Ya tuve suficiente por hoy."

show leaf -surprisedbrow -frownmouth -surprised with dis

red @happy "Tienes razón, lo siento."

red @talkingmouth "Entonces, May, ¿qué vas a hacer ahora?{w=0.5} ¿Vas a salir con Brendan?"

show leaf surprisedbrow frownmouth with dis

may -closedbrow -sadmouth @sadbrow happymouth "Umm, sí... pero, eh, creo que ese tipo de allá quiere hablar contigo."

show blue uniform cocky behind leaf:
    xpos 0.85 xzoom -1
with dis
    
pause 2.0

redmind @playfuleyes unamusedeyebrows unamusedmouth "¿Y ahora qué quiere?"

show may -sadbrow -happymouth with dis
show leaf -surprisedbrow -frownmouth -surprised with dis
    
leaf @talkingmouth "Ahora que lo mencionas, [blue_name] lleva un buen rato mirándote."
leaf @sarcastic "Pensé que te estaba mirando el trasero, pero creo que ya no es el caso."

may @sadbrow happymouth "¿Quiere algo de ti o...?"

red @closedeyes talkingmouth "No sé y no tengo interés en averiguarlo."

leaf @happy "Si tú lo dices."

red @talkingmouth "En fin, estaba pensando en visitar--"
    
blue @talkingmouth "¡Oye, perdedor!"

show blue angry with dis:
    xpos 0.85 alpha 1.0

red @talkingmouth "--la biblioteca de la academia, porque aún no tuve la oportunidad de ver si hay--"
    
blue @talkingmouth "¡Hey, te estoy hablando!"
    
red frownmouth @upeyes talking2mouth "Oh, perdón, no te había escuchado."

show may angrybrow frownmouth 
show leaf angrybrow frownmouth
with dis

blue @talkingmouth "Wow, ¿tonto {i}y{/i} sordo?{w=0.5} ¿Qué tan despistado puedes--"

leaf angrybrow frownmouth @angrymouth "Hey amigo, llevas fastidiando a [first_name] desde el primer día. ¡Déjalo en paz de una vez!"

may angrybrow frownmouth @angrymouth "Sí, ¿qué te pasa?{w=0.5} No te ha hecho nada"

blue @talkingmouth "Ugh, ustedes dos otra vez."

blue cocky @talkingmouth "Así que te la pasas escondiéndote detrás de las chicas, [first_name].{w=0.5} Ni siquiera puedes pelear tus propias batallas, ¿eh?"

leaf @angrymouth "¿Perdón? ¿Qué dijiste?"

red @confusedeyebrows talking2mouth "En serio, [blue_name], ¿qué quieres ahora?{w=0.5} ¿Es otro de tus desafíos sin sentido o...?"

blue @talkingmouth "¡No hay nada de sin sentido en este, esta vez va {i}en serio{/i}! "

if WonBattle("Blue1"):
    show blue angry with dis

    red @closedbrow talking2mouth "¿Y qué hace que este sea diferente del anterior?"
        
    blue "¡Esta vez no voy a contenerme!{w=0.5} ¡Voy a hacerte admitir que lo del martes fue pura suerte!"

else:
    show blue cocky with dis
    
    red @talkingmouth "¿Y qué hace que este sea diferente del anterior?"
        
    blue "¡Esta vez voy a demostrarte que siempre perderás contra mí, especialmente en batallas Pokémon!"

redmind "Realmente tiene una mentalidad cerrada cuando se trata de cosas como esta."
    
show flannery uniform with dis:
    xpos 0.15

show whitney uniform with dis:
    xpos 0.25
    
flannery @talking2mouth "¿Qué está pasando aquí, chicos?{w=0.5} ¿Están haciendo una clase de concurso de gritos?"

whitney @talking2mouth "Si lo fuera, [first_name] estaría perdiendo por paliza."
    
redmind @thinking "Ojalá la voz de [blue_name] no resonara tanto.{w=0.5} Ya hasta formamos una pequeña multitud..."

red @talking2mouth "Vamos, [blue_name], ¿realmente tenemos que hacer esto {i}ahora{/i}?{w=0.5} No podemos dejarlo para más tarde, como--"

blue @talkingmouth "¡Ja! Ni lo sueñes."

show may -angrybrow -frownmouth with dis

show leaf -angrybrow -frownmouth with dis
    
$ renpy.pause(1.25, hard=True)

show blue angry with dis
    
may @sadbrow happymouth "No parece que vaya a aceptar un 'no' como respuesta."

red @thinking "[ellipses]"
red @closedeyes talking2mouth "Ugh, está bien, [blue_name], como quieras."
red @angrybrow talking2mouth "Pero si gano, se acaba esta estupidez.{w=0.5} Nada de provocaciones, nada de insultos y nada de desafíos tontos.{w=0.5} Ya estoy cansado de lo mismo una y otra vez."

blue cocky "No tengo ni idea de qué estás hablando.{w=0.5}{nw}"
extend cocky @talkingmouth " Lo que sea, ¡acepto! No es como si eso fuera a pasar alguna vez."

show whitney surprisedbrow frownmouth with dis

blue @talkingmouth "Pero si yo gano, ¡deberás admitir que siempre serás un Entrenador de segunda comparado conmigo!"

leaf @sarcastic "¿Este tipo tiene un complejo de inferioridad o simplemente te odia con todas sus fuerzas?"

red @closedeyes talkingmouth "Eh...{w=0.5} en realidad, no lo sé."

blue angrybrow talkingmouth "¡Si terminaron de susurrarse, dense prisa!{w=0.5} ¡No tengo todo el día!"

redmind "Sí, claro... aunque eres tú el que insiste con hacer todo esto."

stop music fadeout 0.5

blue cocky @talkingmouth "¡Preparate para perder!"
pause 0.1

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_41

show blank with dis

# FAKE BATTLE
window hide

$ renpy.music.queue("Audio/Music/KantoTrainerStart_Rock.ogg", channel='music', loop=None, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/KantoTrainerLoop_Rock.ogg", channel='music', loop=True, tight=None)

call CreateSplash(["red"], ["blue"], uniforms=[True, True]) from _call_CreateSplash_1

stop music fadeout 0.25

hide blank2

hide blank with dis
    
show may uniform surprisedbrow frownmouth with dis

show leaf uniform surprisedbrow frownmouth with dis

show flannery surprisedbrow frownmouth with dis

show whitney surprisedbrow frownmouth with dis
    
show blue uniform surprised with dis

show screen currentdate

red uniform @confusedeyebrows talking2mouth "Espera, ¿qué? No."

blue angry "¡¿Qué?! ¡¿Cuál es el problema ahora?!"

red @talking2mouth "Estamos en una zona de{i}no combates{/i}. Pelear aquí sería romper las reglas."

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.0, tight=None)
$ renpy.music.stop(channel='crowd', fadeout=0.25)

blue @talkingmouth "¡Dios, eres un cobarde!"

red @closedbrow talking2mouth "Llámame como quieras. No voy a romper las reglas de la academia en mi primera semana solo para alimentar tu ego."

blue @angry "¡Bien! Entonces, tendremos nuestro combate en la Arena de Batalla. ¡Muévete ya!"

hide whitney
hide flannery
with dis

hide blue with dis
        
show leaf -surprisedbrow -frownmouth -surprised with dis
    
show may -surprisedbrow -frownmouth -surprised with dis

$ renpy.pause(2.5, hard=True)

hide blue
    
leaf @talkingmouth "¿De verdad vas a hacer esto?"

red @happy "Dije que lo haría, ¿no?"
red @talkingmouth "Además, tiene razón en algo,{w=0.5} el martes fue solo un combate de práctica. Esto es personal."

leaf @flirttalk "¿Así que piensas aplastarlo hasta el punto que va a dejar de molestarte?"

red @happy "Ese es el plan."

leaf @happy "¡Jeje! Suena interesante.{w=0.5} ¡No puedo esperar!"
    
show hilbert uniform behind leaf with dis:
    xpos (0+240)/1920
    ease 0.75 xpos (100+240)/1920

hilbert @talkingmouth "Por un momento, pensé que no ibas a aceptar su desafío."

red @thinking "[ellipses]"
red @talkingmouth "No puedo decir por tu expresión si crees que aceptarlo fue una buena idea o no."

hilbert @sadbrow talkingmouth "Obviamente lo fue. No te volverás más fuerte si no aceptas este tipo de desafíos."

red @closedeyes talking2mouth "Tienes razón. Bueno, voy a ir a patearle el trasero entonces."

hilbert @talkingmouth "... Asegúrate de estar preparado. He estado observando sus combates; aún no puede controlar a sus Pokémon tan bien como tú, pero los ha entrenado de forma exhaustiva y muy rápido."

red @happy "Aww, gracias, Hilbert. ¿Eso significa que somos amiguis?"

hilbert @angry "Eres ligeramente menos molesto que él, por eso te apoyo. Pero si me provocas, puedo cambiar de bando {i}muy{/i} fácilmente."

red @angrybrow frownmouth "[ellipses]"
red @angrybrow talking2mouth "Gracias."

hide hilbert with dis

red @talkingmouth "Lo siento, chicas, tengo que ir a mi dormitorio."

leaf @surprised "¿Eh? ¿Para qué?"

red @talking2mouth "Hilbert me dio una pista. Se refirió a los Pokémon de Blue en plural. Eso significa que trajo otro, probablemente uno de casa, y planea superarme en número."

may @sad "Oh no... entonces, ¿cómo vas a ganar?"

red @closedbrow talking2mouth "Va a ser complicado, de eso estoy seguro, pero creo que podemos combatir fuego con fuego."

red @happy "Si pudiera tener su atención por un minuto..."

call clearscreens from _call_clearscreens_42
show blank2 with splitfade

show stadium_empty behind blank2

play music "Audio/Music/League_Start.ogg" noloop
queue music "Audio/Music/League_Loop.ogg"

python:
    renpy.transition(dissolve)
    playerparty = [playerparty[0], 
        pikachuobj, 
        GetTrainerTeam("Leaf", "Bulbasaur"),
        GetTrainerTeam("Leaf", "Helioptile"),
        GetTrainerTeam("May", "Torchic"),
        GetTrainerTeam("May", "Venonat")
    ]

show blank2 with Dissolve(1.5)
hide blank2

scene stadium_empty

redmind "Aquí estamos de nuevo.{w=0.5} Me pregunto si siquiera nos dejarán entrar después de lo que pasó la última vez."

show blue uniform frownmouth with dis
    
blue @talkingmouth "¿Tuve que esperar todo este tiempo solo para que fueras a cambiarte? ¡Apresúrate y pídeles que nos dejen usar la arena de una vez!"

red @talking2mouth "¿Por qué yo?{w=0.5} Esto fue {i}tu{/i} idea."
      
blue @talkingmouth "La.{w=0.25}.{w=0.25}.{w=0.5}{nw}"
    
extend @closedbrow talkingmouth " capitana dijo que no podía mostrar mi cara aquí hasta que empiecen las inscripciones para el equipo de batalla."

show blue angry with dis

red @surprised "¿Janine...{w=0.5} te {i}vetó{/i} de la Arena de Batalla?"
red @happy "¡Ja, ja, ja! ¡Y bien merecido!{w=0.5} Eso te pasa por estar de exigente y engreído."
    
blue @talkingmouth "¡Cállate y pregunta de una vez!"
    
red @talkingmouth "Pero espera, eso significa que no podemos tener nuestra batalla si no te dejan entrar.{w=0.5} Qué lástima."

show blue surprisedbrow frownmouth
show janine at leftside
with dis
        
janine @talking2mouth "Estoy dispuesta a hacer una excepción."

red @happy "¡Janine! Soy un gran admirador de tu trabajo. Vi tu combate el miércoles, fue muy impresionante."

janine @angrybrow talking2mouth "Si creés que los halagos te van a servir más que la soberbia de este tipo, estás equivocado."

red @happy "Entendido. Oye, ¿cómo es que tu Venomoth tiene cinco movimientos?"

janine @closedbrow talking2mouth "Técnica secreta shinobi. No te preocupes por eso."

red @happy "Claro. Entonces, ¿ustedes, los del equipo de batalla, están haciendo algo ahora?"

janine @talking2mouth "No, solo estamos yo y un par de graduados del año pasado."
janine @closedbrow talkingmouth "Y escuché lo que estaban diciendo.{w=0.5} Les dejaré usar una arena para su batalla."

red @closedbrow talking2mouth "¿En serio?{w=0.25} ¿Así de fácil?{w=0.5} Pensé que [blue_name] estaba vetado de la Arena de Batalla."

janine @talking2mouth "Lo está, pero tú no. No sería justo echarte por algo que no hiciste."

red @happy "Oye, eres bastante justa. Muchisimas gracias."
    
janine @angrybrow talking2mouth "Sí, sí, tenemos un horario que cumplir. Entren, los pondremos en marcha para que empiecen de inmediato."

hide janine with dis
    
blue @talkingmouth "Buen intento tratando de librarte de esto.{w=0.5} Pero desafortunadamente para ti, no hay escapatoria esta vez."
blue @happy "¡Ahora entra y recibe tu paliza como un hombre!"

if WonBattle("Blue1"):

    show blue angry with dis

    red @angry "Hablas mucho para alguien que ya perdió contra mí antes."
    blue @talkingmouth "Te dije que no iba en serio esa vez.{w=0.5} Y te lo voy a demostrar con esta batalla."
    
else:
    red @closedbrow talking2mouth "Sabes, hay un dicho.{w=0.5}{nw}"

    extend @angry " Decia algo como: 'sé humilde en la victoria y honorable en la der--'"
    
    blue @angrybrow talkingmouth "¡Deja de citar esos estúpidos libros de ancianos, solo estás ganando tiempo!{w=0.5} ¿Acaso tienes tanto miedo de que te destroce? Give me a break!"
    
show blue angry with dis

red @talking2mouth "Terminemos con esto de una vez.{w=0.5} Esta vez vamos en serio, ¿no?"

blue cocky @talkingmouth "Ya era hora de que te pusieras serio.{w=0.5} ¡No voy a contenerme esta vez!"

hide blue with dis
    
pause 1.0

show hilbert uniform:
    xpos 900 alpha 0.0
    ease 0.7 xpos 720 alpha 1.0
    
hilbert @thinking "[ellipses]"

red @happy "¡Hey, Hilbert, sí viniste!"

hilbert @sadbrow talkingmouth "Tu capacidad de observación sigue siendo tan aguda como siempre."

red @talkingmouth "Bueno, me alegra que estés aquí, incluso si tú no lo estás."

hilbert @closedbrow talking2mouth "Solo véncelo. No hace falta tanto sentimentalismo."

red @happy "¡Ese es el plan!"

show hilbert:
    xpos 720 alpha 1.0
    ease 0.75 xpos 1200 alpha 0.0
    
pause 1.5

hide hilbert

show leaf:
    alpha 0.0 xpos 900
    ease 0.5 xpos 750 alpha 1.0
    
leaf @talking2mouth "¿Nervioso?"
    
red @happy "Hey, Leaf. Gracias otra vez por... ya sabes."

leaf @sarcastic "Oh, créeme, quiero ver su boca cerrada tanto como tú. Nunca vi un caso tan grave de 'pez grande en un estanque pequeño'."

red @closedbrow talking2mouth "Entonces... ¿tienes algún consejo útil antes de que entre?"

leaf @surprised "Oh, sí... nope. No necesitas consejos.{w=0.33} Si no puedes vencerlo ahora, nunca lo harás."

if WonBattle("Blue1"):
    leaf @happy "Y como ya lo has hecho antes, ¡esto está en la bolsa!"

else:
    leaf @happy "¡Así que esta es tu oportunidad de redimirte por lo del martes.!"

leaf flirttalk "Estaré animándote desde las gradas de por allá y transmitire en vivo para May.{w=0.5} Ahora, bórrale esa estúpida sonrisa y muéstrale de qué estás hecho."

red @happy "...Bueno, supongo que es ahora o nunca. ¡Allá vamos!"

show leaf -flirt with dis:
    xpos 750 alpha 1.0
    ease 0.5 xpos 800 alpha 0.0
    
$ renpy.pause(1.0, hard=True)

show blue uniform cocky:
    xpos 700 alpha 0.0
    ease 0.5 alpha 1.0

pause 0.5
    
blue @talkingmouth "¿Listo para un viaje directo al basurero?"

red @talkingmouth "Sí, ya tengo el boleto con tu nombre."

stop music fadeout 1.0

blue angry "¡No seas tan engreído! ¡Esta vez tengo un pequeño truco bajo la manga!"

$ renpy.transition(Dissolve(3.0))
show screen currentdate

pause 7.0

red angrybrow talkingmouth "Sí, yo también."

$ trainer1 = Trainer("red", TrainerType.Player, playerparty)
$ trainer2 = MakeTrainer("Blue")
$ GetTrainerTeam("Blue", "Pidgeotto").Level = 18
$ GetTrainerTeam("Blue", "Eevee").Level = 5

call Battle([trainer1, trainer2], uniforms=[False, True]) from _call_Battle_7
$ battlehistory["Blue2"]  = _return

$ renpy.pause(1.0, hard=True)
    
show blue uniform angry behind blank2:
    xpos 700+240 alpha 1.0
    
$ renpy.music.queue("Audio/Music/League_Loop.ogg", channel='music', loop=True, fadein=0.5, tight=None)
$ PlaySound("Short Med Applause.ogg")

show blank2:
    alpha 1.0
    ease 1.0 alpha 0.0
    
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

hide blank2

show red angry at Transform(xpos=0.08, yanchor=0.35)
"{color=#cf0000}[first_name]{/color} & {color=#3110dd}[blue_name]{/color}" "\"¡¿Pero qué MIERDA?!\""

hide red with dis

blue angry "¡Tenías seis Pokémon!"
red angry "Y tu tenías un Pidgeotto de {i}nivel 18{/i}!"
blue "¡Usaste los Pokémon de otras personas!"
red "¡Y tu usaste un Pokémon que has entrenado para luchar durante {i}ocho años{/i}!"
blue "¡Eso fue trampa, imbécil!"
red "¡Mira quién habla, [blue_name]!"

if (WonBattle("Blue2")):
    blue "¡La única razón por la que ganaste es porque hiciste trampa! ¡Me niego a aceptar los resultados de esta batalla!"

    red @angrybrow talking2mouth "¡Sé realista! ¡Sabías que no habría tenido ninguna oportunidad contra tu Pidgeotto sin tomar prestados los Pokémon de mis amigos!"

    show blue angry:
        xpos 700+240
        ease 0.5 xpos 240+800

    blue frownmouth -angry @angrybrow angrymouth"¡Así es, no tienes ninguna oportunidad! ¡Nunca la he tenido y nunca la tendrás!"

    redmind -angry @thinking "Te acabo de ganar hace menos de {i}cinco minutos{/i}."

    show leaf happy:
        xpos 240+1600 alpha 0.0
        parallel:
            ease 0.5 alpha 1.0
        parallel:
            ease 0.75 xpos 240+350
            
    leaf "¡Lo lograron! ¡Sabía que podían hacerlo!"
    
    show leaf -happy with dis:
        alpha 1.0 xpos 240+350
    
    show blue angry at dissolveaway:
        xpos 240+800
    
    $ renpy.music.play(startercry, channel="altcry", loop=None)
    starter "¡[starter_species_name]!"
    
    show leaf:
        xpos 240+350
        ease 0.6 xpos 240+400
        
    show hilbert uniform:
        xpos 240+1200 alpha 0.0
        parallel:
            ease 0.75 xpos 240+1000 alpha 1.0
            
    pause 0.75
    
    show leaf:
        xpos 240+400
        
    show hilbert:
        xpos 240+1000 alpha 1.0
            
    if not WonBattle("Blue1"):
        hilbert @talkingmouth "¿Ves lo que pasa cuando no actúas como un completo bufón? Esa primera derrota con [blue_name] podría haberse evitado por completo."
        red @talkingmouth "¿Cómo? ¿Pidiendo prestados los Pokémon a un par de personas en frente de toda la clase?"
        hilbert @talkingmouth "Sí, eso tambíen habría funcionado."
        
    else:
        hilbert @talkingmouth "Supongo que debo darte algo de crédito, [first_name]."
        
    hilbert @closedbrow talking2mouth "Tengo que ser honesto, no esperaba que fueras a ganar." 
    hilbert @closedbrow talking2mouth "Tampoco se me había ocurrido la idea de tomar prestados los Pokémon de tus amigos... Sólo te estaba indicando que fueras a buscar a tu Pikachu."
    hilbert @talkingmouth "Me has dado mucho en qué pensar."

    red @happy "¿Y bien? ¿Cúal es tu veredicto?"

    hilbert @sadbrow talkingmouth "Si no supiera cuáles realmente te pertenecen, creería que todos son tuyos y que los llevas entrenando desde hace años."
    hilbert @talkingmouth "Además, tengo la ligera sospecha de que podrías haber empezado a darle directivas al Pidgeotto de [blue_name] en medio del combate, y te habría escuchado más a ti que a él."

    red @happy "Ay, vas a hacer que me sonroje con tantos cumplidos. Muchas gracias."

    hilbert @angry "No son cumplidos, demostraste tener el poder. Y mientras el poder exista, alguien va a estar ahí para reclamarlo."
    
    show hilbert sad:
        xpos 240+1000 alpha 1.0
        ease 0.75 xpos 240+1400 alpha 0.0
        
    hilbert "Estuviste bien, eso es todo lo que voy a decirte."
    
    show hilbert:
        alpha 0.0 xpos 240+1400
    
    show leaf:
        xpos 240+400
        ease 0.75 xpos 240+350
        
    pause 0.75
    
    show leaf:
        xpos 240+350
        
    leaf @surprised "Mira eso, incluso tienes al Sr. Serio elogiándote."
    
    red @talkingmouth "Eh, es Hilbert siendo Hilbert.{w=0.5} Ya termine por acostumbrarme."
           
    if WonBattle("Blue1"):
        leaf @closedbrow talkingmouth "Ya van dos seguidas,{w=0.5} ¿crees que eso sera suficiente para que [blue_name] deje de fastidiarte?"
        
    else:
        leaf @closedbrow talkingmouth "Ya estan igualados,{w=0.5} ¿crees que eso sera suficiente para que [blue_name] deje de fastidiarte?"
    
    red @sadbrow talkingmouth "Ni de broma, aunque nunca hay que dejar de soñar."

    leaf @surprised "Pero una promesa es una promesa,{w=0.5} [blue_name] te prometio dejarte en paz."

    red @closedbrow talking2mouth "Sí, pero esta no es ni por lejos la primera vez que tenemos un combate en el que promete dejar de meterse conmigo..."
    red @happy "¡Pero es una de las tres únicas veces que pude ganarle en serio! Puedo jurar que solía tener pesadillas con ese Pidgey. Bueno... ahora es un Pidgeotto."
    
    show blue angry:
        alpha 0.0 xpos 240+50
        ease 0.75 xpos 240+0 alpha 1.0
            
    pause 0.75
    
    show leaf surprisedbrow frownmouth with dis
    
    blue sad "{size=28}{i}¡No se suponía que terminara así...!{/i} {/size}"
    
    red sadbrow frownmouth "[ellipses]"
    redmind "Hace que sea muy difícil sentir lástima por él... quiero decir, entiendo que está desesperado por ganar, pero todas sus heridas son hechas por él mismo... o al menos son {b}muy{/b} evitables."
    red @talking2mouth "Ey. Blue, mirá, lo hiciste bien, pero--"
    
    pause 1.0
    
    show blue angry with dis:
        xpos 240+0
        ease 0.5 xpos 240+400
        
    show leaf surprisedbrow frownmouth:
        xpos 240+350
        pause 0.2
        ease 0.5 xpos 240+1000
        
    blue angry "¡Ni se te ocurra sermonearme!{w=0.5} ¿Realmente crees que eres mejor que yo?"

    show blue angry:
        xpos 240+400
        
    show leaf angry:
        xpos 240+1000
    
    leaf @sarcastic "¡Superalo de una vez! ¡Perdiste el combate, así que dejá de comportarte como un imbécil!"
    leaf @talking2mouth "¡Hiciste una promesa y tienes que cumplirla!"

    blue frownmouth "No tengo ni la más mínima idea de a qué te refieres."

    leaf @surprised "Pe-pe-pero...{nw}"
    show stadium_empty with vpunch
    extend angry " ¡Lo prometiste! Cuando prometés algo, eso significa... ¡significa que lo {i}prometiste{/i}!"
    
    blue angry "¿De qué diantres estás hablando?{w=0.5} ¿Acaso eres la niñera de este perdedor o qué mier--"

else:
    red @talkingmouth "La única razón por la que has ganado es porque has traído un Pidgeotto sobre entrenado a un combate contra un grupo de nivel 5." 

    blue "¡No me jodas! ¡Tu equipo era tres veces más grande que el mío! Sabés que no tenía ninguna chance contra toda esa carne de cañón si no fuera por mi Pidgeotto."

    red @talkingmouth "¡No son carne de cañón, son los amigos de mis amigos! ¡Y lo único que hicieron fue emparejar las cosas! ¡Tú estabas tratando de engañarme! Al menos {i}yo{/i} sabía que ibas a hacer alguna trampa. ¡Pedir prestados Pokémon fue lo único que me dio una oportunidad!"

    show blue angry:
        xpos 700+240
        ease 0.5 xpos 240+800

    blue frownmouth -angry @angrybrow angrymouth "¡No tienes ninguna chance! ¡Nunca la tuviste, y nunca la tendras!"

    redmind -angry frownmouth @thinking "Si hubiera sabido qué Pokémon tenía, podría haberle vencido..."

    show leaf sad:
        xpos 240+1600 alpha 0.0
        parallel:
            ease 0.5 alpha 1.0
        parallel:
            ease 0.75 xpos 240+350
            
    leaf "Bueno... yo creo que lo hicieron muy bien. Especialmente ustedes, Bulbasaur y Helioptile."
    
    show leaf happy:
        alpha 1.0 xpos 240+350

    leaf "Entonces no se pongan tristes, ¿sí, chicos?"
    
    show blue angry at dissolveaway:
        xpos 240+800
    
    $ renpy.music.play(startercry, channel="altcry", loop=None)
    starter "[starter_species_name]..."
    
    show leaf -happy with dis:
        xpos 240+350
        ease 0.6 xpos 240+400
        
    show hilbert uniform:
        xpos 240+1200 alpha 0.0
        parallel:
            ease 0.75 xpos 240+1000 alpha 1.0
            
    pause 0.75
    
    show leaf:
        xpos 240+400
        
    show hilbert:
        xpos 240+1000 alpha 1.0
            
    if WonBattle("Blue1"):
        hilbert @talkingmouth "...{w=0.5} Deberías haberlo hecho mejor. Vi esa primera batalla que tuviste con él, tenías {i}más{/i} que suficiente para ganarle."
        
    else:
        hilbert "Veo que no aprendiste nada de tu primera derrota."
        
    hilbert @talkingmouth "Tuviste una ventaja ideal y la desperdiciaste, qué pérdida de tiempo."

    red @sad "¿Ventaja ideal?"

    hilbert @sadbrow talkingmouth "¿Tomaste prestados esos Pokémon, no? Si no supiera cuáles realmente te pertenecen, creería que todos son tuyos y que los llevas entrenando desde hace años."
    hilbert @talkingmouth "Además, tengo la ligera sospecha de que podrías haber empezado a darle directivas al Pidgeotto de [blue_name] en medio del combate, y te habría escuchado más a ti que a él."
    hilbert @angry "Y aun así perdiste."

    pause 2.0

    hilbert @angry "Si no puedes hacer uso de ese poder, otro más lo hará."
    
    show hilbert sad:
        xpos 240+1000 alpha 1.0
        ease 0.75 xpos 240+1400 alpha 0.0
        
    hilbert "Debes mejorar."
    
    show hilbert:
        alpha 0.0 xpos 240+1400
    
    show leaf:
        xpos 240+400
        ease 0.75 xpos 240+350
        
    pause 0.75
    
    show leaf:
        xpos 240+350
        
    leaf @surprised "Uf... ¿No fue un poco duro?"
    
    red @talkingmouth "Eh, es Hilbert siendo Hilbert.{w=0.5} Ya termine por acostumbrarme."
           
    if WonBattle("Blue1"):
        leaf @closedbrow talkingmouth "De verdad pensé que ganarias otra vez, después de haberle ganado la anterior..."

        red @happy "Sí, yo también lo pensaba. Sólo que no vi venir al Pidgeotto."
        
    else:
        leaf @closedbrow talkingmouth "Quiero decir, estoy segura de que eres bueno combatiendo en otras situaciones. ¿Será que simplemente [blue_name] te saca de tus casillas?"
    
    red @sadbrow talkingmouth "Quiero decir, por más imbécil que sea Blue, es un {i}muy{/i} buen entrenador. Siempre lleva a sus Pokémon al límite de sus capacidades." 
    red @closedbrow talking2mouth "Podrías darle un Rattata y seguro que para el final del día ya sería un Raticate. Seguro, no le haría ni caso, pero con tanto poder... ¿realmente importa?"
    red @happy "Ya hemos combatido antes, y creo que solo le gané dos veces. Puedo jurar que solía tener pesadillas con ese Pidgey. Bueno... ahora es un Pidgeotto."
    
    show blue angry:
        alpha 0.0 xpos 240+50
        ease 0.75 xpos 240+0 alpha 1.0
            
    pause 0.75
    
    show leaf surprisedbrow frownmouth with dis
    
    blue angry "{size=44}¡Hey! Hiciste una promesa, ¿recuerdas? ¡Ponte las pilas y cúmplela, entrenador inferior!{/i}{/size}"
    
    red sadbrow frownmouth "[ellipses]"
    redmind "Haaah... ¿Realmente tengo el suficiente orgullo como para armar un escándalo por esto?"
    redmind "Si fuera cualquier otra persona, probablemente sí, pero..."
    red @talking2mouth "Está bien, Blue. Me ganaste de forma justa y merecida."
    
    pause 1.0
    
    show blue angry with dis:
        xpos 240+0
        ease 0.5 xpos 240+400
        
    show leaf surprisedbrow frownmouth:
        xpos 240+350
        pause 0.2
        ease 0.5 xpos 240+1000
        
    blue angry "¡S-sí, eso ya lo sé! ¡Pero, tú dijiste que admitirías que nunca serás mejor entrenador que yo! ¡Así que {i}dilo{/i}!"

    show blue angry:
        xpos 240+400
        
    show leaf angry:
        xpos 240+1000
    
    leaf @sarcastic "¡Dejá de creérte la gran cosa! Ya ganaste el combate, ¡ahora dejá de actuar como un idiota!"
    leaf @talking2mouth "¡[first_name] cumplió su promesa! ¡Ahora dejalo en paz!"

    blue angry "¿De qué diantres estás hablando?{w=0.5} ¿Acaso eres la niñera de este perdedor o qué mier--"
    
lance @talking2mouth "Es suficiente."

show lance:
    xpos 240+100 alpha 0.0
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        ease 1.25 xpos 240+450

show janine:
    xpos 240+-50 alpha 0.0
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        ease 1.0 xpos 240+70

show blue surprisedbrow frownmouth:
    xpos 240+400
    pause 0.1
    ease 0.75 xpos 240+870
    
show leaf surprisedbrow frownmouth:
    xpos 240+1000
    ease 0.75 xpos 240+1380
    
$ renpy.pause(1.5, hard=True)

show lance:
    alpha 1.0 xpos 240+450

show janine:
    alpha 1.0 xpos 240+70

show blue surprisedbrow frownmouth:
    xpos 240+870
    
show leaf surprisedbrow frownmouth:
    xpos 240+1380

redmind @sadbrow frownmouth "Ay no...{w=0.5} Bueno, era de esperarse de que apareciera por este lugar, ¿pero por qué justo ahora?"

if not WonBattle("Blue2"):
    lance @closedbrow talking2mouth "No hay mérito en jactarse tras una victoria.{w=0.5} ¡No toleraré este tipo de comportamiento en la Arena de Batalla!"

blue @angry "Eres tu..."

lance @closedbrow talking2mouth "El combate ya ha terminado. ¡Apúrense y dense la mano!{w=0.5} Están molestando a los demás Entrenadores."

lance @angry "Eso va para todos.{w=0.5} ¡A no ser que estén con el Equipo de Batalla, lárguense de aquí de inmediato!"

show lance:
    xpos 240+450
    ease 0.5 xpos 240+500
    
show leaf surprisedbrow frownmouth
show blue surprisedbrow frownmouth behind leaf
with dis

lance @talking2mouth "Excepto tú.{w=0.33} Tú te quedas."

show lance:
    xpos 240+500
    
red @surprised "... ¿Yo?"

show hilbert uniform behind leaf:
    xpos 240+1170 alpha 0.0
    ease 0.5 alpha 1.0 xpos 240+1130

hilbert @surprised "¿Qué hiciste, [first_name]?"

show hilbert:
    alpha 1.0 xpos 240+1130
    
red @closedbrow talking2mouth "Parece que no estuviste en el combate de exhibición después de todo. Bueno, creo que esto va a ser la segunda parte de eso."

hilbert @sadbrow talkingmouth "... Bueno, ya me aburrí, así que mejor no lo cuentes."

show hilbert:
    xpos 240+1130 alpha 1.0
    ease 0.5 xpos 240+2000 alpha 0.0
    
hilbert @talkingmouth "Nos vemos."

show hilbert:
    xpos 240+2000 alpha 0.0
    
show leaf surprisedbrow frownmouth:
    xpos 240+1380 ypos 1080 zoom 1.0
    pause 0.25
    ease 0.75 xpos 240+1250 ypos 1330 zoom 1.35
    
leaf @sadbrow talkingmouth "Está bien, supongo que tengo que irme...{w=0.5} Me quedaría, pero prefiero no ponerme en contra de Lance o Janine."

show leaf:
    xpos 240+1250 ypos 1330 zoom 1.35
    
leaf -surprisedbrow -frownmouth @happy "¡Nos hablamos más tarde!"

show leaf:
    xpos 240+1250 alpha 1.0 ypos 1330 
    ease 0.75 xpos 240+1600 alpha 0.0 

red @closedbrow talking2mouth "Okay, nos vemos."

show blue:
    xpos 240+870
    ease 0.75 xpos 240+1200

redmind frownmouth "Ah... sera mejor prepárate para más quejas."
redmind "... Un momento, ¿Blue todavía está aquí?"

hide leaf

show blue:
    xpos 240+1200
    
lance @closedbrow talking2mouth "Tú, el que esta ahí.{w=0.5} Creí haber dicho que todos se marcharan."

show blue:
    xpos 240 + 1200 xzoom 1
    ease 0.5 xzoom -1

blue @talkingmouth "Tú eres el supervisor del Equipo de Batalla, ¿no? Eres Lance."

lance @angry "No lo voy a repetir.{w=0.33} Vete."

show blue:
    xpos 240+1200 xzoom -1
    ease 0.5 xpos 240+1100

blue @surprised "¡Espera! Estuviste viendo nuestro combate, ¿verdad?{w=0.5}{nw}"

show blue:
    xpos 240+1100
    
extend @talkingmouth " Creo que está bastante claro que tengo lo necesario para entrar al Equipo de Batalla."

show janine surprisedbrow frownmouth
show blue happy
with dis

blue @talkingmouth "Janine no quiere admitirlo, ¡pero seguro que alguien como usted reconoce el talento cuando lo ve!"

show blue surprisedbrow frownmouth
show janine -surprisedbrow -frownmouth -surprised
with dis

lance @talking2mouth "No."

show blue:
    xpos 240+1100
    ease 0.75 xpos 240+1200

blue @sadbrow surprisedmouth "Pero...{w=0.25} yo solo--{w=0.5} usted no acaba de..."

show blue surprisedbrow frownmouth:
    xpos 240+1200
    
lance @talking2mouth "Dije que no.{w=0.5} Ahora lárgate."

janine @talking2mouth "No te estás haciendo ningún favor viniendo a rogar todos los días para que te aceptemos, ¿sabés?"
janine @talking2mouth "Es...{w=0.5}{nw}"
extend @sad " bueno, francamente, es un poco vergonzoso de ver."

lance @closedbrow talking2mouth "Además, confío plenamente en el juicio del Capitán del Equipo de Batalla. Si el Capitán dice que entras, entonces entras. Y del mismo modo, si el Capitán dice que no..."
lance @angrybrow talking2mouth "Entonces, no entras." 
lance @talking2mouth "No intentes pasarte por alto la cadena de mando. A pesar de mi estatus como Campeón, soy solo el {i}Asesor{/i} del Equipo de Batalla."

pause 1.5

show blue angry

pause 1.0

show blue angry:
    xpos 240+1200
    ease 0.25 xpos 240+1100
    
blue @talkingmouth "¿Y eso qué?"

if not WonBattle("Blue2"):
    blue @talkingmouth "¿Están {i}ciegos{/i}?{w=0.5} ¡Aplasté a [first_name]! ¡No tuvo ninguna oportunidad!"

blue @talkingmouth "¡Están cometiendo el mayor error de sus vidas al no ponerme en el equipo ahora mismo!{w=0.5} ¡Soy lo mejor que le ha pasado a esta escuela, así que merezco estar aquí {i}ahora mismo{/i}!"

lance @sadbrow talking2mouth "¿{i}Tú eres{/i} el nieto del Profesor Oak?"

show lance:
    xpos 240+500
    ease 1.0 xpos 240+700
    
lance @talking2mouth "Presumes y te pavoneas, pero estás tan inseguro de tus habilidades que te niegas a ganarte tu lugar en el equipo como cualquier otro estudiante."

show lance:
    xpos 240+700

show blue angry:
    xpos 240+1100
    ease 0.5 xpos 240+1000
    
blue @angrybrow talkingmouth "No sabes una mierda sobre mí.{w=0.5}{nw}"

show janine angrybrow frownmouth with dis

extend @talkingmouth " ¿Te creés alguien importante solo porque manejás las cosas en este lugar?"

janine @angrybrow talking2mouth "¡Muestra algo de respeto!{w=0.5} Una palabra más y haré que te saquen de este edificio."

lance @closedbrow talking2mouth "Janine, permíteme."

lance @sadbrow talking2mouth "Es la segunda vez esta semana que un estudiante nuevo se atreve a hacer juicios sobre mi persona."
lance @angrybrow talking2mouth "Y, aunque tú has sido un poco más educado, encuentro tus palabras mucho más tediosas e inútiles de escuchar. No es una posición en la que un aspirante al Equipo de Batalla quiera estar."
lance @sadbrow talking2mouth "Ahora lárgate."

pause 1.0

show blue angry:
    xpos 240+1000
    ease 1.0 xpos 240+1200
    
blue @frownmouth "[ellipses]"

show blue:
    ease 0.5 xpos 240+1200
    
blue closedbrow angrymouth "¡Aghhh!"

show blue:
    xpos 240+1200 alpha 1.0
    ease 0.5 alpha 0.0 xpos 240+1500
    
$ renpy.pause(0.75, hard=True)

hide blue
    
redmind @happy "Wow, I need to start taking tips from these guys to save myself some [blue_name]-induced migraines."

show lance:
    xpos 240+700
    ease 0.75 xpos 240+950
    
show janine:
    xpos 240+70
    ease 1.0 xpos 240+350

lance @sadbrow talking2mouth "Now then...{w=0.5} our business is with you."

show lance:
    xpos 240+950
    
show janine:
    xpos 240+350

lance @talking2mouth "...You look vaguely familiar.{w=0.5} Have we met before?"

red @sadbrow sweat talkingmouth "Um, well... I look pretty similar to Ethan? If you ignore our hair, anyway."

janine -angrybrow @closedbrow talkingmouth "The kid's a new student. He's only been here for... what, five days?{w=0.5} According to Blue, his name's [first_name]."

lance @closedbrow talking2mouth "[first_name]...{w=0.5} I'm sure I've heard that name from somewhere."

red @surprised "Uh, never mind that.{w=0.5} You said you have business with me?{w=0.5}{nw}"
extend @happy " It's getting kinda late, so I'd like to get back before curfew."

janine @talking2mouth "Don't worry, this won't take long.{w=0.5} We just wanted to ask a few questions about your team."

if WonBattle("Blue2") == False:
    lance @talking2mouth "You commanded a team of extremely diverse Pokémon flawlessly. You may have lost that battle, but they responded to your commands with the swiftness of a Champion-trained Pokémon."
else:
    lance @talking2mouth "You commanded a team of extremely diverse Pokémon flawlessly. They responded to your commands with the swiftness of a Champion-trained Pokémon."

lance @talking2mouth "How long have you been training them for?"

janine @closedbrow talkingmouth "My Venomoth didn't get a word I was saying 'til about middle school.{w=0.5} And I've had him since I was four."

janine @talking2mouth "You must've put your team through some intense training.{w=0.5} Why haven't any of them except the Pikachu evolved yet?"

show janine surprisedbrow frownmouth
show lance sadbrow
with dis

red @talkingmouth "Uh... well, actually, only the [starter_species_name] and the Pikachu are mine.{w=0.5} I borrowed the other four from my friends for this specific battle."
redmind @thinking "...Crap, that's not against the rules, is it?"
redmind @thinking "Well, whatever I say here, I can't tell them about Sam's 'Frienergy' theory. If he's right, that's something I need to keep very private."

red @talkingmouth "And I really didn't do anything particularly special.{w=0.5} I just told them what I wanted them to do, and they listened."

show lance closedbrow
show janine thinking
with dis

redmind "...Oh, crap. That was a lie, wasn't it? I've always been awful at lying. Was that, all along, because of Sam's theory?"

pause 1.5

janine @angrybrow talking2mouth "Are you serious?"

show janine surprisedbrow frownmouth
show lance angrybrow
with dis

show blue:
    xpos 240+1700 alpha 0.0
    ease 0.5 xpos 240+1300 alpha 1.0
    
blue uniform @angry "Yeah. Four of those aren't even his! Which is totally cheating, right?"

show janine angrybrow frownmouth

show blue angry:
    xpos 240+1300 alpha 1.0
    
blue @angrybrow talkingmouth "What're you trying to pull, [first_name]?!"

show blue surprisedbrow frownmouth with dis

janine @angrybrow talking2mouth "I thought I told you to keep your mouth shut!"

show blue angry:
    xpos 240+1300 alpha 1.0
    ease 0.5 alpha 0.0 xpos 240+1800
    
$ renpy.pause(1.5, hard=True)

hide blue

janine -angrybrow @closedbrow talkingmouth "In any case, there has to be something else.{w=0.5} Working with Pokémon, let alone battling with them, just isn't that simple."

redmind @sad "Geez. There's just no belief there. Now I'm second-guessing everything I'm saying... This ability is really complicating things."
redmind @thinking "I just wish I knew if it existed."

janine @talking2mouth "Do you use hand signals or specific vocal commands?{w=0.5} Come on, give us something to work with here."

red @sadbrow talkingmouth "I really don't know what to tell you.{w=0.5} They understand me and I can understand them. I'm starting to feel like a broken record here."

janine @closedbrow talkingmouth "Okay, these were your friends' Pokémon. Are your friends, like, Champions? Did they put them through intense training without raising their level?"

red @sadbrow talkingmouth "No... my friends are just other students. I met them, uh, last Friday."

janine @closedbrow talkingmouth "Okay... you said that Pikachu was yours, right? What about--"

lance @closedbrow talking2mouth "I should've known."

show janine surprisedbrow frownmouth with dis

lance @sadbrow talking2mouth "Now I remember.{w=0.5} {i}You're{/i} the one with that runt of a Pikachu."

redmind "Oh, crap."

janine -surprisedbrow -frownmouth @talking2mouth "Wait, this kid?{w=0.5} He's the one that you were complaining about before?"

janine @closedbrow talkingmouth "Small world."

lance @sadbrow talking2mouth "I shudder to think of the time I've wasted listening to your pitiful meanderings...{w=0.5}{nw}"

extend @angrybrow talkingmouth " You had no idea what you were talking about from the beginning."

show lance angrybrow:
    xpos 240+950
    ease 0.5 xpos 240+900
    
lance @talking2mouth "They understand me and I understand them.'{w=0.5} To say such things...{w=0.25} you mock the very foundation of Kobukan Academy."

show lance:
    xpos 240+900

lance closedbrow @talking2mouth "I have nothing more to say to you."

janine @sadbrow talking2mouth "Lance, take it easy.{w=0.5} I think he was being serious."

show lance:
    xpos 240+900
    ease 0.5 xpos 240+950
    
lance @talking2mouth "If he is, and he is not intentionally wasting our time, he is direly delusional, and we have ever more reason to show him the door."
    
redmind @angrybrow frownmouth "What's his problem all of a sudden?{w=0.5} It's like his personality completely turned itself on its head when he remembered who I was."

lance @talking2mouth "I was hoping to get some information out of you, but it's clear that you're just wasting everyone's time."

show blue uniform happy:
    xpos 240+1350 alpha 0.0
    ease 0.5 alpha 1.0
    
blue @talkingmouth "Pfft."
    
show blue sad with dis

lance @angrybrow talking2mouth "{i}Why are you still here?{/i}{w=0.5} Has anyone, ever, even once in your privileged life, told you {i}no?{/i}"

if WonBattle("Blue2"):
    lance @sadbrow talking2mouth "The grandson of Professor Oak losing to someone like him...{w=0.5} What an embarrassment."
    
    blue "...!"
    
    lance @angrybrow talking2mouth "You could have beaten him, but you lacked finesse and discipline.{w=0.5} Even with your absurd level advantage, you struggled mightily."

    lance @closedbrow talking2mouth "Your match was a travesty to watch."

else:
    lance @sadbrow talking2mouth "The grandson of Professor Oak having so much trouble with someone like him...{w=0.5} What an embarrassment."
    show lance angry
    
    blue "...!"
    
    lance @angrybrow talking2mouth "Don't think I didn't hear you mouthing off when you came in here.{w=0.5} Celebrating victory before the match even started...{w=0.5}"
    
    lance @closedbrow talking2mouth "Even with your overwhelming level advantage, it was far from a clean battle."
    

show lance thinking
show blue angry
with dis

redmind @happy "Call me immature, but even I can't stop myself from smiling at [blue_name] getting scolded like that.{w=0.5} It's sort of refreshing to see it happen to someone that's not me."

show blue angry:
    xpos 240+1350
    ease 0.25 xpos 240+1250
    
blue @angrybrow talkingmouth "You got a problem with the way I do things, I'll take you on myself!"

show janine angry

blue @talkingmouth "Acting so high and mighty just 'cause of a few trophies.{w=0.5} Yeah, I know of your accomplishments... or lack thereof."

show lance angry
show blue cocky
with dis

blue @talkingmouth "Yeah, you might've Champed two regions, but how many tries did that take? One of the Elite Four literally died of old age before you ever beat her!"

show blue angry

$ PlaySound("Whoosh.ogg")

show janine:
    alpha 1.0
    ease 0.25 alpha 0.0
show smoke as smoke1:
    alpha 0.0 xpos 240+300 yalign 3.0
    parallel:
        ease 3.0 yalign 0.5
    parallel:
        ease 0.5 alpha 1.0
        pause 0.5
        ease 3.0 alpha 0.0
        
$ renpy.pause(0.5, hard=True)

show smoke as smoke2:
    alpha 0.0 xpos 240+850 yalign 3.0
    parallel:
        ease 3.0 yalign 0.5
    parallel:
        ease 0.5 alpha 1.0
        pause 0.5
        ease 3.0 alpha 0.0

show lance:
    xpos 240+950
    ease 0.75 xpos 240+300

show blue surprisedbrow frownmouth with dis:
    xpos 240+1250
    ease 0.25 xpos 240+1200
    
pause 0.5
    
show janine angry:
    alpha 0.0 xpos 240+850
    ease 0.25 alpha 1.0

janine @angrybrow talking2mouth "I've just had about enough of you and your {nw}"

show janine angry:
    xpos 240+850 alpha 1.0
    
show blue surprisedbrow frownmouth:
    xpos 240+1200

extend @talkingmouth "disrespect towards Lance.{w=0.5} If you don't get out of my face within the next ten seconds, we're gonna have a {i}big{/i} problem."
    
redmind @thinking "'Discretion is the better part of valor,' Blue..."

show blue angry with dis

blue @talkingmouth "...Tch!"

blue @angrybrow talkingmouth "[first_name]! You won't always be able to rely on your friends! You'll be left alone and powerless one day--{w=0.5}and you're still just a third-rate Trainer compared to me!"

show blue angry:
    xpos 240+1200
    ease 0.25 xpos 240+1250
    
show janine angry:
    xpos 240+850
    ease 0.5 xpos 240+950

janine @talking2mouth "Get {i}out!{/i} "
    
show blue angry:
    xpos 240+1250 alpha 1.0
    ease 0.5 xpos 240+1800 alpha 0.0

pause 1.0

hide blue

redmind "I thought I was a second-rate Trainer.{w=0.33} When did I get demoted?"

show janine -angry with dis:
    xpos 240+950
    ease 1.0 xpos 240+1000

show lance -angry with dis:
    xpos 240+300
    ease 0.5 xpos 240+500
    
lance @talking2mouth "And why haven't {i}you{/i} left yet?"
    
lance @sadbrow talking2mouth "Leave. You have no more business being here."

red @talking2mouth "On my way out."

janine @talking2mouth "Just a second, Lance.{w=0.5} I'd like a word with him myself, if you're okay with that."
    
lance @closedbrow talking2mouth "I see no point, but do what you want."

lance @talking2mouth "I take my leave of you.{w=0.5} If you need me for something, you know where to find me."

show lance:
    xpos 240+500 alpha 1.0
    parallel:
        pause 0.5
        ease 0.5 alpha 0.0
    parallel:
        ease 1.0 xpos 240+0
        
$ renpy.pause(2.0, hard=True)

hide lance

show janine:
    xpos 240+1000
    ease 0.75 xpos 240+720
    
janine @happy "Phew! Now that we have some privacy, I'd like to talk a little more about you and your Pokémon."

show janine:
    xpos 240+720
    
janine @talking2mouth "You said you've only had your starter, that [starter_species_name], for a short while, but you two can understand what the other is saying without a hitch.{w=0.5} And it's the same way with your Pikachu."

janine @closedbrow talkingmouth "I mean, you're hiding something, obviously, but I don't think you're straight-up lying."

red @happy "You believe me?{w=0.33} Finally!{w=0.5} It was starting to feel like everybody in the room was against me."

janine @happy "Yeah, but, you might prefer that I didn't believe you. I mean, I'm going to try and use that. Use the heck out of it, actually."

red @surprised "U-use? What do you mean?"

janine @closedbrow talkingmouth "You said that four of your Pokémon weren't actually yours. Never trained with them before?"

red @talkingmouth "Uh, yeah."

janine @closedbrow talkingmouth "Well, that's {i}really{/i} interesting. Because if you can do that with Pokémon that are stronger than the ones you have on-hand, then we could just hand you a couple strong Pokémon and have you go to town."
janine @talking2mouth "As long as you're able to borrow, you wouldn't have to train at all... which would save us so much time..."

redmind @lightblush frownmouth surprisedbrow "Uh... she's looking at me like she's a spider figuring out the best way to eat me..."

red @surprised "I'm not sure I can help {i}that{/i} much. I mean, I'm still figuring out what I can, and, y'know, {i}can't{/i} do with Pokémon."

janine @angrybrow talking2mouth "Uh, yeah. Duh. And this is how we figure it out. Test you until you break."

red @surprised "Could we stop right before that point?"

show janine:
    xpos 240+720
    ease 0.5 xpos 240+800
    
janine @closedbrow talkingmouth "You can tap out any time."

show janine:
    xpos 240+800
    ease 0.5 xpos 240+720

janine @happy "After I let you, I mean."

show janine:
    xpos 240+720

redmind @surprisedbrow frownmouth "Uh... I kinda feel like something in me is awakening..."

janine @talking2mouth "Hey, you alright? You look pale."

red @talkingmouth "Yeah, it's, uh, it's just been a long day."

janine @surprised "Oh, yeah, it's getting late, right? You should probably head back."

red @happy "Right. Thanks."

pause 2.0

show janine:
    xpos 240+720
    ease 0.5 xpos 240+800
    
janine @talking2mouth "Oh, hold up.{nw}{w=0.5}" 
extend @happy " You're cool with being pushed to your absolute breaking point, right?"

menu:
    "As long as it's by you.":
        show janine blush surprised with dis

        pause 2.0
        
        janine angrybrow blush smirkmouth "You've got a lot of nerve."

        red @angrybrow talkingmouth "As I'm willing to prove in battle. Over and over."

        janine -blush -angrybrow -smirkmouth @closedbrow talkingmouth "...Borrow some stronger Pokémon. Your current Pokémon just won't cut it for the tryouts, never mind that you only have two of them."

        red @surprised "Wait, what are you saying?"

        janine @talking2mouth "Well, I'm going to see you at the Battle Team tryouts on the 19th."

        janine @talkingmouth "Right?"

        red @angrybrow talking2mouth "Absolutely."

        pause 1.0

        $ ValueChange("Janine", 2, (240 + 800) /1920)

        janine angrybrow blush smirkmouth "{w=0.25}.{w=0.25}.{w=0.25}.Good boy."

    "Absolutely.":
        janine @closedbrow talkingmouth "...Borrow some stronger Pokémon. Your current Pokémon just won't cut it for the tryouts, never mind that you only have two of them."

        red @surprised "Wait, what are you saying?"

        janine @talking2mouth "Well, I'm going to see you at the Battle Team tryouts on the 19th."

        janine @talkingmouth "Right?"

        red @angrybrow talking2mouth "Absolutely."

        pause 1.0

        $ ValueChange("Janine", 1, (240 + 800) /1920)

        janine @smirkmouth "Correct answer."

    "I'd rather not.":
        janine @closedbrow talkingmouth "Hm... well, there's a way where you wouldn't have to train as hard, I guess."

        janine @closedbrow talkingmouth "...Borrow some stronger Pokémon. Your current Pokémon just won't cut it for the tryouts, never mind that you only have two of them."

        red @surprised "Wait, what are you saying?"

        janine @talking2mouth "Well, I'm going to see you at the Battle Team tryouts on the 19th."

        janine @talkingmouth "Right?"

        red @angrybrow talking2mouth "Absolutely."

        pause 1.0

        janine @smirkmouth "Correct answer."

janine @happy "Now, get to bed.{w=0.5} If you're not back soon, security will catch you."

redmind @thinking "Yeah, I'd have more luck escaping them if I was a pizza... at least according to Hilbert."

show janine:
    xpos 240+800
    ease 1.0 xpos 240+900

janine @talking2mouth "Remember. April 19th. Be there."

window hide

show blank2 with dis:
    alpha 1.0

stop music fadeout 1.5

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_43

python:
    HealParty()
    playerparty.remove(GetTrainerTeam("Leaf", "Bulbasaur"))
    playerparty.remove(GetTrainerTeam("Leaf", "Helioptile"))
    playerparty.remove(GetTrainerTeam("May", "Torchic"))
    playerparty.remove(GetTrainerTeam("May", "Venonat"))
    renpy.pause(3.0, hard=True)

show night at vspaz

pause 3.5

hide night

############################################################################################################################################################################################################################
#### 5. END OF DAY #########################################################################################################################################################################################################
############################################################################################################################################################################################################################

play music "Audio/Music/SoaringIllusions_Intro.ogg" noloop
queue music "Audio/Music/SoaringIllusions.ogg"

$ renpy.transition(dissolve)
show screen currentdate

$ renpy.music.play("Audio/mediumcrowdloop.ogg", channel='crowd', loop=True, fadein=2.0)

scene lounge
show brendan:
    xpos 240+600
show may:
    xpos 240+900
with Dissolve(2.0)

redmind @thinking "What a day..."

redmind @thinking "I agreed to meet with Brendan and May for dinner without a second thought, but I haven't paid any attention to the conversation the entire time."

brendan @talking2mouth "How'd your day go, man?{w=0.5} You seem kinda down."

red @happy "Me? Nah, I'm fine.{w=0.33} Just a little tired. Still haven't found where to buy energy bars in this school."

may -happy @sadbrow happymouth "You've been tired a lot lately.{w=0.5} You should try and take it easy one of these days."

red @happy "Oh, believe me. I've been trying."

show brendan surprisedbrow frownmouth with dis:
    xpos 240+600
    ease 0.5 xpos 240+800
    
show may:
    xpos 240+900
    pause 0.2
    ease 0.5 xpos 240+1100
    
show leaf:
    xpos 240+200 alpha 0.0
    ease 0.7 xpos 240+400 alpha 1.0
    
leaf @talkingmouth "I'll bet you're tired.{w=0.5} I'm surprised you managed to crawl out of that situation in one piece."

show brendan -surprisedbrow -frownmouth -surprised with dis:
    xpos 240+800
    
show may:
    xpos 240+1100
    
show leaf:
    xpos 240+400 alpha 1.0
    
leaf @flirttalk "Seems like you just love getting into trouble."

red @closedbrow talkingmouth "Man, trouble seeks me out. And trouble has spiky, reddish-brown hair."

leaf @happy "Well, I know what'll cheer you up!{w=0.5} What are you guys doing for the weekend?"

brendan @closedbrow talkingmouth "Oh boy, let's see... got a ton of homework for both homeroom and my electives.{w=0.5}{nw}"

extend frownmouth @surprised " Get this, we need to read three chapters and write a three-page rep--"

leaf @happy "Well, {i}I{/i} was thinking that we can go to the fields outside of school to catch some wild Pokémon!"

red @closedbrow talking2mouth "Is that even allowed?"

leaf @talking2mouth "Yep! I asked around and all of the teachers gave me the okay."

leaf @closedbrow talkingmouth "Apparently, all the Pokémon in the fields were originally imported from other regions just for the students here!"

may @happymouth "Really? They just imported Pokémon from other regions?"
may @closedbrow talking2mouth "I hope they remembered to do their research on maintaining the native ecosystem..."

red @closedbrow talking2mouth "That is {i}really{/i} convenient.{w=0.5} I didn't even know importing Pokémon was a thing...{w=0.5} Or legal."

may @talkingmouth "We should invite Serena and the other guys, too.{w=0.5}{nw}"

extend @sadbrow happymouth " I bet they'd get pretty upset if they found out we forgot about them."

red @happy "Definitely. This sounds good to me!"

leaf @happy "Okay, so it's decided!{w=0.5}{nw}"

show brendan surprisedbrow frownmouth with dis

extend @flirttalk " Let's all meet up at the entrance first thing in the morning and catch some wild Pokémon!"

may @happybrow talkingmouth "Yay! I'll be looking forward to it!"

brendan sadbrow frownmouth @closedbrow talkingmouth "But...{w=0.5} my homework..."

redmind @happy "I should bring [pika_name] and [starter_name] with me, too.{w=0.5} Might be a good chance to see them in action against some wild Pokémon."
redmind @thinking "Speaking of which, everyone else is probably bringing their Pokémon, too.{w=0.5} Now, that'll be interesting to see..."
redmind @thinking "I should keep an eye on which Pokémon my friends might let me borrow for the upcoming Battle Team tryouts... oh, geez, I still need to tell everyone about that..."
redmind @happy "I mean, she basically invited me to apply! I guess she doesn't know about Lance's dogma. But she saw how he acted, and didn't seem to care about that, so..."

window hide

show blank2 with dis:
    alpha 1.0
    
$ renpy.music.stop(channel='crowd', fadeout=1.0)
stop music fadeout 2.5

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_44

$ renpy.pause(2.5, hard=True)

narrator "Your mind races, but you eventually manage to drift off into a deep, but excited, sleep."

jump day010410