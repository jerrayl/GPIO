import RPi.GPIO as GPIO
import sys
from pubnub import Pubnub

#Initialize GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)

pubnub = Pubnub(publish_key='pub-c-75f0a823-194a-4f1f-8653-e0781497cfe1',subscribe_key='sub-c-7a9eb724-e8f4-11e5-baae-0619f8945a4f')

channel='lights'

GPIO.output(35,0)
GPIO.output(36,0)
GPIO.output(37,0)
GPIO.output(38,0)

def _callback(m,channel):
    print(m)
    if m['led'][0] == "red":
        GPIO.output(35,m['led'][1])
        print("red recieved")
    elif m['led'][0] == "blue":
        GPIO.output(36,m['led'][1])
        print("blue recieved")
    elif m['led'][0] == "green":
        GPIO.output(37,m['led'][1])
        print("green recieved")
    elif m['led'][0] == "yellow":
        GPIO.output(38,m['led'][1])
        print("yellow recieved")
    elif m['led'][0] == "reset":
        GPIO.output(35,0)
        GPIO.output(36,0)
        GPIO.output(37,0)
        GPIO.output(38,0)
    print(GPIO.input(35))
    print(GPIO.input(36))
    print(GPIO.input(37))
    print(GPIO.input(38))

def _error(m):
    print(m)

pubnub.subscribe(channels=channel,callback=_callback,error=_error)
