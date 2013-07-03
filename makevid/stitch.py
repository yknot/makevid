#
# stores stitching functions to be used by makevid.py
#

import cv2
# used for legacy functions which should be changed out for cv2 functions
import cv2.cv as cv
import numpy as np

# read in more intelligently based on input param
# load the source images

def remap(maps, cams, filenames):
  # 
  # REMAP images to final state
  #
  # run based on number of images and what cameras they are for
  print 'Remapping images'
  dst = []
  for c, name in zip(cams,filenames):
    # map1 and 2 grabbed from maps dictionary
    #### TODO probably don't need to duplicate variable, either pointer or direct ref in remap
    if c == 1:
      i = 0
    elif c == 2:
      i = 3
    elif c == 3:
      i = 2
    else:
      i = 1
    # map1 = np.float32(maps['m_x'][i])
    # map2 = np.float32(maps['m_y'][i])
    source = cv2.imread(name, 1)
    dst.append(cv2.remap(source, np.float32(maps['m_x'][i]), np.float32(maps['m_y'][i]), 1))
    print 'Done 1!'

  # # IMAGE 1

  # # map1 and 2 grabbed from maps dictionary
  # #### TODO probably don't need to duplicate variable, either pointer or direct ref in remap
  # map1 = np.float32(maps['m_x'][0])
  # map2 = np.float32(maps['m_y'][0])
  # # interpolation method
  # interpolation = 1
  # dst1 = cv2.remap(source1, map1, map2, interpolation)
  # print 'Done 1!'
  # # IMAGE 2st

  # # map1 and 2 grabbed from maps dictionary
  # #### also not neccesary
  # map1 = np.float32(maps['m_x'][1])
  # map2 = np.float32(maps['m_y'][1])
  # dst4 = cv2.remap(source4, map1, map2, interpolation)
  # print 'Done 2!'
  #
  # STITCH images together
  #
  print 'Stitching Images'
  # get final dimensions for loop
  row = len(dst[0])
  col = len(dst[0][0])
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
        final[r][c][d] = dst[0][r][c][d]*wgt1[r][c] + dst[1][r][c][d]*wgt4[r][c]

  # write final image to file
  cv2.imwrite('Mosaic.png', final)
  print 'Done!'