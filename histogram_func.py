#### find histogram of images

from __future__ import print_function
from __future__ import division
import cv2 as cv
import numpy as np
import argparse

#path="K:\ASU\Second Term\multimedia project\dataset collected"
#fp=open(path,'r+')

hist_images=[]
def histogram_for_database ( path ="K:/ASU/Second Term/multimedia project/dataset_collected/" ,  ):
    for entry in range(101 , 1000):
        imagename = path+str(entry)+".jpg"

        print(entry+1)

        src = cv.imread(imagename)

        i = entry-101
        print (i)

        if src is None:
            print('Could not open or find the image:')
            exit(0)

        hsv_base = cv.cvtColor(src, cv.COLOR_BGR2HSV)

        h_bins = 50
        s_bins = 60
        histSize = [h_bins, s_bins]
        # hue varies from 0 to 179, saturation from 0 to 255
        h_ranges = [0, 180]
        s_ranges = [0, 256]
        ranges = h_ranges + s_ranges # concat lists
        # Use the 0-th and 1-st channels
        channels = [0, 1]
        hist_images.append(cv.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False))
        cv.normalize(hist_images[i], hist_images[i], alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
    return hist_images

#### save histogram







#### compare
def histogram_query(query_path="K:/ASU/Second Term/multimedia project/dataset_collected/320.jpg"):
    query_image  = cv.imread(query_path)

    if query_image is None:
        print('Could not open or find the image:')
        exit(0)



    hsv_query = cv.cvtColor(query_image, cv.COLOR_BGR2HSV)
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
    cv.normalize(hsv_query, hsv_query, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
    return hist_query ,query_image


#print (names)


def min_max(a,n ):
    names= list(range(101, 1000))
    minpos=[]
    maxpos=[]

    for i in range (n):
        print (a.index(min(a)))

        minpos.append(names[a.index(min(a))])
        maxpos.append( names[a.index(max(a))])

        a.pop(a.index(min(a)))
        a.pop( a.index(max(a)))

        names.pop(names.index(names[a.index(min(a))]))
        names.pop(names.index(names[a.index(max(a))]))


    # printing the position
    return  minpos , maxpos

def compare_func (hist_query, hist_images , compare_method = 3 ):
    hist_difference =[]
    names= list(range(101, 1000))

    for i in range (0,899):

        hist_difference.append(cv.compareHist(hist_query, hist_images[i],compare_method ))

    min,_ = min_max(hist_difference,5 )
    retrieved_images= min


    images =[]

    for i in range (5):
        images.append(cv.imread('K:/ASU/Second Term/multimedia project/dataset_collected/'+str(retrieved_images[i])+'.jpg'))

    return hist_difference,images

def printing (hist_difference,images ,query_image):
    print (hist_difference)
    cv.imshow('Source image',query_image)
    cv.imshow('1', images[0])
    cv.imshow('2', images[1])
    cv.imshow('3', images[2])
    cv.imshow('4', images[3])
    cv.imshow('5', images[4])




hist_images = histogram_for_database ( path ="K:/ASU/Second Term/multimedia project/dataset_collected/" ,  )
hist_query ,query_image =  histogram_query(query_path="K:/ASU/Second Term/multimedia project/dataset_collected/333.jpg")
print(hist_images)
print(hist_query )

hist_difference,images  = compare_func (hist_query, hist_images , compare_method = 3 )
printing (hist_difference,images ,query_image)

cv.waitKey(0)
cv.destroyAllWindows() # destroys the windo
