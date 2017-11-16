import cv2


class Image(object):

    def __init__(self, image_path):
        self.image = cv2.imread(image_path)


    def get_image(self):
        return self.image
