label lunch010514:

Character("Disreputable Blackheart") "\"{size=30}...still here? Thought he would've left by now...{/size}\""

Character("Joking Judas") "\"{size=30}...just ignore him...{/size}\""

Character("Mealymouthed Advisor") "\"{size=30}...I heard he told a Ninetales to attack the school...{/size}\""

if (mayhaslarvesta):
    Character("Bitter Bug Catcher") "\"{size=30}...stole a Larvesta!{/size}\""

show serena angrybrow frownmouth uniform with dis

serena @angrymouth "...I {i}beg{/i} your pardon? Perhaps you'd like to whisper those dark words a bit louder?"

Character("Irritable Imbecile") "\"God, don't make a {i}thing{/i} of it, Kalosian. C'mon, lads.\""

pause 1.0

red uniform @sadbrow talkingmouth "Thanks."

serena -angrybrow @sadbrow talkingmouth "It's only the right thing to do. I suppose you've been handling a lot of that recently?"

red @closedbrow sweat talkingmouth "I wouldn't exactly call it... 'handling' it. But yeah, I've been hearing a lot of it."

serena @talkingmouth "...I suppose it is some relief then, that your power is not as strong as you may have feared."

red @talkingmouth "Little bit, yeah."

if (GetRelationshipRank("Serena") > 0 and not HasEvent("Serena", "Level2SceneVer2")):
    serena -frownmouth @talkingmouth "Well, though I never need an excuse to enjoy your company, I {i}did{/i} come over here with an objective."

    show serena surprisedbrow frownmouth with dis

    red @talkingmouth "I'm not surprised. You've always got one mission or another you're on. I'm pretty impressed by how clearly you can see the path."

    pause 1.0

    $ ValueChange("Serena", 1, 0.5)

    serena @talkingmouth "Ah."

    pause 1.0

    red @confused "What?"

    serena closedbrow @talkingmouth "Ah, well... you remember our conspiracy?"

    red @talkingmouth "Sure. Make sure Calem stays single. Very easy. Very possible, despite how handsome he is. What about it?"

    pause 1.0

    serena sadbrow -frownmouth @talkingmouth "I need... the {i}opposite{/i} of that, actually."

    pause 2.0

    red @unamusedeyebrows playfuleyes unamusedmouth "{i}What.{/i}"

    serena @talkingmouth "I... am trying to get Calem to, um, {i}be with{/i} someone else."

    red @talkingmouth "Huh. So, wait, are you dating?"

    serena @closedbrow talkingmouth "No, no. We're just... rooming together."

    red @confused "So, what triggered this? I mean, this is a complete 360 from where you were before."

    serena @closedbrow talking2mouth "You mean a 180." 
    serena @talkingmouth sadbrow "And... well... it's difficult to describe, but... ah..."

    red @talkingmouth "I thought you wanted to date him?"

    serena @sad "I did! Er... I thought I did? But then I moved in with him, and everything has become so much more difficult, and... I don't know if... that is, to say, I'm unsure if..."

    serena pout "...I mean, ah... it would be easier if he were {i}not{/i} single, since... in regards to... ah..."

    redmind "What's the problem? It looks like she's trying to say something she doesn't know how to say."

    serena @angry "Oh, what-{i}ever!{/i} Listen up, [first_name]. We'all need to get that boy hitched to some other chick--or man, it don't matter--before I have a nervous breakdown!" 
    serena @angry "He's too damn kind, and didn't even {i}mention{/i} the fact I've been lyin' to his face for ages!"

    pause 1.0

    serena -pout @closedbrow sadmouth "Apologies."

    red @talkingmouth "Nah. I get where you're coming from, now. But, one question: what exactly does Calem want out of this?"

    serena @sadbrow talkingmouth "I... honestly have no idea."

    redmind @thinking "...Okay, I realize that I'm being a hypocrite here, given the whole Frienergy thing, but this school {i}desperately{/i} needs a class on communciation."

    red @closedbrow talking2mouth "Alright. So the conspiracy's going in the opposite direction, now. Fine. We're trying to get Calem together with someone else."

    pause 1.0

    red @confused "Do you have any candidates in mind?"

    serena @talkingmouth "Yes. But perhaps we should discuss this another time, less publicly. I'm worried we might be attracting undue attention."

else:
    serena @talkingmouth "Well, I'm confident you'll get through this. It is weak men who chastise others from the shadows."

    red @happy "Thanks, Serena."

    serena @talkingmouth "It is, as always, my pleasure and privilege. Now, please pardon me. I must be off."

red @talkingmouth "Alright. Talk to you later, then."

hide serena with dis

jump PickTable