import cv2
import os
import datetime


now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

figurepath = os.getcwd() + '/camera_figure/'
if not os.path.exists(figurepath):
    os.mkdir(figurepath)

capture = cv2.VideoCapture(0)
ret, img = capture.read()

cv2.imwrite(figurepath + now + '.png', img)

capture.release()