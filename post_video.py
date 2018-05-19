import numpy as np
from skimage.color import rgb2gray
from skimage.filters import rank, threshold_mean, sobel
from skimage.morphology import diamond, erosion, dilation, closing
import cv2
import keyboard


class PostVideo:
    def __init__(self):
        self.frame = None
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

        self.frame = cv2.bitwise_and(pic1, pic2)

    def prep(self, frame):
        if self.th is None:
            self.th = threshold_mean(frame)
        frame = rgb2gray(frame)
        frame = rank.mean(frame, selem=diamond(20))
        ret, frame = cv2.threshold(frame, self.th, 255, cv2.THRESH_BINARY)
        return frame

    @staticmethod
    def pic1_(pic1):
        pic1 = erosion(pic1)
        pic1 = erosion(pic1)
        pic1 = erosion(pic1)
        pic1 = dilation(pic1)
        pic1 = sobel(pic1)
        return pic1

    @staticmethod
    def pic2_(pic2):
        pic2 = sobel(pic2)
        pic2 = dilation(pic2)
        return pic2
