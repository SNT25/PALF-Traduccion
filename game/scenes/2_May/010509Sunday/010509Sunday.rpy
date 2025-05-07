label day010509:

$ HealParty()

call calendar(1) from _call_calendar_34

$ calDate = calDate.replace(day=9, month=5, year=2004)

$ timeOfDay = "Morning"
show morning at vspaz

pause 3.5

show kitchen 
show blue:
    xpos 0.33
show leaf:
    xpos 0.66
with splitfade

blue @talkingmouth "...don't know why you're asking me. I'm not her damn keeper."

leaf @talking2mouth "Look, we're {i}both{/i} her classmate, Blue."

blue @closedbrow talking2mouth "The idea of a Pokémon being a Pokémon trainer... it's ridiculous."

leaf frownmouth @sarcastic "Yeah, sure, it's a gross abomination against morality or whatever. I'm just asking if you've seen her."

blue @angry "And I already told you no! What, do you think I captured her or something?"

leaf @angry "Wouldn't you try to, if you had the chance? You said you would!"

blue @closedbrow talkingmouth "Oh my god, when I said that, I was {i}joking{/i}. Why do people always take {i}your{/i} jokes in the best possible light, but the moment I try to be funny, I've crossed a line?"

leaf @talking2mouth "Maybe because my jokes don't put people down! They just put myself {i}up!{/i}"

blue @angry "Well, I've got an idea for what you can put up your--"

show blue surprisedbrow frownmouth
show leaf surprisedbrow frownmouth
with dis

red @happy "Hey, guys!"

leaf -surprisedbrow -frownmouth @happy "Heya, [first_name]! How are you doing?"

red @talkingmouth "Alright. Sounds like you two are talking about Tia?"

blue -surprisedbrow -frownmouth @closedbrow talkingmouth "Yeah, looks like your pet fled the coop. Not surprised after she had to carry {i}your{/i} fat ass for a whole day."

red @confused "It was sixteen hours, and--once again--I have {i}no{/i} body image issues. You're beating against a wall here."

show leaf angry with dis

blue @happy "Who said I was talking about {i}you{/i}? Smell ya!"

hide blue with dis

pause 1.0

leaf @talking2mouth "D-- did he just say I've got a fat ass?!"

red @closedbrow talking2mouth sweat "I wouldn't take it personally. It's kinda how he says hello."

leaf frownmouth @angrybrow talking2mouth "That punk. I can't believe I was starting to think he wasn't completely awful."

red @closedbrow talking2mouth sweat "Yeah, that's how he gets ya."

leaf @closedbrow talking2mouth "Whatever. Hey, if you see Tia, let me know, okay? I haven't been able to track her down since Wednesday."
leaf @embarrassedbrow talking2mouth "I'm... a little bit worried someone might have seen her when we were flying in, and..."

red @surprised "What, you think someone might have captured her?"

leaf -frownmouth @talking2mouth "No, no, I'm sure that's not it. She's crazy powerful, you know?"
leaf @closedbrow talking2mouth "I mean... I think. I've never seen her battle. But... it seemed like she really wanted to be at Kobukan, and just blowing off the Quarter Qlashes like this is weird."

pause 1.0

if (GetRelationshipRank("Sabrina") > 0):
    red @closedbrow talking2mouth "Come to think of it, Sabrina hasn't been around lately, either...?"

    leaf @closedbrow talkingmouth "Sabrina?"
    leaf @surprised "Oh, the girl those two assholes--"

    red @talkingmouth "Yeah, that one."

    leaf @sadbrow talking2mouth "I don't know about her. I... I think she's been gone ever since Saturday, actually..."

    red @closedbrow talking2mouth "Damn. I guess I won't be seeing her in the future QQs, then..."

    pause 1.0

leaf @talking2mouth "Well, just keep an eye out."

red @happy "Of course. Got plans for today?"

leaf @talking2mouth "Are you inviting me somewhere?"

if (HasEvent("Leaf", "AcceptedConfession")):
    red @talkingmouth "Well, we've got a date to go on, don't we?"

    leaf @surprised "Wait, that's still on?"

    red @surprised "Um... if you want it to be?"

    leaf blush @happy "Oh! I just thought, because of... you know, everything..."

    leaf @talking2mouth "I'm really glad to hear you still want to do that, though."

    red @talkingmouth "'Course. I'm guessing you've got other plans for today, though?"

    leaf @embarrassedbrow talkingmouth "A... a little bit, yeah... sorry about that."

    red @happy "It's cool. You're worth the wait."

    leaf bigblush @surprised "Wha-- hey, what do you think you're doing, busting out lines like that?"

    red @talkingmouth "Turning on {i}the charm{/i}, my lady. Did it work?"

    leaf blush @flirtbrow talking2mouth "Yeah, it totally did, right up until you called me m'lady, and now I don't think I'm physically capable of ever finding you attractive again."

    red @talking2mouth "Damn."

    leaf @talking2mouth "Oh well. Maybe my identical twin will take pity on you."

    red @happy "An identical twin, huh? Say, could you and your twin--"

    show kitchen with vpunch

    show leaf:
        ease 1.0 xpos 1.5

    leaf surprised fullblush "LA {w=0.2}LA {w=0.2}LA {w=0.2}LA {w=0.2}LA--I'm not letting you finish that!--LA {w=0.2}LA {w=0.2}LA {w=0.2}LA {w=0.2}LA {w=0.2}LA!"

else:
    red @talkingmouth "Nah, just wondering."

    leaf @talking2mouth "Alright. Don't really have any big plans, no. Just trying to decompress after the Quarter Qlashes, and train up Jigglypuff a bit more."

    red @talkingmouth "Sounds good. How's she treating you?"

    $ sidemonnum = pokedexlookupname("Jigglypuff", DexMacros.Id)

    $ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))
    sidemon "Jigga- Jiggaloo!"

    leaf @talking2mouth "She's a sweetheart. I think she's been looking forward to stretching her limbs after all those years."

    redmind @confusedeyebrows frownmouth "Limbs?"

    red @talkingmouth "Well, have fun with that. See you later!"

call freeroam from _call_freeroam_16

call texting from _call_texting_14

stop music fadeout 1.5
queue music "audio/music/unwaveringemotions.ogg"

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_129

show blank2 with dis
    
$ renpy.pause(2.5, hard=True)

scene garden night
show drayden at night, rightside 
show janine at night, leftside
with Dissolve(2.0)

drayden @sadeyes "Janine."

janine @talking2mouth "Dean. Thank you for meeting with me."

drayden @happy "It's certainly alright. I was out here anyway, for a different task."
drayden @surprised "That being said, I {i}do{/i} have an office. I don't {i}always{/i} need to meet people outside, in the garden, late at night."

janine @smirkmouth "It's prettier out here, though."

pause 1.0

drayden @happy "Quite so. The stars shine again. I feel that, perhaps, there is a chance they may shine ever brighter than before."

pause 1.0

show janine sadbrow with dis

pause 1.0

drayden @sad "You... don't appear overly enthusiastic."

janine @talking2mouth "I... failed the Battle Team, Dean. I let one of our members lose in the first round."

drayden @sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."

janine @talking2mouth "I don't know what to do. I feel like I'm not fit to keep leading the Battle Team."
janine @closedbrow talking2mouth "But, at the same time, I absolutely can't quit. Not with the way the team is right now."

drayden @sadbrow "Forgive me--I'm not aware of the specifics of this situation. How did you fail the Battle Team?"

janine @talking2mouth "Because our team was smaller this year, I didn't think we would have to bother sending parts of us to different areas of Kobukan."
janine @closedbrow talking2mouth "Because of this, one of my Battle Team members was matched up against another. One of them lost, and... she became the first Battle Team member to ever lose in the first round of the Quarter Qlashes."

drayden @sadbrow "Hm... This was match three of round one, yes?"

janine @talking2mouth "Yes."

drayden @happy "Well, that's not so bad. At least it wasn't matches one or two."

pause 1.0

janine "{w=0.5}.{w=0.5}.{w=0.5}."

drayden "Janine, you made a mistake. I am aware that such a thing, for you, is unheard of. But it's a very human trait."
drayden @happy "It's our humanity that makes life worth living. I think no less of you for a single misstep, especially considering you've been doing this for three years."

janine "{w=0.5}.{w=0.5}.{w=0.5}."

drayden @sadbrow "You seem unconvinced, Janine."

janine @closedbrow talking2mouth "It's just...{w=0.5}{nw}"
extend @talkingmouth " no, it's nothing..."

drayden "Come now. I'm not so old I could fail to see the sadness you wear. Is there something I could do?"

janine @sadbrow smirkmouth "I... don't think so. I mean, there is {i}one{/i} thing, but..."

drayden @surprised "Oh? Something to pull the Captain of our esteemed battle team out of the dumps? Please, go ahead."

janine @talking2mouth "I shouldn't... I mean, it's a hassle, and it might cost some money, too..."

pause 1.0

drayden @happy "Janine, please."

janine @talking2mouth "Well... if you insist..."

pause 2.0


queue music "Audio/Music/fuchsia_start.ogg" noloop
queue music "audio/music/fuchsia_loop.ogg"

show screen songsplash("Fuchsia City", "Zame")

show drayden surprisedbrow with dis

janine -sadbrow @talking2mouth "I got a tip the next Quarter Qlashes are going to be Squad Battles. An incredible zero point five percent of squad battle losses are the result of friendly fire. We need uniforms--"

show janine at night:
    ease 0.5 xpos 0.6

janine @talking2mouth "--here's an online listing, you can sign the check here to get them here by Friday, I've already set up the order--"

show janine at night:
    ease 0.5 xpos 0.33

janine @talking2mouth "--and I'm going to need the highest-quality threadcount, the extra-breathable inserts, and the warranty on the entire batch of them, because if one of my battlers loses their uniform, we need an {i}immediate{/i} replacement."

drayden "Eh?"

janine @talking2mouth "Shared uniforms are the best way to build a cohesive aesthetic among the team, prevent unnecessary friendly-fire incidents, and build team morale. This will work."

pause 1.0

janine @smirkmouth "Sound good? I promise, this is the only thing that could ever make me happy again."

drayden @sadbrow "...I'm so used to your directness, I suppose I'd forgotten your bloodline's proclivity towards trickery."

janine @closedbrow smirkmouth "You gotta mix things up. There's no one strategy that works every time."

drayden @sadbrow "Yes, well, I suppose I {i}did{/i} agree to this. Very well, you'll have your costumes."

janine @closedbrow talkingmouth "'Uniforms.'"

janine @smirkmouth "Thanks, Dean."

hide janine with dis

stop music fadeout 2.0

pause 2.0

drayden -surprisedbrow -frownmouth -surprised @sadbrow "Well, I believe I just got rather... what was the word? 'Pwnd?'"

show iris winter at leftside, night with dis

iris @talkingmouth "No-one says that anymore, Daddy."

drayden @happy "Oh, my bad. It seems my vocabulary is no longer 'lit.'"

show iris sadeyebrows with dis

stop music fadeout 1.5

queue music "audio/music/potown_start.ogg" noloop
queue music "audio/music/potown_loop.ogg"

drayden "In any case... did you make any progress on finding those two missing students?"

iris -sadeyebrows @surprised "Oh! That's what I wanted to tell you about! I'm still looking for them, but my Haxorus {i}definitely{/i} picked up on a scent!"
iris @closedeyes angryeyebrows talking2mouth "I would bet a ton of donuts that there's a strong dragon in there, too."

drayden @sadbrow "Hm... a strong dragon, you say? That's concerning. I hope they're not in any danger..."

iris @talkingmouth "...D'ya think I should go out again? I'm real tough. If they're'n any danger, then shouldn't we rescue them right away?"

pause 1.0

drayden @sadbrow "Perhaps we should. But... Iris... there is something I must confess."

iris @surprised "Huh?"

drayden @sadbrow "You aren't the first person I sent out to look for the missing students. I had hoped that Instructor Will might be able to find his students, given his close connection to one of them, but..."

pause 1.0

show iris surprisedbrow frownmouth with dis

drayden @sadbrow "He has not returned for several days now."
drayden @sadbrow "It may be time to call in a professional for this task. I fear what declaring the forest 'safe' preemptively might have caused. Needless to say that we'll need to repeal that declaration."

pause 1.0

iris sadbrow frownmouth @sadmouth "Will those people be all right?"

pause 1.0

drayden @sadbrow "While the stars still shine.{w=0.5} While the stars still shine..."

scene blank2 with Dissolve(3.0)

jump day010510