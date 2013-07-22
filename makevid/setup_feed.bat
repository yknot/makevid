REM make directories for temp files
mkdir temp

cd temp
set name=..\%1
REM take video and seperate into image file
..\..\MPlayer\mplayer -vo png %name%
cd ..
