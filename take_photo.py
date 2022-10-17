import os
import time
from module import Capture as cap
from module import light as LED


# create folder
figurepath = os.getcwd() + '/camera_figure/'
cap.create_folder(figurepath)

# setting parameter
width = 2592         # photo width
height = 1944        # photo height
number = 3           # number of photos

# take photos
LED.setting()

for n in range(0, number, 1):
    print(str(n + 1) + '/' + number)
    LED.turn_on()
    time.sleep(1)

    img = cap.capture(width, height)

    cap.save_photo(figurepath, img)

    LED.turn_off()
    time.sleep(1)

print('finish')