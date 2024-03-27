import RPi.GPIO as gpio
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
number = [0 for i in range(8)]
nums = [0, 5, 32, 64, 127, 255]
voltage = []

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

for i in nums:
    d_num = i % 256
    bin_num = bin(d_num)

    j = -1
    while bin_num[j] != 'b':
        number[j] = int(bin_num[j])
        j -= 1

    print("{}->{}".format(j, number))

    gpio.output (dac, number)
    volt = float(input())
    voltage.append(volt)

print(voltage)

gpio.output(dac, 0)
gpio.cleanup()