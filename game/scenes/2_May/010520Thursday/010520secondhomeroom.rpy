label secondhomeroom010520:

scene blank2 with splitfade

pause 1.0

stop music fadeout 1.5
queue music "audio/music/celebi_start.ogg" noloop
queue music "audio/music/celebi_loop.ogg"

scene homeroom 
show screen currentdate
show kris angrymouth angrybrow
with splitfade

pause 3.0

redmind uniform @confusedeyebrows frownmouth "Professor Cherry's just been staring at us for the past three minutes, holding a sheet of paper tightly in her hands."

if (GetRelationshipRank("Professor Cherry") > 0):
    redmind @thinking "Wait a minute. I've been spending a while investigating her, so I've started to learn a bit about how she presents herself, and... right now..."

    redmind @surprised "She's scared. Her hands are shaking."

    pause 1.0

    red @talkingmouth "Hey, {i}Leaf!{/i}"

    leaf uniform @talking2mouth "Uh, yeah?"

    show kris surprisedbrow with dis

    red @happy "I've never felt more prepared for a test before in my life. What about you?"

    pause 1.0

    show kris sadbrow -angrymouth with dis

    $ ValueChange("Kris")

    leaf @talking2mouth "Uh, yeah, I feel pretty prepared. Why are you asking?"

    red @talkingmouth "Just curious."

else:
    redmind @thinking "...I guess she's nervous about how this test will go." 
    redmind @thinking "She didn't really have time to prepare us properly for the last one, but she has for this one, so this test will determine if she could salvage something out of Professor Oak's class."    

kris -angrymouth -sadbrow @closedbrow talkingmouth "...It's time. This isn't a midterm, or a final exam, or anything of that nature, so don't stress out about it."

redmind @happy "Lead by example, Professor!"
redmind @sadbrow frownmouth "But... on the other hand... it's obvious to see how much she cares. I hope I don't let her down."

kris @talking2mouth "One last thing. If you see a move or ability you don't recognize--you're allowed to use your phones. There's no shame in looking it up."

redmind @happy "Hm. That's nice. I've memorized most moves and abilities, but it might be a nice refresher for the other students."

whitney @closedbrow talkingmouth uniform "{size=30}Oh, thank god.{/size}"

kris @talking2mouth "Take out your writing implements, students."
kris @talkingmouth "Remember that [bluecolor]this is a graded test.{/color} Take it seriously."
kris @talking2mouth "All you need to know is that [bluecolor]the opponent Togekiss does {i}not{/i} have Hustle or Serene Grace.{/color}"

pause 0.5

kris @happy "I believe in you."

python:
    trainer1 = Trainer("red", TrainerType.Player, [
        Pokemon(264.1, level=45, moves = [GetMove("Switcheroo"), GetMove("Night Slash"), GetMove("Counter"), GetMove("Leer")], ivs=[0, 0, 0, 0, 0, 0], ability = "Quick Feet", item="Scope Lens"),
        Pokemon("Ariados", level=50, moves = [GetMove("Sticky Web"), GetMove("Shadow Sneak"), GetMove("Night Shade"), GetMove("Cross Poison")], ivs=[0, 0, 0, 0, 0, 0], ability = "Insomnia"),
        Pokemon("Grafaiai", level=45, moves = [GetMove("Poison Jab"), GetMove("Taunt"), GetMove("Doodle"), GetMove("Slash")], ivs=[0, 0, 0, 0, 0, 0], ability = "Prankster")
    ], number=3)

    trainer2 = Trainer("kris", TrainerType.Enemy, [
        Pokemon("Togekiss", level=40, moves = [GetMove("Air Cutter")], ivs=[0, 0, 0, 0, 0, 0], ability = "Super Luck")
    ])

    trainer1.GetTeam()[0].Health = 1
    trainer1.GetTeam()[0].ChangeStats(Stats.Attack, -6)
    trainer1.GetTeam()[1].Health = 1
    trainer1.GetTeam()[1].ChangeStats(Stats.Attack, -6)
    trainer1.GetTeam()[2].Health = 1
    trainer1.GetTeam()[2].ChangeStats(Stats.Attack, -6)
    trainer2.GetTeam()[0].ChangeStats(Stats.Defense, 6)
    trainer2.GetTeam()[0].ChangeStats(Stats.SpecialDefense, 6)
    trainer2.GetTeam()[0].ChangeStats(Stats.Speed, -6)

call Battle([trainer1, trainer2], gainexp=False, healParty=False, clearstats=False, uniforms=[True, False], lockbag=True, lockluck=True) from _call_Battle_148
$ RecordBattle("Kris2")

stop music fadeout 1.5
queue music "audio/music/celebi_start.ogg" noloop
queue music "audio/music/celebi_loop.ogg"

if (WonBattle("Kris2")):
    redmind uniform @happy "There we go. I'm pretty confident in my answers for this."

else:
    red uniform @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
    redmind @sadbrow frownmouth "I'm so sorry, Professor Cherry. I {i}really{/i} tried."

pause 2.0

show kris sadbrow angrymouth with dis

narrator "There's a pregnant pause as the last person stands up and delivers their paper to Professor Cherry's desk."

kris @talkingmouth "...You can leave now, if you want."

pause 2.0

show hilbert uniform with dis:
    xpos 0.75

hilbert @talkingmouth "None of us are moving an inch until we know how we did."

show flannery uniform with dis:
    xpos 0.25

flannery @talking2mouth "That's right, Doc. I even went to sleep early the past few days so I wouldn't be so exhausted for the morning lectures."

show whitney uniform with dis:
    xpos .125

whitney @happy "Coming from Flannery, that really means a lot!"

show may uniform:
    xpos 0.875

show kris surprisedbrow with dis

may @sadbrow talkingmouth "I studied harder for this test than I ever have before, Professor. Professor Oak's quizzes have always been a bit touch-and-go for me, but I didn't want to let you down."

show dawn uniform behind flannery with dis:
    xpos 0.35

dawn @sadbrow talkingmouth "I-- I really appreciate everything you've done for us. And, um, I didn't want you to feel like your efforts were wasted."
dawn @closedbrow sadmouth "S-so... I paid attention! I actually cared about what was being taught! And I--I think I did alright!"

show leaf uniform with dis:
    xpos 0.65

leaf @talking2mouth "You've been building this up all week, Doctor Cherry. No way we can just go to sleep and find out our grades tomorrow morning, like normal."

pause 1.0

kris sadbrow -angrymouth @talkingmouth "You are all... {i}excellent{/i} students."
kris @closedbrow talkingmouth "I hear you loud and clear."
kris angrybrow @happymouth "Let the grading commence!"

narrator "Kris finally looks directly at the stack of tests and pulls out a red ballpoint pen."

kris @talking2mouth "Flannery Moore--{w=1.0}{nw}"
show blank
pause 0.1
hide blank
show flannery happy
extend @happy "Passed!"

kris @talking2mouth "Hilbert von Schwarzdrachen--{w=1.0}{nw}"
show blank
pause 0.1
hide blank
show hilbert closedbrow smilemouth
extend @happy "Passed!"

kris @talking2mouth "Whitney Milton--{w=1.0}{nw}"
show blank
pause 0.1
hide blank
show whitney happy lightblush
extend @happy "Passed!"

kris @talking2mouth "Leaf Green--{w=1.0}{nw}"
show blank
pause 0.1
hide blank
show leaf happy
extend @happy "Passed!"

kris @talking2mouth "May Birch--{w=1.0}{nw}"
show blank
pause 0.1
hide blank
show may happy
extend @happy "Passed!"

if (WonBattle("Kris2")):
    kris @ talking2mouth "[first_name] [last_name]--{w=1.0}{nw}"
    show blank
    pause 0.1
    hide blank
    $ ValueChange("Kris", 3)
    extend @happy "Passed!"

show blank2 with Dissolve(3.0)

narrator "This goes on for a while, with Professor Cherry reading the names of all the students who passed."
narrator "Occasionally, she will flip a page over and just wince, skipping to the next test."

if (not WonBattle("Kris2")):
    narrator "You, notably, do not hear your name..."
else:
    narrator "But not often.{w=0.5} Not often at all."

hide blank2 
hide leaf
hide whitney
hide may
hide dawn
hide hilbert
hide flannery
with dis

kris sadbrow @talkingmouth "Incredible work, everyone. I'm so proud of you. Over 95%% of you passed."
kris @happy "That's {i}extremely{/i} good... for this class. But for any class, really. I {i}knew{/i} you were all great students."

flannery uniform @happy "We couldn't've done it without you, Doc."

pause 1.0

kris "{w=0.5}.{w=0.5}.{w=0.5}."

kris @talkingmouth "Tomorrow... we'll do something special. Bring your best battling Pokémon to class, okay?"

$ PlaySound("bellchime.ogg")

kris happy "I'll see you all then."

stop music fadeout 1.5

call clearscreens() from _call_clearscreens_188
show blank2 with splitfade

narrator "By asking around, you are able to find directions to the Cooking Club's clubroom."

scene cookingkitchen 
show screen currentdate
with splitfade

queue music "audio/music/alolaencounter_intro.ogg" noloop
queue music "audio/music/alolaencounter_loop.ogg"

pause 1.0

red @surprisedbrow frownmouth "...Huh."

redmind @confusedeyebrows frownmouth "This clubroom looks almost exactly like Mom's kitchen in Pallet Town."
redmind @thinking "Just with {i}way{/i} more expensive equipment."

show mallow with dis

mallow surprisedbrow frownmouth @happy "Alola! Welcome to the Cooking Club!"

red @happy "Happy to be here! Where's everyone else?"

mallow -surprisedbrow @blush sadbrow poutmouth "{w=0.5}.{w=0.5}.{w=0.5}."

red @sweat talkingmouth "Oh, wait, is it just you?"

mallow @talkingmouth "Um... the Head Chef is here, too... sometimes."

red @talkingmouth "Oh, right, you said you were the Sous-Chef. That means second-in-command, right?"

mallow -frownmouth @talkingmouth "Oh, good, so you know a bit about the kitchen!"

red @happy "My Mom used to rope me into the cooking. She'd put on a fancy Kalosian accent and refer to me as 'Signore Der Chef.'"

mallow @happy "Wow! That's very wrong, but it's still cute!"

red @talkingmouth "Yeah, we had fun."
red @talkingmouth "So, uh, mind if I just get started? I think I can handle a basic cake."

mallow @surprisedbrow talkingmouth "Oh! Like... um... alone?"

red @confusedeyebrows talking2mouth "Yyyy...{w=0.5} ...no?"

mallow @happy "Great! I'm happy to help! It's no problem! An Alolan will {i}always{/i} help someone in their home!"

redmind @sadbrow frownmouth "I think she might be a bit lonely. No wonder she tried so hard to get me to join."

show blank2 with splitfade

mallow @closedbrow talking2mouth "Okay, so this is the oven. This is where you put the cake after you've mixed the ingredients together. In order to do that, you're going to want to whisk--"

red @happy "I know what an oven is! {i}And{/i} a whisk!"

narrator "Despite Mallow's clear disbelief in your cookery skills, you eventually manage to make a fairly-decent cake that should serve about twenty people, and put it in the oven."
narrator "You have to admit that Mallow clearly has more experience in the field than you, but you manage to hold your own."

hide blank2 with splitfade

mallow @surprised "Wow! You actually know what you're doing!"

red @happy "Told ya."

mallow @sadbrow talkingmouth "I'm sorry! I've just never known a guy who could so much as boil an egg without burning it."

red @confused "That's..."

narrator "You think back to some of the breakfasts you had back in Dorm 151, where you were quickly appointed 'the only person in the dorm who can make a satisfying meal.'"

red @closedbrow talking2mouth "...Probably accurate more often than not."

red @talkingmouth "Anyway, the individual layers should each take about half an hour to cook, so we've got some time."
red @talkingmouth "Maybe you could tell me what you know about my Pikachu, now?"

$ renpy.music.play("Audio/Pokemon/pikachu_happy2.ogg", channel="altcry", loop=None)
libpikachu happy "Pika!"

mallow @talkingmouth "Sure! I've gotta say, I'm surprised he's such a cute and friendly little guy. He's nothing at all like the folklore says."

$ PlaySound("idea.ogg")

red @confused "Beg pardon?"

$ renpy.music.play("Audio/Pokemon/pikachu_confused.ogg", channel="altcry", loop=None)
libpikachu confusedeyes surprisedmouth "Pika?"

mallow @surprisedbrow frownmouth "...Oh, you don't know?"

red @talkingmouth sweat "That's practically the title of my autobiography."

mallow frownmouth @talking2mouth "Oh."

pause 0.5

mallow @talkingmouth sadbrow "Maybe I shouldn't tell you this, then--I'm not sure it's something you'd want to hear."

red @talkingmouth "Hey, maybe not, but we're at school to learn uncomfortable truths, right? Lay it on me."

mallow @talkingmouth "Okay."
mallow @talkingmouth "So, you may know Alola is a proud nation of four islands. Thousands of years ago, each of these islands had a king."

red @talkingmouth "Sure."

mallow @happy "These kings had a pact of protection with each other--if any of their islands would be attacked, then the other kings, their armies, and their partner Tapus would come to their aid."
mallow @surprised "Oh, right, the Tapus are the guardian deities of the islands."

red @happy "I know."

mallow @happy "Oh, do you know Alolan folklore as well?"

red @talkingmouth "Nah, but I know Pokémon."

mallow @angrybrow talking2mouth "...The Tapus are {i}way more{/i} than just Pokémon."

red @happy "My bad."

mallow @happy "It's alright. We Alolans are {i}famously{/i} forgiving."
mallow @talkingmouth "Anyway, this was in, um, the 1600s. So, like... 1200 years since the third Unovan Civil War, I think, when they overthrew their kings."

red @closedbrow talking2mouth "Uh, sorry, I think I'm missing some historical context."

mallow @talking2mouth "Oh. Well, I don't really know much about {i}their{/i} history. I think they had two dragons fight each other, and the dragons ruined the country, so the people got angry and overthrew the kings."

red @talking2mouth "Oh, I think I heard about that. And then they installed a President, right? And then that President had a Pikachu like [pika_name]."

$ renpy.music.play("Audio/Pokemon/pikachu_happy1.ogg", channel="altcry", loop=None)
libpikachu @closedbrow happymouth "Pi! Pika!"

mallow @talkingmouth "That's right. And everything was fine for a while. But as the Unovans cycled through presidents, their policies changed, and then..."
mallow @angrybrow talkingmouth "Boom! The Unovans invaded!"

red @surprised "Huh? Who?"

mallow @talking2mouth "Alola, of course."

red @closedbrow talking2mouth "Oh."

mallow @talking2mouth "There were a bunch of factors, but basically the Unovans wanted our land to create banana farms."
mallow @talking2mouth "The biggest thing was that we had kings, though. The Unovans didn't like that."

red @confused "Were your kings, like, corrupt or evil or something?"

mallow @talkingmouth "They're historical figures, so it's hard to know objectively, but... nothing in {i}our{/i} history says they were."

mallow @talking2mouth "So the Unovans attacked our shores, intent on 'liberating' us from our kings."
mallow @sad "Our kings rode out to meet them, astride their Water-type Pokémon, their partner Tapus behind them."
mallow @talkingmouth "They knew they didn't have a chance. The Unovans were backed up by an impossibly large force of Liberation Pikachu."

red @talking2mouth "Right..."

mallow @talkingmouth "From what the kings knew, the battle was a foregone conclusion. The Liberation Pikachu had strange and unnatural powers."
mallow @talkingmouth "They could copy the abilities of their allies, and even their enemies. They could summon warrior spirits to aid them in battle, and were even able to strike with the force of the Mega-Evolved Pokémon from Kalos."

red @talkingmouth "So they thought they'd already lost when they rode out to fight the Unovan Navy."

mallow -frownmouth @talkingmouth "Yep. But the Deities urged them to fight anyway, so they did."
mallow @talkingmouth "And this is the strangest thing. During the fight, apparently, none of the Liberation Pikachu used their powers. It seemed as though they were entirely unwilling to fight--or almost like they {i}couldn't{/i}, for some reason."

red @surprised "Really? They just refused to fight?"

mallow @talkingmouth "That's what the folklore says."
mallow @happy "So then the Guardian Deities absorbed their Z-Power from the kings, and turned into four giant, glowing, golden, Guardians of Alola!"
mallow @happy "The stories say their legs straddled the islands like a colossus!"

red @unamusedeyes unamusedmouth unamusedeyebrows "{w=0.5}.{w=0.5}.{w=0.5}."
red @talking2mouth "Okay, so, this is the part where history becomes mythology, right?"

mallow @talking2mouth "Oh, no, this really happened."

redmind @thinking "Well, I believe she {i}thinks{/i} it happened."

mallow surprisedbrow frownmouth @happy "And then, in a single, mighty, blow, the four Guardians wiped out 75%% of the attacking Unovan Navy!"

red @happy "Good for them! And what about the Liberation Pikachu?"

pause 1.0

mallow -surprisedbrow @sadbrow talkingmouth "Well... the Unovans were coming by boat. And, um, Pikachu can't swim super-well... so..."

red @surprised "Oh."

mallow @talkingmouth "The ones that survived didn't have enough of a breeding population left, and, um, apparently when two Liberation Pikachu breed, there's no guarantee that the resulting Pichu will even become a Liberation Pikachu, so..."

pause 1.0

red @talkingmouth "So that's how they went extinct."

mallow @talking2mouth "...Yep."

pause 1.0

red @happy "Is this the part where you say 'we Alolans are famously good at winning wars'?"

mallow -frownmouth @happy "Hah, no! I'm proud of my home region, but I'm not {i}that{/i} callous."

$ renpy.music.play("Audio/Pokemon/pikachu_angry1.ogg", channel="altcry", loop=None)
libpikachu @angrybrow frownmouth "Pika..."

mallow frownmouth @sadbrow talkingmouth "Sorry, little guy."

red @talkingmouth "Just give him a scratch behind the ears. He'll forgive anything after that."

mallow -frownmouth @happy "Oh, okay!"

show mallow:
    xpos 0.5 ypos 1.0 zoom 1.0
    ease 0.5 xpos 0.35 ypos 1.1 zoom 1.2

pause 1.0

$ renpy.music.play("Audio/Pokemon/pikachu_sad.ogg", channel="altcry", loop=None)
libpikachu @closedbrow talking2mouth "Pika."

show mallow:
    xpos 0.35 ypos 1.1 zoom 1.2
    ease 0.5 xpos 0.5 ypos 1.0 zoom 1.0

mallow @talkingmouth "Thanks for letting me talk your ear off."

red @talkingmouth "Hey, I think I benefited more. I didn't know any of that stuff about [pika_name]. Sonia's got the biology part covered, but I was completely lost on the history part."

mallow @happy "I'm serious! I never get the chance to talk to anyone about Alolan history. Or cooking, actually."
mallow @talkingmouth "There was an incident a few years ago, and now there are barely any Alolans at this school... and Instructor Olivia just depresses me. Plus, I can't get anyone to join the club."
mallow @blush sadbrow talkingmouth "I mean, you can see how much activity the club gets... we've been here for hours, and nothing's happened."

red @closedbrow talking2mouth "Really? What about the Head Chef?"

mallow @talkingmouth "...He has a lot going on. He doesn't often show up. It's only been a couple weeks, though, so hopefully we'll get to see him more, later, when he clears out his schedule."
mallow @happy "I think he has a few too many hobbies, but he's the best chef I've ever met, so I'm willing to put up with it."
mallow @closedbrow talking2mouth "And he {i}somehow{/i} secured the funding for this massive clubroom, and all the ingredients, despite the fact this is a club of one person..."

red @talkingmouth "Well, I'll have to drop by to keep you company once in a while. Don't want all this funding to go to waste."

mallow @happy "That'd be great!"
mallow @talkingmouth "It's not like we're hurting for funding, but we also have a selection of PokéTreats that we sell to other students. The Head Chef makes them himself."
mallow @happy "Oh, you're free to buy some yourself, of course."

if (not HasEvent("Dawn", "UsedGummyWyrms")):
    red @confused "PokéTreats?"

    mallow @talkingmouth "They're a special kind of Pokémon food that lure wild Pokémon of a specific type to your location."
    mallow @surprised blush "They're not edible by humans, though! Don't try it! No matter how delicious they smell!"

mallow @talkingmouth "Would you like to see our collection? Every PokéTreat is $1,000, but last a long time, no matter how many Pokémon you attract, or how long you stay out."

$ boughttreat = False

label treatshop:

menu:
    "Sure.":
        call screen shopkeep(treatitems)
        $ boughtitem = _return
        if (boughtitem == "Back"):
            pass
        else:
            $ totalcost = boughtitem[0] * boughtitems
            if (totalcost > money):
                narrator "You can't afford that!"

                jump treatshop

            else:
                $ AddEvent("Mallow", "BoughtTreat")
                $ itemname = GetItemName(boughtitem[1])
                $ money -= totalcost 
                if (boughtitems > 1):
                    narrator "You bought [boughtitems]x [itemname] for $[totalcost]!"
                else:
                    narrator "You bought [itemname] for $[totalcost]!"
                $ GetItem(itemname, boughtitems)
                $ boughtitems = 1

            mallow @talkingmouth "Great! Want any more?"

            jump treatshop

    "Nah, I'm good.":
        mallow @happy "Alright. If you ever change your mind, though, just come back here to the Student Center! I'll usually be in the kitchen."

    "I'm broke." if (money < 1000 and not boughttreat):
        mallow @surprised "Oh!"

        mallow @happy "Then here, take this one for free! Call this an Alolan's generosity!"

        $ highestelective = GetStatRank(0)

        python:
            for key, value in treatboosts.items():
                if (value == highestelective):
                    GetItem(key)
                    break

        red @happy "I definitely will. Thank you!"

pause 2.0

$ PlaySound("idea.ogg")

mallow @surprised "Oh! Your cake is done!"
mallow sadbrow @talkingmouth "I guess... that means you're leaving, then...?"

pause 1.0

show mallow surprisedbrow frownmouth with dis

red @happy "What are you talking about? I've still got to decorate it, don't I? I'll be here for another hour, at least."

show mallow sadbrow -frownmouth blush with dis

red @happy "C'mon. Give me a hand."

call clearscreens() from _call_clearscreens_189
scene blank2 with splitfade

call freeroam from _call_freeroam_27

call texting from _call_texting_22 

jump day010521