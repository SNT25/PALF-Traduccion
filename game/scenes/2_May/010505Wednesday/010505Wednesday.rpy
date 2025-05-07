label day010505:
$ timeOfDay = "Morning"

call calendar(1) from _call_calendar_30
$ calDate = calDate.replace(day=5, month=5, year=2004)

show morning at vspaz

pause 3.5

stop music channel "misc"
stop sound channel "misc"
stop music fadeout 1.5

show screen songsplash("Run Away, Fugitives", "Lazy Totodile")

queue music "audio/music/runawayfugitives_start.ogg" noloop
queue music "audio/music/runawayfugitives_loop.ogg"

python:
    playercharacter = "Ethan"

    ethanparty = [Pokemon(172.1, level=max(1, pikachuobj.Level - 1), ivs=[1, 1, 1, 1, 1, 1], evs=[0, 0, 0, 0, 0, 0], gender=Genders.Female, ability="Small World", nature=Natures.Lonely)]
    for mon in oldparty:
        ethanparty.append(Pokemon(mon.Id, level=max(1, mon.Level - 1), ivs=[1, 1, 1, 1, 1, 1], evs=[0, 0, 0, 0, 0, 0], moves=copy.deepcopy(mon.Moves), gender=mon.Gender, ability=mon.Ability))
    playerparty = ethanparty

    HealParty()

    classstats = oldclassstats

    inventory = {
        Item.OldPicture : 1,
        Item.FirstAidKit : 1,
        Item.GSBall : 1,
        Item.ExperienceShare : 1
    }

    personalstats = {
        "Charm" : -3,
        "Knowledge" : 5,
        "Courage" : 3,
        "Wit" : 9,
        "Patience" : 69
    }

    persondex = copy.deepcopy(defaultpersondex)
    persondex["Professor Cherry"] = {"Named" : True, "Value" : 247, "Contact": False, "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [] }
    persondex[first_name] = {"Named" : True, "Value" : oldpersondex["Ethan"]["Value"] * 3, "Contact": False, "Sex": Genders.Male, "Relationship": "Wannabe", "RelationshipRank": 0, "Events": [] }
    persondex["Ethan"]["Named"] = True
    persondex["Blue"]["Named"] = False
    persondex["Yellow"]["Named"] = True

narrator "{color=#ff0000}You are no longer you.{/color}"

scene dorm_A
show screen currentdate
with transeye2

pause 1.0

ethan @tired playfuleyes talking2mouth "That nightmare again..."
ethan @closedbrow talking2mouth "...God, I can't believe I'm actually going to try and make it happen {i}on purpose.{/i}"

show calem at leftside
show brendan frownmouth at rightside
show hilbert
with dis

calem @talkingmouth "Ethan. You're up early. What are you trying to make happen?"

ethan @closedbrow talking2mouth "Oh, nothing important."

calem @closedbrow talkingmouth "Hm."

ethan @talkingmouth "So... just out of curiosity... if there was any chance that {nw}"

show hilbert surprisedbrow frownmouth
show calem surprisedbrow frownmouth
show brendan surprisedbrow frownmouth 
with dis

extend @talkingmouth " [first_name] came back, would you, uh, want him?"

show hilbert -surprisedbrow -frownmouth -surprised
show calem -surprisedbrow -frownmouth -surprised
show brendan -surprisedbrow -frownmouth -surprised 
with dis

if (mayhaslarvesta):
    brendan @sad "Of course, bro! What happened to [first_name] up on that stage was seriously effed up. He should've had a chance to say something, or..."

    brendan @closedbrow talking2mouth "Man, I dunno about his freaky powers or anything like that. Maybe they're real, maybe they're not. But I know for a fact that he's a good dude. Of course I'd want him back."

else:
    brendan @talking2mouth "...He seemed like a nice dude, but I just can't get over that time he took that Larvesta egg. It's my fault for not bein' strong enough to stop him, I guess, but..."

    brendan @sad "I dunno, was that the true [first_name] all along?"

if (oldpersondex["Hilbert"]["RelationshipRank"] == 1):
    hilbert @sadbrow talkingmouth "I don't understand him. He was... kind."

hilbert @talkingmouth "But to have this power all along... If I had such a power, I would use it. I cannot comprehend the kind of person who wouldn't. And I cannot welcome back anyone who would."

pause 1.0

ethan @confusedeyebrows talking2mouth "Calem?"

calem @angry "It's Calem, and..."

pause 1.0

calem @sad "I don't know. I just don't know. If his powers exist, then... no? But if his powers {i}do{/i} exist, then do I not have a duty to be a true friend?"
calem @sad "Does he require redemption, or is he innocent? Can my reputation persist through his association? Does it matter? What is the greater good in this case?"
calem @closedbrow talking2mouth "I don't know. ...And, I suppose, it doesn't matter."

ethan @confusedeyebrows talking2mouth "Huh?"

calem @talkingmouth "Well... Serena and I have been talking. We took a close look at our relationship, and how it has evolved, and we have... well, we've decided to take up in a dorm together."

ethan @surprised "What? That's allowed?"

calem @angrybrow talking2mouth "Really, Ethan, you should try to pay more attention to what's going on around you." 
calem @talkingmouth "Yes, the Student Council had a meeting yesterday where they announced that co-ed dorms are being allowed."
calem @happy "Serena's campaigning was not in vain, it seems. Though we won't be able to be the Student Council members we hoped to be, the popularity of our positions was made apparent to the Student Council."

pause 1.0

calem @talkingmouth "I suppose that one could say a 'good thing' came out of this mess, after all."

brendan @sadbrow talking2mouth "Damn. I didn't know how to say this, but... I was also planning on leaving the dorm, guys."

calem surprisedbrow frownmouth @surprised "Hm?"

brendan @talking2mouth "Yeah, uh, I really think I should spend more time with May. She's been pretty broken up about... a couple things... ever since the election, and she needs me."

hilbert @talkingmouth "I'm leaving, too."

brendan @surprised "Dude?"

hilbert @talkingmouth "I forgot, briefly, how stacked against me--against us--the odds were. There's no time for 'friends' or 'camaraderie'. Not if we want to fulfill our dreams."

brendan sadbrow @sad "That doesn't mean you have to leave, though!"

show calem sadbrow with dis

hilbert @sadbrow talkingmouth "You... you all dragged me into your lives. I... don't want to be a part of them. You don't want me to be a part of them. Just focus on graduating on time. Live your small dreams."

hide hilbert with dis

pause 1.0

ethan @sad "So... Dorm 151 is splitting up, huh?"

calem @talkingmouth "...So it would seem."

pause 1.0

show brendan surprisedbrow frownmouth
show calem surprisedbrow frownmouth
with dis

ethan @playfulbrow talking2mouth "...Welp. It's been fun."

scene blank2 with splitfadefast

pause 1.0

$ PlaySound("Door_Slam.ogg")

pause 1.0

ethanmind @closedbrow frownmouth "Don't take it so personally. It's not like they're leaving to get away from you."

pause 1.0

ethanmind @sadbrow frownmouth "...I wasn't even part of their thought process."

scene hall_A
show blue frownmouth at leftside
show yellow neutralhat frownmouth at rightside
with splitfade

ethan @talkingmouth "[blue_name]? Yellow?"

yellow @happy "Good morning, Ethan!"

blue @talkingmouth "Good, you're up."
blue @angrybrow talkingmouth "I want to know what your plan for getting the Disciplinary Committee off my back is."

ethan @closedbrow talking2mouth "Geez. I told Leaf--"

show yellow surprisedbrow frownmouth with dis

blue @angrybrow talkingmouth "I know what you told {i}Leaf.{/i} I'm {i}not{/i} Leaf. It's {i}my{/i} ass on the line, and I don't want you to screw it up."

show yellow happy with dis

ethan @confusedeyebrows talkingmouth "Flattered, but I don't even see you that way."

show yellow -happy with dis

blue @surprised "What? What are you--"
blue @angry "Oh, shut up! Just tell me what your damn plan is!"

ethan @closedbrow talking2mouth "{i}Sigh.{/i}"
ethan @sad2eyes talking2mouth "Fine."

show blank2 with dis

narrator "You convey the details of your plan. Blue nods, once or twice, but doesn't say anything."

show blue closedbrow

hide blank2 with dis

pause 1.0

blue "{w=0.5}.{w=0.5}.{w=0.5}."

blue @talkingmouth "Yellow, what do you think?"

yellow @surprised "Oh? Me? Um..."
yellow @happy "I think it's a great plan."
yellow @sadbrow talkingmouth "It's... a bit dangerous, though..."

ethan @talking2mouth "Can't really be avoided. We {i}are{/i} trying to break the rules, after all."

yellow @talkingmouth "Well... I don't know anything about this 'Frienergy' power... but if your power can do what you say it can, then I think this plan will work."

ethan @talkingmouth "Cool. Kinda figured you'd say something like 'that's the stupidest plan I've ever heard.'"

blue @angrybrow talkingmouth "Tch. Believe me, if you get the Disciplinary Committee on my ass, I'll say something {i}much{/i} stronger than that."

show blue:
    ease 0.5 xpos 1.1

blue @happy "Smell ya later!"

pause 1.0

ethan @confused "Aren't you going, Yellow?"

yellow @talkingmouth "Yes. I just thought... um... Bea, I heard her say that she found a cave in the mountains."

ethan @closedbrow talking2mouth "Oh, you think there might be some tough Pokémon there, huh?"

yellow @happy "Yeah! I, uh, told Blue about it a couple days ago... but he didn't bite."

ethan @talkingmouth "Alright. Thanks for letting me know."

yellow @talking2mouth "Bye, Ethan."

hide yellow with dis

ethan @happy "Bye, Yellow."

pause 1.0

ethanmind "What a nice girl. Shame she's always hanging around Blue."
ethanmind @thinking "That kind of awful taste can't be forgiven."
ethanmind @sad2eyes lightblush frownmouth "Though I'm one to talk."

ethan @closedbrow talking2mouth "Alright. Classes are on pause for the Quarter Qlashes, so... I guess I might as well start now. It'll be a long walk."

narrator "You quickly peek out the window. The mountains beyond the fields are just barely visible beneath a thick, grey, cloud line. The journey looks like it'll be dismal and wet."

ethan @playfuleyes talking2mouth "{i}Perfect.{/i}"

scene clouds:
    yalign 0.75
    ease 5.0 yalign 0.5
show fields1:
    xalign 0.0
    ease 10.0 yalign 0.33 xalign 0.95
with splitfade

python:
    hascyclizar = False
    for mon in playerparty:
        if (mon.GetId() == pokedexlookupname("Cyclizar", DexMacros.Id)):
            hascyclizar = True
            break

if (hascyclizar):
    narrator "After a bit of bribing, begging, and nagging, your Cyclizar agrees to let you mount it, and begin the journey up the mountain."

else:
    $ AddEvent("Ethan", "Spent200")
    if (money >= 200):
        $ money -= 200
        narrator "After requesting the assistance of one of the school's Ride Cyclizar (and paying $200), you mount it, and begin the journey up the mountain."
    else:
        narrator "After requesting the assistance of one of the school's Ride Cyclizar (and promising to pay $200, when you have it), you mount it, and begin the journey up the mountain."  

$ sidemonnum = pokedexlookupname("Cyclizar", DexMacros.Id)

sidemon @talkingmouth "Cycliz! Cyclizar!"

ethan @playfulbrow talking2mouth "Yeah, you said it, buddy. This is going to be a nightmare."

call clearscreens from _call_clearscreens_101
scene blank2 with splitfade

pause 3.5

narrator "{color=#c1861e}You are no longer you.{/color}"

pause 2.0

stop music fadeout 1.5

show screen songsplash("Pallet Town", "Zame")
queue music "audio/music/palletpiano.ogg"

python:
    playercharacter = "Blue"

    #overwriting money, party, inventory, personalstats, and persondex
    playerparty = GetTrainerTeam("Blue")

    inventory = {
        Item.PokeBall : 27,
        Item.GreatBall : 13,
        Item.UltraBall : 4,
        Item.Potion : 9,
        Item.ParalyzeHeal : 4,
        Item.Awakening : 2,
        Item.Antidote : 4,
        Item.BurnHeal : 1,
        Item.IceHeal : 1,
        Item.DragonFang : 2,
        Item.SharpBeak : 2,
        Item.MiracleSeed : 1,
        Item.MysticWater : 1,
        Item.Charcoal : 1,
        Item.PictureofDaisy : 1,
        Item.DadsCoin : 1,
        Item.MomsWatch : 1,
        Item.HandMirror : 1
    }

    personalstats = {
        "Charm" : 4,
        "Knowledge" : 3,
        "Courage" : 38,
        "Wit" : -3,
        "Patience" : 7
    }

    persondex = copy.deepcopy(defaultpersondex)
    persondex["Gramps"] = {"Named" : True, "Value" : 82, "Contact": True, "Sex": Genders.Male, "Relationship": "Grandson", "RelationshipRank": 0, "Events": [] }
    persondex["Yellow"] = {"Named" : True, "Value" : 12, "Contact": True, "Sex": Genders.Female, "Relationship": "Partner", "RelationshipRank": 0, "Events": [] }
    persondex[first_name] = {"Named" : True, "Value" : oldpersondex["Blue"]["Value"], "Contact": True, "Sex": Genders.Male, "Relationship": ("Rival" if oldpersondex["Blue"]["RelationshipRank"] == 0 else "Talker"), "RelationshipRank": 0, "Events": [] }
    persondex["Nate"] = {"Named" : True, "Value" : 58, "Contact": True, "Sex": Genders.Male, "Relationship": "Dormmate", "RelationshipRank": 0, "Events": [] }
    persondex["Cheren"] = {"Named" : True, "Value" : 1, "Contact": True, "Sex": Genders.Male, "Relationship": "Dormmate", "RelationshipRank": 0, "Events": [] }
    persondex["Leaf"] = {"Named" : True, "Value" : 7, "Contact": True, "Sex": Genders.Female, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }
    persondex["Sonia"] = {"Named" : True, "Value" : 4, "Contact": True, "Sex": Genders.Female, "Relationship": "Underclassman", "RelationshipRank": 0, "Events": [] }
    persondex["Hilbert"] = {"Named" : True, "Value" : 9, "Contact": True, "Sex": Genders.Male, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }
    persondex["Silver"] = {"Named" : True, "Value" : 14, "Contact": True, "Sex": Genders.Male, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }
    persondex["Bea"] = {"Named" : True, "Value" : 23, "Contact": True, "Sex": Genders.Female, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }
    persondex["Erika"] = {"Named" : True, "Value" : 4, "Contact": True, "Sex": Genders.Female, "Relationship": "Enemy", "RelationshipRank": 0, "Events": [] }
    persondex["Janine"] = {"Named" : True, "Value" : 31, "Contact": True, "Sex": Genders.Female, "Relationship": "Mentee", "RelationshipRank": 0, "Events": [] }
    persondex["Ethan"] = {"Named" : True, "Value" : 1, "Contact": True, "Sex": Genders.Male, "Relationship": "He's there?", "RelationshipRank": 0, "Events": [] }
    persondex["Dawn"] = {"Named" : True, "Value" : 5, "Contact": True, "Sex": Genders.Female, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }
    persondex["Instructor Winona"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [] }
    persondex["Instructor Clair"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [] }
    persondex["Alder"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [] }
    persondex["Bruno"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [] }
    persondex["Skyla"] = {"Named" : True, "Value" : 2, "Contact": True, "Sex": Genders.Female, "Relationship": "Antihero", "RelationshipRank": 0, "Events": [] }
    persondex["Misty"] = {"Named" : True, "Value" : 2, "Contact": True, "Sex": Genders.Female, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }
    persondex["Flannery"] = {"Named" : True, "Value" : 4, "Contact": True, "Sex": Genders.Female, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }
    persondex["Lance"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Male, "Relationship": "Mentee", "RelationshipRank": 0, "Events": [] }
    persondex["Calem"] = {"Named" : True, "Value" : 7, "Contact": True, "Sex": Genders.Male, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }
    persondex["Tia"] = {"Named" : True, "Value" : 9, "Contact": True, "Sex": Genders.Female, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }

    classstats = { 
        "Normal" : 24,
        "Fire" : 18,
        "Water" : 19,
        "Grass" : 23,
        "Electric" : 2,
        "Ice" : 11,
        "Fighting" : 13,
        "Poison" : 12,
        "Ground" : 16,
        "Flying" : 27,
        "Psychic" : 12,
        "Bug" : 14,
        "Rock" : 11,
        "Ghost" : 9,
        "Dark" : 13,
        "Dragon" : 28,
        "Steel" : 12,
        "Fairy" : 11
    }

    GetTrainerTeam("Blue", "Eevee").Item = Item.SootheBell
    GetTrainerTeam("Blue", "Magikarp").Item = Item.ExperienceShare

scene colosseum
show screen currentdate 
show yellow neutralhat
with splitfade

pause 1.0

blue @closedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}.This is a goddamn nightmare."
blue @surprised "Where are they?"

yellow @happy "It's still the morning, Blue. People probably aren't going to show up for a few hours."

blue @angrybrow talkingmouth "Gah. I hate waiting."

yellow @talkingmouth "...I like it."

blue @surprised "What?"

yellow @happy "Waiting. I like it."

blue @closedbrow talkingmouth "Of course you do. You don't like battles, so it makes perfect sense that you'd like waiting.{w=0.5} {i}Contrarian.{/i}"

yellow @angrybrow talking2mouth "...I think you just don't like waiting because you're not good at it."

blue @surprised "What?"

yellow @happy "You can't sit still, can you? You always want to be {i}doing{/i} something."

blue @angry "And what the hell is wrong with that?!"

yellow @talkingmouth "Nothing. But self-awareness helps you overcome your challenges."

blue @surprised "...You saying I'm challenged?"

yellow @angrybrow talkingmouth "Blue..."

blue @closedbrow talkingmouth "Fine, maybe I was looking for a fight that time."

pause 1.0

blue @angrybrow talkingmouth "Still. This is bullshit. I can't believe I'm putting my ass on the line to help {i}Leaf{/i} get her boyfriend--who I hate--back."

yellow @talkingmouth "Do you hate him?"

blue @surprised "Huh?"

yellow @talking2mouth "I don't think you really hate him, Blue. I think you're jealous of him, and afraid that he'll hate you for what you did back in High School."
yellow @closedbrow talkingmouth "So, to avoid being caught flat-footed, you act like you can't stand him."

pause 1.0

blue @angrybrow talkingmouth "{i}Thank you for your opinion.{/i}"

pause 1.0

yellow @closedbrow talkingmouth "Maybe I'm wrong."

blue @angry "Yeah, that's probably the safer bet."

pause 1.0

blue @talkingmouth "Do you think this school can ever go back to normal? I mean, if [first_name] comes back?"

pause 1.0

yellow @closedbrow talking2mouth "Hm... I don't know."
yellow @talkingmouth "But I think it could become better."
yellow @sadbrow talkingmouth "Saturday was... an awful day. A lot of people were hurt."
yellow @talkingmouth "But it also meant that a lot of people had to confront their secrets, you know? A lot of unhappy situations that people were willing to just 'live with' have come into light."

pause 1.0

yellow @talkingmouth "There's never been a better time to come clean to [first_name] about High School."

blue @surprised "Oh, yeah? But why the hell would I want to do that?"

yellow @talkingmouth "You feel guilty, Blue."

pause 1.0

show yellow angrybrow frownmouth with dis

blue @closedbrow talkingmouth "No I don't."

pause 2.0

yellow -angrybrow @closedbrow talkingmouth "Whatever, Blue. I'm your friend. Not your mother."

pause 1.0 

yellow sadbrow @talkingmouth "But I hope, one day, I can convince you to be honest with yourself."

blue @closedbrow talkingmouth "Yeah, dream on."

scene blank2 with splitfade

pause 3.5

stop music fadeout 1.5
queue music "audio/music/soaringillusions_intro.ogg" noloop
queue music "audio/music/soaringillusions.ogg"

python:
    playercharacter = "Leaf"

    playerparty = GetTrainerTeam("Leaf")

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

pause 1.0

narrator "You are, however, having a pleasant dream. The soft feathers underneath tickle your nose and shift slightly as you begin to wake."

show sky:
    alpha 0.0 yalign 1.0 xalign 0.2 zoom 1.25
    parallel:
        ease 1.0 alpha 1.0
    parallel:
        ease 30.0 xalign 1.0

show clouds1 as base1:
    xpos -200 ypos 100 alpha 0.0
    block:
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 12.0 xpos 2000
        parallel:
            pause 11.0
            linear 1.0 alpha 0.0
show clouds2 as base2:
    xpos -800 ypos 400 alpha 0.0
    block:
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 8.0 xpos 1000
        parallel:
            pause 7.0
            linear 1.0 alpha 0.0
show clouds3 as base3:
    xpos -400 ypos 0 alpha 0.0
    block:
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 10.0 xpos 2200
        parallel:
            pause 9.0
            linear 1.0 alpha 0.0

show clouds1 as set1:
    xpos -1800 ypos 100 alpha 0.0
    block:
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 15.0 xpos 1800
        parallel:
            pause 14.0
            linear 1.0 alpha 0.0
            pause 1.0
            xpos -1500
        repeat
show clouds2 as set2:
    xpos -1700 ypos 100 alpha 0.0
    block:
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 12.0 xpos 2200
        parallel:
            pause 11.0
            linear 1.0 alpha 0.0
            pause 1.0
            xpos -1400
        repeat
show clouds3 as set3:
    xpos -2100 ypos 0 alpha 0.0
    block:
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 17.0 xpos 2200
        parallel:
            pause 16.0
            linear 1.0 alpha 0.0
            pause 1.0
            xpos -1800
        repeat
show clouds1 as set4:
    xpos -1700 ypos -100 alpha 0.0
    pause 5.0
    block:
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 6.0 xpos 1800
        parallel:
            pause 5.0
            linear 1.0 alpha 0.0
            pause 1.0
            xpos -1400
        repeat
show clouds2 as set5:
    xpos -1900 ypos 500 alpha 0.0
    pause 6.0
    block:
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 8.0 xpos 2200
        parallel:
            pause 7.0
            linear 1.0 alpha 0.0
            pause 1.0
            xpos -1700
        repeat
show clouds3 as set6:
    xpos -2100 ypos -50 alpha 0.0
    pause 5.0
    block:
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 20.0 xpos 2200
        parallel:
            pause 19.0
            linear 1.0 alpha 0.0
            pause 1.0
            xpos -1900
        repeat
show clouds2 as set7:
    xpos -1900 ypos 200 alpha 0.0
    pause 4.0
    block:
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 10.0 xpos 2200
        parallel:
            pause 9.0
            linear 1.0 alpha 0.0
            pause 1.0
            xpos -1700
        repeat
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
with splitfade

$ renpy.pause(1.5, hard=True)

leaf uniform "{size=30}Uh...?{/size}"

pause 2.0

red @happy "Good morning, sleepyhead!"

leaf @surprised "{size=30}What?{/size}"
leaf @fullblush surprised "{size=40}WHAT?!{/size}"

show sky with vpunch

$ PlaySound("pokemon/cries/380.mp3")

latias @sweat surprised "La-- la, lati!"

red @surprised "Woah, woah! Don't rock the dragon!"

narrator "As the haze of sleep leaves your mind, you suddenly remember what the situation is."

leaf @surprised bigblush "Oh... right, right! We're on Tia, flying across the ocean. I..."
leaf @fullblush embarrassed "I thought we... were in bed..."

if ("RejectedConfession" in oldpersondex["Leaf"]["Events"]):
    red @playfuleyes talking2mouth "Once again: {w=0.5}we are not dating."

    leaf @flirttalk "We {i}definitely were{/i} in the dream I was having."

    red @sad2eyes talking2mouth "I don't know how to respond to that."

else:
    red @happy "Before our first date? That's pretty fast."

    leaf @blush "Well, you {i}are{/i} a runner."

    red @winkeyes talkingmouth "Yeah, but I'm built for endurance, not speed."

pause 1.0

leaf @surprised "Wait, does that mean I fell asleep on Tia's back?"

red @talkingmouth "It makes sense. You were awake for an eight-hour flight before you picked me up, and we've been flying for..."

narrator "[first_name] looks helplessly at his wrist, as though he expected a watch to be there."

red @happy "Hey, Tia! What's the time?"

latias @happy "La! La! La! La! La! La! La! La! La! La!"

red @happy "That means ten."

leaf @talking2mouth "Huh. That makes two people I know who can speak Pokémon."

red @confused "Two? Who's the second?"

leaf @talking2mouth "Really? She's Blue's friend, so I figured you'd know her."

red @confused "I'm just baffled that [blue_name] has friends."

leaf @talking2mouth "...You know, he's not {i}that{/i} bad."

red @playfulbrow talkingmouth "I literally cannot remember the last time he said something to me that wasn't a command or an insult."

if (oldpersondex["Blue"]["RelationshipRank"] == 1):
    red @closedbrow talkingmouth "Wait, that's not true. I actually {i}do{/i} remember this. He told me that I was a good 'listener', and I had permission to listen to his rants."

    red @playfulbrow talkingmouth "So, yeah, not much improvement."

leaf @talking2mouth "Whatever. Anyway, his friend's name is Yellow."

show sky with vpunch

red @surprised "YELLOW?!"

leaf @surprised "Huh? You recognize the name?"

red @happy "Nope, not at all!"

leaf @angrybrow angrymouth "{w=0.5}.{w=0.5}.{w=0.5}."

latias @angrybrow poutmouth "{w=0.5}.{w=0.5}.{w=0.5}."

red @sweat talkingmouth "Sorry. Just trying to lighten the mood."
red @sadeyebrows sad2eyes talking2mouth "We've been flying for... {i}quite{/i} a while... and it's driving me a little bit crazy."

leaf frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
leaf @angrybrow happymouth "I know how to make the time pass faster."

red @confusedeyebrows angryeyes talking2mouth "I do {i}not{/i} like your expression right now."

leaf @talking2mouth "It's fine, my Dad used to sing this song all the time when we went boating!"
leaf @happy "Ohhhhhh!~ Ninety-nine bottles of beer on the wall! Ninety-nine bottles of beer! Take one down, pass it around, ninety-eight bottles of beer on the wall!"

red @noshine shadow noeyes frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

leaf @angrybrow happymouth "C'mon, Tia, join in!"

latias @happy "Lati!~ Lati-la lati la tias la ti la!"

redmind @noshine shadow noeyes frownmouth "I could be fishing right now."

call clearscreens from _call_clearscreens_102
show blank2 with splitfade

red @noshine shadow noeyes frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

pause 3.5

stop music fadeout 1.5
stop sound channel "misc"

show screen songsplash("Run Away, Fugitives", "Lazy Totodile")

queue music "audio/music/runawayfugitives_start.ogg" noloop
queue music "audio/music/runawayfugitives_loop.ogg"

python:
    playercharacter = "Ethan"

    ethanparty = [Pokemon(172.1, level=max(1, pikachuobj.Level - 1), ivs=[1, 1, 1, 1, 1, 1], evs=[0, 0, 0, 0, 0, 0], gender=Genders.Female, ability="Small World", nature=Natures.Lonely)]
    for mon in oldparty:
        ethanparty.append(Pokemon(mon.Id, level=max(1, mon.Level - 1), ivs=[1, 1, 1, 1, 1, 1], evs=[0, 0, 0, 0, 0, 0], moves=copy.deepcopy(mon.Moves), gender=mon.Gender, ability=mon.Ability))
    playerparty = ethanparty

    classstats = oldclassstats

    inventory = {
        Item.OldPicture : 1,
        Item.FirstAidKit : 1,
        Item.GSBall : 1,
        Item.ExperienceShare : 1
    }

    personalstats = {
        "Charm" : -3,
        "Knowledge" : 5,
        "Courage" : 3,
        "Wit" : 9,
        "Patience" : 69
    }

    persondex = copy.deepcopy(defaultpersondex)
    persondex["Professor Cherry"] = {"Named" : True, "Value" : 247, "Contact": False, "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [] }
    persondex[first_name] = {"Named" : True, "Value" : oldpersondex["Ethan"]["Value"] * 3, "Contact": False, "Sex": Genders.Male, "Relationship": "Wannabe", "RelationshipRank": 0, "Events": [] }
    persondex["Ethan"]["Named"] = True
    persondex["Blue"]["Named"] = False
    persondex["Yellow"]["Named"] = True

narrator "{color=#ff0000}You are no longer you.{/color}"

scene clouds:
    yalign 0.75
    ease 5.0 yalign 0.5
show fields2
show screen currentdate
with splitfade

ethan @shadow angryeyebrows frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

$ sidemonnum = pokedexlookupname("Cyclizar", DexMacros.Id)

$ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))

sidemon @talkingmouth "Cyclizar?"

ethan @shadow angryeyebrows talking2mouth "Keep going."

sidemon @talkingmouth "Cy..."

narrator "As you travel alone up the long path to the mountain, your thoughts turn darker."

ethan @shadow closedbrow talking2mouth "...Geez."

narrator "Your ever-present nightmare swims to the surface of your consciousness. Though the shades are unclear, and the memories are unformed, the emotions they carry with them burn brightly."

pause 1.0

show blank2:
    alpha 0.0
    ease 5.0 alpha 0.2

narrator "{i}Acceptance.{/i} A feeling of belonging, of happiness, of having found yourself."

show blank2:
    alpha 0.2
    ease 5.0 alpha 0.4

narrator "{i}Depression.{/i} You received some sort of bad news. Something you hated to hear, that shattered your happy feelings of acceptance."
narrator "Perhaps it wasn't news at all, but an inevitability you had happily ignored. It is unclear."

show blank2:
    alpha 0.4
    ease 5.0 alpha 0.6

narrator "{i}Bargaining.{/i} You fought, desperately, to prevent the inevitability from occuring. This earth-shattering occurrence could not be allowed to pass."
narrator "For everything within your power, you brought it to bear to stop this disaster. You begged, lied, bribed, cheated, and did it all over again."
narrator "But no bargain could assuage so high a price."

show blank2:
    alpha 0.6
    ease 5.0 alpha 0.8

narrator "{i}Anger.{/i} A red, hot, furious flame that erupted out of you as in a firey roar."
narrator "Your rage burned, uncontrolled and wild. The flames spread in all directions, scorching the world. It acted without direction, without cause, destroying all for the sake of equality."
narrator "And so the flames burned out."

show blank2:
    alpha 0.8
    ease 5.0 alpha 1.0

narrator "{i}Denial.{/i} After the flames left naught but ash, what was there left to do but feel the loss? Grief's blade granted you one mercy--with surgical precision, it allowed you to deny your pain."
narrator "...The subconscious mind is not so easily deceived, though. And it's all too happy to remind you, every night, of what you deny. Of the true influence of your powers."

scene icepath 
show blank2

pause 1.0

hide blank2 with transeye2

ethan @talking2mouth "{i}Sigh...{/i} [first_name] better appreciate the hell out of this."

pause 1.0

$ PlaySound("pokemon/cries/38.mp3")

pause 2.0

ethan @closedbrow talkingmouth "Hm... what was that? Sounded like it was coming from..."

ethan @surprised "Oh, that must be the cave Yellow told me about!"

if (not hascyclizar):
    ethan @talking2mouth "Cyclizar, stay here. Don't get attacked by any Ice-types, okay?"

    $ sidemonnum = pokedexlookupname("Cyclizar", DexMacros.Id)
    $ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))
    sidemon "Cyclizar!"

ethanmind @angrybrow frownmouth "Okay. You know how to do this. Just... let go. Go crazy."

call clearscreens from _call_clearscreens_103
scene blank2 with splitfade

pause 3.5

narrator "{color=#c1861e}You are no longer you.{/color}"

pause 2.0

stop music fadeout 1.5

show screen songsplash("A Rival Appears!", "Zame")
queue music "audio/music/rivalchill_start.ogg" noloop
queue music "audio/music/rivalchill_loop.ogg"

python:
    playercharacter = "Blue"

    #overwriting money, party, inventory, personalstats, and persondex

    playerparty = GetTrainerTeam("Blue")

    inventory = {
        Item.PokeBall : 27,
        Item.GreatBall : 13,
        Item.UltraBall : 4,
        Item.Potion : 9,
        Item.ParalyzeHeal : 4,
        Item.Awakening : 2,
        Item.Antidote : 4,
        Item.BurnHeal : 1,
        Item.IceHeal : 1,
        Item.DragonFang : 2,
        Item.SharpBeak : 2,
        Item.MiracleSeed : 1,
        Item.MysticWater : 1,
        Item.Charcoal : 1,
        Item.PictureofDaisy : 1,
        Item.DadsCoin : 1,
        Item.MomsWatch : 1,
        Item.HandMirror : 1
    }

    personalstats = {
        "Charm" : 4,
        "Knowledge" : 3,
        "Courage" : 38,
        "Wit" : -3,
        "Patience" : 7
    }

    persondex = copy.deepcopy(defaultpersondex)
    persondex["Gramps"] = {"Named" : True, "Value" : 82, "Contact": True, "Sex": Genders.Male, "Relationship": "Grandson", "RelationshipRank": 0, "Events": [] }
    persondex["Yellow"] = {"Named" : True, "Value" : 12, "Contact": True, "Sex": Genders.Female, "Relationship": "Partner", "RelationshipRank": 0, "Events": [] }
    persondex[first_name] = {"Named" : True, "Value" : oldpersondex["Blue"]["Value"], "Contact": True, "Sex": Genders.Male, "Relationship": ("Rival" if oldpersondex["Blue"]["RelationshipRank"] == 0 else "Talker"), "RelationshipRank": 0, "Events": [] }
    persondex["Nate"] = {"Named" : True, "Value" : 58, "Contact": True, "Sex": Genders.Male, "Relationship": "Dormmate", "RelationshipRank": 0, "Events": [] }
    persondex["Cheren"] = {"Named" : True, "Value" : 1, "Contact": True, "Sex": Genders.Male, "Relationship": "Dormmate", "RelationshipRank": 0, "Events": [] }
    persondex["Leaf"] = {"Named" : True, "Value" : 7, "Contact": True, "Sex": Genders.Female, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }
    persondex["Sonia"] = {"Named" : True, "Value" : 4, "Contact": True, "Sex": Genders.Female, "Relationship": "Underclassman", "RelationshipRank": 0, "Events": [] }
    persondex["Hilbert"] = {"Named" : True, "Value" : 9, "Contact": True, "Sex": Genders.Male, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }
    persondex["Silver"] = {"Named" : True, "Value" : 14, "Contact": True, "Sex": Genders.Male, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }
    persondex["Bea"] = {"Named" : True, "Value" : 23, "Contact": True, "Sex": Genders.Female, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }
    persondex["Erika"] = {"Named" : True, "Value" : 4, "Contact": True, "Sex": Genders.Female, "Relationship": "Enemy", "RelationshipRank": 0, "Events": [] }
    persondex["Janine"] = {"Named" : True, "Value" : 31, "Contact": True, "Sex": Genders.Female, "Relationship": "Mentee", "RelationshipRank": 0, "Events": [] }
    persondex["Ethan"] = {"Named" : True, "Value" : 1, "Contact": True, "Sex": Genders.Male, "Relationship": "He's there?", "RelationshipRank": 0, "Events": [] }
    persondex["Dawn"] = {"Named" : True, "Value" : 5, "Contact": True, "Sex": Genders.Female, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }
    persondex["Instructor Winona"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [] }
    persondex["Instructor Clair"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [] }
    persondex["Alder"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [] }
    persondex["Bruno"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [] }
    persondex["Skyla"] = {"Named" : True, "Value" : 2, "Contact": True, "Sex": Genders.Female, "Relationship": "Antihero", "RelationshipRank": 0, "Events": [] }
    persondex["Misty"] = {"Named" : True, "Value" : 2, "Contact": True, "Sex": Genders.Female, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }
    persondex["Flannery"] = {"Named" : True, "Value" : 4, "Contact": True, "Sex": Genders.Female, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }
    persondex["Lance"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Male, "Relationship": "Mentee", "RelationshipRank": 0, "Events": [] }
    persondex["Calem"] = {"Named" : True, "Value" : 7, "Contact": True, "Sex": Genders.Male, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }
    persondex["Tia"] = {"Named" : True, "Value" : 9, "Contact": True, "Sex": Genders.Female, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }

    classstats = { 
        "Normal" : 24,
        "Fire" : 18,
        "Water" : 19,
        "Grass" : 23,
        "Electric" : 2,
        "Ice" : 11,
        "Fighting" : 13,
        "Poison" : 12,
        "Ground" : 16,
        "Flying" : 27,
        "Psychic" : 12,
        "Bug" : 14,
        "Rock" : 11,
        "Ghost" : 9,
        "Dark" : 13,
        "Dragon" : 28,
        "Steel" : 12,
        "Fairy" : 11
    }

    GetTrainerTeam("Blue", "Eevee").Item = Item.SootheBell
    GetTrainerTeam("Blue", "Magikarp").Item = Item.ExperienceShare

scene colosseum
show screen currentdate 
show yellow neutralhat
with splitfade

blue @angry "...I'm going to go crazy if I have to wait one more second."

yellow @surprised "O-oh! B-blue, look! S-someone...!"

show yellow:
    ease 0.5 xpos 0.33

show lace at rightside

lace @talkingmouth "Hm... hello, young man. You must be a student here. Is the Battle Hall this way?"

blue @closedbrow talkingmouth "Nope."

lace @talkingmouth "Oh, okay."

show lace:
    ease 0.5 xpos 1.1

blue @closedbrow talkingmouth "Heh. One down."

yellow @talkingmouth "I'm not sure you can call that 'one down.'"

blue @surprised "What?"

yellow surprised @happy "Well, she's just going to come back, isn't she? If you beat her in a battle, {i}then{/i} you can mark one, right?"

blue @surprised "...Hey... hey, wait! You're right!"

show colosseum with vpunch

blue @angry "Hey! Lady!"

show lace:
    ease 0.5 xpos 0.66

pause 1.0

lace @talkingmouth "Yes, young man?"

blue @talkingmouth "I misspoke. What I meant was that the Battle Hall is right behind me."

lace @talkingmouth "Oh! Well then, thank you very--"

blue @angry "And you ain't gettin' in!"

lace angry "What?"

blue @talkingmouth "You heard me. I'm the Ace of the Kobukan Battle Team, and I can tell just from looking at you that you battling in our hall would just be a waste of time."

lace @talkingmouth "I beg your pardon? Do you know who I am?"

blue @closedbrow talkingmouth "You're a nobody, lady. I've seen a couple dozen people who look just like you in Inspira. Same hair, same clothing."
blue @happy "What, was there a sale at the belted one-piece dress/shirt-combo store? Bet you've got a really 'unique' team, too!"

lace @talkingmouth "How dare you! Young man, I demand you move aside this instant!"

blue @talkingmouth "What? You're coming here to battle, there's a guy who's in your way, and your first instinct is just to 'demand' I move? Psh. You'd never cut it, even without me. C'mon, get your Poké Balls out!"

lace @talkingmouth "Fine! But I warn you, I'm the best battler in my office!"

call clearscreens from _call_clearscreens_104
show blank with dis

window hide

stop music fadeout 0.25

$ renpy.music.queue("Audio/Music/KantoTrainerStart_Rock.ogg", channel='music', loop=None, fadein=1.0, tight=None)

call CreateSplash(["blue"], ["lace"], customexpressions=["blue happy", "blue angrybrow happymouth", "lace neutral", "lace angry"]) from _call_CreateSplash_2

stop music fadeout 0.25

hide blank2
hide blank with dis

show yellow neutralhat -surprised:
    xpos 0.33

show lace angry:
    xpos 0.66

$ playerparty[0].Health = playerparty[0].Health - 1

narrator "This battle..."

pause 1.0

narrator "Was so one-sided, it's not worth showing."

show screen currentdate with dis

show screen songsplash("A Rival Appears!", "Zame")
queue music "audio/music/rivalchill_start.ogg" noloop
queue music "audio/music/rivalchill_loop.ogg"

blue @happy "Hah! That's the best your office can offer up? Geez, lady, where do you work? Bad Battlers, Inc.?"
blue @angry "Get out of here! Try again next year, maybe!"

lace "{w=0.5}.{w=0.5}.{w=0.5}."

hide lace with dis

pause 1.0

blue @talkingmouth "Heh. Now, {i}that's{/i} one."

yellow @sadbrow talkingmouth "Did you have to be... {i}so{/i} mean?"

blue @talkingmouth "Yeah, if I want to get through these people fast enough."
blue @surprised "...Ugh, here's some more."

blue @angry "Hey, bud! You looking for the stupid club? It's the other way!"

show roughneck angry at rightside with vpunch

roughneck @talkingmouth "Hey! No it ain't!"

call clearscreens from _call_clearscreens_105
show blank with dis

window hide

stop music fadeout 0.25

$ renpy.music.queue("Audio/Music/KantoTrainerStart_Rock.ogg", channel='music', loop=None, fadein=1.0, tight=None)

call CreateSplash(["blue"], ["roughneck"], customexpressions=["blue happy", "blue angrybrow happymouth", "roughneck", "roughneck angry"], reanchor=[False, True]) from _call_CreateSplash_3

stop music fadeout 0.25

show screen songsplash("A Rival Appears!", "Zame")
queue music "audio/music/rivalchill_start.ogg" noloop
queue music "audio/music/rivalchill_loop.ogg"

hide blank2

hide blank with dis

show screen currentdate with dis

show yellow neutralhat:
    xpos 0.33

show roughneck angry:
    xpos 0.66

$ playerparty[0].Health = playerparty[0].Health - 1

blue @angrybrow talkingmouth "Yeah, alright, Cue Ball, I'm sure you thought you really had something. Why don't you go home and polish that dome of yours?"

hide roughneck with dis

pause 1.0

blue @talkingmouth "Heh. Leaf was right. This shit is {i}easy.{/i}"

yellow @surprised "Watch out! There are more coming!"

show mace happy with dis:
    xpos 0.66

mace @talkingmouth "Good day, my fellow Student! I hope--"

blue @surprised "Do I know you?"

mace sadbrow @talkingmouth "Er... I don't believe so? I kinda just have one of those faces."

blue @angry "Well, whatever your face is, it's pissing me off! Get out of here!"

mace @sad "But... I was trying to go to the Battle Hall."

blue @angrybrow happymouth "Yeah, and I'm trying to prevent you from getting in. Now, who do you think has bigger stones?"

mace @sad "Ah... well... I'll battle you for it, I suppose..."

call clearscreens from _call_clearscreens_106
show blank with dis

window hide

stop music fadeout 0.25

$ renpy.music.queue("Audio/Music/KantoTrainerStart_Rock.ogg", channel='music', loop=None, fadein=1.0, tight=None)

call CreateSplash(["blue"], ["mace"]) from _call_CreateSplash_4

stop music fadeout 0.25

show screen songsplash("A Rival Appears!", "Zame")
queue music "audio/music/rivalchill_start.ogg" noloop
queue music "audio/music/rivalchill_loop.ogg"

hide blank2

hide blank with dis

show screen currentdate with dis

show yellow neutralhat:
    xpos 0.33

show mace sad:
    xpos 0.66

$ playerparty[0].Health = playerparty[0].Health - 1

blue @talkingmouth "Hah! You fight like a dairy farmer!"

mace @sadbrow talkingmouth "Yeah, well... you... you're... mean!"

hide mace with dis

blue @angrybrow happymouth "C'mon! Make this harder!"

yellow @closedbrow talkingmouth "{size=30}That's Blue. Always making things harder for himself.{/size}"

yellow @talkingmouth "So, would you like some healing?"

blue @happy "Hah, what? No way! I wanna see how many of these punks I can beat in a row without healing!"

yellow @sadbrow talkingmouth "Oh... okay."

blue @talkingmouth "...Wait, what's that big crowd of people outside the gates?"

yellow @talkingmouth "We're pretty close to noon. Those must be the battlers whose matches are in the first few hours of the first round..."

blue @sweat closedbrow talkingmouth "Damn. That's a {i}lot{/i} of people."

pause 2.0

yellow @sad "Are you alright?"

blue @closedbrow talkingmouth "Yeah, just doing some math in my head. Fifty-sixty people... two Pokémon each, on average... each battle takes about a minute..."

pause 1.0

blue @angrybrow talkingmouth "Yeah, I'm going to need to take them on three at a time."

yellow @sad "I... I could join..."

show yellow blush with dis

blue @talkingmouth "It's fine. I know you don't like battling. I got this."

narrator "You look out at the mass of people walking towards you, and count the Poké Balls." 
narrator "Two, five, a dozen, thirty, sixty, a hundred, two hundred..."

pause 1.0

narrator "Your hands tighten around your own, five, Poké Balls, and the Poké Ball belonging to Leaf's Dratini."

bluemind @frownmouth "Outnumbered... outgunned..."
bluemind @angrybrow talking2mouth "But, for the first time in my life, I'm {i}not{/i} outmatched."

show yellow surprisedbrow frownmouth -blush with dis

blue @happy "Ha.{w=0.5} Haha.{w=0.5} Hahaha!{w=0.5} Hahahahaha!{w=0.5} Ahahahahaha!"

yellow @talkingmouth "B-blue? What happened?"

blue @talkingmouth "It's just... it's funny, Yellow. There's {i}so many{/i} of {i}them,{/i} and just one of me."

blue @closedbrow happymouth "But... with my six Pokémon... with my levels... unless those losers can figure out how to work together to beat me... I outnumber {i}them.{/i}"

pause 1.0

blue angrybrow happymouth "How hard can it be? {size=40}Bring it on!{/size}"

call clearscreens from _call_clearscreens_107
scene blank2 with splitfadefast

pause 3.5

stop music fadeout 1.5
queue music "audio/music/soaringillusions_intro.ogg" noloop
queue music "audio/music/soaringillusions.ogg"

python:
    playercharacter = "Leaf"

    playerparty = GetTrainerTeam("Leaf")

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

scene sky:
    yalign 1.0 xalign 0.2 zoom 1.25
    parallel:
        ease 30.0 xalign 1.0
show clouds1 as base1:
    xpos -200 ypos 100 alpha 0.0
    block:
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 12.0 xpos 2000
        parallel:
            pause 11.0
            linear 1.0 alpha 0.0
show clouds2 as base2:
    xpos -800 ypos 400 alpha 0.0
    block:
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 8.0 xpos 1000
        parallel:
            pause 7.0
            linear 1.0 alpha 0.0
show clouds3 as base3:
    xpos -400 ypos 0 alpha 0.0
    block:
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 10.0 xpos 2200
        parallel:
            pause 9.0
            linear 1.0 alpha 0.0

show clouds1 as set1:
    xpos -1800 ypos 100 alpha 0.0
    block:
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 15.0 xpos 1800
        parallel:
            pause 14.0
            linear 1.0 alpha 0.0
            pause 1.0
            xpos -1500
        repeat
show clouds2 as set2:
    xpos -1700 ypos 100 alpha 0.0
    block:
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 12.0 xpos 2200
        parallel:
            pause 11.0
            linear 1.0 alpha 0.0
            pause 1.0
            xpos -1400
        repeat
show clouds3 as set3:
    xpos -2100 ypos 0 alpha 0.0
    block:
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 17.0 xpos 2200
        parallel:
            pause 16.0
            linear 1.0 alpha 0.0
            pause 1.0
            xpos -1800
        repeat
show clouds1 as set4:
    xpos -1700 ypos -100 alpha 0.0
    pause 5.0
    block:
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 6.0 xpos 1800
        parallel:
            pause 5.0
            linear 1.0 alpha 0.0
            pause 1.0
            xpos -1400
        repeat
show clouds2 as set5:
    xpos -1900 ypos 500 alpha 0.0
    pause 6.0
    block:
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 8.0 xpos 2200
        parallel:
            pause 7.0
            linear 1.0 alpha 0.0
            pause 1.0
            xpos -1700
        repeat
show clouds3 as set6:
    xpos -2100 ypos -50 alpha 0.0
    pause 5.0
    block:
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 20.0 xpos 2200
        parallel:
            pause 19.0
            linear 1.0 alpha 0.0
            pause 1.0
            xpos -1900
        repeat
show clouds2 as set7:
    xpos -1900 ypos 200 alpha 0.0
    pause 4.0
    block:
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            linear 10.0 xpos 2200
        parallel:
            pause 9.0
            linear 1.0 alpha 0.0
            pause 1.0
            xpos -1700
        repeat
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
show screen currentdate
with splitfade

$ renpy.pause(1.5, hard=True)

red @closedbrow frownmouth "{size=30}At this point, I think I'd rather go home and be a farmer. How hard can it be? Bring it on.{/size}"

leaf uniform @sarcastic "...Negative one hundred and twenty-eight bottles of beer on the wall. {w=0.5}Negative one hundred and twenty-eight. {w=0.5}Take one down. {w=0.5}Pass it around. {w=0.5}Negative one hundred and twenty-eight."

latias @happy "Lati!~ Lati-la lati la tias la ti la!"

leaf @sadbrow talking2mouth "Hey... sweetheart? Not that this isn't {i}really{/i} fun, but... can I stop now? {size=30}Please?{/size}"

latias @angrybrow poutmouth "Titita!"

leaf @sadbrow talkingmouth "Oh... okay..."

pause 2.0

red @playfulbrow talking2mouth "I'm never touching another drop of alcohol in my life."

leaf @surprised "What, you have?"

red @talkingmouth "Sure. Not a lot, 'cause it's full of sugars and calories, but the odd sip."

leaf @talking2mouth "Yeah, but it's not legal, is it?"

red @happy "Nope. But it's rural Kanto. If the Jennies have enough time to come to {i}Pallet Town{/i} and knock down the door of a guy who had a couple drinks at a neighbor's wedding, then we've achieved world peace."

leaf @happy "Hah! That makes sense."

pause 2.0

red @talkingmouth "...So, what's your thing against water?"

leaf @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
leaf @sadbrow talking2mouth "Do you mind if... if we don't talk about it while we're flying over the ocean?"

red @surprised "Oh, yeah, of course! My bad."

leaf @blush sadbrow talkingmouth "Thanks."

pause 2.0

leaf @surprised "Wait... is that?"

pause 1.0

leaf @angrybrow happymouth "Land ho!"

red @closedbrow talkingmouth "Now, that's no way to refer to Tia. Besides, where would she land?"

leaf @surprised "No, look! On the horizon!"

red @confused "Huh?"

narrator "You strain your eyes, and you see, at the very edge of the horizon, the tip of a mountain cresting from the edge of the water."

leaf @happy "Look, that's the top of Argent Mountain!"

red @confused "You're looking at me like I should know what that is."

leaf @closedbrow talkingmouth "Oh, right, you're terrible at geography... Argent Mountain is the mountain right near Kobukan!"

red @surprised "Oh, right, so we must be {i}pretty{/i} close, right?"

leaf @happy "Yeah! And not a moment too soon."

call clearscreens from _call_clearscreens_108 
show blank2 with dis

pause 1.0

show noon at vspaz
$ timeOfDay = "Noon"

pause 3.5

hide blank2 
show screen currentdate
with dis

leaf @talking2mouth "Oh... oh, crap."

red @surprised "What?"

leaf @sadbrow talking2mouth "It's noon. It's all up to Blue, now."

red @sad2eyes talking2mouth "Great."

pause 1.0

leaf @talking2mouth closedbrow "You could try to be nicer to him."

red @confusedbrow talking2mouth "I could also try to fart rainbows and fly, but I'm not going to do that when there's a high chance of falling a few hundred feet to my death."

leaf @embarrassedbrow talkingmouth "Ah... let's not say the 'f-word', please."

pause 2.0

red @confused "Fuck?"

leaf @angry "Not that one! Fall!"

latias @surprised "La?"

leaf @surprised "That wasn't a command!"

call clearscreens from _call_clearscreens_109
show blank2 with splitfadefast

pause 3.5

stop music fadeout 1.5
queue music "audio/arctic.ogg" loop channel "crowd"

show screen songsplash("Run Away, Fugitives", "Lazy Totodile")

queue music "audio/music/runawayfugitives_start.ogg" noloop
queue music "audio/music/runawayfugitives_loop.ogg"

python:
    playercharacter = "Ethan"

    ethanparty = [Pokemon(172.1, level=max(1, pikachuobj.Level - 1), ivs=[1, 1, 1, 1, 1, 1], evs=[0, 0, 0, 0, 0, 0], gender=Genders.Female, ability="Small World", nature=Natures.Lonely)]
    for mon in oldparty:
        ethanparty.append(Pokemon(mon.Id, level=max(1, mon.Level - 1), ivs=[1, 1, 1, 1, 1, 1], evs=[0, 0, 0, 0, 0, 0], moves=copy.deepcopy(mon.Moves), gender=mon.Gender, ability=mon.Ability))
    playerparty = ethanparty

    classstats = oldclassstats

    inventory = {
        Item.OldPicture : 1,
        Item.FirstAidKit : 1,
        Item.GSBall : 1,
        Item.ExperienceShare : 1
    }

    personalstats = {
        "Charm" : -3,
        "Knowledge" : 5,
        "Courage" : 3,
        "Wit" : 9,
        "Patience" : 69
    }

    persondex = copy.deepcopy(defaultpersondex)
    persondex["Professor Cherry"] = {"Named" : True, "Value" : 247, "Contact": False, "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [] }
    persondex[first_name] = {"Named" : True, "Value" : oldpersondex["Ethan"]["Value"] * 3, "Contact": False, "Sex": Genders.Male, "Relationship": "Wannabe", "RelationshipRank": 0, "Events": [] }
    persondex["Ethan"]["Named"] = True
    persondex["Blue"]["Named"] = False
    persondex["Yellow"]["Named"] = True

narrator "{color=#00b23f}You are no longer you.{/color}"

scene icecave
show aninetales:
    zoom 0.8 xalign 0.5 yanchor 1.0 ypos 1.2
show screen currentdate
with splitfade

ethan @talking2mouth "Listen to my commands."

pause 1.0

$ sidemonnum = 38.1
$ hideside = True

$ PlaySound("pokemon/cries/38.mp3")
sidemon @talkingmouth "Nine."

$ hideside = False

pause 1.0

ethan @confusedeyebrows talking2mouth "Wait, is that, like, 'Nein'? No? Or are you saying the only thing you can say?"

$ hideside = True

$ PlaySound("pokemon/cries/38.mp3")
sidemon @talkingmouth "Tales!"

$ hideside = False

pause 1.0

ethan @talking2mouth "Gotcha."

pause 1.0

narrator "The Ninetales watches you patiently, glittering resplendently in the icy cave."

pause 1.0

narrator "Looking at its wispy tails, which seem to fade into a boreal mist at the tips, you have a strong and sudden urge to grab one of them."

pause 1.0

ethan @closedbrow talking2mouth "It's probably just a folktale... but I'm not going to risk it."

pause 1.0

stop music fadeout 5.0

ethan @talking2mouth "Ninetales. I need you to go down to the school and keep the Disciplinary Committee occupied. I'm trying to help a friend."
ethan @closedbrow talking2mouth "I need you to go to Pledge Hall--a big brick building, as far as possible from the big, round, silver building, okay?"
ethan @talkingmouth "Avoid being caught. Avoid being defeated. Don't hurt anyone, but don't let them move you from that spot."

pause 1.0

$ hideside = True

$ PlaySound("pokemon/cries/38.mp3")
sidemon @talkingmouth "Ninetales!"

pause 1.0

$ hideside = False

ethan @sweat sadbrow talkingmouth "Uh, thanks."

pause 1.0

narrator "The Ninetales tilts its head, as though expecting you to say more."

ethan @sad2eyes talking2mouth "Man, you can just see through me, can't you?"

pause 1.0

ethan @talking2mouth "I think... I think I can make you stronger. Really quickly. But I'm not sure if you'll be... fine?"

narrator "The Ninetales watches you calmly."

ethan @sadbrow talking2mouth "You... probably won't be able to do this without this boost. But... I have nightmares about this, and... I'm pretty sure I can do it, but it might hurt you, so..."

pause 1.0

show aninetales:
    ease 0.5 ypos 1.3
    pause 0.5
    ease 0.5 ypos 1.2

narrator "The Ninetales nods, as though giving you permission to go ahead."

ethan @sadbrow talking2mouth "Oh man, oh man..."
ethan @closedbrow talking2mouth "Okay. You've come this far. You spent too long making this mistake, you can't stop now. Just go ahead, and..."

pause 1.0

show aninetales:
    ease 0.5 zoom 1.3 ypos 1.4

narrator "You reach out a trembling hand to the Ninetales, your breath visible in the cold air."

pause 1.0

narrator "And you think.{w=0.5} About every miserable memory you can conjure up."

narrator "And as your thoughts become darker and darker, so too do the eyes of the Ninetales. Its brows narrow, and its lips curl in a sneer, baring its fangs. A cold wind blows through its fur, faster and more roughly."

$ hideside = True

$ PlaySound("pokemon/cries/38.mp3")
sidemon @talkingmouth "Nnnnnninetales...!"

$ hideside = False

pause 1.0

narrator "The Ninetales' haunches raise as its crystalline fur stands on end, claws digging into the ice in the ground as a deep, throaty, growl begins in its throat."

ethan @sadbrow talking2mouth "{size=30}So... it wasn't just a nightmare...{/size}"

show aninetales:
    zoom 1.3 ypos 1.4 alpha 1.0
    ease 0.5 ypos 0.0 alpha 0.0 zoom 3.0

$ hideside = True

$ PlaySound("pokemon/cries/38.mp3")
sidemon @talkingmouth "Ninetales!"

$ hideside = False

pause 1.0

narrator "The Ninetales bounds over your head in one elegant jump as its fury--{i}on your behalf{/i}--compels it to action."

pause 1.0

ethan @sadbrow frownmouth "So it wasn't just a nightmare."

ethan @closedbrow talking2mouth "Damn it. {i}Damn it.{/i}"

pause 3.0

show phone_B
show phone_A
with fadeinbottom

show phone_C behind phone_A with dis

show phone_msg1 behind phone_A with dis:
    xzoom -1
    
$ title = Text("Silver",size=30,font="fonts/consola_0.ttf",color="#313131")

image msg = Text("Hey! Looks like there's some sort of issue\nat Pledge Hall. Far from the Battle Hall.\nAre you guys the people I should text to\nhave you check this out?",size=21,color="#ffffff",line_spacing=5,text_align=0.0)

show text title behind phone_A:
    xalign 0.51 yalign 0.34
show msg behind phone_A:
    xpos .41 ypos .4
with dis

pause 5.0

image msg2 = Text("Who are you,\nand\nhow did you get this number?",size=21,color="#ffffff",line_spacing=5,text_align=0.0)

show phone_msg1 behind phone_A:
    xzoom 1
show text title behind phone_A:
    xalign 0.51 yalign 0.34
show msg2 behind phone_A:
    xpos .41 ypos .4
hide msg
with pixellate

ethan @talking2mouth "Alright. That should distract them. If [blue_name] can't keep up his end of the plan, then it's not my fault."

pause 1.0

ethan @surprised "Oh, crap! I need to get back for my own match!"

call clearscreens from _call_clearscreens_110
scene blank2 with splitfadefast 

show youarenolongeryou_ethan with Dissolve(3.0)

pause 3.5

hide youarenolongeryou_ethan with Dissolve(1.5)

stop music channel "crowd" fadeout 1.5

show afternoon at vspaz

$ timeOfDay = "Afternoon"

pause 3.5

narrator "{color=#c1861e}You are no longer you.{/color}"

pause 2.0

stop music fadeout 1.5

show screen songsplash("A Rival Appears!", "Zame")
queue music "audio/music/rivalchill_start.ogg" noloop
queue music "audio/music/rivalchill_loop.ogg"

python:
    playercharacter = "Blue"

    playerparty = GetTrainerTeam("Blue")

    inventory = {
        Item.PokeBall : 27,
        Item.GreatBall : 13,
        Item.UltraBall : 4,
        Item.Potion : 9,
        Item.ParalyzeHeal : 4,
        Item.Awakening : 2,
        Item.Antidote : 4,
        Item.BurnHeal : 1,
        Item.IceHeal : 1,
        Item.DragonFang : 2,
        Item.SharpBeak : 2,
        Item.MiracleSeed : 1,
        Item.MysticWater : 1,
        Item.Charcoal : 1,
        Item.PictureofDaisy : 1,
        Item.DadsCoin : 1,
        Item.MomsWatch : 1,
        Item.HandMirror : 1
    }

    personalstats = {
        "Charm" : 4,
        "Knowledge" : 3,
        "Courage" : 38,
        "Wit" : -3,
        "Patience" : 7
    }

    knownclasses = []
    if (1 in oldpersondex["Instructor Winona"]):
        knownclasses.append("Flying")
    if (1 in oldpersondex["Instructor Clair"]):
        knownclasses.append("Dragon")
    if (knownclasses == []):
        knownclasses.append("None")

    persondex = copy.deepcopy(defaultpersondex)
    persondex["Gramps"] = {"Named" : True, "Value" : 82, "Contact": True, "Sex": Genders.Male, "Relationship": "Grandson", "RelationshipRank": 0, "Events": [] }
    persondex["Yellow"] = {"Named" : True, "Value" : 12, "Contact": True, "Sex": Genders.Female, "Relationship": "Partner", "RelationshipRank": 0, "Events": [] }
    persondex[first_name] = {"Named" : True, "Value" : oldpersondex["Blue"]["Value"], "Contact": True, "Sex": Genders.Male, "Relationship": ("Rival" if oldpersondex["Blue"]["RelationshipRank"] == 0 else "Talker"), "RelationshipRank": 0, "Events": [] }
    persondex["Nate"] = {"Named" : True, "Value" : 58, "Contact": True, "Sex": Genders.Male, "Relationship": "Dormmate", "RelationshipRank": 0, "Events": [] }
    persondex["Cheren"] = {"Named" : True, "Value" : 1, "Contact": True, "Sex": Genders.Male, "Relationship": "Dormmate", "RelationshipRank": 0, "Events": [] }
    persondex["Leaf"] = {"Named" : True, "Value" : 7, "Contact": True, "Sex": Genders.Female, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }
    persondex["Sonia"] = {"Named" : True, "Value" : 4, "Contact": True, "Sex": Genders.Female, "Relationship": "Underclassman", "RelationshipRank": 0, "Events": [] }
    persondex["Hilbert"] = {"Named" : True, "Value" : 9, "Contact": True, "Sex": Genders.Male, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }
    persondex["Silver"] = {"Named" : True, "Value" : 14, "Contact": True, "Sex": Genders.Male, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }
    persondex["Bea"] = {"Named" : True, "Value" : 23, "Contact": True, "Sex": Genders.Female, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }
    persondex["Erika"] = {"Named" : True, "Value" : 4, "Contact": True, "Sex": Genders.Female, "Relationship": "Enemy", "RelationshipRank": 0, "Events": [] }
    persondex["Janine"] = {"Named" : True, "Value" : 31, "Contact": True, "Sex": Genders.Female, "Relationship": "Mentee", "RelationshipRank": 0, "Events": [] }
    persondex["Ethan"] = {"Named" : True, "Value" : 1, "Contact": True, "Sex": Genders.Male, "Relationship": "He's there?", "RelationshipRank": 0, "Events": [] }
    persondex["Dawn"] = {"Named" : True, "Value" : 5, "Contact": True, "Sex": Genders.Female, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }
    persondex["Instructor Winona"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [] }
    persondex["Instructor Clair"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [] }
    persondex["Alder"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [] }
    persondex["Bruno"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [] }
    persondex["Skyla"] = {"Named" : True, "Value" : 2, "Contact": True, "Sex": Genders.Female, "Relationship": "Antihero", "RelationshipRank": 0, "Events": [] }
    persondex["Misty"] = {"Named" : True, "Value" : 2, "Contact": True, "Sex": Genders.Female, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }
    persondex["Flannery"] = {"Named" : True, "Value" : 4, "Contact": True, "Sex": Genders.Female, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }
    persondex["Lance"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Male, "Relationship": "Mentee", "RelationshipRank": 0, "Events": [] }
    persondex["Calem"] = {"Named" : True, "Value" : 7, "Contact": True, "Sex": Genders.Male, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }
    persondex["Tia"] = {"Named" : True, "Value" : 9, "Contact": True, "Sex": Genders.Female, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }

    classstats = { 
        "Normal" : 24,
        "Fire" : 18,
        "Water" : 19,
        "Grass" : 23,
        "Electric" : 2,
        "Ice" : 11,
        "Fighting" : 13,
        "Poison" : 12,
        "Ground" : 16,
        "Flying" : 27,
        "Psychic" : 12,
        "Bug" : 14,
        "Rock" : 11,
        "Ghost" : 9,
        "Dark" : 13,
        "Dragon" : 28,
        "Steel" : 12,
        "Fairy" : 11
    }

    GetTrainerTeam("Blue", "Eevee").Item = Item.SootheBell
    GetTrainerTeam("Blue", "Magikarp").Item = Item.ExperienceShare

    for mon in playerparty:
        mon.AdjustHealth(RandomUniform(7, 19), absolute=True)

scene colosseum
show screen currentdate 
show yellow neutralhat sadbrow frownmouth at leftside
with splitfade

narrator "There is a large crowd gathered around you." 
narrator "They mutter discontentedly, but after seeing how many of their fellows faced defeat at your hands, few are willing to challenge you, and some at the back of the queue are wandering off."

blue @angry "Hah! Is that all you've got?! I can do this all day!"

Character("Hapless Officeworker") "\"This guy's crazy!\""

Character("Irritated Man") "\"Move out of the way, dude! I'm going to be late for my match!\""

Character("Confused Student") "\"But if we can't even beat him all together, do we even have a chance in the Quarter Qlashes...?\""

show dawn angrybrow frownmouth at rightside with dis

dawn @sadmouth "...B-Blue."

blue @surprised "What? You? Tch. You can pass. Go ahead."

show dawn:
    xpos 0.75
    ease 0.5 ypos 1.1

dawn @sadmouth "{size=30}That's... that's not what I want...{/size}"

blue @talkingmouth "Uh... fine, then, you don't have to pass. You can stay here with these losers."

show dawn:
    xpos 0.75
    ease 0.5 ypos 1.0

dawn @angrymouth "No-no! You're... you're being a bully, Blue!"

yellow @surprised "Wai, wait! Dawn, you've got it all wrong! Blue's just... he's just, um... protecting the Battle Hall!"

blue @angrybrow talkingmouth "Don't speak for me!"

yellow @talkingmouth "{size=30}Sorry.{/size}"

dawn @angrybrow sadmouth "What are you protecting the Battle Hall from, Blue? The... the Quarter Qlashes were supposed to start two hours ago!"

blue @closedbrow talking2mouth "Yeah, and I'm not stopping them from starting. It's not my fault all these generics give up as soon as I beat them!"

show colosseum with vpunch

dawn @surprisedmouth "Blue! You need to stop!"

blue @talkingmouth "{i}Oh yeah?{/i} {w=0.5}Make me."

yellow surprisedbrow frownmouth @surprised "{size=30}Blue! Don't provoke her!{/size}"

dawn @sadmouth "I... {w=0.5}I..."

blue @angrybrow talkingmouth "You don't have the guts, pinky."
blue @closedbrow talkingmouth "Frankly, I don't see why you're even on the Battle Team. At least Ethan {i}wants{/i} to battle. At least [first_name] tries, a little bit. What are {i}you{/i} even doing here?"

yellow sad "{size=30}Blue! Stop! Please, listen to me, and stop!{/size}"

dawn sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."

blue @closedbrow talkingmouth "Janine's pretty alright, but I don't know what the hell she was thinking when she brought you onboard. This is Kobukan Academy's Battle Team."
blue @angrybrow talkingmouth "The best battlers, in the best school, in the world. And people call {i}you{/i} the ace? You're an insult to everyone who's actually {i}trying{/i}."

pause 1.0

dawn angrybrow @angrymouth "Blue. I'm... I'm..."

blue @surprise "Huh? What?"

dawn angrybrow surprisedmouth "I'm... {i}sick{/i} and {i}tired{/i} of your loud mouth! And I {i}hate{/i} how you talk down to everyone!"

blue @surprised "What...?"

dawn @talkingmouth "You want to know why I'm part of the Battle Team? I'll show you!"

call clearscreens from _call_clearscreens_111
show blank with dis

window hide

stop music fadeout 1.5
$ renpy.music.queue("Audio/Music/legendary.ogg", channel='music', loop=True, tight=None)

call CreateSplash(["blue"], ["dawn"]) from _call_CreateSplash_5

stop music fadeout 0.25

hide blank2

hide blank with dis

show yellow neutralhat surprised:
    xpos 0.33

show dawn angrybrow frownmouth:
    xpos 0.66

python:
    for mon in playerparty:
        mon.Health = 0

narrator "This battle..."

pause 1.0

narrator "Was so one-sided, it's not worth showing."

show screen currentdate with Dissolve(2.0)

yellow @talkingmouth "Blue...? Are you alright?"

narrator "Not once, in that entire fight, was there a single spark of hope for you." 
narrator "There was no action you could have taken that would, in any way, elevate your odds."

blue @sad "What... what {i}are{/i} you?"

pause 1.0

dawn @angrymouth "A sculptor."

pause 1.0

dawn -angrybrow frownmouth @sadmouth "And I've carved a path. So, um. Move aside, please."

blue @sad "Yellow? I... what do I...?"

show yellow -surprisedbrow -frownmouth -surprised neutralhathealingpower glowhandseyes with dis

show blank4 behind yellow with transeye2nopause
$ PlaySound("shine.ogg")
$ HealParty()
pause 1.0
hide blank4 with transeye2nopause

yellow glowhands @closedbrow talkingmouth "Heal."

dawn surprisedbrow frownmouth @surprised "Huh?"

blue sad "Huh?"

yellow -neutralhathealingpower -glowhands @closedbrow talkingmouth "...You have another shot."

blue @talkingmouth "Wait... another..."

yellow @angrybrow talkingmouth "Get it together, Blue. I healed your team. You have another shot against her."

blue @talkingmouth "But--but--you saw her! She {i}demolished{/i} me! I've never lost that badly!"

yellow @happy "You don't need to win. You just need to buy time, right?"

blue @closedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
blue @angrybrow talkingmouth "Right."

pause 1.0

blue @angrybrow talkingmouth "Again!"

dawn sad "Oh... really? I just... I mean, I was really nervous going all-out like that, and..."

blue @angry "Again! You caught me off guard! This was just a warm-up--this next one's for real!"

dawn @angry "...Fine!"

call clearscreens from _call_clearscreens_112
show blank with dis

window hide

stop music fadeout 1.5
$ renpy.music.queue("Audio/Music/legendary.ogg", channel='music', loop=True, tight=None)

call CreateSplash(["blue"], ["dawn"]) from _call_CreateSplash_6

hide blank2

python:
    for mon in playerparty:
        mon.Health = 0

hide blank 
show screen currentdate
show dawn sadbrow frownmouth:
    xpos 0.66
with dis

pause 1.0

blue @surprised "Ugh... no change. Yellow?"

show yellow neutralhathealingpower glowhandseyes sadbrow talkingmouth with dis

show blank4 behind yellow with transeye2nopause
$ PlaySound("shine.ogg")
$ HealParty()
pause 1.0
hide blank4 with transeye2nopause

yellow @talkingmouth "Heal."

show yellow -neutralhathealingpower -glowhandseyes -sadbrow frownmouth with dis

call clearscreens from _call_clearscreens_113
show blank with dis

window hide

stop music fadeout 1.5
$ renpy.music.queue("Audio/Music/legendary.ogg", channel='music', loop=True, tight=None)

call CreateSplash(["blue"], ["dawn"]) from _call_CreateSplash_7

hide blank2

python:
    for mon in playerparty:
        mon.Health = 0

hide blank 
show screen currentdate
show dawn sadbrow frownmouth:
    xpos 0.66
with dis

pause 1.0

blue @surprised "Damn it. Once more!"

show yellow neutralhathealingpower glowhandseyes sad with dis

show blank4 behind yellow with transeye2nopause
$ PlaySound("shine.ogg")
$ HealParty()
pause 1.0
hide blank4 with transeye2nopause

yellow -neutralhathealingpower -glowhandseyes @neutralhathealingpower glowhandseyes "Heal... {size=30}Blue, I'm... I'm getting really tired...{/size}"

blue @talkingmouth "I'm sorry. I'll beat her this time!"

call clearscreens from _call_clearscreens_114
show blank with dis

window hide

stop music fadeout 1.5
$ renpy.music.queue("Audio/Music/legendary.ogg", channel='music', loop=True, tight=None)

call CreateSplash(["blue"], ["dawn"]) from _call_CreateSplash_8

hide blank2

python:
    for mon in playerparty:
        mon.Health = 0

hide blank 
show screen currentdate
show dawn sadbrow frownmouth:
    xpos 0.66
with dis

pause 1.0

blue @surprised "Damn it. Once more!"

show yellow neutralhathealingpower glowhandseyes sad with dis

show blank4 behind yellow with transeye2nopause
$ PlaySound("shine.ogg")
$ HealParty()
pause 1.0
hide blank4 with transeye2nopause

yellow -neutralhathealingpower -glowhandseyes @sad neutralhathealingpower glowhandseyes "{size=30}H-heal...{/size}"

dawn @surprised "W-wait, Blue! Come on! Yellow can't take any more!"

show yellow surprisedbrow frownmouth with dis

blue @angry "Yes she damn well can! She puts up with me every day! Compared to that, she can endure {i}anything!{/i}"
blue @angrybrow talkingmouth "And I promise you you'll fold before she does. I trust her."

yellow blush "Blue...?"

pause 1.0

yellow angrybrow talking2mouth "I can do one more."

dawn @angry "You two--you're acting crazy! Why are you doing this?"

blue @closedbrow happymouth "The 'why' doesn't matter. All that matters is if you can stop us."
blue @angrybrow happymouth "And the way I see it, it doesn't matter how many times you beat us, if we don't give up."

dawn @angry "F-fine! Then I'll just have to {i}force{/i} you to give up!"

bluemind @surprised "Ugh... I talked a big game, but... this might be it..."

dawn @angry "Altaria! Full power! It's time to Mega--"

pause 1.0

$ PlaySound("asteroidwoosh.ogg")

show yellow surprisedbrow frownmouth
show dawn surprisedbrow frownmouth
with dis

pause 2.0

blue @surprised "What... what was that?"

$ PlaySound("impact.ogg")

yellow @surprised "That's... that's Tia!"

blue @surprised "What? They actually made it back?"
blue @angry "C'mon, let's go!"

show yellow:
    ease 0.3 xpos -0.1

pause 2.0

dawn -surprisedbrow -frownmouth -surprised frownmouth @sad "Wait. He... he just left...?"

Character("Hapless Officeworker") "\"Thanks, Miss! You got that guy out of our way!\""

Character("Irritated Man") "\"Thank goodness! I was going to be late for my match!\""

Character("Confused Student") "\"Good job, Dawn! I didn't realize you were such a good battler!\""

dawn sadbrow @talkingmouth "Oh! Uh... yep. You're... you're welcome...?"

call clearscreens from _call_clearscreens_115
show blank2 with splitfadefast

show youarenolongeryou_blue_yellow with Dissolve(3.0)

pause 3.5

hide youarenolongeryou_blue_yellow with Dissolve(1.5)

pause 3.5

python:
    playercharacter = None
    playerparty = [pikachuobj]
    inventory = oldinventory
    personalstats = oldpersonalstats
    persondex = oldpersondex
    classstats = oldclassstats

stop music fadeout 1.5

#c1861e
#3110dd
#00b23f
narrator "{color=#3110dd}Y{/color}{color=#c1861e}o{/color}{color=#00b23f}u {/color}{color=#3110dd}a{/color}{color=#c1861e}r{/color}{color=#00b23f}e {/color}{color=#3110dd}o{/color}{color=#c1861e}n{/color}{color=#00b23f}c{/color}{color=#3110dd}e {/color}{color=#c1861e}a{/color}{color=#00b23f}g{/color}{color=#3110dd}a{/color}{color=#c1861e}i{/color}{color=#00b23f}n {/color}{color=#3110dd}y{/color}{color=#c1861e}o{/color}{color=#00b23f}u{/color}{color=#3110dd}.{/color}"

stop music fadeout 1.5
$ renpy.music.queue("Audio/Music/Dreams and Adventures.ogg", channel='music', loop=True, tight=None)

scene clouds
show garden:
    zoom 0.625
show tia hat:
    xpos 1.0/5.0
show leaf uniform:
    xpos 2.0/5.0
show yellow neutralhat:
    xpos 3.0/5.0
show blue angrybrow frownmouth:
    xpos 4.0/5.0
show blank2

show youarenolongeryou_bg_red_leaf_tia with Dissolve(2.0)

pause 2.0

show youarenolongeryou_ethan with Dissolve(2.0)

pause 2.0

show youarenolongeryou_blue_yellow with Dissolve(2.0)

pause 4.0

redmind @sadbrow frownmouth "I'm back."

hide blank2 
hide youarenolongeryou_bg_red_leaf_tia
hide youarenolongeryou_ethan
hide youarenolongeryou_blue_yellow
show screen currentdate
with transeye2

red @talkingmouth "Hey. I'm back."

pause 1.0

blue @angry "Well, excuse me for not wheeling out the welcome wagon."

red @sweat closedbrow talkingmouth "Hey, Blue. I heard you were battling pretty hard to buy me some more time."

blue -angrybrow -frownmouth @closedbrow talkingmouth "It was nothing. There wasn't a single battle I couldn't do with my eyes closed."
blue @happy "If those are the kinds of losers that'll be in {i}all{/i} the Quarter Qlashes, then no wonder our Battle Team's never been defeated."

leaf @talking2mouth "Blue, did the Disciplinary Committee hassle you?"

blue @talkingmouth "Nope. Guess Ethan succeeded."

leaf @closedbrow talking2mouth "When we were flying over the grounds, we saw a small blizzard near Pledge Hall."

blue @surprised "A blizzard?!"

leaf @sarcastic "A small one."

red @sadbrow talkingmouth "I'm going to let all of you know how thankful I am as soon as I can. I--{w=0.5}I {i}seriously{/i} can't express what this means to me." 

blue @closedbrow talkingmouth "Pah."

red @talkingmouth "But we should probably head to the Battle Hall as soon as we can, right?"

yellow @talkingmouth "Yes. I mean, that's what this was all for, right, [first_name]? Let's go!"

red @happy "Sure thing!"

red @sweat happy "Just one question. Who are you?"

yellow surprisedbrow frownmouth @surprised "Hm? You don't recognize me?"

$ BecomeNamed("Yellow")

blue @angry "She's Yellow."

red @confused "I don't know, for being willing to risk so much for a stranger, she seems pretty brave to me."

blue @surprised "I... what? You do that on purpose, don't you?"

red @happy "Maybe! C'mon, let's go!"

show tia hat:
    ease 0.5 xpos -0.15
show leaf uniform:
    ease 0.5 xpos -0.15
show yellow neutralhat:
    ease 0.5 xpos -0.15
show blue angrybrow frownmouth:
    ease 0.3 xpos -0.15

pause 1.0

show ethan:
    xpos -0.1
    ease 0.5 xpos 0.5

ethan @happy "Hey, guys! Am I late?"

pause 2.0

ethan @sad2eyes talking2mouth "Figures."

scene stadium_empty
show lance shadow anger angrybrow at rightside
show drayden happybrow at leftside
with dis

stop music fadeout 1.5
$ renpy.music.queue("Audio/Music/DragonDenStart_B.ogg", channel='music', loop=False, tight=None)
$ renpy.music.queue("Audio/Music/DragonDenLoop.ogg", channel='music', loop=True, tight=None)

lance @angrymouth "Dean Drayden! It has been {i}two hours{/i}! You {i}must{/i} allow me to find out why our challengers are so late!"

drayden "No, no, I don't think that's necessary. Our new Disciplinary Committee should be more than up to the task."

lance @angrymouth "I agreed with you--two and a half hours ago! This is the absolute end of my patience, Drayden!"

drayden sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."
drayden -sadbrow "And what about {i}my{/i} patience, Lance?"

lance @confusedeyebrows talking2mouth "What?"

drayden @surprisedeyebrows "I have stood here listening to your complaints for, as you say, two and a half hours."
drayden @sadbrow "I understand submission is a concept that is foreign to you, Champion Lance. But I do ask you to remember the chain of command on the grounds of Kobukan Academy."

lance -anger -shadow @closedbrow talking2mouth "...How long will that chain remain unbroken, I wonder?"

drayden @angry "Watch yourself, Lance."

lance @closedbrow talking2mouth "I am not blind to the dissatisfaction of the board. Though they are vulturous opportunists, I happen to agree with this particular complaint."
lance @talking2mouth "You have too much faith in the students. The fiasco last Saturday was because you believed the children to be capable of self-governance."
lance @angrybrow talking2mouth "I fail to see how what is happening {i}right now{/i} is any different."

drayden @sadbrow "I know you do, Lance.{w=0.5} I {i}know{/i} you do."

pause 1.0

lance @confusedeyebrows talking2mouth "What is that noise...?"

show drayden surprisedbrow:
    ease 0.5 xpos 0.1
show lance surprisedbrow
with dis

show leaf uniform surprised:
    xpos 1.1
    ease 0.3 xpos 0.3
show ethan surprisedbrow frownmouth:
    xpos 1.1
    ease 0.7 xpos 0.45
show yellow neutralhat surprised:
    xpos 1.1
    ease 1.1 xpos 0.9
show tia surprisedbrow frownmouth hat:
    xpos 1.1
    ease 0.5 xpos 0.75
show blue surprisedbrow frownmouth:
    xpos 1.1
    ease 0.3 xpos 0.6

pause 2.0

leaf -surprisedbrow -frownmouth -surprised @happy blush "Hey! Are we late?"

show ethan -surprisedbrow -frownmouth -surprised
show yellow -surprisedbrow -frownmouth -surprised
show tia -surprisedbrow -frownmouth -surprised
show blue -surprisedbrow -frownmouth -surprised
with dis

drayden @sadbrow "{size=30}Ah, now I see.{/size}"
drayden -surprisedbrow -frownmouth -surprised @happybrow "No, it would appear that you are perfectly on-time."

lance -surprisedbrow @angry "Of course. {i}Of course{/i} it would involve you three."

drayden @happybrow "Welcome back, Mr. [last_name]."

red @sweat talkingmouth "Hi, Dean Drayden."
red @happy "Um... you know how I said I wanted to drop out on Saturday?"

pause 2.0

drayden @sadbrow "...No."

red @surprised "Huh?"

drayden "I have no recollection of such an event."

red @surprised "What?"

lance @angry "{i}What?{/i}"

drayden @surprised "What?"

red @sweat happy "Um... nothing, I guess. Thank you, Dean."

drayden @sadbrow "I'm sure I have no idea what you're thanking me for. But if there was someone to thank, it would be Miss Magnolia. She established the precedent, after all."

red @surprised "Wait, Sonia? Didn't..."

lance @closedbrow talking2mouth "Yes. I was the one who convinced Dean Drayden, after a good amount of debate, of the importance of letting Sonia back in."
lance @sad2eyes talking2mouth "The irony of my own argument being used to let {i}you{/i} back in is not lost on me."

leaf @angry "Hey! What's up with this? You said that if [first_name] came back, you'd respect him!"

lance @angrybrow shadow talking2mouth "You may notice I am not investigating too closely why the beginning of the Quarter Qlashes has been delayed {i}two whole hours.{/i}"
lance @sad2eyes talking2mouth "You may interpret my reasoning for that however you wish."

pause 1.0

red @confusedeyebrows talking2mouth "Thanks...?"

pause 1.0

lance closedbrow talking2mouth "Tch. I take my leave of this."

stop music fadeout 1.5
$ renpy.music.queue("Audio/Music/Indigo_Start.ogg", channel='music', loop=False, tight=None)
$ renpy.music.queue("Audio/Music/Indigo_Loop.ogg", channel='music', loop=True, tight=None)

hide lance with dis

pause 2.0

ethan @confusedeyebrows talking2mouth "Has anyone ever told him that he can just, like, walk away? He doesn't always have to 'take his leave'?"

drayden @happybrow "Well, students, I cannot imagine what has transpired to bring you all here two hours late, but since you're here, it seems now would be an excellent time to begin the Quarter Qlashes in earnest."

blue @talkingmouth "Yeah, about time. [first_name], think you can avoid derailing everything to be the center of attention for a couple hours?"

red @happy "Hopefully!"

pause 1.0

red @surprised "Oh! Dean Drayden."

drayden @surprisedeyebrows "Young man?"

red @sweat happy "I... wasn't at gym class, so I didn't get my battle assignments. When's my first match?"

drayden @sadbrow "Hm. I don't remember, off the top of my head, who else is in your pool of eight, but it would appear that you...{w=0.5} are in the first round."

red @surprised "Woah! Really?"

yellow @happy "{i}Yes!{/i} Blue, that means that our battling {i}really{/i} mattered!"

blue @closedbrow talkingmouth "Good. If I'd spent two hours battling generics just to find out that his battle was at, like, 6PM, I'd be {i}really{/i} pissed."

red @sad2eyes confusedeyebrows talking2mouth "Oh, when {i}aren't{/i} you?"

drayden @sadbrow "Hm... looks like a good amount of people from the city, and other students, are starting to come in."
drayden @surprisedbrow "And... they do {i}not{/i} look happy."

pause 1.0

show blue surprisedbrow frownmouth with dis

drayden @sadbrow "...Why are they all shouting '[blue_name]'?"

ethan @talking2mouth "It's a new challenge.{w=0.5} On the internet.{w=0.5} Called the [blue_name] challenge."

drayden @surprisedbrow "Oh? But it appears many of them are looking at you, Mr. Oak."

blue @closedbrow talkingmouth "Yeah, well, my name's Blue. Don't have any idea what a [blue_name] is."

leaf @happy "Yep!"

drayden @sadbrow "Hm..."

pause 1.0

drayden "Mr. [last_name]."

red @surprised "Huh?"

show blue angrybrow frownmouth with dis

drayden @sadbrow "Does [blue_name] mean anything to you? Is it, perhaps, a nickname for Mr. Oak?"

redmind @sadbrow frownmouth "Oh... crap. I can't lie, but... if I say yes, then... well, I'd be throwing [blue_name] under the bus for helping me. And I've gotta draw the line somewhere, right?"

pause 1.0

$ oldblue_name = blue_name
$ blue_name = "Blue"

red @talkingmouth "His name is Blue, Sir."

blue -angrybrow "{w=0.5}.{w=0.5}.{w=0.5}."

pause 1.0

drayden @happy "So it is."
drayden @sadbrow "...Now, excuse me, I think I have some preparations to assist with."

hide drayden with dis

pause 1.0

red @talkingmouth "Thanks, Blue."

blue @angrybrow talkingmouth "I only did this so that you could fix this damn school. If there was anyone else who I thought could sort this shit out, I'd go to them."

red @talkingmouth "...Like with the Charmander, then."

blue @angrybrow happymouth "You mean {i}my{/i} Charmander? Yeah."

red @surprised "You... you knew about Frienergy."

blue @closedbrow talkingmouth "Obviously."

red @angrybrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
red @angrybrow talking2mouth "So that's what..."

pause 1.0

red @closedbrow talking2mouth sweat "We'll talk about this later."

pause 2.0

leaf @talking2mouth "I'm going to go change. I've been wearing this uniform for, like, twenty-four hours straight, and it is starting to {i}stank.{/i}"

show tia:
    xpos 0.75
    ease 0.5 ypos 1.1
    ease 0.5 ypos 1.0

yellow @talkingmouth "Tia says that it's true. You smell really bad."

leaf @surprised "Yellow!"

yellow @surprised "That-- that wasn't me! That was Tia!"

blue @angrybrow happymouth "Oh, sure, blame the mute girl."

yellow @sadbrow talkingmouth "H-hey, I'm just relaying the messages..."

leaf happy "Alright, alright! Yellow, you're precious, don't worry about it."
leaf @surprised "Oh, wait, Blue! My Dratini?"

blue @closedbrow talking2mouth "Yeah, here you go."

narrator "Blue passes Leaf a Poké Ball."

if (GetTrainerTeam("Leaf", "Dratini").Gender == Genders.Female):
    blue @closedbrow talkingmouth "She's strong."

    blue @talkingmouth "Take good care of her."
else:
    blue @closedbrow talkingmouth "He's strong."

    
    blue @talkingmouth "Take good care of him."

leaf @happy "Duh!"

hide leaf with dis

ethan @talkingmouth "My battle isn't for a couple hours... but I guess I might as well watch everyone else from the stands."

ethan @happy "Blue, Yellow, Tea, you guys wanna come with?"

blue @closedbrow talkingmouth "No."

show blue behind tia
show tia angrybrow poutmouth:
    ease 0.5 xpos 0.63

pause 0.5

show stadium_empty with vpunch

show tia:
    ease 0.5 xpos 0.75

blue @angry "Hey!"

yellow @talkingmouth "That means 'Yes, you do.'"

blue angrybrow talkingmouth "...I liked her more when I had no idea what she was saying. Can we go back to that?"

call clearscreens from _call_clearscreens_116
scene blank2 with Dissolve(3.0)

narrator "You quickly take your position on the side of the arena and wait for the announcer's call as hundreds of disgruntled battlers and spectators pour through the doors."
narrator "A harried-looking staff member thrusts a card in your hand numbered '#15', and points you towards a place to stand."

scene stadium_empty 
show screen currentdate
with Dissolve(1.0)

narrator "Another battler, someone from the city, toddles up to you excitedly."

stop music fadeout 1.5
$ renpy.music.queue("Audio/Music/Hoenn_Start.ogg", channel='music', loop=False, tight=None)
$ renpy.music.queue("Audio/Music/Hoenn_Loop.ogg", channel='music', loop=True, tight=None)

show oldman milotic with dis

oldman @happymouth "'Ello, youngster!" 

show stadium_full behind oldman:
    alpha 0.0
    ease 120 alpha 1.0

red @happy "Hello, Sir!" 

oldman @happybrow happymouth "Isn't this a pile of apples? We get to battle in Kobukan's own Battle Hall! I've seen a few pictures of this place, but I never thought I'd get to go in!"

red @happy "Yeah. It's pretty cool. I've been here a few times, but it still makes me gasp with how big it is."

oldman @surprisedbrow happymouth "You've been here a few times? What's that about, then, youngster?"

red @talkingmouth "Yeah. I'm actually part of the Kobukan Battle Team."

oldman @happybrow happymouth "Bless me, I've been talking to a celebrity!"

red @sweat talkingmouth "Hah! Not really, Sir. It's pretty early in the year. This'll be the Battle Team's first real challenge."

oldman @sadbrow happymouth "Well, good luck with that, then. What's your number?"

red @happy "Fifteen."

oldman @surprisedbrow happymouth "Oh? I'm sixteen!"

red @confusedeyebrows talkingmouth "Huh... I guess we might be battling each other, then."

oldman @angrybrow talking2mouth "Mrrgrr... just my luck!"
oldman @happybrow happymouth "Oh, well! I figured I'd get smacked down by some whippersnapper sooner or later."
oldman @sadbrow talking2mouth "Still, coming here all the way from Viridian, just to be eliminated in the opening round of battles..."

red @sweat talkingmouth "Sorry, Sir. If it makes you feel any better, I only have one Pokémon on me right now."

oldman @happybrow happymouth "Oh, I've only had two Pokémon in my entire sixty-eight years! And one of these is brand new. Gift from my granddaughter, it was."

red @happy "Cool."

pause 1.0

oldman @sadbrow happymouth "Talking of my granddaughter, she's the announcer for this event, don'tcha know?"

red @surprised "Hm? Last time there was an event with an announcer, I think a random student took the microphone. Is she a student here?"

oldman @sadbrow happymouth "No, no. She's... well, I'm sure you'll recognize her."

narrator "The old man raises his cane and points at the announcer's booth."

hide oldman with dis

narrator "Straining your eyes a bit, you think you vaguely recognize the figure. She seems to be fretfully talking into a Pokégear, pacing back and forth."

show lisia frownmouth sadbrow with dis

lisia @talkingmouth "{size=30}No, Io, this won't work! You {i}promised{/i} we'd co-host! My crew delayed for as long as we could, but the event's about to begin, and if you're still not here, then--!{/size}"

show lisia surprisedbrow surprisedmouth with dis

pause 2.0

lisia angrybrow angrymouth "{size=40}What do you mean you're still in Paldea?!{/size}"

hide lisia with dis

pause 1.0

show oldman milotic with dis

oldman @sadbrow talking2mouth "Eh-heh-heh. She's always like this before a show. But the moment the spotlight shines, it's all class and control with her."

$ BecomeNamed("Lisia")

oldman @surprisedbrow talking2mouth "Now, ain't you happy to learn a bit of celebrity gossip about {i}the{/i} Lisia?"

red @happy "Absolutely."

pause 1.0

red @confusedeyebrows talkingmouth "Who is Lisia?"

oldman @surprisedbrow talking2mouth "Eh? Don'tcha watch {i}any{/i} TV, young man? She's the Contest Champion!"

red @talkingmouth "Oh. Of Kobukan?"

oldman @sadbrow talking2mouth "No, young man! Of the world! She's the niece of Wallace, the previous Contest Champion!"

if (HasEvent("Instructor Wallace", 1)):
    red @happy "Oh, yeah! Wallace. I take classes from him."

else:
    red @happy "Oh, right, Wallace! I think he teaches at this school."

oldman @surprisedbrow talking2mouth "So cavalier..."
oldman @happybrow happymouth "You Kobukan students are really something else. You're not phased at all."

red @sweat "To be honest, Sir... I've got {i}a lot{/i} going on. Maybe I'd be a bit more gobsmacked if I had the time to process, but--"

show oldman milotic surprisedbrow:
    ease 0.5 xpos 0.75

show janine surprisedbrow frownmouth at leftside with vpunch

stop music fadeout 1.5

queue music "Audio/Music/fuchsia_start.ogg" noloop
queue music "audio/music/fuchsia_loop.ogg"

show screen songsplash("Fuchsia City", "Zame")

janine @talking2mouth "[first_name]?!"

red @sadbrow talking2mouth "...Hi, Janine."

oldman @happybrow happymouth "Lady troubles, young man? I'll leave you at it."

hide oldman with dis

show janine -surprisedbrow -frownmouth -surprised with dis:
    ease 0.5 xpos 0.5

pause 1.0

janine closedbrow @talking2mouth "I thought that you were... gone."

red @closedbrow talking2mouth "I was. A little bit."

pause 1.0

red @sadbrow talking2mouth "I'm sorry. Are you mad?"

pause 1.0

janine -closedbrow @talking2mouth "No. I'm just... processing. I had to change a bunch of plans based on your leaving the team, and I'd just gotten used to the new paradigm."
janine @closedbrow talking2mouth "So now I need to figure out if I can just seamlessly revert to the previous plan."

pause 1.0

red @confusedeyebrows talking2mouth "What changes did you make?"

janine @sadbrow sadmouth "Uh..."

lisia @happy "Battler number one! Would you please take your position? We're almost three hours late!~"

red @surprised "What?"

narrator "Janine wordlessly holds up a card, much like your own, that says '#1' on it."

janine @closedbrow talking2mouth "I figured you were our best shot at placing in the national tournament."
janine @sadbrow talking2mouth "When you left, I signed myself up."

red @surprised "You... signed yourself up a couple days ago, but you got the number one spot?"

if (GetRelationshipRank("Janine") == 1):
    janine @happy "I told you I'd be number one."

else:
    janine @talking2mouth "Yeah."

janine @talking2mouth "Just a coincidence, though. It's random. At least, it's meant to be."

red @talkingmouth "Damn. I guess that means you'll be beating me in a Quarter Qlash somewhere down the road, then?"

janine @closedbrow talking2mouth "...Maybe."

pause 1.0

red @sadbrow talkingmouth "Um... I {i}just{/i} got back here... how's the school?"

janine @sadbrow talking2mouth "I'll be real--things have been better."
janine @talking2mouth "A lot of people are still mad at you. But most people are too wrapped up in their own secrets being exposed."
janine @sadbrow talking2mouth "Still, you shouldn't expect to be winning any popularity contests any time soon."

red @sweat talkingmouth "Damn."

janine @talking2mouth "...I still have your back, though."

red @surprised "Huh?"

janine @closedbrow talking2mouth "It was a dumb move, to try and keep this power of yours secret. Obviously, it made you look suspicious as hell."
janine @happymouth "But I don't care if you're a red-haired little blue man from Ultra Space as long as you win battles for me."

red @sadbrow happymouth "Thanks, Janine. That really means a lot."

pause 1.0

janine @talking2mouth "Just out of curiosity, though, {i}do{/i} you have mind control powers?"

red @playfuleyes playfulbrows talking2mouth "No, I do not. All my power does is make people and Pokémon understand what I'm feeling."

pause 1.0

if (GetRelationshipRank("Janine") == 1 and HasEvent("Janine", "Domming")):
    janine @surprised "Oh. So that's why I get the feeling you want me to step on you?"

    red @surprisedbrow lightblush frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    janine @happybrow smirkmouth "I'm kidding. Chill out, [first_name]."

    pause 1.0

    janine @blush smirkmouth "Although I notice you didn't say 'no.'"
    
    janine @closedbrow talkingmouth "Anyway, that's actually a bit disappointing."

else:
    janine @closedbrow talkingmouth "That's actually a bit disappointing."

janine @talking2mouth "If you {i}did{/i} have those powers, I bet they would help you out in your battles a bunch."

red @confusedeyebrows talking2mouth "I already have the ability to make Pokémon listen to me as soon as I catch them! Isn't that enough?"

janine @smirkmouth "If there was some combination of abilities or powers that would let you become Kobukan's champion {i}right now{/i}, then, yeah, I'd say that's enough."

red @sadbrow talking2mouth "Well... I'll still do my best."

janine @smirkmouth "Don't worry too much about it. No Battle Team member has ever been eliminated in the first round of the Quarter Qlashes, and we've had much larger teams before."
janine @sadbrow talking2mouth "You should focus on talking to the other team members. A lot of them are on the fence about you--they're not sure what to think." 
janine @closedbrow talking2mouth "They've had enough time to calm down, but they're still in a position where they can be easily swayed one way or the other."

pause 1.0

janine @closedbrow talking2mouth "Winning your battles would be a good start, but after that, you'll need to give a hell of a speech. We're having an emergency meeting tomorrow to discuss... well, everything. Have it ready by then."

red @sadbrow talkingmouth "I'll... do my best. There's a lot of people in the school that I need to talk to, but fixing things with the Battle Team is definitely on my radar."

janine @sadbrow talkingmouth "Good. I don't want to think that making the Battle Team smaller--more personal--was a mistake, even if it means we're more easily sidetracked by stuff like this, so prove to me that wasn't a poor decision."

red @closedbrow talkingmouth "I'll do my best."

show janine happyneutralmouth with dis

pause 2.0

janine happy "I know you will."

lisia @happy "Battler #1? {i}Take your place, please!{/i}"

hide janine with dis

pause 1.0

redmind @frownmouth "...Okay. I only have [pika_name], but that should be fine, right? I mean, if I can't beat the first trainer in my first QQ match, maybe I really have no business being at Kobukan."

stop music fadeout 1.5
$ renpy.music.queue("Audio/Music/DragonDenStart_B.ogg", channel='music', loop=False, tight=None)
$ renpy.music.queue("Audio/Music/DragonDenLoop.ogg", channel='music', loop=True, tight=None)

show lance with dis

redmind @playfulbrow frownmouth "Oh, great. What now?"

lance @talking2mouth "[last_name]. I would have a word with you."

red @sweat closedbrow talking2mouth "I'm about to go have my first battle..."

lance @sad2eyes talking2mouth "This will take only a minute."
lance @closedbrow talking2mouth "Besides which, as I am the regional Champion of two regions, I would hope my position affords me at least a couple minutes of delay, coming off the three hour delay we've already endured."
lance @sad2eyes talking2mouth "God knows it conveys no other benefits."

red @talking2mouth "...Right."

lance @talking2mouth "I see you have tasted defeat. And you have come back to try again, in spite of it."

red @sadbrow talking2mouth "...Yeah."

lance @closedeyes talking2mouth "The drama of running away from the school, then coming back at the last possible minute, notwithstanding, it appears I may have misjudged you."

red @angrybrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

lance @talking2mouth "So I offer this advice with the full sincerity of a person in my position, attempting to do well."
lance @angrybrow shadow talking2mouth "{color=#ff0000}Some defeats you cannot come back from.{/color}"

red @talking2mouth "Huh?"

lance @talking2mouth "There will be consequences for failure from now on, [last_name]. Once defeat has its claws in you, every fresh defeat draws more blood."
lance @sad2eyes sadeyebrows talking2mouth "...Every battle you have had up to this point has been one that can be won, or lost, with little effect on your sheltered life."
lance @talking2mouth "But make no mistake, if you fail to win this first round of the Quarter Qlashes..."
lance @angrybrow shadow talking2mouth "No matter how much shame you may have felt before, it will {i}pale{/i} in comparison to the infamy of being the first Battle Team member to lose in the first round." 

red @closedbrow sweat talkingmouth "This sincere advice sounds a lot like a threat."

lance @closedbrow talking2mouth "Take it as you will. Now, I--"

show lance surprisedbrow with dis

red @happy "'Take my leave of you?'"

pause 1.0

lance shadow sad2eyes angryeyebrows talking2mouth "I was going to say 'I must go.'"

hide lance with dis

redmind @sweat closedbrow talkingmouth "Yeah, no he wasn't."

call clearscreens from _call_clearscreens_117
scene blank2 with Dissolve(3.0)

narrator "Eventually, all the battlers take their places, and a very frantic-looking Lisia takes to the stand. You watch her take a quick breath, and she dashes a dazzling smile as her voice booms into her microphone."

pause 1.0

stop music fadeout 1.5
show blank as firstblank behind blank2
show stadium_full behind blank2
show blank as secondblank behind blank2
$ renpy.music.play("Audio/Stadium_crowd.ogg", channel='crowd', loop=True, fadein=1.5)
$ renpy.music.play("Audio/Stadium_chant.ogg", channel='crowd2', loop=True, fadein=1.5)

$ renpy.pause(0.75, hard=True)

$ renpy.music.queue("Audio/Music/Indigo_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/Indigo_Loop.ogg", channel='music', loop=True, tight=None)

$ renpy.pause(1.0, hard=True)

hide blank2 with transball
$ renpy.pause(0.25, hard=True)
hide secondblank with dis

show stadium_full:
    subpixel True
    zoom 3.0 alpha 0.65 xalign 0.15 ypos 2600
    ease 1.25 alpha 1.0 xalign 0.0 ypos 3000
    xalign 0.85 alpha 0.65 ypos 2600
    ease 1.25 alpha 1.0 xalign 1.0 ypos 3000
    xalign 0.5 alpha 0.4 ypos 2400
    ease 1.0 alpha 1.0 zoom 1.0 ypos 1080

show lightbeam1 as beam1:
    pause 2.75
    zoom 0.6 alpha 0.0 yalign 0.9 xpos 0 rotate 40
    block:
        ease 0.25 alpha 0.5
    pause 0.3
    block:
        ease 1.0 rotate -40
        pause 0.5
        ease 1.0 rotate 40
        pause 0.5
        repeat
    
show lightbeam1 as beam2:
    pause 2.75
    zoom 0.6 alpha 0.0 yalign 0.9 xpos -300 rotate -40
    block:
        ease 0.25 alpha 0.5
    pause 0.1
    block:
        ease 1.0 rotate 40
        pause 0.5
        ease 1.0 rotate -40
        pause 0.5
        repeat

show lightbeam1 as beam3:
    pause 2.75
    alpha 0.0 yalign 0.8 xpos -400 rotate -40
    block:
        ease 0.25 alpha 0.6
    pause 0.2
    block:
        ease 1.0 rotate 40
        pause 0.5
        ease 1.0 rotate -40
        pause 0.5
        repeat
        
show lightbeam1 as beam4:
    pause 2.75
    alpha 0.0 yalign 0.8 xpos -1400 rotate 40
    block:
        ease 0.25 alpha 0.6
    block:
        ease 1.0 rotate -40
        pause 0.5
        ease 1.0 rotate 40
        pause 0.5
        repeat
        
pause 3.5

show lisia with dis

lisia @happy "Laaaaaadies and {i}gentlemen!{/i} Welcome to the first round of the two hundred and twenty-eighth annual Quarter Qlashes!"
lisia @sadbrow happymouth "I'm {i}sooooo{/i} sorry about the delay, but I'm sure the roaring-hot battles we're about to see will {i}more{/i} than make up for it!"

$ PlaySound("crowd_cheer.ogg")

pause 1.0

lisia @happy "That's what I like to hear! It's me, the one and only Lisia, World Contest Champion, ready to announce for you!"
lisia @talkingmouth "I'll be your host for all the Quarter Qlash battles in the Greater Inspira area this round, so I hope you don't get bored of me!"

$ PlaySound("crowd_cheer.ogg")

pause 1.0

lisia @happy "Awesome, awesome!"
lisia @sadbrow talkingmouth "Now, I'm sure {i}all{/i} the battles happening in this round are going to be {i}super{/i}-exciting, but I can really only commentate one battle at a time."
lisia @happy "So if I don't give your individual battles a play-by-play, then don't feel bad!"
lisia @xdbrow happymouth "Lisia's still watching you!"

$ PlaySound("crowd_cheer.ogg")

pause 1.0

redmind @thinking "Ten battles at a time? Twenty different battlers? No way she can watch {i}all{/i} of us at once."

pause 1.0

redmind @sweat closedbrow "But it's nice of her to say that, anyway. I think I get why this girl's so popular."

lisia @happy "Now, let's do a quick little interview with one of the battlers before we get things started--you all know I like to shine the spotlight on promising trainers!"
lisia angrybrow talking2mouth "Hm... how about..."

pause 1.0

red @surprised "Huh? She's looking right at me!"

lisia -angrybrow -talking2mouth @happy "You!"

show janine with dis:
    xpos 0.33
show lisia:
    ease 0.5 xpos 0.66 

pause 1.0

red @sweat "Oh."

lisia @happy "Hi there, Battler #1! How do you feel, having the first number in the entire Greater Inspira area Quarter Qlashes?"

janine @smirkmouth "Feels pretty good, Lisia."

lisia @talkingmouth "That's great! Now, what's your name? And what are you hoping to accomplish today?"

janine @smirkmouth "My name is Janine Koga. And I aim for nothing less than an overwhelming, dominating, victory."

lisia @surprised "Woah! Big words from our challenger, here! Do we think she can do it?"

$ PlaySound("crowd_cheer.ogg")

pause 1.0

lisia @happy "Awesome, awesome!~♥ Are you a student at Kobukan, then?"

show lisia surprisedbrow frownmouth with dis

janine @talking2mouth "Technically. I'm the Captain of the Battle Team."

lisia @talkingmouth "C-captain?"

pause 1.0

show janine surprisedbrow with dis
show lisia happy:
    ease 0.3 xpos 0.53
    block:
        ease 0.3 ypos 1.1
        ease 0.3 ypos 1.0
        repeat

lisia @talkingmouth "That's amazing! She {i}really is{/i} #1, folks!"

janine -surprisedbrow @sadbrow blush talking2mouth "Yeah. It's not... that big a deal..."

redmind @confusedeyebrows frownmouth "Huh. Janine actually looks a tiny bit sheepish in front of all these people."

show lisia:
    ease 0.5 xpos 0.66 ypos 1.0

lisia -happy @angrybrow happymouth "Well, if you're the Captain of the Battle Team, then you must be heading to the very top, right? You're aiming to get into the National Tournament?"

janine @closedbrow happyneutralmouth "Hm."

narrator "Janine leans into the microphone and says two words."

janine @angrybrow smirkmouth "{i}At least.{/i}"

$ PlaySound("crowd_cheer.ogg")

pause 1.0

lisia @happy "Powerful! Powerful words from Janine Koga, future champion of Kobukan, no doubt! I certainly wouldn't want to face her!"

narrator "Looking past Janine, where she walked from, you see that her opponent seems particularly green in the face."

hide janine with dis

show lisia:
    ease 0.5 xpos 0.5

lisia @happy "Well, I think we've all waited long enough, haven't we? Let's get these battles started, ladies and gents!"

$ PlaySound("crowd_cheer.ogg")

hide lisia with dis

pause 1.0

show oldman milotic angrybrow with dis

oldman @happymouth "Alright, whippersnapper! Time to show me what the Battle Team of Kobukan Academy is all about!"

red @happy "It'd be my pleasure, Sir!"

python:
    trainer1 = MakeRed()
    trainer2 = Trainer("oldman", TrainerType.Enemy, [Pokemon("Feebas", level=3, gender=Genders.Female), Pokemon("Kakuna", level=7, moves=[GetMove("Poison Sting"), GetMove("Harden")])], number=2)

call Battle([trainer1, trainer2], customexpressions=["red", "red angrybrow happymouth", "oldman milotic", "oldman angrybrow happymouth milotic"], specialmusic=("audio/music/swordshieldgym-intro.ogg", "audio/music/swordshieldgym-loop.ogg"), dialogfunc=oldmandialog) from _call_Battle_113 
$ battlehistory["OldMan1"] = _return

if (not WonBattle("OldMan1")):
    jump gameover

$ renpy.music.queue("Audio/Music/Indigo_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/Indigo_Loop.ogg", channel='music', loop=True, tight=None)

show oldman milotic surprisedbrow with dis:
    xpos 0.5

oldman @happymouth "By jove! That's quite a performance, young man!"

red @happy "Hey, it was fun."

oldman -surprisedbrow @happybrow happymouth "Fun? Bah! I've never been defeated so easily. I had a whale of a time, but I can't imagine it was any more fun for you than taking candy from a baby."

red @sweat happy "Well... this is the first battle of the first round of the Quarter Qlashes. Some matchups are going to be a bit unbalanced."

oldman @angrybrow happymouth "Well, lad, if you're going to sweep me off to the side, I hope to see you at the top! My pride as an old codger won't permit anything else!"

red @talkingmouth "I'll do my best, Sir."

oldman @happymouth "See that you do, young man."

pause 1.0

oldman surprisedbrow @happybrow happymouth "I'll put in a good word for you to my granddaughter. You know. {i}The{/i} Lisia. Surely you remember now?"

red @sweat happybrow happymouth "I really appreciate that, but I swear I'd never heard of her until a couple minutes ago."

pause 1.0

scene blank2 with Dissolve(2.0)

narrator "Shortly after, the battles finish, and everyone leaves the stadium's pit to make way for the next twenty battlers."

lisia @happy "Wow! Wasn't that amazing? Janine's Venomoth showed absolutely no hesitation in its attacks, and the sparkles of its toxic scales were {i}gorgeous{/i}! Perhaps our champion, Janine, has some potential as a coordinator?"

janine "{w=0.5}.{w=0.5}.{w=0.5}."

janine @angrybrow talking2mouth "What, like those girls who wear skirts and dance with their Pokémon?"

red @talking2mouth "Apparently, there's actually a lot more to it than that. You don't have to be a girl, for one."

janine @closedbrow talking2mouth "Weird. I don't get why anyone would want to be a coordinator when you could just battle, but I guess it's just not for me."

red @sweat closedbrow talking2mouth "Different strokes, different blokes."

stop music fadeout 1.5
stop music fadeout 1.0 channel "crowd"
stop music fadeout 2.0 channel "crowd2"

pause 2.0

queue music "audio/music/Eterna_Start.ogg" noloop
queue music "audio/music/Eterna_Loop.ogg"

janine @talking2mouth "Go talk to your friends."

red @surprised "Huh?"

janine @closedbrow talking2mouth "Classes are out for the rest of the week, because of the Quarter Qlashes. So this is the perfect opportunity to talk to some of the people who were hurt last Saturday, and patch things over with them."

red @talkingmouth "...I'm surprised you care about... well, my friends."

janine @surprisedbrow talkingmouth "Really?"

pause 1.0

janine @sadbrow talkingmouth "That... actually makes me a bit sad. I'm not heartless, you know. I mean, sure, I'm strict, but I've always said that working together is the best way to succeed as a team..."

red @surprised "W-wait! Sorry! I didn't mean to imply you were heartless or anything! I just... you're so tough, it's surprising to hear that you care about my friendships. Even if they're not battle team friendships, you know?"

janine @closedbrow talking2mouth "...Okay, I see where you're coming from."

janine @smirkmouth "You shouldn't confuse toughness with antisociality, though. One definitely doesn't imply the other."

red @sweat happy "Right..."

janine @closedbrow talking2mouth "Anyway, go on. I'll keep an eye on the next battles in the first round, in case I see anything interesting."

red @talking2mouth "Alright."

pause 1.0

red @sadbrow talkingmouth "...Thanks, Janine."

janine "{w=0.5}.{w=0.5}.{w=0.5}."

janine @talking2mouth "I--{w=0.5} I don't--"

pause 1.0

janine @closedbrow talking2mouth "I don't... 'believe in' people. I don't 'have faith.' I look at the evidence, and figure out from that if they're a person worth having in my team."
janine @sadbrow talking2mouth "...Not everyone does that. A lot of people who {i}do{/i} 'believe in' others are going to be really hurt by this. And they'll take that out on you. So..."

pause 1.0

janine closedbrow @talking2mouth "Harden your heart, [first_name]."

pause 1.0

red @sadbrow talkingmouth "That's good advice. I wish I could take it."

pause 1.0

janine @sadbrow talking2mouth "Mmm..."

scene blank2 with splitfade

pause 2.0

scene colosseum with splitfade

pause 1.0

show ethan with dis

ethan @talking2mouth "Hey, man."

red @talkingmouth "Hey."

pause 1.0

red @talkingmouth "What're you doing?"

ethan @talkingmouth "Going to grab some chips from the vending machine. I'm planning on watching a few more battles. Thought I'd get some refreshments while the second round is getting ready."

red @talkingmouth "I getcha."

pause 1.0

red @sadbrow talkingmouth "Hey. Are we... cool?"

ethan @talking2mouth "...Yeah, we're cool, man."

red @happy "Thanks."

ethan @talkingmouth "...I should probably let you know that I think I have this power as well."

red @surprised "Huh?!"

ethan @talkingmouth "Yeah. Pokémon listen to me, you know? Same as you."

ethan @closedbrow talking2mouth "Of course, the whole bit about 'people feeling what I feel' part... don't know how that shakes out, with all this."

red @closedbrow talkingmouth "Wait... is that why we've been syncing up?"

ethan @talkingmouth "I asked Professor Oak, and he said no. Probably. But I didn't tell him that I thought I had Frienergy as well, so... y'know, maybe that's it."

red @sadbrow talking2mouth "I'm sorry."

ethan @confusedeyebrows talking2mouth "Huh?"

red @talking2mouth "I had no idea that you had Frienergy."

ethan @happy "Man, you're saying it like it's a disease or something. Far as I can tell, Frienergy's exclusively a good thing."

red @closedbrow talking2mouth "...I've got a question.{w=0.5} Can you lie?"

ethan @sadbrow talkingmouth "Nope. Never have been."

red @talkingmouth "Huh. Maybe that's one of Frienergy's side effects, then. Some sort of... forced honesty. Or maybe we just realize, when we're younger, that no-one believes our lies anyway..."

ethan @closedbrow talking2mouth "Yeah... who knows."

pause 1.0

red @talkingmouth "How's the school?"

ethan @sad2eyes talking2mouth "Can't lie. It's been pretty bad. Everyone's really upset, and a lot of people have given up on the school year already."

red @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

ethan @talkingmouth "...Hey, don't look so down, buddy! People'll cheer up eventually. You just gotta wait for them to be in better [bluecolor]moods{/color}."

red @closedbrow talking2mouth "Huh?"

ethan @surprised "Wait, you don't know about [bluecolor]moods?{/color}"

red @talkingmouth "I mean... I know what a mood is, like... the noun..."

ethan @sad2eyes talking2mouth "Yeah, it figures... a popular, friendly guy like you, you've probably only ever had to deal with people in good moods, huh?"

red @angrybrow talking2mouth "Hey. I grew up with Blue yelling at me pretty much every day."

ethan @confusedeyebrows playfuleyes talking2mouth "Yeah, but you realize he {i}likes{/i} arguing, right? Dude's never happier than when he's yelling at someone."

red @surprised "Huh?"

ethan @talkingmouth "Whatever, dude. Here, let me explain how [bluecolor]moods{/color} work..."

show blank2 with dis

python:
    usingmoods = True
    persondex["Blue"]["Mood"] = (-5 if GetRelationshipRank("Blue") == 0 else 0)
    persondex["Blue"]["Nature"] = (TrainerNature.Distant if GetRelationshipRank("Blue") == 0 else TrainerNature.Moody)
    persondex["Silver"]["Mood"] = (-5 if GetRelationshipRank("Silver") == 0 else 0)
    persondex["Leaf"]["Mood"] = (10 if HasEvent("Leaf", "AcceptedConfession") else 5)
    persondex["Calem"]["Mood"] = (0 if GetRelationshipRank("Serena") == 0 else 5)
    persondex["Hilbert"]["Mood"] = (-5 if GetRelationshipRank("Hilbert") == 0 else 0)
    persondex["Brendan"]["Mood"] = (5 if mayhaslarvesta else -6)
    persondex["Brendan"]["Nature"] = (TrainerNature.Friendly if mayhaslarvesta else TrainerNature.Moody)
    persondex["May"]["Mood"] = ((0 if GetRelationshipRank("May") == 0 else 5) if mayhaslarvesta else -6)
    persondex["May"]["Nature"] = (TrainerNature.Neutral if mayhaslarvesta else TrainerNature.Moody)
    persondex["Flannery"]["Mood"] = (0 if GetRelationshipRank("Flannery") == 0 else 5)
    persondex["Whitney"]["Mood"] = (0 if GetRelationshipRank("Whitney") == 0 and GetRelationshipRank("Flannery") == 0 and GetRelationshipRank("Tia") == 0 else 5)
    persondex["Sabrina"]["Mood"] = (-10 if GetRelationshipRank("Sabrina") == 0 else 0)
    persondex["Serena"]["Mood"] = (0 if GetRelationshipRank("Serena") == 0 else 5)
    persondex["Cheren"]["Mood"] = -10
    persondex["Misty"]["Mood"] = (-5 if GetRelationshipRank("Misty") == 0 else 0)
    persondex["Bianca"]["Mood"] = 5
    persondex["Dawn"]["Mood"] = (-5 if GetRelationshipRank("Dawn") == 0 else 0)
    persondex["Nate"]["Mood"] = 5
    persondex["Rosa"]["Mood"] = (0 if GetRelationshipRank("Rosa") == 0 else 5)
    persondex["Bea"]["Mood"] = (0 if GetRelationshipRank("Bea") == 0 else 5)
    persondex["Nessa"]["Mood"] = (0 if GetRelationshipRank("Nessa") == 0 else (5 if GetRelationshipRank("Sonia") == 0 else 10))
    persondex["Hilda"]["Mood"] = (-5 if GetRelationshipRank("Hilda") == 0 else 5)
    persondex["Skyla"]["Mood"] = (0 if GetRelationshipRank("Skyla") == 0 else 5)
    persondex["Erika"]["Relationship"] = "Teammate"
    if (persondex["Hilbert"]["Relationship"] == "Dormmate"):
        persondex["Hilbert"]["Relationship"] = "Teammate"
    persondex["Erika"]["Mood"] = -10
    persondex["Tia"]["Mood"] = 10
    persondex["Sonia"]["Mood"] = (-5 if GetRelationshipRank("Sonia") == 0 else 10)
    persondex["Jasmine"]["Mood"] = (0 if GetCharValue("Jasmine") <= 3 and GetCharValue("Grusha") <= 2 else 5)
    persondex["Grusha"]["Mood"] = (-5 if GetCharValue("Jasmine") <= 3 and GetCharValue("Grusha") <= 2 else 0)
    persondex["Gardenia"]["Mood"] = (5 if investment > 0 else 0)
    persondex["Falkner"]["Nature"] = TrainerNature.Special
    persondex["Brawly"]["Nature"] = TrainerNature.Special
    persondex["Roxanne"]["Nature"] = TrainerNature.Special

    for name, person in persondex.items():
        if (GetNature(name) != TrainerNature.Special and GetMood(name) == 0):
            person["Mood"] = -3

narrator "[bluecolor]From now on, characters will have \"Moods\". Depending on the character's personality, their mood will change day by day.{/color}"
narrator "[bluecolor]You increase (or decrease) the mood of a character by increasing (or decreasing) your bond level with them.{/color}" 
narrator "[bluecolor]If their mood is positive at the start of the day, your bond level with them will increase. If it is negative, it will decrease.{/color}"
narrator "[bluecolor]Moods slowly return to neutral over time, so keep an eye on the moods of characters you want to become closer to!{/color}"
narrator "[bluecolor]There are no additional benefits to raising a mood over 10, so if your favorite character already has a mood of 10 or more, try increasing your bonds with another character!{/color}"
narrator "[bluecolor]Finally, your socials page now displays a person's current mood.{/color}"

pause 1.0

scene clouds
show garden:
    zoom 0.625
show ethan
with splitfade

ethan @talkingmouth "You get it?"

red @sadbrow talkingmouth "I... guess I do. I dunno, though... leaving a person alone after a while, just because there's 'no additional' benefits... feels kinda manipulative..."

ethan @closedbrow talking2mouth "It's not. Figuring out when people need their space is just part of putting effort into a relationship."

pause 1.0 

ethan @playfuleyes confusedeyebrows talking2mouth "{size=30}Which is something {i}most of us{/i} have to do.{/size}"

red @sadbrow talking2mouth "I guess..."

ethan @happy "You'll get used to it, bud. Now, I think there's a bag of Torchips calling my name, so I'll see you later."

show ethan surprisedbrow frownmouth with dis

red @talkingmouth "Oh, yeah. See you back at the dorm."

pause 1.0

red @confused "What?"

ethan sad2eyes talking2mouth "Er... nothing. I'll tell you later."

red @confusedeyebrows closedeyes talking2mouth "Alright."

hide ethan with dis

pause 1.0

if (investment > 0):
    narrator "You are just about to leave the garden when you notice someone walking around the corner."

    show gardenia frownmouth sadbrow with dis:
        xpos 1.1 zoom 0.8
        ease 3.0 xpos 0.3

    pause 3.5

    red @sadbrow talkingmouth "Hey."

    show gardenia surprisedbrow frownmouth with dis

    pause 2.0

    show garden 
    show gardenia happy with dis:
        xpos 0.3 zoom 0.8
        ease 0.3 ypos 1.2 zoom 1.3 xpos 0.5
    with vpunch

    gardenia -happy @happy "[first_name]! You came back!"

    red @surprised "W-woah! I didn't expect such a... positive reaction...?"

    show gardenia:
        xpos 0.5 ypos 1.2 zoom 1.3
        ease 0.5 ypos 1.0 zoom 1.0

    gardenia @happy "We're business partners, aren't we?"
    gardenia @happybrow talking2mouth "I always make sure to pay the people who invest with me."
    gardenia sadbrow frownmouth @sadmouth "And... when you were gone..."

    pause 1.0

    gardenia @angry "I thought I'd have to {i}mail{/i} you your dividends!"
    gardenia @angry "Like, use actual {i}snail mail{/i}! Do you know how much time that would take? My profit margins would be absolutely {i}ruined!{/i}"

    red @sweat talking2mouth closedbrow "Oh."

    pause 1.0

    gardenia @sadbrow talking2mouth "I'm kidding, dude."

    red @surprised "Oh!"

    red @confused "...Then why?"

    gardenia @talkingmouth "It's... complicated."
    gardenia -sadbrow @talking2mouth "I don't think you're a bad dude, for one. I've worked with some bad dudes before."
    gardenia @talkingmouth "Some people are just scared of commitment. The moment they sign a contract, it's like a switch flips in their head that says 'bail!'"

    pause 1.0

    red @sadbrow talking2mouth "I... {i}did{/i} bail, though."

    gardenia @talkingmouth "Yeah, but you came back. The {i}one thing{/i} I can't stand is when people just...{w=0.5} {i}ghost{/i} me. So, thanks for coming back."

    pause 1.0

    gardenia @talking2mouth "So... do you have mind control powers?"

    redmind @thinking "...This is going to be all I'll be doing for the next week, isn't it."

    pause 1.0

    narrator "You explain the true nature of Frienergy to Gardenia."

    pause 1.0

    gardenia @talkingmouth "Well, that {i}sounds{/i} like a fat load of Tauros crap."

    red @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    gardenia -frownmouth @talking2mouth "But, you know, I was already primed to believe that you had mind control powers, so, honestly, the goalposts had shifted so far that 'I make you feel empathy' is kinda reasonable."

    pause 1.0

    gardenia @sadbrow happymouth "Besides... there's one other thing that makes me believe you."

    red @confused "My wallet?"

    gardenia @talkingmouth "I mean, if you're willing to pay me to believe you, I'll take it. But that wasn't what I was thinking, no."
    gardenia @happybrow talking2mouth "No, the reason I believe you is... 'cause I believe you, dude. Something this out-there? This unbelievable? This wild? No way I should believe it. But I do. And I guess that's 'cause I can tell you're telling the truth."

    red @closedbrow talkingmouth "That seems like a tautology."

    gardenia @angrybrow talkingmouth "There's no way you know what a tautology is."

    red @surprised "Wait, does that mean I used that word correctly?"

    gardenia @talkingmouth "Whatever, dude. Look, things're going to be a bit weirder between us--between you and everyone else in the school, really--but it's not like I'm going to hold this against you or anything."
    gardenia @talking2mouth "We have a deal. And I never back out of deals. {size=20}Unless the contractual provisions have undergone modifications resulting in a pecuniary detriment to my interests.{/size}"

    red @confused "Huh?"

    gardenia @happy "Don't worry about it."

    red @talking2mouth "...Alright."

    if (highestbank > 0):
        gardenia @happy "Oh, by the way, here's your dividends from the bank. I was saving 'em for you."
        $ investmentbulk = math.floor(highestbank * 0.01 * 3)
        $ money += investmentbulk
        narrator "Gardenia hands you $[investmentbulk]--three days' worth of investment."

    red @talkingmouth "Thanks."

    narrator "You turn to leave, when..."

    show gardenia sadbrow frownmouth with dis:
        ease 0.3 ypos 1.2 zoom 1.3

    gardenia @talkingmouth "Hey."

    red @surprised "Yeah?"

    gardenia @talkingmouth "...People are going to be... more suspicious of you, now."

    red @closedbrow talking2mouth "Hm?"

    gardenia @talkingmouth "I get it. And I don't blame them. I'm used to it. Whenever I talk to someone, people think I'm just trying to get money from them, so... you know, I don't really have any friends... just business partners."
    gardenia @talkingmouth "And I think that you might... see something similar."

    pause 1.0

    gardenia -sadbrow -frownmouth @happy "Don't let it get to you, [first_name]."

    red @talkingmouth "...Alright, Gardenia. Thanks."

    $ AddEvent("Gardenia", "Makeup")

scene blank2 with splitfade

redmind @thinking "Alright... now, where should I go first?"

$ makeupresearchcenter = False
$ makeupbaseballfield = False
$ makeuprecreationcenter = False
$ makeupaurahall = False
$ makeuprelichall = False
$ makeuppledgehall = False
$ makeupinspira = False

label makeupoptions:

scene map
call screen makeup(_with_none=False) with Dissolve(1.0)
with Dissolve(1.0)

if (_return == "Outside"):
    red @closedbrow talkingmouth "I don't think anyone would be hanging around in the fields right now..."

elif (_return == "Battle Hall"):
    red @closedbrow talkingmouth "The cheers of the crowd are still pretty loud... I don't think I could have a normal conversation there right now."

elif (_return == "Baseball Field"):
    if (makeupbaseballfield):
        narrator "There doesn't appear to be anything happening here right now."

    elif (timeOfDay in ["Morning", "Noon"]):
        narrator "You can hear Flannery screaming at the top of lungs. Even for her, this sounds bad."

        narrator "You decide to return later."

    else:
        scene baseball with splitfade

        stop music fadeout 1.5
        queue music "audio/music/goldenrod_start.ogg" noloop
        queue music "audio/music/goldenrod_loop.ogg"

        narrator "As you walk towards the Baseball Field, you see Flannery and Whitney sitting in the grass and talking quietly. You quickly hide in the dugout."

        show flannery sadbrow frownmouth:
            xpos 0.33
        show whitney sadbrow frownmouth:
            xpos 0.66
        with dis

        pause 2.0

        flannery @talking2mouth "I'm sorry I was a bit of a bitch."

        whitney @talking2mouth "I'm sorry I was even bitchier."
        whitney @sad "But I promise I didn't {i}really{/i} think of you as a project, okay? It's... it was a defense mechanism."

        flannery @talking2mouth "A defense mechanism?"

        whitney @talking2mouth "Look... I like you. And, you know, I'm a lesbian..."

        flannery @talking2mouth "I'm not gay, Whit."

        whitney @surprised "I know! {size=25}And you're really missing out,{/size} but that's totally fine. But I can't just... {i}not{/i} be into you, you know?"
        whitney @sadbrow talking2mouth "So if I thought of you as someone I was helping {i}as well as a friend{/i}... instead of {i}just{/i} a friend... I could live with that."

        pause 1.0

        flannery @talking2mouth "...I was scared, Whit."
        flannery @closedbrow talking2mouth "I was scared that... your patience would run out. I know it's not easy to get along with me."
        flannery -frownmouth @sadbrow happymouth "You basically have to be friends with two separate people. And I don't think there's anyone in this school who'd be willing to put up with me, other than you."

        if (GetRelationshipRank("Flannery") == 1):
            whitney @talking2mouth "What about [first_name]?"

            flannery frownmouth @surprisedbrow talking2mouth "Huh?"

            whitney @talking2mouth "Aren't you pretty good friends with him?"
            whitney @happy "Like, you've been hanging out a lot after school, and stuff, right?"

        else:
            whitney @talking2mouth "What about Tia?"

            flannery frownmouth @surprisedbrow talking2mouth "Huh?"

            whitney @talking2mouth "Aren't you pretty good friends with her?"
            whitney @happy "Like, you've been reading your fanfics to her, right?"

        flannery @talking2mouth "...So, you know about that..."

        whitney -frownmouth @happy "Don't worry about it, Flan! You're {i}allowed{/i} to have other friends! How many times have I said you should, anyway?"

        flannery @talking2mouth "I... thanks."

        pause 1.0

        flannery @talking2mouth "When... when I heard Sabrina say that you called me a project... that scared me."

        whitney frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

        flannery @talking2mouth "I haven't really been able to... you know, do the normal teenage stuff. I was too busy with the Lavaridge Gym. So I thought that you... I mean..."
        flannery @happy "You're friends with everyone, Whit. You collect friends like most people collect clothes."
        flannery @talking2mouth "So I thought that... you'd be easy to be friends with. You'd be easy to {i}be normal{/i} with."

        whitney "{w=0.5}.{w=0.5}.{w=0.5}."

        flannery @happy "I guess I was using you, as well... but I guess you already knew that... And I thought if... if I was angry first, that you couldn't be mad at me..."

        whitney @talking2mouth "Nope."

        flannery @surprised "Huh?"

        whitney @talking2mouth "I didn't hear any of that."

        flannery @surprised "Uh... really?"

        whitney @talking2mouth "Yup. I just heard a bunch of secrets about who was cheating on who."
        whitney @closedbrow talking2mouth "Turns out there are a {i}lot{/i} of scumbags in this school."

        flannery @talking2mouth "Oh."

        pause 1.0

        flannery @talking2mouth "I guess we all heard different things, then."

        pause 1.0

        flannery -sadbrow @talking2mouth "But you heard the bit about [first_name], right?"

        whitney -sadbrow -frownmouth @surprised "Oh, yeah, what was that about? Mind control? Say {i}whaaaaat?{/i}"

        flannery @talking2mouth "I don't know why [first_name] freaked out up there, but personally, I think Cheren's full of it."

        if (GetRelationshipRank("Flannery") == 1):
            flannery @angry "Mind control? Get real! [first_name]'s an awesome dude who's one of the few people patient enough to deal with me in the morning!"
        
        else:
            flannery @angry "Mind control? Get real! [first_name]'s just a regular guy. I mean, we haven't talked {i}that{/i} much outside of classes, but if he was actually controlling people's minds, there's no way he'd put up with me in the morning."

        flannery @talking2mouth "Besides, I don't think mind control is even a real psychic power. Moving stuff with your mind, I get. Reading minds? Makes sense. But controlling minds? I don't think that's a real thing."

        show flannery surprisedbrow frownmouth with dis

        whitney @talking2mouth "Oh. Um... it is, actually. It's in the Diagnostic and Statistical Manual of Esper Powers. It's extremely uncommon, even amongst powerful Espers, but... yeah."

        flannery -surprisedbrow @surprised "Oh."
        flannery @sadbrow talking2mouth "Does that mean he... {i}does{/i} have powers, then?"

        whitney @talking2mouth "Oh, n-no! No way. Well, yeah? A little bit. Tia told me about it."

        if (IsDate(5, 5, 2004)):
            flannery @surprised "What, Tia's here?! She's been missing for, like, a whole day!"

            whitney @surprisedbrow talking2mouth "Oh. Yeah. She just got back."

            flannery @tiredbrow talking2mouth "From what?"

            whitney @talking2mouth "I think she said she went to a water park? There was a lot of water, anyway."

        flannery @closedbrow talking2mouth "Why am I always the last to learn these things...?"

        whitney @talking2mouth "Because you spent your childhood memorizing the ship names of every single character on Galarian television instead of learning sign language?"

        flannery @closedbrow talking2mouth "That's a very clinical answer, Nurse Whitney."

        pause 2.0
        
        flannery @closedbrow talking2mouth "Alright. Well, what power {i}does{/i} [first_name] have?"

        whitney @talking2mouth "Okay. So, what Tia told me was..."

        pause 1.0

        show flannery surprisedbrow frownmouth with dis

        narrator "Whitney explains the true nature of Frienergy to Flannery."

        pause 2.0

        flannery @talking2mouth "Wow. Didn't see that coming."

        if (WonBattle("FlanneryGardenia1")):
            flannery @angry "Wait, so that means during that gamble battle a couple weeks ago, he only won because he had superpowers!"

            flannery @tiredbrow talking2mouth "...That guy owes me $2,000."

        else:
            flannery @happy "Hey, so that means that when I beat him in that gamble battle a couple weeks ago, I won {i}despite{/i} the fact he had superpowers."

        whitney @surprisedbrow talking2mouth "That's what you're getting from this?"

        flannery @happy "Whit, I blow up at people, for no reason, basically becoming a different person. Making people understand your feelings a bit better isn't that weird."

        flannery @closedbrow talking2mouth "Though I'll admit I'm a bit jealous that he can just get Pokémon to listen to him. It's whatever."

        pause 1.0

        whitney @closedbrow talking2mouth "You don't turn into a different person, Flannery."

        flannery @surprised "Huh?"

        whitney @talking2mouth "It's always the same you. I can feel the anger you've buried in the afternoon. And I can feel your happiness in the morning, too."
        whitney @talking2mouth "It's {i}all{/i} one Flan. And I'm friends with all of you."

        pause 1.0

        flannery -surprisedbrow -frownmouth -surprised @closedbrow talking2mouth "...Thanks, Whit. No hard feelings about earlier?"

        whitney @happy "If you've got none for me."

        hide whitney
        hide flannery
        with dis

        flannery @angrybrow happymouth "So, you know that fanfic you commissioned? {size=32}Cynthia.{/size} {size=28}Steven.{/size} {size=24}A hot{/size} {size=20}tub.{/size} {size=16}And fifty pounds of butter...{/size}"

        pause 1.0

        narrator "...Flannery and Whitney walk out of earshot."

        pause 1.0

        narrator "You decide to leave."

        $ makeupbaseballfield = True

elif (_return == "Aura Hall"):
    if (makeupaurahall):
        narrator "There doesn't appear to be anything happening here right now."

    else:
        scene relichall_A with splitfade

        stop music fadeout 1.5
        $ renpy.music.queue("Audio/Music/Vaniville_Start.ogg", channel='music', loop=None, fadein=0.0, tight=None)
        $ renpy.music.queue("Audio/Music/Vaniville_Loop.ogg", channel='music', loop=True, tight=None)

        narrator "As you walk towards Aura Hall, you see Leaf's roommates talking with each other. They seem to be waiting for something, or someone."

        if (IsDate(5, 5, 2004)):
            narrator "They all carry bags or suitcases with them."

        show serena frownmouth:
            xpos 0.2
        show may frownmouth:
            xpos 0.4
        show bianca:
            xpos 0.6
        show hilda frownmouth:
            xpos 0.8
        with dis

        pause 2.0

        hilda @talkingmouth "...Guess this is it, then."

        may @sadmouth "...I'll miss you guys."

        serena @talkingmouth "Oh, we'll still see each other, May. We take Fire classes together, after all."

        hilda @talkingmouth "Yeah... and we can still, like, chat at lunch, or whatever."

        pause 1.0

        may @closedbrow sadmouth "I don't like change..."

        bianca @happy "Change is good! You can't ever {i}really{/i} know what your goal is unless you take the steps to walk toward it."

        hilda @happy "Heh. I'm going to miss your unfailing optimism in my new dorm, Bianca."

        bianca @happy "No you woooon't!~"

        hilda surprisedbrow @surprised "Huh?"

        bianca @talkingmouth "We're dorming together in the new dorm, too!"

        hilda @surprised "...Wait, how do you know?"

        bianca @talkingmouth "Because I'm friends with Nate, and I know Hilbert wants to room with Nate, and I know you want to room with Hilbert, and I want to room with you and Hilbert, so it just makes sense if we room together!"

        hilda -surprisedbrow @closedbrow talkingmouth "Uh... yeah, I guess that's true..."

        hilda @sadbrow talking2mouth "Are you sure that you want to dorm with Hilbert, though? You're kinda setting yourself up for... a {i}really{/i} tough time."

        bianca @happy "I'm already the go-fer for the entire school. It might be nice to help a single person for a while."
        bianca @talkingmouth "Besides, Ms. Miriam is always saying that the most important part of a nurse's job is handling different personalities."

        hilda -frownmouth @closedbrow smirkmouth "Rock on. Thanks, Bianca."

        serena @talkingmouth sadbrow "Well, I'm glad that you two will still have a friendly face to fall back on."

        may @surprised "What do you mean, Serena? Aren't you rooming with Calem?"

        serena @sadbrow talkingmouth "...Yes, but..."

        pause 1.0

        may @surprised "But?"

        serena @sadbrow sadmouth "It's... not as I dreamed it."

        hilda @angrybrow talkingmouth "Hey, isn't the {i}entire{/i} reason you tried to get on the student council so you could dorm with him?"

        serena poutbrow poutmouth "No!"

        pause 2.0

        serena -poutbrow -poutmouth frownmouth @sadbrow talkingmouth "Not... entirely."

        pause 1.0

        serena @talkingmouth "We've had some conversations since then. And things are different." 
        serena @sadbrow talkingmouth "I {i}wanted{/i} this, but... I don't know... this seems too sudden."

        hilda @closedbrow smirkmouth "Heh."

        may @angry "Hilda!"

        hilda @happy "Sorry, sorry!"

        serena @sadbrow talkingmouth "No, May, it's alright. This {i}is{/i} rather... funny, isn't it? I'm like a Houndour chasing cars. I've no idea what to do when the car stops."

        may @happy "Don't worry about it, Serena. You'll figure it out. And Calem's a great guy. Super gentlemanly."

        serena @closedbrow sadmouth "...Yes. He is."

        pause 1.0

        hilda @talkingmouth "Well, what are your dorm plans, May?"

        may @talkingmouth "I'm dorming with Brendan. He says he's found a guy to dorm with, so I guess I'm going to meet some new people." 
        may @closedbrow happymouth "I'll sure miss you guys, though."

        hilda @happy "Well, like Serena said. We'll see each other at lunch, classes, stuff like that. Maybe we can even meet up in clubs."

        may @surprised "Is there a chance you'll join the Coordinator's club?"

        hilda @sadbrow talkingmouth "...{i}Technically.{/i}"

        serena @talkingmouth "How are things with Brendan?"

        may @talkingmouth "...It was difficult. But we've agreed we're going to talk to each other more openly about... everything."

        if (GetRelationshipRank("May") == 1):
            may @closedbrow sadmouth "...[first_name] was right. I should have just talked to Brendan a long time ago."

        else:
            may @closedbrow sadmouth "It's dumb that [first_name] had to be accused of having mind-control powers to get us to do that."

        bianca @talkingmouth "What do you think about him?"

        if (GetRelationshipRank("May") == 1):
            may @talkingmouth "I trust him. He's a good friend."

        else:
            may @closedbrow "{w=0.5}.{w=0.5}.{w=0.5}."

        if (GetRelationshipRank("Serena") == 1):
            serena @talkingmouth "I do not believe it is possible for someone with his personality to do the sort of thing Cheren accused him of."

            serena @closedbrow sadmouth "Even if he... {i}does{/i} have these powers."

        else:
            serena @closedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

        if (GetRelationshipRank("Hilda") == 1):
            hilda @angrybrow talkingmouth "He goes out of his way to do shit for me. Even if I told him not to. It's a tiny bit annoying, but that kinda guy isn't going to be some evil mastermind, you know?"

        else:
            hilda @closedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

        bianca @happy "Well, I don't think he's a mind-controller! That's an {i}extremely{/i} rare Esper power."

        bianca @talkingmouth "If he had that power, I'm pretty sure none of us would know."

        hilda @talkingmouth "Oh, yeah? Where are you getting that from?"

        bianca @talkingmouth "My AP Psychology class."

        pause 1.0

        hilda @talkingmouth "Yup. That'd do it."

        pause 1.0

        hilda @talkingmouth "Alright. Let's go. I've got my battle in a while, so..."

        hide hilda
        hide may
        hide bianca
        hide serena
        with dis

        bianca "Have you ever noticed how {size=32}we only{/size} {size=28}ever stand{/size} {size=24}around and{/size} {size=20}talk{/size} {size=16}about boys?{/size}"

        pause 1.0

        narrator "...The girls walk out of earshot."

        pause 1.0

        narrator "You decide to leave."

        $ makeupaurahall = True

elif (_return == "Relic Hall"):
    if (makeuprelichall):
        narrator "There doesn't appear to be anything happening here right now."

    else:
        scene lobby with splitfade

        stop music fadeout 1.5
        
        $ renpy.music.queue("Audio/Music/Littleroot_Start.ogg", channel='music', loop=False, fadein=1.0, tight=None)
        $ renpy.music.queue("Audio/Music/Littleroot_Loop.ogg", channel='music', loop=True, fadein=0.0, tight=None)

        narrator "As you walk towards your own dorm, you're surprised to see your roommates standing around in the lobby."

        if (IsDate(5, 5, 2004)):
            narrator "They all carry bags or suitcases with them."

        show brendan frownmouth:
            xpos 0.75
        show calem:
            xpos 0.25
        show hilbert:
            xpos 0.5
        with dis

        pause 2.0

        brendan @talking2mouth "...Bye, then."

        hilbert @closedbrow talkingmouth "Don't be so dramatic. We'll still see each other at lunch."

        brendan @closedbrow talking2mouth "Whatever, man. I'm still going to miss you, even if you want to be all moody about it."

        calem @talking2mouth "I will miss you, too."

        pause 1.0

        calem @sad "And... Ethan and [first_name], of course."

        pause 1.0

        brendan @sadbrow talking2mouth "...I wish Ethan wasn't mad at us."

        calem @talking2mouth "We need to give him, like the rest of the school, time to cool down. We can apologize after."

        pause 1.0

        calem @talking2mouth "...The same goes for [first_name]."

        brendan @surprised "Huh?"

        calem @surprised "Hm? Surely you must be aware that [first_name] has returned?"

        brendan @sad "Man, I had no idea..."

        hilbert @talkingmouth "I knew. I didn't care."

        if (GetRelationshipRank("Hilbert") == 1):
            if (IsDate(5, 5, 2004)):
                narrator "Hilbert's fist tightens around the small Vanillite-shaped nightlight you bought him."
            else:
                narrator "Hilbert's jaw clenches, as though he dares the others to defy this claim."

        calem @closedbrow talking2mouth "I wonder where he'll be dorming."

        brendan @talking2mouth "I wonder if he's really got mind-control powers."

        pause 1.0

        calem @talking2mouth "Cheren ruined a lot of my plans. A lot of {i}everyone's{/i} plans. But... even so..."
        calem @closedbrow talking2mouth "I care more about [first_name]'s well-being than my own."

        pause 1.0

        hilbert @closedbrow talkingmouth "Sounds like Cheren was right."

        calem @talking2mouth "Or maybe [first_name] was. How would this differ if he {i}had{/i} said something? If he had protected himself?"
        calem @angrybrow talking2mouth "Do we have any proof that this is not the ideal outcome for the majority?"

        hilbert @sadbrow talkingmouth "...Pathetic. You're trying so hard to rationalize this away. Who's the easiest to pin the blame on? [first_name], Sabrina, and Cheren."
        hilbert @closedbrow talking2mouth "Anything else is just overcomplicating the issue."

        calem @angrybrow talking2mouth "Ease of comprehension does not equal truth."

        hilbert @sadbrow talkingmouth "Who cares about the truth?"

        brendan @talking2mouth "You should, man. I was lyin' to May, and I nearly ruined things for us."

        hilbert @closedbrow talkingmouth "That's your fault for bringing another person into your life."

        pause 1.0

        hilbert @sadbrow talkingmouth "On that note..."

        hide hilbert with dis

        pause 1.0

        calem @closedbrow talking2mouth "...Goodbye, Brendan. It's been a pleasure."

        brendan @talking2mouth "...Hey, man. Can I ask you somethin'?"

        calem @talkingmouth "Of course."

        show calem surprisedbrow with dis

        brendan sadbrow @talking2mouth "How do I... get smart?"

        pause 1.0

        calem @talking2mouth "What do you mean? Brendan, you're emotionally intelligent, you've got an excellent sense of design, you're fastidious, you're..."

        brendan @closedbrow talkingmouth "Nah, man. I'm not asking about any of that. It's, like... you. How do I be more like you?"

        calem -surprisedbrow @sad "If you think of me as intelligent, you might want to consider the events of last Saturday. It was my own utter stupidity that caused that."

        brendan @talking2mouth "...Dude, just listen to how you talk. This is your second language, but you speak like a... like a freakin' politician."

        calem @talking2mouth closedbrow "Well... that {i}was{/i} the dream."
        calem @talking2mouth "But a tendency towards sesquipedalian loquaciousness does not imply intelligence. The ability to paraphrase is a far stronger indicator."

        pause 1.0

        calem @closedbrow talkingmouth "Brendan, you're plenty intelligent. I've seen how much your girlfriend adores you, and you, her. Anyone who can engender that level of passion must be doing the right thing."

        pause 1.0

        calem @sad "Is... is there some reason you're worried about your intelligence? Did you, too, hear something on Saturday?"

        pause 1.0

        brendan "{w=0.5}.{w=0.5}.{w=0.5}."
        brendan @talking2mouth "I..."

        pause 1.0

        brendan @closedbrow talking2mouth "Let's talk about this later, bro."

        calem @talking2mouth "Very well."
        calem @talking2mouth "We'll have plenty of room in our dorm together, after all."

        brendan -sadbrow -frownmouth @surprised "We're dormin' together, dude? Again?"

        calem @talkingmouth "I'd rather like to. If you have no objections. I've found you to be a reliable friend. And your presence doesn't come with the... complicated feelings of our other roommates, though I'll miss them."

        brendan @happy "Awesome! I'd love to do that, then, dude! Looks like the band's not splitting up after all!"

        calem @talkingmouth "Perhaps not. Or, at least, not entirely."

        hide brendan
        hide calem
        with dis

        brendan "So, hey, what do you think {size=32}about Lisia?{/size} {size=28}She's kinda{/size} {size=24}like super{/size} {size=20}famous and{/size} {size=16}her style is...{/size}"

        pause 1.0

        narrator "...Your former roommates walk out of earshot."

        pause 1.0

        narrator "You decide to leave."

        $ makeuprelichall = True

elif (_return == "Pledge Hall"):
    if (makeuppledgehall):
        narrator "There doesn't appear to be anything happening here right now."

    else:
        scene blank2 with dis

        pause 1.0

        narrator "As you get closer, you hear the sound of a fight..."

        narrator "Proceed?"

        if (len(playerparty) == 1):
            narrator "[bluecolor]You may want to go to the city first, to pick up some more Pokémon...{/color}"

        menu:
            ">Proceed":
                pass

            ">Secede":
                jump makeupoptions

        scene relichall_A with splitfade

        show screen songsplash("Embracing One's Duty", "Zame")
        stop music fadeout 1.5
        queue music "audio/music/embracingonesduty.ogg"

        narrator "As you walk towards Pledge Hall, you quickly see three figures engaged in a pitched battle with a Ninetales. It howls fiercely as hail rains down in the middle of an otherwise sunny day."

        show aninetales:
            xpos 0.85 xanchor 0.5 yanchor 1.0 ypos 1.2
            block:
                ease 2.0 ypos 1.23
                ease 2.0 ypos 1.2
                repeat
        show silver angrybrow:
            xpos 0.55
        show cheren angrybrow noshine:
            xpos 0.7
        show skyla angrybrow frownmouth:
            xpos 0.65
        with dis
        
        pause 1.0

        silver @angry "Damn! What's with this thing?!"

        cheren @sadmouth "Its movements are too erratic... it's too strong."

        show blank

        pause 0.1

        hide blank

        pause 0.1

        show silver angrybrow:
            xpos 0.55
            block:
                ease 0.3 xpos 0.1
            block:
                ease 0.05 rotate 3
                ease 2.0 rotate 0
        show cheren angrybrow noshine:
            xpos 0.7
            block:
                ease 0.3 xpos 0.2
            block:
                ease 0.05 rotate 3
                ease 1.0 rotate 0
        show skyla angrybrow frownmouth:
            xpos 0.65
            block:
                ease 0.3 xpos 0.35
            block:
                ease 0.05 rotate 3
                ease 1.5 rotate 0
        show aninetales:
            xpos 0.75
            block:
                ease 0.3 xpos 0.6
                pause 1.5
                ease 1.5 xpos 0.85
            block:
                ease 2.0 ypos 1.23
                ease 2.0 ypos 1.2
                repeat

        skyla @surprised "Gah! I didn't see that coming..."

        silver @angry "Oh, really? You didn't see it using Blizzard for the fifth time?! It's not like that's {i}all{/i} it's been doing!"

        skyla @talkingmouth "Well, you're not being much help either! I don't like them, but shouldn't your Poison-types be able to hit it really hard?"

        silver @angry "They {i}would{/i}, if I wasn't getting freeze-haxxed every goddamn second!"

        cheren @closedbrow sadmouth "This internal argument is not helpful. We should--"

        skyla @angry "Then maybe you should try harder to make sure your Pokémon don't get hit!"

        silver @angry "Oh, sure, let me just take a second to teach my Skorupi {i}fly!{/i} If you two weren't ducking out of the way of its hits all the time, maybe I wouldn't be its only targets!"

        cheren @sad2eyes sadmouth "If I didn't avoid its attacks, I would go down in a single blow."

        silver @talkingmouth "You might as well, for as much use as you're being!"

        pause 1.0

        cheren shadow @sad2eyes talking2mouth "May I suggest that you leave this fight to us for a moment, and go fetch your stronger Pokémon?"

        silver @sadbrow talking2mouth "You guys can't hold this thing here for a whole half an hour by yourself!"

        cheren @sadmouth "I think... {i}perhaps{/i} we do not need to."

        skyla @surprised "Huh?"

        cheren @sadmouth "I'd like to test something."

        show cheren:
            ease 3.0 xpos 0.65

        silver @sadbrow talking2mouth "{size=30}...Great, he wants to test 'how quickly can I die?'{/size}"

        skyla @surprised "Don't worry, I'll save you! Cheren, I--"

        cheren @surprisedeyes surprisedmouth "Halt."

        pause 1.0

        cheren @sadmouth "It is not attacking me. As I thought. This Ninetales is... trained."

        show cheren:
            ease 1.0 xpos 0.2

        silver @surprised "What? My Poké Ball worked on it... before it broke out, though."

        cheren @sadmouth "Yes. It's wild, but it's been given a command. For some reason, it's staying here, at Pledge Hall."

        show relichall_A with vpunch

        cheren @angry "Now, I wonder, {i}who{/i} might be responsible for this?"

        silver @closedbrow talkingmouth "...Ugh, this shit again."

        cheren @angry "Do you have a better explanation for this? Who else could command a wild Pokémon to stake out a specific location for so long?"
        cheren @sadmouth "I am {i}beyond{/i} certain that [first_name] is responsible for this."

        silver @sadbrow talkingmouth "He's not even here anymore..."

        skyla @talkingmouth "He is, actually!"

        silver @surprised "{size=40}Really?!{/size}{w=0.5}{nw}"
        extend @sad " I mean... really?"

        skyla @talkingmouth "Yeah, I saw him fly in right around 1400."

        cheren @closedbrow sadmouth "Of course he did."

        skyla @happy "He was on top of a dragon Pokémon I've never seen before."

        cheren @angry "Of course he was!"

        pause 1.0

        cheren @closedbrow sadmouth "Ah."

        pause 1.0

        cheren @sad2eyes sadmouth "Well. That's why we're here, then."
        cheren @sadmouth "He needed us distracted so that he could sneak into the Quarter Qlashes. Of course. It's so simple."

        pause 1.0

        silver @talkingmouth "How would {i}us{/i}{w=0.5} being {i}here{/i}{w=0.5} help him do that?"

        cheren @sadmouth "I don't know. But I {i}do{/i} know I'm right."

        pause 1.0

        skyla @talkingmouth "...I gotta question."

        cheren @sadmouth "Ask away."

        skyla @talkingmouth "How did you know about all that stuff on Saturday?"

        cheren @sadmouth "...I have no power. No ability to convince people to do what I want, or ability to extract information directly from another's mind."
        cheren @sadmouth "No ability to hide in the shadows and follow him as he plotted. I made note of who he coordinated with, but no more than that."
        cheren @closedbrow sadmouth "All I did was {i}talk.{/i} I simply talked to everyone he talked to. I listened to them. And all I heard was praise. Gushing, effusive praise."

        pause 1.0

        cheren @sadmouth "I saw how they were robbed of their agency under his spell. Not once did it occur to them that they can solve their own problems, or seek out other help."

        pause 1.0

        cheren @sad2eyes sadmouth "I am... {i}genuinely{/i} surprised that he came back."
        cheren @sadmouth "I regret what I did. And my choices in allies could not have been worse. I owe Sabrina a deep and heartfelt apology, which I will deliver as soon as I find her."
        cheren @closedbrow sadmouth "However, I do not regret the outcome of my actions in regard to [first_name] [last_name]. He needed to be stopped."

        pause 1.0

        silver @talkingmouth "You're--"

        cheren @sad2eyes sadmouth "If you're going to say 'a bastard', please, save it. I am fully aware."

        pause 1.0

        silver @talkingmouth "I was going to say 'right.'"

        cheren -noshine @surprised "Hm?"

        silver @talkingmouth "Power corrupts. No matter how good you are, if you have everything you want, then... you want everything."

        if (GetRelationshipRank("Silver") == 1):
            silver @talkingmouth "I was... too close to him to see what he could become."

            silver @sad "I've seen how power changes people. I wouldn't want that to happen to him."

        pause 1.0

        silver @angry "But you did it the dumbest goddamn way possible."

        cheren -noshine @talkingmouth "Whereas your 'contributions to his campaign' were the height of intelligence."

        silver @sad ".{w=0.5}.{w=0.5}.{w=0.5}You can't prove anything."

        skyla @sadbrow talking2mouth "Um... what are you talking about?"

        cheren @sadmouth "Small potatoes. Nothing worth thinking about, any more. We are all on the same side."

        pause 1.0

        skyla @talkingmouth "Then can we get back to fighting the Ninetales?"

        cheren @closedbrow sadmouth "I no longer believe that is an active danger to anyone at this school, as long as people entering or exiting Pledge Hall give it a wide berth. Silver, let's go get your other Pokémon."

        silver @talkingmouth "You don't think we should get an instructor to deal with it?"

        cheren @sad2eyes talkingmouth "I'd rather not confess that the school's new Disciplinary Committee was unable to stop their first true problem, yes."

        silver @sad "Fair."

        hide skyla
        hide silver
        hide cheren
        with dis

        skyla "Do you think we should set up a ranking system for emergencies? {size=32}Like, would this{/size} {size=28}be a demon-class{/size} {size=24}disaster level{/size} {size=20}or maybe{/size} {size=16}a tiger-class or...{/size}"

        pause 1.0

        narrator "...The Disciplinary Committee walks out of earshot."

        pause 1.0

        narrator "The Ninetales stares straight at you, through the small bush you're hiding behind, as though challenging you. Though its eyes have the same wild glint you've grown to know, it doesn't move from its spot."

        narrator "For a moment, nothing happens, but then..."

        show relichall_A with vpunch

        $ PlaySound("pokemon/cries/38.mp3")
        stop music
        $ renpy.music.queue("Audio/Music/RelicCastle_Start.ogg", channel='music', loop=None, tight=None)
        $ renpy.music.queue("Audio/Music/RelicCastle_Loop.ogg", channel='music', loop=True, tight=None)

        show aninetales:
            ease 0.3 xpos 0.5 ypos 1.2 zoom 1.3

        pause 1.0

        $ nummons = 1

        narrator "A Frenzied Pokémon is attacking! How many Pokémon do you want to send out in response?"

        menu:
            "One and done!":
                pass

            "Two to fight through!":
                $ nummons = 2

            "Three for me!":
                $ nummons = 3

        python:
            trainer1 = Trainer("red", TrainerType.Player, playerparty, number=nummons)

            ninetalesobj = Pokemon(38.1, level=24, moves=[GetMove("Blizzard"), GetMove("Confuse Ray"), GetMove("Ice Shard"), GetMove("Aurora Veil")], ability="Snow Warning", frenzynerf=(AimLevel() + 1, ["Aurora Beam", "Draining Kiss", "Aurora Veil", "Charm"]), shinylock=False)
            ninetalesobj.ApplyStatus("frenzied")
            trainer2 = Trainer("sideportraitfull", TrainerType.Enemy, [ninetalesobj], isPokemon=True)
            sidemonnum = 38.1

        hide aninetales with dis

        call Battle([trainer1, trainer2], healParty = False, specialmusic="Nothing") from _call_Battle_114
        $ battlehistory["Ninetales1"]  = _return

        if (ninetalesobj in (AllPokemon())):
            python:
                ninetalesobj.UpdateLevel(AimLevel() + 1, False)
                ninetalesobj.Moves = [GetMove("Aurora Beam"), GetMove("Draining Kiss"), GetMove("Aurora Veil"), GetMove("Charm")]
                ninetalesobj.ClearStatus("all", True)

                pronoun = "him" if ninetalesobj.GetGender() == Genders.Male else "her"
                pronoun2 = "he" if ninetalesobj.GetGender() == Genders.Male else "she"

            narrator "You successfully caught the Ninetales."

        else:
            narrator "The Ninetales flees from you."
        
        narrator "You can't help but feel as though this frenzied Pokémon was... {i}different{/i}, somehow."
        narrator "Although its eyes were wild, and it exhibited far more power than it seemed it should have, its fury seemed directed."
        narrator "At who, or what, you're unclear on."

        pause 1.0

        narrator "You decide to leave."

        $ makeuppledgehall = True

elif (_return == "Inspira"):
    if (makeupinspira):
        narrator "There doesn't appear to be anything happening here right now."

    else:
        scene seaport with splitfade

        stop music fadeout 1.5

        queue music "audio/music/montenevera_start.ogg" noloop
        queue music "audio/music/montenevera_loop.ogg"

        narrator "As you walk towards the Pokémon Center, you pass by the seaport and see Grusha and Jasmine sitting on the dock, talking. You quickly hide behind a fire hydrant."

        show grusha tired angryeyes angryeyebrows frownmouth hospital pale noscarf:
            xpos 0.66
        show jasmine sadbrow frownmouth:
            xpos 0.33 xzoom -1
        with dis

        jasmine @talkingmouth "{size=24}...could{/size} {size=28}be worse,{/size} {size=32}Grusha.{/size} The Doctor said that it was a miracle that you didn't get more seriously hurt."

        pause 1.0

        grusha @angrymouth "I {i}don't care{/i} if it could be worse."

        pause 1.0

        grusha @shadow talking2mouth "I'm {i}sick{/i} of being a miracle."

        pause 1.0

        grusha @closedbrow talking2mouth "Oh, it's a miracle that you survived that snowboard through your chest, Grusha."
        grusha @closedbrow talking2mouth "Oh, it's a {i}miracle{/i} that your heart is still beating even with the arrhythmia, Grusha."
        grusha @angry shadow "Oh, it's a {i}miracle{/i} that you didn't get {i}seriously{/i} injured after having a heart attack and falling off the stage in front of the entire school, Grusha."

        pause 1.0

        jasmine tears "{w=0.5}.{w=0.5}.{w=0.5}."

        grusha -angryeyebrows @sad2eyes talking2mouth "Maybe it would be better if the next time... wasn't a miracle."

        show jasmine with dis:
            ease 0.5 xpos 0.5

        jasmine angry "N-no! How dare you, Grusha! How {i}dare{/i} you!"
        jasmine "You {i}need{/i} to stick around! You're an amazing person, and a brave, kind, man! You've got far too much to give the world to give up now."

        grusha @sad2eyes sadmouth "...Right. {i}I've{/i} got so much to give the world. Like what? What can I even do, now?"
        grusha @closedeyes talking2mouth "I can't snowboard anymore. As a Pokémon trainer, I'm mediocre. I can't even get elected into a Student Council when [first_name] basically gave us the keys to the front door."

        show jasmine -angry sadbrow frownmouth with dis:
            ease 0.5 xpos 0.33

        pause 1.0

        grusha @sad2eyes talking2mouth "...I can't even start a family some day. My heart will give out. Isn't that something? {i}Por mi jodido corazón no puedo hacer el amor.{/i}"
        grusha @closedbrow talking2mouth "Of course, who'd even give me a chance? I'm a ticking time bomb. It's a miracle I'm still alive, but these miracles will run out eventually."

        jasmine @talkingmouth "...There's still something you can offer the world, Grusha."

        pause 1.0

        grusha @sad2eyes talking2mouth "...I love you too much to ask you to tell me what. Because I know you can't."

        pause 1.0

        grusha @closedeyes sadmouth "{i}You{/i} can give the world something, Jasmine. You can fight for others. You {i}do.{/i} I'm just waiting for my last miracle."

        jasmine @talking2mouth "...You can fight for others, too, Grusha."

        grusha @sadbrow talkingmouth "Sure. And when I'm there on the frontlines, next to you, if I just keel over--what will the person I'm fighting for think?"

        pause 1.0

        jasmine @talking2mouth "It's... it's not easy for me, Grusha."
        jasmine -tears @closedbrow talking2mouth "In some ways, you... you actually have it easier than me..."

        pause 1.0

        grusha @confusedeyebrows talking2mouth "Oh, yeah? How do you figure?"

        jasmine @talkingmouth "When you're not... actively having a heart attack, or recovering from one... you're fine."

        pause 2.0

        jasmine @sadbrow talking2mouth "But I... I'm tired. I'm {i}always{/i} tired. Standing up takes active effort."
        jasmine @closedbrow sadmouth "Even when I'm lying down and trying to sleep... I'm {i}exhausted{/i}."

        pause 1.0

        jasmine @talking2mouth "I know you struggle, Grusha, I absolutely do. And I'd never try to say that I have it harder than you, or that your struggles are... anything less than mine."

        pause 1.0

        jasmine @sadbrow talkingmouth "But... I struggle too. And I still try to do things. I still try to live."

        pause 2.0

        grusha @sad2eyes talking2mouth "Yeah. You're right. I'm sorry."

        jasmine @talkingmouth "You don't have anything to apologize for."

        grusha @talkingmouth "I just don't... I don't see the point of doing anything. When all that could be taken away in a moment, you know?"
        grusha @closedbrow talking2mouth "What if I start trying to live again? What if I have hope? And then someone plays an Allhallows prank on me that puts me in the hospital permanently?"
        grusha @talking2mouth "It doesn't seem worth it."

        jasmine @talking2mouth "...But that's true of anyone."
        jasmine @sadbrow happymouth "The healthiest, strongest woman in the world could be hit by a bus tomorrow. Does that invalidate her life?"

        grusha @sad2eyes talking2mouth "I mean, that woman would be, what, Cynthia? Cynthia and I are operating on slightly different wavelengths." 

        jasmine @talking2mouth "[first_name], then. He's a student just like you. When Cheren did that awful thing, and [first_name] left the school, does that invalidate all the good he did while he was here?"

        grusha @confusedeyebrows "{w=0.5}.{w=0.5}.{w=0.5}."

        show jasmine surprisedbrow frownmouth with dis

        grusha @confusedeyebrows talking2mouth "Kinda, yeah."

        jasmine -surprisedbrow -frownmouth -surprised frownmouth @angrybrow poutmouth "Well, I don't think it does."

        jasmine @closedbrow talking2mouth "It's disappointing to hear he was keeping that secret from us, but... I can understand why he would."

        grusha @talking2mouth confusedeyebrows "Wait, you think he really {i}does{/i} have mind control?"

        jasmine @surprised "I... well, yes. I don't think Cheren was lying."

        grusha @closedbrow talkingmouth "Nah, he wasn't lying, but he {i}was{/i} dead wrong. [first_name] is way too much of a goody-two shoes to be doing half of the stuff Cheren said he was."

        jasmine @talking2mouth "Oh."

        pause 1.0

        jasmine @talking2mouth "Well, I've always found you to be a splendid judge of character, so if you think he's innocent, he must be."

        grusha @closedbrow talking2mouth "Well, I wouldn't go so far as to say 'innocent,' but he definitely wasn't mind-controlling people to vote for him or anything."
        grusha @talking2mouth "If he was the kind of person who was willing to do that, then he wouldn't have let Cheren get one word out of his mouth."

        pause 3.0

        jasmine @talkingmouth "We should probably head back to the hospital."

        grusha @sadbrow talking2mouth "Great. So that they can send me back to the school's infirmary, until the next big thing happens, and I have to go back to the hospital?"

        pause 1.0

        grusha @talking2mouth "I thought I was a snowboarding champion, not a ping-pong champion. If I have to see that {i}maldita{/i} infirmary one more time..."
        grusha @talking2mouth "She's a nice lady, so I feel bad saying this, but... I'm getting really sick of seeing Ms. Miriam's face."

        pause 1.0

        jasmine @talkingmouth "...Things will be alright, Grusha. I promise."

        grusha @sad "You can't."

        pause 2.0

        grusha @closedbrow talkingmouth "But... thanks."

        hide grusha 
        hide jasmine 
        with dis

        jasmine @talkingmouth "I think I {size=32}would very{/size} {size=28}much like{/size} {size=24}to go snowboarding{/size} {size=20}some day...{/size}"
        
        pause 1.0

        narrator "...Grusha and Jasmine walk out of earshot."

        pause 1.0

        narrator "You decide to head to the Pokémon Center to pick up the rest of your party."

        narrator "[bluecolor]It is strongly recommended that you pick up your starter Pokémon, [starter_name].{/color}"
        narrator "[bluecolor]Further, it is unclear if you will have time to switch out your Pokémon again before the Quarter Qlashes end. You may want to pick up your strongest Pokémon.{/color}"

        python:
            for mon in oldparty:
                if mon != pikachuobj:
                    box.append(mon)

        scene city_B with Dissolve(2.0)
        $ currentbox = max(0, currentbox)
        show screen partymons
        call screen pokemonswap
        hide screen partymons
        hide screen pokemonswap
        with dis

        $ makeupinspira = True

elif (_return == "Recreation Center"):
    if (makeuprecreationcenter):
        narrator "There doesn't appear to be anything happening here right now."

    else:
        scene pool with splitfade

        stop music fadeout 1.5
        queue music "audio/music/LoFiMaxRaidBattle_start.ogg" noloop
        queue music "audio/music/LoFiMaxRaidBattle_loop.ogg"

        narrator "As you walk into the Recreation Center, you see Nessa and Rosa sitting on pool chairs, talking to each other. You quickly hide behind a pile of towels."

        show nessa frownmouth:
            xpos 0.66
        show rosa frownmouth:
            xpos 0.33 xzoom -1
        with dis

        nessa @closedbrow talkingmouth "What a mess."

        rosa @talkingmouth "Yeeeep."

        pause 1.0

        nessa @talkingmouth "It must be nice to not be the biggest thing at the school for a while, though."

        rosa @sadbrow sadmouth "Maybe a little bit... but I didn't want this. Poor Sabrina... I take classes with her. I really thought she had a bit of an actresses' spirit in her. I had no idea about... everything else."

        nessa @talkingmouth "Yeah. I asked [first_name] on a date."

        rosa @surprised "Oh? You're dating?"

        if (GetRelationshipRank("Nessa") == 1 and not HasEvent("Nessa", "DenyDate")):
            if (IsDate(5, 5, 2004)):
                nessa @talkingmouth "We went on one date. I guess we probably aren't any more, though. He's not answering my calls."

            else:
                nessa @talkingmouth "We went on one date. I guess we probably aren't any more, though. Sonia told me he came back, but I haven't seen him."

        elif (GetRelationshipRank("Nessa") == 1):
            nessa @talkingmouth "Nah. He didn't want to date me. We just hung out."

        else:
            nessa @talkingmouth "No. He never took me up on it."

        pause 1.0

        nessa @happy "Can you believe that?"

        if (GetRelationshipRank("Nessa") == 1 and not HasEvent("Nessa", "DenyDate")):
            if (IsDate(5, 5, 2004)):
                nessa @talkingmouth "He's not answering my calls. Nessa--the model--is banging down his door, and he's not answering."

            else:
                nessa @talkingmouth "He came back, but we haven't even talked. ...Maybe I should go find him. But he {i}is{/i} the guy, so..."

                rosa @surprisedmouth "...He's probably still nervous about going out in public, you know? He's probably scared of how you'll react to {i}him.{/i} Maybe you should go try to find him."

                nessa @closedbrow talkingmouth "Maybe."

                pause 1.0
            
        else:
            nessa @talkingmouth "Nessa--the model--asked him on a date, and he was, like, 'no thanks.'"

        nessa @sadbrow talkingmouth "...Ugh, look at me. Here I am, acting like it was ever anything serious."

        pause 1.0

        nessa @talkingmouth "What do you think about this whole situation?"

        rosa @sadmouth "I... don't know. This whole thing about mind control sounds really far-fetched, like something a D-list director would come up with."

        rosa @sadbrow sadmouth "...But I don't think Cheren was lying. I know an actor when I see one, and I didn't see anyone lying up on that stage."

        pause 1.0

        rosa @angry "Those purple students were full of it, though! They were lying out their noses the entire time!"

        nessa @closedbrow talkingmouth "...I'll take your word for it."

        pause 1.0

        rosa @sadbrow surprisedmouth "What are you going to do?"

        nessa @surprisedbrow talkingmouth "Me?"
        nessa @closedbrow talkingmouth "Lay back and wait for this all to blow over, mostly."

        rosa @sadmouth "...Don't you think we should do something?"
        
        nessa @surprisedbrow talkingmouth "What do you mean?"

        rosa @talkingmouth "Well... we're kinda famous, right? Maybe we can do something about this situation. Protect some people who need it. Or... give a speech or something..."

        nessa @talkingmouth "...Would your contracts allow you to?"

        pause 1.0

        rosa @sadmouth "No..."

        pause 2.0

        nessa @talkingmouth "Hey. Your net worth is about thirty times mine, so I'm probably not in any position to be giving advice, but..."
        nessa @talkingmouth "You can just ignore those."

        rosa @surprised "What?"

        nessa @talkingmouth "Yeah, those contracts. I had to sign a bunch, too."
        nessa @closedbrow talkingmouth "No going to clubs, no posting swimsuit pics online, no drinking, no stuff like that."
        nessa @closedbrow talkingmouth "But I never paid attention to any of them."

        rosa @surprised "Really?"

        nessa @talkingmouth "Yeah."
        
        pause 1.0

        nessa @talkingmouth "They set up all these 'rules.'"
        nessa @angry "They try to control you--act like they own you. That's what they want you to think. Because what they're terrified of you figuring out is that {i}you{/i} own {i}them{/i}."

        pause 1.0

        nessa @closedbrow talkingmouth "Girl, you can just ignore those rules. What are they going to do? Fire you? You earn them billions a year."

        rosa @sadbrow talkingmouth "...Couldn't they sue me?"

        nessa @talkingmouth "Probably. If they did sue you, would you ever work for them again?"

        rosa @angry "No way!"

        show rosa surprisedbrow frownmouth with dis

        nessa @closedbrow talkingmouth "Then they can't sue you."

        rosa -surprisedbrow @talkingmouth "Oh. That's...{w=0.5} okay."

        pause 2.0

        rosa @sweat sadbrow happymouth "I have to be honest--the thought of that is super-scary."

        nessa @talkingmouth "Hey."

        pause 1.0

        nessa @happybrow talkingmouth "Let's do it together."

        rosa @surprised "Wh-what?"

        show nessa:
            ease 0.5 xpos 0.5

        nessa @talkingmouth "Let's do something you're not allowed to. {i}Right now.{/i}"
        
        rosa @surprised "Wh... I... are you coming onto me?"

        show nessa:
            ease 0.5 xpos 0.66

        nessa @closedbrow talkingmouth "No. But, god, wouldn't {i}that{/i} be a headline? 'Movie Star Rosa and Model Nessa found making out in a college pool!'"
        nessa @closedbrow talkingmouth "If we sold pictures of that, we could both retire early."

        rosa -frownmouth @happy "...Hee. Hee hee hah hah hah!"

        nessa @surprised "What?"

        rosa @talkingmouth "Sonia's told me about you, Nessa. But she told me you were really stoic and serious."

        nessa @closedbrow talkingmouth "'Stoic and serious?' Those were her words?"

        rosa @talkingmouth "Yup."

        nessa @closedbrow talkingmouth "That minx. I'm {i}fun{/i}. I'm {i}spontaneous{/i}."

        pause 1.0

        nessa @sadbrow talkingmouth "...No, she's right. I wouldn't normally do something like this."

        pause 1.0

        nessa @talkingmouth "I don't like seeing people trapped. And you seemed... trapped. I don't know if my key will work for you, but... hey, at least you know it exists now."

        rosa @happy "Thanks, Nessa."

        nessa @talkingmouth "...You can call me Ness."

        rosa @happy "Alright, Ness."

        pause 1.0

        nessa @talkingmouth "I normally just... lay back and let things happen. But, about the school... I think that might {i}actually{/i} be the right call here."

        rosa @surprisedbrow sadmouth "Really?"

        nessa @closedbrow talkingmouth "Yeah. If we made any sort of 'public statement' or whatever... it might just make things worse."

        rosa @talkingmouth "I get you. If we said that [first_name] didn't have mind-control powers, or Sabrina didn't mean to read our minds, then..."
        rosa @sweat sadmouth "My entire job is lying to people. So I guess people might not believe me..."
        rosa @angrybrow talkingmouth "Though I'm {i}really{/i} good at lying! But... I guess that would be telling the truth."

        nessa @talkingmouth "You get it. So... we'll just sit back and wait for this to blow over."

        rosa @angrybrow happymouth "...I don't think so."

        nessa @surprised "Hm?"

        rosa @talkingmouth "There's something we {i}can{/i} do to make this better. We need to be friends to Sabrina."

        nessa @surprised "Run that by me, slowly?"

        rosa @sadmouth "She's famous, now. And can hear everyone's thoughts about her, all the time. But she's alone. Doesn't that sound familiar?"

        nessa @sadbrow talkingmouth "Yeah... I see what you mean."

        rosa @happy "We know how to handle that. So we can help her."
        rosa @sweat happy "Besides... I don't know about you, but all my secrets are already public, and on the internet, so I'm not sure what Sabrina could accidentally read that millions of other people don't already know."

        nessa @closedbrow talkingmouth "Same."

        pause 1.0

        nessa @talkingmouth "Is it cool if I bring Sonia along? She still seems scared of trying to... 'reconnect'. I'm hoping that if I give her something to do, she'll be more comfortable."

        rosa @happy "Of course! The more the merrier."

        pause 2.0

        rosa angrybrow @talkingmouth "Do you still want to do something illegal?"

        nessa @surprised "Uh... {i}contractually disallowed{/i}. Like partying. Not illegal, like murder."

        rosa @happy "We can work our way up."

        nessa @closedbrow angrymouth "{size=30}Oh, God. I just made another Raihan.{/size}"

        rosa @happy "I want a Blipbug."

        nessa @surprised "What?"

        rosa @talkingmouth "You're from Galar, right? You must know where they live, right?"

        nessa @surprised "I don't even know what a Blipbug is."

        rosa @happy "That's alright. Let's go to the forest! It's a Bug-type, so I bet it must be there!"

        nessa @closedbrow talkingmouth "I... alright."

        pause 1.0

        nessa @talkingmouth "Alright."

        hide nessa
        hide rosa
        with dis

        rosa "So, when's your Quarter Qlash battle? {size=32}I had to{/size} {size=28}fight off{/size} {size=24}some{/size} {size=20}paparazzi,{/size} {size=16}and...{/size}"

        pause 1.0

        narrator "...Nessa and Rosa walk out of earshot."

        pause 1.0

        narrator "You decide to leave."

        $ makeuprecreationcenter = True
    
elif (_return == "Research Center"):
    if (makeupresearchcenter):
        narrator "There doesn't appear to be anything happening here right now."

    else:
        $ natenicknaming = False

        scene research with splitfade

        stop music fadeout 1.5
        queue music "Audio/Music/StowOnSide_start.ogg" noloop
        queue music "Audio/Music/StowOnSide_loop.ogg"

        narrator "As you walk into the Research Center, you hear two quiet voices talking from behind a door in the back room."

        show nate sadbrow frownmouth:
            xpos 0.33
        show bea:
            xpos 0.66
        with dis

        nate @talking2mouth "...{size=20}can't{/size} {size=24}believe{/size} {size=28}what{/size} {size=32}happened{/size} to them."

        bea @closedbrow talkingmouth "...Yes."

        nate @angrybrow talking2mouth "I mean, like, that was seriously fucked up, you know?"

        bea @talkingmouth "Yes."

        nate @sadbrow talking2mouth "Like, sure... of course, it'd have been better if S didn't know all our secrets in the first place, but..."

        bea @closedbrow talkingmouth "That was not her fault."

        nate sadbrow frownmouth @surprised "No, I know! I'm not blaming her, even a little bit."

        pause 1.0

        nate @talkingmouth "I've got some pretty big secrets. I actually knew about her telepathy even before the school, and... I made sure to talk with her. To get a scope on the situation. I trusted--still trust--her not to spill anything important."

        bea @surprisedbrow talkingmouth "You don't think the secrets she revealed were important?"

        nate @sweat happybrow happymouth "Well...{w=0.5} No? Important's relative. I mean, most of it was just relationship drama, from what I heard."
        nate @talking2mouth "Though... I thought I heard one thing I should probably check out."

        bea @talkingmouth "...I trust her, as well."

        nate @talkingmouth "How do you know her?"

        bea @talkingmouth "I... eat lunch with Sabrina. She is a kind, thoughtful, soul. Her telepathy is inadvertent. And uncontrollable."
        bea @closedbrow talking2mouth "I try to cultivate power, but I cannot imagine what it must be like for her, to live with this unwanted power for so long."

        show nate frownmouth with dis

        pause 1.0

        bea sadbrow @talkingmouth "I would have thought... I would have thought someone would have stepped up to do something when she was being attacked."
        bea @sadmouth "I would have thought that, when the moment came, and I could protect someone... that I could do something."

        show nate sadbrow with dis

        pause 1.0

        bea @sadmouth "But I failed. Again. And I was powerless as another was hurt in front of me."

        nate @talking2mouth "Hey, B2. Don't take it so hard. It's... it's just part of society."

        bea @surprised "What?"

        nate @closedbrow talking2mouth "Our society. We live in a Pokémon world, you know? We're, in every way that matters, post-violence."
        nate @closedbrow talking2mouth "We've got the Pokémon to thank for that. Even wars are decided through Pokémon battles, now. But there are some problems that can't be solved through a Pokémon battle, and..."
        nate @sad "And people have forgotten how to handle them. They just... freeze. And hope that someone strong enough to battle away the problem comes around."

        bea @talkingmouth "...There are exceptions."

        nate @talking2mouth "Yeah. Most people can't even... {i}think{/i} of, like, throwing a punch, you know? The concept of physical violence is just... {i}nonexistent{/i} to most people."
        
        show bea surprisedbrow frownmouth with dis
        
        nate @angrybrow talking2mouth "But sometimes punches need to be thrown. Sometimes you need a steel dagger, or a vial of poison, or a quick, sharp, shock to do the job."

        pause 1.0

        nate @closedbrow talking2mouth "But... that's not what that situation called for. Maybe? Maybe it should have! I don't know."
        nate @angry "It's just... it's so infuriating, you know?" 
        nate @angry "There are all these problems, simple problems, that have what {i}seem{/i} like simple, easy solutions, but the moment you actually {i}use{/i} any of these solutions, you've opened the door to something you can't ever put back."
        nate @closedbrow talking2mouth "It's like the ultimate weapon The Tyrant King of Kalos built." 
        nate @closedbrow talking2mouth "As soon as he built one, imitators started popping up all over the world, and what was meant to be a quick and easy solution to a war ended up being a problem for everyone for thousands of years."
        nate @angry "So, like, I'm not saying the solution to stopping those purple pricks was punching them in the mouth, but would it have made things much worse? Would it have? {i}Really?{/i}"

        pause 3.0

        bea "Um."

        nate @happy sweat "Hah hah... oops! Sorry about that. I get a bit intense about personal responsibility, sometimes. Seems the ol' mask slipped. Let me just..."

        $ PlaySound("drill.ogg")

        pause 1.0

        nate -sadbrow -frownmouth @happy "<Various construction noises.>"

        pause 1.0

        nate @talkingmouth "Alright, I'm normal again."

        nate @happy "We cool?"

        bea @talkingmouth "...I understand you."

        nate @surprised "Huh?"

        bea @closedbrow talkingmouth "I have seen the violence people visit upon their fellow man."
        bea @sad "And I have seen the uncomprehending stares when I attempt to explain it."
        bea -surprisedbrow -frownmouth -surprised @talkingmouth "I, too, wear a mask."

        pause 1.0

        nate @talking2mouth "I'm sorry."

        bea @talkingmouth "And I for you."

        nate @closedbrow angrymouth "No, I should {i}have to{/i} deal with stuff like that. I signed up for it. But you're just... {w=0.5}just a girl."

        bea @closedbrow talkingmouth "Yes. And you are just a boy."

        nate @sadbrow happymouth sweat "Ugh... I'm a bit more than that, though."

        show nate sadbrow frownmouth with dis

        bea @talkingmouth "Are you? Or is that just another mask?"

        pause 3.0

        nate -sadbrow -frownmouth @closedbrow talking2mouth "Let's talk about something else."

        nate @closedbrow talkingmouth "Anyway, what do you think about [first_name]? I heard he came back."

        if (GetRelationshipRank("Bea") == 0):
            bea @talkingmouth "This talk of his mind control powers is interesting, but not overly concerning."

        else:
            bea @talkingmouth "I trust him implicitly."

        nate @surprised "Huh?"

        if (GetRelationshipRank("Bea") == 0):
            bea @talkingmouth "I have absolute control of every facet of my being. I am confident that he has not used his mind control on me, and if he had tried, I would have been able to resist."
        else:
            bea @talkingmouth "He assists me with my training. I have told him many... confidential things, and not once has he been anything but supportive and kind to me."

            bea @closedbrow talkingmouth "Besides, I am confident that he has not used his mind control on me, and if he had tried, I would have been able to resist."

        nate @talking2mouth "So... you think he actually {i}does{/i} have mind control?"

        bea @talkingmouth "I have heard no alternative explanation."

        nate @closedbrow talking2mouth "...God, I got in some real shit for telling someone this before, but... I think, maybe, explaining the truth now would help make up for it...?"

        pause 1.0

        nate @talkingmouth "Okay, so it's not mind control."

        nate @talkingmouth "It's actually like..."

        pause 1.0

        narrator "Nate explains the true nature of Frienergy. As he speaks, it becomes apparent to you that he had somehow listened to your conversation with Professor Oak."

        redmind @closedbrow frownmouth "So... he already knew, I guess..."

        bea surprised "Oh."

        nate @talkingmouth "Yeah."

        bea -surprisedbrow -frownmouth -surprised @closedbrow talkingmouth "How do {i}you{/i} know this?"

        nate @talking2mouth "...Er. That's private."

        bea @talkingmouth "Fair. May I ask another question, then?"

        nate @talkingmouth "Sure."

        bea @closedbrow talking2mouth "I would like to submit a change-of-nickname request."

        nate @surprised "What? But I call you B2."

        bea @talkingmouth "Yes. But Leaf told me that if we ask you to, you will change our nicknames. So I would like to change my nickname."

        nate @angry sweat "Geez, I never should've let her talk me into that..."
        nate @closedbrow talking2mouth "...Fine. Same rule as with everyone else. Three characters or less."

        bea @talkingmouth "I would like you to call me Bea."

        nate @talkingmouth "...What?"

        bea @talkingmouth "Yes. Bea."

        nate @sweat talkingmouth "But... your name {i}is{/i} Bea."

        bea @happy "And it is three characters long."

        nate @surprisedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

        nate @talkingmouth "Well... alright, then."

        nate @talkingmouth "I've already got a 'B,' so that's kinda confusing, to be honest, but..."

        bea @surprisedbrow talkingmouth "Why? 'B' and 'Bea' are completely different."

        nate @sweat closedbrow talking2mouth "Right, but they're vocally indistinguishable."

        bea @closedbrow talkingmouth "I will know the difference."

        nate @talking2mouth "Yeah, so will I. I'll just have to get used to it."

        pause 2.0

        nate @talkingmouth "Wait. Was that a joke? When you said 'B' and 'Bea' are completely different?"

        bea @happy "If you found it funny."

        nate @surprised "Huh!"

        nate @happy "You're funny! No-one told me you were {i}funny.{/i}"

        bea @talkingmouth "...I know some great knock-knock jokes."

        nate @happy "I'm sure you do, Bea."

        nate @talkingmouth "So, hey, when's your Quarter Qlash match?"

        hide nate
        hide bea
        with dis

        bea "It will be later in the day. {size=32}It's{/size} {size=28}a{/size} {size=24}few{/size} {size=20}hours{/size} {size=16}from...{/size}"

        pause 1.0

        narrator "...Bea and Nate walk out of earshot."

        pause 1.0

        narrator "You decide to leave."

        $ natenicknaming = True
        $ makeupresearchcenter = True

$ makeupvalue = 0
python:
    makeuplist = [makeupresearchcenter, makeupbaseballfield, makeuprecreationcenter, makeupaurahall, makeuprelichall, makeuppledgehall, makeupinspira]
    for makeup in makeuplist:
        if (makeup):
            makeupvalue += 1

if (makeupvalue == 3 and timeOfDay != "Evening"):
    call clearscreens from _call_clearscreens_118
    scene blank2 with Dissolve(1.0)

    pause 1.0

    show evening at vspaz
    $ timeOfDay = "Evening"

    pause 3.5

    show screen currentdate with dis

if (makeupvalue != 7):
    jump makeupoptions

scene clouds
show garden:
    zoom 0.625
with splitfade

stop music fadeout 1.5
queue music "audio/music/Eterna_Start.ogg" noloop
queue music "audio/music/Eterna_Loop.ogg"

narrator "You make your way back to the garden, thinking about everything you've heard."
narrator "You hear some heavy footsteps, and a very guilty-looking Ethan sidles into view from behind a bush."

show ethan sadeyebrows frownmouth with Dissolve(2.0)

pause 1.0

ethan @talking2mouth "...Sorry, man."

red @closedbrow frownmouth "Hm."

ethan @sad2eyes sadmouth "I know I should've told you, but..."

pause 1.0

red @sadbrow talking2mouth "...Where will I dorm?"

ethan @closedbrow talking2mouth "Wherever I am, I guess."

red @surprised "Huh?"

ethan @closedbrow talkingmouth "C'mon. You didn't think I was going to ditch you, too, did you?"

ethan @sad2eyes sadmouth "I...{w=0.5} okay, I didn't exactly try to {i}stop{/i} dorm 151 from breaking up, but I didn't encourage it..."

red @sadbrow talkingmouth "...Thanks. It'll be good to have a friend."

pause 1.0

red @talking2mouth "Well... what do we do now?"

show ethan:
    ease 2.0 xpos 0.75 ypos 1.2 zoom 1.3 alpha 0.0

pause 1.0

narrator "Ethan sits on the ground, next to you. You sit down, too."

hide ethan with dis

ethan @talkingmouth "...Don't know, man."

pause 1.0

narrator "You sit together in silence for a while."

pause 2.0

ethan @talkingmouth "Man, my ass hurts."

red @talkingmouth "Try some squats. They'll build up your ass so it can take any kind of punishment."

ethan @confusedeyebrows talking2mouth "That might be the gayest thing that's ever been said."

red @happy "Hey, it'll work."

pause 2.0

red @talkingmouth "Did you do your Quarter Qlash match?"

ethan @talking2mouth "Yup. A guy with a Magikarp and a Metapod."

red @talkingmouth "Huh."

pause 2.0

red @talking2mouth "I couldn't talk to anyone."

ethan @confusedeyebrows frownmouth "Hm?"

red @closedbrow talking2mouth "I tried. But... Every time I saw a group of people, even if I tried to force myself into talking to them, I just... couldn't."

ethan @closedbrow talking2mouth "Well, don't try to force yourself. That never works. Maybe you just need a bit more time?"

red @talkingmouth "Maybe. ...I'm going to be expected to say something during the Battle Team meeting tomorrow, though. People are going to want an explanation."

ethan @happy "Nah, don't worry about it. We all get what you've been going through. I'm sure no one'll--"

red @sweat closedbrow talking2mouth "No, I mean, Janine actually told me that I'm going to need to give a speech."
red @talkingmouth "She doesn't want the Battle Team thinking that one of the people they're fighting alongside is mind-controlling them."

ethan @closedbrow talking2mouth "...Huh. Well, yeah. That makes sense. Sucks for you, though."

red @frownmouth "[ellipses]"

show ethan with dis

ethan @talkingmouth "Alright. Let's go find a new room."

red @talkingmouth "Maybe if we find the Student Council? Falkner was the person who set up our room arrangements last time."

ethan @talkingmouth "That's a good idea. Let's go."

scene blank2 with splitfade

pause 1.0

scene studentcouncil
show cheren sad2eyes tired noshine:
    xpos 0.2
show brawly frownmouth:
    xpos 0.4
show roxanne frownmouth:
    xpos 0.6
show falkner:
    xpos 0.8
with splitfade

cheren @sadmouth "...was settled. Two fights occurred. Silver broke them up. Skyla ensured no-one was injured. We have not yet located Sabrina."

pause 1.0

cheren @sadmouth "That ends my report."

roxanne @closedbrow talkingmouth "Thank you, Cheren. You should probably go to bed, now."

cheren @sadmouth "Very well."

pause 2.0

show cheren -sad2eyes with dis

pause 2.0

narrator "Cheren's eyes slide over to you without a hint of acknowledgement or recognition."

cheren @sadmouth "[first_name]."

narrator "He says your name like an object.{w=0.5} 'Apple.'{w=0.5} 'Door.'{w=0.5} '[first_name].'"

hide cheren with dis

pause 1.0

falkner @closedbrow talking2mouth "{size=30}I cannot fathom what Dean Drayden was thinking, appointing him the head of the Disciplinary Committee...{/size}"

pause 1.0

roxanne @talkingmouth "[first_name]. I see you're back."

show ethan with dis:
    xpos 0.2

ethan @talkingmouth "Yeah, and he's not mind-controlling people, so don't freak out about that. His power just makes people and Pokémon feel empathy."

brawly @angry "I knew it!"

roxanne @talking2mouth "Let's not make any assumptions based on hearsay, or a single person's word."
roxanne @closedbrow talking2mouth "Doing that is how we ended up in this situation."

ethan @sadbrow talkingmouth "Come on. You can't {i}really{/i} believe that stuff Cheeza said?"

roxanne @sadbrow talking2mouth "I believe nothing until I am given enough evidence to prove it. Right now..."

narrator "Roxanne looks at Brawly and Falkner. They nod at her, very slightly."

roxanne @talking2mouth "Right now, the Student Council's position is that everyone is innocent of everything they've been accused of."

pause 1.0

ethan @confusedeyebrows talking2mouth playfuleyes "So you're saying that those siblings {i}weren't{/i} banging?"

roxanne @closedbrow talking2mouth "Their bedroom habits seem irrelevant to the situation at hand."

falkner @talkingmouth "What {i}is{/i} the situation at hand, [first_name]?"

red @sadbrow frownmouth ".{w=0.5}.{w=0.5}.{w=0.5}"

ethan @talkingmouth "Uh, we're looking for a new dorm. Our roomies are dorming with other people, since we can dorm with the opposite sex now, so we're looking for a new room."

brawly @happy "Oh, just that? Phew! I thought you wanted to yell at us, like everyone else we've talked to today!"

falkner @closedbrow talking2mouth "Yes, that's an easy fix."
falkner @talkingmouth "Please just sign this paperwork, and..."

scene blank2 with splitfade

pause 1.0

narrator "You wordlessly sign the paperwork and submit a new room request. Falkner thumbs through a file, surveying it intensely."

falkner @happymouth "So... there are two of you, so a room that only has three people in it would suit you most, I think. How about... Dorm 25? It's in Pledge Hall."
falkner @closedbrow happymouth "This room was newly-formed, as well, so you won't be going into a room where everyone else has been dorming together for a month."

ethan @talking2mouth "Yeah, sure, sounds great, but why are you smirking?" 

falkner @surprised "Me? Smirk? Perish the thought."

ethan @playfuleyes angryeyebrows frownmouth "Hmm..."

pause 1.0

narrator "You and Ethan make your way to Dorm 25."

scene studentcouncil
show brawly:
    xpos 0.33
show roxanne surprisedbrow frownmouth:
    xpos 0.5
show falkner closedbrow smilemouth:
    xpos 0.66
with splitfade

pause 2.0

roxanne @talkingmouth "Wait. Falkner. That paperwork... you didn't?"

falkner @talkingmouth "I did. And it will be hilarious."

call clearscreens from _call_clearscreens_119 
scene blank2 with splitfade

show night at vspaz
$ timeOfDay = "Night"

pause 3.5

show screen currentdate
scene hall_A2b
with splitfade

pause 3.0

scene suitenight with splitfade

pause 3.0

show screen songsplash("A Rival Appears!", "Zame")
queue music "audio/music/rivalchill_start.ogg" noloop
queue music "audio/music/rivalchill_loop.ogg"

narrator "Vaguely, in the back of your mind, you can hear the sound of a cartoon anvil falling toward you."

show lobby at sepia 
show flashback
with dis

$ renpy.pause(1.0, hard=True)

show falkner uniform at sepia behind flashback with dis

pause 0.5

red sepia @happy "If you could make sure I don't dorm with 'Blue Oak,' then I'm good with anyone else!" 

pause 1.0

show blank with splitfade

hide falkner
hide lobby
hide flashback
hide blank
with Dissolve(2.0)

pause 1.0

show blue surprisedbrow frownmouth with dis

blue @talkingmouth "What are you doing here?"

show yellow happy with dis:
    xpos 0.25

yellow @happy "Hi! Good to see you two again. I didn't hear you knock?"

blue angry "What. {w=0.5}Are. {w=0.5}You. {w=0.5}Doing. {w=0.5}Here?"

show leaf happy with vpunch:
    xpos 0.75

leaf @talking2mouth "Heya, new roomies! I'm Leaf, and I--"

leaf sarcastic "Wait, I know you nerds."

yellow @sadbrow happymouth "{size=30}I... didn't hear {i}you{/i} knock, either...?{/size}"

blue angry "{size=40}What are you {i}all{/i} doing here?{/size}"

pause 1.0

show leaf surprisedbrow frownmouth with dis

"{color=#cf0000}[first_name]{/color} & {color=#c1861e}Ethan{/color} & {color=#00b23f}Leaf{/color}" "\"Isn't this Dorm 25?\""

blue surprisedbrow angrymouth "...Gggk. Ggggggkkkk."

narrator "Blue's eyes bug out of his head, and a close observation of his eyeballs reveals that they are beginning to become bloodshot."

show blank2 behind suitenight
show suitenight:
    zoom 1.0 align (0.5, 0.5) alpha 1.0
    ease 0.5 zoom 0.0 alpha 0.0
show relichall_B:
    zoom 2.0 align (0.5, 0.5) alpha 0.0
    ease 0.5 zoom 1.0 alpha 1.0

blue @talkingmouth "{size=40}WHAT.{/size}"

show suitenight:
    zoom 1.0 align (0.5, 0.5) alpha 1.0
    ease 0.5 zoom 0.0 alpha 0.0
show nightmap:
    zoom 2.0 align (0.5, 0.5) alpha 0.0
    ease 0.5 zoom 1.0 alpha 1.0

blue @talkingmouth "{size=60}ARE YOU DOING.{/size}"

show suitenight:
    zoom 1.0 align (0.5, 0.5) alpha 1.0
    ease 0.5 zoom 0.0 alpha 0.0
show planet:
    zoom 2.0 align (0.5, 0.5) alpha 0.0
    ease 0.5 zoom 1.0 alpha 1.0

blue @talkingmouth "{size=80}HERE?!{/size}"

stop music fadeout 5.0

call clearscreens from _call_clearscreens_120
scene blank2 with Dissolve(5.0)

jump day010506
