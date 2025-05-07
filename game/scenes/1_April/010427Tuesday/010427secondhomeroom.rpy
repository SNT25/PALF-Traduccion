label secondhomeroom010427:

scene blank2

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom behind blank2

show oakbg behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade

$ renpy.music.set_volume(0.1, delay=1.0, channel="music")
$ PlaySound("BellChime.ogg")

$ renpy.pause(2.0, hard=True)
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

oak @talkingmouth "...Seems I'll have to cut this lecture short. Remember! Positive changes go on the numerator. Negative on the denominator. Dismissed!"

hide oakbg with dis

pause 0.5

show leaf blush uniform at rightside with dis

pause 0.5
    
leaf @sadbrow happymouth "Hey."

pause 0.5

red uniform @talkingmouth "Hey. You seem a bit... blushy."

leaf @closedbrow talking2mouth "Yeah. Um... look. I've got a question for you."

red @talkingmouth "Shoot."

leaf @talkingmouth "...Well, uh, maybe we could go somewhere else to discuss this?"

red @confusedeyebrows frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
red @happy "Yeah, sure, I get ya. How's the garden?"

leaf @talking2mouth "Yeah. Okay. Let's go."

pause 0.5

scene clouds
show garden:
    zoom 0.625
with splitfade

narrator "You arrive at the garden. Your heart is beating rapidly as you turn a corner, and Leaf makes a big show of making sure you're alone."

pause 0.5

show leaf uniform blush with dis

red uniform @talkingmouth "Familiar situation here. You going to shove some more money into my hands?"

leaf @talking2mouth "Hah, no. Not this time. I mean, unless you ask for it?"

red @happy "I probably won't. So what's up?"

show leaf:
    ease 1.0 xpos 0.65
    ease 2.0 xpos .35
    ease 1.0 xpos 0.5

pause 0.5

leaf -blush @bigblush closedbrow happymouth "Ah, man, this is difficult. I'm {i}really{/i} not used to saying stuff like this."

red @sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."

show leaf surprisedbrow frownmouth with dis

red @happy lightblush "T-{w=0.5}take your time."

leaf @angrybrow happymouth "Oh my God, did you actually just stutter? Stutter {i}and{/i} blush?"

red @sad2eyes talking2mouth sweat "Uh... that's..."

red @lightblush closedbrow talking2mouth "You're one to talk."

leaf -surprisedbrow -frownmouth -surprised @closedbrow talkingmouth "Yeah... okay. Okay, I'm doing this."

pause 1.0

leaf @talkingmouth "So, like, are you dating anyone?"

if (GetRelationshipRank("Nessa") > 0 and not HasEvent("Nessa", "DenyDate")):
    red @talkingmouth "Yeah, actually. Nessa. Maybe you've heard of her?"

    leaf @closedbrow talkingmouth "Yeah, I've heard of her. She's a model, right? Galarian, so she's got that sexy accent? {i}And{/i} she's rich?"

    red @talkingmouth "Yep, that's the one."

    leaf @talking2mouth "Great. Well, she's an option, then. Um, is it serious?"

    red @talkingmouth "Nah. She actually specifically said that she didn't have time for anything serious, so, you know, she manages expectations well."

    leaf @closedbrow talkingmouth "Okay, great. Because that was going to make this conversation way more awkward."

else:
    red @talkingmouth "Nope."

pause 1.0

leaf @talking2mouth "So, uh, you probably noticed, because I haven't exactly been subtle about it...{w=0.5} but, um...{w=0.5} I kinda like you, and, uh..."

leaf @sadbrow happymouth "Do you want to go on a date? Like, no strings. Just a casual thing. To see if we're, y'know, compatible."

pause 3.0

leaf @sadbrow happymouth "Um. Your silence is scaring me, dude."

red @closedbrow talking2mouth "Sorry. Just thinking about what to say."

leaf @sadbrow happymouth "Okay. Well, um. Do you need... like, hours? Or just a couple minutes?"

red @closedbrow "{w=0.5}.{w=0.5}.{w=0.5}."

$ someoneelse = False

label predate:

menu:
    "Yes. Let's go on a date.":
        $ AddEvent("Leaf", "AcceptedConfession")

        leaf -blush fullblush @surprised "Woah! It was that easy?"
        leaf @happy "I've been psyching myself out over this for, like, weeks now."
        leaf @talking2mouth "If I'd known how easy you were going to make this, I would've asked way earlier."

        pause 1.0

        leaf @closedbrow talkingmouth "I mean, I was hinting pretty heavily... but I guess you can't help being a guy."

        red @confusedeyebrows talking2mouth "Leaf, I totally got your hints. I was returning fire the entire time."

        leaf @talking2mouth "Yeah... well...{w=0.5}{nw}"
        extend @closedbrow talking2mouth " I don't have a comeback for that."

        red @closedbrow talking2mouth "Who says we need a comeback?"

        pause 1.0

        red @talkingmouth "So what does this make us?"

        leaf @closedbrow talkingmouth "Um. Dating. Just dating, I think."

        leaf @talking2mouth "It might become something more, later, but, like, we don't even know what each other's dealbreakers are."

        red @confusedeyebrows talking2mouth "Uh, yeah, I'm going to need to know which way you put the toilet paper before we do anything serious."

        leaf @talkingmouth "Yeah, and you better close the toilet lids before you leave the bathroom."

        red @talkingmouth "Do you take decaf or full-caff coffee?"

        leaf @closedbrow talkingmouth "Are you going to want a motorcycle? Guys always want motorcycles."

        python:
            hascyclizar = False
            for mon in AllPokemon():
                if (mon.GetId() == pokedexlookupname("Cyclizar", DexMacros.Id)):
                    hascyclizar = True
                    break

        if (hascyclizar):
            red @happy "Nah, I've got a Cyclizar."

            leaf @surprised "Oh, right, that's cooler, actually."

        else:
            red @angrybrow happymouth "Oh, yeah, I'm definitely going to want a motorcycle. They're seriously cool."

            leaf @talking2mouth "Alright. As long as I get a minivan."

        leaf @talkingmouth "Well... that's, um... that's great. I'm really happy that you think I'm cool enough to hang out with."

        red @talkingmouth "You're more than cool, Leaf. You're ice cold."

        leaf @happy "So... you down to go on a date on Sunday?"

        red @talkingmouth "Sure."

        leaf @talking2mouth "Cool. I know you're super busy with your Student Council stuff, and the elections are Saturday, so Sunday should be a nice break from all that."

        leaf @flirttalk "I'll be expecting you to plan our future dates, though."

        red @surprised "Woah. You're already planning future dates? What if I totally blow the first one?"

        leaf fullblush @talking2mouth "Confession time. I, uh... I actually considered that trip into the fields our first date. And the shopping trip, too."

        red @confused "Huh."

        leaf @talking2mouth "You should try going on dates with people who don't know you're going on a date with them. It's pretty great. All the fun, none of the obligation."

        red @closedbrow talking2mouth "I think that might be called 'stalking?'"

        leaf @talking2mouth "Well, that's for the jury to decide."

        pause 0.5

        leaf @talkingmouth "Hey. I think this'll be really great. For us, I mean."

        red @talkingmouth "Well, the best part is, whether or not it's great is up to us."  

        leaf @happy "Heh heh. I can't wait for our {color=#0048ff}date{/color}."

        pause 0.5

        hide leaf with dis              

        $ oldrelationship = GetRelationship("Leaf")
        $ persondex["Leaf"]["Relationship"] = "Date"

        $ PlaySound("sav.ogg")

        narrator "Your heart shifts as you feel your relationship with Leaf evolve from '{color=#0048ff}[oldrelationship]{/color}' to '{color=#0048ff}Date{/color}'!"

    "No. Sorry.":
        $ AddEvent("Leaf", "RejectedConfession")

        leaf -fullblush surprised "Oh. Is...{w=0.5} is that...{w=1.0} {i}why?{/i}"

        red @sadbrow talking2mouth "Ah, don't ask that, Leaf. Look, you're a good friend. I just don't think we should mess that up."

        leaf sadbrow frownmouth -surprisedbrow -frownmouth -surprised @surprised "Is it... is it the snark? I can tone down the snark. Really. That's {i}not{/i} a mandatory part of my personality."

        red @happy "Nah. I don't want you to change anything about yourself."

        leaf @sadbrow talking2mouth "Well. Um. I... I don't really know what to do."

        leaf @closedbrow talkingmouth "I've...{w=0.5} I've never gotten rejected before, so...{w=0.5} um...{w=0.5} I just...{w=0.5} I just need to...{w=0.5}"

        hide leaf with dis

        pause 1.0

        redmind @sadbrow frownmouth "I mean... I like her. I really like her, a lot. But she's so pushy, and I'm really not sure if she genuinely {i}could{/i} turn off the snark. I just need to--"

        show leaf uniform frownmouth with vpunch

        leaf @angry "No, y'know, what, I'm not going to crawl off, sobbing like a little girl. I am a goddamn {i}woman{/i}, and I am going to handle this maturely."

        red @surprised "!"

        leaf @talking2mouth "Okay, so, obviously, I'm really disappointed. But you're still an awesome guy, and a good friend."

        if (GetRelationship("Leaf") == "Bestie"):
            leaf @talking2mouth "We're besties. {i}Besties.{/i}"

        leaf @talking2mouth "I'm not going to mope around and ruin that. So... yeah."

        red @sadbrow talkingmouth "I'm glad. I {i}do{/i} like you. I want to stay friends."

        pause 0.5

        leaf @sadbrow happymouth "Like broken glass in my heart, Skippy."

        red @sad "{w=0.5}.{w=0.5}.{w=0.5}."

        leaf @talking2mouth "So. I accept your rejection. For now."

        red @talkingmouth "Uh... thanks?"

        leaf @closedbrow talkingmouth "Yeah, you're welcome. But I want you to know I'm going to work on you. And the next time I ask, it won't be {i}your{/i} decision."

        red @closedbrow talking2mouth "...Well, I can't say I hate the thought of you working so hard on me. But... don't overdo it, alright? Friends {i}is{/i} enough."

        leaf @flirttalk "For now."

        pause 0.5

        leaf -frownmouth @sadbrow happymouth "For now." 
        
        leaf @talkingmouth "Now, I'm off. Got some plans to make."

        leaf @flirttalk "And, yes, you're involved in at least half of them. I'm in hot {color=#0048ff}pursuit{/color}."

        pause 0.5

        hide leaf with dis

        $ oldrelationship = GetRelationship("Leaf")
        $ persondex["Leaf"]["Relationship"] = "Pursuit"

        $ PlaySound("sav.ogg")

        narrator "Your heart shifts as you feel your relationship with Leaf evolve from '{color=#0048ff}[oldrelationship]{/color}' to '{color=#0048ff}Pursuit{/color}'!"

    "I'm interested in someone else." if (not someoneelse):
        $ AddEvent("Leaf", "PolyAlright")
        $ someoneelse = True
        
        leaf @talking2mouth "I figured. I mean, a guy like you, you've got to have tons of options, right? Besides Tia, I'm sure there are other girls who are into you."

        pause 0.5

        leaf @closedbrow talkingmouth "Probably a few guys, as well."

        pause 0.5

        leaf @talking2mouth "But, look, that doesn't matter to me."

        red @surprised "Huh?"

        leaf @talking2mouth "Look, in fourth grade, I had two boyfriends, okay? I'm used to this. We'll start out with casual dating, and if we decide to move to something more permanent, then... we'll discuss it with the others. Okay?"

        red @closedbrow talking2mouth "I think you're deciding things for yourself again. Also... I've never even had a partner before. Besides [pika_name], anyway. I'm not sure I want to jump feetfirst into the water like that."

        leaf @sarcastic "Believe me, I know what it's like to want to avoid the water."

        leaf @sadbrow happymouth "But... like, you don't know if you hate something until you try it, right?"

        red @closedbrow talking2mouth "I guess. I just always had this mental image that someday I'd marry a girl, buy a house with a white-picket fence, and have four kids."

        leaf @surprised "Uh... moving a bit fast, aren't you?"

        red @talkingmouth "I'm just trying to make a point."

        pause 1.0

        red @closedbrow talking2mouth "But I guess that mental image has gotten a bit fuzzier ever since I realized I like guys, too. Maybe there's more people in that house than I thought."

        leaf @happy "Right? I {i}promise{/i}, I won't stop you from dating other people. I just..."

        pause 0.5

        leaf @sadbrow happymouth "I just want my own crack at you. Please?"

        jump predate

pause 1.0

red @talkingmouth "Wow."

redmind @frownmouth "Not how I expected this day to go."

pause 1.0

red @closedbrow talking2mouth "Ah, dang it. I forgot to ask for help putting up these posters. I guess I'll do that now, then before I really get my freetime..."

call freeroam from _call_freeroam_11

call texting from _call_texting_8

jump day010428