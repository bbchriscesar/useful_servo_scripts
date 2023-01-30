import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

seconds = 10
print("reverse")

GPIO.output(17, False)
GPIO.output(22, True)
while seconds > 0:
    if GPIO.input(21) == 0:
        GPIO.output(17, False)
        GPIO.output(22, False)
        seconds = -1
    seconds = seconds - 1
    time.sleep(0.5)

GPIO.output(17, False)
GPIO.output(22, False)

GPIO.cleanup()
