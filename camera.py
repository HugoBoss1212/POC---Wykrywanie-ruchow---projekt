import cv2
import time
from skimage.filters import rank, threshold_mean
from skimage import feature
from skimage.morphology import square, dilation, erosion
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import numpy as np


class Camera:
    def __init__(self, mirror, frame_name, step):
        self.camera_01 = cv2.VideoCapture(0)
        self.camera_02 = cv2.VideoCapture(0)
        self.mirror = mirror
        self.frame_name = frame_name
        self.fps = 0
        self.count = 0
        self.avg_fps = 0
        self.start_time = time.time()
        self.end_time = 0
        self.img = None
        self.first = None
        self.second = None
        self.test = True
        self.step = step
        self.temp = None

    def update(self, show=False, fps=False, avg_fps=False):
        self.count += 1
        self.capture_img()

        if show: self.show(fps, avg_fps)

    def show_processing(self):
        pic1 = rgb2gray(np.copy(self.first))
        pic2 = rgb2gray(np.copy(self.second))

        if self.first is not None and self.second is not None:
            pic1 = rank.mean(pic1, selem=square(6))
            pic1 = (pic1 < threshold_mean(pic1))
            pic2 = rank.mean(pic2, selem=square(6))
            pic2 = (pic2 > threshold_mean(pic2))
            pic1 = np.subtract(pic2.astype(int), pic1.astype(int))

            pic1 = erosion(pic1)
            pic1 = dilation(pic1)
            # pic1 = feature.canny(pic1, sigma=3)

            # pic2 = feature.canny(pic2, sigma=3)
            # pic2 = dilation(pic2)

            post_img = np.logical_and(pic2, np.logical_not(pic1))
            plt.imshow(pic1, cmap="gray")
            plt.axis("off")
            plt.show()

        # cv2.imshow(self.frame_name, post_img)

    def capture_img(self):
        if self.count % self.step == 0 and self.test:
            ret_val, self.temp = self.camera_01.read()
            self.test = False
        if self.count % self.step == 0 and not self.test:
            ret_val, self.second = self.camera_01.read()
            self.first = self.temp
            self.show_processing()
            self.test = True

    def show(self, fps, avg_fps):
        start = time.time()
        ret_val, self.img = self.camera_01.read()
        self.end_time = end = time.time()
        if self.mirror: self.img = cv2.flip(self.img, 1)
        if fps and (end - start) > 0:
            print(self.fps)
            self.fps = 1 / (end - start)
        if avg_fps and (self.end_time - self.start_time) > 0:
            print(self.avg_fps)
            self.avg_fps = self.count / (self.end_time - self.start_time)
        cv2.imshow(self.frame_name + "01", self.img)

    @staticmethod
    def exit():
        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            return False
        return True
