label klaraevent:

$ classname = location.title()

if (IsAbsent("Klara", classname)):
    return

if (not HasEvent("Klara", "ClassMeet")):
    $ AddEvent("Klara", "ClassMeet")
    narrator "You'd only just stepped into the classroom, when..."

    show klara makeup uniform hairpin happy with dis:
        ypos 1.0 zoom 1.0
        ease 0.5 ypos 1.2 zoom 1.3
    
    klara "[first_name]!"

    red uniform @happy "Oh, hey, Klara! You're in this class, too?"

    if (classstats[classname] > 9):
        red @happy "I've been to this class pretty often, but I guess I've never noticed."

        klara -happy @surprised "Oh? You didn't notice me...?"

        $ autoquote = False

        show klara:
            ypos 1.2 zoom 1.3
            ease 0.5 ypos 1.0 zoom 1.0

        klara @sad "\"That makes me a bit sad... "
        extend @happy "but it's alright, I forgive you! I noticed you, but I understand you've got a lot going on.\""

        $ autoquote = True

        klara @happy "Anyway, of course I'd be in this class! [classname] is my absolute favorite type of all time!"

    else:
        show klara:
            ypos 1.2 zoom 1.3
            ease 0.5 ypos 1.0 zoom 1.0
            
        klara -happy @happy "Of course! [classname] is my favorite type of all time!"

    red @talkingmouth "That's cool."

    if (classname == "Water"):
        klara @happy "Plus, Instructor Wallace is such a genius coordinator... and he's one of the judges in the upcoming Millennium Drop!"

        red @happy "Trying to get on his good side?"

        klara @surprised "Huh? Oh, you're right! I never even thought of that!"
        klara @happy "But noooo way! I'd never try to get close to someone just because they could help me out somehow."
        klara sad "I mean, some people do that... but not me."

    else:
        klara @happy "Plus, Instructor Burgh is such a great artist. I'm a massive fan of his work!"

        red @talkingmouth "Really? You're the artsy type?"

        klara @sadbrow blush "Oh, well... I'm not any good, but I think everyone's an artist, deep inside."
        klara @happy "I don't brag about it like some people, because I think art should just be used to make people happy. Not for personal glory, you know?"
        klara sad "Unfortunately... not everyone thinks that way..."

    narrator "Klara takes a quick look over at another student, which you realize with a start is Melody."

    redmind @thinking "Oh, she's also in this class..."

    pause 0.5

    redmind @unamusedbrow unamusedmouth "...And she's sitting on the desk again."

    klara -sad @sad "I heard she's in this class because she thinks it'll be an easy A."
    klara @sadbrow talkingmouth "She'll be pretty disappointed when she finds out her {i}usual{/i} strategy won't work."

    red @closedbrow talking2mouth "Huh? What do you mean?"

    klara @sadbrow talkingmouth "Aw, don't make me say it..."

    if (classname == "Water"):
        klara @closedbrow blush happymouth "It's embarrassing! But, like, Instructor Wallace is totally gay, you know?"
    else:
        klara @closedbrow blush happymouth "It's embarrassing! But, like, Instructor Burgh is totally married, you know?"
    
    klara @sadbrow talking2mouth "No luck there, Melody. Sor-ry!"

    red @surprised "Wait, you don't mean she--"

    klara @surprised "That's just what I've heard! I don't think {i}I{/i} believe it. I see the best in everyone."
    klara @sadbrow talking2mouth "But... a lot of other people have been saying it..."

    red @closedbrow talking2mouth sweat "Jeez. Hope she doesn't make class difficult, then..."

    klara happy "Well, if she does, you can just sit with me! There's no need to think about her when I'm here, no matter what she does."

    red @happy "Thanks. I'll keep that in mind! Let me just talk to Ethan for a sec."

    klara "Of course! Don't leave me waiting, though!~"

    hide klara with dis

    pause 2.0

return