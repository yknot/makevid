#
# main file that calls all the other functions based on inputs
#

# import statments
import sys
from settings import *
from init import *
from undistort import *
from stitch import *

#
# GET settings
#
# find out what the user wants either through arguments or asking
if len(sys.argv) < 5:
  setting, location, cam, filename = settings()
else:
  setting, location, cam, filename = set_settings(sys.argv)

#
# SETUP variables
#
# if setting is stitching no need to run matricies() instead run something else
if setting > 2:
	# use this to get specific maps file that we need
	maps = maps(location)
else:
  # get the neccessary calibration matricies
  intrinsic_matrix, distortion_coefficient = matricies(location)

#
# RUN program
#
# run on one image
if setting == 1:
  undistort_image(intrinsic_matrix[int(cam)-1], 
    distortion_coefficient[int(cam)-1], filename)
# run on one feed
elif setting == 2:
  undistort_feed(intrinsic_matrix[int(cam)-1],
    distortion_coefficient[int(cam)-1], filename)
elif setting == 3:
  remap(maps, cam, filename)
# future progress
else:
  print 'Cannot perform this function at this time'
