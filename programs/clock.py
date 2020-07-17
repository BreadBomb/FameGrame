from datetime import datetime

from pygame.surface import Surface

from views import View
from views.ScrollingText import ScrollingText


class Clock(View):
    def __init__(self, periphery, program_manager):
        super().__init__()

        self.periphery = periphery
        self.program_manager = program_manager

        self.register_events()

    def register_events(self):
        self.periphery.periphery_events.button3_released += self.back

    def unregister_events(self):
        self.periphery.periphery_events.button3_released -= self.back

    def back(self):
        print("test")
        self.program_manager.back()

    def run(self, surface):

        test = Surface((31, 14))

        surface.fill((0, 0, 0))

        number = ScrollingText(datetime.now().strftime("%H:%M"), "assets/fonts/helvR12.bdf", (255, 255, 255))
        seconds = ScrollingText(datetime.now().strftime("%S"), "assets/fonts/helvR12.bdf", (255, 255, 255))
        seconds.run(test)

        surface.blit(test, (0, 13))

        number.run(surface)

        pass