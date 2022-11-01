import cv2
import os
import time


class FOCUS:
    def variance_of_laplacian(self, image):
        return cv2.Laplacian(image, cv2.CV_64F)


    def create_goodbadpath(self, path):
        self.goodpath = path + 'good/'
        if not os.path.exists(self.goodpath):
            os.mkdir(self.goodpath)

        self.badpath = path + 'bad/'
        if not os.path.exists(self.badpath):
            os.mkdir(self.badpath)


    def capture_focus(self, WIDTH, HEIGHT, value, figurepath, number):
        capture = cv2.VideoCapture(0)
        capture.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH);
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT);

        for n in range(0, 250, 25):
            capture.set(cv2.CAP_PROP_FOCUS, n)

            time.sleep(3)

            ret, img = capture.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            laplacian = self.variance_of_laplacian(gray)

            # save a photo
            if n == 0:
                cv2.imwrite(figurepath + str(number) + '.png', img)

            if laplacian.var() >= value:
                cv2.imwrite(self.goodpath + str(number) + '_' + str(n) + '(' + str(laplacian.var()) + ').png', img)
            else:
                cv2.imwrite(self.badpath + str(number) + '_' + str(n) + '(' + str(laplacian.var()) + ').png', img)

        capture.release()