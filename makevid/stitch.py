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
  # 
  # REMAP images to final state
  #
  # run based on number of images and what cameras they are for
  if print_flag:
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
    source = cv2.imread(name, 1)
    dst[c-1] = (cv2.remap(source, np.float32(maps['m_x'][i]), np.float32(maps['m_y'][i]), 1))
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
  wgts = [0]*4
  # grab weights from maps dictionary
  wgts[0] = np.float32(maps['weights'][0])
  wgts[1] = np.float32(maps['weights'][3])
  wgts[2] = np.float32(maps['weights'][2])
  wgts[3] = np.float32(maps['weights'][1])

  flgs = [0]*4
  flgs[0] = 1 if type(dst[0]) is np.ndarray else 0
  flgs[1] = 1 if type(dst[1]) is np.ndarray else 0
  flgs[2] = 1 if type(dst[2]) is np.ndarray else 0
  flgs[3] = 1 if type(dst[3]) is np.ndarray else 0
  # create blank image
  final = np.empty([row,col,3], 'uint8')

  # for each row, col and channel
  for i in range(4):
    final[:,:,0] = final[:,:,0] + dst[i][:,:,0]*wgts[i]
    final[:,:,1] = final[:,:,1] + dst[i][:,:,1]*wgts[i]
    final[:,:,2] = final[:,:,2] + dst[i][:,:,2]*wgts[i]
  # write final image to file
  # cv2.imwrite('Mosaic.png', final)
  cv2.imwrite('out/'+filenames[0][5:], final)

#########################################
def stitch_feeds(maps, cams, filenames):

  #
  # SYNC up frames
  #
  time = select_time()
  names = []
  names_short = []
  for folder in filenames:
    names_short.append(select_video(folder, time))
    names.append(folder + '\\' + select_video(folder, time))

  print 'Undistorting and stitching feeds...'
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

  lens = []
  for i in range(1,5):
    frames = calc_frames_off(names_short[i-1], time)
    lens.append(len(os.listdir('temp'+str(i)+'/')) - frames)
    sync_frames(i, frames)

  num_files = min(lens)
  for i in lens:
    print i
  print num_files

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

