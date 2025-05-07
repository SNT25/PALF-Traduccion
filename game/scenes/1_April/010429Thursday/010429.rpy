label day010429:

$ playerparty.remove(pikachuobj)
$ timeOfDay = "Morning"
call calendar(1) from _call_calendar_24
$ calDate = calDate.replace(day=29, month=4, year=2004)

show morning at vspaz

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)
show oakbg
show homeroom behind oakbg

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade    
hide morning

$ renpy.pause(0.6, hard=True)

oak @talkingmouth "And that's about the end of the lesson, students! Two things to remember. The first is that there will be a quiz in the homeroom at the end of the day. Don't forget that!" 
oak @talkingmouth "The second thing is--have you all seen those posters around the school encouraging you to vote in the new student council elections?"

show whitney uniform at leftside with dis

whitney @talking2mouth "Oh, totally! I'm pretty sure that if I vote for Jasmine, she'll open up some kind of accessibility office, and I can get paid for doing what I'm already doing!"

show hilbert uniform at rightside with dis

hilbert @closedbrow talkingmouth "Grusha's international battle tournament can only serve to increase the reputation of this school."

show dawn uniform with dis

dawn sadbrow @talkingmouth "U-u-um... I think it'd be fair if the other clubs got as many resources as the Battle Team, so... I like Cheren..."

pause 0.5

dawn surprisedbrow frownmouth @surprised "W-w-wait! I meant Calem! Not Cheren. Sorry, I always get their names confused. I meant Calem!"

hide dawn with vpunch

pause 0.5

show leaf uniform with dis

leaf @flirttalk "Sure, sure, but we're {i}all{/i} voting for [first_name], right?"

oak @talkingmouth "Well, I should certainly hope so!"

red uniform @happy "Heh. Professor, I'm not sure you should be saying that, but I appreciate the support."

menu:
    "{color=#e226a6}[[Charm]{/color} >Ask for the class' support":
        red @talkingmouth "Since the issue's been raised, I'd like to ask for everyone else's support in the election on Saturday."
        
        $ TraitChange("Charm")
        
        red @angrybrow talking2mouth "You can just look at our posters to see what voting for me will get you."

    "{color=#b7669e}[[Patience]{/color} >Talk up the other hopefuls":
        red @talkingmouth "Since the issue's been raised, I'd like to ask for everyone to show up to the election on Saturday."
        
        $ TraitChange("Patience")
        
        red @angrybrow talking2mouth "You can just look at our posters to see what voting for us will get you."

red @talkingmouth "Curfew. Co-ed dorms. Tournaments. Club funding. These are all {i}real{/i} benefits you'll see immediately."
red @happy "Democracy's important. Frankly, you can't afford {i}not{/i} to vote in this election. It's the only one you'll get for this school."

pause 1.0

red @happy "Hope to see you there. Saturday morning, in the auditorium."

pause 1.0

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.0)

hide oakbg
hide hilbert
hide leaf
hide whitney
with dis

pause 1.0

show flannery uniform tiredbrow tiredmouth with dis

flannery @talking2mouth "Uggggh. Way too early in the morning for this kind of self-promotion."

if (GetRelationship("Flannery") == "Flannery"):
    red @closedbrow talking2mouth "Didn't you say you had to do a bunch of promotion for your gym, back in Lavaridge?"

    flannery "Yeah."

    pause 0.5

    flannery @closedbrow talking2mouth "And I hated it."

red @happy "Sorry, Flannery! I'll see you in the auditorium on Saturday, though?"

flannery @talking2mouth "Yeah. {i}Everyone{/i}'ll be there. It's too damn early to hold an election, if you ask me, but whatever."

show whitney uniform frownmouth with dis:
    xpos 0.25

show flannery:
    ease 0.5 xpos 0.75

whitney @happy "It's true! Well, not the 'being too early bit,' but everyone going to be there. From the people I've been talking to, you've really convinced people to go vote!"

red @happy "Hey, I might not be good at politics, but I know how to talk to people. We just had to tell people why they should care, and they did."

pause 0.5

red @talkingmouth "Hey, what's wrong?"

whitney -frownmouth @surprisedbrow talkingmouth "Oh? {w=0.5}Guess you caught that, huh?"

whitney @closedbrow talkingmouth "I'm concerned about Tia. She's been moody recently. Like, since yesterday."

red @confused "That doesn't seem like a very long time to be moody."

whitney @talking2mouth "No, it's not, but she's usually hyper-happy, all the time."

flannery @closedbrow talking2mouth "It gets annoying."

whitney @talking2mouth "A little bit, but it's part of her, you know?"

red @confused "Have you asked her what's wrong?"

whitney @talking2mouth "Yeah, but she won't say. Maybe you could ask her?"

red @closedbrow talking2mouth "Sure. I'll find her before lunch."

whitney @talking2mouth "Alright. Thanks!"

whitney @happy "Oh, and good luck on your student council thing!"

red @sweat happy "Heh. Thanks."

jump homeroom1transition