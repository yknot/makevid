#
# This file undistorts one feed from the video from Studio1-1
# This is to test the undistort function on video 
#

import cv2
# used for legacy functions which should be changed out for cv2 functions
import cv2.cv as cv
import csv
import numpy as np
# for using ffmeg and file structure information
import os
import subprocess


#
# SETUP variables
#

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

# from the parameters given in the .mat file create matricies
intrinsic_matrix = np.array([[fc[0], 0.0,   cc[0]], 
                             [0.0,   fc[1], cc[1]], 
                             [0.0,   0.0,   1.0 ]], 
                             dtype=np.float32)
distortion_coefficient = np.array([kc[0], kc[1], kc[2], kc[3], kc[4]], 
                                   dtype=np.float32)

#
# SETUP files
#

print 'start setup'
# runs setup batch file to create directories and convert video to images
p = subprocess.Popen('setup.bat')
# wait for the subprocess to finish
p.wait()

# finds the number of frames created
num_files = len([name for name in os.listdir('temp/') 
  if os.path.isfile('temp/'+name)])




#
# UNDISTORT files
#

# print statments to show progress
print 'start undistorting'
print str(num_files), 'frames'

# loop through each image and undistort the image
for i in range(1, num_files+1):
  print '\ron frame ' + str(i),

  # create the filename and open the file
  zeros = '0' * (8-len(str(i)))
  filename = zeros + str(i) + '.png'
  source = cv2.imread('temp/' + filename, 1)

  # run the undistortion function
  destination = cv2.undistort(source, intrinsic_matrix, distortion_coefficient)
  # write the image with the same filename but with out prefix
  cv2.imwrite('out/'+filename, destination)


#
# OUTPUT video
#

print 'put video together'
# runs output batch file to run mencoder, mplayer, and ffmpeg
p2 = subprocess.Popen('output.bat')

p2.wait()
