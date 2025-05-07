label lunch010528:

show silver uniform with dis

silver @talkingmouth "Hey, red."

red uniform @talkingmouth "Hey. Don't you have to go chew out Melody?"

silver @talkingmouth "Ninth time this week. All she does is waste our time, since the worst we can do is tell the Student Council, and they won't do anything about her."

red @closedbrow talking2mouth "Roxanne said she couldn't do anything either. She said even Drayden can't do anything."

silver @sad "Damn. I wish she'd just disappear..."

pause 1.0

silver @surprised "W-wait, I wasn't asking you to do anything to her! That wasn't a command!"

red @confused "No, I know."

silver @sad "Good. Sometimes, my tenants, if I make an offhand comment about something... anyway, I gotta be careful about what I say."

pause 1.0

silver @closedbrow talkingmouth "Anyway, I just wanted to ask you something. During gym class, it looked like Ethan's Pichu was... I dunno. Sparking, or something."

red @sad2eyes sweat talking2mouth "W-well, it {i}is{/i} an Electric-type..."

silver @angrybrow talkingmouth "Bull. There's more to it than that. It looked like the same kind of thing your Pikachu did in that fight against Dawn. What's going on?"

if (GetRelationshipRank("Silver") > 0):
    redmind @thinking "Well... Silver {i}is{/i} my friend. I guess I should tell him."

    red @talking2mouth "I'll tell you, but please keep it secret."

    $ ValueChange("Silver")

    silver @closedbrow talkingmouth "Thanks. And don't worry, I'll bury it."

    show silver surprisedbrow with dis

    red @talkingmouth "Blue's Eevee can make the same gems that my Pikachu can. He gave a couple of those gems to Ethan and Yellow to make up for a misunderstanding."

    silver -surprisedbrow @sad "That doesn't sound like Blue..."
    silver @closedbrow talkingmouth "I guess he's got more depth than I thought. Whatever. I get it. So Blue's the one spreading these powers around?"

    red @confused "I'm pretty sure it's a one-time thing. He only gave them out because he felt pretty bad."

    silver @sad "...Yeah, let's hope."

else:
    show silver angrybrow with dis

    red @sadbrow talkingmouth "I'm... sorry. I don't think I can tell you."

    pause 1.0

    silver @talkingmouth "I've got my eye on you, red."
    silver @sad "That airhead, Skyla, doesn't think you're dangerous. Cheren thinks you could {i}become{/i} dangerous."
    silver @talkingmouth "But I know you {i}are{/i} dangerous. Anyone with power is."

    pause 0.5

    red @talking2mouth "But... doesn't everyone have {i}some{/i} power?"

    silver @closedbrow talkingmouth "Exactly."

silver @talkingmouth "See you around."

hide silver with dis

$ removelunchstudents = { "Silver", "Cheren", "Skyla", "Melody" }

jump PickTable