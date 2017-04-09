import json
import time
from android import Android

droid = Android()
# dt = 100ms
dt = 0.1
droid.startSensingTimed(1, dt)
droid.webViewShow('file:///sdcard/sl4a/scripts' +
                  '/SensorGraph/OrientationSensor/gyroUI.html')
xList = [0] * 20
yList = [0] * 20
zList = [0] * 20

def postOrientationSensorValues():
    xyzList = droid.sensorsReadOrientation().result

    xList.append(xyzList[0])
    yList.append(xyzList[1])
    zList.append(xyzList[2])

    del xList[0]
    del yList[0]
    del zList[0]

    xyzDict = {"x":xList, "y":yList, "z":zList}
    droid.eventPost('stdout', json.dumps(xyzDict))

while True:
    postOrientationSensorValues()
    time.sleep(0.3)