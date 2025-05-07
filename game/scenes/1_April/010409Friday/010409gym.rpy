label gym010409:

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

alder norm @norm2 "[first_name], ¿puedo hablar contigo un momento?"

red uniform @talkingmouth "Por supuesto, profesor."

$ starter_species_name = pokedexlookup(starter_id, DexMacros.Name)
alder happy @happy2 "He notado que tu [starter_species_name] se está volviendo más fuerte. ¡Buen trabajo!"

$ startergenderpronoun = "él" 
if (playerparty[0].GetGender() == Genders.Female):
    $ startergenderpronoun = "ella"
elif (playerparty[0].GetGender() == Genders.Unknown):
    $ startergenderpronoun = "ellos"
red @happy "¡Oh! Eh... gracias, señor. Siento que [startergenderpronoun] realmente lo está intentando."

bruno norm @norm2 "Este es un momento crítico para tu [starter_species_name]. Los primeros niveles influirán en cómo evoluciona tu Pokémon en todas sus futuras batallas."
alder @happy2 "¡Exacto! Unas cuantas clases más, un poco más de estudio... y estarás en ese punto. Hablando de batallas, tu compañero asignado hoy es..."

hide alder
hide bruno 
with dis

show nate uniform with dis

red @happy "¡Hola, Nate!"

$ firstletter = first_name[0]
nate @happybrow happymouth "¡[firstletter]! Quiero ver cómo peleas. Dame un buen combate, ¿sí?"
red @angrybrow happymouth "Haré lo mejor que pueda, pero esta vez Bianca no estará aquí para ayudarte."
nate happymouth "Créeme, no la voy a necesitar. ¡Cuando mi equipo se pone en marcha, trituramos la basura!"
red @confused "...{w=0.5} Espera, ¿a qué viene esa sonrisa?"

$ HealParty()
$ trainer1 = Trainer("red", TrainerType.Player, playerparty)
$ trainer2 = Trainer("nate", TrainerType.Enemy, [
    Pokemon(599, level=2, gender=Genders.Unknown, moves=[GetMove("Vise Grip")], ability="Clear Body"),#Klink
    Pokemon(568, level=3, gender=Genders.Female, moves=[GetMove("Pound"), GetMove("Poison Gas")], ability="Aftermath")])#Trubbish

call Battle([trainer1, trainer2], uniforms=[True, True]) from _call_Battle_6
$ battlehistory["Nate1"]  = _return

$ HealParty()

stop music fadeout 1.0

hide alder
hide bruno

pause 1.0

show alder norm at centerside with dis
show bruno think at leftside with dis
show nate uniform at rightside with dis

$ renpy.music.play("Audio/Music/Gym_Loop.ogg", channel='music', loop=True, fadein=1.25, tight=None)
    
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

hide blank2

python:
    klinkfainted = False
    for mon in trainer2.GetTeam():
        if (mon.GetHealth() == 0):
            klinkfainted = True
    
if (not klinkfainted):
    nate @closedbrow happymouth "Oh... ¡te perdiste mi juego de palabras! Verás, mi segundo Pokémon era un Trubbish. ¿Lo entiendes? ¿Engranajes? ¿Basura?"

red uniform frownmouth "{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}{nw}"
extend @talking2mouth "¿De verdad creíste que eso era gracioso?"

nate happy "¡Sí, totalmente! ¡La expresión en tu cara cuando lo entendiste... jajajaja!"

red @talkingmouth "Dime que no creaste este equipo solo para hacer ese chiste."

nate -happy @talkingmouth "Nah, no llegaría {i}tan{/i} lejos. Hice el equipo {i}y luego{/i} pensé en el chiste."

red @talking2mouth "Eso es...{w=0.5} un poquito mejor."

if (WonBattle("Nate1")):
    nate @angrymouth closedbrow "En fin, estoy un poco molesto conmigo mismo por perder... pero, bueno, estos son Pokémon nuevos."

    nate @happy "Entonces, ¿cuál es tu secreto? ¡Estabas en perfecta sincronía con tu mon todo el tiempo! No me digas que es el inicial que te dio la escuela."

    red @closedeyes talkingmouth "Hombre, no me creerías aunque te lo dijera."

    nate @talkingmouth "Está bien. Hay secretos que tienen que quedarse así, ¿no? Lo respeto."

    $ ValueChange("Nate", 3, 0.75)

    nate @talkingmouth "Nos vemos, [firstletter]."

else:
    nate @angrymouth closedbrow "De todos modos, fue una buena pelea. Entrena un poco para la próxima. Ni siquiera tuve que sacar mis estrategias secretas esta vez..."

    red @angrybrow talking2mouth "Créeme, lo haré. No voy a perder contra ti otra vez."

    nate @happy "¡Lo espero con ansias, [firstletter]!"

jump lunchtransition