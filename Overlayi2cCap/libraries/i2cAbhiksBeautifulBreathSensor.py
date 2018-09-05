class BREATH:
    def __init__(self, bus, path):
        self.name = "AbhiksBeautifulBreathSensor"
        self.address = 0x50
	    self.REFRESH_RATE = 1
        self.DATA_PATH = path
        millis = int(round(time.time() * 1000))
        BREATH_f = open(self.DATA_PATH + "-" + self.name + "-raw-" + time.strftime('%d-%m-%Y-%H-%M-%S', time.localtime()) + "." + str(millis), "a+")
        #in case the bytes start off being read wrong
        firstbyte =  bus.read_byte(self.address)
        secondbyte = bus.read_byte(self.address)
	    if ((firstbyte << 8)+ secondbyte) > 1024:
            _ = bus.read_byte(self.address)


    def log(self, bus):
        firstbyte =  bus.read_byte(self.address)
        secondbyte = bus.read_byte(self.address)
        BREATH_f.write(str((firstbyte << 8)+ secondbyte) + ",")
        return True

    def end():
        BREATH_f.close()
