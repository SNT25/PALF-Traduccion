label day010512:

call clearscreens() from _call_clearscreens_155

$ timeOfDay = "Early Morning"

call calendar(1) from _call_calendar_37

$ calDate = calDate.replace(day=12, month=5, year=2004)

show earlymorning at vspaz

$ renpy.music.play("Audio/Morning_ambience.ogg", channel='crowd', loop=True, fadein=1.0)

scene kitchen 
show ethan sadeyebrows sad2eyes frownmouth
with splitfade

pause 1.0

red @happy "Morning, man!"

ethan @talkingmouth "Mm."

pause 1.0

red @sadbrow talking2mouth "Wait, what's wrong?"

ethan @talkingmouth "It's... nothing."

menu:
    "Oh, alright then.":
        $ AddEvent("Ethan", "IgnoredFrenzyConfession")
        jump afterethanmeeting

    "Go on, you can tell me.":
        pass

ethan @talking2mouth "...Okay. It's a silly thing, but, like, remember how on Monday I said we needed to talk, and we should do that Tuesday morning?"

if (HasEvent("Ethan", "TalkNow")):
    red @closedbrow talking2mouth "Yeah. I tried to convince you to talk then and there, but you didn't go for it. But what about it?"

else:
    red @confused "Yeah?"

pause 1.0

red @surprised "Oh, {i}crap{/i}, sorry, I remember now! I didn't mean to ghost you, man, I just had so much going on."
red @sad "I'm super-sorry about that."

ethan -sad2eyes @sad2eyes talking2mouth "It's fine. I mean, I know how busy you are, but..."
ethan @closedbrow talking2mouth "...Man, nevermind, just ignore me. I'm whining about nothing. I could've talked to you and gotten this over with days ago."

red @talkingmouth "...What do you mean?"

pause 1.0

ethan -frownmouth @talkingmouth "You wanna go for a run?"

red @happy "I thought you'd never ask!"

stop music fadeout 1.5 channel "crowd"

call clearscreens from _call_clearscreens_156
show blank2 with splitfade

pause 1.0

$ renpy.music.queue("audio/music/Fieldstheme_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
$ renpy.music.queue("audio/music/Fieldstheme_Loop.ogg", channel='music', loop=True)

show screen currentdate 
scene clouds:
    yalign 0.5
show fields1:
    yalign 0.33 xalign 0.95
show ethan closedbrow frownmouth sweat
with splitfade

pause 1.0

ethan @talking2mouth "Oh, man, it's been so long since I went running anywhere. This was an awful idea. I gotta tap out, coach, I'm done for. I'm done."

show ethan:
    ease 0.5 ypos 1.1 rotate 5

red @confused "What? Ethan, we haven't even started yet. This was just a jog to the fields. This is where we {i}start{/i} running."

ethan @sadbrow talkingmouth "My previous statement stands."

show fields1:
    ease 0.5 zoom 1.3
show clouds:
    ease 0.5 zoom 1.3
show ethan surprisedbrow frownmouth:
    ease 0.5 ypos 1.3 zoom 1.3

red @happy "C'mon. You're going to be alright. Take my hand."

show ethan sad2eyes heavyblush with dis

pause 1.0

ethan @talking2mouth "Wow, it's totally different when you do it than when Calimari did it."

show ethan -heavyblush with dis:
    ypos 1.3 zoom 1.3 rotate 5
    ease 0.5 rotate 0
    pause 0.5
    ease 0.5 ypos 1.0 zoom 1.0 rotate 0
show fields1:
    ease 0.5 zoom 1.0
show clouds:
    ease 0.5 zoom 1.0

pause 2.0

ethan @talking2mouth "Thanks. I'm still not running, though."

red @happy "I'll work on you."

ethan surprised @closedbrow talkingmouth "Heh."

red @talkingmouth "Anyway, what did you want to talk about?"

ethan -surprisedbrow -frownmouth -surprised frownmouth @sad2eyes talking2mouth "Right. That."

pause 1.0

stop music fadeout 1.5

ethan sad2eyes -sweat @talking2mouth "Okay, so, there's no easy way to say this, but... I think I'm the one causing these frenzied Pokémon."

red @surprised "What?"

menu:
    "Nah, you're not.":
        $ ValueChange ("Ethan", -1, 0.5)

        ethan @angrybrow talking2mouth "Don't immediately discard what I have to say, dude. I don't say much that matters, but this part {i}does{/i}."

        pause 1.0

        red @sad "Sorry."

        ethan @closedbrow talkingmouth "It's alright. I know I say a lot of dumb shit."
        

        $ renpy.music.queue("audio/music/Fieldstheme_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
        $ renpy.music.queue("audio/music/Fieldstheme_Loop.ogg", channel='music', loop=True)

        red @confused "But why do you think that, man?"

    "Why do you think that?":
        $ renpy.music.queue("audio/music/Fieldstheme_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
        $ renpy.music.queue("audio/music/Fieldstheme_Loop.ogg", channel='music', loop=True)

    "So what?":
        $ renpy.music.queue("audio/music/Fieldstheme_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
        $ renpy.music.queue("audio/music/Fieldstheme_Loop.ogg", channel='music', loop=True)

        ethan @surprised "S-so {i}what?{/i} Dude, I don't know how you can be so calm about this! Those Pokémon are freakin' crazy, man!"

        python:
            count = 0

            if (absolobj in AllPokemon()):
                count += 1
            if ("cramorantobj" in globals() and cramorantobj in AllPokemon()):
                count += 1
            if (lopunnyobj in AllPokemon()):
                count += 1
            if (ninetalesobj in AllPokemon()):
                count += 1

        if (count == 4):
            red @talkingmouth "They weren't that bad. I caught them all, anyway."
        elif (count >= 2):
            red @talkingmouth "I've caught more than half of them. They're not too bad."
        elif (count == 0):
            red @talkingmouth "I might not have caught any of them, but they weren't that bad. They didn't hurt me, at least."
        else:
            red @talkingmouth "I've caught a couple of them. They're not that bad."

        if (count >= 2):
            $ ValueChange("Ethan", 1, 0.5)

            ethan @closedbrow talkingmouth "Man, you're too confident. But I guess it's deserved, since you've caught so many of them."

        else: 
            $ ValueChange("Ethan", -1, 0.5)
            ethan @talkingmouth "Man, you're too confident. Pokémon are dangerous anyway, and now just being around me pumps them full of steroids? This is serious."

        red @talkingmouth "Even so, why do you think that you're causing this?"

ethan -sad2eyes @talking2mouth "So I told you that I think I also have Frienergy, right?"

red @talking2mouth "Yeah."

ethan @closedbrow talking2mouth "Well... that means that Pokémon and people can sense your feelings, and your intent, right?"

red @talkingmouth "That's what Oak said to me."

ethan @happy "Well, you're a happy, cheerful guy. But... you know, Pokémon are sensitive." 
ethan @talking2mouth "When their trainer is in a bad mood, they get nervous, flighty, aggressive, because they don't know what to do. Right?"

ethan @sad2eyes talking2mouth "So... what if there was a guy who had Frienergy, and... you know, he had a bad day. Or four."

pause 1.0

red @talkingmouth "But... you don't seem to be having bad days."

ethan happy "That's the plan, my guy."

show ethan sad2eyes noshine frownmouth with Dissolve(1.5)

pause 1.5

ethan @talking2mouth "But... yeah. I guess the Pokémon are more perceptive. Or maybe Frienergy, like, amplifies the effect, or AoE, or whatever."

red @sadbrow talking2mouth "Ethan..."

ethan -sad2eyes -noshine -frownmouth @talking2mouth "I just kinda felt, like... I dunno. That I needed to fess up. Take responsibility, or something."
ethan @closedbrow sweat talking2mouth "Actually... y'know, this is a weird question..."

if (ninetalesobj in playerparty):
    ethan @talking2mouth "You know that Ninetales in your party?"

    red @confused "Huh? Yeah, sure."

    ethan @happy sweat "Mind saying 'sorry' to her, for me? Or him, whatever?"

    red @talkingmouth "Sure, but... what's this about?"

    ethan @sad2eyes noshine talkingmouth "Guess you'll have to find out when you rank up my relationship."

elif (ninetalesobj in box):
    ethan @talking2mouth "Did you ever see a Ninetales on the campus grounds?"

    red @talking2mouth "Yeah, I caught it, actually."

    ethan @surprised "Huh! I shouldn't be surprised."

    ethan @happy sweat "Mind saying 'sorry' to her, for me? Or him, whatever?"

    red @talkingmouth "Sure, but... what's this about?"

    ethan @sad2eyes noshine talkingmouth "Guess you'll have to find out when you rank up my relationship."

else:
    ethan @talking2mouth "Did you ever see a Ninetales on the campus grounds?"

    red @talkingmouth "Yeah. I battled it, but it got away."

    ethan @surprised "Huh. Something getting away from {i}you{/i}? Seems weird."

    red @happy "I'm not trying to catch 'em all, man!"

    ethan @talking2mouth "Well... in a way, that's kinda a relief."

    red @confused "A relief? How come?"
    
    ethan @sad2eyes noshine talkingmouth "Guess you'll have to find out when you rank up my relationship."

red @happy "Man, Blue's kinda right. I don't get most of the things you say."

ethan @talking2mouth "Most of them are video game references. Sometimes I like to pretend I'm in a video game."

red @talkingmouth "Why?"

ethan @happy "Because if I'm right, whatever fourth-dimensional being is watching is going to be freaked the hell out."

red @happy "I'm not sure freaking out fourth-dimensional beings is a great idea."

ethan @talking2mouth "What are they going to do, turn off their computer?"

stop music
$ testbattle = True
show blank2 
hide screen currentdate       

pause 5.0

hide blank2
show screen currentdate
$ testbattle = False
$ renpy.music.queue("audio/music/Fieldstheme_Loop.ogg", channel='music', loop=True)

red @happy "Nah, that doesn't seem likely. Maybe they'll just delete your character file."

ethan @talking2mouth "Yeah. Maybe. {i}Sigh.{/i}"

ethan @upeyes talking2mouth "Anyway, I think I lost the point I was trying to make, but I think I'm the one creating the Frenzies."

red @talking2mouth "Fierce Opposing Entities."

ethan @playfuleyes talking2mouth "Oh, that's what we're calling them?"

red @talkingmouth "I'm trying to make it happen, yeah."

ethan @closedbrow talkingmouth "Stop trying to make FOE happen. It's not going to happen."

pause 1.0

ethan @angry "Wait, you distracted me, {i}again!{/i}"

red @happy "You're trying to feel guilty about this, and I'm not going to let you. Even if you {i}did{/i} make the FOEs--"

ethan @playfuleyes talking2mouth "Frenzies."

red @happyeyes happymouth angryeyebrows anger "--you obviously didn't do it on purpose, and none of them are too much of a threat yet."

ethan @talking2mouth "...I don't know."

red @happy "Neither do I. So let's just keep our chins up, alright? If this turns out to be a problem, we're surrounded by the smartest professors, and strongest trainers, in the world."

pause 1.0

ethan @talking2mouth "...Yeah, I guess you're right."

if (rescuedwill):
    red @talkingmouth "Besides, I fought three of those crazy Pokémon in the forest yesterday, and I don't think you were anywhere near there."

    ethan @surprised "Woah, what? Three frenzies at once?"

    red @talkingmouth "Yeah. They were weaker than normal, though. Professor Will was controlling them."

    ethan @confused "Uh... should we call the cops?"

    red @happy "Nah. He was also being controlled, probably."

    ethan @closedbrow talking2mouth "Wild. It's puppets all the way down."

elif (rescuedtia):
    red @talkingmouth "Besides, I found Tia in the forest yesterday, and she looked pretty frenzied. And I don't think you were anywhere near there."

    ethan @surprised "Oh, what? You actually went along with Leaf's plan?"

    red @happy "Yeah, and this one worked, too!"

    ethan @closedbrow talking2mouth "And you... {i}beat{/i} Tia?"

    pause 1.0

    red @frownmouth closedbrow "{w=0.5}.{w=0.5}.{w=0.5}."

    red @talkingmouth "I'll be honest, she's not a very good battler."

    ethan @talking2mouth "Man, your life is crazy."

pause 1.0

red @talkingmouth "Back to school? We can snag some breakfast before our homerooms."

ethan @talkingmouth "Yeah, let's...{w=0.5}{nw}"
extend @surprised " huh?"

show ethan:
    ease 0.5 xpos 0.66

show dawn with Dissolve(2.0):
    xpos 0.33

dawn @happy "H-hi, guys!"

pause 1.0

dawn @sadbrow talkingmouth "I... was trying to sound casual..."

ethan @talking2mouth "Keep workshopping it, but it's not a bad start."

red @talkingmouth "Hey, Dawn. What's up? We haven't had much time to talk since that battle during the QQs."

dawn closedbrow sadmouth "Right."

pause 1.0

dawn -closedbrow -sadmouth @angrybrow talkingmouth "I've been thinking about it a lot, and I think I want to start over."

ethan @talkingmouth "Huh?"

dawn @talkingmouth "I've been talking with Lisia, and I think I'm going to join the Coordinator Club."
dawn @closedbrow talkingmouth "Well... I mean, most of the reason she stayed here was to teach me how to be a better Coordinator, so I think that goes without saying."
dawn @sadbrow talkingmouth "But I feel like it was my choice, this time, at least."

pause 1.0

dawn @talkingmouth "Our battle reminded me how much I loved the beginning of my journey, when it was just my Pokémon and I, learning to really battle, and..."
dawn @sadbrow talkingmouth "I missed that. So I'm starting over. I've got a new team, I've got a new strategy, and..."

pause 1.0

dawn @closedbrow sadmouth "To be honest, I think I should probably have been paying better attention in class."
dawn @sadbrow talkingmouth "I thought I was beyond all this, but our battle really made me realize that I skipped the fundamentals."
dawn @happy "No wonder I couldn't beat Cynthia!"

ethan @talkingmouth "What's she like? I mean, she's the strongest trainer in the world, obviously, but what's she like as a person?"

dawn @talkingmouth "She's... nice. Humble. You wouldn't expect her to be humble, on account of how crazy strong she is, but she really is."
dawn @closedbrow sadmouth "She does this weird thing where she asks you to do stuff for her all the time, though, even if you don't really know her."
dawn @sadbrow talkingmouth "But she'll usually give you something nice afterwards, if you do it."

show dawn surprisedbrow frownmouth with dis

ethan @happy "Hah! She's so good a trainer that she even trains the people around her."

dawn -surprisedbrow -frownmouth -surprised @surprised "Oh my gosh, you're totally right, that's {i}exactly{/i} what she was doing! I never even thought of it like that!"

ethan @happy "Hahaha! That's the strongest woman in the world for you."

dawn @sadmouth "Yeah... I thought... well, nevermind."

red @talkingmouth "Well, what are you doing here?"

dawn @talkingmouth "Oh, I just finished adding to my new team. There are a bunch of ice-types up near Argent Mountain, so I thought I'd hike up there and round out my team before classes start."

ethan @playfuleyes talking2mouth "In {i}that{/i} outfit?"

dawn @happy "It's a Sinnoh thing. It gets so cold in Sinnoh, everywhere else feels like Alola. Actually, a long, {i}long{/i} time ago in Sinnoh, it was meant to be even colder. I bet someone from back then would be {i}really{/i} hot in our climate."

ethan @talking2mouth "{size=30}Still, a short skirt?{/size}"

pause 1.0

show dawn angrybrow angrymouth with vpunch

$ firstletter = first_name[0]

dawn @talkingmouth "[firstletter]-[first_name]! You're my rival now! And although I enjoyed our battle, I can't forget that you beat me, so, um, for beating me... I'll beat you back! Right here, right now!"

pause 2.0

dawn -angrybrow -angrymouth @sadbrow talkingmouth "I-if that's alright with you..."

menu:
    "Nah, I already beat you once.":
        show dawn sadbrow frownmouth with dis
        $ ValueChange("Dawn", -1, 0.33)

        dawn @sadmouth "Oh... okay."

        ethan @closedbrow talking2mouth "{size=30}Man, you're just picking all the 'dickish' dialogue options, aren't you?{/size}"

        dawn @sadmouth "Well, let's... just go to class, then..."

        jump afterethanmeeting

    "Sure, let's battle!":
        $ ValueChange("Dawn", 1, 0.33)
        dawn @happy "O-okay! Yes! This is it! A new start!"

red @talkingmouth "Just a quick question. Your previous team, you're, uh, you're not using that, are you?"

dawn @talkingmouth "No. I'm keeping my Altaria with me as a sort of, um, mascot for my team, but I won't be using her in battles. Not for a while, anyway, until the rest of my Pokémon catch up."

red @happy "Sounds good! I wasn't looking forward to facing her again so soon."

dawn @talkingmouth "Do you have a battle type you'd like?"

$ battlenum = 1

menu:
    "[bluecolor][[Dawn Rank 1]{/color} Dawn, you can choose." if GetRelationshipRank("Dawn") > 0:
        dawn @closedbrow talkingmouth "Y-yes... yes, I can."

        $ ValueChange("Dawn", 1, 0.33)
        $ battlenum = 3

        dawn @angrybrow happymouth "A triple battle, then!"

    "Nah, you can choose." if GetRelationshipRank("Dawn") == 0:
        $ battlenum = 3

        dawn @closedbrow talkingmouth "Really? Then, I want... a triple battle!"

    "I'm a single man.":
        pass

    "Double's no trouble.":
        $ battlenum = 2

    "Triples... uh... I don't have something for triples.":
        $ battlenum = 3

dawn @closedbrow sadmouth "Okay..."

pause 2.0

dawn angrybrow happymouth "Let's go!"

$ trainer1 = MakeRed(battlenum)
$ trainer2 = Trainer("dawn", TrainerType.Enemy, GetTrainerTeam("Dawn"), battlenum)

call Battle([trainer1, trainer2]) from _call_Battle_128
$ battlehistory["Dawn2"] = _return

$ renpy.music.queue("Audio/Music/snowpoint.ogg", channel='music')

show dawn with dis:
    xpos 0.33

pause 1.0

if (WonBattle("Dawn2")):
    $ ValueChange("Dawn", 3, 0.33)

else:
    dawn @happy "Y-yes, I won!"
    dawn @sadbrow talkingmouth "Um, you're not {i}too{/i} mad, are you?"

    red @talkingmouth "Not at all."

red @happy "That was a great battle. I can't believe you only just caught these Pokémon!"

dawn @talkingmouth "Thanks. My Altaria's trying to teach them to be serious battlers... I, um, I owe a lot to her."

ethan @talkingmouth "Yeah, good job, you two."

if (ninetalesobj not in AllPokemon()):
    ethan @closedbrow talkingmouth "I noticed you've got a Ninetales on your team, Dawn."

    dawn @happy "Yeah, I just caught it. It seems really powerful."
    dawn @closedbrow talking2mouth "Actually, was it just me, or was it looking at you during that fight?"

    ethan @sad2eyes talkingmouth "You're probably imagining things."

    dawn @happy "Yeah, I guess so!"

ethan @talkingmouth "We should probably head back to school now, right?"

dawn @surprised "Oh, that's right! Homeroom's going to start soon."

dawn @happy "Th-thanks, you two! Bye!"

pause 1.0

dawn sadbrow talkingmouth "We're... we're all going the same way, aren't we..."

label afterethanmeeting:

call clearscreens from _call_clearscreens_157
scene blank2

pause 1.0

$ timeOfDay = "Morning"
show morning at vspaz

pause 5.0

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)
show oakbg behind blank2
show homeroom behind oakbg

$ renpy.transition(dissolve)
show screen currentdate

$ HealParty()

hide blank2 with splitfade    
hide morning

pause 1.0

oak @talkingmouth "...And that brings us to the tragedy of the Galarian 'Fossil Fusions'. Though violent and ill-suited for life in the modern era, extremely talented trainers have shown that it {i}is{/i} possible to raise and train them like a modern Pokémon."
oak @talkingmouth "The trainer who led this charge, of course, was Galar's own undefeated Champion Leon." 
oak @talkingmouth "Though prevailing opinion of these unfortunate fossils was that they had no hope for a semi-normal life, his efforts to rehabilitate them to the modern era paved the way for many other trainers' success stories."

$ PlaySound("BellChime.ogg")

pause 1.0

oak @talkingmouth "That being the case, it is still {i}quite{/i} illegal to make any more. So don't get any ideas, now! Now, go on to your next classes. I'll see you this afternoon."

jump homeroom1transition