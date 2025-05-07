label erikaevent(classtype):

if (IsAbsent("Erika", location.title())):
    return

if (IsAfter(11, 4, 2004) and IsBefore(20, 4, 2004) and not HasEvent("Erika", "Backstory")):
    narrator "You recognize a familiar student and go to approach her."

    show erika uniform with dis

    if (classstats[classtype] > 0):
        red uniform @talkingmouth "...Oh, hey, Erika! I don't think I saw you here, before."

        erika @surprised "Oh? Oh, yes. Well, I wasn't."
    else:
        red uniform @talkingmouth "Hey, Erika! Just checking this class out for the first time. How is it?"

        erika @surprised "Oh? I'm afraid I can't quite say. This is my first [classtype] class, as well."

    red @confusedeyebrows talking2mouth "Huh?"

    $ AddEvent("Erika", "Backstory")

    erika @closedbrow talking2mouth "Yes, it had originally been intended for me to simply attend Kobukan Academy in a provisionary role."

    red @confusedeyebrows talkingmouth "A provisionary student? How does that work?"

    erika @talkingmouth "Well, I've never had the fortune to attend a public school. There were some concerns that I might not be able to succeed in that environment."

    redmind @thinking "This girl is {i}master{/i} of the passive voice."

    red @happy "Well, great! What changed?"

    erika @surprised "Ah, well..."

    erika @sadbrow happymouth "That would be you."

    red @surprised "Huh?"

    red @happy "Oh, did I convince you that everything's cool here? That you don't need to worry about other students, and we're all nice guys?"

    erika @happy "Oh, no! Rather, you convinced me that I could defend myself from the brutes and adversaries doubtlessly embedded in the school."

    erika @talkingmouth "I, again, am truly sorry about that slap. But it gave me a tremendous sense of self-confidence about my ability to succeed in this school."

    red @confused "Uh-huh."

    redmind @thinking "Seriously. That was such a weak slap. But I don't have the heart to tell her."

    red @happy "Well, that's great! Maybe I'll see you around some more, then?"

    erika "Yes, I hope so. I've decided to tip my toes into both the Grass and Poison-type electives."

    red @happy "Nice. I guess you have a thing for flowery Pokémon?"
    
    erika @surprised "Oh? Well, yes, I suppose so."

    red @confusedeyebrows talking2mouth "Huh, you didn't pick them because of that?"

    erika @closedbrow talking2mouth "Not so much. Rather, I'm much more interested in Grass-types' natural affinity towards sun-based strategies."
    erika @talkingmouth "There are some rare Pokémon that I believe have been discovered in the Paldea region recently that I believe could synchronize well."

    erika @happy "Oh, and the Poison-types are to check the omnipresent threat of Fairy-types rampaging around in the upper leagues." 
    erika @sadbrow talking2mouth "I originally considered using Fairy-types myself, to counter dragons, but after seeing that awful Lance's horrid performance, I don't think they're nearly as much of a threat as they used to be."

    red @surprised "Huh. For a girl who's never gone to school before, you know a lot about battle."

    erika @closedbrow talkingmouth "Well, my tutors were quite good."

    red @closedbrow talking2mouth "So how come you don't like Lance? I mean, he {i}is{/i} a two-time national Champion."

    pause 2.0

    erika @angry "He does nothing with dignity. He failed, {i}multiple times{/i}, to become Champion. Our region is now saddled with a multiple-time failure as Champion."
    erika @closedbrow talking2mouth "It would have been one thing if he'd simply tried multiple times to become Kanto Champion, but then he further embarrassed us by failing multiple times to become Johto Champion."
    erika @sadbrow talking2mouth "And now he's set his eyes on failing multiple times to become World Champion, so it doesn't seem he's planning on ending that pattern of behavior any time soon."
    erika @happy "As a noted author once said, 'Is it not better to surrender your ambitions than have them slaughtered?'"

    red @closedbrow talking2mouth "Hm. I've got my problems with him, but trying over and over to achieve his goals isn't one of them."

    erika @closedbrow talking2mouth "Oh? Well, I suppose we have different priorities, then."
    erika @happy "That's certainly alright, and I respect your opinion."

    red @happy "Same to you. See you around?"

    erika @happy "Quite right."

    hide erika with dis

    pause 2.0

return