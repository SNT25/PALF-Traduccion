label wildarea(newloc):

stop music fadeout 2.5

python:
    location = newloc
    continualencounters = 0
    inwildarea = True

if (location == "fields"):
    show clouds:
        yalign 0.5
    show fields1 :
        yalign 0.33 xalign 0.95
    with Dissolve(2.0)
elif (location == "alley"):
    show abandonedhouse:
        yalign 0.5
    with Dissolve(2.0)
elif (location == "seaport"):
    scene seaport with Dissolve(2.0)
elif (location == "mountain"):
    scene mountain with Dissolve(2.0)

show screen currentdate with dissolve
    
label afterwildareasetup:

if (location == "fields"):
    $ renpy.music.queue("audio/music/Fieldstheme_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
    $ renpy.music.queue("audio/music/Fieldstheme_Loop.ogg", channel='music', loop=True)
    show clouds:
        yalign 0.5
    show fields1 :
        yalign 0.33 xalign 0.95
    with Dissolve(2.0)
elif (location == "alley"):
    queue music "audio/music/alley_start.ogg" noloop
    queue music "audio/music/alley_loop.ogg"
    show abandonedhouse:
        yalign 0.5
    with Dissolve(2.0)
elif (location == "seaport"):
    queue music "audio/music/seaport_start.ogg" noloop
    queue music "audio/music/seaport_loop.ogg"
    scene seaport with Dissolve(2.0)
elif (location == "mountain"):
    $ renpy.music.queue("audio/arctic.ogg", channel='music', loop=True)
    scene mountain with Dissolve(2.0)

$ trainer1 = Trainer("red", TrainerType.Ally, playerparty)
if (not trainer1.HasMons()):
    narrator "You quickly sprint back to campus, protecting your hurt and fainted Pokémon from further harm."
    $ location = "school"
else:
    $ subtitle = ""
    if (wildcount != 0):
        $ subtitle = " Consecutive battles won: {}".format(wildcount)

    menu:
        "[bluecolor][[Blue Rank 1]{/color} >Talk to Blue" if (IsDate(18, 5, 2004) and location == "mountain" and GetRelationshipRank("Blue") > 0 and not HasEvent("Blue", "MountainTalk")):
            call bluetalkmountainfieldtrip from _call_bluetalkmountainfieldtrip

            jump afterwildareasetup

        "[bluecolor][[Dawn Rank 1]{/color} >Talk to Dawn" if (IsDate(18, 5, 2004) and location == "mountain" and GetRelationshipRank("Dawn") > 0 and not HasEvent("Dawn", "MountainTalk")):
            call dawntalkmountainfieldtrip from _call_dawntalkmountainfieldtrip

            jump afterwildareasetup

        "[bluecolor][[Hilbert Rank 1]{/color} >Talk to Hilbert" if (IsDate(18, 5, 2004) and location == "mountain" and GetRelationshipRank("Hilbert") > 0 and not HasEvent("Hilbert", "MountainTalk")):
            call hilberttalkmountainfieldtrip from _call_hilberttalkmountainfieldtrip

            jump afterwildareasetup

        "Is that Ethan...?" if (IsAfter(17, 5, 2004) and location == "mountain" and not (timeOfDay == "Morning" and IsDate(18, 5, 2004)) and "Ethan" in GetStudents() and "Professor Cherry" in GetStudents() and not HasEvent("Ethan", "MountainTalk")):
            call ethantalkmountainfieldtrip from _call_ethantalkmountainfieldtrip

            jump afterwildareasetup

        "Is that a Cramorant...?" if (location == "seaport" and activetreat in ["Water Bottle", "Bouffalant Wings"] and "Cramorant1" not in battlehistory.keys()):
            call cramorantscene2 from _call_cramorantscene2

        "{b}>Go Exploring!{/b}[subtitle]":
            $ continualencounters += 1
            $ GenerateRandomEvent(location)

            if (IsDate(17, 5, 2004) and location == "fields" and continualencounters == 3):
                call cyclizarhuntpart2 from _call_cyclizarhuntpart2

            jump afterwildareasetup

        ">Head back to campus":
            narrator "Are you sure you want to head back to campus? Doing so will end this free time."

            if (IsDate(17, 5, 2004) and location == "fields"):
                python:
                    cyclizarcount = 0
                    for mon in box + playerparty:
                        if (mon.GetId() == pokedexlookupname("Cyclizar", DexMacros.Id)):
                            cyclizarcount += 1

                narrator "Between your party and your PC Box, you have a total of [cyclizarcount] Cyclizar."
                narrator "You remember Professor Cherry mentioned she couldn't possibly ask you to catch any more than [bluecolor]five...{/color}"

            if (wildcount != 0):
                $ expvalue = 5
                if (location == "alley"):
                    $ expvalue = 9
                elif (location == "seaport"):
                    $ expvalue = 12
                elif (location == "mountain"):
                    $ expvalue = 17
                $ exptotal = math.floor(pow(expvalue, 3) / 25 * min(3, (1 + wildcount / 10)))
                narrator "You have won [wildcount] consecutive battles, so your party will gain [exptotal] experience each. (There are no bonuses after 20 consecutive battles.)"
                if (GetHighestLevel() > AimLevel() + 3):
                    narrator "{color=#f00}Note:{/color} Pokémon that have significantly more experience than is expected right now may receive less."

            menu:
                "Yes, I'm sure.":
                    call clearscreens from _call_clearscreens_64
                    python:
                        activetreat = None
                        continualencounters = 0
                        if (wildcount != 0):
                            for mon in playerparty:
                                mon.GainExperience(exptotal)
                        if (wildcount > highestwildcount):
                            highestwildcount = wildcount
                        wildcount = 0
                        location = "school"
                        inwildarea = False
                    show screen currentdate with dis
                    pass

                "Never mind.":
                    jump afterwildareasetup

return

define treatitems = {
    0  : (1000, Item.PlainBread),
    1  : (1000, Item.SpicyJerky),
    2  : (1000, Item.WaterBottle),
    3  : (1000, Item.EnergyDrink),
    4  : (1000, Item.SaladWrap),
    5  : (1000, Item.IcePop),
    6  : (1000, Item.KnuckleSandwich),
    7  : (1000, Item.FastFood),
    8  : (1000, Item.GroundBeef),
    9  : (1000, Item.BouffalantWings),
    10 : (1000, Item.BrainFood),
    11 : (1000, Item.PicnicBasket),
    12 : (1000, Item.RockCakes),
    13 : (1000, Item.SoulFood),
    14 : (1000, Item.GummyWyrms),
    15 : (1000, Item.DarkChocolate),
    16 : (1000, Item.SteelcutOats),
    17 : (1000, Item.PixieSticks)
}

define treatboosts = {
    Item.PlainBread: "Normal",
    Item.SpicyJerky: "Fire",
    Item.WaterBottle: "Water",
    Item.EnergyDrink: "Electric",
    Item.SaladWrap: "Grass",
    Item.IcePop: "Ice",
    Item.KnuckleSandwich: "Fighting",
    Item.FastFood: "Poison",
    Item.GroundBeef: "Ground",
    Item.BouffalantWings: "Flying",
    Item.BrainFood: "Psychic",
    Item.PicnicBasket: "Bug",
    Item.RockCakes: "Rock",
    Item.SoulFood: "Ghost",
    Item.GummyWyrms: "Dragon",
    Item.DarkChocolate: "Dark",
    Item.SteelcutOats: "Steel",
    Item.PixieSticks: "Fairy"
}

init python:
    def GetTreatBoost(monid):
        if (activetreat == None):
            return 1
        elif (treatboosts[activetreat] in [pokedexlookup(monid, DexMacros.Type1), pokedexlookup(monid, DexMacros.Type2)]):
            return wildcount + 1
        return 1

    def GrabFromEncounterPool(encounterpool):
        encounterlist = []
        encountermax = 0
        for entry, odds in encounterpool.items():
            if (activerepel == None
            or activerepel == "Repel" and odds < 10
            or activerepel == "Super Repel" and odds < 7
            or activerepel == "Max Repel" and odds < 5):
                encounterlist.append((encountermax, entry))
                encountermax += (odds * GetTreatBoost(entry))
        encounterlist.append((9999, 0))
        
        randnum = RandInt(0, encountermax)
        for i in range(len(encounterlist)):
            if (randnum <= encounterlist[i + 1][0]):
                return encounterlist[i][1]

    def GenerateRandomEvent(location):
        global sidemonnum, sidemonnum2, sidemonnum3
        global activerepel
        global repelstepsleft
        #events = []
        #generate more random events through this
        
        goodguys = [MakeRed()]
        badguys = []
        if (IsDate(17, 5, 2004) and location == "fields"):
            goodguys.append(MakeTrainer("Leaf", TrainerType.Ally))
            goodguys.append(MakeTrainer("Dawn", TrainerType.Ally))

        for i, char in enumerate(goodguys):
            encounterpool = {}
            levelrange = range(3, 10)
            if (location == "fields"):
                encounterpool = {
                    263: 10,
                    155: 3,
                    399: 10,
                    191: 10,
                    835: 10,
                    133: 1,
                    919: 10,
                    406: 7,
                    29: 7,
                    32: 7,
                    333: 7,
                    307: 7,
                    401: 10,
                    111: 5,
                    710: 5,
                    659: 10,
                    967: 3,
                    777: 7,
                    764: 7
                }
            elif (location == "alley"):
                levelrange = range(6, 12)
                encounterpool = {
                    431: 10,
                    725: 1,
                    767: 10,
                    412.2: 10,
                    81: 10,
                    351: 1,
                    559: 7,
                    568: 10,
                    104: 7,
                    629: 7,
                    677: 7,
                    917: 10,
                    744: 3,
                    353: 10,
                    88.1: 10,
                    714: 5,
                    965: 5,
                    439: 5
                }
            elif (location == "seaport"):
                levelrange = range(9, 15)
                encounterpool = {
                    190: 10,
                    58: 7,
                    223: 10,
                    781: 1,
                    602: 3,
                    131: 1,
                    852: 7,
                    690: 7,
                    194.1: 10,
                    580: 10,
                    976: 5,
                    595: 7,
                    688: 10,
                    592: 5,
                    592.1: 5,
                    318: 7,
                    885: 3,
                    393: 3,
                    298: 10
                }
            elif (location == "mountain"):
                levelrange = range(14, 20)
                encounterpool = {
                    234: 3,
                    776: 1,
                    86: 10,
                    459: 10,
                    74.1: 10,
                    712: 7,
                    739: 7,
                    757: 7,
                    220: 10,
                    225: 7,
                    337: 5,
                    338: 5,
                    872: 7,
                    932: 10,
                    425: 10,
                    624: 3,
                    996: 1,
                    27.1: 7,
                    703: 5
                }

            newpokemonnum = GrabFromEncounterPool(encounterpool)
            newpokemon = Pokemon(newpokemonnum, level = 1, shinylock=False)
            minlevel = levelrange[0]
            maxlevel = levelrange[len(levelrange) - 1]

            newpokemon.UpdateLevel(RandomChoice(levelrange))
            newpokemon.Heal()
            if (i == 0):
                sidemonnum = newpokemonnum
            elif (i == 1):
                sidemonnum2 = newpokemonnum
            elif (i == 2):
                sidemonnum3 = newpokemonnum
            trainer2 = Trainer("sideportraitfull", TrainerType.Enemy, [newpokemon], isPokemon=True)
            badguys.append(trainer2)

        repelstepsleft -= 1
        if (repelstepsleft == 0):
            activerepel = None

        specialuniforms = []
        specialoutfits = []
        if (IsDate(18, 5, 2004) and timeOfDay == "Morning"):
            specialuniforms=[True, False]

        if (specialuniforms == []):
            if (location == "mountain" and GetRelationshipRank("Silver") > 1):
                specialoutfits=["winter", ""]

        renpy.call("Battle", goodguys + badguys, uniforms=specialuniforms, customoutfits=specialoutfits, healParty=False, specialmusic=("Audio/Music/RBY_Pokemon_Start.ogg", "Audio/Music/RBY_Pokemon_Loop.ogg"), canBeDitto=True)

label cyclizarhuntpart2:
    $ AddEvent("Dawn", "UsedGummyWyrms")
    show leaf angrybrow frownmouth with dis:
        xpos 0.66

    show dawn with dis:
        xpos 0.33

    dawn @sadbrow talkingmouth "I-is... is something wrong, Leaf?"

    leaf @talkingmouth "Yeah. My feet hurt, and I'm all tired and sweaty, and these Cyclizar are {i}way{/i} rarer than I thought they'd be."

    dawn @closedbrow "H-hold on... I think I know what to do here. Um, a staff member... I think he's staff anyway... gave me these."
    dawn @talkingmouth "They're called 'PokéTreats', and they, um, they're meant to attract certain wild Pokémon to your location."

    dawn @talkingmouth "Let's see... this one's the 'Gummy Wyrms', I think. It should make Dragon-types more common."

    $ activetreat = Item.GummyWyrms

    narrator "[bluecolor]Dawn used the Gummy Wyrms.{/color} Now, for every consecutive win, your chances of encountering a Dragon-type Pokémon will increase."

    return

label bluetalkmountainfieldtrip:
    $ AddEvent("Blue", "MountainTalk")
    show blue uniform wistfulbrow glancemouth with dis

    red uniform @talkingmouth "Hey, Blue."

    blue @glancebrow wistfulmouth "Oh. Hi."

    $ ValueChange("Blue", 1, 0.5)

    pause 1.0

    red @talkingmouth "Talk to your grandpa yesterday?"

    pause 1.0

    blue @talkingmouth "Not yet."

    pause 0.5

    blue "{w=0.5}.{w=0.5}.{w=0.5}."

    blue @wistfulmouth "I don't want him to pay attention to me {i}just{/i} because I've got this Eevee."

    hide blue with dis

    pause 1.0

    red @closedbrow talking2mouth "Good talk."

    return

label dawntalkmountainfieldtrip:
    $ AddEvent("Dawn", "MountainTalk")
    show dawn uniform with dis

    red uniform @talkingmouth "Hi, Dawn."

    dawn @happy "O-oh! Hi, [first_name]."

    $ ValueChange("Dawn", 1, 0.5)

    red @talkingmouth "You seem to be in high spirits. Does this place remind you of home?"

    dawn @talkingmouth "A little bit."
    dawn @sadbrow talkingmouth "If I'd known we were taking a class trip out here so soon, though, I wouldn't have gone out here alone last Wednesday."

    red @happy "Think of it like an early advantage. You're the Veteran, now, who can guide all us rookie trainers to the best spots on the mountain."

    dawn @talkingmouth "I guess. Actually, it's nice that I don't need to rush around like everyone else. I can just look at the mountain and enjoy the scenery for a while. {i}Sigh...{/i}"
    dawn @happy "This is actually some great inspiration for that ice sculpture I was making. I wasn't sure what kind of pedestal I wanted..."

    pause 0.5

    dawn happy @sadbrow talkingmouth "I don't suppose it'd be weird if I asked you to pose for me just so I can sketch out some ideas?"

    red @happy "Might be a little weird, but it's the kind of weird I like. Let's do it."

    narrator "You pose for a bit. You feel ridiculous, but Dawn seems very enthusiastic about her sketches, so you try to avoid laughing."

    dawn @talkingmouth "This is great!"

    pause 1.0

    dawn -happy @sadbrow talkingmouth "Um... j-just out of curiosity, I'm not planning anything, but, um... do you have plans this Saturday?"

    red @talkingmouth "Hm? Not that I know of."

    dawn @closedbrow talkingmouth "W-well, it's my Birthday this Saturday, so, um, if you were interested... then... maybe we could... do a thing...?"

    red @happy "Hey, are you inviting me to a birthday party?"

    dawn @sadbrow talkingmouth "M-more or less."

    red @talkingmouth "That sounds great. I'd love to come, Dawn. When and where?"

    dawn @surprised "O-oh. I, um, I don't know. I don't actually have anything planned. I wasn't planning on celebrating, or anything... until very recently."

    red @talkingmouth "Well... we don't have a lot of time. How about you give me a call when you have the deets?"

    dawn surprised "C-c-c-call?!"

    red @closedbrow talkingmouth "A text is fine too."

    dawn -surprised @sadmouth closedbrow "Y-yes, please."
    dawn @closedbrow sadmouth "I... I guess I should ask for your phone number, then... and give you mine."

    red @winkeyes talkingmouth "Yeah, it'd make calling me a bit easier."

    dawn @closedbrow "A-alright, then..."

    $ BecomeContacted("Dawn")

    hide dawn with dis

    return

label hilberttalkmountainfieldtrip:
    $ AddEvent("Hilbert", "MountainTalk")
    show hilbert uniform with dis

    red uniform @talkingmouth "Hey, Hilbert. You looked like you were struggling up the hill, a bit."

    hilbert @closedbrow talkingmouth "Apparently Cyclizar riding takes more grip strength and coordination than I possess."

    pause 0.5

    hilbert @talkingmouth "At least it'll be easy to go back down. Even if I fall off, I'm going the right way."

    pause 2.0

    show hilbert sadbrow with dis

    red @surprised "Was that a joke?"

    hilbert @angrybrow talkingmouth "It was a mistake. Just like coming up here was. I hate the cold. I hate the ice. I hate everything about this."

    pause 1.0

    red @confusedeyebrows frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    show hilbert surprised with dis

    red @happy "We could huddle together for warmth."

    $ ValueChange("Hilbert", 1, 0.5)

    hilbert @closedbrow "D-don't... say ridiculous things like that."
    hilbert @angrybrow talkingmouth "Not unless your words are true."

    red @playfulbrow smirkmouth "Oh, so {i}now{/i} you care about truth?"

    hilbert @sadbrow talkingmouth "I'm leaving."

    hide hilbert with dis

    return

label ethantalkmountainfieldtrip:
    $ AddEvent("Ethan", "MountainTalk")

    show icecave with dis

    narrator "You follow Ethan into an icy cave."
    narrator "However, as soon as you step in, you don't see him anywhere."

    if (IsWeekend()):
        red @talkingmouth "Ethan, bud? You around?"

        show ethan with dis

    else:
        red uniform @talkingmouth "Ethan, bud? You around?"

        show ethan uniform with dis

    ethan @talkingmouth "Oh, hey. Yeah, I came up here to train. I was just checking out the echo in this cave." 

    $ ValueChange("Ethan", 1, 0.5)
    
    ethan @happy "Check this out."

    ethan @happy "{size=40}I'm here!{/size}"

    Character("Echo") "{size=30}I'm here!{/size}"
    Character("Echo") "{size=20}I'm here.{/size}"
    Character("Echo") "{size=10}I'm here...{/size}"
    
    ethan @talkingmouth "Neat, huh? And all the ice makes it kinda pretty, too."

    red @happy "Pretty as a Pecharunt."

    ethan @confused "What?"

    red @talkingmouth "It's a Pokémon from Kitakami. Um, creates Mochi zombies. That's what I've heard, anyway. They're meant to be extremely rare."

    ethan @talkingmouth "Gotcha."

    pause 1.0

    ethan @sad2eyes talking2mouth "Welp, I'm outsies. Looks like there aren't any Pokémon in this cave, now, so we should probably head to the main path."

    red @talkingmouth "Sure. I'll spend just a little bit more time in here. You go on ahead."

    ethan @talking2mouth "Sounds good, man. Don't spend too long in here, though. You'll go crazy talking to the echoes."

    red @happy "I'll keep that in mind."

    hide ethan with dis

    pause 2.0

    narrator "You spend a bit more time looking around the cave, but besides a large rock that seems somewhat out-of-place in the cave, nothing grabs your attention."
    narrator "Every few minutes, a single droplet of water lands on the rock, very, {i}very{/i} slowly covering it in ice. Perhaps, a long time in the future, this rock will be fully frozen."
    narrator "Or perhaps the frozen water will worm its way into the rock's cracks, and just shatter it to pieces. We must pray that the rock can endure."

    redmind @thinking "...Ethan's right, this place {i}does{/i} make you go crazy."

    pause 0.5

    red @talkingmouth "Alright, let's get out of here."

    pause 1.0

    show kris angrymouth with dis:
        xpos 0.25

    pause 1.0

    kris @sadbrow talking2mouth "Oh, Ethan... what happened to you...?"

    pause 0.5

    kris sadbrow @talkingmouth "Thank goodness you've got that [first_name] to watch out for you, at least..."

    $ ValueChange("Kris", 1, 0.5)

    kris angrybrow talking2mouth "I'll figure this out, Ethan. Don't worry."

    hide kris 
    hide icecave
    with dis

    return
