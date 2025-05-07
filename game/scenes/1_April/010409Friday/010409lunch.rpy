label lunch010409:

############################################################################################################################################################################################################################
#### 2. LUNCH SCENE ########################################################################################################################################################################################################
############################################################################################################################################################################################################################



queue music "Audio/Music/Road to Viridian City.ogg"

scene cafe with splitfade

$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(0.5, hard=True)

hide afternoon

show brendan uniform:
    xpos 1.0/7.0 xzoom -1
show may uniform:
    xpos 2.0/7.0
show ethan uniform:
    xpos 3.0/7.0
show leaf uniform:
    xpos 4.0/7.0
show serena uniform:
    xpos 5.0/7.0 xzoom -1
show calem uniform:
    xpos 6.0/7.0 xzoom -1
with dis

brendan @surprised "¡Uff, estoy agotado!{w=0.5} Sé que solía quejarme mucho del instituto en Villa Raíz, pero ahora hasta lo extraño."

may @happy "Eso era la secundaria, Brendan.{w=0.5} En la universidad, las cosas deben ser un poco más difíciles."

ethan @sad "Esto es {i}mucho{/i} más que solo 'un poco más difícil'. Es como pasar de estar en una piscina infantil a estar en medio del océano, en plena tormenta, con una balsa inflable."

leaf @talking2mouth "Y tú, [first_name], ¿qué tal te van en las clases?{w=0.6}{nw}"

extend @flirttalk " ¿Listo para rendirte?"

menu:
    "Todo va bien.":
        red uniform @talkingmouth "Creo que lo llevo bastante bien.{w=0.5} Es un poco más difícil que la secundaria, pero era de esperarse."
        
        leaf @flirtbrow talkingmouth "... Eso fue tan cliché. Hablaste como un verdadero oficinista con el alma drenada."
        
        red @sadeyes sadeyebrows talkingmouth "Vamos, solo estoy diciendo lo que pienso.{w=0.5} No puedes criticarme por eso."
        
        leaf @happybrow talking2mouth "Claro que puedo, y lo haré.{w=0.5} Todos tienen opiniones, [first_name], ¡pero algunas son más entretenidas de escuchar que otras!"
        
        red @closedbrow talking2mouth "Ay, por favor..."

    "¡No lo soporto más!":            
        show brendan surprisedbrow frownmouth
        show ethan surprisedbrow frownmouth
        show calem surprisedbrow
        show may surprisedbrow frownmouth
        show leaf surprisedbrow frownmouth
        show serena surprisedbrow frownmouth
        with dis

        red uniform @sad "¡Es una tortura, se los juro! ¡Nos obligan a combatir {i}todos{/i} los días! ¡Ni siquiera hemos tenido la oportunidad de atrapar nuevos Pokémon y apenas nos queda tiempo para entrenar a los nuestros!" 
        red @angry "¡Hay peleas que simplemente no puedo ganar! Y además... ¡¿qué diablos son esos cuestionarios de batalla?! Solo de recordarlos me duele la cabeza, ni hablar de hacerlos."
        
        pause 2.0

        show brendan happy
        show ethan happy
        show calem -surprisedbrow -frownmouth
        show may -surprisedbrow -frownmouth
        show leaf -surprisedbrow -frownmouth
        show serena -surprisedbrow -frownmouth
        with dis
        
        $ ValueChange("Brendan", 1, 1.0/7.0, False)
        $ ValueChange("Ethan", 1, 3.0/7.0)

        brendan "Bro, ¡estas hablando en {i}basado{/i}!"
        
        leaf @talking2mouth "Eh, ¿no estás siendo un poco melodramático?"
        
        ethan "No lo entiendes, Longaniza.{w=0.5} Algunos no nacimos con una gran inteligencia como tú."

        leaf @angry "(¡¿Longaniza?!)"
        
        brendan @sad "¡Nunca entenderás a los tontos como nosotros!"

        ethan "¡Sí! ¡Somos los tres idiotas!{w=0.5} ¡Todos para uno y uno para todos!"
        
        narrator "Tú y los otros dos idiotas chocan los cinco en señal de camaradería."

        show brendan -happy
        show ethan -happy
        with dis
        
        leaf @closedbrow talking2mouth "Ustedes tres son un caso perdido."
        
    ">Adular a Leaf para esquivar la pregunta":            
        show leaf surprisedbrow
        with dis
        
        red uniform @talkingmouth "¿Y tú, Leaf? Pareces una chica muy lista.{w=0.5} Apuesto a que las clases no son problema para alguien como tú."

        $ ValueChange("Leaf", 1, 4.0/7.0)
        
        leaf @talkingmouth "Oh, no tenía idea de que pensaras eso de mí.{w=0.5}{nw}"
        
        extend -surprisedbrow @happy " ¿De verdad lo crees?"
        
        brendan @angrybrow talking2mouth "¡Oye! No puedes soltar halagos así como así.{w=0.5} Es simplemente...{w=0.25} raro.{w=0.25} ¡Eres raro, bro!"

        may @sadbrow happymouth "A mí no me molestaría que me dijeras algo así de vez en cuando."

        brendan @surprised "¿De veras?{w=0.5}{nw}"
        extend @closedbrow talking2mouth " Bueno...{w=0.25} supongo que está bien."
        
        serena @sadbrow happymouth "Ah, Brendan, a veces puedes ser tan despistado..."

        calem @closedbrow talking2mouth "Entonces... ¿alguien realmente entendió qué piensa [first_name] sobre las clases, o...?"
        
    "¡Esta escuela es demasiado fácil para un genio como yo!" if GetGrade() >= 1:
        show brendan surprisedbrow frownmouth
        show ethan surprisedbrow frownmouth
        show calem surprisedbrow
        show may surprisedbrow frownmouth
        show leaf surprisedbrow frownmouth
        show serena surprisedbrow frownmouth
        with dis
        
        red uniform @talkingmouth "¡Pfft! ¿Me estás tomando el pelo?{w=0.5} Vamos, el último oponente que enfrenté tenía un Trubbish. Un {i}Trubbish{/i}." 
        red @happy "¿Y los cuestionarios de batalla? Hasta alguien que nunca ha visto un Pokémon podría hacerlos con los ojos cerrados."

        may @surprised "¡Guau, [first_name]! No tenía idea de que fueras tan inteligente."
        leaf @surprisedbrow talkingmouth "¿Lo dices en serio?"

        calem -surprisedbrow -frownmouth -surprised @closedbrow talkingmouth "Oh, sí, lo dice completamente en serio y puedo dar fe de ello. Su capacidad de memorización es impresionante."
        calem @surprisedbrow talkingmouth "También lo he visto estudiar con dedicación. Su motivación, en gran parte, me motiva a dar lo mejor de mí."

        show brendan -surprisedbrow -frownmouth
        show ethan -surprisedbrow -frownmouth
        show may -surprisedbrow -frownmouth
        show leaf -surprisedbrow -frownmouth
        with dis

        serena -surprisedbrow -frownmouth -surprised @surprisedbrow talkingmouth "¡Oh! [first_name], no sabía que fueras tan estudioso. Me alegra mucho saberlo."
        leaf @talkingmouth "Estoy impresionada.{w=0.5}{nw}"
        extend @flirttalk " Nunca te hubiera pensado que eras un ratón de biblioteca, [first_name]."

        $ ValueChange("Serena", 1, 5.0/7.0, False)
        $ ValueChange("Calem", 1, 6.0/7.0, False)
        $ ValueChange("Leaf", 1, 4.0/7.0)
        
        red @happy "Bueno, ¿qué puedo decir?{w=0.5} Soy todo un personaje multifacético."
        redmind @thinking "Solo no me pregunten cosas que no tenga que ver con los {i}Pokémon{/i}, por favor."
        
        leaf @flirtbrow talking2mouth "Que no se suba demasiado a la cabeza, listillo."

pause 1.5

may closedbrow frownmouth "[ellipses]"
may @surprisedbrow sadmouth "Siempre se pone ruidoso durante este momento del día...{w=0.5} ¿Una chica no puede relajarse en un lugar tranquilo?"

serena @talkingmouth "Si buscas un lugar para relajarte, ¿no sería más cómodo y silencioso ir a tu habitación?"

may -thinking @sadbrow happymouth "Lo haría, pero no tengo tiempo de ir y volver antes de la próxima clase."
may @happy "Además, en mi habitación no hay nada divertido que hacer.{w=0.5} ¡Pasar el rato con ustedes es mucho más entretenido!"

calem @talkingmouth "Podemos buscar otro sitio si este es demasiado ruidoso."

red @happy "¡Eh, tengo una idea! Serena, Calem, ¿se acuerdan de lo que charlamos el otro día? Algunos amigos mencionaron el jardín, y al parecer es un buen lugar para hacer un picnic."

pause 2.0

show brendan surprisedbrow frownmouth
show ethan surprisedbrow frownmouth
show calem surprisedbrow
show may surprisedbrow frownmouth
show leaf surprisedbrow frownmouth
show serena surprisedbrow frownmouth
with dis

leaf sad "{cps=15}¿Tienes... otros amigos?{/cps}"

red @wince talking2mouth "Uh..."

leaf angry "¡Maldito! ¡Canalla! ¡Miserable! ¡Pensé que teníamos algo especial! ¡Robaste mi corazón solo para destrozarlo sin piedad...! ¡¿Cómo pudiste?! ¡¿Cómo te atreves?!"
leaf @angrybrow angrymouth "¡Otros amigos! ¡De verdad! ¡No puedo creerlo! Mi-- oh, Dios--"
leaf -angry @happy "¡Jajaja, lo siento, jajaja! ¡No puedo seguir con esto! Dios, soy demasiado graciosa."

red @closedbrow talking2mouth "Sí, sí, eres toda una comediante."

leaf @sarcastic "Okay, pero en serio. ¿Quiénes son tus 'otros amigos'?"

$ morefriends_list = []

if persondex["Gardenia"]["Value"] > 0:
    $ morefriends_list.append("Gardenia")
if persondex["Dawn"]["Value"] > 0:
    $ morefriends_list.append("Dawn")
if persondex["Misty"]["Value"] > 0:
    $ morefriends_list.append("Misty")
if persondex["Skyla"]["Value"] > 0:
    $ morefriends_list.append("Skyla")

# Crear la lista completa con los nombres base y los adicionales
$ full_list = ["Hilda", "Bianca", "Hilbert", "Whitney", "Flannery", "Nate"] + morefriends_list + ["Rosa"]

# Convertir la lista en una cadena bien formateada
$ full_list_str = ", ".join(full_list[:-1]) + " y " + full_list[-1] if len(full_list) > 1 else full_list[0]

show leaf surprisedbrow frownmouth with dis

red @closedbrow talking2mouth "Bueno... están [full_list_str]. Ah, y Silver."

ethan @talking2mouth "Bro, estamos en este lugar hace apenas cinco días."

brendan @closedbrow talkingmouth "Tal vez está siendo un poco... flexible con la definición de 'amigo'."

show brendan -surprisedbrow -frownmouth
show ethan -surprisedbrow -frownmouth
show calem -surprisedbrow
show may -surprisedbrow -frownmouth
show leaf -surprisedbrow -frownmouth
show serena -surprisedbrow -frownmouth
with dis

leaf -surprisedbrow -frownmouth -surprised @happy "¡Oh, sí, eso es! ¿Cómo no lo había pensado antes? Quiero decir, ¿alguien de esas {i}docenas{/i} de nombres firmó un Pacto Oficial de Amistad{font=fonts/consola_0.ttf}™{/font}?"

red @closedbrow talking2mouth "¿Nnnno...?"

leaf @flirttalk "Entonces, no cuentan. No son amigos. Lo siento, así son las reglas."

red @closedbrow talking2mouth "Vaya... supongo que nunca he tenido amigos, entonces."

leaf @happy "¡No te preocupes! Haré un Pacto Oficial de Amistad{font=fonts/consola_0.ttf}™{/font} contigo ahora mismo."

red @sadeyes sadeyebrows talkingmouth "Lo siento, me estoy guardando para el matrimonio."

leaf @angrybrow talkingmouth "Ya veremos sobre eso."

pause 2.0

calem @talkingmouth "No es que esta conversación no sea esclarecedora, pero ¿deberiamos dirigirnos a el jardín?"

red @surprised "¡Oh, cierto! Sí, sí, claro."

show may at dissolveaway:
    xpos 2.0/7.0
show leaf at dissolveaway:
    xpos 4.0/7.0
show serena at dissolveaway:
    xpos 5.0/7.0
show calem at dissolveaway:
    xpos 6.0/7.0

pause 2.0

show ethan sadbrow frownmouth with dis

ethan @talkingmouth "... Oye, grandulón."

brendan @talkingmouth "¿Eh? ¿Sí, Ethan?"

ethan @talkingmouth "¿Sabes cómo lo hace?"

brendan @surprisedbrow talkingmouth "¿Hacer qué cosa?"

ethan @talkingmouth "Toda esa gente... Quiero decir, hace amigos con tanta facilidad y tenemos mucho en común, ¿sabes? Así que en teoría yo también debería poder hacerlo." 
ethan -frownmouth @talking2mouth "Pero... no sé. Se siente como si él tuviera algo que yo no."

brendan @happy "Ethan, estás preguntándole eso a la persona equivocada. Desde que los vi a ustedes dos, quise ser amigo de {i}ambos{/i}."

ethan @happy "Ay, gracias grandulón."

brendan @thinking "[ellipses]"

brendan @talking2mouth "¿Me estás llamando 'grandulón' porque olvidaste mi nombre?"

ethan @closedbrow talking2mouth "Sep, lo siento."

brendan @happy "Está bien, hermano. ¡Soy Brendan! Recuerda, ¡Brendan está aquí para hacer amigos! Ahora vamos, tenemos que alcanzar a los demás."

hide brendan with dis

pause 2.0

ethan @closedbrow talking2mouth "No puede ser solo una coincidencia, ¿verdad?"

$ renpy.pause(1.5, hard=True)
    
stop music fadeout 1.0
$ renpy.music.stop(channel='crowd', fadeout=2.0)
$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_39
    
show blank with splitfade
$ renpy.pause(1.5, hard=True)

$ renpy.music.queue("Audio/Music/Celadon_Start.ogg", channel='music', loop=None, fadein=0.5, tight=None)
$ renpy.music.queue("Audio/Music/Celadon_Loop.ogg", channel='music', loop=True, tight=None)

hide cafe

show clouds behind ethan:
    yalign 0.5
show garden behind ethan:
    zoom 1.25 xalign 0.5 zoom 0.85
    ease 5.0 zoom 0.625

hide leaf
hide may
hide brendan
hide ethan
hide calem
hide serena

$ renpy.transition(dissolve)
show screen currentdate

hide blank with splitfade
$ renpy.pause(5.0, hard=True)

show garden:
    zoom 0.625

show leaf uniform with dis:
    xpos 0
    pause 0.2
    ease 1.25 xpos 4.0/7.0

show serena uniform happy behind leaf with dis:
    xpos 0
    ease 0.5 xpos 3.0/7.0

show ethan uniform happy behind leaf with dis:
    xpos 0
    pause 0.25
    ease 1.0 xpos 1.0/7.0

show brendan uniform behind leaf with dis:
    xpos 0
    pause 0.3
    ease 1.5 xpos 2.0/7.0

show may uniform behind leaf with dis:
    xpos 0
    pause 0.5
    ease 1.25 xpos 5.0/7.0
    
show calem uniform behind leaf with dis:
    xpos 0 xzoom -1
    ease 3.0 xpos 6.0/7.0

$ renpy.pause(0.5, hard=True)
    
serena @talkingmouth "Ahhh, ¿no es refrescante?{w=0.5} No hay nada como el aire libre después de pasar tanto tiempo encerrados."

red @talkingmouth "Aire libre es quedarse corto, ¡este es un jardín enorme!{w=0.5} Podría entrar toda la secundaria de mi pueblo en este lugar."
red @happy "Parece que la primavera está en su punto.{w=0.5} Todo está empezando a florecer."
    
serena @talkingmouth "Sí, ¿no es hermoso?{w=0.5} Calem, ¿no te recuerda a los jardines del Palacio Cénit?"

calem @talkingmouth "Más bien, {w=0.5}{nw}"
extend @sad "es como si nunca hubiera salido de casa."

leaf @happy "Escuché que Kalos es una región muy hermosa.{w=0.5} Siempre he querido ir algún día."

calem @talkingmouth "Bueno, si alguna vez vas, deberías visitar Ciudad Témpera. Tiene unas vistas increíbles."

serena @talkingmouth "Deberías ver algunas de las pinturas que Calem hizo de ellas. Tengo fotos de casi todas en mi teléfono."

calem @surprised "¡Ah! Eso quizá no sea lo más... eh... adecuado--"

serena @happy "¿Te gustaría verlas?"

leaf @happy "¿En serio? ¡Eso sería genial!"

red @talkingmouth "¿Qué hay de ti, May?{w=0.5} ¿Hoenn se parece en algo a Kobukan?"

may @closedbrow talking2mouth "Hmmm...{w=0.5}{nw}"
extend @talkingmouth " En términos de clima, supongo que Hoenn es un poco más cálido en esta época del año, pero fuera de eso, nada me llama mucho la atención."

may @sadbrow happymouth "Esperaba ver Pokémon nuevos, pero como Kobukan está tan urbanizado, probablemente no haya muchas especies autóctonas aquí."

leaf @talking2mouth "Bueno, entonces aprovechemos la parte verde que {i}sí{/i} tiene Kobukan y busquemos un buen lugar para hacer un picnic."

brendan @closedbrow talkingmouth "Yeah... about that."

show brendan surprisedbrow frownmouth
show ethan surprisedbrow frownmouth
show calem surprisedbrow frownmouth
show may surprisedbrow frownmouth
show leaf surprisedbrow frownmouth
show serena surprisedbrow frownmouth
with dis

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.0)
$ renpy.music.set_volume(0.5, delay=1.0, channel="crowd")

pause 1.5

brendan @talking2mouth "Parece que la mayoría de los buenos lugares ya están ocupados."
ethan @angry "¡¿En serio?! ¡Incluso aquí afuera! ¿Cuánta gente tiene esta academia {i}exactamente{/i}?"

show brendan -surprisedbrow -frownmouth -surprised
show ethan -surprisedbrow -frownmouth -surprised
show calem -surprisedbrow -frownmouth -surprised
show may -surprisedbrow -frownmouth -surprised
show leaf -surprisedbrow -frownmouth -surprised
show serena -surprisedbrow -frownmouth -surprised
with dis

leaf @happybrow talkingmouth "¡Nye je je! Hay una solución fácil para este problema."

red @angrybrow talking2mouth "Ay aja, ¿qué propones entonces?"

show leaf at getcloser:
    xpos 4.0/7.0

show garden:
    yalign 0.0
    ease 0.03 ypos -10
    ease 0.03 ypos 10
    ease 0.03 ypos 0
    repeat 3
    
leaf happy "{size=44}¡Muy bien! ¡Le daré $1,000 a la primera persona que encuentre un buen lugar!{/size}"
leaf @talking2mouth "[first_name], intenta no hacer nuevos amigos mientras--"

$ PlaySound("Whoosh.ogg")

show garden with vpunch

show brendan surprisedbrow frownmouth
show ethan surprisedbrow frownmouth
show calem surprisedbrow frownmouth
show may surprisedbrow frownmouth
show leaf surprisedbrow frownmouth
show serena surprisedbrow frownmouth
with dis

pause 3.0

show leaf at getfurther:
    xpos 4.0/7.0

ethan @talkingmouth "Uh... creo que él va a ser el ganador."

serena @talkingmouth "YSí, la velocidad con la que salio corrió fue... impresionante."

show brendan -surprisedbrow -frownmouth -surprised
show ethan -surprisedbrow -frownmouth -surprised
show calem -surprisedbrow -frownmouth -surprised
show may -surprisedbrow -frownmouth -surprised
show leaf -surprisedbrow -frownmouth -surprised
show serena -surprisedbrow -frownmouth -surprised
with dis

calem @closedbrow talking2mouth "Hmmm. Bueno, quizá deberíamos dispersarnos también... pero con un poco menos de entusiasmo."

may @happy "¡Sí! Quiero decir, claramente lo necesita más que nosotros. Me pregunto qué va a comprar."

brendan @closedbrow talkingmouth "¿Nuevas zapatillas para correr, quizá? Las que usa todo el tiempo están viejas y con agujeros."

leaf closedbrow talkingmouth "Hmm..."

$ renpy.pause(1.0, hard=True)

hide leaf
hide brendan
hide may
hide ethan
hide calem
hide serena
with dis

redmind "Dios, para ser un jardín tan grande, hay demasiada gente ocupando espacio.{w=0.5} Uno pensaría que habría un lugar tranquilo en algún lado."

show garden:
    zoom 0.625 xalign 0.5
    pause 1.5
    ease 1.25 zoom 0.75 xalign 0.23
    pause 0.25
    ease 1.3 zoom 0.82 xalign 0.9 yalign 0.72
    pause 0.5
    ease 1.0 zoom 0.76 xalign 0.16 yalign 0.9
    pause 0.5
    ease 1.0 zoom 0.625 xalign 0.5
    
redmind "[ellipses]"

$ renpy.music.stop(channel='crowd', fadeout=3.0)

pause 1.5

redmind "[ellipses]"
redmind "Hey, este parece un buen lugar.{w=0.5} Ya era hora, no puedo seguir vagando por este laberinto."
redmind "Ahora toca llamar al grupo."
        
show phone_B 
show phone_A
with fadeinbottom

$ calledleaf = False

menu:
    ">Llamar a Calem" if persondex["Calem"]["Contact"]:
        show calem uniform behind phone_A:
            alpha 1.0 xalign 0.5 zoom 0.9

        $ ValueChange("Calem", 1, 0.5)
            
        calem @talkingmouth "{i}¿Me llamas para informarme? Me siento halagado. ¿Puedo asumir que encontraste un lugar?{/i}"
            
        red @talkingmouth "Sí, es un lugar agradable y tranquilo.{w=0.5} Trae a los demás antes de que termine el almuerzo."
        
        calem @talkingmouth "{i}Esplendido, ¿en donde te encuentras?{/i}"
        
        red @surprised "Uh..."
        redmind @thinking "Genial.{w=0.5} Estaba tan concentrado que no tengo idea de cómo llegué aquí."
        
        red @happyeyes happyeyebrows talkingmouth "Estoy junto a...{w=0.5} unos arbustos llenos de flores,{w=0.5}{nw}"
        
        show calem thinking with dis
        extend @wince talking2mouth " y veo algunos bancos hechos de madera, creo."

        calem @closedbrow talking2mouth "{i}Um, eso... no ayuda mucho.{/i}"
        
        calem @talkingmouth "{i}¿En qué sección te encuentras ahora mismo?{/i}"
        
        red @wince talking2mouth "{size=30}Tal vez debería haber traído un mapa...{/size}"
        
        calem @talkingmouth "{i}No te escuché bien, [first_name], ¿podrías repetirmelo?{/i}"
        
        red @happy "{i}Sí, eh, espera un momento.{w=0.5} Voy a preguntar a alguien y te vuelvo a llamar.{/i}"
        
        calem @talkingmouth "{i}Está bien, hablamos pronto...{/i}{w=0.5}{nw}"
        
        extend happy " {i}eso espero.{/i}"
        
        show calem:
            parallel:
                ypos 1.0
                ease 1.0 ypos 3.0
            parallel:
                alpha 1.0
                ease 0.4 alpha 0.0
    
    ">Llamar a Brendan" if persondex["Brendan"]["Contact"]:
        show brendan uniform behind phone_A:
            alpha 1.0 xalign 0.5 zoom 0.9

        $ ValueChange("Brendan", 1, 0.5)
    
        brendan @talking2mouth "{i}¡Hey, no me lo creo, [first_name]!{w=0.5} ¿Me llamaste a mí? ¡Graciasm bro! ¿Supongo que encontraste un lugar?{/i}"
        
        red @talkingmouth "Sí, es un lugar agradable y tranquilo.{w=0.5} Trae a los demás antes de que termine el almuerzo."
        
        brendan @happy "{i}Genial, genial. ¿Dónde estás?{/i}"
        
        red @surprised "Uh..."
        redmind @thinking "Genial.{w=0.5} Estaba tan concentrado que no tengo idea de cómo llegué aquí."
        
        red @happyeyes happyeyebrows talkingmouth "Estoy junto a...{w=0.5} unos arbustos llenos de flores,{w=0.5}{nw}"
        
        show brendan thinking with dis
        extend @wince talking2mouth " y veo algunos bancos hechos de madera, creo."
        
        brendan @talking2mouth "{i}Eh, sabes...{w=0.5} básicamente acabas de describir todo el jardín.{/i}"
        
        brendan @talking2mouth "{i}¿Sabes en qué sección estás?{/i}"
        
        red @wince talking2mouth "{size=30}Tal vez debería haber traído un mapa...{/size}"
        
        brendan @happy "{i}Perdón, no te escuché bien.{/i}"
        
        red @happy "Sí, eh, espera un momento.{w=0.5} Voy a preguntar a alguien y te vuelvo a llamar."
        
        brendan happy "{i}Tá bien, no hay problema. Llámame cuando lo descubras.{/i}"
            
        show brendan:
            parallel:
                ypos 1.0
                ease 1.0 ypos 3.0
            parallel:
                alpha 1.0
                ease 0.4 alpha 0.0

    ">Llamar a May" if persondex["May"]["Contact"]:
        show may uniform behind phone_A:
            alpha 1.0 xalign 0.5 zoom 0.8 ypos 0.95

        $ ValueChange("May", 1, 0.5)
    
        may @talkingmouth "{i}Oh, ¿me llamaste a mí, [first_name]?{w=0.5}  ¡Ah, cierto! Olvidé que tenías mi número. Entonces, ¿pudiste encontraste un lugar?{/i}"
        
        red @talkingmouth "Sí, es un lugar agradable y tranquilo.{w=0.5} Trae a los demás antes de que termine el almuerzo."
        
        may @happy "{i}¡Genial! ¿En dónde estás?{/i}"
        
        red @surprised "Uh..."
        redmind @thinking "Genial.{w=0.5} Estaba tan concentrado que no tengo idea de cómo llegué aquí."
        
        red @happyeyes happyeyebrows talkingmouth "Estoy junto a...{w=0.5} unos arbustos llenos de flores,{w=0.5}{nw}"
        
        show may thinking with dis
        extend @wince talking2mouth " y veo algunos bancos hechos de madera, creo."
        
        may @talkingmouth "{i}Bueno...{w=0.5} suena muy bonito, pero no estoy segura de poder encontrarlo con esa descripción.{/i}"
        
        may @happy "{i}¿Podrías decirme en qué sección estás?{/i}"
        
        red @wince talking2mouth "{size=30}Tal vez debería haber traído un mapa...{/size}"
        
        may @happy "{i}¿Podrías hablar más fuerte? No te escuché.{/i}"
        
        red @happy "Sí, eh, espera un momento.{w=0.5} Voy a preguntar a alguien y te vuelvo a llamar."
        
        may happy "{i}¡Oki doki! De mientras, voy a decirle a Brendan.{/i}"
            
        show may:
            parallel:
                ypos 1.0
                ease 1.0 ypos 3.0
            parallel:
                alpha 1.0
                ease 0.4 alpha 0.0
    
    ">Llamar a Serena" if persondex["Serena"]["Contact"]:
        show serena uniform behind phone_A:
            alpha 1.0 xalign 0.5 zoom 0.9

        $ ValueChange("Serena", 1, 0.5)
    
        serena @talkingmouth "{i}Oh, ¿me estás llamando a mí, [first_name]?{w=0.5} Ah, claro, recuerdo que intercambiamos números hace un tiempo. Entonces, ¿puedo asumir que encontraste un lugar?{/i}"
        
        red @talkingmouth "Sí, es un lugar agradable y tranquilo.{w=0.5} Trae a los demás antes de que termine el almuerzo."
        
        serena @happy "{i}Fantastique! ¿Dónde estás ahora mismo?{/i}"
        
        red @surprised "Uh..."
        redmind @thinking "Genial.{w=0.5} Estaba tan concentrado que no tengo idea de cómo llegué aquí."
        
        red @happyeyes happyeyebrows talkingmouth "Estoy junto a...{w=0.5} unos arbustos llenos de flores,{w=0.5}{nw}"
        
        show serena thinking with dis
        extend @wince talking2mouth " y veo algunos bancos hechos de madera, creo."
        
        serena @talkingmouth "{i}Seguro que es hermoso... pero, ¿tienes algo más concreto en términos de dirección?{/i}"
        
        serena @happy "{i}Por ejemplo, ¿sabes en qué sección estás?{/i}"
        
        red @talkingmouth "{size=30}Mi sentido de la orientación es tan malo que apenas sé en qué región estoy...{/size}"
        
        serena @happy "{i}¿Dijeste algo? Lo siento, hablaste muy bajo.{/i}"
        
        red @happy "Sí, eh, espera un momento.{w=0.5} Voy a preguntar a alguien y te vuelvo a llamar."
        
        serena happy "{i}De acuerdo, le informaré a Calem y lo mantendré al tanto de la situación.{/i}"
            
        show serena:
            parallel:
                ypos 1.0
                ease 1.0 ypos 3.0
            parallel:
                alpha 1.0
                ease 0.4 alpha 0.0
    
    ">Llamar a Leaf" if persondex["Leaf"]["Contact"]:
        $ calledleaf = True

        show leaf uniform behind phone_A:
            alpha 1.0 xalign 0.5 zoom 0.9
    
        leaf "{i}.{w=0.5}.{w=0.5}.{w=0.5}{/i}"

        red @surprised "Eh... ¿hola? ¿Estás ahí?"

        pause 2.0

        show leaf flirt bigblush with dis

        $ ValueChange("Leaf", 1, 0.5)

        leaf @flirttalk "{i}Jejeje. Me estás llamando a mi teléfono.{/i}"

        red @closedeyes talkingmouth "Ay, Dios. Escuchame, encontré un lugar tranquilo, así que mejor trae a los demás antes de que termine el almuerzo."
        
        leaf -flirt -bigblush @happy "{i}Está bien, está bien. ¿Dónde estás?{/i}"
        
        red @surprised "Uh..."
        redmind @thinking "Genial.{w=0.5} Estaba tan concentrado que no tengo idea de cómo llegué aquí."
        
        red @happyeyes happyeyebrows talkingmouth "Estoy junto a...{w=0.5} unos arbustos llenos de flores,{w=0.5}{nw}"
        
        show leaf thinking with dis
        extend @wince talking2mouth " y veo algunos bancos hechos de madera, creo."
        
        leaf @sarcastic "{i}Así que...{w=0.5} no tienes ni la más minima idea, ¿no?{/i}"
        
        red @talkingmouth "{size=30}O sea, sé que estoy en el jardín...{/size}"
        
        leaf @happy "{i}¡Habla más fuerte! No puedo escuchar tu balbuceo.{/i}"
        
        red @happy "Sí, eh, espera un momento.{w=0.5} Voy a preguntar a alguien y te vuelvo a llamar."
        
        leaf @sarcastic "{i}Más te vale. ¡Hay $1,500 en juego!{/i}"
            
        hide leaf with dis

        pause 2.0

        redmind @thinking "¿$1,500? Pensé que eran $1,000{w=0.5}.{w=0.5}.{w=0.5}."

show phone_B:
    ypos 1080
    ease 1.0 ypos 3000
        
show phone_A:
    ypos 1080
    ease 1.0 ypos 3000
    
redmind @thinking "Bien, tengo que moverme rápido."
redmind @angry "Por supuesto, la {i}única{/i} vez que necesito a alguien cerca, el lugar está vacío.{w=0.5} Tiene que haber alguien con quien pueda habla..."

pause 1.5

show erikaintro:
    alpha 0.0 zoom 1.0
    parallel:
        ease 1.0 alpha 1.0
    parallel:
        ease 5.0 zoom 1.05
show erikaCG awake:
    alpha 0.0 zoom 1.0
    ease 5.0 zoom 1.05
        
$ renpy.pause(2.0, hard=True)

redmind @confusedeyebrows frownmouth "Hmm, parece que alguien tuvo la misma idea de encontrar un lugar tranquilo para dormir.{w=0.5} ¿Pero justo se lo ocurrio hacerlo a la mitad de la jornada escolar?"
redmind @thinking "Podría preguntarle por direcciones, pero realmente no quiero despertar a una desconocida."
redmind "Pero, por otro lado, no veo ni oigo a nadie más cerca..."

show erikaintro:
    alpha 1.0 zoom 1.05
show erikaCG awake:
    alpha 0.0 zoom 1.05

redmind @thinking "Supongo que podría despertarla y preguntarle, pero me pregunto si se enojará por interrumpir su sueño reparado..."

hide garden

menu:
    ">Darle un par de leves sacudidas para despertarla":
        redmind "A buen hambre no hay pan duro."
        redmind "¿Quién sabe dónde estará otra persona en este laberinto?{w=0.5} Intentaré hacerlo con delicadeza."
        
        show erikaintro:
            zoom 1.05
            ease 0.7 zoom 1.1
            ease 0.4 zoom 1.05
            ease 0.5 zoom 1.12
            ease 0.5 zoom 1.05
            
        redmind "Solo le dare...{w=0.5} un par de leves sacudidas...{w=0.5} hasta que despierte..."
        
        erika uniform closedbrow talking2mouth "Mmm..."

        show erikaintro:
            zoom 1.05
        
        redmind "Hey, creo que esta funcionando."
        
    ">Dejarla en paz":
        
        redmind @thinking "No, mejor le pregunto a alguien más.{w=0.5} Con un jardín tan grande, seguro me cruzo con alguien pronto."
        
        redmind @thinking "¿O quizás debería seguir corriendo en línea recta hasta llegar al centro?{w=0.5} Pero, ¿y si alguien del grupo encuentra otro lugar antes? Entonces--"
        
pause 1.0
        
show erikaCG awake with dis

$ renpy.pause(1.5, hard=True)

erika uniform "[ellipses]"

red @happy "¡Hola!"

show erikaintro:
    zoom 1.05
    ease 0.2 zoom 1.0
show erikaCG sad:
    zoom 1.05
    ease 0.2 zoom 1.0

erika surprisedbrow frownmouth @surprised "¡AHHH!"

hide erikaintro
hide erikaCG sad
with dis

show garden behind erikaintro:
    zoom 0.84781 xalign 0.5
    parallel:
        ease 0.03 xalign 0.49
        ease 0.03 xalign 0.51
        ease 0.03 xalign 0.5
        repeat 3
    parallel:
        ease 0.031
        ease 0.03 yalign 0.99
        ease 0.03
        repeat 3
        
show erika surprisedbrow frownmouth with dis:
    xpos 720 ypos 2.0 zoom 1.3565
    ease 0.75 ypos 1.0
    
$ PlaySound("Body Roll.ogg")

red @surprised "¡Wah!"
    
hide erikaintro
hide erikaCG
    
erika sad @sadbrow surprised2mouth "¡P-por favor, aléjate! ¡Te juro que no tengo nada de valor!{w=0.5}{nw}"
extend "¡N-no me hagas daño, es un lugar demasiado público!"

red @surprised "¡¿E-eh?!{w=0.25} Espera, no estaba tratando de...{w=0.25} Déjame expl--"

$ PlaySound("Slap.ogg")
pause 0.1

show erika angry:
    xpos 620 ypos 1.0 zoom 1.3565 rotate 0
    ease 0.1 xpos 520 ypos 1.2 zoom 1.44 rotate -3

show garden at garden_move1

pause 0.25

$ ValueChange("Erika", -1, 620/1920)

red @closedeyes surprisedmouth "Auch, justo en mi lado más fotogénico."

show erika:
    xpos 520 ypos 1.2 zoom 1.44 rotate -3
    ease 0.2 xpos 360 ypos 1.1 zoom 1.3565 rotate 0

show garden at garden_move2

erika sad @surprisedmouth "¡A-aléjate, hay una profesora a la vuelta de la esquina y tengo un Pokémon!"

show garden:
    xpos 960 zoom 0.84781 rotate 0

redmind @frownmouth "Dudo mucho que ambas cosas sean ciertas."

show garden:
    zoom 0.84781
    ease 0.5 zoom 0.625

show erika angry:
    xpos 360 ypos 1.1 zoom 1.3565 rotate 0
    ease 0.5 zoom 1.0 xpos 500 ypos 1.0
    
red @closedeyes talking2mouth "Escucha, cálmate. No te estoy atacando, ni robando, ni nada parecido."
red @sad "Solo quería preguntarte algo. Soy un buen tipo, en serio."

show garden:
    zoom 0.625 xalign 0.5

show erika:
    xpos 500 zoom 1.0
    ease 0.5 xpos 940
    
erika @angry "'Es evidente la bondad que se halla en el corazón del hombre que no habla de sí mismo.'"

show erika surprisedbrow frownmouth with dis

red @happy "Eh... ¿Eso es de un libro?"
red @thinking "[ellipses]"
red @surprised "¡E-espera! ¡Espera, conozco esa frase! ¡{i}El orgullo del paria{/i}! Me, eh, me quedé dormido leyéndolo, pero, um... ¡conozco la referencia!"

erika @talking2mouth "¿Te... {i}quedaste dormido{/i} leyendo {i}El Paria del Orgullo{/i}? ¿Uno de los grandes romances de nuestra época?"

red @happy "Quiero decir, es un gran libro, pero, eh, no tiene nada que ver con los Pokémon, ¿sabes? No era el mejor en la escuela."

red @closedbrow talking2mouth "De hecho, estaba en la parte más baja de mi clase en Pueblo Paleta. Así que... sí, no soy precisamente un erudito."

erika -surprisedbrow -frownmouth @sadbrow talking2mouth "Oh, ¿eres de Pueblo Paleta? ¿En Kanto?"

red @surprised "Espera, ¿en serio has oído hablar de Pueblo Paleta?"

erika @talkingmouth "Por supuesto, mis tutores se aseguraron de que recibiera una educación completa, incluida la geografía de mi región."

erika @talkingmouth "Vivía en Ciudad Azulona antes de que me enviaran aquí."

redmind @thinking ".{w=0.25}.{w=0.25}.{w=0.25} Creo que acabo de encontrar a mi polo opuesto. Yo vengo de un pueblo diminuto y ella de la segunda ciudad más grande de Kanto." 

if (calledleaf):
    redmind @thinking "Yo estoy corriendo por un jardín para ganar $1,500, y sus padres le pagaron tutores."
else:
    redmind @thinking "Yo estoy corriendo por un jardín para ganar $1,000, y sus padres le pagaron tutores."

red @talking2mouth "Bueno, ¿lo ves? Ambos somos de Kanto. A pesar de ese comienzo complicado, podemos encontrar algo en común."

erika sad @talking2mouth "Sí, tienes razón. Supuse lo peor y pensé que actuabas con malas intenciones. Me disculpo."

red @happy "Oye, no te preocupes. También fue culpa mía."

show erika at getcloser:
    xpos 940

erika -sad @talkingmouth "¿Cómo está tu ojo? ¿Te lastimé? Sé un poco de primeros auxilios..."

red @happy "Ah, no te preocupes. Ya he recibido golpes peores."

show erika at getfurther:
    xpos 940

erika @surprised "¿De verdad? Debes de ser todo un rufián experto en las artes del bajo mundo."

redmind @thinking "En realidad, es más porque tienes la fuerza de un Wynaut."

red @talkingmouth "De todos modos, perdón otra vez por despertarte. En realidad, solo estaba tratando de averiguar en qué parte del jardín estoy."

erika @surprised "¿En qué parte...?"

red @closedbrow talking2mouth "Sí, como por ejemplo la sección en la que estamos o cómo llegar aquí desde la entrada principal."

erika sad @sadbrow talkingmouth "Oh... me temo que no lo sé. Solo le dije a mi profesora que quería dormir un rato y me trajo aquí."

red @surprised "Oh, ¿así que {i}realmente{/i} había una profesora a la vuelta de la esquina?"

show erika:
    xpos 940.0/1920.0
    ease 0.5 xpos .75

show kris at leftside with dis

kris @talkingmouth "¡Claro! ¿Cómo puedo ayudarte, muchachito?"

red @confusedeyebrows talking2mouth ".{w=0.25}.{w=0.25}.{w=0.25}{nw}"
extend @talking2mouth "Muy gracioso. ¿Dónde está la {i}verdadera{/i} profesora?"

show erika surprisedbrow frownmouth
show kris surprisedbrow frownmouth
with dis

pause 2.0

kris angrybrow @surprisedmouth "¿{i}Disculpa{/i}?"

red @happy "Quiero decir, gafas y una bata de laboratorio tipo crop-top no te hacen profesora."

show garden at vpunch
show kris at getcloser, leftside

kris @pissedbrow pissedmouth "¡Quizás no, pero mi {i}doctorado{/i} dice lo contrario! ¡¿Te gustaría pasar por mi oficina para que lo veas?!"

red @surprised "Espera... ¿realmente {i}eres{/i} una profesora?"

show kris closedbrow angrymouth at getfurther, leftside with dis

kris @poutmouth "Hmph."

$ BecomeNamed("Professor Cherry")

erika -surprisedbrow -frownmouth @talkingmouth "Eh... ella es la profesora Cherry, mi mentora."

red @surprised "Oh, mierda. Uh, lo siento, señorita... Doctora. ¿Profesora? Doctora Profesora Cherry. Ahora sé quién es usted, es solo que no la vi en la página de los miembros de la facultad."

red @sad "Y, eh, te ves {i}realmente{/i} joven para tener un doctorado."

kris "{w=0.5}.{w=0.5}.{w=0.5}."

kris @angrybrow talking2mouth "¿Cuál es tu nombre?"

red @sad "Eh, [first_name] [last_name], soy compañero de cuarto de Ethan. Creo que lo conoces."

kris "{w=0.5}.{w=0.5}.{w=0.5}."

kris -closedbrow -angrymouth -angrybrow @talkingmouth "Está bien, ya lo supere. Sí, soy profesora, y sí, soy la profesora más joven que ha tenido Kobukan."

red @happy "Bueno, eh... ¡hola! Lo siento mucho, realmente no quise ofenderla."

redmind @thinking "Dios, realmente no estoy en mi mejor momento hoy. Esa noticia de ayer me sigue retumbando en la cabeza."

kris -angrymouth @talkingmouth "¿Dijiste que eres compañero de cuarto de Ethan?"

red @talkingmouth "Sí, así es."

kris @happy "¡Ja! Qué simpático. ¿Y qué piensas de él?"

red @surprised "¿Qué opino de él? Eh... bueno, es un tipo genial, amigable. Aunque hay algo raro, siempre terminamos en los mismos lugares y haciendo las mismas cosas."

kris @happy "¿Él te habló de mí?"

red @closedeyes talking2mouth "No mucho, solo mencionó tu nombre y dijo que eras su profesora principal. Parece que tienen algo de historia, ¿no?"

kris @talkingmouth "Esa es una forma de decirlo. De hecho, solía ser su niñera. Como su papá siempre estaba trabajando, básicamente era como mi hermano pequeño."

red @surprised "{w=0.5}.{w=0.5}.{w=0.5}."

red @angrybrow happymouth "¡Dios mío! ¿Me puedes contar historias embarazosas de Ethan?"

kris @angrybrow happymouth "¿Puedo?"

pause 1.0

red @closedbrow talking2mouth "Ah... casi lo olvido. Perdón, doctora, me encantaría escuchar más sobre Ethan, pero tengo que encontrar un lugar para que mis amigos coman"

kris @talkingmouth "¿Entonces estás haciendo un picnic aquí? Es una buena idea. ¿Te gustaría usar este lugar? Erika y yo íbamos a irnos ya."

$ BecomeNamed("Erika")
$ persondex["Erika"]["Value"] = -1

redmind @thinking "Así que se llama Erika..."

red @closedeyes talking2mouth "Sí, sería genial, de hecho. Eh... ¿sabes cómo llegar aquí? ¿O en qué sección estamos?"

kris @talkingmouth "Claro, es el área con los árboles de {i}Oranomi sinesis{/i}."

pause 2.0

red @wince talking2mouth "Eh... a pesar de mi acento, no soy realmente un granjero. No tengo ni la más mínima idea de qué son."

kris @surprised "Oh, lo siento. Árboles de 'Bayas Oran'."

red @closedbrow talking2mouth "Ah, vale. Creo que vi algunos carteles señalando el 'Huerto Oran' hace un rato, así que los demás deberían poder encontrar el camino hasta aquí."

red @happy "¡Muchísimas gracias, doctora!"

kris @happy "Solo 'profesora' está bien."

erika @sadbrow talkingmouth "Me gustaría, um, disculparme de nuevo por sacar conclusiones precipitadas."

red @talking2mouth "No pasa nada, lo entiendo perfectamente por la situación."

erika @happy "Adiós entonces. 'Entonces, te doy permiso para partir, solo para aumentar la alegría de nuestro eventual reencuentro.'"

red @talkingmouth "Y una cita de un libro antiguo para ti también, Erika."

$ ValueChange("Erika", 2, 0.75, False)
$ ValueChange("Professor Cherry", 1, 0.25)

hide erika
hide kris 
with dis
        
$ renpy.pause(2.5, hard=True)

redmind "Muy bien, es hora de llamar otra vez al grupo."

show blank2 with splitfade
$ renpy.pause(1.5, hard=True)

stop music fadeout 1.5

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

hide brendan
hide ethan
hide calem
hide leaf
hide serena
hide may

show brendan uniform at dissolvein behind blank2:
    xpos 1.0/7.0 xzoom -1
show ethan uniform at dissolvein behind blank2:
    xpos 2.0/7.0
show calem uniform at dissolvein behind blank2:
    xpos 3.0/7.0
show may uniform at dissolvein behind blank2:
    xpos 4.0/7.0
show leaf uniform at dissolvein behind blank2:
    xpos 5.0/7.0
show serena uniform at dissolvein behind blank2:
    xpos 6.0/7.0 xzoom -1

$ renpy.music.play("Audio/Morning_ambience.ogg", channel='crowd', loop=True, fadein=1.0)

hide blank2 with splitfade
$ renpy.pause(1.5, hard=True)

hide text
hide text1
hide text2
hide text3

red @happy "Bueno, ya estamos todos, pero mejor comamos rápido.{w=0.5} La hora del almuerzo va a terminar en nada."

ethan @happy "¡Aja! Yo ya me comí mi almuerzo mientras veníamos.{w=0.5} ¿Lo ves? Siempre estoy dos pasos adelante."

red @surprisedeyes talking2mouth "Supongo que es... una forma de verlo."

show brendan surprisedbrow frownmouth
show ethan surprisedbrow frownmouth
show calem surprisedbrow frownmouth
show may surprisedbrow frownmouth
show leaf surprisedbrow frownmouth
show serena surprisedbrow frownmouth
with dis

$ renpy.music.play("Audio/pokemon/cries/48.mp3", channel="altcry", loop=None)

pause 1.0

ethan @talkingmouth "Whoa, ¿qué fue eso?"

pause 2.0

redmind @surprised "¿Eh? ¿Por qué me están mirando a mí?"

show brendan -surprisedbrow -frownmouth -surprised
show ethan -surprisedbrow -frownmouth -surprised
show calem -surprisedbrow -frownmouth -surprised
show may -surprisedbrow -frownmouth -surprised
show leaf -surprisedbrow -frownmouth -surprised
show serena -surprisedbrow -frownmouth -surprised
with dis

red @happy "¡Perdón, chicos! Aprendí sobre los Pokémon mediante libros, es un poco difícil saber cómo suenan sus gritos solo leyendo un texto."

may @closedbrow talking2mouth "Esperen un segundo, creo que ya sé cuál es..."

brendan @happy "¡Esa es mi chica!"

may @happy "¡Ya lo tengo, es un Venonat! ¡Sabía que tenía que ser tipo Bicho!"

brendan angrybrow happymouth "¡Vamos, cuchurrumin! ¡Vamos a atraparlo para ti!"

may angrybrow happymouth "¡Vamos!"

hide may
hide brendan 
with dis

pause 2.0
    
leaf @talking2mouth "Cambiando totalmente de tema, ¿creen que el Torneo Nacional de este año va a ser una victoria absoluta de la Academia?{w=0.5}{nw}"
extend @surprised " Con lo que vi en la exhibición, no puedo imaginar otro resultado."

calem @talkingmouth "Hmm... no estoy seguro. Janine tiene habilidades impresionantes, no hay duda de que es una entrenadora fuerte a su nivel, pero su mejor Pokémon {i}es{/i} un Venomoth."

ethan @surprised "¿A qué te refieres, Calamari?"

calem @talkingmouth "Bueno, Venomoth no es un Pokémon particularmente fuerte, eso es todo."

red @closedbrow talking2mouth "Estás sonando un poco como Lance."

calem @surprised ".{w=0.25}.{w=0.25}.{w=0.25} Oh, vaya, es cierto. Perdón, los viejos hábitos nunca mueren del todo."

serena @talkingmouth "Independientemente de la fuerza de sus Pokémon, Janine {i}sigue{/i} siendo muy joven. Aún estudia en esta academia, después de todo. No puedo verla como material de Campeona."

leaf @angrybrow talking2mouth "¿Solo porque es joven? La Campeona Nacional de Unova tiene como seis años."

ethan @talkingmouth "En realidad tiene doce."

leaf @sarcastic "Puedes recordar eso, pero no puedes recordar un nombre."

ethan @closedbrow talking2mouth "¿De qué va este Torneo Nacional exactamente?"

leaf @sarcastic "Uh... Es, como, el evento más importante al que cualquier estudiante entrenador espera.{w=0.5} O al menos cualquier entrenador que se respete."

red @talking2mouth "Me gustaría una explicación completa con una porción extra de contexto. Sin sarcasmo, por favor."

leaf @happy "¡Oh, sale enseguida! Cuidado, está caliente."

leaf @closedbrow talkingmouth "Básicamente, la región de Kobukan no es lo suficientemente grande para un desafío tradicional de ocho gimnasios, así que cuatro veces al año, más o menos cada tres meses, todos en Kobukan tienen una semana para competir en los 'Quarter Qlashes'."

ethan @closedbrow talking2mouth "¿Quarter Qlashes?"

leaf @sarcastic "Sí, con dos 'Q' suena ridículo, si me preguntas. En fin, los QQs son mini-torneos de eliminación simple que se hacen todos al mismo tiempo, y en total, debes ganar tres combates en cada serie."

calem @talkingmouth "Si ganas, eliminas a siete personas."

serena @talkingmouth "{i}Personalmente{/i}, elimináras a tres personas."

redmind @thinking "Tal vez sea por sus acentos, pero la forma en que dicen 'eliminar' suena como si quisieran decir 'matar'."

leaf @talkingmouth "Es más o menos lo mismo. Volviendo al tema, si llegas a la final de los cuatro Quarter Qlashes en un año, te permiten participar en el Torneo Nacional al final del año."

ethan @closedbrow talking2mouth "¿Y el ganador de este torneo puede desafiar al Campeón?"

calem @closedbrow talking2mouth "Solo por este año, el ganador simplemente {i}se convertirá{/i} en el Campeón. El Campeón actual de Kobukan renunció más o menos por estas fechas el año pasado."

red @closedbrow talking2mouth "Hmm... solo por curiosidad, ¿algún estudiante de la academia llegó a ser Campeón alguna vez?"

serena @surprised "¿Un estudiante? No, que yo sepa. Aunque la mayoría de los Campeones de Kobukan han sido ex-alumnos."

red @closedbrow talking2mouth "Interesante..."

leaf @sarcastic "Ey, sé lo que estás pensando. Y no, absolutamente no, es imposible."

red @happy "¿Fui tan obvio?"

leaf @closedbrow talkingmouth "Como un libro abierto."

pause 1.0

narrator "Empiezas a charlar sobre trivialidades con tus amigos mientras devoras sándwiches como una máquina, temiendo que te llamen de nuevo a clases."

hide serena
hide calem
with dis

stop music fadeout 8.0

narrator "Eventualmente, Serena y Calem se van, caminando rápido para no llegar tarde."

pause 2.0

show leaf angrybrow
show ethan surprisedbrow frownmouth 
with dis

pause 2.0

hide ethan
show leaf -angrybrow 
with dis

narrator "Y finalmente, tras una mirada especialmente fulminante de Leaf, Ethan los deja solos."

pause 1.0

show leaf at getcloser:
    xpos 5.0/7.0

leaf blush embarrassed "Oye, eh, no tenemos mucho tiempo..."

redmind @surprisedbrow frownmouth sweat "¿?"

leaf -blush flirtbrow bigblush @talking2mouth "Y bueno, sé que estuviste esperando esto, que {i}necesitás{/i} esto, así que..."

redmind surprisedbrow frownmouth @surprised "Esperá, no puede ser, ¿ella va a...?"

$ PlaySound("Get.ogg")

leaf -bigblush -flirtbrow @happy "¡Aquí tienes tus $2,000!"

$ money = 2000

narrator "Leaf te entrega $2,000 en tus manos, las cuales están sudorosas."

red @talkingmouth "Oh."

pause 1.0

red -surprisedbrow -frownmouth -surprised @closedbrow talking2mouth "Espera Leaf, no tenías que... quiero decir, sabía que estabas bromeando."

pause 1.0

leaf sadbrow @talkingmouth "Hey{w=0.5}, está bien, solo acéptalo, ¿sí?"

red @sad "...{w=0.5} ¿Cómo? Quiero decir, ¿cómo conseguiste esto...?"

pause 1.0

leaf @talkingmouth "Solo alguien que realmente lo necesita habría corrido {i}tan{/i} rápido."
leaf @talking2mouth "Además... nunca me respondiste cuando te pregunté si podías pagar para evolucionar a [pika_name]."

red @sad "...No soy tan orgulloso como para rechazarlo, pero..."
red @closedbrow talking2mouth "Tengo que resolver esto por mi cuenta. Ya dependo demasiado de mis amigos."

leaf @surprised "¿Qué? No, no es cierto."

red @sadeyes sadeyebrows talking2mouth "Lo es. Tú nunca me has visto así, pero si no tengo a alguien apoyándome, simplemente...{nw}" 
extend @closedbrow talking2mouth " me apago."

leaf @happy "Bueno, no tienes que preocuparte por eso. Siempre vas a tener {i}alguien{/i} apoyándote. Eres demasiado popular como para quedarte solo, ¿no?"

red @talking2mouth "Eso espero. Por mucho tiempo, Blue fue mi único amigo en Pueblo Paleta, y cuando dejó de ser mi amigo, yo..."
red @talkingmouth "No importa, lo que importa es que decidí que nunca iba a dejar que eso pasara de nuevo."

leaf @closedbrow talkingmouth "¿De veras?"

red @happy "Sí, iba a ponerme en forma, leer todo lo que pudiera conseguir, y hacerme amigo de {i}todos{/i} con los que hablara. Haré todo lo posible para asegurarme de que nunca volviera a perder a todos mis amigos."

leaf @flirttalk "Bueno, creo que ya estás a salvo. Lo único que podría acabar con todos tus amigos ahora sería algo como un meteorito."

red @happy "Estaré atento al pronóstico del clima."

leaf @talking2mouth "Bueno, ¿y qué vas a hacer con ese dinero? ¿Tal vez comprar unas zapatillas nuevas para correr?"

red @happy "Oh, no, las mantengo así a propósito. Podría conseguir unos nuevos, pero me gusta su olor."

leaf @happy "¡Jajaja!{w=0.5} ¡Qué asco!"

show blank2 
hide red
hide leaf
with splitfade

pause 2.0

red uniform @happy "Hey, ¿ya te conté que hice dos nuevas amigas mientras corría? ¡Y una de ellas es una profesora!"
leaf uniform @surprised "¡Por Dios, [first_name]! ¡Tenemos que conseguirte un terapeuta para ayudarte, tu adicción a hacer amigos está destruyendo esta familia!"
red uniform @angry "¡Son mis decisiones, Leaf! ¡Puedo dejar de hacerlo cuando yo quiera!"

pause 2.0

show blue uniform thinking behind blank2
hide blank2 
with dis

blue @talkingmouth "... ¿Un meteorito, eh?"

show blank2
with dis

pause 2.0

jump PickElective