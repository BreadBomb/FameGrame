import serial
import serial.tools.list_ports
from events import Events
import os
import pygame
from utils import ValueAnimation


class Periphery:
    def __init__(self):
        # ports = serial.tools.list_ports.comports()

        # print(list(ports))

        if os.getenv("SERIAL_PORT") is not None:
            port = os.getenv("SERIAL_PORT")
        else:

            port = "/dev/ttyUSB0"

        self.ser = serial.Serial(port, baudrate=9600, timeout=1)

        self.periphery_events = Events()

        if not self.ser.is_open:
            self.ser.open()

        self.button1Pressed = False
        self.button2Pressed = False
        self.button3Pressed = False

        self.angleX = 0
        self.angleY = 0
        self.angleZ = 0

        self.led_color: pygame.Color = pygame.Color(0, 0, 0)
        self.led_animation = None

        self.rotary_last_direction = 0
        self.rotary_step_count = 0

    def close(self):
        self.ser.close()

    def set_led(self, color: pygame.Color):
        self.stop_led_animation()
        self.led_color = color
        self.ser.write(bytes([self.led_color.r, self.led_color.g, self.led_color.b]))

    def stop_led_animation(self):
        self.led_animation = None

    def set_led_animation(self, properties, duration):
        self.led_animation = ValueAnimation(self.led_color, properties, duration)

    def run(self):
        if not self.ser.isOpen():
            return
        line = self.ser.readline()
        try:
            data = line.decode().split(",")
            if data[0] == "1" and not self.button1Pressed:
                self.button1Pressed = True
                self.periphery_events.button1_pressed()
            if data[0] == "0" and self.button1Pressed:
                self.button1Pressed = False
                self.periphery_events.button1_released()
            if data[1] == "1" and not self.button2Pressed:
                self.button2Pressed = True
                self.periphery_events.button2_pressed()
            if data[1] == "0" and self.button2Pressed:
                self.button2Pressed = False
                self.periphery_events.button2_released()
            if data[2] == "1" and not self.button3Pressed:
                self.button3Pressed = True
                self.periphery_events.button3_pressed()
            if data[2] == "0" and self.button3Pressed:
                self.button3Pressed = False
                self.periphery_events.button3_released()
            if data[3] == "1":
                if self.rotary_last_direction == 1:
                    self.rotary_step_count += 1
                if self.rotary_last_direction == 1 and self.rotary_step_count == 3:
                    self.periphery_events.rotary_big_ccw()
                    self.rotary_step_count = 0
                if self.rotary_last_direction != 1:
                    self.rotary_step_count = 2
                self.rotary_last_direction = 1
                self.periphery_events.rotary_ccw()
            if data[3] == "2":
                if self.rotary_last_direction == 2:
                    self.rotary_step_count += 1
                if self.rotary_last_direction == 2 and self.rotary_step_count == 3:
                    self.periphery_events.rotary_big_cw()
                    self.rotary_step_count = 0
                if self.rotary_last_direction != 2:
                    self.rotary_step_count = 2
                self.rotary_last_direction = 2
                self.periphery_events.rotary_cw()
            self.angleX = round(float(data[4]))
            self.angleY = round(float(data[5]))
            self.angleZ = round(float(data[6]))
        except (UnicodeDecodeError, IndexError):
            return

        if self.led_animation is not None:
            self.led_color = self.led_animation.run()
        self.ser.write(bytes([self.led_color[0], self.led_color[1], self.led_color[2]]))
