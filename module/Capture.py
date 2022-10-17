import cv2
import os
import datetime


# create folder
# figurepath = os.getcwd() + '/camera_figure/'
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


def save_photo(figurepath, img):
    # get now time
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # save a photo
    cv2.imwrite(figurepath + now + '.png', img)
