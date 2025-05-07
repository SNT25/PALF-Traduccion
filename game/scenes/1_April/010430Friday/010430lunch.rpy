label lunch010430:

show sabrina uniform with dis

pause 0.5

red uniform @talkingmouth "Hi, Sabrina."

sabrina @talking2mouth "...Hello."

pause 1.0

red @confused "Something I can help you with?"

sabrina @talking2mouth "...I have... a bad feeling."

red @closedbrow talking2mouth "A bad feeling? What do you mean?"

sabrina @talking2mouth "...I cannot describe it. Some Espers have extreme clairvoyance, but my powers are limited to telepathy and psychokinesis. I just... occasionally, get 'feelings' about the future."
sabrina @sad "I just... I see you being attacked... Some sort of battle."

menu:
    "{color=#ff8412}[[Courage]{/color} I'm not worried.":
        $ TraitChange("Courage")
        sabrina @talking2mouth "...I see."

    "{color=#66b77d}[[Knowledge]{/color} Do I win?":
        $ TraitChange("Knowledge")
        sabrina @talking2mouth "I don't know."

        redmind @thinking "Hm. Guess I'd better make sure my team is fully up to snuff, then. I've got a lot happening on Saturday and Sunday, so today might be the last day before Monday I have to prepare for the Quarter Qlashes next week."

sabrina @sad "Often, my... 'feelings' come to no account. But I thought you should know. As an apology for my outburst on Monday."

if (GetRelationship("Sabrina") == "Friend"):
    sabrina @talking2mouth blush "You are my friend, after all. If anyone should know if I have this feeling about you, it's you."

red @talkingmouth "Don't worry about it. I appreciate the heads-up, Sabrina."

redmind "[sabrinacolor]You're welcome.{/color}"

hide sabrina with dis

pause 1.0

if (starterobj in playerparty):
    $ starter_name = starterobj.GetNickname()
    $ starter_id = starterobj.Id
    $ starter_species_name = pokedexlookup(starter_id, DexMacros.Name)
    
    red @confused "Well... that's concerning. But you and I can beat anything, right, [starter_name]?"

    $ PlaySound("pokemon/cries/{}.mp3".format(starter_id))

    starter "[starter_species_name]!"

    red @happy "That's the spirit."

jump PickTable