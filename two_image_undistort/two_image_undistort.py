#
# This file undistorts frames from the video from Studio1-1 and 4
# This is to test the undistort function and parameters from .mat file
# And to stich the files together
#

import cv2
# used for legacy functions which should be changed out for cv2 functions
import cv2.cv as cv
import numpy as np

# file that puts together intrinsic and distortion matricies
from init import *

# create those matricies
intrinsic_matrix, distortion_coefficient = matricies()

# load the source images
source1 = cv2.imread('Studio1-1.png', 1)
source4 = cv2.imread('Studio1-4.png', 1)

# run the undistortion function
# base 0 therefore 0 = cam 1
destination1 = cv2.undistort(source1, intrinsic_matrix[0],
                                      distortion_coefficient[0])
destination4 = cv2.undistort(source4, intrinsic_matrix[3],
                                      distortion_coefficient[3])


# save image that was created by undistorting
cv2.imwrite('Studio1-1-out.png', destination1)
cv2.imwrite('Studio1-4-out.png', destination4)


# src is destination 1
src = destination1
# map1 and 2 need to be read in
interpoolation = 'INTER_NEAREST'
dst1 = cv2.remap(src, map1, map2, interpoolation)

# src is destination 1
src = destination4
# map1 and 2 need to be read in
dst4 = cv2.remap(src, map1, map2, interpoolation)


# stitch images together