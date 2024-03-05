import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(21, gpio.OUT)
gpio.setup(26, gpio.IN)

while True:
    gpio.output(21, gpio.input(26))