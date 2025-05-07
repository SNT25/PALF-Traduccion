label secondhomeroom010419:

if (excusesecondhomeroom):
    narrator "You take advantage of your Excused Absence to skip your second homeroom."
    jump freeroam

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

oak @talkingmouth "Welcome back to class, ladies and gentlemen!" 
oak @talkingmouth "I can tell you're all very excited for the upcoming Battle Team tryouts happening later today, but remember that you have to pass a quiz first!"
oak @talkingmouth "I hope you all remember what I said during homeroom this morning. 'If it's not 100%%, it's 50%%!" 
oak @talkingmouth "You may think your strategy is undefeatable, but even the best trainer can be brought down by something as unlucky as missing Will-O-Wisp five times in a row."
oak @talkingmouth "{color=#0048ff}In this upcoming battle, you'll be under the field effect 'Blinding Fog.'{/color}"
oak @talkingmouth "That means, if a move has a chance to miss, it {i}will.{/i} Keep that in mind."

redmind uniform @thinking "Huh... I've never heard of a field effect like that. I guess it's just a hypothetical, though. I can't imagine something like that existing in real life."

oak @talkingmouth "Now, let's try to complete this test quickly! I don't want to be late to the Battle Team tryouts."

$ trainer1 = Trainer("red", TrainerType.Player, [Pokemon(pokedexlookupname("Nuzleaf", DexMacros.Id), level=28, moves=[GetMove("Razor Leaf"), GetMove("Fake Out"), GetMove("Feint Attack"), GetMove("Leaf Blade")])])
$ trainer2 = Trainer("oak", TrainerType.Enemy, [Pokemon(pokedexlookupname("Roggenrola", DexMacros.Id), level=20, moves=[GetMove("Sand Attack")], ability="Sturdy")])

$ trainer1.GetTeam()[0].ApplyStatus("poisoned")
$ trainer1.GetTeam()[0].Health = 15

call Battle([trainer1, trainer2], currentWeather=("blinding fog", 999), gainexp=False, healParty=False, uniforms=[True, False], lockbag=True) from _call_Battle_45
$ battlehistory["Oak4"] = _return

$ renpy.transition(dissolve)
show screen currentdate

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

if (WonBattle("Oak4")):
    red uniform @happy "Phew. This was a bit of a trickier quiz than I thought. It's nice this one had two ways to win, though."
else:
    red uniform @sad "Oh, crap. I don't think I did this one right."

oak "{w=0.5}.{w=0.5}.{w=0.5}."

pause 0.5

oak @talkingmouth "At a glance..."

pause 0.5

if (WonBattle("Oak4")):
    oak "It looks like everyone did quite well."
else:
    oak "It seems some of you did not take into account my warnings about the inevitability of missing. Or perhaps you're just unaware how a Pokémon's accuracy and evasion interact with move accuracy?"

oak @talkingmouth "Remember, even if a move has 100%% accuracy, if your accuracy has been lowered, you can still miss." 
oak @talkingmouth "The same applies if your opponent's evasion has been raised."

$ renpy.music.set_volume(0.1, delay=1.0, channel="music")
$ PlaySound("BellChime.ogg")

$ renpy.pause(2.0, hard=True)
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

oak @talkingmouth "But I suppose you'll be able to see those maneuvers in battle in a few hours! I hope to see you all at the Battle Team Tryouts shortly! Dismissed!"

label aftersecondhomeroom010419:

if (pikachuobj not in playerparty):
    redmind uniform @thinking "Alright. I should head back to my dorm, pick up [pika_name], then go to the battle tryouts now."
else:
    redmind uniform @thinking "Alright. I should go to the battle tryouts now."

pause 1.0

redmind @thinking "Hm. I wonder if there was some kind of sign-up process I should have done?"
redmind @happy "...Guess I'd better hope that Janine can vouch for me."

call clearscreens from _call_clearscreens_60

scene blank2
show blank2 as secondblank2
with splitfade

pause 1.0

if (pikachuobj not in playerparty):
    $ AddPikachu()

$ HealParty()

show stadium_full behind secondblank2
show blank as secondblank behind secondblank2
$ renpy.music.play("Audio/Stadium_crowd.ogg", channel='crowd', loop=True, fadein=1.5)
$ renpy.music.play("Audio/Stadium_chant.ogg", channel='crowd2', loop=True, fadein=1.5)

$ renpy.pause(0.75, hard=True)
stop music fadeout 1.5
$ renpy.music.queue("Audio/Music/Indigo_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/Indigo_Loop.ogg", channel='music', loop=True, tight=None)

$ renpy.pause(1.0, hard=True)

hide secondblank2 with transball
$ renpy.pause(0.25, hard=True)
show blank as secondblank:
    alpha 1.0
    ease 0.5 alpha 0.0

show stadium_full:
    subpixel True
    zoom 3.0 alpha 0.65 xalign 0.15 ypos 2600
    ease 1.25 alpha 1.0 xalign 0.0 ypos 3000
    xalign 0.85 alpha 0.65 ypos 2600
    ease 1.25 alpha 1.0 xalign 1.0 ypos 3000
    xalign 0.5 alpha 0.4 ypos 2400
    ease 1.0 alpha 1.0 zoom 1.0 ypos 1080

show lightbeam1 as beam1:
    pause 2.75
    zoom 0.6 alpha 0.0 yalign 0.9 xpos 0 rotate 40
    block:
        ease 0.25 alpha 0.5
    pause 0.3
    block:
        ease 1.0 rotate -40
        pause 0.5
        ease 1.0 rotate 40
        pause 0.5
        repeat
    
show lightbeam1 as beam2:
    pause 2.75
    zoom 0.6 alpha 0.0 yalign 0.9 xpos -300 rotate -40
    block:
        ease 0.25 alpha 0.5
    pause 0.1
    block:
        ease 1.0 rotate 40
        pause 0.5
        ease 1.0 rotate -40
        pause 0.5
        repeat

show lightbeam1 as beam3:
    pause 2.75
    alpha 0.0 yalign 0.8 xpos -400 rotate -40
    block:
        ease 0.25 alpha 0.6
    pause 0.2
    block:
        ease 1.0 rotate 40
        pause 0.5
        ease 1.0 rotate -40
        pause 0.5
        repeat
        
show lightbeam1 as beam4:
    pause 2.75
    alpha 0.0 yalign 0.8 xpos -1400 rotate 40
    block:
        ease 0.25 alpha 0.6
    block:
        ease 1.0 rotate -40
        pause 0.5
        ease 1.0 rotate 40
        pause 0.5
        repeat
        
pause 3.5

hide blank as firstblank
hide evening
hide blank

$ renpy.transition(dissolve)
show screen currentdate

show stadium_full:
    alpha 1.0 zoom 1.0 yalign 1.0 xalign 0.5

redmind -uniform "Huh. Back here again. But now I'm standing in the arena. It looks even bigger from the bottom..."

show blue with dis:
    xpos 0.25 zoom 1.0 ypos 1.0
    pause 0.5
    ease 0.5 xpos .375 zoom 1.3 ypos 1.2

blue @talkingmouth "Yo, loser."

red @closedbrow talking2mouth "Hi, [blue_name]."

blue @angry "Lance and Janine told me that if I start anything with you today, I'm done. So I just want to let you know that you should give up before you embarrass yourself."

red @confused "Oh, yeah? I think I'll take my chances with the embarrassment, to be honest."

blue @happy "Your funeral. Smell ya later... after {i}I{/i} win!"

show blue:
    ease 2.0 zoom 0.5 ypos 0.8 xpos 0.125

pause 1.0

red @closedbrow talking2mouth "Win? There's no, like, #1 winner, right? Isn't it just a 'you get in or you don't,' kind of thing?"

show leaf with dis:
    xpos 0.75 zoom 1.0 ypos 1.0
    pause 0.5
    ease 0.5 xpos .675 zoom 1.3 ypos 1.2

leaf @happy "[first_name]! God, I'm so excited! So many battles... this is going to be the {i}best.{w=0.5} Evening.{w=0.5} Ever!{/i}"

red @surprised "Huh? Leaf, you're trying out for the Battle Team?"

leaf @sarcastic "I mean, duh. You know how much I love battles, right?"

red @happy "Yeah, that checks out! Guess I just didn't expect to see you here!"

leaf @angrybrow happymouth blush "Well, then, expect this:{w=0.5} Me.{w=0.5} On top of the winner's podium.{w=0.5} I've got a secret weapon this time around!"

red @talkingmouth "Can't wait to see it."

show leaf:
    ease 2.0 zoom 0.5 ypos 0.8 xpos 0.875

show hilbert with dis:
    xpos 0.45 zoom 1.0 ypos 1.0
    pause 0.5
    ease 0.5 xpos .5 zoom 1.3 ypos 1.2

hilbert @thinking "[ellipses]"

pause 1.0

red @talkingmouth "Come to say good luck?"

hilbert @sadbrow talkingmouth "If you can't win without it, you don't deserve it."

pause 1.0

red @happy "So what did you come to say?"

hilbert @thinking "[ellipses]"
hilbert @closedbrow talkingmouth "Show no mercy to the competition. Especially not to me."

if (WonBattle("Hilbert1")):
    hilbert "You may have won our last battle, but I'm not going to hand you a win again."

else:
    hilbert "I may have won our last battle, but I won't go any easier on you this time."

red @happy "I'll see what I can do. And may the best man win, huh?"

hilbert @closedbrow talking2mouth "May the man with the most power win."

show hilbert:
    ease 1.5 zoom 0.5 ypos 0.8 xpos 0.75

show silver with dis:
    xpos 0.55 zoom 1.0 ypos 1.0
    pause 0.5
    ease 0.5 xpos .5 zoom 1.3 ypos 1.2

pause 2.0

silver @talkingmouth "Let's show that asshole he was wrong."

red @happy "Totally."

silver smilemouth "[ellipses]"

show silver:
    ease 1.5 zoom 0.5 ypos 0.8 xpos 0.25

red @closedbrow talking2mouth "...Lots of people want to get in the Battle Team. I wasn't expecting so many people I recognized, to be honest..."

show erika with dis:
    zoom 1.0 ypos 1.0
    pause 0.5
    ease 0.5 zoom 1.3 ypos 1.2

erika @talkingmouth "Oh, hello, [first_name]!"

if (not HasEvent("Erika", "Backstory")):
    $ AddEvent("Erika", "Backstory")
    red @surprised "Erika! Hi. I'm surprised to see you here."

    erika @talkingmouth "Oh? Surely I've told you about my extensive tutelage in competitive battling, no?"

    red @talkingmouth "Uh... no, I think I'd remember that."

    erika @talkingmouth "Ah. Well, I was originally sent here specifically so I could become a member of the Battle Team."

    red @confusedeyebrows talking2mouth "Huh?"

    erika @closedbrow talking2mouth "Yes, it had originally been intended for me to simply attend Kobukan Academy in a provisionary role. I would not attend classes. Rather, I'd just participate in Battle Team activities."

    red @confusedeyebrows talkingmouth "A provisionary student? How does that work?"

    erika @talkingmouth "Well, I've never had the fortune to attend a public school. There were some concerns that I might not be able to succeed in that environment."

    redmind @thinking "This girl is {i}master{/i} of the passive voice."

    red @happy "Well, great! But you're attending classes now? What changed?"

    erika @surprised "Ah, well..."

    erika @sadbrow happymouth "That would be you."

    red @surprised "Huh?"

    red @happy "Oh, did I convince you that everything's cool here? That you don't need to worry about other students, and we're all nice guys?"

    erika @happy "Oh, no! Rather, you convinced me that I could defend myself from the brutes and adversaries doubtlessly embedded in the school."

    erika @talkingmouth "I, again, am truly sorry about that slap. But it gave me a tremendous sense of self-confidence about my ability to succeed in this school."

    red @confused "Uh-huh."

    redmind @thinking "Seriously. That was such a weak slap. But I don't have the heart to tell her."

    red @happy "Well, that's great! Maybe I'll see you around some more, then?"

    erika "Yes, I hope so. I've decided to tip my toes into both the Grass and Poison-type electives."

    red @happy "Nice. I guess you have a thing for flowery Pokémon?"
    
    erika @surprised "Oh? Well, yes, I suppose so."

    red @confusedeyebrows talking2mouth "Huh, you didn't pick them because of that?"

    erika @closedbrow talking2mouth "Not so much. Rather, I'm much more interested in Grass-types' natural affinity towards sun-based strategies."
    erika @talkingmouth "There are some rare Pokémon that I believe have been discovered in the Paldea region recently that I believe could synchronize well."

    erika @happy "Oh, and the Poison-types are to check the omnipresent threat of Fairy-types rampaging around in the upper leagues." 
    erika @sadbrow talking2mouth "I originally considered using Fairy-types myself, to counter dragons, but after seeing that awful Lance's horrid performance, I don't think they're nearly as much of a threat as they used to be."

    red @surprised "Huh. For a girl who's never gone to school before, you know a lot about battle. Maybe the Battle Team makes more sense than I thought."

    erika @closedbrow talkingmouth "Well, my tutors were quite good."

    red @closedbrow talking2mouth "So how come you don't like Lance? I mean, he {i}is{/i} a two-time national Champion."

    pause 2.0

    erika @angry "He does nothing with dignity. He failed, {i}multiple times{/i}, to become Champion. Our region is now saddled with a multiple-time failure as Champion."
    erika @closedbrow talking2mouth "It would have been one thing if he'd simply tried multiple times to become Kanto Champion, but then he further embarrassed us by failing multiple times to become Johto Champion."
    erika @sadbrow talking2mouth "And now he's set his eyes on failing multiple times to become World Champion, so it doesn't seem he's planning on ending that pattern of behavior any time soon."
    erika @happy "As a noted author once said, 'Is it not better to surrender your ambitions than have them slaughtered?'"

    red @closedbrow talking2mouth "Hm. I've got my problems with him, but trying over and over to achieve his goals isn't one of them."

    erika @closedbrow talking2mouth "Oh? Well, I suppose we have different priorities, then."
    erika @happy "That's certainly alright, and I respect your opinion."

    red @happy "Same to you. See you around?"

    erika @happy "Quite right."

else:
    red @surprised "Oh! Hey, Erika! You know, we had that talk about Pokémon, and you casually mentioned you had some insane competitive knowledge."
    red @happy "Guess I should've expected that you'd be here."

    erika @surprised "Well, I'm rather surprised you're here. Do you have much in the way of formal, competitive Pokémon knowledge?"

    red @talkingmouth "No, not really. But my guys love me, and I love them, and that's almost as good, I think."

    erika @happy "A darling sentiment. Let's see if it holds up on the battlefield, hm?"

show erika:
    ease 1.5 zoom 0.5 ypos 0.8 xpos 0.65

show ethan with vpunch

ethan @happy "Hey, dude! Let's get this done! We're going to crush everyone else and get on that Battle Team, no sweat!"

red @surprised "Ethan? I didn't know you wanted to be on the Battle Team."

ethan @closedbrow talkingmouth "Yeah, it was kinda a spur-of-the-moment thing. But we've got pretty similar teams, and you seem confident, so I figure that I have a chance here." 
ethan @happy "{i}This time,{/i} me being here isn't a coincidence!"

red @happy "Well, what a nice surprise. I'm not going to go any easier on you, just 'cause you're my buddy, though!"

ethan @angrybrow happymouth "You better not! I'm going to beat you {i}twice!{/i}"

show ethan:
    ease 0.5 zoom 0.5 ypos 0.8 xpos .35

$ renpy.music.stop(channel='crowd', fadeout=5.0)
$ renpy.music.stop(channel='crowd2', fadeout=5.0)

pause 3.0

narrator "For the next ten minutes, people continually walk into the Battle Hall. Altogether, it looks like roughly fifty trainers are competing to get into the Battle Team."

redmind "Okay... that's actually a few less people than I thought would try to get in, based on how many people said they wanted to challenge the Pokémon League on my first day of class." 
redmind @thinking "But I guess a bunch of people think they can't make it, so they don't even join the tryouts."
redmind @happy "That won't be me. Even being told 'no' by one of the judges won't stop me from achieving my goal. I'm {i}getting in{/i}... even if it's out of spite."

show blue behind beam1:
    ease 1.0 xpos 0.05 ypos 0.8 zoom 0.3

show silver behind blue:
    ease 1.5 xpos 0.1 ypos 0.7 zoom 0.25

show ethan behind silver:
    ease 2.0 xpos 0.15 ypos 0.6 zoom 0.2

show leaf behind beam1:
    ease 1.0 xpos 0.95 ypos 0.8 zoom 0.3

show hilbert behind leaf:
    ease 1.5 xpos 0.9 ypos 0.7 zoom 0.25

show erika behind hilbert:
    ease 2.0 xpos 0.85 ypos 0.6 zoom 0.2

show janine behind beam1 with Dissolve(1.0):
    xpos 0.5 ypos 0.7 zoom 0.25

janine @talking2mouth "Hm."

show lance behind janine with Dissolve(1.0):
    xpos 0.6 ypos 0.7 zoom 0.25
    ease 1.0 xpos 0.4

show silver angry
show blue angry 
with dis

lance @talking2mouth "The slate looks promising.{w=0.5} With a few exceptions."

blue @talkingmouth "Doubt me all you want! I'm gonna be so good you {i}can't{/i} turn me down!"

show blue behind beam1:
    xpos 0.05 ypos 0.8 zoom 0.3

show silver behind blue:
    xpos 0.1 ypos 0.7 zoom 0.25

show ethan behind silver:
    xpos 0.15 ypos 0.6 zoom 0.2

show leaf behind beam1:
    xpos 0.95 ypos 0.8 zoom 0.3

show hilbert behind leaf:
    xpos 0.9 ypos 0.7 zoom 0.25

show erika behind hilbert:
    xpos 0.85 ypos 0.6 zoom 0.2

show janine behind beam1:
    xpos 0.5 ypos 0.7 zoom 0.25

show lance behind janine:
    xpos 0.4 ypos 0.7 zoom 0.25 

lance @talking2mouth "Your ego continues to appoint you the center of attention. I was not thinking of, or referring to you."
lance @sad "Frankly, I didn't even notice you were here."

show silver -angry
show blue -angry frownmouth
with dis

blue @sad "Wh-what?!"

janine @closedbrow talking2mouth "Enough of this, already. We're about to find out whether I never have to see you again, or whether you're my problem for the next year. Just hold it in 'til then."

pause 1.0

janine @talking2mouth "Shall we go over the rules?"

lance @closedbrow talking2mouth "Mm."

janine @talking2mouth "Alright, everyone! These will be full-party double battles. Any Pokémon you have on-hand are permitted to be used."

lance @angry "{i}Borrowed Pokémon will not be.{/i}"

janine @talking2mouth "{size=30}Sir, we've already said we're not going to do that.{/size}"

lance @talking2mouth closedbrow "You have gone behind my back once already. You will not do so again."

janine @talking2mouth "Right. Anyway, back to the rules... the use of items, used by trainer or Pokémon, is not permitted."

hilbert surprisedbrow frownmouth @surprised "...What? I... my Pokémon only know one move. Choice Items would work so well with that strategy... and I just went to the city, and... so much money..."

show erika surprisedbrow frownmouth with dis

silver surprisedbrow frownmouth @surprised "H-huh?! But I've got a ton of berries, and... {i}shit.{/i}"

erika surprisedbrow frownmouth @surprised "B-but... my strategy heavily depends on the usage of items..."

janine @talking2mouth "Also, this is going to be a level-equal battle. All your Pokémon will be scaled to level 50."

show leaf surprisedbrow frownmouth with dis

blue surprisedbrow frownmouth @surprised "What?! No-one told me about this! That's not fair, my levels are way higher than everyone else here!"

leaf surprisedbrow frownmouth @surprised "Wh-what?! But my secret weapon... I was going to use Dragon Rage, and just sweep everyone! You can't do that!"

janine @talking2mouth "Any questions?"

pause 2.0

show blue angry:
    ease 0.5 xpos 0.25 ypos 0.8

show silver angry behind blue:
    ease 1.5 xpos 0.2 ypos 0.7

show leaf angry:
    ease 1.5 xpos 0.75 ypos 0.8

show hilbert angry behind leaf:
    ease 0.5 xpos 0.8 ypos 0.7

show erika angry behind hilbert:
    ease 2.0 xpos 0.75 ypos 0.6

blue @talkingmouth "Yeah, what the hell's up with this ruleset?"

leaf @talking2mouth "You're just banning everything! You've ruined {i}everyone's{/i} battle plans!"

janine @talking2mouth "A serious battle does not give you the luxury of your preferred ruleset."

pause 1.0

redmind @thinking "...She set up that ruleset for me, didn't she? That ruleset limits pretty much everyone except me."

ethan @happy "Hey, I don't see the problem! I {i}like{/i} that ruleset."

pause 1.0

redmind @thinking "Everyone except Ethan and I, I guess. Still, there's so much I need to learn. Items? Level scaling? Geez."

pause 1.0

lance @talking2mouth "Back away."

show blue -angry frownmouth:
    ease 1.0 xpos 0.05 ypos 0.8

show silver -angry behind blue:
    ease 1.5 xpos 0.1 ypos 0.7

show leaf -angry frownmouth:
    ease 1.5 xpos 0.95 ypos 0.8

show hilbert -angry behind leaf:
    ease 0.5 xpos 0.9 ypos 0.7

show erika -angry frownmouth behind hilbert:
    ease 2.0 xpos 0.85 ypos 0.6

lance @talking2mouth "This tryout will take place as a series of seven round-robin matches. You will be fully healed between battles. Besides the aforementioned rules, no other clauses will be enforced."
lance @closedbrow talking2mouth "Winning all your matches does not guarantee a spot in the Battle Team. Losing all your matches does not guarantee elimination."
lance @angrybrow talking2mouth "Though it does make it {i}far more likely.{/i}"

pause 1.0

lance @talking2mouth "The order of your opponents will be picked randomly."

pause 1.0

lance @sad "Oh. Also, there are prizes for people who win more than four of their battles."

pause 1.0

lance @talking2mouth "That's enough. Let's begin. Janine, read out the beginning matches, please."

janine @talking2mouth "Hold on, Sir. I think we should give everyone five minutes, in case they need to make changes to their teams, now that they've heard the rules."

lance @sad "{w=0.5}.{w=0.5}.{w=0.5}.Fine. Alert me when...{w=0.5} hm?"

show sonia closedbrow frownmouth behind janine:
    xpos 1.5 ypos 0.7 zoom 0.25
    easeout 1.3 xpos .52
    easein 2.0 xpos .58

pause 1.3

show janine surprisedbrow frownmouth with dis:
    ypos 0.7
    linear 0.2 xpos .48 

$ PlaySound("body crash.ogg")

show arenabg 
show soniabg:
    xpos 0.3
    ease 2.0 xpos 0.0
with Dissolve(2.0)

janine @talking2mouth "S-S-Sonia?!"

if (GetRelationship("Nessa") == "Friend"):
    redmind @surprised "Sonia?! Like, Nessa's old friend?! Nessa said she disappeared without a trace! What's she doing here?"
else:
    redmind @surprised "Sonia? Who's that?"

$ BecomeNamed("Sonia")

sonia surprisedmouth "Janine! I'm sorry about last year! I'm really, {i}really{/i} sorry! But, please, let me try out for the Battle Team again!"

show janinebg:
    xpos -0.3
    ease 2.0 xpos 0.0 
with dis

show janine:
    ypos 0.7
    ease 1.0 xpos 0.47

show lance:
    ypos 0.7
    ease 1.0 xpos 0.4

janine @talking2mouth "Wh-what are you {i}doing{/i} here?! Are you okay? Where have you been? When did you get back? How--"

pause 1.0

show janine:
    ypos 0.7
    ease 1.0 xpos 0.5

janine angry "How {i}dare{/i} you show your face here, after what you did last year!"

sonia @talking2mouth "I know, and I'm {i}so{/i} sorry. But I won't let you down again, I promise!"

janine @angry "Yeah! You won't let me down again, because like {i}hell{/i} I'm letting you back on the team!"

sonia @talking2mouth "B-but... I promise I won't lose this time!"

janine @talking2mouth "I don't even care that you lost! I care that you ditched us without telling {i}anyone!{/i} How am I supposed to trust that you'll stick with the team this time?"

sonia @sad "Please!"

janine @talking2mouth "No!"

sonia @talking2mouth "But... but, then..."

hide soniabg
hide janinebg
hide arenabg
with dis

show sonia sad:
    ypos 0.7
    ease 0.5 xpos 0.4

show lance closedbrow:
    ypos 0.7
    ease 0.7 xpos .32

show janine surprisedbrow frownmouth:
    ypos 0.7
    ease 0.3 xpos .52 xzoom -1

sonia @talking2mouth "Sir! I'm so sorry for what happened. I panicked, and made an awful mistake, and I... I just want another chance, Sir! I'll do anything!"

lance @closedbrow "{w=0.5}.{w=0.5}.{w=0.5}."

sonia @talking2mouth "A-anything... Sir... Please.{w=0.5} I {i}promise{/i} I won't let you down again."

pause 1.0

lance -closedbrow @talking2mouth "...I have no objections."

show janine angry:
    ypos 0.7
    ease 0.3 xpos .51

janine @talking2mouth "Sir! How can you say that?!"

lance @closedbrow talking2mouth "Failure is not the mark of a bad trainer. Giving up is."

pause 1.0

show janine angry:
    ypos 0.7
    ease 1.0 xpos .53

lance @talking2mouth "Sonia has already demonstrated her worth in battle. I believe she can rejoin the Battle Team at her old rank."
lance @sad "The final decision rests on your shoulders, of course."

show janine thinking:
    ypos 0.7
    ease 1.0 xpos .51

janine "{w=0.5}.{w=0.5}.{w=0.5}."

pause 1.0

janine @closedbrow talkingmouth "Sir. If I permit Sonia to {i}try out{/i} again... at the same level as everyone else..."

pause 1.0

janine @talking2mouth "You won't interfere with my choices for the Battle Team?" 
janine -thinking @angry "If I decide someone can get in, you'll let them in, and not try to remove them?"

lance @angry ".{w=0.5}.{w=0.5}.{w=0.5}Fine."

sonia -sad surprisedmouth "Th-then... that means...?"

janine @closedbrow talkingmouth "I'm letting you apply. That's all. To me, you're a brand-new student again. We have no history, and I don't care if you get in or don't."

sonia @talking2mouth "Th-thank you..."

janine @angry "Don't make me regret it."

show sonia:
    ypos 0.7
    parallel:
        ease 0.3 xzoom -1
        pause 1.7
        ease 0.3 xzoom 1
    parallel:
        ease 2.0 xpos 0.8 ypos 0.5 zoom 0.15

show janine:
    ypos 0.7
    ease 1.0 xpos 0.55 xzoom 1

show lance:
    ypos 0.7
    ease 1.0 xpos .45

pause 1.0

janine @talking2mouth "Alright, let's get this show on the road. We've got hundreds of battles to get through, so we'll be taking these ten at a time." 
janine @closedbrow talkingmouth "Spread out around the arena, give other battlers some room. Lance and I will be walking between the battles, and keeping an eye on you."

lance @talking2mouth "It goes without saying that if you do not have enough control over your Pokémon to avoid leaving your designated area, that will not reflect favorably on your chances."

janine @talking2mouth "Alright. Let's begin."

narrator "The battles begin, fast and hard. You keep a keen eye on the competition, sizing them up. And then..."

hide janine with dis

pause 1.0

show janine with dis

janine @talking2mouth "Alright. You're up."

python:
    trainerred = Trainer("red", TrainerType.Player, playerparty, number=2)

    #Leaf: A strong, normal team
    trainerleaf = MakeTrainer("Leaf", number=2)

    #Silver: A decently strong, normal team
    trainersilver = MakeTrainer("Silver", number=2)

    #Blue: One intelligent Pokemon
    trainerblue = MakeTrainer("Blue", number=2)

    #Erika: A fully intelligent team, but the *dumbest* movesets
    trainererika = MakeTrainer("Erika", number=2)

    #Ethan: Your team, but weaker. Fully intelligent.
    ethanteam = []
    for mon in playerparty:
        if (mon != pikachuobj):
            ethanteam.append(Pokemon(mon.Id, level=max(1, mon.Level - 1), ivs=[1, 1, 1, 1, 1, 1], evs=[0, 0, 0, 0, 0, 0], moves=copy.deepcopy(mon.Moves), gender=mon.Gender, ability=mon.Ability, intelligence=1))
        else:
            ethanteam.append(Pokemon(172.1, level=mon.Level, ivs=[1, 1, 1, 1, 1, 1], evs=[0, 0, 0, 0, 0, 0], moves=copy.deepcopy(mon.Moves), gender=Genders.Female, ability="Small World", intelligence=1))
    trainerethan = Trainer("ethan", TrainerType.Enemy, ethanteam, number=2)

    #Hilbert: Same gimmick as before
    trainerhilbert = MakeTrainer("Hilbert", number=2)

    #Sonia: Intelligent Team. Imply she was previously much higher level, but her 'mons have lost levels due to not training.
    #Didn't evolve Pokemon, due to being unsure if she could handle their power.
    trainersonia = MakeTrainer("Sonia", number=2)

    potentialtrainers = [trainerleaf, trainerblue, trainererika, trainerhilbert, trainersilver, trainersonia, trainerethan]

$ wins = 0

label randomtryout:
$ selectedtrainer = RandomChoice(potentialtrainers)
$ potentialtrainers.remove(selectedtrainer)
$ selectedtrainername = selectedtrainer.Name.title()

janine @talking2mouth "You'll be facing off against [selectedtrainername]."

if (selectedtrainer == trainerleaf):
    janine @talking2mouth "You should be fine. The level equalizer means her Dragon Rages aren't nearly as much of a threat."

    red @talking2mouth "Good to know."

elif (selectedtrainer == trainerblue):
    janine @talking2mouth "He's full of hot air. Just watch out for that Pidgeotto. He's got it listening to him now."

    red @surprised "Already?!"

elif (selectedtrainer == trainererika):
    janine @talking2mouth "She has no idea how to battle. She obviously spent a fortune on Move Tutors and TMs, but that doesn't make up for her movesets."

    red @closedbrow talking2mouth "Phew..."

elif (selectedtrainer == trainerhilbert):
    janine @talking2mouth "His Pokémon only have one move each. Without their choice items, they won't hit nearly as hard, but watch out anyway."

    red @sad "Sorry, Hilbert..."

    pause 1.0

    red @surprised "Oh, yeah, is it cool if I stream this fight to Hilda? She wanted to see one of Hilbert's battles."

    janine @surprised "Uh... I guess? I don't know who Hilda is, but go ahead."

    red @talkingmouth "Cool."

    show phone_B
    show phone_A
    show hilda behind phone_A:
        zoom 0.95
    with fadeinbottom

    red @talkingmouth "Ready?"

    hilda @talkingmouth "Yep."

    if (GetRelationship("Hilda") == "Caretaker"):
        red @happy "Hey, do you realize what this means?"

        hilda @talkingmouth "What?"

        red @happy "You asked me for help with something. This is {i}progress{/i}."

        hilda veins angry "Bite me! I'm rooting for Hilbert now!"

elif (selectedtrainer == trainersilver):
    janine @talking2mouth "Don't have any advice for this one. Just hit harder than he does."

    red @closedbrow talking2mouth "I'll do my best."

elif (selectedtrainer == trainersonia):
    janine @sad "She... ugh. She's been training for a {i}long{/i} time, but she's obviously out of practice. Just don't let her hit your weaknesses, because she {i}will.{/i} And watch out for her dogs."

    if (GetRelationship("Nessa") == "Friend"):
        red @surprised "Yeah, Nessa warned me about her. I didn't think I'd be fighting her so soon, though."
    else:
        red @talkingmouth "Yeah, if she's a former Battle Team member, I'd better take her seriously..."

elif (selectedtrainer == trainerethan):
    janine @talking2mouth "This guy's Pokémon are weak, and so is he, but they all work together perfectly. Don't get careless."

    red @talkingmouth "Wouldn't dream of it. I know Ethan, and I know he'll give me a tough fight."

janine @talking2mouth "Good luck."

show lance:
    ypos 0.7
    ease 0.5 xpos 0.5

hide janine with dis

call Battle([trainerred, selectedtrainer], gainexp=False, levelscale=50, specialmusic=(("audio/music/swordshieldgym-intro.ogg", "audio/music/swordshieldgym-loop.ogg") if len(potentialtrainers) == 6 else "Nothing"), stopmusic=False) from _call_Battle_46
$ result = _return

if (result):
    $ wins += 1
    $ ValueChange("Janine", 2, 0.5, True)
    narrator "Janine seems pleased."
else:
    narrator "Janine purses her lips."

if (selectedtrainer == trainerleaf):
    $ battlehistory["Leaf1"] = result

elif (selectedtrainer == trainerblue):
    $ battlehistory["Blue3"] = result

    red @angry "Blue, what the hell?!"

    show blue with dis

    blue frownmouth @angry "What, what's your problem {i}this{/i} time?"

    red @talking2mouth "Nate said you were bringing that Charmander to the Pokémon Center!"

    blue @angry "Yeah. We {i}did{/i}. A week ago. Then I came back to the Center, and waited until they re-released it into the wild. Then I caught it."

    red @talking2mouth "But--"

    blue @closedbrow talkingmouth "Look, just 'cause you didn't think of it is no reason to throw a tantrum." 
    blue @angry "If you weren't so busy wasting your time with your friends, maybe you could've taken him to the Pokémon Center yourself."

    red @angrybrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
    red @angrybrow talking2mouth "I'm not forgetting this."

    hide blue with dis

elif (selectedtrainer == trainererika):
    $ battlehistory["Erika1"] = result

elif (selectedtrainer == trainerhilbert):
    $ battlehistory["Hilbert2"] = result

    if (battlehistory["Hilbert2"]):
        hilda @happy "Nice going, farmboy. You're a pretty good battler. Thanks for streaming this!"

    else:
        hilda @happy "You're a pretty good battler, but you just can't beat Hilbert's single-mindedness. Anyway, thanks for streaming this!"

    if (selectedtrainer == trainerhilbert):
        hide phone_B
        hide phone_A
        hide hilda
        with fadeoutbottom

elif (selectedtrainer == trainersilver):
    $ battlehistory["Silver2"] = result

elif (selectedtrainer == trainersonia):
    $ battlehistory["Sonia1"] = result

elif (selectedtrainer == trainerethan):
    $ battlehistory["Ethan1"] = result

    if (absolobj in playerparty):
        show ethan with dis

        red @confused "How did you get an Absol?" 

        ethan @happy "Dude, I was going to say the same thing to you."

        red @talkingmouth "Uh... it showed up about three minutes before a meteor hit the fields outside of campus."

        ethan @talkingmouth "Cool. Mine showed up about three minutes before a forest fire started."

        red @happy "Huh, crazy. Small world?"

        ethan @sadbrow talkingmouth "Small world."

        hide ethan with dis

if (len(potentialtrainers) > 0):
    narrator "Battles rage around you until Janine approaches you again."
    jump randomtryout

$ renpy.music.play("Audio/Music/Indigo_Start.ogg", channel='music', loop=None, fadein=3.0, tight=None)
$ renpy.music.queue("Audio/Music/Indigo_Loop.ogg", channel='music', loop=True, tight=None)

red @happy "Alright, who's next? Can't wait to...{w=0.5} wait."
red @surprised "That was seven, wasn't it? So... I'm done?"

if (wins == 7):
    red @surprised "Holy shit! I won {i}all{/i} my matches! That's insane!"

elif (wins == 6):
    red @closedbrow talking2mouth "Wow... six out of seven? That {i}really{/i} isn't bad! I bet Lance won't be able to ignore that."
    
elif (wins == 5):
    red @closedbrow talking2mouth "Five wins? Well, at least I get a prize."
    
elif (wins == 4):
    red @closedbrow talking2mouth "Only four wins... well, it's more than half... but I need more than that to stand out."
    
elif (wins == 3):
    red @sad "Three wins isn't going to cut it, is it?"
    
elif (wins == 2):
    red @sad "Two wins is definitely not going to cut it. I can only imagine what Janine'll need to pull to make this happen."
    
elif (wins == 1):
    red @closedbrow talking2mouth "Only one win.{w=0.5} ...Damn."
    
elif (wins == 0):
    red @happy "Alright, managed to lose everything, nice! Losing against Erika was actually kinda tricky."
    red @closedbrow talking2mouth ".{w=0.5}.{w=0.5}.{w=0.5}Wait."
    red @sad "This isn't golf."

lance @talking2mouth "That's enough. We've seen everything we needed to."

show lance:
    ypos 0.7
    ease 0.5 xpos 0.45

show janine behind beam1:
    ypos 0.7 xpos 0.55 zoom 0.25

show blue behind beam1:
    xpos 0.05 ypos 0.8 zoom 0.3

show silver behind blue:
    xpos 0.1 ypos 0.7 zoom 0.25

show ethan behind silver:
    xpos 0.15 ypos 0.6 zoom 0.2

show leaf behind beam1:
    xpos 0.95 ypos 0.8 zoom 0.3

show hilbert behind leaf:
    xpos 0.9 ypos 0.7 zoom 0.25

show erika behind hilbert:
    xpos 0.85 ypos 0.6 zoom 0.2

show sonia behind erika:
    xpos 0.8 ypos 0.5 zoom 0.15

with dis

pause 1.0

lance @talking2mouth "Janine and I will make our final decisions shortly. If you are accepted into the Battle Team, we will contact you."
lance @talking2mouth "You may leave."

pause 2.0

red @surprised "What?"

show leaf:
    xpos 0.95 ypos 0.8 zoom 0.3
    ease 0.5 xpos 0.85 ypos 0.8 zoom 0.3

leaf frownmouth @talking2mouth "Sir, what about the prizes for winning?"

lance @talking2mouth "Those will be delivered directly to your dorms in the following days."

show blue frownmouth:
    xpos 0.05 ypos 0.8 zoom 0.3
    ease 0.5 xpos 0.15 ypos 0.8 zoom 0.3

blue @sad "Wait, isn't there an awards ceremony? Some kinda thing where you give out medals?"

lance @closedbrow talking2mouth "No. The school insists I let non-Battle Team members watch the tryouts, but I would, personally, greatly prefer to do this entire event behind closed doors."

janine @sad "Yeah, the drama, and the music, is a bit much. You should really all just... go."

stop music fadeout 2.0

hide beam1
hide beam2
hide beam3
hide beam4
with dis

red @closedbrow talking2mouth "...That's a bit anticlimatic."

blue @talkingmouth "{size=30}Man, this is bullshit...{/size}"

show janine:
    ypos 0.7 xpos 0.55 zoom 0.25
    ease 1.5 xpos 0.5 zoom 1.0 ypos 1.0

show blue:
    xpos 0.15 ypos 0.8 zoom 0.3
    ease 2.5 xpos -0.2

show silver:
    xpos 0.1 ypos 0.7 zoom 0.25
    ease 1.5 xpos -0.2

show ethan behind lance:
    xpos 0.15 ypos 0.6 zoom 0.2
    ease 3.5 xpos 1.2

show leaf:
    xpos 0.85 ypos 0.8 zoom 0.3
    ease 1.5 xpos 1.2

show hilbert:
    xpos 0.9 ypos 0.7 zoom 0.25
    ease 1.5 xpos 1.2

show erika:
    xpos 0.85 ypos 0.6 zoom 0.2
    ease 1.5 xpos 1.2

show sonia:
    xpos 0.8 ypos 0.5 zoom 0.15
    ease 1.5 xpos 0.75 zoom 1.0 ypos 1.0

show lance:
    ease 1.5 xpos 0.25 zoom 1.0 ypos 1.0

janine @talking2mouth "...Sonia?"

if (WonBattle("Sonia1")):
    sonia @sad "I... I won all my battles except one..."

else:
    sonia "I... I won all my battles..."

pause 1.0

janine @talking2mouth "Yeah. But you've got a lot more experience than everyone else."
janine @closedbrow talking2mouth "I wasn't expecting you to lose. I just need to know I can trust you again."

sonia frownmouth @talking2mouth "If you let me join the Team again, I'll prove to you that you can. I {i}promise.{/i}"

janine @closedbrow "{w=0.5}.{w=0.5}.{w=0.5}."

lance @closedbrow talking2mouth "Janine, I recommend you accept her. She was one of our top-performing battlers last year."

janine @talking2mouth "...I promised to let her try out. Nothing more."

lance @talking2mouth "You claimed she would be as a 'brand-new student' to you. Ignore your history."

janine @angry "Why are you pushing so hard to get her in?"

lance @talking2mouth "As I have said before. Her failure does not define her. It shows great courage to try again that which has once defeated you."
lance @angrybrow talking2mouth "I may well ask why you are pushing so hard to get Mr. [last_name] in."

janine @talking2mouth "His natural skill, Sir. I've explained this. If you were to just {i}give{/i} him a Dragonite, he would be practically unstoppable."

lance @talking2mouth "He has no talent. He has no experience. And his success comes not from effort, but from dumb luck."
lance @sad "All factors that another student with a month of training would make null."

red @talkingmouth "Wouldn't I be even stronger with another month of training, then?"

lance @angrybrow talking2mouth ".{w=0.5}.{w=0.5}.{w=0.5}You do not get to speak."
lance @sadbrow talking2mouth "It did not escape my notice you brought your Pikachu to this tryout. You may think you're making some sort of statement, some sort of nonsense about 'fighting with your friends.'"

pause 1.0

lance @angrybrow talking2mouth "All I see is {i}arrogance.{/i} You cripple yourself, and lessen your chances, and for what? To attempt to prove to me the strength of an objectively inferior member of an objectively inferior species?"

pause 1.0

red @talkingmouth "Yes."

pause 1.0

lance closedbrow "Hmph."

pause 1.0 

lance -closedbrow @talking2mouth "Janine, leave us be for a moment."

janine @talking2mouth "Remember what you said, Sir. You wouldn't harass my picks."

lance @talking2mouth "Is this boy getting into the Battle Team, then? Despite my advice?"

if (wins > 5):
    lance @talking2mouth "Even though his performance was only 'acceptable?'"
elif (wins > 3):
    lance @talking2mouth "Even though his performance was poor?"
else:
    lance @talking2mouth "Even though, by all rights, his performance should instantly disqualify him from consideration."

janine @sad "Well... yeah."

janine @talking2mouth "I mean, he's rough, but this skill he has with Pokémon... there's {i}nothing{/i} I wouldn't give to get my hands on that."

lance @talking2mouth "Then let me say one more thing. To him. Alone."

janine sad "Sir..."

pause 1.0

janine @closedbrow talking2mouth "Fine. Just don't be too harsh on him."

redmind @sad "...Aw, man."

hide janine
hide sonia
with dis

show lance:
    ease 2.0 xpos 0.5

pause 2.0

lance @talking2mouth "So. It would seem I have failed to keep you out of my Battle Team."

red @talking2mouth "It would seem so, Sir."

pause 1.0

lance @closedbrow talking2mouth "People react to failure differently. Some admit they will never succeed. Some believe that success was impossible. Some blame others, or their situation. And some try again."

red @talking2mouth "Given what I know about your league attempts, I'm guessing you're in the 'try again' category?"

lance @talking2mouth "Hear me, [first_name]. You are young, foolish, have had everything handed to you, and have not yet tasted defeat."

red @talkingmouth "Hey, I--"

lance @talking2mouth "{i}True{/i} defeat. Not just 'losing a battle,' or 'failing a test.' But failing to fulfill a long-term goal. A {i}dream.{/i}"
lance @talking2mouth "When you do, it will break you, as a meteor does the earth. It will shatter your hopes and ambitions. You will want to cry, and hide, and separate yourself from anyone who knew your dream."

red @angrybrow talking2mouth "And then you'll be happy?"

lance closedbrow @talking2mouth "No."

pause 1.0

lance @talking2mouth "Then I may finally respect you."

pause 2.0

red @angrybrow talking2mouth "Frankly, Sir, I'm not sure that I want the respect of someone who steals cookies from a Pikachu, or yells at a new student in front of a massive crowd."

lance @sad "Your arrogance tires me. I take my leave of you."

hide lance with dis

pause 2.0

stop music fadeout 2.0

redmind @frownmouth "...Ugh. I'm exhausted. I thought maybe I'd have enough energy to do something after this, but... no way. I'm going {i}straight{/i} to bed."

show blank2
show night at vspaz
with dis

pause 2.0

scene dorm_B lightsout with splitfade

play music "audio/music/littleroot_start.ogg" noloop
play music "audio/music/littleroot_loop.ogg"

show ethan at night, leftside with dis 
show hilbert at night, rightside with dis

ethan @talkingmouth "Hey, man."

red night @talkingmouth "Hey, guys. That was something, huh?"

if (WonBattle("Ethan1")):
    ethan @sadbrow talkingmouth "Yeah. Would've been nice to have won a battle, though."

    red @surprised "You didn't win {i}any{/i} of your battles?!"

else:
    ethan @sadbrow talkingmouth "Yeah. Would've been nice to have won more than one battle, though."

    red @surprised "Wait, you didn't beat anyone besides me?!"

ethan @sad "Nah. At least I tried, though. Would've been worse if I'd never figured out how strong I was, right?"

ethan frownmouth @sad "I guess the answer's 'not enough.'"

pause 1.0

hilbert @talkingmouth "I didn't do as well as I would have liked, either."

red @talkingmouth "Huh? How many wins did you get?"

hilbert @closedbrow talking2mouth "Five. Only five. The sixty-sixth percentile."

red @surprised "Really? I'm surprised. You had such a solid strategy, though."

hilbert @angry "I {i}did{/i}... before Janine shot me in the kneecap with that absurd ruleset."

pause 1.0

red @sadbrow talking2mouth "...Sorry, Hilbert."

hilbert @talkingmouth "...I don't know what to do. This doesn't affect my dream, but I had always assumed I would get on the Battle Team. I planned around it. And now...?"
hilbert @sadbrow talkingmouth "Now what?"

pause 1.0

hilbert @sadbrow talkingmouth "Aurea wouldn't want to see me like this. She'd just tell me to keep my chin up and hope. But... the evidence against me is..."

pause 1.0

red @confused "Aurea?"

hilbert @talkingmouth "My guardian. She's a well-known Pokémon Professor in Unova."

ethan @talking2mouth "So... Hildella's not your legal guardian?"

hilbert @sadbrow talkingmouth "I truly hope you're joking."

hide hilbert with dis

ethan @talking2mouth "...Yeah, man. I am."

hide ethan with dis

show blank2 as blank_A with transeye

pause 1.0

redmind @frownmouth "...Lance may have had a point. Everything feels like it's coming too easily to me, doesn't it?"
redmind @thinking "I'm doing well on my Student Council campaign, without having seriously tried." 
redmind @thinking "I got into the Battle Team, with a skewed ruleset that was obnoxiously in my favor."
redmind @thinking "Even getting into Kobukan was..."

pause 1.0

redmind @thinking "Everyone around me is trying so hard to make their dreams come true. But I don't even need to try."
redmind @thinking "Of course, I study, and I train, but none of that has mattered. It all just... {i}happens{/i}."
redmind @thinking "And I think it's all because of Frienergy."

pause 1.0

redmind @thinking "I wonder if Sam..."

pause 1.0

redmind @frownmouth "I wonder if Oak knows how to get rid of it?"

call clearscreens from _call_clearscreens_61

jump day010420