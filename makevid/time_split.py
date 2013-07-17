#
# splits the files to find the right time
#

import sys
import os

#######################################
def select_video(location, time):
  """Returns closest previous video to time given in location given"""
  name = ''
  for filename in os.listdir(location):
    if time[0] > int(filename[0:4]):
      name = filename
      continue
    elif time[0] == int(filename[0:4]):
      if time[1] > int(filename[5:7]):
        name = filename
        continue
      elif time[1] == int(filename[5:7]):
        if time[2] > int(filename[8:10]):
          name = filename
          continue
        elif time[2] == int(filename[8:10]):
          if time[3] > int(filename[11:13]):
            name = filename
            continue
          elif time[3] == int(filename[11:13]):
            if time[4] > int(filename[14:16]):
              name = filename
              continue
            elif time[4] == int(filename[14:16]):
              if time[5] > int(filename[17:19]):
                name = filename
                continue
              elif time[5] == int(filename[17:19]):
                if time[6] > int(filename[20:23]):
                  name = filename
                  continue
                elif time[6] == int(filename[20:23]):
                  name = filename
                  break
                else:
                  break
              else:
                break
            else:
              break
          else:
            break
        else:
          break
      else:
        break
    else:
      break

  if name == '':
    print 'No file found that far back'
    sys.exit(0)

  return name


#######################################
def calc_frames_off(filename, time):
  """calulates how many frames need to be removed from video to line it up with start time"""



time = [2013,04,27,11,39,43,000]
name = select_video("Studio1\\feeds",time)
print name
numOfFrames = calc_frames_off(name, time)
print numOfFrames
#######################################
def sync_frames(camNum, numOfFrames):
  """removes the front frames from the folder containing the extracted frames"""
  location = 'temp' + str(camNum)
  os.chdir(location)
  for filename in os.listdir('.'):
    num = str(int(filename[:-4]) - numOfFrames)
    z = 8 - len(num)
    zeros = '0'*z
    os.rename(filename, zeros + str(num) + '.png')

  os.chdir('..')