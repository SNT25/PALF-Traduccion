label secondhomeroom010415:

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=True, fadein=1.0, tight=None)

scene blank2

show oakbg behind blank2
show homeroom behind oakbg

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with dis

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)
    
show homeroom behind oakbg

oak @talkingmouth "...And that concludes today's lesson! Now, I hope you all prepared for the quiz. Be ready for this!"

show hilbert uniform at rightside with dis

hilbert @talkingmouth "Let's see if this quiz is any more than 'laughably easy,' like the others."

show blue uniform at leftside with dis

blue @happy "Yeah! Every quiz we've taken so far has been done in a single turn. When's the real stuff coming out, huh?"

oak @talkingmouth "It is not my intention to fail any of you. The quizzes will get harder as the school year progresses--if you find them 'too easy' now, take that as a gift."

show hilbert sad 
show blue angry
with dis

"{color=#353535}Hilbert{/color} & {color=#3110dd}[blue_name]{/color}" "\"Tch.\""

hide hilbert 
hide blue
with dis

oak @talkingmouth "You all know what to do. Take a close look at the battlefield before you commit to {i}anything{/i}!"
oak @talkingmouth "Remember, {color=#0048ff}this is graded!{/color}"

$ trainer1 = Trainer("red", TrainerType.Player, [
    Pokemon(pokedexlookupname("Mienfoo", DexMacros.Id), level=20, moves=[GetMove("Fake Out"), GetMove("Meditate"), GetMove("Detect"), GetMove("Double Slap")])
])
$ trainer2 = Trainer("oak", TrainerType.Enemy, [
    Pokemon(pokedexlookupname("Tropius", DexMacros.Id), level=70, moves=[GetMove("Leaf Storm"), GetMove("Body Slam")], ability="Solar Power")
])

$ trainer2.GetTeam()[0].ApplyStatus("badly poisoned")
$ trainer2.GetTeam()[0].Health = trainer2.GetTeam()[0].Health * 3 / 16

call Battle([trainer1, trainer2], clearstats=False, gainexp=False, healParty=False, uniforms=[True, False], lockbag=True) from _call_Battle_18
$ battlehistory["Oak3"] = _return

$ renpy.transition(dissolve)
show screen currentdate

if (WonBattle("Oak3")):
    red uniform @happy "Wow! That level difference scared me at first."
else:
    red uniform @sad "Oh, geez... that level difference was rough. It's faster than me, and {i}any{/i} move it uses could knock me out..."

oak @talkingmouth ".{w=0.5}.{w=0.5}.{w=0.5}"

pause 0.5

oak @talkingmouth "At a glance..."

pause 0.5

if (WonBattle("Oak3")):
    oak "It looks like everyone did quite well. It seems you understand the importance of stalling techniques. Though many decry them as 'unfun,' in a pitched battle with a stronger foe, they may be all you have, and need, to hold on."
else:
    oak "I recommend everyone try a bit harder to learn the effects of your moves. Remember, every battle quiz has a way where you are {i}guaranteed{/i} to win. If you only have 'a chance' to win, keep looking."

oak @talkingmouth "That's it for today, class.{w=0.5} You're all dismissed."

hide oakbg with dis

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.5)

redmind @thinking "Phew. Long day. Let's see if I can find Gardenia, and--"

show leaf uniform sadbrow with dis

leaf @talking2mouth "Hey, [first_name]. Busy?"

red @happy "So busy, you don't even know! I've gotta run to the baseball field now to--"
red @closedbrow talking2mouth "Uh..."
red @talkingmouth "To do a thing."

leaf -sadbrow frownmouth @sarcastic "Does this thing involve that mystery girl you and Whitney have been paying so much attention to recently?"

red @thonk "{w=0.5}.{w=0.5}.{w=0.5}."
red @closedbrow talking2mouth "Indirectly."

leaf @sarcastic "Yeah, I figured."

pause 1.0

red @confusedeyebrows talking2mouth "Using my immense powers of observation, and unsurpassed people skills, I'm guessing you feel a bit ignored?"

leaf -frownmouth @happy "Give the man a cigar! So, what do you think you can say to get out of this?"

menu:
    "\"Would you like to come with me?\"":
        $ ValueChange("Leaf", 1, 0.5)

        leaf @happy "Right answer! And yeah, duh!"

    "\"Seeya.\"":
        show leaf surprisedbrow frownmouth with dis

        $ ValueChange("Leaf", -1, 0.5)

        leaf -surprisedbrow -frownmouth @angry "Hahaha. Not funny. I'm coming with you, you dick."

        red @happy "Yeah, okay. Sorry, bad joke."

red @talkingmouth "Mind if I run back to my dorm to get [pika_name] and change, though?"

leaf @talkingmouth "Nah, go ahead. I'll get changed too. Meet you at the field?"

red @happy "Sure."

scene baseball with wipeleft
$ AddPikachu()

show tia at farleftside
show whitney at leftside behind tia
show flannery at midrightside behind tia
show gardenia at rightside behind flannery
with dis

stop music channel "crowd"

queue music "audio/music/Show me around.ogg"

leaf @happy "Hey, girls!"

show leaf at midleftside behind flannery with dis

red @talkingmouth "Hey, every--"

show whitney surprisedbrow frownmouth 
show flannery surprisedbrow frownmouth
show gardenia surprisedbrow frownmouth
show leaf surprisedbrow frownmouth
with dis

show tia happy:
    ease 0.5 xpos 0.4 zoom 1.3 ypos 1.2
    pause 0.5
    parallel:
        ease 0.3 ypos 1.25
        ease 0.3 ypos 1.2
        repeat

red @surprised "W-woah."

whitney @sad "H-hold on, I can't translate that fast! I, I mean, I need to--"

show tia:
    ease 1.0 xpos 0.5 zoom 1.0 ypos 1.0

show whitney -surprisedbrow -frownmouth -surprised 
show flannery -surprisedbrow -frownmouth -surprised
show gardenia -surprisedbrow -frownmouth -surprised
show leaf -surprisedbrow -frownmouth -surprised
with dis

tia "--and Instructor Clair was complimenting me over and over and I wanted to thank her, but she didn't understand me!"

leaf @closedbrow talkingmouth "Huh? Complimenting you? All she {i}ever{/i} does is rant about how Dragon-types are the best."

tia @surprised "Yes, that's what I said! And then when I went to my other elective, this one girl kept trying to get in my head, so I just shut her out. But then she got upset--but also happy? I don't understand that."

red @closedbrow talking2mouth "Uh... yeah, I can see why there would be some mixed feelings there."
red @surprised "Wait, you can {i}shut her out{/i}?"

tia sad "Oh, yes, it's really easy! But when I went to the cafeteria, it was... oh, it was awful! They were serving Pokémon there!"

red @talkingmouth "Oh, that's, uh, that's actually lab-grown meat. They're named after Pokémon, but people don't actually {i}eat{/i} Pokémon. Not for hundreds of years, anyway."

tia happy "Really? Okay! That's good. But my homeroom quizzes are really hard. How do I learn what moves other Pokémon can even know?"

red @confusedeyebrows talking2mouth "I mean... we're meant to study? Like, our books?"

tia angryeyes angryeyebrows poutmouth "What? But I've already studied so hard just to learn sign language! And reading is {i}really{/i} hard!"

red @sadbrow happymouth "I mean... it's kinda necessary."

tia sadeyes sadeyebrows "Aw..."

pause 1.0

hide flannery
show flannery:
    ypos 1.0 zoom 1.0 xcenter 0.63
    ease 0.5 ypos 1.2 zoom 1.3

flannery @closedbrow talking2mouth "{i}Ahem.{/i}"

hide flannery
show flannery behind tia:
    ypos 1.2 zoom 1.3 xcenter 0.63
    ease 0.5 ypos 1.0 zoom 1.0

red @happy "Oh, right. Hey, uh, T- Bianca."

tia happy "Yes!"

red @sadeyes sadeyebrows happymouth "Whitney and Flannery tell me that you're waking them up in the middle of the night to ask for computer help?"

flannery @sad "And show us memes."

tia happy "I like the one about the grumpy Purugly!"

red @happy "Well, see, the thing is, your dormmates need to sleep as well. So you can't wake them up anymore, alright? Even if you see a really dank meme."

show whitney surprisedbrow frownmouth 
show flannery surprisedbrow frownmouth
show gardenia surprisedbrow frownmouth
show leaf surprisedbrow frownmouth
with dis

tia happy "Okay!"

pause 1.0

whitney @talking2mouth "Wait... it's that easy for you?"

red @confused "Uh... yeah, why?"

show whitney -surprisedbrow -frownmouth -surprised 
show flannery -surprisedbrow -frownmouth -surprised
show gardenia -surprisedbrow -frownmouth -surprised
show leaf -surprisedbrow -frownmouth -surprised
with dis

flannery @sad "She {i}never{/i} listens to us. I mean, even about dumb stuff, like how she needs to wake up in the morning, or not sleep naked."

whitney @happy "I don't mind that!"

flannery @closedbrow talking2mouth "Whitney..."

gardenia @happy "This is a pretty crazy story you guys got going on! I didn't expect your meteor woman to be so quirky."

redmind @surprised "Shit!"

leaf @sarcastic "Meteor woman?"

gardenia @talkingmouth "Yeah, my dormie Skyla told me that she, a hunky dude, and [first_name] found Bianca in a meteor crater outside school."

pause 1.0

redmind @sad "Crap. Now three more people know."

leaf @surprised "Wait, did, like, the meteor hit her?"

tia @happy "No, I hit the meteor!"

gardenia @talkingmouth "Skyla also said something about an alien invader that you guys kicked the ass of?"

if (WonBattle("Absol1")):
    red @closedbrow talking2mouth "It was an Absol, actually."
else:
    red @talkingmouth "It was an Absol. And it was more like it kicked our ass."

leaf @angry "Hey. What's happening here, [first_name]? This mystery girl shows up, and now you're telling me she's from space?"

tia @happy "Actually, I'm from Alto Mare."

leaf @angrybrow angrymouth "Can it, sweetheart."

tia -happy frownmouth @angry "Hey!"

leaf @talking2mouth "Enough beating around the bush. Who is she?"

show tia sadeyes sadeyebrows frownmouth with dis

red @surprisedeyes surprisedeyebrows sadmouth "She... uh, she..."

pause 1.5

tia happy "I'm Tia! I switched places with my sister, Bianca. But I don't want anyone to know. Which is why [first_name] was protecting me."

gardenia @happy "Well, that answers all my questions."

leaf @angry "What? Hey, I've got way more! Why did you only show up now? And why were you fighting a meteor? And--"

show leaf surprisedbrow frownmouth with dis

tia @happy "I'm going to fly back to the garden now. Bye!"

hide tia with dis

pause 2.0

leaf @talking2mouth "What?"

gardenia @happy "...Fun girl! She needs some muscle on her, though. Poor thing's a twig. We sure she's eighteen?"

show whitney surprisedbrow frownmouth 
show flannery surprisedbrow frownmouth
show gardenia surprisedbrow frownmouth
show leaf surprisedbrow frownmouth
with dis

red @closedbrow talking2mouth "Her ID said she was."

pause 2.0

red @surprised "Wait, shit."

show whitney -surprisedbrow -frownmouth -surprised 
show flannery -surprisedbrow -frownmouth -surprised
show gardenia -surprisedbrow -frownmouth -surprised
show leaf -surprisedbrow -frownmouth -surprised
with dis

leaf angrysmilemouth angrybrow @talking2mouth "Why were you looking at her ID?"

red @closedbrow talking2mouth "Uh... I was just confused as to her name. I didn't know the whole Bianca-Tia thing she just explained."

leaf -angrysmilemouth -angrybrow @closedbrow talkingmouth "Hrmph. Well, did you come here to tell the meteor maid not to wake up Flannery and Whitney?"

red @talkingmouth "Actually, I came to talk to you, Gardenia."

show leaf -thinking with dis

gardenia @surprised "Oh?"
gardenia @happy "Oh, sure! You want to hire me as your personal trainer, right? Lucky for you, I have an open slot. I'll even give a discount to a fellow classmate."

red @happy "Tempting, but not this time. I was actually going to ask if you could, uh... not tell anyone about Tia."

gardenia @surprised "Oh, shit. Sorry, man."

red @closedbrow talking2mouth "Hey, it's alright. Just, y'know, if we could {i}all{/i} do our best to not let anyone else know about her, I think that would be... safest. Especially faculty."

gardenia @talking2mouth "I gotcha, I gotcha."
gardenia @happy "But how much is it worth to you?"

red @surprised "Huh? Like, money?"

gardenia @angrybrow happymouth "Yeah. How much are you willing to pay to keep that secret?"

red @talking2mouth "It's not even {i}my{/i} secret. Just hide it, okay? If you want money, I'll sign up for one of your classes as soon as I have time."

gardenia @happy "Hey, it's alright, man. I wouldn't actually make you pay. But, hey, would you be down for a gamble battle?"

red @closedbrow talking2mouth "A gamble battle?"

gardenia @talkingmouth "Yeah, we both put some money on the line. Winner takes it all."

flannery @happy "Sounds fun! Can I join?"

gardenia @happy "Sure! Bigger pool, bigger prizes."

red @closedbrow talking2mouth "Can't do a three-way battle, though."

if (GetRelationshipRank("Leaf") > 0):
    red @happy "I bet you want to get in on this, don't you, battle fanatic?"

    leaf @happy "I {i}totally{/i} do!"

else:
    red @happy "Want to join in, Leaf?"

    leaf @happy "I {i}totally{/i} do!"

gardenia @talkingmouth "Alright, so Flannery and I against you two? Cool. How much are you potting?"

if (money < 2000):
    red @happy "I, uh, I don't actually have--"

else:
    red @happy "Uh, well, the most I can put in is two thous--"

show baseball with vpunch

leaf angrybrow @happymouth "We'll raise the ante to $50,000 each!"

gardenia @surprised "Holy-- no, no way, man. I can't do that. Like, I cap out at a grand. Gotta be prepared to lose."

leaf @closedbrow talkingmouth "Oh. Well, we'll both put in $1,000, then."

red @sadbrow talkingmouth "{size=30}Uh, Leaf? You know money's kinda...{/size}"

leaf @happy "{size=30}Relax. We won't lose.{/size}"

red @wince talking2mouth "{size=30}And... if we do...?{/size}"

leaf @closedbrow talkingmouth "{size=30}I'll cover you. Don't worry about it.{/size}"

red @talking2mouth "{size=30}Look, I don't want to take handouts from my friends...{/size}"

leaf @flirttalk "{size=30}Then you better not lose!{/size}"

redmind @thinking "Hoo boy."

red @talking2mouth "Alright, let's do this."

whitney @happy "Good luck, dormie! Kick their butts!"

red @angry "Hey!"

whitney @surprised "What?"

$ trainer1 = Trainer("red", TrainerType.Player, playerparty)
$ trainer2 = MakeTrainer("Leaf", TrainerType.Ally)
$ trainer3 = Trainer("flannery", TrainerType.Enemy, [GetTrainerTeam("Gardenia", "Budew"), GetTrainerTeam("Gardenia", "Phantump")])
$ trainer4 = Trainer("gardenia", TrainerType.Enemy, [GetTrainerTeam("Flannery", "Numel"), GetTrainerTeam("Flannery", "Onix")])

call Battle([trainer1, trainer2, trainer3, trainer4]) from _call_Battle_19
$ battlehistory["FlanneryGardenia1"] = _return

if (WonBattle("FlanneryGardenia1")):
    show flannery sadbrow frownmouth at midrightside
    show gardenia sadbrow frownmouth at rightside behind flannery
    show leaf at midleftside
    with dis

    red @happy "Yes!"

    $ ValueChange("Leaf", 3, 0.37)

    leaf @happy "Good job, [first_name]! Bringing home the bacon!"

    flannery @sad "Aw... there goes my shopping weekend."

    gardenia @sad "Ugh. I'm going to need to pick up some new clients."

    gardenia -sadbrow -frownmouth @talkingmouth "Fun battle, though. Just don't ask for another one anytime soon. Here's your moolah."
    flannery -sadbrow -frownmouth @talking2mouth closedbrow "Yeah... take this."

    $ PlaySound("Get.ogg")

    $ money += 2000

    narrator "You and Leaf both get $2,000!"

    redmind @thinking "Hm... this might be a way I could make some money, actually. Not with my friends, obviously, but if I could find a battle with high enough stakes..."

else:
    show flannery happy at midrightside
    show gardenia happy at rightside behind flannery
    show leaf sad at midleftside
    with dis

    red @sad "No..."

    leaf -sad @talking2mouth "Ugh. Alright. It's only $2,000. I'll be fine. I'll just have to buy a bit less this weekend..."

    red @sadbrow talkingmouth "{size=30}I really don't mind paying my share, Leaf.{/size}"

    leaf @sarcastic "{size=30}With what money? I'll cover you.{/size}"

    gardenia -happy @happy "Sorry you guys lost, but I had a {i}great{/i} time!"
    flannery -happy @happy"Yeah, this was really fun!"

    $ ValueChange("Flannery", 3, 0.63, False)
    $ ValueChange("Gardenia", 3, 0.75)

    leaf @happy "Yeah... it was fun for me, too. But I don't think I'll be gamble-battling with you guys again any time soon!"
    
    red @closedeyes talking2mouth "Ugh... "

    redmind @thinking "Although this was a bust, if I could manage a win, this might be a way I could make some money." 
    redmind @thinking "Not by battling against my friends, obviously, but if I could find a battle with high enough stakes..."

leaf @happy "Good battle, but I'm exhausted. Going to head back to my dorm now." 
leaf @flirttalk "I'll talk to you all later!"

red @happy "See ya."

show blank2 with Dissolve(2.0)

narrator "Secure in the knowledge that anybody who knows about Tia's presence here at the school is no longer going to tell anyone, you decide to head back early."

call texting from _call_texting_4

jump day010416