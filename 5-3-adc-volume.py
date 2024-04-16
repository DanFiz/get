import RPi.GPIO as GPIO
import time

def dec2bin(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]

def adc():
    value = 0
    signals = [0] * 8
    for i in range(8):
        signals[i] = 1
        GPIO.output(dac, signals)
        time.sleep(0.001)
        if GPIO.input(comp) == 1:
            signals[i] = 0
        else:
            value += 2**(7-i)
    return value

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13
light = [0] * 8

GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(leds, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        val = adc()
        print("V =", round(int(val) / 255 * 330)/100, "В", end = " ")
        for x in dec2bin(val):
            print(x, end = "")
        print()
        x = round(val/256*8)
        for i in range(1,9):
            if (i-0.5) <= x:
                light[-i] = 1
            else:
                light[-i] = 0
        GPIO.output(leds, light)

        
except KeyboardInterrupt:
    time.sleep(0)
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()