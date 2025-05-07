label secondhomeroom010526:

scene blank2

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

show oak 
hide blank2 
with splitfade

$ PlaySound("bellchime.ogg")

oak @talkingmouth "...Which is why Hyper Beam is a particularly effective finishing move. At least, it {i}was{/i} when I was champion."
oak @happy "Yes, I myself had a particular Tauros that managed to utilize the adrenaline rush from knocking out a foe to push through the shock of launching a Hyper Beam!"
oak @talking2mouth "Unfortunately, in his old age, he has lost that ability... and I've not been able to replicate that technique in any of the other Pokémon I've trained. I suppose I, too, have lost that ability."
oak @closedbrow sweat talking2mouth "And unlike my dear Tauros, I cannot be sent to a farm outside Goldenrod to live a life surrounded by amorous Miltank."
oak @talking2mouth "Of course, using our modern understanding of battle techniques, Hyper Beam was not the best move to use in that situation--Giga Impact would have been far better, given my Tauros' significantly higher physical attack stat."

pause 0.5

oak @sad2brow talking2mouth "Back in the day, though, when we were knocking out opponents left and right... it all seemed so much simpler." 
oak @sad2brow talking2mouth "It feels as though the world has shifted around me, and I'm only now beginning to realize the colors around me, and... well, the fact I need to care about them."

pause 1.0

oak @talking2mouth "You know, back in the day, Agatha used an Arbok on her team. That Arbok knew Wrap, and Wrap, I swear, was a move that prevented the foe from moving for multiple turns, locking them down {i}and{/i} damaging them."
oak @happy "Why, it seemed as though Wrap was a move that combined the advantages of both the Frozen and Poisoned status conditions, but did not overlap with either!"

pause 1.0

oak @closedbrow talking2mouth "But... that's simply not true. My memories of Wrap's strength are fiction. Perhaps I only thought it was so strong because Agatha used it to beat me as many times as I used Hyper Beam to beat her."
oak @happy "You know, she never admitted this, but I believe she learned to train Ghost-types specifically because she feared my Hyper Beam so much!"

pause 0.5

redmind uniform @thinking "I've never heard Sam talk about his Champion days so much... sounds like he misses them."
redmind @sadbrow frownmouth "...If life was simpler back then, and he's now realizing how much effort it takes to be a teacher..."
redmind @sad2eyes frownmouth "Well, he's over sixty. I can't imagine he wanted to sign up for an extremely difficult job at his age."

if (classstats["Ground"] > 6 or classstats["Grass"] > 6):
    if (classstats["Ground"] >= classstats["Grass"]):
        redmind @sadbrow frownmouth "Of course, Instructor Bertha's quite a bit older..."

    else:
        redmind @sadbrow frownmouth "Of course, Instructor Ramos is quite a bit older..."

oak @talking2mouth "Well, that's enough rumination on things that never happened."

oak @talking2mouth "Remember, your test on terrains will be tomorrow, and I must be frank that it will be difficult. However, I will do my best, during tomorrow's lectures, to prepare you. Additionally..."

pause 1.0

oak @angrybrow talking2mouth "I will have a zero-tolerance policy for interruption."

show melody bubblemouth uniform with dis: 
    xpos 0.75 xzoom -1

melody "{w=0.5}.{w=0.5}.{w=0.5}."

hide melody with dis

$ PlaySound("bellchime.ogg")

hide oak with dis

pause 1.5

if (HasEvent("Leaf", "AcceptedConfession")):
    show leaf uniform blush with dis:
        xpos 0.5
        
    leaf @talkingmouth "Heya... sport."

    red @confused "'Sport'?"

    leaf @sadbrow talkingmouth "I was thinking, like, of a casual nickname to call you. And, uh, 'sport' was all that came to mind."

    red @unamusedbrow unamusedmouth "{w=0.5}.{w=0.5}.{w=0.5}."
    red @happy "Well then, heya, pops!"

    leaf @closedbrow talking2mouth "Nevermind, date cancelled, see you in another month."

    red @sweat closedbrow talking2mouth "Yeah, seeya."

    pause 1.0

    leaf @happy "Okay, but, no, really! This is it! We're actually going to do it now! {i}Nothing{/i} has gone wrong, so we can finally do this properly!"
    leaf @sarcastic "And then you'll totally fall under my sway, and then think you've spent too much time on me to back out, so you'll be trapped 'cause of the opportunity cost."

    red @happy "Seems you've got a pretty good plan."

    leaf @talkingmouth "Oh yeah, step one: permanently ensnare you due to fear of having wasted time. First move's the most important, you know?"

    red @confused "This is the first move?"

else:
    show leaf uniform with dis:
        xpos 0.5

    leaf @talking2mouth "Hey. Ready to have a real good time?"

    red @talking2mouth "You make it sound like something I'd find on a bathroom stall."

    leaf @closedbrow talking2mouth "I'm {i}marginally{/i} classier than that."

    red @unamusedbrow talking2mouth "How thick is this margin?"

    leaf @closedbrow talkingmouth "Thicker than you, and that's saying a lot, considering you turned me down for a date."
    leaf @sarcastic "I mean, it's {i}me{/i}. So, like, that's a pretty big mistake."

    red @sadbrow talkingmouth sweat "Still trying to get me to change my mind, huh...?"

    leaf @surprised "Still trying? Huh? I haven't even started!"

red @unamusedbrow talking2mouth "You flew across an ocean to grab me."

leaf @closedbrow talkingmouth "Eh, I would've done that anyway. I don't get a stamp on my loyalty card for something I was already planning on."

red @talking2mouth "I don't remember ever handing out loyalty cards."

leaf @talkingmouth "Really gotta get that memory checked out, Skippy. Early-onset dementia's an awful thing."

red @closedbrow talkingmouth "Yeah, yeah. Come on. Let's go to the dorm and get changed."

scene blank2 with splitfade

pause 1.0

scene bedroom with splitfade

if (HasEvent("Leaf", "AcceptedConfession")):
    redmind swimsuithatless @confusedeyebrows frownmouth "...But get changed into what?"
    redmind @thinking "I don't really have anything that I could call a 'date outfit'..."

    if (GetRelationshipRank("Klara") > 0):
        redmind @thinking "Of course, that didn't stop me yesterday. But Klara seemed a bit annoyed that I hadn't dressed up nicely, and I don't want to make that mistake again."

    show bedroom with vpunch

    red @happy "{size=40}HEY! LEAF! WHAT SHOULD I WEAR FOR OUR DATE?!{/size}"

    leaf hatless @happy "{size=40}ABSOLUTELY NOTHING!{/size}"

    red @happy "{size=40}PRETTY SURE THAT'LL VIOLATE SOME LAWS!{/size}"

    ethan @happy "{size=40}BEAUTY ISN'T A CRIME!{/size}"

    yellow neutrallowponytail @angry shadow "{size=40}STOP YELLING ABOUT NUDITY!{/size}"

    ethan @confusedeyebrows talking2mouth "{size=40}YOU'RE A NURSE, WHY IS THIS SUCH A THING FOR YOU?!{/size}"

    yellow @surprised "{size=40}I...{w=0.5} I...{w=0.5}{/size}{nw}" 
    extend @scaredeyes angrymouth furiouseyebrows shadow "{size=40} WE'RE IN THE SAME ROOM! YOU DON'T HAVE TO YELL!{/size}"

    pause 2.0

    $ PlaySound("vibrate.ogg")

    show phone_B
    show phone_A
    with fadeinbottom

    show phone_C behind phone_A with dis

    show phone_msg1 behind phone_A with dis:
        xzoom -1
        
    $ title = Text("Leaf G. Green",size=30,font="fonts/consola_0.ttf",color="#313131")

    image msg3 = Text("Yo. Just realized I should probably just\ntext you. What should I wear?\nI'm kinda dumb when it comes to fashion.",size=21,color="#ffffff",line_spacing=5,text_align=0.0)

    show text title behind phone_A:
        xalign 0.51 yalign 0.34
    show msg3 behind phone_A:
        xpos .41 ypos .4
    with dis

    pause

    image msg4 = Text("It's fine! Don't worry about it.\nYou can wear anything you want.\nThough if you want to match me\nyou could wear your uniform.",size=21,color="#ffffff",line_spacing=5,text_align=0.0)

    show phone_msg1 behind phone_A:
        xzoom 1
    show text title behind phone_A:
        xalign 0.51 yalign 0.34
    show msg4 behind phone_A:
        xpos .41 ypos .4
    hide msg3
    with pixellate

    redmind @thinking "Huh, my uniform? I just took it off, but sure, I guess."

scene blank2 with splitfade

pause 1.0

scene suite with splitfade

if (HasEvent("Leaf", "AcceptedConfession")):
    red uniform @happy "Hey, Leaf! Ready. Decided to take your advice, and put my uniform on."

    redmind @thinking "Feels weird to be wearing this outside of school hours, though. I half expect to have to go to homeroom any second now."

    $ showredonly = True

    red @talkingmouth "Ready?"

    leaf @talking2mouth "A-almost."

    pause 1.0

    leaf @talking2mouth "...Um, how do you feel about makeup?"

    menu:
        "I'm sure you'd look great in it.":
            $ ValueChange("Leaf", 1)

            leaf "Uh... well, I wear some every day, so you'd know."

            pause 0.5

            red @surprised "Wait, really?"

            leaf "Yeah. I mean, not {i}heavy{/i} makeup, but a little toner, a little mascara..."
            leaf "{i}No{/i}-one's eyelashes {i}actually{/i} look like this."

            pause 2.0

            red @sadbrow talking2mouth "You're always so sarcastic, I genuinely can't tell if this is a joke."

            leaf "Not this time! Pretty much every girl wears a bit of makeup."
            leaf "If we don't, guys tell us we 'look tired.' Gotta paint away the indicators that we are, in fact, human."

            pause 0.5

            red @closedbrow talking2mouth "Noted. I don't remember if I've ever said that, but if I have--sorry."

            leaf "You don't need to apologize for something you don't even remember if you did or not!"
            
            pause 0.3

            leaf "Wait, don't tell me--'Sympathy, not culpability.'"

            pause 0.5

            red @happy "You got it."

        "No strong feelings.":
            leaf "What a very diplomatic, but boring, answer."

            pause 0.3

            redmind "What can I say? I like straddling that fence."

            pause 0.3

            leaf "Well, lame centrist answers like that aren't going to give you much luck when it comes to straddling {i}other{/i} things!"

        "You look better without it.":
            $ ValueChange("Leaf", -1)

            leaf "...Okay, I realize you didn't know this, but I wear some every day, so, like, ouch?"

            pause 0.3

            red @surprised "Wait, really?"

            pause 0.3

            leaf "Yeah. I mean, not {i}heavy{/i} makeup, but a little toner, a little mascara..."
            leaf "{i}No{/i}-one's eyelashes {i}actually{/i} look like this."

            pause 2.0

            red @sadbrow talking2mouth "You're always so sarcastic, I genuinely can't tell if this is a joke."

            pause 0.3

            leaf "Not this time! Pretty much every girl wears a bit of makeup."
            leaf "If we don't, guys tell us we 'look tired.' Gotta paint away the indicators that we are, in fact, human."

            pause 0.3

            red @closedbrow talking2mouth "Noted. I don't remember if I've ever said that, but if I have--sorry."

            leaf "You don't need to apologize for something you don't even remember if you did or not!"
            
            pause 0.3

            leaf "Wait, don't tell me--'Sympathy, not culpability.'"

            pause 0.3

            red @happy "You got it."

    pause 1.0

    leaf "{size=30}Alright.{/size}"

    pause 0.5

    leaf "{size=30}Ahem.{/size} Alright! I'm coming out!"

    pause 0.3

    red @confused "Damn, the date hasn't even started, and I've already turned you off of men?"

    leaf "I'm pretty sure we used that joke already. Anyway, who said I'm going to restrict myself to {i}just{/i} women? I enjoy double battles, too."

    pause 1.0

    red @confused "No, seriously, are you coming?"

    leaf @talking2mouth "{size=30}Just... give me a second.{/size}"

    pause 1.0

    menu:
        "[courageoption] You'd look beautiful in a trash bag. Come on.":
            $ TraitChange("Courage")

            pause 1.0

            $ ValueChange("Leaf", 1)

            if (HasEvent("Leaf", "AcceptedConfession")):
                leaf "{size=30}...'Kay.{/size}"

            else:
                leaf "{size=30}Thought... this wasn't a date?"

                red @sadbrow talkingmouth "There are {i}a lot{/i} of beautiful people that I'm not dating, Leaf."

                leaf "...Fair. Okay. I'm coming."

        "[charmoption]Relax. I'm not even dressed up fancily.":
            $ TraitChange("Charm")

            pause 1.0

            leaf "You're right. It's all in my head. I just need to take a step out, because as soon as I do... it's too late to turn back, anyway."

            pause 0.5

            leaf "Like when I was on Tia."

            pause 0.5

            leaf "Okay, I'm coming."

        "[patienceoption]>Wait for Leaf":
            $ TraitChange("Patience")

            pause 2.0

            leaf "Okay, I'm coming."

    show leaf adventure bigblush makeup with Dissolve(2.0):
        xpos 1.0
        ease 1.0 xpos 0.5

    pause 1.0

    leaf @sadbrow talkingmouth "{size=30}H-hey.{/size}"

    $ showredonly = False

    leaf @talkingmouth "...Kinda over-the-top, I guess?"

    menu:
        "Maybe a bit.":
            leaf blush @sadbrow talking2mouth "Oh. Oh, that's fine! I'll change! It's not a problem. Let me just..."

        "Not at all.":
            $ ValueChange("Leaf", 1, 0.5)

            leaf blush @closedbrow blush talkingmouth "Yeah, that's, uh, that's the right answer. Good job. You passed."

        "Gorgeous.":
            show leaf surprisedbrow bigblush frownmouth with dis

            pause 1.0

            $ ValueChange("Leaf", 3, 0.5)

            leaf blush @closedbrow blush talkingmouth "Yeah, well... you're, uh, you're pretty 'gorge' yourself."

            pause 0.5

            leaf @closedbrow talking2mouth "{size=30}Why did I say that.{/size}"

    $ PlaySound("phone.ogg")
            
    leaf frownmouth @surprisedbrow talking2mouth "Wait, what's... huh?"

    red @confused "What is it?"

    leaf @talking2mouth "Not sure. One sec."

    show leaf:
        xpos 0.5 ypos 1.0 zoom 1.0
        ease 0.5 xpos 0.75 ypos 0.9 zoom 0.9

    pause 0.5

    leaf @happy "Hi! Yes, this is Leaf. Yep, Leaf Green."

    pause 1.0

    leaf @surprisedbrow talking2mouth "What... what do you mean?"
    leaf frownmouth @closedbrow talking2mouth "The reservation was for tonight, wasn't it? Seven PM."

    pause 1.0

    leaf @angrybrow talking2mouth "What are you... what do you mean you have to cancel?!"
    leaf @surprised "The entire restaurant...? That's not... no! Why would you have to...?"

    pause 0.5 

    leaf surprised @angry "You're making this up. You have to be! What do you mean, 'health code' concerns?! You're a {i}seven{/i}-star restaurant! I can {i}hear{/i} your Kalosian accent! You don't {i}have{/i} health code--"

    pause 1.0

    Character("Phone") "*{i}Click.{/i}*"

    pause 0.5

    show leaf sadbrow frownmouth with dis:
        xpos 0.75 ypos 0.9 zoom 0.9
        ease 0.5 xpos 0.5 ypos 1.2 zoom 1.3

    red @sadbrow talkingmouth "I'm guessing it's not good news?"

    leaf @closedbrow talking2mouth "...This isn't going to work."

    red @surprised "Huh?"

    leaf @talking2mouth "I give up. The universe is giving me a message, and I need to start listening to it. This date will never happen."
    leaf @sad "It will never work between us. Sorry for wasting your time."

    show leaf:
        xpos 0.5 ypos 1.2 zoom 1.3
        ease 0.3 ypos 1.0 zoom 1.0 xpos 1.2

    pause 0.4

    $ PlaySound("door_slam.ogg")

    red @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    narrator "From within Leaf's bedroom, you hear the sound of something tearing, and you wince at what is likely a pretty expensive tantrum."

    pause 1.0

    redmind @sadbrow frownmouth "Well... now what?"

    show blue og frownmouth with dis:
        xpos -0.2
        ease 1.0 xpos 0.25

    pause 1.0

    red @talking2mouth "Blue?"

    blue @talkingmouth "Well? Now what?"

    red @confused "I was thinking the exact same thing."

    blue @closedbrow talkingmouth "Typical [first_name]. As bad with girls as Gramps is."

    red @unamusedbrow talking2mouth "The fact you were, at some point, birthed, would seem to indicate he wasn't {i}that{/i} bad."

    blue @talkingmouth angrybrow "Tell you what. I'm feeling magnanimous. I'll tell you what to do here--but in exchange, you need to do {i}me{/i} a favor."

    red @closedbrow talking2mouth "Look, I'm pretty sure I know what to do, I was just gathering my thoughts."

    blue @closedbrow talkingmouth "Are you taking the deal or not?"

    red @closedbrow sweat talking2mouth "You're not listening at all... yeah, sure, fine, I'll take the deal."

    blue @happy "Hah! You fell for it! You totally owe me a favor, now, and I can make you do {i}anything{/i} I want!"

    red @unamusedbrow talking2mouth "Yeah, how devious. Just tell me what the deal is. Or what you {i}think{/i} the deal is, more likely."

    pause 1.0

    blue @talkingmouth "Leaf isn't actually giving up. She flew across an ocean for you. She's just tired of {i}her{/i} plans falling through, and wants you to take the initiative."
    blue @closedbrow neutralmouth "Just knock on the door and take her somewhere. She's overcomplicating it, and you're too dumb to see the obvious answer she's ignoring on purpose."

    red @confused "Oh, yeah? How do you figure? Leaf's seemed to be pretty okay with deciding everything up to now."

    blue @closedbrow talkingmouth "You {i}would{/i} say that. Just shows what you know. Women are like an Inverse Battle--throw everything you know out the window."
    blue @closedbrow talkingmouth "If they say they want to decide, decide for them."
    blue @angrybrow talkingmouth "If they say they need space, stay with them."
    blue @wistfulbrow wistfulmouth "And if they say they want you to make more friends... don't."

    show blue scaredbrow frownmouth with dis

    red @talking2mouth "...I'm telling Daisy you said that."

    blue @surprisedmouth "Shit, no, don't!"

    red @talkingmouth "Sorry. There's a fee for misogyny in this dorm."

    blue @sadbrow talkingmouth "Come on, I was speaking metaphorically. Don't tell Daisy!"

    pause 1.0

    red @closedbrow talking2mouth "I'll hold off on telling her until I've seen what your 'favor' is. If it's something ridiculous..."
    red @unamusedbrow talking2mouth "Well, I'm sure Daisy would be very interested in hearing your interpretation of gender relations."

    hide blue with dis

    redmind @closedbrow frownmouth "Okay... now, back to Leaf."
    redmind @frownmouth "Most of what Blue said was garbage, but he might not have been entirely wrong in this case..."
    redmind @sweat closedbrow frownmouth "So, if this works, I guess I really do owe him a favor."

    pause 0.5

    redmind @unamusedbrow unamusedmouth "Fifty-fifty on if I want this to work, now..."

    scene door with splitfade

    $ showredonly = True
    
    $ PlaySound("knock.ogg")

    pause 1.5

    red uniform @sadbrow talkingmouth "Leaf?"

    pause 0.5

    red @closedbrow talkingmouth "Leaf Gracidea Green."

    pause 0.5

    leaf "S'not here."

    pause 0.5

    red @talking2mouth "Well, there's someone who sounds {i}very{/i} similar to her in her dorm. Did she jump out the damn window?"

    leaf "I have a twin. {w=0.5}I told you this."

    pause 0.3

    red @talkingmouth "Well, I want to talk to your twin, then."

    leaf "...Door's open."

    pause 0.3

    red @surprised "Huh?"

    show opendoor with dis
    
    $ showredonly = False

    red @closedbrow talking2mouth "Oh. I didn't, uh, try that."
    redmind @thinking "I just assumed she'd locked it..."

    scene blank2 with splitfade

    pause 0.5

    scene leafbedroom with splitfade

    red uniform @confused "Huh? Leaf?"

    show leaf adventure makeup blush sadbrow frownmouth disguise with Dissolve(2.0)

    $ AddEvent("Leaf", "IsFael")

    leaf @talking2mouth "Leaf eez not here. Eez only Fael. Eez twin of Leaf. And perpetual failure."

    $ RemoveEvent("Leaf", "IsFael")

    leaf @nodisguise sarcastic "See, if I pin my failures on my alter-ego, I can avoid feeling like such crap about my inability to plan even a single measly dinner."

    $ AddEvent("Leaf", "IsFael")

    red @sadbrow talking2mouth "Yeah, I, uh... I got it."

    pause 0.5

    red @talkingmouth "Leaf, can I--"

    leaf @talking2mouth "Eez Fael."

    red @upeyes angryeyebrows talking2mouth "{i}Fael{/i}, can we talk?"

    leaf @sadbrow talking2mouth "Bed eez empty. Seeet."

    show leaf:
        ypos 1.0 zoom 1.0
        ease 0.5 ypos 1.2 zoom 1.3

    pause 1.0

    red @talking2mouth "Look... I think Leaf may have been building me up in her head as something I'm not."
    red @sad2eyes sadeyebrows talkingmouth "And I know she wanted this date to be, like, completely perfect, but..."
    red @sadbrow talkingmouth "Even now, in Kobukan Academy, I'm a simple guy. I like burgers. I like fast cars. I like Pokémon."
    red @happy "And I like my dormmate, Leaf."

    pause 0.5

    red @sadbrow talkingmouth "Whether this date went perfectly or not isn't really important."
    red @happy "After all, we're just trying to figure out if we're compatible, you know? Maybe it wouldn't work out, regardless of how much planning went into it. Then--"

    show leaf sadbrow cry:
        ypos 1.2 zoom 1.3
        ease 0.2 ypos 1.3 zoom 1.4

    show leafbedroom with vpunch

    narrator "Fael suddenly grabs your hands and looks at you with tearful intensity from behind the Beagle Puss."
    narrator "You're unsure why, given you are certain you have never met this individual before."

    leaf @sadbrow surprisedmouth "That's it, though! I don't {i}want it{/i} to not work out! I want this date to go so fantastically that you can't wait for another!"
    leaf @sadbrow talking2mouth "I want to spend the rest of this school year going on dates with you. I want us to have a massive, romantic, dramatic showdown as we face each other in the finals of the National Tournament."
    leaf @closedbrow talking2mouth "I want..."
    leaf @sadbrow talking2mouth "I want you to be so impressed that I stand head and shoulders above all other options. I want this one date to make me number one, forever!"

    show leaf -sadbrow -cry with dis:
        ypos 1.3 zoom 1.4
        ease 0.5 ypos 1.2 zoom 1.3

    pause 1.0

    red @sadbrow talkingmouth "I'm sorry. That's not possible."
    red @happy "But you don't have to try to impress me. I'm already impressed by you. We swore a Friendship Pact, remember?"
    red @talkingmouth "You flew across an ocean for me. I'll never forget that. And... frankly..."
    red @sadbrow talkingmouth "No matter how fancy this dinner was, it was never going to be more impressive than that."

    leaf @closedbrow talking2mouth "...Zis eez obvious."
    leaf @talkingmouth "Maybe Leaf vuz just trying to one-up her vith ze impressivenezz."

    red @confused "Vuz? Vith? Are you a vampire now?"

    leaf @closedbrow talking2mouth "...No."

    $ RemoveEvent("Leaf", "IsFael")

    leaf -disguise surprisedbrow frownmouth @sadbrow talking2mouth "I'm a very silly girl. I'm sorry, [first_name]. I--"

    show leaf:
        ypos 1.2 zoom 1.3
        ease 0.2 ypos 1.0 zoom 1.0

    show leafbedroom with vpunch

    red @surprised "HOLY SHIT LEAF YOU'RE HERE NOW WHAT HAPPENED TO FAEL?!"

    leaf "{w=0.5}.{w=0.5}.{w=0.5}."

    leaf flirtbrow frownmouth @sarcastic "I can't believe I {i}want{/i} to date you."

    red @sadbrow talking2mouth "...Is she gone? I thought we were really hitting it off."

    leaf @closedbrow talking2mouth "Alright, that's enough, joke's over."

    red @confused "Do you have her phone number? Or, like, do you know where she lives?"
    red @sad2eyes sadeyebrows talking2mouth "That moustache did something to me. Do you think her RotoPhoto DMs are open?"

    leaf @sarcastic "Dude. The joke's over."

    red @happy "Hey, you started this bit. That means I get to end it."

    leaf -flirtbrow -frownmouth @surprised "...I feel like starting the bit means that I should have more say over how it ends."
    leaf @closedbrow blush talkingmouth "On the other hand, ooh, how {i}assertive{/i} of you."
    leaf @flirtbrow blush talkingmouth "You have any other decisions you want to make?"

    show suite at sepia
    show flashback
    with dis

    $ renpy.pause(1.0, hard=True)

    show blue og frownmouth at sepia behind flashback with dis:
        xpos 0.25

    blue @closedbrow talkingmouth "You {i}would{/i} say that. Just shows what you know. Women are like an Inverse Battle--throw everything you know out the window."
    
    show blank with splitfade

    hide blue
    hide suite
    hide flashback
    hide blank with dis

    redmind @closedbrow frownmouth "Damn it. I guess I {i}do{/i} owe him a favor, now..."

    red @talkingmouth "Yeah. We're going out."

    leaf @sadbrow talking2mouth "...[first_name]... we can't. The restaurant shut down."

    red @confused "Wait, the entire restaurant?"

    leaf @closedbrow talking2mouth "'Health code concerns.' Apparently some super-fast Pokémon got into their kitchen and sprayed poison everywhere."
    leaf @sarcastic "So now they need to fumigate the restaurant, and won't open for a few more days."

    red @closedbrow talkingmouth sweat "That's unlucky."

    leaf @sadbrow talking2mouth "I'm kind of numb to it, at this point. There have been a lot of weird events like this..."
    leaf @closedbrow talking2mouth "Obviously, stuff like Yellow going missing, or you going to Pallet Town were... you know, those happened, and there wasn't much anyone could do about that, but even smaller annoyances like this kept popping up."
    leaf @sadbrow talkingmouth "I mean, you can see why I thought I was cursed, right?"

    red @closedbrow talkingmouth "Well, you're not. Now come on, get changed."

    leaf @surprisedbrow talking2mouth "Where are we going?"

    red @talking2mouth "A little café in Inspira."

    if (sawwallyellow):
        red @talking2mouth "I saw Wally and Yellow hanging out there a while ago. It's a nice, quiet place."

    else:
        red @talking2mouth "It was one of the ones we went to when you dragged me all across Inspira for that shopping trip with Whitney, Flannery, and Tia."

    show leaf blush surprisedbrow with dis

    red @happy "You'd just be a little overdressed if you went the way you are now."

    show leaf sadbrow with dis

    red @sadbrow talkingmouth "And, to be honest... I think I'd feel too weird to wear my uniform while you're wearing something as pretty as that."

    leaf @sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."
    leaf @talkingmouth "Alright."
    leaf @closedbrow talking2mouth "I'm going to take a shower to clear my head. You can get changed. Meet back in the main suite in five?"

    red @happy "Sounds like a plan."

    scene blank2 with splitfade

    pause 0.5

    scene suite with splitfade

    pause 0.5

    show blue og with dis:
        xpos 0.25

    blue scaredeyes desperateeyebrows frownmouth og @closedbrow neutralmouth "Well, did it work or did it work? What did I tell you? If you listened to me once in a while, you might actually--"

    red @unamusedbrow talking2mouth "Daisy."

    blue @furiousmouth "Fucking {w=0.5}{i}don't!{/i}"
    
    hide blue with dis

    red @closedbrow talking2mouth "Hm... I need to remember that trick."

    pause 0.5

    show leaf with dis:
        xpos 1.2 
        ease 0.5 xpos 0.75

    leaf @talkingmouth "Did I miss something?"

    red @closedbrow talking2mouth "Nah. You ready?"

else:
    red @happy "Hey, Leaf! Ready. You coming?"

    show leaf with dis

leaf blush @sadbrow talkingmouth "Ready as I can be."

scene blank2 with splitfade

$ location = "city"
$ RecordKnownLocations("Leaf", "Cafe")

if (HasEvent("Leaf", "AcceptedConfession")):
    narrator "You lead Leaf to the café in Inspira, silently congratulating yourself on finding the way there without getting lost."

else:
    narrator "Leaf leads you to a simple café in Inspira, one you vaguely remember from that time you went shopping with Whitney, Flannery, and Tia."

    red @talkingmouth "Huh. I assumed you were taking me somewhere really crazy?"

    leaf @closedbrow talking2mouth "I mean, I {i}would have{/i}, if this was a date. I would've dressed up and everything, too."
    leaf @sadbrow talkingmouth "But it's not, so I didn't."

    red @sadbrow talkingmouth "I... appreciate it. I know that took some restraint."

    leaf @closedbrow talkingmouth "I know you mean it, but damn, that sounds sarcastic as hell."

show citycafe 
show leaf blush
with splitfade

if (HasEvent("Leaf", "AcceptedConfession")):
    leaf @talkingmouth "Oh, yeah, I remember this place."

else:
    red @talkingmouth "Oh, yeah, I remember this place."

leaf surprisedbrow frownmouth @neutralbrow talkingmouth "It's just, like, a café, so we can just take a seat wherever. What are you in the mood for? Coffee?"

red @confused "This late in the evening? You shouldn't consume caffeine so soon before going to sleep, you know!"
red @talkingmouth "It wrecks havoc with your sleeping patterns."

leaf -surprisedbrow -frownmouth @closedbrow talkingmouth "Have I ever told you your health nut quirks are really cute?"

red @closedbrow talkingmouth "Ah... thanks. I wouldn't call myself a health nut, though. I just don't want to let myself slip out of good habits."

leaf @sadbrow talkingmouth "...Yeah. I get that."

leaf @talking2mouth "Oh, there's a table there. Come on, let's sit."

show leafdate with Dissolve(2.0)

pause 1.0

if (HasEvent("Leaf", "AcceptedConfession")):
    leafdate @happymouth "So. You brought me here. What are we going to talk about?"
else:
    leafdate @happymouth "So. I brought you here, so that's my part of the planning done. What are we going to talk about?"

$ hadsmalltalk = False
$ GHOSTMODLEAFDATELASTSMALLTALK = "" #Records previous small talk topic, defined earlier to avoid bugs.

label leafdatedialogue:

menu: #Sub menus are now alternative mini scenes
    "What do you think of our roommates?":
        $ hadsmalltalk = True
        if GHOSTMODLEAFDATELASTSMALLTALK != "roommates":
            leafdate @happy "Oh, they're great. I was a bit weirded out at first when I learned that we'd all been assigned to the same dorm, but I guess it worked out. Who do you want to ask about?"
        jump GHOSTMODLEAFDATEROOMMATES

    "What's your story with Klara?":
        $ AddEvent("Klara", "GetKlaraInfo")
        $ hadsmalltalk = True
        $ GHOSTMODLEAFDATELASTSMALLTALK = "klara" #Update last small talk topic
        leafdate @sad "...Actually, I'm not really sure what my story is with her. She's just really friendly and generous. She just started hanging out with me after the Quarter Qlashes."
        leafdate @happymouth "She taught my Ivysaur Bad Breath, but, uh, I didn't actually {i}ask{/i} her to. I'm not sure how she even learned about me, actually... we don't share any classes, as far as I know."
        leafdate @happy "But I'm not complaining! She's really sweet. And I probably shouldn't be looking too closely at why other people might seem to be really nice, given my whole thing with you..."
        jump leafdatedialogue #Go back to main menu

    "What do you think of your classes?":
        $ hadsmalltalk = True
        if GHOSTMODLEAFDATELASTSMALLTALK != "classes":
            leafdate @happymouth "Hm? Sure, which ones?"
        jump GHOSTMODLEAFDATECLASSES

    "How are your Pokémon doing?":
        $ hadsmalltalk = True
        if GHOSTMODLEAFDATELASTSMALLTALK != "pokemon":
            leafdate @happy "Oh, they're doing fantastically! Which one do you want to hear about?"
        jump GHOSTMODLEAFDATEPOKEMON

    "Let's talk about something serious." if (hadsmalltalk):
        leafdate @happymouth "Oh... well, sure. Makes me a bit nervous to hear that, but... yeah."
        leafdate @happy "I'm game."

        jump aftersmalltalkleafdate


label GHOSTMODLEAFDATEROOMMATES:
    menu:
        "Yellow.":
            $ GHOSTMODLEAFDATELASTSMALLTALK = "roommates"
            leafdate @sadbrow happymouth sweat "Yellow's an absolute sweetheart. She just needs to stand up for herself a bit more. But I can understand why it's difficult, if she's spent so much time with Blue."
            leafdate @sad "It seems like everyone knows Yellow... but I'm not sure how many friends she has, outside of our dorm."
            leafdate @happy "I wonder when her birthday is?"

        "[first_name].":
            $ GHOSTMODLEAFDATELASTSMALLTALK = "roommates"
            leafdate @angrybrow happymouth "He's a great guy. Really oblivious, though."

            red @unamusedbrow talking2mouth "You keep saying that, but I'm not..."

            leafdate @angry "He also does this weird thing where sometimes he'll refer to himself in the third person."

            red @confused "[first_name] does not understand what Leaf means?"

            if (not HasEvent("Leaf", "AcceptedConfession")):
                leafdate @angry "Really, my only problem with him is that he won't date me."
                leafdate @happy "But I'm working on that part."

            else:
                leafdate @sadbrow happymouth sweat "Really, my only problem with him is that whenever I look into his eyes, I can feel my IQ dropping, and I'm pretty sure prolonged exposure'll turn me into some kind of brainless coral."

                red @lightblush happy "Eh heh... I don't think that's likely."

        "Ethan.":
            $ GHOSTMODLEAFDATELASTSMALLTALK = "roommates"
            leafdate @happymouth "...Okay, just between us, I'm not sure what to think about him. Like, he's a funny, nice guy. A lot like you."
            leafdate @sadbrow happymouth sweat "But I can't help but feel like he doesn't really mean most of what he says. Like, when he was flirting with Yellow... didn't that feel {i}weird{/i} to you?"
            leafdate @sad "...Maybe it's just me. I mean, he has Frienergy, so I'm sure he's not doing anything {i}bad{/i}, but... geez, I'm sorry, I shouldn't gossip like this." 
            leafdate @happy "He's a nice guy, and that's that."

        "Blue.":
            $ GHOSTMODLEAFDATELASTSMALLTALK = "roommates"
            leafdate @happy "Blue's a lot more interesting than I thought he was at first. He's totally a dick, that hasn't changed at all, but I thought he just hated you because he was jealous."

            pause 0.5

            leafdate @angry "Well, I'm not sure that's untrue, actually, but the point is that he's got more going on in that spiky head of his than {i}just{/i} seething jealousy."
            leafdate @sadbrow happymouth sweat "I couldn't have made it to Pallet Town without him, after all. For as much as he told me to give up, he got onboard with my plan as soon as I had one that {i}might{/i} work."

        "Leaf.":
            $ GHOSTMODLEAFDATELASTSMALLTALK = "roommates"
            leafdate @happy "Oh, she's an actual queen. Literally the most perfect person ever. Hot, smart, tough, and has perfect fashion sense."
            leafdate @happy "She's flawless. I hear her hair's insured for $1,600,000. I hear she does car commercials... in Unova!"
            leafdate @happy "One time she met Raihan on a plane, and he told her she was pretty."

            pause 0.5

            leafdate @angry "She's also known to be extraordinarily humble, by the way."

        "Let's talk about something else." if (GHOSTMODLEAFDATELASTSMALLTALK == "roommates"):
            jump leafdatedialogue #return to main menu

jump GHOSTMODLEAFDATEROOMMATES

label GHOSTMODLEAFDATECLASSES:
    menu:
        "Grass.":
            $ GHOSTMODLEAFDATELASTSMALLTALK = "classes"
            leafdate @sad "I'm a bit worried about Instructor Ramos, honestly. He shows up to class every day with new bruises."
            leafdate @sadbrow happymouth sweat "I mean, I don't think anyone's beating him up, but he's really old, and even little bumps can cause big problems for a man as old as him."
            leafdate @happy "But he really does know what he's talking about... if he remembers to say it."

        "Electric.":
            $ GHOSTMODLEAFDATELASTSMALLTALK = "classes"
            leafdate @angry "Instructor Surge is an absolute lunatic! But... he's not {i}just{/i} a lunatic."
            leafdate @happy "When I was flying to get you, before then, he had a talk with me, and he said some stuff that made me really think about what I was doing."
            leafdate @happy "I don't want to give him any excessive credit--like, I totally would've gone to get you eventually, with or without him--but he definitely pushed me along."

            pause 1.0

            leafdate @angry "Of course, that means that he pushed me to fly across the ocean, by myself, on a Pokémon... which might not have been the most {i}responsible{/i} thing to do."

        "Normal.":
            $ GHOSTMODLEAFDATELASTSMALLTALK = "classes"
            leafdate @happymouth "Instructor Lenora is a really patient, kind, woman. She reminds me of my Mom. I was worried that she'd be irritated I transferred into her class later, but she took it in stride."
            leafdate @happymouth "She's helped me out a lot when it comes to your mom's--I mean, {i}my{/i} Jigglypuff."
            leafdate @happymouth sadbrow "Apparently, she gets a {i}lot{/i} of refugees from Instructor Clair's class... which doesn't entirely surprise me."

        "Dragon.":
            $ GHOSTMODLEAFDATELASTSMALLTALK = "classes"
            leafdate @sad "...Instructor Clair is a bit of a sadist. But I guess I should've expected that from a woman who comes to work everyday dressed in a leather catsuit and a cape."
            leafdate @angry "I'm not in her class anymore, but I can still hear her in the back of my head, screaming at me to push myself and my Pokémon harder."
            leafdate @angry "I mean, I think I'm doing well enough! My Pokémon are happy! And Janine hasn't mentioned that I'm slacking in the Battle Team."

            pause 0.5

            leafdate @sadbrow happymouth sweat "I guess Janine's letter accepting me into the Battle Team {i}did{/i} mention I needed to take battles more seriously..."
            leafdate @happy "But when they're so much fun, how could I?!"

        "Let's talk about something else." if (GHOSTMODLEAFDATELASTSMALLTALK == "classes"):
            jump leafdatedialogue #return to main menu

jump GHOSTMODLEAFDATECLASSES

label GHOSTMODLEAFDATEPOKEMON:
    menu:
        "Ivysaur.":
            $ GHOSTMODLEAFDATELASTSMALLTALK = "pokemon"
            leafdate @happy "Ivysaur's an amazing partner. I was worried that my school-assigned starter might be a bit tricky to train, you know?"
            leafdate @happymouth "That would be really difficult, since a large part of our final grade is based on how our starter is doing."
            leafdate @happy "But Ivysaur's extremely calm! I never really have to worry about him going off on his own or doing something crazy."
            leafdate @sadbrow happymouth sweat "Actually, he might be {i}too{/i} calm... he emits this scent, sometimes, that makes me really sleepy..."

        "Helioptile.":
            $ GHOSTMODLEAFDATELASTSMALLTALK = "pokemon"            
            leafdate @sadbrow happymouth sweat"Helioptile's been a bit antsy, recently. She was a gift from my parents, a few years ago."
            leafdate @happymouth "She wasn't the first Pokémon I ever had, but she was one of the first. So I've been training her for a long time... I think she wants to evolve."
            leafdate @angry "But where are you supposed to find a Sun Stone in Kobukan? Kobukan puts massive fees on stones shipped across the border, too."
            leafdate @sadbrow happymouth sweat "They don't want to disrupt their own tiny mining industry, I guess..."

        "Jigglypuff.":
            $ GHOSTMODLEAFDATELASTSMALLTALK = "pokemon"
            leafdate @happy "Jigglypuff is an absolute angel. She's the easiest Pokémon I've ever trained. It's like she's been trained before!"
            leafdate @sadbrow happymouth sweat "Although... just between you and me... Jigglypuff aren't very strong..."
            leafdate @happy "But she still does her best! And we never would have made it back to Kobukan without her, so I'm never boxing her!"

        "Drampa.":
            $ GHOSTMODLEAFDATELASTSMALLTALK = "pokemon"
            $ drampasex = GetTrainerTeam("Leaf", "Drampa").Gender
            $ drampapronouns = "He" if drampasex == Genders.Male else "She"
            $ drampapronouns2 = "him" if drampasex == Genders.Male else "her"
            leafdate @happymouth "Oh, Drampa! Of course. [drampapronouns]'s relatively new, so I forget, sometimes."

            red @confused "New?"

            leafdate @happymouth "Yeah, I found [drampapronouns2] on Springsday. [drampapronouns] wasn't in one of the eggs, but I think [drampapronouns.lower()] came out of the mountains when [drampapronouns.lower()] heard people celebrating."
            leafdate @happymouth "[drampapronouns] found an egg, which [drampapronouns.lower()] was protecting from Wally... but I convinced [drampapronouns2] that finding and taking care of eggs was just part of the day, and I think that satisfied [drampapronouns2]."
            leafdate @happymouth "After Wally took the egg away, the Drampa came with me."

            red @confused "Wally took an egg? Which was it?"

            leafdate @happymouth sadbrow "It was a Budew egg. I... didn't have the heart to tell him that you can find Budew really easily in the fields..."

        "Dratini.":
            $ AddEvent("Leaf", "GetDratiniInfo")
            $ GHOSTMODLEAFDATELASTSMALLTALK = "pokemon"
            $ dratinisex = GetTrainerTeam("Leaf", "Dratini").Gender
            $ dratinipronouns = "He" if dratinisex == Genders.Male else "She"
            $ dratinipronouns2 = "him" if dratinisex == Genders.Male else "her"
            $ dratinipronouns3 = "his" if dratinisex == Genders.Male else "her"
            leafdate @happymouth "Well, Blue's training [dratinipronouns2] right now. It's frustrating, but Blue's doing a much better job with [dratinipronouns2] than I ever did."
            leafdate @angry "[dratinipronouns] just had such a strong attitude, like [dratinipronouns.lower()] wouldn't even try to battle foes [dratinipronouns.lower()] didn't think were worth [dratinipronouns3] time, and [dratinipronouns.lower()] got in fights with Bulbasaur all the time."

            pause 0.5

            leafdate @sad "Actually... Dratini was one of my first-ever Pokémon. But based on what Yellow and Blue have told me, [dratinipronouns.lower()] doesn't seem to miss me at all. That makes me a bit sad..."
            leafdate @happy "But I guess if [dratinipronouns.lower()]'s getting the training [dratinipronouns.lower()] needs, it's for the best. This is just a temporary thing, after all."

            red @confused "Hey, didn't Janine ask you to stay back one time to talk about your Dratini with you?"

            leafdate @happymouth "Oh, you remember that? Yeah, she did! It was so weird. She just looked at [dratinipronouns2] really intently, examined [dratinipronouns3] scale patterns, checked behind [dratinipronouns3] ear-fins..."
            leafdate @happymouth "It seemed she had a lot of experience handling Dratini. I don't know what she was looking for, but she seemed surprised at the end of it."

            redmind @thinking "Huh. Wonder what that's about..."

        "Let's talk about something else." if (GHOSTMODLEAFDATELASTSMALLTALK == "pokemon"):
            jump leafdatedialogue #return to main menu

jump GHOSTMODLEAFDATEPOKEMON    
#jump leafdatedialogue

label aftersmalltalkleafdate:

hide leafdate with dis

leaf @happy "What kind of 'serious talk' did you want to have? I'll try not to make any jokes."

red @talking2mouth "Okay. So, this is about something you mentioned a while ago, and it's kind of been occupying a spot in my head, bothering me ever since."

pause 0.5

leaf @sadbrow talkingmouth "Alright. I'll answer it, truthfully, whatever it is."

red @talking2mouth closedbrow "Okay."

pause 1.0

show leaf surprisedbrow frownmouth with dis

red @confused "Is it true that everyone at this school pads?"

pause 1.0

leaf angrybrow angrysmilemouth @angry "You dick! You said we were going to have a {i}serious{/i} conversation!"

pause 1.0

leaf -angrybrow -angrysmilemouth @happy "Okay, in retrospect, yeah, that's pretty funny. Thanks for lightening the mood."
leaf @talkingmouth "For real, though, what is it?"

if (HasEvent("Leaf", "AcceptedConfession")):
    red @talking2mouth "Have you dated before?"

    leaf @happy "Ah, immediately checking the quality of the merchandise, huh?"

    red @surprisedbrow talking2mouth "Wow, that's an {i}incredibly{/i} sexist way of putting it."

    leaf @angry "Huh? Who said only men could be sexist? You saying I can't be sexist because I'm a woman? That's sexist."

    pause 1.0

    red @unamusedbrow talking2mouth "I give up."

    leaf @sad "Aw, come on, at least put up a bit of a fight..."

    red @confused "Are you going to answer the question?"

else:
    red @talkingmouth "...I know you wanted this to be a date. But, I have to wonder... have you ever dated before?"

    red @sadbrow talkingmouth "I feel like you know what you're doing, but at the same time... don't."

pause 1.0

leaf @closedbrow talkingmouth "My... first crush was a girl named Cindy."
leaf @talkingmouth "She brought her lunch to school in a Lance lunchbox. I thought that lunchbox was the coolest thing ever."
leaf @sadbrow talkingmouth "This was before Lance was even the Kanto champion. He was just a popular, strong, trainer. Kinda obscure."
leaf @happy "Cindy was always on the cutting edge of things."

pause 0.5

leaf @talking2mouth "...That didn't work out, though. Also, I never talked to her, so, um, I didn't really give it a chance."

red @confused "Do you still... uh, I mean... women?"

leaf @closedbrow talkingmouth "I mean, maybe if Rosa was an option?"

if (HasEvent("Leaf", "PolyAlright")):
    leaf @closedbrow talkingmouth "Then, in fourth grade... oh, wait, I told you this, didn't I?"

    red @talkingmouth "Yeah, but tell me again."

else:
    leaf @talkingmouth "Then, in fourth grade..."

leaf @closedbrow talkingmouth "I had two boyfriends. Miles and Evan."

red @happy "Ooh? Well, weren't you a man's lady."

leaf @sarcastic "Huh?"

red @talkingmouth "You know, man's lady. Like, 'ladies' man', but in reverse."

leaf @closedbrow frownmouth "Hmm..."
leaf @talking2mouth "Shouldn't it be 'Men's' Lady', though? Because 'ladies'' is the plural possessive of 'lady,' so we should use the plural possessive for 'man', too."

red @surprised "Oh, yeah, you're right. Huh."
red @happy "Anyway, you were talking about your grade-school harem?"

leaf @talkingmouth "That's a hell of a way to put it. But yeah, we had a thing."
leaf @talkingmouth "We would hold hands together. Swap the parts of our lunch we didn't like. Sit in the same tree during recess."
leaf @talking2mouth "We hadn't really started kissing when it ended, but... I think we were going to."
leaf sadbrow frownmouth @talking2mouth "We'd... {i}just{/i} started to understand what our relationship was about, when..."

if (GetRelationshipRank("Leaf") > 0):
    redmind @thinking "Cinnabar Island..."

else:
    leaf @sadbrow talkingmouth "It probably adds some context to this story if I tell you I lived on Cinnabar."

    red @surprisedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
    red @sadbrow talking2mouth "Oh. Oh no."

leaf -sadbrow -frownmouth @talking2mouth "So... that one also didn't work."
leaf @closedbrow talking2mouth "Evan and I had started to discuss... what, exactly, we were... and we were going to talk to Miles about it, too..."

pause 0.5

leaf @sadbrow talking2mouth "But I put it off. Just a week. But that week changed everything."

pause 1.0

leaf @closedbrow talkingmouth "Guess I... didn't really learn my lesson, huh."

red @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

red @talkingmouth "Tell me about them."

leaf @surprisedbrow frownmouth "Hm?"

red @sadbrow talkingmouth "It sounds like they were really important to you. I know how it is, with childhood friends. Even if things change, even if years pass, you still miss them."
red @happy "So tell me about them. You probably don't have many chances to tell people about your grade-school harem, right?"

leaf @sarcastic "You'd be surprised. It's, like, the second-most-common thing I open conversations with."

red @sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."

leaf @surprised "Oh, okay, we're being serious now."

pause 1.0

leaf @talkingmouth "Miles was a know-it-all. He called {i}himself{/i} a Super Nerd. I don't remember what his first name was... but his last name was 'Miles', because he thought it sounded cooler than his first name."
leaf @closedbrow talkingmouth "Evan was a shy boy, but he loved nature, loved the outdoors. He used to take us camping. We'd spend hours wading in the water at the beach, while Miles hid from the sun underneath his umbrella."

pause 1.0

leaf @talking2mouth "And that was... the closest thing to a date I've had before right now."

if (not HasEvent("Leaf", "AcceptedConfession")):
    leaf @sadbrow talkingmouth "Which is pretty sad, since this is pretty explicitly not a date."

red @talking2mouth "...I'm not great with numbers, but shouldn't fourth grade have been... ten or so years ago?"

leaf @closedbrow talking2mouth "Closer to nine, but yeah."
leaf @sadbrow talkingmouth "...And I don't have an excuse for that, really. I mean, I'm not totally blind to my, uh, my advantages..."
leaf @closedbrow talkingmouth bigblush "Namely that I'm gorgeous, smart, and rich."

red @closedbrow talking2mouth "And modest."

leaf @talking2mouth "But... I never really tried reaching out until here in Kobukan."
leaf @sadbrow talking2mouth "After Cinnabar... my family moved to Goldenrod, where I attended a girls' school until I went to Kobukan."
leaf @closedbrow talkingmouth "I guess that might have stopped me from dating a bit more than some other high school. But it definitely wasn't a hard and fast stop."
leaf @sadbrow talkingmouth "No, that's just... on me. Sometimes people would ask me out, or would show some sort of interest."
leaf sadbrow frownmouth @sad "But I... I found an excuse. I always found an excuse to avoid it."

pause 1.0

show leaf surprisedbrow frownmouth with dis

red @talking2mouth "...Well, you've gotten over that."

leaf -frownmouth sadbrow @talkingmouth "How do you figure?"

if (HasEvent("Leaf", "AcceptedConfession")):
    red @happy "We're dating now."

    leaf @sadbrow talking2mouth "After a month of delays, and only because you pulled me out of my bedroom."

else:
    red @sadbrow talking2mouth "You did everything you could to make this a date without actually obtaining my consent to be dated."

    leaf @closedbrow talking2mouth "...I guess. Still took me a month to sort it out, though."

red @talkingmouth "Leaf. You did it. There were difficulties. But you {i}did{/i} do it."
red @happy "Give yourself some credit. You can't improve if you always ignore the progress you make."

leaf sadbrow neutralmouth "{w=0.5}.{w=0.5}.{w=0.5}."
leaf @talkingmouth "Look, [first_name]--"

show leaf surprisedbrow:
    xpos 0.5 xzoom 1
    ease 0.3 xpos 0.33 xzoom -1

show melody on with vpunch:
    xpos 0.66 xzoom -1

melody @talkingmouth "Yo."

leaf angrybrow frownmouth @angry "Melody!"

melody bubblemouth @talkingmouth "Leaf. [melody_name]."

leaf @talking2mouth "What are you doing here?"

melody -bubblemouth @talkingmouth "For the ambience."
melody @talkingmouth "Any other questions I can answer for you?" 

leaf @angrybrow talking2mouth "Why are you here? {i}Now?!{/i}"

melody @talkingmouth "I felt a spiritual calling."

pause 0.5

melody @talkingmouth "Also, you're in the makeout chair."

leaf @surprised "What?"

melody @talkingmouth "Every Wednesday, I'd meet my boyfriend at this café, we'd sit at this table, he'd sit in the chair you're sitting in now, and after I had enough sugar in me, I'd sit on his lap and we'd make out."
melody @talkingmouth "Check the back."

show leaf:
    xpos 0.33 xzoom -1
    ease 0.5 xpos 0.37 xzoom 1

pause 0.5

leaf @talking2mouth "There's a heart carved there, and it says 'MxD' there..."

show leaf:
    xpos 0.37 xzoom 1
    ease 0.5 xpos 0.33 xzoom -1

pause 0.5

show leaf:
    xpos 0.33 xzoom -1

leaf @angrybrow talking2mouth "Are you trying to get me to leave?"

melody @talkingmouth "No. Just kind of sad that the makeout chair isn't being made out in, anymore. Your generation has no respect for the old traditions."
melody @talkingmouth "What about you, [melody_name]? Going to be a man about it?"

if (not HasEvent("Leaf", "AcceptedConfession")):
    red @angrybrow talking2mouth "This isn't a date."

    melody @talkingmouth "Clearly. You didn't even order the couples' float."
    melody @talkingmouth "My recommendation, by the way. Don't get the chocolate syrup. It gives you gas, which ruins the after-date experience."
    melody @closedbrow talkingmouth "Unless... you're into that. I feel like you're probably into that."

    red @angry "I--"

    melody @talkingmouth "Please don't tell me anything more about your weird kinks."

else:
    red @talking2mouth "I think we're operating off of very different definitions of 'man.'"

    melody @talkingmouth "'No' is fewer words.'"

melody @talkingmouth "Anyway, I hate to kick you out, but it's getting late."

redmind @thinking "Huh? Is it really..."

narrator "You look outside the window. To your surprise, it really {i}is{/i} getting dark."

leaf @talking2mouth "Wait, you work here?"

melody @talkingmouth "Not all of us have fossil money, Green. Yeah, I work here."

red @closedbrow talking2mouth "I would have thought your uncle would give you all the money you need."

melody @angry "Phobos gave me an {i}opportunity.{/i} Everything else, I earned."

red @sad2eyes angryeyebrows talking2mouth "Cheren {i}also{/i} said he earned everything he has. So did Blue. I wonder why--"

melody @talkingmouth "Okay, I don't have time to unpack all these proper nouns you're dropping on me. Just get up and go. It's closing time."

Character("{color=#34a59a}???{/color}") "\"Excuse me, this establishment does not close until 8 PM. It is only 7:47 PM.\""

melody @closedbrow talkingmouth "{size=30}God.{/size}"
melody @angrymouth angrybrow "Look, Karen, you don't--"
melody @surprisedbrow talking2mouth "Hm?"

show leaf:
    xpos 0.33
    ease 0.5 xpos 0.25

show melody:
    xpos 0.66 xzoom -1
    ease 0.5 xpos 0.5 xzoom 1

show erika with dis:
    xpos 0.75

erika surprisedbrow frownmouth @happybrow talkingmouth "I really do not mean to cause any sort of bother, but is it not factual that this establishment has advertised itself--"

melody @talkingmouth "Stop yapping. You're giving me a headache. Just {i}say{/i} whatever you're going to say."

pause 0.5

erika angrybrow @talkingmouth "Er... my intent... which I was planning to convey summarily, is..."

show melody:
    xzoom 1
    ease 0.5 xzoom -1

melody @talkingmouth "Okay, you're taking too long. I'm kicking these two out right now."

erika @angry "Pray stay your hand!"

show leaf surprisedbrow frownmouth
show melody surprisedbrow
with dis

show melody:
    xzoom -1
    ease 2.0 xzoom 1

melody bubblemouth @talkingmouth "...'Pray stay my hand'?"

erika @talkingmouth "By which I mean kindly allow them to stay until the established closing hours of this business."

leaf @sadbrow talkingmouth "Hey, Erika, I appreciate it, but it's not that big a deal..."

erika @closedbrow talking2mouth "A business enterprise lives and dies by the promises it makes, and its ability and willingness to fulfill said promises."
erika @angry "If you've any passion for this job, you ought not to discard this café's doctrine so easily!"

melody @talkingmouth "...Uh, yeah, I don't. You think {i}anyone{/i} baristas because they're passionate for it?"

erika @talking2mouth "Then you should not be performing a job you have no passion for! There are alternative avenues!"

red @closedbrow talking2mouth "...Oof."

melody @talkingmouth "Okay." 

show leaf -surprisedbrow frownmouth
show melody -surprisedbrow -bubblemouth
with dis

melody @talkingmouth "Now, it's, like, ten minutes 'til closing. Do you still have some moral objection to me closing a bit early, so I can clean up sooner, and head back when it's not completely {i}pitch{/i} black?"

erika @talkingmouth "As a matter of fact, I do. In fact, given your impolite conduct toward me and my Battle Team teammates..."
erika @angrybrow talkingmouth "I wish to speak to your manager."

melody @talkingmouth "...What did Leaf say your name was, again? Erika? Hold on, there's something here..."

pause 1.0

melody @talkingmouth "Erikaren. There we go."

erika @surprised "That is not my name!"

melody @talkingmouth "Whatever you say, Erikaren."

redmind @poutmouth sad2eyes sadeyebrows "Don't laugh, don't laugh, don't laugh..."

erika @surprised "I... I...! Why are you acting in this fashion? What have I done to grievance you in this way?"

melody @talkingmouth "Waltzing in fifteen minutes before closing time is one. Trying to complain to the manager is another one. And, uh, no, you cannot speak to my manager."
melody @talkingmouth "He isn't even here, anyway."

erika @angrybrow frownmouth "[ellipses]"
erika @talkingmouth "Very well. Then I am afraid I will have to make a phone call to remedy this situation."

melody @talkingmouth "Knock yourself out."

narrator "You awkwardly begin to get up, given you never really had a problem with leaving the café in the first place, but Melody puts out a hand, indicating you should stay seated."

melody @talkingmouth "Hold on. Don't you want to see where this goes?"

red @sad2brow talking2mouth "...Not really."

leaf @talking2mouth "It's like a trainwreck... I can't look away."

narrator "Erika pulls out a screenless mobile phone, then gingerly inputs a number into it, focusing intently on typing out the number. A moment later..."

Character("Phone") "\"Mistress Tamamushi. Please state the nature of your emergency.\""

erika @angrybrow talking2mouth "I wish to speak to my father."

Character("Phone") "\"{size=20}What? She wants to... no, we don't have a protocol for this.{/size} Apologies, Mistress. The Master is not accepting phone calls at this time.\""

erika @angrybrow talking2mouth "Be that as it may, I must insist."

Character("Phone") "\"{size=20}No, she's insisting. What do we--well I have to say {i}something!{/i}{/size} Apologies, Mistress. The Master specifically requested that all calls, regardless of origin, be denied.\""
Character("Phone") "\"We can transfer you to your stepmother--perhaps she would be able to allay your concerns?\""

erika winkeyes sweat @surprised "Oh! No, please do not--"

Character("Phone") "\"{i}¡Mi hermosa niña!{/i} Oh, how wonderful it is to hear from you again! Tell me, how are you doing at school? Have you made many friends, yet? How are your classes progressing? Top marks, as always?\""

pause 1.0

Character("Phone") "\"Erika? {i}¿Hija?{/i} Are you there?\""

erika -winkeyes -sweat @closedbrow talking2mouth "Yes... Stepmother."

pause 0.5

Character("Phone") "\"...Beloved, you know you may call me by my name?\""

erika @angrybrow talking2mouth "I wish to speak to Father."

Character("Phone") "\"Oh. {w=1.0}Of course. {w=0.5}I understand. {w=0.5}He is not taking calls at the moment, but I will walk you into his office.\""

pause 0.5

leaf @sadbrow talking2mouth "{size=30}We... really don't need to be here for this.{/size}"

melody @talkingmouth "Shut up and enjoy the show. This is better than an episode of {i}Undella Bay.{/i}"

Character("Phone") "\"{size=30}What? What are you interrupting me for? Hm? Erika? What does she want? {w=0.5}Well, why didn't you ask her? {w=0.5}...Fine, fine! I'm almost done with work for the day, and was hoping to relax...{/size}\""
Character("Phone") "\"Okay, my beloved. Your father will hear you now. ...Oh! It appears he has a few more papers to handle, at first. Do you... wish to talk with me any further...?\""

erika @closedbrow talking2mouth "No."

Character("Phone") "\"...Okay. You are always welcome to call me. {i}Adiós.{/i}\""

melody @talkingmouth "I'm thinking... some Paldean model, a gold digger? Daddy Erika's got some of that 'has a trophy wife' energy, don't you think?"

red @sadbrow talking2mouth "We just want to leave."

melody @talkingmouth "You had your chance. You let Erikaren fight for you, now you're locked in your seats until the curtain falls."

erika -frownmouth @talkingmouth "Father? Are you there...?"

Character("Phone") "\"...Harrumph! Yes, yes, I'm here. Now, what is it? Out with it. I'm very busy right now.\""

erika @talkingmouth "It's been too long since we've spoken, Father. Perhaps we--"

Character("Phone") "\"Oh, enough of that small talk! Does Devereaux's judgment of such things escape you?\""
Character("Phone") "\"'Small talk is a poison most afflict'd, a breath of death to deprive intellectuals of the benefits of higher conversation.'\""
Character("Phone") "\"I've no time to tarry about on such mediocre matters! Out with it, Erika!\""

erika @talkingmouth "I... yes. Apologies."
erika @closedbrow talkingmouth "I have been insulted most grievously, Father."

pause 1.0

show erika surprisedbrow frownmouth with dis

Character("Phone") "\"Oh, is this about that matter of that Esper you had intentions for?\""

erika -surprisedbrow -frownmouth @surprised "N-no, father! He... was not an Esper! And I most certainly did not have a crush on him!"

Character("Phone") "\"I should hope not! You know such things are beneath you, beneath our family. 'Keep fast thine course, stray not from the path that destiny hath laid afore.'\""

erika @closedbrow talking2mouth "'Lest your steps shall falleth betwixt the privilege of surety and sink into undercharted soil, to be stained.' Yes, of course. I've no such delusions."

Character("Phone") "\"Then what is the manner of this insult?\""

erika @surprised "I have been called... 'Erikaren!'"

Character("Phone") "\"...\""
Character("Phone") "\"This is a grave insult indeed. Who spoke this insult? Who do they work for?\""

erika @talkingmouth "It was..."

pause 1.0

melody @talkingmouth "Melody. I work for, uh, the Inspira Pokécafé."

erika @happy "Thank you."
erika @angrybrow talkingmouth "Melody, who works for the Inspira Pokécafé."

Character("Phone") "\"I shall see to it this 'Melody' never holds employment within that business again! I will make her rue the day she crossed the Tamamushi family! I will blot her bloodline from ever--hold on, what was her last name?\""

erika @talkingmouth "What was your last name?"

melody @talkingmouth "Nunya. Of the Shamoutian shipping conglomerate, Nunya Business."

erika @talkingmouth "'Nunya', Father. Of Nunya Business."

Character("Phone") "\"...\""

show erika surprisedbrow frownmouth with dis

Character("Phone") "\"Stupid child. Waste no more of my time.\""
Character("Phone") "\"{i}*Click.*{/i}\""

erika sadbrow frownmouth @talking2mouth "Oh..."

melody @talkingmouth "And that's why you leave when the barista says they're closing. [melody_name], Leaf, it's been {i}a pleasure{/i} having you here. Actually buy something next time."

pause 0.5

melody angry "Time to go! Chop chop!"

scene blank2 with splitfade

$ location = "school"

narrator "You and Leaf quickly make your way back to your dorm, the bizarre display between Erika and Melody replaying over and over in your minds, as you try to make sense of whatever just happened."

pause 1.0

leaf night @talking2mouth "...You know, I planned for us to go shopping before dinner."

red night @confused "Oh, yeah?"

leaf @talking2mouth "We'll have to do that next time."

red @happy "You got a date in mind?"

leaf @sadbrow talkingmouth "For what it's worth."

pause 1.0

leaf @talking2mouth "But can we talk about Erika for a second?"

red @surprised "Oh, no, I'm totally with you."

if (GetRelationshipRank("Erika") > 0):
    red @confused "Like, she told me she had some family issues, but... {i}geez!{/i}"
else:
    red @confused "Like, I think we could have guessed she might have had some family issues, but... {i}geez!{/i}"

leaf @sarcastic "Geez is right. I think I could even forgive her for trying to kick you from the Battle Team, after hearing all {i}that.{/i}"

red @unamusedbrow talking2mouth "Well, I'm sure she's very glad {i}you're{/i} willing to forgive her for something she did to {i}me{/i}."

leaf @flirtbrow blush talkingmouth "Aren't I gracious?"

red @closedbrow talking2mouth "Outrageous, more like."

leaf @talkingmouth "Then you're going to be pretty confused in two to three turns."

pause 1.0

red @confused "If you're the outrageous one, though, shouldn't {i}you{/i} be--"

leaf @angry "It was a joke."

red @closedbrow talking2mouth "Alright, alright."

pause 1.0

leaf @talking2mouth "I know this wasn't worth the wait. But... I hope you enjoyed it."

if (HasEvent("Leaf", "AcceptedConfession")):
    red @happy "It wasn't really a wait. I got to hang out with you every day."

    leaf @happy "You're sweet."

    scene relichall_B 
    show leaf blush at night
    with splitfade

    pause 1.0

    leaf @talking2mouth "So... you want to do another one of these?"

    red night @talkingmouth "Tell you what. I'll invite {i}you{/i}, next time."

    leaf @sadbrow talkingmouth "...Okay. I, uh... hope you do."

    pause 0.5

    leaf @bigblush talkingmouth "We're almost back to the dorm..."

    menu:
        ">Lean in for a kiss":
            $ AddEvent("Leaf", "TryToKiss")
            $ ValueChange("Leaf", -1, 0.5, False)

            show leaf surprisedbrow frownmouth:
                ypos 1.0 zoom 1.0
                linear 0.2 ypos 0.9 zoom 0.9

            leaf @surprisedmouth "{size=30}Eep!{/size}"

            pause 1.0

            red @confused "...Okay, ouch."

            leaf sadbrow @sadmouth "I'm... I'm sorry, I..."

            red @closedbrow talking2mouth "It's alright. Sorry. I get I was moving a bit fast."

            show leaf surprisedbrow frownmouth:
                ypos 0.9 zoom 0.9
                ease 0.5 ypos 1.0 zoom 1.0

            leaf @sadbrow talkingmouth "I don't... {i}not{/i} want to. But I need..."

            red @sadbrow talking2mouth "Time. It's fine. I understand, really."

            pause 1.0

            $ ValueChange("Leaf", 2)

        "We sure are.":
            leaf @talkingmouth "So... hypothetically... is this the part in the movies where we would kiss?"

            if (GetRelationshipRank("Rosa") > 1):
                red @happy "I've watched a {i}bunch{/i} of Rosa's movies, ever since I started hanging out with her, so I feel pretty confident that the answer is yes."

            elif (GetRelationshipRank("Rosa") > 0):
                red @happy "I've watched a few of Rosa's movies, since I've been hanging out with her, and most of them would indicate the answer is yes."

            else:
                red @talkingmouth "You're the movie buff. You tell me!"

            leaf @sadbrow bigblush talkingmouth "W-well... I mean, those are just movies, so... I wouldn't take them as gospel, heh heh!"

            redmind @sadbrow frownmouth "Guess... she needs time. Which is entirely fair."
            redmind @happy "I've got all the time in the world."

    leaf @sadbrow talkingmouth "Thank you."

else:
    red @talkingmouth "Yeah. I did. Thanks for not, uh, tying me to a chair and refusing to feed me until I dated you."

    leaf @closedbrow talking2mouth "{size=30}But would that {i}work...?{/i}{/size}"

    red @unamusedbrow unamusedmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    leaf @closedbrow talkingmouth "Keeping that one in the back pocket, then."

scene blank2 with splitfade

if (GetRelationshipRank("Leaf") < 1):
    $ RelationshipRankUp("Leaf", "True Friend", 1)

jump day010527