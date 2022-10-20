import RPi.GPIO as GPIO


GPIO_number = 25

def setting():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_number, GPIO.OUT)


def turn_on():
    GPIO.output(GPIO_number, GPIO.HIGH)


def turn_off():
    GPIO.output(GPIO_number, GPIO.LOW)