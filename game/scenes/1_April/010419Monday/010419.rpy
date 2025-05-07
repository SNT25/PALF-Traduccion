label day010419:

$ timeOfDay = "Morning"

if (pikachuobj in playerparty):
    $ playerparty.remove(pikachuobj)

call calendar(1) from _call_calendar_14
$ calDate = calDate.replace(day=19, month=4, year=2004)

show morning at vspaz

pause 3.0

$ renpy.music.play("Audio/Morning_ambience.ogg", channel='crowd', loop=True, fadein=1.0)

scene dorm_A with transeye2
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.0, hard=True)

hide blank2

red casual hatless @closedbrow talking2mouth "Man. Being at Kobukan's my dream, but I definitely didn't hate Mondays until I got here. Better pull myself out of bed..."

show calem uniform at leftside with dis

calem @talkingmouth "Good morning, [first_name]."

red @talkingmouth "Hey, Calem. You're up early. Campaign stuff?"

calem @talkingmouth "Quite. I'm actually just returning from the lunch hall, where Serena and I were doing an early-morning Q&A." 
calem @closedbrow talking2mouth "I must say, I'm surprised to see how seriously you took my advice. Very well done."

red @closedbrow talking2mouth "Huh? What do you mean?"

calem @happy "Please, don't be modest. I suppose I shouldn't have doubted your drive."

red @confused "Uh... Calem, I'm not being modest. I really have no idea what you're talking about."

calem @surprised "Oh? Didn't you put campaign posters up yesterday? All over the school?"

red @surprised "Campaign posters? I just hung out with some friends, did some training, studied a bit."
red @talkingmouth "Normal Sunday stuff."
red @closedbrow talking2mouth "Posters probably would've been a better use of my time, come to think of it..."

calem @closedbrow talking2mouth "Well... that's odd."

red @confused "What's up?"

calem @talking2mouth "I think you had better take a look at this."

show calem surprisedbrow frownmouth with dis

show ethan with dis:
    xpos 1.5 ypos 1.5 rotate 45
    ease 1.5 xpos 0.5 ypos 1.0 rotate 0

pause 1.0

ethan @talkingmouth "That's a cliché."

calem @talkingmouth "Hm?"

ethan @talkingmouth "Like, when someone says 'you better take a look at this' instead of just {i}telling{/i} them what they'd better take a look at."
ethan @happy "Happens {i}all{/i} the time in movies."

calem -surprisedbrow -frownmouth -surprised @angry "Right, well, I'm not doing it for dramatic tension. I just find it difficult to explain exactly what I saw."

show ethan with dis:
    xpos 0.5 ypos 1.0 rotate 0
    ease 1.5 xpos 1.5 ypos 1.5 rotate 45

ethan @closedbrow talking2mouth "Eh."

pause 1.0

$ PlaySound("body roll.ogg")

red @talkingmouth "Dude, you {i}do{/i} have to get up for class."

ethan @talkingmouth "Ehhh..."

red @happy "Well, give me a second to get changed, Calem, then I'll follow you to wherever you saw this thing."

scene academyhall with wipeleft

stop sound channel "crowd" fadeout 1.0
queue sound "audio/bigcrowdloop.ogg" channel "crowd" fadein 1.5

red uniform @surprised "Woah. Big crowd. What're they all looking at...?"

narrator "You make your way to the front of the crowd, and see, posted on top of the homeroom assignments..."

show academyhall_blur
show kobukan_trash 
with dis

pause 2.0

red @surprised "What the hell?"

calem uniform @talkingmouth "You can see why I assumed this was because of you."

serena uniform @happy "Personally, I thought it was a brilliant move!"

calem @surprised "Ah! Serena. You're here."

serena @talkingmouth "It's controversial, it's edgy. It spits in the face of the other Student Council hopefuls, with their grand ambitions and structural changes."
serena @closedbrow talking2mouth "It puts in one's face that you, [first_name], have picked up trash. Such a simple thing. A minor thing, even. But still, a thing."
serena @angrybrow happymouth "And it dares to ask the question--what, then, have you done? It forces the viewer to reflect. And they'll remember that when it's time to cast their ballots."

pause 1.0

serena @talkingmouth "A masterful piece of politicking, [first_name]. I wish I'd thought of it."

red @confused "Yeah, the only problem is, {i}I{/i} didn't. I have no idea how this got up here."

calem @closedbrow talking2mouth "{i}These{/i} got up here. They're all over the campus."

red @surprised "Huh?"

calem @talkingmouth "There are so many of them, I can't imagine a single person did this. If they did, then they must have had help from their Pokémon."

red @closedbrow talking2mouth "Hm... is this what Silver meant when he said he'd help me get elected, then? I guess I'd better thank him during lunch."

Character("Befuddled Student") "\"I don't get this. Is this guy running a cleanliness campaign?\""

Character("Clean Student") "\"It's that guy who's running for Student Council, isn't it?\""

$ beter = ("B" + first_name[1:] if first_name[0] not in ["B", 'b'] else "D" + first_name[1:])
$ biffin = ("B" + last_name[1:] if last_name[0] not in ["B", 'b'] else "D" + last_name[1:])

Character("Confused Student") "\"Yeah, wasn't his name [beter] [biffin] or something?\""

show side red uniform thinking with dis

"{color=#cf0000}[beter] [biffin]" "{w=0.5}.{w=0.5}.{w=0.5}.Ooh boy."

hide side red with dis

serena @talkingmouth "{w=0.5}.{w=0.5}.{w=0.5}.Hee."
serena @happy "Hee hee hee! [beter] [biffin]! Oh, that's good! Hee hee hee!"

calem @closedbrow happymouth "Ah, there goes the giggle box again..."

menu:
    "{color=#e226a6}[[Patience]{/color} >Wait to see what happens":

        $ TraitChange("Patience")

        Character("Befuddled Student") "\"Well, if this guy {i}is{/i} running for Student Council, I like him more than that Cheren guy.\""
        
        Character("Clean Student") "\"Yeah. Raises for non-academic staff? I don't want to pay even more for tuition!\""

        Character("Confused Student") "\"Besides, he looks pretty down-to-Earth. I can dig a guy who isn't afraid to get his hands dirty picking up trash.\""

        stop sound channel "crowd" fadeout 1.0

        pause 1.0

        redmind @sadbrow frownmouth "I really don't even have to try, huh...?"

    "{color=#b7669e}[[Charm]{/color} >Explain yourself to the crowd":

        $ TraitChange("Charm")

        red @happy "Hey! My name's [first_name] [last_name]. I'm running for Student Council."

        red @talkingmouth "I don't know how these posters got up here, actually, but as long as they raise awareness of my campaign, I guess that's alright."

        Character("Befuddled Student") "\"What're you going to do if you get elected then?\""
        
        Character("Clean Student") "\"Yeah. You're not going to give raises for non-academic staff, are you? I don't want to pay even more for tuition!\""

        red @closedbrow talking2mouth "I'm not sure that's something a Student Council member can even do, actually."

        red @happy "I'm mostly just running on the co-ed dorms and toilet paper issues."

        Character("Confused Student") "\"Well, I'd prefer if you paid more attention to the curfew lobby, but you look pretty down-to-Earth. I can dig a guy who isn't afraid to get his hands dirty picking up trash.\""

        Character("Befuddled Student") "\"Can't imagine Prince Cheren doing that, can you!\""

        red @angrybrow talking2mouth "Hold on. I'm not badmouthing Cheren here. He's got good policies, and a clear vision for what he wants this school to be."

        stop sound channel "crowd" fadeout 1.0

        pause 1.0

        narrator "The crowd, chastened, quickly disperses."

        redmind @sadbrow frownmouth "I really don't even have to try, huh...?"

show blank2 with splitfade
$ renpy.music.stop(channel='crowd', fadeout=1.5)
stop music fadeout 1.5

$ renpy.pause(2.5, hard=True)

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)

show oakbg at dissolvein behind blank2
show homeroom behind oakbg

hide blank2 with splitfade

$ renpy.pause(0.6, hard=True)

oak @talkingmouth "Good morning, ladies and gentlemen! I know better now than to extoll the virtues of a 'happy Monday,' so I'll simply remind you all that you have a quiz this evening!"

$ PlaySound("class_groan.ogg")

pause 2.0

oak @talkingmouth "{size=30}Hm... so the students aren't fans of Mondays {i}or{/i} quizzes. Good to know. I should start a book on the matter...{size=25}"

pause 1.0

oak @talkingmouth "Well, fan or not, it's time to begin class! We've got a lot of material to cover if we want you to be fully prepared for this evening's quiz." 
oak @talkingmouth "The first thing we should discuss is {i}accuracy.{/i} Remember the old adage--if it's not 100%% accurate, it's 50%% accurate!"

jump homeroom1transition