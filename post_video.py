import numpy as np
from skimage.color import rgb2gray
from skimage.filters import rank, threshold_mean, sobel
from skimage.morphology import square, erosion, dilation, closing
import cv2


class PostVideo:
  def __init__(self):
    self.frame = None
    self.pic1 = None
    self.pic2 = None
    self.results = None

    self.rect = (0, 0, 0, 0)

  def update(self, frames):
    self.pic1 = self.prep(frames[0])
    self.pic2 = self.prep(frames[1])

    if self.pic1 is not None and self.pic2 is not None:
      pic1 = np.subtract(self.pic2, self.pic1)

      pic1 = self.pic1_(pic1)
      pic2 = self.pic2_(self.pic2)

      self.frame = cv2.bitwise_and(pic1, pic2)

      cv2.imshow("frame", self.frame)

  @staticmethod
  def prep(frame):
    frame = rgb2gray(frame)
    frame = rank.mean(frame, selem=square(10))
    ret, frame = cv2.threshold(frame, threshold_mean(frame), 255, cv2.THRESH_BINARY)
    return frame

  @staticmethod
  def pic1_(pic1):
    pic1 = erosion(pic1)
    pic1 = erosion(pic1)
    pic1 = dilation(pic1)
    pic1 = closing(pic1, selem=square(3))
    pic1 = sobel(pic1)
    return pic1

  @staticmethod
  def pic2_(pic2):
    pic2 = sobel(pic2)
    pic2 = dilation(pic2)
    return pic2
