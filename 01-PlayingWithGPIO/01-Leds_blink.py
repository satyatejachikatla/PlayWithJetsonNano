import RPi.GPIO as GPIO
import time

# These are the pin numbers written on the board.
led_pins = [37,35,33,31,29,31, 23,21,19]

def init(pins):
	GPIO.setmode(GPIO.BOARD)
	for pin in pins:
		GPIO.setup(pin, GPIO.OUT)

		#Set Led Off Initially
		GPIO.output(pin, GPIO.LOW)

def on_led(pins):
	for pin in pins:
		GPIO.output(pin, GPIO.HIGH)
def off_led(pins):
	for pin in pins:
		GPIO.output(pin, GPIO.LOW)

def blink_loop(led_pins):
	try:
		while True:
			on_led(led_pins)
			time.sleep(1)
			off_led(led_pins)
			time.sleep(1)
	except KeyboardInterrupt:
		pass
	finally:
		GPIO.cleanup()

if __name__ == '__main__':
	init(led_pins)
	blink_loop(led_pins)