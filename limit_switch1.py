import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# moving upward
StepPins = [23, 24, 18, 17]

for pin in StepPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

Seq = [[1, 0, 0, 1],
       [1, 0, 0, 0],
       [1, 1, 0, 0],
       [0, 1, 0, 0],
       [0, 1, 1, 0],
       [0, 0, 1, 0],
       [0, 0, 1, 1],
       [0, 0, 0, 1]]

while GPIO.input(18):
    for halfstep in range(8):
        for pin in range(4):
            GPIO.output(StepPins[pin], Seq[halfstep][pin])
        time.sleep(0.01)

print("limit switch")

GPIO.cleanup()