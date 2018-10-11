# thisfile is to grab all of the data on the i2c bus based on the the configuration file
#write it to files
# keep an open socket and stream it (via jttp https later)
import time
import smbus
import os

#import all of the devices on the bus for now

#from libraries.i2cMPU60501 import MPU60501
#from libraries.i2cMPU92500 import MPU92500
from libraries.i2cMAX30100 import MAX30100
from libraries.i2cMLX90614 import MLX90614
from libraries.i2cBMP280 import BMP280

bus = smbus.SMBus(1)

#defince product name
PRODUCT_NAME = "AbhiksHappininHat"
DATA_PATH = "AHH"


# extanciate and configure all of the objects

#mpu60501 = MPU60501(bus, DATA_PATH)
#mpu92500 = MPU92500(bus, DATA_PATH)
max30100 = MAX30100(bus)
mlx90614 = MLX90614(bus)
bmp280 = BMP280(bus)


print time.strftime('%d-%m-%Y-%H-%M-%S', time.localtime())
divider = 1
second = 0
starttime=time.time()
while True:
  #a bunch of if statementsfor each sensors
  if (divider % max30100.REFRESH_RATE == 0):
      max30100.log(bus)

  if (divider % mlx90614.REFRESH_RATE == 0):
      mlx90614.log(bus)

  if (divider % bmp280.REFRESH_RATE == 0):
      bmp280.log(bus)


  divider = divider + 1
  time.sleep(0.01 - ((time.time() - starttime) % 0.01))
