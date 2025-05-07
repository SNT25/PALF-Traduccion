label secondhomeroom010514:

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=True, fadein=1.0, tight=None)

scene blank2

show oakbg behind blank2
show homeroom behind oakbg

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with dis

$ PlaySound("BellChime.ogg")

oak @talkingmouth "...Which is why six was decided as the optimal number of Pokémon for a trainer to carry at a time. And that's the end of the lecture. Have a...{w=0.5} have a good weekend, everyone."

hide oakbg with dis

pause 1.0

narrator "Professor Oak seems to be in unusually low spirits right now."

menu:
    ">Go after him":
        $ AddEvent("Blue", "GoAfterSam")
        show oak frownmouth with Dissolve(2.0)

        red uniform @talkingmouth "Hey, Sam. What's biting you?"

        oak @closedbrow talking2mouth "Oh... I suppose my ill mood is visible even to you?" 

        red @happy "You mean {i}especially{/i} to me, Sam. I know you better than any of your other students."

        oak -frownmouth @talkingmouth "Well, that's true enough."

        pause 1.0

        oak @sad2eyes talking2mouth "Well... it's a bit of an embarrassing confession to make, but I am starting to wonder if I am somewhat lacking as a teacher."

        red @surprised "Huh? What do you mean?"

        oak @talkingmouth "Well, ever since Tuesday, I've been looking over everyone's tests quite thoroughly, and..."
        oak @closedbrow talking2mouth sweat "There's no easy way to say this. Many of my students are doing quite poorly. I compared my results to those of the other homeroom instructors, and almost all of them exceed me on several key points."

        red @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

        oak @talking2mouth "I wonder..."

        if (GetGrade() == 9):
            oak @talking2mouth "It's true that you've passed every quiz I've levied at you so far, but your classmates do not show similar success."

        elif (GetGrade() > 6):
            oak @talking2mouth "It's true that you've done decently on most quizzes I've levied at you so far, but I know what a brilliant mind you have. I cannot help but feel like your few failures may have been my fault..."

        else:
            oak @talking2mouth "Even you, my best and brightest pupil, have not done nearly as well as I expected. I wonder if your failures are my fault."

        pause 0.5

        red @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

        red @talkingmouth "I don't know if I can say if you're a good teacher or not. But you're my friend."
        red @happy "So I'm a bit biased."

        oak @closedbrow talking2mouth "...Hm. I may need to think on this a bit more."
        oak @talking2mouth closedbrow "Perhaps Doctor Cherry could provide some insights... she has a way of teaching that, if her students exam scores are any indication, should be something I should try to replicate."

        hide oak with dis

        pause 1.0

        show blue uniform at rightside with dis

        pause 1.0

        red @confused "What?"

        $ ValueChange("Blue", 1, 0.75)

        blue @talkingmouth "About time he listened. I've been trying to tell him for weeks now, but he always just thought I was attacking him."

        red @talkingmouth "Apple doesn't fall far from the grandtree, huh?"

        blue @closedbrow "{w=0.5}.{w=0.5}.{w=0.5}."

        hide blue with dis

        pause 1.0

        narrator "Blue walks off without a word."

    ">Ignore him":
        redmind uniform @thinking "If he's in a bad mood, he'd probably prefer to go back to his lab and do some research right now, anyway."

call freeroam from _call_freeroam_21

scene stadium_empty
show screen currentdate
with Dissolve(2.0)

$ HealParty()

pause 0.5

show blue:
    xpos 1.0/9.0
show leaf:
    xpos 5.0/9.0
show sonia:
    xpos 8.0/9.0
show erika:
    xpos 6.0/9.0
show ethan:
    xpos 4.0/9.0
show silver:
    xpos 2.0/9.0
show bea behind ethan:
    xpos 3.5/10.0
show hilbert behind sonia:
    xpos 7.0/9.0
with dis

pause 1.0

show blue 
show leaf 
show erika 
show ethan 
show silver 
show bea 
show sonia
show hilbert
with dis

stop music fadeout 4.0

show smoke:
    animation
    alpha 0.0 yalign 3.0 xalign 0.5
    parallel:
        ease 3.0 yalign 0.5
    parallel:
        ease 0.5 alpha 1.0
        pause 0.5
        ease 3.0 alpha 0.0 

pause 2.0

stop music
show screen songsplash("Fuchsia City", "Zame")

queue music "Audio/Music/fuchsia_start.ogg" noloop
queue music "audio/music/fuchsia_loop.ogg"


pause 1.0

show blank
show janine behind blank

pause 0.1

hide smoke
hide blank

show lance:
    xpos 1.1 ypos 1.0
    ease 0.5 xpos 0.66

show janine behind lance:
    ease 0.5 xpos 0.33

pause 1.0

janine @closedbrow talking2mouth "You know what to do."

show blue:
    ease 0.8 xpos 1.5
show leaf:
    ease 0.5 xpos -0.5
show erika:
    ease 1.0 xpos 1.5
show ethan:
    ease 0.4 xpos 1.5
    pause 0.2
    ease 0.4 xpos -0.5
show silver:
    ease 0.5 xpos -0.5
show bea:
    ease 0.5 xpos 1.5
show dawn:
    ease 0.2 xpos -0.5
show sonia:
    ease 0.5 xpos 1.5
show hilbert:
    ease 0.5 xpos -0.5

pause 1.0

janine @talking2mouth "It's been one week since the biggest mistake this Battle Team has ever suffered."

pause 1.0

janine @closedbrow talking2mouth "I'm sorry. This was not {i}your{/i} mistake, but you're going to have to work harder to make up for it."

hide blue 
hide leaf 
hide erika 
hide ethan 
hide silver 
hide bea 
hide sonia
hide hilbert

pause 0.5

janine @smirkmouth "I know you can, though. It's not that I \'believe in\' you. I just know you can all get through this. The Quarter Qlashes were a setback, but not a stop."

ethan @sadbrow talkingmouth "{size=30}Except for Dawn...{/size}"

janine @closedbrow talking2mouth "Except for Dawn."

pause 1.0

janine @closedbrow talking2mouth "Now, I got a tip through {i}very legitimate means{/i} that the next Quarter Qlashes are going to be Squad Battles."
janine @closedbrow talking2mouth "That means that the next Quarter Qlashes are going to be team-based. We'll discuss how we'll decide teams later, but for now, I want everyone to be ready to battle alongside anyone else."

hilbert @surprised "Team-based? What? How does that work? Does that mean that multiple people will be eliminated in each round?"

janine @talking2mouth "Yes. I don't know how big the teams will be yet, but you should expect team sizes of anything from three to five."

hilbert @sadbrow talkingmouth "I... don't like working in a team."

pause 2.0

janine @talking2mouth "Kinda a dumbass move joining something called the Battle {i}Team{/i}, then."

hilbert @closedbrow angrymouth "Tch."

janine @talking2mouth 'Speaking of bad moves. Erika, did you apologize to [first_name], like I told you to?'

erika @surprised "I-- I fully intended to apologize to him, regardless of your command!"

janine @talking2mouth "But did you?"

erika @sadbrow talking2mouth "Yes, of course."

janine @talking2mouth "Okay. And did you accept the apology, [first_name]?"

if (HasEvent("Erika", "AcceptApology")):
    red @talking2mouth "Yes."

    $ ValueChange("Janine", 10, 0.33)

    janine @smirkmouth "Good. I'm glad we can all be adults about this."

elif (HasEvent("Erika", "RejectApology")):
    red @sadbrow talking2mouth "No."

    janine @talking2mouth "Hm. I'm disappointed. She was misled, [first_name]. This is obvious. Don't hold it against her."
    janine @closedbrow talking2mouth "Or, if you {i}do{/i}, don't let it affect the team."

    red @closedbrow sweat talking2mouth "Right... sorry."

else:
    red @talking2mouth "I said... I'd give her time to think on it."

    janine @talking2mouth "Right. Time's up. Answer, now."

    menu:
        "Apology accepted.":
            $ AddEvent("Erika", "AcceptApology")
            $ ValueChange("Janine", 10, 0.5)

            janine @smirkmouth "Good. I'm glad we can all be adults about this."

        "I don't accept that apology.":
            red @sadbrow talking2mouth "No."

            janine @talking2mouth "Hm. I'm disappointed. She was misled, [first_name]. This is obvious. Don't hold it against her."
            janine @closedbrow talking2mouth "Or, if you {i}do{/i}, don't let it affect the team."

            red @closedbrow sweat talking2mouth "Right... sorry."

janine @talking2mouth "Moving on. Or, back to what I was talking about before."

lance @talking2mouth "Squad Battles are a team-focused battle format. You have less control over your Pokémon, but can defeat large swathes of opponents at a time."
lance @closedbrow talking2mouth "Strength is ever more paramount, given the lesser role strategy plays. Type advantages are as integral as ever, if not moreso."

janine @smirkmouth "They were invented in Paldea by a group of students from Naranjuva Academy, if you can believe that. Just students like you."
janine @smirkmouth "Shows that it's never too early to change the world."

lance @talking2mouth "This battle format became very popular as an alternative team-based format to double or triple battles. It allows every team member to shine in their individual niches."
lance @sadbrow talking2mouth "It also disallows the ever-so-popular \'teamkilling\' prank that plagues the lower levels of competitive battling."

janine @smirkmouth "Yeah, it's funny, but that's not the kind of funny we're going for."

lance @talking2mouth sadbrow "\'Funny...\' I'm not certain that's the correct term. I'm certainly not laughing."

janine @talking2mouth "When was the last time you laughed at {i}anything,{/i} Lance?"

lance @closedbrow talking2mouth "A ridiculous question. It was{w=0.5}.{w=0.5}.{w=0.5}."

show lance surprisedbrow with dis

pause 1.0

lance -surprisedbrow @closedbrow talking2mouth "Hm."

janine @talking2mouth "For today's meeting, I have a gift for all of you."
janine @talking2mouth "Squad Battles are a type of battle system that rely on teams of battlers working together. It's easy to get confused in those sorts of battles, and lose track of who your allies are."
janine surprisedbrow @talkingmouth "...So we have a solution."

ethan @confused "Uniforms?"

janine sadbrow @talking2mouth "...Yes."

redmind @sadbrow frownmouth "Oh... I think she was looking forward to telling us about them."

janine @talking2mouth "Come here to the front of the Battle Hall and grab your uniform from this box."
janine @talkingmouth "It should be pretty obvious whose is whose."

hide lance
hide janine
show blank2 
with Dissolve(1.0)

narrator "Everybody retrieves their uniforms, then separates, running to the bathrooms to change."
narrator "Shortly..."

show red battleteam with Dissolve(2.0)

pause 1.0

red @happy "Hey. Name's [first_name]. Lookin' good. Lookin' good."

pause 1.5

red @happy "I'm such a dork. Alright, let's go see the others."

hide blank2 
hide red 
show blue closedbrow battleteam:
    xzoom -1
with splitfade

blue @happy "Oh, {i}there's{/i} [first_name]. Slow as usual! What, you get lost in there?"

pause 1.0

show blue surprisedbrow frownmouth with dis

red battleteam @unamusedbrow talking2mouth "You were in such a rush to beat me, you put your shirt on backwards."

blue @talkingmouth "...Sh-shut up!"

show blue:
    xpos 0.5
    ease 0.3 xpos -0.2

pause 1.0

show silver battleteam:
    xpos -0.2
    ease 1.0 xpos 0.33

silver @talkingmouth "Hell's his problem?"

show ethan battleteam with dis:
    xpos 1.2
    ease 1.0 xpos 0.66

ethan @closedbrow talking2mouth "He's an acquired taste."

red @happy "Hey, man. Looking sharp!"

ethan @talkingmouth "Same, both of you."

show leaf flirtbrow battleteam behind silver:
    xpos 1.2 
    ease 0.5 xpos 0.5

leaf angrybrow angrysmilemouth @flirtbrow talkingmouth "Well, while we're handing out compliments, anything you want to say to me, [first_name]?"

red @happy "Sure! Silver really {i}does{/i} look good!"

silver @sad "Alright, lay off..."

show bea battleteam:
    xpos -0.2
    ease 0.5 xpos 0.15
show sonia battleteam:
    xpos 1.2
    ease 0.5 xpos 0.85

bea @talkingmouth "This uniform is well-fitted, lightweight, and familiar. It will not be an obstacle in training."

sonia @talking2mouth "Rather brings to mind the Gym challenge uniforms back in Galar, doesn't it?"

bea @closedbrow talkingmouth "Somewhat. Though this one is more... freeing."

sonia @surprised "Eh?"

bea @talkingmouth "Nothing important."

show blue closedbrow frownmouth lightblush:
    xpos -0.2
    ease 0.5 xpos 0.05

janine @talking2mouth "...Where's Erika?"

leaf -angrybrow -angrysmilemouth @talking2mouth "She was still in the bathroom when I left. Seemed like she was concerned about her outfit...?"

erika battleteam lightblush @talking2mouth "Y-yes! I would... I would like to lodge a complaint!"

janine @closedbrow talking2mouth "God, another one?"

show silver:
    xpos 0.33
    ease 0.5 xpos 0.25

show ethan:
    xpos 0.66
    ease 0.5 xpos 0.85

show sonia:
    xpos 0.85
    ease 0.5 xpos 0.95

show leaf:
    xpos 0.5
    ease 0.5 xpos 0.75

show erika battleteam lightblush embarrassedeyes embarrassedeyebrows embarrassedmouth behind silver:
    xpos 1.2
    ease 0.5 xpos 0.6

erika @talking2mouth "This... this uniform's skirt... it is far too short! There are not even any tights!"

show janine with dis:
    xpos 0.4

janine @talking2mouth "It's flexible and unrestricting."
janine @surprised "What, you didn't think I was going to let you run around on the battlefield in a kimono for the rest of the year, did you?"

erika @talkingmouth "This is... the traditional wear of a Kantonian woman of higher stature, and--"

janine @talking2mouth "And completely impractical for battle."

erika @angry "But-!"

janine @talking2mouth "This is not a debate."

pause 1.0

erika sadbrow frownmouth -lightblush @sadbrow talking2mouth "I'm... sorry."

janine @closedbrow talking2mouth "It's fine. Wear the uniform for the meeting. If you're still uncomfortable afterwards, we can talk about extending the skirt, or getting some tights."

show erika surprisedbrow frownmouth with dis

janine @closedbrow talkingmouth "You'll realize you like it, though. Ever tried a high-kick? Now you can."

erika @talkingmouth "{size=30}High... kick?{/size}"

hide erika
hide leaf
hide blue
hide silver
hide bea
hide ethan
hide sonia
with dis

show janine:
    xpos 0.33
    ease 0.5 xpos 0.5

janine @talking2mouth "Alright, that's enough of the fashion show. Pick a partner and go through our drills. Lance and I will tutor your Pokémon, if you need it, after you're done."

pause 1.0

hide janine with dis

narrator "Lance and Janine split up and begin tutoring the other Battle Team members' Pokémon."

narrator "You look around for someone to train with, and..."

label trainwith514:

menu:
    ">Train with [blue_name]":
        show blue battleteam with dis

        $ ValueChange("Blue", 1, 0.5)

        blue @talkingmouth "...Yeah, sure."

    ">Train with Leaf":
        show leaf battleteam with dis

        $ ValueChange("Leaf", 1, 0.5)

        leaf @happy "Sure!"

    ">Train with Ethan":
        show ethan battleteam with dis

        $ ValueChange("Ethan", 1, 0.5)

        ethan @talkingmouth "Sure thing, man."

    ">Train with Bea":
        show bea battleteam with dis

        $ ValueChange("Bea", 1, 0.5)

        bea @closedbrow talking2mouth "Very well. Let us commence."

        show stadium_empty:
            xalign 0.5 yalign 0.5
            ease 2.0 zoom 1.2

        show bea:
            ease 2.0 ypos 1.2 zoom 1.3

        bea @closedbrow talking2mouth "Now..."

        bea angry "Begin!"

        show bea:
            ease 0.3 ypos 2.0 zoom 3.0 alpha 0.0

    ">Train with Erika":
        if (HasEvent("Erika", "AcceptApology")):
            show erika battleteam with dis

            $ ValueChange("Erika", 1, 0.5)

            erika @closedbrow happymouth "Oh, you wish to train with me? I appreciate the patience you've shown."

        else:
            show erika battleteam with dis

            erika @sadbrow talking2mouth "I apologize, but... I do not think I can train with someone who still harbors a grudge against me."

            hide erika with dis

            jump trainwith514
            
    ">Train with Sonia":
        show sonia battleteam with dis

        $ ValueChange("Sonia", 1, 0.5)

        sonia @talking2mouth "Right-o. I remember a few techniques Janine taught us at the end of last year. If you wouldn't overly mind skipping ahead a bit...?"

        red @happy "Lay it on me."

    ">Train with Silver":
        show silver battleteam with dis

        $ ValueChange("Silver", 1, 0.5)

        silver @surprisedbrow talking2mouth "Huh? What brought this up?"

        if (GetRelationship("Silver") == "Friend"):
            red @happy "Do I need a reason to hang out with you? You're my friend."

            silver @happymouth "Psh. Nothing gets you down, huh?"

        else:
            red @happy "Nothing. I just figure you can teach me something new."

        pause 1.0

        silver @happymouth "Let's see."

    ">Train with Hilbert":
        show hilbert battleteam with dis

        $ ValueChange("Hilbert", 1, 0.5)

        hilbert @closedbrow talking2mouth "Fine. Just don't slow me down."

scene black with dis

narrator "You train while waiting for Lance to make room for you. You notice he, once again, goes out of his way to teach the rest of the Battle Team members first."

$ BattleTeamTraining()

scene stadium_empty
show lance 
with dis

pause 2.0

lance "{w=0.5}.{w=0.5}.{w=0.5}."

pause 1.0

red battleteam @confusedeyebrows frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

pause 1.0

lance "{w=0.5}.{w=0.5}.{w=0.5}."

pause 1.0

red @confusedeyebrows frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

pause 1.0

red @talkingmouth "So I guess I'm talking first?"

lance @talking2mouth "This was not a moral victory."

red @unamusedeyebrows playfuleyes talking2mouth "Oh, great, that's where we're going with this."

lance @closedbrow talking2mouth "My claim was that you hindered yourself by using an objectively inferior member of an inferior species."

silver battleteam @angry "{w=0.5}.{w=0.5}.{w=0.5}."

lance @sadbrow talking2mouth "It is obvious you did not know of your Pikachu's power until it became apparent. Therefore, you had no idea you were not doing the very thing I accused you of."
lance @upeyes talking2mouth "Ergo, this ridiculous ploy at power you and your Pikachu have put on wins nothing but a single meaningless battle."

red @happy "That only works if you believe that I accept your premise, that there's an extant way of ranking the superiority or inferiority of a Pokémon."
red @talkingmouth "I don't think there is. Sure, there's {i}some{/i} objective measurement out there, but I don't think we're ever going to know it."

lance @confusedeyebrows playfuleyes talking2mouth "You would claim to have a better understanding of a Pokémon's limits and abilities than the greatest trainers and scientists?"

red @talkingmouth "Nah. But I think I've got at {i}least{/i} an equal understanding. 'Cause I know one of the greatest scientists in the world, Professor Oak, and he's told me he's pretty much as clueless about this as I am."

pause 1.0

red @happy "And you're one of the greatest trainers in the world, and I'm pretty sure you have no idea what happened, either. Correct me if I'm wrong."

lance @closedbrow shadow talking2mouth "The scale of correction required here is not one that I am capable of providing single-handedly."

red @talking2mouth "...I don't want to hear you badmouth [pika_name] any more. Now he's got a special power. He beat a Mega-evolved champion-level dragon. He's undeniably strong."

lance @closedbrow talking2mouth "I have less interest in what you want than I do in further debating your rudimentary and naive philosophy. What I say or do will be at my own whim, as ever."

redmind @closedbrow sweat frownmouth "...Ugh."

lance @talking2mouth "Enough of this drivel. Make use of my services, or free me from your presence."

label movetutor514:

call screen SelectMon
$ tutormon = _return

if (tutormon == 'back'):
    lance @closedbrow talking2mouth "Are you certain?"

    menu:
        "I don't want to teach any of my Pokémon one of their old moves.":
            lance @closedbrow talking2mouth "Very well."

        "On second thought...":
            jump movetutor514

elif (tutormon == pikachuobj):
    lance @talking2mouth "I am unable to teach this... creature. I cannot begin to determine what skills it may have possessed in the past."

    jump movetutor514

else:
    $ tutormon = _return
    $ tutormonname = pokedexlookup(tutormon.GetId(), DexMacros.Name)

    lance @talking2mouth "Your [tutormonname]. Very well."
    
    $ rememberablemoves = GetRememberableMoves(tutormon)

    if (len(rememberablemoves) == 0):
        lance @talking2mouth "This Pokémon has no moves it can remember. Avoid wasting my time, if you are capable of such a thing."

        jump movetutor514

    else:        
        lance @talking2mouth "Fine. What do you want me to re-teach this Pokémon?"

        $ learnmove = renpy.call_screen("rememberablemoves", tutormon)

        if (learnmove == "Back"):
            lance @talking2mouth "Avoid wasting my time, if you are capable of such a thing."

            jump movetutor514

        else:
            $ tutormon.LearnNewMove([(0, learnmove)])

            if (learnmove not in tutormon.GetMoveNames()):
                jump movetutor514

hide lance with dis

pause 1.0

show janine with dis:
    xpos 0.5

janine @talking2mouth "He seemed more pissed than usual."

red @happy "Can't imagine why."

janine @talking2mouth "Alright. Everyone head back to your dorms. You know the rule--go {i}straight{/i} back. Dean Drayden is on edge, and we don't want to be responsible for any more crises."

scene black with splitfade

if (rescuedtia and rescuedsabrina and rescuedwill):
    narrator "You head back to your dorm."

else:
    narrator "You change out of your uniform and leave the Battle Hall."

    menu:
        ">Head back to your dorm":
            pass

        ">Head to the forest":
            narrator "...You attempt to casually mask your stride, but you can feel Janine's eyes burning into the back of your neck."

            $ ValueChange("Janine", -3, 0.5)

            redmind @sadbrow frownmouth "Sorry, Janine. This is {i}really{/i} important!"

            call nightroam from _call_nightroam_3

scene blank2

pause 2.0

jump day010515