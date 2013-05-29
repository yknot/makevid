import cv2
import cv2.cv as cv
import csv
import numpy as np

# read in values from csv storing data 
# TODO: look into getting straight from .mat or converting file to csv
with open('Studio1-1.csv', 'rb') as csvfile:
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

#load the images
source = cv2.imread('Studio1-1.png', 1)
destination = np.zeros((source.shape[0], source.shape[1]*2, 3), np.uint8)



intrinsic_matrix = np.array([[fc[0], 0.0, cc[0]], 
                             [0.0, fc[1], cc[1]], 
                             [0.0, 0.0, 1.0]], dtype=np.float32)
distortion_coefficient = np.array([kc[0], kc[1], kc[2], kc[3], kc[4]])

cv2.undistort(source, destination, intrinsic_matrix, distortion_coefficient)


