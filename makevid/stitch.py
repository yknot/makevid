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
def remap(maps, cams, filenames, index, location, singleImageFlag):

  # if a single image add filename
  if singleImageFlag:
    filenames = get_filenames(filenames, cams, location)

  # 
  # REMAP images to final state
  #
  if singleImageFlag:
    print 'Remapping images'

  dst = [0]*len(index)
  # remap images into dst list
  for c, name in zip(cams,filenames):
    if not os.path.isfile(name):
      print 'Error: No such file', name
      sys.exit()
    source = cv2.imread(name, 1)
    dst[c-1] = (cv2.remap(source, np.float32(maps['m_x'][index[c-1]]), np.float32(maps['m_y'][index[c-1]]), 1))
    if singleImageFlag:
      print 'Done', str(c) +'!'
      sys.stdout.flush()
    
  #
  # STITCH images together
  #
  if singleImageFlag:
    print 'Stitching Images'

  # get final dimensions for loop
  row = len(dst[cams[0]-1])
  col = len(dst[cams[0]-1][0])

  # create blank image
  final = np.empty([row,col,3], 'uint8')

  # for each row, col and channel
  for i in range(len(index)):
    if type(dst[i]) is np.ndarray:
      final[:,:,0] = final[:,:,0] + dst[i][:,:,0]*np.float32(maps['weights'][index[i]])
      final[:,:,1] = final[:,:,1] + dst[i][:,:,1]*np.float32(maps['weights'][index[i]])
      final[:,:,2] = final[:,:,2] + dst[i][:,:,2]*np.float32(maps['weights'][index[i]])
  # write final image to file
  if singleImageFlag:
    cv2.imwrite('Mosaic.png', final)
  else:
    cv2.imwrite('out/'+filenames[0][5:], final)

#########################################
def stitch_feeds(maps, cams, folder, startTime, endTime, index, location):

  #
  # FIND starting files
  #
  startNames = []
  startNamesShort = []
  endNames = []
  endNamesShort = []

  # add sub folders
  folders = get_folders(folder, cams, location)

  # for each folder get the start video and end video
  for f in folders:
    startNamesShort.append(select_video(f, startTime))
    startNames.append(f + '\\' + select_video(f, startTime))
    endNamesShort.append(select_video(f, endTime))
    endNames.append(f + '\\' + select_video(f, endTime))

  #
  # GET frames
  #
  print 'Starting Setup...'
  sys.stdout.flush()
  # clean up the folders
  for i in cams:
    if os.path.exists('temp'+str(i)):
      shutil.rmtree('temp'+str(i))
    os.makedirs('temp'+str(i))
  if os.path.exists('out'):
    shutil.rmtree('out')
  os.makedirs('out')

  # get frames from videos, only selecting those neccesary
  flag = 0
  for i in range(len(folders)):
    print '\rOn camera ' + str(i+1),
    sys.stdout.flush()
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
  print
  #
  # SYNC frames
  #
  # clean up frames by trimming start and end
  lens = []
  for i in cams:
    startFrames, endFrames = calc_frames_off(startNamesShort[i-1], startTime, endTime)
    sync_frames(i, startFrames, 1)
    sync_frames(i, endFrames, 0)
    lens.append(len(os.listdir('temp'+str(i)+'/')))

  numFiles = min(lens)
  #
  # REMAP frames
  #
  # for each image remap
  for i in range(1, numFiles+1):
    print '\ron frame ' + str(i),
    sys.stdout.flush()
     # create the filename and open the file
    zeros = '0' * (8-len(str(i)))
    filename = zeros + str(i) + '.png'
    if location == 1:
      sources = ['temp1/'+filename,'temp2/'+filename,'temp3/'+filename,'temp4/'+filename]
    else:
      sources = ['temp1/'+filename,'temp2/'+filename,'temp3/'+filename,'temp4/'+filename, 'temp5/' + filename, 'temp6/' + filename]

    remap(maps, cams, sources, index, location, 0)

  #
  # OUTPUT video
  #
  print '\nPuting video together...'
  sys.stdout.flush()
  # runs output batch file to run mencoder, mplayer, and ffmpeg
  p2 = subprocess.Popen('output_feed.bat')
  p2.wait()

  print 'Done!'


#######################################
def get_filenames(filenames, cams, location):
  """For single frame get full file paths"""
  folder = filenames
  filenames = []
  if location == 1:
    if 1 in cams: filenames.append(folder + 'Studio1-1.png')
    if 2 in cams: filenames.append(folder + 'Studio1-2.png')
    if 3 in cams: filenames.append(folder + 'Studio1-3.png')
    if 4 in cams: filenames.append(folder + 'Studio1-4.png')
  elif location == 2:
    if 1 in cams: filenames.append(folder + 'Studio2-1.png')
    if 2 in cams: filenames.append(folder + 'Studio2-2.png')
    if 3 in cams: filenames.append(folder + 'Studio2-3.png')
    if 4 in cams: filenames.append(folder + 'Studio2-4.png')
    if 5 in cams: filenames.append(folder + 'Studio2-5.png')
    if 6 in cams: filenames.append(folder + 'Studio2-6.png')
  elif location == 3:
    if 1 in cams: filenames.append(folder + 'Mez-1.png')
    if 2 in cams: filenames.append(folder + 'Mez-2.png')
    if 3 in cams: filenames.append(folder + 'Mez-3.png')
    if 4 in cams: filenames.append(folder + 'Mez-4.png')
    if 5 in cams: filenames.append(folder + 'Mez-5.png')
    if 6 in cams: filenames.append(folder + 'Mez-6.png')
  else:
    print 'Error: location invalid'
    sys.exit()

  return filenames

#####################################
def get_folders(folder, cams, location):
  folders = []
  if 1 in cams: folders.append(folder + '1\\')
  if 2 in cams: folders.append(folder + '2\\')
  if 3 in cams: folders.append(folder + '3\\')
  if 4 in cams: folders.append(folder + '4\\')
  if location == 2 or location == 3:
    if 5 in cams: folders.append(folder + '5\\')
    if 6 in cams: folders.append(folder + '6\\')

  return folders