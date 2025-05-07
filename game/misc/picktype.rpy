label PickType():
    call screen picktype(_with_none=False) with dissolve
    with dissolve
    "You want to choose from three Pokémon within the [_return] type?"

    menu:
        ">Yes":
            return _return

        ">No":
            jump PickType