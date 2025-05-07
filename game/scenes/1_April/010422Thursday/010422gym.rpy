label gym010422:

$ HealParty()

play music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

$ renpy.transition(dissolve)
show screen currentdate

scene gym with dis

show blank2 behind gym

$ renpy.pause(2.0, hard=True)

hide blank2

show alder spunky2 with dis:
    xpos 0.66

show bruno think with dis:
    xpos 0.33

alder norm @spunky2 "And that concludes the lecture! So, battle time. How has everyone been feeling about the double battle unit so far?"

misty uniform @talkingmouth "I don't get why we bother. All official battles are single battles. Aren't we just wasting time practicing double battles?"

alder @norm2 "Not at all. The skills are definitely transferrable, and Kobukan's own Quarter Qlashes have been in double, triple, and even inverse battle formats before."

misty @surprised "Inverse battles?"

alder @norm2 "Yep. A lot of Pokémon Leagues restrict gym battles to one-versus-one affairs, but there are just as many out-of-the-gym situations where knowing how to control multiple Pokémon at once can be useful."

alder @spunky2 "After all, when you're in the wild, Pokémon aren't likely to just line up one-on-one and fight you, all nicely."

redmind uniform @confusedeyebrows frownmouth "Really? That's kinda what they do for me, though..."

pause 1.0

alder @spunky2 "Oh, looks like you're going to be battling Misty today, [first_name]."

hide alder
hide bruno 
with dis

pause 1.0

show misty uniform
with dis

pause 1.0

misty uniform @talkingmouth "...Hi."

red @happy "Hey! Ready to battle?"

misty @talkingmouth "Yeah, I guess. Let's get this over with."

misty @closedbrow talkingmouth "Staryu, I choose-"

$ sidemonnum = 54

$ PlaySound("Pokemon/Ball sound.ogg")
queue sound "audio/pokemon/cries/54.mp3"

show sideportraitfull at dormdesk, pokeball
show misty surprisedbrow frownmouth:
    easein 0.3 xpos 0.75

$ hideside = True

sidemon @talkingmouth "PSSSSSY!"

$ hideside = False
$ trainer1 = Trainer("red", TrainerType.Player, playerparty, number=2)
$ trainer2 = Trainer("sideportraitfull", TrainerType.Enemy, [Pokemon(54, level=16, moves=[GetMove("Surf"), GetMove("Amnesia"), GetMove("Calm Mind"), GetMove("Confusion")], gender=Genders.Male, ability="Damp")])

call Battle([trainer1, trainer2], uniforms=[True], customexpressions=["red surprised", "red surprised", "sideportraitfull", "sideportraitfull"]) from _call_Battle_49
$ battlehistory["Misty1"]  = _return

$ HealParty()

stop music fadeout 1.0

hide alder
hide bruno

pause 1.0

show alder surprisedbrow frownmouth at centerside 
show bruno think at leftside
show misty sad at rightside
with dis

$ renpy.music.queue("Audio/Music/Gym_Loop.ogg", channel='music', loop=True, fadein=1.25, tight=None)
    
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

hide blank2

if (WonBattle("Misty1")):
    misty @talkingmouth "Ugh... sorry about that. My Psyduck just doesn't listen to me at all... good thing you were here to knock 'im out."
    $ ValueChange("Misty", 3, 0.75)
else:
    misty @talkingmouth "What? Even you couldn't beat that thing? Ugh... Psyduck, {i}return!{/i}"

    queue sound "audio/Pokemon/Ball sound.ogg"
    $ PlaySound("pokemon/cries/54.mp3")

    sidemon "P{size=35}s{/size}{size=30}s{/size}{size=25}s{/size}{size=20}s{/size}{size=15}y{/size}{size=10}!{/size}"

alder @surprised2 "Misty, what's happening here?"

misty @talkingmouth "Um... my Psyduck is kinda... disobedient. He just never listens to me, and when I try to send out one of my Pokémon, he'll jump out instead."

pause 1.0

alder @norm3 "Hm..."

alder @norm4 "Looks to me like a classic case of acting out for attention."

misty surprisedbrow frownmouth @surprised "Huh?"

alder @angry2 "Your Psyduck's actually very strong, so, clearly, you've been training him well. The issue, I think, is that the trainer-Pokémon relationship has more to it than just training."

red @confused "What's that, Sir?"

alder @happy2 "Oh, you already know, [first_name]. I've seen how you interact with your Pokémon."

alder @norm2 "Misty, you need to be more affectionate with your Psyduck. Right now, I'm willing to bet dollars to donuts that it feels underappreciated."

misty -surprisedbrow -frownmouth -surprised @talkingmouth "My Staryu isn't like that, though. And I train them the same way."

alder @sad2 "Well, just like with people, some Pokémon are more emotionally resilient. But just because they're better at hiding how they feel doesn't mean their feelings can be ignored."

misty @sad "I... I see."

alder @happy2 "The good news is, because your Psyduck is still acting out, that means it still cares about you. If it gave up, {i}then{/i} we'd have a problem." 
alder @norm2 "So as long as you make sure to groom it, take it out for non-training purposes, and let it know how important it is to you, we should be fine."

misty sad "...Right. {size=25}I just don't know...{/size}"

jump lunchtransition