makevid
=======

a command line tool to un-distort, combine and help analyze multiple video feeds


Help text
---------
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
                         720  = 895 x 720
                         480  = 598 x 481
  -s setting           specify which setting
                         1 = image
                         2 = feed
                         3 = images
                         4 = feeds
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
