import time
import pigpio

# Connect to pigpio daemon
pi = pigpio.pi()

# Set up the pin the servo is connected to
SERVO_PIN = 18

# Set the maximum and minimum angles for the servo
MAX_ANGLE = 2000
MIN_ANGLE = 1000

while True:
    # Set servo to maximum angle
    pi.set_servo_pulsewidth(SERVO_PIN, MAX_ANGLE)
    time.sleep(2)

    # Set servo to minimum angle
    pi.set_servo_pulsewidth(SERVO_PIN, MIN_ANGLE)
    time.sleep(2)
