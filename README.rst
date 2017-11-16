##############################################################################
Face Detector
##############################################################################

Prequisites

- OpenCV 2.4

==============================================================================
Getting Started
==============================================================================

::

    $ cd detector
    # detecting some faces from an image
    $ python detector_image.py ./data/images/lancome.jpg ./data/models/haarcascade_frontalface_default.xml

    # detecting some faces from a camera
    $ python detector_webcam.py ./data/models/haarcascade_frontalface_default.xml
