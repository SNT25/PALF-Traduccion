label lunch010414:

redmind uniform @thinking "Ugh. I need a big meal to distract myself from Nessa the good-time ruiner."

show whitney sadbrow frownmouth uniform with vpunch

whitney @sad "[first_name]! I need you to bail me out {i}right now!{/i}"

red @surprised "Huh? What is it?"

whitney @sad "Tia's driving me absolutely {i}crazy.{/i} Every free moment I have, she's been yelling at me about wanting to see you!"

red @confusedeyebrows talking2mouth "Yelling?"

whitney @angry "Look, she signs {i}really{/i} loudly, alright? And I'm {i}way{/i} more out of practice than I thought I was. And she's {i}really{/i} chatty!"

red @happy "Well, I {i}do{/i} owe you. What can I do for you?"

whitney @sad "Just sit at our table, and take some of her heat off of me. You don't even have to talk to her, just {i}be{/i} there. I'm begging you."

python:
    tablevalid = True
    for i, character in enumerate(["Whitney", "Gardenia", "Bianca", "Leaf", "Tia"]):
        value = (persondex[character]["Value"] if character in persondex.keys() and "Value" in persondex[character].keys() else 0)
        if (value < 1):
            tablevalid = False

if (not tablevalid):
    red @sadeyes sadeyebrows happymouth "Ah, geez... I'm not sure. I don't think that table is, uh... y'know... ready for me. I like to be more familiar with people at the tables I sit at."
    red @closedbrow talking2mouth "I have to consider the possible desolation of my social standing, you know. Anything could happen when you sit at an unsecured table."

    whitney @surprised "You pledged a life-debt to a girl you barely know, but you draw the line at sitting at a table with a couple strangers?"

    red @confusedeyebrows talking2mouth "Life-debt? Is that what Tia told you?"

    whitney @angry "Look, I'll just social butterfly all over them and talk you up! Just get in there!"

    python:
        for i, character in enumerate(["Gardenia", "Bianca", "Whitney", "Leaf", "Tia"]):
            value = (persondex[character]["Value"] if character in persondex.keys() and "Value" in persondex[character].keys() else 0)
            if (value < 1):
                ValueChange(character, 1, (i + 1) / 6, False)
                persondex[character]["Value"] = 1

    narrator "You feel as though Whitney's table is suddenly far more accepting of your presence."

    red @surprised "Huh... Neat trick, that. In that case..."

red @happy "I'll do my best!"

hide whitney with dis

jump PickTable