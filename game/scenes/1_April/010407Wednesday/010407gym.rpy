label gym010407:

$ timeOfDay = "Noon"

  

play music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

$ renpy.transition(dissolve)
show screen currentdate

scene gym with dis

show blank2 behind gym

$ renpy.pause(2.0, hard=True)

hide blank2

show alder norm2:
    xpos 0.66 alpha 0.0
    ease 0.75 alpha 1.0

show bruno think:
    xpos 0.33 alpha 0.0
    pause 0.25
    ease 0.75 alpha 1.0

alder @talkingmouth "... ¡Y con eso, terminamos la parte teórica! Espero verlos aplicar lo que aprendieron hoy."
alder -norm2 @happy2 "Ahora, pasemos directo a las batallas. Bruno, ¿podrías ir con cada estudiante y decirles quién es su compañero asignado?"

bruno norm2 "Muy bien."

hide bruno
hide alder
with dis

show ethan uniform with dis

ethan @closedbrow talking2mouth "Así que... así es como funcionara, ¿eh? Espero conseguir a alguien que pueda vencer."

hide bruno
hide alder

if (WonBattle("Blue1")):
    ethan @happy "¿Crees que puedas seguir con tu racha de victorias?"
else:
    ethan @happy "¡Esta es tu oportunidad para redimirte después de ayer!"

red uniform @talkingmouth "Voy a intentarlo, eso puedo asegurartelo."

ethan @talkingmouth "¡Buena suerte!"

hide ethan with dis
show bruno at leftside with dis
show cheren uniform at rightside with dis:
    xzoom -1

bruno @norm2 "Este será tu compañero. Cada uno podrá usar un solo Pokémon, el combate termina cuando uno ya no pueda continuar."

hide bruno at leftside with dis

cheren @happy "Será un placer combatir contra ti."

cheren @angrybrow happymouth "Hagamos esto más interesante con una apuesta."

if (council_campaigning):
    cheren @happy "Quien gane tiene que pasar una hora haciendo campaña para el otro. ¿Qué dices?"

    red @happy "Me sirve, un voto más nunca está de más."

else:
    cheren @happy "Si gano, vas a pasar una hora haciendo campaña para mí en las elecciones del Consejo Estudiantil. ¿Te parece bien?"

    red @angrybrow talkingmouth "Seguro, pero si {i}yo{/i} gano, me convertiré en el jefe supremo del gobierno en las sombras que te controla en secreto."
    
    cheren @surprised "Eh... ¿qué?"

    red @happy "Es broma. Suerte, futuro presi del consejo, pero voy a ganar."

cheren @angrybrow happymouth "No cantes victoria tan rápido, [first_name]. En mi ciudad, Engobe, muchos pensaban que yo tomaría el puesto de Líder de Gimnasio cuando el anterior se retiró."

$ trainer1 = Trainer("red", TrainerType.Player, playerparty)
$ trainer2 = Trainer("cheren", TrainerType.Enemy, [Pokemon(509, gender=Genders.Female, ability="Prankster")])#Purrloin

call Battle([trainer1, trainer2], uniforms=[True, True], gainexp=False) from _call_Battle_4
$ battlehistory["Cheren1"]  = _return

$ HealParty()

stop music fadeout 1.0

hide alder
hide bruno

pause 1.0

show alder norm3 at centerside with dis
show bruno think at leftside with dis
show cheren uniform at rightside with dis:
    xzoom -1

$ renpy.music.play("Audio/Music/Gym_Loop.ogg", channel='music', loop=True, fadein=1.25, tight=None)
    
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

hide blank2

if (WonBattle("Cheren1")):
    cheren @sadbrow talking2mouth "Ah, parece que cometí algunos errores tácticos..."

    red uniform @happy "Ah, no te preocupes. A este nivel, los combates son como acertar un cara o cruz."

else:
    cheren @happy "Bien hecho, Purrloin, te merecías esta victoria."

    red uniform @happy "Oye, ¡no te quites mérito tampoco!"

cheren @talkingmouth "Gracias. Ha sido un combate muy entretenido, espero nuestra revancha pronto."

jump lunchtransition