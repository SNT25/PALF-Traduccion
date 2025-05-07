label secondhomeroom010412:

scene blank2

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom behind blank2

show oakbg behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade

oak @talkingmouth "...And that's why we use 'levels' as a general demarcator of a Pokémon's strength!" 
oak @talkingmouth "With mass amounts of education and memorization, very educated individuals are able to just tell what a Pokémon's level is at a glance, but most people use Pokédexes for that task."

redmind uniform @thinking "I mean, I would have, if you let me..."

oak @talkingmouth "Now, I hope no-one's forgotten about the quiz I promised all of you! Let's get right into it."

show dawn uniform frownmouth at leftside with dis

dawn @sad "Oh, no... my stomach's tying itself into knots..."

show whitney uniform at rightside with dis

$ BecomeNamed("Dawn")
whitney @happy "Chill, Dawn! You'll be fine."

dawn @surprised "Huh?! Who're you? And how do you know my name?!"

whitney @surprised "I mean... I've sat in front of you for, like, a week now. We also have Fairy class together...?"
whitney @happy "And the name's Whitney! And I believe in you!"

dawn @sadbrow talkingmouth "Th-thanks..."

hide whitney 
hide dawn
with dis

redmind @happy "Cute."
redmind @thinking "Alright. Gotta focus. Let's do this."

oak @talkingmouth "There's one important thing to remember for this quiz: {color=#0048ff}your opponent has the ability 'Dry Skin!'{/color} Now, with that information, you have everything you need to succeed."

$ trainer1 = Trainer("red", TrainerType.Player, [Pokemon(pokedexlookupname("Lotad", DexMacros.Id), level=5, moves=[GetMove("Leech Seed"), GetMove("Surf"), GetMove("Absorb"), GetMove("Growl")])])
$ trainer2 = Trainer("oak", TrainerType.Enemy, [Pokemon(pokedexlookupname("Paras", DexMacros.Id), level=5, moves=[GetMove("Scratch")], ability="Dry Skin")])

$ trainer1.GetTeam()[0].Health = 1
$ trainer2.GetTeam()[0].ChangeStats(Stats.Speed, -6, trainer2.GetTeam()[0])
$ trainer2.GetTeam()[0].Health = 1

call Battle([trainer1, trainer2], clearstats=False, gainexp=False, healParty=False, uniforms=[True, False], lockbag=True) from _call_Battle_13
$ battlehistory["Oak2"] = _return

$ renpy.transition(dissolve)
show screen currentdate

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

if (WonBattle("Oak2")):
    red uniform @happy "Not too shabby. There was really only one move that was guaranteed to win me the match, there."
else:
    red uniform @sad "Ah, geez... I really need to be more careful about how I battle when my Pokémon is at low health..."

oak @talkingmouth ".{w=0.5}.{w=0.5}.{w=0.5}"

pause 0.5

oak @talkingmouth "At a glance..."

pause 0.5

if (WonBattle("Oak2")):
    oak "It looks like everyone did quite well."
else:
    oak "I recommend everyone brush up on the immunities a Pokémon may possess. If all your other moves will have no effect, even a move that is resisted twice is your best option."

oak @talkingmouth "Remember, immunities can come from more than just a Pokémon's type." 
oak @talkingmouth "Grass-types are immune to many grass-based status moves, Dark-types are immune to the status moves of Pokémon with Prankster, and other types are immune to status conditions outright."

$ renpy.music.set_volume(0.1, delay=1.0, channel="music")
$ PlaySound("BellChime.ogg")

$ renpy.pause(2.0, hard=True)
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

oak @talkingmouth "That's it for today, class.{w=0.5} Now, you're all dismissed."

hide oakbg with dis

redmind @thinking "Phew. Alder mentioned that I can study after school... the best place to do that is probably in {color=#0048ff}the library, in the Academy.{/color}"
redmind @thinking "I should also find a study partner or two. Other people's schedules change, and they're busy, so they won't always be available to drop everything and study with me." 
redmind @thinking "{color=#0048ff}However, if I can contact them, then I can probably convince them to come over, though they probably won't appreciate that as much as they would if I found them when they were already studying.{/color}"

pause 1.0

redmind @happy "But before I do that, I should get [pika_name] from his room! I think he liked having free reign of the place over the weekend, and I'm worried what he'd do to me if I kept him locked up in my room while {i}I{/i} had free time."

call freeroam from _call_freeroam_1

if (not persondex["Leaf"]["Contact"]):
    scene blank2

    show hall_B with dis

    red @closedbrow talking2mouth "Alright, it's pretty much time to head back to bed, I reckon."

    $ renpy.music.play("Audio/Pokemon/pikachu_norm1.ogg", channel="altcry", loop=None)
    pikachu neutral_2 "Pikachu!"

    red @happy "Huh? What is it, boy?"

    show leaf with dis

    pause 1.0

    red @happy "Oh, hi! What's up?"

    leaf @sarcastic "Oh, I just realized I forgot to give you something."

    red @confusedeyebrows talking2mouth "Excuse me for being presumptious, but do we need to go somewhere there aren't security cameras?"

    leaf @happy "How dare you? I am {cps=*0.2}{i}shocked{/i}{/cps} and {cps=*0.2}{i}offended{/i}{/cps} at the {cps=*0.2}{i}implication,{/i}{/cps} good Sir."

    red @confusedeyebrows frownmouth "[ellipses]"

    pause 1.0

    leaf @talking2mouth "You're no fun.{w=0.5}{nw}" 
    leaf @talkingmouth "Anyway, I just wanted to give you my phone number. Can't believe I haven't already, actually."

    if (GetRelationship("Leaf") == "Bestie"):
        leaf @happy "Especially now that we're besties!"

    $ BecomeContacted("Leaf")

    red @talkingmouth "Oh, cool. Thanks. Now, you should really get back to Aura Hall. Curfew's in, like, ten minutes."

    leaf @flirttalk "It's cool. My ninja skills mean I won't get caught."

    red @closedbrow talkingmouth "Well, I'm not going to get caught by not being out. Seeya."

    leaf happy "See you! Bye, [pika_name]!"

    $ renpy.music.play("Audio/Pokemon/pikachu_happy2.ogg", channel="altcry", loop=None)
    pikachu happy_2 "Pikachu!"

call texting from _call_texting_2

jump day010413