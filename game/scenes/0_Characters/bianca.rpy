label Bianca1:
    
show academyhall with dis

pause 1.0

stop music fadeout 3.0

narrator "You're walking through the academy's halls, when, suddenly, you hear what sounds like hiccupy coughing echoing from a classroom."

red @closedbrow talking2mouth "Hm? Class shouldn't be in session right now... who's that?"

narrator "You slowly push open the door..."

show screen songsplash("An Unwavering Heart", "Zame/Pokestir")
queue music "audio/music/unwaveringheart.ogg"

call clearscreens() from _call_clearscreens_177

show blank2 with splitfade

pause 1.0

show classroom 
show bianca closedbrow frownmouth cry
with splitfade

pause 0.5

narrator "You can barely believe your eyes. Bianca, who you've never seen without a big smile on her face, is sitting collapsed over a desk, face wet with tears."

red @sadbrow talking2mouth "...Bianca?"

bianca @sadbrow talking2mouth "...Red hat?"

red @sadbrow talkingmouth "That's me. Red hat number three."

pause 0.5

red @sadbrow talkingmouth "...Do you want to talk?"

pause 0.5

bianca shadow "...No."

pause 0.5

red @sad "Would you like me to leave?"

pause 0.5

bianca -shadow -closedbrow sadeyebrows @sideeyes sadeyebrows talking2mouth "No."

$ ValueChange("Bianca", 3)

red @talkingmouth "Okay."

show bianca:
    ease 0.5 ypos 1.0 zoom 1.1

narrator "You take a seat at a desk two away from Bianca, stepping around the broken glass."

pause 1.0

narrator "And you wait. For a {i}very{/i} long time."

pause 1.0

narrator "You can hazard a guess as to what this is about. You remember Bianca's conversation with Anabel clearly--you remember the horror Bianca reacted with when she learned her father was dead."
narrator "Not much time had passed since then--the emotions are doubtlessly fresh and raw."
narrator "You're unsure what to say. When a person dies, you generally speak well of them. You remember their life, their accomplishments, the marks they left on the living."
narrator "But, in this case, you don't know who Bianca's father was. And what you {i}do{/i} know of him doesn't paint a good picture."

pause 0.5

red @talking2mouth "Is... is this about your father?"

bianca @sadeyes talking2mouth "...Yeah. I was just thinking about him, and... and I started... I had to hide in this classroom, so no-one could see me drop my smile."
bianca @closedeyes sadeyebrows talking2mouth "And I couldn't even do {i}that{/i} properly."

pause 0.5

red @sadbrow talking2mouth "...What does this change?"

bianca @closedbrow talking2mouth "N-nothing. {w=0.5}{i}Sniff.{/i} I'm still living with Professor Fennel. Doctor Amanita is still paying for me to be here. He wasn't a part of my life--a part of {i}anything{/i}."

pause 0.5

bianca @sideeyes sadeyebrows talking2mouth "...Why am I sad? I shouldn't be sad. I should just hook a smile onto my face, like I always do. This is a goo-- {w=0.5}a goo--"
bianca @closedbrow sadmouth "...I can't say it."

pause 0.5

bianca @closedbrow talkingmouth "I... didn't {i}lose{/i} anything. So why am I sad?"

red @talking2mouth "...You don't always love your family. You don't even always like them. But I think you always wish you could, and hope that one day, they might do the same for you."
red @sad "And you... you lost that hope. That's where your pain is coming from."

bianca @sideeyes talking2mouth "...I guess you're right."

pause 0.5

bianca @sadbrow talkingmouth "Thank you. I know you're trying to make me feel better."

red @sadbrow talkingmouth "'Trying?' Not succeeding?"

bianca @sadeyes talking2mouth "...Sorry. I've heard... I've heard everything you're saying from my roommates already."
bianca @sideeyes sadeyebrows talking2mouth "It helped in the beginning, but..."

red @sadbrow talkingmouth "I understand."

pause 0.5

bianca @closedbrow angrymouth "I just wanted to prove to him that he was wrong. I wanted to prove to him that I could be more than what he thought I was."
bianca @sadbrow talking2mouth "And now... now he's dead. And I've missed my chance. Forever."

red @talking2mouth "I know you didn't like him. Your performance at the QQs made that pretty clear."
red @closedbrow talking2mouth "But... who {i}was{/i} he?"

bianca @sideeyes talking2mouth "He was a brain surgeon. He was really good at it... and because he was good at cutting open people's brains, he thought he knew how everyone's brains worked."
bianca @sadeyes talkingmouth "He thought he could tell, from a short list of demographics information, everything about you. He saw patterns everywhere, patterns where they didn't exist."
bianca @talkingmouth "He wanted to know everything. But you can't. So he'd just make wide generalizations--assumptions--and treat them like they were facts."

pause 0.5

bianca @talkingmouth "Over time, those patterns drove away Mom. Daddy got worse, after that. He thought that if I went to university, they'd radicalize me, and... and I'd leave him too."
bianca @closedbrow cry angrymouth "But... but then he kicked me out of the house! If he was afraid of me leaving, then why would he kick me out of the house?! I didn't {i}want{/i} to go!"
bianca @sadbrow talking2mouth "...On that day, I begged him to let me stay. I cried for a week before. I hugged him so hard, because I didn't want to leave, but he called the police, and they dragged me away from him..."

pause 0.5

bianca @shadow angryeyebrows talking2mouth "And now the police have taken him away from me {w=0.5}{i}again.{/i}"

pause 1.0

bianca sad3mouth sad2eyes cry2 -cry "It's not fair. It's {i}so{/i} not fair. I didn't hate him. I {i}didn't{/i} hate him. I just wanted to get back at him a little bit. I never thought... I never thought anyone would..."

narrator "Bianca seems to be hyperventilating."

menu:
    "Take deep breaths, Bianca.":
        show bianca frownmouth -sadeyes cry -cry2 with dis

        red @talkingmouth "It's alright, Bianca. I won't say 'calm down', but you'll get through this. No-one thinks you hated him, or wanted this."

    ">Hug her":
        $ AddEvent("Bianca", "BiancaHug")
        show bianca surprisedbrow -cry2 cry frownmouth with dis:
            ease 0.5 zoom 1.3 ypos 1.1

        red @talkingmouth "It's alright, Bianca. I won't say 'calm down', but you'll get through this. No-one thinks you hated him, or wanted this."

        show bianca closedbrow lightblush with dis

        pause 1.0

        red @sad2eyes lightblush talking2mouth "Er, sorry, should I--?"

        $ ValueChange("Bianca", 3)

        bianca @closedbrow talking2mouth "Please don't let go."

        pause 0.5

        red @closedbrow talkingmouth "Alright. {size=30}It'll be alright.{/size} {size=20}There, there. It'll all be fine.{/size}"

pause 2.0

bianca -lightblush -closedbrow @sad "How can you say that? The policewoman who told me, Anabel, said what I did was a felony." 
bianca @sad2eyes sadmouth "What if she comes back and arrests me? What if, during our big end-of-year graduation ceremony, they're about to hand me my diploma, but then they slap some handcuffs on me and drag me away to the slammer?"
bianca @closedeyes sadeyebrows talking2mouth "Maybe... maybe I {i}should{/i} be in prison."

red @sad2eyes frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
red @talking2mouth "No. I don't know what the law says, or what 'the rules' are, or whatever, but I know you. You're a kind, friendly, good-hearted, girl that everyone loves."
red @sadeyebrows talkingmouth "If you 'should be' in prison, then there's not a person in this school who shouldn't be locked up."

pause 0.5

bianca @closedbrow talking2mouth "...I wish Cheren was here."

red @angryeyebrows surprisedeyes frownmouth "...Woah, I think that just gave me whiplash." 
red @sadbrow sweat talking2mouth "Why Cheren?"

bianca @talkingmouth "Cheren... knew Daddy."

red @surprised "Hm? Oh, that's right..."

show cafeB_CG at sepia, dissolvein behind flashback:
    subpixel True
show flashback
with dis

pause 0.5

$ hideside = True

cheren @talkingmouth "In many ways her focus surpasses mine."

bianca @talkingmouth "Aw, thanks! I knew I'd have to take this seriously after that big brouhaha with my Dad, though."

cheren @talkingmouth "Er... yes. That was quite a 'brouhaha.'"

show blank with splitfade

hide flashback
hide cafeB_CG
hide blank
with dis

$ hideside = False

pause 1.0

red @closedbrow talkingmouth "What was this 'brouhaha,' then?"

bianca @sadbrow talkingmouth "Oh... it was when Daddy was kicking me out of the house."
bianca @talkingmouth "Cheren came over to try and talk some sense into him. A week of me crying and begging hadn't done anything, so I told him not to bother, but..."
bianca @happybrow talkingmouth "But Cheren doesn't stop fighting just because the battle's lost."

pause 0.5

bianca @talking2mouth "He tried to convince Daddy that he was making a mistake, that I could absolutely go to college, that he was going to ruin his relationship with his daughter."
bianca @sideeyes talking2mouth "...But Daddy refused to listen, and demanded that Cheren leave his property."
bianca @closedbrow talking2mouth "...And when Cheren refused, Daddy sent out his Lampent to force him to leave."

pause 0.5

bianca @sadbrow talkingmouth "Cheren's Snivy was no match for my Dad's Lampent. He lost. Badly."
bianca @sadbrow talking2mouth "He looked... {i}so{/i} guilty."
bianca @talking2mouth "I think he's the only one who could really understand how I felt about Daddy, having met him..."

pause 0.5

redmind @closedbrow frownmouth sweat "I can't believe I'm going to say this."

red @sadbrow talkingmouth "Do you want me to get him?"

bianca @talking2mouth "...No. I don't want him to see me like this."

pause 1.0

bianca @talkingmouth "Before my Mom left... she told me to always keep a smile on my face. That there are people out there who can only win by making you cry."
bianca @closedbrow talking2mouth "Cheren's... the only one who knows what my Dad was like. So if he sees me cry, then... then Daddy wins."

pause 1.0

red @sad2eyes sadeyebrows talking2mouth "...Look. Cheren and I aren't best buds, exactly, but if you need a friend, he can be there for you."
red @sadbrow talkingmouth "And, I mean, I can, too. And don't forget about your dormmates. I know they care about you."

pause 0.5

bianca -cry @talking2mouth "...Yeah. Yeah, I guess so. {i}Sniff.{/i}"

pause 1.0

bianca @sadeyebrows closedeyes talking2mouth "...I still miss him. I feel like it's too soon to miss him, but also too late to {i}still{/i} be missing him."

pause 0.5

red @sadbrow talking2mouth "...There's no 'too late' or 'too early' for these things. Whatever you feel is real. I'm just sorry you have to feel it."

pause 1.0

bianca @sad "I'm... I'm sorry. I shouldn't take your time like this. You've probably got more important things to do than hang out with a wreck like me, right?"

red @happy "Bianca, c'mon. A friend of mine is crying in an empty classroom, and you think I can just go to my dorm and focus on studying damage formulas?"

bianca @sadeyebrows talking2mouth "...Are we friends?"

red @sadeyebrows talkingmouth "'Friend' is kind of my default relationship with everyone I meet."

bianca @sadbrow talkingmouth cry "I actually thought... {i}Sniff.{/i} I thought you might hate me for what Cheren did."

red @happy "Nah. Those were {i}his{/i} choices. I'm not going to blame someone for their friend's actions."

bianca @sideeyes talking2mouth "...Well. I, um... I was actually the one who suggested to him you might have some kind of power."

red @surprisedeyes angryeyebrows frownmouth "{w=0.5}What?"

bianca @sadeyes talking2mouth "{i}Please{/i} don't be mad."

red @sad2eyes talking2mouth "I... I can't be mad, of course, not now, but... what's this about?"

bianca @sadeyes talking2mouth "Nurse Miriam was teaching us about Aura-wielders in our Human Physiologies class, and she mentioned that Aura-Wielders are able to connect with people on a deeper, subconscious level."
bianca @sideeyes talking2mouth "Then, when we were hanging up campaign posters..."

scene academy:
    xpos -700 ypos -525
show bianca 
show flashback
with splitfade

cheren @closedbrow talkingmouth "I swear, it's the oddest thing. Serena and Calem's campaign is doing well enough, but [first_name]'s is absolutely soaring."
cheren @talkingmouth "He has a way of touching the hearts and minds of the voters that I can't help but envy. It's a shame he doesn't seem overly enthused about his own progress."
cheren @happy "Oh, well. I suppose I might as well just cheer him on. What do you think, Bianca?"

show bianca:
    ypos 1.0
    block:
        ease 0.3 ypos 1.1
        ease 0.3 ypos 1.0
        repeat 5

bianca @happy "I dunno. You should be doing waaaa~aaay better than him. I mean, he's not trying {i}at alllll.{/i} Ooh, I bet [first_name]'s an Aura-user!"

cheren @surprised "Beg pardon?"

bianca @talkingmouth "'Aura' is a mental and physical power that some people have. They're like Espers, except they train to get their powers, instead of being born with 'em."
bianca @happy "Nurse Miriam just taught us about Aura-Users! Most of 'em come from Sinnoh."

cheren @closedbrow talking2mouth "I don't understand. How would this power help?"

show bianca:
    ypos 1.0
    block:
        ease 0.2 ypos 1.1
        ease 0.2 ypos 1.0
        repeat 5

bianca @talkingmouth "Apparently, Aura-Users can share their emotions with people, and read the emotions of others."

cheren @talking2mouth "I don't see how that would help in his campaign efforts."

show bianca:
    ypos 1.0
    block:
        ease 0.1 ypos 1.1
        ease 0.1 ypos 1.0
        repeat 5

bianca @happy "Because if you know how people feel about what you're saying, you know exactly what to say to make them happy!"

cheren @closedbrow "{w=0.5}.{w=0.5}.{w=0.5}."
cheren @closedbrow talkingmouth "No, that's silly, Bianca. Besides, Aura is--you said it's a trained power? Mostly from Sinnoh?"
cheren @talkingmouth "[first_name] can't be much older than eighteen. And he certainly isn't Sinnohan."
cheren @happy "No, I'm afraid I've got nothing to blame for my failings but an inability to get my message across clearly!"

pause 0.5

cheren @talkingmouth "Besides, we're not competing for seats. There's no reason for us to come into conflict."
cheren @happy "Although, if there was, I should be quite glad that he doesn't have a Lampent!"
cheren @talkingmouth "I still shudder whenever I see one of them. Oof. That was quite a beating I received."

bianca @happy "Yeah, I guess you're right."

hide bianca

cheren @talkingmouth "Hm."

pause 0.5

cheren @sad2eyes noshine "{w=0.5}.{w=0.5}.{w=0.5}."
cheren @sad2eyes noshine talking2mouth "Surely not."

scene classroom
show bianca sadeyebrows frownmouth
with dis

pause 1.0

bianca @talking2mouth "...Are you mad?"

menu:
    "A little, yeah.":
        $ AddEvent("Bianca", "LittleMad")
        
        red uniform @closedbrow talking2mouth "...Now isn't the time. I'm trying to make you feel better, right now."

    "Nah.":
        $ AddEvent("Bianca", "NotMad")
        $ ValueChange("Bianca", 3)

        red @closedbrow talking2mouth "...I might've been mad at one point, but I'm over it now. Besides, it doesn't matter if you put the idea in his head. He was the one who acted on it."

        red @talkingmouth "And even if I {i}was{/i} mad, now wouldn't be the time for it. I'm trying to make you feel better, right now."

pause 1.0

bianca @talkingmouth "I think... actually... I {i}do{/i} feel a little better."

pause 0.5

bianca @talking2mouth "Thank you for letting me cry on you."

red @talkingmouth "It's alright. I'm sorry you had to cry in the first place, but if you need to, my shoulders are ready to serve."

bianca @talking2mouth sadbrow "...Thanks."

pause 1.5

show bianca:
    ypos 1.0
    block:
        ease 0.5 ypos 1.1
        ease 0.5 ypos 1.0
        repeat 2

bianca @sadbrow talkingmouth "You have excellent [bluecolor]shoulders.{/color}"

red @talkingmouth "...They're all yours. Keep your chin up. And call me whenever you want to talk, okay? We're all here for you."

bianca @closedbrow talking2mouth "...Okay."

python:
    haslitwick = False
    haslampent = False
    haschandelure = False
    
    for mon in AllPokemon():
        if (mon.GetId() == pokedexlookupname("Litwick", DexMacros.Id)):
            haslitwick = True
        elif (mon.GetId() == pokedexlookupname("Lampent", DexMacros.Id)):
            haslampent = True
        elif (mon.GetId() == pokedexlookupname("Chandelure", DexMacros.Id)):
            haschandelure = True

if (haslampent):
    red @talkingmouth "...So Cheren's afraid of Lampent, huh?"
    red @happy "It just so happens that I have one..."
    
    bianca @poutmouth sadbrow "Don't be a meanie."
    
    red @sadbrow talkingmouth "Sorry. Just joking."

elif (haschandelure):
    red @talkingmouth "...So Cheren's afraid of Lampent, huh?"
    red @happy "It just so happens that I have a Chandelure..."
    
    bianca @poutmouth sadbrow "Don't be a meanie."

    red @sadbrow talkingmouth "Sorry. Just joking."

elif (haslitwick):
    red @talkingmouth "...So Cheren's afraid of Lampent, huh?"
    red @happy "It just so happens that I have a Litwick..."

    bianca @poutmouth sadbrow "Don't be a meanie."

    red @sadbrow talkingmouth "Sorry. Just joking."

$ RelationshipRankUp("Bianca", "Shoulder", 1)

return