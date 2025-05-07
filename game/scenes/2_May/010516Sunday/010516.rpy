label day010516:
$ timeOfDay = "Morning"
call clearscreens() from _call_clearscreens_173
call calendar(1) from _call_calendar_41


$ calDate = calDate.replace(day=16, month=5, year=2004)

$ HealParty()

stop music

scene blank2
show morning at vspaz

pause 3.5

show screen songsplash("Pallet Town", "Zame")
queue music "audio/music/palletpiano.ogg"

$ AddEvent("Yellow", "LostHat")

scene kitchen 
show leaf hatless at leftside:
    xzoom -1
show yellow neutralbraidfront at rightside
show ethan
with splitfade

red @talkingmouth "Morning, guys!"

leaf @happy "Morning!"

yellow @talkingmouth "Good morning."

ethan @talkingmouth "Sleep well?"

red @talkingmouth "Alright. Thought I had a weird dream, though."

yellow @talkingmouth "Yes... I did too, I think."

pause 1.0

red @talkingmouth "Got any coffee left?"

leaf @happy "Sorry, I just finished it."

red @confused "...Okay, but I can see the pot is still, like, a third full."

leaf @angrybrow angrymouth "{i}I just finished it.{/i}"

ethan @talking2mouth "Dude, she drinks it {i}straight{/i} from the pot. I've ordered a carafe, but until then, I'd be careful about where you pour that."

leaf @embarrassedbrow talkingmouth "It's not {i}my{/i} fault! I can't be trusted around breakable things before I have my coffee, and the coffee mugs are all super-breakable!"
leaf @closedbrow talking2mouth "It's just safer."

red @talking2mouth "That's something I wish I didn't know about you. Moving on."

red @talking2mouth "Yellow, what was Blue talking about last night? Actually, is he here?"

yellow @talkingmouth "He went out to the Battle Hall."
yellow @closedeyes angryeyebrows talkingmouth "I'm not quite sure what he wanted to talk about last night. He was acting a bit strange ever since our picnic, actually..."

redmind @thinking "Hm... does he remember, too?"

red @talkingmouth "Love the new hair, by the way."

yellow @happy "Oh! Thank you. I think I lost my hat yesterday at some point."

leaf @talkingmouth "Want to go into the city to get a new one?"

yellow @sadbrow happymouth "No, thank you. My hat was woven by my uncle Wilton. He makes them himself, to protect himself from the sun, while fishing, so he has lots of spares. I think I'll just ask him for another."

leaf @sadbrow talkingmouth "Aw. That is the {i}sweetest{/i} thing! I didn't know your hat had a story behind it."

yellow @talkingmouth "Yup. Made from dried straw grown right in Viridian Forest."

ethan @talkingmouth "Hey, so, don't you two have plans?"

yellow @talkingmouth "Hm? Leaf and I?"

ethan @talkingmouth "Nah, [first_name] and Lamina."

leaf @sarcastic "That's a new one."

leaf @talkingmouth "But, yeah, actually, you're right."

if (not rescuedtia):
    leaf @closedbrow talking2mouth "After the fuss yesterday, I'm kinda beat... all that hiking through the forest kinda exhausted me."

else:
    leaf @embarrassedbrow talkingmouth "Thing is, though... hah hah..."

    leaf @embarrassedbrow talkingmouth "The place I made a reservation at... uh... we totally missed that."

    leaf @happy "Aaaand it'll take a while for me to get a new reservation, so...?"

    red @talkingmouth "I get it."

leaf @sadbrow talkingmouth "Mind if we take a raincheck?"

if (HasEvent("Leaf", "AcceptedConfession")):
    red @happy "'Course not. But if you keep putting this off, I'm going to think you actually {i}don't{/i} want to date me."

else:
    red @happy "'Course not. But if you keep putting this off, I'm going to think you actually {i}don't{/i} want to hang out."

leaf surprised blush "Hah, whaaaat? No, I do, I definitely do! I just...{w=0.5} you know...{w=0.5} things!"

pause 1.0

leaf embarrassedbrow talkingmouth "I'm going!"

show leaf:
    ease 0.5 xpos 1.5

pause 1.0

redmind @frownmouth confusedeyebrows "{w=0.5}.{w=0.5}.{w=0.5}."

ethan @talkingmouth "Hah. Women, am I right?"

show ethan surprisedbrow frownmouth with dis

yellow cryingeyes smirkmouth @closedeyes happyeyebrows anger challengingmouth "I'm sorry, could you elaborate on that statement?"

ethan @talking2mouth "Uh...{w=0.5} Probably. But I choose not to."

yellow cryingeyes smirkmouth @closedeyes happyeyebrows anger challengingmouth "Wise choice."

red @sweat talkingmouth "See you guys. Stay alive, Ethan."

call clearscreens() from _call_clearscreens_174
scene blank2 with splitfade

pause 2.0

scene stadium_empty 
show janine smilemouth uniform:
    xpos 0.5 xzoom -1
show screen currentdate
with splitfade

pause 1.0

red @happy "Hi, Janine. What's up with the uniform on the weekend?"

janine @talking2mouth "Meeting a pretty important guest. Should be here in a couple hours. What about you? Anything I can do for you?"

red @talkingmouth "I was just looking for Blue. Guess he's not here, though?"

janine @talking2mouth "Yeah, not here. Came in a bit earlier, but left when he saw I was here."

red @closedbrow talking2mouth "That's weird. Normally he {i}likes{/i} an audience when he battles."

janine @closedbrow talking2mouth "Yeah, who knows. Maybe he's practicing a new technique."

red @talkingmouth "Maybe. Guess I'll catch up with him tonight."

janine @talkingmouth "Good luck."

$ removestudents = {"Blue"}

call freeroam from _call_freeroam_23

$ removestudents = set()

call clearscreens() from _call_clearscreens_175
scene blank2

narrator "Despite keeping an eye out for Blue all day, you still haven't seen him at all."

pause 0.5

narrator "Perhaps that's for the best."

scene hall_B_night with splitfade

stop music fadeout 1.5

show screen songsplash("A Rival Appears!", "Zame")
queue music "audio/music/rivalchill_start.ogg" noloop
queue music "audio/music/rivalchill_loop.ogg"

red @confused "...Weird. I wonder where--hm?"

show blue frownmouth with dis

blue @talkingmouth "Alright, [first_name]. I've got some questions, and you're going to answer them."

red @talking2mouth "Hi, Blue. Good to see you too. I haven't seen you all day."

blue @closedbrow talkingmouth "Yeah, {i}hi{/i}, whatever. Questions."

red @talkingmouth "Sure. I'll answer what I can. Is it more questions about [pika_name]? I told you everything I know about how he works."

$ PlaySound("idea.ogg")

blue @talkingmouth "It's not that. I want to know what happened on Saturday."

red @surprised "...Hm?"

blue @talkingmouth "I laid out a nice shirt for the picnic Saturday morning. I {i}know{/i} I did. But I ended up going out with Yellow in this old jacket."

red @surprisedbrow frownmouth "...Uh."

blue @angrybrow wistfulmouth "What's more, my ribs hurt like hell. And my pedometer said I took {i}way{/i} more steps than I thought I had."

red @sad2eyes talking2mouth "Uh... uh...?"

blue @closedbrow furiousmouth "Finally, my knuckles are bruised. Not like something hit them, but like {i}I{/i} hit something. What's that about?"

$ renpy.music.set_volume(0.2, 10.0)

narrator "Your eyes flit back and forth as you search for an easy explanation."

red @sweat sad2eyes talkingmouth "Um... well, you know, I could think of a couple explanations that are almost theoretically possible, so, uh..."

narrator "...You cannot lie, but you also cannot tell the truth. A certain familiar fog starts to creep towards you once again, and your throat tightens."

pause 1.0

narrator "You cannot spe-"

$ renpy.music.set_volume(1)

show hall_B_night with vpunch

blue @surprisedbrow desperatemouth "Hey, don't go silent on me now! It was just a damn question. If you can't answer it without freezing, then just forget it!"

narrator "You let out a breath you didn't realize you were holding."

red @sadbrow talkingmouth "...I'm sorry."

blue @talkingmouth "Whatever. I thought maybe you knew what this crystal shard I had was, but if you can't handle a damn conversation, just forget it."

pause 0.5

red @confused "Crystal shard?"

blue @talkingmouth "Yeah."
blue @happy "Pretty shiny, right? Wonder if Gramps would be interested in this?"

show blue:
    xpos 0.5
    ease 0.5 ypos 1.2 zoom 1.3

narrator "Blue shows you a shard of crystal in his hand. To your horror, it looks exactly like one of the meteorite shards that [pika_name] swallowed a week ago."

red @surprisedbrow talking2mouth "Blue. {i}Where{/i} did you get that?!"

blue @surprised "Huh? I just found it Saturday. It was in my... well, actually, I don't need to tell you where I found it, but it definitely didn't get there on accident."

narrator "Your mind races with what this could mean, if Blue had one of the AZOTH1 fragments in his possession. Does that mean he could make his Pidgeotto...?"

red @talking2mouth "Blue, I need you to give me that."

narrator "Blue's hand immediately closes on the shard."

blue @angrybrow happymouth "Nah, I don't think so. Knowing you want it, this has gotta be something pretty important, right?"

red @angry "Rrrrgh..."

blue @surprised "Oh, wow, you're seriously mad. What could..."

pause 1.0

narrator "Blue looks at the shard, then at you, then at [pika_name] on your shoulder."

$ PlaySound("idea.ogg")

blue -frownmouth angrybrow @talkingmouth "Oh, now I get it. This is one of those things that made [pika_name] so special, isn't it?"

red @closedbrow talking2mouth "Y-yes, it is, but, look, it's {i}really{/i} important no more of those get out, okay?! You need to give it to Sam, and--"

blue @talkingmouth "Nah. I'm taking this. Everything I've ever had, I took, and I'll take {i}this{/i}, too."

red @talking2mouth "Wait. Blue. I'll battle you for it."

pause 0.5

blue @frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
blue @closedbrow talkingmouth "Nah."

pause 1.0

blue @angrybrow happymouth "{size=40}Pidgeotto! How about a {i}meal?!{/i}{/size}"

$ PlaySound("pokemon/ball sound.ogg")

narrator "Your eyes widen as Blue grabs a Poké Ball from his belt and throws both shard and ball high into the air."

blue angrybrow happymouth "Say goodbye to what makes you special, [first_name]! Now it's {i}my{/i} turn to stand out! Gramps will have to study {i}my{/i} Pokémon! It's {i}my{/i} turn to--"

red @angry "[pika_name], grab the shard!"

$ renpy.music.play("Audio/Pokemon/pikachu_angry3.ogg", channel="altcry", loop=None)

libpikachu glowing @angryeyes happymouth sparks "Pik... Pika. Pikerachu!"

blue @talkingmouth "Pidgeotto, don't let him! Get the--"

show hall_B_night
show blue surprisedbrow frownmouth 
with vpunch

narrator "The two Pokémon collide in mid-air, sending the shard spinning off towards the floor, as another one of Blue's Poké Balls go off."
narrator "The Pokémon inside lands right in front of the shard."

hide blue with dis

$ sidemonnum = pokedexlookupname("Eevee", DexMacros.Id)
$ PlaySound("pokemon/ball sound.ogg")
$ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))

show sideportraitfull at pokeball, dormdesk

stop music fadeout 7.0

pause 2.0

sidemon @talkingmouth "Eve."

pause 2.0

narrator "Everyone--all four of you, Pidgeotto, Blue, you and [pika_name], are still for a moment, staring in horror at the curious foxlike Pokémon."

blue @sweat happy "He-ey! Eevee. Come on, now. That's a pretty important piece of rock you've got right there. Why don't you just pick it up and give it to Pidgeotto? You know, your teammate, your mentor?"
blue @angrybrow talkingmouth "{size=30}Stop him! Make yourself useful and tell him to leave the shard alone!{/size}"

red @angrybrow talking2mouth "{size=30}I can't command other people's Pokémon!{/size}"

blue @angrybrow talkingmouth "{size=30}Have you {i}tried?!{/i}{/size}"

red @closedbrow talking2mouth "{size=30}Well, no, but...{/size}"

red @sweat happy "Hey, Eevee. Why don't you go back into your Poké Ball. Nice and easy, you know? No need to make this {i}a thing.{/i}"

show cafe at sepia
show flashback
with dis

$ renpy.pause(1.0, hard=True)

show ethan uniform at sepia behind flashback with dis

pause 0.5

ethan @angrybrow talkingmouth "You know just as much as I do that [oldblue_name]'s Eevee wasn't listening to a single word he said."

red sepia @closedbrow talking2mouth "Yeah, I can't deny that. I guess it makes sense that he'd get such a willful and stubborn 'mon, though. Like trainer, like 'mon."

pause 1.0

show blank with splitfade

hide ethan
hide cafe
hide flashback
hide blank
with Dissolve(2.0)

pause 1.0

red -sepia @closedbrow talking2mouth "...Crap."

stop music

show sideportraitfull:
    ypos 0.78
    ease 0.2 ypos 0.81
    pause 1.0
    ease 0.2 ypos 0.78

$ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))
sidemon @talkingmouth "Nom."

blue @surprisedbrow talkingmouth "Crap!"

pause 1.0

$ renpy.music.queue("audio/music/evolution_cut.ogg", channel="evolution")

show supereevee behind sideportraitfull:
    align (0.5, 0.5) zoom 0.0 matrixcolor BrightnessMatrix(0)
    pause 2.4
    ease 0.6 zoom 0.1 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.2 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.3 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.4 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.5 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.6 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.7 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.7 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.7 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.7 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.8 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 1.0 matrixcolor BrightnessMatrix(1.0)
    ease 5.0 zoom 1.2

show sideportraitfull:
    ease 2.0 align (0.5, 0.5) zoom 1.0 matrixcolor BrightnessMatrix(0)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(0.1)
    ease 0.6 zoom 0.8 matrixcolor BrightnessMatrix(0.2)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(0.3)
    ease 0.6 zoom 0.7 matrixcolor BrightnessMatrix(0.4)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(0.5)
    ease 0.6 zoom 0.6 matrixcolor BrightnessMatrix(0.6)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(0.7)
    ease 0.6 zoom 0.5 matrixcolor BrightnessMatrix(0.8)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(0.9)
    ease 0.6 zoom 0.3 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.3 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.3 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.3 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.3 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.2 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.1 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)

show speedlines behind supereevee at speedlines
show blank2 behind speedlines with Dissolve(5.0)

pause 17.0

scene blank2
stop music
stop music channel "evolution"

pause 5.0

jump day010517