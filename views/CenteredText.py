from datetime import datetime

import pygame
from pygame import freetype

from views.view import View


class CenteredText(View):
    def __init__(self, text, font_path, surface_width, fgcolor):
        self.text = text

        if not freetype.get_init():
            freetype.init()

        self.font = freetype.Font(font_path)

        self.rendered_text, self.rendered_rect = self.font.render(self.text, fgcolor)
        self.fgcolor = fgcolor
        self.rendered_rect.y = 0
        self.rendered_rect.x = (surface_width - self.rendered_rect.width)/2

    def set_text(self, text):
        x = self.rendered_rect.x
        y = self.rendered_rect.y
        self.rendered_text, self.rendered_rect = self.font.render(text, self.fgcolor, (0, 0, 0, 255))
        self.rendered_rect.x = x
        self.rendered_rect.y = y

    def run(self, surface):
        surface.blit(self.rendered_text, self.rendered_rect)
