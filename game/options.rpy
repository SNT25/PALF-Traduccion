## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Pokemon Academy Life Forever")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = True


## The version of the game.

define config.version = "12.23b.2024"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "PokemonAcademyLifeForever"


## Sounds and music ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

# define config.main_menu_music = "main-menu-theme.ogg"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 90
default preferences.skip_unseen = False
default preferences.skip_after_choices = True

## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "PokemonAcademyLifeForever-1669680814"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.webp"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    """
    build.archive("PALF","all")
    build.archive("scripts", "all")
    build.archive("images", "all") #the 3 .rpa files to use

    build.classify('**~', None) #everything that will be excluded
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.classify('**.md', None)
    build.classify('**.pdf', None)
    build.classify('**.psd', None)
    build.classify('**.doc', None)
    build.classify('**.txt', None)
    build.classify('**.xlsx',None)
    build.classify('game/**.rpy', None)
    build.classify('game/scripts/**.rpy', None)

    build.classify("game/**.rpyc", "scripts") #all script files are in scripts.rpa
    build.classify("game/**.jpg", "images") #all images are in images.rpa
    build.classify("game/**.png", "images")
    build.classify("game/**.webp", "images")
    build.classify("game/**.webm", "images")
    build.classify('**/**.**', "PALF") #everything left over in PALF.rpa

    """

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"

define config.say_attribute_transition = Dissolve(0.25)
define config.say_attribute_transition_layer = "master"

transform change_transform(old, new):
    contains:
        (Flatten(old) if showredonly and old == "red" or not showredonly else Null())
        alpha 1.0
        linear 0.25 alpha 0.0
    contains:
        Flatten(new)
        alpha 0.0
        linear 0.25 alpha 1.0

transform same_transform(old, new):
    Flatten(old)
    Flatten(new) with Dissolve(0.25)

transform flattener(new):
    Flatten(new)

define config.side_image_same_transform = same_transform
define config.side_image_change_transform = change_transform
define config.side_image_only_not_showing = True

init -1 python hide:
    style.menu_choice_button.background = Frame("GUI/Choice_Idle.webp",10,10)
    style.menu_choice_button.hover_background = Frame("GUI/Choice_Hover.webp",10,10)
    style.menu_choice_button.yminimum = 85 #Sets height, recommended to be the exact height of your image
    style.menu_choice_button.xminimum = 800
    style.menu_choice_button.xalign = 0.5

    ##Modifies the Menu Choice's Text
    style.menu_choice.color = "#000000"
    style.menu_choice.size = 30
    style.menu_choice.yoffset = 8
    style.menu_choice.font = "fonts/pkmndp.ttf"
    style.menu_choice.xalign = 0.5

    style.file_picker_button.color = "#c25fb9"

define config.main_menu_music = "Audio/Music/Shelf of Memories (Prelude).ogg"
define config.font_replacement_map["fonts/pkmndp.ttf", True, False] = ("fonts/pkmndpb.ttf", False, False)

define config.return_not_found_label = "notfoundlabel"

define config.layers = [ 'undermaster', 'undersayer', 'master', 'arrowlayer', 'transient', 'screens', 'overlay' ]