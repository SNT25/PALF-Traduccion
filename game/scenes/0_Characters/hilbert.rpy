label Hilbert1:
    if (not IsBefore(1, 5, 2004)):
        $ persondex["Hilbert"]["Events"].append("Level2SceneVer2")

    scene city_B
    show hilbert:
        xpos 0.5 ypos 0.9 zoom 0.8
    with Dissolve(2.0)
    stop music fadeout 1.5
    show screen songsplash("Victory Road", "Zame")
    queue music "audio/music/victory_start.ogg" noloop
    queue music "audio/music/victory_loop.ogg"

    narrator "You're in Inspira when you come across Hilbert, standing, frozen, staring at a statue."
    narrator "His unmoving body cuts through the waves of people splitting around him like the hull of an icebreaker, uncaring of the flow of humanity all around."

    pause 0.5

    red @talkingmouth "Hey, Hilbert."

    hilbert @surprised "Hm? Oh."

    pause 0.5

    hilbert @talkingmouth "It's you."

    red @closedbrow talking2mouth "Warm as ever."

    show hilbert:
        ease 0.5 ypos 1.0 zoom 1.0

    pause 0.5

    red @talkingmouth "Checking out the modern art?"

    hilbert @talkingmouth "No. This is {i}classical{/i} art. Pre-renaissance. Medieval."

    red @confused "Wait, isn't Kobukan a really new region? Just a couple hundred years?"

    narrator "Hilbert rolls his eyes and wordlessly points at the plaque on the bottom of the statue."

    narrator "You take a better look at the statue. It is composed of iron, and appears to be of a knight, sword upraised and mouth frozen in an eternal rallying cry."
    narrator "At the dark knight's feet is a child, swaddled up in the knight's discarded cape."

    "Plaque" "IN MEMORIAM OF\n{w=0.5}THE SACRIFICES REQUIRED TO\n{w=0.5}FREE UNOVA OF KINGS." 
    "Plaque" "LET KOBUKAN BENEFIT.{w=0.5}\n{size=15}(Paid for by the Unovan Heritage Association.){/size}"

    hilbert @talkingmouth "Hmph."
    hilbert @closedbrow talking2mouth "A 'gift' from Unova. More like a reminder of what Kobukan owes them."

    red @talkingmouth "You think they gifted Inspira the statue just to remind people that Unova is nearby, and very powerful?"
    red @happy "I think anyone with a map would remember that one."

    hilbert @closedbrow talkingmouth "People don't remember anything that isn't in their face."

    narrator "Hilbert's voice is thick with bitterness."

    red @talking2mouth "...Do you want to talk?"

    if (IsBefore(1, 5, 2004)):
        hilbert @sadmouth "How long have we been roommates? You know this. Obviously, I don't want to talk."

    else:
        hilbert @talkingmouth "How long were we roommates? You know this. Obviously, I don't want to talk."

    red @confused "...Right."

    pause 1.0

    red @closedbrow talking2mouth "What if I wanted to talk?"

    hilbert @closedbrow talking2mouth "I would not be surprised. Has anyone ever told you you're a chatty gossip, [first_name]?"

    red @talking2mouth "Yeah. [blue_name]."

    red @confused "Has anyone ever told you that you need to work a bit harder at getting along with people?"

    pause 0.5

    hilbert @smilemouth "Yes. Hilda."

    red @closedbrow talkingmouth "That checks out."

    pause 1.0

    red @talkingmouth "So, what's your story with her?"

    hilbert @sadbrow talkingmouth "...It really is impossible to turn you off, isn't it?"

    red @talkingmouth "Kinda, yeah."

    hilbert @talkingmouth "Fine. Let's go find somewhere to sit down, though. I can't stand up any longer."

    narrator "Peering closer at Hilbert, you do notice that he's starting to sweat quite a bit in the cool air, as though he was physically over-exerted."

    red @talkingmouth "Uh, sure. A friend of mine has a house here. Want to go there? It's a bit more shaded."

    hilbert @closedbrow talkingmouth "How far?"

    red @confused "Uh, about two miles."

    hilbert @talkingmouth "That's a long walk."

    red @confused "It's like, fifteen minutes, tops. You can do it."

    hilbert @talkingmouth "It's two miles. In order to get there in fifteen minutes, we'd need to walk at eight miles an hour. The average walking speed is three miles per hour. If you--"

    show hilbert surprisedbrow frownmouth with dis

    narrator "You begin walking away."

    hilbert "Wait. Wait, no, come back! I wasn't--"

    scene black with splitfade

    narrator "You make your way to Silver's house, Hilbert in hot pursuit. Every time he gets within ten feet of you, he attempts, indignantly, to explain through his labored breathing why this walk {i}is{/i}, in fact, too long."
    narrator "Of course, he never gets the chance." 
    narrator "By the time he's regained his breath enough to speak, you've already moved thirty feet away from him, using your long legs and not-utterly-ignored musculature to your advantage."

    pause 0.5

    narrator "You sneak a peek over your shoulder at his small form hurrying after you, and you can't help but smirk. He's actually kinda cute... {w=0.5}when he isn't talking, anyway."

    scene abandonedhouse 
    show hilbert angry at night
    with splitfade

    hilbert "{w=0.5}Hah... {w=0.5}Hah... {w=0.5}...Hah. D-don't... {w=0.5}Hah..."

    red night @happy "See? Told you you could make it."

    hilbert @closedbrow angrymouth "And I... told {i}you...{/i} that it was too long a walk."

    pause 2.0

    hilbert -angry @talkingmouth "...Where are we?"

    red @talkingmouth "A friend's house."

    hilbert @angrybrow talkingmouth "Your friend lives in a shack in the middle of the city?"

    if (IsBefore(26, 4, 2004)):
        red @talkingmouth "We can't {i}all{/i} live in palaces, Prince Hilbert."
    else:
        red @talkingmouth "We can't {i}all{/i} live in palaces, Prince von Schwarzdrachen."

    hilbert @surprised "What?"

    red @talkingmouth "Oh, I just called you--"

    hilbert @talkingmouth "No, I know {i}what{/i} you said. {i}Why{/i} did you say that name?"

    red @talking2mouth "...I dunno, man. Sorry if I crossed a line. I was just poking fun at you, since you were acting kinda... princely."

    hilbert @sadbrow talkingmouth "...Tch. That's what my mother used to call me."

    red @closedbrow talking2mouth "Aurea?"

    hilbert @closedbrow talking2mouth "No, Professor Juniper is my guardian. My {i}mother.{/i}"

    red @closedbrow talking2mouth "Um... Hilda?"

    pause 1.0

    hilbert @closedbrow talkingmouth "{size=30}God.{/size}"

    red @happy "Sorry, Hilbert! I don't think you've mentioned your mother before."

    hilbert @talkingmouth "{w=0.5}.{w=0.5}.{w=0.5}.I thought I had.{w=0.5} I suppose I forgot."

    red @talkingmouth "Well, now's as good a time as any, right?"

    hilbert @talkingmouth "She's dead."

    red @surprised "Oh."

    hilbert @talkingmouth "Father's dead, too."

    red @sad "Oh."

    hilbert @talkingmouth "They were murdered. Right in front of me."

    red @sad "Oh..."

    hilbert @talkingmouth "And I swore, on that day, that I would kill the one responsible."

    red @surprised "Oh!"

    pause 1.0

    red @talking2mouth "Wait, {i}kill{/i}?"

    hilbert @talkingmouth "Yes."

    red @talkingmouth "Not... 'find'? Or 'bring to justice'? Or even 'punish'?"

    hilbert @talkingmouth "No. Kill. Revenge is my ideal. I've no interest in the truth."

    pause 1.0

    red @closedbrow talking2mouth "That's... pretty heavy, man."

    hilbert @talkingmouth "It's the only thought that's occupied my mind for many, many years. I've been plotting. Hating. Dreaming of when I could get my revenge."
    hilbert @angry "I have been wallowing in darkness. To the point the dark, and the cold, has become my own bitter blade."

    red @talkingmouth "Uh..."

    hilbert @angry "The dragon of the meteor will fall at my hand. And then, if there's a life left for me..."

    pause 0.5

    hilbert @talkingmouth "...I guess I'll go to prison."

    red @surprised "What?"

    if (not IsBefore(1, 5, 2004)):
        redmind @frownmouth "The dragon of the meteor? He can't be... he {i}can't{/i} be talking about Tia, can he?"
    else:
        redmind @frownmouth "The dragon of the meteor? He can't be... he {i}can't{/i} be talking about Rayquaza, can he?"

    hilbert "{w=0.5}.{w=0.5}.{w=0.5}."

    hilbert @talkingmouth "You don't seem phased."

    red @talking2mouth "Honestly, I'm just not sure how to react. This is a lot you're dropping on me."

    hilbert @sadbrow talkingmouth "Do you see why I don't talk, now? Can you imagine what it's like trying to have friends, have a normal conversation, when you've been planning a death ever since you were twelve?"

    if (not IsBefore(1, 5, 2004)):
        hilbert @talkingmouth "I despise how easily it comes to you. I loathe that you made me trust you, when you knew full well what power you had."

        red @sadbrow talking2mouth "Hilbert, I didn't know about Frienergy until a couple weeks into the year..."

        hilbert @angry "And when you found out, did you tell me about it? Did you tell anyone?"

    pause 1.0

    red @talking2mouth "No."

    if (not IsBefore(1, 5, 2004)):
        hilbert @talkingmouth "Of course you can't."

    else:
        hilbert @talkingmouth "Of course you didn't."

    pause 1.0

    hilbert @talkingmouth "You can go."

    red @confusedeyebrows frownmouth "Hm?"

    if (IsBefore(1, 5, 2004)):
        hilbert @talkingmouth "I haven't shared my dream with anyone. Ever. Because I knew the instant I did, there would be someone out there trying to stop me. So, that's you, now."
    else:
        hilbert @talkingmouth "The only person I've shared my dream with is Nate. And he's got enough problems that {i}my{/i} dream didn't even phase him."
        hilbert @closedbrow talkingmouth "But you're different. You're kind. You can't just shrug this off, like he can."

    hilbert @talkingmouth "I shouldn't have told you."
    hilbert @sadbrow talkingmouth "You made me trust you. And I resent you for that. Someone with my dream can't afford to trust."

    pause 1.0

    red @sad "...Hilbert."

    hilbert @talkingmouth "Yes."

    red @closedbrow frownmouth "I... can't begin to understand the pain you're going through, but killing isn't the answer."

    hilbert @talkingmouth "Then what is? 'Forgiveness'? 'Living well'?"

    red @closedbrow talking2mouth "Um... I'd try just talking it out with the person you've got a vendetta against."

    hilbert @closedbrow talkingmouth "...Whatever. When you see everything with blackened eyes, the world looks dark. 'Living well' is impossible."

    pause 1.0

    red @talkingmouth "Look, Hilbert, I--"

    hilbert @closedbrow talking2mouth "I'm bored of this conversation. Where did you get that hat?"

    red @confused "Huh?"

    hilbert @talkingmouth "Your hat."

    hilbert @sadbrow talkingmouth "It looks like a first edition Pokémon League Expo hat. It's probably a counterfeit, though, since they were only on for a limited run."
        
    red @happy "Oh, uh... Sam gave it to me. Er, Professor Oak, I mean."

    hilbert @talkingmouth "Can I see it?"

    red @closedbrow talking2mouth "Sure?"

    narrator "You hand over your hat."

    hilbert @talkingmouth "Hm. This is the official seal of the Kantonian Pokémon League."

    "{color=#cf0000}[first_name]{/color}" "\"Huh. Is that valuable?\""

    pause 1.0

    hilbert @talkingmouth "{i}Why{/i} are you hiding underneath the table?"

    "{color=#cf0000}[first_name]{/color}" "\"Oh, just tying my laces.\""

    hilbert @angrybrow talkingmouth "Really? Because it looks to me like you're trying to hide your head."

    "{color=#cf0000}[first_name]{/color}" "\"Nope! I'm not.\""

    pause 1.0

    hilbert @talkingmouth "Whatever. Take the hat back."

    pause 1.0

    red @talkingmouth "Thanks."
    red @closedbrow talking2mouth "...But, really, what was that about?"

    hilbert @talkingmouth "There are exactly seven hundred and forty-eight of those hats in existence. They were manufactured in 2001." 
    hilbert @talkingmouth "They were the last Kantonian League Expo hats ever made." 
    hilbert @talkingmouth "This is because, mid-manufacturing, Lance won his seventeenth attempt at beating the Johto league, and the Kanto League Expo was merged with the Johto League Expo into the Indigo League Expo."

    hilbert @talkingmouth "These hats were given away as novelties at the expo, along with their Johto counterparts, which had finished their production run, and numbered in the thousands."

    pause 1.0

    hilbert @talkingmouth "These hats, mementos of a single, significant moment, that could never be replicated, were just {i}given{/i} away. Alongside the new first edition Indigo League Expo hats, which are now a dime a dozen."

    hilbert @talkingmouth "Of that cancelled run of Kantonian League Expo hats, five hundred and sixteen are in the hands of private collectors. One hundred and two are in museums. Lance owns three, and gave one to Janine." 
    hilbert @closedbrow talkingmouth "And the rest are unaccounted for."

    pause 1.0

    $ PlaySound("idea.ogg")

    red @surprised "Wait. So, what you're telling me is... this hat is {i}really{/i} valuable?"

    hilbert @talkingmouth "It could be."

    show hilbert:
        ease 0.5 ypos 1.2 zoom 1.3

    narrator "Hilbert snatches the hat off your head and gestures at its insides angrily."

    hilbert @angrybrow talkingmouth "If you hadn't {i}soiled{/i} it with your greasy hair, and... and your... dandruff!"

    narrator "Hilbert tosses the hat back to you."

    red @surprised "No, this really matters. Like, how valuable was it, before I used it for ten years?"

    hilbert @closedbrow talking2mouth "Easily $1,500,000."

    red @sad "Oh, no... and how much is it worth now?"

    hilbert @angry "After ten years of use? $70,000 maximum."

    pause 1.0

    red @closedbrow sadmouth tears "Oh... I could have been rich..."

    if (IsBefore(1, 5, 2004)):
        hilbert @talkingmouth "Ugh. I'm actually glad we had this talk. At least now you appreciate your damn hat more. It physically pained me seeing you going to bed every night with it on. You don't even put it on the nightstand or anything."

    else:
        hilbert @talkingmouth "Ugh. I'm actually glad we had this talk. At least now you appreciate your damn hat more. It physically pained me seeing you going to bed every night with it on. You didn't even put it on the nightstand or anything."

    pause 0.5

    if (IsBefore(1, 5, 2004)):
        red @talking2mouth "Hey... do you watch me sleep?"

        hilbert @talkingmouth "I watch everyone in the room sleep. You're not special."

        red @confused "Sorry if this is a dumb question--"

        hilbert @closedbrow talkingmouth "Just don't ask it."

        red @angrybrow talking2mouth "No, I'm going to ask it. Why do you watch us sleep?"

        hilbert @talkingmouth "I'm scared of the dark. Watching you four sleep reminds me that I'm not alone."

    else:
        red @talking2mouth "Hey... did you watch me sleep?"

        hilbert @talkingmouth "I watched everyone in that room sleep. You're not special."

        red @confused "Sorry if this is a dumb question--"

        hilbert @closedbrow talkingmouth "Just don't ask it."

        red @angrybrow talking2mouth "No, I'm going to ask it. Why did you watch us sleep?"

        hilbert @talkingmouth "I'm scared of the dark. Watching you four sleep reminded me that I'm not alone."
        hilbert @talkingmouth "I do the same thing in my new dorm."

    pause 1.0

    red @surprised "What?"

    hilbert @angry "What is {i}wrong{/i} with your ears?"

    red @talking2mouth "Is that, like, really dry sarcasm?"

    hilbert @sadbrow talkingmouth "You mean the lowest form of wit? No, it's not."

    pause 1.0

    hilbert @talkingmouth "Tch. This whole conversation has been a waste of time. And now I've forgotten why I even came to Inspira in the first place."

    red @talkingmouth "...I think I know."

    hilbert @talkingmouth "Then keep it to yourself."

    pause 1.0

    red @talkingmouth "You're serious about wanting to kill the one responsible for your parents' death?"

    hilbert @talkingmouth "I would die for it. Attendance at Kobukan just gives me the power and resources I need to make it happen."

    pause 1.0

    red @closedbrow talking2mouth "I can't let that happen. For your safety."

    hilbert "{w=0.5}.{w=0.5}.{w=0.5}."

    red @talkingmouth "...But I'll help you find the one responsible, if you can tell me about them."

    hilbert @talkingmouth "I accept your help."

    red @surprised "Woah. That easily?"

    if (IsBefore(1, 5, 2004)):
        hilbert @talkingmouth "I'm not in any position to be turning down offers of aid. Besides, you're... {w=0.5}competent. I would welcome your aid as my... compatriot."

    else:
        hilbert @sadbrow talkingmouth "Your power affords you... communicative ability. I'm not in any position to be turning down people who can provide that. Besides, you're... {w=0.5}competent. I would welcome your aid as my... compatriot."

    red @talkingmouth "That's{w=0.5}.{w=0.5}.{w=0.5}.{nw}"

    hide hilbert with dis

    extend @surprised " Oh, he just walked away."

    pause 0.5 

    red @talkingmouth "Well, I don't much like the sound of 'compatriot.'"
    red @closedbrow talking2mouth "Before I go back to campus, I should probably swing by a store. I think I can think of a little present Hilbert might appreciate."

    pause 2.0

    show silver surprisedbrow at night with dis

    pause 2.0

    silver @talkingmouth "What the fuck...?"

    scene black with Dissolve(2.0)

    narrator "When Hilbert returns to his room later, he finds a little box on his nightstand. Opening the box, he sees a small, Vanillite-shaped object."

    if (IsBefore(1, 5, 2004)):
        narrator "Turning it over, its form and function becomes apparent. It's a nightlight. Hilbert wordlessly plugs it in, nodding his thanks at you."

        pause 0.5

        narrator "In the dim light, you think you can see traces of a smile. It seems he appreciates his {color=#0048ff}light{/color}."

        pause 0.5

        narrator "Whatever the case, Hilbert's behavior certainly becomes more tolerable, raising the morale of everyone in the room."

    else:
        narrator "Turning it over, its form and function becomes apparent. It's a nightlight. Hilbert wordlessly plugs it in."

        pause 0.5

        narrator "Were you there, in the dim light, you may be able to make out traces of a smile. It seems he appreciates his {color=#0048ff}light{/color}."

        pause 0.5

        narrator "Whatever the case, Hilbert's behavior certainly becomes more tolerable, raising the morale of all his dormmates."

    if (IsBefore(1, 5, 2004)):
        $ ValueChange("Calem", 1, 0.25, False)
        $ ValueChange("Ethan", 1, 0.5, False)
        $ ValueChange("Brendan", 1, 0.75)
    else:
        $ ValueChange("Bea", 1, 0.2, False)
        $ ValueChange("Nate", 1, 0.4, False)
        $ ValueChange("Hilda", 1, 0.6, False)
        $ ValueChange("Bianca", 1, 0.8)

    $ RelationshipRankUp("Hilbert", "Light", 1)

    return

label Hilbert2:
    scene stadium_empty
    with Dissolve(2.0)
    stop music fadeout 1.5
    show screen songsplash("Victory Road", "Zame")
    queue music "audio/music/victory_start.ogg" noloop
    queue music "audio/music/victory_loop.ogg"

    narrator "You'd been idly relaxing in your room, texting random friends when you suddenly received a text."
    narrator "'Come to the Battle Hall now. Alone. -HvS.'"
    narrator "You made your way to the Battle Hall, gently asking some students who were using the Battle Hall to depart. They assumed it was Battle Team business, and ran off without a word of protest."
    if (not persondex["Hilbert"]["Contact"]):
        narrator "Though it was a new number, you figured there was only one person 'HvS' could be."

    show hilbert with dis

    redmind @closedbrow frownmouth "'Hilbert von Schwarzdrachen.'"

    if (not persondex["Hilbert"]["Contact"]):
        $ BecomeContacted("Hilbert")

    hilbert @talkingmouth "You're here early."

    red @talkingmouth "I came as soon as I heard."
    
    pause 0.5

    red @talkingmouth "Wait, are you {i}sweating?{/i}"

    hilbert @closedbrow talkingmouth "I... ran here, yes."
    
    red @happy "Hey, that's new! Good job!"

    hilbert surprisedbrow @closedbrow talkingmouth "Thanks."

    pause 0.5

    hilbert @closedbrow talkingmouth "{size=30}'Thanks'? Since when do I say 'thanks'?{/size}"
    hilbert -surprisedbrow @sadbrow talkingmouth "That was odd. Let's ignore that."

    red @happy "Aight."

    hilbert @talkingmouth "I've asked you to come here for a very specific reason."

    if (HasEvent("Hilbert", "FerrisWheel")):
        red @talking2mouth "Right. On the Ferris Wheel, you said that you thought the second part of your mission was, uh, about to happen, right?"

        hilbert @closedbrow talkingmouth "Good, you remember. That's right."

    else:
        red @talkingmouth "I'm ready to hear it."

        hilbert @talkingmouth "...[first_name], there is something I must confess to you."

        pause 1.0

        hilbert @talkingmouth "I am the king of Team Plasma."

        pause 3.0

        red @surprised "What?"

        hilbert surprised @closedbrow talkingmouth "You're probably surprised. It's because--"

        red @talkingmouth sweat "N-no, I just, uh, [pika_name] was chewing on my ear. What did you just say?"

        hilbert -surprisedbrow -frownmouth -surprised @surprised "Oh."
        hilbert @closedbrow talking2mouth "I said 'I am going to kill the king of Team Plasma.'"

        red @unamusedbrow unamusedmouth "...Okay, I guess I didn't mishear you this time."

        hilbert @talkingmouth "As I was saying. You're probably surprised. It's because the king of Team Plasma is responsible for my parents' deaths."

        red @talkingmouth "I thought you said... it was the dragon of the meteor?"

        hilbert @closedbrow talkingmouth "Every king needs a sword. As I said, the dragon will fall, then the king will die."

        $ PlaySound("Pokemon/pikachu_happy3.ogg")
        libpikachu @happy "Pi-i-i-ka!"

        red @sweat talking2mouth "{size=30}Not the time, bud.{/size}"

        pause 1.0

        if (GetRelationshipRank("Hilda") < 2):
            red @confused "What's Team Plasma?"

            hilbert @talkingmouth "My enemy. That's all you need to know."

        red @sadbrow talking2mouth "Well... I'm glad you're telling me this. But {i}why{/i} are you telling me this?"

        hilbert @talkingmouth "You insisted on being part of my mission. I believe the second part is coming up... very soon."

        redmind @sadbrow frownmouth "Shit. I thought I had more time to talk him out of this."

        hilbert @sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."
        hilbert @talkingmouth "I will continue to appreciate your support."

        pause 0.5

        red @sad "Well... what's next?"

    hilbert @closedbrow talkingmouth "There's something that's always bothered me about my parents' death. I seek to resolve that oddity today."

    narrator "You know that Hilbert's waiting for you to ask for elaboration."
    narrator "However, you also know that if you don't ask for elaboration, Hilbert won't be able to stop explaining himself anyway."

    hilbert @closedbrow talkingmouth "They were killed by... {i}ugh.{/i} A cannon."

    red @confused "A cannon?"

    hilbert @talkingmouth "It's a form of weapon. Last used four hundred years ago, during the Ransei period."
    hilbert @sadbrow talkingmouth "Until a decade ago, of course."

    red @talking2mouth "No, sure, I know what cannons are, in concept. I mean, Blastoise has them. Zap Cannon, Flash Cannon, sure."
    red @closedbrow talking2mouth "But... what's a {i}human{/i} cannon?"

    hilbert @sadbrow talkingmouth "Machines. They're devices created to kill."

    red @surprised "Like a sword?"

    hilbert @angrybrow angrymouth "You're so naive. People use swords at the {i}Pokéathlon.{/i} For sport. {i}Entertainment.{/i}"
    hilbert @closedbrow talkingmouth "This 'cannon' can't do anything {i}but{/i} kill."

    red @sadbrow talking2mouth "...I don't like thinking that such a thing could exist."

    hilbert @closedbrow talkingmouth "Most people don't."

    pause 0.5

    hilbert @sadbrow talkingmouth "Know it exists, I mean. And... I'm sorry I've told you about it."

    pause 0.5

    hilbert @closedbrow talkingmouth "If you want to stop this mission, now's the time. You'll only learn more you wish you hadn't."

    red @talking2mouth "If you already knew, then... I'm in this for the long haul."

    hilbert @closedbrow smilemouth "Hm."

    red @confused "Did you just smile?"

    hilbert @angrybrow talkingmouth "Absolutely not."

    red @closedbrow talking2mouth sweat "Alright. Trick of the light, I guess."

    hilbert @closedbrow talkingmouth "I need to do further research on this 'cannon'. There aren't many people who know they exist--nevermind how to make one."
    hilbert @talkingmouth closedbrow "If I can determine that, then I can narrow down who the King of Team Plasma is. And if I can figure that out... I know who my target is."

    if (GetRelationshipRank("Hilda") >= 2):
        red @talking2mouth "I heard that Team Plasma's airship attacked Opelucid. I guess that aircraft had these 'cannons' on it...?"

        hilbert @closedbrow talking2mouth "That's correct. The cannons that destroyed my home."

    else:
        red @talking2mouth "I'm not seeing the connection."

        hilbert @closedbrow talkingmouth "Team Plasma's ship had the cannons on it. The cannons that destroyed my home."

        red @sadbrow sadmouth "Oh."

    pause 1.0

    red @talking2mouth "Well, if we need to do research, then we should go to the library, right?"

    hilbert @talkingmouth "Yes. But not the school's library. They wouldn't have access to books on such topics."

    red @unamusedbrow unamusedmouth "{w=0.5}.{w=0.5}.{w=0.5}."
    red @unamusedbrow talking2mouth "I'm not going to ask, so just say it."

    hilbert @talkingmouth "There's a library in Inspira."

    red @confused "A... {i}public{/i} library? That has information about thousand-year-old weapons?"

    hilbert @talkingmouth "A shining showcase of the naivete of the Kobukan region. It's not like they could store those important historical books on a military base, or anything of that sort."
    hilbert @closedbrow talkingmouth "Kobukan doesn't even have a military."

    red @sadbrow talkingmouth "I guess, since Kobukan's always been a peaceful nation--"

    show hilbert angrybrow angrymouth:
        ypos 1.0 zoom 1.0
        ease 0.5 ypos 1.1 zoom 1.2
    show stadium_empty 
    with vpunch

    hilbert @angrymouth "No! That's wrong!"
    hilbert -angrymouth @closedbrow angrymouth "Kobukan isn't peaceful. It's {i}harmless.{/i} It couldn't fight for anything if it wanted to. This region is an embarrassment to humanity--it grows fat off the sacrifices of Unova."
    hilbert @talkingmouth "If the kind of tragedy that befell Unova came to Kobukan, who would stop it?"

    pause 1.0

    show hilbert sadbrow with dis

    red @talking2mouth "The students of Kobukan Academy."

    pause 0.5

    hilbert @talkingmouth "Children shouldn't have to fight."

    red @talkingmouth "Hilbert, you're basically a kid yourself."

    hilbert @closedbrow talkingmouth "Who did you think I was talking about?"

    pause 1.0

    red @closedbrow talking2mouth "...Alright. Are they just going to let us in? I mean, if these books talk about ways to, like, {i}kill{/i} people, then, they've got to be restricted, right?"
    
    hilbert @talkingmouth "There are secrets all around this region laid out in plain sight. Being within the pages of a book is one of the better camouflages."

    pause 0.5

    hilbert -sadbrow @closedbrow talkingmouth "After all, it's not like Kobukan students have the time to read anything outside of our assigned readings. And I can't imagine anyone else having the curiosity to plumb the library's secrets."

    red @closedbrow talking2mouth "Alright. Let's go, then."

    scene blank2 with splitfade

    narrator "This time, Hilbert leads {i}you{/i} through the streets of Inspira, until you arrive at a tall, boxy, building you've never seen before."
    narrator "A plaque outside the front door designates it the 'Gray Library for the Public.'"

    hilbert @talkingmouth "In case we are confronted, follow my lead. I understand you cannot lie, so I won't ask you to."

    redmind @frownmouth sadbrow "What if we actually find something that helps Hilbert with his mission, though...?"

    red @talkingmouth sadbrow "You know, we don't have to do this now. We could come back another day."

    narrator "Hilbert takes a big gulp of air, and you notice with some surprise that his hands are shaking."

    hilbert @talkingmouth "...I cannot give myself the time necessary to lose my nerve."

    $ PlaySound("Door_Slam.ogg")

    narrator "Saying so, Hilbert steps through the door, slamming it open."

    stop music

    $ renpy.music.queue("Audio/Music/DragonDenStart_B.ogg", channel='music', loop=False, fadein=1.0, tight=None)
    $ renpy.music.queue("Audio/Music/DragonDenLoop.ogg", channel='music', loop=True, fadein=0.0, tight=None)

    scene blank with splitfadefast

    pause 0.3

    scene graylibrary with splitfade

    narrator "The first thing that hits you is that this library has an oppressively gray color palette. The air conditioning, too, is on full blast, and it's extremely chilly, like stepping into a freezer." 
    narrator "You realize with a start that you can actually see your own breath."

    hilbert @talkingmouth "We're looking for history books. Military history, preferably. About technology used during the Greatest War."

    redmind @closebrow frownmouth "Subtle as a brick to the face."

    narrator "The librarian sitting behind the front desk is entirely unphased, though."

    show hilbert surprisedbrow with dis

    stop music fadeout 3.5

    Character("Librarian") "\"Of course. That's section 944, History of Kalos.\""
    Character("Librarian") "\"Though if you're more interested in specifically the military technology aspect of things, section 355 is Military science. You might also want to check section 623, which is Military and nautical engineering.\""

    hilbert @talkingmouth "Oh."

    pause 1.0

    hilbert -surprisedbrow @closedbrow talkingmouth "Thank you."

    pause 1.0

    show screen songsplash("Victory Road", "Zame")
    queue music "audio/music/victory_start.ogg" noloop
    queue music "audio/music/victory_loop.ogg"

    red @confused "You alright?"

    hilbert @sadbrow talkingmouth "I didn't expect it to be so easy. I feel like I should have to fight more for this."

    red @talkingmouth "Don't lead a gift horse to water, Hilbert."
    red @sweat talking2mouth "Besides, there's {i}plenty{/i} of time for things to go wrong."

    hilbert @talkingmouth closedbrow "True."

    pause 1.0

    hilbert @talkingmouth "Alright. Let's split up."

    red @confused "I didn't know we were dating?"

    hilbert @closedbrow talkingmouth "You are {i}persistently{/i} gay."

    red @happy "Haven't stopped yet."

    hilbert @talkingmouth "{i}As I was saying{/i}, we should split up. I'll cover sections 355 and 623, as they seem more specialized, and therefore easier to read through."
    hilbert @closedbrow talking2mouth "You go to section 944."

    red @confused "The history of Kalos is a pretty huge topic to research. I mean, it's a big region."

    hilbert @closedbrow talkingmouth "Just focus on the time period 3,000 years ago. Any descriptions of the Greatest War may contain details as to how this ancient weaponry had re-emerged in the modern era."

    red @talking2mouth "Alright."

    pause 0.5

    scene blank2 with splitfade

    pause 1.0

    show waytoolonglater at vspaz

    pause 3.5

    scene graylibraryrestricted with splitfade

    pause 1.0

    red @unamusedbrow unamusedmouth "...I'd be bored to tears if I wasn't so horrified of what I was reading."

    narrator "You're currently poring over a massive leather-bound tome called L'Encyclopédie de Kalos."
    narrator "It does, in fact, contain information about the Greatest War, and even about these 'cannons' that Hilbert had mentioned."
    narrator "Yet, the prose is so purple it profoundly precludes any precise perception of the particulars presented."

    red @closedbrow sweat talking2mouth "Great, I'm so far gone I've started alliterating."

    Character("Librarian") "\"Shh!\""

    red @sweat talking2mouth "{size=30}Sorry, Miss.{/size}"

    narrator "You sigh, and return your gaze to the book."

    Character("L'Encyclopédie") "{size=20}The Greatest War was fought approximately 3,000 years ago, notable for being the first and last war fought utilizing the most mortal of instruments, of which there is no greater example than that of which we dare not speak, and as such shall not be addressed, for mankind's kindness; ought to be mentioned, too, are the many myriad of lesser mortal instruments which were bevied and laid upon each other in ultimate conflict; among their number for defense were armor and shields, while offense begat--and forgive us for writing these words, generations of the future--{b}cannons{/b} and shot, as in similarity with the arquebus wielded so brutally in the Ransei Period.{/size}"

    narrator "Though difficult to parse, you're getting the idea that wars in the past were fought not with the intent of capturing opponents and forcing surrender, but of actually {i}killing{/i} the enemy army."
    narrator "A chill runs up your spine."

    redmind @sadbrow frownmouth "That's awful. I can't believe that people used to do this to each other."

    narrator "The Encyclopédie goes on to elaborate that these weapons were used against Pokémon, too. Some Pokémon even {i}used{/i} the weapons in question."

    redmind @closedbrow frownmouth "I can't believe Pokémon would do that. But... I can't really believe that humans would do it, either..."

    narrator "All you've been able to gather from the encyclopedia, after hours of research, is that the world used to be a much more deadly place." 
    narrator "It's also apparent that--true to Hilbert's supposition--most people do not remember that such weapons even exist."
    
    redmind @thinking "So whoever built these cannons for Team Plasma must have had some sort of connection to their history. Maybe a Kalosian?" 
    redmind @thinking "But I'm a kid from Kanto, and I know about them, now... I guess anyone with the blueprints could build 'em, and it doesn't take much to learn about them, either."
    redmind @sadbrow frownmouth "I mean, anyone who ever held this book could be the mastermind. I'm not an engineer, but from how they describe cannons, it seems pretty easy to figure out. I bet Hilbert's sections will tell him how they actually worked, even."

    pause 1.0

    narrator "You're about to put the book back on the shelf and return in defeat when you suddenly remember something Hilbert said one of the first few days you knew him."

    show dorm_A at sepia
    show flashback
    with dis

    $ renpy.pause(1.0, hard=True)
    
    show ethan uniform at centerside, sepia behind flashback with dis
    show calem uniform at leftside, sepia behind flashback with dis
    show brendan uniform at rightside, sepia behind flashback with dis

    red sepia "Hey, guys, focus up. Did anyone notice what time I went to bed last night?"

    ethan @closedbrow talking2mouth "What, like we'd watch you sleep? Nah, man."

    pause 2.0

    show ethan surprisedbrow frownmouth with dis:
        xpos 0.5
        ease 0.5 xpos 0.6
    show brendan surprisedbrow frownmouth with dis:
        xpos 0.75
        ease 0.5 xpos 0.8
    show calem surprisedbrow frownmouth with dis:
        xpos 0.25
        ease 0.5 xpos 0.4
    show hilbert uniform at sepia behind flashback:
        xpos -0.2 xzoom -1
        ease 0.5 xpos 0.2

    hilbert @talkingmouth "1:12. In the morning, obviously."

    pause 1.5

    hilbert @surprised "What?"
    hilbert @angry "You all are just unobservant."

    show ethan surprisedbrow frownmouth with dis:
        xpos 0.6
        ease 0.5 xpos 0.5
    show brendan surprisedbrow frownmouth with dis:
        xpos 0.8
        ease 0.5 xpos 0.75
    show calem surprisedbrow frownmouth with dis:
        xpos 0.4
        ease 0.5 xpos 0.25
    show hilbert at sepia:
        xpos 0.2
        ease 0.5 xpos 1.2

    pause 1.0

    $ PlaySound("door_slam.ogg")

    pause 1.0

    show ethan -surprisedbrow -frownmouth -surprised 
    show brendan -surprisedbrow -frownmouth -surprised
    with dis

    calem closedbrow talking2mouth "If he keeps slamming that door, we're going to have to pay to repair it..."

    pause 0.5

    show blank with splitfade

    pause 1.0

    hide ethan
    hide brendan
    hide calem
    hide hilbert
    hide dorm_A
    hide flashback
    hide blank with dis

    redmind -sepia @angrybrow frownmouth "Unobservant, huh...?"

    narrator "Your eyes narrow as you scan the pages one more time."
    narrator "Slowly, oddities begin to appear--little things you wouldn't have noticed before."

    redmind @frownmouth "Someone dog-eared this page. So... that means someone else has been looking at this book."
    redmind @confusedeyebrows frownmouth "Of course, that doesn't mean anything by itself, but this book was pretty dust-free when I took it down."
    redmind @frownmouth "But this entire section is dusty. It doesn't seem like the books have been touched in a while, besides this one..."
    redmind @frownmouth "In the margins, here, there are notes scribbled in pencil... three-digit codes. Other sections of the library, maybe?"
    redmind @surprisedbrow frownmouth "I recognize these numbers... 355 and 623. They're the other sections the librarian told us to go to!"
    redmind @thinking "So someone was doing the same sort of research we are now."
    redmind @thinking "Who...?"

    pause 0.5

    red @talkingmouth "{size=30}Excuse me, Ma'am?{/size}"

    Character("Librarian") "\"Hm?\"" 

    red @talkingmouth "This book--is there any way I could see who checked it out?"

    Character("Librarian") "\"Oh, L'Encyclopédie de Kalos? I'm sorry, no. We don't allow our encyclopedias to be checked out. They're historical, you see. {i}That{/i} one was owned by André Stendahl himself!\""
    Character("Librarian") "\"You're always welcome to come here and use them for research, though.\""

    narrator "The librarian pauses and looks at the book with a curious expression."

    Character("Librarian") "\"Though... it {i}is{/i} interesting that you have an interest in {i}that{/i} book in particular.\""

    red @happy sweat "I just picked the biggest one off the shelf."

    Character("Librarian") "\"Ohoho! I'm pretty sure that was the reasoning of the last person who found it, too.\""

    $ PlaySound("idea.ogg")

    red @surprised "Ma'am, do you remember who it was?"

    Character("Librarian") "\"Oh? So intense. No, I'm afraid not. I never got his name. He was a young man, though. About your age. Perhaps a Kobukan student.\""

    red @talkingmouth "Ma'am. Please. I need you to tell me anything you can about him. What did he look like? What was he wearing? Did he say anything? Did he check anything else out?"

    Character("Librarian") "\"I... I'm sorry, I don't think I should share that.\""

    show hilbert with dis:
        xpos 0.66

    hilbert @talkingmouth "Why not?"

    redmind @surprised "Whoa, where did he come from? How long had he been listening?"

    Character("Librarian") "\"I'm sorry. Who are you?\""

    hilbert @closedbrow talkingmouth "Unimportant."
    hilbert @angrybrow angrymouth "What {i}is{/i} important is that we need to find the criminal who did this!"

    Character("Librarian") "\"Cr-cr-criminal?! I'm sorry, I think this is all quite a bit above my head, and I should ask you to leave--\""

    narrator "Hilbert points at the book with righteous fury in his eyes."

    hilbert @talkingmouth "Don't shy away from the truth! Look at that massacre with your own eyes!"

    Character("Librarian") "\"What? What do you--\""

    show graylibraryrestricted with vpunch

    Character("Librarian") "\"{size=40}OH MY GOD!{/size}\""

    red @surprised "What?! What is it?!"

    Character("Librarian") "\"Dog ears... pencil markings... ! This book was owned by André Stendhal himself!\""

    hilbert angry "He would be rolling in his grave right now!"

    Character("Librarian") "\"Soiled it! Ruined it! Desecrated it! I'll ruin that young man! I'll absolutely demolish him!\""

    hilbert "Don't you want {i}revenge{/i}? Don't you want {i}justice{/i}?!"

    Character("Librarian") "\"I want retribution! I want reparations! I want blood! I'll have his {i}grandchildren's{/i} library cards revoked!\""

    hilbert surprised @angry "Tell us everything you know. We'll tie him up a smidgeon on the tight side and throw him in the book return box {i}for{/i} you."

    Character("Librarian") "\"Ooooh... that spiky-haired punk... with his puns and his visor and his charm... when I get my hands on him...!\""

    redmind @thinking "Spiky hair... Puns... visor? Really only one person it could be..."

    if (GetRelationshipRank("Nate") > 0):
        red @talkingmouth "We must be on the right track, if we're researching something Nate already researched."

    narrator "Hilbert takes a moment to compose himself."

    hilbert -surprisedbrow -frownmouth -surprised @closedbrow talkingmouth "I know who you're talking about."
    hilbert @talkingmouth "We'll find him for you."

    narrator "Hilbert looks at you, then pointedly jerks his head towards the exit, walking away."

    Character("Librarian") "\"Wait... you know? But I didn't even say anything yet!\""

    red @closedbrow talking2mouth "'Scuse me, Ma'am. {size=30}Sorry about your book.{/size}"

    scene blank2 with splitfade

    pause 1.0

    show city_A
    show hilbert
    with splitfade

    pause 1.0

    narrator "You and Hilbert are headed back to campus. Hilbert is hanging his head, his brow furrowed in thought."

    red @talking2mouth "What was that?"

    hilbert @surprisedbrow talking2mouth "Hm?"

    red @happy "That librarian. You knew exactly what to say. I thought you said you were bad with people?"

    hilbert @closedbrow talkingmouth "You call that 'good with people'? I made her furious."

    red @talkingmouth "We got what we wanted."

    hilbert @sadbrow talkingmouth "[ellipses]"
    hilbert @sadbrow talkingmouth "I lied."

    red @closedbrow talking2mouth "Yeah, I figured we weren't {i}actually{/i} going to jump on and tie up Nate."

    pause 0.5

    hilbert @talkingmouth "From my reading, I learned some interesting information about the cannons of the before time."
    hilbert @closedbrow talkingmouth "They relied on the energy of a Pokémon."
    hilbert @talkingmouth "A powerful Fire-type could fuel a cannon that shot fire. A powerful Electric-type could fuel a lightning-shooting cannon."
    hilbert @closedbrow talkingmouth "And a powerful Ice-type could fuel a cannon that shoots ice."

    pause 0.5

    hilbert @talkingmouth "I have no doubt now the cause of all my strife. The dragon of the meteor. Kyurem. It was said to have incredible control over ice, and a taste for human flesh."
    hilbert @closedbrow talkingmouth "A beast like that probably didn't even need to be coerced into killing. I bet it's second nature for that monster."

    red @talking2mouth "Pokémon are good."

    hilbert @angrybrow talkingmouth "Is a sword good? Only when wielded by a good man. The sword of an evil man is a tool that must be destroyed."

    red @closedbrow talking2mouth "...It's a legendary Pokémon. You said Team Plasma attacked your home. How could Team Plasma capture... I mean, legendary Pokémon are basically gods, right?"

    hilbert @sadbrow talkingmouth "A Pokémon, even if revered as a deity, is still just a Pokémon."

    pause 0.5

    hilbert @talkingmouth "We need to talk to Nate. He's clearly following the same path we are. He's been frustratingly slow with the information he's giving me--perhaps the information we've learned will remind him of his priorities."
    hilbert @closedbrow smilemouth "Hmph."
    hilbert @talkingmouth "I'm getting closer."

    pause 1.0

    narrator "You're suddenly reminded of the conversation you had with Hilda about Hilbert's dream, and you can't help but wish that she was in your place right now."

    $ ValueChange("Hilda", 3, 0.25)

    narrator "Your understanding of Hilda has increased!"

    pause 1.0

    show hilbert surprisedbrow with dis

    red @talking2mouth "What about Hilda?"

    hilbert @talkingmouth "What?"

    red @talking2mouth "I know you don't plan to survive this plan of yours. Either you'll die or you'll go to prison for life."

    hilbert -surprisedbrow @closedbrow talkingmouth "So what?"

    red @talking2mouth "Hasn't Hilda spent over a decade taking care of you? Helping you get to this point? Looking after you? Being your friend?"

    hilbert @talkingmouth "Yes. You know all this."

    red @talking2mouth "Then are you really going to let all that go to waste? She's always believed you'll make it through. She wouldn't put so much effort towards you if she didn't."

    pause 0.5

    hilbert @sadbrow talkingmouth "Her... choices were her own..."

    pause 0.5

    hilbert @closedbrow talkingmouth "And I'm a burden on her, anyway. After the momentary grief, she'll be glad of my absence. She can return to the life she had before."

    red @talking2mouth "Are you 'over' your parents?"

    hilbert @angry "Yes."

    pause 1.0

    red @sad "Hilbert, you're planning to die for them."

    hilbert @closedbrow talkingmouth "This is not an emotional decision. This is based on logic, and reason, and... and... the calculus of justice."

    red @closedbrow talking2mouth "And Hilda doesn't fit into this equation. You'll disappear and leave her alone, with nothing to show for the years she spent with you."

    hilbert @sadbrow talkingmouth "...She will not be alone. Her father is a good, honest, man. And..."

    narrator "Hilbert looks at you curiously."

    hilbert @closedbrow talkingmouth "Well, she'll have you. You are good at helping people through their grief."

    red @talking2mouth unamusedbrow "If that were true, you wouldn't be trying to kill a god and a king."

    hilbert @closedbrow talkingmouth "If it {i}weren't{/i} true, I would have succeeded by now."

    pause 0.5

    red @confused "I don't follow."

    hilbert @closedbrow talkingmouth "I could have done this mission myself. I just needed to go to the library."
    hilbert @sadbrow talkingmouth "But... for some, odd, reason... I went with you."
    hilbert @closedbrow talkingmouth "This took time. Time I did not have. Your schedule is too full."

    pause 0.5

    hilbert @talkingmouth "I will leave a lot unfinished. A lot unsaid. Apologies... undelivered."
    hilbert @sadbrow talkingmouth "I wish there was some way to repay Hilda for everything she has given me. Her patience, her trust, and her help. But I... I know that an appropriate amount of repayment cannot be acquired in my lifetime."
    hilbert @closedbrow talkingmouth "You have shown me the way with your light. I now trust in you to [bluecolor]finish{/color} what I cannot. Especially in regards to Hilda."

    red @sad "That's... an insane amount of pressure."

    hilbert @sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."
    hilbert @talkingmouth "Then your first job when my part is over will be to apologize to yourself on my behalf."

    $ RelationshipRankUp("Hilbert", "Finisher", 2)

    return