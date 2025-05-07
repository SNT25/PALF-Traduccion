label day010529:

$ timeOfDay = "Morning"
call clearscreens() from _call_clearscreens_220
call calendar(1) from _call_calendar_54

$ calDate = calDate.replace(day=29, month=5, year=2004)

$ HealParty()

stop music

scene blank2
show reallyearlymorning at vspaz

pause 3.5

red swimsuithatless @closedbrow talking2mouth "Zzzz... {size=30}N-no, Mom... no more broccoli... it's in my teeth...{/size} zzz..."

$ PlaySound("airhorn.ogg")

pause 0.5

red @deadeyes angrymouth angryeyebrows "MOTHERFU--"

$ renpy.music.play("Audio/Pokemon/pikachu_angry3.ogg", channel="altcry", loop=None)

libpikachu angry2eyes glowing angrymouth "PIIIKA!"

show screen songsplash("Pallet Town", "Zame")
queue music "audio/music/palletpiano.ogg"

scene kitchen 
show leaf hatless flirtbrow:
    xzoom -1 xpos 0.2
show yellow closedbrow neutralhairdown: 
    xpos 0.6
show ethan:
    xpos 0.4
show blue angry:
    xpos 0.8
show screen currentdate
with vpunch

red @angry "Alright, who did that? Was it you, Blue?"

blue @angry "What the hell are you blaming me for? It was {i}her{/i}!"

leaf -flirtbrow @flirtbrow talking2mouth "Stop being so dramatic. It's only six-thirty."

ethan @closedbrow talkingmouth "This coming from the woman who doesn't get out of the shower until 7:45 every morning."

show blue frownmouth with dis

leaf @closedbrow talking2mouth "Look, I'm sure we'd all {i}prefer{/i} to be asleep right now, but we need to have a dorm meeting."
leaf @talkingmouth "And it's not {i}just{/i} a dorm meeting. It's also a Battle Team meeting."

yellow -closedbrow @surprised "Oh! Should I... leave?"

leaf @happy "Of course not, sweetie. You're one of us."

blue @surprised "Hey, did you do something with your hair?"

yellow @unamusedbrow talkingmouth "I... did nothing with it."

pause 1.0

blue @closedbrow frownmouth "Huh."

ethan @talkingmouth "Well, what is it? I was just doomscrolling on my phone, so you didn't actually wake me up, but it must be pretty serious to get {i}you{/i} up so early."

leaf @talking2mouth "Let me answer your question with a question, in the style of the inimitable Professor Oak."
leaf @talking2mouth "Who, in this dorm, has at least one Foreveral?"

red @confused "Uh... me."
ethan @talkingmouth "Yeah, and me?"
blue @closedbrow talkingmouth "Me."

pause 1.0

yellow @surprised "Oh! Me! Sorry. I forgot."

leaf @talkingmouth "Okay. I knew that one. Now, who in this dorm can {i}make{/i} Foreverals?"

red @closedbrow talking2mouth "That's me again."

blue @closedbrow talkingmouth "And me."
blue @surprised "Is there a point to this?"

leaf @talking2mouth "Two points, actually. We have two people here who can make Foreverals. Or, at least, their Pokémon can."
leaf @talkingmouth "Furthermore, of the five people who are known to have Foreverals in this school, not counting Professor Oak, four are in this dorm."

yellow @talkingmouth "Yes..."
yellow @surprised "Oh, are you saying you want one, too?"

leaf @sadbrow talkingmouth "Well, yes, but that's not the {i}main{/i} thing I'm saying."
leaf @winkbrow talking2mouth "Keep it in mind for future gift ideas, maybe, boys."

blue @happy "Fat chance!"

leaf @flirtbrow talking2mouth "Such a charmer."

leaf @talking2mouth "My point is that if Melody has Foreverals, then we know who gave them to her."

ethan @confused "Huh? Explain it to me like I'm slow."

yellow @talkingmouth "There are only five people who have Foreverals. You and I only have one. And if Blue and [first_name] didn't give Melody one, then..."

pause 1.0

red @confusedbrow talking2mouth "Sam."

blue @closedbrow talkingmouth "Bullshit."

red @sad2eyes talking2mouth "...C'mon. You know I love your grandpa, but who else could it be?"

blue @angry "Get creative! Maybe she just snuck into his lab and stole one! Or maybe she got one of those shards that Eevee ate, and fed it to her Wimpod or whatever!"

leaf @talking2mouth "Being fair, those {i}are{/i} all possibilities."

red @closedbrow talking2mouth "Yeah, I guess."

pause 0.5

ethan @talking2mouth "I mean... we could just ask him, right?"

pause 1.0

yellow @talkingmouth "Um... yes. Yes, that's right."

ethan @surprised "Shit, I said something {i}correct?{/i}"
ethan @happy "Hell yeah. That's my one for the week."

blue @talkingmouth "I'll do that today. He's been busy recently with lesson plans, and studying Eevee, but... "
blue @talkingmouth "It'll only take a couple of minutes to ask him that."

leaf @talking2mouth "Cool. Tell us what he says!"

pause 1.0

leaf @happy "Okay, second point of order!"

show yellow surprisedbrow frownmouth blush with dis

leaf @talking2mouth "Yellow, you should participate with [first_name] in the Millennium Drop!"

yellow @talkingmouth "{size=30}Ekkkk.{/size}"

red @talkingmouth "Uh... how do you figure?"

leaf @talking2mouth "Well, firstly, I kinda hate Phobos a little bit."

ethan @closedbrow talking2mouth "Same."

blue @closedbrow talkingmouth "Same."

leaf @flirtbrow talkingmouth "And I think it'd be {i}really{/i} funny if you beat his precious niece in the thing she's best at."

red @sadbrow talkingmouth "I've never seen her perform, but I kinda get the feeling that it's not as simple as signing up for the contest."

leaf @talkingmouth "You beat her in a battle. How hard can beating her in a contest be?"

yellow @sadbrow talkingmouth "Um... much harder. Contests test the Coordinator's sense of rhythm, sense of style, their ability to sing, their ability to coordinate their actions with their Pokémon, their... their..."
yellow @angrybrow talkingmouth "It's not like a battle. There's a lot more factors!"

leaf @happy "And that's why you should team up with [first_name]! He's got the Pokémon know-how, and you have the contest knowledge!"

yellow -surprisedbrow -frownmouth -blush frownmouth @sadbrow talkingmouth "I don't! I barely know anything! I've just watched a couple of their meetings the past few days! I was going to stop, now that... {cps=20}now that...{/cps}"

pause 0.5

blue @wistfulbrow talkingmouth "Now that what?"

yellow @sadbrow talkingmouth "I was going to say... now that Blue's back."

pause 0.5

blue @closedbrow talkingmouth "So, because I'm back, you're going to stop doing something you find fun?"

yellow @sad2eyes talkingmouth "Well... I don't {i}need to{/i}, anymore..."

blue @closedbrow talkingmouth "God. I don't know where you got this dumbass idea that just because I want to do something, we can't also do that shit you want to do."
blue @wistfulbrow talkingmouth "Like, if you want to drag me to watch some girls dancing around in skirts every once in a while, I could choke down the bile, probably."

yellow -frownmouth @happy "Oh, Blue. That's so kind of you."

blue @angry "Don't make a big thing out of it!"

leaf @talkingmouth "Also... when we played Inferno & Logos, you got really into it, Yellow. Like, you acted out all the parts and everything. Isn't acting a Coordinator skill? And you've been doing this for years, right?"
leaf @closedbrow talkingmouth "It's something to consider."

yellow @sadbrow talkingmouth "I appreciate it, but... I've {i}never{/i} coordinated before. Neither has [first_name]. We wouldn't have any chance at all."

ethan @talkingmouth "Just like [first_name] had no chance against Daybreak's Altaria?"

pause 1.0

leaf @surprised "Damn. You're on a roll today."

ethan @closedbrow talking2mouth "You guys probably {i}aren't{/i} getting to the top, yeah. I'll admit that. I mean, you'd have to go against Brendan and April, and they've been doing this their whole lives."
ethan @talking2mouth "But it might be worth asking around, just for more details, right? Like, consider this a sidequest."

yellow @sadbrow talking2mouth "I'm sorry... I really can't. I'm just not... I'm not a Coordinator. I'm not one of {i}them.{/i}"

pause 1.0

show blue angry
show leaf angry
show yellow frownmouth
with dis

ethan @closedbrow talking2mouth "Not a battler, not a coordinator... what are you, then?"

yellow @angrybrow talkingmouth "I'm a nurse."

pause 1.0

show blue -angry
show leaf frownmouth
with dis

ethan @sadbrow talkingmouth "That's fair. Sorry. I won't push this any further."

yellow @talkingmouth "...It's alright."

blue @closedbrow talkingmouth "Well, since we're all up already, I'll go talk to Gramps, and see if he gave Melody that rock."

leaf @talking2mouth "Yeah. And [first_name], maybe you should ask around about the Millennium Drop? I mean, this is a way you could pay for school."

red @closedbrow talking2mouth "It {i}is{/i} tempting."

menu:
    "[knowledgeoption]Learning more about it can't hurt.":
        $ TraitChange("Knowledge")

    "[witoption]Frienergy might help a lot in contests, actually.":
        $ TraitChange("Wit")

leaf @talking2mouth "Yeah. And you make friends like a baker makes bread--I bet a bunch of the Coordinator Club girls (and Brendan) have already talked to you about Coordinating."
leaf @happy "You might know more than you think!"

red @closedbrow talking2mouth "Hm..."

leaf @happy "Alright. That's that, then. Split!"

scene blank2 with splitfade

pause 1.0

$ coordinating = True

narrator "The Millennium Drop Water Festival Contest is being held on June 12th, [bluecolor]two weeks{/color} from now."
narrator "From now until then, every mood increase you gain with a member of the Coordinator Club will increase your [contestcolor]Coordinating Knowledge{/color}."
narrator "Additionally, spending time with Instructors who are accomplished Coordinators will also increase your [contestcolor]Coordinating Knowledge{/color}."
narrator "If you wish to join the Millennium Drop, you should spend this weekend gathering information about it, before you need to make a decision on Monday."
narrator "You can view your current [contestcolor]Coordinating Knowledge{/color} on the stats page, near your traits."

if (HasEvent("Klara", "AcceptCoordinatorClub")):
    narrator "For viewing the Coordinator Club meeting on Tuesday... your [contestcolor]Coordinating Knowledge{/color} went up by fifty points!"
    $ coordinatingknowledge += 50

if (GetRelationshipRank("May") > 0):
    $ coordinatorpointsup = 10 * GetRelationshipRank("May")    
    $ coordinatingknowledge += coordinatorpointsup
    narrator "For your close relationship with May... your [contestcolor]Coordinating Knowledge{/color} went up by [coordinatorpointsup] points!"

if (GetRelationshipRank("Misty") > 0):
    $ coordinatorpointsup = 10 * GetRelationshipRank("Misty")
    $ coordinatingknowledge += coordinatorpointsup
    narrator "For your close relationship with Misty... your [contestcolor]Coordinating Knowledge{/color} went up by [coordinatorpointsup] points!"

if (GetRelationshipRank("Brendan") > 0):
    $ coordinatorpointsup = 10 * GetRelationshipRank("Brendan")
    $ coordinatingknowledge += coordinatorpointsup
    narrator "For your close relationship with Brendan... your [contestcolor]Coordinating Knowledge{/color} went up by [coordinatorpointsup] points!"

if (GetRelationshipRank("Serena") > 0):
    $ coordinatorpointsup = 10 * GetRelationshipRank("Serena")
    $ coordinatingknowledge += coordinatorpointsup
    narrator "For your close relationship with Serena... your [contestcolor]Coordinating Knowledge{/color} went up by [coordinatorpointsup] points!"

if (GetRelationshipRank("Dawn") > 0):
    $ coordinatorpointsup = 10 * GetRelationshipRank("Dawn")
    $ coordinatingknowledge += coordinatorpointsup
    narrator "For your close relationship with Dawn... your [contestcolor]Coordinating Knowledge{/color} went up by [coordinatorpointsup] points!"

if (GetRelationshipRank("Tia") > 0):
    $ coordinatorpointsup = 10 * GetRelationshipRank("Tia")
    $ coordinatingknowledge += coordinatorpointsup
    narrator "For your close relationship with Tia... your [contestcolor]Coordinating Knowledge{/color} went up by [coordinatorpointsup] points!"

if (GetRelationshipRank("Jasmine") > 0):
    $ coordinatorpointsup = 10 * GetRelationshipRank("Jasmine")
    $ coordinatingknowledge += coordinatorpointsup
    narrator "For your close relationship with Jasmine... your [contestcolor]Coordinating Knowledge{/color} went up by [coordinatorpointsup] points!"

if (GetRelationshipRank("Klara") > 0):
    $ coordinatorpointsup = 10 * GetRelationshipRank("Klara")
    $ coordinatingknowledge += coordinatorpointsup
    narrator "For your close relationship with Klara... your [contestcolor]Coordinating Knowledge{/color} went up by [coordinatorpointsup] points!"

if (HasEvent("Instructor Wallace", 2) > 0):
    $ coordinatorpointsup = classstats["Water"]
    $ coordinatingknowledge += coordinatorpointsup
    narrator "For your experience in Instructor Wallace's class... your [contestcolor]Coordinating Knowledge{/color} went up by [coordinatorpointsup] points!"

if (HasEvent("Instructrice Fantina", 2) > 0):
    $ coordinatorpointsup = classstats["Ghost"]
    $ coordinatingknowledge += coordinatorpointsup
    narrator "For your experience in Instructrice Fantina's class... your [contestcolor]Coordinating Knowledge{/color} went up by [coordinatorpointsup] points!"

call freeroam() from _call_freeroam_34 

call freeroam() from _call_freeroam_35

call freeroam() from _call_freeroam_36

stop music fadeout 1.5

show screen songsplash("Pallet Town", "Zame")
queue music "audio/music/palletpiano.ogg"

scene suitenight 
show leaf hatless:
    xpos 0.66
show klara makeup hairpin:
    xpos 0.33 xzoom -1
show screen currentdate
with splitfade

red @surprised "Oh, hey! Klara, what's up?"

klara @happy "Oh, hiiii, [first_name]! I was just chatting with Leaf about you. {i}I{/i} only said good things, don't worry!"

leaf @talkingmouth "Welcome back. Learn anything good today?"

show klara surprisedbrow frownmouth with dis

red @talkingmouth "Enough. I learned there's preliminaries on Wednesday. But the bigger thing is that I learned that my only chance of getting into the Millennium Drop is probably to team up with someone." 
red @happy "So you were pretty pre-scientific, this morning."

leaf @closedbrow talking2mouth "I think you mean prescient. But... hm. that makes things a bit trickier, if Yellow isn't--"

klara -surprisedbrow -frownmouth -surprised @happy "Tricky?! No, this is fantastic! I know exactly what we can do!"

leaf @talkingmouth "Really? Great! Lay it on us."

klara @talkingmouth "You can just partner up with me, [first_name]. My routine is, like, totally scalable. Works with one person, or two, or three, or whatever!"

red @sadbrow talkingmouth "That's a nice offer, but... I don't think I can. I'm pretty sure I'd just drag you down."

klara @puppybrow talking2mouth "What? No! No way... did someone tell you that you couldn't do it? Don't listen to toxic people like that."

show klara:
    xpos 0.33 ypos 1.0 zoom 1.0
    ease 0.3 xpos 0.5 ypos 1.2 zoom 1.3

klara @talkingmouth "You and I are unbeatable! You don't need to listen to what {i}anyone{/i} else says. We can totally do this together!"

if (GetRelationshipRank("Klara") > 0):
    klara @puppybrow happymouth "After all... {size=30}we already have a connection...{/size}"

red @closedbrow talking2mouth "I think I need some more time to think about it. But I'll let you know on Monday, alright?"

show klara surprisedbrow frownmouth with dis

pause 1.0

klara -surprisedbrow -frownmouth @happy "Of course! But, for the record, teaming up with a partner is a {i}really{/i} good idea, especially for beginning Coordinators."

show klara:
    xpos 0.5 ypos 1.2 zoom 1.3
    ease 0.5 xpos 0.33 ypos 1.0 zoom 1.0

pause 1.0

leaf @sadbrow talkingmouth "So..."

klara @talkingmouth "Oh, it's alright, you don't have to tell me to go. I get it."
klara @sadbrow talking2mouth "Bye, [first_name]. I'd love to talk more, but... you know. I guess I need to go."
klara @happy "Text me!"

hide klara with dis

leaf @closedbrow talkingmouth "Hey. Thanks for the save."

red @confused "Was there something wrong?"

leaf @happy "Not really? I just... asked Klara for some information about the Millennium Drop, like, five hours ago, and..."
leaf @closedbrow talking2mouth "Well, she didn't really seem to know a lot. About the Millennium Drop, or... {w=0.5}well, nevermind. I'm sure I just didn't get it."
leaf @talking2mouth "Anyway, it sounds like you're going to make a final decision on Monday?"

red @talkingmouth "Guess so."

leaf @happy "Alright!"
leaf @talkingmouth "That reminds me, Blue came back earlier. Said that Professor Oak swore up and down that he hadn't given Melody a Foreveral."
leaf @sadbrow talking2mouth "Although... Blue also mentioned that Professor Oak didn't seem quite sure, as the conversation was ending."

red @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

red @closedbrow talkingmouth "Alright. Well, the only thing we can do right now is believe him."
red @sadbrow talkingmouth "And even if he did give Melody a Foreveral... I mean, that's his right. I gave some to him, to do whatever he wanted with. So he can do whatever he wants with 'em."

leaf @sadbrow talkingmouth "I'd be a lot more willing to accept that if it didn't possibly mean losing you."

pause 0.5

leaf @closedbrow talkingmouth "As a friend, of course."

red @closedbrow talkingmouth "Of course."

call texting() from _call_texting_30

jump day010530



label nooncontestintermission:

scene concerthall 
show jasmine:
    xpos 0.33 xzoom -1
show brendan:
    xpos 0.66
show screen currentdate
with splitfade

brendan @talking2mouth "...Don't know. Feel like a high-kick {i}after{/i} the twirl would be better. 'Cause, like, the judge's'll be expecting me to do the twirl after, right?"

jasmine @closedbrow talkingmouth "Yes... that's how that routine is typically performed."
jasmine @happy "The classicality of a routine is not necessarily a reason to discount it outright, though, no?"

brendan @talkingmouth "I dunno. Kinda feel like we need to {i}really{/i} stand out if we wanna bag the Millennium Drop, you know? Liz isn't running us hard for nothing."

jasmine @sad2brow talkingmouth "Yes... I only wish I could keep up."

brendan @sadbrow talking2mouth "Hey, Jaz. You're doing fine. Liz knows you need a break every once in a while. She's not holdin' that against you."

jasmine frownmouth @closedbrow sweat talking2mouth "Perhaps, but I cannot help but get the awful feeling she is merely {i}tolerating{/i} my presence on the team."

brendan @surprised "What? Why'd you say that?"

jasmine @sadbrow talkingmouth "She provides Dawn {i}a lot{/i} of advice and pointers."

brendan @closedbrow talking2mouth "Well, yeah. Dawn's her favorite."

jasmine @talkingmouth "True. Even so, she also provides you with a lot of advice. Corrections, too."

brendan frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

brendan @talking2mouth "And you're sayin' she doesn't do that for you?"

jasmine @sad2brow talkingmouth "I'm afraid not... I know I'm not doing perfectly, but it may be she thinks I cannot improve, so there is no point in trying to correct me..."

pause 1.0

brendan sadbrow @talking2mouth "Jaz. No-one's doin' this perfectly. You know, in the Sootopolis Miracle Sparkle Massive Show Contest (SMSMSC), Wallace stepped on his own foot and fell down."
brendan @happy "You know, {i}Champion{/i} Wallace! {i}World Coordinator Champion{/i} Wallace!"
brendan @talking2mouth "Liz's real skilled at Coordinatin', but I think Wallace was better back in the day. So if Wallace is fallin', Liz did too, I bet."

pause 0.5

brendan -frownmouth -sadbrow @talkingmouth "You don't need to be perfect, Jaz. You just gotta be better than you were yesterday. Don't try to impress Liz, just make yourself proud."

pause 1.0

jasmine -sadbrow -frownmouth @talkingmouth "It is so interesting how you have changed from when I knew you in Olivine."

brendan @closedbrow talking2mouth "Man, when I think about what a brat I was back then... I'm sorry, Jaz, I was a real prick, huh?"

jasmine @closedbrow talkingmouth "Not at all. My precious Steelix came from you, when it was only an Onix, after all."

brendan @sadbrow talking2mouth "Yeah, but... that's only 'cause I didn't want to use ugly Pokémon..."

jasmine @closedbrow talkingmouth "...Whatever your reasons, I can assure you that Steelix does not hold a grudge."

brendan @sadbrow talking2mouth "Thanks, Jaz."

pause 1.0

jasmine @surprised "Oh! Look who is joining us."

red @happy "Hey, Jasmine! Hey, Brendan."

brendan @talkingmouth "Hey, bro."

jasmine @talkingmouth "To what do we owe this pleasure?"

if (GetRelationshipRank("Jasmine") > 0):
    jasmine @sadbrow talkingmouth "If you've come to ask about that business on the dock... I'm afraid I haven't made any progress in that regard, yet."

    jasmine @happy sweat "I truly swear it was my first intention, but I've just been so busy with the Coordinator Club!"

    red @happy "It's cool. I get it."

    $ ValueChange("Jasmine", 1, 0.33)

    red @talking2mouth "Anyway, that's not what I wanted to ask about."

red @talkingmouth "You guys are in the Coordinator Club, right? I was hoping you could tell me more about the Millennium Drop."

brendan @talking2mouth "Huh? Oh, sure."
brendan @closedbrow talking2mouth "It's, uh, based on an old Hoenn festival, I think. There was some star Pokémon that only came around every thousand years, and so people sang songs to make it wake up."
brendan @happy "And I guess the singin' to the star Pokémon eventually turned into a contest people just do every year, for fun!"

jasmine @talkingmouth "Your knowledge of contests is very vast, Brendan."

brendan @talkingmouth "Don't know much, but I'm pretty confident in what I {i}do{/i} know."

jasmine @talkingmouth "The contest will be taking place on the twelfth, so, two Saturdays from now."
jasmine @talkingmouth "The top three winners, I believe, will be awarded a scholarship and a ribbon."

brendan @talkingmouth "And the first-place winner will get the Millennium Cup. It's a big fancy trophy with this crystal on top of it."

red @talkingmouth "I getcha. I knew most of that, I think. What are the requirements for entry?"

brendan @talking2mouth "Nothing much. You don't even have to be a member of the Coordinator Club, though if you aren't, it's pretty unlikely that you'll be good enough to pass the preliminaries."

red @confused "Preliminaries?"

jasmine @talkingmouth "Next Wednesday, there will be a series of mock Contests in front of the judge panel--that's when they'll be officially announced."

brendan @closedbrow talkingmouth "But everyone already knows it'll be Fantina, Champion Wallace, and that new crippled guy."

jasmine @sad2brow talking2mouth "...Um."

brendan sadbrow frownmouth @surprised "Oh, shi-I'm sorry, Jaz, I didn't mean it like that! I mean, you and him are completely different. I don't even think of you like... y'know. It's just--that guy's an asshole!"

jasmine @sadbrow talkingmouth "I understand. But there are plenty of other qualities of his that we could use to derogatorily refer to him instead, yes?"

brendan -sadbrow -frownmouth @sadbrow talking2mouth "...Right. Sorry."

jasmine @happy "No harm done."
jasmine @talkingmouth "Anyway, [first_name], the preliminaries happen on Wednesday, and if you cannot show the judges a good performance, then you aren't able to participate in the Millennium Drop proper."

red @closedbrow frownmouth "Hm..."

brendan @talking2mouth "Dude, are you thinking of joining?"

red @confused "Maybe? I'm kinda just trying to figure out how this works, for now."

jasmine @talkingmouth "Well... it would be lovely if you were able to join, but it tends to be pretty competitive."
jasmine @sadbrow talkingmouth "I don't doubt your ability, of course, but if this is something you've only just gained an interest in..."

brendan @talkingmouth "Maybe if he were to team up with someone?"

jasmine @surprised "Oh! Yes, that might work."

red @talkingmouth "You can do that?"

jasmine @happy "Certainly. Most Coordinator Contests are quite free about the number of entrants that are allowed to join together. This is to accommodate band-style performances."

brendan @talking2mouth "The Go-Rock Quads from Fiore are pretty famous Coordinators, and they never participate alone--it's always the four of 'em."

red @talkingmouth "Are you and May going together, then?"

brendan @sweat sadbrow talking2mouth "Nah. I love her, but our performance styles are way too different. She's all pyrotechnics and props, and I do singing and dancing."
brendan @happy "We'd just get in each other's way."
brendan @sadbrow talking2mouth "And, before you ask--sorry, bro. My routine's pretty locked-in. Can't partner with you."

jasmine @sad2brow talkingmouth "I must echo this. I'm afraid I would not be reliable enough to be a partner, in any case..."

red @happy "Ah, it's alright. Good to know, anyway. Thanks, guys!"

jasmine @happy "It is, as always, my pleasure."

brendan @talkingmouth "Lemme know any time you want to talk about Contests more, dude!"

return

label eveningcontestintermission:

scene lobby
show fantina:
    xpos 0.66
show wallace:
    xpos 0.33
show screen currentdate
with splitfade

$ BecomeNamed("Instructrice Fantina")

wallace @happy "Oh, my darling Fantina, how good it is to see you again. It's been too long!"
wallace @sadbrow talkingmouth "After that nonsense at the end of last month, it's felt like we haven't had a single moment of downtime."
wallace @happy "How pleasant for us that we can {i}finally{/i} take a breath!"

fantina happy2 "{i}Oui.{/i} And how more pleasant that it is not our final one! Ohohoho!~"

wallace happy "Ohohoho!~"

pause 0.5

show fantina -happy2 with dis

wallace -happy @sadbrow talkingmouth "Now, I must ask you this, Fantina, as my mentor in teaching... I did not have the pleasure of being at Kobukan last year."
wallace @closedbrow sadmouth "And this new-old student, this 'Melody'... well, she seems to rather despise me."
wallace @closedbrow talkingmouth "Of course, it would be too easy to chalk this up to mere jealousy."

fantina @sad2 "Ah... {i}oui{/i}, there are many who despise that which they cannot attain."
fantina @norm4 "But, though this is just guess... I do not believe it is jealousy that causes her to act as so."

wallace @surprised "Oh? Do you have some unearthly insight to divulge? Some spectral secret that the ghosts have whispered to you?"

fantina @happy2 "{i}Non, non.{/i} Nothing quite so exciting. It is merely... observation. I have traveled to many regions, yes? Seen many contests."
fantina @norm2 "Miss Melody, it seems, is of similar breadth. Millennium Drop is relatively small, in comparison. Only accepting Kobukan Students."

wallace @closedbrow talking2mouth "{i}Oui.{/i} At that charming Phobos' request. Perhaps he feared that Lisia would simply crush the competition if allowed to compete."
wallace @happy "He is, of course, quite right!"

fantina @norm2 "Even so, a smaller contest. This behavior is... {i}inconsistant.{/i}"
fantina @norm4 "It is seeming, that... ah... this Miss Melody... last year, she had great excitement for contests. I remember, yes, it was passion."
fantina @surprised2 "But this year? Oh, surprise! Why, she seems to hate the very concept! New experiences bring change, but, ah... rarely so strong?"

wallace @closedbrow talkingmouth "I imagine she simply lost a contest she had high hopes for. She does not strike me as the kind of child who handles failure well."
wallace @angry "Besides, my darling niece told me that Melody forced herself into the team, not even giving Lisia a choice. This doesn't seem the behavior of someone who hates contests."
wallace @surprised "Oh. Unless... perhaps she wishes to ruin the Coordinator Club's chances, as some measure of revenge?"
wallace @angry "Why, that... that...!"

$ BecomeNamed("Instructor Wallace")

fantina @happy2 "Ohohoho!~ Champion Wallace, please, calm yourself. Such a handsome face ought not to tense with the wrinkles."

wallace @sadbrow talkingmouth "...True. Thank you, my dear."
wallace @angrybrow talking2mouth "It's just... ooh, that {i}blasted{/i} Melody... she frustrates me to {i}no{/i} end! She's so disruptive, she insults me in front of the entire class, and Dean Drayden can't do a darned-dang thing about it!"
wallace surprisedbrow frownmouth @closedbrow talking2mouth "I don't know why she even bothers showing up. It ought to be {i}entirely{/i} apparent that she is {i}not{/i} passing my class."

fantina angry @angry2 "{i}Champion Wallace!{/i}"

wallace @talking2mouth "My dear?"

fantina @angry2 "If you have... ah... any {i}respect{/i} for me as a teacher, you will not utter such things!"

wallace @talkingmouth "Oh course, I have the utmost respect, but..."

fantina @norm4 "We are teachers. It is our job to safeguard and guide next generation. To help to best abilities we have, regardless of who student is."
fantina @sad2 "Besides which... you are Champion. Both of Hoenn and Contests. Do not hold grudge against a misled child. It is... a word... petty."

wallace @closedbrow talkingmouth "It's quite easy to say these things when you're not teaching her personally, but..."
wallace @sadbrow talkingmouth "Yes, I suppose you're right."

show fantina surprised with dis

wallace @closedbrow talkingmouth "After all, if I let that little beast {i}know{/i} she's getting to me, then she wins."

fantina @surprised2 "I... That is not what I meant to imply."

wallace @sadbrow talkingmouth "Oh, I know what you mean, my dear Fantina. I appreciate your advice, as always. Your judgment is as sound in matters of education as it is when you're behind the bench of a Contest Judges' Panel."

fantina -surprisedbrow -frownmouth -surprised @happy "Ohohoho!~ Is experience that comes with age."

wallace @surprised "...I know better than to ask your age, but I must confess to thinking that you were younger than me?"

fantina @surprised2 "Oh? Perhaps so. Is that not the way of Coordinators? Why, we have so much makeup on, I may question what we look like underneath!"

wallace @happy "And I'm afraid we'll have to continue questioning, because if I had to go out without {i}my{/i} makeup, then I fear I would look quite ghastly!"

fantina happy @happy2 "You are too modest, Champion. {i}Non, non,{/i} you would be {i}Adonis{/i} whether made or unmade."

wallace @closedbrow talkingmouth "Flatterer. {i}Do{/i} go on."

hide wallace
hide fantina
with dis

return