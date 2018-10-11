import smbus
import time
import os

class ECG:
    def __init__(self):
        self.address = 0x54


    def read(self, bus):
        firstbyte =  bus.read_byte(self.address)
        secondbyte = bus.read_byte(self.address)
        return (firstbyte << 8)+ secondbyte

class GSR:
    def __init__(self):
        self.address = 0x52


    def read(self, bus):
        firstbyte =  bus.read_byte(self.address)
        secondbyte = bus.read_byte(self.address)
        return (firstbyte << 8)+ secondbyte


class BREATH:
    def __init__(self):
        self.address = 0x50


    def read(self, bus):
        firstbyte =  bus.read_byte(self.address)
        secondbyte = bus.read_byte(self.address)
        return (firstbyte << 8)+ secondbyte

bus = smbus.SMBus(1)

ecg = ECG()
gsr = GSR()
breath = BREATH()

millis = int(round(time.time() * 1000))

ECGf = open("ECG" + str(time.time()) + "." + str(millis), "a+")
GSRf = open("GSR" + str(time.time()) + "." + str(millis), "a+")
Breathf = open("Breath" + str(time.time()) + "." + str(millis), "a+")

starttime=time.time()
while True:
  print time.time()
  ECGf.write(str(ecg.read(bus)) + ",")
  GSRf.write(str(gsr.read(bus)) + ",")
  Breathf.write(str(breath.read(bus)) + ",")
  time.sleep(.01 - ((time.time() - starttime) % .01))
