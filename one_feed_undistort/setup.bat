REM remove and leftover temp files
rmdir temp /S /Q
rmdir out /S /Q

REM make directories for temp files
mkdir temp
mkdir out

cd temp
REM take video and seperate into image file
..\..\MPlayer\mplayer -vo png ..\Studio1-1.avi
cd ..