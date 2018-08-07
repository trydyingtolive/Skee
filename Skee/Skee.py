import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    time.sleep(1)
    if GPIO.input(17):
        print("Pin 17 is HIGH")
    else:
        print("Pin 17 is LOW")
