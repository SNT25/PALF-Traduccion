label day010521:

stop music fadeout 1.5

call calendar(1) from _call_calendar_46
$ calDate = calDate.replace(day=21, month=5, year=2004)

$ timeOfDay = "Morning"

scene homeroom
show screen currentdate
show kris
with splitfade

stop music fadeout 1.5
queue music "audio/music/celebi_start.ogg" noloop
queue music "audio/music/celebi_loop.ogg"

kris @happy "Good morning, everybody!"

kris @talkingmouth "I hope you all brought your best battling Pokémon."
kris @happy "You remember how I said that we're going to do something special in class today?"

hilbert uniform @happymouth "Yes? What is it?"

leaf uniform @surprised "Oh god, he's smiling, [first_name]. He's {i}smiling.{/i}"

kris @talkingmouth "I'd like to invite you to battle me."

whitney uniform @surprised "You?! Like, personally, you?"

kris @talkingmouth "None other."

flannery uniform tired @talking2mouth "But you're a teacher, Doc. Won't you kinda... wipe the floor with us?"

kris @talkingmouth "I don't think so. My party is specialized more for catching than for battling. I'm sure many of you are already better battlers than me."
kris @happy "But I {i}do{/i} have a variety of types. So that's something to watch out for!"

show kris surprisedbrow angrymouth with dis

blue uniform @closedbrow talkingmouth "...We're not allowed to battle in this classroom, are we?"

kris -angrymouth -surprisedbrow @happy "Oh, of course not! I was going to take us outside, to the garden."
kris talkingmouth "Come on, follow me!"

show blank2 with splitfade

pause 1.0

scene garden:
    zoom 0.625
show clouds behind garden
show kris
with splitfade

narrator "One-by-one, the other students challenge Professor Cherry."
narrator "She's a good trainer, but not unbeatable. She loses almost as often as she wins."
narrator "Still, she's clearly having fun, and the difference between her sweating and jumping all over the garden as she delivers a practical lecture on battle techniques..."
narrator "...The difference between this, and Sam's dry lectures, is quite clear."

kris @happy "Phew! That was pretty tiring. Not done yet, though."

kris @talkingmouth "What about you, [first_name]? You want to battle, too? I've heard that you've got a pretty special Pikachu I wouldn't mind taking a look at."

$ renpy.music.play("Audio/Pokemon/pikachu_angry1.ogg", channel="altcry", loop=None)
libpikachu @angryeyes happymouth "Pika."

red uniform @happy "Looks like he wants to battle you, too. Let's do it!"

python:
    trainer1 = MakeRed()
    trainer2 = MakeTrainer("Kris")

call Battle([trainer1, trainer2], uniforms=[True, False]) from _call_Battle_149
$ RecordBattle("Kris3")

stop music fadeout 1.5
queue music "audio/music/celebi_start.ogg" noloop
queue music "audio/music/celebi_loop.ogg"

show kris with dis

if (WonBattle("Kris3")):
    $ ValueChange("Professor Cherry", 3)
    
kris @happy "That was very fun! I see you've been studying hard."

if (not WonBattle("Kris3")):
    red uniform @sadbrow talkingmouth "I didn't win, though..."

    kris @talkingmouth "Not everybody wins all the time. You just have to keep trying."
    kris @happy "But I'm afraid our rematch will have to happen later. I've got the rest of this class to teach."

    kris @talkingmouth "You did well. Don't get discouraged by a single misstep. If {i}I{/i} had, I never would have managed to get where I am."

else:
    red uniform @happy "Thanks! You're a good battler, too."
    red @talkingmouth "I was really surprised that you had so many types on your team."

    kris @talkingmouth "It comes in handy, in my line of work. When trying to capture a Pokémon, you want at least one Pokémon that can weather your opponent's elemental moves, in case the wild Pokémon bursts out of your Poké Ball several times."
    kris @talkingmouth "It helps to have a wide variety of elemental resistances, in that case."

    red @happy "Makes sense."

kris @happy "Great battle, [first_name]. Excuse me."

show kris:
    xpos 0.5
    ease 0.5 xpos 0.25

show blue uniform frownmouth with dis:
    xzoom -1 xpos 0.75

kris @talkingmouth "Well... Mr. Oak? Would you like to battle me next?"

blue @talkingmouth "...Are you going back to your own class after this week?"

kris @surprisedbrow angrymouth "Hm?"
kris @talkingmouth "Well, yes, I am. I suppose you missed your grandfather?"

blue @closedbrow talkingmouth "Something like that."
blue @talkingmouth "And 'no thanks' to the battle."

if (WonBattle("Kris3")):
    show kris surprisedbrow angrymouth with dis

    blue wistfulbrow @wistfulmouth "If [first_name] beat you, then there wouldn't be {i}any{/i} challenge for me."

    redmind @confusedeyebrows frownmouth "...That's not the cockiest thing he's ever said, but it's up there."
    redmind @frownmouth "But he... doesn't look into it. As though he was just reciting from a script."

kris @closedbrow talking2mouth "Well, perhaps another time, then."

hide blue with dis

kris happy "Come on, 1-B! I want to battle everyone who wants to battle before the morning is over!"
kris @talkingmouth "Let's get those bodies moving! Get energetic! E-N-E-R-G-Y!"

whitney uniform mediumblush @surprisedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

redmind @smirkmouth unamusedbrow "Oh. Now I get it."

menu:
    ">Tease Whitney":
        $ AddEvent("Professor Cherry", "IsCute")
        red @unamusedbrow talkingmouth "{size=30}She's cute, huh?{/size}"

        whitney fullblush -bigblush @closedeyes angryeyebrows angrymouth "{size=30}Shutupshutupshutupshutup...{/size}"

    ">Leave the poor girl be":
        pass

call clearscreens() from _call_clearscreens_190
scene blank2 with splitfade

pause 1.0

narrator "Class wraps up shortly, and everyone heads directly from the garden to their first elective class. Professor Cherry stays behind, a somewhat melancholy look on her face."

kris sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."
kris @talkingmouth "Only one more class..."

pause 1.0

if (HasEvent("Professor Cherry", "IsCute")):
    kris surprisedbrow talking2mouth "Wait. Did one of those students just say I was cute?"

    $ ValueChange("Professor Cherry", 1)

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_191
$ renpy.music.stop(channel='crowd', fadeout=1.5)
stop music fadeout 1.5

jump PickElective