#
# stores stitching functions to be used by makevid.py
#
import cv2
# used for legacy functions which should be changed out for cv2 functions
import cv2.cv as cv
import numpy as np
import sys
import os
import subprocess

from time_split import *

#########################################
def remap(maps, cams, filenames, print_flag):

  index = [0]*4
  index[0] = 0
  index[1] = 3
  index[2] = 2
  index[3] = 1
  # 
  # REMAP images to final state
  #
  # run based on number of images and what cameras they are for
  if print_flag:
    print 'Remapping images'
  dst = [0]*4
  for c, name in zip(cams,filenames):
    source = cv2.imread(name, 1)
    dst[c-1] = (cv2.remap(source, np.float32(maps['m_x'][index[c-1]]), np.float32(maps['m_y'][index[c-1]]), 1))
    if print_flag:
      print 'Done', str(c) +'!'
      sys.stdout.flush()
    
  #
  # STITCH images together
  #
  if print_flag:
    print 'Stitching Images'

  # get final dimensions for loop
  row = len(dst[0])
  col = len(dst[0][0])

  # create blank image
  final = np.empty([row,col,3], 'uint8')

  # for each row, col and channel
  for i in range(4):
    if type(dst[i]) is np.ndarray:
      final[:,:,0] = final[:,:,0] + dst[i][:,:,0]*np.float32(maps['weights'][index[i]])
      final[:,:,1] = final[:,:,1] + dst[i][:,:,1]*np.float32(maps['weights'][index[i]])
      final[:,:,2] = final[:,:,2] + dst[i][:,:,2]*np.float32(maps['weights'][index[i]])
  # write final image to file
  if print_flag:
    cv2.imwrite('Mosaic.png', final)
  else:
    cv2.imwrite('out/'+filenames[0][5:], final)

#########################################
def stitch_feeds(maps, cams, filenames):

  #
  # FIND starting files
  #
  start_time, end_time = select_time()
  names = []
  names_short = []
  for folder in filenames:
    names_short.append(select_video(folder, start_time))
    names.append(folder + '\\' + select_video(folder, start_time))

  #
  # GET frames
  #
  print 'Starting Setup...'
  sys.stdout.flush()
  # runs setup batch file to create directories and convert video to images
  cmd = 'setup_feed.bat', names[0], names[1], names[2], names[3]
  p = subprocess.Popen(cmd)
  # wait for the subprocess to finish
  p.wait()

  #
  # SYNC frames
  #
  lens = []
  for i in range(1,5):
    frames = calc_frames_off(names_short[i-1], start_time)
    lens.append(len(os.listdir('temp'+str(i)+'/')) - frames)
    sync_frames(i, frames)

  num_files = min(lens)

  #
  # REMAP frames
  #
  for i in range(1, num_files+1):
    print '\ron frame ' + str(i),
    sys.stdout.flush()
     # create the filename and open the file
    zeros = '0' * (8-len(str(i)))
    filename = zeros + str(i) + '.png'
    sources = ['temp1/'+filename,'temp2/'+filename,'temp3/'+filename,'temp4/'+filename]

    remap(maps, cams, sources, 0)

  #
  # OUTPUT video
  #
  print 'Puting video together...'
  sys.stdout.flush()
  # runs output batch file to run mencoder, mplayer, and ffmpeg
  p2 = subprocess.Popen('output_feed.bat')
  p2.wait()

  print 'Done!'

