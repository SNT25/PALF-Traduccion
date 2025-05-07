label lunch010525:

narrator "As you walk into the cafeteria, you suddenly notice a diverse group of students standing around a table, with a not-so-recognizable figure at the center."

show may uniform frownmouth:
    xpos 1.0/10.0
show brendan uniform frownmouth behind may:#god i wish that was me
    xpos 2.0/10.0 xzoom -1
show serena uniform frownmouth:
    xpos 3.0/10.0
show misty uniform behind serena:
    xpos 4.0/10.0 xzoom -1
show lisia incognito incogbrow incogshades:
    xpos 5.0/10.0
show dawn uniform behind lisia:
    xpos 6.0/10.0
show tia uniform hat frownmouth:
    xpos 7.0/10.0
show klara uniform hairpin makeup shadow angrybrow frownmouth behind tia:
    xpos 8.0/10.0
show jasmine uniform frownmouth:
    xpos 9.0/10.0
with dis

redmind uniform @thinking "Eesh. They don't look happy. Well, except Dawn."

show klara -shadow surprised sweat with dis:
    xpos 8.0/10.0

lisia @talkingmouth "With Phobos here, we absolutely {i}cannot{/i} afford to put forth anything less than our absolute best."

show klara puppybrow frownmouth with dis:
    xpos 8.0/10.0

lisia @closedincogbrow talking2mouth "Our success as Coordinators depends on our success in the Millennium Drop Water Festival Contest."
lisia @talkingmouth "That's why I {i}need{/i} to call another meeting this evening."

$ PlaySound("class_groan.ogg", "crowd2")

brendan @talking2mouth "I get that this contest is really important, but what does... uh, Foe-Boast? What does Foe-boast being here have to do with that?"

lisia @talking2mouth "He's one of the school's board members. And one of the richest, too."

misty @angry "No wonder, if our tuition's been going to him!"

may @closedbrow talking2mouth "Brendan and I were really hoping for a break, though..."

lisia @talking2mouth "Look. Battlers don't take us seriously. They never have. There's a reason the only region where contests are actually {i}popular{/i} is Hoenn, and it's just because they were invented there." 
lisia @angryincogbrow talking2mouth "If we {i}want{/i} battlers to take us seriously--if we want World Contest Champion to someday hold the same weight as 'World Champion'--then we need to {i}be serious{/i}."

pause 1.0

if (not HasEvent("Klara", "BreakHeart")):
    klara @talking2mouth "I was going to go on a date, though..."

    lisia @closedincogbrow talking2mouth "There are more important things to do today than go on dates, Klara."

jasmine @closedbrow sweat talking2mouth "...I've attended all these emergency meetings so far, but it's... tiring. Moreso than I'm accustomed to handling..."

lisia @sadincogbrow talkingmouth "I'm not asking any of you to do more than you can do. I'm only asking you to do the {i}most{/i} you can do."

misty @closedbrow talkingmouth "I guess we have to. None of us are going to walk away from direct instruction by Lisia, anyway..."
misty @surprised "But I still don't get what that pompous blowhard Phobos has to do with this."

serena @surprised "Is it not apparent?"

misty @closedbrow talkingmouth "Just tell us."

serena @talkingmouth sadbrow "Well, if he's a coordinator, he will be inclined to assist us... monetarily, no?"

may @talking2mouth "He wouldn't want to do that if it turns out there's no amount of money that could make us shape up, though..."

lisia @talking2mouth "That's exactly right. That's why we need to win the Millennium Drop Water Festival Contest--"

if (GetRelationshipRank("Tia") > 0):
    tia @thinking "Does she have to say the whole thing every time?"

else:
    tia @thinking "{font=fonts/sign.ttf}Does she have to say the whole thing every time?{/font}"

lisia @talking2mouth "To prove to Phobos that the Coordinator Club deserves {i}just{/i} as much funding as the Battle Team."

misty @closedbrow talking2mouth "That'll never happen. Kobukan's battle team is legendary. Besides, they've got the Tamamushi family bankrolling them now."

lisia @angryincogbrow happymouth "Exactly. They don't need the school's funding--they can just reach into Tamamushi's pockets! And I happen to know for a {i}fact{/i} that Phobos isn't overly fond of the Battle Team."
lisia @closedincogbrow talking2mouth "I'm sure we can get him to divert some funding... but only if we prove to him we're worth it."

lisia angryincogbrow frownmouth @talking2mouth "That's why I don't want to see a single non-Kobukan student in that winner's circle, and that's why we're having an emergency meeting after school today!"

show may closedbrow talking2mouth
show brendan closedbrow sweat talking2mouth
show serena closedbrow sadmouth
show misty closedbrow sweat talkingmouth
show dawn happy
show tia closedbrow sweat
show klara closedbrow sweat talking2mouth
show jasmine closedbrow sweat talking2mouth
with dis

Character("The Coordinator Club") "\"Yes, Liz...\""

dawn @happy "Cheer up, guys! More practice just means we'll shine even better when the contest happens!"

redmind @thinking "Hm... seems like Dawn's the only one who doesn't mind the intense training. I guess, since she's already used to the Battle Team, this probably feels easier..."

hide may
hide brendan
hide serena
hide misty
hide dawn
hide tia
hide klara
hide jasmine
hide lisia
with dis

narrator "The Coordinator Club eventually disperses."

redmind @thinking "Right, I should go find a table, now..."

show klara uniform surprised makeup hairpin with vpunch

klara -surprisedbrow -frownmouth -surprised @surprised "Oh, wow! [first_name]! I totally didn't notice you here."

red @happy "Hey."

klara @blush puppybrow sadmouth "Oh, no, I'm sorry, I didn't mean that you're easy to miss. You're really not. I was just surprised, that's all."

if (not HasEvent("Klara", "BreakHeart")):
    klara @sadbrow sadmouth "Oh, but that reminds me! I've got really bad news..."

    klara @closedbrow talking2mouth "We're going to have to postpone our date."

    red @talking2mouth "I figured. Nothing that can be done about it, though. Lisia's really serious about training you guys. Just the way it is."
    
    show klara surprisedbrow frownmouth with dis
    
    red @happy "I've got something tomorrow, but how about a raincheck to Thursday?"

    klara @talkingmouth "Huh? Why would we need to delay it {i}that{/i} long?"

    red @confused "Well, I mean..."

    klara -surprisedbrow -frownmouth @happy "Oh, it's because of Leaf, isn't it? I'm sorry, I know exactly what you're talking about. She's always dropping out of her commitments."
    klara @talkingmouth "We don't need to delay more than a few hours. We can meet up after the Coordinator Club meeting. I'll just meet you outside Relic Hall."

    red @closedbrow talking2mouth "Hm? Wouldn't that be after curfew, though?"

    klara @talkingmouth "Yeah, but..."

    if (not HasEvent("Instructor Koga", 1)):
        klara @sadbrow talking2mouth "Well, just between you and me, I've heard a lot of shady stuff about Silver. Everyone in Poison class says that he's got a gang that he runs with, and did you hear when he cussed out Lance earlier this year?"
        klara @closedbrow talking2mouth "{i}I{/i} think he's a nice guy, of course. Just a bit awkward. But he acts like a delinquent sometimes, and he and Grusha often meet up in a shady alley in the city."
        klara @sadbrow talking2mouth "I can't imagine what they're doing, but... well, I'm pretty sure Grusha's giving Silver money for something..."

        if (GetRelationshipRank("Silver") > 0):
            red @talking2mouth "Silver's a good guy. Whatever he's doing, I'm sure it's nothing as bad as it looks."

            $ ValueChange("Silver", 1, 0.3)

            narrator "Your confidence in Silver is resolute."

            klara @happy "Well, yeah, like I said, {i}obviously{/i} he'll be a good night watchman, but that's only one, right?"

            if (GetRelationshipRank("Skyla") > 0):
                red @confused "Hm? Nah, Skyla's really dilligent. She takes her job super-seriously--at least as much as she can." 
                red @talkingmouth "She really wants to help and protect people, and if preventing them from going out does that, she'd do that as best as she can."

                $ ValueChange("Skyla", 1, 0.7)

                narrator "Your confidence in Skyla is also resolute."

                klara @happybrow anger "Yeah! Duh! That's what I said!"
                klara happybrow anger madmouth "Skylie and Silver are totally on top of things. But they can't cover the entire school by themselves. Cheren's gotta be somewhere, and we both know he's an incompetent mess."

                pause 0.5

                klara -happybrow -anger -madmouth @puppybrow talking2mouth "I mean, that's what I've heard."

        else:
            klara @talkingmouth "Anyway, I have a feeling that he's not part of the disciplinary committee to stop people from going out at night."

    else:
        klara @talkingmouth "The Disciplinary Committee isn't, like... all that good at their jobs? They're constantly fighting with each other, and everyone hates Cheren."
        klara @happy "Like, even if someone caught us, they wouldn't {i}report{/i} us to the Disciplinary Committee. Honestly, the formation of the Disciplinary Committee kinda made the rules a {i}lot{/i} looser."

    red @closedbrow talking2mouth "I guess that makes sense. Then, where...?"

else:
    red @talkingmouth "Totally fine."

klara @happybrow happymouth "Oh! I {i}just{/i} had this idea, totally off the top of my head. But since you're here..."
klara @puppybrow talkingmouth "Would you like to come with me to today's emergency Coordinator Club meeting?"
klara @talking2mouth "Not to do anything, I'm just asking if you'd like to watch. It's after classes let out, so I guess you wouldn't have any free time, but watching one of Lisia's club meetings is really a one-time experience!"

redmind @thinking "Hm... Yellow mentioned she might want to watch that, too. Maybe if I go there, I'll run into her. On the other hand, I might want to do something else this evening... but, like Klara said, this is a one-time thing."
redmind @thinking "Besides, all the other Coordinators are going to be at the meeting."

menu:
    "Sure, I'll go.":
        $ AddEvent("Klara", "AcceptCoordinatorClub")
        $ ValueChange("Klara", 10)
        klara @surprisedbrow surprisedmouth "Really? Awesome! I love how you think all my ideas are so good--your support means a ton to me."
        klara @happybrow happymouth "That's a really admirable trait! Just another reason I like you!"

        red @talkingmouth "See you later, then."

        klara @talkingmouth "See you later, then!"

    "Sorry, I'm busy.":
        klara @surprisedbrow surprisedmouth "Hah, wow! Really? I mean, okay. I guess you're really confident in what you already know, then?"
        klara @happybrow happymouth "That's a really admirable trait! Just another reason I like you!"

        red @talkingmouth "Talk to you later, then."

        klara @talkingmouth "Talk to you later, then!"

hide klara with dis

pause 1.0

redmind @confusedeyebrows frownmouth "Where's she going? {i}This{/i} is the cafeteria."

pause 1.0

redmind @thinking "Maybe she's eating in the garden again." 
redmind @happy "Well, whatever. I'm in the mood for... Toedscruel rims? Yum!"

jump PickTable