import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

blueLed = 5

GPIO.setup(blueLed, GPIO.OUT)

GPIO.output(blueLed, GPIO.HIGH)
