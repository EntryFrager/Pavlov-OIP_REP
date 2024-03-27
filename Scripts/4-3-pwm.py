import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BCM)
GPIO.setup (26, GPIO.OUT)

n = 10
p = GPIO.PWM (26, 1000)
p.start(0)

try:
    while True:
        f = int(input())
        p.ChangeDutyCycle (f)
        print (3.3 * f / 100)

finally:
    p.stop ()
    GPIO.output (26, 0)
    GPIO.cleanup ()