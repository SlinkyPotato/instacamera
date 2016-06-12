import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

blueLed = 5
redShutter = 16

GPIO.setup(blueLed, GPIO.OUT)
GPIO.setup(redShutter, GPIO.IN)

count = 0

while True:
    inputValue = GPIO.input(redShutter)
    if inputValue:
        count += 1
        print('Button pressed ' + str(count) + ' times.')
    time.sleep(0.1)
