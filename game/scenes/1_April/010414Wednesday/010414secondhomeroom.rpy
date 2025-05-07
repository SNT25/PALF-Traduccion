label secondhomeroom010414:

scene blank2

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom behind blank2

show oakbg behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade

oak @talkingmouth "...So, it's important to remember that Pokémon seem to have an innate desire toward cooperation." 
oak @talkingmouth "There are exceptions in both directions, of course, such as the incredibly cooperative Passimian, or endlessly {i}un{/i}cooperative Zweilous."
oak @talkingmouth "Still, a wild Pokémon that asks another wild Pokémon to assist is likely to receive its desired assistance."
oak @talkingmouth "Perhaps it's the universality of the Pokémon 'language'? Or perhaps Pokémon simply do not regard each other with suspicion, as humans do?"
oak @talkingmouth "The answer to this is unlikely to be learned during my lifetime."

$ renpy.music.set_volume(0.1, delay=1.0, channel="music")
$ PlaySound("BellChime.ogg")

$ renpy.pause(2.0, hard=True)
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

oak @talkingmouth "Still, we can hope.{w=0.5} Dismissed!"

hide oakbg with dis

pause 2.0

show leaf uniform with dissolve

leaf @sarcastic "You ever notice that Oak leaves a lot of his questions really open-ended?"

red uniform @talkingmouth "Well, that's science, I guess. Awesome if we can find hard answers, but most of the time, the scientists' job is just asking questions."

leaf @sarcastic "Maybe if you're a {i}lame{/i} scientist. If you're an awesome one, you just resurrect fossils and drown in boatloads of cash."

red @closedbrow talking2mouth "I can't imagine your clientele is too expansive in that field?"

leaf @happy "Nah, but those who {i}can{/i} pay will pay out the nose for it."

red @talking2mouth "I'd rather they pay out their wallet."

leaf @happy "Hey, if it's green, it's money."

redmind @thinking "Ew."

red @talkingmouth "Ignoring that, what's up?"

$ lowerrank = GetRelationship("Leaf").lower()
leaf @happy "What, can't a girl just check in on her [lowerrank] without an ulterior motive?"

red @happy "I'm sure some could, but that's not what you're doing, is it?"

pause 2.0

leaf @sadbrow happymouth "Guess I'm kinda obvious, huh? I'm {i}crazy{/i} curious to know what's up with that new girl who's been following you around."

red @closedbrow talking2mouth "Uh... I can't say, I'm afraid. I mean, I don't even know, but..."

red @surprised "Oh, shit! Skyla! I forgot, I need to talk with her. Guess I'll do that after my free time this evening."

leaf @closedbrow talkingmouth "Skyla?"

red @talkingmouth "Yeah, she's a pilot."

pause 1.0

leaf @sarcastic "What's the punchline?"

red @closedbrow talking2mouth "It's a bunch of people queueing for a bowl full of fruit juices and spices, but that's not important right now."

leaf @sad "Okay, I'm lost."

red @happy "Do you want a pamphlet? It's got a map on it."

leaf @happy "Bro, sure."

pause 2.0

red @closedeyes happymouth "Heh. We're fun."

leaf @happy "We totally {i}are.{/i}"

leaf @talking2mouth "Can't help you with Skyla, though. Don't even know her."

leaf @closedbrow talkingmouth "Try talking to Whitney? She knows everyone."

red @talkingmouth "It looks like she already left... again."

show leaf:
    ease 0.5 xpos 0.75

show flannery frownmouth uniform at leftside with dis

flannery @talking2mouth "...Again? Aw. That's twice she's ditched me..."

leaf @surprised "Wait, she ditched you?"

flannery @talking2mouth "Yeah... we were supposed to go shopping yesterday, but she cancelled last-minute, so it was going to happen today, instead..."
flannery sadbrow @sad "But I guess that's not happening either."

leaf sadbrow frownmouth "Oh no... that's so sad!"

red @sadeyes sadeyebrows talkingmouth "I think that Bianca's just really running Whitney ragged. As soon as she gets used to her new schedule, I'm sure she'll have time to do fun stuff like that again."

leaf @surprised "Bianca? My roommate?"

flannery @talking2mouth "Nah, Bianca, {i}our{/i} roommate."

leaf @closedbrow talkingmouth "That'll get confusing."

pause 2.0

leaf angry "Well, I will not stand for this! No-one ditches a friend on an established engagement, {i}no matter{/i} how busy they are! We're all going shopping on Saturday, so clear your schedule!"

show flannery happy uniform with dis

pause 2.0

red @closedbrow talking2mouth "Uh... even me? I was kinda planning on getting started on this Student Council thing..."

leaf -angry @talking2mouth "{i}Especially{/i} you! You still need to learn how to use the city properly!"

red @closedbrow talking2mouth "I'm... pretty sure I just go into a store and buy something..."

leaf @sad "...Oh, you poor, deluded, fool. I have {i}so much{/i} to teach you."

red @talking2mouth "Looking forward to it."

call freeroam from _call_freeroam_3

stop music fadeout 1.5

$ renpy.music.queue("Audio/Music/MistraltonCity.ogg", channel='music', loop=True, fadein=1.5, tight=None)

show screen songsplash("Mistralton City Remastered", "Zame")

scene blank2

show hall_B 
show skyla
with dis

red @happy "Skyla, hey! Just the woman I wanted to see."

$ renpy.music.play("Audio/Pokemon/pikachu_norm1.ogg", channel="altcry", loop=None)
pikachu neutral_2 "Pikachu!"

skyla @talkingmouth "Oh? What is it? And who's this cute li'l guy?"

red @talkingmouth "This troublemaker is [pika_name]. He's my buddy."

red @happy "Anyway, you know that meteor we found out about yesterday?"

skyla @happy "Oh, yeah! The alien invader that we vanquished, right?"

red @closedbrow talking2mouth "Uh... not sure that's a completely accurate assessment of the situation, but close enough."

skyla @smirkmouth "Yeah, what about it?"

red @talkingmouth "Would you mind not telling anyone about it?"

skyla surprisedbrow frownmouth @surprised "Woah! How come? Is the meteor actually something big? Did someone find something?"

red @closedbrow talking2mouth "No, I just... uh..."

redmind @thinking "Man. I don't like keeping secrets like this. I feel like I have to lie more and more."

red @sadeyes sadeyebrows talkingmouth "It's to protect someone."

pause 1.0

skyla -surprisedbrow -frownmouth -surprised @angrybrow happymouth "Well, if it's to protect someone, say no more!" 
skyla @angrybrow happymouth "I'm always down to protect someone, and if I can do that just by shutting up, then that's what I'll do!"

show skyla surprisedbrow frownmouth with dis

red @happy "My hero."

pause 1.0

skyla happy "Wow. I actually felt something there. Uh, thank you." 

red @happy "Nah, thank {i}you.{/i} Oh, but I should be getting back for curfew. It's getting late."

skyla -happy @smirkmouth "Right. I'll see you, then."

hide skyla with dis

red @talkingmouth "Alright, [pika_name], let's--"

show skyla surprisedbrow frownmouth with vpunch

skyla @surprised "Wait!"

skyla sadbrow frownmouth @sad "Uh... I just remembered. I actually did already tell someone. About the meteor, the girl, you and Brendan. Everything."

red @closedbrow talking2mouth "Hm. Just one person?"

skyla @talkingmouth "Yeah, just the one. Gardenia. She's one of my dormmates."

red @talkingmouth "That's not so bad. Don't worry about it. I actually met Gardenia before, so I can just talk with her tomorrow."
red @happy "Thanks for the heads-up."

skyla @talkingmouth "Er... yeah. Sorry about my slip-up."

red @talkingmouth "It's cool. You didn't know."

hide skyla with dis

red @talkingmouth "Alright, guys, let's go to bed."

$ renpy.sound.play("Audio/Pokemon/pikachu_norm1.ogg", channel="altcry")
pikachu neutral_2 "Pikachu!"

$ renpy.sound.play(startercry, channel="altcry")
starter @talkingmouth "[starter_fragment]."

call texting from _call_texting_3

jump day010415