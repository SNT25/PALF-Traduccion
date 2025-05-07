label gym010525:

stop music fadeout 1.5
queue music "Audio/Music/Gym_Start.ogg" noloop
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

alder @talkingmouth "...which is why it's important to practice your ability to determine a Pokémon's age at a glance."
alder @happy2 "If you can tell how much experience a Pokémon has, you can figure out how hard a Pokémon will fight."
alder @talkingmouth "But if you know {i}how experienced{/i} a Pokémon is, you can figure out {i}how{/i} it'll fight, which might be more important."

brendan uniform @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

alder @happy2 "Brendan! What's that sad face for?"

brendan @talking2mouth "Oh, it's nothing big. I just... ah, sorry, don't wanna disrupt or slow down the class or anything, but I'm {i}really{/i} not gettin' this."

bruno norm3 @norm4 "State your concerns."

brendan @talking2mouth "Sure. Uh, I just don't get how knowing a Pokémon's age helps us know how it'll fight."
brendan @happy "Sorry, I get that's the most basic part of what you're tryin' to explain."

alder @happy2 "Totally fine! I'm sure lots of other people would appreciate a further explanation, too."

menu:
    ">Agree":
        red uniform @happy "Yeah, I know I would."

        narrator "You hear a few murmurs of assent."

        $ ValueChange("Brendan", 1, 0.1)

        brendan @sadbrow talkingmouth "I know you're just sayin' that, but... thanks."

    ">Stay silent":
        narrator "You hear a few murmurs of assent."

alder @talking2mouth "Think back to my battle with Bruno last Friday. Did you notice anything in particular about how we fought?"

if (HasEvent("Alder", "Volunteer")):
    brendan @closedbrow talkingmouth "Yeah. Uh, Instructor Bruno moved around the battlefield a lot more, and he used his Pokémon's type advantages against you and [first_name]."
else:
    brendan @closedbrow talkingmouth "Yeah. Uh, Instructor Bruno moved around the battlefield a lot more, and he used his Pokémon's type advantages against you and Leaf."

brendan @talking2mouth "But you kinda just stood there, and sent out really powerful moves."

alder @happy2 "That's exactly right!"
alder @talkingmouth "And Pokémon are the same way."
alder @closedbrow talkingmouth "Younger Pokémon usually attack more quickly, and are less careful about spending their energy. Older Pokémon often prefer to line up precise, powerful, attacks that are guaranteed to hit."
alder @talkingmouth "These preferred battle-style preferences are often categorized in groups, called 'Natures'."
alder @happy2 "Of course, there's many other factors besides age--personality is a significant one--but even personality often changes with age."

pause 0.5

alder @talkingmouth "Anyway, does that help, Brendan?"

brendan @happy "Totally!"
brendan @sadbrow talking2mouth "But, uh... I got another question, though..."

alder @happy2 "That's what we're here for."

brendan @talking2mouth "How do we figure out the ages of Pokémon? Like, they all look the same, don't they?"

alder @talkingmouth "Not necessarily. It takes an experienced eye, though. Not even Pokédexes are accurate enough to determine age at a glance."
alder @talking2mouth "A lot of what you'll want to look for are the same sorts of things you'd look for in human beings--size is an indicator. Greying plumage or fur is a significant one."
alder @talking2mouth closedbrow "Scratching or chipping on teeth, horns, or scales..."
alder @happy2 "Oh, and for you Charmander fans out there, a lot of Fire-type Pokémon have exposed flames. On younger Pokémon, the flames tend to be larger, and redder. Older Pokémon have yellower, smaller, flames."
alder @talking2mouth "Bug Pokémon don't tend to live that long, ten to thirty years, depending on size. Though there are exceptions, like Volcarona, which can easily live longer than humans."
alder @closedbrow talking2mouth "...They don't always, though."
alder @talkingmouth "Most mid-size mammalian Pokémon, like Herdier or Raichu, live somewhere from thirty to fifty years. Dragons can hit a hundred, often more."
alder @closedbrow talking2mouth "These are just generalizations, of course. And it's worth noting that an unevolved Pokémon might be very old, or an evolved Pokémon may be very young."
alder @talking2mouth "'Experience', capital 'E', is a measure of their ability to use Pokémon Energy--Pokénergy--not life experience."
alder @happy2 "Only thing that can measure {i}that{/i} is a calendar!"

brendan @closedbrow talking2mouth "Uh-huh... okay. Does the lifespan of a Pokémon change when it evolves, then? Like, you said Raichu could live thirty to fifty years." 
brendan @talkingmouth "What about Pichu? A friend told me Pichu evolves into Pikachu, then Raichu, but, like, Pichu's way smaller, right? Does that mean evolving lets it live longer?"

alder @happy2 "Good thinking! Evolution does not seem to change the lifespan of a Pokémon, though. Even a Bagon, for example, could live over a hundred years, even if it never evolves."

brendan @happy "Thanks, Sir! That really helps a ton."

bruno @norm2 "Of course, there are some Pokémon where a visual assessment is simply not possible."
bruno @norm4 "Many Ghost-types do not ever visually change, nor do they age. Some Steel-types are similarly visually unchanging, though they {i}do{/i} age."

alder @talking2mouth "In cases like those, your best bet might really just be size. Almost all Pokémon get bigger with age, even if they don't... 'age.'"

brendan @talkingmouth "That's wild. Why do they get bigger, then, if they don't age?"

alder @closedbrow happymouth "Beats me! One of the Professors probably knows."

bruno @sad2 "Alder, We know this." 
bruno @norm4 "It's because an unaging Pokémon's maturity is connected to their accumulation of Pokémon Energy."
bruno @think2 "Since they are gathering more energy, it affects their physical body, too."
bruno @norm2 "Many martial artists and Pokémon train to allow their energy to influence their body, but for some Pokémon, it is a condition of their birth."

alder @talking2mouth "Oh, yeah, I think I heard about that once."
alder @talkingmouth "Wasn't there some {i}massive{/i} Haunter causing trouble in Kanto? It was, like, hundreds of years old, right?"

bruno @sad2 "'Black Fog'. Celadon City's darkest hour."
bruno @norm2 "Fortunately, the Pokémon was captured, retrained, and released."

alder @talking2mouth "Huh. How'd they catch it?"

bruno norm @norm2 "{size=30}...Massive Poké Ball.{/size}"

alder @happy2 "Come again?"

bruno @angry2 "We used a massive stone Poké Ball."

alder @happy2 "I {i}have{/i} to hear the logistics of this."

bruno @norm2 "I cannot share that. The creation of such an artifact of immense power is a closely-guarded secret. Agatha was the only one who knew exactly how it worked."

$ autoquote = False

alder @talking2mouth "\"Spoilsport. You got me all excited over the idea of catching an enormous..."
extend @surprised2 " Well, frankly, I'm not sure what I'd want to catch, but the novelty of using a {i}massive{/i} Poké Ball is something I'd like to try.\""

$ autoquote = True

alder @talking2mouth "Like those big balls they use in Galar. Think I could Dynamax up an entire garland of 'em at once?"

raihan uniform @happy "Hammerlocke Gym's open, if you want to give it a fair shot."

alder @happy2 "That's not a half-bad idea. Maybe I'll do that."

bruno @norm2 "I cannot begin to name the reasons why that won't work, but let us discuss this later. It's time for the battles."

alder @happy2 "Fair enough. Let's call 'em out."

bruno @norm2 "[first_name], your opponent today will be Calem."

hide bruno 
hide alder
with dis

pause 1.0

show calem uniform with dis

calem @talkingmouth "Good morning."

red uniform @talkingmouth "Hey. How are you?"

calem @talking2mouth "Can't complain."

$ autoquote = False

calem @talkingmouth "\"My dorm's been extraordinarily busy, recently, with May, Brendan, and Serena all preparing madly for that upcoming contest, the... {w=0.5}hm. "
extend @closedbrow talking2mouth "I'm afraid the name escapes me. I remember it was a mouthful, though.\""

$ autoquote = True

menu:
    "The Eon Ocean Water Gala Contest?":
        calem @closedbrow talking2mouth "No... I don't believe so."

    "The Millennium Drop Water Festival Contest?":
        show calem happy with dis

        $ ValueChange("Calem")

        calem -happy @talkingmouth "Oh, yes, that was it! Exactly. Sharp mind."

    "The Century Bubble Water Feast Contest?":
        calem @closedbrow talking2mouth "No... I don't believe so."

    "The Decade Ripple Water Fair Contest?":
        calem @closedbrow talking2mouth "No... I don't believe so."

calem @talking2mouth "Well, regardless of what it's called, my roommates are quite busy."
calem @sadbrow talkingmouth "I'm rather... ashamed of my comparative inaction, if I may confess such things to you."

red @talkingmouth "It's completely fine to just focus on your studying and training."

$ autoquote = False

calem @closedbrow talking2mouth "\"True. But I {i}did{/i} have plans to join the Student Council, and..."
extend @happy " didn't have a backup plan.\""

$ autoquote = True

calem @sadbrow talkingmouth "My own foolishness, of course."
calem @talkingmouth "Perhaps I'm still looking for my own niche."

red @happy "You'll find it, man."

calem @talkingmouth "I tried, briefly, tutoring Wally in our shared Fighting and Fairy electives... thought perhaps my Kobukan calling might be as a teacher."
calem @talking2mouth "Unfortunately, he seems... uncomfortable around me. Not an ideal situation for roommates to be in."

if (HasEvent("Wally", "ClassIntro") or HasEvent("Wally", "AdviceGiven")):
    calem @happy "He seems rather fond of you, though. Why, half of my aborted attempt at tutelage was just my own vain attempts at teaching him to imitate you."

    red @confusedbrow talking2mouth "Really? How did you do that?"

    calem @talking2mouth "Mostly stating his desire to be a champion and running around a lot."

    red @unamusedbrow unamusedmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    $ ValueChange("Wally", 1, 0.33)

    narrator "Your understanding of Wally goes up... in a direction you are not necessarily appreciative of."

if (wally_name != first_name):
    calem @closedbrow talking2mouth "On that note, is it true that you asked Wally to call you '[wally_name]'?"

    if (wally_name == "Senpai"):
        red @unamusedbrow talking2mouth "I did {i}not{/i} propose that name."

        calem @closedbrow talking2mouth "Noted."

    else:
        red @sweat closedbrow talking2mouth "I didn't think he'd actually do it..."

        calem @surprisedbrow talking2mouth "Oh, he {i}definitely{/i} does. Proudly. Seems to consider it a privilege."

        redmind @thinking "I'm... learning {i}so{/i} much right now."

calem @talkingmouth "Well, I imagine that's enough gab. Let's proceed with our battle."
calem @talking2mouth "I'd ask you to go easy on me, but..."

pause 1.0

calem @closedbrow talking2mouth "Frankly, my Flabébé has been an absolute brat recently, she requires some correction, and I am not equipped to deliver it."

red @closedbrow talking2mouth "Geez, Calem. You really need to get your Flabébé under control."

calem sadbrow talking2mouth "You are preaching to the choir, my dear [first_name]."

python:
    trainer1 = MakeRed()
    trainer2 = MakeTrainer("Calem")

call Battle([trainer1, trainer2], uniforms=[True, True]) from _call_Battle_160
$ RecordBattle("Calem3")

show calem closedbrow smilemouth uniform with dis

stop music fadeout 1.5
queue music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

if (WonBattle("Calem3")):
    $ ValueChange("Calem", 3)

    calem @talkingmouth "I'm not even surprised. Very well done, my friend."

    red uniform @happy "Aw! I want my battles to be fun {i}and{/i} surprising."

    calem -closedbrow @talking2mouth "Tragically, it appears we cannot get {i}everything{/i} we want."
    calem @happy "Though you've a good start."

else:
    calem @talking2mouth "That's rather surprising. Are you feeling off?"

    red uniform @talking2mouth "Might be a little bit. I missed lunch yesterday. Apparently, that's had {i}way{/i} more effect on me than I thought it would."

    calem -closedbrow @sadbrow talking2mouth "Oh dear, that's not good. If you're too busy to eat, I'm certain I could cook something for you."

    red @happy "Calem, I've had your cooking. And you {i}could not{/i} cook."

    calem @closedbrow talking2mouth "That's fair enough. Another thing my au pairs handled for me. I do intend to learn, at some point, but..."
    calem @talkingmouth "Well, I {i}must{/i} prioritize."

if (GetTrainerTeam("Calem", "Flabébé", False).GetHealthPercentage() <= 0):
    $ AddEvent("Calem", "PunishFlower")
    calem @closedbrow talking2mouth "On that note, thank you for your assistance in reprimanding my Flabébé."

    red @sadbrow talking2mouth "All I did was knock her out. She's going to be exactly the same once she gets her energy back."

    calem @closedbrow talking2mouth "So you say, but hope springs eternal."

red @closedbrow talking2mouth "By the way... shouldn't your Flabébé be a Floette by now?"

calem angrybrow -smilemouth "{w=0.5}.{w=0.5}.{w=0.5}."

red @surprised "Oh, geez, sorry, did I say something wrong? I wasn't, like, doubting your ability or anything."

calem @closedbrow talking2mouth "No, no, it's not that. You're quite right. She, by all rights, {i}should{/i} be."
calem @sadbrow talkingmouth "She simply... refuses to evolve. As a sort of power play over me."

red @confused "What? That can't be right."

calem @talking2mouth "I know that Pokémon are inherently good, but her actions really do seem to be... well, 'manipulative' is a strong word, but it rather fits."

pause 1.0

calem @closedbrow talking2mouth "...I cannot imagine what more she wants. I have given her all my attention, fair but effective training, the highest-quality food... and, increasingly, the last dregs of my sanity."

red @talking2mouth "I... know a lot about Pokémon, but I've never heard of something like this."

calem sadbrow @talking2mouth "I certainly did not expect {i}this{/i} to be the sort of lady troubles I'd have to deal with."

red @sadbrow talkingmouth "Stay strong, man."

hide calem with dis

pause 1.0

show alder:
    xpos 0.66
show bruno think:
    xpos 0.33
with dis

jump lunchtransition