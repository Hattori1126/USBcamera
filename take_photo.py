import os
import time
from module import Capture as cap
from module import light as LED


figurepath = os.getcwd() + '/camera_figure/'
cap.create_folder(figurepath)

width = 2592
height = 1944
number = 3

LED.setting()

for n in range(0, number, 1):
    LED.turn_on()
    time.sleep(1)

    img = cap.capture(width, height)

    cap.save_photo(figurepath, img)

    LED.turn_off()
    time.sleep(1)


print('finish')