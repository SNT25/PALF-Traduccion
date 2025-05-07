label ethanevent:

if (IsAbsent("Ethan")):
    return

show ethan uniform with dis

if (not HasEvent("Ethan", "Serendipity1")):
    $ AddEvent("Ethan", "Serendipity1")
    red uniform @surprised  "Huh?! Ethan!"
    ethan @talkingmouth "Huh. Hey, [first_name]."
    red @happy "Good to see you! Crazy we both chose the same first elective, huh?"
    ethan @happy "Yeah, kinda wild."
    red @talkingmouth "This seat taken?"
    ethan @talkingmouth "Go ahead."

elif (not HasEvent("Ethan", "Serendipity2")):
    $ AddEvent("Ethan", "Serendipity2")
    red uniform @surprised "Huh. We're in the same class?"
    ethan @sadbrow talkingmouth "Looks like it. Small world?"
    red @happy "Smaller than I thought!"
    ethan @happy "Well, I'll never turn down more you. Wanna sit here?"
    red @talkingmouth "Don't mind if I do."

elif (not HasEvent("Ethan", "Serendipity3")):
    $ AddEvent("Ethan", "Serendipity3")

    show ethan surprisedbrow frownmouth with dis

    red uniform @surprised "We're... in the same class again."    
    ethan -surprisedbrow -frownmouth @closedbrow talking2mouth "Yeah... well, come on and sit here, I guess."
    red @confused "Sure."

elif (not HasEvent("Ethan", "Serendipity4")):
    $ AddEvent("Ethan", "Serendipity4")
    red uniform @talkingmouth "Hey, Ethan. Again."
    ethan @closedbrow talking2mouth "The odds of this are... so incredibly small, it's hard to describe."
    red @closedbrow talking2mouth "Yeah. But there's something going on here that beats the odds, obviously."

elif (not HasEvent("Ethan", "Serendipity5")):
    $ AddEvent("Ethan", "Serendipity5")
    red uniform @talkingmouth "Hey, Ethan."
    ethan @closedbrow talking2mouth "Let's, uh, let's just pretend there's nothing weird about this from now on."
    red @closedbrow talking2mouth  "Yeah, I don't want to go through this every day for the rest of the year."

else:
    $ renpy.call(GetEthanGenericScenes())

hide ethan with dis

return

default recentethanscenes = []

init python:
    ethangenericsceneconditions = {
        "EthanGeneric11" : (lambda: timeOfDay == "Evening"),
        "EthanGeneric10" : (lambda: timeOfDay == "Morning"),
        "EthanGeneric9" : (lambda: classstats[location.title()] > 4),
        "EthanGeneric4" : (lambda: classstats[location.title()] > 4),
        "EthanGeneric5" : (lambda: AimLevel() > 14)
    }

    def FulfillsConditions(scenename):
        return scenename not in ethangenericsceneconditions or ethangenericsceneconditions[scenename]()

    def GenerateSceneSet():
        ethanscenenames = set()
        tag = 1
        tagname = "EthanGeneric" + str(tag)
        while (renpy.has_label(tagname)):
            ethanscenenames.add(tagname)
            tag += 1
            tagname = "EthanGeneric" + str(tag)
        return ethanscenenames

    def GetEthanGenericScenes():
        sceneset = GenerateSceneSet()
        recents = set(recentethanscenes)
        ethanevent = RandomChoice(list(sceneset - recents))
        while (not FulfillsConditions(ethanevent) or ethanevent in recentethanscenes):
            ethanevent = RandomChoice(list(sceneset - recents))
        recentethanscenes.append(ethanevent)
        if (len(recentethanscenes) > 10):
            recentethanscenes.pop(0)
        return ethanevent

label EthanGeneric1:
    red happy uniform "Hey, Ethan!"
    ethan uniform happy "[first_name]! Good to see ya. Let's get this done!"
    return

label EthanGeneric2:
    show ethan tired with dis
    red surprised uniform "Woah, Ethan, you alright?"
    ethan uniform tiredhappy happy "What, do I look tired? Yeah, man, I'm fine!"
    return

label EthanGeneric3:
    red happy uniform "You look like you could use some coffee."
    ethan uniform happy "Nah, I'm good. Thanks, though!"
    red surprised "I mean... I don't actually have any on me..."
    return

label EthanGeneric4:
    ethan uniform sad "Crap, didn't we have a quiz today...? I'm so unprepared, man..."
    red uniform happy "Don't worry, you can borrow my notes."
    return

label EthanGeneric5:
    $ aimlevel = min(AimLevel(), GetHighestProficiency(0))
    ethan uniform @talkingmouth "I don't get why my Pichu hasn't evolved yet. I mean, look at her. She's level freakin' [aimlevel]!"
    red uniform sadbrow talkingmouth "Everyone goes at their own pace, you know?"
    return

label EthanGeneric6:
    $ classname = location.title()
    ethan @happy "Alright, time for [classname] class!"
    red uniform sadbrow talkingmouth "Gotta buckle down for this one."
    return

label EthanGeneric7:
    $ classname = location.title()
    ethan uniform @closedbrow talking2mouth "Okay, so, about Pokémon that are [classname]-Type..."
    red uniform @closedbrow talking2mouth 'You studying something new?'
    ethan @happy "I'm trying, man!"
    return

label EthanGeneric8:
    show ethan uniform downeyes with dis
    narrator "Ethan is sneakily playing on his Game Boy Advance... hope the teacher doesn't see!"
    return

label EthanGeneric9:
    ethan uniform @talking2mouth "Ugh, the homework for this class was {i}killer{/i}..."
    red uniform @talking2mouth "Tell me about it. Twenty pages of reading, {i}and{/i} a report?"

    show ethan surprisedbrow frownmouth with dis

    pause 1.0

    ethan @surprised "There was a report?"
    return 

label EthanGeneric10:
    red uniform @talking2mouth "You good last night? I thought I heard a scream."
    ethan uniform @closedbrow talking2mouth "Just watching old horror films on my phone. Ever seen 'Bonesaw'?"
    red @happy "Can't say I've had the pleasure."
    return

label EthanGeneric11:
    ethan uniform @closedbrow talking2mouth "Geez, this is one of those days that just goes {i}on{/i} and {i}on{/i}."
    red uniform @talkingmouth "You said it, bud."
    return

label EthanGeneric12:
    ethan uniform @closedbrow talking2mouth "Don't talk to me, man. I just got who I was rolling for one roll away before I'd have sparked pity."
    red uniform @confused "Those are... definitely words."
    return

label EthanGeneric13:
    ethan uniform @talkingmouth "How's [pika_name] doing?"
    red uniform @talking2mouth "Same old. I'm trying to teach him to play dead."
    ethan @talkingmouth "Any luck?"
    red @happy "I've got him to go to sleep on command!"
    return

label EthanGeneric14:
    ethan uniform @talkingmouth "I gotta be real with you, man. I think I should just tell the instructor a Growlithe ate my homework."
    red uniform @sadbrow talkingmouth "You're on your own with that one."
    return

label EthanGeneric15:
    ethan uniform @talkingmouth "I wonder what we'll learn today?"
    red uniform @talkingmouth "Gonna go out on a limb and say 'something about Pokémon.'"
    return

label EthanGeneric16:
    ethan uniform @closedbrow talking2mouth "You know, I actually tried to avoid going to this class. I followed you, saw where you were going, and went to a different elective."
    red uniform @confused "How'd you end up here?"
    ethan @sadbrow talkingmouth "Got lost."
    return

label EthanGeneric17:
    ethan uniform tired @talking2mouth "I stayed up too late last night raiding..."
    red uniform @closedbrow talking2mouth "Raiding? Are you a viking?"
    ethan @closedbrow talking2mouth "Nah, they mostly live in Minnesota."
    return

label EthanGeneric18:
    ethan uniform @talking2mouth "Our roommates: FMK. What do you think?"
    red uniform @surprised "I'm thinking I'm not touching that one with a ten-foot pole!"
    return

label EthanGeneric19:
    $ classname = location.title()
    ethan uniform @talking2mouth "Ugh, [classname] class..."
    red uniform @surprised "Do you not like it?"
    ethan @sadbrow talkingmouth "Nothing against this class, it's just that, right now, I'm considering running to Galar to be a Wooloo farmer and never opening a book again."
    return

label EthanGeneric20:
    ethan uniform @talkingmouth "Dude, can you believe some people still haven't memorized the type chart?"
    red uniform @surprised "Really? In {i}Kobukan{/i}?"
    ethan @talkingmouth "Feeling a bit better about {i}my{/i} chances now!"
    return