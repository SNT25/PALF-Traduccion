label lunch010520:

redmind uniform @thinking "Hm... let's see... where is she...?"

show may uniform happybrow with dis

pause 1.0

redmind @happy "Ah, there she is!"

show may surprisedbrow frownmouth with dis

red @talkingmouth "Hey, May! Got a question for you."

if (GetRelationshipRank("May") > 0):
    may -surprisedbrow -frownmouth @talkingmouth "Sure, [first_name]! What can I do for my second-favorite taster?"

else:
    may -surprisedbrow -frownmouth @talkingmouth "Sure, [first_name]! What's up?"

red @talkingmouth "You've heard about Dawn's birthday, right?"

may @talkingmouth "Yep. Leaf invited all of the old Dorm 251 to come."

red @happy sweat "Well, I was trying to think of what a good present would be, but, uh, I'm kinda tight on money."
red @talkingmouth "So then I thought maybe I could make the cake. I'm not half bad at cooking myself, but I don't have, like, any ingredients, or cooking tools."
red @talkingmouth "I was wondering if you know where the best place to go for that stuff would be."

may @happy "Oh, that'd definitely be the Cooking Club!"

red @confused "We have a Cooking Club?"

may @talkingmouth "Yup. It was only started a week or two ago, I think. Anyway, they have ingredients, ovens, stoves, all that stuff. And it's all completely free to use for clubmembers!"

red @happy "Well, that's where our tuition is going, I guess."

may @sadbrow talkingmouth "I'd want to join myself, but, um..."

pause 1.0

may surprisedbrow frownmouth @surprised "Oh no. There she is!"

show may:
    xpos 0.5
    ease 0.3 xpos -0.5

show lisia incognito incogbrow incogshades angrymouth:
    xpos 1.5
    ease 0.5 xpos -0.3

pause 1.0

lisia @talkingmouth "May Birch! Get back here and go over your footwork one more time!"

pause 1.0

redmind @closedbrow talkingmouth "Geez. From what I've been hearing of the Coordinator Club, it sounds like their training has become as intense as the Battle Team's. At least we only train on specific dates."

pause 1.0

show cafe:
    xalign 0.0
    ease 0.5 zoom 1.2 xpos -0.2
    pause 0.3
    ease 1.0 xpos 0.0
    pause 0.3
    ease 0.5 zoom 1.0

pause 3.0

red @closedbrow talking2mouth "Well... where would I find a Cooking Club? Maybe the kitchens?"

stop music fadeout 1.5
queue music "audio/music/alolaencounter_intro.ogg" noloop
queue music "audio/music/alolaencounter_loop.ogg"

$ hideside = True

mallow @talkingmouth "Hey! Did I hear you mention the Cooking Club?"

pause 0.2

$ hideside = False

red @confused "Hm? Yeah, hi!"

show mallow uniform:
    xpos -0.25 
    ease 0.5 xpos 0.5

red @happy "Don't think I've seen you before. I'm--"

show mallow:
    ease 0.1 ypos 1.1
    ease 0.1 ypos 1.0
    ease 0.1 ypos 1.1
    ease 0.1 ypos 1.0

mallow @happy "You're [first_name] [last_name], duh! Everyone knows you."

red @sweat talkingmouth "I guess I did kinda stand out..."

$ BecomeNamed("Mallow")

mallow @angrybrow talkingmouth "My name's Mallow Pulupulu. And I'm the Sous-Chef of the Cooking Club!"
mallow @happy "Alola!"

narrator "Mallow makes a rainbow gesture with her hands."

red @talkingmouth "Alola? Like the region?"

mallow @talkingmouth "It means 'Hello!' in the old Alolan language. The region was named after our word for 'hello!'"
mallow @happy "That's because we're famous for our hospitality! Alola's a fantastic place to visit over Summer break, you know, and not just because of the gorgeous weather!" 
mallow @talkingmouth "The Aether Foundation's got an amazing internship program!"

redmind @happy "This girl's enthusiasm is kinda infectious. I suspect she might work for the Alolan tourism board... and if she doesn't, they should hire her."

red @talkingmouth "Sounds pretty great. But you mentioned the Cooking Club? (Or, I did, anyway.)"

mallow @surprised "Oh!"
mallow @happy "Right, {i}auwe!{/i} I got so excited to sell you on Alola, I completely forgot why I was here."
mallow @talkingmouth "We at the Cooking Club would {i}love{/i} to have you!"

red @talkingmouth "I'd love to check it out. I'm part of the Battle Team, but it would be fun to drop into the club once in a while."
red @talkingmouth "Right now, though, I'd like to make a cake for a classmate of mine. Dawn Berlitz."

mallow @frownmouth "{w=0.5}.{w=0.5}.{w=0.5}.Hm.{w=0.5}{nw}" 
extend @talking2mouth " No, I don't think I know that name."

red @talkingmouth "Mega Altaria? Fought my Pikachu?"

mallow @happy "Oh, right! You know, I was {i}really{/i} surprised to see another of your Pikachu! I thought they were all extinct."

red @surprised "Huh? You know something about my Pikachu?"

mallow @talkingmouth "I sure do! Every Alolan does."
mallow @frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
mallow @talking2mouth "Well, actually... I guess some younger people might not know. But I'm really into Alola's history and lore and stuff."
mallow @happy "And I just {i}love{/i} sharing my passions, so getting to share my love of cooking, and my {i}secret{/i} knowledge of your Pikachu is like a dream come true! It's like a warm day on Akala's beaches!"

pause 1.0

red @sweat talkingmouth "Uh... so will you?"

mallow flirtbrow catmouth @talkingmouth "What'll you give me for it?"

red @closedbrow talking2mouth "Ah, geez. Look, I--"

mallow -flirtbrow -catmouth @happy "I'm kidding! We Alolans are {i}famously{/i} generous. I'll give it to you all for free!"
mallow @talkingmouth "Just drop by the Student Center after classes today, okay? I'll tell the Head Chef to organize a meeting of the Cooking Club."

red @happy "Wow, thanks! That's really kind of you. Thanks a lot, Mallow."

mallow happy "That's just how we Alolans are! I'll see you later today! Alola!"

hide mallow with dis

pause 1.0

red @happy "What a nice girl. Maybe I should look into this Aether Foundation internship program she mentioned. If all Alolans are as nice as her, it might be a really great way to spend a summer."

$ removestudents = { "May" }

hide blank2
show blank2 with dis:
    alpha 0.8

label TempPickTable:

call screen newtables(_with_none=False) with dissolve
with dissolve
hide blank2 with dissolve
narrator "You chose the [_return]?"

$ tablecalled = _return
menu:
    ">Go to the [tablecalled]":
        call newtable(tablecalled) from _call_newtable_1

        $ removestudents = set()

        jump PickElective
    ">Rethink your choice":
        jump TempPickTable