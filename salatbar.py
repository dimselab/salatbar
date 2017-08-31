####################################
# salatbar.dimselab.dk
#
###################################
from gpiozero import Buzzer
import RPi.GPIO as GPIO
from datetime import  datetime, time

### config pins
relayPin = 27
waterSensorPin = 18
buzzerPin = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(waterSensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(relayPin, GPIO.OUT)

buzzer = Buzzer(buzzerPin)

#buzzer.on();

now = datetime.now()
now_time = now.time()


print ("Ready...")
while  True:
	if (GPIO.input(waterSensorPin) == 0):
		print ("buzzer")
		buzzer.on()
	else:
		buzzer.off()

	# turn on  lights from 8-16
	if now_time >= time(8,00) and now_time <= time(16,00):
		print("Light On")
		GPIO.output(relayPin, GPIO.HIGH)
	else:
		print ("Light Off")
		GPIO.output(relayPin, GPIO.LOW)

	
