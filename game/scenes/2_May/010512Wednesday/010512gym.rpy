label gym010512:

$ HealParty()

play music "Audio/Music/Gym_Start.ogg" noloop
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

alder @talkingmouth "And that's why maintaining weather conditions should always be your number-one priority. Overwriting your opponent's weather with your own is a two-for-one! Now, let's get onto the battles."

bruno @norm2 "[first_name], you will be battling Wallace."

red uniform @surprised "WHAT?!"

hide bruno 
hide alder
with dis

pause 1.0

$ BecomeNamed("Wally")

show wally uniform with dis

wally @happyeyes sadeyebrows talkingmouth "That's, um, 'Wally', actually. It's not short for anything. Just Wally."

if (not HasEvent("Wally", "ClassIntro")):
    $ wally_name = first_name
    if (persondex["Wally"]["Named"]):
        red @talkingmouth "Oh, hey, Wally. I think Yellow mentioned you."

        wally @sideeyes talkingmouth "Y-yeah. She mentioned you, too. Of course, I uh, I knew about you before, from the Frienergy thing..."
        wally @sadbrow talkingmouth "Sorry, you probably didn't want to think about that again."

        red @sadeyebrows talkingmouth "It's kinda unavoidable."

        wally @sideeyes "{w=0.5}.{w=0.5}.{w=0.5}."

    else:
        red @talkingmouth "Oh, hey. I think I saw you during the Quarter Qlashes?"

        wally @sideeyes talking2mouth "You and everyone else."

    redmind @thinking "This guy seems uncomfortable around me. Or maybe he's just uncomfortable in general."

else:
    red @happy "Hey, Wally."

    wally @sadeyes embarrassedmouth "H-hi, [wally_name]."

    pause 1.0

    redmind @happy "He looks embarrassed. Maybe he's remembering all that stuff he said in class..."

menu:
    ">Mention the Quarter Qlashes":
        $ AddEvent("Wally", "MentionQuarterQlashes")
        red @talkingmouth "How'd your Quarter Qlash matches go?"

        wally @unamusedeyebrows talkingmouth "I barely won. Without a miracle, there's no way I'm getting through the second round."

        red @confused "Is that important? I think we get full marks just for participating in the Quarter Qlashes, don't we?"

        wally @talkingmouth "Yeah, but... I need to get more powerful, and barely-wins like this won't cut it."
        wally @sadbrow talkingmouth "I tried out for the Battle Team, you know, and... {i}cough.{/i} Advisor Lance didn't even look at me. Not once. Not during that entire time."
        wally @sadbrow happymouth "He was too busy staring at {i}you.{/i}"

        red @sadbrow talkingmouth "...If it's any consolation, you don't {i}want{/i} Lance's attention."

        wally @surprised "Really?"

        red @talkingmouth "Yeah, he's a bit of a dick."

        wally @sadbrow talkingmouth "Oh. That's very disappointing."

        pause 1.0

        redmind @closedbrow frownmouth "Well, that was a bust."

        wally @talkingmouth "Let's just... let's just do our battle now."

    ">Start the battle":
        red @talkingmouth "Ready to battle?"

        wally @talkingmouth "Huh? Oh, yeah. {i}Cough.{/i} Let's, um, do this."

python:
    trainer1 = MakeRed(3)
    trainer2 = Trainer("wally", TrainerType.Enemy, GetTrainerTeam("Wally"), number=3)

call Battle([trainer1, trainer2], uniforms=[True, True]) from _call_Battle_129
$ battlehistory["Wally1"] = _return

play music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

if (not WonBattle("Wally1")):
    show wally uniform surprised with dis

    wally @talkingmouth "I... I won?"

    red @happy "You sure did."

    wally -surprisedbrow -frownmouth -surprised @closedbrow talkingmouth "...You were going easy on me."

    red @confused "What?"

    wally @sadeyebrows talkingmouth "Come on, give me a little-- {i}Cough{/i}-- credit. You're the guy who can make Pokémon listen to him instantly."
    wally @sadeyebrows happymouth "You've got the special Pikachu that can change types and beat an Altaria four times its level."
    wally @happy "There's no way I could {i}really{/i} win."

    red @sad2eyes frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    wally @sadbrow talkingmouth "I'll see you around."

    jump endwallybattle

show wally uniform sadbrow with dis

$ ValueChange("Wally", 3, 0.5)

wally @talkingmouth "Man, that figures."

red @confused "What?"

wally @sadeyebrows talkingmouth "Come on, give me a little-- {i}Cough{/i}-- credit. You're the guy who can make Pokémon listen to him instantly."
wally @sadeyebrows happymouth "You've got the special Pikachu that can change types and beat an Altaria four times its level."
wally @happy "There's no way I could win."

red @sad2eyes frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

wally @sadbrow talkingmouth "I'll see you around."

menu:
    ">Give him advice":
        $ AddEvent("Wally", "AdviceGiven")
        red @talkingmouth "Hold on."

        wally -sadbrow @talkingmouth "Hm?"

        red @talkingmouth "Maybe you're right, I've got a few more advantages here. But you're not taking advantage of all {i}your{/i} advantages."

        narrator "For a moment, it's unclear how Wally is taking this. You're concerned you'd insulted him, but then--"

        wally @sadeyes lightblush talkingmouth "Um... would you mind explaining more?"
        
        if (not HasEvent("Wally", "Class Intro")):
            wally @lightblush talkingmouth "I only recently got into Pokémon, and I think I might not understand them as well as you."

        red @happy "It's no problem, man."

        if (HasEvent("Wally", "Class Intro")):
            red @happy "I said I would, didn't I?"

        wally @happymouth "Thank you."

        narrator "Wally pulls out a Politoed-themed notepad, and begins scribbling something on it, looking up at you expectantly."

        red @talkingmouth "Well, the first thing is that you're spreading your types too far apart. With your five Pokémon, you've only got one overlapping type, and that's Normal, on your Swablu and Skitty."

        wally @closedbrow talkingmouth "Okay, okay..."

        red @talkingmouth "Most of the time, you want to limit yourself to a smaller number of types, until you have a solid grasp on what your Pokémon at that level can do." 
        red @happy "When all your Pokémon are on-track for the level you should probably be, {i}that's{/i} when you can start spreading out."

        wally @closedbrow talkingmouth "Okay... I get that. {i}Cough.{/i} Go deep before I go wide."

        red @talkingmouth "Yeah, that's why your Pokémon are a bit underleveled right now. The second thing is that none of your Pokémon have any special moves that our elective teachers can teach them."

        wally @closedbrow talkingmouth "Okay, I {i}have{/i} heard about those moves... but they didn't seem like they were worth it. None of them even do damage, right?"

        red @talkingmouth "Only one of the ones you get for passing the first exam does, but later ones will. But damage isn't everything."
        red @talkingmouth "If a move gives you an extra opportunity to attack, using it is just as good a use of your time as attacking twice."
        red @happy "Often better, because it might give you more opportunities later on in the battle."

        pause 1.0

        wally @talkingmouth "Okay... yes, I get it, now. This makes sense."
        wally @lightblush talkingmouth "Thanks for telling me this stuff. I'm sure it must seem very basic to you, but it means a lot to me."

        red @talkingmouth "Hey, I'm just happy to help. Once you nail down some of those issues, I'm sure you'll be an awesome battler."

        show wally smilemouth lightblush sadbrow with dis

        $ ValueChange("Wally", 1, 0.5)

        wally @talkingmouth "Th-thanks."

        Character("Scoffing Jerk") "\"{size=30}...tch. Look at the freak, picking on the sick kid--{/size}\""

        wally -lightblush -smilemouth -sadbrow @angry "Hey! You-- {w=0.5}{i}Cough{/i}-- be quiet! [wally_name] was just battling seriously!"
        wally @angry "That's what {i}any{/i} trainer should do!"

        Character("Scoffing Jerk") "\"{size=30}Whatever...{/size}\""

        pause 1.0

        wally @sadbrow talkingmouth "...Guess you're getting a lot of that?"

        red @happy "I don't always get someone standing up for me. That means a lot. Thanks."

        wally lightblush happy "It's alright. Thanks for helping me."

    ">Let him go":
        Character("Scoffing Jerk") "\"{size=30}...tch. Look at the freak, picking on the sick kid--{/size}\""

label endwallybattle:

hide wally with dis

pause 1.0

show alder:
    xpos 0.66

show bruno:
    xpos 450
with dis

jump lunchtransition