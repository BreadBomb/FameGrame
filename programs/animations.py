import os
from datetime import datetime, timedelta

import configparser
import pygame


class Animation:
    def __init__(self, path, hold, loop, frame_count):
        self.path = path
        self.hold = hold
        self.loop = loop
        self.frame_count = frame_count


class Animations:
    def __init__(self, periphery):
        self.periphery = periphery

        self.path = "assets/animations/animations"

        self.animations = self.read_animations()

        self.current_frame = 0
        self.current_animation_index = 0
        self.current_animation = self.animations[self.current_animation_index]

        self.frame_time = None
        self.image_time = None

        self.image_seconds = 30

        self.periphery.periphery_events.rotary_big_cw += self.next_animation
        self.periphery.periphery_events.rotary_big_ccw += self.previous_animation

    def next_animation(self):
        self.image_time = datetime.now()
        self.current_frame = 0
        self.frame_time = None
        self.current_animation_index += 1
        self.current_animation = self.animations[self.current_animation_index]

    def previous_animation(self):
        self.image_time = datetime.now()
        self.current_frame = 0
        self.frame_time = None
        self.current_animation_index -= 1
        self.current_animation = self.animations[self.current_animation_index]

    def read_animations(self):
        animations = []
        for animation in os.listdir(self.path):
            folderPath = os.path.join(self.path, animation)
            configPath = os.path.join(folderPath, "config.ini")
            config = configparser.ConfigParser()
            config.read(configPath)

            print(animation)

            frame_count = len([f for f in os.listdir(folderPath) if os.path.isfile(os.path.join(folderPath, f))]) - 1

            animation = Animation(folderPath, config["animation"]["hold"], config["animation"]["loop"], frame_count)
            animations.append(animation)

        return animations

    def run(self, surface):
        if self.frame_time is None:
            self.frame_time = datetime.now()
        if self.image_time is None:
            self.image_time = datetime.now()

        if self.frame_time + timedelta(milliseconds=int(self.current_animation.hold)) < datetime.now():
            self.frame_time = datetime.now()
            self.current_frame += 1

            if self.current_frame == self.current_animation.frame_count:
                self.current_frame = 0

        if self.image_time + timedelta(seconds=self.image_seconds) < datetime.now():
            self.image_time = datetime.now()
            self.current_frame = 0
            self.frame_time = None
            self.current_animation_index += 1
            self.current_animation = self.animations[self.current_animation_index]

        if self.current_animation_index == len(self.animations) - 1:
            self.current_animation_index = 0
            self.current_animation = self.animations[self.current_animation_index]

        rect = pygame.Rect(0, 0, 32, 32)
        image = pygame.image.load(os.path.join(self.current_animation.path, "%d.bmp" % self.current_frame))
        image = pygame.transform.scale(image, (32, 32))

        surface.blit(image, rect)

        return
