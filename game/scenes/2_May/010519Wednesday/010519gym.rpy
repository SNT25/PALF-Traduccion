label gym010519:

stop music fadeout 1.5
queue music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

$ renpy.transition(dissolve)
show screen currentdate

scene gym with dis

show blank2 behind gym

$ renpy.pause(2.0, hard=True)

hide blank2

show alder with dis:
    xpos 0.66

show bruno think with dis:
    xpos 0.33

alder @happy2 "And that's how the battle between Champion Blanc and I was {i}actually{/i} much closer than you've probably heard!"

bruno @happy2 "Alder, there is no shame in losing to a superior trainer. You need not defend yourself."

alder @angrybrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

bruno @happy2 "Even if that superior trainer was a tenth your age."

alder @angry2 "She was a {i}fifth{/i} my age, at minimum."

bruno @norm2 "Whatever helps you sleep at night."

alder @surprised2 "Bruno!"

alder @closedbrow talkingmouth "Keep this up, and we're going to have to battle it out in the classroom one of these days. I'll {i}show you{/i} how much of a champion I was, then."

pause 1.0

alder @happy2 "Actually... that might be a good idea. How would you feel about a battle in front of the class, one of these days? Perhaps we could even pull in some students to fight beside us."

bruno @norm2 "That seems reasonable and educational."

alder @happy2 "Excellent! Let's pencil it in for Friday. For now, though, let's get those battle partners assigned."

bruno @think2 "Agreed. [first_name], please battle alongside Leaf."

hide alder
hide bruno 
with dis

pause 1.0

show leaf uniform with dis:
    xpos 0.33 xzoom -1

leaf @talking2mouth "Heya, stranger."

if (HasEvent("Leaf", "AcceptedConfession")):
    red uniform @winkbrow talkingmouth "Hey there, little lady. What's a nice girl like you doing in a place like this?"

    leaf @blush talkingmouth flirtbrow "Looking for trouble. And it looks like I've just found a tall glass of it."

    red @confused "A... a glass of... trouble? I wasn't aware trouble was a fluid."

else:
    red uniform @talkingmouth "Heya, dormie. How're you feeling?"

    leaf @sadbrow talkingmouth "Like I drank a tall glass of butterflies, and they're still alive in my stomach."

    red @confused "A... a glass of... butterflies? I wasn't aware butterflies were a fluid."

leaf @closedbrow talking2mouth "Really? Wow. The Pallet Town educational system was truly atrocious."

red @angrybrow talking2mouth "Hey!" 
red @angrybrow talking2mouth "You're absolutely right!"
red @happy "But I'd say a solid half of it was my own darn fault. Memory of a Magikarp, you know, for anything not about Pokémon."

leaf @talkingmouth "Well, one day your memory will evolve. Just don't forget me 'til then."

red @sweat talkingmouth "You are, in every meaning of the word, unforgettable."

show hilbert uniform:
    xpos 0.75

show hilda uniform:
    xpos 0.5

show leaf:
    xpos 0.33
    ease 0.5 xpos 0.25

hilbert @talkingmouth "Are you two done flirting?"

leaf @closedbrow frownmouth "Hm... thinking about it..."

red @closedbrow sweat talking2mouth "Yes, we're done."

if (HasEvent("Leaf", "RejectedConfession")):
    red @talkingmouth "And it wasn't flirting. Just chatting."

pause 1.0

leaf @talkingmouth "So we're battling you two, huh?"

hilda @talkingmouth "Yeah. Looks like I'm the only one here who's not on the Battle Team."
hilda @sad "Shit. I'll try not to drag you down, Hilbert."

hilbert @talkingmouth "You won't. I'm strong enough to win alone."

leaf @surprised "Hm? You seem pretty confident."

hilbert @talkingmouth "I am. I beat you in the tryouts."
if (not WonBattle("Hilbert2")):
    hilbert @talkingmouth "I also beat [first_name]."

    hilbert @talkingmouth "There's no reason I shouldn't be able to do it again."

else:
    leaf @sarcastic "Oh, yeah? But you lost to [first_name], didn't you?"

    hilbert @sadbrow talkingmouth "...I didn't have my Choice Items back then."

    leaf @surprised "Wait, you mean...?"

hilbert @talkingmouth "Now that I have access to my Choice Items again, I'll defeat you easily."

show leaf:
    xpos 0.25 ypos 1.0 zoom 1.0
    ease 0.5 xpos 0.25 ypos 1.1 zoom 1.2

leaf @closedbrow talking2mouth "{size=30}Okay, we need to take him seriously. Focus on {i}his{/i} Pokémon, all right? If we don't, he'll outspeed us and destroy us with his Choice-boosted moves.{/size}"

hilbert @smilemouth "Hmph."
hilbert @happymouth "Don't count out Hilda. If you spend too much time worrying about me, she'll clean up your messes."

hilda @closedbrow talkingmouth "That {i}is{/i} what I'm best at."

hilbert @talkingmouth "Let's do this. Prepare to battle."

#have one of his pokemon not having a choice item

python:
    trainer1 = MakeRed()
    trainer2 = MakeTrainer("Leaf", TrainerType.Ally)
    trainer3 = MakeTrainer("Hilda")
    trainer4 = MakeTrainer("Hilbert")

call Battle([trainer1, trainer2, trainer3, trainer4], uniforms=[True, True, True, True], dialogfunc=hildahilbertdialog) from _call_Battle_146
$ RecordBattle("HilbertHilda1", _return)

stop music fadeout 1.5
queue music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

show leaf uniform:
    xpos 0.25 xzoom -1
show hilda uniform:
    xpos 0.75
show hilbert uniform:
    xpos 0.5
with dis

if (WonBattle("HilbertHilda1")):
    $ ValueChange("Hilda", 1, 0.25, False)
    $ ValueChange("Hilbert", 1, 0.5, False)
    $ ValueChange("Leaf", 1, 0.75)

red uniform @happy "Wow! You two are {i}seriously{/i} tough together. I don't think I've ever fought both of you at once."

leaf @talking2mouth "You're telling me. You guys are seriously something else."

hilda @happy "Really? You Battle Teamers think so much of us? Shit, I don't know what to say."
hilda @talking2mouth "Thanks, I guess."

hilbert @closedbrow talkingmouth "I've told you you're an excellent battler before. You wouldn't be so surprised if you just listened to me once in a while."

hilda @sad "Oh, God, Hilbert, don't start. Just don't start."

hilbert @sadbrow talkingmouth "{size=30}It was a compliment...{/size}"

pause 1.0

redmind @confusedeyebrows frownmouth "Well, that's the mood killed."

if (GetRelationshipRank("Hilbert") > 0):
    redmind @happy "Hey, if it's a mood that killed Hilbert's parents, this revenge thing will be easy!"

    pause 1.0

    redmind @sweat closedbrow frownmouth "I'm not going to heaven."

    hilbert @talkingmouth "...What are you laughing at?"

    red @sweat talkingmouth "Uh... nothing in particular."

redmind @closedbrow frownmouth sweat "I guess, since the mood's already kinda in the toilet... and those two are Bianca's roommates..."

show leaf frownmouth
show hilda frownmouth 
with dis

red @talkingmouth "Hey. Sorry to bring this up, but... how's Bianca?"

hilbert @sadbrow talkingmouth "She's not coming to classes. Doesn't have any plans to do the homework, either. What do you think?"

hilda @sad "God. Take the {i}worst{/i}, most {i}painful{/i} feeling you can..."

hilbert @closedbrow talkingmouth "And multiply it by a railroad spike through the head."

if (GetRelationshipRank("Bianca") > 0):
    hilda @talkingmouth "Your conversation with her yesterday helped a little bit, [first_name], and I'm seriously thankful for that. Everyone in the dorm is."

else:
    hilda @talkingmouth "Hearing from her old roomie last night helped, Leaf, and I'm seriously thankful for that. Everyone in the dorm is."

hilbert @sadbrow talkingmouth "...Yeah."

hilda @sad "But... I mean, she's still a wreck. My heart breaks that I can't help her."

pause 1.0

leaf @talking2mouth "Maybe... maybe we can?"

hilda @surprised "Hm? What do you mean?"

leaf @talking2mouth "Dawn's Birthday is coming up this Saturday. Dawn mentioned that she hadn't ever had a party before, so I appointed myself Most Honorable Chairwoman of Parties."
leaf -frownmouth @talkingmouth "What if we, like, invite Bianca to the party? Maybe... maybe she'll feel better? And we can invite the rest of the old Dorm 251, so all her friends are there."

hilda -frownmouth @talking2mouth "That might work."

hilbert @closedbrow talkingmouth "I'm not sure Dawn would appreciate her birthday party being converted into a cheer-up-Bianca party, though."

leaf @talking2mouth "It won't be. We'll keep everything very positive and low-key. I won't go overboard. It'll just be a good time for everyone to get together and feel better about... about whatever's bothering them."

hilda @closedbrow talking2mouth "What about Dawn's friends, though? Shouldn't we invite some of them?"

show leaf blush embarrassed with dis

pause 1.0

leaf -blush -embarrassed @talkingmouth "You're looking at him."

pause 1.0

red @confused "Hilbert?"

hilbert @talkingmouth "Absolutely not."

leaf @sarcastic "{i}You{/i}, dork."

red @happy "What? She has more friends than me!"

leaf @sarcastic "Uh-huh. Name two."

pause 1.0

red @closedbrow talking2mouth "Um{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}{nw}" 
extend @confused " Lisia?"

leaf @sarcastic "She's a club advisor, she doesn't count."

pause 1.0

red @sweat closedbrow talking2mouth "Okay, well, she {i}should{/i} have more friends than me. She's cool."

leaf @talkingmouth "Not denying that. And I want to be her friend, and not just because I want to jump into her Altaria's feathers." 
leaf @talking2mouth "But the point is that if we want this party to have more attendees than the Supreme Queen of Parties herself, we're going to have to do some legwork."

red @talkingmouth "Titling yourself, {i}and{/i} referring to yourself in the third person. We're reaching critical levels of smuggery here."

leaf @flirtbrow talkingmouth "Normally, I'd pause to graciously accept this compliment, but I'm on a mission, here."

red @happy "My bad. Don't let me stop your crazy train of thought."

leaf @talking2mouth "Hilda. You'll be there to support Bianca, right?"

hilda @talking2mouth "Hell yeah. I'll clear out my schedule, no matter what else is on it."

show hilbert surprisedbrow with dis

leaf @talkingmouth "And Hilbert, you share Ice classes with Dawn, right? You'll be there to support her?"

show leaf surprisedbrow frownmouth
show hilda surprisedbrow frownmouth
with dis

hilbert -surprisedbrow @closedbrow talkingmouth "No."

hilda @angry "Hilbert! What the fuck?"

hilbert @angry "Let me {i}finish.{/i}"

show hilda -surprisedbrow -frownmouth with dis

hilbert @closedbrow talkingmouth "It's just a birthday. Nothing to celebrate. But I {i}will{/i} be there, for--{w=0.5} for Bianca."

leaf -surprisedbrow -frownmouth @sadbrow talkingmouth "Aw. You {i}do{/i} have a heart."

hilbert @talkingmouth "Her father was {i}murdered.{/i} This has nothing to do with... 'hearts.'"
hilbert @sadbrow talkingmouth "Family is everything. Losing family, like that, I..."

pause 1.0

if (GetRelationshipRank("Hilbert") > 0):
    redmind @sadbrow frownmouth "...I'm sure he can understand more than anybody else how Bianca must be feeling right now."

else:
    redmind @confusedeyebrows frownmouth "Is that the end of that sentence?"

hilbert @talkingmouth "There's a critical amount of time, after a tragedy, where a person needs support to not go off the deep end. I expect everyone to do their best to help Bianca."

redmind @surprisedbrow frownmouth "...Is this {i}Hilbert?!{/i}"

if (not WonBattle("HilbertHilda1")):
    show leaf angry with dis

    hilbert @closedbrow happymouth "And hopefully you two are better at that than you are at battling."

else:
    if (WonBattle("Hilbert1") and WonBattle("Hilbert2")):
        hilbert @sadbrow talkingmouth "And hopefully Hilda and I turn out to be better at {i}that{/i} than we are at battling. I can't believe I lost to you... {i}for the third time.{/i}"

    elif (WonBattle("Hilbert1") or WonBattle("Hilbert2")):
        hilbert @sadbrow talkingmouth "And hopefully Hilda and I turn out to be better at {i}that{/i} than we are at battling. I can't believe I lost to you... {i}again.{/i}"
    
    else:
        hilbert @sadbrow talkingmouth "And hopefully Hilda and I turn out to be better at {i}that{/i} than we are at battling. I can't believe we lost to you..."

hilda angry "Hilbert! Don't be rude!"

redmind @frownmouth upeyes "Oh, there we go. That's the Hilbert I know."

hide leaf
hide hilda
hide hilbert
with dis

pause 1.0

show alder:
    xpos 0.66
show bruno think:
    xpos 0.33
with dis

jump lunchtransition