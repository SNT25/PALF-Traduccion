label secondhomeroom010413:

scene blank2

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom behind blank2

show oakbg behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade

oak @talkingmouth "...To summarize, the range of Pokémon intelligences varies greatly. Some, like Alakazam, have consistently shown IQs that are incomparably vast compared to human intelligences."
oak @talkingmouth "On the other hand, certain Pokémon, like fellow Psychic-type Slowbro, register as so unintelligent that they should be incapable of the very act of living." 
oak @talkingmouth "As such, many leading researchers believe that human methods of measuring intelligence simply don't work on Pokémon, whether intelligent..."

$ renpy.music.set_volume(0.1, delay=1.0, channel="music")
$ PlaySound("BellChime.ogg")

$ renpy.pause(2.0, hard=True)
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

oak @talkingmouth "...or not.{w=0.5} And that, I believe, was the bell. Dismissed!"

hide oakbg with dis

pause 2.0

show oak with dis

oak @talkingmouth "Lad. How's miss Vongole doing?"

red uniform @closedbrow talking2mouth "Vongole... oh, Ti-Bianca! Got it!"
red @happy "Yep! Uh, she got lost before her first elective, but I think Whitney's helping her out now."

show flannery uniform at rightside with dis

flannery @happy "Oh, that's where she went? I was wondering. We were meant to go shopping together. Thanks!"

redmind @thinking "Seeing Flannery all chipper in the evening is... {w=0.5}deeply disturbing."

hide flannery with dis

oak @happy "Lovely! Incidentally, I sent a team out to the meteor crater earlier today."

red @talkingmouth "Oh, great! Find anything interesting?"

oak @closedbrow talking2mouth "I haven't a clue. The team collected a few shards, and took a soil sample of the area, but nothing substantial."
oak @talkingmouth "And even if they'd found something more, I'm not an astrogeologist. I've placed some calls to a few contacts in Hoenn, though, and hopefully they send someone here to take a better look at it."

red @happy "Man, it's rare that you admit there's something you don't know."

oak @happy "Well, it's rare that there's something that I don't know."

redmind @thinking "Humble as ever..."

oak @talkingmouth "In any case, the team has confirmed that the field is safe to be out in, so feel free to return whenever you want. You may find it useful for training."
oak @closedeyes talkingmouth "I'll be going now."

hide oak with dis

pause 1.0

redmind @happy "...And there he goes, leaving without a chance for me to reply. Amazing a man as smart as him has managed to go sixty years without figuring out the basics of human interaction."
redmind @thinking "Actually... after I lost all my friends back home, I was always grateful that he was still my friend, despite the age difference. I mean, he was my only friend." 
redmind @frownmouth "But I was probably his only friend in Pallet Town... like, ever."
redmind @sad ".{w=0.5}.{w=0.5}.{w=0.5}Poor man."

call freeroam from _call_freeroam_2

scene dorm_B norm
show screen currentdate
with Dissolve(2.0)

stop music fadeout 2.5

queue music "Audio/Music/Road to Viridian City.ogg"

show ethan at centerside with dis

ethan @talkingmouth "Hey, man."

red @happy "Oh, hey! What's up?"

ethan @closedbrow talking2mouth "Uh... a new girl showed up in Professor Cherry's class today."

red @confused "Oh, that right? What was she like?"

ethan @happy "Short."

redmind @thinking "She really is."

ethan @talkingmouth "Nah, actually, she seemed a bit weird. She didn't say a word, but she was bouncing up and down in her seat all lesson."
ethan @closedbrow talking2mouth "Sometimes Professor Cherry would ask her a question, and she would just flash gang signs at her."
ethan @happy "I didn't get it, but it looked like the Professor did."

red @sadeyes sadeyebrows happymouth "Hah. I wonder what that's about...?"

ethan @happy "Beats me, dude. I'm going to bed, though. G'night!"

hide ethan with dis

pause 1.0

redmind @thinking "...Hm. That reminds me. If I'm trying to keep the fact that Tia is here a secret, I should probably ask Skyla and Brendan to stay quiet about it."

show brendan with dis

brendan @talkingmouth "Yeah? What's up?"

red @talkingmouth "Hey. You haven't told anyone about that meteor this morning, have you?"

brendan @closedbrow talkingmouth "Nah. I was going to tell May later, but the whole thing kinda just freaks me out, so I haven't gotten around to it."

red @happy "Cool. Would you mind continuing to not tell anyone?"

brendan @surprised "Huh? Well... yeah, sure, I guess." 

pause 1.0

brendan sad "Not even May?"

red @closedbrow talking2mouth "...I guess May's alright. Couples shouldn't have secrets from each other. But tell {i}her{/i} not to tell anyone."

brendan happy "Right on, man. I'm turnin' in now."

red @talkingmouth "Goodnight!"

hide brendan with dis

pause 2.0

redmind hatless casual @thinking "I don't have Skyla's contact information, so I'll just talk to her tomorrow, I guess..."

call afterroomsetuptexting from _call_afterroomsetuptexting

jump day010414