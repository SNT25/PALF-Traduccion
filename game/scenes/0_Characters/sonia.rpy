label Sonia1:
    if (not IsBefore(1, 5, 2004)):
        $ persondex["Sonia"]["Events"].append("Level2SceneVer2")

    scene research
    show sonia at rightside
    show nessa at leftside:
        xzoom -1
    with Dissolve(2.0)
    show screen songsplash("Sonia's Theme", "Syntthetix")
    stop music fadeout 1.5
    queue music "audio/music/sonia_start.ogg" noloop 
    queue music "audio/music/sonia_loop.ogg"

    narrator "You aimlessly walk into the Research Center, possibly to talk with Professor Oak, when you see Sonia and Nessa talking."

    sonia @happy "And the best part, Ness, is I feel like I'm {i}really{/i} succeeding this time!"

    if (IsBefore(4, 10, 2004)):
        nessa @talkingmouth "Don't get too far ahead of yourself. We're not even halfway through the year yet."

    else:
        nessa @talkingmouth "Yeah. I think you are. You made it more than halfway, which was always a sticking point for you, right? Good job."

    pause 0.5

    nessa @surprised "Oh. [first_name]?"

    red @happy "Hey-o. Hope I'm not interrupting anything."

    if (not HasEvent("Nessa", "DenyDate")):
        nessa @talkingmouth "Nah. Sunny, remember that guy I told you about? The one who took me on a date to a pit in the middle of the fields?"
    else:
        nessa @talkingmouth "Nah. Sunny, remember that guy I told you about? The one who turned me down, then took me to a pit in the middle of the fields?"

    sonia @surprised "No, really?"

    nessa @happy "Yeah, it was this guy."

    if (not IsBefore(1, 5, 2004)):
        if (not HasEvent("Nessa", "DenyDate")):
            sonia @surprisedbrow happymouth "...You might've mentioned that your date was my teammate--the one that Cheren said had mind control, to boot."
        else:
            sonia @surprisedbrow happymouth "...You might've mentioned that your friend was my teammate--the one that Cheren said had mind control, to boot."

        nessa @closedbrow talkingmouth "...Yeah, well, I didn't."

    if (not HasEvent("Nessa", "DenyDate")):
        sonia @happy "Well, I'm very happy to see you've found someone, Ness."

        nessa @closedbrow talkingmouth "Slow down there. It's just a casual thing."

        sonia @sadbrow happymouth "Oh. There I go, rushing into assumptions again."

    red @happy "We pretty much just talked about you, actually, Sonia."

    nessa @surprised "You didn't need to say that."

    sonia @surprisedbrow happymouth "Only good things, I hope?"

    show nessa surprisedbrow frownmouth with dis

    red @talkingmouth "Yeah. Nessa cares a lot about you."

    nessa -surprisedbrow @closedbrow talkingmouth "Okay, [first_name], that's enough."

    red @happy "Oops!"

    nessa @closedbrow talkingmouth "I need to go prep some stuff for science club. See you lat--"

    sonia @surprisedbrow happymouth "Wait, {i}science{/i} club?"

    nessa @talkingmouth "Yeah. It's a blow-off club. We mostly just sit around and study rocks. But it's a good place to hang out and kill time."

    sonia @sadbrow talking2mouth "Ness, you know how I feel about geologists..."

    red @confused "Um, sorry, what? Is there some sort of geologist-based tragic backstory I'm not privy to, here?"

    nessa closedbrow happymouth "It's a fun story. Tell him, Sunny. Give him a test run for me."

    $ ValueChange("Nessa", 3, 0.25)

    nessa @talkingmouth "Good seeing you, [first_name]."

    hide nessa with dis

    pause 1.0

    redmind @confusedeyebrows frownmouth "Test run?"

    show sonia:
        ease 0.5 xpos 0.5

    pause 0.5

    sonia @talkingmouth "Don't mind Ness. It's just a running joke we used to have."

    red @closedbrow talking2mouth "A joke... between the Galarian Stars, right?"

    sonia @surprised "Oh, she told you about us?"
    sonia @talkingmouth "Yes, that's right. She, um, she had a lot of suitors back in Galar."

    pause 0.5

    sonia @closedbrow talkingmouth "Well, to call them suitors might be too polite a term, given their intentions."
    sonia @sadbrow happymouth "They knew she would turn them down... so then they'd, erm, make their intentions clear. {w=0.5}To me."
    sonia @sad "Given my lower standards, I'd usually accept, we'd date for a few months, and then... well, usually the relationship would end when they realized that dating me didn't get them any closer to Ness."

    red @confused "Geez.{w=0.5} That's awful. I'm sorry, Sonia."

    sonia @talkingmouth "Well, it happened so often, that Raihan started making jokes about how I was, like, Nessa's 'boyfriend secretary.' That I was giving them 'test runs' for her."

    red @surprised "Eesh. That seems a bit... hurtful, I guess?"

    sonia @closedbrow talking2mouth "Right, it wasn't fantastic."
    sonia @sadbrow happymouth "But I'm over that now."
    sonia @sad "I've got... {i}so much{/i} else to worry about... it barely even registers, honest."

    red @thonk "{w=0.5}.{w=0.5}.{w=0.5}."

    sonia @happy "Ah, sorry. You probably don't want to hear my dull complaints."

    red @talkingmouth "Hey, it's fine. I'm actually really interested in hearing what your vendetta against geologists is."
    red @confused "Seems kinda weird, so there must be a good reason, right?"

    sonia @talkingmouth "Well, I can't quite say if it's a good one, but, yes, I've got a bit of a history with geologists."

    red @closedbrow talking2mouth "...Lay it on me."

    sonia @talkingmouth "Have you ever heard of 'Wishing Stars'?"

    red @talkingmouth "Yeah. They're, um, rocks that fall semi-frequently in Galar, right? And they're part of what powers the Dynamax phenomenon there."

    sonia @closedbrow talking2mouth "Mostly right. What you just described was pretty much everything everyone in Galar knew about the Wishing Stars for... hundreds of years. And they'd been falling for {i}thousands{/i} before."

    sonia @talking2mouth "Well, my Gran made it her life's work to investigate them properly. I helped. And we actually figured out something incredible, something that hundreds of years of past research hadn't shown up."

    pause 1.0

    sonia @sad "They're... not actually rocks."

    pause 0.5

    red @closedbrow talking2mouth "Ah. I think I can see where this is going."

    sonia @happy "It does rather lay itself out, doesn't it? Yes, they're not rocks at all. Instead, they're parts of a super-ancient Pokémon, or otherwise definitively 'organic' entity."
    sonia @surprised "Now, in total fairness, this entity's body is composed of a calcite-like mineralistic keratin which can be very easily mistaken for a rock, and definitely had, for hundreds of years."

    redmind "Hm. She's cute when she's talking about something she's passionate about."

    sonia @talking2mouth "But by analyzing the fragments of biological material still attached to the core of the Wishing Star, those trace fragments that survived the exosphere and impact with Earth--"
    sonia @talkingmouth "I was able to determine that the Wishing Stars were, without a shadow of a doubt, organic."

    pause 1.0

    red @talking2mouth "Which made all the geologists in Galar hate you."

    sonia @sad "Astrogeologists mainly, but... yes."

    red @happy "What about the biologists, though?"

    sonia @talking2mouth "Well, Gran and I did get a few letters from them thanking us for it. But the hatemail we got from those bloody rock nerds quite outstripped the former."

    red @surprised "Jeez! I guess they were passionate about their field."

    sonia @talking2mouth "If I had a pound for every letter I got threatening to 'stone' me... the pun aside, it was quite barbaric."

    red @surprised "Did people lose their jobs over this? Why so much passion?"

    sonia @talking2mouth "The chairman of the Galarian league had invested a {i}lot{/i} of money into gathering up Wishing Stars. There were huge payouts for anyone who could donate them to the league, or who could give him more information about them."
    sonia @talking2mouth closedbrow "But as soon as Gran and I published our paper on the true nature of the Wishing Stars, those bounties dried up." 
    sonia @sadmouth "The Chairman didn't explain his reasoning, just that his understanding of Galar's energy situation, and its solutions, had dramatically shifted."

    red @confused "How so?"

    sonia @talking2mouth "Not certain. There were rumors that he was going to try and build a rocket that could travel into space and mine the source of the Wishing Stars for the energy within."
    sonia @closedbrow talkingmouth "I reckon that, if that {i}was{/i} his plan, us proving that these meteoroids were coming from a Pokémon would make it pretty hard to mine."

    red @closedbrow talking2mouth "I get it."

    sonia @sadbrow happymouth "So it's less that people 'lost their jobs' and more that... well, a lot of people were getting pretty wealthy before Gran and I published our paper."

    pause 1.0

    sonia @angry "Bloody cheapskate never {i}did{/i} pay us. Gran and... well, mostly just me. I could {i}really{/i} use that money right now..."

    pause 1.0

    red @talkingmouth "You know, we're kinda in the same boat."

    sonia @surprised "Beg pardon?"
    sonia @happy "I'm a Kobukan dropout, and you're the favorite of the Battle Team Captain."
    sonia @surprisedbrow happymouth "I'm not sure I see the similarities there."

    red @happy "Yeah, they're more than skin deep."

    pause 1.0

    red @talkingmouth "I say 'same boat' and I mean, well... I can't really pay for Kobukan, either."

    sonia @surprised "{w=0.5}.{w=0.5}.{w=0.5}.Wot?"

    red @sadbrow sweat happymouth "Yeah. I'm from a small town in the Southwest of Kanto. Pallet Town. Most people haven't heard of it. Have you?"

    sonia @sad "'Fraid not. Sorry."

    red @talkingmouth "No biggie. Anyway, yeah, I'm from a tiny town, and I lived in a tiny house, and it was just me and my Mom. I got into this school, but I can't afford it."

    if (not IsBefore(4, 10, 2004)):#FIX THIS: Address if you pay your first semester
        red @closedbrow talking2mouth "I mean, we both obviously managed to pay for our first semesters, but I, at least, have no idea how I'm going to do my second."

    sonia @frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
    sonia @talkingmouth "Something will come up."

    red @confusedeyebrows talkingmouth "Really? Where's this coming from?"

    sonia @talking2mouth "...I can't rightly say. But I have a feeling. I know when bad things are about to happen, but I also know when good things are about to happen. It's... well, I suppose you'd call it an ability."

    if (not IsBefore(1, 5, 2004)):
        sonia @sadbrow happymouth "Though nothing of the sort resembling yours, of course."

    sonia @talkingmouth "There's a group in Galar that believes in a concept called 'Karma.' Good things happen to those who've had bad happen to them, and vice versa."
    sonia @happy "It's a comforting thought. That everything will balance out in the end."
    sonia @talkingmouth "A lot of awful stuff has happened to me, but I'm certain that the good is just around the corner. And the longer I wait, the better it'll be."

    pause 1.0

    redmind @thinking "That's either some impressive optimism...{w=0.5} or {i}damaging{/i} delusion."

    sonia @talking2mouth "I just need to get through the 'now', and tomorrow will be better."

    pause 1.0

    red @talking2mouth "...Hey. Would you be willing to tell me {i}why{/i} you left Kobukan last year?"
    red @closedbrow talking2mouth "Was it {i}really{/i} because you discovered the Battle Team was hideously corrupt and evil, and you had to leave to train for a year until you were strong enough to come back and defeat them?"

    pause 1.0

    sonia @surprised "That sounds like something Leaf would say."

    red @talkingmouth "Yeah, she did."

    sonia @sad "So, people are talking about why I left... well, I suppose that's no surprise."
    sonia @talking2mouth "No, I'm afraid it wasn't anything so stylish. I'm not some sort of secret agent, I don't have an exploding pen, I like my Martinis stirred, and I don't have any insidious dirt on the Battle Team."

    pause 1.0

    sonia @sad "That'd be a more fun story, honest."

    pause 0.5

    sonia @closedbrow talkingmouth "I'm willing to tell you, [first_name], but you'll probably just think less of me."

    red @talkingmouth "Everyone slips and falls occasionally. I'm sure it's not that bad."

    if (not IsBefore(1, 5, 2004)):
        red @talkingmouth "Besides, if you can overlook the whole 'Frienergy' thing..."

    sonia @talking2mouth "...Right. Well, the story began in February."

    red @closedbrow talking2mouth "Last year?"

    sonia @talking2mouth "No, this year. Last {i}school{/i} year, but Kobukan runs a year-long program. So... just a couple months before you enrolled, I imagine."

    red @talkingmouth "Ah, gotcha."

    sonia @talking2mouth "I was part of the Battle Team. A decent battler, I think. I'd gotten through the first Quarter Qlash easily enough. Quarter Qlash two was quite a bit harder. Quarter Qlash three was... almost impossible."

    red @confused "But you {i}did{/i} make it through."

    sonia @talking2mouth "Yes. Not easily, but I managed it."

    red @closedbrow "{w=0.5}.{w=0.5}.{w=0.5}."

    sonia frownmouth @closedbrow talking2mouth "But that's when I... well, that's when... I'd only {i}barely{/i} gotten through QQ three. I needed to train harder. I started staying up at nights to train."

    sonia @sadbrow talking2mouth "But then I ended up losing sleep, so I did poorer on my academics. I needed to focus more on that, so I started skipping lunches to study. The hunger made me even more tired, and I started falling asleep in classes."

    pause 1.0

    sonia @talking2mouth "I collapsed in Gym Class. Went {i}right{/i} out."
    sonia @talking2mouth "Spent three days in the infirmary with pneumonia from my weakened immune system, due to lack of sleep or nutrition."
    sonia @sad "Then they... had to send me to the {i}actual{/i} hospital to pump my lungs, and... the bill for that was enormous... and I was terrified of sending it to Gran, so..."

    pause 1.0

    sonia @closedbrow sadmouth "I'm sorry, I... I can't..."

    red @sadbrow talking2mouth "Hey, it's alright. I understand. You don't need to explain anything. You can stop now."

    pause 0.5

    sonia @sadbrow happymouth "...No. No, I started this. So I should see it through to the end, shouldn't I?"

    pause 0.5

    sonia @talking2mouth "Well. After all that, I was a nervous wreck when it was time to actually show up for the fourth Quarter Qlash. All I could think about was my gym challenge in Galar, and how I'd failed that." 
    sonia @sad "I had every advantage, but Opal still beat me handily."

    pause 0.5

    sonia @closedbrow talking2mouth "I couldn't bear to go through that embarrassment again. I couldn't... let everyone down again, like that."
    sonia @sad "So I did exactly what I was most afraid of, and let everyone down anyway. I just ran away. I hid in Kobukan, renting out a small apartment with my pocket change, and taking on odd jobs at anywhere that would hire me."

    red @talking2mouth "I'm sorry."

    sonia @closedbrow sadmouth "I never intended to come back. But when I heard the music from the Stadium... a years' worth of memories rushed back into me, and I... I couldn't help but think that maybe I had another chance."

    pause 1.0

    sonia @angry "Of course, I may have slightly overlooked the fact that I couldn't possibly {i}afford{/i} a second chance."
    sonia @sad "Dean Drayden was exceedingly generous for letting me re-enroll, even after the deadline. He often makes exceptions like that. But he can't just waive my entire tuition fee."

    pause 1.0

    red @talkingmouth "Well, like you said. Something will come up."

    sonia -frownmouth @happybrow sadmouth "I suppose that's all we can do for now. Keep the faith, right?"

    red @happy "We'll make it through, Sonia. I believe it. We'll make it through together."

    pause 1.0

    sonia @surprisedbrow talkingmouth "Hm. Ness is pretty lucky, finding a guy like you."

    red @surprised "Huh?"

    sonia @sadbrow talkingmouth "Well, most of the guys she attracts are shallow idiots who just want her fame, or money, or nice arse. You seem {i}real.{/i}"

    red @happy "Hey, that's a serious compliment. I'll put that on my review page."

    pause 1.0

    if (not HasEvent("Nessa", "DenyDate")):
        red @closedbrow talking2mouth "But, to be honest, I'm not really sure {i}she{/i} attracted {i}me{/i}. She was pretty forward when it came to, uh, setting up our date."
    else:
        red @closedbrow talking2mouth "But, to be honest, I'm not really sure {i}she{/i} attracted {i}me{/i}. She was pretty forward, even though we didn't go on a date."

    sonia @talkingmouth "Hm. That sounds like Ness, alright."

    sonia @sadbrow happymouth "I almost wish that I {i}could have{/i} given you a test run for her."

    red @confused "Um?"

    sonia @happymouth "Hah! That's a joke. Sorry, in rather poor taste, wasn't it? Just a joke."
    sonia @sadbrow talking2mouth "It's been a while since I've had anyone to talk to like this..."

    pause 0.5

    if ("Raihan" in GetStudents()):
        red @talkingmouth "What about Janine? Nessa? Raihan?"

        sonia @talking2mouth "Well... I'm endlessly glad Nessa and Raihan are here with me, of course, but conversations with them often have to dance around the topic of me leaving last year..."
    else:
        red @talkingmouth "What about Janine? Nessa?"

        sonia @talking2mouth "Well... I'm endlessly glad Nessa's here with me, of course, but conversations with her often have to dance around the topic of me leaving last year..."

    #FIX THIS when more senior students show up
    
    sonia @closedbrow talking2mouth "For good reason, of course. But, since I arrived late, after most people were introduced to each other, I..."
    sonia @sadbrow happymouth "It'd be nice if I had a [bluecolor]friend{/color} that wasn't angry at me."

    pause 1.0

    red @happy "You called?"

    sonia @surprised "Hm?"

    red @talkingmouth "A friend that's not mad at you. He's standing right here, he's got two thumbs, and his name is [first_name] [last_name]."

    sonia @surprised "Oh! Um. Well... I mean, if you're not... against it... I could certainly help you out, I think I know quite a bit from my previous year, and--"

    red @happy "Sonia, chill. You don't need to sell yourself to me. I like you. I want to be friends because of {i}you,{/i} not because of what you can do."
    red @talkingmouth "You're passionate about your work, knowledgeable about research and Pokémon, and you're incredibly determined. When bad stuff happens to you, you just keep going, even if you have to do it alone."
    red @sadbrow happymouth "I admire that about you. Seriously. So, yeah, I want to be friends."

    pause 1.0

    sonia @happymouth "I... um, I'd like that. If you wouldn't mind."

    $ persondex["Sonia"]["Relationship"] = "Friend"
    $ persondex["Sonia"]["RelationshipRank"] = 1

    $ PlaySound("sav.ogg")

    narrator "Your heart shifts as you feel your relationship with Sonia evolve from '{color=#0048ff}Classmate{/color}' to '{color=#0048ff}Friend{/color}'!"

    return

label Sonia2:
    scene research
    show sonia angrybrow frownmouth with Dissolve(2.0)
    show screen songsplash("Sonia's Theme", "Syntthetix")
    stop music fadeout 1.5
    queue music "audio/music/sonia_start.ogg" noloop 
    queue music "audio/music/sonia_loop.ogg"

    narrator "You walk into the Research Center, looking for Sonia, when you suddenly hear her humming a little song to herself."
    narrator "She's looking closely at a glowing red rock on the countertop--or, wait, no. You suddenly remember what Sonia said about Wishing Stars, and how they were {i}not{/i} rocks, but biological material."
    narrator "Her brow is furrowed in concentration, and even her breathing is light."
    narrator "You try to {i}subtly{/i} make your presence known, without startling her."

    red @closedbrow talking2mouth "{size=30}{i}Ahem.{/i}{/size}"

    pause 1.0

    red @confusedeyebrows talking2mouth "{size=35}{i}Ahem!{/i}{/size}"

    sonia @talkingmouth "Right, I {i}can{/i} hear you, you know."

    red @closedbrow sweat talkingmouth "Oop. Sorry."

    sonia @happybrow talking2mouth "Just give me a tad. I feel like I'm on the verge of something quite important, here."

    pause 1.0

    sonia @talking2mouth "Oh! I know. Yamper! Entertain our guests, will you?"

    $ sidemonnum = pokedexlookupname("Yamper", DexMacros.Id)

    $ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))

    sidemon "Yam! Yam-yam!"

    $ PlaySound("Pokemon/pikachu_happy3.ogg")

    libpikachu @happy "Pi-i-i-ka!"

    narrator "[pika_name] jumps off your shoulder and bounds up to Sonia's Yamper, showing a surprising amount of affection."
    narrator "The two run in circles around the lab, sniffing each other."

    pause 0.5

    redmind "That's cute. I didn't know [pika_name] liked Sonia's Yamper so much, though."
    redmind "Wonder what that's about...? Maybe they became friendly during some of the times I dropped [pika_name] off for Sonia to study. "

    show sonia -angrybrow -frownmouth with dis:
        xpos 0.5
        ease 0.5 xpos 0.75 ypos 1.2 zoom 1.3

    sonia @talking2mouth "Right, I think I'm at a good stopping point."

    pause 0.5

    red @talkingmouth "What's up with those two?"

    sonia @talking2mouth "Oh, just a standard Electric-type polarity attraction dynamic."

    red @playfuleyes unamusedeyebrows talking2mouth "Oh, yeah, of course, that was going to be my first guess."

    if (not HasEvent("Lieutenant Surge", 1)):
        sonia @talking2mouth "It's something they teach in Electric-type classes."

    elif (classstats["Electric"] < 50):
        sonia @talking2mouth "Instructor Surge will teach it later in his Electric-type class."

    else:
        sonia @talking2mouth "Hm? Don't you remember when Instructor Surge taught about it in his Electric-type class?"

        red @talking2mouth "I guess since it didn't seem as though it would directly help me win a battle, I forgot."

    red @talkingmouth "Could you give me a quick rundown?"

    sonia @talking2mouth "Simply put, Electric-type Pokémon are some of the best at transferring power between each other."
    sonia @talking2mouth "You might know that many Pokémon with the ability Plus or Minus are Electric-type, so just being in each other's presence powers each other."
    sonia @talkingmouth "Some Pokémon are so good at sharing energy, sharing power between themselves, they effectively become a singular entity. Magnemite, for example."
    sonia @talking2mouth "Kobukanian Plusle and Minun battling together can even share thoughts, feelings, and damage between themselves."

    pause 0.5

    narrator "The two of you watch your Electric-types playing around for a while."

    sonia @talking2mouth "In any case, Electric-types are most prone to cross-species friendships. I suppose one could say it's easy for them to communicate."

    sonia @happy "Look, there. [pika_name] is headbutting Yamper's neck fluff."

    red @talkingmouth "Is that where Yamper stores its electricity, like Pikachu's cheeks?"

    sonia @talking2mouth "Not quite. Yamper can't actually store the electricity it generates. When it runs, it generates electricity, but you can see sparks fly off of it."

    red @surprised "Woah! Is that alright, then? For you to have your Yamper in this laboratory?"

    sonia @happy "Of course! Come here, Yamper!"

    $ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))

    sidemon "Yamper! Yam-yam!"

    sonia @talking2mouth "Look here. See? He's got little rubber wellies that keep him grounded."

    red @happy "Oh my God. That's adorable."

    sonia @talking2mouth "Arguably, I'm more of a static hazard than Yamper here is. I {i}should{/i} probably be wearing a hairnet, but Professor Oak doesn't keep any in stock."
    sonia @closedbrow talkingmouth "And he leaves coffee rings on the delicate equipment here, anyway. I'm pretty sure anything in this laboratory could be replaced at the snap of his fingers."

    $ PlaySound("Pokemon/pikachu_confused.ogg")

    libpikachu @surprised "Piiiika?"

    sonia @happy "Well, except you, of course!"
    sonia @talking2mouth "You're the only liberation form Pikachu, after all."

    $ PlaySound("Pokemon/pikachu_happy1.ogg")

    libpikachu @happyeyes talking2mouth "Pika."

    sonia @talking2mouth "I wanted to thank you, by the way, for letting me study [pika_name]."

    red @talkingmouth "Hey, thank you for studying him. I wouldn't know nearly as much about how he works if you hadn't given me that headstart."

    if (HasEvent("Professor Oak", "ForeveralsNoIdea")):
        red @sadbrow talking2mouth "Seriously, I was {i}completely{/i} lost."
        
    elif (HasEvent("Professor Oak", "ForeveralsALittleBit")):
        red @talkingmouth "I only understood a little bit of how they worked back then."

    else:
        sonia @talking2mouth "You're having me on. You told me back then that you figured out how they worked before we ever chatted, remember?"

        red @sad2eyes sadeyebrows talkingmouth "Oh. Well, er..."

    sonia @talking2mouth "Don't worry yourself about it. It was my pleasure to help, in whatever small ways I could."

    pause 0.5

    sonia @talking2mouth "On that line of thought, is there something I could do for you?"

    red @talkingmouth "Nah, just came in here to talk."

    sonia frownmouth @sad "Ah. Well, I'm not sure if there's anything I could talk of that'd be interesting to you."

    pause 0.5

    red @sad "Why do you do that?"

    sonia @surprised "Hm?"

    red @closedeyes angryeyebrows talking2mouth "You're a researcher working in a groundbreaking field. You're a skilled battler, one of the best on the Battle Team."
    red @happy "You're a reliable Senior to all your classmates. You're amazing, Sonia. You're personal friends with a champion, a Gym Leader, and a supermodel." 

    show sonia blush surprisedbrow frownmouth with dis

    red @sadbrow talkingmouth "It seems like everyone but {i}you{/i} realizes how amazing you are."

    pause 0.5

    sonia -surprisedbrow -frownmouth sadbrow @talking2mouth "C-come on. Lay off. It's not right to tease a lady like that."

    red @talkingmouth "...Wait."

    pause 1.0

    red @closedbrow talking2mouth "Your best friends are a Champion, a powerful and popular Gym Leader, and a supermodel. And your grandmother is a world-famous Dynamax researcher."

    sonia @surprised "Y-yes?"

    red @closedbrow sweat talking2mouth "Janine's a good captain, but she's a bit terse, and doesn't throw compliments out very often. So, I guess that leads me to ask you..."

    show sonia -lightblush surprisedbrow frownmouth with dis

    red @talkingmouth "Have you... {i}ever{/i} had a compliment directed directly at you?"

    sonia -surprisedbrow @happy "Of course! Don't be daft."

    red @confused "What was it?"

    pause 1.0

    sonia @talking2mouth "Er... well, {i}you{/i} just said I was amazing."

    red @talkingmouth "Okay. Besides me."

    sonia @sadbrow talkingmouth "Er..."

    red @happy "Well, no wonder you're having such a tough time, then! Even your crowning achievement, the study of the Wishing Stars, just got a bunch of angry geologists on your back!"

    sonia @talkingmouth sadbrow "Put like that, it does sound like I've had a rather rough run of it, I suppose."

    red @sad "{w=0.5}.{w=0.5}.{w=0.5}."
    red @happy "Well, that sucks. But I know {i}just{/i} what to do."

    show sonia:
        xpos 0.75
        ease 0.5 xpos 0.5 ypos 1.4 zoom 1.5

    narrator "You get very close to Sonia, and look her {i}directly{/i} in the eyes."

    $ firstinitial = first_name[0]

    sonia @blush surprised "[firstinitial]-[first_name]?"

    red @talkingmouth "You're intelligent."

    sonia @sadbrow talking2mouth "Honest, most of my work is pretty derivative of-"

    red @talkingmouth "You're an excellent battler."

    sonia @talking2mouth "Most of it is just remembering type match-ups. Compared to-"

    red @happy "You're funny."

    sonia @surprised "Funny? Now, {i}that's{/i} a laugh. I'm so awkward, I-"

    red @talkingmouth "You're a good friend."

    sonia @sad "How good a friend can I be when I-"

    red @happy "You're beautiful."

    sonia @angry "Now hold on, Ness-"

    red @happy "You're ambitious."

    sonia sad "Leon-"

    scene blank2 with Dissolve(1.0)

    narrator "This goes on for a while.{w=0.5} Eventually, Sonia stops protesting, having melted into a thoroughly mortified puddle draped over a lab table, begging weakly for you to stop."

    red @happy "...You doing alright?"

    sonia fullblush @closedbrow talkingmouth "{size=30}Asdfghjkl...{/size}"

    red @happy "Cool."

    scene research with splitfade

    pause 1.0

    show sonia fullblush sadbrow:
        ypos 2.0 rotate 40
        ease 2.0 ypos 1.0 rotate 0

    sonia -fullblush @fullblush talking2mouth "...Th-thanks. I think, somewhere deep down, I might have needed that."

    red @sadbrow talkingmouth "Not so deep. Everyone needs to be told how awesome they are once in a while."

    sonia -sadbrow @sadbrow talking2mouth "Maybe you're right."

    red @happy "We're not done yet, though."

    sonia @surprised "Wh-what? No, I, I, I really {i}must{/i} insist that you {i}stop!{/i}"
    sonia @angry "I'm your senior, somewhat, and I insist that you quit bothering me with these... these... aggrandizements!"

    red @talkingmouth "Sure. I wasn't going to be the one to say it. {i}You{/i} are."

    sonia @talking2mouth "Beg pardon?"

    red @happy "Say something about yourself that you like. Give {i}yourself{/i} a compliment."

    sonia @talking2mouth "Oh. Well, er... my grades are decent enough."

    red @talking2mouth "I already said that one, when I said you were intelligent. Something I {i}haven't{/i} said."

    sonia @surprised "Besides the fact grades are only somewhat correlated with intelligence, you can't possibly expect me to do that! You've already complimented me every which way possible!"

    red @talkingmouth "Nah, I'm sure I missed a few things. Go ahead."

    pause 1.0

    sonia @closedbrow talkingmouth "I honestly can't think of anything."

    pause 0.5

    sonia @sadbrow talkingmouth "{size=30}Well, there {i}is{/i} that. I suppose you wouldn't want to say that...{/size}"

    pause 0.5

    sonia @closedbrow talking2mouth "{i}Ahem.{/i}"
    sonia @sadbrow bigblush talking2mouth "I have... er... in my own opinion... a rather nice chest."

    pause 1.0

    red @fullblush surprised "Ah."

    sonia @happy "Ah-ha, there we go! Now it's your turn to blush like a little schoolgirl!"

    red @talkingmouth "Well, I mean, I'm not going to deny it, but... yeah, I wasn't going to be the one to say it."

    sonia @blush closedbrow talking2mouth "W-well, then. I won."

    red @happy "I guess you did. Good job."

    pause 1.0

    sonia @sadbrow talking2mouth "May I confide in you something a bit silly?"

    red @talkingmouth "Of course. Go ahead."

    sonia @talking2mouth "I was often compared to Raihan and Nessa in terms of my looks. Sometimes even Leon."

    red @talkingmouth "Okay. I can see that. They're both pretty showy, and--"

    sonia @sadbrow talking2mouth "Beautiful, yes. Their skin is clear and perfect, their bone structure is immaculate, their... well, you know."
    sonia @talkingmouth "Raihan may be broader than a barn, and Nessa may have a stomach flat enough to sharpen a sword on, but I {i}do{/i} have my own advantages."
    sonia @talking2mouth "Actually, it was Nessa who pointed out that I could flatter myself a bit more than I did."
    sonia @sadbrow talking2mouth "Much of my wardrobe before then consisted of my Gran's hand-me-down floral dresses and cardigans."
    sonia @talking2mouth "One day, she sat me down, and told me that she wasn't going to let me dress like an OAP any more."

    pause 0.5

    sonia @talking2mouth "I used to feel like I was just wearing a costume--like I was dressing like someone I'm not. But Raihan told me that that's how {i}everyone{/i} feels."
    sonia @happy "He told me that's what fashion {i}is.{/i}"

    if (IsAfter(12, 5, 2004)):
        $ ValueChange("Raihan", 1, 0.33, False)
        $ ValueChange("Nessa", 1, 0.66)

        narrator "Your understanding of both Raihan and Nessa deepens!"

    else:
        $ ValueChange("Nessa", 3, 0.66)

        narrator "Your understanding of Nessa deepens!"

    pause 0.5

    sonia @sadbrow talking2mouth "So. That's that, I suppose. If you'd ever wondered if I was unaware of how my outfits fit... er... I'm not."
    sonia @talking2mouth "I have difficulty feeling proud of much, but... well... there are some things I'm quite confident about."

    red @playfuleyes surprisedeyebrows smirkmouth "Hm. This is a new side of you."

    sonia @talking2mouth "Oh, bother, I probably shouldn't have told you that.{w=0.5} That {i}gosh-darn{/i} Frienergy."

    red @talkingmouth "I'd like to think it's just my inoffensive charisma."

    sonia blush angrybrow talking2mouth "Oh, get on out of here, you cad. I'm busy unearthing the mysteries of space! I've no more time to talk about boobies!"

    red @happy "Alright, alright! I'm gone!"

    scene blank2 with splitfade

    pause 2.0

    scene research 
    show sonia sadbrow bigblush
    with Dissolve(2.0)

    pause 2.0

    sonia @talkingmouth "Get your head on straight, Sonia. You've no time to be fancying your [bluecolor]juniors{/color}. Focus."

    show sonia surprisedbrow frownmouth with dis

    $ PlaySound("Phone.ogg")

    pause 1.0

    sonia "Hm?"

    sonia "A... a job offer?! From... {i}Macro Cosmos{/i}...?"

    $ persondex["Sonia"]["Relationship"] = "Junior"
    $ persondex["Sonia"]["RelationshipRank"] = 2

    $ PlaySound("sav.ogg")

    narrator "Your heart shifts as you feel your relationship with Sonia evolve from '{color=#0048ff}Friend{/color}' to '{color=#0048ff}Junior{/color}'!"

    return