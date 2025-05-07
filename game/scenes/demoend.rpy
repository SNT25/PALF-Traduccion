label demoend:
label enddemo:

narrator "{b}Wait!{/b} If you want your save to be compatible with the next version, then press \"Back\" at the bottom of the screen, and save before this dialogue box shows up."
narrator "I repeat, as of this textbox, {b}it is too late to save your game! You must reverse.{/b}"

pause 1.0

narrator "...Alright, let's continue."

$ renpy.pause(0.1, hard=True)

scene blank2

show blue with dis:
    xpos 700

stop music fadeout 1.0
play music "audio/music/SoaringDreams_Start.ogg" noloop
queue music "audio/music/SoaringDreams_Loop.ogg" 

$ renpy.pause(1.0, hard=True)

blue @talkingmouth "Great. Time for the {i}theater{/i} arc, I guess. That's just awesome. Love getting sidelined so Mr. Protag can put on a skirt and shake his ass."

show leaf with dis:
    xpos 1050

leaf @talking2mouth "{i}I'd totally watch that.{/i}"

blue @closedbrow talking2mouth "Well, I'm just clocking out of this storyline. Tell me when the alien comes back. I've got a Left for it, too."

hide blue with dis

pause 0.5

show ethan with dis:
    xpos 700

ethan @talkingmouth "Hey, I'll take his place! I--"

hide ethan 
show blue:
    xpos 700
with vpunch

blue @surprised "Nevermind! We can't let Ethan show up in the credits."

ethan @angry "Why not?!"

blue @surprised "I dunno. It's tradition or something at this point."

leaf @sarcastic "Let's just do the outro blurb. Protagonist, over here!"

show red behind blue with dis:
    xpos 450

pause 0.1
    
red @talkingmouth "The demo ends here, but there's a {i}lot{/i} more currently under development and on the way!"

leaf @talking2mouth "As the game goes on, the choices you make will have even more impact.{w=0.25}{nw}"
extend @flirttalk " We've barely scratched the surface!"

blue @closedbrow talkingmouth "Pretty sure that's not true anymore."

show leaf happy with dis

show gardenia:
    alpha 0.0 xpos 1250
    linear 0.75 alpha 1.0
show brendan behind red:
    alpha 0.0 xpos 1600
    pause 0.4
    linear 0.6 alpha 1.0
show dawn:
    alpha 0.0 xpos 1450
    pause 0.5
    linear 0.5 alpha 1.0 
show cheren behind leaf:
    alpha 0.0 xpos 200
    pause 0.25
    linear 0.4 alpha 1.0 
show serena behind gard1:
    alpha 0.0 xpos 875
    pause 0.6
    linear 0.7 alpha 1.0

red @talkingmouth "Your choices will determine who you meet..."
    
show gardenia:
    xpos 1250 alpha 1.0
    ease 0.5 xpos 1280

gardenia @happy "And you can't just find everyone right away!"

dawn @sadbrow talking2mouth "Um... there's probably a bunch of people you haven't met in the electives... so, um, if you want to go back and do that?"

show gardenia:
    xpos 1280
    ease 0.5 xpos 1250

show dawn:
    xpos 1450
    pause 0.25
    ease 0.5 xpos 1420
    
cheren @sadmouth "Sometimes it comes down to your choices. And sometimes you just need to be patient."

brendan @closedbrow talkingmouth "Uhh...{w=0.5} I'm not really sure how to say this...{w=0.5}{nw}"
extend happy " But good luck!"

show dawn:
    xpos 1420
    ease 0.5 xpos 1450

show cheren:
    xpos 200
    pause 0.25
    ease 0.5 xpos 150

cheren @sadmouth "You can check on development updates via the {a=https://discord.gg/RRd2Srjp7n}official discord{/a} or the {a=https://www.pokecommunity.com/showthread.php?t=493106}PokéCommunity{/a} forum."

show cheren:
    xpos 150
    ease 0.5 xpos 200

show serena:
    xpos 875
    pause 0.25
    ease 0.5 xpos 905
    
serena @talkingmouth "Or if you prefer social media, follow the Pokémon Visual {a=https://twitter.com/pokemonvisual}Twitter{/a} account, or shoot a message to the {a=https://www.youtube.com/@PokemonVisual}YouTube Channel{/a}."

cheren @sadmouth "There are a few other platforms that might bear the project's name--a Facebook, or a website, for example..."

show serena surprisedbrow frownmouth
show cheren surprisedbrow frownmouth
with dis

blue @angry "But you won't get shit from those! We don't even own them anymore!" 

blue @closedbrow talkingmouth "Just jump on the discord, alright? {a=https://discord.gg/RRd2Srjp7n}Here's the link,{/a} again, in case you missed it the first time."

show cheren -surprisedbrow -frownmouth -surprised with dis
show serena -surprisedbrow -frownmouth -surprised with dis:
    xpos 905
    ease 0.5 xpos 875

show brendan:
    xpos 1600
    pause 0.25
    ease 0.5 xpos 1640

brendan @talking2mouth "Make sure you report any bugs or anything weird in general! You can reach out to the creator with the previous links."

brendan happy "Or you can send an email to 'pokemonvisualdev@gmail.com.'"

show brendan:
    xpos 1640
    ease 0.5 xpos 1600

red @talkingmouth "Suggestions are also more than welcome, by the way."
show red happy with dis

show serena happy
show blue happy
show dawn happy
show gardenia happy 
show cheren happy
with dis

leaf @happybrow talkingmouth "Thanks for playing!"

pause 0.25

window hide
stop music fadeout 1.5

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_23

scene blank2 with transball
$ renpy.pause(1.0, hard=True)

pause 1.0

show mallow with dis

mallow @happy "Hey, guys! I'm here to do the outro!"

pause 2.0

mallow "{w=0.5}.{w=0.5}.{w=0.5}."
mallow @surprised "Guys?"

pause 2.0

mallow @sadbrow talkingmouth "Maybe I'm early...?"

pause 2.0

$ renpy.music.stop(channel='crowd', fadeout=1.0)

$ renpy.movie_cutscene('images/videos/Credits.webm')

show screen credits with dissolve

pause 60

hide screen credits

stop music

$ MainMenu(confirm=False)()