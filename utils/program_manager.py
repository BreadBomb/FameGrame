from pygame import Color

from views import View


class ProgramManager(View):
    def __init__(self):
        super().__init__()
        self._last_program = None
        self._current_program = None

        self.clear = False

    def set_program(self, program):
        self.clear = True
        if self._current_program is not None:
            self._last_program = self._current_program
            self._current_program.unregister_events()
        self._current_program = program

    def back(self):
        self.clear = True
        temp = self._last_program
        self._last_program = self._current_program
        self._last_program.unregister_events()
        self._current_program = temp
        self._current_program.register_events()
        pass

    def run(self, surface):
        if self.clear:
            surface.fill(Color((0, 0, 0)))
            self.clear = False
        self._current_program.run(surface)
