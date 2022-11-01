import os
import time
import datetime
from module import Capture as cap
from module import light as LED
from module import move_motor as stepmotor
from module import panorama as pano
from module import focus as F


# create folder
figurepath = os.getcwd() + '/camera_figure/'
cap.create_folder(figurepath)

# setting photo parameter
width = 2592         # photo width
height = 1944        # photo height
number = 5           # number of photos
value = 200

# setting motor parameter
wait = 0.001
step = 15
deg = step * 4096
IN1 = 2              # blue to blue
IN2 = 3              # pink to red
IN3 = 4              # yellow to yellow
IN4 = 17             # orange to black
motor = stepmotor.C28BYJ48(IN1, IN2, IN3, IN4)

focus = F.FOCUS()

# take photos
if __name__ == '__main__':
    # create now figure folder
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    folderpath = figurepath + now +'/'
    cap.create_folder(folderpath)

    LED.setting()

    for n in range(0, number, 1):
        count = n + 1
        print(str(count) + '/' + str(number))
        focus.create_goodbadpath(folderpath)

        LED.turn_on()
        time.sleep(5)

        img = cap.capture(width, height)

        # cap.save_photo(folderpath, img, n)
        focus.capture_focus(width, height, value, folderpath, n)

        LED.turn_off()
        motor.Step_CW(deg, wait)
        time.sleep(1)

    pano.create_panorama(folderpath)
    motor.Step_CCW(deg*number*step, wait)
    motor.Cleanup()

print('finish')

