label shatteredglades: #fighting-type dungeon, should be medium-difficulty, partners are Leaf, Flannery, and Whitney
$ HealParty(Trainer("Leaf", TrainerType.Ally, GetTrainerTeam("Leaf")))
$ HealParty(Trainer("Flannery", TrainerType.Ally, GetTrainerTeam("Flannery")))
$ HealParty(Trainer("Whitney", TrainerType.Ally, GetTrainerTeam("Whitney")))

if (timeOfDay == "Night"):
    show leaf at rightside, night
    show flannery at leftside, night
    show whitney at night
    with dis

else:
    show leaf at rightside
    show flannery at leftside
    show whitney
    with dis

leaf @happy "Alright, let's go! The Tia untrapment team is ready to roll out!"

if (timeOfDay == "Night"):
    red night @confused "'Untrapment'?"

else:
    red @confused "Untrapment?"

leaf @sarcastic "You try coming up with a word that means 'rescue' and begins with 'T.'"

whitney @talkingmouth "Does everyone have everything they need? I've got some bandages and antiseptics, in case we get bonked by anything in there, but we should still be careful."

flannery @talking2mouth "I looked ahead. According to this old forum post from a former student, this part of the forest is called the 'Shattered Glades.'"

leaf @surprised "Woah, edgy name. Why?"

flannery @closedbrow talking2mouth "There's a bunch of really hard ironwood trees in this part of the forest. Fighting-types gather to train here by punching the trees, and they end up smashing trees all over the place."
flannery @talkingmouth "Of course, there's also a bunch of Grass-types. It {i}is{/i} a forest."

leaf @closedbrow talking2mouth "Hm. Alright. Sounds like Flying-types would be useful in here, then..."

whitney @angry "Alright, enough standing around! Are we going to {i}do{/i} this thing?"

menu:
    "Hell yeah!":
        leaf @happy "She helped us out, [first_name]--now it's our turn!"

        whitney @talkingmouth "I'm responsible for Tia. So I've gotta pull her out of whatever trouble she's in!"

        flannery @closedbrow talkingmouth "She's our little sister. And we gotta take care of her. Time to wake up and smell the coffee."
        flannery @sadbrow talkingmouth "Although, to be honest, I'm still having some difficulty believing she's a dragon."

    "Just one moment.":
        hide whitney
        hide leaf
        hide flannery
        with dis

        if (timeOfDay == "Night"):
            jump aftersetupnight

        else:
            jump aftersetup

label shatteredgladessetup:
python:
    technicaldungeon = True
    fullsquad = [MakeRed(), MakeTrainer("Whitney", TrainerType.Ally), MakeTrainer("Leaf", TrainerType.Ally), MakeTrainer("Flannery", TrainerType.Ally)]
    wildpool = [
        pokedexlookupname("Makuhita", DexMacros.Id), 
        pokedexlookupname("Mankey", DexMacros.Id), 
        pokedexlookupname("Rowlet", DexMacros.Id),
        pokedexlookupname("Meditite", DexMacros.Id),
        pokedexlookupname("Paras", DexMacros.Id)
    ]
    activedungeon = Dungeon("fallforest", "Shattered Glades", fullsquad, wildpool, "splinteredcopse", "forestdungeonloss", 7, AimLevel(), 
        dungeoncutscenefunc=None, 
        fudgerollfunc=None, 
        eventfunc=None,
        generateitems=[(20, "Gimmighoul Coin"), (10, "Cheri Berry"), (10, "Oran Berry"), (7, "Sitrus Berry"), (5, "Black Belt"), (5, "Miracle Seed")])

stop music fadeout 1.5
queue music "audio/music/duskforest.ogg"

$ HealParty()

jump StartDungeon

label splinteredcopse:

stop music fadeout 1.5
queue music "audio/music/potown_start.ogg" noloop
queue music "audio/music/potown_loop.ogg"

if (timeOfDay == "Night"):
    scene midnightforest
    show leaf at rightside, night
    show flannery at leftside, night
    show whitney sadbrow frownmouth at night
    with dis

else:
    scene eveningforest
    show leaf at rightside
    show flannery at leftside
    show whitney sadbrow frownmouth
    with dis

flannery @happy "Wow! We made it through! Wasn't that {i}great?!{/i}"

whitney @sad "Noooo! I never want to do that again! My feet hurt, and I'm all sweaty, and a million different branches poked me, and I hate the wild!"

leaf @talking2mouth "Whitney, I'm not the biggest fan of the outdoors, either, but aren't you being a bit tough on mother nature?"

whitney @closedbrow surprisedmouth "No! Mother Nature's a bitch! I never want to see her, ever again!"

flannery @sweat talkingmouth "I mean... we still need to get back out after we find Tia..."

whitney @sadeyebrows sad2eyes talking2mouth "...Right. For Tia. Mmmrgrrgrr..."

if (timeOfDay == "Night"):
    show flannery surprised:
        xpos 0.25
    show whitney surprised at night
    with dis
else:
    show flannery surprised:
        xpos 0.25
    show whitney surprised
    with dis

leaf surprised "Wait... oh, wow, our job just got a lot easier!"

flannery @angryeyebrows talking2mouth "Wait, do you mean..."

stop music fadeout 1.5
queue music "audio/music/reliccastle_loop.ogg"

hide flannery
hide whitney
hide leaf
with dis

pause 1.0

if (timeOfDay == "Night"):
    show latias poweredangryeyes powered angrymouth at night with Dissolve(1.0):
        ypos 1.0 xpos 0.5
        parallel:
            ease 2.0 ypos 1.05
            ease 2.0 ypos 1.0
            repeat

        parallel:
            ease 2.0 xpos 0.52
            ease 2.0 xpos 0.5
            ease 2.0 xpos 0.48
            ease 2.0 xpos 0.5
            repeat

else:
    show latias poweredangryeyes powered angrymouth with Dissolve(1.0):
        ypos 1.0 xpos 0.5
        parallel:
            ease 2.0 ypos 1.05
            ease 2.0 ypos 1.0
            repeat

        parallel:
            ease 2.0 xpos 0.52
            ease 2.0 xpos 0.5
            ease 2.0 xpos 0.48
            ease 2.0 xpos 0.5
            repeat

$ PlaySound("pokemon/cries/380.mp3")

latias "...Ra! Rati, lati, tiiii-AS!"

pause 1.0

if (timeOfDay == "Night"):
    leaf night @sadbrow surprisedmouth "Oh, no, what's happening to her?! Why's she screaming like that?"

    whitney night @sad "It's like she's been possessed!"

    red night @sad "Tia...!"

    flannery night @surprised "Holy shit, she actually {i}is{/i} a dragon?!"

else:
    leaf @sadbrow surprisedmouth "Oh, no, what's happening to her?! Why's she screaming like that?"

    whitney @sad "It's like she's been possessed!"

    red @sad "Tia...!"

    flannery @surprised "Holy shit, she actually {i}is{/i} a dragon?!"

latias @closedeyes "Laaaat... ti, {i}ti{/i}, TI!"

pause 1.0

latias soullesseyes talking2mouth "{i}Latias.{/i}"

leaf @surprised "Uh-uh-uh-- she's coming right for us!"

if (timeOfDay == "Night"):
    show midnightforest:
        xalign 0.5 yalign 0.5
        ease 2.0 zoom 1.2

    show latias at night:
        ease 2.0 xpos 0.5 ypos 1.2 zoom 1.3

    leaf @surprised "Watch out!"

    show latias at night:
        ease 0.3 ypos 2.0 zoom 3.0 alpha 0.0

    show leaf at night:
        xpos 0.25 alpha 0.0 ypos 2.0 rotate 0 zoom 1.3
        ease 0.3 xpos 0.5 alpha 1.0 ypos 1.0 zoom 1.0

    $ PlaySound("thud2.ogg")

    pause 0.3

    show midnightforest at vpunch
    show leaf closedbrow angrymouth at night:
        ypos 1.2 zoom 1.3 rotate 10 alpha 1.0
    
    leaf @angrymouth "{size=30}Shit, that hurt.{/size}"

    show leaf at night:
        ypos 1.2 zoom 1.3 rotate 10 alpha 1.0
        ease 0.5 ypos 2.0 rotate 40

    red @surprised "Why-- why did you jump in front of her like that?!"

    leaf "{size=30}C'mon. What part of that was out-of-character for me?{/size}"

    red @sadbrow talking2mouth "That was dumb, Leaf."

    leaf "It was tactical. You're a better battler than me."

    flannery @surprised "Uh, she's coming around for another swipe!"

    show latias poweredangryeyes powered angrymouth at night with Dissolve(2.0):
        ypos 0.9 xpos 0.5 alpha 1.0 zoom 1.0
        parallel:
            ease 2.0 ypos 0.95
            ease 2.0 ypos 0.9
            repeat

        parallel:
            ease 2.0 xpos 0.52
            ease 2.0 xpos 0.5
            ease 2.0 xpos 0.48
            ease 2.0 xpos 0.5
            repeat

else:
    show eveningforest:
        xalign 0.5 yalign 0.5
        ease 2.0 zoom 1.2

    show latias:
        ease 2.0 ypos 1.2 zoom 1.3 xpos 0.5

    leaf @surprised "Watch out!"

    show latias:
        ease 0.3 ypos 2.0 zoom 3.0 alpha 0.0

    show leaf:
        xpos 0.25 alpha 0.0 ypos 2.0 rotate 0 zoom 1.3
        ease 0.3 xpos 0.5 alpha 1.0 ypos 1.0 zoom 1.0

    $ PlaySound("thud2.ogg")

    pause 0.3

    show eveningforest at vpunch
    show leaf closedbrow angrymouth:
        ypos 1.2 zoom 1.3 rotate 10 alpha 1.0

    leaf @talkingmouth "{size=30}Shit, that hurt.{/size}"

    show leaf:
        ypos 1.2 zoom 1.3 rotate 10 alpha 1.0
        ease 0.5 ypos 2.0 rotate 40

    red @surprised "Why-- why did you jump in front of her like that?!"

    leaf "{size=30}C'mon. What part of that was out-of-character for me?{/size}"

    red @sadbrow talking2mouth "That was dumb, Leaf."

    leaf "It was tactical. You're a better battler than me."

    flannery @surprised "Uh, she's coming around for another swipe!"

    show latias poweredangryeyes powered angrymouth with Dissolve(2.0):
        ypos 0.9 xpos 0.5 alpha 1.0 zoom 1.0
        parallel:
            ease 2.0 ypos 0.95
            ease 2.0 ypos 0.9
            repeat

        parallel:
            ease 2.0 xpos 0.52
            ease 2.0 xpos 0.5
            ease 2.0 xpos 0.48
            ease 2.0 xpos 0.5
            repeat

leaf "So {i}battle.{/i}"

flannery @angry "Dragon or not, let's save our friend!"

whitney @angry "[bluecolor]Tia doesn't know any attacking moves...{/color} so don't worry about her! Just beat down her team!"
whitney @sadbrow talking2mouth "Although... just stating {i}all{/i} our options here... but if we knock her out, her other Pokémon will probably give up."

flannery @furious "Whitney!"

python:
    trainer1 = MakeRed()
    trainer2 = MakeTrainer("Whitney", TrainerType.Ally)
    trainer3 = MakeTrainer("Flannery", TrainerType.Ally)
    tiaobj = Pokemon("Latias", nickname = "Tia", level=70, item="Soul Dew", ivs=[15, 15, 15, 15, 15, 15], gender=Genders.Female, moves=[GetMove("Sweet Kiss"), GetMove("Light Screen"), GetMove("Reflect"), GetMove("Heal Pulse")], nature=Natures.Bashful, intelligence = 1)
    tiaobj.ApplyStatus("frenzied")
    tiaparty = [tiaobj] + GetTrainerTeam("Tia")
    trainer4 = Trainer("latias", TrainerType.Enemy, tiaparty, 2)
    trainer4.IgnoresDungeons = True
    HealParty(trainer2)
    HealParty(trainer3)
    HealParty(trainer4)
    tiaobj.Moves[0].PP = 1
    tiaobj.Moves[1].PP = 2
    tiaobj.Moves[2].PP = 2
    tiaobj.Moves[3].PP = 1

call Battle([trainer2, trainer1, trainer3, trainer4], healParty=False, customexpressions=["whitney frownmouth angrybrow", "whitney angry", "red frownmouth angrybrow", "red angrybrow angrymouth", "flannery angrybrow angrymouth", "flannery angry2eyes angry2eyebrows furiousmouth", "latias soullesseyes frownmouth", "latias poweredangryeyes angrymouth powered ruffle poweredruffle"], specialmusic="Nothing", unrunnable=True, dialogfunc=possessedtiadialog) from _call_Battle_127
$ battlehistory["Tia1"]  = _return

if (not WonBattle("Tia1")):
    jump forestdungeonloss

stop music fadeout 1.5
queue music "audio/music/TiaTheme_start.ogg" noloop 
queue music "audio/music/TiaTheme_loop.ogg"

if (timeOfDay == "Night"):
    show leaf sadbrow frownmouth at night:
        xpos 0.8 ypos 1.0 zoom 1.0 rotate 0
    show latias closedbrow frownmouth behind leaf at night:
        xpos 0.6
    show whitney frownmouth at night:
        xpos 0.4
    show flannery frownmouth at night:
        xpos 0.2
    with dis

else:
    show leaf sadbrow frownmouth:
        xpos 0.8 ypos 1.0 zoom 1.0 rotate 0
    show latias closedbrow frownmouth behind leaf:
        xpos 0.6
    show whitney frownmouth:
        xpos 0.4
    show flannery frownmouth:
        xpos 0.2
    with dis

pause 1.0

leaf -sadbrow @talkingmouth "Did we... did we hit her too hard...?"

whitney @talking2mouth "Nah, she's fine. She's just fainted, same as any other Pokémon."
whitney -frownmouth @happy "A revive should fix this right up!"

latias @sadeyes "{w=0.5}.{w=0.5}.{w=0.5}."

latias surprised "!"

if (timeOfDay == "Evening"):
    hide latias
    show tia surprised:
        xpos 0.6
    with gaussdissolve
else:
    hide latias
    show tia surprised at night:
        xpos 0.6
    with gaussdissolve

tia "Hi, Whitney, Flannery! I must've... um... fallen asleep."

flannery @tiredbrow talking2mouth "You... fell asleep."

tia sadbrow "Yep. I fell asleep under my very realistic dragon blanket."

if (timeOfDay == "Evening"):
    redmind @confusedeyebrows frownmouth "I'm going to assume Tia {i}just{/i} learned about lying."

    show tia angrybrow frownmouth with dis:
        xpos 0.6
else:
    redmind night @confusedeyebrows frownmouth "I'm going to assume Tia {i}just{/i} learned about lying."

    show tia angrybrow frownmouth at night with dis:
        xpos 0.6

flannery @talkingmouth "...Looked more like a bird."

tia @angry "I'm not a bird! Don't call me a bird! I'm--Whitney, I know you're leaving something out, translate {i}everything{/i} I'm saying!"

whitney @talking2mouth "Relax, Tia. It's alright. Flan knows about you."

flannery @sad2eyes angryeyebrows talking2mouth "{size=30}Yeah, but I was the last one to learn, {i}again.{/i}{/size}"

tia surprised "What?"

whitney @talkingmouth "Pretty much the entire nurse program knows, too."

tia "Oh."

pause 1.0

tia sadbrow frownmouth "Oh."

flannery @sad "What's wrong? What {i}really{/i} happened?"

tia @closedeyes angrymouth "I don't... I don't remember exactly what happened, but... I think I started getting a headache, and then... someone attacked me! Yeah, I was attacked!"
tia @downeyes talking2mouth "And when I was attacked... I lost my hat."

whitney @sadbrow happymouth "Again?"

leaf @sadbrow happymouth "It's alright, sweetie. I'll buy you another."

tia @sadbrow talking2mouth "Thanks..."

flannery @talking2mouth "Before we go shopping, though, we need to get back to the school."

whitney @happy "Don't worry! I've got tons of potions. We'll be fine."

red @confused "Um... Couldn't Tia just fly us out of here?"

tia @talkingmouth "...Yes. I could."

red @talkingmouth "Got enough energy for it?"

tia @happy "Sure do!"

pause 2.0

tia frownmouth @confusedeyebrows "Am I flying?"

leaf @sarcastic "No."

tia @sadbrow -frownmouth "Oh. I guess I don't."

flannery @happy "The old-fashioned way it is, then. Good! I've got more than enough energy left to burn! This reminds me of hikes down the east side of Lavaridge."

whitney sad tears "Noooo! I haaaate the wiiiiiild!"

python:
    whitneyalive = False
    leafalive = False
    flanneryalive = False
    if (activedungeon != None):
        for mob in activedungeon.Party:
            if (mob.Name == "whitney" and mob.GetTeam()[0].Health > 1):
                whitneyalive = True
            elif (mob.Name == "leaf" and mob.GetTeam()[0].Health > 1):
                leafalive = True
            elif (mob.Name == "flannery" and mob.GetTeam()[0].Health > 1):
                flanneryalive = True
    
if (whitneyalive):
    whitney -frownmouth @talkingmouth "...Although, um, serious time. My feet are really sore, and I can't just spray a potion on myself. [first_name], you were a massive help. Do you think you could do just one more thing and--" 

    $ ValueChange("Whitney", 5, 0.4)

    red @closedbrow sweat talkingmouth "Not a chance."

    whitney "Ah, boo!"

else:
    whitney @talkingmouth "...Although, um, serious time. I'm really banged up right now, and I can't just spray a potion on myself. Flannery, could you--"

    flannery @playfulbrow talking2mouth "Not a chance."

if (flanneryalive):
    flannery -frownmouth @talking2mouth "Man, I forgot how good it feels... I should {i}really{/i} get out like this more. Thanks Whit, Leaf, [first_name]."

    $ ValueChange("Flannery", 5, 0.2)

else:
    flannery @sweat talking2mouth "I feel... pretty banged up as well, actually. I think, if I could fly, I wouldn't be able to now, either."

leaf -frownmouth @talkingmouth "Hey, we got the mission done, together, just like I said. I'm two for two on rescue missions right now! Not bad, if I say so myself."

$ ValueChange("Leaf", 3, 0.8)

red @talkingmouth sweat closedbrow "Yeah, yeah, pat yourself on the back a bit harder. C'mon, let's get back to the school."

call clearscreens() from _call_clearscreens_153
show blank2 with splitfade

pause 1.0

narrator "Everyone makes their way back to the infirmary, battered and bruised."

$ AddEvent("Tia", "Rescued")
$ rescuedtia = True
$ lastsaved = "Tia"
$ technicaldungeon = False
$ _rollback = True
$ renpy.block_rollback()

jump infirmary