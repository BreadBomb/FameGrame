import subprocess
import time
import json
from datetime import datetime
from threading import Thread

from flask import Flask, jsonify
from wifi import Cell
from flask_cors import cross_origin

from views.AnimationView import AnimationView
from views.CenteredText import CenteredText
from views.ScrollingText import ScrollingText

app = Flask(__name__)


def start_server():
    app.run(host="0.0.0.0", port=80)


@app.route("/")
def server_root():
    return "hi"


@app.route("/api/v1/wifi/networks")
@cross_origin()
def get_networks():
    cells = None

    while cells is None:
        try:
            cells = Cell.all('wlan0')
        except:
            time.sleep(.1)

    wlans = []
    ssids = []

    for cell in cells:
        if cell.ssid == "" or cell.ssid is None or any(cell.ssid in ssid for ssid in ssids):
            continue

        wlan = {
            "ssid": cell.ssid,
            "encrypted": cell.encrypted,
            "quality": cell.quality
        }

        ssids.append(cell.ssid)
        wlans.append(wlan)

    return jsonify(wlans)


@app.route("/api/v1/wifi/connect")
@cross_origin()
def connect():
    print("connect")


class Setup:
    def __init__(self, width):
        self.timer = datetime.now()
        self.setup_starting = True
        self.setup_wifi = False

        self.start_initialized = False
        self.start_seconds = 3
        self.width = width

        self.wifi_initialized = False
        self.wifi_pid = 0

    def init_start(self):
        self.start_title = CenteredText("Setup", "./fonts/6x9.bdf", 0, self.width, (0, 0, 255, 255))
        self.start_countdown = CenteredText("3", "./fonts/6x9.bdf", 15, self.width, (0, 0, 255, 255))

    def init_wifi(self):
        self.wifi_animation = AnimationView("./animations/__system/wifi", (4, 0))
        self.wifi_connect = ScrollingText("Please connect to wifi", "./fonts/6x9.bdf", (0, 16), (0, 0, 100, 255), 15)
        self.wifi_scrollingText = ScrollingText("SSID: FameGrame", "./fonts/6x9.bdf", (0, 24), (0, 0, 100, 255), 15)

        out = subprocess.Popen("/usr/bin/create_ap -n --no-virt wlan0 FameGrame fgwifilol", shell=True,
                               stdout=subprocess.PIPE)

        thread = Thread(target=start_server)
        thread.start()
        print("hö?")

    def run(self, surface):
        if self.setup_starting:
            if not self.start_initialized:
                self.init_start()
                self.start_initialized = True
            self.start_setup(surface)
        if self.setup_wifi:
            if not self.wifi_initialized:
                self.init_wifi()
                self.wifi_initialized = True
            self.wifi_setup(surface)

    def start_setup(self, surface):
        if (datetime.now() - self.timer).total_seconds() > 1:
            self.start_seconds -= 1
            self.start_countdown.set_text(str(self.start_seconds))
            self.timer = datetime.now()

            if self.start_seconds == -1:
                self.setup_starting = False
                self.start_wifi_setup()

                surface.fill((0, 0, 0, 0))
                return

        self.start_title.run(surface)
        self.start_countdown.run(surface)

    def wifi_setup(self, surface):
        self.wifi_animation.run(surface)
        self.wifi_connect.run(surface)
        self.wifi_scrollingText.run(surface)

    def start_wifi_setup(self):
        cells = self.get_cells()

        self.setup_wifi = True

    def get_cells(self):
        cells = None

        while cells is None:
            try:
                cells = Cell.all('wlan0')
            except:
                time.sleep(.1)

        return cells
