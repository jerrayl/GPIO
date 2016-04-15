import RPi.GPIO as GPIO
from time import sleep
from math import log1p
from random import random
from random import randint

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
    GPIO.output(5,1)
    sleep(1)
    GPIO.output(5,0)
    print ("Red Pressed")
    global input_state
    input_state = 0
    
def white(channel):
    GPIO.output(6,1)
    sleep(1)
    GPIO.output(6,0)
    print ("White Pressed")
    global input_state
    input_state = 1
    
def green(channel):
    GPIO.output(13,1)
    sleep(1)
    GPIO.output(13,0)
    print ("Green Pressed")
    global input_state
    input_state = 2
    
def yellow(channel):
    GPIO.output(19,1)
    sleep(1)
    GPIO.output(19,0)
    print ("Yellow Pressed")
    global input_state
    input_state = 3

GPIO.add_event_detect(23, GPIO.RISING, callback=red, bouncetime=300)
GPIO.add_event_detect(24, GPIO.RISING, callback=white, bouncetime=300)
GPIO.add_event_detect(16, GPIO.RISING, callback=green, bouncetime=300)
GPIO.add_event_detect(20, GPIO.RISING, callback=yellow, bouncetime=300)

#Initialize variables
sequence = []
mapping = [5,6,13,19]
score = 0
input_state = 4
failed = False
colors=["Red","White","Green","Yellow"]

#Intro
print("Welcome to the Simon Game!")
print("Please remember the sequence displayed and enter it.")
print("Press any button to start")
while input_state==4:
    GPIO.output(mapping[randint(0,3)],randint(0,1))
    sleep(random()/2)

#Reset
sleep(5)
input_state=4
GPIO.output(5,0)
GPIO.output(6,0)
GPIO.output(13,0)
GPIO.output(19,0)

#Main
while not failed:
    #Add to sequence    
    if sequence:
        sequence.append(get_random_number(sequence[-1]))
    else:
        sequence.append(randint(0,3))
    #Display sequence    
    for i in sequence:
        GPIO.output(mapping[i],1)
        sleep(get_time(score))
        GPIO.output(mapping[i],0)
        sleep(0.4)
        print(colors[i])
    input_state=4    
    #Get input       
    for i in sequence:
        if failed:
            break
        while True:
            if input_state==i:
                print("Correct")
                input_state=4
                break
            elif input_state!=4 and input_state!=i:
                print(input_state)
                print("Failed")
                failed=True
                break
    score+=1
    sleep(2)
print("Game over! Your Score is",score)

GPIO.cleanup()



