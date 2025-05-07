label lunch010405:

$ timeOfDay = "Afternoon"

$ renpy.transition(dissolve)
show screen currentdate

queue music "Audio/Music/Road to Viridian City.ogg"
    
hide blank2 with splitfade

$ renpy.pause(0.5, hard=True)

show bianca uniform with dis

bianca @happy "¡Hey, chico guapo con la gorra roja!"

red uniform @talkingmouth "Ese es mi nombre..."

bianca @talkingmouth "¡Cheren quiere verte!"

red @confused "¿Ahora? Pensé que iba a esperar hasta después de clases."

bianca @happy "¡Yo también! ¡Y él también! Y, de alguna manera, ¡todos estábamos equivocados! ¿No es súper rarooooooo?"

red @happy "Tú lo has dicho."
red @talkingmouth "Bueno, llevame a donde esta."

show blank2 with splitfade

hide bianca

narrator "Encuentras el camino hasta la mesa de Cheren, sorprendiéndote al ver algunas caras conocidas allí."
narrator "También te sorprende ver que esta mesa, claramente diseñada para cuatro personas, tiene seis personas apretadas en ella, sin contar contigo."
narrator "Te acomodas torpemente y charlas un poco hasta que Cheren se aclara la garganta, llamando la atención de todos."

cheren uniform @talkingmouth "Damas y caballeros, sin duda se estarán preguntando por qué los he reunido aquí hoy."

hide blank2 with splitfade

show cafeB_CG:
    subpixel True
    alpha 0.0 xalign 0.5 yalign 1.0 zoom 1.25
    parallel:
        ease 1.5 alpha 1.0
    parallel:
        ease 5.0 zoom 1.0

redmind "No está haciendo mucho para despejar la idea de que actúa como el 'jefe de una mafia'..."

serena uniform @talkingmouth "¿Puedo asumir que de alguna manera ya has oído sobre mis intenciones respecto al Consejo Estudiantil?"

cheren @talking2mouth "Sí, eso definitivamente esta relacionado con esto."

hide calem
hide hilda

cheren @talking2mouth "Hasta donde entiendo, tú, Calem, ¿aún estás decidiendo si postularte o no?"

calem uniform @talkingmouth "En pocas palabras, sí."

hilda uniform @smirkmouth "Entonces, ¿para qué estamos aquí {i}nosotros{/i}, Hilbert y yo?"

$ BecomeNamed("Hilda")
cheren @happy "Excelente pregunta, Hilda."
cheren @talkingmouth "Ustedes están aquí como representantes del alumnado."
cheren @closedbrow talking2mouth "No serviría de nada decidir el futuro del alumnado sin contar con la opinión nuestros electores."

hilbert uniform @sadbrow talkingmouth "Paso."

hilda @angry "¡Hilbert!"

cheren @surprised "... Lo siento, pero, ¿por qué?"

hilbert @talkingmouth "No represento a nadie más que a mí mismo. Además, cualquiera que se apunte para el Consejo Estudiantil solo se está preparando para el fracaso. Esta escuela tiene muchos más problemas de los que un par de consejeros podrían solucionar."

cheren @angrybrow "{w=0.5}.{w=0.5}.{w=0.5}."
cheren @sad "Entiendo por qué puedes sentirte así. Sin duda, otros también lo harán. Aun así, agradecería tu opinión, aunque no tengas mucho entusiasmo."
cheren @happy "El 'votante hastiado, apático y desencantado' sigue siendo un sector demográfico al que quiero llegar."

hilbert @sadbrow talkingmouth ".{w=0.25}.{w=0.25}.{w=0.25}Pfft. {w=0.5}{nw}" 
extend @talkingmouth "Como séa."

pause 1.0

red uniform @confused "Eh... ¿y yo por qué estoy aquí?"

cheren @happy "Bueno, [first_name], cuando hablamos el viernes, tú... me {i}motivaste{/i}." 
cheren @talkingmouth "Creí detectar en ti algo que podría ser muy poderoso si se utiliza adecuadamente, una especie de... carisma inofensivo."

red @confused "¿Inofensivo? Gracias."

cheren @happy "¡Es una habilidad valiosa!"
cheren @closedbrow talking2mouth "Y aprecio tu buena voluntad para adelantar nuestra reunión programada. Resulta que tenía otra cita programada después de clases."
cheren @talkingmouth "En cualquier caso, [first_name], te invité aquí porque quería saber si considerarías postularte para el Consejo Estudiantil."

if (council_campaigning):
    red @happy "De hecho, ya lo estoy haciendo. Lo decidí esta mañana, pero sí, quiero postularme."

else:
    menu:
        "Sí, creo que lo haré.":
            $ council_campaigning = True

        "No, estaré demasiado ocupado.":
            pass

if (council_campaigning):
    cheren @happy "Espléndido."
    cheren @talking2mouth "Aunque eso significa que hay una pregunta un poco incómoda la cual deberemos abordar."
    cheren @talking2mouth "[first_name], Serena... y posiblemente Calem..."

else:
    cheren @sad "Es una lástima."
    cheren @talking2mouth "Aunque eso te salva de la incomodidad de la siguiente pregunta."
    cheren @talking2mouth "Serena... y posiblemente Calem..."

cheren @sad "Me gustaría trabajar con ustedes para ser elegidos, pero aún no conozco sus propuestas. Podría ser que terminemos siendo rivales políticos."
cheren @talking2mouth "¿Podrían compartir alguna de las propuestas con las que planean postularse?"

serena @talkingmouth "Por supuesto. Hay una cosa, más que cualquier otra, que quiero."
serena @blush heartbrow talkingmouth "Dormitorios mixtos."

calem @surprised "¿Eh?"

serena @happy "Al fin y al cabo, todos somos adultos, ¿no? Como no tenemos la libertad de vivir en apartamentos cercanos, deberíamos tener la libertad de vivir como queramos en el campus."

cheren @happy "Bien dicho. Estoy seguro de que esta será una propuesta popular, independientemente de lo que yo piense personalmente."

if (council_campaigning):
    cheren @talkingmouth "¿Qué hay de ti, [first_name]?"

    red @talking2mouth "No estoy seguro todavía. Pero nada de lo que han dicho hasta ahora me ha asustado, así que..."

    cheren @closedbrow talkingmouth "... Así que deberíamos estar en la misma página."

hilda @talkingmouth "Parece que lo que ustedes quieren hacer los va a poner en la lista negra de la administración. Especialmente a ti, Cheren."

hilbert @closedbrow talkingmouth "Sí. Incluso si hacen una gran campaña, si están proponiendo algo que a la escuela no le gusta, simplemente se los negara y no podrán hacer nada al respecto."

hide bianca

cheren @closedbrow talkingmouth "Eso siempre es una preocupación, pero el Consejo Estudiantil de la Academia Kobukan tiene mucho poder y un presupuesto aún mayor."
cheren @talkingmouth "Mientras podamos {i}entrar{/i} al consejo, creo que puedo defendernos de la administración."

bianca uniform @happy "¡Creo en ustedes, chicos!"

pause 1.0
    
bianca @happy sweat "Entonces, um, ¿han visto ya el jardín de atrás?{w=0.5} ¡Es tan bonito~!"

redmind @closedbrow talkingmouth "Gracias a Dios por Bianca.{w=0.5} Supongo que es del tipo en el que puedo contar para cambiar el tema a algo más ligero."

serena @talkingmouth "Lo he visto desde afuera, pero nunca he entrado."
serena @happy "¡Deberíamos ir algún día!"

hilda @happy "¡Claro que sí!{w=0.5} Sería un puto desperdicio si no lo hiciéramos."

hilbert @surprised "¿Por qué?{w=0.5} ¿Qué se supone que {i}haces{/i} en un jardín?"

serena @talkingmouth "Pensaba en quizás hacer un picnic.{w=0.5} Escuché que el centro del jardín es un lugar muy popular entre los estudiantes en primavera y verano."

hilbert @talkingmouth "¿Por qué no simplemente comer en la cafetería?{w=0.5} Es más barato, más rápido y no tenemos que preocuparnos de que el viento se lleve todo."

hilda @closedbrow talking2mouth veins "No es lo mismo, Hilbert..."

hilbert @sadbrow talkingmouth "Tienes razón, no lo es."
hilbert @angry "Comer en una mesa es mucho mejor que comer en la tierra y el pasto."

hilda @angrybrow smirkmouth "De verdad crees que comer en un cuarto aburrido, rodeado de gente, es mejor que comer con tus amigos en un jardín tranquilo?"

hilbert @frownmouth "[ellipses]"
hilbert @talkingmouth "Sí."

calem @talkingmouth "Tengo que coincidir con Hilbert."

serena @talkingmouth "¿Calem?{w=0.5} Pensé que tú, de todas las personas, preferirías un lugar con menos gente."

calem @talkingmouth "No te equivocas, pero no me gusta la idea de comer comida tan cerca del suelo.{w=0.5} ¿Quién sabe qué ha estado en el suelo del jardín"

serena @talkingmouth "Bueno, esa es solo tu opinión.{w=0.5} ¿Qué piensa el resto?"

cheren @talking2mouth "Ambos lados tienen sus méritos. No veo razón para tomar una postura absoluta en este asunto."

bianca @happy "¡Depende del día! Dicen que la variedad es el condimento de la vida, ¿saben?"

serena @happy "Parece que la balanza sigue estando equilibrada..."
serena @talkingmouth "¿Tú que opinas, [first_name]?"

redmind @thinking "Uh... ¿de verdad esperan que yo decida esto? No es exactamente una causa en la que me gustaría arriesgarme."

menu:
    "Comer dentro es lo mejor.":
        $ ValueChange("Calem", 1, (448/1920, 641/1080), False)
        $ ValueChange("Hilbert", 1, (1579/1920, 281/1080))
        
        hilbert @closedbrow talkingmouth "Exacto."
        hilbert @talkingmouth "¿Y si olvidas algo en tu habitación?{w=0.5} Entonces tendrías que caminar de regreso a buscarlo.{w=0.5} Sería mucho esfuerzo para nada."
        
        hilda @sad "Está bien, Hilbert, lo entendimos.{w=0.5} No hace falta insistir tanto."
        
        serena @poutmouth "Bueno, {i}yo{/i} sigo pensando que un picnic es una buena idea."
        
        calem @closedbrow talking2mouth "Y yo sigo pensando que es mejor no comer en el suelo.{w=0.5} Cada quien con su opinión."
        
        serena @angrybrow talkingmouth "Sí, lo sé.{w=0.5} Solo era una idea."
    
    "Un picnic suena genial.":
        $ ValueChange("Serena", 1, (112/1920, 426/1080), False)
        $ ValueChange("Hilda", 1, (1455/1920, 650/1080))

        serena @happy "¡Sí! Comer algo ligero rodeado de la naturaleza y bajo el cielo azul suena...{w=0.5} tan romántico."

        calem @sadmouth "Uno puede sobreexponerse demasiado al romance."
        
        hilda @smirkmouth "Da igual.{w=0.5} Se trata de, ya sabes, el ambiente, no de la comida en sí."
        hilda @closedbrow talkingmouth "Los cerezos están floreciendo en esta época del año, ¿no? En Teselia no tenemos eso."
        
        hilbert @angrybrow talkingmouth "Entonces puedes salir y comer entre árboles si tantas ganas tienes."
        hilbert @closedbrow talkingmouth "Los que no quieren un puñado de tierra en su sándwich pueden quedarse aquí."

        hilda @sadbrow talking2mouth "¡Solo era una sugerencia!"
        
        calem @closedbrow talkingmouth "Sigo prefiriendo comer en una superficie estable, pero cada quien con sus preferencias."
    
    "Realmente no importa dónde comas.":
        red @talkingmouth "Lo importante es la comida, no el lugar."
        red @happy "Me podrías poner a comer en el baño y me daría igual, mientras tenga comida."
        
        $ ValueChange("Cheren", 1, (914/1920, 197/1080), False)
        $ ValueChange("Bianca", 1, (1326/1920, 285/1080))
        
        cheren @closedbrow talkingmouth "Fue una forma bastante cruda de decirlo, pero estoy de acuerdo."
        
        bianca @happy "¡Sí! Mientras la comida termine en mi estomaguito, ¡estaré bien!"
        
        serena @sadbrow talkingmouth "Así que seguimos en un punto muerto."
        
        hilbert @angry "¿A quién le importa?{w=0.5} Pueden ir a comer donde se les dé la maldita gana. Ya terminé con esta conversación."
    
bianca @talkingmouth "Bueno, si quieren ir al jardín, está abierto para los estudiantes todo el día, ¡todos los días!"
bianca @happy "Yo planeaba ir para adelantarme en mis clases de tipo Psíquico y Normal."

cheren @confused "¿De qué manera planeabas adelantarte?"

bianca @talkingmouth "No sé, pero pensé que tal vez podría observar de cerca a cualquier Pokémon que encuentre ahí para tener algo con qué comparar en clase. ¿Suena raro?"

cheren @happy "No, es una buena idea.{w=0.5} Yo planeaba hacer algo similar."

bianca @happy "¡Jeje, gracias!"

cheren @closedbrow talkingmouth "Incluso yo caigo en la trampa que tantos otros caen de subestimarte, Bianca. Ya debería saber que eres una estudiante extremadamente diligente."
cheren @happy "En muchos sentidos, tu enfoque supera al mío."

bianca @happy "¡Aw, gracias! Sabía que tenía que tomarme esto en serio después de todo esa con mi papá, jaja."

cheren @sadbrow talkingmouth "Eh... sí. Fue una 'charla' muy ruidosa."

serena @talkingmouth "Hablando de clases, ¿cómo planean manejar sus estudios?{w=0.5} ¿Creen que deberíamos hacer algún tipo de grupo de estudio?"

calem @closedbrow talkingmouth "¿Te preocupa lo que dijeron los profesores sobre la tasa de graduación? Un ochenta por ciento fijo es... preocupante."

serena @sadbrow happymouth "Mmm... solo un poco."

cheren @closedbrow talkingmouth "No hay necesidad de preocuparse por algo como graduarse."
cheren @happy "Tengo confianza en que todos los que estamos en esta mesa no tendremos problemas para graduarnos a tiempo."
cheren @talkingmouth "De lo que deberían preocuparse es de cómo van a pasar su tiempo {i}fuera{/i} de clase.{w=0.5} ¿Ya han decidido en qué actividades extracurriculares se inscribirán?"

bianca @surprised "Oh, ¿te refieres a los clubes? {w=0.5}{nw}" 
extend talkingmouth "Estaba considerando el club de jardinería, pero quería pensarlo un poco más."
bianca @happy "¿Ya te has decidido por alguno, Cheren?"

cheren @talking2mouth "No lo veo necesario.{w=0.5} Estaré ocupado preparándome para las elecciones del Consejo Estudiantil, y aún más si gano."

bianca @surprised "¡Oh, cierto!{w=0.5} ¡Van a estar muy ocupados!"

calem @sad "Todavía estoy indeciso sobre el Consejo Estudiantil, pero, como plan de respaldo, planeo unirme al club de arte.{w=0.5} Sería una buena manera de pasar el tiempo y relajarme"

serena @talkingmouth "Mis padres me han dicho que los musicales de la Academia Kobukan son tan impresionantes que pueden compararse con los profesionales."
serena @happy "Si es posible, me gustaría unirme a la orquesta para tocar el violín."

calem @talkingmouth "Estoy {i}más que seguro{/i} de que si Brendan se enterara de tus habilidades con el violín, haría todo lo posible por meterte en el Club de Coordinadores."

serena @happy "¡Entonces tal vez lo deje intentarlo!"

hilda @sadbrow smirkmouth "Debe ser bonito poder tocar un instrumento musical."
hilda @happy "Lo único que yo sé jugar es tenis."

serena @surprised "¿Entonces te unirás al club de tenis?"

hilda @sadbrow smirkmouth "¿Esta escuela tiene club de tenis?"

pause 1.0

hilda @smirkmouth "Ni siquiera puedo imaginar unirme a un club. Voy a estar demasiado ocupada.{w=0.5} ¿Qué hay de ti, Hilbert?"

hilbert @closedbrow talkingmouth "No sé jugar tenis."

hilda @talkingmouth "No, me refiero a si hay algún club que te interese."

hilbert @talkingmouth "Hmm.{w=0.25}.{w=0.25}."
hilbert @talkingmouth "Me uniré al equipo de batalla."

calem @closedbrow talkingmouth "¿Tienes algún club en mente, [first_name]?"

if council_campaigning:
    calem @talkingmouth "Incluso si estás seguro de que serás elegido, es una buena idea tener un Plan B."

red @closedbrow talking2mouth "Clubes, ¿eh?{w=0.5} Ahora mismo estoy inclinándome hacia..."

menu:
    "El club de arte.":
        red @talkingmouth "Siempre he pensado que sería genial aprender a dibujar y pintar.{w=0.5} Nunca use un lápiz para otra cosa que no sea escribir palabras o números."
        
        $ ValueChange("Calem", 1, (448/1920, 641/1080))
        
        calem @happy "¿Buscando añadir nuevas habilidades a tu repertorio?{w=0.5} Esa es una buena actitud, [first_name]."
        calem @closedbrow talkingmouth "Si crees que te gustaría un curso intensivo de bellas artes, llámame.{w=0.5} Mis padres prácticamente me obligaron a tomar clases de arte cuando era niño."
        
        serena @happy "Calem es un pintor bastante talentoso.{w=0.5} Deberías ver algunas de sus obras, son absolutamente hermosas."
        
        calem @sadbrow talkingmouth "Me halagas excesivamente."
    
    "El club de jardinería.":
        red @talkingmouth "Parece un lugar donde realmente puedo relajarme y descansar un par de horas."
        
        $ ValueChange("Bianca", 1, (1326/1920, 285/1080))       
        
        bianca @happy "{i}¿¿¿Verdad???{/i} ¡Sería taaan relajante desconectar después de un largo día de clases!"
        
        hilda @happy "Sí, suena jodidamente relajante. Ojalá tuviera tiempo para pasarme por ahí."
        
        bianca @puppyeyes happymouth "¡Escuché que también cuidan a los Pokémon!{w=0.5} ¿Crees que nos dejen llevarnos alguno a casa?"
    
    "El club de teatro.":     
        red @talkingmouth "En Pueblo Paleta, {i}combatir{/i} con Pokémon se consideraba bastante elegante. Ni siquiera puedo imaginar cómo sería montar un musical con ellos."
        red @happy "Pero me encantaría averiguarlo."

        $ ValueChange("Serena", 1, (112/1920, 426/1080)) 
        
        serena @happy "¡Oh, qué espléndido! Estoy segura de que serías una gran incorporación a cualquier musical en el que toques un instrumento."
        serena @talkingmouth "¿A cuál departamento estás pensando unirte?"

        red @confused "¿Departamento?{w=0.5} ¿Te refieres a sanidad o algo por el estilo?"
        
        serena @sadbrow happymouth "... No. Me refiero a algo como el equipo de escena, los coreógrafos, la orquesta de foso... ¿No lo sabías?"

        red @closedbrow talking2mouth "Ni la más minima idea."

        pause 1.0

        serena @talkingmouth "No importa.{w=0.5} Lo importante es tu decisión de unirte al club."
    
    "El club de tenis.":
        red @talkingmouth "No era un gran jugador, solo sabía lo básico, pero era bastante rápido con los pies, así que eso ayudaba. ¿Quizás pueda entrar?"

        $ ValueChange("Hilda", 1, 1290/1920)

        hilda @happy "¿Bromeas? Al menos ve e intentalo, hombre. ¿Qué tipo de jugador eres?"
        
        red @talkingmouth "Eh, creo que bastante promedio.{w=0.5} Nada especial."
        
        hilda @smirkmouth "No, ¿me refiero a si eres un pasabolas,{w=0.3} un fondo defensivo,{w=0.3} un contragolpeador{w=0.3} o quizás un jugador de toda pista?"
        
        red @confused "{w=0.25}.{w=0.25}.{w=0.5}. No tengo la más mínima idea, yo solo golpeaba la pelota para que pase por encima de la red."
        
        hilda @happy "Eh, está bien. La única palabra elegante que necesitas saber para jugar es que el 'amor' no significa nada."

        serena @sad "[ellipses]"
        calem @sad "[ellipses]"

        redmind @thinking "Hmm..."

        hilda @smirkmouth "En fin, si quieres aprender algo de terminología o solo practicar un poco, búscame cuando esté libre." 
        hilda @sadbrow smirkmouth "Aunque, honestamente, eso probablemente sea más difícil que dominar el tenis."

    "El equipo de batalla.":
        red @talkingmouth "El equipo de batalla."
        red @talkingmouth "Voy a ser un Campeón algún día, y sé que muchos de los Campeones de Kobukan se unieron al equipo de batalla."

        $ ValueChange("Hilbert", -1, 1690/1920)
        
        hilbert @closedbrow talkingmouth "¿Tienes alguna experiencia en combates Pokémon a nivel competitivo?"
        
        red @talkingmouth "No me llamaría un maestro, pero sé algunos trucos. De niño, participé en peleas de práctica con otros y con los Pokémon que teníamos en el pueblo."

        hilbert @talkingmouth "¿Pero alguna vez has competido en batallas oficiales?{w=0.5} Difícilmente puedes llamarte Entrenador Pokémon hasta que hayas experimentado un combate oficial."
    
        red @closedbrow talking2mouth "Bueno... no."

        hilbert @sadbrow talkingmouth "Y aun así dices que serás un Campeón algún día... sin ninguna prueba, ninguna evidencia y sin ningún atisbo de {i}razón{/i}."

        red @angrybrow  talkingmouth "Sí, porque no hay {i}nada{/i} que no haré para convertirme en Campeón."

calem @surprised "Por supuesto, al elegir un club, es importante recordar el costo de oportunidad que conlleva."

hilbert @closedbrow talkingmouth "No es como si hubiera consecuencias por faltar."

bianca @happy "¡Pero si sientes ganas de probar otro club, seguro que te recibirán con los brazos abiertos!"

cheren @closedbrow talkingmouth "Bueno, excepto el equipo de batalla. Pero ellos son muy exigentes, y con razón."

hilda @smirkmouth "Gracias a Dios. Si estos clubes tuvieran asistencia obligatoria, no podría asistir a ninguno."

bianca @happy "Los clubes de Kobukan son geniales porque no les importa cuándo vas, ¡solo que cuando {i}lo hagas{/i}, la puedas pasar bien~!"

cheren @happy "No es sorprendente, dado lo rigurosa que es nuestra academia, las actividades extracurriculares ofrecen un descanso muy necesario."

bianca @surprisedbrow talking2mouth "Mmm, toda esta charla sobre clubes hace que me duela la cabeza."
bianca @happy "¡Hablemos de algo divertido, como lo increíble que es la comida aquí~!"
bianca @talkingmouth "¿Han probado algo así en casa?"

calem @happy "Soy de Kalos, por supuesto... Aunque la comida aquí es {i}bastante{/i} buena."

hilda @smirkmouth "Sí, claro, señor sofisticado. Para el resto de nosotros, esta mierda es increíble. Deben haber contratado algunos chefs estupidamente caros...{w=0.5} ¿Cuánto financiamiento recibe esta escuela, de todos modos?"

cheren @talkingmouth "Puedes agradecer los resultados y la reputación de esta escuela.{w=0.5} Muchos exalumnos se convierten en algunos de los Entrenadores y académicos más prestigiosos del mundo."

serena @sadmouth closedbrow "Creo que Diantha en realidad abandonó Kobukan para centrarse en su carrera como actriz."
serena @sadbrow happymouth "Quizás sea un mal ejemplo en cuanto a los exalumnos que sí se graduaron..."

hilda @talkingmouth "Veamos, están Alder y Bruno enseñandos gimnasia.{w=0.5} El instructor Koga, Máximo Stone... eh..."

bianca @happy "¡No olvides a Cynthia~!"

narrator "Conversas casualmente con el resto del grupo sobre celebridades mientras el almuerzo llega a su fin."

$ renpy.music.set_volume(0.1, delay=1.0, channel="music")

show blank2 with dis

$ PlaySound("BellChime.ogg")
$ renpy.music.set_volume(1.0, delay=4.0, channel="music")

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_9

$ renpy.pause(1.0, hard=True)

narrator "Es hora de ir a la siguiente clase."

window hide
scene blank2
$ renpy.music.stop(channel='crowd', fadeout=1.0)

jump PickElective