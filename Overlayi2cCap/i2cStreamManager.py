# thisfile is to grab all of the data on the i2c bus based on the the configuration file
#write it to files
# keep an open socket and stream it (via jttp https later)
import time
import smbus
import os

#import all of the devices on the bus for now
from libraries.i2cAbhiksExcitingECG import ECG
from libraries.i2cAbhiksGreatGSRSensor import GSR
from libraries.i2cAbhiksBeautifulBreathSensor import BREATH
from libraries.i2cMPU6050 import MPU6050
from libraries.i2cMPU9250 import MPU9250

bus = smbus.SMBus(1)



#defince product name
PRODUCT_NAME = "AbhiksPoppinPostureCorrector"
DATA_PATH = ""
# extanciate and configure all of the objects
ecg = ECG(bus)
gsr = GSR(bus)
breath = BREATH(bus)
mpu6050 = MPU6050(bus)
mpu9250 = MPU9250(bus)

mpu6050.address = 0x69

millis = int(round(time.time() * 1000))

print time.strftime('%d-%m-%Y-%H-%M-%S', time.localtime()) + "." + str(millis)

#open files to log
ECGf = open(DATA_PATH + "ECG-" + time.strftime('%d-%m-%Y-%H-%M-%S', time.localtime()) + "." + str(millis), "a+")
GSRf = open(DATA_PATH + "GSR-" + time.strftime('%d-%m-%Y-%H-%M-%S', time.localtime()) + "." + str(millis), "a+")
Breathf = open(DATA_PATH + "BREATH-" + time.strftime('%d-%m-%Y-%H-%M-%S', time.localtime()) + "." + str(millis), "a+")
MPU6050f = open(DATA_PATH + "MPU6050-" + time.strftime('%d-%m-%Y-%H-%M-%S', time.localtime()) + "." + str(millis), "a+")
MPU9250f = open(DATA_PATH + "MPU9250-" + time.strftime('%d-%m-%Y-%H-%M-%S', time.localtime()) + "." + str(millis), "a+")

divider = 1
second = 0
starttime=time.time()
while True:
  #a bunch of if statementsfor each sensors
  if (divider % ecg.REFRESH_RATE == 0):
    ECGf.write(str(ecg.read(bus)))

  if (divider % gsr.REFRESH_RATE == 0):
    GSRf.write(str(gsr.read(bus)))

  if (divider % breath.REFRESH_RATE == 0):
    Breathf.write(str(breath.read(bus)))

  if (divider % mpu6050.REFRESH_RATE == 0):
    MPU6050f.write(str(mpu6050.read(bus)))

  if (divider % mpu9250.REFRESH_RATE == 0):
    MPU9250f.write(str(mpu9250.read(bus)))

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
        ECGf = open(DATA_PATH + "ECG-" + time.strftime('%d-%m-%Y-%H-%M-%S', time.localtime()) + "." + str(millis), "a+")
	GSRf = open(DATA_PATH + "GSR-" + time.strftime('%d-%m-%Y-%H-%M-%S', time.localtime()) + "." + str(millis), "a+")
	Breathf = open(DATA_PATH + "BREATH-" + time.strftime('%d-%m-%Y-%H-%M-%S', time.localtime()) + "." + str(millis), "a+")
	MPU6050f = open(DATA_PATH + "MPU6050-" + time.strftime('%d-%m-%Y-%H-%M-%S', time.localtime()) + "." + str(millis), "a+")
	MPU9250f = open(DATA_PATH + "MPU9250-" + time.strftime('%d-%m-%Y-%H-%M-%S', time.localtime()) + "." + str(millis), "a+")

  divider = divider + 1
  time.sleep(0.01 - ((time.time() - starttime) % 0.01))
