import RPi.GPIO as rpi

rpi.setmode(rpi.BCM)

rpi.setup(23, rpi.OUT)
rpi.output(23, 1)