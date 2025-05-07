label secondhomeroom010527:

scene blank2

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

show oak 
hide blank2 
with splitfade

oak @talkingmouth "Welcome back to class, ladies and gentlemen."
oak @talking2mouth "Now, can anyone here quickly recap what I covered in this morning's lecture?"

pause 0.5

oak @happy "Miss Green."

leaf uniform @talking2mouth "You were talking about terrains, and how they change Camouflage. When using Camouflage on an active terrain, you change into the type of Pokémon that the terrain helps."

oak @talkingmouth "Quite right."
oak @sweat talking2mouth "Now, I've mentioned before how to {i}create{/i} a terrain. But sometimes one does not want the battlefield to be altered. There are four ways of removing terrains that I recommend you brush up on."

oak @closedbrow talkingmouth "The first method is simply overwriting the terrain with one of your own. If Misty Terrain is currently in effect, and a Grookey with the ability 'Grassy Surge' comes in, the terrain will be...? Ms. Moore."

flannery uniform @talking2mouth "Uh, Leafy Terrai--"
flannery uniform @surprised "Wait! Sorry, got mixed up. Grassy!"
flannery uniform @lightblush happy "Grassy Terrain."

oak @talkingmouth "Correct. This may seem basic, but using terrain-setting moves is the simplest way to get rid of a different terrain."
oak @talkingmouth "It is not, however, the most common way terrains disappear. Terrains will, of their own accord, disappear after five standard turns."

show hilbert uniform with dis:
    xpos 0.75

hilbert surprised @closedbrow talkingmouth "Or eight turns if-"

oak @angrybrow talking2mouth "Mr. Von Schwarzdrachen. Please do not interrupt me."
oak @talkingmouth "You are correct, but it is disrespectful to both me and your classmates to continually interrupt."

pause 1.0

hilbert closedbrow smilemouth "Hmph."

hide hilbert with dis

oak @talkingmouth "What Mr. Von Schwarzdrachen says is correct. Terrains last for eight turns if the user is holding the 'Terrain Extender' item."
oak @happy "This is one of those items whose function is entirely apparent from the name--much more sensibly named than the 'Life Orb', which is an orb that 'removes' life."
oak @talking2mouth "But that's a lecture for the future, I suppose."

pause 1.0

oak @talkingmouth "Ah, now we come to the crux of the matter. Please take notes on this--exams are open-book, so there's no reason not to, unless you're worried about carpal tunnel syndrome."
oak @closedbrow sweat talking2mouth "{size=30}In which case you should be quite thankful you are not in Professor Willow's class. His students go through pencils like they're {i}eating{/i} them. But that won't be on the test.{/size}"
oak sad2eyes @talkingmouth "The third and final way a terrain may be removed is through a series of moves that {i}explicitly{/i} perform that function."

narrator "Oak takes a quick glance at his notes."

pause 0.5

narrator "You suddenly realize that Professor Oak has notes. For as long as you'd known him, he had {i}never{/i} written down a plan."

redmind uniform @surprisedbrow frownmouth "Wow. Professor Cherry really did a number on him."

oak -sad2eyes @closedbrow talking2mouth "Defog, Ice Spinner, Steel Roller... these moves will {i}entirely{/i} remove any extant terrain, without replacing it."
oak @talkingmouth "They have other effects, too, of course. Defog and Mortal Spin will remove hazards on your side of the field--Defog will extend the same courtesy to your opponents, while also removing any barriers in place." 
oak @closedbrow talking2mouth "Light Screen, Reflect, that sort of thing."
oak @talkingmouth "Steel Roller is a very powerful Steel-type move, hitting well above the comparable Iron Head or Flash Cannon. That being said, it will entirely fail if there is no active terrain when used."
oak @confusedeyebrows talking2mouth "One can see, then, how its large damage potential is mitigated by the logistics of sustaining an active terrain every time you want to use it."

pause 0.5

oak @talkingmouth "And... well, I believe that's the end of the lecture. You should now know everything you need to pass the upcoming test with flying colors."
oak @sweat talking2mouth closedbrow "Of course, I've generally been advised to {i}avoid{/i} teaching to the test, but... I think at this point that doing so may be for the best."
oak @talking2mouth "On the subject of the test, there are three pieces of information you should remember." 
oak @talkingmouth "The first is that your opponent will exclusively attack your Kecleon, as long as it is able to. You must not let them. If your Kecleon takes a single point of damage, you cannot pass this exam."
oak @talking2mouth "The second thing to remember is that {i}almost{/i} all Pokémon on the field will be burned and equipped with an Air Balloon. I suppose it was very hot air!"
oak @talking2mouth "The final thing is that your opponent will only use the following moves--Leech Seed, Dragon Claw, and Bullet Punch."
oak @closedbrow talkingmouth "It will be up to you to determine which opposing Pokémon will use which move, and then what you need to do to counter it."
oak @talkingmouth "Abilities are extremely important in this test. Before you commit to any moves, look over your Pokémon, and make sure you understand what their abilities do."

pause 0.5

oak @talkingmouth "If no-one has any questions, then...?"

pause 1.0

oak @happy "Then please take out your pencils. I know I need not tell you that [bluecolor]this will be graded.{/color}"

#Test: have one Pokémon with the terrains and steel roller Or a bunch of Pokémon that have terrain-setting abilities and moves?
#Test: have one Pokémon with camouflage
#Switch types to become immune to the moves of the opposing Pokémon.
#Misty Terrain to become immune to Dragon move
#Psychic Terrain to become immune to a priority move.
#Grassy Terrain to become immune to Leech Seed

python:
    AddEvent("Professor Oak", "KecleonTest")
    trainer1 = Trainer("red", TrainerType.Player, [
        Pokemon("Kecleon", level=70, moves=["Camouflage"], ivs=[0, 0, 0, 0, 0, 0], ability="Color Change", nature=Natures.Serious),
        Pokemon("Impidimp", level=10, moves=["Misty Terrain", "Nasty Plot", "Confide", "Trick"], ivs=[0, 0, 0, 0, 0, 0], ability="Prankster", item="Air Balloon", nature=Natures.Serious),
        Pokemon("Grookey", level=10, moves=["Grassy Terrain", "Taunt", "Endure", "Growl"], ivs=[0, 0, 0, 0, 0, 0], ability="Grassy Surge", item="Air Balloon", nature=Natures.Serious),
        Pokemon(876.1, level=10, moves=["Play Nice", "Baton Pass", "Charm", "Protect"], ivs=[0, 0, 0, 0, 0, 0], ability="Psychic Surge", item="Air Balloon", nature=Natures.Serious)#Indeedee-F
    ], number=2)

    trainer2 = Trainer("oak", TrainerType.Enemy, [
        Pokemon("Gabite", level=33, moves=["Dragon Claw"], ability="Rough Skin", ivs=[0, 0, 0, 0, 0, 0], item="Air Balloon", nature=Natures.Serious),
        Pokemon("Tangela", level=33, moves=["Leech Seed"], ability="Regenerator", ivs=[0, 0, 0, 0, 0, 0], item="Air Balloon", nature=Natures.Serious),
        Pokemon("Scizor", level=33, moves=["Bullet Punch"], ability="Technician", ivs=[0, 0, 0, 0, 0, 0], item="Air Balloon", nature=Natures.Serious)
    ])

    for mon in trainer1.GetTeam() + trainer2.GetTeam():
        if (mon.GetNickname() != "Kecleon"):
            mon.AdjustHealth(1, True)
            mon.ApplyStatus("burned")

call Battle([trainer1, trainer2], clearstats=False, gainexp=False, healParty=False, uniforms=[True, False], lockbag=True, lockluck=True, custombrain=oakkecleontestbrain, customswitchbrain=oakkecleontestswitchbrain) from _call_Battle_163
$ RecordBattle("Oak12")
$ RemoveEvent("Professor Oak", "KecleonTest")
$ renpy.transition(dissolve)
show screen currentdate

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom
show oak 
with dis

pause 2.0

redmind uniform @confusedeyebrows frownmouth "Sam is just slowly leafing through the tests... it's impossible to tell what he's thinking."

if (WonBattle("Oak12")):
    redmind @thinking "Well, at least I'm confident in my score."

else:
    redmind @thinking "If everyone else did like I did, even with him trying to turn things around..."

pause 0.5

oak @talkingmouth "Well, this is good to see."

pause 1.0

show hilbert uniform with dis:
    xpos 0.75

pause 1.0

oak @talkingmouth "Hm? Yes, Mr. Von Schwarzdrachen. Thank you for raising your hand. What is it?"

hilbert @talkingmouth "Can you provide specifics regarding our performance? How we did as a class?"

oak @closedbrow talking2mouth "Well, I haven't {i}fully{/i} graded them yet, but..."
oak @sweat closedbrow happymouth "After a {i}thorough{/i} glance..."

hide hilbert with dis

oak @talkingmouth "It appears that we may be doing better."
oak @closedbrow talking2mouth "Granted, we all have a ways to go, but this is a marked and objective sign of improvement."

redmind @sadbrow frownmouth "He says 'we'... He's also learning, huh?"

oak @talkingmouth "Well, that's all the time we have for today's test. Thank you for your patience."
oak @happy "Have a nice day!"

hide oak with dis

pause 1.0

show blue uniform with dis:
    xpos 0.33

show leaf uniform with dis:
    xpos 0.66

blue @talkingmouth "Are you going to go talk to Ethan and Yellow now?"

red @talkingmouth "Not right now. I've got some other stuff to do, first. But before I go to bed today. Don't worry."

blue @talkingmouth "Fine."

leaf @talkingmouth "What's this about?"

blue @closedbrow talkingmouth "You don't need to know."

red @unamusedbrow talking2mouth "Look, if you don't tell her, I will, and wouldn't you rather tell the story from {i}your{/i} point of view?"

show leaf surprisedbrow frownmouth with dis

blue @angry "Gah... fine! Leaf, you're helping me train--I'll tell you then!"

show blue with dis:
    xpos 0.33
    ease 0.5 xpos -0.2

pause 1.0

leaf @talking2mouth "Huh. Is this how Yellow feels?"
leaf @sadbrow talkingmouth "On the one hand, I totally don't want to do what he says, but now I'm curious about what's happening between you four..."
$ dratinipronouns = "him" if GetTrainerTeam("Leaf", "Dratini") else "her"
leaf @closedbrow talking2mouth "And I guess he's been training my Dratini for a while. This would be a good time to check in on [dratinipronouns], anyway."

red @happy "Sounds good. See you back at the dorm!"

$ removestudents = { "Blue", "Leaf" }

call freeroam from _call_freeroam_32

$ removestudents = set()

stop music fadeout 1.5

show screen songsplash("Pallet Town", "Zame")
$ renpy.music.queue("Audio/Music/palletpiano.ogg", channel='music', loop=True, tight=None)

narrator "You finish up your business early, and head to the dorm."

scene suitenight 
show ethan:
    xpos 0.33
show yellow neutrallowponytail:
    xpos 0.66
with splitfade

red @happy "Hey, guys."

ethan @happy "Hey, man."

yellow @talkingmouth "Hi. How was your day?"

red @happy "Pretty good. Melody didn't do anything crazy in class today. And Sam seems like he's really trying to turn things around."

ethan @closedbrow talking2mouth "Man, I know he's your friend, but I don't know how you could live with him as a teacher. I'm pretty sure hearing him lecture made me {i}stupider.{/i}"

yellow @sadbrow talkingmouth "It's clear he's very passionate about what interests him."
yellow @sadbrow happymouth "It's just unfortunate that... there wasn't much overlap between what was on the tests, and what he taught us."

ethan @confused "Yeah, it was bad enough for one week. But you've had him for, like, eight weeks, right? I'd request a transfer if I were you. There's a spot in Kris' class, between Yellow and I."

red @closedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

red @sadbrow talkingmouth "He's my friend. I don't leave my friends behind, no matter how badly they're doing."
red @happy "Anyone can be brilliant with enough time and support. Even my sixty-five-year-old teacher."

$ PlaySound("Pokemon/pikachu_norm1.ogg")

libpikachu @talkingmouth "Pika."

red @happy "Even my tubby Pikachu, who only showed an actual interest in battling a month ago."

ethan @closedbrow talkingmouth "...Yeah, you're right."

pause 1.0

yellow @talkingmouth "Well... would you like to play a game? It's a while before curfew."

red @talkingmouth "I was actually hoping we could talk."

ethan @talkingmouth "It's what we're best at."

show ethan unamusedbrow frownmouth
show yellow unamusedbrow frownmouth
with dis

red @sadbrow talkingmouth "See, Blue told me that you guys had a bit of a... disagreement."

ethan -unamusedbrow @talking2mouth "Man. Did Blue seriously ask you to patch things up between us and him?"

red @sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."

yellow -unamusedbrow @sadbrow talkingmouth "I'm... sorry, [first_name]. I know your heart's in the right place, but this doesn't really have anything to do with you."

red @sadbrow talkingmouth "At least hear me out. He told me that he had a serious conversation with you, Ethan. Like, a really meaningful one."

ethan @closedbrow talking2mouth "That's a matter of opinion."

red @talking2mouth "And then he said that his Eevee threw up the Foreverals, and..."
red @closedbrow talking2mouth "You guys thought he was just 'faking' the connection to get the stones."

ethan @confused "Are you saying that's not what happened?"

red @talking2mouth "Sam and I don't... {i}really{/i} understand how the power works, yet."
red @sadbrow talkingmouth "But I don't think that should even be possible. I think the fact the stones showed up means he really did have a connection with you--a connection that meant something to him."

if (len(claimedforeverals) > 0):
    red @happy "At least, that's how it's worked for [pika_name] and I."

else:
    red @talking2mouth "Speaking theoretically, of course. I haven't actually managed to make any solid, usable, Foreverals myself, yet."

pause 1.0

ethan @talking2mouth "...Okay."
ethan @talkingmouth "Cool. I believe ya."

redmind @happy "See, Blue? What did I say? Told you it was that easy."

ethan @closedbrow talking2mouth "Doesn't mean I'm not still mad at him, though."

red @confused "...Oh. I mean, okay, fair. But, why?"

ethan @talkingmouth sadbrow "C'mon. He stomps around this dorm like he's trying to shake the pictures off the walls of the room below us."
ethan @closedbrow talkingmouth "I've always been the guy who defends him whenever you say something bad about him, but he doesn't bother to remember my name half of the time."
ethan @talking2mouth "He makes me feel like that party member that's mandatory in a bunch of story segments, but no-one actually wants to use."
ethan @upeyes talking2mouth "But, I mean, that's just me whining. You've seen how he treats Yellow, right?"
ethan @sad2eyes sadeyebrows talking2mouth "Go on, Yell'. Tell him."

yellow @talkingmouth "...I've given him so much of my time and energy. And all I want is a little thanks. But... he'll never give me that. Not even a kind smile, or a warm hand."
yellow @sadbrow talkingmouth "I don't want to keep going through this cycle of him taking me for granted, then I get mad at him, then he does something big to make up for it, then I forgive him, then he takes me for granted again."
yellow @closedbrow talkingmouth "I don't want to be saved. I just want to be safe."

ethan @talkingmouth "So, like, sure, maybe we were wrong about this {i}one{/i} time, but... can you blame us for assuming the worst?"

yellow @angrybrow talkingmouth "No! I didn't assume the worst! I... I wanted to believe in him! I really did!"
yellow @sadbrow talkingmouth "{size=30}I was just... too tired.{/size}"

ethan @sadbrow talkingmouth "...I know, Yell'. Sorry. Shouldn't have spoken for you."
ethan @unamusedbrow talking2mouth "But, yeah, no, I absolutely assumed the worst."
ethan @closedbrow talking2mouth "And you can't really blame {i}me{/i} for that, after everything Blue has given us to work with."

yellow @sadbrow talkingmouth "I was waiting for him to... to talk with us... But he never came. He hasn't said a word to me in four days."

ethan @upeyes angryeyebrows talking2mouth "And then he sends {i}you{/i} to sort this out for him?"
ethan @angrybrow talking2mouth "Honestly, the more I think about this, the more pissed off I get. Like, he's trying to {i}use{/i} your friendship power to ignore the problem."
ethan @sad2eyes talking2mouth angryeyebrows "If I was you, I'd be pissed, too."

pause 1.0

redmind @sadbrow frownmouth "I... honestly hadn't thought of it like that. But... come to think of it... yeah."
redmind @angryeyebrows frownmouth "Yeah, he {i}is{/i} trying to use me, isn't he? Why {i}shouldn't{/i} I be pissed?"
redmind @angrybrow frownmouth "He can solve his own problems. I've had enough problems with people hating me for my power--I don't want the people who {i}don't{/i} hate me for it to use it!"

red @angry "You know what? Actually--"

show ethan surprisedbrow:
    xpos 0.33
    ease 0.2 xpos 0.1 rotate -15
    pause 0.5
    ease 0.5 xpos 0.25 rotate 0
show yellow surprisedbrow:
    xpos 0.66
    ease 0.2 xpos 0.9 rotate 15
    pause 0.5
    ease 0.5 xpos 0.75 rotate 0

show blue scaredbrow frownmouth:
    xpos 1.2 xzoom -1
    ease 0.5 xpos 0.5

show suitenight with vpunch

blue @talkingmouth "{size=40}I'm sorry!{/size}"

pause 1.0

ethan @confused "Huh?"

show blue scaredbrow frownmouth:
    xzoom -1
    ease 0.5 xzoom 1

blue wistfulbrow @closedbrow talkingmouth "I'm... sorry."

pause 0.5

yellow -surprisedbrow @closedbrow talkingmouth "{size=30}Here I go again...{/size}"
yellow @sadbrow talkingmouth "What are you sorry for, Blue?"

blue @talkingmouth "I'm... sorry for taking you for granted."
blue @angry "But I {i}promise{/i}--"

yellow @sadbrow happymouth "Don't, Blue. Don't promise. I don't need grand gestures. I don't need oaths. I don't need vows. I just need..."
yellow @sad "{w=0.5}.{w=0.5}.{w=0.5}."

blue @talkingmouth "I... will try harder. I, uh, I {i}do{/i} appreciate you."
blue @closedbrow talkingmouth "And, uh, I mean it this time."

yellow @closedbrow talkingmouth "Thank you. Now, it's Ethan's turn."

show blue:
    xzoom 1
    ease 0.5 xzoom -1

show ethan -surprisedbrow with dis

blue @talkingmouth "I'm sorry to you, too. I wasn't trying to get the stones. Until..."
blue @wistfulbrow talkingmouth "Until I did, I didn't think I could ever get you enough to even get the stones, anyway."
blue @talkingmouth "But I do. Get you. More than I did, anyway. And, since I get you..."
blue @closedbrow talkingmouth "I get why you'd be mad. Which is, uh..."

pause 1.0

blue @closedbrow talkingmouth "'Fair.'"
blue @talkingmouth "...But I {i}do{/i} remember your name. Even if I just sometimes call you 'You', or whatever."

pause 1.0

ethan @talking2mouth "...Fine."

blue @surprisedbrow talkingmouth "Huh? ...Is that it?"

ethan @talkingmouth "Don't know what you want me to say, man. I've only known you for two months, and you've been a massive PITA for both of them."
ethan @talkingmouth "I defended you because I'm a contrarian, not because I actually disagreed with anything anyone was saying."
ethan @talking2mouth "You're not turning me around in a single conversation."

blue @closedbrow talkingmouth "That's fair."

pause 1.0

blue @surprised "Wait!"
blue @happy "Oh, this is great! I got it!"
blue -wistfulbrow -frownmouth @talkingmouth "Here! Take this!"

red @surprised "Wait... are those...?"

blue @closedbrow talkingmouth "Yeah, Foreverals."

redmind @unamusedbrow unamusedmouth "...I'm never going to be able to pay for this school, am I?"

yellow @surprised "This power..."

ethan @surprised "Dude! You're just {i}giving{/i} them to us?"

blue @closedbrow talkingmouth "They only work on Pichu. And it's not like I'm going to use one of those electric rats you three use."

ethan @talkingmouth "...Okay. Uh, how do we give them to our Pokémon?"

red @closedbrow talking2mouth "You just kinda push them on. They kinda sink into the Pokémon. Like one of those stick-on gems you buy at craft stores."

yellow @talkingmouth "This... doesn't hurt the Pokémon?"

red @closedbrow talking2mouth "No. The Pokémon can just release them whenever they want."

ethan @talking2mouth "You don't look enthused?"

red @talking2mouth "Well, as I {i}may have{/i} mentioned once or twice, I'm completely broke."
red @closedbrow talking2mouth "I was hoping that I could sell these Foreverals to Champions to pay for my tuition--which becomes harder if someone's giving them away for free."

if (investment >= 2000):
    redmind @thinking "Geez, I sound like Gardenia..."

blue @closedbrow talkingmouth "Relax. It's only two more. You think I'm really going to hand these out to anyone else?"

red @sad2eyes sadeyebrows talking2mouth "No. But... I'm still worried."

ethan @closedbrow talking2mouth "So I hate to admit this, but giving me a shiny one-of-a-kind Pokémon-enhancing gem {i}has{/i}, kind of, helped patch things over."
ethan -frownmouth @confused "Of course, I don't know what it does, yet... if it's something lame, like making my Pichu turn Normal-type or whatever, I'll be pretty pissed."

blue @happy "Hah. I guarantee it won't be. {i}My{/i} Foreverals are way better than whatever trash [first_name] generates! I mean, the Champions won't even want to buy from him when they see what I can do!"

red @closedbrow talking2mouth "Don't even joke about that."

blue @talkingmouth "C'mon. Let's go to the gym. It's late enough it should be mostly empty, and we won't have to run back from the Battle Hall when curfew gets too close."

ethan @talkingmouth "I'm game."

pause 0.5

show blue:
    xzoom -1
    ease 0.5 xzoom 1

blue wistfulbrow frownmouth @wistfulmouth "Amarillo?"

yellow @closedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

show blue kindeyes smilemouth with dis

yellow sadbrow happymouth "Of course."

scene blank2 with splitfade

pause 1.0

scene gym 
show ethan:
    xpos 0.25
show blue
show yellow neutrallowponytail:
    xpos 0.75
with splitfade

ethan @talkingmouth "Alright... Pichu equipped. Let's see what this rock does."

yellow @closedbrow talkingmouth "Blue, I'll battle you. Please go easy on me."

$ autoquote = False

blue @happy "\"Hah! I--"
extend @closedbrow sweat talkingmouth "uh, yeah, will go easy on you.\""

$ autoquote = True

ethan @happy "Guess we're paired, then. Oh, yeah, what kind of battle are you thinking?"

menu:
    "Singles, chum.":
        $ battletype = 1

    "Doubles, buddy.":
        $ battletype = 2

    "Triples, confidant.":
        $ battletype = 3

ethan @talkingmouth "Sounds good... let me just rearrange my team."

pause 0.5

ethan @happy "Alright, ready!"

red @happy "Let's go!"

show blue:
    xpos 0.5
    ease 0.5 xpos 0.25

python:
    trainer1 = MakeRed(battletype)
    trainer2 = MakeTrainer("Ethan", number=battletype)

call Battle([trainer1, trainer2], dialogfunc=firstpichubattle) from _call_Battle_164
$ RecordBattle("Ethan2")

show ethan with dis

if (WonBattle("Ethan2")):
    $ ValueChange("Ethan", 3)

    ethan @talkingmouth "Nice going. Guess I gotta spend some time grinding before I'm hitting your numbers."

    red @happy "It's just practice. That wasn't bad, for your first time using Foreverals."

    ethan @closedbrow talking2mouth "But I feel, actually, like... Pichu got a bit stronger, didn't she? I mean, compared to how she was before the battle."

    red @talkingmouth "You're her trainer. You tell me."
    ethan @talkingmouth "Yeah, I think that's it."

    ethan @closedbrow talking2mouth "...Kinda funny that Blue ended up giving us Foreverals before you, huh?"

    red @surprisedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    ethan @confused "Wait, did you not think of that?"

    red @lightblush sad2eyes talking2mouth "Let's... talk about something else."

else:
    if (HasEvent("Ethan", "SawPichu")):
        ethan @happy "Nice. Looks like the power-up worked."

        if (HasEvent("Ethan", "KOPichu")):
            ethan @talkingmouth "I mean, you knocked her out, but... still, vibes, you know?"

    else:
        ethan @unamusedbrow talking2mouth "Dude... I didn't even send Pichu out."

        red @closedbrow talking2mouth "I... didn't {i}mean{/i} to lose."

        ethan @closedbrow talking2mouth "Yeah, well. Just kinda anticlimactic, isn't it?"
        ethan @closedbrow talkingmouth "I think, if I {i}had{/i} used her, she probably would have been a bit stronger, stats-wise, and had some cool new moves..."
        ethan @unamusedbrow talking2mouth "But I guess we can't know for sure."

        red @upeyes angryeyebrows talking2mouth "Alright, alright, I get it."

        ethan @closedbrow talking2mouth "You're probably just trying to get all the dialogue, aren't you? In all likelihood, you're only reading this dialogue from the script files. No way you'd {i}actually{/i} throw against me."

        red @unamusedbrow talking2mouth "Dude."

        ethan @happy "Alright, I'm done. And I gotta admit, it's fun to win once in a while."

ethan @talking2mouth "Anyway, Yellow, what's up with your Foreveral? What does that one do? Same thing?"

yellow frownmouth @sadbrow talkingmouth "Um..."

blue frownmouth @closedbrow talkingmouth "We couldn't get it to trigger."

red @confused "Huh? I've never had problems triggering Foreverals before."

ethan @talkingmouth "Yeah, and I didn't have any problems just now, either."

yellow @closedbrow talkingmouth "The stone just won't... it won't {i}stick{/i} to Chuchu."

red @confused "Oh. That's... weird."

narrator "True to Yellow's word, when she presses the Foreveral to Chuchu, it refuses to make any sort of connection."

$ sidemonnum = 172
$ PlaySound("pokemon/cries/172.mp3")

sidemon @talkingmouth "Chu..."

red @confused "Well, I'm stumped."

blue @closedbrow talkingmouth "Maybe Chuchu's too weak to handle it?"

yellow @closedbrow talkingmouth "You train my Pokémon, Blue. Isn't it the same training you've given your Eevee?"

blue @happy "Hah! I train {i}my{/i} Pokémon (and Leaf's Dratini) by putting them through the grinder, sending them up against massive amounts of foes, and pushing them to their absolute limit." 
blue @talkingmouth "I train {i}your{/i} Pokémon by giving them softball opponents that they're never in any actual danger from."

yellow @surprised "Wh... why?"

blue @surprised "Wait, you didn't know? I thought you didn't want your Pokémon to evolve. That kind of training is ideal for building up a Pokémon's energy without causing them to want to evolve."
blue @talkingmouth "It's called 'Soft-hand Training'. Normally people who want to train their Pokémon for fun, but only to keep them as pets, use it."

yellow -frownmouth @talkingmouth "Oh. Well, yes, that's correct."

blue @closedbrow talkingmouth "If you {i}do{/i} want your Pokémon to evolve, just let me know. I can do that, too."
blue @talkingmouth "Maybe evolution would make your r--{w=0.5}{i}Chuchu{/i} strong enough to handle that Foreveral."

red @talkingmouth "We can ask your grandfather about it. He might have some theories."

blue -frownmouth @closedbrow talkingmouth "Yeah."

redmind @confusedeyebrows frownmouth "That's interesting, though... Yellow doesn't want her Pokémon to evolve? Why would that be?"

pause 1.0

ethan @talkingmouth "Alright. Don't know about you guys, but I'm bushed. It's almost curfew, after all, so let's get back to the dorm ASAP."

red @talkingmouth "Right with you."

hide yellow
hide ethan 
with dis

pause 1.0

show blue:
    xpos 0.25 xzoom 1
    ease 1.0 xpos 0.5
    pause 1.0
    ease 0.5 xzoom -1
    pause 1.0
    ease 0.5 xzoom 1
    pause 1.0

pause 5.0

blue happy "{size=30}Yes!{/size}"

scene blank2 with splitfadefast

call texting from _call_texting_28

jump day010528
