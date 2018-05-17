import cv2
import time


class Camera:
    def __init__(self, mirror, frame_name, step):
        self.camera_01 = cv2.VideoCapture(0)
        self.mirror = mirror
        self.frame_name = frame_name
        self.fps = 0
        self.count = 0
        self.avg_fps = 0
        self.start_time = time.time()
        self.end_time = 0
        self.img = None
        self.step = step
        self.frame = None

    def update(self, show=False, fps=False, avg_fps=False):
        self.count += 1
        if show: self.show(fps, avg_fps)

    def pass_frame(self):
        if self.count % self.step == 0:
            ret_val, self.frame = self.camera_01.read()
            return self.frame

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
