import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
leds = [2,3,4,17,27,22,18,9]
aux = [21,20,26,16,19,25,23,24]
for i in leds:
    gpio.setup(i, gpio.OUT)
    gpio.output(i, 1)
for i in aux:
    gpio.setup(i, gpio.IN)
while True:
    for i in range(len(leds)):
        if gpio.input(aux[i]) == 0:
            gpio.output(leds[i], 0)
        else:
            gpio.output(leds[i], 1)

