import json
import os

from wifi import Cell

cells = Cell.all('wlan0')

for cell in cells:
    print(cell.ssid)
