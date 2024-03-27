import RPi.GPIO as rpi
import time

rpi.setmode(rpi.BCM)

rpi.setup(26, rpi.OUT)

for i in range(10):
    rpi.output(26, 1)
    time.sleep(1)
    rpi.output(26, 0)
    time.sleep(1)

rpi.output(26, 1)