import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
StepPins = [24, 25, 8, 7]

for pin in StepPins:
    print("Setup pins")
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

WaitTime = 0.001

# Define simple sequence
StepCount1 = 4
Seq1 = []
Seq1 = [i for i in range(0, StepCount1)]
Seq1[0] = [1, 0, 0, 0]
Seq1[1] = [0, 1, 0, 0]
Seq1[2] = [0, 0, 1, 0]
Seq1[3] = [0, 0, 0, 1]
# Define advanced half-step sequence
StepCount2 = 8
Seq2 = []
Seq2 = [i for i in range(0, StepCount2)]
Seq2[0] = [1, 0, 0, 0]
Seq2[1] = [1, 1, 0, 0]
Seq2[2] = [0, 1, 0, 0]
Seq2[3] = [0, 1, 1, 0]
Seq2[4] = [0, 0, 1, 0]
Seq2[5] = [0, 0, 1, 1]
Seq2[6] = [0, 0, 0, 1]
Seq2[7] = [1, 0, 0, 1]
# Choose a sequence to use
Seq = Seq2
StepCount = StepCount2


def steps(nb):
    StepCounter = 0
    if nb < 0:
        sign = -1
    else:
        sign = 1
    nb = sign * nb * 2  # times 2 because half-step
    print("nbsteps {} and sign {}".format(nb, sign))
    for i in range(nb):
        for pin in range(4):
            xpin = StepPins[pin]
            if Seq[StepCounter][pin] != 0:
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin, False)
        StepCounter += sign
        # If we reach the end of the sequence
        # start again
        if StepCounter == StepCount:
            StepCounter = 0
        if StepCounter < 0:
            StepCounter = StepCount - 1
        # Wait before moving on
        time.sleep(WaitTime)


# Start main loop
nbStepsPerRev = 2048
if __name__ == '__main__':
    hasRun = False
    while not hasRun:
        steps(nbStepsPerRev)
        hasRun = True

    print("Stop motor")
    for pin in StepPins:
        GPIO.output(pin, False)
    GPIO.cleanup()
