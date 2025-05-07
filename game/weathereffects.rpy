init:
    image rain = CustomSnowBlossom("images/GFX/Raindrop.webp", count=20, border=1000, xspeed=(0, 10), yspeed=(2500,5000))
    transform thirtydegrees:
        xalign 0.3
        xanchor 0.5
        rotate 30
    image snow = CustomSnowBlossom("images/GFX/Snow.webp", count=1)
    image blizzard = CustomSnowBlossom("images/GFX/Snow.webp", count=20, border=1000, xspeed=(0, 10), yspeed=(1500, 3000))
    transform sixtydegrees:
        yalign 0.2
        yanchor 0.5
        rotate 60
    image ash = CustomSnowBlossom("images/GFX/Ash.webp", count=1)
    image sand = CustomSnowBlossom("images/GFX/Sand.webp", count=3, border=500, xspeed=(0, 10), yspeed=(1000))
    transform ninetydegrees:
        yalign 0.3
        yanchor 0.5
        rotate 90

label cloudytest:
    show fields1
    show rain at thirtydegrees 
    red @talkingmouth "Man it sure is rainy here"
    hide rain

label snowtest:
    show fields1
    show snow
    red @talkingmouth "Man it sure is snowy here"
    hide snow

label blizzardtest:
    show fields1
    show blizzard at sixtydegrees
    red @talkingmouth "Man it sure is snowy here"
    hide blizzard

label ashtest:
    show fields1
    show ash
    red @talkingmouth "Man it sure is ashy here"
    hide ash

label sandtest:
    show fields1
    show sand at ninetydegrees
    red @talkingmouth "Man it sure is sandy here"
    hide sand





init -1 python:
    class CustomSnowBlossomFactory():

        rotate = False

        def __setstate__(self, state):
            self.start = 0
            vars(self).update(state)
            self.init()

        def __init__(self, image, count, xspeed, yspeed, border, rotate=False):
            self.image = renpy.easy.displayable(image)
            self.count = count
            self.xspeed = xspeed
            self.yspeed = yspeed
            self.border = border
            self.rotate = rotate

        def create(self, particles, st):

            def ranged(n):
                if isinstance(n, tuple):
                    return random.uniform(n[0], n[1])
                else:
                    return n

            rv = [ ]

            for _i in range(0, self.count):
                rv.append(CustomSnowBlossomParticle(self.image,
                                            ranged(self.xspeed),
                                            ranged(self.yspeed),
                                            self.border,
                                            st,
                                            random.uniform(0, 100),
                                            rotate=self.rotate))
            return rv

        def predict(self):
            return [ self.image ]


    class CustomSnowBlossomParticle():

        def __init__(self, image, xspeed, yspeed, border, start, offset, rotate):

            # safety.
            if yspeed == 0:
                yspeed = 1

            self.image = image
            self.xspeed = xspeed
            self.yspeed = yspeed
            self.border = border
            self.start = start
            self.offset = offset
            self.rotate = rotate

            if not rotate:
                sh = renpy.config.screen_height
                sw = renpy.config.screen_width
            else:
                sw = renpy.config.screen_height
                sh = renpy.config.screen_width

            if self.yspeed > 0:
                self.ystart = -border
            else:
                self.ystart = sh + border

            travel_time = (2.0 * border + sh) / abs(yspeed)

            xdist = xspeed * travel_time

            x0 = min(-xdist, 0)
            x1 = max(sw + xdist, sw)

            self.xstart = random.uniform(x0, x1)

        def update(self, st):
            to = st - self.start

            xpos = self.xstart + to * self.xspeed
            ypos = self.ystart + to * self.yspeed

            if not self.rotate:
                sh = renpy.config.screen_height
            else:
                sh = renpy.config.screen_width

            if ypos > sh + self.border:
                return None

            if ypos < -self.border:
                return None

            if not self.rotate:
                return int(xpos), int(ypos), to + self.offset, self.image
            else:
                return int(ypos), int(xpos), to + self.offset, self.image


    def CustomSnowBlossom(d,
                    count=10,
                    border=50,
                    xspeed=(20, 50),
                    yspeed=(100, 200),
                    start=0,
                    horizontal=False):
        """
        :doc: sprites_extra

        The CustomSnowBlossom effect moves multiple instances of a sprite up,
        down, left or right on the screen. When a sprite leaves the screen, it
        is returned to the start.

        `d`
            The displayable to use for the sprites.

        `border`
            The size of the border of the screen. The sprite is considered to be
            on the screen until it clears the border, ensuring that sprites do
            not disappear abruptly.

        `xspeed`, `yspeed`
            The speed at which the sprites move, in the horizontal and vertical
            directions, respectively. These can be a single number or a tuple of
            two numbers. In the latter case, each particle is assigned a random
            speed between the two numbers. The speeds can be positive or negative,
            as long as the second number in a tuple is larger than the first.

        `start`
            The delay, in seconds, before each particle is added. This can be
            allows the particles to start at the top of the screen, while not
            looking like a "wave" effect.

        `fast`
            If true, particles start in the center of the screen, rather than
            only at the edges.

        `horizontal`
            If true, particles appear on the left or right side of the screen,
            rather than the top or bottom.
            """

        # If going horizontal, swap the xspeed and the yspeed.
        if horizontal:
            xspeed, yspeed = yspeed, xspeed

        return Particles(CustomSnowBlossomFactory(image=d,
                                            count=count,
                                            border=border,
                                            xspeed=xspeed,
                                            yspeed=yspeed,
                                            rotate=horizontal))
