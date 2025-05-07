label lunch010420:
    
narrator "You walk into the lunch hall, and begin to pick up some lunch, when, suddenly, you hear an ear-splitting screech behind you."

show nessa angry uniform at leftside with vpunch:
    xzoom -1

show sonia frownmouth at rightside with vpunch

nessa "SONIA?!"

sonia @surprisedmouth "Ah...? N-Nessa...?"

nessa "...Well?!"

sonia sadbrow "I... I..."

nessa "What do you have to say for yourself?! You went {i}completely{/i} silent!"
nessa "Leon got lost for {i}two weeks{/i} looking for you! Raihan posted {i}four{/i} crying selfies!"
nessa "Your gran kept asking where you were, and we didn't know what to tell her!"

sonia @neutralbrow surprisedmouth "No! No, Gran knew! I called her!"

nessa "{w=0.5}.{w=0.5}.{w=0.5}."
nessa @closedbrow angrymouth "Well. That's {i}good.{/i}"
nessa -angry frownmouth @talking2mouth "Still. You better have a good explanation for all this."

pause 1.0

redmind uniform @confusedeyebrows frownmouth "...Dare I involve myself in this drama?"

pause 1.0

if (GetRelationship("Nessa") != "Date"):
    redmind @happy "Oh, yeah, I totally dare."

    red @talkingmouth "Hey, Nessa."

    nessa @surprised "Huh? Oh, it's you, [first_name]."

    sonia @surprised "Oh! You're one of the lot I fought during the Battle Team tryouts, aren't you?"

    red @happy "Sure am. I guess this is the infamous ghost Sonia, Nessa?"

    nessa @closedbrow talking2mouth "Yes... the third of the Galarian Stars. Hmph."

    red @talkingmouth "Well, I'm sure there's a reasonable explanation for all of this. And let's not let quick feelings get in the way of a peaceful, long-term resolution, right?"

    nessa @angrybrow talking2mouth "...Fine. I'm willing to hear it."

    sonia sad "I... I just...{w=0.5} I can't."

    nessa @angry "What do you mean you {i}can't?!{/i}"

    sonia "I can't explain it. I'm sorry. I'm so sorry. I know I must seem like a proper prat, but I can't explain it."

    nessa "Just answer this for me, then. It's the twentieth. School started on the second. Did you seriously avoid me for eighteen days?"

    sonia @surprisedmouth "No! Of course not, Ness."

    nessa @angry "{i}Don't.{/i} We're not on nickname terms yet, {i}Sunny.{/i}"

    pause 1.0

    sonia @sad "I... I didn't actually intend to come back at all. I just... I was in the city, doing some shopping... when I heard cheers, and that wub-dub-dub music, from the stadium, and realized what day it was."
    sonia @surprised "And I thought... maybe, if I could try out for the Battle Team again... maybe I could still fulfill our dreams. The dreams we had back then. Do it properly, this time."

    pause 1.0

    nessa @talking2mouth "That dream's over."

    pause 1.0

    nessa @sad "Well... I thought it was. Until this guy and I had a talk. But that dream is {i}probably{/i} over."

    pause 2.0

    red @talkingmouth "Um... Sonia, was it? Do you mind if I ask a question? It might not really fit the mood, but I've gotta ask."

    $ beter = ("B" + first_name[1:] if first_name[0] not in ["B", 'b'] else "D" + first_name[1:])
    sonia @surprised "Right, go off. [beter], wasn't it? I heard some people talking over your campaign posters."

    red @talkingmouth "[first_name], actually, but that's not important. How are you paying for a second year at Kobukan? You aren't getting any financial aid, right?"
    red @talkingmouth "Are you, like... {i}uber{/i}-rich?"

    sonia @surprised "P-pay?"

    red @talkingmouth "Yeah. Kobukan's notoriously expensive. Most of the cost is waived for first-time students, but as far as I know, no returning student has ever had their fees waived."

    sonia @sad "...Bloody hell."

    sonia @happy "Somehow, in all the rush to get in here, I forgot about that. Advisor Lance talked to the Dean, and he let me rejoin, but... Leon paid the first time, but... this second time, I..."

    pause 1.0

    sonia sad "I'm proper sunk now, aren't I?"

    red @closedbrow talking2mouth "...Same boat here..."

    pause 1.0

    nessa @closedbrow talking2mouth "{i}Sigh.{/i} Let's get you sorted for electives."

    sonia -sad @surprisedmouth "Ness?"

    nessa @talkingmouth "We need to get you signed up for your next classes. You'll need to sign up for clubs, too. And we need to get you out of this old coat you always wear and into a uniform."
    nessa @surprised "You're such a hoarder, you probably never threw your old one away, right?"

    sonia -frownmouth @happybrow talkingmouth "Ness!"

    nessa @closedbrow talking2mouth "Yeah, yeah. Don't dally."

    pause 1.0

    nessa @talkingmouth "Hey, [first_name]. Thanks for... making sure I didn't do something I'd regret."

    red @talkingmouth "Nah, you're good. I just stood here. That was all you, Ness."

    nessa @closedbrow talkingmouth "Don't {i}you{/i} start."

    $ ValueChange("Nessa", 3, 0.25, False)
    $ ValueChange("Sonia", 3, 0.75, True)

else:
    redmind "Mmmm... no, I should probably stay away. I think I'll just avoid that table today."

    nessa @angrybrow talking2mouth "...Well? I'm willing to hear it."

    sonia sad "I... I just...{w=0.5} I can't."

    nessa @angry "What do you mean you {i}can't?!{/i}"

    sonia "I can't explain it. I'm sorry. I'm so sorry. I know I must seem like a proper prat, but I can't explain it."

    nessa "Just answer this for me, then. It's the twentieth. School started on the second. Did you seriously avoid me for eighteen days?"

    sonia @surprisedmouth "No! Of course not, Ness."

    nessa @angry "{i}Don't.{/i} We're not on nickname terms yet, {i}Sunny.{/i}"

    pause 1.0

    sonia @sad "I... I didn't actually intend to come back at all. I just... I was in the city, doing some shopping... when I heard cheers, and that wub-dub-dub music, from the stadium, and realized what day it was."
    sonia @surprised "And I thought... maybe, if I could try out for the Battle Team again... maybe I could still fulfill our dreams. The dreams we had back then. Do it properly, this time."

    pause 1.0

    nessa @talking2mouth "That dream's over."

    pause 1.0

    nessa @sad "...It's so like you to make a snap decision like this. I bet you haven't thought this through at all, have you? How are you even going to pay?"

    sonia @surprised "P-pay?"

    nessa @talking2mouth "Yeah. Kobukan's notoriously expensive. You're not a first-time student, so I don't see you getting any fee waivers. How are you going to pay in five months?"

    sonia @sad "...Bloody hell."

    sonia @happy "Somehow, in all the rush to get in here, I forgot about that. Advisor Lance talked to the Dean, and he let me rejoin, but..."

    pause 1.0

    sonia sad "I'm proper sunk now, aren't I?"

    pause 1.0

    nessa @closedbrow talking2mouth "{i}Sigh.{/i} Let's get you sorted for electives."

    sonia -sad @surprisedmouth "Ness?"

    nessa @talkingmouth "We need to get you signed up for your next classes. You'll need to sign up for clubs, too. And we need to get you out of this old coat you always wear and into a uniform."
    nessa @surprised "You're such a hoarder, you probably never threw your old one away, right?"

    sonia -frownmouth @happybrow talkingmouth "Ness!"

    nessa @closedbrow talking2mouth "Yeah, yeah. Don't dally."

hide nessa
hide sonia 
with dis

jump PickTable