import os
import cv2 as cv


imgs = []
# 合成したい画像を指定する
figurepath = os.getcwd() + '/camera_figure/'

imgs.append(cv.imread(figurepath + '20221025133651.png'))
imgs.append(cv.imread(figurepath + '20221025133723.png'))
imgs.append(cv.imread(figurepath + '20221025133733.png'))

stitcher = cv.Stitcher_create()

status, stitched = stitcher.stitch(imgs)

# 画面に表示する
# cv.imshow('result', stitched)

# ファイルに保存する
cv.imwrite(figurepath + "panorama.png", stitched)
cv.waitKey(0)