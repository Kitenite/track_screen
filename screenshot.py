#!/usr/bin/python
from PIL import ImageGrab
from datetime import datetime
import os
import time

folder_path = f"{os.path.dirname(os.path.abspath(__file__))}/images"
compression_rate = 20
wait_time_seconds = 10

while True:
    im = ImageGrab.grab()
    fname = f"{folder_path}/{datetime.now()}.png"
    (width, height) = (im.width // compression_rate, im.height // compression_rate)
    im = im.resize((width, height))
    im.save(fname, 'png')
    time.sleep(wait_time_seconds)
