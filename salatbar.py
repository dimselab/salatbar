from gpiozero import Buzzer
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

buzzer = Buzzer(17)

#buzzer.on();

print ("Ready...")
while  True:
	if (GPIO.input(18) == 0):
		print ("buzzer")
		buzzer.on()
	else:
		buzzer.off()
