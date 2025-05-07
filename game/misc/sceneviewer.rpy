label sceneviewerpreload:
$ persistent.sceneviewer = True
narrator "Select Save File"
call screen load

label sceneviewerafterload:
    stop music fadeout 2.0
    python:
        persistent.sceneviewer = False
        sceneviewer = True
        scenes = GetSeenScenes()
        if len(scenes) == 0:
            renpy.say(None, "This save file does not have any scenes seen.")
            MainMenu(confirm=False)()
        scene = renpy.display_menu(list(zip(scenes, scenes)))
        renpy.block_rollback()
        renpy.jump(scene)
