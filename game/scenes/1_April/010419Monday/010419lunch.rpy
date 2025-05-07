label lunch010419:

show silver uniform with dis

red uniform @happy "Hey, Silver!"

if (GetRelationship("Silver") == "Friend"):
    silver @smilemouth "...Hi."
    silver @happymouth "What's, uh, what's up, [first_name]?"

    redmind uniform @thinking "Hm... kinda awkward, but endearing, in a rough way."

else:
    silver @talkingmouth "The hell do you want?"

red @happy "I saw your posters. I'm not entirely sure they're the best example of graphic design, but they seem to have gotten people talking about my campaign."

red @talking2mouth "You could have told me you were taking pictures of me, though."

silver @surprisedbrow talkingmouth "...Uh?"
silver @sad "Don't know what you're talking about."

red @confused "Huh? Really? Is this, like, a coy 'I don't know what you're talking about,' or a real one?"

silver @talkingmouth "Real one. I haven't done anything yet."

red @confused "Okay. Now... {i}that{/i} is surprising."
red @closedbrow talking2mouth "Hm. Well, I guess I can figure that out later. Will I see you at the Battle Team tryouts?"

silver @happy "Oh, yeah. You definitely will. And I've done a bit of training since the last time we battled."

if (WonBattle("Silver1")):
    red @closedbrow talking2mouth "Think you'll win this time?"

    silver @talkingmouth "Probably not. But I'll make you work harder for your victory."

else:
    red @talkingmouth "Oh, so you'll be even {i}harder?{/i} Looking forward to it."

    silver @happymouth "Heh."

red @happy "Beat you later, then."

if (GetRelationship("Silver") == "Friend"):
    silver @happymouth "I should let you know, I don't hold back against my friends."

    red @happy "Nor do I. So prepare for the fight of your life."

else:
    silver @smilemouth "Yeah, we'll see."

hide silver with dis

jump PickTable