label flyingelective:

$ renpy.transition(dissolve)
show screen currentdate

scene map
show blank2:
    alpha 0.8

show classroom with dis

show flytype:
    alpha 0.0 xalign 0.5 yalign 1.0
    ease 0.5 alpha 1.0

$ location = "flying"
$ passedclass = False

############################################################################################################################################################################################################################
#### 13. FLYING      #######################################################################################################################################################################################################
############################################################################################################################################################################################################################
$ renpy.pause(1.0, hard=True)

call skylaevent from _call_skylaevent
call ethanevent from _call_ethanevent_7
call grushaevent from _call_grushaevent

label afterflyingsetup:

if (HasEvent("Instructor Winona", 2.1)):
    menu:
        "{b}>General Studies{/b}":
            pass

        ">Ask for move tutoring":
            jump movetutorflying

        ">Craft items" if (HasEvent("Instructor Winona", 3.1)):
            jump itemcraftflying

if (not HasEvent("Instructor Winona", 1)): #first class
    $ AddEvent("Instructor Winona", 1)
    $ renpy.pause(1.0, hard=True)

    show blue uniform at rightside with dis
    
    redmind uniform @sad "Ugh, he's here, then? I guess it makes sense... he always did like his flying types..."

    hide blue at rightside with dis

    pause 1.0

    show calem uniform with dis

    red @talkingmouth "Yo, Calem!"    
    calem @talkingmouth "Oh, [first_name] and Ethan. Fancy seeing you two here."
    calem happy "Better take a seat. The teacher's coming in."
        
    red @talkingmouth "Don't mind if I do."
    
    hide calem with dis

    pause 1.0

    show winona with dis

    winona @talking2mouth "{i}*Ahem!*{/i} Hello, students."        
    winona @talking2mouth "Let's get this class started without, um, further ado!"

    hide winona with dis
        
    $ renpy.pause(0.5, hard=True)

    show winonabg with dis

    if (not IsDate(5, 4, 2004)):
        winona @surprised "Oh! It looks like we've got some new students. Well, then..."

    winona @happy "First off, let me welcome you to your first {color=#0048ff}Flying-type class{/color} of the school year!"
    winona @talkingmouth "I'm sure that you're going to learn a lot! Probably!"

    pause 1.5

    winona @closedbrow talking2mouth"{size=28}{i}Um... let's see...{w=0.5} Maybe we should all introduce ourselves?{/i}{/size}"
    
    $ BecomeNamed("Instructor Winona")
    
    winona @talkingmouth "I am Winona, your instructor for this year."
    winona @talking2mouth "I'd like to make clear that, um, this is my first year teaching. I'll strive to do my best to educate you in a way befitting Kobukan Academy."
    winona @closedbrow talking2mouth "But, um... If I start to veer off-course, I trust that you'll give me a heads-up."

    blue angry uniform "{size=30}Great. We've got a complete newbie for a teacher.{/size}"

    pause 1.0

    winona @talkingmouth "Okay, so... Let's begin the lesson!"
    winona @closedbrow talkingmouth "Let me start off with some basic background on Flying-type Pokémon."
    winona @talking2mouth "It all started more then half a billion years ago, when the first Bug Pokémon appeared on Earth..."

    ethan uniform "Basic background, huh? Sounds to me like we're digging real deep in there."
    red @talkingmouth "Huh? Looks like Skyla's on her phone... I guess I can't blame her.{w=0.5} This isn't exactly the most exciting way to start off a class."

    window hide

    image note1 = "GFX/Note1.webp"
    image note2 = "GFX/Note2.webp"

    $ renpy.music.set_volume(0.1, delay=0.5, channel="music")
    $ renpy.music.play("Audio/Music/Sentai snippet.ogg", channel="XYgame", loop=None, fadeout=0.5)

    $ renpy.pause(3.0, hard=True)

    skyla uniform @surprised "Eep!"

    show skylaintro:
        subpixel True
        alpha 0.0 xalign 0.5 yalign 1.0 zoom 1.0
        parallel:
            ease 1.25 alpha 1.0
        parallel:
            ease 5.0 xalign 0.7 zoom 0.75

    show note1 as note1A:
        alpha 0.0 xpos 980 ypos 650
        parallel:
            ease 0.2 alpha 1.0
            pause 0.3
            ease 0.2 alpha 0.0
            pause 0.3
            repeat
        parallel:
            ease 1.0 xpos 450 ypos 550
            ease 0.0 xpos 980 ypos 650
            repeat

    show note1 as note1B:
        alpha 0.0 xpos 1000 ypos 700
        parallel:
            ease 0.2 alpha 1.0
            pause 0.1
            ease 0.2 alpha 0.0
            pause 0.1
            repeat
        parallel:
            ease 0.6 xpos 480 ypos 450
            ease 0.0 xpos 1000 ypos 700
            repeat

    show note1 as note1C:
        alpha 0.0 xpos 990 ypos 670
        parallel:
            ease 0.22 alpha 1.0
            pause 0.15
            ease 0.22 alpha 0.0
            pause 0.15
            repeat
        parallel:
            ease 0.74 xpos 500 ypos 600
            ease 0.0 xpos 990 ypos 670
            repeat

    show note2 as note2A:
        alpha 0.0 xpos 970 ypos 660
        parallel:
            ease 0.1 alpha 1.0
            pause 0.25
            ease 0.1 alpha 0.0
            pause 0.25
            repeat
        parallel:
            ease 0.7 xpos 510 ypos 620
            ease 0.0 xpos 970 ypos 660
            repeat

    show note2 as note2B:
        alpha 0.0 xpos 970 ypos 700
        parallel:
            ease 0.25 alpha 1.0
            pause 0.3
            ease 0.25 alpha 0.0
            pause 0.3
            repeat
        parallel:
            ease 1.1 xpos 460 ypos 520
            ease 0.0 xpos 1000 ypos 700
            repeat

    ethan @talking2mouth "Ooh, left her phone on in class? Rookie mistake."

    winona @surprised "Oh, I forgot to mention.{w=0.5} Please turn off your cellphones in this class."
    winona @sad "...If that's okay with you, I mean! If you really, really, can't bear to part with it, could you at least put it in silent mode? Maybe?"

    skyla uniform @sad "R-right! I mean, duh!{w=0.5} It's common courtesy!"

    show note1 as note1A:
        ease 0.5 alpha 0.0
    show note1 as note1B:
        ease 0.5 alpha 0.0
    show note1 as note1C:
        ease 0.5 alpha 0.0
    show note2 as note2A:
        ease 0.5 alpha 0.0
    show note2 as note2B:
        ease 0.5 alpha 0.0

    $ renpy.music.stop(channel="XYgame", fadeout=0.5)
    $ renpy.music.set_volume(1.0, delay=0.5, channel="music")

    window hide
    pause 1.0

    hide note1 as note1A
    hide note1 as note1B
    hide note1 as note1C
    hide note2 as note2A
    hide note2 as note2B

    skyla @sweat sadbrow happymouth "The nerve of some people, heh! Heh...{w=1.0} .{w=0.25}.{w=0.25}.Heh?"

    red happy "So, I guess you like Pokémon Rangers?"

    skyla @surprised "{size=28}{i}Shhh! N-not so loud!{/i}{/size}"

    red -happy @talkingmouth "Hey, I'm not judging, I think it's cool that you like that show."

    show skylaintro:
        alpha 1.0
        ease 1.0 alpha 0.0

    $ renpy.pause(1.0, hard=True)
    
    show skyla uniform with dis:
        xpos 850 ypos 1.1 zoom 1.3
        ease 1.0 xpos 900

    $ renpy.pause(1.0, hard=True)
        
    skyla surprised "Wait, really?{w=0.5} You don't think it's lame?"
    red @talkingmouth "Skyla, you're a pilot. Everything you do is cool by default. You could be into freakin' {i}My Little Ponyta{/i}, and it'd be cool."
    skyla "[ellipses]"
    red confusedeyebrows "Wait, are you?"

    pause 2.0

    skyla closedbrow angrymouth "I like cartoons, okay! 'Adult' TV is so depressing!"
    red happy "Well, I don't watch TV, so I'll take your word for it."
    show skyla frownmouth with dis

    window hide

    pause 1.0
    
    show skyla:
        
        xpos 900 ypos 1.1
        ease 1.0 xpos 800
        pause 1.0
        ease 0.5 xpos 900

    pause 2.5

    show skyla sad:
        xpos 900 ypos 1.1

    skyla "...Hey, would you mind not telling anybody about this?"
    skyla @closedbrow frownmouth "It's kind of embarrassing..."

    red @talkingmouth "Of course. Your secret's safe with me."

    skyla happy "Thanks!"

    show skyla at dissolveaway:
        xpos 900 ypos 1.1

    pause 2.0

    hide calem

    winona @closedbrow talking2mouth "...And that's when we believe Flying Pokémon were born, long after the birth of Arceus.{w=0.5}"
    winona @talkingmouth "Do you have any questions so far?"

    pause 1.0

    show calem uniform:
        xpos 500 alpha 0.0 zoom 1.0
        ease 0.5 alpha 1.0

    pause 1.0

    if (IsDate(5, 4, 2004)):
        winona "Yes? Um... I don't think I caught your name...?"

        calem @talkingmouth "It's Calem, miss."

    winona @talking2mouth "Go ahead, Calem."

    calem @closedbrow talking2mouth "Isn't Rayquaza the ancestor of Flying Pokémon?{w=0.5} Like how Water and Ground Pokémon came from Kyogre and Groudon, respectively."
    calem @talkingmouth "Rayquaza created the sky, and all the Pokémon that came with it were a byproduct, right?"

    winona @happy "Ah, that is a common misconception."
    winona @talkingmouth "It's true that the ancient Hoenn legends are the guardians of the natural elements, but they did not take part in creating its inhabitants."
    winona @talkingmouth "Pokémon evolved and transformed over countless eons in order to adapt to their environment."
    winona @closedbrow talking2mouth "Rayquaza may be the oldest living Flying-type, but like I've mentioned, we can trace them back to Bug-types and Ground-types. Even back to Arceus, the creator, if you go far enough!"

    winona @talking2mouth "However, while Arceus created Pokémon, the Pokémon themselves only heed those that rule their domain.{w=0.5} Much like how you all follow your parents' rules directly and not necessarily the rules set by the government."

    calem "I see."

    winona @happy "Does that explain it?"

    calem  happymouth "Yes, with that analogy, it's much easier to understand. Thank you."

    winona @talking2mouth "You're welcome."

    hide calem with dis

    winona @talking2mouth "If there are no other questions, I'll continue."
    winona @flirtbrow talkingmouth "And for all those sleeping in the back, this material will be on future tests, so pay attention!"

    ethan happy "Eh, wasn't a strong start, but I think I'll enjoy this class!"
    ethan closedbrow talking2mouth "Although my grandma would flip her lid if she knew Kobukan was teaching Arceism..."

    winona @closedbrow poutmouth "{size=30}{i}Phew.{/i}{/size}"
    winona @talkingmouth "That's all the time we have today. Remember to preview the material for our next class!"

    hide winona
elif (not HasEvent("Instructor Winona", 2.1) and classstats["Flying"] >= 10):#Wing It
    show winona with dis
    if (not HasEvent("Instructor Winona", 2)):
        $ renpy.pause(1.0, hard=True)

        hide winona 
        show winonabg
        with dis

        narrator "Instructor Winona is reading out of a textbook to a class that is clearly not engaged with the material, when..."

        winona "...and that's why the formation of the Flying-type's wing is..."

        pause 1.0

        red uniform @surprised "Hm? She just... she just stopped."

        red @talkingmouth "Instructor Winona?"

        winona "...This isn't working, is it?"

        red @closedbrow talking2mouth "What do you mean?"

        winona "Well, I'm doing what I 'should.' As a teacher, I mean. I'm teaching you the material, I'm telling you the answers to the tests..."

        winona "B-But... you're clearly bored out of your minds!"

        redmind @thinking "Well, I'm glad I didn't have to say it."

        hide winonabg
        show winona
        with dis

        winona @talkingmouth "So I think I'm going to change up the lesson plan a little. I'm going to {i}wing it.{/i}"
        winona @closedbrow talking2mouth "You--sorry, I'm bad with names."

        red @talkingmouth "That's alright. It's [first_name]."

        winona @talking2mouth "Right, [first_name]. Why don't we have a one-on-one battle? That'll liven up the class, and I think you're about ready for your advancement exam, anyway."
        winona @happy "If you pass, I'll even teach you the special aerial technique 'Wing It.'"

        red @surprised "I haven't heard of that one. What does it do?"

        winona @talkingmouth "It will sharply increase a random stat of yours, while decreasing another. If you're in a comfortable position, it's a good, if risky, way to solidify that."

        red @closedbrow talking2mouth "Wow. Yeah, I can see how that would be useful. Okay! I'm ready to go!"

        $ AddEvent("Instructor Winona", 2)
    else:
        red uniform @talking2mouth "Instructor Winona, I'm ready to try the advancement exam again. Will you let me?"

    winona @talkingmouth "Of course. This will be a standard one-on-one battle. {color=#0048ff}Bring a Flying-type for your best odds of victory.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    winona @happy "No books, no rules, no plan... let's fly!"
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("winona", TrainerType.Enemy, [
        Pokemon(46, level=11, moves=[GetMove("Scratch"), GetMove("Stun Spore"), GetMove("Poison Powder"), GetMove("Absorb")], ability="Dry Skin")
    ])

    call Battle([trainer1, trainer2]) from _call_Battle_31
    $ battlehistory["Instructor Winona1"]  = _return

    show winona with dis

    if (WonBattle("Instructor Winona1")):
        $ AddEvent("Instructor Winona", 2.1)

        winona @happy "Good work. Yes, I'll advance you. {size=25}I think I have a paper somewhere telling me how to do that...{/size}"
        winona @talkingmouth "Nevertheless, good job."

        $ passedclass = True
        jump aftertutorintroflying
    
    else:
        winona sad "Wha-?! Oh no! Y-you weren't supposed to lose... I've ruined everything!"

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide winona with dis
elif (not HasEvent("Instructor Winona", 3.1) and classstats["Flying"] >= 20):#Sharp Beak
    show winona with dis
    if (not HasEvent("Instructor Winona", 3)):
        $ renpy.pause(1.0, hard=True)

        winona @talkingmouth "Um... [first_name]?"

        red uniform @talkingmouth "Yes, Instructor Winona?"

        winona @talkingmouth "Do you think you're ready to take the advancement exam?"

        red @closedbrow talking2mouth "Um... geez, Instructor, I don't know. Absolutely no offense intended, but isn't it your job to tell me if I am?"

        winona @talkingmouth "...Maybe? But I don't want to put any pressure on you!"
        winona @sadbrow happymouth "I'm still pretty new at this. I figure you guys have the best understanding of... well, your current understanding. If that makes any sense."
        winona @closedbrow talking2mouth "I think you are ready to take the advancement exam. But if your Pokémon are too low-level, or you don't have the right types on-hand, or... anything like that, really..."
        winona @happy "Well, I don't want to push you out of the nest before you can fly!"

        red @happy "Absolutely. And, as a flightless primate, I appreciate your concern."

        winona @talkingmouth "Hah. So, how are you feeling?"

        red @closedbrow talking2mouth "Well... what do I get if I take the advancement exam?"

        winona @closedbrow talkingmouth "Well, moving to the third level of the class means that you... um... let me check my notes..."

        pause 1.0

        winona @talkingmouth "I'll give you one, uh 'Sharp Beak.' They're a, um, talisman that boosts the power of Flying-type moves by 10%%."

        red @closedbrow talking2mouth "That sounds useful."

        pause 0.5

        red @happy "Then, yeah! I believe I can fly!"

        winona @happy "Oh, I know that song!"

        pause 0.5

        winona @sad "Right, right. The exam."

        $ AddEvent("Instructor Winona", 3)
    else:
        red uniform @talking2mouth "Instructor Winona, I'm ready to try the advancement exam again. Will you let me?"

    winona @talkingmouth "{color=#0048ff}I'll be using a single Flying-type Pokémon.{/color} Oh, and, um, this will be a standard one-on-one battle. "

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    winona @happy "N-no pressure, alright? I know I--you--we--can do this!"
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("winona", TrainerType.Enemy, [
        Pokemon("Swablu", level=21, moves=[GetMove("Dragon Breath"), GetMove("Round"), GetMove("Disarming Voice"), GetMove("Peck")], ability="Cloud Nine", item="Oran Berry")
    ])

    call Battle([trainer1, trainer2]) from _call_Battle_88
    $ battlehistory["Instructor Winona2"]  = _return

    show winona with dis

    if (WonBattle("Instructor Winona2")):
        $ AddEvent("Instructor Winona", 3.1)

        winona @talkingmouth "Phew! That's your second exam down, right? {size=30}Shoot; where did I put my gradebook...?{/size}"
        winona @closedbrow talkingmouth "...Drat. Well, I'll have to find it later. For now, though, take this."

        $ GetItem("Sharp Beak", 1, "You gained a Sharp Beak! It doesn't appear to be organic, thankfully.")

        $ renpy.pop_call()
        jump aftertutoring
    
    else:
        winona @sad "S-sorry... I got your hopes up and everything..."

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide winona with dis
elif (not HasEvent("Instructor Winona", 4.1) and classstats["Flying"] >= 30):#Pluck
    show winona with dis
    if (not HasEvent("Instructor Winona", 4)):
        $ renpy.pause(1.0, hard=True)

        narrator "You're casually working on some problems in a practice booklet when you notice Instructor Winona walking alongside you, apparently lost in thought."

        red uniform @talkingmouth "Instructor Winona?"

        winona @surprised "Oh! Yes?"

        red @confused "I was just wondering... this is your first year as a teacher, right? You never taught at another school, did you?"

        winona @talkingmouth "That's right. I got a job at Kobukan immediately out of postgrad--it was kind of a miracle, honestly! Apparently, there weren't many other qualified Flying-type specialists, so the pool was pretty small."

        red @happy "Why did you decide to become a teacher?"

        winona @happy "I come from Fortree city in Hoenn."

        pause 0.5 

        winona @closedbrow talkingmouth "Well, it's called 'Fortree City'. It's more of a village. It's a very traditional place, very faith-focused. Everyone lives in harmony with nature."
        winona @talking2mouth "Our ancestors were apparently sent from Johto to settle there, but they'd have to chop down acres of lush jungle in order to. The leader of the settlers refused, and so they all built their houses in the treetops."

        red @talkingmouth "...That's cool, but I'm not sure I see the connection to education."

        winona @sad "Our ancestors were noble people, but they didn't really think about the long-term effects of living hundreds of feet above the jungle floor."
        winona @closedbrow talking2mouth "It's pretty hard for us to get professionals--like teachers, doctors, engineers--to visit us from the land. Fortree needed a teacher, so... I decided to become one."

        red @happy "Huh. Kinda like Skyla."

        winona @happy "Our community is very tight-knit. Lots of people take on professions because the community needs them."

        pause 1.0

        winona @closedbrow talking2mouth "Of course, being a teacher in Kobukan doesn't directly help Fortree, but I plan to return there in a few years, and hopefully bring my experience, and a good amount of money, back with me."

        red @talkingmouth "Well, good luck with that."

        winona @happy "Thank you."

        pause 0.5

        winona @talking2mouth "Hm... I think you're about ready to take the advancement exam."

        red @surprised "Really?"
        red @happy "Cool!"

        $ AddEvent("Instructor Winona", 4)
    else:
        red uniform @talking2mouth "Instructor Winona, I'm ready to try the advancement exam again."

    winona @talkingmouth "This will be a standard one-on-one battle. {color=#0048ff}This time, I don't recommend bringing a Flying-type...{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    winona @happy "A-alright... Here we go again!"
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("winona", TrainerType.Enemy, [
        Pokemon("Magneton", level=31, moves=[GetMove("Spark"), GetMove("Gyro Ball"), GetMove("Tri Attack"), GetMove("Thunder Wave")], ability="Sturdy", item="Sitrus Berry")
    ])

    call Battle([trainer1, trainer2]) from _call_Battle_89
    $ battlehistory["Instructor Winona3"]  = _return

    show winona with dis

    if (WonBattle("Instructor Winona3")):
        $ AddEvent("Instructor Winona", 4.1)

        winona @talkingmouth "Great job! That's three tests you've completed. Acccording to this rubric, you needed to beat a Flying-type, beat a Pokémon strong against the Flying-type, and beat a Pokémon weak to the Flying-type."
        winona @happy "So... that's all of them. Yes. Well done! Future tests will have me using three Pokémon, instead of just one."

        red @happy "I had a good teacher. Can't wait to see what's next!"

        $ passedclass = True
        jump aftertutorintroflying
    
    else:
        winona @sad "Shoot and double-shoot. It must be my fault--I'm sorry!!"

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide winona with dis

elif (FindGenericClassScene(True)):#generic scene
    $ renpy.call(FindGenericClassScene())
    hide winona with dis
else:# _really_ generic scene
    show winona with dis
    winona @surprised "Hello, students! Let's see, today, we'll be... ah!"
    winona @talking2mouth "Okay, now, it's very important to understand the many different kinds of flight Flying Pokémon exhibit. Wings aren't necessary, but..."
    hide winona 
    show winonabg
    with dis
    narrator "Class proceeds without incident."

return

label movetutorflying:
show winona with dis
winona @closedbrow talking2mouth "Okay, I'm fairly new to teaching Pokémon moves, but I think I can do that... provided they're Flying-type, of course."
winona @talkingmouth "I can teach Wing It, a move that raises one of your Pokémon's stats by two stages, and decreases another by one."
if (HasEvent("Instructor Winona", 4.1)):
    winona @happy "There's also Pluck. That one's good for stealing Berries."

label aftertutorintroflying:
$ taughtmove = None

menu:
    ">Learn Wing It":
        $ taughtmove = "Wing It"
    ">Learn Pluck" if (HasEvent("Instructor Winona", 4.1)):
        $ taughtmove = "Pluck"
    "Nevermind":
        winona @sad "Oh. Did I...? Um, okay."

        if (passedclass):
            $ renpy.pop_call()
            jump aftertutoring
        else:
            jump afterflyingsetup
python:
    hidebattleui = True
    renpy.transition(dissolve)
    newindex = renpy.call_screen("switch", MakeRed())
    if (newindex != "back"):
        newmon = playerparty[newindex]
    hidebattleui=False
if (newindex == "back"):
    winona @sad "Oh. Did I...? Um, okay."
elif (MonCanLearn(newmon, taughtmove)):
    $ playerparty[newindex].LearnNewMove([(1, taughtmove)])
    if (taughtmove in newmon.GetMoveNames()):
        jump endclass
else:
    winona @sad "I'm very sorry. I don't think I know how to teach that Pokémon [taughtmove] yet."
    
jump aftertutorintroflying

label itemcraftflying:
show winona with dis

winona @talking2mouth "A bird's nest is often filled with trinkets and items that they think they might have a use for later. Trainers should do that, too. If you don't know what's coming next, just have as many tools available as you can."
winona @talkingmouth "For example, the Sharp Beak boosts the power of Flying-type moves by 10%%. We're still figuring out {i}why{/i}, but common consensus is that it scares opponents."

menu:    
    ">Obtain Sharp Beak" if (HasEvent("Instructor Winona", 3.1)):
        $ GetItem("Sharp Beak", 1, "You craft a Sharp Beak. Upon closer inspection, it's just a 3D-printed model.")
        jump endclasscraft
    "Nevermind":
        winona @sad "Right, you wouldn't want to do that now, would you?"
        jump afterflyingsetup