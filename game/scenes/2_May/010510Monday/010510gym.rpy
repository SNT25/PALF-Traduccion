label gym010510:

play music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

$ renpy.transition(dissolve)
show screen currentdate

scene gym with dis

show blank2 behind gym

$ renpy.pause(2.0, hard=True)

hide blank2

show alder with dis:
    xpos 0.66

show bruno think with dis:
    xpos 0.33

alder @happy2 "Good morning, everyone! Good to see you all back in classes again. We missed you!"

pause 1.0

alder @talking2mouth "Didn't we, Bruno?"

bruno norm3 @norm4 "I am glad to see my students again. You all look fit and ready to train."

hilda uniform @happy "Hell yeah! Let's break some heads!"

bruno @norm4 "That is the spirit. First, though, Alder and I must deliver a lecture."

alder @happy2 "Right you are, Bruno. Today, we're going to be learning about item manipulation."
alder @talkingmouth "Can anyone tell me what the rules are for items in most regions?"

misty uniform @talkingmouth "I can. You're allowed to remove any item the opponent is holding, as long as it's not in a special category. Moves like Knock Off or Trick can be used to do that."

alder @happy2 "Makes sense that the Cerulean scion would know this."

misty @sadbrow talkingmouth "...Right."

alder @talkingmouth "You're doing well, Misty. Carry on."

misty @talkingmouth "U-um... right. Well, the special categories are Mega Stones and Z-Crystals. There are also some other items that power up specific species."
misty @closedbrow talkingmouth "You're not allowed to touch those in battles. If a Pokémon loses possession of them during the fight, due to dropping it, or something like that, the battle is paused for the Pokémon to regain possession of the stone."

alder @happy2 "Exactly correct!"
alder @talkingmouth "...However, we do the exact {i}opposite{/i} in Kobukan."

flannery uniform @surprised "Huh? But in the Lavaridge Gym, we..."

alder @talkingmouth "Yes, in Kobukan, items can be removed at your leisure. If you can take a Mega Stone from a Pokémon, you can even prevent them from Mega Evolving!"

bruno norm @norm2 "This is dishonorable."

alder @happy2 "But {i}effective!{/i}"

redmind uniform @thinking "I'm not sure how effective it'd be, actually... that one Lopunny didn't need a Mega Stone, after all..."

if ("ForeveralsFiguredOut" in persondex["Professor Oak"]["Events"]):
    redmind @thinking "And it wouldn't work on me, at all. The Foreverals seem to generate an endless stream of Mega Stone-like objects for my Pokémon."

    redmind @happy "Shame they only last until the end of the battle. If they lasted longer, I could sell them!"

elif ("ForeveralsALittleBit" in persondex["Professor Oak"]["Events"]):
    redmind @thinking "Besides, if I'm understanding these gems right, the Foreverals seem to generate an endless stream of Mega Stone-like objects for my Pokémon."

    redmind @happy "Shame they only last until the end of the battle. If they lasted longer, I could sell them!"

alder @talkingmouth "Anyway, the basic thing we're trying to impart here is that the rules of many other regions don't necessarily apply here."

alder @talkingmouth "You may have also noticed that in this region, Pokémon are allowed to be sent out immediately after another faints."

hilbert uniform @sadbrow talkingmouth "'Allowed to'? You mean they {i}have{/i} to be, to take incoming hits."

alder @closedbrow talking2mouth "You could choose to see it that way. You could also choose to see it as an opportunity to switch in a Pokémon with Storm Drain, or Lightning Rod, or Intimidate, in the middle of your turn."

hilbert @angry "If I wanted to do {i}that{/i}, I'd just use a Pokémon with U-Turn, first."

alder surprised @sad2 "Alright, Hilbert. Tell me when your Honedge learns U-Turn."

hilbert @sadbrow talkingmouth "As long as you tell {i}me{/i} when my Cubchoo gets Intimidate."

pause 1.0

alder -surprisedbrow -frownmouth -surprised @closedbrow happymouth "Ah, it's good to be back in class, isn't it, Bruno?"

bruno happy @happy2 "Very much so."

alder @talkingmouth "Anyway, to wrap up this lecture on items, remember that you get back any item you started with at the end of each battle."
alder @happy2 "Except berries, of course."

pause 0.5

alder @talkingmouth "Now, why don't we start off with some battles?"
alder @closedbrow talkingmouth "Our unit this week will be triple battles." 

hilda @angrybrow talking2mouth "Hell yeah!"

alder @happy2 "Nice enthusiasm, Hilda! As you all must know, the range of your moves matters more in this format than in any other!"
alder @talkingmouth "Bruno, the assignments?"

bruno @think "Hm."

pause 0.5

show bruno:
    ease 0.5 ypos 1.2 zoom 1.3

pause 0.5

bruno norm3 @norm4 "Welcome back, Mr. [last_name]."

red @happy "Good to {i}be{/i} back."

bruno norm @norm2 "You will be battling Miss Jasmine."

hide bruno 
hide alder
with dis

show jasmine uniform with Dissolve(2.0)

jasmine @sadeyebrows talkingmouth "Hello, [first_name]."

red @talkingmouth "Hey, Jasmine. I don't think I've seen you in this class very often?"

jasmine @closedbrow talking2mouth "No, I often get an exception for this class... and I can barely do the physical training anyway."

red @happy "Hey, all a trainer really needs to train is their voice."

jasmine @surprised "No, no, not at all! A good trainer should be able to run around with their Pokémon. Follow them in battle, and move around the field to get a better vantage point and view of the battlefield!"
jasmine @closedeyes angryeyebrows talking2mouth "And, of course, a trainer should be fast enough on their feet to avoid any stray moves... the best trainers are the trainers who stay closest to their Pokémon in battle."
jasmine @happy "Only when you're standing side-by-side with your Pokémon can you see how they should react to your opponent's moves."

pause 1.0

jasmine @closedbrow talking2mouth sweat "Of course... I say all that, but have difficulty really {i}practicing{/i} it. I certainly can't run around the field with them."

red @sadeyebrows talkingmouth "I'm sure they appreciate the thought."

jasmine @closedbrow talkingmouth "Well, my Pokémon are very slow. So, at the least, I can stand by their side in battle."

red @surprised "Wait, you do that? Isn't that dangerous?"

jasmine @happy "Absolutely. But putting oneself in danger to bolster one's friends is a very noble calling, I think."

red @happy "You really never stop impressing me."

pause 1.0

jasmine lightblush @talkingmouth "I... was impressed by your speech on Friday."

red @surprised "Huh?"

jasmine @sad2eyes talkingmouth "I actually thought... well, I thought the extent of your power was greater than it was. Grusha convinced me otherwise, though."
jasmine @talkingmouth "But hearing you tell everyone the truth, unafraid of the consequences, of people's judgement... I thought that was very brave."

menu:
    "Not as brave as you.":
        $ AddEvent("Jasmine", "NotAsBrave")
        show jasmine surprisedbrow frownmouth with dis

        pause 0.5

        $ ValueChange("Jasmine", 1, 0.5)

        jasmine happy "Oh, please. I'm not brave at all. I simply have no other choice than to act the way I do."

        jasmine @talkingmouth "Now, shall we battle?"

    "Thank you.":
        $ AddEvent("Jasmine", "ThankYou")
        jasmine happy "No, thank {i}you{/i}. Now, shall we battle?"

    "Tell 'Grusha' thanks for me.":
        $ AddEvent("Jasmine", "TellGrushaThanks")
        jasmine @talkingmouth "I certainly will. Now, shall we battle?"

python:
    trainer1 = MakeRed(3)
    trainer2 = MakeTrainer("Jasmine", number=3)

call Battle([trainer1, trainer2], uniforms=[True, True], custombrain=jasminebrain1) from _call_Battle_118

$ battlehistory["Jasmine1"]  = _return

show alder
show bruno think at leftside
show jasmine uniform at rightside
show screen currentdate
with dis

play music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

if (WonBattle("Jasmine1")):
    $ ValueChange("Jasmine", 3, 0.75, False)

    jasmine @happy "Splendidly done."

    red @surprised "That was pretty tricky! You really made me work for it."
    red @talkingmouth "I really wasn't expecting to see a Steelix coming out of that Poké Ball. What's the story there?"

else:
    jasmine @talkingmouth "Ah... perhaps I went in a bit too hard?"

    red @happy "No, no, that's great! I just wasn't expecting such tough Pokémon so early. Especially that Steelix. What's the story there?"

jasmine @talkingmouth "Not much story to share, I'm afraid. I had access to a Metal Coat, and thought my partner Onix might look rather good in it."
jasmine @happy "Oh, I'd love to get my hands on a Steelixite... but that's a pursuit for the future."

menu:
    "Well, how'd you get an Onix?":
        $ AddEvent("Jasmine", "BrendanConnection")

        jasmine @talkingmouth "Oh? Well, a friend of mine from Johto helped me catch it, a good many years ago."
        jasmine @talkingmouth "Brendan's his name. By coincidence, he actually goes to {i}this{/i} school too."
        jasmine @sweat happy "I offered it to him, since he likes Ground-types, but... ah... he said it was, quote, 'filthy and far too rugged.'"

        red @surprised "Huh? I know Brendan. He was my roommate until recently. That doesn't sound like him at all."

        jasmine @talkingmouth closedbrow "Well, he was only an elementary-schooler at the time. People change. One thing that {i}hasn't{/i} changed is his devotion to Pokémon contests."
        jasmine @talkingmouth "He got me into them, actually."

    ">Stay silent":
        jasmine @talkingmouth "I'm sure that would help my Steelix truly shine in contests. A well-timed Mega Evolution can turn the judges in your favor like nothing else."

red @talkingmouth "Oh, you do contests, too? With that cracked team, I figured you would be on the trainer course."

jasmine @talkingmouth "I'm exploring my options. The only thing that doesn't seem to be on the table right now is, well, Student Council member."

red @sadbrow talking2mouth "...I'm sorry about that."

jasmine @talkingmouth "You've nothing to apologize for. This was just a terrible misunderstanding."
jasmine @sad2eyes talking2mouth "I'm concerned for Cheren, though. What he did was ill-advised, but it seems he's more interested in punishing himself than actually making things right..."

red @sad2eyes angryeyebrows frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

jasmine @sadbrow talkingmouth "...I know it would be easy to hate him. But hate never helps one move forward."

red @closedeyes angryeyebrows talking2mouth "I'm still figuring out how I feel about him."

jasmine @talkingmouth "Alright. As long as--"

show alder surprisedbrow frownmouth
show bruno surprisedbrow frownmouth
with dis

show jasmine frownmouth sadbrow:
        xpos 0.75
        ease 0.2 rotate -40 ypos 1.5

pause 0.2

show gym with vpunch

pause 0.5

jasmine @talking2mouth "Gosh dang it."

red @surprised "Jasmine! Are you alright? Do you need to--"

jasmine @talkingmouth "No, no, I should be fine. My legs just... I'm quite tired... give me a moment to catch my breath."

show jasmine closedbrow sweat lightblush with dis:
    xpos 0.75
    ease 2.0 rotate 0 ypos 1.3
    ease 4.0 ypos 1.0

pause 4.0

jasmine @talkingmouth "Phew. Seems this battle took quite a bit out of me. I hope you don't mind if I..."

red @talkingmouth "No, of course not. Go ahead."

jasmine -frownmouth @happy "Thank you."

jump lunchtransition