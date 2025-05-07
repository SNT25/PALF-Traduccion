label secondhomeroom010524:

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

pause 0.5

oak @talkingmouth "As you may recall from our first class, Baron Lawrence Phobos III mentioned his niece would be joining us for this class..."

pause 1.0

oak @sadbrow talkingmouth "I'm afraid... I don't see you. Miss Phobos III, would you please stand up?"

hilbert uniform @talkingmouth "{size=30}That's not how titles work...{/size}"

pause 1.0

show oak surprisedbrow frownmouth with dis

show homeroom:
    xalign 0.0 zoom 1.0
    ease 0.5 xalign 0.1 zoom 1.3
    pause 1.0
    ease 1.0 xalign 0.9
    pause 1.0
    ease 2.0 xalign 0.0 zoom 1.0

pause 3.0

oak @talking2mouth "Er... is she not here?"

blue uniform @closedbrow talkingmouth "{i}I{/i} don't see her."

whitney uniform @talkingmouth "Yeah, there's no-one new here, Professor."

oak -surprisedbrow -frownmouth @closedbrow talking2mouth "Well, I suppose I'd better get started, then. I want to give you as much time for the exam as possible."
oak @talking2mouth closedbrow "{size=30}Let's see... I was talking about coverage... ah, yes.{/size}"

pause 0.5

oak @talkingmouth "One often wants their coverage moves to cover a wide array of possible opposing types, hitting as many Pokémon for at least neutral damage as possible."
oak @talkingmouth "Electric and Ice, and Ground and Rock, are particularly reliable combinations, as exemplified through the combinations of Thunderbolt and Ice Beam, and Earthquake and Stone Edge, respectively."
oak @talkingmouth "Another technique that cannot be ignored when speaking of coverage moves is Hidden Power. Being a move learnable by almost every Pokémon, it is also a move that can be any type."

pause 0.5

oak @closedbrow sweat talking2mouth "Curiously, a Fairy-typed Hidden Power has not been able to manifest in some regions... but in Kobukan, it's been observed commonly. Frankly, we're not sure why."
oak @talking2mouth "There are theories that Hidden Power draws its power from the 'Hidden Legends' of a region, or Pokémon of immense power that watch over and guard the various regions." 
oak @closedbrow talkingmouth "There simply aren't many Fairy-type Legendary Pokémon to be found in other regions, perhaps explaining why these 'Hidden Powers' are unable to be drawn from."
oak @closedbrow talking2mouth sweat "This theory somewhat breaks down when one considers Kalos, though..."
oak @happy sweat "And, of course, we'd be even more hard-pressed to name a Fairy-type legend that lives in Kobukan, nevermind prove its existence. This may just be one of those mysteries we'll have to wait for Instructor Valerie to reveal some day."

pause 0.5

oak @surprised "Oh! Apologies for the tangent. I've been trying to avoid doing that. "
oak @happy sweat "In any case, there are two more things you should know about this test."
oak @talking2mouth "[bluecolor]Every opponent will have the ability 'Wonder Guard', instead of whatever abilities they would normally have.{/color} As a reminder, Wonder Guard prevents non super-effective damage from directly-damaging moves."
oak @talkingmouth "The second thing is that it does not matter if your Pokémon faint, as long as you have one Pokémon left standing at the end."
oak @closedbrow talking2mouth "Of course, that's only true in hypothetical essay battles such as this--such a philosophy would be looked on with some concern by Instructor Karen, if you were to try it in a {i}real{/i} battle."
oak surprised @happy "Right, with that covered, please take out your pencils, and--"

show homeroom with vpunch

Character("Class 1-B") "\"{size=+20}[bluecolor]Remember, this will be graded!{/color}{/size}\""

pause 1.0

oak -surprisedbrow -frownmouth -surprised @happy "Ah. I suppose I needn't really say that before {i}every{/i} quiz, then."

pause 0.5

oak @sadeyebrows talkingmouth "I'm sorry, Class 1-B. This is one point where I really am just an old man set in his ways. I don't think I physically {i}can{/i} stop saying that."

redmind uniform @happy "Oh, well."

oak @happy "Good luck!"

#Foe #1: Weak to Bug
#Foe #2: Weak to Grass  
#Foe #3 Weak to Fairy
#Foe #4: Weak to Steel

python:
    trainer1 = Trainer("red", TrainerType.Player, [
        Pokemon("Espeon", level=20, moves=["Confusion", "Signal Beam", "Swift", "Bite"], nature=Natures.Serious, ivs=[0, 0, 0, 0, 0, 0]),
        Pokemon("Electabuzz", level=20, moves=["Shock Wave", "Thunder Wave", "Psychic", "Trailblaze"], nature=Natures.Serious, ivs=[0, 0, 0, 0, 0, 0]),
        Pokemon("Steenee", level=20, moves=["Dazzling Gleam", "Splash", "Zen Headbutt", "Flail"], nature=Natures.Serious, ivs=[0, 0, 0, 0, 0, 0]),
        Pokemon("Wigglytuff", level=20, moves=["Defense Curl", "Charm", "Round", "Gyro Ball"], nature=Natures.Serious, ivs=[0, 0, 0, 0, 0, 0])
    ])

    trainer2 = Trainer("oak", TrainerType.Enemy, [
        Pokemon("Skiddo", level=20, moves=["Vine Whip"], nature=Natures.Serious, ivs=[0, 0, 0, 0, 0, 0]),
        Pokemon("Diglett", level=20, moves=["Bulldoze"], nature=Natures.Serious, ivs=[0, 0, 0, 0, 0, 0]),
        Pokemon("Scraggy", level=20, moves=["Payback"], nature=Natures.Serious, ivs=[0, 0, 0, 0, 0, 0]),
        Pokemon("Aromatisse", level=20, moves=["Fairy Wind"], nature=Natures.Serious, ivs=[0, 0, 0, 0, 0, 0])
    ])

    for mon in trainer1.GetTeam() + trainer2.GetTeam():
        mon.AdjustHealth(1, True)
    
    for mon in trainer2.GetTeam():
        mon.Ability = "Wonder Guard"

call Battle([trainer1, trainer2], clearstats=False, gainexp=False, healParty=False, uniforms=[True, False], lockbag=True, lockluck=True, dialogfunc=melodyinterruption) from _call_Battle_159
$ RecordBattle("Oak10")

$ uifuckery = 0

queue music "audio/music/lawrencetheme_start.ogg" noloop
queue music "audio/music/lawrencetheme_loop.ogg" 

show screen currentdate 
show oak angrybrow frownmouth
with dis

oak @talking2mouth "...I'm afraid that's the amount of time you're allotted, students."

$ PlaySound("class_groan.ogg", "crowd2")

whitney uniform @sad "What? No! I totally didn't get to finish, because Melody was so distracting...!"

flannery uniform @closedeyes angryeyebrows sweat talking2mouth "Deep breaths, deep breaths..."

pause 0.5

flannery @furious "That was {i}bullshit!{/i}"

leaf uniform @angrybrow talking2mouth "I barely had time to finish, and... crap, Scraggy's a Fighting/{i}Dark{/i}-type, isn't it?!"

may uniform @sad "Dark/Fighting, actually, but that doesn't really matter..."

leaf @sad "I thought it was Fighting/Dragon... guess I should have stuck with Instructor Clair a bit longer..."

#play music "Audio/Music/Oak Intro.ogg" noloop
#queue music "Audio/Music/Oak Class.ogg"

if (WonBattle("Oak10")):
    redmind uniform @sad "I think I did alright, but... everyone else had a much harder time, and right when Sam really tried to turn things around..."
else:
    red uniform @angry "...I also had trouble with that one. And I think we all had the {i}same trouble{/i}."

narrator "The entire classroom is staring daggers at Melody."

oak @closedbrow sweat talking2mouth "...Well, Miss Melody, now that the quiz is over, if you could come to the front of the classroom and introduce yourself..."

show melodycgbase
show melodyrightlens
show melodyleftlens
with Dissolve(3.0)

show melody:
    xpos -1.0

show oak surprisedbrow frownmouth with dis

melody @talkingmouth "Nah."

pause 1.0

show oak angrybrow frownmouth with dis

oak @talking2mouth "Miss Melody. I have been extremely patient. I ask for a modicum of respect, so--"

melody @talkingmouth "Nah."
melody @talking2mouth "You're asking me to do something stupid, so I'm not going to."
melody @talkingmouth "'Introduce myself'? Everyone knows who I am."

pause 1.0

hide melodyleftlens with dis

melody up @talkingmouth "I'm Melody. Mark it, memorize it."

pause 3.0

show melodyleftlens with dis

melody @talkingmouth "This is the part where you call the DC, by the way."

pause 1.0

melody @thinking "[ellipses]"

pause 1.0

melody @surprised "Uh, DC? Disciplinary Committee?"
melody @surprisedbrow talkingmouth "Did you not get it?"

pause 1.0

show melody on:
    xpos 0.75 xzoom -1

hide melodycgbase
hide melodyleftlens
hide melodyrightlens
with Dissolve(2.0)

oak @talking2mouth "Miss Melody. I will acquiesce to your request to remember your name, but there is one thing I, in turn, will not let you forget."
oak @talking2mouth "I am Professor Samuel Ohkido Oak. I am the inventor of the Pokédex you carry with you. I reigned as Kanto League Champion from 1966 to 1970."
oak @talking2mouth "I am the grandfather of a Battle Team member, and the teacher of four other students who are, or were, on the Battle Team."
oak @talking2mouth "You may disagree with my methods, personality, or reputation, but I will not tolerate any further conduct that distracts or disrespects my students."
oak @closedbrow sweat talking2mouth "Finally, I am accustomed to a certain level of respect from my students. I do not ask you to 'be my fan', but you have made your point--no further elaboration is necessary."

pause 2.0

melody @talkingmouth "'Kay."

pause 0.5

melody @talkingmouth "I don't hate you any more than any other teacher, anyway."

oak @upeyes angryeyebrows talking2mouth "Splendid."

hide melody with dis

pause 1.0

Character("Nonplussed Ninny") "{size=30}\"Woah, Professor Oak was a champion?!\"{/size}"
Character("Manga Fan") "{size=30}\"Dude, you didn't know?\"{/size}"
Character("Chittering Lackaday") "{size=30}\"Crazy. But what's even crazier is that Melody chick.\"{/size}"
Character("Gasping Gal") "{size=30}\"She was a student before? What's her {i}problem{/i}?\"{/size}"
Character("Rumor-Loving Student") "{size=30}\"You know, {i}I{/i} heard her grades were so bad last year that she threatened a teacher and was kicked out...\"{/size}"
Character("Gullible Guy") "{size=30}\"Huh? No, I heard something way different! I heard she was kicked out of a different school for attacking a student, and we're only taking her back 'cause Lawrence is paying triple!\"{/size}"

redmind @sadbrow frownmouth "...Weird, hearing people spreading rumors about {i}someone else.{/i}"
redmind @closedbrow frownmouth sweat "Honestly, it's kind of a relief. But maybe I should say something...?"

menu:
    ">Dissuade the rumor-mongers":
        $ AddEvent("Melody", "StopRumors")
        red @sadbrow talkingmouth "Hey, let's not say anything we're not {i}sure{/i} of. I mean, when you guys thought I could control minds, I--"

        Character("Gullible Guy") "\"I {i}still{/i} do.\""

        red @upeyes frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
        red @closedbrow talking2mouth "Okay, well, we still shouldn't spread rumors."

        narrator "The other students quiet down, though you can sense they're just waiting for you to leave to start talking again."

    ">Stay silent":
        redmind @closedbrow frownmouth "Not placing myself in the line of fire. Maybe this'll draw some attention away from me..."

narrator "You take a quick look at Melody--you can't even tell if she's looking in your direction, with her sunglasses on."

redmind @closedbrow frownmouth sweat "She's still sitting on the desk..."

$ PlaySound("bellchime.ogg")

oak @closedbrow sweat talking2mouth "Well, I believe that covers everything we needed to address in today's lesson. I'll have these tests graded and back to you by tomorrow."
oak surprised @talkingmouth "Have a nice rest of your day, every--"

show blue uniform frownmouth with vpunch:
    xpos 0.75 xzoom -1

blue @talkingmouth "Gramps, we need to talk."

oak @surprised "Oh? Er, now isn't the best time--"

blue @angry "There's no such thing as the best time! We need to talk {i}now!{/i}"

oak @closedbrow talking2mouth "...Very well. Please come meet me at my laboratory."

hide oak
hide blue
with dis

pause 1.0

show leaf with dis:
    xpos 0.5 

leaf @talking2mouth "What do you think that was about?"

if (GetRelationshipRank("Blue") > 0):
    red @closedbrow talking2mouth "I think I've got a pretty good idea."

    if (WonBattle("Blue6")):
        show facultypoolnight at sepia
        show flashback
        with dis

        $ renpy.pause(1.0, hard=True)

        show blue og at sepia behind flashback with dis

        blue @closedbrow talking2mouth "Guess I can talk to Gramps about this after all. As soon as I tell him it lost to your Pikachu, he probably won't give it a second thought."
        
        show blank with splitfade

        hide blue
        hide facultypoolnight
        hide flashback
        hide blank with dis

    leaf @talking2mouth "Oh, yeah?"

    red @talkingmouth "He's probably going to tell Sam about his Eevee's new ability."

    leaf @surprised "He hadn't done that yet?"

    red @happy "Nah. You know him, though."

    leaf @closedbrow talking2mouth "I keep thinking I do, and then..."
    leaf @talkingmouth "Well, enough about him."

else:
    red @poutmouth "Beats me."

if (HasEvent("Leaf", "AcceptedConfession")):
    leaf @happy "Sound the horns, because I've got a report for you on the status of our date!"

else:
    leaf @happy "Sound the horns, because I've got a report for you on the status of our trip to the city!"

    red @talkingmouth "Right, the platonic not-a-date meetup you've been putting off for four weeks."

    leaf @sarcastic "Yes, that one. The sarcasm is not appreciated, [first_name]."

    red @confusedeyebrows talkingmouth "Who's being sarcastic? That's a literal descriptor."

    leaf @surprised "Oh, yeah, it actually is... huh."
    leaf @closedbrow frownmouth "[ellipses]"
    leaf @happy "Anyway, horns, et cetera, update time!"

red @sadeyebrows talkingmouth "Let me guess. A meteor hit the café, and we need to delay again."

leaf @surprised "Good sir, I am {i}shocked{/i} and {i}appalled{/i}--{w=1.0}{nw}"
extend @closedbrow talkingmouth "but honestly that's completely fair, we've just had the {i}shittiest{/i} luck setting this up."

redmind @confusedeyebrows frownmouth "{i}We?{/i}"

leaf @talking2mouth "But nah, it's nothing like that. Just that everything's still on-track for Wednesday."

red @talkingmouth "Great! Looking forward to it."

if (HasEvent("Leaf", "AcceptedConfession")):
    leaf @sadbrow talkingmouth "I... hope it was worth the wait."
    leaf blush @talking2mouth "I've been trying to think {i}really{/i} hard about something I thought you'd like, but, well, we're {i}very{/i} different people. I might be completely off-base."
    
    red @happy "I don't think you will be. We may be different people, but I like spending time with you, so as long as we're doing something together, I'll be enjoying myself."

    leaf flirtbrow @talkingmouth "Keep busting out lines like that and Professor Oak'll need to call the Disciplinary Committee to break up a PDA."

    red @winkbrow talkingmouth "And I'm well-known for my adherence to, and compliance with, their edicts, so naturally this is not an appealing proposition to me."

    leaf @happy "Your sarcasm is the hottest thing about you, you know that?"

    red @talkingmouth "And here I thought it was my ability to recite every Pokémon in Pokédex order."

    leaf @sarcastic "Actually, that's {i}incredibly{/i} dorky, and I like my men to be meatheads whose internal monologue is the sound of a slice of bread falling over."

    red @thinking "[ellipses]"

    leaf @happy "You're thinking about it now, aren't you?"

    red @closedbrow talking2mouth "Yeah, I'm trying to picture what that would even sound like..."

    leaf -flirtbrow @happy "Perfect. I didn't think it was possible, but you got even better. I guess you're angling for that second date early?"

else:
    red @talkingmouth "I just want to temper expectations--this won't be a date."

    leaf @closedbrow talking2mouth "I know, [first_name]. {i}This{/i} won't be a date."

    red @playfulbrow talking2mouth "I heard the emphasis on the word 'this'."

    leaf @talking2mouth "Good! That was intentional."

    red @sad2eyes angryeyebrows talking2mouth "You know, {i}some{/i} people would find your relentless pursuit of me to be... what's the word?"

    leaf @sarcastic "Sorry, what was that? I couldn't hear you from all the way back in Pallet Town."
    leaf @surprised "Wait, what? You're {i}not{/i} in Pallet Town? Now, tell me, who could it be that made that so?"

    red @unamusedbrow talking2mouth "Tia."

    leaf @closedbrow talkingmouth "Oh, yeah, that's a fair point, actually."
    leaf @talking2mouth "Whatever. The point I was {i}trying{/i} to make was that my 'relentless pursuit' hasn't exactly been to your detriment."
    leaf @happy "Worst-case scenario, I'm giving you unreasonable expectations for whoever you {i}do{/i} decide to date!"

    red @confused "I think that would be 'whomever'?"

    leaf @sarcastic "And suddenly all my attraction to you just flew out the second-story window."

if (not HasEvent("Klara", "BreakHeart")):
    red @talkingmouth "Oh, that reminds me--I actually have a date for tomorrow!"

    leaf @surprised "Woah! Seriously?"

    if (HasEvent("Leaf", "AcceptedConfession")):
        leaf @sadbrow talking2mouth "I... probably shouldn't admit this, but I was kind of hoping I'd be your first date this year..."

        if (GetRelationshipRank("Nessa") > 0 and not HasEvent("Nessa", "DenyDate")):
            red @sadbrow talkingmouth "Sorry, that was Nessa."

        else:
            red @sadbrow talkingmouth "Sorry."

        leaf @happy "Oh, no, that's completely fine!"
        leaf @talkingmouth "I mean... I did push this off for four weeks. I kinda knew that something would probably happen in the meantime."

        if (GetRelationshipRank("Nessa") > 0 and not HasEvent("Nessa", "DenyDate")):
            leaf @closedbrow talking2mouth "Still, off by {i}one{/i} day? Geez..."

    else:
        leaf @talking2mouth "Since when?"

        narrator "You look at your wrist. {w=0.5}You still do not have a watch."

        red @talkingmouth "Uh, about two hours ago."

        leaf @surprised "Holy shit! That was {i}fast.{/i} Like, I am actually in {i}awe.{/i}"
        leaf @closedbrow talking2mouth "{size=30}I should probably take a couple notes from this guy...{/size}"

    leaf surprisedbrow frownmouth @happybrow talkingmouth "Well, who's the lucky person?"

    red @talkingmouth "Uh, Klara. Think you know her?"

    leaf @talking2mouth "Klara?"

    pause 1.0

    red @confused "You seem surprised?"

    leaf -surprisedbrow -frownmouth @happy blush "A little, yeah! I just had no idea she saw you that way. But that's great!"
    leaf @sadbrow talking2mouth "I don't know her... {i}super{/i} well, but from what I do know..."
    leaf @talkingmouth "She's a really great girl. Super kind and smart. And her Galarian accent is so posh and cute."
    leaf @talkingmouth "She actually taught my Ivysaur a special move that Instructor Koga came up with."
    leaf @sadbrow talkingmouth "I... didn't really want to attend his class personally, but since she's in his class, she helped me out."
    leaf @happy "Yeah, I can totally see it. I hope you two have fun!"

    red @talkingmouth "We'll do our best."
    red @talkingmouth "Speaking of which--I should head out. See you back at the dorm?"

    leaf @happy "See ya."

    narrator "You depart."

    pause 2.0

    leaf @angry "Oh, come {i}on!{/i} One day?! {w=0.5}I was beaten by {i}one{/i} actual day?! {w=0.5}Grrrrraaaaah!"

    if (GetRelationshipRank("Nessa") > 0 and not HasEvent("Nessa", "DenyDate")):
        leaf @closedbrow talking2mouth "I mean, sure, maybe Nessa beat me first, but she's a supermodel, I couldn't compete with that anyway. But {i}one{/i} day?! That almost feels purposeful!"

    show leaf:
        xpos 0.5
        ease 0.5 xpos 0.66

    show flannery uniform with dis:
        xpos 0.33

    flannery @happy "The early bird catches the worm, Leaf."
    flannery @winkbrow talkingmouth "Hey, if you want some advice on setting up a date that'll {i}sweep{/i} him off his feet, I've got some 'literature' I can recommend."

    if (HasEvent("Leaf", "AcceptedConfession")): 
        leaf @talking2mouth "Nah. I know what I need to do."
        leaf embarrassed bigblush "It's just... embarrassing..."

    else:
        leaf @sarcastic "If my natural feminine charms haven't won him over, I'm pretty sure that your fanfics aren't going to do it, either."

        flannery @happy "Don't knock them 'til you've tried them. Whitney got her first girlfriend using a line I wrote."

        leaf closedbrow talkingmouth "I'll keep that in reserve."

else:
    redmind @thinking "Should I tell Leaf about Klara...? Nah. Klara apparently didn't even ask me out, anyway, so there's nothing to tell."

    red @talkingmouth "Well, on that note, I should be going. Got some time to kill this evening."

    leaf @talking2mouth "Alright. Seeya back at the dorm!"

call clearscreens() from _call_clearscreens_214
scene blank2 with splitfade

narrator "You try to put Melody out of your mind, as you resolve to enjoy your free time without interruptions..."
narrator "You're still {i}quite{/i} hungry, though."

$ removestudents = { "Blue" }

call freeroam from _call_freeroam_30

$ removestudents = set()

stop music fadeout 1.5
$ renpy.music.queue("Audio/Music/brandnewworld.ogg", channel='music', loop=True, fadein=1.5, tight=None)

scene lobby_night
show raihan frownmouth with dis:
    xpos 0.33
show sonia sad with dis:
    xpos 0.66
with splitfade

raihan @talkingmouth "{size=20}...Y'sure{/size}{size=30} what you're{/size} saying is all right, Sunny?"

sonia @talking2mouth "Do you... not believe me?"

raihan -frownmouth @happy "Nah, I believe you well enough."
raihan @sadbrow talkingmouth "Just, y'know, being an influencer and all, I've heard a fair share of digs about myself."

sonia @angrybrow talking2mouth "These aren't just {i}rumors{/i}, Raihan. I was here last year. I {i}saw{/i} her."

raihan @closedbrow talking2mouth "Fair enough, yeah. I try to keep an open mind, though."

redmind @confusedeyebrows frownmouth "Seems like some kind of mild disagreement...?"
red @talkingmouth "Hey. What's up?"

if (GetRelationshipRank("Sonia") > 1):
    sonia -sad @talking2mouth "[first_name]! Maybe you can talk to this thick-headed Gym Leader."

    raihan @sad "...Y'know, you don't {i}always{/i} have to tell the truth."

elif (GetRelationshipRank("Raihan") > 0):
    raihan @talkingmouth "[first_name]! How you doing, mate?"

    red @happy "Can't complain!"

elif (GetRelationshipRank("Sonia") > 0):
    sonia -sad @talking2mouth "[first_name]?"

red @talkingmouth "What were you talking about?"

sonia @talking2mouth "Who else? Melody."

raihan @closedbrow talkingmouth "Sunny here's trying to convince me that Melody's pretty much the devil herself."
raihan @happy "'Course I trust Sunny, but you get in the DMs of any one of my haters, and I'd sound pretty off, myself."

sonia @angrybrow talkingmouth "I'm not the {i}only{/i} one! Ask anyone else who was here last year!"

raihan @surprisedbrow talkingmouth "Well... I suppose I could, but..."

sonia @angry "Look, there!"
sonia @angry "Brawly!"

hide raihan
hide sonia
with dis

pause 1.0

show brawly:
    xpos 0.25
show roxanne
show falkner:
    xpos 0.75

brawly @talkingmouth "Hey! Sonia, right? What's up?"

show brawly frownmouth
show roxanne frownmouth
with dis

sonia @talking2mouth "It's Melody. Raihan here isn't believing what I'm telling him about her!"

brawly @closedbrow talking2mouth "Ah, geez... yeah, that's been a big pain in the ass already."

roxanne @closedbrow sweat talking2mouth "No less than three reports about her already--and those are only the ones the Disciplinary Committee felt needed our attention."

falkner @closedbrow talking2mouth "Of course, there's little {i}we{/i} can do but elevate the issue to Dean Drayden."

raihan @surprised "Crikey. Y'mean she's actually that much of a problem?"

roxanne @closedbrow talking2mouth "We, as the Acting Student Council, should not tell stories that paint the students under our responsibility in a negative light."

brawly -frownmouth @happy "I'm totally going to, anyway."

roxanne @closedbrow talking2mouth "...Brawly."

brawly @sadbrow talkingmouth "Just one story? You know I love telling {i}that{/i} one."

roxanne @sad2brow sweat talking2mouth "...One supposes a dry recounting of the facts would not be out-of-line, for preparatory purposes..."

show falkner happy behind roxanne with dis:
    xpos 0.75
    ease 0.3 xpos .6

show brawly happy behind roxanne with dis:
    xpos 0.25
    ease 0.3 xpos .4

pause 0.1

$ PlaySound("clap.ogg")

pause 1.0

show falkner smilemouth with dis:
    xpos 0.6
    ease 1.0 xpos .75

show brawly -happy with dis:
    xpos 0.4
    ease 1.0 xpos .25

roxanne @sadbrow talking2mouth "...I feel as though I've opened some door I can no longer close..."

show brawly:
    xpos 0.25
    ease 0.5 xpos 0.5

show roxanne:
    xpos 0.5 xzoom 1
    ease 0.5 xpos 0.25 xzoom -1

brawly @talkingmouth "{size=30}'Scuse me, Roxie...{/size} Alright, now, you three, listen up. Big brother Brawly's going to tell you a seafarer's tale that'll chill your bones more than {i}any{/i} story about Sharpedo or dead waves could."

raihan @happy "Should we grab some popcorn?"

sonia @talking2mouth "Raihan, be serious. This is a matter of {i}survival.{/i}"

roxanne @closedbrow talking2mouth "Brawly, remember, recount only {i}facts.{/i} Let us not speculate on possible other misdemeanors."

falkner @closedbrow talkingmouth "Given Melody's rap sheet, there is hardly a need to embellish." 

brawly @angrybrow talking2mouth "Hey, hey, clear the air! I'm getting into my groove."

falkner @talkingmouth "By all means."

show brawly closedbrow frownmouth with dis

pause 1.0

brawly @talkingmouth "Last year, I shared one class with Melody. Just one. We didn't homeroom together, but we had an elective together."
brawly @talkingmouth "We were taking Instructor Juan's elective."

sonia @surprised "Oh, yes, I remember Instructor Juan!"

raihan @talking2mouth "...Not ringing a bell...?"

sonia @talking2mouth "He taught Water-type classes, if I remember correctly."

brawly -closedbrow -frownmouth @talkingmouth "Yeah, and he was the teacher of Instructor Wallace. Mentored him, apparently. Not in Kobukan, but back in Hoenn, in Pacifidlog."

falkner @talkingmouth "You mean Sootopolis."

brawly @surprised "Huh? Do I?"

roxanne @talkingmouth "You do."

brawly @closedbrow talking2mouth "Damn. And I spent so long trying to figure out how to pronounce that."
brawly @talkingmouth "Anyway, that part isn't important. Melody and I took Instructor Juan's elective together."
brawly @sadbrow talkingmouth "And what I saw in that class... some people are just bad apples, you know?"

falkner @closedbrow talking2mouth "Well-known for spoiling the bunch, unless immediately {i}removed{/i} from the barrel."

brawly @talkingmouth "She {i}hated{/i} Instructor Juan."

roxanne @closedbrow talking2mouth "That's speculation."

brawly @talkingmouth "Nah, she straight-up said she hated him."

brawly @talkingmouth "The two would get in arguments all the time. Melody would even start screaming at him in class, and he kicked her out of class a ton."
brawly @closedbrow talking2mouth "We're pretty sure her grades were in the toilet, and she was angry that he wasn't bending the rules for her."

roxanne @angrybrow talking2mouth "Please remove the speculation from the record."

falkner @surprised "Yes, your honor."

brawly @talkingmouth "Anyway, one day, Instructor Juan just straight-up disappeared."
brawly @angry "And I'm not pointing fingers, but there's only one person who hated him enough to make that happen."

falkner @sadbrow talking2mouth "You make it sound like she had him kidnapped."
falkner @closedbrow talkingmouth "We know where he is--he's running the Sootopolis Gym. But he disappeared from his teaching position without a word of explanation to his class."
falkner @talking2mouth "We, as Student Council, had to field tons of confused questions about where he was, and what his students should do..."

raihan @talking2mouth "Damn. What happened?"

brawly @happy "Uh, I stepped up. I'm not much of a Water-type teacher, mostly focus on Fighting-types, but the class was, like, totally sunk without someone in charge."

roxanne @closedbrow talkingmouth "He was very noble."

brawly @happy "Ah, I only 'taught' that class for, like a week. Then Chef Kofu took over until Instructor Wallace decided to try teaching."

roxanne @sweat talking2mouth "His students seem happy enough, but it's an irresponsible choice. Teachers hold the livelihoods and futures of their students in their hands. Not something to be done on a whim."

falkner @happy "Roxie's a Steven fangirl. She took it very personally when Wallace trounced him."

roxanne @angrybrow blush poutmouth "S-speculation."

raihan @talkingmouth "So, Melody got a teacher fired. I mean, that's pretty bad, but--"

falkner @closedbrow talkingmouth "Baton Pass, Brawly. I'm up."

brawly @happy "Got it."

show roxanne behind falkner

show brawly:
    xpos 0.5 xzoom 1
    ease 0.5 xpos 0.75 xzoom -1

show falkner:
    xpos 0.75
    ease 0.5 xpos 0.5

falkner @talkingmouth "You've only {i}begun{/i} to hear the start of this story."
falkner @closedbrow talking2mouth "And this is where it gets {i}grisly.{/i}"

show roxanne angrybrow blush poutmouth with dis

falkner @talking2mouth "Brawly attended classes with three women of unparalleled beauty."

pause 0.5

roxanne "{w=0.5}.{w=0.5}.{w=0.5}."

pause 0.5

falkner @talkingmouth "Yes, Roxie? Something you'd like to say?"

roxanne @closedbrow talking2mouth "'Unparalleled beauty' is an unverifiable matter of opinion."

falkner @closedbrow talkingmouth "My mistake. Perhaps you would forgive me if I were to apply that descriptor to you, instead?"

pause 1.0

roxanne -angrybrow -blush -poutmouth @blush closedbrow talking2mouth "Well, it's still subjective."

falkner @happy "They were known as the 'Sensational Sisters'. Their names were Daisy, Lily, and Violet."

sonia @talking2mouth "The most popular girls in school. They were solid Teflon--never bothered, never harassed."
sonia @sad "Truthfully, I would have given anything to be one of them..."
sonia @sadbrow happymouth "But I suppose I was doomed to their shadows, given my name was not a flower."

raihan @surprised "...Sunny, your last name is Magnolia."

sonia @angry "It's not the same!"

raihan @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

redmind @thinking "Feels the same to me."

falkner @talkingmouth "Yes, they were powerful, practiced, and perfect. We, as the Student Council, were often forced to negotiate with them, given their sway over popular opinion." 
falkner @closedbrow talking2mouth "But I set the tower up now just to make its eventual destruction ever more poignant."
falkner @surprised "Melody managed to steal their boyfriends."

roxanne @closedbrow talking2mouth "That's not confirmed."

falkner @talkingmouth "Whatever the case, one after another, their boyfriends broke up with them, publicly."
falkner @closedbrow talkingmouth "You have to understand the social stigma here--all three of their boyfriends were ace members of the Battle Team. They, in turn were the stars of the cheer squad."

raihan @happy "We have a cheer squad?"

red @talking2mouth closedbrow "Boy, do we. Nearly got stuck in their changing room."

sonia @talking2mouth "Right, Leaf told me about that one. She rescued you, right?"

red @upeyes talking2mouth "That's one interpretation of events."

falkner @closedbrow talkingmouth "{i}Ahem.{/i}"

sonia @talking2mouth "Sorry, carry on."

falkner @talkingmouth "So, yes, as I was saying--social stigma. They were the perfect pairs, created out of perfect people. To break up... whatever occurred must have been tremendous."
falkner @talkingmouth "We, the student body, were left nonplussed and wondering."
falkner @angrybrow talking2mouth "Until, of course, everything became incredibly clear. Violet's--or perhaps Daisy or Lily's, I don't remember which--ex confessed to Melody."
falkner @closedbrow talkingmouth "Clearly, Melody had managed to seduce the three most popular girls' boyfriends away from them."

pause 1.0

brawly @talkingmouth "Really? Roxie? That's speculation, right?"

roxanne @talkingmouth "It's permissable."

brawly @surprised "What?! Is this because he called you pretty? I'll call you pretty, too!"

roxanne @closedbrow talking2mouth "Later. Falkner, please wrap up."

falkner @talking2mouth "Well, whatever happened, Melody managed to break up the {i}three{/i} biggest couples in school in one fell swoop."

roxanne @closedbrow talking2mouth "High-school level nonsense."

falkner @closedbrow talkingmouth "That it might be, but it {i}was{/i} immensely entertaining. Roxie, if you would?"

show roxanne:
    xpos 0.25
    ease 0.5 xpos 0.5

show falkner:
    xpos 0.5 xzoom 1
    ease 0.5 xpos 0.25 xzoom -1

roxanne @talkingmouth "I have not much to add. There is only one thing I am confident of, one thing I can say that requires no interpretation or imagination to bring into truth."

falkner @talking2mouth "And with no further preamble..."

roxanne @talking2mouth "Melody is absolutely untouchable. For whatever reason, nothing any student, teacher, or even Dean Drayden does can affect her."
roxanne @closedbrow sweat talking2mouth "We are, regrettably, amongst that powerless number."

raihan @surprised "You're telling me even Drayden can't just expel her?"

roxanne @talkingmouth "For one reason or another--no."
roxanne @closedbrow talking2mouth "I am all but certain that she could walk up to Dean Drayden, steal his Pokémon, and he would not lift a finger against her."

sonia @talking2mouth "It's true. She gets away with {i}everything.{/i} {size=30}Some people think she's blackmailing Dean Drayden, somehow...{/size}"

red @talkingmouth "I saw her today. She wasn't wearing her uniform."

roxanne @closedbrow talking2mouth sweat "Among her least offensive infractions, and yet still one that aggravates for no good reason."

pause 1.0

roxanne @closedbrow talking2mouth "...Well, Raihan, I hope that I have made the veracity of Sonia's statements clear to you."

sonia @talking2mouth "I also heard that she was kicked out of this school for being violent towards her classmates, and even teachers..."

roxanne @closedbrow talking2mouth "We cannot confirm that."

raihan @closedbrow talking2mouth "Guess I should've listened to you then, Sunny. Sounds like you were pretty right on the money."

sonia @happy "{i}Thank{/i} you!"

roxanne @talkingmouth "As the Acting Student Council, we, of course, seek the success and happiness of {i}all{/i} the student body."
roxanne @sad2brow talking2mouth "That being said..."

falkner @closedbrow talking2mouth "Stay away from Melody."

brawly @sadbrow talking2mouth "For your own safety, bros."

roxanne @talking2mouth "In lieu of perfect information, one can only act on the information that is immediately apparent. And the information that is apparent in this circumstance is {i}quite{/i} telling."

raihan @talking2mouth "Well, thanks for the news. Won't spread it around, honest."

brawly @happy "Not worried about that. I follow your Rotophotos. Know you're a good guy. Happy birthday, by the way!"

red @surprised "It's your birthday, Raihan?"

raihan @closedbrow sweat talking2mouth "Ah, yeah... sorry, mate, was trying to keep that under wraps."

$ autoquote = False

brawly @surprised "\"Oh!"
extend @sadbrow talkingmouth " Sorry, bro.\""

$ autoquote = True

falkner @talkingmouth "I believe that's our cue to depart. Please make it back to your dorms shortly. Curfew is soon."

hide falkner
hide brawly
hide roxanne
with dis

pause 1.0

show raihan:
    xpos 0.33
show sonia:
    xpos 0.66
with dis

sonia @talking2mouth "Raihan, why were you trying to hide your birthday?"

raihan @closedbrow talkingmouth "Ah, nothing serious. It's just... you know, you and Nessa are enough."
raihan @talking2mouth "Besides, people send me gifts all the time, give me stuff for free. Birthdays aren't so special."
raihan @happy "And I'm already older than most people here. Don't want to draw attention to it, right?"

sonia @happy "You're hardly Opal's age, Raihan. Don't need to worry about seeming old."

raihan @talking2mouth playfulbrow "You say that, but it's amazing how quick your demo drops off when you hit twenty-five."
raihan @talkingmouth "'Course, got a few years 'til that, but I'm not in any hurry..."

if (GetRelationshipRank("Raihan") > 0):
    red @sadbrow talkingmouth "Sorry, Raihan. Wish I knew it was your birthday. I'd have bought a gift."

    raihan happy "Nah, I'm fine, really. Just promise me a good battle sometime later, with that Pikachu, and I'll say you're good for it."

    red @happy "Sure."

    $ ValueChange("Raihan", 1, 0.33)

    show raihan -happy with dis

sonia @talking2mouth "Right, then, we should probably be heading back to our dorms, like Falkner said."

red @talkingmouth "Yeah, alright. See you later!"

scene blank2 with splitfade 

narrator "You make your way back to the dorm... but, weirdly, Yellow and Ethan seem to have already gone to bed." 
narrator "Blue is just sitting on the couch, looking forlornly at an Inferno & Logos mat. Leaf, sitting on the other end of the couch, seems to be trying to escape without being noticed."

scene suitenight
show blue og wistfulbrow frownmouth:
    xpos 0.66
show leaf sadbrow frownmouth:
    xpos 0.33
with splitfade

pause 1.0

red @talkingmouth "...Hey, Blue?"

blue @surprised "Hm?"
blue -wistfulbrow @closedbrow talkingmouth "You're back."

red @talkingmouth "True."

pause 0.5

red @talkingmouth "Guess game night's cancelled?"

blue @talkingmouth "...Guess so."

pause 0.5

red @talkingmouth "You talked to your grandfather?"

blue @closedbrow talkingmouth "Yeah, I talked to Gramps."

pause 1.0

blue @talkingmouth "I know how Eevee works now. So that's great."

leaf @talking2mouth "Um... are you going to tell us?"

blue @talkingmouth "No. Information is power. I might be able to surprise one of you two, and beat you with it."

leaf @closedbrow talking2mouth "...Yeah, I probably should have expected that."
leaf @sadbrow talkingmouth "Well, the air here is, like, really awkward, so I'm just going to... go to bed..."

hide leaf 
show blue wistfulbrow
with dis

pause 1.0

narrator "You wait for a while, but Blue doesn't say anything more."
narrator "Following Leaf's lead, you also go to bed."

call texting from _call_texting_25

jump day010525