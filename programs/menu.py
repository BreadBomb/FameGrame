import pygame

from programs.animations import Animations
from programs.clock import Clock
from programs.tetris import Tetris
from views.ListView import ListView
from views.ScrollingText import ScrollingText


class Menu:
    def __init__(self, periphery, program_manager):
        self.periphery = periphery
        self.program_manager = program_manager

        self.buttonRect = pygame.Rect(0, 0, 4, 6)
        self.right_pressed = False
        self.test = pygame.Surface((16, 16))
        self.listView = ListView(self.periphery)

        self.listView.add(ScrollingText("Animationen", "assets/fonts/5x7.bdf", (255, 255, 255)))
        self.listView.add(ScrollingText("Uhrzeit", "assets/fonts/5x7.bdf", (255, 255, 255)))
        self.listView.add(ScrollingText("Tetris", "assets/fonts/5x7.bdf", (255, 255, 255)))

        self.register_events()

    def register_events(self):
        self.listView.register_events()
        self.listView.events.on_click += self.on_item_click

    def on_item_click(self):
        index = self.listView.selected_index
        print(index)
        if index == 0:
            self.program_manager.set_program(Animations(self.periphery, self.program_manager))
        if index == 1:
            self.program_manager.set_program(Clock(self.periphery, self.program_manager))
        if index == 2:
            self.program_manager.set_program(Tetris(self.periphery, self.program_manager))

    def run(self, surface):
        self.listView.run(surface)

    def unregister_events(self):
        self.listView.unregister_events()
        self.listView.events.on_click -= self.on_item_click


