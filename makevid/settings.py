#
# ask initial settings
#

# TODO:
#   for images and feeds need to add more options for multiple filenames
#   settings for running on all files in folder
#



import sys

def set_settings(args):
  if args[1] == 'image':
    setting = 1
  elif args[1] == 'feed':
    setting = 2
  elif args[1] == 'images':
    setting = 3
  elif args[1] == 'feeds':
    setting = 4
  else:
    sys.exit()

  if args[2] == 'Studio1':
    location = 1
  elif args[2] == 'Studio2':
    location = 2
  elif args[2] == 'Mez':
    location = 3
  else:
    sys.exit()

  return setting, location, args[3], args[4]


def settings():

  setting = int(raw_input('''Enter number:
  \t1) undistort image
  \t2) undistort feed
  \t3) undistort images and stitch
  \t4) undistort feeds and stitch\n'''))

  if setting > 3 or setting < 1:
    sys.exit()

  location = int(raw_input('''Choose location:
  \t1) Studio 1
  \t2) Studio 2
  \t3) Mez\n'''))

  if location > 3 or location < 1:
    sys.exit()

  cam = int(raw_input('Enter camera number: '))

  filename = raw_input('Enter filename: ')

  return setting, location, cam, filename