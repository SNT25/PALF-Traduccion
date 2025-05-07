label day010515:
$ timeOfDay = "Morning"

call calendar(1) from _call_calendar_40

$ calDate = calDate.replace(day=15, month=5, year=2004)

show morning at vspaz

pause 3.5

$ renpy.music.play("Audio/Morning_ambience.ogg", channel='crowd', loop=True, fadein=1.0)

scene bedroom 
show screen currentdate
with transeye2

$ renpy.pause(1.0, hard=True)

$ PlaySound("knock.ogg")

leaf hatless @happy "Wakey-wakey, eggs and bakey! Time to get up and drink the coffee I makey!"

pause 1.0

red swimsuithatless @tired unamusedmouth playfuleyes unamusedeyebrows "{w=0.5}.{w=0.5}.{w=0.5}."

red @tired talking2mouth "Who the hell are you? Because I know there's {i}no{/i} way my roommate, Leaf Gracidea Green, is waking up at this time of the day."

leaf @happy "Oh, I woke up even {i}earlier{/i}, Sleeping Beauty. And why shouldn't I? Today's a biiiig day!"

red @talking2mouth "Oh, yeah? How do you figure?"

leaf @flirttalk "Why don't you give it your best guess, and I'll tell you if you're right, lad?"

red @closedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

leaf @surprised "Oh, are we not there yet? Not at the I-imitate-your-sixty-year-old-best-friend level?"

red @sadbrow talking2mouth "No, we're there. I'm just genuinely disturbed how accurate it was."

leaf @happy "Hah hah! Yeah, I'm kinda the best. Get dressed and meet me in the suite!"

red @talkingmouth "Sure."

pause 1.0

red @closedbrow talking2mouth "Wait. How do you know I'm not dressed already?"

leaf @talkingmouth "Oh, that would be the cameras I've planted all around your room."

red @upeyes talkingmouth "I'm calling the cops."

if (rescuedsabrina and GetRelationshipRank("Sabrina") >= 1 or GetRelationship("Sabrina") == '...?'):
    leaf @talkingmouth "You've got a psychic girl halfway across campus who lives in your head."
    leaf @flirttalk "I {i}cannot{/i} be the perpetrator of your greatest privacy violation."

    red @happy "Hey, she doesn't live in my head. She just kinda... drops in, sometimes."

    leaf @sarcastic "Whatever. I'd at least charge her rent. Now, {i}come on{/i} already!"

else:
    leaf @angry "They'll never catch me alive!"

narrator "You hear Leaf leave the door."

pause 1.0

narrator "You spend a little bit of time looking through your possessions, just to make sure there aren't actually any cameras, but immediately feel bad for doing so."

redmind -swimsuithatless @thinking "Hm. No keyhole on the door. Guess she was just joking."

$ PlaySound("Pokemon/pikachu_norm1.ogg")

libpikachu @unamusedeyes unamusedmouth "Pi."

show suite 
show leaf hatless
with splitfade

pause 1.0

leaf @happy "[first_name]! It's an important day today! Can you guess what it is?"

menu:
    "Your birthday?":
        $ AddEvent("Leaf", "KnowsBirthday")

        leaf @happy "No, but it's September 28th, so write that down! I'll be expecting a {i}big{/i} cake!"

    "Are we going on a date today?" if HasEvent("Leaf", "AcceptedConfession"):
        if (rescuedtia):
            $ ValueChange("Leaf", 1, 0.5)

            leaf @happy "Heck yeah!"

        else:
            $ ValueChange("Leaf", -1, 0.5)

            leaf @surprised "Wait... did you forget about Tia? Is that why you've been so... {i}inactive{/i} the past week?"
            
            red @sadbrow talking2mouth "Er... I didn't {i}forget{/i} about Tia, exactly, but..."
    
    "Are we hanging out today?" if HasEvent("Leaf", "RejectedConfession"):
        if (rescuedtia):
            $ ValueChange("Leaf", 1, 0.5)

            leaf @happy "Heck yeah!"

        else:
            $ ValueChange("Leaf", -1, 0.5)

            leaf @surprised "Wait... did you forget about Tia? Is that why you've been so... {i}inactive{/i} the past week?"

            red @sadbrow talking2mouth "Er... I didn't {i}forget{/i} about Tia, exactly, but..."

    "Are we rescuing Tia today?" if not rescuedtia:
        $ ValueChange("Leaf", 1, 0.5)

        leaf @angrybrow happymouth "Darn right!"

    "National straw hat day?":
        leaf @surprisedbrow talking2mouth "Huh?"

        leaf @talking2mouth "No. That's weird. What are you talking about?"

        red @happy "It's a thing. I swear. Look it up!"

        leaf @closedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}.Huh. I guess it is."
        leaf @closedbrow talking2mouth "Maybe I should get one for myself, then, to, like, celebrate the holiday..."

        leaf @happy "Anyway, {i}no{/i}, that's not it!"

if (not rescuedtia):
    leaf @talking2mouth "We're going into the forest to rescue Tia today. We {i}have{/i} to. It's been, like, ten days."

    red @talkingmouth "Alright."

else:
    leaf @happy "We've been talking about it enough! I've made plans. We're going to go into the city today. I've got everything sorted out, so don't worry about it!"

    if (HasEvent("Leaf", "RejectedConfession")):
        red @talking2mouth "Okay, but you know this isn't a date, right?"

        leaf @sarcastic "Say that another fifteen times, and I might be offended."

        red @sweat closedbrow talking2mouth "Sorry."

    elif (GetRelationshipRank("Nessa") > 0 and not HasEvent("Nessa", "DenyDate")):
        red @happy "Thanks. This is actually only my second date ever, so, uh, I appreciate you taking the lead here."

        leaf @surprised "Huh. Your second date {i}ever?{/i} How'd that happen?"

        red @sweat closedbrow talkingmouth "Blue."

        leaf @sadbrow talkingmouth "Oh, right."

    else:
        red @happy "Thanks. This is actually my first date ever, so, uh, I appreciate you taking the lead here."

        leaf @surprised "Huh. Your first date {i}ever?{/i} How'd that happen?"

        red @sweat closedbrow talkingmouth "Blue."

        leaf @sadbrow talkingmouth "Oh, right."

red @talkingmouth "Are you ready to go?"

if (not rescuedtia):
    leaf @talking2mouth "Yeah, in a moment. Let me just grab some supplies for the road. Ethan's still sleeping, but I asked him if I could steal his First Aid kit for the day."
    leaf @talkingmouth "You know, just in case."

    red @talkingmouth "Good thinking."

else:
    leaf @talking2mouth "Yeah, in a moment."

    leaf @flirttalk "Let me just slip into something {i}more comfortable.{/i}"

show blue og with dis:
    xpos 0.33

show leaf with dis:
    xpos 0.5
    ease 0.5 xpos 0.66

pause 1.0

leaf @talkingmouth "New threads? Very flattering."

blue @talkingmouth "You're not wearing your hat. I guess you {i}aren't{/i} balding, after all."

leaf angrybrow frownmouth @angry "Oh, you {i}cocky prick{/i}. Come on, [first_name], let me at him. One quick shot to the nuts. That's all I need. Just one good rustling of the jimmies, one good plunder of the family jewels."

red @confused "You don't need {i}my{/i} permission for it."

blue @talkingmouth "Whatever. What are you two doing?"

if (not rescuedtia):
    show blue surprisedbrow frownmouth with dis

    leaf @talking2mouth "Rescuing Tia. Because {i}we{/i} know how to be grateful."

    blue -surprisedbrow -frownmouth @closedbrow talkingmouth "She's a... a Latias? I think that's what she said. Anyway, she's a {i}dragon.{/i} What do you think she needs rescuing from?"

    if (rescuedsabrina and rescuedwill):
        red @talking2mouth "Sabrina and Instructor Will were in a hazy, hypnotized, state in the forest. Maybe the same thing happened to Tia."
        
    elif (rescuedsabrina):
        red @talking2mouth "Sabrina was in a hazy, hypnotized, state in the forest. Maybe the same thing happened to Tia."
        
    elif (rescuedwill):
        red @talking2mouth "Instructor Will was in a hazy, hypnotized, state in the forest. Maybe the same thing happened to Tia."

    else:
        red @talking2mouth "We don't know, but she's not the only one out there who needs saving. And it's about time {i}someone{/i} does something."

        leaf @closedbrow talking2mouth "{size=30}I've been trying to get you to do that {i}all week.{/i}{/size}"

    blue @talkingmouth "Well, good luck with that. If it was anyone else, I might actually offer to help, but pretending you can help an actual {i}dragon{/i} is pretty arrogant, from where I'm standing."

    red @upeyes talking2mouth "Pots and kettles come to mind."

else:
    leaf @talking2mouth "Going out to the city. Because {i}we{/i} know how to get along."

    blue @talkingmouth "Tch."

leaf @talking2mouth "You know, you were actually {i}somewhat{/i} tolerable Monday night, when we were playing {i}Inferno & Logos{/i}."
leaf @sarcastic "And when you asked if you could train my Dratini, I mean, you were almost {i}polite{/i}."
leaf @talking2mouth "I misjudged you when I first met you, like, a month ago. I thought you were an insecure, swaggering little twerp who used too much hair gel back then."

blue @glanceeyes glanceeyebrows talking2mouth "I know better than to assume this is actually {i}going{/i} anywhere, but let's pretend."

leaf @angrybrow talking2mouth "But now I get that you just {i}act{/i} like an insecure, swaggering little twerp."
leaf @sarcastic "{size=30}But you still use too much hair gel.{/size}"
leaf @angrybrow angrymouth "So my question is '{i}why{/i}'?! Why do you make being around you so difficult for everyone? Even for yourself?"

pause 0.5

leaf -angrybrow -frownmouth @closedbrow talking2mouth "I had some wild idea that maybe being dormmates with you would make you easier to get along with, and then when I saw Yellow, I thought I finally got what you were all about..."

pause 1.0

leaf @sarcastic "But now I'm back at square one."

blue @talkingmouth "Maybe if you stop treating me like a game, you'll stop landing on the squares that send you back."

leaf @happy "Oh, damn, that was good! You come up with that one? Or was it Yellow?"

blue @sad2eyes talkingmouth "I don't think that's important."
blue @closedbrow talkingmouth "Anyway, I just wanted to tell you that your Dratini is doing fine. Gained a bunch of experience."
blue @closedbrow talking2mouth "Strong-willed little wyrm, but we're getting along well. Not used to dealing with such a prideful Pokémon, though."

leaf @talking2mouth "Oh."

pause 0.5

$ pronoun = "he" if leafdratiniobj.Gender == Genders.Male else "she"

leaf @embarrassedbrow talkingmouth "Does, um... does [pronoun] talk about me?"

blue @surprisedbrow talkingmouth "What're you talking about?"

leaf @talkingmouth "Well, you always train with Yellow. I thought, maybe, you'd know how [pronoun] feels about me."

blue @closedbrow talkingmouth "I don't know. Maybe Yellow does. You can ask her."

leaf @talking2mouth "Yeah, maybe when she gets back."

blue @surprisedbrow surprisedmouth "Back? Back from where?"

leaf @talking2mouth "Um... I dunno. She just grabbed some coffee this morning, and left. I think she said she was looking for something."

blue @closedbrow talkingmouth "Tch. What's she doing...?"

leaf @sarcastic "What, did you have plans?"

blue sad2eyes frownmouth lightblush "{w=0.5}.{w=0.5}.{w=0.5}."

leaf @happy "Oh my God, you totally {i}did.{/i}"

blue -lightblush -frownmouth -sad2eyes @closedbrow talkingmouth "Shuuuuut up. We're just going on a picnic. As a way of me... 'apologizing' or whatever for... you know. What happened last Wednesday."

red @closedbrow talking2mouth "What happened?"

leaf @talking2mouth "Oh, right, you weren't there for that. Yellow--"

blue @angry "He doesn't need to know."

red @happy "...I'll tell you what Yellow's doing right now if you let Leaf finish."

blue @glanceeyes glanceeyebrows talking2mouth "Like you know."

red @confused "Why would I lie about this? Actually, better question, what makes you think I {i}could{/i} lie about this? You were around for the past week, right?"

blue @talkingmouth "Psh. Ethan's got the same power as you, and he lies all the time."

red @confused "What? No he doesn't."

blue @sad2eyes wistfuleyebrows talkingmouth "Yup, you're right. I'm just lying for no reason. Looks like you got me, detective. Well done."

red @confusedeyebrows frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
red @talking2mouth "Whatever. Yellow's gone to look for a picnic spot. {i}Apparently{/i}, you get in fights with other picnickers too often for her to trust you to do it yourself."

blue @surprisedbrow talkingmouth "...She said that?"

red @closedbrow talkingmouth "Not those exact words."

pause 1.0

blue @closedbrow talkingmouth "Since you're so nosy about it, this whole picnic thing is happening because she blew up at me. She said we never get to do what {i}she{/i} wants." 
blue @glanceeyebrows glanceeyes talking2mouth "Well, apparently, what {i}she{/i} wants is to go hike out into the woods and sit in some rotten leaves and eat some... eat some..."
blue frownmouth @surprised "Wait. {size=30}...No. She wouldn't have, would she...?{/size}"

$ PlaySound("idea.ogg")

stop music fadeout 1.5 channel "crowd"
queue music "audio/music/Sneaking Again.ogg"

leaf @surprised "Wait. You don't think she went out into the forest, do you?"

blue @closedbrow talkingmouth "Most of our picnics before have been in forests. She really likes them. But I don't think that..."
blue @angry "I mean, we've had announcements every damn day! Every day this week, the Dean's grabbed the intercom and told us that entry into the forest is prohibited."
blue @sad2eyes glancemouth "She wouldn't just... blow that off, would she?"

pause 1.0

if (rescuedtia):
    leaf @talking2mouth "Wait. She's in the nurse course, right? Yellow was helping me talk to Tia yesterday, and I think she mentioned that."

    blue @talkingmouth "Yeah. Fully."

    leaf @surprised "So she doesn't take elective classes?"

    blue @talkingmouth "No."
    blue @desperateeyes desperateeyebrows desperatemouth "...No!"

else:
    leaf @talking2mouth "Wait. Which electives does she take?"

    blue @talkingmouth "She's fully committed to the nurse course. Her electives are Virus Prevention and Removal and Alt-Human Sciences."

    leaf @surprised "So she doesn't take type elective classes?"

    blue @talkingmouth "No."
    blue @desperateeyes desperateeyebrows desperatemouth "...No!"

red @closedbrow talking2mouth "Wait... Janine doesn't take elective classes, either. Remember what she said yesterday night? She didn't know that the forest had been re-closed. That means she'd never heard the announcement!"

leaf @closedbrow talking2mouth "Okay, hold on. {i}Surely{/i} she must get announcements at the end of her nurse course classes, as well."

blue @closedbrow talking2mouth "...I don't know."

leaf @talking2mouth "You don't know?"

blue @talkingmouth "No, I don't know."

if (rescuedsabrina or rescuedtia or rescuedwill):
    red @talkingmouth "I know who would."

    red @talkingmouth "Come on."

    leaf embarrassed "I need to get my hat."

    blue sad2eyes glanceeyebrows @talking2mouth "I need to change my clothes."

else:
    leaf @talking2mouth "Well, I know who would."

    leaf @angrybrow talking2mouth "Come on."

    blue sad2eyes glanceeyebrows @talking2mouth "I need to change my clothes."

    leaf embarrassed "Oh, yeah, I need to get my hat..."

red @sweat talking2mouth "Alright, get your stuff, {i}then{/i} let's go."

call clearscreens() from _call_clearscreens_164
scene blank2 with splitfade

pause 1.0

stop music fadeout 1.5
queue music "audio/music/nurse.ogg"

if (rescuedtia):
    scene infirmary 
    show leaf:
        xpos 0.8
    show miriam:
        xpos 0.6
    show tia hospital hathospital:
        xpos 0.4
    show blue:
        xpos 0.2
    show screen currentdate
    with splitfade

    leaf @talking2mouth "Hey, Tia!"

    show tia happy with dis:
        ypos 1.0 xpos 0.4
        ease 0.2 ypos 1.1
        ease 0.2 ypos 1.0
        repeat 5

    narrator "Tia smiles happily and signs a few simple words at you."

    if (GetRelationshipRank("Tia") == 0):
        narrator "Alas, even this rudimentary communication escapes you."

    else:
        tia "Hi, Leaf! Hi, [first_name]! Hi, [oldblue_name]!"

        narrator "You decide not to tell Blue that Tia is still using his old nickname."

    show tia -happy with dis

else:
    scene infirmary 
    show leaf:
        xpos 0.8
    show miriam:
        xpos 0.6
    show whitney:
        xpos 0.4
    show blue:
        xpos 0.2
    show screen currentdate
    with splitfade

    leaf @talking2mouth "Hey, Whit!"

    whitney @angrybrow talkingmouth "Hey yourself! When are we going to go rescue Tia?!"

    leaf @talking2mouth "Today! I made an executive decision."

    pause 1.0

    leaf @embarrassedbrow talkingmouth "Although... it's possible we might need to rescue someone else, too."

    whitney @surprised "Whaaaat?!"

miriam @talkingmouth "Hello, you three. Can I help you?"

red @talkingmouth "Yes, we just had a bit of an odd question. For students in the Nurse Course, where are they at around 11 AM?"

miriam @closedbrow talking2mouth "Hm... 11 AM? Well, they'd probably be in one of the recovery rooms, like this."

show blue desperateeyes desperateeyebrows glancemouth with dis

narrator "You notice Blue's eyes immediately begin scanning the ceiling, looking for an intercom system."

leaf @talking2mouth "Okay. Do the recovery rooms have an intercom system?"

miriam @talkingmouth "No, not usually. We don't want an intercom going off and waking up a patient who's resting."
miriam @talkingmouth "However, medical personnel such as myself always have an earpiece that we use to communicate with each other."
miriam @closedbrow talkingmouth "It's whisper-quiet. A wonderful piece of technology, I'd say. It was originally used on nonverbal patients, but found use amongst their caregivers, and..."

if (HasEvent("Nurse Miriam", "LearnedName")):
    miriam @happy "Well, I'm sure you'd rather not be bored by the medical history of aural enhancers. You're right, though, [first_name], these {i}are{/i} odd questions! Why are you asking?"

else:
    miriam @happy "Well, I'm sure you'd rather not be bored by the medical history of aural enhancers. You're right, though, these {i}are{/i} odd questions! Why are you asking?"

show miriam surprisedbrow frownmouth with dis

red @sadbrow talking2mouth "Every day this week, we've had an announcement after our first elective period that the forest is off-limits."

pause 1.0

miriam @talking2mouth "Oh."

miriam -surprisedbrow -frownmouth -surprised @angrybrow talking2mouth "So when you went into the forest this week..."

red @surprised "No, no, {i}I{/i} was allowed to. I had special permission from the Disciplinary Committee."

miriam @talkingmouth "Well, thank you for letting me know."

pause 1.0

miriam @sadbrow talking2mouth "...There's another student out there, isn't there?"

leaf @sadbrow talking2mouth "Y-"

blue -desperateeyes -desperateeyebrows -glancemouth frownmouth @angry "No!"

pause 0.5

miriam @talkingmouth "...Okay. But if there is, or you learn of one, you really should tell someone responsible."

blue @sad2eyes glanceeyebrows talking2mouth "Yeah."

redmind @confusedeyebrows frownmouth "What's up with him?"

if (rescuedtia):
    hide leaf
    hide blue 
    with dis

    pause 1.0

    narrator "You and your dormmates leave the infirmary swiftly."

    miriam frownmouth @angrybrow talking2mouth "...Hm. Tia, I think that they might be able to use your help."

    show tia angrybrow frownmouth with dis

    pause 2.0

scene blank2 with splitfade

pause 1.0

stop music fadeout 1.5

$ renpy.music.queue("Audio/Music/Cinnabar_Start.ogg", channel='music', loop=None, fadein=0.0, tight=None)
$ renpy.music.queue("Audio/Music/Cinnabar_Loop.ogg", channel='music', loop=True, tight=None)

scene academyhall_zoom 
show leaf:
    xpos 0.66
show blue frownmouth:
    xpos 0.33
with splitfade

blue frownmouth glanceeyes @desperateeyes desperateeyebrows desperatemouth "We can't tell anyone Yellow left."

leaf @angrybrow talking2mouth "Why the hell not?"

blue @angrybrow talkingmouth "Didn't you hear the announcements? Every damn time, Dean Drayden said that rule-breakers will be expelled."

leaf @talking2mouth "You battled, like, a ton of people in front of the Battle Hall."

blue @angrybrow angrymouth "Yeah, and Ethan was running interference, then. And even if he failed, I'd be the one punished. But this is {i}Yellow{/i}'s school life on the line." 
blue @closedbrow angrymouth "I can't even claim I, I dunno, {i}forced{/i} her out there. You know how impossible it is to defend her? She just gives up immediately! Heck, she'd turn herself in!"

red @sadbrow talkingmouth "Blue, it was an accident. Dean Drayden's reasonable. He'd understand."

blue @angrybrow talkingmouth "You'd expect him to understand, because people understand you. They always do. That's your literal superpower."
blue @sad2eyes frownmouth "The rest of us have to actually work to convince people of shit. I--"

show academyhall_zoom with vpunch

show leaf surprisedbrow frownmouth
show blue scaredeyes scaredeyebrows frownmouth 
with dis

$ renpy.music.play("Audio/Music/DragonDenStart_B.ogg", channel='music', loop=False, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/DragonDenLoop.ogg", channel='music', loop=True, fadein=0.0, tight=None)

red @angry2eyes anger2 angryeyebrows angrymouth "Blue, shut the {i}hell{/i} up!"

blue sad2eyes -scaredeyebrows "{w=0.5}.{w=0.5}.{w=0.5}."

red @angryeyes angryeyebrows talking2mouth "We're on the same goddamn side. We're on the same goddamn team. We live in the same goddamn dorm. Stop {i}whining{/i}, stop complaining that no-one wants to help you, and just {i}accept{/i} our help!"
red @angryeyes angryeyebrows talking2mouth "I have been hearing people, {i}all{/i} week, call me a freak, say I get stuff I don't deserve, even insult {i}[pika_name]!{/i}"
red @closedbrow talking2mouth "Contrary to appearances, it {i}is{/i} getting to me. I don't need {i}you{/i} putting on this act, too."

stop music fadeout 3.0

pause 1.0

red @closedbrow talking2mouth sweat "...Sorry. I know you're under a lot of stress right now, too."

pause 2.0

blue @sad2eyes wistfulmouth "Y-yeah. Let's, uh... let's go."

$ renpy.music.queue("Audio/Music/Cinnabar_Start.ogg", channel='music', loop=None, fadein=0.0, tight=None)
$ renpy.music.queue("Audio/Music/Cinnabar_Loop.ogg", channel='music', loop=True, tight=None)

leaf -surprisedbrow -frownmouth @talking2mouth "Hold on. We can't get started without a plan."

red @talkingmouth "...From what I've been told of the [first_name] rescue team, that seems like your department."

leaf @talking2mouth "We're going to need to talk to two people before we get started. Your old roommates, Blue."

blue @closedbrow talking2mouth "What? The fat guy and the photography nerd?"

leaf @surprised "What? No! Cheren and Nate!"

blue @closedbrow talking2mouth "That makes more sense. But why them?"

leaf @talking2mouth "We need to make sure that we're doing this all above-board."
leaf @sadbrow talking2mouth "[first_name], Blue was a little bit right. If we don't get permission to do this rescue ahead of time, then we might be in a lot of trouble when we get back."

red @talking2mouth "I already got permission from Cheren earlier this week."

leaf @talking2mouth "Was it through the weekend?"

red @angryeyebrows sad2eyes talking2mouth "...No."

leaf @talking2mouth "There we go, then."

red @talkingmouth "Okay. What about Nate?"

leaf @talking2mouth "Nate told Ethan and I that there's some sort of really powerful, dangerous Pokémon out there in the forest. He's been trying to get info on it, apparently, the entire school year."
leaf @sarcastic "{size=30}That's how he justified trading off everyone else's information, anyway.{/size}"
leaf @talking2mouth "I've seen him battle in my Electric-type classes, and I've got a hunch he could really help out. Also, he owes you one, [first_name]."

blue @talkingmouth "Fine. Who do we go to first?"

leaf @angrybrow talkingmouth "I'll handle Nate. You handle Cheren. Blue, go back to the dorm and wake Ethan. We'll want him, too."

narrator "Blue looks like he's about to argue, but just sighs and stomps his foot, before briskly walking off."

hide blue with dis

red @talkingmouth "Ok-"

show academyhall_zoom with vpunch

show leaf:
    xpos 0.66
    ease 0.5 xpos 0.5 ypos 1.2 zoom 1.3

leaf fullblush embarrassedbrow talkingmouth "Okay, is it, like, wrong of me to say that that was {i}incredibly{/i} hot, and I kind of want to see you yelling more?"

red @unamusedeyebrows playfuleyes unamusedmouth "{w=0.5}.{w=0.5}.{w=0.5}."

red @closedbrow talking2mouth sweat "We'll have to dissect that later."

leaf blush @happybrow talkingmouth "...Yeah, okay. Meet you back at the dorm!"

scene blank2 with splitfade

pause 0.5

narrator "You run briskly to the Disciplinary Committee's office, your mind racing with all the things you want to say to Cheren..."

pause 0.5

narrator "And, of course, all the things you probably {i}should{/i} say. There is little overlap."

show screen songsplash("Embracing One's Duty", "Zame")
stop music fadeout 1.5
queue music "audio/music/embracingonesduty.ogg"

scene studentcouncil 
show skyla:
    xpos 0.25
show cheren noshine sad2eyes:
    xpos 0.5
show silver:
    xpos 0.75
with splitfade

pause 2.0

cheren @neutraleyes talking2mouth "[first_name]."

red @talkingmouth "Cheren."

skyla @talkingmouth "Silver?"

silver angrybrow @talkingmouth "What?"

show silver closedbrow with dis

skyla @happy sweat "Nothing, I just didn't want to be left out."

pause 1.0

show silver -closedbrow with dis

cheren @neutraleyes talking2mouth "Is there something I can do for you?"

if (rescuedtia or rescuedwill or rescuedsabrina):
    if (rescuedwill):
        cheren @talking2mouth "You assisted in rescuing Instructor Will."

    if (rescuedsabrina):
        cheren @talking2mouth "You managed to rescue Sabrina Natsume before our own efforts yielded any fruit."
        
    if (rescuedtia):
        if (rescuedsabrina or rescuedwill):
            cheren @talking2mouth "You even managed to rescue Bianca Vongole... or should I say 'Tia', as it seems she is more commonly called."
        else:
            cheren @talking2mouth "You managed to rescue Bianca Vongole... or should I say 'Tia', as it seems she is more commonly called."

    cheren @neutraleyes talking2mouth "By any fair metric, you're a hero. What further business does the Pikachu wielder, hero of Kobukan, have with us?"

    red @closedbrow talkingmouth "...The job's not done."

else:
    cheren @talkingmouth "Perhaps it slipped your mind, but there are still three missing persons out there in the forest. We intend to spend all day searching for them."

    red @sweatbrow talking2mouth "...{i}Four{/i} missing persons."

cheren @surprised "Beg pardon?"

red @talkingmouth "There's a student called 'Yellow' out there in the forest."

skyla frownmouth @surprised "Oh, Yellow! I know her."

silver @sad "Yeah... so do I."

cheren @talking2mouth "Everyone knows Yellow."
cheren @neutraleyes sadeyebrows talkingmouth "So. You want to ask permission to take a rescue team out to find Yellow. Am I correct in your intention?"

red @closedbrow talking2mouth "Pretty much."

if (rescuedtia and rescuedwill and rescuedsabrina):
    cheren @talkingmouth "Go."

    red @surprised "Huh? Just like that."

    cheren @talking2mouth "You've rescued three others this week alone. It would be pointless to deny your skills, and foolish to deprive myself of another way order might be restored to this school."
    cheren @neutraleyes talking2mouth "That being said, we Disciplinary Committee members will of course go out and search for the missing student as well."
    cheren @talking2mouth "I might suggest you form a team of like-minded individuals. You are good at that."

    red @talkingmouth "One step ahead."

    cheren @closedbrow talking2mouth "As expected."

    pause 0.5

    cheren @talking2mouth "I would ask... a favor."

    red @angry "A {i}favor?!{/i}"
    
    cheren @talkingmouth "Yes. A favor."
    cheren @talking2mouth "Only one. I would have you battle one of us. Your choice. A single battle."
    cheren @talking2mouth "Battles are permitted in our office, as long as we clean up after ourselves. This is not some sort of trick."

    label predisciplinarycommitteebattlechoicefree:

    menu:
        "I'll beat you, Cheren.":
            cheren @surprisedbrow talking2mouth "Oh?"

            cheren @talkingmouth "There's no denying I'm the weakest amongst us three, but I'd suggest not picking me just because you're certain of an easy win. Are you sure?"

            menu:
                "Yes.":
                    $ AddEvent("Cheren", "BattledChoice")
                    cheren @talking2mouth "Very well."

                "Actually...":
                    jump predisciplinarycommitteebattlechoicefree

            python:
                trainer1 = MakeRed()
                trainer2 = Trainer("Cheren", TrainerType.Enemy, GetTrainerTeam("Cheren"))

            call Battle([trainer1, trainer2], custombrain=cherenbrain1) from _call_Battle_134
            $ battlehistory["Cheren3"] = _return

            show cheren sad2eyes noshine with dis:
                xpos 0.5

            if (WonBattle("Cheren3")):
                $ ValueChange("Cheren", -3, 0.5)

                cheren @talkingmouth "...I'd call this an expected outcome. Not one I'm particularly fond of, but... the expectancy lessens the impact somewhat..."

            else:
                cheren shadow @talking2mouth "I battled with absolutely no conviction. If you... if you cannot even beat me, a passive man who throws away all honor in pursuit of victory..."
                cheren neutraleyes angryeyebrows talking2mouth "You cannot save {i}anybody.{/i}"

                jump gameover

        "Silver, ready for a rematch?":
            $ AddEvent("Silver", "BattledChoice")
            silver @angrybrow talkingmouth "Bring it on."
            
            if (GetRelationshipRank("Silver")):
                silver @sad "I still don't know how to feel about this... power, this Frienergy, about you. Show me. Help me decide."

            python:
                trainer1 = MakeRed()
                trainer2 = Trainer("Silver", TrainerType.Enemy, GetTrainerTeam("Silver"))

            call Battle([trainer1, trainer2]) from _call_Battle_135
            $ battlehistory["Silver4"] = _return

            show silver with dis:
                xpos 0.75

            if (WonBattle("Silver4")):
                $ ValueChange("Silver", 3, 0.75)

                silver @talkingmouth "...I expected better from myself. I'm sorry, my Pokémon. You all did really well."

            else:
                silver @talkingmouth "...I expected better from you. You should apologize to your Pokémon."

        "Come on, Skyla, let's do this!":
            $ AddEvent("Skyla", "BattledChoice")
            skyla @angrybrow happymouth "I should warn you, I've gotten {i}serious{/i} since I joined the Disciplinary Committee!"

            if (GetRelationshipRank("Skyla")):
                skyla @happy "And I'm not going to go easy on you just 'cause we're friends!"

            python:
                trainer1 = MakeRed()
                trainer2 = Trainer("Skyla", TrainerType.Enemy, GetTrainerTeam("Skyla"))

            call Battle([trainer1, trainer2]) from _call_Battle_136
            $ battlehistory["Skyla2"] = _return

            show skyla with dis:
                xpos 0.25

            if (WonBattle("Skyla2")):
                $ ValueChange("Skyla", 3, 0.25)

                skyla @talkingmouth "Nice battle! I see you've only gotten stronger since we battled in gym class!"

            else:
                skyla @sadbrow talkingmouth "Oof. That was a really close one, [first_name]. Don't feel bad!"

        "No, screw you.":
            $ AddEvent("Cheren", "DidNotBattle")
            show silver surprisedbrow
            show skyla surprisedbrow
            show cheren smilemouth
            with dis

            $ ValueChange("Silver", -1, 0.25, False),
            $ ValueChange("Cheren", -1, 0.5, False),
            $ ValueChange("Skyla", -1, 0.75)

            narrator "You leave."

            jump afterpermission

else:
    pause 1.0

    cheren @talking2mouth "On one condition."

    red @closedbrow talking2mouth "Just one?"

    cheren @talking2mouth "Only one. I would have you battle one of us. Your choice. A single battle."
    cheren @talking2mouth "If your performance is inadequate, I may consider your weakness a... {i}liability,{/i} and forbid you from going."

    pause 1.0

    cheren @talkingmouth sad2eyes "Well, I say 'forbid', but let's be honest, there's little I can do to stop you."
    cheren @talking2mouth "In any case, please make your choice."

    label predisciplinarycommitteebattlechoice:

    menu:
        "I'll beat you, Cheren.":
            cheren @surprisedbrow talking2mouth "Oh?"

            cheren @talking2mouth "There's no denying I'm the weakest amongst us three, but I'd suggest not picking me just because you're certain of an easy win. Are you sure?"

            menu:
                "Yes.":
                    $ AddEvent("Cheren", "BattledChoice")
                    cheren @talking2mouth "Very well."

                "Actually...":
                    jump predisciplinarycommitteebattlechoice

            
            python:
                trainer1 = MakeRed()
                trainer2 = Trainer("Cheren", TrainerType.Enemy, GetTrainerTeam("Cheren"))

            call Battle([trainer1, trainer2], custombrain=cherenbrain1) from _call_Battle_137
            $ battlehistory["Cheren3"] = _return

            show cheren sad2eyes noshine with dis:
                xpos 0.5

            if (WonBattle("Cheren3")):
                $ ValueChange("Cheren", -3, 0.5)

                cheren @talkingmouth "...I'd call this an expected outcome. Not one I'm particularly fond of, but... the expectancy lessens the impact somewhat..."

            else:
                cheren shadow @talking2mouth "I battled with absolutely no conviction. If you... if you cannot even beat me, a passive man who throws away all honor in pursuit of victory..."
                cheren neutraleyes angryeyebrows talking2mouth "You cannot save {i}anybody.{/i}"

                jump gameover

        "Silver, ready for a rematch?":
            $ AddEvent("Silver", "BattledChoice")
            silver @angrybrow talkingmouth "Bring it on."
            
            if (GetRelationshipRank("Silver")):
                silver @sad "I still don't know how to feel about this... power, this Frienergy, about you. Show me. Help me decide."

            python:
                trainer1 = MakeRed()
                trainer2 = Trainer("Silver", TrainerType.Enemy, GetTrainerTeam("Silver"))

            call Battle([trainer1, trainer2]) from _call_Battle_138
            $ battlehistory["Silver4"] = _return

            show silver with dis:
                xpos 0.75

            if (WonBattle("Silver4")):
                $ ValueChange("Silver", 3, 0.75)

                silver @talkingmouth "...I expected better from myself. I'm sorry, my Pokémon. You all did really well."

            else:
                silver @talkingmouth "...I expected better from you. You should apologize to your Pokémon."

        "Come on, Skyla, let's do this!":
            $ AddEvent("Skyla", "BattledChoice")
            skyla @angrybrow happymouth "I should warn you, I've gotten {i}serious{/i} since I joined the Disciplinary Committee!"

            if (GetRelationshipRank("Skyla")):
                skyla @happy "And I'm not going to go easy on you just 'cause we're friends!"

            python:
                trainer1 = MakeRed()
                trainer2 = Trainer("Skyla", TrainerType.Enemy, GetTrainerTeam("Skyla"))

            call Battle([trainer1, trainer2]) from _call_Battle_139
            $ battlehistory["Skyla2"] = _return

            show skyla with dis:
                xpos 0.25

            if (WonBattle("Skyla2")):
                $ ValueChange("Skyla", 3, 0.25)

                skyla @talkingmouth "Nice battle! I see you've only gotten stronger since we battled in gym class!"

            else:
                skyla @sadbrow talkingmouth "Oof. That was a really close one, [first_name]. Don't feel bad!"

show screen songsplash("Embracing One's Duty", "Zame")
stop music fadeout 1.5
queue music "audio/music/embracingonesduty.ogg"

pause 1.0

if (not HasEvent("Cheren", "BattledChoice")):
    cheren @talking2mouth "I've seen enough."
    cheren -noshine @neutraleyes talking2mouth "You performed well. Both of you."

else:
    cheren @talking2mouth "You performed well."

cheren noshine @talking2mouth "[first_name], you may go. Be the man everyone thinks you are. Return home safely."

red @confusedeyebrows frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

pause 0.5

narrator "You leave."

label afterpermission:

pause 1.0

skyla @talkingmouth "Why did you want us to battle him, boss?"

cheren @talking2mouth "Because that man is the greatest threat to this school's safety and security. A simple-hearted, kind, man."
cheren @talkingmouth "...But the sword he pulls from the stone can bring ruin whether wielded by a kind man, or a wicked man."

silver @talkingmouth "Less bullshit metaphors, more plain talk."

cheren @upeyes talking2mouth "I wanted to see, if we had to fight him, if we could beat him."

if (HasEvent("Cheren", "DidNotBattle")):
    cheren @talkingmouth "I didn't anticipate this... {i}dismissal{/i}, though."

else:
    silver @talkingmouth "Verdict?"

    cheren "{w=0.5}.{w=0.5}.{w=0.5}."

    cheren @sadbrow talking2mouth "Maybe... all three of us together..."

show blank2 with splitfade

pause 1.0

$ renpy.music.queue("Audio/Music/Cinnabar_Start.ogg", channel='music', loop=None, fadein=0.0, tight=None)
$ renpy.music.queue("Audio/Music/Cinnabar_Loop.ogg", channel='music', loop=True, tight=None)

show hall_B 
show leaf
with splitfade

pause 1.0

leaf @talking2mouth "{i}There{/i} you are! Blue and I already found our people. What's taking you so long?"

if (not HasEvent("Cheren", "DidNotBattle")):
    red @sweat talkingmouth "Sorry. Cheren wanted me to battle."

    leaf @talkingmouth "Did you win?"

    if ((HasEvent("Silver", "BattledChoice") and WonBattle("Silver4"))
        or (HasEvent("Skyla", "BattledChoice") and WonBattle("Skyla2"))
        or (HasEvent("Cheren", "BattledChoice") and WonBattle("Cheren3"))):
            red @happy "Duh."

            leaf @happy "That's my dormie!"

    else:

        red @closedbrow sweat "Sorry."

else:
    red @sweat talking2mouth "Sorry. Cheren needed to get in another five minutes of monologuing."

leaf @talkingmouth "Well, whatever. Let's... wait, isn't that...?"

if (not rescuedsabrina):
    show rosa surprisedbrow frownmouth with dis:
        xpos 0.33 xzoom -1
    
    show leaf with dis:
        ease 0.5 xpos 0.66

    rosa "Leaf?"

    leaf @happy "Rosa! What're you doing?"

    rosa -surprisedbrow -frownmouth -surprised @talkingmouth "I was looking for [first_name]."
    rosa @angrybrow talkingmouth "Hey, when were you planning on rescuing Sabrina?"

    show rosa sadbrow frownmouth with dis

    red @sad2eyes sadeyebrows talking2mouth "I've... had a {i}lot{/i} going on..."

    rosa @sadbrow talkingmouth "Look, even {i}Nessa{/i} is saying we need to go {i}today.{/i} Are you coming? I'm about to meet up with Sonia and Raihan out on the forest edge."
    rosa @talkingmouth "Raihan beat Cheren in a battle, so we have permission to go."

    red @sadbrow talkingmouth "I'm sorry. I've got to rescue someone else."

    if (not rescuedwill):
        rosa @surprised "Instructor Will?"

        red @closedbrow sweat talking2mouth "N-no. Someone else."

        $ ValueChange("Rosa", -1, 0.33)

    rosa @sadbrow talking2mouth "Geez."
    rosa @talking2mouth "That's kind of disappointing, [first_name]. I thought we were on the same page..."

    red @sadbrow talking2mouth "Sorry."

    hide rosa with dis

    pause 1.0

    leaf @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    red @closedbrow talking2mouth "Come on. You {i}know{/i} I've been busy. You skipped an entire day of classes on Monday."

    leaf @sadbrow talking2mouth "...Yeah, I guess."

    pause 1.0

else:
    stop music fadeout 1.5

    queue music "audio/music/lavender_start.ogg" noloop
    queue music "audio/music/lavender_loop.ogg"

    show sabrina casualoldhair with dis:
        xpos 0.33
    
    show leaf with dis:
        ease 0.5 xpos 0.66

    pause 1.0

    red @surprised "Sabrina?"

    redmind @thinking "I'm surprised to see her here..."

    if (GetRelationship("Sabrina") == "...?"):
        redmind @thinking "I've been giving her some space since we rescued her from the forest..."

        redmind @surprisedbrow frownmouth "[sabrinacolor]...Yes. I've noticed. I'm thankful.{/color}"

    sabrina @sadbrow talking2mouth "...I heard that... that someone was in danger."

    pause 0.5
    
    sabrina @sadbrow talking2mouth "I'm sorry. I shouldn't have been listening. I just thought... maybe... there was a chance, that..."

    leaf @talkingmouth "You want to help?"

    sabrina @sadbrow talkingmouth "If... I mean, if you..."

    show sabrina surprisedbrow with dis

    leaf @angrybrow talking2mouth "How far does your mind-reading reach?"

    sabrina @talking2mouth "Oh. Um. Several miles, if working through a pre-existing connection."

    leaf @talkingmouth "Great. Can you reach out to Yellow?"

    sabrina -surprisedbrow @sad "I've never talked to her before..."

    leaf @angrybrow talking2mouth "Hm. But do you have to be talking to the person to establish the connection? Couldn't you just reach out and look for, like, 'sockets' to connect to?"

    sabrina @talking2mouth "No. That's not how my powers work."

    red @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    sabrina @closedbrow talkingmouth "I mean... I don't think so...?"

    leaf @sadbrow talkingmouth "...Might be worth a try?"

    pause 1.0

    sabrina @closedbrow talking2mouth "It's easier to establish connections closer to the... target."

    if (HasEvent("Raihan", "WasRescueTeam")):
        red @happy "Take Raihan. Heck, take Nessa, Sonia, and Rosa, too. They've all been into the forest before."

    else:
        red @happy "Take Raihan. Heck, take Nessa, Sonia, and Rosa, too. Those three have been into the forest before, and Raihan's a Gym Leader."

    red @talkingmouth "They can guard you while you're trying to establish a connection."

    sabrina @sad2eyes "{w=0.5}.{w=0.5}.{w=0.5}."

    red @sadbrow talking2mouth "What? What's wrong?"

    sabrina @talking2mouth "What if... I get taken over again? I was out there for... for a week. I should be dead, shouldn't I...? What if...?"

    leaf @sadbrow talkingmouth "Hey, if {i}that{/i} happens, we'll just rescue you again."

    redmind @playfuleyes confusedeyebrows frownmouth "'We?'"

    leaf @talking2mouth "It won't happen, though. Raihan and Sonia are really strong trainers. You'll be fine with them."

    red @happy "Really? You're not talking up Rosa?"

    leaf @talkingmouth "I {i}actually{/i} beat her in Gym Class a while ago. I know, it's the craziest thing."
    
    if (HasEvent("Rosa", "GiveToLeaf")):
        leaf @happy "Besides, I've got her strongest Pokémon right now."

    sabrina @talking2mouth "...Okay. I'll try."

    if (not rescuedwill):
        sabrina @talking2mouth "I can look for Instructor Will, then, too..."

    leaf @happy "Thanks, Sabrina!"

    leaf @surprised "Oh, but make sure to get permission from Cheren! As long as you're with Raihan, though, you should be fine."

    pause 0.5

    leaf @sadbrow talkingmouth "And for what it's worth, I thought it was really screwed up what happened."

    sabrina @sad "{w=0.5}.{w=0.5}.{w=0.5}."

    pause 0.5

    sabrina @talking2mouth "Thank you."

    hide sabrina with dis

    pause 1.0

    leaf @closedbrow talking2mouth "Eeesh! I get the heebie-jeebies talking with her."

    red @confused "Why?"

    leaf @surprised "Like, half of the conversation we just had was in my mind."

    red @closedbrow talkingmouth "Oh, yeah, she {i}does{/i} do that. She's nice, though, really."

    leaf @talking2mouth "Sure, not arguing that, but I kinda wish I could, like, put up a gate in my mind and only open it {i}sometimes{/i}, you know?"

    red @talkingmouth "She probably wishes the same."

    leaf @closedbrow talking2mouth "...Right."

    pause 0.5 

    leaf @talking2mouth "Alright, let's go. Back to the dorm."

stop music fadeout 1.5
show screen songsplash("Sinis Trio", "Zame")
queue music "audio/music/natetheme_start.ogg" noloop
queue music "audio/music/natetheme_loop.ogg"

scene hall_A2b
show nate frownmouth:
    xpos 0.25
show ethan frownmouth
show blue frownmouth:
    xpos 0.75 xzoom -1
with splitfade

nate @talking2mouth "[nate_name]."

red @talkingmouth "Nate."

ethan @confusedeyebrows talking2mouth "Man, why don't we ever get together to, like, binge bad movies or whatever? It's always 'rescue this person' or 'save whatever day.'"

blue @sad2eyes talkingmouth "We've been dormmates for barely a week. {size=30}And we played a game on Monday.{/size}"

pause 1.0

nate @talking2mouth "Leaf gave me a sitrep. There's no denying that I owe you one, [nate_name], and if a {i}fifth{/i} student has disappeared into the forest, then I need to move."
nate @angrybrow talking2mouth "But this is a serious situation. There's {i}real{/i} danger out there. Not necessarily the kind of danger a Pokémon battle can solve."

leaf @closedbrow talkingmouth "...What, you can't do it?"

nate @talking2mouth "I can. My Pokéradar is getting absolutely massive pings of psychic energy from the center of the forest. But there's some sort of interference blocking our path. I can't explain that, so I can't defend you from that."

blue @angrybrow angrymouth "We can {i}defend ourselves.{/i}"

nate @closedbrow sweat talking2mouth "...I know you {i}think{/i} you can."

blue @angry "Hey, what's {i}that{/i} supposed to mean?!"

nate @talking2mouth "Look, if a Pokémon attacked you directly, what would you do?"

blue @surprisedbrow talkingmouth "What are you asking? I'd just battle it!"

show blue surprisedbrow with dis

nate @closedbrow talking2mouth "No, B! I'm asking what you would do if a Pokémon attacked {i}you.{/i} Directly. What would you {i}do?{/i}"

pause 1.0

show nate sadbrow with dis

pause 1.0

blue @sad2eyes wistfulmouth "I'd just... my Pokémon would protect me."

nate @closedbrow talking2mouth "...Okay."

pause 1.0

nate @talkingmouth "...Okay. Tell you what, I could use some company in the forest. B, [nate_name], you guys come with me."
nate @sad "'Fraid I'm going to have to ask you and MC² to keep the bench warm, though, LG."

leaf @surprised "Keep the bench warm?! [first_name]'s the one who got permission from Cheren to even go out today! And it's {i}my{/i} rescue mission!"

nate @sadbrow talkingmouth sweat "I'm... operating under an authority a bit higher than {i}Cheren's{/i}, LG."

pause 0.5

nate @sadbrow talking2mouth "And... this isn't a rescue mission. It's an elimination mission."
nate @talking2mouth "The Pokémon in the forest has been too much trouble, for too long. This is the last day I have to deal with it."

pause 0.5

nate @talkingmouth "Rescuing Yellow isn't my priority. Securing the forest is. But I'll try to help you with your goal, if you can assist me with mine."

ethan @talking2mouth "Why are you giving me and Stamen the boot, though?"

nate @talkingmouth "...Battling isn't everything, but I {i}do{/i} need the best battlers with me."

ethan @closedbrow talking2mouth  "Ouch."

leaf @angrybrow angrymouth "Oh, I'm sorry, am I sniffing glue, or are you the {i}only person here{/i} who {i}isn't{/i} part of the Battle Team?"

nate @talkingmouth sweat happybrow "Yeah, I'm not much of a team player."

if (not rescuedtia):
    leaf @talking2mouth "I'd fight this more, but... I {i}do{/i} need to go find Tia, anyway..."

    leaf @angry "Hey, you're not going to stop me from going out into the forest with some other people, are you?"

    show nate closedbrow sweat with dis

    pause 1.0

    nate -closedbrow -sweat @talking2mouth "No, that should be fine. Just don't follow me."

else:
    leaf @talking2mouth "That's BS. What do you want me to do, then? Just stay back here on campus and twiddle my thumbs?"

    nate @talkingmouth sweat "...Tell Dean Drayden to come out to the forest's edge. And bring his daughter, if possible."

    leaf @surprised "Huh? His daughter?"

    nate @sad "It's {i}really{/i} important."

    leaf @sadbrow talking2mouth "...I feel like you're lying."

    pause 0.5

    leaf @closedbrow talking2mouth "Ugh. Fine. I won't fight this."

ethan @talkingmouth "Well... {i}I'm{/i} not going to fight this, at all. Can I just--"

leaf @angrybrow angrymouth "Oh no you don't, mister. You're joining me."

ethan @talking2mouth "Yeah, saw that coming."

nate @talking2mouth "Let's move."

scene blank2 with splitfade

$ HealParty()

pause 1.0

narrator "You are about to enter an area saturated in Mysteriosity. [bluecolor]Take this time to make any last-minute preparations, and put the Pokémon you wish to bring with you in your first party slot.{/color}"

pause 1.0

narrator "Ready?"

narrator "Godspeed."

$ technicaldungeon = True

narrator "You, Nate, and Blue head out to the forest."
$ totalrescues = rescuedtia + rescuedwill + rescuedsabrina

if (totalrescues >= 1):
    narrator "Although Nate leads the team at first, he eventually defers to your experience in the forest."

    nate @talkingmouth "You really seem to know this place."

    red @talking2mouth "I've been here a few times, yeah."

    redmind @thinking "But... it looks completely different from how it looked last time..."

else:
    narrator "You attempt to lead the team through the forest, but quickly find yourself hopelessly lost. Nate has to keep guiding you back onto the path."

    nate @talkingmouth "Hey, remember, I've got a ping on the target. You don't need to just pick a direction and run."

    red @sweat closedbrow talking2mouth "Old habits, I guess."

    redmind @thinking "But... I swear I'm not {i}this{/i} bad with directions. I feel like the entire forest is... shifting, almost."

pause 1.0

$ timeOfDay = "Noon"

show noon at vspaz 

pause 3.5

scene forest
show blue frownmouth:
    xpos 0.66 xzoom -1
show nate frownmouth:
    xpos 0.33
show screen currentdate
with splitfade

pause 1.0

blue @talkingmouth "This looks like where we battled those two kissin' cousins."

nate @talkingmouth "Yeah. Seems like a long time ago."

pause 1.0

nate @angrybrow talking2mouth "Hold on. It seems {i}way{/i} too much like that. But that should've been close to the entrance. Is it really..."

narrator "Nate looks at his PokéRadar intently."

show nate surprisedbrow frownmouth 
show blue surprisedbrow 
with dis

$ PlaySound("idea.ogg")

nate @talkingmouth "Oh, {i}crap!{/i} That explains it!"

blue @talkingmouth "Huh?"

nate -surprisedbrow -frownmouth -surprised frownmouth @talking2mouth "Okay, I'm going to need you to just... step away {i}there,{/i} please."

red @closedbrow talking2mouth "...Sure?"

show nate:
    xpos 0.3
    ease 0.5 ypos 0.9 zoom 0.8

nate @talking2mouth "{size=30}Come in. Operator, Come in. B2 reporting. I'm 0.7 miles away from-{/size}"

show nate surprisedbrow frownmouth with dis

pause 1.0

nate -surprisedbrow -frownmouth -surprised frownmouth @talking2mouth "{size=30}...No, Sir. No, Sir. Apologies, Sir. No, Sir.{/size}"

pause 0.5

nate @closedbrow talking2mouth "{size=30}Imminent danger, Sir. High potential for civilian casualties.{/size}"

pause 0.5

nate @closedbrow talking2mouth "{size=30}Mysteriosity concentrations of over 7.6 Hales. Natural, no registered Unown presence.{/size}"

pause 0.5 

nate @talking2mouth "{size=30}Permission to utilize PW05?{/size}"

show forest with vpunch

nate @angry "{size=+10}Denied?!{/size} Sir, there are people in {i}actual{/i} danger here! We are {i}in{/i} a Mystery Dungeon! Actively, right now!"

pause 0.5

nate @sad "{size=30}No. No, of course not, Sir. Then, permission to use BEM774?{/size}"
nate @closedbrow sweat talkingmouth "{size=30}...I don't like working with 651, Sir.{/size}"

pause 0.5

nate @talking2mouth "Of course not, Sir. Fine. Fine."

pause 0.5

nate @closedbrow talking2mouth sweat "...Ugh. One more day, and I could've been out of here."

show nate:
    xpos 0.33
    ease 0.5 ypos 1.0 zoom 1.0

nate @talkingmouth "You shouldn't eavesdrop, you know."

blue @talkingmouth "What the hell was that? {i}All{/i} of that?"

nate @talking2mouth "...Just checking in with a friend. She knows a lot about Mystery Dungeons. Thought it might be helpful."

red @confused "Mystery Dungeons?"

nate @talking2mouth "We're in one right now. It's what you call an area saturated in Mysteriosity. Mysteriosity is--"

red @talkingmouth "I actually know what that is."

nate @sad "Great. Then you know it's {i}extremely{/i} strange that there's so much of it so close to an urban area."
nate @closedbrow talking2mouth "I guess that's how the people in here managed to survive for so long. People in Mystery Dungeons don't get hungry or thirsty--just tired. And even then, that's only if they're moving around."

show nate sadbrow with dis

blue sad "...What does this mean for Yellow?"

pause 0.5

nate angrybrow talking2mouth "It means we need to hurry."

call clearscreens from _call_clearscreens_166
scene blank2 with splitfade

pause 1.0

narrator "You rush further into the forest." 
$ hideside = True

narrator "...Quietly, a voice begins to make its way to your ears..."

stop music fadeout 1.0
queue music "audio/music/reliccastle_start.ogg" fadein 10.0
queue music "audio/music/reliccastle_loop.ogg"

yellow @talkingmouth "{size=30}P-p-p-please! No! Leave me alone!{/size}"

pause 0.5

$ hideside = False

pause 0.5

blue @desperateeyes desperatemouth scaredeyebrows shadow "{size=20}Ggk.{/size}"

red @angry "What... that wasn't...?"

nate @angry "{i}Move!{/i}"

pause 0.5

$ hideside = True

pause 0.5

yellow @talkingmouth "{size=30}S-someone... please, help!{/size}"

$ sidemonnum = 97

scene forest3 with splitfadefast

$ hideside = False

nate @angrybrow talking2mouth "Here! The massive psychic disturbance is {i}right here!{/i}"

show yellow scaredeyes angrymouth shadow cry:
    xpos 0.25 xzoom -1
show fullhypno:
    xpos 0.75 yanchor 1.0 ypos 1.2 xanchor 0.5
with Dissolve(2.0)

pause 2.0

red @angrybrow talking2mouth "...Okay, I think I get the situation, now."

show blue scaredeyes angryeyebrows furiousmouth with dis:
    xpos 0.75 ypos 2.0 zoom 2.0
    ease 0.2 xpos 0.5 ypos 1.0 zoom 1.0

show yellow surprisedeyes surprisedeyebrows frownmouth -shadow -cry tears with dis

show fullhypno:
    xpos 0.75
    ease 0.3 xpos 1.5

blue @talkingmouth "Get {i}away!{/i}"

sidemon @talkingmouth "Hyyyypnoooo..."

yellow @talkingmouth "B-blue? You're... You're here again?"

blue desperateeyes desperateeyebrows @scaredeyes angryeyebrows furiousmouth "Of course I am! And now I'm going to turn this Hypno into a greasy yellow stain all over those trees!"

yellow @sad "W-wait, don't! Just knock it out! It doesn't--"

blue shadow scaredeyes angryeyebrows furiousmouth "[first_name], you're with me, right?! Let's destroy this thing!"

redmind @thinking "Oh boy. I should probably make sure Blue doesn't commit a crime."

nate @angrybrow talking2mouth "Stay on guard."

if (totalrescues != 3):
    nate @angrybrow talking2mouth "Look, over there."

    hide yellow
    hide blue 
    with dis

    if (not rescuedtia):
        show latias poweredeyes powered frownmouth with Dissolve(1.0):
            ypos 1.0 xpos 0.75
            parallel:
                ease 2.0 ypos 1.05
                ease 2.0 ypos 1.0
                repeat

            parallel:
                ease 2.0 xpos 0.77
                ease 2.0 xpos 0.75
                ease 2.0 xpos 0.73
                ease 2.0 xpos 0.75
                repeat

    if (not rescuedwill):
        show will poweredbrow powered frownmouth with Dissolve(1.0)

    if (not rescuedsabrina):
        show sabrina casualoldhair psychicangryeyes powered with Dissolve(1.0):
            xpos 0.25

    if (totalrescues != 2):
        narrator "You suddenly notice the missing Espers all lined up on the edge of the clearing, blank-faced."

        nate @angrybrow talking2mouth "That Hypno seems to be controlling them. You might have to fight them, too."

    else:
        narrator "You suddenly notice the lone missing Esper still, by the edge of the glade, blank-faced."
        
        nate @angrybrow talking2mouth "That Hypno seems to be controlling them. You might have to fight them, too."

    if (not rescuedtia):
        red @surprised "Wait, you know about Tia?"

        nate @sadbrow talkingmouth "I'll debrief you later. And that's not an innuendo."

    nate @closedbrow talking2mouth "...According to these readings... Yeah, okay."

    if (not rescuedwill):
        nate @angrybrow talking2mouth "It looks the Hypno is sapping some of Instructor Will's knowledge. It's learned the move Clear Mind, one of Instructor Will's own creations."

        if (HasEvent("Instructor Will", 2.1)):
            red @talking2mouth "I know what that does."

            nate @talking2mouth "Alright."

        else:
            red @talking2mouth "I don't know what that does."

            nate @talking2mouth "It lets him clear his own status conditions, and reset his stat changes."

    if (not rescuedwill):
        nate @talking2mouth "It also seems that... huh."

    if (not rescuedtia):
        nate @talking2mouth "It seems the Hypno is directly controlling Tia. She's going to assist him in this fight."

    if (not rescuedtia or not rescuedwill):
        nate @talking2mouth "There's more."

    if (not rescuedsabrina):
        nate @talking2mouth "Okay, yeah, that's bad. Sabrina's emotions are fluctuating like crazy. Hypno's stats are going to steadily increase, the longer this battle goes."

    red @talking2mouth "Okay."

nate @talking2mouth "Remember, this is just a Pokémon. No matter what this looks like, that Hypno isn't evil. Don't let Blue... you know."

blue shadow scaredeyes angryeyebrows furiousmouth "I'll {i}tear you apart!{/i}"

nate @closedbrow talking2mouth "That."

$ renpy.music.play("Audio/Pokemon/pikachu_angry3.ogg", channel="altcry", loop=None)

libpikachu glowing @angryeyes angrymouth sparks "Pik... Pika. Pikerachu!"

python:
    sidemonnum = 97
    sidemonnum2 = 97
    sidemonnum3 = 97
    trainer1 = MakeRed()
    trainer2 = Trainer("blue", TrainerType.Ally, GetTrainerTeam("Blue"))
    tiaobj = Pokemon("Latias", nickname = "Tia", level=70, item="Soul Dew", ivs=[15, 15, 15, 15, 15, 15], gender=Genders.Female, moves=[GetMove("Sweet Kiss"), GetMove("Light Screen"), GetMove("Reflect"), GetMove("Heal Pulse")], nature=Natures.Bashful, intelligence = 1)
    trainer3 = Trainer("latias", TrainerType.Enemy, [tiaobj])

    if (not rescuedwill):
        hypnoobj = Pokemon(97, level=33, moves=[GetMove("Hypnosis"), GetMove("Dream Eater"), GetMove("Clear Mind"), GetMove("Headbutt")], intelligence=1, foreverals=["Hypno Foreveral"], frenzynerf=(AimLevel() + 1, ["Confusion", "Hypnosis", "Disable", "Poison Gas"]), shinylock=False)
    else:
        hypnoobj = Pokemon(97, level=33, moves=[GetMove("Hypnosis"), GetMove("Swagger"), GetMove("Confusion"), GetMove("Headbutt")], intelligence=0, foreverals=["Hypno Foreveral"], frenzynerf=(AimLevel() + 1, ["Confusion", "Hypnosis", "Poison Gas", "Disable"]), shinylock=False)

    if (not rescuedsabrina):
        hypnoobj.ApplyStatus(".moody")

    hypnoobj.ApplyStatus("frenzied")

    trainer4 = Trainer("sideportraitfull", TrainerType.Enemy, [hypnoobj], isPokemon=True)

    battlers = [trainer1, trainer2, trainer4]
    expressions = ["red angrybrow frownmouth", "red angrybrow angrymouth", "blue angrybrow frownmouth", "blue scaredeyes angryeyebrows furiousmouth furiousmouth", "sideportraitfull", "sideportraitfull"]
    dialog = None
    if (not rescuedtia):
        battlers = [trainer1, trainer2, trainer3, trainer4]
        expressions = ["red angrybrow frownmouth", "red angrybrow angrymouth", "blue angrybrow frownmouth", "blue scaredeyes angryeyebrows furiousmouth furiousmouth", "latias poweredeyes powered frownmouth", "sideportraitfull", "latias poweredeyes powered angrymouth", "sideportraitfull"]
        dialog = possessedtiadialog

$ HealParty(trainer1)
$ HealParty(trainer2)
$ HealParty(trainer3)
if (not rescuedtia and not rescuedsabrina):
    $ tiaobj.ApplyStatus(".moody")
call Battle(battlers, healParty = False, specialmusic="Nothing", unrunnable=True, customexpressions=expressions, dialogfunc=dialog) from _call_Battle_140
$ battlehistory["Hypno1"]  = _return

scene forest3
show blue frownmouth:
    xpos 0.5 xzoom -1
show yellow frownmouth:
    xpos 0.25 xzoom -1
show nate frownmouth: 
    xpos 0.75 xzoom -1
with dis

show screen songsplash("Pallet Town", "Zame")
queue music "audio/music/palletpiano.ogg"

if (hypnoobj in AllPokemon()):
    blue @surprisedbrow scaredmouth "Why did you {i}catch{/i} the damn thing?"

    red @playfuleyes unamusedeyebrows talkingmouth "I was pretty sure you were going to commit a felony, if I didn't."

    $ ValueChange("Blue", 3, 0.5)

elif (WonBattle("Hypno1")):
    blue @closedbrow cryingmouth "There. We beat the damn thing. But why were you getting in my way during that battle, [first_name]?"

    red @playfuleyes unamusedeyebrows talkingmouth "I was pretty sure you were going to commit a felony, if I didn't."

    $ ValueChange("Blue", 1, 0.5)

else:
    jump gameover

blue @sad2eyes sadeyebrows wistfulmouth "...Yeah, maybe."

if (totalrescues != 3):
    if (totalrescues == 0):
        red @talkingmouth "Come on. Let's go see if those three are okay."

    elif (totalrescues == 1):
        red @talkingmouth "Come on. Let's go see if those two are okay."

    elif (totalrescues == 2):
        if (not rescuedtia):
            red @talkingmouth "Come on. Let's go see if Tia is okay."
        elif (not rescuedsabrina):
            red @talkingmouth "Come on. Let's go see if Sabrina is okay."
        else:
            red @talkingmouth "Come on. Let's go see if Instructor Will is okay."

    nate @talking2mouth "Hold on. That wasn't the main threat."

yellow @surprised "What?"

stop music fadeout 1.5

nate @talking2mouth "The massive psychic readings I was getting from this part of the forest are {i}still here.{/i} That means..."

queue music "audio/music/deoxys_start.ogg" noloop
queue music "audio/music/deoxys_loop.ogg"

if (totalrescues != 3):
    if (not rescuedtia):
        narrator "You glance at Tia. She's collapsed on the forest floor. Nate notices, and catches your gaze."

        nate @closedbrow talking2mouth "No. Not her. She's a powerful Pokémon, but she's not what's causing this."

    else:
        if (totalrescues == 1):
            narrator "You glance at the fallen Espers behind the Hypno. They appear to be unconscious, but physically undamaged."

            nate @closedbrow talking2mouth "No. Not them. Sabrina's a powerful Esper, but she's not what's causing this."

        else:
            narrator "You glance at the fallen Esper behind the Hypno. There are no visible injuries. Nate notices, and catches your gaze."

            nate @closedbrow talking2mouth "No. No {i}human{/i} could put off these sorts of readings, even an Esper."

pause 1.0

yellow @talkingmouth "U-um..."

show blue:
    xpos 0.5
    ease 0.2 xpos 0.4

show yellow surprisedbrow frownmouth with dis:
    xpos 0.25
    ease 0.5 xpos .15

blue @talkingmouth "Yellow, are you alright? Did that Hypno hurt you?"

yellow -surprisedbrow -frownmouth -surprised frownmouth @sadbrow talkingmouth "N-no. I just got lost while... um, while I was looking for a picnic spot. Then this Hypno jumped out from behind a tree, and..."

pause 0.5

blue @sad2eyes wistfulmouth "You were crying."

pause 0.5

yellow @tears sadbrow blush happymouth "Oh, you know me... I'm a bit of a crybaby..."

pause 0.5

yellow @sadbrow talkingmouth "I... that Hypno, I think... it was really upset. But... I don't think it was {i}really{/i} the Hypno. It felt more like... someone was talking {i}through{/i} it."

nate @surprisedbrow talking2mouth "...Talking {i}through{/i} it?"

yellow @talkingmouth "Yes. And... and it was holding a Foreveral! [first_name], did you notice?"

red @closedbrow talking2mouth "I did, yeah."

nate @closedbrow talking2mouth "{size=30}Of {i}course.{/i} It uses the Foreverals to whip these Pokémon up into a frenzied state, and then they're suggestible--controllable. So...{/size}"

show blue:
    xpos 0.4 xzoom -1
    ease 0.2 xpos 0.6 xzoom 1

blue @angry "Hey, instead of mumbling over there, why don't you tell us what {i}you{/i} were doing during this fight? Huh?" 
blue @angrybrow talkingmouth "You talked big about not letting any sub-par battlers go with you, but then you didn't even participate! What were {i}you{/i} doing?"

pause 1.0

nate @talkingmouth "What was I doing?"

pause 0.5

nate @talkingmouth "Aiming."

blue @surprisedbrow talkingmouth "Huh?"

nate @talking2mouth "Whenever there's an invisible Pokémon in the area, it leaves a slight shimmer of light around it, like a heat haze."

nate @angrybrow talking2mouth "I first noticed it about two feet up and behind 'Tia.' And there's another one... right {i}there.{/i}"

redmind @surprised "What?"

hide nate
hide blue
hide yellow 
with dis

pause 1.0

nate @angrybrow talking2mouth "Show yourself, AZOTH1."

pause 1.0

show fulldeoxys with gaussdissolve:
    xanchor 0.6 xpos 0.5 xzoom -1 zoom .8 ypos 1.2 yanchor 1.0
    parallel:
        linear 0.1 xpos 0.51
        linear 0.1 xpos 0.5
        pause 5.0
        linear 0.1 xpos 0.49
        linear 0.1 xpos 0.5
        pause 5.0
        repeat
    parallel:
        ease 2.0 ypos 1.2
        ease 2.0 ypos 1.23
        ease 2.0 ypos 1.2
        ease 2.0 ypos 1.17
        repeat

pause 1.0

nate @talking2mouth "...It must've picked that trick up after fighting Tia."

yellow @surprised "W-what... what...?"

blue @surprisedbrow talkingmouth "No, {i}what?{/i}"

nate @talking2mouth "...I'm not sure what you're asking?"

blue @talkingmouth "Is that a Pokémon?"

red @talking2mouth "Is this {i}another{/i} new Pokémon I've never heard of? The second in two weeks?"

nate @talkingmouth "It... {i}might{/i} be a Pokémon. Either that or an Ultra Beast."

blue @talkingmouth "{size=30}Yellow, stay behind me.{/size}"

nate @talking2mouth "This is the entity known as AZOTH1."
nate @closedbrow talkingmouth "The Mysteriosity readings have decreased massively... I'm pretty sure AZOTH1 was {i}purposefully{/i} making them."

$ technicaldungeon = False

nate @angrybrow talking2mouth "But that leaves the question... {i}why?{/i}"

$ PlaySound("pokemon/cries/386.mp3")

show fulldeoxys:
    ease 0.5 xzoom 1
    parallel:
        linear 0.1 xpos 0.51
        linear 0.1 xpos 0.5
        pause 4.0
        linear 0.1 xpos 0.49
        linear 0.1 xpos 0.5
        pause 4.0
        repeat
    parallel:
        ease 1.5 ypos 1.2
        ease 1.5 ypos 1.23
        ease 1.5 ypos 1.2
        ease 1.5 ypos 1.17
        repeat

"AZOTH1" "\"{font=fonts/alien.ttf}Deoxys.{/font}\""

pause 1.0

nate @talking2mouth "AZOTH1. What are your intentions with this planet?"

show fulldeoxys:
    ease 0.5 xzoom -1
    parallel:
        linear 0.1 xpos 0.51
        linear 0.1 xpos 0.5
        pause 3.0
        linear 0.1 xpos 0.49
        linear 0.1 xpos 0.5
        pause 3.0
        repeat
    parallel:
        ease 1.0 ypos 1.2
        ease 1.0 ypos 1.23
        ease 1.0 ypos 1.2
        ease 1.0 ypos 1.17
        repeat

"AZOTH1" "\"{font=fonts/alien.ttf}Deoxys.{/font}\""

yellow @surprised "They're... they're afraid. They're running from something. A 'bad person.'"

redmind @surprisedbrow frownmouth "Wait... isn't that what Tia, said, too?"

show fulldeoxys:
    ease 0.5 xzoom 1
    parallel:
        linear 0.1 xpos 0.51
        linear 0.1 xpos 0.5
        pause 2.0
        linear 0.1 xpos 0.49
        linear 0.1 xpos 0.5
        pause 2.0
        repeat
    parallel:
        ease 0.5 ypos 1.2
        ease 0.5 ypos 1.23
        ease 0.5 ypos 1.2
        ease 0.5 ypos 1.17
        repeat

"AZOTH1" "\"{font=fonts/alien.ttf}D E O X Y S.{/font}\""

yellow @sad "They're... they're being chased. Someone is trying to take their treasure. Is... what's your treasure, Azoth?"

"AZOTH1" "\"{font=fonts/alien.ttf}Deoxys.{/font}\""

pause 1.0

nate @talking2mouth "Well?"

yellow @sad "I don't... I don't understand. They're becoming agitated."

$ PlaySound("pokemon/cries/386.mp3")

show fulldeoxys:
    ease 0.5 xzoom -1
    parallel:
        linear 0.1 xpos 0.51
        linear 0.1 xpos 0.5
        pause 1.0
        linear 0.1 xpos 0.49
        linear 0.1 xpos 0.5
        pause 1.0
        repeat
    parallel:
        ease 0.5 ypos 1.2
        ease 0.5 ypos 1.23
        ease 0.5 ypos 1.2
        ease 0.5 ypos 1.17
        repeat

nate @talking2mouth "AZOTH1! If you can understand me, I need you to surrender yourself into my custody. I'm a member of the--"

show fulldeoxys:
    ease 0.2 xpos 0.5 zoom 3 ypos 3.0 alpha 0.0

narrator "Suddenly, the strange creature lunges straight at [pika_name]!"

nate @surprised "Shit! [first_name], watch out!"

show blue:
    ease 0.2 xpos 0.5

blue @talkingmouth "Oh, no, you {i}don't!{/i}"

hide fulldeoxys

python:
    technicaldungeon = False
    trainer1 = Trainer("blue", TrainerType.Ally, GetTrainerTeam("Blue"))
    sidemonnum = 386
    deoxysobj = Pokemon(386, level=40, moves=["Psychic"], ivs=[31, 31, 31, 31, 31, 31], nature=Natures.Lonely, gender=Genders.Unknown)
    trainer2 = Trainer("sideportraitfull", TrainerType.Enemy, [deoxysobj], isPokemon=True)

call Battle([trainer1, trainer2], unrunnable=True, dialogfunc=deoxysdialog, specialmusic="Nothing", stopmusic=False) from _call_Battle_141

show blue frownmouth:
    xpos 0.25
show fulldeoxys:
    xanchor 0.6 xpos 0.75 zoom .8 ypos 1.2 yanchor 1.0
    parallel:
        linear 0.1 xpos 0.76
        linear 0.1 xpos 0.75
        pause 5.0
        linear 0.1 xpos 0.74
        linear 0.1 xpos 0.75
        pause 5.0
        repeat
    parallel:
        ease 2.0 ypos 1.2
        ease 2.0 ypos 1.23
        ease 2.0 ypos 1.2
        ease 2.0 ypos 1.17
        repeat
with dis

stop music fadeout 1.5 

$ renpy.music.queue("Audio/Music/ViridianB_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/ViridianB_Loop.ogg", channel='music', loop=True, tight=None)

nate @surprised "Blue! What are you {i}doing?{/i}"

blue @sad2eyes wistfulmouth "I'm trying to {i}not{/i} solve my problems by battling. You asked me what I'd do if a Pokémon attacked me. If battling didn't work. Well, here you go."
blue @talkingmouth "Yellow. You're up."

show yellow with dis:
    xpos 0.5 xzoom -1

yellow @talkingmouth "Azoth? We don't want to hurt you. We're not trying to take anything from you. We're just trying to--"

stop music

show yellow surprisedbrow frownmouth with dis:
    xpos 0.5
    pause 0.3
    ease 0.2 ypos 1.5 rotate 90

show fulldeoxys:
    xpos 0.75
    ease 0.1 xpos 0.6
    pause 0.2
    ease 0.5 xpos 0.75

show blue desperateeyes with dis

pause 0.1

$ PlaySound("body roll.ogg")

pause 0.9

yellow sad "O-ow..."

pause 1.0

red @surprised "Y-Yellow...?"

narrator "You quickly rush to Yellow's side. She's gasping for breath from the impact of the creature's blow, but..."

red @talking2mouth "Blue, she's still alive. Blue--"

blue shadow @furiousmouth "I'll destroy you."

play music "audio/music/bigbluebattle_start.ogg" noloop
queue music "audio/music/bigbluebattle_loop.ogg"

pause 1.0

blue @closedbrow wistfulmouth "You want to know what I'm sick of, Azoth? I'm sick of your goddamn railroad of Diabolus ex Machina."
blue @angry "First a super-powerful rare Pokemon fell out of the sky, and instantly latched onto my biggest rival."
blue @glanceeyes talking2mouth "Then my rival's common rat ate a bunch of meteorite shards, and his Pokémon got a massive power boost."
blue @angry "And now {i}you{/i} fall out of the sky, get a Hypno to attack Yellow, and then hit her yourself."

pause 1.0

blue @closedbrow furiousmouth "You're going to pay."
blue @desperateeyes furiousmouth "Everyone has something. Some power, some gift, some {i}friend{/i} that gives them an advantage over me."
blue @angry "Look at where I'm standing! [first_name] has his Pikachu and Frienergy! Yellow can heal Pokémon! Nate's some kind of government spook!"
blue @angry "Even your {i}other{/i} victims... two of them are Espers, and one's a goddamn dragon. I am {i}surrounded{/i} by the most powerful beings on the planet, and I'm just a man!"
blue @closedbrow furiousmouth "And {i}every{/i} time I think I've finally caught up, something falls out of space and gets in my way!"
blue @furiousmouth "Well, you know what? I wasn't born with power! Everything I have, everything I've {i}ever{/i} had, I earned and {i}took!{/i} So, guess what, space freak? I'm going to take {i}your{/i} power, too!"

show blue:
    xpos 0.25
    linear 0.2 xpos 1.2

show fulldeoxys:
    xpos 0.75
    linear 0.4 xpos 1.5

scene blank2 with splitfadefast

blue scaredeyes happymouth "{b}Die!{/b}"

narrator "Blue charges right at the creature. It, apparently not expecting this, stares at Blue with a sort of silent bewilderment on its emotionless face."

pause 1.0

narrator "Which {i}promptly{/i} meets Blue's fist."

$ PlaySound("pokemon/cries/386.mp3")
$ PlaySound("shatter.ogg")

blue shadow scaredeyes happyeyebrows happymouth "Yeah! How'd you like that?"

pause 1.0

nate @talking2mouth "Oh my god. He's actually going to die."

stop music fadeout 1.0

pause 1.0

show screen songsplash("Sinis Trio", "Zame")
queue music "audio/music/natetheme_start.ogg" noloop
queue music "audio/music/natetheme_loop.ogg"

nate @closedbrow talking2mouth "Alright. Going to have to operate outside of the parameters I was assigned. Sir's really going to thrash me for this one..."

call clearscreens() from _call_clearscreens_167

pause 1.0

show natepullsthetriggerbg with Dissolve(2.0)

nate @talking2mouth "AZOTH1. You have assaulted a human being. If you are capable of understanding the severity of that crime, you will stand trial."

show natepullsthetriggernate with Dissolve(2.0)

nate @talking2mouth "If you are {i}not{/i} capable of understanding the severity of that crime, you will be restrained, retrained, and released once it is determined you are no longer a threat."
nate @talking2mouth "You are instructed to stop fighting immediately, or I will use reasonable force to end this battle."

blue @angrybrow angrymouth "If you've got something that can end this, then do it, {i}now!{/i}"

nate @talking2mouth "AZOTH1, under the authority of the International Police's Extraplanetary Affairs Bureau, I place you under arrest."

red @surprised "What?!"

$ hideside = True

pause 1.0

$ PlaySound("pokemon/ball sound.ogg")

nate @talkingmouth "PW05. Initiate the Fermi's Answer Protocol."

$ PlaySound("pokemon/cries/649.mp3")

show natepullsthetriggergenesect behind natepullsthetriggernate with Dissolve(3.0):
    xpos 1.0
    ease 2.0 xpos 0.0

red @surprised "What... what is {i}that?!{/i}"

nate @talkingmouth "My mission."

show natepullsthetrigger with dis

pause 0.5

nate @talkingmouth "PW05. {i}Fire.{/i}"

call clearscreens() from _call_clearscreens_168
scene blank with spinfaderapid

$ PlaySound("thunder.ogg")

$ hideside = False

pause 3.0

narrator "There's a tremendous crashing explosion sound, and your head rings as a huge wave of energy blasts past you."

pause 0.5

narrator "...But you seem to be okay?"

scene forest3 
show screen currentdate
show deoxysblackeyes:
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
show blue surprisedbrow frownmouth:
    xpos 0.5 xzoom -1
show yellow surprisedbrow frownmouth:
    xpos 0.66
show nate:
    xpos 0.85 xzoom -1
with splitfadefast

pause 2.0

blue @talkingmouth "...What?"

nate @talkingmouth "I've neutralized it using a powerful Techno Blast. It's no longer a threat."

pause 1.0

show blue:
    xzoom -1
    ease 0.5 xzoom -1

blue @surprisedbrow talkingmouth "...No, again, {i}what?{/i}"

nate @sadbrow talkingmouth "...Again, I'm not sure what you're asking?"

narrator "Blue looks at his hand, and quickly folds his arms in front of him, sticking his chin out defiantly."

show yellow -surprisedbrow with dis

blue @closedbrow talkingmouth "Tell us {i}everything{/i}. Now. No more bullshit, half-truths, lies of omission. {i}Everything.{/i}"

nate @sadbrow talkingmouth "...I'll tell you everything I {i}know.{/i}"

pause 1.0

nate @talking2mouth sadbrow "Easy stuff first, I guess."

$ AddEvent("Nate", "Blake")

nate @sadbrow happymouth "Call me Blake. My handler calls me Black No. 2, but that sounds like something you'd drop off in the toilet after drinking a lot of coffee, so I prefer Blake."

blue @surprised "What?! Your name isn't even Nate?"

nate @closedbrow talking2mouth "Nope. It's Blake. Blake Hall, Jr."

pause 0.5

nate @talking2mouth "Not ringing a bell?"

red @talkingmouth "Blake Hall? Wasn't he a country singer?"

nate @sadbrow talkingmouth "Not exactly."

pause 1.0

nate @closedbrow talkingmouth "I guess that's not important."
nate @talkingmouth "What {i}is{/i} important is that I'm a member of the International Police. An agent, actually. I'm part of a task force that deals with extra-planetary entities."

blue @closedbrow wistfulmouth "Bull."

nate @happy "You know many Pokémon trainers who carry around cannon-wielding robot bugs?"

blue @talkingmouth "Yeah, yeah. Whatever. Just 'cause you have a special Pokémon doesn't mean that you're a cop."

nate @closedbrow talking2mouth "I'm not a cop. I'm an {i}agent.{/i}"

blue @sad2eyes angryeyebrows talkingmouth "Whatever."

#nate @talking2mouth "I'm fake. A fake man. Everything about me--the way I talk, my personality, my appearance, even my name--is fake."
#nate @talking2mouth "It's all a cover."

pause 0.5 

nate @sadbrow talking2mouth "I was sent here by the international police to investigate one of my classmates. But while I was here, that meteor fell."

red @surprised "So that meteor...!"

nate @talking2mouth "Yeah. But it wasn't {i}just{/i} a meteor. It was actually a protective shell for an alien invader."

show hall_B at sepia:
    zoom 0.8
show flashback
with dis

$ renpy.pause(1.0, hard=True)

show skyla angrybrow happymouth at sepia behind flashback with dis

skyla @talkingmouth "I {i}knew{/i} it!"

show blank with splitfade

hide skyla
hide hall_B
hide flashback
hide blank 
with dis

pause 1.0

redmind @thinking "Well, one point for Skyla."

nate @closedbrow talking2mouth "So, as I mentioned, this creature is codenamed AZOTH1 by Interpol's EAB. We first discovered it when our scanners picked up a meteor headed toward Kobukan."
nate @talkingmouth "The Latias you call Tia was sent to intercept it. Her family back home were the first people to recalculate the meteor's rebound location."

yellow @surprised "Rebound location?"

nate @talking2mouth "This meteor fell once before. In Hoenn. It was going to wipe out the region, cause untold death and destruction."
nate @closedbrow talkingmouth "But... somehow... it was {i}deflected.{/i} Almost as though it hit a giant trampoline."

nate @talkingmouth "All the governments of the world had their eyes on it, of course, so when the impact hour came and went, there was a mad scramble to find it. The astronomers of Alto Mare were the first to locate it."

pause 0.5

red @surprised "So... Tia wasn't {i}in{/i} the meteor! And it didn't hit her! Instead, she was trying to destroy it!"

nate @talking2mouth "But it broke apart before it ever hit the ground."

pause 0.5

nate @talking2mouth "I'm sure you can guess what {i}was{/i} inside, then. I'm not quite sure what it is, though."

show nate surprisedbrow frownmouth with dis

yellow @talkingmouth "This... this {i}is{/i} a Pokémon. I can tell."

pause 1.0

nate @talkingmouth "Noted."
nate -surprisedbrow @happy "Or should I say 'Nated'?"

blue @angry "You {i}shouldn't.{/i}"

nate @closedbrow talking2mouth "Tough crowd."

blue @talkingmouth "So. This... this {i}Pokémon.{/i} That's what Gramps has been poking and prodding at for the past three weeks?"

nate @talkingmouth "Fragments of its protective shell, yeah. Its true power is much greater than even he could predict, though."

yellow @closedbrow talkingmouth "So... {i}this{/i} is what made the Foreverals."

narrator "Blue looks at his hand again."

nate @talkingmouth "That's right. Really powerful Pokémon sometimes generate an aura of mysteriosity, too. If it's been in the forest for weeks, undisturbed, I can imagine that it probably caused this Mystery Dungeon, too."

yellow @surprisedbrow sadmouth "But--it's been here, undisturbed, for weeks, like you said! Is it really a threat?"

nate @sadbrow talkingmouth "...I couldn't tell you that. But my orders are to bring it in for study. And the fact that it first appeared in a meteor that could cause an extinction-level event isn't a good look for it."
nate @closedbrow talking2mouth "Not to mention that it punched you in the stomach..."

yellow @sadbrow talkingmouth "I don't get it. When I held the Foreverals, I felt... a friendly power. Like it wanted to give me what I wanted. If it's such a threat, why did they feel friendly?"

nate @sadbrow talking2mouth "I don't know. I'm sorry."

show nate:
    ease 0.5 xpos 0.3 xzoom 1

show blue:
    xpos 0.6
    ease 0.5 xpos 0.75

show yellow:
    xpos 0.75 
    ease 0.5 xpos 0.5

yellow @talkingmouth "Can I--"

nate @sadbrow talkingmouth "'Fraid not. It seems to be able to assimilate genetic material into itself, and copy their abilities. We don't want to give it the ability to heal itself any time, you know? It might wake up now."

yellow @sadbrow talkingmouth "Oh."

blue -surprisedbrow @talkingmouth "...So this thing is what caused all of this."

pause 0.5

nate @talkingmouth "{w=0.5}.{w=0.5}.{w=0.5}.One second."

show nate:
    xpos 0.3
    ease 0.5 xzoom -1

pause 0.5

nate @talking2mouth "Sir, these readings... extraterrestrial, definitely, but not extradimensional. This doesn't appear to be involved with the UB project."

pause 0.5

nate @talking2mouth "No, Sir. I {i}chose{/i} to disregard orders. The risk of--"

pause 0.5

nate @talking2mouth "Yes, Sir. Standard Lethe protocol. I understand. I will turn myself over to your authority as soon as I have contained AZOTH1."

pause 0.5

nate sadbrow sadmouth "{w=0.5}.{w=0.5}.{w=0.5}."

narrator "Nate crushes something in his hand."

pause 0.5

nate @talking2mouth "Bye, Sir."

pause 1.0

show nate:
    xzoom -1 xpos 0.3
    ease 0.5 xzoom 1

pause 1.0

blue @sad2eyes wistfulmouth "...When we were roommates, you actually listened to what I was saying."

nate -sadbrow -sadmouth @sadbrow talkingmouth "My problems are arresting international criminals and securing dangerous and unknown Pokémon from space."
nate @sadbrow happymouth "It was nice to listen to problems of your scale for once."

pause 0.5

blue @sad2eyes wistfulmouth "I shouldn't have kicked you out of the dorm."

nate @happy "Hey, it's alright. Now that my mission's complete, it's probably better that you cut the ties before I have to wipe your memory, anyway."

$ PlaySound("idea.ogg")

stop music fadeout 1.5
queue music "audio/music/DontEverForget_start.ogg" noloop
queue music "audio/music/DontEverForget_loop.ogg"

pause 1.0

red @confused "What?"

nate @sadbrow talkingmouth "C'mon, you didn't really think that I was going to reveal all this stuff and let you walk away with it, did you?"

blue @closedbrow wistfulmouth "Wipe our memories, huh?"

red @sadbrow happymouth "Can I opt out?"

nate @sadbrow happymouth "'Fraid not."

$ sidemonnum = 649

$ PlaySound("pokemon/cries/649.mp3")

sidemon @talkingmouth "Ge. Ne. Se. Ct."

nate @closedbrow talking2mouth "Down."

pause 0.5

nate @talking2mouth "Hey, sometimes, when I do this, people want to, like, get something off their chest, before everything gets wiped."

pause 0.5

nate @happy "You got any confessions to make?"

pause 0.5

yellow @closedbrow talkingmouth "{size=30}I'm your fool.{/size}"

blue @surprised "Huh?"

show yellow:
    xpos 0.5 xzoom 1
    ease 0.5 xzoom -1

yellow @talkingmouth "Blue. I've been a fool."

blue sadbrow frownmouth @sad "Wait. What do you...?"

yellow @tears surprisedmouth cryingeyes "I've been trying so hard, Blue. I've been trying {i}so{/i} hard to get you to show that you're a better person. And it's exhausting. Every inch of progress is something I have to fight for, for ages."

yellow @unamusedeyes unamusedeyebrows talkingmouth "And I hate fighting."

yellow @surprisedmouth cryingeyes tears "I need... I {i}need{/i} you to try harder. I know there's good in you. I've seen it. You saved me today, just like you did back then."

yellow @angrybrow talkingmouth "But my friendship is {i}not{/i} unconditional. If you don't try harder... I'm giving up. I... I can't be the only one who sees the best of you anymore."

pause 0.5

yellow @sad "...I'm sorry. That's just something I know I could never say if you'd actually remember it."

blue @sad2eyes sadeyebrows talkingmouth "I... get it."

pause 1.0

show yellow surprisedbrow frownmouth tears with dis

blue @closedbrow talkingmouth "I'm sorry. I'm sorry to you, Yellow, and to you, [first_name]. Neither of you deserve me."

menu:
    "[bluecolor][[Blue Rank 1]{/color} I'm sorry, too." if (GetRelationshipRank("Blue") > 0):
        $ AddEvent("Blue", "Apologized")
        red @sad2eyes talking2mouth "I should have tried harder to reach out when we were kids. Yeah, I was a kid, but... I enjoyed your grandpa's attention. Maybe a bit too much. I'm sorry."

        $ ValueChange("Blue", 1, 0.75)

    "[ellipses]":
        pass

pause 1.0

blue @kindeyes wistfulmouth "...I asked to dorm with you, [first_name]. Leaf and Ethan, too. And you, of course, Yellow."

pause 0.5

blue @sad2eyes wistfulmouth sadeyebrows "That's why Falkner... that's why."

blue @closedbrow talking2mouth "He said... no way. So I nagged him. Over and over and over. I thought... if we were forced to live together..."

blue @sad2eyes wistfulmouth sadeyebrows "...then maybe."

pause 2.0

nate @talking2mouth "It's time. You'll wake up on campus, with no memory of this morning's events." 
nate @talking2mouth "You'll remember going into the forest, finding your friend, and leaving, but nothing about AZOTH1 or me."

blue @closedbrow sadmouth "Good. Let's get all this sappy shit out of our heads."
blue @surprisedbrow talkingmouth "How do we do this? You got a pen we look at?"

nate @talkingmouth "Something like that. Go, BEM651."

$ sidemonnum = 606
$ PlaySound("pokemon/ball sound.ogg")
$ PlaySound("pokemon/cries/606.mp3")

sidemon @talkingmouth "Beeeeheeeyem!"

red @talkingmouth "Beheeyem. Three foot three. Native to Unova. Evolved at level 42. Psychic-type."
red @talking2mouth "...And well-known for being able to hypnotize people to erase and rewrite their memories."

blue @sad2eyes talkingmouth "There goes the human Pokédex."

red @sweat closedbrow talking2mouth "I've been kinda off my game with all these new, never-before-seen Pokémon. I'm just reminding myself that I'm {i}really{/i} good when it comes to common Pokémon."

nate @talkingmouth "Mind sending out your Pokémon? I normally don't bother, but since Yellow can talk to Pokémon, I've gotta think about that, too."

yellow closedeyes -tears @angryeyebrows talkingmouth "I {i}can't{/i} talk to Pokémon."

nate @happy "My bad."

pause 2.0

nate @sadbrow talking2mouth "Hasta la vista, guys. I hope the next time I see you, they give me a friendlier personality."

call clearscreens() from _call_clearscreens_169
show blank2 with transeye

pause 1.0

$ technicaldungeon = False

narrator "You close your eyes."

$ PlaySound("shine.ogg")

nate @talkingmouth "Alright, now teleport them back to campus."

if (not rescuedsabrina and not rescuedwill):
    nate "The Espers, too. Send them to the infirmary."

elif (not rescuedsabrina):
    nate "Sabrina, too. Send her to the infirmary."

elif (not rescuedsabrina and not rescuedwill):
    nate "Will, too. Send him to the infirmary."

if (not rescuedtia):
    nate "But leave Tia here. It might be awkward for her if I were to teleport her back without her illusion."

$ PlaySound("Whoosh.ogg")

pause 1.0

narrator "You wait for a numbness, or a blindness, or a lack of {i}something{/i}."

pause 0.5

narrator "But, oddly enough, you don't feel anything."

pause 0.5

redmind @thinking "Okay... I still remember going into the forest. Rescuing Yellow. Blue's apology."
redmind @confusedeyebrows closedeyes frownmouth "If Nate--Blake--didn't wipe {i}that{/i}, what did he wipe?"

show screen songsplash("Viridian Forest", "Zame")
stop music fadeout 1.5
queue music "audio/music/viridianforestgentle_start.ogg" noloop
queue music "audio/music/viridianforestgentle_loop.ogg"

scene relichall_A 
show screen currentdate
show blue closedbrow frownmouth:
    xpos 0.33
show yellow closedeyes:
    xpos 0.66
with transeye2

pause 1.0

blue -closedbrow -frownmouth @sad2eyes wistfuleyebrows wistfulmouth "...Huh?"

pause 0.5

yellow @surprisedmouth "{size=40}Yaaaaawwwwnnnn.{/size}"
yellow -closedbrow @surprisedbrow talkingmouth "Hm? What were we talking about?"

pause 0.5

blue @closedbrow talkingmouth "We were... we were going to train, right?"

show blue scaredeyes surprisedeyebrows frownmouth with dis

yellow @closedeyes talkingmouth "I thought... we were going on a picnic?"

blue -scaredeyes -frownmouth @closedbrow talking2mouth "Well... yeah, obviously! C'mon, let's go."

yellow @happy "Okay. Bye, [first_name]!"

red @confused "Bye...?"

hide blue
hide yellow
with dis

pause 1.0

redmind @frownmouth "That was... bizarre. I {i}swear{/i} I still remember everything, right?"

red @talkingmouth "...Buddy? Do you remember what just happened?"

$ PlaySound("Pokemon/pikachu_confused.ogg")

libpikachu @confusedeyes surprised2mouth "Pi?"

red @talking2mouth "I guess you don't, huh?"

narrator "You spend a while wracking your brains, trying to remember what you forgot. {w=1.0}No such luck."

pause 1.0

red @talkingmouth "Well... I can't think of anything else to do, so..."

show phone_B 
show leaf surprisedbrow frownmouth
show phone_A
with fadeinbottom

leaf @talking2mouth "[first_name]? What are you doing? Are you back at school already?"

red @talkingmouth "Yeah. We, uh, we found Yellow."

if (not rescuedtia):
    red @talkingmouth "And Tia's fine, too. She's at the infirmary."

    leaf @surprised "What?! Oh, geez, Whitney is {i}not{/i} going to be happy we were hiking through the forest for four hours for nothing."

    whitney @angry2eyes angryeyebrows anger2 angrymouth "We were {i}what?!{/i}"

    leaf -surprisedbrow -frownmouth -surprised @happy "Gotta take this, sorry! See you at the infirmary, then...?"

else:
    leaf @surprised "What?! Oh, geez, Ethan is {i}not{/i} going to be happy he was hiking through the forest for four hours for nothing."

    ethan @angry2eyes angryeyebrows anger2 angrymouth "We were {i}what?!{/i}"

    leaf -surprisedbrow -frownmouth -surprised @happy "Gotta take this, sorry! See you back at the dorm, then...?"

red @talking2mouth "Yeah, see you there."

hide phone_B
hide phone_A
hide leaf
with fadeoutbottom

if (rescuedsabrina):
    pause 0.5

    red @surprised "Oh, that reminds me! I should probably... let's see..."

    redmind @thinking "Sabrina?"

    pause 2.0

    redmind @closedeyes frownmouth "[sabrinacolor][first_name]?{/color}"

    redmind @happy "Hey! I found Yellow."

    if (not rescuedwill):
        redmind @happy "{i}And{/i} Instructor Will!"

        redmind @surprisedbrow frownmouth "[sabrinacolor]R-really?! You found Instructor Will? Thank goodness!{/color}" 

        redmind @happy "Wow. You were really happy about that."

        redmind @surprisedbrow frownmouth "[sabrinacolor]Yes. Yes, I am. He means... so much to me. I was really worried about him.{/color}" 

        pause 1.0

        redmind @sadbrow frownmouth "[sabrinacolor]If he didn't come back, I'd be {i}truly{/i} alone.{/color}"

        if (GetRelationshipRank("Sabrina") >= 1 or GetRelationship("Sabrina") == "...?"):
            redmind @happy "Hey, you'd still have me!"

    redmind @thinking "[sabrinacolor]And... you know about... Blake?{/color}"

    redmind @closedeyes frownmouth "I guess so. But I don't think I should. Did you have anything to do with that?"

    redmind @thinking "[sabrinacolor]No. Nothing at all. I try to stay as far away from Blake as possible. It's dangerous for me to be around him.{/color}"

    redmind @thinking "Yeah, I can understand that."

    if (not rescuedwill):
        redmind @happy "Anyway, since I found Yellow and Instructor Will, you can come back."
    else:
        redmind @happy "Anyway, since I found Yellow, you can come back."

    redmind "[sabrinacolor]Yes. We'll be coming back shortly.{/color}"

pause 0.5

red @closedbrow talking2mouth "Well... now what? Looks like I've got some time to kill..."

python:
    removestudents = {"Leaf", "Ethan", "Blue", "Yellow", "Cheren", "Skyla", "Silver", "Nate"}
    if (not rescuedtia):
        removestudents.update({"Tia", "Whitney", "Flannery"})
    if (not rescuedsabrina):
        removestudents.update({"Sabrina", "Nessa", "Rosa", "Raihan", "Sonia"})

call clearscreens() from _call_clearscreens_170
scene blank2 
with Dissolve(1.0)

show evening at vspaz
$ timeOfDay = "Evening"

pause 3.0

call freeroam from _call_freeroam_22

stop music fadeout 1.5
queue music "audio/music/Eterna_Start.ogg" noloop
queue music "audio/music/Eterna_Loop.ogg"

$ removestudents = set()

if (not rescuedtia):
    narrator "Enough time passes, and you meet up with Leaf at the infirmary."

    if (persondex["Nurse Miriam"]["Named"]):
        narrator "However, Nurse Miriam insists that the people inside need their rest, and their privacy."

    else:
        narrator "However, the Nurse insists that the people inside need their rest, and their privacy."

    narrator "Apparently, Instructor Will is already fretting over Tia and Sabrina something fierce."

    leaf @talking2mouth "...Welp. That's that, I guess."
    leaf @talking2mouth closedbrow "Man, this was a really busy day of doing nothing, huh?"

    red @confused "...Yeah."

    redmind @thinking "...'Nothing'. 'Nothing' at all."

else:
    narrator "Enough time passes, and you're unsure what there is left to do."

if (rescuedsabrina and rescuedwill and rescuedtia):
    $ AddEvent("Instructor Will", "Scholarship")

    narrator "Bereft of other ideas, you decide to head back to your dorm, when an announcement over the loudspeaker cuts through the mild fog of confusion you've been stumbling through."

    will "Hohoho! The Great Will requests the presence of Sabrina Natsume, Bianca Vongole, and [first_name] [last_name] in the Psychic Elective classroom!"

    redmind @confusedeyebrows frownmouth "At this time of the evening?"

    will "Yes, at this time of the evening! Chop chop, now!"

    redmind @confusedeyebrows frownmouth "...Okay."

    scene blank2 with splitfade

    pause 1.0

    show classroom
    show psychtype:
        xalign 0.5 yalign 1.0
    show sabrina casualoldhair:
        xpos 0.75
    show will:
        xpos 0.5
    if (rescuedtia):
        show tia hat:
            xpos 0.25
    else:
        show tia:
            xpos 0.25
    with splitfade

    will @happy "Ah, the man of the hour!"

    red @confused "I'm... sorry, I'm not quite sure what the occasion is?"

    will @happy "Ah, modest to a fault!"

    red @talkingmouth "No, I'm just genuinely lost here."

    will @talkingmouth "Pish and tosh. You rescued all three of us this week, young [first_name] [last_name], and that's not a favor we Espers shall soon forget!"

    show sabrina sad2eyes with dis 

    will @talkingmouth "Now, Sabrina has told me that you are having a few... ah, 'monetary concerns' in regard to Kobukan."

    sabrina @sadbrow talking2mouth "I'm... sorry. He asked if I knew of any problems he could help with..."

    menu:
        "That was private.":
            $ ValueChange("Sabrina", -1, 0.75)

            sabrina @shadow angry "I {i}said{/i} I was sorry."

        "It's cool.":
            $ ValueChange("Sabrina", 1, 0.75)

        "Whatever.":
            pass

    show sabrina -sad2eyes with dis

    will @talkingmouth "In any case, for your help in rescuing us, I wanted to make you aware of an opportunity. There's a certain scholarship that I have the honor of being able to hand out every year." 
    will @happy "[bluecolor]'The Mind Scholarship for Promising Psychic Students!'{/color}"

    red @surprised "Hm?"

    will @happy "Typically, it's given to Espers. Indeed, I fully intended to give it to dear Bri here. But we talked it over, and it seems that you may need it a good amount more than her."

    red @surprised "Wait... Instructor Will, are you saying...?"

    if (HasEvent("Instructor Will", 2.1)):
        will @happy "Oh, you're one of my best students. It only makes sense that I give it to you! You might be a Euthymic, but you're certainly a skilled Psychic-type trainer."

    elif ((GetRelationshipRank("Sabrina") >= 1 or GetRelationship("Sabrina") == "...?") and GetRelationshipRank("Tia") >= 1):
        will @happy "You may not be a frequent student of mine, but Sabrina and Tia have spoken highly of you, you saved us from that awful, smelly, rotting forest, and that's enough for me!"

    elif (GetRelationshipRank("Sabrina") >= 1 or GetRelationship("Sabrina") == "...?"):
        will @happy "You may not be a frequent student of mine, but Sabrina has spoken highly of you, you saved us from that awful, smelly, rotting forest, and that's enough for me!"

    elif (GetRelationshipRank("Tia") >= 1):
        will @happy "You may not be a frequent student of mine, but Tia has spoken highly of you, you saved us from that awful, smelly, rotting forest, and that's enough for me!"

    else:
        will @happy "You may not be a frequent student of mine, but you saved us from that awful, smelly, rotting forest, and that's enough for me!"

    $ PlaySound("Get.ogg")
    $ DisplayGetItem("mindscholarship")
    $ scholarshipslist.append("Mind Scholarship for Promising Psychic Students")

    narrator "[bluecolor]You earned the Mind Scholarship for Promising Psychic Students!{/color}"

    pause 2.0

    red @happy "Oh my God. Thank you, Professor. Thank you, {i}so{/i} much. That means a tremendous amount to me. You--"

    will @happy "Yes, that will pay a whole eighth of your tuition!"

    red @unamusedeyebrows playfuleyes unamusedmouth "What."

    will @surprised "Oh? What's that face about? You didn't think the scholarship would pay your {i}entire{/i} tuition, did you?"

    red @sad2eyes angryeyebrows talking2mouth "I... entertained the thought."

    will @happy "Hahaha! No, I'm afraid the adventure's not over quite yet."

    red @closedbrow talking2mouth "Okay. Well, still, that's {i}really{/i} helpful. Thank you, Instructor Will."

    show sabrina lightblush with dis

    will @talkingmouth "Of course. Now, I believe Sabrina wanted to say something? Didn't you, Bri?"

    pause 1.0

    if (HasEvent("Sabrina", "Apologized")):
        sabrina @talking2mouth "I... I {i}did{/i} say this before. I apologized. But now you have even saved me. And my... I mean... Instructor Will."

        sabrina @talking2mouth "I want to say thank you. Again."

        red @sadbrow talkingmouth "It was nothing. Really. ...Again."

    else:
        $ AddEvent("Sabrina", "Apologized")

        sabrina @talking2mouth "I... you saved me. And the Instructor. And I think... maybe... I was a bit harsh before. When I told you to 'stay away.'"

        if (GetRelationshipRank("Sabrina") >= 1 or GetRelationship("Sabrina") == "...?"):
            sabrina @sadmouth "And then when I yelled at you for rescuing me. Yelled, instead of thanking you. That was... wrong of me."

        red @sadeyebrows sadeyes talkingmouth "High-stress situation. I get it."

        pause 1.0

        sabrina -sad2eyes @talking2mouth "I want to say... 'thank you.' Properly."

        show sabrina blush happyeyebrows happyeyes with dis

        sabrina @talking2mouth "So. Th-thank..."

        pause 1.0

        show sabrina heavyblush sadeyebrows sad2eyes poutmouth poutface with dis

        sabrina "Mmmmrmph."

        will @happy "Come now, Bri! There's nothing embarrassing about this."

        pause 1.0

        show sabrina lightblush sadeyebrows happy2eyes -poutmouth -poutface smilemouth with dis

        sabrina @happymouth "Thank you."

        call clearscreens() from _call_clearscreens_171
        show sabrinatakesabreath with Dissolve(2.0)

        pause 6.0

        sabrina @talking2mouth "{i}Thank you, [first_name].{/i}"

call clearscreens() from _call_clearscreens_172
scene blank2 with splitfade

pause 3.0

show night at vspaz
$ timeOfDay = "Night"

pause 3.0

show bedroommidnight

$ showredonly = True

blue @talkingmouth "...Alright, I give up."

pause 1.0

red swimsuithatless tired @sadeyebrows talking2mouth "That doesn't seem like you."

blue @talkingmouth "Can it. You know what I'm talking about."

ethan @talkingmouth "Well, I don't. Share with the class?"

leaf @talking2mouth "Yeah, what's happening?"

blue @talkingmouth "This was a {b}private{/b} conversation!"

leaf @talking2mouth "It's not private when you're yelling through the walls, honey."

yellow @talkingmouth "Um... I'm pretty tired from today, so do you mind if we...?"

ethan @talkingmouth "I spent all morning getting dragged around by Leaf, and then it turns out the person we were looking for was back at school. I've got so much adrenaline that was just {i}wasted.{/i}"

if (not rescuedtia):
    ethan "Like, I'm glad you and Tio are alright, but I'm not going to bed until, like, tomorrow."

else:
    ethan "Like, I'm glad you're alright, but I'm not going to bed until, like, tomorrow."

yellow @talkingmouth "It already {i}is{/i} tomorrow, though."

blue @talkingmouth "Would {i}everyone{/i} just shut up?! I'm trying to talk to [first_name]!"

pause 2.0

yellow @talkingmouth "Blue, did you just tell me to shut up?"

blue @talkingmouth "{size=-3}U-u-uh... no.{/size} {size=-6}I mean, not you, specifically.{/size} {size=-9}It was more of a general-purpose{/size} {size=-12}'stop talking...'{/size} {size=-15}not directed at anyone in particular...?{/size}"

pause 2.0

$ showredonly = False

narrator "You keep your ears open, but Blue's voice trails off, and the conversation seems to end for the night."

jump day010516