
import numpy as np
# for reading mat files
import scipy.io

def read_csvs(name):
  """function to read the csvs of calibration numbers"""
  calib = scipy.io.loadmat('calib.mat')
  
  return calib[name+'_fc'], calib[name+'_cc'], calib[name+'_kc']

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

  # get the variable values
  fc, cc, kc = read_csvs(name)
  
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

def maps(location):
  """function to get the maps needed to stitch together frames
     uses the location parameter to grap the right maps"""

  if location == 1:
    maps = scipy.io.loadmat('studio1_maps.mat')
  elif location == 2:
    maps = scipy.io.loadmat('studio2_maps.mat')
  elif location == 3:
    maps = scipy.io.loadmat('mez_maps.mat')
  else:
    print 'Error: can\'t read maps'

  return maps