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

# load the source video
# TODO: Can't open avi look into dll problems
source = cv2.VideoCapture()
source.open('Studio1-1.avi')


# from the parameters given in the .mat file create matricies
intrinsic_matrix = np.array([[fc[0], 0.0,   cc[0]], 
                             [0.0,   fc[1], cc[1]], 
                             [0.0,   0.0,   1.0 ]], 
                             dtype=np.float32)
distortion_coefficient = np.array([kc[0], kc[1], kc[2], kc[3], kc[4]], 
                                   dtype=np.float32)

# open a video writer
#destination = cv2.VideoWriter.open('Studio1-1-out.avi')

fps = 18
width = 1280
height = 960
# uncompressed YUV 4:2:0 chroma subsampled
fourcc = cv.CV_FOURCC('Y','V','1','2')
writer = cv2.VideoWriter('Studio1-1-out.avi', fourcc, fps, (width, height), 1)

for frame in source.read():
  # run the undistortion function
  destination = cv2.undistort(frame[1], intrinsic_matrix, distortion_coefficient)


# release the capture (file)
source.release()