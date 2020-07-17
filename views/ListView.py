from pygame import gfxdraw, Color, time
from pygame.surface import Surface
from events import Events

from utils import ValueAnimation
from views.view import View


class ListView(View):
    def __init__(self, periphery):
        super().__init__()

        self.periphery = periphery

        self.items = []
        self.selected_index = 0

        self.buttonPressed = False

        self.events = Events()

    def register_events(self):
        self.periphery.periphery_events.rotary_big_ccw += self.list_down
        self.periphery.periphery_events.rotary_big_cw += self.list_up
        self.periphery.periphery_events.button2_pressed += self.click
        self.periphery.periphery_events.button2_released += self.released

    def unregister_events(self):
        self.periphery.periphery_events.rotary_big_ccw -= self.list_down
        self.periphery.periphery_events.rotary_big_cw -= self.list_up
        self.periphery.periphery_events.button2_pressed -= self.click
        self.periphery.periphery_events.button2_released -= self.released

    def released(self):
        self.events.on_click()
        self.buttonPressed = False

    def click(self):
        self.buttonPressed = True

    def list_up(self):
        if self.selected_index > 0:
            self.selected_index -= 1

    def list_down(self):
        if self.selected_index < len(self.items) - 1:
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
            test = Surface((31, 6))
            if pos == self.selected_index and not self.buttonPressed:
                test.fill(Color((100, 0, 0)))
            elif pos == self.selected_index and self.buttonPressed:
                test.fill(Color((150, 0, 0)))
            item.run(test)
            surface.blit(test, (0, pos * 7))
            pos += 1
