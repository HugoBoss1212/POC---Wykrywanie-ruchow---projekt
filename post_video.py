import numpy as np
from skimage.color import rgb2gray
from skimage.filters import rank, threshold_mean, sobel
from skimage.morphology import square, erosion, dilation, opening, closing
import matplotlib.pyplot as plt


class PostVideo:
    def __init__(self):
        self.frame = None

    def update(self, frames):
            pic1 = rgb2gray(np.copy(frames[0]))
            pic2 = rgb2gray(np.copy(frames[1]))

            pic1 = rank.mean(pic1, selem=square(10))
            pic2 = rank.mean(pic2, selem=square(10))

            pic1 = (pic1 < threshold_mean(pic1))
            pic2 = (pic2 < threshold_mean(pic2))

            pic1 = np.subtract(pic2.astype(int), pic1.astype(int))

            pic1 = erosion(pic1)
            pic2 = sobel(pic2)

            pic1 = dilation(pic1)
            pic2 = dilation(pic2)

            pic1 = closing(pic1, selem=square(3))
            pic1 = sobel(pic1)

            self.frame = np.logical_and(pic2, pic1)

            self.show(self.frame)

    @staticmethod
    def show(test):
        plt.imshow(test, cmap="gray")
        plt.axis("off")
        plt.show()