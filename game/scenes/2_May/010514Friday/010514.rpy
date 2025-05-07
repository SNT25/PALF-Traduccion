label day010514:

$ timeOfDay = "Morning"

call calendar(1) from _call_calendar_39

show morning at vspaz

$ calDate = calDate.replace(day=14, month=5, year=2004)

pause 3.0

$ renpy.music.play("Audio/Morning_ambience.ogg", channel='crowd', loop=True, fadein=1.0)

scene bedroom with transeye2
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.0, hard=True)

hide blank2

$ PlaySound("knock.ogg")

red @tired unamusedeyebrows talking2mouth swimsuithatless "...Who's that?"

yellow uniformhat @talking2mouth "Um, it's me. Yellow."

red @happytired neutraleyebrows happyeyes swimsuithatless talkingmouth "Oh, hey! What's up?"

yellow @talkingmouth "The Quarter Qlash rankings are out. I thought you might be interested in seeing them."

red @swimsuithatless happyeyes happymouth neutraleyebrows happytired "Oh, for sure! Just gimme a sec."

pause 1.0

scene suite 
show yellow uniformhat
with splitfade

red uniform @confused "...Where's everyone else?"

yellow @talkingmouth "Blue and Leaf headed out early to the Battle Hall. Ethan's still asleep."

red @closedbrow talking2mouth "Huh. Well, he's got some time before classes begin. Let's let him sleep. Anyway, you said the QQ rankings were out?"

yellow @happy "Yep! Hung up by the homerooms."

red @talkingmouth "Cool. Let's check them out."

call clearscreens() from _call_clearscreens_162
scene academyhall with splitfade

stop music fadeout 1.5 channel "crowd"
$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.0)

pause 2.0

show academyhall_blur
show rankings 
show screen currentdate
show text "{font=fonts/consola_0.ttf}{color=#000000}{size=15}{b}[last_name], [first_name[0]].{/b}{/size}{/color}{/font}":
    xpos 560 ypos 298
with dis

pause 3.0

red uniform @confused "Someone took my face."

yellow uniformhat @sadbrow talkingmouth "...That's not {i}great{/i}, but look at the winners sheet!"

pause 1.0

red @surprised "Huh?! I took the number one spot!"

yellow @talkingmouth "The spot you take is relative to the strength of the trainers you beat. Since you beat a trainer that was projected to go much, {i}much{/i} farther than you, you earned a ton of points!"

red @happy "Awesome! Oh, but wait, that means..."

narrator "You look at the bottom-right of the 'Runners-Up' sheet. As predicted, '{font=fonts/consola_0.ttf}{color=#000000}Berlitz, D.{/color}{/font}' is there."

redmind @thinking "Oops. Sorry, Dawn."

pause 1.0

narrator "Looking over the sheets, you're not overly surprised by any of the results. It seems that almost everyone you know made it through."

redmind @thinking "That's to be expected for a Kobukan student, though, I guess."

narrator "There are only a few notable exceptions. Yellow and Dawn did not pass, as you were aware. However, neither did Nate or Serena."

red @confused "Hm. That's odd. I've battled both of them, and they seemed tough enough. I wonder what... well, I suppose I can ask later."

yellow @talkingmouth "...Well, that was pretty much it."

pause 1.0

yellow @sadbrow talkingmouth "Sorry about... um, your face."

menu:
    "{color=#e226a6}[[Patience]{/color} People will forget eventually. I just have to wait it out.":
        $ TraitChange("Patience")

    "{color=#ff8412}[[Courage]{/color} I'll give them something else to talk about.":
        $ TraitChange("Courage")

yellow @talkingmouth "That's a good idea."

pause 1.0

yellow @talkingmouth "[first_name], do you, um... do you remember me?"

red @talkingmouth "...No? I don't think so. As far as I know, we met in the garden last Wednesday."

if (last_name == "Sugimori"):
    yellow @talkingmouth "...Hm. But you {i}are{/i} [first_name] Sugimori from Pallet Town, right?"

else:
    yellow @talkingmouth "...Hm. But you {i}are{/i} [first_name] from Pallet Town, right? And you used to go by [first_name] Sugimori?"

red @talkingmouth "Far as I know. I'm pretty sure I'm the only one."

yellow @talkingmouth "Okay."

pause 1.0

yellow @talkingmouth "Maybe we should talk about this sometime."

red @talkingmouth "Sure. How's tomorrow?"

yellow @talkingmouth "Hm... Blue and I are going on a picnic tomorrow. But perhaps in the afternoon?"

red @happy "No way. You and him? A picnic? How does that go down? Does he get in a fight with other campers over the best picnicking spot?"

yellow @closedbrow talkingmouth "...Sometimes."
yellow @sadbrow unamusedmouth "I'm trying to avoid that this time, though, so I'm in charge of finding the picnic spot."
yellow @talkingmouth "I'm thinking... somewhere shady, maybe... near a river would be nice."

redmind @sadbrow frownmouth "The devil works hard, but Yellow works harder."

red @talkingmouth "Alright. Sounds good! Wanna get some breakfast before class?"

yellow @talkingmouth "Sure."

pause 1.0

call clearscreens() from _call_clearscreens_163
scene blank2 with splitfade

pause 1.0

jump homeroom1transition