# -*- coding: utf-8 -*-

"""
Skeleton for first part of the blob-detection coursework as part of INF250
at NMBU (Autumn 2017).
"""

__author__ = "Kristian Gunder Kramås"
__email__ = "kristian.gunder.kramas@outlook.com"

import numpy as np
import cv2


def threshold(image, th=None):
    """Returns a binarized version of given image, thresholded at given value.

    Binarises the image using a global threshold `th`. Uses Otsu's method
    to find optimal threshold value if the threshold variable is None. The
    returned image will be in the form of an 8-bit unsigned integer array
    with 255 as white and 0 as black.

    Parameters:
    -----------
    image : np.ndarray
        Image to binarise. If this image is a colour image then the last
        dimension will be the colour value (as RGB values).
    th : numeric
        Threshold value. Uses Otsu's method if this variable is None.

    Returns:
    --------
    binarised : np.ndarray(dtype=np.uint8)
        Image where all pixel values are either 0 or 255.
    """

    # Setup
    shape = np.shape(image)
    binarised = np.zeros([shape[0], shape[1]], dtype=np.uint8)

    if len(shape) == 3:
        image = image.mean(axis=2)
    elif len(shape) > 3:
        raise ValueError('Must be a 2D image')

    if th is None:
        th = otsu_thval(image)

    # Start thresholding
    # WRITE YOUR CODE HERE

    return binarised


def histogram(image):
    """Returns the image histogram with 256 bins.
    """

    # Setup
    shape = np.shape(image)
    histogram = np.zeros(256)

    if len(shape) == 3:
        image = image.mean(axis=2)
    elif len(shape) > 3:
        raise ValueError('Must be at 2D image')

    # Start to make the histogram
    # WRITE YOUR CODE HERE

    return histogram


def otsu(image):
    """Finds the optimal thresholdvalue of given image using Otsu's method.
    """
    hist = histogram(image)
    th = 0

    # WRITE YOUR CODE HERE

    return th


if __name__ == "__main__":
    img = cv2.imread('bees.jpeg')
    ret, thresh = cv2.threshold(
        img, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
