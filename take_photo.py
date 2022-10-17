import os
from module import Capture as cap


figurepath = os.getcwd() + '/camera_figure/'
cap.create_folder(figurepath)

width = 2592
height = 1944

img = cap.capture(width, height)

cap.save_photo(figurepath, img)

print('finish')