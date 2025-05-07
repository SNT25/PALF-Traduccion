label day010430:

$ timeOfDay = "Morning"

if (pikachuobj in playerparty):
    $ playerparty.remove(pikachuobj)

call calendar(1) from _call_calendar_25
$ calDate = calDate.replace(day=30, month=4, year=2004)

show morning at vspaz

pause 3.0

$ renpy.music.play("Audio/Morning_ambience.ogg", channel='crowd', loop=True, fadein=1.0)

scene dorm_A with transeye2
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.0, hard=True)

hide blank2

red @happy "Mmph. Good morning, [pika_name]!"

$ PlaySound("Pokemon/pikachu_norm1.ogg")

pikachu neutral_2 "Pika."

show ethan uniform with dis

ethan @talkingmouth "Hey, man."

red @talkingmouth "Hey, buddy. Sleep well?"

ethan @talkingmouth "Sure did." 

red @surprisedbrow talkingmouth "You're up early. Dressed, too."

ethan @happy "Yeah, I dunno. I felt like I needed to step it up."

red @talkingmouth "Oh, for real? Good for you. What caused this?"

ethan @closedbrow talking2mouth "Man, I don't even know."
ethan @sadbrow talkingmouth "I think watching you just kinda reminded me of what I {i}could{/i} be doing, y'know? We've got so much in common, so I feel like I don't have a good reason to not {i}at least{/i} do as well as you."

red @happy "Hey, I'm flattered."

ethan frownmouth @talking2mouth "...Yeah."

pause 0.5

ethan @closedbrow talking2mouth "So, I've got this {i}crazy{/i} theory about why we might be, like, syncing up."

red @confused "Oh, yeah?"

ethan @talkingmouth "Yeah. It's something Professor Elm told me about a long time ago. I never even gave it a second thought when it came to {i}our{/i} thing, but... yeah, we should talk about that."

red @happy "Lemme guess. You want to talk about it on Sunday, right?"

ethan @talkingmouth "Huh? Yeah, how'd you know?"

red @talkingmouth "My Sunday's pretty jam-packed already. Everybody and their mother has been asking to do something with me on Sunday."

ethan -frownmouth @sadbrow talkingmouth "Oh, yeah? I was thinking you'd be busy with school today, and Student Council stuff tomorrow. Raincheck to Monday?"

red @talkingmouth "Nah. We can do it on Sunday, it's fine. I'll cram it in between talking with Tia and going to the city with Leaf."

ethan @happy "Man. What a life you live, huh?"

red @talkingmouth "It keeps me busy! Sometimes I need to remind myself I'm here to study how to become a Pokémon champion."

ethan @talkingmouth "Hey. Eyes on the prize, right?"

red @happy "Right!"
red @talkingmouth "Now, c'mon, let's get some breakfast."

ethan @closedbrow talking2mouth "You think they have any more of that dinosaur egg oatmeal...?"

scene blank2 with splitfade
$ renpy.music.stop(channel='crowd', fadeout=1.5)
stop music fadeout 1.5

$ renpy.pause(2.5, hard=True)

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)

show oakbg at dissolvein behind blank2
show homeroom behind oakbg

hide blank2 with splitfade

$ renpy.pause(0.6, hard=True)

oak @talkingmouth "Good morning, students! Let's wrap up this week, and the first month of the semester, with some review."

pause 0.5

oak @talkingmouth "Ah, okay. So, the subject of these so-called Alolan 'Ultra Beasts' is quite controversial amongst academics right now. Are they Pokémon? Are they not? Does the distinction matter?"
oak @talkingmouth "In this lesson, we'll be discussing what is known of Ultra Beasts, as well as their relation to the 'Ultra Wormhole' and 'Faller' phenomenons."
oak @talkingmouth "Seven years ago..."

jump homeroom1transition