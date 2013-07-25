REM remove previous output file if there is one
del output.avi
cd out

REM put images into file
..\..\MPlayer\mencoder "mf://*.png" -mf type=png:w=895:h=720:fps=18 -ovc lavc -lavcopts vcodec=huffyuv:format=422p -oac copy -o huffyuv.avi
REM convert video to a stream
..\..\MPlayer\mplayer huffyuv.avi -vo yuv4mpeg
REM convert stream into video
..\..\MPlayer\ffmpeg -i stream.yuv -r 18 -b 6048k ..\output.avi
cd ..

REM rmdir out /S /Q
REM rmdir temp /S /Q
REM rmdir temp1 /S /Q
REM rmdir temp2 /S /Q
REM rmdir temp3 /S /Q
REM rmdir temp4 /S /Q