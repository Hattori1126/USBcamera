import cv2
import os
import datetime


WIDTH = 1280
HEIGHT = 720

now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

figurepath = os.getcwd() + '/camera_figure/'
if not os.path.exists(figurepath):
    os.mkdir(figurepath)

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH) ;
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT);

ret, img = capture.read()

cv2.imwrite(figurepath + now + '.png', img)

capture.release()

print('finish')