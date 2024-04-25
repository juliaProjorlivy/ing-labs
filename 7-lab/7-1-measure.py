import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

def to_bin(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]
            

def adc():
    bin = [0 for i in range(8)]
    digit = 0

    for i in range(7, -1, -1):
        bin[i] = 1

        GPIO.output(dac, bin)
        time.sleep(0.01)

        if(GPIO.input(comp) == GPIO.LOW):
            bin[i] = 0
        digit += bin[i] * (2 ** i)
    return digit


GPIO.setmode(GPIO.BCM)
led = [2, 3, 4, 17, 27, 22, 10, 9]
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(comp, GPIO.IN)

Ts = []
Vs = []

GPIO.output(troyka, 0)

try:
    start_time = time.time()
    GPIO.output(troyka, 0) 
    digit = 0
    while digit < 248:
        digit = adc()
        GPIO.output(led, to_bin(digit))
        Ts.append(time.time() - start_time)
        Vs.append(digit)
        print(digit)
        #time.sleep(0.01)
        ##print("digit ={}, votage = {:.2f}\n".format(digit, digit * 3.3 / 256))

    time_end1 = time.time()
    print("time is {:.2f}".format(time_end1 - start_time))
    print(digit)
    GPIO.output(troyka, 1)
    while digit > 6:
        digit = adc()
        print(digit)
        GPIO.output(led, to_bin(digit))
        Ts.append(time.time() - start_time)
        Vs.append(digit)
        #time.sleep(0.01)
        ##print("digit ={}, votage = {:.2f}\n".format(digit, digit * 3.3 / 256))

    end_time = time.time()
    print("all time = {:.2f}\n".format(end_time - start_time))
    print("one step period = {:.2f}\n".format((end_time - start_time) / len(Ts)))


    plt.plot(Ts, Vs)
    plt.scatter(Ts, Vs, marker=".", color="r")
    plt.show()

    with open("data.txt", "w") as f:
        f.write(str(Vs))
    f.close()

finally:
    GPIO.output(troyka, 0)
    GPIO.output(dac, 0)
    GPIO.cleanup()





