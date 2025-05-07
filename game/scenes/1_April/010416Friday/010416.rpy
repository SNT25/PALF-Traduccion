label day010416:

$ playerparty.remove(pikachuobj)
$ timeOfDay = "Morning"
call calendar(1) from _call_calendar_11
$ calDate = calDate.replace(day=16, month=4, year=2004)

show morning at vspaz

$ renpy.music.play("Audio/Morning_ambience.ogg", channel='crowd', loop=True, fadein=1.0)

scene dorm_A 
with transeye2
$ renpy.transition(dissolve)
show screen currentdate

show brendan at rightside
show calem at leftside 
show hilbert at midrightside
show ethan at midleftside
with dis

red @talkingmouth "Morning, guys."

calem @talkingmouth "[first_name]. Pleasure."

red @happy "So, hey--did I tell you guys that Janine asked me to participate in the Battle Team tryouts on Monday?"

show brendan surprisedbrow frownmouth
show calem surprisedbrow frownmouth
show ethan surprisedbrow frownmouth
with dis

pause 1.0

hilbert @talkingmouth "No, but it's obvious."

ethan @angry "Dude! How is {i}that{/i} obvious? You talked with Janine? {i}The{/i} Janine? And she {i}asked{/i} you to apply?"

hilbert @talkingmouth "He battled with [blue_name] in the Battle Hall one week ago. Janine would be a fool to not immediately latch onto his power."
hilbert @closedbrow talkingmouth "And Janine, as we saw in the battle exhibition, is no fool."

show brendan -surprisedbrow -frownmouth -surprised
show calem -surprisedbrow -frownmouth -surprised
show ethan -surprisedbrow -frownmouth -surprised
with dis

brendan @closedbrow talkingmouth "I dunno, man. I don't think it's {i}that{/i} obvious."

hilbert @angry "That's because you're an imbecile."

brendan @sad "I know, man, but I'm trying..."

ethan @happy "Hey, how come Janny isn't asking me to try out for the Battle Team, then?"

hilbert @closedbrow talkingmouth "You've never battled in front of her. And you're bad at battling, anyway."

ethan @surprised "Huh?"

hilbert @talkingmouth "The fact your Pokémon listen to you perfectly doesn't negate the fact you're telling them to do {i}really{/i} stupid things."

ethan @sad "Aw..."

red @talkingmouth "Hey, guys. Focus up. Janine told me to borrow Pokémon for the upcoming battle. Would I be able to borrow you guys' Pokémon?"

brendan @happy "'Course, dude!"

ethan @talkingmouth "Yeah, go ahead."

calem @closedbrow talkingmouth "I can't think of any reason not to let you. As long as you return them shortly after the tryouts."

pause 1.0

ethan @talkingmouth "What about you, Harrier?"

hilbert @sadbrow talkingmouth "It's Hilbert."

pause 1.0

hilbert @talkingmouth "I'm unsure."

red @talkingmouth "Something I can do to make you sure?"

hilbert @closedbrow talking2mouth "I'm not sure about that, either."

red @talkingmouth "Well, why are you struggling? Like, what are the pros and cons? The blacks and whites?"

hilbert @smilemouth "Hm."
hilbert @happymouth "Now you're speaking my language."
hilbert @talkingmouth "If I lend you my Pokémon, you will be indebted to me. I want someone with your power to be around me."

ethan @happy "Hey, what about--"

hilbert @closedbrow angrymouth "Be {i}quiet{/i}, Ethan!"

ethan @sad "{size=30}Sorry...{/size}"

hilbert @closedbrow talkingmouth "However, if I lend you my Pokémon, they may experience loss. I do not want that."

red @happy "Pretty cocky. You don't think they'll ever lose if you're leading them?"

hilbert @talkingmouth "They might, but I can be certain that I did my best to avert that."

pause 1.0

red @talking2mouth "Then let me prove to you I'll do my best to avert that as well. I'll battle you after school. If I win, I can borrow your Pokémon for the battle tryout."

hilbert @closedbrow talkingmouth "...Fine."

red @happy "Cool. Now, let's all go get breakfast. Hilbert, will you come with us this time?"

hilbert @talkingmouth "I will walk in the same direction as you, at a similar speed."
hilbert @closedbrow talkingmouth "You can interpret that as 'coming with you,' if you want."

red @happy "I'll take it."

$ renpy.music.stop(channel='crowd', fadeout=1.0)

scene blank2 with Dissolve(2.0)

stop music fadeout 1.5

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)
show oakbg
show homeroom behind oakbg

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade    
hide morning

$ renpy.pause(0.6, hard=True)

oak @talkingmouth "And that's how the Pokémon League of Alola was founded! The vacant Champion position has been much desired by many from other regions, but no-one, as of yet, has been able to defeat the Elite Four."
oak @talkingmouth "Though the denizens of Alola are likely too busy dealing with their invasive species problem to mount a serious league attempt at this current time."

pause 1.0

oak @talkingmouth "The last four years, as a whole, actually have been marked by a notable uptick in strange activity worldwide. Thank goodness none of that has spilled over into our own Kobukan!"
oak @talkingmouth "Perhaps it's our isolation, or small size, but the sorts of disasters and cataclysmic events that have been growing more and more common seem as though they intend to leave this place alone."
oak @talkingmouth "But perhaps I shouldn't tempt fate. That'll be all for today's lesson!"

jump homeroom1transition