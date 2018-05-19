import numpy as np


class Rect:
    def __init__(self):
        self.rect = [(0, 0), (0, 0)]
        self.draw = False
        self.x = []
        self.y = []

    def count_rect(self):
        self.rect[0] = (self.y[0], self.x[0])
        element, index = max(list(zip(self.y, range(len(self.y)))))
        self.rect[1] = (element + 20, self.x[index] + 150)
        self.draw = True

    def points(self, frame):
        if frame is not None: self.x, self.y = np.where(frame > 0)
        if len(self.x) != 0 and len(self.y) != 0: self.count_rect()
        else: self.draw = False
