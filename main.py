from easy_sdl.setup import *
from easy_sdl.tools import *
from easy_sdl.sprite import Sprite



screen = setup(win_width=1200,
               win_height=800,
               level_width=4440,
               level_height=2160)


screen.append(Sprite(512, 512, image="brick.png"))
screen.append(Sprite(768, 512, image="brick.png"))
screen.append(Sprite(1024, 512, image="brick.png"))
screen.append(Sprite(512, 256, image="brick.png"))
screen.append(Sprite(512, 0, image="brick.png"))
player = Sprite(0, 0, image="fatbot.png")
screen.append(player)


def f():
    player.move(2, 1)
    screen.focus(player)

screen.run(f)


