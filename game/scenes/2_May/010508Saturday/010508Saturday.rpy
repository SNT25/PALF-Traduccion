label day010508:

$ HealParty()
$ libtypes = []

call calendar(1) from _call_calendar_33
$ calDate = calDate.replace(day=8, month=5, year=2004)

$ timeOfDay = "Morning"
show morning at vspaz

pause 3.5

queue music "audio/music/power plant_start.ogg" noloop fadein 1.0
queue music "audio/music/power plant_loop.ogg"

scene research 
show screen currentdate
show sonia
with splitfade

sonia @talking2mouth "Extinct."

red @confusedeyebrows talkingmouth "Extinct?"

sonia @talking2mouth "That's right."
sonia @sadbrow talking2mouth "I'm sorry. I wish I could tell you more about it. But my specialties are Galarian myth-history, and astrobiology."
sonia @sadbrow happymouth "And, er, your Pikachu doesn't quite appear to be from Galar. Or space."
sonia @talking2mouth "They were a Unovan regional variant of Pikachu, though. It was called Pikachu's 'Liberation Form.' The first president of Unova famously had one."

red @talkingmouth "But if the species has been extinct for hundreds of years, then... how did [pika_name] turn into it?"

show oak at leftside with dis:
    xpos 0.33

show sonia:
    ease 0.5 xpos 0.66

oak @talking2mouth "My tests so far are coming up with a simple conclusion."

pause 2.0

sonia @confused "Go on, then."

oak @closedbrow talkingmouth "This did {i}not{/i} appear to be a case of evolution. This seems to be a form change, of the kind that other Pokémon such as Castform or Darmanitan have exhibited."
oak @talkingmouth "I propose we dub this new form change 'Liberization', in reference to your Pikachu's historical roots.'"

red @closedbrow talking2mouth "Huh... I thought so. It looks too similar to a Pikachu to be a full evolution."
red @talkingmouth "Those Pokémon usually revert back when battle is over, though."

show oak:
    ease 0.5 xpos 0.25

show sonia:
    ease 0.5 xpos 0.75

show libpikachu with dis:
    xpos 0.45 ypos 0.72

pause 1.0

red @closedbrow talking2mouth "I guess he does look {i}kinda{/i} different outside of battle..."

show blank

pause 0.1

hide blank

$ PlaySound("pokemon/pikachu_happy3.ogg")

show oak surprisedbrow frownmouth
show sonia surprisedbrow frownmouth
with dis

libpikachu glowing angryeyes happymouth sparks "Pi-kerachu!"

pause 2.0

show libpikachu happybrow -happymouth -glowing -sparks with dis

oak @closedbrow talkingmouth "Seems this transformation does not require an immediate threat to take on his enhanced form, then."

sonia @talking2mouth "Or perhaps it transforms when it sees a real threat worth fighting, and then that form just stays?"

oak @surprisedbrow surprisedmouth "Why... yes, of course! The legendary beasts of Galar were said to take on a stronger form when the moment called for it, weren't they?"

sonia -surprisedbrow -frownmouth -surprised @closedbrow talking2mouth "Yes. Their 'Crowned' forms were--"

$ PlaySound("pokemon/pikachu_angry3.ogg")

libpikachu -happybrow frownmouth @angry "Pika!"

red @surprised "Woah. What's wrong, Pikachu?"

$ PlaySound("pokemon/pikachu_angry1.ogg")

libpikachu poutmouth @angrybrow angrymouth "Pikera... chu."

oak -surprisedbrow -frownmouth -surprised @closedbrow talkingmouth "Hm... he seemed to react negatively when you mentioned the scientific classification of Zacian and Zamazenta's forms... perhaps that has some connection to this ability of his, whatever it might be."

red @talkingmouth "Right. I'm glad that we're, uh, thinking about figuring out what he is, now, but the main reason I brought him in was because I was worried about those shards of rock in his stomach?"

oak @surprised "Oh! That was the entire reason I ran these tests."
oak @angrybrow talking2mouth "Lad, they're entirely gone. They seem to have been consumed by [pika_name] as a fuel for his evolution." 
oak @talkingmouth "His stomach is empty--quite empty, in fact. I might recommend upping the amount of food you give him."

red @confusedeyebrows talking2mouth "Did he pay you to say that?"

$ PlaySound("pokemon/pikachu_norm1.ogg")

libpikachu -poutmouth @playfuleyes playfulmouth "Pikera."

oak @talkingmouth "In any case, since we don't know anything about what [pika_name] is, or what he might have become, I strongly recommend you keep him by your side at all times so as to keep an eye on him."

red @happy "Of course. That's what I do anyway."

pause 1.0

red @closedbrow talking2mouth "Hey... Professor Oak?"

oak @talkingmouth "Yes, lad?"

red @confused "Where did you get [pika_name] from? I always figured you caught him in Viridian Forest, but I'm guessing that's not the case anymore."

oak @surprised "Oh!" 
oak @happy "Ohohoho. No, not at all, lad. This Pikachu was given to me by a former student named Brock. Not a student here, you understand, but I taught him much of what he knows."

red @closedbrow talking2mouth "Hm. Do you know where Brock caught this Pikachu?"

show libpikachu closedeyes frownmouth with dis

oak @closedbrow talking2mouth "I'm afraid not. But I assume it was somewhere here in Kobukan--Brock sent it back to me shortly after he left Kanto for Kobukan."

red @talkingmouth "Do you know how I could get in contact with this 'Brock'?"

show libpikachu surprisedeyes surprised2mouth with dis

sonia @happy "Ooh! I know this one. He works in the nursing department. As a volunteer, I think. He was here last year, as well."

red @closedbrow talking2mouth "Huh. I'll have to drop by and talk to him, then."

pause 1.0

show libpikachu dizzyeyes surprisedmouth with dis

red @happy "Later, though. I think [pika_name] and I have earned a break. I'm planning on just spending this weekend chilling out. Maybe catch up on some homework I missed."

red @happy "Isn't that right, [pika_name]?"

show oak surprisedbrow frownmouth
show sonia surprisedbrow frownmouth
with dis

show libpikachu:
    ease 0.3 ypos 1.5 rotate 90

pause 0.3

show research with vpunch

red @surprised "[pika_name]?! Are you okay? What's--what's happening?"

hide libpikachu

narrator "[pika_name] is hacking, coughing, and retching, as though he's trying to throw up a hairball."

red @sad "Wait, buddy, are you--"

narrator "Suddenly, a large clump of...{w=0.5} {i}something{/i} falls out of his mouth."

$ PlaySound("pokemon/pikachu_angry1.ogg")

libpikachu @angryeyes talking2mouth "Pika!"

narrator "Inspecting the pile closer, it appears... that they are... gems?"

show foreverals at itemhover

$ PlaySound("item_get.ogg")

pause 2.0

show foreverals at itemhide
$ renpy.pause(1.5, hard=True)

hide foreverals

pause 1.0

red @confused "Sam? I thought you said that his stomach was empty."

oak @surprisedbrow talking2mouth "It certainly was. What are..."

show oak: 
    ease 0.5 ypos 1.2 zoom 1.3

oak @talkingmouth "Good lord! Emeras, my boy!"

oak @talkingmouth "Quickly, we need to get them into a containment unit!"

show foreverals:
    alpha 0.0 xpos 700 ypos 300 zoom 0.75 rotate 0
    pause 0.5
    parallel:
        ease 0.25 rotate 360
        ease 0.25 rotate 0
        repeat
    parallel:
        ease 0.3 xpos 600 ypos 100 zoom 0.5
        ease 0.5 xpos 550 ypos 700 zoom 0.1
    parallel:
        ease 0.15 alpha 1.0
    parallel:
        pause 0.55
        ease 0.25 alpha 0.0

pause 1.5

show oak:
    ease 0.3 xpos 0.1 alpha 0.0 ypos 1.0 zoom 1.0

narrator "Professor Oak snatches the gems from your hand and quickly runs off to the back of the laboratory."

pause 1.0

show sonia:
    ease 0.5 xpos 0.5

red @confused "Emeras?"

sonia -surprisedbrow -frownmouth -surprised @talking2mouth "A type of gem."
sonia @talking2mouth "They're not usually seen in a solid form like that, though."
sonia @closedbrow talkingmouth "Most of the time, they're just a dusty powder."
sonia @talking2mouth "Emeras exist in a wholly unstable state--even attempts in laboratories to solidify their structure haven't managed to produce anything that stays stable for more than 10 minutes."
sonia @closedbrow talkingmouth "They can only coalesce in an environment saturated with Mysteriosity."

red @talkingmouth "Mysteriosity?"

sonia @closedbrow talkingmouth "A natural phenomenon that certain wild locations seem to exhibit. Woods, caves, oceans." 
sonia @talking2mouth "We don't know much about it, though. Anytime humans move into an area with Mysteriosity, the Mysteriosity fades in a matter of days."

red @closedbrow frownmouth "Hm."
red @talkingmouth "So unless Professor Oak can get those gems into a wood, or a big cave, without being there, they'll just break apart in a couple minutes."

sonia @talking2mouth "That's the sum of it. The Wishing Stars of Galar do a similar thing when taken too far from Eternatus, actually."
sonia @sadbrow talkingmouth "Of course... Eternatus is pretty big... so its effect is equal over the entire planet, largely."

red @confused "I guess that makes sense. What I'm not sure of is... hey, [pika_name]? How did those end up in your stomach?"

$ PlaySound("pokemon/pikachu_sad.ogg")

libpikachu @dizzyeyes surprisedmouth "Pika...?"

red @happy "Guess you don't know, huh?"

pause 2.0

narrator "You and Sonia make small talk for a couple of hours before Professor Oak returns."

hide oak

pause 1.0

show oak:
    xpos 0.33

show sonia:
    ease 0.5 xpos 0.66

oak @talkingmouth "I have a theory."

narrator "Professor Oak holds out his hand, and the gems are still there, whole and unblemished."

sonia @surprised "What?"

oak @closedbrow talkingmouth "I believe that the meteorite was not consumed entirely by [pika_name]'s transformation."
oak @talking2mouth "Rather, I believe that he still has a tremendous amount of energy within him."
oak @closedbrow talkingmouth "We have seen how [pika_name]'s distinctive tail has grown larger from the transformation, and the starburst patterns on his cheeks certainly evoke the idea of energy 'exploding' out of him."

pause 1.0

oak @talkingmouth "However, that only explains how he might vent the excess energy from the meteorite's shards."
oak @closedbrow talkingmouth "The 'matter' in question is still unaccounted for."
oak @talking2mouth "Ergo, my theory is that the matter has crystallized into this... Emera-like form."

pause 1.0

oak @closedbrow talkingmouth "As these are not Emeras, and merely resemble them strongly, I suggest a new name." 
oak @talkingmouth "While Emeras were named after their ephemeral nature, it would do to name these new gems after their permanency."
oak @closedbrow talkingmouth "May I suggest, perhaps, 'Foreveralds?'"
oak @happy "As a portmanteau of 'forever' and 'emerald', I find it quite clever!"

sonia @closedbrow talkingmouth "...It sounds like you're saying 'forever old', though."

oak @surprised "Oh."
oak @closedbrow talking2mouth "Yes, I suppose that's right. Cut the 'd', then. 'Foreverals' sounds like an attractive enough title for my next paper."

red @talkingmouth "Okay."

pause 1.0

red @closedbrow talking2mouth "Um... should we get [pika_name] some tummy medication, then?"

oak @surprised "Lad? I don't think you understand just what a monumental occurrence this is for science!"

red @happy "No, I definitely don't."

oak @talkingmouth "[pika_name] has not only managed to--somehow--transform into a member of an extinct species, but has also managed to metastasize whole, stable Emera-like gems within his own body."
oak @closedbrow talkingmouth "I cannot {i}begin{/i} to describe how extraordinary this is. His gut flora must be fascinating."

red @talkingmouth "Cool. And... what, exactly... should I do?"

oak @closedbrow talking2mouth "Well, your admission to Blueberry Academy is quite off the table, now. You simply {i}must{/i} stay here for observation."

redmind @sadbrow frownmouth "So... the same deal as before, then?"

oak @talkingmouth "In any case, it seems your issues with your classmates should be resolved now. I saw your speech. Quite well-put. I can't imagine anyone should have any problems with you after that."

redmind @sadbrow frownmouth "Oh, Sam..."

oak @closedbrow talking2mouth "For now, I might suggest that you take these Foreverals and take good care of them."

red @surprised "Really? You don't want to run tests on them?"

oak @talkingmouth "I certainly do, and I'd appreciate if you drop in, often, such that I may run more. But you {i}did{/i} say that you wanted today to be a day of relaxation. And I've run a decent number of tests already."
oak @closedbrow talkingmouth "My understanding is that these Foreverals are attuned to a certain kind of Pokémon. If you were to give these Foreverals to a Pokémon, that Pokémon should have its abilities enhanced."
oak @closedbrow talking2mouth "I do not understand what rhyme or reason there is to it." 
oak @talking2mouth "It seems to enhance a Pokémon by altering its DNA, similar to an evolutionary stone, but the changes seem to be {i}based on{/i} something no less arbitrary than the Pokémon's wishes."
oak @talkingmouth "Nevertheless, I am certain some sort of practical battle application can be found for this."

red @confused "Oh, like an item?"

oak @talkingmouth "Partially. But as this is uncharted territory, and these gems are {i}quite{/i} small, I can't imagine there's any harm in giving a Pokémon both an item {i}and{/i} a Foreveral."

red @happy "Oh, awesome!"

oak @talkingmouth "There's one more thing. [pika_name], as the source of these Foreverals, seems as though he could be compatible with {i}any{/i} Foreveral, or possibly even combinations of Foreverals."
oak @closedbrow talking2mouth "However, in order to avoid over-taxing his system before we know what he's capable of, and better understand the nature of Foreverals, I might recommend you give him only one at a time for now."

red @closedbrow talking2mouth "Okay."

narrator "[bluecolor]You now have access to Foreverals!{/color}"

python:
    usingforeverals = True
    added = UpdateForeverals()
    for key, value in added.items():
        if (len(value) == 3):
            fvl1, fvl2, fvl3 = value
            renpy.say(None, "Your bond with {} earned you the {}, {}, and {}!".format(key, fvl1, fvl2, fvl3))
        elif (len(value) == 6):
            fvl1, fvl2, fvl3, fvl4, fvl5, fvl6 = value
            renpy.say(None, "Your bond with {} earned you the {}, {}, {}, {}, {}, and {}!!".format(key, fvl1, fvl2, fvl3, fvl4, fvl5, fvl6))
        elif (len(value) == 9):
            fvl1, fvl2, fvl3, fvl4, fvl5, fvl6, fvl7, fvl8, fvl9 = value
            renpy.say(None, "Your bond with {} earned you the {}, {}, {}, {}, {}, {}, {}, {}, and {}!!!".format(key, fvl1, fvl2, fvl3, fvl4, fvl5, fvl6, fvl7, fvl8, fvl9))
        elif (len(value) == 12):
            fvl1, fvl2, fvl3, fvl4, fvl5, fvl6, fvl7, fvl8, fvl9, fvl10, fvl11, fvl12 = value
            renpy.say(None, "Your bond with {} earned you the {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, and {}!!!!".format(key, fvl1, fvl2, fvl3, fvl4, fvl5, fvl6, fvl7, fvl8, fvl9, fvl10, fvl11, fvl12))
        elif (len(value) == 15):
            fvl1, fvl2, fvl3, fvl4, fvl5, fvl6, fvl7, fvl8, fvl9, fvl10, fvl11, fvl12, fvl13, fvl14, fvl15 = value
            renpy.say(None, "Your bond with {} earned you the {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, and {}!!!!!".format(key, fvl1, fvl2, fvl3, fvl4, fvl5, fvl6, fvl7, fvl8, fvl9, fvl10, fvl11, fvl12, fvl13, fvl14, fvl15))

if (len(claimedforeverals) > 0):
    narrator "[bluecolor]The mechanics of these will be explained shortly... but for now, why don't you experiment?{/color}"

else:
    narrator "However, none of the Foreverals [pika_name] disgorged seem to be in a usable state..."

pause 2.0

oak @talkingmouth "What a mystery... Liberization and Foreverals."
oak @happy "Perhaps it is a good thing my Frienergy research has hit a dead end. You're definitely giving me enough to focus on for now, Lad!"

stop music fadeout 1.5

pause 1.0

oak @sweat closedbrow talking2mouth "Of course... Pokémon-human Psychosociology is my field of study, not so much any of this..."

$ renpy.music.set_volume(0.1)
play music "audio/music/imminence_start.ogg" fadein 10.0 noloop
queue music "audio/music/imminence_loop.ogg"

oak @closedbrow talkingmouth "It {i}really{/i} might be time to call in an expert.{w=1.0} Someone who knows the ins and outs of battle, a peerless researcher and historian...{w=1.0} perhaps even an archeologist..."

pause 3.0

stop music
$ renpy.music.set_volume(1.0)
queue music "audio/music/power plant_start.ogg" noloop fadein 1.0
queue music "audio/music/power plant_loop.ogg"

oak @closedbrow talkingmouth "Well, I can think of a few options I may want to reach out to."

oak @happy "For now, Lad, please--just enjoy your weekend!"

call clearscreens from _call_clearscreens_127
scene blank2 with splitfade

pause 2.0

call freeroam from _call_freeroam_15

hide red
hide yellow

show suitenight 
show yellow
show screen currentdate
with splitfade

show screen songsplash("Viridian Forest", "Zame")
stop music fadeout 1.5

queue music "audio/music/viridianforestgentle_start.ogg" noloop
queue music "audio/music/viridianforestgentle_loop.ogg"

redmind @thinking "Man. I'm tired. Can't wait to get into bed and conk out for the day..."

$ PlaySound("pokemon/pikachu_sad.ogg") 
libpikachu closedeyes playfulmouth "Pikaaa..."

show yellow surprisedbrow with dis

red @happy "Hey, 'night, Yellow. Sorry I haven't really properly introduced myself yet. Let's do something next week, alright?"

yellow @sadbrow talkingmouth "Um... we {i}have{/i} met, though."

red @confused "Hm? Well, yeah, I mean, when I landed in the garden with Tia, I kinda said 'hi', but when I moved in with my last group of roommates, we did a whole bunch of stuff together."
red @happy "I just mean we should do something like that. Maybe next week?"

yellow @sadbrow happymouth "Oh... okay. Hah hah."

pause 1.0

yellow @surprised "Wait, what are those?"

red @confused "Hm?"

narrator "You follow Yellow's gaze and see that [pika_name] is holding a pawful of new Foreverals. They seem small and misshapen, though."

red @happy "Oh! Those are one of Professor Oak's new discoveries. {w=0.5}(Sort of.) They're called Foreverals. They do some crazy stuff."

show yellow:
    ease 0.5 ypos 1.2 zoom 1.3

yellow @talkingmouth "May I?"

red @talkingmouth "Go ahead."

show yellow closedbrow frownmouth with dis

narrator "Yellow examines the Foreverals closely, turning them over in her hands. You think you see a small yellow glow emanating from Yellow's hands... but surely that's a trick of the light."

yellow -closedbrow -frownmouth @talkingmouth "I really like these. They feel... friendly. If you get any more, would you let me see them?"

red @happy "Sure! Heck, keep those ones. I don't think I could use them, anyway."

$ numforeverals = len(foreveralinv)

if (numforeverals > 0):
    red @talkingmouth "Actually, I've got a bunch of them here with me..."

    show blank2 with splitfade

    narrator "You share your Foreverals with Yellow."

    if (numforeverals > 20):
        $ ValueChange("Yellow", 10, 0.5, changemood=False)
        $ ValueChange("Yellow", numforeverals - 20, 0.5, changemood=False)
        $ ValueChange("Yellow", 10, 0.5, changemood=False)
    elif (numforeverals > 10):
        $ ValueChange("Yellow", 10, 0.5, changemood=False)
        $ ValueChange("Yellow", numforeverals - 10, 0.5, changemood=False)
    else:
        $ ValueChange("Yellow", numforeverals, 0.5, changemood=False)

yellow @talkingmouth "Thank you very much! I'll take a good look at these and see if I can figure something out."

red @surprised "Huh, do you have experience with these kinds of things?"

yellow @happy "I don't even know what kind of thing this is, yet. So maybe!"

red @happy "Fair enough. Now, I'm going to bed."

call texting from _call_texting_13

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_128

show blank2 with dis
    
$ renpy.pause(2.5, hard=True)

jump day010509