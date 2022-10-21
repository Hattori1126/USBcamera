import cv2
import os
import datetime


# create folder
def create_folder(figurepath):
    if not os.path.exists(figurepath):
        os.mkdir(figurepath)


# resolution
def capture(width, height):
    # take a photo
    capture = cv2.VideoCapture(0)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, width) ;
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height);

    ret, img = capture.read()

    capture.release()

    return img


def save_photo(figurepath, img, number):

    # save a photo
    cv2.imwrite(figurepath + number + '.png', img)
