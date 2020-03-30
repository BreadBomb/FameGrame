import os
import subprocess

from programs.setup import Setup
from renderer import Renderer
from views.AnimationView import AnimationView
from views.CenteredText import CenteredText
from views.ScrollingText import ScrollingText


def main():
    renderer = Renderer()

    # out = subprocess.run(['/usr/bin/create_ap', '-n', '--daemon', 'wlan0', 'FameGrame', 'fgwifilol'])

    # print(out.stdout)

    setup = Setup(renderer.Content.get_rect().width)

    while 1:
        # animation.run(renderer.Content)
        # connect.run(renderer.Content)
        # scrollingText.run(renderer.Content)
        setup.run(renderer.Content)

        renderer.run()


if __name__ == "__main__":
    main()
