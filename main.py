from easy_mobile.setup import *
from easy_mobile.tools import *
from easy_mobile.sprite import Sprite



screen = setup(win_width=2220,
               win_height=1080,
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


