from matplotlib import pyplot as plt
import cv2
# import os, sys
# ci_build_and_not_headless = False
# try:
#     from cv2.version import ci_build, headless
#     ci_and_not_headless = ci_build and not headless
# except:
#     pass
# if sys.platform.startswith("linux") and ci_and_not_headless:
#     os.environ.pop("QT_QPA_PLATFORM_PLUGIN_PATH")
# if sys.platform.startswith("linux") and ci_and_not_headless:
#     os.environ.pop("QT_QPA_FONTDIR")
import math
import statistics
import numpy as np
from os import listdir
from os.path import isfile, join


def get_files(folder_path):
    only_files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    for i in range(len(only_files)):
        only_files[i] = folder_path + only_files[i]
    return only_files


def mean_color_layout(image_path):
    # Define the window size
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    window_size_r = math.floor(image.shape[0] / 4)
    window_size_c = math.floor(image.shape[1] / 4)

    #  Crop out the window and calculate the histogram
    j = 0
    cropped_img = []
    for r in range(0, image.shape[0], window_size_r):
        for c in range(0, image.shape[1], window_size_c):
            window = image[r:r + window_size_r, c:c + window_size_c]
            cropped_img.append(window)
            # cv2.imshow("cropped" + str(j), window)
            j = j + 1

    meancolor = []
    filename = image_path[image_path.rfind("/") + 1:]
    for j in range(len(cropped_img)):
        average = np.mean(cropped_img[j], axis=(0, 1))
        meancolor.append(average)

    return meancolor


def mean_color_layout_similarity(query_color_layout, db_color_layout_list):
    similar_parts = []
    similar_pic_index = []

    for i in range(len(db_color_layout_list)):
        for j in range(len(query_color_layout)):
            if ((int(query_color_layout[j][0]) in range(
                    int((int(db_color_layout_list[i][j][0])) - (0.7 * int(db_color_layout_list[i][j][0]))),
                    int((0.7 * int(db_color_layout_list[i][j][0])) + (int(db_color_layout_list[i][j][0])))
            )) and (
                    int(query_color_layout[j][1]) in range(
                int((int(db_color_layout_list[i][j][1])) - (0.7 * int(db_color_layout_list[i][j][1]))),
                int((0.7 * int(db_color_layout_list[i][j][1])) + (int(db_color_layout_list[i][j][1])))
            )) and (
                    int(query_color_layout[j][2]) in range(
                int((int(db_color_layout_list[i][j][2])) - (0.7 * int(db_color_layout_list[i][j][2]))),
                int((0.7 * int(db_color_layout_list[i][j][2])) + (int(db_color_layout_list[i][j][2])))
            ))):
                similar_parts.append(i)

        if similar_parts.count(i) == 14:
            # similar_pic_index = list(set(similar_pic_index))
            similar_pic_index.append(i)

        if len(similar_pic_index) == 5:
            return similar_pic_index

    return similar_pic_index


####testing###

# paths = get_files('D:/college/2nd semester/Multimedia/all dataset/')
# data = []
# for i in range(len(paths)):
#     data.append(mean_color_layout(paths[i]))
# avg = mean_color_layout_similarity(mean_color_layout('D:/college/2nd semester/Multimedia/all dataset/200.jpg'), data)
# print(avg)
# cv2.waitKey(0)
