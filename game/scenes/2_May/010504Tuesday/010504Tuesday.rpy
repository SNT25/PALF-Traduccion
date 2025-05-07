label day010504:
$ timeOfDay = "Early Morning"

call calendar(1) from _call_calendar_29
$ calDate = calDate.replace(day=4, month=5, year=2004)

show earlymorning at vspaz

pause 3.5

stop music fadeout 1.5

queue music "audio/music/mansion_start.ogg" noloop
queue music "audio/music/mansion_loop.ogg"

python:
    HealParty()
    
    playercharacter = "Leaf"

    playerparty = GetTrainerTeam("Leaf")

    HealParty()

    inventory = {
        Item.PokeBall : 12,
        Item.GreatBall : 5,
        Item.Potion : 4,
        Item.ParalyzeHeal : 2,
        Item.BurnHeal : 7,
        Item.DragonFang : 1,
        Item.MiracleSeed : 1,
        Item.Magnet : 1,
        Item.Diary : 1,
        Item.Towel : 1,
        Item.RootFossil : 1,
        Item.AirHorn : 1,
        Item.ExperienceShare : 1
    }

    personalstats = {
        "Charm" : 43,
        "Knowledge" : 8,
        "Courage" : 4,
        "Wit" : 24,
        "Patience" : -3
    }

    knownclasses = []
    if (1 in oldpersondex["Instructor Ramos"]):
        knownclasses.append("Grass")
    if (1 in oldpersondex["Instructor Clair"]):
        knownclasses.append("Dragon")
    if (1 in oldpersondex["Lieutenant Surge"]):
        knownclasses.append("Electric")
    if (knownclasses == []):
        knownclasses.append("None")

    persondex = copy.deepcopy(defaultpersondex)
    persondex["Rosa"] = {"Named" : True, "Value" : 4002, "Contact": True, "Sex": Genders.Female, "Relationship": "Idolater", "RelationshipRank": 0, "Events": [] }
    persondex[first_name] = {"Named" : True, "Value" : oldpersondex["Leaf"]["Value"] * 3, "Contact": True, "Sex": Genders.Male, "Relationship": ("Pursuer" if "RejectedConfession" in oldpersondex["Leaf"]["Events"] else "Date"), "RelationshipRank": 0, "Events": [] }
    persondex["Leaf"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Female, "Relationship": "Self", "RelationshipRank": 0, "Events": [] }
    persondex["Blue"] = {"Named" : True, "Value" : 7, "Contact": True, "Sex": Genders.Male, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }
    persondex["Professor Oak"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [] }
    persondex["Professor Cherry"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [] }
    persondex["May"] = {"Named" : True, "Value" : 32, "Contact": True, "Sex": Genders.Female, "Relationship": "Dormmate", "RelationshipRank": 0, "Events": [] }
    persondex["Bianca"] = {"Named" : True, "Value" : 16, "Contact": True, "Sex": Genders.Female, "Relationship": "Dormmate", "RelationshipRank": 0, "Events": [] }
    persondex["Hilda"] = {"Named" : True, "Value" : 23, "Contact": True, "Sex": Genders.Female, "Relationship": "Dormmate", "RelationshipRank": 0, "Events": [] }
    persondex["Serena"] = {"Named" : True, "Value" : 28, "Contact": True, "Sex": Genders.Female, "Relationship": "Dormmate", "RelationshipRank": 0, "Events": [] }
    persondex["Ethan"] = {"Named" : True, "Value" : 2, "Contact": True, "Sex": Genders.Male, "Relationship": "Investigator", "RelationshipRank": 0, "Events": [] }
    persondex["Brendan"] = {"Named" : True, "Value" : 16, "Contact": True, "Sex": Genders.Male, "Relationship": "Friend", "RelationshipRank": 0, "Events": [] }
    persondex["Cheren"] = {"Named" : True, "Value" : 2, "Contact": True, "Sex": Genders.Male, "Relationship": "Hater", "RelationshipRank": 0, "Events": [] }
    persondex["Hilbert"] = {"Named" : True, "Value" : 11, "Contact": True, "Sex": Genders.Male, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [] }
    persondex["Calem"] = {"Named" : True, "Value" : 14, "Contact": True, "Sex": Genders.Male, "Relationship": "Friend", "RelationshipRank": 0, "Events": [] }
    persondex["Gardenia"] = {"Named" : True, "Value" : 19, "Contact": True, "Sex": Genders.Female, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [] }
    persondex["Whitney"] = {"Named" : True, "Value" : 22, "Contact": True, "Sex": Genders.Female, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [] }
    persondex["Flannery"] = {"Named" : True, "Value" : 18, "Contact": True, "Sex": Genders.Female, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [] }
    persondex["Nate"] = {"Named" : True, "Value" : 3, "Contact": True, "Sex": Genders.Male, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [] }
    persondex["Sonia"] = {"Named" : True, "Value" : 18, "Contact": True, "Sex": Genders.Female, "Relationship": "Underclassman", "RelationshipRank": 0, "Events": [] }
    persondex["Silver"] = {"Named" : True, "Value" : 14, "Contact": True, "Sex": Genders.Male, "Relationship": "Teammate", "RelationshipRank": 0, "Events": [] }
    persondex["Bea"] = {"Named" : True, "Value" : 5, "Contact": True, "Sex": Genders.Female, "Relationship": "Teammate", "RelationshipRank": 0, "Events": [] }
    persondex["Erika"] = {"Named" : True, "Value" : 2, "Contact": True, "Sex": Genders.Female, "Relationship": "Teammate", "RelationshipRank": 0, "Events": [] }
    persondex["Janine"] = {"Named" : True, "Value" : 18, "Contact": True, "Sex": Genders.Female, "Relationship": "Mentee", "RelationshipRank": 0, "Events": [] }
    persondex["Dawn"] = {"Named" : True, "Value" : 13, "Contact": True, "Sex": Genders.Female, "Relationship": "Teammate", "RelationshipRank": 0, "Events": [] }
    persondex["Tia"] = {"Named" : True, "Value" : 3, "Contact": True, "Sex": Genders.Female, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [] }
    persondex["Yellow"] = {"Named" : True, "Value" : 5, "Contact": True, "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [] }
    persondex["Instructor Ramos"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [] }
    persondex["Lieutenant Surge"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [] }
    persondex["Instructor Clair"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [] }
    persondex["Alder"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [] }
    persondex["Bruno"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [] }
    persondex["Lance"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Male, "Relationship": "Mentee", "RelationshipRank": 0, "Events": [] }
    
    classstats = { 
        "Normal" : 14,
        "Fire" : 1,
        "Water" : 0,
        "Grass" : 22,
        "Electric" : 21,
        "Ice" : 1,
        "Fighting" : 1,
        "Poison" : 1,
        "Ground" : 1,
        "Flying" : 1,
        "Psychic" : 1,
        "Bug" : 1,
        "Rock" : 1,
        "Ghost" : 1,
        "Dark" : 1,
        "Dragon" : 23,
        "Steel" : 1,
        "Fairy" : 1
    }

narrator "{color=#3110dd}You are no longer you.{/color}"

scene dorm_A
show screen currentdate
with transeye2

narrator "You wake up at the crack of dawn, a phenomenon you are altogether unfamiliar with. Ordinarily, it would take an airhorn next to your ear in order to get you out of bed before seven."
narrator "But, today, you are on a mission."

pause 1.0

narrator "You reach into your bag and pull out your weapon of mass (sleep) disruption."

pause 1.0

$ PlaySound("airhorn.ogg")

show dorm_A with vpunch

show hilda angrybrow frownmouth with Dissolve(0.5):
    xpos 0.2

show may sadbrow frownmouth with Dissolve(0.5):
    xpos 0.4

show serena sadbrow frownmouth with Dissolve(0.5):
    xpos 0.6

show bianca happy with Dissolve(0.5):
    xpos 0.8

hilda @angry "{i}What the fuck, Leaf?{/i} Why are you waking us up so goddamn early in the morning?"

leaf @talking2mouth "Listen up! I've got a mission for one of you, and I need to know which of you is {i}woman enough{/i} to do it!"

pause 1.0

hilda sadbrow @talkingmouth "I'm going back to bed."

hide hilda with dis

leaf @surprised "W-wait! Hilda, come back!"

show hilda frownmouth with dis:
    xpos 0.2

hilda @talkingmouth "{cps=20}What?{/cps}"

show hilda surprisedbrow
show may surprisedbrow
show serena surprisedbrow
show bianca surprisedbrow
with dis

leaf @talking2mouth "I need to know which one of you would be willing to miss the first Quarter Qlash to spend several hours flying across the ocean to rural Kanto to deliver a speech I wrote."

pause 1.0

leaf @talking2mouth "...Also, you'll be riding the back of a Dragon Pokémon going at about Mach 1."

pause 1.0

leaf @surprised "Oh, but, the Pokémon can put up a psychic barrier to protect you from wind resistance! It'll be like you're sitting in a room with completely still air."

show hilda angrybrow
show may angrybrow
show serena angrybrow
show bianca -surprisedbrow
with dis

leaf @embarrassedbrow talking2mouth blush "As... as long as you don't fall off."

pause 1.0

hilda @talkingmouth "What kind of joke is this, Leaf?"

leaf @talking2mouth "It's... it's not a joke."

hilda @talkingmouth "...Okay, so that's worse."

show serena behind may
show hilda behind may

show may:
    xpos 0.4
    ease 0.5 ypos 1.2 zoom 1.3

may @angrymouth "Leaf, you realize, right, that my boyfriend and I are figuring out if our relationship is even real right now?"

show bianca behind serena
show may behind serena
show serena:
    xpos 0.6
    ease 0.5 ypos 1.2 zoom 1.3

serena @angrymouth "Has it perhaps slipped your mind that I've yet to find a moment where I can reconcile with Calem? Do you not think I might have my own priorities?"

show may behind hilda
show hilda:
    xpos 0.2
    ease 0.5 ypos 1.2 zoom 1.3

hilda @sad "Yeah. I need to talk to Hilbert. He's... I heard some... well, look, it doesn't matter, alright? The fact you're even asking is ridiculous."

pause 1.0

leaf @sadbrow talking2mouth "Bianca?"

bianca @happy "Oh, I'd love to go! I just can't miss the first Quarter Qlash."
bianca @surprisedmouth "Participation is mandatory, you know. If you don't participate, unless you have a {i}really{/i} good excuse, then you can't graduate."

pause 1.0

leaf @surprised "What?"

bianca @happy "Yup! Sorry, Leaf."

leaf @sadbrow talking2mouth "Oh.{w=0.5} Oh, crap."

hilda @closedbrow talkingmouth "Yeah, I'm going back to bed."

hilda @angry "And if I see that damn air horn again, I'm flushing it down the toilet."

hide may
hide serena
hide hilda
with dis

pause 2.0

leafmind @closedbrow frownmouth "Finding someone else willing to do this is going to be harder than I thought."

call clearscreens from _call_clearscreens_95
scene blank2 with Dissolve(2.0)

stop music fadeout 1.5

queue music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show morning at vspaz

pause 3.5

$ timeOfDay = "Morning"

scene homeroom 
show whitney uniform frownmouth:
    xpos 0.8
show dawn uniform frownmouth:
    xpos 0.6
show hilbert uniform:
    xpos 0.4
show flannery uniform tiredbrow frownmouth:
    xpos 0.2
show screen currentdate
with splitfade

pause 1.5

show homeroom with vpunch

leaf uniform @surprised "What? {i}None{/i} of you?"

hilbert @closedbrow talkingmouth "I don't have time for this. You realize you're asking us to give up any chance of graduating to try and get a guy who was mind-controlling us, right?"

leaf @angrybrow talking2mouth "He {i}wasn't!{/i} All his power did was make you understand his feelings!"

hilbert @talkingmouth "It made me {i}trust{/i} him. Which I resent. Find a different pilot."

hide hilbert with dis

whitney sadbrow @talking2mouth "Sorry, Leaf. I've kinda got a few million other fires I need to put out right now..."

hide whitney with dis

flannery @tiredbrow talking2mouth "Yeah, no way. This isn't happening."

hide flannery with dis

show dawn:
    ease 5.0 xpos 0.8

pause 3.0

show dawn surprisedbrow frownmouth with dis

leaf @sadbrow happymouth "Dawn? You've flown on your Altaria before, right?"

dawn @talkingmouth "Uh... no thank you, sorry, you're welcome, no!"

show dawn:
    ease 0.3 xpos 1.2

pause 2.0

leafmind @sadbrow frownmouth "Crap."

pause 1.0

show blue uniform frownmouth at leftside with dis

blue @talkingmouth "About eight hours left. Guessing no-one's dumb enough to sign up for your suicide mission?"

leaf @talking2mouth "...It's not a suicide mission."

blue @closedbrow talkingmouth "It kinda is. Whoever goes won't be able to come back, right? So whoever goes is giving up their graduation."

leaf @talking2mouth "Yellow just said that Tia would go slower with two people, not that she couldn't do it. If she {i}really{/i} pushes herself, maybe she could make it in time?"

blue @angrybrow talkingmouth "Yeah, and maybe if you {i}really{/i} pushed yourself, you wouldn't be begging random classmates to go grab a guy an ocean away."

leaf @sadbrow talking2mouth "...I can't."

blue @talkingmouth "Yeah, well, as long as you're saying that, maybe you should just get used to the idea that that's all you're going to hear from everyone else."
blue @angrybrow talkingmouth "People have too much to lose to risk even more trying to get that dumbass to change his mind."

pause 1.0

leaf @angrybrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

pause 1.0

show blank

pause 0.1

hide blank

$ PlaySound("idea.ogg")

leaf @surprised "Wait, that's it!"

blue surprisedbrow frownmouth @surprised "Huh?"

leaf @talking2mouth "All I need to do is find someone with {i}nothing{/i} to lose!"

blue @surprisedbrow talkingmouth "I... guess that might work? But--"

leaf @angry "Ethan!"

$ PlaySound("whoosh.ogg")

blue @sad "Hey! Homeroom's starting in, like, five minutes!"

show blank2 with splitfadefast

narrator "You quickly dash through the hallways, at a speed greater than you'd ever comfortably ran, as you manically try to make it to Professor Cherry's homeroom before the first bell rings."

show blank with splitfadefast
scene newhomeroom with splitfadefast

queue music "audio/bigcrowdloop.ogg" channel "crowd" 

$ PlaySound("BellChime.ogg")

leaf uniform @surprised "Ethan!"

pause 1.0

show kris surprisedbrow frownmouth at leftside with dis

pause 2.0

kris -surprisedbrow -frownmouth -surprised @talkingmouth "Miss Green? Is there something I can help you with?"

leaf @sadbrow talking2mouth "Sorry. I was trying to get here before the bell. I just need a second. Is Ethan here?"

stop music channel "crowd" fadeout 1.5

show ethan uniform at rightside with dis

ethan @talking2mouth "Yo, Stem. Where's the fire?"

stop music fadeout 1.5

show kris surprisedbrow frownmouth
show ethan frownmouth
with dis

leaf @talking2mouth "It's Leaf. And I need to know if you can fly a Dragon Pokémon to Kanto to get [first_name] back here before the Quarter Qlashes."

pause 1.0

leaf @embarrassedbrow talking2mouth "{size=30}Also, you probably won't be able to fly back in time.{/size}"

ethan @sad2brow talking2mouth "No."

show kris -surprisedbrow -frownmouth -surprised angrymouth sadbrow with dis

leaf @surprisedbrow talking2mouth "...Wh-what?"

ethan angrybrow @talking2mouth "{i}No.{/i} I get what you're thinking. You're thinking I don't have anything to lose, right? That I can afford to skip the Quarter Qlashes and fly off to Kanto. Because I don't care enough to succeed, or whatever."

leaf @embarrassedbrow talking2mouth "...Yes?"

ethan -angrybrow @closedbrow talkingmouth "Well, you're wrong. It's a miracle that I'm here, but I'm not going to give up that miracle. I like [first_name]. A lot. But I'm not going to fly across an ocean for him."

pause 1.0

leaf @sadbrow talking2mouth "Can I bribe you?"

ethan @confusedeyebrows sad2eyes talking2mouth "...You got five billion on you?"

pause 1.0

leaf @talking2mouth "No."

ethan closedbrow talking2mouth "Sorry."

hide ethan with dis

pause 2.0

show kris:
    ease 0.5 xpos 0.5

leaf @sadbrow talking2mouth "Sorry for interrupting, Professor Cherry."

kris @talking2mouth "It's alright, Leaf. I can tell this was important. I might suggest going to your homeroom now, though. Professor Oak doesn't like when students are late for roll call."

leaf @closedbrow talking2mouth "Right..."

pause 1.0

narrator "For the first time since you burst into the classroom, you take a second to look around at the class."
narrator "It is {i}very notably{/i} less fancy than Professor Oak's classroom."

leafmind frownmouth "Hm... I guess Professor Oak's reputation got him the big room, then... Pretty sure no-one's heard of Professor Cherry."

kris @angrybrow talking2mouth "{size=30}Leaf.{/size}"

leaf @surprised "{size=30}Hm?{/size}"

kris @angrybrow talking2mouth "{size=30}I don't fully understand what you need to do here, but it sounds like you need someone with the time and ability to fly across the ocean before the Quarter Qlashes begin. Is that right?{/size}"

leaf @surprised "{size=30}Yes, that's right!{/size}"

kris @talking2mouth "{size=30}I assume you've already asked Skyla?{/size}"

leaf @sadbrow talking2mouth "{size=30}First person I went to...{/size}"

kris -sadbrow -angrymouth @happybrow talkingmouth "{size=30}That's alright.{/size}"
kris @closedbrow talking2mouth "{size=30}The faculty had an all-hands meeting on Sunday. It was mainly to address the events of Saturday. We were all there, and I remember Arnold telling us how the military would handle things like this back when he was a pilot."

leaf @sarcastic "{size=30}Uh... Arnold?{/size}"

kris @talkingmouth "{size=30}Oh, Surge. Arnold Surge.{/size}"

leaf @surprised "{size=30}Wait. Instructor Lieutenant Surge's first name is {i}Arnold?!{/i}{/size}"

kris @closedbrow talking2mouth "{size=30}Is that really the important part of what I just said?{/size}"

leaf @sarcastic "{size=30}No, but it's a helluva thing to learn.{/size}"

kris @talking2mouth "{size=30}Well, I hope that information helps you, at least a little.{/size}"
kris @happy "Now, I need to get back to my class... and you do too, I think."

pause 1.0

show kris angrybrow angrymouth with dis

leaf @embarrassedbrow talking2mouth "Um... could you write a note to Professor Oak explaining why I'm late for homeroom? And maybe, like, give him a better reason?"

pause 1.0

kris @talking2mouth "Fine. But that's your one for the semester."

leaf @embarrassedbrow happymouth "Thanks!"

scene blank2 with splitfadefast

narrator "You rush back to Professor Oak's class, note in hand, which he accepts good-naturedly. You're barely able to pay attention to the lesson, jumping out of your seat at the end of homeroom the exact moment the bell rings."

show classroom with dis

show elecclass with dis:
    xalign 0.5 yalign 1.0
show classlights:
    alpha 0.0 xalign 0.5 yalign 1.0
    parallel:
        pause 0.65
        ease 0.25 alpha 0.75
        pause 0.2
        ease 0.25 alpha 0.25
        pause 0.5
        ease 0.25 alpha 0.5
        pause 0.5
        ease 0.25 alpha 0.2
        pause 0.7
        ease 0.25 alpha 0.75
        pause 0.65
        ease 0.25 alpha 0.25
        repeat
show zap_A as zap1A:
    xpos 520 yalign 0 alpha 0.75
    parallel:
        pause 0.15
        ease 0.0 xpos 540 yalign 0 rotate 90
        pause 0.15
        ease 0.0 xpos 500 yalign 0 rotate 270
        pause 0.15
        ease 0.0 xpos 520 yalign 0 rotate 0
        repeat
    parallel:
        pause 0.1
        ease 0.0 alpha 0.75
        pause 0.2
        ease 0.0 alpha 0.0
        pause 0.1
        ease 0.0 alpha 0.75
        pause 0.1
        ease 0.0 alpha 0.0
        pause 0.2
        ease 0.0 alpha 0.75
        pause 0.1
        ease 0.0 alpha 0.0
        repeat
show zap_A as zap2A:
    xpos 690 yalign 0.23 alpha 0.75 zoom 0.66
    parallel:
        pause 0.12
        ease 0.0 xpos 710 yalign 0.23 rotate 94
        pause 0.16
        ease 0.0 xpos 670 yalign 0.23 rotate 265
        pause 0.14
        ease 0.0 xpos 690 yalign 0.23 rotate 5
        repeat
    parallel:
        pause 0.1
        ease 0.0 alpha 0.0
        pause 0.2
        ease 0.0 alpha 0.75
        pause 0.1
        ease 0.0 alpha 0.0
        pause 0.1
        ease 0.0 alpha 0.75
        pause 0.2
        ease 0.0 alpha 0.0
        pause 0.1
        ease 0.0 alpha 0.75
        repeat
show zap_A as zap3A:
    xpos 810 yalign 0.35 alpha 0.75 zoom 0.33
    parallel:
        ease 0.0 xpos 830 yalign 0.35 rotate 0
        pause 0.13
        ease 0.0 xpos 790 yalign 0.35 rotate 250
        pause 0.13
        ease 0.0 xpos 810 yalign 0.35 rotate 80
        pause 0.13
        repeat
    parallel:
        pause 0.1
        ease 0.0 alpha 0.75
        pause 0.2
        ease 0.0 alpha 0.0
        pause 0.1
        ease 0.0 alpha 0.75
        pause 0.1
        ease 0.0 alpha 0.0
        pause 0.2
        ease 0.0 alpha 0.75
        pause 0.1
        ease 0.0 alpha 0.0
        repeat
show zap_B as zap1B:
    xpos 1180 yalign 0 alpha 0.75
    parallel:
        pause 0.16
        ease 0.0 xpos 1200 yalign 0 rotate 45
        pause 0.2
        ease 0.0 xpos 1160 yalign 0 rotate 180
        pause 0.13
        ease 0.0 xpos 1180 yalign 0 rotate 90
        repeat
    parallel:
        pause 0.1
        ease 0.0 alpha 0.0
        pause 0.2
        ease 0.0 alpha 0.75
        pause 0.1
        ease 0.0 alpha 0.0
        pause 0.1
        ease 0.0 alpha 0.75
        pause 0.2
        ease 0.0 alpha 0.0
        pause 0.1
        ease 0.0 alpha 0.75
        repeat
show zap_B as zap2B:
    xpos 1080 yalign 0.23 alpha 0.75 zoom 0.66
    parallel:
        pause 0.12
        ease 0.0 xpos 1100 yalign 0.23 rotate 100
        pause 0.14
        ease 0.0 xpos 1060 yalign 0.23 rotate 250
        pause 0.12
        ease 0.0 xpos 1080 yalign 0.23 rotate 10
        repeat
    parallel:
        pause 0.1
        ease 0.0 alpha 0.75
        pause 0.2
        ease 0.0 alpha 0.0
        pause 0.1
        ease 0.0 alpha 0.75
        pause 0.1
        ease 0.0 alpha 0.0
        pause 0.2
        ease 0.0 alpha 0.75
        pause 0.1
        ease 0.0 alpha 0.0
        repeat
show zap_B as zap3B:
    xpos 1040 yalign 0.35 alpha 0.75 zoom 0.33
    parallel:
        ease 0.0 xpos 1060 yalign 0.35 rotate 90
        pause 0.15
        ease 0.0 xpos 1020 yalign 0.35 rotate 270
        pause 0.15
        ease 0.0 xpos 1040 yalign 0.35 rotate 0
        pause 0.15
        repeat
    parallel:
        pause 0.1
        ease 0.0 alpha 0.0
        pause 0.2
        ease 0.0 alpha 0.75
        pause 0.1
        ease 0.0 alpha 0.0
        pause 0.1
        ease 0.0 alpha 0.75
        pause 0.2
        ease 0.0 alpha 0.0
        pause 0.1
        ease 0.0 alpha 0.75
        repeat
with splitfadefast

stop music fadeout 1.5
queue music "Audio/Music/Vermillion_Start.ogg" noloop
queue music "Audio/Music/Vermillion_Loop.ogg"

pause 1.0

show surge with dis

surge @talkingmouth "Alright, ladies! You better get your asses IN those SEATS before I--"

surge surprisedbrow frownmouth @surprised "Wait, it's not class yet. You've got five more minutes."

show elecclass with vpunch

surge @angry "Private Green! What the HELL are you doing in this class so EARLY!?"

show surge surprisedbrow frownmouth with dis

leaf uniform @talkingmouth "I need to talk to you about your military experience, Sir."

pause 1.0

surge -surprisedbrow -frownmouth -surprised @happy "Well, isn't that SOMETHING! We might make a SOLDIER out of you YET, Private Green!"

leaf @embarrassedbrow happymouth "{size=30}Er... not sure that's what I'm going for...{/size}"

surge @happy "Well, fine, fine! What is it you're looking to hear about, Private? I can tell you about the war!" 
surge @happy "My Pokémon shocked my enemies into paralysis, I'll have you know! Once they were paralyzed, I could Headbutt them all day, and they wouldn't have a chance to move!"

leaf @talkingmouth "Yes, I've heard you tell those stories before. But I'm actually asking about your time as a pilot."

surge @surprised "Eh?"

leaf @sadbrow talking2mouth "I know you were in the Army, which I didn't think had pilots, but... someone told me that you were a pilot... and I was just holding out hope that that was true?"

surge @sad "...Yeah, the Army's got pilots."

surge @happy "Not as many as the Air Force, OF COURSE, but we've got a FEW!"

surge @talkingmouth "And I tell you what, the ARMY probably flies on more missions than the AIR FORCE! They're just paid to sit around on their asses in FANCY HOTEL ROOMS all the time! That's why we call them the CHAIR FORCE."

leaf @talking2mouth "Right, Sir. We all know how you feel about the Air Force. But I really need to hear about {i}your{/i} time as a pilot."

surge frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

surge @closedbrow talkingmouth "I flew a couple missions during the war, yeah. Our Pokémon on the frontlines were getting battered, and needed a resupply, asap."
surge @angrymouth "The pilot of my squadron had already been taken prisoner after losing his battles. No-one else in the squad could do it."
surge @angry "So I got my Raichu to fill my plane with 10,000 volts and jump-started that sucker, flying it back to base!"
surge @happy "Heh. Those punks never saw it coming. They thought they only had a few more Pokémon to beat, and then they'd have won the battle." 
surge @talkingmouth "I came back with enough Revives to choke a Wailord, and they practically gave up right there and then!"

leaf @happy "That's fantastic! Do you still have your plane?"

surge @surprised "What? 'Course not. You don't just keep your equipment when you leave the Army, Private."

leaf @surprised ".{w=0.5}.{w=0.5}.{w=0.5}Oh."

pause 2.0

leaf @sadbrow talking2mouth "Do you... do you have any interest in flying to Kanto? On a dragon Pokémon? To grab a runaway student?"

pause 1.0

python:
    title = " "
    if (4.1 in oldpersondex["Lieutenant Surge"]["Events"]):
        title = " Second Class "

surge @sadmouth "You're talking about Private[title][last_name]?"

leaf @surprised "You know?"

surge @talkingmouth "It makes sense. If I went through what that kid's gone through, I might go AWOL too."

leaf @happy "So you understand! That's great! So you'll fly to Kanto?"

surge @sadbrow talking2mouth "No can do, Private."

leaf @sadbrow surprisedmouth "What?"

surge @talkingmouth "Three reasons. First, I've got to teach classes for the rest of this week."
surge @sadbrow talkingmouth "Secondly, I'm pretty sure what you're asking me to do is some form of kidnapping or stalking."
surge @talkingmouth "Thirdly, I joined the Army specifically so I could keep my feet on the ground. I hate flying, and I do my best to avoid it whenever I can."

leaf @surprised "What?"

surge @happy "Why do you think I train ELECTRIC-TYPES, Private?! If it's in the air, I want it {i}out{/i} of my face!"

leaf @surprised "But... you flew anyway!"

surge @sad "Yeah. But I had to. If I hadn't, my brothers-in-arms would've been taken prisoner, and who knows how long it'd be before they could come back home?"

leaf @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

show surge:
    ease 0.5 ypos 1.2 zoom 1.3

surge @sadmouth "There's something my old XO used to tell me." 
surge @closedbrow happymouth "I was facedown in the mud, it was raining like hell, and lightning was cracking down all around us." 
surge @happy "I'd just done forty consecutive pushups, and he was screaming at the top of his lungs to give him another twenty. That's when I made the mistake of telling him something real dumb."
surge @talkingmouth "Any guesses as to what I said, Private?"

leaf @sadbrow talking2mouth "Um... 'No?'"

surge @happy "Hell, Private, I told you I said something dumb, not suicidal!"
surge @talkingmouth "Nah, I didn't say anything like that. I said 'I can't.'"

pause 1.0

surge @talkingmouth "That's when my XO knelt down there in the mud with me, and, for the first time since I met the bastard, stopped screaming. And he said, barely above a whisper, '{cps=10}It don't matter if you can't. {i}Because you have to.{/i}{/cps}'"

pause 1.0

show surge:
    ease 0.5 ypos 1.0 zoom 1.0

surge @happy "Then that bastard stomped in the mud, splashed it over my face, and told me to do another twenty for getting his boots dirty!"

leaf @sad "Uh... that sounds like hazing."

surge @closedbrow talkingmouth "Maybe it was. But it taught me something real important, that I took with me onto the battlefield."
surge @talkingmouth "Private Green, it's amazing what you can do when you have no choice."

pause 1.0

leaf @sadbrow sadmouth "But... maybe I do still have a choice?"

surge @closedbrow talkingmouth "Get serious, Private. You really think there's anyone in the school who you're going to convince to fly across an ocean to pick up a guy you like?"

leafmind @angrybrow frownmouth "Does {i}everyone{/i} know about that?"

surge @talkingmouth "If you want this done, you're going to have to do it yourself."

leaf @sadbrow sadmouth "But... {w=0.5}{size=30}I'm scared...{/size}"

surge @talkingmouth "I know what it's like to be afraid of flying, Private. But if you--"

show surge surprisedbrow frownmouth with dis

leaf @surprised "Oh! Um, I'm not actually afraid of flying. I'm afraid of... well, the water."

surge @talkingmouth "What?"

show elecclass with vpunch 

surge angry "WHAT?!"

surge @anger "Water?! {i}WATER?!{/i} What sort of candy-ass sorry excuse for a fear is that?! Flying's terrifying, but you're scared of {i}water{/i}?!"

leaf @angry "Hey! Water's totally terrifying!"

surge biganger @talkingmouth "No it goddamn isn't! When you're in the sky, you're just a thin piece of metal away from plummeting thousands of feet! What are you going to bump into in the water? A lilypad? A Ducklett? You can swim, can't you?"

leaf @angry "Maybe? I don't know!"

surge @angry "Then get your hydrophobic ass down to the recreation center right now and find out!"

leaf @angry "This is {i}not{/i} how you're supposed to deal with fears! And--"
leaf @surprised "Wait, now?"

surge @talkingmouth "Do you have time to wait around for the end of the school day? You've got ten hours left before you need to fly, don't you?!"
surge @angry "Get busy swimming, or get busy figuring out what you're going to tell your squadmates when you come back without a pilot!"

leaf @angry "W-well... fine, then! I will! I'll go to the recreation center right now, then!"

surge @talkingmouth "You better! And I'll be telling your other professors you'll be out {i}all{/i} day, so don't you come back unless you've completed your mission!"

leaf @angry "F-fine! I will! I'm going!"

pause 1.0

leaf @sadbrow happymouth "Are you sure--"

show elecclass with vpunch

surge angry "GET OUT!"

scene blank2 with splitfadefast

pause 1.0

narrator "Before you can think about what you're doing, you dash to the recreation center, throwing wide the door."

pause 0.1

scene pool with splitfadefast

leafmind uniform @angrybrow happymouth "There! See? It's just a pool! I can totally--"

stop music fadeout 2.0

show pool:
    align (0.5, 0.5) matrixcolor SaturationMatrix(1.0) rotate 0 zoom 1.0
    ease 10.0 matrixcolor SaturationMatrix(0.0) rotate 3 zoom 1.1

pause 2.0
    
leafmind @sad "I... I can totally..."

show flashsick as flashsick1 with dis:
    xalign 0.5 yalign 0.5
    block:
        ease 10.0 rotate 360
        ease 10.0 rotate 0
        repeat

show flashsick as flashsick2 with dis:
    xalign 0.5 yalign 0.5 rotate 90
    block:
        ease 7.0 rotate 360
        ease 7.0 rotate 0
        repeat

show flashsick as flashsick3 with dis:
    xalign 0.5 yalign 0.5 rotate 180
    block:
        ease 13.0 rotate 360
        ease 13.0 rotate 0
        repeat

pause 2.0

leafmind @sadbrow frownmouth "I'm going to throw up."

call clearscreens from _call_clearscreens_96
show blank2 with transeye

leafmind @closedbrow frownmouth "Just... just close your eyes. Pretend it's not there."

pause 1.0

leafmind @angrybrow frownmouth "You're being ridiculous, Leaf! It's {i}just{/i} water! It's not even saltwater! And the last time you tried to swim, you were completely fine!"

pause 1.0

leafmind "So open your eyes, and just... just dip a toe in. Just do it, okay?"

hide blank2 with transeye2

pause 1.0

show blank2 with transeye

leaf @sadbrow talking2mouth "Yup. That's not happening. Not today. Not ever. Never."

pause 1.0

narrator "You stand there for what feels like hours, but must really only be minutes. All you can hear is the pounding of your heart as you attempt to take even one step closer to the pool."

leafmind @angry "You.{w=0.5} Are.{w=0.5} Being.{w=0.5} Ridiculous!"

pause 1.0

narrator "Knowledge, however, does not correlate to action."

pause 1.0

show brock frownmouth behind blank2 

hide flashsick1
hide flashsick2
hide flashsick3

show pool:
    align (0.5, 0.5) matrixcolor SaturationMatrix(1.0) rotate 0 zoom 1.0

brock @talkingmouth "So, like, are you going to get in the pool or just kinda space out...?"

hide blank2 
show screen currentdate
with transeye2

show screen songsplash("Pewter City", "TeruTeruSky")
stop music fadeout 1.5
queue music "audio/music/pewter_start.ogg" noloop
queue music "audio/music/pewter_loop.ogg"

$ BecomeNamed("Brock")

brock @happymouth "Hey. Brock's the name. What's yours, Li'l Sis?"

leaf @sadbrow talking2mouth "Um, Leaf. Sorry, who are you?"

brock @happymouth "Oh, I'm a man of many names. Many faces. Some have called me the vagabond of love. Others call me that 'no-good hobo who needs to get a real job.'"

leaf @surprised "Huh?"

brock -frownmouth @talkingmouth "Jokes on them, I've got a real job! I've got a half-dozen real jobs. I'm just... in-between stages of my career at the moment."
brock @angrybrow talkingmouth "I prefer not to give myself too many labels. But for you, Li'l Sis, you can call me...{w=0.5} a missed connection."

pause 1.0

leaf @sarcastic "How old are you? Twenty? Twenty-five? I need to know how old you are before I decide to either blow you off with some mild sarcasm or call the cops."

brock frownmouth @sad2brow surprisedmouth "Ooh. You cut me to the bone, Li'l Sis."

leaf @talking2mouth "It's Leaf."

brock -frownmouth @talkingmouth "Leaf? Righteous. Some of my favorite plants are leaves."

leaf @talking2mouth "Yeah, I kinda got that impression."
leaf @closedbrow talking2mouth "Anyway, I need to go find a pilot for a thing, so if you could just, like, let me leave..."

brock @happymouth "Hey, Leaf, you're the one who's blocking the doorway. I tried to sneak out around you, but you were standing here, rock-solid, like a statue."

leaf @closedbrow talking2mouth "Oh. Right. Well..."

narrator "You shift awkwardly to the side."

leaf @closedbrow talking2mouth "Here."

brock @talkingmouth "Much obliged, Missy. Though I seem to have forgotten my way off the campus grounds."
brock @happy "Perhaps you'd be a gentleman and escort me?"

leaf @sarcastic "Uh-huh. I'm not going anywhere alone with you."

show brock frownmouth with dis

pause 1.0

brock @talkingmouth "Leaf, I hate to point out the obvious, but we're already completely alone here. And based on how you were shivering at that water, this is a place with serious bad juju for you, no?"

leaf @talking2mouth "Oh, so you were being a gentleman in trying to get me out of here, then?"

brock -frownmouth @happy "Now you get it, Li'l Sis!"

pause 1.0

leaf @talking2mouth "Why are you calling me Li'l Sis?"

brock @talkingmouth "Force of habit, {i}mi amiga.{/i} I grew up with nine siblings in inner-city Pewter. Pretty much everyone I talked to was a sibling, heh heh!"

show brock sad2brow frownmouth with dis

leaf @surprised "Wait, you grew up in Pewter City? I lived in Cinnabar!"

brock @talkingmouth "Cinnabar, no cap? No wonder, then."
brock @sadmouth "I heard that the evacuation efforts took days for some people. Were you...?"

pause 1.0

leaf @sadbrow talking2mouth "Yeah."

brock -frownmouth @talkingmouth "{w=0.5}.{w=0.5}.{w=0.5}.Well, let me give you some straight-shooting, then."
brock @happy "This water? Nothing to worry about! Heck, I'm a Rock-type specialist, and I wouldn't think twice about sending my Pokémon out to fight here!"
brock @happymouth "See this? Clean, chlorinated, safe. Deepest it goes? Nine feet. Besides, I'm a champion swimmer. In fact, I was even certified as a lifeguard at the Cerulean City Gym."

leaf @talking2mouth "Huh, and here I was thinking you were just a creepy old guy hanging around the pool to see girls in their swimsuits."

brock @talkingmouth "{w=0.5}.{w=0.5}.{w=0.5}.Well, I mean, I became a lifeguard for a reason."

leaf @sarcastic "Of course."

brock @heavyblush happymouth "You ever see the Cerulean Gym Leaders? Daisy, Violet, and Lily? Three of them. And they wear their swimsuits {i}all the time.{/i} Even during battles, man. You had to be there."

leaf @talking2mouth "Uh-huh. And I bet when someone nearly drowned because you were too busy ogling the Gym Leaders, you were more than happy to provide mouth-to-mouth."

brock @surprisedbrow talkingmouth "Oh, no, you aren't supposed to do that for CPR anymore. Chest compressions only. Turns out mouth-to-mouth breaks up the rhythm."

pause 1.0

leaf @talking2mouth "Oh."

brock @happymouth "Anyway, no-one ever drowned on my watch. Heh." 
brock surprisedbrow @talkingmouth "Although I had to swim out and rescue a few babes that seemed like they were really good swimmers..."
brock frownmouth @talkingmouth "And then {i}they{/i} would ask for mouth-to-mouth, even though they were conscious, and didn't need it..."

pause 1.0

brock @talkingmouth "Hm. Kinda think I might be realizing something."

leaf @sarcastic "Yeah, can you do that on your own time? I appreciate getting to be part of this moment of self-awareness or whatever, but there's a bit of a difference between this pool, and the water I'm going to need to go into."

brock -surprisedbrow -frownmouth @talkingmouth "Oh, yeah? How much difference?"

show brock surprisedbrow with dis

leaf @sarcastic "About 700 trillion gallons' difference."

pause 1.0

brock -surprisedbrow @surprisedbrow talkingmouth "That's a bit of a difference.{w=0.5} What're you planning to do, swim across the ocean?"

leaf @sadbrow talking2mouth "No, just fly over... but I'll be on a Pokémon."

pause 1.0

brock @happy "What've you got to worry about, then?"

leaf @surprised "Huh?"

brock @talkingmouth "Pokémon have got your back. If a Pokémon thinks it can't do something, it won't try. And they always underestimate their abilities."
brock @happymouth "See what I mean? They play it safe. That's why we trainers exist, to push them to their limit."
brock @talkingmouth "So if the Pokémon even gets off the ground, you know you're good."

leaf @surprised "But... but..."
leaf @angry "The water!"

brock @happymouth "What about the water, Li'l Sis? You're not touching it. You're not even going to be anywhere near it."
brock @talkingmouth "Now, if you want to run back to your dorm and grab a swimsuit, I'll be the last guy to stop you. But I don't think you even need to consider the water as a factor."
brock @happy "After all, if you fall off a Pokémon at a height of anything more than, like, 50 feet, you're probably not going to hit the water slowly enough to worry about the whole 'swimming' part of it."

leaf @angrybrow angrymouth "{w=0.5}.{w=0.5}.{w=0.5}."
leaf @angry "Was that meant to help me?"

brock @frownmouth "Hm."
brock @talkingmouth "Kinda, yeah."

leaf @talking2mouth "Maybe you should stick to lifeguarding. You're not much of a motivational speaker."

brock shadow sadbrow frownmouth @talkingmouth "No, I guess not."

pause 2.0

leaf @sadbrow talking2mouth "I guess you aren't secretly a pilot with a lot of free time on your hands?"

brock -shadow -sadbrow @talkingmouth "'Fraid not, Li'l Sis. I fly on my Pokémon once in a while, but nothing more than that."

leaf @sad "Yeah, I figured."

pause 1.0

brock @talkingmouth "He's a lucky guy."

leaf @sarcastic "What?"

brock @talkingmouth "You're in love, Li'l Sis. I can tell. Nothing else would make a nice girl like you try to fly across an ocean, while terrified of water. Where is he?"

leafmind @angrybrow frownmouth "...I'm annoyed that he guessed it so easily."

leaf @closedbrow talking2mouth "It's not love. He's a good friend."

if ("AcceptedConfession" in oldpersondex["Leaf"]["Events"]):
    leaf @closedbrow blush talking2mouth "And he owes me a date."
else:
    leaf @talking2mouth "He made it pretty clear that's where it ended."

brock -frownmouth @happymouth "Doesn't change anything from where I'm standing. He's a lucky guy, to have a friend like you."

brock @happymouth "Man, back in the day, I did some {i}real{/i} dumb stuff for the girls I liked."

brock @talkingmouth "Heh. So, I told you about how I became a licensed lifeguard so I could work at the Cerulean gym, right?"
brock @happymouth "Then I decided to become a Pokémon Breeder because there was a girl I was traveling with that collected baby Pokémon like they were magnets."
brock @talkingmouth "Then I became a doctor because there was a really adorable nurse I had a bit of a thing for."
brock @angrybrow sadmouth "...And I tried to become a police officer because there was a cute Jenny who'd arrested me a few weeks earlier, but I failed the dr-- uh, the entrance exam."
brock @talkingmouth "Then a few weeks after that I learned how to sing, and actually sold a couple albums... but it turns out she didn't really like country..."
brock sadbrow frownmouth @talkingmouth "And then my last job was pretty much to try and impress a girl as well. Turned out she was more into contests than battling, though."

pause 2.0

leaf @surprised "Wow. I thought this story was going to end, but it {i}just kept going.{/i}"

brock -sadbrow -frownmouth @happymouth "Yeah, I guess you could say I'm pretty worldly."

leaf @sarcastic "{size=30}That's one word for it.{/size}"

brock @talkingmouth "Anyway, the point of all that is that people do dumb stuff for the people they love."

leaf @angry "I--"

brock @angrybrow talkingmouth "Or the people they're 'into', whatever."
brock @talkingmouth "My goal has always been love. But on the way I learned to love the journey. So, see? Even though my efforts have been marked by failure and despair at every heartwrenching turn, I still achieved my goal."
brock @happy "And if a guy like me can do it, so can you!"

leaf @frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
leaf @closedbrow talking2mouth "Fuck it."
leaf @talking2mouth "Fine. Somehow, {i}somehow{/i}, you've convinced me. Mainly the part about the water not even being a factor, but hearing about your screw-ups made me feel a bit better as well, so... thanks."

brock eyesneutralbrow heavyblush happymouth "The thanks of a beautiful woman are all I need, Li'l Sis."

pause 2.0

leaf @surprised "Um..."

leaf @surprised "I'm.{w=1.0} I'm going."

call clearscreens from _call_clearscreens_97
scene blank2 with splitfadefast

pause 1.0

$ PlaySound("pokemon/ball sound.ogg")
$ PlaySound("pokemon/cries/142.mp3")

pause 1.0

brock @talkingmouth "Cinnabar, huh? Guess it's still having its effect on people, all these years later..."

$ PlaySound("pokemon/cries/142.mp3")

pause 1.0

brock @happymouth "Maybe we should stick around a bit longer. This school could do with a Cooking Club, couldn't it?"

pause 1.0

show noon at vspaz
$ timeOfDay = "Noon"

pause 3.5

stop music fadeout 1.5
queue music "Audio/Music/Route 1 Anime.ogg"

show screen currentdate
scene cafe 
with splitfade

show blue uniform frownmouth at leftside
show misty uniform at rightside

blue @talkingmouth "{size=20}...and{/size} {size=25}then{/size} {size=30}that{/size} {i}idiot{/i} said that his stupid fatass Pikachu was going to beat me next time."

misty @talkingmouth "Uh-huh."

pause 1.0

misty @closedbrow talkingmouth "...Did he?"

blue @angry "Well, duh, but that's because he had type advantage! I still won {i}most{/i} of the time!"

show blue surprisedbrow frownmouth 
show misty surprisedbrow frownmouth
with dis

leaf uniform @sarcastic "Still whining about [first_name], huh, [blue_name]?"

blue -surprisedbrow -frownmouth -surprised frownmouth @closedbrow talkingmouth "Tch. What's it to you?"

leaf @sarcastic "I just thought you would've been a bit more careful about that after what happened last time."

blue @sad "Hey, wait--"

leaf @angrybrow talking2mouth "It doesn't matter. We need to talk."

blue surprisedbrow frownmouth @surprised "Huh?"

hide blue
hide misty
show yellow angrybrow frownmouth uniformhat
with splitfadefast

leaf @talking2mouth "We can make this work. But I'm going to need your help."

hide yellow
show tia angrybrow frownmouth uniform hat
with splitfadefast

leaf @talking2mouth "I'm going to be the pilot. But we need to leave during lunch. {i}Now.{/i}"

hide tia
show ethan confusedeyebrows playfuleyes frownmouth uniform
with splitfadefast

leaf @talking2mouth "And I've got a plan to get myself, and [first_name], back."

pause 1.0

ethan @talking2mouth "Uh... I feel like I'm missing some context."

leaf @sarcastic "Just come out with me to the garden."

scene blank2 with splitfade

pause 1.0

scene clouds
show garden:
    xalign 0.5 yalign 0.5
show blue uniform frownmouth:
    xpos 0.8
show yellow uniformhat frownmouth:
    xpos 0.6
show tia uniform hat frownmouth:
    xpos 0.4
show ethan uniform frownmouth:
    xpos 0.2
show screen currentdate
with splitfade

pause 2.0

stop music fadeout 1.5
queue music "audio/music/mansion_start.ogg" noloop
queue music "audio/music/mansion_loop.ogg"

leaf uniform @talking2mouth "Normally, I'd say something like 'so, you're probably wondering why I've gathered you here today', but we don't have time for jokes like that. We need to do one thing, and one thing only."

leaf @talkingmouth "I'm proud to announce the inaugural meeting of the [first_name] Rescue Team!"

pause 1.0

ethan @confusedbrow talking2mouth "I'd kinda like an explanation of why we're here, actually?"

leaf @sarcastic "{size=30}What did I just--{/size} Fine. [first_name] is back in Pallet Town. We're going to get him back."

ethan @confusedbrow talking2mouth "Uh-huh. All I told you was that he dropped out of Kobukan. How do you know he didn't just get a job somewhere in Inspira?"

pause 1.0

show tia surprisedbrow frownmouth
show yellow surprisedbrow frownmouth
with dis

blue @angry "Yeah, actually, how {i}do{/i} you know that?! Are you saying this entire time, that idiot could've been just a couple miles away?"

show tia -surprisedbrow -frownmouth -surprised frownmouth
show yellow -surprisedbrow -frownmouth -surprised frownmouth
with dis

leaf @talking2mouth "No. Not a chance. I asked Ethan where he wanted to be on Sunday, and he said 'Home.'"

yellow @talkingmouth "Um... what does that have to do with anything?"

ethan @sad2brow talking2mouth "It's crazy, but [first_name] and I are kinda, like... in sync. We end up at the same place all the time. Still, to bet so much on this..."

leaf @talking2mouth "I'm confident I'm right. And if I'm not, I'll take the fall, no-one else."

pause 1.0

leafmind @sadbrow frownmouth "Ulp. Don't think about falling."

ethan @talkingmouth "So, I don't hate this plan. Like I said, I'd like to get [first_name] back as well. But isn't there a more sensible solution that we could try, first?"

leaf @sarcastic "Any suggestions?"

ethan @closedbrow talking2mouth "Uh, like, a regular plane ticket?"

blue @closedbrow talkingmouth "Tried that. Nothing's going out and coming back soon enough."

leaf @embarrassedbrow talkingmouth "We could, maybe, try to reserve a seat on a plane that's already fully-booked and just hope for a cancellation, but this plan, though it's crazier, I actually think has a higher chance of succeeding."

ethan @closedbrow talking2mouth "Damn."
ethan @surprised "Oh, wait, what about that one pilot student? Eartha, or whatever?"

blue @angry "We already asked her! God, can you come up with a {i}single{/i} original thought?!"

ethan @sad2eyes talking2mouth "{size=30}Well, excuse {i}me{/i}, princess...{/size}"

leaf @angrybrow talking2mouth "Hey. Lay off."

show tia sadeyes with dis

blue @angrybrow talkingmouth "Oh, like {i}you're{/i} any better! You're just as much of an asshole as I am, people just like you 'cause you pretend your insults are jokes."

pause 1.0

leaf @sadbrow talking2mouth "What?"

pause 1.0

blue closedbrow @talkingmouth "Tch."

pause 1.0

yellow @talkingmouth "Um... Blue's sorry."

blue -closedbrow @angrybrow talkingmouth "Don't speak for me."

yellow @sad "I'm sorry..."

pause 2.0

ethan @closedbrow talking2mouth "{size=30}Damn, this is awkward.{/size} So, I can't help but notice that we have about 24 hours until the Quarter Qlashes begin."
ethan @confusedbrow talking2mouth "We really left it to the last minute, huh?"

leaf @happy "We're students. Last-minute desperation is when we're most productive!"

show tia:
    xpos 0.4
    ease 0.5 ypos 1.1
    ease 0.5 ypos 1.0

pause 0.5

ethan @confusedeyebrows talking2mouth "I totally get that. Been there. And I don't want to rain on any parades, but I think we left it a bit too long. I mean, as far as I know, none of you have a Pokémon that can make that journey fast enough, right?"

pause 1.0

show garden with vpunch
show ethan confusedeyebrows with dis

leaf @surprised "Oh my God, we didn't tell Ethan."

blue @surprised "What?"

leaf @talking2mouth "We didn't tell Ethan about Tia."

blue @angrybrow talkingmouth "Damn, I was hoping that was a dream."

leaf @talking2mouth "Okay, we don't have time to do this gently. Tia, rip the band-aid off."

pause 1.0

show tia angrybrow poutmouth with dis

pause 1.0

leaf @angrybrow talking2mouth "What?"

show blue:
    xpos 0.8
    ease 0.5 ypos 1.2 zoom 1.3

blue @closedbrow talkingmouth "{size=30}Get a clue. She might be an airhead, but she's still a powerful dragon Pokémon. Think she's going to listen to some rookie trainer without [first_name]'s bullshit powers?{/size}"

pause 1.0

leaf @sadbrow talking2mouth "I... no, I didn't think about that."

show blue:
    xpos 0.8
    ease 0.5 ypos 1.0 zoom 1.0

pause 1.0

leaf @sadbrow happymouth "Hey, sweetie. Um... could you show Ethan your true form, please?"

show tia:
    xpos 0.4
    ease 0.2 xpos 0.39
    ease 0.2 xpos 0.4
    ease 0.2 xpos 0.41
    ease 0.2 xpos 0.4

pause 0.5

yellow @closedbrow talkingmouth "That means no."

leaf @sarcastic "Yeah. Got it."

pause 1.0

leaf @embarrassedbrow talking2mouth "Hey, uh, Ethan. This is going to sound like a really weird question, but can you ask Tia to show you her true form?"

ethan @confusedeyebrows talkingmouth "Her 'true form'? Uh... she's going to keep her clothes on, right?"

leaf @sadbrow happymouth "Well, she'll keep the hat."

ethan @closedbrow talking2mouth "{size=30}This is the weirdest orgy I've ever been to.{/size}"
ethan @sadbrow talkingmouth "Hey, Tia. Think you could show me your true form? I think it'd be really helpful for figuring out what's going on."

show tia:
    xpos 0.4
    ease 0.5 ypos 1.1
    ease 0.5 ypos 1.0
    
pause 0.5

yellow @talkingmouth "That means--"

ethan @closedbrow talkingmouth "I think we got it, thanks."

show tia neutraleyebrows poweredeyes poweredhat neutralpowered with Dissolve(2.0)

ethan surprisedbrow frownmouth @surprised "Huh?"

hide tia
show latias hat frownmouth poweredeyes poweredhat powered behind blue:
    xpos 0.4 ypos 1.0
    parallel:
        ease 4.0 xpos 0.42
        ease 4.0 xpos 0.4
        ease 4.0 xpos 0.38
        ease 4.0 xpos 0.4
        repeat
    parallel:
        ease 2.0 ypos 1.0
        ease 2.0 ypos 1.02
        ease 3.0 ypos 1.0
        ease 3.0 ypos 0.98
        repeat
with gaussdissolve

pause 2.0

ethan -surprisedbrow -frownmouth -surprised @talking2mouth "Okay, {i}now{/i} it's the weirdest."

$ PlaySound("pokemon/cries/380.mp3")

latias -frownmouth -poweredeyes -poweredhat -powered @happy "Latias!"

ethan @talking2mouth "Latias, huh?"

pause 2.0

ethan @closedbrow talking2mouth "Can you get to Pallet Town fast enough?"

latias @angrybrow talkingmouth "La."

ethan @talkingmouth "Alright. I think I'm caught up."

leaf @surprised "Really? That easily?"

ethan @happy "Pretty much nothing phases me. My roommate has mind control powers. Okay. My classmate's a dragon. Sure, whatever."
ethan @closedbrow talking2mouth "Anyway, we don't have time for me to lose my mind over this. What's the plan?"

hide latias
show tia hat uniform:
    xpos 0.4
with gaussdissolve

leaf @talking2mouth "I'm going to fly to Pallet Town on Tia's back."

ethan @talkingmouth "Strong start. Carry on."

show yellow surprisedbrow frownmouth with dis

leaf @talking2mouth "When we get there, [first_name] and I are going to ride back on Tia."

yellow -surprisedbrow -frownmouth -surprised frownmouth @sad "Oh... I'm sorry, Leaf, but Tia probably won't be fast enough to get back with two people on her. Too much weight."

show tia surprisedbrow frownmouth with dis

leaf @closedbrow talking2mouth "I remember. But I think Tia {i}can{/i} do it."

pause 1.0

blue @surprised "Uh, yeah, why? What are you basing that on?"

leaf @talking2mouth "Remember what Instructor Clair said? She said Dragon-types rise to meet the demands of the challenge in front of them."
leaf @talking2mouth "Maybe you've never flown that fast before. But I believe you can when it matters."

show tia sadbrow embarrassedmouth with dis

pause 1.0

blue @closedbrow talkingmouth "You know what a freak Clair is about Dragon-types. She says they can do anything."

leaf @talking2mouth "Yes. But there's one more thing. A... uh... {i}a guy{/i} reminded me that Pokémon underestimate their capabilities. I'm sure [first_name] can get more out of her."

show tia:
    xpos 0.4
    ease 0.5 ypos 1.1
    ease 0.5 ypos 1.0

yellow @surprised "Oh!"

leaf @surprised "What, what did she say?"

if (oldpersondex["Tia"]["RelationshipRank"] == 1):
    yellow @talkingmouth "She said that [first_name] is already her trainer. And she, um, she thinks you're right. That her trainer can probably make her speed up."

else:
    yellow @talkingmouth "She said that might work. She says she feels more energetic, more powerful, around [first_name]. So she might be able to speed up."

yellow @sad "But... not enough..."

leaf @closedbrow talking2mouth "That's fine. This is a three-part plan."

show blue surprisedbrow frownmouth
show yellow surprisedbrow frownmouth
show tia surprisedbrow frownmouth
show ethan surprisedbrow frownmouth
with dis

leaf @talking2mouth "We need to delay the beginning of the Quarter Qlashes."

blue @happy "Oh, yeah, sure, let me just submit the paperwork, and I'll--{nw}"

show garden with vpunch
show yellow -surprisedbrow -frownmouth -surprised frownmouth
show tia -surprisedbrow -frownmouth -surprised frownmouth
show ethan -surprisedbrow -frownmouth -surprised frownmouth
with dis

extend @angry " Are you insane?!"

leaf @talking2mouth "No. I did a ton of research last night. The Greater Inspira area is meant to field 960 matches on Wednesday, starting at noon and ending at 8 PM."

leaf @talking2mouth "We all know when our time slots are, because Alder and Bruno told us during Gym Class. The problem is we don't know when [first_name] is meant to battle, so we just need to delay the entire event."

blue @closedbrow talkingmouth "Yeah, I'm sure you {i}did the math.{/i}"
blue surprised @angry "That's still a stupid plan! How do you think we're--{w=0.5} {i}you're{/i} going to delay the Quarter Qlashes while you're riding across the ocean?"

leaf @talking2mouth "I'm not going to. But {i}you{/i} are."

pause 1.0

blue -surprisedbrow -frownmouth -surprised frownmouth @closedbrow talkingmouth "Yeah, you're crazy."

leaf @angry "At least hear me out!"

pause 1.0

blue @talkingmouth "I'm not going anywhere. Keep on flapping your jaws. Unlike some people, I actually {i}listen{/i} to the people around me, even if they're idiots."

leaf @sarcastic "Great."
leaf @talking2mouth "So, as I was saying, I did the math. Wednesday will field 960 matches across eight hours." 
leaf @talking2mouth "The event can only start when enough people to field the first round of matches show up, so about twenty, assuming the arena can hold ten battles at a time, like with the tryouts."

blue @talkingmouth "Uh-huh."

leaf @talking2mouth "So here's what you do. Stand at the entrance to the Battle Hall and challenge {i}anyone{/i} who comes your way to a battle." 
leaf @talking2mouth "If they win, they get to go past you. And if they lose, then they need to run back to Inspira to heal. But I don't think it's likely they'll show up again after losing to you."

blue @angrybrow talkingmouth "What do you mean?"

leaf @embarrassedbrow talkingmouth "Um..."

pause 1.0

leaf @talking2mouth "Okay, I'm just going to say this... losing to you is seriously demoralizing."

blue @angry "Huh? What, because you think you're {i}better{/i}--"

leaf @angry "No! Calm down, Blue, it's not an attack! It's because of your trash talk!"

blue @surprised "Huh?"

leaf @closedbrow talking2mouth "Whenever I battle with you, in gym class, or during our Battle Team meetings, I never get the idea that you {i}like{/i} battling."

blue @angrybrow talkingmouth "What are you talking about? I'm amazing at it."

leaf @sarcastic "That's not what I said."
leaf @talking2mouth "I said you don't {i}like{/i} battling."
leaf @happy "I love it. I feel {i}alive{/i} when I battle. To see the emotions on my opponent's face, to put myself through the pressure, to have to come up with a plan, and then see that plan succeed or fail... that's what I love."

pause 1.0

leaf @talking2mouth "But... when I battle you... I feel like you don't battle for fun. You battle to embarrass, dominate, and humiliate your opponent. You battle to prove you're better."

pause 1.0

blue @closedbrow talkingmouth "And you think that'll stop people from getting into the battle hall?"

leaf @happy "Definitely. Just make sure to say 'smell ya later!' after you win, and I bet some people who try to get in will just leave."

blue @closedbrow talkingmouth "You're asking me to take on dozens of battles in a row."

pause 2.0

leaf @sarcastic "What, are you expecting me to try and reverse-psychology you? Like, 'I bet you can't do it?'"

show yellow surprisedbrow frownmouth with dis

leaf @talking2mouth "I know you can. You train all night. Janine practically had to pull you off of Bea during our last battle meeting."

show yellow frownmouth with dis

blue surprisedbrow frownmouth @surprised "H-hey! {i}She{/i} jumped on {i}me{/i}!"

pause 1.0

show blue -surprisedbrow -frownmouth -surprised closedbrow frownmouth with dis

leaf @sarcastic "...I was talking about the battle."

blue @talkingmouth "I knew that."

leaf @talking2mouth "Anyway, what do you think?"

blue @surprisedbrow talkingmouth "Isn't there something better I could be doing?"

leaf @talking2mouth "What would you be doing otherwise? Training, right? This is just training. Training against {i}actual trainers{/i}. Think of it as a warm-up to your Quarter Qlash match."

blue @talkingmouth "That's still {i}a lot{/i} of battles. And I can't tap out until you get back."

leaf @talking2mouth "These will be the same people that are attempting to compete in the Quarter Qlashes." 
leaf @talking2mouth "Remember what Instructor Lance said? {i}No Battle Team member{/i} has {i}ever{/i} been eliminated in the first round of the Quarter Qlashes. You can probably beat 99.9%% of the people who show up here."

blue @surprisedbrow talkingmouth "And if another Battle Team member shows up?"

leaf @talking2mouth "Just let them by. There's less than ten of us. The Quarter Qlashes can't start with that small number."

blue @talkingmouth "...Makes sense, so far."

pause 1.0

blue @talkingmouth "If I'm going to be battling dozens of people back-to-back, I'm going to need healing. Even if I one-shot those bozos, my 'mons will still get tired."

pause 1.0

show yellow surprisedbrow frownmouth with dis

blue -closedbrow @talkingmouth "...Yellow, will you help me do this?"

yellow -surprisedbrow -frownmouth -surprised blush @happy "Oh! Y-yes! Always, Blue!"

blue @talkingmouth "Fine. One more thing. Your Dratini, Leaf."

leaf @surprised "Huh?"

blue @talkingmouth "Let me borrow your Dratini while I'm battling."

leaf @angrybrow talking2mouth "Why?"

blue @angrybrow talkingmouth "Call it 'insurance,' if you want."
blue @closedbrow talkingmouth "Your Dratini is... very powerful. Like, for a baby dragon, I've never seen one as strong as yours. I want to use it."
blue @talkingmouth "And if I'm fighting a dozen guys for you, I need every advantage I can get."

pause 2.0

$ PlaySound("Pokemon/ball sound.ogg")

pause 1.0

leaf @talking2mouth "Dratini, are you okay with this?"

$ sidemonnum = pokedexlookupname("Dratini", DexMacros.Id)

sidemon @talkingmouth "Dra!"

leaf @sadbrow happymouth "Alright, sweetie. If you want. Blue's a good trainer, so... you'll be fine."

$ AddEvent("Leaf", "LentDratini")
$ playerparty.remove(GetTrainerTeam("Leaf", "Dratini"))

narrator "You lent Blue your Dratini."

blue @happy "Then I guess I'm doing this!"
blue @talkingmouth "Kinda funny. I spent so long trying to get into the Battle Hall, and now {i}I've{/i} gotta keep people from getting in."
blue @angrybrow happymouth "But those suckers aren't getting past me."

pause 1.0

ethan @talking2mouth "Yeah. Hi. Still here. I hate to blow a hole in the side of your theory, but the Quarter Qlashes are an actual Kobukan-wide event. There's going to be official security and stuff."

yellow @surprised "Oh! Not quite."

ethan @confusedeyebrows talkingmouth "Huh?"

yellow @talkingmouth "Ms. Miriam told us that in the event of any emergency happening on school grounds, the school's own nursing department, and students, would be responsible for... um, the response."
yellow @closedbrow talkingmouth "It's the same for the security department."

ethan @talkingmouth "Damn. Didn't know that, Yellow. But that still doesn't put us in the clear. If Inspira security isn't here, then we know who will be."

blue @surprised "Wait... then that means..."
blue @angrybrow talkingmouth "Damn it. The {i}Disciplinary Committee{/i} is going to be on my ass."
blue @talkingmouth "I can't afford to get on their bad side. Cheren's already said that he's keeping an eye on me."

leaf @talking2mouth "And that's where you come in, Ethan."

ethan @confusedeyebrows talking2mouth "...I'm not seeing it."

leaf @happy "You've got the same power--Frienergy--as [first_name] does."

show yellow surprisedbrow frownmouth
show tia surprisedbrow frownmouth
with vpunch

blue angry "WHAT?!"

ethan @sad2eyes talking2mouth "I don't know for sure, but... I can command Pokémon instantly, like [first_name] can. So maybe?"

show yellow -surprisedbrow -frownmouth -surprised
show tia -surprisedbrow -frownmouth -surprised
with dis

blue -angry frownmouth @angry "{size=30}Goddamn. {i}Everyone{/i} but me, huh?{/size}"

ethan @talking2mouth "Anyway, I still don't see how this power is supposed to help me with the Disciplinary Committee."

leaf @talking2mouth "Just distract them. You can talk to them, and drag them into a long conversation, and 'cause people like you, you can keep them there for a long time." 
leaf @talking2mouth "It'll probably even take an hour or so for them to even realize anything is wrong, so that's when you step in."

ethan @confusedeyebrows talking2mouth "...'Because people like me'?"

leaf @happymouth "Sure."

ethan @talking2mouth "I think maybe you weren't listening to Professor Oak. The entire point of Frienergy is that people don't like me--or [first_name]. They just understand our feelings." 
ethan @closedbrow talking2mouth "So if I'm trying to trick or delay the Disciplinary Committee, {i}they'll know.{/i}"
ethan @sad2eyes talking2mouth "Like, I can lie, and even if people don't believe me, if there's nothing they can do about it, they just have to drop the issue. But that won't work against the DC."
ethan @sadbrow happymouth "Heck, the moment I show up at their office, they'll probably just get the feeling that they should check out the Battle Hall."

pause 1.0

leaf @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
leaf @talking2mouth "Do you... do you have any other suggestions?"

pause 2.0

ethan @talkingmouth "No. But I think I can do something."

leaf @surprised "What?"

ethan @closedbrow talking2mouth "I can't tell you what my plan is. But I {i}think{/i} I might be able to distract the Disciplinary Committee."

leaf @flirtbrow talking2mouth "Why can't you tell us?"

ethan @sad2eyes talkingmouth "Because it's a long shot and I'll look really stupid if it fails."

show tia:
    xpos 0.4
    ease 0.5 ypos 1.1
    ease 0.5 ypos 1.0

yellow @talkingmouth "Tia believes in you."

ethan @sad2eyes talkingmouth "Yeah, I'm still processing that one of my classmates is a Pokémon."

blue @closedbrow talkingmouth "{size=30}Two, actually...{/size}"

ethan @surprised "What?"

blue @talkingmouth "Nothing."

leaf @sadbrow talking2mouth "Okay... I'm kinda nervous about that, not going to lie, but we're quickly running out of time."

pause 1.0

yellow @talkingmouth "Lunch is almost over. If you're going to go, then..."

leaf @closedbrow talking2mouth "...Yeah."

pause 1.0

blue @talkingmouth "What are you going to do about the water, though?"

leaf @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

leaf @talking2mouth "Tia."

show tia surprisedbrow frownmouth with dis

leaf @sadbrow talking2mouth "I'm... I'm sorry for acting jealously over [first_name]."

pause 1.0

show tia happybrow with dis:
    xpos 0.4
    ease 0.5 ypos 1.2 zoom 1.3

pause 1.0

leaf @surprised "Huh?"

leafmind sadbrow blush "A hug?"

pause 1.0

leafmind @frownmouth "She never saw me as a rival at all..."

show tia -happybrow with dis:
    xpos 0.4
    ease 0.5 ypos 1.0 zoom 1.0

pause 1.0

leaf -blush @sadbrow talking2mouth "This might have been easier if you {i}did{/i} have some sort of grudge against me."
leaf @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
leaf @talking2mouth "Tia, when I get on your back, I'm probably going to immediately ask you to let me off. I'm going to scream, and... maybe say some pretty awful stuff to you... so I need you to not let me off, no matter what I say, okay?"
leaf @angrybrow talking2mouth "We need to see this to the end."

show tia angrybrow frownmouth with dis:
    xpos 0.4
    ease 0.5 ypos 1.1
    ease 0.5 ypos 1.0

pause 0.5

yellow @happymouth "She says that she won't be able to hear you because of the wind, anyway. Putting up the light screen will block wind for you, but reduce her own aerodynamics, so she's going to keep the area of effect as small as possible."

leaf @sadbrow happymouth "Great...?"

blue @closedbrow talkingmouth "And you're still trying to claim you don't 'speak Pokémon', huh?"

yellow @angrybrow talkingmouth "I don't."

pause 1.0

leaf @talking2mouth "Alright. We're actually leaving a little bit early. Unless we get {i}massively{/i} delayed by running into, like, an airliner, we should be there tonight."

blue @closedbrow talkingmouth "...Yep."

pause 1.0

leaf @sadbrow talking2mouth "You guys will play your parts, right?"

blue @angry "Stop stalling! Get on the damn dragon!"

show garden:
    xalign 0.5 yalign 0.5 zoom 1.0
    ease 10.0 zoom .625

show ethan:
    xpos 0.2
    ease 10.0 zoom 0.8

show tia:
    xpos 0.4
    ease 10.0 zoom 0.8

show yellow:
    xpos 0.6
    ease 10.0 zoom 0.8

show blue:
    xpos 0.8
    ease 10.0 zoom 0.8

pause 1.0

leaf @embarrassedbrow happymouth "H-hey, you know, I was kinda thinking that maybe we should just see if we can book a plane ticket anyway, or..."

yellow @happy "Oh, it's too late for that."

ethan @happy "Yup. You canned these worms--now lie in them."

leaf @sadbrow happymouth "H-hey, guys, this is actually kinda a dumb plan, isn't it? Shouldn't we just--"

hide tia
show latias hat playfuleyes playfulmouth behind yellow:
    xpos 0.4 ypos 1.0 zoom 0.8
    parallel:
        ease 4.0 xpos 0.42
        ease 4.0 xpos 0.4
        ease 4.0 xpos 0.38
        ease 4.0 xpos 0.4
        repeat
    parallel:
        ease 2.0 ypos 1.0
        ease 2.0 ypos 1.02
        ease 3.0 ypos 1.0
        ease 3.0 ypos 0.98
        repeat
with gaussdissolve

leafmind @surprisedbrow frownmouth "{size=20}Oh no.{/size}"

show garden with vpunch

show ethan happy behind latias
show yellow happy behind latias
show blue happy behind latias
show latias angrybrow happymouth:
    ease 0.3 xpos 0.4 zoom 1.3 ypos 1.2
with dis

leafmind @surprised "{size=50}{b}Oh no.{/b}{/size}"  

show garden:
    ease 0.5 ypos 2.0

show ethan:
    xpos 0.2
    ease 0.5 ypos 2.0

show latias:
    xpos 0.4
    ease 0.5 ypos -1.0

show yellow:
    xpos 0.6
    ease 0.5 ypos 2.0

show blue:
    xpos 0.8
    ease 0.5 ypos 2.0

pause 0.5

call clearscreens from _call_clearscreens_98

show blank2:
    alpha 0.0
    ease 10.0 alpha 1.0

leaf @surprised "{cps=20}AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!{/cps}"

pause 3.0

show evening at vspaz

$ timeOfDay = "Evening"

pause 3.5

python:
    playercharacter = None
    
    playerparty = [pikachuobj]
    inventory = oldinventory
    personalstats = oldpersonalstats
    persondex = oldpersondex
    classstats = oldclassstats
    persondex["Cheren"]["Relationship"] = "Anathema"
    persondex["Grusha"]["Relationship"] = "Friend"
    persondex["Jasmine"]["Relationship"] = "Friend"
    persondex["Brock"]["Relationship"] = "...Student?"

stop music fadeout 1.5

narrator "{color=#00b23f}You are no longer you.{/color}"

show screen currentdate
scene farmland 
with Dissolve(5.0)

$ PlaySound("Pokemon/pikachu_sad.ogg")
pikachu sad_2 "Pika... Pi-ka."

show screen songsplash("Pallet Town", "Zame")
queue music "audio/music/sadpallet.ogg"

narrator "You stand in the middle of a field."

pause 1.0

$ PlaySound("Pokemon/pikachu_sad2.ogg")
pikachu sad "Pi-ka?"

narrator "A long tool is in your hand."

pause 1.0

$ PlaySound("Pokemon/pikachu_sad.ogg")
pikachu sad_2 "Pi..."

narrator "You take a deep breath."

pause 1.0

play sound "audio/shovel.ogg" loop

narrator "And you begin to dig."

show mom sadeyes sadeyebrows tired angrymouth with Dissolve(3.0)

mom "{w=0.5}.{w=0.5}.{w=0.5}."

pause 1.0 

mom @talking2mouth "Sweetheart."

red shadow frownmouth noeyes noshine "{w=0.5}.{w=0.5}.{w=0.5}."

show mom:
    xpos 0.5
    ease 0.5 ypos 1.2 zoom 1.3

mom @sadmouth "{size=30}Sweetheart?{/size}"

red  "{w=0.5}.{w=0.5}.{w=0.5}."

mom tears @closedbrow talking2mouth "Please, honey. Talk to me. We don't have to talk about what happened. I just want to hear your voice."

red "{w=0.5}.{w=0.5}.{w=0.5}."

pause 1.0

stop sound

red -shadow -noeyes -noshine tired @sadbrow talking2mouth "{size=30}Okay.{/size}"

mom @surprised "Oh!"

show mom happybrow tiredhappy -angrymouth with dis

narrator "Your mother hugs you for an uncomfortably long time...{w=0.5} before finally letting go."

show mom -tears -happybrow tired with dis:
    xpos 0.5
    ease 0.5 ypos 1.0 zoom 1.0

mom @talking2mouth "...What are you doing, sweetheart?"

show mom surprisedbrow frownmouth with dis

red @talking2mouth "I'm becoming a farmer."

play sound "audio/shovel.ogg" loop

pause 1.0

mom @confusedeyebrows talking2mouth "A... farmer, sweetheart?"

red @closedbrow talking2mouth "Yep."

pause 1.0

show mom -surprisedbrow -frownmouth -surprised sadeyebrows sadeyes angrymouth with dis

red @talking2mouth "Couldn't hack it as a Pokémon trainer. Couldn't even keep my friends, when I literally had a power that made it easier for me."

mom @confusedeyebrows sadmouth "{size=30}What?{/size}"

red @closedbrow talking2mouth "So I'm giving up. Giving up Pokémon, giving up ever having a social life. Giving up having a life, period."

pause 1.0

red @talking2mouth noshine "And becoming a farmer."

pause 1.0

mom @talkingmouth "...Are you digging a pit?"

red @talking2mouth "Yep. This is where I'm going to bury my hopes and dreams. And after that, maybe I'll plant some carrots here."

$ PlaySound("Pokemon/pikachu_sad.ogg")
pikachu sad_2 "Pi..."

pause 1.0

mom "{w=0.5}.{w=0.5}.{w=0.5}."
mom @talkingmouth "Wouldn't you rather use a shovel for this?"

red @confusedeyebrows talking2mouth "Huh?"

mom @talkingmouth "It's just that you're using a hoe. A hoe isn't a very good tool for digging."

pause 1.0

stop sound

pause 1.0

$ PlaySound("throwmetal.ogg")

show mom sadbrow angrymouth with dis

show farmland with vpunch

pause 1.0

red sadbrow tears @talking2mouth "...I don't know what to do, Mom."

show mom:
    ease 1.0 zoom 1.3 ypos 1.2

mom @talking2mouth "...I'm here to listen to whatever you want to say. And no matter what you say, I'll love you more than anyone else in the world."

pause 1.0

show mom surprisedbrow frownmouth with dis

red @sadbrow happymouth "...Grace Umaoka is a lousy Rhyhorn racer."

mom -surprisedbrow -frownmouth -surprised @playfuleyes talking2mouth "I have my limits, young man. You know this house is an Umaoka family shrine."

if (GetRelationshipRank("Serena") == 1):
    pause 1.0

    red @talkingmouth "...I met her daughter, you know."

    mom @surprised "Grace's daughter? What?!"

    red @talking2mouth "Yup."

    mom @happy tiredhappy "What was she like?"

    red @closedbrow talking2mouth "She's pretending to be Kalosian, and likes conspiracy theories."

    pause 1.0

    mom @surprised "Oh."

else:
    red @talkingmouth "Yeah. I know. I've still got her poster in my room."

pause 2.0

show mom surprisedbrow frownmouth with dis

red @talking2mouth "I... was running in a Student Council election."

show mom -surprisedbrow -frownmouth -surprised with dis

narrator "Your mother waits patiently for you to continue your story."

pause 1.0

$ PlaySound("Pokemon/pikachu_sad2.ogg")
pikachu sad "Pika."

narrator "It takes a while."

pause 1.0

red @closedbrow tears talking2mouth "When I was up there... I'd just finished giving my last speech. The only thing left was the voting."
red @shadow -tired noeyes noshine talking2mouth "And then... someone I thought was a friend... he told everyone about Frienergy."

pause 1.0

mom @talking2mouth "About what, sweetheart?"

red @sadbrow happymouth "You don't know? I kinda figured you would."

pause 1.0

show mom surprisedbrow frownmouth with dis

red @talking2mouth "I've... apparently I've got this power that makes people and Pokémon understand my feelings better."
red @sadbrow talking2mouth "Sam told me about it. It's called Frienergy, and... he wanted to see what its effects were like on large groups of people, or other Pokémon."

show mom -surprisedbrow -frownmouth -surprised closedeyes angryeyebrows angrymouth with dis

pause 2.0

red @sadbrow talking2mouth "I know it's hard to believe, Mom, but I promise I'm telling the truth."

mom @talking2mouth "I believe you."

red @confused "That easily?"

mom -closedbrow @sadbrow happymouth "You're my darling baby boy, [first_name]. From the first moment I held you in my arms, I knew I would love, trust, and believe in you, no matter who or what you became."

mom @happyeyes happyeyebrows tiredhappy talkingmouth "My only fear when you went off to some big-city school was that you'd come back embarrassed of a simple country girl like me."

show mom surprisedbrow frownmouth 
show farmland 
with vpunch

red @tears cry surprised "Mom!"

show mom:
    xpos 0.5
    ease 0.5 ypos 1.3 zoom 1.4

narrator "You embrace your mother tightly, tears streaming down your face."

show mom sadbrow embarrassedmouth with dis

pause 2.0

mom tears @talkingmouth "{size=30}{cps=20}It's alright, sweetheart.{w=0.5} It'll {i}all{/i} be alright.{/cps}{/size}"

scene blank2 with Dissolve(3.0)

narrator "You sit there with your mother for quite a while as you slowly tell the story of your past month at school."

scene farmland
show mom angrymouth sadbrow 
with Dissolve(1.0)

pause 1.0

mom @talking2mouth "I'm so sorry you had to go through all that alone."

red @sadbrow talkingmouth "It's my bad, really. I should've told you about this a long time ago."

pause 1.0

red @sadbrow talking2mouth "What... what would you have told me to do, if I had told you as soon as I found out?"

mom @closedbrow talking2mouth "I would have told you to trust your heart. But if you didn't know what to do, I would have told a couple close friends."
mom @angryeyebrows closedeyes talking2mouth "Then, based on how they reacted, I'd start making it more public. Maybe faster or slower."

red @sadbrow talking2mouth "Sam told me not to do that, though."

mom @sadbrow talkingmouth "Doctor Samuel is an extremely smart man. Whenever he starts talking, I'm still trying to figure out what he was saying in the last conversation we had."
mom @angrybrow talking2mouth "But he is a darn {i}fool{/i} when it comes to people. Anyone could have told him this would happen if you tried to keep it secret."
mom @talkingmouth "Secrets just hurt people. The people you're keeping the secret from, and the person keeping the secret."

red @closedbrow talking2mouth "...{i}Sigh.{/i}"

pause 1.0

red @talking2mouth "Yeah. In hindsight, I really should have known that. Maybe I'm just as oblivious to people as Sam is."

mom @sadbrow talkingmouth "No, sweetheart. You're an incredibly empathetic and intuitive young man. You're just immature and inexperienced."

red @confusedeyebrows happyeyes talking2mouth "Didn't you have me when you were, like, sixteen?"

mom @angrybrow poutmouth "...Well, yes, but I never claimed to be more mature than you at the same age."
mom @closedbrow talkingmouth "Heaven knows I made my mistakes back in the day."
mom @sadbrow talking2mouth "But you, my baby boy, have never been counted amongst them."

pause 2.0

red @sadbrow tears talking2mouth "Where do I go from here?"
red @closedbrow tears talking2mouth "{size=30}I {i}really{/i} don't want to be a farmer.{/size}"

mom -angrymouth @happy "You don't have to be a farmer, sweetheart."

pause 1.0

mom @talking2mouth "I can't tell you what to do, angel. Only that you should follow your heart."
mom @confusedeyebrows closedeyes talking2mouth "What do you {i}want{/i} to do?"

pause 1.0

stop music fadeout 1.5
show screen songsplash("The Very Best?", "PianoDeuss")
queue music "audio/music/TheVeryBest_start.ogg" noloop
queue music "audio/music/TheVeryBest_loop.ogg"

red @sadbrow talking2mouth "I... I want to be the very best. Like no-one ever was."

mom @closedbrow talking2mouth "...Mm. You're so much like your father."

pause 1.0

red @sadbrow talking2mouth "What would Dad do in this situation, Mom?"

mom @angrybrow poutmouth "Oh, he'd almost certainly run right back into the danger. Every challenge he ever faced, he faced with courage."
mom @sadbrow talking2mouth "...Right up to the end."

pause 1.0

red @talking2mouth "What happened?"

mom @surprised "You don't remember?"

red @closedbrow talkingmouth "Maybe I did, back in the day."
red @sadbrow happymouth "But we don't ever talk about him, so I guess... I forgot."

mom @closedbrow talking2mouth "Hm. That's... odd. We don't often talk about him, that's true, but I could have sworn you'd remember..."

if (last_name != "Sugimori"):
    mom @confusedeyebrows talkingmouth "Remember how you took his last name after he passed away, as a way of honoring him?"

    red @talkingmouth "Yeah, I remember that. But that was after the funeral, like, two months after."

    mom @closedbrow talkingmouth "Hm..."

red @sadbrow talking2mouth "Sorry, Mom. I guess my memory isn't as good as I thought it was."

mom @closedbrow talking2mouth "Oh, it's alright, dear. It was a very scary and sad day for everyone."

pause 1.0

mom @talkingmouth "It was the day of the Cinnabar eruption, remember? You were out playing with your friend, when we felt an intense heat wave come from the south."
mom @closedbrow talking2mouth "We saw the magma pouring out of the volcano in the south just a few moments later."
mom @sad2eyes sadeyebrows talking2mouth "Your father knew that the people on Cinnabar couldn't afford to wait for the Coast Guard to arrive to evacuate. So he grabbed his Poliwhirl and rushed out there to..."

pause 1.0

mom @happy "To be a hero, sweetheart. And that he was."

pause 1.0

mom @closedbrow talking2mouth "I tried to stop him, briefly. I asked him to think about his son, about me--how we needed him."
mom @sadbrow talking2mouth "And he asked me to think about the sons and wives of the people he could save."

pause 1.0

mom @closedbrow talking2mouth "For a while... I hated him."

pause 1.0

mom @happy "But that's just the sort of man he was. He never cared what people thought of him, or what might happen to him, as long as he was doing the right thing."
mom @sadbrow talkingmouth "He... he wanted his Poliwhirl to be your first Pokémon, you know..."
mom @happy "But I suppose if that happened, then you wouldn't have found [pika_name]."

red @talkingmouth "...What's the right thing in this situation?"

mom @closedbrow talkingmouth "What scares you more, darling? The fire? Or the water?"

red @surprised "Huh?"

mom @talkingmouth "If you go back there, people will be scared of you. You'll have to constantly explain yourself to everyone you come across. You'll have to ask for forgiveness, over and over, even though you've done nothing wrong."
mom @closedbrow talkingmouth "You'll have to beg Dean Drayden to let you back in. We still don't know how you'll pay for the school. Some people will blame you for their problems, even years down the line."

red @confused "You're... not making this sound appealing. Is there a 'but' to this?"

mom @sadbrow talking2mouth "No 'but', sweetheart."
mom @closedbrow talkingmouth "That's the fire you'll be walking into."

pause 1.0

mom @talkingmouth "Or... you can stay here. Go back in your room. I'll take care of you, honey, and I'll never say another word about this, unless you want me to."
mom @sadbrow talking2mouth "After a while, the pain will dull. But there will be nights when you remember what might have been. And water will pour from your eyes."

pause 1.0

red @confusedeyebrows talking2mouth "Geez, Mom..."

mom @closedbrow talking2mouth "I'm sorry, sweetheart. I'm just trying to be realistic."

red @happy "No, I mean, geez, you've got a way with words. Didn't you want to be an English teacher?"

mom @sad2eyes talking2mouth "Yes, but... if I had a teacher's salary, I'd be making even less than I do now!"
mom @happy "This call center job might suck, but at least I can do it remotely."

pause 1.0

show mom surprisedbrow frownmouth with dis

red @sadbrow talking2mouth "{i}If{/i} I go back..."
red @closedbrow talking2mouth "I'm going to miss the first round of the Quarter Qlashes. Participation is mandatory. I don't think I can even graduate without participating."

mom -surprisedbrow -frownmouth -surprised @confusedeyebrows playfuleyes talkingmouth "Can you graduate without {i}paying{/i}?"

red @talkingmouth "Touchy."

mom @closedbrow talking2mouth "I think it's pronounced {i}touché{/i}."

pause 1.0

red @closedbrow talking2mouth "Ugh. I really made a dumb decision. Running away like that probably just convinced everyone that Cheren was right."
red @sadbrow talking2mouth "If I hadn't frozen, then... maybe I could have... explained the truth, at least. I would've had a real shot of turning the tide."

show mom:
    xpos 0.5
    ease 0.5 ypos 1.2 zoom 1.3

pause 1.0

mom @closedbrow talkingmouth "None of that, my boy. There's no could or would worth thinking about. All that matters is what you can and will."

show mom:
    xpos 0.5
    ease 0.5 ypos 1.0 zoom 1.0

red @sadbrow talkingmouth "I'm sorry. I know we couldn't afford the flight back here. Never mind the flight back there."

mom @happy "We couldn't afford the {i}school{/i}, darling. A couple flights is nothing. Just like we always have, we'll figure something out. I've been taking on more hours, actually."

pause 1.0

redmind @sadbrow frownmouth "...How am I the luckiest son in the world?"

pause 2.0

mom @talkingmouth "So. Should I book you a plane ticket?"

red @sadbrow happymouth "I... I guess so."

mom @happy "Wonderful. It's already done."

red @surprised "Wh-wh-what?!"

mom @angrybrow happymouth "Please. You're my son, and the son of your father. There was never a doubt in my mind that you would spring back up."
mom @talkingmouth "...And if you didn't, it's only a small fee to cancel the flight back."

red @sadbrow happymouth "Geez, Mom. When does it take off?"

mom @talking2mouth "I'm afraid the soonest I could get a flight I could actually afford brings you back on Friday, early in the morning."

red @closedbrow talking2mouth "Well... I'll still be there for the last day of the Quarter Qlashes, then."

mom @talkingmouth "Let's spend tomorrow together. Perhaps we could go out to the beach and fish for a bit. I still have your Old Rod."

red @happy "That piece of junk? All I ever catch with that thing are Magikarp!"

stop music fadeout 10.0

call clearscreens from _call_clearscreens_99
show blank2:
    alpha 0.0
    ease 10.0 alpha 1.0

mom @talkingmouth "True. But you catch Magikarp {i}every time{/i}, don't you?"

red @sadbrow talkingmouth "Guess so..."

mom @talkingmouth "Now, come inside, darling. I've got some meatloaf in the oven. And after that maybe we can kick up our feet and put on a Diantha movie."

scene blank2

show night at vspaz
$ timeOfDay = "Night"

pause 3.5

narrator "You are watching a movie together with your mother. It's an older drama that you've practically memorized every line of at this point."
narrator "Four boys are walking on railroad tracks."

pause 1.0

narrator "Suddenly..."

pause 1.0

$ PlaySound("asteroidwoosh.ogg")

pause 3.0

red @angrybrow talking2mouth "Wait a minute. Do you hear that?"

mom @talkingmouth "Hm? Isn't that just part of the movie?"

red @closedbrow talkingmouth "No, I recognize that sound. It's..."

pause 1.0

$ PlaySound("idea.ogg")

red @surprised "Oh my God!"

mom @closedbrow talking2mouth "Language, dear."

$ PlaySound("impact.ogg")

pause 1.0

mom @angrybrow talking2mouth "What the fuck was that?"

red @surprised "Mom?!"

mom @angrybrow talking2mouth "I swear, if some drunkard fell into our compost heap again..."

scene blank2 with splitfadefast

pause 0.1

scene nightfarmland
show screen currentdate 
with splitfadefast

narrator "You emerge out into the crisp night air, and though the stars and moon light everything up quite clearly enough for you to see, you cannot believe your eyes."

$ renpy.music.queue("Audio/Music/Cinnabar_Start.ogg", channel='music', loop=None, fadein=0.0, tight=None)
$ renpy.music.queue("Audio/Music/Cinnabar_Loop.ogg", channel='music', loop=True, tight=None)

show leaf uniform frownmouth closedbrow at night with Dissolve(3.0)

pause 1.0

narrator "You're completely speechless, as your mind races, trying wildly to come up with some reasonable explanation for Leaf standing in front of you now."

show leaf blush angrybrow frownmouth
show nightfarmland 
with vpunch

leaf @talking2mouth "[first_name]! I'm here to take you back to Kobukan!"

pause 2.0

mom night @playfuleyes angryeyebrows playfulmouth "{size=20}Oh, I definitely need to see this.{/size}"

pause 1.0

leaf @sadbrow talking2mouth "I know it's easier to give up on the world, okay? I get it! But you can't! I never give up, {i}never{/i}, and that means my friends aren't allowed to give up, either!"
leaf @sadbrow talking2mouth "[first_name], I can't even begin to imagine what you were thinking up there. And I should've done something at the time. I should've done {i}more.{/i}" 
leaf @angry "But I'm here now because I care about you! A whole heck of a lot, okay? You're not alone in this, and I want to help you find your way back to Kobukan." 
leaf @talking2mouth "You might think you're alone, and that everyone wants you gone--that's not true!" 
leaf @sadbrow talking2mouth "I talked to Oak! I get what Frienergy is {i}really{/i} about, now. And there's a whole bunch of us who want you back! Me! Tia! Even Blue is helping us, kinda! {w=0.5}...Also Ethan!"
leaf @closedbrow talking2mouth "The point is you haven't been abandoned! Some people probably won't let this go, but... but you... it's your life! And if they don't like you, fuck 'em!"
leaf @talkingmouth "We've done {i}everything{/i} we can, and we've come up with what is honestly a {i}really{/i} solid plan! We can get you back to Kobukan before the Quarter Qlashes."
leaf @angry "But if you're going to get back there in time, you need to leave {i}now!{/i}"

show leaf:
    ease 0.5 ypos 1.2 zoom 1.3

if (HasEvent("Leaf", "RejectedConfession")):
    leaf @talking2mouth "Remember when I asked you for a date and you said no? I said the next time I asked it wouldn't be your choice!"
    leaf @closedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
    leaf @talking2mouth "Well, this part {i}also{/i} isn't your choice! You {i}need{/i} to fulfill your dream, [first_name]! You {i}need{/i} to become a Champion!"
else:
    leaf @talking2mouth "And... and on top of all that... you still owe me a date! And I don't see any malls in Pallet Town!"

leaf @talking2mouth "I'm not taking no for an answer! Because--"

show leaf surprisedbrow frownmouth:
    ease 0.3 ypos 1.0 zoom 1.0

red night @happy "Okay."

pause 1.0

leaf @surprisedbrow talking2mouth "Wh-what?"

red @talkingmouth "Okay."

pause 1.0

leaf -surprisedbrow -frownmouth -surprised @talking2mouth "Um."

leaf @talking2mouth "You're... talking. And you're... agreeing to go? Just like that?"

red @talkingmouth "Yep."

narrator "You cast a quick glance behind yourself, where your mother is hiding behind a barrel near the front door."

pause 1.0

redmind @closedbrow frownmouth "I can't believe Leaf came all the way out here."
redmind @sadbrow frownmouth "The least I can do is not tell her I was already convinced."

leaf @surprised "Oh. {w=0.5}Um. {w=0.5}Okay."

leaf @embarrassedbrow talkingmouth "You're... you're sure you don't want me to say the rest of my speech?"

red @happy "Nah, I think you've covered most of it already."

leaf sadbrow @talking2mouth "Oh."

pause 2.0

leaf -sadbrow -frownmouth @happy "Wait, no, what's your damage, Leaf? This is good! This is good."

red @confused "Quick question? How did you get here?"

leaf @talking2mouth "Oh. Right."

leaf @closedbrow talkingmouth "You can come out now."

pause 1.0

red @talkingmouth "Okay. Leaf, I like men."

leaf @closedbrow talking2mouth "Har-de-har. I'm not talking to you."

red @confused "Then who...?"

show latias at night, rightside behind leaf:
    ypos 1.0
    parallel:
        ease 4.0 xpos 0.77
        ease 4.0 xpos 0.75
        ease 4.0 xpos 0.73
        ease 4.0 xpos 0.75
        repeat
    parallel:
        ease 2.0 ypos 1.0
        ease 2.0 ypos 1.02
        ease 3.0 ypos 1.0
        ease 3.0 ypos 0.98
        repeat
with gaussdissolve

$ PlaySound("pokemon/cries/380.mp3")

latias @happy "Latias!"

pause 3.0

red @confused "This answers none of my questions, and just raises further questions."

leaf @surprised "Really? You don't recognize her?"

leaf @talkingmouth "Oh, wait, I know!"

show leaf behind latias:
    ease 0.5 xpos 0.75

leaf @happy "Here you go, sweetheart! Kept it safe on the ride, just like I said."

show latias at night:
    ease 0.5 ypos 1.4 xpos 0.75
    pause 1.0
    "latias hat"
    matrixcolor nightmatrix
    parallel:
        ease 4.0 xpos 0.77
        ease 4.0 xpos 0.75
        ease 4.0 xpos 0.73
        ease 4.0 xpos 0.75
        repeat
    parallel:
        ease 2.0 ypos 1.0
        ease 2.0 ypos 1.02
        ease 3.0 ypos 1.0
        ease 3.0 ypos 0.98
        repeat

show leaf:
    xpos 0.75
    pause 2.0
    ease 0.5 xpos 0.5

pause 3.0

show leaf surprisedbrow frownmouth
show latias hat surprised
with dis

red @angry "Seriously? Did Tia's hat get stolen {i}again?!{/i}"

show latias sad2eyes lightblush embarrassedmouth with dis

leaf -surprisedbrow -frownmouth -surprised @sarcastic "Uh... no."
leaf @talking2mouth "Maybe you should, um, put up the illusion, sweetie?"

latias @talking2mouth "La."

hide latias
show tia hat at rightside, night
with gaussdissolve

pause 3.0

show leaf happy
show tia happy
with dis

red @surprised "Oh. Oh! Ohhhhh."

pause 2.0

show leaf surprisedbrow frownmouth
show tia surprisedbrow frownmouth
with dis

red @playfuleyes talking2mouth "This answers none of my questions, and just raises further questions."

show tia -surprisedbrow -frownmouth -surprised with dis

leaf -surprisedbrow -frownmouth -surprised @angrybrow talking2mouth "Okay, you really have to go, {i}soon{/i}, so here's the gist: Tia is a powerful Dragon-type Pokémon that can fly to Kobukan before noon tomorrow."

red @surprised "Wh-what? You're a Pokémon?!"

if (GetRelationshipRank("Tia") == 1):
    tia @happy "Yup! I am!"

    red @talking2mouth "But... you can talk! And... and write! And, like... do all kinds of human stuff!"

    tia @happy lightblush "Aw. {font=fonts/sign.ttf}Thank{/font} you! I've been {font=fonts/sign.ttf}trying{/font} really hard. For a {font=fonts/sign.ttf}very{/font} long time."
else:
    narrator "Tia nods happily."

    red @talking2mouth "But... you can talk! And... and write! And, like... do all kinds of human stuff!"

    narrator "Tia begins signing out a complicated sentence, before seeming to realize you couldn't possibly understand it at your current JSL proficiency." 
    
    show tia lightblush sadbrow with dis

    narrator "She simply shrugs and smiles sheepishly."

leaf @talking2mouth "I was pretty surprised, too. I've heard about some Pokémon that use illusions to live as people, and can even talk, but I never thought I'd meet one."

leaf @closedbrow talking2mouth "...And I thought they were Dark-type, anyway."

red night @surprisedeyes talking2mouth "But... there's a Pokémon attending our school! And she's a trainer! And... and... aren't the implications of that massive?"

red @surprisedeyes talking2mouth "Nevermind the fact she's a Pokémon I've never seen before, meaning she {i}must{/i} be a Mythical!"

show tia -lightblush happy with dis

leaf @surprisedbrow talking2mouth "Like, yeah, I get that this is kinda a mind-blowing thing to realize, but there's not much we can do about it right now." 
leaf @talking2mouth "You need to get back to Kobukan, right? And, maybe, when you're there, we can... I dunno, tell Professor Oak about Tia."

show tia sadbrow frownmouth with dis

pause 2.0

show tia happy with dis

leaf @talking2mouth "Or... not?"

pause 1.0

red @talkingmouth "I... okay. Okay. Tia, can you definitely fly us back? You aren't tired or anything?"

if (GetRelationshipRank("Tia") == 1):
    tia @happy "I'm not even a little bit tired!"

else:
    show tia angrybrow with dis:
        xpos 0.75 
        ease 0.5 ypos 1.1
        ease 0.5 ypos 1.0

    pause 2.0

show tia surprisedeyes lightblush with dis

red @talkingmouth "Alright. I trust you."

show tia -surprisedeyes with dis

pause 2.0

show tia surprisedbrow frownmouth:
    ease 0.3 xpos 1.1
show leaf surprisedbrow frownmouth:
    ease 0.5 xpos 0.75

mom @sadbrow talking2mouth "Sweetheart?"

leaf @talking2mouth "Woah! Who's that?"

show mom at leftside, night with dis

red @sadbrow happymouth "That's my Mom."

leaf @talking2mouth "M-m-mom? You're... you're Mrs. [last_name]?"

if (last_name != "Sugimori"):
    mom @happy "Oh, no, no. I'm Ms. Sugimori. Mr. [last_name] was his father."

else:
    mom @happy "{i}Ms.{/i} Sugimori."

leaf @surprised "Oh!"

mom playfuleyes playfulmouth @talkingmouth "And you must be Leaf."

pause 1.0

mom @talkingmouth "I've heard... quite a bit about you."

leaf @sadbrow happymouth "Oh? R-really? Heh, heh... what, uh, what did you hear?"

mom -playfuleyes playfulmouth @happy "Only good things!"
mom @closedbrow talkingmouth "Anyway, it looks like you're going to be quite busy flying soon, so..."

show mom -playfulmouth with dis:
    xpos 0.25
    ease 0.5 xpos 0.5 ypos 1.2 zoom 1.3

mom @tears talkingmouth "I love you, my Champion. It's going to be a difficult time, going back, I'm sure of it. But I know, even more than that, that you can overcome it."
mom @happybrow tears happymouth "You'll always make me proud, no matter what you do."

red @tears "I love you, Mom."

mom @talkingmouth "And I, you."

pause 1.0

show mom angrybrow angrymouth with dis:
    xpos 0.5
    ease 0.5 xpos 0.6 ypos 1.0 zoom 1.0

mom @closedbrow talkingmouth "Oh, and Leaf?"

leaf sadbrow frownmouth @sad "Y-yes?"

mom @talking2mouth "Take care of my boy. He's not used to big cities yet, and there's a lot of people up there who'll try to take advantage of his good nature."

leaf @happymouth "Uh... of-- of course! Hahaha..."

pause 2.0

show mom -angrybrow -angrymouth with dis:
    ease 0.5 xpos 0.25

pause 1.0

mom @thinking "[ellipses]"

mom @closedbrow playfulmouth "Mmm."

pause 1.0

mom @talkingmouth "You two might want to be a bit more discrete about the little dragon girl, if you're trying to keep her a secret."

red @closedbrow sweat talking2mouth "Er... noted."

mom @closedbrow talkingmouth "...Now, I don't want to overstay my welcome between you two, but are you both planning on riding the little dragon girl back to Kobukan?"

red @talkingmouth "I guess so."

leaf embarrassed "Um..."

pause 1.0

red @surprised "What?"

leaf @sadbrow happymouth "...It won't work. We're too heavy, [first_name]."

pause 1.0

red @surprised "Wait. So... you...?"

leaf sadbrow -embarrassed @happymouth "I'm not going back."

red @sadbrow talking2mouth "You... you gave your slot up for me...?"

leaf @talking2mouth "[first_name], I know we only met a month ago, but... I knew this was the right thing to do. I feel... I mean, you, and I, we..."

show leaf surprisedbrow frownmouth blush with dis

mom @closedbrow talkingmouth "None of that, now. There's a simple solution to this."

red @surprised "Huh?"

mom @closedbrow talking2mouth "I'm going to look around in the attic. Don't go anywhere!"

hide mom with dis

pause 2.0

red @talkingmouth "So... what were you going to say?"

leaf -surprisedbrow -frownmouth -surprised @embarrassed "Nothing!"

pause 2.0

show mom at night with dis:
    xpos 0.25

mom @talkingmouth "There, I knew she was around here somewhere."

narrator "In your mother's hand is an old, dusty Poké Ball that you've never seen before."

red @surprised "Mom? What's that?"

mom @talkingmouth "This is a good friend of mine."

$ PlaySound("Pokemon/ball sound.ogg")
$ PlaySound("pokemon/cries/39.mp3")
$ sidemonnum = 39

show leaf surprisedbrow frownmouth with dis

show sideportraitfull at dormdesk, pokeball, night

sidemon @talkingmouth "Jiggaloo!"

pause 1.0

leaf @talking2mouth "Oh my God. She's adorable."

red @surprised "Mom, I didn't know you had a Jigglypuff."

mom @happy "Yes. I raised this darling from an Igglybuff..."
mom @sadbrow talkingmouth "But she'd be another mouth to feed if I let her roam around the house like [pika_name] does. So I'm afraid keeping her in her Poké Ball was the best option I had."
mom @talkingmouth "They don't get hungry in their balls, after all."

pause 1.0

mom @sadbrow talking2mouth "But it's unfair to her to expect her to just live in my attic forever, so I think this would be an excellent opportunity to give you the Jigglypuff."

red @happy "Oh, Mom, I don't--"

mom @talkingmouth "I'm talking to Leaf, sweetheart."

red @surprised "Oh! {size=25}Okay.{/size}"

leaf -surprisedbrow -frownmouth -surprised @sadbrow talking2mouth "Thank you so much, Ms. Sugimori. But I'm not sure how this will help...?"

mom @talkingmouth "Oh, it's quite a simple little trick. My Jigglypuff is especially rubbery, you see. She's like a little gumball."
mom @closedbrow talkingmouth "When you give her the command, she'll inflate, becoming much lighter. In fact, she'll weigh less than nothing."
mom @talkingmouth "When I was a little girl, she used to be able to carry me up in the air... your grandfather used to raise hell about that, [first_name]. He thought Jigglypuff would carry me off."

leaf @surprised "So, if I just... hold Jigglypuff, and she puffs up, we'll be lighter?"

mom @talkingmouth "Yes. Much lighter. Your weight, at least, should be fairly cancelled out."
mom @closedeyes angryeyebrows talking2mouth "Though you'll need to let her take breaks every once in a while to deflate and stretch herself out."

show sideportraitfull at backinpokeball

red @sadbrow happymouth "Mom. Thank you so much."

mom @closedbrow talkingmouth "Well, I didn't want this lovely young woman sacrificing her own shot at Kobukan for you."
mom @talkingmouth "...But I appreciate you were willing to, for my son, Leaf. Believe me when I say I know, better than anybody else, why you would."

$ PlaySound("Get.ogg")

leaf @talking2mouth "...Thanks, Ms. Sugimori. I... I promise I'll take good care of your Jigglypuff."

mom @talkingmouth "Yours, now."
mom @happy "Goodbye, you two. I hope to see you again, soon! Perhaps with... better news, next time."

hide mom with Dissolve(1.0)

show leaf:
    ease 1.0 xpos 0.33

show tia lightblush embarrassedeyes embarrassedmouth:
    ease 1.0 xpos 0.66

pause 1.0

leaf -surprisedbrow -frownmouth -surprised @closedbrow talking2mouth "Okay. We need to get you on Tia. You're bigger than she is, so you'll have to kinda hunch over. Keep your head down, lie as flat as possible, keep your arms around her neck, and--"

red @talking2mouth "Wait. How are you going to fit on?"

leaf @surprised "Well... I think we'll just have to... uh... scooch really close together."

show tia sad 
show leaf surprisedbrow frownmouth 
with dis

red @confused "Even with Jigglypuff, though... I'm not sure Tia's big enough to carry both of us."

show leaf -surprisedbrow -frownmouth -surprised with dis:
    xpos 0.33
    ease 0.5 ypos 1.2 zoom 1.3

leaf @sad "{size=30}Hey, don't say that.{/size}"

red @confused "Huh?"

leaf @talking2mouth "{size=30}Tia thinks the world of you. You're a Pokémon trainer, and she's a Pokémon. If you make her doubt herself, she probably {i}won't{/i} be able to do it!{/size}"
leaf @happy "{size=30}You've got to {i}encourage{/i} her! Cheer her on, and assure her that she'll be fine!{/size}"

red @confused "{size=30}C'mon, will that even make a difference? I'm not exactly in the most motivational mood right now.{/size}"

pause 2.0

leaf @angry "[first_name]. I just flew across an ocean to grab you. Now that I'm here, I {i}have{/i} to fly back, but coming here was voluntary."
leaf @closedbrow talking2mouth "Mostly."
leaf @sarcastic "If you can't muster up the gumption to cheer on the adorable dragon girl who {i}also{/i} flew across an ocean to grab you, then I don't know what to tell you."

red @confused "Adorable dragon girl? You sure turned around on her fast."

show tia surprisedbrow frownmouth with dis

leaf @closedbrow talkingmouth "Yeah, realizing that she wasn't even trying to get into your pants really made me re-evaluate a couple things."

show tia poutmouth angrybrow with dis

if (GetRelationshipRank("Tia") == 1):
    tia @talking2mouth "She thought I was what?!"

    red @sadbrow talkingmouth "Uh, it's a phrase that means--"

    tia @talking2mouth "I know what it means! But you're a human! That's forbidden love!"

    red @closedbrow talking2mouth "Fair, but she didn't know you were a Pokémon, remember?"

    tia @surprised "Oh. Oh, right."

else:
    narrator "Tia huffs indignantly."

red @talkingmouth "Anyway, I get the message."

leaf sadbrow frownmouth @talking2mouth "Alright. We should... we should probably head back."

show leaf:
    ease 0.5 xpos 0.66 ypos 1.0 zoom 1.0

show tia:
    ease 0.5 xpos 0.33

red night @closedbrow talkingmouth "Yeah. Will you two be fine? Neither of you are too tired, or, like, hungry, are you?"

leaf @talking2mouth "My... my stomach is pretty upset, actually... but..."

hide tia
show latias hat at night, leftside:
    xzoom -1
with gaussdissolve

latias @happy "La!"

leaf @angry "Hey! Not again! I can get on you myself, this time!"

latias @playfuleyes playfulmouth "Ti... Tias?"

show leaf:
    ease 1.0 xpos 0.5
    pause 0.5
    ease 1.0 xpos 0.75

show latias at night:
    ease 0.5 ypos 1.3 xpos 0.25
    pause 0.75
    "latias nohat"
    matrixcolor nightmatrix 
    parallel:
        ease 4.0 xpos 0.25
        ease 4.0 xpos 0.27
        ease 4.0 xpos 0.25
        ease 4.0 xpos 0.23
        repeat
    parallel:
        ease 2.0 ypos 1.0
        ease 2.0 ypos 1.02
        ease 3.0 ypos 1.0
        ease 3.0 ypos 0.98
        repeat

red @talkingmouth "Alright. Um, I have some energy bars in my back pocket... it was pretty much all I ate for my first two days back here."

leaf @talking2mouth "...If my stomach ever settles down, I might take you up on that."

pause 1.0

leaf @talking2mouth "Hey... you've still got one thing you need to do, right?"

red @confused "Huh?"

narrator "Leaf nods at your shoulder. Confused, you put your hand up, and realize [pika_name] is on your shoulder--a feeling so familiar you didn't even think about it."

$ renpy.music.play("Audio/Pokemon/pikachu_happy1.ogg", channel="altcry", loop=None)
pikachu night happy "Pika!"

red @happy "Oh, right."

red @sadbrow talking2mouth "Hey, [pika_name]. I know you don't like going in your Poké Ball, but you really need to, okay?"

$ renpy.music.play("Audio/Pokemon/pikachu_scared.ogg", channel="altcry", loop=None)
pikachu surprisedbrow frownmouth @surprised "Pika?!"

red @sad "I get why you don't want to go in. You think that if I can't see you, I'll forget about you."

$ renpy.music.play("Audio/Pokemon/pikachu_sad.ogg", channel="altcry", loop=None)
pikachu sad "Pika..."

red @sad "I promise, buddy, that'll {i}never{/i} happen, okay? You're my friend. Always. I won't--can't--forget about you. So I need you to go back into your Poké Ball for a few hours, alright?" 
red @happy "And then, when we're back at school, if I can somehow resume a normal school life, I'll need you to stay in your Poké Ball so I can bring you to classes, okay?"

$ renpy.music.play("Audio/Pokemon/pikachu_sad2.ogg", channel="altcry", loop=None)
pikachu sad_2 "Pika?"

red @happy "I promise, buddy. Together, forever."

$ renpy.music.play("Audio/Pokemon/pikachu_question.ogg", channel="altcry", loop=None)
pikachu happy "Pika...?"

$ renpy.music.play("Audio/Pokemon/pikachu_angry1.ogg", channel="altcry", loop=None)
pikachu cocky_2b "Pika! Pika!"

show blank

pause 0.05

hide blank

$ PlaySound("sav.ogg")

narrator "[pika_name]'s heart shifts as his relationship with you evolves from '{color=#0048ff}(Slightly) Less-Lazy Rat{/color}' to '{color=#0048ff}Obedient Rat{/color}'!"

red @confusedeyebrows talkingmouth "...Wait, buddy. Did something about you just change?"

$ renpy.music.play("Audio/Pokemon/pikachu_happy1.ogg", channel="altcry", loop=None)
pikachu happy "Pika."

$ freelectricphases.append(2)

narrator "{color=#0048ff}[pika_name] will now patiently wait in his Poké Ball whenever you need him to. (But don't forget to let him out for walkies!){/color}"

red @closedbrow talking2mouth "Alright. And now we have to play stack-the-humans. Let's do this."

leaf @talking2mouth "Right. Come on out, Jigglypuff."

$ PlaySound("pokemon/cries/39.mp3")
$ sidemonnum = 39

sidemon @talkingmouth "Jiggaloo!"

leaf @happy "Cutie! Get in my arms. I've got a really important job for you, okay?"

scene blank2 with Dissolve(2.0)

narrator "You begin the unenviable process of trying to figure out how you and Leaf will both rest on Tia's back." 
narrator "Thankfully, you find that if you sort of sit straight, with your legs in front of Tia's forelegs, you can maintain your balance relatively easily."
narrator "Tia's fur-like feathers seem to suck you in, curling around you and securing your position on her back. Relatively painless, all things considered."

pause 1.0

narrator "...Leaf, however, is a different task altogether."

leaf night uniform @embarrassedbrow surprisedmouth fullblush "Wh-wh-what?! You want me to sit {i}where?!{/i}"

red night @lightblush closedbrow talking2mouth "Look, I'm kinda embarrassed, too, but your two options are being held in Tia's hands, hanging off the bottom, or on my lap. I can't maintain my balance if I scoot forward, and you have a smaller profile, so you should be in the front."

leaf @embarrassed fullblush "But--but--but you--I--I'm not ready! This is such a big step!"

if (HasEvent("Leaf", "RejectedConfession")):
    red @confusedeyebrows playfuleyes talking2mouth "This {i}isn't{/i} a step. We're not even dating, Leaf, remember?"

    red @talking2mouth "Anyway, I don't remember First Base being 'riding a dragon together for eight hours.'"

else:
    red @talkingmouth "I don't remember First Base being 'riding a dragon together for eight hours.'"

leaf @sadbrow talking2mouth "It'll probably be more than eight. I mean, it was eight when it was just me... and although your Mom's Jigglypuff will reduce our weight, I don't know if it'll make up for you."

red @confusedeyebrows talking2mouth "Then we should really get going."
red @happy "C'mon. Don't think about it."

leaf @talking2mouth "I mean... I'm wearing a skirt...?"

red @talkingmouth "So?"

leaf @fullblush angrybrow angrysmilemouth "...Well. F-fine. Fine! I don't care! Why should I care? I've been flirting with you for, like, a month! This is what I want! So, yeah! I don't care!"

narrator "Saying so, Leaf swings a leg over Tia, and mounts her, sitting squarely in your lap as you grab tighter to Tia's neck."

pause 1.0

narrator "A moment later, you suddenly realize why Leaf's choice of attire seemed to matter so much to her."

red @sad2eyes lightblush talking2mouth "Ah. I get it now."

leaf @fullblush angrybrow angrysmilemouth "Oh, {i}do ya?!{/i}"

pause 1.0

red @lightblush closedbrow talking2mouth "Why did you wear a skirt?"

leaf @fullblush angry "I WASN'T THINKING, ALRIGHT?!"

pause 2.0

leaf @closedbrow blush talking2mouth "My only other outfit has an even shorter skirt, and it doesn't have any tights..."

pause 1.0

leaf @angrybrow angrymouth "Tia, why're you taking so long? Can't you start flying?"

pause 1.0

latias night @playfuleyes playfulmouth "Laaaatias...?~"

red @sad2eyes lightblush talking2mouth "Yeah, uh, you can go."

latias @playfuleyes lightblush playfulmouth "La.~"

red @sad "{size=30}Tia. Please go. I can't take much more of this.{/size}"

$ PlaySound("pokemon/cries/380.mp3")

latias @happy "Latititititi!"

$ PlaySound("whoosh.ogg")

narrator "You soar into the sky, Tia chirping merrily. At first, the wind speed is intense, and your teeth chatter from the cold."
narrator "In a moment, though, you begin to see a pale pink shield of light form around you, and you gradually warm up as the land beneath you rushes by at unimaginable speed."

stop music fadeout 1.5
queue music "audio/music/soaringillusions_intro.ogg" noloop
queue music "audio/music/soaringillusions.ogg"

scene stars 
show lightscreen as lightscreen1:
    alpha 1.0
    block:
        ease 12.0 alpha 0.0
        ease 12.0 alpha 1.0
        repeat

show lightscreen as lightscreen2:
    alpha 0.75 xzoom -1
    block:
        ease 14.0 alpha 0.0
        ease 14.0 alpha 1.0
        repeat

show lightscreen as lightscreen3:
    alpha 0.5 yzoom -1
    block:
        ease 16.0 alpha 0.0
        ease 16.0 alpha 1.0
        repeat

show lightscreen as lightscreen4:
    alpha 0.25 xzoom -1 yzoom -1
    block:
        ease 18.0 alpha 0.0
        ease 18.0 alpha 1.0
        repeat
with Dissolve(4.0)

pause 2.0

red night @surprised "Wow. You're really fast, Tia."

latias night @happy "La!"

pause 1.0

leaf uniform night @sadbrow embarrassedmouth "Hm..."

red @confused "{size=30}What? What's wrong?{/size}"

leaf @sadbrow talking2mouth "{size=30}She was much faster when it was just the two of us...{/size}"

#redmind @thinking "...Well, I guess we've gotta throw you overboard."

red @closedbrow talkingmouth "Hm."

pause 2.0

red @sadbrow talkingmouth "Thank you."

leaf @surprised "Huh?"

latias @surprised "Ata?"

red @happy "Thank you so much. I really, {i}really{/i} appreciate what you've done. Both of you."

latias @happy "La!"

leaf @happy "Hey, you would've done the same thing for us."

pause 1.0

redmind @thinking "...Would I have? Would I have flown across an ocean to grab someone I'd have every reason to distrust?"

pause 1.0

redmind @closedbrow frownmouth "I don't know. I don't know how far I'd go for a friend. I'd like to think I'd go to the stars, but..."

narrator "You look up at the stars. They look down at you."

pause 1.0

redmind @closedbrow frownmouth "But I don't know."

red @sadbrow talkingmouth "Hey... Tia?"

latias @surprised "La?"

red @closedeyes sadeyebrows talking2mouth "I'm really sorry for standing you up on Sunday. I'm sure you were really upset, and wondered if you did something wrong."

latias @sad2eyes talking2mouth "La, la..."

red @talkingmouth "So let's spend this time, now, making up for it, right?"

latias @sadbrow happymouth "Tias!"

red @happy "I guess I can probably figure out what you were going to tell me, huh? Wow. A {i}Latias.{/i}"

latias @lightblush talking2mouth "Lat-a."

red @talkingmouth "I never heard of a Pokémon called Latias before. Based on your moves, you're a... Dragon/Psychic type, huh?"

latias @angrybrow happymouth "Latatata!"

red @talkingmouth "I can tell you're really fast. I mean, just look at the ground, right? Zoom!"

latias @happy "Laaaaaa!"

red @angrybrow talkingmouth "But I wonder... just how fast {i}can{/i} you go?"

latias @surprised "Latias?"

red @happyeyes sweat talkingmouth "It's just, uh, we're kinda in a {i}massive{/i} rush, you know? So I'd be really interested in seeing your absolute top speed!" 
red @surprised "Not to the point of, like, hurting yourself, of course."
red @talkingmouth "It's just--you know, we're going so fast already. I'd be {i}really{/i} impressed if you could go even faster!"

latias @surprised "La...?"

$ PlaySound("pokemon/cries/380.mp3")

latias @angrybrow happymouth "Latiiiiiias!"

$ PlaySound("whoosh.ogg")

narrator "Tia flaps her wings as you grab on tighter to her down, and a tremendous tailwind starts to blow from behind, pushing you along at a much faster clip."

pause 2.0

leaf @talkingmouth "Nice going, skippy. Knew you could do it."

red @talkingmouth "...This was part of your plan, too, huh?"

leaf @closedbrow happymouth "Sure, but I'm only admitting that because it worked."

pause 1.0

red @talkingmouth "I'm sorry I ditched you, too."

leaf @blush angrybrow angrysmilemouth "H-hey. Don't apologize for that! That wasn't your fault! That wasn't even {i}close{/i} to your fault."

red @sadbrow happymouth "I'm expressing sympathy, not culpability."

leaf @closedbrow blush talking2mouth "Well... good. Good. Because you did nothing wrong."

red @playfulbrow talking2mouth "I don't know if the rest of the school will agree with you."

leaf @closedbrow talking2mouth "Maybe they won't."
leaf @happy "But that's fine. I know you have a good heart. You'll win them back."

pause 2.0

red @talking2mouth "Why me, Leaf?"
red @closedbrow talking2mouth "Out of all the students in this school, all your friends, why are you going so far for me?"

leaf @sarcastic "Because your mind control powers compel me to, oh dark master."

red @playfulbrow talking2mouth "Excellent, my thrall. You have done well my bidding."

leaf @happy "Dork."

pause 1.0

leaf @closedbrow talkingmouth "Well, first of all, this is {i}nothing{/i} compared to what I'd do for Rosa. If Cheren stood up there and said that {i}she{/i} had mind control powers, I would have stormed the stage and hung, drawn, and quartered him."

red @confusedeyebrows talking2mouth "Graphic."

leaf @talkingmouth "But... serious answer... I don't know. I guess you were my first friend at Kobukan. And I was coming off a bit of a dry spell of having friends, honestly."

red @surprised "Is that right? A popular girl like you?"

leaf @talking2mouth "...To be honest, I wasn't really popular until Kobukan."

red @talking2mouth "Huh."

leaf @happy "I dunno. It's just kinda nice that we've got each other, right? Two people who came here, friendless, and became each other's first friend."

red @happy "Oh, you weren't my first friend."

leaf @surprised "What?!"

red @talkingmouth "Yeah, before I met you, I met Silver, Brawly, and Falkner."

leaf @flirtbrow talking2mouth "Ah, but did they make an Official Friendship Pact{font=fonts/consola_0.ttf}™{/font}?"

red @sweat closedbrow talkingmouth "Can't say they did."

leaf @talkingmouth "Then I'll make one with you, now. To make this official."

pause 1.0

leaf @talkingmouth blush "I, Leaf{w=0.5} Gracidea{w=0.5} Green,{w=0.5} promise to be your friend until the very end.{w=0.5} No matter what.{w=0.5} I will {i}always{/i} be there for you."

pause 2.0

red @talkingmouth "Uh... thanks."

leaf @angrybrow angrymouth "Oi, dork. You're supposed to say one back."

red @closedbrow talkingmouth "{i}Sigh.{/i} Alright, alright."

pause 1.0

if (last_name != "Sugimori"):
    red @talkingmouth "I, [first_name]{w=0.5} Sugimori{w=0.5} [last_name],{w=0.5} promise to be your friend until the very end.{w=0.5} No matter what.{w=0.5} I will {i}always{/i} be there for you."
else:
    red @talkingmouth "I, [first_name]{w=0.5} Sugimori,{w=0.5} promise to be your friend until the very end.{w=0.5} No matter what.{w=0.5} I will {i}always{/i} be there for you."

pause 1.0

leaf @happy bigblush "Cool."

pause 1.0

red @closedbrow talkingmouth "Well... that killed ten minutes. What are we going to do for the next eight hours?"

leaf @sadbrow talking2mouth "It'll... probably be closer to thirteen, actually..."

red @sad2eyes talking2mouth "Sheesh. At least it's faster than the plane."

call clearscreens from _call_clearscreens_100
scene blank2 with Dissolve(4.0)

show youarenolongeryou_bg_red_leaf_tia with Dissolve(3.0)

pause 3.5

hide youarenolongeryou_bg_red_leaf_tia with Dissolve(1.5)

jump day010505
