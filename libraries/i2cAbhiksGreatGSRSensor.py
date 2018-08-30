import smbus


class AbhiksGreatGSRSensor:
    def __init__(self):
        self.address = 0x54


    def read(bus):
        firstbyte =  bus.read_byte(self.address)
        secondbyte = bus.read_byte(self.address)
        return (firstbyte << 8)+ secondbyte
