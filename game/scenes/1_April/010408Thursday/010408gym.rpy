label gym010408:

$ timeOfDay = "Noon"

  

play music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

$ renpy.transition(dissolve)
show screen currentdate

scene gym with dis

show blank2 behind gym

$ renpy.pause(2.0, hard=True)

hide blank2

show alder spunky2 with dis:
    xpos 0.66

show bruno think with dis:
    xpos 0.33

alder @talkingmouth "Y con esto concluye la lección de hoy."

pause 2.0

alder norm @norm2 "[first_name], ¿me permites un momento?"

red uniform @surprised "¿Oh? Uh, sí, por supuesto, profesor."
redmind @thinking "Mierda. Espero que esto no tenga que ver con lo que dijo Lance..."

if (WonBattle("Blue1") and WonBattle("Cheren1")):
    alder happy2 "Has estado ganando bastante. Contra Blue, contra Cheren... Lo cual es bueno, por supuesto."
    alder sad @sad2 "Pero eso conlleva ciertas expectativas."
elif (not (WonBattle("Blue1") or WonBattle("Cheren1"))):
    alder sad @sad2 "o te ha ido muy bien contra tus compañeros hasta ahora, y creo que Bruno y yo hemos descubierto por qué."

bruno @think2 "Tus Pokémon no están mejorando."

red @surprised "¿Eh?"

alder norm @norm2 "Bueno, es como él dice. Ese [starter_species_name] tuyo ya ha estado en varias batallas, pero no ha cambiado en absoluto."

bruno norm @norm2 "Has tenido mucha suerte de que te obedezca. Nunca había visto un Pokémon tan disciplinado."

alder @spunky2 "Pero incluso el Pokémon más obediente tendrá problemas si pelea contra otro el doble de fuerte."

$ startergenderpronoun = "él" 
if (playerparty[0].GetGender() == Genders.Female):
    $ startergenderpronoun = "ella"
elif (playerparty[0].GetGender() == Genders.Unknown):
    $ startergenderpronoun = "él"
red @closedbrow talking2mouth "¿Y que puedo hacer para que [startergenderpronoun] se vuelva más fuerte entonces?"

show bruno surprisedbrow frownmouth
show alder surprisedbrow frownmouth
with dis

show blue uniform at rightside with dis:
    xzoom -1 xpos 0.85

blue @happybrow happymouth "¡JA! ¿Qué clase de idiota no sabe entrenar a su propio Pokémon? No mereces estar en esta academia."

pause 2.0

show bruno norm with dis

alder angry2 "... Sr. Oak. No toleramos ese tipo de comentarios en esta clase. {w=1.0}{nw}"
extend happy @happy2 "Además, ¿para qué crees que existe la Academia Kobukan, si no es para enseñar a la gente a entrenar Pokémon? Parece que el Sr. [last_name] está aprovechando bien su dinero."

pause 1.0

blue closedbrow talkingmouth "Pff... Como sea. Estaré por ahí y {i}no{/i} hare perder el tiempo de nuestros profesores."

redmind @unamusedbrow unamusedmouth "Me da la sensación de que si ya lo sabe todo, entonces el único que está perdiendo su tiempo aquí es él..."

hide blue at rightside with dis

red @happy "Volvamos al tema... ¿Entrenamiento? ¿Cómo puedo hacerlo?"

bruno @norm2 "Debes criticar a tu Pokémon."

red @surprised "¿Q-qué? ¿Criticar? Pero... [starter_name] es mi compañero. No sé si quiero hacer eso..."

alder norm3 @norm4 "Criticar quizá sea una palabra un poco dura, pero Bruno tiene razón." 
alder @norm4 "Tienes que hacerle saber a tu Pokémon cuándo está fallando y cuándo lo está haciendo bien. Si no, seguirá haciendo lo mismo una y otra vez, sin ganar experiencia."

red @sadeyes sadeyebrows talking2mouth "Pero... Nunca he hecho algo así. Digo, incluso dejaba que mi Pikachu en casa se subiera al mostrador"

alder sad @sad2 "¿Cuál es tu sueño, [first_name] [last_name]?"

red @talking2mouth "Eh... Convertirme en un Campeón. Como usted, señor."

alder happy @happy2 "Bueno, por tu bien, ¡espero que llegues a ser mucho mejor que yo! Pero déjame decirte algo sobre los Pokémon."
alder spunky @spunky2 "Son inteligentes, muy inteligentes, más de lo que incluso los profesores que los estudian creen."

alder norm @norm2 "Pero necesitan a los humanos para aprovechar esa inteligencia. Humanos y Pokémon son el equipo perfecto." 
alder sad @sad2 "Uno tiene el poder, el otro sabe cómo usarlo. Eh... No es que el poder, por sí solo, sea algo bueno, pero esa es otra lección."

red @closedbrow talking2mouth "Bueno... Entonces, ¿qué debo hacer, señor?"

alder @happy2 "Si tu Pokémon falla un ataque, dile por qué. Si fue demasiado lento para reaccionar, anímalo a ser más rápido. Si no se toma en serio a su oponente, regañalo."
alder norm @angry2 "No dejes que tu Pokémon te dé menos de lo que sabes que es capaz de dar."

red @closedbrow talking2mouth "Pero... ¿Cómo sabré de lo que es capaz?"

alder @norm2 "Parte de eso lo aprenderás estudiando y con la experiencia. Además, {color=#0048ff}tus clases electivas de tipos deberían darte una idea de lo que pueden hacer tus Pokémon{/color}."

bruno norm @norm2 "{color=#0048ff}Tus electividades aumentarán el poder máximo que tu Pokémon puede alcanzar. Tus batallas, como las de este gimnasio, aumentarán su poder real.{/color}"

red @closedbrow talking2mouth "Entiendo... Por ahora estoy saltando entre electivas, pero si me concentro mucho en una sola, ¿podría hacer que mi Pokémon se vuelva súper fuerte rápidamente?"

bruno think @think2 "No, aún tendrías que entrenar a tus Pokémon mediante batallas." 
alder happy @happy2 "No hay mucho que puedas hacer para acelerar el proceso, salvo esperar a que pase el tiempo. Tus compañeros se fortalecerán con el tiempo, así que tendrás rivales más desafiantes que te daran mejores recompensarán si logras vencerlos."

red @closedbrow talking2mouth "Entiendo...{nw}" 
extend @confused " Espera, ¿qué pasaría si entreno a un Pokémon antes de tomar suficientes clases electivas para saber de lo que es capaz?"

bruno norm @norm2 "Si tomas la electividad en otro momento, no habrá ningún problema. Tanto tú como tu Pokémon recordarán la experiencia y podrán aprovecharla en la próxima batalla."

red @closedbrow talking2mouth "Okay."

bruno think @think2 "Y una cosa más, aprenderás más perdiendo que ganando."
alder happy @happy2 "Pero... Si quieres mantener el respeto de tus compañeros y el de tus Pokémon, no pierdas a propósito. Tus batallas en esta clase no se califican, pero {i}nos daremos cuenta{/i} si pierdes demasiado." 

if (WonBattle("Blue1") and WonBattle("Cheren1")):
    alder @happy2 "Aunque eso no debería ser un problema para ti si sigues como vas hasta ahora."

alder @happy2 "En fin, tu oponente de hoy será este joven. Creo que ya se conocen, ¿no?"

show alder spunky2 with dis:
    xpos 0.66 alpha 1.0
    ease 0.75 alpha 0.0

show bruno think with dis:
    xpos 0.33 alpha 1.0
    pause 0.25
    ease 0.75 alpha 0.0

show silver uniform with dis

pause 2.0

red @surprised "Oh." 
red @wince talking2mouth "Hola, Silver."

silver "{w=0.5}.{w=0.5}.{w=0.5}."

red @happyeyes happyeyebrows talkingmouth "Eh... Gracias por defenderme el otro día."

silver ".{w=0.5}.{w=0.5}.{w=0.5}{nw}"
extend @talkingmouth "¿Hablabas en serio?"

red @surprised "¿Eh?"

silver @sad "Lo de entrar al equipo de batalla, sin importar qué."

red @talkingmouth "Sí, va a pasar para mí y para [pika_name], y si lo quieres, también para ti."

silver "{w=0.5}.{w=0.5}.{w=0.5}."

silver angry "Demuéstramelo."

$ HealParty()
$ trainer1 = Trainer("red", TrainerType.Player, playerparty)
$ trainer2 = Trainer("silver", TrainerType.Enemy, [Pokemon(451, gender=Genders.Male, level=3, moves=[GetMove("Poison Sting"), GetMove("Leer"), GetMove("Hone Claws")], ability="Sniper")])#Skorupi

call Battle([trainer1, trainer2], uniforms=[True, True]) from _call_Battle_3
$ battlehistory["Silver1"]  = _return

$ HealParty()

stop music fadeout 1.0

hide alder
hide bruno

pause 1.0

show alder norm at centerside with dis
show bruno think at leftside with dis
show silver uniform at rightside with dis

$ renpy.music.play("Audio/Music/Gym_Loop.ogg", channel='music', loop=True, fadein=1.25, tight=None)
    
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

hide blank2

if (WonBattle("Silver1")):
    silver @angrymouth closedbrow "Maldición... Te fallé, Skorupi. Lo siento."

    red uniform @happy "¡Fue una gran batalla! No seas tan duro contigo mismo."

    silver @sad "... Lance tenía razón.{w=0.5} El poder es lo único que importa en este mundo."

    red @surprised "¿Qué?"

    $ ValueChange("Silver", 3, 0.75)

    silver smilemouth @happy "Pero el poder no es lo que él cree. Déjame ver lo que significa para ti, [first_name]."

else:
    silver ".{w=0.5}.{w=0.5}.{w=0.5}{nw}"
    extend @talkingmouth "Esto no es suficiente. Necesitas mejorar si no quieres fallarle a tus Pokémon."

    red uniform @closedeyes talking2mouth "Lo sé, estoy trabajando en ello."

    silver @closedbrow talkingmouth "... Nos vemos."

jump lunchtransition