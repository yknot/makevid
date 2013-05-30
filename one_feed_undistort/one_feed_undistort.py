#
# This file undistorts one feed from the video from Studio1-1
# This is to test the undistort function on video 
#

import cv2
# used for legacy functions which should be changed out for cv2 functions
import cv2.cv as cv
import csv
import numpy as np

# read in values from csv storing data 
# TODO: look into getting straight from .mat or converting file to csv
with open('../calibrations/Studio1-1.csv', 'rb') as csvfile:
  valuereader = csv.reader(csvfile, delimiter=',')
  for row in valuereader:
    if row[0] == 'fc':
      fc = row[1:]
    elif row[0] == 'cc':
      cc = row[1:]
    elif row[0] == 'kc':
      kc = row[1:]
    else:
      print 'error in value'

# load the source image
source = cv2.imread('Studio1-1.png', 1)

# from the parameters given in the .mat file create matricies
intrinsic_matrix = np.array([[fc[0], 0.0,   cc[0]], 
                             [0.0,   fc[1], cc[1]], 
                             [0.0,   0.0,   1.0 ]], 
                             dtype=np.float32)
distortion_coefficient = np.array([kc[0], kc[1], kc[2], kc[3], kc[4]], 
                                   dtype=np.float32)

# run the undistortion function
destination = cv2.undistort(source, intrinsic_matrix, distortion_coefficient)

# save image that was created by undistorting
cv2.imwrite('Studio1-1-out.png', destination)