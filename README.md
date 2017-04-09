WARNING: Currently, as it is, the scripts and below instructions do not work when I tested them on a Nexus 6P running Android 7.1.2. 

Py4AsensorGraph
===============

Plotting an Android phone's accelerometer, gyro and magnetometer values with Python using [SL4A](https://code.google.com/p/android-scripting/), [Py4A](https://code.google.com/p/python-for-android/) and [Flot](http://www.flotcharts.org/). Short video demo can be found [here](https://www.youtube.com/watch?v=79S9gTuYy9M).

## Installing necessary apps:

1. Download and install the latest [SL4A App apk file](https://github.com/kuri65536/sl4a/releases).
2. Then download and install [Py4A App apk file](https://github.com/kuri65536/python-for-android/releases/download/r26/PythonForAndroid-debug-r26.apk).
    -  Open Python for Android and press Install
    
## Copying the programs: 

Copy the SensorGraph file into `/sdcard/sl4a/scripts`

## Running a program(an example):

1. Open the SL4A app:
    - Click on SensorGraph
    - Click on Accelerometer
    - Click on accGraph.py
    - Click on the 'Shell' icon(it looks like [this](http://screenshots.en.sftcdn.net/blog/en/2008/08/screen-capture-2.png)) to run the program.

## Exiting the program:

  1. Swipe down on your status bar.
    - Click on SL4A service
    - Long press on the program name
    - Click on 'Stop'
    - Press back and click on 'Yes'

### Screenshot:

![Accelerometer Graph](http://i.imgur.com/IIxFEXh.jpg?1)
