#
# This file undistorts frames from the video from Studio1-1 and 4
# This is to test the undistort function and parameters from .mat file
# And to stich the files together
#

import cv2
# used for legacy functions which should be changed out for cv2 functions
import cv2.cv as cv
import numpy as np
# for loading mat file
import scipy.io

# load mat file with maps and weights
maps = scipy.io.loadmat('maps.mat')

# load the source images
source1 = cv2.imread('Studio1-1.png', 1)
source4 = cv2.imread('Studio1-4.png', 1)

#
# REMAP images to final state
#


# IMAGE 1

# map1 and 2 grabbed from maps dictionary
#### TODO probably don't need to duplicate variable, either pointer or direct ref in remap
map1 = np.float32(maps['m_x'][0])
map2 = np.float32(maps['m_y'][0])
# interpolation method
interpolation = 1
dst1 = cv2.remap(source1, map1, map2, interpolation)

# IMAGE 2

# map1 and 2 grabbed from maps dictionary
#### also not neccesary
map1 = np.float32(maps['m_x'][1])
map2 = np.float32(maps['m_y'][1])
dst4 = cv2.remap(source4, map1, map2, interpolation)

#
# STITCH images together
#

# get final dimensions for for loop
row = len(dst1)
col = len(dst1[1])
# grab weights from maps dictionary
#### also not neccesary
wgt1 = np.float32(maps['weights'][0])
wgt4 = np.float32(maps['weights'][1])

# create blank image
final = np.empty([row,col,3], 'uint8')

# for each row, col and channel
for r in range(row):
  for c in range(col):
    for d in range(3):
      # add matricies with the weights dictating how much of each pixel to use
      final[r][c][d] = dst1[r][c][d]*wgt1[r][c] + dst4[r][c][d]*wgt4[r][c]

# write final image to file
cv2.imwrite('Mosaic.png', final)