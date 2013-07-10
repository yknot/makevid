#
# stores undistort functions to be called
#

import cv2
# used for legacy functions which should be changed out for cv2 functions
import cv2.cv as cv
import numpy as np
# for one feed
import os
import subprocess

def undistort_image(int_mat, dist_coef, filename):

  print 'Undistorting one image...'

  # load the source image
  source = cv2.imread(filename, 1)

  # run the undistortion function
  destination = cv2.undistort(source, int_mat, dist_coef)

  filename_out = filename[:-4] + '-out.png'

  # save image that was created by undistorting
  cv2.imwrite(filename_out, destination)

  print 'Done!'


def undistort_feed(int_mat, dist_coef, filename):
  #
  # GET frames
  #
  print 'Undistorting one feed...'
  print 'Starting setup...'
  # runs setup batch file to create directories and convert video to images
  cmd = 'setup.bat', filename
  p = subprocess.Popen(cmd)
  # wait for the subprocess to finish
  p.wait()

  # finds the number of frames created
  num_files = len([name for name in os.listdir('temp/') 
    if os.path.isfile('temp/'+name)])

  #
  # UNDISTORT frames
  #
  # print statments to show progress
  print 'Starting undistorting frames...'
  print str(num_files), 'frames'

  # loop through each image and undistort the image
  for i in range(1, num_files+1):
    print '\ron frame ' + str(i),

    # create the filename and open the file
    zeros = '0' * (8-len(str(i)))
    filename = zeros + str(i) + '.png'
    source = cv2.imread('temp/' + filename, 1)

    # run the undistortion function
    destination = cv2.undistort(source, int_mat, dist_coef)
    # write the image with the same filename but with out prefix
    cv2.imwrite('out/'+filename, destination)

  #
  # OUTPUT video
  #
  print 'Puting video together...'
  # runs output batch file to run mencoder, mplayer, and ffmpeg
  p2 = subprocess.Popen('output.bat')

  p2.wait()

  print 'Done!'