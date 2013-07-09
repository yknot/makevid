#
# stores stitching functions to be used by makevid.py
#

import cv2
# used for legacy functions which should be changed out for cv2 functions
import cv2.cv as cv
import numpy as np
import sys

# read in more intelligently based on input param
# load the source images

def remap(maps, cams, filenames):
  # 
  # REMAP images to final state
  #
  # run based on number of images and what cameras they are for
  print 'Remapping images'
  dst = [0]*4
  for c, name in zip(cams,filenames):
    # map1 and 2 grabbed from maps dictionary
    #### TODO probably don't need to duplicate variable, either pointer or direct ref in remap
    if c == 1:
      i = 0
    elif c == 2:
      i = 3
    elif c == 3:
      i = 2
    elif c == 4:
      i = 1
    else:
      print "Error"
    # map1 = np.float32(maps['m_x'][i])
    # map2 = np.float32(maps['m_y'][i])
    source = cv2.imread(name, 1)
    dst[c-1] = (cv2.remap(source, np.float32(maps['m_x'][i]), np.float32(maps['m_y'][i]), 1))
    print 'Done', str(c) +'!'
    sys.stdout.flush()

  # STITCH images together
  #
  print 'Stitching Images'
  # get final dimensions for loop
  row = len(dst[0])
  col = len(dst[0][0])
  # grab weights from maps dictionary
  wgt1 = np.float32(maps['weights'][0])
  wgt2 = np.float32(maps['weights'][3])
  wgt3 = np.float32(maps['weights'][2])
  wgt4 = np.float32(maps['weights'][1])

  flag1 = 1 if type(dst[0]) is np.ndarray else 0
  flag2 = 1 if type(dst[1]) is np.ndarray else 0
  flag3 = 1 if type(dst[2]) is np.ndarray else 0
  flag4 = 1 if type(dst[3]) is np.ndarray else 0
  # create blank image
  final = np.empty([row,col,3], 'uint8')

  print row, 'rows'
  print col, 'cols'

  # for each row, col and channel
  for r in range(row):
    print '\ron row ' + str(r),
    for c in range(col):
      for d in range(3):
        # add matricies with the weights dictating how much of each pixel to use
        final[r][c][d] = (dst[0][r][c][d] if flag1 else 0)*wgt1[r][c] + (dst[1][r][c][d] if flag2 else 0)*wgt2[r][c] + (dst[2][r][c][d] if flag3 else 0)*wgt3[r][c] + (dst[3][r][c][d] if flag4 else 0)*wgt4[r][c]

  # write final image to file
  cv2.imwrite('Mosaic.png', final)
  print 'Done!'