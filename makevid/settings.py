#
# ask initial settings
#
import sys
#######################################
def help():
  print """
usage: makevid.py [-h] [-t hour minute second] [-e hour minute second] [-f folder]
                   [-l location] [-r resolution] [-c cams]

Video feed stitching program

optional arguments:
  -h                   show this help message and exit
  -d                   show default settings and exit
  -t hour minute sec   set the start time
  -e hour minute sec   set the end time
  -f folder            set the parent folder or singular filename
  -l location          set location
                         1 = Studio1
                         2 = Studio2
                         3 = Mez
  -r resolution        set resolution
                         full = 2300 x 1850
                         1080 = 1342 x 1080
                         720  = 895 x 720
                         480  = 598 x 481
  -s setting           specify which setting
                         1 = image
                         2 = feed
                         3 = images
                         4 = feeds
  """
#######################################
def default(startHour, startMin, startSec, startMilli, endHour, endMin, endSec, endMilli, folder, location, resolution, cams, setting):
  print 'Defaults:'
  print '  startHour =', int(startHour)
  print '  startMin =', int(startMin)
  print '  startSec =', int(startSec)
  print '  startMilli =', int(startMilli)
  print '  endHour =', int(endHour)
  print '  endMin =', int(endMin)
  print '  endSec =', int(endSec)
  print '  endMilli =', int(endMilli)
  print '  folder =', folder
  print '  location =', int(location)
  print '  resolution =', resolution
  print '  cams =', cams
  print '  setting =', int(setting)

#######################################
def flags(args):
  """Interperet flags set by user"""

  ################################
  ######## DEFAULT VALUES ########  
  startHour = 11
  startMin = 39
  startSec = 45
  startMilli = 0
  endHour = 11
  endMin = 40
  endSec = 15
  endMilli = 0
  folder = 'Studio1\\feeds\\'
  location = 1
  resolution = '720'
  cams = '1234'
  setting = 4
  ################################

  # go through arguments and use flags to identitfy 
  for i in range(len(args)):
    if i == 0:
      continue
    elif args[i] == '-h':
      help()
      sys.exit()
    elif args[i] == '-d':
      default(startHour, startMin, startSec, startMilli, endHour, endMin, endSec, endMilli, folder, location, resolution, cams, setting)
      sys.exit()
    elif args[i] == '-t':
      startHour = int(args[i+1])
      startMin = int(args[i+2])
      startSec = int(args[i+3])
    elif args[i] == '-e':
      endHour = int(args[i+1])
      endMin = int(args[i+2])
      endSec = int(args[i+3])
    elif args[i] == '-f':
      folder = args[i+1]
    elif args[i] == '-l':
      location = int(args[i+1])
    elif args[i] == '-r':
      resolution = args[i+1]
    elif args[i] == '-c':
      cams = args[i+1]
    elif args[i] == '-s':
      setting = int(args[i+1])
    else:
      continue

  # seperate the cams into a list
  c = []
  for letter in cams:
    c.append(int(letter))

  # return all the settings
  return [2013, 4, 27, startHour, startMin, startSec, startMilli], [2013, 4, 27, endHour, endMin, endSec, endMilli], folder, location, resolution, c, setting

#######################################