import cv2


class Visualizer(object):

    def __init__(self, image):
        self.image = image


    def viz(self, data):
        for (x, y, w, h) in data:
            cv2.rectangle(self.image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow("Faces found", self.image)
