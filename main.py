import time

import pygame
import pygame.freetype

from renderer import Renderer
from views.view import View


def main():
    renderer = Renderer()

    pygame.freetype.init()

    font = pygame.freetype.Font("./fonts/7x14B.bdf")

    test = pygame.Surface((32, 32))

    renderer.Content = test

    cube = pygame.Surface((2, 2))
    cubeRect = cube.get_rect()

    while 1:
        cubeRect = cubeRect.move([1, 1])
        test.fill((255, 0, 0, 0))
        cube.fill((0, 255, 0, 0))
        test.blit(cube, cubeRect)
        font.render_to(test, (3, 0), "DAMN")

        time.sleep(.2)

        renderer.run()


if __name__ == "__main__":
    main()
