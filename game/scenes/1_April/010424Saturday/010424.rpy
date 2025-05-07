label day010424:

$ timeOfDay = "Early Morning"
call calendar(1) from _call_calendar_19
$ calDate = calDate.replace(day=24, month=4, year=2004)

show blank2
queue music "Audio/Music/Show Me Around.ogg"
show earlymorning at vspaz

pause 3.5

$ renpy.transition(dissolve)
show screen currentdate

scene garden:
    zoom 0.625
show clouds behind garden

hide earlymorning    
hide blank2

play sound "audio/bigcrowdloop.ogg" channel "crowd" fadein 1.5

if (HasEvent("Instructor Valerie", 1)):
    narrator "Waking up at the crack of dawn, you drag yourself out of bed and into the gardens, where Instructor Valerie is ready to begin the egg hunt."
else:
    narrator "Waking up at the crack of dawn, you drag yourself out of bed and into the gardens, where an eccentrically-dressed instructor is ready to begin the egg hunt."

show valerie with dis

valerie @talkingmouth "Good morning, my darling Beautifly."

valerie @happy "Happy Springsday, everyone. Today is the day where the Buneary hop around in the fields, the Psyduck swim in their lakes, and the Vivillon waft about, spreading happiness to all the new life."

$ PlaySound("Pokemon/Ball sound.ogg")
$ PlaySound("pokemon/cries/54.mp3")

$ sidemonnum = 54

show sideportraitfull:
    xpos 1.2 zoom 0.85 ypos 0.8
    ease 2.0 xpos -0.2


pause 1.0

misty @surprised "Wha- Psyduck, stop! She wasn't calling you!"

valerie @closedbrow talking2mouth "Today is a day of celebration, as we all become more aware of our place in the great circle of life."

valerie @happy "Let joy fill your hearts, each and every one of you. For you are young, and the new life that springs from you will guide the future of Kobukan, and the world."

calem @surprised "{size=30}We... {i}we{/i} are young? She can't be any older than twenty-five.{/size}"

valerie @happy "It is my pleasure--and my privilege--to begin Kobukan's 124th annual Springsday egg hunt."

$ PlaySound("crowd_cheer.ogg")

stop music channel "crowd" fadeout 1.5

pause 1.0

valerie @happy "Go out, my Beautifly. Fly and unite your youthful souls with the new births waiting to be discovered."

hide valerie with dis

pause 1.0

show leaf with dis

leaf @happy "It's time for egg hunts and bunny suits! Who's ready for the Springsday celebrations?"

show leaf frownmouth 
show blue at leftside 
with dis

blue @happy "Hah, [first_name]--"

show blue surprisedbrow frownmouth with dis
show brendan frownmouth at rightside with vpunch

brendan @angry "That's enough, bro. You're always gettin' on [first_name]'s case. You better back off."

blue -surprisedbrow -frownmouth -surprised @angry "Oh, yeah? Or what? You gonna do some pull-ups at me?"
blue @happy "I'm the ace of the Kobukan Battle Team! I'd beat you with my Poké Balls tied behind my back."

brendan @angry "Yeah, but I'm roommates with {i}three{/i} other Battle Team members, and they've got {i}my{/i} back."

show blue:
    ease 0.5 xpos 0.2

pause 1.0

blue @surprised "So, you, [first_name], Hilbert, and that loser, Ethan, are all dormmates?"

show ethan behind brendan with dis:
    xpos 0.65

ethan @happy "Hey, you remembered me!"

blue @talkingmouth "Yeah, I saw your 'battles.' If there's anyone in this school who deserves their battle position less than this loser, it's you."

ethan @closedbrow talking2mouth "Well, I can't exactly deny that..."

leaf @talking2mouth "Y'know, you're not actually a bad battler. You beat me in the tryouts."

blue @surprised "Wasn't hard. Is there a {i}point{/i} to this?"

leaf @angry "What the hell are you trying to prove?! You've got skills! We get it! It's literally just your awful personality that we hate!"
leaf @angrybrow angrymouth "Is your ego really so fragile that you need to spend every moment of every day proving you're better than everyone else?"
leaf @sarcastic "Seriously, just buy a lifted truck and leave [first_name] alone."

blue @closedbrow happymouth "Pah. I'm not stopping 'til [first_name] finally admits I'm a better trainer than him, once and for all!"

pause 1.0

show blue surprisedbrow frownmouth with dis

pause 2.0

show garden with vpunch

blue -surprisedbrow -frownmouth -surprised frownmouth @angry "{size=40}Well, [first_name]?!{/size}"

red @surprised "Huh? Sorry, what's happening? Kinda zoned out. [pika_name] is a bit cranky, so I was giving him a massage."

$ hideside = False

$ PlaySound("pokemon/pikachu_sad.ogg")
pikachu sad_2 "Pi-ka..."

blue @angry "Gah! What a waste of space. You're not taking this seriously at all, are you?"

red @talkingmouth "Not taking anything seriously has worked out pretty well for me so far."
red @closedbrow talking2mouth "Anyway, what're you talking about? The egg hunt?"

blue @angry "It's more than just an egg hunt!"

leaf @sarcastic "I mean... it literally {i}is{/i} an egg hunt, though. I mean, {i}kids{/i} do this stuff."

blue @closedbrow talkingmouth "Whatever. I guess you just don't get it."

brendan @closedbrow talkingmouth "...Uh... what am I not getting?"

blue @surprised "{w=0.5}.{w=0.5}.{w=0.5}."

blue @closedbrow talkingmouth "Look, since you guys are so slow, I'll take pity on you."

ethan @closedbrow talking2mouth "How gracious."

blue @talkingmouth "This isn't just your average egg hunt. Each of the Pokémon in these eggs are the descendants of a top trainer's Pokémon."

blue @happy "There are some Pokémon here that were sired by a champion's Pokémon! So you better believe they're all powerful as all get-out, and I'm going to get every single one of them!"

brendan @angry "Hey! Don't be a dick, man. Don't be greedy."

blue @talkingmouth "It's loser talk like that that means you'll always be second-place to us Battle Team members."

brendan @closedbrow talkingmouth "Uh... I don't want to be on the Battle Team, though. I'm going to be a coordinator."

blue @surprised "What, like those girls who wear skirts and dance with their Pokémon?"

brendan @talking2mouth "Yeah, uh, there's actually a lot more to it than that. You don't have to be a girl, for one."

blue @angry "Whatever! Just make sure none of you get in my way! I'm going to grab more eggs than all you losers put together!"

hide blue with dis

show ethan:
    ease 0.5 xpos 0.25

pause 1.0

brendan @angry "Man, what is that guy's {i}problem?{/i}"

leaf @sarcastic "It's a little something we call 'small PP syndrome.'"

brendan @closedbrow talkingmouth "I mean, he could just buy a PP Up. They're not that expensive."

pause 1.0

leaf @happy "Hah, I see what May sees in you. You're cute, in a muscular kind of way."

ethan @closedbrow talking2mouth "So, about what Blue was saying...?"

leaf @talkingmouth "Oh, yeah, he was pretty much right. I mean, he was a dick, but this is a seriously good opportunity to pick up some powerful Pokémon."

ethan @talkingmouth "They'll all be level one though, right?"

red @talkingmouth "Sure, but we're just at the beginning of our own school years. It'll be pretty easy to catch them up."

ethan @sadbrow happymouth "Easy for you, maybe, Man. I copy your notes in our elective classes, but I still don't do as well as you."

$ starter_preposition = ("a" if starter_species_name[0] not in ["A", "E", "I", "O", "U"] else "an")
leaf @surprised "Oh, right, you two have that weird magnetism thing, where you both ended up with [starter_preposition] [starter_species_name] for your starter, right? And you randomly end up in the same electives all the time?"

red @talking2mouth "Yeah. It's weird, because we're both pretty sure we're not doing it on purpose, but... I haven't made any progress on figuring out why that's happening."

redmind @thinking "Could it be some sort of weird side-effect of Frienergy? Feels like the kind of thing Sam would have mentioned, though..."

brendan @closedbrow talkingmouth "Hey, did you guys ever figure out why your Pokémon listen to you so well?"

show red surprisedbrow frownmouth at Transform(xpos=0.08, yanchor=0.35)
show ethan surprisedbrow frownmouth 
show leaf surprisedbrow frownmouth
show brendan surprisedbrow frownmouth
with dis

"{color=#cf0000}[first_name]{/color} & {color=#c1861e}Ethan{/color}" "\"Huh?\""

show ethan thinking 
show red thinking 
with dis

"{color=#cf0000}[first_name]{/color} & {color=#c1861e}Ethan{/color}" "\"Uh...\""

show ethan happy
show red happy 
with dis

"{color=#cf0000}[first_name]{/color} & {color=#c1861e}Ethan{/color}" "\"They really trust me!\""

pause 1.0

hide red 
show ethan -happy
show brendan -surprisedbrow -frownmouth -surprised
show leaf -surprisedbrow -frownmouth -surprised
with dis

leaf @closedbrow talkingmouth "Wow, so, {i}that{/i} was creepy."

pause 1.0

leaf @talking2mouth "Hey, do you think you two could put on some dresses, stand at the end of a dimly-lit hallway, and say 'come play with us?'"

brendan @talking2mouth "Oh, like in that one movie of Rosa's, right? {i}The Glimmering{/i}?"

leaf @surprised "Oh, you watch horror?"

brendan @talking2mouth "Eh, if it's on TV. May hides her face in my chest whenever we sit down to watch one, so we're both kinda distracted."

ethan @talkingmouth "Horror films are awesome! You guys ever watched 'Strong Jaws: The Revenge?' It's great."

menu:
    "{color=#b7669e}[[Charm]{/color} I watch horror, too!":
        $ TraitChange("Charm")

        brendan @happy "Oh, yeah? Maybe we should do a watch-together or something. I heard the Human Sizzlipede's pretty awful. In a 'ya gotta see it' kinda way!"

    "{color=#ff8412}[[Courage]{/color} Can't stomach the stuff, myself.":
        $ TraitChange("Courage")

        brendan @talking2mouth "Eh, that's alright, man. We all like different stuff. More of an action film guy?"

        leaf @happy "No way! That'd be basic, but understandable, at least. But this guy likes old black-and-white films! Like Brycen's old stuff!"

        brendan @talking2mouth "Still cool. Like I said. Different strokes."

$ PlaySound("Phone.ogg")

pause 1.0

brendan @talking2mouth "Oh, that's May. She said she had a lead on an egg she really wanted, so I'm going off to meet her now!"

brendan @happy "See ya guys!"

hide brendan with dis

pause 1.0

red @confused "So, May's already made plans for when she's going to get that egg, huh?"
red @closedbrow talking2mouth "At the risk of giving a bit of credit to [blue_name], maybe I don't get how serious this actually is?"

leaf @talking2mouth "Well, it's like he said. There's a bunch of Pokémon eggs out there, and you can keep any you find."

ethan @talking2mouth "Though we gotta bring them to the incubator in the Research Lab before the end of the day. They're close to hatching, but aren't done, yet."

leaf @talkingmouth "Yeah, but there's no rush there. As long as you don't, like, throw an egg in your backpack and forget about it for three days, it'll be fine."

red @closedbrow talking2mouth "Hm... you got any advice, you two?"

leaf @happy "[bluecolor]You should probably be able to recognize the eggs from the pattern on the outside, and where they're located!{/color}"

ethan @talkingmouth "Yeah, Mr. Alder said that the eggs belong to baby Pokémon, and their eggs usually look exactly like the Pokémon inside."

leaf @talkingmouth "There aren't any, like, prizes, for getting more, or getting specific ones, so just pick up whatever you want."

pause 1.0

leaf @closedbrow talking2mouth "But maybe not {i}every{/i} single one you want. Like, don't be a dick."

ethan @talkingmouth "Hey, uh, what's the threshold for dickishness?"

leaf @sarcastic "I dunno. Three, maybe? I wouldn't take any more than three."

ethan @closedbrow talking2mouth "What happens if we end up picking up an egg we don't want?"

leaf @talking2mouth "[bluecolor]If you have an egg you don't want, you can just donate it to the Research Lab. At the end of the egg hunt, the school will call us all back, and the Student Council will gather up the eggs."

red @happy "Cool. Guess I've just got one more question, then."

leaf @happy "Yeah?"

red @confused "How do you know all this?"

leaf @talking2mouth "Oh, it was explained during that homeroom you missed because you were too busy hanging out with the meteor girl."

ethan @surprised "Uh... a meatier girl? Who, Beatroot?"

show leaf surprisedbrow frownmouth with dis

red @angrybrow talking2mouth "Leaf, that's meant to be private."

leaf -surprisedbrow -frownmouth -surprised frownmouth @sad "Ah... I'm really sorry! I just... I genuinely forgot you were there, Ethan."

red @surprised "Leaf!"

ethan @happy "Nah, it's fine. I'm used to it. What'd I say, [first_name]? {i}Your{/i} friends."

red @sad "Ethan..."

pause 1.0

redmind @thinking "Damn, where's Calem when you need him? He usually smooths over awkward stuff like this."

pause 1.0

ethan @closedbrow talking2mouth "Man, where's Catcher-In-The-Rye?"

leaf -frownmouth @talking2mouth "Oh, Serena said she had plans for him, and dragged him off somewhere. I think she's got some eggs she wants, too."

ethan @talkingmouth "Shame that Hamburger refused to get up before 7. He'll miss out on a bunch of eggs."

red @closedbrow talking2mouth "Yeah, Hilbert's been moody ever since he got into the Battle Team."

leaf @sarcastic "What, like he isn't normally?"

red @happy "Fair enough! But there's different levels of Hilbert moody."

ethan @happy "Yeah! There's Threat Level: One. That's when he's just scowling at everyone around him, maybe muttering stuff under his breath."

red @happy "Shortly after that is Threat Level: B. This is the point at which he makes audible threats."

ethan @closedbrow talking2mouth "Threat Level: III is scary. That's when Haraam starts yelling. Dude's, like, nineteen, but his voice still cracks when he yells at you."

red @surprised "Finally, the dreaded Threat Level: Midnight. That's when he brings an Aegislash to class."

leaf @surprised "Uh, has he done that?"

red @closedbrow talking2mouth "Nah, but give him twenty-four levels and a Dusk Stone, and he will."

pause 1.0

leaf @happy "Oh my god, you guys are {i}such dorks{/i}!"

show red happy at Transform(xpos=0.08, yanchor=0.35)
show ethan happy 
show leaf surprisedbrow frownmouth
with dis

"{color=#cf0000}[first_name]{/color} & {color=#c1861e}Ethan{/color}" "\"I resemble that remark!\""

hide red
show ethan -happy 
with dis

leaf -surprisedbrow -frownmouth -surprised @closedbrow talking2mouth "Yeah, still creepy."

ethan @talkingmouth "So, you got any eggs you want to grab?"

leaf @talkingmouth "Nah. Maybe if something shows up, but... nothing I'm specifically looking for."

leaf @happy "I'll probably just battle people for their eggs, and be like, 'mwahaha! Now all your eggs are belong to me!'"
leaf @sarcastic "But I won't actually take the egg, or anything." 
leaf @talkingmouth "I just think the battling would be fun."

red @talkingmouth "Maybe we'll cross paths, then. Unless you want to go together?"

leaf @flirttalk "You just can't get enough of me, can you?"
leaf @happy "Sorry, boys, but I've got my own plans today. I'm going to be {i}so busy{/i} battling. Don't have time to get sidetracked by stuff like 'the actual objective.'"

red @happy "Well, have fun on your sidequests, then."

hide leaf with dis

pause 1.0

red @talkingmouth "Hey, Ethan. You wanna come with?"

ethan @happy "Sure thing, man."

red @happy "Right behind you?"

ethan @surprised "Huh?"
ethan @happy "Well, sure, man. Thanks!"

show iris uniform with dis:
    xpos 1.1 ypos 1.4
    ease 2.0 xpos 0.5

pause 2.0

red @confused "Huh, did you hear something?"

ethan @closedbrow talking2mouth "Huh? I don't think so?"

iris @happy "Hey, Misters! Down here!"

red @confused "Down? Down where?"

show garden:
    zoom 0.625 xalign 0.5 yalign 0.5
    ease 0.5 zoom 0.8 yalign 0.9

show ethan:
    xpos 0.25
    ease 0.5 ypos 0.7

show iris:
    ease 0.5 ypos 1.1

ethan @talkingmouth "Oh, hi! You must be another student."

red @closedbrow talking2mouth "Not unless the school lets six-year-olds enroll." 
red @sadbrow happymouth "Hey, sweetie. Are you meant to be here? And where'd you get that uniform!"

iris @happybrow talkingmouth "I am {i}totally{/i} meant to be here! Daddy gave me it!"
iris @angrybrow happymouth "He said it was a 'sguise! So as long as I'm wearing it, I can go anywhere, and no-one can do nothing about it!"

red @confused "Right, of course, sweetie. Very sneaky. Um, who's your Daddy?"

show garden:
    zoom 0.8 yalign 0.9
    ease 0.5 zoom 0.625 xalign 0.5 yalign 0.5

show ethan:
    xpos 0.25
    ease 0.5 ypos 1.0

show iris:
    ease 0.5 ypos 1.4

red @closedbrow talking2mouth "{size=30}Think we should call someone? I don't know how to handle kids.{/size}"

ethan @talkingmouth "{size=30}I mean, she must be, like, a staff member's kid, right? I think it's probably fine. Actually, I think I've seen her before.{/size}"

show garden:
    zoom 0.625 xalign 0.5 yalign 0.5
    ease 0.5 zoom 0.8 yalign 0.9

show ethan:
    xpos 0.25
    ease 0.5 ypos 0.7

show iris:
    ease 0.5 ypos 1.1

iris @happy "...So that means Daddy's in charge of you all! He's the one who makes the rules 'n stuff."

red @happy "Okay. Well, if your Dad is a teacher here, then I guess it's fine. But my buddy and I are going to be going on an egg hunt soon, so..."

iris @surprised "{i}*Gasp!*{/i} An egg hunt! Can I join?"

show garden:
    zoom 0.8 yalign 0.9
    ease 0.5 zoom 0.625 xalign 0.5 yalign 0.5

show ethan:
    xpos 0.25
    ease 0.5 ypos 1.0

show iris:
    ease 0.5 ypos 1.4

red @talkingmouth "{size=30}You cool with it?{/size}"

ethan @talkingmouth "{size=30}I guess? Probably better she tags along with us than she tries to hitch a ride with Blue.{/size}"

red @closedbrow talking2mouth "{size=30}Eeesh. Yeah, for real.{/size}"

show iris:
    ease 0.2 ypos 1.3
    ease 0.2 ypos 1.4
    ease 0.2 ypos 1.3
    ease 0.2 ypos 1.4

iris @surprised "Ooh! Misters, I almost forgot my manners!"

show garden:
    zoom 0.625 xalign 0.5 yalign 0.5
    ease 0.5 zoom 0.8 yalign 0.9

show ethan:
    xpos 0.25
    ease 0.5 ypos 0.7

show iris:
    ease 0.5 ypos 1.1

$ BecomeNamed("Iris")
    
iris @talkingmouth "I'm Iris Blanc! I'm twelve and a half years old! And I'm a really good Pokémon Battler!"

red @talkingmouth "Aw. I'm [first_name] [last_name], and this guy is Ethan."

ethan @talkingmouth "Yeah, Ethan Gold."

red @confused "Gold? Seriously? I don't think I knew that."

ethan @happy "It's kinda a dorky name, so... yeah... I don't usually tell people."

iris @happy "I think your name is really cool, Mr. Gold!"

ethan @surprised "{i}M-Mister?{/i}"
ethan @closedbrow talking2mouth "Ah, jeez, I'm only eighteen. Is this how Calemflower felt...?"

show garden:
    zoom 0.8 yalign 0.9
    ease 0.5 zoom 0.625 xalign 0.5 yalign 0.5

show ethan:
    xpos 0.25
    ease 0.5 ypos 1.0

show iris:
    ease 0.5 ypos 1.0

iris @happy "C'mon, Misters [last_name] and Gold! Let's get some eggs!"

red @talkingmouth "Where to first?"

$ wasdick = False
$ mayhaslarvesta = False
$ beahastyrogue = False
$ calemhastogepi = False
$ biancahaswynaut = False
$ skylahasmantyke = False
$ rosahastoxel = False

$ magbytaken = False

init python:
    def PlacesVisited():
        return visitedbaseballfield + visitedaurahall + visitedbattlehall + visitedacademy + (visitedrelichallmorning or visitedrelichallafternoon) + visitedstudentcenter + visitedpledgehall + visitedgarden + visitedrecreationcenter + visitedresearchcenter

    def HasEgg(eggname = None):
        for item in inventory.keys():
            if (eggname == None):
                if (ItemHasTag(item, "egg hunt")):
                    return True
            else:
                if (eggname == GetItemName(item)):
                    return True

    def NumEggs():
        value = 0
        for item in inventory.keys():
            if (ItemHasTag(item, "egg hunt")):
                value += 1
        return value

$ visitedbaseballfield = False
$ visitedaurahall = False
$ visitedbattlehall = False
$ visitedacademy = False
$ visitedrelichallmorning = False
$ visitedrelichallafternoon = False
$ visitedstudentcenter = False
$ visitedpledgehall = False
$ visitedgarden = False
$ visitedrecreationcenter = False
$ visitedresearchcenter = False

$ hasapologized = False
$ melonyegg = "Smoochum Egg"
$ happinyegg = None

label egghuntoptions:

queue music "Audio/Music/Show Me Around.ogg"

$ HealParty()

scene map

call screen egghunt(_with_none=False) with Dissolve(1.0)
with Dissolve(1.0)

if (_return == "Outside"):
    ethan @talkingmouth "Hey, I don't think the school's going to hide any eggs off school grounds."
    if (timeOfDay in ["Early Morning", "Morning", "Noon"]):
        iris uniform @talkingmouth "Yeah, Daddy said I shouldn't leave the campus."
    else:
        iris @talkingmouth "Yeah, Daddy said I shouldn't leave the campus."

elif (_return == "Baseball Field"):
    if (not visitedbaseballfield):
        $ visitedbaseballfield = True
        show baseball
        show brendan:
            xpos 0.8
        show may:
            xpos 0.6
        show ethan:
            xpos 0.4
        if (timeOfDay in ["Early Morning", "Morning", "Noon"]):
            show iris uniform:
                xpos 0.2
        else:
            show iris:
                xpos 0.2 
        with Dissolve(1.0)

        iris @surprised "Oh! Lookit that! There's a big egg buried in the sand near second base."

        narrator "You notice the egg, whose top is covered in a fluffy white silk-like substance, while the bottom is made of platelike brown ridges."
        narrator "Even from this distance, you can tell a significant amount of heat is emanating from it."

        ethan @surprised "Oh, yeah, you're right!"

        iris @happy "Haha! I recognize that one! It's from my home in Unova! Mr. Alder has one."

        red @closedbrow talking2mouth "Oh, so that must mean..." 

        may @happy "Yep! That's a Larvesta egg! Ever since I saw Alder take out his Volcarona, I knew I wanted one."

        brendan @talking2mouth "It's true. It's all she's been talkin' about. And we've been looking for it for ages."

        may @talkingmouth "Did you know the ancient Unovans used to say that Larvesta fell from the sun?"
        may @angrybrow happymouth "There's actually a really cool theory that, since they make their nests in the bases of volcanoes, the first Larvesta was found when a volcano erupted, sending the eggs flying everywhere!"
        may @happy "If the eggs fell from the sky, surrounded by lava, then it's understandable that an ancient people would think they fell from the sun, wouldn't they?"
        may @talkingmouth "I've been doing a ton of research on them."

        ethan @talkingmouth "Yeah, that's pretty cool."

        may @talkingmouth "So... since I got here first... I get the egg, right?"

        menu:
            "Go ahead.":
                $ ValueChange("May", 1, 0.6, False)
                $ ValueChange("Brendan", 1, 0.8)

                may @happy "Aw, thanks!"
                $ mayhaslarvesta = True

            "Nah, I want it.":
                show brendan surprisedbrow frownmouth
                show may surprisedbrow frownmouth
                show ethan surprisedbrow frownmouth
                show iris surprisedbrow frownmouth
                with dis

                pause 1.0

                $ ValueChange("May", -1, 0.6, False)
                $ ValueChange("Brendan", -1, 0.8)

                may @sad "Hey... that was a joke, right?"

                menu:
                    "Yeah, you can have it.":
                        may @happy "Oh! Ph-phew. You really had me going there, hah hah..."
                        $ mayhaslarvesta = True

                    "No, I'm serious.":
                        show brendan angrybrow frownmouth
                        show may sad
                        show ethan closedbrow frownmouth
                        show iris frownmouth
                        with dis

                        $ ValueChange("May", -2, 0.6, False)
                        $ ValueChange("Brendan", -2, 0.8)

                        may @sad "[first_name], c'mon... I {i}really{/i} like Larvesta, and I don't know if I'll ever get one again..."

                        menu:
                            "Fine, take it.":
                                may @happy "Oh... okay! Wow, you really had me going there for a moment! Haha..."
                                $ mayhaslarvesta = True

                            "I'll battle you for it.":
                                $ wasdick = True
                                show brendan angry
                                show may sad
                                hide ethan
                                hide iris
                                with dis

                                pause 1.0

                                $ ValueChange("May", -3, 0.6, False)
                                $ ValueChange("Brendan", -3, 0.8)

                                may @sad "...Alright."

                                red @talkingmouth "Hey, Ethan, you want to..."
                                red @confused "Wait, where'd he go?"

                                brendan "I'm joining May. You're my friend, dude, but you're being a dick."

                                red @happy "C'mon! It's just a friendly battle between trainers."

                                brendan @closedbrow talking2mouth "Nah, not this time."

                                $ trainer1 = Trainer("red", TrainerType.Player, playerparty, number=2)
                                $ trainer2 = MakeTrainer("May")
                                $ trainer3 = MakeTrainer("Brendan")

                                call Battle([trainer1, trainer2, trainer3], customexpressions=["red", "red angrybrow happymouth", "may sad", "brendan angry", "may sad", "brendan angry"]) from _call_Battle_52
                                $ battlehistory["BrendanMay2"] = _return

                                show brendan angry:
                                    xpos 0.8

                                show may sad:
                                    xpos 0.6

                                if (WonBattle("BrendanMay2")):
                                    $ mayhaslarvesta = False
                                    brendan @talking2mouth "Fine. Take the egg. And get out of here, dude. I know you're not normally like this, but you're being a huge dick."

                                    show may:
                                        xpos 0.6
                                        ease 3.0 ypos 1.1

                                    may "{size=30}I... I really wanted...{/size}"

                                    if (GetRelationship("May") == "Taster"):
                                        may "{size=30}I was {i}really{/i} trying something new. I was standing up for myself. I wasn't scared of change for once. And...{/size}"

                                    show brendan:
                                        ease 0.5 xpos 0.45 xzoom -1.0

                                    pause 0.5

                                    brendan @sad "Hey, babe. It's alright. We'll find another one. Well, maybe not another Larvesta... you know that one Galar Pokémon that's a Fire/Bug-type? We'll find you one of those."

                                    $ GetItem("Larvesta Egg", 1)

                                else:
                                    $ mayhaslarvesta = True
                                    brendan @talking2mouth "There. It's done. Get out of here, dude. I know you're not normally like this, but you're being a huge dick."

                                    red @closedbrow talking2mouth "Damn. Burned some bridges, and didn't even get the bug out of it."
    else:
        if (mayhaslarvesta):
            narrator "There doesn't seem to be much to do there now..."
        else:
            show baseball
            show brendan frownmouth at rightside
            show may frownmouth at leftside
            with Dissolve(1.0)

            brendan @talking2mouth "What, man?"

            menu:
                "I wanted to apologize." if not hasapologized:
                    show may sad
                    show brendan closedbrow 
                    with dis

                    pause 1.0

                    brendan @closedbrow talkingmouth "Yeah, that doesn't really get my girl her Larvesta, does it? Whatever."

                    may @sadbrow happymouth "Thanks for apologizing, at least..."

                    $ ValueChange("Brendan", 1, 0.75, False)
                    $ ValueChange("May", 1, 0.25)
                    $ hasapologized = True

                "I wanted to return the egg." if HasEgg("Larvesta Egg"):
                    show may surprisedbrow frownmouth
                    show brendan surprisedbrow frownmouth 
                    with dis

                    pause 1.0

                    brendan -surprisedbrow -frownmouth -surprised @closedbrow talkingmouth "Damn, you couldn't have done this earlier?"

                    may -surprisedbrow -frownmouth -surprised @happy "Well, I'm not going to look a gift larva in the mouth! Thank you, [first_name]!"

                    $ ValueChange("Brendan", 3, 0.75, False)
                    $ ValueChange("May", 3, 0.25)
                    $ mayhaslarvesta = True
                    $ del inventory[Item.LarvestaEgg]

                "Nothing.":
                    brendan @closedbrow talking2mouth "Fine."

elif (_return == "Aura Hall"):
    if (not visitedaurahall):
        $ visitedaurahall = True
        show lobby
        show calem:
            xpos 0.6
        show misty:
            xpos 0.8
        show ethan:
            xpos 0.4
        if (timeOfDay in ["Early Morning", "Morning", "Noon"]):
            show iris uniform:
                xpos 0.2
        else:
            show iris:
                xpos 0.2 
        with Dissolve(1.0)

        calem @surprised "No, no, I insist! You simply {i}must{/i} take this egg!"

        misty @talkingmouth "And I've told you I don't want it! I can't even train that Pokémon!"
        
        narrator "As you walk into Aura Hall, you see Misty and Calem arguing loudly over a small white egg covered in blue and red triangle outlines."

        narrator "While the egg rests snugly inside a pile of fluffy down pillows, Calem and Misty are both quite agitated."

        iris @surprised "Uh-oh! Big guy fight!"

        ethan @closedbrow talking2mouth "Yeah. Normally Cul-de-sac's the one who calms things down. [first_name], think you can step up?"

        red @confused "No, but I'll try anyway."

        red @happy "Hey, Calem! Hey, Misty! What seems to be the problem?"

        if (GetRelationship("Misty") == "Jerk"):
            misty @talkingmouth "Oh, great, the jerk's come to back up the world's fakest gentleman."

        else:
            misty @angry "How about you mind your own business?!"

        calem @closedbrow talkingmouth "Oh, thank goodness. Another rational mind to help me out here."

        red @confused "I'm not sure anything about this situation is rational. What happened here?"

        calem @talkingmouth "I, and this young lady, were just walking down the hallway, when we saw this egg at the same time."
        calem @happy "I offered it to her. It's only the polite thing to do." 
        calem @sad "But she..."

        misty @talkingmouth "Get it through your bony head, old man! I don't want your damn egg! If I got that thing, I'd just throw it in the PC forever!"

        calem @talkingmouth "And there you have it. I would certainly appreciate the egg myself, but I can't possibly accept it while I might be taking it away from a lady."

        ethan @closedbrow talking2mouth "Oh boy. Talk about overcomplicating the situation. [first_name], I'd just make Calimari take the egg."

        iris @closedbrow talking2mouth "Yeah, I don't think Mr. Calimari is really listening to what Ms. Misty's saying."

        $ trainer1 = Trainer("red", TrainerType.Player, playerparty)
        $ trainer2 = MakeTrainer("Calem")
        $ mistystaryuobj = Pokemon(120, level=12, moves=[GetMove("Water Gun"), GetMove("Harden"), GetMove("Rapid Spin"), GetMove("Recover")], nature=Natures.Sassy, ability="Analytic")
        $ trainer3 = MakeTrainer("Misty")

        menu:
            "Calem, just take the egg.":
                $ ValueChange("Misty", 1, 0.8, False)
                show calem surprisedbrow frownmouth
                show misty happy
                with dis

                pause 1.0

                calem -surprisedbrow -frownmouth -surprised @angry "I... I {i}would{/i} like the egg... but I'm trying to be gentlemanly here! There's no time for self-serving goals!"

                red @closedbrow talking2mouth "...Phew. Well, I tried to resolve this peacefully, but... I guess we'd better just resolve this with a battle?"

                if (GetRelationship("Misty") == "Jerk"):
                    misty "You might be able to talk a big game about dumb feelings and stuff, but I really know how to battle! Just watch me, [first_name]!"
                else:
                    misty "C'mon! Let's show this pompous blowhard what's what!"

                $ trainer3.Type = TrainerType.Ally
                call Battle([trainer1, trainer3, trainer2]) from _call_Battle_53
                $ battlehistory["Calem2"] = _return

                show calem:
                    xpos 0.6
                show misty:
                    xpos 0.8
                with dis

                if (WonBattle("Calem2")):
                    calem @happy "Oh, well done. Brilliantly fought."

                    calem @closedbrow talking2mouth "I must admit, I somewhat appreciate the fact the decision-making power is now out of my hands."

                    if (GetRelationship("May") == "Taster"):
                        redmind @thinking "Yeah, well, just don't let yourself become a May."

                    misty @closedbrow talkingmouth "So, we beat him. What're you doing with the egg?"

                    menu:
                        "Give it to Calem.":
                            jump calemgetegg

                        "I'll keep it.":
                            jump igetegg

                else:
                    misty @angry "Ugh, [first_name], you're useless! Well, I'm not keeping it! I'm {i}leaving!{/i}"

                    show misty:
                        ease 0.5 xpos 1.5

                    pause 0.5

                    calem @surprised "Oh. Well... somehow, I never realized that I could have just walked away from the situation... I suppose that would have simplified things."

                    calem @happy "Ahem. Well, yes, I'll take the egg then, I suppose. Victor's spoils, and all that."

                    $ calemhastogepi = True

                    jump aftertogepibranch

            "Misty, just take the egg.":
                $ ValueChange("Misty", -3, 0.8, False)
                $ ValueChange("Calem", 1, 0.6)

                show calem happy
                show misty surprisedbrow frownmouth
                with dis

                pause 1.0

                $ lowertime = timeOfDay.lower()

                if (lowertime in ["early morning", "noon"]):
                    $ lowertime = "morning"

                misty -surprisedbrow -frownmouth -surprised angry "I didn't care, at first, but after this guy spent all [lowertime] harrassing me, I want to {i}force{/i} him to take the egg now!"

                red @closedbrow talking2mouth "...Phew. Well, I tried to resolve this peacefully, but... I guess we'd better just resolve this with a battle?"

                calem "I'll back you up, my friend!"

                $ trainer2.Type = TrainerType.Ally
                call Battle([trainer1, trainer2, trainer3]) from _call_Battle_54
                $ battlehistory["Misty2"] = _return

                show calem:
                    xpos 0.6
                show misty:
                    xpos 0.8
                with dis

                if (WonBattle("Misty2")):
                    calem @happy "Oh, well done. Brilliantly fought."

                    misty @angry "Seriously?! You're going to force me to take an egg I don't want? Why, do you think you're winning points with me? You're {i}not!{/i} I'm just going to box the thing forever!"

                    menu:
                        "Take the egg.":
                            jump mistygetegg

                        "Fine, Calem can have it.":
                            jump calemgetegg
                            
                        "Nevermind, I'll keep it.":
                            jump igetegg
                            
                else:
                    misty @angry "Hah! Beat you! Calem, take the thing, and never harass me again!"

                    show misty:
                        ease 0.5 xpos 1.5

                    pause 0.5

                    calem @surprised "Oh. Well... somehow, I never realized that I could have just walked away from the situation... I suppose that would have simplified things."

                    calem @happy "Ahem. Well, yes, I'll take the egg then, I suppose. The victor demanded it, after all."

                    $ calemhastogepi = True

                    jump aftertogepibranch

            "I'll take the egg.":
                show calem surprisedbrow frownmouth
                show misty surprisedbrow frownmouth
                with dis

                pause 1.0

                calem -surprisedbrow -frownmouth -surprised angry "Do you mind? I'm trying to be gentlemanly here! There's no time for self-serving goals!"

                $ lowertime = timeOfDay.lower()

                if (lowertime in ["early morning", "noon"]):
                    $ lowertime = "morning"

                misty -surprisedbrow -frownmouth -surprised angry "Yeah! I didn't care, at first, but after this guy spent all [lowertime] harrassing me, I want to {i}force{/i} him to take the egg now!"

                red @closedbrow talking2mouth "...Phew. Well, I tried to resolve this peacefully, but... I guess we'd better just resolve this with a battle?"

                call Battle([trainer1, trainer2, trainer3]) from _call_Battle_55
                $ battlehistory["CalemMisty1"] = _return

                show calem:
                    xpos 0.6
                show misty:
                    xpos 0.8
                with dis

                if (WonBattle("CalemMisty1")):
                    calem @happy "Oh, well done. Brilliantly fought."

                    calem @closedbrow talking2mouth "I must admit, I somewhat appreciate the fact the decision-making power is now out of my hands."

                    if (GetRelationship("May") == "Taster"):
                        redmind @thinking "Yeah, well, just don't let yourself become a May."

                    misty @closedbrow talkingmouth "Ugh. We should've won. Well, fine, what're you doing with the egg?"

                    menu:
                        "Give it to Calem.":
                            jump calemgetegg

                        "Give it to Misty.":
                            $ ValueChange("Misty", -1, 0.8)

                            misty @surprised "You're literally never going to see this again. As soon as I go home, I'm boxing it. You sure?"

                            menu:
                                "Yes.":
                                    jump mistygetegg

                                "Nevermind, Calem can have it.":
                                    jump calemgetegg
                                    
                                "Nevermind, I'll keep it.":
                                    jump igetegg

                        "Like I said, I'll keep it.":
                            jump igetegg
                else:
                    misty @surprised "Huh. I guess we still need to figure out who gets the egg, then..."

                    calem @closedbrow talking2mouth "I noticed your Psyduck seemed a bit... hard-headed during that fight."

                    misty @talkingmouth "Yeah, same thing about your Flabébé."

                    pause 1.0

                    calem @sad "It's difficult, isn't it?"

                    misty @sad "It is."

                    calem @closedbrow talking2mouth "I do the best I can for her, but it's never quite enough. But I still feel awful whenever I let her down."

                    if (GetRelationship("Misty") == "Jerk"):
                        misty @closedbrow talking2mouth "Yeah, and my Psyduck is always acting out for my attention, but I just don't know how to tell him he has it..."
                    else:
                        misty @closedbrow talking2mouth "Yeah, and my Psyduck just never listens to me, for no reason..."

                    red @confused "...Well, did kicking my ass help you guys figure something out?"

                    calem @happy "Maybe so. Perhaps I {i}will{/i} take this egg, if that's alright with you, Misty."

                    misty @happy "Yeah, dummy. That's what I was trying to {i}tell{/i} you."

                    $ calemhastogepi = True

                    jump aftertogepibranch

        label calemgetegg:
            $ calemhastogepi = True
            $ ValueChange("Misty", 1, 0.8, False)
            $ ValueChange("Calem", 3, 0.6)

            calem @closedbrow talking2mouth "...It probably would have been easier to just admit I wanted it all along, wouldn't it have been?"

            red @closedbrow talking2mouth "Yeah, kinda."

            calem @talkingmouth "Well, I thank you for your perceptiveness."

            jump aftertogepibranch

        label igetegg:
            $ GetItem("Togepi Egg", 1)

            jump aftertogepibranch

        label mistygetegg:
            $ wasdick = True
            $ ValueChange("Misty", -2, 0.8)

            misty @angry "You're a jerk {i}and{/i} a simp."

        label aftertogepibranch:

        calem @closedbrow talking2mouth "A thought occurs. Who is that small child that's accompanying you and Ethan?"

        iris @happy "Oh, I'm Iris Blanc! I'm twelve and a half years old, and I'm a really good battler!"

        calem @talkingmouth "Right. And she is...?"

        red @talkingmouth "Not a student, no."

        if (timeOfDay in ["Early Morning", "Morning", "Noon"]):
            red @happy "I see why the uniform would throw you off, though."

        calem @sad "I was asking more about... {i}why{/i} she's here."

        iris @happy "Daddy said I could come to school today to participitate... participitiate... {i}do{/i} the egg hunt!"
        iris @closedbrow talking2mouth "And I like to watch other people battle, too! Grown-ups battle in such a cool way. I wanna be like you when I grow up!"

        calem @happy "Now, isn't that darling. I'm sure you will, young miss Blanc."

    else:
        narrator "There doesn't seem to be much to do there now..."

elif (_return == "Battle Hall"):
    if (not visitedbattlehall):
        $ visitedbattlehall = True
        show stadium_empty
        show bea:
            xpos 0.75 ypos 1.1
        show ethan:
            xpos 0.4
        if (timeOfDay in ["Early Morning", "Morning", "Noon"]):
            show iris uniform:
                xpos 0.2
        else:
            show iris:
                xpos 0.2 
        with Dissolve(1.0)

        narrator "You walk into the arena and see Bea sitting, cross-legged in front of an egg. She is, seemingly, contemplating it."

        narrator "The egg is rugged, pockmarked with firm indentations, and with a purple top and brown bottom."

        red @talkingmouth "...Hey, Bea."

        bea @surprised "Hm?"
        bea @talkingmouth "Oh. Hello. Please, take a seat."

        show ethan:
            xpos 0.4 
            ease 0.5 ypos 1.1

        show iris:
            xpos 0.2
            ease 0.5 ypos 1.1

        show stadium_empty:
            xalign 0.5 yalign 0.5
            ease 1.0 zoom 1.1

        red @talkingmouth "Whatcha doing? Just pondering your egg?"

        bea @talkingmouth "Yes. This is the egg of a Tyrogue. A Pokémon with multiple futures."

        red @happy "Yeah, I'm familiar."
        red @talkingmouth "What'll you evolve it into?"

        bea @closedbrow talkingmouth "I'm not certain."

        pause 1.0

        bea @talkingmouth "Hence my reticence to claim the egg for myself."

        menu:
            "I'll take it off your hands.":
                $ wasdick = True
                $ ValueChange("Bea", -1, 0.75)
                show bea surprisedbrow frownmouth with dis

                pause 1.0

                bea @sad "Well... since I can't make my mind up... yes, I suppose that's fine..."

                $ GetItem("Tyrogue Egg", 1)

            "Let's talk about it.":
                show bea surprisedbrow frownmouth with dis
                $ ValueChange("Bea", 1, 0.75)

                pause 1.0

                bea -surprisedbrow -frownmouth -surprised @talkingmouth "Well... okay."

                iris @talkingmouth "So, whatcha gonna do with it? You want it to take some hits, or do some hits?"

                bea @closedbrow talking2mouth "My team has some issues on the defensive, so I suppose I'd rather it could take hits than deal them..."

                ethan @talkingmouth "Defensive, huh..."

                bea @sad "But my team already has a notable flying weakness. I enlisted in the rock elective to counter that, but an easy counter to that is simply to give Flying-type moves to otherly-typed Pokémon."

                bea @closedbrow talking2mouth "Flying-type moves can be learned most easily by Dragon-types. So perhaps I should seek a Pokémon that can learn fairy moves?" 
                bea @closedbrow talking2mouth "But then a sensible opponent would use a Poison-type, which my Fighting-types would also have difficulty fighting."

                bea @angry "Of course, then I could teach my Pokémon ground-type moves, but that compounds my flying weakness." 
                bea @sad "So then I should teach them psychic moves, but that gives a foe Dark-type the chance for a free switch in, which is--"

                show bea surprisedbrow frownmouth with dis

                iris @shadow angry "Hey! Miss! Stoppit!"

                bea -surprisedbrow -frownmouth -surprised @surprisedbrow talkingmouth "I... sorry?"

                iris @happy "You're tyin' yourself all up in knots! Every Pokémon's got a counter, yeah, but if you try to plan for every strategy, you end up just being a generalist who's great at nothin'!"

                red @talkingmouth "It's true. Look how many champions out there are mono-type specialists. There's nothing wrong with throwing scissors every time, as long as you can do it {i}really{/i} well."

                pause 1.0

                bea @closedbrow talking2mouth "'I fear not the man who has practiced a thousand kicks, but I do fear the man who has practiced one kick a thousand times.'"

                red @happy "Yeah, exactly!"

                if (GetRelationship("Bea") == "Planner"):
                    bea @closedbrow talking2mouth "It seems you have, once again, helped me extricate myself from the gordian knots I weave around myself..."
                    bea @talkingmouth "Thank you, [first_name]."

                iris @closedbrow talking2mouth "Now, you said you wanted a friend that can make your team more defensive, yep?"

                bea @talkingmouth "Yes."

                ethan @closedbrow talking2mouth "So... that'd be Hitmonchan, right? Tyrogue evolves into those guys if their defense is higher than their attack."

                iris @talkingmouth "Not exactly, Mr. Gold! Hitmontop actually has higher defenses than Hitmonchan."
                iris @happy "Plus, their Intimidate ability makes the foe get real scared whenever you switch in, so they can't hit as hard!"

                ethan @talkingmouth "Oh, that's right. And Mr. Alder said that you need a Rapid Spinner on your team, right? Hitmontop can do that, too, so your other 'mons don't take as much damage when they swap in."

                iris @surprised "Woah! You know that too, Mr. Gold? You're real smart!"

                ethan @sadbrow happymouth "Hey, now, I'm being patronized by a six-year-old?"

                iris @angry "I'm not six! I'm twelve and a half!"

                pause 1.0

                iris @closedbrow talking2mouth "What does patronized mean?"

                bea @talkingmouth "'Talking down to.'"

                iris @surprised "Oh, no! I'd never do that! I always mind my manners around grown-ups! Daddy told me to."

                bea @happy "Hah. You remind me of my brother, little lady. What's your name?"

                iris @happy "Oh! I'm Iris. Iris Blanc. And I'm a really good battler!"

                bea @talkingmouth "Bea. Just Bea."

                pause 1.0

                bea @talkingmouth "Well, Iris Blanc, and my teammates, I think I've come to a conclusion. I thank you for your assistance."

                show bea:
                    xpos 0.75 ypos 1.1
                    ease 0.5 ypos 1.0

                show ethan:
                    xpos 0.4 ypos 1.1
                    ease 0.5 ypos 1.0

                show iris:
                    xpos 0.2 ypos 1.1
                    ease 0.5 ypos 1.0

                show stadium_empty:
                    xalign 0.5 yalign 0.5 zoom 1.1
                    ease 1.0 zoom 1.0

                $ ValueChange("Bea", 2, 0.75)

                bea @closedbrow talking2mouth "Still, it would be remiss of me not to offer you a fragment of my appreciation."

                bea @talkingmouth "If you wish to take the egg, you may. I'm certain you'll do as well with it as I might."

                menu:
                    "Take the egg.":
                        $ GetItem("Tyrogue Egg", 1)

                        bea @talkingmouth "Very well."

                    "Leave it for Bea.":
                        $ ValueChange("Bea", 2, 0.75)
                        $ beahastyrogue = True

                        bea @happy "Thank you."

    else:
        narrator "There doesn't seem to be much to do there now..."

elif (_return == "Academy"):
    if (melonyegg != None):
        show classroom
        show icetype
        show iceglow:
            alpha 0.5 xalign 0.5 yalign 1.0
            block:
                ease 2.0 alpha 0.25
                ease 1.8 alpha 0.7
                repeat
        if (not visitedacademy):
            $ visitedacademy = True
            show ethan:
                xpos 0.75
            if (timeOfDay in ["Early Morning", "Morning", "Noon"]):
                show iris uniform:
                    xpos 0.25
            else:
                show iris:
                    xpos 0.25
            with Dissolve(1.0)

            if (timeOfDay not in ["Early Morning", "Morning", "Noon"]):
                iris @sadbrow talking2mouth "Brr! It's chilly in here. I shoulda kept my uniform on."

            red @closedbrow talking2mouth "Hm... Dawn said there was an egg in here, right?"

            ethan @talkingmouth "I mean, what she actually said was 'room there egg has sorry bye sorry!'"

            red @talkingmouth "Yeah, but I'm pretty sure that means there's an egg in here. I just don't see it."

            iris @surprised "Oh! Look there, Mr. [last_name]! It's on the desk!"

            red @talkingmouth "Oh, yeah, you're right."

            show classroom:
                align (0.5, 0.5)
                ease 0.5 zoom 1.6
            show icetype:
                align (0.5, 0.5)
                ease 0.5 zoom 1.6

            show iris:
                ease 0.5 xpos -0.25

            show ethan:
                ease 0.5 xpos 1.25

            pause 1.0

            red @closedbrow talking2mouth "Hm. What's this...?"

            narrator "Approaching the desk at the front of the classroom, you see an egg wrapped up in a fluffy wool blanket. The egg is a bright pink, with wispy yellow tufts on its top." 
            
            show ethan surprisedbrow frownmouth
            show iris surprisedbrow frownmouth
            with dis

            narrator "However, of more immediate concern than the egg is what sounds like a quiet sobbing."

            if (HasEvent("Instructor Melony", 1)):
                narrator "Due to your experience in your Ice-type elective, you are easily able to recognize this as Instructor Melony."

            red @closedbrow talking2mouth "Oh boy. This'll be a thing, won't it?"

            red @sadbrow happymouth "Hey... is something wrong?"

            pause 1.0

            show melony sadbrow tears frownmouth with dis

            show ethan -surprisedbrow -frownmouth
            show iris -surprisedbrow -frownmouth
            with dis

            melony @sadmouth "Oh! It's awful, just awful... I know I have to leave the eggs out for my students. That's my job as a teacher... but if you take the egg, then I'll be left all alone... again..."

            red @closedbrow talking2mouth "Ah, geez. Hey, isn't it a bit too cold in here for eggs, anyway?"

            ethan @talkingmouth "Professor Elm said that eggs can endure pretty much anything for twenty-four hours. It should be fine for a while."

            iris @happy "Yup, it's true! Besides, that's a Smoochum egg. They're Ice-types."

            red @talkingmouth "Well... I guess since the egg's wrapped up in that blanket, it's fine, but..."

            if (HasEvent("Instructor Melony", 1)):
                redmind @thinking "I'd feel a bit bad just taking the egg from Instructor Melony."
            else:
                redmind @thinking "I'd feel a bit bad just taking the egg from this woman."

                if not HasEgg():
                    redmind @thinking "Maybe if I come back later with another egg, I can swap it out...?"

        label eggswap:

        menu:
            ">Swap the egg out for one of your own." if HasEgg():
                menu:
                    ">Swap in the Larvesta egg." if HasEgg("Larvesta Egg"):
                        $ GetItem(melonyegg, 1)
                        $ melonyegg = "Larvesta Egg"
                        $ del inventory[Item.LarvestaEgg]

                        red @happy "Here, Ma'am! I'm leaving behind this Larvesta egg. It's pretty warm, so maybe it'll warm up this classroom?"

                    ">Swap in the white egg with red and blue triangles." if HasEgg("Togepi Egg"):
                        $ GetItem(melonyegg, 1)
                        $ melonyegg = "Togepi Egg"
                        $ del inventory[Item.TogepiEgg]

                        red @happy "Here, Ma'am! I'm leaving behind this egg. It's kinda cute, and looks really nice all wrapped up in this blanket."

                    ">Swap in the Tyrogue egg." if HasEgg("Tyrogue Egg"):
                        $ GetItem(melonyegg, 1)
                        $ melonyegg = "Tyrogue Egg"
                        $ del inventory[Item.TyrogueEgg]

                        red @happy "Here, Ma'am! I'm leaving behind this Tyrogue egg. It's kinda rugged, so I bet you could give it tight hugs without hurting it."

                    ">Swap in the Smoochum egg." if HasEgg("Smoochum Egg"):
                        $ GetItem(melonyegg, 1)
                        $ melonyegg = "Smoochum Egg"
                        $ del inventory[Item.SmoochumEgg]

                        red @happy "Here, Ma'am! I'm bringing back the Smoochum egg you had originally."

                    ">Swap in the red, warm, lumpy egg." if HasEgg("Magby Egg"):
                        $ GetItem(melonyegg, 1)
                        $ melonyegg = "Magby Egg"
                        $ del inventory[Item.MagbyEgg]
                        
                        red @happy "Here, Ma'am! I'm leaving behind this warm, lumpy egg. It's pretty warm, so maybe it'll warm up this classroom?"

                    ">Swap in the rubbery blue egg." if HasEgg("Wynaut Egg"):
                        $ GetItem(melonyegg, 1)
                        $ melonyegg = "Wynaut Egg"
                        $ del inventory[Item.WynautEgg]

                        red @happy "Here, Ma'am! I'm leaving behind this rubbery, blue egg. If you want an egg to stay with, why not this one?"

                    ">Swap in the heavy, brown egg." if HasEgg("Bonsly Egg"):
                        $ GetItem(melonyegg, 1)
                        $ melonyegg = "Bonsly Egg"
                        $ del inventory[Item.BonslyEgg]

                        red @happy "Here, Ma'am. I'm leaving behind this heavy, brown egg. It seems really sturdy--but it's not actually a log!"

                    ">Swap in the blue egg with the markings." if HasEgg("Mantyke Egg"):
                        $ GetItem(melonyegg, 1)
                        $ melonyegg = "Mantyke Egg"
                        $ del inventory[Item.MantykeEgg]

                        red @happy "Here, Ma'am. I'm leaving behind this blue egg. It's got some interesting markings on it that look kinda like a happy face. Maybe it'll cheer you up?"

                    ">Swap in the purple, humming egg." if HasEgg("Toxel Egg"):
                        $ GetItem(melonyegg, 1)
                        $ melonyegg = "Toxel Egg"
                        $ del inventory[Item.ToxelEgg]

                        red @happy "Here, Ma'am. I'm leaving behind this purple, humming egg. It's got some nasty static electricity, so make sure you're grounded when you touch it."

                    "Nevermind.":
                        jump eggswap

            ">Take the egg":
                $ wasdick = True
                $ GetItem(melonyegg, 1)
                $ melonyegg = None
                red @talking2mouth "Uh, I'm going to take this egg."

                show melony closedbrow cry frownmouth with dis

                melony closedbrow cry @sadmouth "Oh nooooo..."

                redmind @thinking "Sorry, Ma'am."

            ">Just leave":
                pass
    else:
        narrator "There doesn't seem to be much to do there now..."

elif (_return == "Relic Hall"):
    if ((not visitedrelichallmorning and timeOfDay in ["Early Morning", "Morning", "Noon"]) or (not visitedrelichallafternoon and timeOfDay not in ["Early Morning", "Morning", "Noon"] and not magbytaken)):
        $ visitedrelichall = True
        show library
        if (timeOfDay in ["Early Morning", "Morning", "Noon"]):
            show flannery angry:
                xpos 0.75
                block:
                    ease 0.1 ypos 0.9
                    ease 0.1 ypos 1.0
                    pause 1.5
                    repeat
        else:
            show flannery:
                xpos 0.75
                block:
                    ease 0.1 ypos 0.9
                    ease 0.1 ypos 1.0
                    pause 1.5
                    repeat
        show ethan:
            xpos 0.4
        if (timeOfDay in ["Early Morning", "Morning", "Noon"]):
            show iris uniform:
                xpos 0.2
        else:
            show iris:
                xpos 0.2 
        with Dissolve(1.0)

        narrator "You walk into the lobby and see Flannery is staring at an egg that's just a tiny bit out of reach on top of a bookshelf." 
        narrator "She is repeatedly jumping up, attempting to grab it. It's amusing to see the quite-tall Flannery face such a vertical challenge."

        narrator "The egg is red, and covered in lumps. It gives off a palpable heat, even from this distance."

        if (timeOfDay in ["Early Morning", "Morning", "Noon"]):
            $ visitedrelichallmorning = True
            flannery "Gah! I can't reach the... damn egg, it's just..."

            show ethan surprisedbrow frownmouth
            show iris surprisedbrow frownmouth
            with dis

            show library with vpunch

            show flannery:
                ease 0.1 xpos 0.75 ypos 1.0

            flannery @furious "GAAAAAAH!"

            redmind @surprised "Okay... I'm getting a powerful, furious aura from Flannery here. I should probably tread carefully..."

            if (GetRelationship("Flannery") == "Challenger"):
                redmind @thinking "I've been doing a bit of research on her 'condition' ever since we had our talk, and from what I know of Flannery, [bluecolor]I should probably just leave and come back later.{/color}"

            show ethan -surprisedbrow frownmouth
            show iris -surprisedbrow frownmouth
            with dis

            menu:
                ">Try to grab the egg":
                    flannery @surprised "Huh?! You trying to take the egg?!"

                    red @talkingmouth "Uh, yeah. Do you mind?"

                    flannery @furious "Hell yeah, I do! That egg is mine, and I'm getting it as soon as I get a stool, or a long stick or something!"

                    red @confused "Careful you don't knock it over, or anything, though..."

                    flannery @furious "I come from Lavaridge! We basically turned hatching eggs into a science! I know what I'm doing!"

                    red @talkingmouth "Okay, but I kinda want the egg myself, so--"

                ">Offer your help to Flannery":
                    flannery @surprised "Huh?! You trying to take the egg?!"

                    red @talkingmouth "Uh, no. Just going to help you. You look a bit unsteady on your feet. Just making sure you don't knock it over or something."

                    flannery @furious "I come from Lavaridge! We basically turned hatching eggs into a science! I know what I'm doing!"

                    red @talking2mouth "Okay, but if you keep rocking the bookshelf like that, then--"

                ">Just leave":
                    red @closedbrow talking2mouth "Yep, Flannery does {i}not{/i} appreciate charity in the mornings. I should come back later."
                    jump postrelichall
        else:
            $ visitedrelichallafternoon = True
            show flannery surprisedbrow frownmouth with dis:
                ease 0.1 xpos 0.75 ypos 1.0

            flannery -surprisedbrow -frownmouth -surprised @happy "Oh, hey, [first_name]! Good to see you. I've been trying to get this darn egg off the bookshelf for ages now."
            flannery @sadbrow sweat happymouth "Guess I'm just a couple inches too short, heh."

            iris @surprised "No way, miss! You're really tall!"

            flannery @happy "Hah, well, maybe compared to you, squirt."

            iris @talkingmouth "Daddy says I'm in the top percentage of my height group! That means I'm taller than my classmates!"

            flannery @talking2mouth "Cool. Hey, kiddo. Want to ride on my shoulders? I bet if you do, we can get that darn egg!"

            iris @surprised "Can I?"

            pause 1.0

            red @talkingmouth "Ethan, she's asking you."

            ethan @surprised "H-huh? Me? What're you asking me for? I mean, [first_name]'s right there."

            iris @talking2mouth "Yeah, but I don't want you to feel left out. Daddy says I should give everyone in my company equal attention."

            ethan @sadbrow happymouth "...Geez, you're a cute kid."

            iris @happy "Hehe! Thanks!"

            ethan @talkingmouth "Anyway, I'm not your Daddy, but, sure, go ahead. Climb that mountain."

            pause 1.0

            flannery @tired "Did you just call me a mountain?"

            ethan @happy "Yep! I mean, I had to do something to ruin this cute moment, didn't I? Me and my big mouth."

            show iris:
                ease 0.5 xpos 0.75

            pause 0.2

            show blank2 with dis

            narrator "Flannery lifts Iris up on her shoulders, and Iris deftly grabs the egg from the top of the bookshelves, though she yelps a little at the heat."

            show iris:
                xpos 0.2

            hide blank2 with dis

            iris @angry "That egg's hot! It burned my fingers..."

            ethan @closedbrow talking2mouth "Oh? Uh, hold on, I think I've got some cream in my bag."

            red @closedbrow talking2mouth "Hey, I always wondered. What's in that bag you carry around all over?"

            ethan @happy "Ah, just emergency stuff. First aid kit, spare phone, batteries. You know, stuff like that."

            flannery @talking2mouth "Well, thanks for helping me get the egg, li'l miss."

            show iris:
                xpos 0.2
                ease 0.5 ypos 1.1
                pause 1.0
                ease 0.5 ypos 1.0

            iris @happy "It was my pleasure, big Miss!"

            flannery @talking2mouth "Hey, since you burned your fingers getting it, do you want it?"

            ethan @surprised "Woah, isn't Iris a bit young for that? I mean, she keeps saying she's a really good battler, but you can't be a trainer yet, can you?"

            iris @happy "Yeah! I got my Trainer's License in Driftveil! Daddy says they're a 'national embarrassment'!"

            iris @talkingmouth "But... I don't think I have room on my team for that kind of Pokémon. Why don't you take it, [first_name]?"

            menu:
                "Give it to Flannery.":
                    show flannery happy with dis

                    $ AddEvent("Flannery", "HasMagby")

                    $ ValueChange("Flannery", 3, 0.75)

                    flannery "Score! Thanks!"

                "Take it.":
                    $ GetItem("Magby Egg")

                    red @talkingmouth "Sure. Thanks for the assist, Flannery."

                    if (GetRelationship("Flannery") == "Challenger"):
                        flannery @talking2mouth "Anything for my challenger! Use that li'l guy to figure out why I can't handle mornings!"

                        pause 1.0

                        red @confused "How?"

                        flannery @tiredbrow talking2mouth "I dunno, that's your job."

                    else:
                        flannery "No probs!"

            jump wraparoundegghunt

        label flannerybattle:
        $ ValueChange("Flannery", -1, 0.75)

        flannery furious "BATTLE ME!"

        red @surprised "What?! In the library?! Hold on, I--"

        $ trainer1 = Trainer("red", TrainerType.Player, playerparty)
        $ flannerydarumakaobj = Pokemon(pokedexlookupname("Darumaka", DexMacros.Id), level=11, moves=[GetMove("Fire Fang"), GetMove("Rage"), GetMove("Rollout")], gender=Genders.Female, ability="Inner Focus")

        $ trainer2 = MakeTrainer("Flannery")

        call Battle([trainer1, trainer2]) from _call_Battle_56
        $ battlehistory["Flannery1"] = _return

        show flannery frownmouth with dis:
            xpos 0.75

        if (WonBattle("Flannery1")):
            flannery @talking2mouth "Hah... Hah... Hah..."

            red @closedbrow talking2mouth "Hm... she's still kinda angry, but... maybe she's tired enough now that I can grab the egg without her physically tackling me."

            show flannery surprisedbrow frownmouth with dis

            red @happy "'Scuse me!"

            show library:
                align (0.5, 0.5) zoom 1.0
                ease 0.5 align (0.75, 0.75) zoom 1.5

            $ ValueChange("Flannery", -2, 0.75)

            pause 1.0

            show library:
                align (0.75, 0.75) zoom 1.5
                ease 0.5 align (0.5, 0.5) zoom 1.0

            flannery furious "Hey!"

            menu:
                ">Keep the egg":
                    $ magbytaken = True
                    $ wasdick = True
                    $ GetItem("Magby Egg", 1)

                    red @happy "Hay's for horses. Seeya!"

                ">Give her the egg":
                    $ magbytaken = True
                    $ AddEvent("Flannery", "HasMagby")

                    red @happy "Here you go."

                    flannery -furious frownmouth @surprised "Huh?!"

                    red @talkingmouth "You looked like you were having some trouble. So, here you go."

                    pause 1.0

                    show flannery tired with dis

                    $ ValueChange("Flannery", 3, 0.75)

                    flannery @tiredbrow talking2mouth "...Yeah, okay."

        else:
            $ AddEvent("Flannery", "HasMagby")
            $ visitedrelichallmorning = True
            $ visitedrelichallafternoon = True

            flannery @angry "GET OUT!"

            redmind @thinking "Well, that was a bust..."

    else:
        narrator "There doesn't seem to be much to do there now..."

    label postrelichall:

elif (_return == "Student Center"):
    if (not visitedstudentcenter):
        $ visitedstudentcenter = True
        show clouds
        show garden:
            zoom 0.625
        show bianca:
            xpos 0.8
        show tia hat:
            xpos 0.6
        show ethan:
            xpos 0.4
        if (timeOfDay in ["Early Morning", "Morning", "Noon"]):
            show iris uniform:
                xpos 0.2
        else:
            show iris:
                xpos 0.2 
        with Dissolve(1.0)

        narrator "As you walk to the student center, Bianca and Tia abruptly walk out of it, nearly colliding into you."

        red @happy "Oh, hey!"

        bianca @happy "Oh, hiya red-hat!"

        if (GetRelationship("Tia") != "Protector"):
            tia @happy "Hi, [first_name]!"

        red @talkingmouth "Hey, Biancas."

        pause 1.0

        red @closedbrow talking2mouth "Huh, something just occurred to me. Ethan, you know these two have the same name, right?"

        ethan @surprised "Huh? Yeah."

        red @closedbrow talking2mouth "So, who are they?"

        ethan @closedbrow talking2mouth "Uh... blonde is Bel and brunette is Ven?"

        pause 1.0

        red @confused "It's amazing how close you are, yet still incredibly off. We {i}just{/i} established they have the same name, didn't we? Iris, back me up here."

        iris @happy "Yep! You did, Mr. [last_name]!"

        bianca @happy "You totally did!"
        
        if (GetRelationship("Tia") != "Protector"):
            tia @happy "Yeah, you did!"

        ethan @sadbrow talkingmouth "What can I say? Bad with names."

        red @talkingmouth "Well, how are you two doing? Find any good eggs?"

        show tia happy with dis:
            xpos 0.6
            ease 0.2 ypos 1.1
            ease 0.2 ypos 1.0
            repeat

        show bianca with dis:
            xpos 0.8
            ease 0.2 ypos 1.1
            ease 0.2 ypos 1.0
            repeat

        bianca @talkingmouth "Well, that's the thing! We were walking into the Student Center together and we saw this egg at the same time and we both kinda want it, but we can't figure out who should have it so we were trying to decide--"
        
        if (GetRelationship("Tia") != "Protector"):
            show tia:
                xpos 0.6
                ease 0.2 ypos 1.0

            show bianca with dis:
                xpos 0.8
                ease 0.2 ypos 1.0

            red @surprised "Who-whoa! Please, one at a time!"

            bianca @surprised "One at a time? But I was the only one talking."

            red @happy "Yeah, but Tia was signing, and I've actually learned enough JSL that it's a bit distracting."

            bianca @happy "Oh, but that reminds me of the point of this story!"

            show tia happy with dis:
                xpos 0.6
                ease 0.2 ypos 1.1
                ease 0.2 ypos 1.0
                repeat

            show bianca with dis:
                xpos 0.8
                ease 0.2 ypos 1.1
                ease 0.2 ypos 1.0
                repeat
        
        bianca @talkingmouth "And basically because we can't talk, I have no idea how we decide who gets the egg! Do you want it?"

        show tia happy with dis:
            xpos 0.6
            ease 0.2 ypos 1.0

        show bianca with dis:
            xpos 0.8
            ease 0.2 ypos 1.0

        red @talkingmouth "Yeah... I'm definitely not fluent enough to translate yet. Sorry."
        red @confused "Hey, uh, Ethan, Iris? Either of you guys know JSL?"

        ethan @talkingmouth "Professor Cherry does, but I never learned a bit of it. Pass, man."

        iris @talkingmouth "I'm only twelve and a half! How'm I supposed to learn something like that? You gotta be a grown-up to do that!"

        show ethan surprisedbrow frownmouth with dis

        bianca @talkingmouth "Actually, a child is much better at learning languages than grown-ups! Your neural plasticity is super-adaptable before you get older!"

        pause 1.0

        ethan @talkingmouth "How do you know that?"

        bianca @talkingmouth "Oh, I've done a bunch of research on dreams. A friend of mine is a leading scientist in the field, so I've studied all kinds of brain stuff."

        red @confused "Huh, is that why you have a Munna?"

        bianca @happy "Yeah! My Moony was a gift."

        red @happy "Cool. About the egg, though..."

        narrator "You look at the egg Bianca's holding. It's blue, and it has a rubbery texture. You feel like, if you dropped it, it would almost certainly bounce back... not that you'd risk that, of course."

        red @closedbrow talking2mouth "Well, I guess someone's gotta make a call."

        menu:
            "Good luck figuring that out.":
                if (Random() < 0.5):
                    $ biancahaswynaut = True
                else:
                    $ AddEvent("Tia", "HasWynaut")

                bianca @happy "Thanks! We'll do our best."

            "Bianca should take it.":
                $ biancahaswynaut = True
                show bianca happy with dis

                $ ValueChange("Bianca", 3, 0.8)
                
                show bianca happy with dis:
                    xpos 0.8
                    ease 0.2 ypos 1.1
                    ease 0.2 ypos 1.0
                    ease 0.2 ypos 1.1
                    ease 0.2 ypos 1.0

                bianca "Yay!"

                red @happy "Glad I could sort that out for ya."

            "Shorter Bianca should take it.":
                $ AddEvent("Tia", "HasWynaut")
                show tia happy with dis

                $ ValueChange("Tia", 3, 0.6)

                if (GetRelationship("Tia") != "Protector"):
                    tia "Yay!"
                
                show tia happy with dis:
                    xpos 0.6
                    ease 0.2 ypos 1.1
                    ease 0.2 ypos 1.0
                    ease 0.2 ypos 1.1
                    ease 0.2 ypos 1.0

                red @happy "Glad I could sort that out for ya."

            "I'll take it.":
                show tia happy with dis
                
                if (GetRelationship("Tia") != "Protector"):
                    tia "That's a great idea! You're an awesome {font=fonts/sign.ttf}Trainer{/font}, so I bet you'll take good care of it!"

                bianca @surprised "...Oh, that makes things simple!" 
                
                bianca @happy "Alright, here you go!"

                $ GetItem("Wynaut Egg", 1)
    else:
        narrator "There doesn't seem to be much to do there now..."

elif (_return == "Pledge Hall"):
    if (not visitedpledgehall):
        $ visitedpledgehall = True
        show relichall_A
        show nessa frownmouth:
            xpos 0.8
        show hilda frownmouth:
            xpos 0.6 xzoom -1
        show ethan:
            xpos 0.4
        if (timeOfDay in ["Early Morning", "Morning", "Noon"]):
            show iris uniform:
                xpos 0.2
        else:
            show iris:
                xpos 0.2 
        with Dissolve(1.0)

        show iris surprisedbrow frownmouth
        show ethan surprisedbrow frownmouth
        with dis

        hilda @angry "...Do you know how hard I work my ass off to study for my Rock elective? Gimme a goddamn break!"

        nessa @talkingmouth "Green's not a good color on you. And explain why I should care you're overworking yourself? Seems like a you problem."

        show nessa surprisedbrow frownmouth 
        show hilda surprisedbrow frownmouth
        with dis

        red @surprised "W-woah, hey! Little ears! Little ears, here!"

        nessa -surprisedbrow -frownmouth -surprised frownmouth @surprised "[first_name]? What're you doing here? ...Who's the kid?"

        hilda -surprisedbrow -frownmouth -surprised frownmouth @angrymouth "Look, I'm just telling 'Nessa' here where she can {i}shove{/i}--"

        ethan @sadbrow happymouth "Uh... I'll just take Iris somewhere else."

        iris sad "What? No! I wanna hear the grown-up words!"

        show ethan:
            ease 0.5 xpos -0.2

        show iris:
            ease 0.5 xpos -0.2

        show hilda:
            ease 0.5 xpos 0.25

        show nessa:
            ease 0.5 xpos 0.75

        narrator "You notice that, evenly spaced between the two trainers, there's an egg. It's large, brown, looks heavy, and strongly resembles a log."

        red @talking2mouth "So, you're arguing over... that egg?"

        hilda @talkingmouth "Yeah. It's a Rock-type, and I want that for my team."

        nessa @talkingmouth "...And I want that for {i}my{/i} team."

        hilda @angry "And she expects, because she's a model and gorgeous, that I'm just going to roll over and let her take the egg!"

        nessa @surprised "You know who I am?"

        hilda @sad "Yeah. I've seen you in a {i}lot{/i} of Hilbert's 'magazines.'"
        hilda @angrybrow talkingmouth "But sorry, honey, you can't just three-quarters pose your way out of this one. I'm taking the egg."

        nessa @angrybrow talkingmouth "Do you know how little I actually care about things? Anything? I care about {i}this.{/i} Why, now, of all times, are you getting in my way?"

        hilda @surprised "Getting in your way?! This has {i}nothing{/i} to do with you! You're so self-centered--I'm just picking up a goddamn egg because my team needs a 'mon that can use utility moves!"

        nessa @angry "No, you're just doing this out of spite, now. You're high-strung and jealous, because you overworked yourself. I've got no sympathy for people like you."

        hilda @surprised "P-people like {i}me?!{/i} What the hell's that supposed to mean? People who had to work a day in their life?"

        nessa @surprised "You think my job isn't work, sister? I dare you to go down to any agency and try to pull off what I did. You wouldn't make it twelve hours without ending up on the casting couch."

        hilda angry "You {i}bitch!{/i}"

        nessa angry "Screw you!"

        redmind @surprised "{w=0.5}.{w=0.5}.{w=0.5}."
        redmind @thinking "Oh, man..."
        
        $ trainer1 = Trainer("red", TrainerType.Player, playerparty)
        $ trainer2 = MakeTrainer("Hilda")
        
        menu:
            ">Side with Nessa":
                show nessa happy
                show hilda angry
                with dis

                $ ValueChange("Hilda", -3, 0.25, False)
                $ ValueChange("Nessa", 3, 0.75)

                if (GetRelationship("Nessa") == "Friend"):
                    nessa @talkingmouth "It's nice having a reliable friend who has my back. Reminds me of before."
                else:
                    nessa @talkingmouth "See? Even [first_name] gets it. You lost all claim to the egg when you started the personal attacks."

                hilda @angrymouth "Oh, so you think, just because it's two on one, that I'm going to lay down and let you take the egg?"
                hilda @closedbrow talkingmouth "Sorry, sister, but you can't have {i}everything{/i} you want." 
                hilda @angrybrow talkingmouth "And [first_name], I'm disappointed in you. I thought you had better taste, frankly."

                red @confused "Um. This isn't about taste."

                hilda @closedbrow smirkmouth "Sure it isn't."

                nessa @talkingmouth "Let's just battle. Winner decides who gets the egg."

                hilda @angry "I was going to say that!"

                $ trainer3 = Trainer("nessa", TrainerType.Ally, [GetTrainerTeam("Nessa", "Corsola")])
                call Battle([trainer1, trainer3, trainer2], customexpressions=["red", "red angrybrow happymouth", "nessa", "nessa angrybrow happymouth", "hilda angry", "hilda angry"]) from _call_Battle_57
                $ battlehistory["Hilda2"] = _return

                show nessa frownmouth at rightside
                show hilda frownmouth at leftside
                with dis

                if (WonBattle("Hilda2")):
                    hilda @angry "Fine! {i}Fine!{/i} You win! Great job! Dumb of me to think that I could have something go my way for once. Won't make {i}that{/i} mistake again!"

                    hide hilda with dis

                    nessa @happy "Nice job, [first_name]. I didn't even have to get serious."

                    pause 1.0

                    nessa "{w=0.5}.{w=0.5}.{w=0.5}."
                    nessa @sad "I probably went a bit overboard. I just..."
                    nessa @closedbrow angrymouth "I can't {i}stand{/i} people who get themselves so caught up in their own problems. Just {i}deal with them{/i} in a way that doesn't spill over onto other people."
                    nessa @sad "But... yeah. I lost sight of the end goal there. This egg doesn't mean much in the long run. Want it?"

                    menu:
                        ">Take the egg":
                            $ GetItem("Bonsly Egg", 1)

                            nessa @closedbrow talkingmouth "Take care of it."
                            nessa @talkingmouth "Hope I see it fully-evolved some day."

                        ">Insist Nessa take the egg":
                            $ ValueChange("Nessa", 3, 0.75)
                            $ AddEvent("Nessa", "HasBonsly")

                            nessa @happy "Hm. You still trust me to take it?"

                            red @happy "Sure."

                            if (GetRelationship("Nessa") == "Friend"):
                                red @talkingmouth "Maybe you did something you regret, a little bit. But you've got plenty of time to make it right, right? You'll focus on the big picture."

                                nessa @closedbrow talkingmouth "...Thanks."

                            else:
                                nessa @closedbrow talkingmouth "I bet you're just trying not to jeopardize our date... But whatever. Your reasons are your own. Thanks."

                        ">Suggest giving the egg to Hilda":
                            $ AddEvent("Hilda", "HasBonsly")
                            pause 1.0

                            nessa @closedbrow talkingmouth "Might as well. Don't want to burn that bridge. Not yet, anyway."
                            nessa @sad "...God, I don't like rolling back anything I say, though. You can't move forward when you're changing the past."

                            red @happy "I'll handle it."

                            nessa @surprised "You will?"

                            red @talkingmouth "Yeah, no problem."

                            if (GetRelationship("Nessa") == "Friend"):
                                nessa @closedbrow talkingmouth "I guess you're trying not to jeopardize that second date, huh?"
                                nessa @talkingmouth "You don't need to do that. But thank you, anyway."

                            else:
                                nessa @talkingmouth "Thanks. Date's still on, then."

                                red @confused "Hm?"

                                nessa @happy "Joke."
                            
                            hide nessa with dis

                            pause 1.0

                            show hilda with dis

                            hilda @surprised "Hm? What is it?"

                            red @talkingmouth "Two things. First, I just wanted to check in on you."

                            hilda @sad "Ugh, yeah. I'm fine. Shit, I don't know." 
                            hilda @closedbrow talking2mouth "I guess I got a bit worked up there... It just felt... I mean, here's this wealthy, gorgeous, popular girl who's making a big deal about how she wanted the egg {i}I{/i} wanted."
                            hilda @closedbrow talkingmouth "I just... saw red, I guess."                

                            pause 1.0

                            hilda @talkingmouth "You said you had two things?"

                            red @talkingmouth "Yeah. Here."

                            show hilda surprisedbrow frownmouth with dis:
                                ease 0.5 zoom 0.9 ypos 0.9

                            hilda "The egg?"

                            red @talkingmouth "Yeah. Nessa felt badly about, uh, demanding the egg. So here, a peace offering."

                            hilda -surprisedbrow -frownmouth -surprised @closedbrow talking2mouth "Hmph. Maybe I misjudged her. Still don't like her, though."

                            hilda @smirkmouth "Thanks, though. Means a lot that you'd do that for me. I'll even forgive you for kicking my team's shit in."

                            red @closedbrow talking2mouth "Uh... yeah, sorry about that."

                            red @surprised "Actually, that reminds me. Where was the rest of your team when we battled in gym class?"

                            hilda @talkingmouth "Ugh, I hadn't asked for them to be sent from home yet."
                            hilda @sad "I had to do it for Hilbert first, and the shipping company can only do so many Poké Balls in a single shipment. You know, in case something goes wrong."
                            hilda @closedbrow sadmouth "So then I had to wait three to five business days for their next shipment, and then the weekend came around, and that was a huge hassle, so... yeah."

                            hilda @happy "Gotta say, it was goddamn embarrassing to be using one Pokémon on the first day of the double battle unit. Sucks to suck, I guess."
                            
                            if (GetRelationship("Hilda") == "Caretaker"):
                                hilda @happymouth "At least I was battling you. If I'd been battling anyone else, it probably would've been worse."

                            hilda @sad "Anyway..."

                            $ ValueChange("Hilda", 3, 0.5)

                            hilda @happybrow smirkmouth "Thanks for the egg!"

                else:
                    $ AddEvent("Hilda", "HasBonsly")
                    hilda @happy "Nice. Training paid off! Don't hold it against me, right?"

                    nessa @angrybrow talkingmouth "I'll forget you even exist by tomorrow morning."

                    hide nessa
                    hide hilda
                    with dis

                    pause 1.0

                    red @closedbrow talking2mouth "Well, that was an awful time for everyone."

            ">Side with Hilda":
                show hilda happy
                show nessa angry
                with dis

                $ ValueChange("Hilda", 3, 0.25, False)
                $ ValueChange("Nessa", -3, 0.75)

                if (GetRelationship("Hilda") == "Caretaker"):
                    hilda "See, this is the kind of shit I don't mind if you do for me! Thanks, [first_name]! Glad {i}someone's{/i} got my back!"

                else:
                    hilda "Uh, yeah, obviously."

                nessa @talkingmouth "That's fine. You know what? I don't even care. Let's just battle. Winner decides who gets the egg."

                nessa @angry "Oh, by the way, [first_name]? {i}This time{/i}, I'm battling seriously."

                $ trainer2.Type = TrainerType.Ally
                $ trainer3 = Trainer("nessa", TrainerType.Enemy, [GetTrainerTeam("Nessa", "Drednaw")])
                call Battle([trainer1, trainer2, trainer3], customexpressions=["red", "red angrybrow happymouth", "hilda", "hilda angrybrow happymouth", "nessa angry", "nessa angry"]) from _call_Battle_58
                $ battlehistory["Nessa2"] = _return

                show nessa frownmouth at rightside
                show hilda frownmouth at leftside
                with dis

                if (WonBattle("Nessa2")):
                    nessa @closedbrow angrymouth "...Whatever. Fine, take the egg. In the long run, it doesn't matter."

                    hide nessa with dis

                    hilda @happy "Hah! We beat her, {i}and{/i} her ridiculous Drednaw!"

                    red @closedbrow talking2mouth "Yeah, that was a close one."

                    hilda "{w=0.5}.{w=0.5}.{w=0.5}."
                    hilda @sad "I guess I got a bit worked up there... It just felt... I mean, here's this wealthy, gorgeous, popular girl who's making a big deal about how she wanted the egg {i}I{/i} wanted."
                    hilda @closedbrow talkingmouth "I just... saw red, I guess."
                    hilda @sad "Gah. I made an ass of myself. Thanks for backing me up, at least, but now I'm not sure if I should even have that egg... you want it?"

                    menu:
                        ">Take the egg":
                            $ GetItem("Bonsly Egg", 1)

                            hilda @closedbrow talkingmouth "Take care of it."
                            hilda @smirkmouth "Don't get in any fights over it."

                        ">Insist Hilda take the egg":
                            $ ValueChange("Hilda", 3, 0.25)
                            $ AddEvent("Hilda", "HasBonsly")

                            hilda @happy "Aw, even after that, you think I should have it? Thanks, [first_name]."

                            if (GetRelationship("Hilda") == "Caretaker"):
                                hilda @closedbrow talking2mouth "I guess this is just another way you're doing stuff for me."
                                hilda @talkingmouth "Which I don't hate. Just... be careful. Don't overdo it."

                                red @confused "{i}You're{/i} telling {i}me{/i} not to over do it?"

                        ">Suggest giving the egg to Nessa":
                            $ AddEvent("Nessa", "HasBonsly")
                            pause 1.0

                            hilda @closedbrow talkingmouth "Yeah, fine. I guess. Go ahead."
                            hilda @sad "It's probably the mature thing to do... but, shit, I hate that."

                            red @happy "I'll handle it."

                            hilda @surprised "You will?"

                            red @talkingmouth "Yeah, no problem."

                            if (GetRelationship("Hilda") == "Caretaker"):
                                hilda @closedbrow talking2mouth "I guess this is just another way you're doing stuff for me."
                                hilda @talkingmouth "Which I don't hate. Just... be careful. Don't overdo it."

                                red @confused "You're telling {i}me{/i} not to over do it?"

                            else:
                                hilda @talkingmouth "Thanks."
                            
                            hide hilda with dis

                            pause 1.0

                            show nessa with dis

                            nessa @surprised "Hm? What is it?"

                            red @talkingmouth "Two things. First, that was an awesome Drednaw."

                            nessa @talkingmouth "Yeah. She's a trooper. Moves slowly, and thinks things through, but when she decides to take action, she gets things done."
                            nessa @sad "I don't... I don't remember the last time she lost."

                            pause 1.0

                            nessa @talkingmouth "You said you had two things?"

                            red @talkingmouth "Yeah. Here."

                            show nessa surprisedbrow frownmouth with dis:
                                ease 0.5 zoom 0.9 ypos 0.9

                            nessa "The egg?"

                            red @talkingmouth "Yeah. Hilda felt badly about, uh, blowing up at you. So here, a peace offering."

                            nessa -surprisedbrow -frownmouth -surprised @talkingmouth "And you're her messenger?"

                            if (GetRelationship("Hilda") == "Caretaker"):
                                red @talkingmouth "Amongst other things."
                            else:
                                red @happy "For now, yeah!"

                            if (GetRelationship("Nessa") == "Friend"):
                                red @talkingmouth "Besides, I didn't want to do anything to jeopardize my chances of a second date. Thought you might reconsider after that battle."
                            else:
                                red @talkingmouth "Besides, I didn't want to do anything to jeopardize our date. Thought you might reconsider after that battle."

                            nessa @talkingmouth "...Nah. To be honest, I'm kind of impressed. I was outnumbered, but that doesn't matter most of the time."

                            nessa @talkingmouth "Getting past my Drednaw is a pretty big achievement. So pat yourself on the back."

                            $ ValueChange("Nessa", 3, 0.5)

                            nessa @happybrow talkingmouth "And thanks for the egg."

                else:
                    $ AddEvent("Nessa", "HasBonsly")
                    nessa @talkingmouth "Hm. Guess I'm taking the egg, then. No hard feelings?"

                    hilda @angry "Screw off!"

                    hide nessa
                    hide hilda
                    with dis

                    pause 1.0

                    red @closedbrow talking2mouth "Well, that was an awful time for everyone."

            ">Run":
                $ AddEvent("Nessa", "HasBonsly")
                narrator "Got away safely!"

    else:
        narrator "There doesn't seem to be much to do there now..."

elif (_return == "Garden"):
    if (not visitedgarden):
        $ visitedgarden = True
        show clouds
        show garden:
            zoom 0.625
        show ethan:
            xpos 0.75
        if (timeOfDay in ["Early Morning", "Morning", "Noon"]):
            show iris uniform:
                xpos 0.25
        else:
            show iris:
                xpos 0.25
        with dis

        narrator "As you walk into the garden, you hear what sounds like a light rustling in the bushes."

        ethan @surprised "Oh, heads up, man. A wild Pokémon?"

        red @closedbrow talking2mouth "Maybe."

        iris @talkingmouth "Would you like me to check it out, Mr. [last_name]?"

        red @talkingmouth "Nah. If it's in the garden, it probably isn't very dangerous. I don't think we need the skills of a real good battler for this one."

        show iris:
            xpos 0.25
            ease 0.2 ypos 1.1
            ease 0.2 ypos 1.0
            ease 0.2 ypos 1.1
            ease 0.2 ypos 1.0

        iris @happy "Oh, okay!"

        red @closedbrow talking2mouth "Hm, let's see, it's..."

        red @surprised "Oh!"

        $ sidemonnum = 440

        $ hideside = True

        show sideportraitfull with dis

        $ PlaySound("pokemon/cries/440.mp3")

        sidemon "Happ! Hap-hap-hap."

        $ hideside = False

        show sideportraitfull:
            ease 0.5 xpos 0.5 ypos 1.1 xzoom 1 zoom 0.7
            block:
                ease 2.0 xpos 0.25
                ease 0.1 xzoom -1
                ease 2.0 xpos 0.5
                ease 2.0 xpos 0.75
                ease 0.1 xzoom 1
                ease 2.0 xpos 0.5
                repeat

        pause 1.0

        narrator "A Happiny toddles unsteadily from the bushes. Based on its diminutive size, you can assume it's just hatched from one of the eggs that was hidden."

        iris @surprisedmouth happybrow "Oh, it's {i}soooo{/i} cute! I wanna hug it! But it's probably too young... ooh, but I want to!"

        ethan frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

        pause 1.0

        red @talkingmouth "You see it, too?"

        ethan @closedbrow talking2mouth "Yeah. It's looking for something."

        iris @surprised "Oh? What's it lookin' for?"

        red @talking2mouth "Well, Happiny usually carry around small, ovaloid stones, to practice for when they become Chansey. But since this Happiny's a newborn, it looks like it's looking for something to put in its pouch."

        show sideportraitfull:
            ease 1.0 xpos 0.5 xzoom 1

        red @talkingmouth "Maybe if I just..."

        show sideportraitfull:
            ease 0.3 xpos 0.75 xzoom 1

        red @surprised "Oh! Okay. She does {i}not{/i} want to be touched."

        ethan @closedbrow talking2mouth "It's probably feeling real insecure, since it's got this, like, urge to do something, but doesn't know what. Our knack for Pokémon might not be enough to overcome that."

        iris @talking2mouth "It might not let you close unless you help it..."

        red @talkingmouth "Hm..."

    if (happinyegg == None):
        show clouds behind sideportraitfull
        show garden behind sideportraitfull:
            zoom 0.625
        show ethan:
            xpos 0.75
        if (timeOfDay in ["Early Morning", "Morning", "Noon"]):
            show iris uniform:
                xpos 0.25
        else:
            show iris:
                xpos 0.25
        with dis
        $ sidemonnum = 440

        show sideportraitfull:
            xpos 0.5 ypos 1.1 xzoom 1 zoom 0.7
            block:
                ease 2.0 xpos 0.25
                ease 0.1 xzoom -1
                ease 2.0 xpos 0.5
                ease 2.0 xpos 0.75
                ease 0.1 xzoom 1
                ease 2.0 xpos 0.5
                repeat

        label happinyegg:

        menu:
            ">Give the Happiny an egg." if HasEgg():
                menu:
                    ">Hand over the Larvesta egg." if HasEgg("Larvesta Egg"):
                        $ del inventory[Item.LarvestaEgg]
                        $ happinyegg = "Larvesta Egg"
                        narrator "The Happiny juggles the egg for a bit, getting used to the heat, then tucks it into its pouch, seemingly contented."
                        jump gaveegg

                    ">Hand over the white egg with red and blue triangles." if HasEgg("Togepi Egg"):
                        $ del inventory[Item.TogepiEgg]
                        $ happinyegg = "Togepi Egg"
                        narrator "The Happiny tucks the egg into its pouch, seemingly contented."
                        jump gaveegg

                    ">Hand over the Tyrogue egg." if HasEgg("Tyrogue Egg"):
                        $ del inventory[Item.TyrogueEgg]
                        $ happinyegg = "Tyrogue Egg"
                        narrator "The Happiny tucks the egg into its pouch, seemingly contented."
                        jump gaveegg

                    ">Hand over the Smoochum egg." if HasEgg("Smoochum Egg"):
                        $ del inventory[Item.SmoochumEgg]
                        $ happinyegg = "Smoochum Egg"
                        narrator "The Happiny is surprised by the cold of the egg, and quickly tucks the egg into its pouch to warm it up, seemingly contented."
                        jump gaveegg

                    ">Hand over the red, warm, lumpy egg." if HasEgg("Magby Egg"):
                        $ del inventory[Item.MagbyEgg]
                        $ happinyegg = "Magby Egg"
                        narrator "The Happiny juggles the egg for a bit, getting used to the heat, then tucks it into its pouch, seemingly contented."
                        jump gaveegg

                    ">Hand over the rubbery blue egg." if HasEgg("Wynaut Egg"):
                        $ del inventory[Item.WynautEgg]
                        $ happinyegg = "Wynaut Egg"
                        narrator "The Happiny tucks the egg into its pouch, seemingly contented."
                        jump gaveegg
                        
                    ">Hand over the heavy, brown egg." if HasEgg("Bonsly Egg"):
                        $ del inventory[Item.BonslyEgg]
                        $ happinyegg = "Bonsly Egg"
                        narrator "The Happiny seems confused as to why you're giving it a log, before recognizing it as an egg, and tucking it into its pouch, seemingly contented."
                        jump gaveegg

                    ">Hand over the blue egg with the markings." if HasEgg("Mantyke Egg"):
                        $ del inventory[Item.MantykeEgg]
                        $ happinyegg = "Mantyke Egg"
                        narrator "The Happiny tucks the egg into its pouch, seemingly contented."
                        jump gaveegg

                    ">Hand over the purple, humming egg." if HasEgg("Toxel Egg"):
                        $ del inventory[Item.ToxelEgg]
                        $ happinyegg = "Toxel Egg"
                        narrator "The Happiny tucks the egg into its pouch, seemingly contented, though it jumps from the static every once in a while."
                        jump gaveegg

                    "Nevermind.":
                        jump happinyegg

            ">Come back later":
                jump wraparoundegghunt

        label gaveegg:
            $ sidemonnum = 440

            narrator "The Happiny, now calmed, sits patiently at your and Ethan's feet."

            iris @surprised "Wow! She really likes you two, Misters!"

            red @happy "What can I say?"

            ethan @happy "We've got a knack."

            iris @closedbrow talking2mouth "It's still a baby though. It should probably go to the research center, to get a check-up and shots and stuff."

            ethan @talkingmouth "For sure. Shall we, dude?"

            redmind @confusedeyebrows frownmouth "Shots? Are Pokémon meant to have {i}shots?{/i} Jeez. I'm so behind the curve..."

            red @happy "Yeah, let's do it."

            show blank2 with dis

            pause 1.0

            narrator "You carefully carry the Happiny back to the research center. By the time you arrive at the lab, she has drifted to sleep peacefully in your arms. You leave her with one of the incubators' attendants, then continue the egg hunt."
    
    else:
        narrator "There doesn't seem to be much to do there now..."

elif (_return == "Recreation Center"):
    if (not visitedrecreationcenter):
        $ visitedrecreationcenter = True
        show pool
        show ethan:
            xpos 0.25
        if (timeOfDay in ["Early Morning", "Morning", "Noon"]):
            show iris uniform:
                xpos 0.75
        else:
            show iris:
                xpos 0.75
        with dis

        narrator "As you walk into the recreation center, you notice there's an egg floating in the center of the pool. It's a deep, marine, blue, and has markings on it that vaguely resemble a happy face."

        red @closedbrow talking2mouth "Hm. Any idea what that one is?"

        ethan @talkingmouth "Blue eggs? I dunno. My old neighbor probably would. She was always fiddling around with eggs and stuff. Wooper, maybe?"

        red @talkingmouth "Yeah, maybe. I think--"

        show ethan surprisedbrow frownmouth
        show iris surprisedbrow frownmouth
        with dis

        show skyla surprisedbrow frownmouth with vpunch

        skyla "Oh, no! That egg is drowning!"

        red @surprised "D-drowning? What? I'm pretty sure eggs don't breathe..."

        skyla "No, no! The eggshells are porous! Air still needs to go in and out! That egg must've rolled into the pool!"

        narrator "At this, you notice a pile of towels with a slight indentation to the side of the pool. You could easily imagine the egg rolling off of it."

        ethan @talkingmouth "Well... we gotta rescue it!"

        skyla @talkingmouth "I'll jump in! Look away!"

        red @confused "Huh?"

        skyla "I need to take my clothes off! I can't let this outfit get wet, it practically becomes transparent!"

        ethan "What, you mean that's {i}not{/i} a swimsuit?! What is it, then?!"

        skyla @angry "Just don't peek!"

        show blank2 with transeye

        pause 2.0

        $ PlaySound("splash.ogg")

        pause 1.0

        hide iris

        menu:
            ">Just don't peek":
                narrator "You dutifully keep your eyes closed."

                pause 1.0

                narrator "...Though the temptation is nigh-unbearable."

                pause 1.0

                redmind @thinking "Why didn't I just jump in myself? Heck, I don't care if these clothes get wet."

                pause 1.0

                redmind @thinking "Hindsight is two thousand and twenty, I guess..."

                pause 1.0

                narrator "A few moments pass, and then..."

                skyla -surprisedbrow -frownmouth -surprised @talkingmouth "Alright, {i}now{/i} you can look."

                hide blank2 with transeye

                skyla sweat @happybrow talkingmouth "I rescued the egg!"
                skyla @happy "And... I might've made a bit of a silly mistake."

                ethan -surprisedbrow -frownmouth -surprised @closedbrow talking2mouth "Let me guess. It's a Water-type, and its eggs are safe underwater?"

                skyla @happy "Pretty sure, yeah! There's a thin layer of protective film that covers the egg. I think that would filter out the water."

                red @happy "Oh, well. The intention was there."

                skyla @talkingmouth "Yeah... but I sure feel dumb. Do you want the egg?"

                menu:
                    "Sure.":
                        $ GetItem("Mantyke Egg")

                    "Nah, go ahead.":
                        $ skylahasmantyke = True
                        $ ValueChange("Skyla", 3, 0.5, False)

                        skyla @happy "Aw, thanks."

            ">Just don't not peek":
                $ skylahasmantyke = True
                $ wasdick = True

                red @closedbrow talking2mouth "Surely just a single peek wouldn't--"

                ethan @surprised "Hey! What're you doing?"

                red @surprised "N-nothing! I mean, nothing much. Maybe something? I don't know!"

                pause 1.0

                red @confused "Wait, how did you know I was opening my eyes?"

                ethan @surprised "...Uhhhhhhh..."

                $ ValueChange("Skyla", -3, 0.5)

                skylatease @template angry "Hey! Eyes up front, busters!"

                pause 1.0

                ethan @closedbrow talking2mouth "{size=30}...Worth.{/size}"

                pause 1.0

                narrator "A few moments pass, and then..."

                skyla angrybrow frownmouth "Alright, {i}now{/i} you can look."

                hide blank2 with transeye

                skyla sweat @talkingmouth "I rescued the egg. No thanks to the peeping tom gallery over here."

                red @confused "My bad, but I could've just jumped into the water myself. I don't care if these clothes get wet."

                skyla @closedbrow talkingmouth "Yeah, well, you didn't. You're lucky I'm forgiving. Some girls would slap you for that."

                show skyla -angrybrow -frownmouth with dis

        pause 1.0

        skyla @surprised "Huh? Where'd that girl that was with you go?"

        red @confused "...Huh. I dunno. I guess she slipped away while my eyes were closed."

        skyla closedbrow talking2mouth "Hm. It's kinda weird, 'cause I could {i}swear{/i} that I'd seen her before..."

        pause 1.0

        skyla happy "Well, whatever. Good luck on the rest of the egg hunt!"

        hide skyla with dis

        pause 2.0

        if (timeOfDay in ["Early Morning", "Morning", "Noon"]):
            show iris uniform
        else:
            show iris

        ethan @happy "Oh, hey, there you are! Where'd you get up to?"

        iris @happy "Oh, Miss Skyla's from Unova. I could tell 'cause of her accent."

        red @confused "Uh... you got something against Unovans?"
        redmind @thinking "She's a little young to be racist, isn't she?"

        iris @talkingmouth "No, no, I'm from Unova, too! But, um..."
        iris @sadbrow happymouth "Unovan people get real weird when they see me, and I just want everyone to have fun lookin' for eggs."

        red @sad "Aw. I'm sure Skyla wouldn't get weird. She's a great person."

        if (GetRelationship("Skyla") == "Wingman"):
            red @happy "She wants to be a hero, you know!"

        iris happy "Well, that's okay. Maybe next time, then. Now, c'mon, let's go!"

        hide iris with dis

        pause 1.0

        red @closedbrow talking2mouth "That's a bit weird, right?"

        ethan @talking2mouth "Yeah, a bit. I feel like I've seen Sclera before as well, but..."

        pause 1.0

        red @closedbrow talking2mouth "Sclera? Do you mean Skyla? Or Iris?"

        ethan @surprised "The second one. Why, what'd I say?"
    
    else:
        narrator "There doesn't seem to be much to do there now..."

elif (_return == "Research Center"):
    if (not visitedresearchcenter):
        $ visitedresearchcenter = True
        show research
        show rosa:
            xpos 5/6
        show nate:
            xpos 4/6
        show leaf:
            xpos 3/6
        show ethan:
            xpos 2/6
        if (timeOfDay in ["Early Morning", "Morning", "Noon"]):
            show iris uniform:
                xpos 1/6
        else:
            show iris:
                xpos 1/6
        with Dissolve(1.0)

        pause 1.0

        show iris surprisedbrow frownmouth with dis

        pause 0.5

        show iris:
            ease 0.5 xpos -0.5
        show ethan:
            ease 0.5 xpos 0.2
        show leaf:
            ease 0.5 xpos 0.4
        show nate:
            ease 0.5 xpos 0.6
        show rosa:
            ease 0.5 xpos 0.8

        leaf @happy "Oh, hey!"

        rosa @sadbrow talkingmouth sweat "Hi, [first_name]! We were just having a talk here about... um, about Leaf... and how she's a {i}really{/i} big fan..."

        nate @happy "Yeah, Leaf's been telling us the whole runthrough of Rosa's career. I think we've just about reached 2003?"

        leaf @embarrassedbrow talkingmouth "Um... well, yes..."

        nate @talkingmouth "Well, hey, L, carry on. Don't let me stop you."

        leaf @angrybrow angrymouth "Hey, has anyone told you that's a bit rude?"

        nate @surprised "What?"

        leaf @closedbrow talking2mouth "Oh, I dunno, just calling me 'L.' I mean, of all the nicknames--really?"

        nate @surprised "Geez, I never even thought about that..."

        ethan @talkingmouth "Hey. Why don't you just give her a new nickname?"

        nate @talkingmouth "Oh, like I did with you?"

        ethan @happy "Yeah, exactly!"

        red @confused "Huh, I didn't realize re-nicknaming was an option. When did this happen?"

        ethan @talkingmouth "Hm? Oh, I was hanging out with this guy last weekend. He was askin' all sorts of questions about--"

        nate @surprised "Hey! C'mon, Ethan, don't spill my beans like that. This is meant to be a secret, right?"

        ethan @surprised "Oh... yeah, sorry! My bad."

        rosa @closedbrow talking2mouth "So... what's your Nate-name?"

        ethan @happy "Well, he already knows an 'E,' so I go by MC²! Pretty clever, right?"

        nate @angrybrow talking2mouth "Hey."

        ethan @closedbrow talking2mouth "Alright, he came up with it."

        leaf @closedbrow talkingmouth "So... can you change my nickname to, like, 'Princess?'"

        red @closedbrow talking2mouth "I thought you were a queen? Or possibly a pirate ship captain?"

        nate @closedbrow talking2mouth "Guys, the name thing is just a casual shorthand I use. If we spend a bunch of time figuring out what everyone's nicknames are, then all the time and memory space I would have saved is wasted. I'm not a Name Rater."

        pause 1.0

        leaf @sarcastic "So no Princess." 

        nate @closedbrow talking2mouth "No. Three characters or less."

        leaf "{w=0.5}.{w=0.5}.{w=0.5}."

        show leaf bigblush flirtbrow talkingmouth with dis     

        leaf "...Sex."

        nate @happy "'Preciate the offer, but no thanks. I'm swinging for the other team right now."

        show ethan:
            ease 0.5 xpos 0.2

        leaf -flirtbrow -talkingmouth @closedbrow talking2mouth "Ugh, it's {i}always{/i} like that, isn't it?"

        show rosa surprisedbrow frownmouth
        show ethan surprisedbrow frownmouth

        leaf @talking2mouth "Hey, [first_name], just so I'm not wasting my time, you {i}do{/i} like girls, right?"

        pause 1.0

        redmind @surprisedbrow frownmouth "Damn, this girl is forward."

        show ethan -surprisedbrow -frownmouth -surprised
        show rosa -surprisedbrow -frownmouth -surprised
        with dis

        red @talkingmouth "Uh, yep.{w=0.5} Women.{w=0.5} And Men.{w=0.5} And everything in-between.{w=0.5} And outside.{w=0.5} And, uh... yeah.{w=0.5} Girls."

        leaf @talkingmouth "Cool."

        pause 1.0

        leaf @flirtbrow talkingmouth "And what about you, Backup Plan?"

        ethan -surprisedbrow -frownmouth -surprised @angry "Oh, come on!"

        nate @happy "Hey, she didn't say she was talkin' to you. She could be talking about R!"

        leaf -bigblush @surprised "Oh my god, could I, though? [first_name], forget you. Rosa, you're at the top of my list now. Would you? Swear to god, I'm not gold-digging."

        rosa @happy sweat "Uh, no! Sorry! Can't do that. Um, wouldn't {i}want{/i} to do that. No offense."

        leaf @closedbrow talking2mouth "Damn."

        leaf @sarcastic "Alright, fine, I guess you're back at the top of my list, [first_name]."

        red @confused "Imagine my joy."

        leaf @talking2mouth "Yeah, you're blessed. Anyway, wrapping back around to the real point of the convo... Nate, can't you just call me, like, LG?"

        nate @closedbrow talking2mouth "Life's good? Sure."

        leaf @sarcastic "Uh, no. Leaf Green."

        red @closedbrow talking2mouth "Tell me that's not your name."

        leaf @angry "What?! It's totally my name! And it's an awesome name, too!"

        ethan @talking2mouth "It sounds like a dispensary, dude."

        leaf @talking2mouth "Oh, yeah? Well, what's your last name?!"

        ethan @talkingmouth "Gold."

        leaf @closedbrow talking2mouth "Oh, that's actually kinda cool. Uh, give me a second to think up something snarky..."

        pause 1.0

        leaf @sarcastic "Gold? More like silver."

        ethan @closedbrow talking2mouth "Wow, {i}never{/i} heard that one before."

        red @talkingmouth "How are you guys doing on the egg hunt? Find anything good?"

        nate @surprised "Oh, yeah! We were actually just about to battle to figure out who gets this little guy."

        narrator "You see, behind Nate, there's a purple egg with some light-purple thunderbolt patterns on it. It hums quietly, like it's charged with static electricity."

        nate @happy "But then LG showed up and fangirled all over R, so... yeah. Got a bit distracted."

        leaf @happy "Oh, we could do a two-on-two!"

        red @confused "Yeah, but then somebody would have to--"

        ethan @happy "Eh, I'll step out. I learn more by watching, anyway. Go ahead."

        pause 1.0

        red @talking2mouth "If you're sure."

        ethan @talkingmouth "Don't worry about it."

        show ethan:
            ease 0.5 xpos 0.2

        leaf @closedbrow talkingmouth "Well... who do you want to join, [first_name]?"

        $ trainer1 = Trainer("red", TrainerType.Player, playerparty)
        $ trainer2 = MakeTrainer("Nate")
        $ trainer3 = MakeTrainer("Rosa")
        $ trainer4 = MakeTrainer("Leaf")
        $ invitedleaf = False

        label triplefight:

        menu:
            "I'll join Nate.":
                $ ValueChange("Nate", 1, 0.6)

                nate @happy "Alright, males against females, then? Cool, cool."

                leaf @sarcastic "Ugh. 'Males', 'Females.' What are you, a breeder?"

                nate @happy "Hah, no way! I haven't even hit second base yet."

                nate @talkingmouth "Serious talk, though, it's just military parlance. Picked it up from my Mom. No disrespect intended."

                leaf @talking2mouth "Whatever, jughead."

                nate @talking2mouth "Pretty sure you mean jarhead. And, uh, Navy, not Marines."

                leaf @happy "I repeat: What-{i}ever.{/i} I'm going to get to trounce some boys alongside my idol in a battle. This is the best day ever."

                red @confused "Uh, pretty cocky, aren't you? How do you know team masculinity won't win?"

                leaf @flirttalk "Oh, my dear, poor, foolish, child."

                if (WonBattle("Leaf1")):
                    leaf @happy "The only reason you won our Battle Team tryout match was because my Dragon Rages were {i}seriously{/i} nerfed. That's no longer the case!"

                else:
                    leaf @happy "Have you forgotten how our Battle Team tryout match went?"

                red @closedbrow talking2mouth "Hmm..."

                leaf @talking2mouth "Hey, Rosa, if we beat them, can we take a victory selfie together?"

                rosa @sweat happy "Um... that's kinda against my contract... but sure! As long as you don't post it anywhere."

                nate @talkingmouth "Then I guess it's up to me to protect the sanctity of Rosa's contract. You're not getting through my team."

                leaf @sarcastic "{size=30}Nonbattleteammembersayswhat?{/size}"

                nate @talking2mouth "...Yeah, okay. Let's do this."

                $ trainer2.Type = TrainerType.Ally
                call Battle([trainer1, trainer2, trainer3, trainer4]) from _call_Battle_59
                $ battlehistory["LeafRosa1"] = _return

                show leaf:
                    xpos 0.4
                show nate:
                    xpos 0.6
                show rosa:
                    xpos 0.8
                with dis

                if (WonBattle("LeafRosa1")):
                    $ ValueChange("Leaf", 3, 0.4, False)
                    $ ValueChange("Rosa", 3, 0.8)

                    leaf @surprised "No... even with my full-power Dratini, you still...?"
                    $ firstinitial = first_name[0]
                    nate @talking2mouth "Hm. Your battle style, [firstinitial]... you've gotten more focused."
                    nate @happy "Pretty cool."

                    rosa @sadbrow happymouth "Oh, darn. Well, I can probably ask the agency to send me a new one a while from now..."

                    nate @happy "Yeah, good luck on that front. So, [firstinitial]? Who'd'ya think should get this egg? You or me, buddy?"

                    menu:
                        ">Give him the egg":
                            $ AddEvent("Nate", "HasToxel")
                            $ ValueChange("Nate", 3, 0.6, False)

                            nate @happy "Noted. Thanks!"

                        ">Keep the egg":
                            $ GetItem("Toxel Egg")

                            nate @happy "Noted."

                else:
                    $ rosahastoxel = True
                    rosa @happy "Yes! It was a long shot, but we did it, Leaf!"

                    leaf @happy "Yeah, we did! You and me! And as a sign of my fanship, here--the egg!"

                    rosa @surprised "Me? But couldn't you use it?"

                    leaf @sadbrow happymouth "Yeah, but... your team. I think I know what's going on there. You {i}need{/i} this egg."

            "I'll join Rosa.":
                $ ValueChange("Rosa", 1, 0.8)

                rosa @happy "Hey, thanks!"

                leaf @surprised "Oh my god. I'm going to get to beat my idol in a battle. This is the best day ever."

                red @confused "Uh, pretty cocky, aren't you? How do you know team [first_name]-Rosa won't win?"

                leaf @flirttalk "Oh, my dear, poor, foolish, child."

                if (WonBattle("Leaf1")):
                    leaf @happy "The only reason you won our Battle Team tryout match was because my Dragon Rages were {i}seriously{/i} nerfed. That's no longer the case!"

                else:
                    leaf @happy "Have you forgotten how our Battle Team tryout match went?"

                red @closedbrow talking2mouth "Hmm..."

                leaf @talking2mouth "Hey, Rosa, if I beat you, will you let me take a couple pictures with you?"

                rosa @sweat happy "Um... that's kinda against my contract... but sure!"

                nate @talkingmouth "Well, sorry to disappoint, LG, but if {i}I{/i} land the finishing blow, I get the picture."

                leaf @sarcastic "{size=30}Nonbattleteammembersayswhat?{/size}"

                nate @talking2mouth "...Yeah, okay. Let's do this."

                $ trainer3.Type = TrainerType.Ally
                call Battle([trainer1, trainer3, trainer2, trainer4]) from _call_Battle_60
                $ battlehistory["LeafNate1"] = _return

                show leaf:
                    xpos 0.4
                show nate:
                    xpos 0.6
                show rosa:
                    xpos 0.8
                with dis

                if (WonBattle("LeafNate1")):
                    $ ValueChange("Leaf", 3, 0.4, False)
                    $ ValueChange("Nate", 3, 0.6)

                    leaf @surprised "No... even with my full-power Dratini, you still...?"
                    
                    nate @talking2mouth "Hm. Your battle style... you've gotten more focused."
                    nate @happy "Pretty cool."

                    rosa @sadbrow happymouth "Well, that's pretty cool! We won! So, um, do you want the egg, or can I take it?"
                    rosa @sadbrow talkingmouth "Um... that egg is one of the few Pokémon my agency approved that I can actually use, so... if you don't mind..."

                    leaf @surprised "Oh, for real?"

                    leaf @angry "Hey, [first_name]! Do the right thing! Give her that egg!"

                    menu:
                        ">Give her that egg":
                            $ rosahastoxel = True
                            $ ValueChange("Rosa", 3, 0.8, False)

                            rosa @happy "Oh, thank you very much! I really appreciate your support!"

                            pause 1.0

                            rosa @sadbrow happymouth "Er, sorry, autopilot. But I really am thankful!"

                        ">Don't give her that egg":
                            $ GetItem("Toxel Egg")

                            leaf @sad "No... I'm sorry, Rosa. I've failed you..."
                            rosa @sweat happy "Um, this really isn't that big of a deal."

                else:
                    $ rosahastoxel = True
                    rosa @happy "Oh, well. It was a long shot."

                    nate @talkingmouth "Yeah, you did pretty well, all things considered."
                    nate @happy "Anyway, want the egg, LG?"

                    leaf @closedbrow talkingmouth "Hm... Yes."

                    nate @talkingmouth "Cool."

                    narrator "Leaf happily takes the egg... and immediately hands it to Rosa."

                    pause 1.0

                    nate @closedbrow talking2mouth "Can't say I'm surprised."

                    rosa @surprised "Oh! Um... I lost, though."

                    leaf @talking2mouth "Yeah, but... your team. I think I know what's going on there. You {i}need{/i} this egg."

            "I'll join you." if not invitedleaf:
                $ invitedleaf = True
                leaf blush @surprised "R-really?"

                red @sadbrow talkingmouth "What's surprising about that?"

                leaf @talkingmouth "Um... I mean... you have the chance to team up with an internationally-famous movie star..."

                red @talkingmouth "Sure do. And I chose you."

                pause 1.0

                $ ValueChange("Leaf", 1, 0.4)

                leaf bigblush @surprisedbrow happymouth "Ah, no, no, no! I can't take that! You're too earnest! Just, gah... pick someone else!" 

                show leaf -bigblush with dis

                jump triplefight

            "I'll take you all on!":
                show leaf surprisedbrow frownmouth
                show rosa surprisedbrow frownmouth
                show nate surprisedbrow frownmouth
                with dis

                pause 2.0

                show leaf flirt
                show nate angrybrow
                show rosa angrybrow
                with dis

                pause 1.0

                red @surprised "Uh... I feel like my mouth may have written a check I can't cash..."

                leaf @talkingmouth "I'll give you one chance to back out, skippy."

                menu:
                    "Nothing ventured, nothing gained!":
                        leaf @closedbrow talkingmouth "Is this your first time against three at once?"
                        leaf "I'll be gentle."

                        rosa @talkingmouth "This'll definitely be a show, no matter how it turns out. Let me just set up a camera..."

                        nate @closedbrow talking2mouth "Choosing to be outnumbered and outgunned here, huh. Three people against one..."
                        nate @happy "Looks like the odds are against you!"

                        red @angry "Was that a pun? It was a bad one. That was a bad pun!"

                        call Battle([trainer1, trainer2, trainer3, trainer4]) from _call_Battle_61
                        $ battlehistory["LeafNateRosa1"] = _return

                        show leaf:
                            xpos 0.4
                        show nate:
                            xpos 0.6
                        show rosa:
                            xpos 0.8
                        with dis

                        if (WonBattle("LeafNateRosa1")):
                            $ ValueChange("Leaf", 3, 0.4, False)
                            $ ValueChange("Nate", 3, 0.6, False)
                            $ ValueChange("Rosa", 3, 0.8)

                            red @surprised "Wow. Didn't think I'd make it through that one."

                            leaf @surprised "Uh... wow. Okay, that was... yeah. Damn."
                            
                            nate @talking2mouth "Totally outnumbered, and you still pulled through. Huh."
                            nate @happy "Pretty cool."

                            rosa @sadbrow talking2mouth "Eeesh. That was a great fight, but I don't think I can use that footage... it's just embarrassing, losing that hard!"

                            leaf @flirttalk "Well, victor, who gets the egg? We, the lowly defeated, must bow to your judgment."

                            rosa @sadbrow talkingmouth "Um... that egg is one of the few Pokémon my agency approved that I can actually use, so... if you don't mind..."

                            leaf @surprised "Oh, for real? Well, uh, I'll pull out, then."

                            pause 1.0

                            leaf @angrybrow angrymouth "Hey. Nate. Anything you want to say?"

                            nate @happy "Nah! I still want it."

                            leaf @angry "Hey! Rosa is a {i}princess{/i}, and she deserves anything she wants!"

                            nate @talkingmouth "I thought you were the princess, LG? Or was that Queen?"

                            leaf @angry "There can be multiple princesses! Do you {i}know{/i} how many concubines the king has?"

                            rosa @happy "Um, I don't want to cause any trouble. If you want to give the egg to Nate, or keep it, that's totally fine."

                            redmind @thinking "I believe her... but she's an amazing liar, so who knows if she's telling the truth."

                            menu:
                                ">Give the egg to Nate":
                                    $ AddEvent("Nate", "HasToxel")
                                    $ ValueChange("Nate", 3, 0.6, False)

                                    nate @happy "Sick."

                                ">Give the egg to Rosa":
                                    $ rosahastoxel = True
                                    $ ValueChange("Rosa", 3, 0.8, False)

                                    rosa @happy "Oh, thank you very much! I really appreciate your support!"

                                    pause 1.0

                                    rosa @sadbrow happymouth "Er, sorry, autopilot. But I really am thankful!"

                                ">Keep the egg":
                                    $ GetItem("Toxel Egg")

                                    leaf @sad "No... I'm sorry, Rosa. I've failed you..."
                                    rosa @sweat happy "Um, this really isn't that big of a deal."

                        else:
                            $ rosahastoxel = True

                            red @happy "Oh, well. It was a long shot."

                            nate @talkingmouth "Yeah, you did pretty well, all things considered."

                            pause 1.0

                            leaf @closedbrow talkingmouth "Us beating him didn't actually solve anything, did it?"

                            nate @closedbrow talking2mouth "Nope."

                            rosa @closedbrow talking2mouth "Well... um... if it matters, at all... that egg hatches into one of the few Pokémon my agency lets me use that I can actually train, so..."

                            pause 1.0

                            leaf @angrybrow angrymouth "So you're not going to take that away from Queen Rosa, are you, {i}Nathan?{/i}"

                            nate @surprised "Woah. You sound like my Mom."

                            pause 1.0 

                            nate @closedbrow talking2mouth "Yeah, alright, Rosa. You can take the egg."

                            rosa @happy "Oh, thank you very much! I really appreciate your support!"

                            pause 1.0

                            rosa @sadbrow happymouth "Er, sorry, autopilot. But I really am thankful!"

                    "Let me save first...":
                        ethan @happy "Heh. Video game joke."

                        show leaf -flirt
                        show nate -angrybrow
                        show rosa -angrybrow
                        with dis

                        jump triplefight

        red @closedbrow talking2mouth "Yeah, actually, I've got a question about your team, Rosa."

        rosa @closedbrow talking2mouth "Oh, no. It's, um... it looks a bit silly, doesn't it?"

        nate @closedbrow talking2mouth "Yeah. A Charmander, a Pikachu, and an Eevee? Kinda an overplayed hand, isn't it, R?"

        rosa @sadbrow happymouth "Little bit, yeah. But the agency said I'll need to use them for future shoots, so... I thought I might as well get used to them..."
        rosa @sweat happy "But I don't know anything about their species, except my own Pikachu! I don't have any idea how to train them, and they don't listen to me, either."

        rosa @closedbrow talking2mouth "I might just have to see if the agency can send someone to train them for me... but that'd kinda defeat the point of being at Kobukan, wouldn't it?"

        pause 1.0

        show rosa surprisedbrow frownmouth
        show nate surprisedbrow frownmouth
        show ethan surprisedbrow frownmouth
        show leaf surprisedbrow frownmouth 
        with dis

        red @surprised "Oh my god."

        ethan "Huh? What is it, dude?"

        red @surprised "Where'd she go?"

        ethan @closedbrow talking2mouth "Where'd who--"

        ethan @surprised "Oh, shoot! Uh, I dunno!"

        red @happy "Ah, sorry, guys! Gotta go!"

        hide rosa
        show nate -surprisedbrow -frownmouth -surprised
        hide ethan
        show leaf -surprisedbrow -frownmouth -surprised 
        with dis

        $ PlaySound("fading_footsteps.ogg")

        pause 1.0

        leaf @flirtbrow talking2mouth "Running after Tia again, huh..."

        nate @talkingmouth "Hm? Tia?"

        leaf @surprised "Oh! Uh, no, nothing. She's just a new friend of [first_name]'s."

        nate @happy "Just a friend? Cool, cool. Let's talk for a bit about that."

        leaf @sad "Uh... I'm not sure..."

    elif (PlacesVisited() == 10):
        narrator "Would you like to go to the Research Center to end your day, or do you have more to do?"

        menu:
            "Yes, I'm finished.":
                jump endegghunt

            "There's more to do.":
                jump egghuntoptions
    
    else:
        narrator "There doesn't seem to be much to do there now..."

label wraparoundegghunt:

if (PlacesVisited() != 10):
    hide blank2
    
    if (PlacesVisited() == 2 and timeOfDay != "Morning"):
        call clearscreens from _call_clearscreens_65
        show blank2
        show morning at vspaz
        with dis

        $ timeOfDay = "Morning"

        pause 3.5

        $ renpy.transition(dissolve)
        show screen currentdate    
        hide blank2
        hide morning 
        with dis
    
    elif (PlacesVisited() == 4 and timeOfDay != "Noon"):
        call clearscreens from _call_clearscreens_66
        show blank2
        show noon at vspaz
        with dis

        $ timeOfDay = "Noon"

        pause 3.5

        $ renpy.transition(dissolve)
        show screen currentdate    
        hide blank2
        hide noon 
        with dis

    elif (PlacesVisited() == 6 and timeOfDay != "Afternoon"):
        call clearscreens from _call_clearscreens_67
        show blank2
        show afternoon at vspaz
        with dis

        $ timeOfDay = "Afternoon"

        pause 3.5

        $ renpy.transition(dissolve)
        show screen currentdate
        hide afternoon 
        hide iris
        with dis

        iris uniform @frownmouth "Jeezy louisey! It's hot out here. I'm going to take my disguise off."

        pause 1.0

        iris -uniform @happy "There we go! It was super-stuffy wearing this all day underneath my disguise."

        redmind @confusedeyebrows frownmouth "I mean... I'm not sure the disguise was doing anything in the first place, but now it {i}definitely{/i} won't."

        hide blank2 with dis

    elif (PlacesVisited() == 8 and timeOfDay != "Evening"):
        call clearscreens from _call_clearscreens_68
        show blank2
        show evening at vspaz
        with dis

        $ timeOfDay = "Evening"

        pause 3.5

        $ renpy.transition(dissolve)
        show screen currentdate    
        hide blank2
        hide evening 
        with dis        

    jump egghuntoptions

narrator "Would you like to go to the Research Center to end your day, or do you have more to do?"

menu:
    "Yes, I'm finished.":
        pass

    "There's more to do.":
        jump egghuntoptions

label endegghunt:

$ HealParty()

stop music fadeout 3.5

call clearscreens from _call_clearscreens_69
show blank2
show night at vspaz
with dis

$ timeOfDay = "Night"

pause 3.5

$ renpy.transition(dissolve)
show screen currentdate    
hide blank2
hide night 
with dis

scene garden night

queue music "audio/music/nuvema2_start.ogg" noloop
queue music "audio/music/nuvema2_loop.ogg"

red night @surprised "Damn! It's gotten late. Have we seriously been doing this {i}all{/i} day?"

show ethan at leftside, night with dis

ethan @talkingmouth "Guess so, man."

show iris at rightside, night with dis

iris @closedbrow talking2mouth "I'm sleepy..."

red @sadbrow talkingmouth "It's probably past your bedtime, isn't it? Why don't we see if we can find your Dad now?"

iris @sadbrow frownmouth "Aw... but I wanna keep lookin' for eggs..."

ethan @sadbrow talkingmouth "I get ya, but it's getting really dark. We should probably head back home before it gets too late."

iris @sadbrow talking2mouth "Okay, Mr. Gold. But only 'cause you're a grown-up, so I hafta listen to you."

ethan @happy "Darn right."

red @talkingmouth "Do you know where your Dad might be, Iris?"

iris @closedbrow talking2mouth "Yeah, I think he's in the academy building."

red @closedbrow talking2mouth "Makes sense. Let's just go by the research center to drop off our eggs, then."

show ethan frownmouth with dis:
    ease 0.5 xpos 0.2
show iris frownmouth with dis:
    ease 0.5 xpos 0.8

show mace at night:
    xpos 0.4
show face at night:
    xpos 0.6
with dis

stop music fadeout 1.5

queue music "audio/music/tension_start.ogg" noloop
queue music "audio/music/tension_loop.ogg"

mace @angrybrow happymouth "Not so fast."

face @angrybrow happymouth "We'll be relieving you of those eggs."

red @confused "...You serious?"

mace @angry "Deadly serious. These eggs are the progeny of champions. Their legacy should only be in the hands of trainers who would know how to use them."

if (HasEgg() == False):
    red @confused "I don't even have any eggs, guys. You're barking up the wrong tree."

mace @talkingmouth "Regardless of whatever eggs {i}you{/i} might have on hand, you aren't our only target."

face @talkingmouth "And what of your companions? The man who got into the Battle Team with an {i}atrocious{/i} tryout performance? {i}Nothing{/i} suspicious there."

mace @angry "And don't get me started on the {i}literal child{/i} you have tagging along. She isn't even a student! {i}Our tuition{/i} pays for access to these eggs!"

face @angrybrow talkingmouth "The fact the school turns the acquisition of such a valuable battle asset into a game is bad enough..."

red @closedbrow talking2mouth "You guys understand this is robbery, right? Like, this isn't just a hazing ritual. I could report you to the Office of Student Conduct and Conflict Resolution. Heck, I could report you to the {i}cops.{/i}"

mace @angrybrow talkingmouth "Yes, and we could just as easily tell the student body that you've only gotten into this school because you're 'best buds' with Professor Oak."

face @happy "You should consider yourself grateful that we only put up posters exposing your weekend hobbies, trashman!"

pause 1.0

red @surprised "Oh my god, that was you?"

mace @angry "I hope you see, now, how serious we--"

stop music

queue music "Audio/Music/Show Me Around.ogg"

red @happy "Thanks!"

mace @surprised "Beg pardon?"

red @talkingmouth "Yeah, people have been talking about my campaign non-stop ever since. That gave me a seriously-needed boost in the public eye. You really helped me out."

pause 1.0

face @angry "{size=30}Piss.{/size}"

mace @angrybrow talkingmouth "{size=30}See? I told you this was a bad idea! I {i}told{/i} you this wouldn't work.{/size}"

face @angrybrow talking2mouth "{size=30}It was {i}your{/i} idea!{/size}"

mace @angry "{size=30}It most certainly was not!{/size}"

red @confused "Hey, kinda out of the blue, but what's you guys' relationship?"

ethan @closedbrow talking2mouth "I've been wondering that, too. The matching clothes are throwing me off. Are you, like, siblings? Lovers? Both?"

mace @angry "I don't see how that's in {i}any{/i} way any business of yours."

pause 1.0

ethan @happy "Both, got it."

mace @angry "We are NOT--"

show ethan surprisedbrow frownmouth
show mace surprisedbrow frownmouth
show face surprisedbrow frownmouth
show iris surprisedbrow frownmouth
with dis

$ PlaySound("pokemon/cries/428.mp3")

pause 1.0

red @closedbrow talking2mouth "What was...?"

stop music fadeout 1.5

show flashback with dis

$ renpy.music.queue("Audio/Music/RelicCastle_Start.ogg", channel='music', loop=None, tight=None, fadein=2.5)
$ renpy.music.queue("Audio/Music/RelicCastle_Loop.ogg", channel='music', loop=True, tight=None)

hide mace
hide face
hide iris
hide ethan
with dis

redmind @thinking "Why do I feel this intense pressure? I've felt it once before, but..."

pause 1.0

redmind @frownmouth "Something's coming."

pause 1.0

show garden night:
    align (0.5, 0.5) 
    ease 7.0 zoom 1.4
    ease 0.5 zoom 1.0

pause 7.0

show buneary as buneary1 at night:
    xpos 1/8 xanchor 0.5 zoom 0.0 xzoom -1 yalign 0.5
    parallel:
        ease_bounce 2.0 yalign 1.0
    parallel:
        ease 2.0 zoom 1.0
show buneary as buneary2 at night:
    xpos 2/8 xanchor 0.5 zoom 0.0 xzoom -1 yalign 0.5
    parallel:
        ease_bounce 1.1 yalign 0.9
    parallel:
        ease 1.1 zoom 1.0
show lopunny as lopunny1 at night behind buneary2:
    xpos 3/8 xanchor 0.5 zoom 0.0 xzoom -1 yalign 0.5
    parallel:
        ease_bounce 1.6 yalign 0.8
    parallel:
        ease 1.6 zoom 1.0
show megalop behind lopunny1 at night:
    xpos 4/8 + 0.05 xanchor 0.5 zoom 0.0 yalign 0.5
    parallel:
        ease_bounce 2.5 yalign 0.7
    parallel:
        ease 2.5 zoom 1.4
show lopunny as lopunny2 at night:
    xpos 5/8 xanchor 0.5 zoom 0.0 yalign 0.5
    parallel:
        ease_bounce 1.5 yalign 0.8
    parallel:
        ease 1.5 zoom 1.0
show buneary as buneary3 at night:
    xpos 6/8 xanchor 0.5 zoom 0.0 yalign 0.5
    parallel:
        ease_bounce 1.2 yalign 0.9
    parallel:
        ease 1.2 zoom 1.0
show buneary as buneary4 at night:
    xpos 7/8 xanchor 0.5 zoom 0.0 yalign 0.5
    parallel:
        ease_bounce 1.8 yalign 1.0
    parallel:
        ease 1.8 zoom 1.0

hide flashback with dis

pause 2.0

red @surprised "Crap, there's a lot of them! I'll take the big one, you guys try to handle the others!"

$ trainer1 = MakeRed()
$ lopunnyobj = Pokemon(428.1, level=20, moves=[GetMove("Mirror Coat"), GetMove("Magic Coat"), GetMove("Jump Kick"), GetMove("Bounce")], ability="Scrappy", frenzynerf=(11, ["Pound", "Endure", "Mirror Coat", "Return"], 428), shinylock=False)
$ lopunnyobj.ApplyStatus("frenzied")
$ sidemonnum = 428.1
$ trainer2 = Trainer("sideportraitfull", TrainerType.Enemy, [lopunnyobj], isPokemon=True)

hide lopunny1
hide lopunny2
hide megalop
hide buneary1
hide buneary2
hide buneary3
hide buneary4

call Battle([trainer1, trainer2], healParty=False, specialmusic="Nothing", unrunnable=True) from _call_Battle_62
$ battlehistory["Lopunny1"] = _return

$ lopunnyobj.Id = 428
$ lopunnyobj.UpdateLevel(11)
$ lopunnyobj.Experience = lopunnyobj.CalculateAllExperienceNeededForLevel(11)
$ lopunnyobj.Ability = RandomChoice(["Klutz", "Cute Charm"])
$ lopunnyobj.UpdateMoves(["Pound", "Endure", "Mirror Coat", "Return"])

show iris at farleftside, night
show ethan at leftside, night 
with dis

if (lopunnyobj in playerparty or lopunnyobj in box):
    $ ValueChange("Ethan", 3, 0.25)
    ethan @surprised "Woah. Nice catching it, dude."

elif (WonBattle("Lopunny1")):
    $ ValueChange("Ethan", 1, 0.25)
    ethan @talkingmouth "Nice beating it, dude."

else:
    ethan @sad "Ah... looks like it ran away. You okay, dude?"

red night @closedbrow talking2mouth "Yeah. But... I'm confused."

ethan frownmouth @closedbrow talking2mouth "Right. I only {i}just{/i} learned this, but that was a Mega-Evolved Lopunny. Don't Pokémon need trainers to Mega Evolve? How did it do that?"

red @sad "I don't know, man. I've never heard of {i}anything{/i} like that before. Everything I know about Mega Evolution tells me that there needs to be a mega stone, a key stone, and a trainer involved."

red @closedbrow talking2mouth "And this was clearly a wild Pokémon."

if (lopunnyobj in playerparty or lopunnyobj in box):
    red @closedbrow talking2mouth "I mean, my Poké Ball wouldn't have worked on it if it was registered to another trainer."

ethan @closedbrow talking2mouth "No kidding."

red @closedbrow talking2mouth "Hm..."

pause 1.0

iris @happy "I've hearda somethin' like this before."

red @surprised "Huh?"

iris @happy "Yeah! There's a big ol' dragon from Hoenn called... um... Rayquaza. It showed up a few years ago, when I was a kid. And it can Mega Evolve without a trainer."
iris @angrybrow happymouth "I know a {i}lotta{/i} 'bout dragons."

pause 1.0

redmind @thinking "It would be easy to dismiss that as a child's imagination, but..."

red @talkingmouth "Do you know {i}how{/i} it does that?"

iris @talkingmouth "Yep. It's got a special organ. The mi-ka-do organ. And it eats up meteors to charge it with energy!"

red @surprised "Meteors?"

iris @happy "Yeah!"

red @closedbrow talking2mouth "So... if another Pokémon, like, for example, a Lopunny, ate a fragment of a meteor... would it be able to Mega Evolve, too?"

iris @closedbrow talking2mouth "Mmm... I don't think so. Rayquaza's the only one with that organ, I think. And it's prolly gotta be a special kind of meteor. Like how grown-ups need to eat their broccoli to get big."

red @closedbrow talking2mouth "Hm..."

pause 1.0

ethan @closedbrow talking2mouth "What're you thinking, man?"

red @happy "I'm thinking I'm out of my depth, here! I guess it's something to ask Sam."

ethan @closedbrow talking2mouth "Yeah... I guess so. Well, let's go back to the Research Center. We've still gotta drop these eggs off."

red @surprised "Oh, right!"

hide ethan
hide iris
show blank2 
with Dissolve(1.0)

label eggdonation:

$ numeggs = NumEggs()
if (numeggs > 1):
    Character("Attendant") "\"Welcome. It looks like you currently have... [numeggs] eggs with you. Would you like to donate any of them to the school, or have us keep them until they hatch?\""

    menu:
        ">Donate the Larvesta egg." if HasEgg("Larvesta Egg"):
            $ del inventory[Item.LarvestaEgg]
            jump eggdonation

        ">Donate the white egg with red and blue triangles." if HasEgg("Togepi Egg"):
            $ del inventory[Item.TogepiEgg]
            jump eggdonation

        ">Donate the Tyrogue egg." if HasEgg("Tyrogue Egg"):
            $ del inventory[Item.TyrogueEgg]
            jump eggdonation

        ">Donate the Smoochum egg." if HasEgg("Smoochum Egg"):
            $ del inventory[Item.SmoochumEgg]
            jump eggdonation

        ">Donate the red, warm, lumpy egg." if HasEgg("Magby Egg"):
            $ del inventory[Item.MagbyEgg]
            jump eggdonation
            
        ">Donate the rubbery blue egg." if HasEgg("Wynaut Egg"):
            $ del inventory[Item.WynautEgg]
            jump eggdonation

        ">Donate the heavy, brown egg." if HasEgg("Bonsly Egg"):
            $ del inventory[Item.BonslyEgg]
            jump eggdonation

        ">Donate the blue egg with the markings." if HasEgg("Mantyke Egg"):
            $ del inventory[Item.MantykeEgg]
            jump eggdonation

        ">Donate the purple, humming egg." if HasEgg("Toxel Egg"):
            $ del inventory[Item.ToxelEgg]
            jump eggdonation

        ">Keep the rest":
            Character("Attendant") "\"Very well.\""

else:
    narrator "You and Ethan deposit your eggs with the attendants at the Research Center, and prepare to leave."

pause 1.0

red -night @happy "Hey, Iris. Since you're not a student here, you're not planning on keeping those eggs you've got, are you?"

iris @talking2mouth "Nope. I'm gonna give it to the school. I've already got a big version of this one, anyway."

narrator "Peering at the eggs in Iris' hands, you see a pair of smaller eggs with a blue base. The top half is covered in a rough, black, furlike substance peppered with infrequent red triangles."

iris @closedbrow talking2mouth "Hm... actually..."

if (not wasdick and NumEggs() <= 3):
    iris @happy "How's about you take it, Mr. [last_name] and Mr. Gold?"

    red @surprised "What? No way! I mean, you found 'em, right?"

    iris @happy "Yeah, but, like I said, I got a big one already. And I'm sure they'll be happy with you two."
    iris @sadbrow happymouth "You two've been real nice to me today. You didn't call me a kid, or nothin'. And you listened to me when I told you about Rayquaza."
    iris @happy "I think Daddy would really like you two!"

    iris @closedbrow talking2mouth "That's important, because those eggs hatch into real ornery Pokémon. They might try ta bite you or somethin'. So it's real important to be nice to 'em."

    $ GetItem("Deino Egg")

    red @happy "Aw. Thanks, Iris. I really appreciate it."

    ethan @happymouth "Yeah, ditto."

    iris @happy "Thank you, Misters! Now, it's my bedtime. I'd better get back to Daddy before he blows a fuse!"
    
elif (NumEggs() == 0):
    iris @closedbrow talking2mouth "I think you two should take these."

    red @surprised "Huh?"

    iris @talkingmouth "I learned a lot during this egg hunt. And I'm not totally sure what to think. Grown-ups are more complicated than I thought."

    red @closedbrow talking2mouth "Uh... thanks?"

    iris @talking2mouth "Since you don't have any eggs, I think you should take this one. It'd be real bad if you went home on Springsday without any eggs."

    red @sadbrow happymouth "Aw. That's not... you don't have to worry about that."

    iris @happy "Daddy says that the people you should give the most help to are those who need it, not those who make it easiest."

    $ GetItem("Deino Egg")

    red @confused "Wise man."

iris @happy "I really hope I get to see you two again!"

red @closedbrow talking2mouth "Well, will I see you around the school?"

iris @sadbrow happymouth "Um... probably not. I should be flying back to Unova soon. But I'll ask Daddy if I can show up to more festivals like this!"

red @talkingmouth "Good luck."

iris @happy "Thank you! You too, you two!"

hide iris with dis

pause 1.0

ethan @thinking "[ellipses]"

red @closedbrow talking2mouth "Cute kid."

ethan @closedbrow talking2mouth "Yeah. Feels like the little sister I never had."

pause 1.0

red @confused "We should definitely make sure she gets back safely, right?"

ethan @talking2mouth "For sure. It's weird as hell that rampaging Pokémon got this far onto the school grounds."

red @closedbrow talking2mouth "Alright, let's go."

hide blank2
show mace at night, leftside
show face at night, rightside
with Dissolve(2.0)

queue music "audio/music/nuvema2_start.ogg" noloop
queue music "audio/music/nuvema2_loop.ogg"

pause 1.0

mace @talkingmouth "Well, that was an utter failure."

face @angry "Trounced by bunnies. On {i}Springsday.{/i} What a joke."

mace @angry "Are we meant to just give up, then? Accept [first_name]'s meteoric rise as inevitable?"

face @talkingmouth "Hmph. Perhaps we should focus our efforts on other beneficiaries of nepotism, like Blue Oak."

show cheren at night 
show mace surprisedbrow frownmouth
show face surprisedbrow frownmouth
with dis

cheren @sadmouth "Blue has done nothing wrong."

show face -surprisedbrow -frownmouth -surprised with dis

mace -surprisedbrow -frownmouth -surprised @angry "You! You're one of those cretins who ripped that Charmander from out of our hands!"

cheren @closedbrow talking2mouth "My efforts hardly contributed to that."

face @talkingmouth "Why should we take you at your word? You're doubtlessly a beneficiary of nepotism yourself!"

cheren @closedbrow talking2mouth "'Nepotism.'{w=0.5} You keep using that word.{w=0.5} ...Who recommended you to this school?"

mace @talkingmouth "Our parents, who are lauded alumni, and sit on the Board of Trustees!"

pause 1.0

cheren @closedbrow talking2mouth "You understand how that, in itself, is nepotism, right? You're no less guilty than [first_name]. Unless you have access to information I do not about his particular situation."

face @angry "Psh. Just look at him. He's a barely-literate fool who bungled--"

cheren @closedbrow talking2mouth "Bungled his way onto the Battle Team, yes, I know, I know. I've heard all these complaints before, from Blue."

mace @angry "Well, what are you doing here, then? Isn't it close to curfew?"

cheren @sad "...I am in desperate need of allies."

mace @surprised "What?"

cheren @closedbrow talking2mouth "Damn me for it, but I am confident there is something about [first_name] that is... unbeatable. That no fair play can overcome."
cheren @sad "If I could just prove to myself that I was wrong, I would accept that. But I've been unable to, as of yet."

face @talkingmouth "I don't see why we should care about your little political games. Your bleeding-heart liberal antics are of no concern to us."

cheren @angry "Are you blind? We have a common foe. [first_name]. In three weeks, he's practically charmed the entire school. If we don't do something, by the time the first Quarter Qlash is over with, he'll be the Dean of the Academy!"

pause 1.0

mace @angry "...Well, what's this {i}something{/i} you suggest?"

cheren @sadmouth "Find the truth. Then tell it."

pause 1.0

face @angry "Oh, {i}very{/i} clever, Cheren. Because truth is what wins politics. What a revolutionary strategy you have."

cheren @closedbrow talking2mouth "If I am right about the truth I believe is lying undercover, then... yes. It will win. But I need {i}your{/i} aid to find it."

cheren @angry "I do not like you. But you are possibly two of the three people in the entire school who do not like [first_name] [last_name]. So you're valuable."

mace @talkingmouth "...Go on."

cheren @closedbrow talking2mouth "{i}(Forgive me for this, [first_name]. But I must be sure.){/i}"

jump day010425
