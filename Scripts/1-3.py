import RPi.GPIO as rpi

rpi.setmode(rpi.BCM)

rpi.setup(26, rpi.OUT)
rpi.setup(23, rpi.IN)
rpi.output(26, rpi.input(23))

