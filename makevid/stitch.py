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
import shutil

from time_split import *
from init import move_files

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
def stitch_feeds(maps, cams, folders):

  #
  # FIND starting files
  #
  startTime, endTime = select_time()
  startNames = []
  startNamesShort = []
  endNames = []
  endNamesShort = []
  for folder in folders:
    startNamesShort.append(select_video(folder, startTime))
    startNames.append(folder + '\\' + select_video(folder, startTime))
    endNamesShort.append(select_video(folder, endTime))
    endNames.append(folder + '\\' + select_video(folder, endTime))


  #
  # GET frames
  #
  print 'Starting Setup...'
  sys.stdout.flush()
  for i in cams:
    if os.path.exists('temp'+str(i)):
      shutil.rmtree('temp'+str(i))
    os.makedirs('temp'+str(i))
  if os.path.exists('out'):
    shutil.rmtree('out')
  os.makedirs('out')
  flag = 0
  for i in range(len(folders)):
    for filename in os.listdir(folders[i]):
      if filename == startNamesShort[cams[i]-1]:
        flag = 1
      if flag:
        name = folders[i] + '\\' + filename
        # runs setup batch file to create directories and convert video to images
        cmd = 'setup_feed.bat', name
        p = subprocess.Popen(cmd)
        p.wait()
        move_files(cams[i])
      if filename == endNamesShort[cams[i]-1]:
        break

  #
  # SYNC frames
  #
  lens = []
  for i in cams:
    startFrames = calc_frames_off(startNamesShort[i-1], startTime, endTime, 1)
    endFrames = calc_frames_off(endNamesShort[i-1], startTime, endTime, 0)
    lens.append(len(os.listdir('temp'+str(i)+'/')) - startFrames - endFrames)
    sync_frames(i, startFrames, 1)
    sync_frames(i, endFrames, 0)

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

  # clean up
  for i in cams:
    shutil.rmtree('temp'+str(i))
  shutil.rmtree('out')
  shutil.rmtree('temp')

