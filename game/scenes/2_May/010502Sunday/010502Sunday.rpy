label day010502:
$ timeOfDay = "Morning"

camera master

if (pikachuobj in playerparty):
    $ playerparty.remove(pikachuobj)

call calendar(1) from _call_calendar_27
$ calDate = calDate.replace(day=2, month=5, year=2004)

show morning at vspaz

pause 3.5

narrator "{color=#ff0000}You are no longer you.{/color}"

pause 2.0

stop music channel "misc"
stop sound channel "misc"

show screen songsplash("Run Away, Fugitives", "Lazy Totodile")

queue music "audio/music/runawayfugitives_start.ogg" noloop
queue music "audio/music/runawayfugitives_loop.ogg"

python:
    playercharacter = "Ethan"

    #overwriting party, inventory, personalstats, and persondex

    oldparty = []
    ethanparty = []
    for mon in playerparty:
        oldparty.append(mon)
        ethanparty.append(Pokemon(mon.Id, level=max(1, mon.Level - 1), ivs=[1, 1, 1, 1, 1, 1], evs=[0, 0, 0, 0, 0, 0], moves=copy.deepcopy(mon.Moves), gender=mon.Gender, ability=mon.Ability))
    playerparty = ethanparty

    oldinventory = copy.copy(inventory)
    inventory = {
        Item.OldPicture : 1,
        Item.FirstAidKit : 1,
        Item.Pichu : 1,
        Item.GSBall : 1,
        Item.ExperienceShare : 1
    }

    oldpersonalstats = copy.copy(personalstats)
    personalstats = {
        "Charm" : -3,
        "Knowledge" : 5,
        "Courage" : 2,
        "Wit" : 9,
        "Patience" : 69
    }

    oldpersondex = copy.deepcopy(persondex)
    persondex = copy.deepcopy(defaultpersondex)
    persondex[first_name] = {"Named" : True, "Value" : oldpersondex["Ethan"]["Value"] * 3, "Contact": False, "Sex": Genders.Male, "Relationship": "Wannabe", "RelationshipRank": 0, "Events": [] }
    persondex["Professor Cherry"] = {"Named" : True, "Value" : 247, "Contact": False, "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [] }
    persondex["Ethan"]["Named"] = True
    persondex["Blue"]["Named"] = False

scene dorm_A:
    zoom 1.1 rotate 2 yalign 0.5 xalign 0.5
show screen currentdate
with transeye2

narrator "You wake up from a nightmare. It's the same old one. You barely register it anymore."

$ hideside = True

pause 1.0

narrator "You yawn, checking the time on your clock."
narrator "It seems you've woken up early."

call clearscreens from _call_clearscreens_79

show blank2 with Dissolve(1.0)

show noon at vspaz

pause 3.5

$ timeOfDay = "Noon"

hide blank2
hide noon
show screen currentdate
with dis

pause 1.0

narrator "Well, relatively early.{w=0.5} Still, it's a Sunday. It's not like you have anything going on."

pause 1.0

show dorm_A:
    ease 2.0 zoom 1.1 rotate 0

narrator "You slowly pull yourself out of bed. Your four roommates are gone, of course. It's so late in the day, it could only be expected."

$ pichuid = 172
$ PlaySound("pokemon/cries/{}.mp3".format(pichuid))

pause 1.0

narrator "Your little electric partner jumps into your bag as you swing it over your shoulder."
narrator "You ponder what they might be serving in the cafeteria. Maybe they're still serving breakfast. You could get a... late brunch or something..."
narrator "You yawn again, but a minor electric shock from your bag reminds you that you're not the only hungry one in the room right now."

scene blank with splitfade

pause 2.0

scene cafe with splitfade

narrator "As you walk into the cafeteria, you hear a low, disgruntled, murmuring sound echoing from your classmates. You ignore it, as no-one looks at you."

pause 1.0

show cafe:
    xalign 1.0 yalign 0.0
    ease 2.0 zoom 1.3

narrator "You find an empty table and sit down to eat by yourself, picking at some leftover waffles."

pause 1.0

show cafe:
    xalign 1.0 yalign 0.0
    ease 2.0 zoom 1.0 xalign 0.5 yalign 0.5

narrator "It's only noon, but you already feel like you've wasted your entire day."

pause 1.0

narrator "You decide to take a nap. Perhaps when you wake up, you'll feel more prepared to handle what comes next."

show cafe:
    xalign 0.5 yalign 0.5
    ease 1.0 rotate 2 zoom 1.1

show blank2 with transeye

pause 2.0

show blank2 at vpunch

leaf @talking2mouth "Hey!"

hide blank2 
show leaf angry
with transeye2

narrator "You blearily blink the sleep out of your eyes as you look up and see a familiar girl standing over the table, glaring down at you."

leaf @talking2mouth "Are you just going to sleep there and pretend there isn't a {i}big{/i} elephant in the room? What are we going to do?"

narrator "You raise an eyebrow at the girl. She seems to have some very strong feelings about something you aren't familiar with."
narrator "...It sounds like a whole lot of 'not your problem.'"
narrator "You shrug, and prepare to go back to sleep."

show leaf:
    ease 0.2 ypos 1.2 zoom 1.3
show cafe with vpunch:
    ease 0.5 rotate 0 zoom 1.0

leaf @talking2mouth "{i}{color=#c1861e}Ethan!{/color}{/i}"

$ hideside = False

ethan @surprised "Woah, what?"

leaf @talking2mouth "What.{w=0.5}{nw}"

show leaf with vpunch

extend @talkingmouth " Are we going.{w=0.5}{nw}"

show leaf with vpunch

extend @talkingmouth " To do?"

ethan @closedbrow talking2mouth "Look, Leaf, I don't know what you're talking about, but I can't help you with whatever it is that's got you like this."

show leaf -angry sadbrow frownmouth with dis:
    ease 1.0 ypos 1.0 zoom 1.0

leaf @talking2mouth "My name's Leaf, not Leaflet. And I thought you were, like, his best friend."

ethan @happy "Man, I'm not {i}anybody's{/i} best friend."

leaf @talking2mouth "Do you at least know where he is?"

ethan @confusedeyebrows talking2mouth "Yeah, uh, maybe I wasn't clear. Who are you talking about?"

leaf @surprised "Wh-- {i}who?!{/i} Are you kidding me, Ethan? {i}[first_name]!{/i} Your roommate!"

ethan @surprised "Woah, what's with the passion? No, I don't know where he is!"
ethan @closedbrow talking2mouth "It's a Sunday, he's probably out studying or training or something. It's not like I keep tabs on him."

leaf @angrybrow angrymouth "Oh, right, so it's a {i}total{/i} coincidence that you always end up in the same places? You just {i}coincidentally{/i} end up doing everything he does?"

if (len(eggshatched) == 1):
    $ oneegg = eggshatched[0]
    if (oneegg not in ["Happiny", "Deino"]):
        ethan @angry "Hey! {i}He{/i} might be copying me! Like, even during the egg hunt, you know how he got that [oneegg] egg?"

        leaf @sarcastic "Yeah?"

        ethan @talking2mouth "I already had a [oneegg] egg in the incubator! My old neighbor sent it to me, like a week before Springsday!"

        leaf @sarcastic "Sure. Why would your neighbor send you an egg?"

        ethan @closedbrow talking2mouth "She's a competitive breeder, and she dumps her breedjects on me... I dunno, but that's what she does, alright?"
    elif (oneegg == "Happiny"):
        if (HasEvent("Whitney", "HasHappiny")):
            ethan @angry "Hey! {i}He{/i} might be copying me! Like, you know how he traded his Happiny for a Munchlax on Monday?"

            leaf @sarcastic "Yeah?"

            ethan @talking2mouth "I already had a Munchlax! My old neighbor sent it to me, like a week before Springsday!"

            leaf @sarcastic "Sure. Why would your neighbor send you a Munchlax?"

            ethan @closedbrow talking2mouth "She's a competitive breeder, and she dumps her breedjects on me... I dunno, but that's what she does, alright?"

        else:
            ethan @angry "Hey! {i}He{/i} might be copying me! Like, even during the egg hunt, you know how he got that Happiny?"

            leaf @sarcastic "Yeah?"

            ethan @talking2mouth "I already had a Happiny! My old neighbor sent it to me, like a week before Springsday!"

            leaf @sarcastic "Sure. Why would your neighbor send you a Happiny?"

            ethan @closedbrow talking2mouth "She's a competitive breeder, and she dumps her breedjects on me... I dunno, but that's what she does, alright?"
    else:
        ethan @angry "Hey! {i}He{/i} might be copying me! Like, even during the egg hunt, you know how he got that Deino?"

        leaf @sarcastic "Yeah?"

        ethan @angry "This one girl gave {i}both{/i} of us a Deino at once! She had two eggs! I didn't decide that!"

        leaf @sarcastic "Sure. Why would some random girl give you two Deino?"

        ethan @closedbrow talking2mouth "I don't know. She said she already had big versions of them. Maybe she has a really buff Deino. Maybe she's a competitive breeder, dumping her breedjects on us. I dunno."

elif (len(eggshatched) > 1):
    ethan @angry "Hey! {i}He{/i} might be copying me! Like, you know those Pokémon he picked up during the egg hunt?"

    leaf @sarcastic "Yeah?"

    ethan @talking2mouth "I already had their {i}exact{/i} eggs in the incubator! My old neighbor sent them to me."

    ethan @talking2mouth "That's why I didn't pick up any eggs during the hunt! I already had as many as I could carry."
    
    if ("Deino" in eggshatched):
        ethan @talking2mouth "And you can't blame me for the Deino. Someone gave us two Deino eggs at once."

    if ("Happiny" in eggshatched):
        python:
            hasmunchlax = False
            hashappiny = False
            for mon in AllPokemon():
                if (mon.GetId() == pokedexlookupname("Munchlax", DexMacros.Id)):
                    hasmunchlax = True
                elif (mon.GetId() == pokedexlookupname("Happiny", DexMacros.Id)):
                    hashappiny = True

        if (hasmunchlax):
            leaf @sarcastic "And the Munchlax he has?"
        
            ethan @closedbrow talking2mouth  "My old neighbor sent it to me, like a week before Springsday!"

            leaf @sarcastic "Sure. Why would your neighbor send you a Munchlax and a bunch of eggs?"

        elif (hashappiny):
            leaf @sarcastic "And the Happiny he found?"
        
            ethan @closedbrow talking2mouth  "My old neighbor sent it to me, like a week before Springsday!"

            leaf @sarcastic "Sure. Why would your neighbor send you a Happiny and a bunch of eggs?"

        else:
            leaf @sarcastic "Sure. Why would your neighbor send you a bunch of eggs?"

    ethan @closedbrow talking2mouth "She's a competitive breeder, and she dumps her breedjects on me... I dunno, but that's what she does, alright?"

leaf "{w=0.5}.{w=0.5}.{w=0.5}."

leaf @sarcastic "Well, fine, maybe you aren't stalking him. But can't you at least use your connection to figure out where he is?"

ethanmind @thinking "Great. Ethan Gold, the world's best compass for people who are better than him."

ethan @talking2mouth "Yeah, I don't know. I don't go out of my way to follow him. Heck, half the time, I get there first."

show leaf sadbrow frownmouth with dis 

leaf "{w=0.5}.{w=0.5}.{w=0.5}."

leaf @talking2mouth "...Well, if you could be anywhere right now, where do you wish you were?"

ethan @happy "Honestly? Home."

leaf @closedbrow talking2mouth "...Ugh."

ethan @talking2mouth "Yeah, sorry. Why are you even asking? Don't you have his phone number?"

leaf @talking2mouth "I do! But he's not answering his phone. I haven't been able to track him down all of today, or yesterday."

leaf @closedbrow talking2mouth "I gave him some space yesterday, but... I thought we needed to talk today..."

pause 1.0

ethan @angrybrow talking2mouth "You know, {i}nothing{/i} about you passes the Bechdel test."

leaf @surprised "What?"

ethan @talkingmouth "Nothing. Anyway, what's this about giving him space? Did something happen?"

leaf surprisedbrow frownmouth @surprised "What?"

ethan @confused "Okay, I'm getting the vibe that something {i}did{/i} happen."

leaf surprisedbrow frownmouth @surprised "Did... did you not go to the speeches? You didn't even go there to support your two roommates?"

ethan @happy "Hey, I was going to! I was{w=0.5}.{w=0.5}.{w=0.5}."

ethan @sad2eyes sadmouth "I just didn't feel up to it. Figured it'd be better to take a nap, and maybe when I woke up, things'd be... better."

leaf -surprisedbrow -frownmouth -surprised frownmouth @sadbrow talking2mouth "Oh. Um... then someone should probably tell you what happened."

ethan @confused "Sounds like you're going to tell me some bad news that wasn't affecting me before just now. Can I opt out?"

leaf @talking2mouth "[first_name] has a power that makes people and Pokémon like him. That's how all his Pokémon listen to him, and how he got so many... so many friends."

ethan frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

ethan @talking2mouth "That sounds hard to believe."

pause 1.0

ethan @closedbrow talking2mouth "How did you find out? How many people know?"

leaf closedbrow @talking2mouth "You're going to want to be sitting down for this."

show leaf angrysmilemouth angrybrow with dis

ethan @confused "I am?"

show blank2 with dis

narrator "{color=#00b23f}???{/color} tells you the details of the prior day's disastrous Student Council election."

ethanmind sad "Why...?"
ethanmind closedbrow talking2mouth "Why didn't he just lie and tell everyone Cheren was crazy? It's not that hard. It's... {i}really{/i} easy, actually..."
ethanmind "It sounds like Cheren was willing to accept any lie he was told, if only [first_name] was willing to lie..."

hide blank2 with dis

leaf -angrysmilemouth -angrybrow frownmouth @talking2mouth "...so everyone lost track of him after the election. And no-one I've talked to has been able to find him since."

ethan @talking2mouth "Well, sorry to disappoint. He wasn't there when I went to bed last night."
ethan @closedbrow talking2mouth "Come to think of it, I don't think any of my roomies were, and I went to bed pretty close to curfew."

leaf @talking2mouth "...We were meant to go into the city today."

$ PlaySound("idea.ogg")

ethan @surprised "Crap, that's right! I was going to have a talk with [first_name] about my theory!"
ethan @closedbrow talking2mouth "Damn. I remembered for half a second after I woke up, but I figured since he wasn't in the room that he'd cancelled on me."

leaf @talking2mouth "You didn't think to, I dunno, call him and see if your plans were still on?"

ethan @confused "What, you've never had someone ghost you for some meeting you set up, but didn't actually want to do?"
ethan @happy "It's the best feeling in the world. Believe me."

leaf @sarcastic "...I'm not going to be your therapist."

ethan @talkingmouth "Hey, that's what my Dad said."

leaf @sarcastic "Ugh. He has three other roommates, right? Maybe one of them will know where he went."

ethan @closedbrow talking2mouth "Wait, wait. Fine. I'll help you find him. Again, it's Sunday, so he could be anywhere. Dude's a massive socialite, as you've probably noticed by now."

leaf @talking2mouth "Great. Thanks."

pause 1.0

leaf @sadbrow talking2mouth "But, uh, where to, then?"

ethan @confused "Well, you said you were meant to meet up in the city, right? Maybe he's out there?"

leaf @talking2mouth "...Without me?"

ethan @closedbrow talking2mouth "Sure. He went there to meet you, because his phone's dead. It's unlikely, but it's the only lead I've got."

leaf @talking2mouth "...Sure. I'm willing to try it."

show blank2 with splitfade

pause 2.0

scene city_A with splitfade

pause 1.0

narrator "You and {color=#00b23f}???{/color} make your way to the city. It's not long before you see a familiar face, though wearing an unfamiliar expression."

show nate frownmouth angrybrow with dis

pause 2.0

show nate surprisedbrow frownmouth with dis

ethan @happy "...Hey, Nate!"

nate -surprisedbrow @closedbrow talking2mouth "{size=30}Nardie?{/size} Hey, MC². I'm kinda busy right now."

show nate:
    ease 0.5 xpos 0.25

show leaf frownmouth at rightside with dis

leaf @sarcastic "Yeah? What're you doing? Looks to me like you're just looking at that statue. Having a good conversation?"

nate "{w=0.5}.{w=0.5}.{w=0.5}."

nate sadbrow @closedbrow talking2mouth "I don't--{w=0.5} I mean, I didn't--{w=0.5}"

pause 1.0

leaf @sarcastic "Elucidating."

ethan @talking2mouth "That's a gnarly word."

pause 1.0

show nate surprisedbrow frownmouth with dis

leaf @angrybrow talking2mouth "...Hold on. You were asking me questions about Tia. Then you started asking me questions about [first_name]. Aren't you Cheren's roommate? Were you spying on [first_name] for him?"

ethanmind @confusedeyebrows frownmouth "Tia? Who's that?"

nate @talking2mouth "N-no! No, I wasn't spying on-- okay, well, I {i}was{/i}, but it wasn't for Cheren! I didn't even know that acehole was working with him."
nate sadbrow @sadmouth "You gotta believe me. That guy in purple came up, and offered a trade. I had no idea what he'd do with what I told him. I just needed some information, and he had it."

leaf angrybrow @angrymouth "...{i}What{/i} did you tell him, to get that information, Nate?"

show leaf surprisedbrow frownmouth with dis

nate @talking2mouth "Look, I just... I just told him how to access the security footage from the laboratory's security cameras."

pause 1.0

nate @surprisedbrow sadmouth "It's not {i}that{/i} big a deal! I didn't, like, tell them any secret passwords or anything! All that information's publically available through the school's security room. You just have to walk in there and ask for the recordings!"

ethan @closedbrow talking2mouth "Oh, yeah, we were going to do that our first week here, when we thought [first_name]'s bag was stolen..."

leaf -surprisedbrow -frownmouth -surprised angrybrow angrysmilemouth "If {i}that{/i} was all you did, why are you looking so guilty? You've been asking me a bunch of questions about Tia and [first_name]. You were asking Ethan a bunch of questions, too, weren't you?"

ethan @surprised "Huh? How'd you know?"

pause 0.5

show leaf embarrassed with dis

pause 0.5

ethan @closedbrow talking2mouth "Gotcha. The only reason someone would hang out with me is if they wanted something. I see where you're coming from now. Yeah, you're right."

nate @talking2mouth "MC²..."

leaf angry "Well, Nate? You didn't {i}just{/i} tell him how to get some publically-accessible information. There's something more."

pause 1.0

nate @closedbrow talking2mouth "Look, I... I knew what he was going to find. I watched the vids first. But I didn't think he was going to do something like {i}that!{/i}"

$ firstletter = first_name[0]
nate @angry "I mean, he couldn't exactly try to make some sort of argument that [firstletter] got into the school unfairly without turning a massive lens on himself, right? I didn't think he'd be so stupid!"

leaf -angry frownmouth @angrybrow "{w=0.5}.{w=0.5}.{w=0.5}."
leaf @talking2mouth "What did the video show?"

nate @closedbrow talking2mouth "Not falling for that one again. I purged the database, magnetized the tapes, and put three-factor authentication that has to go through me on any future information requests."

leaf @talking2mouth "Great, so now that the ship is sinking, you think you can just stuff a towel in the holes, and we'll forgive you?"

nate @closedbrow talking2mouth "...I don't particularly care for your forgiveness. I just want [first_name]'s. Or at least the chance to apologize. I really screwed things up for him."

pause 1.0

leaf @talking2mouth "What information did you want so desperately that you were willing to burn down Kobukan to get it?"

nate @talking2mouth "I can't tell you that."

leaf @talking2mouth "Why the hell not?"

nate @talking2mouth "I can't tell you that, either."

leaf @thinking "[ellipses]"

nate @closedbrow talking2mouth "Look. You can't tell anybody about this. But I'm pretty sure there's a dangerous Pokémon hiding out in the forest."
nate angrybrow @talking2mouth "Everyone here could be in danger." 
nate @talking2mouth "Now, I know some people who can subdue the Pokémon, but if I'm going to convince them to come here, I need to know {i}where{/i} the Pokémon is, how powerful it is, and when there will be no-one around."
nate @talking2mouth "Understand? This is bigger than a college student's small secrets. I'll trade away anything I need to make sure I complete my mission."

leaf @sarcastic "...You're a real piece of work."

leaf @closedbrow talking2mouth "Well, since you can't get a single piece of information from two idiots without ruining everything for everyone, and can't fight off a mystery 'dangerous Pokémon', excuse my disbelief, do you at least know where [first_name] is?"

pause 1.0

nate @talking2mouth "No. All my sources have gone silent. The whole school has. No-one's talking to each other. Everyone's hiding out in their dorms... empty classrooms... there are walls between my usual network."

show nate sadbrow with dis

leaf @angry "Gah! Then what good {i}are{/i} you?"

hide leaf with dis

pause 0.5

nate @sad "{size=30}What... good am I...?{/size}"
nate "{w=0.5}.{w=0.5}.{w=0.5}."

ethan @closedbrow talking2mouth "Bye, Nate. It was fun while you were pretending to be interested in me."

nate @talking2mouth "Ethan."

ethan @sadbrow talking2mouth "If you're trying to convince me that you weren't just looking for information on [first_name], {w=0.5}save it."

pause 1.0

nate @closedbrow talking2mouth "I don't know where he is. But B might."

ethan @talking2mouth "Great."

call clearscreens from _call_clearscreens_80
scene blank2 with splitfade 

pause 1.0

ethan @talking2mouth "Leaf."

leaf @talking2mouth "My name's Leaf, but yeah?"

ethan @closedbrow talkingmouth "Nate thinks that [blue_name] might know where [first_name] is."

leaf @surprised "{size=30}Nacho? Who the hell is...{/size} Oh, of course! If you're not [first_name]'s stalker, then [blue_name] totally is!"

ethan @confused "Or, like, you."

leaf @sarcastic "Or Tia."

pause 1.0

ethan @talking2mouth "Sounds to me like Cheren might've had a point."

pause 1.0

show afternoon at vspaz
$ timeOfDay = "Afternoon"

pause 3.5

show screen currentdate
scene stadium_empty 
with splitfade

pause 1.0

show blue angrybrow frownmouth with dis

narrator "As you walk into the Battle Hall, you see {color=#3110dd}???{/color} training. Sweat covers his brow, and soaks through his clothes. He's clearly been working at this, very hard, for a long time."

narrator "His Pokémon have the same sort of stony determination. They all look tired, but they're moving through their paces, attacking, defending, and counterattacking, with a resolute rhythm."

pause 0.5

show blue:
    ease 0.5 xpos 0.25

show leaf frownmouth at rightside with dis

leaf @talking2mouth "Hey, [blue_name]! Are--"

show leaf surprisedbrow with dis

show stadium_empty with vpunch

blue angry "YOU!"
blue angry "You're the reason he went to that goddamn election! This is {i}your{/i} fault!"

ethan @angry "Hey! I didn't even go to the election!"

blue @closedbrow angrymouth "I'm not talking to {i}you!{/i} I'm talking to Leaf!"

ethan @surprised "Oh!"

pause 1.0

ethan @closedbrow talking2mouth "Yeah, that makes a lot more sense. Like, I was going to say, I {i}really{/i} didn't see a way you could blame me for this."

pause 0.5

ethan @confused "Wait, what did Leaf do?"

leaf -surprisedbrow @angry "Nothing!"

blue @angry "You just {i}refused{/i} to step away from him for half a second, so I couldn't talk to him! If I'd talked to him {i}properly{/i} he wouldn't have gone to the election!"

leaf @angry "Bullshit. You could have told him not to go while I was there!"

blue @angry "What do you think I was doing?! It's not like I could tell him in front of you that 'if you go, Cheren will tell everyone about Frienergy!'"

$ PlaySound("idea.ogg")

ethan @confused "...What?"

blue surprisedbrow frownmouth @surprised "...Nothing."

ethan @talkingmouth "No, you said 'Frienergy.'"

blue @closedbrow talkingmouth "...Well, yeah, that's what the power's called. What, weren't you at the damn election? I wasn't, and even I know that."

leaf @sarcastic "Don't think so, bud. Cheren never told us what the power was called."

pause 1.0

blue -surprisedbrow -frownmouth -surprised sweat frownmouth @closedbrow talkingmouth "...Damn."

ethanmind frownmouth "'Frienergy'? Is that what... I have?"

leaf @talking2mouth "Well? How did you... {w=0.5}wait."

pause 0.5

leaf surprisedbrow frownmouth @surprised "You already knew."

pause 1.0

if (oldpersondex["Leaf"]["RelationshipRank"] != 1):
    leaf @angry "I overheard you talking with [first_name] about how all his friends left him in high school, because of something {i}you{/i} did!"
    
leaf @angry "That's what you told all his friends back then! That's how you convinced them to abandon him! Because you convinced them that he was just brainwashing them!"

blue @closedbrow talking2mouth "Tch."

leaf @angry "But that wasn't even enough for you, was it?! You had to go and do it again!"

blue -sweat @surprisedmouth "You don't know what the hell you're talking about."

leaf @angry "Oh, yeah? Because it sounds to me like you were sick of being second-best to [first_name], so you blasted [first_name]'s reputation again, but let Cheren take the fall for it this time!"

show stadium_empty with vpunch

blue angry "Shut {i}up!{/i} No-one listens to me! No-one! So how the hell was I supposed to know Cheren actually {i}was{/i}?!"

leaf surprisedbrow frownmouth @surprised "What?"

blue @talkingmouth "You saw how [first_name] was at the Battle Team meeting on Friday! Mouthing off to Lance like that. 'Oh, I'm on the left side of the room!'"
blue @talkingmouth "I {i}hate{/i} that dumb country boy schtick of his! We're from the same damn town, but he acts like he grew up riding Rhyhorn and milking Tauros!"

leaf -surprisedbrow -frownmouth -surprised flirtbrow frownmouth @sarcastic "Uh-huh."

blue @talkingmouth "So, yeah, I was complaining to Cheren! And I told him that [first_name] gets anything he wants, and {i}everyone{/i} pays attention to him, just because of who he is!"
blue @talkingmouth "That he's just had everything he ever wanted {i}handed{/i} to him!"

ethan @surprised "Wait, so...?"

blue @closedbrow talking2mouth "So Cheren asked if that seemed 'unusual' to me, like he had some sort of 'power!' And I said yeah, because what kind of idiot would think it was an {i}actual{/i} power?!"
blue @angry "I've said shit like that a hundred times, and no-one's ever listened to me! No-one's ever cared that it's unfair! So how the hell was I supposed to know that this {i}one{/i} time someone was listening?"
blue @angry "I was just... I was just {i}venting!{/i}"

pause 2.0

ethan @happy "Seems pretty sus."

show blue angry
show leaf angry
with vpunch

"{color=#00b23f}???{/color} & {color=#3110dd}???{/color}" "\"Shut the {i}fuck{/i} up, Ethan!\""

pause 1.0

show leaf -angry frownmouth 
show blue -angry frownmouth
with dis

leaf @talking2mouth "Well, great job. You ruined his life again. You and Nate."

blue surprisedbrow frownmouth @surprised "Nate? What did that egghead--"

pause 0.5 

blue -surprisedbrow -frownmouth -surprised frownmouth @closedbrow angrymouth "...The lab's security cameras. Damn it, Gramps."

pause 0.5

ethan @talking2mouth "What I don't get is how you knew he had this power in the first place."

show blue surprisedbrow frownmouth with dis

leaf @talking2mouth "Think about it, Ethan. If those purple students wanted to see video footage from the research lab, then [first_name] must have been there. Probably talking to someone." 
leaf @talking2mouth "Who do we know who [first_name] is close to, who hangs out around the Research Center a lot?"

ethan @confused "Uh... that redhead with the right proper Ga'arian accent? What was her name, Sonia?"

leaf @closedbrow talking2mouth "God."

ethan @surprised "God?!"

leaf @angry "NO! I'm saying 'god,' you're literally painful to talk to!"

ethan @talking2mouth "Yeah, uh, some people would say the same thing about you, princess. You're kinda 110%%, all the time."

leaf @angry "Well at least I'm not 0%% all the time!"

blue @angry "Oh my god, would you two shut up?! Yeah, Gramps told me! Over and over and over, believe me." 
blue -surprisedbrow -frownmouth -surprised frownmouth angrybrow @angry "There wasn't a single goddamn second when I was a kid when I wasn't being {i}reminded{/i} that [first_name] had this 'special power' that made him {i}sooo{/i} much more important than me!"

pause 1.0

leaf sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

leaf @talking2mouth "That... I mean, you're still an {i}enormous{/i} douchebag, but..."

blue @angry "Can it. I don't need sympathy from [first_name]'s hanger-on and clone."

leaf -sadbrow @angrybrow angrysmilemouth "Well, you're not getting it, now."

ethan @confused "I was never offering it."

leaf @talking2mouth "Do you at least know where [first_name] is?"

blue @talkingmouth "No, but he's probably with his other Student Council nerd friends. I bet they're all decorating the student council room right now."

leaf @talking2mouth "Are you serious?"

blue @surprised "What?"

leaf @talking2mouth "You seriously think [first_name]--any of them--got elected? After Sabrina dropped her bombshell, there was a twenty-minute riot in the auditorium. {i}Lance{/i} had to step in to quiet everything."
leaf @sad "The only one of the Student Council hopefuls still on the stage by the time Lance stepped in was Jasmine, and I think she was three seconds away from fainting."

blue @surprised "...Seriously?"

leaf @surprised "Uh, yeah! Why are you so surprised?"

pause 1.0

blue @closedbrow talking2mouth "...I'm not used to something actually going {i}badly{/i} for [first_name]. Even with my screwup, I figured..."

show lance
show blue surprisedbrow frownmouth
show leaf surprisedbrow frownmouth 
with dis

lance @talking2mouth "I can assure you, Mr. Oak, that this went {i}very{/i} poorly for {i}everyone{/i} involved."
lance @closedbrow talking2mouth "A third of the school's student population was involved in that nonsense. The news, I imagine, has spread to the other two-thirds."
lance @angrybrow talking2mouth "And {i}someone{/i} is going to have to clean up your messes. The school has already incurred two significant legal actions as a result of that catastrophe."

pause 1.0

lance @talking2mouth "I might have known that the first major crisis this year would be because of you and [first_name], Blue."

blue @angry "Hey! I {i}just{/i} explained that--"

lance @angry "You just made an excuse. Take responsibility for your mistake."

blue sadbrow frownmouth @talkingmouth "...I..."

leaf -surprisedbrow -frownmouth -surprised @talking2mouth "Advisor Lance."

lance @sadbrow talking2mouth "I cannot begin to describe how frustrated I am right now. Think {i}very{/i} carefully about whether what you are about to say needs to be said."

leaf @talking2mouth "Do you know where [first_name] is?"

lance @angry "{size=30}.{w=0.5}.{w=0.5}.{w=0.5}I give good advice, and the children just ignore it.{/size}"
lance @sadbrow talking2mouth "No, I do not. But, if he is intelligent, which there is not yet any evidence of, he'll make sure I do not know where he is for {i}at least{/i} one week."

leaf frownmouth @sad "Oh."

pause 1.0

lance @sadbrow talking2mouth "...But, if I were to hazard a guess as to who might know, I would point you in the direction of Professor Oak. He seems to have a close relationship with the boy."
lance @talking2mouth "I imagine he sees something of interest in young Mr. [last_name], though I can't imagine what. A fascinating gut flora, perhaps."

leaf @talking2mouth "Right. Thank you, advisor."

hide lance with dis

leaf @angry "C'mon, Ethan. We're getting answers to this."

pause 1.0

blue -sadbrow @talkingmouth "Wait."

leaf @talking2mouth "Hm?"

blue @closedbrow talkingmouth "Did [first_name] freeze? Go completely silent while he was up there?"

leaf @talking2mouth "Yeah."

blue "{w=0.5}.{w=0.5}.{w=0.5}."
blue @talkingmouth "...I didn't know him. Not really, not until he got over it. But when we were kids... until we were eight or so..."
blue @closedbrow talkingmouth "He was {color=#ff0000}silent.{/color}"

ethan @surprised "Huh?"

blue @talkingmouth "Not completely. He would sometimes yell, or grunt, or mutter something no-one could hear."
blue @closedbrow talkingmouth "The doctors said he was perfectly fine. As far as they could tell, he just... didn't see the need to talk."

pause 0.5

blue @talkingmouth "The one time I heard him say anything, it was 'words are unnecessary.' So you've got an idea of the kind of kid he was."
blue @angry "Anyway, that's when Gramps got bored of his current project, and decided that 'curing' [first_name] would be a great way to spend my lifetime."

ethan @confused "How did he do it?"

blue @closedbrow talking2mouth "I don't know. But sometimes I wish he hadn't. Now you can't get [first_name] to shut up."
blue @angry "Hey, when you find [first_name], you tell him to find me, huh? I'll be right here. I'm not going to stop training 'til I see his ugly mug, and can beat it in for being a hard-headed dumbass again."

leaf @talking2mouth "...We need to see your grandfather, then."

blue @talkingmouth "Yeah. Smell ya later."

hide blue 
hide leaf 
with dis

pause 1.0

ethanmind @closedbrow talking2mouth "I don't really see the point of me being in this scene."

scene blank2 with splitfade

pause 2.0

scene research 
show oak angrymouth at leftside
with splitfade

pause 1.0

show leaf frownmouth at rightside with dis 

leaf @talking2mouth "Professor Oak."

oak @surprised "Oh? Oh, yes, Ms. Green."
oak @closedbrow talking2mouth "I'm sorry, Ms. Green, but my office hours are closed."

$ hideside = True

hide oak with dis

oak @closedbrow talking2mouth "Please come back tomorrow, after class--"

show leaf with vpunch 

leaf @talking2mouth "Wait!{w=0.5} It's about [first_name]."

pause 1.0

show oak angrymouth at leftside with dis

oak @talking2mouth "...I feared as much."

leaf @talking2mouth "Please, Professor. Tell us everything."

oak @angrybrow "{w=0.5}.{w=0.5}.{w=0.5}."
oak @closedbrow talking2mouth "I suppose this data is irretrievably corrupted. I certainly won't be publishing any more. So I will answer three questions."

leaf @surprised "What? Only three questions?"

oak @talking2mouth "I've recently spent the better part of two decades working towards an academic dead end. It's only the promise of the meteor project that you don't find me collapsed in my office, smelling strongly of whisky."
oak @closedbrow talking2mouth "My time, for now, is still valuable."

pause 1.0

leaf @talking2mouth "...Fine. What is [first_name]'s power?"

oak @talking2mouth "It's a simple empathy inducer. Those around him cannot help but feel his feelings, understand his intent, truly {i}know{/i} him."
oak @sadbrow talking2mouth "I named his power Frienergy. A kind, humble name. I believed that it could revolutionize our understanding of humanity's bonds, and our bonds with Pokémon."

pause 1.0

oak @talking2mouth "I did not consider that the feelings of those affected would be as strong as they are."
oak @sadbrow talking2mouth "...As you have seen, in this world, there are many who consider being asked to show empathy a direct attack."
oak @closedbrow talking2mouth "I should have anticipated that this power which, by its own nature, could not be kept secret forever, would reveal itself damagingly."

leaf @talking2mouth "So... it's not mind control?"

oak @talking2mouth "Not at all. It is kindness. Pure, concentrated, unconditional kindness. Which, naturally, is an enormous threat to the way of things."

leaf "{w=0.5}.{w=0.5}.{w=0.5}."
leaf -frownmouth @talkingmouth "So... he wasn't mind controlling me? The reason I liked him so much is because... he, uh... wanted that?"

oak @surprised "Er...? Well, I cannot speak to the specifics of your particular case, but... if you had a fondness for him, it's very likely he had a fondness for you, too."

$ hideside = False

leaf @blush talkingmouth closedbrow "Knew it."

pause 1.0

leaf @talking2mouth "Alright, I'm happy. Ethan, you can ask your questions now."

ethan @surprised "Huh?"

oak @surprised "Er... you asked three."

leaf @talkingmouth "Sure, but you said we can both ask three."

oak @angrybrow talking2mouth "No, I didn't."

leaf @sarcastic "Didn't you?"

oak @surprised "...No?"

leaf @talking2mouth "Yes."

oak @sad "Yes?"

leaf @talking2mouth "Well, if you insist. Ethan, go ahead."

ethan @talkingmouth "{size=30}Gaslighting an old man, nice. All you gotta do now is gatekeep and girlboss.{/size}"

leaf @angrybrow angrymouth "{size=30}Are you going to complain, or ask your questions?{/size}"

ethan @closedbrow talking2mouth "{size=30}Oh, don't think I can't do both. I am {i}quite{/i} the multitasker.{/size}"

pause 0.5

ethan @happy "Um... Professor Oak. Hey."
ethan @talkingmouth "I don't think we've ever met before. But, uh, Professor Cherry has told me a lot about you. She really respects you."

oak @sadmouth "We'll see if that's the case this afternoon. I believe we teachers are meant to have a meeting to discuss the events of the Student Council election."
oak @sadbrow talking2mouth "Oh, when I think that I {i}encouraged{/i} all my students to go there..."

ethan @talking2mouth "Right. Um, here's my question. [first_name] and I, like... end up in the same place... doing the same thing... making the same decisions."
ethan @confused "Is that, like, a side-effect of Frienergy?"

oak @surprisedbrow talking2mouth "No."

ethan @surprised "Oh."

pause 1.0

ethan @confused "Is there, like, even a chance?"

oak @talkingmouth "No. At its most powerful, Frienergy might influence someone to follow a wielder, given the bonds of trust inherent in such a thing."
oak @talking2mouth "But what you're describing--a persistent, systemic 'copying' effect--is outside the realm of the Frienergy I've studied."

ethan @closedbrow talking2mouth "Well, that's a dead end."

oak @talkingmouth "I am... {i}mildly{/i} interested in this phenomenon you mentioned, though. Perhaps, when I am able to publish my meteor thesis, I'll see what is happening to you and [first_name]."

ethanmind @thinking "Great. Second place to a rock."

ethan @confused "Okay. Question number two, then. [blue_name] told us that you told him about Frienergy. If you were trying to keep this a secret from everyone but [first_name], why would you tell [blue_name]?"

oak @closedbrow talkingmouth "Well, quite simply, he asked why I was spending so much time with his best friend. And I'm a firm believer that family shouldn't have secrets from each other."

ethan @confused "You didn't think that would give him a complex? That his best friend had some sort of super power that made people like him?"

oak @closedbrow talking2mouth "{size=30}That is {i}not{/i} what Frienergy does. Why must the discoveries of science be constantly misinterpreted by the public in the least charitable fashion?{/size}"
oak @talking2mouth "In any case, no, I did not think that would give him any sort of 'complex'. He is confident enough in himself that I daresay {i}nothing{/i} could so much as give him reason to pause, let alone a complex."

leaf @surprised "{size=30}Wow. Ol' Sam's a {i}terrible{/i} judge of character.{/size}"

ethan @closedbrow talking2mouth "{size=30}Yeah, I'm learning a lot about the faculty of Kobukan today.{/size}"

oak @closedbrow talking2mouth "You've one more question."

ethan @talkingmouth "Right. I really only wanted to know those two, to be honest, but... well, we've asked everyone else, and no-one else knew, so... do you know where [first_name] is?"

oak @closedbrow talking2mouth "Hm."
oak @talking2mouth "No. Did you check the city?"

leaf @sarcastic "Yeah. I mean, not all ninety square miles of it, but a bit."

oak @closedbrow talking2mouth "What about the Battle Hall?"

leaf @sarcastic "We're both Battle Team members. Yes, we checked the Battle Hall."

oak @sad "I'm afraid I've no idea, then. But if you see him, do make sure to let me know, if you will. I'd like to talk to him about his place in this academy, given... recent developments."

show leaf angrybrow frownmouth with dis

leaf @talking2mouth "...Sure."

call clearscreens from _call_clearscreens_81
scene blank2 with splitfade

pause 1.0

narrator "You and {color=#00b23f}???{/color} end up spending the rest of the day crossing the campus searching for [first_name]." 
narrator "{color=#00b23f}???{/color} rummages through every bush in the gardens."
narrator "You look in every stall in the sports center locker rooms."
narrator "{color=#00b23f}???{/color} even drags you up to a women's restroom near the cheer squad's changing room, for some reason."
narrator "Unsurprisingly, he's not there, either."

pause 1.0

narrator "Eventually, the two of you awkwardly part ways, with you promising to call {color=#00b23f}???{/color} if [first_name] is back at your dorm."

pause 1.0

narrator "Of course, you don't have her number..."

pause 1.0

show night at vspaz
$ timeOfDay = "Night"

pause 3.5

narrator "You're almost back to your dorm, when you spot a familiar man, standing in a familiar garden, staring up at a familiar sky."

scene garden night 
show drayden sad at night
with splitfade

pause 2.0

ethan night @talking2mouth "Dean?"

pause 1.0

drayden @neutraleyes neutraleyebrows "...Mr. Gold."

ethan @talking2mouth "Are you alright?"

pause 1.0

drayden @neutraleyes neutraleyebrows "It breaks my heart, Mr. Gold. One day, you're all children, fresh-faced and excited to face the world."
drayden -sad sadbrow "And the next... you're men and women, in a war. A war of survival. Against the world, against each other, against yourselves."

pause 1.0

drayden -sadbrow "But the stars still shine for you."

pause 1.0

drayden @neutraleyes neutraleyebrows "Oh, they still shine for you. There's no doubt about that. But do they shine for me?"
drayden @sad "Is there something I could have done differently?" 
drayden @sad "I disallowed faculty from attending the elections with the thought that you would be more free, more honest, about your thoughts and desires without the administration breathing heavily down your neck."
drayden @neutraleyes neutraleyebrows "Was that a mistake? Was I, Drayden, meant to anticipate the cruelty of men who believe themselves to be on the side of truth?"

pause 1.0

ethan @talking2mouth "I couldn't say, Sir."

drayden @neutraleyes neutraleyebrows "No, I don't think anyone could. Pardon my ruminations."

ethan @talking2mouth "...What will happen to those students? To everyone involved?"

drayden @angrybrow "Mr. Cheren requested to be expelled. I refused him, insisting he take responsibility for his actions."
drayden @neutraleyes neutraleyebrows "I'm unsure, for now, what form that responsibility will take. Whatever the case, there are hundreds of students who are scared, upset, and angry."
drayden @happybrow "I'm half-tempted to place him in the Student Council, and make him deal with the mess he caused."

pause 0.5

drayden @angrybrow "But I think that would send the wrong message to the student body. His fate remains to be seen."

pause 0.5

drayden @sad "...Those incestuous siblings have been pulled from the school. Their parents, who are on the board of trustees, are understandably upset. I fear a phone call from the President of the university any minute now."
drayden @neutraleyes neutraleyebrows "Mr. Calem and Ms. Serena have, I believe, taken temporary off-campus accommodations. They likely need time to process, refocus, and prepare to face their mundane day-to-day once more."
drayden "Ms. Jasmine, though distressed, has showed remarkable improvement today. I believe she'll be back in classes tomorrow."
drayden @sadbrow "Mr. Grusha, however... The fall from the stage exacerbated his condition. I do hope that he recovers quickly. But his doctor recommended he spend a bit more time in the infirmary."

pause 1.0

drayden "Given the extraordinary circumstances, I've asked the previous Student Council to remain onboard for as long as they are willing."
drayden @angry "I was never fond of them." 
drayden @angry "A slacker who was elected purely through popularity, a woman who demanded irrational, massive, sweeping changes to our very academic system, and then a third, sensible fellow neither of the other two listened to."
drayden @sad "But, at the very least, they managed to avoid getting into a fight onstage that caused the entire student body to turn against itself."
drayden @angrybrow "I truly didn't think that was a positive quality I should have commended them for, last year."

pause 1.0

drayden sad "And... well. As for Mr. [last_name]. I suppose I needn't tell you what's happened to him."
drayden "I tried to stop him. But... whereas Cheren, at least, I could cow into following my will, it felt like there was no force of nature, no man or beast, that could move [first_name] from his path."

ethan @surprised "Wait... what? I've been trying to figure out where [first_name] went all day!"

drayden surprisedbrow @surprised "Oh."

stop music fadeout 10.0

pause 1.0

drayden -surprisedbrow -surprised sad "This is... exceedingly painful for me to tell you, then."

ethan @sadbrow talking2mouth "What... what do you mean, Dean?"

drayden "Ethan."
drayden @neutraleyes sadwrinkles sadeyebrows "Last night, almost exactly twenty-four hours ago, [first_name] visited me in my office. He didn't say a word, but he held with him a piece of paper."

ethan @shadow talking2mouth "Wait."

drayden "Ethan... "

call clearscreens from _call_clearscreens_82
show blank2

pause 1.0

extend @talkingmouth "{cps=20}{color=#ff0000}[first_name] [last_name] dropped out of Kobukan.{/color}{/cps}"

pause 5.0

jump day010503
