import cv2


class Detector(object):

    def __init__(self, casc_path):
        self.classifier = cv2.CascadeClassifier(casc_path)


    def detect(self, image):
        return self.classifier.detectMultiScale(image,
                                                scaleFactor=1.1,
                                                minNeighbors=5,
                                                minSize=(30,30),
                                                flags=0)
