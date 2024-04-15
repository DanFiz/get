import RPi.GPIO as gpio
from time import sleep
gpio.setmode(gpio.BCM)
dac = [8, 11, 7, 1, 0, 5, 12,6]
comp = 14
troyka = 13
leds = [9, 10, 22,27, 17,4, 3, 2]
gpio.setup(dac, gpio.OUT)
gpio.setup(leds, gpio.OUT)
gpio.setup(troyka,gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

def perev(a):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]

def adc():
    k=0
    for i in range(7, -1, -1):
        k+=2**i
        gpio.output(dac, perev(k))
        sleep(0.005)
        if gpio.input(comp)==gpio.HIGH:
            k-=2**i
    return k


def volume(n):
    n=int(round(n/32,0))
    mas=[0]*8
    for i in range(n):
        mas[i]=1
    return mas

try:
    while True:
        k=adc()
        if k!=0:
            gpio.output(leds, volume(k))
            print(int(k)/256*10)

        
finally:
    gpio.output(dac, 0)
    gpio.cleanup()
