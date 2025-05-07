label day010428:

$ timeOfDay = "Morning"

if (pikachuobj in playerparty):
    $ playerparty.remove(pikachuobj)

call calendar(1) from _call_calendar_23
$ calDate = calDate.replace(day=28, month=4, year=2004)

show morning at vspaz

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)
show oakbg
show homeroom behind oakbg

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade    
hide morning

$ renpy.pause(0.6, hard=True)

oak @talkingmouth "If you take anything away from this lesson, let it be that evolutionary stones are exceedingly rare in Kobukan. Without a well-funded mining expedition that can go {i}very{/i} deep into Kobukan's surface, you're unlikely to find anything."
oak @talkingmouth "In fact, over seventy percent of our mineral resources are purchased from the Unovan city of Driftveil."
oak @talkingmouth "This can be considered a blessing, though, as Kobukan's peaceful past is largely due to the fact it had nothing worth taking by foreign warlords until the modern age."
oak @talkingmouth "Even the dueling monarchies of nearby Unova, infamous as their conflict was, never thought Kobukan an attractive target for their conquests."

pause 1.0

oak @talkingmouth "There are historical records, actually, that say the Tyrant King of Kalos, who conquered 27%% of the known world at one time, left Kobukan alone, as he thought conquering it would be an indignity to his station."
oak @talkingmouth "...So, unless anyone has any questions, I think that about brings us to the end of the lecture!" 

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.0)

hide oakbg with dis

pause 1.0

show leaf uniform with dis

leaf @talkingmouth "...Hey."

if (GetRelationship("Leaf") == "Date"):
    red uniform @talkingmouth "Hey. You look good."

    leaf @closedbrow talkingmouth blush "Don't I always?"

    red @closedbrow talking2mouth "Can't say I've ever seen you {i}not{/i} look good, no."

    leaf @sadbrow blush talkingmouth "Heh. I went fishing for that one."

    red @talkingmouth "Speaking of. I know you're planning our next date, but, y'know, on the off chance I get a second date, how would you feel about fishing?"

else:
    red uniform @talkingmouth "Hey. You doing alright?"

    leaf @sadbrow talkingmouth "Been better. How are you, though?"

    red @sadbrow talkingmouth "I'm alright. Thanks for asking."

    leaf @talking2mouth "So. I was going to ask if you wanted to hang out some time. Sunday, maybe."

    red @confusedeyebrows frownmouth "[ellipses]"

    leaf @closedbrow talking2mouth "No, this isn't a trick. I just think it'd be fun to go into the city. {i}As friends.{/i} We can invite Tia."

    if (punkwins > 0):
        red @talkingmouth "Sure. Last time I was in the alley, I think I saw this little seaport area. I bet we could do some fishing there."
    else:
        red @talkingmouth "Sure. Inspira has a port, right? I bet we could do some fishing there."

show leaf surprisedbrow frownmouth:
    ease 0.2 zoom 0.9 ypos 0.9

pause 0.5 

red @confused "Or... not? You don't want to catch any fish Pokémon?"

show leaf:
    ease 1.0 zoom 1.0 ypos 1.0

leaf -surprisedbrow -frownmouth @closedbrow talking2mouth "It's... not the fish I mind. I, mean, I don't love Water-types, but..."

pause 1.0

leaf @talking2mouth "Tell you what, how about I give you more details on Sunday?"

red @talkingmouth "Sure thing. Sounds like a plan."

leaf @talkingmouth "Alright. See you then."

hide leaf with dis

pause 1.0

redmind @confusedeyebrows frownmouth "Huh. She 'doesn't love Water-types'?"

redmind @thinking "Come to think of it, her entire team is really good against Water-types, isn't it?"

redmind @thinking "Wonder what that's about...{w=0.5} guess I'll find out on Sunday."

jump homeroom1transition