import atexit
import os
import sys
import time

import pygame
from setuptools.command.setopt import option_base

from views.view import View


class Renderer:
    def __init__(self):
        self.useEmulator = os.getenv("EMULATOR") is not None

        if not self.useEmulator:
            os.environ["SDL_VIDEODRIVER"] = "dummy"
            os.environ['SDL_AUDIODRIVER'] = 'dsp'

        pygame.init()

        if self.useEmulator:
            self.size = (32, 32)
            self.screen = pygame.display.set_mode((512, 512))
            self.Content = pygame.Surface(self.size)
        else:
            self.size = (32, 32)
            self.Content = pygame.display.set_mode(self.size)

            from rgbmatrix import RGBMatrix
            self.matrix = RGBMatrix(options=self.__generateMatrixOptions())
            self.canvas = self.matrix.CreateFrameCanvas()

    def __generateMatrixOptions(self):
        from rgbmatrix import RGBMatrixOptions
        options = RGBMatrixOptions()
        options.rows = 32
        options.chain_length = 1
        options.parallel = 1
        options.hardware_mapping = 'regular'
        options.pwm_lsb_nanoseconds = 160
        options.brightness = 100
        options.drop_privileges = False

        return options

    def run(self):
        if self.useEmulator:
            pygame.transform.scale(self.Content, (512, 512), self.screen)
            pygame.display.flip()
        else:
            pygame.display.flip()
            for x in range(32):
                for y in range(32):
                    color = self.Content.get_at((x, y))
                    self.canvas.SetPixel(x, y, color.r, color.g, color.b)
            self.matrix.SwapOnVSync(self.canvas)

    def close(self):
        pygame.display.quit()
        pygame.quit()
