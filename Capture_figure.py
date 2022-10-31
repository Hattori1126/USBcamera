import cv2
import os
import datetime

# resolution
WIDTH = 2592
HEIGHT = 1944
FOCUS = 260

# get now time
now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

# create folder
figurepath = os.getcwd() + '/camera_figure/'
if not os.path.exists(figurepath):
    os.mkdir(figurepath)

# take a photo
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH) ;
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT);
capture.set(cv2.CAP_PROP_FOCUS, FOCUS)

ret, img = capture.read()

# save a photo
cv2.imwrite(figurepath + now + '.png', img)

capture.release()

print('finish')