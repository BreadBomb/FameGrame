import math

import serial
from pygame import draw, gfxdraw, camera
import pygame

from views.AnimationView import AnimationView
from views.CenteredText import CenteredText
from views.ListView import ListView
from views.ScrollingText import ScrollingText


class Menu:
    def __init__(self, periphery):
        self.periphery = periphery

        self.buttonRect = pygame.Rect(0, 0, 4, 6)

        self.right_pressed = False

        self.test = pygame.Surface((16, 16))

        self.periphery.periphery_events.button1_pressed += self.button1_pressed
        self.periphery.periphery_events.button1_released += self.button1_released

        self.listView = ListView(periphery)
        self.listView.add(ScrollingText("test1", "assets/fonts/5x7.bdf", (255, 255, 255)))
        self.listView.add(ScrollingText("test2", "assets/fonts/5x7.bdf", (255, 255, 255)))

    def button1_pressed(self):
        self.right_pressed = True

    def button1_released(self):
        self.right_pressed = False

    def run(self, surface):
        self.listView.run(surface)


