label secondhomeroom010426:

if (pikachuobj in playerparty):
    $ playerparty.remove(pikachuobj)

scene blank2

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom behind blank2

show oakbg behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade

oak @talkingmouth "How has your Monday been, ladies and gentlemen?" 
oak @talkingmouth "I hope you've been thinking about this upcoming quiz! After last Thursday's one-versus-three affair, we're going back to basics." 
oak @talkingmouth "Though it {i}should{/i} be noted that this is the first battle that will make use of held items!"
oak @talkingmouth "{color=#0048ff}As such, your opponent will be equipped with one 'Oran Berry,' which restores 10 HP to a Pokémon in distress.{/color} Do keep this in mind."

pause 0.5

oak @talkingmouth "Now, take out your pencils! [bluecolor]Remember, this is graded!{/color}"

$ trainer1 = Trainer("red", TrainerType.Player, [Pokemon("Munchlax", level=12, moves=[GetMove("Covet"), GetMove("Body Slam"), GetMove("Belch"), GetMove("Metronome")])])
$ trainer2 = Trainer("oak", TrainerType.Enemy, [Pokemon("Petilil", level=10, moves=[GetMove("Synthesis")], ability="Own Tempo", item="Oran Berry")])

$ trainer1.GetTeam()[0].ApplyStatus("burned")
$ trainer1.GetTeam()[0].Health = 1
$ trainer1.GetTeam()[0].ChangeStats(Stats.Accuracy, 1)

call Battle([trainer1, trainer2], gainexp=False, healParty=False, clearstats=False, uniforms=[True, False], lockbag=True, lockluck=True) from _call_Battle_64
$ battlehistory["Oak6"] = _return

$ renpy.transition(dissolve)
show screen currentdate

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

if (WonBattle("Oak6")):
    if (trainer1.GetTeam()[0].GetMoves()[3].PP != trainer1.GetTeam()[0].GetMoves()[3].MaxPP):
        redmind @thinking "I'm almost certain that using Metronome was {i}not{/i} the intended answer."
    else:
        redmind uniform @happy "...That might have been the grossest possible solution to that fight. Steal a berry, eat it in front of the foe, then burp it up into their face?"
        redmind @thonk "Pokémon morality is weird."
else:
    red uniform @sad "Uh-oh. I don't have a good feeling about this one."

    if (trainer1.GetTeam()[0].GetMoves()[3].PP != trainer1.GetTeam()[0].GetMoves()[3].MaxPP):
        red @closedbrow talking2mouth "I probably shouldn't have used Metronome..."

oak @talkingmouth ".{w=0.5}.{w=0.5}.{w=0.5}"

pause 0.5

oak @talkingmouth "At a glance..."

pause 0.5

if (WonBattle("Oak6")):
    oak "It looks like everyone did quite well."
else:
    oak "There were a few mistakes. It's important to remember that many items can be used at different points in the battle."
    oak "For example, the Oran Berry can be used directly by a trainer, or can be used automatically anytime the holding Pokémon takes damage that brings them to beneath 50%% of their health."
    oak "Additionally, any time an item switches hands, if the item can be used, the item {i}will{/i} be."

oak @talkingmouth "Item usage is an important facet of battles. Study their effects, and when it's most advantageous to use them!"
oak @talkingmouth "Not only could this save your victory in a battle, it could save your wallet!"

redmind @thinking "Well, that's definitely relevant."

if (punkwins > 0):
    redmind @thinking "Right now, my primary income is beating up criminals in a dark alleyway. I need to save every penny I can get."

if (investment == 0):
    redmind @thinking "Maybe I should visit Gardenia. Although I'm nervous about spending money on {i}anything{/i}, nevermind a shifty-sounding deal like that, it's just burning a hole in my pocket right now."

$ PlaySound("BellChime.ogg")

pause 2.0

oak @talkingmouth "Well, that seems to be the end of our class, then. Have a nice rest of your day! And make sure to brush up on item usage. It will be relevant for your next quiz, I promise."

hide oakbg with dis

redmind uniform @thinking "Alright. I've got the Battle Team meeting soon. I've just gotta track down the Student Council first."

pause 0.5

red @closedbrow talking2mouth "...So. Where would I be, if I was a Student Council?"

show leaf uniform at rightside with dis

pause 1.0

leaf @talking2mouth "Standing around in a classroom, talking to yourself?"

red @closedbrow talking2mouth "Hm... no, that doesn't sound like me."

leaf @happy "Hey, [first_name]! It's been ages since we've done something together. Want to go to the battle hall and pound out a couple of battles before the meeting?"

red @talkingmouth "Sorry, nah. I'm on a mission from Calem."

leaf @surprised "Oh? What about?"

red @closedbrow talking2mouth "I need to track down the old Student Council. A bunch of us Student Council guys are trying to put together a meeting before the elections."

leaf frownmouth @sad "Ugh. That sounds... dull."

red @confusedeyebrows frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

leaf -frownmouth @sadbrow happymouth "Er... sorry, that was rude, wasn't it? It's just... I'm so surprised whenever I hear that you're, like, actually into this Student Council stuff. It really doesn't seem like you."
leaf @closedbrow talkingmouth "Or... maybe it totally {i}is{/i} you, and I just don't know you as much as I thought I did?"

menu:
    "{color=#e226a6}[[Patience]{/color} No, you're right.":

        $ TraitChange("Patience")

        leaf @happy "Oh, for real? Phew. I was wondering if I'd totally misjudged you."

    "{color=#66b77d}[[Knowledge]{/color} It wasn't me before, but it is now.":

        $ TraitChange("Knowledge")

        leaf @closedbrow talkingmouth "Oh, okay. I get it. I guess you're, like, still getting used to this, huh?"

red @talkingmouth "I definitely didn't come into this school thinking 'I want to be part of the Student Council,' like I did with the Battle Team."
red @happy "But with everyone pushing me into it... well, I'm at least going to do my best."

pause 0.5

red @sweat happy "...Of course, I might not even get elected. So I'm not counting my chickens with their heads cut off."

leaf @closedbrow talkingmouth "I'm pretty sure that's not how the phrase goes."

red @talkingmouth "Noted. But I gotta go now. We don't have a whole bunch of time before the Battle Team meeting. Want to come with me?"

leaf @flirttalk "Well, aren't you forward?"

red @confused "Ha."

leaf @happy "Yeah, sure, let's go."

show leaf:
    xpos 0.75
    ease 0.5 xpos 0.5 ypos 1.2 zoom 1.3

pause 1.0

red @surprisedeyebrows talkingmouth "Huh."

leaf blush @angrysmilemouth "What?"

red @happy "Nothing. Just didn't expect you to grab my hand like that."

leaf @closedbrow talking2mouth "Yeah, well... I did. Do you have a problem with it?"

red @happy "Nah. It's just kinda cute how you were trying to make it seem so casual, {w=0.5}{nw}"

show leaf surprisedbrow frownmouth:
    ease 0.5 xpos 0.6 ypos 1.0 zoom 1.0

extend @talkingmouth "and, uh, failed totally at it."

leaf -blush angrysmilemouth angrybrow bigblush "H-hey! When a girl tries to casually grab your hand, you don't point out whether or not they succeed in doing it casually."

red @closedbrow talking2mouth "I mean, have you tried counting shoulders? That one always works."
red @happy "Or maybe you could say there's some mud on my hand, and try to wipe it off! That one's a classic."

leaf "{w=0.5}.{w=0.5}.{w=0.5}."
leaf @closedbrow talkingmouth "Okay. Newsflash, buster. I'm trying to be serious here. And...{w=0.5} um...{w=0.5}"
leaf embarrassed "I guess if I was trying to be serious, I shouldn't've started that sentence with 'newsflash, buster.'"

pause 1.0

leaf blush -embarrassed -bigblush @happy "Okay, okay, okay! New plan. I'm not doing this now. I'd rather jump in a lake than do this now. So, yeah, uh, let's just pretend the last five minutes didn't happen, please?"

red @confusedeyebrows happymouth "Aw. And here I thought I was getting somewhere."

leaf @closedbrow talkingmouth "Sorry, Skippy. You might be the second-best on the Battle Team, and kind and fit and hilarious, but I guess that {i}just isn't enough{/i} for me."

red @confused "{i}Second{/i}-best?"

leaf @sarcastic "Uh, yeah, I'm there."

red @happy "Oh, of course, my mistake. But it kinda sounds like you've got some pretty unrealistic standards."

leaf @talkingmouth "Please. I can afford to have any standards I want.{w=0.5}{nw}" 
extend  -blush @happy " Have you seen me? I'm a catch."

red @confused "{size=30}So is a Magikarp.{/size}"

red @closedbrow talking2mouth "Anyway, what, then, would be enough for your standards? Maybe if I was a rocket scientist?"

leaf @closedbrow talkingmouth "Nah, that don't impress me much."

leaf @happy "How about you get onto the Student Council? Then, {i}just maybe{/i} then, I'd feel like I can hang out with you without ruining my reputation."

red @confused "Well, at least you're not picky."

leaf @happy "Hah, hah! Come on, [first_name]! We gotta find that Student Council, right?"

show leaf blush with dis:
    xpos 0.6
    ease 0.5 xpos 0.5 ypos 1.2 zoom 1.3

leaf @talkingmouth "C'mon, you dork. Let's go."

scene hall_B with splitfade

pause 0.5

show sonia with dis

pause 0.5

leaf uniform @surprised "Oh, Sonia! I bet she can help us find them."

red uniform @closedbrow talking2mouth "Huh?"

show sonia:
    xpos 0.5
    ease 0.5 xpos 0.25 xzoom -1

show leaf uniform with dis:
    xpos 0.5 zoom 1.3 ypos 1.2
    ease 0.5 xpos 0.75 zoom 1.0 ypos 1.0

leaf @talking2mouth "Hey, Sonia."

sonia @talking2mouth "Oh, hi there, you two. Were you after me, then?"

red @confused "Apparently?"

leaf @talkingmouth "Yeah, we wanted to rely on your expertise, as our Senior."

sonia @surprised "I'm not sure if my experience will be of any use, really, but I'll give it my best shot."

leaf @talking2mouth "Well, we're trying to find the Student Council. [first_name] is going to tell them to clear out their offices."

red @happy "That's not {i}exactly{/i} what I'm doing."

leaf @closedbrow talkingmouth "Thing is, though, we're not really sure where they are. We don't know if there's, like a club room or meeting place or something."

sonia @closedbrow talkingmouth "Oh, so because I was here last year, you reckon I know where they might be? Right, I see..."

sonia @sad "I was never very involved in the Student Council. Seemed like a lot of fuss without a lot of yield.{w=0.5}{nw}" 
extend @talkingmouth " But I distinctly remember them meeting in Relic Hall's lobby after school every day."

red @talkingmouth "Really? Relic Hall's lobby? Alright, I know the way there, no problem."

leaf @flirttalk "You sure about that, navigator?"

red @happy "I got lost {i}one{/i} time! {i}Once!{/i} In a brand-new school that's practically larger than my entire hometown!"

sonia @happymouth "I must admit, I was a tad overwhelmed the first time I came to Kobukan, too."
sonia @sadbrow happymouth "I'm from Wedgehurst, in Galar, and I must say, cities have always had a way of spinning me around."
sonia @closedbrow talkingmouth "I've been to Hammerlocke a couple of times, and just looking up at the castle's ramparts gave me vertigo something awful."

leaf @talking2mouth "...Hey, Sonia. Mind if I ask you a question?"

sonia @surprisedbrow happymouth "{i}Another{/i} one, you mean. But of course, go off."

leaf @talking2mouth "I don't mean to pry, but from what we heard from Janine, it sounds like you were in the Battle Team last year, but you just quit. Not just the Battle Team, but the school itself."

pause 0.5

sonia @sadmouth "Right."

leaf @talking2mouth "...Um. Why?"

show leaf frownmouth with dis

sonia @talking2mouth "...If you don't mind, I'd rather keep a lid on that for now."
sonia @sadbrow happymouth "I know we're Battle Team teammates, but there are a few things I'd rather keep close to my chest. At least for a while."
sonia @closedbrow talkingmouth "Last year... {w=0.5}isn't exactly something I'm proud of."

leaf @sadbrow happymouth "Oh, yeah, of course. I get it. {w=0.5}Um. {w=0.5}Sorry."

sonia @happy "That's quite alright. Glad I could help you with your other tidbit."

leaf -frownmouth @talking2mouth "Thank you."

red @closedbrow talking2mouth "Anything we can do for you?"

sonia @happy "Well... if you have the money, and need some research work done, I'm a deft hand at that. My specialties are astrobiology and Galarian myth-history."

redmind @thinking "Yeah, I, uh, I'm definitely not going to have the money for that."

leaf @happy "We'll keep it in mind."

sonia @talking2mouth "Good luck, you two!"

hide sonia with dis

pause 0.5

red @closedbrow talking2mouth "Alright, the Relic Hall lobby, right?"
red @talkingmouth "Follow me. Up for a jog?"

leaf @sarcastic "I will literally sweat out {i}everything{/i} if I do that."

red @surprised "Oh, that's not good. You gotta remember to stay hydrated!"

leaf @talking2mouth "I do. By not running."

red @closedbrow talking2mouth "Huh. I mean, I just drink a ton of water to replenish, but I guess we all have different strategies."

leaf @talkingmouth "...I'll speedwalk with you."

red @happy "Sure, that's close enough!"

pause 0.5

show lounge with splitfade

pause 0.5

show brawly at leftside 
show falkner at rightside
show roxanne
with dis

pause 0.5

brawly @happy "[first_name] Gonzalez! Fastest Student Council hopeful in the west. How are you doing?"

red @happy "Pretty good, Brawly."

falkner @closedbrow talking2mouth "Oh... I think I remember you. Yes, I believe I do. Dorm 151, and you wished to be separated from Blue Oak."

red @closedbrow talking2mouth "Yeah, that didn't work out great. At least I don't have to dorm with him."

roxanne @talkingmouth "Well, [first_name] [last_name], what can we do for you?"

red @closedbrow talking2mouth "Calem's organizing a meeting of the Student Council hopefuls tomorrow morning, in the cafeteria. He's hoping we can all compare our positions, align our goals, then come up with a united campaign to get people to vote."

roxanne @closedbrow frownmouth "A nice goal. I tried something similar last year. But what part do we play in this?"

red @talkingmouth "Calem was hoping you could come to the meeting, and hear our thoughts. If you like what we're saying, then maybe you'd give us your endorsement. Calem thinks that would mean a lot to the current students."

brawly @happy "Sure, why not?"

falkner @talkingmouth "It's an interesting idea. I don't object."

roxanne @closedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
roxanne @sadbrow talking2mouth "Hm. I am Student Council president for only four more days, but I want to be sure that I'm leaving my school in good hands."
roxanne @surprisedbrow talking2mouth "You've been talking quite a bit about 'Calem'. He's the one who has planned everything so far."

red @talkingmouth "Well, he planned {i}this,{/i} yeah."

roxanne @closedbrow frownmouth "He's not running on a single issue, like Jasmine and Grusha are."
roxanne @angrybrow frownmouth "He's not overtly controversial, like Cheren is."
roxanne @closedbrow talkingmouth "It seems to me that he would be the best pick for Student Council President."

red @closedbrow talking2mouth "What about Serena?"

falkner @closedbrow talking2mouth "She is a valid option, but in all Serena and Calem's public engagements, it has been Serena standing at Calem's side. He is a better public speaker."
falkner @sad "Likely better able to weather the thrown stones that inevitably follow election, too."

brawly @happy "Hah, yeah. There's a {w=0.5}{i}lot{/i} of those."

red @talkingmouth "Well, why are you talking about the presidency? Don't the council members who get elected decide amongst themselves who the President is?"

roxanne @talkingmouth "That is the case."

falkner @angrybrow talking2mouth "If Cheren is elected President of your Student Council, you will be powerless."
falkner @closedbrow angrymouth "He will demand radical, sweeping, structural changes immediately after election. This will vaporize any goodwill the administration may have held to allow him to implement his smaller changes."

red @sad "What...?"

roxanne @sad "It's true, I'm afraid. My council had the same problem. After I was elected, I tried to implement voting holidays, re-implement a financial affirmative action program, and even tried to strip away the privileges of legacy admissions."
roxanne @sadbrow happymouth "I still fervently believe that these policies would make Kobukan more fair, but I was quite promptly shut down. And the administration has never {i}seriously{/i} listened to us since."

brawly @happy "If we had another year, hey, maybe we'd be able to do something. We know how to play the game now. But bein' in the council involves a lot more politicking than I think any of us were prepared for."

falkner @sad "I was telling Roxanne she needed to slow down before she was elected."
falkner @closedbrow talking2mouth "But, like Cassandra, those with the keenest eyes have the weakest grasp."

roxanne @closedbrow talking2mouth "Calem is subtle. He could make some of your policies happen. I'm sure of it."

pause 1.0

roxanne @angrybrow frownmouth "But Cheren will lead you into a brick wall. For the sake of your Student Council, he must revoke his claim to the Student Council's Presidency."

pause 1.0

red @confused "Is that a condition of your endorsement?"

roxanne @closedbrow teachingmouth "For him, yes. I don't imagine there will be any issues endorsing the rest of you." 
roxanne @talking2mouth "Jasmine and Grusha's focus {i}is{/i} quite narrow, but they seem sensible enough to pivot to new positions once their accessibility concerns are addressed."

pause 0.5

red @closedbrow talking2mouth "Damn. I'm not sure how to tell Cheren this myself."
red @sadbrow talking2mouth "Can you tell him at the meeting tomorrow?"

roxanne @talkingmouth "Yes. We'll arrive early, so we can have this conversation with him before you take over."

red @talkingmouth "Alright. Thank you."

pause 0.5

hide leaf

leaf uniform @surprised "Uh, wait! Sorry, I know I'm not really part of this conversation, but, um, I've got a question."

brawly @talkingmouth "Yeah? Shoot."

leaf @talking2mouth "What about [first_name]? Why couldn't he be a president candidate?"

pause 0.5

roxanne @sadbrow happymouth "Well... he could. But there's a certain level of charming innocence here that I think it'd be a dreadful shame to extinguish."
roxanne @sadbrow frownmouth "...As becoming president {i}most certainly{/i} would."
roxanne @sadbrow happymouth "Don't lock yourself into anything, [first_name]. It'd be a dreadful waste for a man with your options."

red @confused "Uh... thanks for looking out for me?"

roxanne @happy "That's my job. For a few more days, in any case."

hide roxanne with Dissolve(1.0)

pause 0.2

hide falkner with Dissolve(1.5)

pause 0.2

brawly @talkingmouth "...Well, I guess I'll see you tomorrow."

red @talkingmouth "Yeah, see ya."

hide brawly with Dissolve(1.0)

red @talkingmouth "Alright. Let's go get changed and meet up at the Battle Hall."

leaf frownmouth "{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}{nw}"
extend @talkingmouth "Yeah, of course."

call clearscreens from _call_clearscreens_76

scene blank2 with Dissolve(2.0)

pause 0.5

leaf uniform @closedbrow talkingmouth "...His options, huh?"

pause 0.5

leaf @closedbrow frownmouth "...If I want him to take me seriously, if I want him to see me as more than an option, maybe I need to take him more seriously."

scene stadium_empty
show screen currentdate
with Dissolve(2.0)

if (pikachuobj not in playerparty):
    $ AddPikachu()

$ HealParty()

pause 0.5

show janine with dis

stop music fadeout 1.5

janine @talking2mouth "Good, you're all here."
janine @closedbrow talking2mouth "We need to talk about--"

queue music "Audio/Music/fuchsia_start.ogg" noloop
queue music "audio/music/fuchsia_loop.ogg"

show screen songsplash("Fuchsia City", "Zame")

pause 0.5

janine @talking2mouth "Wait. One of you {i}is{/i} missing. Where's Erika?"

show stadium_empty:
    xalign 0.0 zoom 1.0
    ease 1.5 xalign 0.1 zoom 1.3
    pause 1.0
    ease 1.0 xalign 0.9
    pause 1.0
    ease 2.0 xalign 0.0 zoom 1.0

show janine:
    xalign 0.5 zoom 1.0
    ease 1.5 xalign 0.9 zoom 1.3 ypos 1.2
    pause 1.0
    ease 1.0 xalign 0.1
    pause 1.0
    ease 2.0 xalign 0.5 zoom 1.0 ypos 1.0

pause 5.0

red @talkingmouth "Well, {i}I{/i} don't see her."

janine @closedbrow talking2mouth "Unbelievable. Our second meeting, and the girl's late."

janine @angry "This isn't going to happen again. Understand? I have absolutely no tolerance for this kind of thing." 
janine @angry "We have less than a year to occupy the highest position of honor in the entire Kobukan region. If you think I'm going to let you slack off on that, then you don't understand what the Battle Team is. Now--"

$ PlaySound("GenericDoorOpen.ogg")

pause 0.5

show janine surprisedbrow

erika @happy "Ah, hello! Apologies for my lateness. I was just picking up some items I thought might be useful."

narrator "Erika walks into the room, wheeling a trolley full of strange headsets and fanny packs."

erika @talkingmouth "I hope this serves as an adequate apology for my tardiness, Miss Janine."

pause 0.5

janine -surprisedbrow @closedbrow talkingmouth "I don't want you thinking that you can buy your way into my good books."

erika @happy "I wouldn't dare."

pause 0.5

janine @happymouth "Alright. You're off the hook. Come up here and tell everyone what you've brought."

show janine:
    ease 0.5 xpos 0.25

show erika with dis:
    xpos 1.0 ypos 1.2 zoom 1.3
    ease 0.5 xpos 0.75 ypos 1.0 zoom 1.0

erika @talkingmouth "Hello, my fellow teammates!"

ethan @talkingmouth "Hey, Harlacher!"

erika surprisedbrow frownmouth @surprised "I... my name is Erika."

ethan @closedbrow talking2mouth "What, didn't I say that?"

pause 1.0

janine @talking2mouth "Erika, continue. Ethan, until you've sorted out your issues, just stay quiet."

ethan @surprised "Eh? ...Er, okay."

erika -surprisedbrow -frownmouth -surprised @talkingmouth "Well, right. I believe many of us have recently come into the possession of baby Pokémon hatched from the Springsday eggs, yes?"
erika @happy "It occurred to me that training them up might be quite a bother. It certainly would be for me. So I purchased a shipment of Silph Co.'s proprietary Experience Share equipment."
erika @happy "Of course, it would be poor form if I were to use the shipment only for myself, so I purchased enough for the entire Battle Team."

redmind @surprisedbrow frownmouth "Based on the size of that pile, I think she may have purchased enough for {i}last year's{/i} Battle Team."

erika @happy "Of course, many Pokémon body types are not well-suited for the shape of the Experience Share, so I've also purchased a shipment of Lumiosian Battle Bags. They're hand-woven by genuine Kalosian artisans!"

ethan @talkingmouth "Alert: A dumb question is incoming. Hey, uh, what's a 'battle bag?'"

leaf @talking2mouth "You know how, in battles, your Pokémon can hold berries, or wear Heavy-Duty Boots, or Rocky Helmets, or something?"

ethan @talkingmouth "Yeah, sure.{w=0.5}{nw}" 
extend @happy " I mean, some of 'em. I don't know how you'd put boots on a Hoppip."

janine @talking2mouth "That's exactly what Battle Bags are for. They're a multi-purpose item-holding equipment that can let pretty much any body type use any item they want."
janine @happy "Heh. There was a time before the Battle Bag was invented in Johto when people would choose Pokémon just because they were bipedal, and could use battle equipment properly."
janine @sad "Of course, there was a much wider variety of equipment before then. The battle bags kinda made equipment for differing body types obsolete."

red @closedbrow talking2mouth "Sounds like a win for accessibility, but a loss for small business, then."

hide erika with dis

show janine:
    ease 0.5 xpos 0.5

pause 1.0

narrator "Erika hands out an Experience Share and a Battle Bag to every Battle Team member."

dawn @happy "Oh, pink! That's my color. Thank you, Erika."

erika @talkingmouth "That's quite alright. I thought I sensed in you a fellow woman with an eye for fashion."

dawn @sadbrow happymouth "Oh... well... I wouldn't say that. I mean, it's not like I'm trying to stand out."

erika @surprised "Whyever not? I'm certain that if you tried, you could quite easily turn your battles into spectacle. Why, with that Altaria of yours, you remind me of the Hoenn Contest Champion."

dawn @sadbrow talkingmouth "Ah...{w=0.5} Um, I...{w=0.5} Er...{w=0.5} That's..."

janine @talking2mouth "Nope, that's enough. You get three chances to spit it out. If it takes four tries, we don't have time for it."

janine @angrybrow talking2mouth "Erika, does everyone have one?"

erika @happy "Almost!"

show erika with dis:
    xpos 0.9 ypos 1.0
    ease 0.5 xpos 0.75 ypos 1.2 zoom 1.3

erika @talkingmouth "Here you go, [first_name]. A little thanks for the confidence boost you gave me."

red @happy "Thanks!"

redmind @thinking "Now, here's a girl who could pay my tuition without even thinking about it."

pause 0.5

redmind @thinking "Hey, what the hell, [first_name]? Don't become someone's friend just to get at their money. That's messed up."

pause 0.5

redmind @thinking "Geez, the stress is getting to me..."

$ usinginventory = True
$ GetItem("Experience Share", text="Erika delicately places an Experience Share in your hands! Her touch lingers perhaps a moment too long.")

leaf @frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

show erika with dis:
    ease 0.5 xpos 1.0 ypos 1.0 zoom 1.0 alpha 0.0

janine @talking2mouth "You know how to use all these, right?"

hide erika

ethan @talkingmouth "[bluecolor]Yeah, just click the button on the bottom-right of the screen. And if I want to unequip an item from a Pokémon, I just got to click the item on their stats page, right?{/color}"

leaf @talking2mouth "Yeah, that's pretty much it."

sonia @surprisedbrow happymouth "That's what I did last year."

silver @surprisedbrow talking2mouth "{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}{nw}"
extend @surprisedbrow talkingmouth "Uh?"

pause 0.5

janine @talking2mouth "Equip those Experience Shares to your lowest-leveled Pokémon. If you don't, you're just wasting experience."

pause 0.5

janine @talking2mouth closedbrow "Speaking of experience."

janine @talking2mouth "What levels are all your Pokémon right now? They should be around level 12. By the end of Sunday, you should have a team of level 14s."

blue @happy "Hah! All my Pokémon are {i}way{/i} higher levels than that!"

janine @talking2mouth "Good job."

pause 0.5

blue @surprised "What?"

janine @talking2mouth "I said good job, Blue. I hate repeating myself."

blue @surprised "But-- you-- I didn't... what?"

leaf @talking2mouth "What's [blue_name] stuttering about?"

red @closedbrow talking2mouth "I think this might be the first person who's ever actually said 'good job' to him."
red @happy "Probably doesn't know how to handle it!"

leaf @sadbrow talking2mouth "...Right."

janine @talking2mouth "I'll keep you updated on what levels your team should be at any given moment. [bluecolor]If you ever want a reminder, visit me in your free time in the Battle Hall.{/color}"

dawn @talkingmouth "Um... if we're below that level, where should we train?"

janine @talking2mouth "Besides the battles you have in class, the wild is an option."

hilbert @closedbrow talkingmouth "The Pokémon in the wild are all far too weak for me to care about. My Pokémon learn nothing from defeating them."

janine @closedbrow talking2mouth "Right. The school's almost done securing the forest after that fire, so I think you should probably be able to go into the forest soon."
janine @talking2mouth "The Pokémon there tend to be a bit stronger than the ones you might find in the city. Until the forest opens up, though, your best option is just to get in whatever practice you can on-campus."

pause 0.5

janine @closedbrow talkingmouth "Speaking of. It's time we do some practice battles. Normally we'll do these every Friday, but I wanted to get a head start, since the first Quarter Qlash is soon."

bea @talkingmouth "You said you don't anticipate that we'll be matched up against anyone we cannot easily beat in the first Quarter Qlash."

janine @talking2mouth "That's right. I {i}don't{/i} anticipate that. Which is why we need to prepare for it."

red @surprisedeyebrows frownmouth "Intense."

janine @talking2mouth "Pair up. I want everyone to focus on training their Pokémon beneath level 12 right now."

janine @talking2mouth "[bluecolor]Battle Team training will always provide an extra boost to Pokémon beneath the recommended level.{/color}"

pause 0.5

bea @talkingmouth "Are you going to assign partners?"

janine @talking2mouth "No. You'll eventually learn who your best training partner is. Until then, just pick someone."

hide janine with dis

pause 0.5

show leaf with dis

leaf @talking2mouth "Hey. Figured I'd better grab you before someone else did."

red @happy "Sure thing."

$ ValueChange("Leaf", 3, 0.5)

scene black with dis
call clearscreens from _call_clearscreens_77

narrator "You train with Leaf for the rest of the evening."

$ BattleTeamTraining()

call texting from _call_texting_7

jump day010427