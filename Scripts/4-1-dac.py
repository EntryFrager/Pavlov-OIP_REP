import RPi.GPIO as GPIO

def bin_system(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


GPIO.setwarnings (False)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode (GPIO.BCM)
GPIO.setup (dac, GPIO.OUT)

try:
    while True:
        num = input("Type a number from 0 to 255: ")
        try:
            num = int(num)
            if (0 <= num <= 255):
                GPIO.output (dac, bin_system(num))
                voltage = float(num) / 256 * 3.3
                print (f"Output voltage is about {voltage:.4} volt")
            else:
                if (num < 0):
                    print ("Number have to be >= 0! Try again...")
                else:
                    print ("Number is out of range [0, 255]! Try again...")
        except Exception:
            if (num == 'q'):
                break
            print ("You have to type a number, not string! Try again...")

finally:
    GPIO.output (dac, 0)
    GPIO.cleanup ()
    print("EOP")