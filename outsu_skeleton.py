# -*- coding: utf-8 -*-
"""INF250 Mandatory assignment 1 - see README.md"""

__author__ = "Kristian Gunder Kramås"
__email__ = "kristiankramas@outlook.com"

import numpy as np
import cv2
from skimage.filters import threshold_otsu as cv_otsu
import matplotlib.pyplot as plt


def create_histogram(image):
    """Returns the image histogram with 256 bins."""

    image = image.ravel()
    histogram = np.zeros(256)

    for value in image:
        histogram[value] += 1

    return histogram


def otsu(image):
    """Finds the optimal threshold value of given image using Otsu's method.

    Based on the following implementation:
    http://courses.cs.tau.ac.il/pyProg/1112a/recitations/ta10.pdf
    """

    histogram = create_histogram(image)

    # sum the values of all pixels
    sum_all = 0

    for t in range(256):
        sum_all += t * histogram[t]

    sum_back, w_back, w_for, v_max, t_best = 0, 0, 0, 0, 0
    total = image.shape[0] * image.shape[1]

    # Go over all possible thresholds
    for t in range(256):
        # Update weights
        w_back += histogram[t]
        if w_back == 0:
            continue
        w_for = total - w_back
        if w_for == 0:
            break

        # Calculate classes means
        sum_back += t * histogram[t]
        mean_back = sum_back / w_back
        mean_forw = (sum_all - sum_back) / w_for

        # Calculate between class variance
        v_between = w_back * w_for * (mean_back - mean_forw) ** 2

        if v_between > v_max:
            v_max = v_between
            t_best = t

    return t_best


def visualize(image, threshold, title=None):
    """Shows a figure of orginal image, histogram and thresholded image.

    Based on:
    https://scikit-image.org/docs/0.13.x/auto_examples/xx_applications/plot_thresholding.html

    Args:
        image ([type]): [description]
        threshold ([type]): [description]
    """
    binary = image > threshold

    fig, axes = plt.subplots(ncols=3, figsize=(10, 3))

    if title:
        fig.suptitle(title, fontsize=14)

    ax = axes.ravel()
    ax[0] = plt.subplot(1, 3, 1, adjustable="box")
    ax[1] = plt.subplot(1, 3, 2)
    ax[2] = plt.subplot(1, 3, 3, sharex=ax[0], sharey=ax[0], adjustable="box")

    ax[0].imshow(image, cmap=plt.cm.gray)
    ax[0].set_title("Original")
    ax[0].axis("off")

    # As matplotlib has histograms baked in, we'll use that instead of the
    # histogram() function. Then we will also support the OpenCV-implementation
    # with no extra code.
    ax[1].hist(image.ravel(), bins=256)
    ax[1].set_title("Histogram")
    ax[1].axvline(threshold, color="r")

    ax[2].imshow(binary, cmap=plt.cm.gray)
    ax[2].set_title("Thresholded")
    ax[2].axis("off")

    plt.subplots_adjust(wspace=0.5, top=0.7)
    plt.show()


def load_gray_image(image):
    """Returns image in grayscale

    Args:
        image ([type]): Image file

    Returns:
        numpy.ndarray: 2D-array of integers 0-255
    """
    image = cv2.imread(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image


if __name__ == "__main__":
    image = load_gray_image("bie_threshold.jpeg")

    # Scikit version for reference
    threshold = cv_otsu(image)
    visualize(image, threshold, "CV2 Implementation")

    # Manual implementation
    threshold = otsu(image)
    visualize(image, threshold, "Manual Implementation")
