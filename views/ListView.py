from pygame import gfxdraw, mask
from pygame.surface import Surface
from pygame.mask import Mask

from utils import ValueAnimation
from views.view import View


class ListView(View):
    def __init__(self, periphery):

        self.periphery = periphery

        self.items = []
        self.selected_index = 0

        self.periphery.periphery_events.rotary_big_ccw += self.list_down
        self.periphery.periphery_events.rotary_big_cw += self.list_up
        pass

    def list_up(self):
        self.selected_index -= 1

    def list_down(self):
        self.selected_index += 1

    def add(self, view: View):
        self.items.append(view)

    def run(self, surface):
        surface.set_at((31, 0), (255, 0, 0))
        surface.set_at((31, 31), (255, 0, 0))

        if len(self.items) > 0:
            bar_height = round(30 / len(self.items))
        else:
            bar_height = 30

        gfxdraw.line(surface, 31, 1, 31, 30, (0, 0, 0))
        bar_height_end = (1 + bar_height) * (1 + self.selected_index)
        if bar_height_end > 30:
            bar_height_end = 30
        gfxdraw.line(surface, 31, 1 + bar_height * self.selected_index, 31, bar_height_end, (0, 255, 0))

        pos = 0

        for item in self.items:
            test = Surface((31, 7))
            item.run(test)
            if pos == self.selected_index:
                m: Mask = mask.from_surface(test)
                m.invert()
                m.to_surface(test)
            surface.blit(test, (0, pos * 6))
            pos += 1
