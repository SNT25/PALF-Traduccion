call PickElective() from _call_PickElective#this exists purely so the bug fixer has somewhere to go when it gets stuck.

label PickElective():

$ HealParty()
show blank2 as blackground with dis

if (excusesecondelective):
    narrator "You take advantage of your Excused Absence to skip your elective."
    jump freeroam

show map with dis
hide blank2
show blank2 with dis:
    alpha 0.8

stop music fadeout 1.5
$ renpy.music.stop(channel="crowd", fadeout=1.5)
$ renpy.music.queue("Audio/Music/ViridianCity_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/ViridianCity_Loop.ogg", channel='music', loop=True, tight=None)

label AfterMusic:

if (timeOfDay == "Morning"):
    $ lastclass = ""

call screen electives(_with_none=False) with dissolve
with dissolve
hide blackground
hide screen classmates with dissolve
if (_return not in starters.keys()):
    jump AfterMusic

narrator "¿Eliges la clase de tipo [type_translation[_return]]?"

menu:
    ">Ir a clase de tipo [type_translation[_return]].":
        python:
            classtype = _return
            jumpname = classtype.lower() + "elective"
            lastclass = classtype
            renpy.call(jumpname)

        $ PlaySound("BellChime.ogg", otherchannel="crowd")

        python:
            numstudents = len(GetStudents(classtype)) + 1
            for i, student in enumerate(GetStudents(classtype) | {"Ethan"}):
                renpy.hide(student.lower())
                xbuffer = (i + 1) / (numstudents + 1)
                
                renpy.show(GetCharacterSprite(student.lower(), classmood, True), [Flatten, Transform(xpos=xbuffer), dissolvein])

            renpy.pause(0.5)

            for i, student in enumerate(GetStudents(classtype) | {"Ethan"}):
                xbuffer = (i + 1) / (numstudents + 1)
                valueamount = 1
                if (student in ["Jasmine", "Grusha"]):
                    valueamount = 2
                ValueChange(student, valueamount, xbuffer, False)
            
            #PlaySound("PointsUp.ogg")

        hide blank2

        if (classmood < -6):
            narrator "Even in the hostile atmosphere, your classmates are able to band together..."
        elif (classmood < 0):
            narrator "Even though the mood is low, your classmates are able to band together..."
        else:
            narrator "Classmates' bonds increased!"

        python:
            if (not HasEvent("Professor Oak", classtype)):
                AddEvent("Professor Oak", classtype)
                IncreaseProficiency(classtype, 5)
            else:
                IncreaseProficiency(classtype, 1)
            classmood = 10

        label aftertutoring:

        if (IsAfter(9, 5, 2004) and IsBefore(17, 5, 2004) and timeOfDay == "Morning"):#Drayden forest is forbidden warning
            $ hideside = True

            narrator "As everyone prepares to leave, the intercom system in the classroom crackles to life."
            if (IsDate(10, 5, 2004)):
                drayden "Hello. This is Dean Drayden speaking. This is a reminder that all access to the forest is prohibited."
                drayden "Again, last week's announcement that the forest is open to students was made in error."
                drayden "The forest is {i}not{/i} open to anyone not engaged in Student Council or Disciplinary Committee business."
                drayden "We must regrettably enforce this rule with {i}extreme{/i} prejudice. Expulsion will be considered for any rule-breakers."
                drayden "This message will be repeated at the end of every morning elective."

            else:
                drayden "Hello. This is a reminder that all access to the forest is prohibited to students not engaged in official duties. Expulsion is a likely punishment for rule-breaking. This message will be repeated."

            pause 1.0

            $ hideside = False

        if (classtype in ["Water", "Ghost"] and coordinating):#coordinating knowledge going up for attending ghost/water class
            $ coordinatingknowledge += 3
            narrator "Your [contestcolor]Coordinating Knowledge{/color} went up by three!"

        if (classtype == "Steel" and GetRelationshipRank("Jasmine") == 1 and IsPresent("Jasmine", "Steel") and HasEvent("Jasmine", "Jasmine2Part1")):
            call Jasmine2Part2 from _call_Jasmine2Part2

        $ taughtmove = None

        if (timeOfDay == "Morning"):
            $ timeOfDay = "Noon"
        elif (timeOfDay == "Afternoon"):
            $ timeOfDay = "Evening"

        hide blank2
        show blank2 with dis

        $ renpy.transition(dissolve)
        call clearscreens from _call_clearscreens_1

        window hide
        stop music fadeout 1.0
        $ renpy.pause(1.0, hard=True)
        $ HealParty()

        if (timeOfDay == "Noon"):
            show noon at vspaz
        elif (timeOfDay == "Evening"):
            show evening at vspaz
            
        pause 3.5

        python:
            jumpto = "gym" if timeOfDay == "Noon" else "secondhomeroom"
            jumptoyear = "01"
            jumptomonth = ("0" if calDate.month < 10 else "") + str(calDate.month)
            jumptodate = ("0" if calDate.day < 10 else "") + str(calDate.day)
            labelname = jumpto + jumptoyear + jumptomonth + jumptodate
            if (timeOfDay == "Bugfix"):
                renpy.jump("day" + jumptoyear + jumptomonth + jumptodate)
            elif (renpy.has_label(labelname)):
                renpy.jump(labelname)
            else:
                renpy.jump("day" + jumptoyear + jumptomonth + jumptodate)

    ">Mejor me lo pienso bien.":
        jump AfterMusic

label endclass:#for skipping class if you elect for move tutoring instead
narrator "The class passes swiftly as you are tutored in a new move."

$ taughtmove = None
$ renpy.pop_call()
jump aftertutoring

label endclasscraft:# for skipping class if you elect for crafting instead
narrator "The class passes swiftly as you craft the item."

$ renpy.pop_call()
jump aftertutoring
