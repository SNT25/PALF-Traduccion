label Kris1:

if (not IsBefore(1, 5, 2004)):
    $ persondex["Professor Cherry"]["Events"].append("Level2SceneVer2")

scene garden:
    zoom 0.625
show clouds behind garden
show kris angrymouth:
    xpos 0.5 ypos 1.3
with Dissolve(2.0)
stop music fadeout 1.5
queue music "audio/music/celebi_start.ogg" noloop
queue music "audio/music/celebi_loop.ogg"

narrator "You're walking through the garden when you notice Professor Cherry furrowing her brow and looking at an Oran Berry tree with mild displeasure."

red @talkingmouth "Professor Cherry?"

kris surprisedbrow frownmouth @surprised "Oh!"

show kris -angrymouth -surprised:
    ease 0.5 ypos 1.0

kris @talkingmouth "Well, [first_name]. What can I help you with?"

red @happy "Nothing much, Doctor."
red @talkingmouth "Is there something I can help you with? It looked like you were giving that {i}Oranomi sinesis{/i} tree a serious stink eye."

kris @closedbrow talking2mouth "No, I don't think there's anything you can do about that one. Unfortunately, these trees seem as though they're being nibbled at by a Bug-type Pokémon."

show kris:
    ease 0.5 ypos 1.2 zoom 1.3

narrator "Professor Cherry gets surprisingly close to you, and points directly through your line of sight at some faint scratch markings on the trees."

kris @talkingmouth "See those? Mandible markings. The slight disintegration of the wood pulp around the edges indicates the offending Pokémon was probably venomous."
kris @closedbrow talking2mouth "It's only a small amount of poison damage, though, so it wasn't anything big. I think it was probably a--"

red @talkingmouth "A Venonat?"

kris @surprised "Hm? How'd you know?"

red @happy "Well, I'm a very good student, who stays up-to-date on the readings, and makes sure to take diligent notes."

kris @happy "Well, I'm quite happy to hear that."

if (IsBefore(1, 5, 2004)):
    red @sadbrow sweat happymouth "Or maybe a friend of mine caught a Venonat in this garden earlier this month."
else:
    red @sadbrow sweat happymouth "Or maybe a friend of mine caught a Venonat in this garden in early April."

kris @angrybrow happymouth "That's fair, too. That's what we call 'field research!'"

red @happy "Well, I'll leave you to {i}your{/i} field research, then, Doctor."

kris @talkingmouth "Yes, have a good.{w=0.5}.{w=0.5}.{w=0.5}"

show kris angrybrow angrymouth with dis:
    ease 2.0 ypos 1.0 zoom 1.0

red @confused "Hm?"

kris @talking2mouth "Don't move."

red @surprised "Um... okay."

show kris:
    ease 2.0 ypos 0.9 zoom 0.8

narrator "Professor Cherry slowly takes a Poké Ball from her coat pocket and holds it in the air."

pause 0.5

show kris angrybrow happymouth:
    parallel:
        ease 0.2 ypos 1.0 zoom 1.0
    parallel:
        ease 0.2 xzoom -1.0
        ease 0.2 xzoom 1.0

$ PlaySound("whoosh.ogg")

narrator "A moment later, she drops it, and, in an instantaneous spinning kick, almost faster than you can see, expertly kicks the ball through your legs."

red @surprised "Woah!"

$ PlaySound("pokemon/ball sound.ogg")
$ PlaySound("pokemon/cries/48.mp3")

show kris sadbrow angrymouth with dis:
    xzoom 1.0

narrator "Turning around, you see a Poké Ball rock once...{w=1.0} {nw}"

show kris -sadbrow -angrymouth surprised with dis

extend @talkingmouth "twice...{w=1.0} {nw}" 

show kris -surprisedbrow -frownmouth -surprised angrybrow angrymouth with dis

extend @talkingmouth "three times...{w=1.0} {nw}" 

show kris -angrybrow -angrymouth happy with dis

extend  @talkingmouth "and then click."

show kris:
    ease 0.5 ypos 1.2
    pause 0.5
    ease 0.5 ypos 1.0

kris -happy @happy "Found the pest!"
kris @angrybrow happymouth "This little guy certainly won't be nibbling at the garden's Oran groves any more."
kris @happy "Now, I should--"

show kris surprisedbrow frownmouth with vpunch

red @surprised "Ma'am, I need you to tell me how to do that."

kris -surprisedbrow -frownmouth -surprised @talkingmouth "Oh, the capturing a Pokémon by kicking the Poké Ball?"

red @talkingmouth "Yes! That was amazing, Doctor."

kris @closedbrow talking2mouth "{size=30}Doctor, Professor, Ma'am... pick one, geez.{/size}"
kris @happy "Well, I'm afraid it's not the sort of thing I can really easily teach. I was... er..."
kris @talkingmouth "Well, it's not a nice story, but I {i}had{/i} to learn to use my feet for a while."

red @talkingmouth "Woah. Can I hear this story?"

kris @sadbrow talking2mouth "Ah... I don't think it'd be entirely appropriate for me to tell a student that story. I'm sure you're mature enough to handle it, but I don't want to risk it."

redmind @thinking "Mature enough to handle it? No way Professor Cherry is any more than four years older than me. Heck, in certain lights, she looks like she might be younger."

red @talkingmouth "That's alright, then. I can understand wanting to err on the side of caution, as a teacher."

pause 0.5

redmind @thinking "...Okay, this is bothering me, actually. I don't think anyone's ever {i}not{/i} told me something about themselves when I asked them to."
redmind @thinking "That's because of Frienergy, I guess."

red @talkingmouth "Um... I know this is a weird question, but... are you busy, Doctor?"

kris @surprised "Hm?"
kris @happy "Well, yes. I'm a teacher. I'm {i}always{/i} busy."
kris @talkingmouth "But I've got time if you need help with a subject. I was actually just in my office, holding office hours, but it looks like it's a slow day."

pause 0.5

kris @talkingmouth "So. What can I help you with?"

red @talkingmouth "Well, you promised me some embarrassing stories about Ethan."

kris @happy "Oh, that's right!"
kris @talkingmouth "Hm... how about I tell you about the time we went to see the Pokéathlon together?"

red @talkingmouth "Sure."

kris @talkingmouth "There was a girl in our town, New Bark Town, Lyra, who was a Junior Pokéathlete. Ethan and her butted heads, but I think there was a bit of a crush there, too."
kris @happy "Anyway, she invited her entire class, and their parents, to watch her participate in the Block Smash event."
kris @talkingmouth "Ethan's Dad was away on a business trip, so I went with him."
kris @closedbrow talkingmouth "He cheered himself hoarse for a week. Hah, hah. Lyra was really grateful he showed up, since that pretty much guaranteed everyone else would as well."

$ PlaySound("idea.ogg")

red @surprised "Hm?"

kris @talkingmouth "Well, he was really popular, and the leader of his class. So wherever he went, everyone else followed."

if (GetRelationshipRank("Ethan") == 0):
    red @confused "That... well, I mean, he's a good friend, but that doesn't sound like the kind of thing Ethan is about."

else:
    red @confused "Right. He told me about that. But it's kinda hard to think of him like that now, isn't it? I mean, he's a good friend, but that doesn't sound like the kind of thing Ethan is about."


kris @surprised "Oh."
kris @closedbrow angrymouth "Hm..."
kris @talking2mouth "I did end up... 'leaving' New Bark Town for two years, and after that we didn't have much contact. I was distracted by my research, and have been, pretty much ever since."
kris @closedbrow talking2mouth "I suppose he might've changed somewhat in the interim."

red @talkingmouth "What made you disappear for two years, anyway? Some sort of foreign exchange thing? Or were you already a Professor-in-training, then?"

kris @talkingmouth "Hm. That's another private detail, I'm afraid."

redmind @surprised "...WHAT? Okay, I get she's a Professor, and Professors aren't supposed to share their personal lives with their students, but... what's happening here?"

red @talkingmouth "Okay. Well, um... what made you decide to be a teacher?"

show kris angrybrow angrymouth with dis

pause 1.0

red @confused "No way. That's {i}also{/i} private?"

kris -angrybrow -angrymouth @happy "Afraid so."

red @closedbrow talking2mouth "Damn."

kris @happy "I get the feeling most people don't put up boundaries around you."

if (not IsBefore(1, 5, 2004)):
    kris @sadbrow happymouth "Perhaps that's due to your friendship power?"

    redmind @sweat closedbrow frownmouth "Right, I guess all the teachers would have heard about that..."

red @sadbrow happymouth "Yeah, no, generally speaking. And I totally get where you're coming from, this is just... a very new experience."

kris @talkingmouth "Well, then I must be doing my job as a teacher well. A teacher's meant to introduce you to new experiences, isn't she?"

red @closedbrow talking2mouth "Yeah..."

pause 0.5

red @talkingmouth "Okay, here's one. I bet I could just look this up on, like, the school's staff page. What's your doctorate in?"

kris @surprised "Oh!"
kris @happy "I can answer that one, sure. I'm actually a Doctor of Pokémon Capturing."

red @surprised "Huh?"

kris @talkingmouth "Back in postgrad, my classmates barely even saw me, I spent so much time studying. I was on the fast-track, as well. They didn't even know what my name was, most of them, so they just called me 'Catcher.'"
kris @happy "It took a last-minute intervention from the Dean to make sure that my degree didn't say 'Catcher Cherry' on it."

red @talkingmouth "Huh, I had no idea that catching Pokémon was a complicated enough field to be a science. I kinda thought you--"

kris @closedbrow talkingmouth "--just lowered the opponent Pokémon's HP, then threw a Poké Ball at it. Yes, I know."
kris @angrybrow talkingmouth "Believe me, I've had to explain that capturing Pokémon {i}is{/i} a science to more people than I can count." 
kris @closedbrow talkingmouth "My own parents still don't get what I went to school for, but they'd support me in pretty much anything, after... {w=0.5}after school."

pause 1.0

redmind @surprisedbrow frownmouth "Hm? That was weird."

red @talkingmouth "Well, what's the science of catching about?"

kris @talkingmouth "Well, there are many different kinds of Pokémon, right? And they all have different ways of trying to evade capture."
kris @angrybrow talkingmouth "Now, the thing about the Pokémon's evasion instinct, or 'Compulsive Capture Avoidance', is that they're not {i}truly{/i} trying to avoid being captured."

red @surprised "Huh."

kris @talking2mouth "The reason a Pokémon tries to avoid being captured by a trainer, even if the Pokémon approached the trainer to challenge them, is an evolutionary mechanism."
kris @closedbrow talkingmouth "Long-term evolution, of course, not the short-term metamorphosis we call 'evolution.'"

red @talkingmouth "Right, got it."

kris @talking2mouth "With Pokémon being social creatures, who have evolved and adapted alongside humans, it benefits a Pokémon to make sure only the strongest trainers can catch them."

red @talkingmouth "That's why they fight back against us, in the wild, then?"

kris @happy "That's right!"
kris @talkingmouth "That's also why they attempt to bust out of Poké Balls thrown at them."
kris @talking2mouth "They want us to prove ourselves to them. Personally, I think that's admirable."

red @talkingmouth "But that Venonat you just caught... you didn't weaken it, first, but it just went into the ball?"

#Kris team: Stonjourner, Blaziken, Hitmonlee -- kicks?
kris @happy "Well, that {i}was{/i} a risky move, but I don't have any Pokémon on-hand right now, so I just had to aim for the Pokémon's energy nexus."

pause 1.0

red @confused "Pardon?"

kris @talkingmouth "You know, their nexus. Where they concentrate the energy for their elemental attacks."

pause 0.5

red @confused "I've actually never heard of that before."

kris @surprised "Huh."

pause 0.5

kris @happy "Well, yes, every Pokémon has a nexus that their energy is concentrated in. A 'critical hit' is often the result of hitting that special spot."
kris @talkingmouth "And if you hit the Pokémon on that spot directly with a Poké Ball, that's called a 'Critical Capture.'"

red @talkingmouth "Huh."

kris @sadbrow talkingmouth "They really didn't teach you any of this in High School?"

red @closedbrow talkingmouth "It was a miracle that they taught me {i}anything{/i} in high school, honestly."

kris @closedbrow angrymouth "Hm."
kris @happy "Well, you're lucky that I'm here, then! I'm always ready to help my students outside of class. Heck, as I said, I'm doing office hours now."

red @talkingmouth "Cool. So, learning about these 'Nexus Points' will help me with my capturing skills, right?"

kris @talkingmouth "It should."

red @talking2mouth "Okay, what's the first step?"

kris @closedbrow talking2mouth "Memorizing nexus locations. There isn't really an easy way to do that. You kind of have to just sit down with a book and memorize them slowly."

red @happy "Professor Cherry, I memorized the Pokédex. I can memorize one more data point for every Pokémon."

kris @surprised "Really? The entire Pokédex?"

red @talkingmouth happybrow "Yep. Not purposefully, but I did."

kris @talkingmouth "Alright. Well, let's just get started, then. I'll start in the Kantonian National Pokédex order, as that's what I imagine you're most familiar with."

pause 0.5

kris @closedbrow talking2mouth "Okay."

pause 0.5

kris @closedbrow talkingmouth "Bulbasaur line--the tip of their bulbs, or flowers. Charmander line--the tip of their tails. Squirtle and Wartortle are the nose. Blastoise is cannons. Caterpie's crest--"

show black with Dissolve(2.0)

narrator "As Professor Cherry lists off the locations of various Pokémon to you, you sit on a bench, paying rapt attention."

hide black with dis

kris @happy "And Dragonite's Nexus is, of course, the little horn on the top of its head. That finishes the Kanto Pokédex. Are you still with me for Johto?"

red @talkingmouth "Sure, but we've been doing this for a while. Are your office hours still open?"

kris @surprised "Oh! Wow, time has {i}seriously{/i} flown."
kris @happy "Sometimes I get so caught up in {cps=35}what I'm {cps=30}doing I {cps=25}don't notice{nw}" 
extend angrymouth @sadbrow talkingmouth "{cps=20} that hours {cps=15}have{cps=10}.{cps=5}.."
kris @sadbrow frownmouth "[ellipses]"

pause 0.5

red @talkingmouth "Is... something wrong, Professor?"

kris @closedbrow talking2mouth "Oh. Um... nothing."

red @confused "...Okay."

kris @happy "Have a good rest of your day, alright? I hope that my impromptu lecture on critical captures was helpful."

red @talking2mouth "Right. You... too."

hide kris with dis

red @closedbrow talking2mouth "Huh? What just happened?"

narrator "[bluecolor]You can now perform critical captures!{/color}"
narrator "When performing a critical capture, you will {i}always{/i} capture the Pokemon, independent of your normal capture rate."
$ critcatchrate = GetAverageProficiency()
narrator "Your critical capture rate is equal to the average of all your class proficiencies. So, right now, it's equal to [critcatchrate]%%."
narrator "If you want to check your Critical Capture Rate easily, check in with Professor Cherry during your free time!"

redmind @thinking "Hm... No, I have no idea."

pause 1.0

show ethan with dis

red @talkingmouth "Hey, Ethan."

ethan @talkingmouth "Oh, hey, [first_name]. Whatcha doing here?"

red @talkingmouth "Just talking with Professor Cherry for a bit."

ethan @talking2mouth "That's cool. Learn anything new?"

red @closedbrow talking2mouth "Nothing about you, don't worry."

ethan @happy "Phew! She's got {i}so{/i} much dirt on me, it's terrifying."

red @talkingmouth "Hey... could you share some information with me?"

ethan @closedbrow talkingmouth "About her?"

red @talkingmouth "Yeah."

ethan @closedbrow talking2mouth "Right, so you picked up on her... avoidance of talking about her past, huh."

red @confused "A little bit. I'm honestly super-confused as to how this happened. I mean... no-one has ever {i}not{/i} told me something about their past when I asked about it."

red @happy "Sorry, that sounds weird, doesn't it?"

ethan @talkingmouth "Eh, I get ya."

pause 1.0

red @confused "So?"

ethan @sweat talkingmouth "I don't think I should tell ya, but, honestly, man, this is all public information. You can probably just look it up on the internet."

red @talkingmouth "Hm... Doctor Kris Cherry, right?"

ethan @talkingmouth "Yeah. And she has a younger sister named Marina, who was involved. Marina was my age, but I didn't see her much. She went to a girls' school in Goldenrod."

red @talkingmouth "Alright. I'll look them up, then."

ethan @happy "Yeah, good luck."

pause 0.5

ethan @talkingmouth "Hey, uh, Professor Cherry is really cool about stuff. But, um, don't let her know you're looking into her, alright? Because that's, like, the one thing she won't be cool with."
ethan @closedbrow talking2mouth "The one time I've ever seen her lose her cool was when a couple journalists from the School Newspaper club interrupted homeroom to interrogate her."

red @talkingmouth "Don't worry. I'll be subtle."

$ ValueChange("Ethan", 5, 0.5)

ethan @talking2mouth "Cool, man. Seeya around."

hide ethan with dis

pause 1.0

red blackglasses talking2mouth "Alright. [bluecolor]Investigator{/color} [last_name] is on the case."

$ PlaySound("Pokemon/pikachu_question.ogg")

if (IsBefore(1, 5, 2004)):
    pikachu bashful_2 "Pika?"
else:
    libpikachu sadeyes happymouth "Pika?"

$ persondex["Professor Cherry"]["Relationship"] = "Investigator"
$ persondex["Professor Cherry"]["RelationshipRank"] = 1

$ PlaySound("sav.ogg")

narrator "Your heart shifts as you feel your relationship with Professor Cherry evolve from '{color=#0048ff}Student{/color}' to '{color=#0048ff}Investigator{/color}'!"

return