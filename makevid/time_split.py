#
# splits the files to find the right time
#
import sys
import os
#######################################
def sync_frames(camNum, numOfFrames, start):
  """removes the front frames from the folder containing the extracted frames"""
  location = 'temp' + str(camNum)
  os.chdir(location)
  if start:
    for filename in os.listdir('.'):
      num = str(int(filename[:-4]) - numOfFrames)
      if int(num) < 1:
        os.remove(filename)
      else:
        z = 8 - len(num)
        zeros = '0'*z
        os.rename(filename, zeros + str(num) + '.png')
  else:
    for filename in os.listdir('.'):
      num = str(filename[:-4])
      if int(filename[:-4]) > numOfFrames:
        os.remove(filename)

  os.chdir('..')

#######################################
def select_time():
  return [2013,4,27,11,39,43,500], [2013,4,27,11,39,44,0]
  start_time = [0]*7
  temp = raw_input('Enter Start: year month day hour minute seconds milliseconds\n')
  temp = temp.split()
  for i in range(len(temp)):
    start_time[i] = int(temp[i])

  end_time = [0]*7
  temp = raw_input('Enter End: year month day hour minute seconds milliseconds\n')
  temp = temp.split()
  for i in range(len(temp)):
    end_time[i] = int(temp[i])

  # return start_time, end_time

#######################################
def calc_frames_off(startName, startTime, endName, endTime):
  """calulates how many frames need to be removed from video to line it up with start time"""
  diff = [0]*7
  diff[0] = startTime[0] - int(startName[0:4])
  diff[1] = startTime[1] - int(startName[5:7])
  diff[2] = startTime[2] - int(startName[8:10])
  diff[3] = startTime[3] - int(startName[11:13])
  diff[4] = startTime[4] - int(startName[14:16])
  diff[5] = startTime[5] - int(startName[17:19])
  diff[6] = startTime[6] - int(startName[20:23])
  if diff[6] < 0:
    diff[5] = diff[5] - 1
    diff[6] = 1000 + diff[6]
    if diff[5] < 0:
      diff[4] = diff[4] - 1
      diff[5] = 60 + diff[5]
      if diff[4] < 0:
        diff[3] = diff[3] - 1
        diff[4] = 60 + diff[4]
        if diff[3] < 0:
          diff[2] = diff[2] - 1
          diff[3] = 24 + diff[3]
          if diff[2] < 0:
            diff[1] = diff[1] - 1
            diff[2] = 30 + diff[2]
            if diff[1] < 0:
              diff[0] = diff[0] - 1
              diff[1] = 12 + diff[1]

  startFrames = diff[5]*1000 + diff[6]
  # print 'start frames', startFrames
  # print 'diffs before end', diff
  diff[0] = endTime[0] - int(endName[0:4])
  diff[1] = endTime[1] - int(endName[5:7])
  diff[2] = endTime[2] - int(endName[8:10])
  diff[3] = endTime[3] - int(endName[11:13])
  diff[4] = endTime[4] - int(endName[14:16])
  diff[5] = endTime[5] - int(endName[17:19])
  diff[6] = endTime[6] - int(endName[20:23])
  if diff[6] < 0:
    diff[5] = diff[5] - 1
    diff[6] = 1000 + diff[6]
    if diff[5] < 0:
      diff[4] = diff[4] - 1
      diff[5] = 60 + diff[5]
      if diff[4] < 0:
        diff[3] = diff[3] - 1
        diff[4] = 60 + diff[4]
        if diff[3] < 0:
          diff[2] = diff[2] - 1
          diff[3] = 24 + diff[3]
          if diff[2] < 0:
            diff[1] = diff[1] - 1
            diff[2] = 30 + diff[2]
            if diff[1] < 0:
              diff[0] = diff[0] - 1
              diff[1] = 12 + diff[1]
  # print 'diffs after end', diff
  endFrames = startFrames + diff[5]*1000 + diff[6] 
  startFrames = startFrames / 50
  endFrames = endFrames / 50
  return startFrames, endFrames

#######################################
def select_video(location, time):
  """Returns closest video to time given in location given"""
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