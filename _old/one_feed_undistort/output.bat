REM remove previous output file if there is one
del output.mpg
cd out

REM put images into file
..\..\MPlayer\mencoder "mf://*.png" -mf type=png:w=1280:h=960:fps=18 -ovc lavc -lavcopts vcodec=huffyuv:format=422p -oac copy -o huffyuv.avi
REM convert video to a stream
..\..\MPlayer\mplayer huffyuv.avi -vo yuv4mpeg
REM convert stream into video
..\..\MPlayer\ffmpeg -i stream.yuv -r 18 -b 6048k ..\output.avi
cd ..
rmdir temp /S /Q
rmdir out /S /Q