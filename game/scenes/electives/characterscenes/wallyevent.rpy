label wallyevent:

if (IsAbsent("Wally", location.title())):
    return

if (not HasEvent("Wally", "ClassIntro")):
    narrator "You spot a familiar student and go to greet him."
    
    show wally uniform with dis

    pause 0.5

    red uniform @happy "Hi there!"

    wally @talkingmouth "Oh. Hi."

    if (classstats[location.title()] > 0):
        red @talkingmouth "Don't think I've seen you in this class before. Is it your first time taking this class?"

    else:
        red @talkingmouth "This is my first time taking this class. What about you? Is it your first time, too?"

    wally @embarrassedmouth sideeyes "No, I just... {w=0.5}{i}Cough{/i}{w=0.5} usually sit in the back corner."
    wally @lightblush happyeyes "I'm a little bit shy, I guess... hah hah..."

    if (not persondex["Wally"]["Named"]):
        $ BecomeNamed("Wally")

        wally @surprised "Oh! Um, I don't think I introduced myself. I'm Wally. And you're [first_name], of course."

        red @happy "Pleasure. Wally, you said?"

        wally @sadeyebrows sadeyes talkingmouth "Yes. But, um... don't tell too many people..."

    red @closedbrow "{w=0.5}.{w=0.5}.{w=0.5}."
    red @talking2mouth "You know... if you're hiding from someone, you wouldn't be the only one."

    show wally surprisedbrow sadmouth with dis

    wally @surprisedbrow surprisedmouth "How did you...?"

    red @sadbrow talkingmouth "You thought taking a swan dive onto the arena floor was a preferable alternative to being on a camera for a few minutes during the Quarter Qlashes."

    wally @closedbrow sweat "Ah."
    wally -sadmouth -surprisedbrow @happy "Yeah, that {w=0.5}{i}Cough{/i}{w=0.5} would do it."
    wally @sad2eyes talkingmouth "Just out of curiosity, but... how would {i}you{/i} have handled that?"

    red @closedbrow talking2mouth "Hm."
    red @talkingmouth "Well, if your intention is to avoid attention, probably just saying a firm 'no thanks', as soon as Lisia looked over at you would do it."
    red @happy "She seems like she'd respect that and keep the camera moving, without anyone even noticing."

    wally @sadbrow talkingmouth "Yeah... you're right. I panicked, though, and I thought..."

    red @talkingmouth "Hey, are you in any actual {i}danger{/i}? If this is serious, there are people who can {i}really{/i} help you."

    wally @surprisedbrow lightblush "{w=0.5}.{w=0.5}.{w=0.5}."
    wally @talkingmouth "Please teach me?"

    red @confused "What?"

    wally surprisedeyes @talkingmouth "Please, teach me how to be a strong trainer, like you. How to be cool, and calm, and kind, even after what happened to you."

    red @happy "Hey, you're making me blush!"

    wally fullblush sadeyebrows shineeyes @happymouth "I... I admire you! I think you're really, {i}really{/i} cool! And I know I can't be like you, but... but I want to be! So please teach me!"

    narrator "Wally's passion begins to attract the attention of the rest of the crowd."

    wally @surprisedmouth "I-I'll... I'll study as hard as I need to! I'll carry all your books! I'll even go to the gym! But I need to be as strong as you before... before..."
    wally -fullblush -sadeyebrows -sadeyes @sadeyes sadeyebrows "Before it's too late."

    show wally surprisedeyes sadmouth with dis

    red sadeyebrows @talkingmouth "Wally, calm down."

    show wally sadeyes with dis

    pause 1.0

    wally @talkingmouth "I... can't explain why, but... this means {i}so{/i} much to me."
    wally @talkingmouth "Please."

    pause 1.0

    show wally shineeyes with dis

    red @talking2mouth "I'm not a teacher. I'm not qualified to do what you're asking, and there are dozens of strong trainers around who {i}are.{/i}"

    pause 1.0

    narrator "You pause, studying Wally's reaction. You expected him to argue, or perhaps get upset, or at the very least interrupt you and try to continue his point."
    narrator "But he doesn't. He silently stares up at you, eyes full of hope."

    pause 0.5

    narrator "He looks a little like Blue did, many, many, {i}many{/i} years ago. Sans the hair, of course."

    pause 1.0

    show wally surprisedeyes with dis

    red @talking2mouth "I can't be a teacher. But if I can help a friend out, by telling him what little I've learned as a trainer-student... I'll do that."

    pause 1.0

    wally -surprisedeyes smilemouth @talkingmouth "...You will? We can be friends? And you'll tell me what you know?"

    red @happy "Sure. Just don't get your expectations too high. I only started training at the beginning of the school year, same as you."

    show wally:
        ease 0.3 ypos 1.1
        pause 0.3
        ease 0.3 ypos 1.0

    wally @happy lightblush "{size=30}Yes!{/size}"

    narrator "Wally ineffectually attempts to hide a fist-pump."

    wally @happy "Thank you! Thank you so much!"

    wally @talkingmouth "When should... {w=0.5}{i}Cough{/i}{w=0.5} um, when?"

    red @talkingmouth "I'll find you. Oh, wait, do you have a phone?"

    wally @lightblush "Y-yeah."

    $ BecomeContacted("Wally")

    $ wally_name = "Senpai"

    wally @happy "Th-thanks, [wally_name]!"

    red @frownmouth confusedeyebrows "{w=0.5}.{w=0.5}.{w=0.5}."

    menu:
        "You know what, I can dig it.":
            wally @happy "G-great! {w=0.5}{i}Cough.{/i}{w=0.5} I wasn't sure, but it... it just kinda felt right..."

            wally @shineeyes happymouth "Heh heh."

        "Let's try something else.":
            wally @sadeyes sadeyebrows embarrassedmouth "Oh. Um, okay. What should I call you, then...?"

            $ wally_name = renpy.input("What would you like Wally to call you?", default=first_name, exclude="{}[[]%<>", length=12)

            wally @happy "Oh, okay! [wally_name]! That sounds good."

        "Absolutely not.":
            $ wally_name = first_name
            wally @sad "Oh. Sorry, [wally_name]."

    pause 0.5

    wally shineeyes happymouth "Thanks, [wally_name]. Thank you, {i}so{/i} much. I really appreciate this."

    red @happy "Can't wait to get started."

    hide wally with dis

    pause 2.0

    $ AddEvent("Wally", "ClassIntro")

return