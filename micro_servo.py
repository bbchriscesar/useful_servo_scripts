from gpiozero import AngularServo
from time import sleep

global servo
servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0024)

while True:
    sleep(0.1)
    servo.value=1
    sleep(.5)
    servo.detach()
    sleep(0.1)
    servo.value=-1
    sleep(.5)
    servo.detach()
