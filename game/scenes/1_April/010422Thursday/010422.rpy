label day010422:

$ playerparty.remove(pikachuobj)
$ timeOfDay = "Morning"
call calendar(1) from _call_calendar_17
$ calDate = calDate.replace(day=22, month=4, year=2004)

show morning at vspaz

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)
show oakbg
show homeroom behind oakbg

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade    
hide morning

$ renpy.pause(0.6, hard=True)

oak @talkingmouth "And that's the end of the lecture! If you have any questions, feel free to drop into the Research Lab during my office hours!"

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.0)

hide oakbg with dis

pause 1.0

show oak with dis

oak @talkingmouth "Yes, lad?"

red uniform @closedbrow talking2mouth "I just wanted to let you know, Sam, I handled that crisis you caused."

oak surprisedbrow frownmouth @surprised "I beg your pardon?"

red @talkingmouth "You know. When you told Cheren to...?"

oak @talkingmouth "Oh! Oh, yes, you did seem to indicate that you thought that might be some sort of problem."

oak -surprisedbrow -frownmouth -surprised @closedbrow talkingmouth "Well, I'm glad you've satisfied your concerns on the matter."

red @talking2mouth "Right. And you won't tell anyone else about...{w=0.5} {i}anything{/i} about me, right?"

oak @talkingmouth "Hm... not sure I can restrain myself, lad. I'm quite proud of you, you know. A Battle Team Member? A frontrunner in the student council election? An excellent student?"
oak @happy "How could I stop myself from talking about you?"

red @sadbrow happymouth "...Thanks, Sam. I just mean, don't tell anyone about... you know. Our private stuff."

oak @closedbrow talkingmouth "Mmm. Don't worry about that, lad. I'll be discrete."

hide oak with dis

pause 1.0

show blue angry uniform with dis:
    xpos -0.5
    ease 1.0 xpos 0.25

blue @talkingmouth "So, you got into the Battle Team too?"

red @confused "Were you listening to our conversation?"

blue @talkingmouth "Ex-{i}cuse{/i} me for not being able to ignore Gramps yelling 'oh, [first_name]'s so great, I love [first_name]' across the classroom."

show leaf uniform with dis:
    xpos 1.5
    ease 1.0 xpos 0.75

leaf @sarcastic "Yeah, I agree with [blue_name] about as often as the clock strikes thirteen, but Professor Oak {i}was{/i} being a bit loud."

leaf @happy "Hey, maybe that's where you got it from, [blue_name]!"

red @talkingmouth "Wait, [blue_name], did you say you got into the Battle Team... 'too?'"

blue -angry @closedbrow talkingmouth "Yeah. {i}Obviously.{/i} I bet that sucks for you, huh? You really thought you were going to be number one."

leaf @surprised "Oh, wow! You actually nagged your way into the team?"

blue angry "It wasn't that! Janine was impressed by how hard I trained! Not like [first_name] here, who just slipped and fell into success!"

pause 1.0

blue -angry surprised @closedbrow talkingmouth "Tch. I don't need to have this argument with a non-Battle Team member like you. You don't exist for me anymore." 

leaf @surprised "Oh.{w=0.5} Oh!{w=0.5} Oh...{w=0.5}"

blue @talkingmouth "What, do you have hiccups or something?"

leaf @closedbrow talkingmouth "Hm... okay, I can't decide what to do."

red @confused "What do you mean?"

show blue sad with dis

leaf @sarcastic "Like, would it be funnier to tell him I got into the Battle Team {i}now{/i}, or just show up at Friday's meeting?"

blue @talkingmouth "W-what?! You too?!"

leaf @happy "Yep! Sorry, cupcake. Guess it's going to be pretty hard to battle someone who doesn't exist, right?"

blue -sad @closedbrow talkingmouth "Well, whatever. At least you actually earned {i}your{/i} spot."

if (wins > 4):
    if (wins == 7):
        red @talkingmouth "I won all of my matches."
    elif (wins == 6):
        red @talkingmouth "I won all but one of my matches."
    elif (wins == 5):
        red @talkingmouth "I won all but two of my matches."

    blue @closedbrow talking2mouth "I repeat. What-ever."

red @confused "Why do you think I didn't earn my spot, [blue_name]?"

blue @angry "Drop that bullshit. The battle rules were blatantly set up to favor you."

red @closedbrow talking2mouth "...They helped Ethan, too."

blue @surprised "Who?{w=0.5}{nw}" 
extend @talkingmouth "...Whatever, I don't care."

blue @talkingmouth "Look, [first_name]. I {i}earned{/i} my spot. In the Battle Team. In this school. And with our friends back home."

red @angry "Seriously?! You're going to bring up high school now?!"

blue @talkingmouth "Yeah. And you're just mad 'cause you know I'm right."

pause 1.0

red @closedbrow talking2mouth "I'm done with you. Don't you have a nerd to give swirlies to?"

show blue angry with dis

pause 1.0

blue @talkingmouth "This isn't going to last forever. I'll be happy as hell when you finally crash and burn."

hide blue with dis

pause 1.0

show leaf:
    ease 0.5 xpos 0.5

leaf @sarcastic "I think he's actually gotten nicer."

show leaf surprisedbrow frownmouth
show homeroom 
with vpunch

red @happy "Leaf!"

leaf @talking2mouth "H-huh?!"

red @happy "You got into the Battle Team?! That's amazing! Good for you--seriously, I'm really happy for you!"

if (GetRelationship("Leaf") == "Bestie"):
    red @happy "Besides, I know how much battling means to you, and how much fun you have doing it. It's a perfect fit for you, bestie."

pause 1.0

leaf blush -surprisedbrow -frownmouth -surprised @sadbrow talkingmouth "...You're a great guy, you know that, [first_name]?"

red @confused "What? For saying 'good job?'"

leaf @sarcastic "Yeah, obviously I'm referring to that, and only that."

red @talking2mouth "How come you didn't tell me Tuesday, though?"

leaf -blush @surprised "Huh? I didn't find out until last night."

red @closedbrow talking2mouth "Oh, yeah... I guess maybe the invites went out in waves, then. It probably took Janine a while to box up all the rewards."

leaf @talkingmouth "Oh, I'm sure she has Battle Team minions for that."

red @happy "What do you think the Battle Team meeting will be about?"

leaf @closedbrow talking2mouth "Going to go out on a limb here and say we're probably going to battle."

red @surprised "Damn. The one thing I wasn't prepared for."

leaf blush @flirt "Well, shoot. Guess [blue_name] was right, and you're going to flunk out horribly."

red @closedbrow talking2mouth "It really do be like that."

leaf -blush @closedbrow talking2mouth "On a serious note, though, I hope they're going to tell us more about how the Quarter Qlashes work. And I want to know what part Janine's playing in this."
leaf @closedbrow talkingmouth "She's pretty badass, but I don't think she has any influence over how people in the QQs are matched up. She probably wants to avoid knocking out any of her own team, you know, but it's kinda unavoidable."

red @closedbrow talking2mouth "Right. I've got a few questions I want to ask about tournaments, personally."

leaf @surprised "Oh, I didn't even think about that! Good point."
leaf @happy "It'd be {i}so cool{/i} if we got to see how people from other regions battle."

red @confused "Wait, is there a difference?"

leaf @closedbrow talkingmouth "Are you serious?"

red @happy "Yep. 'Scuse my shelteredness."

leaf @happy "Yeah, there's tons of differences! People from Orre pretty much only do double battles. Unovan trainers love their Triple Battles." 
leaf @happy "And there's a new battle type from Paldea that's {i}really{/i} catching on called Squad Battles, that have entire teams of trainers facing each other! I heard the Academy is going to really push those this year."

red @sadbrow talkingmouth ".{w=0.5}.{w=0.5}.{w=0.5}Didn't know that."

pause 1.0

leaf @sadbrow happymouth "Hey. It's alright. That's what we're here to learn, right?"

red @happy "Right. It's kinda fun to think about what Janine might be about to teach us, isn't it?"

leaf @happy "Totally! I bet she knows all kinds of battling tricks that we can't even begin to imagine."
leaf @closedbrow talkingmouth "...Like how her Venomoth had five moves. I didn't imagine that, right?"

red @surprised "You noticed, too? Yeah, that was the weirdest thing!"

jump homeroom1transition