import RPi.GPIO as GPIO

def to_bin(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT)
try:
    while (1):
        try:
            num = input("Enter a number from 0 to 255\n")
            if(num == "q"):
                break
            num = int(num)
            if(num < 0):
                print("Negative number\n")
                break
            if(num > 255):
                print("Incorrect input\n")
                break
            GPIO.output(dac, to_bin(num))
            print("V = ","{:.2f}".format(3.3 * (num/256)),"\n")
        except Exception:
            print("Something went wrong\n")
            
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
