makevid
=======

a command line tool to un-distort, combine and help analyze multiple video feeds

resolutions
* Full - 2300 x 1850
* 1080 - 1342 x 1080
*  720 -  895 x  720
*  481 -  598 x  481




Flow chart:

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
