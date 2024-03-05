import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
leds = [2,3,4,17,27,22,18,9]
for i in leds:
    gpio.setup(i, gpio.OUT)
    gpio.output(i, 0)

'''for i in leds:
    gpio.output(i, 1)'''

for _ in range(3):
    for i in leds:
        gpio.output(i,1)
        time.sleep(0.2)
        gpio.output(i,0)


for i in leds:
    gpio.output(i, 0)

gpio.cleanup()

    