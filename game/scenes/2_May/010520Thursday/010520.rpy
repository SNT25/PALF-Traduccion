label day010520:

stop music fadeout 1.5

call calendar(1) from _call_calendar_45
$ calDate = calDate.replace(day=20, month=5, year=2004)

$ timeOfDay = "Morning"

scene homeroom
show screen currentdate
show kris
with splitfade

stop music fadeout 1.5
queue music "audio/music/celebi_start.ogg" noloop
queue music "audio/music/celebi_loop.ogg"

kris @happy "Gooo~oood morning, everybody!"

redmind @surprisedbrow uniform frownmouth "Woah. That's definitely a tone change from yesterday."

kris @talking2mouth "You've got your test coming up later today. I expect everyone should be entirely prepared."
kris @angrybrow talking2mouth "Remember, as long as you have three increases to your critical hit ratio, your hits are {i}guaranteed{/i} to be critical."

hilbert uniform @talkingmouth "As long as the opponent isn't under the effect of Lucky Chant, and doesn't have the abilities Shell Armor or Battle Armor."

kris @happy "That's right! Please raise your hand, next time, Hilbert, but that's right."

hilbert @closedbrow smilemouth "{w=0.5}.{w=0.5}.{w=0.5}."

flannery uniform @tired "Ugh. Seeing Hilbert actually {i}liking{/i} class makes me feel worse than an all-nighter."

whitney uniform @frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

flannery @confusedeyebrows tiredeyes talking2mouth eyebags frazzled "Why are you always staring at Doctor Cherry?"

whitney embarrassedeyes embarrassedmouth @surprised "Huh? What? Staring? I'm not staring, you're staring!"

kris @surprised "Hm? Is there something happening here?"

whitney fullblush @surprised "No, Doctor, sorry! {size=30}Please ignore me.{/size}"

kris @angrybrow angrymouth "Hm... Whitney, right? I feel like I know you from somewhere... Outside of class, I mean."

whitney @fullblush surprised "Nope! Nope! Absolutely not, not a chance!"

kris @closedbrow angrymouth "Hm."

pause 1.0

kris @talkingmouth "Well, as long as you pass this week's quiz, you could be a board member, and I'd still be happy to see you."

kris @angrybrow talkingmouth "Get out your pencils and pens, everyone! You still have two more hours of notes I can cram in you before the exam!"

jump homeroom1transition