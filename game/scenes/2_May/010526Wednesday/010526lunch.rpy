label lunch010526:

show klara makeup uniform hairpin with dis

if (GetRelationshipRank("Klara") > 0):
    klara @happy "Hiii, sweetie!"

else:
    klara @happy "Hi, [first_name]."

red uniform @happy "Hey. What's up?"

klara @surprised "Oh, I can't believe I forgot, but we should totally exchange contact info."

if (GetRelationshipRank("Klara") > 0):
    klara @sadbrow blush talkingmouth "I mean, after last night..."

else:
    klara @sadbrow blush talkingmouth "I mean, you know, if you ever want to meet up and do anything... um..."

red @happy "Sure. What's yours?"

klara @happy "Oh, why don't you just give me your phone? I'll put it in for you."
klara @sadbrow blush talkingmouth "And then you can put yours in mine."

pause 1.0

if (HasEvent("Klara", "FirstBase")):
    redmind @thinking "Pretty sure I already did."

else:
    redmind @poutmouth sad2eyes "I deserve some sort of award for not making a joke out of that."

$ BecomeContacted("Klara")

if (GetRelationshipRank("Klara") > 0):
    klara @talkingmouth "Anyway... I really enjoyed yesterday. Want to do it again tonight?"

    red @happy "I don't think my sleep schedule could take two nights of that in a row."
    red @talkingmouth "Besides, I've got something planned with Leaf. I thought I mentioned that...?"

else:
    klara @talkingmouth "Anyway... Want to do something tonight?"

    red @talkingmouth "Sorry, I've got something planned with Leaf. I thought I mentioned that...?"

klara @closedbrow talkingmouth "Well, yeah, you've got 'something planned'..."

pause 1.0

red @confusedbrow frownmouth ".{w=0.5}.{w=0.5}.{w=0.5}?"

klara @sadbrow talkingmouth "Look, I just don't want you to be disappointed if... um... she backs out again."
klara @happy "But if she does, I'm here for you. I think being reliable is a really important quality for a person."
klara @sadbrow talkingmouth "That's why I like {i}you{/i} so much. I know I can trust you."

red @closedbrow talkingmouth "I'll keep that in mind. But it's not, like, she's {i}trying{/i} to push it off. We've just had some bad luck."

klara @sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."
klara @talking2mouth "Some people... just look for the easy way to get what they want. If it's a breakup, they just leave their partner. If it's money, they just take it. If it's to put off a long-standing engagement..."
klara @closedbrow talking2mouth "Well, you know. I'm not saying that Leaf's doing that, of course. Just that some people do."
klara @happy "I really like putting in the work to get what I want, though! It makes it much more satisfying, to know I've {i}earned{/i} whatever I get."

pause 0.5

klara surprisedbrow frownmouth @surprised "Oh!"

show klara with dis:
    xpos 0.5
    ease 0.5 xpos 0.66

show leaf uniform with dis:
    xpos 0.33

if (HasEvent("Leaf", "AcceptedConfession")):
    leaf @happy "Hey, [first_name]! Date update: We are {i}still{/i} on track!"

else:
    leaf @happy "Hey, [first_name]! Not-a-date update: We are {i}still{/i} on track!"

klara -surprisedbrow -frownmouth -surprised @happy "Heyyyy, Leaf! How are you, bestie?"

show leaf uniform with dis:
    xpos 0.33 xzoom 1
    ease 0.5 xpos 0.33 xzoom -1

leaf surprisedbrow frownmouth @talking2mouth "Hm? Oh, um, I'm... I'm fine? Bestie?"

pause 1.0

leaf @talkingmouth "Oh, shoot, sorry, I totally interrupted what you were doing here, didn't I? My bad!"

klara @talkingmouth "No, it's fine! I know you felt left out. It's totally fine."

leaf @surprisedbrow talkingmouth "...Oh. Um, well, that was pretty much it, anyway. I can just leave now. It's really no problem."

klara @happy "What're you talking about, Bestie? You've been talking about this date you've been planning for months now. Now that it's {i}actually{/i} going to happen, I want to know every detail!"

if (not HasEvent("Leaf", "AcceptedConfession")):
    red @talking2mouth "It's not a date."

    leaf @surprisedbrow talking2mouth "I didn't say it was!"

leaf @sadbrow talkingmouth "It's really not that big a deal... and besides, I want it to be a bit of a surprise for [first_name], you know?"

klara @talking2mouth "Oh, no, I totally get it. I mean, I helped you plan a bunch of those previous ones, but I guess since those didn't work out, you'd just try to do it yourself, right?"

leaf @closedbrow talkingmouth "Uh... Klara, you didn't really help me plan any of those plans, though."

klara surprisedbrow frownmouth @talking2mouth "Oh."

klara puppybrow @talkingmouth "...I'm sorry. I thought I {i}was{/i} helping... I guess I was just getting in your way."
klara @closedbrow talking2mouth "What about your Ivysaur...? Did I not actually teach it Instructor Koga's special move? Was I just a problem then, too?"

leaf @surprised "N-no! You weren't ever in the way! I'm sorry, I misspoke--you weren't a problem at all!"

klara @sadbrow talking2mouth "...Oh..."

pause 0.5

klara @talking2mouth "Then... will you tell me what you're doing for this date...?"

if (not HasEvent("Leaf", "AcceptedConfession")):
    redmind @frownmouth closedbrow "It's still not a date. But maybe now isn't the time to interrupt."

leaf @closedbrow talkingmouth "Oh, alright."
leaf -surprisedbrow -frownmouth @flirtbrow talkingmouth "Sorry, [first_name]. You're going to have to wait another...{w=0.5} three hours for your hint."

red @unamusedbrow talking2mouth "I may actually die of anticipation."

leaf @closedbrow talkingmouth "Classic. Made it four weeks, but that last three hours was the straw on the Camerupt's back."

red @talking2mouth "The time of death on my gravestone is going to have to be very specific."

leaf @closedbrow talkingmouth "Huh. I just realized something--how come they don't put cause of death on gravestones any more?"

red @surprisedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
red @confused "You know, I don't know. I don't think I realized until {i}just now{/i} that that was a thing."
red @confused "But you're right. Like, really old gravestones will say 'run over by a Ponyta' or 'run over by a Mudsdale' or 'run over by a Blitzle'."

leaf @talkingmouth "Okay, I've got a different question. What the hell kinds of cemeteries do you have in Pallet Town?"

red @talking2mouth "Apparently cemeteries populated by people who, in life, were pretty vulnerable to getting run over by equine Pokémon."

leaf @closedbrow talkingmouth "That's going to be the new battle meta. Pallet-types are weak to Horse-types."

show leaf surprisedbrow frownmouth with dis

red @unamusedbrow talking2mouth "If we're talking about the weaknesses of people in our hometowns, you're standing in a pretty glass house."

pause 1.0

leaf @happy "You dick! I can't believe you went there."

red @closedbrow talking2mouth "Yeah, I realized it was too far halfway through saying it. Thanks for not blowing up at me."

leaf @sarcastic "Was that another volcano joke?"

red @talkingmouth "Not intentionally, but I'm going to fill my mouth with food before I find another way to put my foot in it."

leaf happy "Good idea."

hide leaf
hide klara 
with dis

$ removelunchstudents = { "Leaf", "Klara" }

jump PickTable