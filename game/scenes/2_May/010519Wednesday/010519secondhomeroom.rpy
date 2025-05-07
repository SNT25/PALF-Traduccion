label secondhomeroom010519:

scene blank2 with splitfade

pause 1.0

stop music fadeout 1.5
queue music "audio/music/celebi_start.ogg" noloop
queue music "audio/music/celebi_loop.ogg"

scene homeroom 
show screen currentdate
show kris
with splitfade

kris @happy "Evening, class! One more day before the big test!"

redmind uniform @thinking "With the way she's hyping this up, either this test is going to be absolutely insane, or she's just {i}that{/i} desperate to get our grades up."

kris @sadbrow talkingmouth "I'm going to do everything I can to prepare you for this test, besides giving you the exact answer, so please pay attention."
kris @talkingmouth "Scope Lens. Razor Fang. Focus Energy. Night Slash."

hilbert uniform @closedbrow talkingmouth "{size=30}Two items. Two moves. What kind of game is this...?{/size}"

kris @talkingmouth "Which one of these is the odd one out? May?"

show may surprisedbrow frownmouth uniform with dis:
    xpos 0.25

may @talkingmouth "Eh?"
may -surprisedbrow -frownmouth -surprised @closedbrow sadmouth "Shoot, that's a tricky one. I'm going to say... the Scope Lens."

kris @talkingmouth "Okay. Could you elaborate on this, please?"

may @talkingmouth "Well, Focus Energy and Night Slash are Pokémon moves. And Razor Fangs are teeth dropped by a Pokémon."
may @talkingmouth "So those three are natural. But the Scope Lens is an item created by... {w=0.5}{size=30}um, not Devon...{/size} {w=0.5}Silph, I think."
may @talkingmouth "So the Scope Lens is the only man-made item or move in that list."

kris @happy "That's very clever, May! Professor Birch is always gushing about you, you know."

may @sadbrow talkingmouth "Aw. That's my Dad for you..."

kris @sadbrow talkingmouth "Now, I'm afraid that wasn't the answer I was {i}looking{/i} for, but it was still a correct one."
kris @happy "I'll give you a little extra participation credit for thinking outside of the box."

may @happy "Thanks, Professor!"

hide may with dis

kris @talkingmouth "Hm... [first_name], do you think you know what answer I was expecting?"

redmind uniform @thinking "Hm... well, it has to be..."

menu:
    "Scope Lens.":
        show kris sadbrow angrymouth with dis

        pause 1.0

        kris @talking2mouth "...Oh. Um, May just said that one, [first_name]."

        $ ValueChange("Kris", -1)

        kris -sadbrow -angrymouth @closedbrow talking2mouth "Try to pay a bit more attention, okay?"

        red @closedbrow talking2mouth "Sorry."
        
        kris @talkingmouth "The correct answer is the 'Razor Fang'. Everything I've mentioned increases your chances of landing critical hits in some way, except the Razor Fang, which has a chance to flinch the opponent.'"

    "Razor Fang.":
        kris @talkingmouth "Okay. And can you explain your reasoning?"

        red @happy "I hope so! Um, everything else increases your chance of landing critical hits, right? But the Razor Fang only gives your moves a chance to cause the opponent to flinch."

        $ ValueChange("Kris", 1, 0.5)

        kris @happy "That's exactly right. Well done, [first_name]."

    "Focus Energy.":
        kris @talkingmouth "Good guess, but not quite."
        
        kris @talkingmouth "The correct answer is the 'Razor Fang'. Everything I've mentioned increases your chances of landing critical hits in some way, except the Razor Fang, which has a chance to flinch the opponent.'"

    "Night Slash.":
        kris @talkingmouth "Good guess, but not quite."

        kris @talkingmouth "The correct answer is the 'Razor Fang'. Everything I've mentioned increases your chances of landing critical hits in some way, except the Razor Fang, which has a chance to flinch the opponent.'"

kris @talkingmouth "Now, remember what I said in class yesterday about critical hits? That you can guarantee a critical hit if you have three different sources boosting your critical hit ratio?"
kris @talkingmouth "Focus Energy actually counts as 'two' sources. The battle drug 'Dire Hit' does as well. So if you use a move with a high critical hit ratio, like Leaf Blade, after using a Dire Hit, it will be a guaranteed crit."

pause 0.5

kris @closedbrow talkingmouth "Let's see... the exact ratios for no crit stages, one crit stage, two crit stages, and three or more are..."
kris @talkingmouth "4.17%%, 12.5%%, 50%%, and of course, 100%%. You won't need to know these exact ratios for the test, though, but they're good to keep in mind."

show blank2 
hide kris
with splitfade

kris @talkingmouth "Now, let's move onto practical applications..."

narrator "Professor Cherry finishes the lecture, while you stare at the back of Blue's head, anticipating whatever weirdness is about to come."

$ PlaySound("BellChime.ogg")

kris @talkingmouth "I'll see you tomorrow. Enjoy the rest of your evenings. But not too much! You want to be well-rested for tomorrow's test!"

hide blank2 with splitfade

pause 1.0

red @surprisedbrow frownmouth "{i}Gulp.{/i}"

show blue kindeyebrows kindeyes smilemouth uniform with dis

pause 1.0

blue @neutralmouth "{size=30}Hey... dormie.{/size}"

pause 1.0

red @talking2mouth "What is happening, here?"

show blue:
    ypos 1.0 
    ease 0.5 zoom 1.2 ypos 1.1

blue @happy "We're... {w=0.5}{i}friends{/i}, right, pal?"

menu:
    "No.":
        pass

    "S-sure?":
        pass

blue @happy "G-great. That's awesome to hear. I'm {i}befriending{/i} you so hard right now."

pause 2.0

blue -kindeyebrows -kindeyes frownmouth @angrybrow angrymouth "I {i}said{/i}, I'm befriending you {i}so{/i} hard right now."

pause 1.0

blue @scaredeyes angryeyebrows furiousmouth "{size=50}I {i}said--{/i}{/size}"

red @surprisedbrow talking2mouth "Blue. Seriously. {i}What{/i} is going on?"

blue @closedbrow talking2mouth "...It's him."

$ sidemonnum = pokedexlookup("Eevee", DexMacros.Id)
$ PlaySound("pokemon/ball sound.ogg")
$ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))

pause 1.5

sidemon @talkingmouth "Eev."

pause 1.0

red @confused "What about him?"

blue @closedbrow embarrassedmouth "He's not changing. Nothing's changed. He isn't glowing, or changing type, or retching up kidney stones."

pause 1.0

blue @lightblush glancebrow wistfulmouth "And... you mentioned you thought those rocks were created out of your bond with other people, so... I thought if we... you know..."

pause 0.5

red @happy "You thought if we became closer friends, that your Eevee would throw up some [first_name] Foreverals?"

blue @closedbrow lightblush embarrassedmouth "That's how it works, right? That's just what you do."
blue @talkingmouth "You just walk up to people, have a conversation with them, maybe give them a gift, and then--"
blue @surprised "Huh?"
blue -frownmouth @happy "Oh, I got it! Here you go, {i}Friend.{/i}"

python:
    partyids = []
    for mon in playerparty:
        partyids.append(mon.Id)

    if (Item.SootheBell not in inventory):
        GetItem("Soothe Bell")

pause 1.0

red @closedbrow talking2mouth "A... Soothe Bell?"

blue @talkingmouth "I don't need that junk. My Pokémon respect me without some bell ringing 24/7. But it'd be perfect for you."

python:
    isgame = False
    disableinventory = False
    newpartyids = []
    for mon in playerparty:
        newpartyids.append(mon.Id)

if (newpartyids == partyids and not bellrung):
    red @confused "...What do I do with this?"

    blue @happy "Hah! Typical. Look, just go into your inventory and ring the damn thing."

    pause 3.0

    if (bellrung):
        jump afterringbell

    label ringbell:

    redmind @thinking "It looks like he actually expects me to ring the Soothe Bell right now..."

    if (bellrung):
        jump afterringbell

    blue @talkingmouth "Go on, then. See what it does."

    if (not bellrung):
        jump ringbell

    label afterringbell:

    red @talkingmouth "Nice, so I can evolve certain Pokémon with this... That's helpful. Thanks, Blue."

elif (newpartyids == partyids):
    red @talkingmouth "Nice, so I can evolve certain Pokémon with this... That's helpful. Thanks, Blue."

else:
    red @talkingmouth "Nice, my Pokémon evolved. That's helpful. Thanks, Blue."

blue @angrybrow neutralmouth "Yeah, wasn't that a great gift? We're really friendly now, right?!"

red @confused "I... I guess we're marginally more friendly than we were before?"

pause 1.0

red @confused "Wait, were you giving me this because you think gifting items to people is a way to make them like you..."

show blue surprisedbrow frownmouth with dis

red @confused "Or did you give it to me because you thought it would make {i}me{/i} friendlier, like my Pokémon?"

blue @talkingmouth "The first one, obviously."

pause 1.0

blue @closedbrow wistfulmouth "Unless, uh, it--"

red @unamusedbrow unamusedmouth "{w=0.5}.{w=0.5}.{w=0.5}."

hide blue
show forest3 at sepia
show deoxysblackeyes at sepia:
    xpos 0.10 xanchor 0.5 xzoom -1 ypos 1.2 zoom .8 yanchor 1.0
    parallel:
        linear 0.1 xpos 0.11
        linear 0.1 xpos 0.1
        pause 5.0
        linear 0.1 xpos 0.09
        linear 0.1 xpos 0.1
        pause 5.0
        repeat
    parallel:
        ease 2.0 ypos 1.2
        ease 2.0 ypos 1.23
        ease 2.0 ypos 1.2
        ease 2.0 ypos 1.17
        repeat
show blue surprisedbrow frownmouth at sepia:
    xpos 0.75 xzoom -1
show yellow surprisedbrow frownmouth tears at sepia:
    xpos 0.5 xzoom -1
show nate at sepia:
    xpos 0.3
show flashback
with dis

$ renpy.pause(1.0, hard=True)

pause 0.5

blue @kindeyes wistfulmouth "...I asked to dorm with you, [first_name]. Leaf and Ethan, too. And you, of course, Yellow."

pause 0.5

blue @sad2eyes wistfulmouth sadeyebrows "That's why Falkner... that's why."
blue @closedbrow talking2mouth "He said... no way. So I nagged him. Over and over and over. I thought... if we were forced to live together..."
blue @sad2eyes wistfulmouth sadeyebrows "...then maybe."

show blank with splitfade

hide forest3
hide deoxysblackeyes
hide blue
hide yellow
hide nate
hide flashback
hide blank 
show blue uniform frownmouth
with dis

pause 1.0

redmind @closedbrow frownmouth "...Is this him trying?"
redmind @closedbrow frownmouth "Well, at least he's not calling me a loser anymore, and demanding a battle every five seconds."

red @talking2mouth "Blue, you can't just give someone a gift and expect your Pokémon to make with the stones. I mean, I don't even know if your Eevee can do that."
red @confused "Just ask Professor Oak. It might be that your Eevee has a completely different power. Or just a bunch of rocks in its stomach. Either way, he could tell us."

pause 1.0

if (HasEvent("Blue", "MountainTalk")):
    blue @wistfulbrow wistfulmouth "{w=0.5}.{w=0.5}.{w=0.5}.I told you before. I don't want him to pay attention to me {i}just{/i} because of this Eevee."

else:
    blue @wistfulbrow wistfulmouth "I don't want him to pay attention to me {i}just{/i} because of this Eevee."

blue @closedbrow talkingmouth "If I figured out how to get him to work {i}before{/i} I talked to Gramps, then..."

pause 1.0

blue @closedbrow talkingmouth "Bah."
blue @talkingmouth "I don't know why I'm going to {i}you{/i} for advice. You tried to take the damn meteorite shard from me in the first place."
blue @angry "If it was up to you, I wouldn't even have the chance to {i}talk{/i} to gramps about this."

pause 0.5

show blue surprisedbrow frownmouth with dis

red @closedbrow talking2mouth "I... geez. I'm sorry."

blue @talkingmouth "What?"

show blue scaredbrow frownmouth with dis

red @sadbrow talkingmouth "That was wrong of me. There's no getting around that."
red @sad2eyes sadeyebrows talkingmouth "I was panicking. I'd {i}just{/i} talked with your grandpa about how I was going to afford Kobukan, and our plan relied on me being the only person who can make the Foreverals."
red @sad2eyes angryeyebrows talking2mouth "And... I guess maybe I was a little bit afraid that this shard would give you some kind of permanent, unassailable advantage over me."
red @closedbrow talking2mouth "I don't know. I had a lot of stuff going through my head, then. I was seriously pissed Monday morning, but..."

pause 1.0

red @happy "Well, right now, I kinda just want to know what your Eevee's power is. I guess my curiosity won out over my fear."
red @sadbrow talkingmouth "And for what it's worth, I {i}am{/i} sorry. Hope we can be cool about it? When you talk to Professor Oak, maybe we could compare notes on our Pokémon."

pause 2.0

red @sadeyebrows talking2mouth "Blue? You here?"
red @sadeyebrows talking2mouth "I don't want things to be weird between us. We're [bluecolor]dormmates{/color}, after all."

$ sidemonnum = pokedexlookup("Eevee", DexMacros.Id)
$ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))

sidemon @talkingmouth "{i}Hack!{/i} {i}Bleh!{/i} Eev."

narrator "A small handful of Foreverals drops, unceremoniously, at Blue's feet. His Eevee curls his tail around his feet, looking very proud of himself."

pause 1.0

show blue:
    ypos 1.0
    ease 0.3 ypos 1.2
    pause 0.5
    ease 0.3 ypos 1.0

narrator "Blue, without saying a word, scoops them up and pockets them."

hide blue with dis

narrator "And walks away."

pause 2.0

redmind @surprisedbrow frownmouth "Holy shit. Did he actually just get me? Did he {i}seriously{/i} get me with that?"

pause 1.0

redmind @happy "Fair play! I never saw that coming."

call freeroam from _call_freeroam_26

stop music fadeout 1.5

$ renpy.music.queue("Audio/Music/Cinnabar_Start.ogg", channel='music', loop=None, fadein=0.0, tight=None)
$ renpy.music.queue("Audio/Music/Cinnabar_Loop.ogg", channel='music', loop=True, tight=None)

$ removestudents = set()

scene suitenight
show leaf hatless
with splitfade

red @talkingmouth "Hey. Glad I caught you."

leaf @talking2mouth "Yeah, sorry, we haven't talked much, have we? I've been running all over the place trying to set up Dawn's birthday party."
leaf @closedbrow talking2mouth "I thought making it a low-key event would make it easier, but I'm seriously not used to it... God, I wish I could just rent out a club for a night."

red @happy "I'm sure Dawn will appreciate that you {i}didn't{/i} do that."

leaf @closedbrow talking2mouth "Yeah, well, she's a sweetheart. I'd die for her. Anyway, what's up, Skippy?"

red @talkingmouth "I was just thinking about what I should get Dawn as a present."

leaf @happy "Aw. That's so sweet."

red @talkingmouth sweat "Problem is, I'm a bit low on cash."

leaf @talkingmouth "Oh, I'll cover you."

red @happy "I know you would. But I want it to be something meaningful, something that actually seems like it might come from me. Do you have any ideas?"

leaf @closedbrow frownmouth "Hmm..."
leaf @talking2mouth "How are you at cooking?"

red @talkingmouth "Decent enough, out of necessity."

leaf @talkingmouth "Great. I don't have a cake planned. I was originally going to commission one from May, but apparently she's backed up so much, she has {i}negative{/i} commission slots."
leaf @closedbrow talkingmouth "And she said that Lisia is {i}literally{/i} chasing her down over some contest club mishap involving pyrotechnics, so that's also interfering."

red @confused "She's joking, right?"

leaf @talkingmouth "I've never known May to use the word 'literally' figuratively."

red @closedbrow talking2mouth "Alright, I'll see what I can figure out. Maybe I'll talk to May, just for advice about this cake."

leaf @talking2mouth "Good idea."

red @happy "Going to bed now. Don't stay up too late!"

leaf @sadbrow talkingmouth "It's amazing how little control I have over that. When I start to obsess over something... I can't sleep."
leaf @happy "Anyway, goodnight!"

call texting from _call_texting_21 

jump day010520