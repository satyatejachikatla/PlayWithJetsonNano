import RPi.GPIO as GPIO
import time

# These are the pin numbers written on the board.
led_pins = [[37,35,33] , [31,29,32] , [23,21,19]]

led_pins_shape = (3,3)

frame_sleep_time = 0.1

frames_diagonal = [
	[
	 [1,0,0],
	 [0,0,0],
	 [0,0,0]
	],
	[
	 [0,1,0],
	 [1,0,0],
	 [0,0,0]
	],
	[
	 [0,0,1],
	 [0,1,0],
	 [1,0,0]
	],
	[
	 [0,0,0],
	 [0,0,1],
	 [0,1,0]
	],
	[
	 [0,0,0],
	 [0,0,0],
	 [0,0,1]
	],
	[
	 [0,0,0],
	 [0,0,1],
	 [0,1,0]
	],
	[
	 [0,0,1],
	 [0,1,0],
	 [1,0,0]
	],
	[
	 [0,1,0],
	 [1,0,0],
	 [0,0,0]
	],
]



def init():
	GPIO.setmode(GPIO.BOARD)
	for line in led_pins:
		for pin in line:
			GPIO.setup(pin, GPIO.OUT)

			#Set Led Off Initially
			GPIO.output(pin, GPIO.LOW)

def print_pattern(pattern):
	for i in range(led_pins_shape[0]):
		for j in range(led_pins_shape[1]):
			if pattern[i][j] == 0:
				GPIO.output(led_pins[i][j], GPIO.LOW)
			else:
				GPIO.output(led_pins[i][j], GPIO.HIGH)

def blink_loop():
	try:
		while True:
			for pattern in frames_diagonal:
				print_pattern(pattern)
				time.sleep(frame_sleep_time)
	except KeyboardInterrupt:
		pass
	finally:
		GPIO.cleanup()

if __name__ == '__main__':
	init()
	blink_loop()