label lunch010428:

redmind uniform @thinking "Hm... I think I might go for a gazpacho today."

redmind @happy "I don't know what it is, but it sounds good!"

show hilda uniform at leftside 
show tia uniform at centerside 
show whitney uniform at rightside
with dis

pause 1.0

hilda @surprised "Oh, [first_name]! Great, maybe you can help me figure this out."

red @talkingmouth "Sure, what's up?"

whitney @talking2mouth "Hilda was just asking me if I knew who the pineapple-haired guy hanging out with Hilbert all the time is."

red @confused "Pineapple-haired?"

hilda @talkingmouth "Yeah, Whitney told me his name is Nathan. So who {i}is{/i} this guy?"

redmind @thonk "{i}Nathan?{/i}"
red @talkingmouth "Um... he's just another student, as far as I know."

hilda @closedbrow talking2mouth "You're Hilbert's roommate. Do you know why he's spending time with someone else?"

whitney @angrybrow happymouth "Oh, are you jealous?"

hilda @surprised "What? No! I'm... shit, I dunno, concerned? Hilbert doesn't 'hang out' with people unless he's forced to."
hilda @sad "So, like, that must mean that Nate's got something on Hilbert, right? I'm just worried about what that is."

tia @talkingmouth "Is it a bad thing, if Hilbert spends time with other people?"

hilda @surprised "Huh? Well, no, I guess not. Hell, I've been trying to convince him to be more social for our entire lives."
hilda @closedbrow talkingmouth "But... you know, him suddenly finding a new best friend is concerning."
hilda @sad "There's... gotta be something that caused it, right?"

tia @talkingmouth "Maybe, but I don't think him finding a new friend is something you need to worry about."

red @talkingmouth "I agree. I just battled them in Gym Class, and they seemed fine enough. I kinda got the vibe they were working on some big secret."

red @confused "Is your birthday coming up?"

hilda @talkingmouth "Not for a long while. March 4th."

red @closedbrow talking2mouth "Beats me, then."

hilda @talkingmouth "Shit. Guess I just have to ask Hilbert, then. But I don't want him to think that I'm not {i}encouraging{/i} new friendships..."

whitney @talking2mouth "So... just out of curiosity, since I did that little favor for you, would you mind doing a favor for me?"

hilda @surprisedbrow frownmouth "Hm?"
hilda @happy "Shit, of course! What's up?"

whitney @happy "Go ahead, Tia."

tia lightblush sadbrow @happymouth "Um... my hat got ripped. Do you know how to repair it? My fingers aren't small enough..."

hilda @closedbrow talking2mouth "Your fingers? You've gotta have way smaller fingers than me, at your size. But, hell yeah, that'd be a piece of cake. Just a bit of darning."

tia @talkingmouth "Thank you!"

hilda @talkingmouth "No problem."

red @talkingmouth "Hey, how'd your hat get a rip, though? I've seen how carefully you take care of it. What happened?"

whitney @talking2mouth "It was the weirdest thing. We were just in Inspira, walking by the seaport, when--"

tia -lightblush @angrybrow frownmouth "I was in the city when this really big, bad, and angry person stole my hat!"

red @surprised "Again?"

whitney @surprisedmouth "Um, she said 'person,' but it was a Pokémon, wasn't it?"

tia sadbrow frownmouth @talkingmouth "...Yes. But Pokémon are people."

hilda @closedbrow talking2mouth "I mean... one of those Pokémon-rights organizations in Unova said that, but most people wouldn't agree."
hilda @sad "They ended up being terrorists, anyway."

pause 1.0

tia @sad2brow talking2mouth "Does that mean... um... you don't think I'm a {i}person?{/i}"

whitney @surprised "What? No, of course you are, sweetie! You're a human!"

pause 1.0

tia @sad2eyes happymouth "Hah! Of course. I'm a human. Hah hah."

whitney @happy "C'mon, Tee, you're probably lightheaded from all that running around you've been doing. Let's get you some fish."

tia @sad2eyes talking2mouth "I {i}do{/i} like fish..."

pause 1.0

tia @talking2mouth "[first_name]? Do you think a Pokémon can be a person?"

menu:
    "No way.":
        pass

    "Sure, they all are.":
        $ ValueChange("Tia", 3, 0.5)

    "Maybe some of them.":
        $ ValueChange("Tia", 2, 0.5)

tia @closedbrow talking2mouth "Hmm..."

hide tia 
hide hilda
hide whitney
with dis

pause 1.0

redmind @thinking "Big, bad, and angry? Sounds like another one of those frenzied Pokémon that I've been seeing around."

menu:
    "{color=#66b77d}[[Knowledge]{/color} I should investigate.":
        $ TraitChange("Knowledge")

    "{color=#ff8412}[[Courage]{/color} I should fight it!":
        $ TraitChange("Courage")

redmind "[bluecolor]The next time I go to the city, I should see if I can find that Pokémon. By the seaport, right? There are probably some new Pokémon to catch there.{/color}"

pause 0.5

redmind @thinking "Hm. Maybe I should talk to Sam about these frenzied Pokémon. If he figures out what's happening, and this hasn't happened before, maybe I could be the one to name them!"
redmind @happy "Maybe something like... Frenzied Overpowered Enemy? Or Fantastically Outraged Executor? Maybe Fierce Opposing Entity?"

if (GetRelationship("Sabrina") == "Friend"):
    redmind @surprised "[sabrinacolor]It sounds like you're really trying to force the acronym F.O.E.{/color}"

    redmind @angrybrow frownmouth "Hey! Sabrina, I don't step into {i}your{/i} mind and judge how {i}you{/i} name things."

    redmind @closedbrow frownmouth "[sabrinacolor]...Apologies.{/color}"

    pause 1.0

    redmind @closedbrow sweat talkingmouth "[sabrinacolor]I like the third one most.{/color}"

else:
    redmind @happy "...Nah, that's silly."

jump PickTable