import time

class GSR:
    def __init__(self):
        self.address = 0x52
        firstbyte =  bus.read_byte(self.address)
        secondbyte = bus.read_byte(self.address)
        if ((firstbyte << 8)+ secondbyte) > 1024:
            _ = bus.read_byte(self.address)


    def read(self, bus):
        firstbyte =  bus.read_byte(self.address)
        secondbyte = bus.read_byte(self.address)
        return (firstbyte << 8)+ secondbyte


bus = smbus.SMBus(1)
gsr = GSR()

starttime=time.time()
while True:
  val = gsr.read(bus)
  h = int(val/8)
  o = ""
  for _ in range(h):
      o = o +"#"
  print str(val) + "\t" + o
  time.sleep(.01 - ((time.time() - starttime) % .01))
