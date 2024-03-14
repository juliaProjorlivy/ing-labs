import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
pin = 25
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, 60)

p.start(0)
try:
    while (1):
        freq = int(input("Enter fill coef\n"))
        try:
            p.ChangeDutyCycle(freq)
            print("Assumed V = ","{:.2f}".format(3.3 * (freq/100)),"\n")
        except Exception:
            print("Something went wrong\n")
            
finally:
    p.stop()
    GPIO.output(pin, 0)
    GPIO.cleanup()