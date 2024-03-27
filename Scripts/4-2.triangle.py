import RPi.GPIO as GPIO
from time import sleep
from matplotlib import pyplot as plt
import numpy as np

def bin_system(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


GPIO.setwarnings (False)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode (GPIO.BCM)
GPIO.setup (dac, GPIO.OUT)

inc_flag = 1
t = 0
x = 0

try:
    period = float (input ("Type a period for sygnal: "))
    print (f"period = {period:.4}")
    while True:
        GPIO.output (dac, bin_system(x))

        voltage = float(x) / 256 * 3.3
        print (f"Output voltage is about {voltage:.4} volt")
        print (bin_system (x))

        if (x == 0):    inc_flag = 1
        elif (x == 255):    inc_flag = 0

        if inc_flag == 1:
            x += 1
        else:
            x -= 1

        sleep (period / 512)
        t += 1

except ValueError:
    print ("Inapropriate period!")

finally:
    GPIO.output (dac, 0)
    GPIO.cleanup ()
    print ("EOP")