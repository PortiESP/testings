import RPi.GPIO as gp
import threading, Adafruit_ADS1x15, time

class portiOSDriver:
	def __init__(self, pins):
		self.pins = pins
		self.pin_Q0 = pins[0]
		self.pin_Q1 = pins[1]
		self.pin_Q2 = pins[2]
		self.pin_EI = pins[3]
		self.pin_CodData = pins[4]
		self.pin_CodBtn = pins[5]
		

		gp.setmode(gp.BOARD)
		tuple(map(lambda x: gp.setup(x, gp.IN, pull_up_down=gp.PUD_DOWN), self.pins))

		self.a2d = Adafruit_ADS1x15.ADS1115()

	def startListeners(self):
		gp.add_event_detect(self.pin_EI, gp.RISING, callback=self.encoderCallback, bouncetime=300)
		gp.add_event_detect(self.pin_CodBtn, gp.RISING, callback=self.rotEncoderButtonCallback, bouncetime=300)


	def encoderCallback(self):
		data = f"{gp.input(self.Q2)}{gp.input(self.Q1)}{gp.input(self.Q0)}"
		data = int(bin(data))
		print("Data: ", str(data))
		if data <= 4:
			print("Button ", str(data))
		elif data == 5:
			print("IRR data")
		elif data == 6:
			print("Encoder rotation:", str(gp.input(self.pin_CodData)))
		elif data == 7:
			print("Joystick button")

	def rotEncoderButtonCallback(self):
		print("Rotation encoder button")


