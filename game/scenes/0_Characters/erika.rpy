label Erika1:
    scene garden:
        zoom 0.625
    show clouds behind garden
    with Dissolve(2.0)

    stop music fadeout 1.5
    queue music "audio/music/celadon_start.ogg" fadein 1.5 noloop 
    queue music "audio/music/celadon_loop.ogg"

    narrator "You're walking through the garden when you suddenly hear a somewhat familiar noise--{w=1.0}soft, unconscious breathing."

    $ PlaySound("!.ogg")

    red @surprised "Oh, crap."

    redmind @thinking "That's definitely Erika. I didn't realize I'd wandered toward her nap spot..."
    redmind @thinking "Okay, I need to get out of here without her seeing. There's no outcome in which she doesn't get mad at me if she catches me here while she's sleeping, and Professor Cherry isn't here to bail me out this time..."#FIX THIS: If your character becomes class enough with Professor Cherry to call her "Kris"

    pause 0.5

    redmind @sadbrow frownmouth "Why do all these bushes look the same...?"

    show blank2 with transeye

    narrator "Picking a direction, you forge forward blindly..."

    pause 1.0

    narrator "Which you should really know better than to do by this point."

    scene gardennook
    show erika closedbrow 
    with transeye2

    pause 0.5

    redmind @unamusedbrow unamusedmouth "...All roads lead to slapping, I guess."
    red @closedbrow talking2mouth "C'mon, [pika_name], let's get out of here. Even if it didn't hurt, I don't want to give her another chance to accuse me of something I didn't do..."

    $ PlaySound("Pokemon/pikachu_sad.ogg")
    libpikachu @angrybrow poutmouth "Pi..."

    red @surprised "Hm? You doing something there, [pika_name]?"

    $ PlaySound("Pokemon/pikachu_norm1.ogg")
    libpikachu @closedbrow talkingmouth "Pika."

    narrator "[pika_name] crawls off your shoulder, then steps lightly onto the floor. Making his way stealthily over to Erika's sleeping figure, he simply headbutts her ankle."

    redmind @surprised "Wait, you're {i}waking her up?!{/i} Traitor!"

    erika -closedbrow @happybrow tears surprisedmouth "{i}Yawwwwn...{/i}"
    erika @unamusedbrow frownmouth "Hmm...?"
    erika @surprised "Oh. I must have dozed off while reading this book."
    erika @confusedeyebrows talkingmouth "But what woke me...?"

    $ PlaySound("Pokemon/pikachu_happy1.ogg")
    libpikachu @happy "Pikachu!"

    erika downeyes @talkingmouth "Oh? A Pikachu?"

    $ PlaySound("Pokemon/pikachu_happy2.ogg")
    libpikachu @angrybrow happymouth glowing "Pikerachu!"

    erika surprised "Oh! [first_name]'s Pikachu! But if you are here, then..."

    show erika surprisedbrow frownmouth:
        ypos 1.0 zoom 1.0
        ease 0.3 zoom 0.9 ypos 0.9
    
    red @sadbrow talkingmouth "Hi."

    pause 1.0

    erika frownmouth @sad2eyes talking2mouth "H... hello."

    pause 0.5

    red @talkingmouth "Well, I was, just, um, on my way out of here. Didn't mean to wake you up."

    erika @closedbrow talking2mouth "Of course. 'Pray, do not allow me to hinder you in the least.'"

    red @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    pause 0.5

    red @sad2eyes talking2mouth "...Hey, sorry if this is coming out of nowhere, but... are you scared of me?"

    erika @surprised "Wh-what!? No! By, er, which I mean... 'What, pray tell, could have led you to entertain such a notion?'"

    red @talkingmouth "Well, the moment you saw me, you hid behind that bench. That was kind of a sign."

    show erika surprisedbrow frownmouth:
        ypos 0.9 zoom 0.9
        ease 0.7 zoom 1.0 ypos 1.0

    red @closedbrow talking2mouth "I guess you don't do that in Battle Team meetings, or in Gym Class, though..."
    red @confused "Oh, wait, is it because it's just the two of us, here?"
    red @happy sweat "If so, I actually get that. Sorry--I'll leave."

    show erika:
        ypos 1.0 zoom 1.0
        ease 0.3 ypos 1.2 zoom 1.2

    erika frownmouth @angry "'I beseech you, do not depart!'"

    red @surprisedbrow talking2mouth "Woah. Okay. No beseeching necessary. I'll stay."

    pause 1.0

    red @confused "...But why?"

    show erika:
        ypos 1.2 zoom 1.2
        ease 0.5 ypos 1.0 zoom 1.0

    erika @sadbrow talkingmouth "My honor has been greatly damaged through my actions, yet further through inaction."
    erika @talkingmouth "I would ask that you help me restore it."

    pause 1.0

    red @confused "Um... honor?"

    erika @sadbrow talking2mouth "Oh."
    erika @sad2brow talking2mouth "It is a word that means... ah... the worth of a person."

    red @unamusedbrow talking2mouth "I know what honor means."
    red @confused "At least, I thought I did? I think our definitions are a bit different."
    red @talking2mouth "Whatever. What exactly ruined your honor? And why do you need {i}me{/i} to help you restore it?"

    erika @talking2mouth "Oh. You do not remember? Perhaps it was of less import to you."
    erika @talking2mouth "'I am quite uncertain whether I wish to recall to you my past transgressions, then...'"
    erika @closedbrow talking2mouth "'But uncertainty is, as ever, the violator of progress, such that my path is laid out clearly and immovably.'"

    pause 1.0

    red @talkingmouth "Y-yeah. My thoughts exactly."

    erika @talkingmouth "As it seems you have no recollection, let me impart this memory."
    erika @sad2eyes talking2mouth "On the sixth of May, I arose a motion to attempt to have you removed from the Battle Team."

    pause 1.0

    redmind @unamusedbrow unamusedeyes "Is she for real?"

    pause 0.5

    show erika surprisedbrow with dis

    red @closedbrow talking2mouth "Yeah, no, I remember {i}that{/i}. I guess the part I'm not getting is how that ruined {i}your{/i} honor?"

    if (not HasEvent("Erika", "AcceptApology")):
        erika -surprisedbrow @talking2mouth "Because, when I apologized, my apology was not accepted... and thus there is a stain between us. One of imbalance. Dishonor." 

        red @closedbrow sweat talking2mouth "...You don't really need to consider my acceptance of an apology so highly."

    else:
        erika @surprised "Because I moved to take action against an innocent person! Imagine my horror had I succeeded!"

        red @confused "Yeah, I'm sure that'd be pretty, uh, horrifying for you."

        erika @sad2eyes talking2mouth "Though I have apologized, and you have graciously accepted that apology, the truth remains that there is a transgression on my record... and thus there is a stain between us. One of imbalance. Dishonor." 

        red @closedbrow sweat talking2mouth "It was a crappy thing to do, but you apologized, I accepted, it's in the past. You don't really need to keep bowing and scraping over that. "

    erika -surprisedbrow @sadbrow talkingmouth "...I'm afraid I do, though."
    erika @talkingmouth closedbrow "The Tamamushi family, of which I am a proud member, does not permit favors to be given, nor apologies to be left unaccepted."
    erika @talkingmouth "Anything that may make us owe another... any debt we might have to some other party... we do not allow such things, not in our business, nor in our personal lives."
    erika @talking2mouth "The act itself enough was enough to imbalance our ledgers, but that would have been a justified transaction only if it truly been in the best interest of the Battle Team--which I believed it to be."
    erika @sad2brow talking2mouth "But intent is not enough of a factor to void action, nor effect."

    pause 1.0

    if (not HasEvent("Erika", "AcceptApology")):
        red @sad2eyes angryeyebrows talking2mouth "Look. I'm not going to accept that apology. But that's fine, alright? You don't need to take it so seriously."
    else:
        red @sad2eyes sadeyebrows talking2mouth "Look. It's all done on my side. Like I said, it's in the past. We can move on. You don't need to take it so seriously."

    pause 0.5

    erika @sad2brow talking2mouth "It is not, in its entirety, within my power to decide."

    red @confusedeyebrows talking2mouth "Hm?"

    erika @talkingmouth "My Father... er, Shoku Tamamushi, has rather mandated that I expunge this blemish."#Yes, I know it means "Meal". Don't @ me.
    erika @happy "I've a rather sizeable apportionment allocated for this express purpose, actually, so I consider this a sign that it is a significant priority to my father."

    red @surprised "He... gave you {i}money{/i} to spend on 'restoring your honor?'"

    erika @talking2mouth "That is its intended usage, yes."

    pause 1.0

    erika @talking2mouth "I know that I cannot simply pay you to forgive and forget, though. Do not fear, I've no intent to insult you in that fashion."

    redmind @poutmouth sad2eyes "I mean... depending on amounts... doesn't hurt to try, right?"

    red @talking2mouth "Okay. So, I'm still one hundred percent willing to go, if you want, but you seem a bit more comfortable now."
    red @sadbrow talkingmouth "Is it alright if I ask a question or two?"

    erika surprised @talkingmouth "I ask only that you permit me the same courtesy."

    red @talkingmouth "Sure. So, first question: What exactly is the Tamamushi family?"

    erika "You jest?"

    red @talkingmouth "Not this time."

    erika -surprisedbrow -frownmouth -surprised @talkingmouth "Oh. Well, then... my family is, er, privileged to be the owners of Silph Co. Between my father, uncle, and elder male cousins, they have a controlling interest in it."

    red @talking2mouth "Huh. {i}The{/i} Silph Co.? Like, the one that makes most of the Poké Balls, battle items, medicines and stuff in Kanto?"

    erika @talkingmouth "The very same. Though our reach is not purely Kantonian. Johto, too, is all but ours, with Sinnoh shortly behind. Why, if it were not for Devon, then we may very well claim the continent."
    erika @sadbrow talkingmouth "But supposedly the government hinders our attempts at preventing Devon from existing. I am unsure of the particulars, but my father is quite insistent they are, ah, 'totalitarian fascists' on the matter."

    red @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
    redmind @sadbrow frownmouth "I think... I think I'm getting it, now. She really... doesn't know anything."

    red @talkingmouth "It sounds like your father's pretty important to you?"

    erika -frownmouth @happy "More than I could ever say. I adore him. He is my greatest blessing, moreso than any bill or coin I may possess."

    red @talking2mouth "...Okay. Do you, uh, have any siblings?"

    erika angrybrow frownmouth @surprised "Oh? No, that's an odd question. 'Why, pray, do you inquire?'"

    red @closedbrow talking2mouth "Well, I'm just wondering if you're going to inherit your father's shares in the company. If you had siblings, then I assumed--"
    red @confused "Wait, what did I say wrong?"

    erika @talking2mouth "Your inquiries into my father's business are highly suspicious. I suspect you to be motivated by more than idle curiosity."

    red @sadbrow talkingmouth "...Did you father tell you to be suspicious of other people?"

    erika @surprised "I... well, yes. I am the delicate flower of the Tamamushi family, as he always says. My mere existence invites kidnappers, ransomers... even duplicitous business partners."
    erika @talkingmouth "'Every friend is one fey mood away from becoming a creditor--every relationship must be looked at from the angle of one who has much to lose from it.'"
    erika surprisedbrow frownmouth @talking2mouth "And he also warned that they may send handsome men as scouts, to pry into Silph Co.'s plans... I shall not be lead astray by such an obvious ploy."

    red @happy "Hey, thanks."

    erika @closedeyes angryeyebrows lightblush talking2mouth "This was not intended to aggrandize you."

    red @talkingmouth "Don't worry, I'm not even a little aggravated. I took it as a compliment."

    erika @sad2eyes sadmouth "I... Ah. Perhaps I have done it again. You weren't trying to pry at all, were you?"
    erika -surprisedbrow @closedbrow talking2mouth "Apologies."

    pause 1.5

    redmind @surprisedbrow frownmouth "Oh my god, I can't believe playing dumb actually worked here. I thought for {i}sure{/i} that Frienergy would have busted me here."

    red @happy "Well, if you don't want to talk about business{w=0.5}--and I don't blame you{w=0.5}--let's talk about something else."
    red @talkingmouth "What's that book you're holding?"

    erika @talkingmouth "Oh. Yes, I was reading it when I fell asleep. It's called... '{i}Valedictory Elegies.{/i}'"
    erika @talkingmouth "The account of a certain Kobukan student who, after graduating top of his class, realized he'd wasted his life on academic achievement and promptly took his own life."
    erika @sadbrow talkingmouth "...It is an enthralling read, but one I must confess I've read 'til the pages are threadbare. Or pulpbare, as it were. Perhaps explaining my narcoleptic lapse just now."

    red @talkingmouth "Oh, so you're reading it again? I could recommend some new books."

    erika @happy sweat "Not easily, though the thought is much appreciated. I must write a report on the book, to be submitted to my tutors, before I am allowed to read it."
    erika @sadbrow talkingmouth "As the flower of the Tamamushi family, my time is too important to be taken up reading noncontributory literature. This method ensures that any book which does not pass muster does not waste my time."
    erika -frownmouth @sadbrow talkingmouth "Though if you pray permit a moment of selfishness... I would quite like to read some 'lesser' books. Just so I may know what to avoid. But I understand that is not in my best interest."

    red @surprised "What? But... how do you write a report on a book you haven't read?"

    erika @closedbrow sweat talking2mouth "I will confess I had some difficulties, when this process was implemented. I believe I was four years old at the time."
    erika @talkingmouth "It's manageable enough now, though. I need simply read reviews of the book in {i}other{/i}, already-approved books. These books often have descriptors of plot, in addition to evaluations of literary merit."
    
    redmind @sadbrow frownmouth "That's actually psychopathic."
    red @closedbrow talking2mouth "I guess that makes it hard to avoid spoilers, then."

    erika @surprisedbrow talking2mouth "Spoilers?"

    red @sadbrow talkingmouth "Yeah, you know. Like, the twists at the end of the book. The surprises?"

    erika @surprised "Why would... why would one want to be {i}surprised{/i} by a book? That's the sort of lowest-common-denominator appeal reserved for reality television, is it not?"
    erika @sad2brow talking2mouth "It is unfortunate enough that reality contains so many unpleasant surprises... illness, divorce, remarriage, death... I prefer the world of fantasy to be free of such things."

    red @sad2brow talking2mouth "I'm... not sure how to respond to that. Let's just go back to the book thing."
    red @talkingmouth "You said there were some pre-approved books that you could get reviews for other books from, right? What sorts of books are those?"

    erika @talkingmouth "Oh, they're my father's personal favorites. 'Superior literature penned by a higher class of individual,' as he says. Though nonfiction, they often make reference to other fictive books."
    erika @talkingmouth "Every two months or so, I get a letter that lists the new additions to that hall of fame. I believe I have this month's somewhere..."

    show erika:
        ypos 1.0 zoom 1.0
        ease 0.5 ypos 1.2 zoom 1.3

    narrator "Erika produces a piece of paper, handing it, almost proudly, to you."

    show erika:
        ypos 1.2 zoom 1.3
        ease 0.5 ypos 1.0 zoom 1.0

    red @winkeyes sadeyebrows sweat talking2mouth "I'm almost afraid to look, but..."

    Character("Note") "\"- The Traditional Woman's Bible\"{w=1.5}\n\"- Conservative Fiscal Policy for Children\"{w=1.5}\n\"- Reclaiming Kanto; The Solution to the Johto Problem\""

    pause 0.5

    redmind @thinking "It's actually worse than I thought."

    narrator "You absent-mindedly fold the paper up and put it in your pocket, trying to come up with a way to state what comes next tactfully."

    red @winkeyes sadeyebrows sweat talking2mouth "Your father seems to have very distinct tastes."

    erika @talkingmouth "A byproduct of his upbringing. He went to the finest schools, much as I have had the chance to do now. As he says."
    erika @talkingmouth "Kobukan is only the most recent of the world-class schools I have attended... though I always had a specialized, personal, curriculum, at those other schools."
    erika @surprised "Dean Drayden seemed against allowing the implementation of such a thing at Kobukan--I can't imagine why. The courses are already so famously flexible."

    red @talkingmouth "Hm... what kind of other schools did you go to?"

    erika @talkingmouth "Celadon Preparatory Grammar School. Followed swiftly by Celadon Primary Grammar School, on the same campus."

    red @talkingmouth "Was it actually a grammar school?"
    
    erika @talkingmouth "No longer, though it was founded as one."
    erika @talkingmouth "I then attended La Mesa Escuela Primaria Avanzada in Paldea, before graduating and going to Naranjuva Academy."

    red @happy "Hey, I've heard of that one!"

    erika @talkingmouth "I then graduated that, and... well, now I am here."

    red @talkingmouth "Sounds like you spent quite a while in Paldea. You don't have an accent at all, though."

    erika @surprised "Oh, heaven forbid. Can you imagine a Tamamushi speaking with that... that... dialect?"

    red @sad2brow talking2mouth "...I mean, it's just an accent. People say my accent makes me sound like a farmer."

    erika @talking2mouth "I... {i}did{/i} assume it was a family business."

    red @closedbrow talkingmouth "...Nah. But tell me more about Paldea. What's it like?"

    erika @happy "Oh, it is as a dream. Sunny and beautiful. The people are clean and well-dressed. Children roam the region without fear."
    erika @sadbrow talkingmouth "At least, that is what the travel guides said. I rarely left my campuses. During my many years there, I did not even catch a single Paldean Pokémon..."
    erika surprised @talkingmouth "But Silph Co. has always had a mastery of seeing that which does not yet exist. The Terastal energy in Paldea is a fascinating phenomenon with many applications beyond..."

    pause 1.0

    erika -surprisedbrow -frownmouth -surprised @closedbrow talking2mouth -sweat "Regardless of reason, I was there for many years."
    erika @talkingmouth "...And during my time there, when my Father visited... we met many interesting people. The Elite Four of the Paldean League, of course. Business partners."
    erika angrybrow talking2mouth shadow "...And then there's someone else."

    pause 0.5

    erika sad2brow frownmouth -shadow @talking2mouth "I apologize. I do not believe I am in any further mood to discuss the particulars of my time in Paldea."

    red @sadbrow talking2mouth "Okay."

    erika @closedbrow talking2mouth "I am sorry for wasting your time with my idle chatter. 'Small talk is a poison most afflict'd, a breath of death to deprive intellectuals of the benefits of higher conversation.'"
    erika @sadbrow talkingmouth "It is easy to forget this quote when one is... 'chatting.'"

    pause 1.0

    if (not HasEvent("Erika", "AcceptApology")):
        erika @talking2mouth "I must ask again. Will you accept my most ardent apology for my transgressions? For slapping you the day we met, and for attempting to have you removed from the Battle Team?"

        menu:
            "Sorry, no.":
                erika @closedbrow talking2mouth "I fully understand. Take this as no sign of my resignation on the matter, though."

            "Yes.":
                $ AddEvent("Erika", "AcceptApology")
                $ AddEvent("Erika", "AcceptSecondApology")
                $ ValueChange("Erika", 10)

                erika @closedbrow talkingmouth "It does my heart much good to hear that. Thank you."

    erika @closedbrow talkingmouth "I have enjoyed our time here, and it is only with reluctance that I must insist on our parting, now. I have much to think on."

    red @sad2brow talking2mouth "Yeah... okay."

    pause 1.5

    show erika surprisedbrow frownmouth with dis

    red @happy "Hey. Crazy question. Have you ever considered writing something yourself?"

    erika "{w=0.5}.{w=0.5}.{w=0.5}."

    red @sadbrow talkingmouth "Guess that's a no. Something to think on, maybe."

    narrator "You depart."

    pause 1.0

    erika @closedbrow talking2mouth "Why did he say that? Does he think that I...?"
    erika surprised "Oh! He took my list of approved books!" 

    pause 1.0

    erika sad2brow talkingmouth "W-well... given this list  was wrested from me by a dastardly [bluecolor]thief{/color}, who overpowered me, then, surely... my only resolution is to remember what was on it. And any miscarriages of memory can hardly be considered my fault..."

    hide erika with Dissolve(1.0)

    narrator "Erika quickly heads off in the direction of the library."

    $ persondex["Erika"]["Nature"] = TrainerNature.Neutral
    $ RelationshipRankUp("Erika", "Thief", 1)

    narrator "Erika's Nature shifts from {color=#0048ff}Distant{/color} to {color=#0048ff}Neutral{/color}!"

    return