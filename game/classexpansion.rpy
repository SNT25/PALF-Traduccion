default seenclasses = { }

init python:
    #Good functions to look for: IsBefore, IsDate, IsAfter, IsPresent, IsAbsent, GetRelationshipRank
    genericclasssceneconditionals = {
        "bug_class_x1" : (lambda: IsDate(23, 4, 2004)),
        "bug_class_x3" : (lambda: IsAfter(9, 5, 2004) and IsBefore(15, 5, 2004) and not (rescuedwill)),
        "bug_class_x4" : (lambda: IsDate(19, 7, 2004)),
        "dark_class_x1" : (lambda: IsDate(23, 4, 2004)),
        "dark_class_x3" : (lambda: IsAfter(9, 5, 2004) and IsBefore(15, 5, 2004) and not (rescuedtia or rescuedsabrina or rescuedwill)),
        "dark_class_x4" : (lambda: IsDate(24, 11, 2004)),
        "dragon_class_x1" : (lambda: IsDate(23, 4, 2004)),
        "dragon_class_x3" : (lambda: IsAfter(9, 5, 2004) and IsBefore(15, 5, 2004) and not (rescuedwill)),
        "dragon_class_x4" : (lambda: IsDate(12, 2, 2005)),
        "electric_class_x1" : (lambda: IsDate(23, 4, 2004)),
        "electric_class_x3" : (lambda: IsAfter(9, 5, 2004) and IsBefore(15, 5, 2004) and not (rescuedtia or rescuedsabrina or rescuedwill)),
        "electric_class_x4" : (lambda: IsDate(23, 12, 2004)),
        "fairy_class_x1" : (lambda: IsDate(23, 4, 2004)),
        "fairy_class_x3" : (lambda: IsAfter(9, 5, 2004) and IsBefore(15, 5, 2004) and not (rescuedtia or rescuedsabrina or rescuedwill)),
        "fairy_class_x4" : (lambda: IsDate(8, 10, 2004)),
        "fighting_class_x1" : (lambda: IsDate(23, 4, 2004)),
        "fighting_class_x3" : (lambda: IsAfter(9, 5, 2004) and IsBefore(15, 5, 2004) and not (rescuedtia or rescuedsabrina or rescuedwill)),
        "fighting_class_x4" : (lambda: IsDate(9, 8, 2004)),
        "fire_class_x1" : (lambda: IsDate(23, 4, 2004)),
        "fire_class_x3" : (lambda: IsAfter(9, 5, 2004) and IsBefore(15, 5, 2004) and not (rescuedtia or rescuedsabrina or rescuedwill)),
        "fire_class_x4" : (lambda: IsDate(10, 4, 2004)),
        "flying_class_x1" : (lambda: IsDate(23, 4, 2004)),
        "flying_class_x3" : (lambda: IsAfter(9, 5, 2004) and IsBefore(15, 5, 2004) and not (rescuedtia or rescuedsabrina or rescuedwill)),
        "flying_class_x4" : (lambda: IsDate(4, 10, 2004)),
        "ghost_class_x1" : (lambda: IsDate(23, 4, 2004)),
        "ghost_class_x3" : (lambda: IsAfter(9, 5, 2004) and IsBefore(15, 5, 2004) and not (rescuedsabrina or rescuedwill)),
        "ghost_class_x4" : (lambda: IsDate(31, 3, 2005)),
        "grass_class_x1" : (lambda: IsAfter(13, 6, 2004) and IsBefore(19, 6, 2004)),
        "grass_class_x2" : (lambda: IsDate(23, 4, 2004)),
        "grass_class_x4" : (lambda: IsAfter(9, 5, 2004) and IsBefore(15, 5, 2004) and not (rescuedtia or rescuedsabrina or rescuedwill)),
        "ground_class_x1" : (lambda: IsDate(23, 4, 2004)),
        "ground_class_x3" : (lambda: IsAfter(9, 5, 2004) and IsBefore(15, 5, 2004) and not (rescuedtia or rescuedsabrina or rescuedwill)),
        "ground_class_x4" : (lambda: IsDate(4, 5, 2004)),
        "ice_class_x1" : (lambda: IsDate(23, 4, 2004)),
        "ice_class_x3" : (lambda: IsAfter(9, 5, 2004) and IsBefore(15, 5, 2004) and not (rescuedtia or rescuedsabrina or rescuedwill)),
        "ice_class_x4" : (lambda: IsDate(8, 6, 2004)),
        "normal_class_26" : (lambda: IsAfter(31, 4, 2004) and IsAbsent("Cheren", "Normal")),
        "normal_class_35" : (lambda: IsPresent("Cheren", "Normal")),
        "normal_class_36" : (lambda: IsPresent("Cheren", "Normal")),
        "normal_class_39" : (lambda: IsPresent("Cheren", "Normal") and ClassSceneSeen("Normal", 36)),
        "normal_class_x1" : (lambda: IsDate(23, 4, 2004)),
        "normal_class_x3" : (lambda: IsAfter(9, 5, 2004) and IsBefore(15, 5, 2004) and not (rescuedtia or rescuedsabrina or rescuedwill)),
        "normal_class_x4" : (lambda: IsDate(21, 5, 2004)),
        "poison_class_x1" : (lambda: IsDate(23, 4, 2004)),
        "poison_class_x3" : (lambda: IsAfter(9, 5, 2004) and IsBefore(15, 5, 2004) and not (rescuedtia or rescuedsabrina or rescuedwill)),
        "poison_class_x4" : (lambda: IsDate(13, 9, 2004)),
        "psychic_class_x1" : (lambda: IsDate(23, 4, 2004)),
        "psychic_class_x2" : (lambda: IsDate(11, 11, 2004)),
        "rock_class_x1" : (lambda: IsDate(23, 4, 2004)),
        "rock_class_x3" : (lambda: IsAfter(9, 5, 2004) and IsBefore(15, 5, 2004) and not (rescuedsabrina or rescuedwill)),
        "rock_class_x4" : (lambda: IsDate(29, 1, 2005)),
        "steel_class_11" : (lambda: IsAfter(26, 4, 2004) and IsAbsent("Jasmine", "Steel")),
        "steel_class_x1" : (lambda: IsDate(23, 4, 2004)),
        "steel_class_x3" : (lambda: IsAfter(9, 5, 2004) and IsBefore(15, 5, 2004) and not (rescuedwill)),
        "steel_class_x4" : (lambda: IsDate(29, 10, 2004)),
        "water_class_x1" : (lambda: IsDate(23, 4, 2004)),
        "water_class_x3" : (lambda: IsAfter(9, 5, 2004) and IsBefore(15, 5, 2004) and not (rescuedtia or rescuedsabrina or rescuedwill)),
        "water_class_x4" : (lambda: IsDate(12, 7, 2004))
    }

    def ClassSceneSeen(classtype, number):
        classtype = classtype.lower()
        eventstring = classtype + "_class_" + ("0" if number < 10 else "") + str(number)
        return classtype in seenclasses.keys() and eventstring in seenclasses[classtype]

    def PassesConditions(eventstring):
        return (not ("class_x" in eventstring or eventstring in genericclasssceneconditionals)) or (eventstring in genericclasssceneconditionals and genericclasssceneconditionals[eventstring]())

    def FindGenericClassScene(evaluate = False):
        classsceneid = 1
        eventstring = location + "_class_x1"
        while (renpy.has_label(eventstring)):
            if ((location in seenclasses and eventstring in seenclasses[location]) or not PassesConditions(eventstring)):#if this particular scene has been seen already, or does not pass the conditionals...
                classsceneid += 1#increment the scene counter
                eventstring = location + "_class_x" + str(classsceneid)#set the new scene label to check for
                continue#skip the rest of this loop, going back up to the top of the "while" loop

            if (not evaluate):
                if (location in seenclasses.keys()):#if you've seen a generic scene for this class before, then...
                    seenclasses[location].append(eventstring)#append it to the pre-existing list
                else:#otherwise...
                    seenclasses[location] = [eventstring]#create a new list with this scene as the first event

            return eventstring#and return true, so the "generic-generic" scene doesn't show up.

        #location = bug/fire/water, etc. set at the beginning of each class. Global variable so not defined here.
        classsceneid = 1
        eventstring = location + "_class_01"
        
        while (renpy.has_label(eventstring)):#as long as you're looking at actual written scenes....
            if ((location in seenclasses and eventstring in seenclasses[location]) or not PassesConditions(eventstring)):#if this particular scene has been seen already, or does not pass the conditionals...
                classsceneid += 1#increment the scene counter
                eventstring = location + "_class_" + str(classsceneid).zfill(2)#set the new scene label to check for
                continue#skip the rest of this loop, going back up to the top of the "while" loop

            if (not evaluate):
                if (location in seenclasses.keys()):#if you've seen a generic scene for this class before, then...
                    seenclasses[location].append(eventstring)#append it to the pre-existing list
                else:#otherwise...
                    seenclasses[location] = [eventstring]#create a new list with this scene as the first event

            return eventstring#and return true, so the "generic-generic" scene doesn't show up.
    
        return False#if you hit this point, you've run out of generic scenes, just show the generic-generic one.