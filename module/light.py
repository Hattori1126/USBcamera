import RPi.GPIO as GPIO


def setting():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25, GPIO.OUT)


def turn_on():
    GPIO.output(25, GPIO.HIGH)


def turn_off():
    GPIO.output(25, GPIO.LOW)