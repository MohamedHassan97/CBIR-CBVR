from matplotlib import pyplot as plt
import cv2
import math
import statistics


def color_layout(image_path):
    # Define the window size
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    window_size_r = math.floor(image.shape[0] / 4)
    window_size_c = math.floor(image.shape[1] / 4)

    #  Crop out the window and calculate the histogram
    i = 0
    cropped_img = []
    for r in range(0, image.shape[0], window_size_r):
        for c in range(0, image.shape[1], window_size_c):
            window = image[r:r + window_size_r, c:c + window_size_c]
            cropped_img.append(window)
            # cv2.imshow("cropped" + str(i), window)
            i = i + 1

    histograms = {}
    filename = image_path[image_path.rfind("/") + 1:]
    for i in range(len(cropped_img)):
        hist = cv2.calcHist([cropped_img[i]], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
        hist = cv2.normalize(hist, hist).flatten()
        histograms[filename + str(i)] = hist
        # plt.plot(hist)
        # plt.xlim([0, 256])
        # plt.title("hist" + str(i))
        # plt.show()
    return histograms


def pic_layout_similarity(query_hist_dic, db_hist_dic):
    i = 0
    result = {}
    for q_hist, db_hist in zip(query_hist_dic.values(), db_hist_dic.values()):
        d = cv2.compareHist(q_hist, db_hist, 0)
        result["Correlation_" + str(i)] = d
        i += 1
    average_Correlation = statistics.mean(result.values())
    return result, average_Correlation


####### Testing  #######

# image_path1 = 'D:/college/2nd semester/Multimedia/dataset/training_set/foods/921.jpg'
# image_path2 = 'D:/college/2nd semester/Multimedia/dataset/training_set/foods/923.jpg'
#
# hist1 = color_layout(image_path1)
# hist2 = color_layout(image_path2)
# compare, avg = pic_layout_similarity(hist1, hist2)
#
# print(compare, "\n", "avg =", avg, "\n", compare.keys())

cv2.waitKey(0)
