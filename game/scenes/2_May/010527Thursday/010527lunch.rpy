label lunch010527:

show whitney uniform with dis

pause 1.0

whitney @surprised "[first_name], am I crazy?"

menu:
    "[knowledgeoption]You're the nurse. You tell me.":
        $ TraitChange("Knowledge")

    "[patienceoption]Why do you say that?":
        $ TraitChange("Patience")

whitney @sweat talkingmouth "Okay, you're not going to believe this... but, I was just at the baseball field, right?"

red uniform @confused "With you so far."

whitney @talking2mouth "And then, I swear to god, I saw a Combee. It looked right at me, called me 'hot,' and then asked if I like jazz."

red @confused "On the baseball field? What were Combee doing on the baseball field? That's pretty far from the forest. How did they get on campus?"

whitney @angry "That's what you're concerned with?! Not that it called me hot? Combee shouldn't speak Japanese!"

red @happy "I mean, yeah. Can't fault it for speaking the truth, but it really shouldn't be that close to campus."

if (GetRelationshipRank("Whitney") > 0):
    $ ValueChange("Whitney", 1)

    whitney @talking2mouth "I mean, true. I {i}am{/i} hot. But I didn't realize that crossed species."

    red @happy "Hot's hot all over, I guess."

else:
    whitney @talking2mouth "You're a weird dude, [first_name]."

whitney @closedbrow talkingmouth "Anyway, I can't just stay away from the Baseball Field... I do everything there... but if you could come around some time and just help me prove I'm not crazy to myself, that'd be great."

red @happy "I'll keep that in mind."

hide whitney with dis

redmind @closedbrow frownmouth "All jokes aside, this could be a problem, if it's another Pokémon too far from home... it might be another F.O.E."

if (GetRelationshipRank("Sabrina") > 0):
    redmind @surprised "[sabrinacolor]No-one is going to call them F.O.E.s.{/color}"

    redmind @upeyes angryeyebrows frownmouth "Sabrina, if I'm the only one calling them, I can call them F.O.E.s. if I want to."

    redmind @closedbrow frownmouth "[sabrinacolor]It's forced.{/color}"

    red @closedbrow talking2mouth "Yeah, you've made your opinion of my naming abilities clear. Thanks."

jump PickTable