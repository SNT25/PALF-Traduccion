label lunch010407:

$ timeOfDay = "Afternoon"

show cafe behind blank2

queue music "Audio/Music/Route 1 Anime.ogg"

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade
$ renpy.pause(0.5, hard=True)

hide afternoon

redmind uniform @closedeyes frownmouth "Hmm... Parece que hay un montón de mesas diferentes en las que me puedo sentar. Sé que elegir una mesa para sentarse es un asunto serio, así que no debería tomármelo a la ligera."
redmind "Para no arruinar por completo mi vida social, {color=#0048ff}mejor me siento solo en mesas donde conozca a todos y me lleve bien con ellos.{/color}"

pause 1.0

narrator "[bluecolor]Para ser absolutamente claro, necesitas al menos un punto de vínculo con cada personaje de una mesa para sentarte allí.{/color}" 

python:
    validtables = []
    tables = ["Angry Table", "Cheerful Table", "Busy Table", "Romantic Table", "Calm Table", "Quiet Table"]
    for table in tables:
        tablevalid = True
        for i, character in enumerate(GetCharsInTable(table)):
            value = (persondex[character]["Value"] if character in persondex.keys() and "Value" in persondex[character].keys() else 0)
            if (value < 1):
                tablevalid = False
        if (tablevalid):
            validtables.append(table)
        
    if (len(validtables) == 0):
        renpy.say(None, "{}Ya que actualmente no puedes sentarte en ninguna mesa principal, prueba la Mesa Dormilona, con Ethan. (Arriba a la izquierda.){{/color}}".format(bluecolor))

jump PickTable