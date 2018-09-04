class GSR:
    def __init__(self, bus):
        self.address = 0x52
	self.REFRESH_RATE = 1
        firstbyte =  bus.read_byte(self.address)
        secondbyte = bus.read_byte(self.address)
        #in case the bytes start off being read wrong
	if ((firstbyte << 8)+ secondbyte) > 1024:
            _ = bus.read_byte(self.address)


    def read(self, bus):
        firstbyte =  bus.read_byte(self.address)
        secondbyte = bus.read_byte(self.address)
        return (firstbyte << 8)+ secondbyte

