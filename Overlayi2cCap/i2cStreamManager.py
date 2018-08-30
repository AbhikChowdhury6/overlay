# thisfile is to grab all of the data on the i2c bus based on the the configuration file
#write it to files
# keep an open socket and stream it (via jttp https later)
import time
import smbus
import os
#import all of the devices on the bus for now




bus = smbus.SMBus(1)

# extanciate and configure all of the objects
ECG =
GSR =
Breath =
MPU6050 =
MPU9250 =

millis = int(round(time.time() * 1000))

#open files to log
ECGf = open("MPU6050" + str(time.time()) + "." + str(millis), "a+")
GSRf = open("MPU6050" + str(time.time()) + "." + str(millis), "a+")
Breathf = open("MPU6050" + str(time.time()) + "." + str(millis), "a+")
MPU6050f = open("MPU6050" + str(time.time()) + "." + str(millis), "a+")
MPU9250f = open("MPU6050" + str(time.time()) + "." + str(millis), "a+")

divider = 0
second = 0
starttime=time.time()
while True:
  #a bunch of if statementsfor each sensors
  if (divider % ECG.REFRESH_RATE == 0):
    ECGf.write(ECG.READ())

  if (divider % GSR.REFRESH_RATE == 0):
    GSRf.write(GSR.READ())

  if (divider % Breath.REFRESH_RATE == 0):
    Breathf.write(Breath.READ())

  if (divider % MPU6050.REFRESH_RATE == 0):
    MPU6050f.write(MPU6050.READ())

  if (divider % MPU9250.REFRESH_RATE == 0):
    MPU9250f.write(MPU9250.READ())

  if (divider % 100 == 0):
      second = second + 1
      if (second % 60 == 0):
        second = 0
        millis = int(round(time.time() * 1000))
        #close all files
        ECGf.close()
        GSRf.close()
        Breathf.close()
        MPU6050f.close()
        MPU9250f.close()
        #Open new files to log
        ECGf = open("MPU6050" + str(time.time()) + "." + str(millis), "a+")
        GSRf = open("MPU6050" + str(time.time()) + "." + str(millis), "a+")
        Breathf = open("MPU6050" + str(time.time()) + "." + str(millis), "a+")
        MPU6050f = open("MPU6050" + str(time.time()) + "." + str(millis), "a+")
        MPU9250f = open("MPU6050" + str(time.time()) + "." + str(millis), "a+")

  divider = divider + 1
  time.sleep(0.01 - ((time.time() - starttime) % 0.01))
