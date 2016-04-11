import RPi.GPIO as GPIO
from time import sleep
from math import log1p
from random import random
from random import randint

#Initialize GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)

#Create Functions
def get_time(score):
    return 1/log1p(score+1)

def get_random_number(x):
    y = randint(0,3)
    if x==y:
        return randint(0,3)
    else:
        return y

def red(channel):
    GPIO.output(35,1)
    sleep(1)
    GPIO.output(35,0)
    print ("Red Pressed")
    global input_state
    input_state = 0
def blue(channel):
    GPIO.output(36,1)
    sleep(1)
    GPIO.output(36,0)
    print ("Blue Pressed")
    global input_state
    input_state = 1
def green(channel):
    GPIO.output(37,1)
    sleep(1)
    GPIO.output(37,0)
    print ("Green Pressed")
    global input_state
    input_state = 2
def yellow(channel):
    GPIO.output(38,1)
    sleep(1)
    GPIO.output(38,0)
    print ("Yellow Pressed")
    global input_state
    input_state = 3

GPIO.add_event_detect(11, GPIO.FALLING, callback=red, bouncetime=300)
GPIO.add_event_detect(12, GPIO.FALLING, callback=blue, bouncetime=300)
GPIO.add_event_detect(15, GPIO.RISING, callback=green, bouncetime=300)
GPIO.add_event_detect(16, GPIO.RISING, callback=yellow, bouncetime=300)

GPIO.output(35,0)
GPIO.output(36,0)
GPIO.output(37,0)
GPIO.output(38,0)

while True;
pass
GPIO.cleanup()



