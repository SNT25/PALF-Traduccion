label day010423:

$ playerparty.remove(pikachuobj)
$ timeOfDay = "Morning"
call calendar(1) from _call_calendar_18
$ calDate = calDate.replace(day=23, month=4, year=2004)

show morning at vspaz

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)
show oakbg
show homeroom behind oakbg

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade    
hide morning

$ renpy.pause(0.6, hard=True)

oak @talkingmouth "I tell you, these meteorite fragments are truly something! There appears to be biological residue embedded within the very stone."
oak @talkingmouth "My new assistant is an utter godsend, I tell you. With her experience, we could be moments--moments, I say--from discovering the Kobukanian equivalent of Wishing Stars."

pause 1.0

oak @talkingmouth "But... I suppose that won't be on the test, so your interest being limited is understandable, if disheartening."
oak @talkingmouth "{i}Sigh.{/i}"
oak @talkingmouth "Very well. You're dismissed."

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.0)

redmind uniform @thinking "...Man, I kinda need to get to my next elective, but I can't just leave Oak looking so morose up there... besides, maybe I could learn something."

menu:
    "{color=#66b77d}[[Knowledge]{/color} >Approach Professor Oak as a student":
        $ TraitChange("Knowledge")
        red @happy "Professor Oak. Would you mind sharing some of your current research with me? It sounds pretty nifty."

    "{color=#e226a6}[[Patience]{/color} >Approach Sam as a friend":
        $ TraitChange("Patience")
        red @happy "Hey, Sam. Wanna tell me about some of your research? Sounds pretty cool."

hide oakbg with dis

pause 1.0

show oak surprisedbrow frownmouth with dis

oak @talkingmouth "You're asking me, lad?"

red @talkingmouth "Of course. You're the world-famous Professor Oak. If you say you're about to discover something exciting, then, as a future Champion, I want to be one of the first to know about it."

oak -surprisedbrow -frownmouth -surprised @happy "Well, lad, I'd be more than happy to tell you!"
oak @talkingmouth "You see, [first_name], the genetic material I've discovered in these meteorite fragments appears to be in a constant state of flux. It's... why, {i}adapting{/i} to its environs."

red @surprised "Whoa."

oak @angrybrow talking2mouth "'Whoa' is quite right. When I prod it with my forceps, it hardens. When I heat it up, it develops holes for ventilation. I've attempted chilling it, and it's actually started vibrating at higher frequencies, generating heat!"

red @closedbrow talking2mouth "What the hell could that be? I don't know of any Pokémon like that..."

oak @happy "Oh? Don't you?"

red @closedbrow talking2mouth "Uh... well, I can't really think of one..."

oak @talking2mouth "What if I were to tell you that you've had an intimate experience with one already?"

red @confused "I'd say you should watch your phrasing. Do you mean Absol?"

oak @closedeyes talking2mouth "Not quite. Your rival's Pokémon...?"

red @surprised "Oh! Right, Eevee! It's got an extremely unstable genetic makeup, right?"

oak @happy "Yes, that's correct! The slightest external stimuli is capable of triggering a massive change in Eevee. No wonder it has so many evolutions."

red @confused "So, what, the meteorite had bits of a space-Eevee in it?"

oak @closedeyes talking2mouth "No, certainly not. Eevee is definitely of terrestrial origin." 
oak @talkingmouth "But the genetic material from this meteorite, which I must assume comes from an unknown Pokémon, demonstrates an adaptability quite similar to Eevee's."
oak @happy "I suspect it would be quite a bit more powerful if we were to find the whole, original, Pokémon, but..."

pause 1.0

red @closedbrow talking2mouth "Since the genetic material is embedded into rock, it doesn't seem likely that the original Pokémon was alive, even before it blew through the atmosphere and crashed into the planet?"

oak @talkingmouth "Essentially. The material might not even be fragments of something larger, and may just be microscopic Pokémon outright."

red @happy "Woah. There could be Pokémon too small to see?"

oak @talkingmouth "The distinction between a germ, a virus, a bacteria, and a microscopic Pokémon would be a hard one to define. Perhaps the work of a biologist."

red @talkingmouth "Right. As opposed to you, who are...?"

oak @closedeyes talking2mouth "A Poké-homo Psychosociologist."

red @confused "Eeesh."

oak @talkingmouth "Yes, there's a reason most people just call me the Pokémon Professor."

pause 1.0

oak @surprised "Oh, dear! You should probably get to your next elective soon, shouldn't you?"

red @happy "Hey, you remembered something about someone else's schedule!"

oak @closedeyes talkingmouth "Well, I {i}am{/i} attempting to get better at that, after you pointed out it was a weakness of mine eleven years ago."

red @talkingmouth "Who said an old Mabosstiff can't learn new moves?"

jump homeroom1transition