import cv2


class Preprocessor(object):

    def __init__(self, image):
        self.image = image


    def preprocess(self):
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
