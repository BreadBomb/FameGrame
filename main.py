from core import bootstrap_application
from core import Application
from programs.animations import Animations
from programs.menu import Menu


class Main(Application):
    def __init__(self):
        super().__init__()

        menu = Animations(self.periphery)

        self.Content = menu


if __name__ == "__main__":
    bootstrap_application(Main)
