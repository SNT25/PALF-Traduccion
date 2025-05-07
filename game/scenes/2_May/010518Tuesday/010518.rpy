label day010518:

stop music fadeout 1.5

call calendar(1) from _call_calendar_43
$ calDate = calDate.replace(day=18, month=5, year=2004)

$ timeOfDay = "Morning"

scene homeroom
show screen currentdate
show kris
with splitfade

stop music fadeout 1.5
queue music "audio/music/celebi_start.ogg" noloop
queue music "audio/music/celebi_loop.ogg"

kris @talkingmouth "Good morning, students! Good to see that you're almost all here."

show hilbert uniform sadbrow:
    xpos 1.2 
    ease 5.0 xpos 0.75

kris @happy "It's nice to see how much you care about your education."

hilbert @talkingmouth "I have decided where the limit of my care is. It is located at precisely 7:15 AM."

show whitney uniform:
    xpos 0.25
with dis

whitney @angrybrow happymouth "Well, you're here, aren't you? Don't be so grumpy! This'll be great!"

pause 0.5

whitney @sadbrow talking2mouth "As long as we can ride on a Cyclizar, of course. We, uh, we don't have to walk...?"

kris @talkingmouth "No, no. Did anyone bring any Cyclizar with them to class?"

narrator "A few students--Leaf, Dawn, even Hilbert--walk up to the front of the classroom and hand over their Poké Balls, or have a quick discussion with Professor Cherry."

python:
    cyclizarcount = 0
    for mon in box + playerparty:
        if (mon.GetId() == pokedexlookupname("Cyclizar", DexMacros.Id)):
            cyclizarcount += 1
    cyclizarcount = min(cyclizarcount, 5)

if (cyclizarcount == 0):
    narrator "You stay seated."

elif (cyclizarcount == 1):
    red uniform @talkingmouth "Hi. I've got a Cyclizar, so you don't need to rent one for me."

    $ ValueChange("Professor Cherry", 3, 0.5)

    kris @happy "Fantastic! Thank you, [first_name]. That's very helpful."

else:    
    red uniform @talkingmouth "Hi. I've got a couple Cyclizar, so you don't need to rent one for me, and I can lend them to some of the other students."

    $ ValueChange("Professor Cherry", cyclizarcount * 2, 0.5)

    kris @happy "Fantastic! Thank you, [first_name]. That's very helpful."

show blank2 with splitfade

pause 1.0

scene newhomeroom 
show oak:
    xpos 0.66
show kris:
    xpos 0.33
with splitfade

narrator "The class swings by Professor Cherry's homeroom to use the PC there. While there, you suddenly realize that Professor Oak is at the front of the class, lecturing."

oak sad2eyes frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

narrator "He seems to avoid eye contact. You then notice Ethan is making very active eye contact, and clearly mouthing the words 'help me.'"

ethan uniform @angrybrow anger talking2mouth "(Help. Me.)"

narrator "...Looking around, it seems most of the students in this class look either bored out of their mind or actively disgusted..."

kris angrymouth @sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."
kris @sadbrow talkingmouth "Well, how are my students doing, Doctor Oak?"

oak -sad2eyes -frownmouth @closedbrow talkingmouth "Oh... splendidly, splendid, Doctor Cherry. They're so engaged with the lectures. Absolutely wonderful. Couldn't ask for a better class."

pause 1.0

redmind uniform @sadbrow frownmouth "And the worst part is, he means every word."

kris @talkingmouth "We're still planning on swapping back at the end of the week, yes?"

oak @surprised "Why... yes, certainly. Unless there was some reason to change the plan?"

kris -angrymouth @happy "N-no! No reason."

pause 0.5

kris @closedbrow talkingmouth "Well... come along, class 1-B. Grab your Cyclizar, and let's go."

scene blank2 with splitfade

pause 1.0

narrator "You all go out to the fields and mount your Cyclizar. Some people need a bit more help riding them, and others seem to get it right away."

python:
    hascyclizar = False
    for mon in AllPokemon():
        if (mon.GetId() == pokedexlookupname("Cyclizar", DexMacros.Id)):
            hascyclizar = True
            break

if (hascyclizar):
    $ PlaySound("pokemon/cries/{}.mp3".format(pokedexlookupname("Cyclizar", DexMacros.Id)))

    narrator "You pet your Cyclizar's neck as you wait for your classmates to get situated. Your Cyclizar growls impatiently, desire to run clear in its eyes."

else:
    narrator "You pet your Ride Cyclizar's neck as you wait for your classmates to get situated. Despite its impatience, this Cyclizar is a trained professional, and stays still."

#ethan uniform @closedbrow talking2mouth "{size=30}Man, I can't believe I'm going back here so soon.{/size}"

kris @talkingmouth "Everyone, remember to hang on tight. We don't want anyone to get injured on the mountain by falling off their Cyclizar."

pause 1.0

kris @closedbrow talkingmouth "Come to think of it, I probably should have rented helmets for us, as well..."

leaf uniform @angrybrow happymouth "Onwards and upwards, lads! {i}Tonight, we ride!{/i}"

whitney uniform @surprised "Wh-wh-wha! Slow down!"

flannery uniform tiredbrow @talking2mouth "And it's barely 7:30 in the morning..."

scene mountain with splitfade

$ PlaySound("pokemon/cries/{}.mp3".format(pokedexlookupname("Cyclizar", DexMacros.Id)))

narrator "You make your way to the top of the mountain without incident. Professor Cherry dismounts, hair flapping in the crisp mountain air."

show kris with dis

kris @happy "Oh, isn't this {i}grand{/i}? Look at this beautiful snow!"

show hilbert uniform with dis:
    xpos 0.75

hilbert @talkingmouth "Why is it here? It's the middle of May."

show kris:
    ease 0.5 xzoom -1

kris @talkingmouth "Hm... Dawn, you can answer this one, can't you?"

show kris:
    xzoom -1

show dawn uniform surprised with dis:
    xpos 0.25

dawn @talkingmouth "Huh? Wh- I mean- I don't think- It's-"

pause 1.0

dawn frownmouth sadbrow "...Sorry."

kris @sadbrow talkingmouth "It's alright, Dawn. I sprang that on you, didn't I?"

dawn @talkingmouth "N-no, I'm just... a nervous wreck..."

pause 1.0

dawn @talkingmouth "B-but... I {i}can{/i} answer this. It's because of the wild Pokémon."

hilbert @surprised "Hm?"

dawn @talkingmouth "There are a lot of Snover around here, as well as Vulpix. The Alolan kind, I mean."

if (ninetalesobj not in AllPokemon()):
    dawn @happy "I even caught a Ninetales here, once."

dawn -frownmouth @talkingmouth "They have an ability to make it snow around them. And hail, sometimes, too. So if their habitat gets too warm, they'll just cool it down themselves."

kris @happy "Excellent work, Dawn. I see your Snowpoint upbringing taught you a lot about Ice-types."

hide dawn with dis

show kris:
    ease 0.5 xzoom 1

kris @talkingmouth "Though these Ice-type Pokémon are capable of cooling down their own environments, they still prefer to make their homes in as cold environments as possible. So, in Summer, that means the tips of mountains."

show kris:
    xzoom 1

kris @happy "Of course, Argent isn't a very {i}tall{/i} mountain, but beggars can't be choosers."
kris @talkingmouth "In fact, this is an observable phenomenon in almost every region--even the tropical Hoenn has a series of ice caves the native Spheal and Snorunt have carved out."
kris @surprised "Truth be told, it {i}used{/i} to be a volcano--it's been dormant for hundreds of years, though, since before the founding of the Academy."
kris @talkingmouth "You'd never know by looking at it nowadays, but you can still catch the occasional fire-type that lives deep within the mountain's core."
kris @angrybrow talkingmouth "When they emerge out into the surface like this, they're apex predators of the many ice-types that live around here!" 

hilbert @closedbrow talkingmouth "I see. So Pokémon can use their abilities in non-battle contexts, too..."

hide hilbert with dis

kris @angrybrow talkingmouth "Absolutely. I hope that, if I can teach you anything, I can teach you that. Pokémon are how people become the best versions of themselves."
kris @happy "And I don't mean in a moral or philosophical sense! I mean stronger, smarter, faster." 
kris @talkingmouth "Trainers don't just make Pokémon better. Your Pokémon are your friends, and friends make {i}each other{/i} better."

pause 1.0

kris @talkingmouth "Well, I think that's about everything I wanted to cover. Trying not to take too much time up with lectures, you know."
kris @happy "Go wild!"

pause 0.5

show leaf uniform surprisedbrow frownmouth with dis:
    xpos 0.75

leaf @surprised "Um... 'go wild'?"

kris @talkingmouth "Yes. Battle Pokémon. Explore. As long as you're in the field, you're gaining experience. Practical, field experience is what you need more than anything right now."

leaf @talking2mouth "...'Kay."

hide leaf
hide kris 
with dis

pause 1.0

narrator "The crowd awkwardly disperses after Professor Cherry's proclamation, wandering off in random directions, unused to this level of freedom."

redmind uniform "Well, I'm not going to look a gift two hours in the minutes. Let's see what's around!"

$ wildcount = 0

call wildarea("mountain") from _call_wildarea_7

show kris with dis

kris @talkingmouth "Alright! Good to see all of you are still here. Nobody got eaten by an Abomasnow."
kris @happy "Of course, they normally only come after you if you're skiing."

red uniform @closedbrow talking2mouth "Oh, more obscure references no-one except Ethan and Professor Cherry understand."

leaf uniform surprised "Wait, Professor Cherry {i}gets{/i} Ethan's references?!"

red uniform @talkingmouth "Sure. She used to be his babysitter."

pause 1.0

show mountain with vpunch

leaf @surprised "I didn't know that! You can't hide this stuff from me!"

kris @talkingmouth "{i}A-hem!{/i} Eyes up front, please!"

red @closedbrow talking2mouth "Sorry, Professor."

kris @talkingmouth "We don't have a lot of time before your first electives start, so we need to make our way back down the mountain now. We should make it on time, but if anyone's late, just blame it on me."
kris @closedbrow talking2mouth "We're in a hurry, but {i}do not{/i} rush. A mountainside is one of the worst places to be injured, and if you break something, it's a long way to the hospital."
kris @talkingmouth "Nurse Miriam is good, but she can't fix bones in-house. Keep a calm, steady, pace and watch out for your classmates around you."

Character("Class") "\"Yes, Professor!\""

call clearscreens() from _call_clearscreens_183
scene blank2 with splitfade

narrator "As you make your way back down the mountain, you overhear a conversation, shouted between students as they ride their Cyclizar."

Character("Gossipy Bint") "\"Man, I thought Oak was pretty cool, but I didn't realize how much {i}better{/i} class could be!\""

Character("Shocked Bambino") "\"Yeah! I mean, we were supposed to have a PC in our classroom this entire time? I could've been training {i}so{/i} many more Pokémon!\""

Character("Ranting Imbecile") "\"And it turns out that Oak just wasn't preparing us for the tests! So the fact I failed most of 'em isn't {i}my{/i} fault!\""

Character("Gossipy Bint") "\"I... don't know about that one. You {i}are{/i} kinda a dumbass.\""

pause 1.0

narrator "...It seems Professor Cherry heard the conversation, too."

kris @sadbrow angrymouth "{w=0.5}.{w=0.5}.{w=0.5}."

redmind uniform @thinking "She's in an awkward position. She doesn't want to badmouth her colleague, or let anyone else badmouth him, but at the same time, she {i}did{/i} make clear she was pretty upset about what Sam was teaching us..."
redmind @sweat closedbrow frownmouth "Or {i}not{/i} teaching us, I guess."

pause 0.5

redmind @thinking "Maybe I should talk to her."

if (GetRelationshipRank("Professor Cherry") > 0):
    redmind @thinking "After all, I'm 'investigating' her. I could do with-"

else:
    redmind @thinking "After all, if she's going to be my homeroom teacher for the rest of the week, then-"

kris @surprised "[first_name] [last_name]! Eyes open on the mountain!"

red uniform @surprised "G-gah, sorry, Professor! Got lost in thought!"

pause 1.0

redmind @sadbrow frownmouth "Maybe I'll talk to her later."

$ HealParty()

jump homeroom1transition