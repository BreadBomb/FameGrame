from pygame import Color

from core import Renderer
from utils import Periphery
from views import View


class Application:
    def __init__(self):
        self.renderer = Renderer()
        self.periphery = Periphery()

        self.Content: View = None

        self.__running = False

    def start(self):
        self.__running = True
        self.run()

    def close(self):
        self.renderer.close()
        self.periphery.close()
        self.__running = False

    def run(self):
        while self.__running:
            if self.Content is not None:
                self.Content.run(self.renderer.Content)

            self.renderer.run()
            self.periphery.run()
