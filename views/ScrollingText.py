from datetime import datetime

import pygame
from pygame import freetype

from views.view import View


class ScrollingText(View):
    def __init__(self, text, font_path, fgcolor=None, speed=10):
        self.text = text

        if not freetype.get_init():
            freetype.init()

        self.font = freetype.Font(font_path)
        self.speed = speed

        self.delay = True
        self.direction = -1

        self.rendered_text, self.rendered_rect = self.font.render(self.text, fgcolor)
        self.fgcolor = fgcolor
        self.timer = datetime.now()
        self.rendered_rect.x = 0
        self.rendered_rect.y = 0

    def run(self, surface):
        if self.delay and (datetime.now() - self.timer).total_seconds() > 2:
            self.delay = False
            self.timer = datetime.now()

        if not self.delay and (datetime.now() - self.timer).total_seconds() > .5 / self.speed and self.rendered_rect.width > surface.get_rect().width:
            self.rendered_rect = self.rendered_rect.move([self.direction, 0])
            self.timer = datetime.now()

            if self.rendered_rect.width - surface.get_rect().width + self.rendered_rect.x == 0:
                self.delay = True
                self.direction = 1

            if self.rendered_rect.x == 0 and self.direction == 1:
                self.delay = True
                self.direction = -1

            self.rendered_text, _ = self.font.render(self.text, self.fgcolor)

        surface.blit(self.rendered_text, self.rendered_rect)
