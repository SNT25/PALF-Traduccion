label secondhomeroom010423:

scene blank2

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom behind blank2

show oakbg behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade

oak @talkingmouth "Well, that about finishes it. Have a good Friday, everyone! And have fun with the Springsday celebrations tomorrow!" 
oak @talkingmouth "Remember, if you get any eggs in the egg hunt, make absolutely sure to bring them to the Research Lab for incubation." 
oak @talkingmouth "The eggs can handle being outside for the duration of the egg hunt, but after that, they should be kept warm again."

$ renpy.music.set_volume(0.1, delay=1.0, channel="music")
$ PlaySound("BellChime.ogg")

$ renpy.pause(2.0, hard=True)
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

oak @talkingmouth "Well, that about finishes things up! Dismissed."

hide oakbg with dis

redmind uniform @thinking "Alright. I've got a bit of free time before the Battle Team's first meeting. I should use this time to prepare."

if (punkwins == 0):
    redmind @thinking "I could also go to the city. I bet I can find some Pokémon there that I wouldn't be able to find in the fields."
    redmind "Maybe if I beat Silver's gang, they'll clear out the alleyway, and I can look around for a bit..."

call freeroam from _call_freeroam_9

stop music fadeout 1.5

queue music "audio/music/DragonDenStart_B.ogg" noloop
queue music "audio/music/DragonDenLoop.ogg"

scene blank2

narrator "As soon as night falls, you make your way to the Battle Hall. While on the grounds, a security team member notices you, looks at a digital pad in his hand, and nods, letting you through."

show stadium_empty 
with splitfade

pause 1.0

show blue:
    xpos 1.0/10.0
show leaf:
    xpos 6.0/10.0
show sonia:
    xpos 9.0/10.0
show erika:
    xpos 7.0/10.0
show ethan:
    xpos 4.0/10.0
show silver:
    xpos 2.0/10.0
show bea behind ethan:
    xpos 3.0/10.0
show dawn frownmouth behind ethan:
    xpos 5.0/10.0
show hilbert behind sonia:
    xpos 8.0/10.0
with dis

narrator "Walking into the Battle Hall, you see a few faces you recognize, out of about a dozen people. In fact, you see everyone you battled during the tryouts."

redmind @surprised "Woah. Everyone I battled got in? I guess I already knew four of them did, but, still..."

if (GetRelationship("Dawn") == "Muse"):
    show leaf behind dawn
    show ethan behind dawn

    show dawn:
        ease 0.5 ypos 1.1 zoom 1.2
    
    red @confused "Hey... Dawn? How did you end up in the Battle Team?"

    dawn @closedbrow talking2mouth "I... I won all my tryout matches..."

    red @confused "Huh? But, I mean, how did you end up in the tryouts?"

    dawn @closedbrow talking2mouth "...Janine forced me into it."

    red @closedbrow talking2mouth "She {i}forced{/i} you?"

    show dawn:
        ease 0.5 ypos 1.2

    dawn @closedbrow talking2mouth "Yeah... she saw my Mega Altaria in gym class, then ambushed me before lunch a week ago."

    dawn @sad "She... she pinned me up against a locker and told me I was going to join the Battle Team. And I've... I've kinda just been following her instructions ever since..."

    pause 1.0

    redmind @thinking "Is it wrong of me to think that's kinda hot?"

    pause 1.0

    red @happy "Well, chin up. Janine's kinda intense, but if she's forcing you into the Battle Team, that must mean she's certain that you can make it through our training."

    dawn @sad "Yaaaay..."

    show dawn behind ethan:
        ease 0.5 ypos 1.0 zoom 1.0

if (not persondex["Bea"]["Named"]):
    show silver behind bea
    show ethan behind bea

    show bea:
        ease 0.5 xpos 0.3 ypos 1.1 zoom 1.2

    redmind @thinking "And who's this?"

    red @happy "Hi there!"

    bea @talkingmouth "Hello."
    
    $ BecomeNamed("Bea")
    bea @talkingmouth "My name is Bea. What's yours?"

    red @talkingmouth "It's [first_name]. From Pallet Town in Kanto. You?"

    bea @talkingmouth "Stow-on-Side in Galar. It's a pleasure to meet you."

    red @thinking "[ellipses]"
    red @confused "...Are you sure?"

    bea @talkingmouth "What do you mean?"

    red @talking2mouth "Uh, I mean, I don't want to assume, but you're kinda..."

    pause 1.0

    bea @talkingmouth "Stony-faced?"

    red @happy "That's a ballpark."

    bea @talkingmouth "Apologies. Due to my extensive physical training, my body and face barely have any involuntary movements."

    red @confused "Oh, yeah? How's that work?"

    bea @talkingmouth "Essentially, I have absolute control over every physical aspect of my being. I do not flinch, I do not recoil, and I do not stumble."
    bea @sad "Consequently, I also do not emote."

    red @surprised "Wait, a minute! You just looked sad there!"

    bea sweat "You must be imagining things."

    red @happy "No, you're totally sweating now."

    bea angry "[ellipses]"

    pause 1.0

    bea "...DAMN IT!"

    red @surprised "Woah, what?"

    bea @closedbrow talking2mouth "I thought I'd gotten to the point where I had entirely discarded my involuntary reflexes!"

    red @confused "Wait, you WANT this?"

    bea @angry "You! You better take responsibility for making me lose my two-week streak!"

    red @confused "You went two weeks without showing emotions?!"

    bea @angry "I will accept no excuses! Whenever your schedule is unoccupied, meet me in the gym. You'll assist in my training."

    red @talkingmouth "I don't get what you--"

    show bea behind ethan:
        ease 0.5 xpos 0.3 ypos 1.0 zoom 1.0

show blue surprisedbrow frownmouth
show leaf surprisedbrow frownmouth 
show erika surprisedbrow frownmouth 
show ethan surprisedbrow frownmouth 
show silver surprisedbrow frownmouth 
show bea surprisedbrow frownmouth 
show dawn surprisedbrow frownmouth 
show sonia surprisedbrow frownmouth
show hilbert surprisedbrow frownmouth
with dis

stop music fadeout 4.0

show smoke:
    animation
    alpha 0.0 yalign 3.0 xalign 0.5
    parallel:
        ease 3.0 yalign 0.5
    parallel:
        ease 0.5 alpha 1.0
        pause 0.5
        ease 3.0 alpha 0.0 

pause 4.0

red @confused "Huh?"

ethan @closedbrow talking2mouth "Dusk, are you smoking?"

queue music "Audio/Music/fuchsia_start.ogg" noloop
queue music "audio/music/fuchsia_loop.ogg"

show screen songsplash("Fuchsia City", "Zame")

pause 1.0

show blank
show janine behind blank

pause 0.1

hide smoke
hide blank

pause 1.0

janine @closedbrow talking2mouth "Line up."

show blue:
    ease 0.8 xpos 1.5
show leaf:
    ease 0.5 xpos -0.5
show erika:
    ease 1.0 xpos 1.5
show ethan:
    ease 0.4 xpos 1.5
    pause 0.2
    ease 0.4 xpos -0.5
show silver:
    ease 0.5 xpos -0.5
show bea:
    ease 0.5 xpos 1.5
show dawn:
    ease 0.2 xpos -0.5
show sonia:
    ease 0.5 xpos 1.5
show hilbert:
    ease 0.5 xpos -0.5

pause 1.0

janine "{w=0.5}.{w=0.5}.{w=0.5}."
janine @closedbrow talking2mouth "Hm."
janine @talking2mouth "Alright, listen up."
janine @talking2mouth "2001. The Battle Team got forty-seven members through QQ1, twenty-three through QQ2, five through QQ3, and zero through QQ4." 
janine @closedbrow sadmouth "Despite being eliminated during the third Quarter Qlash, the previous Team Captain appointed me the next year's Captain."
janine @talking2mouth "2002. The Battle Team, under my command, got through the third Quarter Qlash with five members out of sixty-two. Again, no-one got through QQ4 into the National Tournament." 
janine @closedbrow sadmouth "This time, I was eliminated in the fourth round. Regrettably, I had removed five of my own teammates across the entire year."
janine @sad "Not a mistake I intend to repeat."
janine @talking2mouth "2003. Last year. The Team was much smaller, only thirty-eight members. For the third year in a row, we got five members through Quarter Qlash three." 
janine @closedbrow talking2mouth "I didn't participate that year, because I didn't want to eliminate any of my teammates."

pause 1.0

janine @closedbrow talking2mouth "Unfortunately, four of the team members who got through Quarter Qlash three were eliminated in Quarter Qlash four. And one was disqualified."

hide sonia 
sonia @frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

janine @talking2mouth "That brings us to 2004. I've tried something completely different this year."

janine @closedbrow talkingmouth "If you were thinking the tryouts were rigged, grab a cookie. I wasn't trying to put everyone on equal footing. I was trying to see how you handled adversity."

pause 1.0

janine @talking2mouth "I'm serious about the cookies, by the way. There's a plate on the table over there."

hide ethan
hide erika
hide leaf

ethan @happy "Sweet!"

erika @talkingmouth "Oh, how delightful."

leaf @flirttalk "Hey, I thought the Battle Team was meant to be super-intense and hardcore? But you're baking cookies for us?"

janine @talking2mouth "If I'm going to push you harder than you've ever been pushed before, I'm going to start off gently. Besides, I didn't make them, Instructor Bertha did."

pause 1.0

janine @angrybrow talking2mouth "Alright, that's enough time. Get back in line."

pause 1.0

janine @talking2mouth "So, as I said, trying something different. In previous years, I pretty much followed Lance's advice to a tee. But we've..."
janine @sad "We've failed to put any of our own in the National Tournament, the biggest Kobukan event, for four years." 
janine @talking2mouth "If we fail again this year, this will be the longest Kobukan Academy has ever gone without placing a current student in the National Tournament."
janine @closedbrow talkingmouth "Kobukan deserves better than that. Besides, there's no notable alumni who've declared they'll be launching a Kobukan league challenge this year. It's up to us."
janine @talking2mouth "If necessary, I {i}will{/i} launch my own bid for the national tournament this year. I'm certain I could have made it last year--I just chose not to."

hide blue 

blue @happy "Hah! You don't need to worry about that, Janny! I'll sweep that National Tournament so hard they'll put me in the history books."

janine @surprised "Janny? Wow. Call me that again and I swear to god, the only thing you'll be sweeping is this arena."

blue @surprised "Tch..."

janine @closedbrow talkingmouth "In case I {i}do{/i} have to launch my own campaign--in case I'm not sure any of you can make it--I've kept the Battle Team very small." 
janine @talking2mouth "Hopefully, we won't get matched up against each other until the end of the year."
janine @talking2mouth "Though, even if you {i}are{/i} eliminated from the National Championships, you can still participate in intra-school tournaments, and experience the Battle Team's intense training."

pause 1.0

janine @talking2mouth "Now. Any questions?"

hide dawn

dawn @sad "Um... how did you pick the Battle Team members?"

janine @talking2mouth "I looked for what was lacking in previous years. The last few years' Battle Teams have just been the most powerful students. It seemed obvious, that I should pick those, right? Lance thought so." 
janine @closedbrow talkingmouth "But raw power hasn't been working out. So maybe my Dad had a point after all. I don't know. But this is the last year I've got to figure it out. Because, no matter what, we're placing in the National Tournament this year." 
janine @sad "Look, I'll be straight with you. I've been watching all of you. In your gym classes, in the fields." 
janine @smirkmouth "The tryouts were a formality. There's only a couple of you who surprised me in the tryouts, I pretty much knew how they were going to go down."

hide leaf

leaf @surprised "What?!"

janine @talking2mouth "Only a couple of you have enough Pokémon to mount multiple different strategies. If you're both using a known strategy, it's pretty easy to just run the calcs before the tryout."

pause 1.0

janine @smirkmouth "Which I did."

pause 1.0

hide erika 

erika @talkingmouth "Well... would it be alright if I asked what I demonstrated that you thought would be a worthy addition to the team?"
erika @happy "Why, I thought I did rather abominably! I was all but ready to pack my luggage and head home."

janine @talking2mouth "...Erika, how much did you spend to prepare your team for this battle tryout?"

erika @surprised "Oh? Well... discussing matters of monetary concern in public is rather vulgar, no?"

janine @closedbrow talking2mouth "Deal."

erika @sadbrow talking2mouth "Well... just over four hundred thousand."

janine @talking2mouth "Right. And how much would you have been willing to spend, if you could guarantee victory?"

erika @closedbrow talking2mouth "Well... I think it would be irresponsible to spend any more than five million on a single series of battles, yes?"

pause 1.0

red @surprised "{size=30}F-f-five million?! She'd have been willing to spend {i}five million{/i} on the tryouts?!{/size}"

leaf @surprised "{size=30}Holy shit. That's a lot. That's a lot for {i}me.{/i} That's {i}a lot!{/i}{/size}"

janine @talking2mouth "Yeah. So that's why. The Battle Team is pretty well-funded. But never having to worry about the cost of TMs, training items, field trips... that's a very calculable advantage."

erika @sadbrow talking2mouth "Oh... so I'm a member of the Battle Team because I can afford to be, then..."

janine @closedbrow talking2mouth "No. My Dad recommended you to me specifically. He said that your knowledge of high-level competitive Pokémon theory is the best of any of his students."
janine @closedbrow talkingmouth "Besides, your Pokémon were some of the highest-leveled before the equalizer. You've got a lot going for you."

erika @sadbrow talking2mouth "It seems I failed to put it into practice, though..."

janine @talking2mouth "Yeah. But that's what the Battle Team's training will do. It'll crush your mistakes."

erika @talkingmouth "...Very well. I'll do my best not to disappoint."

pause 1.0

hide silver

silver @talkingmouth "Well, what about me? You say you've been watching us. If you've really been watching me, then I don't get why the hell you'd want me in this school, nevermind on the Battle Team."

janine @talking2mouth "You're fearless. When you talked back to Lance during the exhibition match... that's what I want to see more of." 
janine @talking2mouth "A lot of people lose because they think they can't beat their foe. I get the feeling you think you can't win, but you're going to fight anyway."

silver @talkingmouth "That's not fearlessness. I just don't have anything to lose."

janine @closedbrow talking2mouth "Then you win."

pause 1.0

leaf @talking2mouth "Then what about--"

janine @angrybrow talking2mouth "Okay, that's enough. I'm not going to go through each of you one-by-one and tell you why I think you have a shot at the National Championships."
janine @talking2mouth "You should all be smart enough to figure it out amongst each other. Or just trade the letters I wrote you, whatever."

hide sonia 

pause 1.0

sonia @talking2mouth "...Thanks, Janine."

pause 1.0

janine @sad "Yeah, whatever."

pause 1.0

janine @talking2mouth "It's getting late. Let's talk strategy for the first Quarter Qlash, which starts on May 5th."

blue @surprised "What?! That's just twelve days from now!"

janine @talking2mouth "Calm down. No Battle Team member has ever been eliminated in the first Quarter Qlash. You're up against the entire general population of Kobukan, including hobbyists and people who only keep Pokémon as pets."
janine @talking2mouth "The strategy here is just about how to stagger our sign-ups so it's least likely that any of us get matched up against each other."
janine @closedbrow talkingmouth "Previous years have figured out that if we sign up exactly thirty-one minutes after one another, we're fourty-four percent less likely to end up in battles against each other in the third Quarter Qlash."

leaf @talking2mouth "Oh... so the battles for Quarter Qlash one are going to be really easy?"

janine @closedbrow talkingmouth "Let me put it this way: in 2002, I battled against, in total, three Bidoof in Quarter Qlash one. And that was against three different trainers, yes."

hide dawn

dawn @sad "Oh... well, I could probably handle that..."

janine @angrybrow talking2mouth "You've got a Mega Altaria, and that's just {i}one{/i} of your Pokémon. Stop forgetting."

dawn @sad "Sorry..."

pause 1.0

janine @closedbrow talkingmouth "Oh boy. This is going to be a year. When the team was just a few dozen meatheads, everyone blended together, but this year, everyone's idiosyncrasies are really going to stand out."
janine @closedbrow talkingmouth "We should probably do some teambuilding exercises, just so that our personalities don't cause too many problems later on down the line."

pause 1.0

blue @angry "Hey, why are you all looking at me?!"

hide blank2
show blank2 with Dissolve(3.0)

narrator "After doing some cringe-inducing icebreakers, you begin some intense training, that culminates in your doing push-ups with [pika_name] on your back."
narrator "Apparently, this builds the bond between Pokémon and trainer."

hide bea

bea sweat @talkingmouth "Hah! Hah! Hah! That's ninety-nine, Ma'am!"

hide janine

janine @angry "I'm not a Ma'am, and if you've got enough breath left to speak, you have enough breath to do another twenty!"

bea @angry "Yes! Clobbopus, use Bulk Up! I need more weight!"

ethan @surprised "M-more?! I can barely... breathe..."

redmind "He... has a Pichu on his back. Pichu weigh four point four pounds. That's about the weight of a pair of boots."

call clearscreens from _call_clearscreens_73

narrator "Your Pokémon all benefit greatly from the experience."

$ BattleTeamTraining()

narrator "Janine announces the Battle Team will hold a mandatory meeting Monday night, then sends you all back to your dorms, battered, sore, and satisfied."

hide ethan

ethan @happy "Dude! Is it kinda weird to say that I'm starting to like the pain?"

red @talkingmouth "Nah, Janine has that effect on me, too."

stop music fadeout 3.0

jump day010424