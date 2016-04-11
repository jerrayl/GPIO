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

#Initialize variables
sequence = []
mapping = [35,36,37,38]
score = 0
input_state = 4
failed = False
colors=["Red","Blue","Green","Yellow"]

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
GPIO.output(35,0)
GPIO.output(36,0)
GPIO.output(37,0)
GPIO.output(38,0)

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



