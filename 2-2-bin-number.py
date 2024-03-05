import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
dac = [8,11,7,1,0,5,12,6]
number = [0,0,0,0,0,0,1,0]
'''a = input()
for  i in a:
    number.append(int(i))'''

for i in dac:
    gpio.setup(i, gpio.OUT)
    gpio.output(i, 0)

for i in range(len(dac)):
    print(i)
    if i == 0:
        print('True')
        gpio.output(8, 0)
    gpio.output(dac[i], number[i])
time.sleep(10)
for i in dac:
    gpio.output(i, 0)
gpio.cleanup()
