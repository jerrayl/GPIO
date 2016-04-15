import RPi.GPIO as GPIO
import sys
from pubnub import Pubnub

#Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

pubnub = Pubnub(publish_key='pub-c-75f0a823-194a-4f1f-8653-e0781497cfe1',subscribe_key='sub-c-7a9eb724-e8f4-11e5-baae-0619f8945a4f')

channel='lights'

GPIO.output(5,0)
GPIO.output(6,0)
GPIO.output(13,0)
GPIO.output(19,0)

def _callback(m,channel):
    print(m)
    if m['led'][0] == "red":
        GPIO.output(5,m['led'][1])
        print("red recieved")
    elif m['led'][0] == "blue":
        GPIO.output(6,m['led'][1])
        print("blue recieved")
    elif m['led'][0] == "green":
        GPIO.output(13,m['led'][1])
        print("green recieved")
    elif m['led'][0] == "yellow":
        GPIO.output(19,m['led'][1])
        print("yellow recieved")

def _error(m):
    print(m)

pubnub.subscribe(channels=channel,callback=_callback,error=_error)
