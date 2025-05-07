label Blue1:

if (not IsBefore(1, 5, 2004)):
    $ persondex["Blue"]["Events"].append("Level2SceneVer2")

scene fields2
show clouds behind fields2:
    yalign 0.75
    ease 5.0 yalign 0.5
with Dissolve(2.0)

narrator "You are heading out to the fields to train, when, suddenly, you see a spiky brown bush over the nearest hill. Approaching closer, you recognize the person attached to the bottom of it."

show screen songsplash("A Rival Appears!", "Zame")
queue music "audio/music/rivalchill_start.ogg" noloop
queue music "audio/music/rivalchill_loop.ogg"

show blue with dis:
    xpos 0.5 zoom 0.8 ypos 1.2

pause 1.0

redmind @thinking "Ah, great. Maybe I can try to just turn around and..."

pause 1.0

if (IsBefore(1, 5, 2004)):
    redmind @thinking "Actually... maybe I should talk to [blue_name] for a bit? I know I definitely can't convince him to lay off me, but maybe I can at least try to see where he's coming from."
else:
    redmind @thinking "Actually... maybe I should talk to [blue_name] for a bit? ...I don't like him, but since we're roommates now, I could try a bit harder to get along with him."
    redmind @closedbrow frownmouth "And... I guess I {i}kinda{/i} owe him for delaying the first Quarter Qlash round..."

pause 0.5

red @closedbrow talking2mouth "Well, here goes nothing."

show blue:
    xpos 0.5
    ease 0.5 ypos 1.0 zoom 1.0

red @happy "Hey, Blue!"

blue @talkingmouth "Oh, it's you.{w=0.5}{nw}" 
extend frownmouth @angry " What do you want?"

red @talkingmouth "A thousand dollars would be a good start."

blue @closedbrow talking2mouth "You've had enough damn handouts."

pause 1.0

stop music fadeout 1.5
show screen songsplash("Pallet Town", "Zame")
$ renpy.music.queue("Audio/Music/palletpiano.ogg", channel='music', loop=True, tight=None)

red @confused "What do you mean?"

blue @angry "What do you mean, 'what do I mean?'! Don't play dumb."

red @confused "Believe me, I'm not playing."

blue @closedbrow talkingmouth "{i}Tch.{/i} You only got into this school because Gramps wanted you. It's the only thing that makes sense. I know you didn't have the grades, or the battling ability, to get in any other way."

redmind @thinking "He's... not exactly wrong."

blue @talkingmouth "Then you got put in the homeroom class of the teacher that bent the rules to get you in here in the first place. And you got {i}exactly{/i} the starter you wanted."

blue @angry "Then the damn Battle Team tryouts were rigged in your favor! Everyone just {i}gives{/i} you things! You haven't earned a single thing in your life!"

if (IsBefore(1, 5, 2004)):
    redmind @thinking "He's not exactly wrong, because of Frienergy... but I can't tell him that..."

else:
    red @angrybrow talking2mouth "You know that's not my fault. It's Frienergy. I only learned about it recently."

    blue @closedbrow talkingmouth "Yeah, but you didn't go out of your way to let everyone know after you learned about it, did you?"

    blue @angry "You were perfectly happy just sitting back and picking up {i}all{/i} the unearned benefits."

red @confused "Well, what do you want me to do, when someone wants to give me something? Just turn them down? Say no?"

pause 1.0

blue @talkingmouth "Uh, yeah."

pause 1.0

blue @surprised "What, did you not realize you could do that?"

red @closedbrow talking2mouth "I'm not going to turn down other people's kindness just to make you feel like your situation is more 'fair.'"

blue @closedbrow talkingmouth "'Course you're not. Because you don't give a damn about what's fair or not, do you?"

red @talkingmouth "Blue, we're equal. I don't think I'm better than you."

pause 1.0

blue @angry "Don't you {i}dare{/i} say we're equal. I {i}train{/i} harder. I {i}study{/i} harder. I {i}battle{/i} harder. You just coast along on other losers' handouts, and that means that I'm {i}better{/i} than you."

red @closedbrow talking2mouth "...Sigh. That's not true, [blue_name], but whatever."

if (IsBefore(30, 4, 2004)):
    blue @angry "And that's another thing! That goddamn nickname! My name is {b}Blue{/b}! {b}Blue Oak{/b}! Emphasis on the Blue, de-emphasize the Oak!"

    blue @angry "You ruined any possibility I had of having friends in Pallet Town, with everyone calling me [blue_name] all the time! Because {i}of course{/i}, they would 'follow the leader,' and just copy whatever you were doing!"

else:
    blue @angry "That's another thing that's been bugging me! That goddamn nickname you called me! I can't believe you brought it back up here... My name is {b}Blue{/b}! {b}Blue Oak{/b}! Emphasis on the Blue, de-emphasize the Oak!"

    blue @angry "You ruined any possibility I had of having friends in Pallet Town, with everyone calling me [oldblue_name] all the time! Because {i}of course{/i}, they would 'follow the leader,' and just copy whatever you were doing!"
    
red @talking2mouth "{i}I{/i} ruined your friends? You ruined mine! I went four years in High School without anyone even wanting to {i}look{/i} at me!"

blue @angry "Yeah, and I thought maybe you would've learned your lesson, then!"

pause 1.0

show blue surprisedbrow frownmouth with vpunch

red @angry "What fucking lesson?!"

show blue -surprisedbrow -frownmouth -surprised with dis

pause 1.0

blue @angry "...That you can't push me around forever."

red @talking2mouth "Oh my god, this is ridiculous. {i}I{/i} was not the bully. {i}I{/i} did not push you around!"

blue @talkingmouth "Oh, yeah? Well, whenever I was trying to get Gramps' attention, who was always there to get in my way?"

red @angrybrow talking2mouth "He was, like, the only adult in Pallet Town I knew personally! I was a literal child--it was {i}his{/i} responsibility to make sure he was paying attention to you!"

blue -frownmouth @happy "Hah! So you admit that Gramps ignored me!"

red @talking2mouth "Yes, of course he did, and that was super-unfair.{w=0.5}{nw}"

show blue sadbrow frownmouth with dis

extend @closedbrow talking2mouth " But that {i}wasn't{/i} my fault, and we're both adults now, so we need to just get over it."

blue -sadbrow @angry "Oh, sure, you want me to just {i}forget{/i} the years of being shoved into the shadows while everyone sucks your dick." 
blue @closedbrow talkingmouth "Yeah, no, I don't think I'm going to be 'getting over that' anytime soon. Why don't you 'get over' losing all your friends and blaming me for it, huh?"

pause 0.5

red @closedbrow talking2mouth "Ugh. This is a waste of time."
red @confused "What are you even doing out here?"

blue -frownmouth @talkingmouth "What do you think? Picking daisies? I'm training, obviously."

red @closedbrow talking2mouth "...Aren't the Pokémon here at way too low a level for you?"

blue @closedbrow happymouth "It's typical you'd say something like that. I'm doused in Max Repel right now. You know what that means? Only the strongest Pokémon make their way out here! Pokémon at {i}my{/i} level!"

narrator "You give a quick sniff. The air {i}does{/i} smell vaguely of Haxorus Body Spray. [pika_name], on your shoulder, is holding his nose with two paws."

red @talkingmouth "Yeah. Okay. I guess that makes sense."

pause 1.0

red @talkingmouth "I guess the only reason you don't already have a level 100 Pidgeot is because you couldn't get Max Repels back in Pallet Town."

blue frownmouth @closedbrow angrymouth "Kuh. I could've had them delivered, if I had any pocket money. But Gramps didn't give Sis and I an allowance, and he only barely remembered holidays, when I at least had an excuse to ask him for money."
blue @angry "And unlike {i}you{/i}, I have some goddamn pride, so I wasn't about to beg Daisy for money from her job in Viridian."

pause 1.0

blue @angry "You know Sis and I were snowed in one day? We {i}literally{/i} couldn't get out the front door. We had barely any food in the house, the phone lines weren't working, we didn't have mobiles." 
blue @angry "Gramps was still in his damn lab, working through the night."

red @talking2mouth "Yeah. I {i}do{/i} remember that."

blue @talkingmouth "You remember when it was, too?"

red @talkingmouth "...Snowfall Day, right? December 25th?"

pause 1.0

blue @closedbrow talkingmouth "Well, at least you remember that. Yeah, Snowfall Day. While every other kid was opening presents, or roasting chestnuts on the fire, Daisy and I were shivering in our house, starving, trying not to freeze to death."

pause 1.0

red @talkingmouth "...Do you remember what happened around noon, though?"

pause 1.0

blue closedbrow @talkingmouth "Tch."

red @talkingmouth "[pika_name] and I finally dug through the pile of snow until we got to your window."

blue -closedbrow @talkingmouth "You scratched the glass."

red @talkingmouth "We opened the window and came into your house. I brought out a bag of chestnuts. Then [pika_name] used his electricity to start a fire, and we all had an awesome Snowfall Day."

pause 1.0

blue @talkingmouth "Yeah, well--"

red @angrybrow talking2mouth "What happened? We were friends then, [blue_name]."

blue @angry "{i}Were we?{/i}"

if (IsBefore(1, 5, 2004)):
    red @surprised "Wha-what? What do you mean?"

    pause 1.0

    blue @closedbrow talkingmouth "Whatever. If you're too slow to figure it out, I'm not going to explain it for you."

else:
    red @talkingmouth "Yes. Blue, Frienergy aside, we {i}were{/i} friends. Always."

    blue @closedbrow talkingmouth "Tch. Easy for you to say."

pause 1.0

blue @talkingmouth "Whatever. I'm busy. If you aren't here to help me out, then you can just get lost."

red @confused "Help you out?"

blue @closedbrow talkingmouth "{i}Train{/i}, dumbass."
blue @talkingmouth "You're a loser, but at least you know how to battle."

red @angrybrow talking2mouth "Thanks for the show of support."

blue @angry "Well? Are we training or not?"

red @talkingmouth "Just be straight with me. When you're asking me to train, like this, you realize you're asking me to stick around, right?"
red @happy "You're asking me to {i}spend time{/i} with you. You're aware of that, right?"

blue @happy "Psh. You wish."
blue @closedbrow talkingmouth "I'm {i}offering{/i} my time to you, because it'd be seriously pathetic to have my rival be lagging so far behind me all the time."

red @closedbrow talking2mouth "Yeah. Okay. Whatever. Let's do it."

call clearscreens from _call_clearscreens_72
show black 
with Dissolve(2.0)

pause 0.5

narrator "You and Blue train intensely for a couple hours."

pause 0.5

python:
    for mon in playerparty:
        mon.GainExperience(math.floor(pow(AimLevel(), 3) / 25 / 2))

show screen currentdate
hide black
show blue happy
with Dissolve(1.0)

$ speciesname = "Pidgeotto"

blue @talkingmouth "Hah! Did you see that? My Pidgeotto totally rocks!"

redmind @sweat frownmouth "Damn... we were both training pretty much the same way, but I can tell that [blue_name]'s Pokémon pulled way ahead."

red @sweat talkingmouth "Well, it's no surprise, you've been training that Pidgey ever since we were kids."

pause 1.0

show blue -happy frownmouth with dis

pause 1.0

red @sweat confused "What?"

blue @closedbrow talkingmouth "Do you remember when we got our starters?"

red @happy "Yeah! And I got [pika_name], and he--"

blue @talkingmouth "That's when I realized that life wasn't fair. That's when I realized that I had to fight harder than {i}anyone{/i} else to get what I deserved."

red @confused "Huh? What do you mean?"

blue @talkingmouth "What, you've really never put two and two together? God, you really {i}are{/i} slow."

red @confused "Enlighten me, oh wise one, oh fount of knowledge."

if (IsBefore(1, 5, 2004)):
    blue @closedbrow talkingmouth "Tch. Listen up, blockhead. My grandpa gave {i}you{/i} a Pikachu, which is a rare Electric-type that can only be captured in Viridian Forest."

    blue @angry "And he gave {i}me{/i} a Pidgey, which is a dirt-common Flying-type you can catch by taking a couple steps outside the Pallet fence."

    pause 1.0

    red @sad "{w=0.5}.{w=0.5}.{w=0.5}.Oh."

    pause 1.0

    blue @talkingmouth "You think you're making some kind of statement by using your Pikachu in the Battle Team, because Pikachu's so weak, or whatever."
    blue @angry "I'd be {i}lucky{/i} to have a Pikachu."

else:
    blue @closedbrow talkingmouth "Tch. Listen up, blockhead. My grandpa gave {i}you{/i} a Pikachu, which is a rare Electric-type that can only be captured in Viridian Forest."

    blue @angry "And he gave {i}me{/i} a Pidgey, which is a dirt-common Flying-type you can catch by taking a couple steps outside the Pallet fence."

    pause 1.0

    red @sad "{w=0.5}.{w=0.5}.{w=0.5}.Oh."

    pause 1.0

    blue @talkingmouth "Even ignoring the weird form your Pikachu's got, you always had the advantage. You thought you were making some sort of statement by using a Pikachu on the Battle Team?"
    blue @angry "I'd be {i}lucky{/i} to have a Pikachu."

pause 1.0

red @closedbrow talking2mouth "...I mean, I'm sorry, man, I--"

show blue surprisedbrow frownmouth with dis

blue @talkingmouth "What?"

red @confused "Huh? I just... I just said I was sorry. About... well, about how your grandpa treats you."

redmind @thinking "Regardless of how much he brought it onto himself, Professor Oak had a responsibility to be the adult in the room."

blue -surprisedbrow -frownmouth -surprised frownmouth angrybrow @angrymouth "Don't say that. Don't apologize for other people, dumbass!"

red @confused "Wha- okay? Fine, I take it back."

blue @closedbrow talkingmouth "Gramps has a lot to apologize for. You do too. But neither of you are getting off by apologizing for what someone else did."

red @confusedeyebrows frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
red @closedbrow talking2mouth "Okay. This is going to be dumb. But what do I have to apologize for?"

blue @talkingmouth "You can start by apologizing for coming up with that dumbass nickname, and bringing it back up at Kobukan."

red @confusedeyebrows talkingmouth "...You know what? Alright. Fine. I'll do that."

blue @angry "Yeah, I knew you wouldn't--"
blue surprisedbrow frownmouth @surprised "Wait, what?"

red @talkingmouth "I'm sorry for calling you names when I was, like, seven. And I'm sorry for bringing it back up here. That was childish."

pause 1.0

blue -surprisedbrow -frownmouth -surprised @angry "You don't mean that."

red @angry "Oh my god, Blue! Why are you so stubborn?! You're determined to never be happy!"

blue frownmouth @angry "It's not {i}my{/i} fault that everyone who {i}should{/i} be on my side thinks kicking me down is the greatest thing since sliced bread!"

red @surprised "WHAT?!"

blue @angry "My own grandpa! My {i}only{/i} living adult relative! Spent more time in his lab than he did with you, and more time with you than he did with me!"
blue @angry "Daisy had to get a job at fourteen just to support us! Passing out free Potion samples to random people who walked in and out of town!"
blue @angry "And then my so-called 'Best Friend' decided that gathering the world's biggest friend group was more important than seeing if I was doing okay!"

red @talking2mouth "Blue, {i}I was fourteen!{/i}"
red @angry "I had no way of knowing if you were doing okay unless you told me! And you just got angry! If you weren't terrified of showing even a tiny bit of vulnerability to your friend, then maybe I {i}could've{/i} helped you!"

pause 1.0

blue @closedbrow talkingmouth "Whatever. I've wasted enough time here."

pause 1.0

red @talking2mouth "Blue."

blue @surprised "What?"

red @sadbrow talkingmouth "Do you want to be friends again? We can make it happen. It's that easy."

blue @talkingmouth "Oh, shove off."

hide blue with Dissolve(1.0)

pause 1.0

redmind @thinking "...I can tell he's hurt. And he {i}does{/i} want to be friends again. But he's not willing to open the door even a centimeter."
redmind @sadbrow frownmouth "...I've done everything I can, right? I mean, all that stuff he's blaming me for... none of it was {i}really{/i} my fault, right?"

show blue frownmouth with Dissolve(2.0)

red @confused "Blue?"

if (IsBefore(1, 5, 2004)):
    blue @closedbrow talkingmouth "You're a second-rate trainer. And I'll never be caught dead being friends with you ever again. But we can hang out."
else:
    blue @closedbrow talkingmouth "You're a second-rate trainer. And I'll never be caught dead being friends with you ever again. But since we're roommates, I can probably learn to {i}tolerate{/i} you."

red @confused "Hm?"

blue @talkingmouth "I was serious when I said I'd miss my favorite stooge while I was taking my place amongst the champions of the world. If you have even one skill, it's that you're a good [bluecolor]listener{/color}."

red @closedbrow talking2mouth "And god knows you like to talk."

blue @angry "And for {i}some{/i} reason, when I tell people I'm the best trainer in Kobukan, no-one takes me seriously." 

if (IsBefore(1, 5, 2004)):
    blue @angry "You and Janine might be the only people in this whole school who actually get it, and for you it's just because I keep beating your ass."
else:
    blue @angry "Our roommates and Janine might be the only people in this whole school who actually get it, and for you it's just because I keep beating your ass."

red @closedbrow talking2mouth "I'm honored."

blue @talkingmouth "So. Yeah. If you want to just hang around me, and listen to me talk about how great I am, then I won't kick you away. Maybe you'll actually learn something."

hide blue with dis

pause 1.0

red @closedbrow talking2mouth "Maybe I will."

$ RelationshipRankUp("Blue", "Listener", 1)
$ persondex["Blue"]["Nature"] = TrainerNature.Moody

if (usingmoods):
    narrator "Blue's Nature shifts from {color=#0048ff}Distant{/color} to {color=#0048ff}Moody{/color}!"

return