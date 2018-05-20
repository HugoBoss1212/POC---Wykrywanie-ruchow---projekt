import cv2
import keyboard
import numpy as np


class Camera:
    def __init__(self, ignored_area, mirror, step):
        self.camera_01 = cv2.VideoCapture(0)
        self.first_frame = None
        self.frame = None
        self.gray = None
        self.ignored_area = ignored_area
        self.mirror = mirror
        self.count = 0
        self.step = step

        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0

    def update(self):
        self.count += 1
        (grabbed, self.frame) = self.camera_01.read()

        self.gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        self.gray = cv2.GaussianBlur(self.gray, (21, 21), 0)

        if self.first_frame is None or self.count % self.step == 0:
            self.first_frame = self.gray.copy()

        self.keyboard_input()
        self.calc_rect()
        cv2.imshow("Live Feed", self.frame)

    def calc_rect(self):
        if self.frame is not None and self.gray is not None:
            kernel = np.ones((5, 5), np.uint8)

            frame_delta = cv2.absdiff(self.first_frame, self.gray)
            thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
            thresh = cv2.dilate(thresh, kernel, iterations=2)
            im, cnts, hier = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for c in cnts:
                if cv2.contourArea(c) < self.ignored_area: continue
                self.show_feed(cv2.boundingRect(c))

    def show_feed(self, rect):
        if rect is not None:
            (self.x, self.y, self.w, self.h) = rect
            # if self.mirror: self.frame = cv2.flip(self.frame, 1)
            cv2.rectangle(self.frame, (self.x, self.y), (self.x + self.w, self.y + self.h), (0, 255, 0), 2)

    def keyboard_input(self):
        if keyboard.is_pressed('+'):
            self.step += 1
            print("Step: " + str(self.step))
        if keyboard.is_pressed('-'):
            if self.step > 1: self.step -= 1
            print("Step: " + str(self.step))
        if keyboard.is_pressed(']'):
            self.ignored_area += 10
            print("Ignored area: " + str(self.ignored_area))
        if keyboard.is_pressed('['):
            self.ignored_area -= 10
            print("Ignored area: " + str(self.ignored_area))

    @staticmethod
    def exit():
        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            return False
        return True
