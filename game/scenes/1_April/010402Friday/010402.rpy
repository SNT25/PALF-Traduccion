############################################################################################################################################################################################################################
# FIRST DAY ON CAMPUS: PLAYER MEETS HALL GUIDE, PROCEEDS TO LOOK FOR POTENTIAL ROOMMATE MATCH, MEETS BLUE, THEN HAS CHOICE OF ROOMMATE BETWEEN BRENDAN, CALEM, CHEREN AND TIERNO.
# PATH DIVERGES UPON SELECTING ROOMMATE, PLAYER SEPARATES FROM ROOMMATE, GETS LOST AND MEETS LEAF, REUNITES WITH ROOMMATE, THEN PROCEEDS TO THE ORIENTATION.
# PLAYER SEES ROXANNE AT ORIENTATION, ALTERNATIVE DIALOGUE DEPENDING ON ROOMMATE, PLAYER RETURNS TO ROOM WITH ROOMMATE AND SELECTS TYPE ELECTIVE CLASSES.

label day010402:    
    $ renpy.pause(1.0, hard=True)
    scene lobby with dissolve

    show falkner uniform with dis
        
    pause 0.5

    falkner @talkingmouth "Saludos. Y bienvenido a la Residencia Ancestral, una de las tres residencias de esta prestigiosa academia."
    
    hide relichall_A
    hide blank
    
    falkner @closedbrow talking2mouth "¿Estás aquí para elegir una habitación compartida? Si es así, ¿puedes decirme tu nombre y apellido?"
    
    red happy "¡Claro, es [first_name] [last_name]! Y estoy aquí para reservar una habitación, eso es lo que Brawly me dijo que hiciera."
    falkner @closedbrow talkingmouth "Hmm. Entonces, ¿ya conociste a Brawly?"
    red -happy @talkingmouth "¿Lo conoces?"

    $ BecomeNamed("Falkner")
    
    falkner @talking2mouth "Por supuesto. Me llamo Falkner, y trabajamos juntos en el consejo estudiantil.{w=0.5} Aunque 'trabajar' puede ser una palabra demasiado fuerte en su caso."

    red closedeyes angryeyebrows talking2mouth "He estado escuchando mucho sobre Brawly, pero a mí me parece alguien genial."

    falkner @closedbrow happymouth "Estoy seguro de que él lo aprecia."
    falkner @talkingmouth "En cualquier caso, las habitaciones se asignan por orden de llegada. Si tienes permiso de la academia para compartir con alguien en particular, házmelo saber. De lo contrario, puedo asignarte una habitacion que este disponible."
    falkner @sadbrow talking2mouth "También puedo asegurarme de que no compartas habitación con alguien con quien preferirías no pasar un año."

    red happy "¡Si pudieras asegurarte de que no compartiera con 'Blue Oak', entonces estaré bien con cualquiera!"

    falkner @closedbrow talking2mouth "Muy bien. Estarás en la habitación... 151. Sigue por este pasillo, gira a la izquierda en la salida del Ala Tranquill y continúa en diagonal pasando el puente elevado." 
    falkner @talkingmouth "Después de dejar tu equipaje, tal vez quieras dirigirte al vestíbulo. Para... 'relacionarse'."
    
    red @talkingmouth "Lo haré.{w=0.5} ¡Gracias!"

    hide falkner with dis

    pause 1.0
    
    redmind @confusedbrow frownmouth "Okay, la forma en que dijo 'relacionarse' fue muy rara."
    redmind "Pero bueno, es hora de ir a mi habitación."

stop music fadeout 1.5
$ renpy.pause(1.5, hard=True)
scene hall_A2b with Dissolve(1.0)
pause 1.0

show hall_A2:
    xalign 0.0 yalign 1.0 xpos 0 ypos 1080 zoom 0.625
    parallel:
        ease 1.2 xalign 0.0 yalign 1.0 xpos -300 ypos 1120
    parallel:
        ease 1.0 zoom 0.8
        
$ renpy.pause(1.2, hard=True)

show hall_A2:
    xalign 0.0 yalign 1.0 xpos -300 ypos 1120 zoom 0.8
    parallel:
        ease 1.2 xalign 0.0 yalign 1.0 xpos -100 ypos 1200
    parallel:
        ease 1.0 zoom 0.85
        
$ renpy.pause(1.4, hard=True)

show hall_A2:
    xalign 0.0 yalign 1.0 xpos -100 ypos 1200 zoom 0.85
    parallel:
        ease 1.2 xalign 0.0 yalign 1.0 xpos -550 ypos 1300
    parallel:
        ease 1.0 zoom 0.9

$ renpy.pause(1.5, hard=True)

show hall_A2:
    xalign 0.0 yalign 1.0 xpos -550 ypos 1300 zoom 0.9
    ease 1.0 xalign 0.0 yalign 1.0 xpos -480 ypos 1250 zoom 0.85

red @frownmouth "[ellipses]"

red happy "Sep. Definitivamente estoy perdido."

redmind closedeyes frownmouth "Supongo que mi racha de suerte de encontrarme con cada miembro del consejo estudiantil tenía que terminar en algún momento."

show hall_A2:
    xalign 0.0 yalign 1.0 xpos -480 ypos 1250 zoom 0.85

redmind "Pero debo haber salido del área de los dormitorios. Cuando estaba allí, había montones de estudiantes alrededor, pero ahora estoy solo."
redmind happy "Bueno. Si elijo una dirección y corro, ¡apuesto a que encontraré el camino de regreso!"
redmind -happy "Solo tengo que ajustarme los cordones y luego..."

pause 1.0

show hall_A2:
    xalign 0.0 xpos -480 ypos 1250 zoom 0.85
    ease 1.5 xpos -530 ypos 1120 zoom 0.8

pause 1.0

redmind sadeyes sadeyebrows frownmouth "Pensándolo bien... Tal vez debería esperar. No quiero tirar un jarrón ni nada, se ven muy caros."

show hall_A2:
    xpos -530 ypos 1120 zoom 0.8

Character("{color=#00b23f}???{/color}") "\"{size=30}{i}Oye, inquietin. ¿Qué estas haciendo por aquí? {/i}{/size}\""

show hall_A2 with vpunch:
    xalign 0.0 xpos -530 ypos 1120 zoom 0.8
    ease 0.1 xpos -100 ypos 1100 zoom 0.7

show leaf surprisedbrow frownmouth with dis:
    xpos 0.5

red surprisedbrow frownmouth @surprised "¡AHHH!"

$ renpy.music.queue("Audio/Music/Pallet Town A.ogg", channel='music', loop=True, fadein=1.0, tight=None)

show hall_A2:
    xpos -100 ypos 1100 zoom 0.7

red closedeyes talking2mouth "Dios, qué susto..."

show leaf -surprisedbrow -frownmouth -surprised frownmouth with dis

red happy "¡Lo siento, me asustaste muchísimo!"
red @sad2eyes embarrassedeyebrows talkingmouth "Perdon por preguntar pero, ¿te gusta escabullirte detrás de la gente y susurrarles al oído?"

leaf @talking2mouth "{i}¿Yo{/i} escabullirme?{w=0.5} ¿Tienes {i}alguna{/i} idea de dónde estás?"

red -happy @talking2mouth "Ehm..."
red @talking2mouth "Estoy...{w=0.25} estoy en un pasillo cualquier de los dormitorios, ¿no?"

show hall_A2:
    xalign 0.0 xpos -100 ypos 1100
    ease 1.0 xpos 0 ypos 1175
        
show leaf flirt with dis:
    subpixel True
    xpos 0.5 ypos 1.0
    ease 1.0 xpos 0.6 ypos 1.1

red @sad2eyes talking2mouth "Oh, espera, creo que había un letrero por aquí..."

show leaf happy with dis
    
red talking2mouth "{cps=12}'Vestidores del equipo de animadoras'{/cps}{w=0.5}"

pause 1.5

red @closedbrow talking2mouth "Oh, bueno... Parece que si que estoy {i}totalmente{/i} perdido."

pause 1.0

red closedeyes talking2mouth "Ah, mierda.{w=0.5} ¿Vas a difundir rumores raros sobre mí?"

show hall_A2:
    xalign 0.0 yalign 1.0 xpos 0 ypos 1175
    ease 1.0 xpos -100 ypos 1100
        
show leaf happy:
    subpixel True
    xpos 0.6 ypos 1.1
    ease 1.0 xpos 0.5 ypos 1.0

red sadeyes sadeyebrows @talking2mouth "En serio, solo llegué aquí por accidente. Es obvio, ¿no?"
red sadeyes sadeyebrows @talking2mouth "Además, es bastante tonto que el vestidor del equipo de animadoras esté tan lejos de donde entrenan."

show leaf happy:
    xpos 0.5 ypos 1080

leaf -happy @talkingmouth "Tengo que ser honesta, siento que estoy viendo a un Growlithe persiguiéndo su propia cola."
leaf @flirtbrow talkingmouth "Es un poco lindo."

red @confused "¿Lindo?"

leaf @happybrow talkingmouth "Sí, siempre he pensado que tener un sentido de la orientación de mierda es muy atractivo."

red @sad2eyes angryeyebrows frownmouth "[ellipses]"
red @talkingmouth "Bueno, genial. Me alegra saberlo pero, ¿podrías indicarme la dirección correcta?"

leaf -happybrow -talkingmouth @talkingmouth "No creo que el folleto sea tan difícil de seguir.{w=0.5}{nw}"
leaf @talkingmouth "No creo que el folleto sea tan difícil de seguir.{fast} Quiero decir, el diseño de las alas de los dormitorios está organizado en forma de cuadrícula, así que debería ser muy fácil de navegar."
leaf @happy "Aquí, déjame ver el tuyo."

show leaf:
    xpos 0.5 ypos 1.0
    ease 1.0 zoom 1.2 ypos 1.1 xpos 0.6

red -angrybrow closedeyes @talkingmouth "Yo... no tengo uno de esos."
red @talkingmouth "Aunque, ahora que lo mencionas, recuerdo vagamente que otros estudiantes andaban llevando unos pequeños folletos... Maldición. Supongo que me quedé sin la oportunidad de tener uno."

leaf surprisedbrow sadmouth "¿En serio fuiste todo este tiempo sin un mapa?{w=0.5} ¿Y luego lograste llegar hasta aquí desde el vestíbulo principal?"

leaf @blush talkingmouth "Debo decir que tu sentido de la orientación es increíble.{w=0.7} Ah, espera, no lo es.{w=0.5}{nw}"
leaf @happy "Debo decir que tu sentido de la orientación es increíble. Ah, espera, no lo es.{fast} ¡Es simplemente una mierda!"
    
show leaf happy:
    zoom 1.2 ypos 1.1 xpos 0.6
    ease 1.0 zoom 1.0 xpos 0.5 ypos 1.0

extend -happy @happy " ¡Jajaja!"
$ renpy.music.set_volume(1.0, delay=0.0, channel="ctc")
    
red @closedbrow talking2mouth "No me estás ganando puntos por tu personalidad en este momento..."

leaf -fullblush @flirtbrow talkingmouth "Ah, ¿así que estoy gano puntos de otra manera? Quizá sea por mi sentido de la moda."

red @sad2eyes angryeyebrows talking2mouth "Sí, claro, lo que digas. Ahora, ¿vas a seguir riéndote o me ayudaras a salir de aquí?"

leaf -flirt @closedbrow talking2mouth "Ya que lo pediste de forma tan amablemente, aceptaré esa oferta."

show leaf:
    xpos 0.5
    ease 0.5 xpos -0.5
        
leaf happy "¡Jajajajajaja!"

red @angrybrow talking2mouth "¡Oye! Deja de--"

Character("Estudiante femenina") "{size=20}... s{/size}{size=22}í{/size}{size=24}, e{/size}{size=26}lla n{/size}{size=28}os i{/size}{size=29}ba a{/size}{size=30} de{/size}{size=31}jar t{/size}{size=32}ira{/size}{size=33}das p{/size}{size=34}ara ir d{/size}e compr..."

redmind @closedbrow sweat frownmouth "Ah, genial. Más gente. Parece que ahora tendré que dar explicaciones a todo un grupo. Tal vez si mantengo la cabeza baja, pueda pasar de largo."

show leaf surprisedbrow frownmouth blush with dis:
    xpos 0.4
    ease 0.6 xpos 0.5

pause 0.6

show leaf surprisedbrow frownmouth blush:
    xpos 0.5 alpha 1.0
    
show hall_A2:
    xalign 0.0 xpos -100 ypos 1100 zoom 0.7
    ease 2.5 xpos -2000 ypos 2640 zoom 2.0 
show leafintro_A with dis:
    alpha 0.0 xalign 0.5 yalign 0.5 zoom 1.08
    pause 1.5
    ease 1.25 zoom 1.0 alpha 1.0
        
show leaf surprisedbrow frownmouth blush:
    alpha 1.0
    pause 1.5
    ease 1.0 alpha 0.0

red -angrybrow surprised "¡Gah! Eso si que es un agarre firme."
red closedeyes @talkingmouth "Oye, lo aprecio, pero no necesitas rescatarme de este lugar.{w=0.5} Puedo explicarles lo que suce--"

show leafintro_A:
    alpha 1.0
hide leaf with dis

leaf surprisedbrow frownmouth @surprised "¡No te estoy rescatando a ti! Me estoy rescatando a mí misma. No quiero que se corran rumores de que ando merodeando el vestuario de las animadoras antes de mi primera clase."
red @upeyes talking2mouth "Y yo que por un momento pensé que quizás estabas haciendo algo desinteresado."
red @closedbrow talking2mouth "Gracias por aclarármelo."

show leafintro_A:
    xalign 0.5 yalign 0.5 zoom 1.0 alpha 1.0

$ PlaySound("GenericDoorOpen.ogg")
leaf @talking2mouth "Oh por favor, ¡deja de lloriquearear y quédate aquí!"

$ PlaySound("GenericDoorClose.ogg")

redmind @thinking "...{w=0.5} Acaba de entrar al baño de mujeres."
redmind @confusedbrow frownmouth "[ellipses]"
redmind "Esto va a ser muy estúpido."

pause 1.0

$ PlaySound("GenericDoorOpen.ogg")

leaf happy "Bien, escóndete aquí. Iré a buscarte cuando esté despejado."

red @talkingmouth "No pensé que tuviera que decírtelo, pero ese es el baño de mujeres."

$ PlaySound("GenericDoorClose.ogg")
leaf firtbrow talking2mouth "Sí, yo también tengo ojos. Es el único baño que no está cerrado en este pasillo, ¡así que métete antes de que nos vean!"

red @confusedbrow talking2mouth ".{w=0.25}.{w=0.25}.{w=0.25}{nw}"
extend @confused " Estoy batallando para encontrar las palabras necesarias que expliquen por qué esto no va a suceder." 

leaf angrybrow talking2mouth "¿Cuál es tu problema? ¡Es solo un baño de chicas, no algún santuario privado! Créeme, {i}definitivamente{/i} no vas a profanarlo con {i}tu{/i} presencia masculina."

red angrybrow frownmouth "{w=0.25}.{w=0.25}.{w=0.25}.{nw}"
extend @talking2mouth " Está bien, no me gusta cómo enfatizaste el 'tu'. Te prometo que, definitivamente, soy hombre."

leaf angrybrow talkingmouth "¿En serio? Porque ahora mismo te estás comportando como una chica."

red angrybrow talking2mouth "Eso es sexista."

leaf angry "¡Simplemente métete al maldito baño!"

if (profanity):
    menu:
        ">Entrar al maldito baño":        
            red -angrybrow @talkingmouth "Está bien, lo haré. Pero voy a cubrirme los ojos mientras esté ahí."
            
            show leafintro_happy with dis
            
            leaf @happy "Eres todo un caballero."

            pause 1.0
            
            leaf @talkingmouth "Y ni una sola palabrita mientras hasta que vuelva, ¿entendido?"
            
            $ PlaySound("GenericDoorOpen.ogg")
            
            leaf @flirtbrow talkingmouth "Las damas primero."
            
            red @unamusedbrow talking2mouth "Ja.{w=0.5} Ja.{w=0.5} Ja."
            
        ">No entrar al maldito baño":        
            red @closedbrow talking2mouth "Ni loco, he pasado dieciocho años sin pisar un baño de mujeres, y no voy a empezar ahora, sería ir contra mis principios.{w=0.5} Además, ¿qué pasa si hay alguien adentro?{w=0.5} Eso sí que nos metería en problemas."
            
            leaf angry "¿Tienes problemas de memoria? ¡{i}Acabo{/i} de revisar!"

            red @surprisedeyes surprisedeyebrows talking2mouth "Sí, pero... alguien pudo haber entrado después. Hemos estado mirando la puerta, pero hay ventanas adentro."
            
            show leafintro_mad with dis:
                alpha 1.0

            red @winkeyes sadeyebrows sweat talking2mouth "Así que alguien pudo, no sé... {cps=20}escalar desde afuera, y... {cps=15}entrar por ahí..."
            
            leaf @angrysmilemouth angrybrow "[ellipses]"
            leaf @angry "{cps=12}{i}¡¿Por la ventana?!{/i}"
            
            $ PlaySound("GenericDoorOpen.ogg")
            
            red @closedeyes talking2mouth "{w=0.5}.{w=0.5}.{w=0.5}."
            red @closedeyes talking2mouth "Mejor me callo y entro."
            
        ">Saltar por la maldita ventana":
            $ leafwindowjump = True
            
            red @closedbrow talking2mouth "Ni loco, he pasado dieciocho años sin pisar un baño de mujeres, y no voy a empezar ahora, pero creo que tengo una mejor idea."
            
            leaf surprised "¿En serio? ¿Cuál?"

            red @closedeyes talking2mouth "Estamos en el segundo piso, ¿no? Y abajo solo hay césped."

            show leafintro_mad with dis

            leaf @angrysmilemouth angrybrow "[ellipses]"

            red -closedeyes -frownmouth @talkingmouth "Si salto por la ventana, seguro sobrevivo a la caída."
            
            leaf @angrysmilemouth angrybrow "[ellipses]"
            leaf @angry "{cps=12}{i}¡¿Me estas tomando el pelo?!{/i}"
            
            $ PlaySound("GenericDoorOpen.ogg")
            
            red @closedeyes talking2mouth "{w=0.5}.{w=0.5}.{w=0.5}."
            red @closedeyes talking2mouth "Mejor me callo y entro."
else:
    menu:
        ">Entrar al ******* baño":        
            red -angrybrow @talkingmouth "Está bien, lo haré. Pero voy a cubrirme los ojos mientras esté ahí."
            
            show leafintro_happy with dis
            
            leaf @happy "Eres todo un caballero."

            pause 1.0
            
            leaf @talkingmouth "Y ni una sola palabrita mientras hasta que vuelva, ¿entendido?"
            
            $ PlaySound("GenericDoorOpen.ogg")
            
            leaf @flirtbrow talkingmouth "Las damas primero."
            
            red @unamusedbrow talking2mouth "Ja.{w=0.5} Ja.{w=0.5} Ja."
            
        ">No entrar al ******* baño":        
            red @closedbrow talking2mouth "Ni loco, he pasado dieciocho años sin pisar un baño de mujeres, y no voy a empezar ahora, sería ir contra mis principios.{w=0.5} Además, ¿qué pasa si hay alguien adentro?{w=0.5} Eso sí que nos metería en problemas."
            
            leaf angry "¿Tienes problemas de memoria? ¡{i}Acabo{/i} de revisar!"

            red @surprisedeyes surprisedeyebrows talking2mouth "Sí, pero... alguien pudo haber entrado después. Hemos estado mirando la puerta, pero hay ventanas adentro."
            
            show leafintro_mad with dis:
                alpha 1.0

            red @winkeyes sadeyebrows sweat talking2mouth "Así que alguien pudo, no sé... {cps=20}escalar desde afuera, y... {cps=15}entrar por ahí..."
            
            leaf @angrysmilemouth angrybrow "[ellipses]"
            leaf @angry "{cps=12}{i}¡¿Por la ventana?!{/i}"
            
            $ PlaySound("GenericDoorOpen.ogg")
            
            red @closedeyes talking2mouth "{w=0.5}.{w=0.5}.{w=0.5}."
            red @closedeyes talking2mouth "Mejor me callo y entro."
            
        ">Saltar por la ******* ventana":
            $ leafwindowjump = True
            
            red @closedbrow talking2mouth "Ni loco, he pasado dieciocho años sin pisar un baño de mujeres, y no voy a empezar ahora, pero creo que tengo una mejor idea."
            
            leaf surprised "¿En serio? ¿Cuál?"

            red @closedeyes talking2mouth "Estamos en el segundo piso, ¿no? Y abajo solo hay césped."

            show leafintro_mad with dis

            leaf @angrysmilemouth angrybrow "[ellipses]"

            red -closedeyes -frownmouth @talkingmouth "Si salto por la ventana, seguro sobrevivo a la caída."
            
            leaf @angrysmilemouth angrybrow "[ellipses]"
            leaf @angry "{cps=12}{i}¡¿Me estas tomando el pelo?!{/i}"
            
            $ PlaySound("GenericDoorOpen.ogg")
            
            red @closedeyes talking2mouth "{w=0.5}.{w=0.5}.{w=0.5}."
            red @closedeyes talking2mouth "Mejor me callo y entro."
        
scene bathroom_light with splitfadefast
$ renpy.pause(0.75, hard=True)

hide leafintro_A
hide leafintro_mad
hide leafintro_happy

red night @unamusedbrow talking2mouth "Ah, sí, apaga las luces también. Eso no es para nada espeluznante..."

leaf @sarcastic "Solo compórtate y quédate aquí, no tardo."

$ PlaySound("GenericDoorClose.ogg")
show bathroom_dark with splitfadefaster

redmind @sadeyes sadeyebrows frownmouth "Definitivamente... esto no era lo que esperaba de Kobukan.{w=0.5} Estar atrapado en el baño de mujeres,{nw}"
$ PlaySound("fading_footsteps.ogg")
extend @closedbrow sweat frownmouth " y la chica que me metió aquí se acaba de ir corriendo."

pause 1.0

redmind @sad2eyes angryeyebrows frownmouth "Le doy cinco minutos para volver, y si no, salto por la ventana."

pause 1.0

$ PlaySound("GenericDoorOpen.ogg")
hide bathroom_dark with splitfadefast

leaf @happy "Listo, ya puedes salir."

window hide
hide leaf
    
scene hall_A2 with splitfade:
    xanchor 0.0 zoom 0.7
    
$ renpy.pause(1.0, hard=True)

show leaf with dis

red @talkingmouth "Eso fue rápido. ¿Qué les dijiste?"
    
leaf @happy "Solo les dije que vi un Eevee shiny en la hierba alta al otro lado del edificio. Eso debería entretenerlos un rato."

red @surprised "¡Eso es casi cruel! Aunque estuviera un 99%% seguro de que mentías, tendría que ir a comprobarlo."

leaf @flirtbrow talking2mouth "Nunca vi a un grupo de gente girar en seco y salir corriendo tan rápido.{w=0.5}{nw}" 
extend @sad " Lo admito, me sentí un poquito culpable."

red @confusedeyebrows frownmouth "[ellipses]"

leaf @talkingmouth "Bueno, ya se me pasó. {w=0.25}Por cierto, antes de que se me olvide... {w=0.25}toma, recogí uno de los folletos que dejaron caer."

show leaf at getcloser

pause 1.0
    
leaf @happy "Si no me equivoco, te va a venir bien."

red @talkingmouth "Gracias, supongo. No estoy seguro de que todo esto fuera necesario, pero lo hiciste... {w=0.5}{nw}"
extend @sadeyebrows sadeyes talkingmouth "Yo... bueno..."

leaf @talking2mouth flirtbrow "Serías mucho más lindo si hubieras terminado la frase con un 'gracias'."

red @sad2eyes sweat talkingmouth "Lo tendré en cuenta la próxima vez que una chica me encierre en un baño para salvar su reputación de chismes de bachillerato."

show leaf at getfurther

leaf closedbrow happymouth "Me lo agradecerás, créeme, sé {i}todo{/i} sobre manejar intrigas sociales." 
leaf -happymouth @talking2mouth "Pero, ¿sabes? A pesar de todo lo que pasó, fue...{w=0.6} algo.{w=0.25}.{w=0.25}."

$ renpy.pause(2.0, hard=True)

leaf sadbrow blush -frownmouth @talkingmouth "Muy divertido.{w=0.5} Probablemente, lo más divertido que he tenido en un buen tiempo."
leaf -sadbrow @happy "¡Deberíamos hacerlo otra vez!"

show leaf:
    alpha 1.0 ypos 1.0 zoom 1.0

red @closedeyes talkingmouth "Voy a hacer lo posible por evitarlo, pero si no puedo... {w=0.5}{nw}"
extend @happy "Seguro, ¿por qué no?"

show leaf happy with dis:
    xpos 0.5 zoom 1.0 ypos 1.0
    ease 1.5 xpos 1.0 zoom 1.35 ypos 1.5

pause 2.0

hide leaf
hide leafintro_A

redmind "... Parecía una chica agradable."

window hide
$ renpy.pause(1.5, hard=True)

redmind @wince frownmouth "Ah, olvidé preguntarle su nombre."

window hide
stop music fadeout 2.5

scene blank2 with Dissolve(1.5)
$ renpy.pause(1.5, hard=True)

queue music "Audio/Music/SoaringIllusions_Intro.ogg" noloop
queue music "Audio/Music/SoaringIllusions.ogg"

show dorm_empty_A with Dissolve(1.0):
    zoom 1.0 xpos 0 ypos 0 xanchor 0 yanchor 0
    ease 4.0 zoom 1.18 xpos -170 ypos -180

$ PlaySound("Door_Open1.ogg")

redmind @thinking "Oh, así que esta es mi habitación."

pause 1.0

redmind @thinking "Por el próximo año..."

pause 1.0

redmind @thonk "Hmm, ¿no se suponía que esto era un dormitorio compartido? No veo las cosas de nadie más, aunque hay cuatro camas más."

$ PlaySound("Chime.ogg")

Character("{color=#a2254b}Voz de Roxanne") "{color=#e70000}Atención, son las 2:00 PM. En una hora dará inicio la sesión de orientación en el auditorio de la Residencia Ancestral. Se recomienda la asistencia de todos los alumnos de nuevo ingreso.{/color}"

redmind thinking "¿Seré el primero de mis compañeros de cuarto en llegar? Parece que van a llegar muy justos de tiempo."

$ PlaySound("Door_Open1.ogg")

pause 1.0

show dorm_empty_A:
    zoom 1.18 xpos -170 ypos -180 xanchor 0 yanchor 0
    ease 0.4 zoom 1.0 xpos 0 ypos 0

Character("{color=#c1861e}Voz joven") "\"{size=20}...van {/size}{size=22}a llegar {/size}{size=24}muy justos de tiempo, {/size}¿eh?\""

show ethan with dis:
    xpos 1.5
    ease 1.0 xpos 0.5

show red happy at Transform(xpos=0.08, yanchor=0.35)
show ethan happybrow talkingmouth with dis
Character("{color=#cf0000}[first_name]{/color} & {color=#c1861e}???{/color}") "\"¡Oh, hola!\""

show ethan surprisedbrow frownmouth -talkingmouth with dis
show red surprisedbrow frownmouth with dis

red @thinking "[ellipses]"
ethan @thinking "[ellipses]"

show red talkingmouth with dis
show ethan talkingmouth -surprisedbrow -frownmouth -surprised with dis
Character("{color=#cf0000}[first_name]{/color} & {color=#c1861e}???{/color}") "\"¿Quieres hablar tú primero?\""

show ethan happybrow talkingmouth with dis
show red happybrow talkingmouth with dis
Character("{color=#cf0000}[first_name]{/color} & {color=#c1861e}???{/color}") "\"Hey, perdon, esto es un poco raro.\""

show ethan angrybrow talking2mouth with dis
show red angrybrow talking2mouth with dis
Character("{color=#cf0000}[first_name]{/color} & {color=#c1861e}???{/color}") "\"Ve tú primero.\""

show ethan surprisedbrow frownmouth with dis
show red surprisedbrow frownmouth with dis
Character("{color=#cf0000}[first_name]{/color} & {color=#c1861e}???{/color}") "\"[ellipses]\""

show ethan angrybrow surprisedmouth with dis
show red angrybrow surprisedmouth with dis
Character("{color=#cf0000}[first_name]{/color} & {color=#c1861e}???{/color}") "\"¡Tres tristes tigres, tragaban trigo en un trigal!\""

pause 1.0

hide red at Transform(xpos=0.08, yanchor=0.35) with dis

pause 1.0

hide red

ethan -angrybrow -surprisedmouth @happy "Ethan."

red @talkingmouth sadbrow "Oh, gracias al cielo, rompimos la maldición. ¿Quién es Ethan?"

$ BecomeNamed("Ethan")

ethan @talkingmouth "Yo. Parece que también soy uno de tus compañeros de cuarto."

red @talkingmouth "Genial, un gusto, me llamo [first_name]."

ethan @talkingmouth "Entonces, cuéntame, ¿cuál es tu historia?"

red @talkingmouth "Bueno, soy de Pueblo Paleta, en Kanto. {w=0.5}... Y eso es básicamente todo."

ethan @talking2mouth "¿Pueblo Paleta? ¡Oh, conozco ese lugar! Ahí vive el Profesor Oak, ¿no? Fui a su laboratorio una vez en un viaje escolar. Yo soy de Pueblo Primavera, en Johto."

red @surprised "...{w=0.5} Espera, ¿el Profesor Oak? ¿Te refieres a Sam?"

ethan @confusedeyebrows talking2mouth "¿Hablas en serio? Sí, puede que sea algo mayor, pero es un investigador Pokémon mundialmente famoso. Es mucho más que solo 'Sam'."

red @talkingmouth "Huh."
red -surprisedbrow -frownmouth -surprised @sadbrow talkingmouth "Para mí, solo era mi vecino."

ethan @talkingmouth "Guau, ¿+él era tu vecino? Espera..."
ethan @surprised "¡Mierda, ya me acordé de ti! ¡Casi atropellas a nuestra profesora cuando cruzábamos el centro del pueblo!"

red @happy "No me acuerdo de eso, ¡pero suena como algo que haría!"

ethan @happy "Al parecer el mundo es un pañuelo..."

show ethan -surprisedbrow -frownmouth -surprised with dis

red @talkingmouth "Parece que llegamos prácticamente al mismo tiempo. ¿Quieres tomar alguna de estas dos camas? Así podemos empezar a desempacar."

ethan @talking2mouth "¡Claro! Aunque me pregunto quiénes serán los otros tres."

red @confused "Ojalá no tengamos que pasar por toda la rutina de hablar al mismo tiempo con ellos también."
red @happy "Si los cinco hablamos a la vez, podríamos explotarle los oídos a un Loudred."

ethan @happy "Jajaja, sí."

pause 1.0

ethan @sadbrow happymouth "¿Un qué?"

show ethan surprisedbrow frownmouth with dis

red @talkingmouth "Oh, es un Pokémon de Hoenn de tipo normal. Tiene dos orejas grandes que pueden recibir y emitir sonido. La mayoría son completamente inmunes a los ataques basados en sonido."

ethan @surprised "Bro... ¿De verdad solo sabías eso de memoria?"

red @sadeyes sadeyebrows talkingmouth "Bueno... sí. He estudiado un poco."

ethan -surprisedbrow -frownmouth @happy "Bastante impresionante, [first_name]. Creo que ya sé con quién quiero estudiar."

red @happy "Bueno, dejemos eso para después de que terminemos de acomodar la habitación."

$ PlaySound("Door_Open1.ogg")

show ethan surprisedbrow frownmouth with dis

pause 1.0

show calem with dis:
    xpos 1.5 xzoom -1
    ease 1.0 xpos 0.66

show ethan: 
    xpos 0.5
    ease 1.0 xpos 0.33

calem @talkingmouth "Sí, este parece ser el lugar correcto."

$ BecomeNamed("Calem")

calem @talking2mouth "Un placer, me llamo Calem. ¿Y ustedes?"

ethan -surprisedbrow -frownmouth @happy "¡Hey, Calem! Yo soy Ethan, y este tipo de aquí es [first_name]."

red @talkingmouth "¡Mucho gusto!"

calem @happymouth "Igualmente. Llegar a mi dormitorio era una de mis prioridades, pero parece que me demoré un poco."

ethan @talkingmouth "No te preocupes, [first_name] y yo justo íbamos a desempacar."
ethan @playfulbrow talkingmouth "Oye, ¿ese es un acento de Kalos?"

calem @closedbrow talkingmouth "Sí, así es. Soy de Pueblo Boceto, al sureste de Kalos."
ethan @happy "Hombre, entonces seguro tienes mucha suerte con las chicas. Sé que se vuelven locas por un sexy acento kalosiano."

show ethan surprisedbrow frownmouth with dis

calem @angrybrow talking2mouth "Uno podría sorprenderse. Me han dicho que tiendo a sonar pretencioso."

pause 1.0

ethan -surprisedbrow -frownmouth -surprised @confused "Bro. ¿'Tiendes a sonar pretencioso'...?"

calem smilemouth @closedbrow talking2mouth "Sí, supongo que eso es un defecto que se demuestra por sí solo."

pause 1.0

red @talkingmouth "Bueno, ¿tienes alguna preferencia sobre alguna cama?"

calem -closedbrow @talking2mouth "Preferiría no dormir demasiado cerca de otros hombres. Me quedaré con la quinta cama, la que está más apartada."

ethan @talkingmouth "Genial. Entonces solo nos queda desempacar y..."

$ PlaySound("Door_Open1.ogg")

ethan @surprisedbrow talking2mouth "Oh, ¿aquí viene un nuevo retador?"

show ethan surprisedbrow frownmouth
show calem surprisedbrow frownmouth
with dis

show hilbert with dis:
    xpos 1.5
    ease 1.0 xpos 0.75

show calem:
    xpos 0.66 xzoom -1
    ease 1.0 xpos 0.5 xzoom 1

show ethan: 
    xpos 0.33
    ease 1.0 xpos 0.25

pause 2.0

hilbert @angrybrow talkingmouth "Bueno, ¿y ustedes qué tanto miran?"

show calem:
    xpos 0.5 xzoom 1

calem -surprisedbrow -frownmouth @closedbrow talking2mouth "Por la forma en que entraste, asumo que eres uno de nuestros compañeros de cuarto, ¿me equivoco? Tu primera prioridad, entonces, debería ser decirnos tu nombre."

ethan -surprisedbrow -frownmouth @happy "Sí, ¡yo soy Ethan, este tipo es [first_name] y este otro es Calamari!"

calem @sadbrow talkingmouth "{size=30}En realidad, es Calem.{/size}"

show calem angrybrow
show ethan angry
with dis

hilbert @sadbrow talkingmouth "...{w=0.5} No recuerdo haber preguntado y definitivamente no me importa."

show hilbert:
    xpos 0.75
    linear 1.0 xpos 0.375

pause 1.0

show dorm_empty_A at vpunch

show calem surprisedbrow frownmouth with dis
show ethan surprisedbrow frownmouth with dis
show hilbert angrybrow with dis
red angry "Dinos tu nombre, o te llamaremos 'Edgelord' todo el año."

pause 1.0 

hilbert @thinking "[ellipses]"

red frownmouth "[ellipses]"

Character("{color=#353535}Edgelord") "\"[ellipses]\""

red @thinking "[ellipses]"

$ BecomeNamed("Hilbert")

hilbert @closedbrow talkingmouth "[ellipses]{w=0.5} Hilbert."
hilbert @sadbrow talkingmouth "Y tomaré la cama que esta allá."

show hilbert:
    xpos 0.375
    ease 1.0 xpos -0.5

pause 1.0

show ethan -surprisedbrow -frownmouth -surprised with dis

calem -surprisedbrow -frownmouth -surprised smilemouth @closedbrow talkingmouth "{size=30}Esa iba a ser mi cama... {/size}Bueno, da igual. Buen trabajo, [first_name]."

ethan @happy "¡Sí, estuvo genial!"
ethan @sad "Supongo que pasaremos el año con el querido Hindenburg entonces..."

calem @closedbrow talking2mouth "{size=30}Estoy bastante seguro de que dijo 'Hilbert'.{/size}"
calem @talkingmouth sadbrow "En fin, en una academia tan prestigiosa como esta, puedo entender que algunos no estén interesados en hacer amigos."
calem @talking2mouth angrybrow "Pero la competitividad de este lugar no es excusa para tener malos modales."

ethan @happy "¿Verdad? Es como, 'ok, bro, ya entendimos que eras el tipo rudo de tu bachillerato'. Relájate un poco."

red @wince talking2mouth "Bueno, esperemos que nuestro último compañero de cuarto sea... un poco diferente."

pause 1.0

$ PlaySound("Door_Open1.ogg")

pause 1.0

calem angrybrow -smilemouth @surprisedbrow talkingmouth "{i}En parlant du loup...{/i}"

ethan @happy "¡Ya rugiste, Calamari!"

pause 1.0

calem -angrybrow @happybrow talkingmouth "Es Calem, Ethan. Me llamo Calem."

show brendan happy with dis:
    xpos 1.5
    ease 1.0 xpos 0.75

brendan @happy "¡Hey, chicos!"

$ BecomeNamed("Brendan")

brendan -happy @talking2mouth "¡Me llamo Brendan y los Pokémon son mi pasión! ¿Qué estan haciendo?"

show calem angrybrow with dis

ethan happy "¡Eso está mucho mejor! ¡Hey, Brendan! Yo soy Ethan, este tipo es [first_name], el 'Sr. Acento sexy' es Calamari, y el bajito, oscuro y melancólico de allá es Hildegard."

pause 2.0

calem sadbrow @angry "¿Por qué seguimos dejando que Ethan nos presente? ¿Y por qué solo acierta con el tuyo?"

show ethan -happy with dis

red @happy sweat "Sí, eh, este tipo es Calem y ese de ahí es Hilbert. ¡Encantado, Brendan!"

show brendan at getcloser, rightside
show ethan surprisedbrow frownmouth with dis
show calem surprisedbrow with dis

brendan surprisedbrow frownmouth @surprised "¡Bro! Tú y yo somos almas gemelas, ¡puedo sentirlo!"

red @confused "¿Ah, sí...?"

brendan -surprisedbrow -frownmouth -surprised @happy "¡Tus muslos, amigo! Están increíblemente tonificados. Corres mucho, ¿no?"

show calem closedbrow smilemouth with dis
show ethan -surprisedbrow -frownmouth with dis

red @happy "Oh, eh sí, todo el tiempo. De hecho, una vez al día sí puedo."

show brendan -surprisedbrow -frownmouth at getfurther, rightside with dis

brendan @talkingmouth "¡Genial! Tú y yo correremos juntos, entonces. Así me aseguro de no saltarme el día de pierna."
red @talkingmouth "Es toda una responsabilidad, pero haré lo que pueda."
ethan @happy "Chicos, ¿ven lo que significa esto? ¡Los cinco estamos aquí y ahora! ¡Los cinco compañeros de cuarto que pasarán el próximo año juntos! ¿No es increíble?"
calem @happybrow talkingmouth "Definitivamente parece el inicio de algo excelente. Espero con ansias conocerlos, y hasta entablar amistad con todos ustedes."
brendan @happy "¡Igualmente, chicos! Oigan, si alguno necesita ayuda con algo, o quiere entrenar, solo díganme. ¡Brendan está aquí para hacer amiguis!"

show brendan angrybrow frownmouth with dis
show calem closedbrow -smilemouth with dis
show ethan angrybrow frownmouth with dis

show brendan:
    xpos 0.75
    ease 1.0 xpos 0.8

show hilbert sadbrow with dis:
    xpos -0.5
    ease 1.0 xpos 0.2

show calem:
    xpos 0.5 xzoom 1
    ease 1.0 xpos 0.6 xzoom -1

show ethan: 
    xpos 0.25
    ease 1.0 xpos 0.4

stop music fadeout 1.0

hilbert @sadbrow talkingmouth "...{w=1.25} Patético."

show brendan:
    xpos 0.8

show hilbert sadbrow with dis:
    xpos 0.2

show calem:
    xpos 0.6 xzoom -1

show ethan: 
    xpos 0.4

$ renpy.music.queue("Audio/Music/Littleroot_Start.ogg", channel='music', loop=False, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/Littleroot_Loop.ogg", channel='music', loop=True, fadein=0.0, tight=None)

ethan @angry "¿Cuál es tu maldito problema, amigo?"

show hilbert:
    xzoom 1 xpos 0.2
    ease 0.5 xzoom -1 xpos 0.2

hilbert @angrybrow talkingmouth "Están hablando de amistad, camaradería y {i}trabajar juntos{/i}. ¿No se dan cuenta de lo que esta academia les hará pasar?"

show hilbert:
    xzoom -1 xpos 0.2

calem @closedbrow talkingmouth "Sea lo que sea que nos haga pasar, enfrentarlo con aliados es mucho mejor que hacerlo solos."

hilbert @talkingmouth "Tienes que hacerlo solo, [first_name]. Puedo ver en tus ojos que sabes a lo que me refiero. Explícaselos."

red @angrybrow frownmouth "[ellipses]"

ethan @surprised "¿Espera, [first_name]? ¿Sabes a lo que se refiere?"

red -angrybrow @sadeyes talking2mouth "La Academia Kobukan tiene una tasa de graduación obligatoria del 80%%. A los estudiantes del 20%% inferior no se les permite graduarse. Se te permite intentarlo de nuevo, pero..."

show brendan surprisedbrow frownmouth with dis

red @closedeyes talking2mouth "Si alguna vez fallas en graduarte, no serás elegible para ningún tipo de ayuda financiera."
red @closedeyes talking2mouth "En la práctica, si no te gradúas la primera vez, nunca lo harás. A menos que seas ridículamente rico."
calem @sad "Esto solo es posible gracias al currículo único de un año de Kobukan."
calem @sad "Si fuera un plan de estudios estándar de tres años, los estudiantes gastarían mucho más tiempo y dinero antes de que se les dijera que no pueden graduarse."

show ethan sadbrow frownmouth
show calem sadbrow
show brendan sadbrow frownmouth
with dis

pause 2.0

hilbert @angrybrow talkingmouth "¿Ven a lo que me refiero? Uno de cada cinco estudiantes no se graduará, y aquí somos cinco."
hilbert angry "Hagan sus calculos. Pueden alegar, pero los números no mienten."

show hilbert:
    ease 1.0 xpos 1.5

pause 0.9

$ PlaySound("Door_Slam.ogg")

pause 1.0

show calem -sadbrow -frownmouth with dis
show brendan -sadbrow -frownmouth with dis

ethan@ happy "B-bueno, eh... ¡Hagámoslo tan bien para que el emo termine siendo el que no se gradúe en lugar de uno de nosotros!"

red @happy "¡Así se habla, Ethan!"

ethan @happy "¡Sí!"
ethan @thinking "[ellipses]"
ethan @sadbrow talkingmouth "Ok voy a ser sincero, yo no sabía {i}nada{/i} de esto y la verdad me está asustando un poco."

calem @talkingmouth "Debemos ser conscientes de nuestras probabilidades, pero no hay nada que una mente clara y prioridades definidas no pueda solucionar."

brendan @angrybrow happymouth "¡Sí! No firmé todos esos papeles ni hice todas esas pruebas solo para asustarme con las estadísticas de años anteriores. ¡Quizá hasta seamos tan buenos que este año desechen la regla del 80%% de graduación!"

red @happy "¡Claro que sí! No te preocupes. Puede que acabe de conocerte, Ethan, pero apuesto a que te graduarás tan fácilmente como cualquiera de nosotros." 
red @happy "Y casi al final del año, cuando Hilbert nos ruegue que le ayudemos a estudiar, tal vez seamos tan amables de decir que sí."

stop music fadeout 1.0

ethan -frownmouth @sadbrow talkingmouth "Si tu lo dices..."

queue music "Audio/Music/SoaringIllusions_Intro.ogg" noloop
queue music "Audio/Music/SoaringIllusions.ogg"

ethan happy "¡Está bien! ¡Aún no me rendiré! ¡No antes de que siquiera empiece el año!"

show calem happy with dis
show brendan happy with dis

red @happy "¡Ese es el espiritu!"

$ renpy.music.set_volume(0.3, delay=3.0, channel="music")

show flashback with Dissolve(2.0)

redmind @thinking "Yo ya conocía esas estadísticas, pero... aunque de alguna manera entré, sigo en el décimo percentil inferior."
redmind @thinking "Si quiero pasar el año, voy a tener que esforzarme más que nunca..."
redmind @happy "¡Pero eso está bien! Algún día seré un campeón, y siempre supe que tendría que trabajar hasta el límite para lograrlo. ¡Así que mejor empiezo ya!"

$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

hide flashback
show ethan -happy
show brendan -happy
show calem -happy 
with dis

calem @closedbrow talkingmouth "Originalmente planeaba desempacar antes de la orientación, pero se nos esta acabando el tiempo. ¿Quizás deberíamos ir a la orientación y luego volver?"

ethan @talkingmouth "Claro, me parece bien."

stop music fadeout 1.0
$ renpy.pause(1.25, hard=True)

queue music "Audio/Music/Kalos_Start.ogg" noloop
queue music "Audio/Music/Kalos_Loop.ogg"

scene orientation with dissolve
$ renpy.pause(1.0, hard=True)

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.0)

red surprisedbrow frownmouth @surprised "Guau, es impresionante cuántos estudiantes hay en este lugar."

show calem with dis

calem @closedbrow talking2mouth "Uno podría preguntarse, ¿cuántos estudiantes tendrían si siguiera un plan de estuidos estándar de tres años? De por si ya parece que tienen las manos llenas tal como estan ahora."

red -surprisedbrow -frownmouth -surprised @talkingmouth "No pareces afectado."
calem @talking2mouth "Hago lo posible por no estarlo, pero te aseguro que estoy bastante impresionado. Sin embargo, he pasado bastante tiempo en Ciudad Luminalia la cual es aún más grande que Ciudad Inspira."

pause 1.0

show brendan sadbrow frownmouth at rightside with dis

brendan @talking2mouth "Hmm... No la veo."

show ethan at leftside with dis

ethan @talkingmouth "¿A quién buscas, Brentham?"

calem @angry "{size=30}Bueno, al menos no se equivoca {i}solo{/i} con mi nombre.{/size}"

brendan @talking2mouth "A mi novia, me dijo que se encontraría conmigo durante la orientación."

show calem surprisedbrow with dis

ethan @surprised "¡No puede ser! ¡¿Tan rapido te pusiste de novio con una chica de este lugar?!"

show calem closedbrow smilemouth with dis

brendan -sadbrow -frownmouth @happy "Oh no amigo, lo entendiste mal. Es mi amiga de la infancia, nos inscribimos juntos."

ethan @sweat happy "Ahhhhh, vale. Ya iba a decir que eso había sido demasiado rápido."

brendan @happy sweat "Jaja, lo habría sido ¿no? {w=0.5}{nw}"
extend @surprised "¡Oh, esperen, ahí está!"

show calem:
    xpos 0.5 xzoom 1
    ease 1.0 xpos 0.8 xzoom -1

show ethan:
    xpos 0.25
    ease 1.0 xpos 0.6

show brendan:
    xpos 0.75
    ease 1.0 xpos 0.4

show may happy with dis:
    xpos -0.5
    ease 1.0 xpos 0.2

may happybrow @happy "¡Hola, cariño!"

show calem:
    xpos 0.8 xzoom -1

show brendan:
    xpos 0.4

show may:
    xpos 0.2

show ethan at getcloser:
    xpos 0.6

ethan surprisedbrow frownmouth @surprised "{size=30}Dios santo, ¡es muy linda!{/size}"
red @sad2eyes angryeyebrows talking2mouth "{size=30}Sí, y es la novia de nuestro compañero de cuarto, así que no te hagas ideas raras.{/size}"
ethan -surprisedbrow -frownmouth @sadbrow talkingmouth "{size=30}Er... claro, jaja...{/size}"

show ethan at getfurther:
    xpos 0.6

$ BecomeNamed("May")

brendan @talking2mouth "Chicos, ella es mi novia, May. Crecimos juntos en Villa Raíz."

ethan @talkingmouth "Oh, conozco ese lugar. Ahí vive el Profesor Abedul. Está en Hoenn, ¿verdad?"

may -happybrow @happy "Oh, ¿lo conoces? ¡Sí, estas en lo cierto!"

brendan @surprisedbrow talking2mouth "Vaya, ¿conoces al viejo de May?"

ethan @surprised "¿Viejo...? ¡Espera, te refieres a...!"

may @sadbrow talkingmouth "¡Sip! Mi nombre completo es May Abedul."

ethan @closedbrow talking2mouth sweat "Vaya, esto si que es curioso. [first_name] conoce al Profesor Oak, Brendan conoce al Profesor Abedul, yo conozco al Profesor Elm..."

calem @closedbrow talking2mouth "Quizás valga la pena mencionar que trabajé como pasante del Profesor Ciprés durante un par de años."

ethan @confused "¿Qué demonios...?{w=0.5} ¿Así que todos, excepto Hickey, tenemos conexión personal con un Profesor importante de nuestra región?"

brendan @closedbrow talkingmouth "O sea, no sabemos si él tiene o no. Probablemente no nos lo diría de todos modos."

may @sadbrow talkingmouth "¿De qué están hablando?"

calem @thinking "[ellipses]"

brendan @closedbrow talkingmouth "Me pregunto si...{w=0.5} nah, no es nada."
brendan @talking2mouth "En fin, cariño, ¿cómo está tu habitación? ¿Te tocó con gente tan genial como los chicos con los que estoy?"

may @angrybrow happymouth "Bueno, son un poco menos 'varoniles', pero sí, ¡creo que son bastante geniales!"

calem @talkingmouth "Hubiera preferido que pudiéramos elegir a nuestros compañeros de cuarto directamente, pero al menos parece que todo salió bien."

may -angrybrow @happy "Oh, ¡a mí me encanta la aleatoriedad de todo esto! Incluso si hubiéramos podido elegir, habría optado por el azar solo para ver con quién terminaba."

brendan @happy "¡Sí! May siempre ha amado dejar las cosas al azar. Es más, la primera vez que le pedí salir, ¡lo decidió jugando cara o cruz!"

may @sadbrow talkingmouth "No me molestaria si dejaras de contarle eso a la gente..."

calem @surprised "¡ !"

calem @talkingmouth "Oh, miren el escenario. Creo que están a punto de empezar, deberíamos ir a buscar asientos."

redmind @thinking "Hmm, vio ese momento incómodo y cambió de tema de inmediato. Eso fue muy astuto."

ethan @talkingmouth "Sí, vamos."

stop music

$ PlaySound("Mic_Feedback.ogg")
$ renpy.music.stop(channel='crowd', fadeout=0.5)

show orientation:
    parallel:
        xalign 0.0
        ease 0.02 xpos -30
        ease 0.02 xpos 30
        ease 0.02 xpos 0
        repeat 40
    parallel:
        yalign 0.0
        ease 0.02 ypos -15
        ease 0.02 ypos 15
        ease 0.02 ypos 0
        repeat 40

show calem surprisedmouth deadbrow at monochrome:
    parallel:
        xpos 0.8
        ease 0.02 xpos 0.85
        ease 0.02 xpos 0.75
        ease 0.02 xpos 0.8
        repeat 40
    parallel:
        yalign -0.11
        ease 0.02 ypos 25
        ease 0.02 ypos -25
        ease 0.02 ypos 0
        repeat 40
    
show brendan surprisedmouth deadbrow at monochrome:
    parallel:
        xpos 0.4
        ease 0.02 xpos 0.45
        ease 0.02 xpos 0.35
        ease 0.02 xpos 0.4
        repeat 40
    parallel:
        yalign -0.11
        ease 0.02 ypos 25
        ease 0.02 ypos -25
        ease 0.02 ypos 0
        repeat 40

show may surprisedmouth deadbrow at monochrome:
    parallel:
        xpos 0.2
        ease 0.02 xpos 0.25
        ease 0.02 xpos 0.15
        ease 0.02 xpos 0.2
        repeat 40
    parallel:
        yalign -0.11
        ease 0.02 ypos 25
        ease 0.02 ypos -25
        ease 0.02 ypos 0
        repeat 40

show ethan surprisedmouth deadeyes surprisedeyebrows at monochrome:
    parallel:
        xpos 0.6
        ease 0.02 xpos 0.65
        ease 0.02 xpos 0.55
        ease 0.02 xpos 0.6
        repeat 40
    parallel:
        yalign -0.11
        ease 0.02 ypos 25
        ease 0.02 ypos -25
        ease 0.02 ypos 0
        repeat 40

show red:
    xpos -0.5

red @talkingmouth "{cps=0}OH, DIOS. {size=44}¿POR QUÉ?{w=0.5} ¡SANTO CIELOS!{/size}{/cps} ¡Este ruido! {cps=120}¡Es como si mil Pokémon usaran Chillido y Supersónico al mismo tiempo!{w=0.5} ¡No sé si estoy gritando por el dolor o si todavía es el eco!{/cps}"

window hide

show calem at monochrome:
    xpos 0.8 ypos 1.0
    ease 0.5 xpos 0.78 ypos 1.1 rotate -10.0
show ethan at monochrome:
    xpos 0.6 ypos 1.0
    ease 0.5 xpos 0.62 ypos 1.1 rotate 10.0
show brendan at monochrome:
    xpos 0.4 ypos 1.0
    ease 0.5 xpos 0.38 ypos 1.1 rotate -10.0
show may at monochrome:
    xpos 0.2 ypos 1.0
    ease 0.5 xpos 0.22 ypos 1.1 rotate 10.0
$ renpy.pause(0.5, hard=True)
show calem at monochrome:
    xpos 0.78 ypos 1.1 rotate -10.0
    ease 0.5 xpos 0.8 ypos 1.2 rotate 10.0
show ethan at monochrome:
    xpos 0.62 ypos 1.1 rotate 10.0
    ease 0.5 xpos 0.6 ypos 1.2 rotate -10.0
show brendan at monochrome:
    xpos 0.38 ypos 1.1 rotate -10.0
    ease 0.5 xpos 0.4 ypos 1.2 rotate 10.0
show may at monochrome:
    xpos 0.22 ypos 1.1 rotate 10.0
    ease 0.5 xpos 0.2 ypos 1.2 rotate -10.0
$ renpy.pause(1.0, hard=True)
hide calem
hide ethan
hide brendan
hide may
with moveoutbottom
show orientation at vpunch

hide red
$ PlaySound("Thud2.ogg")
$ PlaySound("Thud.ogg")
$ renpy.pause(0.5, hard=True)

$ PlaySound("Complaining.ogg")
    
red @wince talking2mouth "¡¿Qué clase de pésimo altavoz hace un sonido así?!"

$ PlaySound("Mic_Feedback2.ogg")

roxanne uniform @angry "--Te dije que esta cosa estúpida no va a funcionar!"    
roxanne @surprised ".{w=0.25}.{w=0.25}.{w=0.5}{nw}"

queue music "Audio/Music/Kalos_Start.ogg" noloop
queue music "Audio/Music/Kalos_Loop.ogg"

roxanne @happy "...{fast} ¡Oh, ahí está!"

redmind -angrybrow @closedbrow frownmouth "Dudo que se haya dado cuenta de que la mitad de la sala sigue en el suelo con el cerebro frito después de ese estruendo..."
redmind @wince frownmouth "Si mis oídos tuvieran ojos, estarían llorando."
    
wally @sadbrow surprised2mouth sweat "Ah... mis oídos...{w=0.5} ¿Qué fue eso? ¡¿Algún tipo de rito de iniciación?!"

grusha @wince "{i}Calm down, take it easy.{/i} Respira profundo. Está bien. {size=30}Todo está bien.{/size}"
    
show flannery furious veins:
    xpos 0.5 ypos 1.6
    ease 0.25 xpos 0.5 ypos 1.0

show whitney surprisedbrow sadmouth:
    xpos 0.75 ypos 1.6 rotate -15.0
    pause 0.75
    ease 0.25 xpos 0.65 ypos 1.0 rotate -15.0

flannery "{size=45}¡LOS VOY A MATAR!{/size}{w=0.75}{nw}"

$ BecomeNamed("Flannery")

whitney "¡Flannery!{nw}"

show flannery angry with dis:
    subpixel True
    xpos 0.5
    ease 0.5 xpos 0.4

show whitney:
    subpixel True
    xpos 0.65 rotate -15.0
    ease 0.5 xpos 0.55 rotate -15.0
    
extend @talkingmouth " ¡No aquí!{w=1.5}{nw}"

show flannery:
    subpixel True
    xpos 0.4
    ease 0.7 xpos 0.3
        
show whitney thinking with dis:
    subpixel True
    xpos 0.55 rotate -15.0
    ease 0.7 xpos 0.45 rotate -15.0

whitney @talking2mouth "¡Unf!{w=1.0}{nw}"

show flannery:
    subpixel True
    xpos 0.3
    ease 0.5 xpos 0.2
        
show whitney surprisedbrow sadmouth with dis:
    subpixel True
    xpos 0.45 rotate -15.0
    ease 0.5 xpos 0.35 rotate -15.0
    
whitney @talking2mouth "Amiga, ¡deberías dejar de comer tantas Galletas Lava!"

show flannery:
    subpixel True
    xpos 0.2 
    ease 0.8 xpos -0.3
        
show whitney thinking with dis:
    subpixel True
    xpos 0.35 rotate -15.0
    ease 0.8 xpos -0.15 rotate -15.0
        
show hilbert with dis:
    xpos 1540
    ease 0.5 xpos 1540
    
pause 0.5

hide flannery
hide whitney

hilbert @talkingmouth ".{w=0.25}.{w=0.25}.{w=0.6}{nw}"

show hilbert angry

extend @talkingmouth " Inténtalo de nuevo."

hide hilbert angry
with moveoutright

show sabrina:
    xpos 0.5 ypos 1.8
    ease 1.5 xpos 0.75 ypos 1.0

pause 2.5 

sabrina neutralpowered poweredbrow "[ellipses]"

show sabrina neutralpowered poweredbrow:
    xpos 0.75 alpha 1.0
    ease 1.5 xpos 1.5 alpha 0.0

$ renpy.pause(1.75, hard=True)

show orientation
with vpunch

hide sabrina

roxanne @angry "{size=44}¡Vamos, estamos con el tiempo justo! ¡MUÉVANSE!{/size}"

red @talking2mouth "Agh. Solo conocí a Roxanne por un momento, pero ahora mismo no me está cayendo precisamente bien."

show ethan sad:
    ypos 2.0 xpos 0.5 rotate 10.0
    ease 2.0 ypos 1.2 xpos 0.75 rotate 10.0

pause 1.0

$ ethanmisname = False

ethan "¿Quién es... Roxanne?"

$ ethanmisname = True

show roxie_orientation behind ethan with dis

pause 1.0

red @talkingmouth "Es la chica que está con el micrófono."

show ethan closedbrow sadmouth:
    ypos 1.2 xpos 0.75 rotate 10.0
    ease 2.0 ypos 2.0 xpos 0.75 rotate 0.0

ethan "Ohhhhh..."

window hide

show calem thinking:
    ypos 2.0 xpos 0.65
    ease 2.0 ypos 1.2 xpos 0.65

calem @talkingmouth "Hay mejores lugares para dormir una siesta antes que el suelo, ¿sabes?"

hide ethan

calem @talking2mouth "Vamos, toma mi mano."

show calem:
    ypos 1.2 xpos 0.65 rotate 0.0
    ease 1.0 ypos 1.4 xpos 0.65 rotate 10.0
    pause 1.0
    ease 1.0 ypos 1.0 xpos 0.65 rotate 0.0

show ethan:
    ypos 2.0 xpos 0.75 rotate 10.0
    pause 2.0
    ease 1.0 ypos 1.0 xpos 0.75 rotate 0.0

pause 3.0

ethan @happy "¡Gracias, Kallen!"
calem @closedbrow talkingmouth "Bueno, al menos es mejor que Calamari."
calem @surprisedbrow frownmouth "[ellipses]"

pause 1.0

show calem:
    xpos 0.65
    ease 0.25 xpos 0.25

calem smilemouth @sadbrow talkingmouth "Necesito mi espacio personal, por favor."
ethan @surprised "¿Eh? Oh, ah, claro."

show brendan angrybrow frownmouth:
    xpos 0.5 ypos 2.0
    ease 0.25 xpos 0.6 ypos 1.0

show may angrybrow frownmouth:
    xpos 0.5 ypos 2.0
    ease 1.0 xpos 0.4 ypos 1.0

brendan @talking2mouth "¿Cual era la gran idea? ¡¿Reventarnos los oídos?!"
may @angrybrow talking2mouth "¡En serio! ¿Sólo era para llamar nuestra atención? ¡Es más ruidosa que un Loudred!"
ethan @happy "¡Hey, a ese sí lo conozco!"
calem @surprisedbrow frownmouth "[ellipses]"
calem @talkingmouth "Muy bien hecho."

show roxie_orientation:
    zoom 1.0 xpos 0 ypos 0 xanchor 0 yanchor 0
    ease 5.0 zoom 1.1 xpos -80 ypos 0

stop music fadeout 1.5
    
$ renpy.music.play("Audio/Music/Hoenn_Start.ogg", channel='music', loop=None, fadein=1.5, tight=None)
$ renpy.music.queue("Audio/Music/Hoenn_Loop.ogg", channel='music', loop=True, tight=None)

roxanne @happy "¡Buenas noches a nuevos amigos!{w=4.0}{nw}"

show roxspeech with Dissolve(2.0):
    subpixel True
    zoom 1.25 xalign 0.5
    ease 40.0 zoom 1.0

roxanne uniform @talkingmouth "Soy Roxanne, y para comenzar, quiero agradecer al personal de la academia por permitir que el consejo organice este evento especial."
roxanne @closedbrow talkingmouth "Espero que todos aprovechen esta ocasión al máximo y me permitan darles oficialmente la bienvenida a este prestigiosa institución."
roxanne @happy "Todos...{w=0.5} bienvenidos a la Academia Kobukan de Artes y Ciencias Avanzadas Pokémon."
roxanne @teachingmouth "Aunque llamemos a este evento una orientación, les pido paciencia en esta asamblea inicial antes de que puedan volver a conocerse o atender sus asuntos personales."

redmind @thinking "Toca acomodarse.{w=0.5} Esto va a ser uno de esos discursos largos y que curan el insomnio."

roxanne @talkingmouth"Lo primero que quiero mencionar es que espero que todos hayan conseguido reservar su propia habitación en una de las tres residencias estudiantiles."
roxanne @talking2mouth "Actualmente, nos encontramos en la {color=#0048ff}Residencia Ancestral{/color}, y las otras dos son, la {color=#0048ff}Residencia Elemental{/color} y la {color=#0048ff}Residencia Umbral{/color}, las cuales están ubicadas al este y al oeste, respectivamente."
roxanne @teachingmouth "Otro tema importante es el itinerario academico que tendran durante el resto del año."
roxanne @angrybrow talkingmouth "Todos ustedes seguirán un horario preestablecido de seis períodos al día.{w=0.5} Presten mucha atención, porque esta será su rutina durante el próximo año."

hide roxie_orientation
hide calem
hide ethan
hide may
hide brendan

red @closedbrow talking2mouth "...{w=0.5} Todo esto ya estaba en la página web."

calem @happy "Aún así, puede ser un buen repaso para los que llegaron menos informados."
    
roxanne @closedbrow talkingmouth "{color=#0048ff}El primer período de cada día será una clase general{/color}, que durará dos horas. Aquí se cubrirán las competencias básicas con su profesor asignado."

brendan @surprised "¡¿Dos horas?!"
calem @closedbrow talking2mouth "Lo sé. Dos horas son apenas suficientes para cubrir todo el material."
may @sad "Especialmente cuando solo tenemos un año..."
ethan @surprised "Eh... chicos, no creo que se refería a eso."
red @happy "Una vez pasé dos horas en el Monte Moon sin repelentes. No puede ser peor que eso."
ethan @angry "Oh dios, ¿Zubat por todas partes, verdad? ¿Sabías que son una especie invasora? Kanto tiene mucho que explicar por dejarlos cruzar la frontera y arruinar Johto."
red @confused "¿Y qué se supone que hagamos? ¿Poner una red gigante?"

roxanne @talkingmouth "{color=#0048ff}Después de la clase general, tendrán una hora de una asignatura electiva de tipo Pokémon{/color} a su elección.{w=0.5} Podrán seleccionar {color=#0048ff}{b}dos{/b} de los dieciocho tipos conocidos{/color} para enfocarse cada día."

ethan @surprised "¡Whoa, esperen un segundo!"
ethan @confused "¿Nos estamos especializando en dos tipos de Pokémon?{w=0.5} ¿Solo dos de dieciocho?"
calem @talkingmouth "No exactamente. Podemos elegir siempre los mismos dos tipos si queremos, pero también podemos cambiar entre ellos cuando deseemos."
brendan @surprised "¡¿Eh?! ¿Cómo funciona eso?"
calem @talkingmouth "Gracias a la alta proporción de profesores por alumno en Kobukan, los instructores pueden ajustar el plan de estudios según el nivel de cada estudiante, incluso si nunca tomaron dicha clase antes."
red @talkingmouth "Esa es otra ventaja del plan de estudios único que posee Kobukan. Al ser de solo un año tenemos que trabajar tres veces más duro y rápido que otras academias, pero podemos personalizar nuestra educación a nuestro gusto."
redmind @thinking "Sé que muchos estudiantes de Kobukan que llegaron a destacar se enfocaron en dos o tres electividades. Dominar los dieciocho tipos en un año parece imposible."
redmind @frownmouth angrybrow "Incluso un estudiante excepcional solo podría manejar {color=#0048ff}seis{/color} electivas."

show roxspeech:
    ease 0.75 zoom 1.0

roxanne @talkingmouth "Además de sus clases electivas, también tendrán un período de gimnasia y almuerzo."
roxanne @closedbrow teachingmouth "Luego, tendran un ultimo periodo con su profesor de clases generales hasta las 3 PM."
roxanne @talkingmouth "Aquellos que participen en investigaciones o actividades extracurriculares podrán usar los edificios del campus."
roxanne @sadbrow talking2mouth "Como es tradición, habrá un toque de queda. Los estudiantes que sean vistos fuera de sus dormitorios después de las 8 PM recibirán sanciones disciplinarias graves."

show roxspeech:
    zoom 1.0

red @surprised "¡¿8 PM?!{w=0.5} Eso es--"

show roxspeechmad with dis:
    zoom 1.0 xalign 0.5

brawly uniform @angrybrow talking2mouth "¡Sí, 8 PM! ¡Es demasiado temprano! El año pasado fue un {i}infierno{/i}, y seguir con esto es ridículo. ¡La noche apenas {i}empieza{/i} a las 8 PM!"

roxanne @angrybrow talking2mouth "{b}¡Ajem!{/b} Y ni piensen en escaparse.{w=0.5} Hay cámaras de seguridad en cada habitación y en cada edificio."

roxanne @closedbrow talking2mouth "La única forma de salir en ese horario es si tienen un permiso especial de un miembro del personal, del consejo estudiantil o de alguien autorizado para otorgarlo. No habra excepciones a--"

brawly @angrybrow talking2mouth "Sí, sí, ya sé lo de las cámaras. ¡Pero esto es una tontería! ¿Se supone que los estudiantes debemos quedarnos sentados toda la noche...? {b}¡¿Estudiando?!{/b} "

falkner uniform @talking2mouth "Todos debemos seguir las reglas, Brawly."

brawly @sad "O sea... sí, sé que ya lo intentamos, pero podríamos hablar con Drayden otra vez y tal vez esta vez--"

roxanne @angry "¡¿Podrías {b}callarte{/b} de una vez?! ¡Estamos en medio de una asamblea! "

roxanne @closedbrow angrymouth "Si tienes problemas con la manera en que se administra esta academia, ventilar nuestros trapos sucios en medio del auditorio no es la forma de resolverlo. ¡Ten algo de decoro!"

redmind @sad "Pobre Brawly... Que lo reprendan así enfrente de todo el auditorio..."

falkner @closedbrow talkingmouth "Roxanne, tu discurso."

roxanne @angrybrow talking2mouth "Cuando esto termine, tú y yo vamos a tener una pequeña charla."
    
show roxspeechmad:
    alpha 1.0
    ease 0.33 alpha 0.0

roxanne @closedbrow frownmouth "{i}Ejem{/i}... ¿En donde estaba?"
roxanne @happy "¡Ah, sí! Como decía, es un privilegio formar parte de esta gran institución a la que llamamos la Academia Kobukan. {w=0.4} Ahora tienen la oportunidad de sus vidas para abrir una nueva puerta en sus vidas."

calem @surprised "¿Pudo cambiar toda su personalidad de un momento a otro?{w=0.5} Eso es impresionante."

roxanne @talkingmouth "Solo trabajando juntos podremos alcanzar nuestras metas y desarrollar nuestros talentos. {w=0.5} Pero, al final, dependerá de cada uno de ustedes encontrar su propio camino y tomar el destino en sus manos."

$ PlaySound("Big Applause.ogg")

roxanne @happy "Y con eso, ¡les doy la bienvenida oficialmente a la Academia Kobukan!"

window hide

hide roxspeechmad

show roxspeech:
    alpha 1.0
    ease 2.0 alpha 0.0

show orientation:
    zoom 1.1 xpos -80 ypos 0 xanchor 0 yanchor 0
    ease 4.0 zoom 1.0 xpos 0 ypos 0   

$ renpy.pause(2.5, hard=True)

roxanne @closedbrow teachingmouth "¡Que tengan un excelente resto del día y no olviden completar sus inscripciones!"

show brendan happy with dis:
    xpos 0.2 xzoom -1

show may happy with dis:
    xpos 0.4

show ethan happy with dis:
    xpos 0.6

show calem happy with dis:
    xpos 0.8 xzoom -1
    
pause 1.0

show brendan -happy with dis
show may -happy with dis
show ethan -happy with dis
show calem -happy with dis

calem @talkingmouth "Bueno, ¿qué les pareció?"

brendan @talking2mouth "¿Qué cosa? ¿El discurso?"

calem @closedbrow talking2mouth "Bueno, supongo que eso también."
calem @talkingmouth "Pero me refería a la parte del cronograma que tendremos por el resto del año."
calem @closedbrow talkingmouth "Ya hemos resuelto todo sobre los dormitorios, así que no hay nada más que hacer en ese aspecto."

calem @talking2mouth "Será difícil elegir solo dos electivas de tipo entre dieciocho. {color=#0048ff}Y tendremos diferentes instructores y compañeros de clase según los tipos que elijamos...{/color}"
calem @talkingmouth "Aunque tenemos la libertad de cambiar entre electivas en cualquier momento, muchos estudiantes optan por enfocarse en dos o tres tipos durante todo el año."

redmind @thinking "Eso puede funcionar para otros estudiantes, pero si quiero convertirme en un campeón, {color=#0048ff}probablemente debería cambiar entre electivas dependiendo del tipo de Pokémon que quiera entrenar.{/color}"

calem @closedbrow talkingmouth "Nos espera una gran decisión cuando volvamos a nuestra habitación. Deberíamos ocuparnos de eso primero."

brendan @happy "¡Genial!"
brendan @talking2mouth "Te diré algo, [first_name], ¡voy a elegir las mismas electivas que tú!"
brendan @happy "Así seremos compañeros de clase también. ¡Será genial!"

red @surprisedeyes surprisedeyebrows sadmouth "Yo.{w=0.25}.{w=0.25}."

may @happy "Imaginen si también les toca el mismo profesor de aula.{w=0.5} ¡Parecerían una pareja!"

red @closedbrow talkingmouth "No estoy seguro de cómo sentirme al respecto."

brendan @happy "¡Es broma, hombre! Solo estoy jugando."
brendan surprisedbrow frownmouth @neutralbrow talking2mouth "Aún no tengo decidido qué electivas voy a tomar, así que si al final terminamos en las mismas, ¡será pura coincidencia!"

may @talkingmouth "Cariño, ¿aquí no enseña el campeón Wallace en esta academia? Creo que da clases de tipo Agua."

brendan -surprisedbrow -frownmouth @happy "¡¿Deberas?! Bueno, eso ya decide una de mis opciones."

may @happy "[first_name], yo voy a elegir las clases de tipo Fuego, así que si también decides tomar esa, al menos tendrás una cara conocida en la clase."

show may surprisedbrow frownmouth
show calem surprisedbrow frownmouth
show brendan surprisedbrow frownmouth 
with dis

red @closedbrow talking2mouth "Creo que probablemente ire rotando entre electivas."

ethan @surprised "¡¿Estas hablando en serio?! ¡Escuché que eso es bastante difícil de hacer bien!"

red @sadbrow talkingmouth "Sí, eso he oído, pero casi todos los Campeones que salieron de Kobukan lo hicieron. No sería el primero en intentarlo."

show may -surprisedbrow -frownmouth
show calem -surprisedbrow -frownmouth
show brendan -surprisedbrow -frownmouth 
with dis

ethan @happy "Vaya. Bueno, ¡no voy a decirte que no lo hagas! Yo pensaba hacer lo mismo."

red @surprised "¿En serio?"

ethan @talkingmouth "Sí. La única desventaja es que, supongo, si ambos estamos cambiando de electivas, probablemente no tendremos muchas clases juntos."

red @happy "Bueno, cuando coincidamos, las disfrutaremos mucho más." 

brendan @talkingmouth "¿Quieres venir con nosotros a elegir las electividades, May?"

may @sadbrow happymouth "Voy a pasar, chicos,{w=0.5}{nw}"
extend @happy " Ya quedé en verme con Leaf más tarde."

red @talkingmouth "¿Leaf?"

brendan @talking2mouth "Es una de sus compañeras de cuarto."
brendan @talkingmouth "¡Las conocí a todas antes de llegar a nuestra habitación! {nw}{w=0.5}"
extend @sadbrow talking2mouth "Eh...{w=0.5} Uh...{w=0.5} ¿cómo eran sus nombres?"

may sadbrow frownmouth @talking2mouth "...{w=0.5} ¿No estabas escuchando?"

brendan sadbrow @talkingmouth "N-no, ¡claro que sí!{w=0.5} Es solo que... eh, soy muy malo con los nombres.{w=0.5} ¿Verdad, Erick?"

ethan @angrybrow frownmouth "[ellipses]"

show brendan angrymouth closedbrow sweat with dis

ethan @angrybrow talking2mouth "Me llamo Ethan. Y es muy grosero de tu parte equivocarse de nombre, Brendan."

show brendan -angrymouth -closedbrow -sweat
show may -sadbrow -frownmouth
with dis

calem @closedbrow talking2mouth "Volvamos al tema. May, ¿cuáles son los nombres de tus compañeras de cuarto?"

may @closedbrow talkingmouth "Bueno... estamos Leaf, yo, y una chica de Teselia llamada Hilda--"

show orientation with hpunch

show brendan surprisedbrow frownmouth with dis:
    xpos 0.2 xzoom -1
    ease 0.5 xpos 0.5 xzoom 1

show may surprisedbrow frownmouth with dis:
    xpos 0.4
    ease 0.5 xpos 0.6

show ethan surprisedbrow frownmouth with dis:
    xpos 0.6
    ease 0.5 xpos 0.7

show calem surprisedbrow with dis

show hilbert angrybrow:
    xpos -0.5 xzoom -1
    ease 0.25 xpos 0.2

hilbert @angry "¡¿Qué?! ¡¿Hilda?!"

pause 1.0

calem @closedbrow talkingmouth "Por favor, espacio personal."

show calem:
    xpos 0.8
    ease 1.0 xpos 0.1

pause 1.0

calem @frownmouth "[ellipses]"
calem @sad "No importa, esto es mucho peor."

show calem:
    xpos 0.1
    ease 1.0 xpos 0.8

pause 1.0

hilbert @angry "¡¿Dijiste Hilda?! ¡Respóndeme!"

show brendan:
    xpos 0.5
    ease 0.5 xpos 0.4

brendan angrybrow @angry "Oye, tranquilo viejo."
may sadbrow @sad "S-sí... Hilda es su nombre. Eh, ¿la conoces?"
hilbert sadbrow "[ellipses]"
hilbert @sadbrow talkingmouth "Probablemente no, es un nombre común."
hilbert @closedbrow talkingmouth "Olvídenlo."

show hilbert:
    xpos 0.2
    ease 1.0 xpos -0.5

calem @closedbrow talkingmouth "...{w=0.5} Qué tipo tan maleducado. Que esto sirva como recordatorio de cómo {i}no{/i} reaccionar. May, por favor, continúa."

may @sadbrow talkingmouth "E-eh... después de Hilda, hay una chica de Kalos llamada Serena--"

show brendan surprisedbrow frownmouth with dis:
    xpos 0.4 xzoom 1
    ease 0.5 xpos 0.2 xzoom -1

show may surprisedbrow frownmouth with dis:
    xpos 0.6
    ease 0.5 xpos 0.3

show ethan surprisedbrow frownmouth with dis:
    xpos 0.7
    ease 0.5 xpos 0.4

show calem surprisedbrow with dis

show orientation with hpunch

calem @surprised "¡¿QUÉ?!"

ethan @confused "¿Y ahora qué pasa?"

calem @sad "¡Por favor, descríbela!"

show ethan surprisedbrow frownmouth with dis

may @closedbrow blush talkingmouth "Uh, bueno... tiene la piel perfecta, un gran busto, piernas largas--"
calem sadbrow @sad "¿Lentes de sol? ¿Usa lentes de sol?"

show brendan happy with dis

may @happy "¡Oh, sí! La hacen parecer un Hoothoot. Se rió cuando se lo dije."

calem @closedbrow sadmouth "No puede ser. {size=30}Ella no debería estar aquí...{/size}"

show may sadbrow frownmouth with dis
show brendan sadbrow frownmouth with dis
show ethan sadbrow frownmouth with dis

pause 1.0

red sadeyebrows sadeyes talking2mouth "Oye, Calem. ¿Estás bien?"

calem @talkingmouth "Sí... excepto por la horrible realización de que tomé la decisión más difícil de mi vida... para nada."

ethan @confused "...{w=0.5} ¿En español?"

calem @closedbrow talkingmouth "Uno a menudo encuentra su destino en el camino que toma para evitarlo."

ethan @unamusedbrow talking2mouth "Creo que ninguno de nosotros sabe qué significa eso, Calamari."

show brendan surprisedbrow frownmouth with dis:
    xpos 0.2 xzoom -1
    ease 1.0 xpos 0.5 xzoom 1

show may surprisedbrow frownmouth with dis:
    xpos 0.3
    ease 1.0 xpos 0.6 ypos 1.0 rotate 0

show ethan surprisedbrow frownmouth with dis:
    xpos 0.4
    ease 1.0 xpos 0.7

show calem closedbrow with dis

show serena:
    xpos -0.5
    ease 1.5 xpos 0.2

serena @talkingmouth "Discúlpame. ¿Eres tú, Calem?"

$ BecomeNamed("Serena")

redmind @surprisedbrow frownmouth "{cps=*0.2}...{/cps}Bueno, ciertamente encaja con la descripción que dio May, por vaga que fuera. Con esas gafas de sol y ese acento, estoy bastante seguro de que es Serena."

calem -closedbrow @talkingmouth "Oh, hola, Serena."

show ethan closedbrow:
    xpos 0.7
    ease 10.0 xpos 1.5

show may:
    xpos 0.6 rotate 0
    ease 3.0 xpos 0.1 
    pause 2.0
    "may blush flirtbrow poutmouth"
    ease 2.0 rotate -5.0 ypos 1.2
    pause 1.0
    ease 1.0 xpos -0.5

show brendan:
    xpos 0.5
    ease 2.0 xpos -0.5
    pause 5.0
    ease 1.0 xpos 0.05
    pause 1.0
    ease 1.0 xpos -0.5

calem @closedbrow talkingmouth "Uh..."
calem @happybrow talkingmouth "No tenía idea de que te habías inscrito aquí."

serena @talkingmouth "Lo mismo digo.{w=0.5}{nw}" 
extend @happy " Qué agradable serendipia."
serena @talkingmouth "En cualquier caso, ya que nos hemos encontrado por pura casualidad, no desperdiciemos la oportunidad. ¿Estás ocupado?"

pause 1.0

narrator "Calem te señala vagamente con la mano."
    
show serena at getcloser:
    xpos 0.2

pause 1.0

serena @sadbrow talkingmouth "¿Oh? ¿Y quién eres tú?"

red @happy "¿Yo? Oh, eh, soy [first_name], y..."

menu:   
    "Con esas gafas, seguro te confunden a menudo con un Hoothoot.":
        show calem surprisedbrow with dis
        show serena surprisedbrow frownmouth with dis

        pause 2.0
        
        redmind @wince frownmouth "Esto fue una apuesta arriesgada, espero que haya salido bien."

        show calem -surprisedbrow smilemouth with dis

        serena @closedbrow frownmouth "Je... je..."

        redmind -talkingmouth -frownmouth @confusedbrow frownmouth "Una de dos, o está llorando o está riéndose."

        serena @closedbrow frownmouth "Je... je....{w=0.5}{nw}"
        extend @happy " {w=0.5}¡Jajajajaja!"
        show serena happy with dis 
        $ ValueChange("Serena", 1, 0.2)

        serena @happy "Es la segunda vez que lo oigo hoy. Si que me parezco a uno, ¿no?"
        serena @talkingmouth "¿Me creerías si te dijera que fueron un regalo de mi madre?"
        serena @happy "Todos me dicen que se ven algo ridículas, pero a mí me parecen adorables."

        redmind @closedbrow sweat "Menos mal que le di al blanco..."
        
    "Es un placer conocerte.":          
        red @happy "Es un placer conocerte."

        serena @happy "Y lo mismo digo, sin duda."

pause 1.0

serena @surprised "¡Oh, vaya, miren la hora!"

show serena at getfurther:
    xpos 0.2

serena @sadbrow talkingmouth "Tengo que irme. Voy a hacer algunos  con unas chicas que conocí hoy."

serena @happy "¡Pero me alegra mucho verte aquí!"
serena @happybrow talkingmouth "¡Pongámonos al día más tarde!"

calem @happy "Por supuesto, nos vemos."

hide serena with dis
    
pause 1.0

show calem sadbrow with dis

show calem:
    xpos 0.8
    ease 0.5 xpos 0.5

stop music fadeout 3.0

red @talkingmouth "Y se fue."

pause 1.0

red @angrybrow talking2mouth "... Y al parecer, también el resto."

pause 1.0

red @sadbrow talking2mouth "Oye, en serio, Calem, ¿te encuentras bien?"
calem @sadbrow talking2mouth "[ellipses] No, pero lo estaré."

pause 1.0

red -angrybrow -frownmouth @talkingmouth "Está bien. Pero, ya sabes, estoy aquí para hablar. Tal vez necesitemos compartir un almuerzo o dos, conocernos mejor y todo eso, pero puedes {i}confiar en mí{/i}."

calem @happy "Gracias por tu preocupación. Te aseguro que mi amistad normalmente no involucra tanto drama."

$ renpy.music.queue("Audio/Music/SoaringIllusions.ogg", channel='music', loop=True, fadein=3.0, tight=None)

red @talkingmouth "¿Es una amiga tuya?"

calem @talkingmouth "Podría decirse que sí."
calem @closedbrow talkingmouth "Éramos vecinos, como ya habrás podido deducir. Pero no sabía que se había inscrito aquí, me pregunto por qué.{w=0.25}.{w=0.25}."

calem @surprised "Ah.{w=0.75}{nw}"
extend smilemouth @talkingmouth happybrow " Por cierto, ya que vamos a ser compañeros de dormitorio, ¿qué te parece si intercambiamos nuestros números de contacto? Podría ser útil en caso de cualquier emergencia."

red @talkingmouth "Oh, sí. Buena idea."

$ BecomeContacted("Calem")

calem @talkingmouth "Muy bien. Parece que nos han 'abandonado', así que voy a resolver unos asuntos."
calem @closedbrow talking2mouth "Tengo que ocuparme de algo en la oficina de inscripciones. Algo sobre mis cartas de recomendación, ssi no recuerdo mal."
calem @talkingmouth "Sospecho que otros estudiantes estarán allí por otras razones, así que prefiero ir antes de que cierren."

red @talkingmouth "Vale, genial. ¿Necesitas que te acompañe?"

calem @talking2mouth "No, está bien."
calem @happy "Creo que ese estudiante andrógino del consejo estudiantil nos recomendó ir al vestíbulo a relacionarnos. ¿Por qué no te diriges hasta allí?"
calem @closedbrow talking2mouth "Nunca sabes qué conexiones podrías hacer."

red @playfuleyes confusedeyebrows talkingmouth "Oh, ¿así que se trata solo de hacer contactos que puedas aprovechar más tarde?"

calem @sadbrow talkingmouth "¿Piensas tan poco de mí? No soy Hilbert, sabes. No, creo que formar lazos con otras personas es genuinamente divertido. Independientemente de las ventajas que puedan traer."

red @happy "Solo bromeo, sé que no eres así. En fin, ¿nos vemos después?"

calem @happy "Sí, llámame si necesitas algo."
calem smilemouth @talkingmouth "{i}Au revoir.{/i}"

show calem:
    xpos 0.5
    ease 1.0 xpos 1.5

pause 2.0

redmind @thinking "Muy bien, ¡hora de encontrar el vestíbulo! Veamos... si empiezo a correr en una dirección al azar, entonces..."

show hall_A2b at sepia with dis
show flashback with dis

$ renpy.pause(1.0, hard=True)

show leaf flirtbrow angrysmilemouth at sepia, dissolvein behind flashback

pause 1.5

leaf @talking2mouth "¡Hey! ¿Te di ese folleto para nada? ¡Úsalo, tontito!"

show blank with splitfade

hide leaf
hide hall_A2b
hide flashback
hide blank with dis

redmind "Genial, ahora tengo a dos muejeres gritándome en la cabeza. Está bien, ¡usaré el folleto!"
red surprisedbrow frownmouth @surprisedbrow "[ellipses]"
redmind thinking "Vaya, esto es en realidad súper fácil de seguir. Tal vez esa chica tenía razón."
red angrybrow happymouth "¡Muy bien, es hora de ir al vestíbulo!"

$ renpy.pause(1.0, hard=True)

show blank2:
    alpha 1.0
    ease 1.5 alpha 0.0

show hall_B behind blank2:
    xpos 960 xalign 0.5 ypos 1080 yalign 1.0 zoom 0.9
    ease 0.5 zoom 0.95

$ renpy.pause(0.5, hard=True)

show hall_B:
    alpha 1.0 zoom 0.95
    ease 1.2 zoom 1.0
    block:
        ease 0.03 xpos 940 ypos 1060
        ease 0.03 xpos 980 ypos 1100
        ease 0.03 xpos 960 ypos 1080
        repeat 2

$ showredonly = True

show misty surprisedbrow frownmouth:
    xpos -0.5 zoom 1.0 ypos 1.0
    pause 1.1
    ease 0.3 zoom 1.5 ypos 1.3 xpos 0.5
    ease 0.7 rotate 45.0 ypos 3.0

$ renpy.pause(1.2, hard=True)

stop music fadeout 1.0

$ PlaySound("Body Crash.ogg")
$ renpy.pause(0.4, hard=True)

hide blank2

misty @talkingmouth "{size=48}¡HEY! ¡MIRA POR DÓNDE VAS!{/size}"
    
red surprisedbrow frownmouth @surprised "¿Uh?"

queue music "Audio/Music/CeruleanCity.ogg"

$ showredonly = False

show misty angry:
    ypos 3.0 rotate 45.0 zoom 1.0
    ease 1.5 ypos 1.0 rotate 0.0
        
misty @talkingmouth "¡No me vengas con '¿uh?'! ¿Y por qué pones esa cara de idiota?"
misty @talkingmouth "¿Eres sordo o simplemente despistado? No te quedes ahí parado mirándome, al menos admite que no estabas prestando atención,{w=0.25} ¡porque claramente no lo estabas!"

menu:
    "Lo siento mucho.":
        show misty surprisedbrow -angrymouth with dis
        red @talkingmouth "Iba con prisa y doblé la esquina demasiado rápido. ¿Estás bien?"      
            
        misty @closedbrow talking2mouth "{i}Suspiro.{/i}"
        
        misty @talkingmouth "Estoy bien."
        
        misty @angry "¡Estoy bien!{w=0.6} ¡Todo está bien!"
        misty @closedbrow talkingmouth "Solo intenta no atropellar a más chicas en el camino a... {w=0.5}{nw}"
        extend @sadbrow talkingmouth "... donde sea que vayas."
        
        hide misty with dis
            
        stop music fadeout 2.0
        
        redmind @thinking "Genial. Me grita, se desquita conmigo y luego se va sin siquiera decir su nombre. Muy cortés de su parte."
        redmind @sad2eyes frownmouth "Agh, rebajarme así me dejó un mal sabor de boca..."

    "¡Tú chocaste conmigo!":
        show misty surprisedbrow frownmouth with dis
        red @talking2mouth angrybrow "Si dejaras de insultarme por un segundo, tal vez te des cuenta de que esto fue completamente tu culpa."

        $ ValueChange("Misty", -1, 0.5)

        misty "You...{w=0.7}{nw}"
        extend angry " ¡IDIOTA!"
        
        show misty angry:
            zoom 1.0 ypos 1.0 xpos 960
            ease 0.5 zoom 1.25 ypos 1.2 xpos 720
        
        $ renpy.pause(1.0, hard=True)
        $ PlaySound("Slap.ogg")
        pause 0.1
        
        show misty angry:
            xpos 720 ypos 1.2 zoom 1.25 rotate 0
            ease 0.1 xpos 520 ypos 1.1 zoom 1.33 rotate -3
        
        show hall_B at hall_move1
        
        pause 1.0
        
        show misty angry:
            xpos 520 ypos 1.1 zoom 1.33 rotate -3
            ease 0.2 xpos 360 ypos 1.0 zoom 1.25 rotate 0
        
        show hall_B at hall_move2
        
        redmind @closedbrow frownmouth "Auch."
        
        show misty angry:
            zoom 1.25 xpos 360 ypos 1.0 alpha 1.0
            parallel:
                pause 0.5
                ease 0.5 alpha 0.0
            parallel:
                ease 1.0 xpos -200
        
        stop music fadeout 2.0
        
        pause 1.0
        
        red @angry "{size=40}¡¿Alguien te ha dicho alguna vez que no te tomas las críticas demasiado bien?!{/size}"

    "Fue culpa mía, pero baja el tono.":
        show misty surprisedbrow -angrymouth with dis
        red @talkingmouth "Solo estaba pensando qué decir. Así que, vale, lo siento, ¿de acuerdo? Pero no hace falta tratarme así. Ahora, ¿estás bien?"
        
        $ ValueChange("Misty", 1, 0.5)        
            
        misty @closedbrow talking2mouth "{i}Suspiro.{/i}"
        
        misty @talkingmouth "Estoy bien."
        
        misty @angry "¡Estoy bien!{w=0.6} ¡Todo está bien!"
        misty @closedbrow talkingmouth "Solo intenta no atropellar a más chicas en el camino a... {w=0.5}{nw}"
        extend -closedbrow -angrymouth @angry " donde sea que vayas."
        
        hide misty with dis
            
        stop music fadeout 2.0
        
        redmind @unamusedbrow frownmouth "Genial. Me grita, se desquita conmigo y luego se va sin siquiera decir su nombre. Muy cortés de su parte."

pause 1.0

$ renpy.music.play("Audio/mediumcrowdloop.ogg", channel='crowd', loop=True, fadein=1.0)

scene lounge:
    alpha 0.0 zoom 1.0
    ease 3.0 alpha 1.0 zoom 1.1 ypos -100

show hall_B behind lounge

$ renpy.pause(2.5, hard=True)

redmind "Huh, parece que la mayoría de la gente está discutiendo sobre la orientación."
redmind "Imagino que muchos están inscribiendose a sus electividades y organizando sus horarios."

show lounge:
    zoom 1.1 ypos -100 alpha 1.0
    ease 0.75 zoom 1.0 ypos 0

redmind "No veo a mis compañeros de habitación por aquí...{w=0.5} pero está bien. De todos modos, creo que me gustaría empezar una conversación con alguien nuevo."

show lounge:
    zoom 1.0
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

stop music fadeout 1.0
$ cap_player = first_name.upper()
"{color=#3110dd}???{/color}" "\"{size=45}¡¡¡[cap_player]!!!{/size}\""

red happy "¡Vaya! ¡Ese tipo sí que sabe cómo llamar la atención!"

show lounge:
    yalign 1.0 xalign 0.5

show blue angry with dis:
    xpos 720

pause 0.5
play music "Audio/Music/RivalTune.ogg" noloop
$ renpy.music.queue("Audio/Music/Show Me Around.ogg", channel='music', loop=None, fadein=1.0, tight=None)
    
$ renpy.pause(0.5, hard=True)

red unamusedbrow talking2mouth "Oh, debí haberlo sabido."

blue @talkingmouth "¡¿Qué demonios haces siguiéndome?!{w=0.25} Espera, ¡¿cómo demonios entraste aquí?!"

show blue:
    zoom 1.0 ypos 1.0
    ease 0.5 zoom 1.25 ypos 1.1 xpos 600

blue @surprisedbrow talkingmouth "¡¿Te colaste solo para seguirme?! Eso es algo muy rarito de tu parte."
blue @surprisedbrow talkingmouth "Alguien me dijo que vio a un tipo que se parecia a ti en este lugar. Pensé que estaba equivocada... ¡pero realmente estás {i}muy{/i} desesperado!"
blue frownmouth angrybrow @angry "¡Será mejor que te largues antes de que llame a seguridad para que te saquen a patadas!"

red @talkingmouth "Por favor...{w=0.5} Tengo una carta de aceptación, al igual que tú, [blue_name]."

show blue:
    zoom 1.25 ypos 1.1 xpos 600
    ease 0.5 zoom 1.0 ypos 1.0 xpos 720

blue sweat @surprisedbrow angrymouth "¿Tú...{w=0.5} recibiste una carta de aceptación?"

show blue surprisedbrow frownmouth with dis
red @closedbrow sweat "Sí, me llego el mes pasado.{w=0.5} De hecho, al principio pensamos que era tuya, pero--"

show blue angry:
    zoom 1.0 ypos 1.0
    ease 0.25 zoom 1.25 ypos 1.1 xpos 600

blue -sweat @angrybrow talking2mouth "¡Y una mierda, déjame verla!"
    
show letter at itemgive

red @upbrow talking2mouth "Seguro, si eso te hace sentir mejor."
red @angrybrow talking2mouth "... Pero ni se te ocurra doblarla en lo más minimo."

hide letter with dis

pause 1.5
    
blue -angry surprisedmouth ".{w=0.4}.{w=0.4}."

red -angrybrow talking2mouth "¿Hola? Tierra llamando a [blue_name]. ¿Satisfecho?"

blue surprisedbrow frownmouth @surprised "[ellipses]"

show blue:
    zoom 1.25 ypos 1.1 xpos 600
    ease 0.5 zoom 1.0 ypos 1.0 xpos 720

blue sad "Esto significa que...{w=0.5} entonces, ¿por qué el abuelo...?"
blue @talkingmouth "... Esto no tiene sentido.{w=0.5}{nw}"
blue angry "... Esto no tiene sentido.{fast} ¿Por qué estás aquí? ¡Eres la última persona en el mundo que debería estar aquí!"
red angrybrow "... Y, sin embargo, aquí estoy, al igual que tú. ¿Qué dice eso de ti?"
blue @talkingmouth "Eres un completo desperdicio de espacio, es asqueroso que el abuelo te haya recomendado.{w=0.5} Seguro que solo lo hizo porque le dio lástima que no tuvieras amigos."

show blue closedbrow:
    xpos 720
    ease 0.5 xpos 500

blue @talkingmouth "Tch, hablar de esto contigo es una pérdida de tiempo."

blue angry "Pase lo que pase, solo deja de entrometerte en mi camino y no tendremos problemas, ¿capisci, [first_name]?"

blue -angry @talkingmouth "Ahora, si me disculpas, tengo mejores cosas que hacer que perder el tiempo contigo.{w=0.5}"

show blue:
    xpos 500 alpha 1.0
    ease 0.4 xpos 0 alpha 0.0

blue happybrow angrymouth "¡Me piro vampiro, perdedor!"

pause 2.0

redmind -angrybrow sad "Eso fue absolutamente miserable. Mejor voy a ver si hay alguien más con quien hablar y luego me voy a desempacar."

cheren @closedbrow talking2mouth "Disculpame."
red @talkingmouth "Oh, hola."

show cheren with dis

cheren @disappointed "En nombre de mi compañero de clase, me gustaría disculparme por su conducta inapropiada."
red @happy "¿Eh? No necesitas disculparte por [blue_name]. Él, y solo él, es responsable de cómo actúa."
cheren @sad "Aun así, tener algunos de tus primeros momentos en esta prestigiosa academia arruinados por los atroces modales de este hombre..."
red @happy "Está bien, de verdad. Sé cómo lidiar con este tipo de cosas."
red @confused "De todos modos, aprecio tu preocupación, pero, eh... ¿por qué te involucras en esto? Eres solo un estudiante normal y corriente, ¿verdad?"
cheren @talkingmouth "Por el momento. Sin embargo, tengo la intención de unirme al consejo estudiantil en un futuro cercano."
red @surprised "¿Ah, sí? Ahora que lo mencionas, tengo algunas preguntas."
red @surprised "Ya que nuestro plan de estudios dura solo un año, ¿cómo funciona el consejo estudiantil? Además, ¿cómo es posible que exista uno antes de que el año escolar haya comenzado?"
cheren @happy "¡Será un placer responder tus preguntas! Los estudiantes del año pasado pueden optar por quedarse en la academia después de graduarse."
cheren @sadmouth "Estos asumen un rol de supervisión durante varios meses, asegurándose de que la nueva camada de estudiantes pueda adaptarse." 
cheren @closedbrow talking2mouth "Sin embargo, un mes después de que comience el año, se llevara a cabo una nueva elección para determinar el consejo estudiantil de este año."
cheren @closedbrow talking2mouth "A partir de ahí, el Consejo votara internamente para decidir quién será su nuevo presidente."
red @confused "Vaya, ¿así que solo tienen un mes para iniciar una campaña y conseguir el voto de la gente?"
cheren @sad "En terminos generales, así es."
red @happy "Bueno, entonces, ¿cuáles son tus propuestas? Intenta convencer a este votante."
cheren surprisedbrow frownmouth @surprised "¿Oh? Eh... mis propuestas, sí..."

pause 2.0

red @sadeyes sadeyebrows talkingmouth "¿Estás bien?"

pause 1.0

cheren -surprisedbrow -frownmouth -surprised @disappointedbrow happymouth "{i}... Absolutamente.{/i}"

pause 1.0

cheren @angry "Mis propuestas son las siguientes: la introducción de dormitorios mixtos, aumentos salariales para el personal no académico y la derogación del absurdo toque de queda de la academia. ¡Somos adultos, después de todo!"
cheren @disappointedbrow talking2mouth "Además, los beneficios que otorga la titularidad en esta institución permiten demasiada 'creatividad' a la hora de impartir las clases. Por otro lado, el personal debe poder sindicalizarse."
cheren @closedbrow talkingmouth "En cuanto a las ayudas financieras, creo que deben repartirse entre quienes más las necesitan y no entre quienes poseen más conexiones."
cheren @angry "Y, finalmente, aquellos rumores altamente sospechosos acerca de cómo esta academia decide la admisión de sus estudiantes deben ser investigados, aclarados y, si es necesario, 'eliminados'."

redmind @surprisedbrow frownmouth "... Mierda, este tipo si que esta muy comprometido."
redmind @frownmouth closedbrow "Y creo que está investigando algo que podría causarme serios problemas a futuro."
red @confused "Tienes ideas muy ambiciosas. ¿El consejo estudiantil realmente tiene autoridad para hacer todo eso? Suena más como cosas que el personal de la academia manejaría."
cheren @closedbrow talkingmouth sweat "Ciertamente lo son, pero ¿qué es la política, sino la lucha por arrebatar el poder a quienes desean retenerlo para siempre?"
cheren @sad "Lamentablemente, lo que puedo prometer esta limitado por el alcance de mi ambición. Y muchos, al intentar abarcar más de lo que pueden, han sellado su destino con una muerte prematura."
cheren @angrybrow happymouth "Pero te aseguro que, si me eliges para el consejo estudiantil, nunca dejaré de luchar por una Academia Kobukan más igualitaria, justa y de calidad."

pause 2.0

cheren @disappointed "Oh, y también buscaré la implementación de papel higiénico de cinco capas en los baños."
cheren @upeyes talking2mouth "Es una petición muy popular entre cierto lobby, así que{cps=*0.2}..."

pause 1.0

red @happy "Bueno, tienes mi voto. ¿Cómo te llamas futuro candidato?"

$ BecomeNamed("Cheren")

cheren @surprised "¡Oh! Claro. Mi nombre es Cheren, soy de Ciudad Engobe. Esta ubicada en el suroeste de la regíon de Teselia."

red @happy "Genial, espero que tengas éxito con tu campaña."

cheren happy "Aprecio mucho tu apoyo. ¡Que tengas un buen día!"

hide cheren with dis

redmind thinking "Bueno, parece agradable, pero me preocupa lo que pueda descubrir. Aunque... considerando lo que dice que quiere hacer, seguramente no avanzará lo suficiente como para encontrar algo sobre mí..."
redmind sadeyes sadeyebrows "{cps=*0.2}... Eso espero.{/cps}"

$ renpy.music.stop(channel='crowd', fadeout=2.0)

show blank2 with dis:
    alpha 1.0

pause 2.0

redmind "Muy bien. Todavía no he desempacado mis cosas, así que probablemente debería volver a mi habitación para hacerlo."

scene hall_A with dissolve    

queue music "Audio/Music/CeruleanCity.ogg"

$ renpy.pause(1.5, hard=True)

pause 1.5

red surprisedbrow frownmouth @surprised "Uh."

show misty with dis:
    xpos 860

pause 1.0
    
misty @surprised "¿En serio? ¿No te acabo de ver hace {i}un{/i}  momento?"
misty "{w=0.5}.{w=0.5}.{w=0.5}."
misty @angry "Eres el tipo que me atropelló."

if (persondex["Misty"]["Value"] > 0):
    misty @talkingmouth "Pero al menos fuiste lo suficientemente decente como para disculparte."
    misty @sad "No mucha gente admite sus errores.{w=0.5}{nw}"
    extend @closedbrow sweat talkingmouth " Yo lo, eh... aprecio."

$ renpy.pause(1.5, hard=True)
misty @closedbrow talkingmouth "Tch. Como sea, no te lo echaré en cara."
$ renpy.pause(1.5, hard=True)

$ BecomeNamed("Misty")
misty @surprisedbrow talkingmouth "¿Y bien? ¿Qué estás esperando? Preséntate. Yo me llamo Misty."

if (persondex["Misty"]["Value"] > 0):
    red @happy "Me llamo [first_name], encantado de conocerte."
else:
    red @happy "Creo que empezamos con el pie izquierdo. Empecemos de nuevo. Soy [first_name], un gusto conocerte."

if first_name in ["Abel", "Adrián", "Agustín", "Alejandro", "Álvaro", "Andrés", "Antonio", "Armando", "Arturo", "Baltasar", "Benjamín", "Bruno", "Camilo", "Carlos", "Chucho", "Cristian", "Cristóbal", "Daniel", "Darío", "David", "Diego", "Eduardo", "Edgar", "Edmundo", "Emilio", "Emiliano", "Enrique", "Escoto", "Esteban", "Fernando", "Fabián", "Fausto", "Federico", "Felipe", "Félix", "Francisco", "Gabriel", "Gaspar", "Gerardo", "Gonzalo", "Gregorio", "Guido", "Guillermo", "Haroldo", "Héctor", "Horacio", "Iván", "Ismael", "Jacinto", "Jacobo", "Jaime", "Javier", "Jesús", "Joaquín", "Jorge", "José", "José", "Jonatán", "Juan", "Juanito", "Julián", "Julio", "Justino", "Kevin", "Lautaro", "Lázaro", "Leandro", "Leonardo", "Lucas", "Luis", "Lorenzo", "Manuel", "Mario", "Marcos", "Mariano", "Martín", "Mateo", "Maximiliano", "Miguel", "Nicolás", "Norberto", "Óscar", "Orlando", "Pablo", "Patricio", "Pedro", "Pepe", "Raúl", "Raúl", "Renato", "René", "Ricardo", "Roberto", "Rodrigo", "Rogelio", "Rubén", "Samuel", "Salvador", "Salamandra","Sebastián", "Sergio", "Silvio", "Santiago", "Teodoro", "Timoteo", "Tomás", "Tristán", "Valerio", "Valentín", "Vicente", "Víctor", "Walter"]:
    misty @surprised "'¿[first_name]?' ¿En serio?{w=0.5} Suena muy basico."
    red @unamusedbrow talking2mouth "Parece ser que se equivocaron al ponerme ese nombre..."
    misty @surprised "Uhh, solo quiero decir que no esperaba que tu nombre fuera tan normal, solo eso."

else:
    misty @surprised " '¿[first_name]?' ¿En serio?{w=0.5} ¿Qué clase de nombre es ese?"
    red @unamusedbrow talking2mouth "Parece ser que se equivocaron al ponerme ese nombre..."
    misty @surprised "Uhh, solo quiero decir que no conozco a muchas personas con ese nombre, solo eso."

misty @sadbrow sweat talkingmouth "¡No estoy diciendo que sea raro ni nada por el estilo, de verdad!"

redmind @unamusedbrow frownmouth "Adelante. Sigue cavando tu propia tumba..."
misty -sweat surprised @sad "{size=30}{i}Ugh, ¿por qué siempre soy tan...? {/i}{/size}"

red @closedbrow talking2mouth "Vas a tener que hablar un poco más fuerte. Empezaste a bajar la voz en esa última frase."

misty -surprisedbrow -frownmouth -surprised @angry "¡Yo no dije nada!"

pause 1.0

redmind @thinking "Tch, está más tensa que un resorte enrollado. No estoy seguro si esta conversación vale la pena al punto de pisar en falso, pero..."

menu:
    "¿Vives aquí?":
        red @talkingmouth "¿Esta es tu habitación, verdad?"
        misty @surprised "¿Sí? ¿Y qué?"

        $ renpy.pause(1.0, hard=True)

        misty @closedbrow talkingmouth "Genial. Ahora sabes dónde vivo."
        misty @angry "¡No te hagas ideas raras!"
        red @happy "Hey, soy un buen chico.{w=0.5} No me atrevería a hacer algo así."
        misty @closedbrow talkingmouth "Hmm."
        
        misty @talkingmouth "Supongo que puedo confiar en ti.{w=0.75}{nw}"
        misty @angrybrow talkingmouth "¡Solo asegúrate de mirar por dónde vas cuando empiecen las clases!"
        redmind @thinking "Puedes dejar de decir eso en cualquier momento, ¿sabes...?"
        
    "¿Cómo estuvo tu día?":
        red -angrybrow -talking2mouth @talkingmouth "Entonces, ¿cómo estuvo tu primer día aquí?"
        misty @talkingmouth "¿Aparte de que me tiraste al suelo?{w=0.5} Todo perfecto."
        redmind @thinking "Puedes dejar de decir eso en cualquier momento, ¿sabes...?"

    "¿Es ese un uniforme de Ciudad Celeste?":
        show misty happy with dis        
        $ ValueChange("Misty", 1, 0.5)

        misty smilemouth -happy @happy "¿Conoces Ciudad Celeste?"
        
        red @talkingmouth "¡Claro! Mi mamá y yo solíamos ir a sus parques acuáticos todo el tiempo cuando era un niño pequeño."
        red @sadeyes sadeyebrows talkingmouth "Aunque, esos paseos en Gyarados siempre me daban un miedo tremendo en ese entonces."
        
        misty @sadbrow talkingmouth "Aw, ¿En serio?{w=0.5} ¿De dónde eres?"
        
        red @talkingmouth "Soy de Pueblo Paleta.{w=0.5} No es el lugar más conocido en Kanto, pero seguramente has oído de él."
        
        misty -smilemouth @surprisedbrow talkingmouth "¿Dijiste Pueblo Plateado?"
        
        red @closedbrow talkingmouth "Uh, no. ¿Pueblo Paleta?{w=0.5} Ya sabes, el que tiene muchos árboles y pasto...{w=0.5} Está al sur de Ciudad Verde...{w=0.5}"
        red @sadbrow talkingmouth "¿Te suena de algo?"

        misty @closedbrow talkingmouth "Nope. Lo siento."

        redmind @closedbrow frownmouth "¡Maldita sea! Estaba tan cerca de tener una conversación normal con alguien. ¡Maldigo mi origen humilde!"

show misty surprisedbrow frownmouth with dis

red @happy "De todos modos, tengo que desempacar mis cosas. No debería seguir reteniéndote."

red @talkingmouth "Déjame ayudarte con tus bolsos, para compensarte por lo de antes."
red @surprised "... Huh. Vaya, estos bolsos sí que son elegantes. ¿Qué dice esta etiqueta? ¿Algo sobre un gimnasio?"

misty angry "¡No los toques!"

show misty:
    xpos 860 ypos 1080 zoom 1.0
    ease 0.4 zoom 1.2 ypos 1250 xpos 780
    
$ renpy.pause(0.5, hard=True)

red @confused "Eh, vale. Parece que no necesitas mi ayuda."

show misty angry:
    xpos 780 ypos 1250 zoom 1.2
    ease 0.5 zoom 1.0 ypos 1080 xpos 820

misty @talkingmouth "Tú... desconsiderado, cabezón... tú..."

show misty angry:
    xpos 820 zoom 1.0

misty @talkingmouth "¡No vayas tocando las cosas de una chica sin su permiso!"

show misty angry:
    xpos 820 alpha 1.0
    ease 0.33 xpos 200 alpha 0.0
    
pause 0.33

$ PlaySound("Door_Slam.ogg")
show hall_A:
    yalign 0.0
    ease 0.03 ypos -10
    ease 0.03 ypos 10
    ease 0.03 ypos 0
    repeat 3

red @unamusedbrow frownmouth "[ellipses]"

if (persondex["Misty"]["Value"] == 2):
    redmind @happy "No, no me vas a espantar tan fácilmente. Voy a ser tu amigo, y no hay nada que puedas hacer al respecto."
elif (persondex["Misty"]["Value"] == -1):
    redmind @unamusedbrow frownmouth "... Ugh. Ya estoy harto de ella."
else:
    redmind @unamusedbrow frownmouth "Siento que me termine equivocando en algo..."

hide misty

stop music fadeout 1.5

$ renpy.pause(1.5, hard=True)
    
scene dorm_empty_B with dis

$ PlaySound("Door_Open1.ogg")

$ renpy.pause(2.5, hard=True)

hide blank2

redmind @thonk "¿...?"
redmind @thinking "Algo... no encaja."
redmind @thonk "Es como esos juegos que jugaba de niño donde tenía que encontrar las diferencias entre dos imágenes parecidas."
redmind @thonk "Definitivamente hay algo fuera de lugar, pero no logro ver lo que es."

$ PlaySound("Door_Close1.ogg")

show calem at leftside with dis
show brendan at rightside with dis
show ethan at centerside with dis

calem @talkingmouth "¿Pasa algo, [first_name]?"
red @confused "No estoy seguro..."
calem @talkingmouth "¿Has estado bebiendo agua? Con toda la emoción, es fácil olvidarse.{w=0.5} La deshidratación puede ser peligrosa."
brendan @surprised "¡Oh, mierda! ¿Te duele la cabeza? ¿O dolor de estómago, tal vez?{w=0.5} Dame un segundo, creo que May dejó un par de Bayas Ziuela en mi mochila."

red @confused "¿En tu mochila{w=0.25}.{w=0.25}.{w=0.25}.?"
red @surprisedbrow talking2mouth "...{w=0.5} Mochila."

pause 2.0

show dorm_empty_B:
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

queue music "Audio/Music/Found It.ogg" noloop
$ renpy.music.queue("Audio/Music/Sneaking Again.ogg", channel='music', loop=True, tight=None)

show brendan surprisedbrow frownmouth
show ethan surprisedbrow frownmouth
show calem surprisedbrow
with dis

red @angry "{size=42}¡Mi mochila no esta!{/size}"

ethan @surprised "¿La de color amarillo con negro?"

calem @sadbrow talkingmouth "Sí, yo también la vi. ¿Dónde fue la última vez que la viste?"

red @sad "¡Maldita sea, la necesito! ¡Tiene prácticamente todo menos mi ropa!"

brendan angrybrow @angry "¡Alguien tuvo que haberla robado! ¡Voy a destrozar a ese desgraciado en una batalla!"

calem -surprisedbrow @talkingmouth "Tranquilízate, solo nosotros cinco y el personal podemos entrar a nuestra habitación."

red @confused "[ellipses]{w=0.5} ¿Nosotros {i}cinco{/i}?"

ethan @angry "Espera un momento... ¡Hillenbrand no está aquí!"

calem @surprised "Eso es verdaderamente desconcertante."
calem @closedbrow talkingmouth "En cualquier caso, puede que él no lo esté, pero sí todo su equipaje. No tiene sentido que se escapara con tu mochila y deje todas sus posesiones aquí a nuestra merced."

brendan @closedbrow sweat talking2mouth "Huh... Esa chica, Roxanne, dijo que había un montón de cámaras de seguridad, ¿no?"

red @angrybrow happymouth "¡Sí, es cierto! Buena idea. Voy ahora mismo a la oficina de seguridad."

pause 1.0

show calem sadbrow smilemouth with dis
show ethan closedbrow frownmouth sweat with dis
show brendan sadbrow frownmouth with dis

red -angrybrow @sad "Eh..."

pause 1.0

calem @talking2mouth "¿Estoy en lo correcto al suponer que ninguno de nosotros sabe dónde está la oficina de seguridad?"

pause 1.0

red @closedbrow talking2mouth "Síp... Pero..."

show ethan -sweat happy with dis
show brendan happy with dis
show calem surprisedbrow frownmouth with dis

red @angrybrow happymouth "¡Si elegimos una dirección y empezamos a correr, tarde o temprano la encontraremos!"

ethan @happy "¡Así se habla!"

brendan @happy "Día de pierna, ¡allá vamos!"

show brendan:
    xpos 0.75
    ease 0.4 xpos 1.5

show ethan:
    xpos 0.5
    ease 0.4 xpos 1.5

pause 0.4

$ PlaySound("Door_Slam.ogg")

pause 2.0

calem @sadbrow talkingmouth "Así no es como funciona el mundo, no puedes correr en una dirección aleatoria y simplemente llegar a tu destino."
calem @sadbrow frownmouth "[ellipses]"
calem happy "Oh, qué más da. ¡Esperenme!"

show calem:
    xpos 0.25
    ease 1.0 xpos 1.5

pause 0.5

show blank2 with splitfadefast

$ renpy.pause(1.0, hard=True)

show lobby_night behind blank2
hide dorm_empty_B

$ renpy.pause(0.5, hard=True)
$ renpy.music.play("Audio/hall_crowd.ogg", channel='crowd', loop=True, fadein=1.5)

hide blank2 with splitfadefast

red @talking2mouth "¿Eh...? ¿Por qué están todos gritando?"

show face with dis:
    xpos 0.6

face angrybrow @surprised "¿Tú otra vez? ¿Tuviste algo que ver con esto?"

red @confused "¿Qué?"

show mace with dis:
    xpos 0.4

hide brendan

mace @talkingmouth "Hace unos minutos había algo corriendo por el vestíbulo.{w=0.5} Y cada vez que alguien intentaba tocarlo, soltaba una descarga eléctrica. Aunque parecía... un insecto."

red @talkingmouth "¿Qué podría ser? ¿Un Galvantula? ¿O un Charjabug?"

mace @surprised "Oh, así que realmente sabes de sobre los Pokémon. Hmph. {nw}"
extend @talkingmouth "Siendo ese el caso, deberías saber que no podía ser un Charjabug, porque se movía demasiado rápido. Pero también parecía demasiado pequeño para ser un Galvantula."

face @closedbrow talkingmouth "¿Acaso no tenía la apariencia de una mochila amarilla con detalles en negro?"

mace @closedbrow talkingmouth "Hmm... Ahora que lo mencionas, francamente lo parecía."

hide mace
hide face
with dis

show brendan with dis:
    xpos 0.75
    
brendan frownmouth @talking2mouth "Huh. Esa es una gran coincidencia."

hide calem

if (profanity):
    red @confused "¡Coincidencia y una mierda!{w=0.5} ¡¿Por qué mi mochila está corriendo por el vestíbulo?!"
else:
    red @confused "¡Coincidencia y una ******!{w=0.5} ¡¿Por qué mi mochila está corriendo por el vestíbulo?!"

show calem thinking with dis:
    xpos 0.25

calem @closedbrow talkingmouth "... Interesante.{w=0.5} ¿Qué dijiste que habías empacado en tu mochila, [first_name]?"

show calem surprisedbrow frownmouth with dis

red @closedbrow talking2mouth sweat "¡Te aseguro que no empacé un Galvantula!{w=0.5} Sea lo que sea, lo único que quiero es recuperar mi mochila."

show calem -surprisedbrow -frownmouth -surprised with dis

red @closedbrow talking2mouth "¿Para dónde se fue?"

hide ethan
show ethan with dis

ethan @talkingmouth "El alboroto viene de esa dirección, creo que solo deberíamos seguir los gritos y estaremos bien. Pero si no nos apresuramos, los guardias del campus probablemente se harán cargo primero... o algún otro estudiante."

brendan @angry "¡Oh no! Esa es tu mochila, ¿no, [first_name]? {w=0.5} Si esos tipos la agarran antes, quién sabe qué le van a hacer a tus cosas."
brendan @sad "No tengo muy claro qué está pasando, pero si hay algo realmente raro {i}dentro{/i} de tu mochila, ¿no te meterías en un gran problema si descubren que es tuya?"

calem @talkingmouth sadbrow "En teoría, nos meteríamos en más problemas si interfirimos con el equipo de seguridad de la academia..."

ethan @surprised "Yo... eh... mejor paso de elegir. Lo que decidas hacer seguro que es lo mejor."
     
red @closedbrow sweat talking2mouth "Pase lo que pase, esa sigue siendo mi mochila, y la quiero de vuelta."
red @talkingmouth sad2eyes angryeyebrows "La situación se está yendo de las manos, pero esa es una razón más para encargarme de esto yo mismo."

calem @closedbrow talkingmouth "Si tú lo dices.{w=0.5} No voy a cuestionar tu decisión, así que si crees que esto es lo mejor, entonces te seguiré."
calem @happy "De todos modos, alguien tiene que asegurarse de que no hagas algo estúpido."

brendan @happy "¡Ya rugiste! ¡Esa mochila es tuya y no dejaremos que nadie la toque con sus sucias manos!"
brendan @angry "¡Lidera el camino, [first_name], y yo te cubro!"

ethan @happy "Allons-y!"

show blank2 with splitfade

$ renpy.pause(1.5, hard=True)

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

$ renpy.music.stop(channel='crowd', fadeout=1.5)

hide lobby_night

$ renpy.pause(3.0, hard= True)

show hall_B_night behind brendan:
    subpixel True
    xalign 0.5 yalign 1.0 zoom 1.0
    ease 2.5 xalign 0.5 yalign 1.0 zoom 1.07

hide blank2 with splitfade

$ renpy.music.play("Audio/hall_crowd.ogg", channel='crowd', loop=True, fadein=1.5)

$ renpy.pause(1.5, hard= True)

show calem surprisedbrow frownmouth with dis
show ethan surprisedbrow frownmouth with dis
show brendan surprisedbrow frownmouth with dis

red @surprised "Puedo oír a la gente gritando.{w=0.5} ¡Tenemos que estar cerca!"

show hall_B_night:
    xpos 960 ypos 1080 zoom 1.07

hide text
hide text1
hide text2
hide text3

ethan @surprised "¡Hey, por aquí! ¡Veo tu bolsa!{w=0.5} Está.{w=0.25}.{w=0.25}.{w=0.5}{nw}"
extend @confused " ¡¿realmente moviéndose sola?!"
calem @talkingmouth "Obviamente no. Debe de haber algo dentro que esté impulsando su movimiento."

show backpack with dis:
    alpha 1.0
    
pause 0.5

$ PlaySound("Pokemon/Moves/Paralyzed.ogg")

$ renpy.pause(1.0, hard=True)

show backpack

redmind @thinking "Parece ser que mi mochila se esta deslizando entre las piernas de la gente como si fuera un Pokémon pequeño.{w=0.5} Pero el problema más grande son todas las personas que están tratando de agarrarla..."
red @angry "¡Oigan, detenganse! ¡Es mi mochila!"

Character("Estudiante codicioso") "\"¡Ni hablar, yo la vi primero!\""
Character("Estudiante grosero") "\"¡Sí, claro! ¡El que la encuentra se la queda, idiota!\""

red @wince talking2mouth "No, quiero decir que es {i}literalmente{/i} mía. ¡Tiene mi nombre escrito!"

brendan @happymouth angrybrow "No te preocupes, [first_name], ¡yo me encargo!{w=0.5} He lidiado con este tipo de cosas ant--"

$ PlaySound("thunder.ogg")
show blank:
    alpha 0.5
    pause 0.1
    alpha 0.0
    pause 0.1
    repeat 5

show backpack:
    parallel:
        xalign 0.0
        ease 0.03 xpos -20
        ease 0.03 xpos 20
        ease 0.03 xpos 0
        repeat 8
    parallel:
        yalign 0.0
        ease 0.03 ypos -20
        ease 0.03 ypos 20
        ease 0.03 ypos 0
        repeat 8

show hall_B_night:
    parallel:
        xalign 0.0
        ease 0.03 xpos -20
        ease 0.03 xpos 20
        ease 0.03 xpos 0
        repeat 7
    parallel:
        yalign 0.0
        ease 0.03 ypos -20
        ease 0.03 ypos 20
        ease 0.03 ypos 0
        repeat 7

show calem surprisedmouth deadbrow at leftside, monochrome behind backpack
show ethan surprisedmouth deadeyes surprisedeyebrows at monochrome behind backpack
show brendan surprisedmouth deadbrow at rightside, monochrome behind backpack

Character("Roomies") "\"{size=48}AaaaarrrRGBLRLBLRBLLBR{/size}\""

hide blank

hide backpack with dis

$ renpy.pause(1.0, hard=True)

show calem:
    ypos 1.0 xpos 0.25
    ease 1.0 ypos 1.1 rotate 5.0
show ethan:
    ypos 1.0
    ease 1.0 ypos 1.2 rotate -5.0
show brendan:
    ypos 1.0 xpos 0.75
    ease 1.0 ypos 1.15 rotate 7.0

$ renpy.pause(1.5, hard=True)

red @angry "¡Oigan, chicos!{w=0.5} ¡Levantense!"

show calem:
    ypos 1.1 rotate 5.0 xpos 0.25
    ease 0.5 ypos 2.0 rotate 30.0
show ethan:
    ypos 1.2 rotate -5.0
    ease 0.5 ypos 2.0 rotate -30.0
show brendan:
    ypos 1.15 rotate 7.0 xpos 0.75
    ease 0.5 ypos 2.0 rotate 35.0

$ renpy.pause(0.5, hard=True)

$ PlaySound("Body Roll.ogg")

show hall_B_night with vpunch

$ renpy.pause(1.5, hard=True)

stop music
show flashback with dis

$ renpy.music.queue("Audio/Music/RelicCastle_Start.ogg", channel='music', loop=None, tight=None)
$ renpy.music.queue("Audio/Music/RelicCastle_Loop.ogg", channel='music', loop=True, tight=None)

redmind @thinking "Bien, hay algo dentro de mi mochila. Es casi seguro de tipo eléctrico: es rápido, pequeño, no muy poderoso, pero decidido a lo que sea que esté haciendo."
redmind @thinking "No puede ser un Rotom, porque mi mochila no es mecánica. Se mantiene en el suelo, así que no puede volar ni levitar. Puede ver hacia dónde va, por lo que su cabeza debe estar cerca del suelo y, además, se mueve en cuatro patas."
redmind @thinking "Parece medir menos de cincuenta centímetros de largo, y por la forma en que se mueve, su velocidad base debe estar en un rango entre ochenta y cien."
redmind @thinking "Entonces... podría ser un Pachirisu, un Minun, un Togedemaru, o incluso un..."

stop music
hide flashback
show hall_B_night with vpunch

security @talkingmouth "¡Cuidado, chico!"

red @surprised "¡Gwaah!"

show hall_B_night with vpunch

red @wince angrymouth "{size=42}¡No voy a poder esquivarla!{/size}"

stop music fadeout 1.0

red @closedbrow talking2mouth ".{w=0.25}.{w=0.25}.{w=0.75}{nw}"
extend @closedbrow talking2mouth "¿Huh?"
red @confused "No...{w=0.5} está haciendo nada."
red @thonk "[ellipses]"
red @happy "Bueno, ¿por qué no te abrimos y vemos qué está pasando aquí, eh?"

security @talkingmouth "¡E-eh, chico! ¡No hagas movimientos bruscos!{w=0.5} ¡Esa cosa es peligrosa!"

$ PlaySound("Pokemon/Unzip Pikachu.ogg")
$ renpy.pause(3.0, hard=True)

$ renpy.music.queue("Audio/Music/New_Adventure_Start.ogg", channel='music', loop=None, tight=None)
$ renpy.music.queue("Audio/Music/New_Adventure_Loop.ogg", channel='music', loop=True, tight=None)

$ renpy.pause(1.0, hard=True)

red surprisedbrow frownmouth @surprised "¡Esto es...!{w=0.75}{nw}"

show redpika01:
    alpha 0.0 zoom 1.1 yalign 1.0 xalign 0.5
    ease 1.0 zoom 1.0 yalign 1.0 xalign 0.5 alpha 1.0

extend @talkingmouth ""

red @talkingmouth "¡¿[pika_name]?!{w=0.5} ¿Qué? ¿Cómo llegaste a...?"

$ PlaySound("Pokemon/pikachu_happy3.ogg")

hide pikachu

pikachu happy_3 "¡Pipipi... Pika!"

hide calem
hide ethan
hide brendan

calem @sadbrow talking2mouth "... ¿Trajiste un Pikachu?{w=0.5} No mencionaste eso cuando te pregunté qué había en la mochila."

red @surprised "¡No! Lo dejé con mi mamá y...{w=0.25} ¿cómo llegaste aquí?{w=0.5} ¡¿Te escondiste en mi maleta?!"

$ PlaySound("Pokemon/pikachu_excite5.ogg")

pikachu neutral_2 "¡Piii-kaaaa-chuuu!"

red @angry "¡¿No te dije que te quedaras con mamá?! ¿Acaso sabe siquiera que estás aquí?{w=0.5} ¡Si te hubiera metido en la bodega de equipaje, podrías haberte congelado, maldita bola de pelos!"

$ PlaySound("Pokemon/pikachu_sad.ogg")
pikachu neutral_4 "P-Pika...{w=0.5}{nw}"
$ PlaySound("Pokemon/pikachu_happy2.ogg")
extend pikachu neutral_2b " ¡Pikaaaaa!~"

red @sad "... ¿Tantas ganas tenías de verme?"
red @happy "Oh, ¿cómo podría decirte que no?{w=0.5} ¡Bienvenido de vuelta, [pika_name]!"

$ PlaySound("Pokemon/pikachu_excite3.ogg")
pikachu @happy_3 "¡Pika, pika!"

hide redpika01 with Dissolve(1.0)

pause 1.0   
     
stop music fadeout 2.0

redmind @happy "¡Muy bien! Al parecer, todo lo que empieza bien, termina bien...{w=0.5}{nw}"
extend @wince frownmouth " Excepto por un problema."

$ renpy.music.queue("Audio/Music/Littleroot_Start.ogg", channel='music', loop=False, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/Littleroot_Loop.ogg", channel='music', loop=True, fadein=0.0, tight=None)

pause 1.0

security @talkingmouth "Así que esto es lo que ha causado todo el alboroto.{w=0.5} Joven, ¿este Pokémon es tuyo?"

red @sad "Sí, señor. Lo es."
    
security @talkingmouth "Jovencito, permitir que tu Pokémon deambule libremente por la residencia es una cosa, pero poner en peligro a los estudiantes y al personal de este edificio es otra."
security @talkingmouth "Me temo que voy a tener que pedirte a ti y a tu Pokémon que me acompañen a mi oficina."

show calem at leftside with dis

calem @talkingmouth "Disculpe, señor, pero no creo que esto sea justo para [first_name] o su Pikachu."
calem @closedbrow talkingmouth "Difícilmente podemos culparlo por sentirse asustado en un ambiente desconocido.{w=0.5} Solo intentaba llegar a [first_name] antes de que todos aquí comenzaran a agitarlo."
    
show brendan at rightside with dis

brendan @angry "¡Sí, espera un segundo! ¿Cuál es el gran problema?{w=0.5} ¡Pikachu solo intentaba encontrar a [first_name], como haría cualquier Pokémon con su Entrenador!"
brendan frownmouth @angrybrow talking2mouth "¡Ustedes fueron los que lo persiguieron por todo el lugar y lo asustaron, así que obviamente iba a electrocutar a algunas personas!"

show ethan with dis

ethan frownmouth @angry "¡Sí!{w=0.5} [first_name] ni siquiera sabía que su Pikachu estaba en su mochila."

calem @sadbrow talkingmouth "Si ese es el caso, ¿no sería más sensato asumir que la culpa está en otro lado? Quizás... en quienes deberían cuidar la propiedad."

brendan @closedbrow talking2mouth "¿Verdad?{w=0.5} ¿Qué clase de sistema de seguridad tienen donde alguien puede {i}accidentalmente{/i} traer un Pikachu sin que se den cuenta?"    

security @talkingmouth "Hmph. {w=0.5}Veo lo que están haciendo, chicos, pero las reglas son muy claras. Necesito llevar a este joven a la oficina, y si interfieren, también tendré que reportarlos."

show calem surprisedbrow frownmouth with dis
show brendan surprisedbrow frownmouth with dis

ethan @surprised "¿R-reportarnos?! ¡¿Por qué?! ¿Por defender a un amigo?"

red @happy "Chicos, relájense. No se preocupen, encontraré una solución. No hay necesidad de que se metan en problemas por mi culpa."

show calem sadbrow frownmouth with dis
show brendan sadbrow frownmouth with dis

ethan @sad "P-pero..."

pause 1.0

security @talkingmouth "Eso está mejor. Ahora, joven, ven conmigo y..."

show hilbert:
    xpos -0.5 zoom 1.0 ypos 1.0
    ease 0.5 xpos 0.3 zoom 1.2 ypos 1.1

show ethan surprisedbrow frownmouth:
    xpos 0.5
    ease 0.5 xpos 0.8

show brendan surprisedbrow frownmouth:
    xpos 0.75
    ease 0.5 xpos 0.9

show calem surprisedbrow frownmouth:
    xpos 0.25
    ease 0.5 xpos 0.7

show hall_B_night with vpunch

stop music

$ renpy.music.queue("Audio/Music/DragonDenStart_B.ogg", channel='music', loop=False, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/DragonDenLoop.ogg", channel='music', loop=True, fadein=0.0, tight=None)

hilbert angrybrow @angry "{size=42}Patético.{/size}"

security @talkingmouth "¿J-jovencito...?"

hilbert @closedbrow talkingmouth "Vivo en el dormitorio de donde vino esa mochila. Estuve allí antes que cualquiera y lo vi {b}todo{/b}."

pause 1.0

hilbert @angry "Lo que vi fue {b}patético{/b}. '¿Equipo de seguridad?' Más bien, son un equipo improvisado de payasos. Tú y tu banda de incompetentes no podrían asegurar ni una pizza."
hilbert @talkingmouth "¿Cuándo fue la última vez que {i}alguno{/i} de ustedes pasó un examen físico? ¿Y su coordinación? Ridícula. Los escuché discutir durante cinco minutos sobre qué 'código' era esta situación."
hilbert @angry "Tienen suerte de que esto fuera solo un Pikachu. Si hubiera sido algo más grande, gente inocente podría haber {i}muerto.{/i}"
hilbert @angry "¿Eso los haría darse cuenta de lo poco calificados que son para mantener a {i}alguien{/i} a salvo? ¿O simplemente van a renunciar?"

pause 1.0

hilbert sadbrow @talkingmouth "Ahora, sal de mi vista."

hide hilbert with Dissolve(1.5)

pause 2.0

stop music 

show ethan -surprisedbrow -frownmouth:
    xpos 0.8
    ease 0.5 xpos 0.5

show brendan -surprisedbrow -frownmouth:
    xpos 0.9
    ease 0.5 xpos 0.75

show calem -surprisedbrow -frownmouth:
    xpos 0.7
    ease 0.5 xpos 0.25

$ renpy.music.queue("Audio/Music/New_Adventure_Start.ogg", channel='music', loop=None, tight=None)
$ renpy.music.queue("Audio/Music/New_Adventure_Loop.ogg", channel='music', loop=True, tight=None)

red @surprised "S-santos cielos..."

ethan @talkingmouth "Bro.{w=0.5} ¿Hillenbrand realmente nos la dejo barata antes...?"

pause 1.0

red @sad "Ehm, si le sirve de consuelo, señor, yo no creo que hicieron un muy mal trabajo..."
red @thonk "[ellipses]"
red @confused "Esperen un segundo, ¿a dónde se fue?"

calem @closedbrow talkingmouth "Se fue por ahí.{w=0.5} Llorando, creo."

red @confused "Bueno, supongo que deberíamos empezar a volver a nuestra habitación.{w=0.5} Ya casi es la hora de dormir, y Cheren todavía no es presidente, así que..."

ethan @confused "¿Quién?"

red @happy "Es un tipo genial que se quiere postular para el consejo estudiantil, y..."

pause 1.5

window hide
show blank2 with splitfade
stop music fadeout 1.5
$ renpy.pause(2.0, hard=True)

hide calem
hide ethan
hide brendan

$ renpy.music.queue("Audio/Music/SoaringIllusions_Intro.ogg", channel='music', loop=None, tight=None)
$ renpy.music.queue("Audio/Music/SoaringIllusions.ogg", channel='music', loop=True, tight=None)

$ renpy.pause(1.0, hard=True)

show phone_B behind blank2
show phone_A behind blank2
with fadeinbottom

show mom behind phone_A:
    xalign 0.5 zoom 0.95

mom sad "{i}¡Oh, lo siento, cariño!{w=0.5} Cuando decidió seguirte, simplemente no tuve corazón para detenerlo...{/i}"
mom -sad @talkingmouth "{i}¡Quería llamarte, pero creo que los aviones no tienen señal cuando están en el aire!{/i}"
    
show dorm_empty_B behind phone_B

hide blank2 with dis

red sad "¿Y por qué no lo hiciste cuando aterricé?"

mom @talkingmouth "{i}Bueno, para cuando lo recordé, supuse que ya lo habrías encontrado.{/i}{w=0.5}{nw}"
mom @happy "{i}Bueno, para cuando lo recordé, supuse que ya lo habrías encontrado. {fast}¡De hecho, estaba más sorprendida de que no me llamaras antes!{/i}"

hide blank2

show mom surprisedbrow frownmouth with dis

red @closedbrow talking2mouth "Ugh, mamá... tienes suerte de que mi compañero de cuarto me haya cubierto, o me habría metido en un gran problema."

mom @happy "{i}Oh, ¿y cómo{/i} es {i}tu compañero de cuarto?{w=0.5} ¿Es un buen chico? ¿De dónde es? ¿Cómo es?{/i}"

hide hilbert

red @happy "Bueno, en realidad tengo cuatro compañeros de cuarto. Pero el que me cubrió se llama Hilbert. Es, eh... todo un personaje."

show mom -surprisedbrow -frownmouth with dis

red @talkingmouth "De todos modos, te lo dire todo mañana.{w=0.5} Todavía tengo cosas que desempacar y acomodar antes de irme a la cama."
red @sweat sadbrow talkingmouth "Todo para prepararme para el primer día de clases y todo lo demás."

mom @happy "{i}¡Oh, por supuesto!{w=0.5} ¡Buenas noches, mi querido campeón! Hablamos mañana.{/i}"

show phone_B:
    ypos 1.0
    ease 1.0 ypos 3.0
        
show mom:
    parallel:
        ypos 1.0
        ease 1.0 ypos 3.0
    parallel:
        alpha 1.0
        ease 0.25 alpha 0.0
        
show phone_A:
    ypos 1.0
    ease 1.0 ypos 3.0

$ renpy.pause(2.0, hard=True)  


show hilbert with dis:
    xpos 0.2 xzoom -1

show ethan with dis:
    xpos 0.4

show brendan with dis:
    xpos 0.6

show calem with dis:
    xpos 0.8 xzoom -1

ethan @confused "Entonces, [first_name] y yo vamos a intercambiar entre electividades, pero ¿qué hay de ustedes? ¿Cuáles elegirán?"

brendan @angrybrow happymouth "¡Planta y Tierra para mí! Tengo mucha experiencia con esos tipos en Hoenn."

pause 1.0

brendan @happy "¡Oh, y Agua también! {i}El campeón Wallace{/i} está enseñando esa clase. Amo a ese tipo. Su reinado fueron las mejores vacaciones de primavera que he tenido."

calem @talkingmouth "Los tipo Lucha, Volador y Hada son mis preferencias. Tal vez tome otra optativa por variedad, pero creo que ya estoy bastante decidido."

pause 1.0

ethan @angrybrow talking2mouth "También te estaba preguntando a ti, Hillenbrand."

hilbert @sadbrow talkingmouth "Es Hilbert."
hilbert @thinking "[ellipses]"
hilbert @closedbrow talkingmouth "Y estaré en las clases de Acero, Hielo y Fantasma."

show hilbert at dissolveaway:
    xpos 0.2

pause 2.0

ethan happy "¡Por supuesto que sí, era de esperarse de nuestro querido edgelord!"

show hilbert angry:
    xpos 0.2

show ethan surprisedbrow frownmouth with dis
show brendan surprisedbrow frownmouth with dis
show calem surprisedbrow frownmouth with dis

show dorm_empty_B at vpunch

pause 1.0


hilbert @talkingmouth "¡No es nada de eso! El Hielo es el tipo ofensivo más poderoso, y el Acero es el tipo defensivo más poderoso. Elegir a esos dos es lógico, mientras que el tipo Fantasma cubre sus debilidades ante el tipo Lucha."

pause 1.0

hilbert sadbrow talkingmouth "Tch. Ni se para que lo digo, no estoy obligado a explicarte nada."

show hilbert at dissolveaway:
    xpos 0.2

pause 2.0

show calem thinking with dis
show ethan thinking with dis

brendan frownmouth @sadbrow talking2mouth "¿Es... eso cierto? ¿Son el tipo Hielo y Acero los mejores?"

calem @talkingmouth closedbrow "Depende de lo que busques. Ciertamente, los tipos Acero son conocidos por su alta defensa, y los tipos Hielo por sus ventajas elementales."
calem -closedbrow -thinking @talkingmouth "Pero los tipos Planta y Tierra pueden hacer muchas cosas de las que carecen los tipos Acero o Hielo."

show brendan -frownmouth with dis

ethan -thinking @happy "Lo que quiere decir es...{w=0.5} ¡No te preocupes! No importa qué elijas, no puedes arruinar tu educación {i}demasiado{/i}."

calem @talkingmouth "Siempre que te limites a dos o tres tipos, claro. Es posible 'arruinarte' si intentas abarcar demasiado."

ethan @sad "Ehh...{w=0.5} sí." 
ethan @happy "Jajaja.{w=0.5} Lo sé. ¡No te preocupes, tengo planes desde la A hasta la Z!"

red @happy "¡Yo también! Pero mi plan ahora mismo es irme a dormir."
red @talkingmouth "¿Listo para ir a la cama, [pika_name]?"

$ renpy.sound.play("Audio/Pokemon/pikachu_excite2.ogg", channel="altcry", loop=None)
pikachu happy_2 "¡Pika!"

calem @surprised "¿No lo guardaras en su Poké Ball?"

red @confused "No, ¿por qué?"

stop music fadeout 2.0

calem @sadbrow talkingmouth "Yo...{w=0.5} Bueno, ¿dónde sueles dejarlo antes de irte a dormir?"

queue music "Audio/Music/Opening_Intro.ogg" noloop

red @talkingmouth "Justo aquí conmigo.{w=0.5} ¿Es algo raro?"

calem @happy "No, supongo que no."

brendan @happy "¡A mí me parece raro!{w=0.5} Pero si no te electrocuta, ¿supongo que está bien?"

ethan @talkingmouth "¡No es raro! Mi Pichu hace exactamente lo mismo."
ethan @closedbrow talking2mouth sweat "Si alguna vez intento guardarla en su Poké Ball antes de dormir, me termino despertando a las cuatro de la mañana con ella encima de mi cara."

brendan @surprised "¡Huh! Tal vez yo soy el raro, entonces."
brendan @happy sweat "Bueno, da igual. Me voy a dormir, chicos.{w=0.5} ¡Buenas noches, [first_name], Calem, Ethan, Hilbert y [pika_name]!"

show brendan at dissolveaway:
    xpos 0.6

calem happy "Sí, buenas noches a todos."

show calem at dissolveaway:
    xpos 0.8

ethan happy "¡Nos vemos mañana!"

show ethan at dissolveaway:
    xpos 0.4
    
red -sadeyebrows -sadeyes @talkingmouth "Buenas noches, chicos."
red @happy "Vamos a dormir, [pika_name].{w=0.5} Tenemos muchas cosas que hacer este fin de semana antes de que empiecen las clases."

$ PlaySound("pokemon/pikachu_norm3.ogg")
pikachu neutral_2b "Pika."

window hide

show blank2 with Dissolve(1.0)
$ renpy.pause(1.0, hard=True)

show relichall_B with dis

redmind casual hatless night @closedeyes frownmouth "Lo admito. Me da un poco de miedo que, si me duermo ahora, despierte y me dé cuenta de que haber entrado en la Academia Kobukan, no fue más que... un sueño."
redmind @sadbrow frownmouth "Pero ahora sé que es real.{w=0.5} Mi subconsciente no es lo suficientemente astuto como para haber hecho que [pika_name] se colara en mi equipaje hasta Kobukan. Ni siquiera en mis fantasías más locas de entrar en Kobukan imaginé algo así."
redmind @happy "Me alegra que él este aquí..."
redmind @thinking sweat "Pero {i}realmente{/i} tenemos que trabajar en su paciencia."

window hide

scene blank2 with transball

stop music fadeout 1.0
$ renpy.pause(1.0, hard=True)

hide calem
hide brendan
hide ethan
hide hilbert

hide dorm_empty_B

$ renpy.pause(1.0, hard=True)

show text "{color=#ffffff}{size=40}Pokémon Academy Life{/size}{/color}":
    alpha 1.0 yalign 0.5 xalign 0.5
    pause 3.0
    linear 1.0 alpha 0.0
    
$ renpy.pause(4.0, hard=True)

$ renpy.movie_cutscene('images/videos/Intro.webm')
    
$ renpy.pause(2.0, hard=True)

jump day010405