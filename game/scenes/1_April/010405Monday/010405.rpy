label day010405:
call calendar(3) from _call_calendar
$ calDate = calDate.replace(day=5, month=4, year=2004)

$ timeOfDay = "Morning"

queue music "Audio/Music/Road to Viridian City.ogg"

scene dorm_A with Dissolve(2.0)
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.0, hard=True)

hide blank2

$ renpy.music.set_volume(1.0, delay=0.0, channel="ctc")

redmind uniform closedbrow frownmouth "Finalmente es el primer día de clases. Pasé el fin de semana recorriendo este lugar, así que no debería perderme otra vez."
redmind happy "¡Se me esta poniendo la piel de gallina! ¡Qué emocion!"

show calem uniform:
    xpos 0.25 alpha 0.0
    ease 0.5 alpha 1.0

show ethan uniform:
    xpos 0.5 alpha 0.0
    ease 0.5 alpha 1.0

show brendan uniform:
    xpos 0.75 alpha 0.0
    ease 0.5 alpha 1.0
    
$ renpy.pause(0.5, hard=True)
    
calem @talkingmouth "¿Están listos para ir a desayunar?"
brendan @happy "¡Sí! Nunca te saltes el desayuno, es la comida más importante del día."
ethan @closedbrow talking2mouth "Estoy bastante seguro de haber leído en algún lado que eso era desinformación de la gran industria del desayuno..."
red @happy "¿Vamos a la cafetería principal?"
calem @talking2mouth "En efecto."

show calem surprisedbrow with dis

$ renpy.music.play("Audio/Pokemon/pikachu_pikapika1.ogg", channel="altcry", loop=None)

pikachu neutral_2b "¡Pika, pika!"

red @talkingmouth "Oh, ¿puede venir [pika_name] con nosotros?"

calem -surprisedbrow @sadbrow talkingmouth "Ayer lo consulté en la recepción y me dijeron que los Pokémon deben permanecer en sus habitaciones o en una Poké Ball fuera de la habitación, a menos que la academia lo autorice."

brendan @talking2mouth "Así que, ¿podriamos llevarlo siempre y cuando permanezca en su Poké Ball?"

ethan @sadbrow talkingmouth "No estoy seguro de que le guste la idea..."

show calem surprisedbrow
show brendan surprisedbrow frownmouth
with dis

$ renpy.music.play("Audio/Pokemon/pikachu_excite1.ogg", channel="altcry", loop=None)

pikachu angry_3 "¡Pi-{i}ka{/i}!"

show brendan -surprisedbrow -frownmouth with dis

calem -surprisedbrow @closedbrow talkingmouth "Tal vez no, entonces."

ethan @happy "Sí, algunos Pokémon simplemente no les gusta pasar tiempo en sus Poké Balls. Una vez intenté poner a mi Pichu en una Lujo Ball, ¿sabes? Pensé que sería más acogedora..."
ethan @sad "No sirvió de nada, y además me costó un buen dinero."

brendan @happy "Bros, eso es realmente genial.{w=0.5} Es como si tuvieran Pokémon rebeldes o algo así."

calem @talkingmouth "Es curioso, nunca había oído hablar de un Pokémon que mostrara ese tipo de comportamiento y ahora he oído hablar de dos."

red @confused "Tal vez... ¿tenga algo que ver con su línea evolutiva? Después de todo, Pichu evoluciona en Pikachu."

brendan @surprised "Guau, ¡¿Deberas?! Pensé que era una situación tipo Plusle y Minun, donde son simbióticos, pero no evolucionan."

calem @happy "Cuando te cuente sobre Raichu, seguro te explotara el cerebro."

red @sadeyes sadeyebrows talkingmouth "Lo siento, [pika_name], pero tendrás que quedarte aquí hasta que regrese..."
red @confused "¿A menos que quieras venir en tu Poké Ball?"

$ renpy.music.play("Audio/Pokemon/pikachu_angry1.ogg", channel="altcry", loop=None)

pikachu angry_2 "¡Pi-ka!"
    
red @happy "Muy bien, como quieras.{w=0.5} Hay algo de comida en mi cajón, pero no te la comas toda de una vez. ¡Volveremos después de clases!"
red @angrybrow talking2mouth "Y nada de escaparte y seguirme, ¿entendido?"

$ renpy.music.play("Audio/Pokemon/pikachu_happy2.ogg", channel="altcry", loop=None)

pikachu happy_3 "Piiiikaaaa.~"

pause 2.0

show calem:
    xpos 0.25
    ease 1.0 xpos 0.4

show ethan:
    xpos 0.5
    ease 1.0 xpos 0.6

show brendan:
    xpos 0.75
    ease 1.0 xpos 0.8

show hilbert uniform:
    xpos -0.5 xzoom -1
    ease 1.0 xpos 0.2

pause 2.0

red @confused "¿Sí?"

hilbert @closedbrow talkingmouth "Iremos a la cafetería, ¿no?"

ethan @playfulbrow talking2mouth "Me imaginé que no querrías venir."

hilbert @sadbrow talkingmouth "Necesito comer para sobrevivir.{w=0.5} No pensé que tendría que decírtelo..."

calem @closedbrow talkingmouth "Podrías ir solo."

hilbert @talkingmouth "Podría..."

brendan @happy "¿Pero no quieres?"

hilbert @angrybrow talkingmouth "Las circunstancias bajo las que operaba han cambiado. Ahora quiero ir a la cafetería y disfrutar de un delicioso desayuno con ustedes. ¿Quieren saber la historia de mi vida, o podemos dejarlo así?"

pause 1.0

ethan @happy "Bueno... Supongo que vamos, entonces. ¡Es bueno tenerte con nosotros, Happenstance!"

show hilbert:
    xpos 0.2
    ease 1.0 xpos 1.5

pause 1.0

$ PlaySound("Door_Close1.ogg")

red @closedeyes sadeyebrows talkingmouth "En realidad, uh, es Hilbert."

ethan surprisedbrow frownmouth @surprised "¿Por qué? ¿Qué dije?"

pause 0.75

window hide

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_2

show blank2 with dis:
    alpha 1.0
    
$ renpy.pause(2.0, hard=True)

hide ethan
hide brendan
hide hilbert
hide calem

show relichall_A behind brendan with dis
    
pause 1.0

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with dis

show may uniform with dis
    
$ renpy.pause(1.0, hard=True)

red @talkingmouth "¡Oh, hey, May! ¿Llevas mucho esperando?"

show may:
    xpos 0.5
    ease 0.5 xpos 0.33

show brendan uniform with dis:
    xpos 0.66
    
hide blank2

may @happy "¡Nah! ¡Qué bueno verte de nuevo! No te vi mucho el fin de semana."

red @happy "Bueno, aunque Brendan y yo hicimos los mismos mandados, no planeaba ser la tercera rueda todo el tiempo."

may @sadbrow talkingmouth "Hablando de ser la tercera rueda...{w=0.5} todavía no has conocido a mis otras compañeras de cuarto además de Serena, ¿verdad?"

red @talkingmouth "Con suerte, nos cruzaremos con algunas de ellas hoy de camino a clase."

may @happy "Bueno, si veo a alguna, te avisaré. Oh, eso me recuerda, cariño, ¿ya le diste a [first_name] tu número de teléfono?"

brendan @surprised "¡Ah! No, no lo hice. ¡Aquí tienes, [first_name]!"

show brendan happy with dis

$ BecomeContacted("Brendan")

brendan -happy @talking2mouth "Oye, ¿por qué no le das tu número también? Así, si mi teléfono está apagado o algo, aún puede contactarme."

may @surprised "¿Eh? Oh, um, ¡claro! Si estás de acuerdo con eso."

red @talkingmouth "No hay problema."

show may happy 
with dis

$ BecomeContacted("May")

show may -happy with dis

ethan uniform @happy "¡Muy bien, vamos! No sé si es mi estómago o Hillenbrand gruñendo, pero no es nada que un gran plato de huevos revueltos no pueda arreglar."

scene cafe with Dissolve(1.5)
$ renpy.pause(1.5, hard=True)

hide blank2

red uniform @surprisedbrow talking2mouth "¡Guau! Esto si que es muy lujoso."

show calem uniform with dis:
    xpos 0.166

calem @talkingmouth "Supongo que tales lujos estaban un poco fuera de alcance en Ciudad Paleta, ¿no?"

red @wince talking2mouth"Sí."

show ethan uniform with dis:
    xpos 0.333

ethan @talkingmouth "¡Apuesto a que no es nada parecido a Kalos! Escuché que hasta su pueblo más pequeño tiene un restaurante de cinco estrellas."

calem @surprised "Has... oído muchas cosas interesantes sobre Kalos."

show calem:
    xpos 0.166
    ease 5.0 xpos 0.07

show brendan uniform with dis:
    xpos 0.499

brendan @happy "¡Oye, May, mira! ¡Tienen hasta tartar de Basculin!"

show may uniform with dis:
    xpos 0.666

may @sadbrow talkingmouth "Sí, pero eres vegetariano, cariño..."

brendan @happybrow angrymouth "Eh... ¡Por supuesto! No lo olvidé. Es solo que... ¡{i}tartar de Basculin{/i}! ¡Qué elegancia la de Francia!"

show hilbert uniform with dis:
    xpos 0.833

hilbert @sadbrow angrymouth "{size=30}Maldición, ¿dónde {i}está{/i}? Vamos, sal de una vez...{/size}"

redmind @thonk "¿A que se referiría con {i}eso{/i}?"

show hilbert with dis

show calem:
    xpos 0.07 xzoom 1.0
    ease 0.5 xzoom -1.0

pause 1.5
    
calem @talkingmouth "Oh, miren quién se nos une esta mañana."

show calem:
    xpos 0.07 xzoom -1
    ease 0.5 xpos (2.0/7.0)

show ethan:
    xpos 0.333
    ease 0.5 xpos (3.0/7.0)

show brendan:
    xpos 0.499
    ease 0.5 xpos (4.0/7.0)

show may:
    xpos 0.666
    ease 0.5 xpos (5.0/7.0)

show hilbert:
    xpos 0.833
    ease 0.5 xpos (6.0/7.0)

show serena uniform:
    xpos -0.5
    ease 1.0 xpos (1.0/7.0)

pause 1.5

ethan @happy "Espera, espera, no me lo digas. Tu siguiente frase sera 'espacio personal', ¿verdad, Calem?"
calem @sadbrow talkingmouth "Iba a decir eso, pero ahora parece redundante."

redmind @thonk "Hmm... Serena. Calem habló con ella varias veces durante el fin de semana, pero parece que todavía la trata con una obvia y forzada normalidad."
redmind @thonk "Añadiré eso a mi lista de 'cosas para preguntar cuando seamos más cercanos'."

red @talkingmouth "Buenos días, Serena."

serena @talkingmouth "Buenos días, [first_name]. ¿No te ves apuesto con tu nuevo uniforme?"

calem @surprised "¡!"
calem @closedbrow happymouth "Sí, ¿verdad? Francamente, le queda bastante bien."

serena @sadbrow talkingmouth "Ah, bueno, ciertamente es un nuevo look. Tal vez solo me haya acostumbrado a verte {i}a ti{/i} así."

calem @angrybrow talking2mouth "...{w=0.5} Sí, tal vez."

pause 2.0

redmind @confusedeyebrows frownmouth "¿Qué clase de juegos mentales están jugando estos dos?"

hilbert @talkingmouth "Oye. ¿Tu compañera de cuarto Hilda está por aquí?"

serena @surprised "Oh? No, I don't believe so. She said she was looking for someone."

ethan @surprised "¡Oh-oh!"

brendan @surprisedbrow talking2mouth "¿Qué pasa, bro?"

ethan @sweat closedbrow talkingmouth "Cada vez que hablamos de alguien, aparece. Así que Hilda probablemente llegará en cualquier momento."

hilbert @angry "No seas supersticioso."

ethan @happy "No es eso, solo que no creo que podamos {i}físicamente{/i} meter a más personas en pantalla."

hilbert @sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."

hilbert @closedbrow talkingmouth "Eso no tiene ningún sentido, mejor voy a buscarnos una mesa."

show hilbert:
    xpos (6.0/7.0)
    ease 1.0 xpos 1.5

ethan happy "Mejor lo acompaño para asegurarnos de que no se meterá en problemas."

show ethan:
    xpos (3.0/7.0)
    ease 1.0 xpos 1.5

show may happy with dis

brendan happy "No sé ustedes, pero yo voy a buscar algo para llenar el estomago."

show brendan:
    xpos (4.0/7.0)
    ease 1.0 xpos -0.5

show may:
    xpos (5.0/7.0)
    ease 1.0 xpos -0.5

pause 2.0

serena @talkingmouth "Bueno, ahora que tus amigos se han apartado un momento, ¿podemos hablar?"

show calem: 
    xpos (2.0/7.0)
    ease 0.2 xpos 0.75

show serena sadbrow with dis:
    xpos (1.0/7.0)
    ease 1.0 xpos 0.25

calem @talking2mouth "Sí, podriamos hacerlo."

redmind @thinking "Auch, que frio."

redmind @surprisedbrow frownmouth "Espera un segundo, ¡yo todavía sigo aquí!"

serena sadbrow @talkingmouth "... Se trata de..."

show calem thinking with dis

serena sadbrow frownmouth "[ellipses]"

serena -sadbrow -frownmouth @sadbrow talkingmouth "El consejo estudiantil."

calem -thinking @surprised "¿Oh?"

stop music fadeout 1.5
queue music "Audio/Music/Waltz of the Sea_start.ogg" noloop
queue music "Audio/Music/Waltz of the Sea_loop.ogg"

serena @talkingmouth "Hemos hecho trabajo de liderazgo antes, ¿verdad, Calem?{w=0.5} Ser miembro del Consejo Estudiantil Kobukan en nuestro currículum sería muy, muy atractivo para futuros empleadores."

calem @closedbrow talking2mouth "Hmm. No conozco los detalles, pero he oído que es muy difícil entrar en el Consejo Estudiantil de Kobukan."

serena @closedbrow talkingmouth "Sí, solo tendríamos un mes para hacer campaña." 
serena @happy "Pero ya hemos superado juntos obstáculos mayores"
serena @talkingmouth "¿Recuerdas las pasantías del profesor Ciprés, y lo mucho que trabajamos para conseguirlas?"

calem smilemouth @happy "Cierto. Nunca lo habría conseguido sin tu incesante apoyo."

serena @closedbrow talkingmouth "En cualquier caso, creo que deberíamos intentarlo. Como solo tenemos un mes para hacer campaña, si fallamos... bueno, al menos no habremos perdido demasiado tiempo."

calem @closedbrow talking2mouth "En efecto. Sería un compromiso de tiempo importante, mucho más si ganamos, pero quizá sea algo a considerar."

serena @sadbrow talkingmouth "Bueno... Tenemos que decidirnos, ya que es nuestro tercer día aquí y ese tipo 'Cheren' ya ha pegado carteles en la mitad de la academia y está dando discursos en el patio."

calem @sadbrow talkingmouth "Sí, bueno... dadas las políticas que defiende, no me sorprendería que la administración de la academia lo hiciera desaparecer antes del fin de semana."

serena @happy "Puede que debamos ser un poco {i}menos{/i} radicales para mantener nuestra elegibilidad."

calem @closedbrow talking2mouth "Sí, un poco."

serena @thinking "[ellipses]"

calem @thinking "[ellipses]"

serena @pout "[ellipses]"

serena @sadbrow talkingmouth "¿Y bien?"

calem @sad "No estoy... seguro. Realmente necesito un poco más de tiempo para decidir, ¿podrías darme hasta mañana?"

serena @pout "[ellipses]"
serena @happy "¡Está bien! Pero me {i}vas{/i} a responder mañana, ¿verdad?"

calem @closedbrow talkingmouth "Lo juro."

serena @happy "¡Esplendido! Reunámonos aquí mañana por la mañana para terminar de resolver esto. ¡Adiós, Calem! ¡Adiós, [first_name]!"

menu:
    "Adiós, Serena.":
        redmind @thinking "Oh, así que sí {i}sabía{/i} que estaba aquí. Ya me estaba preguntando..."
       
    "¡Espera, cuenten conmigo!":
        $ council_campaigning = True

        show calem surprisedbrow -smilemouth
        show serena surprisedbrow frownmouth
        with dis

        red @happy "Calem puede que necesite más tiempo, pero yo no. Quiero unirme a ustedes en el Consejo Estudiantil."
        
        $ ValueChange("Serena", 1, 0.25, False)
        $ ValueChange("Calem", 1, 0.75)

        pause 1.5
        
        calem -surprisedbrow @sadbrow talkingmouth "¿Oh? ¿Tienes... alguna experiencia en este tipo de trabajo?"
        
        show serena -surprisedbrow -frownmouth with dis

        red @sweat happy "Hombre, vengo de Pueblo Paleta. Sabes que no."
        
        red @talkingmouth "Pero siempre estoy listo para aprender. Tengo un mes, ¿no?"
        
        serena @sadbrow happymouth "Bueno... será complicado. Pero estaré encantada de ayudarte, si aceptas mi tutela."
        
        calem @closedbrow talkingmouth "Hmm. Tienes esa confianza en ti mismo y un cierto carisma que podrían hacerte popular entre los estudiantes, si pudiéramos refinar un poco tus posiciones..."
        
        red @happy "Sí. Sé que tengo un mes de campaña por delante y, sinceramente, ni siquiera sé por dónde empezar. ¿Algún consejo?"
        
        calem @closedbrow talking2mouth "Bueno... yo intentaría hablar con el actual Consejo Estudiantil. Si consigues el respaldo del consejo anterior, tienes casi garantizada la entrada."
        
        serena @closedbrow talkingmouth "También podrias apostar por el sondeo. Ir de estudiante en estudiante y hablarles directamente de tus propuestas e intentar convencerlos."
        
        calem @closedbrow talkingmouth "Como último recurso, puedes confiar en el reconocimiento de tu nombre. Cualquier cosa que te ponga en el ojo público, sea bueno o malo, aumenta tus probabilidades."
        
        red @confused "Espera, ¿bueno {i}o{/i} malo?"
        
        calem @sad "Lamentablemente, así es el mundo de la política."
        
        serena @happy "De todos modos, qué agradable sorpresa. No parecías el tipo de persona que querría involucrarse en algo como esto."
        
        calem @happy "¡[first_name] está lleno de sorpresas!"
        calem @closedbrow talking2mouth "Oh, si ustedes dos definitivamente van a trabajar juntos en el Consejo Estudiantil, deberían intercambiar sus contactos."
        
        serena @sad "[ellipses]"
        serena @talkingmouth "Sí, por supuesto."
        
        redmind @thonk "Hm. ¿Me lo imaginé, o...?"

        $ BecomeContacted("Serena")
        
        serena @happy "Espléndido. Estoy deseando hablar con ustedes sobre nuestro meteórico ascenso al Consejo Estudiantil. Calem, [first_name]."

show serena at dissolveaway:
    xpos 0.25

show calem:
    xpos 0.75
    ease 1.0 xpos 0.5

pause 2.0

menu:
    "¿Cuál es tu problema?":
        red @angrybrow talking2mouth "¿Cuál es tu problema?"
        
        calem angrybrow frownmouth @talking2mouth "¿Disculpas?"
        
        red @talking2mouth "Ella es amable, hermosa y obviamente está loca por ti. Y la tratas como si fuera una molestia."
        red @talking2mouth "Y sé que te gustan las chicas, así que ¿por qué no le correspondes?"

        $ ValueChange("Calem", -1, 0.5)

        calem @angry "Lo siento, pero simplemente no voy a hablar de esto contigo."

        red @closedbrow talking2mouth "{i}Suspiro{/i}... Está bien. Puedo ver que es un tema complicado con el que llevas lidiando mucho antes de conocerme. Aun así, tienes que tener los pies en la tierra."
        
        calem @angrybrow talking2mouth "{cps=*0.2}Aprecio el consejo.{/cps}"
        calem -sad @closedbrow talking2mouth "¿Nos vamos?"
       
    "Parece alguien agradable.":
        red @happy "Parece ser una chica agradable."
        
        calem sad "Lo es, mucho más de lo que merezco."
        calem "[ellipses]"
        calem -sad @closedbrow talking2mouth "Bueno, suficiente de esto. ¿Nos vamos?"

    "¿Estás bien?":
        red @sadeyebrows sadeyes talkingmouth "¿Te encuentras bien?"
        
        calem @sad "... Estoy luchando con la idea de si debería unirme al Consejo Estudiantil.{w=0.5} Realmente quiero hacerlo, pero pasaría casi todos los días con ella..."
        calem @angrybrow talking2mouth "Y está bastante claro que eso es exactamente lo que ella quiere."
        
        red @confused "¿Y tú no quieres eso?"
        
        calem @happy "Yo...{w=0.5} ya no estoy seguro de lo que quiero, para ser honesto."
        
        $ ValueChange("Calem", 1, 0.5)
        
        calem @sadbrow talkingmouth "Pero te agradezco que me dejes desahogarme mientras lo descubro."
        calem @talkingmouth "Bueno, suficiente de esto. ¿Nos vamos?"

red @talkingmouth "Sí, vamos a desayunar con los demás."

if council_campaigning:
    redmind @thinking "Ahora que estoy intentando entrar en el Consejo Estudiantil, debería decírselo a Cheren. ¡Quizás podríamos intercambiar consejos!"

scene cafe with Dissolve(1.5)

show bianca uniform with dis

bianca @thinking "[ellipses]"
redmind uniform "[ellipses]"

show bianca happyeyes with dis:
    ypos 1.0 zoom 1.0
    ease 0.2 ypos 1.05 zoom 1.1

redmind @confusedeyebrows frownmouth "¿...?"

show bianca happyeyes with dis:
    ypos 1.05 zoom 1.1
    ease 0.2 ypos 1.1 zoom 1.2

calem uniform @talkingmouth "Se está acercando a ti."
red @closedeyes talking2mouth "Sí, yo me encargo, gracias."

show bianca excitedeyes:
    ypos 1.1 zoom 1.2
    ease 0.2 ypos 1.15 zoom 1.3

redmind @surprised "¿Por qué estoy sudando tanto?"

show bianca excitedeyes:
    ypos 1.15 zoom 1.3
    ease 0.2 ypos 1.2 zoom 1.4

red talking2mouth "Hola, eh, ¿puedo ayudarte?"

$ BecomeNamed("Bianca")

bianca @happy "¡Hola! Soy Bianca. Cheren me dijo que buscara al 'chico guapo con la gorra roja'."

red @surprised "Eh..."

bianca @happymouth "Así que, por supuesto, pensé que eras tú, pero antes pensé que era el otro chico con la gorra roja, pero solo me miró con cara de pocos amigos, y luego pensé que era el otro otro chico  con la gorra roja, pero entonces él dijo--"
bianca -excitedeyes @happy "--que no tenía idea de quién era Cheren, así que ahora te estoy preguntando a ti y ¡realmente espero que seas tú porque me estoy poniendo muy nerviosa hablando con tantos chicos lindos con una gorra roja!"

show calem uniform surprisedbrow at dissolvein:
    xpos 0.25

calem @sadbrow talkingmouth "Espera... ¿por qué no me preguntaste a mí?"

show bianca:
    ypos 1.2 zoom 1.4 xpos 0.5
    ease 1.0 ypos 1.0 zoom 1.0 xpos 0.75

bianca @happy "Oh, eres lindo, de verdad, pero creo que Cheren estaba buscando a un estudiante, ¡no a un profesor!"

show calem deadbrow surprisedmouth at monochrome with vpunch:
    ypos 1.0 xpos 0.25
    ease 1.0 ypos 1.1 rotate 5.0    

calem @talkingmouth "Yo... tengo dieciocho..."

show calem at monochrome:
    ypos 1.1 rotate 5.0 xpos 0.25
    ease 0.5 ypos 2.0 rotate 30.0

show bianca:
    ypos 1.0 zoom 1.0 xpos 0.75
    ease 1.0 ypos 1.2 zoom 1.4 xpos 0.5

bianca @talkingmouth "De todos modos, ¿eres [first_name]? Porque Cheren está impaciente, y el primer chico con la gorra roja está en nuestra mesa discutiendo con mi compañera de cuarto, Hilda, y--"

red @surprised "Espera, ¿dijiste Hilda?"

bianca @happy "Oh, ¿la conoces?"

red @confused "Bueno, sé {i}de{/i} ella. Al parecer, es lo único que asusta a Hilbert."
red @closedbrow sweat talking2mouth "Uh, el primer chico con la gorra roja se llama Hilbert."

bianca @talkingmouth "Okay.{w=0.5}.{w=0.5}.{w=0.5} Entonces, ¿eres [first_name]?"

red @happy "¡Oh, sí! ¿Cheren me necesita ahora? Porque estaba a punto de buscar algo de comer para ir a desayunar con mis compañeros de cuarto."

bianca @talkingmouth "Nope, sólo quería que te diera un mensaje."

redmind @thinking "¿Qué? ¿Como si fuera un mafioso? '[first_name] dormiras con los peces...'"

bianca @unamusedbrow trianglemouth "Por favor, ven aquí después de clases. Me gustaría hablar contigo."

red @confused ".{w=0.5}.{w=0.5}.{w=0.5} ¿Eso es todo?"

bianca @talkingmouth "¡Sipi!"

red @happy "Eh, está bien entonces. Estaré en la cafetería más tarde."

bianca happy "¡Misión completada!"

show bianca:
    xpos 0.5 ypos 1.2 zoom 1.4
    ease 2.0 xpos 1.5 ypos 1.0 zoom 1.0

redmind @thonk ".{w=0.5}.{w=0.5}.{w=0.5} No puedo decir si esto es simplemente lo normal en esta ciudad, o hay algo en mí que solo atrae a personas raras."
redmind @thinking "¿Y si soy yo el raro?"

show blank2 with dis

pause 2.0

red @happy "¡Hey chicos!"

ethan uniform @talkingmouth"Hey, [first_name], ¿por qué tardaste tanto? Calem volvió hace poco y parece estar algo shockeado."

red @talkingmouth "Solo estaba hablando con otra estudiante. Oye, ¿no habías dicho de que ibas a evitar que Hilbert se metiera en problemas?"

ethan @surprised "¿¡Qué?! ¡Pensé que lo hice! ¡Estaba aquí hace un momento!"

red @talking2mouth "Bueno, me acabo de enterar de que esa chica 'Hilda', a la cual tanto miedo tiene, acaba de encontrarlo. Supongo que tiene sentido que no pudiera esconderse por más de cuatro días."

pause 1.0

brendan uniform angrymouth closedbrow "¡Chicos!, no quiero apurarlos pero esta apunto de empezar la primer clase."

may uniform surprised "¡Caray, tienes razón! Supongo que tengo que terminar de comer esto rápido antes de irnos..."

ethan @sweat lightblush sadbrow talkingmouth "Oye, podrías, no sé, ¿ponerte una tostada en tu boca y correr a clase?"

may frownmouth sadbrow @talking2mouth "...{w=0.5} Podría, pero no veo por qué. Tengo tiempo para terminarla aquí."

ethan sadbrow happymouth "Ah... Eh... Mejor olvídalo."

brendan @angrybrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

brendan @talkingmouth sweat closedbrow "Juro que esto me recuerda algo que una vez dijo Wally. Algo sobre anime."

pause 1.0

hide calem

red @sadbrow talkingmouth "Hey, Calem, ¿vas a estar bien?"
calem uniform sad "{size=30}Tengo dieciocho, no soy viejo, mi cabello es naturalmente gris. Tengo dieciocho, no soy viejo, mi cabello es naturalmente gris.{/size}"

red @confused "Claaaaaro... Bueno, eh... tenemos que irnos. No te quedes muy atrás, ¿vale?"

calem surprisedbrow frownmouth @surprised "¿Eh?" 
calem sad "Oh, sí, por supuesto. Solo... denme un segundo."

pause 1.0

red @happy "Bien, vamos. ¡El último en llegar al tablero de asignación de clases es un HUEVO MALO!"

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_3
scene blank2 with dissolve

$ renpy.music.stop(channel='crowd', fadeout=1.5)
stop music fadeout 1.5
$ renpy.pause(1.5, hard=True)
play music "Audio/Music/Beyond.ogg" loop fadein 3.0

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.5)
$ renpy.pause(3.0, hard=True)

$ renpy.transition(dissolve)
show screen currentdate

scene academyold with Dissolve(2.0)

$ renpy.pause(2.0, hard=True)

hide blank2
hide cafe

show academy:
    xpos 0 ypos 0 zoom 0.625
    ease 3.0 zoom 1.0 xpos -700 ypos -575

$ renpy.pause(3.0, hard=True)

red uniform @surprised "¡Guau, esta parte del campus es increíble!"

show academy:
    zoom 1.0 xpos -700 ypos -575
    ease 1.0 zoom 1.1 xpos -730 ypos -300
$ renpy.pause(1.2, hard=True)

red @talkingmouth "¿Ven lo que dice en la fachada?"
red @angrybrow talkingmouth "'Academia Kobukan.' Está escrito en Unown antiguo."
red @happy "¿Sabían que esta academia fue fundada en 1636?{w=0.5} Es difícil de creerlo, el estado de este lugar hace que parezca que fue construido ayer."

show academy:
    zoom 1.1 xpos -730 ypos -300
    ease 1.0 zoom 1.05 xpos -730 ypos -300
$ renpy.pause(1.0, hard=True)

red @talkingmouth "Me cuesta imaginar que esto es lo que veré todos los días a partir de ahora."

show academy:
    zoom 1.05 xpos -730 ypos -300
    ease 1.5 zoom 1.0 xpos -700 ypos -575
$ renpy.pause(2.0, hard=True)

red @happy "No es que me queje.{w=0.5} Solo estoy emocionado de estar aquí.{w=0.5} Igual que ustedes, ¿verdad?"

pause 1.0
show academy:
    zoom 1.0 xpos -700 ypos -575
    ease 0.5 zoom 0.9 xpos -800 ypos -450
pause 1.0
show academy:
    zoom 0.9 xpos -800 ypos -450
    ease 0.75 zoom 0.85 xpos -100 ypos -350
pause 2.0
show academy:
    zoom 0.85 xpos -100 ypos -350
    ease 1.0 zoom 1.0 xpos -700 ypos -525
$ renpy.pause(2.0, hard=True)

redmind @thinking "Uh, supongo que corrí un poco demasiado rápido."
redmind @happy "Eh, da igual. Necesito entrar y revisar a que clase me asignaron."

show academy:
    zoom 1.0 xpos -700 ypos -525
    ease 4.0 zoom 1.4 xpos -600 ypos -600
$ renpy.pause(1.0, hard=True)

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_4

scene blank with Dissolve(1.0)
$ PlaySound("ExitBuilding.ogg")

stop music fadeout 2.25
$ renpy.music.stop(channel='crowd', fadeout=1.5)
$ renpy.pause(3.0, hard=True)

$ renpy.music.play("Audio/hall_crowd.ogg", channel='crowd', loop=True, fadein=1.5)
scene academyhall with Dissolve(1.5)

$ renpy.transition(dissolve)
show screen currentdate
$ renpy.pause(1.5, hard=True)

hide blank
hide academy
hide academyold

redmind uniform "Hay un grupo de estudiantes reunidos junto a un tablón de anuncios.{w=0.5} Ese debe ser la lista de clases."

window hide
show academyhall_blur with dis:
    alpha 1.0

show class_assign:
    alpha 0.0 xalign 0.5 ypos -50
    ease 1.0 alpha 1.0

python:
    fontsize = 15
    if (len(last_name) > 12):
        fontsize = 10

show text "{font=fonts/consola_0.ttf}{color=#000000}{size=[fontsize]}{b}[last_name], [first_name[0]].{/b}{/size}{/color}{/font}":
    alpha 0.0 xanchor 188 ypos 634
    ease 1.0 alpha 0.7

$ renpy.pause(2.0, hard=True)

redmind surprisedbrow frownmouth @surprised "{w=0.5}.{w=0.5}.{w=0.5}."
redmind "Espera, ¿Oak?"
redmind "¿Profesor Oak? ¿Sam? ¿Mi vecino? ¡¿El abuelo de [blue_name]?!"
redmind "¿Él enseña aquí? ¡La página de profesores en la web no decía nada de esto!"
redmind angrybrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
redmind angrybrow "Y... ¿por qué mi nombre está en una fuente diferente? Parece que alguien simplemente lo escribió a mano..."

blue uniform "¡Vaya, vaya, vaya!"

show academyhall_blur:
    alpha 1.0
    ease 0.5 alpha 0.0
show class_assign:
    alpha 1.0
    ease 0.5 alpha 0.0
show text "{font=fonts/consola_0.ttf}{color=#000000}{size=[fontsize]}{b}[last_name], [first_name[0]].{/b}{/size}{/color}{/font}":
    alpha 1.0 xanchor 188 ypos 634
    ease 0.5 alpha 0.0

red @frownmouth "[ellipses]"

show blue with dis:
    xpos 1600
    ease 0.75 xpos 700

play music "Audio/Music/RivalTune.ogg" noloop
$ renpy.music.queue("Audio/Music/Road to Viridian City.ogg", channel='music', loop=True, fadein=4.0, tight=None)

$ renpy.pause(0.75, hard=True)

hide class_assign
hide academyhall_blur
hide text
    
blue @angry "Dije, ¡VAYA, VAYA, VAYA!"
red @upeyes talking2mouth "Te escuché la primera vez."
blue @angrybrow happymouth "¡Al menos mírame cuando te hablo!"
blue @happy "Pero, guau, ¡de verdad llegaste antes la campana!{w=0.5} No antes que yo, pero eso es natural."
redmind -angrybrow @confusedeyebrows frownmouth "¿En qué mundo he sido yo {i}más{/i} lento que tú?"
blue @closedbrow talking2mouth "¿Y bien?{w=0.5} ¿En qué clase estás?"
show blue surprisedbrow frownmouth with dis
red @talking2mouth "En la de tu abuelo, según esto.{w=0.5} ¡Podrías haberme dicho que Sam trabajaba aquí! Hubiera visto si podía hacerme un favor"
blue @talkingmouth "¿La de mi abuelo? ¿Hablas en serio?"
blue sad "¿Por qué?{w=0.5} Pensé que le dije que--"
$ renpy.pause(1.0, hard=True)
blue angry "¡Ah, qué más da!" 
blue closedbrow -angrymouth @talkingmouth "¡Ahora tengo asiento en primera fila para verte fracasar estrepitosamente en clase!"

$ showredonly = True

leaf uniform "¡Oh! ¿Ustedes también están con el Profesor Oak?"

redmind surprisedbrow frownmouth @surprised "Esa voz..."

$ showredonly = False

show blue surprisedbrow frownmouth with dis:
    xpos 700
    ease 0.5 xpos 450

show leaf uniform:
    alpha 0.0 xpos 1800 
    ease 0.75 xpos 970 alpha 1.0
    
$ renpy.pause(0.75, hard=True)

show blue surprisedbrow frownmouth with dis:
    xpos 450

show leaf:
    xpos 970 alpha 1.0

red @talkingmouth "¿Oh? Hey, ¡eres tú!"
leaf @happy "¡Cuánto tiempo sin verte!"
leaf @flirtbrow talkingmouth "¿Te perdiste en el camino para llegar aquí?"

show blue angry with dis

red @pity "Hey, dame un respiro, pensé que ya habíamos superado eso.{w=0.5} ¿No dijiste que te habías divertido?"

leaf @flirtbrow talkingmouth blush "Oye, no lo malinterpretes.{w=0.5} ¡Me divertí mucho!"

show leaf angrybrow frownmouth with dis

blue frownmouth -angry @sad2eyes talkingmouth"¿Conoces a este charlatán?"

leaf @angrybrow talking2mouth "Eh, disculpa.{w=0.5} No interrumpas a una chica cuando está hablando con su {i}amigo{/i}."

show leaf surprisedbrow frownmouth with dis

blue @closedbrow talkingmouth "Sí, claro. Apuesto a que ni siquiera sabes su nombre."

pause 1.0

leaf embarrassed @embarrassedbrow talking2mouth "Obviamente es..."

window hide
pause 1.5

leaf @frownmouth "[ellipses]"

show leaf at getcloser:
    xpos 970
    ease 0.9 xpos 840
    
$ renpy.pause(0.9, hard=True)

redmind @thinking lightblush"Huh. Puedo oler su perfume."

leaf flirtbrow blush @talking2mouth "{size=30}Psst, ¿cómo te llamabas?{/size}"

red @sad2eyes talkingmouth lightblush "{size=30}Es, eh, [first_name] [last_name].{/size}"
red @closedbrow talkingmouth "{size=30}Y, eh, ¡soy un firme creyente del espacio personal!{/size}"

show leaf at getfurther:
    xpos 840
    ease 0.9 xpos 970

leaf -flirtbrow @happy "¡Ah, sí! ¡[first_name]!{w=0.4} ¡Somos los mejores amigos! ¡Siempre lo hemos sido!"

blue @closedbrow angrymouth "¡No engañas a nadie!"

leaf @surprised "Espera...{w=0.5} ¿[first_name]?"
leaf @happybrow talkingmouth "¡[first_name]! Oh, ¿eres [first_name]?{w=0.5} ¿Eres amigo de May, cierto?"

red @talkingmouth "¿Conoces a May?"

leaf @winkbrow talkingmouth "Eso espero, soy su compañera de cuarto."

redmind @thinking "Bien... he conocido a Bianca, Serena y May... así que, echando una moneda al aire, y teniendo en cuenta que no {i}parece{/i} una Hilda..."

red @talkingmouth "¿Eres Leaf?"

$ BecomeNamed("Leaf")

leaf @happy "¡Ese es mi nombre!"

blue @surprisedbrow angrymouth "Por Dios... ¡deja de fingir!{w=0.5} ¡Tu actuación es tan mala que me está enfadando!"

red @closedbrow sweat talking2mouth "Déjalo, [blue_name]. Sé quién es Leaf."
red @talkingmouth "La conocí en nuestro primer día aquí y me ayudó a salir de un apuro.{w=0.5} Ambos íbamos con prisa y olvidamos presentarnos--"

show leaf surprisedbrow frownmouth with dis

blue @closedbrow angrymouth "¡Me importa una mierda de Rattata lo que pasó!"

pause 0.7

blue @angrybrow talkingmouth "Ugh, ya han desperdiciado suficiente de mi tiempo. Tengo que encontrarme con un amigo, uno {i}de verdad{/i}, no como esta farsa que {i}tú{/i} haces."
blue angrybrow happymouth "¡Me piro, vampiro!"

show blue:
    alpha 1.0 xpos 450
    parallel:
        ease 0.65 xpos 1000
    parallel:
        ease 0.5 alpha 0.0

$ renpy.pause(2, hard=True)
    
leaf @talking2mouth "{i}¿Me piro vampiro?{/i}{w=0.5} ¿Qué se supone que significa eso?"

hide blue

red @closedbrow sweat talking2mouth "Así es Blue... o como lo llamo yo, '[blue_name].'{w=0.5} Ha dicho eso desde que lo conozco.{w=0.25} Y lo conozco desde hace mucho tiempo."
red @closedeyes talking2mouth "No es algo de lo que esté particularmente orgulloso."

leaf flirtbrow -frownmouth @talkingmouth "Entonces, ¿te ha estado succionando sangre por mucho tiempo?{w=0.5} Qué raro."

red @closedbrow sweat talking2mouth "No se refería a eso..."

leaf happy "¡Ja, ja, ja!{w=0.5} Vamos, [first_name], ¡llegaremos tarde a nuestra primera clase!"

window hide

show leaf happy:
    alpha 1.0 xpos 970
    parallel:
        ease 0.5 xpos 1120
    parallel:
        ease 0.5 alpha 0.0
        
$ renpy.pause(1.5, hard=True)

redmind @thinking "Leaf, ¿eh?{w=1} Y [blue_name],{w=1} y yo,{w=0.5} en la misma habitación durante dos horas."

hide leaf

redmind @thinking "Todos los días, dos veces al día, durante el próximo año."
redmind @thinking "[ellipses]"
redmind @happy "Este año va a ser muy interesante."

window hide

show academyhall:
    subpixel True
    zoom 1.0 xpos 960 ypos 1080
    ease 3.5 zoom 1.5 xpos 850 ypos 1320
$ renpy.pause(1.0, hard=True)

show blank2 with dis:
    alpha 1.0

$ renpy.pause(1.0, hard=True)
$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_5
$ renpy.music.stop(channel='crowd', fadeout=1.5)
stop music fadeout 1.5
$ renpy.pause(2.0, hard=True)

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

scene homeroom with Dissolve(2.0)

show oakbg:
    xpos 2500

$ renpy.transition(dissolve)
show screen currentdate
$ renpy.pause(1.5, hard=True)

hide blank2
hide academyhall

show leaf uniform with dis:
    xpos 430
    ease 0.5 xpos 550

show may uniform with dis:
    xpos 1120
    pause 0.5
    ease 0.5 xpos 1000

leaf @happy "¡May! ¡No puedo creer que estemos en la misma clase!"

show leaf:
    xpos 550

show may:
    xpos 1000

red uniform @talkingmouth "Ñas coincidencias de hoy no dejan de acumularse."

may @talkingmouth "¡El mundo es un pañuelo!{w=0.5}"
may @happy "[first_name], veo que finalmente tú y Leaf se conocieron."

leaf @flirtbrow talkingmouth "May, ¿recuerdas al chico del que te hablé cuando nos conocimos?"

show may surprisedbrow frownmouth with dis

leaf @happy "Resulta que lo conociste todo este tiempo."

may -surprisedbrow -frownmouth @sadbrow talkingmouth "Oh, [first_name]. Como te adelantaste sin nosotros después del desayuno, ahora entiendo perfectamente cómo lograste perderte en el primer día."
may @happy "Pero está bien, ¡tener un gran sentido de la aventura es algo bueno!"

red @closedeyes talking2mouth "Nunca voy a poder dejar esto atrás, ¿verdad?"

leaf @blush happybrow talkingmouth "Un chico, varado en el territorio prohibido del terrible equipo de animadoras. Presintiendo la inminente perdición, escogió su veneno y buscó refugio en el baño de damas." 
leaf @sadbrow cry talking2mouth blush "Fue entonces cuando una hermosa doncella, una chica de la que nada sabía, tropezó con él en el momento oportuno, tirando de él hacia la luz y guiándole hacia el santuario."

show leaf -blush happy
show may happy 
with dis

red @angrybrow talking2mouth "Gracias por el resumen épico."

if leafwindowjump == True:
    red @angrybrow talking2mouth "Y para que quede en el registro, ¡tú fuiste la que me {i}forzó{/i} a entrar al baño!{w=0.5} Me gustaba más mi idea de la ventana."
else:
    pass

show leaf flirt blush:
    xpos 550 ypos 1080
    ease 0.5 ypos 1120 xpos 530
    pause 1.0
    ease 0.5 ypos 1080 xpos 550

pause 1.0

redmind @thonk "¿Una reverencia? Es increíblemente engreída."

show leaf -flirt -blush
show may -happy 
with dis

red @talkingmouth "Ya que estás aquí, May, supongo que Brendan está en otra clase."

may @happy "Brendan está en la Clase 1-A, la dé al lado."

leaf @talkingmouth "Oh, in your Dad's."

show leaf surprisedbrow frownmouth
show may surprisedbrow frownmouth 
with dis

oak @talkingmouth "Deberías decirle a tu padre, Señorita Birch,{nw}"

show oak with dis:
    xpos 150
    ease 1.5 xpos 300

show leaf:
    xpos 550
    ease 0.65 xpos 800

show may:
    xpos 1000
    ease 0.75 xpos 1200

extend @talkingmouth " que su reciente artículo sobre los pros y los contras de los Pokémon Bicho invasivos como control biológico ha sido bien recibido.{w=0.5} Estoy impresionado."

show oak:
    xpos 300

show leaf:
    xpos 800

show may:
    xpos 1200

red @happy "¡Sam!"

oak @talkingmouth "Hola, muchacho. Me alegra ver que te has acomodado bien aquí."

red @pity "Sam, ¿qué está pasando? ¿Por qué estoy aquí? ¿Por qué estás enseñando? ¿Por qué no me dijiste que trabajarías en Kobukan? ¿Cómo--"

oak @angrybrow talkingmouth "[first_name]. Hay un tiempo y lugar para todo, pero ahora no es el momento."

redmind @thinking "Ugh... He escuchado eso antes."

oak @closedeyes talkingmouth "Además... frente a otros estudiantes, por favor, dime Profesor Oak."

red @surprised "¡Oh! Uh, sí, claro. Lo siento, Sam-- ¡Digo, Oak! Profesor Oak."

show leaf -surprisedbrow -frownmouth 
show may -surprisedbrow -frownmouth
with dis

oak @happy "De todos modos, Señorita Birch, sobre el tema de su padre..."

may @sadbrow talkingmouth "¡Oh! Sí, supongo que el trabajo de mi papá en el campo ha dado sus frutos."
may @happy "En los últimos años, si un enjambre de Ninjask no lo persigue, entonces sera uno de Beautifly o el ocasional Surskit."

oak @talkingmouth "Ah, ¿estás bien versada en tipos de bichos, May? Supongo que habrás adquirido mucha experiencia mientras ayudabas con el trabajo de tu padre."

may @happy "¡Sí! Al principio no me gustaban, pero planeo tomar la electividad de Tipo Bicho.{w=0.5} También me gustaría ir a Teselia algún día. ¡Escuché que tienen Pokémon tipo Bicho realmente poderosos!"

oak @closedbrow talkingmouth "Ya veo.{w=0.5} Entonces, ¿en qué tipos de Pokémon se centrarán en estudiar los tres este año?"

may @talkingmouth "Bueno, además del tipo Bicho, también planeo tomar las clases de Fuego y Lucha."

leaf @talkingmouth "Planta, Eléctrico y Dragón por aquí."

oak @happy "¡Opciones sólidas! Variadas y versátiles. ¿Y tú, muchacho? ¿Quizás tomarás Normal, como lo hice yo cuando era un entrenador?"

red @happy "Yo, eh, en realidad no planeo especializarme en un solo tipo. Solo tomaré clases que ayuden a los Pokémon que pueda atrapar."

oak angrybrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

redmind @sad "Oh, mierda, ¿dije algo malo?"

oak -angrybrow -frownmouth @happyeyes talkingmouth "Por supuesto que lo harás. Por {i}supuesto{/i} que lo harás."
oak @happy "Muchacho, nunca dejas de impresionarme. Eres un campeón, si es que alguna vez he visto uno."

red @surprised "Eh..."
red @happy "Gracias, Profesor Oak. ¿Eso significa que es la decisión correcta?"

oak @closedeyes sadeyebrows happymouth "No podría decirte eso, [first_name]. Pero es la decisión que tomaste."

red @closedbrow talkingmouth "Uh... sí, supongo."

oak @closedbrow talkingmouth "Aun así, te recomendaría que, por ahora al menos, [bluecolor]te enfoques en al menos un tipo. Podría ser difícil entrenar a tus Pokémon si te dispersas demasiado.{/color}"
oak @talkingmouth "¡Muy bien! Todas son excelentes elecciones.{w=0.5} Ahora, espero que todos estén listos. La campana sonará pronto, así que vayan y tomen asiento."

hide oak with dis

window hide

pause 1.0

show may surprisedbrow frownmouth with dis

show homeroom with vpunch

leaf @angry "Okay, ¿qué {i}demonios{/i}, 'muchacho'? ¡¿Ya estas en confianza con nuestro profesor?!"

show may -surprisedbrow -frownmouth with dis

red @closedbrow talking2mouth "Uh, sí. Era mi vecino."

leaf @closedbrow talking2mouth "Todavía {i}no{/i} hemos terminado de hablar de esto, pero por ahora.{w=0.5}.{w=0.5}.{w=0.5}" 
leaf @happy "Vamos a sentarnos juntas, May."
leaf happy @flirtbrow talkingmouth blush "Lo siento, [first_name], pero como estarás saltando de electividad en electividad como un Spoink, ¡apuesto a que tendremos muchas oportunidades para conocernos mejor más tarde!~"

hide leaf with dis

$ renpy.pause(1.25, hard=True)

show may:
    xpos 1200
    ease 0.65 xpos 880

$ renpy.pause(0.65, hard=True)

may @angrybrow talkingmouth "Entooonces... ¿qué piensas de Leaf, [first_name]?"
    
hide leaf

red @pity "Es absolutamente encantadora."
may @happybrow talkingmouth "Jeje, ¡es muy divertido estar con ella!"
may @happy "¡Ven a sentarte con nosotras!"

hide may

$ renpy.pause(1.0, hard=True)

red @happy "Esta bien, ni de broma me sentaré junto a [blue_name]."

$ renpy.music.set_volume(0.1, delay=1.0, channel="music")
$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_6
show blank2 with splitfade
$ renpy.pause(0.5, hard=True)
$ PlaySound("BellChime.ogg")
show morning at vspaz  
pause 3.5
hide blank2 with splitfade
$ renpy.music.set_volume(1.0, delay=1.00, channel="music")
$ renpy.transition(dissolve)
show screen currentdate
$ renpy.pause(1.0, hard=True)
hide morning

show oak with dis

oak @talkingmouth "¡Buenos días y bienvenidos a su primera clase en la Academia Kobukan!"
oak @talkingmouth "Seré su maestro en esta clase. Pueden llamarme Oak, pero la mayoría de la gente simplemente me llama el Profesor Pokémon."
oak @talkingmouth "Este mundo está habitado por criaturas que llamamos Pokémon.{w=0.5} Humanos y Pokémon viven juntos apoyándose mutuamente..."

window hide
pause 1.5

oak @closedbrow sweat talking2mouth "... Creo que puedo saltarme esta parte. El examen de ingreso que la mayoría de ustedes tomó debería haber filtrado al menos a aquellos que no saben qué es un Pokémon."

Character("Estudiante emocionado") "\"¡No puedo creer que estemos escuchando al Profesor Oak hablar justo frente a nosotros! ¡El hombre es una leyenda!\""
Character("Estudiante chismoso") "\"¡Lo sé! Mi papá es un gran fan suyo, tiene todas sus enciclopedias de la A a la Z. ¡No se lo va a creer cuando le diga que estoy en su clase!\""

redmind "Incluso fuera de Kanto, todo el mundo lo conoce."
redmind thinking "No sabía que tanta gente lo admiraba.{w=0.5} Para ellos debe ser como un superhéroe."
redmind happy "Pero para mí, solo es mi vecino."

oak @angrybrow talking2mouth "Ahora, algo que deben saber sobre esta clase es que es extremadamente importante para su calificación final."
oak @closedbrow talking2mouth sweat "El año pasado, todos los que no lograron aprobar esta clase tampoco lograron graduarse."

Character("Estudiante impactado") "\"¡Mierda!\""
Character("Estudiante chismoso") "\"De repente ya no quiero estar en esta clase...\""

redmind @closedbrow frownmouth "Ugh... si hay una clase en la que no puedo meter la pata, es ésta."

oak @talking2mouth "Sí, esta clase es todo un reto, pero si trabajan duro y se esfuerzan en sus estudios, deberían pasar con éxito."
oak @talkingmouth "Mi trabajo no es darles calificaciones reprobatorias.{w=0.5} Pero tampoco es consentirlos."
oak @happy "Mi trabajo es asegurarme de que se gradúen en esta academia con el conocimiento y las habilidades para sobresalir en el mundo Pokémon."
oak @talking2mouth "Lo que me lleva al siguiente punto."
oak @talkingmouth "Como todos saben, Kobukan es una academia muy selectiva, y exige que den lo mejor de sí mismos en todo momento, o serán superados por sus compañeros."
oak @angrybrow talking2mouth "{color=#0048ff}La tasa de graduación de esta academia está fijada en un ochenta por ciento.{/color}{w=0.5} ¡No es para los débiles de voluntad ni para los desmotivados!"

Character("Estudiante desconcertado") "\"¡Tiene que estar bromeando!\""
Character("Estudiante cínico") "\"¡¿Esto es una broma?!{w=0.5} ¡¿Qué tipo de vida escolar es esta?!\""

redmind -frownmouth @sadeyes sadeyebrows "Parece que algunas personas no leyeron la página web... pero yo tampoco tomé un folleto, así que supongo que todos tenemos nuestros puntos ciegos."

show may surprisedbrow frownmouth uniform with dis:
    xpos 0.25 ypos 1.3 zoom 1.35

show leaf surprisedbrow frownmouth uniform with dis:
    xpos 0.75 ypos 1.3 zoom 1.35

pause 1.0

redmind @sadbrow frownmouth "Supongo que Ethan no era la única persona que conocía que no sabía esto."

hide leaf
hide may
show blue smilemouth uniform:
    xpos 0.75 xzoom -1
with dis

pause 1.0

redmind @angrybrow frownmouth "Por supuesto, [blue_name] no se inmuta en lo absoluto."

hide leaf
hide may
hide blue 
with dis

show hilbert uniform with dis:
    xpos 1200

pause 1.0
    
redmind @surprisedbrow frownmouth "Y no me di cuenta al principio, pero Hilbert también está en esta clase.{w=0.5} Parece que ya lo sabía de antemano, no está para nada sorprendido."

hide hilbert with dis

oak @closedbrow sweat talking2mouth "Ajem... Sí, solo quería aclarar eso."
oak @talkingmouth "Ahora, ¿alguno de ustedes está interesado en competir en la Liga Pokémon después de graduarse? Levanten la mano si lo están."

redmind @sad2eyes frownmouth "Parece solo son unas pocas docenas de manos... Blue, Leaf..."
redmind @surprisedbrow frownmouth "¡Ah! ¡Yo también debería levantar la mano!" 

oak @angrybrow talking2mouth "Miren bien a su alrededor."

window hide
pause 1.5

oak @closedbrow talkingmouth "Ahora, todos en las dos secciones del medio, bajen la mano."

redmind @thinking "Quedan menos de diez estudiantes con la mano levantada.{w=0.5} Creo que sé hacia dónde va esto."

oak @talkingmouth "Ese es el porcentaje de los que realmente {i}calificarán{/i} para la Liga Pokémon. Y es incluso menor el número de los que {i}llegarán{/i} allí."
oak confusedbrow frownmouth @happy "Ahora, no dejen que esto los desanime. Comencemos con--"

window hide
pause 1.0

redmind @thonk "¿Mhm? ¿Qué está mirando?"

oak -confusedbrow @confusedbrow talking2mouth "Sí, ¿tienes alguna pregunta?"

show blue closedbrow happymouth uniform:
    xpos 0.75 xzoom -1

blue @happy "¡Ja! ¡Voy a decir esto ahora mismo para todos los que rendirse en esta sala!"
blue angrybrow talkingmouth @talkingmouth "¡Voy a llegar a la Liga Pokémon y no hay ninguna maldita posibilidad de que no lo haga!"

redmind @thinking "Oh por Dios, ¿por qué siempre tiene que ser así?{w=0.5} No han pasado ni diez minutos desde que empezó la clase y ya está tratando de hacer una escena."
redmind @thinking "Se esfuerza tanto por parecer genial y fracasa tanto que ya parece ser enfermizo."

blue @talkingmouth "¡No voy a parar hasta trapear el suelo con todos los campeones regionales de la Liga Pokémon! ¡Están en presencia del próximo Campeón Mundial!"

oak @closedbrow talkingmouth "Por favor, siéntate--"
oak sadbrow @confused "Ehm, ¿cómo era tu nombre?"

blue wistfulbrow scaredmouth "¿Qué...? ¡Abuelo, soy yo!"

oak @closedbrow talking2mouth "Sí, sé que eres tú. Pero ¿cómo era tu--"

show blue angry with dis

red @happy "¡Es [blue_name]!"

leaf uniform @happy "Oh Dios mío, ¡¿realmente acabas de decir eso?! ¡Sí que tienes pelotas, [first_name]!"

oak -sadbrow -frownmouth @closedbrow talking2mouth "¡Ah, sí! ¡Es verdad! De todos modos, ¡siéntate!"

blue @angry "Que monton de...{w=0.5} no puedo creer que esto este pasando..."

pause 1.0

may uniform @sad "[blue_name] te está fulminando con la mirada..."
red @happy "Sí, bueno, cuando se pone así, lo mejor es sonreír y darle un pulgar arriba."

show blue angrybrow talkingmouth with dis

redmind @playfulbrow smirkmouth "Eso sólo lo hizo enojar más.{w=0.4} Estoy empezando a disfrutar cada vez más esta clase."

hide blue with dis

oak @talkingmouth "Muy bien. Creo que eso es suficiente charla.{w=0.5} Empecemos a repasar el programa, por ahora."
oak @closedbrow talking2mouth "Antes de hacerme cualquier pregunta sobre cómo serán mis clases o sobre lo que implicarán, les pido que primero revisen el programa. ¡Es una herramienta muy útil!"
oak @talkingmouth "Por el momento, lo más importante a recordar es--"

show oak surprisedbrow frownmouth with dis

show homeroom with vpunch

$ showredonly = True

whitney uniform @surprised "{cps=20}{size=26}¡¡E{/size}{size=28}E{/size}{size=30}E{/size}{size=32}E{/size}{size=34}S{/size}{size=36}SS{/size}{size=38}PE{/size}{size=40}EE{/size}{size=42}R{/size}{size=44}E{/size}{size=46}E{/size}{size=48}E{/size}{size=50}N{/size}{size=52}N!!{/size}{/cps}"

window hide
$ PlaySound("ExitBuilding.ogg")

show whitney surprisedbrow sadmouth uniform:
    xpos 2000 ypos 1.1 alpha 0.0 rotate 10
    ease 0.4 xpos 500 alpha 1.0
    ease 0.5 xpos 300
    pause 0.5
    ease 0.5 xpos 500 ypos 1.2 rotate 0
    
$ renpy.pause(2.0, hard=True)

show whitney happy with dis

$ showredonly = False

redmind @thinking "Y ahora posa como si acabara de hacer una acrobacia en el Pokéathlon."

whitney @talking2mouth "¡Aquí estoy!{W=0.5} ¡No llego tarde, sólo estaba esperando el momento perfecto para hacer mi gran entrada!"

show whitney:
    xpos 500 zoom 1.0
    ease 0.4 xpos 340 ypos 1.2 zoom 1.3
    pause 0.3
    ease 0.15 ypos 1.3

narrator "La extraña pelirroja se sienta en la silla vacía frente a ti, como si no hubiera ocurrido nada."

show whitney -happy with dis:
    xpos 340 ypos 1.3 zoom 1.3

pause 1.5
    
whitney @talking2mouth "Por favor, continúe."

oak -surprisedbrow -frownmouth @closedbrow talking2mouth "Muy bien, te sugiero que intentes llegar a clase un poco antes en el futuro. Esto es una universidad... no el instituto."
oak @talking2mouth "No habrá hojas de asistencia, no se pasará lista y nadie te hará responsable de tu asistencia a clase."
oak @angrybrow talking2mouth "Nadie excepto tú misma. Así que, {i}sé{/i} responsable contigo misma."
oak @talkingmouth sad2eyes "Fuera de eso, si {i}debes{/i} llegar tarde, intenta hacerlo {i}sin{/i} una 'gran entrada', por favor."

whitney @happy sweat "Ja, ja... ¡sí, por supuesto!"

pause 1.0

whitney @surprised "¡Oh!"
whitney @sadeyebrows talking2mouth "Uhm... mi compañera de dormitorio tampoco está aquí todavía."

oak @closedbrow talking2mouth "Entonces, confío en que le transmitirás lo esencial de mi discurso anterior."

$ showredonly = True

flannery tired uniform "{cps=22}¿De qué.{w=0.25}.{w=0.25}.{w=0.5} estamos hablando...?{/cps}"

show flannery -tired tiredbrow frownmouth uniform behind whitney with dis:
    xpos 0 ypos 1.9 zoom 1.2
    ease 0.75 xpos 0.2 ypos 1.3 zoom 1.1
    ease 1.25 xpos 0.35 ypos 1.1 zoom 1.0
        
$ renpy.pause(2.0, hard=True)

$ showredonly = False

whitney @sweat happy "¡De ti Flan! Y como estamos {i}totalmente{/i} apenadas de haber llegado tarde, ¿verdad?"

flannery @closedbrow frazzled talking2mouth "Sí, lo siento... No soy un gran fan de las mañanas..."

oak @talking2mouth "Fan o no, intenta llegar a clase a tiempo a partir de ahora."

flannery @talking2mouth "Sí... está bien."

show flannery tired:
    xpos 0.35 ypos 1.1 zoom 1.0
    ease 1.5 xpos 0.75 ypos 1.1 zoom 1.35 xzoom -1
    pause 0.5
    ease 0.4 ypos 1.2
    
$ renpy.pause(2.5, hard=True)

redmind @thonk "Ella es... un poco intimidante. Me recuerda a una de esas chicas motociclistas que andan al oeste de Ciudad Azulona."

pause 1.0

hide flannery 
hide whitney
with dis

redmind @thinking "De todos modos, ahora que está sentada a mi lado, tengo a May a mi izquierda, esta nueva pelirroja a mi derecha, la chica de pelo rosa delante de mí, y detrás de mí está..."

hide oak 
show dawn uniform 
with dis

pause 1.0

redmind @thonk "Otra chica linda."
redmind @thinking "¿Es algún tipo de experimento social? ¿Invitar a un estudiante ridículamente poco cualificado a Kobukan, pero rodearlo de mujeres atractivas, para que no pueda concentrarse en absoluto?"

hide dawn
show oakbg
with dis

redmind @happy "Bueno, menos mal que quien haya organizado esto no sabía que también me ponen los hombres."

pause 1.0

show flannery tired uniform with dis:
    xpos 1200 xzoom -1 ypos 1.2 zoom 1.25

pause 1.0

narrator "Al cabo de un momento, te das cuenta de que la pelirroja de pelo de punta te está mirando."

redmind @thonk "¿Mhm? ¿Espera que le diga algo? ¿O solo tiene la mirada perdida por el cansancio?"

menu:
    "Mañana difícil, ¿eh?":        
        flannery angrybrow frownmouth eyebags frazzled @angrybrow talking2mouth "¿Y a ti qué te importa?"

        red @surprisedbrow talking2mouth "Uh, solo pensé que, bueno, parecías algo cansada."
        red @closedbrow talking2mouth "{size=30}Pero ya no.{/size}"

        show flannery angry frazzled with dis:
            xpos 1200 ypos 1.2
            ease 0.5 xpos 1140
            
        flannery "¿Qué tal si te metes en tus asuntos?{w=0.5} No recuerdo haberte pedido tu opinión sobre nada."

    "¿Quieres café?":
        red @talkingmouth "Tomé uno extra esta mañana."

        flannery angrybrow frownmouth eyebags frazzled @angrybrow talking2mouth "¿Me estás hablando a {i}mí{/i}?"
        
        red @confusedbrow talking2mouth "... ¿Dije algo malo?"
        
        flannery angry frazzled "¿Te parece que soy un caso de caridad?"
        
        $ ValueChange("Flannery", -1, 0.66)

        red @wince talking2mouth "¡No! Solo te ves muy cansada y pensé que--"
        
        flannery furiousbrow angrymouth frazzled "¿Pensaste qué?{w=0.5} ¿Que aceptaría tus limosnas?"
        
        show flannery frazzled with dis:
            xpos 1200 ypos 1.2
            ease 0.5 xpos 1140
            
        flannery furious frazzled veins "¿Por qué no agarras ese café y te lo metes por el--"

    ">Quedarse callado":        
        redmind "OPensándolo bien, mejor no. Con esa mirada... a veces la discreción es la mejor opción."
        
        redmind @thonk "Cambiando de tema... ¿su cabello no rompe alguna norma de la escuela?{w=0.5} Debe medir al menos un metro de ancho."
        
        show flannery eyebags angrybrow frazzled frownmouth with dis
        
        redmind @closedeyes confusedeyebrows sweat frownmouth "Cómo diablos logra que se mantenga así?{w=0.5} No puedo imaginar la cantidad de fijador que debe de usar."
        
        flannery @angrymouth "¿Tienes algún problema, amigo?"
        
        red @confused "¿Eh?"
        
        flannery @furiousbrow angrymouth "¿Por qué demonios me miras así?"
        
        red @surprisedeyes surprisedeyebrows talking2mouth "Uh, por nada en especial. Solo me preguntaba cómo haces para que tu cabello se vea.{w=0.25}.{w=0.25}.{w=0.5} así."
        
        flannery frazzled furiousbrow angrymouth "{i}¿Así cómo?{/i}"
        
        red @wince "Ya sabes...{w=0.5} así..."

        show flannery frazzled with dis:
            xpos 1200 ypos 1.2
            ease 0.5 xpos 1140
            
        flannery furious frazzled veins "¡¿Te estás burlando de mi cabello?! ¡Te voy a partir la cara!"

hide whitney

show whitney uniform with dis:
    xpos 685 ypos 1.2 zoom 1.25
    ease 0.5

whitney @happy "¡Relájate, Flan!{w=0.5} Estoy segura de que no lo dijo con mala intención."

show flannery tiredbrow frownmouth -veins with dis

red @closedeyes talking2mouth  "¡Sí, gracias!"

whitney @talking2mouth "Es el primer día."
whitney @sadbrow talking2mouth "Deberías bajarle tres rayitas, chica."

show flannery:
    xpos 1140 ypos 1.2
    ease 0.6 xpos 1200
    
flannery angrybrow @talking2mouth "Psh."

hide flannery with dis

pause 1.0

$ BecomeNamed("Flannery")

whitney @talking2mouth "Vas a tener que tenerle paciencia a Flannery.{w=0.5} En las mañanas es un poco difícil de tratar."

red uniform @sadbrow talkingmouth "Lo entiendo, la mañana tampoco es mi momento favorito del día."

whitney @angrybrow happymouth "Jeje, llegamos tarde porque Flan se quedó dormida y no escuchó ninguna de sus alarmas."

show flannery uniform tiredbrow tiredmouth with dis:
    xpos 1200 ypos 1.2 xzoom -1 zoom 1.25

$ BecomeNamed("Whitney")

flannery @talking2mouth "No funcionan, Whitney. No sé cuántas veces tengo que decírtelo."

pause 1.5

show flannery surprisedbrow frownmouth with dis

whitney @happy "Creo que es porque roncas más fuerte que los despertadores."

flannery @furious veins "¡Yo NO ronco!"
flannery tiredbrow tiredmouth @angrybrow -veins furiousmouth "¡Oye! ¿De qué te ríes?{w=0.5} No ronco, ¡¿me oíste?!"

red @pity "Te creo.{w=0.5} Así que tú eres Whitney, y tú eres Flannery."
red @happy "Yo soy [first_name]."

whitney @happy "¡Encantada de conocerte, [first_name]!"

if persondex["Flannery"]["Value"] != -1:
    flannery sad2eyes talking2mouth "Sí... Lo siento por haberte molestado antes."

    red @wince talking2mouth "No te preocupes por eso."

show flannery surprisedbrow frownmouth
show whitney surprisedbrow frownmouth 
with dis


oak @talkingmouth "¡Bajen la voz allá atrás!"

hide flannery
hide whitney 
with dis

stop music fadeout 1.5

redmind @closedbrow sweat frownmouth "Muy bien, ahora tengo que concentrarme realmente..."

$ renpy.music.queue("Audio/Music/ViridianCity_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/ViridianCity_Loop.ogg", channel='music', loop=True, tight=None)

$ renpy.pause(0.75, hard=True)

$ renpy.music.set_volume(0.1, delay=1.0, channel="music")

show blank2 with dis

$ PlaySound("BellChime.ogg")
$ renpy.music.play("Audio/hall_crowd.ogg", channel='crowd', loop=True, fadein=1.75)
$ renpy.music.set_volume(1.0, delay=4.0, channel="music")

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_7

pause 2.0

narrator "El resto de la clase transcurre sin incidentes."
narrator "Ahora es momento de elegir la electividad a la que asistirás."

window hide
scene blank2
$ renpy.music.stop(channel='crowd', fadeout=1.0)

narrator "[bluecolor]Es importante recordar dos cosas: asistir a una electividad aumentará tu competencia, y tu competencia en un tipo determinará el nivel máximo al que tus Pokémon podrán subir.{/color}"

narrator "[bluecolor]Los Pokémon que ya superen ese límite no perderán niveles, pero tampoco podrán seguir subiendo.{/color}"

narrator "[bluecolor]Por esta razón, es recomendable enfocarse en al menos un tipo por un tiempo. Sin embargo, pasará un tiempo antes de que tus Pokémon comiencen a ganar experiencia en combate.{/color}"

jump PickElective