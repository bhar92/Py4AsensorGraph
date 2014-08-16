import sys
from android import Android
import json
import time


droid = Android()
dt = 0.1 	# dt = 100ms
droid.startSensingTimed(1,dt)
droid.webViewShow('file:///sdcard/sl4a/scripts/SensorGraph/Accelerometer/accUI.html')
xList = [0] * 20
yList = [0] * 20
zList = [0] * 20

def postAccelerometerValues():
	xyzList = droid.sensorsReadAccelerometer().result
		
	xList.append(xyzList[0])
	yList.append(xyzList[1])
	zList.append(xyzList[2])

	del xList[0]
	del yList[0]
	del zList[0]
	
	xyzDict = {"x":xList, "y":yList, "z":zList}
	droid.eventPost('stdout', json.dumps(xyzDict))
 
i = 0
while True: 
    postAccelerometerValues()
    time.sleep(0.3)

    