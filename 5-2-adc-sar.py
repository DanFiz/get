import RPi.GPIO as gpio
from time import sleep
gpio.setmode(gpio.BCM)
dac = [8, 11, 7, 1, 0, 5, 12,6]
comp = 14
troyka = 13
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka,gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

def perev(a):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]

def adc():
    k=0
    for i in range(7, -1, -1):
        k+=2**i
        gpio.output(dac, perev(k))
        sleep(0.1)
        if gpio.input(comp)==gpio.HIGH:
            k-=2**i
    return k

try:
    while True:
        i=adc()
        if i!=0:
            if i != None:
                print(i, '{:.2f}v'.format(3.3*int(i)/256))
            else:
                print(255, 3.28)
        
finally:
    gpio.output(dac, 0)
    gpio.cleanup()
