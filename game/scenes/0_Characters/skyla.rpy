label Skyla1:

if (not IsBefore(1, 5, 2004)):
    $ persondex["Skyla"]["Events"].append("Level2SceneVer2")

scene city_B
with Dissolve(2.0)
stop music fadeout 1.5
$ renpy.music.queue("Audio/Music/MistraltonCity.ogg", channel='music', loop=True, fadein=1.5, tight=None)

show screen songsplash("Mistralton City Remastered", "Zame")

show skyla surprisedbrow frownmouth with dis

skyla @talkingmouth "Woah! [first_name], is that you?"

red @talkingmouth "Huh? Oh, yeah. I was just doing some shopping. What's up?"

skyla -surprisedbrow -frownmouth -surprised @angrybrow happymouth "Adventure's up! I'm hot on the tail of a couple of criminals!"

red @closedbrow talking2mouth "...Criminals?"

skyla @happy "Yeah!"

red @talkingmouth "And these are definitely criminals, right? Because you thought a meteor was an alien invader."

skyla @angry "Hey! I still maintain that that meteor is not entirely {i}not{/i} an alien invader."

red @closedbrow talking2mouth "Right. Well, if you're trying to stop an actual criminal, shouldn't we leave that to the cops?"

skyla @closedbrow talking2mouth "Cops are useless! If anyone's going to step up and be a hero, it'll be us!"

red @confused "Okay. Just so I know what we're walking into here, these criminals are...?"

skyla @angry "A pair of skinheads. They look real mean, too."

red @closedbrow talking2mouth "And you know they're criminals because...?"

skyla @closedbrow talking2mouth "Well... I mean..."
skyla @angry "They're bald! And they were {i}skulking!{/i}"

red @confused "Skulking."

skyla @angrybrow happymouth "Yeah! They were...{w=0.5} kinda...{w=0.5} walking side-by-side...{w=0.5} and, uh...{w=0.5} looking shifty..."

red @closedbrow talking2mouth "Skyla, I think you might be hot on the tail of a couple of {i}bears{/i}."

skyla @surprised "No way! I know a human being when I see one."

red @talkingmouth "Alright. Well, why don't you lead me to these 'criminals,' and we'll see what mischievous deeds they're up to?"

skyla @happy "Gladly! They just went down this alleyway."

show skyla:
    ease 0.5 xpos 1.5

red @surprised "Wait... {i}that{/i} alleyway?! Skyla, stop!"

scene abandonedhouse with slideleft

pause 1.0

show skyla surprisedbrow frownmouth at night with dis

skyla @talkingmouth "Look! [first_name], this is it! I was right! This must be their evil hideout!"

show roughneck at leftside, night
show roughneck2 at rightside, night
with dis

pause 2.0

roughneck @happy "Hey, [first_name]."

skyla @surprised "You know these rogues, [first_name]?"

red night @sadbrow talkingmouth "Not personally?"

skyla angry "Well, halt, evildoers! Your machiavellian schemes end today!"

red @closedbrow talking2mouth "Oooh, boy. Okay, Skyla, these guys might not be the {i}most{/i} morally white, but the worst they'll do is steal someone's hat."

roughneck2 @happy "Yeah, I {i}did{/i} do that once."

roughneck @happy "Heh, me too."

skyla surprisedbrow frownmouth @surprised "See? They admit to their... their heinous crimes!"

red @talking2mouth "Skyla. You're massively outnumbered, there's a couple dozen guys as backup just twenty feet away in the shack, and their boss is a skilled trainer."

show skyla -surprisedbrow -frownmouth -surprised frownmouth with dis

red @happy "But let's ignore all that, and just play this out."
red @closedbrow talking2mouth "Let's say you {i}did{/i} manage to beat these two in a Pokémon battle."
red @happy "Which, let's be honest, isn't hard."

roughneck @angry "Oi."

roughneck2 @surprised "Yeah, we're tough as nails!"

red @talkingmouth "So, you've beaten them now. We can assume that your Pokémon will let you make them go wherever you want to bring them. What will you do with them?"

skyla @closedbrow talking2mouth "Um... tie them up a smidgen on the tight side, then leave them for the cops?"

red @closedbrow talking2mouth "Didn't you say the police were useless earlier? Well, whatever."

show skyla sad with dis

red @confused "How are you going to tie them up? A smidgen tightly or not? Do you have any rope? And how will you let the police know that they're here? Because, if you don't, they go free."
red @talking2mouth "Further, are you going to leave an explanation of why you beat and tied up these trainers? Do you have evidence of their crimes? Without those, the cops start looking for {i}you,{/i} and they go free."
red @closedbrow talking2mouth "That's not even mentioning that vigilantism is illegal. So beating and tying up a criminal, even if they totally {i}did{/i} do something wrong, is probably going to let them go free."
red @talkingmouth "Put simply; they go free."

pause 2.0

roughneck @happy "So... can we go free?"

pause 1.0

red @confused "Skyla?"

skyla closedbrow talkingmouth "Yeah... I guess."

hide roughneck
hide roughneck2
with dis

pause 1.0

skyla -closedbrow -talkingmouth frownmouth @angry "Dang it."

pause 1.0

red @happy "Alright. Let's get out of this alleyway, and maybe you can tell me what this was all about, alright?"

skyla @sad "Yeah... alright."

scene city_A
show skyla 
with Dissolve(2.0)

narrator "You spend several minutes walking together in silence until you make your way to a different part of the city, and Skyla's mood seems to improve."

red @talkingmouth "So. What was up with that, huh?"

skyla @smirkmouth "I... want to be a hero. I always have."

red @happy "Straight and to the point. I like that you know what you're about."
red @closedbrow talking2mouth "So, like, a firefighter?"

skyla @talkingmouth "No. Like... a real hero. A Superhero."

red @surprised "Uh... a superhero? That seems a bit... out of reach."

skyla @surprised "Does it? Really?"

red @confused "I mean... yeah. Doesn't it? Where would you get superpowers from?"

if (not IsBefore(1, 5, 2004)):
    skyla @talkingmouth "{i}You've{/i} got superpowers yourself, you know."

    red @closedbrow talkingmouth "Geez. Frienergy isn't a superpower, you know."

    pause 1.0

    red @sad2eyes talking2mouth "Okay, maybe it is, a little bit, but it's not {i}really.{/i}"

    skyla @talkingmouth "Anyway, since I wasn't born with superpowers, I know exactly where I could get mine from."

skyla @smirkmouth "My Pokémon."
skyla @talkingmouth "Pokémon can fly, turn invisible, read minds, be super-strong, be super-fast... superheroes already exist all around us. They're just called Pokémon."
skyla @talkingmouth "There has to be a way for a person to have those powers, too, right?"

if (not IsBefore(1, 5, 2004)):
    skyla @smirkmouth "Sabrina can read minds. Bea can punch through brick. You can make friends with anyone. There's gotta be a way, right?"

red @surprised "I... I guess? Maybe?"

skyla @closedbrow talking2mouth "Besides, you don't need powers to be a Superhero. You just need..."

pause 1.0

skyla @sadbrow smirkmouth "Well, I guess that's the problem. I don't know what you need to be a superhero."
skyla @closedbrow talkingmouth "I thought that if I stopped two criminals from... I don't know. Doing what they're doing... that maybe I'd be making some progress there."

red @talkingmouth "Tell me more. Where did this desire come from?"

skyla @talkingmouth "Well..."

if (not IsBefore(1, 5, 2004)):
    skyla @sad "When you were up on that stage, or when Sabrina was being harassed by those two punks... I wanted to help. I wanted {i}so desperately{/i} to help. But I had no idea what to do."

    skyla @closedbrow talkingmouth "I've always wanted to be a hero. That was my chance!"

    skyla @sad "...And I blew it."

    pause 1.0

if (not HasEvent("Skyla", "Backstory")):
    $ AddEvent("Skyla", "Backstory")
    skyla closedbrow talking2mouth "I'm from Mistralton City, in the West of Unova, but there's a town on the East side of the region called Lentimas, and they were, like, really isolated, so..."
    skyla happy sweat "I learned to fly so I could, uh, transport stuff over there. Food and medicine and stuff."

    pause 1.0

    red @talkingmouth "Uh... so you had family there, or something?"

    skyla -happy -sweat talkingmouth "Nope. No connection. Well, before I got my pilot's license, anyway."

    red @talkingmouth "So you just... learned to fly planes... to help out a town on the opposite side of the region? That you had no connection to?"

    skyla closedbrow sweat -talkingmouth @talkingmouth "Yyyyyep."

    red @happy "That's insane."

    skyla @smirkmouth "I've heard that before."

skyla @closedbrow talking2mouth "I just... heroes are {i}it{/i}, you know? They're the best thing there is. The best kind of person."
skyla @happy "Think about other titles. There can be bad presidents, bad cops, even bad Champions."
skyla @smirkmouth "But there's no such thing as a bad hero."

red @closedbrow talking2mouth "I guess that's true."

show skyla:
    ease 0.25 ypos 1.2 zoom 1.3

skyla @talkingmouth "I want to {i}help{/i} people, [first_name]. Really help them. And I want to punish those who hurt others."

red @sadbrow talkingmouth "You're already the one point of contact to an extremely isolated town back in Unova. And you're still doing flights for them, right?"

skyla @talkingmouth "Yeah. Not as often as I used to, but my family's taken over most of my flights while I'm in Kobukan."

red @closedbrow talking2mouth "I can't help but feel like you're already helping people. Like, a {i}lot.{/i} Doesn't that mean you're already a hero?"

skyla @talkingmouth "...I thought so, at first. Like, right after I got my pilot's license, for a few years, I really thought that was all I needed."

pause 1.0

skyla @smirkmouth "But I've been doing that for a few years. And I'm kinda over it. If I'm going to be a hero, a {i}real{/i} hero, I'm going to need to do more than just transport food and medicine to people."

red @confused "So you settled on stopping criminals."

skyla @talkingmouth "Yeah! When I graduate, I want to become a Pokémon Ranger."

red @surprised "Like the TV Show?"

skyla @angry "Wha- no! Like the job!"
skyla @smirkmouth "There's this one super-famous and super cool ranger in Fiore--well, actually, she's from Almia, but she lives in Fiore now--called Elita."
skyla @happy "She's famous for this awesome Skarmory she flies around with, and everyone calls her the 'Steel Samurai of the Sky!'"

red @confused "Everyone?"

skyla @closedbrow talking2mouth "Well, the producers of {i}Pokémon Rangers{/i} call her that."

red @confused "The producers of the job?"

skyla @angry "Wha- no! The show!"

pause 1.0

skyla @talkingmouth "Oh, wait. You were messing with me, weren't you?"

red @happy "Maybe a little bit."

skyla @happy "Jerk. Be serious! I'm pouring out my hopes and dreams for you here."

red @closedbrow talking2mouth "I mean, being a Ranger is a great goal. And I support that for you, seriously. But running into the middle of a city, and looking for a fight, just seems dangerous."
red @happy "And I can't see how that'll make you any more heroic, honestly."

skyla sad "But..."

red @closedbrow talking2mouth "If you want to be a hero, I think the best chance you have is to {i}help{/i} people. Keep on doing what you've been doing."

skyla @thinking "[ellipses]"

red @talkingmouth "No-one's going to think you're any less of a good person if you do the same good things every day."

skyla @talkingmouth "Yeah, but would you watch a cartoon where the hero does the exact same thing in every episode?"

red @talkingmouth "I... didn't really watch a lot of TV. But I guess that does sound... boring."

skyla @talkingmouth "I don't want to be a... a {i}fixture{/i}, [first_name]."
skyla @happy "I want people to {i}cheer{/i} when they see me. Not just think 'oh, here comes Skyla, with the food again.'"

red @talkingmouth "Then... are you really doing it for other people? Or are you doing it for yourself?"

skyla @sad "{w=0.5}.{w=0.5}.{w=0.5}."
skyla @closedbrow talking2mouth "If I wanted to do good things for the wrong reasons, is that so bad?"

red @closedbrow talking2mouth "I genuinely have no idea. We might need to ask a Professor that one. It's a bit too philosophical for me to figure out."

skyla -sad @talkingmouth "Well, alright, then! Let's do that."

red @surprised "Huh? Do what?"

skyla @happy "You suggested it! Talk to a Professor, goof."
skyla @talkingmouth "Even if they can't answer whether selfish good is still good, maybe they can think of ways I could satisfy my desire to be a hero..."

pause 1.0

skyla @sad "That are less likely to end up with me unconscious in an alleyway."

pause 1.0

skyla @sadbrow smirkmouth "I should... probably thank you for what you did, by the way."
skyla @closedbrow talking2mouth "I wasn't really thinking, and if I'd gone into that alley alone, and had to face down all those thugs by myself, well... I don't know what would've happened."

red @happy "Oh, nothing {i}too{/i} bad, I'm sure. They're not really scary, just kinda... lost and bored."
red @talkingmouth "Besides, their boss is a good person."

skyla @surprised "Oh! Yeah, that reminds me! How do you know those people? How do you know whoever their boss is?"
skyla @closedbrow talking2mouth "Were you secretly part of their evil team? But then you broke away, blowing up their base as you left, but not before stealing a powerful piece of forbidden technology?"

red @talking2mouth "Yes, that's it exactly. Nailed it."

skyla @happy "Yessss. Knew it!"

red @surprised "Wait, you, uh... sorry, I should've made clear I was joking. Yeah, that's not actually the case."

skyla @sad "Aw. But that was fun."

show skyla surprisedbrow frownmouth with dis

red @talkingmouth "Sorry to disappoint. One of those thugs stole the hat of a friend of mine. I ran after him, chased them to their hideout, and then met their boss."

pause 1.0

show skyla angry with dis

pause 1.0

skyla @talkingmouth "Oh, but when {i}I{/i} do it, suddenly you're all 'vigilantism is bad' this and 'with great power comes great responsibility' that!"

red @confused "I can guarantee I never said that second one."

skyla -angry @closedbrow talkingmouth "Well... I remember you saying that."

red @sadbrow talkingmouth "Will you at least promise me that you won't try to fist fight an entire gang before we have time to figure out alternate, {i}safer{/i} ways of handling your hero complex?"

if (not IsBefore(1, 5, 2004)):
    red @sad2eyes talking2mouth "Personally, I'd think being part of the Disciplinary Committee would be enough, but if not, then..."

skyla @angrybrow talkingmouth "God, fine. But you're being a total buzzkill."

red @closedbrow talking2mouth "If that's the price I have to pay to not have you {i}literally be killed,{/i} then that's what I'll do."

pause 1.0

skyla @smirkmouth "Hey. It just occurred to me. Every superhero has a {color=#0048ff}sidekick{/color}, right?"

red @talking2mouth "With the greatest amount of respect--I will not be your sidekick."

skyla @sad "Aw..."

red @closedbrow talking2mouth "Maybe later. How about, for now... I be your wingman?"

skyla @happy "Alright! I'll take it! That can even be your codename--{color=#0048ff}Wingman!{/color}"

$ RelationshipRankUp("Skyla", "Wingman", 1)

scene blank2 with Dissolve(2.0)

pause 2.0

narrator "Later, back in your dorm, you discover a letter pushed underneath your door."

Character("{color=#686080}???{/color}") "Thanks for handling that. She's tried to 'vanquish' my guys a couple of times. It's getting {s}fucking{/s} {s}goddamn{/s} {s}really{/s} annoying. Keep her out of my hair, and you'll be rewarded.{w=1.0} -S"

$ ValueChange("Silver", 3, -0.5)

narrator "You gained three points with Silver!"

return