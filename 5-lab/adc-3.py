import RPi.GPIO as GPIO
import time

def to_bin(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
led = [2, 3, 4, 17, 27, 22, 10, 9]
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=1)
GPIO.setup(comp, GPIO.IN)

def adc():
    bin = [0 for i in range(8)]
    digit = 0

    for i in range(7, -1, -1):
        bin[i] = 1

        GPIO.output(dac, bin)
        time.sleep(0.001)

        if(GPIO.input(comp) == GPIO.HIGH):
            bin[i] = 0
        digit += bin[i] * (2 ** i)
    return digit

def to_vol(x):
    bin = [0]*8
    for i in range(int((256/8 - x // 8))):
        bin[i] = 1
    return bin

try:
    while 1:
        digit = adc()
        GPIO.output(led, to_bin(digit))
        time.sleep(0.001)
        print("digit ={}, votage = {:.2f}\n".format(digit, digit * 3.3 / 256))
            
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()