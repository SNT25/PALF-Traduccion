label Cheren1:
    call clearscreens() from _call_clearscreens_165
    scene blank2 with splitfade

    pause 1.0 

    "{color=#ff0000}You are no longer you.{/color}"

    stop music fadeout 1.5
    queue music "Audio/Music/eterna_start.ogg"
    queue music "Audio/Music/eterna_loop.ogg"
    call clearscreens() from _call_clearscreens_225
    scene blank2 with splitfade

    show midnight at vspaz    

    python:
        timeOfDay = "Midnight"
        playercharacter = "Cheren"
        oldinventory = copy.copy(inventory)
        oldpersonalstats = copy.copy(personalstats)
        oldparty = copy.copy(playerparty)
        oldpersondex = copy.copy(persondex)
        oldclassstats = copy.copy(classstats)

        inventory = {
            Item.Notepad : 1,
            Item.SparePens : 7,
            Item.BrokenGlasses : 1,
            Item.TapeRoll: 1,
            Item.ToDoList : 1,
            Item.MusicPlayer : 1,
            Item.SpareTieClip : 1,
            184 : 1 # Paper with [first_name]'s Face
        }
        personalstats = {
            "Charm" : -7,
            "Knowledge" : 24,
            "Courage" : 71,
            "Wit" : 13,
            "Patience" : 3
        }
        playerparty = GetTrainerTeam("Cheren")
        persondex = copy.deepcopy(defaultpersondex)
        #battle teammates
        persondex["Cheren"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Male, "Relationship": "Self", "RelationshipRank": 0, "Events": [] }
        persondex["Bianca"] = {"Named" : True, "Value" : 113, "Contact": True, "Sex": Genders.Female, "Relationship": "Disappointment", "RelationshipRank": 0, "Events": [] }
        persondex["Falkner"] = {"Named" : True, "Value" : 9, "Contact": False, "Sex": Genders.Male, "Relationship": "Underling", "RelationshipRank": 0, "Events": [] }
        persondex["Blue"] = {"Named" : True, "Value" : 17, "Contact": False, "Sex": Genders.Male, "Relationship": "Memory", "RelationshipRank": 0, "Events": [] }
        persondex["Nate"] = {"Named" : True, "Value" : 2, "Contact": False, "Sex": Genders.Male, "Relationship": "Memory", "RelationshipRank": 0, "Events": [] }
        persondex["Sabrina"] = {"Named" : True, "Value" : 34, "Contact": False, "Sex": Genders.Female, "Relationship": "Beggar", "RelationshipRank": 0, "Events": [] }
        persondex[first_name] = {"Named" : True, "Value" : oldpersondex["Cheren"]["Value"], "Contact": True, "Sex": Genders.Male, "Relationship": "Anathema", "RelationshipRank": 0, "Events": [], "Mood": 0 }
        persondex["Roxanne"] = {"Named" : True, "Value" : 14, "Contact": False, "Sex": Genders.Female, "Relationship": "Underling", "RelationshipRank": 0, "Events": [] }
        persondex["Brawly"] = {"Named" : True, "Value" : 8, "Contact": True, "Sex": Genders.Male, "Relationship": "Underling", "RelationshipRank": 0, "Events": [] }   
        persondex["Calem"] = {"Named" : True, "Value" : 28, "Contact": True, "Sex": Genders.Male, "Relationship": "Traitor", "RelationshipRank": 0, "Events": [] }
        persondex["Serena"] = {"Named" : True, "Value" : 24, "Contact": False, "Sex": Genders.Female, "Relationship": "Traitor", "RelationshipRank": 0, "Events": [] }
        persondex["Silver"] = {"Named" : True, "Value" : 68, "Contact": False, "Sex": Genders.Male, "Relationship": "Co-Worker", "RelationshipRank": 0, "Events": [] }
        persondex["Jasmine"] = {"Named" : True, "Value" : 22, "Contact": False, "Sex": Genders.Female, "Relationship": "Traitor", "RelationshipRank": 0, "Events": [] }
        persondex["Grusha"] = {"Named" : True, "Value" : 11, "Contact": False, "Sex": Genders.Male, "Relationship": "Traitor", "RelationshipRank": 0, "Events": [] }
        persondex["Gardenia"] = {"Named" : True, "Value" : 38, "Contact": True, "Sex": Genders.Female, "Relationship": "Target", "RelationshipRank": 0, "Events": [] }
        persondex["Skyla"] = {"Named" : True, "Value" : 53, "Contact": True, "Sex": Genders.Female, "Relationship": "Co-Worker", "RelationshipRank": 0, "Events": [] }
        persondex["Brendan"] = {"Named" : True, "Value" : 5, "Contact": False, "Sex": Genders.Male, "Relationship": "Schoolmate", "RelationshipRank": 0, "Events": [] }
        persondex["May"] = {"Named" : True, "Value" : 4, "Contact": False, "Sex": Genders.Female, "Relationship": "Schoolmate", "RelationshipRank": 0, "Events": [] }
        persondex["Melody"] = {"Named" : True, "Value" : 3, "Contact": False, "Sex": Genders.Female, "Relationship": "Dickless", "RelationshipRank": 0, "Events": [] }

        classstats = { 
            "Normal" : AimLevel() - 2,
            "Fire" : 1,
            "Water" : 1,
            "Grass" : 1,
            "Electric" : 1,
            "Ice" : 1,
            "Fighting" : 1,
            "Poison" : 1,
            "Ground" : 1,
            "Flying" : 1,
            "Psychic" : 1,
            "Bug" : 1,
            "Rock" : 1,
            "Ghost" : 0,
            "Dark" : AimLevel() - 1,
            "Dragon" : 1,
            "Steel" : 1,
            "Fairy" : 1
        }

    pause 3.5

    scene bedroommidnight 
    show screen currentdate
    with splitfade

    pause 2.0

    narrator "{color=#1f67df}But you have not been you for a while.{/color}"

    pause 1.0

    cherenmind night shirtless tired "...I'm so tired."
    cherenmind "Why can't I sleep...?"

    show phone_B 
    show brokenphone
    with fadeinbottom

    cherenmind "I'll call Dad. He's probably still up writing, anyway."

    $ PlaySound("vibrate.ogg")

    pause 3.0

    hide brokenphone
    show brokenphoneperson
    with Dissolve(1.0)

    dad "Heya, kiddo! I haven't heard from you in a while!"
    dad "{w=0.5}.{w=0.5}.{w=0.5}."
    dad "Hey, what's this? I can't see you, kid."

    cheren @sad2eyes talkingmouth "I... fell. My phone broke a little bit."

    dad "{w=0.5}.{w=0.5}.{w=0.5}."
    dad "Well, alright then, kiddo. Just let me know if you need a replacement!"

    cheren @talking2mouth "...Alright."

    pause 0.5

    cheren @talking2mouth sadbrow "I hope I didn't wake you up."

    dad "Not a chance! You know your old man. I've been working on this massive article--an exposé on the construction of the PWT!"
    dad "You'd never believe what those Driftveil contractors are doing. Get this--they're actually hiring illegal immigrants {i}on purpose{/i}, so they can blackmail them and force them to work for lower wages!"
    dad "Well, I won't stand for it! I don't care how many billions they're saving--no amount of money is worth the price of human dignity! As soon as I publish this article, their whole operation will crack like an egg!"
    dad "I tell ya, kiddo! This article will be bigger than the Bronius interview!"

    cheren @sad2brow talking2mouth "...Stay safe. An article like that will make you enemies."

    dad "Hah! Kiddo, {i}way{/i} too late for that one. I was running away from corporate thugs with Sawk on their belts since I was younger than you!"
    dad "And you know what? I'd do the whole thing again!"
    dad "Gahahahaha!"

    pause 1.0

    dad "Hey, Cheren. What's up? You're all quiet."

    cheren @talking2mouth "I'm... just tired."

    dad "C'mon, kiddo. I'm a journalist. I find truth. Besides that, you're my son--I know when you're upset."

    pause 1.0

    cheren @talking2mouth "It's... a deeper tiredness. Today was exhausting."

    dad @talkingmouth "Oh, yeah? Well, tell me about it."

    pause 1.0

    cheren @talking2mouth "Okay."

    stop music fadeout 1.5

    call clearscreens() from _call_clearscreens_226
    scene blank2 with splitfade

    pause 1.0

    show morning at vspaz

    $ timeOfDay = "Morning"

    pause 3.5

    show screen songsplash("Embracing One's Duty", "Zame")
    queue music "audio/music/embracingonesduty.ogg"

    scene studentcouncil
    show silver uniform:
        xpos 0.33
    show skyla uniform:
        xpos 0.66 xzoom -1
    show flashback
    show screen currentdate
    with splitfade

    cheren uniform @talkingmouth "Good morning, you two. I trust your patrols were uneventful. Damage report?"

    skyla @happy "All clear skies and smooth seas, Captain!"

    silver @talkingmouth "Someone set fire to a dumpster, Melody made two different girls cry (and one guy), Brendan and May were caught in the janitor's closet again..."
    silver @closedbrow talkingmouth "On the faculty side of things, Siebold, Kofu, and Katy are fighting. Since they can't agree on what to cook, they're demanding a doubled kitchen budget to make two meals a day."

    pause 1.0

    skyla @happy "All clear skies and smooth seas, Captain!"

    silver @sadbrow talkingmouth "Oh, and someone made an effigy of you and hung it in the auditorium."

    cheren @confusedeyebrows talking2mouth "Oh? That's a new one."
    cheren @closedbrow talking2mouth "...Was it you?"

    silver @angrybrow happymouth "Well, I didn't stop them."

    cheren @tired talkingmouth "Ah... we have fun."

    pause 0.5

    cheren @talkingmouth "Well, I suppose I had better resolve some of these issues..."

    show gardenia uniform angrybrow frownmouth behind silver:
        xpos 1.2 ypos 1.0
        parallel:
            easein 0.3 ypos 0.7
            easeout 0.3 ypos 1.0
        parallel:
            ease 0.3 xpos 0.25
        parallel:
            pause 0.3
            ease 0.5 xzoom -1

    show skyla surprisedbrow frownmouth:
        xpos 0.66
        ease 0.5 xpos 0.75

    show silver surprisedbrow:
        xpos 0.33 xzoom 1
        ease 0.5 xpos 0.5 xzoom -1

    gardenia @angrymouth "Hey!"

    cheren @closedbrow talking2mouth "Good morning again, Gardenia. No, no-one said 'business.'"

    gardenia @talkingmouth "That's not it. I finally have it--{i}undeniable{/i} proof that this school is haunted!"

    cheren @closedbrow talking2mouth "We've talked about this. There's no such thing as ghosts, and your nagging that the Disciplinary Committee drop the important work we're doing to chase phantoms continues to grate on our limited time and patience."

    silver @sad "Important work? That's a laugh. I didn't sign up with you to actually {i}do{/i} Disciplinary Committee work, and even {i}I{/i} feel annoyed at how little we can actually do."

    skyla @angrybrow talkingmouth "We totally do important work! Just yesterday, we helped find a student's lost Poké Ball! Remember? We spent {i}all day{/i} on that."

    gardenia @surprised "A single Poké Ball? They cost, like, $200."

    silver @angry "That's what {i}I{/i} said! It didn't even have a Pokémon in it!"

    cheren @closedbrow talking2mouth "We're getting off-topic. Gardenia, we will not be participating in your ghost hunt. Please take this request to the Occult Club."

    gardenia @angry "I told you, that {i}won't{/i} work. Only people who don't believe in ghosts can get rid of them. The Occult Club is full of believers."

    cheren @sadbrow talkingmouth "And I suppose the instant we find these ghosts, we'd be helpless to 'exorcise' them? Presumably, finding them would make it quite clear that they are, in fact, real."

    show silver sad
    show skyla sad
    with dis

    gardenia @sad "...Just seeing isn't believing. Like how you can {i}see{/i} [first_name] isn't evil, but can't believe it. That stubbornness--that refusal to believe--is what's needed to {i}really{/i} get rid of a ghost."

    cheren shadow sadbrow noshine talking2mouth  "{w=0.5}.{w=0.5}.{w=0.5}."
    cheren @talkingmouth "If you won't leave, then I will. I have {i}real{/i} work to do."

    $ renpy.music.set_volume(0.8, 10)

    scene blank2 with splitfade

    dad "Hah! Every time you tell me about those two, they crack me up. Silver and Skyla, right? I'm pretty sure I know Skyla's Dad. Never heard of this Silver guy, but if he's a Johtonian, he's off my beat."

    cheren tired night shirtless @sadbrow talking2mouth "They tolerate me, which is more than can be said about most people."

    dad "I'd be careful about that Gardenia girl, though. I get a dangerous vibe from her. I feel like she knows exactly what she wants, and she's not going to take no for an answer."

    cheren @sad2brow talkingmouth "You're very right. Anyway, later in the day..."

    call clearscreens() from _call_clearscreens_227

    pause 1.0

    show noon at vspaz

    $ timeOfDay = "Noon"

    pause 3.5

    scene studentcouncil
    show flashback
    show screen currentdate
    with splitfade

    $ PlaySound("knock.ogg")

    pause 0.5

    cheren uniform @downeyes talking2mouth "Come in."

    show melody uniform on behind flashback with Dissolve(2.0)

    melody @talkingmouth "Yo, dickless."

    cheren @talking2mouth "My name is Cheren."

    melody @talkingmouth "Course it is."

    pause 1.0

    melody @talkingmouth "So, third time today, right? Do I get a prize?"

    cheren @talking2mouth "No."

    pause 1.0

    melody @talkingmouth "You're boring me."

    cheren @angrybrow talking2mouth "I am not here to entertain. You are here to think on what you have done wrong, in silence."

    melody @talkingmouth "Uh-huh. 'Cause I'm pretty sure Ex-Champion Wallace sent me here expecting you to punish me."

    cheren @closedbrow uniform "{w=0.5}.{w=0.5}.{w=0.5}."

    melody @talking2mouth "But you can't do that, can you?"

    cheren @talking2mouth "I will elevate this incident to the Student Council, as I have been instructed to do in matters concerning you."

    narrator "You write a note on a piece of paper, placing it on the stack next to you. The stack is already quite large."

    melody @talkingmouth "So dickless..."

    pause 1.0

    melody @talkingmouth "You know, if I'm going to be here so often, you could at least put a beanbag in here. Maybe hook a Wii up on that wall there. Do you do Mario Party? Mario Party co-op?"

    pause 1.0

    melody @sadbrow talkingmouth "Oh, no, of course you don't. Because that would require friends."

    pause 1.0

    melody @talkingmouth "{size=30}And a dick.{/size}"

    $ renpy.music.set_volume(0.6, 10)

    call clearscreens() from _call_clearscreens_228
    show blank2 with transeye 

    cherenmind @sad2brow talkingmouth "I'd almost prefer it were [first_name] who kept getting sent here..."

    pause 0.5

    dad "That Melody... what a piece of work! You said she was Lawrence Phobos' niece? Odd, I don't recall him having any siblings... but that guy's a real piece of work, too."
    dad "A coworker wrote an article about alleged illegal acts happening in Phobos' mansion, the 'Phobosphere'--what a tacky name--and he lost his job the next day. I'm not calling that a coincidence!"

    pause 0.5

    dad "Anyway, what happened next?"

    pause 1.0

    show afternoon at vspaz

    $ timeOfDay = "Afternoon"

    pause 3.5

    scene studentcouncil
    show flashback
    show screen currentdate
    with splitfade

    $ PlaySound("knock.ogg")

    pause 0.5

    cheren uniform @downeyes talking2mouth "Come in."

    show brendan sadbrow uniform behind flashback:
        xpos 0.33
    show may sadbrow uniform behind flashback:
        xpos 0.66
    with dis

    cheren @surprised "Oh? You two? What..."
    cheren @sadbrow talkingmouth "Oh. Was it the janitor's closet again?"

    brendan @talking2mouth "Empty classroom."

    may @talkingmouth "Well, we {i}thought{/i} it was empty."

    cheren @closedbrow sweat talking2mouth "You're putting me in an exceedingly awkward position."
    cheren @sad2brow talkingmouth "Obviously, a little physical affection between consenting adults is not exactly something I wish to punish..."
    cheren @upeyes talking2mouth "But at this point, you've been warned to tone it down so many times, it truly feels like direct rebellion."

    brendan @surprised "I... I swear, it wasn't, man! It's just, when we're together... I mean..."

    may @talkingmouth "Come on. We just love each other so much, Cheren. You {i}must{/i} love someone that much, too, right? Surely you understand."

    cheren @sad2brow talking2mouth "...I do."

    pause 0.5

    show may angrybrow frownmouth
    show brendan angrybrow frownmouth
    with dis

    cheren @closedbrow talking2mouth "But I cannot simply let you off with a warning, this time. You've had enough chances."

    brendan @talking2mouth "Tch."

    may @angry "Great job keeping the school safe from seeing a healthy relationship, Cheren. Thank goodness you're here to save us from that."

    $ renpy.music.set_volume(0.4, 10)

    call clearscreens() from _call_clearscreens_229
    show blank2 with transeye 

    narrator "You scribble a note, and add it to the pile on your desk. The pile bulges, and seems as though it is about to topple."
    narrator "The note you just added slides off the top, into the trashcan next to your desk. You pretend not to notice."

    cherenmind @sad2brow talkingmouth "...I really do understand. Brendan, May... I understand more than you ever could."

    pause 0.5

    dad "Hah hah! College PDA. Classic, kiddo. Hey, you aren't getting into anything you shouldn't, are you? But if you are, well, college is the time for it. Just remember to wear protection!"

    pause 0.5

    dad "Ah, you probably don't want to hear your old man saying that, huh? My bad. How about the rest of your day?"

    pause 1.0

    show evening at vspaz

    $ timeOfDay = "Evening"

    pause 3.5

    scene library
    show flashback
    show screen currentdate
    with splitfade

    pause 0.5

    cherenmind uniform @closedbrow talking2mouth "Alright. I've put this off long enough. I need to do this now."

    show sabrina casualoldhair behind flashback with dis

    pause 1.0

    cheren @talkingmouth "Sabrina, I--"

    sabrina @closedbrow talking2mouth "You wish to apologize."

    cheren @sad2brow talking2mouth "...Yes."

    pause 1.0

    cheren @talking2mouth "I truly--"

    sabrina @closedbrow talking2mouth "You truly never meant any harm to anyone except [first_name]. And even then, you only wanted to bring him down to everyone else's level."
    sabrina @sad2brow talking2mouth "But your passion got the better of you, and you saw how dire the situation was when the school was 'invaded'. You believed drastic measures were necessary."
    sabrina @talking2mouth "You feared meeting with him one-on-one and accusing him directly, as, if he was morally bankrupt, as you feared, he may remove your ability to tell others."
    sabrina @talking2mouth "You left your 'allies' without oversight, believing that they would simply talk to other students and gain compromising information, as you had done. You never meant for me to hurt."
    sabrina @talking2mouth "I know."

    pause 1.0

    show sabrina casualoldhair psychicangryeyes gen1aura: 
        ypos 1.0
        ease 2.0 ypos 0.8
        parallel:
            ease 2.0 ypos 0.85
            ease 2.0 ypos 0.8
            repeat

        parallel:
            ease 2.0 xpos 0.52
            ease 2.0 xpos 0.5
            ease 2.0 xpos 0.48
            ease 2.0 xpos 0.5
            repeat

    sabrina @angryeyebrows psychicfuriouseyes angrymouth "I've had to hear you rehearsing this speech in your head for {i}weeks.{/i} Over and over... just {i}waiting{/i} for you to finally say the words."

    cheren @surprisedbrow talking2mouth "I... my intentions were only ever good..."

    sabrina @talking2mouth "I {i}know{/i}."
    sabrina @talking2mouth "And because I cannot help but know your intentions, you feel entitled to my empathy."
    sabrina psychicfuriouseyes angryeyebrows angrymouth "You will not get it. Take nothing but my scorn. Take it, leave with it, and stay gone."

    cheren @sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."

    cheren @shadow closedbrow talking2mouth "As you wish."

    $ renpy.music.set_volume(0.2, 10)

    call clearscreens() from _call_clearscreens_230
    show blank2 with transeye 

    dad "{w=0.5}.{w=0.5}.{w=0.5}."
    dad "Are you alright, kiddo?"

    show night at vspaz

    $ timeOfDay = "Night"

    pause 3.5

    scene studentcouncilnight
    show flashback
    show screen currentdate
    with splitfade

    pause 0.5

    cherenmind night uniform @closedbrow talkingmouth "Finally. Almost time to go back to the dorm..."
    cherenmind @sad2brow smilemouth "Where I can be surrounded by people who may hate me, but at least don't talk to me."

    $ PlaySound("knock.ogg")

    cheren @surprised "Huh? Who is it? The Disciplinary Committee is closed for today--"

    show falkner behind flashback at night with Dissolve(2.0)

    falkner @talking2mouth "Cheren."

    cheren @closedbrow talkingmouth "*{i}Sigh.{/i}*"
    cheren @talkingmouth "Thank goodness, it's just you. I thought it was a late-night complaint, or..."

    pause 0.5

    cheren @sad2brow talking2mouth "You don't look happy."

    falkner @talking2mouth "I'm not, Cheren. That pile of reports you gave us this afternoon--why wasn't Brendan and May's PDA reported there?"

    cheren @sadbrow talking2mouth "...What?"

    falkner @talking2mouth "We know they were caught, and reported here, as instructed."
    falkner @angrybrow talking2mouth "Brendan told us later, to apologize for giving us more work."
    falkner @talking2mouth "But we didn't have any work, because we were never told."

    pause 1.0

    cherenmind @sadbrow talking2mouth "No good deed goes unpunished."

    cheren @shadow sad2brow talking2mouth "It's a foolish rule. A relic of Kobukan's past. We are not children. This is not a high school. Brendan and May did nothing wrong."

    falkner @angry "That is not for you to decide. You had your chance to change the law when you were running for Student Council. You now exist to {i}serve{/i} the law, not debate it."

    cheren @sad2brow shadow "{w=0.5}.{w=0.5}.{w=0.5}."

    falkner @talking2mouth "Roxanne will tell Drayden about this. I imagine he'll have words for you. Remember, you are a member of the Disciplinary Committee as a {i}punishment{/i}."

    cheren @shadow sad2brow talking2mouth "This is not justice."

    falkner @closedbrow talking2mouth "Justice is an ephemeral--a convenient spirit that means only what the speaker says."
    falkner @talking2mouth "What we want, concretely, is a school where the Student Council can rely on the Disciplinary Committee to follow the established rules laid out, until such a time as they're changed."

    pause 1.0

    falkner @talking2mouth "'Justice' is a ghost."
    falkner @talking2mouth "Do what you said you would do."
    falkner closedbrow talking2mouth "Stop chasing ghosts."

    hide falkner with Dissolve(2.0)

    stop music fadeout 2.0

    call clearscreens() from _call_clearscreens_231
    show blank2 with transeye 

    pause 0.5

    show midnight at vspaz

    $ timeOfDay = "Midnight"

    pause 3.5

    scene bedroommidnight
    show phone_B 
    show brokenphoneperson
    show screen currentdate
    with splitfade

    dad "{w=0.5}.{w=0.5}.{w=0.5}."
    dad "There are bad days, kiddo. There will always be bad days. Things'll turn around."

    cheren night shirtless @sadbrow tears talking2mouth "...I hope you're right."
    cheren @sadbrow talking2mouth "But... what if I don't deserve for them to turn around? What if this, forever, is what I deserve?"

    pause 1.0

    dad "I can't believe that."

    pause 0.5

    dad "It's easy to give up. Every time I bust out the typewriter, I have to consider if I'm okay ruining my life over what I'm about to write."
    dad "And people have promised all sorts of things in retaliation. If I had a nickel for every time someone said 'I'd regret this', I coulda sent you to Kobukan {i}twice.{/i}"
    dad "And you know what? Sometimes, I did. Sometimes I {i}did{/i} regret it. But even when I thought I'd done something wrong, I knew I {i}meant{/i} to do the right thing."
    dad "That's all anyone can do. Besides, call it my bias, but I don't think you did anything wrong."

    cheren @sad2brow talking2mouth "I hurt hundreds of innocent people. I... I may have only managed to expose a {i}single{/i} person who actually deserved it."

    dad "Kid... you're my boy, Cheren. From the first moment I held you in my arms, I knew I would love, trust, and believe in you, no matter who or what you became."
    dad "My only fear when you left Unova was that you'd come back thinking you had to be like {i}them{/i} to win. And everything you're telling me tells me that you're as far from that as you ever were."

    cheren @closedbrow angrymouth cry "Dad..."

    dad "Keep your head up, kiddo."
    dad "And call me more often. I miss you. It's lonely here without you."

    pause 0.5

    dad "...Remember, kid. Even when your Mom left us, I knew I'd done the right thing."
    dad "If I can still hold my head high and believe in justice after that, you can too."

    pause 1.0

    dad "Maybe justice {i}is{/i} a ghost."
    dad "But is there really anything so wrong with chasing ghosts?"

    pause 0.5

    dad "Love you."

    hide phone_B 
    hide brokenphoneperson
    with fadeoutbottom

    pause 2.0

    cherenmind @sad2brow talking2mouth "...It seems that positively affecting reality absolutely eludes me."
    cherenmind @sad2brow smilemouth "Perhaps it is only in fiction, then, that my influence can be found."

    stop music
    $ renpy.music.set_volume(1)
  
    queue music "audio/music/potown_start.ogg" noloop fadein 2.5
    queue music "audio/music/potown_loop.ogg"

    show phone_B
    show phone_A
    with fadeinbottom

    show phone_C behind phone_A with dis

    show phone_msg1 behind phone_A with dis:
        xzoom -1
        
    $ title = Text("Gardenia Natane",size=30,font="fonts/consola_0.ttf",color="#313131")

    image msg6 = Text("Fine.\nRemind me, what was that poem you held\nso much stock in? The cause of all\nthose early-morning interruptions?",size=21,color="#ffffff",line_spacing=5,text_align=0.0)

    show text title behind phone_A:
        xalign 0.51 yalign 0.34 
    show msg6 behind phone_A:
        xpos .41 ypos .4 
    with dis

    pause

    call clearscreens() from _call_clearscreens_232
    scene blank2 with Dissolve(2.0)

    image poemline1 = Text("In hallowed halls, old with wear",size=30,color="#fff")
    image poemline2 = Text("Shadows call to those who dare",size=30,color="#fff")
    image poemline3 = Text("One Living, Ghost in mortal shell",size=30,color="#fff")
    image poemline4 = Text("One Changed, Ghost back from hell",size=30,color="#fff")
    image poemline5 = Text("One Dead, Ghost here further more",size=30,color="#fff")
    image poemline6 = Text("Two Unfed, Ghosts once adored",size=30,color="#fff")
    image poemline7 = Text("By day they hide, by night they roam",size=30,color="#fff")
    image poemline8 = Text("Haunted spectres far from home",size=30,color="#fff")
    image poemline9 = Text("Disaster comes with undrawn breath",size=30,color="#fff")
    image poemline10 = Text("{gradient=#fff-#f00}If not freed, naught else comes but death{/gradient}",size=30,color="#fff")

    show poemline1 with gaussdissolve:
        ypos 1/13 xalign 0.5 yanchor 0.5

    pause 0.5

    show poemline2 with gaussdissolve:
        ypos 2/13 xalign 0.5 yanchor 0.5

    pause 0.5

    show poemline3 with gaussdissolve:
        ypos 3/13 xalign 0.5 yanchor 0.5

    pause 0.5

    show poemline4 with gaussdissolve:
        ypos 4/13 xalign 0.5 yanchor 0.5

    pause 0.5

    show poemline5 with gaussdissolve:
        ypos 5/13 xalign 0.5 yanchor 0.5

    pause 0.5

    show poemline6 with gaussdissolve:
        ypos 6/13 xalign 0.5 yanchor 0.5

    pause 0.5

    show poemline7 with gaussdissolve:
        ypos 7/13 xalign 0.5 yanchor 0.5

    pause 0.5

    show poemline8 with gaussdissolve:
        ypos 8/13 xalign 0.5 yanchor 0.5

    pause 0.5

    show poemline9 with gaussdissolve:
        ypos 9/13 xalign 0.5 yanchor 0.5

    pause 0.5

    show poemline10 with gaussdissolve:
        ypos 10/13 xalign 0.5 yanchor 0.5

    pause

    python:
        inventory = oldinventory
        personalstats = oldpersonalstats
        playerparty = oldparty
        persondex = oldpersondex
        classstats = oldclassstats
        playercharacter = None
        AddEvent("Cheren", "Scene1")
        persondex["Cheren"]["RelationshipRank"] = 1
        maxliberationlimit += 20

    scene blank2 with splitfade

    narrator "As the enemy forces gather in the night, the banner of liberation flies higher, readying for the fight! Your resolve resonates through [pika_name]."
    narrator "[pika_name]'s Liberation Limit increased by [bluecolor]twenty{/color}!"

    return
