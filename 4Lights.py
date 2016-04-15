#Import Module
import RPi.GPIO as GPIO

#Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

#Poll for button press
while True:
    if GPIO.input(23)==1:
        GPIO.output(5,1)
    else:
        GPIO.output(5,0)
        
    if GPIO.input(24)==1:
        GPIO.output(6,1)
    else:
        GPIO.output(6,0)
        
    if GPIO.input(16)==1:
        GPIO.output(13,1)
    else:
        GPIO.output(13,0)
        
    if GPIO.input(20)==1:
        GPIO.output(19,1)
    else:
        GPIO.output(19,0)

GPIO.cleanup()



