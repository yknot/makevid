del output.mpg
cd out
..\..\MPlayer\mencoder "mf://*.png" -mf type=png -ovc lavc -lavcopts vcodec=huffyuv:format=422p -oac copy -o huffyuv.avi
..\..\MPlayer\mplayer huffyuv.avi -vo yuv4mpeg
..\..\MPlayer\ffmpeg -i stream.yuv -b 6048k ..\output.mpg
cd ..
rmdir temp /S /Q
rmdir out /S /Q