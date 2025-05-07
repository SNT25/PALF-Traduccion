label day010417:

$ timeOfDay = "Morning"
call calendar(1) from _call_calendar_12
$ calDate = calDate.replace(day=17, month=4, year=2004)

show blank2
stop music fadeout 1.5
queue music "Audio/Music/Show Me Around.ogg"
show morning at vspaz

pause 3.5

$ renpy.transition(dissolve)
show screen currentdate

scene relichall_A with Dissolve(2.0)

hide morning    
hide blank2

show leaf at centerside with dis

leaf @happy "Gooood morning, campers! Ready for a fun-filled day of exploring the city?"

pause 2.0

leaf @sarcastic "...Where the hell is everybody?"

whitney @surprised "{cps=20}{size=26}W{/size}{size=28}W{/size}{size=30}W{/size}{size=32}A{/size}{size=34}A{/size}{size=36}AA{/size}{size=38}AA{/size}{size=40}AI{/size}{size=42}I{/size}{size=38}I{/size}{size=46}I{/size}{size=48}I{/size}{size=50}T{/size}{size=52}T!!{/size}{/cps}"

show whitney surprisedbrow frownmouth:
    xpos -0.5 rotate -45 ypos 1.0
    ease 0.8 rotate 0 xpos 0.8 ypos 1.1
    pause 1.0 
    ease 0.3 ypos 1.0

pause 0.5

whitney @talking2mouth "Sorry I'm late!" 
whitney -surprisedbrow -frownmouth -surprised @happy "Tia actually let us sleep last night, so I ended up catching up on three days' worth of beauty rest."

leaf @happy "And Flannery? Can't fulfill your promise to take her shopping without her, you know!"

show flannery tired behind whitney:
    xpos -0.5 ypos 1.0
    ease 2.0 xpos 0.1
    pause 1.0
    ease 0.8 xpos 0.2
    pause 1.0
    ease 0.8 xpos 0.4
    pause 1.0
    ease 0.8 xpos 0.6

pause 3.0

flannery @tiredbrow talking2mouth "I... {w=0.5}hate... {w=0.5}mornings..."

leaf surprisedbrow frownmouth @surprised "Geez, you're not looking so good, Flan. Do you want some coffee?"

show whitney winkeyes sadeyebrows sweat frownmouth with dis

red @surprised "Oh, I wouldn't... ah, too late."

show flannery:
    ease 0.5 xpos 0.25

show leaf sadbrow with dis

flannery angry "What're you trying to say, huh? You think I need your {i}charity?{/i} Am I not living up to your {i}standards{/i}, so you're going to {i}fix{/i} me?!"

show leaf behind whitney:
    xpos 0.5
    ease 1.5 xpos 0.55

leaf @sad "Wha...? N-no, I was just..."

show flannery:
    ease 0.5 xpos 0.35

flannery furious "How about you {i}take{/i} that coffee of yours, and shove it right up your--"

show whitney with vpunch:
    ease 0.2 xpos 0.5

show flannery surprisedbrow frownmouth with dis:
    ease 0.4 xpos 0.25

show leaf:
    ease 0.5 xpos 0.75

whitney -sweat -winkeyes -sadeyebrows frownmouth @angry "Flan! Chill out! You're going to ruin a fun day if you can't keep your morning temper under control!"

pause 1.0

flannery @frownmouth "[ellipses]"

show leaf -sadbrow frownmouth with dis

flannery @sad "I... yeah. Sorry. I just woke up, and... I know that's not an excuse, but..."

flannery -surprisedbrow @closedbrow talking2mouth "Sorry."

red @happy "Don't worry about it. No-one likes mornings. But it's better than sleeping the day away. Right, buddy?"

$ renpy.music.play("Audio/Pokemon/pikachu_angry1.ogg", channel="altcry", loop=None)
pikachu angry_2 "Pika!"

red @closedbrow talking2mouth "Maybe I should get {i}him{/i} some coffee for the mornings..."

flannery tiredbrow tiredmouth "Mm."
flannery @talking2mouth "Hey, where'd Tia go?"

whitney @surprised "What? I thought she was behind with you!"

flannery @surprised "Why?! The girl's fast as a jet plane! I figured she ran ahead with you!"

leaf -frownmouth @talkingmouth "Can't you two just call her?"

flannery @talking2mouth "She's already a nightmare just with a laptop. You think we're going to give her a phone?"

red @surprised "Wait, you just {i}bought{/i} her a laptop?"

whitney @happy "She needed it for class! Besides, I'm sure she'll pay us back eventually."

redmind @thinking "I keep forgetting this school is full of crazy-rich people..."

stop music fadeout 2.0

show tia with Dissolve(1.0):
    xpos 1112 ypos 258 zoom .01

pause 0.5

red @talking2mouth "Wait... wait a minute."

queue music "audio/music/reliccastle_start.ogg" fadein 3.0
queue music "audio/music/reliccastle_loop.ogg"

show leaf surprisedbrow frownmouth:
    ease 2.0 xpos 0.76
show whitney surprisedbrow frownmouth:
    ease 2.0 xpos .49
show flannery surprisedbrow frownmouth:
    ease 2.0 xpos .24
with dis

show tia:
    ease 1.0 xpos 1112 ypos 263 zoom .01

show relichall_A with vpunch

red @surprised "Wait... {i}NO!{/i} NO, DON'T!"

leaf @sad "[first_name], what're you doing--?"

show leaf surprisedbrow frownmouth:
    ease 0.4 xpos 1.5
show whitney surprisedbrow frownmouth:
    ease 0.4 xpos -0.5
show flannery surprisedbrow frownmouth:
    ease 0.4 xpos -0.5

show relichall_A behind tia:
    align (0.5, 0.5)
    ease 0.4 zoom 1.5

show tia:
    ease 0.4 xpos 1200 ypos 140 zoom .015

show flashback with dis

narrator "Before your body is consciously aware of it, you push past your friends and begin a mad sprint towards the academy building, hoping, somehow, that you'll reach the bottom before Tia does."

stop music

show tia neutralpowered with dis:
    alpha 1.0
    ease 0.5 xpos 1240 ypos 110
    linear 0.03 xpos 1243
    parallel:
        ease 2.0 xpos 1330 ypos 1080
    parallel:
        ease 1.0 alpha 0.0

pause 3.0

hide flashback with Dissolve(2.0) 

narrator "You do not."

hide tia

red @surprised "N-no. What... no? She didn't just..."

play music "audio/music/show me around.ogg"

show tia happy:
    xpos 1.5 
    ease 1.0 xpos 0.6

pause 2.0

show tia surprisedbrow frownmouth with dis

red @surprised "Wh-WHAT?! How! I just saw you jump! And, I mean, I'm glad you're alive, but how did you...? How could you have...?"

show tia happy with dis

narrator "Tia happily signs at you."

if (persondex["Tia"]["Value"] > 4):
    narrator "From what little of sign language you've managed to pick up since Tuesday, you could have sworn she just signed 'I can fly.'" 
    narrator "Clearly, you need to study JSL more."
else:
    narrator "You have no idea what she's saying, of course."

show relichall_A:
    ease 2.0 zoom 1.0

show leaf surprisedbrow frownmouth:
    ease 1.0 xpos 0.8
show whitney surprisedbrow frownmouth:
    ease 1.0 xpos 0.4
show flannery surprisedbrow frownmouth:
    ease 1.0 xpos 0.2

leaf @talking2mouth "[first_name], geez, you run too fast... What the hell happened? You look like you saw a ghost."

whitney -surprisedbrow -frownmouth -surprised frownmouth @angry "Yeah! You knocked me over!"

redmind @surprised "None of them saw her jump? But... but she..."

show leaf -surprisedbrow -frownmouth -surprised with dis

flannery tiredbrow tiredmouth @talking2mouth "Way too early in the morning for this, dude. You don't yell like that unless someone's about to die."

tia "C'mon! Let's go shopping! I've never been to a department store before."

red @surprised "B-but... she... you..."

show tia:
    ease 1.5 xpos 1.5

show flannery:
    ease 2.0 xpos 1.5

show whitney:
    ease 3.0 xpos 1.5

show leaf:
    ease 4.0 xpos 1.5
    ease 1.0 xpos 0.8

pause 5.0

leaf @sarcastic "Well?"

red @sad "Well what?"

leaf @talking2mouth "I know you well enough now to know when something scared the shit out of you. What happened?"

red @closedbrow talking2mouth "...You wouldn't believe me."

leaf @sarcastic "Probably not, but you'll explode if you don't tell {i}someone{/i}, so lay it on me, skippy."

pause 2.0

show leaf surprisedbrow frownmouth with dis

red @sad "I thought I saw Tia jump off the roof."

pause 2.0

leaf -surprisedbrow -frownmouth -surprised @talking2mouth "Well, shit, I don't know how to help you with that one. I thought you were going to say something like 'my girlfriends were about to meet.'"

red @talking2mouth "Yeah, well, if they did, they would have known about each other beforehand. I'm not a dick."

leaf @closedbrow talkingmouth "Jury's out on that one. But about Tia... I mean, obviously, she's fine, right? So either she can jump off of buildings and be okay, or you didn't see her."

red @closedbrow talking2mouth "I guess. I {i}really{/i} feel like it was the first one, though."

leaf @talking2mouth "Maybe just ask her about it. Girl follows you around like a Rockruff, anyway, she'd probably tell you if you asked straight-up."
leaf @closedbrow talkingmouth "Oh, I guess you'd need to learn some more sign first, though, if you don't want to go through Whitney."

red @sadeyes sadeyebrows talkingmouth "Man, my schedule is already so full..."

leaf @happy "That's what happens when you embed yourself into the business of literally every person you meet. You might want to show a little discretion."

red @confusedeyebrows talking2mouth "Queen Leaf of her eternal smugness is lecturing {i}me{/i} on discretion?"

leaf @angry "Hey! That's Queen Leaf III, praise unto her, to you, {i}peasant!{/i}"

red @happy "Apologies, your majestyness. I didn't get no good schoolin', and me royal forms of address be a bit shape-ship."

leaf @flirttalk "Your Queen graciously forgives your impertinence in exchange for eight hours of hard labor."

pause 1.0

red @closedbrow talking2mouth "Carrying shopping bags?"

leaf @surprised "The peasantry {i}can{/i} be taught! Fascinating."

red @sad "Oh, God. I just realized. I'm going shopping with four women. I'm going to have to hold four sets of bags."

leaf @happy "Right you are! So hop to it, cabin boy!"

show leaf:
    ease 1.0 xpos 1.5

pause 0.5

red @angrybrow talking2mouth "Cabin boy?! I thought I was a peasant! You can't just demote me like that!"

scene city_A with Dissolve(2.0)

stop music fadeout 2.5

queue music "audio/music/Inspira_start.ogg" noloop
queue music "audio/music/Inspira_loop.ogg"

$ renpy.music.queue("Audio/Bus arrive1.ogg", channel='misc', loop=None, tight=None)
queue sound "Audio/ExitBuilding.ogg"

show leaf:
    xpos 0.2 xzoom -1
show tia:
    xpos 0.4
show whitney:
    xpos 0.6
show flannery:
    xpos 0.8 xzoom -1
with dis

whitney @happy "Here we are, girls! (And [first_name]!) Welcome to the city!"

tia @surprised "There's so many people! Wow... how many people are there?"

flannery @closedbrow talkingmouth "Probably around three million?"

leaf @talkingmouth "Try a third of that. It's the biggest city in Kobukan, but Kobukan's still a tiny region."

red @talkingmouth "I read the only reason the academy is in Kobukan is because the President of Kobukan at the time basically begged Kanto to build a school here."

whitney @talking2mouth "So, where are we going first?"

red @talkingmouth "I actually need to go to the Pokémon Center. Janine told me to do some stuff there before the battle tryouts on Monday."

flannery @surprised "Wait, she asked {i}you{/i} to join the tryouts?"

red @confusedeyebrows talking2mouth ".{w=0.25}.{w=0.25}.{w=0.25}Feeling kind of offended."

whitney @talking2mouth "I think she's just surprised. You must've done something really big to impress her, given what Lance said to you."

red @happy "Hey, I always try to impress!"

leaf @closedbrow talkingmouth "Alright, so how about [first_name] goes to the Pokécenter, while we go to the Kobukan department store?"

red @talkingmouth "Sounds good."

leaf @sarcastic "Are you sure you'll be able to find the store after you're done at the Center?"

red @angrybrow talking2mouth "You {i}wound{/i} me. When have I ever been known to have difficulty getting anywhere?"

leaf @sarcastic "Oh, of course, silly me." 

show leaf at getcloser:
    xpos 0.2

leaf @talkingmouth "But, seriously, just use your phone if you get lost, okay?"

red @talkingmouth "Don't worry! No chance of that."

show leaf at getfurther:
    xpos 0.2

leaf @happy "Alright, then! See you in a bit."

scene blank2 with wipeleft

queue sound "Audio/ExitBuilding.ogg"

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.0)

narrator "You make your way to the Pokémon Center without much trouble--its bright red roof makes it easy to spot."

redmind @happy "Okay, looks like Janine's login credentials work... didn't expect her to have such a kiddy username and password, though. That's pretty funny."
redmind @frownmouth "Hm... So, if I just create a new set of boxes for myself, then [bluecolor]I should be able to store an unlimited number of Pokémon here.{/color}"

redmind @thinking "I guess I don't have to worry about filling her boxes up, then. Nice."
redmind @thinking "Actually, since I've got access to her Pokémon boxes right now, maybe I should take a peek...?"

menu:
    "{color=#66b77d}[[Knowledge]{/color} >Examine a Champion-contender's Pokémon":

        $ TraitChange("Knowledge")

        redmind @thinking "Hm... looks like they're mostly level 75s. A lot of Poison-types, but a few Fighting-types, too." 
        
        redmind @thinking "But there's a lot of moves I don't recognize..."

        redmind @happy "Well, at least now I know what sort of levels someone with a shot at Champion should have! That'll be useful a few hundred days from now."

    "{color=#e226a6}[[Patience]{/color} >You'll see them personally later":

        $ TraitChange("Patience")

        redmind "Nah. It's not worth the chance of getting in trouble here."

        redmind @happy "Besides, when I get on the Battle Team, I can just look at Janine's Pokémon in-person!"

redmind @thinking "Let's see, next, she wanted me to get as many Poké Balls as I could carry... the clerk over there can handle that..."

if (Item.PokeBall in inventory.keys()):
    $ inventory[Item.PokeBall] += 10
else:
    $ inventory[Item.PokeBall] = 10
$ inventory[Item.PremierBall] = 1
$ money -= 2000

show pokeball at itemhover

$ renpy.music.set_volume(0.25, delay=0.0, channel="music")
$ PlaySound("item_get.ogg")
$ renpy.music.set_volume(1.0, delay=2.0, channel="music")

pause 2.0

show pokeball at itemhide
$ renpy.pause(1.5, hard=True)

hide pokeball

narrator "You gained 10 Poké Balls! You also gained a Premier Ball as an added bonus!"
narrator "But you spent $2,000..."

redmind @surprised "Oh, God. I {i}really{/i} don't like spending money..."
redmind @thinking "Anyway, now that I know how stuff out here works, I should be able to come out here in my free time." 
redmind @thinking "{color=#0048ff}Shopping and swapping out Pokémon can be done in the same trip to the city, but it will take up most of my time.{/color}"

scene city_A with wipeleft

queue sound "Audio/ExitBuilding.ogg"

stop music fadeout 2.5
stop music channel "crowd" fadeout 2.5

queue music "audio/music/littleroot_start.ogg" noloop fadein 2.5
queue music "audio/music/littleroot_loop.ogg"

red @happy "Alright, buddy. You ready to go find the ladies?"

$ renpy.music.play("Audio/Pokemon/pikachu_scared.ogg", channel="altcry", loop=None)
pikachu sad_2 "Pika!"

red @surprised "Huh? What're you talking about, buddy? I'd never leave you behind. Where's this coming from?"

$ renpy.music.play("Audio/Pokemon/pikachu_sad.ogg", channel="altcry", loop=None)
pikachu sad "Pika..."

red @closedbrow talking2mouth "I'm confused. You didn't seem to have a problem with [starter_name], right? Why are you concerned that I'll add more Pokémon to the team?"

$ renpy.music.play("Audio/Pokemon/pikachu_sad2.ogg", channel="altcry", loop=None)
pikachu sad_2 "Pika. Pi-ka..."

red @surprised "What? No, of course not, buddy!" 
red @happy "You're my best friend! And you were my first friend, too! I'll never just shove you in the PC and leave you there, unless that's definitely what you want."

$ renpy.music.play("Audio/Pokemon/pikachu_question.ogg", channel="altcry", loop=None)
pikachu bashful "Pi-ka?"

red @talkingmouth "Don't worry about it. Don't worry about it even a little bit. You'll always be by my side."

$ renpy.music.play("Audio/Pokemon/pikachu_happy1.ogg", channel="altcry", loop=None)
pikachu happy "Pika!"

red @happy "Yeah! No matter how lazy, or unmotivated, or slow, or stubborn you are! You'll always be my buddy."

$ renpy.music.play("Audio/Pokemon/pikachu_confused.ogg", channel="altcry", loop=None)
pikachu neutral_3 "Pika..."

red @happy "You'll be by my side even if you absolutely {i}refuse{/i} to get serious in battles, or if you eat half of my food, or if you fall asleep during training, or if you--"

$ renpy.music.play("Audio/Pokemon/pikachu_angry1.ogg", channel="altcry", loop=None)
pikachu angry_4 "Pika!"

red @happy "Okay, okay, I'll stop!"
red @talkingmouth "But, seriously, I know everything about you. Maybe it's just sunk-cost at this point, but Frienergy aside, there's not a Pokémon I understand better than you."
red @happy "I know exactly what you're capable of, and how to push you to get there. And one day, you're going to be a star."

$ renpy.music.play("Audio/Pokemon/pikachu_question.ogg", channel="altcry", loop=None)
pikachu happy "Pika...?"

$ renpy.music.play("Audio/Pokemon/pikachu_angry1.ogg", channel="altcry", loop=None)
pikachu cocky_2b "Pika! Pika!"

show blank

pause 0.05

hide blank

$ renpy.music.set_volume(0.1, delay=0.0, channel="music")
$ PlaySound("sav.ogg")
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

narrator "[pika_name]'s heart shifts as his relationship with you evolves from '{color=#0048ff}Lazy Rat{/color}' to '{color=#0048ff}(Slightly) Less-Lazy Rat{/color}'!"

red @confusedeyebrows talkingmouth "...Wait, buddy. Did something about you just change?"

$ renpy.music.play("Audio/Pokemon/pikachu_happy1.ogg", channel="altcry", loop=None)
pikachu happy "Pika."

$ freelectricphases.append(1)

narrator "{color=#0048ff}[pika_name] will now have a level cap that is one level higher than any other Pokémon in your party.{/color}"

red @happy "Alright, let's head off. The girls probably need their packhorse by now."

stop music fadeout 1.5
queue music "audio/music/Inspira_start.ogg" noloop
queue music "audio/music/Inspira_loop.ogg"

$ renpy.music.play("Audio/Pokemon/pikachu_happy2.ogg", channel="altcry", loop=None)
pikachu happy "Pika!~"

$ timeOfDay = "Noon"

show city_B with Dissolve(2.0)

show leaf:
    xpos 0.2
show whitney:
    xpos 0.6
show flannery tired:
    xpos 0.8
show tia hat:
    xpos 0.4
with dis

red @sad "Yep. Just as I predicted, they've got at least twenty bags between them... my muscles are already sore at the thought."

show tia surprisedbrow frownmouth with dis

pause 1.0

show tia:
    parallel:
        ease 0.2 xpos 0.5
    parallel:
        ease 0.3 ypos 1.1
        ease 0.3 ypos 1.0
        repeat

tia happy "[first_name]! Look, look! Leaf bought me a hat!"

menu: 
    "It looks very good on you.":
        $ ValueChange("Tia", 1, 0.5)

        tia lightblush "Hee hee! Thanks! There were so many different kinds of hats. But this one looks like my sister's, so I wanted it!"

    "That was very considerate, Leaf.":
        $ ValueChange("Leaf", 1, 0.2)

        leaf @blush happy "Oh, I just {i}knew{/i} I had to buy it as soon as I saw it. It makes her look like a little artist!"

show tia:
    ease 0.5 xpos 0.4 ypos 1.0

red @talkingmouth "What did the rest of you get?"

whitney @talking2mouth "I got a new set of shoes. The cleats in my old ones were wearing down. Oh, and I got a couple really cute skirts, and then there were materials to make Springsday baskets! So I bought a ton of those."

flannery @talking2mouth "I got a bag of coffee grounds."

pause 1.0

flannery @sadbrow talking2mouth "{i}Several{/i} bags. I'm going to try and kick this damn morning haze, or die trying."

leaf @sadbrow happymouth "I might have bought an entire rack of gossip magazines..."
leaf @happy "But I think there might actually be something true in them this time! They even say the Champion of Unova is coming here!"

red @closedbrow talking2mouth "Sorry, roll it back a bit--Springsday, Whitney? What's that?"

whitney @happymouth "What, you don't know about Springsday?"

red @confusedeyebrows talking2mouth "Clearly not, otherwise I wouldn't have said 'what's that?'"

whitney @happy "Wow! What rock have you been living under?"

red @closedbrow talking2mouth "It's called Pallet Town, and having very limited internet access."

tia @surprised "I don't know what Springsday is, either!"

leaf @closedbrow talkingmouth "Now, see, {i}that's{/i} surprising."
leaf @talkingmouth "Springsday is a holiday celebrating... well, Spring. People celebrate by painting and hiding Pokémon eggs." 

whitney @happy "Some people just compete to see who can get the most, and rarest eggs, but at Kobukan, you can actually keep the eggs you find!" 

flannery tiredbrow @talking2mouth "Yeah, and you can also celebrate by eating buttloads of chocolate. White chocolate, mostly."

whitney @talking2mouth "Did you know white chocolate isn't actually chocolate? Check the packaging. It'll always say something like 'white confection.'"

leaf @talking2mouth "Marshmallows are also pretty popular Springsday snacks. People cook them into the shape of Torchic, Psyduck and Buneary."

red @happy "Man. I'm hungry, now. When's this Springsday thing?"

whitney @talking2mouth "April 24th. So, next Saturday."

leaf @closedbrow talkingmouth "That means it'll be the last event the outgoing Student Council will host, huh? One last hurrah."

red @happy "Looking forward to it."

pause 1.0

red @talking2mouth "But, seriously, I'm hungry. And if I'm going to be lugging you ladies' bags everywhere, then I'm going to need some refreshment."

leaf @happy "Did someone say restaurant tour?"

red @closedbrow talking2mouth "N-no. No-one said that."

leaf @angrybrow angrymouth "Too bad. We're going on a restaurant tour now! I've already seen most of the restaurants in this city, so I want to find something new."

red @surprised "Most of the restaurants? This is a {i}massive{/i} city."

leaf @sarcastic "Yeah, but everyone knows about those. You don't find trendy by just going to the places everyone else is going to!"

pause 1.0

red @closedbrow talking2mouth "I feel like that's exactly how you find trendy."

leaf @happy "Interesting opinion. Unfortunately, you're a boy."

red @sad "...Man, I just want to eat."

leaf @happy "Don't forget to take our bags!"

show flannery happy:
    ease 0.3 xpos 0.575 ypos 1.2 zoom 1.3

show whitney happy:
    ease 0.3 xpos 0.525 ypos 1.2 zoom 1.3

show tia happy:
    ease 0.3 xpos 0.475 ypos 1.2 zoom 1.3

show leaf happy:
    ease 0.3 xpos 0.425 ypos 1.2 zoom 1.3

show city_B with vpunch

red @surprised "OOOF!"

red @sad "C-can't... carry..."

leaf @flirttalk "Sorry. This is what you get for skipping arm day."

hide flannery
hide whitney
hide tia
hide leaf
with dis

show blank2 behind city_B

show city_B:
    align (0.5, 0.5)
    ease 3.0 rotate -4 zoom 1.2

pause 1.0

red @angry "In what world... ngh... have I skipped... {i}anything?!{/i}"

show city_B:
    parallel:
        easein_bounce 3.0 ypos 1.5
        pause 1.0
        ease 1.0 ypos 2.0
    parallel:
        ease 1.0 rotate -10 

pause 4.0

narrator "You spend a great many hours serving as a caddy to your female friends. Despite your bitter complaining, you actually quite enjoy yourself." 
narrator "Problems arise, however, as Tia displays a reckless disregard for traffic safety..."

leaf @surprised "Wh--Tia! The walking man! You need to wait for the walking man!"

flannery @surprised "Alright, add 'traffic lights' to the list of things that Tia has never seen before, I guess."

narrator "...Societal norms..."

hide city_B
hide city_A

whitney @surprised "Tia! Get out of the fountain! Pidove poop in that thing!"

narrator "...And, eventually, personal space."

hide blank2
show city_A 
show roughneck at leftside
with dis

show tia happy hat:
    xpos 1.5
    easeout 1.3 xpos .3
    "tia surprised hat"
    easein 1.0 xpos .65

show roughneck:
    xpos 0.25
    pause 1.3
    "roughneck angrybrow angrymouth"

pause 1.3

$ PlaySound("body crash.ogg")

roughneck -angrymouth @angrymouth "Hey! Watch where you're going!"

narrator "Despite the fact the man barely shifted, he clearly seems as though he's ready to start a fight."

roughneck neutralbrow neutralmouth @angrybrow angrymouth "Didn't your Mom teach you any goddamn manners?! Or'm I gonna have to teach you, huh?"

show tia happy with dis

narrator "Tia happily signs away at the thug, but it's apparent he doesn't have any clue what she's saying."

show tia sadeyes sadeyebrows frownmouth with dis

roughneck surprisedbrow @surprised "Hey, hey, what kinda signs are those? I don't know any gang like that. And who'd accept a shrimp like you, anyway?"
roughneck angrybrow neutralmouth @angrymouth "You tryin' to cause problems, is that it? Because I'm a big guy, you think you can just beat up on me whenever you want, huh?"

red @talking2mouth "Sir. We're not trying to cause any trouble. She was just having a bit of fun and bumped into you."

show tia happy with dis

roughneck neutralbrow neutralmouth @angrybrow angrymouth "Who the fuck is this? Your boyfriend?"

show leaf behind tia:
    xpos 1.5
    ease 1.5 xpos 0.4

show tia:
    ease 1.5 xpos 0.5

show whitney frownmouth behind tia:
    xpos 1.5
    ease 1.5 xpos 0.7
show flannery tired behind whitney:
    xpos 1.5 xzoom -1
    ease 1.5 xpos 0.8

leaf @talking2mouth "No, but with the way they're going, give it a week."

roughneck surprisedbrow @surprised "Ugh, more of you? Oh, I know, you're some of those brats from the college, right?"
roughneck happy "...Actually, you lot are always loaded, aren't you?"
roughneck neutralmouth @angrybrow angrymouth "Hey. When shortie here ran into me, it really hurt. Don't you think you owe me some compensation? Catch my meaning?"

pause 2.0

show flannery surprisedbrow frownmouth 
show whitney surprisedbrow frownmouth
show tia surprisedbrow frownmouth
with dis

leaf @sarcastic "Well, it's better than leering at a bunch of girls half your age and saying 'why don't you ditch this loser and come with me,' but it's still a cliché performance."
leaf @closedbrow talkingmouth "I give it a 6/10. You could really do to explore some of the wider variants of thuggery. There's no need to restrict yourself."

show roughneck:
    ease 0.5 xpos 0.2

roughneck angry "The fuck?"

leaf @closedbrow talkingmouth "Actually, you could even try expanding outside the range of thug and thug-adjacent roles. Obviously, with that face and body type, you're always going to be a bit typecast, but I bet you would make a very decent hockey goalie."

show whitney happy
show tia happy
with dis

roughneck neutralbrow neutralmouth "[ellipses]"

leaf @happy "Or, like, a sumo wrestler! Or maybe a cop? You know, one who was really good a few years ago, but has been on 'administrative leave' ever since Megan took the kids." 
leaf @sad "And, you know, with all that free time, booze and donuts have started to look {i}really{/i} good."

roughneck @talkingmouth "You sayin' I'm fat?"

leaf @happy "Good job! Give the man a cookie."

leaf @closedbrow talkingmouth "Although, actually, it might be better if you {i}don't{/i} have that cookie. Your veins are already so clogged with fat that one more cookie would probably cause you to keel over right now."

pause 1.5

roughneck @angry "...So you get that I'm not going to let you get away with that, right?"

show leaf:
    ease 0.4 xpos 0.6

show tia surprisedbrow frownmouth:
    ease 0.4 xpos 0.7 
    
show whitney surprisedbrow frownmouth:
    ease 0.4 xpos 0.8

show flannery angry:
    ease 0.4 xpos 0.4

flannery @angrybrow talking2mouth "You get within arms' reach of touch {i}any{/i} of us and my Numel will turn your entire team into cinders."

roughneck @happy "Hah. Cute, girlie. I like feisty chicks like you. Why don't you ditch these losers, and come with me?"

leaf @sad "Seriously, who's writing this guy's dialogue...?"

flannery furious "Back off, punk! Last warning!"

roughneck angry "Oh, yeah? Well, what if I don't want to back off, huh? Maybe I want {i}you{/i} to back off!"

show tia -surprisedbrow -frownmouth -surprised
show whitney -surprisedbrow -frownmouth -surprised
with dis

flannery "That's it! You better watch yourself! I'm a Gym Leader in the Hoenn League, and, {w=0.5}uh, you... {w=0.5}uh, puny punk, you... {w=0.5}uh... better prepare for a world of... {w=0.5}uh, hurt?"

pause 1.5

flannery sadbrow frownmouth @closedbrow sweat talking2mouth "Uh, guys? I kinda have to admit I've run out of bluffs. I think we actually {i}will{/i} have to battle him."

python:
    """
    pause 1.0

    flannery surprisedbrow frownmouth @surprised "Wait. What time is it, Whitney?"

    whitney @surprised "Time? Uh... three minutes after noon?"

    show blank2
    show afternoon at vspaz
    call clearscreens from _call_clearscreens_55

    $ timeOfDay = "Afternoon"

    pause 3.5

    show flannery sadbrow frownmouth behind leaf:
        ease 1.0 xpos 0.5

    show screen currentdate
    hide blank2
    hide afternoon
    with dis

    pause 1.0

    flannery @sadmouth "Actually... maybe we should just take the long way around here."
    """

red @confusedeyebrows talking2mouth "Seriously?"

flannery @happy sweat "Aaaand, I think I might have bit off more than I can chew. I don't actually have my Pokémon with me right now."

red @angrybrow talking2mouth "{i}Seriously?!{/i}"

roughneck @angrymouth "Hey! I'm talking here! You better not be ignoring me!"

red @closedeyes talking2mouth "Enough {i}arguing{/i}. I'll battle you. If I lose, you get all my money. If I win, you back off."

roughneck happy "Heh. Sure thing, brat. But you don't have a chance! Go, guys! Get him!"

$trainer1 = Trainer("red", TrainerType.Player, playerparty, number=2)
$trainer2 = Trainer("roughneck", TrainerType.Enemy, [
    Pokemon(pokedexlookupname("Scraggy", DexMacros.Id), level=7, moves=[GetMove("Rock Smash"), GetMove("Sand Attack"), GetMove("Leer"), GetMove("Headbutt")], gender=Genders.Male, ability="Intimidate"),
    Pokemon(pokedexlookupname("Zubat", DexMacros.Id), level=7, moves=[GetMove("Absorb"), GetMove("Acid"), GetMove("Supersonic"), GetMove("Astonish")], gender=Genders.Male, ability="Inner Focus")
], number=2)

call Battle([trainer1, trainer2], customexpressions=["red angrybrow frownmouth", "red angry", "roughneck", "roughneck angrybrow happymouth"]) from _call_Battle_22
$ battlehistory["Roughneck1"]  = _return

show roughneck behind tia with dis:
    xpos 0.2 

queue music "audio/music/Inspira_start.ogg" noloop
queue music "audio/music/Inspira_loop.ogg"

red @angry "That was a dirty trick, sending out two Pokémon at once. I didn't agree to a double battle."

if (WonBattle("Roughneck1")):
    roughneck @talking2mouth "Dirty trick? You're the one who pretended to be some kinda student when you're obviously a trainer already!"

    leaf @happy "Hah! That's the great part of this. He actually isn't. You just {i}genuinely{/i} had your butt kicked by a newbie."

    roughneck @angry "...Grr... Fuck this."

else:
    roughneck @happy "Cry some more about it! Now fork up the money you owe!"

    if (money == 0):
        red @happy "Funny thing about that, actually. I'm dead broke. Like, completely. I don't have any money at all."

        roughneck @angry "Huh?! You damn brat! You lied!"

        red @angrybrow talking2mouth "We both lied a little bit. I think that evens us out."
    
    else:
        red @closedeyes talkingmouth "Yeah, fine. Just leave us alone."

        leaf @sadbrow talking2mouth "[first_name], no..."

        $ money = 0

roughneck @talkingmouth "I'm getting out of here. But I'll leave you something to remember me by!"

show leaf angry behind roughneck
show whitney angry behind roughneck
show flannery angry behind roughneck
with dis

show roughneck:
    ease 0.2 xpos .6

pause 0.2

show tia surprisedbrow frownmouth -hat with vpunch

roughneck angry "Got your hat, shrimp! That'll teach you not to mess with us!"

show roughneck happy:
    ease 0.4 xpos -0.5

roughneck @talkingmouth "Neener neener neener!"

red @angry "Hey! Get back here, asshole!"

scene city_B with slideleft

narrator "You dash after the thuggish ruffian." 
narrator "You push past pedestrians, barrel between blockades, and flagrantly violate traffic laws in pursuit of this man... until you become aware he's leading you into an isolated, shady area." 
narrator "No sooner had the thought crossed your mind, then..."

stop music fadeout 2.5
$ renpy.music.play("Audio/Morning_ambience.ogg", channel='crowd', loop=True, fadein=1.0)

scene abandonedhouse with slideleft

narrator "You emerge in a small grassy clearing in the middle of the city. It's almost completely cut off from light by the skyscrapers that imprison it on all sides."
narrator "A dilapidated house, overgrown and in poor condition, sits in front of you. It creaks in the still darkness that settles on the area."
narrator "It would be very hard to stumble across this area on accident."

show roughneck as roughneck2 at rightside, night with dis
show roughneck as roughneck3 at leftside, night with dis

pause 1.0

red night @surprised "Ah, crap. You've got brothers, then?"

show roughneck at centerside, night with dis

roughneck angry "Damn right I do. And we've got each other's backs. And now you're in our territory. So what do you think we should do with a trespasser?"

red @angrybrow talking2mouth "Just give me the hat. You stole a hat from a tiny 18-year-old girl. That's not the kind of thing you want people knowing your gang for, is it?"

roughneck neutralbrow neutralmouth "[ellipses]"

roughneck3 @happy "Kid's got a point!"

roughneck2 @surprised "Yeah, uh, why'd you steal a kid's hat?"

roughneck @angry "It seemed like a good idea at the time, alright?!"

roughneck @angry "Look, just help me pile on this kid and make sure he doesn't come back here! And give me some potions, so I can heal my guys!"

red @angry "{i}You{/i} led me here!"

roughneck @happy "Cry some more, baby!"

if (len(trainer1.GetUnfaintedTeam()) > 0): 
    hide roughneck
    hide roughneck2
    hide roughneck3
    with dis

    $trainer1 = Trainer("red", TrainerType.Player, playerparty, number=3)
    $trainer2 = Trainer("roughneck", TrainerType.Enemy, [
        Pokemon(pokedexlookupname("Stunky", DexMacros.Id), level=5, moves=[GetMove("Poison Gas"), GetMove("Scratch"), GetMove("Focus Energy")], ability="Aftermath"),
        Pokemon(pokedexlookupname("Rattata", DexMacros.Id), level=5, moves=[GetMove("Tackle"), GetMove("Tail Whip"), GetMove("Quick Attack")], ability="Hustle")
    ])

    $trainer3 = Trainer("roughneck", TrainerType.Enemy, [
        Pokemon(pokedexlookupname("Scraggy", DexMacros.Id), level=7, moves=[GetMove("Rock Smash"), GetMove("Sand Attack"), GetMove("Leer"), GetMove("Headbutt")], gender=Genders.Male, ability="Intimidate"),
        Pokemon(pokedexlookupname("Zubat", DexMacros.Id), level=7, moves=[GetMove("Absorb"), GetMove("Acid"), GetMove("Supersonic"), GetMove("Astonish")], gender=Genders.Male, ability="Inner Focus")
    ])

    $trainer4 = Trainer("roughneck", TrainerType.Enemy, [
        Pokemon(pokedexlookupname("Skrelp", DexMacros.Id), level=6, moves=[GetMove("Tackle"), GetMove("Smokescreen"), GetMove("Water Gun"), GetMove("Feint Attack")], ability="Poison Point"),
        Pokemon(32, level=7, moves=[GetMove("Leer"), GetMove("Peck"), GetMove("Focus Energy")], ability="Poison Point")
    ])

    call Battle([trainer1, trainer2, trainer3, trainer4], healParty=False, customexpressions=["red angrybrow frownmouth", "red angry", "roughneck", "roughneck angry", "roughneck", "roughneck angry", "roughneck", "roughneck angry"], reanchor=[False, True, True, True]) from _call_Battle_23
    $ battlehistory["Roughnecks1"]  = _return

    show roughneck as roughneck2 at rightside, night with dis
    show roughneck as roughneck3 at leftside, night with dis
    show roughneck at centerside, night with dis

    $ renpy.music.play("Audio/Morning_ambience.ogg", channel='crowd', loop=True, fadein=1.0)

    pause 1.0

    if (WonBattle("Roughnecks1")):
        red night @angrybrow talking2mouth "There we go. I beat all three of you. Will you return the damn hat now?"

        roughneck @surprised "Bros... this guy's intense..."

        $ TraitChange("Courage")

        narrator "For beating the odds while severely outnumbered, you gain a point of courage!"

        $ TraitChange("Courage")

        narrator "And another one!"

    else:
        roughneck @happy "Hah! See? You're nothin' compared to us."

        red night @angry "There's three of you and one of me! I don't really feel bad about losing that one, to be honest!"

$ renpy.music.play("Audio/Morning_ambience.ogg", channel='crowd', loop=True, fadein=1.0)

"{color=#686080}Angry Voice{/color}" "\"What's going on out there?\""

roughneck @surprised "B-boss! We were just... uh..."

show roughneck3:
    ease 0.5 xpos 0.8
show roughneck2:
    ease 0.5 xpos 0.7
show roughneck:
    ease 0.5 xpos 0.2

pause 0.5

show silver closedbrow at night behind roughneck with Dissolve(2.0)

silver @talkingmouth "I've told you idiots a thousand times, I'm not your boss, I'm your landlord. And..."

silver surprisedbrow "[ellipses]"

silver sad "Shit."

red @confusedeyebrows talking2mouth "Silver...?"

silver @closedbrow talkingmouth "You weren't supposed to see this. I..."

silver @thinking "[ellipses]"

silver @angry "{size=40}Piss off!{/size}"

show roughneck3:
    ease 1.0 xpos -0.5
show roughneck2:
    ease 1.0 xpos -0.5
show roughneck:
    ease 1.0 xpos 1.5

pause 2.0

silver closedbrow frownmouth @talkingmouth "And leave the damn hat, obviously."

show roughneck:
    ease 2.0 xpos 0.8 zoom 1.3 ypos 1.2
    pause 1.0
    ease 1.0 xpos -0.5 zoom 1.0 ypos 1.0

pause 4.0

silver -closedbrow -frownmouth @talkingmouth "...Sorry. I can't control those idiots."

red @talking2mouth "...Silver, what are you doing here? Who were those people? Why were you in that shack?"

silver -sad "[ellipses]"

silver @talkingmouth "...This shack is...{w=0.5} my home."

red @surprised "Huh?"

silver @sad "Yeah. I don't live in the dorms.{w=0.5} I live off-campus.{w=0.5} Here."

red @sad "Why? Dorm accommodations don't cost any extra money..."

silver @closedbrow talkingmouth "I need to keep an eye on these guys. They're... they're likely to get in a lot of trouble if I wasn't here."
silver @sad "Sorry about them stealing your hat. Uh, your friend's hat, probably."

red @confusedeyebrows talking2mouth "But... who are they? Why do you feel you need to watch them?"

silver @talkingmouth "...They're my Dad's former employees. He wasn't a good boss. He ruined a lot of lives with his success. But when he failed, and left, he ruined even more."
silver @sad "These idiots don't know how to live without some asshole exploiting and abusing them. So I'm trying to... I dunno. Rehabilitate them?"

red @talkingmouth "That's why they call you boss, then?"

silver @closedbrow talkingmouth "Yeah. There's about twenty of us living in this piece of crap shack buried in the middle of the city, and all these grown-ass men and women treat me like I'm the second coming."
silver @angry "It's a joke."

red @sad "[ellipses]"
red @sad "Anything I can do?"

silver @closedbrow "[ellipses]Hm." 
silver @talking2mouth "Actually, if you could come here once in a while, and battle them... they're always getting too near the school, trying to pick fights."
silver @happy "Might do them some good if a fight picked {i}them{/i} once in a while." 
silver @sad "I can't do it, because they already think they're lower than me. As though I wasn't the lowest."

pause 1.0

silver @talkingmouth "Oh, yeah. I can't pay you, but those guys love to do gamble battles."
silver @closedbrow talkingmouth "So if you're subtle about it, you can probably make some cash."
silver @closedbrow talkingmouth "...I'd give them a bit of time, though. Like, they'll notice if you come here {i}every{/i} day. {color=#0048ff}Once a week would probably be as much punishment as they could handle.{/color}"

$ beatgrunts = True

silver @talkingmouth "So... wait until Monday before coming back here, alright?"

red @talkingmouth "Noted."

silver @closedbrow talkingmouth "Although we're probably not going to have time, given the Battle Team tryouts are on Monday..."

pause 1.0

red @closedbrow talking2mouth "You said your guys wander near the school?"

silver @talkingmouth "Yeah. If you beat 'em up once in a while, though, I can probably get them to stay here."

red @happy "Well, cleaning up a delinquent problem sounds just like the kind of thing a future Student Council member could put on their resume."

silver @closedbrow talkingmouth "You're trying to get on the SC?"

red @talkingmouth "Yeah. Today's the first day I'm actually going out of my way to make that happen, though."

silver @surprisedbrow talking2mouth "Your first day? {i}Shit.{/i} You work fast."

red @talking2mouth 'Well, I only have two weeks, so, yeah. I kinda gotta.'

silver @sad "...Let's make a deal."

red @confusedeyebrows talking2mouth "What kind of deal?"

silver @talkingmouth "Firstly, you come over here every once in a while and let my guys get it out of their system."
silver @sad "Second, you don't tell the cops about this."
silver @closedbrow talkingmouth "The property's legally mine, but they won't give two shits about that if they decide they don't want us here."

pause 1.0

silver @talkingmouth "Anyway, if you do that... I'll help you get elected." 

red @closedbrow talking2mouth "Why do you care?"

silver @sad "I don't like what that Cheren guy is saying about repealing the curfew. Looks like, if he gets elected, he'll actually be able to make it happen."
silver @closedbrow sadmouth "And if that happens, then people at the school will come {i}here{/i} at night. And I can't do anything about people who come here, you know?"

red @sad "Oh, yeah... I didn't think of that. And this isn't the kind of thing you can just explain to him, is it?"

silver @sad "Nah. I've watched him in our dark elective class, and I can tell you, dude's absolutely a narc."

red @talking2mouth "Alright. I mean, that's a pretty popular position he holds. Even if I'm elected, he might still pass the issue."

silver @closedbrow talkingmouth "Yeah, well. If anyone can convince him to drop it, it's you. You can just... talk. And people don't even care what you say, they just like how you make them feel."

red @confusedeyebrows talking2mouth "Uh... have you heard that from someone? Or is that just you?"

silver @angrybrow talkingmouth "Don't play games with me. You know exactly what I'm talking about."
silver @sad "Even if I don't."

red @confused "...When you say you'll 'help me get elected,' what do you mean by that?"

silver @closedbrow talkingmouth "Don't ask. Just know that it'll work."

pause 1.0

red @sadeyes sadeyebrows talkingmouth "Silver, you're just asking me to do stuff I already would've done."

silver @angry "Then take it as a goddamn present! "

pause 1.0

silver @surprisedbrow talkingmouth "...People are coming. I gotta go."

show silver:
    matrixcolor nightmatrix alpha 1.0
    ease 2.0 matrixcolor BrightnessMatrix(-1.0) * ContrastMatrix(0.0) alpha 0.0

pause 2.0

leaf @angry "Alright, punks! This is the ICPD! Come on out with your Poké Balls out and your hands up, and we won't put you in the slammer!"

red @closedbrow happymouth "...{i}Sigh.{/i} Leaf."

stop music channel "crowd" fadeout 1.5
queue music "audio/music/Inspira_start.ogg" noloop
queue music "audio/music/Inspira_loop.ogg"

scene city_B
show leaf surprisedbrow frownmouth:
    xpos 0.2 xzoom -1
show whitney surprisedbrow frownmouth:
    xpos 0.4
show tia surprisedbrow frownmouth:
    xpos 0.6
show flannery surprisedbrow frownmouth:
    xpos 0.8 xzoom -1
with Dissolve(1.0)

$ timeOfDay = "Evening"

red @happy "Hey, ladies. Here's your hat, Tia."

show leaf happy
show whitney happy
show tia hat happy
show flannery happy
with dis

leaf @surprised "[first_name]? You're still alive?!"

red @confusedeyebrows talking2mouth "Actually, I died, and have come back to take care of my unfinished business. I seem to remember you guys had some bags?"

show leaf sad
show whitney sad
show tia hat sad
show flannery sad
with dis

leaf sad "...Oh no! We left them in the middle of the road when we ran after you."

show leaf -sad
show whitney -sad
show tia hat -sad
show flannery -sad
with dis

red @happy "Welp. The day's still young. Let's try to find them and, if we can't, then we can just go shopping again."

leaf @sarcastic "You're in a good mood. What happened in that alleyway?"

red @happy "Oh, happy surprises. Impersonating a cop's a crime, by the way."

leaf -flirtbrow -talking2mouth @happy "What are they going to do, arrest me? You can't arrest a cop."

scene city_A with Dissolve(2.0)

pause 1.0

show leaf happy:
    xpos 0.2 xzoom -1
show whitney happy:
    xpos 0.4
show tia hat happy:
    xpos 0.6
show flannery happy:
    xpos 0.8 xzoom -1
with dis

narrator "When you retrace your steps to where the girls left their shopping bags, you find them{w=2.0}{nw}"

show leaf sad
show whitney sad
show tia hat sad
show flannery sad
with dis

extend @talkingmouth " in pieces, scattered across the road, and showing clear signs of having been run over by {i}several{/i} cars."

whitney @sad "Oh, no... my cleats... my Springsday baskets!"

flannery tiredbrow tiredmouth @talking2mouth "Well, guess this is a sign from the universe that I'm never going to get over my anger issues. Damn, that was a lot of coffee."

leaf -sad @talking2mouth "Oh, well. It's not great, but we can just re-buy that stuff."

whitney angrybrow frownmouth @angry "We're not all made of money, like you, Leaf!"

tia angrybrow frownmouth @angrymouth "Yeah! I can't afford another hat."

leaf @sarcastic "Sweetie, you're wearing the hat right now. Also, I bought it for you."

tia @angryeyes angryeyebrows poutmouth "Yeah! And I want another!"

leaf @sarcastic "Right, well, you girls can complain all you want, but if you want {i}solutions{/i} to your issues, you've got a loaded friend who is feelin' pretty generous."

show whitney -angrybrow -frownmouth
show tia -angrybrow -frownmouth
show flannery -tiredbrow -tiredmouth
with dis

leaf @sadbrow talkingmouth "Besides... it's kinda my fault that the stuff got hit."

red @talkingmouth "Huh? How come?"

leaf blush @embarrassedbrow talkingmouth "Well... after you ran off, I told everyone to just ditch our stuff and run after you."
leaf @closedbrow talking2mouth "Which I might not have done if I remembered how fast you run, since we were like five minutes late. But whatever, I did."

flannery @talkingmouth "Yeah, she bolted right after you, like a Manectric. But... then got tired out after, like, fifty feet."

leaf -blush @angry blush "Hey! I'm a woman of many positive qualities, and I never claimed my athleticism was one of them!"

red @happy "I appreciate you running after me, anyway."

leaf @bigblush flirttalk "Yeah, I'm kinda used to it at this point."

red @closedbrow talking2mouth "Well, this is going to sound like an excuse to get out of shopping with you girls, but someone should really clean up this trash." 
red @talkingmouth "If you guys want to go back and get your stuff before the school closes for the day, we can all meet back up here."

leaf @surprised "You're going to clean this junk up? How civically responsible."

red @happy "Hey, Inspira's a pretty city. Besides, this is the kinda stuff a Student Council member should do."

tia @happy "I'll clean up trash, too!"

whitney @surprisedbrow talking2mouth "Oh? Should I stay here to interpret for you, Tia?"

tia @happy "Nope! [first_name] and I don't need words."

pause 1.0

leaf @sarcastic "Ugh, I'm {i}so{/i} over being surprised by this girl. Just let me know when she starts eating your face, alright?"

red @confusedeyebrows talking2mouth "Kinda hoping you'll notice that one yourself. And call an ambulance?"

leaf @angrybrow angrymouth "I'm not talking about literally eating your face, you {i}dork.{/i} I mean..."

leaf @sarcastic "Ugh, whatever. Back to shopping, round two."
leaf @happy "Beat your last time and win a prize!"

hide leaf
hide whitney
hide flannery
with dis

if (persondex["Tia"]["Value"] >= 5):
    tia happy "Let's go!"

    red @happy "Hey, I understood that!"

show tia:
    ease 1.5 xpos 0.7
    ease 0.2 ypos 1.1
    ease 0.2 ypos 1.0
    ease 1.5 xpos 0.3
    ease 0.2 ypos 1.1
    ease 0.2 ypos 1.0
    ease 1.5 xpos 0.9
    ease 0.2 ypos 1.1
    ease 0.2 ypos 1.0
    ease 1.5 xpos 0.1
    ease 0.2 ypos 1.1
    ease 0.2 ypos 1.0
    ease 1.5 xpos 0.5
    ease 0.2 ypos 1.1
    ease 0.2 ypos 1.0
    repeat

narrator "You and Tia begin the slow and laborious process of cleaning up the shattered shopping on the road, made more difficult by the fact you have to stop your work every time a car goes by."
narrator "A few people in the cars wave at you and give you a thumbs-up."

red @happy "It's nice to be appreciated, right, Tia?"
red @closedbrow talking2mouth "Still, I bet Lance would never be caught dead picking up trash like this. This probably isn't making me Champion material..."

narrator "Tia nods, enthusiastically. Her eyes are wide and admiring."

red @happy "Hey, stop looking at me like that. It's picking up trash. Not exactly glamorous work."

play music "audio/music/BW_Pokemon_Start.ogg"
queue music "audio/music/BW_Pokemon_Loop.ogg"

show tia surprisedbrow frownmouth with dis: #changes to add animation start here
    ease 0.5 xpos 0.3 ypos 1.0

$ PlaySound("Pokemon/cries/88.mp3")
queue sound "Audio/Pokemon/cries/568.mp3"

$ sidemonnum = 88.1

sidemon @talkingmouth "Griiime! Grimer!"

$ sidemonnum = 568

sidemon @talkingmouth "Trub. Trub-bish!"

red @angrybrow talking2mouth "Crap. Looks like the wildlife doesn't want us to clean this up. And my team's pretty beat up already, from those thugs earlier..."

show tia angryeyes angryeyebrows poutmouth with dis:
    xpos 0.3 ypos 1.0 xzoom -1

show grimer with dis:
    xpos .75 ypos .4
    parallel:
            ease 0.7 rotate 5
            ease 0.7 rotate -10
            ease 0.7 rotate -5
            ease 0.7 rotate 10
            repeat

pause 1.0

red @confusedeyebrows talking2mouth "Tia? What, are you going to fight them?" 

show tia happy with dis:
    xpos 0.3
    ease .25 ypos 1.03
    ease .25 ypos 1.00

pause 1.0

if (GetRelationshipRank("Tia") == 0):
    red @talkingmouth "Alright, be my guest. I don't think I've seen your Pokémon yet, anyway, so..."

else:
    red @talkingmouth "Alright, be my guest. I don't think I've seen your Mime Jr. battle yet, anyway, so..."


pause 0.5

show tia:
    xpos 0.3 ypos 1.0 xzoom -1
    parallel:
        ease 2.4 xpos 0.7
    parallel:
        easein 0.55 ypos .92
        easeout 0.25 ypos 1.0
        easein 0.55 ypos .92
        easeout 0.25 ypos 1.0
        easein 0.55 ypos .92
        easeout 0.25 ypos 1.0
        
pause 2.4

narrator "Tia happily smiles and skips over to the encroaching horde of Pokémon..."

show tia:
    xpos .7 ypos 1.0
    ease .3 xpos .65
    pause .3
    ease .2 xpos .9

pause 0.7

show grimer:
    xpos 0.75 rotate 0
    parallel:
        easein 0.3 ypos -.4 rotate -180

stop music

$ PlaySound("Body punch.ogg")
$ PlaySound("Pokemon/cries/88.mp3")
pause 0.3

show grimer:
        zoom 0.5 xpos 0.8 ypos -.2
        parallel:
            ease 0.25 rotate 90
            ease 0.25 rotate 180
            ease 0.25 rotate 270
            ease 0.25 rotate 360
            ease 0.25 rotate 450
            ease 0.25 rotate 540
            ease 0.25 rotate 630
            ease 0.25 rotate 720
            ease 0.25 rotate 810
            ease 0.25 rotate 900
            ease 0.25 rotate 990
            ease 0.25 rotate 1080
            repeat
        parallel:
            ease 3.0 ypos .5
        parallel:
            ease 0.5 zoom 0.4
            ease 0.5 zoom 0.3
            ease 0.5 zoom 0.2
            ease 0.5 zoom 0.12
            ease 0.5 zoom 0.05
            ease 0.5 zoom 0.0
        parallel:
            ease 0.5 xpos 0.77
            ease 0.5 xpos 0.74
            ease 0.5 xpos 0.71
            ease 0.5 xpos 0.68
            ease 0.5 xpos 0.66
            ease 0.5 xpos 0.65

narrator "And punches a Grimer in the face."

pause 2.0

red @surprised "Wh- Tia, no! That's Pokémon abuse! You're not allowed to fight Pokémon! Get back here!"

show tia surprisedbrow frownmouth: #changed
    xzoom 1 xpos .9
    ease 2.0 xpos 0.5
    "tia worriedeyebrows sadeyes hat frownmouth"

narrator "Tia looks confused at this, but nevertheless jumps right back to your side, then looks up at you, as though awaiting more commands."

show tia worriedeyebrows sadeyes hat frownmouth:
    xpos 0.5

narrator "Thankfully, the rest of the horde, having seen a human break all the rules of nature they understood, and just sock one of them in the face, quickly absconds."

red @angrybrow talking2mouth "Tia, what the hell, seriously. You can't just {i}fight{/i} Pokémon. I mean, only Pokémon do that."

show tia happy with dis:
    ease .3 ypos 1.05
    ease .3 ypos 1.00

pause 1.0

red @confused "...Tia. Be honest with me. Did I see you jump off the roof this morning?"

show tia -happy with dis: #last change
    ease .3 ypos 1.05
    ease .3 ypos 1.00

narrator "Tia nods, again, without a moment of hesitation."

red @closedbrow talking2mouth "Geez. I don't know what to do with this information..."

pause 2.0

red @wince talking2mouth "Let's just continue our cleaning. But the next time I have some free time... and I understand sign a bit better... we're going to have a talk about this."

show blank2 with dis

narrator "The rest of the cleanup efforts pass without incident. Eventually, the other girls come back with new bags, and you struggle back to campus under their weight, thoroughly exhausted from such an active day."

pause 2.0

mace @talkingmouth "...Did you see that? Cleaning up trash in the city? Pathetic."

face @angry "Amongst the garbage is the right place for someone like him. Filthy cheater."

mace @talkingmouth "...Hm. I think I might have a plan to expose him as the beneficiary of nepotism that he is. We certainly can't let someone like {i}that{/i} get into our Student Council."

face @happy "Really? I have a plan too, actually."

mace @surprisedbrow happymouth "Oh? I'm all ears..."

call clearscreens from _call_clearscreens_56

stop music fadeout 2.5

queue music "Audio/Music/Road to Viridian City.ogg"

show night at vspaz

$ timeOfDay = "Night"

pause 3.5

scene relichall_B 
show leaf at night:
    xpos 0.2 xzoom -1
show whitney at night:
    xpos 0.4
show tia hat at night:
    xpos 0.6
show flannery at night:
    xpos 0.8 xzoom -1
show screen currentdate 
with dis

whitney @surprised "Wow, it's {i}waaaaay{/i} later than I thought it was. We aren't going to get in any kind of trouble with security, are we?"

flannery @talkingmouth "Not if we {i}run{/i} back to our dorm."

leaf @surprisedbrow talking2mouth "You three are from Pledge Hall, right? You guys should probably go, then."

whitney @talking2mouth "Yeah, you're right. See you tomorrow, maybe? But, if not, definitely see you Monday!"

leaf @happy "See you!"

hide tia
hide flannery
hide whitney 
with dis

red night @closedeyes talking2mouth "Phew. That's three-fourths bags gone. Mind taking your portion now?"

leaf @talking2mouth "Not so fast. What {i}actually{/i} happened in that alley?"

red @sadeyes sadeyebrows talkingmouth "You're going to hate this, but... it's a secret."

leaf @angry "Damn, {i}another{/i} one?!"

red @talkingmouth "Yeah... people are just... confiding in me. Really fast. And {i}a lot.{/i}"

if (GetRelationshipRank("Leaf") > 0):
    leaf @happy "Well, beats how it was back in Pallet Town, right? You've got so many friends, it's actually becoming a problem!"
else:
    leaf @sarcastic "Oh, boo-hoo. You whiner. 'Oh no, I'm too popular.'"

red @closedbrow talking2mouth "Hey, serious question time."

leaf @sarcastic "Yes, I wear a padded bra, and so does everyone else at this school. Including the teachers. Including the {i}male{/i} teachers."

red @surprised "Wow. You really just say anything you want, don't you?"

leaf @talkingmouth "Why would I say something I didn't want to?"

red @closedbrow talking2mouth "Touch."

leaf @sarcastic "It's pronounced 'touché'."

red @talkingmouth "Whatever, fancypants. Can I ask my actual question now?"

show leaf at night:
    ease 1.5 xpos 0.5

leaf @talkingmouth "Yeah, go ahead."

red @closedbrow talking2mouth "Okay. So, I've got two friends. And they both want very different things. Actually, the things they want are opposites."

red @talkingmouth "How do I decide who to help?"

leaf @sarcastic "Uh, help the one you like more?"

red @angrybrow talking2mouth "Be serious, please."

leaf @talking2mouth "No, I am being serious. There's no other way. Unless you can somehow show them that they don't actually want what they think they do, you've just gotta make a choice."

red @sad "That first option sounds kinda... manipulative..."

leaf @talkingmouth "'Social engineering,' you mean."

red @closedeyes talking2mouth "...Alright, that's enough for tonight. Take your gossip mags, and let me sleep for a year."

leaf @happy "Alright! Got any plans for Sunday?"

red @happy "No. And I'm looking forward to it!"

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_57

show blank2 with dis
    
$ renpy.pause(2.5, hard=True)

jump day010418
