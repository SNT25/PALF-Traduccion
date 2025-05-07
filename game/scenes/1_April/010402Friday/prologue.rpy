
label prologue:
    stop music

    scene blank2 

    Character("DISCLAIMER") "¡ATENCIÓN! Este juego está hecho por fans y no posee ninguna conexión con algún producto oficial de Pokémon." 
    Character("ADVERTENCIA DE CONTENIDO") "La historia contiene elementos maduros como abusos, agresión, asesinato y pobreza extrema. Adultos, niños y animales pueden sufrir lo mencionado anteriormente." 
    Character("DISCLAIMER") "Este juego no debe ser jugado por personas menores de edad en su país de residencia. Independientemente de la edad, se recomienda discreción al jugador."

    menu: 
        ">Lo entiendo y deseo jugar.":
            narrator "Perfecto, disfruta de tu aventura."

        ">No soy lo suficientemente mayor para jugar.":
            narrator "Esta bien, regresa cuando lo seas."

            $ MainMenu(confirm=False)()

    play music "audio/music/Dreams and Adventures.ogg"
    
    show pallet with dis:
        alpha 0.75
        
    show blank with dis:
        alpha 0.85
    
    pause 2.0

    show oak with dis

    oak @talkingmouth "¡Hola!{w=0.5} ¡Bienvenido al mundo de Pokémon!"
    oak @happy "Mi nombre es Oak. ¡Pero la gente me llama Profesor Pokémon!"
    oak @talkingmouth "¡Este mundo está habitado por criaturas llamadas Pokémon!{w=0.5} Para algunos, los Pokémon son mascotas. Pero otros los usan para pelear."
    oak @closedbrow talkingmouth "En cuanto a mí... Estudio a los Pokémon como profesión."
    oak @happy "Pero bueno, es suficiente de mí, háblame de ti."
    red "[ellipses]"
    oak @confusedbrow talkingmouth "Empecemos por tu nombre.{w=0.5} ¿Cómo te llamas?"

    label firstname:
        $ first_name = renpy.input("{color=#e70000}¿Cuál es tu nombre? (Presiona Enter para utilizar el predefinido){/color}", length=12, exclude="{}[[]%<>",)
        $ first_name = first_name.strip()

        if first_name == "":
            $ first_name = "Rojo"

        oak @talkingmouth "¡Muy bien! ¿Así que tu nombre es [first_name]?"

        menu:
            "Así es":
                red @happy "Ese soy yo."
                pass

            "Me confundi.":
                red @sadeyes sadeyebrows talkingmouth "Me confundi, pensaba que preguntabas por otra persona."
                oak @surprised "¿Ah? Entonces, ¿cual {i}es{i} tu nombre?"
                jump firstname

    oak @talkingmouth "Muy bien, ¿y como era tu apellido?"

    label lastname:
        $ last_name = renpy.input("{color=#e70000}¿Cuál es tu apellido? (Presiona Enter para utilizar el predefinido){/color}", length=20, exclude="{}[[]%<>",)
        $ last_name = last_name.strip()

        if last_name == "":
            $ last_name = "Sugimori"

        oak @happy "¡Muy bien! ¿Así que tu apellido es [last_name]?"

        menu:
            "Claro que sí.":
                red @happy "Por supuesto."
                pass

            "Dejame pensarmelo de nuevo.":
                red @sadeyes sadeyebrows talkingmouth "Se me fue de la mente, dejame pensarmelo de nuevo."
                oak @surprised "¿Eh? Esta bien."
                jump lastname

    oak @happy "¡Perfecto! Así que te llamas [first_name] [last_name]..."
    oak @surprised sweat "¡Ah! Ahora lo recuerdo. {w=0.5}{nw}" 
    extend @happy sweat "Eres el entrenador de este Pikachu."

    $ renpy.music.play("Audio/Pokemon/pikachu_norm1.ogg", channel="altcry")

    pikachu neutral_2 "¡Pi-KA-CHU!"

    oak @happy "Parece que te tiene bastante cariño...{w=0.5}{nw}"
    oak @sadeyes sadeyebrows talkingmouth "Parece que te tiene bastante cariño...{fast} Eh, ¿podrías recordarme su nombre?"

    label pikaname:
        $ pika_name = renpy.input("{color=#e70000}¿Cuál es el nombre de tu Pikachu?{/color}", length=12, exclude="{}[[]%<>",)
        $ pika_name = pika_name.strip()
        
        if pika_name == "" or pika_name == "pikachu":
            $ pika_name = "Pikachu"

        oak @talkingmouth "¿Su nombre es [pika_name]?"

        menu:
            "El único e inigualable.":
                red @happybrow talkingmouth "Así es, el único e inigualable, no hay otro como él."
                pass

            "¿Qué clase de nombre es ese?":
                red @angrybrow talking2mouth "¿Qué clase de nombre es ese? ¡Nunca había escuchado un nombre tan raro!"
                oak @surprised "¿Eh? Entonces, ¿cual es su {i}verdadero{/i} nombre entonces?"
                jump pikaname

    oak @happy "¡Es verdad! ¡Ahora lo recuerdo!{w=0.5} ¡Su nombre es [pika_name]!"

    oak @talkingmouth "Una última cosa. Esta es una historia que involucra a muchos adultos jóvenes, personas de tu misma edad, y bueno..."
    oak @sadbrow talkingmouth sweat "Para ser franco, vas a escuchar palabrotas. Sin embargo, tienes la opción de censurarlas si así lo deseas."
    oak @closedbrow talkingmouth "Por cierto, puedes cambiar esto en cualquier momento desde el menú de pausa al que accedes haciendo clic derecho."

    oak @talkingmouth "En cualquier caso, ¿te gustaría censurar las groserías de momento? {color=#ff0000}(Esta funcion todavía no es {i}100%%{/i} funcional.){/color}"

    menu:
        "No me *****, no.":
            $ profanity = True
            red @angry "No me jodas, no quiero."

        "Sí, por favor.":
            red @sadbrow happymouth "Sí, por favor."

    oak @happy "Muy bien."
    
    oak @talkingmouth "¡[first_name]!{w=0.5} ¡Tu propia leyenda Pokémon está a punto de comenzar!"

    oak @angrybrow talkingmouth "¡Un mundo de sueños y aventuras con los Pokémon te espera!"
    oak happy "¡Ahora es tiempo de que despiertes! ¡DESPIERTA!"

    hide oak with dis

    stop music fadeout 2.5
        
    show blank:
        alpha 0.85
        ease 2.0 alpha 1.0
        
    oak "¡Pikachuuuu~!"
    
    show pallet:
        alpha 0.75
        pause 2.5
        ease 2.5 alpha 1.0
    
    $ renpy.pause(2.5, hard=True)

    hide blank    
    show pallet with vpunch:
        alpha 1.0
    $ PlaySound("Body Roll.ogg")
    
    red casual hatless @surprised "¡AHHHHHHH!"

    $ renpy.music.queue("Audio/Music/Pallet Town A.ogg", channel='music', loop=True, fadein=1.0, tight=None)
    $ renpy.pause(1.25, hard=True)

    hide oak
    hide blank2
    hide blank
    
    red sadeyebrows closedeyes talking2mouth "{cps=*0.1}Aghh..."

    red angrybrow happymouth "¡Menos mal, casi me quedo dormido!"

    pause 1.5
    
    $ renpy.music.play("Audio/Pokemon/pikachu_question.ogg", channel="altcry", loop=None)
    pikachu neutral_4 "¿Pi-ka?"

    red -sadeyebrows -closedeyes -talking2mouth "¿Qué pasa [pika_name]?"

    $ renpy.music.play("Audio/Pokemon/pikachu_norm2.ogg", channel="altcry", loop=None)
    pikachu neutral_2b "¡Piiii-ka!"

    red -angrybrow -happymouth @happy "¡Es hora de levantarse y disfrutar de este lindo día!"

    $ renpy.music.play("Audio/Pokemon/pikachu_sad.ogg", channel="altcry", loop=None)
    pikachu bashful "Piiii{w=0.5}{nw}"
    extend bashful_2 "kaaaa."

    red talkingmouth "¡Vamos, levantarse temprano es algo bueno! El Pokémon de un futuro campeón {i}debería{/i} despertarse temprano y acostarse tarde."

    red talking2mouth angrybrow "Ya sabes lo que dicen: 'Irte a la cama tarde y despertarte temprano te hace...' {w=0.5}Uhmm...{w=0.5} {nw}"
    red -angrybrow happy "Ya sabes lo que dicen: 'Irte a la cama tarde y despertarte temprano te hace... Uhmm...{fast} ¡Estar cansado! !Todo el tiempo!'"

    $ renpy.music.play("Audio/Pokemon/pikachu_excite4.ogg", channel="altcry", loop=None)
    pikachu neutral_2b "¡Piii-kaaaa!"

    show mom:
        xpos 1.5

    mom "¿Acabo de escuchar a mi precioso bebecito decir la palabra 'cansado'?"

    show mom at moveinleft

    pause 1.0

    red frownmouth angryeyes confusedeyebrows @talking2mouth "Oh, hola mamá y bienvenida a mi habitación. ¡Por favor, pasa y siéntete como en tu casa!"

    mom @angry "¡Mientras sigas viviendo bajo mi techo, por supuesto que lo haré!"

    red closedeyes -confusedeyebrows happymouth "... Buen punto."

    mom @happymouth "Como sea, creí haberte oído decir 'cansado', y ni siquiera sabía que conocías esa palabra, cariño."

    red surprised "¿A qué te refieres con eso mamá?"

    mom @happy "... Bueno, cuando tienes más energía que tu Pikachu, una madre puede llegar a pensar que su hijo no duerme."

    red -surprisedbrow -frownmouth -surprised @happy sweat "No hay tiempo para dormir si pienso convertirme en campeón algún día."

    mom sadeyebrows sadeyes @talkingmouth "Me pregunto si [pika_name] estará de acuerdo contigo."

    pause 1.0

    $ renpy.music.play("Audio/Pokemon/pikachu_sad.ogg", channel="altcry", loop=None)

    pikachu yawn "{cps=*0.1}Pikaaaaaa..."

    pause 1.0

    red @closedeyes talking2mouth "... Bueno, cuando sea campeón, tendré más Pokémon además de [pika_name]."
    red @angrybrow happymouth "En fin, ¡estamos perdiendo el día! ¡Vamos, [pika_name], salgamos a correr antes de que el sol esté demasiado alto!"

    mom @surprised "¡Espera! Dios, ¡¿podrías quedarte quieto por un segundo?! ¡Tengo noticias muy pero que muy importantes!"

    red -angrybrow -happymouth @talkingmouth "Ya me estoy poniendo los tenis, pero dimelas."

    mom sadeyes sadeyebrows @talkingmouth "... ¿No te gustaría adivinar?"

    menu:
        "¿Vas a empezar a cobrarme renta?":
            show mom -sadeyes -sadeyebrows with dis

            red happy "¿Vas a empezar a cobrarme renta?"

            mom @sadeyes sadeyebrows happymouth "Aww, cariño, ni en sueños haría eso. Siempre serás bienvenido en casa, mi pequeño terron de azucar."

            red -happy @talkingmouth "Ya lo sé mamá. Pero, en serio, no me molestaría trabajar para contribuir al hogar también."
            
            red @closedeyes sadeyebrows talking2mouth "{size=30}O al menos conseguir una cama más grande...{/size}"
            
            mom @talkingmouth "Cariño, no necesitas preocuparte por eso todavía. ¡Acabas de graduarte de la preparatoria! Tendrás más tiempo para trabajar, pero ahora deberías estar disfrutando tu juventud."
            
            mom @happy "¡Además, esta noticia va a interferir con cualquier plan de trabajo que hayas tenido!"
           
            red @confused "¿Eh?"

            show mom happy:
                zoom 1.0 ypos 1.0
                ease 0.75 zoom 1.25 ypos 1.25
            
            pause 0.75
            
            mom "Mi precioso bebecito... ¡Estoy tan orgullosa de ti!"

            red @closedeyes lightblush talking2mouth "¿Me estás pellizcando las mejillas, mamá? Tengo dieciocho años, ¿sabías?"

            show mom -happy sadeyes sadeyebrows:
                zoom 1.25 ypos 1.25
                ease 0.75 zoom 1.0 ypos 1.0
            
            mom @sadbrow talkingmouth "Oh, lo sé... y pasó demasiado rápido para mi corazón."
            
            mom @happy "Pero basta de mis recuerdos más felices.{w=0.5} ¡Entraste a la Academia Kobukan!"
            
        "¿Otro video de un Skitty?":
            show mom surprisedbrow frownmouth with dis

            red @playfulbrow sweat talkingmouth "¿No será otro video de un Skitty? ¿No?"

            mom angrybrow frownmouth -surprisedbrow -frownmouth -surprised @surprised "¿Qué?{w=0.25} ¡No!{w=0.5} ¡Cariño, esto es mucho más importante que eso!"
            
            red -angrybrow happymouth "Entonces, ¿es un Lillipup?"
            
            mom @angry "¡Sí que tienes agallas!{w=0.5} No recuerdo haber criado a un hijo tan hablador."
                      
            mom -angrybrow -frownmouth @happy "Pero no, tampoco es eso. Cariño, ¡te aceptaron en la Academia Kobukan!"
        
        "Voy a salir a correr.":
            show mom -sadeyes -sadeyebrows with dis

            red @sadeyebrows closedeyes talkingmouth sweat "Oye, es viernes.{w=0.5} Si no te molesta, voy a aprovechar mi día libre y..."
            
            mom @happy "Buen intento, cariño."

            show mom happy:
                zoom 1.0 ypos 1.0
                ease 0.75 zoom 1.25 ypos 1.25
            
            pause 0.75
            
            mom "Mi precioso bebecito... ¡Estoy tan orgullosa de ti!"

            red @closedeyes lightblush talking2mouth "¿Me estás pellizcando las mejillas, mamá? Tengo dieciocho años, ¿sabías?"

            show mom -happy sadeyes sadeyebrows:
                zoom 1.25 ypos 1.25
                ease 0.75 zoom 1.0 ypos 1.0
            
            mom @sadbrow talkingmouth "Oh, lo sé... y pasó demasiado rápido para mi corazón."
            
            mom @happy "Pero basta de mis recuerdos más felices.{w=0.5} ¡Entraste a la Academia Kobukan!"

    stop music fadeout 2.0    

    pause 2.0

    red angrybrow sadmouth "... No, no lo hice."

    $ renpy.music.queue("Audio/Music/Littleroot_Start.ogg", channel='music', loop=False, fadein=1.0, tight=None)
    $ renpy.music.queue("Audio/Music/Littleroot_Loop.ogg", channel='music', loop=True, fadein=0.0, tight=None)

    mom sadeyebrows frownmouth @surprised "... ¿Qué?"

    red -angrybrow closedeyes sadeyebrows "No pude, mamá. Solo la tarifa de inscripción era de $10,000."

    red sadeyes "Además, mis calificaciones están en el décimo percentil más bajo para Kobukan. Y ni hablemos de mis inexistentes actividades extracurriculares. ¿Qué se puede hacer en Pueblo Paleta? Aparte de pasar el rato con Sam."

    red @talkingmouth "... Ni siquiera tuve la posibilidad postularme, mamá. Escribí tres cartas pidiendo una exención de la tarifa. Solo recibí respuesta en la tercera carta, y solo dijeron que dejara de molestarlos."

    mom @angry "¡Cariño! ¡Podríamos haber pagado la tarifa de inscripción!"

    red sad "No con mi suerte. Usé una de esas calculadoras en línea, ¿sabes? Dijo que mis oportunidades de ser aceptado eran tan bajas que ni siquiera la pudo calcular."

    red sadeyebrows closedeyes happymouth "Lo cual, al menos, tiene que ser algún tipo de récord."

    mom @sad "Oh... cariño, lo siento. Sé que entrar a Kobukan siempre fue un sueño para ti."

    red happy "No importa, ese solo era el camino más fácil para ser campeón. Encontraré otra manera."
    red happy "Despues de todo, ¡No puedo rendirme solo por una piedra en el camino!"

    pause 1.0

    stop music fadeout 1.0

    red confused "Ahora que lo pienso... ¿Por qué pensaste que entré a Kobukan?"

    $ renpy.music.queue("Audio/Music/Pallet Town A.ogg", channel='music', loop=True, fadein=1.0, tight=None)

    mom happy "Oh, es solo porque recibimos una carta que dice 'Carta de Aceptación de la Academia Kobukan' en el sobre."

    red -confused closedeyes talking2mouth "Vaya, eso suena muy sospechoso...{w=1.0}{nw}"
    red neutraleyes talking2mouth "Vaya, eso suena muy sospechoso... {fast}¿Puedo verla?"

    mom -happy @talkingmouth "Por supuesto, cariño."

    show letter at itemhover

    show mom:
        xcenter 0.5
        ease 1.0 xcenter 0.75
    
    $ PlaySound("item_get.ogg")

    red @confused "Oh, sí, aquí lo dice.{w=0.5} Vaya.{w=0.5} Esto es...{w=0.5} raro."
    red @sad2eyes angryeyebrows talking2mouth "Ya tengo una idea lo que pasó. Seguro que esto estaba destinado a {i}él{/i}, ¿verdad?"

    mom sadeyes sadeyebrows @talkingmouth "Tal vez. Pero, ¿por qué no simplemente la lees?"

    red happy "No voy a leer su correo, mamá. Eso es prácticamente un delito grave."

    mom @angry "Bueno, yo ya la leí. Y no querrás que vaya a prisión sola, ¿no?"

    red closedeyes @talkingmouth "Y así fue como la familia [last_name] inició su ascenso en el mundo del crimen..."

    show letter at itemhide
    show mom:
        ease 1.0 xcenter 0.5

    red -happy -closedeyes @talkingmouth "Muy bien, veamos qué dice esto."

    red @thinking "[ellipses]"
    show mom -sadeyebrows -sadeyes with dis

    show red:
        xpos -0.5

    show image "CG/Acceptance Letter.webp" with Dissolve(2.0)

    red @surprisedeyes frownmouth "[ellipses]"

    show mom happyeyes happyeyebrows with dis

    red @surprisedeyes frownmouth "[ellipses]"

    show mom happy with dis

    red @surprised "[ellipses]"

    pause 1.0

    red @surprised "Dios mío, mamá."

    mom @talkingmouth "Bueno, cariño. ¿Esta era, quizás, una carta destinada a nuestro encantador vecino?"

    mom @playfulbrow talkingmouth blush "¿O era, como dije, la prueba de que cosas buenas les pasan a las personas buenas?"

    red @surprisedeyes confusedeyebrows talking2mouth "... {w=1.0}¿Cómo es esto posible?"

    mom @closedbrow talking2mouth "Yo...{w=0.5} en realidad no lo sé. Nunca dudé que entrarías, pero si ni siquiera aplicaste, no estoy segura de que mi instinto maternal fuera {i}tan{/i} poderoso."

    red @surprised "[ellipses]"

    $ renpy.music.play("Audio/Pokemon/pikachu_confused.ogg", channel="altcry", loop=None)
    pikachu neutral_4 "¿Piiika?"

    red @surprised "... No tengo idea, [pika_name]. Simplemente, no tengo idea."

    show mom happybrow neutralmouth
    hide image "CG/Acceptance Letter.webp"
    hide red
    with Dissolve(1.0)

    pause 1.0

    red hatless casual @happy "¡Pero no voy a obligar a este caballo regalado beber el diente!"

    mom sadeyes sadeyebrows @talkingmouth "No creo que esa sea {i}exactamente{/i} la forma correcta de decirlo..."

    stop music fadeout 2.0
    show blank2 with splitfade
    
    $ renpy.pause(2.0, hard=True)
    
    hide pallet
    hide mom
    
    $ renpy.music.queue("Audio/Music/ViridianB_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
    $ renpy.music.queue("Audio/Music/ViridianB_Loop.ogg", channel='music', loop=True, tight=None)
    
    $ renpy.music.play("Audio/bigcrowdloop.ogg", channel='crowd', loop=True, fadein=0.5)
    
    scene airport behind blank2:
        xalign 1.0 yalign 1.0
    hide blank2 with splitfade
    
    pause 1.0

    redmind angrybrow frownmouth "La terminal del aeródromo de Kanto en Ciudad Verde...{w=0.5} y un boleto de solo ida a la región de Kobukan."
    red -angrybrow closedeyes @talkingmouth sweat"No puedo creer que haya pasado un mes entero y todavía no tengamos ni idea de cómo ingresé a Kobukan."
    red -closedeyes @confused "Definitivamente enviamos {i}varios{/i} correos electrónicos a la academia para asegurarnos de que no fuera un error, ¿verdad?"
    
    show mom with dis

    mom @talkingmouth "Por supuesto, cariño. Ambos lo hicimos."

    red @closedbrow talking2mouth "Así que ahora hay dos grandes preguntas. {w=0.5} ¿Cómo entré? {w=0.5}{nw}"
    extend @closedbrow sweat talkingmouth "¿Y cómo vamos a pagar esto?"
    
    mom @angry "Eso debería ser lo último de lo que te preocupes, cariño. {w=0.5}{nw}"
    extend @happy "¡Ya encontraremos una solución, no te preocupes!"

    red @thinking "[ellipses]"
    red @sadeyes sadeyebrows talkingmouth "Te creo, mamá. {w=0.5} Encontraremos una solución."
    red @happy "Y, oye, en el peor de los casos, obtengo seis meses de matrícula gratuita antes de que se den cuenta de que no podemos pagar, ¡Me expulsen y nos demanden por la colegiatura! Jaja..."
    mom @angryeyes angryeyebrows happymouth blush "¡Ni siquiera bromees con eso!"
    
    pause 2.0

    mom @sadeyebrows sadeyes talkingmouth "Hasta aquí puedo acompañarte, [first_name]."
    
    red @talkingmouth "Tengo dieciocho años, mamá. Estaré bien."
    
    mom @happy "Lo sé."
    mom @sadbrow talkingmouth "¿Un abrazo de despedida de mi querido campeón?"
    
    red @sad2eyes sadeyebrows lightblush talkingmouth "Cielos santos... voy a tener que esforzarme mucho para que la gente en Kobukan no se dé cuenta de que soy un gran niño de mamá."

    show mom happyeyes sadeyebrows -happymouth blush:
        zoom 1.0 ypos 1.0
        ease 0.75 zoom 1.25 ypos 1.25
    
    pause 2.5

    show mom -happy -blush:
        zoom 1.25 ypos 1.25
        ease 0.75 zoom 1.0 ypos 1.0
    
    red @talkingmouth sadbrow "Te quiero, mamá."
    mom tears sadbrow @talkingmouth "Yo también te quiero, cariño."
    
    $ renpy.music.play("Audio/Pokemon/pikachu_sad.ogg", channel="altcry", loop=None)
    pikachu sad_2 "Piiiikaaaa."

    mom sadeyes sadeyebrows @talkingmouth "Parece que [pika_name] también te quiere."
    
    red @happy "¡Hey, amiguito, no pongas esa cara! {w=0.5} Te enviaré a buscar apenas me lo permitan. Simplemente no me dejan traer a mis Pokémon personales de inmediato."
    red @talkingmouth "Hazle compañia a mamá mientras tanto, ¿sí?"
    red @happy "Ven aquí, te daré una de las famosas caricias en la cabeza de [first_name] para que aguantes hasta entonces."

    $ renpy.music.play("Audio/Pokemon/pikachu_sad2.ogg", channel="altcry", loop=None)
    pikachu @sad "Pika... piiiikaaaa."
    
    show mom -sadeyebrows -sad -talkingmouth with dis

    red @talkingmouth "Ya es hora, nos vemos mamá."
    
    mom @talkingmouth "¡Que tengas un buen viaje! {w=0.5} ¡Cuídate mucho!"

    show mom surprised:
        xpos 0.5
        ease 7.0 xpos 1.2
        
    show airport:
        xalign 1.0 yalign 1.0
        ease 8.0 xalign 0.0
        
    mom "¡Oh! ¡Y asegúrate de lavar tu ropa! {w=0.5} Y ve a dormir {size=34}más{/size}{size=32} temprano{/size} {size=30}para que{/size} {size=28}no termines{/size} {size=26}quedándote{/size} {size=24} dormido{/size}{size=22} todo el tiempo{/size} {size=20}!{/size}{size=18} Y come comidas completas,{/size}{size=16} ¡no solo barras energéticas...!{/size}"

    pause 1.0

    redmind sadeyes sadeyebrows "Parece que ya está empezando a sentir el síndrome del nido vacío..."

    pause 1.0

    redmind sad "Y a eso tengo que agregarle que [pika_name] parece realmente triste... Tendrá que ser fuerte hasta que pueda enviarlo a la academia."

    stop music fadeout 2.0
    pause 2.5
    
    show airport:
        xalign 0.0 yalign 1.0
        ease 4.0 xalign 1.0

    show mom -surprisedbrow -frownmouth -surprised:
        xpos 1.2
        ease 4.0 xpos 0.5
    
    $ renpy.pause(4.5, hard=True)
    
    show airport:
        xalign 1.0
    
    $ renpy.music.play("Audio/Pokemon/pikachu_sad2.ogg", channel="altcry", loop=None)
    pikachu sad_2 "Pika... piiiikaaaa."
        
    mom -tears @talkingmouth "No te preocupes, [pika_name], ¡estarás con él antes de lo que crees! {w=0.5}{nw}"
    extend angryeyes angryeyebrows @talkingmouth "Aunque sería mucho más fácil subirte al avión si te quedaras en tu Poké Ball..."
    
    $ renpy.music.play("Audio/Pokemon/pikachu_sad.ogg", channel="altcry", loop=None)
    pikachu sad "Piiiikaaaa."

    mom -angryeyes -angryeyebrows -talkingmouth @happy "Oh, sé cómo te sientes, de verdad lo sé. {w=0.5} Pero es mejor no quedarse atrapado en estos sentimientos."
    mom happyeyes talkingmouth -tears @talkingmouth "Todos los hijos dejan su hogar algún día. ¡Lo vi en un programa de televisión!"
    mom -happyeyes @talkingmouth "Vamos, es hora de ir a casa."

    hide mom with dis
    
    $ PlaySound("plane_chime.ogg")
    
    Character("Altavoz") "{color=#e70000}Este es el anuncio de preembarque para el vuelo de las 7:45 AM con destino a Ciudad Inspira. El despegue será en 45 minutos.{/color}"
    Character("Altavoz") "{color=#e70000}Solicitamos ahora el abordaje de pasajeros con niños pequeños y Pokémon. El abordaje general comenzará en quince minutos.{/color}"
    
    pikachu neutral_3 "[ellipses]"
    
    $ renpy.music.play("Audio/Pokemon/pikachu_angry1.ogg", channel="altcry", loop=None)
    pikachu angry_2 "¡Pi-ka!"
    $ renpy.music.stop(channel='crowd', fadeout=1.0)
    
    $ renpy.music.queue("Audio/Music/SoaringDreams_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
    $ renpy.music.queue("Audio/Music/SoaringDreams_Loop.ogg", channel='music', loop=True, tight=None)
    
    hide mom
    
    show sky:
        alpha 0.0 yalign 1.0 xalign 0.2 zoom 1.25
        parallel:
            ease 1.0 alpha 1.0
        parallel:
            ease 30.0 xalign 1.0
    
    show clouds1 as base1:
        xpos -200 ypos 100 alpha 0.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 12.0 xpos 2000
            parallel:
                pause 11.0
                linear 1.0 alpha 0.0
    show clouds2 as base2:
        xpos -800 ypos 400 alpha 0.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 8.0 xpos 1000
            parallel:
                pause 7.0
                linear 1.0 alpha 0.0
    show clouds3 as base3:
        xpos -400 ypos 0 alpha 0.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 10.0 xpos 2200
            parallel:
                pause 9.0
                linear 1.0 alpha 0.0
    
    show clouds1 as set1:
        xpos -1800 ypos 100 alpha 0.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 15.0 xpos 1800
            parallel:
                pause 14.0
                linear 1.0 alpha 0.0
                pause 1.0
                xpos -1500
            repeat
    show clouds2 as set2:
        xpos -1700 ypos 100 alpha 0.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 12.0 xpos 2200
            parallel:
                pause 11.0
                linear 1.0 alpha 0.0
                pause 1.0
                xpos -1400
            repeat
    show clouds3 as set3:
        xpos -2100 ypos 0 alpha 0.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 17.0 xpos 2200
            parallel:
                pause 16.0
                linear 1.0 alpha 0.0
                pause 1.0
                xpos -1800
            repeat
    show clouds1 as set4:
        xpos -1700 ypos -100 alpha 0.0
        pause 5.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 6.0 xpos 1800
            parallel:
                pause 5.0
                linear 1.0 alpha 0.0
                pause 1.0
                xpos -1400
            repeat
    show clouds2 as set5:
        xpos -1900 ypos 500 alpha 0.0
        pause 6.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 8.0 xpos 2200
            parallel:
                pause 7.0
                linear 1.0 alpha 0.0
                pause 1.0
                xpos -1700
            repeat
    show clouds3 as set6:
        xpos -2100 ypos -50 alpha 0.0
        pause 5.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 20.0 xpos 2200
            parallel:
                pause 19.0
                linear 1.0 alpha 0.0
                pause 1.0
                xpos -1900
            repeat
    show clouds2 as set7:
        xpos -1900 ypos 200 alpha 0.0
        pause 4.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 10.0 xpos 2200
            parallel:
                pause 9.0
                linear 1.0 alpha 0.0
                pause 1.0
                xpos -1700
            repeat
    
    $ renpy.pause(1.5, hard=True)
    
    hide airport
    
    redmind -sadeyebrows closedeyes frownmouth "¡Guau!"
    redmind "¿Es cierto que la gente de la ciudad siempre usa aviones para ir a todos lados?{w=0.5} Esto no se parece en nada a volar un Pokémon.{w=0.5}"
    redmind happymouth "Aunque, no es algo que haya hecho...{w=0.5} todavía."
    redmind -happymouth -closedeyes -frownmouth "Algunos de los mayores de Pueblo Paleta me dijeron que la región Kobukan está justo al lado de Unova... pero bastante lejos de Kanto."
    redmind confusedeyebrows frownmouth "Si Kobukan está tan lejos, no quiero imaginar lo lejos que estarán Kalos o Paldea."
    redmind closedeyes frownmouth "... Ugh. Llevo aquí diez horas...{w=0.5}{nw}" 
    redmind surprised "... Ugh. Llevo aquí diez horas... {fast}¡Espera!{w=0.5} ¿Qué es eso por la ventana?"

    $ PlaySound("plane_chime.ogg")

    "Altavoz" "{color=#e70000}Buenas tardes, pasajeros. Al habla el capitán. Esperamos aterrizar en la región Kobukan en aproximadamente veinte minutos. El clima en la Ciudad Inspira es claro y soleado.{/color}" 
    "Altavoz" "{color=#e70000}Mientras comenzamos nuestro descenso, por favor asegúrese de que su cinturón de seguridad esté correctamente abrochado, su mesa de apoyo esté en la posición vertical y todos los dispositivos electrónicos apagados.{/color}"
    "Altavoz" "{color=#e70000}¡Muchas gracias por volar con nosotros y les deseamos una feliz estadía en la regíon!{/color}"

    red happy "¡Aquí vamos!{w=0.5} ¡Este es el inicio de un nuevo capítulo!"
    
    show blank2 with Dissolve(1.0)
        
    $ PlaySound("Airplane.ogg")
    
    $ renpy.pause(2.0, hard=True)
    
    hide clouds1 as base1
    hide clouds2 as base2
    hide clouds3 as base3
    hide clouds1 as set1
    hide clouds2 as set2
    hide clouds3 as set3
    hide clouds1 as set4
    hide clouds2 as set5
    hide clouds3 as set6
    hide clouds2 as set7    
    
    stop music fadeout 2.0
    $ renpy.pause(2.5, hard=True)
    
    $ renpy.music.play("Audio/cityambience.ogg", channel='crowd', loop=True, fadein=1.5)
    
    $ renpy.pause(1.5, hard=True)
    
    scene city_A with Dissolve(2.0)
        
    $ renpy.pause(1.5, hard=True)
    
    hide sky
    hide blank2
    
    redmind closedeyes frownmouth "... Excepto que no tengo ni idea de dónde estoy ni en qué dirección queda la academia."
    redmind happymouth "Si recuerdo bien lo que vi en internet, debería haber un autobús que lleva hasta allí, no? El de la Línea Roja."
    redmind angrybrow frownmouth "El problema es...{w=0.5} veo la Línea Escarlata, la Línea Rubí, incluso la Línea Perla. Todas son más o menos...{w=0.5} rojas."
    red -angrybrow happy "Bueno, si elijo una dirección y empiezo a correr, seguro que me topo con algo que me indique el camino correcto."

    show pallet at sepia
    show flashback
    with dis

    $ renpy.pause(1.0, hard=True)
    
    show mom angry at sepia, dissolvein behind flashback

    mom "¡Por el amor de Arceus, detente y fíjate en tu entorno! Si te pierdes, simplemente pregunta a alguien por direcciones."

    show blank with splitfade

    hide mom
    hide pallet
    hide flashback
    hide blank with dis

    red @talkingmouth "Sí, supongo que podría hacer eso."

    pause 1.5

    red talkingmouth "¡Oiga! Disculpe.{w=0.5} ¿Sabe qué autobús va a...?"
    
    "{color=#3110dd}Voz familiar" "\"¿Eh?\""

    show blue surprisedbrow frownmouth sweat with dis

    red surprised "¿Qué de-"

    show blue -surprisedbrow -frownmouth -surprised closedbrow frownmouth with dis
    
    pause 1.0
    
    blue "[ellipses]"
    
    play music "Audio/Music/RivalTune.ogg" noloop
    blue -sweat -frownmouth @happymouth "... No puede ser."

    red -surprisedbrow -frownmouth -surprised angrybrow talking2mouth "... Blue."
    
    queue music "audio/music/Inspira_start.ogg" noloop
    queue music "audio/music/Inspira_loop.ogg"

    blue -happymouth -closedbrow @surprised "¿¡Qué demonios haces {i}tú{/i} aquí!?"
    
    red @closedbrow talking2mouth "¿Tan difícil es creer que entré a la Academia Kobukan?"
    
    blue @happy "No, ¡me lo creo totalmente! Así como también puedo creer que eres la Reina de Kalos o que en el techo dice 'ingenuo'."
    
    red -angrybrow @confused "Pero, ¿no estamos al aire libre...?"
    
    show blue surprisedbrow frownmouth with dis

    pause 1.5

    blue -surprisedbrow -frownmouth -surprised @happy "Casi desearía que de {i}verdad{/i} hubieras entrado a Kobukan. Voy a extrañar a mi bufón favorito cuando esté tomando mi lugar entre los futuros Campeones del mundo."
    
    red -surprisedeyes -surprisedeyebrows -frownmouth @playfulbrow talkingmouth "Entonces estarás {i}muy{/i} feliz cuando me veas caminando por los mismos pasillos que tú."
    
    blue -happy @surprised sweat "Tú...{w=0.5} casi suenas como si hablaras en serio."
    
    red @happy "Hay dos cosas que me tomo en serio, Blue. Mi sueño de ser campeón Pokémon, y nuestra rivalidad."
    
    blue -surprisedbrow -frownmouth -surprised -sweat @angry "¡No seas tan arrogante! Yo no te tomo en serio en lo absoluto. Eres un soñador sin rumbo."
    blue -angry @closedbrow talkingmouth "Yo sé exactamente a dónde voy, y cómo voy a llegar allí."

    red -happy @frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    red @talkingmouth "Oye, Blue. Ya que, obviamente, yo no voy a la Academia Kobukan y tú sí, eso significa que nadie en tu nueva academia se enterará de tu apodo, ¿cierto?"

    blue frownmouth @angrybrow talkingmouth "Ni se te ocurra."

    red @talking2mouth "¿Ese apodo con el que todos te llamaban? El que inventé cuando tenía, ¿qué?, ¿ocho años? Y que se te quedó pegado todo este tiempo..."

    blue -frownmouth angry "¡Te estoy advirtiendo!"

    red -talking2mouth @happy "No me acuerdo bien... ¿Me ayudas a recordarlo?"

    label bluename:
        $ blue_name = renpy.input("{color=#e70000}¿Cual era el apodo de Blue? (Presiona Enter para utilizar el predefinido){/color}", length=12, exclude="{}[[]%<>",)
        $ blue_name = blue_name.strip()

        if blue_name == "" or blue_name == "Blue" or blue_name == "Blue":
            $ blue_name = "Blueito"

        red @happy "Oh, creo que ya casi lo tengo. ¿Era...{w=0.5} [blue_name]?"

        menu:
            "Sí, así era.":
                red happyeyes talkingmouth "Ya me acorde, era ¡[blue_name]!"
                pass

            "Hay uno mejor.":
                red happyeyes talkingmouth "Oh, espera, tengo uno aún mejor."
                jump bluename

    blue @angry "¡No tiene sentido! No es ingenioso, ni pegadizo, ni...{w=0.5} ¡Era tan estúpido! ¡¿Por qué todos me llamaban así?!"

    red -happyeyes -happyeyebrows -talkingmouth @talkingmouth "Supongo que el humor es demasiado sofisticado para ti, [blue_name]."

    blue @closedbrow happymouth "No reconocerías lo que es 'sofisticado' ni aunque te lo embarraran en la cara."
    blue @angry "Eres un simple pueblerino que vio a un campeón en la tele un día y se engañó a sí mismo pensando que tenía una oportunidad para volverse uno."
    blue @angry "Ahora, tengo cosas {i}mucho{/i} más importantes que hacer que perder el tiempo con un payaso como tú, así que me largo."
    blue -angry @surprisedbrow happymouth "¡Bueno, me piro, vampiro!"

    show blue:
        parallel:
            ease 0.5 alpha 0.0
        parallel:
            ease 0.75 xpos 1.3

    pause 1.5

    redmind @thonk "¿Pueblerino? Pero si venimos del mismo pueblo..."
    
    show city_A:
        zoom 1.0 xalign 0.5 yalign 1.0
        block:
            ease 0.5 zoom 1.1 yalign 1.0 xalign 1.0
            pause 0.5
            ease 0.5 xalign 0.0
            pause 0.5
            ease 0.4 xalign 0.5
            
    redmind -surprisedbrow -frownmouth -surprised "Como sea, necesito encontrar a alguien que pueda indicarme el camino a la academia."
    redmind closedeyes frownmouth "Tal vez alguien a quien {i}no{/i} conozca esta vez..."
    
    show city_A:
        zoom 1.1 xalign 0.5 yalign 1.0
        ease 0.5 zoom 1.0
    
    pause 0.5
    
    show silver neutral with dis:
        xpos 1.3
        ease 1.0 xpos 0.5
    
    pause 2.0
    
    hide blue
    
    redmind @playfulbrow unamusedmouth "... Hmm. No creo haber visto antes a alguien cuya cara diga, de forma más obvia, 'no me hables'."
    redmind happy "Bueno, seguro que puedo encontrar a alguien sin ese aura de antisocial si simplemente..."

    silver @talkingmouth "Oye, rojo."

    red surprised "¿Quién? ¿Yo?"

    silver angrybrow "¿Qué, eres tonto o qué? ¡Te estoy mirando {i}directo{/i} a los ojos!"
    
    redmind @winkeyes sadeyebrows sweat frownmouth "Oh, mierda, ¿este tipo está buscando pelea?" 
    redmind @thinking "... Pero no tengo ningún Pokémon conmigo. Lo mejor sería irme."

    red @sad2eyes talking2mouth "Eh... Creo que debería irme."
    
    silver sad "¡E-espera! Yo, eh... Solo quería..."

    pause 1.5

    silver closedbrow "Mejor olvídalo."

    redmind @confusedeyebrows frownmouth "¿O tal vez solo es un poco torpe para hablar?"

    red @happy "Eh, quizás empezamos con el pie izquierdo. ¿Por qué no me cuentas qué pasa?"

    pause 1.5

    silver -closedbrow @sad "... Ugh. Solo quería decir que... eh... escuché tu conversación..."

    red @talking2mouth angrybrow "No es un {i}gran{/i} comienzo, pero sigue."

    silver @closedbrow talkingmouth "Y pensé que... bueno, si realmente entraste a Kobukan... y como estabas mirando... probablemente intentabas encontrar el camino allí."

    red @happy "¡Eres bastante perspicaz!"

    silver @sadbrow happymouth "Gracias, es mi mecanismo de supervivencia."
    silver @talkingmouth "De todas formas, ¿estoy en lo correcto? {w=0.5} Quiero decir, ¿estás intentando llegar a Kobukan?"

    red @talkingmouth "Sí. Si pudieras indicarme el camino, me sería de gran ayuda."

    silver @closedbrow talkingmouth "Bien. Eso es lo que quiero. {w=0.5}{nw}"
    extend @surprisedbrow talkingmouth "Ser útil, quiero decir."

    pause 1.5

    red @talking2mouth "Entonces..."

    silver @closedbrow talkingmouth "Por allí."

    red happy "¡Gracias! ¿Está muy lejos de aquí si voy a pie?"

    silver @surprisedbrow talkingmouth "Quiero decir...{w=0.5} Yo no lo haría, pero probablemente sí."

    red @happy "Genial. ¡Nos vemos!"

    show silver:
        xpos 0.5
        ease 3.0 xpos 0.0
        
    show city_A:
        ease 3.0 zoom 2.0

    pause 3.0

    silver @surprised "Hey, ¡espera un segundo!"
    show city_A:
        linear 1.0 zoom 1.0

    show silver:
        linear 1.0 xpos 0.5

    red @talkingmouth "¿Sí? ¿Qué pasa?"

    silver @closedbrow talkingmouth "Sobre lo de antes...{w=0.5} Lo siento. Es que, eh,{w=0.25} ha sido un día bastante difícil hasta ahora."
        
    red @confused "Pero si apenas ha pasado el mediodía, ¿no?"

    silver @surprisedbrow talkingmouth "Eh..."
    
    red @happy "No te preocupes, todos tenemos esos días."
    
    silver @closedbrow talkingmouth "Hmm... {w=0.5}{nw}"
    extend @happy "¡Ah, ya sé!"
    silver @happymouth "Toma, esto."
    
    show ragecandy at itemhover

    show silver:
        xcenter 0.5
        ease 1.0 xcenter 0.75
    
    $ renpy.music.set_volume(0.25, delay=0.0, channel="music")
    $ PlaySound("item_get.ogg")
    $ renpy.music.set_volume(1.0, delay=2.0, channel="music")
    
    pause 2.0

    red surprised "¿Una barra de chocolate?"
        
    silver sadbrow @talkingmouth "Es una barra Furía...{w=0.5} Son de Johto."
    
    red @talkingmouth "Ya veo."

    show ragecandy at itemhide

    show silver:
        xcenter 0.75
        ease 1.0 xcenter 0.5

    pause 1.0

    red happy "Bueno, mi madre siempre me dijo que no aceptara dulces de extraños. Así que, mi nombre es [first_name]. ¿Y el tuyo?"

    $ BecomeNamed("Silver")

    silver @talkingmouth "Oh. Eh, es Silver."

    red -happy @talkingmouth "Genial. Nos vemos entonces."

    show silver closedbrow with dis:
        xpos 0.5
        ease 3.0 xpos 0.0
        
    show city_A:
        ease 3.0 zoom 2.0

    pause 3.0

    $ renpy.music.queue("Audio/Bus arrive1.ogg", channel='misc', loop=None, tight=None)
    $ renpy.music.queue("Audio/Bus arrive2.ogg", channel='misc', loop=True, tight=None)
    
    pause 2.0
    
    silver neutralbrow @talkingmouth "... Si te interesa, ese autobús va directamente allí."

    show city_A:
        linear 0.5 zoom 1.0

    show silver:
        linear 0.5 xpos 0.5

    red angryeyebrows angryeyes frownmouth @talkingmouth "Hombre...{w=0.25} Parece que nunca voy a poder salir a correr, ¿verdad?" 
    red happy "Ni modo...{w=0.25} Está bien, subiré al autobús."
    
    silver surprisedbrow @talkingmouth "Siento que me falta algo de contexto..."
    
    red @talkingmouth "La vida es más sabrosa sin él. ¡Nos vemos, rojo!"

    $ renpy.music.set_volume(0.25, delay=0.5, channel="music")
    $ renpy.music.stop(channel='misc', fadeout=1.5)
    
    show blank2 with splitfade
    $ renpy.music.play("Audio/Bus_stop.ogg", channel='misc', loop=None, fadein=0.0)
    
    $ renpy.pause(2.0, hard=True)
    
    show text "{color=#ffffff}.{/color}" as text1:
        alpha 1.0
        pause 0.5
        linear 0.0 alpha 0.0
    show text "{color=#ffffff}..{/color}" as text2:
        alpha 0.0
        pause 0.5
        block:
            linear 0.0 alpha 1.0
            pause 0.5
            linear 0.0 alpha 0.0
    show text "{color=#ffffff}...{/color}" as text3:
        alpha 0.0
        pause 1.0
        block:
            linear 0.0 alpha 1.0
            pause 1.5
            linear 1.0 alpha 0.0
    $ renpy.pause(4.0, hard=True)
    
    hide city_A
    show city_B behind blank2
    
    hide text
    hide text1
    hide text2
    hide text3
    
    $ renpy.music.set_volume(1.0, delay=1.0, channel="music")
    $ renpy.music.play("Audio/bigcrowdloop.ogg", channel='crowd2', loop=True, fadein=0.5)
    
    hide blank2 with splitfade
    
    $ renpy.pause(1.5, hard=True)
    
    red @surprised "¡Guau!"

    redmind @thinking "¡Este lugar muy pero que muy grande! Vi muchas veces fotos de Ciudad Inspira cuando investigaba sobre Kobukan, pero..."
    redmind @upeyes sweat frownmouth "Uff. Solo mirar los rascacielos me da vértigo, tengo que inclinar mucho el cuello para verlos."

    red happy "Hey, ¡se puede ver la academia desde aquí! Muy bien, ahora, si solo me ajusto bien los cordones, por fin podré-"

    show city_B with hpunch
    
    Character("Hombre grosero") "\"¿Podrías {i}moverte{/i}, tal vez? ¡Hay gente caminando por aquí!, ¡¿sabes?!\""

    red @surprised "Eh... ¿p-perdón? ¡Perdón!"

    redmind @closedeyes frownmouth "Espera, ¡eso fue totalmente culpa de él! ¿Por qué me disculpé?"

    show brawly uniform:
        xcenter 1.5
        ease 0.5 xcenter 0.5

    brawly happy @angrybrow happymouth "¡Bro! No puedes dejar que tipos como ese te pasen por encima. ¡Tienes que plantar cara a esta clase de idiotas y ponerlos en su lugar!"
    brawly @closedbrow talking2mouth -happy "¡Ten más confianza en ti mismo! No necesitas a nadie que te respalde."
 
    red surprised "... Uh, ¿hola?"
    red -surprisedbrow -frownmouth -surprised @talking2mouth "Aprecio el apoyo, pero... ¿quién eres?"

    $ BecomeNamed("Brawly")

    brawly -happy @happy "¡Brawly!"

    redmind closedeyes frownmouth "Sí, eso me cuadra."
    red surprised "¡Oye! Ese uniforme... Eres estudiante de Kobukan, ¿no?"
    brawly @surprised "¡Oh, sí! De hecho, soy miembro del consejo estudiantil. ¿Eres un estudiante nuevo?"
    red -surprisedbrow -frownmouth -surprised @talkingmouth "Sí. Me llamo [first_name]. Justo ahora estoy yendo a la academia."
    brawly @talkingmouth "¡Pues un gusto, [first_name]! En realidad, llego un poco tarde a una orientación que dirige la presidenta del Consejo, así que tengo que correr. ¿Te apuntas a una carrera?"
    red surprised "{w=0.5}.{w=0.5}.{w=0.5}."
    red happy "Creo que nos vamos a llevar muy bien. Sí, guía el camino, Brawly."

    show blank2:
        alpha 0.0
        ease 2.0 alpha 1.0
    
    $ renpy.music.stop(channel='crowd', fadeout=1.5)
    $ renpy.music.stop(channel='crowd2', fadeout=1.5)
    
    $ renpy.pause(4.0, hard=True)
    
    show relichall_A:
        alpha 0.0
        ease 2.0 alpha 1.0
    
    $ renpy.pause(2.5, hard=True)

    hide brawly
    
    hide blank2

    show brawly uniform:
        xcenter 1.5 xzoom -1
        ease 0.5 xcenter 0.5

    brawly @surprisedbrow happymouth "¡Sí que eres bastante rápido! ¿Seguro que nunca entrenaste?"
    red closedeyes @talking2mouth "Solo salía a correr un poco cada día. Nunca tuve la oportunidad de hacer más. En mi bachillerato en Pueblo Paleta, lo más parecido a un equipo deportivo que teníamos era el club de bingo de los ancianos."
    brawly @happy "Entonces tal vez sea un talento natural. ¡En fin, ya llegamos!"
    
    hide city_B
    
    show relichall_A:
        subpixel True
        zoom 1.0 xpos 0.0 ypos 0.0 alpha 1.0
        ease 6.0 zoom 1.14 xpos -0.14 ypos -0.04
    
    red surprised "... Maldición. Este lugar es bellísimo."
     
    red closedeyes happymouth happyeyebrows "De acuerdo, tengo que calmarme." 
    red -closedeyes -happymouth -happyeyebrows @talkingmouth "Dijiste que hay una especie de orientación primero, ¿verdad, Brawly?"
    brawly @happy "Sí, eso es-"

    show relichall_A with vpunch

    roxanne uniform @angry "{size=50}{b}¡BRAWLY!{/b}{/size}"
    brawly @closedbrow talking2mouth "... Sí, esa es la cosa para la que llego tarde."
    
    show roxanne uniform:
        xcenter -0.5 xzoom -1
        ease 1.0 xcenter 0.33

    show brawly:
        xcenter 0.5
        ease 1.0 xcenter 0.66

    roxanne @angrybrow talking2mouth "Brawly, ¿estuviste corriendo otra vez con el uniforme?"
    brawly @sadbrow happymouth "¡Sip! Lo siento, Prez."
    roxanne @happybrow talkingmouth "Oh, cariño, lo sentirás. {i}Vaya si lo sentirás.{/i}"
    brawly @sadbrow happymouth "Eh je je... Ya lo estoy sintiendo."
    
    show roxanne:
        xcenter 0.33
        ease 0.75 zoom 1.25 xcenter 0.33 ypos 1.1

    roxanne @talkingmouth "Y bien, ¿quién es este?"
    red @talkingmouth "[first_name], señora."

    menu: 
        ">Encubrir a Brawly":
            show brawly happy with dis
            red @talkingmouth "Soy un estudiante nuevo. Estaba un poco perdido, así que Brawly me ayudó a encontrar el camino."
            $ AddEvent("Brawly", "Covered")

            show roxanne:
                zoom 1.25 xcenter 0.33 ypos 1.1
                ease 0.5 xzoom -1 xcenter 0.33 ypos 1.1 

            roxanne @happy "¿De verdad? Qué maravilloso es saber que te tomas en serio tus responsabilidades en el consejo estudiantil.{w=1.0} Por una vez."

            show roxanne:
                xzoom -1 xcenter 0.33 ypos 1.1 
                ease 0.75 xzoom 1 xcenter 0.33 ypos 1.1

            roxanne @talkingmouth "Pero, ¿dónde están mis modales? Por favor, permíteme presentarme."

        ">Dejarlo pasar":
            red @talkingmouth "Un placer conocerla."
            roxanne @talkingmouth "El placer es todo mío, estoy segura."

    $ BecomeNamed("Roxanne")
    roxanne @closedbrow talkingmouth "Mi nombre es Roxanne, Presidenta del consejo estudiantil de la Academia Kobukan. Por favor, si alguna vez necesitas algo, ten en cuenta que nosotros, el consejo estudiantil, estamos aquí para ayudarte."
    roxanne @happybrow sweat talking2mouth "... Excepto ahora mismo, porque llegamos muy tarde a la orientación que tenemos que preparar. Por favor, discúlpannos."

    red surprised "¿Eh? Ah, sí, claro."

    brawly @happy "¡Nos vemos, [first_name]! Puedes relajarte hasta que anunciemos la orientación por los altavoces. Puedes ir a los dormitorios y eligir una habitación."

    show brawly:
        ease 1.0 xcenter -0.5

    show roxanne:
        zoom 1.25 ypos 1.1
        ease 1.0 xcenter -0.5

    red -surprisedbrow -frownmouth -surprised @talkingmouth "¿Dormitorios? Supongo que debería ir a echar un vistazo."

    show relichall_A:
        ease 3.0 zoom 1.3

    pause 3.0

    show mace:
        alpha 0.0 xpos 0
        parallel:
            ease 0.5 alpha 1.0
        parallel:
            ease 1.75 xpos 0.66

    show face:
        alpha 0.0 xpos 0
        pause 0.25
        parallel:
            ease 0.5 alpha 1.0
        parallel:
            ease 1.5 xpos 0.33    
    
    mace @talkingmouth "Oh, ¿eres acaso un estudiante de ingreso?"
    
    show relichall_A:
        zoom 1.3
        ease 1.0 zoom 1.14 xpos -0.1 ypos -0.1
    
    red @talkingmouth "Eh, sí. ¿Pasa algo?"

    show face smile2mouth happyeyebrows with dis

    mace smilemouth happybrow @happy "¡Maravilloso! Nosotros también. Un placer conocerte."
    
    face @happy "Estábamos esperando que supieras algo sobre la orientación que viene. Sabemos que la {i}hay{/i}, pero no tenemos idea de dónde se llevara a cabo."

    show face surprisedbrow frownmouth
    show mace surprisedbrow frownmouth
    with dis

    red @happy "Oh, sí, estaba charlando con un miembro del consejo estudiantil sobre eso. Me dijo que simplemente elija una habitación del dormitorio, y luego anunciarían la reunión por los altavoces."
    
    show face surprisedbrow with dis
    
    mace surprisedbrow @surprisedbrow talkingmouth "¿Ya has captado la atención de un miembro del consejo estudiantil? Impresionante. ¿Debemos asumir que cuentas con ciertos contactos?"
    
    red -happy @sweat talkingmouth "No exactamente. Lo conocí hace media hora en Ciudad Inspira. No conozco a {i}nadie{/i} aquí, salvo a otro estudiante ingresante, en realidad."

    face -surprisedbrow -frownmouth -surprised smile2mouth sadbrow @happy "¿De verdad, no tienes ninguna conexión? Es tan, tan difícil llegar aquí... ¿cómo lo lograste?"
    
    mace @closedbrow talkingmouth "¿Sería demasiado atrevido asumir que vienes de una familia {i}acomodada{/i}?"
    
    show face sad
    show mace sad
    with dis
    
    red @happy "Jajaja, ¡ojalá! No, en realidad, vivía en una casa pequeña en Pueblo Paleta."
    
    mace @sweat sadbrow sadmouth "... Entonces, ¿quizás vienes de una familia con un prominente {i}legado{/i}?"
    
    red -happy @talkingmouth "En realidad, soy la primera persona de mi familia que va a la universidad."
    
    face @angry "¡Entonces tus calificaciones deben haber sido {i}impecables{/i}! Promedio perfecto en todas las materias y el primero de tu clase, ¿no?"
    
    red @closedeyes sadmouth "No vas a creer esto, pero en mi bachillerato las notas eran aprobado o desaprobado. Así que, en cierto modo, éramos pocos y todos aprobamos, así que en cierto modo fui el primero de la clase."
    red @happy sweat "Peeero...{w=0.5} probablemente fui el último de ese grupo."
    
    mace angry -sweat "[ellipses]"
    
    face @closedbrow frownmouth "[ellipses]"
    
    show face sad with dis
    
    mace @sad "Mil disculpas. Debemos atender ciertos asuntos...{w=0.5} en otra parte."

    show mace sad:
        alpha 1.0 xpos 0.66
        parallel:
            pause 0.25
            ease 0.5 alpha 0.0
        parallel:
            ease 1.0 xpos 1.0

    show face sad:
        alpha 1.0 xpos 0.33
        parallel:
            pause 0.5
            ease 0.5 alpha 0.0
        parallel:
            ease 1.0 xpos 1.0
    
    pause 2.0

    stop music fadeout 3.5
    
    redmind sad "Sí...{w=0.5} Tiene sentido...{w=0.5} Quiero decir, desde su perspectiva, y hasta la mía, no hay forma de que debería estar aquí."
    red @thinking "[ellipses]"
    redmind angrybrow frownmouth "Pero estoy aquí. Y haré lo que sea necesario para demostrarle a todos, y a mí mismo, que merezco esta oportunidad."

    queue music "Audio/Music/Show Me Around.ogg"
    
    show relichall_A:
        subpixel True
        zoom 1.14 xpos -0.1 ypos -0.1
        ease 3.0 zoom 1.25 ypos -200 xpos -320
    
    $ renpy.pause(1.8, hard=True)
    
    $ PlaySound("ExitBuilding.ogg")
    scene blank with dip_white

    jump day010402