import numpy as numpy
from matplotlib import pyplot as plt
import cv2
import math

image = cv2.imread('test-image3.jpg')
cv2.imshow("Original", image)


def color_layout(image):
    # Define the window size
    window_size_r = math.floor(image.shape[0] / 4)
    window_size_c = math.floor(image.shape[1] / 4)

    #  Crop out the window and calculate the histogram
    i = 0
    cropped_img = []
    for r in range(0, image.shape[0], window_size_r):
        for c in range(0, image.shape[1], window_size_c):
            window = image[r:r + window_size_r, c:c + window_size_c]
            cropped_img.append(window)
            cv2.imshow("cropped" + str(i), window)
            i = i + 1

    histograms = []
    color = ('b', 'g', 'r')
    for i in range(len(cropped_img)):
        for j, col in enumerate(color):
            hist = cv2.calcHist([cropped_img[i]], [j], None, [256], [0, 256])
            plt.plot(hist, color=col)
            plt.xlim([0, 256])
            histograms.append(hist)
        plt.title("hist" + str(i))
        plt.show()
    return histograms


# print(len(histograms))
hist = color_layout(image)
cv2.waitKey(0)
