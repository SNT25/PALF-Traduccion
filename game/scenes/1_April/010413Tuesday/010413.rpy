label day010413:

$ timeOfDay = "Morning"

if (pikachuobj in playerparty):
    $ playerparty.remove(pikachuobj)

call calendar(1) from _call_calendar_8
$ calDate = calDate.replace(day=13, month=4, year=2004)

show morning at vspaz

$ renpy.music.play("Audio/Morning_ambience.ogg", channel='crowd', loop=True, fadein=1.0)

scene dorm_A 
with transeye2
$ renpy.transition(dissolve)
show screen currentdate

show brendan at getcloser behind blank2

$ renpy.pause(1.0, hard=True)

hide blank2

red casual hatless @surprised "Woah. Hello there, welcome to my personal space. What's up?"

show brendan at getfurther 

brendan @happy "I was thinkin' we could go out to the fields together this mornin'! Before school begins."

brendan @talking2mouth "Maybe catch some new Pokémon, y'know?"

if (HasEvent("Brendan", "NotCaughtSandshrew")):
    brendan @closedbrow talkingmouth "I still wanna try and catch a Sandshrew after that last one got away."

red @happy "Oh, sure! That sounds great. Just the two of us?"

$ renpy.music.stop(channel='crowd', fadeout=1.0)

brendan @talkingmouth "Yeah. I'd ask the others, but..."

show dorm_A:
    xalign 0.0 zoom 1.0
    ease 0.5 xalign 0.1 zoom 1.3
    pause 1.0
    ease 1.0 xalign 0.9
    pause 1.0
    ease 2.0 xalign 0.0 zoom 1.0

narrator "Looking around, you see that Calem and Ethan are still fast asleep."
narrator "Hilbert is,{w=0.25} notably,{w=0.25} not,{w=0.25} and is staring straight up at the ceiling, unblinking."

hilbert hatless @talkingmouth "Try to get me out of this bed before 7:00 AM and I will commit murder."

brendan surprisedbrow frownmouth @surprised "But you're already awake, bro."

hilbert @angry "Did you not hear me? Murder. I will commit it. Before 7 o'clock, Kobukan Standard Time. Death will come as a result of my actions."

brendan frownmouth @closedbrow talking2mouth "...I don't get it."

red @sadeyes sadeyebrows happymouth "H-hey, Brendan, how about we just get out of here before Hilbert really starts explaining, alright? Alright. We're all cool. Let's go."

brendan happy "Alright!"

$ renpy.music.play("Audio/Pokemon/pikachu_sad2.ogg", channel="altcry", loop=None)
pikachu yawn "Pika, pi-ka..."

show brendan -happy with dis

red @happy "It's alright, buddy, you can stay here if you want."

$ renpy.music.play("Audio/Pokemon/pikachu_angry1.ogg", channel="altcry", loop=None)
pikachu angry_2 "Pika!"

$ AddPikachu()

red @surprised "Or you can come with us, I guess. Man, you're moody in the mornings, aren't you? I should call you Pikannery."

brendan @closedbrow talkingmouth "Huh?"

red @talkingmouth "You know, like, Pikachu and Flannery? Flannery's a girl in my homeroom who, uh, {i}really{/i} doesn't handle mornings well."

brendan @talking2mouth "Huh, not sure I like the name. How about, uh, Flachu?"

red @happy "Gesundheit."

show brendan surprisedbrow frownmouth with dis

hilbert @angry "I will murder both of you. Both! Lots of blood! Blood and death!"

pause 2.0

red @confusedeyebrows talking2mouth "Is there an 'or' to that sentence, or...?"

show dorm_A with vpunch

stop music

play sound ["audio/Body Roll.ogg", "audio/Body Crash.ogg"]

hilbert @angry "GET OUT!"

scene blank2 with splitfadefaster

pause 2.0

show clouds:
    yalign 0.75
    ease 5.0 yalign 0.5
show fields1 :
    xalign 0.0
    ease 10.0 yalign 0.33 xalign 0.95
with Dissolve(2.0)

play music "Audio/Music/Fieldstheme_Start.ogg" noloop
queue music "Audio/Music/Fieldstheme_Loop.ogg"

pause 2.0

red @talkingmouth "...No, I think it'd still be better if we went with your third idea."

show brendan with dis

brendan @closedbrow talkingmouth "Yeah, that was a good one. What was that one, again? Flanachu?"

red @talkingmouth "Yeah, except two 'n's. So, like, Flan-nachu."

brendan @surprised "I dunno, bro, it still sounds a bit too much like 'flan nachos.' I think I just came up with it 'cause I was hungry."

red @closedbrow talking2mouth "Hungry for the nachos, I guess? I know you don't like sweet things."

brendan sad "Well, I'm glad {i}someone{/i} does. I swear, I keep tellin' May, but I think she really only knows how to make candy! I've volunteered to cook so many times, but..."

pause 1.0

red @surprised "Uh... not where I expected this to go."

brendan -sad @happy "Ah, sorry, bro. Overshared, huh?"

red @happy "We're cool. Let's just settle with Flanachu, then."

brendan @talking2mouth "Right on."

pause 2.0

brendan @surprised "Oh, shit, we ran all the way here! {w=0.5}{nw}" 
extend @happy " Didn't even notice!"

red @talkingmouth "Looks like we're not the only ones. Check it out."

show brendan:
    ease 0.5 xpos 0.75

show brawly at leftside with dis

brawly @talkingmouth "Hey, bros! You guys going for a run before school?"

brendan @talking2mouth "We sure are! Thought we might catch some Pokémon, as well."

brawly @talkingmouth "Right on."

red @talkingmouth "What's a student council member doing here this early in the morning? Just running?"

brawly @happy "Sorta! I'm also re-stockin' the fields with imported Pokémon."

brendan @surprised "Woah. I knew the Pokémon here were imported, but I didn't think that the Student Council was responsible for importing them."

brawly @talkingmouth "I volunteered for this, actually. Anythin' to get me out of the SC office, y'know. My Hariyama hates all the paperwork Roxanne makes us do."

red @talkingmouth "Are all Student Councils so focused on... paperwork? That kinda stuff?"

brawly @talkingmouth "Eh, it depends on how the Prez wants to run it, really. Some SCs are all about organizing tournaments and new programs for the school."
brawly @happy "Some are more about enforcin' discipline, and making sure that Kobukan's reputation doesn't slip, and its budget is airtight."
brawly @talkingmouth "Really depends. The council might be very active, or very passive. Very powerful, or very weak. Even just the time of the year can change that. The biggest changes always happen after an election."
brawly @happy "Anyway, that's what the guy last year told me! Heh heh. I've pretty much forgotten what the last council was like. It's been Roxanne's council for the last year, and we haven't really done much."

brendan sad "Oh... sorry, man. Do you feel like you missed out?"

brawly @happy "Nah! I bagged the Student Council prez, and that's way better than actually gettin' anythin' done."

brendan -sad @happy "My man!"

show brendan happy with dis:
    xpos 0.75
    ease 0.3 xpos .6

show brawly happy with dis:
    xpos 0.25
    ease 0.3 xpos .4

pause 0.1

$ PlaySound("clap.ogg")

pause 1.0

show brendan -happy with dis:
    xpos 0.6
    ease 1.0 xpos .75

show brawly  -happy with dis:
    xpos 0.4
    ease 1.0 xpos .25

pause 0.5

red @talkingmouth "Hey, as a Student Council member, what do you think about the new candidates campaigning for the Student Council?"

brawly @talkingmouth "Well, those two Kalos kids are probably going to get in. They've been pretty busy campaigning, and they're not sayin' anything that scares people away."
brawly @talkingmouth "Cheren, well, I'm not so sure about. I mean, Roxanne really doesn't like him. He's given one too many speeches about 'the complacency of the current administration.'"

red @closedbrow talking2mouth "Really... of all the candidates I know of, it seems like he's been trying the hardest. And his ideas sound really good, if hard to achieve."

brawly @talkingmouth "Yeah, well... Roxanne was like that before she got elected, too. I mean, the school's a business. Some stuff, a student just can't do."

red @sad "Maybe... you should tell Cheren this? He might need to hear it from someone with experience."

brawly @happy "Maybe I will."
brawly @talkingmouth "...But it might be nice to let him have hope for a bit longer."

pause 2.0

brawly @talkingmouth "Hey, I just realized where I remember you from! We met on the first day, didn't we? In Inspira?"

red @happy "Yeah, that's right! [first_name] here."

if (HasEvent("Brawly", "Covered")):
    brawly @happy "I really gotta thank you for covering for me back then."

    red @talkingmouth "It's alright. I {i}did{/i} slow you down, after all."

    brawly @talkingmouth "Nah, I mean it. Here, have a bunch of these. I normally throw these in random parts of the fields so new students can find and use them, but this time I'll give 'em directly to you."

    $ inventory[Item.PokeBall] = 10

    show pokeball at itemhover

    $ renpy.music.set_volume(0.25, delay=0.0, channel="music")
    $ PlaySound("item_get.ogg")
    $ renpy.music.set_volume(1.0, delay=2.0, channel="music")

    pause 2.0

    show pokeball at itemhide
    $ renpy.pause(1.5, hard=True)

    hide pokeball

    narrator "You gained 10 Poké Balls! They're covered in sweat..."

    brawly @talkingmouth "Anyway, now I remember your name, I get why you were askin' about the Student Council stuff."

else:
    brawly "Oh, right! Now I remember your name, I get why you were askin' about the Student Council stuff."

red @closedbrow talking2mouth "...Huh. What do you mean?"

brawly @happy "Well, you're running for Student Council, aren't you?"

if (not council_campaigning):
    menu:
        "Why does everyone keep saying that?":
            red @angrybrow talking2mouth "No. Seriously, I've never said that I am. I don't know why everyone keeps saying that."

        "Yeah, fine, I guess.":
            $ council_campaigning = True
            red @closedbrow talking2mouth "I wasn't, at first, but it seems like everyone else is kinda pushing me into it. I mean, even Cheren thinks I'm his biggest opponent."

else:
    red @happy "Er... yes, but I actually haven't, like, started? And I've only got two weeks left."

brawly @talkingmouth "Huh. Maybe it's just who you're hanging out with?"

$ highest = "Calem"
if (persondex["Serena"]["Value"] > persondex["Calem"]["Value"]):
    $ highest = "Serena"
if (persondex["Cheren"]["Value"] > persondex[highest]["Value"]):
    $ highest = "Cheren"

red @closedbrow talking2mouth "Maybe? I've been hanging out with [highest] a lot. Maybe people just see the two of us together, know that [highest] is involved in Student Council stuff, and think I am, too?"

brawly @happy "Hey, maybe. That's basically how I got roped into this. It's all a popularity contest at the end of the day, y'know?"

red @sadeyes sadeyebrows happymouth "Yeah... guess so."

redmind @thinking "Is this all just because of Frienergy? I wish I could share it with Cheren. Poor guy needs it way more than me."

brawly @happy "Anyway, bros, I'm off!"

menu:
    "{color=#b7669e}[[Charm]{/color} Wait! Put in a good word for me with the Council?" if council_campaigning:
        brawly @happy "Hah! Bro, I already did. I liked your vibe the day I met ya." 

        $ TraitChange("Charm")

        brawly @talkingmouth "You just need to get a bit tougher for yourself, alright? If something goes wrong, SC's the first place people blame."
        brawly @happy "You need some thicker skin if you wanna survive that."

    "{color=#b7669e}[[Charm]{/color} Wait! I want to join the Student Council!" if not council_campaigning:

        $ TraitChange("Charm")

        brawly @talkingmouth "...Uh... I thought you weren't trying to get in?"
        
        red @happy "I wasn't. But, I mean, if everyone's telling me I'm a shoo-in, it would be a shame to let this opportunity go to waste."

        brawly "Right on, bro. Grab that opportunity by the balls!"

    "Have time for a run before you leave?":
        brawly @happy "Hey, sure, why not?"

        hide blank2
        show blank2 with dis

        narrator "You, Brawly, and Brendan all run around the fields a couple times before collapsing in a sweaty, gross pile underneath a tree." 
        narrator "Your manly bonds are forged together under the anvil and hammer of exercise."
        narrator "As the steam rolls off your body and dissipates in the cool air of the morning dew, you cannot help but feel a greater connection to the universal manhood, the seed of life from which all manly things sprout."

        hide blank2 with dis

        $ ValueChange("Brendan", 1, 0.75)

brawly @happy "Well, it's been real, bros! I'm out."

red @happy "Bye."

hide brawly 
show brendan:
    xpos 0.75
    ease 0.5 xpos 0.5
with dis

pause 1.0

brendan @happy "Alright! Let's go catch some wild Pokémon! Wanna team up with me?"

red @happy "I totally would, but if your Pokémon don't listen to you super-well, it's probably for the best if we stay in our own lanes, you know?"

red @closedbrow talking2mouth "It'd probably be a lot harder to catch Pokémon with both of our guys acting at once."

brendan @surprised "Oh, yeah, that makes sense, dude." 
brendan @talking2mouth "Well, catch you later, then! Let's meet up before we go back to the dorms."

hide brendan with dis

if (GetItemCount("Poké Ball") == 0):
    red @talkingmouth "...Uh. Brendan?"

    show brendan with dis

    brendan @happy "Yeah, bro?"

    red @happy "Uh... can I have some Poké Balls? I don't actually have any on me."

    $ ballsleft = 20 - ballsused

    if (ballsleft > 10):
        brendan @surprised "Oh, sure, dude. I got a bunch left from Saturday. Here, take half."
        
        $ ballsgained = math.ceil(ballsleft / 2.0)
        $ inventory[Item.PokeBall] = ballsgained

        show pokeball at itemhover

        $ renpy.music.set_volume(0.25, delay=0.0, channel="music")
        $ PlaySound("item_get.ogg")
        $ renpy.music.set_volume(1.0, delay=2.0, channel="music")

        pause 2.0

        show pokeball at itemhide
        $ renpy.pause(1.5, hard=True)

        hide pokeball
        
        narrator "You gained [ballsgained] Poké Balls! They're covered in cookie crumbs..."

        red @happy "Thanks a bunch."

        redmind @thinking "Alright. Time to catch some new Pokémon. Since I can only keep six on me at a time, and I don't have anywhere to store my extras yet, I should be careful about filling up my party."
        redmind @thinking "I might be stuck with the same six Pokémon for a while, if I fill my party up now, and {color=#0048ff}you never know when a strong or rare Pokémon will show up.{/color}"

    elif (ballsleft > 5):
        brendan @closedbrow talkingmouth "Uh... I don't actually have all that many after Saturday. Think you could just take, like, five?"

        red @sadeyes sadeyebrows happymouth "I'll take it. Thanks a bunch."
        
        $ inventory[Item.PokeBall] = 5

        show pokeball at itemhover

        $ renpy.music.set_volume(0.25, delay=0.0, channel="music")
        $ PlaySound("item_get.ogg")
        $ renpy.music.set_volume(1.0, delay=2.0, channel="music")

        pause 2.0

        show pokeball at itemhide
        $ renpy.pause(1.5, hard=True)

        hide pokeball

        narrator "You gained [ballsgained] Poké Balls! They're covered in cookie crumbs..."

        red @happy "Thanks."

        redmind @thinking "Alright. Time to catch some new Pokémon. Since I can only keep six on me at a time, and I don't have anywhere to store my extras yet, I should be careful about filling up my party."
        redmind @thinking "I might be stuck with the same six Pokémon for a while, if I fill my party up now, and {color=#0048ff}you never know when a strong or rare Pokémon will show up.{/color}"

    elif (ballsused == 20):
        brendan surprised "...Crap, man. I just realized. I don't actually have any. I used 'em all up on Saturday."

        red @surprised "...Oh."

        pause 2.0

        red @happy "Well, that's embarrassing. But we can at least look around the fields, see what's there for when we {i}do{/i} have Poké Balls!"

        brendan @sad "Yeah... I guess..."

else:
    redmind @thinking "Alright. Time to catch some new Pokémon. Since I can only keep six on me at a time, and I don't have anywhere to store my extras yet, I should be careful about filling up my party."
    redmind @thinking "I might be stuck with the same six Pokémon for a while, if I fill my party up now, and {color=#0048ff}you never know when a strong or rare Pokémon will show up.{/color}"

$ wildcount = 0

call wildarea("fields") from _call_wildarea_2

show fields2 with Dissolve(2.0)

pause 2.0

hide fields1

show brendan happy at rightside with dis
show skyla happy at leftside with dis

narrator "You eventually find your way back to Brendan, who is deep in conversation with another student."

brendan -happy @talking2mouth "No shit? That's amazing, man! Or, uh, wo-man!"

skyla -happy @talkingmouth "Well, it needed to be done, right? And I was in the right place, at the right time, and had enough time to do it."

$ wasnamed = persondex["Skyla"]["Named"]

if (wasnamed):
    redmind @thinking "Huh. Skyla and Brendan? Weird to see my friend groups intersect like this." 
    redmind @happy "I like it, though! That just means I have enough friends to have multiple friend groups."

red @talkingmouth "Hey!"

brendan @happy "[first_name]! Hey there. I just met this chick on the other side of the hill over there, and I knew I {i}had{/i} to talk with her!"

redmind @confusedeyebrows frownmouth "Right... does that have anything to do with her outfit?"

if (wasnamed):
    redmind @thinking "It's... kinda different from what I'm used to seeing Skyla wearing..."

    skyla @talkingmouth "Hey, [first_name]! Good to see you again."

else:
    $ BecomeNamed("Skyla")
    skyla @talkingmouth "Hey! I'm Skyla. Brendan here said your name was [first_name]? Nice to meet you!"

    red @talkingmouth "Same."

skyla @happy "So, you guys are going on an early-morning run and Pokémon-catching spree, huh? Get anything good?"

$ monscaught = len(playerparty) - 2
if (monscaught == 1):
    red @talking2mouth "Yeah, I got one."
elif (monscaught == 2 or monscaught == 3):
    red @talkingmouth "Just a couple."
elif (monscaught == 4):
    red @happy "Filled up my entire party, actually. I've got six on hand right now."

    brendan @surprised "Bro, for real? That's insane. You're going to try and teach five new Pokémon, all at once? Crazy."

    red @closedbrow talking2mouth "Maybe more, if I can find somewhere to store these guys..."
else:
    red @closedbrow talking2mouth "Not this time."

if (HasEvent("Brendan", "CaughtSandshrew")):
    brendan @talking2mouth "I didn't get anything."

brendan @closedbrow talkingmouth "I was kinda hoping I'd catch somethin' else, but there's always next time, I guess."

red @talkingmouth "Yeah. So what're you doing? Running?"

skyla @surprised sweat "Oh, I'm scoping out the land for a runway. The fields here are perfect for one."

if (not wasnamed):
    red @confusedeyebrows talkingmouth "A runway? What, are you a pilot?"

    brendan @happy "Bro, that's the crazy thing--she actually {i}is!{/i}"

    red @surprised "Woah! I thought you needed to be, like, twenty-five to get a pilot's license?"

    skyla @talkingmouth "In Unova, where I come from, you only need to be seventeen. And in Kobukan, you only need to be eighteen, so it's still legal!"

red @talkingmouth "So you're planning on setting up your own little runway here?"

skyla @winkbrow happymouth "Yeah. Might take a couple months to get the area zoned out and approved by the Kobukan Air Authority, but I should be able to take people to other regions soon."

red @happy "Sick! What inspired this?"

skyla @angry "Well, {i}currently{/i}, my plane is stored at the airport in Inspira. So I need to take a bus over there every time I want to fly, and they're charging me through the nose to keep it there, too."

red @confusedeyebrows talking2mouth "Then, uh... won't they have a vested interest in not letting you build your runway here?"

skyla @closedbrow talkingmouth "Yeah, probably. But I don't answer to them, I answer to the KAA. And if they say--"

$ PlaySound("pokemon/cries/359.mp3")

show brendan surprisedbrow frownmouth
show skyla surprisedbrow frownmouth
with dis

pause 2.0

stop music fadeout 1.5

queue music "audio/music/reliccastle_start.ogg" fadein 3.0
queue music "audio/music/reliccastle_loop.ogg"

red @confused "What was that?"

skyla -surprisedbrow -frownmouth -surprised @closedbrow talking2mouth "Hm... I don't see anything..."

brendan -surprisedbrow -frownmouth -surprised sadbrow frownmouth @talking2mouth "Oh, man, that's an Absol. They're from Hoenn, and they're bad news."

skyla @surprised "Bad news? How can a Pokémon be bad news?"

brendan @talking2mouth "They only show up when something {i}real{/i} bad is about to happen. Normally they stay up in their mountains, so if one's close enough for us to hear, we might be in trouble."

skyla @talkingmouth "...Are Absol black and white, with long, bladed tails and a single horn?"

brendan -sadbrow -frownmouth @surprised "Yeah! Why?"

skyla @talkingmouth "There's one on the top of that hill, and it's running at us at full speed."

stop music fadeout 5.0

show absol:
    zoom 0.05 align (0.35, 0.17) alpha 0.0
    parallel:
        linear 10.0 align (0.35, 0.37)
    parallel:
        ease 2.0 alpha 1.0
        pause 6.0
        ease 1.0 alpha 0.0

pause 5.0

skyla @sweat sadbrow happymouth "Well, y'know, full speed is relative... But it {i}is{/i} getting closer!"

red @talkingmouth "Uh... should we do something while we're waiting for it to show up, or...?"

brendan @happy "Well, I've got some potions, in case your team needs 'em."

$ HealParty()

pause 2.0

skyla @winkbrow happymouth "So... you guys come here often?"

queue music "audio/music/reliccastle_loop.ogg"

show absol:
    zoom 0.05 align (0.35, 0.37) alpha 0.0
    ease 0.5 zoom 2.0 align (0.5, 0.5) alpha 1.0

show brendan surprisedbrow frownmouth
show skyla surprisedbrow frownmouth
with vpunch

red @surprised "Shit!"

hide absol with dis

python: 
    absolobj = Pokemon(359, level=28, moves=[GetMove("Double Team"), GetMove("Quick Attack"), GetMove("Night Slash"), GetMove("Swords Dance")], frenzynerf=(10, ["Pursuit", "Quick Attack", "Leer", "Scratch"]), shinylock=False)

    absolobj.ApplyStatus("frenzied")

    trainer1 = Trainer("red", TrainerType.Player, playerparty)
    trainer2 = MakeTrainer("Brendan", TrainerType.Ally)
    trainer3 = MakeTrainer("Skyla", TrainerType.Ally)
    sidemonnum = 359
    trainer4 = Trainer("sideportraitfull", TrainerType.Enemy, [absolobj], number=3, isPokemon=True)

$ HealParty(trainer2)
$ HealParty(trainer3)
call Battle([trainer1, trainer2, trainer3, trainer4], healParty = False, specialmusic="Nothing") from _call_Battle_14
$ battlehistory["Absol1"]  = _return

stop music
queue music "audio/music/fieldstheme_start.ogg"
queue music "audio/music/fieldstheme_loop.ogg"

show brendan surprisedbrow frownmouth at rightside
show skyla surprisedbrow frownmouth at leftside
with dis

if (absolobj in playerparty):
    $ absolobj.Level = 10
    $ absolobj.Moves =[GetMove("Pursuit"), GetMove("Quick Attack"), GetMove("Leer"), GetMove("Scratch")]
    $ absolobj.Experience = absolobj.CalculateAllExperienceNeededForLevel(10)
    $ absolobj.RecalculateStats()
    
    brendan @surprised "Woah! Look at that, [first_name]! The Absol totally calmed down."
    skyla @surprised "I'm surprised, [first_name]! You're kinda crazy-good at battling, huh? Are you sure you just started out?"

    $ ValueChange("Skyla", 2, 0.25, pausing=False)
    $ ValueChange("Brendan", 2, 0.75)

    red @closedbrow talking2mouth "Pretty sure, yeah. Besides, looks like it's not actually as powerful as we thought... I guess it was just {i}really{/i} upset."

elif ((trainer1.HasMons() or trainer2.HasMons() or trainer3.HasMons()) and absolobj.GetHealthPercentage() <= 0):
    brendan @surprised "Ah, geez, that was tough! We just barely beat it off..."
    skyla @surprised "I'm surprised, [first_name]! You're pretty good at battling, huh? Are you sure you just started out?"

    $ ValueChange("Skyla", 1, 0.25, pausing=False)
    $ ValueChange("Brendan", 1, 0.75)

    red @closedbrow talking2mouth "Pretty sure, yeah."

elif ((trainer1.HasMons() or trainer2.HasMons() or trainer3.HasMons()) and absolobj.GetHealthPercentage() > 0):
    brendan @surprised "Ugh, that thing was too tough. Good thing we got out of there when we did."
    skyla @angry "Heroes of justice aren't supposed to run from the bad guy! That was lousy."

    $ ValueChange("Skyla", -1, 0.25, pausing=False)
    $ ValueChange("Brendan", 1, 0.75)

else:
    brendan @surprised "What the heck? This thing kicked all our asses, and just ran off? Geez..."
    skyla @angry "Ugh. What a lousy battle. I totally messed that up..."

    $ ValueChange("Skyla", -1, 0.25, pausing=False)
    $ ValueChange("Brendan", -1, 0.75)

brendan -surprisedbrow -frownmouth -surprised @closedbrow talkingmouth "It's weird, though. Absol're bad luck, everyone knows that, but normally they're pretty calm. Wonder what got this one so riled up?"

red @closedbrow talking2mouth "Who could say? Maybe its habitat was disturbed by something? Or--"

$ PlaySound("idea.ogg")

skyla @talking2mouth "Or the meteor?"

show brendan surprisedbrow frownmouth with dis

red @surprised "Huh?"

skyla @angrybrow talkingmouth "Uh... meteor. Right there."

$ PlaySound("asteroidwoosh.ogg")

show meteor behind fields2: 
    alpha 0.0 xanchor 0.0 yanchor 1.0 xpos 1.0 ypos 0.0 zoom 0.05 rotate 45
    parallel:
        linear 0.4 alpha 1.0
    parallel:
        linear 2.0 xpos -0.4 ypos 0.6 zoom 1.0

show fields2:
    ease 0.05 ypos 1.0
    pause 0.05
    ease 0.05 ypos 1.1
    repeat

red @surprised "WHA--"

brendan @talking2mouth "Not again!"

show brendan:
    ease 0.25 xpos 0.85 rotate 90 ypos 1.5

show skyla:
    ease 0.25 xpos 0.15 rotate -90 ypos 1.5

$ PlaySound("impact.ogg")

show fields2:
    ease 0.05 ypos 1.2
    pause 0.05
    ease 0.05 ypos 1.0
    ease 0.05 ypos 1.1
    pause 0.05
    ease 0.05 ypos 1.0
    ease 0.05 ypos 1.05
    pause 0.05
    ease 0.05 ypos 1.0
    ease 0.05 ypos 1.025
    pause 0.05
    ease 0.05 ypos 1.0
    ease 0.05 ypos 1.0125
    pause 0.05
    ease 0.05 ypos 1.0

pause 2.0

red @closedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

red @closedbrow talking2mouth "Anyone dead?"

show brendan:
    ease 2.0 xpos 0.75 rotate 0 ypos 1.0

show skyla:
    ease 1.2 xpos 0.25 rotate 0 ypos 1.0

brendan sadbrow frownmouth @talking2mouth "Not me, man."

skyla -surprisedbrow -frownmouth -surprised @happy "We {i}need{/i} to investigate that!"

brendan @talking2mouth "I dunno. Meteors are nasty business, y'know? We should probably get a Professor. And homeroom's soon..."

skyla @angrybrow happymouth "But what if it's an alien invader?! Then we have a duty to vanquish it!"

brendan @angrybrow talking2mouth "Alien invaders aren't our problem. I mean, we're not even legal trainers yet."

skyla @happy "Well, what do you think, [first_name]?"

pause 2.0

skyla surprisedbrow frownmouth @surprised "Uh... where'd he go?"

brendan @talking2mouth "Dude's already halfway to the impact site... guess we're going, then."

skyla -surprisedbrow -frownmouth -surprised @winkbrow happymouth "Well, hey, if you want to run back and get a Professor, be my guest. {i}I'm{/i} going!"

show skyla:
    ease 0.5 xpos -0.5

brendan @talking2mouth "Man... I really can't afford to be late to class..."

show brendan:
    ease 1.5 xpos -0.5

show blank2 with Dissolve(3.0)

stop music fadeout 1.5
queue music "Audio/Music/SoaringIllusions_Intro.ogg" noloop
queue music "Audio/Music/SoaringIllusions.ogg"

narrator "You make your way to the impact zone, sprinting and jumping over fallen trees and large gouges in the dirt as you do so."
narrator "When you arrive, however, you see no traces of the meteor. Rather..."

show venetiaintro with dis:
    zoom 2.0
    parallel:
        ease 2.0 xpos -0.5
        ease 2.0 xpos 0.0 ypos -0.5
        ease 2.0 xpos -0.3 ypos -0.3
        ease 2.0 xpos 0.0 ypos 0.0
    parallel:
        ease 10.0 zoom 1.0

pause 13.0

red @surprised "Oh, shit. Did the meteor hit someone?!"

hide blank2
hide brendan
hide skyla

red @surprised "Hey, hey, you! Are you alright? Hold on, I'll call someone to come help!"
red @closedbrow talking2mouth "Wait... what's the number for an ambulance in Kobukan? It's not 119, like in Kanto... is it 999? Like in Galar?"
red @surprised "Shit, I could look this up, if I just..."

skyla @happy "Wow, [first_name], you're fast! What's--"
skyla @surprised "Oh, no! What happened? Did the meteor hit her?"
red @surprised "I don't know! That's what I thought, so maybe?"

brendan @closedbrow talkingmouth "Hey, I caught up. What's--"
brendan @surprised "Holy shit! Did the meteor hit that girl?"

red @angry "I don't know! Nobody knows if the meteor hit her! What's the number for an ambulance in Kobukan?"

skyla @angry "What? No, don't call an ambulance! You want to bankrupt that poor girl, right after she got hit by a meteor?"

red @surprised "B-bankrupt?"

skyla @talkingmouth "Yeah, don't you know how much they charge for ambulances in this region?"

brendan @surprised "You have to {i}pay for an ambulance{/i}?!"

red @talking2mouth "Well, how else are we going to get her to a hospital?! We can't {i}fly{/i} her!"

skyla @closedbrow talking2mouth "I think I saw a helicopter in Inspira... if I hitched a ride to the city, I might be able to steal it..."

red @angry "Why do you think this is a better plan than just calling a damn ambulance?!"

show venetiaintrobg with dis

narrator "While you and your friends are panicking, you don't notice that the girl has clawed her way out of the crater, and..."

tia sadeyebrows sadeyes frownmouth "[ellipses]"

show tia behind venetiaintrobg

hide venetiaintro with dis

show venetiaintrobg with vpunch

"{color=#cf0000}[first_name]{/color} & {color=#db4039}Brendan{/color} & {color=#5c87b9}Skyla{/color}" "\"Ahhh!\""

hide venetiaintrobg with dis

red @talking2mouth "Are you okay?"

show tia -frownmouth with dis

narrator "The girl ponders for a moment, then slowly touches her fingertips together, in the universal 'ok' gesture."

red @talkingmouth "So the meteor didn't hit you?"

show tia closedeyes with dis

narrator "The girl shakes her head."

red @confusedeyebrows talking2mouth "Damn. Then how did you end up in that crater?"

show tia surprisedbrow frownmouth with dis

narrator "The girl's eyes go wide, and her hands begin moving in unfamiliar, but intentional, patterns."

show brendan at rightside 
show skyla at leftside
with dis

red @closedbrow talking2mouth "Uh... anyone?"

skyla @sad "Oh, I think I know what's happening here..."

skyla @sadbrow happymouth "Hey, sweetie. Can you, um... speak?"

show tia closedeyes -surprisedbrow -frownmouth -surprised with dis

narrator "The girl shakes her head."

brendan @talking2mouth "Damn. Imagine not being able to speak, {i}and{/i} gettin' hit by a meteor. That's double-unlucky."

show tia angryeyes angryeyebrows poutmouth with dis

red @talking2mouth "Well, she wasn't {i}actually{/i} hit by the meteor, remember." 
red @closedbrow talking2mouth "Wait... where is it?"

brendan @talking2mouth "Most meteors vaporize before they hit the ground, and those that don't usually vaporize on impact."
brendan @closedbrow talkingmouth "Maybe the meteor hit, vaporized, and then she fell in the crater?"

show tia closedeyes with dis

narrator "The girl shakes her head emphatically, and begins signing again, more insistently."

red @sadeyes sadeyebrows talking2mouth "I'm really sorry. None of us know how to sign. But, if you're really okay, I'm sure there's someone at the academy who knows."

show tia sadeyebrows sadeyes tears frownmouth with dis

narrator "The girl seems to calm down significantly, though she still looks distressed."

red @talkingmouth "We'll bring you back to the academy, find someone who can translate for you, then if you need it, we'll bring you to a hospital, okay?"

show tia -tears -frownmouth with dis

narrator "The girl slowly nods her head."

red @closedbrow talking2mouth "Alright. Uh... let's head back to the school. Brendan, I know you want to get back to homeroom, so you don't need to stick around for this."

brendan @sadbrow happymouth "Are you sure, man?"

red @closedbrow talking2mouth "Yeah, it's fine. Go on back to homeroom. I'll call you if something comes up."

brendan @talking2mouth "Alright. Thanks a bunch."

show brendan:
    ease 0.5 xpos 1.5

show tia:
    ease 0.5 xpos 0.75

red @talking2mouth "Alright, Skyla, and, um...{w=0.5} you...{w=0.5}{nw}"
extend @sadeyes sadeyebrows happymouth " sorry, I'm not sure what to call you. Damn, I don't suppose you have a pencil and paper on you?"

show tia happymouth with dis

narrator "The girl shakes her head."

show tia -happymouth with dis

red @closedbrow talking2mouth "Right... And Skyla, you obviously don't, either."

skyla @talkingmouth "What do you mean?"

red @talkingmouth "Well, your outfit, uh... it's..."

redmind @thinking "Does this girl seriously not see it? What do I even say here? 'It's completely skintight, and kinda shows off everything?'"

red @talking2mouth "...It doesn't have pockets."

skyla @happy "Oh, gotcha!"

red @talkingmouth "Anyway, let's all head back to the school. Come with me."

show tia:
    ease 0.5 xpos 0.85 alpha 0.0 zoom 1.3 ypos 1.2

show skyla surprisedbrow frownmouth with dis

narrator "Without warning, the new girl obediently walks next to you and grabs your hand."

pause 2.0

red @surprised "Oh. Okay."

skyla -surprisedbrow -frownmouth @winkbrow smirkmouth "Well, that's a neat trick."

red @wince talking2mouth "I swear I didn't do it on purpose."

redmind @thinking "What is this? Frienergy on steroids?"

redmind @thinking "...No, I can't keep attributing {i}everyone{/i}'s behavior to Frienergy. She's probably just scared, and wants someone to hold onto."

pause 2.0

redmind @thinking "...Though she didn't grab {i}Skyla's{/i} hand..."

show blank2 with Dissolve(2.0)

narrator "You make your way back to the Academy, the mysterious girl's surprisingly-cold hand clamped tightly around yours the whole way."
narrator "You take her to Professor Oak's lab, reasoning that you can wait for him there until homeroom is over. Skyla, meanwhile, goes to her homeroom with Professor Sycamore."

scene research 
show tia
with Dissolve(2.0) 

red @talkingmouth "So. We've got paper here. What's your name?"

narrator "The girl, in quick and messy handwriting, writes 'Venetia. But I go by Tia.'"

$ BecomeNamed("Tia")
red @talkingmouth "Venetia, huh? That doesn't sound like a Kobukanian name. Or a Kantonian one, come to think of it."

tia @happy "It's not! I'm new to the region."

red @talkingmouth "Are you a student here? That would explain how you ended up in the fields..."

tia concernedeyebrows sadeyes frownmouth "No, I'm just{w=0.5}{nw}"
tia "{s}N{/s}o, I'm just{fast}{w=0.02}{nw}"
tia "{s}No{/s}, I'm just{fast}{w=0.02}{nw}"
tia "{s}No,{/s} I'm just{fast}{w=0.02}{nw}"
tia "{s}No, {/s}I'm just{fast}{w=0.02}{nw}"
tia "{s}No, I{/s}'m just{fast}{w=0.02}{nw}"
tia "{s}No, I'{/s}m just{fast}{w=0.02}{nw}"
tia "{s}No, I'm{/s} just{fast}{w=0.02}{nw}"
tia "{s}No, I'm {/s}just{fast}{w=0.02}{nw}"
tia "{s}No, I'm j{/s}ust{fast}{w=0.02}{nw}"
tia "{s}No, I'm ju{/s}st{fast}{w=0.02}{nw}"
tia "{s}No, I'm jus{/s}t{fast}{w=0.02}{nw}"
tia "{s}No, I'm just{/s}{fast} Yes."

red @confused "...Are you sure?"

tia poutmouth "Yes!{w=0.5}{nw}"
tia "{s}Y{/s}es!{fast}{w=0.02}{nw}"
tia "{s}Ye{/s}s!{fast}{w=0.02}{nw}"
tia "{s}Yes{/s}!{fast}{w=0.02}{nw}"
tia "{s}Yes!{/s}{fast}{w=1.0} No.{w=1.0}{nw}"
tia "{s}Yes!{/s} {s}N{/s}o.{fast}{w=0.02}{nw}"
tia "{s}Yes!{/s} {s}No{/s}.{fast}{w=0.02}{nw}"
tia "{s}Yes!{/s} {s}No.{/s}{fast}{w=2.0} Yes."

redmind frownmouth "Hm. Now might not be the time to push for more details. Maybe she's a bit dazed from her fall."

show oak surprisedbrow frownmouth at leftside 
show tia -poutmouth -concernedeyebrows -sadeyes
with dis

show tia surprisedbrow frownmouth:
    ease 0.5 xpos 0.75

oak @talking2mouth "Lad?! What on earth happened? And who's this?"

show tia -surprisedbrow -frownmouth -surprised with dis

red @talkingmouth "Well, um... I was out in the field this morning, when a couple friends and I saw what looked like a meteor crash into the fields." 
red @closedbrow talking2mouth "When we arrived at the impact zone, there weren't any traces of the meteor, but this girl was in the crater."

oak -surprisedbrow -frownmouth -surprised @talkingmouth "Oh? Are you alright?"

show oak surprisedbrow frownmouth with dis

narrator "Tia quickly begins signing at Professor Oak at rapid speed."

pause 2.0

oak -surprisedbrow -frownmouth -surprised @sadeyes sadeyebrows sadmouth "Er... apologies, but this method of communication utterly escapes me."

red @talkingmouth "Hold on, she's got a pad of paper, and a pen here."

show tia poutmouth angryeyebrows angryeyes with dis

narrator "Tia purses her lips, but begins writing on her paper, impatiently."

$ autoquote = False

tia "<I'm fine. I'm"

narrator "Tia takes a quick glance at you."

show tia sadeyes sadeyebrows frownmouth with dis

$ autoquote = True

tia "I'm fine. I'm{fast}{w=0.5} a student here."

oak happy "Ah! Well, that's good to hear. Seems you're right where you need to be, then. Though a check-up at the hospital probably wouldn't be remiss."

show tia surprisedbrow frownmouth with dis

oak -happy @closedbrow talking2mouth "Who's your homeroom teacher? Though there's no attendance, they might be worried about you."

narrator "Tia looks at you, helplessly."

redmind @surprised "What? Uh... I don't know what to say here. I mean, I can't lie..."

pause 2.0

show tia happy with dis

red @sadeyes sadeyebrows happymouth "Hey, uh, Sam. What do you think about Professor Cherry?"

show tia -happy with dis

oak surprisedbrow frownmouth @surprised "Eh? Cherry? Well, she's a decent enough Professor, I suppose. Startlingly young. But that's certainly nothing I hold against her."

oak @closedbrow talking2mouth "Actually, I keep meaning to have a good sit-down conversation with her, but her schedule is so full, I can rarely find time to talk to her."

oak -surprised @talkingmouth "Anyway, miss, your homeroom teacher?"

tia -surprisedbrow -frownmouth -surprised @happy "Professor Cherry."

oak @talkingmouth "Oh, is that right? Well, perhaps you can just tell her to call me if she needs any confirmation of your story. Tracking that woman down outside of her homeroom is utterly impossible."

pause 1.0

oak @closedbrow talking2mouth "Ah, excuse me. I don't believe I caught your name. Refresh me?"

show tia surprisedbrow frownmouth with dis

narrator "Tia sneaks another furtive glance at you."

show tia sadeyes sadeyebrows with dis

tia "{w=0.5}Bianca{w=0.5} Vongole."

redmind @thinking "...Huh. So, she's trying to hide her identity, huh?"
redmind @thinking "I should probably tell Sam about this, but..."

pause 1.0

redmind @thinking "The way she grabbed my hand, earlier. I think she's afraid--like she's running from someone. Or something."
redmind @thinking "Until I know why she's hiding herself, I probably shouldn't stop her for no reason."

pause 1.0

oak @happy "Well, you should both run back to your rooms and get changed! If you hurry now, you should be able to get into your uniforms before your first elective!"

red @happy "Right. Thanks, Sam."

scene lobby 
show tia
with Dissolve(2.0)

red @talkingmouth "Hey. Be real with me. You aren't a student here, are you?"

show tia frownmouth with dis

narrator "Tia, having left her paper back in Professor Oak's lab, shakes her head."

red @talkingmouth "It's fine. But you're going to need a room, and you'll need an ID card to get into the cafeteria, and most of the buildings. And someone's going to realize that 'Bianca Vongole' isn't a student here."

show tia surprisedbrow frownmouth with dis

narrator "Tia quickly digs into her skirt and pulls out an ID card. Though the name says 'Bianca Vongole,' the picture is unmistakably the woman standing in front of you."

show tia happy with dis

red @surprised "Huh. Plot twist."

show tia -happy -frownmouth with dis
 
red @closedbrow talking2mouth "So, you actually {i}are{/i} Bianca?"

narrator "Tia shakes her head."

red @confusedeyebrows talking2mouth "But you look exactly like her."

narrator "Tia nods."

red @closedbrow talking2mouth "And you have her ID card."

narrator "Tia nods."

red @closedbrow talking2mouth "Did you steal it?"

show tia surprisedeyes surprisedeyebrows poutmouth with dis

narrator "Tia seems offended, and shakes her head emphatically."

red @talking2mouth "So you must be Bianca, right?"

show tia happy with dis

narrator "Tia shakes her head."

red @confusedeyebrows talking2mouth "Then what's the deal?"

show tia closedeyes angryeyebrows poutmouth with dis

narrator "Tia begins signing with great gusto at you. All you can do is watch helplessly."

pause 2.0

red @talkingmouth "Here, take my phone. Just type out a message there."

show tia surprisedbrow frownmouth with dis

narrator "Tia takes your phone with wide-eyed bewilderment, jumping a little when the electric screen flashes on. She examines it from every angle before slowly typing a message."

tia "I{w=1.0} c{w=1.0}o{w=1.0}"

narrator "Tia types so slowly and deliberately, that you quickly realize you're going to run out of time before your first elective."
narrator "It truly seems like she has never used a phone before."

red @sadeyes sadeyebrows happymouth "Hey, y'know what? It'll probably be faster for us to just find an interpreter. But I've gotta go to my elective now, and you need to go too... apparently."

show tia angryeyes angryeyebrows poutmouth with dis

pause 0.5

red @sadbrow talkingmouth "Hey, c'mon. What's with the sad face?"

show tia sadeyes sadeyebrows tears frownmouth with dis

pause 0.5

red @happy "I'm not ditching you, honest! I'll find you during lunch. Would that work?"

narrator "Tia continues to stare at you, pleadingly."

red @sad "...I'm sorry, I don't know what you want."

narrator "Tia signs at you aggressively, to no avail."

red @closedbrow talking2mouth "...Do you know how to sign up for electives? If this is your first day, and you weren't around for the opening weekend, you must've missed that, right?"

show tia -tears happy with dis

narrator "Tia nods, enthusiastically, her mood seemingly instantly improved."

show blank2:
    alpha 0.0
    ease 3.0 alpha 1.0

red @happy "Alright. Now we're getting somewhere. I guess you don't have a phone, so you can use one of the computers in the library to lock in your elective selection. Just follow me..."

$ playerparty.remove(pikachuobj)

narrator "After teaching Tia how to sign up for classes, you go back to your dorm, get changed, and run to your first elective at a breakneck speed."

call clearscreens from _call_clearscreens_53
$ renpy.music.stop(channel='crowd', fadeout=1.5)
stop music fadeout 1.5
$ renpy.pause(2.5, hard=True)

jump PickElective
