label lunch010510:

show hilda frownmouth uniform:
    xpos 0.33
show hilbert uniform:
    xpos 0.66
with dis

narrator "As you walk into the cafeteria, you suddenly notice Hilda and Hilbert standing in a corner, talking intently about something."

pause 1.0

narrator "...You think about moving away from their conversation, but you're in line, and the Miltank ribeye looks {i}really{/i} good."

hilda @talkingmouth "{size=30}I'm worried about you, Hilbert.{/size}"

hilbert @talkingmouth "There's nothing to be worried about."

hilda @closedbrow talkingmouth "Don't give me that shit. You've been completely out of it for, like, three weeks now. Even {i}before{/i} the elections. And you're spending {i}way{/i} more time with that Nathan guy."

hilbert @sadbrow talkingmouth "It's just Nate. And of course I'm spending time with him. We're roommates."

hilda @angry "Yeah, we're {i}also{/i} roommates, but you're not hanging off of my hip every moment."

pause 1.0

hilbert @talkingmouth "Is there something {i}wrong{/i} with me having other friends?"

hilda @sad "No, of course not, Hilbert, you {i}know{/i} I want that for you. But I'm concerned that you're..."

pause 0.5

hilda @talkingmouth "...I've never seen you so focused. It's like you {i}know{/i} what you're doing. Like you have a plan, for the first time."

hilbert @sadbrow talkingmouth "...Ridiculous."

show hilda sad with dis

hilbert @closedbrow talkingmouth "I'm just as aimless as I've ever been. Don't worry, your refusal to help me fulfill my dream is as effective as it's ever been."

pause 2.0

hilbert @sadbrow talkingmouth "...Sorry. That was unnecessary."

hilda -sad frownmouth @closedbrow talkingmouth "...Yeah, maybe a bit. But I get how you feel."

pause 1.0

hilbert @talkingmouth "I don't."

hilda @surprised "Huh?"

hilbert @talkingmouth "I don't feel. 'Feel' implies passion, or desire. My dream is an absolute. It's the tracks ahead of me. It is a task that must be done{w=0.5} like breathing."

pause 1.0

hilda @angrybrow talkingmouth "...I've heard that shit before. And you know what I think of it."

pause 0.5

hilbert @sadbrow talkingmouth "...I'm bored of this conversation."

hilda @closedbrow talkingmouth "Fine. I just wanted to tell you that I care about you, and I don't want you ramming your face headfirst into another pile of shit..."
hilda @closedbrow talking2mouth "...Before you let me grab a shovel, anyway."

hide hilbert 
hide hilda 
with dis

pause 1.0

narrator "Hilda and Hilbert part ways."

menu:
    ">Leave them alone":
        pass

    "[bluecolor][[Hilbert Rank 1]{/color} >Chase after Hilbert" if (GetRelationshipRank("Hilbert") > 0):
        $ AddEvent("Hilbert", "ChaseAfter")
        show hilbert uniform with dis

        pause 0.5

        hilbert @talkingmouth "I presume you heard that."

        red uniform @talking2mouth "Yes."

        hilbert @sadbrow talkingmouth "It was a distraction. Like everything is."

        pause 0.5

        hilbert @talkingmouth "Like {i}you{/i} are."

        pause 1.0

        hilbert @sadbrow talkingmouth "You know where my path ends. The limelight of a transforming Pikachu, battles against famous friends, the spectacle of the road to champion..."

        pause 0.5

        hilbert @talkingmouth "That's not got anything to do with me."

        pause 1.0

        red @talking2mouth "It could. {i}After.{/i}"

        hilbert @talkingmouth "There's no after for me."

        red @talkingmouth "Then don't shy away from what you have in the present."

        hilbert @talkingmouth "...Are you saying that, even now, you think there's some merit to existing within my sphere?"

        red @happy "I told you I'd show you the light, Hilbert. And based on that scowl on your face, you're still {i}very{/i} in the dark."

        hilbert @closedbrow smilemouth "Your efforts are...{w=0.5} {i}foolish.{/i}"

        $ ValueChange("Hilbert", 1, 0.5)

        hilbert @sadbrow talkingmouth "But I will not turn them away."

        hide hilbert with dis

        pause 1.0

        redmind @thinking "Oh, man..."

        hide hilbert with dis
    
    "[bluecolor][[Hilda Rank 1]{/color} >Chase after Hilda" if (GetRelationshipRank("Hilda") > 0):
        $ AddEvent("Hilda", "ChaseAfter")
        show hilda uniform with dis

        pause 0.5

        hilda @talkingmouth "Ah, I guess you heard that, huh?"

        red uniform @sadbrow talkingmouth "Little bit?"

        hilda @closedbrow talkingmouth "Man, I don't like airing our dirty laundry out in public like that."

        red @talkingmouth "If it helps, at all, I think your patience is kinda... well, insane, honestly!"
        red @sadbrow happymouth "In a good way. If a bit self-injurious."

        hilda @closedbrow smirkmouth "I'm tough. I can take it."

        pause 1.0

        hilda @sadbrow talkingmouth "How've you been? We haven't had a real chance to reconnect since... well, since you went absolutely fucking ballistic during the Quarter Qlashes."

        red @happy "Absolutely ballistic is right. I'm alright. Answering a lot of questions other people have about my power, and my Pikachu."
        red @sadbrow talkingmouth "Anything I can answer for you?"

        hilda @talkingmouth "Nah, I listened to your speech. I get the gist."

        red @closedbrow talking2mouth "Thank God."

        hilda @talkingmouth "...But seriously, is there anything I can do for {i}you?{/i} Those elections... {i}damn.{/i} Shit went {i}south.{/i}"

        red @sadbrow talking2mouth "I'm still trying to get you to take more breaks and do stuff for yourself. I couldn't ask for anything."

        $ ValueChange("Hilda", 1, 0.5)

        hilda @happy "Aw. You're a good guy, [first_name], you know that?"

        hide hilda with dis

narrator "As you walk away, you hear another conversation starting nearby..."

pause 2.0

show bianca uniform sadeyebrows frownmouth:
    xpos 0.75 ypos 1.0
    block:
        ease 0.3 ypos 1.1
        ease 0.3 ypos 1.0
        repeat 20
show rosa uniform frownmouth
with dis

bianca @cryingeyes cry sad3mouth "{size=30}...and Sabrina's not there and Tia's not there, which is awful, of course, but then Professor Will isn't even there either and I don't know what we're going to do because classes are cancelled and if we can't attend class we can't learn about Psychic-types and if I don't learn more about Psychic-types then I can't raise my starter and if I can't raise my starter then I'll fail out of school and die!{/size}" (what_line_spacing=1)

show bianca uniform sadeyebrows frownmouth:
    xpos 0.75 ypos 1.0

rosa @sadbrow talkingmouth "I don't think that's going to happen, Bianca, but it {i}is{/i} concerning... we don't want to let ourselves slip behind..."

bianca @closedeyes talking2mouth "I kinda get why Sabrina would leave, but Tia always seemed to really like the class, and there's no way that Instructor Will would have just left."

rosa @sadbrow talkingmouth "...I guess we just have to hope that the school's administration figures out what's going on before we fall too far behind."

bianca @angrybrow talkingmouth "Why should we fall behind? Let's just study with each other!"

rosa @sadbrow talkingmouth "I'm not sure... do we know enough to even help each other study at the level Instructor Will teaches at?"

bianca @closedbrow talking2mouth "Maybe not at {i}his{/i} level... but we can still do our best!"

rosa @happy "Alright... alright! I like the enthusiasm! Yeah, let's do this!"
rosa @sideeyes sadeyebrows talkingmouth "Um... just don't tell anybody about this. Because I think it might be against one of my contracts..."
rosa @happy "Alright, it's a plan! And then, maybe we can go out and rescue Sabrina and the others?"

redmind uniform @thinking "Rescue?"

bianca @confusedeyebrows talkingmouth "Rescue?"

rosa @angrybrow talkingmouth "Yes, rescue. 'When someone needs help, it's the duty of the people left behind to rescue them.' That's the way it is in {i}all{/i} my movies."

bianca @talking2mouth "Okaaaaay... but where are they, then?"

hide rosa
hide bianca
with dis

rosa uniform @sweat sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

bianca uniform @tonguemouth animepleasedeyes "One scene at a time, Rosa."

rosa @closedbrow sweat talkingmouth "Yeah..."

pause 1.0

redmind uniform @thinking "Hearing Rosa reminded me of how Leaf was talking about {i}her{/i} rescue mission for me. Maybe those two would get along better than you'd think."

pause 1.0

redmind @thinking "Speaking of which... where {i}is{/i} Leaf?"

pause 0.5

narrator "Trying to ignore the subtle whispered accusations that surround you as you walk into the dining room, you realize that the sitting arrangement of the tables seems to have shifted around dramatically."

redmind @playfuleyes frownmouth unamusedeyebrows "Oh, great. It'll take me ages to open these tables up again."

pause 1.0

Character("Ruinous Boy") "\"{size=30}...the freak's there! Don't let him sit here...{/size}\""

Character("Emotional Juvenile") "\"{size=30}...'Frienergy'? Yeah, right...{/size}\""

Character("Nancy Brat") "\"{size=30}...can't believe I ever...{/size}\""

redmind @sweat closedbrow "...You know what? I think I've passed the point where I need to worry about the desolation of my social standing. I'm just going to sit wherever I want, and if people have a problem with it, well, I can work on them."

redmind @thinking "Anyway, if I want to study my Psychic elective, I should probably join the table with all the Psychic-Type students... the ones that are left, at least."

jump PickTable