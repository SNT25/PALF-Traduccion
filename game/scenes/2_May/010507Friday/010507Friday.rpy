label day010507:

call calendar(1) from _call_calendar_32
$ calDate = calDate.replace(day=7, month=5, year=2004)

$ timeOfDay = "Morning"
show morning at vspaz

pause 3.5

$ renpy.music.queue("Audio/Morning_ambience.ogg", channel='music', loop=True, fadein=1.5, tight=None)

scene bedroom
show screen currentdate
with transeye2

pause 1.0

narrator "You awake to feel a weight on your chest."

redmind @thinking "Oh, great. Did the stress get to me? Time for a sheer heart attack?"

$ renpy.music.play("Audio/Pokemon/pikachu_sad.ogg", channel="altcry", loop=None)
pikachu yawn "Pi-ka..."

redmind @happy "Oh, nope. Just a fat Pikachu."

pause 1.0

redmind @thinking "Actually..."

red @talkingmouth "Buddy, have you been losing weight? You seem more fit than you used to be. Are these actual muscles?"

$ renpy.music.play("Audio/Pokemon/pikachu_sad.ogg", channel="altcry", loop=None)
pikachu yawn "Pi-ka..."

redmind @thinking "Hm. I guess he {i}has{/i} been battling a lot more than he used to."

scene kitchen 
show leaf flirtbrow frownmouth
with splitfade

pause 1.0

leaf @talking2mouth "Mmmmorning."

red @happy "Not a morning person?"

leaf @talking2mouth "Bleh. Want some coffee?"

pause 1.0

red @happy "Nah. The only thing I need to get me going in the morning is a brisk run."

leaf @surprised "Wow. I literally hate you so much right now."

red @sweat happy "Heh..."

pause 1.0

if (HasEvent("Leaf", "Splashed")):
    red @closedbrow sweat talking2mouth "Sorry about splashing water on you yesterday."

    leaf @angrysmilemouth "I mean, I forgive you, but I'm also going to hold it against you forever."

    red @sweat talking2mouth "That's not what forgiveness is."

leaf @talking2mouth "Whatever. You have a plan for Dawn?"

show leaf surprisedbrow with dis

red @closedbrow talkingmouth "No. But Lance says he's going to talk to me about... something I could do."

leaf @talking2mouth "Well, that woke me up."
leaf -surprisedbrow @talking2mouth "You're friendly with Lance now, huh?"

red @closedbrow talking2mouth "I think he respected that I came back. {w=0.5}...Which I guess I have you to thank for."

leaf @talking2mouth "More like your Mom. You've called her to say how awesome she is, right?"

red @talkingmouth "Of course."

leaf @talking2mouth "Next time you talk to her, tell her that her Jigglypuff is a badass."

red @sweat happymouth "I might word it differently, but sure."

pause 2.0

leaf @talking2mouth "{i}Sip.{/i}"

pause 2.0

leaf @talking2mouth "Alright. You need to be at the Battle Hall by... ten, you said? Then let's do some quick studying or battling first. Everyone else is ready in the main room." 
leaf @talking2mouth "This'll probably be the last chance you have to upgrade your team before you have to face Dawn."

red @closedbrow frownmouth "Right."

$ attemptedtoleave3 = False

label preqq3:

scene blank2

$ pretype = None

menu:
    ">Study a type":
        call screen studyfocus
        $ selectedtype = _return 

        hide blank2 with dis

        if (selectedtype == "Back"):
            jump preqq3

        redmind @thinking "With everyone studying together, I should probably be able to increase my proficiency by one."

        menu:
            "That's fine.":
                $ pretype = selectedtype

                $ IncreaseProficiency(selectedtype, 1)

                narrator "You and your new roommates crack open the books and pore over the readings you missed during your leave of absence."

                $ ValueChange("Leaf", 1, 0.2, False)
                $ ValueChange("Blue", 1, 0.4, False)
                $ ValueChange("Ethan", 1, 0.6)

                narrator "Bonds increased!"

            "Nevermind.":
                jump preqq3

    ">Train your Pokémon":
        $ aimlevel = AimLevel()
        $ expamount = math.floor(pow(aimlevel, 3) / 25)
        
        redmind @thinking "With everyone training together, I should probably be able to increase my Pokémon's experience by [expamount], if they're at level [aimlevel]."

        menu:
            "Let's do it.":
                narrator "You and your new roommates head out to the gym and throw your Pokémon at each other until everyone's good and warmed up for the upcoming battles."

                $ BattleTeamTraining()

                $ ValueChange("Leaf", 1, 0.2, False)
                $ ValueChange("Blue", 1, 0.4, False)
                $ ValueChange("Ethan", 1, 0.6)

                narrator "Bonds increased!"

            "Nevermind.":
                jump preqq3

    ">Leave the dorm alone" if not attemptedtoleave3:
        narrator "You'll need to do this soon, to meet Lance. There's no need to rush it."

        $ attemptedtoleave3 = True

        jump preqq3

scene suite
show screen currentdate
show blue frownmouth:
    xpos 0.2
show leaf:
    xpos 0.8
show yellow:
    xpos 0.6
show ethan:
    xpos 0.4    
with Dissolve(2.0)

ethan @talkingmouth "This might be the last time we see you before your battle with Daybreak, if Lance keeps you for a while."

yellow @talkingmouth "Right. Because you need to talk to Professor Oak before your battle, remember."

red @sweat talkingmouth "Can't forget."

blue @talkingmouth "And remember what I said about Dawn. If you play fair, you lose."

red @playfulbrow talking2mouth "Yeah. Got it. {i}Thanks.{/i}"

leaf @happy "Seeya!"

scene blank2 with splitfade

pause 2.0

scene stadium_empty
show lance closedbrow 
with dis

pause 2.0

lance @talking2mouth "You're here on time."

red @talkingmouth "This seemed pretty important to talk about."

lance -closedbrow "{w=0.5}.{w=0.5}.{w=0.5}."

lance @talking2mouth "I do not understand why you sometimes seem able to speak. And why sometimes you cannot."

pause 1.0

lance @talking2mouth "When I berated you the first time, I saw that same frozen fear in your eyes as I did yesterday. But now you speak as though we are 'chums.'"

pause 1.0

red @sadbrow talking2mouth "I don't get it, either."

pause 1.0

lance @sad2eyes talking2mouth "It's of no consequence."

pause 1.0

lance @talking2mouth "Rather, we are here to talk about how we could squeeze the slightest amount of victory out of your regrettable circumstance."
lance @sad2eyes sadeyebrows talking2mouth "It was a mistake on Janine's part not to sign you all up in separate districts, but... as advisor... it was my mistake to not remind her to."
lance @closedbrow talking2mouth "Foolishness on my part. I was distracted by my grudge against you."

pause 1.0

red @confused "Yeah... what's that about?"

lance @shadow angrybrow talking2mouth "I have {i}told{/i} you. You exist here through the kindness of others and luck. And you fritter this opportunity away through self-sabotage."

red @talking2mouth "You mean [pika_name]."

lance @talking2mouth "I do."

pause 1.0

lance @talking2mouth "When you were gone, Ms. Green asked me for the usage of my Dragonite. She wished to use it to retrieve you."
lance @sad2eyes talking2mouth "I denied her, obviously. I believed that your self-pity would not permit you to come back, even if someone made the effort to reach out."
lance @closedbrow talking2mouth "However, given the infinitesimal amount of respect I have for you, the significantly greater amount of respect I have for her, and the immense amount of respect I have for Janine, I have a proposal."

red @happy "Oh, that's great! Who's the lucky woman?"

pause 1.0

lance @confusedeyebrows playfuleyes talking2mouth "Do you think you're {i}charming,{/i} child?"

red @closedbrow talkingmouth "Sometimes."

lance @talking2mouth "Enough nonsense. As I denied Leaf the usage of my Dragonite before, I am willing to loan a different one to you, for the purpose of this one battle."

pause 1.0

red @surprised "What?"

lance @talking2mouth "I have talked with Dawn. I do not agree with Janine's insistence that she {i}not{/i} drop out, but as Janine is Captain, that is her call to make."
lance @closedbrow talking2mouth "The only way we preserve the Battle Team's reputation, then, is if you beat Dawn fairly, and she retires from the Battle Team before the final blow is dealt."

pause 1.0

lance @closedbrow talking2mouth "This, she has agreed to do."

red @sadbrow talkingmouth "That doesn't seem... fair."

lance @sad2eyes talking2mouth "All that matters is the {i}letter{/i} of the law. This is the ideal outcome for everyone. Most importantly, Janine."

red @angrybrow talking2mouth "Janine doesn't {i}want{/i} Dawn to drop out."

lance @angrybrow talking2mouth "Janine doesn't want to {i}have to ask Dawn{/i} to drop out."

red @angrybrow talking2mouth "You can't know that."

lance @angry "I was the girl's godfather. I was practically her uncle. She is absolute and determined, but will not go the last inch required to secure victory!"

red @angry "I think you're just saying that because you don't want the Battle Team's reputation ruined while you're advisor!"

lance @angry "Do you think I care about Kobukan's reputation? It's a {i}building!{/i} Filled with idealists, fools, and more money than any man needs!"
lance @closedbrow angrymouth "Do you think I care about my own reputation? I know what people say of me. They call me the Champion of failures. They say I don't know what a Dragon is!"
lance @angry "I seek to preserve nothing except Janine's reputation. {i}She{/i} is all I care about!"
lance @shadow angry "She deserves perfection. Not to be saddled with an incomplete victory, or, gods forbid, a {i}failure.{/i}" 
lance @angrybrow talking2mouth "For as much as you sabotage yourself, she has sabotaged herself even harder by recruiting {i}you{/i}!"

$ PlaySound("Pokemon/pikachu_angry3.ogg")
pikachu angry_4 "Pika!"

pause 1.0

lance @shadow sad2eyes talking2mouth "Shut up, rat."

red @shadow angrybrow talking2mouth "So that's how it is."

lance @talking2mouth "This drama is unnecessary. I am not asking for your opinion on this solution. I am telling you to take it."

pause 1.0

lance @talking2mouth "You will take my Dragonite. You will agree with Dawn to fight a one-on-one battle. You will use my Tera Orb to Terastallize my Dragonite into a Normal Type." 
lance @talking2mouth "You will command her to use Extreme Speed. Dawn's Altaria will faint. Dawn will deny ever being part of the Battle Team."
lance @closedbrow talking2mouth "And everyone will come out of this situation with the minimal amount of damage."

redmind @closedbrow frownmouth "This sounds... like a plan that is {i}likely{/i} to be successful. But..."

lance @talking2mouth "I have already talked with Dawn. She will agree to the one-on-one. She also knows that it is her role to lose. There will be no difficulty here."

pause 1.0

lance @shadow angrybrow talking2mouth "What's taking you so long? I am {i}giving{/i} you your victory. Once again, another is pulling you out of the fire. This {i}cannot{/i} be an unusual circumstance for you."

$ PlaySound("Pokemon/pikachu_sad2.ogg")
pikachu sad_2 "Pika...?"

pause 1.0

narrator "What {w=0.5}will {w=0.5}you {w=0.5}do?"

$ lanceplan = False

menu:
    ">Follow Lance's plan":
        lance @sad2eyes talking2mouth "Thank you for showing a modicum of sense."
        lance @angrybrow talking2mouth "There is one condition for the use of my Dragonite, however."
        lance @talking2mouth "You will leave your Pikachu with me."

        red @surprised "What?"

        lance @talking2mouth "I do not trust that you will not attempt to sneak your Pikachu into your team in some way or another. Only when I have it on my belt can I be certain you will follow the plan."

        red @angry "You want a {i}hostage.{/i}"

        lance @angrybrow talking2mouth "I want {i}certainty.{/i}"

        $ PlaySound("Pokemon/pikachu_sad.ogg")
        pikachu sad "Pika...?"

        menu:
            ">Follow Lance's plan":
                $ lanceplan = True
                
                red @sad2eyes sadeyebrows talking2mouth "I'm... sorry, [pika_name]. I don't think there's another way."

                $ PlaySound("Pokemon/pikachu_scared.ogg")
                pikachu sad "Pika? Pika."

                $ PlaySound("pokemon/ball sound.ogg")

                $ playerparty.remove(pikachuobj)

                show lance playfuleyes happymouth with dis

                pause 2.0

                narrator "You feel as though you've taken a dirty deal."

                lance @closedbrow talking2mouth "Well done. Perhaps we'll make a champion out of you, after all."

                red @angrybrow talking2mouth "Your Dragonite?"

                lance -happymouth -playfuleyes @closedbrow talking2mouth "Yes, yes. Don't be impatient."

                $ lancedragonite1obj = Pokemon("Dragonite", level=87, moves=[GetMove("Outrage"), GetMove("Extreme Speed"), GetMove("Draco Meteor"), GetMove("Earthquake")], item="Heavy-Duty Boots", ability="Multiscale", ivs=[31, 31, 31, 12, 31, 31], evs=[4, 252, 0, 0, 0, 252], nature=Natures.Adamant, gender=Genders.Female, teratype="Normal")

                $ playerparty.append(lancedragonite1obj)
                $ GetItem("Tera Orb")

                narrator "Dragonite joined your party. Lance handed you a Tera Orb."

                pause 1.0

                narrator "Lance looks at you with something akin to pride. You are filled with shame."

                if (lancedragonite1obj.Item != Item.HeavyDutyBoots):
                    narrator "However, his pride quickly fades into a scowl as he sees you've taken off the Dragonite's Heavy-Duty Boots."

                    narrator "He rolls his eyes and doesn't deign to acknowledge the blatant act of theft."

                lance @talking2mouth "With this one action, your victory has been guaranteed. As has the preservation of Janine's reputation."

                pause 2.0

                lance sad2eyes talking2mouth "Therefore, we have no reason to remain here. I take my leave of you."

                hide lance with dis

                pause 1.0

                narrator "You stand still for a bit, wrestling with whether you made the right choice. You inspect the Dragonite's Ultra Ball."

                pause 1.0

                narrator "It feels heavy in your hand."

            ">Back out":
                red @angry "You almost had me, Lance."

                red @angrybrow talking2mouth "No."

                jump rejectlance
                
    ">Reject Lance's plan":
        red @angrybrow talking2mouth "No."

        label rejectlance:
            show lance angrybrow shadow with dis

            pause 2.0

            narrator "Lance is silent. He stares at you, unmoving. You stare back, just as steadfastly."

            pause 2.0

            lance @talking2mouth "You, {w=0.5}stupid, {w=0.5}stupid, {i}child.{/i}"

            pause 2.0

            red @confused "That seemed uncalled for."

            lance @talking2mouth "This is selfishness. Selfishness and pride."

            pause 1.0

            lance @talking2mouth "Damn you."

            hide lance with dis

            narrator "You stand alone in the battle hall for a while."

            redmind @frownmouth "...When I'm Champion..."

            redmind @thinking "I'll never be like that."

scene blank2 with splitfade

pause 2.0

scene research with splitfade

pause 1.0

redmind @confusedeyebrows frownmouth "Where's--"

show oak surprisedbrow frownmouth with vpunch

oak @talkingmouth "Lad!"

show oak closedbrow frownmouth with dis:
    ease 0.3 ypos 1.2 zoom 1.3

narrator "Before you're even aware of what's happening, Professor Oak has swept you up into a tight hug."

red @surprised lightblush "S-Sam? What're you doing?"

pause 2.0

show oak sadbrow with dis

oak @talking2mouth "I'm so sorry, my boy. I can't imagine what it was like for you all this time."

show oak:
    ease 0.5 ypos 1.0 zoom 1.0
oak @closedbrow talking2mouth "I take full responsibility for what happened, and beg your forgiveness."
oak @angryeyebrows closedeyes talking2mouth "I know how much transparency and truth matters to you, and I've always tried to emulate that... I can never seem to get a firm grasp of when I {i}shouldn't{/i} be honest, though..."
oak @sadmouth "In any case, I clearly made a dreadful mistake asking you to keep this secret."

pause 1.0

oak @talking2mouth "Could you ever forgive me, lad?"

menu:
    "There's nothing to forgive.":
        oak @talking2mouth "No, no, there certainly is! And I aim to earn that forgiveness."

    "Of course, Sam.":
        oak @talking2mouth "Thank you, [first_name]. But you need not forgive yet. I aim to earn that forgiveness."

    "...Not yet.":
        oak @talking2mouth "Of course, of course. I aim to earn that forgiveness."

oak @closedbrow talkingmouth "Don't worry about a thing, my boy. I've already made preparations."

red @confused "Huh?"

oak -sadbrow -frownmouth @talkingmouth "Yes, I've already purchased a flight ticket back home. We can forget this whole awful business ever occurred."
oak @happy "And I have an 'in' with Director Cyrano of Blueberry Academy, just a few hundred miles away. He's all but guaranteed your admission. Why, you could even fly back to visit on weekends!"
oak @closedbrow talking2mouth "I'm still working on figuring out how we will explain your disappearance, but--"

red @surprised "Woah, woah, wait! Sam, I {i}just{/i} came back from Pallet Town!"

oak @surprised "I... beg your pardon?"

red @talkingmouth "I flew back to Pallet Town on Saturday."
red @sad2eyes talking2mouth "Leaf... actually came and got me on Tuesday. I just got back on Wednesday, two days ago."
red @sadbrow talkingmouth "I don't want to leave again."

pause 1.0

oak frownmouth @surprised "But... my boy. You must!"
oak @sad "Your secret has been exposed, my lad. They'll tear you apart for this. You'll be an outsider, and-- and--"
oak @sad "And... if it comes out that you're here only because of my favor, there will be a {i}valid{/i} reason to expel you! Never mind what might happen to my career."

red @sadbrow talking2mouth "Wait..."

oak @sad "Please, lad, don't misunderstand me. I am {i}absolutely{/i} not trying to 'get rid of you' because I'm worried that we'll be caught in our arrangement, or something of that nature."
oak @sad "You're a child. You don't understand how cruel these people will be to you. I don't want you to have to suffer that because I wanted answers."

red @sad "Sam... I've been here three days by now. Some people are upset, some are angry. But some people are in better places than before." 
red @closedbrow talking2mouth "I caused this. Not the whole thing, but I didn't help. Running away the first time was a dumb idea. I can't do it again."

oak @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
oak @talking2mouth "I'm so sorry, lad, but... I can't accept that. This is for your own good."

red @surprised "What?"

oak @talkingmouth "I'll pay your full enrollment and tuition at Blueberry. I shan't make this mistake again. I'll visit you as often as I'm able. You can call me whenever you want, for advice or... anything."
oak @angrybrow talking2mouth "But you {i}must{/i} leave Kobukan. You {i}must.{/i}"

red @sad "{w=0.5}.{w=0.5}.{w=0.5}."
red @sadbrow talking2mouth "I can't. This is my dream, Sam. And... I'm so thankful for you helping me get here. But I'm not going to let you drive me away."

pause 2.0

oak shadow angrybrow frownmouth @talking2mouth "Lad. You have no reason to be here."

red @surprised "Huh?"

if (not lanceplan):
    $ renpy.music.play("Audio/Pokemon/pikachu_confused.ogg", channel="altcry", loop=None)
    pikachu neutral_4 "Pika?"

oak @talking2mouth "You're here because I wanted you to be. And, now, you'll leave, because I want you gone."

if (not lanceplan):
    $ renpy.music.play("Audio/Pokemon/pikachu_angry1.ogg", channel="altcry", loop=None)
    pikachu angry "Pika!"

pause 1.0

oak tears @angrybrow surprisedmouth "Do you hear me, lad?! There is {i}nothing{/i} for you here! No friends! No future! {i}Nothing!{/i}"
oak @surprisedmouth "Give-- give me a single reason to keep you here! An excuse! A reason! {i}ANYTHING!{/i}"

if (not lanceplan):
    $ renpy.music.play("Audio/Pokemon/pikachu_angry2.ogg", channel="altcry", loop=None)
    pikachu angry_3 "Pika!"

pause 1.0

narrator "Your heart hurts."

pause 1.0

narrator "...But Sam has never been a good liar."

red @closedeyes tears talking2mouth "I know what you're trying to do, Sam. And it's not going to work. It's just going to--"

if (not lanceplan):
    show oak -shadow -tears surprised with dis

    $ renpy.music.play("Audio/Pokemon/pikachu_angry3.ogg", channel="altcry", loop=None)
    pikachu angry_4b "Pipipipipkakakakachu!"

    oak "Wait, what's [pika_name] doing?"

    narrator "You turn around to see [pika_name] standing next to a glass case with a few glowing shards of rock inside."

    oak @sadbrow surprisedmouth "W-wait! [pika_name], stop! Those are the meteorite fragments! You mustn't--"

    $ PlaySound("Pokemon/pikachu_angry3.ogg")
    $ PlaySound("shatter.ogg")

    stop music

    narrator "Before you have a chance to react, [pika_name] smashes the glass case and immediately swallows the meteorite shards."

    pause 3.0

    red @surprised "Shit."

    oak @surprised "Shit!"

    $ renpy.music.play("Audio/Pokemon/pikachu_happy1.ogg", channel="altcry", loop=None)
    pikachu happy_2 "Pi."

    red @talking2mouth "Crap, sorry. I think he thought you actually wanted a reason to keep me here, so--"

    oak surprisedbrow @talking2mouth "No, no, I understand that! But we need to induce vomiting, {i}immediately!{/i}"

    red @surprised "What?"

    oak sadbrow frownmouth @talking2mouth "[pika_name] just ate shards of rock covered in a constantly-shifting space-borne organism! If the rock doesn't tear up his insides, the bacteria could potentially make him deathly sick!"

    red @surprised "Crap! Uh, [pika_name]! Throw it up! Throw up! Now!"

    pause 1.0

    $ renpy.music.play("Audio/Pokemon/pikachu_confused.ogg", channel="altcry", loop=None)
    pikachu neutral_3 "Pika?"

    pause 2.0

    red @confused "He seems fine."

    oak @talkingmouth "...Perhaps the shards will remain stationary as long as he doesn't move...? I... I need to call Miriam."

    pause 1.0

    red @talking2mouth "...Sam."

    oak @surprised "Lad?"

    red @talking2mouth "What you were saying before..."

    pause 1.0

    oak @sadeyebrows sad2eyes talking2mouth "I'm... sorry. I meant none of it."

    red @closedbrow talkingmouth "{i}Sigh.{/i} {w=0.5}Yeah. I know."
    red @talkingmouth "But you need to be careful about what you say to people, Sam. That seriously hurt my feelings. If I didn't know you so well, I would have thought--"

    $ renpy.music.set_volume(0.3, channel="crowd3")
    $ renpy.music.play("Audio/crowd_cheer.ogg", channel='crowd3', loop=None, fadein=0.0)

    pause 1.0

    red @surprised "Shit! The Quarter Qlashes are starting!"

    oak @surprised "Oh... well, you must go, then! Just call [pika_name] back into his Poké Ball. Try to avoid using him in battle. We don't know what effects those shards might have on him, so we don't want to agitate them before a nurse can look at them."

    red @closedbrow talking2mouth "Good idea."

    $ PlaySound("pokemon/pikachu_angry1.ogg")
    $ PlaySound("pokemon/ball sound.ogg")

    red @talking2mouth "Okay, I have to go now. But we'll talk later, right?"

    oak @sadbrow talkingmouth "Y-yes, of course. And... I'm very sorry about... well, everything, lad."

    red @sadeyebrows talkingmouth "...Even the great Professor Oak has some things left to learn."

    scene blank2 with splitfade

else:
    pause 1.0

    red @talking2mouth "It's just going to hurt me."

    oak @talking2mouth "...As will everyone else."

    narrator "Your fist tightens around Lance's Dragonite's Poké Ball, which you still haven't attached to your belt."

    red @closedbrow talking2mouth "Whatever. I'm leaving."

    oak @sadbrow talking2mouth "[first_name]. Please. You must--"

    stop music fadeout 1.0

    scene blank2 with splitfadefast

    pause 1.0

    narrator "You feel... very alone."

pause 2.0

show noon at vspaz
$ timeOfDay = "Noon"

pause 3.5

stop music fadeout 1.5
show blank as firstblank behind blank2
show stadium_full behind blank2
show blank as secondblank behind blank2
$ renpy.music.play("Audio/Stadium_crowd.ogg", channel='crowd', loop=True, fadein=1.5)
$ renpy.music.play("Audio/Stadium_chant.ogg", channel='crowd2', loop=True, fadein=1.5)

$ renpy.pause(0.75, hard=True)

$ renpy.music.queue("Audio/Music/Indigo_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/Indigo_Loop.ogg", channel='music', loop=True, tight=None)

$ renpy.pause(1.0, hard=True)

hide blank2 with transball
$ renpy.pause(0.25, hard=True)
hide secondblank with dis

show stadium_full:
    subpixel True
    zoom 3.0 alpha 0.65 xalign 0.15 ypos 2600
    ease 1.25 alpha 1.0 xalign 0.0 ypos 3000
    xalign 0.85 alpha 0.65 ypos 2600
    ease 1.25 alpha 1.0 xalign 1.0 ypos 3000
    xalign 0.5 alpha 0.4 ypos 2400
    ease 1.0 alpha 1.0 zoom 1.0 ypos 1080

show lightbeam1 as beam1:
    pause 2.75
    zoom 0.6 alpha 0.0 yalign 0.9 xpos 0 rotate 40
    block:
        ease 0.25 alpha 0.5
    pause 0.3
    block:
        ease 1.0 rotate -40
        pause 0.5
        ease 1.0 rotate 40
        pause 0.5
        repeat
    
show lightbeam1 as beam2:
    pause 2.75
    zoom 0.6 alpha 0.0 yalign 0.9 xpos -300 rotate -40
    block:
        ease 0.25 alpha 0.5
    pause 0.1
    block:
        ease 1.0 rotate 40
        pause 0.5
        ease 1.0 rotate -40
        pause 0.5
        repeat

show lightbeam1 as beam3:
    pause 2.75
    alpha 0.0 yalign 0.8 xpos -400 rotate -40
    block:
        ease 0.25 alpha 0.6
    pause 0.2
    block:
        ease 1.0 rotate 40
        pause 0.5
        ease 1.0 rotate -40
        pause 0.5
        repeat
        
show lightbeam1 as beam4:
    pause 2.75
    alpha 0.0 yalign 0.8 xpos -1400 rotate 40
    block:
        ease 0.25 alpha 0.6
    block:
        ease 1.0 rotate -40
        pause 0.5
        ease 1.0 rotate 40
        pause 0.5
        repeat
        
pause 3.5

show lisia behind beam1 with dis

lisia @happy "Laaaaaadies and {i}gentlemen!{/i} Welcome to the third round of the two hundred and twenty-eighth annual Quarter Qlashes!"
lisia @xdbrow happymouth "The battles have been heating up with every round, and I'm sure that today, as we close out the first Quarter Qlash, we're about to see battles like we've {i}never{/i} seen before!"

$ PlaySound("crowd_cheer.ogg")

pause 1.0

lisia @happy "Yeah, let me hear those cheers! For the last round of this Quarter Qlash, it's me, the one and only Lisia, World Contest Champion, here to announce!"
lisia @talkingmouth "We're going to see a lot of familiar and powerful faces down there in the pit, this time, but I'm most excited to see the new faces! You might be seeing the first big battles of champions, ladies and gentlemen!"

$ PlaySound("crowd_cheer.ogg")

pause 1.0

lisia @happy "Awesome! Now, my team's advised me not to take any more audience comment after what happened yesterday, but..."
lisia @xdbrow happymouth "I'm sorry, Gabby, I just can't hold myself back! I really want to talk to the battlers!"

show stadium_full with vpunch 

$ PlaySound("crowd_cheer.ogg")

"\"Gabby\"" "\"Damn it, Liz!\""

show lisia:
    ease 1.0 xpos 0.25
    pause 1.0
    ease 2.0 xpos 0.75
    pause 1.0
    ease 2.0 xpos 0.25

lisia @talkingmouth "Hm..."
lisia @closedbrow frownmouth "What about... or maybe... oh, how about you!"

show dawn sadbrow frownmouth at rightside with dis

redmind @thinking "Oh, great. Lisia literally {i}couldn't{/i} find someone more camera-shy than Dawn."

lisia @happy "Hi~ya, battler! What's your name?"

dawn @talkingmouth "D-Dawn."

lisia @surprised "Wow! I actually have a friend with a daughter named Dawn. It can't be possible--are you {i}Johanna's{/i} daughter?"

dawn @closedbrow talkingmouth "...Yes. Yes, I am..."

lisia @happy "Wow! That's amazing! Johanna must be so proud of you."

dawn @sadmouth "{size=30}...No.{/size}"

lisia frownmouth @surprised "What?"

"\"Gabby\"" "\"{size=30}God damn it, not again...{/size}\""

dawn @talkingmouth "I'm... I'm going to lose... I'm here to lose..."

lisia @sadmouth "Aw, don't say that, sweetheart! All you need to do is believe in your Pokémon, and if you try your hardest, everyone can say they had a good time!"

dawn @sadmouth "No... no, you don't get it. I've been {i}told{/i} to lose. To just give up."

lisia @surprised "What?"
lisia @angry "Well, you don't have to listen to whichever jerk told you that! You just need to battle the best you can, and--"

stop music fadeout 1.5 channel "crowd"
stop music fadeout 1.5 channel "crowd2"
stop music fadeout 1.5

show stadium_full with vpunch

dawn @angry "{size=40}It's not that easy!{/size}"

pause 1.0

dawn @sad "It should be. But... nothing works. When you're weak, people beat you down, blame you for it, and say you disappoint them! When you're weak, nothing you do matters!"
dawn @angry "But when you're strong, people want you to take falls--to lose and make way for someone else! When you're strong, everything you do matters too much! You can't even have a Pokémon battle without some sort of message!"

lisia sadbrow @talking2mouth "...I know what you mean, Dawn."

dawn @sadbrow sadmouth "How can you? Everyone loves you, Lisia. My Mom would always say what Lisia would do in this situation. All she wanted was for me to be a contest star, but I..."

dawn @angrybrow sadmouth "I {i}never{/i} get to do what I want. {i}Never.{/i} I had to participate in contests because my mother was a famous coordinator. Then I had to be a battler because I was 'gifted' at it."
dawn @angrybrow angrymouth "Then I had to challenge the Sinnoh league, even though I {i}knew{/i} I wasn't ready! Then I had to enroll in Kobukan! Just because I lost to the best trainer in the world doesn't mean I needed to go back to school!"
dawn @angry "Then I was {i}forced{/i} into joining the Battle Team, then I was {i}forced{/i} into a situation that will ruin the Team's reputation, and now I'm being {i}forced{/i} to lose! Just once, I want--"

show lisia:
    ease 0.3 xpos 0.5

narrator "Lisia grabs Dawn's hand."

dawn @surprisedbrow frownmouth "{size=30}...What?{/size}"

lisia @sadbrow talkingmouth "...Finish what you were saying, Dawn. What do you want?"

dawn @closedbrow sadmouth "I just want... {i}for once...{/i} to battle without it meaning anything. To battle without having to win, or having to lose."

lisia @talkingmouth "And you don't think you can do that?"

dawn "{w=0.5}.{w=0.5}.{w=0.5}."

narrator "Dawn looks at you, and sighs."

dawn @sadmouth "No. No, I can't."

show lisia:
    ease 0.5 xpos 0.33

lisia @happy "Well, I think you can!"

dawn @surprised "Huh?"

lisia @angrybrow happymouth "Listen up, everyone! This is {i}Dawn!{/i} She's the daughter of Johanna Berlitz, contest champion of the Sinnoh region! She's an amazing battler!"

lisia @angrybrow happymouth "Now, Dawn thinks that she's going to lose in this battle--what do we think, everyone?!"

$ PlaySound("crowd_cheer.ogg")

$ renpy.music.play("Audio/Stadium_crowd.ogg", channel='crowd', loop=True, fadein=1.5)
$ renpy.music.play("Audio/Stadium_chant.ogg", channel='crowd2', loop=True, fadein=1.5)
$ renpy.music.queue("Audio/Music/Indigo_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/Indigo_Loop.ogg", channel='music', loop=True, tight=None)

pause 1.0

lisia @happy "That's what I'm saying! Dawn, don't worry about what anyone else tells you to do, or expects of you! You're not fighting for them! Not for your Mom, not for Kobukan, not for me!"
lisia @sadbrow happymouth "You're fighting for yourself, and for your Pokémon! You're fighting for fun--and for the show!"

dawn @sadbrow neutralmouth "{w=0.5}.{w=0.5}.{w=0.5}."

lisia @talkingmouth "You can take my advice. Or you can ignore it. You're your own person, Dawn--and no-one here is going to tell you what to do."
lisia @happy "I'll be happy as long as you're happy!"

dawn @closedbrow sadmouth "Okay."

pause 1.0

dawn angrybrow happymouth "Okay. Okay! I'll do this! I'll do this, for myself, and my Pokémon! And no-one else!"

redmind @happy "Fantastic."

if (lanceplan):
    redmind @thinking "But... this does make my situation a bit more awkward..."

else:
    redmind @thinking "On the other hand, I'm about to lose so hard that my grandkids will feel it."

    pause 1.0

    redmind @happy "Oh, well."

    redmind @sadbrow frownmouth "Sorry, Leaf, Tia, Blue, Ethan, Yellow... I know you tried really hard to get me back here on time."

hide lisia with dis

show dawn:
    ease 0.5 xpos 0.5

dawn @talkingmouth "Alright, [first_name]. I hope you're ready. Ready for a {i}real{/i} battle. I'm going to go all-out against you, and I want you to go all-out against me, too!"

red @sweat talking2mouth "So... we're not following Lance's plan?"

dawn @angrybrow sadmouth "No."

red @sweat closedbrow talking2mouth "Damn."

if (lanceplan):
    dawn @talkingmouth "...But if you want to do a one-on-one, then... that's fine."

    red @surprised "Really?"

    dawn @talkingmouth "Yeah! As long as you do your best! And--and I'll do my best, too!"

    redmind @happy "Hey. Maybe I've got a chance after all!"

    python:
        dawnaltariaobj = Pokemon("Altaria", level=68, moves=[GetMove("Roost"), GetMove("Cotton Guard"), GetMove("Hyper Voice"), GetMove("Dragon Pulse")], ivs=[31, 31, 31, 31, 31, 31], evs=[252, 0, 252, 4, 0, 0], nature=Natures.Bold, gender=Genders.Female, item="Altarianite", ability="Cloud Nine")
        dawnparty = [dawnaltariaobj]
        trainer1 = Trainer("red", TrainerType.Player, [lancedragonite1obj])
        trainer2 = Trainer("dawn", TrainerType.Enemy, dawnparty)

    call Battle([trainer1, trainer2], gainexp=False, specialmusic="Audio/Music/legendary.ogg", dialogfunc=dawndragonitedialog, custombrain=dawndragonitebrain, lockbag=True) from _call_Battle_116
    $ battlehistory["Dawn1"] = _return

    if (WonBattle("Dawn1")):
        narrator "You managed to defeat Dawn."

        scene blank2

        narrator "You easily succeed at everything you do for the rest of the year, and then, your life."

        pause 1.0

        narrator "Congratulations. You won the game."

        $ MainMenu(confirm=False)()
    
    else:
        jump gameover

else:
    dawn @talkingmouth "But... I actually only brought one Pokémon with me, anyway. I thought I {i}was{/i} going to follow Lance's plan."

    red @surprised "Really? Don't you have more?"

    dawn @happy "Oh, definitely! And they're all really strong."

    dawn @angrybrow happymouth "But my Altaria is the strongest."
    dawn @sadbrow talking2mouth "Um... if you want it to be a bit more equal, you can use two Pokémon at once... I think, technically, you have to, actually..."

    redmind @happy "Well... sucks to be me. But I'm going to give it my all!"

    red @angrybrow happymouth "This'll be a {i}real{/i} battle, Dawn. No expectations or absolutes. You deserve to be {i}free.{/i}"

    if (GetRelationshipRank("Dawn") == 1):
        dawn @sadbrow happymouth "...I'm sorry I have to battle {i}you{/i}... I never thought you were mind-controlling anyone."

        red @talking2mouth "Dawn Berlitz."

        pause 1.0

        red @happy "It's an honor to battle you."
    
    else:
        dawn @sadbrow talking2mouth "I... I don't think you were mind-controlling anyone anymore."

        red @winkeyes talkingmouth "Well, that's one down."

    python:
        dawnaltariaobj = Pokemon("Altaria", level=68, moves=[GetMove("Ominous Wind"), GetMove("Earthquake"), GetMove("Hyper Voice"), GetMove("Dragon Pulse")], ivs=[31, 31, 31, 31, 31, 31], evs=[252, 0, 252, 4, 0, 0], nature=Natures.Bold, gender=Genders.Female, item="Altarianite", ability="Cloud Nine")
        HealParty()
        dawnparty = [dawnaltariaobj]
        playerparty.remove(pikachuobj)
        playerparty.append(pikachuobj)
        trainer1 = MakeRed(2)
        trainer2 = Trainer("dawn", TrainerType.Enemy, dawnparty)
        dawnbattle = True

    call Battle([trainer1, trainer2], gainexp=False, specialmusic="Audio/Music/legendary.ogg", dialogfunc=dawnpikachudialog, custombrain=dawnpikachubrain) from _call_Battle_117
    $ battlehistory["Dawn1"] = _return
    $ dawnbattle = False

    if (not WonBattle("Dawn1")):
        jump gameover

python:
    removethis = None
    for newmove in pikachuobj.GetMoves():
        if (newmove.Name == "Liberage"):
            removethis = newmove

    pikachuobj.GetMoves().remove(removethis)

    allowfractions = False
    PlaySound("crowd_cheer.ogg")

queue music "audio/music/new_adventure_start.ogg" noloop
queue music "audio/music/new_adventure_loop.ogg"

show dawn:
    xpos 0.66
show lisia:
    xpos 0.33
with dis

lisia @surprised "That was absolutely incredible!"
lisia @happy "I've never seen such a beautiful performance! You're an absolute superstar!"

red @happy "Hey, I'm just happy to--"

show lisia:
    ease 0.3 xpos 0.5

lisia @talkingmouth "Dawn! That was incredible! You've got a coordinator's spirit inside of you, I can tell!"

redmind @closedbrow frownmouth "Oh. I really need to stop assuming that Lisia's talking to me."
redmind @happy sweat "After all, compared to a world-famous star like her... I'm kinda a nobody."

$ PlaySound("pokemon/pikachu_happy1.ogg")

libpikachu -glowing @happy "Pikaaa!~"

redmind @angrybrow frownmouth "But I'm a nobody who just beat a girl who battled {i}Cynthia.{/i}"

narrator "You bend down and ruffle [pika_name]'s fur."

red @talkingmouth "You've gotten bigger, buddy. Not much bigger, but a little bigger."

$ PlaySound("pokemon/pikachu_norm3.ogg")

libpikachu @sadeyes talkingmouth "Pika."

redmind @frownmouth "He's tired..."

narrator "[pika_name] totters toward you, and in an entirely unexpected move, taps his heavy head against his own Poké Ball."

$ PlaySound("pokemon/ball sound.ogg")

pause 1.0

red @surprisedbrow frownmouth "...That's new."

narrator "You tune back into the conversation that Dawn's having with Lisia."

lisia @talkingmouth "Oh, please, please, {i}please{/i} won't you be my protégé?"
lisia @happy "I've never seen someone command such a high-level Pokémon so beautifully except my own uncle Wallace!"
lisia @sadbrow talkingmouth "You could do absolutely amazing in contests, sweetheart!"

dawn @sadbrow talkingmouth "Oh... I don't know about that... I have to go to school, and everything..."

lisia @surprised "Oh!"
lisia @xdbrow happymouth "Of course, of course! I'm not asking you to drop out or anything! But if there were some way I could convince you...?"
lisia @talkingmouth "Flights to Hoenn are pretty cheap, and this is a once-in-a-lifetime opportunity, so..."

dawn @sadbrow talkingmouth "I don't think there is. I'm really sorry, Lisia, but I've got... um... a lot going on, and I don't do contests anymore, so..."

$ PlaySound("whoosh.ogg")

show calem closedbrow angrymouth:
    xpos 1.2 xzoom -1
    ease 0.3 xpos 0.75

show dawn surprisedbrow frownmouth with dis:
    xpos 0.66
    ease 0.5 xpos 0.5

show lisia surprisedbrow frownmouth with dis:
    xpos 0.5
    ease 0.5 xpos 0.25

narrator "Calem comes running across the arena, skidding to a halt in the center of the girls' conversation."

calem @talkingmouth "Ah...{w=0.5} hah...{w=0.5} Lisia..."

pause 2.0

show dawn -surprisedbrow -frownmouth
show lisia -surprisedbrow -frownmouth

lisia @sadbrow happymouth "Hi! Are you a coordinator, too? I'm sorry, but I'm only looking for one apprentice right now."

calem @talkingmouth "N-no...{w=0.5} sorry, let me just...{w=0.5} catch my breath..."

pause 1.0

show calem -closedbrow -angrymouth with dis

narrator "Calem stands up straight and talks, clearly and directly."

calem @talkingmouth "Ms. Lisia. I am a classmate of Dawn here."
calem @closedbrow talkingmouth "I can, at the very least, vouch for her competence with Fairy-type Pokémon. Her Pokémon adore her, and she knows a tremendous amount about the subject."

lisia @sadbrow talkingmouth "Uh... I know...?"

calem @talkingmouth "I say this to make clear what a... well, what a 'catch' she is."

show dawn surprisedbrow frownmouth with dis

dawn @talkingmouth "Uh-uh..."

calem @closedbrow talkingmouth "She is not alone. My roommate is an avid follower of your work. He is a skilled coordinator in his own right, and my good friend Serena has an interest in performance as well."
calem @happy "Why, this school is chock-full of people who would be willing to learn the delicate arts of Pokémon coordination from you, Champion Lisia."

lisia @surprised "So...?"

calem @closedbrow talkingmouth "I think, perhaps, we are approaching this from the wrong angle. Perhaps it is not necessarily a question of 'how can we get Dawn to go with you'? Perhaps it is a question of 'how can we get you to stay with Dawn'?"

lisia closedbrow talking2mouth "Hmm..."

calem @angrybrow happymouth "You are to be the announcer for all the Quarter Qlashes in this area, yes? Surely it would be tiring to fly here and to Hoenn eight times this year."
calem @happy "Why not stay here, Lisia? You could keep an eye on your protégé directly. You'd have the opportunity to {i}live{/i} on the historic Kobukan Academy grounds. You'd be able to share your art with a new generation of coordinators."

lisia @talkingmouth "I... Hm."

calem @talkingmouth "And, if I remember correctly, you have family here...?"

pause 1.0

calem @happy "It goes without saying that this would also be a paid position."

pause 2.0

lisia -closedbrow -frownmouth @happy "Alright! I've got a big announcement! Everyone--ladies and gentlemen--your favorite Lisia is going to be staying here at Kobukan Academy for the next year!"

$ PlaySound("crowd_cheer.ogg")

pause 2.0

lisia @sadbrow talking2mouth "Wait, are you even allowed to offer me a position here? It's obvious you're a professor, but... are you, like, {i}money{/i} staff?"

calem surprisedbrow frownmouth @surprised "Er? Obvious I'm a professor?"

lisia @happy "Well, you're greying--"

show calem deadbrow surprisedmouth at monochrome with vpunch:
    ypos 1.0 xpos 0.75
    ease 1.0 ypos 1.1 rotate 5.0    

calem @talkingmouth "{size=30}I'm... I'm eighteen...{/size}"

show calem at monochrome:
    ypos 1.1 rotate 5.0 xpos 0.75
    ease 0.5 ypos 2.0 rotate 30.0

lisia @surprised "Ah! Is this old man okay?"

show janine at rightside with dis:
    xzoom -1

show dawn surprisedbrow frownmouth with dis

janine @talking2mouth "I'll clean up the body."

pause 2.0

dawn -surprisedbrow -frownmouth -surprised sadbrow frownmouth @sad "Oh... J-Janine... sorry, I f-forgot about the Battle Team... um... I'm sorry, I should have asked you, and... I can change my mind... I know I'm not allowed to leave... and I'm sorry about ruining the Battle Team's reputation..."

janine @talking2mouth "...Dawn. You shouldn't apologize."

pause 1.0

janine @sadbrow talking2mouth "...I should apologize."

dawn @surprised "Wh-- no, no, you totally shouldn't! You didn't do anything wrong!"

janine @sadbrow talking2mouth "I put you in this situation by forcing you into the Battle Team. And then I put you in {i}this{/i} situation by being too cocky."

pause 1.0

janine @closedbrow talking2mouth "I want to say I planned this whole thing so you'd learn how to resist when people try to push you into things, but... no. It was just a couple of dumb mistakes."
janine @talking2mouth "I'm sorry."

dawn -frownmouth @sadbrow talkingmouth "...You were a really good Captain for the two weeks I had you."

janine @closedbrow smirkmouth "Psh. No I wasn't. I broke the Battle Team's untainted round one victory streak."

dawn @closedbrow sadmouth "I think that was me, really... I'm really sorry about that."

janine @smirkmouth "Hey. It's just a victory streak. All I care about is getting into the National Tournament, and... depending on what you might've just done for [first_name], you might've just {i}increased{/i} our chances there."

pause 2.0

narrator "The women all turn to look at you."

pause 2.0

red @happy "Heh?"

janine @talking2mouth "You have no idea what just happened?"

red @talkingmouth "Nope."

janine @closedbrow talking2mouth "When you do, tell me. For now..."

show janine:
    ease 0.5 xpos 0.35

show dawn:
    ease 0.5 xpos 0.75

pause 0.5

narrator "Janine holds out a hand, and Lisia obediently places her microphone in Janine's palm."

pause 1.0

lisia @surprised "{size=30}Wait, why did I do that?{/size}"

show janine:
    ease 0.5 xpos 0.5 ypos 1.2 zoom 1.3

janine @talking2mouth "Here."

show janine:
    ease 0.5 ypos 1.0 zoom 1.0

stop music fadeout 5.0

janine @closedbrow talking2mouth "You know what to do."

if (GetRelationship("Janine") == "Good Boy"):
    pause 1.0

    janine @talking2mouth "You're brave. Use that bravery."

else:
    janine @talking2mouth "Tell the truth."

hide janine
hide dawn
hide calem 
hide lisia
with dis

$ dialogs = [
    "Leaf looks at you, unconditional admiration in her eyes. She urges you to try.",
    "Ethan shakes his head and shrugs. His expression seems to say 'Come on. You've got this.'",
    "Blue scoffs. It's clear he's tired of being the only person who knows the truth.",
    "Yellow gives a silent cheer and a fist-pump. You remember what your mother always says about secrets...",
    "You think of your mother. She gives an encouraging nod, and a warm hug.",
    "{}'s Poké Ball shifts as, even exhausted, he cheers you on.".format(pika_name),
    "You hear a whisper in your mind that, ever-so-gently, encourages you to speak.",
    "You remember Cheren's face onstage--a mask of calm, devoted to truth, no matter the pain."
]

label givespeech:

menu:
    "Give a speech.":
        queue music "audio/music/unwaveringemotions.ogg"

    "Stay silent.":
        $ randomdialog = random.choice(dialogs)
        narrator "[randomdialog]"

        jump givespeech

narrator "You close your eyes, open your mouth, and give a speech. A real one. With thought and meaning to it, this time."

red @talkingmouth "I'd like to say something. Um, to everyone here."

red @closedbrow talking2mouth "I know there are a lot of people here who aren't students of Kobukan, so I'll provide some quick context."

red @happy sweat "And, uh, I'll try to make it quick, because I know we have a few more matches today."

pause 2.0

red @talkingmouth "Last Saturday, I was accused of having mind-control powers. This was a very public event."
red @sad2eyes sadeyebrows talking2mouth "I was asked to deny it. I did not deny it."
red @closedbrow talking2mouth "I should have. But I was...{w=0.5} I was scared. I thought I'd be misunderstood, and I understood why people would think that this is some sort of... unfair advantage."

pause 1.0

red @talkingmouth "I do {i}not{/i} have mind-control powers."

pause 1.0

red @happy sweat "Sounds kinda silly when I put it like that, huh?"

red @talkingmouth "...I just want everyone here to know the truth. Because secrets just hurt people--the person holding the secret, and the person who the secret's being kept from. My Mom always says that."
red @closedbrow talkingmouth "I guess between High School and coming here, I forgot how smart she was."

pause 1.0

red @talkingmouth "I don't have mind-control powers, but I still want to apologize. I shouldn't have kept this a secret from all of you."
red @talking2mouth "My power is called Frienergy. It induces empathy in others. People and Pokémon around me know what I'm thinking or feeling."
red @closedbrow talking2mouth "Maybe that means you trust me more easily. And maybe that makes you more uncomfortable. If so, I'm sorry."
red @talking2mouth "I've talked to some of you about personal stuff. I wasn't trying to, like, 'harvest secrets' or anything. I just wanted you to have someone you could trust or confide in."
red @sadbrow talkingmouth "I promise, now and forever on, that I'm not using this power in any way that would hurt anyone. I don't think it even can be."

pause 1.0

red @happy "I just want to be friends with everyone, guys. That's the sum of it."

pause 2.0

narrator "You're not sure what you're expecting. Maybe a slow cheer. Maybe a chorus of boos."

pause 1.0

narrator "But all that meets you is silence."

pause 1.0

narrator "Still. You feel like those who you were talking to--those who matter--heard you."
narrator "Perhaps today is not the day you will hear cheers from the stands..."

pause 1.0

narrator "But you're one step closer."

narrator "For the {color=#ff8412}Courage{/color} it took to say this..."

$ TraitChange("Courage")

narrator "For the {color=#e226a6}Patience{/color} you showed while weathering the aspersions and rumors of others..."

$ TraitChange("Patience")

narrator "For the {color=#60c2f8}Wit{/color} you demonstrated by conveying your message clearly and concisely..."

$ TraitChange("Wit")

narrator "For the {color=#66b77d}Knowledge{/color} you held to recall and convey every detail..."

$ TraitChange("Knowledge")

narrator "And, finally, for the {color=#b7669e}Charm{/color} you showed by valuing others, and caring about another's happiness..."

$ TraitChange("Charm")

pause 2.0

$ PlaySound("sav.ogg")

narrator "Your heart shifts as you feel your relationship with yourself evolve from '{color=#0048ff}Entity{/color}' to '{color=#0048ff}Ally{/color}'!"

pause 2.0

show lisia sadbrow frownmouth with dis:
    ypos 1.2 zoom 1.3

lisia @talking2mouth "Um... microphone, please."

red @sweat happy "Here you go. Sorry about... the derailing."

lisia -sadbrow -frownmouth @sadbrow talkingmouth "I don't remember the last time I had a show go smoothly. It's not too big a deal."

pause 1.0

show lisia happy:
    ease 0.5 xpos 0.5 ypos 1.0 zoom 1.0

lisia @happy "Okaaaay! Lots of stuff happening here today, everyone! That's why battling is such a great way of showing yourself off!"

narrator "You step back from the spotlight as silence closes around your throat once more."

call clearscreens from _call_clearscreens_126
scene blank2 with transeye

stop music fadeout 5.0

pause 5.0

jump day010508
