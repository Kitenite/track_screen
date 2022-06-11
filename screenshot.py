#!/usr/bin/python
from PIL import ImageGrab
from datetime import datetime
import os
import time

folder_path = f"{os.path.dirname(os.path.abspath(__file__))}/images"
compression_rate = 20
wait_time_seconds = 5
previous_image = None

def save_image(image):
    file_name = f"{folder_path}/{datetime.now()}.png"
    image.save(file_name, 'png')

while True:
    current_image = ImageGrab.grab()
    (width, height) = (current_image.width // compression_rate, current_image.height // compression_rate)
    current_image = current_image.resize((width, height))

    if not previous_image:
        save_image(current_image)
    elif list(current_image.getdata()) != list(previous_image.getdata()):
        save_image(current_image)
    # else is idle

    previous_image = current_image
    time.sleep(wait_time_seconds)
