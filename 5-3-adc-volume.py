import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

led = [2, 3, 4, 17, 27, 22, 10, 9]
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setup(led, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)


def dec2bin(num):
    return [int(elem) for elem in bin(num)[2:].zfill(8)]


def adc2():
    k = 0
    for i in range(7, -1, -1):
        k += 2 ** i
        dac_val = dec2bin(k)
        GPIO.output(dac, dac_val)
        comp_val = GPIO.input(comp)
        sleep(0.1)
        if comp_val == 0:
            k -= 2 ** i
    return k


def adc1():
    for i in range(256):
        dac_val = dec2bin(i)
        GPIO.output(dac, dac_val)
        comp_val = GPIO.input(comp)
        sleep(0.1)
        if comp_val:
            return i
    return 0


def volume(val):
    val = int(val / 256 * 10)
    arr = [0] * 8
    for i in range(val - 1):
        arr[i] = 1
    return arr


try:
    while True:
        i = adc2()
        if i:
            voltage = i * 3.3 / 256.0
            print("{:.2f}V".format(voltage))
            volume_val = volume(i)
            GPIO.output(led, volume_val)
            # print(int(i / 256 * 10))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("EOP")