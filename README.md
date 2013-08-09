makevid
=======

a command line tool to un-distort, combine and help analyze multiple video feeds from RPI's EMPAC facility  
  
  
Requires the use of programs:
* mplayer
* mencoder
* ffmpeg  

Python libraries:
* numpy
* scipy
* opencv (cv2)

Included with python install:
* shutil
* os
* sys
* subprocess

Description
-----------

This tool is used specifically for the feeds from Studio1, Studio2 and Mez cameras in RPI's EMPAC facility.
For each location you can perform the following tasks:
* undistorting one image
* undistorting one feed of images
* stitching together multiple images
* stitching together multiple feeds of images

To do this consult the help text and use the appropriate flags. You can also change the defaults so that
running the program with no flags will produce the desired result. This is done by editing the actual source code.

When running this program for multiple images the filenames should be of the format 'location-cameraNumber.png'
for example 'Studio1-1.png'. The parent folder can be specifed seperately though.

When running this program for multiple feeds the files should be left in their origonal naming scheme with date and time information for a title and in folders numbered by the camera they were from. For example if all the Studio1 videos are in the parent folder Studio1/ the videos should be in Studio1/1/, Studio1/2/ and so on.


Help text
---------
The text below can be displayed with the -h flag, and shows what settings are available.
Some of the settings available are start and end time selection, parent folder location, which camera studio, resolution of the video (and therefore speed of stitching), and which cameras will be in the final product.
<pre>
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
                         720  = 908 x 730
                         480  = 604 x 486
  -s setting           specify which setting
                         1 = image
                         2 = feed
                         3 = images
                         4 = feeds
  -e event             pick event for date
                         1 = Gamefest
                         2 = Volleyball
                         3 = CRAIVE
                         4 = Graduate Sound Recording
</pre>
Flow chart
----------

                          makevid.py
                              |
                          settings.py
                      /                  \
                single cam            multi cam
                    |                     |
             init.py (matricies)        init.py (maps) 
                    |                        |
               undistort.py                 stitch.py
               /         \                 /        \
     undistort_image   undistort_feed    remap     remap_feed(for remap)
                             |                            |
                         bat files                   time_split.py
                                                          |
                                                     select_video
                                                          |
                                                     calc_frames
                                                          |                                                     
                                                     sync_frames
                                                          |                                                     
                                                     select_time
