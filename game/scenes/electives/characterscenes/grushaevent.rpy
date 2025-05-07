label grushaevent:

if (IsAbsent("Grusha", location.title())):
    return

if (((IsDate(26, 4, 2004) and timeOfDay == "Afternoon") or not IsBefore(27, 4, 2004)) and "ClassMeet" not in GetEvents("Grusha")):
    $ AddEvent("Grusha", "ClassMeet")

    narrator "You spot a familiar student and go to greet him."
    
    show grusha uniform with dis

    red uniform happy "Hey, Grusha."

    grusha "Oh, you're here, too."

    pause 0.5

    red @confused "You seem... less than enthused."

    grusha @talkingmouth "Give me a break. I like my privacy. I'd love nothing more than to fly under the radar for the rest of the year."

    if (IsBefore(1, 5, 2004)):
        grusha @closedbrow talkingmouth "Kinda hard to do that when I'm out with [first_name], student council hopeful, Battle Team ace, and unfixable attention magnet."
    else:
        grusha @closedbrow talkingmouth "Kinda hard to do that when I'm out with [first_name], wielder of Frienergy, Battle Team ace, and unfixable attention magnet."

    red @surprised "Attention magnet?"

    grusha @talkingmouth "You know what I'm talking about. Don't pretend you don't love the eyes of the world."

    grusha @sadbrow talking2mouth "I don't blame you for that. I did too, once."

    pause 0.5

    grusha @talkingmouth "But that time's over for me. Now I know it's much smarter to shun them all."

    pause 0.5

    if (IsBefore(1, 5, 2004)):
        red @confused "I'm... confused. What do you mean? I mean, I guess it's true I tend to get a lot of attention. But... is there anything wrong with that?"

        grusha @talkingmouth "Not yet. But there will be. You want to know something, [first_name]? The {i}only{/i} thing people like more than an underdog is to see the establishment fall."
        
    else:
        red @talkingmouth "That seems defeatist. Sure, things came to a nasty head during the Student Council election, but things turned around. I got to explain the truth."

        grusha @sad2eyes talkingmouth "A stumble. When you're up on the slope, you never fall the first time. It's just a stumble, then you straighten up, and think you've got it."

        pause 0.5

        grusha @talkingmouth "That's when the {i}real{/i} fall happens."

    grusha @closedbrow talking2mouth "Become a popular enough underdog and you become the establishment. And the people who cheered you up the mountain will laugh as you come crashing down."
    grusha @sadbrow talking2mouth "Failure follows everyone like a reaper with a blade. You really want to bring an audience with you when she catches up?"

    red @talkingmouth "...I can't say I know what the point of succeeding without an audience is."

    grusha @talkingmouth "It's safer. That's the {i}only{/i} point. But it's a good one."

    red @angrybrow talking2mouth "I don't know your story. I don't know where you're coming from. And I'm sure this makes a lot of sense from your perspective. But from {i}my{/i} perspective, it sounds like you're being needlessly pessimistic."

    if (IsBefore(1, 5, 2004)):
        grusha @closedbrow talking2mouth "You will."
    else:
        grusha @confusedeyebrows talking2mouth "Even after everything you went through with the Student Council?"

        grusha @closedbrow talking2mouth "Hm. Maybe you're made of tougher stuff than I am. I'll stay in my cold shadows, I think."

    pause 0.5

    red @talkingmouth "Or maybe I'll convince you that attention isn't that bad."

    grusha @closedbrow talking2mouth "Hmph."

    narrator "You leave Grusha and head to your spot with Ethan."

    pause 0.5

    if (IsBefore(1, 5, 2004)):
        grusha @sadbrow talking2mouth "A comet is flying ice. A brilliant star that burns itself into nothingness. Everyone loves the spectacle of destruction."
        grusha "...Don't destroy yourself, [first_name] [last_name]. I couldn't bear to hear their cheers again."

    else:
        grusha @sadbrow talking2mouth "A comet is flying ice. A brilliant star that burns itself into nothingness. Everyone loves the spectacle of destruction."
        grusha "When you destroyed yourself, I couldn't bear to hear their cheers again. But... maybe, for you, there's a chance they'll cheer again."         

    hide grusha with dis

    pause 2.0

return