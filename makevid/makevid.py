#
# main file that calls all the other functions based on inputs
#

# import statments
import sys
from settings import *
from init import *
from undistort import *
from stitch import *
# from time_split import *


#
# GET settings
#
# find out what the user wants either through arguments or asking
startTime, endTime, folder, location, resolution, cam, setting = flags(sys.argv)

#
# SETUP variables
#
# if setting is stitching no need to run matricies() instead run something else
if setting > 2:
	# use this to get specific maps file that we need
  maps = maps(location, resolution)
  index = indexes(location)
else:
  # get the neccessary calibration matricies
  intrinsic_matrix, distortion_coefficient = matricies(location)

#
# RUN program
#
# run on one image
if setting == 1:
  undistort_image(intrinsic_matrix[int(cam)-1], 
    distortion_coefficient[int(cam)-1], folder)
# run on one feed
elif setting == 2:
  undistort_feed(intrinsic_matrix[int(cam)-1],
    distortion_coefficient[int(cam)-1], folder)
# run on multiple cameras for one image
elif setting == 3:
  remap(maps, cam, folder, index, location, 1)
# run on multiple cameras for feeds
elif setting == 4:
  stitch_feeds(maps, cam, folder, startTime, endTime, index, location)
else:
  print 'Cannot perform this function'
