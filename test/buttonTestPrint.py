import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

btnOne = 22
btnTwo = 24

GPIO.setup(btnOne, GPIO.IN)
GPIO.setup(btnTwo, GPIO.IN)

count = 0

while True:
    inputValue = GPIO.input(btnOne)
    if inputValue:
        count += 1
        print('Button pressed ' + str(count) + ' times.')
    time.sleep(0.1)
