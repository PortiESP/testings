import RPi.GPIO as gp
import threading, Adafruit_ADS1x15, time

class portiOSDriver:
	def __init__(self, pins):
		self.pins = pins
		self.pin_Q0 = pins[0]
		self.pin_Q1 = pins[1]
		self.pin_Q2 = pins[2]
		self.pin_E0 = pins[3]
		self.pin_CodData = pins[4]
		self.pin_CodBtn = pins[5]
		

		gp.setmode(gp.BOARD)
		tuple(map(lambda x: gp.setup(x, gp.IN, pull_up_down=gp.PUD_DOWN), self.pins))

		self.a2d = Adafruit_ADS1x15.ADS1115()

	def startListeners(self):
		gp.add_event_detect(self.pin_E0, gp.FALLING, callback=self.encoderCallback, bouncetime=300)
		gp.add_event_detect(self.pin_CodBtn, gp.FALLING, callback=self.rotEncoderButtonCallback, bouncetime=300)


	def encoderCallback(self, _):
		data = (gp.input(self.pin_Q2)*4) + (gp.input(self.pin_Q1)*2) + gp.input(self.pin_Q0)
		print("Data: ", str(data))
		if data <= 4:
			print("Button ", str(data))
		elif data == 5:
			print("IRR data")
		elif data == 6:
			print("Encoder rotation:", str(gp.input(self.pin_CodData)))
		elif data == 7:
			print("Joystick button")

	def rotEncoderButtonCallback(self, _):
		print("Rotation encoder button")


driver = portiOSDriver((37,35,33,31,29,23))
print("Started driver")
driver.startListeners()
while 1:
	time.sleep(0.1)
		
