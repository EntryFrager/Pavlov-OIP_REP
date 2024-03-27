import RPi.GPIO as gpio
import time

leds = [2, 3, 4, 17, 27, 22, 10, 9]

gpio.setmode(gpio.BCM)
gpio.setup(leds, gpio.OUT)

for i in range(3):
    for j in range(8):
        gpio.output (leds[j], 1)
        time.sleep (1)
        gpio.output (leds[j], 0)

gpio.output (leds, 0)
gpio.cleanup ()