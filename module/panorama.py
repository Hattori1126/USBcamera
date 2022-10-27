import os
import cv2 as cv
import glob


def get_filelist(folderpath):
    filelist = glob.glob(folderpath + '/*' + '.png')

    # filenamelist = []
    # for f in filelist:
    #     filenamelist = filenamelist + [os.path.splitext(os.path.basename(f))[0]]

    # Use natsort to sort filename like Windows Explorer
    return filelist


def create_panorama(figurepath):
    imgs = []
    imgspath = get_filelist(figurepath)

    for n in range(0, len(imgspath), 1):
        imgs.append(cv.imread(imgspath[n]))

    stitcher = cv.Stitcher_create()

    status, stitched = stitcher.stitch(imgs)[0]

    # 画面に表示する
    # cv.imshow('result', stitched)

    # ファイルに保存する
    cv.imwrite(figurepath + "panorama.png", stitched)
    cv.waitKey(0)