label secondhomeroom010421:

scene blank2

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom behind blank2

show oakbg behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade

oak @talkingmouth "And that about wraps up this lesson! Remember--the ability Sturdy not only prevents a Pokémon from being knocked out at full health, but also grants full immunity to One-Hit KO moves."
oak @talkingmouth "This rarely comes up, but it's worth remembering. Another thing worth remembering is that if a Pokémon with Sturdy loses health, then is restored to full health again, Sturdy will {i}still{/i} work."

$ renpy.music.set_volume(0.1, delay=1.0, channel="music")
$ PlaySound("BellChime.ogg")

$ renpy.pause(2.0, hard=True)
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

oak @talkingmouth "Keep that in mind! And as long as you do, you're all dismissed."

hide oakbg with dis

redmind uniform @thinking "Alright. Cheren wants to talk to me after school, so I guess I might as well just kill time until that happens."

if (wins > 4 and falinksobj in playerparty):
    red @happy "Maybe I could train [falinks_name] for a while!"
elif (wins < 5):
    red @closedbrow talking2mouth "I didn't do great at the battle tryouts, so I should train up before our meeting on Friday."

call freeroam from _call_freeroam_7

scene blank2

show clouds
show garden night 
show cheren at night
with splitfade

stop music fadeout 2.5

queue music "audio/music/Nuvema2_Start.ogg" noloop
queue music "audio/music/Nuvema2_Loop.ogg"

red night @happy "Hey, Cheren! It's been a while! What's up?"

cheren "{w=0.5}.{w=0.5}.{w=0.5}."
cheren @closedbrow sadmouth "I came here expecting a confrontation. And yet, upon seeing your eyes, I find all my desire to berate or chastise escapes me."
cheren sadbrow @sadmouth "Why, pray tell, do you think that is?"

red @sad "Oh... geez. Um... I mean... I don't want to fight. Pokémon battle, maybe, but... not a fight."

cheren @sadmouth "Nor I."

pause 1.0

cheren -sadbrow @sadmouth "I've come across some disturbing news, [first_name]."
cheren @closedbrow sadmouth "Disturbing news that directly involves you."

red @sad "[ellipses]"

cheren @sadmouth "Do you remember those two purple-clad students Nate, Blue, and I fought on the tenth?"

red @sadbrow talking2mouth "Yeah."

cheren @sadmouth "They hurled some vicious allegations at you. Accusing you of getting in through nepotism."
cheren @closedbrow talking2mouth "I thought nothing of it. Sharp words from an unpleasant pair of jealous fools."
cheren @sadmouth "But then you revealed you actually {i}do{/i} know Professor Oak. That alone, I could dismiss as a coincidence, but..."

pause 1.0

cheren @sadmouth "Blue has a habit of ranting about you. I swear, every third word out of his mouth is [first_name]."
cheren @sad "And... from what I've gathered in those rants... Professor Oak seems especially fond of you. Moreso than he is towards his own grandson."
cheren @sadmouth "Again, hardly what I'd consider an issue {i}by itself.{/i}"

pause 1.0

red @sad "...But Sam told you to stop looking into me."

cheren @surprised "Oh? You already know?"

red @closedbrow talking2mouth "Yeah. He told me. Look, Cheren, I..."

cheren @thinking "[ellipses]"

red @thinking "[ellipses]"

cheren sadbrow @sadmouth "I'm waiting for you to tell me that my concerns are misplaced, [first_name]."

show cheren shadow sad2eyes with dis

red @talking2mouth "...Professor Oak's recommendation played a very, {i}very{/i} large role in my admittance here."

pause 1.0

cheren @sadmouth "So. It's as I feared."

red @sad "Cheren, I'm working hard, {i}every day,{/i} to make sure that I'm worthy of Professor Oak's recommendation."

if (wins > 4):
    red @sad "I did well at the Battle Team tryouts."

if (GetGrade() == 4):
    red @sad "I've passed all my homeroom tests."

cheren @sadmouth "My fear was less that you earned your spot through... nonstandard... means and more that... you, {i}too,{/i} have."

red @surprised "Huh?"

cheren -shadow -sad2eyes @closedbrow sadmouth "[first_name], I finally understand why the more I get my message out there, the less people care to hear it."

pause 1.0

cheren @sadmouth "I can count on one hand the number of people who got into this school purely on the basis of academics or skill at training."

cheren @sad "Amusingly, the only other person I can be certain didn't {i}bend{/i} the rules is my dormmate, Professor Oak's own grandson."

cheren @happy "If I were to attempt to remove all the students who did not follow the standard admissions process, I'm certain the school would be entirely empty."

pause 1.0

cheren @closedbrow sadmouth "Perhaps it doesn't matter. I've made so many compromises already. What's one more?"

pause 1.0

red @talking2mouth "I'm really sorry about this."

cheren shadow sad2eyes @sadmouth "Don't be. There's no point in {i}both{/i} of us despairing over the issue."

pause 1.0

cheren -shadow -sad2eyes @sadmouth "Anyway. Bianca told me that you had something you wanted to say to me, too?"

red @surprised "Oh... geez, uh, I did, but I'm not sure if now's the best time..."

cheren @closedbrow sadmouth "Please. Go ahead."

red @talkingmouth "Alright. I was just thinking about how you were planning on repealing the curfew."

cheren @happy "Ah, yes. One of my few campaign points that I may actually be able to deliver on."

red @closedbrow talking2mouth "Right. I was just wondering... are you sure that's a good idea?"

show cheren surprisedbrow frownmouth with dis

cheren @talkingmouth "{w=0.5}.{w=0.5}.{w=0.5}.What?"

red @talking2mouth "I was in the city recently. There are a bunch of thugs there, and I know they wander near the school at nighttime."

red @confused "If you repeal the curfew, aren't you concerned that you might be putting students at risk of running into them?"

pause 1.0

cheren -surprisedbrow -frownmouth -surprised @angry "...I was under the impression that repealing curfew was a cornerstone of your campaign, as well."

red @closedbrow talking2mouth "I mean... I'm not sure I ever established what the cornerstones of my campaign were."

cheren @closedbrow angrymouth "No, of course you didn't. You've continued as you {i}always have{/i} in this process. Expending a fraction of my effort, and reaping multitudes of my rewards."

red @sad "Cheren..."

cheren @sadmouth "Let me be clear with you. I will {i}not{/i} consider leaving the curfew in place."
cheren @angry "This is a measure that will {i}benefit{/i} you. Do you not see that? You'll be able to go wherever you want at night. This is something I can do to help you. For what earthly reason could you rally against that?"

red @talking2mouth "...Like I said, the thugs."

cheren @sadmouth "We're going to a school for Pokémon trainers. I do not consider these unnamed 'thugs,' even if they exist, to be credible threats that we cannot fight off."

red @surprised "Wait... you don't believe me?"

cheren @angry "No, [first_name], I do not. With proof, I would believe you, but as of now, it seems you're propping up a bogeyman to get me to repeal one of my few popular positions."

red @sad "I'm... I'm not."

cheren @sad "Well. If you were, I'd say you have no need. You're doing well enough on your campaign without resorting to tricks like that. Certainly, if either of us needed to go on the offensive, it would be me."

pause 1.0

red @talkingmouth "...You still have my vote, Cheren."

cheren @closedbrow sadmouth "I appreciate that."

cheren @sad "I'll be keeping a keen eye on you, to ensure that you remain worthy of mine."

call clearscreens from _call_clearscreens_63
scene blank2 with splitfade

pause 1.0

cheren night @closedbrow sadmouth "What is it about that man...? I should hate him. I should be throwing the book at him, with as much force as I can muster. And yet..."

pause 1.0

cheren @closedbrow talking2mouth "Perhaps Blue will know."

call texting from _call_texting_6

jump day010422