label day010414:

$ timeOfDay = "Morning"

if (pikachuobj in playerparty):
    $ playerparty.remove(pikachuobj)

call calendar(1) from _call_calendar_9
$ calDate = calDate.replace(day=14, month=4, year=2004)

show morning at vspaz

$ renpy.music.play("Audio/Morning_ambience.ogg", channel='crowd', loop=True, fadein=1.0)

scene dorm_A 
with transeye2
$ renpy.transition(dissolve)
show screen currentdate

show calem sadbrow behind blank2

$ renpy.pause(1.0, hard=True)

hide blank2

red hatless casual @talkingmouth "Morning, Calem. What's up? You look tired."

calem @surprised "Ah! You're awake?" 
calem @closedbrow talking2mouth "Oh, of course you are, you go for your runs every morning."
calem @talkingmouth "Yes, well... I am."

red @talkingmouth "Anything I can help with, or is it just general Kobukan stressors?"

calem @sadbrow talkingmouth "Serena and I have been... holding ourselves to an absolutely manic pace. At this rate, I'm not certain I even want to get into the Student Council."
calem @closedbrow talking2mouth "Of course, I simply {i}must{/i}, for my future career interests."

red @sad "Can't you slow down?"

calem -sadbrow @happy "Not while Cheren is out there. I think he got some bad news yesterday, because he's seemed to redouble his efforts."
calem @talkingmouth "We're all trying to get onto the same council, but with how much attention Cheren is drawing to himself--and not, necessarily, in positive ways--aligning myself with him is discomforting."

red @sad "Geez. I don't know. Cheren is ambitious, and passionate, but he obviously {i}really{/i} cares about the school. Why's he having so much trouble?"

calem @closedbrow talking2mouth "He wants sweeping reforms. But the polls show, overwhelmingly, that the students would rather just... well, have the Student Council organize a couple inter-school tournaments and leave it at that."

redmind @thinking "I get that. Most students will only be here for a year. Few of the changes Cheren wants to make are going to affect students this year."

calem @talkingmouth "I've privately cautioned him to focus more on the co-ed dorms, curfew, and toilet paper issues. That's where he's popular." 
calem @sad "But to no avail. If he believes people aren't appreciating his points, he just pushes them harder."
calem @surprised "I've even heard rumors that the school faculty is considering making a formal statement announcing some of his intentions {i}cannot{/i} be."

red @sad "So... do you think you'll have to run against him?"

calem @closedbrow talking2mouth "No, not quite yet. The voters simply decide who they want to be on the council. We're not directly competing for seats." 
calem @talkingmouth "But Serena and I may need to step away from Cheren's influence if we want to make any progress."

red @happy "Well, hey. I believe in you."

calem @happy "Much appreciated. I need all the belief I can get."

if (council_campaigning):
    calem @talkingmouth "Now, how are your own efforts going?"
    
    red @happy "I... might've bit off more than I can chew. My days are so busy, I haven't really had any time to sit down and really {i}focus{/i} on reaching out."
    red @closedbrow talking2mouth "...But from what I've heard, it sounds like I'm becoming kinda well-known already. Though I'm not sure what people think my positions are."

else:
    red @happy "Hey, Brawly and Cheren have both mentioned that my name is actually being bounced around a lot when it comes to Student Council stuff. What do you think about that?"

    calem @happy "Beyond my abject jealousy? Nothing."

    calem @talkingmouth "On a serious note, though, I strongly suggest you consider campaigning. With all these opportunities lined out in front of you, it would be a waste not to do so."

    red @confusedeyebrows frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    pause 2.0

    redmind @thinking "Oh. I get it. This wasn't actually ever a choice, was it?"

    red @angrybrow talking2mouth "Fiiiine. I'll do the Student Council thing. But only to help you out, and try to even out what Cheren's doing."
    red @angrybrow frownmouth "{size=30}Damn my inoffensive charisma...{/size}"

    narrator "For holding out against a half-dozen recruitment efforts, each less subtle than the last..."

    $ TraitChange("Patience")

    calem @happy "Splendid! That's very good to hear."

    red @closedbrow talking2mouth "Still, I don't know how I'm going to have time for this. My days are so busy, I haven't really had any time to sit down and really {i}focus{/i} on reaching out, even if I'd wanted to before now."
    red @talkingmouth "...Although it sounds like I'm becoming kinda well-known already. Though I'm not sure what people think my positions are."

calem @happy "Well, I'd strongly advise beginning your campaign in earnest as soon as you can. Two weeks, I think, is the absolute minimum amount of time you'd want to afford yourself."

red @closedbrow talking2mouth "So you're saying I can continue to goof off until Saturday?"

calem @sad "Er... that wasn't what I was {i}trying{/i} to say, but... I suppose so?"

red @happy "Cool. Now, let's get dressed. I skipped breakfast yesterday to go running with Brendan, some stuff happened, and I felt dead on my feet all afternoon."

$ renpy.music.stop(channel='crowd', fadeout=1.0)

scene blank2 with Dissolve(2.0)

stop music fadeout 1.5

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)

show homeroom behind oakbg

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade    
hide morning

show oakbg with dis

$ renpy.pause(0.6, hard=True)

redmind uniform -hatless @wince frownmouth "...Damn. From the lecture, I can tell that I missed some pretty key information in yesterday morning's homeroom. I really gotta be careful not to miss another homeroom like that again."

oak @talkingmouth "Now, can someone summarize what the Cortondo incident was?"

oak "{w=0.5}.{w=0.5}.{w=0.5}."

oak @talkingmouth "No-one? Remember, two Pokémon were attracted to a woman who had suffered a mental breakdown. [first_name], how about you?"

redmind @surprised "What?! I wasn't here for morning homeroom yesterday! Give me a break, Sam..."

menu:
    "{color=#66b77d}[[Knowledge]{/color} >Try to recall what you know about Cortondo":

        red @closedeyes talking2mouth "Okay. Cortondo incident... the name sounds Paldean. And I'm pretty sure Hatterene and Blissey can be found in Paldea. So..."

        $ TraitChange("Knowledge")

    "{color=#60c2f8}[[Wit]{/color} >Figure it out based on what the Pokémon might be":
        red @closedeyes talking2mouth "Okay. So, two Pokémon were 'attracted' to a human having a mental breakdown. I think Blissey and Hatterene seem the most likely in that case?"

        $ TraitChange("Wit")

oak @talkingmouth "Yes, correct! A woman having a mental breakdown attracted a Blissey and a Hatterene simultaneously."

oak @talkingmouth "As you may recall, Blissey will travel many miles to comfort a person who they perceive to be distressed, and are capable of sensing upset people from an equally far distance."
oak @talkingmouth "Hatterene will similarly travel many miles to find a distressed person... but, rather, to 'quiet' them."
oak @talkingmouth "The Blissey and Hatterene in this situation were equally matched." 
oak @talkingmouth "Given they both had access to recovery moves and many wild Leppa berries, they were able to wage a guerilla war on each other for weeks, terrorizing the town."
oak @talkingmouth "Of course, the townspeople's terror just attracted {i}more{/i} Blissey and Hatterene. Eventually, the hordes were dispersed through the efforts of elite trainers from the local Naranjuva Academy."

jump homeroom1transition