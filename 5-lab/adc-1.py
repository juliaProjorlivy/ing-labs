import RPi.GPIO as GPIO
import time

def to_bin(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=1)
GPIO.setup(comp, GPIO.IN)

def adc():
    for i in range(256):
        GPIO.output(dac, to_bin(i))
        time.sleep(0.01)
        if(GPIO.input(comp) == GPIO.HIGH):
            return i
    return 0

try:
    while 1:
        digit = adc()
        print("digit ={}, votage = {:.2f}\n".format(digit, digit * 3.3 / 256))
            
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()