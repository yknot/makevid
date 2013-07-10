REM remove and leftover temp files
rmdir out /S /Q
rmdir temp1 /S /Q
rmdir temp2 /S /Q
rmdir temp3 /S /Q
rmdir temp4 /S /Q

REM make directories for temp files
mkdir out
mkdir temp1
mkdir temp2
mkdir temp3
mkdir temp4

cd temp1
set name=..\%1
REM take video and seperate into image file
..\..\MPlayer\mplayer -vo png %name%
cd ..\temp2
set name=..\%2
REM take video and seperate into image file
..\..\MPlayer\mplayer -vo png %name%
cd ..\temp3
set name=..\%3
REM take video and seperate into image file
..\..\MPlayer\mplayer -vo png %name%
cd ..\temp4
set name=..\%4
REM take video and seperate into image file
..\..\MPlayer\mplayer -vo png %name%
cd ..