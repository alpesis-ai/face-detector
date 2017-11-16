"""
$ python detector_image.py ./data/images/lancome.jpg ./data/models/haarcascade_frontalface_default.xml  
"""

import sys

import cv2

from core.image import Image
from core.detector import Detector
from core.preprocessor import Preprocessor
from viz.visualizer import Visualizer


def main():
    image_path = sys.argv[1]
    casc_path = sys.argv[2]

    image = Image(image_path)
    image_loaded = image.get_image()
    preprocessor = Preprocessor(image_loaded)
    image_processed = preprocessor.preprocess()

    detector = Detector(casc_path)
    faces = detector.detect(image_processed)
    print "Found {0} faces!".format(len(faces))
    print "Faces: ", faces

    visualizer = Visualizer(image.get_image())
    visualizer.viz(faces)

    cv2.waitKey(0)

if __name__ == "__main__":
    
    main()
