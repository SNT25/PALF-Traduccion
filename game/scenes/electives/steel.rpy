label steelelective:

$ renpy.transition(dissolve)
show screen currentdate

scene map
show blank2:
    alpha 0.8

show classroom with dis

show steeltype:
    xalign 0.5 yalign 1.0

############################################################################################################################################################################################################################
#### 13. STEEL       #######################################################################################################################################################################################################
############################################################################################################################################################################################################################
$ renpy.pause(1.0, hard=True)

$ location = "steel"
$ passedclass = False

call hildaevent from _call_hildaevent_2
call nateevent from _call_nateevent_2
call jasmineevent from _call_jasmineevent_1
call ethanevent from _call_ethanevent_16

label aftersteelsetup:

if (HasEvent("Instructor Byron", 2.1)):
    menu:
        "{b}>General Studies{/b}":
            pass

        ">Ask for move tutoring":
            jump movetutorsteel

        ">Craft items" if (HasEvent("Instructor Byron", 3.1)):
            jump itemcraftsteel

if (not HasEvent("Instructor Byron", 1)): #first class
    $ AddEvent("Instructor Byron", 1)
    $ renpy.pause(1.0, hard=True)

    show hilda uniform sad at rightside with dis
    show hilbert uniform angry at leftside with dis

    red thinking uniform "Well, there's Hilbert and Hilda. They're looking... well."
    ethan uniform happy "Yeah, I don't think we should pull the pin on that grenade. Let's sit somewhere else."

    hide hilda at rightside with dis
    hide hilbert at leftside with dis

    pause 1.0

    show byron happy2:
        xpos 900 yalign 1.0 alpha 0.0
        ease 1.25 xpos 800 alpha 1.0

    byron "[timeOfDay], students."
    show byron happy with dis

    red @talkingmouth "What's with the shovel and cloak? Is this an archeology class?"
    ethan @closedbrow talking2mouth "Maybe he's on his way back from conquering a castle?"
    red -thinking @confusedeyebrows talking2mouth "Huh?"
    ethan @happy "Y'know, like a castle full of rats, with a big knight at the end! Like in a video game?"
    red @talkingmouth "Ethan, what the hell are you talking about?"
    
    byron angry2 "Hey! You two. What're your names?"

    ethan surprised "Ah, shit, sorry, Sir. I'm Ethan."

    red sad "[first_name], Sir."

    ethan sad "That was totally my fault, Sir. I distracted [first_name], so if you're going to punish someone, it should be me."

    byron ".{w=0.5}.{w=0.5}.{w=0.5}"
    byron norm2 "I respect you standing up for your friend. Don't let me catch you doing it again, though."

    if (not (calDate.month == 4 and calDate.day == 5)):
        byron "Hm... you two are new to this class, aren't you?"

    $ BecomeNamed("Instructor Byron")
    byron "I'm Byron, your {color=#0048ff}Steel class{/color} teacher."

    byron angry2 "I'll let you know up front: there won't be any coddling in this classroom."

    show byron angry:
        xpos 800 alpha 1.0
        ease 1.0 xpos 750 alpha 0.0

    show byronbg:
        alpha 0.0 yalign 1.0 xalign 0.5
        pause 1.5
        ease 0.5 alpha 1.0

    $ renpy.pause(1.0, hard=True)

    byron angry2 "If you want to succeed as a Pokémon trainer, poor confidence and a weak character will be crippling liabilities."
    byron norm4 "You've got to build up your own strength--prove to {i}yourselves{/i} that you can stand on your own two feet."
    byron norm2 "I can guarantee you that if you work hard and persevere through the hardships in life, there's nothing you can't do.{w=0.5} But that's easier said than done."
    byron norm4 "Like Steel Pokémon, you have to be resilient, determined, but not too forceful to the point of antagonizing others."
    byron norm4 "Be tough and guarded, but not to the point where you start putting up walls."
    byron norm2 "...Ahh, listen to me monologuing. Sorry for starting things off on such a serious note. Just keep your heads down, take your licks on the chin, and you're gonna do great."

    show hilbert_hildaintro:
        subpixel True
        alpha 0.0 xalign 0.5 zoom 1.0
        parallel:
            ease 1.5 alpha 1.0
        parallel:
            ease 5.0 zoom 0.75

    hilbert uniform "That's the most absurd thing I've ever heard."

    hilda uniform angry "Shhh!"

    byron norm3 "What was that?"

    hilda surprised "Uh, nothing. He was just asking something."

    hilbert angry "Yeah, what sort of 'teacher' would waste our time with such meaningless platitudinal drivel when we--"

    show hilbert_hildaintro at vpunch
    
    hilda angry "Hilbert! Shut up!"

    if (IsDate(5, 4, 2004)):
        byron @norm4 "You two. What are your names?"

        hilda @talkingmouth "Hilda, Sir."

        hilbert @talkingmouth "Hilbert."

    byron @norm4 "Hilda and Hilbert. If you have something on your mind, say it now."

    hilda surprised "No! There's nothing on our mind."
    hilda angry "{size=30}{i}Right,{w=0.3} {cps=7}Hilbert?{/cps}{/i}{/size}"

    hilbert angry "[ellipses]"
    hilbert sad "Right."

    byron "...That's what I thought."
    byron "But keep the noise level down!{w=0.5} Disrupting the class will affect your grade!"

    hilda -angry @talkingmouth "Yes, Sir."

    show hilbert_hildaintro:
        alpha 1.0
        pause 1.0
        ease 1.0 alpha 0.0

    hilbert angry "You always do this. {size=36}When{/size} {size=34}are{/size} {size=32}you{/size} {size=30}go{/size}{size=30}ing{/size} {size=28}to{/size} {size=26}st{/size}{size=24}op{/size} {size=22}trea{/size}{size=22}ting{/size} {size=20}me{/size} {size=18}like...{/size}"

    pause 1.0

    byron @norm2 "Well, now that we're all acquainted, let's get started on the lecture."

    narrator "Byron tells the class some of the finer points of raising and battling with Steel-type Pokémon."
    narrator "Apparently, the process is ten percent luck, twenty percent skill, fifteen percent concentrated power of will, five percent pleasure, and fifty percent pain."

    byron "Remember everything I told you today!"
    byron "Dismissed!"

    hide byron
elif (not HasEvent("Instructor Byron", 2.1) and classstats["Steel"] >= 10):#Metallize
    show byron with dis
    if (not HasEvent("Instructor Byron", 2)):
        $ renpy.pause(1.0, hard=True)

        narrator "The class is researching the diets of Steel-type Pokémon. You're nearly finished penning an essay on the eating habits of Forretress when Instructor Byron shows up."

        byron angry @angry2 "[first_name]!"

        redmind uniform @thinking "Oh, crap, what'd I do? Instructor Byron's intense..."

        byron @angry2 "[first_name], I want to talk to you about the last assignment you turned in."

        red @closedbrow talking2mouth "Oh, uh, the one about... Aron relocation efforts in Hoenn, right? How they were eating up the railways, and--"

        byron norm3 @norm4 "Yes, that's right. And I've got a problem with it."

        red @sad "Oh, no, really...? I {i}really{/i} tried on that one. I thought I did pretty well."

        byron @angry2 "You did excellently."

        red @surprised "Huh? Then... what's the problem? I mean, um, what do you find the problem to be?"

        byron @norm4 "Why the hell haven't you been trying this hard on all your assignments?"

        red @surprised "A-all my assignments? I mean, Sir... I stayed up really late on that one. I studied during lunch, in-between classes. I asked all my friends." 
        red @closedbrow talking2mouth "I even sent an email to a guy who lives in Dewford for a first-hand account. And he was really hard to get anything out of." 
        red @closedbrow talking2mouth "He just kept talking about how BEAN SPACEMAN is the trendy thing. Personally, I don't get it."

        pause 1.0

        byron @norm4 "I think we're communicating on two different wavelengths here, kid. I'm asking you to give your all. And you're acting like that's unreasonable."

        red @surprised "I mean, sometimes, sure. But no-one can give their all, all the time!"

        byron @surprised2 "And why the hell not?"

        red @sad "Think about it, Sir. If you tried, you'd be constantly exhausted, and... and... I mean, if you give your all, you won't have anything left."

        byron @angry2 "You're wrong, kid. If you give all you've got, you'll {i}get{/i} all you want."

        red @closedbrow talking2mouth "Well... yeah, that's how the world {i}should{/i} work."

        pause 1.0

        byron @angry2 "I don't like you disagreeing with me."
        byron @happy2 "But I respect that you're standing by your beliefs."
        byron norm @norm2 "Anyway, enough bellyaching. I'm giving you a compliment. Just accept it."

        red @surprised "That was a {i}compliment?!{/i}"

        byron @happy2 "Yeah, and here's another one. I think you're ready to advance in this class. Take the advancement exam, and I'll make it happen for you. What do you say?"

        red @surprised "Uh... I mean, sure. Could I have some more details, though?"

        byron @norm2 "It'll be a one-on-one battle. And if you win, I'll let you use the move {i}Metallize{/i}."

        red @closedbrow talking2mouth "I don't think I know this one...?"

        byron @norm4 "My son invented it. We thought he was going to take over my gym someday. Which didn't happen {i}quite{/i} how I'd planned it, but..."

        byron @norm2 "Metallize adds the steel type to any Pokémon on the field, in addition to whatever their other types are. It can add that type even if the Pokémon is already a Steel-type."

        red @surprised "Wow! That's pretty unique."

        byron @happy2 "Yeah, my boy was always good at digging up gems like that."

        byron @norm2 "Anyway. Let's get a move on. Challenge me properly, and we'll battle."

        red @talkingmouth "Oh. Okay."

        red @angrybrow talking2mouth "Instructor Byron, I challenge you to a Pokémon battle for my right to advance to the next level of this class!"

        $ AddEvent("Instructor Byron", 2)
    else:
        red uniform @talking2mouth "Byron, I've studied since the last time we fought--and now I'm ready to advance for real."

    byron @norm2 "Let's see if you deserve it, then. {color=#0048ff}Pick a Steel-type for this fight, or you'll regret it.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    byron @happy2 "Take what you can, kid."
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("byron", TrainerType.Enemy, [
        Pokemon(703, level=11, moves=[GetMove("Tackle"), GetMove("Harden"), GetMove("Smack Down")], ability="Clear Body")
    ])

    call Battle([trainer1, trainer2], customexpressions=["red uniform", "red uniform angrybrow happymouth", "byron norm", "byron angry2"], reanchor=[False, True]) from _call_Battle_40
    $ battlehistory["Instructor Byron1"]  = _return

    show byron with dis

    if (WonBattle("Instructor Byron1")):
        $ AddEvent("Instructor Byron", 2.1)

        byron @happy2 "See? That's what giving your all looks like. Now, don't stop. {i}Ever.{/i}"

        $ passedclass = True
        jump aftertutorintrosteel
    
    else:
        byron @surprised2 "Hm. You did alright, kid. But you could've given more. That would've made the difference."

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide byron with dis
elif (not HasEvent("Instructor Byron", 3.1) and classstats["Steel"] >= 20):#Iron Coat
    show byron with dis
    if (not HasEvent("Instructor Byron", 3)):
        $ renpy.pause(1.0, hard=True)

        byron @norm2 "Hm... [first_name]."

        red uniform @talkingmouth "Yes, Instructor?"

        byron @norm2 "Question for you. What's the weight of a Bronzor?"

        red @closedbrow talking2mouth "Hm. 133.4 pounds, I think, Sir."

        byron @norm2 "Right. And how much base power would Low Kick have on it?"

        red @closedbrow talking2mouth "80, unless the Bronzor's ability is Heavy Metal, in which case it would have 100."

        byron @happy2 "Not bad. I think you're ready to take this class's advancement exam, then."

        red @happy "Really? Awesome, Instructor!"

        byron @norm2 "Passing the advancement exam gives you the right to use the metalworking equipment in this classroom to make Metal Coats. I'll show you how."

        red @closedbrow talking2mouth "Those are the items that boost your Steel-type moves by 10%%, right?"

        byron @norm2 "That's right."

        pause 0.5

        byron @happy2 "It's refreshing, having a student who doesn't moan and whine about my sink-or-swim style of teaching."

        red @sweat sadbrow happymouth "Well, it's a bit hard to stay afloat all the time, but I've managed so far."

        byron @norm2 "Mm. Ready to battle?"

        red @talkingmouth "Yes, Sir."

        $ AddEvent("Instructor Byron", 3)
    else:
        red uniform @talking2mouth "Instructor Byron, I've studied since the last time we fought--and now I'm ready to advance for real."

    byron @norm2 "Alright. Let's get this battle underway. {color=#0048ff}I'll be using a Steel-type for this fight.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    byron @happy2 "Let's see what you've got."
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("byron", TrainerType.Enemy, [
        Pokemon("Shieldon", level=21, moves=[GetMove("Iron Defense"), GetMove("Take Down"), GetMove("Rock Slide"), GetMove("Iron Head")], ability="Sturdy", item="Oran Berry")
    ])

    call Battle([trainer1, trainer2], customexpressions=["red uniform", "red uniform angrybrow happymouth", "byron norm", "byron angry2"], reanchor=[False, True]) from _call_Battle_107
    $ battlehistory["Instructor Byron2"]  = _return

    show byron with dis

    if (WonBattle("Instructor Byron2")):
        $ AddEvent("Instructor Byron", 3.1)

        byron @happy2 "There. You're figuring things out. Now come on over to the forges, and I'll show you how to work them."

        $ GetItem("Metal Coat", 1, "After an hour of sweaty work, you successfully create a Metal Coat!")

        $ renpy.pop_call()
        jump aftertutoring
    
    else:
        byron @surprised2 "Hm. Could've been worse, but I know you can dig deeper."

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide byron with dis
elif (not HasEvent("Instructor Byron", 4.1) and classstats["Steel"] >= 30):#Metal Claw
    show byron with dis
    if (not HasEvent("Instructor Byron", 4)):
        $ renpy.pause(1.0, hard=True)

        red uniform @talkingmouth "Instructor Byron?"

        byron @norm2 "Yeah, kid?"

        red @talkingmouth "Could I take this class' advancement exam?"

        byron @norm4 "You think you deserve it?"

        red @closedbrow talking2mouth "I don't know. That's what I was hoping the exam would tell me."

        byron @happy2 "Right answer. Right answer, kid."

        byron @norm2 "Sure, you can take the exam. And if you pass, I'll teach your Pokémon Metal Claw. It has a chance of increasing your attack. Just a chance, though. Nothing's guaranteed."

        red @talkingmouth "I think it'll still be worth it."

        byron @norm4 "Mm. We'll see."

        $ AddEvent("Instructor Byron", 4)
    else:
        red uniform @talking2mouth "Instructor Byron, I've studied since the last time we fought--and now I'm ready to advance for real."

    byron @norm2 "Pick one Pokémon. {color=#0048ff}You shouldn't pick a Steel-type for this fight, or you'll regret it.{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    byron @happy2 "Gloves up, kid."
    $ hidebattleui=False
    $ mustswitch = False
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("byron", TrainerType.Enemy, [
        Pokemon("Combusken", level=31, moves=[GetMove("Bounce"), GetMove("Slash"), GetMove("Flame Charge"), GetMove("Double Kick")], ability="Blaze", item="Sitrus Berry")
    ])

    call Battle([trainer1, trainer2], customexpressions=["red uniform", "red uniform angrybrow happymouth", "byron norm", "byron angry2"], reanchor=[False, True]) from _call_Battle_108
    $ battlehistory["Instructor Byron3"]  = _return

    show byron with dis

    if (WonBattle("Instructor Byron3")):
        $ AddEvent("Instructor Byron", 4.1)

        byron @happy2 "Not bad. My own kid could take notes from you. You've beaten a Steel-type, a Pokémon weak to Steel-types, and a Pokémon that gives Steel-types a hard time."
        byron @norm2 "I'm clearly not challenging you anymore, so future exams will have me using three Pokémon against your own."
        byron @happy2 "Keep on digging, kid. I'm looking forward to what you've got next."

        $ passedclass = True
        jump aftertutorintrosteel
    
    else:
        byron @sad "Alright, alright. That's enough for now. I'll be waiting for you to get back on your feet."

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide byron with dis

elif (FindGenericClassScene(True)):#generic scene
    $ renpy.call(FindGenericClassScene())
    hide byron with dis
else:# _really_ generic scene
    show byron with dis
    byron "[timeOfDay], students. Look sharp, we've got a long lecture ahead of us. Steel yourselves for that."
    hide byron with dis
    show byronbg with dis
    byron "...Pun not intended. I guess I {i}am{/i} a Dad, so it shines through sometimes. Anyway, focus on what I'm about to say..."
    narrator "Class proceeds without incident."

return

label movetutorsteel:
show byron with dis
byron @norm2 "You think your Pokémon needs a new Steel-type move? Sure. Which one?"
byron @norm2 "I can teach Metallize, which is a move that adds the steel type to any Pokémon on the field, including Steel-types."
if (HasEvent("Instructor Byron", 4.1)):
    koga @happy2 "Metal Claw's more direct. It does damage, and has a chance of boosting your attack stat. Not guaranteed, but a good chance."

label aftertutorintrosteel:
$ taughtmove = None

menu:
    ">Learn Metallize":
        $ taughtmove = "Metallize"
    ">Learn Metal Claw" if (HasEvent("Instructor Byron", 4.1)):
        $ taughtmove = "Metal Claw"
    "Nevermind":
        byron @angry2 "Don't waste our time, kid."

        if (passedclass):
            $ renpy.pop_call()
            jump aftertutoring
        else:
            jump aftersteelsetup
python:
    hidebattleui = True
    renpy.transition(dissolve)
    newindex = renpy.call_screen("switch", MakeRed())
    if (newindex != "back"):
        newmon = playerparty[newindex]
    hidebattleui=False
if (newindex == "back"):
        byron @angry2 "Don't waste our time, kid."
elif (MonCanLearn(newmon, taughtmove)):
    $ newmon.LearnNewMove([(1, taughtmove)])
    if (taughtmove in newmon.GetMoveNames()):
        jump endclass
else:
    byron @surprised2 "Don't think that Pokémon can learn [taughtmove]..."

jump aftertutorintrosteel

label itemcraftsteel:
show byron with dis

byron @norm2 "There's a couple tools that you ought to learn how to use if you want to train Steel-types right."
byron @think2 "Metal Coats boost the power of Steel-type moves by 10%%. They can also trigger evolution in Scyther and Onix."

menu:    
    ">Craft Metal Coat" if (HasEvent("Instructor Byron", 3.1)):
        $ GetItem("Metal Coat", 1, "You take a blowtorch and angle grinder to a lump of iron, slowly forming it into the Metal Coat's iconic cylindrical shape.")
        jump endclasscraft
    "Nevermind":
        byron @closedbrow tears sadmouth "Oh... you don't want to make anything with me, then...?"
        jump aftersteelsetup