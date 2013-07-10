REM remove and leftover temp files
rmdir temp /S /Q
rmdir out /S /Q

REM make directories for temp files
mkdir temp
mkdir out

cd temp
set name=..\%1
REM take video and seperate into image file
..\..\MPlayer\mplayer -vo png %name%
cd ..