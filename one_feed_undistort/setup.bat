REM rmdir temp /S /Q
REM rmdir out /S /Q
mkdir temp
mkdir out
cd temp
..\..\MPlayer\mplayer -vo png ..\Studio1-1.avi
cd ..