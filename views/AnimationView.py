import os
from datetime import datetime

import pygame

from views.view import View


class AnimationView(View):
    def __init__(self, folder):
        super().__init__()

        print("init AnimationView")

        self.images = []
        self.position = 1
        self.folder = folder

        for _ in os.listdir(self.folder):
            image_path = os.path.join(self.folder, "%d.bmp" % self.position)

            self.images.append(pygame.image.load(image_path))
            self.position += 1

        self.position = 1
        self.timer = datetime.now()

    def run(self, surface):
        if (datetime.now() - self.timer).total_seconds() > .05:
            if self.position == len(self.images) - 1:
                self.position = 1
            else:
                self.position += 1
            self.timer = datetime.now()

        surface.blit(self.images[self.position], (0, 0))
