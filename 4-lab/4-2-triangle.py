import RPi.GPIO as GPIO
import time

def to_bin(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT)


try:
    period = float(input("Enter a period\n"))
    while (1):
        try:
            for i in range(256):
                signal = to_bin(i)
                GPIO.output(dac, signal)
                time.sleep(period/510)
        except Exception:
            print("Something went wrong\n")
            
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()