#
# combines videos 
# give it path to folder with video files
# TODO: figure out why it needs to run twice
#

import os, sys

f = open('files.txt', 'w')

cwd = sys.argv[1]
listdir = os.listdir(cwd)

for name in listdir:
  if name[-4:] == '.avi':
    f.write('file \'' + cwd + '\\' + name + '\'\n')


# run this command
# ffmpeg\bin\ffmpeg -f concat -i files.txt -c copy output.avi