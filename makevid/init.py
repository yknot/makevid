
import csv
import numpy as np

# function to read the csvs of calibration numbers
def read_csvs(name):
  fc = []
  cc = [] # store the variables from the calibrations
  kc = []

  # loop through each calibration file
  for i in range(1,5):
    filename = name + str(i) + '.csv'

    # read in values from csvs storing data 
    with open(filename, 'rb') as csvfile:
      valuereader = csv.reader(csvfile, delimiter=',')
      # reads in values and double checks that the values are correct
      for row in valuereader:
        # grab all but first one since that is variable name
        if row[0] == 'fc':
          fc.append(row[1:])
        elif row[0] == 'cc':
          cc.append(row[1:])
        elif row[0] == 'kc':
          kc.append(row[1:])
        else:
          print 'error in value'
  # return variables
  return fc, cc, kc

# function to create the intrinsic and distortion matricies based
#    on the variables recorded in the function above
def matricies(location):
  if location == 1:
    name = '../calibrations/Studio1-'
  elif location == 2:
    name = '../calibrations/Studio2-'
  elif location == 3:
    name = '../calibrations/Mez'
  else:
    print 'Error: can\'t retrieve matricies'

  # get the variable values
  fc, cc, kc = read_csvs(name)
  
  # set up the blanck matricies
  intrinsic_matrix = []
  distortion_coefficient = []

  # for each camera (assuming studio 1 at this point)
  for i in range(4):
    # from the parameters given in the .mat file create matricies
    intrinsic_matrix.append(np.array([[fc[i][1], 0.0,   cc[i][0]], 
                                      [0.0,   fc[i][1], cc[i][1]], 
                                      [0.0,   0.0,   1.0 ]], 
                                      dtype=np.float32))
    distortion_coefficient.append(np.array([kc[i][0], kc[i][1], kc[i][2], 
                                            kc[i][3], kc[i][4]], 
                                            dtype=np.float32))
  return intrinsic_matrix, distortion_coefficient