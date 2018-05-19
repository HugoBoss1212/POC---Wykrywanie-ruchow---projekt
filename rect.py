class Rect:
    def __init__(self):
        self.rect = (0, 0, 0, 0)
        self.po = []

    def count_rect(self):
        weight_point = (int((max(self.po, key=lambda t: t[0])[0]
                        - min(self.po, key=lambda t: t[0])[0]) / 2),
                        int((max(self.po, key=lambda t: t[1])[1]
                        - min(self.po, key=lambda t: t[1])[1]) / 2))
        print(weight_point)

    def points(self, frame):
        if frame is not None:
            for i in range(frame.shape[0]):
                for j in range(frame.shape[0]):
                    if frame[i][j] > 0:
                        self.po.append((i, j))
        if self.po: self.count_rect()
        self.po.clear()

