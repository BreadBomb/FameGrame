import atexit
import os
import sys
import time

import pygame

from views.view import View

def goodbye():
    print("goodbye")
    pygame.display.quit()
    pygame.quit()
    sys.exit()


class Renderer:
    def __init__(self):
        self.useEmulator = os.getenv("EMULATOR") is not None

        self.__initialize()

        if self.useEmulator:
            self.size = (32, 32)
            self.screen = pygame.display.set_mode((512, 512))
            self.Content = pygame.Surface(self.size)
        else:
            self.size = (32, 32)
            self.Content = pygame.display.set_mode(self.size)

            from rgbmatrix import RGBMatrix
            self.matrix = RGBMatrix(options=self.__generateMatrixOptions())

    def __initialize(self):
        if not self.useEmulator:
            os.environ["SDL_VIDEODRIVER"] = "dummy"

        atexit.register(goodbye)

        pygame.init()

    def __generateMatrixOptions(self):
        from rgbmatrix import RGBMatrixOptions
        options = RGBMatrixOptions()
        options.rows = 32
        options.chain_length = 1
        options.parallel = 1
        options.hardware_mapping = 'regular'

        return options

    def run(self):
            if not self.useEmulator:
                for x in range(32):
                    for y in range(32):
                        color = self.Content.get_at((x, y))
                        self.matrix.SetPixel(x, y, color.r, color.g, color.b)
            else:
                pygame.transform.scale(self.Content, (512, 512), self.screen)

            pygame.display.flip()

