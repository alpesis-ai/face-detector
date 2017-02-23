"""
$ python detector_webcam.py ./data/models/haarcascade_frontalface_default.xml
"""

import sys

import cv2

from core.preprocessor import Preprocessor
from core.detector import Detector
from viz.visualizer import Visualizer


def main():
    casc_path = sys.argv[1]
    detector = Detector(casc_path)
    
    video_capture = cv2.VideoCapture(0)
    while True:
        is_frame, frame = video_capture.read()
        # print "is_frame: ", is_frame
        # print "frame: ", frame

        preprocessor = Preprocessor(frame)
        image_processed = preprocessor.preprocess()
        
        faces = detector.detect(image_processed)

        visualizer = Visualizer(frame)
        visualizer.viz(faces)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':

    main()
