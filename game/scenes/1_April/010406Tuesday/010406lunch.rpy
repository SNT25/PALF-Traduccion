label lunch010406:

$ timeOfDay = "Afternoon"

show cafe behind blank2

queue music "Audio/Music/Route 1 Anime.ogg"

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade
$ renpy.pause(0.5, hard=True)

hide afternoon

redmind uniform @wince frownmouth "¡Ufff!"

redmind @thinking "Estoy agotado...{w=0.5} Puede que sea la presión de tener a toda la clase observándome durante la batalla, pero me siento mucho más cansado de lo que debería."
redmind @thinking "Quiero decir, ni siquiera soy yo quien estaba peleando de verdad, [starter_name] es quien hace todo el trabajo... Entonces, ¿por qué estoy tan cansado?"

show cafe at vpunch

show hilda uniform angry at rightside

hilda @talkingmouth "¡Oye, [first_name]! ¿Qué demonios fue eso?"

red @confused "Eh... ¿Hola, Hilda?"

hilda sad "Sí, sí, hola, lo que sea.{w=0.5}{nw}"
extend angry @talkingmouth " ¡¿Pero qué demonios fue eso?!"

red @happy "Vas a tener que ser mucho más específica."

show brendan uniform at leftside with dis:
    xzoom -1

show may uniform at centerside with dis

may @talkingmouth "¡Hey, [first_name]! ¿Pasa algo?"

red @happy "Nah, solo charlando con Hilda. Parece que tiene algunas dudas... eso creo."

hilda -angry @talkingmouth "No te hagas el que no tienes idea de lo que pasó."

red @talking2mouth "Entonces voy a seguir sin hacerme el que no tengo idea de lo que pasó."

brendan @talking2mouth "Uh... bro, creo que está hablando de cómo [starter_name] acaba de hacer exactamente lo que le dijiste."

red @confused "¿Ah?"

may @happy "Brendan me contó que dejaste salir a tu Pokémon en el dormitorio y que se quedó completamente quieto. No estaba segura de creerle, ¡pero ahora lo vi con mis propios ojos!"

hilda @talkingmouth "Exacto. Es un Pokémon completamente nuevo, no puedes entrenarlos para que sean así de obedientes. Literalmente, {i}no puedes entrenarlos{/i}."

show cheren uniform at midleftside with dis

cheren @closedbrow talkingmouth "Debo decir que también noté el comportamiento peculiar de tu Pokémon. Quería preguntarte sobre cómo lograste hacer eso..."

show gardenia uniform at midrightside with dis

show may surprisedbrow frownmouth
show brendan surprisedbrow frownmouth
show hilda surprisedbrow frownmouth 
show cheren surprisedbrow
with dis

gardenia @happy "¡Sí, fue súper raro! Si no supiera nada del tema, diría que llevas meses entrenándolo."

if (not persondex["Gardenia"]["Named"]):
    pause 1.5

    red @confused "Eh... ¿te conozco?"
    gardenia @surprised "Oh, supongo que no.{w=0.5}{nw}"
    $ BecomeNamed("Gardenia")
    extend @happy " ¡Soy Gardenia! Bueno, volviendo al tema... ¿cómo es que combates así, amigo?"

else:
    red @sweat unamusedbrow talking2mouth "Oh, hola, Gardenia."

show may -surprisedbrow -frownmouth
show hilda -surprisedbrow -frownmouth
show cheren -surprisedbrow
show brendan -surprisedbrow -frownmouth
with dis

brendan -surprisedbrow -frownmouth -surprised @closedbrow talking2mouth "Uh... bro, ¿te diste cuenta de que hiciste amigos bien rápido, [first_name]?"

cheren @happy "Como dije: 'carisma inofensivo'."

show calem uniform at farleftside with dis

calem @talkingmouth "[first_name], yo..."

pause 1.0

calem @sad "Hmm. Hay demasiada gente aquí, hablaremos en otro momento."

hide calem at farleftside with dis

show hilbert uniform at farleftside with dis:
    xzoom -1

hilbert @talkingmouth "Yo tomaré su lugar, tienes que responder algunas preguntas."

show leaf uniform at farrightside with dis

leaf @talkingmouth "Oigan, ¿qué pasa con la multitud?"

show may surprisedbrow frownmouth
show brendan surprisedbrow frownmouth
show hilda surprisedbrow frownmouth 
show cheren surprisedbrow frownmouth 
show leaf surprisedbrow frownmouth 
show gardenia surprisedbrow frownmouth
show hilbert surprisedbrow frownmouth
with dis
red @surprised "¡Chicos! No tengo respuestas. Solo le pido a mi Pokémon que haga algo, ¡y lo hace!"


show may -surprisedbrow -frownmouth -surprised
show brendan thinking 
show hilda sad 
show cheren thinking
show leaf flirt
show gardenia happy
show hilbert sad
with dis

red @talking2mouth closedbrow "O sea, eso es lo que {i}hacemos{/i} los entrenadores, ¿no?"

hilda @talkingmouth "Bueno... supongo."
brendan @talking2mouth "Sí, pero, bro, tú lo haces ver tan fácil..."
cheren @sadmouth "Tal vez estás aplicando algún tipo de estrategia de forma subconsciente."
hilbert @talkingmouth "Eso es un monton de mierda. No te creo."

show hilbert:
    xpos 0.12
    ease 0.5 xpos -0.2

redmind @thinking "... Agh. No están escuchando, ¿verdad?"

hide may at centerside with dis
hide brendan at leftside, dissolveaway 
hide hilda at rightside with dis
hide cheren at midleftside with dis
hide leaf at farrightside with dis
hide gardenia at midrightside with dis

redmind @thinking "Creo que Sam es el único que podría responderme esta pregunta... pero juro que me está evitando a propósito."
redmind @thinking "Tal vez pueda encontrarlo después de mi siguiente clase."

pause 2.0

if (not WonBattle("Blue1")):
    red @surprised "Esperen... {i}perdí{/i} esa batalla. ¿Todos vinieron a... animarme?"
    pause 1.0
    red @happy "Son unos tontos...{w=0.5} gracias."
    pause 1.0

show ethan uniform at centerside with dis

ethan @talking2mouth "Hey, bro."

red @talkingmouth "¡Hey!"

ethan @happy "Buena batalla. Como tenemos el mismo Pokémon, puedo aprender a luchar mejor viendo cómo lo haces tú."

red @angrybrow happymouth "¿Qué, soy como un muñeco de pruebas ahora?"

ethan @closedbrow talkingmouth "Bueno, no un muñeco. Pero sí... {i}algo{/i} por el estilo."

red @talkingmouth "Bueno, tal vez no deberías seguir mi ejemplo exactamente."

if (not WonBattle("Blue1")):
    red @sad "Después de todo, no gané."

    ethan @happybrow talkingmouth "Sí, pero eso no fue porque [blue_name] sea mejor."

else:
    ethan @happybrow talkingmouth "¿Por qué no? ¡Ganaste!"

    ethan @closedbrow talking2mouth "Aunque supongo que no fue del todo gracias a ti..."

ethan @angrybrow talkingmouth "Sabes tan bien como yo que el Eevee de [blue_name] no le estaba haciendo el menor caso."

red @talking2mouth "Sí, no puedo negar eso. Aunque tiene sentido que le tocara un Pokémon tan testarudo. De tal entrenador, tal Pokémon."

ethan @closedbrow talking2mouth "Me pregunto..."

red @confused "¿Qué cosa?"

ethan @closedbrow talking2mouth "Es solo que... la conversación que tuvimos en el dormitorio anoche, sumado a algunas cosas que dijo el Profesor Cherry."

red @confused "¿Tú también tienes la vibra de que la gente cree que entrenar Pokémon es mucho más difícil de lo que nos ha parecido hasta ahora?"

ethan @surprised "¡Sí! ¡Eso es exactamente lo que estaba pensando!"

red @closedbrow talking2mouth "Entonces, o somos muy buenos en esto..."

ethan @closedbrow talking2mouth "O estamos a punto de descubrir por qué los demás lo ven tan difícil."

red @happy "Esperemos que sea lo primero."

ethan @happy "¡Crucemos los dedos de que así sea!"

show blank2 with dis
    
$ renpy.pause(1.0, hard=True)

stop music fadeout 1.0
$ renpy.music.stop(channel='crowd', fadeout=1.5)

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_24

$ renpy.pause(2.0, hard=True)

jump PickElective