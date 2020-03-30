from datetime import datetime

import pygame
from pygame import freetype

from views.View import View


class ScrollingText(View):
    def __init__(self, text, font_path, pos=(0, 0), fgcolor=None, speed=1):
        self.text = text
        self.pos = pos

        if not freetype.get_init():
            freetype.init()

        self.font = freetype.Font(font_path)
        self.speed = speed

        self.delay = True
        self.direction = -1

        self.rendered_text, self.rendered_rect = self.font.render(self.text, fgcolor)
        self.fgcolor = fgcolor
        self.timer = datetime.now()
        self.rendered_rect.x = pos[0]
        self.rendered_rect.y = pos[1]

    def run(self, surface):
        if self.delay and (datetime.now() - self.timer).total_seconds() > 2:
            self.delay = False
            self.timer = datetime.now()

        if not self.delay and (datetime.now() - self.timer).total_seconds() > .5 / self.speed:
            self.rendered_rect = self.rendered_rect.move([self.direction, 0])
            self.timer = datetime.now()

            if self.rendered_rect.width - surface.get_rect().width + self.rendered_rect.x == 0:
                self.delay = True
                self.direction = 1

            if self.rendered_rect.x == 0 and self.direction == 1:
                self.delay = True
                self.direction = -1

        self.rendered_text.fill((0, 0, 0, 255))
        surface.blit(self.rendered_text, self.rendered_rect)
        self.rendered_text, _ = self.font.render(self.text, self.fgcolor)
        surface.blit(self.rendered_text, self.rendered_rect)
