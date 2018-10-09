import time
class MPU92500:
	def __init__(self, bus, path):
		self.address = 0x68
		self.REFRESH_RATE = 1
		self.bus = bus
		self.name = "MPU92500"
		self.DATA_PATH = path

		# Power management registers
		power_mgmt_1 = 0x6b
		power_mgmt_2 = 0x6c
		self.bus.write_byte_data(self.address, power_mgmt_1, 0)

		#create files to log
                millis = int(round(time.time() * 1000))
                self.ACCEL_X_f = open(self.DATA_PATH + "-" + self.name + "-ACCEL_X-" + time.strftime('%d-%m-%Y-%H-%M-%S', time.localtime()) + "." + str(millis), "a+")
                self.ACCEL_Y_f = open(self.DATA_PATH + "-" + self.name + "-ACCEL_Y-" + time.strftime('%d-%m-%Y-%H-%M-%S', time.localtime()) + "." + str(millis), "a+")
                self.ACCEL_Z_f = open(self.DATA_PATH + "-" + self.name + "-ACCEL_Z-" + time.strftime('%d-%m-%Y-%H-%M-%S', time.localtime()) + "." + str(millis), "a+")
                self.GYRO_X_f = open(self.DATA_PATH + "-" + self.name + "-GYRO_X-" + time.strftime('%d-%m-%Y-%H-%M-%S', time.localtime()) + "." + str(millis), "a+")
                self.GYRO_Y_f = open(self.DATA_PATH + "-" + self.name + "-GYRO_Y-" + time.strftime('%d-%m-%Y-%H-%M-%S', time.localtime()) + "." + str(millis), "a+")
                self.GYRO_Z_f = open(self.DATA_PATH + "-" + self.name + "-GYRO_Z-" + time.strftime('%d-%m-%Y-%H-%M-%S', time.localtime()) + "." + str(millis), "a+")
#		MAG_X_f = open(self.DATA_PATH + "-" + self.name + "-MAG_X-" + time.strftime('%d-%m-%Y-%H-%M-%S', time.localtime()) + "." + str(millis), "a+")
#        MAG_Y_f = open(self.DATA_PATH + "-" + self.name + "-MAG_Y-" + time.strftime('%d-%m-%Y-%H-%M-%S', time.localtime()) + "." + str(millis), "a+")
#        MAG_Z_f = open(self.DATA_PATH + "-" + self.name + "-MAG_Z-" + time.strftime('%d-%m-%Y-%H-%M-%S', time.localtime()) + "." + str(millis), "a+")

	def read_word(self,adr):
    		high = self.bus.read_byte_data(self.address, adr)
    		low = self.bus.read_byte_data(self.address, adr+1)
    		val = (high << 8) + low
    		return val

	def read_word_2c(self,adr):
    		val = self.read_word(adr)
    		if (val >= 0x8000):
        		return -((65535 - val) + 1)
    		else:
        		return val

	def log(self,bus):
		self.ACCEL_X_f.write(str(self.read_word_2c(0x3b)) + ",")
		self.ACCEL_Y_f.write(str(self.read_word_2c(0x3d)) + ",")
		self.ACCEL_Z_f.write(str(self.read_word_2c(0x3f)) + ",")
		self.GYRO_X_f.write(str(self.read_word_2c(0x43)) + ",")
		self.GYRO_Y_f.write(str(self.read_word_2c(0x45)) + ",")
		self.GYRO_Z_f.write(str(self.read_word_2c(0x47)) + ",")
#		MAG_X_f.write(str(self.read_word_2c(0x04)) + ",")
#		MAG_Y_f.write(str(self.read_word_2c(0x06)) + ",")
#		MAG_Z_f.write(str(self.read_word_2c(0x08)) + ",")
		return True

        def end(self):
		self.ACCEL_X_f.close()
		self.ACCEL_Y_f.close()
		self.ACCEL_Z_f.close()
		self.GYRO_X_f.close()
		self.GYRO_Y_f.close()
		self.GYRO_Z_f.close()
#		MAG_X_f.close()
#		MAG_Y_f.close()
#		MAG_Z_f.close()
