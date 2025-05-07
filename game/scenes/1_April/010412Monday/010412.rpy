label day010412:

$ timeOfDay = "Morning"

if (pikachuobj in playerparty):
    $ playerparty.remove(pikachuobj)

call calendar(1) from _call_calendar_7
$ calDate = calDate.replace(day=12, month=4, year=2004)

show morning at vspaz

$ renpy.music.play("Audio/Morning_ambience.ogg", channel='crowd', loop=True, fadein=1.0)

scene dorm_A with transeye2
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.0, hard=True)

hide blank2

red casual hatless @closedbrow talking2mouth "{cps=*0.2}Morning already? Geez...{/cps} Why have I been so tired recently?"
red @surprised "Wait, crap! I don't think I have time to get to breakfast before homeroom. Ugh..."

$ renpy.music.stop(channel='crowd', fadeout=1.0)

menu:
    "{color=#ff8412}[[Courage]{/color} >Just run like the wind! You can do it!":

        redmind @thinking "Okay, here goes..."

        show blank2 with dis

        pause 1.0

        narrator "You make it halfway to the cafeteria before realizing you forgot to change into your uniform." 
        narrator "After grabbing your food and running back, you manage to roll into Professor Oak's class a second before the last ring of the bell."

        $ TraitChange("Courage")

        show homeroom behind blank2

        $ renpy.transition(dissolve)
        show screen currentdate

        hide blank2 with splitfade    
        hide morning

        show oakbg with dis

        narrator "You are a sweaty, puffing mess by the time you sit down."

        show leaf uniform at rightside with dis

        leaf @surprised "Woah. [first_name], what happened? You're seriously sweaty."

        show blue uniform at leftside with dis

        blue @happy "He probably just tried walking up some stairs!"

        red uniform -hatless @confusedeyebrows talking2mouth "What's up with the constant fitness cracks? I run, like, every day. There's no insecurity there."

        hide blue
        hide leaf
        with dis

    "{color=#b7669e}[[Charm]{/color} >Ask one of your friends to bring food to homeroom":
        redmind @thinking "Yeah, alright. I'll just ask May to pick me something up. She's probably still at the cafeteria with Brendan, considering how much the big guy eats."

        show blank2 with dis

        pause 1.0

        narrator "You call May and ask her to bring some food from the cafeteria to homeroom, which she happily agrees to."

        $ TraitChange("Charm")

        narrator "However, when it arrives..."

        show homeroom behind blank2

        $ renpy.transition(dissolve)
        show screen currentdate

        hide blank2 with splitfade    
        hide morning

        show oakbg with dis

        show may uniform at leftside with dis

        may @happy "Here you go, [first_name]! I picked out my favorites! Quesadillas, chili, and jalapeno poppers!"

        red uniform -hatless  @closedbrow talking2mouth "Hm... spicy."

        redmind @thinking "Ow, ow, ow, ow, ow, ow, ow, ow."

        if (GetRelationshipRank("Sabrina") > 0):
            redmind @surprised "{color=#600080}Hm... I'd like some chili now.{/color}"

            redmind @angrybrow frownmouth "Sabrina. Would you mind not popping into my mind unless I reach out first?"

            redmind @thinking "[ellipses]"

            redmind @thinking "Nothing, huh."

        hide may with dis

$ renpy.pause(0.6, hard=True)

oak @talkingmouth "Happy Monday, everyone!"

$ PlaySound("class_groan.ogg")

pause 2.0

oak @talkingmouth "Yes, well, I suppose no-one's {i}really{/i} a fan of Mondays. In any case, your first week is over, and I shan't be coddling you any further! I expect everyone to be prepared for the test this afternoon."

oak @talkingmouth "For now, though, it's about time we address the Copperajah in the room of symbiotic evolutions. Magneton, Wugtrio, and Metagross are examples. In order to..."

jump homeroom1transition