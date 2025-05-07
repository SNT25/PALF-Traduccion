label day010503:
$ timeOfDay = "Early Morning"

call calendar(1) from _call_calendar_28
$ calDate = calDate.replace(day=3, month=5, year=2004)

show earlymorning at vspaz

pause 3.5

narrator "{color=#c1861e}You are no longer you.{/color}"

pause 2.0

stop music fadeout 1.5

show screen songsplash("Pallet Town", "Zame")
queue music "audio/music/palletpiano.ogg"

python:
    playercharacter = "Blue"

    #overwriting party, inventory, personalstats, and persondex

    playerparty = GetTrainerTeam("Blue")

    HealParty()

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

    oldclassstats = copy.copy(classstats)
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

scene suite
show screen currentdate
with transeye2

narrator "You wake up at the crack of dawn, as you almost always do."

pause 1.0

narrator "Your roommates aren't here. Unsurprising, given the events of last night. You {i}had{/i} told them all never to come back."

blue @closedbrow angrymouth "Tch. One little screaming match and all those slackers ditch me. Quitters like that will {i}never{/i} be the number one trainer in Kobukan."

narrator "You throw off your blankets, looking at yourself in the mirror."

blue @happy "Hah. Hair's looking good. Alright, time to get training!"

pause 1.0

blue @closedbrow talkingmouth "But... who? Nate and Cheren are out, those other two losers aren't here, [first_name]'s dead or something..."
blue @surprised "{w=0.5}.{w=0.5}.{w=0.5}.I guess there's {i}her.{/i}"
blue @talking2mouth "Might as well."

show blank with splitfade

pause 1.0

show hall_A 
show yellow neutralhat closedbrow frownmouth
with splitfade

pause 2.0

$ BecomeNamed("Yellow")

bluemind @surprised "She fell asleep waiting for me again, huh..."

yellow @talkingmouth "{cps=20}Zzz... zzz...{/cps}"

pause 2.0

show hall_A
show yellow surprisedbrow frownmouth
with vpunch

blue @angry "Wake up!"

pause 1.0

yellow blush -closedbrow -frownmouth happy "Blue!"

blue @closedbrow talking2mouth "Yeah, yeah. You ready to go training?"

yellow -happy -blush @happymouth "I sure am. I was doing a bunch of research last night on fish-type Pokémon anatomy, and I think I should be a lot better at healing them, now."

blue @talkingmouth "Yeah, yeah. Y'know, if you didn't have that dumb thing against battling, you could train {i}without{/i} me knocking out Pokémon for you."

yellow @happy "It's more fun this way, though."

blue @surprised "What, it's fun for you to watch me hit a 999-KO streak out in the fields?"

yellow heavyblush @happymouth "Yes."

blue @surprised "...Whatever. C'mon, let's go."

show hall_A:
    xalign 0.0 yalign 0.0
    ease 2.0 xpos -0.2 ypos -0.2 zoom 1.2
    pause 0.5
    ease 1.0 xalign 0.0 yalign 0.0 zoom 1.0

show yellow -heavyblush surprised with dis:
    xalign 0.5
    ease 1.5 xalign 0.75
    ease 0.5 xalign 0.25

pause 1.5

yellow @talkingmouth "W-wait!"

blue @surprised "Yeah, what?"

yellow frownmouth @sadbrow talkingmouth "Um... there're people arguing that way."

blue @angrybrow talking2mouth "So? Who {i}cares?{/i} You know I love a good argument."

yellow @talkingmouth "...It'd also be faster to go the other way, if you want to go to the fields."

pause 1.0

blue frownmouth "{w=0.5}.{w=0.5}.{w=0.5}.What're they arguing about?"

yellow @talkingmouth "Your friend, [first_name]. And if he--"

blue @angry "He's {i}not{/i} my friend. How many times do I have to tell you that?"

yellow sad "I'm sorry."

pause 2.0

show yellow -sad with dis

blue @closedbrow talkingmouth "Fine. I've heard enough of that idiot's name over the past three days to last me a lifetime. I'll go your way."

yellow happy "Yay! Come on, Blue."

hide yellow with dis

pause 1.0

bluemind @closedbrow frownmouth "That Yellow... why does she always follow me around? Doesn't she get the message?"

scene seaport
with splitfade

stop music fadeout 1.5

queue music "audio/music/seaport_start.ogg" noloop
queue music "audio/music/seaport_loop.ogg"

pause 1.0

show yellow neutralhat surprised with dis

yellow -surprisedbrow -frownmouth -surprised @talkingmouth "Oh? We're going to the seaport? I thought we were going to the fields."

blue @talkingmouth "Yeah, I changed my mind."

if (seaportunlocked):
    blue @talkingmouth "That Cramorant that was around here finally disappeared, so I can train properly without being attacked by that thing every five seconds."

    blue @happy "Hah, it's almost a shame. I was going to try and catch it. Those things like to swallow Pikachu, right? Maybe I could finally get rid of that stupid rat for good."

else:
    blue @talkingmouth "There's a tough Cramorant around here that I want to beat. Maybe even capture. Those things like to swallow Pikachu, right? Maybe I can finally get rid of that stupid rat for good."

yellow sad "{w=0.5}.{w=0.5}.{w=0.5}."

blue @surprised "What, what's your issue?"

yellow @talkingmouth "...I have a Pichu. My Chuchu."

blue @angry "Well,{w=0.5} {i}obviously{/i},{w=0.5} I'm not going to get my Cramorant to chow down on {i}your{/i} rat."

yellow -sad @talkingmouth "...Okay. Shall we train?"

blue @talkingmouth "Yeah."

show yellow closedbrow with dis:
    ease 0.5 xpos 0.8
    pause 0.3
    ease 0.5 ypos 1.1

blue @talkingmouth "You sure you don't want to {i}actually battle{/i} this time? Fat lot of good your 'training' will do in the Quarter Qlashes."

yellow @talkingmouth "I'm sure. I'm in the nursing program, anyway, so this is a much more important kind of training."

show yellow surprisedbrow with dis

blue @closedbrow talkingmouth "Tch. I don't know what the point of medical training to be a Pokémon nurse is. You just put your Pokémon in the healing machine, slap the big red button, then wait three seconds for the beeps to end."

yellow angrybrow frownmouth @talkingmouth "I've told you before, Blue. Those machines can't handle serious injuries, or diseases. And what if a Pokémon is too agitated to get into their Poké Ball? Nurses need to know how to calm them down."

blue @happy "Sure, or you could just have a strong trainer--like me--battle it until it calms down."

yellow @closedbrow talkingmouth "You can't battle away all your problems, Blue."

blue @talkingmouth "That sounds like something someone who's not good at battling would say."

yellow -angrybrow -frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

yellow @talking2mouth angrybrow "Just for that, I'm not healing your Pokémon until you defeat at least thirty wild Pokémon in a row."

pause 1.0

show seaport:
    xalign 1.0 yalign 1.0
    ease 0.5 zoom 1.2

show yellow surprisedbrow frownmouth with dis:
    ease 0.5 ypos 1.0 xalign 0.5 zoom 1.2

blue @angrybrow happymouth "{i}Make. {w=0.5}It. {w=0.5}Harder.{/i}"

pause 1.0

yellow heavyblush "Oh. Um. Then-- then, um. {size=30}Oh, gosh, you're close.{/size} F-fifty wild Pokémon in a row?"

show seaport:
    zoom 1.2
    ease 0.5 zoom 1.0

show yellow surprisedbrow frownmouth:
    ease 0.5 xpos 0.8 ypos 1.3

blue @talkingmouth "Yeah, that's a good start."

blue @happy "Sit back and watch, {i}Amarillo!{/i}"

show blank2 with Dissolve(2.0)

narrator "Two hours pass as you train furiously, Yellow sitting calmly on the dock and healing each of the Pokémon you defeat back to full health."

show yellow -surprisedbrow -frownmouth -surprised -heavyblush

narrator "As is always the case, by the time you're almost finished training, Yellow ends up with a handful of wild Pokémon that willingly stay with her, watching you train."

blue @surprised "Weirdest shit I've ever seen..."

narrator "Finally..."

hide blank2 with dis

python:
    location = "seaport"
    for mon in playerparty:
        mon.AdjustHealth(RandomUniform(7, 19), absolute=True)

label bluewildarea:

menu:
    "{b}>Go Exploring!{/b} Consecutive battles won: 49.":
        $ trainer1 = Trainer("blue", TrainerType.Player, playerparty)
        $ sidemonnum = pokedexlookupname("Magikarp", DexMacros.Id)
        $ magikarpobj = Pokemon("Magikarp", level=9, nature=Natures.Adamant, ivs=[28, 31, 23, 4, 28, 31], gender=Genders.Male)
        $ trainer2 = Trainer("sideportraitfull", TrainerType.Enemy, [magikarpobj], isPokemon=True)
        call Battle([trainer1, trainer2], healParty=False) from _call_Battle_111
        $ battlehistory["Magikarp1"] = _return
        
        queue music "audio/music/seaport_start.ogg" noloop
        queue music "audio/music/seaport_loop.ogg"

        if (magikarpobj in playerparty):
            $ oldpersondex["Blue"]["Events"].append("CaughtMagikarp")
            blue @closedbrow happymouth "And that's fifty! Piece of goddamn cake. No sweat for the best goddamn trainer in Kobukan!"

            show yellow:
                ease 0.5 xpos 0.5 ypos 1.0

            yellow @happy "You're getting even better, Blue. I {i}know{/i} you'll beat [first_name] next time."

            yellow @surprised "Oh? Oh, this... um, this Magikarp..."

            blue @surprised "Spit it out."

            yellow @happy "Well, this Magikarp is really good!"

            blue @surprised "Huh? Let me check on this thing with my Pokédex."

            pause 1.0

            blue @closedbrow frownmouth "Hm..."

            yellow @surprised "An Adamant nature, and {i}really{/i} good IVs."

            blue @closedbrow talkingmouth "...This Magikarp was just born better, huh?"

            yellow @talkingmouth "Well, it's naturally very strong. If it becomes a Gyarados, it--"

            show yellow surprisedbrow frownmouth with dis

            $ PlaySound("pokemon/Ball Sound.ogg")
            $ PlaySound("pokemon/cries/129.mp3")
            $ PlaySound("splash.ogg")

            $ playerparty.remove(magikarpobj)

            narrator "You release the Magikarp back into the wild."

            blue @talkingmouth "Someone else's problem."

            yellow "Blue?"

            $ PlaySound("PointsUp.ogg")

            blue @talking2mouth "I've already got the best Magikarp in the world. And it's the best because it's {i}mine{/i}. I don't need any others, 'specially not some Magikarp that was just lucky."

            $ oldpersondex["Blue"]["Value"] += 5

            yellow -surprisedbrow -frownmouth -surprised @talkingmouth "...Blue."

        elif (WonBattle("Magikarp1")):
            $ oldpersondex["Blue"]["Events"].append("BeatMagikarp")
            blue @closedbrow happymouth "And that's fifty! Piece of goddamn cake. No sweat for the best goddamn trainer in Kobukan!"

            show yellow:
                ease 0.5 xpos 0.5 ypos 1.0

            yellow @happy "You're getting even better, Blue. I {i}know{/i} you'll beat [first_name] next time."

        elif (Fled):
            $ oldpersondex["Blue"]["Events"].append("FledMagikarp")
            blue @closedbrow happymouth "Oh noooo.{w=0.5} This terrifying Magikarp forced me to run away.{w=0.5} How embarrassing."

            show yellow:
                ease 0.5 xpos 0.5 ypos 1.0

            yellow @angrybrow talking2mouth "You lost on purpose, to make me laugh, didn't you?"

            blue @surprised "Think whatever you want. Maybe I took a dive because I wanted to call your bluff about only healing my guys after fifty victories."

            yellow @closedbrow talkingmouth "...Aw, I really need to get better about actually doing what I say I will."
            
        else:
            $ oldpersondex["Blue"]["Events"].append("LostToMagikarp")
            blue @closedbrow happymouth "Oh noooo.{w=0.5} This terrifying Magikarp beat me.{w=0.5} How embarrassing."

            show yellow:
                ease 0.5 xpos 0.5 ypos 1.0

            yellow @angrybrow talking2mouth "You lost on purpose, to make me laugh, didn't you?"

            blue @surprised "Think whatever you want. Maybe I took a dive because I wanted to call your bluff about only healing my guys after fifty victories."

            yellow @closedbrow talkingmouth "...Aw, I really need to get better about actually doing what I say I will."

    ">Head back to campus":
        narrator "Are you sure you want to head back to campus? Doing so will end this free time."

        $ exptotal = math.floor(pow(12, 3) / 12 * min(3, (1 + wildcount / 10)))
        narrator "You have won 49 consecutive battles, so your party will gain [exptotal] experience each."

        menu:
            "Yes, I'm sure.":
                call clearscreens from _call_clearscreens_85
                python:
                    for mon in playerparty:
                        mon.GainExperience(exptotal)
                show screen currentdate with dis

                show yellow:
                    ease 0.5 xpos 0.5 ypos 1.0

                yellow @surprised "You're quitting now?"

                blue @angrybrow happymouth "I'd call it 'calling your bluff' about only healing my guys after fifty victories."

                yellow @closedbrow talkingmouth "...Aw, I really need to get better about actually doing what I say I will."

            "Never mind.":
                jump bluewildarea

blue @closedbrow talkingmouth "Yeah, yeah. Anyway, make with the healing."

yellow @closedbrow talkingmouth "Please send out your team so I can heal them properly."

blue @surprised "What, you're going to try and heal all of them at once? Fine, but if you pass out, I'm not dragging you back to school again."

$ PlaySound("pokemon/ball sound.ogg")

blue @talkingmouth "Go ahead."

show yellow neutralhathealingpower glowhands with dis:
    ease 3.0 ypos 1.1

narrator "Yellow takes a deep breath, and embraces your Pokémon."
narrator "Then, instead of pulling out a potion, or retrieving a bag of Oran Berries, she says one word, simply."

show blank4 behind yellow with transeye2nopause
$ PlaySound("shine.ogg")
$ HealParty()
pause 1.0
hide blank4 with transeye2nopause

yellow glowhandseyes @talkingmouth "Heal."

pause 1.0

show yellow -glowhandseyes -neutralhathealingpower with dis:
    ease 1.0 ypos 1.0

$ PlaySound("pokemon/ball sound.ogg")

narrator "You yawn and check your watch."

blue @talkingmouth "Alright. Looks like we've got another half hour to get some training in, so I'm going to go for another fifty streak. You still in?"

yellow @sadeyebrows talkingmouth "Shouldn't we go to homeroom?"

blue @closedbrow angrymouth "Ugh. I {i}don't{/i} want to see Gramps' face right now."

yellow @talkingmouth "I think... I think Professor Cherry might be upset if I'm late... and a lot of people are already pretty upset over what happened on Saturday. Maybe we shouldn't make it worse."

blue @closedbrow talking2mouth "Whatever. Fine, I'll stop training. But I'm stopping because {i}you're{/i} tired and wimpy, not because I need to."

yellow frownmouth @sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."

yellow @angrybrow talkingmouth "Remember when I stayed up {i}all night{/i} to heal your Pokémon?"

blue @talkingmouth "Yeah. And you were so scared that we were going to get caught, I figured someone was going to hear your whining."

yellow @talkingmouth "No-one's asked how you're able to train all night?"

blue frownmouth "...No."

blue @closedbrow talkingmouth "But it doesn't matter. After that shit on Saturday, you probably want to keep your power under wraps."

yellow @surprised "Oh. Um... I'm not sure that's... possible."

blue @surprised "Huh?"

yellow @talkingmouth "Yeah. Whitney already knows. We work together in the nursing classes we take. And, um, Tia knows. A few others, too..."

blue @surprised "Huh. I... I kinda figured that you were trying to keep it a secret."

yellow @happy "Secrets just hurt people. The people you're keeping the secret from, and the person keeping the secret."

blue @talkingmouth "Put it on a fortune cookie, pipsqueak."

pause 1.0

blue @closedbrow talkingmouth "Alright, enough playing around. Time to go to homeroom and face the music."

pause 1.0

yellow @sadbrow talkingmouth "Did you ever find out why your grandfather didn't put us in the same class?"

blue @closedbrow talkingmouth "No. I {i}did{/i} ask him to, but then he put {i}[first_name]{/i} there instead, so I figured he was just doing it to piss me off."

yellow @talkingmouth "I'm sure your grandfather doesn't want to upset you."

blue @angrybrow talkingmouth "You don't know him. {w=0.5}You're not even in his class."

yellow @talkingmouth "No...{w=0.5}{nw}"
extend @happy " But I try to see the best in everyone!"

blue @happy "Well, you're going to have your work cut out for you."

narrator "You walk away."

pause 2.0

yellow blush @talkingmouth "It's hard, sometimes. But I know there's good in everyone. Especially you, Blue."

call clearscreens from _call_clearscreens_86
scene blank2 with Dissolve(1.0)

stop music fadeout 1.5

show screen songsplash("Pallet Town", "Zame")
queue music "audio/music/palletpiano.ogg"
queue music "audio/bigcrowdloop.ogg" channel "crowd" fadein 0.5

show morning at vspaz

pause 3.5

$ timeOfDay = "Morning"

scene homeroom 
show oak angrymouth 
show screen currentdate
with splitfadeslow

oak @talking2mouth "Now, students, please stop talking amongst yourselves. Yes, I know you're very excited over the events of last Saturday, but we need to proceed with the lesson."

hide oak

pause 2.0

show flannery tiredbrow tiredmouth uniform at leftside
show whitney uniform sad at rightside
with dis

whitney @talking2mouth "Please, Flan, you've got to believe me! I {i}really{/i} see you as a friend, not just a project!"

flannery @talking2mouth "...I don't care."

whitney @talking2mouth "N-no, c'mon, Flan, please! Yes, I want to help you with your--"

show flannery furious:
    ease 0.2 xpos 0.5

flannery @talking2mouth "With {i}what?!{/i} With my {i}emotions?!{/i} With my {i}mood?!{/i} That's not something you can just {i}fix{/i}, Whitney!"
flannery @talking2mouth "And if you're trying, then I don't see how you could {i}actually{/i} be my friend, if you're just looking at me like a... worse than a project, like a {i}patient!{/i}"

whitney @talking2mouth "Flan, please, I--"

flannery tired "Drop it. This is over. We're over."

hide flannery
hide whitney 
with dis

pause 2.0

show leaf sadbrow frownmouth uniform at rightside
show may sadbrow frownmouth uniform at leftside
with dis

may @sad "Snff.{w=0.5} Snff."

leaf @sadmouth "Aw, May, what's wrong?"

may @sadmouth "Brendan was lyin' about being a vegan... just so he didn't have to eat my cooking! Isn't that messed up?"

leaf @talking2mouth "...Aw. I'm sorry, sweetie."

may @sadmouth "Brendan doesn't know, but I heard his voice loud and clear on Saturday. I thought I was over it, but then... coming back here to this class, I... I..."

hide may
hide leaf
with dis

pause 2.0

show hilbert angry uniform at rightside with dis

hilbert "{size=30}...So much power, just put to waste. If {i}I{/i} had that power, then...{/size}"

show dawn sad uniform at leftside with dis

dawn "{size=30}...It's just like my twelfth birthday party all over again...{/size}"

hide hilbert
hide dawn
with dis

pause 2.0

blue uniform @talkingmouth "Hah. What a bunch of washouts. Some rando doesn't get to be Student Council President, a few secrets are spilled, and you all fall to pieces? You losers need to learn to keep your eyes on the target."

show leaf angry uniform with vpunch

leaf @talking2mouth "Don't pretend, {i}even for a second{/i}, that you're handling this any better than the rest of us!"

show leaf surprisedbrow frownmouth with dis

blue @talkingmouth "Heh? What're you talking about? This doesn't affect me. Sounds like [first_name] got taken down a peg--a peg that he should've fallen off years ago."

leaf @talking2mouth "Wait. You don't know?"

blue @surprised "What, we're playing 20 questions now? What is it?"

show leaf -surprisedbrow -frownmouth -surprised frownmouth angrybrow with dis

leaf @talking2mouth "So, you don't know."

blue @surprised "What?! What don't I know?"

leaf @sarcastic "...You're a dick, so I'm not going to tell you."

show homeroom with vpunch

blue @angry "WHAT?!"

show leaf surprisedbrow frownmouth with dis:
    ease 0.2 xpos 0.25 zoom 0.9 ypos 0.9

show oak angry with dis

stop music fadeout 1.5 channel "crowd"

oak "Students, be quiet! Blue, please! Take a seat! I'd expect better of you."

pause 1.0

hide oak with dis

pause 1.0

bluemind angrybrow frownmouth "Yeah. You always do. But you never acknowledge when I {i}do{/i} better."

pause 1.0

hide leaf
show oakbg 
with dis

oak @talkingmouth "{i}Spectaculum pergere debet,{/i} students. The show must go on. You've all invested too much into this school--monetarily or otherwise--to let it all fall apart now."
oak @talkingmouth "Now. If we are to continue our unit on so-called 'Mythical' Pokémon, it's important to remember that they, by their very nature, have not had their existence ever scientifically proven."
oak @talkingmouth "This is counter to 'Legendary' Pokémon, who definitely exist, though our records of them may be thin and prone to embellishment."

pause 1.0

oak @talkingmouth "Let's see... in Unova, the Pokémon 'Victini' is known to..."

pause 1.0

narrator "You sit back with your feet on the desk and take notes whenever your grandfather says something you didn't already know."

pause 1.0

narrator "After a moment, you become aware that class seems weirdly quiet. Looking over your shoulder, you suddenly realize that [first_name] is no longer here."

bluemind frownmouth "Huh."

show leaf uniform frownmouth with dis:
    xpos -0.1 ypos 1.15 xzoom -1
    ease 0.5 xpos 0.25

leaf @talking2mouth "Psst. We've got dragon class fifth period, right?"

blue @surprised "Huh? Yeah, I think. Why, what's it to you?"

leaf @talking2mouth "You're a dick, but this is important, so I'll tell you then."

blue @closedbrow talking2mouth "Great, I've got {i}more{/i} of you flapping your gums to look forward to."

leaf @angrysmilemouth angrybrow "Yeah, you're blessed."

hide leaf with dis

$ renpy.music.set_volume(0.0, delay=1.0, channel="music")
$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_87

$ PlaySound("BellChime.ogg")
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")
hide blank2
show blank2 with splitfade

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_88
$ renpy.music.stop(channel='crowd', fadeout=1.5)

$ renpy.transition(dissolve)
show screen currentdate

scene classroom with dis
show flytype with dis:
    xalign 0.5 yalign 1.0

$ location = "flying"

$ renpy.pause(1.0, hard=True)

show winona sadbrow with dis:
    parallel:
        ease 0.5 xpos 0.75
        pause 1.0
        ease 1.0 xpos 0.25
        pause 1.0
        ease 0.5 xpos 0.5
    parallel:
        pause 0.5
        ease 0.25 ypos 1.1
        ease 0.25 ypos 1.0
        pause 1.5
        ease 0.25 ypos 1.1
        ease 0.25 ypos 1.0

winona @sadmouth "Oh... h-hello, students. Yes, um, please, come in. I... yes, I know you're upset... Please don't cry..."

pause 1.0

blue uniform frownmouth @closedbrow talking2mouth "...Here too, huh."

winona @talking2mouth "...Does anyone know where Grusha is? I didn't get a notification from the infirmary that he'd be out."

hide winona with dis

pause 1.0

show calem uniform at rightside with dis:
    xzoom -1

calem @talking2mouth "I imagine he's still recovering from his fall, Miss."

show skyla sadbrow frownmouth uniform behind calem at leftside with dis

skyla @surprised "Oh no! Is he okay?"

pause 1.0

calem @talking2mouth "...Are any of us?"

show skyla:
    ease 2.0 xpos 0.6

skyla @talkingmouth "...Is, um... would it help to talk about it?"

show skyla surprisedbrow frownmouth with dis

calem @talking2mouth "I attempted to show Kobukan a front of unity. And all I achieved was revealing, in the bleakest possible way, how fragile any peace I build truly is."

calem "{w=0.5}.{w=0.5}.{w=0.5}."

show skyla -surprisedbrow -frownmouth -surprised sadbrow frownmouth with dis

calem @closedbrow talkingmouth "No, that didn't help at all."

hide calem
hide skyla
with dis

show classroom with vpunch

blue @talkingmouth "Hey, can we get {i}on{/i} with the lesson? I didn't come here to hear you winners bellyaching about how you didn't get to be a student council hotshot or whatever."

show winona with dis

winona surprisedbrow frownmouth @surprised "O-oh!"

winona sadbrow @talkingmouth "Right, yes, let's... um... let's... get on with the lesson, then..."

hide winona with dis

pause 1.0

show winonabg with dis

winona @talkingmouth "Okay. Flying-type abilities can be separated into two distinct categories, usually."
winona @talkingmouth "Those provided by lift, and those provided by levitation. Now, it's important to remember the difference between these, because... um... let me check my notes..."

pause 1.0

bluemind "Seems like the school's really taking what happened on Saturday hard."

pause 1.0

bluemind "Not my problem. They need to just get over it."

call clearscreens from _call_clearscreens_89
show blank2 with dis

show noon at vspaz
    
pause 3.5

$ timeOfDay = "Noon"

show screen songsplash("Pallet Town", "Zame")
queue music "audio/music/palletpiano.ogg"

$ renpy.transition(dissolve)
show screen currentdate

scene gym with dis

$ renpy.pause(2.0, hard=True)

show alder sad with dis:
    xpos 0.75

show bruno think with dis:
    xpos 0.05

alder @norm4 "...Hi, kids."
alder @sad2 "...There's a lot I want to tell you. But I figure you've probably heard enough from your other teachers, and I'm not paid to be a therapist."

pause 1.0

alder surprised @sad2 "But, even so. If, uh... if any of you want to talk... I'm here."

blue uniform @angry "Goddamnit, can we have {i}one{/i} class without everyone being all mopey? It's not like anyone {i}died!{/i}"

show alder angry with dis

bruno angry @angry2 "Your disrespect for others' feelings will not protect your own. You hurt others for no reason."

blue @angry "Yeah, well, moping like this doesn't fix anything!"

alder @angry2 "Blue, things are {i}very{/i} tense right now, and your attitude is only making things worse. Simmer down."

blue @angry "S-simmer down?! Aren't you meant to be a Champion?! A stupid election went sideways, and some people's secrets became public! Big deal! Bigger scandals than this happen on social media every day!"

show gym with vpunch

alder @angry4 "Blue! Be {i}quiet!{/i}"

blue @sad "Wha-- I..."

alder @angry2 "...You need to learn some manners, young man. You need to learn some respect. And, for the love of god, you need to learn some empathy."

bruno -angry @think2 "You will not talk to us, or your classmates, in this manner. After class, you will report to the school's Disciplinary Committee."

blue @surprised "What? We don't have one of those."

alder norm3 @norm4 "It's new. Dean Drayden thought we needed one, after Saturday."
alder @sad2 "I'm not sure if I agree with how he implemented it, but... that's not my place to say."

pause 1.0

bruno @think2 "Perhaps, since we have so many students gathered here, we should make the announcement now."

alder @norm4 "Yes, that makes sense."

pause 1.0

alder @norm2 "Students, the Dean has implemented a new Disciplinary Committee. In order to avoid the Student Council being swamped with reports from students, you should instead go to the committee."

bruno @norm2 "If you have any conflicts with your fellow students, or with a teacher, that need to be resolved, you are asked to go to the Disciplinary Committee."

erika uniform @surprised "I was not made aware of this. Who is on this committee?"

$ hideside = True

"{color=#1f67df}???{/color}" "\"The rest of the members are still being selected, but for now...\""

show cheren uniform noshine with dis

pause 1.0

stop music fadeout 0.5

cheren @sadmouth "I am."

pause 2.0

$ hideside = False

show alder surprisedbrow frownmouth
show bruno surprisedbrow frownmouth
show gym 
with vpunch

show cheren shadow with dis

play music "<from 10>audio/crowdargue.ogg" channel "crowd"
play music "audio/crowdargue2.ogg" channel "crowd2"

"???" "\"What?! Him?! No way!\""

show gym 
with vpunch

"???" "\"This has to be some kind of sick joke!\""

show gym 
with vpunch

"???" "\"He {i}caused{/i} this mess!\""

pause 1.0

bluemind @surprised "The teachers aren't defending him... guess they agree."

pause 1.0

bluemind @happy "Well, sucks to be him!"

"???" "\"Get him out of here!\""

"???" "\"I'm never going to respect the Disciplinary Committee, with {i}him{/i} in it!\""

"???" "\"Fuck Cheren!\""

show yellow uniformhat angry with vpunch:
    xpos 0.375

show cheren surprisedbrow with dis

stop music channel "crowd" fadeout 0.5
stop music channel "crowd2" fadeout 1.5

queue music "audio/music/viridianforest_start.ogg" noloop
queue music "audio/music/viridianforest_loop.ogg"

yellow @talkingmouth "Stop it!"

bluemind @surprised "Huh? That pipsqueak? What does she think she's doing?"

"???" "\"Who's that...?\""

yellow @talkingmouth "You're trying to shout down Cheren before he even gets a chance to say anything!"

show cheren sad2brow with dis

"???" "\"He's said enough!\""

"???" "\"Yeah! He ruined Kobukan!\""

yellow -angry @talkingmouth "Kobukan's only ruined if you give up on it. We still have eleven months to go. We can turn things around! We can find the good in this!"

yellow @happy "Look, Cheren feels bad! Don't you?"

cheren @sadmouth "Indescribably."

pause 1.0

cheren -noshine -shadow @sadmouth "No. I {i}will{/i} describe it."

cheren -sad2eyes @sadmouth "Classmates, I... I have committed a grave, {i}grave{/i} trespass against all of you. I never meant for so many to get caught up in this. I only wanted..."

cheren @disappointedeyes sadeyebrows tears angrymouth "I only wanted the truth to be known. No matter who it hurt, how much it hurt. I thought myself justified. I thought that--"

show gym with vpunch

show cheren surprisedbrow frownmouth 
show yellow surprisedbrow frownmouth
with dis

stop music fadeout 0.5

play music "<from 10>audio/crowdargue.ogg" channel "crowd"
play music "audio/crowdargue2.ogg" channel "crowd2"

"???" "\"Shut up! Save your sob stories! You were just jealous!\""

show cheren -surprisedbrow -frownmouth -surprised sad2eyes shadow noshine
show yellow sad 
with dis

"???" "\"Yeah, haven't you talked your way into enough trouble for now?\""

cheren sadmouth "In any case--"

show gym with vpunch

"???" "\"Shut up!\""

cheren @talkingmouth "--I will work as the Disciplinary Committee's--"

show gym with vpunch

"???" "\"Get out of here!\""

cheren @talkingmouth "--student liasion, to reduce pressure on--"

show gym with vpunch

"???" "\"We don't want you!\""

cheren @talkingmouth "--the student council, and the faculty."

bluemind @sad "Get {i}out{/i} of there, Yellow!"

cheren @talkingmouth "My door is always open. Come to me with any complaints."

hide cheren with dis

show gym with vpunch

"???" "\"Booo!\""

hide yellow with Dissolve(1.0)

show bruno norm
show alder angry
with dis

stop music channel "crowd" fadeout 1.5
stop music channel "crowd2" fadeout 1.5

alder @angry3 "Alright, that's {i}enough!{/i}" 

show screen songsplash("Pallet Town", "Zame")
queue music "audio/music/palletpiano.ogg"

alder @angry2 "If you've got any complaints about how the Disciplinary Committee is run..."

pause 1.0

alder -angry norm3 @norm4 "Well, bring them to the Disciplinary Committee, I suppose."

pause 1.0

alder @norm4 "Yeah, I see the problem. But there's nothing I can do about it in {i}this{/i} class, so let's just move onto the lecture, then the battles."

call clearscreens from _call_clearscreens_90
show blank2 with dis

pause 1.0

narrator "Class proceeds without incident. After it ends, instead of heading to the lunch hall with all the other students, you proceed to the Disciplinary Committee's Office."

blue uniform @angry "Typical. This 'detention squad' is {i}brand new{/i}, and I'm probably the first person who's got to report to it. Just my luck."

scene studentcouncil
show cheren uniform shadow noshine sad2eyes
show silver uniform angrybrow at rightside:
    xzoom -1
show skyla uniform frownmouth at leftside
show screen currentdate
with splitfade

pause 1.0

show studentcouncil
show skyla surprisedbrow frownmouth
with vpunch

skyla frownmouth -surprisedbrow -frownmouth -surprised @surprised "Ah! Our first villain!"

silver @angrymouth "Get your head out of the clouds. It's not--"

silver @surprisedbrow talkingmouth "Blue?"

blue uniform @surprised "Silver? The hell you doing here?"

silver @sad "Ehh... I'm part of the Disciplinary Committee."

blue @surprised "No, the hell you're not. A shady guy like you?"

silver @angrybrow happymouth "Yeah, I was pretty surprised, too."

cheren -sad2eyes @sadmouth "Silver's passion for enforcing curfew is intense. We had nearly come to blows before over it. It seemed logical, given enforcing curfew is now one of the Disciplinary Committee's responsibilities."

skyla @surprised "Wait, I thought you wanted to repeal curfew?"

cheren @sadeyes talkingmouth "What I want is no longer of any account."

blue @surprised "Oh, yeah, and what about this airhead?"

skyla @angrybrow talkingmouth "Airhead? I'm a hero of justice! I want to make sure that no evildoers ever try to break onto campus again, and--"

pause 1.0

skyla sad "And I want to make sure what happened to poor Sabrina never happens again. I should've done something then, but I was just... I was so shocked by what I heard about [first_name]..."

pause 1.0

skyla -sad @surprised "Oh! Not that, like, I'm mad about it, or anything, though! I think people with superpowers are super-cool!"

pause 1.0

silver @talkingmouth "{size=30}Yeah, well, some of us actually have to {i}work{/i} to make our Pokémon like us. Can't say I see the 'cool' side of this...{/size}"

skyla frownmouth @angry "Hey! I heard that! Can't you see that [first_name] didn't mean to have that power? You've read comic books, right?"

silver @angry "No, we don't all have that luxury. And I'd remind you that {i}this isn't a goddamn comic.{/i} I stuck my neck out for that man, and... this is what happened?"

skyla @angrybrow talkingmouth "He's a victim in this situation."
skyla @talkingmouth "He needs saving just as much as any of the rest of us."

silver @talkingmouth "You're delusional. You think a guy who can cut through the effort the rest of us have to put in is going to feel anything over this?"
silver @angry "Believe me, it's {i}very{/i} easy to stop caring that people hate you."

hide silver
hide skyla
with dis

pause 1.0

blue @surprised "What's up with them?"

cheren @sadmouth closedbrow "...Given my history of poorly-chosen allies, I elected to choose two companions that I thought would... {i}not{/i} have the sort of relationship my former partners did."

blue @talkingmouth "Yeah, well, I think you got that one. I think you'll be too busy trying to prevent those two from fighting to actually get anything done!"

cheren @sadmouth "I have some ideas. A common foe works wonders for bringing enemies together."

pause 1.0

blue @talkingmouth "You're a real bastard, you know that."

cheren @sadeyes talking2mouth "So I've heard."

show cheren -shadow surprised -noshine with dis

blue @talkingmouth "But you actually listened to me."

cheren @talkingmouth "Eh?"

blue @talkingmouth "So we're even. I'm not going to give you a hard time about your massive, {w=0.5}{nw}"

show cheren -surprisedbrow -frownmouth -surprised with dis

extend @talkingmouth " monumental,{w=0.5}{nw}"

show cheren noshine with dis

extend @talkingmouth " colossal,{w=0.5}{nw}"

show cheren sad2eyes with dis

extend @talkingmouth " tremendous,{w=0.5}{nw}"

show cheren shadow with dis

extend @talkingmouth " fuck-up."

pause 1.0

cheren @sadmouth "Are you--"

blue @angry "You bastard."

pause 1.0

cheren @sadbrow sadmouth "Are you done?"

blue @talkingmouth "Yeah, I'm done."

cheren @sadbrow sadmouth "I was under the impression you were... 'not fond' of [first_name]."

blue @angry "Oh, believe me, I hate that loser's guts. But you screwed up this entire school. Everyone's whining and moaning about what happened, even the teachers."

blue @angry "We're here to learn, aren't we? We're here to train? Enough of the moping around!"

cheren @sadmouth "Mm."

pause 1.0

cheren @talkingmouth "On that note, I believe you were instructed to report to the Disciplinary Committee for your disrespect to instructors Alder and Bruno, and the Gym Class, no?"

blue @closedbrow talkingmouth "Yeah, yeah. What, you're going to make me write lines?"

cheren @sadmouth "No. This is a first offense, so you will receive only a warning."

cheren @talkingmouth "Future offenses will result in a removal of your after-school privileges. You will have to spend your free time with the Disciplinary Committee, reflecting on what you have done wrong."

pause 1.0

cheren @angrybrow sadmouth "...Though I should mention that your habit of sneaking out of your dorm at night in order to train ends today."

blue @surprised "What?!"

cheren @sadmouth "I made very clear that you would end that behavior if I was elected to Student Council. That did not happen... obviously... but as it is now my responsibility to ensure that curfew is upheld, I cannot look the other way."

pause 1.0

cheren @sadeyes sadmouth "Silver would not allow it, for one."

blue @talkingmouth "So all that talk about repealing the curfew, and how we're mature enough to handle it, goes out the window as soon as someone tells you to drop it?"

pause 1.0

cheren @sadmouth "Yes."

blue @angry "...You {i}are{/i} a bastard."

cheren -shadow @talkingmouth "...Every time I hear that, it hurts slightly less."

pause 1.0

cheren @closedbrow sadmouth "That is all. You may go."

blue @angry "{w=0.5}.{w=0.5}.{w=0.5}."

call clearscreens from _call_clearscreens_91
scene blank2 with splitfade

show cafe behind blank2

$ renpy.music.play("Audio/bigcrowdloop.ogg", channel='crowd', loop=True, fadein=0.5)

queue music "Audio/Music/Route 1 Anime.ogg"

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade
$ renpy.pause(1.0, hard=True)

hide afternoon

show flannery uniform tired at leftside
show misty uniform
show hilbert uniform at rightside
with dis

blue uniform @angrybrow happymouth "What's up, losers?"

misty "{w=0.5}.{w=0.5}.{w=0.5}."

blue @surprised "Huh? Cat got your tongue? What, you too weak to come up with a comeback?"

hilbert @closedbrow talkingmouth "Cut it out, Blue."

flannery @talking2mouth "Yeah, we're not in the mood to argue."

blue @sad "Wh-what?! But-- this is {i}our table{/i}! We argue every day! Why the hell would you stop now?"

misty @angry "Maybe you didn't notice, but we've all got enough to worry about without this dumbass daily ritual."

flannery @closedbrow talking2mouth "I don't even know why I keep coming to this table."

blue @sad "No..."
blue @angrybrow happymouth "C'mon, Hilbert. I know you never turn down an argument. What's the best Pokémon, huh?"

hilbert @closedbrow talkingmouth "I'm bored of this conversation."

hide hilbert with dis

flannery @talking2mouth "Yeah, I think I'll probably just go take a nap until lunch is over."

hide flannery with dis

misty "{w=0.5}.{w=0.5}.{w=0.5}."
misty @angry "Well, {i}I'm{/i} not leaving this table. I was here first."

blue @angry "{w=0.5}.{w=0.5}.{w=0.5}.Worthless! You're all worthless!"

hide misty with dis

pause 0.5

show yellow uniformhat at rightside with dis

pause 0.5

yellow @talkingmouth "Um, Blue? Would you like to--"

show yellow surprisedbrow frownmouth with dis

blue @angry "Not now, Yellow!"

pause 1.0

yellow sad "{w=0.5}.{w=0.5}.{w=0.5}."

scene blank2 with splitfade

show afternoon at vspaz
    
pause 3.5

$ timeOfDay = "Afternoon"

play music "audio/bigcrowdloop.ogg" fadein 1.5 channel "crowd"

scene classroom
show dragontype:
    xalign 0.5 yalign 1.0
show dragclass:
    alpha 0.5 xalign 0.5 yalign 1.0
    block:
        ease 2.0 alpha 1.0
        ease 2.0 alpha 0.5
        repeat
show classlights:
    alpha 0.5 xalign 0.5 yalign 1.0
show dragglow:
    alpha 0.75 xalign 0.5 yalign 1.0
    block:
        ease 2.25 alpha 0.5
        ease 1.8 alpha 0.75
        repeat
with splitfade

pause 1.0

bluemind uniform @frownmouth "Can't believe that I'm relying on Queen Hardass to bring this day back to normal."
bluemind @surprisedbrow frownmouth "But I'm sure there's {i}nothing{/i} that can interrupt her fetish for Dragon-types, right?"

show clair with dis

pause 1.0

stop music channel "crowd" fadeout 1.5

clair @talking2mouth "Alright! Quickly, now, take your seats. Stop your discussions, unless they pertain to Dragon-types."
clair @angry "We have a lot of material to get through, and I will tolerate no interruption."

bluemind @happy "Finally! A teacher who's got her head on straight."

clair @closedbrow talking2mouth "I would just like to say a couple words regarding the events of last Saturday."

bluemind @angry "Son of a {i}bitch.{/i}"

hide clair with dis

pause 1.0

show clairbg with dis

clair @talkingmouth "Unlike the mighty dragons, who {size=31}blah{/size} {size=26}blah{/size} {size=21}blah{/size} {size=16}blah{/size}{size=11}...{/size}"

narrator "You zone out as Clair's droning voice goes {i}on{/i} and {i}on{/i} about stuff you really don't care about."

bluemind @angrybrow frownmouth "This sucks. Is this what the rest of the year's going to be like?"

pause 1.0

bluemind @angry "This is all that damn [first_name]'s fault. If that idiot hadn't gone all mannequin-mode, he could have explained what Frienergy {i}actually{/i} is, and people wouldn't have freaked out like this."

pause 1.0

bluemind @closedbrow frownmouth "...Well, I guess people are still upset about their own secrets or whatever, but... Like I care! All that matters is [first_name]!"

pause 1.0

bluemind @angry "By which I mean that [first_name] doesn't matter at all!"

show leaf uniform frownmouth with dis:
    xpos 1.1 ypos 1.2
    ease 0.5 xpos 0.75

leaf @sarcastic "Scary face you got there. Any particular reason you're casting the eyes of death on Dawn?"

bluemind @surprised "Huh?"

show dawn uniform sad at leftside with dis:
    ypos 1.2

narrator "You suddenly become aware that you've been subconsciously snarling in Dawn's general direction for the past fifteen minutes."

blue @angry "{size=30}What're you looking at?{/size}"

dawn surprisedbrow frownmouth @surprised "You!{w=1.0} Wait, no, I meant n-nothing! I was just thinking 'don't say you', so I said it, but I meant to say 'nothing!' Not to imply you're nothing, though, I mean, you're really something, but not in a bad way, I just-- I mean--"
dawn sad "I'm sorry!"

hide dawn with vpunch

blue @surprised "{w=0.5}.{w=0.5}.{w=0.5}."

leaf @sarcastic "Smooth."

blue @closedbrow talkingmouth "Yeah, what do {i}you{/i} want?"

leaf @talking2mouth "Figured it out, yet?"

blue @talkingmouth "Cut the crap. What were you going to tell me this morning?"

leaf @talking2mouth "You could say 'Please.'"

blue @angrybrow talkingmouth "{i}Please{/i} stop being a pain in the ass and just tell me what's so goddamn important it needed, like, six hours of build-up."

pause 1.0

leaf @talking2mouth "[first_name] dropped out of Kobukan."

blue @surprised "...What? No, he didn't."

leaf @sarcastic "Uh, yes, he did. Saturday night. Ethan told me this morning."

blue @angry "That's bullshit. He wouldn't quit."

pause 1.0

blue @sad "I mean, I wish he would!{w=0.5}{nw}" 
extend @angry " But he didn't."

pause 1.0

leaf @sarcastic "Sure."

pause 1.0

leaf @talkingmouth "So you agree."

blue @surprised "Huh?"

leaf @talking2mouth "I was just thinking the same thing. Sure, he handed in his dropout paperwork, and sure, he's flown back to Pallet Town, but, y'know, that's not enough to actually {i}quit.{/i}"

blue @surprised "What the hell are you saying?"

leaf @sarcastic "Listen. We have slightly over two days until Wednesday. That means we have just under fifty hours to get [first_name] back to Kobukan before the Quarter Qlashes."

blue @surprised "We? Who the hell is 'we'? You can do whatever the hell you want. I'm glad he's gone. I knew a quitter like him couldn't hack it at Kobukan."

leaf @sarcastic "You just said he wouldn't quit, though."

blue @angry "Don't twist my words!"

leaf @angry "I am {i}literally{/i} just quoting you!"

blue @surprised "Just... shut up. Shut up! I wasn't thinking straight, alright? I was surprised!"

hide clairbg
show leaf surprisedbrow frownmouth:
    ease 0.2 xpos 0.9
show clair angry 
with vpunch

clair @talkingmouth "Mr. Oak! Is there anything you would care to share with the class?"

pause 1.0

blue @closedbrow talkingmouth "No, Instructor Clair."

bluemind @frownmouth "...I can't afford to be sent to the Disciplinary Committee again, not so soon... I need my evenings to train, if that bastard is going to stop me from going out at nights."

show clair surprisedbrow frownmouth 
show leaf surprisedbrow
with dis

blue @talkingmouth "I'm... {cps=10}sorry.{/cps}"

show leaf flirt with dis 

clair -surprisedbrow -frownmouth -surprised @talking2mouth "I... I beg your pardon?"

blue @closedbrow angrymouth "I'm {i}sorry{/i}, Instructor Clair. {size=30}Can we move on, now...?{/size}"

clair @happy "Well! How pleasant it is to see that you can tone down the aggressiveness once in a while. Perhaps my cousin's reports on your temper were exaggerated."

blue @angrybrow talking2mouth "Yep. That's it."

hide clair with dis

pause 1.0

show leaf -flirt frownmouth:
    ease 0.5 xpos 0.75
show clairbg
with dis

leaf @talking2mouth "{size=30}Meet me in the garden after school. We're going to get [first_name] back.{/size}"

blue @angry "{size=30}And why the hell would I want that?{/size}"

leaf @sarcastic "{size=30}Four reasons.{/size}"

$ bluewins = 0

if (WonBattle("Blue1")):
    leaf @talking2mouth "{size=30}Your first battle. You lost, but only because you were using a brand-new Pokémon.{/size}"
else:
    $ bluewins += 1
    leaf @talking2mouth "{size=30}Your first battle. You won, but only because [first_name] was using a brand-new Pokémon.{/size}"

if (WonBattle("Blue2")):
    leaf @talking2mouth "{size=30}Your second battle. You lost, but only because [first_name] massively outnumbered your team.{/size}"
else:
    $ bluewins += 1
    leaf @talking2mouth "{size=30}Your second battle. You won, but only because [first_name] was massively underleveled compared to you.{/size}"

if (WonBattle("Blue3")):
    leaf @talking2mouth "{size=30}Your third battle. You lost, but only because the Battle Tryouts' ruleset totally cut into your level advantage.{/size}"
else:
    $ bluewins += 1
    leaf @talking2mouth "{size=30}Your third battle. You won, but only because [first_name] wasn't used to battling under a level equalizer.{/size}"

if (WonBattle("Blue4")):
    leaf @talking2mouth "{size=30}Finally, your most recent battle. You lost, but that's because I was there. So, obviously, you {i}never{/i} had a chance.{/size}"
    
    blue @angry "{size=30}{i}I beat you{/i} in the tryouts.{/size}"

    leaf @sarcastic "{size=30}Ignoring that.{/size}"
else:
    $ bluewins += 1
    leaf @talking2mouth "{size=30}Finally, your most recent battle. You won, but that's because [first_name] and I weren't totally in-sync, and our Pokémon got in each others' way.{/size}"

    blue @angry "{size=30}Bullshit. You two were totally working well together.{/size}"

    leaf @happy fullblush "{size=30}Oh, you think so? Thank you so much!{/size}"

    leaf @sarcastic "{size=30}But, no, we just make it look easy.{/size}"

blue @angry "{size=30}Is there a point to all this? I remember every battle I had with that guy, I don't need your damn reminders.{/size}"

leaf @talking2mouth "{size=30}I mean, just doing some math on the back of the napkin here, but it looks like your win record is...{/size}"

if (bluewins == 4):
    leaf @talking2mouth "{size=30}Four out of four. Not bad, right? But there isn't a single one-on-one battle where you're fighting each other on equal ground in there, is there?{/size}"

    leaf @sarcastic "{size=30}Don't you want to {i}really{/i} fight him? Don't you want to fight him as equals, so you can finally prove you're better than him?{/size}"

elif (bluewins == 3):
    leaf @talking2mouth "{size=30}Three out of four. Which, you know, good job. That's not bad at all. But there's always going to be that one loss against you, won't there?{/size}"

    leaf @sarcastic "{size=30}Personally, I can't help but feel like I'd want to do one more battle to erase that one lost battle, hm?{/size}"

    leaf @talking2mouth "{size=30}One more battle as equals, one-on-one? So you can finally prove you're better than him?{/size}"

elif (bluewins == 2):
    leaf @talking2mouth "{size=30}Two to two. You're tied. I mean, doesn't that just kinda {i}bite{/i} at you?{/size}"

    leaf @sarcastic "{size=30}Personally, I can't help but feel like I'd want to do one more battle as a tiebreaker, right?{/size}"

    leaf @talking2mouth "{size=30}One more battle as equals, one-on-one? So you can finally prove you're better than him?{/size}"

elif (bluewins == 1):
    leaf @talking2mouth "{size=30}One to three. I mean, doesn't that just kinda {i}bite{/i} at you?{/size}"

    leaf @sarcastic "{size=30}Personally, I can't help but feel like I'd want to do one more battle. {i}At least{/i} one more. Let's be honest, a lot of those losses, the odds were against you, weren't they?{/size}"

    leaf @talking2mouth "{size=30}Don't you want just one more battle as equals, one-on-one? No gimmicks, no handicaps, nothing in your way? Just one more, so you can finally prove you're better than him?{/size}"
  
elif (bluewins == 0):
    leaf @talking2mouth "{size=30}Zero to four. I mean, doesn't that just kinda {i}bite{/i} at you?{/size}"

    leaf @sarcastic "{size=30}Personally, I can't help but feel like I'd want to do one more battle. {i}At least{/i} one more. Let's be honest, a lot of those losses, the odds were against you, weren't they?{/size}"

    leaf @talking2mouth "{size=30}Don't you want just one more battle as equals, one-on-one? No gimmicks, no handicaps, nothing in your way? Just one more, so you can finally prove you're better than him?{/size}"

pause 1.0

blue @angry "{size=30}You must think I'm an idiot.{/size}"

leaf sadbrow @talking2mouth "{size=30}No. I just think you deserve better than what you've gotten.{/size}"

blue @angry "{size=30}...Shut up. I told you I don't want your pity.{/size}"

hide leaf with dis

pause 1.0

narrator "You ignore Leaf for the rest of the lesson, trying to put her words out of your mind."

call clearscreens from _call_clearscreens_92
scene blank2 with splitfade

pause 1.0

scene homeroom 
show oakbg 
show screen currentdate
with splitfadeslow

pause 1.0

narrator "Of course, this is difficult, since your next class has Leaf in it, too."

show leaf uniform with dis:
    ease 0.5 xpos 0.25

leaf @talking2mouth "Hey, did you see Tia in our Dragon class?"

blue uniform @surprised "What? No. Why do you care?"

leaf @closedbrow talking2mouth "I figured that she might be able to help us get [first_name] back. If there's one person in this school more obsessed with him than you, it's Tia."

blue @surprised "More obsessed than me?! Look who's talking!"

show leaf surprisedbrow frownmouth with dis:
    ease 0.5 xpos -0.15

oak @talkingmouth "Whoever's talking should {i}stop{/i}!"

blue @closedbrow frownmouth "Tch."

pause 1.0

oak @talkingmouth "As everyone should remember, it's time to take your quiz. Please pull out your pens."
oak @talkingmouth "As for what you should know... [bluecolor]The opponent Excadrill only knows Dig. The opponent Wailord only knows Dive. And the opponent Braviary only knows Fly.{/color}"
oak @talkingmouth "[bluecolor]Additionally, each opponent will target the foe they can do the most damage to.{/color}"

pause 1.0

oak @talkingmouth "Remember to look at your party before committing to any moves. Finally, remember that this is graded."

python:
    trainer1 = Trainer("blue", TrainerType.Player, [
        Pokemon("Breloom", level=39, moves=[GetMove("Spore"), GetMove("Leech Seed"), GetMove("Sky Uppercut"), GetMove("Substitute")]),
        Pokemon("Dugtrio", level=39, moves=[GetMove("Magnitude"), GetMove("Sandstorm"), GetMove("Dig"), GetMove("Protect")]),
        Pokemon("Lanturn", level=39, moves=[GetMove("Thunderbolt"), GetMove("Whirlpool"), GetMove("Aqua Ring"), GetMove("Charge")])
        ], number = 3)
    trainer2 = Trainer("oak", TrainerType.Enemy, [
        Pokemon("Braviary", level=100, moves=[GetMove("Fly")], intelligence = 1),
        Pokemon("Excadrill", level=100, moves=[GetMove("Dig")], intelligence = 1),
        Pokemon("Wailord", level=100, moves=[GetMove("Dive")], intelligence = 1)
        ], number = 3)
    for mon in trainer2.GetTeam() + trainer1.GetTeam():
        mon.Health = 1
        mon.ChangeStats(Stats.Accuracy, 1)
    trainer1.GetTeam()[0].ApplyStatus("burned")
    trainer1.GetTeam()[2].ApplyStatus("poisoned")

call Battle([trainer1, trainer2], customexpressions=["blue uniform frownmouth", "blue uniform angrybrow frownmouth", "oak angrymouth", "oak angrybrow angrymouth"], gainexp=False, healParty=False, clearstats=False, uniforms=[True, False], lockbag=True) from _call_Battle_112
$ battlehistory["IgnoredOak"] = _return

show screen songsplash("Pallet Town", "Zame")
queue music "audio/music/palletpiano.ogg"

show screen currentdate
show oakbg
with dis

oak @talkingmouth "...Hm."

pause 2.0

$ PlaySound("BellChime.ogg")

oak @talkingmouth "Well, that will be all."

pause 1.0

hide oakbg with dis

bluemind uniform @angrybrow frownmouth "I knew it. Every time we take one of these tests, he just looks at [first_name]'s. He doesn't even look at the rest of ours, does he?"

pause 1.0

call clearscreens from _call_clearscreens_93
scene blank2 with splitfade

show evening at vspaz

$ timeOfDay = "Evening"

pause 3.5

show screen currentdate
show academyhall with dis

pause 1.0

show yellow uniformhat with dis

pause 1.0

yellow @surprised "Blue? What's wrong?"

pause 1.0

blue uniform @angrybrow talkingmouth "Were you waiting for me again?"

yellow -surprisedbrow -frownmouth -surprised @talkingmouth "Not this time."

blue @talkingmouth "...Do you have plans?"

yellow @talkingmouth "I was planning on--"

blue @angrybrow talkingmouth "Drop them. We're training."

yellow @surprised "Oh! Um... I... I actually need to--"

blue @talkingmouth "I can't do this without you."

pause 1.0

yellow blush @sadbrow talkingmouth "Th-that's not fair, Blue... You can't just say that to make me do what you want, and not mean it..."

show yellow surprisedbrow frownmouth:
    ease 0.2 ypos 1.2 zoom 1.3

blue @talkingmouth "I mean it. I can't train without you. I {i}need{/i} you there."

yellow @sadbrow talkingmouth "Al... alright..."

show yellow surprisedbrow frownmouth:
    ease 0.5 ypos 1.0 zoom 1.0

blue @happy "Alright! Good to hear. I'm going back to my dorm to get changed. Meet you outside Aura Hall."

pause 1.0

yellow sad "...You don't make this easy, Blue..."

scene blank2 with splitfade

pause 1.0

scene relichall_A with splitfade

show yellow with Dissolve(2.0)

blue @surprised "...Where's your hat?"

yellow @surprised "Oh. I left it in my dorm."

blue @frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

yellow @sadbrow talkingmouth "Is there... something wrong?"

blue @talkingmouth "Your hair's longer than I remembered."

yellow @angrybrow talkingmouth "...I haven't cut it recently."

pause 1.0

blue @talkingmouth "...Right."

pause 1.0

blue @surprised "Did you, like, do {i}anything{/i} with it recently?"

yellow @talkingmouth "No."

pause 1.0

blue @talkingmouth "Right."

bluemind @surprised "This is weird. Why is her hair distracting me like this?"

bluemind @closedbrow frownmouth "...God. Those losers at school have gotten into my head."

yellow @talkingmouth "Where are we going to train? I heard Bea say that while training on Sunday, she found a cave in the mountains."
yellow @happy "I bet it's chock-full of powerful Pokémon!"
yellow @closedbrow talkingmouth "It's pretty far away, but I think the academy has a couple ride Cyclizar that we can use to get there and back on time."

blue @closedbrow talking2mouth "Hah. Some dumb cave? Sure, I bet there's a {i}real{/i} tough Zubat there that's just waiting to fight me."

yellow frownmouth @angrybrow talkingmouth "Okay. So what's your idea?"

blue @talkingmouth "Let's head to the garden."

yellow surprisedbrow frownmouth @surprised "Really? But there are barely any Pokémon in the garden."

blue @angry "Yeah, well, I want to go there.{w=0.5} It's not a crime!{w=0.5} C'mon, already!" 

scene blank2 with splitfadefast

yellow surprisedbrow frownmouth @surprised "W-wait!"

pause 1.0

scene clouds
show garden:
    zoom 0.625
with splitfade


blue @talkingmouth "God, took you long enough."

show yellow with dis:
    xpos -0.1
    ease 2.0 xpos 0.5

yellow @talkingmouth "That's not fair. Your legs are longer than mine..."

blue @closedbrow talkingmouth "Yeah, yeah. Cry about it."

pause 1.0

show garden:
    xalign 0.0 zoom 0.625
    ease 0.5 xalign 0.1 zoom 0.8
    pause 1.0
    ease 1.0 xalign 0.9
    pause 1.0
    ease 2.0 xalign 0.0 zoom 0.625

bluemind "{w=0.5}.{w=0.5}.{w=0.5}."

pause 1.0

yellow @surprisedbrow talkingmouth "What are you looking for?"

show yellow sad with vpunch

blue @angry "No-one!"

yellow @talkingmouth "{size=30}...Stop yelling at me...{/size}"

pause 1.0

blue @talkingmouth "Sorry. But could you quit crying about it? You didn't {i}have{/i} to come out here."

yellow -sad frownmouth @angrybrow talkingmouth "I'm {i}not{/i} crying."

blue @surprised "Huh? Then what's that noise I...?"

narrator "You pause, listening carefully. There's definitely a sobbing sound coming from somewhere around here."

pause 1.0

yellow @talkingmouth "Actually, I think I heard this same sound this morning..."

blue @surprised "Huh..."

narrator "It sounds like the noise is coming from a bush just a few feet away."

blue @talkingmouth "Probably a wild Pokémon. Ignore it, let's go to the groves."

yellow angrybrow @talkingmouth "N-no. I'm going to check."

hide yellow with dis

pause 1.0

bluemind @angry "Ugh, of all the times to grow a spine. Now I've gotta stop some Rattata from chewing her hair off."

pause 1.0

bluemind @surprised "There it is {i}again.{/i} Why am I thinking about her hair?"

narrator "You walk behind the bushes... and see absolutely nothing, besides Yellow."

show yellow frownmouth at rightside with dis

pause 1.0

narrator "This would be less unnerving if the crying sound wasn't {i}very{/i} loud, and clearly coming from,{w=0.5} like,{w=0.5} {i}right in front of you.{/i}"

blue @closedbrow talking2mouth "This is new."

blue @talkingmouth "What do you think, Yellow? A Kecleon?"

show yellow sad:
    ease 1.5 xpos 0.6

pause 1.0

yellow frownmouth sadbrow @talkingmouth "{w=0.5}.{w=0.5}.{w=0.5}.Tia?"

pause 2.0

bluemind @closedbrow frownmouth "She's finally snapped."

show tia date tired tears sadbrow frownmouth with gaussdissolve:
    xpos 0.4 xzoom -1

pause 1.0

bluemind @surprised "Nevermind, apparently {b}I{/b} have."

pause 1.0

bluemind @angry "I blame [first_name] for this."

narrator "Yellow gently grabs one of Tia's hands, and touches foreheads with her."

yellow @talkingmouth "Tia...? What's wrong?"

show tia closedbrow talking2mouth with dis

"{color=#C96A70}Tia{/color}" "\"Ahh...\""

show tia -closedbrow -talking2mouth frownmouth sadbrow with dis

narrator "Tia's mouth opens, but all you hear is a choking sob."

yellow @talkingmouth "Oh... sweetheart, I'm sorry."

show tia talking2mouth with dis

"{color=#C96A70}Tia{/color}" "\"La...\""

show tia -talking2mouth frownmouth sadbrow with dis

yellow @talkingmouth "All Sunday? Oh, I'm sorry, that's awful. And you dressed up so cutely, too. I'm sure he'd be here if he could be."

narrator "You watch, perplexed, for a couple minutes, as Yellow seems to carry on a fluent conversation with Tia, despite Tia not saying a single intelligible word."

pause 1.0

blue @frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

narrator "Your patience, already minimal, is quickly stretched to its limit."

show yellow surprisedbrow frownmouth
show tia surprisedbrow frownmouth
with dis

blue @angry "Could someone explain what's going on here?!"

show yellow -surprisedbrow -frownmouth -surprised frownmouth
show tia -surprisedbrow -frownmouth -surprised frownmouth 
with dis

yellow @talkingmouth "Um...{w=0.5} well, Tia is...{w=0.5} um..."

yellow @closedbrow talkingmouth "It sounds like Tia was expecting [first_name] to show up here. But he didn't, because of... you know, Saturday."

show tia closedbrow with dis:
    xpos 0.4
    ease 0.5 ypos 1.1
    ease 0.5 ypos 1.0

pause 1.0

show tia -closedbrow with dis

yellow @talkingmouth "She could tell a bunch of people were upset on Saturday, but didn't know what to do. So she just came here to the garden, and waited, and... she's been waiting ever since."

blue @happy "Oh, yeah, okay, that makes perfect sense."

pause 1.0

show yellow surprisedbrow frownmouth
show tia surprisedbrow frownmouth
with vpunch

blue @angry "Like I give a rat's ass about any of that! Why the hell was she invisible just now?!"

show tia -surprisedbrow -frownmouth -surprised frownmouth sadbrow with dis

yellow -surprisedbrow -frownmouth -surprised frownmouth @surprisedbrow talkingmouth "Oh."

pause 1.0

narrator "The seconds stretch by with the speed of a Relaxed Shuckle as Yellow's eyes dart from side to side, looking for a reasonable explanation."

pause 1.0

yellow @happy "Um... she can just do that. Like how I can heal Pokémon, or how [first_name] can make Pokémon trust him right away. She can just turn invisible."

pause 1.0

blue @angrybrow talkingmouth "She.{w=0.5} Can just.{w=0.5} {i}Do that.{/i}"

pause 1.0

yellow sadbrow @talkingmouth "Yyyyyes."

blue @angrybrow talkingmouth "Of course."

pause 2.0

show tia surprisedbrow frownmouth with dis
show yellow surprisedbrow frownmouth with dis

pause 1.0

scene blank2 with splitfade

narrator "You walk away. You've had quite enough distractions from your academy life for the foreseeable future."

scene clouds
show garden:
    zoom 0.625
with splitfadefast

pause 1.0

show leaf surprisedbrow frownmouth:
    xpos 1.5 zoom 1.0 ypos 1.0
    ease 0.3 zoom 1.5 ypos 1.3 xpos 0.5
    ease 0.7 rotate 45.0 ypos 3.0

pause 0.3

show garden with vpunch

$ PlaySound("Body Crash.ogg")

pause 0.3

show garden with vpunch

narrator "Unfortunately, the distractions have not had quite enough of you."

show leaf angry:
    zoom 0.9
    ease 0.5 xpos 0.6 rotate 3 ypos 1.1

leaf @talking2mouth "Hey!"

blue @angry "Hey, yourself! Watch where you're--"

leaf @surprised "Wait, it's you? You showed up?"

show leaf:
    ease 0.5 xpos 0.5 rotate 0 ypos 1.0 zoom 1.0

stop music fadeout 1.5

$ renpy.music.queue("Audio/Music/Cinnabar_Start.ogg", channel='music', loop=None, fadein=0.0, tight=None)
$ renpy.music.queue("Audio/Music/Cinnabar_Loop.ogg", channel='music', loop=True, tight=None)

leaf -angry @happy "Oh, great! Look, I've hit a bit of a snag."

blue @surprised "Huh?"

leaf @talking2mouth "So, I've called him a bunch, but he's not answering. I'm pretty sure that he'll only come back if someone {i}goes there{/i} and gets him."

leaf @closedbrow talking2mouth "Yeah, so, here's the issue. [first_name] told me there was a student in this school named 'Skyla.'"

blue @talkingmouth "Yeah, the pilot."

leaf @surprised "Oh, you know her? Huh."

blue @closedbrow talkingmouth "We take Flying-type classes together."

leaf @talking2mouth "Right. Anyway, I asked her if she could, um, fly her plane over to Kanto."

blue @surprised "You're kidding."

leaf @angry "Hey! Do you know how much it costs to fly a plane from Kobukan to Southwest Kanto and back again?"

blue @surprised "No?"

leaf @embarrassedbrow talkingmouth "Well, neither did I. I thought that it'd be a lot cheaper..."
leaf @sarcastic "But the big thing is that she apparently needs, like, approval from the KAA at least two weeks in advance."

blue @surprised "KAA?"

leaf @talking2mouth "Kobukan Air Authority."

blue @talkingmouth "...Well, sucks to be you."

leaf @sarcastic "Nuh-uh. Sucks to be {i}us.{/i} Because we're in this together, remember?"

blue @angry "Why the hell won't you take {i}no{/i} for an answer, you crazy bitch?"

leaf @talking2mouth "{w=0.5}.{w=0.5}.{w=0.5}.You're the one who showed up to the garden."

pause 1.0

blue @closedbrow talkingmouth "I was in the area."

leaf @sarcastic "Uh-huh."

pause 1.0

leaf @talking2mouth "Anyway, since Skyla's plane isn't an option, I was wondering if your Pidgeotto could fly you."

pause 2.0

narrator "You can hear the blood rushing in your ears, as you're {i}sure{/i} that you've just had a coronary from the massive increase in blood pressure you've undergone."

show leaf surprisedbrow frownmouth with vpunch

blue @angry "{i}That's almost 7000 miles!{/i} Over open ocean! And you want my Pidgeotto to {i}fly{/i} there?! {i}TWICE?!{/i} In two days?!"

leaf -surprisedbrow @talking2mouth "I... I thought Pidgeotto could go at Mach 2?"

blue @closedbrow talkingmouth "That's {i}Pidgeot.{/i} And that's at maximum speed, with no rider. If a person tried to ride a Pidgeot going that fast, the sonic boom would snap their neck and liquefy their brain before they went even a fraction of that speed."

leaf -surprisedbrow "{w=0.5}.{w=0.5}.{w=0.5}."
leaf sadbrow @talking2mouth "I'm... open to other ideas."

pause 1.0

blue @talkingmouth "Give it up. If he left, he's gone. You'd need to be able to fly at the speed of a jet plane in order to even get there and back in time."

leaf @talking2mouth "What?"

blue @talkingmouth "Yeah. We have, what, 44 hours until the Quarter Qlashes start? Planes need to land, swap out their tires, refuel, shit like that. And pilots need to sleep. You can't fly for 16 hours straight."

leaf @angrybrow talking2mouth "How do you know so much about planes?"

blue @angry "Unlike {i}some{/i} people, I listen to the people around me! Skyla talks about her plane all the time."

leaf @talking2mouth "Oh."

pause 1.0

leaf -sadbrow @flirt "You did the math."

blue @surprised "Huh?"

leaf @talking2mouth "You figured out how fast someone would have to go in order to get to Pallet Town and back."

blue @frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
blue @closedbrow talkingmouth "Yeah. But only so I could tell you it's impossible."

leaf sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

pause 1.0

leaf @closedbrow talking2mouth "Okay, wait, wait, we're not over yet. Dragonite. They can circle the globe in 16 hours, right? How about--"

show leaf surprisedbrow with vpunch

blue @angry "GIVE IT UP! There's {i}nothing{/i} we can do! Even if we {i}had{/i} a Dragonite, no rider could stand the wind resistance without some kind of barrier!"

pause 1.0

blue @angrybrow talkingmouth "Give.{w=0.5} Up."

pause 1.0

leaf closedbrow @talking2mouth "Some... some kind of barrier?"

pause 1.0

$ PlaySound("idea.ogg")

show blank

pause 0.1

hide blank

leaf @angrybrow talkingmouth "A Dragonite... with a barrier!"

show leaf:
    ease 0.3 xpos -0.2

leaf angry "Follow me!"

blue @surprised "What? That pushy... God, why does she {i}always{/i} think she's going to get her way?"

show yellow frownmouth:
    xpos 0.6
show tia hat frownmouth:
    xpos 0.8
with dis

yellow @surprised "Blue? Um... Tia and I overheard what you were saying, and..."

blue @angrybrow talkingmouth "Not now, Yellow! Kinda in the middle of something!"

pause 1.0

blue @surprised "Actually..."
blue @talkingmouth "Follow me!"

pause 1.0

show yellow angrybrow:
    ease 0.5 xpos 0.5
show tia:
    ease 0.5 xpos 0.75
with dis

pause 1.0

yellow @closedbrow talkingmouth "{size=30}...See the good in everyone, Amarillo. See the good.{/size}"

call clearscreens from _call_clearscreens_94
scene blank2 with splitfadefast

pause 0.5

scene stadium_empty 
show leaf frownmouth at rightside
show lance at leftside
show screen currentdate
with splitfadefast

pause 1.0

lance @talking2mouth "Absolutely not."

leaf @surprised "What?"

lance @sadbrow talking2mouth "No."

pause 1.0

leaf sadbrow @talking2mouth "Did you mean yes?"

lance @closedbrow talking2mouth "No."

leaf @closedbrow talking2mouth "{size=30}Damn, that normally works.{/size}"

blue @closedbrow talkingmouth "What the hell is happening here?"

lance @sadbrow talking2mouth "{size=30}Oh, joy, there's more.{/size}"

leaf @talking2mouth "Well... you said that no-one could ride on a Dragonite at its top speed without some sort of barrier."
leaf @surprisedbrow talking2mouth "And that reminded me that Advisor Lance has a Dragonite that {i}knows{/i} Barrier!"

lance @talking2mouth "I see you have been listening to my cousin's lectures. Good. She is an excellent teacher, and you would do well to listen to her."
lance @talking2mouth "In any case, you are correct. Dragonite cannot normally learn the Barrier technique." 
lance @closedbrow talking2mouth "However, I taught it the move after months of intensive training, learning from powerful Espers who have exiled themselves to the far reaches of Mount Silver, in order to train their skills."
lance @angrybrow talking2mouth "One can understand, then, why I would be reticent to allow my Dragonite to assist in the recapture of a truculent runaway."

leaf @surprised "Wait, you know what I was going to ask?"

lance @sadbrow talking2mouth "Your appalling taste in men has not escaped me, no."
if (len(last_name) > 10):
    lance @talking2mouth "Your thinking is obvious. You are aware my Dragonite can erect a psychic barrier around its rider to protect said rider from wind resistance."
    lance @talking2mouth "You aim to use my Dragonite to retrieve Mr. [last_name] from whatever hole he has crawled into."
else:
    lance @talking2mouth "It is quite obvious that you think my Dragonite, who can erect a psychic barrier around its rider to protect said rider from wind resistance, could be used to retrieve Mr. [last_name] from whatever hole he has crawled into."
lance @sadbrow talking2mouth "My answer to this request, as stated, is {i}no.{/i}"

pause 1.0

show leaf angrybrow with dis

pause 1.0

leaf @angrymouth "I bet he can't do it."

pause 1.0

lance @angrybrow talking2mouth "Your attempt to bait me is disrespectful--and, may I add, laughable."

show leaf surprisedbrow with dis

lance @closedbrow talking2mouth "My Dragonite, who I might add is {i}female{/i}, once flew from Kobukan to Cinnabar Island in a matter of hours."

leaf @talking2mouth "{size=30}What?{/size}"

pause 1.0

bluemind @surprised "Why isn't she talking? What, does she want {i}me{/i} to say something now?"

blue @talkingmouth "I hate the guy as much as you, Sir, but... c'mon, isn't there something you can do?"

lance @talking2mouth "There is an immense amount I {i}could{/i} do. I see no reason to."

leaf @angry "Wait, but--you said-- you said that once [first_name] failed, you would finally respect him!"

lance @sadbrow talking2mouth "I believe I told you to leave the room for that conversation."

leaf @angry "I was by the door! But that doesn't matter--You made a promise!"

lance @talking2mouth "I made no such thing, and certainly not to you."
lance @sadbrow talking2mouth "What I {i}said{/i} was that I {i}may{/i} respect him."
lance @sadbrow talking2mouth "I didn't think it was necessary that I state failure alone was not a condition of my respect."
lance @talking2mouth "{i}Perseverance{/i} is. Failure, followed by another attempt at success."
lance @sadbrow talking2mouth "Given that, upon being faced with failure, his first recourse was to run home, it is clear he does not have the mental fortitude or wherewithal to succeed in this academy, so there is no reason to drag him back."

pause 1.0

show leaf angrybrow frownmouth with dis

lance @angrybrow talking2mouth "Exactly as I said."

pause 1.0

leaf @angrymouth "{cps=20}Why do you hate him so much?!{/cps}"

lance @closedbrow talking2mouth "Your characterization of my feelings towards him as 'hate' is incorrect."
lance @talking2mouth "I would have liked to see him succeed, as I would any student of Kobukan. But his personality is one that hinders itself, and I object to having my time wasted training a student who does not do their best."

leaf @talking2mouth "Why are you even a teacher?"

lance happymouth "{w=0.5}.{w=0.5}.{w=0.5}."
lance @closedbrow talking2mouth "For the pay, of course."

leaf @sarcastic "I don't believe that for a moment."

lance -happymouth @closedbrow talking2mouth "That's the first intelligent thing you've said since you walked in here."

pause 1.0

leaf @closedbrow talking2mouth "Wait. If... if we can somehow get another Dragonite... would you teach it Barrier?"

lance @angrybrow "{w=0.5}.{w=0.5}.{w=0.5}."

show leaf sadbrow with dis

lance @sadbrow talking2mouth "{i}If{/i} you could somehow get your hands on another Dragonite. Then, certainly, I would be willing to spend the {i}multiple weeks{/i} of dedicated training it would take to teach your Dragonite Barrier."

hide lance with dis

pause 1.0

leaf @talking2mouth "Blue? Can you... can you train my Dratini into a Dragonite?"

bluemind @frownmouth "No."

blue @talkingmouth "What level is it?"

leaf @talking2mouth "Sixteen..."

pause 1.0

blue @talkingmouth "No. I can't increase a Pokémon's level by thirty-nine levels in, like, thirty hours."

pause 1.0

leaf @closedbrow talking2mouth "Okay, but what if we--"

show stadium_empty 
show leaf surprisedbrow frownmouth
with vpunch

blue @angry "Give it up, already! Why are you so desperate?"

show stadium_empty
show leaf angry:
    ease 0.3 xpos 0.5 ypos 1.2 zoom 1.3
with vpunch

leaf @talking2mouth "{size=45}[first_name] isn't the only person who came here with no friends, [blue_name]!{/size}"

pause 1.0

show leaf sadbrow frownmouth with dis:
    ease 0.5 ypos 1.0 zoom 1.0

pause 1.0

blue @talkingmouth "It's Blue."

blue @closedbrow talkingmouth "And there's nothing we-- nothing you can do. Just give up on him."
blue @talkingmouth "This won't work, okay? I mean, I can't even think of a bird Pokémon that could fly that far in one shot. It'd probably {i}have{/i} to be a dragon."
blue @sadbrow talkingmouth "We'd need a dragon, that can go faster than a jet, that can put up some sort of psychic barrier to protect the rider. Find me one of those, and maybe I'll say you've got a chance."

pause 1.0

show yellow frownmouth:
    xpos 1.1
    ease 1.0 xpos 0.65

show tia hat frownmouth:
    xpos 1.1
    ease 1.0 xpos 0.8

pause 1.0

yellow @talkingmouth "Um. I... I think that you might want to listen to what Tia has to say..."

show yellow surprisedbrow frownmouth with vpunch

blue @angry "Not now, Yellow!"

show leaf surprisedbrow frownmouth behind yellow:
    ease 0.2 xpos 0.25 xzoom -1
show yellow angry:
    ease 0.5 xpos 0.5 ypos 1.2 zoom 1.3
show tia surprisedbrow frownmouth:
    ease 0.5 xpos 0.9
    pause 1.0
    ease 1.0 xpos 0.75
with dis
show stadium_empty with vpunch

stop music fadeout 0.5
queue music "audio/music/viridianforest_start.ogg" noloop
queue music "audio/music/viridianforest_loop.ogg"

yellow @talkingmouth "Why not?! Why don't you ever think that what {i}I{/i} have to say might be important?!"

blue @sad "Huh? I, uh, I didn't mean..."

show stadium_empty with vpunch

yellow @talkingmouth "All I've been trying to do, {i}all day{/i}, {i}all month{/i}, is help you! But you never even say thank you!"

blue @angrybrow sadmouth "{size=30}Yellow, c'mon, not here...{/size}"

show stadium_empty with vpunch

yellow @talkingmouth "It's always 'not now, Yellow', or 'not here, Yellow'! Then, when? You won't even introduce me to your friends! I don't want to be a secret!"

blue @closedbrow talkingmouth "I, uh, I didn't want them to..."

show stadium_empty with vpunch

yellow @talkingmouth "And we always have to do what {i}you{/i} want! Why can't we just go out for a picnic once in a while? Why are you {i}always{/i} fighting something or someone?!"

blue @sadbrow talkingmouth "{size=30}I don't know...?{/size}"

pause 1.0

show yellow sad:
    ease 0.5 ypos 1.0 zoom 1.0
show leaf -surprisedbrow -frownmouth -surprised frownmouth 
show tia -surprisedbrow -frownmouth -surprised frownmouth
with dis

pause 1.0

yellow @talkingmouth "...I'm sorry."

bluemind @angrybrow frownmouth "I'm sorry."

pause 1.0

bluemind @closedbrow frownmouth "Okay, now say it {i}aloud.{/i}"

pause 1.0

blue @closedbrow talkingmouth "{size=30}Y-yeah.{/size} Fine."

pause 1.0

blue @closedbrow talkingmouth "What, uh, what was it you wanted to say?"

yellow -sad frownmouth @talkingmouth "Um, Tia's also looking for [first_name]. And she thinks she can help you."

leaf @talking2mouth "That's... that's great. Um, sorry, I don't think I've seen you before?"

yellow -frownmouth @happy "Oh! Hiya. I'm Yellow. Or Amarillo, if you want. I'm Blue's... um..."

pause 1.0

blue @talkingmouth "...Friend."

show leaf:
    xpos 0.25
    ease 0.5 ypos 1.2 zoom 1.3

leaf @surprised "Uh... how come you haven't mentioned her before, Blue? She's super-cute."

blue @angry "I don't go around telling all my friends about my other friends! And you aren't even my friend!"

show leaf:
    xpos 0.25
    ease 0.5 ypos 1.0 zoom 1.0

leaf @sarcastic "Fair enough, I guess."

pause 1.0

leaf @talking2mouth "Well, Tia? What do you think you can do to help us?"

blue @talkingmouth "Yeah, uh, I don't think turning invisible is going to cut it this time."

leaf @surprised "Huh?"

blue @closedbrow talkingmouth "Inside joke."

show tia closedbrow talking2mouth with dis

narrator "Tia inhales and lets out a big sigh."

show tia angrybrow frownmouth with dis

pause 1.0

yellow @talkingmouth "Go ahead, Tia."

show tia:
    ease 1.0 xpos 0.5

show yellow:
    ease 1.0 xpos 0.75

pause 2.0

show tia closedeyes angryeyebrows talking2mouth with dis

pause 2.0

show leaf surprisedbrow with dis

show tia neutraleyebrows poweredeyes poweredhat neutralpowered with Dissolve(2.0)

blue @surprised "Uh... this is new."

hide tia
show latias hat frownmouth poweredeyes poweredhat powered behind leaf:
    xpos 0.5 ypos 1.0
    parallel:
        ease 4.0 xpos 0.52
        ease 4.0 xpos 0.5
        ease 4.0 xpos 0.48
        ease 4.0 xpos 0.5
        repeat
    parallel:
        ease 2.0 ypos 1.0
        ease 2.0 ypos 1.02
        ease 3.0 ypos 1.0
        ease 3.0 ypos 0.98
        repeat
with gaussdissolve

show leaf surprisedbrow frownmouth with dis:
    ease 3.0 xpos 0.15

pause 3.0

blue @surprisedbrow talkingmouth "What?"

leaf @talking2mouth "{size=30}What am I seeing? Should I be screaming?{/size}"

blue @surprisedbrow talkingmouth "No, really, {i}what?{/i}"

leaf @talking2mouth "{size=30}I think I should be screaming, right? I should probably be screaming.{/size}"

blue @surprisedbrow talkingmouth "{i}What is going on?!{/i}"

pause 1.0

$ PlaySound("pokemon/cries/380.mp3")

latias -frownmouth -poweredeyes -poweredhat -powered @happy "Latias!"

yellow @happy "This is the {i}real{/i} Tia!"

pause 1.0

show latias surprisedbrow frownmouth
show yellow surprisedbrow frownmouth
with dis

blue @surprisedbrow talkingmouth "What is it?"

show latias poutmouth angrybrow
show yellow frownmouth
with dis

yellow @closedbrow talkingmouth "{i}She{/i} is a Latias."

blue @closedbrow talkingmouth "Ask a dumb question..."

leaf @talking2mouth "{size=30}Okay, but, like, what... {i}is{/i} she? Is she a Pokémon?{/size}"

blue @talkingmouth "Why are you still whispering?"

leaf @talking2mouth "{size=30}I don't know!{/size}"

latias -poutmouth -angrybrow @sadeyes talking2mouth "Latias. Lati. Titititi. Latias!"

show yellow closedbrow with dis

narrator "Yellow closes her eyes and holds the Lati-- sorry, Tia's hand."

pause 1.0

yellow -closedbrow @talkingmouth "Tia says that she hopes you aren't scared by her true form. And she wants you to know that she's the same girl you've attended Ms. Clair's elective with."

leaf @talking2mouth "Wait, you can {i}speak Pokémon?{/i}"

yellow @closedbrow talkingmouth "No. But I can feel what they're feeling, in a general sense. And, um, I think Tia's species is very empathic, anyway, so it's easier for me to 'read' her."

show leaf -surprisedbrow -frownmouth -surprised:
    ease 0.5 xpos 0.25

leaf @talking2mouth "Okay, but, wait. You--Tia--you said that you thought you could help us get [first_name] back, right?"

latias @happy "La!"

blue @surprised "My Pokédex isn't getting a reading on this thing... is it {i}really{/i} a Pokémon?"

yellow @talkingmouth "There are a lot of Pokémon that have never been catalogued, Blue. Some Pokémon that are common in one region aren't even in the Pokédex of another region."

blue @surprised "Wait, so you're telling me that this... dragon... thing... is like the Rattata of another region?"

latias @angrybrow poutmouth "Lati! As."

yellow @closedbrow talking2mouth "No. She's just a special Pokémon that has never been caught."

blue @angrybrow happymouth "Well, that ends today!"

show leaf surprisedbrow frownmouth
show latias surprisedbrow frownmouth
show yellow surprisedbrow frownmouth
with vpunch

pause 2.0

show latias -surprisedbrow -frownmouth -surprised
show yellow -surprisedbrow -frownmouth -surprised
show leaf -surprisedbrow -frownmouth -surprised
with dis

blue @surprised "What, can't you take a joke?"

leaf @sarcastic "Can we {i}try{/i} to stay on-topic, please? Thanks." 
leaf @talking2mouth "Tia, our Pokédexes aren't working on you, but you at least {i}look{/i} like some sort of dragon. Does this mean--does this mean {i}you{/i} can get to Pallet Town and back before the Quarter Qlashes?"

latias @angrybrow talkingmouth "La."

yellow @talkingmouth "She says yes."

leaf @happy "Then I'm cool with this."

blue @talkingmouth "I'm not! How many of our classmates are actually Pokémon?!"

latias @talking2mouth "Ti."

yellow @talkingmouth "She says two."

blue @surprised "What?! That was a rhetorical question! Two?! Who the hell-- {i}Who's the second?!{/i}"

leaf @talking2mouth "Blue! Focus! Tia's how you can get to Pallet Town!"

blue @surprised "Me?"

leaf frownmouth @talking2mouth "Yeah. Of course! What, you didn't think I was going to ride on her back for, like, an entire day, did you? {i}Across an ocean?{/i}"

blue @happy "Hah. Okay. I've played along with your little game so far, because-- I'll admit it-- I feel like I haven't really finished things with [first_name]."

show leaf surprisedbrow with dis

blue @angry "But if you think for one second I'm going to ride the back of one of my classmates across a {i}goddamn{/i} ocean to give a pep talk to a guy I hate, you're out of your mind."

leaf -surprisedbrow @embarrassedbrow talkingmouth "Well... when you put it like that..."

latias sadeyes @talking2mouth "Tias... Latias..."

stop music fadeout 20
queue music "audio/music/lament.ogg"

yellow frownmouth @talkingmouth "She should probably mention. She can put up a Light Screen to protect her rider. But... she can only carry one at a time without slowing down a lot."
yellow @sadbrow talkingmouth "So... when she comes back, whoever went to get [first_name] won't be able to come back with him."

pause 1.0

yellow @sadbrow talkingmouth "You'll miss the first Quarter Qlash."

pause 1.0

leaf sadbrow @talking2mouth "Tia? Can you go by yourself?"

latias @talking2mouth "Las..."

yellow @talkingmouth "She's never been to Kanto before. She wouldn't know how to get there, or where Pallet Town is."
yellow @closedbrow talkingmouth "Also... she wouldn't know what to say to [first_name]."

blue @talkingmouth "Face it, Leaf. You're the only one who cares enough about that dumbass to do this."

leaf @closedbrow talkingmouth "But..."
leaf @sadbrow talking2mouth "I... I can't. I can't go across an ocean. I just can't."

blue @surprised "What, can't you swim?"

leaf @angrybrow talking2mouth "I mean, yes, but that's not the point!"

latias @happy "Latititititi!"

yellow @talkingmouth "If you fall, Tia can definitely catch you. She can fly faster than you can fall."

leaf @surprisedbrow talking2mouth "That's not the point! I can't just... I mean, I... it's {i}an entire ocean!{/i}"

blue @happy "A little water never hurt anyone."
blue @angrybrow happymouth "What's the deal? You were so gung-ho about sending me on a trip across the pond. Not so fun when you're the one in the pilot's seat, is it?"

pause 1.0

show leaf:
    xpos 0.25 ypos 1.0
    parallel:
        ease 0.2 xpos 0.245
        ease 0.2 xpos 0.25
        ease 0.2 xpos 0.245
        ease 0.2 xpos 0.25
    parallel:
        ease 1.0 ypos 1.1

show yellow sadbrow
show latias frownmouth
with dis

leaf @talking2mouth "Blue. Please. {i}Please{/i}. I need you to get [first_name]. I can't. I {i}c-can't.{/i}"

pause 1.0

blue @angrybrow talkingmouth "You can't get everything you want without working for it."

show latias sad2eyes frownmouth
show yellow frownmouth
with dis

leaf @thinking "[ellipses]"

pause 1.0

yellow @talkingmouth "Um... if Tia is going to get to Pallet Town and back... she needs to leave tomorrow, immediately after school."

pause 1.0

show blank2 

pause 2.0

yellow @talkingmouth "{i}We have... 20 hours to find a pilot.{/i}"

jump day010504
