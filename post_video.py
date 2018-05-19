import numpy as np
from skimage.color import rgb2gray
from skimage.filters import rank, threshold_mean
from skimage.morphology import diamond, erosion, dilation
import cv2
import keyboard


class PostVideo:
    def __init__(self):
        self.th = None

    def update(self, frames):
        pic1 = self.prep(frames[0])
        pic2 = self.prep(frames[1])

        if keyboard.is_pressed('+'):
            self.th += 10
            print(self.th)
        if keyboard.is_pressed('-'):
            self.th -= 10
            print(self.th)

        pic1 = np.subtract(pic2, pic1)

        pic1 = self.pic1_(pic1)
        pic2 = self.pic2_(pic2)

        return cv2.bitwise_and(pic1, pic2)

    def prep(self, frame):
        if self.th is None:
            self.th = threshold_mean(frame)
        frame = rgb2gray(frame)
        frame = rank.mean(frame, selem=diamond(20))
        ret, frame = cv2.threshold(frame, self.th, 255, cv2.THRESH_BINARY)
        return frame

    @staticmethod
    def pic1_(pic1):
        kernel = np.ones((5, 5), np.uint8)
        pic1 = cv2.erode(pic1, kernel, iterations=1)
        pic1 = cv2.morphologyEx(pic1, cv2.MORPH_CLOSE, kernel)
        pic1 = cv2.dilate(pic1, kernel, iterations=1)
        pic1 = cv2.Laplacian(pic1, cv2.CV_64F)
        return pic1

    @staticmethod
    def pic2_(pic2):
        kernel = np.ones((5, 5), np.uint8)
        pic2 = cv2.Laplacian(pic2, cv2.CV_64F)
        pic2 = cv2.dilate(pic2, kernel, iterations=1)
        return pic2
