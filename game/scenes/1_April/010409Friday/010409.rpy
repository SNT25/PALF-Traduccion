label day010409:

$ timeOfDay = "Morning"
call calendar(1) from _call_calendar_5
$ calDate = calDate.replace(day=9, month=4, year=2004)

show morning at vspaz

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)

show homeroom behind oakbg

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade    
hide morning

show oakbg with dis

$ renpy.pause(0.6, hard=True)

redmind uniform @thinking "A pesar de la bomba de ayer, Sam parece tan tranquilo como siempre. Supongo que él cree que su parte en esto ya terminó y ahora solo está esperando que lleguen los datos..."
oak @talkingmouth "Bien, ¿alguien recuerda lo que decía la lectura sobre el origen de los Pokémon de tipo Hada? [first_name], ¡parece que estás prestando atención! ¿Por qué no lo intentas?"
redmind @surprised "¡Oh, mierda! ¿Qué acaba de decir? Algo sobre la lectura y los tipo Hada... Ugh, ¿qué debería {i}decir{/i}?"

menu:
    "{color=#66b77d}[[Knowledge]{/color} >Recitar toda la lectura":

        red @closedeyes talking2mouth "Bueno, Profesor, para comprender el origen de los Pokémon de tipo Hada, primero es necesario entender la importancia de la reclasificación, tal como se define en la página 347, donde el tipo 'Hada', anteriormente considerado como..."

        $ TraitChange("Knowledge")

        $ PlaySound("class_groan.ogg")

        narrator "Tus compañeros se molestan contigo y Flannery se queda dormida, pero logras responder la pregunta...{w=0.5} pero te tardas quince minutos."

    "{color=#60c2f8}[[Wit]{/color} >Dar una respuesta vaga, pero correcta":
        red @closedeyes talking2mouth "La respuesta es sencilla, la opinión de la lectura coincide exactamente con la del reconocido investigador de los Pokémon de tipo Hada, el Profesor Peach."

        redmind @thinking "Sí... porque él fue consultor en la redacción del libro y..."

        $ TraitChange("Wit")

        narrator "Aunque desconcertado, el Profesor Oak parece satisfecho con esta respuesta."

redmind @thinking "Ugh, es exactamente este tipo de cosas, como quedarme dormido, lo que hizo que mis notas fueran tan malas en Pueblo Paleta. De verdad tengo que concentrarme más."

jump homeroom1transition