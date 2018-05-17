import cv2


class PostVideo:
    def __init__(self, mirror, frame_name):
        self.camera_01 = cv2.VideoCapture(0)
        self.mirror = mirror
        self.frame_name = frame_name

    def update(self, frame, show=False):
        if show: self.show(frame)

    def show(self, frame):
        if self.mirror: frame = cv2.flip(frame, 1)
        cv2.imshow(self.frame_name + "02", frame)

    # def show_processing(self):
    #     pic1 = rgb2gray(np.copy(self.first))
    #     pic2 = rgb2gray(np.copy(self.second))
    #
    #     if self.first is not None and self.second is not None:
    #         pic1 = rank.mean(pic1, selem=square(6))
    #         pic1 = (pic1 < threshold_mean(pic1))
    #         pic2 = rank.mean(pic2, selem=square(6))
    #         pic2 = (pic2 > threshold_mean(pic2))
    #         pic1 = np.subtract(pic2.astype(int), pic1.astype(int))
    #
    #         pic1 = erosion(pic1)
    #         pic1 = dilation(pic1)
    #         pic1 = feature.canny(pic1, sigma=3)
    #
    #         pic2 = feature.canny(pic2, sigma=3)
    #         pic2 = dilation(pic2)
    #
    #         post_img = np.logical_and(pic2, np.logical_not(pic1))
    #         plt.imshow(pic1, cmap="gray")
    #         plt.axis("off")
    #         plt.show()
    #
    #         cv2.imshow(self.frame_name, post_img)