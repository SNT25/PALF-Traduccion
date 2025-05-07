label forestdungeonloss:
    stop music fadeout 1.5

    call clearscreens() from _call_clearscreens_154
    call cleardungeonscreens() from _call_cleardungeonscreens_7

    scene blank2 #with Dissolve(2.0)

    narrator "The forces arrayed against you prove too much to handle at your current power. You and your allies quickly beat a retreat back to the safety of campus, vowing to return."

    python:
        dungeonhistory.append((activedungeon.Name, activedungeon.TallyMorale(), activedungeon.MaxMorale(), activedungeon.ItemHistory, activedungeon.BattleHistory))
        isgame = False
        activedungeon.DungeonWon = False
        activedungeon.DungeonLost = True
        _rollback = True
        technicaldungeon = False
        renpy.block_rollback()
        renpy.suspend_rollback(False)

    if (timeOfDay == "Night"):
        jump afternightroam
    else:
        jump afterfreetime

label infirmary:
    $ location = "school"

    stop music fadeout 1.5

    if (timeOfDay == "Evening"):
        scene infirmaryevening
        show screen currentdate
        with splitfade

    else:
        scene infirmarynight
        show screen currentdate
        with splitfade

    $ rescues = rescuedtia + rescuedsabrina + rescuedwill

    if (rescues == 1):
        narrator "You open the door to the infirmary. Though you've met various other students outside of it, you've never been inside before."

        redmind @thinking "And I hope I don't have to go inside too many more times."

        narrator "The room smells vaguely of formaldehyde."

        pause 1.0

        if (timeOfDay == "Evening"):
            narrator "It appears to be empty."

            redmind @thinking "That's odd. We've still got a good few hours of daylight left. They wouldn't have closed yet, would they?"

        else:
            narrator "It appears to be empty, though the lights are still on."

        if (lastsaved == "Will"):
            cheren @confusedeyebrows talking2mouth "Odd. Is Ms. Miriam not...? Bianca told me she is always here."

        elif (lastsaved == "Tia"):
            whitney @surprised "Wait... where's Ms. Miriam? She's always here!"

        elif (lastsaved == "Sabrina"):
            sonia @confusedbrow talking2mouth "That's a bit odd. I seem to recall Ms. Miriam was always here last year."

        queue music "audio/music/nurse.ogg"

        show miriam closedbrow with dis

        miriam @blush talking2mouth "{i}Yawn...{/i}"

        show miriam surprisedbrow with dis

        red @confused "Nurse Miriam?"

        $ BecomeNamed("Nurse Miriam")

        miriam -surprisedbrow @happy "Yes, can I...?"

    elif (rescues == 2):

        queue music "audio/music/nurse.ogg"

        show miriam surprisedbrow surprisedmouth with dis

        narrator "You arrive once more at the infirmary."

    else:
        
        queue music "audio/music/nurse.ogg"

        show miriam sadbrow sadmouth with dis

        narrator "You arrive, hopefully for the third and final time, at the infirmary."

    show miriam:
        ease 0.5 xpos 0.66

    if (lastsaved == "Will"):
        show will sadbrow with dis:
            xpos 0.33
    elif (lastsaved == "Tia"):
        show tia sadbrow with dis:
            xpos 0.33
    elif (lastsaved == "Sabrina"):
        show sabrina casualoldhair sadbrow with dis:
            xpos 0.33

    miriam -surprisedbrow -surprisedmouth -sadbrow -sadmouth @angrybrow talking2mouth "Oh."

    if (lastsaved == "Will"):
        miriam @closedbrow talking2mouth "Will, please lie down on this bed, here."

        will @talking2mouth "Ah... no words to exalt my heroic deeds, oh beautiful nurse?"

        miriam @closedbrow talking2mouth "You're not seriously injured, but we don't want you to do anything that might exacerbate your condition."
        miriam @smilebrow smilemouth "Try not to get too excited over nothing."

        will @happy "Ah, but surely, a token of your favor is not {i}nothing{/i}, oh Maid Miriam? Why, it may be the only thing that can nurse me back to health."

        pause 0.5

        miriam @closedbrow talking2mouth "William. Right now, you are my patient. Control yourself."

        will @closedbrow talking2mouth "Yes... apologies."

        pause 1.0

        will @talkingmouth "Students, you have done remarkably. I am... immensely proud."

        will @talking2mouth "You are good men and women. Every one of you."

        cheren @sad2eyes noshine tears "{w=0.5}.{w=0.5}.{w=0.5}."

        hide will with dis

    elif (lastsaved == "Tia"):
        miriam @closedbrow talkingmouth "Tia, you remember what to do, right, hun?"

        show tia:
            ypos 1.0 xpos 0.33
            ease 0.3 ypos 1.2
            pause 0.3
            ease 0.3 ypos 1.0

        narrator "Tia nods politely and lies down on a bed. You notice that several seconds after her body 'lies' on the bed, there's a creak of mattress springs."

        leaf @happy "You rest up, okay, Tia? And sleep well."

        whitney @angrybrow happymouth "Yeah! Get better soon! And then you can come back to the dorm, and hang out with us again!"

        flannery @happy "I've been working hard on that story you requested. I can't wait to share it when you get back."

        show tia happy with dis

        $ ValueChange("Tia", 10, 0.33)

        pause 1.0

        hide tia with dis

    elif (lastsaved == "Sabrina"):
        miriam @sadbrow talking2mouth "Sabrina, I'm glad you're safe. Please lie down on this bed, here."

        if ("Raihan" in GetStudents()):
            sabrina tears closedbrow sadmouth "I... thank you, you five. It means... it means so much to me, I..."
        else:
            sabrina tears closedbrow sadmouth "I... thank you, you four. It means... it means so much to me, I..."

        rosa @sadbrow talkingmouth "Aw, Sabrina, it was the right thing to do. Don't worry about it."

        sonia @happy "Right. It was only proper."

        nessa @sadbrow happymouth "I don't like seeing people trapped. You could call it selfishness."

        if ("Raihan" in GetStudents()):
            raihan @closedbrow sadmouth "I still don't really get what we were doing, or why we were doing it, but I get it was the right thing to do."

        sabrina "I... I must tell you that..."

        miriam @angrybrow talking2mouth "There'll be plenty of time for telling your friends whatever you wish {i}after{/i} you've rested."

        sabrina -tears -closedbrow -sadmouth @closedbrow talking2mouth "...Okay."

        sabrina happy tears "Thank you. Thank you so much."

        hide sabrina with dis

    if (timeOfDay == "Evening"):
        show infirmarycurtainevening behind miriam with dis
    else:
        show infirmarycurtainnight behind miriam with dis

    if (lastsaved == "Sabrina" and "Raihan" in GetStudents()):
        miriam @sadbrow talking2mouth "I'm sorry, but the infirmary has a strict one-visitor-at-a-time limit. Would four of you mind stepping out for a moment?"
        miriam @talkingmouth "I'd just like to ask some questions about the patient from one of you, if that's alright."

    else:
        miriam @sadbrow talking2mouth "I'm sorry, but the infirmary has a strict one-visitor-at-a-time limit. Would three of you mind stepping out for a moment?"
        miriam @talkingmouth "I'd just like to ask some questions about the patient from one of you, if that's alright."
    
    red @talking2mouth "Sure, I can answer."

    if (lastsaved == "Will"):
        cheren @talking2mouth "Of course."

        silver @talkingmouth "Yeah, uh, seeya, [first_name]. Good job."

        skyla @happy "We all did great! We should totally come up with a team name!"

        silver @talkingmouth "What, like 'The Disciplinary Committee?'"

        skyla @surprised "Oh, yes, that's perfect! Or the DC for short! That'd be marvelous!"

        cheren @closedbrow smilemouth "Hm."

    elif (lastsaved == "Tia"):
        whitney @talkingmouth "Sure thing, Miss."

        flannery @talking2mouth "I'll see you later then, Miss Miriam."

        leaf @flirtbrow talkingmouth "And I'll see {i}you{/i} later, [first_name]. I think the conquering heroes deserve a reward!"

        red @confused "What are you thinking?"

        leaf @happy "Coooo~kies!"

        red @sadbrow talkingmouth "Not going to lie... that'd be really nice."

    elif (lastsaved == "Sabrina"):
        rosa @angrybrow happymouth "Of course! We need to find our next mission, after all!"

        nessa @talkingmouth "Oh, no. No more missions. We did {i}your{/i} thing, Rosa, now I'm going to teach you how to chill out."

        sonia @surprisedbrow happymouth "C'mon, you know it was fun, right, Ness?"

        nessa @sadbrow happymouth "I'm not denying that, Sunny. But Sabrina needs calm."
        nessa @talkingmouth "And that means no shenanigans for, like, a week. {i}At least{/i} a week."

        rosa @talkingmouth "Oh... okay."

        if ("Raihan" in GetStudents()):
            raihan @closedbrow happymouth "After that, though, I got a couple of {i}really{/i} great shenanigans in mind."

        pause 1.0

        rosa @closedbrow talkingmouth "{size=30}I've got enough footage from all that to make a little documentary, anyway, so that could be fun...{/size}"

        nessa @surprised "{size=30}Wait, you were recording all that?{/size}"

    narrator "Your companions leave the room."

    if (rescues == 1):
        red @talkingmouth "Hi, Ms. Miriam. I don't think I've met you before."

        miriam @sadbrow talkingmouth "If we were lucky, you'd never have to."

        if (lastsaved == "Will"):
            miriam @talkingmouth "But nurses like me exist for when luck fails. Don't worry. He'll be fine."
        else:
            miriam @talkingmouth "But nurses like me exist for when luck fails. Don't worry. She'll be fine."

    elif (rescues == 2):
        red @talkingmouth "Hi, Ms. Miriam. I'm back."

        miriam @sadbrow talkingmouth "That's unfortunate. A nurse is never happier than when she has no work to do, and can just sit back with a nice book."

        miriam @closedbrow talking2mouth "I'm going to ask you the same questions you heard last time."

    elif (rescues == 3):
        red @talkingmouth "Hi, Ms. Miriam. Guess who's back?"

        miriam @angrybrow talkingmouth "I really hope you're not planning on making a routine of this, young man."

        red @talkingmouth "As long as there are people who need to be rescued, I'm planning on it, yeah."

        miriam @closedbrow talking2mouth "Well, you know the routine by now."

    miriam @talking2mouth "Can you describe the nature of the injuries the patient sustained?"

    if (rescues == 1):
        red @talking2mouth "Not really. A few bumps and scrapes were all I saw."

        if (lastsaved == "Will"):
            miriam @sadbrow talking2mouth "Yes... that's all I saw, too. Though, of course, I haven't performed a full examination yet, it seems odd to me that he's in such {i}good{/i} health after such a long time."
        else:
            miriam @sadbrow talking2mouth "Yes... that's all I saw, too. Though, of course, I haven't performed a full examination yet, it seems odd to me that she's in such {i}good{/i} health after such a long time."

        miriam @talkingmouth "Maybe I should just count my blessings, but I'd like to dig into this more."

        miriam @sadbrow smilemouth "Please, {i}really{/i} try. Can you think of any other injuries that the patient might have had? Anything they mentioned hurt, or strange behaviors?"

        red @closedbrow talking2mouth "Come to think of it..."

        if (lastsaved == "Will"):
            red @talkingmouth "Will {i}did{/i} mention something about a danger and treasure before we saw him. His eyes were glowing, and he controlled a bunch of wild Pokémon to attack us."
            red @closedbrow talking2mouth "Then... yeah, then he said he had a headache. He said he was attacked in the forest by... {i}something.{/i}"
        elif (lastsaved == "Tia"):
            red @talkingmouth "Tia didn't seem herself. She was sputtering, making strange noises when we saw her. Her eyes were glowing, and she... told her Pokémon to attack us."
            red @closedbrow talking2mouth "Then... yeah, then she said she couldn't remember anything. She said she was attacked in the forest by... {i}something.{/i}"
        elif (lastsaved == "Sabrina"):
            red @talkingmouth "Sabrina {i}did{/i} mention something about a danger and treasure before we saw her. Her eyes were glowing, and she told her Pokémon to attack us."
            red @closedbrow talking2mouth "Then... yeah, then she said she had a headache. She said she was attacked in the forest by... {i}something.{/i}"

    else:
        red @talkingmouth "The same stuff as last time. A few bumps and scrapes, but also confusion, disorientation, headaches."

    miriam @closedbrow frownmouth "Hm."

    pause 1.0

    red @talkingmouth "Any ideas, Nurse Miriam?"

    if (rescues == 1):
        miriam @talkingmouth "I've lots of ideas. I'm not sure which ones are true, though."
        miriam @talking2mouth "I'll have to figure that out. Maybe if I had some more data..."

    elif (rescues == 2):
        miriam @talkingmouth "Yes... I'm fairly confident my patients have been hypnotized."

        red @surprised "Huh?"

        miriam @talking2mouth "It's a form of short-term hypnosis that wears off after a time. Long-term hypnosis is a much more complicated affair, but it seems whoever did this didn't want to cause lasting damage."
        miriam @talkingmouth "It seems the shock of being defeated in battle was enough to snap them out of it."

        red @closedbrow happymouth "Well, that's a lucky coincidence."

        miriam @talkingmouth "What interests me more is how they were able to survive for so long without an obvious source of food or water."
        miriam @closedbrow talking2mouth "I'd need more cases to come to a firm conclusion--but, obviously, I don't {i}want{/i} that."

    elif (rescues == 3):
        miriam @talking2mouth "I mentioned before I was fairly confident that my patients had been hypnotized, yes? I am beyond certain of it now. It seemed whatever was out there in the forest wanted them to fulfill some purpose."
        miriam @closedbrow talking2mouth "...I don't believe it wanted to hurt them, as they seemed to have been entirely under its control. It wanted to {i}keep{/i} them, then, but not hurt them."
        miriam @talking2mouth "Whoever, or whatever, is out there... perhaps it's confused, and wanted them to deliver some sort of message? Maybe that's what was behind their garbled speech."

        red @closedbrow talking2mouth "Hm."
        red @talkingmouth "Is there any chance they're still hypnotized?"

        miriam @talkingmouth "No, not at all. A person who is currently under the effects of hypnosis cannot be hypnotized again. My hypnotherapy treatments worked on the other two, so they're definitely free, now."

        red @happy "That's a relief."

    pause 1.0

    if (lastsaved == "Will"):
        miriam @happy "Well, I'm sure after a nice, long nap, Will will be right as rain... and back to his flirtatious ways."

        red @confusedeyebrows frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
        
        miriam @blush smilemouth smilebrow "He's ridiculous. But it's the sort of ridiculous that makes me laugh."

        miriam @talking2mouth "And he's a very caring man, behind that showy facade. When I think what he put himself through for Sabrina..."
        
        if (rescues == 1):
            miriam @sadbrow talking2mouth "Oh, though he keeps a smile in front of you students, he must feel terribly guilty for what happened to her. And not just her!"
        else:
            miriam @sadbrow talking2mouth "Oh, though he keeps a smile in front of you students, he must feel terribly guilty for what happened to her."

    elif (lastsaved == "Tia"):
        miriam @happy "Well, I'm sure after a nice, long nap, Tia will be right as rain... and back to being my best student."

        red @talkingmouth "Your best student?"

        miriam @talkingmouth "Yes. She's polite, eager to learn, enthusiastic for the work we do here, and has a healing power, like Yellow."
        miriam @happy "What are the odds that we'd get {i}two{/i} students who have the healing touch this year?"

        red @talkingmouth "That's... normal?"

        miriam @sadbrow talkingmouth "Um... no. It's not normal at all. That's why I said it was unlikely that we'd have two this year."

        miriam @talkingmouth "But abnormal doesn't mean {i}bad{/i}."

    elif (lastsaved == "Sabrina"):
        miriam @happy "Well, I'm sure after a nice, long nap, Sabrina will be right as rain... and it sounds like she's developed a good support network to rely on."

        red sweat @closedbrow talking2mouth "Actually... I'm pretty sure Sabrina didn't know {i}any{/i} of those girls before today. Maybe Rosa, barely."

        if (rescues == 1):
            miriam @sadbrow talking2mouth "Poor girl. She's gone through so much hardship already, and all because of those powers of hers. And she's not the only one!"
        else:
            miriam @sadbrow talking2mouth "Poor girl. She's gone through so much hardship already, and all because of those powers of hers."

    if (rescues == 1):
        python:
            bestinstructor = None
            for key, item in classtaught.items():
                if (item == GetStatRank(0)):
                    bestinstructor = key
                    break
            gender = "his" if persondex[bestinstructor]["Sex"] == Genders.Male else "her"

        miriam @sadbrow talking2mouth "I heard from [bestinstructor] that one of [gender] best students was ostracized in front of the entire school recently because he had a power that did nothing more than induce {i}empathy.{/i}"
        miriam @sadbrow talking2mouth "Isn't that awful? Can you imagine how that boy must have felt?"

        red @sweat talkingmouth "It's... pretty easy, actually."

        miriam @sadbrow talkingmouth "I'm sorry to hear that. If you ever need to talk about your problems, I'm here."
        miriam @smilemouth smilebrow "I'm just a nurse. Not a guidance counselor, or any sort of trained professional."
        miriam @angrybrow talking2mouth "{size=30}Over my urgings, the board has not seen fit to hire an onsite therapist, despite the obvious signs that this agglomeration of prodigies and wunderkinds is, largely, in desperate need of therapy.{/size}"
        miriam @talkingmouth "But if you need an ear, I'm here to provide it."

        red @talkingmouth "Thanks, Nurse Miriam. Glad to finally meet you."

        if (GetRelationshipRank("Whitney") > 0):
            red @happy "Whitney talks very highly of you."

        miriam @talkingmouth "It was a pleasure to meet you, too. I hope I don't see you again."

        show miriam surprisedbrow frownmouth with dis

        red @sweat happy "Yeah, there's... two more in the forest, so..."

        miriam "What?"

    elif (rescues == 2):
        pause 1.0

        miriam @talkingmouth "Thank you for delivering another patient to my door, safe, if not sound."

        show miriam surprisedbrow frownmouth with dis

        red @talkingmouth "I plan to do it once more."

        miriam surprisedbrow @talking2mouth "Beg pardon?"

    elif (rescues == 3):
        pause 1.0

        miriam @happy "Thank you for everything you've done. I shudder to imagine what would have happened to these poor people if you hadn't rescued them."

        red @happy "Hey, it was a group effort, every time. I'm just glad to help."

        miriam @talkingmouth "I won't be forgetting this. ...I don't mean to pry, but do you have any interest in the nursing course?"

        red @sadbrow talkingmouth "Sounds great, Ms. Miriam, but I don't think it's for me."

        pause 1.0

        $ AddEvent("Nurse Miriam", "LearnedName")

        miriam @sadbrow talking2mouth "Perhaps it's embarrassing at this point... but I don't believe I ever caught your name."

        red @confused "Huh? Yeah, I guess you never asked."

        show miriam surprisedbrow frownmouth with dis
        
        $ AddEvent("Nurse Miriam", "KnowsName")

        red @happy "It's [first_name]. [first_name] [last_name]."

        miriam "Oh! {i}You're{/i}... [first_name]."

        red @talkingmouth "Yep. The one who... well, you know."

        show miriam sadbrow frownmouth with dis

        miriam @talking2mouth "Oh... I'm so sorry. What you went through was grossly unfair. If people knew just how much variance there were in our bodies, they wouldn't think powers like yours to be strange at all."

        red @closedbrow talkingmouth "Well, that was half of it. I also tried to hide it. But I've moved past that, and other people are starting to, too. This isn't the worst thing in the world."

        miriam @talking2mouth "Well, my offer from before still stands. If you ever need to talk, I'm here, unqualified as I am."

        red @happy "After seeing how you take care of Grusha, Jasmine, and my other classmates, I'm pretty sure you're qualified for anything."

        miriam @surprisedbrow frownmouth blush "Hm...? Dilated capillaries on the cheeks, a higher heart rate...?"
        miriam @angrybrow happymouth "Oh, you! This must be your 'Frienergy' at work. Go off, now! I've patients who require my attention!"

        red @happy "Sure thing, Ms. Miriam. Thank you for taking care of my friends."

    pause 1.0

    if (timeOfDay == "Night"):
        jump afternightroam
    else:
        jump afterfreetime