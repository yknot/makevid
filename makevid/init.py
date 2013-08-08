
import numpy as np
# for reading mat files
import scipy.io
import os
import sys


#######################################
def read_mats(name):
  """function to read the mats of calibration numbers"""
  calib = scipy.io.loadmat('calib.mat')
  
  return calib[name+'_fc'], calib[name+'_cc'], calib[name+'_kc']

#######################################
def matricies(location):
  """function to create the intrinsic and distortion matricies based
    on the variables recorded in the function above"""
  
  if location == 1:
    name = 'studio1'
    cams = 4
  elif location == 2:
    name = 'studio2'
    cams = 6
  elif location == 3:
    name = 'mez'
    cams = 6
  else:
    print 'Error: can\'t retrieve matricies'
    sys.exit()

  # get the variable values
  fc, cc, kc = read_mats(name)
  
  # set up the blanck matricies
  intrinsic_matrix = []
  distortion_coefficient = []

  # for each camera
  for i in range(cams):
    # from the parameters given in the .mat file create matricies
    intrinsic_matrix.append(np.array([[fc[i][0], 0.0,   cc[i][0]], 
                                      [0.0,   fc[i][1], cc[i][1]], 
                                      [0.0,   0.0,   1.0 ]], 
                                      dtype=np.float32))
    distortion_coefficient.append(np.array([kc[i][0], kc[i][1], kc[i][2], 
                                            kc[i][3], kc[i][4]], 
                                            dtype=np.float32))
  return intrinsic_matrix, distortion_coefficient

#######################################
def maps(location, resolution):
  """function to get the maps needed to stitch together frames
     uses the location parameter to grap the right maps"""

  if location == 1:
    if resolution == 'full':
      maps = scipy.io.loadmat('studio1_maps/full.mat')
    elif resolution == '1080':
      maps = scipy.io.loadmat('studio1_maps/1080.mat')
    elif resolution == '720':
      maps = scipy.io.loadmat('studio1_maps/730.mat')
    elif resolution == '480':
      maps = scipy.io.loadmat('studio1_maps/486.mat')
    else:
      print 'Resolution not supported'
      sys.exit()
  elif location == 2:
    if resolution == 'full':
      maps = scipy.io.loadmat('studio2_maps/full.mat')
    elif resolution == '1080':
      maps = scipy.io.loadmat('studio2_maps/1080.mat')
    elif resolution == '720':
      maps = scipy.io.loadmat('studio2_maps/720.mat')
    elif resolution == '480':
      maps = scipy.io.loadmat('studio2_maps/480.mat')
    else:
      print 'Resolution not supported'
      sys.exit()
  elif location == 3:
    if resolution == 'full':
      maps = scipy.io.loadmat('mez_maps/full.mat')
    elif resolution == '1080':
      maps = scipy.io.loadmat('mez_maps/1080.mat')
    elif resolution == '720':
      maps = scipy.io.loadmat('mez_maps/720.mat')
    elif resolution == '480':
      maps = scipy.io.loadmat('mez_maps/480.mat')
    else:
      print 'Resolution not supported' 
      sys.exit()
  else:
    print 'Error: location invalid'
    sys.exit()

  return maps

#######################################
def move_files(cam):
  start = len(os.listdir('temp'+str(cam)))
  for i in range(1, len(os.listdir('temp'))+1):
    zerosOld = '0' * (8-len(str(i)))
    nameOld = zerosOld + str(i) + '.png'
    zerosNew = '0' * (8-len(str(i+start)))
    nameNew = zerosNew + str(i+start) + '.png'
    os.rename('temp/' + nameOld, 'temp'+str(cam)+'/'+nameNew)

#######################################
def indexes(location):
  """Provides the indexes for the cameras according to location"""
  if location == 1:
    index = [0]*4
    index[0] = 0
    index[1] = 3
    index[2] = 2
    index[3] = 1
  elif location == 2:
    index = [0]*6
    index[0] = 0
    index[1] = 1
    index[2] = 2
    index[3] = 3
    index[4] = 4
    index[5] = 5
  elif location == 3:
    index = [0]*6
    index[0] = 0
    index[1] = 3
    index[2] = 2
    index[3] = 1
    index[4] = 4
    index[5] = 5
  else:
    print 'Error: location invalid'
    sys.exit()
    
  return index