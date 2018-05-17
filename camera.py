import cv2
import time


class Camera:
    def __init__(self, mirror, frame_name):
        self.camera = cv2.VideoCapture(0)
        self.mirror = mirror
        self.frame_name = frame_name
        self.fps = 0
        self.count = 0
        self.avg_fps = 0
        self.start_time = time.time()
        self.end_time = 0

    def update(self, show=False, fps=False, avg_fps=False):
        if show: self.show(fps, avg_fps)

    def show(self, fps, avg_fps):
        start = time.time()
        ret_val, img = self.camera.read()
        self.end_time = end = time.time()
        if self.mirror: img = cv2.flip(img, 1)
        if fps: print(self.fps)
        if avg_fps: print(self.avg_fps)
        cv2.imshow(self.frame_name, img)

        self.fps = 1/(end - start)
        self.count += 1
        self.avg_fps = self.count/(self.end_time - self.start_time)

    @staticmethod
    def exit():
        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            return False
        return True
