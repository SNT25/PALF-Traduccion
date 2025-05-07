label lunch010511:

show cheren uniform noshine with Dissolve(2.0)

red uniform @angryeyebrows frownmouth shadow "{w=0.5}.{w=0.5}.{w=0.5}."

cheren @talkingmouth "...That's quite an expression. I rather like it."

pause 1.0

cheren @talking2mouth "You must hate me."

menu:
    "Hate isn't strong enough.":
        $ AddEvent("Cheren", "StrongHate")
        $ ValueChange("Cheren", -3, 0.5)

        cheren @closedbrow talking2mouth "I'm glad to see where you stand, then."

    "I don't care enough to hate.":
        $ AddEvent("Cheren", "NoCare")
        cheren @closedbrow talking2mouth "Fair enough."

    "[ellipses]":
        $ AddEvent("Cheren", "SilenceHate")
        cheren @talking2mouth "This will be easier, {i}for both of us{/i}, if you {i}do{/i} hate me."

pause 1.0

red @angrybrow talking2mouth "What do you want?"

cheren @talking2mouth "Nothing. However, the Disciplinary Committee's head would like you to come with me for a short meeting."

label cherenchoices:

menu:
    "Never.":
        cheren @talking2mouth "An appropriate response. Allow me to clarify--this is not an invitation."

        menu:
            "Still never.":
                cheren @sad2eyes talking2mouth "Hm."

                cheren @talking2mouth "I will ask you one more time. Direct defiance of a Disciplinary Committee member's order permits me to elevate the issue to your homeroom teacher."
                cheren @talking2mouth "Upon doing that, you will have to comply with his request. If you refuse to do so, you will have to answer to Dean Drayden."
                cheren @talking2mouth "Dean Drayden who, might I remind you, controls the apportionment of scholarships and admittance status of the student body."

                menu:
                    ">Punch him in the face":
                        $ AddEvent("Cheren", "PunchCheren")
                        stop music channel "crowd"
                        stop music channel "crowd2"
                        stop music
                        
                        $ PlaySound("thud2.ogg")
                        
                        show cheren surprisedblackeye surprisedeyebrows -shadow:
                            xpos 0.5 ypos 1.0 zoom 1.0 rotate 0
                            linear 0.1 ypos 0.95 zoom 0.95 rotate 1
                            pause 0.5
                            "cheren uniform shadow disappointedblackeye neutraleyebrows angrymouth"
                            ease 0.7 ypos 1.2 rotate 10
                        show cafe with vpunch

                        narrator "Cheren lays still. For a moment, you're worried you'd punched him too hard, but..."

                        show cheren neutralblackeye -surprisedblackeye -surprisedeyebrows noshine:
                            ypos 1.2 rotate 10 zoom 0.95 
                            ease 0.5 ypos 1.0 zoom 1.0

                        cheren @talking2mouth "Nevermind. I thought I did not understand you. Now, clearly, I do. I see your very essence."

                        cheren @sadmouth "You... are an ape."

                        show cheren -surprisedbrow -frownmouth -surprised:
                            rotate 10
                            ease 0.5 rotate 0

                        cheren @anger2blackeye anger2 angrymouth "A violent, self-serving, impulsive, lustful, wrathful, and prideful {i}ape{/i}, who ought to be destroyed for everyone else's safety."

                        pause 1.0

                        cheren shadow @sad2blackeye talking2mouth "Fool."

                        hide cheren with dis

                        pause 0.5

                        $ renpy.music.play("Audio/bigcrowdloop.ogg", channel='crowd', loop=True, fadein=0.5)

                        queue music "Audio/Music/Route 1 Anime.ogg"

                        redmind @happy "That might not have been the smartest thing to do, but boy was it satisfying."

                        jump PickTable

                    "For the third time, no.":
                        $ AddEvent("Cheren", "RejectCherenMeeting")
                        cheren @talking2mouth "...Very well. You'll be hearing from Professor Oak, then."

                        pause 1.0

                        cheren @sad2eyes talkingmouth "Fool."

                        hide cheren with dis

                        jump PickTable

                    "Fine.":
                        cheren @talking2mouth "Thank you. Please come with me."

            "Fine.":
                cheren @talking2mouth "Thank you. Please come with me."

    "Fine.":
        cheren @talking2mouth "Thank you. Please come with me."

    "Explain." if not HasEvent("Cheren", "ExplainMeeting"):
        $ AddEvent("Cheren", "ExplainMeeting")
        $ ValueChange("Cheren", -3, 0.5)

        cheren @upeyes noshine talking2mouth "I don't like to do so."
        cheren @talking2mouth "...But fine. I am not acting in a personal role. I am the Disciplinary Committee's instrument. I would like nothing more than to never interact with you again."
        cheren @sad2eyes sadmouth "But, for the safety of others, such that I might repent, I have sublimated my will to the school's control. So, for the school, I ask for this meeting."

        jump cherenchoices

scene blank2 with splitfade

show screen songsplash("Embracing One's Duty", "Zame")
stop music fadeout 1.5
queue music "audio/music/embracingonesduty.ogg"

pause 1.0

scene studentcouncil
show cheren uniform noshine
show skyla uniform surprised at leftside
with splitfade

pause 1.0

skyla -surprisedbrow -frownmouth -surprised @surprised "W-woah! Boss! You're back early!"

cheren @talking2mouth "He proved less trouble to track down than I thought."

if (GetRelationshipRank("Skyla") > 0):
    $ skylarelationship = GetRelationship("Skyla")
    red uniform @sadbrow talking2mouth "Skyla? You're working with {i}him?{/i} Aren't I meant to be {i}your{/i} [skylarelationship]?"

    skyla @talkingmouth "...Yes. But it's not because of you! It's because of Sabrina! What happened to her was {i}awful,{/i} and I want to make sure nothing like that happens again."

    cheren @talking2mouth "Relatedly, it is the matter of Sabrina that made me bring [first_name] here today."

cheren @closedbrow talking2mouth "When you're done with the paperwork, you can go."

skyla @sweat happy "Uh... I think it might be a {i}long{/i} time before I'm done with this paperwork... Should I just go into the side office?"

cheren @talking2mouth "{w=0.5}.{w=0.5}.{w=0.5}.I suppose you might as well stay. This concerns you, too. Is Silver not around?"

red uniform @angryeyebrows talking2mouth "Right... Silver's working with you, too."

cheren @sad2eyes talking2mouth "Yes."

pause 0.5

if (HasEvent("Cheren", "StrongHate")):
    cheren @closedbrow talking2mouth "If it's any consolation, he despises me as much as you do."
else:
    cheren @talking2mouth "If it's any consolation, he despises me as much as any other student."

cheren @sad2eyes talkingmouth "The Disciplinary Committee is certainly not formed around the charisma of its head."

pause 1.0

cheren @talking2mouth "Skyla, Silver?"

skyla @surprised "Oh, right! Um... I don't know. He said he was heading out for a smoke."

cheren @talking2mouth "I do not believe he smokes."

skyla @happy sweat "Yeah, I've never seen that."

cheren @talking2mouth "Whatever. Enough ado."

pause 0.5

cheren @talking2mouth "[first_name], Sabrina Natsume is missing. Bianca Vongole is too."

redmind @confusedeyebrows frownmouth "{i}Natsume?{/i}"

cheren @talking2mouth "They are likely in the burned forest. Instructor Will was sent in after them. He has also failed to return."

red @talking2mouth "...Well?"

cheren @closedbrow talking2mouth "It would reflect poorly on the Disciplinary Committee if we were unable to retrieve these missing personnel."
cheren @talking2mouth "Even moreso if another unaffiliated student {i}were{/i} to do so."

red @angryeyes frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

cheren @talking2mouth "For this reason, it is instructed that you do not leave the campus at night to venture into the forest. Such an activity would be foolhardy, dangerous, and {i}not{/i} endorsed."
cheren @talking2mouth "Of course, as is always the case, there is no way I could stop you from doing what you want."

pause 0.5

red @talking2mouth angryeyes "I understand."

cheren @talking2mouth "The exception to this, of course, is if you were to assist in the Disciplinary Committee's own retrieval efforts."
cheren @sad2eyes talking2mouth "We aim to bring back Instructor Will--perhaps his knowledge could be of some use to us in retrieving the other two."

if (GetRelationshipRank("Sabrina") > 0):
    red @talkingmouth "Really? You did all that shit to Sabrina, and you're not trying to rescue {i}her?{/i}"

    cheren @talking2mouth "I am trying to rescue {i}everyone.{/i} Instructor Will is the logical person to seek out first--he will give us greater odds in the other pursuits."
    cheren @closedbrow talking2mouth "I do not expect you to believe, nor understand me, but my guilt for what my actions have done to Sabrina is immense."
    cheren @upeyes talking2mouth "Clearly, though, because I am attempting to pursue the path that gives everyone the greatest chance for a happy ending, I am a monster."

red @talking2mouth "...At night, you said?"

cheren @talking2mouth "That would be preferable. Though if you can manage it in your evenings, more power to you."
cheren @talkingmouth "We also cannot stop you from bringing any accomplices along on these excursions. That being said..."
cheren @closedbrow talking2mouth "There may be... {i}complications{/i}, if others were to see how dire the situation is."
cheren @talking2mouth "For that reason, if you choose to callously disregard the Disciplinary Committee's instructions and succeed in rescuing someone, we ask you bring them straight to the infirmary, and inform us at your leisure."
cheren @talking2mouth "There is no need to involve any except the minimum required to rescue everyone in this mess."

pause 1.0

cheren @talking2mouth "...I'd recommend doing it soon, too. They've already been missing quite a while. I shudder to imagine what might happen if they were left there any longer than Friday." 
cheren @closedbrow sadmouth "Sunday is the absolute last day they have before... Dean Drayden's backup plan arrives."

pause 0.5

cheren @talkingmouth "Speaking of, given that the Disciplinary Committee spent all week, last week, looking for the missing students and faculty, and failed, I managed to secure a reprieve of penalty from Dean Drayden."
cheren @talkingmouth "The students who missed the Quarter Qlashes will not be punished. Unfortunately, they will still not be able to participate in any future Quarter Qlashes, but that's a matter for the Kobukan league, not our academy."
cheren @sad2eyes talking2mouth "Of course, Drayden was disappointed to hear that the Disciplinary Committee had failed to find the people in question. He would be further disappointed to hear we have failed again."

pause 1.0 

cheren @closedbrow talking2mouth "But that's a consequence we Disciplinary Committee members will face. Live as you wish."

pause 0.5

cheren @closedbrow talking2mouth "Do you have any questions?"

menu:
    "Why'd you do it?":
        cheren @sad2eyes talkingmouth "Why?"

        pause 1.0

        cheren @talking2mouth "Skyla, would you please give us some time?"

        hide skyla with dis

        pause 0.5

        red @sadbrow talking2mouth "I thought we were friends, man. I trusted you. I even supported you. I was going to {i}vote{/i} for you."

        cheren @talking2mouth "And I to you."

        pause 0.5

        cheren @talking2mouth "So why didn't you tell me about your power?"
        cheren @angryeyes talking2mouth "Why didn't you tell {i}anyone{/i}?"

        pause 1.0

        cheren @talking2mouth "You may not believe this, but I felt no ill will to you. I still do not. But I absolutely cannot understand you. And, as it seems everyone else can, I cannot understand them, either."

        red @talking2mouth "I only wanted to help people, man. People would be weirded out if they knew I had a power. I didn't want to do that to them."

        cheren @talking2mouth "So your silence was for the greater good."

        red @talking2mouth "Yes."

        cheren @talking2mouth "Then my lack of silence was for the same."
        cheren @sad2eyes talking2mouth "They adored you. Everyone. And they didn't even know why. You could have given them the courtesy of giving them a choice as to whether they loved you."

        red @closedbrow talkingmouth "Look, it's not mind control-"

        cheren @angryeyes angrymouth "I {i}know{/i} it's not mind control! It was never about if it was mind control or not! It was about the way people fawned over you with little to no effort on your own part!"
        cheren @sad2eyes angryeyebrows angrymouth "Certainly, I feared that it {i}may{/i} be mind control, but regardless of what it was, it clearly had to {i}stop!{/i}"

        pause 1.0

        cheren @upeyes talking2mouth "And, somehow, the speech you gave to the entire student body has convinced them that {i}I{/i} was wrong--as though you were not admitting to exactly what I accused you of."

        pause 1.0

        red @talkingmouth "Does it matter if people like me a little more easily? I'm not a bad guy. I'll only help people."

        pause 0.5

        cheren @talking2mouth "There is a story from Galar. Perhaps you're familiar with it."
        cheren @closedbrow talking2mouth "There was a noble king, wise and fair. He gathered about him eleven honorable knights, brave and just, and one more. These knights followed the king's every word, and never questioned his goodness."
        cheren @talking2mouth "With him, he had a wife. But the king was a busy man, as he had many adoring citizens to appease. He could not pay attention to his wife. So this wife's heart strayed, and she fell in love with the twelfth knight."
        cheren @talking2mouth "The king's wife, and this knight, eloped. The punishment for leaving the king was death. So the king, with a heavy heart, ordered his men to find and murder his wife and knight."

        pause 1.0

        cheren @sad2eyes talking2mouth "So they obeyed."
        cheren @talking2mouth "Isn't it interesting? These eleven knights, who were good men, expressed loyalty, a virtue. But these good men, driven by a virtue, did evil work."

        red @talking2mouth playfuleyes unamusedeyebrows "I don't get it."

        cheren @talking2mouth "It is a {i}danger{/i}, [first_name], for there to be any man whose goodness is unquestioned. Who engenders loyalty beyond logic."
        cheren @talking2mouth "Even with all I've done, I only managed to slow you down. I now rely on my classmates' ability to stop themselves from becoming hopelessly dependent on you."

        pause 0.5

        cheren @upeyes talkingmouth "I may as well rely on a Magikarp to climb a waterfall. But I've done all I can."
        cheren @talking2mouth "...I do not expect us to speak again, except when necessary. We are fated, I believe, to misunderstand each other forevermore."

        red @sadbrow talking2mouth "I don't want that."

        cheren @talking2mouth "We don't always get what we want, [first_name]."

        pause 1.0

        cheren @talking2mouth "Oh, and one more thing."

        if (ninetalesobj in playerparty):
            cheren @talking2mouth "I'm aware of that Ninetales you carry on your belt."

        else:
            cheren @talking2mouth "You may recall that Ninetales that was outside Pledge Hall."

        cheren @talking2mouth "In the event that any more of these 'wild' Pokémon attack the school, I will be turning over every leaf and stone in order to find proof you are the one doing it."

        red @upeyes talking2mouth "I'm not."

        cheren @surprisedeyebrows talking2mouth "Hm?"

        pause 1.0

        cheren @closedbrow talking2mouth "Well... perhaps it is no surprise that I believe you. But that does {i}not{/i} mean you are telling the truth."

        redmind @thinking "Geez."

        cheren @talking2mouth "That is all. You may go back to lunch."

        pause 2.0

        $ ValueChange("Cheren", -5, 0.5)

        cheren shadow sad2eyes talking2mouth "I just don't understand that man..."

    ">Leave without a word":
        show skyla surprisedbrow frownmouth with dis

        pause 0.5

        cheren closedbrow shadow "Hm."

call clearscreens from _call_clearscreens_146
scene blank2 with splitfade

pause 1.0

scene cafe 
show screen currentdate
with splitfade

jump PickTable