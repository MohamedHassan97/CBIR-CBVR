
from __future__ import print_function
from __future__ import division
import cv2 as cv
import numpy as np
import argparse



def histogram_calc(path):
    image  = cv.imread(path)
    if image is None:
        print('Could not open or find the image:')
        exit(0)

    hsv_query = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    h_bins = 50
    s_bins = 60
    histSize = [h_bins, s_bins]
    # hue varies from 0 to 179, saturation from 0 to 255
    h_ranges = [0, 180]
    s_ranges = [0, 256]
    ranges = h_ranges + s_ranges # concat lists
    # Use the 0-th and 1-st channels
    channels = [0, 1]
    hist_query = cv.calcHist([hsv_query], channels, None, histSize, ranges, accumulate=False)
    hist_query = cv.normalize(hist_query,hist_query, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
    return hist_query


def min_max(lst, num,  index_of_first_img, index_of_last_img):
    names = list(range(index_of_first_img, index_of_last_img))
    minpos = [None]*num
    maxpos = [None]*num
    for i in range (num):
        #print (type(a[0]))
        minpos[i] = names[lst.index(min(lst))]
        maxpos[i] = names[lst.index(max(lst))]
        lst.pop(lst.index(min(lst)))
        lst.pop(lst.index(max(lst)))
        names.pop(names.index(names[lst.index(min(lst))]))
        names.pop(names.index(names[lst.index(max(lst))]))
    # printing the position
    return  minpos , maxpos

def compare(db_size,query_hist , hist_images  ) :

    hist_difference=[None]*db_size
    for i in range(0, db_size):
                # hist_difference[i]=cv.compareHist(query_hist, hist_images[i],3 )
                hist_difference[i] = np.sum(np.abs(query_hist - hist_images[i]))

    return  hist_difference


def retrival (hist_difference,num ,index_1,index_2 ) :

    min,_ = min_max(hist_difference,num,index_1, index_2 )
    retrieved_images_names = min

    loaded_images =[]

    for i in range (5):
        loaded_images.append(cv.imread('K:/ASU/Second Term/multimedia project/dataset_collected/'+str(retrieved_images_names[i])+'.jpg'))

    return retrieved_images_names

def printing (hist_difference,images ,query_image):
    print (hist_difference)
    cv.imshow('Source image',query_image)
    cv.imshow('1', images[0])
    cv.imshow('2', images[1])
    cv.imshow('3', images[2])
    cv.imshow('4', images[3])
    cv.imshow('5', images[4])



# query_hist =histogram_calc(path="K:/ASU/Second Term/multimedia project/dataset_collected/333.jpg")
#
#
# ###### main ################
# loaded_query_image=  cv.imread("K:/ASU/Second Term/multimedia project/dataset_collected/333.jpg")
#
#
#
#
# db_size=1000-200
# db_path='K:/ASU/Second Term/multimedia project/dataset_collected/'
# start_from=200
# hist_images=[None]*db_size
#
# for i in range(0, db_size):
#             imagename =db_path+str(i+start_from)+'.jpg'
#             hist_images[i]=histogram_calc(imagename)
#
#
# hist_difference =compare(db_size,query_hist , hist_images  )
# retrieved_images_names,loaded_images=retrival (hist_difference,5 ,200,1000 )
# printing (hist_difference,loaded_images ,loaded_query_image)
#
# cv.waitKey(0)
# cv.destroyAllWindows() # destroys the windo

