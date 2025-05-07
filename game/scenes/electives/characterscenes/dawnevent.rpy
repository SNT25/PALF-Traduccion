label dawnevent:

if (IsAbsent("Dawn", location.title())):
    return

if (not persondex["Dawn"]["Named"]):
    narrator "You spot an unfamiliar student and go to greet her."
    
    show dawn uniform with dis

    red uniform happy "Hi th--"

    dawn surprised "Hi there! You're Dawn, what's my name?"
    dawn surprisedbrow frownmouth "[ellipses]"

    red surprised "...Uh, come again?"

    dawn sadbrow @closedbrow sadmouth "I... I was thinking about what I was going to say if you came over for five minutes, and..."

    red happy "Ah, you got tongue-tied? That's alright!"
    red @talkingmouth "So, I guess that your name's Dawn?"

    $ BecomeNamed("Dawn")
    dawn @sadmouth "Yes..."

    red @talkingmouth "Cool. I'm [first_name], from Pallet Town. Where're you from?"

    dawn @happy "Oh, I live in Snowpoint City! In Sinnoh!"
    dawn @sadmouth "W-wait... no, I don't. I {i}lived{/i} there. I actually live here. Because I'm a student. Who goes to this school."
    dawn @closedbrow sadmouth "{size=30}Help me.{/size}"

    red @sadeyes sadeyebrows talkingmouth "Seems like you're a bit nervous."

    dawn @closedbrow sadmouth "I just... think about what I should say before I say it. But I think about it so hard that I say the wrong thing when it's time to actually say it."

    red @happy "Shouldn't affect your skills as a trainer. Your Pokémon only need to understand a couple words when you're commanding them in battle, right?"

    dawn @sad "...In battle? Yeah..."

    red @happy "You don't sound enthused. Not into battling?"

    dawn @closedbrow sadmouth "Not really."

    red @talkingmouth "Huh. I guess you're more of a Contest Coordinator, then?"

    dawn @talkingmouth "I've done a {i}lot{/i} of it, but... no."

    red @surprised "Uh, you want to study Pokemon? Like, as a Professor or Research Assistant!"

    dawn @sad "{size=30}...No.{/size}"

    red @closedbrow sweat talking2mouth "Uh... Musical coordinator? Ranger? Groomer? Breeder?"

    show dawn:
        ypos 1.0
        ease 0.5 ypos 1.2

    dawn @closedbrow sadmouth "{size=30}Can you please stop?{/size}"

    red @sadeyes sadeyebrows talkingmouth "Oh, geez, sorry. Hey, I didn't mean to harass you."

    dawn @sadbrow happymouth "It's... not your fault. I'm just... a freak."

    red @angry "Woah, hey, what? I'm sure that's not true."
    red @sad2eyes sadeyebrows frownmouth "[ellipses]"
    red @sadbrow talkingmouth "Hey, why don't you tell me what you want to do with Pokémon, huh?"

    dawn @sad "{size=30}...I don't.{/size}"

    red @confused "Huh?"

    show dawn: 
        ypos 1.2
        ease 0.2 ypos 1.0

    dawn @angrybrow surprisedmouth "{size=50}I don't, okay!{/size} I don't want to do anything with Pokémon."

    red @confused ".{w=0.5}.{w=0.5}.{w=0.5}I don't understand."

    dawn @sadbrow talkingmouth "No-one does. Even I don't. I get that I should love them. Everyone else does. And I don't, like, have a good reason to not be into them. But... I just want to..."

    pause 1.0

    dawn @closedbrow sadmouth "I'm sorry for taking your time! And I'm sorry for oversharing! And I'm sorry for overapologizing! And I'm sorry for running away!"

    hide dawn with dis

    pause 2.0

    narrator "Dawn quickly skips away and takes a new seat at the far corner of the classroom."

    redmind @wince frownmouth "...That could've gone better."

    hide dawn

return