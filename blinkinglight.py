#Import Modules
import RPi.GPIO as GPIO
from time import sleep

#Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(5, GPIO.OUT)


#Poll for button press
for i in range(10):
  GPIO.output(5,1)
  sleep(1)
  GPIO.output(5,0)
  sleep(1)

GPIO.cleanup()
