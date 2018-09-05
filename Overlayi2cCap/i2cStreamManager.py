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
from libraries.i2cMPU60501 import MPU60501
from libraries.i2cMPU92500 import MPU92500

bus = smbus.SMBus(1)

#defince product name
PRODUCT_NAME = "AbhiksPoppinPostureCorrector"
DATA_PATH = "AHH"


# extanciate and configure all of the objects
ecg = ECG(bus, DATA_PATH)
gsr = GSR(bus, DATA_PATH)
breath = BREATH(bus, DATA_PATH)
mpu60501 = MPU60501(bus, DATA_PATH)
mpu92500 = MPU92500(bus, DATA_PATH)



print time.strftime('%d-%m-%Y-%H-%M-%S', time.localtime())
divider = 1
second = 0
starttime=time.time()
while True:
  #a bunch of if statementsfor each sensors
  if (divider % ecg.REFRESH_RATE == 0):
      ecg.log(bus)

  if (divider % gsr.REFRESH_RATE == 0):
      gsr.log(bus)

  if (divider % breath.REFRESH_RATE == 0):
      breath.log(bus)

  if (divider % mpu60501.REFRESH_RATE == 0):
      mpu60501.log(bus)

  if (divider % mpu92500.REFRESH_RATE == 0):
      mpu92500.log(bus)

  divider = divider + 1
  time.sleep(0.01 - ((time.time() - starttime) % 0.01))
