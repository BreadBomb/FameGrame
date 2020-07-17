from core import bootstrap_application
from core import Application
from programs.animations import Animations
from programs.menu import Menu
from utils.program_manager import ProgramManager


class Main(Application):
    def __init__(self):
        super().__init__()

        program_manager = ProgramManager()
        program_manager.set_program(Menu(self.periphery, program_manager))

        self.Content = program_manager


if __name__ == "__main__":
    bootstrap_application(Main)
