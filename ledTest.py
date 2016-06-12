import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

blueLed = 5

GPIO.setup(blueLed, GPIO.OUT)
GPIO.output(blueLed, GPIO.HIGH)
GPIO.output(blueLed, GPIO.LOW)
